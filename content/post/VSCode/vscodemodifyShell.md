---
title: "Modeify Visual Studio Code Terminal"
date: 2020-05-13T13:40:56+08:00
categories:
 - "筆記"
tags:
 - "ubuntu"
 - "Visual Studio Code"
toc: true
draft: true
---


## 修改 Visual Studio Code Terminal
<!--more-->

Visual Studio Code Terminal   使用（Zsh）


## 安裝需要的Powerline字型

```Shell script
$git clone https://github.com/powerline/fonts.git --depth=1
$cd fonts
$ ./install.sh
$cd ..
$rm -rf fonts  
```

## 設定Zsh theme

使用Powerlevel9k

```Shell script

$git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
$echo 'ZSH_THEME="powerlevel9k/powerlevel9k"' >> ~/.zshrc
$source ~/.zshrc
```

## 設定VS Code

進入VS Code
進入[喜好設定]>[設定]

```json
{
    // 更黑紗體：
    "terminal.integrated.fontFamily": "Sarasa Mono SC",
    "terminal.integrated.fontSize": 14  
}
```

存檔之後你將會看到漂漂der終端機摟

調整前



調整後





參考
[Powershell 美化作戰 —— 字型、執行原則和 oh-my-posh | 伊果的沒人看筆記本](https://igouist.github.io/post/2020/08/powershell-beauty/)

