---
title: "Java 多型：介面、覆寫與執行時派發"
date: 2023-08-02T07:38:35+08:00
lastmod: 2026-10-07T20:50:40+08:00
description: "用完整 Java 範例理解共同型別、方法覆寫與執行期派發，並區分多型和多載。"
featuredOrder: 1
categories: ["筆記"]
tags: ["Polymorphism", "java"]
toc: true
draft: false
---

用完整 Java 範例理解共同型別、方法覆寫與執行期派發，並區分多型和多載。

<!--more-->

適用：Java 21 標準函式庫；本次以 JDK 25 的 --release 21 編譯，核對輸出。原 OpenJDK 21.0.1 驗證環境保留如下。

當程式要處理不同種類的物件，但它們共享同一組行為時，可以讓呼叫端依賴共同型別，由各個類別提供自己的實作。這篇用動物的 `sound()` 示範 Java 的多型。



## 使用情境與概念

例如有貓與狗，呼叫端都需要讓牠們發出聲音。如果每次都用 `if` 判斷種類，再選擇對應方法，新增種類時就得修改呼叫邏輯。

可以先定義共同的 `Animal` 型別，再讓 `Cat` 與 `Dog` 覆寫 `sound()`。呼叫 `animal.sound()` 時，Java 依物件在執行期的實際類別選擇方法實作。

參考型別決定編譯期可以呼叫哪些方法；實際物件型別決定被覆寫的例項方法會執行哪個版本。

## 驗證環境

- OpenJDK 21.0.1。
- 範例僅使用 Java 標準函式庫，不需要框架或外部依賴。

## 完整範例

將下列程式存為 `PolymorphismDemo.java`。同一個檔案包含共同型別與兩個實作類別，只有入口類別宣告為 `public`。

```java
public class PolymorphismDemo {
    public static void main(String[] args) {
        Animal[] animals = {new Cat(), new Dog()};
        for (Animal animal : animals) {
            animal.sound();
            animal.breathe();
        }
    }
}

abstract class Animal {
    abstract void sound();

    void breathe() {
        System.out.println("Animal breathes");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}
```

執行：

```shell
javac PolymorphismDemo.java
java PolymorphismDemo
```

預期結果：

```text
Cat meows
Animal breathes
Dog barks
Animal breathes
```

兩個物件都透過 `Animal` 參考呼叫。`sound()` 執行各自覆寫的版本，`breathe()` 則使用繼承的共同實作。

## 常見混淆與限制

- **覆寫與多載不同。** 覆寫使用相同方法簽章，由執行期物件決定實作；多載是同名但不同引數的方法，選擇主要依編譯期型別進行。
- **子類別專屬方法不會自動成為共同介面。** 如果 `Cat` 有額外方法，`Animal` 參考不能直接呼叫它；先判斷需求是否真的需要依賴該具體類別。
- **靜態方法與欄位不是這個範例的分派方式。** 本文討論的是被覆寫的例項方法。
- 此範例為概念練習；實際系統也能用介面表達共同契約，選擇繼承或介面取決於是否需要共享狀態與實作。

## 重點回顧

呼叫端用共同型別描述需要的行為，實作類別處理各自細節。重點是共同契約與可替換的實作，而不是只把不同物件放在同一個陣列裡。


- [Oracle Java Tutorials：Polymorphism](https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html)
- [Java Language Specification 21：Method Invocation Expressions](https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html#jls-15.12)
- 原始學習參考：[Polymorphism 影片](https://www.youtube.com/watch?v=tYw-BKKcD3s)、[Java 多型教學](https://www.learnerslesson.com/JAVA/Java-Polymorphism.htm)。上方程式已整理為獨立可執行範例。

## 修訂確認

原有完整範例保留；本文是可控的學習情境，實際系統還需依資料庫延遲與併發負載調整。查核不代表任何引數能直接適用所有 production 服務。

## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

## 參考資料

- [Java 多型：介面、覆寫與執行時派發官方參考](https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html)
- [Java Language Specification 21：Method Invocation Expressions](https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html#jls-15.12)
- [Polymorphism 影片](https://www.youtube.com/watch?v=tYw-BKKcD3s)
- [Java 多型教學](https://www.learnerslesson.com/JAVA/Java-Polymorphism.htm)
