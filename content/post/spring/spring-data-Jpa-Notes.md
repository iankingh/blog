---
title: "SpringDataJpaNotes"
date: 2020-06-04T05:45:59+08:00
categories:
 - "筆記"
tags:
 - "java"
 - "Spring"
 - "Spring Data JPA"
toc: true
draft: false
---

## Spring Data JPA 介紹

### Spring-Data 概述

  **Spring Data** 是一個資料訪問框架 ，用於簡化資料庫訪問，旨在提供一致的資料庫訪問模型，同時仍然保留不同資料庫底層資料存儲的特點，**Spring** **Data** 採用了**領域驅動模型**的設計思想，實現了訪問關係型數據庫、非關係型數據庫的統一的介面，只需要定義好領域模型（**Entity**），後續的創建表、**CURD**、排序操作不需要手動添加任何**SQL**語句，同時也支持手動擴展功能。

  **Spring Data** 只要定義介面，遵循 **Spring Data** 的規範，就無需寫實現類。

  **Spring Data** 提供了預設的交易處理方式，即所有的查詢均聲明為唯讀事務。

  **Spring Data** 專案所支援 **NoSQL** 存儲：**MongoDB** （文檔資料庫）、**Neo4j**（圖形資料庫）、Redis（**鍵**/值存儲）、**Hbase**（列族資料庫）

  **Spring Data** 專案所支援的關係資料存儲技術：**JDBC、JPA**

<!--more-->

### Spring Data JPA 概述

 JPA(Java Persistence API)是 **Sun** 官方提出的 **Java** 持久化規範。

 **JPA**主要是為了簡化現有的持久化開發工作和整合 **ORM** 技術， 是在充分吸收了現有 **Hibernate、TopLink、JDO** 等 **ORM** 框架的基礎上發展而來的，具有易於使用、伸縮性強等優點。

 **Spring Data JPA** 是 **Spring** 基於 **ORM** 框架、**JPA** 規範的基礎上封裝的一套 **JPA** 應用框架，可使開發者用簡單代碼即可實現對資料的訪問和操作。

 它提供了包括增刪改查等在內的常用功能，且易於擴展！通常我們寫持久層，都是先寫一個介面，再寫介面對應的實現類，在實現類中進行持久層的業務邏輯處理。而現在，**Spring Data JPA**幫助我們自動完成了持久層的業務邏輯處理，開發者唯一要做的，就只是聲明持久層的介面，其他都交給 **Spring Data JPA** 來幫你完成！

 `注意：JPA 是一套規範，不是一套產品， Hibernate、TopLink、JDO 它們是一套產品，如果說這些產品實現了這個 JPA 規範，那麼就可以叫它們為 JPA 的實現產品。`

## Repository 

### Repository介面

**Repository** 介面是 **Spring Data** 的一個核心介面，是一個抽象的介面，使用者通過繼承該介面來實現資料的訪問，它不提供任何方法，開發者需要在自己定義的介面中聲明需要的方法

```java
public interface Repository<T, ID> { }
```

很重要的一點就是，**Repository**的實現類是在應用啟動的時候生成的，也就是**Spring**的應用上下文創建的時候.而不是通過代碼生成技術產生的，也不是介面方法調用時才產生的 基礎的**Repository**提供了最基本的資料訪問功能，其幾個子介面則擴展了一些功能。

編寫**Spring Data JPA Repository** 的關鍵在於從一組介面中挑選一個進行擴展

EX:

```java
public interface CustomerRepository extends Repository<CustomerEntity,Long> { }
```

添加注解為其指定 **CustomerEntity**和 **id** 屬性。

`在spring boot中如果使用了 spring-boot-starter-data-jpa ,會自動掃描所有擴展了Repository介面的類`

###  CrudRepository 介面

**CrudRepository** 介面繼承**Repository**，提供對實體類(**CRUD**)增刪改查方法，可以直接調用。 

**CrudRepository**介面實現了**save、delete、count、exists**等方法，繼承這個介面時需要兩個範本參數**T**和**ID**，**T**就是你的實體類（對應資料庫表），**ID**就是主鍵。

```java

public interface CrudRepository<T, ID extends Serializable> extends Repository<T, ID> 
{
    <S extends T> S save(S entity); //Saves the given entity (保存給定的實體。)

    Optional<T> findById(ID primaryKey); //Returns the entity identified by the given ID.(返回由給定ID標識的實體。)

    Iterable<T> findAll(); //Returns all entities.(返回所有實體。)
    
    long count();//Returns the number of entities.(查詢實體數量) 
    
    void delete(T entity); //	Deletes the given entity.(刪除給定的實體。)
    
    boolean existsById(ID primaryKey); //Indicates whether an entity with the given ID exists.(根據id判斷實體是否存在)
    
    void delete(ID id);//根據Id刪除實體 
   
	<S extends T> Iterable<S> saveAll(Iterable<S> entities);//保存集合

}
```

