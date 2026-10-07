---
title: "Vagrant：VM 生命週期、SSH 與共享檔案"
date: 2021-03-03T13:45:46+08:00
categories:
 - "筆記"
tags:
 - "vagrant"
toc: true
draft: false
description: "修正 provision 和 ssh-config 的用途，保留歷史 CentOS box並補上目前選版方法。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正 provision 和 ssh-config 的用途，保留歷史 CentOS box並補上目前選版方法。

<!--more-->

適用：Vagrant2、已安裝且支援主機架構的provider。原CentOS8／VirtualBox示例是歷史環境。

## 選擇 Box

先在官方registry確認publisher、OS、版本與provider。CentOS Linux8已EOL，Apple Silicon也不能預設用x86 VirtualBox box；需選適合架構的provider與box。本篇不虛構一個保證所有平臺可用的box名稱。

Vagrantfile最小骨架（把box換成已核對的實際名稱與版本）：

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "PUBLISHER/BOX_NAME"
  config.vm.box_version = "VERIFIED_VERSION"
  config.vm.hostname = "note-vm"
  config.vm.network "forwarded_port", guest: 8080, host: 18080, host_ip: "127.0.0.1"
end
```

兩個明確佔位不是待補章節，執行前按平臺選定值。原public_network會接主機網路，練習先用NAT與loopback轉發。

## 操作順序

```bash
vagrant validate
vagrant up
vagrant status
vagrant ssh
vagrant halt
vagrant up
```

validate只查Vagrantfile，不下載／啟動；up建立或啟動VM，halt關機但保留磁碟。provision重新執行供應指令碼，不等於「啟動已存在的VM」。ssh-config輸出Host、Port與IdentityFile，不是在建立SSL私鑰。

## 檔案與清理

預設專案目錄可能在guest的/vagrant共享，視provider與設定確認。原vagrant-scp是第三方plugin，安裝前核對維護與相容性，也可用ssh-config配合標準scp／sftp；SSH host key與許可權仍須處理。

destroy刪VM與guest內資料，先複製重要檔案回主機，確認這是自己練習VM。重新up是否能由Vagrantfile/provision恢復可用環境才是可重現性的證據，只有VM開機不算應用驗收。

## 參考資料

- [Vagrant commands](https://developer.hashicorp.com/vagrant/docs/cli)
- [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile)
- [SSH config](https://developer.hashicorp.com/vagrant/docs/cli/ssh_config)
- [Box選擇](https://developer.hashicorp.com/vagrant/docs/boxes)
- [invernizzi/vagrant-scp: Copy files to a Vagrant VM via SCP.](https://github.com/invernizzi/vagrant-scp)
