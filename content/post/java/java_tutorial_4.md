---
title: "Java 入門 04：封裝、繼承與多型"
date: 2021-07-25T20:58:15+08:00
draft: false
categories:
  - "筆記"
  - "技術"
tags:
- "Java"
- "JDK"
toc: true
description: "以技能介面和角色物件示範物件導向，補上可執行程式與設計限制。"
lastmod: 2026-10-07T20:50:40+08:00
---

以技能介面和角色物件示範物件導向，補上可執行程式與設計限制。

<!--more-->

適用：Java 8 基礎語法；新版練習可使用 JDK 21。先安裝 JDK 並瞭解第 0 篇的編譯／執行環境。

## 三個概念放進同一個範例

```java
public class ObjectDemo {
    interface Skill { String use(); }
    static class Heal implements Skill {
        public String use() { return "恢復生命"; }
    }
    static class Fire implements Skill {
        public String use() { return "施放火球"; }
    }
    static class Adventurer {
        private final String name;
        Adventurer(String name) { this.name = name; }
        String perform(Skill skill) { return name + "：" + skill.use(); }
    }
    public static void main(String[] args) {
        Adventurer hero = new Adventurer("Ian");
        System.out.println(hero.perform(new Heal()));
        System.out.println(hero.perform(new Fire()));
    }
}
```

儲存為 ObjectDemo.java，編譯執行：

```text
Ian：恢復生命
Ian：施放火球
```

name 私有且由建構子初始化是封裝；Heal / Fire 實作共同的 Skill 契約；perform 接收 Skill 並呼叫不同實作是多型。Java 類別單一繼承、可以實作多個介面，介面不是建立物件的類別。

## 設計選擇

繼承應符合「是一種」關係，單純想共用幾行程式可以用組合或函式，不必建深層父類別。overload 依編譯時的引數型別選擇方法，override 依執行時物件派發實體方法；欄位與 static 方法不照相同規則派發。更完整對照見多型範例。

Java 8 的基本契約仍適用；新版 record 適合部分不可變資料模型、sealed 可限制繼承範圍，但不改變封裝責任，應在理解基礎後再使用。


先備：[第 03 章]({{< ref "/post/java/java_tutorial_3.md" >}})的基礎概念與已確認的 JDK 編譯環境。

## 系列導覽

[00 環境]({{< ref "/post/java/java_tutorial_0.md" >}}) · [01 第一支程式]({{< ref "/post/java/java_tutorial_1.md" >}}) · [02 型別]({{< ref "/post/java/java_tutorial_2.md" >}}) · [03 變數]({{< ref "/post/java/java_tutorial_3.md" >}}) · [04 物件導向]({{< ref "/post/java/java_tutorial_4.md" >}}) · [多型範例]({{< ref "/post/java/polymorphism.md" >}})

[上一章]({{< ref "/post/java/java_tutorial_3.md" >}}) · [延伸：多型]({{< ref "/post/java/polymorphism.md" >}})

## 參考資料

- [物件導向觀念](https://docs.oracle.com/javase/tutorial/java/concepts/)
- [介面](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html)
