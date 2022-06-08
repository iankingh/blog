---
title: "Modeify Visual Studio Code Terminal"
date: 2020-05-13T13:40:56+08:00
categories:
 - "筆記"
tags:
 - "Visual Studio Code"
toc: true
draft: true
---

## 有問題再試試看

## 修改 Visual Studio Code Terminal 使用（Zsh）
<!--more-->
有時看到別人Terminal 都很華麗，就想自己是不是也可以這樣做，這樣就可以讓我們的Terminal更加華麗

以下是修改 Visual Studio Code Terminal 使用（Zsh）的方法：

## 安裝需要的Powerline字型

```Shell script
1. git clone https://github.com/powerline/fonts.git --depth=1

2. cd fonts

3. ./install.sh

4. cd ..

5. rm -rf fonts  
```

## 設定

使用Powerlevel9k

```Shell script

1. git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

2. echo 'ZSH_THEME="powerlevel9k/powerlevel9k"' >> ~/.zshrc

3. source ~/.zshrc
```

## 設定VS Code

進入VS Code

進入[manage(喜好設定)]>[setting(設定)]

```json
{
    // 更紗黑體：
    "terminal.integrated.fontFamily": "Sarasa Mono SC",
    "terminal.integrated.fontSize": 14  
}
```

存檔之後你將會看到漂漂der終端機摟

調整前

調整後


## 參考

[Powershell 美化作戰 —— 字型、執行原則和 oh-my-posh | 伊果的沒人看筆記本](https://igouist.github.io/post/2020/08/powershell-beauty/)