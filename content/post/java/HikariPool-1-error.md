---
title: "HikariCP 連線逾時：診斷與可重現範例"
date: 2021-05-06T21:18:55+08:00
lastmod: 2026-10-07T20:50:40+08:00
description: "依連線池狀態診斷取得連線逾時，以 H2 範例重現耗盡、釋放與再次取得連線。"
featuredOrder: 2
categories: ["筆記"]
tags: ["java", "連線池"]
toc: true
draft: false
---

依連線池狀態診斷取得連線逾時，以 H2 範例重現耗盡、釋放與再次取得連線。

<!--more-->

適用：本文原有 Java 21 練習環境；HikariCP 範例的第三方版本以文內依賴清單為準。

遇到 `Connection is not available, request timed out after 30000ms`，表示呼叫端在等待期限內沒有從 HikariCP 取得可用連線。先觀察連線的使用情況，再判斷要修程式、查詢或設定。



## 錯誤代表什麼

常見訊息：

```text
java.sql.SQLTransientConnectionException:
HikariPool-1 - Connection is not available, request timed out after 30000ms.
```

`connectionTimeout` 是呼叫 `getConnection()` 時，等待從連線池取得連線的最長時間，單位為毫秒。**它不是 SQL 查詢的執行逾時。** 查詢執行很久，可能因為長時間佔用連線，間接讓其他請求無法取得連線。

HikariCP 的預設值為 30000 ms，最低接受值為 250 ms。提高等待時間只是讓請求等得更久，不能修復連線未歸還、慢查詢或資料庫不可用等根因。

## 建議的診斷順序

1. **觀察連線池。** 檢查使用中與閒置的連線數，以及等待連線的執行緒數。若全部連線長期使用中，再查是哪個工作佔用。
2. **確認生命週期。** JDBC 連線、Statement 與 ResultSet 使用 try-with-resources，交易完成後應歸還連線。不要在取得連線後執行耗時的外部服務呼叫。
3. **查 SQL 與交易。** 看慢查詢、鎖等待、未完成交易與一次讀取過量資料。
4. **檢查資料庫與網路。** 確認資料庫可連線、連線額度、認證與網路是否正常；同時看連線建立失敗的日誌。
5. **再調整容量與等待。** 根據併發需求與資料庫容量評估 `maximumPoolSize`；等待時間應符合請求可接受的時間。增加連線數也可能讓資料庫負擔更重。

`leakDetectionThreshold` 可以協助記錄連線被借出過久的位置，但它不會自動回收該連線，日誌也不必然代表真正的洩漏。

## 設定範例

Spring Boot 使用 HikariCP 的設定位置如下；縮排用空白，所有時間值均為毫秒。這是設定位置示例，應依實際環境量測後調整。

```yaml
spring:
  datasource:
    hikari:
      minimum-idle: 2
      maximum-pool-size: 10
      idle-timeout: 120000
      connection-timeout: 30000
```

下面的 Java 練習刻意使用 **1 條連線與 300 ms 等待**，快速重現問題；與上面的應用設定分開使用。

## 驗證環境與依賴

- OpenJDK 21.0.1。
- HikariCP 7.0.2、H2 2.4.240、SLF4J API 2.0.17。
- H2 使用記憶體資料庫，無需啟動外部資料庫。

Maven dependency 座標：

```xml
<dependencies>
  <dependency>
    <groupId>com.zaxxer</groupId>
    <artifactId>HikariCP</artifactId>
    <version>7.0.2</version>
  </dependency>
  <dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <version>2.4.240</version>
  </dependency>
  <dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>2.0.17</version>
  </dependency>
</dependencies>
```

若直接用 `javac`，把以上三個依賴的 JAR 放在 `lib/`。SLF4J API 沒有 provider 時會輸出提示，但不影響本範例的 JDBC 行為。

## 完整重現範例

存為 `PoolTimeoutDemo.java`：

