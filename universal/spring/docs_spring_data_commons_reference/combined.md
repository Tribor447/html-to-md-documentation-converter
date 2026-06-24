# Spring Data Commons

## Navigation

- Overview
  
- [Overview](#index)
  
- [Dependencies](#dependencies)
  
- [Upgrading Spring Data](#upgrade)
  
- [Object Mapping Fundamentals](#object-mapping)
  
- [Working with Spring Data Repositories](#repositories)
    
- [Core concepts](#repositories-core-concepts)
    
- [Query Methods](#repositories-query-methods)
    
- [Defining Repository Interfaces](#repositories-definition)
    
- [Defining Query Methods](#repositories-query-methods-details)
    
- [Vector Search](#repositories-vector-search)
    
- [Creating Repository Instances](#repositories-create-instances)
    
- [Custom Repository Implementations](#repositories-custom-implementations)
    
- [Publishing Events from Aggregate Roots](#repositories-core-domain-events)
    
- [Spring Data Extensions](#repositories-core-extensions)
    
- [Scrolling](#repositories-scrolling)
    
- [Null Handling of Repository Methods](#repositories-null-handling)
    
- [Projections](#repositories-projections)
  
- [Query by Example](#query-by-example)
  
- [Value Expressions Fundamentals](#value-expressions)
  
- [Property Paths](#property-paths)
  
- [Auditing](#auditing)
  
- [Custom Conversions](#custom-conversions)
  
- [Entity Callbacks](#entity-callbacks)
  
- [Entity State Detection Strategies](#is-new-state-detection)
  
- [Ahead of Time Optimizations](#aot)
  
- [Kotlin Support](#kotlin)
    
- [Requirements](#kotlin-requirements)
    
- [Null Safety](#kotlin-null-safety)
    
- [Object Mapping](#kotlin-object-mapping)
    
- [Extensions](#kotlin-extensions)
    
- [Coroutines](#kotlin-coroutines)
  - Appendices
    
- [Namespace reference](#repositories-namespace-reference)
    
- [Populators namespace reference](#repositories-populator-namespace-reference)
    
- [Repository query keywords](#repositories-query-keywords-reference)
    
- [Repository query return types](#repositories-query-return-types-reference)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/index.html -->

<!-- page_index: 1 -->

# Spring Data Commons

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-data-commons"></a>

# Spring Data Commons

© 2008-2026 The original authors.

> [!NOTE]
> Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

<a id="index--preface"></a>

## Preface

The Spring Data Commons project applies core Spring concepts to the development of solutions using many relational and non-relational data stores.

<a id="index--project"></a>
<a id="index--project-metadata"></a>

## Project Metadata

- Version control: [github.com/spring-projects/spring-data-commons](https://github.com/spring-projects/spring-data-commons)
- Bugtracker: [github.com/spring-projects/spring-data-commons/issues](https://github.com/spring-projects/spring-data-commons/issues)
- Release repository: [repo1.maven.org/maven2/](https://repo1.maven.org/maven2/)
- Milestone repository: [repo.spring.io/milestone/](https://repo.spring.io/milestone/)
- Snapshot repository: [repo.spring.io/snapshot/](https://repo.spring.io/snapshot/)

---

<a id="dependencies"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/dependencies.html -->

<!-- page_index: 2 -->

# Dependencies

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="dependencies--page-title"></a>
<a id="dependencies--dependencies"></a>

# Dependencies

Due to the different inception dates of individual Spring Data modules, most of them carry different major and minor version numbers. The easiest way to find compatible ones is to rely on the Spring Data Release Train BOM that we ship with the compatible versions defined. In a Maven project, you would declare this dependency in the `<dependencyManagement />` section of your POM as follows:

Using the Spring Data release train BOM

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.data</groupId>
      <artifactId>spring-data-bom</artifactId>
      <version>2026.0.0</version>
      <scope>import</scope>
      <type>pom</type>
    </dependency>
  </dependencies>
</dependencyManagement>
```

The current release train version is `2026.0.0`. The train version uses [calver](https://calver.org/) with the pattern `YYYY.MINOR.MICRO`.
The version name follows `${calver}` for GA releases and service releases and the following pattern for all other versions: `${calver}-${modifier}`, where `modifier` can be one of the following:

- `SNAPSHOT`: Current snapshots
- `M1`, `M2`, and so on: Milestones
- `RC1`, `RC2`, and so on: Release candidates

You can find a working example of using the BOMs in our [Spring Data examples repository](https://github.com/spring-projects/spring-data-examples/tree/main/bom). With that in place, you can declare the Spring Data modules you would like to use without a version in the `<dependencies />` block, as follows:

Declaring a dependency to a Spring Data module such as JPA

```xml
<dependencies>
  <dependency>
    <groupId>org.springframework.data</groupId>
    <artifactId>spring-data-jpa</artifactId>
  </dependency>
</dependencies>
```

<a id="dependencies--dependencies.spring-boot"></a>
<a id="dependencies--dependency-management-with-spring-boot"></a>

## Dependency Management with Spring Boot

Spring Boot selects a recent version of the Spring Data modules for you. If you still want to upgrade to a newer version, set the `spring-data-bom.version` property to the [train version and iteration](#dependencies--dependencies.train-version)
you would like to use.

See Spring Boot’s [documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/dependency-versions.html#appendix.dependency-versions.properties)
(search for "Spring Data Bom") for more details.

<a id="dependencies--dependencies.spring-framework"></a>
<a id="dependencies--spring-framework"></a>

## Spring Framework

The current version of Spring Data modules require Spring Framework 7.0.8 or better. The modules might also work with an older bugfix version of that minor version. However, using the most recent version within that generation is highly recommended.

---

<a id="upgrade"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/upgrade.html -->

<!-- page_index: 3 -->

<a id="upgrade--page-title"></a>
<a id="upgrade--upgrading-spring-data"></a>

# Upgrading Spring Data

Instructions for how to upgrade from earlier versions of Spring Data are provided on the project [wiki](https://github.com/spring-projects/spring-data-commons/wiki).
Follow the links in the [release notes section](https://github.com/spring-projects/spring-data-commons/wiki#release-notes) to find the version that you want to upgrade to.

Upgrading instructions are always the first item in the release notes. If you are more than one release behind, please make sure that you also review the release notes of the versions that you jumped.

---

<a id="object-mapping"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/object-mapping.html -->

<!-- page_index: 4 -->

# Object Mapping Fundamentals

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="object-mapping--page-title"></a>
<a id="object-mapping--object-mapping-fundamentals"></a>

# Object Mapping Fundamentals

This section covers the fundamentals of Spring Data object mapping, object creation, field and property access, mutability and immutability.
Note, that this section only applies to Spring Data modules that do not use the object mapping of the underlying data store (like JPA).
Also be sure to consult the store-specific sections for store-specific object mapping, like indexes, customizing column or field names or the like.

Core responsibility of the Spring Data object mapping is to create instances of domain objects and map the store-native data structures onto those.
This means we need two fundamental steps:

1. Instance creation by using one of the constructors exposed.
2. Instance population to materialize all exposed properties.

<a id="object-mapping--mapping.object-creation"></a>
<a id="object-mapping--object-creation"></a>

## Object creation

Spring Data automatically tries to detect a persistent entity’s constructor to be used to materialize objects of that type.
The resolution algorithm works as follows:

1. If there is a single static factory method annotated with `@PersistenceCreator` then it is used.
2. If there is a single constructor, it is used.
3. If there are multiple constructors and exactly one is annotated with `@PersistenceCreator`, it is used.
4. If the type is a Java `Record` the canonical constructor is used.
5. If there’s a no-argument constructor, it is used.
   Other constructors will be ignored.

The value resolution assumes constructor/factory method argument names to match the property names of the entity, i.e. the resolution will be performed as if the property was to be populated, including all customizations in mapping (different datastore column or field name etc.).
This also requires either parameter names information available in the class file or an `@ConstructorProperties` annotation being present on the constructor.

The value resolution can be customized by using Spring Framework’s `@Value` value annotation using a store-specific SpEL expression.
Please consult the section on store specific mappings for further details.

<a id="object-mapping--mapping.property-population"></a>
<a id="object-mapping--property-population"></a>

## Property population

Once an instance of the entity has been created, Spring Data populates all remaining persistent properties of that class.
Unless already populated by the entity’s constructor (i.e. consumed through its constructor argument list), the identifier property will be populated first to allow the resolution of cyclic object references.
After that, all non-transient properties that have not already been populated by the constructor are set on the entity instance.
For that we use the following algorithm:

1. If the property is immutable but exposes a `with…` method (see below), we use the `with…` method to create a new entity instance with the new property value.
2. If property access (i.e. access through getters and setters) is defined, we’re invoking the setter method.
3. If the property is mutable we set the field directly.
4. If the property is immutable we’re using the constructor to be used by persistence operations (see [Object creation](#object-mapping--mapping.object-creation)) to create a copy of the instance.
5. By default, we set the field value directly.

Let’s have a look at the following entity:

A sample entity

```java
class Person {

  private final @Id Long id;                                                (1)
  private final String firstname, lastname;                                 (2)
  private final LocalDate birthday;
  private final int age;                                                    (3)

  private String comment;                                                   (4)
  private @AccessType(Type.PROPERTY) String remarks;                        (5)
  private @Transient String summary;                                        (6)

  static Person of(String firstname, String lastname, LocalDate birthday) { (7)

    return new Person(null, firstname, lastname, birthday,
      Period.between(birthday, LocalDate.now()).getYears());
  }

  Person(Long id, String firstname, String lastname, LocalDate birthday, int age) { (7)

    this.id = id;
    this.firstname = firstname;
    this.lastname = lastname;
    this.birthday = birthday;
    this.age = age;
  }

  Person withId(Long id) {                                                  (1)
    return new Person(id, this.firstname, this.lastname, this.birthday, this.age);
  }

  void setRemarks(String remarks) {                                         (5)
    this.remarks = remarks;
  }
}
```

**1**

The identifier property is final but set to `null` in the constructor.
The class exposes a `withId(…)` method that’s used to set the identifier, e.g. when an instance is inserted into the datastore and an identifier has been generated.
The original `Person` instance stays unchanged as a new one is created.
The same pattern is usually applied for other properties that are store managed but might have to be changed for persistence operations.
The wither method is optional as the persistence constructor (see 6) is effectively a copy constructor and setting the property will be translated into creating a fresh instance with the new identifier value applied.

**2**

The `firstname` and `lastname` properties are ordinary immutable properties potentially exposed through getters.

**3**

The `age` property is an immutable but derived one from the `birthday` property.
With the design shown, the database value will trump the defaulting as Spring Data uses the only declared constructor.
Even if the intent is that the calculation should be preferred, it’s important that this constructor also takes `age` as parameter (to potentially ignore it) as otherwise the property population step will attempt to set the age field and fail due to it being immutable and no `with…` method being present.

**4**

The `comment` property is mutable and is populated by setting its field directly.

**5**

The `remarks` property is mutable and is populated by invoking the setter method.

**6**

The `summary` property transient and will not be persisted as it is annotated with `@Transient`.
Spring Data doesn’t use Java’s `transient` keyword to exclude properties from being persisted as `transient` is part of the Java Serialization Framework.
Note that this property can be used with a persistence constructor, but its value will default to `null` (or the respective primitive initial value if the property type was a primitive one).

**7**

The class exposes a factory method and a constructor for object creation.
The core idea here is to use factory methods instead of additional constructors to avoid the need for constructor disambiguation through `@PersistenceCreator`.
Instead, defaulting of properties is handled within the factory method.
If you want Spring Data to use the factory method for object instantiation, annotate it with `@PersistenceCreator`.

<a id="object-mapping--mapping.general-recommendations"></a>
<a id="object-mapping--general-recommendations"></a>

## General recommendations

- *Try to stick to immutable objects* — Immutable objects are straightforward to create as materializing an object is then a matter of calling its constructor only.
  Also, this avoids littering your domain objects with setter methods that allow client code to manipulate the object’s state.
  If you need those, prefer to make them package protected so that they can only be invoked by a limited amount of co-located types.
  Constructor-only materialization is up to 30% faster than properties population.
- *Provide an all-args constructor* — Even if you cannot or don’t want to model your entities as immutable values, there’s still value in providing a constructor that takes all properties of the entity as arguments, including the mutable ones, as this allows the object mapping to skip the property population for optimal performance.
- *Use factory methods instead of overloaded constructors to avoid `@PersistenceCreator`* — With an all-argument constructor needed for optimal performance, we usually want to expose more application use case specific constructors that omit things like auto-generated identifiers etc.
  It’s an established pattern to rather use static factory methods to expose these variants of the all-args constructor.
- *Make sure you adhere to the constraints that allow the generated instantiator and property accessor classes to be used* —
- *For identifiers to be generated, still use a final field in combination with an all-arguments persistence constructor (preferred) or a `with…` method* —
- *Use Lombok to avoid boilerplate code* — As persistence operations usually require a constructor taking all arguments, their declaration becomes a tedious repetition of boilerplate parameter to field assignments that can best be avoided by using Lombok’s `@AllArgsConstructor`.

<a id="object-mapping--mapping.general-recommendations.override.properties"></a>
<a id="object-mapping--overriding-properties"></a>

### Overriding Properties

Java allows a flexible design of domain classes where a subclass could define a property that is already declared with the same name in its superclass.
Consider the following example:

```java
public class SuperType {
private CharSequence field;
public SuperType(CharSequence field) {this.field = field;}
public CharSequence getField() {return this.field;}
public void setField(CharSequence field) {this.field = field;}}
public class SubType extends SuperType {
private String field;
public SubType(String field) {super(field); this.field = field;}
@Override public String getField() {return this.field;}
public void setField(String field) {this.field = field;
// optional super.setField(field);}}
```

Both classes define a `field` using assignable types. `SubType` however shadows `SuperType.field`.
Depending on the class design, using the constructor could be the only default approach to set `SuperType.field`.
Alternatively, calling `super.setField(…)` in the setter could set the `field` in `SuperType`.
All these mechanisms create conflicts to some degree because the properties share the same name yet might represent two distinct values.
Spring Data skips super-type properties if types are not assignable.
That is, the type of the overridden property must be assignable to its super-type property type to be registered as override, otherwise the super-type property is considered transient.
We generally recommend using distinct property names.

Spring Data modules generally support overridden properties holding different values.
From a programming model perspective there are a few things to consider:

1. Which property should be persisted (default to all declared properties)?
   You can exclude properties by annotating these with `@Transient`.
2. How to represent properties in your data store?
   Using the same field/column name for different values typically leads to corrupt data so you should annotate least one of the properties using an explicit field/column name.
3. Using `@AccessType(PROPERTY)` cannot be used as the super-property cannot be generally set without making any further assumptions of the setter implementation.

<a id="object-mapping--mapping.kotlin"></a>
<a id="object-mapping--kotlin-support"></a>

## Kotlin support

Spring Data adapts specifics of Kotlin to allow object creation and mutation.

<a id="object-mapping--mapping.kotlin.creation"></a>
<a id="object-mapping--kotlin-object-creation"></a>

### Kotlin object creation

Kotlin classes are supported to be instantiated, all classes are immutable by default and require explicit property declarations to define mutable properties.

Spring Data automatically tries to detect a persistent entity’s constructor to be used to materialize objects of that type.
The resolution algorithm works as follows:

1. If there is a constructor that is annotated with `@PersistenceCreator`, it is used.
2. If the type is a [Kotlin data class](#object-mapping--mapping.kotlin) the primary constructor is used.
3. If there is a single static factory method annotated with `@PersistenceCreator` then it is used.
4. If there is a single constructor, it is used.
5. If there are multiple constructors and exactly one is annotated with `@PersistenceCreator`, it is used.
6. If the type is a Java `Record` the canonical constructor is used.
7. If there’s a no-argument constructor, it is used.
   Other constructors will be ignored.

Consider the following `data` class `Person`:

```kotlin
data class Person(val id: String, val name: String)
```

The class above compiles to a typical class with an explicit constructor. We can customize this class by adding another constructor and annotate it with `@PersistenceCreator` to indicate a constructor preference:

```kotlin
data class Person(var id: String, val name: String) {

    @PersistenceCreator
    constructor(id: String) : this(id, "unknown")
}
```

Kotlin supports parameter optionality by allowing default values to be used if a parameter is not provided.
When Spring Data detects a constructor with parameter defaulting, then it leaves these parameters absent if the data store does not provide a value (or simply returns `null`) so Kotlin can apply parameter defaulting. Consider the following class that applies parameter defaulting for `name`

```kotlin
data class Person(var id: String, val name: String = "unknown")
```

Every time the `name` parameter is either not part of the result or its value is `null`, then the `name` defaults to `unknown`.

> [!NOTE]
> Delegated properties are not supported with Spring Data. The mapping metadata filters delegated properties for Kotlin Data classes.
> In all other cases you can exclude synthetic fields for delegated properties by annotating the property with [`@Transient`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/annotation/Transient.html).

<a id="object-mapping--property-population-of-kotlin-data-classes"></a>

### Property population of Kotlin data classes

In Kotlin, all classes are immutable by default and require explicit property declarations to define mutable properties.
Consider the following `data` class `Person`:

```kotlin
data class Person(val id: String, val name: String)
```

This class is effectively immutable.
It allows creating new instances as Kotlin generates a `copy(…)` method that creates new object instances copying all property values from the existing object and applying property values provided as arguments to the method.

<a id="object-mapping--mapping.kotlin.override.properties"></a>
<a id="object-mapping--kotlin-overriding-properties"></a>

### Kotlin Overriding Properties

Kotlin allows declaring [property overrides](https://kotlinlang.org/docs/inheritance.html#overriding-properties) to alter properties in subclasses.

```kotlin
open class SuperType(open var field: Int)

class SubType(override var field: Int = 1) :
	SuperType(field) {
}
```

Such an arrangement renders two properties with the name `field`.
Kotlin generates property accessors (getters and setters) for each property in each class.
Effectively, the code looks like as follows:

```java
public class SuperType {
private int field;
public SuperType(int field) {this.field = field;}
public int getField() {return this.field;}
public void setField(int field) {this.field = field;}}
public final class SubType extends SuperType {
private int field;
public SubType(int field) {super(field); this.field = field;}
public int getField() {return this.field;}
public void setField(int field) {this.field = field;}}
```

Getters and setters on `SubType` set only `SubType.field` and not `SuperType.field`.
In such an arrangement, using the constructor is the only default approach to set `SuperType.field`.
Adding a method to `SubType` to set `SuperType.field` via `this.SuperType.field = …` is possible but falls outside of supported conventions.
Property overrides create conflicts to some degree because the properties share the same name yet might represent two distinct values.
We generally recommend using distinct property names.

Spring Data modules generally support overridden properties holding different values.
From a programming model perspective there are a few things to consider:

1. Which property should be persisted (default to all declared properties)?
   You can exclude properties by annotating these with `@Transient`.
2. How to represent properties in your data store?
   Using the same field/column name for different values typically leads to corrupt data so you should annotate least one of the properties using an explicit field/column name.
3. Using `@AccessType(PROPERTY)` cannot be used as the super-property cannot be set.

<a id="object-mapping--mapping.kotlin.value.classes"></a>
<a id="object-mapping--kotlin-value-classes"></a>

### Kotlin Value Classes

Kotlin Value Classes are designed for a more expressive domain model to make underlying concepts explicit.
Spring Data can read and write types that define properties using Value Classes.

Consider the following domain model:

```kotlin
@JvmInline
value class EmailAddress(val theAddress: String)                                    (1)

data class Contact(val id: String, val name:String, val emailAddress: EmailAddress) (2)
```

**1**

A simple value class with a non-nullable value type.

**2**

Data class defining a property using the `EmailAddress` value class.

> [!NOTE]
> Non-nullable properties using non-primitive value types are flattened in the compiled class to the value type.
> Nullable primitive value types or nullable value-in-value types are represented with their wrapper type and that affects how value types are represented in the database.

---

<a id="repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories.html -->

<!-- page_index: 5 -->

# Working with Spring Data Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories--page-title"></a>
<a id="repositories--working-with-spring-data-repositories"></a>

# Working with Spring Data Repositories

The goal of the Spring Data repository abstraction is to significantly reduce the amount of boilerplate code required to implement data access layers for various persistence stores.

> [!IMPORTANT]
> *Spring Data repository documentation and your module*
>
> This chapter explains the core concepts and interfaces of Spring Data repositories.
> The information in this chapter is pulled from the Spring Data Commons module.
> It uses the configuration and code samples for the Jakarta Persistence API (JPA) module.
> If you want to use XML configuration you should adapt the XML namespace declaration and the types to be extended to the equivalents of the particular module that you use. “[Namespace reference](#repositories-namespace-reference--repositories.namespace-reference)” covers XML configuration, which is supported across all Spring Data modules that support the repository API.
> “[Repository query keywords](#repositories-query-keywords-reference)” covers the query method keywords supported by the repository abstraction in general.
> For detailed information on the specific features of your module, see the chapter on that module of this document.

---

<a id="repositories-core-concepts"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/core-concepts.html -->

<!-- page_index: 6 -->

# Core concepts

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-core-concepts--page-title"></a>
<a id="repositories-core-concepts--core-concepts"></a>

# Core concepts

The central interface in the Spring Data repository abstraction is `Repository`.
It takes the domain class to manage as well as the identifier type of the domain class as type arguments.
This interface acts primarily as a marker interface to capture the types to work with and to help you to discover interfaces that extend this one.

> [!TIP]
> Spring Data considers domain types to be entities, more specifically aggregates.
> So you will see the term "entity" used throughout the documentation that can be interchanged with the term "domain type" or "aggregate".
>
> As you might have noticed in the introduction it already hinted towards domain-driven concepts.
> We consider domain objects in the sense of DDD.
> Domain objects have identifiers (otherwise these would be identity-less value objects), and we somehow need to refer to identifiers when working with certain patterns to access data.
> Referring to identifiers will become more meaningful as we talk about repositories and query methods.

The [`CrudRepository`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/CrudRepository.html) and [`ListCrudRepository`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/ListCrudRepository.html) interfaces provide sophisticated CRUD functionality for the entity class that is being managed.

`CrudRepository` Interface

```java
public interface CrudRepository<T, ID> extends Repository<T, ID> {

  <S extends T> S save(S entity);      (1)

  Optional<T> findById(ID primaryKey); (2)

  Iterable<T> findAll();               (3)

  long count();                        (4)

  void delete(T entity);               (5)

  boolean existsById(ID primaryKey);   (6)

  // … more functionality omitted.
}
```

| **1** | Saves the given entity. |
| --- | --- |
| **2** | Returns the entity identified by the given ID. |
| **3** | Returns all entities. |
| **4** | Returns the number of entities. |
| **5** | Deletes the given entity. |
| **6** | Indicates whether an entity with the given ID exists. |

The methods declared in this interface are commonly referred to as CRUD methods.
`ListCrudRepository` offers equivalent methods, but they return `List` where the `CrudRepository` methods return an `Iterable`.

> [!IMPORTANT]
> The repository interface implies a few reserved methods like `findById(ID identifier)` that target the domain type identifier property regardless of its property name.
> Read more about this in “[Defining Query Methods](#repositories-query-methods-details--repositories.query-methods.reserved-methods)”.
>
> You can annotate your query method with `@Query` to provide a custom query if a property named `Id` doesn’t refer to the identifier.
> Following that path can easily lead to confusion and is discouraged as you will quickly hit type limits if the `ID` type and the type of your `Id` property deviate.

> [!NOTE]
> We also provide persistence technology-specific abstractions, such as `JpaRepository` or `MongoRepository`.
> Those interfaces extend `CrudRepository` and expose the capabilities of the underlying persistence technology in addition to the rather generic persistence technology-agnostic interfaces such as `CrudRepository`.

In addition to `CrudRepository`, there are [`PagingAndSortingRepository`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/PagingAndSortingRepository.html) and [`ListPagingAndSortingRepository`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/ListPagingAndSortingRepository.html) which add additional methods to ease paginated access to entities:

`PagingAndSortingRepository` interface

```java
interface PagingAndSortingRepository<T, ID> extends Repository<T, ID> {

  Iterable<T> findAll(Sort sort);

  Page<T> findAll(Pageable pageable);
}
```

> [!NOTE]
> Extension interfaces are subject to be supported by the actual store module.
> While this documentation explains the general scheme, make sure that your store module supports the interfaces that you want to use.

To access the second page of `User` by a page size of 20, you could do something like the following:

```java
PagingAndSortingRepository<User, Long> repository = // … get access to a bean
Page<User> users = repository.findAll(PageRequest.of(1, 20));
```

`ListPagingAndSortingRepository` offers equivalent methods, but returns a `List` where the `PagingAndSortingRepository` methods return an `Iterable`.

In addition to pagination, scrolling provides a more fine-grained access to iterate through chunks of larger result sets.

In addition to query methods, query derivation for both count and delete queries is available.
The following list shows the interface definition for a derived count query:

Derived Count Query

```java
interface UserRepository extends CrudRepository<User, Long> {

  long countByLastname(String lastname);
}
```

The following listing shows the interface definition for a derived delete query:

Derived Delete Query

```java
interface UserRepository extends CrudRepository<User, Long> {

  long deleteByLastname(String lastname);

  List<User> removeByLastname(String lastname);
}
```

---

<a id="repositories-query-methods"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/query-methods.html -->

<!-- page_index: 7 -->

# Query Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-methods--page-title"></a>
<a id="repositories-query-methods--query-methods"></a>

# Query Methods

Standard CRUD functionality repositories usually have queries on the underlying datastore.
With Spring Data, declaring those queries becomes a four-step process:

1. Declare an interface extending Repository or one of its subinterfaces and type it to the domain class and ID type that it should handle, as shown in the following example:


```java
interface PersonRepository extends Repository<Person, Long> { … }
```

2. Declare query methods on the interface.


```java
interface PersonRepository extends Repository<Person, Long> {
  List<Person> findByLastname(String lastname);
}
```

3. Set up Spring to create proxy instances for those interfaces, either with [JavaConfig](#repositories-create-instances--repositories.create-instances.java-config) or with [XML configuration](#repositories-create-instances).

   - Java
   - XML


```java
import org.springframework.data.….repository.config.EnableJpaRepositories;

@EnableJpaRepositories
class Config { … }
```


```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns:jpa="http://www.springframework.org/schema/data/jpa"
   xsi:schemaLocation="http://www.springframework.org/schema/beans
     https://www.springframework.org/schema/beans/spring-beans.xsd
     http://www.springframework.org/schema/data/jpa
     https://www.springframework.org/schema/data/jpa/spring-jpa.xsd">

   <repositories base-package="com.acme.repositories"/>

</beans>
```

   The JPA namespace is used in this example.
   If you use the repository abstraction for any other store, you need to change this to the appropriate namespace declaration of your store module.
   In other words, you should exchange `jpa` in favor of, for example, `mongodb`.

   Note that the JavaConfig variant does not configure a package explicitly, because the package of the annotated class is used by default.
   To customize the package to scan, use one of the `basePackage…` attributes of the data-store-specific repository’s `@EnableJpaRepositories`-annotation.
4. Inject the repository instance and use it, as shown in the following example:


```java
class SomeClient {
private final PersonRepository repository;
SomeClient(PersonRepository repository) {this.repository = repository;}
void doSomething() {List<Person> persons = repository.findByLastname("Matthews");}}
```

The sections that follow explain each step in detail:

- [Defining Repository Interfaces](#repositories-definition)
- [Defining Query Methods](#repositories-query-methods-details)
- [Creating Repository Instances](#repositories-create-instances)
- [Custom Implementations for Spring Data Repositories](#repositories-custom-implementations)

---

<a id="repositories-definition"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/definition.html -->

<!-- page_index: 8 -->

# Defining Repository Interfaces

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-definition--page-title"></a>
<a id="repositories-definition--defining-repository-interfaces"></a>

# Defining Repository Interfaces

To define a repository interface, you first need to define a domain class-specific repository interface.
The interface must extend `Repository` and be typed to the domain class and an ID type.
If you want to expose CRUD methods for that domain type, you may extend `CrudRepository`, or one of its variants instead of `Repository`.

<a id="repositories-definition--repositories.definition-tuning"></a>
<a id="repositories-definition--fine-tuning-repository-definition"></a>

## Fine-tuning Repository Definition

There are a few ways to get started with your repository interface.

The typical approach is to extend `CrudRepository`, which gives you methods for CRUD functionality.
CRUD stands for Create, Read, Update, Delete.
With version 3.0 we also introduced `ListCrudRepository` which is very similar to the `CrudRepository` but for those methods that return multiple entities it returns a `List` instead of an `Iterable` which you might find easier to use.

If you are using a reactive store you might choose `ReactiveCrudRepository`, or `RxJava3CrudRepository` depending on which reactive framework you are using.

If you are using Kotlin you might pick `CoroutineCrudRepository` which utilizes Kotlin’s coroutines.

Additionally you can extend `PagingAndSortingRepository`, `ReactiveSortingRepository`, `RxJava3SortingRepository`, or `CoroutineSortingRepository` if you need methods that allow to specify a `Sort` abstraction or in the first case a `Pageable` abstraction.
Note that the various sorting repositories no longer extend their respective CRUD repository as they did in Spring Data versions prior to 3.0.
Therefore, you need to extend both interfaces if you want functionality of both.

If you do not want to extend Spring Data interfaces, you can also annotate your repository interface with `@RepositoryDefinition`.
Extending one of the CRUD repository interfaces exposes a complete set of methods to manipulate your entities.
If you prefer to be selective about the methods being exposed, copy the methods you want to expose from the CRUD repository into your domain repository.
When doing so, you may change the return type of methods.
Spring Data will honor the return type if possible.
For example, for methods returning multiple entities you may choose `Iterable<T>`, `List<T>`, `Collection<T>` or a VAVR list.

If many repositories in your application should have the same set of methods you can define your own base interface to inherit from.
Such an interface must be annotated with `@NoRepositoryBean`.
This prevents Spring Data to try to create an instance of it directly and failing because it can’t determine the entity for that repository, since it still contains a generic type variable.

The following example shows how to selectively expose CRUD methods (`findById` and `save`, in this case):

Selectively exposing CRUD methods

```java
@NoRepositoryBean interface MyBaseRepository<T, ID> extends Repository<T, ID> {
Optional<T> findById(ID id);
<S extends T> S save(S entity);}
interface UserRepository extends MyBaseRepository<User, Long> {User findByEmailAddress(EmailAddress emailAddress);}
```

In the prior example, you defined a common base interface for all your domain repositories and exposed `findById(…)` as well as `save(…)`.These methods are routed into the base repository implementation of the store of your choice provided by Spring Data (for example, if you use JPA, the implementation is `SimpleJpaRepository`), because they match the method signatures in `CrudRepository`.
So the `UserRepository` can now save users, find individual users by ID, and trigger a query to find `Users` by email address.

> [!NOTE]
> The intermediate repository interface is annotated with `@NoRepositoryBean`.
> Make sure you add that annotation to all repository interfaces for which Spring Data should not create instances at runtime.

<a id="repositories-definition--repositories.multiple-modules"></a>
<a id="repositories-definition--using-repositories-with-multiple-spring-data-modules"></a>

## Using Repositories with Multiple Spring Data Modules

Using a unique Spring Data module in your application makes things simple, because all repository interfaces in the defined scope are bound to the Spring Data module.
Sometimes, applications require using more than one Spring Data module.
In such cases, a repository definition must distinguish between persistence technologies.
When it detects multiple repository factories on the class path, Spring Data enters strict repository configuration mode.
Strict configuration uses details on the repository or the domain class to decide about Spring Data module binding for a repository definition:

1. If the repository definition [extends the module-specific repository](#repositories-definition--repositories.multiple-modules.types), it is a valid candidate for the particular Spring Data module.
2. If the domain class is [annotated with the module-specific type annotation](#repositories-definition--repositories.multiple-modules.annotations), it is a valid candidate for the particular Spring Data module.
   Spring Data modules accept either third-party annotations (such as JPA’s `@Entity`) or provide their own annotations (such as `@Document` for Spring Data MongoDB and Spring Data Elasticsearch).

The following example shows a repository that uses module-specific interfaces (JPA in this case):

Example 1. Repository definitions using module-specific interfaces

```java
interface MyRepository extends JpaRepository<User, Long> { }

@NoRepositoryBean
interface MyBaseRepository<T, ID> extends JpaRepository<T, ID> { … }

interface UserRepository extends MyBaseRepository<User, Long> { … }
```

`MyRepository` and `UserRepository` extend `JpaRepository` in their type hierarchy.
They are valid candidates for the Spring Data JPA module.

The following example shows a repository that uses generic interfaces:

Example 2. Repository definitions using generic interfaces

```java
interface AmbiguousRepository extends Repository<User, Long> { … }

@NoRepositoryBean
interface MyBaseRepository<T, ID> extends CrudRepository<T, ID> { … }

interface AmbiguousUserRepository extends MyBaseRepository<User, Long> { … }
```

`AmbiguousRepository` and `AmbiguousUserRepository` extend only `Repository` and `CrudRepository` in their type hierarchy.
While this is fine when using a unique Spring Data module, multiple modules cannot distinguish to which particular Spring Data these repositories should be bound.

The following example shows a repository that uses domain classes with annotations:

Example 3. Repository definitions using domain classes with annotations

```java
interface PersonRepository extends Repository<Person, Long> { … }

@Entity
class Person { … }

interface UserRepository extends Repository<User, Long> { … }

@Document
class User { … }
```

`PersonRepository` references `Person`, which is annotated with the JPA `@Entity` annotation, so this repository clearly belongs to Spring Data JPA. `UserRepository` references `User`, which is annotated with Spring Data MongoDB’s `@Document` annotation.

The following bad example shows a repository that uses domain classes with mixed annotations:

Example 4. Repository definitions using domain classes with mixed annotations

```java
interface JpaPersonRepository extends Repository<Person, Long> { … }

interface MongoDBPersonRepository extends Repository<Person, Long> { … }

@Entity
@Document
class Person { … }
```

This example shows a domain class using both JPA and Spring Data MongoDB annotations.
It defines two repositories, `JpaPersonRepository` and `MongoDBPersonRepository`.
One is intended for JPA and the other for MongoDB usage.
Spring Data is no longer able to tell the repositories apart, which leads to undefined behavior.

[Repository type details](#repositories-definition--repositories.multiple-modules.types) and [distinguishing domain class annotations](#repositories-definition--repositories.multiple-modules.annotations) are used for strict repository configuration to identify repository candidates for a particular Spring Data module.
Using multiple persistence technology-specific annotations on the same domain type is possible and enables reuse of domain types across multiple persistence technologies.
However, Spring Data can then no longer determine a unique module with which to bind the repository.

The last way to distinguish repositories is by scoping repository base packages.
Base packages define the starting points for scanning for repository interface definitions, which implies having repository definitions located in the appropriate packages.
By default, annotation-driven configuration uses the package of the configuration class.
The [base package in XML-based configuration](#repositories-create-instances--repositories.create-instances.xml) is mandatory.

The following example shows annotation-driven configuration of base packages:

Annotation-driven configuration of base packages

```java
@EnableJpaRepositories(basePackages = "com.acme.repositories.jpa")
@EnableMongoRepositories(basePackages = "com.acme.repositories.mongo")
class Configuration { … }
```

---

<a id="repositories-query-methods-details"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/query-methods-details.html -->

<!-- page_index: 9 -->

# Defining Query Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-methods-details--page-title"></a>
<a id="repositories-query-methods-details--defining-query-methods"></a>

# Defining Query Methods

The repository proxy has two ways to derive a store-specific query from the method name:

- By deriving the query from the method name directly.
- By using a manually defined query.

Available options depend on the actual store.
However, there must be a strategy that decides what actual query is created.
The next section describes the available options.

<a id="repositories-query-methods-details--repositories.query-methods.query-lookup-strategies"></a>
<a id="repositories-query-methods-details--query-lookup-strategies"></a>

## Query Lookup Strategies

The following strategies are available for the repository infrastructure to resolve the query.
With XML configuration, you can configure the strategy at the namespace through the `query-lookup-strategy` attribute.
For Java configuration, you can use the `queryLookupStrategy` attribute of the `EnableJpaRepositories` annotation.
Some strategies may not be supported for particular datastores.

- `CREATE` attempts to construct a store-specific query from the query method name.
  The general approach is to remove a given set of well known prefixes from the method name and parse the rest of the method.
  You can read more about query construction in “[Query Creation](#repositories-query-methods-details--repositories.query-methods.query-creation)”.
- `USE_DECLARED_QUERY` tries to find a declared query and throws an exception if it cannot find one.
  The query can be defined by an annotation somewhere or declared by other means.
  See the documentation of the specific store to find available options for that store.
  If the repository infrastructure does not find a declared query for the method at bootstrap time, it fails.
- `CREATE_IF_NOT_FOUND` (the default) combines `CREATE` and `USE_DECLARED_QUERY`.
  It looks up a declared query first, and, if no declared query is found, it creates a custom method name-based query.
  This is the default lookup strategy and, thus, is used if you do not configure anything explicitly.
  It allows quick query definition by method names but also custom-tuning of these queries by introducing declared queries as needed.

<a id="repositories-query-methods-details--repositories.query-methods.query-creation"></a>
<a id="repositories-query-methods-details--query-creation"></a>

## Query Creation

The query builder mechanism built into the Spring Data repository infrastructure is useful for building constraining queries over entities of the repository.

The following example shows how to create a number of queries:

Query creation from method names

```java
interface PersonRepository extends Repository<Person, Long> {

  List<Person> findByEmailAddressAndLastname(EmailAddress emailAddress, String lastname);

  // Enables the distinct flag for the query
  List<Person> findDistinctPeopleByLastnameOrFirstname(String lastname, String firstname);
  List<Person> findPeopleDistinctByLastnameOrFirstname(String lastname, String firstname);

  // Enabling ignoring case for an individual property
  List<Person> findByLastnameIgnoreCase(String lastname);
  // Enabling ignoring case for all suitable properties
  List<Person> findByLastnameAndFirstnameAllIgnoreCase(String lastname, String firstname);

  // Enabling static ORDER BY for a query
  List<Person> findByLastnameOrderByFirstnameAsc(String lastname);
  List<Person> findByLastnameOrderByFirstnameDesc(String lastname);
}
```

Parsing query method names is divided into subject and predicate.
The first part (`find…By`, `exists…By`) defines the subject of the query, the second part forms the predicate.
The introducing clause (subject) can contain further expressions.
Any text between `find` (or other introducing keywords) and `By` is considered to be descriptive unless using one of the result-limiting keywords such as a `Distinct` to set a distinct flag on the query to be created or [`Top`/`First` to limit query results](#repositories-query-methods-details--repositories.limit-query-result).

The appendix contains the [full list of query method subject keywords](#repositories-query-keywords-reference--appendix.query.method.subject) and [query method predicate keywords including sorting and letter-casing modifiers](#repositories-query-keywords-reference--appendix.query.method.predicate).
However, the first `By` acts as a delimiter to indicate the start of the actual criteria predicate.
At a very basic level, you can define conditions on entity properties and concatenate them with `And` and `Or`.

The actual result of parsing the method depends on the persistence store for which you create the query.
However, there are some general things to notice:

- The expressions are usually property traversals combined with operators that can be concatenated.
  You can combine property expressions with `AND` and `OR`.
  You also get support for operators such as `Between`, `LessThan`, `GreaterThan`, and `Like` for the property expressions.
  The supported operators can vary by datastore, so consult the appropriate part of your reference documentation.
- The method parser supports setting an `IgnoreCase` flag for individual properties (for example, `findByLastnameIgnoreCase(…)`) or for all properties of a type that supports ignoring case (usually `String` instances — for example, `findByLastnameAndFirstnameAllIgnoreCase(…)`).
  Whether ignoring cases is supported may vary by store, so consult the relevant sections in the reference documentation for the store-specific query method.
- You can apply static ordering by appending an `OrderBy` clause to the query method that references a property and by providing a sorting direction (`Asc` or `Desc`).
  To create a query method that supports dynamic sorting, see “[Paging, Iterating Large Results, Sorting & Limiting](#repositories-query-methods-details--repositories.special-parameters)”.

<a id="repositories-query-methods-details--repositories.query-methods.reserved-methods"></a>
<a id="repositories-query-methods-details--reserved-method-names"></a>

## Reserved Method Names

While derived repository methods bind to properties by name, there are a few exceptions to this rule when it comes to certain method names inherited from the base repository targeting the *identifier* property.
Those *reserved methods* like `CrudRepository#findById` (or just `findById`) are targeting the *identifier* property regardless of the actual property name used in the declared method.

Consider the following domain type holding a property `pk` marked as the identifier via `@Id` and a property called `id`.
In this case you need to pay close attention to the naming of your lookup methods as they may collide with predefined signatures:

```java
class User {
  @Id Long pk;                          (1)

  Long id;                              (2)

  // …
}

interface UserRepository extends Repository<User, Long> {

  Optional<User> findById(Long id);     (3)

  Optional<User> findByPk(Long pk);     (4)

  Optional<User> findUserById(Long id); (5)
}
```

| **1** | The identifier property (primary key). |
| --- | --- |
| **2** | A property named `id`, but not the identifier. |
| **3** | Targets the `pk` property (the one marked with `@Id` which is considered to be the identifier) as it refers to a `CrudRepository` base repository method. Therefore, it is not a derived query using of `id` as the property name would suggest because it is one of the *reserved methods*. |
| **4** | Targets the `pk` property by name as it is a derived query. |
| **5** | Targets the `id` property by using the descriptive token between `find` and `by` to avoid collisions with *reserved methods*. |

This special behaviour not only targets lookup methods but also applies to the `exists` and `delete` ones.
Please refer to the “[Repository query keywords](#repositories-query-keywords-reference--appendix.query.method.reserved)” for the list of methods.

<a id="repositories-query-methods-details--repositories.query-methods.query-property-expressions"></a>
<a id="repositories-query-methods-details--property-expressions"></a>

## Property Expressions

Property expressions can refer only to a direct property of the managed entity, as shown in the preceding example.
At query creation time, you already make sure that the parsed property is a property of the managed domain class.
However, you can also define constraints by traversing nested properties.
Consider the following method signature:

```java
List<Person> findByAddressZipCode(ZipCode zipCode);
```

Assume a `Person` has an `Address` with a `ZipCode`.
In that case, the method creates the `x.address.zipCode` property traversal.
The resolution algorithm starts by interpreting the entire part (`AddressZipCode`) as the property and checks the domain class for a property with that name (uncapitalized).
If the algorithm succeeds, it uses that property.
If not, the algorithm splits up the source at the camel-case parts from the right side into a head and a tail and tries to find the corresponding property — in our example, `AddressZip` and `Code`.
If the algorithm finds a property with that head, it takes the tail and continues building the tree down from there, splitting the tail up in the way just described.
If the first split does not match, the algorithm moves the split point to the left (`Address`, `ZipCode`) and continues.

Although this should work for most cases, it is possible for the algorithm to select the wrong property.
Suppose the `Person` class has an `addressZip` property as well.
The algorithm would match in the first split round already, choose the wrong property, and fail (as the type of `addressZip` probably has no `code` property).

To resolve this ambiguity you can use `_` inside your method name to manually define traversal points.
So our method name would be as follows:

```java
List<Person> findByAddress_ZipCode(ZipCode zipCode);
```

> [!NOTE]
> Because we treat underscores (`_`) as a reserved character, we strongly advise to follow standard Java naming conventions (that is, not using underscores in property names but applying camel case instead).

> [!WARNING]
> Field Names starting with underscore:
>
> Field names may start with underscores like `String _name`.
> Make sure to preserve the `_` as in `_name` and use double `_` to split nested paths like `user__name`.
>
> Upper Case Field Names:
>
> Field names that are all uppercase can be used as such.
> Nested paths if applicable require splitting via `_` as in `USER_name`.
>
> Field Names with 2nd uppercase letter:
>
> Field names that consist of a starting lower case letter followed by an uppercase one like `String qCode` can be resolved by starting with two upper case letters as in `QCode`.
> Please be aware of potential path ambiguities.
>
> Path Ambiguities:
>
> In the following sample the arrangement of properties `qCode` and `q`, with `q` containing a property called `code`, creates an ambiguity for the path `QCode`.
>
> ```java
> record Container(String qCode, Code q) {}
> record Code(String code) {}
> ```
>
> Since a direct match on a property is considered first, any potential nested paths will not be considered and the algorithm picks the `qCode` field.
> In order to select the `code` field in `q` the underscore notation `Q_Code` is required.

<a id="repositories-query-methods-details--repositories.collections-and-iterables"></a>
<a id="repositories-query-methods-details--repository-methods-returning-collections-or-iterables"></a>

## Repository Methods Returning Collections or Iterables

Query methods that return multiple results can use standard Java `Iterable`, `List`, and `Set`.
Beyond that, we support returning Spring Data’s `Streamable`, a custom extension of `Iterable`, as well as collection types provided by [Vavr](https://www.vavr.io/).
Refer to the appendix explaining all possible [query method return types](#repositories-query-return-types-reference--appendix.query.return.types).

<a id="repositories-query-methods-details--repositories.collections-and-iterables.streamable"></a>
<a id="repositories-query-methods-details--using-streamable-as-query-method-return-type"></a>

### Using Streamable as Query Method Return Type

You can use `Streamable` as alternative to `Iterable` or any collection type.
It provides convenience methods to access a non-parallel `Stream` (missing from `Iterable`) and the ability to directly `….filter(…)` and `….map(…)` over the elements and concatenate the `Streamable` to others:

Using Streamable to combine query method results

```java
interface PersonRepository extends Repository<Person, Long> {
  Streamable<Person> findByFirstnameContaining(String firstname);
  Streamable<Person> findByLastnameContaining(String lastname);
}

Streamable<Person> result = repository.findByFirstnameContaining("av")
  .and(repository.findByLastnameContaining("ea"));
```

<a id="repositories-query-methods-details--repositories.collections-and-iterables.streamable-wrapper"></a>
<a id="repositories-query-methods-details--returning-custom-streamable-wrapper-types"></a>

### Returning Custom Streamable Wrapper Types

Providing dedicated wrapper types for collections is a commonly used pattern to provide an API for a query result that returns multiple elements.
Usually, these types are used by invoking a repository method returning a collection-like type and creating an instance of the wrapper type manually.
You can avoid that additional step as Spring Data lets you use these wrapper types as query method return types if they meet the following criteria:

1. The type implements `Streamable`.
2. The type exposes either a constructor or a static factory method named `of(…)` or `valueOf(…)` that takes `Streamable` as an argument.

The following listing shows an example:

```java
class Product {                                         (1) MonetaryAmount getPrice() { … }}
@RequiredArgsConstructor(staticName = "of") class Products implements Streamable<Product> {         (2)
private final Streamable<Product> streamable;
public MonetaryAmount getTotal() {                    (3) return streamable.stream() .map(Product::getPrice) .reduce(Money.of(0), MonetaryAmount::add);}
@Override public Iterator<Product> iterator() {                 (4) return streamable.iterator();}}
interface ProductRepository extends Repository<Product, Long> {Products findAllByDescriptionContaining(String text); (5)}
```

| **1** | A `Product` entity that exposes API to access the product’s price. |
| --- | --- |
| **2** | A wrapper type for a `Streamable<Product>` that can be constructed by using `Products.of(…)` (factory method created with the Lombok annotation). A standard constructor taking the `Streamable<Product>` will do as well. |
| **3** | The wrapper type exposes an additional API, calculating new values on the `Streamable<Product>`. |
| **4** | Implement the `Streamable` interface and delegate to the actual result. |
| **5** | That wrapper type `Products` can be used directly as a query method return type. You do not need to return `Streamable<Product>` and manually wrap it after the query in the repository client. |

<a id="repositories-query-methods-details--repositories.collections-and-iterables.vavr"></a>
<a id="repositories-query-methods-details--support-for-vavr-collections"></a>

### Support for Vavr Collections

[Vavr](https://www.vavr.io/) is a library that embraces functional programming concepts in Java.
It ships with a custom set of collection types that you can use as query method return types, as the following table shows:

| Vavr collection type | Used Vavr implementation type | Valid Java source types |
| --- | --- | --- |
| `io.vavr.collection.Seq` | `io.vavr.collection.List` | `java.util.Iterable` |
| `io.vavr.collection.Set` | `io.vavr.collection.LinkedHashSet` | `java.util.Iterable` |
| `io.vavr.collection.Map` | `io.vavr.collection.LinkedHashMap` | `java.util.Map` |

You can use the types in the first column (or subtypes thereof) as query method return types and get the types in the second column used as implementation type, depending on the Java type of the actual query result (third column).
Alternatively, you can declare `Traversable` (the Vavr `Iterable` equivalent), and we then derive the implementation class from the actual return value.
That is, a `java.util.List` is turned into a Vavr `List` or `Seq`, a `java.util.Set` becomes a Vavr `LinkedHashSet` `Set`, and so on.

<a id="repositories-query-methods-details--repositories.query-streaming"></a>
<a id="repositories-query-methods-details--streaming-query-results"></a>

## Streaming Query Results

You can process the results of query methods incrementally by using a `Stream<T>` as the return type.
Instead of wrapping the query results in a `Stream`, data store-specific methods are used to perform the streaming, as shown in the following example:

Stream the result of a query with Java 8 `Stream<T>`

```java
@Query("select u from User u")
Stream<User> findAllByCustomQueryAndStream();

Stream<User> readAllByFirstnameNotNull();

@Query("select u from User u")
Stream<User> streamAllPaged(Pageable pageable);
```

> [!NOTE]
> A `Stream` potentially wraps underlying data store-specific resources and must, therefore, be closed after usage.
> You can either manually close the `Stream` by using the `close()` method or by using a `try`-with-resources block, as shown in the following example:

Working with a `Stream<T>` result in a `try-with-resources` block

```java
try (Stream<User> stream = repository.findAllByCustomQueryAndStream()) {
  stream.forEach(…);
}
```

> [!NOTE]
> Not all Spring Data modules currently support `Stream<T>` as a return type.

<a id="repositories-query-methods-details--repositories.query-async"></a>
<a id="repositories-query-methods-details--asynchronous-query-results"></a>

## Asynchronous Query Results

You can run repository queries asynchronously by using [Spring’s asynchronous method running capability](https://docs.spring.io/spring-framework/reference/7.0/integration/scheduling.html).
This means the method returns immediately upon invocation while the actual query occurs in a task that has been submitted to a Spring `TaskExecutor`.
Asynchronous queries differ from reactive queries and should not be mixed.
See the store-specific documentation for more details on reactive support.
The following example shows a number of asynchronous queries:

```java
@Async
Future<User> findByFirstname(String firstname);               (1)

@Async
CompletableFuture<User> findOneByFirstname(String firstname); (2)
```

**1**

Use `java.util.concurrent.Future` as the return type.

**2**

Use `java.util.concurrent.CompletableFuture` as the return type.

<a id="repositories-query-methods-details--repositories.special-parameters"></a>
<a id="repositories-query-methods-details--paging-iterating-large-results-sorting-limiting"></a>

## Paging, Iterating Large Results, Sorting & Limiting

To handle parameters in your query, define method parameters as already seen in the preceding examples.
Besides that, the infrastructure recognizes certain specific types like `Pageable`, `Sort` and `Limit`, to apply pagination, sorting and limiting to your queries dynamically.
The following example demonstrates these features:

Using `Pageable`, `Slice`, `Sort` and `Limit` in query methods

```java
Page<User> findByLastname(String lastname, Pageable pageable);

Slice<User> findByLastname(String lastname, Pageable pageable);

List<User> findByLastname(String lastname, Sort sort);

List<User> findByLastname(String lastname, Sort sort, Limit limit);

List<User> findByLastname(String lastname, Pageable pageable);
```

> [!IMPORTANT]
> APIs taking `Sort`, `Pageable` and `Limit` expect non-`null` values to be handed into methods.
> If you do not want to apply any sorting or pagination, use `Sort.unsorted()`, `Pageable.unpaged()` and `Limit.unlimited()`.

The first method lets you pass an `org.springframework.data.domain.Pageable` instance to the query method to dynamically add paging to your statically defined query.
A `Page` knows about the total number of elements and pages available.
It does so by the infrastructure triggering a count query to calculate the overall number.
As this might be expensive (depending on the store used), you can instead return a `Slice`.
A `Slice` knows only about whether a next `Slice` is available, which might be sufficient when walking through a larger result set.

Sorting options are handled through the `Pageable` instance, too.
If you need only sorting, add an `org.springframework.data.domain.Sort` parameter to your method.
As you can see, returning a `List` is also possible.
In this case, the additional metadata required to build the actual `Page` instance is not created (which, in turn, means that the additional count query that would have been necessary is not issued).
Rather, it restricts the query to look up only the given range of entities.

> [!NOTE]
> To find out how many pages you get for an entire query, you have to trigger an additional count query.
> By default, this query is derived from the query you actually trigger.

> [!IMPORTANT]
> Special parameters may only be used once within a query method.
> Some special parameters described above are mutually exclusive.
> Please consider the following list of invalid parameter combinations.
>
> | Parameters | Example | Reason |
> | --- | --- | --- |
> | `Pageable` and `Sort` | `findBy…(Pageable page, Sort sort)` | `Pageable` already defines `Sort` |
> | `Pageable` and `Limit` | `findBy…(Pageable page, Limit limit)` | `Pageable` already defines a limit. |
>
> The `Top` keyword can be used together with `Pageable`: `Top` defines the total maximum number of results, while the `Pageable` parameter may reduce this number further.

<a id="repositories-query-methods-details--repositories.scrolling.guidance"></a>
<a id="repositories-query-methods-details--which-method-is-appropriate"></a>

### Which Method is Appropriate?

The value provided by the Spring Data abstractions is perhaps best shown by the possible query method return types outlined in the following table below.
The table shows which types you can return from a query method

<table class="tableblock frame-all grid-all stretch">
<caption>Table 1. Consuming Large Query Results</caption>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Method</th>
<th>Amount of Data Fetched</th>
<th>Query Structure</th>
<th>Constraints</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="#repositories-query-methods-details--repositories.collections-and-iterables"><code>List&lt;T&gt;</code></a></p></td>
<td><p>All results.</p></td>
<td><p>Single query.</p></td>
<td><p>Query results can exhaust all memory. Fetching all data can be time-intensive.</p></td>
</tr>
<tr>
<td><p><a href="#repositories-query-methods-details--repositories.collections-and-iterables.streamable"><code>Streamable&lt;T&gt;</code></a></p></td>
<td><p>All results.</p></td>
<td><p>Single query.</p></td>
<td><p>Query results can exhaust all memory. Fetching all data can be time-intensive.</p></td>
</tr>
<tr>
<td><p><a href="#repositories-query-methods-details--repositories.query-streaming"><code>Stream&lt;T&gt;</code></a></p></td>
<td><p>Chunked (one-by-one or in batches) depending on <code>Stream</code> consumption.</p></td>
<td><p>Single query using typically cursors.</p></td>
<td><p>Streams must be closed after usage to avoid resource leaks.</p></td>
</tr>
<tr>
<td><p><code>Flux&lt;T&gt;</code></p></td>
<td><p>Chunked (one-by-one or in batches) depending on <code>Flux</code> consumption.</p></td>
<td><p>Single query using typically cursors.</p></td>
<td><p>Store module must provide reactive infrastructure.</p></td>
</tr>
<tr>
<td><p><code>Slice&lt;T&gt;</code></p></td>
<td><p><code>Pageable.getPageSize() + 1</code> at <code>Pageable.getOffset()</code></p></td>
<td><p>One to many queries fetching data starting at <code>Pageable.getOffset()</code> applying limiting.</p></td>
<td><div><div>
<p>A <code>Slice</code> can only navigate to the next <code>Slice</code>.</p>
</div>
<div>
<ul>
<li>
<p><code>Slice</code> provides details whether there is more data to fetch.</p>
</li>
<li>
<p>Offset-based queries becomes inefficient when the offset is too large because the database still has to materialize the full result.</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td><p><code>Page&lt;T&gt;</code></p></td>
<td><p><code>Pageable.getPageSize()</code>  at <code>Pageable.getOffset()</code></p></td>
<td><p>One to many queries starting at <code>Pageable.getOffset()</code> applying limiting. Additionally, <code>COUNT(…)</code> query to determine the total number of elements can be required.</p></td>
<td><div><div>
<p>Often times, <code>COUNT(…)</code> queries are required that are costly.</p>
</div>
<div>
<ul>
<li>
<p>Offset-based queries becomes inefficient when the offset is too large because the database still has to materialize the full result.</p>
</li>
</ul>
</div></div></td>
</tr>
</tbody>
</table>

<a id="repositories-query-methods-details--repositories.paging-and-sorting"></a>
<a id="repositories-query-methods-details--paging-and-sorting"></a>

### Paging and Sorting

You can define simple sorting expressions by using property names.
You can concatenate expressions to collect multiple criteria into one expression.

Defining sort expressions

```java
Sort sort = Sort.by("firstname").ascending()
  .and(Sort.by("lastname").descending());
```

For a more type-safe way to define sort expressions, start with the type for which to define the sort expression and use method references to define the properties on which to sort.

Defining sort expressions by using the type-safe API

```java
TypedSort<Person> person = Sort.sort(Person.class);

Sort sort = person.by(Person::getFirstname).ascending()
  .and(person.by(Person::getLastname).descending());
```

> [!NOTE]
> `TypedSort.by(…)` makes use of runtime proxies by (typically) using CGlib, which may interfere with native image compilation when using tools such as GraalVM Native Image.

If your store implementation supports Querydsl, you can also use the generated metamodel types to define sort expressions:

Defining sort expressions by using the Querydsl API

```java
QSort sort = QSort.by(QPerson.firstname.asc())
  .and(QSort.by(QPerson.lastname.desc()));
```

<a id="repositories-query-methods-details--repositories.limit-query-result"></a>
<a id="repositories-query-methods-details--limiting-query-results"></a>

### Limiting Query Results

In addition to paging it is possible to limit the result size using a dedicated `Limit` parameter.
You can also limit the results of query methods by using the `First` or `Top` keywords, which you can use interchangeably but may not be mixed with a `Limit` parameter.
You can append an optional numeric value to `Top` or `First` to specify the maximum result size to be returned.
If the number is left out, a result size of 1 is assumed.
The following example shows how to limit the query size:

Limiting the result size of a query with `Top` and `First`

```java
List<User> findByLastname(String lastname, Limit limit);

User findFirstByOrderByLastnameAsc();

User findTopByLastnameOrderByAgeDesc(String lastname);

Page<User> queryFirst10ByLastname(String lastname, Pageable pageable);

Slice<User> findTop3By(Pageable pageable);

List<User> findFirst10ByLastname(String lastname, Sort sort);

List<User> findTop10ByLastname(String lastname, Pageable pageable);
```

The limiting expressions also support the `Distinct` keyword for datastores that support distinct queries.
Also, for the queries that limit the result set to one instance, wrapping the result into with the `Optional` keyword is supported.

If pagination or slicing is applied to a limiting query pagination (and the calculation of the number of available pages), it is applied within the limited result.

> [!NOTE]
> Limiting the results in combination with dynamic sorting by using a `Sort` parameter lets you express query methods for the 'K' smallest as well as for the 'K' biggest elements.

---

<a id="repositories-vector-search"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/vector-search.html -->

<!-- page_index: 10 -->

# Vector Search

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-vector-search--page-title"></a>
<a id="repositories-vector-search--vector-search"></a>

# Vector Search

With the rise of Generative AI, Vector databases have gained strong traction in the world of databases.
These databases enable efficient storage and querying of high-dimensional vectors, making them well-suited for tasks such as semantic search, recommendation systems, and natural language understanding.

Vector search is a technique that retrieves semantically similar data by comparing vector representations (also known as embeddings) rather than relying on traditional exact-match queries.
This approach enables intelligent, context-aware applications that go beyond keyword-based retrieval.

In the context of Spring Data, vector search opens new possibilities for building intelligent, context-aware applications, particularly in domains like natural language processing, recommendation systems, and generative AI.
By modelling vector-based querying using familiar repository abstractions, Spring Data allows developers to seamlessly integrate similarity-based vector-capable databases with the simplicity and consistency of the Spring Data programming model.

<a id="repositories-vector-search--vector-search.model"></a>
<a id="repositories-vector-search--vector-model"></a>

## Vector Model

To support vector search in a type-safe and idiomatic way, Spring Data introduces the following core abstractions:

- [`Vector`](#repositories-vector-search--vector-search.model.vector)
- [`SearchResults<T>` and `SearchResult<T>`](#repositories-vector-search--vector-search.model.search-result)
- [`Score`, `Similarity` and Scoring Functions](#repositories-vector-search--vector-search.model.scoring)

<a id="repositories-vector-search--vector-search.model.vector"></a>
<a id="repositories-vector-search--vector"></a>

### `Vector`

The `Vector` type represents an n-dimensional numerical embedding, typically produced by embedding models.
In Spring Data, it is defined as a lightweight wrapper around an array of floating-point numbers, ensuring immutability and consistency.
This type can be used as an input for search queries or as a property on a domain entity to store the associated vector representation.

```java
Vector vector = Vector.of(0.23f, 0.11f, 0.77f);
```

Using `Vector` in your domain model removes the need to work with raw arrays or lists of numbers, providing a more type-safe and expressive way to handle vector data.
This abstraction also allows for easy integration with various vector databases and libraries.
It also allows for implementing vendor-specific optimizations such as binary or quantized vectors that do not map to a standard floating point (`float` and `double` as of [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)) representation.
A domain object can have a vector property, which can be used for similarity searches.
Consider the following example:

> [!NOTE]
> Associating a vector with a domain object results in the vector being loaded and stored as part of the entity lifecycle, which may introduce additional overhead on retrieval and persistence operations.

<a id="repositories-vector-search--vector-search.model.search-result"></a>
<a id="repositories-vector-search--search-results"></a>

### Search Results

The `SearchResult<T>` type encapsulates the results of a vector similarity query.
It includes both the matched domain object and a relevance score that indicates how closely it matches the query vector.
This abstraction provides a structured way to handle result ranking and enables developers to easily work with both the data and its contextual relevance.

In this example, the `searchByCountryAndEmbeddingNear` method returns a `SearchResults<Comment>` object, which contains a list of `SearchResult<Comment>` instances.
Each result includes the matched `Comment` entity and its relevance score.

Relevance score is a numerical value that indicates how closely the matched vector aligns with the query vector.
Depending on whether a score represents distance or similarity a higher score can mean a closer match or a more distant one.

The scoring function used to calculate this score can vary based on the underlying database, index or input parameters.

<a id="repositories-vector-search--vector-search.model.scoring"></a>
<a id="repositories-vector-search--score-similarity-and-scoring-functions"></a>

### Score, Similarity, and Scoring Functions

The `Score` type holds a numerical value indicating the relevance of a search result.
It can be used to rank results based on their similarity to the query vector.
The `Score` type is typically a floating-point number, and its interpretation (higher is better or lower is better) depends on the specific similarity function used.
Scores are a by-product of vector search and are not required for a successful search operation.
Score values are not part of a domain model and therefore represented best as out-of-band data.

Generally, a Score is computed by a `ScoringFunction`.
The actual scoring function used to calculate this score can depend on the underlying database and can be obtained from a search index or input parameters.

Spring Data support declares constants for commonly used functions such as:

Euclidean Distance
:   Calculates the straight-line distance in n-dimensional space involving the square root of the sum of squared differences.

Cosine Similarity
:   Measures the angle between two vectors by calculating the Dot product first and then normalizing its result by dividing by the product of their lengths.

Dot Product
:   Computes the sum of element-wise multiplications.

The choice of similarity function can impact both the performance and semantics of the search and is often determined by the underlying database or index being used.
Spring Data adapts to the database’s native scoring function capabilities and whether the score can be used to limit results.

<a id="repositories-vector-search--vector-search.methods"></a>
<a id="repositories-vector-search--vector-search-methods"></a>

## Vector Search Methods

Vector search methods are defined in repositories using the same conventions as standard Spring Data query methods.
These methods return `SearchResults<T>` and require a `Vector` parameter to define the query vector.
The actual implementation depends on the actual internals of the underlying data store and its capabilities around vector search.

> [!NOTE]
> If you are new to Spring Data repositories, make sure to familiarize yourself with the [basics of repository definitions and query methods](#repositories-core-concepts).

Generally, you have the choice of declaring a search method using two approaches:

- Query Derivation
- Declaring a String-based Query

Vector Search methods must declare a `Vector` parameter to define the query vector.

<a id="repositories-vector-search--vector-search.method.derivation"></a>
<a id="repositories-vector-search--derived-search-methods"></a>

### Derived Search Methods

A derived search method uses the name of the method to derive the query.
Vector Search supports the following keywords to run a Vector search when declaring a search method:

| Logical keyword | Keyword expressions |
| --- | --- |
| `NEAR` | `Near`, `IsNear` |
| `WITHIN` | `Within`, `IsWithin` |

Derived search methods are typically easier to read and maintain, as they rely on the method name to express the query intent.
However, a derived search method requires either to declare a `Score`, `Range<Score>` or `ScoreFunction` as second argument to the `Near`/`Within` keyword to limit search results by their score.

<a id="repositories-vector-search--vector-search.method.string"></a>
<a id="repositories-vector-search--annotated-search-methods"></a>

### Annotated Search Methods

Annotated methods provide full control over the query semantics and parameters.
Unlike derived methods, they do not rely on method name conventions.

With more control over the actual query, Spring Data can make fewer assumptions about the query and its parameters.
For example, `Similarity` normalization uses the native score function within the query to normalize the given similarity into a score predicate value and vice versa.
If an annotated query does not define e.g. the score, then the score value in the returned `SearchResult<T>` will be zero.

<a id="repositories-vector-search--vector-search.method.sorting"></a>
<a id="repositories-vector-search--sorting"></a>

### Sorting

By default, search results are ordered according to their score.
You can override sorting by using the `Sort` parameter:

Example 1. Using `Sort` in Repository Search Methods

```java
interface CommentRepository extends Repository<Comment, String> {

  SearchResults<Comment> searchByEmbeddingNearOrderByCountry(Vector vector, Score score);

  SearchResults<Comment> searchByEmbeddingWithin(Vector vector, Score score, Sort sort);
}
```

Please note that custom sorting does not allow expressing the score as a sorting criteria.
You can only refer to domain properties.

---

<a id="repositories-create-instances"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/create-instances.html -->

<!-- page_index: 11 -->

# Creating Repository Instances

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-create-instances--page-title"></a>
<a id="repositories-create-instances--creating-repository-instances"></a>

# Creating Repository Instances

This section covers how to create instances and bean definitions for the defined repository interfaces.

<a id="repositories-create-instances--repositories.create-instances.java-config"></a>
<a id="repositories-create-instances--java-configuration"></a>

## Java Configuration

Use the store-specific `@EnableJpaRepositories` annotation on a Java configuration class to define a configuration for repository activation.
For an introduction to Java-based configuration of the Spring container, see [JavaConfig in the Spring reference documentation](https://docs.spring.io/spring-framework/reference/7.0/core/beans/java.html).

A sample configuration to enable Spring Data repositories resembles the following:

Sample annotation-based repository configuration

```java
@Configuration @EnableJpaRepositories("com.acme.repositories") class ApplicationConfiguration {
@Bean EntityManagerFactory entityManagerFactory() {// …}}
```

> [!NOTE]
> The preceding example uses the JPA-specific annotation, which you would change according to the store module you actually use. The same applies to the definition of the `EntityManagerFactory` bean. See the sections covering the store-specific configuration.

<a id="repositories-create-instances--repositories.create-instances.java-config.placeholders-and-patterns"></a>
<a id="repositories-create-instances--property-placeholders-and-ant-style-patterns"></a>

### Property Placeholders and Ant-style Patterns

The `basePackages` and `value` attributes in `@EnableJpaRepositories` support `${…}` property placeholders which are resolved against the `Environment` as well as Ant-style package patterns such as `"org.example.**"`.

The following example specifies the `app.scan.packages` property placeholder for the implicit `value` attribute in `@EnableJpaRepositories`.

- Java
- Kotlin

```java
@Configuration
@EnableJpaRepositories("${app.scan.packages}")    (1)
public class ApplicationConfiguration {
  // …
}
```

**1**

`app.scan.packages` property placeholder to be resolved against the `Environment`

```kotlin
@EnableJpaRepositories(["\${app.scan.packages}"]) (1)
class ApplicationConfiguration {
  // …
}
```

**1**

`app.scan.packages` property placeholder to be resolved against the `Environment`

<a id="repositories-create-instances--repositories.create-instances.xml"></a>
<a id="repositories-create-instances--xml-configuration"></a>

## XML Configuration

Each Spring Data module includes a `repositories` element that lets you define a base package that Spring scans for you, as shown in the following example:

Enabling Spring Data repositories via XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans xmlns:beans="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://www.springframework.org/schema/data/jpa"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    https://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/data/jpa
    https://www.springframework.org/schema/data/jpa/spring-jpa.xsd">

  <jpa:repositories base-package="com.acme.repositories" />

</beans:beans>
```

In the preceding example, Spring is instructed to scan `com.acme.repositories` and all its sub-packages for interfaces extending `Repository` or one of its sub-interfaces.
For each interface found, the infrastructure registers the persistence technology-specific `FactoryBean` to create the appropriate proxies that handle invocations of the query methods.
Each bean is registered under a bean name that is derived from the interface name, so an interface of `UserRepository` would be registered under `userRepository`.
Bean names for nested repository interfaces are prefixed with their enclosing type name.
The base package attribute allows wildcards so that you can define a pattern of scanned packages.

<a id="repositories-create-instances--repositories.using-filters"></a>
<a id="repositories-create-instances--using-filters"></a>

## Using Filters

By default, the infrastructure picks up every interface that extends the persistence technology-specific `Repository` sub-interface located under the configured base package and creates a bean instance for it.
However, you might want more fine-grained control over which interfaces have bean instances created for them.
To do so, use filter elements inside the repository declaration.
The semantics are exactly equivalent to the elements in Spring’s component filters.
For details, see the [Spring reference documentation](https://docs.spring.io/spring-framework/reference/7.0/core/beans/classpath-scanning.html) for these elements.

For example, to exclude certain interfaces from instantiation as repository beans, you could use the following configuration:

Using filters

- Java
- XML

```java
@Configuration
@EnableJpaRepositories(basePackages = "com.acme.repositories",
    includeFilters = { @Filter(type = FilterType.REGEX, pattern = ".*SomeRepository") },
    excludeFilters = { @Filter(type = FilterType.REGEX, pattern = ".*SomeOtherRepository") })
class ApplicationConfiguration {

  @Bean
  EntityManagerFactory entityManagerFactory() {
    // …
  }
}
```

```xml
<repositories base-package="com.acme.repositories">
  <context:include-filter type="regex" expression=".*SomeRepository" />
  <context:exclude-filter type="regex" expression=".*SomeOtherRepository" />
</repositories>
```

The preceding example includes all interfaces ending with `SomeRepository` and excludes those ending with `SomeOtherRepository` from being instantiated.

<a id="repositories-create-instances--repositories.create-instances.standalone"></a>
<a id="repositories-create-instances--standalone-usage"></a>

## Standalone Usage

You can also use the repository infrastructure outside of a Spring container — for example, in CDI environments.You still need some Spring libraries in your classpath, but, generally, you can set up repositories programmatically as well.The Spring Data modules that provide repository support ship with a persistence technology-specific `RepositoryFactory` that you can use, as follows:

Standalone usage of the repository factory

```java
RepositoryFactorySupport factory = … // Instantiate factory here
UserRepository repository = factory.getRepository(UserRepository.class);
```

---

<a id="repositories-custom-implementations"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/custom-implementations.html -->

<!-- page_index: 12 -->

# Custom Repository Implementations

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-custom-implementations--page-title"></a>
<a id="repositories-custom-implementations--custom-repository-implementations"></a>

# Custom Repository Implementations

Spring Data provides various options to create query methods with little coding.
But when those options don’t fit your needs you can also provide your own custom implementation for repository methods.
This section describes how to do that.

<a id="repositories-custom-implementations--repositories.single-repository-behavior"></a>
<a id="repositories-custom-implementations--customizing-individual-repositories"></a>

## Customizing Individual Repositories

To enrich a repository with custom functionality, you must first define a fragment interface and an implementation for the custom functionality, as follows:

Interface for custom repository functionality

```java
interface CustomizedUserRepository {
  void someCustomMethod(User user);
}
```

Implementation of custom repository functionality

```java
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

  @Override
  public void someCustomMethod(User user) {
    // Your custom implementation
  }
}
```

> [!NOTE]
> The most important part of the class name that corresponds to the fragment interface is the `Impl` postfix.
> You can customize the store-specific postfix by setting `@Enable<StoreModule>Repositories(repositoryImplementationPostfix = …)`.

> [!WARNING]
> Historically, Spring Data custom repository implementation discovery followed a
> [naming pattern](https://docs.spring.io/spring-data/commons/docs/1.9.0.RELEASE/reference/html/#repositories.single-repository-behaviour)
> that derived the custom implementation class name from the repository allowing effectively a single custom implementation.
>
> A type located in the same package as the repository interface, matching *repository interface name* followed by *implementation postfix*, is considered a custom implementation and will be treated as a custom implementation.
> A class following that name can lead to undesired behavior.
>
> We consider the single-custom implementation naming deprecated and recommend not using this pattern.
> Instead, migrate to a fragment-based programming model.

The implementation itself does not depend on Spring Data and can be a regular Spring bean.
Consequently, you can use standard dependency injection behavior to inject references to other beans (such as a `JdbcTemplate`), take part in aspects, and so on.

Then you can let your repository interface extend the fragment interface, as follows:

Changes to your repository interface

```java
interface UserRepository extends CrudRepository<User, Long>, CustomizedUserRepository {

  // Declare query methods here
}
```

Extending the fragment interface with your repository interface combines the CRUD and custom functionality and makes it available to clients.

Spring Data repositories are implemented by using fragments that form a repository composition.
Fragments are the base repository, functional aspects (such as [Querydsl](#repositories-core-extensions--core.extensions.querydsl)), and custom interfaces along with their implementations.
Each time you add an interface to your repository interface, you enhance the composition by adding a fragment.
The base repository and repository aspect implementations are provided by each Spring Data module.

The following example shows custom interfaces and their implementations:

Fragments with their implementations

```java
interface HumanRepository {void someHumanMethod(User user);}
class HumanRepositoryImpl implements HumanRepository {
@Override public void someHumanMethod(User user) {// Your custom implementation}}
interface ContactRepository {
void someContactMethod(User user);
User anotherContactMethod(User user);}
class ContactRepositoryImpl implements ContactRepository {
@Override public void someContactMethod(User user) {// Your custom implementation}
@Override public User anotherContactMethod(User user) {// Your custom implementation}}
```

The following example shows the interface for a custom repository that extends `CrudRepository`:

Changes to your repository interface

```java
interface UserRepository extends CrudRepository<User, Long>, HumanRepository, ContactRepository {

  // Declare query methods here
}
```

Repositories may be composed of multiple custom implementations that are imported in the order of their declaration.
Custom implementations have a higher priority than the base implementation and repository aspects.
This ordering lets you override base repository and aspect methods and resolves ambiguity if two fragments contribute the same method signature.
Repository fragments are not limited to use in a single repository interface.
Multiple repositories may use a fragment interface, letting you reuse customizations across different repositories.

The following example shows a repository fragment and its implementation:

Fragments overriding `save(…)`

```java
interface CustomizedSave<T> {<S extends T> S save(S entity);}
class CustomizedSaveImpl<T> implements CustomizedSave<T> {
@Override public <S extends T> S save(S entity) {// Your custom implementation}}
```

The following example shows a repository that uses the preceding repository fragment:

Customized repository interfaces

```java
interface UserRepository extends CrudRepository<User, Long>, CustomizedSave<User> {
}

interface PersonRepository extends CrudRepository<Person, Long>, CustomizedSave<Person> {
}
```

<a id="repositories-custom-implementations--repositories.configuration"></a>
<a id="repositories-custom-implementations--configuration"></a>

### Configuration

The repository infrastructure tries to autodetect custom implementation fragments by scanning for classes below the package in which it found a repository.
These classes need to follow the naming convention of appending a postfix defaulting to `Impl`.

The following example shows a repository that uses the default postfix and a repository that sets a custom value for the postfix:

Example 1. Configuration example

- Java
- XML

```java
@EnableJpaRepositories(repositoryImplementationPostfix = "MyPostfix")
class Configuration { … }
```

```xml
<repositories base-package="com.acme.repository" />

<repositories base-package="com.acme.repository" repository-impl-postfix="MyPostfix" />
```

The first configuration in the preceding example tries to look up a class called `com.acme.repository.CustomizedUserRepositoryImpl` to act as a custom repository implementation.
The second example tries to look up `com.acme.repository.CustomizedUserRepositoryMyPostfix`.

<a id="repositories-custom-implementations--repositories.single-repository-behaviour.ambiguity"></a>
<a id="repositories-custom-implementations--resolution-of-ambiguity"></a>

#### Resolution of Ambiguity

If multiple implementations with matching class names are found in different packages, Spring Data uses the bean names to identify which one to use.

Given the following two custom implementations for the `CustomizedUserRepository` shown earlier, the first implementation is used.
Its bean name is `customizedUserRepositoryImpl`, which matches that of the fragment interface (`CustomizedUserRepository`) plus the postfix `Impl`.

Example 2. Resolution of ambiguous implementations

```java
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

  // Your custom implementation
}
```

```java
@Component("specialCustomImpl")
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

  // Your custom implementation
}
```

If you annotate the `UserRepository` interface with `@Component("specialCustom")`, the bean name plus `Impl` then matches the one defined for the repository implementation in `com.acme.impl.two`, and it is used instead of the first one.

<a id="repositories-custom-implementations--repositories.manual-wiring"></a>
<a id="repositories-custom-implementations--manual-wiring"></a>

#### Manual Wiring

If your custom implementation uses annotation-based configuration and autowiring only, the preceding approach shown works well, because it is treated as any other Spring bean.
If your implementation fragment bean needs special wiring, you can declare the bean and name it according to the conventions described in the [preceding section](#repositories-custom-implementations--repositories.single-repository-behaviour.ambiguity).
The infrastructure then refers to the manually defined bean definition by name instead of creating one itself.
The following example shows how to manually wire a custom implementation:

Example 3. Manual wiring of custom implementations

- Java
- XML

```java
class MyClass {
  MyClass(@Qualifier("userRepositoryImpl") UserRepository userRepository) {
    …
  }
}
```

```xml
<repositories base-package="com.acme.repository" />

<beans:bean id="userRepositoryImpl" class="…">
  <!-- further configuration -->
</beans:bean>
```

<a id="repositories-custom-implementations--repositories.spring-factories"></a>
<a id="repositories-custom-implementations--registering-fragments-with-spring.factories"></a>

#### Registering Fragments with spring.factories

As already mentioned in the [Configuration](#repositories-custom-implementations--repositories.configuration) section, the infrastructure only auto-detects fragments within the repository base-package.
Therefore, fragments residing in another location or want to be contributed by an external archive will not be found if they do not share a common namespace.
Registering fragments within `spring.factories` allows you to circumvent this restriction as explained in the following section.

Imagine you’d like to provide some custom search functionality usable across multiple repositories for your organization leveraging a text search index.

First all you need is the fragment interface.
Note the generic `<T>` parameter to align the fragment with the repository domain type.

Fragment Interface

```java
public interface SearchExtension<T> {

    List<T> search(String text, Limit limit);
}
```

Let’s assume the actual full-text search is available via a `SearchService` that is registered as a `Bean` within the context so you can consume it in our `SearchExtension` implementation.
All you need to run the search is the collection (or index) name and an object mapper that converts the search results into actual domain objects as sketched out below.

Fragment implementation

```java
import org.springframework.beans.factory.annotation.Autowired; import org.springframework.data.domain.Limit; import org.springframework.data.repository.core.RepositoryMethodContext;
class DefaultSearchExtension<T> implements SearchExtension<T> {
private final SearchService service;
DefaultSearchExtension(SearchService service) {this.service = service;}
@Override public List<T> search(String text, Limit limit) {return search(RepositoryMethodContext.getContext(), text, limit);}
List<T> search(RepositoryMethodContext metadata, String text, Limit limit) {
Class<T> domainType = metadata.getRepository().getDomainType();
String indexName = domainType.getSimpleName().toLowerCase(); List<String> jsonResult = service.search(indexName, text, 0, limit.max());
return jsonResult.stream().map(…).collect(toList());}}
```

In the example above `RepositoryMethodContext.getContext()` is used to retrieve metadata for the actual method invocation.
`RepositoryMethodContext` exposes information attached to the repository such as the domain type.
In this case we use the repository domain type to identify the name of the index to be searched.

Exposing invocation metadata is costly, hence it is disabled by default.
To access `RepositoryMethodContext.getContext()` you need to advise the repository factory responsible for creating the actual repository to expose method metadata.

Expose Repository Metadata

- Marker Interface
- Bean Post Processor

Adding the `RepositoryMetadataAccess` marker interface to the fragments implementation will trigger the infrastructure and enable metadata exposure for those repositories using the fragment.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Limit;
import org.springframework.data.repository.core.support.RepositoryMetadataAccess;
import org.springframework.data.repository.core.RepositoryMethodContext;

class DefaultSearchExtension<T> implements SearchExtension<T>, RepositoryMetadataAccess {

    // ...
}
```

The `exposeMetadata` flag can be set directly on the repository factory bean via a `BeanPostProcessor`.

```java
import org.springframework.beans.factory.config.BeanPostProcessor; import org.springframework.context.annotation.Configuration; import org.springframework.data.repository.core.support.RepositoryFactoryBeanSupport;
@Configuration class MyConfiguration {
@Bean static BeanPostProcessor exposeMethodMetadata() {
return new BeanPostProcessor() {
@Override public Object postProcessBeforeInitialization(Object bean, String beanName) {
if(bean instanceof RepositoryFactoryBeanSupport<?,?,?> factoryBean) {factoryBean.setExposeMetadata(true);} return bean;} };}}
```

Please do not just copy/paste the above but consider your actual use case which may require a more fine-grained approach as the above will simply enable the flag on every repository.

Having both, the fragment declaration and implementation in place you can register the extension in the `META-INF/spring.factories` file and package things up if needed.

Register the fragment in `META-INF/spring.factories`

```properties
com.acme.search.SearchExtension=com.acme.search.DefaultSearchExtension
```

Now you are ready to make use of your extension; Simply add the interface to your repository.

Using it

```java
import com.acme.search.SearchExtension;
import org.springframework.data.repository.CrudRepository;

interface MovieRepository extends CrudRepository<Movie, String>, SearchExtension<Movie> {

}
```

<a id="repositories-custom-implementations--repositories.customize-base-repository"></a>
<a id="repositories-custom-implementations--customize-the-base-repository"></a>

## Customize the Base Repository

The approach described in the [preceding section](#repositories-custom-implementations--repositories.manual-wiring) requires customization of each repository interfaces when you want to customize the base repository behavior so that all repositories are affected.
To instead change behavior for all repositories, you can create an implementation that extends the persistence technology-specific repository base class.
This class then acts as a custom base class for the repository proxies, as shown in the following example:

Custom repository base class

```java
class MyRepositoryImpl<T, ID>
  extends SimpleJpaRepository<T, ID> {

  private final EntityManager entityManager;

  MyRepositoryImpl(JpaEntityInformation entityInformation,
                          EntityManager entityManager) {
    super(entityInformation, entityManager);

    // Keep the EntityManager around to used from the newly introduced methods.
    this.entityManager = entityManager;
  }

  @Override
  @Transactional
  public <S extends T> S save(S entity) {
    // implementation goes here
  }
}
```

> [!WARNING]
> The class needs to have a constructor of the super class which the store-specific repository factory implementation uses.
> If the repository base class has multiple constructors, override the one taking an `EntityInformation` plus a store specific infrastructure object (such as an `EntityManager` or a template class).

The final step is to make the Spring Data infrastructure aware of the customized repository base class.
In configuration, you can do so by using the `repositoryBaseClass`, as shown in the following example:

Example 4. Configuring a custom repository base class

- Java
- XML

```java
@Configuration
@EnableJpaRepositories(repositoryBaseClass = MyRepositoryImpl.class)
class ApplicationConfiguration { … }
```

```xml
<repositories base-package="com.acme.repository"
     base-class="….MyRepositoryImpl" />
```

<a id="repositories-custom-implementations--repositories.customize-repository-factory"></a>
<a id="repositories-custom-implementations--customizing-the-repository-factory"></a>

## Customizing the Repository Factory

Customizing the [repository factory](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/core/support/RepositoryFactorySupport.html) through [`RepositoryFactoryCustomizer`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/core/support/RepositoryFactoryCustomizer.html) provides direct access to components involved with repository instance creation.
This mechanism is useful when you want to adjust selected aspects of proxy creation without introducing a fully custom repository factory bean.
The following example, demonstrates registering additional listeners and proxy advisors:

```java
factoryBean.addRepositoryFactoryCustomizer(repositoryFactory -> {
	repositoryFactory.addInvocationListener(…);
	repositoryFactory.addQueryCreationListener(…);

	repositoryFactory.addRepositoryProxyPostProcessor((factory, repositoryInformation) -> factory.addAdvice(…));
});
```

A `RepositoryFactoryCustomizer` is associated with a particular repository factory bean, ideally through `BeanPostProcessor` so that only specific repositories are affected.
Note that customizer beans are not applied automatically to prevent unwanted wiring that become especially relevant in multi-repository arrangements or when using multiple Spring Data modules.

<a id="repositories-custom-implementations--repositories.customize-repository-factory-bean"></a>
<a id="repositories-custom-implementations--customize-the-repository-factory-bean"></a>

## Customize the Repository Factory Bean

The most powerful approach to customize repository creation is to provide a custom repository factory bean, typically a subclass of [`RepositoryFactorySupport`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/core/support/RepositoryFactorySupport.html), [`TransactionalRepositoryFactoryBeanSupport`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/core/support/TransactionalRepositoryFactoryBeanSupport.html) or the store-specific repository factory bean.

Customizing the repository factory bean allows you to change repository creation entirely with full access to the underlying repository factory.

Note that this approach requires the most effort and is typically only needed when you want to change core aspects of repository creation.
Also, you need to take into consideration repository metadata derivation that is used to identify query methods, base implementation methods and custom implementations.
The following summary outlines the key aspects:

- `repositoryBaseClass`: The repository base class defines which methods are implemented by the base class and which methods require additional handling through aspects or custom implementations.
- `repositoryFragmentsContributor`: A [`RepositoryFragmentsContributor`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/repository/core/support/RepositoryFragmentsContributor.html) allows contributions to repository composition after all standard fragments have been collected.
  Store modules use this mechanism to add features such as Querydsl or Query-by-Example support.
  It also serves as an SPI for third-party extensions.
- `exposeMetadata`: Controls whether [invocation metadata](#repositories-custom-implementations--expose-repository-metadata) is available through `RepositoryMethodContext.getContext()`.

---

<a id="repositories-core-domain-events"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/core-domain-events.html -->

<!-- page_index: 13 -->

# Publishing Events from Aggregate Roots

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-core-domain-events--page-title"></a>
<a id="repositories-core-domain-events--publishing-events-from-aggregate-roots"></a>

# Publishing Events from Aggregate Roots

Entities managed by repositories are aggregate roots.
In a Domain-Driven Design application, these aggregate roots usually publish domain events.
Spring Data provides an annotation called `@DomainEvents` that you can use on a method of your aggregate root to make that publication as easy as possible, as shown in the following example:

Exposing domain events from an aggregate root

```java
class AnAggregateRoot {
@DomainEvents (1) Collection<Object> domainEvents() {// … return events you want to get published here}
@AfterDomainEventPublication (2) void callbackMethod() {// … potentially clean up domain events list}}
```

**1**

The method that uses `@DomainEvents` can return either a single event instance or a collection of events.
It must not take any arguments.

**2**

After all events have been published, we have a method annotated with `@AfterDomainEventPublication`.
You can use it to potentially clean the list of events to be published (among other uses).

The methods are called every time one of the following a Spring Data repository methods are called:

- `save(…)`, `saveAll(…)`
- `delete(…)`, `deleteAll(…)`, `deleteAllInBatch(…)`, `deleteInBatch(…)`

Note, that these methods take the aggregate root instances as arguments.
This is why `deleteById(…)` is notably absent, as the implementations might choose to issue a query deleting the instance and thus we would never have access to the aggregate instance in the first place.

---

<a id="repositories-core-extensions"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/core-extensions.html -->

<!-- page_index: 14 -->

# Spring Data Extensions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-core-extensions--page-title"></a>
<a id="repositories-core-extensions--spring-data-extensions"></a>

# Spring Data Extensions

This section documents a set of Spring Data extensions that enable Spring Data usage in a variety of contexts.
Currently, most of the integration is targeted towards Spring MVC.

<a id="repositories-core-extensions--core.extensions.querydsl"></a>
<a id="repositories-core-extensions--querydsl-extension"></a>

## Querydsl Extension

[Querydsl](http://www.querydsl.com/) is a framework that enables the construction of statically typed SQL-like queries through its fluent API.

> [!NOTE]
> Querydsl maintenance has slowed down to a point where the community has forked the project under OpenFeign at [github.com/OpenFeign/querydsl](https://github.com/OpenFeign/querydsl) (groupId `io.github.openfeign.querydsl`).
> Spring Data supports the fork on a best-effort basis.

Several Spring Data modules offer integration with Querydsl through `QuerydslPredicateExecutor`, as the following example shows:

QuerydslPredicateExecutor interface

```java
public interface QuerydslPredicateExecutor<T> {

  Optional<T> findById(Predicate predicate);  (1)

  Iterable<T> findAll(Predicate predicate);   (2)

  long count(Predicate predicate);            (3)

  boolean exists(Predicate predicate);        (4)

  // … more functionality omitted.
}
```

| **1** | Finds and returns a single entity matching the `Predicate`. |
| --- | --- |
| **2** | Finds and returns all entities matching the `Predicate`. |
| **3** | Returns the number of entities matching the `Predicate`. |
| **4** | Returns whether an entity that matches the `Predicate` exists. |

To use the Querydsl support, extend `QuerydslPredicateExecutor` on your repository interface, as the following example shows:

Querydsl integration on repositories

```java
interface UserRepository extends CrudRepository<User, Long>, QuerydslPredicateExecutor<User> {
}
```

The preceding example lets you write type-safe queries by using Querydsl `Predicate` instances, as the following example shows:

```java
Predicate predicate = user.firstname.equalsIgnoreCase("dave")
	.and(user.lastname.startsWithIgnoreCase("mathews"));

userRepository.findAll(predicate);
```

<a id="repositories-core-extensions--core.web"></a>
<a id="repositories-core-extensions--web-support"></a>

## Web support

Spring Data modules that support the repository programming model ship with a variety of web support.
The web related components require Spring MVC JARs to be on the classpath.
Some of them even provide integration with [Spring HATEOAS](https://github.com/spring-projects/spring-hateoas).
In general, the integration support is enabled by using the `@EnableSpringDataWebSupport` annotation in your JavaConfig configuration class, as the following example shows:

Enabling Spring Data web support

- Java
- XML

```java
@Configuration
@EnableWebMvc
@EnableSpringDataWebSupport
class WebConfiguration {}
```

```xml
<bean class="org.springframework.data.web.config.SpringDataWebConfiguration" />

<!-- If you use Spring HATEOAS, register this one *instead* of the former -->
<bean class="org.springframework.data.web.config.HateoasAwareSpringDataWebConfiguration" />
```

The `@EnableSpringDataWebSupport` annotation registers a few components.
We discuss those later in this section.
It also detects Spring HATEOAS on the classpath and registers integration components (if present) for it as well.

<a id="repositories-core-extensions--core.web.basic"></a>
<a id="repositories-core-extensions--basic-web-support"></a>

### Basic Web Support

The configuration shown in the [previous section](#repositories-core-extensions--core.web) registers a few basic components:

- A [Using the `DomainClassConverter` Class](#repositories-core-extensions--core.web.basic.domain-class-converter) to let Spring MVC resolve instances of repository-managed domain classes from request parameters or path variables.
- [`HandlerMethodArgumentResolver`](#repositories-core-extensions--core.web.basic.paging-and-sorting) implementations to let Spring MVC resolve `Pageable` and `Sort` instances from request parameters.
- [Jackson Modules](#repositories-core-extensions--core.web.basic.jackson-mappers) to de-/serialize types like `Point` and `Distance`, or store specific ones, depending on the Spring Data Module used.

<a id="repositories-core-extensions--core.web.basic.domain-class-converter"></a>
<a id="repositories-core-extensions--using-the-domainclassconverter-class"></a>

#### Using the `DomainClassConverter` Class

The `DomainClassConverter` class lets you use domain types in your Spring MVC controller method signatures directly so that you need not manually lookup the instances through the repository, as the following example shows:

A Spring MVC controller using domain types in method signatures

```java
@Controller @RequestMapping("/users") class UserController {
@RequestMapping("/{id}") String showUserForm(@PathVariable("id") User user, Model model) {
model.addAttribute("user", user); return "userForm";}}
```

The method receives a `User` instance directly, and no further lookup is necessary.
The instance can be resolved by letting Spring MVC convert the path variable into the `id` type of the domain class first and eventually access the instance through calling `findById(…)` on the repository instance registered for the domain type.

> [!NOTE]
> Currently, the repository has to implement `CrudRepository` to be eligible to be discovered for conversion.

<a id="repositories-core-extensions--core.web.basic.paging-and-sorting"></a>
<a id="repositories-core-extensions--handlermethodargumentresolvers-for-pageable-and-sort"></a>

#### HandlerMethodArgumentResolvers for Pageable and Sort

The configuration snippet shown in the [previous section](#repositories-core-extensions--core.web.basic.domain-class-converter) also registers a `PageableHandlerMethodArgumentResolver` as well as an instance of `SortHandlerMethodArgumentResolver`.
The registration enables `Pageable` and `Sort` as valid controller method arguments, as the following example shows:

Using Pageable as a controller method argument

```java
@Controller @RequestMapping("/users") class UserController {
private final UserRepository repository;
UserController(UserRepository repository) {this.repository = repository;}
@RequestMapping String showUsers(Model model, Pageable pageable) {
model.addAttribute("users", repository.findAll(pageable)); return "users";}}
```

The preceding method signature causes Spring MVC try to derive a `Pageable` instance from the request parameters by using the following default configuration:

| `page` | Page you want to retrieve. 0-indexed and defaults to 0. |
| --- | --- |
| `size` | Size of the page you want to retrieve. Defaults to 20. |
| `sort` | Properties that should be sorted by in the format `property,property(,ASC\|DESC)(,IgnoreCase)`. The default sort direction is case-sensitive ascending. Use multiple `sort` parameters if you want to switch direction or case sensitivity — for example, `?sort=firstname&sort=lastname,asc&sort=city,ignorecase`. |

> [!IMPORTANT]
> `Sort.Order` instances resolved from request parameters are plain transfer objects carrying property names as is, without any validation against the domain model. Applications are responsible for verifying these values to prevent unintended sorting.

To customize this behavior, register a bean that implements the `PageableHandlerMethodArgumentResolverCustomizer` interface or the `SortHandlerMethodArgumentResolverCustomizer` interface, respectively.
Its `customize()` method gets called, letting you change settings, as the following example shows:

```java
@Bean SortHandlerMethodArgumentResolverCustomizer sortCustomizer() {
    return s -> s.setPropertyDelimiter("<-->");
}
```

If setting the properties of an existing `MethodArgumentResolver` is not sufficient for your purpose, extend either `SpringDataWebConfiguration` or the HATEOAS-enabled equivalent, override the `pageableResolver()` or `sortResolver()` methods, and import your customized configuration file instead of using the `@Enable` annotation.

If you need multiple `Pageable` or `Sort` instances to be resolved from the request (for multiple tables, for example), you can use Spring’s `@Qualifier` annotation to distinguish one from another.
The request parameters then have to be prefixed with `${qualifier}_`.
The following example shows the resulting method signature:

```java
String showUsers(Model model,
      @Qualifier("thing1") Pageable first,
      @Qualifier("thing2") Pageable second) { … }
```

You have to populate `thing1_page`, `thing2_page`, and so on.

The default `Pageable` passed into the method is equivalent to a `PageRequest.of(0, 20)`, but you can customize it by using the `@PageableDefault` annotation on the `Pageable` parameter.

<a id="repositories-core-extensions--core.web.page"></a>
<a id="repositories-core-extensions--creating-json-representations-for-page"></a>

### Creating JSON representations for `Page`

It’s common for Spring MVC controllers to try to ultimately render a representation of a Spring Data page to clients.
While one could simply return `Page` instances from handler methods to let Jackson render them as is, we strongly recommend against this as the underlying implementation class `PageImpl` is a domain type.
This means we might want or have to change its API for unrelated reasons, and such changes might alter the resulting JSON representation in a breaking way.

With Spring Data 3.1, we started hinting at the problem by issuing a warning log describing the problem.
We still ultimately recommend to leverage [the integration with Spring HATEOAS](#repositories-core-extensions--core.web.pageables) for a fully stable and hypermedia-enabled way of rendering pages that easily allow clients to navigate them.
But as of version 3.3 Spring Data ships a page rendering mechanism that is convenient to use but does not require the inclusion of Spring HATEOAS.

<a id="repositories-core-extensions--core.web.page.paged-model"></a>
<a id="repositories-core-extensions--using-spring-data-s-pagedmodel"></a>

#### Using Spring Data’s `PagedModel`

At its core, the support consists of a simplified version of Spring HATEOAS' `PagedModel` (the Spring Data one located in the `org.springframework.data.web` package).
It can be used to wrap `Page` instances and result in a simplified representation that reflects the structure established by Spring HATEOAS but omits the navigation links.

```java
import org.springframework.data.web.PagedModel;

@Controller
class MyController {

  private final MyRepository repository;

  // Constructor omitted

  @GetMapping("/page")
  PagedModel<?> page(Pageable pageable) {
    return new PagedModel<>(repository.findAll(pageable)); (1)
  }
}
```

**1**

Wraps the `Page` instance into a `PagedModel`.

This will result in a JSON structure looking like this:

```javascript
{"content" : [… // Page content rendered here ],"page" : {"size" : 20,"totalElements" : 30,"totalPages" : 2,"number" : 0}}
```

Note how the document contains a `page` field exposing the essential pagination metadata.

<a id="repositories-core-extensions--core.web.page.config"></a>
<a id="repositories-core-extensions--globally-enabling-simplified-page-rendering"></a>

#### Globally enabling simplified `Page` rendering

If you don’t want to change all your existing controllers to add the mapping step to return `PagedModel` instead of `Page` you can enable the automatic translation of `PageImpl` instances into `PagedModel` by tweaking `@EnableSpringDataWebSupport` as follows:

```java
@EnableSpringDataWebSupport(pageSerializationMode = VIA_DTO)
class MyConfiguration { }
```

This will allow your controller to still return `Page` instances and they will automatically be rendered into the simplified representation:

```java
@Controller class MyController {
private final MyRepository repository;
// Constructor omitted
@GetMapping("/page") Page<?> page(Pageable pageable) {return repository.findAll(pageable);}}
```

<a id="repositories-core-extensions--core.web.pageables"></a>
<a id="repositories-core-extensions--hypermedia-support-for-page-and-slice"></a>

#### Hypermedia Support for `Page` and `Slice`

Spring HATEOAS ships with a representation model class (`PagedModel`/`SlicedModel`) that allows enriching the content of a `Page` or `Slice` instance with the necessary `Page`/`Slice` metadata as well as links to let the clients easily navigate the pages.
The conversion of a `Page` to a `PagedModel` is done by an implementation of the Spring HATEOAS `RepresentationModelAssembler` interface, called the `PagedResourcesAssembler`.
Similarly `Slice` instances can be converted to a `SlicedModel` using a `SlicedResourcesAssembler`.
The following example shows how to use a `PagedResourcesAssembler` as a controller method argument, as the `SlicedResourcesAssembler` works exactly the same:

Using a PagedResourcesAssembler as controller method argument

```java
@Controller
class PersonController {

  private final PersonRepository repository;

  // Constructor omitted

  @GetMapping("/people")
  HttpEntity<PagedModel<Person>> people(Pageable pageable,
    PagedResourcesAssembler assembler) {

    Page<Person> people = repository.findAll(pageable);
    return ResponseEntity.ok(assembler.toModel(people));
  }
}
```

Enabling the configuration, as shown in the preceding example, lets the `PagedResourcesAssembler` be used as a controller method argument.
Calling `toModel(…)` on it has the following effects:

- The content of the `Page` becomes the content of the `PagedModel` instance.
- The `PagedModel` object gets a `PageMetadata` instance attached, and it is populated with information from the `Page` and the underlying `Pageable`.
- The `PagedModel` may get `prev` and `next` links attached, depending on the page’s state.
  The links point to the URI to which the method maps.
  The pagination parameters added to the method match the setup of the `PageableHandlerMethodArgumentResolver` to make sure the links can be resolved later.

Assume we have 30 `Person` instances in the database.
You can now trigger a request (`GET localhost:8080/people`) and see output similar to the following:

```javascript
{ "links" : [{ "rel" : "next", "href" : "http://localhost:8080/persons?page=1&size=20" } ],"content" : [… // 20 Person instances rendered here ],"page" : {"size" : 20,"totalElements" : 30,"totalPages" : 2,"number" : 0}}
```

> [!WARNING]
> The JSON envelope format shown here doesn’t follow any formally specified structure and it’s not guaranteed stable and we might change it at any time.
> It’s highly recommended to enable the rendering as a hypermedia-enabled, official media type, supported by Spring HATEOAS, like [HAL](https://docs.spring.io/spring-hateoas/docs/3.1.1/reference/html/#mediatypes.hal).
> Those can be activated by using its `@EnableHypermediaSupport` annotation.
> Find more information in the [Spring HATEOAS reference documentation](https://docs.spring.io/spring-hateoas/docs/3.1.1/reference/html/#configuration.at-enable).

The assembler produced the correct URI and also picked up the default configuration to resolve the parameters into a `Pageable` for an upcoming request.
This means that, if you change that configuration, the links automatically adhere to the change.
By default, the assembler points to the controller method it was invoked in, but you can customize that by passing a custom `Link` to be used as base to build the pagination links, which overloads the `PagedResourcesAssembler.toModel(…)` method.

<a id="repositories-core-extensions--core.web.basic.jackson-mappers"></a>
<a id="repositories-core-extensions--spring-data-jackson-modules"></a>

### Spring Data Jackson Modules

The core module, and some of the store specific ones, ship with a set of Jackson Modules for types, like `org.springframework.data.geo.Distance` and `org.springframework.data.geo.Point`, used by the Spring Data domain.
Those modules are imported once [web support](#repositories-core-extensions--core.web) is enabled and a `tools.jackson.databind.ObjectMapper` (Jackson 3) is available on the classpath.

> [!NOTE]
> `tools.jackson.databind` is the Jackson 3 package prefix.
> Jackson 2 used `com.fasterxml.jackson.databind`.
> Jackson 2 support is deprecated and will be removed in a future release; see the [Jackson 3 migration guide](https://github.com/FasterXML/jackson/wiki/Jackson-Release-3.0) for upgrade instructions.

During initialization `SpringDataJackson3Modules`, like the `SpringDataJackson3Configuration`, get picked up by the infrastructure, so that the declared `tools.jackson.databind.JacksonModule`s are made available to the Jackson `ObjectMapper`.

Data binding mixins for the following domain types are registered by the common infrastructure.

```
org.springframework.data.geo.Distance
org.springframework.data.geo.Point
org.springframework.data.geo.Box
org.springframework.data.geo.Circle
org.springframework.data.geo.Polygon
```

> [!NOTE]
> The individual module may provide additional `SpringDataJackson3Modules`.
> Please refer to the store specific section for more details.

<a id="repositories-core-extensions--core.web.binding"></a>
<a id="repositories-core-extensions--web-databinding-support"></a>

### Web Databinding Support

You can use Spring Data projections (described in [Projections](#repositories-projections)) to bind incoming request payloads by using either [JSONPath](https://goessner.net/articles/JsonPath/) expressions (requires [Jayway JsonPath](https://github.com/json-path/JsonPath)) or [XPath](https://www.w3.org/TR/xpath-31/) expressions (requires [XmlBeam](https://xmlbeam.org/)), as the following example shows:

HTTP payload binding using JSONPath or XPath expressions

```java
@ProjectedPayload
public interface UserPayload {

  @XBRead("//firstname")
  @JsonPath("$..firstname")
  String getFirstname();

  @XBRead("/lastname")
  @JsonPath({ "$.lastname", "$.user.lastname" })
  String getLastname();
}
```

You can use the type shown in the preceding example as a Spring MVC handler method argument or by using `ParameterizedTypeReference` on one of methods of the `RestTemplate`.
The preceding method declarations would try to find `firstname` anywhere in the given document.
The `lastname` XML lookup is performed on the top-level of the incoming document.
The JSON variant of that tries a top-level `lastname` first but also tries `lastname` nested in a `user` sub-document if the former does not return a value.
That way, changes in the structure of the source document can be mitigated easily without having clients calling the exposed methods (usually a drawback of class-based payload binding).

Nested projections are supported as described in [Projections](#repositories-projections).
If the method returns a complex, non-interface type, a Jackson `ObjectMapper` is used to map the final value.

For Spring MVC, the necessary converters are registered automatically as soon as `@EnableSpringDataWebSupport` is active and the required dependencies are available on the classpath.
For usage with `RestTemplate`, register a `ProjectingJacksonHttpMessageConverter` (JSON) or `XmlBeamHttpMessageConverter` manually.

For more information, see the [web projection example](https://github.com/spring-projects/spring-data-examples/tree/main/web/projection) in the canonical [Spring Data Examples repository](https://github.com/spring-projects/spring-data-examples).

> [!NOTE]
> By default, binding collection-like properties is capped at 1024 entries. You can override this limit by setting the `spring.data.web.projection.collection-limit` property through a `spring.properties` file or as a system property.

<a id="repositories-core-extensions--core.web.type-safe"></a>
<a id="repositories-core-extensions--querydsl-web-support"></a>

### Querydsl Web Support

For those stores that have [Querydsl](http://www.querydsl.com/) integration, you can derive queries from the attributes contained in a `Request` query string.

Consider the following query string:

```text
?firstname=Dave&lastname=Matthews
```

Given the `User` object from the previous examples, you can resolve a query string to the following value by using the `QuerydslPredicateArgumentResolver`, as follows:

```text
QUser.user.firstname.eq("Dave").and(QUser.user.lastname.eq("Matthews"))
```

> [!NOTE]
> The feature is automatically enabled, along with `@EnableSpringDataWebSupport`, when Querydsl is found on the classpath.

Adding a `@QuerydslPredicate` to the method signature provides a ready-to-use `Predicate`, which you can run by using the `QuerydslPredicateExecutor`.

> [!TIP]
> Type information is typically resolved from the method’s return type.
> Since that information does not necessarily match the domain type, it might be a good idea to use the `root` attribute of `QuerydslPredicate`.

The following example shows how to use `@QuerydslPredicate` in a method signature:

```java
@Controller
class UserController {

  @Autowired UserRepository repository;

  @RequestMapping(value = "/", method = RequestMethod.GET)
  String index(Model model, @QuerydslPredicate(root = User.class) Predicate predicate,    (1)
          Pageable pageable, @RequestParam MultiValueMap<String, String> parameters) {

    model.addAttribute("users", repository.findAll(predicate, pageable));

    return "index";
  }
}
```

**1**

Resolve query string arguments to matching `Predicate` for `User`.

The default binding is as follows:

- `Object` on simple properties as `eq`.
- `Object` on collection like properties as `contains`.
- `Collection` on simple properties as `in`.

You can customize those bindings through the `bindings` attribute of `@QuerydslPredicate` or by making use of Java 8 `default methods` and adding the `QuerydslBinderCustomizer` method to the repository interface, as follows:

```java
interface UserRepository extends CrudRepository<User, String>,
                                 QuerydslPredicateExecutor<User>,                (1)
                                 QuerydslBinderCustomizer<QUser> {               (2)

  @Override
  default void customize(QuerydslBindings bindings, QUser user) {

    bindings.bind(user.username).first((path, value) -> path.contains(value))    (3)
    bindings.bind(String.class)
      .first((StringPath path, String value) -> path.containsIgnoreCase(value)); (4)
    bindings.excluding(user.password);                                           (5)
  }
}
```

**1**

`QuerydslPredicateExecutor` provides access to specific finder methods for `Predicate`.

**2**

`QuerydslBinderCustomizer` defined on the repository interface is automatically picked up and shortcuts `@QuerydslPredicate(bindings=…)`.

**3**

Define the binding for the `username` property to be a simple `contains` binding.

**4**

Define the default binding for `String` properties to be a case-insensitive `contains` match.

**5**

Exclude the `password` property from `Predicate` resolution.

> [!TIP]
> You can register a `QuerydslBinderCustomizerDefaults` bean holding default Querydsl bindings before applying specific bindings from the repository or `@QuerydslPredicate`.

<a id="repositories-core-extensions--core.repository-populators"></a>
<a id="repositories-core-extensions--repository-populators"></a>

## Repository Populators

If you work with the Spring JDBC module, you are probably familiar with the support for populating a `DataSource` with SQL scripts.
A similar abstraction is available on the repositories level, although it does not use SQL as the data definition language because it must be store-independent.
Thus, the populators support XML (through Spring’s OXM abstraction) and JSON (through Jackson) to define data with which to populate the repositories.

Assume you have a file called `data.json` with the following content:

Data defined in JSON

```javascript
[ { "_class" : "com.acme.Person",
 "firstname" : "Dave",
  "lastname" : "Matthews" },
  { "_class" : "com.acme.Person",
 "firstname" : "Carter",
  "lastname" : "Beauford" } ]
```

You can populate your repositories by using the populator elements of the repository namespace provided in Spring Data Commons.
To populate the preceding data to your `PersonRepository`, declare a populator similar to the following:

Declaring a Jackson repository populator

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:repository="http://www.springframework.org/schema/data/repository"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    https://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/data/repository
    https://www.springframework.org/schema/data/repository/spring-repository.xsd">

  <repository:jackson2-populator locations="classpath:data.json" />

</beans>
```

The preceding declaration causes the `data.json` file to be read and deserialized by a Jackson `ObjectMapper`.

The type to which the JSON object is unmarshalled is determined by inspecting the `_class` attribute of the JSON document.
The infrastructure eventually selects the appropriate repository to handle the object that was deserialized.

To instead use XML to define the data the repositories should be populated with, you can use the `unmarshaller-populator` element.
You configure it to use one of the XML marshaller options available in Spring OXM.
See the [Spring reference documentation](https://docs.spring.io/spring-framework/reference/7.0/data-access/oxm.html) for details.
The following example shows how to unmarshall a repository populator with JAXB:

Declaring an unmarshalling repository populator (using JAXB)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:repository="http://www.springframework.org/schema/data/repository"
  xmlns:oxm="http://www.springframework.org/schema/oxm"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    https://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/data/repository
    https://www.springframework.org/schema/data/repository/spring-repository.xsd
    http://www.springframework.org/schema/oxm
    https://www.springframework.org/schema/oxm/spring-oxm.xsd">

  <repository:unmarshaller-populator locations="classpath:data.json"
    unmarshaller-ref="unmarshaller" />

  <oxm:jaxb2-marshaller contextPath="com.acme" />

</beans>
```

---

<a id="repositories-scrolling"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/scrolling.html -->

<!-- page_index: 15 -->

# Scrolling

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-scrolling--page-title"></a>
<a id="repositories-scrolling--scrolling"></a>

# Scrolling

Scrolling is a more fine-grained approach to iterating through chunks of larger result sets.
Scrolling consists of a stable sort, a scroll type (Offset- or Keyset-based scrolling) and result limiting.
You can define simple sorting expressions by using property names and define static result limiting using the [`Top` or `First` keyword](#repositories-query-methods-details--repositories.limit-query-result) through query derivation.
You can concatenate expressions to collect multiple criteria into one expression.

Scroll queries return a `Window<T>` that allows obtaining the element’s scroll position to fetch the next `Window<T>` until your application has consumed the entire query result.
Similar to consuming a Java `Iterator<List<…>>` by obtaining the next batch of results, query result scrolling lets you access a `ScrollPosition` through `Window.positionAt(…)`, as in the following example:

```java
Window<User> users = repository.findFirst10ByLastnameOrderByFirstname("Doe", ScrollPosition.offset());
do {

  for (User u : users) {
    // consume the user
  }

  if (users.isLast() || users.isEmpty()) {
    break;
  }

  // obtain the next Scroll
  users = repository.findFirst10ByLastnameOrderByFirstname("Doe", users.positionAt(users.size() - 1));
} while (!users.isEmpty());
```

> [!NOTE]
> The `ScrollPosition` identifies the exact position of an element with the entire query result.
> Query execution treats the position parameter *exclusive*, results will start *after* the given position.
> `ScrollPosition#offset()` and `ScrollPosition#keyset()` as special incarnations of a `ScrollPosition` indicating the start of a scroll operation.

> [!NOTE]
> The above example shows static sorting and limiting.
> You can define query methods alternatively that accept a `Sort` object define a more complex sorting order or sorting on a per-request basis.
> In a similar way, providing a `Limit` object allows you to define a dynamic limit on a per-request basis instead of applying a static limitation.
> Read more on dynamic sorting and limiting in the [Query Methods Details](#repositories-query-methods-details--repositories.special-parameters).

Scrolling through consuming `Window` instances requires quite a few conditionals to reach optimum database round-trips and can quickly become a repetitive task that can be simplified using `WindowIterator`.

`WindowIterator` provides a utility to simplify scrolling across `Window`s by removing the need to check for the presence of a next `Window` and applying the `ScrollPosition`.

```java
WindowIterator<User> users = WindowIterator.of(position -> repository.findFirst10ByLastnameOrderByFirstname("Doe", position))
  .startingAt(ScrollPosition.offset());

while (users.hasNext()) {
  User u = users.next();
  // consume the user
}
```

<a id="repositories-scrolling--repositories.scrolling.offset"></a>
<a id="repositories-scrolling--scrolling-using-offset"></a>

## Scrolling using Offset

Offset scrolling uses similar to pagination, an Offset counter to skip a number of results and let the data source only return results beginning at the given Offset.
This simple mechanism avoids large results being sent to the client application.
However, most databases require materializing the full query result before your server can return the results.

Example 1. Using `OffsetScrollPosition` with Repository Query Methods

```java
interface UserRepository extends Repository<User, Long> {

  Window<User> findFirst10ByLastnameOrderByFirstname(String lastname, OffsetScrollPosition position);
}

WindowIterator<User> users = WindowIterator.of(position -> repository.findFirst10ByLastnameOrderByFirstname("Doe", position))
  .startingAt(OffsetScrollPosition.initial()); (1)
```

**1**

Start with no offset to include the element at position `0`.

> [!WARNING]
> There is a difference between `ScrollPosition.offset()` and `ScrollPosition.offset(0L)`.
> The former indicates the start of scroll operation, pointing to no specific offset whereas the latter identifies the first element (at position `0`) of the result.
> Given the *exclusive* nature of scrolling, using `ScrollPosition.offset(0)` skips the first element and translate to an offset of `1`.

<a id="repositories-scrolling--repositories.scrolling.keyset"></a>
<a id="repositories-scrolling--scrolling-using-keyset-filtering"></a>

## Scrolling using Keyset-Filtering

Offset-based scrolling requires most databases to materialize the entire result before the server can return it.
So while the client only sees the portion of the requested results, your server needs to build the full result, which causes additional load.

Keyset-Filtering approaches result subset retrieval by leveraging built-in capabilities of your database aiming to reduce the computation and I/O requirements for individual queries.
This approach maintains a set of keys to resume scrolling by passing keys into the query, effectively amending your filter criteria.

The core idea of Keyset-Filtering is to start retrieving results using a stable sorting order.
Once you want to scroll to the next chunk, you obtain a `ScrollPosition` that is used to reconstruct the position within the sorted result.
The `ScrollPosition` captures the keyset of the last entity within the current `Window`.
To run the query, reconstruction rewrites the criteria clause to include all sort fields and the primary key so that the database can leverage potential indexes to run the query.
The database needs only constructing a much smaller result from the given keyset position without the need to fully materialize a large result and then skipping results until reaching a particular offset.

> [!WARNING]
> Keyset-Filtering requires the keyset properties (those used for sorting) to be non-nullable.
> This limitation applies due to the store specific `null` value handling of comparison operators as well as the need to run queries against an indexed source.
> Keyset-Filtering on nullable properties will lead to unexpected results.

Using `KeysetScrollPosition` with Repository Query Methods

```java
interface UserRepository extends Repository<User, Long> {

  Window<User> findFirst10ByLastnameOrderByFirstname(String lastname, KeysetScrollPosition position);
}

WindowIterator<User> users = WindowIterator.of(position -> repository.findFirst10ByLastnameOrderByFirstname("Doe", position))
  .startingAt(ScrollPosition.keyset()); (1)
```

**1**

Start at the very beginning and do not apply additional filtering.

Keyset-Filtering works best when your database contains an index that matches the sort fields, hence a static sort works well.
Scroll queries applying Keyset-Filtering require to the properties used in the sort order to be returned by the query, and these must be mapped in the returned entity.

You can use interface and DTO projections, however make sure to include all properties that you’ve sorted by to avoid keyset extraction failures.

When specifying your `Sort` order, it is sufficient to include sort properties relevant to your query;
You do not need to ensure unique query results if you do not want to.
The keyset query mechanism amends your sort order by including the primary key (or any remainder of composite primary keys) to ensure each query result is unique.

---

<a id="repositories-null-handling"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/null-handling.html -->

<!-- page_index: 16 -->

# Null Handling of Repository Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-null-handling--page-title"></a>
<a id="repositories-null-handling--null-handling-of-repository-methods"></a>

# Null Handling of Repository Methods

Repository CRUD methods that return an individual aggregate instances can use `Optional` to indicate the potential absence of a value.
Besides that, Spring Data supports returning the following wrapper types on query methods:

- `com.google.common.base.Optional`
- `scala.Option`
- `io.vavr.control.Option`

Alternatively, query methods can choose not to use a wrapper type at all.
The absence of a query result is then indicated by returning `null`.
Repository methods returning collections, collection alternatives, wrappers, and streams are guaranteed never to return `null` but rather the corresponding empty representation.
See “[Repository query return types](#repositories-query-return-types-reference)” for details.

<a id="repositories-null-handling--repositories.nullability.annotations"></a>
<a id="repositories-null-handling--nullability-annotations"></a>

## Nullability Annotations

<a id="repositories-null-handling--_jspecify"></a>
<a id="repositories-null-handling--jspecify"></a>

### JSpecify

As of Spring Framework 7 and Spring Data 4, you can express nullability constraints for repository methods by using [JSpecify](https://jspecify.dev/docs/start-here/).
JSpecify is well integrated into IntelliJ and Eclipse to provide a tooling-friendly approach and opt-in `null` checks during runtime, as follows:

- [`@NullMarked`](https://jspecify.dev/docs/api/org/jspecify/annotations/NullMarked.html): Used on the module-, package- and class-level to declare that the default behavior for parameters and return values is, respectively, neither to accept nor to produce `null` values.
- [`@NonNull`](https://jspecify.dev/docs/api/org/jspecify/annotations/NonNull.html): Used on a type level for parameter or return values that must not be `null` (not needed on parameters and return values already covered by `@NullMarked`).
- [`@Nullable`](https://jspecify.dev/docs/api/org/jspecify/annotations/Nullable.html): Used on the type level for parameter or return values that can be `null`.
- [`@NullUnmarked`](https://jspecify.dev/docs/api/org/jspecify/annotations/NullUnmarked.html): Used on the package-, class-, and method-level to roll back nullness declaration and opt-out from a previous `@NullMarked`.
  Nullness changes to unspecified in such a case.

`@NullMarked` at the package level via a `package-info.java` file

```java
@NullMarked
package org.springframework.core;

import org.jspecify.annotations.NullMarked;
```

In the various Java files belonging to the package, nullable type usages are defined explicitly with
[`@Nullable`](https://jspecify.dev/docs/api/org/jspecify/annotations/Nullable.html).
It is recommended that this annotation is specified just before the related type.

For example, for a field:

```java
private @Nullable String fileEncoding;
```

Or for method parameters and return value:

```java
public static @Nullable String buildMessage(@Nullable String message,
                                            @Nullable Throwable cause) {
    // ...
}
```

When overriding a method, nullness annotations are not inherited from the superclass method.
That means those nullness annotations should be repeated if you just want to override the implementation and keep the same API nullness.

With arrays and varargs, you need to be able to differentiate the nullness of the elements from the nullness of the array itself.
Pay attention to the syntax
[defined by the Java specification](https://docs.oracle.com/javase/specs/jls/se17/html/jls-9.html#jls-9.7.4) which may be initially surprising:

- `@Nullable Object[] array` means individual elements can be null but the array itself can’t.
- `Object @Nullable [] array` means individual elements can’t be null but the array itself can.
- `@Nullable Object @Nullable [] array` means both individual elements and the array can be null.

The Java specifications also enforces that annotations defined with `@Target(ElementType.TYPE_USE)` like JSpecify
`@Nullable` should be specified after the last `.` with inner or fully qualified types:

- `Cache.@Nullable ValueWrapper`
- `jakarta.validation.@Nullable Validator`

[`@NonNull`](https://jspecify.dev/docs/api/org/jspecify/annotations/NonNull.html) and
[`@NullUnmarked`](https://jspecify.dev/docs/api/org/jspecify/annotations/NullUnmarked.html) should rarely be needed for typical use cases.

<a id="repositories-null-handling--_spring_framework_nullability_and_jsr_305_annotations"></a>
<a id="repositories-null-handling--spring-framework-nullability-and-jsr-305-annotations"></a>

### Spring Framework Nullability and JSR-305 Annotations

You can express nullability constraints for repository methods by using [Spring Framework’s nullability annotations](https://docs.spring.io/spring-framework/reference/7.0/core/null-safety.html).

> [!NOTE]
> As of Spring Framework 7, Spring’s nullability annotations are deprecated in favor of JSpecify.
> Consult the framework documentation on [Migrating from Spring null-safety annotations to JSpecify](https://docs.spring.io/spring-framework/reference/7.0/core/null-safety.html) for more information.

They provide a tooling-friendly approach and opt-in `null` checks during runtime, as follows:

- [`@NonNullApi`](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/lang/NonNullApi.html): Used on the package level to declare that the default behavior for parameters and return values is, respectively, neither to accept nor to produce `null` values.
- [`@NonNull`](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/lang/NonNull.html): Used on a parameter or return value that must not be `null` (not needed on a parameter and return value where `@NonNullApi` applies).
- [`@Nullable`](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/lang/Nullable.html): Used on a parameter or return value that can be `null`.

Spring annotations are meta-annotated with [JSR 305](https://jcp.org/en/jsr/detail?id=305) annotations (a dormant but widely used JSR).
JSR 305 meta-annotations let tooling vendors (such as [IDEA](https://www.jetbrains.com/help/idea/nullable-and-notnull-annotations.html), [Eclipse](https://help.eclipse.org/latest/index.jsp?topic=/org.eclipse.jdt.doc.user/tasks/task-using_external_null_annotations.htm), and [Kotlin](https://kotlinlang.org/docs/reference/java-interop.html#null-safety-and-platform-types)) provide null-safety support in a generic way, without having to hard-code support for Spring annotations.
To enable runtime checking of nullability constraints for query methods, you need to activate non-nullability on the package level by using Spring’s `@NonNullApi` in `package-info.java`, as shown in the following example:

Declaring Non-nullability in `package-info.java`

```java

```

Once non-null defaulting is in place, repository query method invocations get validated at runtime for nullability constraints.
If a query result violates the defined constraint, an exception is thrown.
This happens when the method would return `null` but is declared as non-nullable (the default with the annotation defined on the package in which the repository resides).
If you want to opt-in to nullable results again, selectively use `@Nullable` on individual methods.
Using the result wrapper types mentioned at the start of this section continues to work as expected: an empty result is translated into the value that represents absence.

The following example shows a number of the techniques just described:

Using different nullability constraints

```java
package com.acme;                                                       (1)

import org.springframework.lang.Nullable;

interface UserRepository extends Repository<User, Long> {

  User getByEmailAddress(EmailAddress emailAddress);                    (2)

  @Nullable
  User findByEmailAddress(@Nullable EmailAddress emailAddress);          (3)

  Optional<User> findOptionalByEmailAddress(EmailAddress emailAddress); (4)
}
```

**1**

The repository resides in a package (or sub-package) for which we have defined non-null behavior.

**2**

Throws an `EmptyResultDataAccessException` when the query does not produce a result.
Throws an `IllegalArgumentException` when the `emailAddress` handed to the method is `null`.

**3**

Returns `null` when the query does not produce a result.
Also accepts `null` as the value for `emailAddress`.

**4**

Returns `Optional.empty()` when the query does not produce a result.
Throws an `IllegalArgumentException` when the `emailAddress` handed to the method is `null`.

<a id="repositories-null-handling--repositories.nullability.kotlin"></a>
<a id="repositories-null-handling--nullability-in-kotlin-based-repositories"></a>

## Nullability in Kotlin-based Repositories

Kotlin has the definition of [nullability constraints](https://kotlinlang.org/docs/reference/null-safety.html) baked into the language.
Kotlin code compiles to bytecode, which does not express nullability constraints through method signatures but rather through compiled-in metadata.
Make sure to include the `kotlin-reflect` JAR in your project to enable introspection of Kotlin’s nullability constraints.
Spring Data repositories use the language mechanism to define those constraints to apply the same runtime checks, as follows:

Using nullability constraints on Kotlin repositories

```kotlin
interface UserRepository : Repository<User, String> {

  fun findByUsername(username: String): User     (1)

  fun findByFirstname(firstname: String?): User? (2)
}
```

**1**

The method defines both the parameter and the result as non-nullable (the Kotlin default).
The Kotlin compiler rejects method invocations that pass `null` to the method.
If the query yields an empty result, an `EmptyResultDataAccessException` is thrown.

**2**

This method accepts `null` for the `firstname` parameter and returns `null` if the query does not produce a result.

---

<a id="repositories-projections"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/projections.html -->

<!-- page_index: 17 -->

# Projections

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-projections--page-title"></a>
<a id="repositories-projections--projections"></a>

# Projections

Spring Data query methods usually return one or multiple instances of the aggregate root managed by the repository.
However, it might sometimes be desirable to create projections based on certain attributes of those types.
Spring Data allows modeling dedicated return types, to more selectively retrieve partial views of the managed aggregates.

Imagine a repository and aggregate root type such as the following example:

A sample aggregate and repository

```java
class Person {
@Id UUID id; String firstname, lastname; Address address;
static class Address {String zipCode, city, street;}}
interface PersonRepository extends Repository<Person, UUID> {
Collection<Person> findByLastname(String lastname);}
```

Now imagine that we want to retrieve the person’s name attributes only.
What means does Spring Data offer to achieve this?
The rest of this chapter answers that question.

> [!NOTE]
> Projection types are types residing outside the entity’s type hierarchy.
> Superclasses and interfaces implemented by the entity are inside the type hierarchy hence returning a supertype (or implemented interface) returns an instance of the fully materialized entity.

<a id="repositories-projections--projections.interfaces"></a>
<a id="repositories-projections--interface-based-projections"></a>

## Interface-based Projections

The easiest way to limit the result of the queries to only the name attributes is by declaring an interface that exposes accessor methods for the properties to be read, as shown in the following example:

A projection interface to retrieve a subset of attributes

```java
interface NamesOnly {

  String getFirstname();
  String getLastname();
}
```

The important bit here is that the properties defined here exactly match properties in the aggregate root.
Doing so lets a query method be added as follows:

A repository using an interface based projection with a query method

```java
interface PersonRepository extends Repository<Person, UUID> {

  Collection<NamesOnly> findByLastname(String lastname);
}
```

The query execution engine creates proxy instances of that interface at runtime for each element returned and forwards calls to the exposed methods to the target object.

> [!NOTE]
> Declaring a method in your `Repository` that overrides a base method (e.g. declared in `CrudRepository`, a store-specific repository interface, or the `Simple…Repository`) results in a call to the base method regardless of the declared return type.
> Make sure to use a compatible return type as base methods cannot be used for projections.
> Some store modules support `@Query` annotations to turn an overridden base method into a query method that then can be used to return projections.

Projections can be used recursively.
If you want to include some of the `Address` information as well, create a projection interface for that and return that interface from the declaration of `getAddress()`, as shown in the following example:

A projection interface to retrieve a subset of attributes

```java
interface PersonSummary {
String getFirstname(); String getLastname(); AddressSummary getAddress();
interface AddressSummary {String getCity();}}
```

On method invocation, the `address` property of the target instance is obtained and wrapped into a projecting proxy in turn.

<a id="repositories-projections--projections.interfaces.closed"></a>
<a id="repositories-projections--closed-projections"></a>

### Closed Projections

A projection interface whose accessor methods all match properties of the target aggregate is considered to be a closed projection.
The following example (which we used earlier in this chapter, too) is a closed projection:

A closed projection

```java
interface NamesOnly {

  String getFirstname();
  String getLastname();
}
```

If you use a closed projection, Spring Data can optimize the query execution, because we know about all the attributes that are needed to back the projection proxy.
For more details on that, see the module-specific part of the reference documentation.

<a id="repositories-projections--projections.interfaces.open"></a>
<a id="repositories-projections--open-projections"></a>

### Open Projections

Accessor methods in projection interfaces can also be used to compute new values by using the `@Value` annotation, as shown in the following example:

An Open Projection

```java
interface NamesOnly {

  @Value("#{target.firstname + ' ' + target.lastname}")
  String getFullName();
  …
}
```

The aggregate root backing the projection is available in the `target` variable.
A projection interface using `@Value` is an open projection.
Spring Data cannot apply query execution optimizations in this case, because the SpEL expression could use any attribute of the aggregate root.

The expressions used in `@Value` should not be too complex — you want to avoid programming in `String` variables.
For very simple expressions, one option might be to resort to default methods (introduced in Java 8), as shown in the following example:

A projection interface using a default method for custom logic

```java
interface NamesOnly {
String getFirstname(); String getLastname();
default String getFullName() {return getFirstname().concat(" ").concat(getLastname());}}
```

This approach requires you to be able to implement logic purely based on the other accessor methods exposed on the projection interface.
A second, more flexible, option is to implement the custom logic in a Spring bean and then invoke that from the SpEL expression, as shown in the following example:

Sample Person object

```java
@Component class MyBean {
String getFullName(Person person) {…}}
interface NamesOnly {
@Value("#{@myBean.getFullName(target)}") String getFullName(); …}
```

Notice how the SpEL expression refers to `myBean` and invokes the `getFullName(…)` method and forwards the projection target as a method parameter.
Methods backed by SpEL expression evaluation can also use method parameters, which can then be referred to from the expression.
The method parameters are available through an `Object` array named `args`.
The following example shows how to get a method parameter from the `args` array:

Sample Person object

```java
interface NamesOnly {

  @Value("#{args[0] + ' ' + target.firstname + '!'}")
  String getSalutation(String prefix);
}
```

Again, for more complex expressions, you should use a Spring bean and let the expression invoke a method, as described [earlier](#repositories-projections--projections.interfaces.open.bean-reference).

<a id="repositories-projections--projections.interfaces.nullable-wrappers"></a>
<a id="repositories-projections--nullable-wrappers"></a>

### Nullable Wrappers

Getters in projection interfaces can make use of nullable wrappers for improved null-safety.
Currently supported wrapper types are:

- `java.util.Optional`
- `com.google.common.base.Optional`
- `scala.Option`
- `io.vavr.control.Option`

A projection interface using nullable wrappers

```java
interface NamesOnly {

  Optional<String> getFirstname();
}
```

If the underlying projection value is not `null`, then values are returned using the present-representation of the wrapper type.
In case the backing value is `null`, then the getter method returns the empty representation of the used wrapper type.

<a id="repositories-projections--projections.dtos"></a>
<a id="repositories-projections--class-based-projections-dtos"></a>

## Class-based Projections (DTOs)

Another way of defining projections is by using value type DTOs (Data Transfer Objects) that hold properties for the fields that are supposed to be retrieved.
These DTO types can be used in exactly the same way projection interfaces are used, except that no proxying happens and no nested projections can be applied.

If the store optimizes the query execution by limiting the fields to be loaded, the fields to be loaded are determined from the parameter names of the constructor that is exposed.

The following example shows a projecting DTO:

A projecting DTO

```java
record NamesOnly(String firstname, String lastname) {
}
```

Java Records are ideal to define DTO types since they adhere to value semantics:
All fields are `private final` and `equals(…)`/`hashCode()`/`toString()` methods are created automatically.
Alternatively, you can use any class that defines the properties you want to project.

<a id="repositories-projections--projection.dynamic"></a>
<a id="repositories-projections--dynamic-projections"></a>

### Dynamic Projections

So far, we have used the projection type as the return type or element type of a collection.
However, you might want to select the type to be used at invocation time (which makes it dynamic).
To apply dynamic projections, use a query method such as the one shown in the following example:

A repository using a dynamic projection parameter

```java
interface PersonRepository extends Repository<Person, UUID> {

  <T> Collection<T> findByLastname(String lastname, Class<T> type);
}
```

This way, the method can be used to obtain the aggregates as is or with a projection applied, as shown in the following example:

Using a repository with dynamic projections

```java
void someMethod(PersonRepository people) {

  Collection<Person> aggregates =
    people.findByLastname("Matthews", Person.class);

  Collection<NamesOnly> aggregates =
    people.findByLastname("Matthews", NamesOnly.class);
}
```

> [!NOTE]
> Query parameters of type `Class` are inspected whether they qualify as dynamic projection parameter.
> If the actual return type of the query equals the generic parameter type of the `Class` parameter, then the matching `Class` parameter is not available for usage within the query or SpEL expressions.
> If you want to use a `Class` parameter as query argument then make sure to use a different generic parameter, for example `Class<?>`.

> [!NOTE]
> When using [Class-based projection](#repositories-projections--projections.dtos), types must declare a single constructor so that Spring Data can determine their input properties.
> If your class defines more than one constructor, then you cannot use the type without further hints for DTO projections.
> In such a case annotate the desired constructor with `@PersistenceCreator` as outlined below so that Spring Data can determine which properties to select:
>
> ```java
> public class NamesOnly {
>
>   private final String firstname;
>   private final String lastname;
>
>   protected NamesOnly() { }
>
>   @PersistenceCreator
>   public NamesOnly(String firstname, String lastname) {
>       this.firstname = firstname;
>       this.lastname = lastname;
>   }
>
>   // ...
> }
> ```

---

<a id="query-by-example"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/query-by-example.html -->

<!-- page_index: 18 -->

# Query by Example

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="query-by-example--page-title"></a>
<a id="query-by-example--query-by-example"></a>

# Query by Example

<a id="query-by-example--query-by-example.introduction"></a>
<a id="query-by-example--introduction"></a>

## Introduction

This chapter provides an introduction to Query by Example and explains how to use it.

Query by Example (QBE) is a user-friendly querying technique with a simple interface.
It allows dynamic query creation and does not require you to write queries that contain field names.
In fact, Query by Example does not require you to write queries by using store-specific query languages at all.

> [!NOTE]
> This chapter explains the core concepts of Query by Example.
> The information is pulled from the Spring Data Commons module.
> Depending on your database, String matching support can be limited.

<a id="query-by-example--query-by-example.usage"></a>
<a id="query-by-example--usage"></a>

## Usage

The Query by Example API consists of four parts:

- Probe: The actual example of a domain object with populated fields.
- `ExampleMatcher`: The `ExampleMatcher` carries details on how to match particular fields.
  It can be reused across multiple Examples.
- `Example`: An `Example` consists of the probe and the `ExampleMatcher`.
  It is used to create the query.
- `FetchableFluentQuery`: A `FetchableFluentQuery` offers a fluent API, that allows further customization of a query derived from an `Example`.
  Using the fluent API lets you specify ordering projection and result processing for your query.

Query by Example is well suited for several use cases:

- Querying your data store with a set of static or dynamic constraints.
- Frequent refactoring of the domain objects without worrying about breaking existing queries.
- Working independently of the underlying data store API.

Query by Example also has several limitations:

- No support for nested or grouped property constraints, such as `firstname = ?0 or (firstname = ?1 and lastname = ?2)`.
- Store-specific support on string matching.
  Depending on your databases, String matching can support starts/contains/ends/regex for strings.
- Exact matching for other property types.

Before getting started with Query by Example, you need to have a domain object.
To get started, create an interface for your repository, as shown in the following example:

Sample Person object

```java
public class Person {

  @Id
  private String id;
  private String firstname;
  private String lastname;
  private Address address;

  // … getters and setters omitted
}
```

The preceding example shows a simple domain object.
You can use it to create an `Example`.
By default, fields having `null` values are ignored, and strings are matched by using the store specific defaults.

> [!NOTE]
> Inclusion of properties into a Query by Example criteria is based on nullability.
> Properties using primitive types (`int`, `double`, …) are always included unless the [`ExampleMatcher` ignores the property path](#query-by-example--query-by-example.matchers).

Examples can be built by either using the `of` factory method or by using [`ExampleMatcher`](#query-by-example--query-by-example.matchers). `Example` is immutable.
The following listing shows a simple Example:

Example 1. Simple Example

```java
Person person = new Person();                         (1)
person.setFirstname("Dave");                          (2)

Example<Person> example = Example.of(person);         (3)
```

| **1** | Create a new instance of the domain object. |
| --- | --- |
| **2** | Set the properties to query. |
| **3** | Create the `Example`. |

You can run the example queries by using repositories.
To do so, let your repository interface extend `QueryByExampleExecutor<T>`.
The following listing shows an excerpt from the `QueryByExampleExecutor` interface:

The `QueryByExampleExecutor`

```java
public interface QueryByExampleExecutor<T> {

  <S extends T> S findOne(Example<S> example);

  <S extends T> Iterable<S> findAll(Example<S> example);

  // … more functionality omitted.
}
```

<a id="query-by-example--query-by-example.matchers"></a>
<a id="query-by-example--example-matchers"></a>

## Example Matchers

Examples are not limited to default settings.
You can specify your own defaults for string matching, null handling, and property-specific settings by using the `ExampleMatcher`, as shown in the following example:

Example 2. Example matcher with customized matching

```java
Person person = new Person();                          (1)
person.setFirstname("Dave");                           (2)

ExampleMatcher matcher = ExampleMatcher.matching()     (3)
  .withIgnorePaths("lastname")                         (4)
  .withIncludeNullValues()                             (5)
  .withStringMatcher(StringMatcher.ENDING);            (6)

Example<Person> example = Example.of(person, matcher); (7)
```

| **1** | Create a new instance of the domain object. |
| --- | --- |
| **2** | Set properties. |
| **3** | Create an `ExampleMatcher` to expect all values to match. It is usable at this stage even without further configuration. |
| **4** | Construct a new `ExampleMatcher` to ignore the `lastname` property path. |
| **5** | Construct a new `ExampleMatcher` to ignore the `lastname` property path and to include null values. |
| **6** | Construct a new `ExampleMatcher` to ignore the `lastname` property path, to include null values, and to perform suffix string matching. |
| **7** | Create a new `Example` based on the domain object and the configured `ExampleMatcher`. |

By default, the `ExampleMatcher` expects all values set on the probe to match.
If you want to get results matching any of the predicates defined implicitly, use `ExampleMatcher.matchingAny()`.

You can specify behavior for individual properties (such as "firstname" and "lastname" or, for nested properties, "address.city").
You can tune it with matching options and case sensitivity, as shown in the following example:

Configuring matcher options

```java
ExampleMatcher matcher = ExampleMatcher.matching()
  .withMatcher("firstname", endsWith())
  .withMatcher("lastname", startsWith().ignoreCase());
}
```

Another way to configure matcher options is to use lambdas (introduced in Java 8).
This approach creates a callback that asks the implementor to modify the matcher.
You need not return the matcher, because configuration options are held within the matcher instance.
The following example shows a matcher that uses lambdas:

Configuring matcher options with lambdas

```java
ExampleMatcher matcher = ExampleMatcher.matching()
  .withMatcher("firstname", match -> match.endsWith())
  .withMatcher("firstname", match -> match.startsWith());
}
```

Queries created by `Example` use a merged view of the configuration.
Default matching settings can be set at the `ExampleMatcher` level, while individual settings can be applied to particular property paths.
Settings that are set on `ExampleMatcher` are inherited by property path settings unless they are defined explicitly.
Settings on a property path have higher precedence than default settings.
The following table describes the scope of the various `ExampleMatcher` settings:

| Setting | Scope |
| --- | --- |
| Null-handling | `ExampleMatcher` |
| String matching | `ExampleMatcher` and property path |
| Ignoring properties | Property path |
| Case sensitivity | `ExampleMatcher` and property path |
| Value transformation | Property path |

<a id="query-by-example--query-by-example.fluent"></a>
<a id="query-by-example--fluent-api"></a>

## Fluent API

`QueryByExampleExecutor` defines fluent query methods for flexible execution of queries based on `Example` instances through `findBy(Example<S> example, Function<FluentQuery.FetchableFluentQuery<S>, R> queryFunction)`.

As with other methods, it executes a query derived from a `Example`.
However, the query function allows you to take control over aspects of query execution that you cannot dynamically control otherwise.
You do so by invoking the various intermediate and terminal methods of `FetchableFluentQuery`.

**Intermediate methods**

- `sortBy`: Apply an ordering for your result.
  Repeated method calls append each `Sort` (note that `page(Pageable)` using a sorted `Pageable` overrides any previous sort order).
- `limit`: Limit the result count.
- `as`: Specify the type to be read or projected to.
- `project`: Limit the queries properties.

**Terminal methods**

- `first`, `firstValue`: Return the first value. `first` returns an `Optional<T>` or `Optional.empty()` if the query did not yield any result. `firstValue` is its nullable variant without the need to use `Optional`.
- `one`, `oneValue`: Return the one value. `one` returns an `Optional<T>` or `Optional.empty()` if the query did not yield any result. `oneValue` is its nullable variant without the need to use `Optional`.
  Throws `IncorrectResultSizeDataAccessException` if more than one match found.
- `all`: Return all results as a `List<T>`.
- `page(Pageable)`: Return all results as a `Page<T>`.
- `slice(Pageable)`: Return all results as a `Slice<T>`.
- `scroll(ScrollPosition)`: Use scrolling (offset, keyset) to retrieve results as a `Window<T>`.
- `stream()`: Return a `Stream<T>` to process results lazily.
  The stream is stateful and must be closed after use.
- `count` and `exists`: Return the count of matching entities or whether any match exists.

> [!NOTE]
> Intermediate and terminal methods must be invoked within the query function.

Example 3. Use the fluent API to get a projected `Page`, ordered by `lastname`

```java
Page<CustomerProjection> page = repository.findBy(example,
    q -> q.as(CustomerProjection.class)
          .page(PageRequest.of(0, 20, Sort.by("lastname")))
);
```

Example 4. Use the fluent API to get the last of potentially many results, ordered by `lastname`

```java
Optional<Customer> match = repository.findBy(example,
    q -> q.sortBy(Sort.by("lastname").descending())
          .first()
);
```

---

<a id="value-expressions"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/value-expressions.html -->

<!-- page_index: 19 -->

# Value Expressions Fundamentals

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="value-expressions--page-title"></a>
<a id="value-expressions--value-expressions-fundamentals"></a>

# Value Expressions Fundamentals

Value Expressions are a combination of [Spring Expression Language (SpEL)](https://docs.spring.io/spring-framework/reference/7.0/core/expressions.html) and [Property Placeholder Resolution](https://docs.spring.io/spring-framework/reference/7.0/core/beans/annotation-config/value-annotations.html).
They combine powerful evaluation of programmatic expressions with the simplicity to resort to property-placeholder resolution to obtain values from the `Environment` such as configuration properties.

Expressions are expected to be defined by a trusted input such as an annotation value and not to be determined from user input.

<a id="value-expressions--_scope"></a>
<a id="value-expressions--scope"></a>

## Scope

Value Expressions are used in contexts across annotations.
Spring Data offers Value Expression evaluation in two main contexts:

- **Mapping Model Annotations**: such as `@Document`, `@Field`, `@Value` and other annotations in Spring Data modules that ship with their own mapping models respective Entity Readers such as MongoDB, Elasticsearch, Cassandra, Neo4j.
  Modules that build on libraries providing their own mapping models (JPA, LDAP) do not support Value Expressions in mapping annotations.

  The following code demonstrates how to use expressions in the context of mapping model annotations.

  Example 1. `@Document` Annotation Usage


```java
@Document("orders-#{tenantService.getOrderCollection()}-${tenant-config.suffix}")
class Order {
  // …
}
```

- **Repository Query Methods**: primarily through `@Query`.

  The following code demonstrates how to use expressions in the context of repository query methods.

  Example 2. `@Query` Annotation Usage


```java
class OrderRepository extends Repository<Order, String> {

  @Query("select u from User u where u.tenant = ?${spring.application.name:unknown} and u.firstname like %?#{escape([0])}% escape ?#{escapeCharacter()}")
  List<Order> findContainingEscaped(String namePart);
}
```

> [!NOTE]
> Consult your module’s documentation to determine the actual parameter by-name/by-index binding syntax.
> Typically, expressions are prefixed with `:#{…}`/`:${…}` or `?#{…}`/`?${…}`.

<a id="value-expressions--_expression_syntax"></a>
<a id="value-expressions--expression-syntax"></a>

## Expression Syntax

Value Expressions can be defined from a sole SpEL Expression, a Property Placeholder or a composite expression mixing various expressions including literals.

Example 3. Expression Examples

```none
#{tenantService.getOrderCollection()}                          (1)
#{(1+1) + '-hello-world'}                                      (2)
${tenant-config.suffix}                                        (3)
orders-${tenant-config.suffix}                                 (4)
#{tenantService.getOrderCollection()}-${tenant-config.suffix}  (5)
```

| **1** | Value Expression using a single SpEL Expression. |
| --- | --- |
| **2** | Value Expression using a static SpEL Expression evaluating to `2-hello-world`. |
| **3** | Value Expression using a single Property Placeholder. |
| **4** | Composite expression comprised of the literal `orders-` and the Property Placeholder `${tenant-config.suffix}`. |
| **5** | Composite expression using SpEL, Property Placeholders and literals. |

> [!NOTE]
> Using value expressions introduces a lot of flexibility to your code.
> Doing so requires evaluation of the expression on each usage and, therefore, value expression evaluation has an impact on the performance profile.

[Spring Expression Language (SpEL)](https://docs.spring.io/spring-framework/reference/7.0/core/expressions/language-ref.html) and [Property Placeholder Resolution](https://docs.spring.io/spring-framework/reference/7.0/core/beans/annotation-config/value-annotations.html) explain the syntax and capabilities of SpEL and Property Placeholders in detail.

<a id="value-expressions--valueexpressions.api"></a>
<a id="value-expressions--parsing-and-evaluation"></a>

## Parsing and Evaluation

Value Expressions are parsed by the `ValueExpressionParser` API.
Instances of `ValueExpression` are thread-safe and can be cached for later use to avoid repeated parsing.

The following example shows the Value Expression API usage:

Parsing and Evaluation

- Java
- Kotlin

```java
ValueParserConfiguration configuration = SpelExpressionParser::new;
ValueEvaluationContext context = ValueEvaluationContext.of(environment, evaluationContext);

ValueExpressionParser parser = ValueExpressionParser.create(configuration);
ValueExpression expression = parser.parse("Hello, World");
Object result = expression.evaluate(context);
```

```kotlin
val configuration = ValueParserConfiguration { SpelExpressionParser() }
val context = ValueEvaluationContext.of(environment, evaluationContext)

val parser = ValueExpressionParser.create(configuration)
val expression: ValueExpression = parser.parse("Hello, World")
val result: Any = expression.evaluate(context)
```

<a id="value-expressions--valueexpressions.spel"></a>
<a id="value-expressions--spel-expressions"></a>

## SpEL Expressions

[SpEL Expressions](https://docs.spring.io/spring-framework/reference/7.0/core/expressions.html) follow the Template style where the expression is expected to be enclosed within the `#{…}` format.
Expressions are evaluated using an `EvaluationContext` that is provided by `EvaluationContextProvider`.
The context itself is a powerful `StandardEvaluationContext` allowing a wide range of operations, access to static types and context extensions.

> [!NOTE]
> Make sure to parse and evaluate only expressions from trusted sources such as annotations.
> Accepting user-provided expressions can create an entry path to exploit the application context and your system resulting in a potential security vulnerability.

<a id="value-expressions--_extending_the_evaluation_context"></a>
<a id="value-expressions--extending-the-evaluation-context"></a>

### Extending the Evaluation Context

`EvaluationContextProvider` and its reactive variant `ReactiveEvaluationContextProvider` provide access to an `EvaluationContext`.
`ExtensionAwareEvaluationContextProvider` and its reactive variant `ReactiveExtensionAwareEvaluationContextProvider` are default implementations that determine context extensions from an application context, specifically `ListableBeanFactory`.

Extensions implement either `EvaluationContextExtension` or `ReactiveEvaluationContextExtension` to hydrate an `EvaluationContext` with: a root object, named properties, and functions (top-level methods).

The following example shows a context extension that provides a root object, properties, functions and an aliased function.

Implementing a `EvaluationContextExtension`

- Java
- Kotlin

```java
@Component public class MyExtension implements EvaluationContextExtension {
@Override public String getExtensionId() {return "my-extension";}
@Override public Object getRootObject() {return new CustomExtensionRootObject();}
@Override public Map<String, Object> getProperties() {
Map<String, Object> properties = new HashMap<>();
properties.put("key", "Hello");
return properties;}
@Override public Map<String, Function> getFunctions() {
Map<String, Function> functions = new HashMap<>();
try {functions.put("aliasedMethod", new Function(getClass().getMethod("extensionMethod"))); return functions; } catch (Exception o_O) {throw new RuntimeException(o_O);}}
public static String extensionMethod() {return "Hello World";}
public static int add(int i1, int i2) {return i1 + i2;}
}
public class CustomExtensionRootObject {
public boolean rootObjectInstanceMethod() {return true;}
}
```

```kotlin
@Component class MyExtension : EvaluationContextExtension {
override fun getExtensionId(): String {return "my-extension"}
override fun getRootObject(): Any? {return CustomExtensionRootObject()}
override fun getProperties(): Map<String, Any> {val properties: MutableMap<String, Any> = HashMap()
properties["key"] = "Hello"
return properties}
override fun getFunctions(): Map<String, Function> {val functions: MutableMap<String, Function> = HashMap()
try {functions["aliasedMethod"] = Function(javaClass.getMethod("extensionMethod")) return functions } catch (o_O: Exception) {throw RuntimeException(o_O)}}
companion object {fun extensionMethod(): String {return "Hello World"}
fun add(i1: Int, i2: Int): Int {return i1 + i2}}}
class CustomExtensionRootObject {fun rootObjectInstanceMethod(): Boolean {return true}}
```

Once the above shown extension is registered, you can use its exported methods, properties and root object to evaluate SpEL expressions:

Example 4. Expression Evaluation Examples

```none
#{add(1, 2)}                                             (1)
#{extensionMethod()}                                     (2)
#{aliasedMethod()}                                       (3)
#{key}                                                   (4)
#{rootObjectInstanceMethod()}                            (5)
```

**1**

Invoke the method `add` declared by `MyExtension` resulting in `3` as the method adds both numeric parameters and returns the sum.

**2**

Invoke the method `extensionMethod` declared by `MyExtension` resulting in `Hello World`.

**3**

Invoke the method `aliasedMethod`.
The method is exposed as function and redirects into the method `extensionMethod` declared by `MyExtension` resulting in `Hello World`.

**4**

Evaluate the `key` property resulting in `Hello`.

**5**

Invoke the method `rootObjectInstanceMethod` on the root object instance `CustomExtensionRootObject`.

You can find real-life context extensions at [`SecurityEvaluationContextExtension`](https://github.com/spring-projects/spring-security/blob/main/data/src/main/java/org/springframework/security/data/repository/query/SecurityEvaluationContextExtension.java).

<a id="value-expressions--valueexpressions.property-placeholders"></a>
<a id="value-expressions--property-placeholders"></a>

## Property Placeholders

Property placeholders following the form `${…}` refer to properties provided typically by a `PropertySource` through `Environment`.
Properties are useful to resolve against system properties, application configuration files, environment configuration or property sources contributed by secret management systems.
You can find more details on the property placeholders in [Spring Framework’s documentation on `@Value` usage](https://docs.spring.io/spring-framework/reference/7.0/core/beans/annotation-config/value-annotations.html#page-title).

---

<a id="property-paths"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/property-paths.html -->

<!-- page_index: 20 -->

# Property Paths

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="property-paths--page-title"></a>
<a id="property-paths--property-paths"></a>

# Property Paths

This chapter covers the concept of property paths.
Property paths are a form of navigation through domain classes to apply certain aspects in the context of interacting with the model.
Application code provides property paths to data access components to express intents such as selection of properties within a query, forming predicates, or applying sorting.
A property path originates from its owning type and can consist of one to many segments.

> [!TIP]
> Following domain-driven design principles the classes that form the backbone of your persistent domain model and that are accessed through Spring Data are called entities.
> An entry point to the object graph is called aggregate root.
>
> Understanding how to navigate and reference these properties is essential for working with repositories and query operations.

<a id="property-paths--property-path-overview"></a>

## Property Path Overview

Property paths provide a simple, text-based mechanism to navigate domain model properties.
This section introduces the fundamentals of property path navigation and demonstrates trade-offs between string-based and type-safe approaches.

Domain model example

- Java
- Kotlin

```java
class Person {
  String firstname, lastname;
  int age;
  Address address;
  List<Address> previousAddresses;

  String getFirstname() { … } // other property accessors omitted for brevity

}

class Address {
  String city, street;

  // accessors omitted for brevity

}
```

```kotlin
class Person {
  var firstname: String? = null
  var lastname: String? = null
  var age: Int = 0
  var address: Address? = null
  var previousAddresses: List<Address> = emptyList()
}

class Address {
  var city: String? = null
  var street: String? = null
}
```

Property paths use dot-notation to express property references throughout Spring Data operations, such as sorting and filtering:

Dot-notation property references

```java
Sort.by("firstname", "address.city")
```

A property path consists of one or more segments separated by a dot (`.`).
Methods accepting property paths support single-segment references (top-level properties) and multi-segment navigation unless otherwise indicated.

Collection and array properties support transparent traversal to their component type, enabling direct reference to nested properties:

```
Sort.by("address.city")             (1)

Sort.by("previousAddresses")        (2)

Sort.by("previousAddresses.city")   (3)
```

| **1** | Navigate from the top-level `address` property to the `city` field. |
| --- | --- |
| **2** | Reference the entire `previousAddresses` collection (supported by certain technologies for collection-based sorting). |
| **3** | Navigate through the collection to sort by the `city` field of each address. |

String-based property paths offer simplicity and can be broadly applied but there are tradeoffs to consider:

- **Flexibility**: Property paths are flexible and can be constructed from constant string, configuration or as result of user input.
- **Untyped**: String paths do not carry compile-time type information.
  Typed as textual content they do not have a dependency on the underlying domain type.
- **Refactoring risk**: Renaming domain properties requires often manual updates to string literals; IDEs cannot reliably track these references.

To improve refactoring safety and type consistency, prefer type-safe property references using method references.
This approach associates property paths with compile-time type information and enables compiler validation and IDE-driven refactoring.
See [Type-safe Property-References](#property-paths--type-safe-property-references) for details.

> [!NOTE]
> For implementation details, refer to [Property Path Internals](#property-paths--property-path-internals) for more information.

<a id="property-paths--property-path-internals"></a>

### Property Path Internals

The [`org.springframework.data.core`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/core/package-summary.html) package is the basis for Spring Data’s navigation across domain classes.
The [`TypeInformation`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/core/TypeInformation.html) interface provides type introspection capable of resolving the type of a property. [`PropertyPath`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/core/PropertyPath.html) represents a textual navigation path through a domain class.

Together they provide:

- Generic type resolution and introspection
- Property path creation and validation
- Actual type resolution for complex properties such as collections and maps

<a id="property-paths--type-safe-property-references"></a>

## Type-safe Property-References

Type-safe property-references eliminate a common source of errors in data access code: Brittle, string-based property references.
This section explains how method references can be used to express refactoring-safe property paths.

While a property path is a simple representation of object navigation, String-based property paths are inherently fragile during refactoring as they can be easily missed with an increasing distance between the property definition and its usage.
Type-safe alternatives through [`TypedPropertyPath`](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/core/TypedPropertyPath.html) derive property paths from method references, enabling the compiler to validate property names and IDEs to support refactoring operations.

- Java
- Kotlin

```java
// Inline usage with Sort
Sort.by(Person::getFirstName, Person::getLastName);

// Composed navigation
Sort.by(TypedPropertyPath.of(Person::getAddress).then(Address::getCity),
            Person::getLastName);
```

```kotlin
// Inline usage with Sort
Sort.by(Person::firstName, Person::lastName)

// Composed navigation
Sort.by(Person::address / Address::city, Person::lastName)
```

Type-safe property paths integrate seamlessly with query abstractions and criteria builders, enabling declarative query construction without string-based property references.

Adopting type-safe property references aligns with modern Spring development principles.
Providing declarative, type-safe, and fluent APIs leads to simpler reasoning about data access eliminating an entire category of potential bugs through IDE refactoring support and early feedback on invalid properties by the compiler.

Lambda introspection is cached for efficiency enabling repeatable use.
The JVM reuses static lambda instances contributing to minimal overhead of one-time parsing.

You can use `TypedPropertyPath` on its own if you are looking for a type-safe variant which benefits from compiler validation and IDE support for cases that do not directly integrate with Spring Data APIs:

- Java
- Kotlin

```java
import static org.springframework.data.core.TypedPropertyPath.path;

// Static import variant
path(Person::getAddress)
                 .then(Address::getCity);

// Fluent composition
TypedPropertyPath.of(Person::getAddress)
                 .then(Address::getCity);
```

```kotlin
// Kotlin API
TypedPropertyPath.of(Person::address / Address::city)

// as extension function
(Person::address / Address::city).toPath()
```

<a id="property-paths--type-safe-property-references-recommendations"></a>
<a id="property-paths--type-safe-property-reference-api-recommendations"></a>

### Type-safe Property-Reference API Recommendations

When using (or building) APIs using type-safe property-references, consider the following recommendations:

- **Use method references**: Accept method references (e.g., `Person::getFirstName`) instead of strings to leverage compile-time validation and IDE refactoring support.
  Method references are preferred as they share similar representations with both Java and Kotlin.
  Additionally, method references provide a better performance baseline compared to lambdas due to their simpler representation.
- **Leverage the `T` type of `TypedPropertyPath`**: Whenever accepting a typed property path, consider using the generic type `T` of `TypedPropertyPath<T, P>`.
  Limiting property paths to a specific domain type that is used within the current operation reduces the potential of using unintended properties from other types.
  Whenever accepting or providing multiple property paths, consider using `TypedPropertyPath<T, ?>` to allow for properties within the context of the owning type `T` to limit property paths to a common owning type.

> [!NOTE]
> Graal Native Image compilation requires reachability metadata for serializable `TypedPropertyPath` lambdas.
> Spring Data ships a built-in [feature](https://www.graalvm.org/sdk/javadoc/org/graalvm/nativeimage/hosted/Feature.html) through `org.springframework.data.core.TypedPropertyPathFeature`.
> The feature is auto-activated and registers required serialization- and reflection metadata for lambda parsing and referenced reflective members (fields and methods).
> Note also, when using lambda expressions instead of method references you will have to include the Java source code of the class containing the lambda expression in the native image configuration yourself.

---

<a id="auditing"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/auditing.html -->

<!-- page_index: 21 -->

# Auditing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="auditing--page-title"></a>
<a id="auditing--auditing"></a>

# Auditing

<a id="auditing--auditing.basics"></a>
<a id="auditing--basics"></a>

## Basics

Spring Data provides sophisticated support to transparently keep track of who created or changed an entity and when the change happened.
To benefit from that functionality, you have to equip your entity classes with auditing metadata that can be defined either using annotations or by implementing an interface.
Additionally, auditing has to be enabled either through Annotation configuration or XML configuration to register the required infrastructure components.
Please refer to the store-specific section for configuration samples.

> [!NOTE]
> Applications that only track creation and modification dates are not required to make their entities implement [`AuditorAware`](#auditing--auditing.auditor-aware).

<a id="auditing--auditing.annotations"></a>
<a id="auditing--annotation-based-auditing-metadata"></a>

### Annotation-based Auditing Metadata

We provide `@CreatedBy` and `@LastModifiedBy` to capture the user who created or modified the entity as well as `@CreatedDate` and `@LastModifiedDate` to capture when the change happened.

An audited entity

```java
class Customer {

  @CreatedBy
  private User user;

  @CreatedDate
  private Instant createdDate;

  // … further properties omitted
}
```

As you can see, the annotations can be applied selectively, depending on which information you want to capture.
The annotations, indicating to capture when changes are made, can be used on properties of type JDK8 date and time types, `long`, `Long`, and legacy Java `Date` and `Calendar`.

The time giving instance is provided by a `org.springframework.data.auditing.DateTimeProvider`.
By default this is a `CurrentDateTimeProvider`.
This can be changed via the `dateTimeProviderRef` attribute when enabling auditing, or a dedicated `AuditingHandler` or `DateTimeProvider` bean being present in the `ApplicationContext`.

Auditing metadata does not necessarily need to live in the root level entity but can be added to an embedded one (depending on the actual store in use), as shown in the snippet below.

Audit metadata in embedded entity

```java
class Customer {

  private AuditMetadata auditingMetadata;

  // … further properties omitted
}

class AuditMetadata {

  @CreatedBy
  private User user;

  @CreatedDate
  private Instant createdDate;

}
```

<a id="auditing--auditing.interfaces"></a>
<a id="auditing--interface-based-auditing-metadata"></a>

### Interface-based Auditing Metadata

In case you do not want to use annotations to define auditing metadata, you can let your domain class implement the `Auditable` interface. It exposes setter methods for all of the auditing properties.

<a id="auditing--auditing.auditor-aware"></a>
<a id="auditing--auditoraware"></a>

### `AuditorAware`

In case you use either `@CreatedBy` or `@LastModifiedBy`, the auditing infrastructure somehow needs to become aware of the current principal. To do so, we provide an `AuditorAware<T>` SPI interface that you have to implement to tell the infrastructure who the current user or system interacting with the application is. The generic type `T` defines what type the properties annotated with `@CreatedBy` or `@LastModifiedBy` have to be.

The following example shows an implementation of the interface that uses Spring Security’s `Authentication` object:

Implementation of `AuditorAware` based on Spring Security

```java
class SpringSecurityAuditorAware implements AuditorAware<User> {

  @Override
  public Optional<User> getCurrentAuditor() {

    return Optional.ofNullable(SecurityContextHolder.getContext())
            .map(SecurityContext::getAuthentication)
            .filter(Authentication::isAuthenticated)
            .map(Authentication::getPrincipal)
            .map(User.class::cast);
  }
}
```

The implementation accesses the `Authentication` object provided by Spring Security and looks up the custom `UserDetails` instance that you have created in your `UserDetailsService` implementation. We assume here that you are exposing the domain user through the `UserDetails` implementation but that, based on the `Authentication` found, you could also look it up from anywhere.

<a id="auditing--auditing.reactive-auditor-aware"></a>
<a id="auditing--reactiveauditoraware"></a>

### `ReactiveAuditorAware`

When using reactive infrastructure you might want to make use of contextual information to provide `@CreatedBy` or `@LastModifiedBy` information.
We provide an `ReactiveAuditorAware<T>` SPI interface that you have to implement to tell the infrastructure who the current user or system interacting with the application is. The generic type `T` defines what type the properties annotated with `@CreatedBy` or `@LastModifiedBy` have to be.

The following example shows an implementation of the interface that uses reactive Spring Security’s `Authentication` object:

Implementation of `ReactiveAuditorAware` based on Spring Security

```java
class SpringSecurityAuditorAware implements ReactiveAuditorAware<User> {

  @Override
  public Mono<User> getCurrentAuditor() {

    return ReactiveSecurityContextHolder.getContext()
                .mapNotNull(SecurityContext::getAuthentication)
                .filter(Authentication::isAuthenticated)
                .mapNotNull(Authentication::getPrincipal)
                .map(User.class::cast);
  }
}
```

The implementation accesses the `Authentication` object provided by Spring Security and looks up the custom `UserDetails` instance that you have created in your `UserDetailsService` implementation. We assume here that you are exposing the domain user through the `UserDetails` implementation but that, based on the `Authentication` found, you could also look it up from anywhere.

---

<a id="custom-conversions"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/custom-conversions.html -->

<!-- page_index: 22 -->

# Custom Conversions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="custom-conversions--page-title"></a>
<a id="custom-conversions--custom-conversions"></a>

# Custom Conversions

The following example of a Spring `Converter` implementation converts from a `String` to a custom `Email` value object:

```java
@ReadingConverter
public class EmailReadConverter implements Converter<String, Email> {

  public Email convert(String source) {
    return Email.valueOf(source);
  }
}
```

If you write a `Converter` whose source and target type are native types, we cannot determine whether we should consider it as a reading or a writing converter.
Registering the converter instance as both might lead to unwanted results.
For example, a `Converter<String, Long>` is ambiguous, although it probably does not make sense to try to convert all `String` instances into `Long` instances when writing.
To let you force the infrastructure to register a converter for only one way, we provide `@ReadingConverter` and `@WritingConverter` annotations to be used in the converter implementation.

Converters are subject to explicit registration as instances are not picked up from a classpath or container scan to avoid unwanted registration with a conversion service and the side effects resulting from such a registration. Converters are registered with `CustomConversions` as the central facility that allows registration and querying for registered converters based on source- and target type.

`CustomConversions` ships with a pre-defined set of converter registrations:

- JSR-310 Converters for conversion between `java.time`, `java.util.Date` and `String` types.

> [!NOTE]
> Default converters for local temporal types (e.g. `LocalDateTime` to `java.util.Date`) rely on system-default timezone settings to convert between those types. You can override the default converter, by registering your own converter.

<a id="custom-conversions--customconversions.converter-disambiguation"></a>
<a id="custom-conversions--converter-disambiguation"></a>

## Converter Disambiguation

Generally, we inspect the `Converter` implementations for the source and target types they convert from and to.
Depending on whether one of those is a type the underlying data access API can handle natively, we register the converter instance as a reading or a writing converter.
The following examples show a writing- and a read converter (note the difference is in the order of the qualifiers on `Converter`):

```java
// Write converter as only the target type is one that can be handled natively
class MyConverter implements Converter<Person, String> { … }

// Read converter as only the source type is one that can be handled natively
class MyConverter implements Converter<String, Person> { … }
```

---

<a id="entity-callbacks"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/entity-callbacks.html -->

<!-- page_index: 23 -->

# Entity Callbacks

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="entity-callbacks--page-title"></a>
<a id="entity-callbacks--entity-callbacks"></a>

# Entity Callbacks

The Spring Data infrastructure provides hooks for modifying an entity before and after certain methods are invoked.
Those so called `EntityCallback` instances provide a convenient way to check and potentially modify an entity in a callback fashioned style.
An `EntityCallback` looks pretty much like a specialized `ApplicationListener`.
Some Spring Data modules publish store specific events (such as `BeforeSaveEvent`) that allow modifying the given entity. In some cases, such as when working with immutable types, these events can cause trouble.
Also, event publishing relies on `ApplicationEventMulticaster`. If configuring that with an asynchronous `TaskExecutor` it can lead to unpredictable outcomes, as event processing can be forked onto a Thread.

Entity callbacks provide integration points with both synchronous and reactive APIs to guarantee in-order execution at well-defined checkpoints within the processing chain, returning a potentially modified entity or a reactive wrapper type.

Entity callbacks are typically separated by API type. This separation means that a synchronous API considers only synchronous entity callbacks and a reactive implementation considers only reactive entity callbacks.

> [!NOTE]
> The Entity Callback API has been introduced with Spring Data Commons 2.2. It is the recommended way of applying entity modifications.
> Existing store specific `ApplicationEvents` are still published **before** the invoking potentially registered `EntityCallback` instances.

<a id="entity-callbacks--entity-callbacks.implement"></a>
<a id="entity-callbacks--implementing-entity-callbacks"></a>

## Implementing Entity Callbacks

An `EntityCallback` is directly associated with its domain type through its generic type argument.
Each Spring Data module typically ships with a set of predefined `EntityCallback` interfaces covering the entity lifecycle.

Anatomy of an `EntityCallback`

```java
@FunctionalInterface public interface BeforeSaveCallback<T> extends EntityCallback<T> {
/** * Entity callback method invoked before a domain object is saved.* Can return either the same or a modified instance.* * @return the domain object to be persisted.*/ (1) T onBeforeSave(T entity, (2) String collection); (3)}
```

**1**

`BeforeSaveCallback` specific method to be called before an entity is saved. Returns a potentially modified instance.

**2**

The entity right before persisting.

**3**

A number of store specific arguments like the *collection* the entity is persisted to.

Anatomy of a reactive `EntityCallback`

```java
@FunctionalInterface public interface ReactiveBeforeSaveCallback<T> extends EntityCallback<T> {
/** * Entity callback method invoked on subscription, before a domain object is saved.* The returned Publisher can emit either the same or a modified instance.* * @return Publisher emitting the domain object to be persisted.*/ (1) Publisher<T> onBeforeSave(T entity, (2) String collection); (3)}
```

**1**

`BeforeSaveCallback` specific method to be called on subscription, before an entity is saved. Emits a potentially modified instance.

**2**

The entity right before persisting.

**3**

A number of store specific arguments like the *collection* the entity is persisted to.

> [!NOTE]
> Optional entity callback parameters are defined by the implementing Spring Data module and inferred from call site of `EntityCallback.callback()`.

Implement the interface suiting your application needs like shown in the example below:

Example `BeforeSaveCallback`

```java
class DefaultingEntityCallback implements BeforeSaveCallback<Person>, Ordered {      (2)
@Override public Object onBeforeSave(Person entity, String collection) {                   (1)
if("user".equals(collection)) {return …;}
return …;}
@Override public int getOrder() {return 100;                                                                  (2)}}
```

**1**

Callback implementation according to your requirements.

**2**

Potentially order the entity callback if multiple ones for the same domain type exist. Ordering follows lowest precedence.

<a id="entity-callbacks--entity-callbacks.register"></a>
<a id="entity-callbacks--registering-entity-callbacks"></a>

## Registering Entity Callbacks

`EntityCallback` beans are picked up by the store specific implementations in case they are registered in the `ApplicationContext`.
Most template APIs already implement `ApplicationContextAware` and therefore have access to the `ApplicationContext`

The following example explains a collection of valid entity callback registrations:

Example `EntityCallback` Bean registration

```java
@Order(1)                                                           (1) @Component class First implements BeforeSaveCallback<Person> {
@Override public Person onBeforeSave(Person person) {return // ...}}
@Component class DefaultingEntityCallback implements BeforeSaveCallback<Person>,Ordered { (2)
@Override public Object onBeforeSave(Person entity, String collection) {// ...}
@Override public int getOrder() {return 100;                                                  (2)}}
@Configuration public class EntityCallbackConfiguration {
@Bean BeforeSaveCallback<Person> unorderedLambdaReceiverCallback() {   (3) return (BeforeSaveCallback<Person>) it -> // ...}}
@Component class UserCallbacks implements BeforeConvertCallback<User>,BeforeSaveCallback<User> {   (4)
@Override public Person onBeforeConvert(User user) {return // ...}
@Override public Person onBeforeSave(User user) {return // ...}}
```

| **1** | `BeforeSaveCallback` receiving its order from the `@Order` annotation. |
| --- | --- |
| **2** | `BeforeSaveCallback` receiving its order via the `Ordered` interface implementation. |
| **3** | `BeforeSaveCallback` using a lambda expression. Unordered by default and invoked last. Note that callbacks implemented by a lambda expression do not expose typing information hence invoking these with a non-assignable entity affects the callback throughput. Use a `class` or `enum` to enable type filtering for the callback bean. |
| **4** | Combine multiple entity callback interfaces in a single implementation class. |

---

<a id="is-new-state-detection"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/is-new-state-detection.html -->

<!-- page_index: 24 -->

# Entity State Detection Strategies

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="is-new-state-detection--page-title"></a>
<a id="is-new-state-detection--entity-state-detection-strategies"></a>

# Entity State Detection Strategies

The following table describes the strategies that Spring Data offers for detecting whether an entity is new:

`@Id`-Property inspection (the default)

By default, Spring Data inspects the identifier property of the given entity.
If the identifier property is `null` or `0` in case of primitive types, then the entity is assumed to be new.
Otherwise, it is assumed to not be new.

`@Version`-Property inspection

If a property annotated with `@Version` is present and `null`, or in case of a version property of primitive type `0` the entity is considered new.
If the version property is present but has a different value, the entity is considered to not be new.
If no version property is present Spring Data falls back to inspection of the identifier property.

Implementing `Persistable`

If an entity implements `Persistable`, Spring Data delegates the new detection to the `isNew(…)` method of the entity.
See the [Javadoc](https://docs.spring.io/spring-data/commons/reference/4.1.0/api/java/org/springframework/data/domain/Persistable.html) for details.

*Note: Properties of `Persistable` will get detected and persisted if you use `AccessType.PROPERTY`.
To avoid that, use `@Transient`.*

---

<a id="aot"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/aot.html -->

<!-- page_index: 25 -->

# Ahead of Time Optimizations

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="aot--page-title"></a>
<a id="aot--ahead-of-time-optimizations"></a>

# Ahead of Time Optimizations

This chapter covers Spring Data’s Ahead of Time (AOT) optimizations that build upon [Spring’s Ahead of Time Optimizations](https://docs.spring.io/spring-framework/reference/7.0/core/aot.html).

<a id="aot--aot.bestpractices"></a>
<a id="aot--best-practices"></a>

## Best Practices

<a id="aot--_annotate_your_domain_types"></a>
<a id="aot--annotate-your-domain-types"></a>

### Annotate your Domain Types

During application startup, Spring scans the classpath for domain classes for early processing of entities.
By annotating your domain types with Spring Data Store specific `@Table`, `@Document` or `@Entity` annotations you can aid initial entity scanning and ensure that those types are registered with `ManagedTypes` for Runtime Hints.
Classpath scanning is not possible in native image arrangements and so Spring has to use `ManagedTypes` for the initial entity set.

<a id="aot--aot.code-gen"></a>
<a id="aot--ahead-of-time-code-generation"></a>

## Ahead of Time Code Generation

Ahead of time code generation is not limited to usage with GraalVM Native Image but also offers benefits when working with regular deployments and can help optimize startup performance on the jvm.

> [!NOTE]
> With AOT optimizations some decisions (like database dialects for example) will be frozen at build time and get included as is in the application setup.

If Ahead of Time compilation is enabled Spring Data can (depending on the actual Module in use) contribute several components during the AOT phase of your build.

- Bytecode for generated Type/Property Accessors
- Sourcecode for the defined Repository Interfaces
- Repository Metadata in JSON format

Each of the above is enabled by default.
However, users may fine-tune the configuration with the following options.

`spring.aot.data.accessors.enabled`

Boolean flag to control contribution of Bytecode for generated Type/Property Accessors

`spring.aot.data.accessors.include`

Comma separated list of FQCN for which to contribute Bytecode for generated Type/Property Accessors.
Ant-style include patterns matching package names (e.g. `example.springdata.**`) or type names inclusion.
If a type is matched by an inclusion and an exclusion, the inclusion wins and the type is considered included.

`spring.aot.data.accessors.exclude`

Comma separated list of FQCN for which to skip contribution of Bytecode for generated Type/Property Accessors.
Ant-style exclude patterns matching package names (e.g. `example.springdata.**`) or type names exclusion.
If a type is matched by an inclusion and an exclusion, the inclusion wins and the type is considered included.

`spring.aot.repositories.enabled`

Boolean flag to control contribution of Source Code for Repository Interfaces

`spring.aot.[module-name].repositories.enabled`

Boolean flag to control contribution of Source Code for Repository Interfaces for a certain module (e.g. `cassandra`, `jdbc`, `jpa`, `mongodb`)

`spring.aot.repositories.metadata.enabled`

Boolean flag to control contribution of JSON repository metadata containing query methods and actual query strings.
Requires `spring.aot.repositories.enabled` to be enabled.

<a id="aot--aot.repositories"></a>
<a id="aot--ahead-of-time-repositories"></a>

## Ahead of Time Repositories

> [!NOTE]
> Ahead of Time repositories are only available for imperative (non reactive) repository interfaces of certain modules.
> The criteria identifying eligible query methods varies between the implementing modules.

AOT Repositories are an extension to AOT processing by pre-generating eligible query method implementations.
Query methods are opaque to developers regarding their underlying queries being executed in a query method call.
AOT repositories contribute query method implementations based on derived, annotated, and named queries that are known at build-time.
This optimization moves query method processing from runtime to build-time, which can lead to a significant performance improvement as query methods do not need to be analyzed reflectively upon each application start.

The resulting AOT repository fragment follows the naming scheme of `<Repository FQCN>Impl__AotRepository` and is placed in the same package as the repository interface.

> [!WARNING]
> Consider AOT repository classes an internal optimization.
> Do not use them directly in your code as generation and implementation details may change in future releases.

<a id="aot--aot.repositories.json"></a>
<a id="aot--repository-metadata"></a>

### Repository Metadata

AOT processing introspects query methods and collects metadata about repository queries.
Spring Data stores this metadata in JSON files that are named after the source repository within the same package.
Repository JSON Metadata contains details about queries and fragments.
An example for the following repository is shown below:

- Metadata
- Repository

```json
{"name": "example.springdata.UserRepository","module": "JDBC","type": "IMPERATIVE","methods": [{"name": "findBy","signature": "public abstract java.util.List<example.springdata.User> example.springdata.UserRepository.findBy()","query": {"query": "SELECT * FROM User"} },{"name": "findByLastnameStartingWith","signature": "public abstract org.springframework.data.domain.Page<example.springdata.User> example.springdata.UserRepository.findByLastnameStartingWith(java.lang.String,org.springframework.data.domain.Pageable)","query": {"query": "SELECT * FROM User u WHERE lastname LIKE :lastname","count-query": "SELECT COUNT(*) FROM User WHERE lastname LIKE :lastname"} },{"name": "findByEmailAddress","signature": "public abstract example.springdata.User example.springdata.UserRepository.findByEmailAddress(java.lang.String)","query": {"query": "select * from User where emailAddress = ?1"} },
```

```java
interface UserRepository extends CrudRepository<User, Integer> {

  List<User> findBy();

  Page<User> findByLastnameStartingWith(String lastname, Pageable page);

  @Query("select * from User where emailAddress = ?1")
  User findByEmailAddress(String username);
}
```

> [!NOTE]
> Creating JSON metadata can be controlled via the `spring.aot.repositories.metadata.enabled` flag.

<a id="aot--aot.hints"></a>
<a id="aot--native-image-runtime-hints"></a>

> [!NOTE]
> ## Native Image Runtime Hints

Running an application as a native image requires additional information compared to a regular JVM runtime.
Spring Data contributes [Runtime Hints](https://docs.spring.io/spring-framework/reference/7.0/core/aot.html#aot.hints) during AOT processing for native image usage.
These are in particular hints for:

- Auditing
- `ManagedTypes` to capture the outcome of class-path scans
- Repositories

  - Reflection hints for entities, return types, and Spring Data annotations
  - Repository fragments
  - Querydsl `Q` classes
  - Kotlin Coroutine support
- Web support (Jackson Hints for `PagedModel`)

---

<a id="kotlin"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/kotlin.html -->

<!-- page_index: 26 -->

# Kotlin Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kotlin--page-title"></a>
<a id="kotlin--kotlin-support"></a>

# Kotlin Support

[Kotlin](https://kotlinlang.org) is a statically typed language that targets the JVM (and other platforms) which allows writing concise and elegant code while providing excellent [interoperability](https://kotlinlang.org/docs/reference/java-interop.html) with existing libraries written in Java.

Spring Data provides first-class support for Kotlin and lets developers write Kotlin applications almost as if Spring Data was a Kotlin native framework.

The easiest way to build a Spring application with Kotlin is to leverage Spring Boot and its [dedicated Kotlin support](https://docs.spring.io/spring-boot/reference/features/kotlin.html).
This comprehensive [tutorial](https://spring.io/guides/tutorials/spring-boot-kotlin/) will teach you how to build Spring Boot applications with Kotlin using [start.spring.io](https://start.spring.io/#!language=kotlin&type=gradle-project).

<a id="kotlin--section-summary"></a>

## Section Summary

- [Requirements](#kotlin-requirements)
- [Null Safety](#kotlin-null-safety)
- [Object Mapping](#kotlin-object-mapping)
- [Extensions](#kotlin-extensions)
- [Coroutines](#kotlin-coroutines)

---

<a id="kotlin-requirements"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/kotlin/requirements.html -->

<!-- page_index: 27 -->

<a id="kotlin-requirements--page-title"></a>
<a id="kotlin-requirements--requirements"></a>

# Requirements

Spring Data supports Kotlin 1.9 and above and requires `kotlin-stdlib` and `kotlin-reflect` to be present on the classpath.
Those are provided by default if you bootstrap a Kotlin project via [start.spring.io](https://start.spring.io/#!language=kotlin&type=gradle-project).

---

<a id="kotlin-null-safety"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/kotlin/null-safety.html -->

<!-- page_index: 28 -->

# Null Safety

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kotlin-null-safety--page-title"></a>
<a id="kotlin-null-safety--null-safety"></a>

# Null Safety

One of Kotlin’s key features is [null safety](https://kotlinlang.org/docs/null-safety.html), which cleanly deals with `null` values at compile time.
This makes applications safer through nullability declarations and the expression of “value or no value” semantics without paying the cost of wrappers, such as `Optional`.
(Kotlin allows using functional constructs with nullable values. See this [comprehensive guide to Kotlin null safety](https://www.baeldung.com/kotlin/null-safety).)

> [!NOTE]
> As of Spring Framework 7 and Spring Data 4, Spring Data uses [JSpecify](https://jspecify.dev/docs/start-here/) for nullability annotations.
> The earlier [JSR-305](https://jcp.org/en/jsr/detail?id=305)-based `org.springframework.lang` annotations are deprecated and should no longer be relied upon.
> See [Null Handling of Repository Methods](#repositories-null-handling) for the current recommended approach.

Although Java does not let you express null safety in its type system, the Spring Data API is annotated with JSpecify annotations.
By default, types from Java APIs used in Kotlin are recognized as [platform types](https://kotlinlang.org/docs/reference/java-interop.html#null-safety-and-platform-types), for which null checks are relaxed.
JSpecify annotations provide null safety for the whole Spring Data API to Kotlin developers, with the advantage of dealing with `null`-related issues at compile time.

See [Null Handling of Repository Methods](#repositories-null-handling) for details on how null safety applies to Spring Data repositories.

> [!NOTE]
> Generic type arguments, varargs, and array element nullability are not supported yet, but should be in an upcoming release.

---

<a id="kotlin-object-mapping"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/kotlin/object-mapping.html -->

<!-- page_index: 29 -->

<a id="kotlin-object-mapping--page-title"></a>
<a id="kotlin-object-mapping--object-mapping"></a>

# Object Mapping

See [Kotlin support](#object-mapping--mapping.kotlin) for details on how Kotlin objects are materialized.

---

<a id="kotlin-extensions"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/kotlin/extensions.html -->

<!-- page_index: 30 -->

# Extensions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kotlin-extensions--page-title"></a>
<a id="kotlin-extensions--extensions"></a>

# Extensions

Kotlin [extensions](https://kotlinlang.org/docs/reference/extensions.html) provide the ability to extend existing classes with additional functionality. Spring Data Kotlin APIs use these extensions to add new Kotlin-specific conveniences to existing Spring APIs.

> [!NOTE]
> Keep in mind that Kotlin extensions need to be imported to be used.
> Similar to static imports, an IDE should automatically suggest the import in most cases.

For example, [Kotlin reified type parameters](https://kotlinlang.org/docs/reference/inline-functions.html#reified-type-parameters) provide a workaround for JVM [generics type erasure](https://docs.oracle.com/javase/tutorial/java/generics/erasure.html), and Spring Data provides some extensions to take advantage of this feature.
This allows for a better Kotlin API.

---

<a id="kotlin-coroutines"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/kotlin/coroutines.html -->

<!-- page_index: 31 -->

# Coroutines

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kotlin-coroutines--page-title"></a>
<a id="kotlin-coroutines--coroutines"></a>

# Coroutines

Kotlin [Coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html) are instances of suspendable computations allowing to write non-blocking code imperatively.
On language side, `suspend` functions provides an abstraction for asynchronous operations while on library side [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) provides functions like [`async { }`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/async.html) and types like [`Flow`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html).

Spring Data modules provide support for Coroutines on the following scope:

- [Deferred](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-deferred/index.html) and [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) return values support in Kotlin extensions

<a id="kotlin-coroutines--kotlin.coroutines.dependencies"></a>
<a id="kotlin-coroutines--dependencies"></a>

## Dependencies

Coroutines support is enabled when `kotlinx-coroutines-core`, `kotlinx-coroutines-reactive` and `kotlinx-coroutines-reactor` dependencies are in the classpath:

Dependencies to add in Maven pom.xml

```xml
<dependency>
	<groupId>org.jetbrains.kotlinx</groupId>
	<artifactId>kotlinx-coroutines-core</artifactId>
</dependency>

<dependency>
	<groupId>org.jetbrains.kotlinx</groupId>
	<artifactId>kotlinx-coroutines-reactive</artifactId>
</dependency>

<dependency>
	<groupId>org.jetbrains.kotlinx</groupId>
	<artifactId>kotlinx-coroutines-reactor</artifactId>
</dependency>
```

> [!NOTE]
> Supported versions `1.7.0` and above.

<a id="kotlin-coroutines--kotlin.coroutines.reactive"></a>
<a id="kotlin-coroutines--how-reactive-translates-to-coroutines"></a>

## How Reactive translates to Coroutines?

For return values, the translation from Reactive to Coroutines APIs is the following:

- `fun handler(): Mono<Void>` becomes `suspend fun handler()`
- `fun handler(): Mono<T>` becomes `suspend fun handler(): T` or `suspend fun handler(): T?` depending on if the `Mono` can be empty or not (with the advantage of being more statically typed)
- `fun handler(): Flux<T>` becomes `fun handler(): Flow<T>`

[`Flow`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) is `Flux` equivalent in Coroutines world, suitable for hot or cold stream, finite or infinite streams, with the following main differences:

- `Flow` is push-based while `Flux` is push-pull hybrid
- Backpressure is implemented via suspending functions
- `Flow` has only a [single suspending `collect` method](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/collect.html) and operators are implemented as [extensions](https://kotlinlang.org/docs/reference/extensions.html)
- [Operators are easy to implement](https://github.com/Kotlin/kotlinx.coroutines/tree/master/kotlinx-coroutines-core/common/src/flow/operators) thanks to Coroutines
- Extensions allow adding custom operators to `Flow`
- Collect operations are suspending functions
- [`map` operator](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/map.html) supports asynchronous operation (no need for `flatMap`) since it takes a suspending function parameter

Read this blog post about [Going Reactive with Spring, Coroutines and Kotlin Flow](https://spring.io/blog/2019/04/12/going-reactive-with-spring-coroutines-and-kotlin-flow) for more details, including how to run code concurrently with Coroutines.

<a id="kotlin-coroutines--kotlin.coroutines.repositories"></a>
<a id="kotlin-coroutines--repositories"></a>

## Repositories

Here is an example of a Coroutines repository:

```kotlin
interface CoroutineRepository : CoroutineCrudRepository<User, String> {

    suspend fun findOne(id: String): User

    fun findByFirstname(firstname: String): Flow<User>

    suspend fun findAllByFirstname(id: String): List<User>
}
```

Coroutines repositories are built on reactive repositories to expose the non-blocking nature of data access through Kotlin’s Coroutines.
Methods on a Coroutines repository can be backed either by a query method or a custom implementation.
Invoking a custom implementation method propagates the Coroutines invocation to the actual implementation method if the custom method is `suspend`-able without requiring the implementation method to return a reactive type such as `Mono` or `Flux`.

Note that depending on the method declaration the coroutine context may or may not be available.
To retain access to the context, either declare your method using `suspend` or return a type that enables context propagation such as `Flow`.

- `suspend fun findOne(id: String): User`: Retrieve the data once and synchronously by suspending.
- `fun findByFirstname(firstname: String): Flow<User>`: Retrieve a stream of data.
  The `Flow` is created eagerly while data is fetched upon `Flow` interaction (`Flow.collect(…)`).
- `fun getUser(): User`: Retrieve data once **blocking the thread** and without context propagation.
  This should be avoided.

> [!NOTE]
> Coroutines repositories are only discovered when the repository extends the `CoroutineCrudRepository` interface.

---

<a id="repositories-namespace-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/namespace-reference.html -->

<!-- page_index: 32 -->

# Namespace reference

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-namespace-reference--page-title"></a>
<a id="repositories-namespace-reference--namespace-reference"></a>

# Namespace reference

<a id="repositories-namespace-reference--populator.namespace-dao-config"></a>
<a id="repositories-namespace-reference--the-repositories-element"></a>

## The `<repositories />` Element

The `<repositories />` element triggers the setup of the Spring Data repository infrastructure. The most important attribute is `base-package`, which defines the package to scan for Spring Data repository interfaces. See “[XML Configuration](#repositories-create-instances--repositories.create-instances.xml)”. The following table describes the attributes of the `<repositories />` element:

| Name | Description |
| --- | --- |
| `base-package` | Defines the package to be scanned for repository interfaces that extend `*Repository` (the actual interface is determined by the specific Spring Data module) in auto-detection mode. All packages below the configured package are scanned, too. Wildcards are allowed. |
| `repository-impl-postfix` | Defines the postfix to autodetect custom repository implementations. Classes whose names end with the configured postfix are considered as candidates. Defaults to `Impl`. |
| `query-lookup-strategy` | Determines the strategy to be used to create finder queries. See “[Query Lookup Strategies](#repositories-query-methods-details--repositories.query-methods.query-lookup-strategies)” for details. Defaults to `create-if-not-found`. |
| `named-queries-location` | Defines the location to search for a Properties file containing externally defined queries. |
| `consider-nested-repositories` | Whether nested repository interface definitions should be considered. Defaults to `false`. |

---

<a id="repositories-populator-namespace-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/populator-namespace-reference.html -->

<!-- page_index: 33 -->

<a id="repositories-populator-namespace-reference--page-title"></a>
<a id="repositories-populator-namespace-reference--populators-namespace-reference"></a>

# Populators namespace reference

<a id="repositories-populator-namespace-reference--namespace-dao-config"></a>
<a id="repositories-populator-namespace-reference--the-populator-element"></a>

## The <populator /> element

The `<populator />` element allows to populate a data store via the Spring Data repository infrastructure.[[1](#repositories-populator-namespace-reference--_footnotedef_1 "View footnote.")]

| Name | Description |
| --- | --- |
| `locations` | Where to find the files to read the objects from the repository shall be populated with. |

--
-

[1](#repositories-populator-namespace-reference--_footnoteref_1). see [XML Configuration](#repositories-create-instances--repositories.create-instances.xml)

---

<a id="repositories-query-keywords-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/query-keywords-reference.html -->

<!-- page_index: 34 -->

# Repository query keywords

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-keywords-reference--page-title"></a>
<a id="repositories-query-keywords-reference--repository-query-keywords"></a>

# Repository query keywords

<a id="repositories-query-keywords-reference--appendix.query.method.subject"></a>
<a id="repositories-query-keywords-reference--supported-query-method-subject-keywords"></a>

## Supported query method subject keywords

The following table lists the subject keywords generally supported by the Spring Data repository query derivation mechanism to express the predicate.
Consult the store-specific documentation for the exact list of supported keywords, because some keywords listed here might not be supported in a particular store.

| Keyword | Description |
| --- | --- |
| `find…By`, `read…By`, `get…By`, `query…By`, `search…By`, `stream…By` | General query method returning typically the repository type, a `Collection` or `Streamable` subtype or a result wrapper such as `Page`, `GeoResults` or any other store-specific result wrapper. Can be used as `findBy…`, `findMyDomainTypeBy…` or in combination with additional keywords. |
| `exists…By` | Exists projection, returning typically a `boolean` result. |
| `count…By` | Count projection returning a numeric result. |
| `delete…By`, `remove…By` | Delete query method returning either no result (`void`) or the delete count. |
| `…First<number>…`, `…Top<number>…` | Limit the query results to the first `<number>` of results. This keyword can occur in any place of the subject between `find` (and the other keywords) and `by`. |
| `…Distinct…` | Use a distinct query to return only unique results. Consult the store-specific documentation whether that feature is supported. This keyword can occur in any place of the subject between `find` (and the other keywords) and `by`. |

<a id="repositories-query-keywords-reference--appendix.query.method.reserved"></a>
<a id="repositories-query-keywords-reference--reserved-methods"></a>

## Reserved methods

The following table lists reserved methods that use predefined functionality (as defined in `CrudRepository`).
These methods are directly invoked on the backing (store-specific) implementation of the repository proxy.
See also “[Defining Query Methods](#repositories-query-methods-details--repositories.query-methods.reserved-methods)”.

`deleteAllById(Iterable<ID> identifiers)`

`deleteById(ID identifier)`

`existsById(ID identifier)`

`findAllById(Iterable<ID> identifiers)`

`findById(ID identifier)`

<a id="repositories-query-keywords-reference--appendix.query.method.predicate"></a>
<a id="repositories-query-keywords-reference--supported-query-method-predicate-keywords-and-modifiers"></a>

## Supported query method predicate keywords and modifiers

The following table lists the predicate keywords generally supported by the Spring Data repository query derivation mechanism.
However, consult the store-specific documentation for the exact list of supported keywords, because some keywords listed here might not be supported in a particular store.

| Logical keyword | Keyword expressions |
| --- | --- |
| `AND` | `And` |
| `OR` | `Or` |
| `AFTER` | `After`, `IsAfter` |
| `BEFORE` | `Before`, `IsBefore` |
| `CONTAINING` | `Containing`, `IsContaining`, `Contains` |
| `BETWEEN` | `Between`, `IsBetween` |
| `ENDING_WITH` | `EndingWith`, `IsEndingWith`, `EndsWith` |
| `EXISTS` | `Exists` |
| `FALSE` | `False`, `IsFalse` |
| `GREATER_THAN` | `GreaterThan`, `IsGreaterThan` |
| `GREATER_THAN_EQUALS` | `GreaterThanEqual`, `IsGreaterThanEqual` |
| `IN` | `In`, `IsIn` |
| `IS` | `Is`, `Equals`, (or no keyword) |
| `IS_EMPTY` | `IsEmpty`, `Empty` |
| `IS_NOT_EMPTY` | `IsNotEmpty`, `NotEmpty` |
| `IS_NOT_NULL` | `NotNull`, `IsNotNull` |
| `IS_NULL` | `Null`, `IsNull` |
| `LESS_THAN` | `LessThan`, `IsLessThan` |
| `LESS_THAN_EQUAL` | `LessThanEqual`, `IsLessThanEqual` |
| `LIKE` | `Like`, `IsLike` |
| `NEAR` | `Near`, `IsNear` |
| `NOT` | `Not`, `IsNot` |
| `NOT_IN` | `NotIn`, `IsNotIn` |
| `NOT_LIKE` | `NotLike`, `IsNotLike` |
| `REGEX` | `Regex`, `MatchesRegex`, `Matches` |
| `STARTING_WITH` | `StartingWith`, `IsStartingWith`, `StartsWith` |
| `TRUE` | `True`, `IsTrue` |
| `WITHIN` | `Within`, `IsWithin` |

In addition to filter predicates, the following list of modifiers is supported:

| Keyword | Description |
| --- | --- |
| `IgnoreCase`, `IgnoringCase` | Used with a predicate keyword for case-insensitive comparison. |
| `AllIgnoreCase`, `AllIgnoringCase` | Ignore case for all suitable properties. Used somewhere in the query method predicate. |
| `OrderBy…` | Specify a static sorting order followed by the property path and direction (e.g. `OrderByFirstnameAscLastnameDesc`). |

---

<a id="repositories-query-return-types-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/commons/reference/repositories/query-return-types-reference.html -->

<!-- page_index: 35 -->

# Repository query return types

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-return-types-reference--page-title"></a>
<a id="repositories-query-return-types-reference--repository-query-return-types"></a>

# Repository query return types

<a id="repositories-query-return-types-reference--appendix.query.return.types"></a>
<a id="repositories-query-return-types-reference--supported-query-return-types"></a>

## Supported Query Return Types

The following table lists the return types generally supported by Spring Data repositories.
However, consult the store-specific documentation for the exact list of supported return types, because some types listed here might not be supported in a particular store.

> [!NOTE]
> Geospatial types (such as `GeoResult`, `GeoResults`, and `GeoPage`) are available only for data stores that support geospatial queries.
> Some store modules may define their own result wrapper types.

| Return type | Description |
| --- | --- |
| `void` | Denotes no return value. |
| Primitives | Java primitives. |
| Wrapper types | Java wrapper types. |
| `T` | A unique entity. Expects the query method to return one result at most. If no result is found, `null` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Iterator<T>` | An `Iterator`. |
| `Collection<T>` | A `Collection`. |
| `List<T>` | A `List`. |
| `Optional<T>` | A Java `Optional` or Guava `Optional`. Expects the query method to return one result at most. If no result is found, `Optional.empty()` or `Optional.absent()` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Option<T>` | Either a Scala or Vavr `Option` type. Semantically the same behavior as Java’s `Optional`, described earlier. |
| `Stream<T>` | A Java `Stream`. |
| `Streamable<T>` | A convenience extension of `Iterable` that directly exposes methods to stream, map and filter results, concatenate them etc. |
| Types that implement `Streamable` and take a `Streamable` constructor or factory method argument | Types that expose a constructor or `….of(…)`/`….valueOf(…)` factory method taking a `Streamable` as argument. See [Returning Custom Streamable Wrapper Types](#repositories-query-methods-details--repositories.collections-and-iterables.streamable-wrapper) for details. |
| Vavr `Seq`, `List`, `Map`, `Set` | Vavr collection types. See [Support for Vavr Collections](#repositories-query-methods-details--repositories.collections-and-iterables.vavr) for details. |
| `Future<T>` | A `Future`. Expects a method to be annotated with `@Async` and requires Spring’s asynchronous method execution capability to be enabled. |
| `CompletableFuture<T>` | A `CompletableFuture`. Expects a method to be annotated with `@Async` and requires Spring’s asynchronous method execution capability to be enabled. |
| `Slice<T>` | A sized chunk of data with an indication of whether there is more data available. Requires a `Pageable` method parameter. |
| `Page<T>` | A `Slice` with additional information, such as the total number of results. Requires a `Pageable` method parameter. |
| `Window<T>` | A `Window` of results obtained from a scroll query. Provides `ScrollPosition` to issue the next scroll query. Requires a `ScrollPosition` method parameter. |
| `GeoResult<T>` | A result entry with additional information, such as the distance to a reference location. |
| `GeoResults<T>` | A list of `GeoResult<T>` with additional information, such as the average distance to a reference location. |
| `GeoPage<T>` | A `Page` with `GeoResult<T>`, such as the average distance to a reference location. |
| `SearchResult<T>` | A result entry with additional information, such as the score in relation to the reference search term. |
| `SearchResults<T>` | A list of `SearchResult<T>`. |
| `Mono<T>` | A Project Reactor `Mono` emitting zero or one element using reactive repositories. Expects the query method to return one result at most. If no result is found, `Mono.empty()` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Flux<T>` | A Project Reactor `Flux` emitting zero, one, or many elements using reactive repositories. Queries returning `Flux` can emit also an infinite number of elements. |
| `Single<T>` | A RxJava `Single` emitting a single element using reactive repositories. Expects the query method to return one result at most. If no result is found, an error signal (e.g. `EmptyResultDataAccessException`) is emitted. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Maybe<T>` | A RxJava `Maybe` emitting zero or one element using reactive repositories. Expects the query method to return one result at most. If no result is found, `Maybe.empty()` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Flowable<T>` | A RxJava `Flowable` emitting zero, one, or many elements using reactive repositories. Queries returning `Flowable` can emit also an infinite number of elements. |

---
