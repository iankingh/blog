---
title: "VS Code Remote SSH：連線、遠端資料夾與 Vagrant"
date: 2021-02-08T11:11:01+08:00
aliases:
 - "/post/visual-studio-code/vscodeuaeremote/"
draft: false
categories:
 - "筆記"
tags:
 - "Remote"
 - "Visual Studio Code"
toc: true
description: "補齊原測試章節，以示例主機取代真實公網地址，說明遠端server與extension範圍。"
lastmod: 2026-10-07T00:01:00+08:00
---

補齊原測試章節，以示例主機取代真實公網地址，說明遠端server與extension範圍。

<!--more-->

適用：VS Code Remote-SSH與受支援遠端OS；先能用標準SSH成功登入。

## SSH 設定

建立合法可測的Linux主機與一般帳號，在~/.ssh/config加入（替換example地址及key為自己擁有的值）：

```sshconfig
Host note-lab
    HostName 192.0.2.10
    User developer
    Port 22
    IdentityFile ~/.ssh/note_lab_key
    IdentitiesOnly yes
```

192.0.2.10是文件專用地址，不是實際可連線VM。先`ssh note-lab`核對host fingerprint與認證，看到遠端shell後再進VSCode。私鑰限制許可權、不上傳repo；passphrase與ssh-agent可依團隊策略配置。

## VS Code 接線

安裝Microsoft Remote-SSH，命令面板執行Remote-SSH: Connect to Host，選擇note-lab。首次會在遠端安裝匹配的VSCode Server，需網路／磁碟／支援OS。Open Folder選遠端專案，左下連線狀態和終端hostname應為遠端。

部分extension在本機、部分在remote，按照extension職責安裝，不假設本機JDK／Node會用於遠端build。在遠端終端執行該專案build、編輯一個測試檔確認實際儲存位置。

## Vagrant 與排錯

在Vagrant專案執行`vagrant ssh-config`取得實際HostName、Port與IdentityFile，再複製成SSH別名；它不會建立SSL私鑰。VM重建可能改變key／port，要重新核對配置。

不能連線先看Remote-SSH輸出與普通ssh-v日誌（去掉秘密），區分網路、認證與server安裝階段。舊CentOS系統可能不滿足當前server的glibc／庫要求，依官方支援矩陣升級或採用適合的環境，不盲目裝相容補丁。

埠forward用於本地檢視遠端服務時限制loopback，未要求分享就不公開。結束close remote connection，別把本機目錄／remote目錄混作同一工作樹。

## 查核範圍

官方文件／原廠入口與規格查核，程式碼和內部連結完成靜態檢查；需特定平台、帳號、服務或叢集的步驟未實機執行，文內列出讀者確認方式。詳細紀錄見[逐篇查核紀錄]({{< ref "/note-review.md" >}})。

## 參考資料

- [Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
- [Remote troubleshooting](https://code.visualstudio.com/docs/remote/troubleshooting)
- [Vagrant ssh-config](https://developer.hashicorp.com/vagrant/docs/cli/ssh_config)

### 原始筆記保留的來源

- [Remote - SSH](https://code.visualstudio.com/docs/remote/remote-overview)
- [ssh client](https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client)
- [vscode remote vagrant ssh](https://code.visualstudio.com/blogs/2019/07/25/remote-ssh)
- [使用VSCode Remote透過 SSH 進行遠端開發 - HackMD](https://hackmd.io/@brick9450/vscode-remote)
