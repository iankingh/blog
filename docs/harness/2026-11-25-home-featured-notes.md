# 首頁文案與置頂筆記驗收

2026-11-25，以 main 的 `cecb1e26` 加上本次首頁與文章差異建置。保留營地插畫與作者的寫作動機，移除重複圖說和卡片連結。三篇置頂筆記各自以文章的 description 提供首頁與搜尋摘要。

| 案例 | 結果 |
| --- | --- |
| Hugo 網站驗證 | `python3 .github/scripts/verify-blog.py` 共 12 項通過。本機 Hugo 0.168.0，CI 固定 0.167.0。 |
| 手機首屏 | 390 × 844 完整顯示第一篇標題，營地橫幅高 120px。320px 寬度無橫向溢出。 |
| 置頂與搜尋 | 三個標題依序連到 Skills 收藏、AI Skills、AI 專案目錄，卡片摘要與搜尋索引一致。 |
| 鍵盤與主題 | Chromium 於 320、390、1440px 的明暗主題共 36 項檢查通過。Tab 每張卡片停一次，標題有可見焦點。 |

本次待發布版本的本機證據在 `/private/tmp/blog-home-publish.ImGBhE/`，網站報告為 `verification/report.json`，瀏覽器結果為 `browser.json`，同目錄包含桌面與手機截圖。行動版以 Chromium 模擬視窗驗收。
