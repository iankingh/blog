---
title: "[從 0 開始的 JAVA 生活]No.3 變數與它的小夥伴們"
date: 2020-06-15T06:20:37+08:00
draft: true
categories:
  - "筆記"
  - "技術"
tags:
 - "java"
toc: true
---


<!-- # [從 0 開始的 JAVA 生活]No.3 變數與它的小夥伴們 -->
<!--more-->

instance variable -

## 變數的種類與有效範圍(Variable Scope)
基本觀念
-區域變數(local variables):
    -區域變數只能在它們被宣告的(method)內存取
    -又稱 automatic , temporary , 或stack variables

-實體變數(insance variables):
    -宣告在(method)之外;(並且沒有static修飾子)
    -實體變數可被類別內的任何非static method 所存取
    -又稱 成員變數 (member variables) ,屬性變數(attribute variables)
-加上static 修飾子的類別變數(class variables)又稱靜態變數(sttic variables)


## 變數的宣告(Declaration)與初始化(Initializtion)
基本觀念
 -變數被使用前須有初值,否則(compile)時會有錯誤
 -基本的宣告方式 :
  <變數型態><變數名稱>;
 EX : int i ;
 -宣告之後,在指定初始值[區域變數]才可以
EX : int i = 0;

-區域變數(local variables):



參考 :




