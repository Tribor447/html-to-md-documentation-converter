# Spring Data MongoDB

## Navigation

- Overview
  
- [Overview](#index)
    
- [Upgrading Spring Data](#commons-upgrade)
    
- [Migration Guides](#migration-guides)
      
- [Migration Guide from 2.x to 3.x](#migration-guide-migration-guide-2.x-to-3.x)
      
- [Migration Guide from 3.x to 4.x](#migration-guide-migration-guide-3.x-to-4.x)
      
- [Migration Guide from 4.x to 5.x](#migration-guide-migration-guide-4.x-to-5.x)
  
- [MongoDB Support](#mongodb)
    
- [Requirements](#preface)
    
- [Getting Started](#mongodb-getting-started)
    
- [Connecting to MongoDB](#mongodb-configuration)
    
- [Template API](#mongodb-template-api)
      
- [Configuration](#mongodb-template-config)
      
- [Index and Collection Management](#mongodb-template-collection-management)
      
- [Saving, Updating, and Removing Documents](#mongodb-template-crud-operations)
      
- [Querying Documents](#mongodb-template-query-operations)
      
- [Property Paths](#mongodb-property-paths)
      
- [Counting Documents](#mongodb-template-document-count)
      
- [Aggregation Framework Support](#mongodb-aggregation-framework)
    
- [GridFS Support](#mongodb-template-gridfs)
    
- [Object Mapping](#mongodb-mapping-mapping)
      
- [JSON Schema](#mongodb-mapping-mapping-schema)
      
- [Type based Converter](#mongodb-mapping-custom-conversions)
      
- [Property Converters](#mongodb-mapping-property-converters)
      
- [Unwrapping Types](#mongodb-mapping-unwrapping-entities)
      
- [Object References](#mongodb-mapping-document-references)
      
- [Index Creation](#mongodb-mapping-mapping-index-management)
    
- [Value Expressions Fundamentals](#mongodb-value-expressions)
    
- [Lifecycle Events](#mongodb-lifecycle-events)
    
- [Auditing](#mongodb-auditing)
    
- [Sessions & Transactions](#mongodb-client-session-transactions)
    
- [Change Streams](#mongodb-change-streams)
    
- [Tailable Cursors](#mongodb-tailable-cursors)
    
- [Sharding](#mongodb-sharding)
    
- [MongoDB Search](#mongodb-mongo-search-indexes)
    
- [Encryption](#mongodb-mongo-encryption)
    
- [Ahead of Time Optimizations](#mongodb-aot)
- [Repositories](#repositories)
  
- [Repositories](#repositories)
    
- [Core concepts](#repositories-core-concepts)
    
- [Defining Repository Interfaces](#repositories-definition)
    
- [MongoDB Repositories](#mongodb-repositories-repositories)
    
- [Spring Data Extensions](#repositories-core-extensions)
    
- [Creating Repository Instances](#repositories-create-instances)
    
- [Defining Query Methods](#repositories-query-methods-details)
    
- [MongoDB-specific Query Methods](#mongodb-repositories-query-methods)
    
- [Vector Search](#mongodb-repositories-vector-search)
    
- [MongoDB-specific Data Manipulation Methods](#mongodb-repositories-modifying-methods)
    
- [Projections](#repositories-projections)
    
- [Custom Repository Implementations](#repositories-custom-implementations)
    
- [Publishing Events from Aggregate Roots](#repositories-core-domain-events)
    
- [Null Handling of Repository Methods](#repositories-null-handling)
    
- [CDI Integration](#mongodb-repositories-cdi-integration)
    
- [Repository query keywords](#repositories-query-keywords-reference)
    
- [Repository query return types](#repositories-query-return-types-reference)
- [Observability](#observability-observability)
  
- [Observability](#observability-observability)
    
- [Conventions](#observability-conventions)
    
- [Metrics](#observability-metrics)
    
- [Spans](#observability-spans)
  
- [Kotlin Support](#kotlin)
    
- [Requirements](#kotlin-requirements)
    
- [Null Safety](#kotlin-null-safety)
    
- [Extensions](#kotlin-extensions)
    
- [Coroutines](#kotlin-coroutines)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/index.html -->

<!-- page_index: 1 -->

# Spring Data MongoDB

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-data-mongodb"></a>

# Spring Data MongoDB

*Spring Data MongoDB provides support for the MongoDB database.
It uses familiar Spring concepts such as a template classes for core API usage and lightweight repository style data access to ease development of applications with a consistent programming model.*

| [MongoDB](#mongodb) | MongoDB support and connectivity |
| --- | --- |
| [Repositories](#repositories) | Mongo Repositories |
| [Observability](#observability-observability) | Observability Integration |
| [Kotlin](#kotlin) | Kotlin support |
| [Wiki](https://github.com/spring-projects/spring-data-commons/wiki) | What’s New, Upgrade Notes, Supported Versions, additional cross-version information. |

Mark Pollack; Thomas Risberg; Oliver Gierke; Costin Leau; Jon Brisbin; Thomas Darimont; Christoph Strobl; Mark Paluch; Jay Bryant

© 2008-2026 VMware Inc.

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

---

<a id="commons-upgrade"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/commons/upgrade.html -->

<!-- page_index: 2 -->

<a id="commons-upgrade--page-title"></a>
<a id="commons-upgrade--upgrading-spring-data"></a>

# Upgrading Spring Data

Instructions for how to upgrade from earlier versions of Spring Data are provided on the project [wiki](https://github.com/spring-projects/spring-data-commons/wiki).
Follow the links in the [release notes section](https://github.com/spring-projects/spring-data-commons/wiki#release-notes) to find the version that you want to upgrade to.

Upgrading instructions are always the first item in the release notes. If you are more than one release behind, please make sure that you also review the release notes of the versions that you jumped.

---

<a id="migration-guides"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/migration-guides.html -->

<!-- page_index: 3 -->

# Migration Guides

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides--page-title"></a>
<a id="migration-guides--migration-guides"></a>

# Migration Guides

This section contains version-specific migration guides explaining how to upgrade between two versions.

<a id="migration-guides--section-summary"></a>

## Section Summary

- [Migration Guide from 2.x to 3.x](#migration-guide-migration-guide-2.x-to-3.x)
- [Migration Guide from 3.x to 4.x](#migration-guide-migration-guide-3.x-to-4.x)
- [Migration Guide from 4.x to 5.x](#migration-guide-migration-guide-4.x-to-5.x)

---

<a id="migration-guide-migration-guide-2.x-to-3.x"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/migration-guide/migration-guide-2.x-to-3.x.html -->

<!-- page_index: 4 -->

# Migration Guide from 2.x to 3.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guide-migration-guide-2.x-to-3.x--page-title"></a>
<a id="migration-guide-migration-guide-2.x-to-3.x--migration-guide-from-2.x-to-3.x"></a>

# Migration Guide from 2.x to 3.x

Spring Data MongoDB 3.x requires the MongoDB Java Driver 4.x
To learn more about driver versions please visit the [MongoDB Documentation](https://www.mongodb.com/docs/drivers/java/sync/current/upgrade/).

<a id="migration-guide-migration-guide-2.x-to-3.x--dependency-changes"></a>

## Dependency Changes

- `org.mongodb:mongo-java-driver` (uber jar) got replaced with:

  - bson-jar
  - core-jar
  - sync-jar

The change in dependencies allows usage of the reactive support without having to pull the synchronous driver.
NOTE: The new sync driver does no longer support `com.mongodb.DBObject`. Please use `org.bson.Document` instead.

<a id="migration-guide-migration-guide-2.x-to-3.x--signature-changes"></a>

## Signature Changes

- `MongoTemplate` no longer supports `com.mongodb.MongoClient` and `com.mongodb.MongoClientOptions`.
  Please use `com.mongodb.client.MongoClient` and `com.mongodb.MongoClientSettings` instead.

In case you’re using `AbstractMongoConfiguration` please switch to `AbstractMongoClientConfiguration`.

<a id="migration-guide-migration-guide-2.x-to-3.x--namespace-changes"></a>

## Namespace Changes

The switch to `com.mongodb.client.MongoClient` requires an update of your configuration XML if you have one.
The best way to provide required connection information is by using a connection string.
Please see the [MongoDB Documentation](https://docs.mongodb.com/manual/reference/connection-string/) for details.

```xml
<mongo:mongo.mongo-client id="with-defaults" />
```

```xml
<context:property-placeholder location="classpath:..."/>

<mongo:mongo.mongo-client id="client-just-host-port"
                          host="${mongo.host}" port="${mongo.port}" />

<mongo:mongo.mongo-client id="client-using-connection-string"
                          connection-string="mongodb://${mongo.host}:${mongo.port}/?replicaSet=rs0" />
```

```xml
<mongo:mongo.mongo-client id="client-with-settings" replica-set="rs0">
		<mongo:client-settings cluster-connection-mode="MULTIPLE"
							   cluster-type="REPLICA_SET"
							   cluster-server-selection-timeout="300"
							   cluster-local-threshold="100"
							   cluster-hosts="localhost:27018,localhost:27019,localhost:27020" />
	</mongo:mongo.mongo-client>
```

---

<a id="migration-guide-migration-guide-3.x-to-4.x"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/migration-guide/migration-guide-3.x-to-4.x.html -->

<!-- page_index: 5 -->

<a id="migration-guide-migration-guide-3.x-to-4.x--page-title"></a>
<a id="migration-guide-migration-guide-3.x-to-4.x--migration-guide-from-3.x-to-4.x"></a>

# Migration Guide from 3.x to 4.x

Spring Data MongoDB 4.x requires the MongoDB Java Driver 4.8.x
To learn more about driver versions please visit the [MongoDB Documentation](https://www.mongodb.com/docs/drivers/java/sync/current/upgrade/).

---

<a id="migration-guide-migration-guide-4.x-to-5.x"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/migration-guide/migration-guide-4.x-to-5.x.html -->

<!-- page_index: 6 -->

# Migration Guide from 4.x to 5.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guide-migration-guide-4.x-to-5.x--page-title"></a>
<a id="migration-guide-migration-guide-4.x-to-5.x--migration-guide-from-4.x-to-5.x"></a>

# Migration Guide from 4.x to 5.x

Spring Data MongoDB 5.x requires the MongoDB Java Driver 5.6+
To learn more about driver versions please visit the [MongoDB Documentation](https://www.mongodb.com/docs/drivers/java/sync/current/upgrade/).

<a id="migration-guide-migration-guide-4.x-to-5.x--_mongodb_java_driver_4_x_driver_compatibility_removed"></a>
<a id="migration-guide-migration-guide-4.x-to-5.x--mongodb-java-driver-4.x-driver-compatibility-removed"></a>

## MongoDB Java Driver 4.x Driver Compatibility Removed

Spring Data MongoDB does no longer support the 4.x MongoDB Java Driver generation.

<a id="migration-guide-migration-guide-4.x-to-5.x--_uuid_representation_changes"></a>
<a id="migration-guide-migration-guide-4.x-to-5.x--uuid-representation-changes"></a>

## UUID Representation Changes

Spring Data no longer defaults UUID settings via its configuration support classes, factory beans, nor XML namespace.
In order to persist UUID values the `UuidRepresentation` hast to be set explicitly.

- Java
- XML

```java
@Configuration static class Config extends AbstractMongoClientConfiguration {
@Override protected void configureClientSettings(MongoClientSettings.Builder builder) {builder.uuidRepresentation(UuidRepresentation.STANDARD);}
// ...}
```

```xml
<mongo:mongo-client>
	<mongo:client-settings uuid-representation="STANDARD"/>
</mongo:mongo-client>
```

<a id="migration-guide-migration-guide-4.x-to-5.x--_bigintegerbigdecimal_conversion_changes"></a>
<a id="migration-guide-migration-guide-4.x-to-5.x--biginteger-bigdecimal-conversion-changes"></a>

## BigInteger/BigDecimal Conversion Changes

Spring Data no longer defaults BigInteger/BigDecimal conversion via its configuration support classes.
In order to persist those values the default `BigDecimalRepresentation` hast to be set explicitly.

```java
@Configuration static class Config extends AbstractMongoClientConfiguration {
@Override protected void configureConverters(MongoConverterConfigurationAdapter configAdapter) {configAdapter.bigDecimal(BigDecimalRepresentation.DECIMAL128);}
// ...}
```

Users upgrading from prior versions may choose `BigDecimalRepresentation.STRING` as default to retain previous behaviour.

<a id="migration-guide-migration-guide-4.x-to-5.x--_defaultmessagelistenercontainer_auto_startup"></a>
<a id="migration-guide-migration-guide-4.x-to-5.x--defaultmessagelistenercontainer-auto-startup"></a>

## DefaultMessageListenerContainer auto startup

The `DefaultMessageListenerContainer` that can be used to listen to e.g. *Change Streams* now defaults its `SmartLifecycle` auto startup to `true`.

<a id="migration-guide-migration-guide-4.x-to-5.x--_jmx_support_discontinued"></a>
<a id="migration-guide-migration-guide-4.x-to-5.x--jmx-support-discontinued."></a>

## JMX Support Discontinued.

We recommend switching to Spring Boot [Actuator Endpoints](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html).

---

<a id="mongodb"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb.html -->

<!-- page_index: 7 -->

# MongoDB Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb--page-title"></a>
<a id="mongodb--mongodb-support"></a>

# MongoDB Support

Spring Data support for MongoDB contains a wide range of features:

- [Spring configuration support](#mongodb-template-config) with Java-based `@Configuration` classes or an XML namespace for a Mongo driver instance and replica sets.
- [`MongoTemplate` helper class](#mongodb-template-api) that increases productivity when performing common Mongo operations.
  Includes integrated object mapping between documents and POJOs.
- [Exception translation](#mongodb-template-api--mongo-template.exception-translation) into Spring’s portable Data Access Exception hierarchy.
- Feature-rich [Object Mapping](#mongodb-mapping-mapping) integrated with Spring’s Conversion Service.
- [Annotation-based mapping metadata](#mongodb-mapping-mapping--mapping-usage-annotations) that is extensible to support other metadata formats.
- [Persistence and mapping lifecycle events](#mongodb-lifecycle-events).
- [Java-based Query, Criteria, and Update DSLs](#mongodb-template-query-operations).
- Automatic implementation of [Repository interfaces](#repositories), including support for custom query methods.
- [QueryDSL integration](#repositories-core-extensions--mongodb.repositories.queries.type-safe) to support type-safe queries.
- [Multi-Document Transactions](#mongodb-client-session-transactions).
- [GeoSpatial integration](#mongodb-template-query-operations--mongo.geo-json).
- [Vector Index](#mongodb-mongo-search-indexes--mongo.search.vector) and declarative [Vector Search](#mongodb-repositories-vector-search) support.
- [Ahead Of Time (AOT)](#mongodb-aot) optimizations.

For most tasks, you should use `MongoTemplate` or the Repository support, which both leverage the rich mapping functionality.
`MongoTemplate` is the place to look for accessing functionality such as incrementing counters or ad-hoc CRUD operations.
`MongoTemplate` also provides callback methods so that it is easy for you to get the low-level API artifacts, such as `com.mongodb.client.MongoDatabase`, to communicate directly with MongoDB.
The goal with naming conventions on various API artifacts is to copy those in the base MongoDB Java driver so you can easily map your existing knowledge onto the Spring APIs.

<a id="mongodb--section-summary"></a>

## Section Summary

- [Requirements](#preface)
- [Getting Started](#mongodb-getting-started)
- [Connecting to MongoDB](#mongodb-configuration)
- [Template API](#mongodb-template-api)
- [GridFS Support](#mongodb-template-gridfs)
- [Object Mapping](#mongodb-mapping-mapping)
- [Value Expressions Fundamentals](#mongodb-value-expressions)
- [Lifecycle Events](#mongodb-lifecycle-events)
- [Auditing](#mongodb-auditing)
- [Sessions & Transactions](#mongodb-client-session-transactions)
- [Change Streams](#mongodb-change-streams)
- [Tailable Cursors](#mongodb-tailable-cursors)
- [Sharding](#mongodb-sharding)
- [MongoDB Search](#mongodb-mongo-search-indexes)
- [Encryption](#mongodb-mongo-encryption)
- [Ahead of Time Optimizations](#mongodb-aot)

---

<a id="preface"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/preface.html -->

<!-- page_index: 8 -->

# Requirements

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="preface--page-title"></a>
<a id="preface--requirements"></a>

# Requirements

The Spring Data MongoDB 5.x binaries require JDK level 17 and above and [Spring Framework](https://spring.io/docs) 7.0.8 and above.

<a id="preface--compatibility.matrix"></a>
<a id="preface--compatibility-matrix"></a>

## Compatibility Matrix

> [!TIP]
> Please visit [OSS Support](https://spring.io/projects/spring-data-mongodb#support) for detailed Spring Data support timelines.
> For the MongoDB Server Support Policy please refer to the [MongoDB Software Lifecycle Schedule](https://www.mongodb.com/legal/support-policy/lifecycles).

The following compatibility matrix summarizes Spring Data versions and their required minimum MongoDB client version.
Database versions show server generations that pass the Spring Data test suite, older server versions might have difficulties dealing with new/changed commands.
You may use newer server versions unless your application uses functionality that is affected by [changes in the MongoDB server](#preface--compatibility.changes).
See also the [official MongoDB driver compatibility matrix](https://www.mongodb.com/docs/drivers/java/sync/current/compatibility/) for driver- and server version compatibility.

| Spring Data Release Train | Spring Data MongoDB | Minimum Driver Version | Tested Database Versions |
| --- | --- | --- | --- |
| 2026.0 | `5.1.x` | `5.6.x` | `6.x to 8.x` |
| 2025.1 | `5.0.x` | `5.6.x` | `6.x to 8.x` |
| 2025.0 | `4.5.x` | `5.5.x` | `6.x to 8.x` |
| 2024.1 | `4.4.x` | `5.2.x` | `4.4.x to 8.x` |
| 2024.0 | `4.3.x` | `4.11.x & 5.x` | `4.4.x to 7.x` |

<a id="preface--compatibility.changes-4.4"></a>
<a id="preface--relevant-changes-in-mongodb-4.4"></a>

### Relevant Changes in MongoDB 4.4

- Fields list must not contain text search score property when no `$text` criteria present. See also [`$text` operator](https://docs.mongodb.com/manual/reference/operator/query/text/)
- Sort must not be an empty document when running map reduce.

<a id="preface--compatibility.changes-4.2"></a>
<a id="preface--relevant-changes-in-mongodb-4.2"></a>

### Relevant Changes in MongoDB 4.2

- Removal of `geoNear` command. See also [Removal of `geoNear`](https://docs.mongodb.com/manual/release-notes/4.2-compatibility/#remove-support-for-the-geonear-command)
- Removal of `eval` command. See also [Removal of `eval`](https://docs.mongodb.com/manual/release-notes/4.2-compatibility/#remove-support-for-the-eval-command)

---

<a id="mongodb-getting-started"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/getting-started.html -->

<!-- page_index: 9 -->

# Getting Started

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-getting-started--page-title"></a>
<a id="mongodb-getting-started--getting-started"></a>

# Getting Started

An easy way to bootstrap setting up a working environment is to create a Spring-based project via [start.spring.io](https://start.spring.io/#!type=maven-project&dependencies=data-mongodb) or create a Spring project in [Spring Tools](https://spring.io/tools).

<a id="mongodb-getting-started--mongo.examples-repo"></a>
<a id="mongodb-getting-started--examples-repository"></a>

## Examples Repository

The GitHub [spring-data-examples repository](https://github.com/spring-projects/spring-data-examples) hosts several examples that you can download and play around with to get a feel for how the library works.

<a id="mongodb-getting-started--mongodb.hello-world"></a>
<a id="mongodb-getting-started--hello-world"></a>

## Hello World

First, you need to set up a running MongoDB server. Refer to the [MongoDB Quick Start guide](https://docs.mongodb.org/manual/core/introduction/) for an explanation on how to startup a MongoDB instance.
Once installed, starting MongoDB is typically a matter of running the following command: `/bin/mongod`

Then you can create a `Person` class to persist:

```java
public class Person {
private String id; private String name; private int age;
public Person(String name, int age) {this.name = name; this.age = age;}
public String getId() {return id;}
public String getName() {return name;}
public int getAge() {return age;}
@Override public String toString() {return "Person [id=" + id + ", name=" + name + ", age=" + age + "]";}}
```

You also need a main application to run:

- Imperative
- Reactive

```java
import static org.springframework.data.mongodb.core.query.Criteria.*;

import org.springframework.data.mongodb.core.MongoOperations;
import org.springframework.data.mongodb.core.MongoTemplate;

import com.mongodb.client.MongoClients;

public class MongoApplication {

	public static void main(String[] args) throws Exception {

		MongoOperations mongoOps = new MongoTemplate(MongoClients.create(), "database");
		mongoOps.insert(new Person("Joe", 34));

		System.out.println(mongoOps.query(Person.class).matching(where("name").is("Joe")).firstValue());

		mongoOps.dropCollection("person");
	}
}
```

```java
import static org.springframework.data.mongodb.core.query.Criteria.*;

import org.springframework.data.mongodb.core.ReactiveMongoOperations;
import org.springframework.data.mongodb.core.ReactiveMongoTemplate;

import com.mongodb.reactivestreams.client.MongoClients;

public class ReactiveMongoApplication {

	public static void main(String[] args) throws Exception {

		ReactiveMongoOperations mongoOps = new ReactiveMongoTemplate(MongoClients.create(), "database");

		mongoOps.insert(new Person("Joe", 34))
			.then(mongoOps.query(Person.class).matching(where("name").is("Joe")).first())
			.doOnNext(System.out::println)
			.block();

		mongoOps.dropCollection("person").block();
	}
}
```

When you run the main program, the preceding examples produce the following output:

```none
10:01:32,265 DEBUG o.s.data.mongodb.core.MongoTemplate - insert Document containing fields: [_class, age, name] in collection: Person
10:01:32,765 DEBUG o.s.data.mongodb.core.MongoTemplate - findOne using query: { "name" : "Joe"} in db.collection: database.Person
Person [id=4ddbba3c0be56b7e1b210166, name=Joe, age=34]
10:01:32,984 DEBUG o.s.data.mongodb.core.MongoTemplate - Dropped collection [database.person]
```

Even in this simple example, there are few things to notice:

- You can instantiate the central helper class of Spring Mongo, [`MongoTemplate`](#mongodb-template-api), by using the standard or reactive `MongoClient` object and the name of the database to use.
- The mapper works against standard POJO objects without the need for any additional metadata (though you can optionally provide that information. See [here](#mongodb-mapping-mapping)).
- Conventions are used for handling the `id` field, converting it to be an `ObjectId` when stored in the database.
- Mapping conventions can use field access. Notice that the `Person` class has only getters.
- If the constructor argument names match the field names of the stored document, they are used to instantiate the object

---

<a id="mongodb-configuration"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/configuration.html -->

<!-- page_index: 10 -->

# Connecting to MongoDB

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-configuration--page-title"></a>
<a id="mongodb-configuration--connecting-to-mongodb"></a>

# Connecting to MongoDB

One of the first tasks when using MongoDB and Spring is to create a `MongoClient` object using the IoC container.
There are two main ways to do this, either by using Java-based bean metadata or by using XML-based bean metadata.

> [!NOTE]
> For those not familiar with how to configure the Spring container using Java-based bean metadata instead of XML-based metadata, see the high-level introduction in the reference docs [here](https://docs.spring.io/spring/docs/3.2.x/spring-framework-reference/html/new-in-3.0.html#new-java-configuration) as well as the detailed documentation [here](https://docs.spring.io/spring-framework/docs/7.0.8/reference/html/core.html#beans-java-instantiating-container).

<a id="mongodb-configuration--mongo.mongo-java-config"></a>
<a id="mongodb-configuration--registering-a-mongo-instance"></a>

## Registering a Mongo Instance

The following example shows an example to register an instance of a `MongoClient`:

Registering `MongoClient`

- Imperative
- Reactive
- XML

```java
@Configuration public class AppConfig {
/* * Use the standard Mongo driver API to create a com.mongodb.client.MongoClient instance.*/ public @Bean com.mongodb.client.MongoClient mongoClient() {return com.mongodb.client.MongoClients.create("mongodb://localhost:27017");}}
```

```java
@Configuration public class AppConfig {
/* * Use the standard Mongo driver API to create a com.mongodb.client.MongoClient instance.*/ public @Bean com.mongodb.reactivestreams.client.MongoClient mongoClient() {return com.mongodb.reactivestreams.client.MongoClients.create("mongodb://localhost:27017");}}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:mongo="http://www.springframework.org/schema/data/mongo"
xsi:schemaLocation=
"
http://www.springframework.org/schema/data/mongo https://www.springframework.org/schema/data/mongo/spring-mongo.xsd
http://www.springframework.org/schema/beans
https://www.springframework.org/schema/beans/spring-beans.xsd">

    <!-- Default bean name is 'mongo' -->
    <mongo:mongo-client host="localhost" port="27017"/>

</beans>
```

This approach lets you use the standard `MongoClient` instance, with the container using Spring’s `MongoClientFactoryBean`/`ReactiveMongoClientFactoryBean`.
As compared to instantiating a `MongoClient` instance directly, the `FactoryBean` has the added advantage of also providing the container with an `ExceptionTranslator` implementation that translates MongoDB exceptions to exceptions in Spring’s portable `DataAccessException` hierarchy for data access classes annotated with the `@Repository` annotation.
This hierarchy and the use of `@Repository` is described in [Spring’s DAO support features](https://docs.spring.io/spring-framework/reference/7.0/data-access.html).

The following example shows an example of a Java-based bean metadata that supports exception translation on `@Repository` annotated classes:

Registering a `MongoClient` via `MongoClientFactoryBean` / `ReactiveMongoClientFactoryBean`

- Imperative
- Reactive

```java
@Configuration public class AppConfig {
/* * Factory bean that creates the com.mongodb.client.MongoClient instance */ public @Bean MongoClientFactoryBean mongo() {MongoClientFactoryBean mongo = new MongoClientFactoryBean(); mongo.setHost("localhost"); return mongo;}}
```

```java
@Configuration public class AppConfig {
/* * Factory bean that creates the com.mongodb.reactivestreams.client.MongoClient instance */ public @Bean ReactiveMongoClientFactoryBean mongo() {ReactiveMongoClientFactoryBean mongo = new ReactiveMongoClientFactoryBean(); mongo.setHost("localhost"); return mongo;}}
```

To access the `MongoClient` object created by the `FactoryBean` in other `@Configuration` classes or your own classes, use a `private @Autowired MongoClient mongoClient;` field.

<a id="mongodb-configuration--mongo.mongo-db-factory"></a>
<a id="mongodb-configuration--the-mongodatabasefactory-interface"></a>

## The MongoDatabaseFactory Interface

While `MongoClient` is the entry point to the MongoDB driver API, connecting to a specific MongoDB database instance requires additional information, such as the database name and an optional username and password.
With that information, you can obtain a `MongoDatabase` object and access all the functionality of a specific MongoDB database instance.
Spring provides the `org.springframework.data.mongodb.core.MongoDatabaseFactory` & `org.springframework.data.mongodb.core.ReactiveMongoDatabaseFactory` interfaces, shown in the following listing, to bootstrap connectivity to the database:

- Imperative
- Reactive

```java
public interface MongoDatabaseFactory {

  MongoDatabase getDatabase() throws DataAccessException;

  MongoDatabase getDatabase(String dbName) throws DataAccessException;
}
```

```java
public interface ReactiveMongoDatabaseFactory {

  Mono<MongoDatabase> getDatabase() throws DataAccessException;

  Mono<MongoDatabase> getDatabase(String dbName) throws DataAccessException;
}
```

The following sections show how you can use the container with either Java-based or XML-based metadata to configure an instance of the `MongoDatabaseFactory` interface.
In turn, you can use the `MongoDatabaseFactory` / `ReactiveMongoDatabaseFactory` instance to configure `MongoTemplate` / `ReactiveMongoTemplate`.

Instead of using the IoC container to create an instance of the template, you can use them in standard Java code, as follows:

- Imperative
- Reactive

```java
public class MongoApplication {
public static void main(String[] args) throws Exception {
MongoOperations mongoOps = new MongoTemplate(new SimpleMongoClientDatabaseFactory(MongoClients.create(), "database"));
// ...}}
```

The code in bold highlights the use of `SimpleMongoClientDbFactory` and is the only difference between the listing shown in the [getting started section](#mongodb-getting-started).
Use `SimpleMongoClientDbFactory` when choosing `com.mongodb.client.MongoClient` as the entrypoint of choice.

```java
public class ReactiveMongoApplication {
public static void main(String[] args) throws Exception {
ReactiveMongoOperations mongoOps = new MongoTemplate(new SimpleReactiveMongoDatabaseFactory(MongoClients.create(), "database"));
// ...}}
```

<a id="mongodb-configuration--mongo.mongo-db-factory.config"></a>
<a id="mongodb-configuration--registering-a-mongodatabasefactory-reactivemongodatabasefactory"></a>

## Registering a `MongoDatabaseFactory` / `ReactiveMongoDatabaseFactory`

To register a `MongoDatabaseFactory`/ `ReactiveMongoDatabaseFactory` instance with the container, you write code much like what was highlighted in the previous section.
The following listing shows a simple example:

- Imperative
- Reactive

```java
@Configuration public class MongoConfiguration {
@Bean public MongoDatabaseFactory mongoDatabaseFactory() {return new SimpleMongoClientDatabaseFactory(MongoClients.create(), "database");}}
```

```java
@Configuration public class ReactiveMongoConfiguration {
@Bean public ReactiveMongoDatabaseFactory mongoDatabaseFactory() {return new SimpleReactiveMongoDatabaseFactory(MongoClients.create(), "database");}}
```

MongoDB Server generation 3 changed the authentication model when connecting to the DB.
Therefore, some of the configuration options available for authentication are no longer valid.
You should use the `MongoClient`-specific options for setting credentials through `MongoCredential` to provide authentication data, as shown in the following example:

- Java
- XML

```java
@Configuration public class MongoAppConfig extends AbstractMongoClientConfiguration {
@Override public String getDatabaseName() {return "database";}
@Override protected void configureClientSettings(Builder builder) {
builder .credential(MongoCredential.createCredential("name", "db", "pwd".toCharArray())) .applyToClusterSettings(settings  -> {settings.hosts(singletonList(new ServerAddress("127.0.0.1", 27017))); });}}
```

```xml
<mongo:db-factory dbname="database" />
```

Username and password credentials used in XML-based configuration must be URL-encoded when these contain reserved characters, such as `:`, `%`, `@`, or `,`.
The following example shows encoded credentials:
`m0ng0@dmin:mo_res:bw6},Qsdxx@admin@database` → `m0ng0%40dmin:mo_res%3Abw6%7D%2CQsdxx%40admin@database`
See [section 2.2 of RFC 3986](https://tools.ietf.org/html/rfc3986#section-2.2) for further details.

If you need to configure additional options on the `com.mongodb.client.MongoClient` instance that is used to create a `SimpleMongoClientDbFactory`, you can refer to an existing bean as shown in the following example. To show another common usage pattern, the following listing shows the use of a property placeholder, which lets you parametrize the configuration and the creation of a `MongoTemplate`:

- Java
- XML

```java
@Configuration
@PropertySource("classpath:/com/myapp/mongodb/config/mongo.properties")
public class MongoAppConfig extends AbstractMongoClientConfiguration {

  @Autowired
  Environment env;

  @Override
  public String getDatabaseName() {
    return "database";
  }

  @Override
  protected void configureClientSettings(Builder builder) {

    builder.applyToClusterSettings(settings -> {
    settings.hosts(singletonList(
          new ServerAddress(env.getProperty("mongo.host"), env.getProperty("mongo.port", Integer.class))));
    });

    builder.applyToConnectionPoolSettings(settings -> {

      settings.maxConnectionLifeTime(env.getProperty("mongo.pool-max-life-time", Integer.class), TimeUnit.MILLISECONDS)
          .minSize(env.getProperty("mongo.pool-min-size", Integer.class))
          .maxSize(env.getProperty("mongo.pool-max-size", Integer.class))
          .maintenanceFrequency(10, TimeUnit.MILLISECONDS)
          .maintenanceInitialDelay(11, TimeUnit.MILLISECONDS)
          .maxConnectionIdleTime(30, TimeUnit.SECONDS)
          .maxWaitTime(15, TimeUnit.MILLISECONDS);
    });
  }
}
```

```xml
<context:property-placeholder location="classpath:/com/myapp/mongodb/config/mongo.properties"/>

<mongo:mongo-client host="${mongo.host}" port="${mongo.port}">
  <mongo:client-settings connection-pool-max-connection-life-time="${mongo.pool-max-life-time}"
    connection-pool-min-size="${mongo.pool-min-size}"
    connection-pool-max-size="${mongo.pool-max-size}"
    connection-pool-maintenance-frequency="10"
    connection-pool-maintenance-initial-delay="11"
    connection-pool-max-connection-idle-time="30"
    connection-pool-max-wait-time="15" />
</mongo:mongo-client>

<mongo:db-factory dbname="database" mongo-ref="mongoClient"/>

<bean id="anotherMongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
  <constructor-arg name="mongoDbFactory" ref="mongoDbFactory"/>
</bean>
```

---

<a id="mongodb-template-api"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-api.html -->

<!-- page_index: 11 -->

# Template API

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-api--page-title"></a>
<a id="mongodb-template-api--template-api"></a>

# Template API

The [`MongoTemplate`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoTemplate.html) and its [reactive](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/ReactiveMongoTemplate.html) counterpart class, located in the `org.springframework.data.mongodb.core` package, is the central class of Spring’s MongoDB support and provides a rich feature set for interacting with the database.
The template offers convenience operations to create, update, delete, and query MongoDB documents and provides a mapping between your domain objects and MongoDB documents.

> [!NOTE]
> Once configured, `MongoTemplate` is thread-safe and can be reused across multiple instances.

<a id="mongodb-template-api--mongo-template.convenience-methods"></a>
<a id="mongodb-template-api--convenience-methods"></a>

## Convenience Methods

The [`MongoTemplate`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoTemplate.html) class implements the interface [`MongoOperations`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoOperations.html).
In as much as possible, the methods on `MongoOperations` are named after methods available on the MongoDB driver `Collection` object, to make the API familiar to existing MongoDB developers who are used to the driver API.
For example, you can find methods such as `find`, `findAndModify`, `findAndReplace`, `findOne`, `insert`, `remove`, `save`, `update`, and `updateMulti`.
The design goal was to make it as easy as possible to transition between the use of the base MongoDB driver and `MongoOperations`.
A major difference between the two APIs is that `MongoOperations` can be passed domain objects instead of `Document`.
Also, `MongoOperations` has fluent APIs for `Query`, `Criteria`, and `Update` operations instead of populating a `Document` to specify the parameters for those operations.

For more information please refer to the [CRUD](#mongodb-template-crud-operations) and [Query](#mongodb-template-query-operations) sections of the documentation.

> [!NOTE]
> The preferred way to reference the operations on `MongoTemplate` instance is through its interface, `MongoOperations`.

<a id="mongodb-template-api--mongo-template.execute-callbacks"></a>
<a id="mongodb-template-api--execute-callbacks"></a>

## Execute Callbacks

`MongoTemplate` offers many convenience methods to help you easily perform common tasks.
However, if you need to directly access the MongoDB driver API, you can use one of several `Execute` callback methods.
The `execute` callbacks gives you a reference to either a `MongoCollection` or a `MongoDatabase` object.

- `<T> T` **execute** `(Class<?> entityClass, CollectionCallback<T> action)`: Runs the given `CollectionCallback` for the entity collection of the specified class.
- `<T> T` **execute** `(String collectionName, CollectionCallback<T> action)`: Runs the given `CollectionCallback` on the collection of the given name.
- `<T> T` **execute** `(DbCallback<T> action)`: Runs a DbCallback, translating any exceptions as necessary.
  Spring Data MongoDB provides support for the Aggregation Framework introduced to MongoDB in version 2.2.
- `<T> T` **execute** `(String collectionName, DbCallback<T> action)`: Runs a `DbCallback` on the collection of the given name translating any exceptions as necessary.
- `<T> T` **executeInSession** `(DbCallback<T> action)`: Runs the given `DbCallback` within the same connection to the database so as to ensure consistency in a write-heavy environment where you may read the data that you wrote.

The following example uses the [`CollectionCallback`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/CollectionCallback.html) to return information about an index:

- Imperative
- Reactive

```java
boolean hasIndex = template.execute("geolocation", collection ->
    Streamable.of(collection.listIndexes(org.bson.Document.class))
        .stream()
        .map(document -> document.get("name"))
        .anyMatch("location_2d"::equals)
);
```

```java
Mono<Boolean> hasIndex = template.execute("geolocation", collection ->
    Flux.from(collection.listIndexes(org.bson.Document.class))
        .map(document -> document.get("name"))
        .filterWhen(name -> Mono.just("location_2d".equals(name)))
        .map(it -> Boolean.TRUE)
        .single(Boolean.FALSE)
    ).next();
```

<a id="mongodb-template-api--mongo-template.fluent-api"></a>
<a id="mongodb-template-api--fluent-api"></a>

## Fluent API

Being the central component when it comes to more low-level interaction with MongoDB `MongoTemplate` offers a wide range of methods covering needs from collection creation, index creation, and CRUD operations to more advanced functionality, such as Map-Reduce and aggregations.
You can find multiple overloads for each method.
Most of them cover optional or nullable parts of the API.

`FluentMongoOperations` provides a more narrow interface for the common methods of `MongoOperations` and provides a more readable, fluent API.
The entry points (`insert(…)`, `find(…)`, `update(…)`, and others) follow a natural naming schema based on the operation to be run.
Moving on from the entry point, the API is designed to offer only context-dependent methods that lead to a terminating method that invokes the actual `MongoOperations` counterpart — the `all` method in the case of the following example:

Imperative
: ```java
List<Jedi> all = template.query(SWCharacter.class) (1)
  .inCollection("star-wars") (2)
  .as(Jedi.class) (3)
  .matching(query(where("jedi").is(true))) (4)
  .all();
```

**1**

The type used to map fields used in the query to.

**2**

The collection name to use if not defined on the domain type.

**3**

Result type if not using the original domain type.

**4**

The lookup query.

Reactive
: ```java
Flux<Jedi> all = template.query(SWCharacter.class)
  .inCollection("star-wars")
  .as(Jedi.class)
  .matching(query(where("jedi").is(true)))
  .all();
```


> [!NOTE]
> Using projections allows `MongoTemplate` to optimize result mapping by limiting the actual response to fields required by the projection target type.
> This applies as long as the [`Query`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/query/Query.html) itself does not contain any field restriction and the target type is a closed interface or DTO projection.


> [!WARNING]
> Projections must not be applied to [DBRefs](#mongodb-mapping-document-references).


You can switch between retrieving a single entity and retrieving multiple entities as a `List` or a `Stream` through the terminating methods: `first()`, `one()`, `all()`, or `stream()`.

Results can be contextually post-processed by using a `QueryResultConverter` that has access to both the raw result `Document` and the already mapped object by calling `map(…)` as outlined below.


```
List<Optional<Jedi>> result = template.query(Person.class)
    .as(Jedi.class)
    .matching(query(where("firstname").is("luke")))
    .map((document, reader) -> Optional.of(reader.get()))
    .all();
```


When writing a geo-spatial query with `near(NearQuery)`, the number of terminating methods is altered to include only the methods that are valid for running a `geoNear` command in MongoDB (fetching entities as a `GeoResult` within `GeoResults`), as the following example shows:

- Imperative
- Reactive


```java
GeoResults<Jedi> results = template.query(SWCharacter.class)
  .as(Jedi.class)
  .near(alderaan) // NearQuery.near(-73.9667, 40.78).maxDis…
  .all();
```

```java
Flux<GeoResult<Jedi>> results = template.query(SWCharacter.class)
  .as(Jedi.class)
  .near(alderaan) // NearQuery.near(-73.9667, 40.78).maxDis…
  .all();
```

<a id="mongodb-template-api--mongo-template.exception-translation"></a>
<a id="mongodb-template-api--exception-translation"></a>

## Exception Translation

The Spring framework provides exception translation for a wide variety of database and mapping technologies.
This has traditionally been for JDBC and JPA.
The Spring support for MongoDB extends this feature to the MongoDB Database by providing an implementation of the `org.springframework.dao.support.PersistenceExceptionTranslator` interface.

The motivation behind mapping to Spring’s [consistent data access exception hierarchy](https://docs.spring.io/spring-framework/reference/7.0/data-access.html#dao-exceptions) is that you are then able to write portable and descriptive exception handling code without resorting to coding against MongoDB error codes.
All of Spring’s data access exceptions are inherited from the root `DataAccessException` class so that you can be sure to catch all database related exception within a single try-catch block.
Note that not all exceptions thrown by the MongoDB driver inherit from the `MongoException` class.
The inner exception and message are preserved so that no information is lost.

Some of the mappings performed by the [`MongoExceptionTranslator`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoExceptionTranslator.html) are `com.mongodb.Network` to `DataAccessResourceFailureException` and `MongoException` error codes 1003, 12001, 12010, 12011, and 12012 to `InvalidDataAccessApiUsageException`.
Look into the implementation for more details on the mapping.

Exception Translation can be configured by setting a customized [`MongoExceptionTranslator`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoExceptionTranslator.html) on your `MongoDatabaseFactory` or its reactive variant.
You might also want to set the exception translator on the corresponding `MongoClientFactoryBean`.

Example 1. Configuring `MongoExceptionTranslator`

```java
ConnectionString uri = new ConnectionString("mongodb://username:password@localhost/database");
SimpleMongoClientDatabaseFactory mongoDbFactory = new SimpleMongoClientDatabaseFactory(uri);
mongoDbFactory.setExceptionTranslator(myCustomExceptionTranslator);
```

A motivation to customize exception can be MongoDB’s behavior during transactions where some failures (such as write conflicts) can become transient and where a retry could lead to a successful operation.
In such a case, you could wrap exceptions with a specific MongoDB label and apply a different exception translation strategy.

<a id="mongodb-template-api--mongo-template.type-mapping"></a>
<a id="mongodb-template-api--domain-type-mapping"></a>

## Domain Type Mapping

The mapping between MongoDB documents and domain classes is done by delegating to an implementation of the [`MongoConverter`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/convert/MongoConverter.html) interface.
Spring provides [`MappingMongoConverter`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/convert/MappingMongoConverter.html), but you can also write your own converter.
While the `MappingMongoConverter` can use additional metadata to specify the mapping of objects to documents, it can also convert objects that contain no additional metadata by using some conventions for the mapping of IDs and collection names.
These conventions, as well as the use of mapping annotations, are explained in the [Mapping](#mongodb-mapping-mapping) chapter.

---

<a id="mongodb-template-config"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-config.html -->

<!-- page_index: 12 -->

# Configuration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-config--page-title"></a>
<a id="mongodb-template-config--configuration"></a>

# Configuration

You can use the following configuration to create and register an instance of `MongoTemplate`, as the following example shows:

Registering a `MongoClient` object and enabling Spring’s exception translation support

- Imperative
- Reactive
- XML

```java
@Configuration class ApplicationConfiguration {
@Bean MongoClient mongoClient() {return MongoClients.create("mongodb://localhost:27017");}
@Bean MongoOperations mongoTemplate(MongoClient mongoClient) {return new MongoTemplate(mongoClient, "geospatial");}}
```

```java
@Configuration class ReactiveApplicationConfiguration {
@Bean MongoClient mongoClient() {return MongoClients.create("mongodb://localhost:27017");}
@Bean ReactiveMongoOperations mongoTemplate(MongoClient mongoClient) {return new ReactiveMongoTemplate(mongoClient, "geospatial");}}
```

```xml
<mongo:mongo-client host="localhost" port="27017" />

<bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
  <constructor-arg ref="mongoClient" />
  <constructor-arg name="databaseName" value="geospatial" />
</bean>
```

There are several overloaded constructors of [`MongoTemplate`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoTemplate.html) and [`ReactiveMongoTemplate`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/ReactiveMongoTemplate.html):

- `MongoTemplate(MongoClient mongo, String databaseName)`: Takes the `MongoClient` object and the default database name to operate against.
- `MongoTemplate(MongoDatabaseFactory mongoDbFactory)`: Takes a MongoDbFactory object that encapsulated the `MongoClient` object, database name, and username and password.
- `MongoTemplate(MongoDatabaseFactory mongoDbFactory, MongoConverter mongoConverter)`: Adds a `MongoConverter` to use for mapping.

Other optional properties that you might like to set when creating a `MongoTemplate` / `ReactiveMongoTemplate` are the default `WriteResultCheckingPolicy`, `WriteConcern`, `ReadPreference` and others listed below.

<a id="mongodb-template-config--mongo-template.read-preference"></a>
<a id="mongodb-template-config--default-read-preference"></a>

## Default Read Preference

The default read preference applied to read operations if no other preference was defined via the [Query](#mongodb-template-query-operations--mongo.query.read-preference).

<a id="mongodb-template-config--mongo-template.writeresultchecking"></a>
<a id="mongodb-template-config--writeresultchecking-policy"></a>

## WriteResultChecking Policy

When in development, it is handy to either log or throw an exception if the `com.mongodb.WriteResult` returned from any MongoDB operation contains an error. It is quite common to forget to do this during development and then end up with an application that looks like it runs successfully when, in fact, the database was not modified according to your expectations. You can set the `WriteResultChecking` property of `MongoTemplate` to one of the following values: `EXCEPTION` or `NONE`, to either throw an `Exception` or do nothing, respectively. The default is to use a `WriteResultChecking` value of `NONE`.

<a id="mongodb-template-config--mongo-template.writeconcern"></a>
<a id="mongodb-template-config--default-writeconcern"></a>

## Default WriteConcern

If it has not yet been specified through the driver at a higher level (such as `com.mongodb.client.MongoClient`), you can set the `com.mongodb.WriteConcern` property that the `MongoTemplate` uses for write operations. If the `WriteConcern` property is not set, it defaults to the one set in the MongoDB driver’s DB or Collection setting.

<a id="mongodb-template-config--mongo-template.writeconcernresolver"></a>
<a id="mongodb-template-config--writeconcernresolver"></a>

## WriteConcernResolver

For more advanced cases where you want to set different `WriteConcern` values on a per-operation basis (for remove, update, insert, and save operations), a strategy interface called `WriteConcernResolver` can be configured on `MongoTemplate`. Since `MongoTemplate` is used to persist POJOs, the `WriteConcernResolver` lets you create a policy that can map a specific POJO class to a `WriteConcern` value. The following listing shows the `WriteConcernResolver` interface:

```java
public interface WriteConcernResolver {
  WriteConcern resolve(MongoAction action);
}
```

You can use the `MongoAction` argument to determine the `WriteConcern` value or use the value of the Template itself as a default.
`MongoAction` contains the collection name being written to, the `java.lang.Class` of the POJO, the converted `Document`, the operation (`REMOVE`, `UPDATE`, `INSERT`, `INSERT_LIST`, or `SAVE`), and a few other pieces of contextual information.
The following example shows two sets of classes getting different `WriteConcern` settings:

```java
public class MyAppWriteConcernResolver implements WriteConcernResolver {
@Override public WriteConcern resolve(MongoAction action) {if (action.getEntityType().getSimpleName().contains("Audit")) {return WriteConcern.ACKNOWLEDGED; } else if (action.getEntityType().getSimpleName().contains("Metadata")) {return WriteConcern.JOURNALED;} return action.getDefaultWriteConcern();}}
```

<a id="mongodb-template-config--mongo-template.entity-lifecycle-events"></a>
<a id="mongodb-template-config--publish-entity-lifecycle-events"></a>

## Publish entity lifecycle events

The template publishes [lifecycle events](#mongodb-lifecycle-events--mongodb.mapping-usage.events).
In case there are no listeners present, this feature can be disabled.

```java
@Bean
MongoOperations mongoTemplate(MongoClient mongoClient) {
    MongoTemplate template = new MongoTemplate(mongoClient, "geospatial");
	template.setEntityLifecycleEventsEnabled(false);
	// ...
}
```

<a id="mongodb-template-config--mongo-template.entity-callbacks-config"></a>
<a id="mongodb-template-config--configure-entitycallbacks"></a>

## Configure EntityCallbacks

Nest to lifecycle events the template invokes [EntityCallbacks](#mongodb-lifecycle-events--mongo.entity-callbacks) which can be (if not auto configured) set via the template API.

- Imperative
- Reactive

```java
@Bean
MongoOperations mongoTemplate(MongoClient mongoClient) {
    MongoTemplate template = new MongoTemplate(mongoClient, "...");
	template.setEntityCallbacks(EntityCallbacks.create(...));
	// ...
}
```

```java
@Bean
ReactiveMongoOperations mongoTemplate(MongoClient mongoClient) {
    ReactiveMongoTemplate template = new ReactiveMongoTemplate(mongoClient, "...");
	template.setEntityCallbacks(ReactiveEntityCallbacks.create(...));
	// ...
}
```

<a id="mongodb-template-config--mongo-template.count-documents-config"></a>
<a id="mongodb-template-config--document-count-configuration"></a>

## Document count configuration

By setting `MongoTemplate#useEstimatedCount(…)` to `true` *MongoTemplate#count(…)* operations, that use an empty filter query, will be delegated to `estimatedCount`, as long as there is no transaction active and the template is not bound to a [session](#mongodb-client-session-transactions).
Please refer to the [Counting Documents](#mongodb-template-document-count--mongo.query.count) section for more information.

---

<a id="mongodb-template-collection-management"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-collection-management.html -->

<!-- page_index: 13 -->

# Index and Collection Management

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-collection-management--page-title"></a>
<a id="mongodb-template-collection-management--index-and-collection-management"></a>

# Index and Collection Management

`MongoTemplate` and `ReactiveMongoTemplate` provide methods for managing indexes and collections.
These methods are collected into a helper interface called `IndexOperations` respectively `ReactiveIndexOperations`.
You can access these operations by calling the `indexOps` method and passing in either the collection name or the `java.lang.Class` of your entity (the collection name is derived from the `.class`, either by name or from annotation metadata).

The following listing shows the `IndexOperations` interface:

- Imperative
- Reactive

```java
public interface IndexOperations {

    String ensureIndex(IndexDefinition indexDefinition);

    void alterIndex(String name, IndexOptions options);

    void dropIndex(String name);

    void dropAllIndexes();

    List<IndexInfo> getIndexInfo();
}
```

```java
public interface ReactiveIndexOperations {

    Mono<String> ensureIndex(IndexDefinition indexDefinition);

    Mono<Void> alterIndex(String name, IndexOptions options);

    Mono<Void> dropIndex(String name);

    Mono<Void> dropAllIndexes();

    Flux<IndexInfo> getIndexInfo();
```

<a id="mongodb-template-collection-management--mongo-template.index-and-collections.index"></a>
<a id="mongodb-template-collection-management--methods-for-creating-an-index"></a>

## Methods for Creating an Index

You can create an index on a collection to improve query performance by using the MongoTemplate class, as the following example shows:

- Imperative
- Reactive

```java
template.indexOps(Person.class)
    .ensureIndex(new Index().on("name",Order.ASCENDING));
```

```java
Mono<String> createIndex = template.indexOps(Person.class)
    .ensureIndex(new Index().on("name",Order.ASCENDING));
```

`ensureIndex` makes sure that an index for the provided IndexDefinition exists for the collection.

You can create standard, geospatial, and text indexes by using the `IndexDefinition`, `GeoSpatialIndex` and `TextIndexDefinition` classes.
For example, given the `Venue` class defined in a previous section, you could declare a geospatial query, as the following example shows:

```java
template.indexOps(Venue.class)
    .ensureIndex(new GeospatialIndex("location"));
```

> [!NOTE]
> `Index` and `GeospatialIndex` support configuration of [collations](#mongodb-template-query-operations--mongo.query.collation).

<a id="mongodb-template-collection-management--mongo-template.index-and-collections.access"></a>
<a id="mongodb-template-collection-management--accessing-index-information"></a>

## Accessing Index Information

The `IndexOperations` interface has the `getIndexInfo` method that returns a list of `IndexInfo` objects.
This list contains all the indexes defined on the collection. The following example defines an index on the `Person` class that has an `age` property:

- Imperative
- Reactive

```java
template.indexOps(Person.class)
    .ensureIndex(new Index().on("age", Order.DESCENDING).unique());

List<IndexInfo> indexInfoList = template.indexOps(Person.class)
   .getIndexInfo();
```

```java
Mono<String> ageIndex = template.indexOps(Person.class)
    .ensureIndex(new Index().on("age", Order.DESCENDING).unique());

Flux<IndexInfo> indexInfo = ageIndex.then(template.indexOps(Person.class)
   .getIndexInfo());
```

<a id="mongodb-template-collection-management--mongo-template.index-and-collections.collection"></a>
<a id="mongodb-template-collection-management--methods-for-working-with-a-collection"></a>

## Methods for Working with a Collection

The following example shows how to create a collection:

- Imperative
- Reactive

```java
MongoCollection<Document> collection = null;
if (!template.getCollectionNames().contains("MyNewCollection")) {
    collection = mongoTemplate.createCollection("MyNewCollection");
}
```

```java
MongoCollection<Document> collection = template.getCollectionNames().collectList()
    .flatMap(collectionNames -> {
        if(!collectionNames.contains("MyNewCollection")) {
            return template.createCollection("MyNewCollection");
        }
        return template.getMongoDatabase().map(db -> db.getCollection("MyNewCollection"));
    });
```

> [!NOTE]
> Collection creation allows customization with `CollectionOptions` and supports [collations](https://docs.spring.io/spring-data/mongodb/reference/mongodb/collation.html).

<details>
<summary>Methods to interact with MongoCollections</summary>
<div>
<div>
<ul>
<li>
<p><strong>getCollectionNames</strong>: Returns a set of collection names.</p>
</li>
<li>
<p><strong>collectionExists</strong>: Checks to see if a collection with a given name exists.</p>
</li>
<li>
<p><strong>createCollection</strong>: Creates an uncapped collection.</p>
</li>
<li>
<p><strong>dropCollection</strong>: Drops the collection.</p>
</li>
<li>
<p><strong>getCollection</strong>: Gets a collection by name, creating it if it does not exist.</p>
</li>
</ul>
</div>
</div>
</details>

<a id="mongodb-template-collection-management--time-series"></a>

## Time Series

MongoDB 5.0 introduced [Time Series](https://docs.mongodb.com/manual/core/timeseries-collections/) collections that are optimized to efficiently store documents over time such as measurements or events.
Those collections need to be created as such before inserting any data.
Collections can be created by either running the `createCollection` command, defining time series collection options or extracting options from a `@TimeSeries` annotation as shown in the examples below.

Example 1. Create a Time Series Collection

Create a Time Series via the MongoDB Driver

```java
template.execute(db -> {

    com.mongodb.client.model.CreateCollectionOptions options = new CreateCollectionOptions();
    options.timeSeriesOptions(new TimeSeriesOptions("timestamp"));

    db.createCollection("weather", options);
    return "OK";
});
```

Create a Time Series Collection with `CollectionOptions`

```java
template.createCollection("weather", CollectionOptions.timeSeries("timestamp"));
```

Create a Time Series Collection derived from an Annotation

```java
@TimeSeries(collection="weather", timeField = "timestamp")
public class Measurement {

    String id;
    Instant timestamp;
    // ...
}

template.createCollection(Measurement.class);
```

The snippets above can easily be transferred to the reactive API offering the very same methods.
Make sure to properly *subscribe* to the returned publishers.

> [!TIP]
> You can use the `@TimeSeries#expireAfter` option to have MongoDB automatically remove expired buckets.
> The attribute allows different timeout formats like `10s`, `3h`,… as well as expression (`#{@mySpringBean.timeout}`) and property placeholder (`${my.property.timeout}`) syntax.

---

<a id="mongodb-template-crud-operations"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-crud-operations.html -->

<!-- page_index: 14 -->

# Saving, Updating, and Removing Documents

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-crud-operations--page-title"></a>
<a id="mongodb-template-crud-operations--saving-updating-and-removing-documents"></a>

# Saving, Updating, and Removing Documents

`MongoTemplate` / `ReactiveMongoTemplate` let you save, update, and delete your domain objects and map those objects to documents stored in MongoDB.
The API signatures of the imperative and reactive API are mainly the same only differing in their return types.
While the synchronous API uses `void`, single `Object` and `List` the reactive counterpart consists of `Mono<Void>`, `Mono<Object>` and `Flux`.

Consider the following class:

```java
public class Person {
private String id; private String name; private int age;
public Person(String name, int age) {this.name = name; this.age = age;}
public String getId() {return id;}
public String getName() {return name;}
public int getAge() {return age;}
@Override public String toString() {return "Person [id=" + id + ", name=" + name + ", age=" + age + "]";}}
```

Given the `Person` class in the preceding example, you can save, update and delete the object, as the following example shows:

- Imperative
- Reactive

```java
public class MongoApplication {

  private static final Log log = LogFactory.getLog(MongoApplication.class);

  public static void main(String[] args) {

    MongoOperations template = new MongoTemplate(new SimpleMongoClientDbFactory(MongoClients.create(), "database"));

    Person p = new Person("Joe", 34);

    // Insert is used to initially store the object into the database.
    template.insert(p);
    log.info("Insert: " + p);

    // Find
    p = template.findById(p.getId(), Person.class);
    log.info("Found: " + p);

    // Update
    template.updateFirst(query(where("name").is("Joe")), update("age", 35), Person.class);
    p = template.findOne(query(where("name").is("Joe")), Person.class);
    log.info("Updated: " + p);

    // Delete
    template.remove(p);

    // Check that deletion worked
    List<Person> people =  template.findAll(Person.class);
    log.info("Number of people = : " + people.size());


    template.dropCollection(Person.class);
  }
}
```

The preceding example would produce the following log output (including debug messages from `MongoTemplate`):

```none
DEBUG apping.MongoPersistentEntityIndexCreator:  80 - Analyzing class class org.spring.example.Person for index information.
DEBUG work.data.mongodb.core.MongoTemplate: 632 - insert Document containing fields: [_class, age, name] in collection: person
INFO               org.spring.example.MongoApp:  30 - Insert: Person [id=4ddc6e784ce5b1eba3ceaf5c, name=Joe, age=34]
DEBUG work.data.mongodb.core.MongoTemplate:1246 - findOne using query: { "_id" : { "$oid" : "4ddc6e784ce5b1eba3ceaf5c"}} in db.collection: database.person
INFO               org.spring.example.MongoApp:  34 - Found: Person [id=4ddc6e784ce5b1eba3ceaf5c, name=Joe, age=34]
DEBUG work.data.mongodb.core.MongoTemplate: 778 - calling update using query: { "name" : "Joe"} and update: { "$set" : { "age" : 35}} in collection: person
DEBUG work.data.mongodb.core.MongoTemplate:1246 - findOne using query: { "name" : "Joe"} in db.collection: database.person
INFO               org.spring.example.MongoApp:  39 - Updated: Person [id=4ddc6e784ce5b1eba3ceaf5c, name=Joe, age=35]
DEBUG work.data.mongodb.core.MongoTemplate: 823 - remove using query: { "id" : "4ddc6e784ce5b1eba3ceaf5c"} in collection: person
INFO               org.spring.example.MongoApp:  46 - Number of people = : 0
DEBUG work.data.mongodb.core.MongoTemplate: 376 - Dropped collection [database.person]
```

```java
public class ReactiveMongoApplication {

  private static final Logger log = LoggerFactory.getLogger(ReactiveMongoApplication.class);

  public static void main(String[] args) throws Exception {

    CountDownLatch latch = new CountDownLatch(1);

    ReactiveMongoTemplate template = new ReactiveMongoTemplate(MongoClients.create(), "database");

    template.insert(new Person("Joe", 34)).doOnNext(person -> log.info("Insert: " + person))
      .flatMap(person -> template.findById(person.getId(), Person.class))
      .doOnNext(person -> log.info("Found: " + person))
      .zipWith(person -> template.updateFirst(query(where("name").is("Joe")), update("age", 35), Person.class))
      .flatMap(tuple -> template.remove(tuple.getT1())).flatMap(deleteResult -> template.findAll(Person.class))
      .count().doOnSuccess(count -> {
        log.info("Number of people: " + count);
        latch.countDown();
      })

      .subscribe();

    latch.await();
  }
}
```

`MongoConverter` caused implicit conversion between a `String` and an `ObjectId` stored in the database by recognizing (through convention) the `Id` property name.

The preceding example is meant to show the use of save, update, and remove operations on `MongoTemplate` / `ReactiveMongoTemplate` and not to show complex mapping functionality.
The query syntax used in the preceding example is explained in more detail in the section “[Querying Documents](#mongodb-template-query-operations)”.

> [!IMPORTANT]
> MongoDB requires that you have an `_id` field for all documents.
> Please refer to the [ID handling](#mongodb-template-crud-operations) section for details on the special treatment of this field.

> [!IMPORTANT]
> MongoDB collections can contain documents that represent instances of a variety of types.
> Please refer to the [type mapping](https://docs.spring.io/spring-data/mongodb/reference/mongodb/converters-type-mapping.html) for details.

<a id="mongodb-template-crud-operations--mongo-template.save-insert"></a>
<a id="mongodb-template-crud-operations--insert-save"></a>

## Insert / Save

There are several convenient methods on `MongoTemplate` for saving and inserting your objects.
To have more fine-grained control over the conversion process, you can register Spring converters with the `MappingMongoConverter` — for example `Converter<Person, Document>` and `Converter<Document, Person>`.

> [!NOTE]
> The difference between insert and save operations is that a save operation performs an insert if the object is not already present.

The simple case of using the save operation is to save a POJO.
In this case, the collection name is determined by name (not fully qualified) of the class.
You may also call the save operation with a specific collection name.
You can use mapping metadata to override the collection in which to store the object.

When inserting or saving, if the `Id` property is not set, the assumption is that its value will be auto-generated by the database.
Consequently, for auto-generation of an `ObjectId` to succeed, the type of the `Id` property or field in your class must be a `String`, an `ObjectId`, or a `BigInteger`.

The following example shows how to save a document and retrieving its contents:

Inserting and retrieving documents using the MongoTemplate

- Imperative
- Reactive

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import static org.springframework.data.mongodb.core.query.Criteria.query;

//...

template.insert(new Person("Bob", 33));

Person person = template.query(Person.class)
    .matching(query(where("age").is(33)))
    .oneValue();
```

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import static org.springframework.data.mongodb.core.query.Criteria.query;

//...

Mono<Person> person = mongoTemplate.insert(new Person("Bob", 33))
    .then(mongoTemplate.query(Person.class)
        .matching(query(where("age").is(33)))
        .one());
```

The following insert and save operations are available:

- `void` **save** `(Object objectToSave)`: Save the object to the default collection.
- `void` **save** `(Object objectToSave, String collectionName)`: Save the object to the specified collection.

A similar set of insert operations is also available:

- `void` **insert** `(Object objectToSave)`: Insert the object to the default collection.
- `void` **insert** `(Object objectToSave, String collectionName)`: Insert the object to the specified collection.

<a id="mongodb-template-crud-operations--mongo-template.id-handling"></a>
<a id="mongodb-template-crud-operations--how-the-_id-field-is-handled-in-the-mapping-layer"></a>

### How the `_id` Field is Handled in the Mapping Layer

MongoDB requires that you have an `_id` field for all documents.
If you do not provide one, the driver assigns an `ObjectId` with a generated value without considering your domain model as the server isn’t aware of your identifier type.
When you use the `MappingMongoConverter`, certain rules govern how properties from the Java class are mapped to this `_id` field:

1. A property or field annotated with `@Id` (`org.springframework.data.annotation.Id`) maps to the `_id` field.
2. A property or field without an annotation but named `id` maps to the `_id` field.

The following outlines what type conversion, if any, is done on the property mapped to the `_id` document field when using the `MappingMongoConverter` (the default for `MongoTemplate`).

1. If possible, an `id` property or field declared as a `String` in the Java class is converted to and stored as an `ObjectId` by using a Spring `Converter<String, ObjectId>`.
   Valid conversion rules are delegated to the MongoDB Java driver.
   If it cannot be converted to an `ObjectId`, then the value is stored as a string in the database.
2. An `id` property or field declared as `Date` is converted to and stored as `ObjectId`.
3. An `id` property or field declared as `BigInteger` in the Java class is converted to and stored as an `ObjectId` by using a Spring `Converter<BigInteger, ObjectId>`.

If no field or property specified in the previous sets of rules is present in the Java class, an implicit `_id` file is generated by the driver but not mapped to a property or field of the Java class.

When querying and updating, `MongoTemplate` uses the converter that corresponds to the preceding rules for saving documents so that field names and types used in your queries can match what is in your domain classes.

Some environments require a customized approach to map `Id` values such as data stored in MongoDB that did not run through the Spring Data mapping layer.
Documents can contain `_id` values that can be represented either as `ObjectId` or as `String`.
Reading documents from the store back to the domain type works just fine.
Querying for documents via their `id` can be cumbersome due to the implicit `ObjectId` conversion.
Therefore documents cannot be retrieved that way.
For those cases `@MongoId` provides more control over the actual id mapping attempts.

Example 1. `@MongoId` mapping

```java
public class PlainStringId {@MongoId String id; (1)}
public class PlainObjectId {@MongoId ObjectId id; (2)}
public class StringToObjectId {@MongoId(FieldType.OBJECT_ID) String id; (3)}
```

| **1** | The id is treated as `String` without further conversion. |
| --- | --- |
| **2** | The id is treated as `ObjectId`. |
| **3** | The id is treated as `ObjectId` if the given `String` is a valid `ObjectId` hex, otherwise as `String`. Corresponds to `@Id` usage. |

<a id="mongodb-template-crud-operations--mongo-template.save-insert.collection"></a>
<a id="mongodb-template-crud-operations--into-which-collection-are-my-documents-saved"></a>

### Into Which Collection Are My Documents Saved?

There are two ways to manage the collection name that is used for the documents.
The default collection name that is used is the class name changed to start with a lower-case letter.
So a `com.test.Person` class is stored in the `person` collection.
You can customize this by providing a different collection name with the `@Document` annotation.
You can also override the collection name by providing your own collection name as the last parameter for the selected `MongoTemplate` method calls.

<a id="mongodb-template-crud-operations--mongo-template.save-insert.individual"></a>
<a id="mongodb-template-crud-operations--inserting-or-saving-individual-objects"></a>

### Inserting or Saving Individual Objects

The MongoDB driver supports inserting a collection of documents in a single operation.
The following methods in the `MongoOperations` interface support this functionality:

- **insert**: Inserts an object.
  If there is an existing document with the same `id`, an error is generated.
- **insertAll**: Takes a `Collection` of objects as the first parameter.
  This method inspects each object and inserts it into the appropriate collection, based on the rules specified earlier.
- **save**: Saves the object, overwriting any object that might have the same `id`.

<a id="mongodb-template-crud-operations--mongo-template.save-insert.batch"></a>
<a id="mongodb-template-crud-operations--inserting-several-objects-in-a-batch"></a>

### Inserting Several Objects in a Batch

The MongoDB driver supports inserting a collection of documents in one operation.
The following methods in the `MongoOperations` interface support this functionality via `insert`, `bulkWrite` (requires MongoDB 8.0+) or a dedicated `BulkOperations` interface.

Batch Insert

- Imperative
- Reactive

```java
Collection<Person> inserted = template.insert(List.of(...), Person.class);
```

```java
Flux<Person> inserted = template.insert(List.of(...), Person.class);
```

<a id="mongodb-template-crud-operations--_bulk_writes"></a>
<a id="mongodb-template-crud-operations--bulk-writes"></a>

#### Bulk Writes

BulkWrite allows you to perform insert, update, and delete operations using a single request.

> [!NOTE]
> MongoDB 8.0 introduced BulkWrite across multiple collections.
>
> Use `bulkWrite(Bulk, BulkWriteOptions)` when you need a single request with mixed insert, update, and delete operations, optionally across multiple collections (MongoDB 8.0+).
> If your targeting a single collection you’ll still be able to leverage the new `bulkWrite` method with older MongoDB server version, or keep using the classic `bulkOps(BulkMode, Class)` API.

BulkWrite (multiple collections)

- Imperative
- Reactive

```java
Bulk bulk = Bulk.create(builder -> builder
        .inCollection(Person.class, spec -> spec
                .insert(person1)
                .insert(person2)
                .upsert(where("_id").is("..."), new Update().set("firstname", "...")))
        .inCollection(User.class, spec -> spec.insert(new User("..."))));

BulkWriteResult result = template.bulkWrite(bulk, BulkWriteOptions.ordered());
```

```java
Bulk bulk = Bulk.create(builder -> builder
        .inCollection(Person.class, spec -> spec
                .insert(person1)
                .insert(person2)
                .upsert(where("_id").is("..."), new Update().set("firstname", "...")))
        .inCollection(User.class, spec -> spec.insert(new User("..."))));

template.bulkWrite(bulk, BulkWriteOptions.ordered()).subscribe();
```

BulkWrite (single collection)

- Imperative
- Reactive

```java
BulkWriteResult result = template.bulkOps(BulkMode.ORDERED, Person.class)
    .insert(List.of(...))
    .execute();
```

```java
Mono<BulkWriteResult> result = template.bulkOps(BulkMode.ORDERED, Person.class)
    .insert(List.of(...))
    .execute();
```

> [!NOTE]
> Server performance for individual operations of batch and bulk is identical.
> Bulk however uses less resources since it can operate upon a single request.
> [Lifecycle events](#mongodb-lifecycle-events) publishing is limited for bulk operations.

> [!IMPORTANT]
> Any `@Version` property that has not been set prior to calling insert will be auto initialized with `1` (in case of a simple type like `int`) or `0` for wrapper types (eg. `Integer`).
> Read more in the [Optimistic Locking](#mongodb-template-crud-operations--mongo-template.optimistic-locking) section.

<a id="mongodb-template-crud-operations--mongodb-template-update"></a>
<a id="mongodb-template-crud-operations--update"></a>

## Update

For updates, you can update the first document found by using `MongoOperations.updateFirst` or you can update all documents that were found to match the query by using the `MongoOperations.updateMulti` method or `all` on the fluent API.
The following example shows an update of all `SAVINGS` accounts where we are adding a one-time $50.00 bonus to the balance by using the `$inc` operator:

Updating documents by using the `MongoTemplate` / `ReactiveMongoTemplate`

- Imperative
- Reactive

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import org.springframework.data.mongodb.core.query.Update;

// ...

UpdateResult result = template.update(Account.class)
    .matching(where("accounts.accountType").is(Type.SAVINGS))
    .apply(new Update().inc("accounts.$.balance", 50.00))
    .all();
```

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import org.springframework.data.mongodb.core.query.Update;

// ...

Mono<UpdateResult> result = template.update(Account.class)
    .matching(where("accounts.accountType").is(Type.SAVINGS))
    .apply(new Update().inc("accounts.$.balance", 50.00))
    .all();
```

In addition to the `Query` discussed earlier, we provide the update definition by using an `Update` object.
The `Update` class has methods that match the update modifiers available for MongoDB.
Most methods return the `Update` object to provide a fluent style for the API.

> [!IMPORTANT]
> `@Version` properties if not included in the `Update` will be automatically incremented.
> Read more in the [Optimistic Locking](#mongodb-template-crud-operations--mongo-template.optimistic-locking) section.

<a id="mongodb-template-crud-operations--mongodb-template-update.methods"></a>
<a id="mongodb-template-crud-operations--methods-for-running-updates-for-documents"></a>

### Methods for Running Updates for Documents

- **updateFirst**: Updates the first document that matches the query document criteria with the updated document.
- **updateMulti**: Updates all objects that match the query document criteria with the updated document.

> [!WARNING]
> `updateFirst` does not support ordering for MongoDB Versions below 8.0. Running one of the older versions, please use [findAndModify](#mongodb-template-crud-operations--mongo-template.find-and-upsert) to apply `Sort`.

> [!NOTE]
> Index hints for the update operation can be provided via `Query.withHint(…)`.

<a id="mongodb-template-crud-operations--mongodb-template-update.update"></a>
<a id="mongodb-template-crud-operations--methods-in-the-update-class"></a>

### Methods in the `Update` Class

You can use a little "'syntax sugar'" with the `Update` class, as its methods are meant to be chained together.
Also, you can kick-start the creation of a new `Update` instance by using `public static Update update(String key, Object value)` and using static imports.

The `Update` class contains the following methods:

- `Update` **addToSet** `(String key, Object value)` Update using the `$addToSet` update modifier
- `Update` **currentDate** `(String key)` Update using the `$currentDate` update modifier
- `Update` **currentTimestamp** `(String key)` Update using the `$currentDate` update modifier with `$type` `timestamp`
- `Update` **inc** `(String key, Number inc)` Update using the `$inc` update modifier
- `Update` **max** `(String key, Object max)` Update using the `$max` update modifier
- `Update` **min** `(String key, Object min)` Update using the `$min` update modifier
- `Update` **multiply** `(String key, Number multiplier)` Update using the `$mul` update modifier
- `Update` **pop** `(String key, Update.Position pos)` Update using the `$pop` update modifier
- `Update` **pull** `(String key, Object value)` Update using the `$pull` update modifier
- `Update` **pullAll** `(String key, Object[] values)` Update using the `$pullAll` update modifier
- `Update` **push** `(String key, Object value)` Update using the `$push` update modifier
- `Update` **pushAll** `(String key, Object[] values)` Update using the `$pushAll` update modifier
- `Update` **rename** `(String oldName, String newName)` Update using the `$rename` update modifier
- `Update` **set** `(String key, Object value)` Update using the `$set` update modifier
- `Update` **setOnInsert** `(String key, Object value)` Update using the `$setOnInsert` update modifier
- `Update` **unset** `(String key)` Update using the `$unset` update modifier

Some update modifiers, such as `$push` and `$addToSet`, allow nesting of additional operators.

```java
// { $push : { "category" : { "$each" : [ "spring" , "data" ] } } }
new Update().push("category").each("spring", "data")

// { $push : { "key" : { "$position" : 0 , "$each" : [ "Arya" , "Arry" , "Weasel" ] } } }
new Update().push("key").atPosition(Position.FIRST).each(Arrays.asList("Arya", "Arry", "Weasel"));

// { $push : { "key" : { "$slice" : 5 , "$each" : [ "Arya" , "Arry" , "Weasel" ] } } }
new Update().push("key").slice(5).each(Arrays.asList("Arya", "Arry", "Weasel"));

// { $addToSet : { "values" : { "$each" : [ "spring" , "data" , "mongodb" ] } } }
new Update().addToSet("values").each("spring", "data", "mongodb");
```

<a id="mongodb-template-crud-operations--mongo-template.aggregation-update"></a>
<a id="mongodb-template-crud-operations--aggregation-pipeline-updates"></a>

### Aggregation Pipeline Updates

Update methods exposed by `MongoOperations` and `ReactiveMongoOperations` also accept an [Aggregation Pipeline](#mongodb-aggregation-framework) via `AggregationUpdate`.
Using `AggregationUpdate` allows leveraging [MongoDB 4.2 aggregations](https://docs.mongodb.com/manual/reference/method/db.collection.update/#update-with-aggregation-pipeline) in an update operation.
Using aggregations in an update allows updating one or more fields by expressing multiple stages and multiple conditions with a single operation.

The update can consist of the following stages:

- `AggregationUpdate.set(…).toValue(…)` → `$set : { … }`
- `AggregationUpdate.unset(…)` → `$unset : [ … ]`
- `AggregationUpdate.replaceWith(…)` → `$replaceWith : { … }`

Example 2. Update Aggregation

```java
AggregationUpdate update = Aggregation.newUpdate()
    .set("average").toValue(ArithmeticOperators.valueOf("tests").avg())     (1)
    .set("grade").toValue(ConditionalOperators.switchCases(                 (2)
        when(valueOf("average").greaterThanEqualToValue(90)).then("A"),
        when(valueOf("average").greaterThanEqualToValue(80)).then("B"),
        when(valueOf("average").greaterThanEqualToValue(70)).then("C"),
        when(valueOf("average").greaterThanEqualToValue(60)).then("D"))
        .defaultTo("F")
    );

template.update(Student.class)                                              (3)
    .apply(update)
    .all();                                                                 (4)
```

```javascript
db.students.update(                                                         (3) { },[{ $set: { average : { $avg: "$tests" } } },                            (1) { $set: { grade: { $switch: {                                          (2) branches: [{ case: { $gte: [ "$average", 90 ] }, then: "A" },{ case: { $gte: [ "$average", 80 ] }, then: "B" },{ case: { $gte: [ "$average", 70 ] }, then: "C" },{ case: { $gte: [ "$average", 60 ] }, then: "D" } ],default: "F" } } } } ],{ multi: true }                                                          (4))
```

**1**

The 1st `$set` stage calculates a new field *average* based on the average of the *tests* field.

**2**

The 2nd `$set` stage calculates a new field *grade* based on the *average* field calculated by the first aggregation stage.

**3**

The pipeline is run on the *students* collection and uses `Student` for the aggregation field mapping.

**4**

Apply the update to all matching documents in the collection.

<a id="mongodb-template-crud-operations--mongo-template.upserts"></a>
<a id="mongodb-template-crud-operations--upsert"></a>

## Upsert

Related to performing an `updateFirst` operation, you can also perform an `upsert` operation, which will perform an insert if no document is found that matches the query.
The document that is inserted is a combination of the query document and the update document.
The following example shows how to use the `upsert` method:

- Imperative
- Reactive

```java
UpdateResult result = template.update(Person.class)
  .matching(query(where("ssn").is(1111).and("firstName").is("Joe").and("Fraizer").is("Update"))
  .apply(update("address", addr))
  .upsert();
```

```java
Mono<UpdateResult> result = template.update(Person.class)
  .matching(query(where("ssn").is(1111).and("firstName").is("Joe").and("Fraizer").is("Update"))
  .apply(update("address", addr))
  .upsert();
```

> [!WARNING]
> `upsert` does not support ordering.
> Please use [findAndModify](#mongodb-template-crud-operations--mongo-template.find-and-upsert) to apply `Sort`.

> [!IMPORTANT]
> `@Version` properties if not included in the `Update` will be automatically initialized.
> Read more in the [Optimistic Locking](#mongodb-template-crud-operations--mongo-template.optimistic-locking) section.

<a id="mongodb-template-crud-operations--mongo-template.replace"></a>
<a id="mongodb-template-crud-operations--replacing-documents-in-a-collection"></a>

### Replacing Documents in a Collection

The various `replace` methods available via `MongoTemplate` allow to override the first matching Document.
If no match is found a new one can be upserted (as outlined in the previous section) by providing `ReplaceOptions` with according configuration.

Replace one

```java
Person tom = template.insert(new Person("Motte", 21)); (1)
Query query = Query.query(Criteria.where("firstName").is(tom.getFirstName())); (2)
tom.setFirstname("Tom"); (3)
template.replace(query, tom, ReplaceOptions.none()); (4)
```

| **1** | Insert a new document. |
| --- | --- |
| **2** | The query used to identify the single document to replace. |
| **3** | Set up the replacement document which must hold either the same `_id` as the existing or no `_id` at all. |
| **4** | Run the replace operation. .Replace one with upsert |

```java
Person tom = new Person("id-123", "Tom", 21) (1)
Query query = Query.query(Criteria.where("firstName").is(tom.getFirstName()));
template.replace(query, tom, ReplaceOptions.replaceOptions().upsert()); (2)
```

**1**

The `_id` value needs to be present for upsert, otherwise MongoDB will create a new potentially with the domain type incompatible `ObjectId`.
As MongoDB is not aware of your domain type, any `@Field(targetType)` hints are not considered and the resulting `ObjectId` might be not compatible with your domain model.

**2**

Use `upsert` to insert a new document if no match is found

> [!WARNING]
> It is not possible to change the `_id` of existing documents with a replace operation.
> On `upsert` MongoDB uses 2 ways of determining the new id for the entry:
> \* The `_id` is used within the query as in `{"_id" : 1234 }`
> \* The `_id` is present in the replacement document.
> If no `_id` is provided in either way, MongoDB will create a new `ObjectId` for the document.
> This may lead to mapping and data lookup malfunctions if the used domain types `id` property has a different type like e.g. `Long`.

<a id="mongodb-template-crud-operations--mongo-template.find-and-upsert"></a>
<a id="mongodb-template-crud-operations--find-and-modify"></a>

## Find and Modify

The `findAndModify(…)` method on `MongoCollection` can update a document and return either the old or newly updated document in a single operation.
`MongoTemplate` provides four `findAndModify` overloaded methods that take `Query` and `Update` classes and converts from `Document` to your POJOs:

```java
<T> T findAndModify(Query query, Update update, Class<T> entityClass);

<T> T findAndModify(Query query, Update update, Class<T> entityClass, String collectionName);

<T> T findAndModify(Query query, Update update, FindAndModifyOptions options, Class<T> entityClass);

<T> T findAndModify(Query query, Update update, FindAndModifyOptions options, Class<T> entityClass, String collectionName);
```

The following example inserts a few `Person` objects into the container and performs a `findAndUpdate` operation:

```java
template.insert(new Person("Tom", 21));
template.insert(new Person("Dick", 22));
template.insert(new Person("Harry", 23));

Query query = new Query(Criteria.where("firstName").is("Harry"));
Update update = new Update().inc("age", 1);

Person oldValue = template.update(Person.class)
  .matching(query)
  .apply(update)
  .findAndModifyValue(); // oldValue.age == 23

Person newValue = template.query(Person.class)
  .matching(query)
  .findOneValue(); // newValye.age == 24

Person newestValue = template.update(Person.class)
  .matching(query)
  .apply(update)
  .withOptions(FindAndModifyOptions.options().returnNew(true)) // Now return the newly updated document when updating
  .findAndModifyValue(); // newestValue.age == 25
```

The `FindAndModifyOptions` method lets you set the options of `returnNew`, `upsert`, and `remove`.
An example extending from the previous code snippet follows:

```java
Person upserted = template.update(Person.class)
  .matching(new Query(Criteria.where("firstName").is("Mary")))
  .apply(update)
  .withOptions(FindAndModifyOptions.options().upsert(true).returnNew(true))
  .findAndModifyValue()
```

> [!IMPORTANT]
> `@Version` properties if not included in the `Update` will be automatically incremented.
> Read more in the [Optimistic Locking](#mongodb-template-crud-operations--mongo-template.optimistic-locking) section.

<a id="mongodb-template-crud-operations--mongo-template.find-and-replace"></a>
<a id="mongodb-template-crud-operations--find-and-replace"></a>

## Find and Replace

The most straight forward method of replacing an entire `Document` is via its `id` using the `save` method.
However this might not always be feasible.
`findAndReplace` offers an alternative that allows to identify the document to replace via a simple query.

Example 3. Find and Replace Documents

```java
Optional<User> result = template.update(Person.class)      (1)
    .matching(query(where("firstname").is("Tom")))          (2)
    .replaceWith(new Person("Dick"))
    .withOptions(FindAndReplaceOptions.options().upsert()) (3)
    .as(User.class)                                        (4)
    .findAndReplace();                                     (5)
```

**1**

Use the fluent update API with the domain type given for mapping the query and deriving the collection name or just use `MongoOperations#findAndReplace`.

**2**

The actual match query mapped against the given domain type.
Provide `sort`, `fields` and `collation` settings via the query.

**3**

Additional optional hook to provide options other than the defaults, like `upsert`.

**4**

An optional projection type used for mapping the operation result.
If none given the initial domain type is used.

**5**

Trigger the actual processing.
Use `findAndReplaceValue` to obtain the nullable result instead of an `Optional`.

> [!IMPORTANT]
> Please note that the replacement must not hold an `id` itself as the `id` of the existing `Document` will be carried over to the replacement by the store itself.
> Also keep in mind that `findAndReplace` will only replace the first document matching the query criteria depending on a potentially given sort order.

<a id="mongodb-template-crud-operations--mongo-template.delete"></a>
<a id="mongodb-template-crud-operations--delete"></a>

## Delete

You can use one of five overloaded methods to remove an object from the database:

```java
template.remove(tywin, "GOT");                                              (1)

template.remove(query(where("lastname").is("lannister")), "GOT");           (2)

template.remove(new Query().limit(3), "GOT");                               (3)

template.findAllAndRemove(query(where("lastname").is("lannister"), "GOT");  (4)

template.findAllAndRemove(new Query().limit(3), "GOT");                     (5)
```

| **1** | Remove a single entity specified by its `_id` from the associated collection. |
| --- | --- |
| **2** | Remove all documents that match the criteria of the query from the `GOT` collection. |
| **3** | Remove the first three documents in the `GOT` collection. Unlike <2>, the documents to remove are identified by their `_id`, running the given query, applying `sort`, `limit`, and `skip` options first, and then removing all at once in a separate step. |
| **4** | Remove all documents matching the criteria of the query from the `GOT` collection. Unlike <3>, documents do not get deleted in a batch but one by one. |
| **5** | Remove the first three documents in the `GOT` collection. Unlike <3>, documents do not get deleted in a batch but one by one. |

<a id="mongodb-template-crud-operations--mongo-template.optimistic-locking"></a>
<a id="mongodb-template-crud-operations--optimistic-locking"></a>

## Optimistic Locking

The `@Version` annotation provides syntax similar to that of JPA in the context of MongoDB and makes sure updates are only applied to documents with a matching version.
Therefore, the actual value of the version property is added to the update query in such a way that the update does not have any effect if another operation altered the document in the meantime.
In that case, an `OptimisticLockingFailureException` is thrown.
The following example shows these features:

```java
@Document
class Person {

  @Id String id;
  String firstname;
  String lastname;
  @Version Long version;
}

Person daenerys = template.insert(new Person("Daenerys"));                            (1)

Person tmp = template.findOne(query(where("id").is(daenerys.getId())), Person.class); (2)

daenerys.setLastname("Targaryen");
template.save(daenerys);                                                              (3)

template.save(tmp); // throws OptimisticLockingFailureException                       (4)
```

| **1** | Initially insert document. `version` is set to `0`. |
| --- | --- |
| **2** | Load the just inserted document. `version` is still `0`. |
| **3** | Update the document with `version = 0`. Set the `lastname` and bump `version` to `1`. |
| **4** | Try to update the previously loaded document that still has `version = 0`. The operation fails with an `OptimisticLockingFailureException`, as the current `version` is `1`. |

Only certain CRUD operations on `MongoTemplate` do consider and alter version properties.
Please consult `MongoOperations` java doc for detailed information.

> [!NOTE]
> Optimistic Locking requires write acknowledgement (a write result response) by the server.
> Using `WriteConcern.UNACKNOWLEDGED` can lead to silently swallowed `OptimisticLockingFailureException`.

> [!NOTE]
> As of Version 2.2 `MongoOperations` also includes the `@Version` property when removing an entity from the database.
> To remove a `Document` without version check use `MongoOperations#remove(Query,…)` instead of `MongoOperations#remove(Object)`.

> [!NOTE]
> As of Version 2.2 repositories check for the outcome of acknowledged deletes when removing versioned entities.
> An `OptimisticLockingFailureException` is raised if a versioned entity cannot be deleted through `CrudRepository.delete(Object)`.
> In such case, the version was changed or the object was deleted in the meantime.
> Use `CrudRepository.deleteById(ID)` to bypass optimistic locking functionality and delete objects regardless of their version.

---

<a id="mongodb-template-query-operations"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-query-operations.html -->

<!-- page_index: 15 -->

# Querying Documents

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-query-operations--page-title"></a>
<a id="mongodb-template-query-operations--querying-documents"></a>

# Querying Documents

You can use the `Query` and `Criteria` classes to express your queries.
They have method names that mirror the native MongoDB operator names, such as `lt`, `lte`, `is`, and others.
The `Query` and `Criteria` classes follow a fluent API style so that you can chain together multiple method criteria and queries while having easy-to-understand code.
To improve readability, static imports let you avoid using the 'new' keyword for creating `Query` and `Criteria` instances.
You can also use `BasicQuery` to create `Query` instances from plain JSON Strings, as shown in the following example:

Example 1. Creating a Query instance from a plain JSON String

```java
BasicQuery query = new BasicQuery("{ age : { $lt : 50 }, accounts.balance : { $gt : 1000.00 }}");
List<Person> result = mongoTemplate.find(query, Person.class);
```

<a id="mongodb-template-query-operations--mongodb-template-query"></a>
<a id="mongodb-template-query-operations--querying-documents-in-a-collection"></a>

## Querying Documents in a Collection

Earlier, we saw how to retrieve a single document by using the `findOne` and `findById` methods on `MongoTemplate`.
These methods return a single domain object right way or using a reactive API a `Mono` emitting a single element.
We can also query for a collection of documents to be returned as a list of domain objects.
Assuming that we have a number of `Person` objects with name and age stored as documents in a collection and that each person has an embedded account document with a balance, we can now run a query using the following code:

Querying for documents using the MongoTemplate

- Imperative
- Reactive

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import static org.springframework.data.mongodb.core.query.Query.query;

// ...

List<Person> result = template.query(Person.class)
  .matching(query(where("age").lt(50).and("accounts.balance").gt(1000.00d)))
  .all();
```

```java
import static org.springframework.data.mongodb.core.query.Criteria.where;
import static org.springframework.data.mongodb.core.query.Query.query;

// ...

Flux<Person> result = template.query(Person.class)
  .matching(query(where("age").lt(50).and("accounts.balance").gt(1000.00d)))
  .all();
```

All find methods take a `Query` object as a parameter.
This object defines the criteria and options used to perform the query.
The criteria are specified by using a `Criteria` object that has a static factory method named `where` to instantiate a new `Criteria` object.
We recommend using static imports for `org.springframework.data.mongodb.core.query.Criteria.where` and `Query.query` to make the query more readable.

The query should return a `List` or `Flux` of `Person` objects that meet the specified criteria.
The rest of this section lists the methods of the `Criteria` and `Query` classes that correspond to the operators provided in MongoDB.
Most methods return the `Criteria` object, to provide a fluent style for the API.

<details id="mongodb-template-query.criteria">
<summary>Methods of the Criteria Class</summary>
<div>
<div>
<p>The <code>Criteria</code> class provides the following methods, all of which correspond to operators in MongoDB:</p>
</div>
<div>
<ul>
<li>
<p><code>Criteria</code> <strong>all</strong> <code>(Object o)</code> Creates a criterion using the <code>$all</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>and</strong> <code>(String key)</code> Adds a chained <code>Criteria</code> with the specified <code>key</code> to the current <code>Criteria</code> and returns the newly created one</p>
</li>
<li>
<p><code>Criteria</code> <strong>andOperator</strong> <code>(Criteria… criteria)</code> Creates an and query using the <code>$and</code> operator for all of the provided criteria (requires MongoDB 2.0 or later)</p>
</li>
<li>
<p><code>Criteria</code> <strong>andOperator</strong> <code>(Collection&lt;Criteria&gt; criteria)</code> Creates an and query using the <code>$and</code> operator for all of the provided criteria (requires MongoDB 2.0 or later)</p>
</li>
<li>
<p><code>Criteria</code> <strong>elemMatch</strong> <code>(Criteria c)</code> Creates a criterion using the <code>$elemMatch</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>exists</strong> <code>(boolean b)</code> Creates a criterion using the <code>$exists</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>gt</strong> <code>(Object o)</code> Creates a criterion using the <code>$gt</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>gte</strong> <code>(Object o)</code> Creates a criterion using the <code>$gte</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>in</strong> <code>(Object… o)</code> Creates a criterion using the <code>$in</code> operator for a varargs argument.</p>
</li>
<li>
<p><code>Criteria</code> <strong>in</strong> <code>(Collection&lt;?&gt; collection)</code> Creates a criterion using the <code>$in</code> operator using a collection</p>
</li>
<li>
<p><code>Criteria</code> <strong>is</strong> <code>(Object o)</code> Creates a criterion using field matching (<code>{ key:value }</code>). If the specified value is a document, the order of the fields and exact equality in the document matters.</p>
</li>
<li>
<p><code>Criteria</code> <strong>lt</strong> <code>(Object o)</code> Creates a criterion using the <code>$lt</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>lte</strong> <code>(Object o)</code> Creates a criterion using the <code>$lte</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>mod</strong> <code>(Number value, Number remainder)</code> Creates a criterion using the <code>$mod</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>ne</strong> <code>(Object o)</code> Creates a criterion using the <code>$ne</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>nin</strong> <code>(Object… o)</code> Creates a criterion using the <code>$nin</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>norOperator</strong> <code>(Criteria… criteria)</code> Creates an nor query using the <code>$nor</code> operator for all of the provided criteria</p>
</li>
<li>
<p><code>Criteria</code> <strong>norOperator</strong> <code>(Collection&lt;Criteria&gt; criteria)</code> Creates an nor query using the <code>$nor</code> operator for all of the provided criteria</p>
</li>
<li>
<p><code>Criteria</code> <strong>not</strong> <code>()</code> Creates a criterion using the <code>$not</code> meta operator which affects the clause directly following</p>
</li>
<li>
<p><code>Criteria</code> <strong>orOperator</strong> <code>(Criteria… criteria)</code> Creates an or query using the <code>$or</code> operator for all of the provided  criteria</p>
</li>
<li>
<p><code>Criteria</code> <strong>orOperator</strong> <code>(Collection&lt;Criteria&gt; criteria)</code> Creates an or query using the <code>$or</code> operator for all of the provided  criteria</p>
</li>
<li>
<p><code>Criteria</code> <strong>regex</strong> <code>(String re)</code> Creates a criterion using a <code>$regex</code></p>
</li>
<li>
<p><code>Criteria</code> <strong>sampleRate</strong> <code>(double sampleRate)</code> Creates a criterion using the <code>$sampleRate</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>size</strong> <code>(int s)</code> Creates a criterion using the <code>$size</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>type</strong> <code>(int t)</code> Creates a criterion using the <code>$type</code> operator</p>
</li>
<li>
<p><code>Criteria</code> <strong>matchingDocumentStructure</strong> <code>(MongoJsonSchema schema)</code> Creates a criterion using the <code>$jsonSchema</code> operator for <a href="#mongodb-mapping-mapping-schema">JSON schema criteria</a>. <code>$jsonSchema</code> can only be applied on the top level of a query and not property specific. Use the <code>properties</code> attribute of the schema to match against nested fields.</p>
</li>
<li>
<p><code>Criteria</code> <strong>bits()</strong> is the gateway to <a href="https://docs.mongodb.com/manual/reference/operator/query-bitwise/">MongoDB bitwise query operators</a> like <code>$bitsAllClear</code>.</p>
</li>
</ul>
</div>
<div>
<p>The Criteria class also provides the following methods for geospatial queries.</p>
</div>
<div>
<ul>
<li>
<p><code>Criteria</code> <strong>within</strong> <code>(Circle circle)</code> Creates a geospatial criterion using <code>$geoWithin $center</code> operators.</p>
</li>
<li>
<p><code>Criteria</code> <strong>within</strong> <code>(Box box)</code> Creates a geospatial criterion using a <code>$geoWithin $box</code> operation.</p>
</li>
<li>
<p><code>Criteria</code> <strong>withinSphere</strong> <code>(Circle circle)</code> Creates a geospatial criterion using <code>$geoWithin $center</code> operators.</p>
</li>
<li>
<p><code>Criteria</code> <strong>near</strong> <code>(Point point)</code> Creates a geospatial criterion using a <code>$near</code> operation</p>
</li>
<li>
<p><code>Criteria</code> <strong>nearSphere</strong> <code>(Point point)</code> Creates a geospatial criterion using <code>$nearSphere$center</code> operations. This is only available for MongoDB 1.7 and higher.</p>
</li>
<li>
<p><code>Criteria</code> <strong>minDistance</strong> <code>(double minDistance)</code> Creates a geospatial criterion using the <code>$minDistance</code> operation, for use with $near.</p>
</li>
<li>
<p><code>Criteria</code> <strong>maxDistance</strong> <code>(double maxDistance)</code> Creates a geospatial criterion using the <code>$maxDistance</code> operation, for use with $near.</p>
</li>
</ul>
</div>
</div>
</details>

The `Query` class has some additional methods that allow to select certain fields as well as to limit and sort the result.

<details id="mongodb-template-query.query">
<summary>Methods of the Query class</summary>
<div>
<div>
<ul>
<li>
<p><code>Query</code> <strong>addCriteria</strong> <code>(Criteria criteria)</code> used to add additional criteria to the query</p>
</li>
<li>
<p><code>Field</code> <strong>fields</strong> <code>()</code> used to define fields to be included in the query results</p>
</li>
<li>
<p><code>Query</code> <strong>limit</strong> <code>(int limit)</code> used to limit the size of the returned results to the provided limit (used for paging)</p>
</li>
<li>
<p><code>Query</code> <strong>skip</strong> <code>(int skip)</code> used to skip the provided number of documents in the results (used for paging)</p>
</li>
<li>
<p><code>Query</code> <strong>with</strong> <code>(Sort sort)</code> used to provide sort definition for the results</p>
</li>
<li>
<p><code>Query</code> <strong>with</strong> <code>(ScrollPosition position)</code> used to provide a scroll position (Offset- or Keyset-based pagination) to start or resume a <code>Scroll</code></p>
</li>
</ul>
</div>
</div>
</details>

The template API allows direct usage of result projections that enable you to map queries against a given domain type while projecting the operation result onto another one as outlined below.

```java
class

template.query(SWCharacter.class)
    .as(Jedi.class)
```

For more information on result projections please refer to the [Projections](#repositories-projections) section of the documentation.

<a id="mongodb-template-query-operations--mongo-template.querying.field-selection"></a>
<a id="mongodb-template-query-operations--selecting-fields"></a>

## Selecting fields

MongoDB supports [projecting fields](https://docs.mongodb.com/manual/tutorial/project-fields-from-query-results/) returned by a query.
A projection can include and exclude fields (the `_id` field is always included unless explicitly excluded) based on their name.

Example 2. Selecting result fields

```java
public class Person {

    @Id String id;
    String firstname;

    @Field("last_name")
    String lastname;

    Address address;
}

query.fields().include("lastname");              (1)

query.fields().exclude("id").include("lastname") (2)

query.fields().include("address")                (3)

query.fields().include("address.city")           (4)
```

| **1** | Result will contain both `_id` and `last_name` via `{ "last_name" : 1 }`. |
| --- | --- |
| **2** | Result will only contain the `last_name` via `{ "_id" : 0, "last_name" : 1 }`. |
| **3** | Result will contain the `_id` and entire `address` object via `{ "address" : 1 }`. |
| **4** | Result will contain the `_id` and and `address` object that only contains the `city` field via `{ "address.city" : 1 }`. |

Starting with MongoDB 4.4 you can use aggregation expressions for field projections as shown below:

Example 3. Computing result fields using expressions

```java
query.fields()
  .project(MongoExpression.create("'$toUpper' : '$last_name'"))         (1)
  .as("last_name");                                                     (2)

query.fields()
  .project(StringOperators.valueOf("lastname").toUpper())               (3)
  .as("last_name");

query.fields()
  .project(AggregationSpELExpression.expressionOf("toUpper(lastname)")) (4)
  .as("last_name");
```

**1**

Use a native expression. The used field name must refer to field names within the database document.

**2**

Assign the field name to which the expression result is projected. The resulting field name is not mapped against the domain model.

**3**

Use an `AggregationExpression`. Other than native `MongoExpression`, field names are mapped to the ones used in the domain model.

**4**

Use SpEL along with an `AggregationExpression` to invoke expression functions. Field names are mapped to the ones used in the domain model.

`@Query(fields="…")` allows usage of expression field projections at `Repository` level as described in [MongoDB JSON-based Query Methods and Field Restriction](#mongodb-repositories-repositories--mongodb.repositories.queries.json-based).

<a id="mongodb-template-query-operations--mongo.query.additional-query-options"></a>
<a id="mongodb-template-query-operations--additional-query-options"></a>

## Additional Query Options

MongoDB offers various ways of applying meta information, like a comment or a batch size, to a query.Using the `Query` API
directly there are several methods for those options.

<a id="mongodb-template-query-operations--mongo.query.hints"></a>
<a id="mongodb-template-query-operations--hints"></a>

> [!NOTE]
> ### Hints

Index hints can be applied in two ways, using the index name or its field definition.

```java
template.query(Person.class)
    .matching(query("...").withHint("index-to-use"));

template.query(Person.class)
    .matching(query("...").withHint("{ firstname : 1 }"));
```

<a id="mongodb-template-query-operations--mongo.query.cursor-size"></a>
<a id="mongodb-template-query-operations--cursor-batch-size"></a>

### Cursor Batch Size

The cursor batch size defines the number of documents to return in each response batch.

```java
Query query = query(where("firstname").is("luke"))
    .cursorBatchSize(100)
```

<a id="mongodb-template-query-operations--mongo.query.collation"></a>
<a id="mongodb-template-query-operations--collations"></a>

### Collations

Using collations with collection operations is a matter of specifying a `Collation` instance in your query or operation options, as the following two examples show:

```java
Collation collation = Collation.of("de");

Query query = new Query(Criteria.where("firstName").is("Amél"))
    .collation(collation);

List<Person> results = template.find(query, Person.class);
```

<a id="mongodb-template-query-operations--mongo.query.read-preference"></a>
<a id="mongodb-template-query-operations--read-preference"></a>

### Read Preference

The `ReadPreference` to use can be set directly on the `Query` object to be run as outlined below.

```java
template.find(Person.class)
    .matching(query(where(...)).withReadPreference(ReadPreference.secondary()))
    .all();
```

> [!NOTE]
> The preference set on the `Query` instance will supersede the default `ReadPreference` of `MongoTemplate`.

<a id="mongodb-template-query-operations--mongo.query.comment"></a>
<a id="mongodb-template-query-operations--comments"></a>

### Comments

Queries can be equipped with comments which makes them easier to look up in server logs.

```java
template.find(Person.class)
    .matching(query(where(...)).comment("Use the force luke!"))
    .all();
```

<a id="mongodb-template-query-operations--mongo-template.query.distinct"></a>
<a id="mongodb-template-query-operations--query-distinct-values"></a>

## Query Distinct Values

MongoDB provides an operation to obtain distinct values for a single field by using a query from the resulting documents.
Resulting values are not required to have the same data type, nor is the feature limited to simple types.
For retrieval, the actual result type does matter for the sake of conversion and typing. The following example shows how to query for distinct values:

Example 4. Retrieving distinct values

```java
template.query(Person.class)  (1)
  .distinct("lastname")       (2)
  .all();                     (3)
```

| **1** | Query the `Person` collection. |
| --- | --- |
| **2** | Select distinct values of the `lastname` field. The field name is mapped according to the domain types property declaration, taking potential `@Field` annotations into account. |
| **3** | Retrieve all distinct values as a `List` of `Object` (due to no explicit result type being specified). |

Retrieving distinct values into a `Collection` of `Object` is the most flexible way, as it tries to determine the property value of the domain type and convert results to the desired type or mapping `Document` structures.

Sometimes, when all values of the desired field are fixed to a certain type, it is more convenient to directly obtain a correctly typed `Collection`, as shown in the following example:

Example 5. Retrieving strongly typed distinct values

```java
template.query(Person.class)  (1)
  .distinct("lastname")       (2)
  .as(String.class)           (3)
  .all();                     (4)
```

| **1** | Query the collection of `Person`. |
| --- | --- |
| **2** | Select distinct values of the `lastname` field. The fieldname is mapped according to the domain types property declaration, taking potential `@Field` annotations into account. |
| **3** | Retrieved values are converted into the desired target type — in this case, `String`. It is also possible to map the values to a more complex type if the stored field contains a document. |
| **4** | Retrieve all distinct values as a `List` of `String`. If the type cannot be converted into the desired target type, this method throws a `DataAccessException`. |

+= GeoSpatial Queries

MongoDB supports GeoSpatial queries through the use of operators such as `$near`, `$within`, `geoWithin`, and `$nearSphere`. Methods specific to geospatial queries are available on the `Criteria` class. There are also a few shape classes (`Box`, `Circle`, and `Point`) that are used in conjunction with geospatial related `Criteria` methods.

> [!NOTE]
> Using GeoSpatial queries requires attention when used within MongoDB transactions, see [Special behavior inside transactions](#mongodb-client-session-transactions--mongo.transactions.behavior).

To understand how to perform GeoSpatial queries, consider the following `Venue` class (taken from the integration tests and relying on the rich `MappingMongoConverter`):

<details>
<summary>Venue.java</summary>
<div>
<div>
<div>
<pre><code>@Document(collection="newyork")
public class Venue {

  @Id
  private String id;
  private String name;
  private double[] location;

  @PersistenceCreator
  Venue(String name, double[] location) {
    super();
    this.name = name;
    this.location = location;
  }

  public Venue(String name, double x, double y) {
    super();
    this.name = name;
    this.location = new double[] { x, y };
  }

  public String getName() {
    return name;
  }

  public double[] getLocation() {
    return location;
  }

  @Override
  public String toString() {
    return "Venue [id=" + id + ", name=" + name + ", location="
        + Arrays.toString(location) + "]";
  }
}</code></pre>
</div>
</div>
</div>
</details>

To find locations within a `Circle`, you can use the following query:

```java
Circle circle = new Circle(-73.99171, 40.738868, 0.01);
List<Venue> venues =
    template.find(new Query(Criteria.where("location").within(circle)), Venue.class);
```

To find venues within a `Circle` using spherical coordinates, you can use the following query:

```java
Circle circle = new Circle(-73.99171, 40.738868, 0.003712240453784);
List<Venue> venues =
    template.find(new Query(Criteria.where("location").withinSphere(circle)), Venue.class);
```

To find venues within a `Box`, you can use the following query:

```java
//lower-left then upper-right
Box box = new Box(new Point(-73.99756, 40.73083), new Point(-73.988135, 40.741404));
List<Venue> venues =
    template.find(new Query(Criteria.where("location").within(box)), Venue.class);
```

To find venues near a `Point`, you can use the following queries:

```java
Point point = new Point(-73.99171, 40.738868);
List<Venue> venues =
    template.find(new Query(Criteria.where("location").near(point).maxDistance(0.01)), Venue.class);
```

```java
Point point = new Point(-73.99171, 40.738868);
List<Venue> venues =
    template.find(new Query(Criteria.where("location").near(point).minDistance(0.01).maxDistance(100)), Venue.class);
```

To find venues near a `Point` using spherical coordinates, you can use the following query:

```java
Point point = new Point(-73.99171, 40.738868);
List<Venue> venues =
    template.find(new Query(
        Criteria.where("location").nearSphere(point).maxDistance(0.003712240453784)),
        Venue.class);
```

<a id="mongodb-template-query-operations--mongo.geo-near"></a>
<a id="mongodb-template-query-operations--geo-near-queries"></a>

## Geo-near Queries

> [!WARNING]
> **Changed in 2.2!**
> [MongoDB 4.2](https://docs.mongodb.com/master/release-notes/4.2-compatibility/) removed support for the
> `geoNear` command which had been previously used to run the `NearQuery`.
>
> Spring Data MongoDB 2.2 `MongoOperations#geoNear` uses the `$geoNear` [aggregation](https://docs.mongodb.com/manual/reference/operator/aggregation/geoNear/)
> instead of the `geoNear` command to run a `NearQuery`.
>
> The calculated distance (the `dis` when using a geoNear command) previously returned within a wrapper type now is embedded
> into the resulting document.
> If the given domain type already contains a property with that name, the calculated distance
> is named `calculated-distance` with a potentially random postfix.
>
> Target types may contain a property named after the returned distance to (additionally) read it back directly into the domain type as shown below.
>
> ```java
> GeoResults<VenueWithDistanceField> = template.query(Venue.class) (1)
>     .as(VenueWithDistanceField.class)                            (2)
>     .near(NearQuery.near(new GeoJsonPoint(-73.99, 40.73), KILOMETERS))
>     .all();
> ```
>
> **1**
>
> Domain type used to identify the target collection and potential query mapping.
>
> **2**
>
> Target type containing a `dis` field of type `Number`.

MongoDB supports querying the database for geo locations and calculating the distance from a given origin at the same time. With geo-near queries, you can express queries such as "find all restaurants in the surrounding 10 miles". To let you do so, `MongoOperations` provides `geoNear(…)` methods that take a `NearQuery` as an argument (as well as the already familiar entity type and collection), as shown in the following example:

```java
Point location = new Point(-73.99171, 40.738868);
NearQuery query = NearQuery.near(location).maxDistance(new Distance(10, Metrics.MILES));

GeoResults<Restaurant> = operations.geoNear(query, Restaurant.class);
```

We use the `NearQuery` builder API to set up a query to return all `Restaurant` instances surrounding the given `Point` out to 10 miles.
The `Metrics` enum used here actually implements an interface so that other metrics could be plugged into a distance as well.
A `Metric` is backed by a multiplier to transform the distance value of the given metric into native distances.
The sample shown here would consider the 10 to be miles. Using one of the built-in metrics (miles and kilometers) automatically triggers the spherical flag to be set on the query.
If you want to avoid that, pass plain `double` values into `maxDistance(…)`.
For more information, see the Javadoc of [`NearQuery`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/query/NearQuery.html) and `Distance`.

The geo-near operations return a `GeoResults` wrapper object that encapsulates `GeoResult` instances.
Wrapping `GeoResults` allows accessing the average distance of all results.
A single `GeoResult` object carries the entity found plus its distance from the origin.

<a id="mongodb-template-query-operations--mongo.geo-json"></a>
<a id="mongodb-template-query-operations--geojson-support"></a>

## GeoJSON Support

MongoDB supports [GeoJSON](https://geojson.org/) and simple (legacy) coordinate pairs for geospatial data. Those formats can both be used for storing as well as querying data. See the [MongoDB manual on GeoJSON support](https://docs.mongodb.org/manual/core/2dsphere/#geospatial-indexes-store-geojson/) to learn about requirements and restrictions.

<a id="mongodb-template-query-operations--mongo.geo-json.domain.classes"></a>
<a id="mongodb-template-query-operations--geojson-types-in-domain-classes"></a>

## GeoJSON Types in Domain Classes

Usage of [GeoJSON](https://geojson.org/) types in domain classes is straightforward. The `org.springframework.data.mongodb.core.geo` package contains types such as `GeoJsonPoint`, `GeoJsonPolygon`, and others. These types are extend the existing `org.springframework.data.geo` types. The following example uses a [`GeoJsonPoint`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/geo/GeoJsonPoint.html):

```java
public class Store {
String id;
/** * { "type" : "Point", "coordinates" : [ x, y ] } */ GeoJsonPoint location;}
```

> [!TIP]
> If the `coordinates` of a GeoJSON object represent *latitude* and *longitude* pairs, the *longitude* goes first followed by *latitude*.
> `GeoJsonPoint` therefore treats `getX()` as *longitude* and `getY()` as *latitude*.

<a id="mongodb-template-query-operations--mongo.geo-json.query-methods"></a>
<a id="mongodb-template-query-operations--geojson-types-in-repository-query-methods"></a>

## GeoJSON Types in Repository Query Methods

Using GeoJSON types as repository query parameters forces usage of the `$geometry` operator when creating the query, as the following example shows:

```java
public interface StoreRepository extends CrudRepository<Store, String> {

	List<Store> findByLocationWithin(Polygon polygon);  (1)

}

/*
 * {
 *   "location": {
 *     "$geoWithin": {
 *       "$geometry": {
 *         "type": "Polygon",
 *         "coordinates": [
 *           [
 *             [-73.992514,40.758934],
 *             [-73.961138,40.760348],
 *             [-73.991658,40.730006],
 *             [-73.992514,40.758934]
 *           ]
 *         ]
 *       }
 *     }
 *   }
 * }
 */
repo.findByLocationWithin(                              (2)
  new GeoJsonPolygon(
    new Point(-73.992514, 40.758934),
    new Point(-73.961138, 40.760348),
    new Point(-73.991658, 40.730006),
    new Point(-73.992514, 40.758934)));                 (3)

/*
 * {
 *   "location" : {
 *     "$geoWithin" : {
 *        "$polygon" : [ [-73.992514,40.758934] , [-73.961138,40.760348] , [-73.991658,40.730006] ]
 *     }
 *   }
 * }
 */
repo.findByLocationWithin(                              (4)
  new Polygon(
    new Point(-73.992514, 40.758934),
    new Point(-73.961138, 40.760348),
    new Point(-73.991658, 40.730006)));
```

**1**

Repository method definition using the commons type allows calling it with both the GeoJSON and the legacy format.

**2**

Use GeoJSON type to make use of `$geometry` operator.

**3**

Note that GeoJSON polygons need to define a closed ring.

**4**

Use the legacy format `$polygon` operator.

<a id="mongodb-template-query-operations--mongo.geo-json.metrics"></a>
<a id="mongodb-template-query-operations--metrics-and-distance-calculation"></a>

## Metrics and Distance calculation

Then MongoDB `$geoNear` operator allows usage of a GeoJSON Point or legacy coordinate pairs.

```java
NearQuery.near(new Point(-73.99171, 40.738868))
```

```json
{
  "$geoNear": {
    //...
    "near": [-73.99171, 40.738868]
  }
}
```

```java
NearQuery.near(new GeoJsonPoint(-73.99171, 40.738868))
```

```json
{
  "$geoNear": {
    //...
    "near": { "type": "Point", "coordinates": [-73.99171, 40.738868] }
  }
}
```

Though syntactically different the server is fine accepting both no matter what format the target Document within the collection
is using.

> [!WARNING]
> There is a huge difference in the distance calculation. Using the legacy format operates
> upon *Radians* on an Earth like sphere, whereas the GeoJSON format uses *Meters*.

To avoid a serious headache make sure to set the `Metric` to the desired unit of measure which ensures the
distance to be calculated correctly.

In other words:

Assume you’ve got 5 Documents like the ones below:

```json
{"_id" : ObjectId("5c10f3735d38908db52796a5"),"name" : "Penn Station","location" : { "type" : "Point", "coordinates" : [  -73.99408, 40.75057 ] }} {"_id" : ObjectId("5c10f3735d38908db52796a6"),"name" : "10gen Office","location" : { "type" : "Point", "coordinates" : [ -73.99171, 40.738868 ] }} {"_id" : ObjectId("5c10f3735d38908db52796a9"),"name" : "City Bakery ","location" : { "type" : "Point", "coordinates" : [ -73.992491, 40.738673 ] }} {"_id" : ObjectId("5c10f3735d38908db52796aa"),"name" : "Splash Bar","location" : { "type" : "Point", "coordinates" : [ -73.992491, 40.738673 ] }} {"_id" : ObjectId("5c10f3735d38908db52796ab"),"name" : "Momofuku Milk Bar","location" : { "type" : "Point", "coordinates" : [ -73.985839, 40.731698 ] }}
```

Fetching all Documents within a 400 Meter radius from `[-73.99171, 40.738868]` would look like this using
GeoJSON:

Example 6. GeoNear with GeoJSON

```json
{"$geoNear": {"maxDistance": 400, (1) "num": 10,"near": { type: "Point", coordinates: [-73.99171, 40.738868] },"spherical":true, (2) "key": "location","distanceField": "distance"}}
```

Returning the following 3 Documents:

```json
{"_id" : ObjectId("5c10f3735d38908db52796a6"),"name" : "10gen Office","location" : { "type" : "Point", "coordinates" : [ -73.99171, 40.738868 ] } "distance" : 0.0 (3)} {"_id" : ObjectId("5c10f3735d38908db52796a9"),"name" : "City Bakery ","location" : { "type" : "Point", "coordinates" : [ -73.992491, 40.738673 ] } "distance" : 69.3582262492474 (3)} {"_id" : ObjectId("5c10f3735d38908db52796aa"),"name" : "Splash Bar","location" : { "type" : "Point", "coordinates" : [ -73.992491, 40.738673 ] } "distance" : 69.3582262492474 (3)}
```

| **1** | Maximum distance from center point in *Meters*. |
| --- | --- |
| **2** | GeoJSON always operates upon a sphere. |
| **3** | Distance from center point in *Meters*. |

Now, when using legacy coordinate pairs one operates upon *Radians* as discussed before. So we use `` Metrics#KILOMETERS
when constructing the `$geoNear `` command. The `Metric` makes sure the distance multiplier is set correctly.

Example 7. GeoNear with Legacy Coordinate Pairs

```json
{"$geoNear": {"maxDistance": 0.0000627142377, (1) "distanceMultiplier": 6378.137, (2) "num": 10,"near": [-73.99171, 40.738868],"spherical":true, (3) "key": "location","distanceField": "distance"}}
```

Returning the 3 Documents just like the GeoJSON variant:

```json
{"_id" : ObjectId("5c10f3735d38908db52796a6"),"name" : "10gen Office","location" : { "type" : "Point", "coordinates" : [ -73.99171, 40.738868 ] } "distance" : 0.0 (4)} {"_id" : ObjectId("5c10f3735d38908db52796a9"),"name" : "City Bakery ","location" : { "type" : "Point", "coordinates" : [ -73.992491, 40.738673 ] } "distance" : 0.0693586286032982 (4)} {"_id" : ObjectId("5c10f3735d38908db52796aa"),"name" : "Splash Bar","location" : { "type" : "Point", "coordinates" : [ -73.992491, 40.738673 ] } "distance" : 0.0693586286032982 (4)}
```

| **1** | Maximum distance from center point in *Radians*. |
| --- | --- |
| **2** | The distance multiplier so we get *Kilometers* as resulting distance. |
| **3** | Make sure we operate on a 2d\_sphere index. |
| **4** | Distance from center point in *Kilometers* - take it times 1000 to match *Meters* of the GeoJSON variant. |

<a id="mongodb-template-query-operations--mongo.textsearch"></a>
<a id="mongodb-template-query-operations--full-text-search"></a>

## Full-text Search

Since version 2.6 of MongoDB, you can run full-text queries by using the `$text` operator. Methods and operations specific to full-text queries are available in `TextQuery` and `TextCriteria`. When doing full text search, see the [MongoDB reference](https://docs.mongodb.org/manual/reference/operator/query/text/#behavior) for its behavior and limitations.

Before you can actually use full-text search, you must set up the search index correctly.
See [Text Index](#mongodb-mapping-mapping--mapping-usage-indexes.text-index) for more detail on how to create index structures.
The following example shows how to set up a full-text search:

```javascript
db.foo.createIndex({title : "text",content : "text" },{weights : {title : 3}})
```

A query searching for `coffee cake` can be defined and run as follows:

Example 8. Full Text Query

```java
Query query = TextQuery
  .queryText(new TextCriteria().matchingAny("coffee", "cake"));

List<Document> page = template.find(query, Document.class);
```

To sort results by relevance according to the `weights` use `TextQuery.sortByScore`.

Example 9. Full Text Query - Sort by Score

```java
Query query = TextQuery
  .queryText(new TextCriteria().matchingAny("coffee", "cake"))
  .sortByScore() (1)
  .includeScore(); (2)

List<Document> page = template.find(query, Document.class);
```

**1**

Use the score property for sorting results by relevance which triggers `.sort({'score': {'$meta': 'textScore'}})`.

**2**

Use `TextQuery.includeScore()` to include the calculated relevance in the resulting `Document`.

You can exclude search terms by prefixing the term with `-` or by using `notMatching`, as shown in the following example (note that the two lines have the same effect and are thus redundant):

```java
// search for 'coffee' and not 'cake'
TextQuery.queryText(new TextCriteria().matching("coffee").matching("-cake"));
TextQuery.queryText(new TextCriteria().matching("coffee").notMatching("cake"));
```

`TextCriteria.matching` takes the provided term as is.
Therefore, you can define phrases by putting them between double quotation marks (for example, `\"coffee cake\")` or using by `TextCriteria.phrase.`
The following example shows both ways of defining a phrase:

```java
// search for phrase 'coffee cake'
TextQuery.queryText(new TextCriteria().matching("\"coffee cake\""));
TextQuery.queryText(new TextCriteria().phrase("coffee cake"));
```

You can set flags for `$caseSensitive` and `$diacriticSensitive` by using the corresponding methods on `TextCriteria`.
Note that these two optional flags have been introduced in MongoDB 3.2 and are not included in the query unless explicitly set.

<a id="mongodb-template-query-operations--mongo.query-by-example"></a>
<a id="mongodb-template-query-operations--query-by-example"></a>

## Query by Example

[Query by Example](#mongodb-repositories-query-methods--query-by-example) can be used on the Template API level run example queries.

The following snipped shows how to query by example:

Typed Example Query

```java
Person probe = new Person();
probe.lastname = "stark";

Example example = Example.of(probe);

Query query = new Query(new Criteria().alike(example));
List<Person> result = template.find(query, Person.class);
```

By default `Example` is strictly typed. This means that the mapped query has an included type match, restricting it to probe assignable types.
For example, when sticking with the default type key (`_class`), the query has restrictions such as (`_class : { $in : [ com.acme.Person] }`).

By using the `UntypedExampleMatcher`, it is possible to bypass the default behavior and skip the type restriction. So, as long as field names match, nearly any domain type can be used as the probe for creating the reference, as the following example shows:

Example 10. Untyped Example Query

```java
class JustAnArbitraryClassWithMatchingFieldName {
  @Field("lastname") String value;
}

JustAnArbitraryClassWithMatchingFieldNames probe = new JustAnArbitraryClassWithMatchingFieldNames();
probe.value = "stark";

Example example = Example.of(probe, UntypedExampleMatcher.matching());

Query query = new Query(new Criteria().alike(example));
List<Person> result = template.find(query, Person.class);
```

> [!NOTE]
> When including `null` values in the `ExampleSpec`, Spring Data Mongo uses embedded document matching instead of dot notation property matching.
> Doing so forces exact document matching for all property values and the property order in the embedded document.

> [!NOTE]
> `UntypedExampleMatcher` is likely the right choice for you if you are storing different entities within a single collection or opted out of writing type hints.
>
> Also, keep in mind that using `@TypeAlias` requires eager initialization of the `MappingContext`. To do so, configure `initialEntitySet` to to ensure proper alias resolution for read operations.

Spring Data MongoDB provides support for different matching options:

<details>
<summary><code>StringMatcher</code> options</summary>
<div>
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Matching</th>
<th>Logical result</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>DEFAULT</code> (case-sensitive)</p></td>
<td><p><code>{"firstname" : firstname}</code></p></td>
</tr>
<tr>
<td><p><code>DEFAULT</code> (case-insensitive)</p></td>
<td><p><code>{"firstname" : { $regex: firstname, $options: 'i'}}</code></p></td>
</tr>
<tr>
<td><p><code>EXACT</code>  (case-sensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /^firstname$/}}</code></p></td>
</tr>
<tr>
<td><p><code>EXACT</code> (case-insensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /^firstname$/, $options: 'i'}}</code></p></td>
</tr>
<tr>
<td><p><code>STARTING</code>  (case-sensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /^firstname/}}</code></p></td>
</tr>
<tr>
<td><p><code>STARTING</code> (case-insensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /^firstname/, $options: 'i'}}</code></p></td>
</tr>
<tr>
<td><p><code>ENDING</code>  (case-sensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /firstname$/}}</code></p></td>
</tr>
<tr>
<td><p><code>ENDING</code> (case-insensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /firstname$/, $options: 'i'}}</code></p></td>
</tr>
<tr>
<td><p><code>CONTAINING</code>  (case-sensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /.*firstname.*/}}</code></p></td>
</tr>
<tr>
<td><p><code>CONTAINING</code> (case-insensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /.*firstname.*/, $options: 'i'}}</code></p></td>
</tr>
<tr>
<td><p><code>REGEX</code>  (case-sensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /firstname/}}</code></p></td>
</tr>
<tr>
<td><p><code>REGEX</code> (case-insensitive)</p></td>
<td><p><code>{"firstname" : { $regex: /firstname/, $options: 'i'}}</code></p></td>
</tr>
</tbody>
</table>
</div>
</details>

<a id="mongodb-template-query-operations--mongo.jsonschema.query"></a>
<a id="mongodb-template-query-operations--query-a-collection-for-matching-json-schema"></a>

## Query a collection for matching JSON Schema

You can use a schema to query any collection for documents that match a given structure defined by a JSON schema, as the following example shows:

Example 11. Query for Documents matching a `$jsonSchema`

```java
MongoJsonSchema schema = MongoJsonSchema.builder().required("firstname", "lastname").build();

template.find(query(matchingDocumentStructure(schema)), Person.class);
```

Please refer to the [JSON Schema](#mongodb-mapping-mapping-schema) section to learn more about the schema support in Spring Data MongoDB.

---

<a id="mongodb-property-paths"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/property-paths.html -->

<!-- page_index: 16 -->

# Property Paths

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-property-paths--page-title"></a>
<a id="mongodb-property-paths--property-paths"></a>

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

<a id="mongodb-property-paths--property-path-overview"></a>

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
See [Type-safe Property-References](#mongodb-property-paths--type-safe-property-references) for details.

> [!NOTE]
> For implementation details, refer to [Property Path Internals](#mongodb-property-paths--property-path-internals) for more information.

<a id="mongodb-property-paths--property-path-internals"></a>

### Property Path Internals

The [`org.springframework.data.core`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/core/package-summary.html) package is the basis for Spring Data’s navigation across domain classes.
The [`TypeInformation`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/core/TypeInformation.html) interface provides type introspection capable of resolving the type of a property. [`PropertyPath`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/core/PropertyPath.html) represents a textual navigation path through a domain class.

Together they provide:

- Generic type resolution and introspection
- Property path creation and validation
- Actual type resolution for complex properties such as collections and maps

<a id="mongodb-property-paths--type-safe-property-references"></a>

## Type-safe Property-References

Type-safe property-references eliminate a common source of errors in data access code: Brittle, string-based property references.
This section explains how method references can be used to express refactoring-safe property paths.

While a property path is a simple representation of object navigation, String-based property paths are inherently fragile during refactoring as they can be easily missed with an increasing distance between the property definition and its usage.
Type-safe alternatives through [`TypedPropertyPath`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/core/TypedPropertyPath.html) derive property paths from method references, enabling the compiler to validate property names and IDEs to support refactoring operations.

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

<a id="mongodb-property-paths--type-safe-property-references-recommendations"></a>
<a id="mongodb-property-paths--type-safe-property-reference-api-recommendations"></a>

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

<a id="mongodb-template-document-count"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-document-count.html -->

<!-- page_index: 17 -->

# Counting Documents

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-document-count--page-title"></a>
<a id="mongodb-template-document-count--counting-documents"></a>

# Counting Documents

The template API offers various methods to count the number of documents matching a given criteria.
One of them outlined below.

```java
template.query(Person.class)
    .matching(query(where("firstname").is("luke")))
    .count();
```

In pre-3.x versions of SpringData MongoDB the count operation used MongoDBs internal collection statistics.
With the introduction of [MongoDB Transactions](#mongodb-client-session-transactions--mongo.transactions) this was no longer possible because statistics would not correctly reflect potential changes during a transaction requiring an aggregation-based count approach.
So in version 2.x `MongoOperations.count()` would use the collection statistics if no transaction was in progress, and the aggregation variant if so.

As of Spring Data MongoDB 3.x any `count` operation uses regardless the existence of filter criteria the aggregation-based count approach via MongoDBs `countDocuments`.
If the application is fine with the limitations of working upon collection statistics `MongoOperations.estimatedCount()` offers an alternative.

> [!TIP]
> By setting `MongoTemplate#useEstimatedCount(…)` to `true` *MongoTemplate#count(…)* operations, that use an empty filter query, will be delegated to `estimatedCount`, as long as there is no transaction active and the template is not bound to a [session](#mongodb-client-session-transactions).
> It will still be possible to obtain exact numbers via `MongoTemplate#exactCount`, but may speed up things.

> [!NOTE]
> MongoDBs native `countDocuments` method and the `$match` aggregation, do not support `$near` and `$nearSphere` but require `$geoWithin` along with `$center` or `$centerSphere` which does not support `$minDistance` (see [jira.mongodb.org/browse/SERVER-37043](https://jira.mongodb.org/browse/SERVER-37043)).
>
> Therefore a given `Query` will be rewritten for `count` operations using `Reactive`-/`MongoTemplate` to bypass the issue like shown below.
>
> ```javascript
> { location : { $near : [-73.99171, 40.738868], $maxDistance : 1.1 } } (1)
> { location : { $geoWithin : { $center: [ [-73.99171, 40.738868], 1.1] } } } (2)
>
> { location : { $near : [-73.99171, 40.738868], $minDistance : 0.1, $maxDistance : 1.1 } } (3)
> {$and :[ { $nor :[ { location :{ $geoWithin :{ $center :[ [-73.99171, 40.738868 ], 0.01] } } } ]}, { location :{ $geoWithin :{ $center :[ [-73.99171, 40.738868 ], 1.1] } } } ] } (4)
> ```
>
> | **1** | Count source query using `$near`. |
> | --- | --- |
> | **2** | Rewritten query now using `$geoWithin` with `$center`. |
> | **3** | Count source query using `$near` with `$minDistance` and `$maxDistance`. |
> | **4** | Rewritten query now a combination of `$nor` `$geowithin` critierias to work around unsupported `$minDistance`.

---

<a id="mongodb-aggregation-framework"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/aggregation-framework.html -->

<!-- page_index: 18 -->

# Aggregation Framework Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-aggregation-framework--page-title"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-support"></a>

# Aggregation Framework Support

Spring Data MongoDB provides support for the Aggregation Framework introduced to MongoDB in version 2.2.

For further information, see the full [reference documentation](https://docs.mongodb.org/manual/aggregation/) of the aggregation framework and other data aggregation tools for MongoDB.

<a id="mongodb-aggregation-framework--mongo.aggregation.basic-concepts"></a>
<a id="mongodb-aggregation-framework--basic-concepts"></a>

## Basic Concepts

The Aggregation Framework support in Spring Data MongoDB is based on the following key abstractions: [`Aggregation`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/aggregation/Aggregation.html) and [`AggregationResults`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/aggregation/AggregationResults.html).

- `Aggregation`

  An `Aggregation` represents a MongoDB `aggregate` operation and holds the description of the aggregation pipeline instructions. Aggregations are created by invoking the appropriate `newAggregation(…)` static factory method of the `Aggregation` class, which takes a list of `AggregateOperation` and an optional input class.

  The actual aggregate operation is run by the `aggregate` method of the `MongoTemplate`, which takes the desired output class as a parameter.
- `TypedAggregation`

  A `TypedAggregation`, just like an `Aggregation`, holds the instructions of the aggregation pipeline and a reference to the input type, that is used for mapping domain properties to actual document fields.

  At runtime, field references get checked against the given input type, considering potential `@Field` annotations.

Changed in 3.2 referencing non-existent properties does no longer raise errors. To restore the previous behaviour use the `strictMapping` option of `AggregationOptions`.

- `AggregationDefinition`

  An `AggregationDefinition` represents a MongoDB aggregation pipeline operation and describes the processing that should be performed in this aggregation step. Although you could manually create an `AggregationDefinition`, we recommend using the static factory methods provided by the `Aggregate` class to construct an `AggregateOperation`.
- `AggregationResults`

  `AggregationResults` is the container for the result of an aggregate operation. It provides access to the raw aggregation result, in the form of a `Document` to the mapped objects and other information about the aggregation.

  The following listing shows the canonical example for using the Spring Data MongoDB support for the MongoDB Aggregation Framework:


```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

Aggregation agg = newAggregation(
    pipelineOP1(),
    pipelineOP2(),
    pipelineOPn()
);

AggregationResults<OutputType> results = mongoTemplate.aggregate(agg, "INPUT_COLLECTION_NAME", OutputType.class);
List<OutputType> mappedResult = results.getMappedResults();
```

Note that, if you provide an input class as the first parameter to the `newAggregation` method, the `MongoTemplate` derives the name of the input collection from this class. Otherwise, if you do not not specify an input class, you must provide the name of the input collection explicitly. If both an input class and an input collection are provided, the latter takes precedence.

<details id="aggregation-stages">
<summary>Supported Aggregation Operations &amp; Stages</summary>
<div>
<div>
<p>The MongoDB Aggregation Framework provides the following types of aggregation stages and operations:</p>
</div>
<div>
<ul>
<li>
<p>addFields - <code>AddFieldsOperation</code></p>
</li>
<li>
<p>bucket / bucketAuto - <code>BucketOperation</code> / <code>BucketAutoOperation</code></p>
</li>
<li>
<p>count - <code>CountOperation</code></p>
</li>
<li>
<p>densify - <code>DensifyOperation</code></p>
</li>
<li>
<p>facet - <code>FacetOperation</code></p>
</li>
<li>
<p>geoNear - <code>GeoNearOperation</code></p>
</li>
<li>
<p>graphLookup - <code>GraphLookupOperation</code></p>
</li>
<li>
<p>group - <code>GroupOperation</code></p>
</li>
<li>
<p>limit - <code>LimitOperation</code></p>
</li>
<li>
<p>lookup - <code>LookupOperation</code></p>
</li>
<li>
<p>match - <code>MatchOperation</code></p>
</li>
<li>
<p>merge - <code>MergeOperation</code></p>
</li>
<li>
<p>project - <code>ProjectionOperation</code></p>
</li>
<li>
<p>redact - <code>RedactOperation</code></p>
</li>
<li>
<p>replaceRoot - <code>ReplaceRootOperation</code></p>
</li>
<li>
<p>sample - <code>SampleOperation</code></p>
</li>
<li>
<p>set - <code>SetOperation</code></p>
</li>
<li>
<p>setWindowFields - <code>SetWindowFieldsOperation</code></p>
</li>
<li>
<p>skip - <code>SkipOperation</code></p>
</li>
<li>
<p>sort / sortByCount - <code>SortOperation</code> / <code>SortByCountOperation</code></p>
</li>
<li>
<p>unionWith - <code>UnionWithOperation</code></p>
</li>
<li>
<p>unset - <code>UnsetOperation</code></p>
</li>
<li>
<p>unwind - <code>UnwindOperation</code></p>
</li>
</ul>
</div>
</div>
</details>

> [!TIP]
> Unsupported aggregation stages (like [$search](https://www.mongodb.com/docs/atlas/atlas-search/query-syntax/) for MongoDB Atlas) can be provided by implementing either `AggregationOperation`.
> `Aggregation.stage` is a shortcut for registering a pipeline stage by providing its JSON or `Bson` representation.
>
> ```java
> Aggregation.stage(""" { $search : {"near": {"path": "released","origin": { "$date": { "$numberLong": "..." } } ,"pivot": 7}}} """);
> ```

At the time of this writing, we provide support for the following Aggregation Operators in Spring Data MongoDB:

Set Aggregation Operators

`setEquals`, `setIntersection`, `setUnion`, `setDifference`, `setIsSubset`, `anyElementTrue`, `allElementsTrue`

Group/Accumulator Aggregation Operators

`addToSet`, `bottom`, `bottomN`, `covariancePop`, `covarianceSamp`, `expMovingAvg`, `first`, `firstN`, `last`, `lastN` `max`, `maxN`, `min`, `minN`, `avg`, `push`, `sum`, `top`, `topN`, `count` (\*), `median`, `percentile`, `stdDevPop`, `stdDevSamp`

Arithmetic Aggregation Operators

`abs`, `acos`, `acosh`, `add` (\* via `plus`), `asin`, `asin`, `atan`, `atan2`, `atanh`, `ceil`, `cos`, `cosh`, `derivative`, `divide`, `exp`, `floor`, `integral`, `ln`, `log`, `log10`, `mod`, `multiply`, `pow`, `round`, `sqrt`, `subtract` (\* via `minus`), `sin`, `sinh`, `tan`, `tanh`, `trunc`

String Aggregation Operators

`concat`, `substr`, `toLower`, `toUpper`, `strcasecmp`, `indexOfBytes`, `indexOfCP`, `regexFind`, `regexFindAll`, `regexMatch`, `replaceAll`, `replaceOne`, `split`, `strLenBytes`, `strLenCP`, `substrCP`, `trim`, `ltrim`, `rtim`

Comparison Aggregation Operators

`eq` (\* via `is`), `gt`, `gte`, `lt`, `lte`, `ne`

Array Aggregation Operators

`arrayElementAt`, `arrayToObject`, `concatArrays`, `filter`, `first`, `in`, `indexOfArray`, `isArray`, `last`, `range`, `reverseArray`, `reduce`, `size`, `sortArray`, `slice`, `zip`

Literal Operators

`literal`

Date Aggregation Operators

`dateSubstract`, `dateTrunc`, `dayOfYear`, `dayOfMonth`, `dayOfWeek`, `year`, `month`, `week`, `hour`, `minute`, `second`, `millisecond`, `dateAdd`, `dateDiff`, `dateToString`, `dateFromString`, `dateFromParts`, `dateToParts`, `isoDayOfWeek`, `isoWeek`, `isoWeekYear`, `tsIncrement`, `tsSecond`

Variable Operators

`map`

Conditional Aggregation Operators

`cond`, `ifNull`, `switch`

Type Aggregation Operators

`type`

Convert Aggregation Operators

`convert`, `degreesToRadians`, `toBool`, `toDate`, `toDecimal`, `toDouble`, `toInt`, `toLong`, `toObjectId`, `toString`

Object Aggregation Operators

`objectToArray`, `mergeObjects`, `getField`, `setField`

Script Aggregation Operators

`function`, `accumulator`

\* The operation is mapped or added by Spring Data MongoDB.

Note that the aggregation operations not listed here are currently not supported by Spring Data MongoDB. Comparison aggregation operators are expressed as `Criteria` expressions.

<a id="mongodb-aggregation-framework--mongo.aggregation.projection"></a>
<a id="mongodb-aggregation-framework--projection-expressions"></a>

## Projection Expressions

Projection expressions are used to define the fields that are the outcome of a particular aggregation step. Projection expressions can be defined through the `project` method of the `Aggregation` class, either by passing a list of `String` objects or an aggregation framework `Fields` object. The projection can be extended with additional fields through a fluent API by using the `and(String)` method and aliased by using the `as(String)` method.
Note that you can also define fields with aliases by using the `Fields.field` static factory method of the aggregation framework, which you can then use to construct a new `Fields` instance. References to projected fields in later aggregation stages are valid only for the field names of included fields or their aliases (including newly defined fields and their aliases). Fields not included in the projection cannot be referenced in later aggregation stages. The following listings show examples of projection expression:

Example 1. Projection expression examples

```java
// generates {$project: {name: 1, netPrice: 1}}
project("name", "netPrice")

// generates {$project: {thing1: $thing2}}
project().and("thing1").as("thing2")

// generates {$project: {a: 1, b: 1, thing2: $thing1}}
project("a","b").and("thing1").as("thing2")
```

Example 2. Multi-Stage Aggregation using Projection and Sorting

```java
// generates {$project: {name: 1, netPrice: 1}}, {$sort: {name: 1}}
project("name", "netPrice"), sort(ASC, "name")

// generates {$project: {name: $firstname}}, {$sort: {name: 1}}
project().and("firstname").as("name"), sort(ASC, "name")

// does not work
project().and("firstname").as("name"), sort(ASC, "firstname")
```

More examples for project operations can be found in the `AggregationTests` class. Note that further details regarding the projection expressions can be found in the [corresponding section](https://docs.mongodb.org/manual/reference/operator/aggregation/project/#pipe._S_project) of the MongoDB Aggregation Framework reference documentation.

<a id="mongodb-aggregation-framework--mongo.aggregation.facet"></a>
<a id="mongodb-aggregation-framework--faceted-classification"></a>

## Faceted Classification

As of Version 3.4, MongoDB supports faceted classification by using the Aggregation Framework. A faceted classification uses semantic categories (either general or subject-specific) that are combined to create the full classification entry. Documents flowing through the aggregation pipeline are classified into buckets. A multi-faceted classification enables various aggregations on the same set of input documents, without needing to retrieve the input documents multiple times.

<a id="mongodb-aggregation-framework--buckets"></a>

### Buckets

Bucket operations categorize incoming documents into groups, called buckets, based on a specified expression and bucket boundaries. Bucket operations require a grouping field or a grouping expression. You can define them by using the `bucket()` and `bucketAuto()` methods of the `Aggregate` class. `BucketOperation` and `BucketAutoOperation` can expose accumulations based on aggregation expressions for input documents. You can extend the bucket operation with additional parameters through a fluent API by using the `with…()` methods and the `andOutput(String)` method. You can alias the operation by using the `as(String)` method. Each bucket is represented as a document in the output.

`BucketOperation` takes a defined set of boundaries to group incoming documents into these categories. Boundaries are required to be sorted. The following listing shows some examples of bucket operations:

Example 3. Bucket operation examples

```java
// generates {$bucket: {groupBy: $price, boundaries: [0, 100, 400]}}
bucket("price").withBoundaries(0, 100, 400);

// generates {$bucket: {groupBy: $price, default: "Other" boundaries: [0, 100]}}
bucket("price").withBoundaries(0, 100).withDefault("Other");

// generates {$bucket: {groupBy: $price, boundaries: [0, 100], output: { count: { $sum: 1}}}}
bucket("price").withBoundaries(0, 100).andOutputCount().as("count");

// generates {$bucket: {groupBy: $price, boundaries: [0, 100], 5, output: { titles: { $push: "$title"}}}
bucket("price").withBoundaries(0, 100).andOutput("title").push().as("titles");
```

`BucketAutoOperation` determines boundaries in an attempt to evenly distribute documents into a specified number of buckets. `BucketAutoOperation` optionally takes a granularity value that specifies the [preferred number](https://en.wikipedia.org/wiki/Preferred_number) series to use to ensure that the calculated boundary edges end on preferred round numbers or on powers of 10. The following listing shows examples of bucket operations:

Example 4. Bucket operation examples

```java
// generates {$bucketAuto: {groupBy: $price, buckets: 5}}
bucketAuto("price", 5)

// generates {$bucketAuto: {groupBy: $price, buckets: 5, granularity: "E24"}}
bucketAuto("price", 5).withGranularity(Granularities.E24).withDefault("Other");

// generates {$bucketAuto: {groupBy: $price, buckets: 5, output: { titles: { $push: "$title"}}}
bucketAuto("price", 5).andOutput("title").push().as("titles");
```

To create output fields in buckets, bucket operations can use `AggregationExpression` through `andOutput()` and [SpEL expressions](#mongodb-aggregation-framework--mongo.aggregation.projection.expressions) through `andOutputExpression()`.

Note that further details regarding bucket expressions can be found in the [`$bucket` section](https://docs.mongodb.org/manual/reference/operator/aggregation/bucket/) and
[`$bucketAuto` section](https://docs.mongodb.org/manual/reference/operator/aggregation/bucketAuto/) of the MongoDB Aggregation Framework reference documentation.

<a id="mongodb-aggregation-framework--multi-faceted-aggregation"></a>

### Multi-faceted Aggregation

Multiple aggregation pipelines can be used to create multi-faceted aggregations that characterize data across multiple dimensions (or facets) within a single aggregation stage. Multi-faceted aggregations provide multiple filters and categorizations to guide data browsing and analysis. A common implementation of faceting is how many online retailers provide ways to narrow down search results by applying filters on product price, manufacturer, size, and other factors.

You can define a `FacetOperation` by using the `facet()` method of the `Aggregation` class. You can customize it with multiple aggregation pipelines by using the `and()` method. Each sub-pipeline has its own field in the output document where its results are stored as an array of documents.

Sub-pipelines can project and filter input documents prior to grouping. Common use cases include extraction of date parts or calculations before categorization. The following listing shows facet operation examples:

Example 5. Facet operation examples

```java
// generates {$facet: {categorizedByPrice: [ { $match: { price: {$exists : true}}}, { $bucketAuto: {groupBy: $price, buckets: 5}}]}}
facet(match(Criteria.where("price").exists(true)), bucketAuto("price", 5)).as("categorizedByPrice"))

// generates {$facet: {categorizedByCountry: [ { $match: { country: {$exists : true}}}, { $sortByCount: "$country"}]}}
facet(match(Criteria.where("country").exists(true)), sortByCount("country")).as("categorizedByCountry"))

// generates {$facet: {categorizedByYear: [
//     { $project: { title: 1, publicationYear: { $year: "publicationDate"}}},
//     { $bucketAuto: {groupBy: $price, buckets: 5, output: { titles: {$push:"$title"}}}
// ]}}
facet(project("title").and("publicationDate").extractYear().as("publicationYear"),
      bucketAuto("publicationYear", 5).andOutput("title").push().as("titles"))
  .as("categorizedByYear"))
```

Note that further details regarding facet operation can be found in the [`$facet` section](https://docs.mongodb.org/manual/reference/operator/aggregation/facet/) of the MongoDB Aggregation Framework reference documentation.

<a id="mongodb-aggregation-framework--mongo.aggregation.sort-by-count"></a>
<a id="mongodb-aggregation-framework--sort-by-count"></a>

### Sort By Count

Sort by count operations group incoming documents based on the value of a specified expression, compute the count of documents in each distinct group, and sort the results by count. It offers a handy shortcut to apply sorting when using [Faceted Classification](#mongodb-aggregation-framework--mongo.aggregation.facet). Sort by count operations require a grouping field or grouping expression. The following listing shows a sort by count example:

Example 6. Sort by count example

```java
// generates { $sortByCount: "$country" }
sortByCount("country");
```

A sort by count operation is equivalent to the following BSON (Binary JSON):

```
{ $group: { _id: <expression>, count: { $sum: 1 } } },
{ $sort: { count: -1 } }
```

<a id="mongodb-aggregation-framework--mongo.aggregation.projection.expressions"></a>
<a id="mongodb-aggregation-framework--spring-expression-support-in-projection-expressions"></a>

### Spring Expression Support in Projection Expressions

We support the use of SpEL expressions in projection expressions through the `andExpression` method of the `ProjectionOperation` and `BucketOperation` classes. This feature lets you define the desired expression as a SpEL expression. On running a query, the SpEL expression is translated into a corresponding MongoDB projection expression part. This arrangement makes it much easier to express complex calculations.

<a id="mongodb-aggregation-framework--complex-calculations-with-spel-expressions"></a>

#### Complex Calculations with SpEL expressions

Consider the following SpEL expression:

```java
1 + (q + 1) / (q - 1)
```

The preceding expression is translated into the following projection expression part:

```javascript
{ "$add" : [ 1, {
    "$divide" : [ {
        "$add":["$q", 1]}, {
        "$subtract":[ "$q", 1]}
    ]
}]}
```

You can see examples in more context in [Aggregation Framework Example 5](#mongodb-aggregation-framework--mongo.aggregation.examples.example5) and [Aggregation Framework Example 6](#mongodb-aggregation-framework--mongo.aggregation.examples.example6).
You can find more usage examples for supported SpEL expression constructs in `SpelExpressionTransformerUnitTests`.

<details>
<summary>Supported SpEL transformations</summary>
<div>
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>SpEL Expression</th>
<th>Mongo Expression Part</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>a == b</p></td>
<td><p>{ $eq : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a != b</p></td>
<td><p>{ $ne : [$a , $b] }</p></td>
</tr>
<tr>
<td><p>a &gt; b</p></td>
<td><p>{ $gt : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a &gt;= b</p></td>
<td><p>{ $gte : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a &lt; b</p></td>
<td><p>{ $lt : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a ⇐ b</p></td>
<td><p>{ $lte : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a + b</p></td>
<td><p>{ $add : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a - b</p></td>
<td><p>{ $subtract : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a * b</p></td>
<td><p>{ $multiply : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a / b</p></td>
<td><p>{ $divide : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a^b</p></td>
<td><p>{ $pow : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a % b</p></td>
<td><p>{ $mod : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a &amp;&amp; b</p></td>
<td><p>{ $and : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>a || b</p></td>
<td><p>{ $or : [$a, $b] }</p></td>
</tr>
<tr>
<td><p>!a</p></td>
<td><p>{ $not : [$a] }</p></td>
</tr>
</tbody>
</table>
</div>
</details>

In addition to the transformations shown in the preceding table, you can use standard SpEL operations such as `new` to (for example) create arrays and reference expressions through their names (followed by the arguments to use in brackets). The following example shows how to create an array in this fashion:

```java
// { $setEquals : [$a, [5, 8, 13] ] }
.andExpression("setEquals(a, new int[]{5, 8, 13})");
```

<a id="mongodb-aggregation-framework--mongo.aggregation.examples"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-examples"></a>

### Aggregation Framework Examples

The examples in this section demonstrate the usage patterns for the MongoDB Aggregation Framework with Spring Data MongoDB.

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example1"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-1"></a>

#### Aggregation Framework Example 1

In this introductory example, we want to aggregate a list of tags to get the occurrence count of a particular tag from a MongoDB collection (called `tags`) sorted by the occurrence count in descending order. This example demonstrates the usage of grouping, sorting, projections (selection), and unwinding (result splitting).

```java
class TagCount {
 String tag;
 int n;
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

Aggregation agg = newAggregation(
    project("tags"),
    unwind("tags"),
    group("tags").count().as("n"),
    project("n").and("tag").previousOperation(),
    sort(DESC, "n")
);

AggregationResults<TagCount> results = mongoTemplate.aggregate(agg, "tags", TagCount.class);
List<TagCount> tagCount = results.getMappedResults();
```

The preceding listing uses the following algorithm:

1. Create a new aggregation by using the `newAggregation` static factory method, to which we pass a list of aggregation operations. These aggregate operations define the aggregation pipeline of our `Aggregation`.
2. Use the `project` operation to select the `tags` field (which is an array of strings) from the input collection.
3. Use the `unwind` operation to generate a new document for each tag within the `tags` array.
4. Use the `group` operation to define a group for each `tags` value for which we aggregate the occurrence count (by using the `count` aggregation operator and collecting the result in a new field called `n`).
5. Select the `n` field and create an alias for the ID field generated from the previous group operation (hence the call to `previousOperation()`) with a name of `tag`.
6. Use the `sort` operation to sort the resulting list of tags by their occurrence count in descending order.
7. Call the `aggregate` method on `MongoTemplate` to let MongoDB perform the actual aggregation operation, with the created `Aggregation` as an argument.

Note that the input collection is explicitly specified as the `tags` parameter to the `aggregate` Method. If the name of the input collection is not specified explicitly, it is derived from the input class passed as the first parameter to the `newAggreation` method.

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example2"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-2"></a>

#### Aggregation Framework Example 2

This example is based on the [Largest and Smallest Cities by State](https://docs.mongodb.org/manual/tutorial/aggregation-examples/#largest-and-smallest-cities-by-state) example from the MongoDB Aggregation Framework documentation. We added additional sorting to produce stable results with different MongoDB versions. Here we want to return the smallest and largest cities by population for each state by using the aggregation framework. This example demonstrates grouping, sorting, and projections (selection).

```java
class ZipInfo {
   String id;
   String city;
   String state;
   @Field("pop") int population;
   @Field("loc") double[] location;
}

class City {
   String name;
   int population;
}

class ZipInfoStats {
   String id;
   String state;
   City biggestCity;
   City smallestCity;
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

TypedAggregation<ZipInfo> aggregation = newAggregation(ZipInfo.class,
    group("state", "city")
       .sum("population").as("pop"),
    sort(ASC, "pop", "state", "city"),
    group("state")
       .last("city").as("biggestCity")
       .last("pop").as("biggestPop")
       .first("city").as("smallestCity")
       .first("pop").as("smallestPop"),
    project()
       .and("state").previousOperation()
       .and("biggestCity")
          .nested(bind("name", "biggestCity").and("population", "biggestPop"))
       .and("smallestCity")
          .nested(bind("name", "smallestCity").and("population", "smallestPop")),
    sort(ASC, "state")
);

AggregationResults<ZipInfoStats> result = mongoTemplate.aggregate(aggregation, ZipInfoStats.class);
ZipInfoStats firstZipInfoStats = result.getMappedResults().get(0);
```

Note that the `ZipInfo` class maps the structure of the given input-collection. The `ZipInfoStats` class defines the structure in the desired output format.

The preceding listings use the following algorithm:

1. Use the `group` operation to define a group from the input-collection. The grouping criteria is the combination of the `state` and `city` fields, which forms the ID structure of the group. We aggregate the value of the `population` property from the grouped elements by using the `sum` operator and save the result in the `pop` field.
2. Use the `sort` operation to sort the intermediate-result by the `pop`, `state` and `city` fields, in ascending order, such that the smallest city is at the top and the biggest city is at the bottom of the result. Note that the sorting on `state` and `city` is implicitly performed against the group ID fields (which Spring Data MongoDB handled).
3. Use a `group` operation again to group the intermediate result by `state`. Note that `state` again implicitly references a group ID field. We select the name and the population count of the biggest and smallest city with calls to the `last(…)` and `first(…)` operators, respectively, in the `project` operation.
4. Select the `state` field from the previous `group` operation. Note that `state` again implicitly references a group ID field. Because we do not want an implicitly generated ID to appear, we exclude the ID from the previous operation by using `and(previousOperation()).exclude()`. Because we want to populate the nested `City` structures in our output class, we have to emit appropriate sub-documents by using the nested method.
5. Sort the resulting list of `StateStats` by their state name in ascending order in the `sort` operation.

Note that we derive the name of the input collection from the `ZipInfo` class passed as the first parameter to the `newAggregation` method.

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example3"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-3"></a>

#### Aggregation Framework Example 3

This example is based on the [States with Populations Over 10 Million](https://docs.mongodb.org/manual/tutorial/aggregation-examples/#states-with-populations-over-10-million) example from the MongoDB Aggregation Framework documentation. We added additional sorting to produce stable results with different MongoDB versions. Here we want to return all states with a population greater than 10 million, using the aggregation framework. This example demonstrates grouping, sorting, and matching (filtering).

```java
class StateStats {
   @Id String id;
   String state;
   @Field("totalPop") int totalPopulation;
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

TypedAggregation<ZipInfo> agg = newAggregation(ZipInfo.class,
    group("state").sum("population").as("totalPop"),
    sort(ASC, previousOperation(), "totalPop"),
    match(where("totalPop").gte(10 * 1000 * 1000))
);

AggregationResults<StateStats> result = mongoTemplate.aggregate(agg, StateStats.class);
List<StateStats> stateStatsList = result.getMappedResults();
```

The preceding listings use the following algorithm:

1. Group the input collection by the `state` field and calculate the sum of the `population` field and store the result in the new field `"totalPop"`.
2. Sort the intermediate result by the id-reference of the previous group operation in addition to the `"totalPop"` field in ascending order.
3. Filter the intermediate result by using a `match` operation which accepts a `Criteria` query as an argument.

Note that we derive the name of the input collection from the `ZipInfo` class passed as first parameter to the `newAggregation` method.

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example4"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-4"></a>

#### Aggregation Framework Example 4

This example demonstrates the use of simple arithmetic operations in the projection operation.

```java
class Product {
    String id;
    String name;
    double netPrice;
    int spaceUnits;
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

TypedAggregation<Product> agg = newAggregation(Product.class,
    project("name", "netPrice")
        .and("netPrice").plus(1).as("netPricePlus1")
        .and("netPrice").minus(1).as("netPriceMinus1")
        .and("netPrice").multiply(1.19).as("grossPrice")
        .and("netPrice").divide(2).as("netPriceDiv2")
        .and("spaceUnits").mod(2).as("spaceUnitsMod2")
);

AggregationResults<Document> result = mongoTemplate.aggregate(agg, Document.class);
List<Document> resultList = result.getMappedResults();
```

Note that we derive the name of the input collection from the `Product` class passed as first parameter to the `newAggregation` method.

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example5"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-5"></a>

#### Aggregation Framework Example 5

This example demonstrates the use of simple arithmetic operations derived from SpEL Expressions in the projection operation.

```java
class Product {
    String id;
    String name;
    double netPrice;
    int spaceUnits;
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

TypedAggregation<Product> agg = newAggregation(Product.class,
    project("name", "netPrice")
        .andExpression("netPrice + 1").as("netPricePlus1")
        .andExpression("netPrice - 1").as("netPriceMinus1")
        .andExpression("netPrice / 2").as("netPriceDiv2")
        .andExpression("netPrice * 1.19").as("grossPrice")
        .andExpression("spaceUnits % 2").as("spaceUnitsMod2")
        .andExpression("(netPrice * 0.8  + 1.2) * 1.19").as("grossPriceIncludingDiscountAndCharge")

);

AggregationResults<Document> result = mongoTemplate.aggregate(agg, Document.class);
List<Document> resultList = result.getMappedResults();
```

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example6"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-6"></a>

#### Aggregation Framework Example 6

This example demonstrates the use of complex arithmetic operations derived from SpEL Expressions in the projection operation.

Note: The additional parameters passed to the `addExpression` method can be referenced with indexer expressions according to their position. In this example, we reference the first parameter of the parameters array with `[0]`. When the SpEL expression is transformed into a MongoDB aggregation framework expression, external parameter expressions are replaced with their respective values.

```java
class Product {
    String id;
    String name;
    double netPrice;
    int spaceUnits;
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

double shippingCosts = 1.2;

TypedAggregation<Product> agg = newAggregation(Product.class,
    project("name", "netPrice")
        .andExpression("(netPrice * (1-discountRate)  + [0]) * (1+taxRate)", shippingCosts).as("salesPrice")
);

AggregationResults<Document> result = mongoTemplate.aggregate(agg, Document.class);
List<Document> resultList = result.getMappedResults();
```

Note that we can also refer to other fields of the document within the SpEL expression.

<a id="mongodb-aggregation-framework--mongo.aggregation.examples.example7"></a>
<a id="mongodb-aggregation-framework--aggregation-framework-example-7"></a>

#### Aggregation Framework Example 7

This example uses conditional projection. It is derived from the [$cond reference documentation](https://docs.mongodb.com/manual/reference/operator/aggregation/cond/).

```java
public class InventoryItem {

  @Id int id;
  String item;
  String description;
  int qty;
}

public class InventoryItemProjection {

  @Id int id;
  String item;
  String description;
  int qty;
  int discount
}
```

```java
import static org.springframework.data.mongodb.core.aggregation.Aggregation.*;

TypedAggregation<InventoryItem> agg = newAggregation(InventoryItem.class,
  project("item").and("discount")
    .applyCondition(ConditionalOperator.newBuilder().when(Criteria.where("qty").gte(250))
      .then(30)
      .otherwise(20))
    .and(ifNull("description", "Unspecified")).as("description")
);

AggregationResults<InventoryItemProjection> result = mongoTemplate.aggregate(agg, "inventory", InventoryItemProjection.class);
List<InventoryItemProjection> stateStatsList = result.getMappedResults();
```

This one-step aggregation uses a projection operation with the `inventory` collection. We project the `discount` field by using a conditional operation for all inventory items that have a `qty` greater than or equal to `250`. A second conditional projection is performed for the `description` field. We apply the `Unspecified` description to all items that either do not have a `description` field or items that have a `null` description.

As of MongoDB 3.6, it is possible to exclude fields from the projection by using a conditional expression.

Example 7. Conditional aggregation projection

```java
TypedAggregation<Book> agg = Aggregation.newAggregation(Book.class,
  project("title")
    .and(ConditionalOperators.when(ComparisonOperators.valueOf("author.middle")     (1)
        .equalToValue(""))                                                          (2)
        .then("$$REMOVE")                                                           (3)
        .otherwiseValueOf("author.middle")                                          (4)
    )
	.as("author.middle"));
```

| **1** | If the value of the field `author.middle` |
| --- | --- |
| **2** | does not contain a value, |
| **3** | then use [`$$REMOVE`](https://docs.mongodb.com/manual/reference/aggregation-variables/#variable.REMOVE) to exclude the field. |
| **4** | Otherwise, add the field value of `author.middle`. |

---

<a id="mongodb-template-gridfs"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/template-gridfs.html -->

<!-- page_index: 19 -->

# GridFS Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-template-gridfs--page-title"></a>
<a id="mongodb-template-gridfs--gridfs-support"></a>

# GridFS Support

MongoDB supports storing binary files inside its filesystem, GridFS.
Spring Data MongoDB provides a [`GridFsOperations`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/gridfs/GridFsOperations.html) and [`ReactiveGridFsOperations`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/gridfs/ReactiveGridFsOperations.html) interface as well as the corresponding implementation, `GridFsTemplate` and `ReactiveGridFsTemplate`, to let you interact with the filesystem.
You can set up a template instance by handing it a `MongoDatabaseFactory`/`ReactiveMongoDatabaseFactory` as well as a `MongoConverter`, as the following example shows:

- Imperative
- Reactive
- XML

```java
class GridFsConfiguration extends AbstractMongoClientConfiguration {
// … further configuration omitted
@Bean public GridFsTemplate gridFsTemplate() {return new GridFsTemplate(mongoDbFactory(), mappingMongoConverter());}}
```

```java
class ReactiveGridFsConfiguration extends AbstractReactiveMongoConfiguration {
// … further configuration omitted
@Bean public ReactiveGridFsTemplate reactiveGridFsTemplate() {return new ReactiveGridFsTemplate(reactiveMongoDbFactory(), mappingMongoConverter());}}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:mongo="http://www.springframework.org/schema/data/mongo"
xsi:schemaLocation="http://www.springframework.org/schema/data/mongo
https://www.springframework.org/schema/data/mongo/spring-mongo.xsd
http://www.springframework.org/schema/beans
https://www.springframework.org/schema/beans/spring-beans.xsd">

  <mongo:db-factory id="mongoDbFactory" dbname="database" />
  <mongo:mapping-converter id="converter" />

  <bean class="org.springframework.data.mongodb.gridfs.GridFsTemplate">
    <constructor-arg ref="mongoDbFactory" />
    <constructor-arg ref="converter" />
  </bean>

</beans>
```

The template can now be injected and used to perform storage and retrieval operations, as the following example shows:

Using GridFS to store files

- Imperative
- Reactive

```java
class GridFsClient {

  @Autowired
  GridFsOperations operations;

  @Test
  public void storeFileToGridFs() {

    FileMetadata metadata = new FileMetadata();
    // populate metadata
    Resource file = … // lookup File or Resource

    operations.store(file.getInputStream(), "filename.txt", metadata);
  }
}
```

The `store(…)` operations take an `InputStream`, a filename, and (optionally) metadata information about the file to store.
The metadata can be an arbitrary object, which will be marshaled by the `MongoConverter` configured with the `GridFsTemplate`.
Alternatively, you can also provide a `Document`.

```java
class ReactiveGridFsClient {

  @Autowired
  ReactiveGridFsTemplate operations;

  @Test
  public Mono<ObjectId> storeFileToGridFs() {

    FileMetadata metadata = new FileMetadata();
    // populate metadata
    Publisher<DataBuffer> file = … // lookup File or Resource

    return operations.store(file, "filename.txt", metadata);
  }
}
```

The `store(…)` operations take an `Publisher<DataBuffer>`, a filename, and (optionally) metadata information about the file to store.
The metadata can be an arbitrary object, which will be marshaled by the `MongoConverter` configured with the `ReactiveGridFsTemplate`.
Alternatively, you can also provide a `Document`.

The MongoDB’s driver uses `AsyncInputStream` and `AsyncOutputStream` interfaces to exchange binary streams.
Spring Data MongoDB adapts these interfaces to `Publisher<DataBuffer>`.
Read more about `DataBuffer` in [Spring’s reference documentation](https://docs.spring.io/spring-framework/reference/7.0/core/databuffer-codec.html).

You can read files from the filesystem through either the `find(…)` or the `getResources(…)` methods.
Let’s have a look at the `find(…)` methods first.
You can either find a single file or multiple files that match a `Query`.
You can use the `GridFsCriteria` helper class to define queries.
It provides static factory methods to encapsulate default metadata fields (such as `whereFilename()` and `whereContentType()`) or a custom one through `whereMetaData()`.
The following example shows how to use the template to query for files:

Using GridFsTemplate to query for files

- Imperative
- Reactive

```java
class GridFsClient {
@Autowired GridFsOperations operations;
@Test public void findFilesInGridFs() {GridFSFindIterable result = operations.find(query(whereFilename().is("filename.txt")));}}
```

```java
class ReactiveGridFsClient {
@Autowired ReactiveGridFsTemplate operations;
@Test public Flux<GridFSFile> findFilesInGridFs() {return operations.find(query(whereFilename().is("filename.txt")))}}
```

> [!NOTE]
> Currently, MongoDB does not support defining sort criteria when retrieving files from GridFS. For this reason, any sort criteria defined on the `Query` instance handed into the `find(…)` method are disregarded.

The other option to read files from the GridFs is to use the methods introduced by the `ResourcePatternResolver` interface.
They allow handing an Ant path into the method and can thus retrieve files matching the given pattern.
The following example shows how to use `GridFsTemplate` to read files:

Using GridFsTemplate to read files

- Imperative
- Reactive

```java
class GridFsClient {
@Autowired GridFsOperations operations;
public GridFsResources[] readFilesFromGridFs() {return operations.getResources("*.txt");}}
```

```java
class ReactiveGridFsClient {
@Autowired ReactiveGridFsOperations operations;
public Flux<ReactiveGridFsResource> readFilesFromGridFs() {return operations.getResources("*.txt");}}
```

`GridFsOperations` extends `ResourcePatternResolver` and lets the `GridFsTemplate` (for example) to be plugged into an `ApplicationContext` to read Spring Config files from MongoDB database.

> [!NOTE]
> By default, `GridFsTemplate` obtains `GridFSBucket` once upon the first GridFS interaction.
> After that, the template instance reuses the cached bucket.
> To use different buckets, from the same Template instance use the constructor accepting `Supplier<GridFSBucket>`.

---

<a id="mongodb-mapping-mapping"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/mapping.html -->

<!-- page_index: 20 -->

# Object Mapping

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-mapping--page-title"></a>
<a id="mongodb-mapping-mapping--object-mapping"></a>

# Object Mapping

Rich mapping support is provided by the `MappingMongoConverter`.
The converter holds a metadata model that provides a full feature set to map domain objects to MongoDB documents.
The mapping metadata model is populated by using annotations on your domain objects.
However, the infrastructure is not limited to using annotations as the only source of metadata information.
The `MappingMongoConverter` also lets you map objects to documents without providing any additional metadata, by following a set of conventions.

This section describes the features of the `MappingMongoConverter`, including fundamentals, how to use conventions for mapping objects to documents and how to override those conventions with annotation-based mapping metadata.

<a id="mongodb-mapping-mapping--mapping.fundamentals"></a>
<a id="mongodb-mapping-mapping--object-mapping-fundamentals"></a>

## Object Mapping Fundamentals

This section covers the fundamentals of Spring Data object mapping, object creation, field and property access, mutability and immutability.
Note, that this section only applies to Spring Data modules that do not use the object mapping of the underlying data store (like JPA).
Also be sure to consult the store-specific sections for store-specific object mapping, like indexes, customizing column or field names or the like.

Core responsibility of the Spring Data object mapping is to create instances of domain objects and map the store-native data structures onto those.
This means we need two fundamental steps:

1. Instance creation by using one of the constructors exposed.
2. Instance population to materialize all exposed properties.

<a id="mongodb-mapping-mapping--mapping.object-creation"></a>
<a id="mongodb-mapping-mapping--object-creation"></a>

### Object creation

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

<a id="mongodb-mapping-mapping--mapping.property-population"></a>
<a id="mongodb-mapping-mapping--property-population"></a>

### Property population

Once an instance of the entity has been created, Spring Data populates all remaining persistent properties of that class.
Unless already populated by the entity’s constructor (i.e. consumed through its constructor argument list), the identifier property will be populated first to allow the resolution of cyclic object references.
After that, all non-transient properties that have not already been populated by the constructor are set on the entity instance.
For that we use the following algorithm:

1. If the property is immutable but exposes a `with…` method (see below), we use the `with…` method to create a new entity instance with the new property value.
2. If property access (i.e. access through getters and setters) is defined, we’re invoking the setter method.
3. If the property is mutable we set the field directly.
4. If the property is immutable we’re using the constructor to be used by persistence operations (see [Object creation](#mongodb-mapping-mapping--mapping.object-creation)) to create a copy of the instance.
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

<a id="mongodb-mapping-mapping--mapping.general-recommendations"></a>
<a id="mongodb-mapping-mapping--general-recommendations"></a>

### General recommendations

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

<a id="mongodb-mapping-mapping--mapping.general-recommendations.override.properties"></a>
<a id="mongodb-mapping-mapping--overriding-properties"></a>

#### Overriding Properties

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

<a id="mongodb-mapping-mapping--mapping.kotlin"></a>
<a id="mongodb-mapping-mapping--kotlin-support"></a>

### Kotlin support

Spring Data adapts specifics of Kotlin to allow object creation and mutation.

<a id="mongodb-mapping-mapping--mapping.kotlin.creation"></a>
<a id="mongodb-mapping-mapping--kotlin-object-creation"></a>

#### Kotlin object creation

Kotlin classes are supported to be instantiated, all classes are immutable by default and require explicit property declarations to define mutable properties.

Spring Data automatically tries to detect a persistent entity’s constructor to be used to materialize objects of that type.
The resolution algorithm works as follows:

1. If there is a constructor that is annotated with `@PersistenceCreator`, it is used.
2. If the type is a [Kotlin data class](#mongodb-mapping-mapping--mapping.kotlin) the primary constructor is used.
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
> In all other cases you can exclude synthetic fields for delegated properties by annotating the property with [`@Transient`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/annotation/Transient.html).

<a id="mongodb-mapping-mapping--property-population-of-kotlin-data-classes"></a>

#### Property population of Kotlin data classes

In Kotlin, all classes are immutable by default and require explicit property declarations to define mutable properties.
Consider the following `data` class `Person`:

```kotlin
data class Person(val id: String, val name: String)
```

This class is effectively immutable.
It allows creating new instances as Kotlin generates a `copy(…)` method that creates new object instances copying all property values from the existing object and applying property values provided as arguments to the method.

<a id="mongodb-mapping-mapping--mapping.kotlin.override.properties"></a>
<a id="mongodb-mapping-mapping--kotlin-overriding-properties"></a>

#### Kotlin Overriding Properties

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

<a id="mongodb-mapping-mapping--mapping.kotlin.value.classes"></a>
<a id="mongodb-mapping-mapping--kotlin-value-classes"></a>

#### Kotlin Value Classes

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

<a id="mongodb-mapping-mapping--mapping-conventions"></a>
<a id="mongodb-mapping-mapping--convention-based-mapping"></a>

## Convention-based Mapping

`MappingMongoConverter` has a few conventions for mapping objects to documents when no additional mapping metadata is provided.
The conventions are:

- The short Java class name is mapped to the collection name in the following manner.
  The class `com.bigbank.SavingsAccount` maps to the `savingsAccount` collection name.
- All nested objects are stored as nested objects in the document and **not** as DBRefs.
- The converter uses any Spring Converters registered with it to override the default mapping of object properties to document fields and values.
- The fields of an object are used to convert to and from fields in the document.
  Public `JavaBean` properties are not used.
- If you have a single non-zero-argument constructor whose constructor argument names match top-level field names of document, that constructor is used.Otherwise, the zero-argument constructor is used.If there is more than one non-zero-argument constructor, an exception will be thrown.

<a id="mongodb-mapping-mapping--mapping.conventions.id-field"></a>
<a id="mongodb-mapping-mapping--how-the-_id-field-is-handled-in-the-mapping-layer."></a>

### How the `_id` field is handled in the mapping layer.

MongoDB requires that you have an `_id` field for all documents.If you don’t provide one the driver will assign a ObjectId with a generated value.The `_id` field can be of any type, other than arrays, so long as it is unique.The driver naturally supports all primitive types and Dates.When using the `MappingMongoConverter` there are certain rules that govern how properties from the Java class are mapped to the `_id` field.

The following outlines what field will be mapped to the `_id` document field:

- A field annotated with `@Id` (`org.springframework.data.annotation.Id`) will be mapped to the `_id` field.
  Additionally, the name of the document field can be customized via the `@Field` annotation, in which case the document will not contain a field `_id`.
- A field without an annotation but named `id` will be mapped to the `_id` field.

| Field definition | Resulting Id-Fieldname in MongoDB |
| --- | --- |
| `String` id | `_id` |
| `@Field` `String` id | `_id` |
| `@Field("x")` `String` id | `x` |
| `@Id` `String` x | `_id` |
| `@Field("x")` `@Id` `String` y | `_id` (`@Field(name)` is ignored, `@Id` takes precedence) |

The following outlines what type conversion, if any, will be done on the property mapped to the \_id document field.

- If a field named `id` is declared as a String or BigInteger in the Java class it will be converted to and stored as an ObjectId if possible.
  ObjectId as a field type is also valid.
  If you specify a value for `id` in your application, the conversion to an ObjectId is done by the MongoDB driver.
  If the specified `id` value cannot be converted to an ObjectId, then the value will be stored as is in the document’s `_id` field.
  This also applies if the field is annotated with `@Id`.
- If a field is annotated with `@MongoId` in the Java class it will be converted to and stored as using its actual type.
  No further conversion happens unless `@MongoId` declares a desired field type.
  If no value is provided for the `id` field, a new `ObjectId` will be created and converted to the properties type.
- If a field is annotated with `@MongoId(FieldType.…)` in the Java class it will be attempted to convert the value to the declared `FieldType`.
  If no value is provided for the `id` field, a new `ObjectId` will be created and converted to the declared type.
- If a field named `id` is not declared as a String, BigInteger, or ObjectID in the Java class then you should assign it a value in your application so it can be stored 'as-is' in the document’s `_id` field.
- If no field named `id` is present in the Java class then an implicit `_id` file will be generated by the driver but not mapped to a property or field of the Java class.

When querying and updating `MongoTemplate` will use the converter to handle conversions of the `Query` and `Update` objects that correspond to the above rules for saving documents so field names and types used in your queries will be able to match what is in your domain classes.

<a id="mongodb-mapping-mapping--mapping-conversion"></a>
<a id="mongodb-mapping-mapping--data-mapping-and-type-conversion"></a>

## Data Mapping and Type Conversion

Spring Data MongoDB supports all types that can be represented as BSON, MongoDB’s internal document format.
In addition to these types, Spring Data MongoDB provides a set of built-in converters to map additional types.
You can provide your own converters to adjust type conversion.
See [Custom Conversions - Overriding Default Mapping](#mongodb-mapping-custom-conversions) for further details.

<details>
<summary>Built in Type conversions:</summary>
<div>
<table>
<caption>Table 2. Type</caption>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Type</th>
<th>Type conversion</th>
<th>Sample</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>String</code></p></td>
<td><p>native</p></td>
<td><p><code>{"firstname" : "Dave"}</code></p></td>
</tr>
<tr>
<td><p><code>double</code>, <code>Double</code>, <code>float</code>, <code>Float</code></p></td>
<td><p>native</p></td>
<td><p><code>{"weight" : 42.5}</code></p></td>
</tr>
<tr>
<td><p><code>int</code>, <code>Integer</code>, <code>short</code>, <code>Short</code></p></td>
<td><p>native
32-bit integer</p></td>
<td><p><code>{"height" : 42}</code></p></td>
</tr>
<tr>
<td><p><code>long</code>, <code>Long</code></p></td>
<td><p>native
64-bit integer</p></td>
<td><p><code>{"height" : 42}</code></p></td>
</tr>
<tr>
<td><p><code>Date</code>, <code>Timestamp</code></p></td>
<td><p>native</p></td>
<td><p><code>{"date" : ISODate("2019-11-12T23:00:00.809Z")}</code></p></td>
</tr>
<tr>
<td><p><code>byte[]</code></p></td>
<td><p>native</p></td>
<td><p><code>{"bin" : { "$binary" : "AQIDBA==", "$type" : "00" }}</code></p></td>
</tr>
<tr>
<td><p><code>java.util.UUID</code> (According to UuidRepresentation)</p></td>
<td><p>native</p></td>
<td><p><code>{"uuid" : { "$binary" : "MEaf1CFQ6lSphaa3b9AtlA==", "$type" : "04" }}</code></p></td>
</tr>
<tr>
<td><p><code>Date</code></p></td>
<td><p>native</p></td>
<td><p><code>{"date" : ISODate("2019-11-12T23:00:00.809Z")}</code></p></td>
</tr>
<tr>
<td><p><code>ObjectId</code></p></td>
<td><p>native</p></td>
<td><p><code>{"_id" : ObjectId("5707a2690364aba3136ab870")}</code></p></td>
</tr>
<tr>
<td><p>Array, <code>List</code>, <code>BasicDBList</code></p></td>
<td><p>native</p></td>
<td><p><code>{"cookies" : [ … ]}</code></p></td>
</tr>
<tr>
<td><p><code>boolean</code>, <code>Boolean</code></p></td>
<td><p>native</p></td>
<td><p><code>{"active" : true}</code></p></td>
</tr>
<tr>
<td><p><code>null</code></p></td>
<td><p>native</p></td>
<td><p><code>{"value" : null}</code></p></td>
</tr>
<tr>
<td><p><code>Document</code></p></td>
<td><p>native</p></td>
<td><p><code>{"value" : { … }}</code></p></td>
</tr>
<tr>
<td><p><code>Decimal128</code></p></td>
<td><p>native</p></td>
<td><p><code>{"value" : NumberDecimal(…)}</code></p></td>
</tr>
<tr>
<td><p><code>AtomicInteger</code>

calling <code>get()</code> before the actual conversion</p></td>
<td><p>converter
32-bit integer</p></td>
<td><p><code>{"value" : "741" }</code></p></td>
</tr>
<tr>
<td><p><code>AtomicLong</code>

calling <code>get()</code> before the actual conversion</p></td>
<td><p>converter
64-bit integer</p></td>
<td><p><code>{"value" : "741" }</code></p></td>
</tr>
<tr>
<td><p><code>BigInteger</code></p></td>
<td><p>native

<code>NumberDecimal</code>, <code>String</code> (see <code>BigDecimalRepresentation</code>)</p></td>
<td><p><code>{"value" : NumberDecimal(741) }</code>, <code>{"value" : "741" }</code></p></td>
</tr>
<tr>
<td><p><code>BigDecimal</code></p></td>
<td><p>native

<code>NumberDecimal</code>, <code>String</code> (see <code>BigDecimalRepresentation</code>)</p></td>
<td><p><code>{"value" : NumberDecimal(741.99) }</code>, <code>{"value" : "741.99" }</code></p></td>
</tr>
<tr>
<td><p><code>URL</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"website" : "https://spring.io/projects/spring-data-mongodb/" }</code></p></td>
</tr>
<tr>
<td><p><code>Locale</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"locale : "en_US" }</code></p></td>
</tr>
<tr>
<td><p><code>char</code>, <code>Character</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"char" : "a" }</code></p></td>
</tr>
<tr>
<td><p><code>NamedMongoScript</code></p></td>
<td><p>converter

<code>Code</code></p></td>
<td><p><code>{"_id" : "script name", value: (some javascript code)</code>}</p></td>
</tr>
<tr>
<td><p><code>java.util.Currency</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"currencyCode" : "EUR"}</code></p></td>
</tr>
<tr>
<td><p><code>Instant</code>

(Java 8)</p></td>
<td><p>native</p></td>
<td><p><code>{"date" : ISODate("2019-11-12T23:00:00.809Z")}</code></p></td>
</tr>
<tr>
<td><p><code>Instant</code>

(Java 8)</p></td>
<td><p>converter</p></td>
<td><p><code>{"date" : ISODate("2019-11-12T23:00:00.809Z")}</code></p></td>
</tr>
<tr>
<td><p><code>LocalDate</code>

(Java 8)</p></td>
<td><p>converter / native (Java 8)<sup>[<a href="#mongodb-mapping-mapping--_footnotedef_1" id="_footnoteref_1" title="View footnote.">1</a>]</sup></p></td>
<td><p><code>{"date" : ISODate("2019-11-12T00:00:00.000Z")}</code></p></td>
</tr>
<tr>
<td><p><code>LocalDateTime</code>, <code>LocalTime</code>

(Java 8)</p></td>
<td><p>converter / native (Java 8)<sup>[<a href="#mongodb-mapping-mapping--_footnotedef_2" id="_footnoteref_2" title="View footnote.">2</a>]</sup></p></td>
<td><p><code>{"date" : ISODate("2019-11-12T23:00:00.809Z")}</code></p></td>
</tr>
<tr>
<td><p><code>ZoneId</code> (Java 8)</p></td>
<td><p>converter</p></td>
<td><p><code>{"zoneId" : "ECT - Europe/Paris"}</code></p></td>
</tr>
<tr>
<td><p><code>Box</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"box" : { "first" : { "x" : 1.0 , "y" : 2.0} , "second" : { "x" : 3.0 , "y" : 4.0}}</code></p></td>
</tr>
<tr>
<td><p><code>Polygon</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"polygon" : { "points" : [ { "x" : 1.0 , "y" : 2.0} , { "x" : 3.0 , "y" : 4.0} , { "x" : 4.0 , "y" : 5.0}]}}</code></p></td>
</tr>
<tr>
<td><p><code>Circle</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"circle" : { "center" : { "x" : 1.0 , "y" : 2.0} , "radius" : 3.0 , "metric" : "NEUTRAL"}}</code></p></td>
</tr>
<tr>
<td><p><code>Point</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"point" : { "x" : 1.0 , "y" : 2.0}}</code></p></td>
</tr>
<tr>
<td><p><code>GeoJsonPoint</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"point" : { "type" : "Point" , "coordinates" : [3.0 , 4.0] }}</code></p></td>
</tr>
<tr>
<td><p><code>GeoJsonMultiPoint</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"geoJsonLineString" : {"type":"MultiPoint", "coordinates": [ [ 0 , 0 ], [ 0 , 1 ], [ 1 , 1 ] ] }}</code></p></td>
</tr>
<tr>
<td><p><code>Sphere</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"sphere" : { "center" : { "x" : 1.0 , "y" : 2.0} , "radius" : 3.0 , "metric" : "NEUTRAL"}}</code></p></td>
</tr>
<tr>
<td><p><code>GeoJsonPolygon</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"polygon" : { "type" : "Polygon", "coordinates" : [[ [ 0 , 0 ], [ 3 , 6 ], [ 6 , 1 ], [ 0 , 0  ] ]] }}</code></p></td>
</tr>
<tr>
<td><p><code>GeoJsonMultiPolygon</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"geoJsonMultiPolygon" : { "type" : "MultiPolygon", "coordinates" : [
[ [ [ -73.958 , 40.8003 ] , [ -73.9498 , 40.7968 ] ] ],
[ [ [ -73.973 , 40.7648 ] , [ -73.9588 , 40.8003 ] ] ]
] }}</code></p></td>
</tr>
<tr>
<td><p><code>GeoJsonLineString</code></p></td>
<td><p>converter</p></td>
<td><p><code>{ "geoJsonLineString" : { "type" : "LineString", "coordinates" : [ [ 40 , 5 ], [ 41 , 6 ] ] }}</code></p></td>
</tr>
<tr>
<td><p><code>GeoJsonMultiLineString</code></p></td>
<td><p>converter</p></td>
<td><p><code>{"geoJsonLineString" : { "type" : "MultiLineString", coordinates: [
[ [ -73.97162 , 40.78205 ], [ -73.96374 , 40.77715 ] ],
[ [ -73.97880 , 40.77247 ], [ -73.97036 , 40.76811 ] ]
] }}</code></p></td>
</tr>
</tbody>
</table>
</div>
</details>

> [!NOTE]
> Collection Handling
>
> Collection handling depends on the actual values returned by MongoDB.
>
> - If a document does **not** contain a field mapped to a collection, the mapping will not update the property.
>   Which means the value will remain `null`, a java default or any value set during object creation.
> - If a document contains a field to be mapped, but the field holds a `null` value (like: `{ 'list' : null }`), the property value is set to `null`.
> - If a document contains a field to be mapped to a collection which is **not** `null` (like: `{ 'list' : [ … ] }`), the collection is populated with the mapped values.
>
> Generally, if you use constructor creation, then you can get hold of the value to be set.
> Property population can make use of default initialization values if a property value is not being provided by a query response.

<a id="mongodb-mapping-mapping--mapping-configuration"></a>

## Mapping Configuration

Unless explicitly configured, an instance of `MappingMongoConverter` is created by default when you create a `MongoTemplate`.
You can create your own instance of the `MappingMongoConverter`.
Doing so lets you dictate where in the classpath your domain classes can be found, so that Spring Data MongoDB can extract metadata and construct indexes.
Also, by creating your own instance, you can register Spring converters to map specific classes to and from the database.

You can configure the `MappingMongoConverter` as well as `com.mongodb.client.MongoClient` and MongoTemplate by using either Java-based or XML-based metadata.
The following example shows the configuration:

- Java
- XML

```java
@Configuration public class MongoConfig extends AbstractMongoClientConfiguration {
@Override public String getDatabaseName() {return "database";}
// the following are optional
@Override public String getMappingBasePackage() { (1) return "com.bigbank.domain";}
@Override void configureConverters(MongoConverterConfigurationAdapter adapter) { (2)
adapter.registerConverter(new org.springframework.data.mongodb.test.PersonReadConverter()); adapter.registerConverter(new org.springframework.data.mongodb.test.PersonWriteConverter());}
@Bean public LoggingEventListener<MongoMappingEvent> mappingEventsListener() {return new LoggingEventListener<MongoMappingEvent>();}}
```

**1**

The mapping base package defines the root path used to scan for entities used to pre initialize the `MappingContext`.
By default the configuration classes package is used.

**2**

Configure additional custom converters for specific domain types that replace the default mapping procedure for those types with your custom implementation.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:mongo="http://www.springframework.org/schema/data/mongo"
  xsi:schemaLocation="
    http://www.springframework.org/schema/data/mongo https://www.springframework.org/schema/data/mongo/spring-mongo.xsd
    http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans-3.0.xsd">

  <!-- Default bean name is 'mongo' -->
  <mongo:mongo-client host="localhost" port="27017"/>

  <mongo:db-factory dbname="database" mongo-ref="mongoClient"/>

  <!-- by default look for a Mongo object named 'mongo' - default name used for the converter is 'mappingConverter' -->
  <mongo:mapping-converter base-package="com.bigbank.domain">
    <mongo:custom-converters>
      <mongo:converter ref="readConverter"/>
      <mongo:converter>
        <bean class="org.springframework.data.mongodb.test.PersonWriteConverter"/>
      </mongo:converter>
    </mongo:custom-converters>
  </mongo:mapping-converter>

  <bean id="readConverter" class="org.springframework.data.mongodb.test.PersonReadConverter"/>

  <!-- set the mapping converter to be used by the MongoTemplate -->
  <bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
    <constructor-arg name="mongoDbFactory" ref="mongoDbFactory"/>
    <constructor-arg name="mongoConverter" ref="mappingConverter"/>
  </bean>

  <bean class="org.springframework.data.mongodb.core.mapping.event.LoggingEventListener"/>

</beans>
```

`AbstractMongoClientConfiguration` requires you to implement methods that define a `com.mongodb.client.MongoClient` as well as provide a database name.
`AbstractMongoClientConfiguration` also has a method named `getMappingBasePackage(…)` that you can override to tell the converter where to scan for classes annotated with the `@Document` annotation.

You can add additional converters to the converter by overriding the `customConversionsConfiguration` method.
MongoDB’s native JSR-310 support can be enabled through `MongoConverterConfigurationAdapter.useNativeDriverJavaTimeCodecs()`.
Also shown in the preceding example is a `LoggingEventListener`, which logs `MongoMappingEvent` instances that are posted onto Spring’s `ApplicationContextEvent` infrastructure.

> [!TIP]
> Java Time Types
>
> We recommend using MongoDB’s native JSR-310 support via `MongoConverterConfigurationAdapter.useNativeDriverJavaTimeCodecs()` as described above as it is using an `UTC` based approach.
> The default JSR-310 support for `java.time` types inherited from Spring Data Commons uses the local machine timezone as reference and should only be used for backwards compatibility.

> [!NOTE]
> `AbstractMongoClientConfiguration` creates a `MongoTemplate` instance and registers it with the container under the name `mongoTemplate`.

The `base-package` property tells it where to scan for classes annotated with the `@org.springframework.data.mongodb.core.mapping.Document` annotation.

> [!TIP]
> If you want to rely on [Spring Boot](https://spring.io/projects/spring-boot) to bootstrap Data MongoDB, but still want to override certain aspects of the configuration, you may want to expose beans of that type.
> For custom conversions you may eg. choose to register a bean of type `MongoCustomConversions` that will be picked up the by the Boot infrastructure.
> To learn more about this please make sure to read the Spring Boot [Reference Documentation](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#data.nosql.mongodb).

<a id="mongodb-mapping-mapping--mapping-usage"></a>
<a id="mongodb-mapping-mapping--metadata-based-mapping"></a>

## Metadata-based Mapping

To take full advantage of the object mapping functionality inside the Spring Data MongoDB support, you should annotate your mapped objects with the `@Document` annotation.
Although it is not necessary for the mapping framework to have this annotation (your POJOs are mapped correctly, even without any annotations), it lets the classpath scanner find and pre-process your domain objects to extract the necessary metadata.
If you do not use this annotation, your application takes a slight performance hit the first time you store a domain object, because the mapping framework needs to build up its internal metadata model so that it knows about the properties of your domain object and how to persist them.
The following example shows a domain object:

Example 1. Example domain object

```java
@Document
public class Person {

  @Id
  private ObjectId id;

  @Indexed
  private Integer ssn;

  private String firstName;

  @Indexed
  private String lastName;
}
```

> [!IMPORTANT]
> The `@Id` annotation tells the mapper which property you want to use for the MongoDB `_id` property, and the `@Indexed` annotation tells the mapping framework to call `createIndex(…)` on that property of your document, making searches faster.
> Automatic index creation is only done for types annotated with `@Document`.

> [!WARNING]
> Auto index creation is **disabled** by default and needs to be enabled through the configuration (see [Index Creation](#mongodb-mapping-mapping--mapping.index-creation)).

<a id="mongodb-mapping-mapping--mapping-usage-annotations"></a>
<a id="mongodb-mapping-mapping--mapping-annotation-overview"></a>

### Mapping Annotation Overview

The MappingMongoConverter can use metadata to drive the mapping of objects to documents.
The following annotations are available:

- `@Id`: Applied at the field level to mark the field used for identity purpose.
- `@MongoId`: Applied at the field level to mark the field used for identity purpose.
  Accepts an optional `FieldType` to customize id conversion.
- `@Document`: Applied at the class level to indicate this class is a candidate for mapping to the database.
  You can specify the name of the collection where the data will be stored.
- `@DBRef`: Applied at the field to indicate it is to be stored using a com.mongodb.DBRef.
- `@DocumentReference`: Applied at the field to indicate it is to be stored as a pointer to another document.
  This can be a single value (the *id* by default), or a `Document` provided via a converter.
- `@Indexed`: Applied at the field level to describe how to index the field.
- `@CompoundIndex` (repeatable): Applied at the type level to declare Compound Indexes.
- `@GeoSpatialIndexed`: Applied at the field level to describe how to geoindex the field.
- `@TextIndexed`: Applied at the field level to mark the field to be included in the text index.
- `@HashIndexed`: Applied at the field level for usage within a hashed index to partition data across a sharded cluster.
- `@Language`: Applied at the field level to set the language override property for text index.
- `@Transient`: By default, all fields are mapped to the document.
  This annotation excludes the field where it is applied from being stored in the database.
  Transient properties cannot be used within a persistence constructor as the converter cannot materialize a value for the constructor argument.
- `@PersistenceCreator`: Marks a given constructor or a `static` factory method - even a package protected one - to use when instantiating the object from the database.
  Constructor arguments are mapped by name to the key values in the retrieved Document.
- `@Value`: This annotation is part of the Spring Framework . Within the mapping framework it can be applied to constructor arguments.
  This lets you use a Spring Expression Language statement to transform a key’s value retrieved in the database before it is used to construct a domain object.
  In order to reference a property of a given document one has to use expressions like: `@Value("#root.myProperty")` where `root` refers to the root of the given document.
- `@Field`: Applied at the field level it allows to describe the name and type of the field as it will be represented in the MongoDB BSON document thus allowing the name and type to be different than the fieldname of the class as well as the property type.
- `@Version`: Applied at field level is used for optimistic locking and checked for modification on save operations.
  The initial value is `zero` (`one` for primitive types) which is bumped automatically on every update.

The mapping metadata infrastructure is defined in a separate spring-data-commons project that is technology agnostic.
Specific subclasses are using in the MongoDB support to support annotation based metadata.
Other strategies are also possible to put in place if there is demand.

<details>
<summary>Here is an example of a more complex mapping</summary>
<div>
<div>
<div>
<pre><code>@Document
@CompoundIndex(name = "age_idx", def = "{'lastName': 1, 'age': -1}")
public class Person&lt;T extends Address&gt; {

  @Id
  private String id;

  @Indexed(unique = true)
  private Integer ssn;

  @Field("fName")
  private String firstName;

  @Indexed
  private String lastName;

  private Integer age;

  @Transient
  private Integer accountTotal;

  @DBRef
  private List&lt;Account&gt; accounts;

  private T address;

  public Person(Integer ssn) {
    this.ssn = ssn;
  }

  @PersistenceCreator
  public Person(Integer ssn, String firstName, String lastName, Integer age, T address) {
    this.ssn = ssn;
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.address = address;
  }

  public String getId() {
    return id;
  }

  // no setter for Id.  (getter is only exposed for some unit testing)

  public Integer getSsn() {
    return ssn;
  }

// other getters/setters omitted
}</code></pre>
</div>
</div>
</div>
</details>

> [!TIP]
> `@Field(targetType=…)` can come in handy when the native MongoDB type inferred by the mapping infrastructure does not match the expected one.
> Like for `BigDecimal`, which is represented as `String` instead of `Decimal128`, just because earlier versions of MongoDB Server did not have support for it.
>
> ```java
> public class Balance {
>
>   @Field(targetType = STRING)
>   private BigDecimal value;
>
>   // ...
> }
> ```
>
> You may even consider your own, custom annotation.
>
> ```java
> @Target(ElementType.FIELD)
> @Retention(RetentionPolicy.RUNTIME)
> @Field(targetType = FieldType.STRING)
> public @interface AsString { }
>
> // ...
>
> public class Balance {
>
>   @AsString
>   private BigDecimal value;
>
>   // ...
> }
> ```

<a id="mongodb-mapping-mapping--_special_field_names"></a>
<a id="mongodb-mapping-mapping--special-field-names"></a>

### Special Field Names

Generally speaking MongoDB uses the dot (`.`) character as a path separator for nested documents or arrays.
This means that in a query (or update statement) a key like `a.b.c` targets an object structure as outlined below:

```json
{
    'a' : {
        'b' : {
            'c' : …
        }
    }
}
```

Therefore, up until MongoDB 5.0 field names must not contain dots (`.`).
Using a `MappingMongoConverter#setMapKeyDotReplacement` allowed circumvent some of the limitations when storing `Map` structures by substituting dots on write with another character.

```java
converter.setMapKeyDotReplacement("-");
// ...

source.map = Map.of("key.with.dot", "value")
converter.write(source,...) // -> map : { 'key-with-dot', 'value' }
```

With the release of MongoDB 5.0 this restriction on `Document` field names containing special characters was lifted.
We highly recommend reading more about limitations on using dots in field names in the [MongoDB Reference](https://www.mongodb.com/docs/manual/core/dot-dollar-considerations/).
To allow dots in `Map` structures please set `preserveMapKeys` on the `MappingMongoConverter`.

Using `@Field` allows customizing the field name to consider dots in two ways.

1. `@Field(name = "a.b")`: The name is considered to be a path.
   Operations expect a structure of nested objects such as `{ a : { b : … } }`.
2. `@Field(name = "a.b", fieldNameType = KEY)`: The names is considered a name as-is.
   Operations expect a field with the given value as `{ 'a.b' : ….. }`

> [!WARNING]
> Due to the special nature of the dot character in both MongoDB query and update statements field names containing dots cannot be targeted directly and therefore are excluded from being used in derived query methods.
> Consider the following `Item` having a `categoryId` property that is mapped to the field named `cat.id`.
>
> ```java
> public class Item {
>
> 	@Field(name = "cat.id", fieldNameType = KEY)
> 	String categoryId;
>
> 	// ...
> }
> ```
>
> Its raw representation will look like
>
> ```json
> {
>     'cat.id' : "5b28b5e7-52c2",
>     ...
> }
> ```
>
> Since we cannot target the `cat.id` field directly (as this would be interpreted as a path) we need the help of the [Aggregation Framework](#mongodb-aggregation-framework--mongo.aggregation).
>
> Query fields with a dot in its name
>
> ```java
> template.query(Item.class)
>     // $expr : { $eq : [ { $getField : { input : '$$CURRENT', 'cat.id' }, '5b28b5e7-52c2' ] }
>     .matching(expr(ComparisonOperators.valueOf(ObjectOperators.getValueOf("value")).equalToValue("5b28b5e7-52c2"))) (1)
>     .all();
> ```
>
> **1**
>
> The mapping layer takes care of translating the property name `value` into the actual field name.
> It is absolutely valid to use the target field name here as well.
>
> Update fields with a dot in its name
>
> ```java
> template.update(Item.class)
>     .matching(where("id").is("r2d2"))
>     // $replaceWith: { $setField : { input: '$$CURRENT', field : 'cat.id', value : 'af29-f87f4e933f97' } }
>     .apply(AggregationUpdate.newUpdate(ReplaceWithOperation.replaceWithValue(ObjectOperators.setValueTo("value", "af29-f87f4e933f97")))) (1)
>     .first();
> ```
>
> **1**
>
> The mapping layer takes care of translating the property name `value` into the actual field name.
> It is absolutely valid to use the target field name here as well.
>
> The above shows a simple example where the special field is present on the top document level.
> Increased levels of nesting increase the complexity of the aggregation expression required to interact with the field.

<a id="mongodb-mapping-mapping--mapping-custom-object-construction"></a>
<a id="mongodb-mapping-mapping--customized-object-construction"></a>

### Customized Object Construction

The mapping subsystem allows the customization of the object construction by annotating a constructor with the `@PersistenceCreator` annotation.
The values to be used for the constructor parameters are resolved in the following way:

- If a parameter is annotated with the `@Value` annotation, the given expression is evaluated and the result is used as the parameter value.
- If the Java type has a property whose name matches the given field of the input document, then it’s property information is used to select the appropriate constructor parameter to pass the input field value to.
  This works only if the parameter name information is present in the java `.class` files which can be achieved by compiling the source with debug information or using the new `-parameters` command-line switch for javac in Java 8.
- Otherwise, a `MappingException` will be thrown indicating that the given constructor parameter could not be bound.

```java
class OrderItem {

  private @Id String id;
  private int quantity;
  private double unitPrice;

  OrderItem(String id, @Value("#root.qty ?: 0") int quantity, double unitPrice) {
    this.id = id;
    this.quantity = quantity;
    this.unitPrice = unitPrice;
  }

  // getters/setters omitted
}

Document input = new Document("id", "4711");
input.put("unitPrice", 2.5);
input.put("qty",5);
OrderItem item = converter.read(OrderItem.class, input);
```

> [!NOTE]
> The SpEL expression in the `@Value` annotation of the `quantity` parameter falls back to the value `0` if the given property path cannot be resolved.

Additional examples for using the `@PersistenceCreator` annotation can be found in the [MappingMongoConverterUnitTests](https://github.com/spring-projects/spring-data-mongodb/blob/master/spring-data-mongodb/src/test/java/org/springframework/data/mongodb/core/convert/MappingMongoConverterUnitTests.java) test suite.

<a id="mongodb-mapping-mapping--mapping-usage-events"></a>
<a id="mongodb-mapping-mapping--mapping-framework-events"></a>

### Mapping Framework Events

Events are fired throughout the lifecycle of the mapping process.
This is described in the [Lifecycle Events](#mongodb-lifecycle-events) section.

Declaring these beans in your Spring ApplicationContext causes them to be invoked whenever the event is dispatched.

--
-

[1](#mongodb-mapping-mapping--_footnoteref_1). Uses UTC zone offset. Configure via [MongoConverterConfigurationAdapter](#mongodb-mapping-mapping--mapping-configuration)

[2](#mongodb-mapping-mapping--_footnoteref_2). Uses UTC zone offset. Configure via [MongoConverterConfigurationAdapter](#mongodb-mapping-mapping--mapping-configuration)

---

<a id="mongodb-mapping-mapping-schema"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/mapping-schema.html -->

<!-- page_index: 21 -->

# JSON Schema

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-mapping-schema--page-title"></a>
<a id="mongodb-mapping-mapping-schema--json-schema"></a>

# JSON Schema

As of version 3.6, MongoDB supports collections that validate documents against a provided [JSON Schema](https://docs.mongodb.com/manual/core/schema-validation/#json-schema).
The schema itself and both validation action and level can be defined when creating the collection, as the following example shows:

Example 1. Sample JSON schema

```json
{"type": "object",                                                        (1)
"required": [ "firstname", "lastname" ],                                 (2)
"properties": {                                                          (3)
"firstname": {                                                         (4) "type": "string","enum": [ "luke", "han" ] },"address": {                                                           (5) "type": "object","properties": {"postCode": { "type": "string", "minLength": 4, "maxLength": 5 }}}}}
```

**1**

JSON schema documents always describe a whole document from its root. A schema is a schema object itself that can contain
embedded schema objects that describe properties and subdocuments.

**2**

`required` is a property that describes which properties are required in a document. It can be specified optionally, along with other
schema constraints. See MongoDB’s documentation on [available keywords](https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/#available-keywords).

**3**

`properties` is related to a schema object that describes an `object` type. It contains property-specific schema constraints.

**4**

`firstname` specifies constraints for the `firstname` field inside the document. Here, it is a string-based `properties` element declaring
possible field values.

**5**

`address` is a subdocument defining a schema for values in its `postCode` field.

You can provide a schema either by specifying a schema document (that is, by using the `Document` API to parse or build a document object) or by building it with Spring Data’s JSON schema utilities in `org.springframework.data.mongodb.core.schema`. `MongoJsonSchema` is the entry point for all JSON schema-related operations. The following example shows how use `MongoJsonSchema.builder()` to create a JSON schema:

Example 2. Creating a JSON schema

```java
MongoJsonSchema.builder()                                                    (1)
    .required("lastname")                                                    (2)

    .properties(
                required(string("firstname").possibleValues("luke", "han")), (3)

                object("address")
                     .properties(string("postCode").minLength(4).maxLength(5)))

    .build();                                                                (4)
```

| **1** | Obtain a schema builder to configure the schema with a fluent API. |
| --- | --- |
| **2** | Configure required properties either directly as shown here or with more details as in 3. |
| **3** | Configure the required String-typed `firstname` field, allowing only `luke` and `han` values. Properties can be typed or untyped. Use a static import of `JsonSchemaProperty` to make the syntax slightly more compact and to get entry points such as `string(…)`. |
| **4** | Build the schema object. |

There are already some predefined and strongly typed schema objects (`JsonSchemaObject` and `JsonSchemaProperty`) available
through static methods on the gateway interfaces.
However, you may need to build custom property validation rules, which can be created through the builder API, as the following example shows:

```java
// "birthdate" : { "bsonType": "date" }
JsonSchemaProperty.named("birthdate").ofType(Type.dateType());

// "birthdate" : { "bsonType": "date", "description", "Must be a date" }
JsonSchemaProperty.named("birthdate").with(JsonSchemaObject.of(Type.dateType()).description("Must be a date"));
```

`CollectionOptions` provides the entry point to schema support for collections, as the following example shows:

Example 3. Create collection with `$jsonSchema`

```java
MongoJsonSchema schema = MongoJsonSchema.builder().required("firstname", "lastname").build();

template.createCollection(Person.class, CollectionOptions.empty().schema(schema));
```

<a id="mongodb-mapping-mapping-schema--mongo.jsonschema.generated"></a>
<a id="mongodb-mapping-mapping-schema--generating-a-schema"></a>

## Generating a Schema

Setting up a schema can be a time-consuming task, and we encourage everyone who decides to do so, to really take the time it takes.
It’s important, schema changes can be hard.
However, there might be times when one does not want to balked with it, and that is where `JsonSchemaCreator` comes into play.

`JsonSchemaCreator` and its default implementation generates a `MongoJsonSchema` out of domain types metadata provided by the mapping infrastructure.
This means, that [annotated properties](#mongodb-mapping-mapping--mapping-usage-annotations) as well as potential [custom conversions](#mongodb-mapping-mapping--mapping-configuration) are considered.

Example 4. Generate Json Schema from domain type

```java
public class Person {

    private final String firstname;                   (1)
    private final int age;                            (2)
    private Species species;                          (3)
    private Address address;                          (4)
    private @Field(fieldType=SCRIPT) String theForce; (5)
    private @Transient Boolean useTheForce;           (6)

    public Person(String firstname, int age) {        (1) (2)

        this.firstname = firstname;
        this.age = age;
    }

    // getter / setter omitted
}

MongoJsonSchema schema = MongoJsonSchemaCreator.create(mongoOperations.getConverter())
    .createSchemaFor(Person.class);

template.createCollection(Person.class, CollectionOptions.empty().schema(schema));
```

```json
{'type' : 'object','required' : ['age'],                     (2) 'properties' : {'firstname' : { 'type' : 'string' },  (1) 'age' : { 'bsonType' : 'int' }        (2) 'species' : {                         (3) 'type' : 'string','enum' : ['HUMAN', 'WOOKIE', 'UNKNOWN']} 'address' : {                         (4) 'type' : 'object' 'properties' : {'postCode' : { 'type': 'string' }} },'theForce' : { 'type' : 'javascript'} (5)}}
```

| **1** | Simple object properties are considers regular properties. |
| --- | --- |
| **2** | Primitive types are considered required properties |
| **3** | Enums are restricted to possible values. |
| **4** | Object type properties are inspected and represented as nested documents. |
| **5** | `String` type property that is converted to `Code` by the converter. |
| **6** | `@Transient` properties are omitted when generating the schema. |

> [!NOTE]
> `_id` properties using types that can be converted into `ObjectId` like `String` are mapped to `{ type : 'object' }`
> unless there is more specific information available via the `@MongoId` annotation.

| Java | Schema Type | Notes |
| --- | --- | --- |
| `Object` | `type : object` | with `properties` if metadata available. |
| `Collection` | `type : array` | - |
| `Map` | `type : object` | - |
| `Enum` | `type : string` | with `enum` property holding the possible enumeration values. |
| `array` | `type : array` | simple type array unless it’s a `byte[]` |
| `byte[]` | `bsonType : binData` | - |

The above example demonstrated how to derive the schema from a very precise typed source.
Using polymorphic elements within the domain model can lead to inaccurate schema representation for `Object` and generic `<T>` types, which are likely to represented as `{ type : 'object' }` without further specification.
`MongoJsonSchemaCreator.property(…)` allows defining additional details such as nested document types that should be considered when rendering the schema.

Example 5. Specify additional types for properties

```java
class Root {Object value;}
class A {String aValue;}
class B {String bValue;} MongoJsonSchemaCreator.create() .property("value").withTypes(A.class, B.class) (1)
```

```json
{'type' : 'object','properties' : {'value' : {'type' : 'object','properties' : {                       (1) 'aValue' : { 'type' : 'string' },'bValue' : { 'type' : 'string' }}}}}
```

**1**

Properties of the given types are merged into one element.

MongoDBs schema-free approach allows storing documents of different structure in one collection.
Those may be modeled having a common base class.
Regardless of the chosen approach, `MongoJsonSchemaCreator.merge(…)` can help circumvent the need of merging multiple schema into one.

Example 6. Merging multiple Schemas into a single Schema definition

```java
abstract class Root {String rootValue;}
class A extends Root {String aValue;}
class B extends Root {String bValue;}
MongoJsonSchemaCreator.mergedSchemaFor(A.class, B.class) (1)
```

```json
{'type' : 'object','properties' : { (1) 'rootValue' : { 'type' : 'string' },'aValue' : { 'type' : 'string' },'bValue' : { 'type' : 'string' }}}}
```

**1**

Properties (and their inherited ones) of the given types are combined into one schema.

> [!NOTE]
> Properties with the same name need to refer to the same JSON schema in order to be combined.
> The following example shows a definition that cannot be merged automatically because of a data type mismatch.
> In this case a `ConflictResolutionFunction` must be provided to `MongoJsonSchemaCreator`.
>
> ```java
> class A extends Root {
> 	String value;
> }
>
> class B extends Root {
> 	Integer value;
> }
> ```

<a id="mongodb-mapping-mapping-schema--mongo.jsonschema.encrypted-fields"></a>
<a id="mongodb-mapping-mapping-schema--encrypted-fields"></a>

## Encrypted Fields

MongoDB 4.2 [Field Level Encryption](https://docs.mongodb.com/master/core/security-client-side-encryption/) allows to directly encrypt individual properties.

Properties can be wrapped within an encrypted property when setting up the JSON Schema as shown in the example below.

Example 7. Client-Side Field Level Encryption via Json Schema

```java
MongoJsonSchema schema = MongoJsonSchema.builder()
    .properties(
        encrypted(string("ssn"))
            .algorithm("AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic")
            .keyId("*key0_id")
	).build();
```

Instead of defining encrypted fields manually it is possible leverage the `@Encrypted` annotation as shown in the snippet below.

Example 8. Client-Side Field Level Encryption via Json Schema

```java
@Document
@Encrypted(keyId = "xKVup8B1Q+CkHaVRx+qa+g==", algorithm = "AEAD_AES_256_CBC_HMAC_SHA_512-Random") (1)
static class Patient {

    @Id String id;
    String name;

    @Encrypted (2)
    String bloodType;

    @Encrypted(algorithm = "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic") (3)
    Integer ssn;
}
```

| **1** | Default encryption settings that will be set for `encryptMetadata`. |
| --- | --- |
| **2** | Encrypted field using default encryption settings. |
| **3** | Encrypted field overriding the default encryption algorithm. |

> [!TIP]
> The `@Encrypted` Annotation supports resolving keyIds via SpEL Expressions.
> To do so additional environment metadata (via the `MappingContext`) is required and must be provided.
>
> ```java
> @Document
> @Encrypted(keyId = "#{mongocrypt.keyId(#target)}")
> static class Patient {
>
>     @Id String id;
>     String name;
>
>     @Encrypted(algorithm = "AEAD_AES_256_CBC_HMAC_SHA_512-Random")
>     String bloodType;
>
>     @Encrypted(algorithm = "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic")
>     Integer ssn;
> }
>
> MongoJsonSchemaCreator schemaCreator = MongoJsonSchemaCreator.create(mappingContext);
> MongoJsonSchema patientSchema = schemaCreator
>     .filter(MongoJsonSchemaCreator.encryptedOnly())
>     .createSchemaFor(Patient.class);
> ```
>
> The `mongocrypt.keyId` function is defined via an `EvaluationContextExtension` as shown in the snippet below.
> Providing a custom extension provides the most flexible way of computing keyIds.
>
> ```java
> public class EncryptionExtension implements EvaluationContextExtension {
> @Override public String getExtensionId() {return "mongocrypt";}
> @Override public Map<String, Function> getFunctions() {return Collections.singletonMap("keyId", new Function(getMethod("computeKeyId", String.class), this));}
> public String computeKeyId(String target) {// ... lookup via target element name}}
> ```

<a id="mongodb-mapping-mapping-schema--mongo.jsonschema.types"></a>
<a id="mongodb-mapping-mapping-schema--json-schema-types"></a>

## JSON Schema Types

The following table shows the supported JSON schema types:

| Schema Type | Java Type | Schema Properties |
| --- | --- | --- |
| `untyped` | - | `description`, generated `description`, `enum`, `allOf`, `anyOf`, `oneOf`, `not` |
| `object` | `Object` | `required`, `additionalProperties`, `properties`, `minProperties`, `maxProperties`, `patternProperties` |
| `array` | any array except `byte[]` | `uniqueItems`, `additionalItems`, `items`, `minItems`, `maxItems` |
| `string` | `String` | `minLength`, `maxLentgth`, `pattern` |
| `int` | `int`, `Integer` | `multipleOf`, `minimum`, `exclusiveMinimum`, `maximum`, `exclusiveMaximum` |
| `long` | `long`, `Long` | `multipleOf`, `minimum`, `exclusiveMinimum`, `maximum`, `exclusiveMaximum` |
| `double` | `float`, `Float`, `double`, `Double` | `multipleOf`, `minimum`, `exclusiveMinimum`, `maximum`, `exclusiveMaximum` |
| `decimal` | `BigDecimal` | `multipleOf`, `minimum`, `exclusiveMinimum`, `maximum`, `exclusiveMaximum` |
| `number` | `Number` | `multipleOf`, `minimum`, `exclusiveMinimum`, `maximum`, `exclusiveMaximum` |
| `binData` | `byte[]` | (none) |
| `boolean` | `boolean`, `Boolean` | (none) |
| `null` | `null` | (none) |
| `objectId` | `ObjectId` | (none) |
| `date` | `java.util.Date` | (none) |
| `timestamp` | `BsonTimestamp` | (none) |
| `regex` | `java.util.regex.Pattern` | (none) |

> [!NOTE]
> `untyped` is a generic type that is inherited by all typed schema types. It provides all `untyped` schema properties to typed schema types.

For more information, see [$jsonSchema](https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/#op._S_jsonSchema).

---

<a id="mongodb-mapping-custom-conversions"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/custom-conversions.html -->

<!-- page_index: 22 -->

# Custom Conversions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-custom-conversions--page-title"></a>
<a id="mongodb-mapping-custom-conversions--custom-conversions"></a>

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

<a id="mongodb-mapping-custom-conversions--customconversions.converter-disambiguation"></a>
<a id="mongodb-mapping-custom-conversions--converter-disambiguation"></a>

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

<a id="mongodb-mapping-custom-conversions--mongo.custom-converters"></a>
<a id="mongodb-mapping-custom-conversions--type-based-converter"></a>

## Type based Converter

The most trivial way of influencing the mapping result is by specifying the desired native MongoDB target type via the `@Field` annotation.
This allows to work with non MongoDB types like `BigDecimal` in the domain model while persisting values in eg. `String` format.

Example 1. Explicit target type mapping

```java
public class Payment {

  @Id String id; (1)

  @Field(targetType = FieldType.STRING) (2)
  BigDecimal value;

  Date date; (3)

}
```

```java
{
  "_id"   : ObjectId("5ca4a34fa264a01503b36af8"), (1)
  "value" : "2.099",                              (2)
  "date"  : ISODate("2019-04-03T12:11:01.870Z")   (3)
}
```

**1**

String *id* values that represent a valid `ObjectId` are converted automatically. See [How the `_id` Field is Handled in the Mapping Layer](#mongodb-template-crud-operations--mongo-template.id-handling)
for details.

**2**

The desired target type is explicitly defined as `String`.
Otherwise.

**3**

`Date` values are handled by the MongoDB driver itself are stored as `ISODate`.

The snippet above is handy for providing simple type hints. To gain more fine-grained control over the mapping process, you can register Spring converters with the `MongoConverter` implementations, such as the `MappingMongoConverter`.

The `MappingMongoConverter` checks to see if any Spring converters can handle a specific class before attempting to map the object itself. To 'hijack' the normal mapping strategies of the `MappingMongoConverter`, perhaps for increased performance or other custom mapping needs, you first need to create an implementation of the Spring `Converter` interface and then register it with the `MappingConverter`.

> [!NOTE]
> For more information on the Spring type conversion service, see the reference docs [here](https://docs.spring.io/spring-framework/reference/7.0/core.html#validation).

<a id="mongodb-mapping-custom-conversions--mongo.custom-converters.writer"></a>
<a id="mongodb-mapping-custom-conversions--writing-converter"></a>

### Writing Converter

The following example shows an implementation of the `Converter` that converts from a `Person` object to a `org.bson.Document`:

```java
import org.springframework.core.convert.converter.Converter;

import org.bson.Document;

public class PersonWriteConverter implements Converter<Person, Document> {

  public Document convert(Person source) {
    Document document = new Document();
    document.put("_id", source.getId());
    document.put("name", source.getFirstName());
    document.put("age", source.getAge());
    return document;
  }
}
```

<a id="mongodb-mapping-custom-conversions--mongo.custom-converters.reader"></a>
<a id="mongodb-mapping-custom-conversions--reading-converter"></a>

### Reading Converter

The following example shows an implementation of a `Converter` that converts from a `Document` to a `Person` object:

```java
public class PersonReadConverter implements Converter<Document, Person> {
public Person convert(Document source) {Person p = new Person((ObjectId) source.get("_id"), (String) source.get("name")); p.setAge((Integer) source.get("age")); return p;}}
```

<a id="mongodb-mapping-custom-conversions--mongo.custom-converters.xml"></a>
<a id="mongodb-mapping-custom-conversions--registering-converters"></a>

### Registering Converters

```java
class MyMongoConfiguration extends AbstractMongoClientConfiguration {
@Override public String getDatabaseName() {return "database";}
@Override protected void configureConverters(MongoConverterConfigurationAdapter adapter) {adapter.registerConverter(new com.example.PersonReadConverter()); adapter.registerConverter(new com.example.PersonWriteConverter());}}
```

<a id="mongodb-mapping-custom-conversions--mongo.numeric-conversion"></a>
<a id="mongodb-mapping-custom-conversions--big-number-format"></a>

## Big Number Format

MongoDB in its early days did not have support for large numeric values such as `BigDecimal`.
To persist `BigDecimal` and `BigInteger` values, Spring Data MongoDB converted values their `String` representation.
This approach had several downsides due to lexical instead of numeric comparison for queries, updates, etc.

With MongoDB Server 3.4, `org.bson.types.Decimal128` offers a native representation for `BigDecimal` and `BigInteger`.
As of Spring Data MongoDB 5.0. there no longer is a default representation of those types and conversion needs to be configured explicitly.
You can register multiple formats, 1st being default, and still retain the previous behaviour by configuring the `BigDecimalRepresentation` in `MongoCustomConversions` through `MongoCustomConversions.create(config → config.bigDecimal(BigDecimalRepresentation.STRING, BigDecimalRepresentation.DECIMAL128))`.
This allows you to make use of the explicit storage type format via `@Field(targetType = DECIMAL128)` while keeping default conversion set to String.
Choosing none of the provided representations is valid as long as those values are no persisted.

> [!NOTE]
> Very large values, though being a valid `BigDecimal` or `BigInteger`, might exceed the maximum bit length of `org.bson.types.Decimal128` in their store native representation.

---

<a id="mongodb-mapping-property-converters"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/property-converters.html -->

<!-- page_index: 23 -->

# Property Converters

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-property-converters--page-title"></a>
<a id="mongodb-mapping-property-converters--property-converters"></a>

# Property Converters

While [type-based conversion](#mongodb-mapping-custom-conversions) already offers ways to influence the conversion and representation of certain types within the target store, it has limitations when only certain values or properties of a particular type should be considered for conversion.
Property-based converters allow configuring conversion rules on a per-property basis, either declaratively (via `@ValueConverter`) or programmatically (by registering a `PropertyValueConverter` for a specific property).

A `PropertyValueConverter` can transform a given value into its store representation (write) and back (read) as the following listing shows.
The additional `ValueConversionContext` provides additional information, such as mapping metadata and direct `read` and `write` methods.

Example 1. A simple PropertyValueConverter

```java
class ReversingValueConverter implements PropertyValueConverter<String, String, ValueConversionContext> {
@Override public String read(String value, ValueConversionContext context) {return reverse(value);}
@Override public String write(String value, ValueConversionContext context) {return reverse(value);}}
```

You can obtain `PropertyValueConverter` instances from `CustomConversions#getPropertyValueConverter(…)` by delegating to `PropertyValueConversions`, typically by using a `PropertyValueConverterFactory` to provide the actual converter.
Depending on your application’s needs, you can chain or decorate multiple instances of `PropertyValueConverterFactory` — for example, to apply caching.
By default, Spring Data MongoDB uses a caching implementation that can serve types with a default constructor or enum values.
A set of predefined factories is available through the factory methods in `PropertyValueConverterFactory`.
You can use `PropertyValueConverterFactory.beanFactoryAware(…)` to obtain a `PropertyValueConverter` instance from an `ApplicationContext`.

You can change the default behavior through `ConverterConfiguration`.

<a id="mongodb-mapping-property-converters--mongo.property-converters.declarative"></a>
<a id="mongodb-mapping-property-converters--declarative-value-converter"></a>

## Declarative Value Converter

The most straight forward usage of a `PropertyValueConverter` is by annotating properties with the `@ValueConverter` annotation that defines the converter type:

Example 2. Declarative PropertyValueConverter

```java
class Person {

  @ValueConverter(ReversingValueConverter.class)
  String ssn;
}
```

<a id="mongodb-mapping-property-converters--mongo.property-converters.programmatic"></a>
<a id="mongodb-mapping-property-converters--programmatic-value-converter-registration"></a>

## Programmatic Value Converter Registration

Programmatic registration registers `PropertyValueConverter` instances for properties within an entity model by using a `PropertyValueConverterRegistrar`, as the following example shows.
The difference between declarative registration and programmatic registration is that programmatic registration happens entirely outside of the entity model.
Such an approach is useful if you cannot or do not want to annotate the entity model.

Example 3. Programmatic PropertyValueConverter registration

```java
PropertyValueConverterRegistrar registrar = new PropertyValueConverterRegistrar();

registrar.registerConverter(Address.class, "street", new PropertyValueConverter() { … }); (1)

// type safe registration
registrar.registerConverter(Person.class, Person::getSsn())                               (2)
  .writing(value -> encrypt(value))
  .reading(value -> decrypt(value));
```

**1**

Register a converter for the field identified by its name.

**2**

Type safe variant that allows to register a converter and its conversion functions.
This method uses class proxies to determine the property.
Make sure that neither the class nor the accessors are `final` as otherwise this approach doesn’t work.

> [!WARNING]
> Dot notation (such as `registerConverter(Person.class, "address.street", …)`) for navigating across properties into subdocuments is **not** supported when registering converters.

> [!TIP]
> `MongoValueConverter` offers a pre-typed `PropertyValueConverter` interface that uses `MongoConversionContext`.

<a id="mongodb-mapping-property-converters--mongocustomconversions-configuration"></a>

## MongoCustomConversions configuration

By default, `MongoCustomConversions` can handle declarative value converters, depending on the configured `PropertyValueConverterFactory`.
`MongoConverterConfigurationAdapter` helps to set up programmatic value conversions or define the `PropertyValueConverterFactory` to be used.

Example 4. Configuration Sample

```java
MongoCustomConversions.create(configurationAdapter -> {

    SimplePropertyValueConversions valueConversions = new SimplePropertyValueConversions();
    valueConversions.setConverterFactory(…);
    valueConversions.setValueConverterRegistry(new PropertyValueConverterRegistrar()
        .registerConverter(…)
        .buildRegistry());

    configurationAdapter.setPropertyValueConversions(valueConversions);
});
```

---

<a id="mongodb-mapping-unwrapping-entities"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/unwrapping-entities.html -->

<!-- page_index: 24 -->

# Unwrapping Types

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-unwrapping-entities--page-title"></a>
<a id="mongodb-mapping-unwrapping-entities--unwrapping-types"></a>

# Unwrapping Types

Unwrapped entities are used to design value objects in your Java domain model whose properties are flattened out into the parent’s MongoDB Document.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.mapping"></a>
<a id="mongodb-mapping-unwrapping-entities--unwrapped-types-mapping"></a>

## Unwrapped Types Mapping

Consider the following domain model where `User.name` is annotated with `@Unwrapped`.
The `@Unwrapped` annotation signals that all properties of `UserName` should be flattened out into the `user` document that owns the `name` property.

Example 1. Sample Code of unwrapping objects

```java
class User {

    @Id
    String userId;

    @Unwrapped(onEmpty = USE_NULL) (1)
    UserName name;
}

class UserName {

    String firstname;

    String lastname;

}
```

```json
{
  "_id" : "1da2ba06-3ba7",
  "firstname" : "Emma",
  "lastname" : "Frost"
}
```

**1**

When loading the `name` property its value is set to `null` if both `firstname` and `lastname` are either `null` or not present.
By using `onEmpty=USE_EMPTY` an empty `UserName`, with potential `null` value for its properties, will be created.

For less verbose embeddable type declarations use `@Unwrapped.Nullable` and `@Unwrapped.Empty` instead `@Unwrapped(onEmpty = USE_NULL)` and `@Unwrapped(onEmpty = USE_EMPTY)`.
Both annotations are meta-annotated with JSR-305 `@javax.annotation.Nonnull` to aid with nullability inspections.

> [!WARNING]
> It is possible to use complex types within an unwrapped object.
> However, those must not be, nor contain unwrapped fields themselves.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.mapping.field-names"></a>
<a id="mongodb-mapping-unwrapping-entities--unwrapped-types-field-names"></a>

## Unwrapped Types field names

A value object can be unwrapped multiple times by using the optional `prefix` attribute of the `@Unwrapped` annotation.
By dosing so the chosen prefix is prepended to each property or `@Field("…")` name in the unwrapped object.
Please note that values will overwrite each other if multiple properties render to the same field name.

Example 2. Sample Code of unwrapped object with name prefix

```java
class User {

    @Id
    String userId;

    @Unwrapped.Nullable(prefix = "u_") (1)
    UserName name;

    @Unwrapped.Nullable(prefix = "a_") (2)
    UserName name;
}

class UserName {

    String firstname;

    String lastname;
}
```

```json
{
  "_id" : "a6a805bd-f95f",
  "u_firstname" : "Jean",             (1)
  "u_lastname" : "Grey",
  "a_firstname" : "Something",        (2)
  "a_lastname" : "Else"
}
```

**1**

All properties of `UserName` are prefixed with `u_`.

**2**

All properties of `UserName` are prefixed with `a_`.

While combining the `@Field` annotation with `@Unwrapped` on the very same property does not make sense and therefore leads to an error.
It is a totally valid approach to use `@Field` on any of the unwrapped types properties.

Example 3. Sample Code unwrapping objects with `@Field` annotation

```java
public class User {

	@Id
    private String userId;

    @Unwrapped.Nullable(prefix = "u-") (1)
    UserName name;
}

public class UserName {

	@Field("first-name")              (2)
    private String firstname;

	@Field("last-name")
    private String lastname;
}
```

```json
{
  "_id" : "2647f7b9-89da",
  "u-first-name" : "Barbara",         (2)
  "u-last-name" : "Gordon"
}
```

**1**

All properties of `UserName` are prefixed with `u-`.

**2**

Final field names are a result of concatenating `@Unwrapped(prefix)` and `@Field(name)`.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.queries"></a>
<a id="mongodb-mapping-unwrapping-entities--query-on-unwrapped-objects"></a>

## Query on Unwrapped Objects

Defining queries on unwrapped properties is possible on type- as well as field-level as the provided `Criteria` is matched against the domain type.
Prefixes and potential custom field names will be considered when rendering the actual query.
Use the property name of the unwrapped object to match against all contained fields as shown in the sample below.

Example 4. Query on unwrapped object

```java
UserName userName = new UserName("Carol", "Danvers")
Query findByUserName = query(where("name").is(userName));
User user = template.findOne(findByUserName, User.class);
```

```json
db.collection.find({
  "firstname" : "Carol",
  "lastname" : "Danvers"
})
```

It is also possible to address any field of the unwrapped object directly using its property name as shown in the snippet below.

Example 5. Query on field of unwrapped object

```java
Query findByUserFirstName = query(where("name.firstname").is("Shuri"));
List<User> users = template.findAll(findByUserFirstName, User.class);
```

```json
db.collection.find({
  "firstname" : "Shuri"
})
```

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.queries.sort"></a>
<a id="mongodb-mapping-unwrapping-entities--sort-by-unwrapped-field."></a>

### Sort by unwrapped field.

Fields of unwrapped objects can be used for sorting via their property path as shown in the sample below.

Example 6. Sort on unwrapped field

```java
Query findByUserLastName = query(where("name.lastname").is("Romanoff"));
List<User> user = template.findAll(findByUserName.withSort(Sort.by("name.firstname")), User.class);
```

```json
db.collection.find({
  "lastname" : "Romanoff"
}).sort({ "firstname" : 1 })
```

> [!NOTE]
> Though possible, using the unwrapped object itself as sort criteria includes all of its fields in unpredictable order and may result in inaccurate ordering.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.queries.project"></a>
<a id="mongodb-mapping-unwrapping-entities--field-projection-on-unwrapped-objects"></a>

### Field projection on unwrapped objects

Fields of unwrapped objects can be subject for projection either as a whole or via single fields as shown in the samples below.

Example 7. Project on unwrapped object.

```java
Query findByUserLastName = query(where("name.firstname").is("Gamora"));
findByUserLastName.fields().include("name");                             (1)
List<User> user = template.findAll(findByUserName, User.class);
```

```json
db.collection.find({
  "lastname" : "Gamora"
},
{
  "firstname" : 1,
  "lastname" : 1
})
```

**1**

A field projection on an unwrapped object includes all of its properties.

Example 8. Project on a field of an unwrapped object.

```java
Query findByUserLastName = query(where("name.lastname").is("Smoak"));
findByUserLastName.fields().include("name.firstname");                   (1)
List<User> user = template.findAll(findByUserName, User.class);
```

```json
db.collection.find({
  "lastname" : "Smoak"
},
{
  "firstname" : 1
})
```

**1**

A field projection on an unwrapped object includes all of its properties.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.queries.by-example"></a>
<a id="mongodb-mapping-unwrapping-entities--query-by-example-on-unwrapped-object."></a>

### Query By Example on unwrapped object.

Unwrapped objects can be used within an `Example` probe just as any other type.
Please review the [Query By Example](#mongodb-template-query-operations--mongo.query-by-example) section, to learn more about this feature.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.queries.repository"></a>
<a id="mongodb-mapping-unwrapping-entities--repository-queries-on-unwrapped-objects."></a>

### Repository Queries on unwrapped objects.

The `Repository` abstraction allows deriving queries on fields of unwrapped objects as well as the entire object.

Example 9. Repository queries on unwrapped objects.

```java
interface UserRepository extends CrudRepository<User, String> {

	List<User> findByName(UserName username);         (1)

	List<User> findByNameFirstname(String firstname); (2)
}
```

**1**

Matches against all fields of the unwrapped object.

**2**

Matches against the `firstname`.

> [!NOTE]
> Index creation for unwrapped objects is suspended even if the repository `create-query-indexes` namespace attribute is set to `true`.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.update"></a>
<a id="mongodb-mapping-unwrapping-entities--update-on-unwrapped-objects"></a>

## Update on Unwrapped Objects

Unwrapped objects can be updated as any other object that is part of the domain model.
The mapping layer takes care of flattening structures into their surroundings.
It is possible to update single attributes of the unwrapped object as well as the entire value as shown in the examples below.

Example 10. Update a single field of an unwrapped object.

```java
Update update = new Update().set("name.firstname", "Janet");
template.update(User.class).matching(where("id").is("Wasp"))
   .apply(update).first()
```

```json
db.collection.update({"_id" : "Wasp" },{"$set" { "firstname" : "Janet" } },{ ... })
```

Example 11. Update an unwrapped object.

```java
Update update = new Update().set("name", new Name("Janet", "van Dyne"));
template.update(User.class).matching(where("id").is("Wasp"))
   .apply(update).first()
```

```json
db.collection.update({"_id" : "Wasp" },{"$set" {"firstname" : "Janet","lastname" : "van Dyne",} },{ ... })
```

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.aggregations"></a>
<a id="mongodb-mapping-unwrapping-entities--aggregations-on-unwrapped-objects"></a>

## Aggregations on Unwrapped Objects

The [Aggregation Framework](#mongodb-aggregation-framework) will attempt to map unwrapped values of typed aggregations.
Please make sure to work with the property path including the wrapper object when referencing one of its values.
Other than that no special action is required.

<a id="mongodb-mapping-unwrapping-entities--unwrapped-entities.indexes"></a>
<a id="mongodb-mapping-unwrapping-entities--index-on-unwrapped-objects"></a>

## Index on Unwrapped Objects

It is possible to attach the `@Indexed` annotation to properties of an unwrapped type just as it is done with regular objects.
It is not possible to use `@Indexed` along with the `@Unwrapped` annotation on the owning property.

```java
public class User {

	@Id
    private String userId;

    @Unwrapped(onEmpty = USE_NULL)
    UserName name;                    (1)

    // Invalid -> InvalidDataAccessApiUsageException
    @Indexed                          (2)
    @Unwrapped(onEmpty = USE_Empty)
    Address address;
}

public class UserName {

    private String firstname;

    @Indexed
    private String lastname;           (1)
}
```

**1**

Index created for `lastname` in `users` collection.

**2**

Invalid `@Indexed` usage along with `@Unwrapped`

---

<a id="mongodb-mapping-document-references"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/document-references.html -->

<!-- page_index: 25 -->

# Using DBRefs

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-document-references--page-title"></a>
<a id="mongodb-mapping-document-references--using-dbrefs"></a>

# Using DBRefs

The mapping framework does not have to store child objects embedded within the document.
You can also store them separately and use a `DBRef` to refer to that document.
When the object is loaded from MongoDB, those references are eagerly resolved so that you get back a mapped object that looks the same as if it had been stored embedded within your top-level document.

The following example uses a DBRef to refer to a specific document that exists independently of the object in which it is referenced (both classes are shown in-line for brevity’s sake):

```java
@Document
public class Account {

  @Id
  private ObjectId id;
  private Float total;
}

@Document
public class Person {

  @Id
  private ObjectId id;
  @Indexed
  private Integer ssn;
  @DBRef
  private List<Account> accounts;
}
```

You need not use `@OneToMany` or similar mechanisms because the List of objects tells the mapping framework that you want a one-to-many relationship.
When the object is stored in MongoDB, there is a list of DBRefs rather than the `Account` objects themselves.
When it comes to loading collections of `DBRef`s it is advisable to restrict references held in collection types to a specific MongoDB collection.
This allows bulk loading of all references, whereas references pointing to different MongoDB collections need to be resolved one by one.

> [!IMPORTANT]
> The mapping framework does not handle cascading saves.
> If you change an `Account` object that is referenced by a `Person` object, you must save the `Account` object separately.
> Calling `save` on the `Person` object does not automatically save the `Account` objects in the `accounts` property.

`DBRef`s can also be resolved lazily.
In this case the actual `Object` or `Collection` of references is resolved on first access of the property.
Use the `lazy` attribute of `@DBRef` to specify this.
Required properties that are also defined as lazy loading `DBRef` and used as constructor arguments are also decorated with the lazy loading proxy making sure to put as little pressure on the database and network as possible.

> [!TIP]
> Lazily loaded `DBRef`s can be hard to debug.
> Make sure tooling does not accidentally trigger proxy resolution by e.g. calling `toString()` or some inline debug rendering invoking property getters.
> Please consider to enable *trace* logging for `org.springframework.data.mongodb.core.convert.DefaultDbRefResolver` to gain insight on `DBRef` resolution.
> Though technically possible, avoid saving back individual lazily loaded entities obtained via properties of the referencing root.

> [!WARNING]
> Lazy loading may require class proxies, that in turn, might need access to jdk internals, that are not open, starting with Java 16+, due to [JEP 396: Strongly Encapsulate JDK Internals by Default](https://openjdk.java.net/jeps/396).
> For those cases please consider falling back to an interface type (eg. switch from `ArrayList` to `List`) or provide the required `--add-opens` argument.

<a id="mongodb-mapping-document-references--mapping-usage.document-references"></a>
<a id="mongodb-mapping-document-references--using-document-references"></a>

## Using Document References

Using `@DocumentReference` offers a flexible way of referencing entities in MongoDB.
While the goal is the same as when using [DBRefs](#mongodb-mapping-document-references), the store representation is different.
`DBRef` resolves to a document with a fixed structure as outlined in the [MongoDB Reference documentation](https://docs.mongodb.com/manual/reference/database-references/).
Document references, do not follow a specific format.
They can be literally anything, a single value, an entire document, basically everything that can be stored in MongoDB.
By default, the mapping layer will use the referenced entities *id* value for storage and retrieval, like in the sample below.

```java
@Document
class Account {

  @Id
  String id;
  Float total;
}

@Document
class Person {

  @Id
  String id;

  @DocumentReference                                   (1)
  List<Account> accounts;
}
```

```java
Account account = …

template.insert(account);                               (2)

template.update(Person.class)
  .matching(where("id").is(…))
  .apply(new Update().push("accounts").value(account)) (3)
  .first();
```

```json
{
  "_id" : …,
  "accounts" : [ "6509b9e" … ]                        (4)
}
```

| **1** | Mark the collection of `Account` values to be referenced. |
| --- | --- |
| **2** | The mapping framework does not handle cascading saves, so make sure to persist the referenced entity individually. |
| **3** | Add the reference to the existing entity. |
| **4** | Referenced `Account` entities are represented as an array of their `_id` values. |

The sample above uses an `_id`-based fetch query (`{ '_id' : ?#{#target} }`) for data retrieval and resolves linked entities eagerly.
It is possible to alter resolution defaults (listed below) using the attributes of `@DocumentReference`

| Attribute | Description | Default |
| --- | --- | --- |
| `db` | The target database name for collection lookup. | `MongoDatabaseFactory.getMongoDatabase()` |
| `collection` | The target collection name. | The annotated property’s domain type, respectively the value type in case of `Collection` like or `Map` properties, collection name. |
| `lookup` | The single document lookup query evaluating placeholders via SpEL expressions using `#target` as the marker for a given source value. `Collection` like or `Map` properties combine individual lookups via an `$or` operator. | An `_id` field based query (`{ '_id' : ?#{#target} }`) using the loaded source value. |
| `sort` | Used for sorting result documents on server side. | None by default. Result order of `Collection` like properties is restored based on the used lookup query on a best-effort basis. |
| `lazy` | If set to `true` value resolution is delayed upon first access of the property. | Resolves properties eagerly by default. |

> [!WARNING]
> Lazy loading may require class proxies, that in turn, might need access to jdk internals, that are not open, starting with Java 16+, due to [JEP 396: Strongly Encapsulate JDK Internals by Default](https://openjdk.java.net/jeps/396).
> For those cases please consider falling back to an interface type (eg. switch from `ArrayList` to `List`) or provide the required `--add-opens` argument.

`@DocumentReference(lookup)` allows defining filter queries that can be different from the `_id` field and therefore offer a flexible way of defining references between entities as demonstrated in the sample below, where the `Publisher` of a book is referenced by its acronym instead of the internal `id`.

```java
@Document
class Book {

  @Id
  ObjectId id;
  String title;
  List<String> author;

  @Field("publisher_ac")
  @DocumentReference(lookup = "{ 'acronym' : ?#{#target} }") (1)
  Publisher publisher;
}

@Document
class Publisher {

  @Id
  ObjectId id;
  String acronym;                                            (1)
  String name;

  @DocumentReference(lazy = true)                            (2)
  List<Book> books;

}
```

`Book` document

```json
{
  "_id" : 9a48e32,
  "title" : "The Warded Man",
  "author" : ["Peter V. Brett"],
  "publisher_ac" : "DR"
}
```

`Publisher` document

```json
{
  "_id" : 1a23e45,
  "acronym" : "DR",
  "name" : "Del Rey",
  …
}
```

**1**

Use the `acronym` field to query for entities in the `Publisher` collection.

**2**

Lazy load back references to the `Book` collection.

The above snippet shows the reading side of things when working with custom referenced objects.
Writing requires a bit of additional setup as the mapping information do not express where `#target` stems from.
The mapping layer requires registration of a `Converter` between the target document and `DocumentPointer`, like the one below:

```java
@WritingConverter class PublisherReferenceConverter implements Converter<Publisher, DocumentPointer<String>> {
@Override public DocumentPointer<String> convert(Publisher source) {return () -> source.getAcronym();}}
```

If no `DocumentPointer` converter is provided the target reference document can be computed based on the given lookup query.
In this case the association target properties are evaluated as shown in the following sample.

```java
@Document
class Book {

  @Id
  ObjectId id;
  String title;
  List<String> author;

  @DocumentReference(lookup = "{ 'acronym' : ?#{acc} }") (1) (2)
  Publisher publisher;
}

@Document
class Publisher {

  @Id
  ObjectId id;
  String acronym;                                        (1)
  String name;

  // ...
}
```

```json
{"_id" : 9a48e32,"title" : "The Warded Man","author" : ["Peter V. Brett"],"publisher" : {"acc" : "DOC"}}
```

**1**

Use the `acronym` field to query for entities in the `Publisher` collection.

**2**

The field value placeholders of the lookup query (like `acc`) is used to form the reference document.

It is also possible to model relational style *One-To-Many* references using a combination of `@ReadonlyProperty` and `@DocumentReference`.
This approach allows link types without storing the linking values within the owning document but rather on the referencing document as shown in the example below.

```java
@Document
class Book {

  @Id
  ObjectId id;
  String title;
  List<String> author;

  ObjectId publisherId;                                        (1)
}

@Document
class Publisher {

  @Id
  ObjectId id;
  String acronym;
  String name;

  @ReadOnlyProperty                                            (2)
  @DocumentReference(lookup="{'publisherId':?#{#self._id} }")  (3)
  List<Book> books;
}
```

`Book` document

```json
{
  "_id" : 9a48e32,
  "title" : "The Warded Man",
  "author" : ["Peter V. Brett"],
  "publisherId" : 8cfb002
}
```

`Publisher` document

```json
{
  "_id" : 8cfb002,
  "acronym" : "DR",
  "name" : "Del Rey"
}
```

**1**

Set up the link from `Book` (reference) to `Publisher` (owner) by storing the `Publisher.id` within the `Book` document.

**2**

Mark the property holding the references to be readonly.
This prevents storing references to individual `Book`s with the `Publisher` document.

**3**

Use the `#self` variable to access values within the `Publisher` document and in this retrieve `Books` with matching `publisherId`.

With all the above in place it is possible to model all kind of associations between entities.
Have a look at the non-exhaustive list of samples below to get feeling for what is possible.

Example 1. Simple Document Reference using *id* field

```java
class Entity {
  @DocumentReference
  ReferencedObject ref;
}
```

```json
// entity {"_id" : "8cfb002","ref" : "9a48e32" (1)}
// referenced object {"_id" : "9a48e32" (1)}
```

**1**

MongoDB simple type can be directly used without further configuration.

Example 2. Simple Document Reference using *id* field with explicit lookup query

```java
class Entity {
  @DocumentReference(lookup = "{ '_id' : '?#{#target}' }") (1)
  ReferencedObject ref;
}
```

```json
// entity {"_id" : "8cfb002","ref" : "9a48e32"                                        (1)}
// referenced object {"_id" : "9a48e32"}
```

**1**

*target* defines the reference value itself.

Example 3. Document Reference extracting the `refKey` field for the lookup query

```java
class Entity {
  @DocumentReference(lookup = "{ '_id' : '?#{refKey}' }")  (1) (2)
  private ReferencedObject ref;
}
```

```java
@WritingConverter
class ToDocumentPointerConverter implements Converter<ReferencedObject, DocumentPointer<Document>> {
	public DocumentPointer<Document> convert(ReferencedObject source) {
		return () -> new Document("refKey", source.id);    (1)
	}
}
```

```json
// entity {"_id" : "8cfb002","ref" : {"refKey" : "9a48e32"                                   (1)}}
// referenced object {"_id" : "9a48e32"}
```

**1**

The key used for obtaining the reference value must be the one used during write.

**2**

`refKey` is short for `target.refKey`.

Example 4. Document Reference with multiple values forming the lookup query

```java
class Entity {
  @DocumentReference(lookup = "{ 'firstname' : '?#{fn}', 'lastname' : '?#{ln}' }") (1) (2)
  ReferencedObject ref;
}
```

```json
// entity {"_id" : "8cfb002","ref" : {"fn" : "Josh",           (1) "ln" : "Long"            (1)}}
// referenced object {"_id" : "9a48e32","firstname" : "Josh",      (2) "lastname" : "Long",       (2)}
```

**1**

Read/write the keys `fn` & `ln` from/to the linkage document based on the lookup query.

**2**

Use non *id* fields for the lookup of the target documents.

Example 5. Document Reference reading from a target collection

```java
class Entity {
  @DocumentReference(lookup = "{ '_id' : '?#{id}' }", collection = "?#{collection}") (2)
  private ReferencedObject ref;
}
```

```java
@WritingConverter
class ToDocumentPointerConverter implements Converter<ReferencedObject, DocumentPointer<Document>> {
	public DocumentPointer<Document> convert(ReferencedObject source) {
		return () -> new Document("id", source.id)                                   (1)
                           .append("collection", … );                                (2)
	}
}
```

```json
// entity {"_id" : "8cfb002","ref" : {"id" : "9a48e32",                                                                (1) "collection" : "…"                                                               (2)}}
```

**1**

Read/write the keys `_id` from/to the reference document to use them in the lookup query.

**2**

The collection name can be read from the reference document using its key.

> [!WARNING]
> We know it is tempting to use all kinds of MongoDB query operators in the lookup query and this is fine.
> But there a few aspects to consider:
>
> - Make sure to have indexes in place that support your lookup.
> - Make sure to use the same data types: `@DocumentReference(lookup="{'someRef':?#{#self._id} }")` can easily fail when using `@Id String id` and `String someRef` as `String @Id`'s are subject to automatic ObjectId conversion (but not other `String` properties containing `ObjectId.toString()`).
>   Reference lookup uses values from the resulting `Document` and in that case, it would query a String field using an `ObjectId` yielding no results.
> - Mind that resolution requires a server roundtrip inducing latency, consider a lazy strategy.
> - A collection of document references is bulk loaded using the `$or` operator.
>   The original element order is restored in memory on a best-effort basis.
>   Restoring the order is only possible when using equality expressions and cannot be done when using MongoDB query operators.
>   In this case results will be ordered as they are received from the store or via the provided `@DocumentReference(sort)` attribute.
>
> A few more general remarks:
>
> - Do you use cyclic references?
>   Ask your self if you need them.
> - Lazy document references are hard to debug.
>   Make sure tooling does not accidentally trigger proxy resolution by e.g. calling `toString()`.
>   Though technically possible, avoid saving back individual lazily loaded entities obtained via properties of the referencing root.
> - There is no support for reading document references using reactive infrastructure.

---

<a id="mongodb-mapping-mapping-index-management"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mapping/mapping-index-management.html -->

<!-- page_index: 26 -->

# Index Creation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mapping-mapping-index-management--page-title"></a>
<a id="mongodb-mapping-mapping-index-management--index-creation"></a>

# Index Creation

Spring Data MongoDB can automatically create indexes for entity types annotated with `@Document`.
Index creation must be explicitly enabled since version 3.0 to prevent undesired effects with collection lifecycle and performance impact.
Indexes are automatically created for the initial entity set on application startup and when accessing an entity type for the first time while the application runs.

We generally recommend explicit index creation for application-based control of indexes as Spring Data cannot automatically create indexes for collections that were recreated while the application was running.

`IndexResolver` provides an abstraction for programmatic index definition creation if you want to make use of `@Indexed` annotations such as `@GeoSpatialIndexed`, `@TextIndexed`, `@CompoundIndex` and `@WildcardIndexed`.
You can use index definitions with `IndexOperations` to create indexes.
A good point in time for index creation is on application startup, specifically after the application context was refreshed, triggered by observing `ContextRefreshedEvent`.
This event guarantees that the context is fully initialized.
Note that at this time other components, especially bean factories might have access to the MongoDB database.

> [!WARNING]
> `Map`-like properties are skipped by the `IndexResolver` unless annotated with `@WildcardIndexed` because the *map key* must be part of the index definition. Since the purpose of maps is the usage of dynamic keys and values, the keys cannot be resolved from static mapping metadata.

Example 1. Programmatic Index Creation for a single Domain Type

```java
class MyListener {

  @EventListener(ContextRefreshedEvent.class)
  public void initIndicesAfterStartup() {

    MappingContext<? extends MongoPersistentEntity<?>, MongoPersistentProperty> mappingContext = mongoTemplate
      .getConverter().getMappingContext();

    IndexResolver resolver = new MongoPersistentEntityIndexResolver(mappingContext);

    IndexOperations indexOps = mongoTemplate.indexOps(DomainType.class);
    resolver.resolveIndexFor(DomainType.class).forEach(indexOps::ensureIndex);
  }
}
```

Example 2. Programmatic Index Creation for all Initial Entities

```java
class MyListener {

  @EventListener(ContextRefreshedEvent.class)
  public void initIndicesAfterStartup() {

    MappingContext<? extends MongoPersistentEntity<?>, MongoPersistentProperty> mappingContext = mongoTemplate.
      getConverter().getMappingContext();

    IndexResolver resolver = new MongoPersistentEntityIndexResolver(mappingContext);

      // consider only entities that are annotated with @Document
    mappingContext.getPersistentEntities()
      .stream()
      .filter(it -> it.isAnnotationPresent(Document.class))
      .forEach(it -> {

        IndexOperations indexOps = mongoTemplate.indexOps(it.getType());
        resolver.resolveIndexFor(it.getType()).forEach(indexOps::ensureIndex);
      });
  }
}
```

Alternatively, if you want to ensure index and collection presence before any component is able to access your database from your application, declare a `@Bean` method for `MongoTemplate` and include the code from above before returning the `MongoTemplate` object.

> [!NOTE]
> To turn automatic index creation *ON* please override `autoIndexCreation()` in your configuration.
>
> ```java
> @Configuration public class Config extends AbstractMongoClientConfiguration {
> @Override public boolean autoIndexCreation() {return true;}
> // ...}
> ```

> [!IMPORTANT]
> Automatic index creation is turned *OFF* by default as of version 3.0.

<a id="mongodb-mapping-mapping-index-management--mapping-usage-indexes.compound-index"></a>
<a id="mongodb-mapping-mapping-index-management--compound-indexes"></a>

## Compound Indexes

Compound indexes are also supported. They are defined at the class level, rather than on individual properties.

> [!NOTE]
> Compound indexes are very important to improve the performance of queries that involve criteria on multiple fields

Here’s an example that creates a compound index of `lastName` in ascending order and `age` in descending order:

Example 3. Example Compound Index Usage

```java
@Document
@CompoundIndex(name = "age_idx", def = "{'lastName': 1, 'age': -1}")
public class Person {

  @Id
  private ObjectId id;
  private Integer age;
  private String firstName;
  private String lastName;

}
```

> [!TIP]
> `@CompoundIndex` is repeatable using `@CompoundIndexes` as its container.
>
> ```java
> @Document
> @CompoundIndexes({
>     @CompoundIndex(name = "cmp-idx-one", def = "{'firstname': 1, 'lastname': -1}"),
>     @CompoundIndex(name = "cmp-idx-two", def = "{'address.city': -1, 'address.street': 1}")
> })
> public class Person {
>
>   String firstname;
>   String lastname;
>
>   Address address;
>
>   // ...
> }
> ```

<a id="mongodb-mapping-mapping-index-management--mapping-usage-indexes.hashed-index"></a>
<a id="mongodb-mapping-mapping-index-management--hashed-indexes"></a>

## Hashed Indexes

Hashed indexes allow hash based sharding within a sharded cluster.
Using hashed field values to shard collections results in a more random distribution.
For details, refer to the [MongoDB Documentation](https://docs.mongodb.com/manual/core/index-hashed/).

Here’s an example that creates a hashed index for `_id`:

Example 4. Example Hashed Index Usage

```java
@Document
public class DomainType {

  @HashIndexed @Id String id;

  // ...
}
```

Hashed indexes can be created next to other index definitions like shown below, in that case both indices are created:

Example 5. Example Hashed Index Usage together with simple index

```java
@Document
public class DomainType {

  @Indexed
  @HashIndexed
  String value;

  // ...
}
```

In case the example above is too verbose, a compound annotation allows to reduce the number of annotations that need to be declared on a property:

Example 6. Example Composed Hashed Index Usage

```java
@Document
public class DomainType {

  @IndexAndHash(name = "idx...")                            (1)
  String value;

  // ...
}

@Indexed
@HashIndexed
@Retention(RetentionPolicy.RUNTIME)
public @interface IndexAndHash {

  @AliasFor(annotation = Indexed.class, attribute = "name") (1)
  String name() default "";
}
```

**1**

Potentially register an alias for certain attributes of the meta annotation.

> [!NOTE]
> Although index creation via annotations comes in handy for many scenarios cosider taking over more control by setting up indices manually via `IndexOperations`.
>
> ```java
> mongoOperations.indexOpsFor(Jedi.class)
>   .ensureIndex(HashedIndex.hashed("useTheForce"));
> ```

<a id="mongodb-mapping-mapping-index-management--mapping-usage-indexes.wildcard-index"></a>
<a id="mongodb-mapping-mapping-index-management--wildcard-indexes"></a>

## Wildcard Indexes

A `WildcardIndex` is an index that can be used to include all fields or specific ones based a given (wildcard) pattern.
For details, refer to the [MongoDB Documentation](https://docs.mongodb.com/manual/core/index-wildcard/).

The index can be set up programmatically using `WildcardIndex` via `IndexOperations`.

Example 7. Programmatic WildcardIndex setup

```java
mongoOperations
    .indexOps(User.class)
    .ensureIndex(new WildcardIndex("userMetadata"));
```

```javascript
db.user.createIndex({ "userMetadata.$**" : 1 }, {})
```

The `@WildcardIndex` annotation allows a declarative index setup that can used either with a document type or property.

If placed on a type that is a root level domain entity (one annotated with `@Document`) , the index resolver will create a
wildcard index for it.

Example 8. Wildcard index on domain type

```java
@Document
@WildcardIndexed
public class Product {
	// …
}
```

```javascript
db.product.createIndex({ "$**" : 1 },{})
```

The `wildcardProjection` can be used to specify keys to in-/exclude in the index.

Example 9. Wildcard index with `wildcardProjection`

```java
@Document
@WildcardIndexed(wildcardProjection = "{ 'userMetadata.age' : 0 }")
public class User {
    private @Id String id;
    private UserMetadata userMetadata;
}
```

```javascript
db.user.createIndex(
  { "$**" : 1 },
  { "wildcardProjection" :
    { "userMetadata.age" : 0 }
  }
)
```

Wildcard indexes can also be expressed by adding the annotation directly to the field.
Please note that `wildcardProjection` is not allowed on nested paths such as properties.
Projections on types annotated with `@WildcardIndexed` are omitted during index creation.

Example 10. Wildcard index on property

```java
@Document
public class User {
    private @Id String id;

    @WildcardIndexed
    private UserMetadata userMetadata;
}
```

```javascript
db.user.createIndex({ "userMetadata.$**" : 1 }, {})
```

<a id="mongodb-mapping-mapping-index-management--mapping-usage-indexes.text-index"></a>
<a id="mongodb-mapping-mapping-index-management--text-indexes"></a>

## Text Indexes

> [!NOTE]
> The text index feature is disabled by default for MongoDB v.2.4.

Creating a text index allows accumulating several fields into a searchable full-text index.
It is only possible to have one text index per collection, so all fields marked with `@TextIndexed` are combined into this index.
Properties can be weighted to influence the document score for ranking results.
The default language for the text index is English.To change the default language, set the `language` attribute to whichever language you want (for example,`@Document(language="spanish")`).
Using a property called `language` or `@Language` lets you define a language override on a per-document base.
The following example shows how to created a text index and set the language to Spanish:

Example 11. Example Text Index Usage

```java
@Document(language = "spanish")
class SomeEntity {

    @TextIndexed String foo;

    @Language String lang;

    Nested nested;
}

class Nested {

    @TextIndexed(weight=5) String bar;
    String roo;
}
```

---

<a id="mongodb-value-expressions"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/value-expressions.html -->

<!-- page_index: 27 -->

# Value Expressions Fundamentals

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-value-expressions--page-title"></a>
<a id="mongodb-value-expressions--value-expressions-fundamentals"></a>

# Value Expressions Fundamentals

Value Expressions are a combination of [Spring Expression Language (SpEL)](https://docs.spring.io/spring-framework/reference/7.0/core/expressions.html) and [Property Placeholder Resolution](https://docs.spring.io/spring-framework/reference/7.0/core/beans/annotation-config/value-annotations.html).
They combine powerful evaluation of programmatic expressions with the simplicity to resort to property-placeholder resolution to obtain values from the `Environment` such as configuration properties.

Expressions are expected to be defined by a trusted input such as an annotation value and not to be determined from user input.

<a id="mongodb-value-expressions--_scope"></a>
<a id="mongodb-value-expressions--scope"></a>

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

<a id="mongodb-value-expressions--_expression_syntax"></a>
<a id="mongodb-value-expressions--expression-syntax"></a>

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

<a id="mongodb-value-expressions--valueexpressions.api"></a>
<a id="mongodb-value-expressions--parsing-and-evaluation"></a>

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

<a id="mongodb-value-expressions--valueexpressions.spel"></a>
<a id="mongodb-value-expressions--spel-expressions"></a>

## SpEL Expressions

[SpEL Expressions](https://docs.spring.io/spring-framework/reference/7.0/core/expressions.html) follow the Template style where the expression is expected to be enclosed within the `#{…}` format.
Expressions are evaluated using an `EvaluationContext` that is provided by `EvaluationContextProvider`.
The context itself is a powerful `StandardEvaluationContext` allowing a wide range of operations, access to static types and context extensions.

> [!NOTE]
> Make sure to parse and evaluate only expressions from trusted sources such as annotations.
> Accepting user-provided expressions can create an entry path to exploit the application context and your system resulting in a potential security vulnerability.

<a id="mongodb-value-expressions--_extending_the_evaluation_context"></a>
<a id="mongodb-value-expressions--extending-the-evaluation-context"></a>

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

<a id="mongodb-value-expressions--valueexpressions.property-placeholders"></a>
<a id="mongodb-value-expressions--property-placeholders"></a>

## Property Placeholders

Property placeholders following the form `${…}` refer to properties provided typically by a `PropertySource` through `Environment`.
Properties are useful to resolve against system properties, application configuration files, environment configuration or property sources contributed by secret management systems.
You can find more details on the property placeholders in [Spring Framework’s documentation on `@Value` usage](https://docs.spring.io/spring-framework/reference/7.0/core/beans/annotation-config/value-annotations.html#page-title).

---

<a id="mongodb-lifecycle-events"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/lifecycle-events.html -->

<!-- page_index: 28 -->

# Lifecycle Events

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-lifecycle-events--page-title"></a>
<a id="mongodb-lifecycle-events--lifecycle-events"></a>

# Lifecycle Events

The MongoDB mapping framework includes several `org.springframework.context.ApplicationEvent` events that your application can respond to by registering special beans in the `ApplicationContext`.
Being based on Spring’s `ApplicationContext` event infrastructure enables other products, such as Spring Integration, to easily receive these events, as they are a well known eventing mechanism in Spring-based applications.

Entity lifecycle events can be costly and you may notice a change in the performance profile when loading large result sets.
You can disable lifecycle events on the [Template API](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/MongoTemplate.html#setEntityLifecycleEventsEnabled(boolean)).

To intercept an object before it goes through the conversion process (which turns your domain object into a `org.bson.Document`), you can register a subclass of `AbstractMongoEventListener` that overrides the `onBeforeConvert` method.
When the event is dispatched, your listener is called and passed the domain object before it goes into the converter.
The following example shows how to do so:

```java
public class BeforeConvertListener extends AbstractMongoEventListener<Person> {
  @Override
  public void onBeforeConvert(BeforeConvertEvent<Person> event) {
    ... does some auditing manipulation, set timestamps, whatever ...
  }
}
```

To intercept an object before it goes into the database, you can register a subclass of [`AbstractMongoEventListener`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/mapping/event/AbstractMongoEventListener.html) that overrides the `onBeforeSave` method. When the event is dispatched, your listener is called and passed the domain object and the converted `com.mongodb.Document`. The following example shows how to do so:

```java
public class BeforeSaveListener extends AbstractMongoEventListener<Person> {
  @Override
  public void onBeforeSave(BeforeSaveEvent<Person> event) {
    … change values, delete them, whatever …
  }
}
```

Declaring these beans in your Spring ApplicationContext causes them to be invoked whenever the event is dispatched.

<details>
<summary>Callbacks on <code>AbstractMappingEventListener</code>:</summary>
<div>
<div>
<ul>
<li>
<p><code>onBeforeConvert</code>: Called in <code>MongoTemplate</code> <code>insert</code>, <code>insertList</code>, and <code>save</code> operations before the object is converted to a <code>Document</code> by a <code>MongoConverter</code>.</p>
</li>
<li>
<p><code>onBeforeSave</code>: Called in <code>MongoTemplate</code> <code>insert</code>, <code>insertList</code>, and <code>save</code> operations <strong>before</strong> inserting or saving the <code>Document</code> in the database.</p>
</li>
<li>
<p><code>onAfterSave</code>: Called in <code>MongoTemplate</code> <code>insert</code>, <code>insertList</code>, and <code>save</code> operations <strong>after</strong> inserting or saving the <code>Document</code> in the database.</p>
</li>
<li>
<p><code>onAfterLoad</code>: Called in <code>MongoTemplate</code> <code>find</code>, <code>findAndRemove</code>, <code>findOne</code>, and <code>getCollection</code> methods after the <code>Document</code> has been retrieved from the database.</p>
</li>
<li>
<p><code>onAfterConvert</code>: Called in <code>MongoTemplate</code> <code>find</code>, <code>findAndRemove</code>, <code>findOne</code>, and <code>getCollection</code> methods after the <code>Document</code> has been retrieved from the database was converted to a POJO.</p>
</li>
</ul>
</div>
</div>
</details>

> [!NOTE]
> Lifecycle events are only emitted for root level types.
> Complex types used as properties within a document root are not subject to event publication unless they are document references annotated with `@DBRef`.

> [!WARNING]
> Lifecycle events depend on an `ApplicationEventMulticaster`, which in case of the `SimpleApplicationEventMulticaster` can be configured with a `TaskExecutor`, and therefore gives no guarantees when an Event is processed.

<a id="mongodb-lifecycle-events--entity-callbacks"></a>

## Entity Callbacks

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

<a id="mongodb-lifecycle-events--entity-callbacks.implement"></a>
<a id="mongodb-lifecycle-events--implementing-entity-callbacks"></a>

### Implementing Entity Callbacks

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

<a id="mongodb-lifecycle-events--entity-callbacks.register"></a>
<a id="mongodb-lifecycle-events--registering-entity-callbacks"></a>

### Registering Entity Callbacks

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

<a id="mongodb-lifecycle-events--mongo.entity-callbacks"></a>
<a id="mongodb-lifecycle-events--store-specific-entitycallbacks"></a>

## Store specific EntityCallbacks

Spring Data MongoDB uses the `EntityCallback` API for its auditing support and reacts on the following callbacks.

| Callback | Method | Description | Order |
| --- | --- | --- | --- |
| `ReactiveBeforeConvertCallback` `BeforeConvertCallback` | `onBeforeConvert(T entity, String collection)` | Invoked before a domain object is converted to `org.bson.Document`. | `Ordered.LOWEST_PRECEDENCE` |
| `ReactiveAfterConvertCallback` `AfterConvertCallback` | `onAfterConvert(T entity, org.bson.Document target, String collection)` | Invoked after a domain object is loaded. Can modify the domain object after reading it from a `org.bson.Document`. | `Ordered.LOWEST_PRECEDENCE` |
| `ReactiveAuditingEntityCallback` `AuditingEntityCallback` | `onBeforeConvert(Object entity, String collection)` | Marks an auditable entity *created* or *modified* | 100 |
| `ReactiveBeforeSaveCallback` `BeforeSaveCallback` | `onBeforeSave(T entity, org.bson.Document target, String collection)` | Invoked before a domain object is saved. Can modify the target, to be persisted, `Document` containing all mapped entity information. | `Ordered.LOWEST_PRECEDENCE` |
| `ReactiveAfterSaveCallback` `AfterSaveCallback` | `onAfterSave(T entity, org.bson.Document target, String collection)` | Invoked before a domain object is saved. Can modify the domain object, to be returned after save, `Document` containing all mapped entity information. | `Ordered.LOWEST_PRECEDENCE` |

<a id="mongodb-lifecycle-events--_bean_validation"></a>
<a id="mongodb-lifecycle-events--bean-validation"></a>

### Bean Validation

Spring Data MongoDB supports Bean Validation for MongoDB entities annotated with [https://xxx](https://beanvalidation.org/)
[Jakarta Validation annotations].

You can enable Bean Validation by registering `ValidatingEntityCallback` respectively `ReactiveValidatingEntityCallback` for reactive driver usage in your Spring `ApplicationContext` as shown in the following example:

- Imperative
- Reactive

```java
@Configuration class Config {
@Bean public ValidatingEntityCallback validatingEntityCallback(Validator validator) {return new ValidatingEntityCallback(validator);}}
```

```java
@Configuration class Config {
@Bean public ReactiveValidatingEntityCallback validatingEntityCallback(Validator validator) {return new ReactiveValidatingEntityCallback(validator);}}
```

If you’re using both, imperative and reactive, then you can enable also both callbacks.

> [!NOTE]
> When using XML-based configuration, historically, `ValidatingMongoEventListener` is registered through our namespace handlers when configuring `<mongo:mapping-converter>`.
> If you want to use the newer Entity Callback variant, make sure to not use `<mongo:mapping-converter>`, otherwise you’ll end up with both, the `ValidatingMongoEventListener` and the `ValidatingEntityCallback` being registered.

---

<a id="mongodb-auditing"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/auditing.html -->

<!-- page_index: 29 -->

# Auditing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-auditing--page-title"></a>
<a id="mongodb-auditing--auditing"></a>

# Auditing

Since Spring Data MongoDB 1.4, auditing can be enabled by annotating a configuration class with the `@EnableMongoAuditing` annotation, as the following example shows:

- Imperative
- Reactive
- XML

```java
@Configuration @EnableMongoAuditing class Config {
@Bean public AuditorAware<AuditableUser> myAuditorProvider() {return new AuditorAwareImpl();}}
```

```java
@Configuration @EnableReactiveMongoAuditing class Config {
@Bean public ReactiveAuditorAware<AuditableUser> myAuditorProvider() {return new ReactiveAuditorAwareImpl();}}
```

```xml
<mongo:auditing mapping-context-ref="customMappingContext" auditor-aware-ref="yourAuditorAwareImpl"/>
```

If you expose a bean of type `AuditorAware` / `ReactiveAuditorAware` to the `ApplicationContext`, the auditing infrastructure picks it up automatically and uses it to determine the current user to be set on domain types.
If you have multiple implementations registered in the `ApplicationContext`, you can select the one to be used by explicitly setting the `auditorAwareRef` attribute of `@EnableMongoAuditing`.

---

<a id="mongodb-client-session-transactions"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/client-session-transactions.html -->

<!-- page_index: 30 -->

# Sessions & Transactions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-client-session-transactions--page-title"></a>
<a id="mongodb-client-session-transactions--sessions-transactions"></a>

# Sessions & Transactions

As of version 3.6, MongoDB supports the concept of sessions.
The use of sessions enables MongoDB’s [Causal Consistency](https://docs.mongodb.com/manual/core/read-isolation-consistency-recency/#causal-consistency) model, which guarantees running operations in an order that respects their causal relationships.
Those are split into `ServerSession` instances and `ClientSession` instances.
In this section, when we speak of a session, we refer to `ClientSession`.

> [!WARNING]
> Operations within a client session are not isolated from operations outside the session.

Both `MongoOperations` and `ReactiveMongoOperations` provide gateway methods for tying a `ClientSession` to the operations.
`MongoCollection` and `MongoDatabase` use session proxy objects that implement MongoDB’s collection and database interfaces, so you need not add a session on each call.
This means that a potential call to `MongoCollection#find()` is delegated to `MongoCollection#find(ClientSession)`.

> [!NOTE]
> Methods such as `(Reactive)MongoOperations#getCollection` return native MongoDB Java Driver gateway objects (such as `MongoCollection`) that themselves offer dedicated methods for `ClientSession`.
> These methods are **NOT** session-proxied.
> You should provide the `ClientSession` where needed when interacting directly with a `MongoCollection` or `MongoDatabase` and not through one of the `#execute` callbacks on `MongoOperations`.

<a id="mongodb-client-session-transactions--mongo.sessions.reactive"></a>
<a id="mongodb-client-session-transactions--clientsession-support"></a>

## ClientSession support

The following example shows the usage of a session:

- Imperative
- Reactive

```java
ClientSessionOptions sessionOptions = ClientSessionOptions.builder()
    .causallyConsistent(true)
    .build();

ClientSession session = client.startSession(sessionOptions); (1)

template.withSession(() -> session)
    .execute(action -> {

        Query query = query(where("name").is("Durzo Blint"));
        Person durzo = action.findOne(query, Person.class);  (2)

        Person azoth = new Person("Kylar Stern");
        azoth.setMaster(durzo);

        action.insert(azoth);                                (3)

        return azoth;
    });

session.close()                                              (4)
```

| **1** | Obtain a new session from the server. |
| --- | --- |
| **2** | Use `MongoOperation` methods as before. The `ClientSession` gets applied automatically. |
| **3** | Make sure to close the `ClientSession`. |
| **4** | Close the session. |

> [!WARNING]
> When dealing with `DBRef` instances, especially lazily loaded ones, it is essential to **not** close the `ClientSession` before all data is loaded.
> Otherwise, lazy fetch fails.

```java
ClientSessionOptions sessionOptions = ClientSessionOptions.builder()
.causallyConsistent(true)
.build();

Publisher<ClientSession> session = client.startSession(sessionOptions); (1)

template.withSession(session)
.execute(action -> {

        Query query = query(where("name").is("Durzo Blint"));
        return action.findOne(query, Person.class)
            .flatMap(durzo -> {

                Person azoth = new Person("Kylar Stern");
                azoth.setMaster(durzo);

                return action.insert(azoth);                            (2)
            });
    }, ClientSession::close)                                            (3)
    .subscribe();                                                       (4)
```

| **1** | Obtain a `Publisher` for new session retrieval. |
| --- | --- |
| **2** | Use `ReactiveMongoOperation` methods as before. The `ClientSession` is obtained and applied automatically. |
| **3** | Make sure to close the `ClientSession`. |
| **4** | Nothing happens until you subscribe. See [the Project Reactor Reference Guide](https://projectreactor.io/docs/core/release/reference/#reactive.subscribe) for details. |

By using a `Publisher` that provides the actual session, you can defer session acquisition to the point of actual subscription.
Still, you need to close the session when done, so as to not pollute the server with stale sessions.
Use the `doFinally` hook on `execute` to call `ClientSession#close()` when you no longer need the session.
If you prefer having more control over the session itself, you can obtain the `ClientSession` through the driver and provide it through a `Supplier`.

> [!NOTE]
> Reactive use of `ClientSession` is limited to Template API usage.
> There’s currently no session integration with reactive repositories.

<a id="mongodb-client-session-transactions--mongo.transactions"></a>
<a id="mongodb-client-session-transactions--mongodb-transactions"></a>

## MongoDB Transactions

As of version 4, MongoDB supports [Transactions](https://www.mongodb.com/transactions).
Transactions are built on top of [Sessions](#mongodb-client-session-transactions) and, consequently, require an active `ClientSession`.

> [!NOTE]
> Unless you specify a `MongoTransactionManager` within your application context, transaction support is **DISABLED**.
> You can use `setSessionSynchronization(ALWAYS)` to participate in ongoing non-native MongoDB transactions.

To get full programmatic control over transactions, you may want to use the session callback on `MongoOperations`.

The following example shows programmatic transaction control:

Programmatic transactions

- Imperative
- Reactive

```java
ClientSession session = client.startSession(options);                   (1)

template.withSession(session)
    .execute(action -> {

        session.startTransaction();                                     (2)

        try {

            Step step = // ...;
            action.insert(step);

            process(step);

            action.update(Step.class).apply(Update.set("state", // ...

            session.commitTransaction();                                (3)

        } catch (RuntimeException e) {
            session.abortTransaction();                                 (4)
        }
    }, ClientSession::close)                                            (5)
```

| **1** | Obtain a new `ClientSession`. |
| --- | --- |
| **2** | Start the transaction. |
| **3** | If everything works out as expected, commit the changes. |
| **4** | Something broke, so roll back everything. |
| **5** | Do not forget to close the session when done. |

The preceding example lets you have full control over transactional behavior while using the session scoped `MongoOperations` instance within the callback to ensure the session is passed on to every server call.
To avoid some of the overhead that comes with this approach, you can use a `TransactionTemplate` to take away some of the noise of manual transaction flow.

```java
Mono<DeleteResult> result = Mono
    .from(client.startSession())                                                             (1)

    .flatMap(session -> {
        session.startTransaction();                                                          (2)

        return Mono.from(collection.deleteMany(session, ...))                                (3)

            .onErrorResume(e -> Mono.from(session.abortTransaction()).then(Mono.error(e)))   (4)

            .flatMap(val -> Mono.from(session.commitTransaction()).then(Mono.just(val)))     (5)

            .doFinally(signal -> session.close());                                           (6)
      });
```

| **1** | First we obviously need to initiate the session. |
| --- | --- |
| **2** | Once we have the `ClientSession` at hand, start the transaction. |
| **3** | Operate within the transaction by passing on the `ClientSession` to the operation. |
| **4** | If the operations completes exceptionally, we need to stop the transaction and preserve the error. |
| **5** | Or of course, commit the changes in case of success. Still preserving the operations result. |
| **6** | Lastly, we need to make sure to close the session. |

The culprit of the above operation is in keeping the main flows `DeleteResult` instead of the transaction outcome published via either `commitTransaction()` or `abortTransaction()`, which leads to a rather complicated setup.

> [!NOTE]
> Unless you specify a `ReactiveMongoTransactionManager` within your application context, transaction support is **DISABLED**.
> You can use `setSessionSynchronization(ALWAYS)` to participate in ongoing non-native MongoDB transactions.

<a id="mongodb-client-session-transactions--mongo.transactions.reactive-operator"></a>
<a id="mongodb-client-session-transactions--transactions-with-transactiontemplate-transactionaloperator"></a>

## Transactions with TransactionTemplate / TransactionalOperator

Spring Data MongoDB transactions support both `TransactionTemplate` and `TransactionalOperator`.

Transactions with `TransactionTemplate` / `TransactionalOperator`

- Imperative
- Reactive

```java
template.setSessionSynchronization(ALWAYS);                                     (1)

// ...

TransactionTemplate txTemplate = new TransactionTemplate(anyTxManager);         (2)

txTemplate.execute(new TransactionCallbackWithoutResult() {

    @Override
    protected void doInTransactionWithoutResult(TransactionStatus status) {     (3)

        Step step = // ...;
        template.insert(step);

        process(step);

        template.update(Step.class).apply(Update.set("state", // ...
    }
});
```

| **1** | Enable transaction synchronization during Template API configuration. |
| --- | --- |
| **2** | Create the `TransactionTemplate` using the provided `PlatformTransactionManager`. |
| **3** | Within the callback the `ClientSession` and transaction are already registered. |

> [!WARNING]
> Changing state of `MongoTemplate` during runtime (as you might think would be possible in item 1 of the preceding listing) can cause threading and visibility issues.

```java
template.setSessionSynchronization(ALWAYS);                                          (1)

// ...

TransactionalOperator rxtx = TransactionalOperator.create(anyTxManager,
                                   new DefaultTransactionDefinition());              (2)


Step step = // ...;
template.insert(step);

Mono<Void> process(step)
    .then(template.update(Step.class).apply(Update.set("state", …))
    .as(rxtx::transactional)                                                         (3)
    .then();
```

| **1** | Enable transaction synchronization for Transactional participation. |
| --- | --- |
| **2** | Create the `TransactionalOperator` using the provided `ReactiveTransactionManager`. |
| **3** | `TransactionalOperator.transactional(…)` provides transaction management for all upstream operations. |

<a id="mongodb-client-session-transactions--mongo.transactions.reactive-tx-manager"></a>
<a id="mongodb-client-session-transactions--transactions-with-mongotransactionmanager-reactivemongotransactionmanager"></a>

## Transactions with MongoTransactionManager & ReactiveMongoTransactionManager

`MongoTransactionManager` / `ReactiveMongoTransactionManager` is the gateway to the well known Spring transaction support.
It lets applications use [the managed transaction features of Spring](https://docs.spring.io/spring-framework/reference/7.0/data-access.html#transaction).
The `MongoTransactionManager` binds a `ClientSession` to the thread whereas the `ReactiveMongoTransactionManager` is using the `ReactorContext` for this.
`MongoTemplate` detects the session and operates on these resources which are associated with the transaction accordingly.
`MongoTemplate` can also participate in other, ongoing transactions.
The following example shows how to create and use transactions with a `MongoTransactionManager`:

Transactions with `MongoTransactionManager` / `ReactiveMongoTransactionManager`

- Imperative
- Reactive

```java
@Configuration static class Config extends AbstractMongoClientConfiguration {
@Bean MongoTransactionManager transactionManager(MongoDatabaseFactory dbFactory) {  (1) return new MongoTransactionManager(dbFactory);}
@Bean MongoTemplate mongoTemplate(MongoDatabaseFactory dbFactory) {                 (1) return new MongoTemplate(dbFactory);}
// ...}
@Component public class StateService {
@Transactional void someBusinessFunction(Step step) {                                        (2)
template.insert(step);
process(step);
template.update(Step.class).apply(Update.set("state", // ...}; });
```

**1**

Register `MongoTransactionManager` in the application context.
Also, make sure to use the same `MongoDatabaseFactory` when creating `MongoTemplate` to participate in transactions in the scope of the same `MongoDatabaseFactory`.

**2**

Mark methods as transactional.

> [!NOTE]
> `@Transactional(readOnly = true)` advises `MongoTransactionManager` to also start a transaction that adds the
> `ClientSession` to outgoing requests.

```java
@Configuration public class Config extends AbstractReactiveMongoConfiguration {
@Bean ReactiveMongoTransactionManager transactionManager(ReactiveMongoDatabaseFactory factory) {  (1) return new ReactiveMongoTransactionManager(factory);}
@Bean ReactiveMongoTemplate reactiveMongoTemplate(ReactiveMongoDatabaseFactory dbFactory) {       (1) return new ReactiveMongoTemplate(dbFactory);}
// ...}
@Service public class StateService {
@Transactional Mono<UpdateResult> someBusinessFunction(Step step) {                                  (2)
return template.insert(step) .then(process(step)) .then(template.update(Step.class).apply(Update.set("state", …)); }; });
```

**1**

Register `ReactiveMongoTransactionManager` in the application context.
Also, make sure to use the same `ReactiveMongoDatabaseFactory` when creating `ReactiveMongoTemplate` to participate in transactions in the scope of the same `ReactiveMongoDatabaseFactory`.

**2**

Mark methods as transactional.

> [!NOTE]
> `@Transactional(readOnly = true)` advises `ReactiveMongoTransactionManager` to also start a transaction that adds the `ClientSession` to outgoing requests.

<a id="mongodb-client-session-transactions--mongo.transaction.options"></a>
<a id="mongodb-client-session-transactions--controlling-mongodb-specific-transaction-options"></a>

### Controlling MongoDB-specific Transaction Options

Transactional service methods can require specific transaction options to run a transaction.
Spring Data MongoDB’s transaction managers support evaluation of transaction labels such as `@Transactional(label = { "mongo:readConcern=available" })`.

By default, the label namespace using the `mongo:` prefix is evaluated by `MongoTransactionOptionsResolver` that is configured by default.
Transaction labels are provided by `TransactionAttribute` and available to programmatic transaction control through `TransactionTemplate` and `TransactionalOperator`.
Due to their declarative nature, `@Transactional(label = …)` provides a good starting point that also can serve as documentation.

Currently, the following options are supported:

Max Commit Time
:   Controls the maximum execution time on the server for the commitTransaction operation.
    The format of the value corresponds with ISO-8601 duration format as used with `Duration.parse(…)`.

    Usage:
    `mongo:maxCommitTime=PT1S`

Read Concern
:   Sets the read concern for the transaction.

    Usage:
    `mongo:readConcern=LOCAL|MAJORITY|LINEARIZABLE|SNAPSHOT|AVAILABLE`

Read Preference
:   Sets the read preference for the transaction.

    Usage:
    `mongo:readPreference=PRIMARY|SECONDARY|SECONDARY_PREFERRED|PRIMARY_PREFERRED|NEAREST`

Write Concern
:   Sets the write concern for the transaction.

    Usage:
    `mongo:writeConcern=ACKNOWLEDGED|W1|W2|W3|UNACKNOWLEDGED|JOURNALED|MAJORITY`

> [!NOTE]
> Nested transactions that join the outer transaction do not affect the initial transaction options as the transaction is already started.
> Transaction options are only applied when a new transaction is started.

<a id="mongodb-client-session-transactions--mongo.transactions.behavior"></a>
<a id="mongodb-client-session-transactions--special-behavior-inside-transactions"></a>

## Special behavior inside transactions

Inside transactions, MongoDB server has a slightly different behavior.

**Connection Settings**

The MongoDB drivers offer a dedicated replica set name configuration option turing the driver into auto-detection mode.
This option helps identify the primary replica set nodes and command routing during a transaction.

> [!NOTE]
> Make sure to add `replicaSet` to the MongoDB URI.
> Please refer to [connection string options](https://docs.mongodb.com/manual/reference/connection-string/#connections-connection-options) for further details.

**Collection Operations**

MongoDB does **not** support collection operations, such as collection creation, within a transaction.
This also affects the on the fly collection creation that happens on first usage.
Therefore, make sure to have all required structures in place.

**Transient Errors**

MongoDB can add special labels to errors raised during transactional operations.
Those may indicate transient failures that might vanish by merely retrying the operation.
We highly recommend [Spring Retry](https://github.com/spring-projects/spring-retry) for those purposes.
Nevertheless, one may override `MongoTransactionManager#doCommit(MongoTransactionObject)` to implement a [Retry Commit Operation](https://docs.mongodb.com/manual/core/transactions/#retry-commit-operation)
behavior as outlined in the MongoDB reference manual.

**Count**

MongoDB `count` operates upon collection statistics which may not reflect the actual situation within a transaction.
The server responds with *error 50851* when issuing a `count` command inside a multi-document transaction.
Once `MongoTemplate` detects an active transaction, all exposed `count()` methods are converted and delegated to the aggregation framework using `$match` and `$count` operators, preserving `Query` settings, such as `collation`.

Restrictions apply when using geo commands inside of the aggregation count helper.
The following operators cannot be used and must be replaced with a different operator:

- `$where` → `$expr`
- `$near` → `$geoWithin` with `$center`
- `$nearSphere` → `$geoWithin` with `$centerSphere`

Queries using `Criteria.near(…)` and `Criteria.nearSphere(…)` must be rewritten to `Criteria.within(…)` respective `Criteria.withinSphere(…)`.
Same applies for the `near` query keyword in repository query methods that must be changed to `within`.
See also MongoDB JIRA ticket [DRIVERS-518](https://jira.mongodb.org/browse/DRIVERS-518) for further reference.

The following snippet shows `count` usage inside the session-bound closure:

```javascript
session.startTransaction();

template.withSession(session)
    .execute(ops -> {
        return ops.count(query(where("state").is("active")), Step.class)
        });
```

The snippet above materializes in the following command:

```javascript
db.collection.aggregate(
   [
      { $match: { state: "active" } },
      { $count: "totalEntityCount" }
   ]
)
```

instead of:

```javascript
db.collection.find( { state: "active" } ).count()
```

---

<a id="mongodb-change-streams"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/change-streams.html -->

<!-- page_index: 31 -->

# Change Streams

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-change-streams--page-title"></a>
<a id="mongodb-change-streams--change-streams"></a>

# Change Streams

As of MongoDB 3.6, [Change Streams](https://docs.mongodb.com/manual/changeStreams/) let applications get notified about changes without having to tail the oplog.

> [!NOTE]
> Change Stream support is only possible for replica sets or for a sharded cluster.

Change Streams can be consumed with both, the imperative and the reactive MongoDB Java driver. It is highly recommended to use the reactive variant, as it is less resource-intensive. However, if you cannot use the reactive API, you can still obtain change events by using the messaging concept that is already prevalent in the Spring ecosystem.

It is possible to watch both on a collection as well as database level, whereas the database level variant publishes
changes from all collections within the database. When subscribing to a database change stream, make sure to use a
suitable type for the event type as conversion might not apply correctly across different entity types.
In doubt, use `Document`.

<a id="mongodb-change-streams--change-streams-with-messagelistener"></a>

## Change Streams with `MessageListener`

Listening to a [Change Stream by using a Sync Driver](https://docs.mongodb.com/manual/tutorial/change-streams-example/) creates a long running, blocking task that needs to be delegated to a separate component.
In this case, we need to first create a [`MessageListenerContainer`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/messaging/MessageListenerContainer.html) which will be the main entry point for running the specific `SubscriptionRequest` tasks.
Spring Data MongoDB already ships with a default implementation that operates on `MongoTemplate` and is capable of creating and running `Task` instances for a [`ChangeStreamRequest`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/messaging/ChangeStreamRequest.html).

The following example shows how to use Change Streams with `MessageListener` instances:

Example 1. Change Streams with `MessageListener` instances

```java
MessageListenerContainer container = new DefaultMessageListenerContainer(template);
container.start();                                                                                              (1)

MessageListener<ChangeStreamDocument<Document>, User> listener = System.out::println;                           (2)
ChangeStreamRequestOptions options = new ChangeStreamRequestOptions("db", "user", ChangeStreamOptions.empty()); (3)

Subscription subscription = container.register(new ChangeStreamRequest<>(listener, options), User.class);       (4)

// ...

container.stop();                                                                                               (5)
```

**1**

Starting the container initializes the resources and starts `Task` instances for already registered `SubscriptionRequest` instances. Requests added after startup are ran immediately.

**2**

Define the listener called when a `Message` is received. The `Message#getBody()` is converted to the requested domain type. Use `Document` to receive raw results without conversion.

**3**

Set the collection to listen to and provide additional options through `ChangeStreamOptions`.

**4**

Register the request. The returned `Subscription` can be used to check the current `Task` state and cancel it to free resources.

**5**

Do not forget to stop the container once you are sure you no longer need it. Doing so stops all running `Task` instances within the container.

`DefaultMessageListenerContainer` implements `SmartLifecycle` and will by default be automatically started when registered as a bean in the Application Context.

> [!NOTE]
> Errors while processing are passed on to an `org.springframework.util.ErrorHandler`. If not stated otherwise a log appending `ErrorHandler` gets applied by default.
> Please use `register(request, body, errorHandler)` to provide additional functionality.

<a id="mongodb-change-streams--reactive-change-streams"></a>

## Reactive Change Streams

Subscribing to Change Streams with the reactive API is a more natural approach to work with streams. Still, the essential building blocks, such as `ChangeStreamOptions`, remain the same. The following example shows how to use Change Streams emitting `ChangeStreamEvent`s:

Example 2. Change Streams emitting `ChangeStreamEvent`

```java
Flux<ChangeStreamEvent<User>> flux = reactiveTemplate.changeStream(User.class) (1)
    .watchCollection("people")
    .filter(where("age").gte(38))                                              (2)
    .listen();                                                                 (3)
```

**1**

The event target type the underlying document should be converted to. Leave this out to receive raw results without conversion.

**2**

Use an aggregation pipeline or just a query `Criteria` to filter events.

**3**

Obtain a `Flux` of change stream events. The `ChangeStreamEvent#getBody()` is converted to the requested domain type from (2).

<a id="mongodb-change-streams--resuming-change-streams"></a>

## Resuming Change Streams

Change Streams can be resumed and resume emitting events where you left. To resume the stream, you need to supply either a resume
token or the last known server time (in UTC). Use [`ChangeStreamOptions`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/core/ChangeStreamOptions.html) to set the value accordingly.

The following example shows how to set the resume offset using server time:

Example 3. Resume a Change Stream

```java
Flux<ChangeStreamEvent<User>> resumed = template.changeStream(User.class)
    .watchCollection("people")
    .resumeAt(Instant.now().minusSeconds(1)) (1)
    .listen();
```

**1**

You may obtain the server time of an `ChangeStreamEvent` through the `getTimestamp` method or use the `resumeToken`
exposed through `getResumeToken`.

> [!TIP]
> In some cases an `Instant` might not be a precise enough measure when resuming a Change Stream. Use a MongoDB native
> [BsonTimestamp](https://docs.mongodb.com/manual/reference/bson-types/#timestamps) for that purpose.

---

<a id="mongodb-tailable-cursors"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/tailable-cursors.html -->

<!-- page_index: 32 -->

# Tailable Cursors

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-tailable-cursors--page-title"></a>
<a id="mongodb-tailable-cursors--tailable-cursors"></a>

# Tailable Cursors

By default, MongoDB automatically closes a cursor when the client exhausts all results supplied by the cursor.
Closing a cursor on exhaustion turns a stream into a finite stream. For [capped collections](https://docs.mongodb.com/manual/core/capped-collections/), you can use a [Tailable Cursor](https://docs.mongodb.com/manual/core/tailable-cursors/) that remains open after the client
consumed all initially returned data.

> [!TIP]
> Capped collections can be created with `MongoOperations.createCollection`. To do so, provide the required `CollectionOptions.empty().capped()…`.

Tailable cursors can be consumed with both, the imperative and the reactive MongoDB API. It is highly recommended to use the
reactive variant, as it is less resource-intensive. However, if you cannot use the reactive API, you can still use a messaging
concept that is already prevalent in the Spring ecosystem.

<a id="mongodb-tailable-cursors--tailable-cursors.sync"></a>
<a id="mongodb-tailable-cursors--tailable-cursors-with-messagelistener"></a>

## Tailable Cursors with `MessageListener`

Listening to a capped collection using a Sync Driver creates a long running, blocking task that needs to be delegated to
a separate component. In this case, we need to first create a `MessageListenerContainer`, which will be the main entry point
for running the specific `SubscriptionRequest`. Spring Data MongoDB already ships with a default implementation that
operates on `MongoTemplate` and is capable of creating and running `Task` instances for a `TailableCursorRequest`.

The following example shows how to use tailable cursors with `MessageListener` instances:

Example 1. Tailable Cursors with `MessageListener` instances

```java
MessageListenerContainer container = new DefaultMessageListenerContainer(template);
container.start();                                                                  (1)

MessageListener<Document, User> listener = System.out::println;                     (2)

TailableCursorRequest request = TailableCursorRequest.builder()
  .collection("orders")                                                             (3)
  .filter(query(where("value").lt(100)))                                            (4)
  .publishTo(listener)                                                              (5)
  .build();

container.register(request, User.class);                                            (6)

// ...

container.stop();                                                                   (7)
```

**1**

Starting the container initializes the resources and starts `Task` instances for already registered `SubscriptionRequest` instances. Requests added after startup are ran immediately.

**2**

Define the listener called when a `Message` is received. The `Message#getBody()` is converted to the requested domain type. Use `Document` to receive raw results without conversion.

**3**

Set the collection to listen to.

**4**

Provide an optional filter for documents to receive.

**5**

Set the message listener to publish incoming `Message`s to.

**6**

Register the request. The returned `Subscription` can be used to check the current `Task` state and cancel it to free resources.

**7**

Do not forget to stop the container once you are sure you no longer need it. Doing so stops all running `Task` instances within the container.

<a id="mongodb-tailable-cursors--tailable-cursors.reactive"></a>
<a id="mongodb-tailable-cursors--reactive-tailable-cursors"></a>

## Reactive Tailable Cursors

Using tailable cursors with a reactive data types allows construction of infinite streams. A tailable cursor remains open until it is closed externally. It emits data as new documents arrive in a capped collection.

Tailable cursors may become dead, or invalid, if either the query returns no match or the cursor returns the document at the “end” of the collection and the application then deletes that document. The following example shows how to create and use an infinite stream query:

Example 2. Infinite Stream queries with ReactiveMongoOperations

```java
Flux<Person> stream = template.tail(query(where("name").is("Joe")), Person.class);

Disposable subscription = stream.doOnNext(person -> System.out.println(person)).subscribe();

// …

// Later: Dispose the subscription to close the stream
subscription.dispose();
```

Spring Data MongoDB Reactive repositories support infinite streams by annotating a query method with `@Tailable`. This works for methods that return `Flux` and other reactive types capable of emitting multiple elements, as the following example shows:

Example 3. Infinite Stream queries with ReactiveMongoRepository

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

  @Tailable
  Flux<Person> findByFirstname(String firstname);

}

Flux<Person> stream = repository.findByFirstname("Joe");

Disposable subscription = stream.doOnNext(System.out::println).subscribe();

// …

// Later: Dispose the subscription to close the stream
subscription.dispose();
```

---

<a id="mongodb-sharding"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/sharding.html -->

<!-- page_index: 33 -->

# Sharding

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-sharding--page-title"></a>
<a id="mongodb-sharding--sharding"></a>

# Sharding

MongoDB supports large data sets via sharding, a method for distributing data across multiple database servers.
Please refer to the [MongoDB Documentation](https://docs.mongodb.com/manual/sharding/) to learn how to set up a sharded cluster, its requirements and limitations.

Spring Data MongoDB uses the `@Sharded` annotation to identify entities stored in sharded collections as shown below.

```java
@Document("users")
@Sharded(shardKey = { "country", "userId" }) (1)
public class User {

	@Id
	Long id;

	@Field("userid")
	String userId;

	String country;
}
```

**1**

The properties of the shard key get mapped to the actual field names.

<a id="mongodb-sharding--sharding.sharded-collections"></a>
<a id="mongodb-sharding--sharded-collections"></a>

## Sharded Collections

Spring Data MongoDB does not auto set up sharding for collections nor indexes required for it.
The snippet below shows how to do so using the MongoDB client API.

```java
MongoDatabase adminDB = template.getMongoDbFactory()
    .getMongoDatabase("admin");                                     (1)

adminDB.runCommand(new Document("enableSharding", "db"));           (2)

Document shardCmd = new Document("shardCollection", "db.users")     (3)
	.append("key", new Document("country", 1).append("userid", 1)); (4)

adminDB.runCommand(shardCmd);
```

| **1** | Sharding commands need to be run against the *admin* database. |
| --- | --- |
| **2** | Enable sharding for a specific database if necessary. |
| **3** | Shard a collection within the database having sharding enabled. |
| **4** | Specify the shard key. This example uses range based sharding. |

<a id="mongodb-sharding--sharding.shard-key"></a>
<a id="mongodb-sharding--shard-key-handling"></a>

## Shard Key Handling

The shard key consists of a single or multiple properties that must exist in every document in the target collection.
It is used to distribute documents across shards.

Adding the `@Sharded` annotation to an entity enables Spring Data MongoDB to apply best effort optimisations required for sharded scenarios.
This means essentially adding required shard key information, if not already present, to `replaceOne` filter queries when upserting entities.
This may require an additional server round trip to determine the actual value of the current shard key.

> [!TIP]
> By setting `@Sharded(immutableKey = true)` Spring Data does not attempt to check if an entity shard key was changed.

Please see the [MongoDB Documentation](https://docs.mongodb.com/manual/reference/method/db.collection.replaceOne/#upsert) for further details.
The following list contains which operations are eligible for shard key auto-inclusion:

- `(Reactive)CrudRepository.save(…)`
- `(Reactive)CrudRepository.saveAll(…)`
- `(Reactive)MongoTemplate.save(…)`

---

<a id="mongodb-mongo-search-indexes"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mongo-search-indexes.html -->

<!-- page_index: 34 -->

# MongoDB Search

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mongo-search-indexes--page-title"></a>
<a id="mongodb-mongo-search-indexes--mongodb-search"></a>

# MongoDB Search

MongoDB enables users to do keyword or lexical search as well as vector search data using dedicated search indexes.

<a id="mongodb-mongo-search-indexes--mongo.search.vector"></a>
<a id="mongodb-mongo-search-indexes--vector-search"></a>

## Vector Search

MongoDB Vector Search uses the `$vectorSearch` aggregation stage to run queries against specialized indexes.
Please refer to the MongoDB documentation to learn more about requirements and restrictions of `vectorSearch` indexes.

<a id="mongodb-mongo-search-indexes--mongo.search.vector.index"></a>
<a id="mongodb-mongo-search-indexes--managing-vector-indexes"></a>

### Managing Vector Indexes

`SearchIndexOperationsProvider` implemented by `MongoTemplate` are the entrypoint to `SearchIndexOperations` offering various methods for managing vector indexes.

The following snippet shows how to create a vector index for a collection

Create a Vector Index

- Java
- Mongo Shell

```java
VectorIndex index = new VectorIndex("vector_index")
  .addVector("plotEmbedding", vector -> vector.dimensions(1536).similarity(COSINE)) (1)
  .addFilter("year"); (2)

mongoTemplate.searchIndexOps(Movie.class) (3)
  .createIndex(index);
```

**1**

A vector index may cover multiple vector embeddings that can be added via the `addVector` method.

**2**

Vector indexes can contain additional fields to narrow down search results when running queries.

**3**

Obtain `SearchIndexOperations` bound to the `Movie` type which is used for field name mapping.

```console
db.movie.createSearchIndex("movie", "vector_index",{"fields": [{"type": "vector","numDimensions": 1536,"path": "plot_embedding", (1) "similarity": "cosine" },{"type": "filter","path": "year"}]})
```

**1**

Field name `plotEmbedding` got mapped to `plot_embedding` considering a `@Field(name = "…")` annotation.

Once created, vector indexes are not immediately ready to use although the `exists` check returns `true`.
The actual status of a search index can be obtained via `SearchIndexOperations#status(…)`.
The `READY` state indicates the index is ready to accept queries.

<a id="mongodb-mongo-search-indexes--mongo.search.vector.query"></a>
<a id="mongodb-mongo-search-indexes--querying-vector-indexes"></a>

### Querying Vector Indexes

Vector indexes can be queried by issuing an aggregation using a `VectorSearchOperation` via `MongoOperations` as shown in the following example

Query a Vector Index

- Java
- Mongo Shell

```java
VectorSearchOperation search = VectorSearchOperation.search("vector_index") (1)
  .path("plotEmbedding") (2)
  .vector( ... )
  .numCandidates(150)
  .limit(10)
  .withSearchScore("score"); (3)

AggregationResults<MovieWithSearchScore> results = mongoTemplate
  .aggregate(newAggregation(Movie.class, search), MovieWithSearchScore.class);
```

**1**

Provide the name of the vector index to query since a collection may hold multiple ones.

**2**

The name of the path used for comparison.

**3**

Optionally add the search score with given name to the result document.

```console
db.embedded_movies.aggregate([{"$vectorSearch": {"index": "vector_index","path": "plot_embedding", (1) "queryVector": [ ... ],"numCandidates": 150,"limit": 10} },{"$addFields": {"score": { $meta: "vectorSearchScore" }}} ])
```

**1**

Field name `plotEmbedding` got mapped to `plot_embedding` considering a `@Field(name = "…")` annotation.

---

<a id="mongodb-mongo-encryption"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/mongo-encryption.html -->

<!-- page_index: 35 -->

# Encryption

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-mongo-encryption--page-title"></a>
<a id="mongodb-mongo-encryption--encryption"></a>

# Encryption

Client Side Encryption is a feature that encrypts data in your application before it is sent to MongoDB.
We recommend you get familiar with the concepts, ideally from the [MongoDB Documentation](https://www.mongodb.com/docs/manual/core/security-in-use-encryption/) to learn more about its capabilities and restrictions before you continue applying Encryption through Spring Data.

> [!NOTE]
> Make sure to set the drivers `com.mongodb.AutoEncryptionSettings` to use client-side encryption.
> MongoDB does not support encryption for all field types.
> Specific data types require deterministic encryption to preserve equality comparison functionality.

<a id="mongodb-mongo-encryption--_client_side_field_level_encryption_csfle"></a>
<a id="mongodb-mongo-encryption--client-side-field-level-encryption-csfle"></a>

## Client Side Field Level Encryption (CSFLE)

Choosing CSFLE gives you full flexibility and allows you to use different keys for a single field, eg. in a one key per tenant scenario.
Please make sure to consult the [MongoDB CSFLE Documentation](https://www.mongodb.com/docs/manual/core/csfle/) before you continue reading.

<a id="mongodb-mongo-encryption--mongo.encryption.automatic"></a>
<a id="mongodb-mongo-encryption--automatic-encryption-csfle"></a>

### Automatic Encryption (CSFLE)

MongoDB supports [Client-Side Field Level Encryption](https://www.mongodb.com/docs/manual/core/csfle/) out of the box using the MongoDB driver with its Automatic Encryption feature.
Automatic Encryption requires a [JSON Schema](#mongodb-mapping-mapping-schema) that allows to perform encrypted read and write operations without the need to provide an explicit en-/decryption step.

Please refer to the [JSON Schema](#mongodb-mapping-mapping-schema--mongo.jsonschema.encrypted-fields) section for more information on defining a JSON Schema that holds encryption information.

To use a `MongoJsonSchema`, you must supply it together with `AutoEncryptionSettings` which can be done e.g., via a `MongoClientSettingsBuilderCustomizer`.

```java
@Bean
MongoClientSettingsBuilderCustomizer customizer(MappingContext mappingContext) {
    return (builder) -> {

        // ... keyVaultCollection, kmsProvider, ...

        MongoJsonSchemaCreator schemaCreator = MongoJsonSchemaCreator.create(mappingContext);
        MongoJsonSchema patientSchema = schemaCreator
            .filter(MongoJsonSchemaCreator.encryptedOnly())
            .createSchemaFor(Patient.class);

        AutoEncryptionSettings autoEncryptionSettings = AutoEncryptionSettings.builder()
            .keyVaultNamespace(keyVaultCollection)
            .kmsProviders(kmsProviders)
            .extraOptions(extraOpts)
            .schemaMap(Collections.singletonMap("db.patient", patientSchema.schemaDocument().toBsonDocument()))
            .build();

        builder.autoEncryptionSettings(autoEncryptionSettings);
    };
}
```

<a id="mongodb-mongo-encryption--mongo.encryption.explicit"></a>
<a id="mongodb-mongo-encryption--explicit-encryption-csfle"></a>

### Explicit Encryption (CSFLE)

Explicit encryption uses the MongoDB driver’s encryption library (`org.mongodb:mongodb-crypt`) to perform encryption and decryption tasks.
The `@ExplicitEncrypted` annotation is a combination of the `@Encrypted` annotation used for [JSON Schema creation](#mongodb-mapping-mapping-schema--mongo.jsonschema.encrypted-fields) and a [Property Converter](#mongodb-mapping-property-converters).
In other words, `@ExplicitEncrypted` uses existing building blocks to combine them for simplified explicit encryption support.

> [!NOTE]
> Fields annotated with `@ExplicitEncrypted` are always encrypted as whole.
> Consider the following example:
>
> ```java
> @ExplicitEncrypted(…)
> String simpleValue;        (1)
>
> @ExplicitEncrypted(…)
> Address address;           (2)
>
> @ExplicitEncrypted(…)
> List<...> list;            (3)
>
> @ExplicitEncrypted(…)
> Map<..., ...> mapOfString; (4)
> ```
>
> | **1** | Encrypts the value of the simple type such as a `String` if not `null`. |
> | --- | --- |
> | **2** | Encrypts the entire `Address` object and all its nested fields as `Document`. To only encrypt parts of the `Address`, like `Address#street` the `street` field within `Address` needs to be annotated with `@ExplicitEncrypted`. |
> | **3** | `Collection`-like fields are encrypted as single value and not per entry. |
> | **4** | `Map`-like fields are encrypted as single value and not as a key/value entry.

Client-Side Field Level Encryption allows you to choose between a deterministic and a randomized algorithm. Depending on the [chosen algorithm](https://www.mongodb.com/docs/v5.0/reference/security-client-side-automatic-json-schema/#std-label-field-level-encryption-json-schema/), [different operations](https://www.mongodb.com/docs/manual/core/csfle/reference/supported-operations/) may be supported.
To pick a certain algorithm use `@ExplicitEncrypted(algorithm)`, see `EncryptionAlgorithms` for algorithm constants.
Please read the [Encryption Types](https://www.mongodb.com/docs/manual/core/csfle/fundamentals/encryption-algorithms) manual for more information on algorithms and their usage.

To perform the actual encryption we require a Data Encryption Key (DEK).
Please refer to the [MongoDB Documentation](https://www.mongodb.com/docs/manual/core/csfle/quick-start/#create-a-data-encryption-key) for more information on how to set up key management and create a Data Encryption Key.
The DEK can be referenced directly via its `id` or a defined *alternative name*.
The `@EncryptedField` annotation only allows referencing a DEK via an alternative name.
It is possible to provide an `EncryptionKeyResolver`, which will be discussed later, to any DEK.

Example 1. Reference the Data Encryption Key

```java
@EncryptedField(algorithm=…, altKeyName = "secret-key") (1)
String ssn;
```

```java
@EncryptedField(algorithm=…, altKeyName = "/name")      (2)
String ssn;
```

**1**

Use the DEK stored with the alternative name `secret-key`.

**2**

Uses a field reference that will read the actual field value and use that for key lookup.
Always requires the full document to be present for save operations.
Fields cannot be used in queries/aggregations.

By default, the `@ExplicitEncrypted(value=…)` attribute references a `MongoEncryptionConverter`.
It is possible to change the default implementation and exchange it with any `PropertyValueConverter` implementation by providing the according type reference.
To learn more about custom `PropertyValueConverters` and the required configuration, please refer to the [Property Converters - Mapping specific fields](#mongodb-mapping-property-converters) section.

<a id="mongodb-mongo-encryption--mongo.encryption.queryable"></a>
<a id="mongodb-mongo-encryption--queryable-encryption-qe"></a>

## Queryable Encryption (QE)

Choosing QE enables you to run different types of queries, like *range* or *equality*, against encrypted fields.
Please make sure to consult the [MongoDB QE Documentation](https://www.mongodb.com/docs/manual/core/queryable-encryption/) before you continue reading to learn more about QE features and limitations.

<a id="mongodb-mongo-encryption--_collection_setup"></a>
<a id="mongodb-mongo-encryption--collection-setup"></a>

### Collection Setup

Queryable Encryption requires upfront declaration of certain aspects allowed within an actual query against an encrypted field.
The information covers the algorithm in use as well as allowed query types along with their attributes and must be provided when creating the collection.

`MongoOperations#createCollection(…)` can be used to do the initial setup for collections utilizing QE.
The configuration for QE via Spring Data uses the same building blocks (a [JSON Schema creation](#mongodb-mapping-mapping-schema--mongo.jsonschema.encrypted-fields)) as CSFLE, converting the schema/properties into the configuration format required by MongoDB.

You can configure Queryable Encryption either manually or in a derived way:

**Manual setup**

Manual setup gives you full control over how encrypted fields are declared and how collections are created.
It’s useful when you need to explicitly manage data keys, encryption algorithms, and field mappings.

- ✅ Full control over encryption configuration
- ✅ Explicitly manage data keys and algorithms
- ✅ Allows for complex encryption scenarios
- ✅ Explicit configuration avoids the risk of surprises (e.g. missing configuration because of improper annotations or class-path scanning)
- ⚠️ An Explicit Field Configuration can diverge from the domain model and you must keep it in sync with the domain model

**Derived setup**

Derived setup relies on annotations in your domain model and automatically generates the required encrypted field configuration from it.
This is simpler and recommended for typical Spring applications where your data model is already annotated.

- ✅ Domain model-driven configuration
- ✅ Easy to set up and maintain
- ⚠️ Might not cover all complex scenarios
- ⚠️ Risk of surprises (e.g. missing configuration for documents based on subtypes because of improper annotations or class-path scanning)

- Manual Collection Setup
- Derived Collection Setup
- MongoDB Collection Info

```java
BsonBinary pinDK = clientEncryption.createDataKey("local", new com.mongodb.client.model.vault.DataKeyOptions());
BsonBinary ssnDK = clientEncryption.createDataKey("local", new com.mongodb.client.model.vault.DataKeyOptions());
BsonBinary ageDK = clientEncryption.createDataKey("local", new com.mongodb.client.model.vault.DataKeyOptions());
BsonBinary signDK = clientEncryption.createDataKey("local", new com.mongodb.client.model.vault.DataKeyOptions());

CollectionOptions collectionOptions = CollectionOptions.encryptedCollection(options -> options
    .encrypted(string("pin"), pinDK)
    .queryable(encrypted(string("ssn")).algorithm("Indexed").keyId(ssnDK.asUuid()), equality().contention(0))
    .queryable(encrypted(int32("age")).algorithm("Range").keyId(ageDK.asUuid()), range().contention(8).min(0).max(150))
    .queryable(encrypted(int64("address.sign")).algorithm("Range").keyId(signDK.asUuid()), range().contention(2).min(-10L).max(10L))
);

mongoTemplate.createCollection(Patient.class, collectionOptions); (1)
```

**1**

Using the template to create the collection may prevent capturing generated keyIds. In this case render the `Document` from the options and use the `createEncryptedCollection(…)` method via the encryption library.

```java
class Patient {

    @Id String id;        (1)

    Address address;      (1)

    @Encrypted(algorithm = "Unindexed")
    String pin;           (2)

    @Encrypted(algorithm = "Indexed")
    @Queryable(queryType = "equality", contentionFactor = 0)
    String ssn;           (3)

    @RangeEncrypted(contentionFactor = 8, rangeOptions = "{ 'min' : 0, 'max' : 150 }")
    Integer age;          (4)

    @RangeEncrypted(contentionFactor = 0L,
        rangeOptions = "{\"min\": {\"$numberDouble\": \"0.3\"}, \"max\": {\"$numberDouble\": \"2.5\"}, \"precision\": 2 }")
    double height;        (5)
}

MongoJsonSchema patientSchema = MongoJsonSchemaCreator.create(mappingContext)
    .filter(MongoJsonSchemaCreator.encryptedOnly())
    .createSchemaFor(Patient.class);

Document encryptedFields = CollectionOptions.encryptedCollection(patientSchema)
        .getEncryptedFieldsOptions()
        .map(CollectionOptions.EncryptedFieldsOptions::toDocument)
        .orElseThrow();

template.execute(db -> clientEncryption.createEncryptedCollection(db, template.getCollectionName(Patient.class), new CreateCollectionOptions()
        .encryptedFields(encryptedFields), new CreateEncryptedCollectionParams("local"))); (1)
```

| **1** | `id` and `address` are not encrypted. Those fields can be queried normally. |
| --- | --- |
| **2** | `pin` is encrypted but does not support queries. |
| **3** | `ssn` is encrypted and allows equality queries. |
| **4** | `age` is encrypted and allows range queries between `0` and `150`. |
| **5** | `height` is encrypted and allows range queries between `0.3` and `2.5`. |

The `Queryable` annotation allows to define allowed query types for encrypted fields.
`@RangeEncrypted` is a combination of `@Encrypted` and `@Queryable` for fields allowing `range` queries.
It is possible to create custom annotations out of the provided ones.

```json
{name: 'patient',type: 'collection',options: {encryptedFields: {escCollection: 'enxcol_.test.esc',ecocCollection: 'enxcol_.test.ecoc',fields: [{keyId: ...,path: 'ssn',bsonType: 'string',queries: [ { queryType: 'equality', contention: Long('0') } ] },{keyId: ...,path: 'age',bsonType: 'int',queries: [ { queryType: 'range', contention: Long('8'), min: 0, max: 150 } ] },{keyId: ...,path: 'pin',bsonType: 'string' },{keyId: ...,path: 'address.sign',bsonType: 'long',queries: [ { queryType: 'range', contention: Long('2'), min: Long('-10'), max: Long('10') } ]}]}}}
```

> [!NOTE]
> - It is not possible to use both QE and CSFLE within the same collection.
> - It is not possible to query a `range` indexed field with an `equality` operator.
> - It is not possible to query an `equality` indexed field with a `range` operator.
> - It is not possible to set `bypassAutoEncrytion(true)`.
> - It is not possible to use self maintained encryption keys via `@Encrypted` in combination with Queryable Encryption.
> - Contention is only optional on the server side, the clients requires you to set the value (Default us `8`).
> - Additional options for eg. `min` and `max` need to match the actual field type. Make sure to use `$numberLong` etc. to ensure target types when parsing bson String.
> - Queryable Encryption will an extra field `safeContent` to each of your documents.
>   Unless explicitly excluded the field will be loaded into memory when retrieving results.
> - For a complete example, see:
>   [spring-data-queryable-encryption](https://github.com/mongodb-developer/spring-data-queryable-encryption)

<a id="mongodb-mongo-encryption--mongo.encryption.queryable.automatic"></a>
<a id="mongodb-mongo-encryption--automatic-encryption-qe"></a>

### Automatic Encryption (QE)

MongoDB supports Queryable Encryption out of the box using the MongoDB driver with its Automatic Encryption feature.
Automatic Encryption requires a [JSON Schema](#mongodb-mapping-mapping-schema) that allows to perform encrypted read and write operations without the need to provide an explicit en-/decryption step.

All you need to do is create the collection according to the MongoDB documentation.
You may utilize techniques to create the required configuration outlined in the section above.

<a id="mongodb-mongo-encryption--mongo.encryption.queryable.manual"></a>
<a id="mongodb-mongo-encryption--explicit-encryption-qe"></a>

### Explicit Encryption (QE)

Explicit encryption uses the MongoDB driver’s encryption library (`org.mongodb:mongodb-crypt`) to perform encryption and decryption tasks based on the meta information provided by annotation within the domain model.

> [!NOTE]
> There is no official support for using Explicit Queryable Encryption.
> The audacious user may combine `@Encrypted` and `@Queryable` with `@ValueConverter(MongoEncryptionConverter.class)` at their own risk.

<a id="mongodb-mongo-encryption--mongo.encryption.converter-setup"></a>
<a id="mongodb-mongo-encryption--mongoencryptionconverter-setup"></a>

## MongoEncryptionConverter Setup

The converter setup for `MongoEncryptionConverter` requires a few steps as several components are involved.
The bean setup consists of the following:

1. The `ClientEncryption` engine
2. A `MongoEncryptionConverter` instance configured with `ClientEncryption` and a `EncryptionKeyResolver`.
3. A `PropertyValueConverterFactory` that uses the registered `MongoEncryptionConverter` bean.

The `EncryptionKeyResolver` uses an `EncryptionContext` providing access to the property allowing for dynamic DEK resolution.

Example 2. Sample MongoEncryptionConverter Configuration

```java
class Config extends AbstractMongoClientConfiguration {

    @Autowired ApplicationContext appContext;

    @Bean
    ClientEncryption clientEncryption() {                                                            (1)
        ClientEncryptionSettings encryptionSettings = ClientEncryptionSettings.builder();
        // …

        return ClientEncryptions.create(encryptionSettings);
    }

    @Bean
    MongoEncryptionConverter encryptingConverter(ClientEncryption clientEncryption) {

        Encryption<BsonValue, BsonBinary> encryption = MongoClientEncryption.just(clientEncryption);
        EncryptionKeyResolver keyResolver = EncryptionKeyResolver.annotated((ctx) -> …);             (2)

        return new MongoEncryptionConverter(encryption, keyResolver);                                (3)
    }

    @Override
    protected void configureConverters(MongoConverterConfigurationAdapter adapter) {

        adapter
            .registerPropertyValueConverterFactory(PropertyValueConverterFactory.beanFactoryAware(appContext)); (4)
    }
}
```

**1**

Set up a `Encryption` engine using `com.mongodb.client.vault.ClientEncryption`.
The instance is stateful and must be closed after usage.
Spring takes care of this because `ClientEncryption` is `Closeable`.

**2**

Set up an annotation-based `EncryptionKeyResolver` to determine the `EncryptionKey` from annotations.

**3**

Create the `MongoEncryptionConverter`.

**4**

Enable for a `PropertyValueConverter` lookup from the `BeanFactory`.

---

<a id="mongodb-aot"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/aot.html -->

<!-- page_index: 36 -->

# Ahead of Time Optimizations

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-aot--page-title"></a>
<a id="mongodb-aot--ahead-of-time-optimizations"></a>

# Ahead of Time Optimizations

This chapter covers Spring Data’s Ahead of Time (AOT) optimizations that build upon [Spring’s Ahead of Time Optimizations](https://docs.spring.io/spring-framework/reference/7.0/core/aot.html).

<a id="mongodb-aot--aot.bestpractices"></a>
<a id="mongodb-aot--best-practices"></a>

## Best Practices

<a id="mongodb-aot--_annotate_your_domain_types"></a>
<a id="mongodb-aot--annotate-your-domain-types"></a>

### Annotate your Domain Types

During application startup, Spring scans the classpath for domain classes for early processing of entities.
By annotating your domain types with Spring Data Store specific `@Table`, `@Document` or `@Entity` annotations you can aid initial entity scanning and ensure that those types are registered with `ManagedTypes` for Runtime Hints.
Classpath scanning is not possible in native image arrangements and so Spring has to use `ManagedTypes` for the initial entity set.

<a id="mongodb-aot--aot.code-gen"></a>
<a id="mongodb-aot--ahead-of-time-code-generation"></a>

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

<a id="mongodb-aot--aot.repositories"></a>
<a id="mongodb-aot--ahead-of-time-repositories"></a>

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

<a id="mongodb-aot--aot.repositories.json"></a>
<a id="mongodb-aot--repository-metadata"></a>

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

<a id="mongodb-aot--aot.hints"></a>
<a id="mongodb-aot--native-image-runtime-hints"></a>

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

<a id="mongodb-aot--_mongodb_specific_ahead_of_time_features"></a>
<a id="mongodb-aot--mongodb-specific-ahead-of-time-features"></a>

## MongoDB Specific Ahead Of Time Features

<a id="mongodb-aot--aot.repositories.mongodb"></a>
<a id="mongodb-aot--mongodb-ahead-of-time-repositories"></a>

### MongoDB Ahead of Time Repositories

With Spring Data MongoDb we generally support query methods that are not backed by an [implementation fragment](#repositories-custom-implementations), and don’t require, with a few limitations detailed below.

> [!NOTE]
> Reactive Repository interfaces using Project Reactor, Kotlin Coroutines et. al. are not supported.

**Supported Features**

- Derived `find`, `count`, `exists` and `delete` methods
- Query methods annotated with `@Query` (excluding those containing SpEL)
- Methods annotated with `@Aggregation`, `@Update`, and `@VectorSearch`
- `@Hint`, `@Meta`, and `@ReadPreference` support
- `Page`, `Slice`, and `Optional` return types
- DTO & Interface Projections

**Limitations**

- `@Meta.flags` is not evaluated.
- Limited `Collation` detection.
- No support for in-clauses with pattern matching / case insensitivity.
- Custom Collection return types (e.g. `io.vavr.collection`, `org.eclipse.collections`) are not yet supported.

**Excluded methods**

- `CrudRepository` and other base interface methods
- Querydsl and Query by Example methods
- Query Methods obtaining MQL from a file

> [!TIP]
> Consider using `Pattern` instead of `String` as parameter type when working with derived queries using the `LIKE` keyword.
>
> ```java
> List<Person> findByLastnameLike(Pattern lastname);
> ```

---

<a id="repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories.html -->

<!-- page_index: 37 -->

<a id="repositories--page-title"></a>
<a id="repositories--repositories"></a>

# Repositories

This chapter explains the basic foundations of Spring Data repositories and MongoDB specifics.
Before continuing to the MongoDB specifics, make sure you have a sound understanding of the basic concepts explained in [Working with Spring Data Repositories](#repositories-core-concepts).

The goal of the Spring Data repository abstraction is to significantly reduce the amount of boilerplate code required to implement data access layers for various persistence stores.

---

<a id="repositories-core-concepts"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/core-concepts.html -->

<!-- page_index: 38 -->

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

The [`CrudRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/CrudRepository.html) and [`ListCrudRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/ListCrudRepository.html) interfaces provide sophisticated CRUD functionality for the entity class that is being managed.

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

In addition to `CrudRepository`, there are [`PagingAndSortingRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/PagingAndSortingRepository.html) and [`ListPagingAndSortingRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/ListPagingAndSortingRepository.html) which add additional methods to ease paginated access to entities:

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

<a id="repositories-core-concepts--is-new-state-detection"></a>
<a id="repositories-core-concepts--entity-state-detection-strategies"></a>

## Entity State Detection Strategies

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
See the [Javadoc](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/domain/Persistable.html) for details.

*Note: Properties of `Persistable` will get detected and persisted if you use `AccessType.PROPERTY`.
To avoid that, use `@Transient`.*

---

<a id="repositories-definition"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/definition.html -->

<!-- page_index: 39 -->

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

<a id="mongodb-repositories-repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/repositories/repositories.html -->

<!-- page_index: 40 -->

# MongoDB Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-repositories-repositories--page-title"></a>
<a id="mongodb-repositories-repositories--mongodb-repositories"></a>

# MongoDB Repositories

This chapter points out the specialties for repository support for MongoDB.
This chapter builds on the core repository support explained in [core concepts](#repositories-core-concepts).
You should have a sound understanding of the basic concepts explained there.

<a id="mongodb-repositories-repositories--mongo-repo-usage"></a>
<a id="mongodb-repositories-repositories--usage"></a>

## Usage

To access domain entities stored in a MongoDB, you can use our sophisticated repository support that eases implementation quite significantly.
To do so, create an interface for your repository, as the following example shows:

Example 1. Sample Person entity

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

Note that the domain type shown in the preceding example has a property named `id` of type `String`.The default serialization mechanism used in `MongoTemplate` (which backs the repository support) regards properties named `id` as the document ID.
Currently, we support `String`, `ObjectId`, and `BigInteger` as ID types.
Please see [ID mapping](#mongodb-template-crud-operations--mongo-template.id-handling) for more information about on how the `id` field is handled in the mapping layer.

Now that we have a domain object, we can define an interface that uses it, as follows:

Basic repository interface to persist Person entities

- Imperative
- Reactive

```java
public interface PersonRepository extends PagingAndSortingRepository<Person, String> {

    // additional custom query methods go here
}
```

```java
public interface PersonRepository extends ReactiveSortingRepository<Person, String> {

    // additional custom query methods go here
}
```

To start using the repository, use the `@EnableMongoRepositories` annotation.
That annotation carries the same attributes as the namespace element.
If no base package is configured, the infrastructure scans the package of the annotated configuration class.
The following example shows how to configuration your application to use MongoDB repositories:

- Imperative
- Reactive
- XML

```java
@Configuration @EnableMongoRepositories("com.acme..repositories") class ApplicationConfig extends AbstractMongoClientConfiguration {
@Override protected String getDatabaseName() {return "e-store";}
@Override protected String getMappingBasePackage() {return "com.acme..repositories";}}
```

```java
@Configuration @EnableReactiveMongoRepositories("com.acme..repositories") class ApplicationConfig extends AbstractReactiveMongoConfiguration {
@Override protected String getDatabaseName() {return "e-store";}
@Override protected String getMappingBasePackage() {return "com.acme..repositories";}}
```

> [!NOTE]
> MongoDB uses two different drivers for imperative (synchronous/blocking) and reactive (non-blocking) data access. You must create a connection by using the Reactive Streams driver to provide the required infrastructure for Spring Data’s Reactive MongoDB support. Consequently, you must provide a separate configuration for MongoDB’s Reactive Streams driver. Note that your application operates on two different connections if you use reactive and blocking Spring Data MongoDB templates and repositories.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:mongo="http://www.springframework.org/schema/data/mongo"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    https://www.springframework.org/schema/beans/spring-beans-3.0.xsd
    http://www.springframework.org/schema/data/mongo
    https://www.springframework.org/schema/data/mongo/spring-mongo-1.0.xsd">

  <mongo:mongo-client id="mongoClient" />

  <bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
    <constructor-arg ref="mongoClient" />
    <constructor-arg value="databaseName" />
  </bean>

  <mongo:repositories base-package="com.acme.*.repositories" />

</beans>
```

This namespace element causes the base packages to be scanned for interfaces that extend `MongoRepository` and create Spring beans for each one found.
By default, the repositories get a `MongoTemplate` Spring bean wired that is called `mongoTemplate`, so you only need to configure `mongo-template-ref` explicitly if you deviate from this convention.

Because our domain repository extends `PagingAndSortingRepository`, it provides you with methods for paginated and sorted access to the entities.
In the case of reactive repositories only `ReactiveSortingRepository` is available since the notion of a `Page` is not applicable.
However finder methods still accept a `Sort` and `Limit` parameter.

> [!NOTE]
> The reactive space offers various reactive composition libraries. The most common libraries are [RxJava](https://github.com/ReactiveX/RxJava) and [Project Reactor](https://projectreactor.io/).
>
> Spring Data MongoDB is built on top of the [MongoDB Reactive Streams](https://mongodb.github.io/mongo-java-driver-reactivestreams/) driver, to provide maximal interoperability by relying on the [Reactive Streams](https://www.reactive-streams.org/) initiative. Static APIs, such as `ReactiveMongoOperations`, are provided by using Project Reactor’s `Flux` and `Mono` types. Project Reactor offers various adapters to convert reactive wrapper types (`Flux` to `Observable` and vice versa), but conversion can easily clutter your code.
>
> Spring Data’s Reactive Repository abstraction is a dynamic API, mostly defined by you and your requirements as you declare query methods. Reactive MongoDB repositories can be implemented by using either RxJava or Project Reactor wrapper types by extending from one of the following library-specific repository interfaces:
>
> - `ReactiveCrudRepository`
> - `ReactiveSortingRepository`
> - `RxJava3CrudRepository`
> - `RxJava3SortingRepository`
>
> Spring Data converts reactive wrapper types behind the scenes so that you can stick to your favorite composition library.

In case you want to obtain methods for basic CRUD operations also add the `CrudRepository` interface.
Working with the repository instance is just a matter of dependency injecting it into a client .
Consequently, accessing the second page of `Person` objects at a page size of 10 would resemble the following code:

Paging access to Person entities

- Imperative
- Reactive

```java
@ExtendWith(SpringExtension.class)
@ContextConfiguration
class PersonRepositoryTests {

    @Autowired PersonRepository repository;

    @Test
    void readsFirstPageCorrectly() {

      Page<Person> persons = repository.findAll(PageRequest.of(0, 10));
      assertThat(persons.isFirstPage()).isTrue();
    }
}
```

```java
@ExtendWith(SpringExtension.class)
@ContextConfiguration
class PersonRepositoryTests {

    @Autowired PersonRepository repository;

    @Test
    void readsFirstPageCorrectly() {

        Flux<Person> persons = repository.findAll(Sort.unsorted(), Limit.of(10));

        persons.as(StepVerifer::create)
            .expectNextCount(10)
            .verifyComplete();
    }
}
```

The preceding example creates an application context with Spring’s unit test support, which performs annotation-based dependency injection into test cases.
Inside the test method, we use the repository to query the datastore.
We hand the repository a `PageRequest` instance that requests the first page of `Person` objects at a page size of 10.

---

<a id="repositories-core-extensions"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/core-extensions.html -->

<!-- page_index: 41 -->

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

<a id="repositories-core-extensions--mongodb.repositories.queries.type-safe"></a>
<a id="repositories-core-extensions--type-safe-query-methods-with-querydsl"></a>

### Type-safe Query Methods with Querydsl

MongoDB repository and its reactive counterpart integrates with the [Querydsl](http://www.querydsl.com/) project, which provides a way to perform type-safe queries.

> Instead of writing queries as inline strings or externalizing them into XML files they are constructed via a fluent API.

— Querydsl Team

It provides the following features:

- Code completion in the IDE (all properties, methods, and operations can be expanded in your favorite Java IDE).
- Almost no syntactically invalid queries allowed (type-safe on all levels).
- Domain types and properties can be referenced safely — no strings involved!
- Adapts better to refactoring changes in domain types.
- Incremental query definition is easier.

See the [Querydsl documentation](http://www.querydsl.com/static/querydsl/latest/reference/html/) for how to bootstrap your environment for APT-based code generation using Maven or Ant.

QueryDSL lets you write queries such as the following:

- Imperative
- Reactive

```java
QPerson person = QPerson.person;
List<Person> result = repository.findAll(person.address.zipCode.eq("C0123"));

Page<Person> page = repository.findAll(person.lastname.contains("a"),
                                       PageRequest.of(0, 2, Direction.ASC, "lastname"));
```

```java
QPerson person = QPerson.person;

Flux<Person> result = repository.findAll(person.address.zipCode.eq("C0123"));
```

`QPerson` is a class that is generated by the Java annotation processor.
See [Setting up Annotation Processing](#repositories-core-extensions--mongodb.repositories.queries.type-safe.apt) for how to set up Annotation Processing with your Build System.
It is a `Predicate` that lets you write type-safe queries.
Notice that there are no strings in the query other than the `C0123` value.

You can use the generated `Predicate` class by using the `QuerydslPredicateExecutor` / `ReactiveQuerydslPredicateExecutor` interface, which the following listing shows:

- Imperative
- Reactive

```java
public interface QuerydslPredicateExecutor<T> {

    Optional<T> findOne(Predicate predicate);

    List<T> findAll(Predicate predicate);

    List<T> findAll(Predicate predicate, Sort sort);

    List<T> findAll(Predicate predicate, OrderSpecifier<?>... orders);

    Page<T> findAll(Predicate predicate, Pageable pageable);

    List<T> findAll(OrderSpecifier<?>... orders);

    long count(Predicate predicate);

    boolean exists(Predicate predicate);

    <S extends T, R> R findBy(Predicate predicate, Function<FluentQuery.FetchableFluentQuery<S>, R> queryFunction);
}
```

```java
interface ReactiveQuerydslPredicateExecutor<T> {

    Mono<T> findOne(Predicate predicate);

    Flux<T> findAll(Predicate predicate);

    Flux<T> findAll(Predicate predicate, Sort sort);

    Flux<T> findAll(Predicate predicate, OrderSpecifier<?>... orders);

    Flux<T> findAll(OrderSpecifier<?>... orders);

    Mono<Long> count(Predicate predicate);

    Mono<Boolean> exists(Predicate predicate);

    <S extends T, R, P extends Publisher<R>> P findBy(Predicate predicate,
            Function<FluentQuery.ReactiveFluentQuery<S>, P> queryFunction);
}
```

To use this in your repository implementation, add it to the list of repository interfaces from which your interface inherits, as the following example shows:

- Imperative
- Reactive

```java
interface PersonRepository extends MongoRepository<Person, String>, QuerydslPredicateExecutor<Person> {

    // additional query methods go here
}
```

```java
interface PersonRepository extends ReactiveMongoRepository<Person, String>, ReactiveQuerydslPredicateExecutor<Person> {

    // additional query methods go here
}
```

> [!NOTE]
> Please note that joins (DBRef’s) are not supported with Reactive MongoDB support.

<a id="repositories-core-extensions--mongodb.repositories.queries.type-safe.apt"></a>
<a id="repositories-core-extensions--setting-up-annotation-processing"></a>

### Setting up Annotation Processing

To use Querydsl with Spring Data MongoDB, you need to set up annotation processing in your build system that generates the `Q` classes.
While you could write the `Q` classes by hand, it is recommended to use the Querydsl annotation processor to generate them for you to keep your `Q` classes in sync with your domain model.

Spring Data MongoDB ships with an annotation processor [`MongoAnnotationProcessor`](https://docs.spring.io/spring-data/mongodb/reference/api/java/org/springframework/data/mongodb/repository/support/MongoAnnotationProcessor.html) that isn’t registered by default.
Typically, annotation processors are registered through Java’s service loader via `META-INF/services/javax.annotation.processing.Processor` that also activates these once you have them on the class path.
Most Spring Data users do not use Querydsl, so it does not make sense to require additional mandatory dependencies for projects that would not benefit from Querydsl.
Hence, you need to activate annotation processing in your build system.

The following example shows how to set up annotation processing by mentioning dependencies and compiler config changes in Maven and Gradle:

- Maven
- Gradle

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.data</groupId>
        <artifactId>spring-data-mongodb</artifactId>
    </dependency>

    <dependency>
        <groupId>com.querydsl</groupId>
        <artifactId>querydsl-mongodb</artifactId>
        <version>${querydslVersion}</version>

        <!-- Recommended: Exclude the mongo-java-driver to avoid version conflicts -->
        <exclusions>
            <exclusion>
                <groupId>org.mongodb</groupId>
                <artifactId>mongo-java-driver</artifactId>
            </exclusion>
        </exclusions>
    </dependency>

    <dependency>
        <groupId>com.querydsl</groupId>
        <artifactId>querydsl-apt</artifactId>
        <version>${querydslVersion}</version>
        <classifier>jakarta</classifier>
        <scope>provided</scope>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <configuration>
                <annotationProcessors>
                    <annotationProcessor>
                        org.springframework.data.mongodb.repository.support.MongoAnnotationProcessor
                    </annotationProcessor>
                </annotationProcessors>

                <!-- Recommended: Some IDE's might require this configuration to include generated sources for IDE usage -->
                <generatedTestSourcesDirectory>target/generated-test-sources</generatedTestSourcesDirectory>
                <generatedSourcesDirectory>target/generated-sources</generatedSourcesDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

```groovy
dependencies {implementation("com.querydsl:querydsl-mongodb:$querydslVersion") {exclude group: "org.mongodb", module: "mongo-java-driver"}
annotationProcessor "com.querydsl:querydsl-apt:$querydslVersion:jakarta" annotationProcessor "org.springframework.data:spring-data-mongodb"
testAnnotationProcessor "com.querydsl:querydsl-apt:$querydslVersion:jakarta" testAnnotationProcessor "org.springframework.data:spring-data-mongodb"}
tasks.withType(JavaCompile).configureEach {options.compilerArgs += ["-processor","org.springframework.data.mongodb.repository.support.MongoAnnotationProcessor"]}
```

Note that the setup above shows the simplest usage omitting any other options or dependencies that your project might require.
This way of configuring annotation processing disables Java’s annotation processor scanning because MongoDB requires specifying `-processor` by class name.
If you’re using other annotation processors, you need to add them to the list of `-processor`/`annotationProcessors` as well.

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

<a id="repositories-create-instances"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/create-instances.html -->

<!-- page_index: 42 -->

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

Use the store-specific `@EnableMongoRepositories` annotation on a Java configuration class to define a configuration for repository activation.
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

The `basePackages` and `value` attributes in `@EnableMongoRepositories` support `${…}` property placeholders which are resolved against the `Environment` as well as Ant-style package patterns such as `"org.example.**"`.

The following example specifies the `app.scan.packages` property placeholder for the implicit `value` attribute in `@EnableMongoRepositories`.

- Java
- Kotlin

```java
@Configuration
@EnableMongoRepositories("${app.scan.packages}")    (1)
public class ApplicationConfiguration {
  // …
}
```

**1**

`app.scan.packages` property placeholder to be resolved against the `Environment`

```kotlin
@EnableMongoRepositories(["\${app.scan.packages}"]) (1)
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
@EnableMongoRepositories(basePackages = "com.acme.repositories",
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

<a id="repositories-query-methods-details"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/query-methods-details.html -->

<!-- page_index: 43 -->

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
For Java configuration, you can use the `queryLookupStrategy` attribute of the `EnableMongoRepositories` annotation.
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

Using `Pageable`, `Slice`, `ScrollPosition`, `Sort` and `Limit` in query methods

```java
Page<User> findByLastname(String lastname, Pageable pageable);

Slice<User> findByLastname(String lastname, Pageable pageable);

Window<User> findTop10ByLastname(String lastname, ScrollPosition position, Sort sort);

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
<td><p>Offset-based <code>Window&lt;T&gt;</code></p></td>
<td><p><code>limit + 1</code> at <code>OffsetScrollPosition.getOffset()</code></p></td>
<td><p>One to many queries fetching data starting at <code>OffsetScrollPosition.getOffset()</code> applying limiting.</p></td>
<td><div><div>
<p>A <code>Window</code> can only navigate to the next <code>Window</code>.</p>
</div>
<div>
<ul>
<li>
<p><code>Window</code> provides details whether there is more data to fetch.</p>
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
<tr>
<td><p>Keyset-based <code>Window&lt;T&gt;</code></p></td>
<td><p><code>limit + 1</code> using a rewritten <code>WHERE</code> condition</p></td>
<td><p>One to many queries fetching data starting at <code>KeysetScrollPosition.getKeys()</code> applying limiting.</p></td>
<td><div><div>
<p>A <code>Window</code> can only navigate to the next <code>Window</code>.</p>
</div>
<div>
<ul>
<li>
<p><code>Window</code> provides details whether there is more data to fetch.</p>
</li>
<li>
<p>Keyset-based queries require a proper index structure for efficient querying.</p>
</li>
<li>
<p>Most data stores do not work well when Keyset-based query results contain <code>null</code> values.</p>
</li>
<li>
<p>Results must expose all sorting keys in their results requiring projections to select potentially more properties than required for the actual projection.</p>
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

<a id="mongodb-repositories-query-methods"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/repositories/query-methods.html -->

<!-- page_index: 44 -->

# MongoDB-specific Query Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-repositories-query-methods--page-title"></a>
<a id="mongodb-repositories-query-methods--mongodb-specific-query-methods"></a>

# MongoDB-specific Query Methods

Most of the data access operations you usually trigger on a repository result in a query being executed against the MongoDB databases.
Defining such a query is a matter of declaring a method on the repository interface, as the following example shows:

PersonRepository with query methods

- Imperative
- Reactive

```java
public interface PersonRepository extends PagingAndSortingRepository<Person, String> {

    List<Person> findByLastname(String lastname);                      (1)

    Page<Person> findByFirstname(String firstname, Pageable pageable); (2)

    Person findByShippingAddresses(Address address);                   (3)

    Person findFirstByLastname(String lastname);                       (4)

    Stream<Person> findAllBy();                                        (5)
}
```

**1**

The `findByLastname` method shows a query for all people with the given last name.
The query is derived by parsing the method name for constraints that can be concatenated with `And` and `Or`.
Thus, the method name results in a query expression of `{"lastname" : lastname}`.

**2**

Applies pagination to a query.
You can equip your method signature with a `Pageable` parameter and let the method return a `Page` instance and Spring Data automatically pages the query accordingly.

**3**

Shows that you can query based on properties that are not primitive types.
Throws `IncorrectResultSizeDataAccessException` if more than one match is found.

**4**

Uses the `First` keyword to restrict the query to only the first result.
Unlike <3>, this method does not throw an exception if more than one match is found.

**5**

Uses a Java 8 `Stream` that reads and converts individual elements while iterating the stream.

```java
public interface ReactivePersonRepository extends ReactiveSortingRepository<Person, String> {

    Flux<Person> findByFirstname(String firstname);                                   (1)

    Flux<Person> findByFirstname(Publisher<String> firstname);                        (2)

    Flux<Person> findByFirstnameOrderByLastname(String firstname, Pageable pageable); (3)

    Mono<Person> findByFirstnameAndLastname(String firstname, String lastname);       (4)

    Mono<Person> findFirstByLastname(String lastname);                                (5)
}
```

**1**

The method shows a query for all people with the given `lastname`. The query is derived by parsing the method name for constraints that can be concatenated with `And` and `Or`. Thus, the method name results in a query expression of `{"lastname" : lastname}`.

**2**

The method shows a query for all people with the given `firstname` once the `firstname` is emitted by the given `Publisher`.

**3**

Use `Pageable` to pass offset and sorting parameters to the database.

**4**

Find a single entity for the given criteria. It completes with `IncorrectResultSizeDataAccessException` on non-unique results.

**5**

Unless <4>, the first entity is always emitted even if the query yields more result documents.

> [!WARNING]
> The `Page` return type (as in `Mono<Page>`) is not supported by reactive repositories.

It is possible to use `Pageable` in derived finder methods, to pass on `sort`, `limit` and `offset` parameters to the query to reduce load and network traffic.
The returned `Flux` will only emit data within the declared range.

```java
Pageable page = PageRequest.of(1, 10, Sort.by("lastname"));
Flux<Person> persons = repository.findByFirstnameOrderByLastname("luke", page);
```

> [!NOTE]
> We do not support referring to parameters that are mapped as `DBRef` in the domain class.

<details>
<summary>Supported keywords for query methods</summary>
<div>
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Keyword</th>
<th>Sample</th>
<th>Logical result</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>After</code></p></td>
<td><p><code>findByBirthdateAfter(Date date)</code></p></td>
<td><p><code>{"birthdate" : {"$gt" : date}}</code></p></td>
</tr>
<tr>
<td><p><code>GreaterThan</code></p></td>
<td><p><code>findByAgeGreaterThan(int age)</code></p></td>
<td><p><code>{"age" : {"$gt" : age}}</code></p></td>
</tr>
<tr>
<td><p><code>GreaterThanEqual</code></p></td>
<td><p><code>findByAgeGreaterThanEqual(int age)</code></p></td>
<td><p><code>{"age" : {"$gte" : age}}</code></p></td>
</tr>
<tr>
<td><p><code>Before</code></p></td>
<td><p><code>findByBirthdateBefore(Date date)</code></p></td>
<td><p><code>{"birthdate" : {"$lt" : date}}</code></p></td>
</tr>
<tr>
<td><p><code>LessThan</code></p></td>
<td><p><code>findByAgeLessThan(int age)</code></p></td>
<td><p><code>{"age" : {"$lt" : age}}</code></p></td>
</tr>
<tr>
<td><p><code>LessThanEqual</code></p></td>
<td><p><code>findByAgeLessThanEqual(int age)</code></p></td>
<td><p><code>{"age" : {"$lte" : age}}</code></p></td>
</tr>
<tr>
<td><p><code>Between</code></p></td>
<td><p><code>findByAgeBetween(int from, int to)</code>
<code>findByAgeBetween(Range&lt;Integer&gt; range)</code></p></td>
<td><p><code>{"age" : {"$gt" : from, "$lt" : to}}</code>

lower / upper bounds (<code>$gt</code> / <code>$gte</code> &amp; <code>$lt</code> / <code>$lte</code>) according to <code>Range</code></p></td>
</tr>
<tr>
<td><p><code>In</code></p></td>
<td><p><code>findByAgeIn(Collection ages)</code></p></td>
<td><p><code>{"age" : {"$in" : [ages…]}}</code></p></td>
</tr>
<tr>
<td><p><code>NotIn</code></p></td>
<td><p><code>findByAgeNotIn(Collection ages)</code></p></td>
<td><p><code>{"age" : {"$nin" : [ages…]}}</code></p></td>
</tr>
<tr>
<td><p><code>IsNotNull</code>, <code>NotNull</code></p></td>
<td><p><code>findByFirstnameNotNull()</code></p></td>
<td><p><code>{"firstname" : {"$ne" : null}}</code></p></td>
</tr>
<tr>
<td><p><code>IsNull</code>, <code>Null</code></p></td>
<td><p><code>findByFirstnameNull()</code></p></td>
<td><p><code>{"firstname" : null}</code></p></td>
</tr>
<tr>
<td><p><code>Like</code>, <code>StartingWith</code>, <code>EndingWith</code></p></td>
<td><p><code>findByFirstnameLike(String name)</code></p></td>
<td><p><code>{"firstname" : name} (name as regex)</code></p></td>
</tr>
<tr>
<td><p><code>NotLike</code>, <code>IsNotLike</code></p></td>
<td><p><code>findByFirstnameNotLike(String name)</code></p></td>
<td><p><code>{"firstname" : { "$not" : name }} (name as regex)</code></p></td>
</tr>
<tr>
<td><p><code>Containing</code> on String</p></td>
<td><p><code>findByFirstnameContaining(String name)</code></p></td>
<td><p><code>{"firstname" : name} (name as regex)</code></p></td>
</tr>
<tr>
<td><p><code>NotContaining</code> on String</p></td>
<td><p><code>findByFirstnameNotContaining(String name)</code></p></td>
<td><p><code>{"firstname" : { "$not" : name}} (name as regex)</code></p></td>
</tr>
<tr>
<td><p><code>Containing</code> on Collection</p></td>
<td><p><code>findByAddressesContaining(Address address)</code></p></td>
<td><p><code>{"addresses" : { "$in" : address}}</code></p></td>
</tr>
<tr>
<td><p><code>NotContaining</code> on Collection</p></td>
<td><p><code>findByAddressesNotContaining(Address address)</code></p></td>
<td><p><code>{"addresses" : { "$not" : { "$in" : address}}}</code></p></td>
</tr>
<tr>
<td><p><code>Regex</code></p></td>
<td><p><code>findByFirstnameRegex(String firstname)</code></p></td>
<td><p><code>{"firstname" : {"$regex" : firstname }}</code></p></td>
</tr>
<tr>
<td><p><code>(No keyword)</code></p></td>
<td><p><code>findByFirstname(String name)</code></p></td>
<td><p><code>{"firstname" : name}</code></p></td>
</tr>
<tr>
<td><p><code>Not</code></p></td>
<td><p><code>findByFirstnameNot(String name)</code></p></td>
<td><p><code>{"firstname" : {"$ne" : name}}</code></p></td>
</tr>
<tr>
<td><p><code>Near</code></p></td>
<td><p><code>findByLocationNear(Point point)</code></p></td>
<td><p><code>{"location" : {"$near" : [x,y]}}</code></p></td>
</tr>
<tr>
<td><p><code>Near</code></p></td>
<td><p><code>findByLocationNear(Point point, Distance max)</code></p></td>
<td><p><code>{"location" : {"$near" : [x,y], "$maxDistance" : max}}</code></p></td>
</tr>
<tr>
<td><p><code>Near</code></p></td>
<td><p><code>findByLocationNear(Point point, Distance min, Distance max)</code></p></td>
<td><p><code>{"location" : {"$near" : [x,y], "$minDistance" : min, "$maxDistance" : max}}</code></p></td>
</tr>
<tr>
<td><p><code>Within</code></p></td>
<td><p><code>findByLocationWithin(Circle circle)</code></p></td>
<td><p><code>{"location" : {"$geoWithin" : {"$center" : [ [x, y], distance]}}}</code></p></td>
</tr>
<tr>
<td><p><code>Within</code></p></td>
<td><p><code>findByLocationWithin(Box box)</code></p></td>
<td><p><code>{"location" : {"$geoWithin" : {"$box" : [ [x1, y1], x2, y2]}}}</code></p></td>
</tr>
<tr>
<td><p><code>IsTrue</code>, <code>True</code></p></td>
<td><p><code>findByActiveIsTrue()</code></p></td>
<td><p><code>{"active" : true}</code></p></td>
</tr>
<tr>
<td><p><code>IsFalse</code>,  <code>False</code></p></td>
<td><p><code>findByActiveIsFalse()</code></p></td>
<td><p><code>{"active" : false}</code></p></td>
</tr>
<tr>
<td><p><code>Exists</code></p></td>
<td><p><code>findByLocationExists(boolean exists)</code></p></td>
<td><p><code>{"location" : {"$exists" : exists }}</code></p></td>
</tr>
<tr>
<td><p><code>IgnoreCase</code></p></td>
<td><p><code>findByUsernameIgnoreCase(String username)</code></p></td>
<td><p><code>{"username" : {"$regex" : "^username$", "$options" : "i" }}</code></p></td>
</tr>
</tbody>
</table>
</div>
</details>

> [!NOTE]
> If the property criterion compares a document, the order of the fields and exact equality in the document matters.

> [!NOTE]
> In some scenarios, you might require additional options, such as a maximum run time, additional log comments, or the permission to temporarily write data to disk.
> Use the `@Meta` annotation to set those options via `maxExecutionTimeMs`, `comment` or `allowDiskUse`. `@Meta` can only be used on repository query methods, not on base interface or fragment interface methods.

<a id="mongodb-repositories-query-methods--mongodb.repositories.queries.geo-spatial"></a>
<a id="mongodb-repositories-query-methods--geo-spatial-queries"></a>

## Geo-spatial Queries

As you saw in the preceding table of keywords, a few keywords trigger geo-spatial operations within a MongoDB query.
The `Near` and `Within` keywords allows some further modification, as the next few examples show.

The following example shows how to define a `near` / `within` query that finds all persons using different shapes:

Advanced `Near` queries

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    // { 'location' : { '$near' : [point.x, point.y], '$maxDistance' : distance } }
    List<Person> findByLocationNear(Point location, Distance distance);

    // { 'location' : { $geoWithin: { $center: [ [ circle.center.x, circle.center.y ], circle.radius ] } } }
    List<Person> findByLocationWithin(Circle circle);

    // { 'location' : { $geoWithin: { $box: [ [ box.first.x, box.first.y ], [ box.second.x, box.second.y ] ] } } }
    List<Person> findByLocationWithin(Box box);

    // { 'location' : { $geoWithin: { $polygon: [ [ polygon.x1, polygon.y1 ], [ polygon.x2, polygon.y2 ], ... ] } } }
    List<Person> findByLocationWithin(Polygon polygon);

    // { 'location' : { $geoWithin: { $geometry: { $type : 'polygon', coordinates: [[ polygon.x1, polygon.y1 ], [ polygon.x2, polygon.y2 ], ... ] } } } }
    List<Person> findByLocationWithin(GeoJsonPolygon polygon);
}
```

```java
interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    // { 'location' : { '$near' : [point.x, point.y], '$maxDistance' : distance } }
    Flux<Person> findByLocationNear(Point location, Distance distance);

    // { 'location' : { $geoWithin: { $center: [ [ circle.center.x, circle.center.y ], circle.radius ] } } }
    Flux<Person> findByLocationWithin(Circle circle);

    // { 'location' : { $geoWithin: { $box: [ [ box.first.x, box.first.y ], [ box.second.x, box.second.y ] ] } } }
    Flux<Person> findByLocationWithin(Box box);

    // { 'location' : { $geoWithin: { $polygon: [ [ polygon.x1, polygon.y1 ], [ polygon.x2, polygon.y2 ], ... ] } } }
    Flux<Person> findByLocationWithin(Polygon polygon);

    // { 'location' : { $geoWithin: { $geometry: { $type : 'polygon', coordinates: [[ polygon.x1, polygon.y1 ], [ polygon.x2, polygon.y2 ], ... ] } } } }
    Flux<Person> findByLocationWithin(GeoJsonPolygon polygon);
}
```

Adding a `Distance` parameter to the query method allows restricting results to those within the given distance.
If the `Distance` was set up containing a `Metric`, we transparently use `$nearSphere` instead of `$code`, as the following example shows:

Example 1. Using `Distance` with `Metrics`

```java
Point point = new Point(43.7, 48.8);
Distance distance = new Distance(200, Metrics.KILOMETERS);
… = repository.findByLocationNear(point, distance);
// {'location' : {'$nearSphere' : [43.7, 48.8], '$maxDistance' : 0.03135711885774796}}
```

> [!NOTE]
> Reactive Geo-spatial repository queries support the domain type and `GeoResult<T>` results within a reactive wrapper type. `GeoPage` and `GeoResults` are not supported as they contradict the deferred result approach with pre-calculating the average distance. However, you can still pass in a `Pageable` argument to page results yourself.

Using a `Distance` with a `Metric` causes a `$nearSphere` (instead of a plain `$near`) clause to be added.
Beyond that, the actual distance gets calculated according to the `Metrics` used.

(Note that `Metric` does not refer to metric units of measure.
It could be miles rather than kilometers.
Rather, `metric` refers to the concept of a system of measurement, regardless of which system you use.)

> [!NOTE]
> Using `@GeoSpatialIndexed(type = GeoSpatialIndexType.GEO_2DSPHERE)` on the target property forces usage of the `$nearSphere` operator.

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    // {'geoNear' : 'location', 'near' : [x, y] }
    GeoResults<Person> findByLocationNear(Point location);

    // No metric: {'geoNear' : 'person', 'near' : [x, y], maxDistance : distance }
    // Metric: {'geoNear' : 'person', 'near' : [x, y], 'maxDistance' : distance,
    //          'distanceMultiplier' : metric.multiplier, 'spherical' : true }
    GeoResults<Person> findByLocationNear(Point location, Distance distance);

    // Metric: {'geoNear' : 'person', 'near' : [x, y], 'minDistance' : min,
    //          'maxDistance' : max, 'distanceMultiplier' : metric.multiplier,
    //          'spherical' : true }
    GeoResults<Person> findByLocationNear(Point location, Distance min, Distance max);

    // {'geoNear' : 'location', 'near' : [x, y] }
    GeoResults<Person> findByLocationNear(Point location);
}
```

```java
interface PersonRepository extends ReactiveMongoRepository<Person, String>  {

    // {'geoNear' : 'location', 'near' : [x, y] }
    Flux<GeoResult<Person>> findByLocationNear(Point location);

    // No metric: {'geoNear' : 'person', 'near' : [x, y], maxDistance : distance }
    // Metric: {'geoNear' : 'person', 'near' : [x, y], 'maxDistance' : distance,
    //          'distanceMultiplier' : metric.multiplier, 'spherical' : true }
    Flux<GeoResult<Person>> findByLocationNear(Point location, Distance distance);

    // Metric: {'geoNear' : 'person', 'near' : [x, y], 'minDistance' : min,
    //          'maxDistance' : max, 'distanceMultiplier' : metric.multiplier,
    //          'spherical' : true }
    Flux<GeoResult<Person>> findByLocationNear(Point location, Distance min, Distance max);

    // {'geoNear' : 'location', 'near' : [x, y] }
    Flux<GeoResult<Person>> findByLocationNear(Point location);
}
```

<a id="mongodb-repositories-query-methods--mongodb.repositories.queries.json-based"></a>
<a id="mongodb-repositories-query-methods--json-based-query-methods-and-field-restriction"></a>

## JSON-based Query Methods and Field Restriction

By adding the `org.springframework.data.mongodb.repository.Query` annotation to your repository query methods, you can specify a MongoDB JSON query string to use instead of having the query be derived from the method name, as the following example shows:

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    @Query("{ 'firstname' : ?0 }")
    List<Person> findByThePersonsFirstname(String firstname);

}
```

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    @Query("{ 'firstname' : ?0 }")
    Flux<Person> findByThePersonsFirstname(String firstname);

}
```

The `?0` placeholder lets you substitute the value from the method arguments into the JSON query string.

> [!NOTE]
> `String` parameter values are escaped during the binding process, which means that it is not possible to add MongoDB specific operators through the argument.

You can also use the filter property to restrict the set of properties that is mapped into the Java object, as the following example shows:

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    @Query(value="{ 'firstname' : ?0 }", fields="{ 'firstname' : 1, 'lastname' : 1}")
    List<Person> findByThePersonsFirstname(String firstname);

}
```

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    @Query(value="{ 'firstname' : ?0 }", fields="{ 'firstname' : 1, 'lastname' : 1}")
    Flux<Person> findByThePersonsFirstname(String firstname);

}
```

The query in the preceding example returns only the `firstname`, `lastname` and `Id` properties of the `Person` objects.
The `age` property, a `java.lang.Integer`, is not set and its value is therefore null.

<a id="mongodb-repositories-query-methods--mongodb.repositories.queries.json-spel"></a>
<a id="mongodb-repositories-query-methods--json-based-queries-with-spel-expressions"></a>

## JSON-based Queries with SpEL Expressions

Query strings and field definitions can be used together with SpEL expressions to create dynamic queries at runtime.
SpEL expressions can provide predicate values and can be used to extend predicates with subdocuments.

Expressions expose method arguments through an array that contains all the arguments.
The following query uses `[0]`
to declare the predicate value for `lastname` (which is equivalent to the `?0` parameter binding):

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    @Query("{'lastname': ?#{[0]} }")
    List<Person> findByQueryWithExpression(String param0);
}
```

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    @Query("{'lastname': ?#{[0]} }")
    Flux<Person> findByQueryWithExpression(String param0);
}
```

Expressions can be used to invoke functions, evaluate conditionals, and construct values.
SpEL expressions used in conjunction with JSON reveal a side effect, because Map-like declarations inside of SpEL read like JSON, as the following example shows:

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    @Query("{'id': ?#{ [0] ? {$exists :true} : [1] }}")
    List<Person> findByQueryWithExpressionAndNestedObject(boolean param0, String param1);
}
```

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    @Query("{'id': ?#{ [0] ? {$exists :true} : [1] }}")
    Flux<Person> findByQueryWithExpressionAndNestedObject(boolean param0, String param1);
}
```

> [!WARNING]
> SpEL in query strings can be a powerful way to enhance queries.
> However, they can also accept a broad range of unwanted arguments.
> Make sure to sanitize strings before passing them to the query to avoid creation of vulnerabilities or unwanted changes to your query.

Expression support is extensible through the Query SPI: `EvaluationContextExtension` & `ReactiveEvaluationContextExtension`
The Query SPI can contribute properties and functions and can customize the root object.
Extensions are retrieved from the application context at the time of SpEL evaluation when the query is built.
The following example shows how to use an evaluation context extension:

- Imperative
- Reactive

```java
public class SampleEvaluationContextExtension extends EvaluationContextExtensionSupport {
@Override public String getExtensionId() {return "security";}
@Override public Map<String, Object> getProperties() {return Collections.singletonMap("principal", SecurityContextHolder.getCurrent().getPrincipal());}}
```

```java
public class SampleEvaluationContextExtension implements ReactiveEvaluationContextExtension {
@Override public String getExtensionId() {return "security";}
@Override public Mono<? extends EvaluationContextExtension> getExtension() {return Mono.just(new EvaluationContextExtensionSupport() { ... });}}
```

> [!NOTE]
> Bootstrapping `MongoRepositoryFactory` yourself is not application context-aware and requires further configuration to pick up Query SPI extensions.

> [!NOTE]
> Reactive query methods can make use of `org.springframework.data.spel.spi.ReactiveEvaluationContextExtension`.

<a id="mongodb-repositories-query-methods--mongodb.repositories.queries.full-text"></a>
<a id="mongodb-repositories-query-methods--full-text-search-queries"></a>

## Full-text Search Queries

MongoDB’s full-text search feature is store-specific and, therefore, can be found on `MongoRepository` rather than on the more general `CrudRepository`.
We need a document with a full-text index (see “[Text Indexes](#mongodb-mapping-mapping--mapping-usage-indexes.text-index)” to learn how to create a full-text index).

Additional methods on `MongoRepository` take `TextCriteria` as an input parameter.
In addition to those explicit methods, it is also possible to add a `TextCriteria`-derived repository method.
The criteria are added as an additional `AND` criteria.
Once the entity contains a `@TextScore`-annotated property, the document’s full-text score can be retrieved.
Furthermore, the `@TextScore` annotated also makes it possible to sort by the document’s score, as the following example shows:

```java
@Document
class FullTextDocument {

  @Id String id;
  @TextIndexed String title;
  @TextIndexed String content;
  @TextScore Float score;
}

interface FullTextRepository extends Repository<FullTextDocument, String> {

  // Execute a full-text search and define sorting dynamically
  List<FullTextDocument> findAllBy(TextCriteria criteria, Sort sort);

  // Paginate over a full-text search result
  Page<FullTextDocument> findAllBy(TextCriteria criteria, Pageable pageable);

  // Combine a derived query with a full-text search
  List<FullTextDocument> findByTitleOrderByScoreDesc(String title, TextCriteria criteria);
}


Sort sort = Sort.by("score");
TextCriteria criteria = TextCriteria.forDefaultLanguage().matchingAny("spring", "data");
List<FullTextDocument> result = repository.findAllBy(criteria, sort);

criteria = TextCriteria.forDefaultLanguage().matching("film");
Page<FullTextDocument> page = repository.findAllBy(criteria, PageRequest.of(1, 1, sort));
List<FullTextDocument> result = repository.findByTitleOrderByScoreDesc("mongodb", criteria);
```

<a id="mongodb-repositories-query-methods--mongodb.repositories.queries.aggregation"></a>
<a id="mongodb-repositories-query-methods--aggregation-methods"></a>

## Aggregation Methods

The repository layer offers means to interact with [the aggregation framework](#mongodb-aggregation-framework) via annotated repository query methods.
Similar to the [JSON based queries](#mongodb-repositories-repositories--mongodb.repositories.queries.json-based), you can define a pipeline using the `org.springframework.data.mongodb.repository.Aggregation` annotation.
The definition may contain simple placeholders like `?0` as well as [SpEL expressions](https://docs.spring.io/spring-framework/reference/7.0/core.html#expressions) `?#{ … }`.

Example 2. Aggregating Repository Method

```java
public interface PersonRepository extends CrudRepository<Person, String> {

  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : $firstname } } }")
  List<PersonAggregate> groupByLastnameAndFirstnames();                            (1)

  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : $firstname } } }")
  List<PersonAggregate> groupByLastnameAndFirstnames(Sort sort);                   (2)

  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : ?0 } } }")
  List<PersonAggregate> groupByLastnameAnd(String property);                       (3)

  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : ?0 } } }")
  Slice<PersonAggregate> groupByLastnameAnd(String property, Pageable page);       (4)

  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : $firstname } } }")
  Stream<PersonAggregate> groupByLastnameAndFirstnamesAsStream();                  (5)

  @Aggregation(pipeline = {
      "{ '$match' :  { 'lastname' :  '?0'} }",
      "{ '$project': { _id : 0, firstname : 1, lastname : 1 } }"
  })
  Stream<PersonAggregate> groupByLastnameAndFirstnamesAsStream();                  (6)

  @Aggregation("{ $group : { _id : null, total : { $sum : $age } } }")
  SumValue sumAgeUsingValueWrapper();                                              (7)

  @Aggregation("{ $group : { _id : null, total : { $sum : $age } } }")
  Long sumAge();                                                                   (8)

  @Aggregation("{ $group : { _id : null, total : { $sum : $age } } }")
  AggregationResults<SumValue> sumAgeRaw();                                        (9)

  @Aggregation("{ '$project': { '_id' : '$lastname' } }")
  List<String> findAllLastnames();                                                 (10)

  @Aggregation(pipeline = {
		  "{ $group : { _id : '$author', books: { $push: '$title' } } }",
		  "{ $out : 'authors' }"
  })
  void groupAndOutSkippingOutput();                                                (11)
}
```

```java
public class PersonAggregate {
private @Id String lastname;                                                     (2) private List<String> names;
public PersonAggregate(String lastname, List<String> names) {// ...}
// Getter / Setter omitted}
public class SumValue {
private final Long total;                                                        (6) (8)
public SumValue(Long total) {// ...}
// Getter omitted}
interface PersonProjection {String getFirstname(); String getLastname();}
```

**1**

Aggregation pipeline to group first names by `lastname` in the `Person` collection returning these as `PersonAggregate`.

**2**

If `Sort` argument is present, `$sort` is appended after the declared pipeline stages so that it only affects the order of the final results after having passed all other aggregation stages.
Therefore, the `Sort` properties are mapped against the methods return type `PersonAggregate` which turns `Sort.by("lastname")` into `{ $sort : { '_id', 1 } }` because `PersonAggregate.lastname` is annotated with `@Id`.

**3**

Replaces `?0` with the given value for `property` for a dynamic aggregation pipeline.

**4**

`$skip`, `$limit` and `$sort` can be passed on via a `Pageable` argument. Same as in <2>, the operators are appended to the pipeline definition. Methods accepting `Pageable` can return `Slice` for easier pagination.

**5**

Aggregation methods can return interface based projections wrapping the resulting `org.bson.Document` behind a proxy, exposing getters delegating to fields within the document.

**6**

Aggregation methods can return `Stream` to consume results directly from an underlying cursor. Make sure to close the stream after consuming it to release the server-side cursor by either calling `close()` or through `try-with-resources`.

**7**

Map the result of an aggregation returning a single `Document` to an instance of a desired `SumValue` target type.

**8**

Aggregations resulting in single document holding just an accumulation result like e.g. `$sum` can be extracted directly from the result `Document`.
To gain more control, you might consider `AggregationResult` as method return type as shown in <7>.

**9**

Obtain the raw `AggregationResults` mapped to the generic target wrapper type `SumValue` or `org.bson.Document`.

**10**

Like in <6>, a single value can be directly obtained from multiple result `Document`s.

**11**

Skips the output of the `$out` stage when return type is `void`.

In some scenarios, aggregations might require additional options, such as a maximum run time, additional log comments, or the permission to temporarily write data to disk.
Use the `@Meta` annotation to set those options via `maxExecutionTimeMs`, `comment` or `allowDiskUse`.

```java
interface PersonRepository extends CrudRepository<Person, String> {

  @Meta(allowDiskUse = "true")
  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : $firstname } } }")
  List<PersonAggregate> groupByLastnameAndFirstnames();
}
```

Or use `@Meta` to create your own annotation as shown in the sample below.

```java
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.METHOD })
@Meta(allowDiskUse = "true")
@interface AllowDiskUse { }

interface PersonRepository extends CrudRepository<Person, String> {

  @AllowDiskUse
  @Aggregation("{ $group: { _id : $lastname, names : { $addToSet : $firstname } } }")
  List<PersonAggregate> groupByLastnameAndFirstnames();
}
```

> [!NOTE]
> Simple-type single-result inspects the returned `Document` and checks for the following:
>
> 1. Only one entry in the document, return it.
> 2. Two entries, one is the `_id` value. Return the other.
> 3. Return for the first value assignable to the return type.
> 4. Throw an exception if none of the above is applicable.

> [!WARNING]
> The `Page` return type is not supported for repository methods using `@Aggregation`. However, you can use a
> `Pageable` argument to add `$skip`, `$limit` and `$sort` to the pipeline and let the method return `Slice`.

<a id="mongodb-repositories-query-methods--query-by-example"></a>

## Query by Example

<a id="mongodb-repositories-query-methods--query-by-example.introduction"></a>
<a id="mongodb-repositories-query-methods--introduction"></a>

### Introduction

This chapter provides an introduction to Query by Example and explains how to use it.

Query by Example (QBE) is a user-friendly querying technique with a simple interface.
It allows dynamic query creation and does not require you to write queries that contain field names.
In fact, Query by Example does not require you to write queries by using store-specific query languages at all.

> [!NOTE]
> This chapter explains the core concepts of Query by Example.
> The information is pulled from the Spring Data Commons module.
> Depending on your database, String matching support can be limited.

<a id="mongodb-repositories-query-methods--query-by-example.usage"></a>
<a id="mongodb-repositories-query-methods--usage"></a>

### Usage

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
> Properties using primitive types (`int`, `double`, …) are always included unless the [`ExampleMatcher` ignores the property path](#mongodb-repositories-query-methods--query-by-example.matchers).

Examples can be built by either using the `of` factory method or by using [`ExampleMatcher`](#mongodb-repositories-query-methods--query-by-example.matchers). `Example` is immutable.
The following listing shows a simple Example:

Example 3. Simple Example

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

<a id="mongodb-repositories-query-methods--query-by-example.matchers"></a>
<a id="mongodb-repositories-query-methods--example-matchers"></a>

### Example Matchers

Examples are not limited to default settings.
You can specify your own defaults for string matching, null handling, and property-specific settings by using the `ExampleMatcher`, as shown in the following example:

Example 4. Example matcher with customized matching

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

<a id="mongodb-repositories-query-methods--query-by-example.fluent"></a>
<a id="mongodb-repositories-query-methods--fluent-api"></a>

### Fluent API

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

Example 5. Use the fluent API to get a projected `Page`, ordered by `lastname`

```java
Page<CustomerProjection> page = repository.findBy(example,
    q -> q.as(CustomerProjection.class)
          .page(PageRequest.of(0, 20, Sort.by("lastname")))
);
```

Example 6. Use the fluent API to get the last of potentially many results, ordered by `lastname`

```java
Optional<Customer> match = repository.findBy(example,
    q -> q.sortBy(Sort.by("lastname").descending())
          .first()
);
```

<a id="mongodb-repositories-query-methods--query-by-example.running"></a>
<a id="mongodb-repositories-query-methods--running-an-example"></a>

### Running an Example

The following example shows how to query by example when using a repository (of `Person` objects, in this case):

Example 7. Query by Example using a repository

```java
public interface PersonRepository extends QueryByExampleExecutor<Person> {
}
public class PersonService {
@Autowired PersonRepository personRepository;
public List<Person> findPeople(Person probe) {return personRepository.findAll(Example.of(probe));}}
```

<a id="mongodb-repositories-query-methods--repositories.scrolling"></a>
<a id="mongodb-repositories-query-methods--scrolling"></a>

## Scrolling

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

<a id="mongodb-repositories-query-methods--repositories.scrolling.offset"></a>
<a id="mongodb-repositories-query-methods--scrolling-using-offset"></a>

### Scrolling using Offset

Offset scrolling uses similar to pagination, an Offset counter to skip a number of results and let the data source only return results beginning at the given Offset.
This simple mechanism avoids large results being sent to the client application.
However, most databases require materializing the full query result before your server can return the results.

Example 8. Using `OffsetScrollPosition` with Repository Query Methods

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

<a id="mongodb-repositories-query-methods--repositories.scrolling.keyset"></a>
<a id="mongodb-repositories-query-methods--scrolling-using-keyset-filtering"></a>

### Scrolling using Keyset-Filtering

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

<a id="mongodb-repositories-query-methods--mongodb.repositories.queries.sort"></a>
<a id="mongodb-repositories-query-methods--sorting-results"></a>

## Sorting Results

MongoDB repositories allow various approaches to define sorting order.
Let’s take a look at the following example:

Sorting Query Results

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    List<Person> findByFirstnameSortByAgeDesc(String firstname); (1)

    List<Person> findByFirstname(String firstname, Sort sort);   (2)

    @Query(sort = "{ age : -1 }")
    List<Person> findByFirstname(String firstname);              (3)

    @Query(sort = "{ age : -1 }")
    List<Person> findByLastname(String lastname, Sort sort);     (4)
}
```

**1**

Static sorting derived from method name. `SortByAgeDesc` results in `{ age : -1 }` for the sort parameter.

**2**

Dynamic sorting using a method argument.
`Sort.by(DESC, "age")` creates `{ age : -1 }` for the sort parameter.

**3**

Static sorting via `Query` annotation.
Sort parameter applied as stated in the `sort` attribute.

**4**

Default sorting via `Query` annotation combined with dynamic one via a method argument. `Sort.unsorted()`
results in `{ age : -1 }`.
Using `Sort.by(ASC, "age")` overrides the defaults and creates `{ age : 1 }`.
`Sort.by
(ASC, "firstname")` alters the default and results in `{ age : -1, firstname : 1 }`.

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    Flux<Person> findByFirstnameSortByAgeDesc(String firstname);

    Flux<Person> findByFirstname(String firstname, Sort sort);

    @Query(sort = "{ age : -1 }")
    Flux<Person> findByFirstname(String firstname);

    @Query(sort = "{ age : -1 }")
    Flux<Person> findByLastname(String lastname, Sort sort);
}
```

<a id="mongodb-repositories-query-methods--mongodb.repositories.index-hint"></a>
<a id="mongodb-repositories-query-methods--index-hints"></a>

> [!NOTE]
> ## Index Hints

The `@Hint` annotation allows to override MongoDB’s default index selection and forces the database to use the specified index instead.

Example 9. Example of index hints

```java
@Hint("lastname-idx")                                          (1)
List<Person> findByLastname(String lastname);

@Query(value = "{ 'firstname' : ?0 }", hint = "firstname-idx") (2)
List<Person> findByFirstname(String firstname);
```

**1**

Use the index with name `lastname-idx`.

**2**

The `@Query` annotation defines the `hint` alias which is equivalent to adding the `@Hint` annotation.

For more information about index creation please refer to the [Collection Management](#mongodb-template-collection-management) section.

<a id="mongodb-repositories-query-methods--mongo.repositories.collation"></a>
<a id="mongodb-repositories-query-methods--collation-support"></a>

## Collation Support

Next to the [general Collation Support](https://docs.spring.io/spring-data/mongodb/reference/mongodb/collation.html) repositories allow to define the collation for various operations.

```java
public interface PersonRepository extends MongoRepository<Person, String> {

  @Query(collation = "en_US")  (1)
  List<Person> findByFirstname(String firstname);

  @Query(collation = "{ 'locale' : 'en_US' }") (2)
  List<Person> findPersonByFirstname(String firstname);

  @Query(collation = "?1") (3)
  List<Person> findByFirstname(String firstname, Object collation);

  @Query(collation = "{ 'locale' : '?1' }") (4)
  List<Person> findByFirstname(String firstname, String collation);

  List<Person> findByFirstname(String firstname, Collation collation); (5)

  @Query(collation = "{ 'locale' : 'en_US' }")
  List<Person> findByFirstname(String firstname, @Nullable Collation collation); (6)
}
```

| **1** | Static collation definition resulting in `{ 'locale' : 'en_US' }`. |
| --- | --- |
| **2** | Static collation definition resulting in `{ 'locale' : 'en_US' }`. |
| **3** | Dynamic collation depending on 2nd method argument. Allowed types include `String` (eg. 'en\_US'), `Locacle` (eg. Locacle.US) and `Document` (eg. new Document("locale", "en\_US")) |
| **4** | Dynamic collation depending on 2nd method argument. |
| **5** | Apply the `Collation` method parameter to the query. |
| **6** | The `Collation` method parameter overrides the default `collation` from `@Query` if not null. |

> [!NOTE]
> In case you enabled the automatic index creation for repository finder methods a potential static collation definition, as shown in (1) and (2), will be included when creating the index.

> [!TIP]
> The most specific `Collation` outrules potentially defined others. Which means Method argument over query method annotation over domain type annotation.

To streamline usage of collation attributes throughout the codebase it is also possible to use the `@Collation` annotation, which serves as a meta annotation for the ones mentioned above.
The same rules and locations apply, plus, direct usage of `@Collation` supersedes any collation values defined on `@Query` and other annotations.
Which means, if a collation is declared via `@Query` and additionally via `@Collation`, then the one from `@Collation` is picked.

Example 10. Using `@Collation`

```java
@Collation("en_US") (1)
class Game {
  // ...
}

interface GameRepository extends Repository<Game, String> {

  @Collation("en_GB")  (2)
  List<Game> findByTitle(String title);

  @Collation("de_AT")  (3)
  @Query(collation="en_GB")
  List<Game> findByDescriptionContaining(String keyword);
}
```

| **1** | Instead of `@Document(collation=…)`. |
| --- | --- |
| **2** | Instead of `@Query(collation=…)`. |
| **3** | Favors `@Collation` over meta usage. |

<a id="mongodb-repositories-query-methods--_read_preferences"></a>
<a id="mongodb-repositories-query-methods--read-preferences"></a>

## Read Preferences

The `@ReadPreference` annotation allows you to configure MongoDB’s ReadPreferences.

Example 11. Example of read preferences

```java
@ReadPreference("primaryPreferred") (1)
public interface PersonRepository extends CrudRepository<Person, String> {

    @ReadPreference("secondaryPreferred") (2)
    List<Person> findWithReadPreferenceAnnotationByLastname(String lastname);

    @Query(readPreference = "nearest") (3)
    List<Person> findWithReadPreferenceAtTagByFirstname(String firstname);

    List<Person> findWithReadPreferenceAtTagByFirstname(String firstname); (4)
```

**1**

Configure read preference for all repository operations (including inherited, non custom implementation ones) that do not have a query-level definition. Therefore, in this case the read preference mode will be `primaryPreferred`

**2**

Use the read preference mode defined in annotation `ReadPreference`, in this case secondaryPreferred

**3**

The `@Query` annotation defines the `read preference mode` alias which is equivalent to adding the `@ReadPreference` annotation.

**4**

This query will use the read preference mode defined in the repository.

> [!TIP]
> The `MongoOperations` and `Query` API offer more fine grained control for `ReadPreference`.

---

<a id="mongodb-repositories-vector-search"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/repositories/vector-search.html -->

<!-- page_index: 45 -->

# Vector Search

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-repositories-vector-search--page-title"></a>
<a id="mongodb-repositories-vector-search--vector-search"></a>

# Vector Search

With the rise of Generative AI, Vector databases have gained strong traction in the world of databases.
These databases enable efficient storage and querying of high-dimensional vectors, making them well-suited for tasks such as semantic search, recommendation systems, and natural language understanding.

Vector search is a technique that retrieves semantically similar data by comparing vector representations (also known as embeddings) rather than relying on traditional exact-match queries.
This approach enables intelligent, context-aware applications that go beyond keyword-based retrieval.

In the context of Spring Data, vector search opens new possibilities for building intelligent, context-aware applications, particularly in domains like natural language processing, recommendation systems, and generative AI.
By modelling vector-based querying using familiar repository abstractions, Spring Data allows developers to seamlessly integrate similarity-based vector-capable databases with the simplicity and consistency of the Spring Data programming model.

To use Vector Search with MongoDB, you need a MongoDB Atlas instance that is either running in the cloud or by using [Docker](https://www.mongodb.com/docs/atlas/cli/current/atlas-cli-deploy-docker/).

<a id="mongodb-repositories-vector-search--vector-search.model"></a>
<a id="mongodb-repositories-vector-search--vector-model"></a>

## Vector Model

To support vector search in a type-safe and idiomatic way, Spring Data introduces the following core abstractions:

- [`Vector`](#mongodb-repositories-vector-search--vector-search.model.vector)
- [`SearchResults<T>` and `SearchResult<T>`](#mongodb-repositories-vector-search--vector-search.model.search-result)
- [`Score`, `Similarity` and Scoring Functions](#mongodb-repositories-vector-search--vector-search.model.scoring)

<a id="mongodb-repositories-vector-search--vector-search.model.vector"></a>
<a id="mongodb-repositories-vector-search--vector"></a>

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

```java
class Comment {

  @Id String id;
  String country;
  String comment;

  Vector embedding;

  // getters, setters, …
}
```

> [!NOTE]
> Associating a vector with a domain object results in the vector being loaded and stored as part of the entity lifecycle, which may introduce additional overhead on retrieval and persistence operations.

<a id="mongodb-repositories-vector-search--vector-search.model.search-result"></a>
<a id="mongodb-repositories-vector-search--search-results"></a>

### Search Results

The `SearchResult<T>` type encapsulates the results of a vector similarity query.
It includes both the matched domain object and a relevance score that indicates how closely it matches the query vector.
This abstraction provides a structured way to handle result ranking and enables developers to easily work with both the data and its contextual relevance.

Example 1. Using `SearchResult<T>` in a Repository Search Method

```java
interface CommentRepository extends Repository<Comment, String> {

  @VectorSearch(indexName = "my-index", numCandidates="#{#limit.max() * 20}")
  SearchResults<Comment> searchByCountryAndEmbeddingNear(String country, Vector vector, Score score,
    Limit limit);

  @VectorSearch(indexName = "my-index", limit="10", numCandidates="200")
  SearchResults<Comment> searchByCountryAndEmbeddingWithin(String country, Vector embedding,
      Score score);

}

SearchResults<Comment> results = repository.searchByCountryAndEmbeddingNear("en", Vector.of(…), Score.of(0.9), Limit.of(10));
```

> [!TIP]
> The MongoDB [vector search aggregation](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-stage/) stage defines a set of required arguments and restrictions.
> Please make sure to follow the guidelines and make sure to provide required arguments like `limit`.

In this example, the `searchByCountryAndEmbeddingNear` method returns a `SearchResults<Comment>` object, which contains a list of `SearchResult<Comment>` instances.
Each result includes the matched `Comment` entity and its relevance score.

Relevance score is a numerical value that indicates how closely the matched vector aligns with the query vector.
Depending on whether a score represents distance or similarity a higher score can mean a closer match or a more distant one.

The scoring function used to calculate this score can vary based on the underlying database, index or input parameters.

<a id="mongodb-repositories-vector-search--vector-search.model.scoring"></a>
<a id="mongodb-repositories-vector-search--score-similarity-and-scoring-functions"></a>

### Score, Similarity, and Scoring Functions

The `Score` type holds a numerical value indicating the relevance of a search result.
It can be used to rank results based on their similarity to the query vector.
The `Score` type is typically a floating-point number, and its interpretation (higher is better or lower is better) depends on the specific similarity function used.
Scores are a by-product of vector search and are not required for a successful search operation.
Score values are not part of a domain model and therefore represented best as out-of-band data.

Generally, a Score is computed by a `ScoringFunction`.
The actual scoring function used to calculate this score can depends on the underlying database and can be obtained from a search index or input parameters.

Spring Data support declares constants for commonly used functions such as:

Euclidean Distance
:   Calculates the straight-line distance in n-dimensional space involving the square root of the sum of squared differences.

Cosine Similarity
:   Measures the angle between two vectors by calculating the Dot product first and then normalizing its result by dividing by the product of their lengths.

Dot Product
:   Computes the sum of element-wise multiplications.

The choice of similarity function can impact both the performance and semantics of the search and is often determined by the underlying database or index being used.
Spring Data adopts to the database’s native scoring function capabilities and whether the score can be used to limit results.

MongoDB reports the score directly as similarity value.
The scoring function must be specified in the index and therefore, Vector search methods do not consider the `Score.scoringFunction`.
The scoring function defaults to `ScoringFunction.unspecified()` as there is no information inside of search results how the score has been computed.

Example 2. Using `Score` and `Similarity` in a Repository Search Methods

```java
interface CommentRepository extends Repository<Comment, String> {

  @VectorSearch(…)
  SearchResults<Comment> searchTop10ByEmbeddingNear(Vector vector, Score similarity);

  @VectorSearch(…)
  SearchResults<Comment> searchTop10ByEmbeddingNear(Vector vector, Similarity similarity);

  @VectorSearch(…)
  SearchResults<Comment> searchTop10ByEmbeddingNear(Vector vector, Range<Similarity> range);
}

repository.searchByEmbeddingNear(Vector.of(…), Score.of(0.9));                (1)

repository.searchByEmbeddingNear(Vector.of(…), Similarity.of(0.9));           (2)

repository.searchByEmbeddingNear(Vector.of(…), Similarity.between(0.5, 1));   (3)
```

| **1** | Run a search and return results with a similarity of `0.9` or greater. |
| --- | --- |
| **2** | Return results with a similarity of `0.9` or greater. |
| **3** | Return results with a similarity of between `0.5` and `1.0` or greater. |

<a id="mongodb-repositories-vector-search--vector-search.methods"></a>
<a id="mongodb-repositories-vector-search--vector-search-methods"></a>

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

<a id="mongodb-repositories-vector-search--vector-search.method.derivation"></a>
<a id="mongodb-repositories-vector-search--derived-search-methods"></a>

### Derived Search Methods

A derived search method uses the name of the method to derive the query.
Vector Search supports the following keywords to run a Vector search when declaring a search method:

| Logical keyword | Keyword expressions |
| --- | --- |
| `NEAR` | `Near`, `IsNear` |
| `WITHIN` | `Within`, `IsWithin` |

MongoDB Search methods must use the `@VectorSearch` annotation to define the index name for the [`$vectorSearch`](https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/vectorSearch/) aggregation stage.

Example 3. Using `Near` and `Within` Keywords in Repository Search Methods

```java
interface CommentRepository extends Repository<Comment, String> {

  @VectorSearch(indexName = "my-index", numCandidates="200")
  SearchResults<Comment> searchTop10ByEmbeddingNear(Vector vector, Score score);

  @VectorSearch(indexName = "my-index", numCandidates="200")
  SearchResults<Comment> searchTop10ByEmbeddingWithin(Vector vector, Range<Similarity> range);

  @VectorSearch(indexName = "my-index", numCandidates="200")
  SearchResults<Comment> searchTop10ByCountryAndEmbeddingWithin(String country, Vector vector, Range<Similarity> range);
}
```

Derived Search Methods can define domain model attributes to create the pre-filter for indexed fields.

Derived search methods are typically easier to read and maintain, as they rely on the method name to express the query intent.
However, a derived search method requires either to declare a `Score`, `Range<Score>` or `ScoreFunction` as second argument to the `Near`/`Within` keyword to limit search results by their score.

<a id="mongodb-repositories-vector-search--vector-search.method.string"></a>
<a id="mongodb-repositories-vector-search--annotated-search-methods"></a>

### Annotated Search Methods

Annotated methods provide full control over the query semantics and parameters.
Unlike derived methods, they do not rely on method name conventions.

Annotated search methods use the `@VectorSearch` annotation to define parameters for the [`$vectorSearch`](https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/vectorSearch/) aggregation stage.

Example 4. Using `@VectorSearch` Search Methods

```java
interface CommentRepository extends Repository<Comment, String> {

  @VectorSearch(indexName = "cos-index", filter = "{country: ?0}", limit="100", numCandidates="2000")
  SearchResults<Comment> searchAnnotatedByCountryAndEmbeddingWithin(String country, Vector embedding,
      Score distance);

  @VectorSearch(indexName = "my-index", filter = "{country: ?0}", limit="?3", numCandidates = "#{#limit * 20}",
				searchType = VectorSearchOperation.SearchType.ANN)
  List<Comment> findAnnotatedByCountryAndEmbeddingWithin(String country, Vector embedding, Score distance, int limit);
}
```

Annotated Search Methods can define `filter` for pre-filter usage.

`filter`, `limit`, and `numCandidates` support [Value Expressions](#mongodb-value-expressions) allowing references to search method arguments.

With more control over the actual query, Spring Data can make fewer assumptions about the query and its parameters.
For example, `Similarity` normalization uses the native score function within the query to normalize the given similarity into a score predicate value and vice versa.
If an annotated query does not define e.g. the score, then the score value in the returned `SearchResult<T>` will be zero.

<a id="mongodb-repositories-vector-search--vector-search.method.sorting"></a>
<a id="mongodb-repositories-vector-search--sorting"></a>

### Sorting

By default, search results are ordered according to their score.
You can override sorting by using the `Sort` parameter:

Example 5. Using `Sort` in Repository Search Methods

```java
interface CommentRepository extends Repository<Comment, String> {

  SearchResults<Comment> searchByEmbeddingNearOrderByCountry(Vector vector, Score score);

  SearchResults<Comment> searchByEmbeddingWithin(Vector vector, Score score, Sort sort);
}
```

Please note that custom sorting does not allow expressing the score as a sorting criteria.
You can only refer to domain properties.

---

<a id="mongodb-repositories-modifying-methods"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/repositories/modifying-methods.html -->

<!-- page_index: 46 -->

# MongoDB-specific Data Manipulation Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-repositories-modifying-methods--page-title"></a>
<a id="mongodb-repositories-modifying-methods--mongodb-specific-data-manipulation-methods"></a>

# MongoDB-specific Data Manipulation Methods

Next to the [query methods](#mongodb-repositories-query-methods) it is possible to update data with specialized methods.

<a id="mongodb-repositories-modifying-methods--mongodb.repositories.queries.update"></a>
<a id="mongodb-repositories-modifying-methods--update-methods"></a>

## Update Methods

You can also use the keywords in the preceding table to create queries that identify matching documents for running updates on them.
The actual update action is defined by the `@Update` annotation on the method itself, as the following listing shows.
Note that the naming schema for derived queries starts with `find`.
Using `update` (as in `updateAllByLastname(…)`) is allowed only in combination with `@Query`.

The update is applied to **all** matching documents and it is **not** possible to limit the scope by passing in a `Page` or by using any of the [limiting keywords](#mongodb-repositories-modifying-methods--repositories.limit-query-result).
The return type can be either `void` or a *numeric* type, such as `long`, to hold the number of modified documents.

Example 1. Update Methods

```java
public interface PersonRepository extends CrudRepository<Person, String> {

    @Update("{ '$inc' : { 'visits' : 1 } }")
    long findAndIncrementVisitsByLastname(String lastname); (1)

    @Update("{ '$inc' : { 'visits' : ?1 } }")
    void findAndIncrementVisitsByLastname(String lastname, int increment); (2)

    @Update("{ '$inc' : { 'visits' : ?#{[1]} } }")
    long findAndIncrementVisitsUsingSpELByLastname(String lastname, int increment); (3)

    @Update(pipeline = {"{ '$set' : { 'visits' : { '$add' : [ '$visits', ?1 ] } } }"})
    void findAndIncrementVisitsViaPipelineByLastname(String lastname, int increment); (4)

    @Update("{ '$push' : { 'shippingAddresses' : ?1 } }")
    long findAndPushShippingAddressByEmail(String email, Address address); (5)

    @Query("{ 'lastname' : ?0 }")
    @Update("{ '$inc' : { 'visits' : ?1 } }")
    void updateAllByLastname(String lastname, int increment); (6)
}
```

**1**

The filter query for the update is derived from the method name.
The update is “as is” and does not bind any parameters.

**2**

The actual increment value is defined by the `increment` method argument that is bound to the `?1` placeholder.

**3**

Use the Spring Expression Language (SpEL) for parameter binding.

**4**

Use the `pipeline` attribute to issue [aggregation pipeline updates](#mongodb-template-crud-operations--mongo-template.aggregation-update).

**5**

The update may contain complex objects.

**6**

Combine a [string based query](#mongodb-repositories-repositories--mongodb.repositories.queries.json-based) with an update.

> [!WARNING]
> Repository updates do not emit persistence nor mapping lifecycle events.

<a id="mongodb-repositories-modifying-methods--mongodb.repositories.queries.delete"></a>
<a id="mongodb-repositories-modifying-methods--delete-methods"></a>

## Delete Methods

The keywords in the preceding table can be used in conjunction with `delete…By` or `remove…By` to create queries that delete matching documents.

`Delete…By` Query

- Imperative
- Reactive

```java
public interface PersonRepository extends MongoRepository<Person, String> {

    List <Person> deleteByLastname(String lastname);      (1)

    Long deletePersonByLastname(String lastname);         (2)

    @Nullable
    Person deleteSingleByLastname(String lastname);       (3)

    Optional<Person> deleteByBirthdate(Date birthdate);   (4)
}
```

**1**

Using a return type of `List` retrieves and returns all matching documents before actually deleting them.

**2**

A numeric return type directly removes the matching documents, returning the total number of documents removed.

**3**

A single domain type result retrieves and removes the first matching document.

**4**

Same as in 3 but wrapped in an `Optional` type.

```java
public interface PersonRepository extends ReactiveMongoRepository<Person, String> {

    Flux<Person> deleteByLastname(String lastname);      (1)

    Mono<Long> deletePersonByLastname(String lastname);         (2)

    Mono<Person> deleteSingleByLastname(String lastname);       (3)
}
```

**1**

Using a return type of `Flux` retrieves and returns all matching documents before actually deleting them.

**2**

A numeric return type directly removes the matching documents, returning the total number of documents removed.

**3**

A single domain type result retrieves and removes the first matching document.

---

<a id="repositories-projections"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/projections.html -->

<!-- page_index: 47 -->

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

<a id="repositories-custom-implementations"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/custom-implementations.html -->

<!-- page_index: 48 -->

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
@EnableMongoRepositories(repositoryImplementationPostfix = "MyPostfix")
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
@EnableMongoRepositories(repositoryBaseClass = MyRepositoryImpl.class)
class ApplicationConfiguration { … }
```

```xml
<repositories base-package="com.acme.repository"
     base-class="….MyRepositoryImpl" />
```

<a id="repositories-custom-implementations--repositories.customize-repository-factory"></a>
<a id="repositories-custom-implementations--customizing-the-repository-factory"></a>

## Customizing the Repository Factory

Customizing the [repository factory](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFactorySupport.html) through [`RepositoryFactoryCustomizer`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFactoryCustomizer.html) provides direct access to components involved with repository instance creation.
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

The most powerful approach to customize repository creation is to provide a custom repository factory bean, typically a subclass of [`RepositoryFactorySupport`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFactorySupport.html), [`TransactionalRepositoryFactoryBeanSupport`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/TransactionalRepositoryFactoryBeanSupport.html) or the store-specific repository factory bean.

Customizing the repository factory bean allows you to change repository creation entirely with full access to the underlying repository factory.

Note that this approach requires the most effort and is typically only needed when you want to change core aspects of repository creation.
Also, you need to take into consideration repository metadata derivation that is used to identify query methods, base implementation methods and custom implementations.
The following summary outlines the key aspects:

- `repositoryBaseClass`: The repository base class defines which methods are implemented by the base class and which methods require additional handling through aspects or custom implementations.
- `repositoryFragmentsContributor`: A [`RepositoryFragmentsContributor`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFragmentsContributor.html) allows contributions to repository composition after all standard fragments have been collected.
  Store modules use this mechanism to add features such as Querydsl or Query-by-Example support.
  It also serves as an SPI for third-party extensions.
- `exposeMetadata`: Controls whether [invocation metadata](#repositories-custom-implementations--expose-repository-metadata) is available through `RepositoryMethodContext.getContext()`.

---

<a id="repositories-core-domain-events"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/core-domain-events.html -->

<!-- page_index: 49 -->

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

<a id="repositories-null-handling"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/null-handling.html -->

<!-- page_index: 50 -->

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

<a id="mongodb-repositories-cdi-integration"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/mongodb/repositories/cdi-integration.html -->

<!-- page_index: 51 -->

# CDI Integration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="mongodb-repositories-cdi-integration--page-title"></a>
<a id="mongodb-repositories-cdi-integration--cdi-integration"></a>

# CDI Integration

Instances of the repository interfaces are usually created by a container, and Spring is the most natural choice when working with Spring Data.
As of version 1.3.0, Spring Data MongoDB ships with a custom CDI extension that lets you use the repository abstraction in CDI environments.
The extension is part of the JAR.
To activate it, drop the Spring Data MongoDB JAR into your classpath.
You can now set up the infrastructure by implementing a CDI Producer for the `MongoTemplate`, as the following example shows:

```java
class MongoTemplateProducer {
@Produces @ApplicationScoped public MongoOperations createMongoTemplate() {
MongoDatabaseFactory factory = new SimpleMongoClientDatabaseFactory(MongoClients.create(), "database"); return new MongoTemplate(factory);}}
```

The Spring Data MongoDB CDI extension picks up the `MongoTemplate` available as a CDI bean and creates a proxy for a Spring Data repository whenever a bean of a repository type is requested by the container.
Thus, obtaining an instance of a Spring Data repository is a matter of declaring an `@Inject`-ed property, as the following example shows:

```java
class RepositoryClient {
@Inject PersonRepository repository;
public void businessMethod() {List<Person> people = repository.findAll();}}
```

---

<a id="repositories-query-keywords-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/query-keywords-reference.html -->

<!-- page_index: 52 -->

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

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/repositories/query-return-types-reference.html -->

<!-- page_index: 53 -->

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

<a id="observability-observability"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/observability/observability.html -->

<!-- page_index: 54 -->

# Observability

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="observability-observability--page-title"></a>
<a id="observability-observability--observability"></a>

# Observability

> [!NOTE]
> MongoDB Java Driver 5.7+ comes with observability directly built in.
> We recommend switching to the driver native `ObservabilitySettings`, which can be configured as outlined below:
>
> ```java
> @Bean MongoClientSettingsBuilderCustomizer mongoDbObservabilitySettings(ObservationRegistry registry) {return (clientSettingsBuilder) -> {clientSettingsBuilder.observabilitySettings(ObservabilitySettings.micrometerBuilder() .observationRegistry(observationRegistry) .build()); };}
> ```
>
> In the light of driver native observability support, the types within the Spring Data provided *org.springframework.data.mongodb.observability* package will not see further development and are subject to deprecation/removal in subsequent releases.

To use Spring Data MongoDB’s flavor of Observability you must:

1. opt into Spring Data MongoDB’s configuration settings by customizing `MongoClientSettings` through either your `@SpringBootApplication` class or one of your configuration classes.

   Example 1. Registering MongoDB Micrometer customizer setup


```java
@Bean
MongoClientSettingsBuilderCustomizer mongoMetricsSynchronousContextProvider(ObservationRegistry registry) {
    return (clientSettingsBuilder) -> {
        clientSettingsBuilder.contextProvider(ContextProviderFactory.create(registry))
                             .addCommandListener(new MongoObservationCommandListener(registry));
    };
}
```

2. Your project must include **Spring Boot Actuator**.
3. Disable Spring Boot’s autoconfigured MongoDB command listener and enable tracing manually by adding the following properties to your `application.properties`

   Example 2. Custom settings to apply


```none
# Disable Spring Boot's autoconfigured tracing
management.metrics.mongo.command.enabled=false
# Enable it manually
management.tracing.enabled=true
```

   Be sure to add any other relevant settings needed to configure the tracer you are using based upon Micrometer’s reference documentation.

This should do it! You are now running with Spring Data MongoDB’s usage of Spring Observability’s `Observation` API.
See also [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/database/#mongodb) for further reference.

---

<a id="observability-conventions"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/observability/conventions.html -->

<!-- page_index: 55 -->

<a id="observability-conventions--page-title"></a>
<a id="observability-conventions--conventions"></a>

# Conventions

Below you can find a list of all `GlobalObservationConvention` and `ObservationConvention` declared by this project.

| ObservationConvention Class Name | Applicable ObservationContext Class Name |
| --- | --- |
| `org.springframework.data.mongodb.observability.DefaultMongoHandlerObservationConvention` | `MongoHandlerContext` |
| `org.springframework.data.mongodb.observability.MongoHandlerObservationConvention` | `MongoHandlerContext` |

---

<a id="observability-metrics"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/observability/metrics.html -->

<!-- page_index: 56 -->

# Metrics

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="observability-metrics--page-title"></a>
<a id="observability-metrics--metrics"></a>

# Metrics

Below you can find a list of all metrics declared by this project.

<a id="observability-metrics--observability-metrics-mongodb-command-observation"></a>
<a id="observability-metrics--mongodb-command-observation"></a>

## Mongodb Command Observation

> Timer created around a MongoDB command execution.

**Metric name** `spring.data.mongodb.command`. **Type** `timer`.

**Metric name** `spring.data.mongodb.command.active`. **Type** `long task timer`.

> [!IMPORTANT]
> KeyValues that are added after starting the Observation might be missing from the \*.active metrics.

> [!IMPORTANT]
> Micrometer internally uses `nanoseconds` for the baseunit. However, each backend determines the actual baseunit. (i.e. Prometheus uses seconds)

Fully qualified name of the enclosing class `org.springframework.data.mongodb.observability.MongoObservation`.

| Name | Description |
| --- | --- |
| `db.mongodb.collection` *(required)* | MongoDB collection name. |
| `db.name` *(required)* | MongoDB database name. |
| `db.operation` *(required)* | MongoDB command value. |
| `db.system` *(required)* | MongoDB database system. |
| `net.peer.name` *(required)* | Name of the database host. |
| `net.peer.port` *(required)* | Logical remote port number. |
| `net.sock.peer.addr` *(required)* | Mongo peer address. |
| `net.sock.peer.port` *(required)* | Mongo peer port. |
| `net.transport` *(required)* | Network transport. |
| `spring.data.mongodb.cluster_id` *(required)* | MongoDB cluster identifier. |

---

<a id="observability-spans"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/observability/spans.html -->

<!-- page_index: 57 -->

# Spans

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="observability-spans--page-title"></a>
<a id="observability-spans--spans"></a>

# Spans

Below you can find a list of all spans declared by this project.

<a id="observability-spans--observability-spans-mongodb-command-observation"></a>
<a id="observability-spans--mongodb-command-observation-span"></a>

## Mongodb Command Observation Span

> Timer created around a MongoDB command execution.

**Span name** `spring.data.mongodb.command`.

Fully qualified name of the enclosing class `org.springframework.data.mongodb.observability.MongoObservation`.

| Name | Description |
| --- | --- |
| `db.mongodb.collection` *(required)* | MongoDB collection name. |
| `db.name` *(required)* | MongoDB database name. |
| `db.operation` *(required)* | MongoDB command value. |
| `db.system` *(required)* | MongoDB database system. |
| `net.peer.name` *(required)* | Name of the database host. |
| `net.peer.port` *(required)* | Logical remote port number. |
| `net.sock.peer.addr` *(required)* | Mongo peer address. |
| `net.sock.peer.port` *(required)* | Mongo peer port. |
| `net.transport` *(required)* | Network transport. |
| `spring.data.mongodb.cluster_id` *(required)* | MongoDB cluster identifier. |

---

<a id="kotlin"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/kotlin.html -->

<!-- page_index: 58 -->

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

---

<a id="kotlin-requirements"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/kotlin/requirements.html -->

<!-- page_index: 59 -->

<a id="kotlin-requirements--page-title"></a>
<a id="kotlin-requirements--requirements"></a>

# Requirements

Spring Data supports Kotlin 1.9 and above and requires `kotlin-stdlib` and `kotlin-reflect` to be present on the classpath.
Those are provided by default if you bootstrap a Kotlin project via [start.spring.io](https://start.spring.io/#!language=kotlin&type=gradle-project).

---

<a id="kotlin-null-safety"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/kotlin/null-safety.html -->

<!-- page_index: 60 -->

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

<a id="kotlin-extensions"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/kotlin/extensions.html -->

<!-- page_index: 61 -->

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

To retrieve a list of `SWCharacter` objects in Java, you would normally write the following:

```java
Flux<SWCharacter> characters = template.query(SWCharacter.class).inTable("star-wars").all()
```

With Kotlin and the Spring Data extensions, you can instead write the following:

```kotlin
val characters = template.query<SWCharacter>().inTable("star-wars").all()
// or (both are equivalent)
val characters : Flux<SWCharacter> = template.query().inTable("star-wars").all()
```

As in Java, `characters` in Kotlin is strongly typed, but Kotlin’s clever type inference allows for shorter syntax.

<a id="kotlin-extensions--mongo.query.kotlin-support"></a>
<a id="kotlin-extensions--type-safe-queries-for-kotlin"></a>

## Type-safe Queries for Kotlin

Kotlin embraces domain-specific language creation through its language syntax and its extension system.
Spring Data MongoDB ships with a Kotlin Extension for `Criteria` using [Kotlin property references](https://kotlinlang.org/docs/reference/reflection.html#property-references) to build type-safe queries.
Queries using this extension are typically benefit from improved readability.
Most keywords on `Criteria` have a matching Kotlin extension, such as `inValues` and `regex`.

Consider the following example explaining Type-safe Queries:

```kotlin
import org.springframework.data.mongodb.core.query.*
mongoOperations.find<Book>(Query(Book::title isEqualTo "Moby-Dick")               (1))
mongoOperations.find<Book>(Query(titlePredicate = Book::title exists true))
mongoOperations.find<Book>(Query(Criteria().andOperator(Book::price gt 5,Book::price lt 10 )))
// Binary operators mongoOperations.find<BinaryMessage>(Query(BinaryMessage::payload bits { allClear(0b101) }) (2))
// Nested Properties (i.e. refer to "book.author") mongoOperations.find<Book>(Query(Book::author / Author::name regex "^H")          (3))
```

**1**

`isEqualTo()` is an infix extension function with receiver type `KProperty<T>` that returns `Criteria`.

**2**

For bitwise operators, pass a lambda argument where you call one of the methods of `Criteria.BitwiseCriteriaOperators`.

**3**

To construct nested properties, use the `/` character (overloaded operator `div`).

<a id="kotlin-extensions--mongo.update.kotlin-support"></a>
<a id="kotlin-extensions--type-safe-updates-for-kotlin"></a>

## Type-safe Updates for Kotlin

A syntax similar to [Type-safe Queries for Kotlin](#kotlin-extensions--mongo.query.kotlin-support) can be used to update documents:

```kotlin
mongoOperations.updateMulti<Book>(
  Query(Book::title isEqualTo "Moby-Dick"),
  update(Book:title, "The Whale")                        (1)
    .inc(Book::price, 100)                               (2)
    .addToSet(Book::authors, "Herman Melville")          (3)
)
```

**1**

`update()` is a factory function with receiver type `KProperty<T>` that returns `Update`.

**2**

Most methods from `Update` have a matching Kotlin extension.

**3**

Functions with `KProperty<T>` can be used as well on collections types

---

<a id="kotlin-coroutines"></a>

<!-- source_url: https://docs.spring.io/spring-data/mongodb/reference/kotlin/coroutines.html -->

<!-- page_index: 62 -->

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
