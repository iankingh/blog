---
title: "VSCodeUaeRemote"
date: 2021-02-08T11:11:01+08:00
draft: true
categories:
 - "xx"
tags:
 - "xxx"
 - "xxx"
toc: true
---

# VSCode 使用 Remote 套件 進行遠端連線開發
<!--more-->

## 前言 
有時需要連線到遠端主機，此時使用可以使用 shh 的方式連線過去，但每一次都要輸入連線密碼，且看不到資料夾的狀態， 此時可以用 VS code 安裝
Remote - SSH 
https://code.visualstudio.com/docs/remote/remote-overview

這一套 擴充插件

## 安裝

1.安裝
<a href="https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client" title="ssh client ">
ssh client</a> 

2.安裝Visual Studio Code

3.安裝遠程開發擴展包(Remote - SSH )。

在Extension搜尋remote就可以看到了，這邊我們選擇安裝SSH的


## 設定
按下 ctrl +shift + p 

open ssh confin



```
Host  40.124.99.20
  HostName 40.124.99.20
  User azureuser
  IdentityFile C:/Users/Ian/Desktop/MyGitlab/azureuser.pem
```

Host LabServer             #填寫別名例如 LabSever
    HostName 172.31.00.00  #主機名稱或是ip位置
    User root              #登入的使用者名稱
    Port                   #如果有指定的Port號

## 連線

測試連線



## 連線 vagrant  

到 vagrant 機器 執行
```
vagrant ssh-config

```
得到
```
Host ian-centos8
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile "C:/Users/Ian/Desktop/side project/.vagrant/machines/default/virtualbox/private_key"
  IdentitiesOnly yes
  LogLevel FATAL

```





**注：**  感謝 **KFC 前輩**的提供 remote 的方法

## 參考

https://hackmd.io/@brick9450/vscode-remote


vscode remote vagrant ssh

https://code.visualstudio.com/blogs/2019/07/25/remote-ssh