---
title: "Spring Cloud Gateway"
date: 2021-04-12T14:08:40+08:00
draft: true
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring Cloid"
toc: true
---

## Spring Cloud Gateway 筆記
<!-- 簡介 -->

## Spring Cloud Gateway 簡介



Spring生態系統之上構建的API網關，包括：Spring 5，Spring Boot 2和Project Reactor。Spring Cloud Gateway旨在提供一種簡單而有效的方法來路由到API，並基於Filter 提供 gateway的基本功能，例如：安全性，監視/指標和彈性。


<!--more-->



## Spring Cloud Gateway 監控

### 添加依賴 -  build.gradle

```build.gradle
implementation 'org.springframework.cloud:spring-cloud-starter-gateway'
implementation 'org.springframework.boot:spring-boot-starter-actuator'
implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
```

### 配置文件 -  application.properties OR application.yml

該/gateway驅動器的端點允許監視和使用Spring的雲網關應用程序進行交互。為了可遠程訪問，必須在應用程序屬性中通過HTTP或JMX啟用和公開端點。

application.properties
```properties
management.endpoint.gateway.enabled=true # default value
management.endpoints.web.exposure.include=gateway
```


application.yml
```yml
management:
  endpoint:
    gateway:
      enabled: true
  endpoints:
    web:
      exposure:
        include: gateway

```



### 得到所有route的資訊
**{IP}/actuator/gateway/routes**

```json
[
    {
        "predicate": "Paths: [/hollword/**], match trailing slash: true",
        "route_id": "holl-word",
        "filters": [],
        "uri": "lb://holl-word",
        "order": 0
    },
    {
        "predicate": "Paths: [/hollJava/**], match trailing slash: true",
        "route_id": "holl-Java",
        "filters": [],
        "uri": "lb://holl-Java",
        "order": 0
    }
]
```


| Path                     | Type   | Description                                                  |
| ------------------------ | ------ | ------------------------------------------------------------ |
| `route_id`               | String | The route id. 路由代號                                       |
| `route_object.predicate` | Object | The route predicate.                                         |
| `route_object.filters`   | Array  | The [GatewayFilter factories](https://cloud.spring.io/spring-cloud-gateway/multi/multi__actuator_api.html) applied to the route. 過濾器 |
| `order`                  | Number | The route order. 路線順序                                    |

### 得到某個route的資訊

**{IP}/actuator/gateway/routes/{id}**

````
{
    "predicate": "Paths: [/wealth/**], match trailing slash: true",
    "route_id": "wealth",
    "filters": [],
    "uri": "lb://wealth-system",
    "order": 0
}
````



## 所有Gateway actuator可以用的列表

`/actuator/gateway/{ID}`

| ID            | HTTP Method | Description                                                  |
| :------------ | :---------- | :----------------------------------------------------------- |
| globalfilters | GET         | Displays the list of global filters applied to the routes.   |
| routefilters  | GET         | Displays the list of GatewayFilter factories applied to a particular route. |
| refresh       | POST        | Clears the routes cache.                                     |
| routes        | GET         | Displays the list of routes defined in the gateway.          |
| routes/{id}   | GET         | Displays information about a particular route.               |
| routes/{id}   | POST        | Adds a new route to the gateway.                             |
| routes/{id}   | DELETE      | Removes an existing route from the gateway.                  |



## Spring Cloud Gateway 使用







## 參考

[Spring Cloud Gateway](https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/)

[SpringCloud gateway （史上最全） - 疯狂创客圈 - 博客园](https://www.cnblogs.com/crazymakercircle/p/11704077.html)

[Spring Cloud Gateway 开发指南（五） Actuator API | OnePiece](https://cdrcool.github.io/2020/02/27/Spring%20Cloud%20Gateway%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97(%E4%BA%94)%20Actuator%20API/)

