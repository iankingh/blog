---
title: "▶️ YT-Fred 聊 SOLID 設計原則｜五個原則環環相扣：SRP 是前提、OCP 是目標、DIP 是做法，LSP 與 ISP 守住介面（筆記）"
slug: fred-solid-principles
date: 2026-10-20
lastmod: 2026-10-20T21:35:29+08:00
description: "依 Fred 的分享串起 SOLID 五個原則，從業務職責、依賴方向到介面契約，以 JDK 25 範例理解可維護性。"
categories: ["筆記"]
tags: ["軟體設計", "SOLID", "java"]
toc: true
draft: false
---

SOLID 五個原則可以放在同一個問題下理解：需求改變時，怎麼讓修改停留在合理的範圍？這篇依 Fred 的分享，從業務職責談到元件依賴，再用一個可執行的發票儲存範例，整理介面與契約的作用。

<!--more-->

適用：已接觸物件導向、介面與後端服務，想把 SOLID 用在日常重構與程式審查的工程師。Java 範例使用 JDK 25 與標準函式庫，不需要 Spring 或雲端帳號。

## 這部影片是什麼

### 來源：[Fred聊聊SOLID設計原則](https://www.youtube.com/watch?v=e0UOuQ_lCUY)

- **背景**：講者在幫公司技術團隊準備內部培訓課，把 Uncle Bob（Robert C. Martin）從 1980 年代到 2017 年《Clean Architecture》和之後的文章都讀過一遍，整理成這場分享。投影片做了大約三週 [1:48:47](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=6527s)。
- **想回答的問題**：為什麼很多人覺得 SOLID 很淺（例如 SRP 只是「一個類別做一件事」、LSP 只是長方形和正方形），但讀《Clean Architecture》的 SOLID 章節時卻看不懂 Uncle Bob 想表達什麼？[2:38](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=158s)
- **核心觀點**：SOLID 的原始描述和 Uncle Bob 後來的「擴充闡述」差很多；後來的版本把五個原則提升到架構層次，而且五個原則**環環相扣**，不是照字母順序各自獨立。
- **講解順序**：SRP → OCP → DIP → LSP → ISP（依原則之間的關聯排，不照 SOLID 字母順序）[58:27](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=3507s)。
- **適合誰**：寫過幾年後端、聽過 SOLID 但覺得「知道定義、不知道怎麼用」的工程師；正在讀《Clean Architecture》的人。
- **注意事項**：這是直播錄影，口語化、有一些停頓；例子多半來自支付、電商、會員系統（使用者服務、信用卡綁定、對帳檔、發票匯出）。講者提到投影片是公司夥伴專屬，影片沒有附投影片。

講者為 **Fred（林世鵬）**。本文依既有影片筆記整理；章節時間沿用原筆記，未重新逐段觀看影片核對。下方 Java 程式為重新撰寫的教學範例，不是講者的原始碼。

## 五個原則如何連在一起？

影片採用 SRP → OCP → DIP → LSP → ISP 的順序，從修改者與使用者兩個角度整理耦合問題；總結可回看 [1:43:15](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=6195s)。這是一種閱讀路線，不表示五個原則只有單一實現方式。

| 原則 | 在這條閱讀路線中的作用 | 審查時可以問的問題 |
| --- | --- | --- |
| SRP：單一職責 | 釐清元件為誰負責、因何變動 | 哪一群需求提出者會要求修改它？ |
| OCP：開放封閉 | 讓擴充有位置，限制修改影響範圍 | 新需求需要改多少既有業務流程？ |
| DIP：依賴反轉 | 讓高階政策依賴抽象，細節配合契約 | 核心流程是否直接依賴 SDK 或資料庫細節？ |
| LSP：里氏替換 | 約束替代實作的行為 | 換一個實作後，呼叫端原本的假設還成立嗎？ |
| ISP：介面隔離 | 依使用者需要提供合適的介面 | 呼叫端是否被迫知道自己用不到的功能？ |

「SRP 是前提、OCP 是目標、DIP 是做法」有助於記憶；實際設計仍要由變更需求與使用情境判斷，不能只因為多加了介面就認定符合 SOLID。

## 先辨識可維護性的壞味道

影片 [07:43](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=463s) 將敏捷交付與可維護性連在一起：如果每次變更都容易牽動不相干功能，小步交付也會變得昂貴。

| 壞味道 | 可觀察的現象 |
| --- | --- |
| 僵化（Rigidity） | 改一個識別碼格式，許多服務與報表都要一起改 |
| 脆弱（Fragility） | 訂單需求變更，卻讓不相關的日誌或會員功能失效 |
| 難以複用（Immobility） | 想取出一個模組，卻必須連同許多無關依賴一起搬走 |
| 黏滯（Viscosity） | 正常擴充太困難，只能不斷新增特殊旗標與分支 |

它們可以作為重構線索，但仍需要找出實際依賴。介面數量、類別大小或某個關鍵字，不能單獨證明設計好壞。

## SRP：職責要從變更來源判斷

