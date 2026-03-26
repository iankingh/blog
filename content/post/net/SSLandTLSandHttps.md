---
title: "SSlAndTLS"
date: 2020-12-23T11:38:01+08:00
draft: false
categories:
 - "筆記"
tags:
 - "SSL"
 - "TLS"
toc: true
---

# SSL、TLS 以及 HTTPS

當我們瀏覽網頁時：網址列的開頭是不是有個 🔒鎖的圖案。

這個鎖代表你現在連線到的網站是安全可信任的。

即使用[HTTPS (HTTP Secure)](https://en.wikipedia.org/wiki/HTTPS) 連線，而不是使用不安全的[ HTTP protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)。

<!--more-->

## SSL憑證(SSL certificate)的原理

SSL 的全名是 **Secure Sockets Layer**，即安全通訊端層，這是一種標準的技術，用於保持網際網路連線安全以及防止在兩個系統之間傳送的所有敏感資料被罪犯讀取及修改任何傳輸的資訊，包括潛在的個人詳細資料。兩個系統可以是伺服器與使用者端 (例如購物網站與瀏覽器)，或者伺服器至伺服器 (例如，含有個人身份資訊或含有薪資資訊的應用程式)。

這樣做是為了確保使用者與網站、或兩個系統之間傳輸的任何資料保持無法被讀取的狀態。此技術可使用加密演算法以混淆輸送中的資料，防止駭客在資料透過連線傳送時讀取資料。此資訊可能是任何敏感或個人資訊，包括信用卡號與其他財務資訊、姓名與地址。

SSL 讓瀏覽器（所謂的 client）要連到一個遠端網站（所謂的 server）之前，先要求這個網站提供身分認證，跟這個網站約定暗號（交換鑰匙），打好交情（建立加密的 session），才會心甘情願地跟這個網站連線。

總共有 三個步驟 1. 建立連線 2. 憑證交換 3. 金鑰交換

步驟如下：

1.1  建立連線  - 客戶端和伺服器官表示想要發起 HTTPS 連線，說明自己支援的 SSL/TLS 版本和加密演算法。伺服器端會回應客戶端說可以使用哪一種組合。瀏覽器對想要連線的網站送出連線請求，同時要求網站驗證自己。

2.1  憑證交換 - 伺服器必須照明_自己是誰_。伺服器會拿出一張憑證，基本上這張憑證記載了伺服器的身份、位置（網址）、憑證的公鑰、有效日期和數位簽章。客戶端會確認是否要相信這張憑證，要麼這張憑證是被設定要信任，要麼這張憑證是由某個信任的機構 (CA) 簽署的。另外，這個機制其實可以雙向使用，伺服器端驗證客戶端的身份，不過這個機制很少用到

2.2  憑證交換 - 網站將自己的 SSL 數位憑證 (SSL certificate) 回傳給 client，裡麵包含了網站的 public key

2.3  憑證交換 - 瀏覽器驗證網站回傳的的 root certificate，透過 [chain of trust 機制](https://jennycodes.me/posts/security-ssl-https#chainoftrust) 確認這個證明檔案是否可以被信認，同時也確認這個憑證是否過期。

3.1  金鑰交換- 當認證透過，瀏覽器會用網站的 public key 建立一個 [symmetric session key](https://en.wikipedia.org/wiki/Session_key)。

3.2  金鑰交換 - 網站用自己的 private key 解讀 session key，並且回傳一個確認訊息，開始一個被 SSL 保護的 session。

3.3  金鑰交換 - 這個 session key 會被用來加密所有之後瀏覽器與網站之間傳送的資料。



### SSL Handshake

在 TCP Three-way Handshake 完成之後，如果 Alice 有希望使用 SSL 加密時就會開始做 SSL Handshake。

時序圖如下：

SSL在傳輸之前事先用來溝通雙方（使用者端與伺服器端）所使用的加密演算法或金鑰交換演算法，或是在伺服器和使用者端之間安全地交換金鑰及雙方的身分認證等相關規則，讓雙方有所遵循。在身分認證方面，SSLHandshake可用來認證伺服器的身分。SSL Handshake的運作流程如下所述：

(1) SSL使用者端利用Client Hello訊息將本身支援的SSL版本、加密演算法、演算法等資訊傳送給SSL伺服器。

(2) SSL伺服器收到Client Hello訊息並確定本次通訊採用的SSL版本和加密套件後，利用Server Hello訊息回覆給SSL使用者端。

(3) SSL伺服器將利用Certificate訊息將本身公鑰的數位憑證傳給SSL使用者端。

(4) SSL伺服器傳送Server Hello Done訊息，通知SSL使用者端版本和加密套件協商結束，並開始進行金鑰交換。

(5) 當SSL使用者端驗證SSL伺服器的證書合法後，利用伺服器的證書中之公鑰加密SSL使用者端隨機生成的Premaster Secret（這是一個用在對稱加密金鑰產生中的46位元組的亂數字），並透過Client Key Exchange訊息傳送給SSL伺服器。

(6) SSL使用者端傳送Change Cipher Spec訊息，通知SSL伺服器後續報文將採用協商好的金鑰和加密套件進行加密。

(7) SSL使用者端計算已互動的握手訊息的Hash值，利用協商好的金鑰和加密演算法處理Hash值，並透過Finished訊息傳送給SSL伺服器。SSL伺服器利用同樣的方法計算已互動的握手訊息的Hash值，並與Finished訊息的解密結果比較，如果兩者相同，則證明金鑰和加密套件協商成功。

(8) SSL伺服器傳送Change Cipher Spec訊息，通知SSL使用者端後續傳輸將採用協商好的金鑰和加密套件進行加密。

(9) SSL伺服器計算已互動的握手訊息的Hash值，利用協商好的金鑰和加密套件處理Hash值，並透過Finished訊息傳送給SSL使用者端。SSL使用者端利用同樣的方法計算已互動的握手訊息的Hash值，並與Finished訊息的解密結果比較，如果兩者相同，且MAC值驗證成功，則證明金鑰和加密套件協商成功。在SSL使用者端接收到SSL伺服器傳送的Finished訊息後，如果解密成功，則可以判斷SSL伺服器是數位證書的擁有者，即SSL伺服器身分驗證成功。這是因為只有擁有私鑰的SSL伺服器才能從Client Key Exchange訊息中解密得到Premaster Secret，從而間接地實現了SSL使用者端對SSL伺服器的身分驗證。



- `SSL 1.0` 是由     Netscape 設計的，但時間不詳。
- `SSL 2.0` 1995 年發布，2011     年棄用。
- `SSL 3.0` 1996 年發布，2015     年棄用。後來     IETF 也將此協定特別發布了 [RFC      6101](https://tools.ietf.org/html/rfc6101) 作為歷史記錄。


## TLS


TSL 的全名是 Transport Layer Security 傳輸層安全性)是更新、更安全的 SSL 版本。我們仍將安全性憑證稱為 SSL，因為這是較常用的詞彙，不過當您透過DigiCert[購買 SSL ](https://www.websecurity.digicert.com/zh/tw/ssl-certificate?inid=infoctr_buylink_sslhome)時，您所購買的其實是最新的 TLS 憑證及 [ECC、RSA 或 DSA 的加密選項](https://www.websecurity.digicert.com/zh/tw/security-topics/how-ssl-works)。

- `TLS 1.0` 1999 年     IETF 將 SSL 標準化，發布了 [RFC      2246](https://tools.ietf.org/html/rfc2246)，同時改名為 TLS。也因此     SSL 3.0 和 TLS 1.0 其實沒有什麼太大差別，甚至可以說是一樣的東西。而     TLS 1.0 也支援相容 SSL 3.0 的功能，但這做法同時也降低了安全性。
- `TLS 1.1` 2006 年發布 [RFC      4346](https://tools.ietf.org/html/rfc4346)，雖然目前沒什麼問題，還是計劃於 2020 年棄用
- `TLS 1.2` 2008 年發布 [RFC      5246](https://tools.ietf.org/html/rfc5246)，可運作在 HTTP/2 上。
- 2014 年，Google 發現了     SSL 3.0 有致命的安全性漏洞，加上 TLS 1.0 因為加密模式設計不良，會[造成加密內容被解密](http://securityalley.blogspot.com/2014/07/ssltls-beast.html)，因此馬上變成主要的資安檢核專案之一，建議早日關閉。
- `TLS 1.3` 2018 年發布 [RFC      8446](https://tools.ietf.org/html/rfc8446)

注意看了一下，TLS 每個 RFC 都是 `46` 結尾，不知道是不是故意的。

值得一提的是，[HTTP/2](https://zh.wikipedia.org/wiki/HTTP/2) 協定是允許非加密的，同時也允許 TLS 1.2 或更新的版本，但目前主流瀏覽器都只實作加密的 HTTP/2，這讓 HTTP/2 + TLS 變成了強制標準。



### TLS 運作原理

TLS 在 [OSI 模型](https://en.wikipedia.org/wiki/OSI_model)裡，它屬於傳輸層的協定，而[簡介 HTTP](https://ithelp.ithome.com.tw/articles/10217426) 是有提到 HTTP 是應用層協定。而 OSI 模型在設計上是符合[里氏替換原則](https://ithelp.ithome.com.tw/articles/10192317)與[依賴反轉原則](https://ithelp.ithome.com.tw/articles/10192844)的，這代表傳輸層是否有 TLS 是不會影響應用層的 HTTP；反之，不管應用層是 HTTP、[FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) 或 [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) 等，都能使用 TLS 加密。



### TCP Three-way Handshake

傳輸層上還有另一個廣泛使用的協定－－[RFC 793 - Transmission Control Protocol（TCP）](https://tools.ietf.org/html/rfc793)，裡面有提到一開始建立連線的方法，即為 [Three-way Handshake](https://zh.wikipedia.org/wiki/传输控制协议)。



```
@startuml
Alice -> Bob: SYN
Alice <- Bob: SYN-ACK
Alice -> Bob: ACK
@enduml
```

簡單來說，這過程有點像在打電話：

1. Alice：「喂？」

2. Bob：「喂？有聽到嗎？」

3. Alice：「有聽到了！」

然後就可以開始正常講話了。

### HTTPS

HTTPS 全名 [超文字傳輸安全協定](https://zh.wikipedia.org/wiki/超文本传输安全协议)，那個 S 就是 Secure 的意思；HTTPS 透過 HTTP 進行通訊，但通訊過程使用 [SSL/TLS](https://zh.wikipedia.org/wiki/傳輸層安全性協定) 進行加密，藉由類似於前述的加密方式，在 HTTP 之上定義了相對安全的資料傳輸方法。

由於非對稱加密的運算量較高，傳遞回應較慢；實際的架構上，會透過公開金鑰加密傳遞出共用的金鑰，再透過共用金鑰加密進行後續的傳遞，兼顧了安全性及傳遞速度。

HTTPS (Hyper Text Transfer Protocol Secure，超級文字傳輸協議安全) 會在網站受到 SSL 憑證保護時在網址中出現。該憑證的詳細資料包括發行機構與網站擁有人的企業名稱，可以透過按一下瀏覽器列上的鎖定標記進行檢視。

基本的public key, private key 和 https的關系如下： 

(1)  主機(server)上要先生成private key, public key兩把key。( 可以互相上鎖、解鎖 )

   其中，private key要留在主機裡，public key則是公開給全世界知道 

(2) 當一般使用者在瀏覽網頁時拿到這臺主機的public key之後，browser就可以靠public key來加密，由此而建立https 

然而，實際上，在(2) 的步驟，一般使用者拿到public key時，他心裡有一個疑問，「我怎麼知道，現在給我public key的你，沒有被別人冒用了呢？」 這種時候，使用者的瀏覽器就會冒出警告訊息，說收到的public key並沒有被認證過。 

於是，為了電子商務的安全性，就要由第三方公正機關 「憑證中心」來代為處理這個「信賴」的問題。將上述的模型複雜化，引入了「憑證中心」這個角色之後，就變成如下： 

(1) 主機(server)上要先生成private key, public key兩把key。( 可以互相上鎖、解鎖 )

   其中，private key要留在主機裡，public key則是要先做加工之後，才可以讓全世界得知。 

(2) public key送給憑證中心簽署認證。這種時候，因為要送public key和相關的一些網站基本資訊出去給憑證中心簽署認證，需要把public key放進一個檔案檔，這個檔案檔就叫做certificate signing request，副檔名通常是CSR 

(3) 憑證中心簽署完畢後的public key，又可以稱之為ceriticate 。

   certificate自憑證中心取回之後，要安裝入主機(server)，作為SSL的public key 來使用 

(4) 當一般使用者在瀏覽網頁時拿到這臺主機的public key( 這時候可以叫它certificate )之後，browser裡頭早就預先安裝好的憑證中心public key會認証這個certificate，然後回報說，這個網站的https是沒有問題的。於是browser就可以用public key來加密，由此而建立https ( 如此一來，browser就不會跳出警告訊息了。)

### 憑證的信任機制

一般來說，憑證要被信任，要滿足以下兩種需求之一：

1. 這張憑證是由某一個你信任的組織 (CA, Certificate Authority, 憑證授權中心) 簽發的 (root certificate, 根憑證)

2. 憑證本身的 CA，又能夠證明是被 #1 裡面的 CA 信任的 (intermidiate certificate, 中介證書)

通常 #1 比較單純，各家瀏覽器都會內建一份清單，記載有什麼 CA 是可以被相信的。要進入這個名單的流程非常的嚴謹，而且，由於事關重大，若 CA 做了什麼不太好的事情，那很快就會從這個清單內驅逐出去。不過實務上，除了看瀏覽器裡面的清單以外，也會看作業系統內帶的清單。兩份清單都可以自己做增減。

名單的控管，可以參考一下 [Mozilla CA Certificate Store](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/)，至於從名單內被驅逐出的範例，可以參考一下 [WoSign](https://blog.mozilla.org/security/2016/10/24/distrusting-new-wosign-and-startcom-certificates/) 和 [中國官方的CA, CNNIC](https://blog.mozilla.org/security/2015/04/02/distrusting-new-cnnic-certificates/)。

至於 #2 的部分，會需要「數位簽章」的機制來做驗證。

### 數位簽章

一張憑證可以被另一個授權中心做簽章的動作。正常狀況下，簽章代表著授權中心已經確認過原憑證持有方是真的擁有這個位置（網址）。實務上，這個授權中心會拿自己的私鑰去幫這張憑證的內容做加密，然後把這個密文嵌在憑證當中，當作數位簽章。這個流程和前述非對稱加密的流程是相反的，在數位簽章的狀況下，任何人都能拿這家憑證中心的公鑰去解開這張憑證，來確認這簽章是正常的。

所以流程是這樣：

1. 你要進行 HTTPS 連線，雙方做 Hello

2. 伺服器丟一張憑證給你，憑證上面寫說他被某 CA 簽了

3. 你剛好有這家 CA 的公鑰，拿公鑰解他的憑證，看是不是解的出來，內容是否正常

4. 繼續下一步

另外，這個方式可以連結很多張憑證，不過憑證一多，就要多花一點時間去檢查（重複2和3）。

### 常見的狀況：自簽憑證

因為之前提過，任何人都能夠隨便生憑證，重點是「這張憑證是否被大家相信」。有時候，在開發流程中，你會需要用 HTTPS，但你生不出一張正常的憑證（例如你根本沒網域，或是沒錢買，或是來不及弄），所以你就必須要自己當自己的 CA，然後自己用那個 CA 私鑰去生一張憑證出來。因為你自己的 CA 通常不會在信任名單裡面，所以大家跟你連線的時候，都會出現警示。

這種狀況下，你還是正在使用 HTTPS，所以資料傳輸過程有加密。不過，除非你將這張憑證加入信任清單，不然你沒有辦法防止別人做「中間人攻擊（即假裝他是那臺伺服器）」。

### 機制弱點

前述提到，曾經發生過授權中心被除名的狀況。因為這些授權中心是可以讓任何憑證在大家的裝置上變得可用，因此，他們需要以非常嚴謹的態度來對待每一個憑證申請。被除名的 CNNIC，是因為某一間公司用中介證書簽了幾個 Google 網域底下的證書給其他人，而這張中介證書的根憑證是來自 CNNIC 的。因此，CNNIC 沒有做好管控措施，且這家公司是把憑證拿來做「竄改連線」的用途，因此就被除名了。

HTTPS 或是任何一個系統，都不是完全安全的。他防止不了有 CA 違規的情形、也防止不了你在服務裡面寫 shit logic。但是它還是一個很有效的資料傳輸方式。



## SSL 相關名詞

#### TLS: Transport Layer Security Protocol

在[上一篇文](https://jennycodes.me/posts/security-ssh#sshvsssl)中有稍微提到 TLS 的歷史，簡而言之，由於 SSL 已經不再安全（[POODLE](https://en.wikipedia.org/wiki/POODLE) 與 [DROWN](https://drownattack.com/) 是兩個曾經發生過的著名攻擊），所以現在已經被 TLS protocol 取代。慣性使然，當我們說 SSL（比如說 SSL 憑證）時，大部分情況其實是在說 TLS。

#### CA: Certificate Authority

[數位憑證認證機構，簡稱 CA](https://en.wikipedia.org/wiki/Certificate_authority)，是負責發放與管理數位憑證 （certificate）的單位。前面提到進行 SSL 連線的前置作業是 server 要提供數位憑證讓瀏覽器驗證，但瀏覽器要怎麼驗證？它會去看這個憑證是不是被一個它相信的 CA 簽署的。如果是，那瀏覽器就相信這個 server 可以信任，如果不是，那瀏覽器就再看這個 CA 有沒有它自己的 certificate，如果有，而這個 certificate 是被一個瀏覽器信任的 CA 簽的，那就放行，如果沒有，就再往下找。如果一路找下去，找不到可以信任的 CA，就失敗。

假設今天世界上有甲乙丙三家 CA。CA 丙簽了 CA 乙的憑證，而 CA 乙簽了 CA 甲的憑證。瀏覽器小明想連線到網站 A，而小明只知道 CA 丙。連線前，網站 A 傳了它的 certificate 們給小明。小明先看第一張，眉頭一皺，發現 A 的憑證是不認識的 CA 甲簽的，往下翻，看到 CA 乙簽了甲的憑證，但小明也不認識乙，所以繼續往下翻，下一張是乙的憑證，是 CA 丙簽署的 — bingo! 於是網站 A 順利與小明建立連線。

所以 CA 其實很像保證人的角色，它向瀏覽器保證一個網域的合法性，讓想要連線的那一方確保自己的連線物件是安全的。

#### Chain of Trust

這樣一層一層檢查 certificate，直到找到信任的 CA 的機制，叫做 [chain of trust](https://en.wikipedia.org/wiki/Chain_of_trust)。你可能會疑惑，為什麼不直接讓所有 server 都帶著 CA 丙簽的 certificate 就好了？為什麼還需要經過這麼多層？主要原因是安全。如果今天壞人 B 找到一個破解 CA 甲的方法，可以偽造甲的簽名，這個漏洞一旦被發現，所有被甲簽過的憑證就都沒有意義了，那些網域必須要重新找 CA 來擔保自己的合法性。

使用 chain of trust 的好處是，它可以降低 root CA（chain of trust 的源頭 CA，就是例子中的 CA 丙）被暴露的風險。不過這也代表，要成為一個 root CA，安全防護必須要做到謹慎再謹慎，不然如果 root CA 的私鑰被攻破了，後果不堪設想。

OpenSSL
 SSL/TLS 是 protocol，而 [OpenSSL](https://www.openssl.org/) 就是一個開源的實作（[SSH 與 OpenSSH](https://jennycodes.me/posts/security-ssh#openssh) 也是同樣的關係）。如果你的電腦是 Unix 系列的，很大的機率是系統已經裝好 OpenSSL 了。如果是 Windows 系統，也可以直接去[網站下載](https://www.openssl.org/source/)最新的版本。

```
$ openssl version
LibreSSL 2.6.5
```

可以先開啟終端機，試試 `version` 指令，如果有回傳版本給你，就代表你的電腦已經有 OpenSSL 了。

用 `$openssl help`（或是任何 OpenSSL 不認得的指令…）就可以看到 OpenSSL 提供的指令包。                

openssh commands

其中 `s_client`是一個挺實用的工具，讓我們診斷與測試 SSL 的安全連線。下面示範測試 jennycodes.me 網站的 SSL 狀態。

```
$ openssl s_client -connect jennycodes.me:443 -servername jennycodes.meCONNECTED(00000005)
depth=2 C = IE, O = Baltimore, OU = CyberTrust, CN = Baltimore CyberTrust Root
verify return:1
depth=1 C = US, ST = CA, L = San Francisco, O = “CloudFlare, Inc.”, CN = CloudFlare Inc ECC CA-2
verify return:1
depth=0 C = US, ST = CA, L = San Francisco, O = “CloudFlare, Inc.”, CN = sni.cloudflaressl.com
verify return:1
 — -
Certificate chain
 0 s:/C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=sni.cloudflaressl.com
 i:/C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=CloudFlare Inc ECC CA-2
 1 s:/C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=CloudFlare Inc ECC CA-2
 i:/C=IE/O=Baltimore/OU=CyberTrust/CN=Baltimore CyberTrust Root
 — -
Server certificate
 — — -BEGIN CERTIFICATE — — -
（略）
 — — -END CERTIFICATE — — -
subject=/C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=sni.cloudflaressl.com
issuer=/C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=CloudFlare Inc ECC CA-2
 — -
No client certificate CA names sent
Server Temp Key: ECDH, X25519, 253 bits
 — -
SSL handshake has read 2642 bytes and written 307 bytes
 — -
New, TLSv1/SSLv3, Cipher is ECDHE-ECDSA-CHACHA20-POLY1305
Server public key is 256 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
 Protocol : TLSv1.2
 Cipher : ECDHE-ECDSA-CHACHA20-POLY1305
 Session-ID: 5FEF2BA2A72483061BEB18C92222BBC507A1A95749AE67094F2863D537B7C600
 （略）
 Verify return code: 0 (ok)
 — -
closed
 
```

結果長這樣。解釋一下，我目前用的 SSL 是直接從 CloudFlare （CDN 伺服器）設定，不影響效用，但是 certificate 不會看到 jennycodes.me 的字樣。從上面一路看下來，`certificate chain` 的部分可以看到 openssl client 經過兩步 chain of trust 就認證了 jennycodes.me 網域（CloudFlare Inc ECC CA-2 -> Baltimore CyberTrust Root），緊接著的是 `server certificate` 內容，再下面可以注意的是 `SSL-Session` 下的 protocol 是用 `TLSv1.2`，而不是 SSL。

如果加上 `-state` 指令，變成：

```
$openssl s_client -connect jennycodes.me:443 -servername jennycodes.me -state
 
```

就會看到前面出現這段

```
SSL_connect:before/connect initialization 
SSL_connect:SSLv3 write client hello A
SSL_connect:SSLv3 read server hello A
depth=2 C = IE, O = Baltimore, OU = CyberTrust, CN = Baltimore CyberTrust Root
verify return:1
depth=1 C = US, ST = CA, L = San Francisco, O = “CloudFlare, Inc.”, CN = CloudFlare Inc ECC CA-2
verify return:1
depth=0 C = US, ST = CA, L = San Francisco, O = “CloudFlare, Inc.”, CN = sni.cloudflaressl.com
verify return:1
SSL_connect:SSLv3 read server certificate A
SSL_connect:SSLv3 read server key exchange A
SSL_connect:SSLv3 read server done A
SSL_connect:SSLv3 write client key exchange A
SSL_connect:SSLv3 write change cipher spec A
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
SSL_connect:SSLv3 read server session ticket A
SSL_connect:SSLv3 read finished A
```

這是連線前的握手過程，逐步確認 SSL 連線的步驟是否正確，滿好玩的。

再來，上面的指令只會顯示最前面那張 certificate 內容（也就是 server certificate）。如果想要看到所有的 certificate ，可以加上 `-showcerts`：

```
$openssl s_client -connect jennycodes.me:443 -servername jennycodes.me -showcerts
```

就可以拿到包含 root certificate 的所有憑證了。

光是 `s_client` 就有很多指令可以用，這邊送上 [s_client 的 man page](https://www.openssl.org/docs/man1.0.2/man1/openssl-s_client.html)，請好奇的人自行欣賞。

## 參考

[Security] SSL — HTTPS 背後的功臣. Security 資訊安全系列文第三篇！ | by 施靜樺 | Starbugs Weekly 星巴哥技術專欄 | Medium

[https://medium.com/starbugs/security-ssl-https-%E8%83%8C%E5%BE%8C%E7%9A%84%E5%8A%9F%E8%87%A3-df714e4df77b](https://medium.com/starbugs/security-ssl-https-背後的功臣-df714e4df77b)

HTTPS/SSL/TLS 概述，整體流程、憑證、數位簽章 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天

https://ithelp.ithome.com.tw/articles/10193095

SSL憑証(SSL certificate)的原理 - 知識庫 - 無限空間,虛擬主機,網域註冊,網域管理

https://support.unethost.com/index.php?rp=/knowledgebase/82/SSLSSL-certificate.html

一文搞懂 HTTP 和 HTTPS 是什麼？兩者有什麼差別｜ALPHA Camp Blog

https://tw.alphacamp.co/blog/http-https-difference

簡介 SSL、TLS 協定 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天

https://ithelp.ithome.com.tw/articles/10219106

網站SSL加密原理簡介 | 網管人

https://www.netadmin.com.tw/netadmin/zh-tw/technology/6F6D669EB83E4DC9BEA42F1C94636D46





