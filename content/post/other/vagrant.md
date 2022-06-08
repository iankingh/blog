---
title: "Vagrant"
date: 2021-03-03T13:45:46+08:00
categories:
 - "筆記"
tags:
 - "vagrant"
toc: true
draft: false
---

## vagrant 使用筆記
<!--more-->
### 初始化虛擬機

```shell
vagrant init
```

### 啟動 虛擬機

```shell
vagrant up 
```

### 啟動 已存在的 虛擬機

```shell
vagrant provision
```

### 停止虛擬機

```shell
vagrant halt
```

### 新增 虛擬主機的 SSL private key 

```shell
vagrant ssh-config
```

### 砍掉 虛擬機

```shell
vagrant destroy
```

## vagrant scp

### 安裝網址

[invernizzi/vagrant-scp: Copy files to a Vagrant VM via SCP.](https://github.com/invernizzi/vagrant-scp)

### Install

```shell
vagrant plugin install vagrant-scp

```

### 使用方法

If you have just a single Vagrant guest, you can copy files over like this:

```
vagrant scp <some_local_file_or_dir> <somewhere_on_the_vm>
```

If you have multiple VMs, you can specify it.

```
vagrant scp <some_local_file_or_dir> [vm_name]:<somewhere_on_the_vm>
```

Copying files out of the guest works in the same fashion

```
vagrant scp [vm_name]:<somewhere_on_the_vm> <some_local_file_or_dir>
```



## Vagrantfile

```vagrantfile
Vagrant.configure("2") do |config|

  #pull images centos/8
  config.vm.box = "centos/8"
  
  #採用橋接，共享主機網絡
  config.vm.network "public_network"
  #虛擬機名字heaton-centos8，內存，核數
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.name= "ian-centos8"
      vb.cpus= 2
    end
end
```

## 參考