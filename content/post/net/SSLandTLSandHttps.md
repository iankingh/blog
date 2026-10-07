---
title: "SSL、TLS 與 HTTPS：憑證、握手和驗證限制"
date: 2020-12-23T11:38:01+08:00
draft: false
categories:
 - "筆記"
tags:
 - "SSL"
 - "TLS"
toc: true
description: "修正鎖頭代表網站可信的說法，區分加密、憑證與應用安全，補上排錯順序。"
lastmod: 2026-10-07T20:50:40+08:00
---

修正鎖頭代表網站可信的說法，區分加密、憑證與應用安全，補上排錯順序。

<!--more-->

適用：IPv4／IPv6與一般開發網路診斷。平臺專用命令按本文標示的OS使用，不混用Linux與Windows引數。

## 三個名稱

SSL是舊協定名稱，SSL2/3已不適合作現代連線；TLS是後續安全傳輸協定，常見TLS1.2/1.3。HTTPS是在安全傳輸上的HTTP，HTTP/1.1或HTTP/2通常用TCP+TLS，HTTP/3使用QUIC，不能把所有HTTPS簡化為同一個TCP握手。

憑證證明特定身份／網域與公鑰之間的關聯，不證明網站內容誠實或不存在漏洞。瀏覽器安全標記表示連線相關狀態，釣魚站也可能有有效HTTPS。

## 握手與信任

client/server協商協議與演算法，完成必要身份驗證與金鑰協商，再以對稱保護應用資料。TLS1.3不使用舊RSA靜態金鑰交換，不能描述成所有資料都直接用證書公鑰加密。數位簽章與加密的目的不同。

驗證包括hostname/SAN、有效時間、信任鏈與相關用途／撤銷策略。自簽憑證可在受控環境建立明確信任，但沒有公開CA預設信任；不能以關閉驗證代替配置可信根。

## 本機排錯流程

用已知且獲授權的站點替換example.com：

```bash
curl -Iv https://example.com/
openssl s_client -connect example.com:443 -servername example.com -verify_hostname example.com -verify_return_error
```

curl應能成功完成驗證並取得HTTP headers；openssl檢查協商版本、chain與驗證結果。OpenSSL信任store可能與OS／瀏覽器不同，錯誤要先確認CA來源。不要用curl -k做正式「通過」証據。

先查主機時間、DNS、SNI、證書鏈與代理，再看TLS版本／cipher與應用HTTP錯誤。鏈缺中繼certificate、hostname不符和HTTP403是不同層問題，增加記憶體或換瀏覽器通常不是針對原因。

## 邊界與延伸

TLS保護傳輸，不保護被盜端點、伺服器內部明文日誌或錯誤的業務授權。憑證續期需部署到真正終止TLS的proxy／server並確認reload生效。HSTS、Cookie Secure、CSP與mixed content是相關Web機制，仍需分別設定和測試。

## 簽章、憑證鏈與自簽情境

憑證含公開金鑰、名稱與簽發資訊；CA 用自己的私鑰對憑證資料簽章，客戶端以簽發者公開金鑰驗證，再沿中繼憑證走到其信任庫中的根。簽章提供完整性與簽發者認證，並非用私鑰把整個網站內容「加密」。伺服器需要證明持有對應私鑰；TLS 1.3 不使用舊式 RSA key exchange 的敘述。

自簽憑證可以加密流量，但沒有預先受信任的鏈，瀏覽器因此警告。內網可使用管理完善的私有 CA，把根依正式流程安裝到受管理設備；本機練習要分開測「信任正確根」與「未知根」，不要以關閉驗證當部署方案。憑證鏈完整仍需核對 hostname／SAN、有效期與撤銷政策。

HTTPS 的信任邊界包含 CA、用戶端信任庫、私鑰保護與終端設備；遇到合法憑證仍不能推定網站內容可信。HSTS 可要求瀏覽器後續使用 HTTPS，但不替代 TLS 配置，也不自行修好應用授權或遭入侵的 endpoint。

原 TCP 三向交握是傳輸連線步驟，TLS 握手在其上協商加密（HTTP/3 則使用 QUIC，不能直接套 TCP 流程）。HTTP 的 request／response 語意與下層安全協商分開看，排錯才知道應查 DNS、路由、TLS 還是 HTTP 狀態。