[18:07](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=1087s) 開始的 SRP 討論，不是把每一個動作都拆成一個類別，而是把元件對應的業務關聯方與變更原因說清楚。

例如 `AccountService` 同時負責會員等級、綁定信用卡與報表匯出，不同團隊的需求可能改到同一個狀態欄位。此時問題在於不同業務的規則被綁在一起，不只是方法太多。

可以先畫出需求來源與資料含義：

| 現象 | 需要追問的問題 | 可考慮的調整 |
| --- | --- | --- |
| 同一欄位兼作卡片排序與失效狀態 | 排序與有效性是否會獨立變動？ | 分開表達排序與狀態 |
| 以訂單編號格式推測來源商家 | 外部編號規則變動會影響哪些流程？ | 用明確欄位表示來源 |
| 會員服務直接計算風險分數 | 風控規則由誰維護？是否屬於另一種業務政策？ | 將計算交給具明確職責的元件 |
| 一個服務有 20 個方法 | 是否仍服務同一群需求者，變更與維護成本如何？ | 方法多不代表必須拆成 20 個服務 |

這與 Uncle Bob 在 [The Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) 強調的「依相同或不同變更原因組織程式」相呼應。

實務上可以先問：「這個欄位、類別或服務，是用來處理什麼需求？」回答中出現多個用途時再追問是否會獨立變動，不必把每個「和」都當作違反 SRP 的證據。

## OCP：讓擴充有位置，而不是追求零修改

影片 [44:02](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=2642s) 提到，新增會員折扣時，若所有規則都寫進同一串條件分支，新增需求會反覆修改既有流程。策略介面是一種可能的擴充點。

擴充仍可能需要新增設定、組裝實作或調整政策；目標是讓變更發生在合理的位置，而不是宣稱系統從此沒有任何程式碼需要修改。

例如報表原本只輸出網頁，之後要支援列印版，若計算與格式化分開，新增輸出方式就不必重新修改核心計算。這種元件邊界比「每個類別都建立一個介面」更重要。

原則也有成本：不確定的未來需求不值得無限制抽象。先選定已知或合理預期的變化點，再用測試確認既有行為沒有被破壞。

## DIP：分清控制流與原始碼依賴

影片 [58:27](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=3507s) 用發票匯出說明依賴反轉。如果匯出服務直接建立 S3 client、設定 SDK 引數並上傳檔案，核心流程就同時知道了儲存供應商的細節。

可以改成：

```text
執行時的控制流：匯出服務 → 儲存實作
原始碼的依賴：匯出服務 → 業務儲存介面 ← 儲存實作
```

介面描述業務需要的能力，由應用／業務邊界持有；儲存 adapter 實作這個契約。更換 SDK 時，變更可以集中在 adapter 與組裝位置。

依賴注入是把實作交給使用者的組裝方式，DIP 則關心依賴方向；使用某個 DI 框架並不會自動消除對具體細節的依賴。

### JDK 25 完整範例：匯出流程只依賴所需能力

將程式存為 `SolidInvoiceDemo.java`。這個範例將「儲存」與「讀取」分成兩個角色介面，使用記憶體 adapter 模擬儲存空間；**不連 S3、不寫入真實發票，也不提供 HTTP 下載功能**。

```java
import java.util.HashMap;
import java.util.Map;

public class SolidInvoiceDemo {
    record InvoiceFile(String id, String text) {
        InvoiceFile {
            if (id == null || id.isBlank() || text == null) {
                throw new IllegalArgumentException("invalid invoice");
            }
        }
    }

    // 契約：成功時保存原內容並回傳非空 key，可覆寫同一 id。
    interface InvoiceWriter {
        String save(InvoiceFile file);
    }

    interface InvoiceReader {
        String read(String key);
    }

    static final class InvoiceExportService {
        private final InvoiceWriter writer;

        InvoiceExportService(InvoiceWriter writer) {
            this.writer = writer;
        }

        String export(String id, String text) {
            return writer.save(new InvoiceFile(id, text));
        }
    }

    static final class MemoryInvoiceStore
            implements InvoiceWriter, InvoiceReader {
        private final String prefix;
        private final Map<String, String> files = new HashMap<>();

        MemoryInvoiceStore(String prefix) {
            this.prefix = prefix;
        }

        public String save(InvoiceFile file) {
            String key = prefix + "/" + file.id();
            files.put(key, file.text());
            return key;
        }

        public String read(String key) {
            if (!files.containsKey(key)) {
                throw new IllegalArgumentException("missing invoice");
            }
            return files.get(key);
        }
    }

    public static void main(String[] args) {
        for (String prefix : new String[] {"memory-a", "memory-b"}) {
            var store = new MemoryInvoiceStore(prefix);
            var service = new InvoiceExportService(store);
            String key = service.export("INV-001", "amount=100");
            if (key.isBlank() || !store.read(key).equals("amount=100")) {
                throw new AssertionError("save contract violated");
            }
            service.export("INV-001", "amount=200");
            if (!store.read(key).equals("amount=200")) {
                throw new AssertionError("overwrite contract violated");
            }
            System.out.println(prefix + ": amount=200");
        }
        try {
            new InvoiceFile("", "amount=100");
            throw new AssertionError("blank id accepted");
        } catch (IllegalArgumentException expected) {
            System.out.println("invalid invoice: rejected");
        }
    }
}
```

