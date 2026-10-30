---
title: "npm 設定筆記：omit-lockfile-registry-resolved"
date: 2026-10-30T23:33:35+08:00
lastmod: 2026-10-30T23:33:35+08:00
description: "用 .npmrc 的 omit-lockfile-registry-resolved 省略 npm 鎖檔中的 registry 下載網址，整理設定方式、鎖檔差異、換源情境與安裝取捨。"
categories:
  - "技術"
tags:
  - "Node.js"
  - "npm"
toc: true
draft: false
---

在專案的 `.npmrc` 加上這一行，npm 寫入鎖檔時就會省略 **registry 套件的 `resolved` 欄位**：

```ini
omit-lockfile-registry-resolved=true
```

後續安裝時，npm 再向目前設定的 registry 查詢該版本的套件下載位置，因此安裝可能花更久。這是 npm 的設定，通常與 Node.js 開發環境一起使用。[官方選項說明](https://docs.npmjs.com/cli/v11/using-npm/config/#omit-lockfile-registry-resolved)

<!--more-->

適用：使用 npm 與 `package-lock.json` 管理依賴的專案。本文依 npm 11 官方文件說明，操作案例使用 Node.js 26.13.0／npm 11.20.0；其他 npm 版本先確認是否支援此選項。

## 設定放在哪裡

把設定加進專案根目錄的 `.npmrc`，與 `package.json` 放在同一層：

```text
my-project/
├── .npmrc
├── package.json
└── package-lock.json
```

在該目錄執行下列命令，確認 npm 讀到的有效值：

```bash
npm --version
npm config get omit-lockfile-registry-resolved
```

第二個命令預期輸出 `true`；這個選項的預設值是 `false`。

專案 `.npmrc` 適合跟著版本控制一起保存，讓團隊與 CI 使用相同設定。寫在使用者的 `~/.npmrc` 會影響該使用者執行的其他專案；專案設定只適用於該專案，執行 `npm install -g` 時不會讀取它。命令列或環境變數也可能覆蓋檔案設定。[`.npmrc` 官方說明](https://docs.npmjs.com/cli/v11/configuring-npm/npmrc/)

## 鎖檔會有什麼差異

`package-lock.json` 中，registry 套件的 `resolved` 通常是套件壓縮檔，也就是 tarball 的下載網址。以下只示意單一套件紀錄，`integrity` 的省略內容不能拿來當實際雜湊值。

啟用前：

```json
{
  "node_modules/example-package": {
    "version": "1.0.0",
    "resolved": "https://registry.example.com/example-package/-/example-package-1.0.0.tgz",
    "integrity": "sha512-..."
  }
}
```

啟用後：

```json
{
  "node_modules/example-package": {
    "version": "1.0.0",
    "integrity": "sha512-..."
  }
}
```

| 欄位 | 用途 | 啟用後 |
| --- | --- | --- |
| `version` | 記錄鎖定的套件版本 | 保留 |
| `resolved` | 記錄套件取得位置 | 省略 registry 依賴的這個欄位 |
| `integrity` | 校驗下載內容的完整性 | 保留 |

版本仍由鎖檔記錄；若下載內容與既有 `integrity` 不符，安裝仍會失敗。這個開關只針對 registry 依賴，不能據此認為 Git、直接指定 tarball URL 等來源也會全部省略。[鎖檔欄位說明](https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json/)

## 讓既有鎖檔套用設定

修改 `.npmrc` 後，需要讓 npm 重新寫入鎖檔。若這次只想更新鎖檔，可以在專案目錄執行：

```bash
npm install --package-lock-only
git diff -- package-lock.json
```

`--package-lock-only` 用來更新鎖檔，不會把依賴安裝進 `node_modules`。這個流程不需要先刪除 `package-lock.json`；保留原檔，才能對照版本與來源欄位的變化。[npm install 官方說明](https://docs.npmjs.com/cli/v11/commands/npm-install/)

檢查差異時，確認預期的 registry `resolved` 已移除，並檢查是否還有版本、依賴結構或鎖檔格式變動。若 `package.json` 已與鎖檔不一致，npm 可能重新解析依賴；不同 npm 版本也可能產生額外差異。

確認後，以鎖檔重新安裝：

```bash
npm ci
```

`npm ci` 會先移除既有的 `node_modules` 再安裝，且不會改寫鎖檔。因此，「改好設定後直接執行 `npm ci`」不會幫既有鎖檔移除 `resolved`；更新鎖檔與依鎖檔安裝是兩個步驟。[npm ci 官方說明](https://docs.npmjs.com/cli/v11/commands/npm-ci/)

完成後，將 `.npmrc` 與檢查過的 `package-lock.json` 一起納入版本控制。

## 什麼情況可以考慮使用

依照「安裝時向目前 registry 查詢下載位置」的行為，當團隊需要讓同一份鎖檔用於不同 registry 或 mirror，且各環境都提供相同套件、版本與內容時，可以考慮這個設定。例如，開發環境與 CI 使用不同的公司套件代理入口。

使用時有幾個取捨：

- **安裝可能變慢**：少了鎖檔中的下載位置，後續安裝需要再向 registry 查詢；實際影響取決於網路與快取。
- **仍需設定正確的來源**：`registry`、scope 對應的 registry、認證與網路都要能正常使用。這個選項本身不會替你切換 registry。
- **新來源必須提供相同內容**：只有套件名稱與版本相同還不夠；若 tarball 內容不同，仍可能出現 `EINTEGRITY`。

另外，npm 對鎖檔中的 `registry.npmjs.org` 原本就有「目前設定的 registry」這個特殊語意。遇到換源問題時，先查看實際 `resolved` 與 registry 設定，再判斷是否需要省略欄位，不能只因鎖檔出現網址就認定一定無法換源。

## 設定後仍有問題時

| 現象 | 檢查方向 |
| --- | --- |
| `npm config get` 仍是 `false` | 確認執行目錄、`.npmrc` 位置，以及命令列／環境變數是否覆蓋設定。 |
| 鎖檔裡還有 `resolved` | 確認已重新寫入鎖檔，再檢查該依賴是否為直接 URL 或其他非 registry 來源。 |
| 安裝仍連到非預期主機 | 檢查有效的 registry、scope 設定、明確 URL 依賴，以及 registry 回傳的 tarball 位置。 |
| 出現 `EINTEGRITY` | 核對下載內容與鎖檔雜湊，確認代理／鏡像提供的檔案；不要直接刪掉 `integrity`。 |

若是 Angular 的 `ERESOLVE` 或 peer dependency 衝突，可接著閱讀 [Angular npm 安裝錯誤：peer dependency 診斷]({{< ref "post/angular/Angular-npm-Error.md" >}})。本設定處理的是鎖檔中的下載位置欄位。

## 參考資料

- [npm config：omit-lockfile-registry-resolved](https://docs.npmjs.com/cli/v11/using-npm/config/#omit-lockfile-registry-resolved)
- [npm：.npmrc 設定檔](https://docs.npmjs.com/cli/v11/configuring-npm/npmrc/)
- [npm：package-lock.json 欄位與格式](https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json/)
- [npm install：更新鎖檔](https://docs.npmjs.com/cli/v11/commands/npm-install/)
- [npm ci：依鎖檔安裝](https://docs.npmjs.com/cli/v11/commands/npm-ci/)
