---
title: "VSCodeUaeRemote"
date: 2021-02-08T11:11:01+08:00
draft: false
categories:
 - "筆記"
tags:
 - "Remote"
 - "Visual Studio Code"
toc: true
---

## VSCode 使用 Remote 套件 進行遠端連線開發
<!--more-->

## 前言

有時需要連線到遠端主機，此時使用可以使用 shh 的方式連線過去，但每一次都要輸入連線密碼，且看不到資料夾的狀態， 此時可以用 VS code 安裝

[Remote - SSH](https://code.visualstudio.com/docs/remote/remote-overview)

這一套擴充插件，來進行`SSH`連線。

## 安裝

1. 安裝 [ssh client](https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client)

2. 安裝 visual studio Code

3. 安裝遠程開發擴展包(Remote - SSH )。

在Extension搜尋remote就可以看到了，這邊我們選擇安裝SSH的

## 連線到 Azure

### 設定

按下 `ctrl +shift + p`

open ssh configuration
打開 .ssh\config
設定 remote

```shell
  Host     40.124.99.20
  HostName 40.124.99.20
  User     azureuser
  IdentityFile C:/Users/Ian/azureuser.pem
```

- Host LabServer      # 填寫別名例如 LabSever
- HostName 127.0.0.1  # 主機名稱或是ip位置
- User root           # 登入的使用者名稱
- Port                # 如果有指定的Port號

### 測試連線


## 連線到 vagrant  

到有 `Vagrantfile` 目錄執行

```shell
vagrant ssh-config
```

得到

```shell
  Host ian-centos8
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile "/XXX/private_key"
  IdentitiesOnly yes
  LogLevel FATAL

```

點選對應的 Remote 進行連線

**注：**  感謝 **KFC 前輩**的提供 remote 的方法

## 參考

[vscode remote vagrant ssh](https://code.visualstudio.com/blogs/2019/07/25/remote-ssh)
[使用VSCode Remote透過 SSH 進行遠端開發 - HackMD](https://hackmd.io/@brick9450/vscode-remote



