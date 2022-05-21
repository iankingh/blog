---
title: "ModifyUbuntuShell"
date: 2020-05-11T13:40:56+08:00
categories:
 - "筆記"
tags:
 - "ubuntu"
toc: true
draft: true
---


# 修改ubuntu Shell 
<!--more-->


Install zsh / oh-my-zsh on Ubuntu
zsh是個很酷的shell，提供高度可自訂化的shell環境，更多詳細訊息請見 zsh官方網站

本篇筆記如何在Ubuntu環境安裝zsh，並使用oh-my-zsh客製化zsh環境，部分指令與OS X上有些許出入，OS X的安裝請見 oh my zsh Github

原始教學參考自 AJ ONeal的YouTube教學影片

Dim Powerline Theme by Howar31

#Requirement
Ubuntu 本篇測試環境Ubuntu Server 12.10
bash 基本知識
例如 pushd、popd、apt-get 等等
vim 基本知識 或其它類似文字編輯器
#Installation
#ZSH

```Shell script
sudo apt-get update && sudo apt-get install -y curl vim git zsh
```
上述指令做了五件事:

更新apt-get
安裝curl
安裝vim
安裝git
安裝zsh
除了zsh是核心之外，其它是在等等過程中會用到的工具，如果系統中原本就已經安裝最新版，則會自動跳過

#Oh My ZSH
一行指令就能裝好
```Shell script

curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | bash

```
很多網站指令後面寫sh，但Ubuntu要改成bash

#Setting Default Shell
將zsh設定為目前使用者的預設shell

```Shell script
sudo chsh -s $(which zsh) $(whoami)
```
$(which zsh) 表示找到zsh的位置

$(whoami) 表示目前使用者

設定好後，可以手動到home的.bashrc看是否設定成功

#Configure ZSH by Oh My ZSH
修改home的.zshrc即可
vim ~/.zshrc
佈景主題修改ZSH_THEME="theme_name"
佈景主題位置在.oh-my-zsh/themes/底下
oh-my-zsh Theme Wiki

在 Ubuntu 18.04 LTS / 16.04 LTS 中安裝使用 Oh-My-Zsh


近期剛重新安裝 Ubuntu 16.04 LTS 系統，當然新的系統要立馬裝上自己慣用的開發環境及軟體，但有些東西久沒用真的都會忘記怎麼設置，於是就有了這篇文章的產生
這篇就來簡單教學如何在新安裝好的環境中安裝好用的 oh-my-zsh，並套用主題
P.S. 經過測試後此步驟在 Ubuntu 18.04 LTS 也適用喔~
基本安裝
首先，在乾淨完整的 Ubuntu 16.04 中，打開終端機 （Ctrl+Alt+t）預設啟用的是我們常見的 Bash Shell
新系統當然要先更新一下
$sudo apt-get update
$sudo apt-get upgrade
接著需要安裝 zsh ，oh-my-zsh 就是基於此 shell 之上運作的

```Shell script
$sudo apt-get install zsh
```

若還沒安裝 git 的也安裝一下

```Shell script
$sudo apt-get install git
```
安裝完後可以輸入指令查看一下是否安裝成功，若出現 /usr/bin/zsh 就是成功了

```Shell script
$cat /etc/shells
```
接著要安裝 oh-my-zsh，可以用 curl 或 wget 兩種方式安裝，選一種安裝即可（如果沒有安裝這兩種工具的也記得安裝一下）
# via curl
```Shell script
$sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
# via wget

```Shell script
$sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```
若安裝完應該會直接進入 oh-my-zsh 的歡迎畫面
到這邊基本安裝已經完成了，但我們要再修改一些配置讓它用起來更方便
修改配置
目前預設開機使用的 Shell 依然是 Bash Shell，要使用 oh-my-zsh 的方式有二
一個是在每次啟動 Terminal 時先輸入 zsh 進入 oh-my-zsh ，但這樣太麻煩了，所以可以輸入這指令修改預設的 Shell
```Shell script
$chsh -s /bin/zsh
```
然後把電腦登出再登入再開啟 Terminal 就可以看到自動進入 oh-my-zsh 了

再來就是要設定我們自己喜歡的主題啦，可以從官方提供的各式主題中自己挑選喜歡的主題使用，但就要自行安裝各主題所需要的套件
官方主題庫
我個人喜歡使用 Bullet train 這款主題，先從 這裡 按右鍵直接儲存連接將主題檔存至電腦上（預設下載至 Download 資料夾，根據個人下載位置修改接下來的指令）
然後將主題檔移動至 oh-my-zsh 的主題資料夾中
# back home folder
```Shell script
$cd
```
# move file
```Shell script
$sudo mv Downloads/bullet-train.zsh-theme .oh-my-zsh/themes/
```
接著用 nano 編輯器開啟 .zshrc 檔進行編輯
```Shell script
$sudo nano .zshrc
```
找到 ZSH_THEME 修改成 “bullet-train”

按下 CTRL+x 接著按 y 儲存離開
重啟 Terminal 應該會看到類似如下畫面

會發現好像出現破圖現象，那是因為少了 Powerline 的字型包
用以下指令安裝
```Shell script
$sudo apt-get install powerline
```
```Shell script
$sudo apt-get install fonts-powerline
```
## 參考
在 Ubuntu 18.04 LTS / 16.04 LTS 中安裝使用 Oh-My-Zsh - Wiffer - Medium  
https://medium.com/@wifferlin0505/%E5%9C%A8-ubuntu-16-04-lts-%E4%B8%AD%E5%AE%89%E8%A3%9D%E4%BD%BF%E7%94%A8-oh-my-zsh-cf92203ca8a2

打造最强终端 - iTerm 2 - 开发工具 - 掘金  
https://juejin.im/entry/5804c81dda2f60004fed51db

Install zsh / oh-my-zsh on Ubuntu | Howar31 Blog  
https://blog.howar31.com/wordpress/install-zsh-oh-my-zsh-on-ubuntu/#requirement