在使用中，使用者需要繼承這個介面，**CustomerEntity**就是定義的實體，**Long**是主鍵類型

```java
public interface CustomerRepository extends CrudRepository<CustomerEntity, Long>
{
    
}
```

````java

package com.example.demo;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

/**
 * CustomerRepositoryTest
 */
@SpringBootTest
public class CustomerRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    // CRUD 操作

    // 增 save(entity), save(entities)

    @Test
    public void save1() {

        UserEntity userEntity = new UserEntity();

        userEntity.setName("肯德基20");

        userEntity = userRepository.save(userEntity);

        System.out.println(userEntity);

    }

    // save(entities)

    @Test
    public void saveManyTest() {

        UserEntity userEntity = new UserEntity();

        userEntity.setName("test21");

        UserEntity userEntity2 = new UserEntity();

        userEntity2.setName("test22");

        ArrayList<UserEntity> userEntities = new ArrayList<UserEntity>();

        userEntities.add(userEntity);

        userEntities.add(userEntity2);

        userRepository.saveAll(userEntities);

    }

}

````

    // 刪 delete(id),delete(entity),delete(entities),deleteAll
    
    // 查 findOne(id) ,findAll, exits(id)
    
    // save***只要 id一樣,就會更新,而不是添加.


### PagingAndSortingRepository 介面 

繼承**CrudRepository**，具有分頁查詢和排序功能

```java
public interface PagingAndSortingRepository<T, ID extends Serializable> extends CrudRepository<T, ID> {
 
  Iterable<T> findAll(Sort sort); //排序
 
  Page<T> findAll(Pageable pageable); //分頁查詢（含排序功能）
}
```

**example: **

````java
package com.example.demo;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

/**
 * CustomerRepositoryTest
 */
@SpringBootTest
public class CustomerRepositoryTest {

    @Autowired
    private CustomerRepository customerRepository;

   @Test
    public void findAll() {
        Iterable iterable = customerRepository.findAll();
        System.out.println("iterable " + iterable);

    }
}
````



### JpaRepository 介面

繼承 **PagingAndSortingRepository**，實現一組 **JPA** 規範相關的方法， 
該介面提供了**JPA**的相關功能  ，**PagingAndSortingRepository**介面本身已經繼承了 **CrudRepository**

```java
public interface JpaRepository<T,ID> extends PagingAndSortingRepository<T,ID>, QueryByExampleExecutor<T>
{
    
	List<T> findAll(); //查找所有實體
    
	List<T> findAll(Sort sort); //排序、查找所有實體
    
	List<T> save(Iterable<? extends T> entities);//保存集合
    
	T saveAndFlush(T entity);//強制執行持久化
    
    void flush();//執行緩存與資料庫同步
    
	void deleteInBatch(Iterable<T> entities);//刪除一個實體集合

}

```

### JpaSpecificationExecutor介面

可以執行原生SQL查詢也可以自訂**Repository**的方法不屬於Repository體系，實現一組 JPA **Criteria** 查詢相關的方法 **Specification**：封裝  **JPA Criteria** 查詢準則。通常使用匿名內部類的方式來創建該介面的物件 

**Specification**：封裝 **JPA Criteria** 查詢準則。通常使用匿名內部類的方式來創建該介面的物件

由於**JpaSpecificationExecutor** 並不繼承**repository** 介面，所以它不能單獨使用，只能和**jpa Repository** 一起用。

```java
public interface JpaSpecificationExecutor<T> {

    T findOne(Specification<T> spec);

    List<T> findAll(Specification<T> spec);

    Page<T> findAll(Specification<T> spec, Pageable pageable);

    List<T> findAll(Specification<T> spec, Sort sort);

    long count(Specification<T> spec);
}

```



```java
 public interface CustomerRepository extends CrudRepository<Customer, Long>,  JpaSpecificationExecutor {
 
 }
```



## Spring-Data 方法定義規範

```java
public interface ProductInfoRepository extends JpaRepository<ProductInfoEntity,String> {
   //定義一個方法:根據商品名稱查找所有的商品
  List<ProductInfoEntity> findAllByProductName(String name);
}
```

當創建 **Repository** 實現的時候， **Spring Data**會檢查 **Repository** 介面的所有方法，解析方法的名稱，並基於被持久化的物件來推測方法的目的，**Spring Data** 定義了一組小型的領域特定語言(**DSL**) ，在這裡持久化的細節都是通過 **Repository**的方法簽名來描述的