## 參考資料

- [TLS1.3 RFC8446](https://www.rfc-editor.org/rfc/rfc8446)
- [TLS1.2 RFC5246](https://www.rfc-editor.org/rfc/rfc5246)
- [HTTP3 RFC9114](https://www.rfc-editor.org/rfc/rfc9114)
- [OpenSSL s_client](https://docs.openssl.org/master/man1/openssl-s_client/)
- [HTTPS (HTTP Secure)](https://en.wikipedia.org/wiki/HTTPS)
- [ HTTP protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [chain of trust 機制](https://jennycodes.me/posts/security-ssl-https#chainoftrust)
- [symmetric session key](https://en.wikipedia.org/wiki/Session_key)
- [RFC      6101](https://tools.ietf.org/html/rfc6101)
- [購買 SSL ](https://www.websecurity.digicert.com/zh/tw/ssl-certificate?inid=infoctr_buylink_sslhome)
- [ECC、RSA 或 DSA 的加密選項](https://www.websecurity.digicert.com/zh/tw/security-topics/how-ssl-works)
- [RFC      2246](https://tools.ietf.org/html/rfc2246)
- [RFC      4346](https://tools.ietf.org/html/rfc4346)
- [RFC      5246](https://tools.ietf.org/html/rfc5246)
- [造成加密內容被解密](http://securityalley.blogspot.com/2014/07/ssltls-beast.html)
- [RFC      8446](https://tools.ietf.org/html/rfc8446)
- [HTTP/2](https://zh.wikipedia.org/wiki/HTTP/2)
- [OSI 模型](https://en.wikipedia.org/wiki/OSI_model)
- [簡介 HTTP](https://ithelp.ithome.com.tw/articles/10217426)
- [里氏替換原則](https://ithelp.ithome.com.tw/articles/10192317)
- [依賴反轉原則](https://ithelp.ithome.com.tw/articles/10192844)
- [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [RFC 793 - Transmission Control Protocol（TCP）](https://tools.ietf.org/html/rfc793)
- [Three-way Handshake](https://zh.wikipedia.org/wiki/传输控制协议)
- [超文字傳輸安全協定](https://zh.wikipedia.org/wiki/超文本传输安全协议)
- [SSL/TLS](https://zh.wikipedia.org/wiki/傳輸層安全性協定)
- [Mozilla CA Certificate Store](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/)
- [WoSign](https://blog.mozilla.org/security/2016/10/24/distrusting-new-wosign-and-startcom-certificates/)
- [中國官方的CA, CNNIC](https://blog.mozilla.org/security/2015/04/02/distrusting-new-cnnic-certificates/)
- [上一篇文](https://jennycodes.me/posts/security-ssh#sshvsssl)
- [POODLE](https://en.wikipedia.org/wiki/POODLE)
- [DROWN](https://drownattack.com/)
- [數位憑證認證機構，簡稱 CA](https://en.wikipedia.org/wiki/Certificate_authority)
- [chain of trust](https://en.wikipedia.org/wiki/Chain_of_trust)
- [OpenSSL](https://www.openssl.org/)
- [SSH 與 OpenSSH](https://jennycodes.me/posts/security-ssh#openssh)
- [網站下載](https://www.openssl.org/source/)
- [s_client 的 man page](https://www.openssl.org/docs/man1.0.2/man1/openssl-s_client.html)
- [https://medium.com/starbugs/security-ssl-https-%E8%83%8C%E5%BE%8C%E7%9A%84%E5%8A%9F%E8%87%A3-df714e4df77b](https://medium.com/starbugs/security-ssl-https-背後的功臣-df714e4df77b)
- [原始參考入口 1](https://ithelp.ithome.com.tw/articles/10193095)
- [原始參考入口 2](https://support.unethost.com/index.php?rp=/knowledgebase/82/SSLSSL-certificate.html)
- [原始參考入口 3](https://tw.alphacamp.co/blog/http-https-difference)
- [原始參考入口 4](https://ithelp.ithome.com.tw/articles/10219106)
- [原始參考入口 5](https://www.netadmin.com.tw/netadmin/zh-tw/technology/6F6D669EB83E4DC9BEA42F1C94636D46)
