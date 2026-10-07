---
title: "API 文件工具：OpenAPI、Slate 與 apiDoc 的選擇"
date: 2021-07-20T06:49:34+08:00
categories:
 - "學習"
tags:
 - "API"
toc: true
draft: false
description: "補上契約來源、生成方式與限制，提供最小 OpenAPI 文件。"
lastmod: 2026-10-07T20:50:40+08:00
---

補上契約來源、生成方式與限制，提供最小 OpenAPI 文件。

<!--more-->

適用：HTTP API文件規劃；工具產物不會自動代替後端驗證或契約測試。

## 比較

| 工具 | 輸入來源 | 適合與限制 |
| --- | --- | --- |
| OpenAPI／Swagger UI | 結構化API規格 | 可互動、生成工具；規格仍要與實作一致 |
| Slate | Markdown與範例 | 易寫敘述；不是自動驗證HTTP schema |
| apiDoc | 程式碼註解 | 靠近實作；需維護註解與生成版本 |

OpenAPI是規格，SwaggerUI是呈現與操作工具，兩者不能只當同一產品名稱。Spring的生成整合見[Swagger筆記]({{< ref "/post/spring-boot/spring-boot-Swagger2.md" >}})。

## 最小契約

```yaml
openapi: 3.0.3
info:
  title: 筆記 API
  version: 1.0.0
paths:
  /tasks:
    get:
      summary: 列出任務
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  required: [id, title]
                  properties:
                    id: {type: string}
                    title: {type: string}
```

在相容的OpenAPIvalidator檢查後用檔案工具呈現，應有GET /tasks與回應欄位。此例故意只涵蓋成功清單，沒有分頁／授權；真正API補上錯誤、認證、限制與範例。

## 維護

選擇spec-first或code-first後定義唯一權威來源，CI檢查生成差異與實際響應schema。工具版本鎖定，別在每次build抓latest生成不同檔案。檔案示例用本地假資料，不含真實token／個資；公開範圍與程式原始碼範圍分開考慮。

## 參考資料

- [OpenAPI3.0.3](https://spec.openapis.org/oas/v3.0.3.html)
- [Slate](https://github.com/slatedocs/slate)
- [apiDoc](https://apidocjs.com/)
- [SwaggerUI](https://swagger.io/tools/swagger-ui/)
- [API文件和模擬工具 - HackMD](https://hackmd.io/@YuTingKung/HkrFjefxt#SwaggerHub-API-Auto-Mocking)
- [建立漂亮的靜態 API 文件開源工具 - Soft & Share (softnshare.com)](https://softnshare.com/opensource-slate/)
- [Slate - 為你打造漂亮的 API 文件 | 丸匠筆記 (weijutu.github.io)](https://weijutu.github.io/2018/08/02/tools/slate-api-document/)
