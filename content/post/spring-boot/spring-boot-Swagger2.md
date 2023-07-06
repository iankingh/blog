---
title: "Spring Boot中使用Swagger2 "
date: 2020-07-03T16:01:24+08:00
draft: true
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring boot"
toc: true
---

## Spring Boot中使用Swagger2 

<!--more-->

## Spring Boot中使用Swagger2構建RESTful API文檔

- 由於介面眾多，並且細節複雜（需要考慮不同的HTTP請求類型、HTTP頭部資訊、HTTP請求內容等），高品質地創建這份文檔本身就是件非常吃力的事，下游的抱怨聲不絕於耳。 

- 隨著時間推移，不斷修改介面實現的時候都必須同步修改介面文檔，而文檔與代碼又處於兩個不同的媒介，除非有嚴格的管理機制，不然很容易導致不一致現象。 

- 為解決上面這樣的問題，本文將介紹RESTful API的好夥伴Swagger2，它可以輕鬆的整合到Spring Boot中，並與Spring MVC程式配合組織出強大RESTful API文檔。它既可以減少我們創建文檔的工作量，同時說明內容又整合入實現代碼中，讓維護文檔和修改代碼整合為一體，可以讓我們在修改代碼邏輯的同時方便的修改文檔說明。另外Swagger2也提供了強大的頁面測試功能來調試每個RESTful API。具體效果如下圖所示： 

本文主要內容是： 

- 先利用 SpringFox 庫生成即時文檔； 

- 再利用 Swagger2Markup Maven外掛程式生成 asciidoc 文檔；  
- 最後利用 asciidoctor Maven外掛程式生成 html 或 pdf 檔； 
 
環境： SpringBoot + SpringFox + Swagger2Markup + Maven 
<!--more-->

下面我們直接進入正題，如何在spring boot專案中使用Swagger。總共分為三部 
第一步，引入swagger依賴 
第二部，在spring-boot中配置swagger-ui介面 
第三步，提供API檔頁基本資訊 
第四步，給rest API編寫檔 
1.1	springfox-swagger
swagger的功能非常強大，spring這個大神就開始試圖想把swagger繼承到自己的專案中，就有了後來的spring-swagger，再後來又演變成了springfox。雖然是通過plug的方式把swagger整合進來，但是它本身對api的生成，主要還是依靠swagger實現的。
1.2	SpringFox的大致原理
springfox的大致原理就是，在專案啟動的過程中，spring上下文的初始化的過程，框架自動根據配置家在一些swagger相關的bean到當前的上下文，並且自動掃描系統中可能需要生成的api檔的那些類，並生成響應的資訊快取起來。一般的都會掃描控制層Controller類，根據這些Controller類中的功能方法自動生成API介面檔。

1.3	添加Swagger2依賴


在pom.xml中加入Swagger2的依賴
```
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.2.2</version>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.2.2</version>
</dependency>
```

1.4	建Swagger2配置類
新增Swagger2的配置檔案：configuration
在Application.java同級創建Swagger2的配置類Swagger2。

@Configuration
@EnableSwagger2
public class Swagger2 {

    @Bean
    public Docket createRestApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.didispace.web"))
                .paths(PathSelectors.any())
                .build();
    }
    
    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("Spring Boot中使用Swagger2構建RESTful APIs")
                .description("更多Spring Boot相關文章請關注：http://blog.didispace.com/")
                .termsOfServiceUrl("http://blog.didispace.com/")
                .contact("程式猿DD")
                .version("1.0")
                .build();
    }

}
如上代碼所示，通過@Configuration注解，讓Spring來載入該類配置。再通過@EnableSwagger2注解來啟用Swagger2。
再通過createRestApi函數創建Docket的Bean之後，apiInfo()用來創建該Api的基本資訊（這些基本資訊會展現在文檔頁面中）。select()函數返回一個ApiSelectorBuilder實例用來控制哪些介面暴露給Swagger來展現，本例採用指定掃描的包路徑來定義，Swagger會掃描該包下所有Controller定義的API，並產生文檔內容（除了被@ApiIgnore指定的請求）。
1.5	添加文檔內容