**findAllByProductName(String name)** 方法非常簡單，**Repoditory** 方法是 由一個動詞，一個可選主題,關鍵字**By**以及一個斷言所組成

在**findAllByProductName** 方法中,動詞是**findAll** ,斷言是 **ProductName**，主題並沒有指定，

暗含就是 **ProductInfoEntity Repository** 方法的主題是可選的,它主要是讓你命名方法的時候有很多的靈活性,findAllByProductName和findAllProductInfoEntityByProductName方法沒有什麼區別. 要查詢的物件的類型是通過如何參數化 Repository 介面來決定的,而不是方法名稱中的主題.

### 擴展查詢

按照Spring Data 的規範，查詢方法以find | read | get 開頭， 涉及條件查詢時，條件的屬性用條件關鍵字連接，要注意的是：條件屬性以首字母大寫。

find | read | get方法都會查詢資料並返回物件.而 count 則會返回匹配對象的數量,而不是對象本身.

EX：定義一個 Entity 實體類

````java
class UserEntity｛

  	private String  firstName; 

    private String lastName; 

｝
````

使用And條件連接時，應這樣寫：

```java
findByLastNameAndFirstName(String lastName,String firstName);
```

假如創建如下的查詢：findByUserDepUuid()，框架在解析該方法時，首先剔除 findBy，然後對剩下的屬性進行解析，假設查詢實體為Doc
 （1）先判斷 userDepUuid （根據 POJO 規範，首字母變為小寫）是否為查詢實體的一個屬性，如果是，則表示根據該屬性進行查詢；如果沒有該屬性，繼續第二步；
 （2）從右往左截取第一個大寫字母開頭的字串(此處為Uuid)，然後檢查剩下的字串是否為查詢實體的一個屬性，如果是，則表示根據該屬性進行查詢；如果沒有該屬性，則重複第二步，繼續從右往左截取；最後假設 user 為查詢實體的一個屬性；
 （3）接著處理剩下部分（DepUuid），先判斷 user 所對應的類型是否有depUuid屬性，如果有，則表示該方法最終是根據 “ Doc.user.depUuid” 的取值進行查詢；否則繼續按照步驟 2 的規則從右往左截取，最終表示根據 “Doc.user.dep.uuid” 的值進行查詢。
 （4）可能會存在一種特殊情況，比如 Doc包含一個 user 的屬性，也有一個 userDep 屬性，此時會存在混淆。可以明確在屬性之間加上 "_" 以顯式表達意圖，比如 "findByUser_DepUuid()" 或者 "findByUserDep_uuid()"
 特殊的參數： 還可以直接在方法的參數上加入分頁或排序的參數，比如：

```java
 Page<UserModel> findByName(String name, Pageable pageable);
 List<UserModel> findByName(String name, Sort sort);
```



如果覺得curdrepository提供的查詢不符合要求，可以繼承該介面進行擴展，

Spring Data JPA為此提供了一些表達條件查詢的關鍵字，大致如下：

條件的屬性名稱與個數要與參數的位置與個數一一對應
 直接在介面中定義查詢方法，如果是符合規範的，可以不用寫實現，目前支援的關鍵字寫法如下：

 

| **Keyword** | Description                 | **Sample**                                                   |
| ----------- | --------------------------- | ------------------------------------------------------------ |
| And         | 等價於SQL中的and 關鍵字     | findByUsernameAndPassword(String user, Striang pwd)；        |
| Or          | 等價於SQL中的or 關鍵字      | findByUsernameOrAddress(String user, String addr);           |
| Between     | 等價於SQL中的between 關鍵字 | findBySalaryBetween(int max,int min)；                       |
| LessThan    | 等價於SQL中的"<"            | findBySalaryLessThan(int max)；                              |
| GreaterThan | 等價於SQL中的">"            | findBySalaryGreaterThan(intmin)；                            |
| IsNull      | 等價於SQL中的"is null"      | findByUsernameIsNull()；                                     |
| IsNotNull   | 等價於SQL中的"is not null"  | findByUsernameIsNotNull()；                                  |
| NotNull     | 與IsNotNull等價             |                                                              |
| Like        | 等價於SQL中的"like"         | findByUsernameLike(String user)；                            |
| NotLike     | 等價於SQL中的"not like"     | findByUsernameNotLike(Stringuser)；                          |
| OrderBy     | 等價於SQL中的"order by"     | findByUsernameOrderBySalaryAsc(String user)；                |
| Not         | 等價於SQL中的"！ ="         | findByUsernameNot(String user)；                             |
| In          | 等價於SQL中的"in"           | findByUsernameIn(Collection<String> userList)，方法的參數可以是 Collection類型，也可以是陣列或者不定長參數； |
| NotIn       | 等價於SQL中的"not in"       | findByUsernameNotIn(Collection<String> userList)，方法的參數可以是 Collection類型，也可以是陣列或者不定長參數； |