```java
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLTransientConnectionException;
import java.sql.Statement;

public class PoolTimeoutDemo {
    public static void main(String[] args) throws Exception {
        HikariConfig config = new HikariConfig();
        config.setPoolName("note-demo");
        config.setJdbcUrl("jdbc:h2:mem:pool_demo");
        config.setMaximumPoolSize(1);
        config.setMinimumIdle(1);
        config.setConnectionTimeout(300);
        config.setValidationTimeout(250);

        try (HikariDataSource pool = new HikariDataSource(config)) {
            try (Connection held = pool.getConnection()) {
                long started = System.nanoTime();
                try (Connection unexpected = pool.getConnection()) {
                    throw new AssertionError("應該因為池已耗盡而逾時");
                } catch (SQLTransientConnectionException expected) {
                    long waitedMillis = (System.nanoTime() - started) / 1_000_000;
                    if (waitedMillis < 250) {
                        throw new AssertionError("等待不足 250 ms：" + waitedMillis);
                    }
                    System.out.println("連線被佔用：第二次取得連線逾時");
                }
            }
            // held.close() 已將連線歸還池。
            try (Connection recovered = pool.getConnection();
                 Statement statement = recovered.createStatement();
                 ResultSet result = statement.executeQuery("SELECT 1")) {
                if (!result.next() || result.getInt(1) != 1) {
                    throw new AssertionError("連線釋放後應可執行查詢");
                }
                System.out.println("連線已釋放：再次取得連線並查詢成功");
            }
        }
    }
}
```

macOS／Linux 執行：

```shell
javac -encoding UTF-8 -cp "lib/*" PoolTimeoutDemo.java
java -cp ".:lib/*" PoolTimeoutDemo
```

Windows 的 classpath 分隔符改用 `;`，執行時使用 `java -cp ".;lib/*" PoolTimeoutDemo`。

預期標準輸出：

```text
連線被佔用：第二次取得連線逾時
連線已釋放：再次取得連線並查詢成功
```

第一個 try 區塊借走唯一的連線；第二次取得會等待到期後丟出例外。範例另外確認等待至少 250 ms，避免把立即失敗誤當成等待逾時；這個下限只用於驗證行為，並非效能指標。第一個區塊結束後，連線歸還池，下一次取得就能執行查詢。

## 限制與重點回顧

這個本機練習驗證的是「池內無可用連線」的機制，沒有模擬網路故障、真實服務負載或資料庫鎖等待。H2 查詢成功也不代表正式環境的容量設定適當。

遇到逾時時先找出連線為何無法使用。確認根因後，再評估池大小與等待設定；不要只把等待時間改長。


- [HikariCP 7.0.2：Configuration](https://github.com/brettwooldridge/HikariCP/blob/HikariCP-7.0.2/README.md#frequently-used)
- [H2：Database URL 與 Embedded Mode](https://h2database.com/html/features.html#database_url)
- 原始問題參考：[Stack Overflow：HikariPool connection timeout](https://stackoverflow.com/questions/47758091/hikaripool-1-connection-is-not-available-request-timed-out-after-30000ms-for)。本文已補上獨立重現步驟與限制。

## 修訂確認

原有完整範例保留；本文是可控的學習情境，實際系統還需依資料庫延遲與併發負載調整。查核不代表任何引數能直接適用所有 production 服務。

## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

## 參考資料

- [HikariCP 連線逾時：診斷與可重現範例官方參考](https://github.com/brettwooldridge/HikariCP)
- [HikariCP 7.0.2：Configuration](https://github.com/brettwooldridge/HikariCP/blob/HikariCP-7.0.2/README.md#frequently-used)
- [H2：Database URL 與 Embedded Mode](https://h2database.com/html/features.html#database_url)
- [Stack Overflow：HikariPool connection timeout](https://stackoverflow.com/questions/47758091/hikaripool-1-connection-is-not-available-request-timed-out-after-30000ms-for)
