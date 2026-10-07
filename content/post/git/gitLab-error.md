---
title: "GitLab 認證失敗：HTTPS 憑證與 SSH 診斷"
date: 2020-05-15T16:36:13+08:00
draft: false
categories:
 - "筆記"
tags:
 - "git"
 - "gitLab"
toc: true
description: "補上 token、認證快取與 SSH 的核對順序，區分 401、403、憑證和網路問題。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上 token、認證快取與 SSH 的核對順序，區分 401、403、憑證和網路問題。

<!--more-->

適用：GitLab 的 HTTPS／SSH clone 與 fetch；GitLab.com 與自架版本的政策可能不同。

## HTTPS 診斷順序

1. 用 `git remote -v` 確認 repository URL，排除舊網域與拼字。
2. 在瀏覽器確認帳號對專案有存取權，private 專案不一定把不存在與無許可權分開顯示。
3. 若啟用 2FA 或伺服器禁密碼認證，以有效 token 按該 GitLab 版本檔案提供；clone/fetch 與 push 所需 scope 不同。
4. 檢查 token 是否過期、撤銷，以及 Windows Credential Manager / Git credential helper 是否仍儲存舊憑證。

```bash
git config --show-origin --get-all credential.helper
git ls-remote origin
```

成功應列出 refs；命令不會下載工作目錄。不要將 token 放 remote URL、提交檔案或公開日誌。憑證更新後只移除對應主機的舊專案，不清除全部個人憑證。

## SSH 與其他問題

GitLab.com 可用 `ssh -T git@gitlab.com` 測認證；自架用實際 hostname 與 port。首次連線核對官方或管理員提供的 host fingerprint，不能直接忽略。SSH 成功不等於對所有專案有寫入許可權。

401 多為認證，403 可能為許可權／政策，TLS 錯誤先查時間、CA 與代理，連線逾時查DNS、port及VPN；不要以 `http.sslVerify=false` 躲過憑證驗證。

確認修復用原 repository 的 ls-remote/fetch；若只是讀許可權測試，不為驗證而建立無意義提交或 push。

## 參考資料

- [GitLab Token](https://docs.gitlab.com/user/profile/personal_access_tokens/)
- [GitLab SSH](https://docs.gitlab.com/user/ssh/)
- [Git 憑證](https://git-scm.com/docs/gitcredentials)
- [在gitlab 遇到fatal: Authentication failed for.... 的問題 | Frank的探索之旅 - 點部落](https://dotblogs.com.tw/zeroade/2018/10/11/111941)