### @Query注解

**Spring Data** 這個小型的DSL**依舊有其局限性**,有時候通過方法名表達預期的查詢很繁瑣,甚至無法實現.如果與呆這種情況,**Spring Data**能讓我們通過**@Query**注解來解決問題

這種查詢可以聲明在 **Repository** 方法中，擺脫像命名查詢那樣的約束，將查詢直接在相應的介面方法中聲明，結構更為清晰，這是 **Spring data** 的特有實現。

如果是 **@Query** 中有 **LIKE** 關鍵字，後面的參數需要前面或者後面加 **%**，這樣在傳遞參數值的時候就可以不加 **%**：

**@Query**注解
 這種查詢可以聲明在 **Repository** 方法中，擺脫像命名查詢那樣的約束，將查詢直接在相應的介面方法中聲明，結構更為清晰，這是 **Spring data** 的特有實現。

自訂 **Repository** 方法
 定義一個介面: 聲明要添加的, 並自實現的方法
 提供該介面的實現類: 類名需在要聲明的 **Repository** 後添加 **Impl**, 並實現方法
 聲明 **Repository** 介面, 並繼承 1) 聲明的介面
 使用.
 注意: 預設情況下, **Spring Data** 會在 **base-package** 中查找 "介面名**Impl**" 作為實現類. 也可以通過　**repository-impl-postfix**　聲明尾碼

```java
@Query("select o from UserModel o where o.name like %?1")
```

### @Query來指定本地查詢

使用**@Query**來指定本地查詢，只要設置**nativeQuery**為**true**

```java
@Query(value="select * from tbl_user where name like %?1" ,nativeQuery=true)
```

**@Query** 與 **@Modifying** 這兩個 **annotation**一起聲明，可定義個性化更新操作，例如只涉及某些欄位更新時最為常用

**Springdata**支援**JPQL** 語句對查詢進行擴展，

例子如下：

```java
public interface  CustomerRepository extends  CrudRepository<Customer,  Long> 
	{   
      @Query("select a from Customer a WHERE  a.firstName = ?")
      List<Customer> findByQuery(StringfirstName);  
	}  
```

EX:

```java
//聲明自訂查詢
    /**
    *	使用JPA SQL語句
    *	@return
    **/
   @Query("select p from ProductInfoEntity p where p.productName like '%米%' ")
   List<ProductInfoEntity> findProductInfo();


```



 ```java
/**
*	使用JPA SQL語句 查詢價格最高的商品
**/
   @Query("select p from ProductInfoEntity p " +

       "where p.productPrice=" +

       "(select max(p2.productPrice) from ProductInfoEntity p2)")

   List<ProductInfoEntity> findMaxPrice();
 ```

 

 ````java
  /**
   * 使用JPA SQL語句 帶參數的查詢1
   * @param name
   * @param price
   * @return
   **/
   @Query("select o from ProductInfoEntity o where o.productName=?1 and o.productPrice=?2")

   List<ProductInfoEntity> findParam(String name, double price);
 ````



 

```java
  /**
   * 使用JPASQL語句 帶參數的查詢2
   * @param name
   * @param price
   * @return
   **/
   @Query("select o from ProductInfoEntity o where o.productName=:name and o.productPrice=:price")

   List<ProductInfoEntity> findParam2(@Param("name") String name, @Param("price") double price);

當然還可以使用原生SQL語句進行查詢,只需要 nativeQuery = true 即可
```



```java
 /**
  *使用原生SQL語句 查詢
  * @return
  **/

  @Query(nativeQuery = true,value = "select count(*) from product_info")

  Integer getCount();
```

**Spring data JPA** 更新及刪除操作整合事物的使用

更新操作注意事項:

```java
 /** 使用Query注解寫更新JPA語句
 *添加 @Modifying 注解
 **/
 @Modifying
  @Query("update ProductInfoEntity o set o.productPrice =:price where o.productId=:id")

  Integer updatePrice(@Param("id") String id,@Param("price") double price);
```



- 在service層添加事物     @Transactional

 ````java
package com.itguang.weixinsell.service;
 
import com.itguang.weixinsell.repository.ProductInfoRepository;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;

import org.springframework.transaction.annotation.Transactional;

 
@Service

@Transactional

public class ProductInfoService {


  @Autowired

  private ProductInfoRepository infoRepository;


  public Integer updatePrice( String id,double price){

   Integer i = infoRepository.updatePrice(id, price);

    return i;
  }

}
 ````




## 參考