在API上做一些宣告：在Controller類中新增相關的swagger註解。但是有一個要求，這個Controller類一定要讓上一步配置類的@ComponentScan掃描到；
在完成了上述配置後，其實已經可以生產文檔內容，但是這樣的文檔主要針對請求本身，而描述主要來源於函數等命名產生，對用戶並不友好，我們通常需要自己增加一些說明來豐富文檔內容。如下所示，我們通過@ApiOperation注解來給API增加說明、通過@ApiImplicitParams、@ApiImplicitParam注解來給參數增加說明。

@RestController
@RequestMapping(value="/users")     // 通過這裡配置使下麵的映射都在/users下，可去除
public class UserController {

    static Map<Long, User> users = Collections.synchronizedMap(new HashMap<Long, User>());
    
    @ApiOperation(value="獲取用戶列表", notes="")
    @RequestMapping(value={""}, method=RequestMethod.GET)
    public List<User> getUserList() {
        List<User> r = new ArrayList<User>(users.values());
        return r;
    }
    
    @ApiOperation(value="創建使用者", notes="根據User物件創建使用者")
    @ApiImplicitParam(name = "user", value = "使用者詳細實體user", required = true, dataType = "User")
    @RequestMapping(value="", method=RequestMethod.POST)
    public String postUser(@RequestBody User user) {
        users.put(user.getId(), user);
        return "success";
    }
    
    @ApiOperation(value="獲取使用者詳細資訊", notes="根據url的id來獲取使用者詳細資訊")
    @ApiImplicitParam(name = "id", value = "用戶ID", required = true, dataType = "Long")
    @RequestMapping(value="/{id}", method=RequestMethod.GET)
    public User getUser(@PathVariable Long id) {
        return users.get(id);
    }
    
    @ApiOperation(value="更新使用者詳細資訊", notes="根據url的id來指定更新物件，並根據傳過來的user資訊來更新使用者詳細資訊")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "id", value = "用戶ID", required = true, dataType = "Long"),
            @ApiImplicitParam(name = "user", value = "使用者詳細實體user", required = true, dataType = "User")
    })
    @RequestMapping(value="/{id}", method=RequestMethod.PUT)
    public String putUser(@PathVariable Long id, @RequestBody User user) {
        User u = users.get(id);
        u.setName(user.getName());
        u.setAge(user.getAge());
        users.put(id, u);
        return "success";
    }
    
    @ApiOperation(value="刪除使用者", notes="根據url的id來指定刪除物件")
    @ApiImplicitParam(name = "id", value = "用戶ID", required = true, dataType = "Long")
    @RequestMapping(value="/{id}", method=RequestMethod.DELETE)
    public String deleteUser(@PathVariable Long id) {
        users.remove(id);
        return "success";
    }

}
完成上述代碼添加上，啟動Spring Boot程式，
訪問：http://localhost:8080/swagger-ui.html
。就能看到前文所展示的RESTful API的頁面。我們可以再點開具體的API請求，以POST類型的/users請求為例，可找到上述代碼中我們配置的Notes資訊以及參數user的描述資訊，如下圖所示。

1.6	API文檔訪問與調試
在上圖請求的頁面中，我們看到user的Value是個輸入框？是的，Swagger除了查看介面功能外，還提供了調試測試功能，我們可以點擊上圖中右側的Model Schema（黃色區域：它指明了User的資料結構），此時Value中就有了user物件的範本，我們只需要稍適修改，點擊下方“Try it out！”按鈕，即可完成了一次請求調用！
此時，你也可以通過幾個GET請求來驗證之前的POST請求是否正確。
相比為這些介面編寫文檔的工作，我們增加的配置內容是非常少而且精簡的，對於原有代碼的侵入也在忍受範圍之內。因此，在構建RESTful API的同時，加入swagger來對API文檔進行管理，是個不錯的選擇。
1.7	代碼示例 

