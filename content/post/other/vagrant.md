---
title: "Vagrant"
date: 2021-03-03T13:45:46+08:00
draft: false
categories:
 - "筆記"
tags:
 - "vagrant"
toc: true
---

# vagrant 使用筆記
<!--more-->

## 初始化虛擬機
```
vagrant init
```
## 啟動 虛擬機 
```
vagrant up 
```

## 啟動 已存在的 虛擬機

vagrant provision

## 停止虛擬機

```
vagrant halt
```

## 新增 虛擬主機的 SSL private key 
```
  vagrant ssh-config
```

## 砍掉 虛擬機

```
vagrant destroy
```


# vagrant scp  

安裝網址:
https://github.com/invernizzi/vagrant-scp

Install
```
vagrant plugin install vagrant-scp

```

Usage
```

```


# Vagrantfile

```
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