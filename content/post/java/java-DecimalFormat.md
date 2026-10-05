---
title: "Java DecimalFormat：明確控制格式、Locale 與捨入"
date: 2020-05-26T08:59:50+08:00
lastmod: 2026-10-05T21:48:32+08:00
description: "用 Java 21 的完整範例整理 DecimalFormat：0 與 #、千分位、百分比、Locale 以及 BigDecimal 的 HALF_EVEN 與 HALF_UP 捨入結果。"
featuredOrder: 3
categories: ["筆記"]
tags: ["java"]
toc: true
draft: false
---

當 API、報表或畫面需要固定的小數位數與千分位，可以用 `DecimalFormat` 控制呈現。要讓不同電腦產生相同結果，除了 pattern，也需要明確指定 Locale 與捨入方式。

<!--more-->

## 使用情境與適用環境

本文示例在 OpenJDK 21.0.1 執行，僅使用 Java 標準函式庫。選用 `Locale.US`，讓小數點使用 `.`、分組符號使用 `,`。

格式化的結果是字串。資料本身的計算與畫面的輸出格式是兩個步驟，顯示為兩位小數不代表原始數值已改變。

## 常用格式符號

| 符號 | 意義 | 示例 |
|---|---|---|
| `0` | 位數不足時補零 | `000000.000`：`123.78` → `000123.780` |
| `#` | 可省略的數字位置 | `#,##0.###`：`123456.789` → `123,456.789` |
| `.` | pattern 中的小數分隔位置 | 顯示符號由 Locale 決定 |
| `,` | pattern 中的分組位置 | `#,##0.00`：`1234` → `1,234.00` |
| `%` | 格式化前將數值乘以 100，附上百分比符號 | `0.00%`：`0.125` → `12.50%` |

## 完整可執行範例

存為 `DecimalFormatDemo.java`：

```java
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

public class DecimalFormatDemo {
    private static DecimalFormat formatter(String pattern, RoundingMode rounding) {
        DecimalFormat format = new DecimalFormat(
                pattern, DecimalFormatSymbols.getInstance(Locale.US));
        format.setRoundingMode(rounding);
        return format;
    }

    public static void main(String[] args) {
        System.out.println(formatter("#,##0.###", RoundingMode.HALF_EVEN)
                .format(new BigDecimal("123456.789")));
        System.out.println(formatter("000000.000", RoundingMode.HALF_EVEN)
                .format(new BigDecimal("123.78")));
        System.out.println(formatter("0.00%", RoundingMode.HALF_EVEN)
                .format(new BigDecimal("0.125")));
        System.out.println(formatter("0.00", RoundingMode.HALF_EVEN)
                .format(new BigDecimal("2.345")));
        System.out.println(formatter("0.00", RoundingMode.HALF_UP)
                .format(new BigDecimal("2.345")));
    }
}
```

執行：

```shell
javac DecimalFormatDemo.java
java DecimalFormatDemo
```

預期結果：

```text
123,456.789
000123.780
12.50%
2.34
2.35
```

最後兩行使用同一個精確十進位值 `2.345`。在兩位小數的中點，`HALF_EVEN` 選擇最後保留位為偶數的 `2.34`；`HALF_UP` 則得到 `2.35`。`DecimalFormat` 預設使用 `HALF_EVEN`，因此要明確選擇符合需求的規則。

## 為什麼使用 BigDecimal 的字串建構子

`new BigDecimal("2.345")` 保留字串表示的十進位值。`double` 是二進位浮點數，像 `2.345` 這類值可能無法精確表示；將它先轉成 double 再建構 BigDecimal，測試就不再是相同的精確中點。

本文為了展示確定的捨入結果，使用字串建構 BigDecimal。格式化只處理輸出，計算時仍要在適當位置決定精度與捨入規則。

## 限制與常見錯誤

- `Locale.US` 是本文重現結果的選擇；多語系畫面應依目標使用者的 Locale 呈現。
- `DecimalFormat` 不是執行緒安全的物件，不要把單一實例放進多執行緒共用且沒有同步的服務。
- 數值 `0.125` 使用 `%` 會變成 `12.50%`；已經以 `12.5` 表達百分比的資料，不能再套用同樣轉換。
- 把 `$` 寫進 pattern 只會加上字元，不會選擇貨幣或進行匯率轉換。
- 若需要處理輸入字串，`parse()` 的規則與回傳型別也必須另外確認，不能只靠輸出格式推斷。

## 重點回顧

固定 Locale、使用明確的十進位資料與捨入方式，範例才能在不同環境中重現。選好 pattern 之後，再確認百分比、分組符號與多執行緒使用方式是否符合需求。

## 參考

- [Java SE 21：DecimalFormat](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/text/DecimalFormat.html)
- [Java SE 21：BigDecimal](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/BigDecimal.html)
- [Java SE 21：RoundingMode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/math/RoundingMode.html)
- [Oracle Java Tutorials：Customizing Formats](https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html)
