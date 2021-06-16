---
title: "WindowsInstallWSL"
date: 2021-06-16T17:10:10+08:00
draft: true
categories:
 - "筆記"
tags:
 - "windows"
 - "docker"
toc: true
---

## Windows Install WSL2筆記
<!-- 簡介 -->
<!--more-->

## WSL2 的 Error 0x80370102 解决方案

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

```
bcdedit /set hypervisorlaunchtype auto
```

## WSL2 的 Error 0xc03a001a 解决方案

C:\Users\電腦使用者名稱ㄌ\AppData\Local\Packages

1. 第一步 找到  CanonicalGroupLimited.Ubuntu<br>
   並點選右鍵 -> 內容。

2. 點選「進階」

3. 將「壓縮內容，節省磁碟空間」取消勾選，並按確定。

4. 再一次重新開啟Linux後，錯誤問題就解決了。




## 參考

[wsl2的Error 0x80370102 解决方案 - 知乎](https://zhuanlan.zhihu.com/p/147233604)

[安裝WSL2子系統出現 0xc03a001a錯誤 - 清晨小農夫](https://rdfarm.net/wsl2-error-0xc03a001a/)

[使用 WSL 2 打造優質的多重 Linux 開發環境 | The Will Will Web](https://blog.miniasp.com/post/2020/07/26/Multiple-Linux-Dev-Environment-build-on-WSL-2)

