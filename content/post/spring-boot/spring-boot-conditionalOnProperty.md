---
title: "SpringBoot_ConditionalOnProperty"
date: 2021-02-03T11:41:55+08:00
draft: false
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring boot"
toc: true
---

## Spring ConditionalOnProperty的作用和用法
<!--more-->

## 前言

   在spring 中有時會希望在某些特定環境底下才能生效的component，例如:建立假資料等，但我們在正式環境底下又不希望使用時，可以使用@ConditionalOnProperty 來達成

## @ConditionalOnProperty的作用和用法

在spring boot中需要控制配置類是否生效，可以使用@ConditionalOnProperty注解來控@Configuration是否生效

ConditionalOnProperty的使用
	@Retention(RetentionPolicy.RUNTIME)
	@Target({ElementType.TYPE, ElementType.METHOD})
	@Documented
	@Conditional({OnPropertyCondition.class})
	public @interface ConditionalOnProperty {
	    String[] value() default {}; //陣列，獲取對應property名稱的值，與name不可同時使用
	 
	    String prefix() default "";//property名稱的首碼，可有可無
	 
	    String[] name() default {};//陣列，property完整名稱或部分名稱（可與prefix組合使用，組成完整的property名稱），與value不可同時使用

	    String havingValue() default "";//可與name組合使用，比較獲取到的屬性值與havingValue給定的值是否相同，相同才載入配置
 
	    boolean matchIfMissing() default false;//缺少該property時是否可以載入。如果為true，沒有該property也會正常載入；反之報錯

	    boolean relaxedNames() default true;//是否可以鬆散匹配，至今不知道怎麼使用的
	}
 


配置類代碼:
@Configuration
@ConditionalOnProperty(prefix = "filter",name = "loginFilter",havingValue = "true")
public class FilterConfig {
	//prefix為設定檔中的首碼,
	//name為配置的名字
	//havingValue是與配置的值對比值,當兩個值相同返回true,配置類生效.
    @Bean
    public FilterRegistrationBean getFilterRegistration() {
        FilterRegistrationBean filterRegistration  = new FilterRegistrationBean(new LoginFilter());
        filterRegistration.addUrlPatterns("/*");
        return filterRegistration;
    }
}

設定檔中的代碼
filter.loginFilter=true

測試
當設定檔中值為true時:輸出了"篩檢程式"三個字,說明loginFilter生效了,說明配置類生效了.
 
當設定檔中值為false時:沒有輸出了"篩檢程式"三個字,說明loginFilter沒有生效,說明配置類沒有生效.
 
總結:
通過@ConditionalOnProperty控制配置類是否生效,可以將配置與代碼進行分離,實現了更好的控制配置.
@ConditionalOnProperty實現是通過havingValue與設定檔中的值對比,返回為true則配置類生效,反之失效.


@ConditionalOnExpression("{'prod', 'alsoProd'}.contains('${env.name}')")



## 參考

@ConditionalOnProperty的作用和用法_sqlgao22的博客-CSDN博客
https://blog.csdn.net/sqlgao22/article/details/96476754

Conditional Beans with Spring Boot
https://reflectoring.io/spring-boot-conditionals/

ConditionalOnProperty的使用_堅持，讓夢想閃耀！-CSDN博客
https://blog.csdn.net/u010002184/article/details/79353696

java - Spring Boot SpEL ConditionalOnExpression check multiple properties - Stack Overflow
https://stackoverflow.com/questions/40477251/spring-boot-spel-conditionalonexpression-check-multiple-properties/40497419#40497419

java - Spring @ConditionalOnExpression with OR statement - Stack Overflow
https://stackoverflow.com/questions/45736846/spring-conditionalonexpression-with-or-statement

