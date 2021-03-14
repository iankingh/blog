---
title: "AngualrOnIE11"
date: 2021-03-10T13:21:43+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

# Angualr IE 11 使用筆記
在IE 11 上的 使用
<!--more-->

## 前言 

基本上Angualr 與 IE11 不是很 OK ,建議不要再使用IE,如果有不幸的用到有幾點要注意

## 第一點

於index.html 加上 

``` html
    <meta http-equiv="X-UA-Compatible" content="IE=edge,IE=11" >
      <!-- //不快取 -->
    <META HTTP-EQUIV="pragma" CONTENT="no-cache">
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate">
    <META HTTP-EQUIV="expires" CONTENT="0">
```



## 第二點

如果要引用外部js 盡量在 angular.json 的scripts 地方做全局引用

``` json
  "scripts": [
              "src/assets/js/jquery.js" ,
              "src/assets/js/ie.js"
            ]

```

## 第三點  引用 ie.js

引用 ie.js ;新建一個 ie.js ,再引用內容如下


https://npmcdn.com/angular2@2.0.0-beta.21/es6/dev/src/testing/shims_for_IE.js

``` javascript
// function.name (all IE)
/*! @source http://stackoverflow.com/questions/6903762/function-name-not-supported-in-ie*/
if (!Object.hasOwnProperty('name')) {
  Object.defineProperty(Function.prototype, 'name', {
    get: function() {
      var matches = this.toString().match(/^\s*function\s*(\S*)\s*\(/);
      var name = matches && matches.length > 1 ? matches[1] : "";
      // For better performance only parse once, and then cache the
      // result through a new accessor for repeated access.
      Object.defineProperty(this, 'name', {value: name});
      return name;
    }
  });
}

//此處弱掃會有問題 ,可以先拿掉看可不可以運作 ,不行再加回來
// URL polyfill for SystemJS (all IE)
/*! @source https://github.com/ModuleLoader/es6-module-loader/blob/master/src/url-polyfill.js*/
// from https://gist.github.com/Yaffle/1088850
(function(global) {
  function URLPolyfill(url, baseURL) {
    if (typeof url != 'string') {
      throw new TypeError('URL must be a string');
    }
    var m = String(url).replace(/^\s+|\s+$/g, "").match(/^([^:\/?#]+:)?(?:\/\/(?:([^:@\/?#]*)(?::([^:@\/?#]*))?@)?(([^:\/?#]*)(?::(\d*))?))?([^?#]*)(\?[^#]*)?(#[\s\S]*)?/);
    if (!m) {
      throw new RangeError();
    }
    var protocol = m[1] || "";
    var username = m[2] || "";
    var password = m[3] || "";
    var host = m[4] || "";
    var hostname = m[5] || "";
    var port = m[6] || "";
    var pathname = m[7] || "";
    var search = m[8] || "";
    var hash = m[9] || "";
    if (baseURL !== undefined) {
      var base = baseURL instanceof URLPolyfill ? baseURL : new URLPolyfill(baseURL);
      var flag = protocol === "" && host === "" && username === "";
      if (flag && pathname === "" && search === "") {
        search = base.search;
      }
      if (flag && pathname.charAt(0) !== "/") {
        pathname = (pathname !== "" ? (((base.host !== "" || base.username !== "") && base.pathname === "" ? "/" : "") + base.pathname.slice(0, base.pathname.lastIndexOf("/") + 1) + pathname) : base.pathname);
      }
      // dot segments removal
      var output = [];
      pathname.replace(/^(\.\.?(\/|$))+/, "")
        .replace(/\/(\.(\/|$))+/g, "/")
        .replace(/\/\.\.$/, "/../")
        .replace(/\/?[^\/]*/g, function (p) {
          if (p === "/..") {
            output.pop();
          } else {
            output.push(p);
          }
        });
      pathname = output.join("").replace(/^\//, pathname.charAt(0) === "/" ? "/" : "");
      if (flag) {
        port = base.port;
        hostname = base.hostname;
        host = base.host;
        password = base.password;
        username = base.username;
      }
      if (protocol === "") {
        protocol = base.protocol;
      }
    }

    // convert windows file URLs to use /
    if (protocol == 'file:')
      pathname = pathname.replace(/\\/g, '/');

    this.origin = protocol + (protocol !== "" || host !== "" ? "//" : "") + host;
    this.href = protocol + (protocol !== "" || host !== "" ? "//" : "") + (username !== "" ? username + (password !== "" ? ":" + password : "") + "@" : "") + host + pathname + search + hash;
    this.protocol = protocol;
    this.username = username;
    this.password = password;
    this.host = host;
    this.hostname = hostname;
    this.port = port;
    this.pathname = pathname;
    this.search = search;
    this.hash = hash;
  }
global.URLPolyfill = URLPolyfill;
})(typeof self != 'undefined' ? self : global);

//classList (IE9)
/*! @license please refer to http://unlicense.org/ */
/*! @author Eli Grey */
/*! @source https://github.com/eligrey/classList.js */
;if("document" in self&&!("classList" in document.createElement("_"))){(function(j){"use strict";if(!("Element" in j)){return}var a="classList",f="prototype",m=j.Element[f],b=Object,k=String[f].trim||function(){return this.replace(/^\s+|\s+$/g,"")},c=Array[f].indexOf||function(q){var p=0,o=this.length;for(;p<o;p++){if(p in this&&this[p]===q){return p}}return -1},n=function(o,p){this.name=o;this.code=DOMException[o];this.message=p},g=function(p,o){if(o===""){throw new n("SYNTAX_ERR","An invalid or illegal string was specified")}if(/\s/.test(o)){throw new n("INVALID_CHARACTER_ERR","String contains an invalid character")}return c.call(p,o)},d=function(s){var r=k.call(s.getAttribute("class")||""),q=r?r.split(/\s+/):[],p=0,o=q.length;for(;p<o;p++){this.push(q[p])}this._updateClassName=function(){s.setAttribute("class",this.toString())}},e=d[f]=[],i=function(){return new d(this)};n[f]=Error[f];e.item=function(o){return this[o]||null};e.contains=function(o){o+="";return g(this,o)!==-1};e.add=function(){var s=arguments,r=0,p=s.length,q,o=false;do{q=s[r]+"";if(g(this,q)===-1){this.push(q);o=true}}while(++r<p);if(o){this._updateClassName()}};e.remove=function(){var t=arguments,s=0,p=t.length,r,o=false;do{r=t[s]+"";var q=g(this,r);if(q!==-1){this.splice(q,1);o=true}}while(++s<p);if(o){this._updateClassName()}};e.toggle=function(p,q){p+="";var o=this.contains(p),r=o?q!==true&&"remove":q!==false&&"add";if(r){this[r](p)}return !o};e.toString=function(){return this.join(" ")};if(b.defineProperty){var l={get:i,enumerable:true,configurable:true};try{b.defineProperty(m,a,l)}catch(h){if(h.number===-2146823252){l.enumerable=false;b.defineProperty(m,a,l)}}}else{if(b[f].__defineGetter__){m.__defineGetter__(a,i)}}}(self))};

//console mock (IE9)
if (!window.console) window.console = {};
if (!window.console.log) window.console.log = function () { };
if (!window.console.error) window.console.error = function () { };
if (!window.console.warn) window.console.warn = function () { };
if (!window.console.assert) window.console.assert = function () { };

//RequestAnimationFrame (IE9, Android 4.1, 4.2, 4.3)
/*! @author Paul Irish */
/*! @source https://gist.github.com/paulirish/1579671 */
// http://paulirish.com/2011/requestanimationframe-for-smart-animating/
// http://my.opera.com/emoller/blog/2011/12/20/requestanimationframe-for-smart-er-animating

// requestAnimationFrame polyfill by Erik Möller. fixes from Paul Irish and Tino Zijdel

// MIT license

(function() {
    var lastTime = 0;

    if (!window.requestAnimationFrame)
        window.requestAnimationFrame = function(callback, element) {
            var currTime = Date.now();
            var timeToCall = Math.max(0, 16 - (currTime - lastTime));
            var id = window.setTimeout(function() { callback(currTime + timeToCall); },
              timeToCall);
            lastTime = currTime + timeToCall;
            return id;
        };

    if (!window.cancelAnimationFrame)
        window.cancelAnimationFrame = function(id) {
            clearTimeout(id);
        };
}());



```







## 參考

http://ymblog.azurewebsites.net/%E9%80%8F%E9%81%8E-angular-cli-%E7%94%A2%E7%94%9F%E7%9A%84%E5%89%8D%E7%AB%AF%E7%A8%8B%E5%BC%8F%E5%9C%A8-ie11-%E7%84%A1%E6%B3%95%E6%AD%A3%E7%A2%BA%E5%9F%B7%E8%A1%8C/

https://github.com/angular/angular-cli/issues/9508