以 JDK 25 原生編譯並執行：

```shell
javac -encoding UTF-8 SolidInvoiceDemo.java
java SolidInvoiceDemo
```

預期輸出：

```text
memory-a: amount=200
memory-b: amount=200
invalid invoice: rejected
```

本次使用 OpenJDK 25.0.4.1，編譯產物為 class major version 69。兩個測試設定使用同一個 adapter 類別，只用來驗證輸出、覆寫與無效輸入；不是兩種雲端供應商相容性的證明。這個記憶體實作不持久化，也不支援並行存取，不可直接當成正式儲存服務。

範例裡，匯出服務只接收 `InvoiceWriter`。讀取端可另外接收 `InvoiceReader`；adapter 同時實作兩者，不表示每個使用者都必須依賴完整的儲存介面。

## LSP：替換時要守住行為契約

影片 [1:16:14](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=4574s) 從繼承談到可替換性。重點不只是方法簽章相同，而是呼叫端依賴的行為仍然成立。

以儲存介面為例，應先約定：成功是否代表內容已可讀取？相同 key 是覆寫還是衝突？失敗用什麼方式回報？如果其中一個 adapter 只排入非同步佇列就回報完成，呼叫端卻期待立刻讀到內容，即使型別相容，也不符合這份契約。

**工程補充：** Liskov 的替代性關注程式可觀察的行為與假設；通常還需檢查前置條件、後置條件、例外及狀態限制。不能只因為有共同介面就推論所有實作可互換，見 [Data Abstraction and Hierarchy](https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf)。

這個觀點也能協助思考 API 相容性，但「升級 API 必須另開一支」不是所有情況的唯一規則。應先分辨相容的擴充與行為破壞；需要破壞性變更時，再決定版本、遷移與相容期。

如果只是想重用一段程式，不必直接建立深層繼承；組合常能減少對父類別內部細節的依賴。既有的 [Java 多型筆記]({{< ref "post/java/polymorphism.md" >}}) 可以對照型別分派與行為契約的差異。

## ISP：依使用者角色設計介面

影片 [1:31:22](https://www.youtube.com/watch?v=e0UOuQ_lCUY&t=5482s) 用印表機的多功能工作介面說明：只需要列印的呼叫方，不應因掃描、裝訂等無關功能而承擔額外依賴。

在發票範例中，匯出端只需要 `save`；若要求它依賴一個包含查詢、刪除、權限設定、同步、備份等方法的大介面，就會增加不必要的知識與維護成本。

SRP 與 ISP 互相呼應，但觀察位置不同：SRP 看元件的變更來源，ISP 看某個使用者究竟需要哪些能力。拆出角色介面後，也要檢查背後的實作是否仍把不相干政策混在一起；介面分開不代表實作完全沒有耦合。

## 把五個原則用在程式審查

| 檢查順序 | 先找的證據 | 可採取的下一步 |
| --- | --- | --- |
| SRP | 多個業務方反覆修改同一欄位或類別 | 釐清資料含義與責任邊界 |
| OCP | 每新增一個情境都要改許多舊流程 | 找出穩定流程與已知變化點 |
| DIP | 業務流程直接 import 外部 SDK | 定義業務介面，把技術細節移到 adapter |
| LSP | 呼叫端針對不同實作寫特例 | 寫清契約，讓實作共用行為測試 |
| ISP | 呼叫端被迫理解許多不使用的方法 | 依角色拆介面，縮小依賴 |

可以先從一段與外部儲存 SDK 綁在一起的服務開始：寫出目前行為測試、說清變更原因，再逐步移動依賴。保留必要的簡單重複，往往比過早建立一個萬用父類別容易維護。

若想用活動系統練習，可搭配 [那些年我們實作過的抽獎系統]({{< ref "post/system-design/▶️ YT-Fred 那些年我們實作過的抽獎系統｜Will 保哥 × Fred：機率設計五個維度、大獎不靠機率、Redis 扣庫存與壓測（筆記）.md" >}})，辨識資格判斷、獎項選取、庫存與發獎的不同責任。這是本文延伸練習，不是講者或特定公司的面試題。

## 參考資料

- [Robert C. Martin：The Single Responsibility Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)
- [Robert C. Martin：The Open-Closed Principle](https://blog.cleancoder.com/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html)
- [Robert C. Martin：Solid Relevance](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
- [Barbara Liskov：Data Abstraction and Hierarchy](https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf)
- [原影片：Fred聊聊SOLID設計原則](https://www.youtube.com/watch?v=e0UOuQ_lCUY)
- [Manifesto for Agile Software Development](https://agilemanifesto.org/)
- [Dan North：Why Every Element of SOLID is Wrong!](https://speakerdeck.com/tastapod/why-every-element-of-solid-is-wrong)：原筆記列出的對照觀點。
