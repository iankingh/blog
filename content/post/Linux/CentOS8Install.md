---
title: "CentOS 8 Install"
date: 2020-06-29T08:51:38+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Linux"
 - "CentOS"
toc: true
---

## CentOS 8 Install
<!--more-->


## Step 1: Download Centos 8

在 CentOS 官方網站 https://www.centos.org/download/ 下載 CentOS 8 ISO 檔案。

CentOS 8 的新特性

- DNF 成為了預設的軟體包管理器，同時 yum 仍然是可用的
- 使用網路管理器（nmcli 和 nmtui）進行網路配置，移除了網路指令碼
- 使用 Podman     進行容器管理
- 引入了兩個新的包倉庫：BaseOS 和 AppStream
- 使用     Cockpit 作為預設的系統管理工具
- 預設使用     Wayland 作為顯示伺服器
- iptables 將被 nftables 取代
- 使用 Linux 核心 4.18
- 提供 PHP     7.2、Python 3.6、Ansible 2.8、VIM 8.0 和 Squid 4

CentOS 8 所需的最低硬體配置:

- 2 GB     RAM
- 64 位 x86 架構、2 GHz 或以上的 CPU
- 20 GB 硬碟空間

## Step 2: Make a bootable device(建立 CentOS 8 啟動介質)

使用 dd建立

```
dd if=CentOS-8-x86_64-1905-dvd1.iso of=/dev/sdb
```



## Step 3:Start with the installation process

當系統從 CentOS 8 ISO 啟動介質啟動之後，就可以看到以下這個介面。

使用 CentOS 8 安裝檔開機會有下述三種模式：

\1.   Install CentOS Linux 8：正常安裝系統流程。

\2.   Test this media & install CentOS Linux 8：測試媒體後在進入安裝系統流程。

\3.   Troubleshooting：進入【除錯模式】，能夠救授 CentOS 系統和執行記憶體測試 (Run a memory test) ...。

選擇“Install CentOS Linux 8.0”（安裝 CentOS Linux 8.0）選項。



![image-20200628221546004](C:\Users\Ian\AppData\Roaming\Typora\typora-user-images\image-20200628221546004.png)

再選擇





## Step 4: Choose the language for the installation process

 第四步：選擇系統語言

選擇想要在 CentOS 8 安裝過程中使用的語言，然後繼續。



![image-20200628221723578](C:\Users\Ian\AppData\Roaming\Typora\typora-user-images\image-20200628221723578.png)

## Step5 : Select the keyboard language for the installation process



## Step 7: Configure the network and hostname



## **Step 8: Configure the location and the timezone**





## **Step 9: Select the destination for the installation**

磁碟分割與檔案系統

/home、swap 和 / 這三個【掛載點】將來容量有可能會變動，因此【裝置類型】設定為可以彈性增加和減少檔案系統容量的 LVM。

| 磁碟分割建議表 |              |              |                                                              |
| -------------- | ------------ | ------------ | ------------------------------------------------------------ |
| **掛載點**     | **裝置類型** | **檔案系統** | **建議容量**                                                 |
| biosboot       | 標準分割區   | BIOS Boot    | 2MB                                                          |
| /boot          | 標準分割區   | ext4         | 1GB                                                          |
| /home          | LVM          | xfs          | 10GB 以上                                                    |
| swap           | LVM          | swap         | [參考 Red Hat swap 建議](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_storage_devices/getting-started-with-swap_managing-storage-devices#recommended-system-swap-space_getting-started-with-swap) |
| /              | LVM          | xfs          | 剩餘容量                                                     |

 





## Step 10: Choose the partitioning scheme



## **Step 11: Create the mount points**





**Step 12: Select the server environment and the features to install**



**Step 13: Begin the installation**



**Step 14: Create your user account**



**Step 15: Configure the root password**



**Step 16: Reboot and accept the licence agreement**



**Step 17: Log in your new system**



## 安裝 Cockpit

[Cockpit](https://cockpit-project.org/) 是基於 Web 介面的應用程式，可用來管理伺服器並監視和調整系統資源。

如果 CentOS 8 是使用【最小型安裝】Cockpit 須手動安裝：

dnf install -y cockpit

Bash

Copy

設定 Cockpit 開機自動啟用 (enable) 且立即啟用 (--now)：

systemctl enable --now cockpit.socket

Bash

Copy

firewall 預設已允許 cockpit (port 9090)：

firewall-cmd --list-all

Bash

Copy

public (active)

 target: default

 icmp-block-inversion: no

 interfaces: enp0s3

 sources:

 services: cockpit dhcpv6-client ssh



開啟瀏覽器輸入 IP:9090 即可連結到 Cockpit。

## 參考

CentOS 8 安裝圖解 | IT人

https://iter01.com/443455.html

How to Install CentOS 8 (Step by Step with Screenshots)

https://linoxide.com/distros/how-to-install-centos/

CentOS 8 伺服器作業系統安裝和設定 - MIS 腳印

https://www.footmark.info/linux/centos/centos8-installation/