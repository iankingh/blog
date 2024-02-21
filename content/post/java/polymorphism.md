---
title: "Polymorphism"
date: 2023-08-02T07:38:35+08:00
categories:
- "筆記"
tags:
- "Polymorphism"
- "java"
toc: true
draft: false
---

# Polymorphism 

<!-- 簡介 -->
<!--more-->

## 前言

Polymorphism中文翻譯為多型

定義為 ：
一個訊息的含義，由訊息接收者所決定，而不是訊息發送者所決定 

### 舉例來說

狗跟貓都是一種動物 但是我們只有在狗跟貓叫的時候才會知道他是給還是貓

以程式碼來說就是在Runtime時才會知道是誰要做動作

### 程式碼的部分

****ex.****

```java
public class Cat extends Animal{

public void sound(){

  System.out.println("Cats Meao");
  }

public void catRelated(){

  System.out.println("It loves sleeping.");
  }
}
```

```java
public class Dog extends Animal{

public void sound(){

  System.out.println("Dog Barks");
  }

public void dogRelated(){

  System.out.println("Very obidient.");
  }
}
```


```java
Class Test{
  public static void main(String[] arg){
  Animal animalCat = new Cat();
  Animal animalDog = new Dog();
  animalCat.sound(); // Calls the sound() behaviour of Cat.
  animalDog.sound(); // Calls the sound() behaviour of Dog.
  animalCat.breathe(); // Calls the breathe() behaviour of Animal.
  animalDog.breathe(); // Calls the breathe() behaviour of Animal.

  }
}

```




## Summary

## 參考

[(68) Polymorphism - YouTube](https://www.youtube.com/watch?v=tYw-BKKcD3s)

https://caterpillar.gitbooks.io/javase6tutorial/content/c8_2.html

https://www.learnerslesson.com/JAVA/Java-Polymorphism.htm