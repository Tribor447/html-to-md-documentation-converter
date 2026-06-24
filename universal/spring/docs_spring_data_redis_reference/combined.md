# Spring Data Redis

## Navigation

- Overview
  
- [Overview](#index)
    
- [Upgrading Spring Data](#commons-upgrade)
    
- [Migration Guides](#upgrading)
  
- [Redis](#redis)
    
- [Getting Started](#redis-getting-started)
    
- [Drivers](#redis-drivers)
    
- [Connection Modes](#redis-connection-modes)
    
- [RedisTemplate](#redis-template)
    
- [Redis Cache](#redis-redis-cache)
    
- [Redis Cluster](#redis-cluster)
    
- [Hash Mapping](#redis-hash-mappers)
    
- [Pub/Sub Messaging](#redis-pubsub)
      
- [Publishing (Sending a Message)](#redis-pubsub-sending)
      
- [Subscribing (Receiving a Message)](#redis-pubsub-receiving)
      
- [Annotation-driven Listener Endpoints](#redis-pubsub-annotated)
    
- [Redis Streams](#redis-redis-streams)
    
- [Scripting](#redis-scripting)
    
- [Redis Transactions](#redis-transactions)
    
- [Pipelining](#redis-pipelining)
    
- [Support Classes](#redis-support-classes)
  
- [Redis Repositories](#repositories)
    
- [Core concepts](#repositories-core-concepts)
    
- [Defining Repository Interfaces](#repositories-definition)
    
- [Creating Repository Instances](#repositories-create-instances)
    
- [Usage](#redis-redis-repositories-usage)
    
- [Object Mapping Fundamentals](#repositories-object-mapping)
    
- [Object-to-Hash Mapping](#redis-redis-repositories-mapping)
    
- [Keyspaces](#redis-redis-repositories-keyspaces)
    
- [Secondary Indexes](#redis-redis-repositories-indexes)
    
- [Time To Live](#redis-redis-repositories-expirations)
    
- [Redis-specific Query Methods](#redis-redis-repositories-queries)
    
- [Query by Example](#redis-redis-repositories-query-by-example)
    
- [Redis Repositories Running on a Cluster](#redis-redis-repositories-cluster)
    
- [Redis Repositories Anatomy](#redis-redis-repositories-anatomy)
    
- [Projections](#repositories-projections)
    
- [Custom Repository Implementations](#repositories-custom-implementations)
    
- [Publishing Events from Aggregate Roots](#repositories-core-domain-events)
    
- [Null Handling of Repository Methods](#repositories-null-handling)
    
- [CDI Integration](#redis-redis-repositories-cdi-integration)
    
- [Repository query keywords](#repositories-query-keywords-reference)
    
- [Repository query return types](#repositories-query-return-types-reference)
  
- [Observability](#observability)
  
- [Appendix](#appendix)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/index.html -->

<!-- page_index: 1 -->

# Spring Data Redis

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-data-redis"></a>

# Spring Data Redis

*Spring Data Redis provides Redis connectivity and repository support for the Redis database.
It eases development of applications with a consistent programming model that need to access Redis data sources.*

| [Redis](#redis) | Redis support and connectivity |
| --- | --- |
| [Repositories](#repositories) | Redis Repositories |
| [Observability](#observability) | Observability Integration |
| [Wiki](https://github.com/spring-projects/spring-data-commons/wiki) | What’s New, Upgrade Notes, Supported Versions, additional cross-version information. |

Costin Leau, Jennifer Hickey, Christoph Strobl, Thomas Darimont, Mark Paluch, Jay Bryant

© 2008-2026 VMware, Inc.

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

---

<a id="commons-upgrade"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/commons/upgrade.html -->

<!-- page_index: 2 -->

# Upgrading Spring Data

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commons-upgrade--page-title"></a>
<a id="commons-upgrade--upgrading-spring-data"></a>

# Upgrading Spring Data

Instructions for how to upgrade from earlier versions of Spring Data are provided on the project [wiki](https://github.com/spring-projects/spring-data-commons/wiki).
Follow the links in the [release notes section](https://github.com/spring-projects/spring-data-commons/wiki#release-notes) to find the version that you want to upgrade to.

Upgrading instructions are always the first item in the release notes. If you are more than one release behind, please make sure that you also review the release notes of the versions that you jumped.

Once you’ve decided to upgrade your application, you can find detailed information regarding specific features in the rest of the document.
You can find [migration guides](#upgrading--redis.upgrading) specific to major version migrations at the end of this document.

Spring Data’s documentation is specific to that version, so any information that you find in here will contain the most up-to-date changes that are in that version.

---

<a id="upgrading"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/upgrading.html -->

<!-- page_index: 3 -->

# Migration Guides

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="upgrading--page-title"></a>
<a id="upgrading--migration-guides"></a>

# Migration Guides

This section contains details about migration steps, deprecations, and removals.

<a id="upgrading--upgrading.2-to-3"></a>
<a id="upgrading--upgrading-from-2.x-to-3.x"></a>

## Upgrading from 2.x to 3.x

<a id="upgrading--upgrading.2-to-3.types"></a>
<a id="upgrading--re-moved-types"></a>

### Re-/moved Types

| Type | Replacement |
| --- | --- |
| o.s.d.redis.Version | o.s.d.util.Version |
| o.s.d.redis.VersionParser | - |
| o.s.d.redis.connection.RedisZSetCommands.Aggregate | o.s.d.redis.connection.zset.Aggregate |
| o.s.d.redis.connection.RedisZSetCommands.Tuple | o.s.d.redis.connection.zset.Tuple |
| o.s.d.redis.connection.RedisZSetCommands.Weights | o.s.d.redis.connection.zset.Weights |
| o.s.d.redis.connection.RedisZSetCommands.Range | o.s.d.domain.Range |
| o.s.d.redis.connection.RedisZSetCommands.Limit | o.s.d.redis.connection.Limit.java |
| o.s.d.redis.connection.jedis.JedisUtils | - |
| o.s.d.redis.connection.jedis.JedisVersionUtil | - |
| o.s.d.redis.core.convert.CustomConversions | o.s.d.convert.CustomConversions |

<a id="upgrading--changed-methods-and-types"></a>

### Changed Methods and Types

| Type | Method | Replacement |
| --- | --- | --- |
| o.s.d.redis.core.Cursor | open | - |
| o.s.d.redis.core.RedisTemplate | execute | doWithKeys |
| o.s.d.redis.stream.StreamMessageListenerContainer | isAutoAck | isAutoAcknowledge |
| o.s.d.redis.stream.StreamMessageListenerContainer | autoAck | autoAcknowledge |

| Type | Method | Replacement |
| --- | --- | --- |
| o.s.d.redis.connection.ClusterCommandExecutionFailureException | getCauses | getSuppressed |
| o.s.d.redis.connection.RedisConnection | bgWriteAof | bgReWriteAof |
| o.s.d.redis.connection.RedisConnection | slaveOf | replicaOf |
| o.s.d.redis.connection.RedisConnection | slaveOfNoOne | replicaOfNoOne |
| o.s.d.redis.connection.ReactiveClusterCommands | clusterGetSlaves | clusterGetReplicas |
| o.s.d.redis.connection.ReactiveClusterCommands | clusterGetMasterSlaveMap | clusterGetMasterReplicaMap |
| o.s.d.redis.connection.ReactiveKeyCommands | getNewName | getNewKey |
| o.s.d.redis.connection.RedisClusterNode.Flag | SLAVE | REPLICA |
| o.s.d.redis.connection.RedisClusterNode.Builder | slaveOf | replicaOf |
| o.s.d.redis.connection.RedisNode | isSlave | isReplica |
| o.s.d.redis.connection.RedisSentinelCommands | slaves | replicas |
| o.s.d.redis.connection.RedisServer | getNumberSlaves | getNumberReplicas |
| o.s.d.redis.connection.RedisServerCommands | slaveOf | replicaOf |
| o.s.d.redis.core.ClusterOperations | getSlaves | getReplicas |
| o.s.d.redis.core.RedisOperations | slaveOf | replicaOf |

| Type | Method | Replacement |
| --- | --- | --- |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoAdd | add |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoDist | distance |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoHash | hash |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoPos | position |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoRadius | radius |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoRadiusByMember | radius |
| o.s.d.redis.core.GeoOperations & BoundGeoOperations | geoRemove | remove |

| Type | Method | Replacement |
| --- | --- | --- |
| o.s.d.redis.cache.RedisCacheConfiguration | prefixKeysWith | prefixCacheNameWith |
| o.s.d.redis.cache.RedisCacheConfiguration | getKeyPrefix | getKeyPrefixFor |

<a id="upgrading--upgrading.2-to-3.jedis"></a>
<a id="upgrading--jedis"></a>

### Jedis

Please read the Jedis [upgrading guide](https://github.com/redis/jedis/blob/v4.0.0/docs/3to4.md) which covers important driver changes.

| Type | Method | Replacement |
| --- | --- | --- |
| o.s.d.redis.connection.jedis.JedisConnectionFactory | getShardInfo | *can be obtained via JedisClientConfiguration* |
| o.s.d.redis.connection.jedis.JedisConnectionFactory | setShardInfo | *can be set via JedisClientConfiguration* |
| o.s.d.redis.connection.jedis.JedisConnectionFactory | createCluster | *now requires a `Connection` instead of `Jedis` instance* |
| o.s.d.redis.connection.jedis.JedisConverters |  | has package visibility now |
| o.s.d.redis.connection.jedis.JedisConverters | tuplesToTuples | - |
| o.s.d.redis.connection.jedis.JedisConverters | tuplesToTuples | - |
| o.s.d.redis.connection.jedis.JedisConverters | stringListToByteList | - |
| o.s.d.redis.connection.jedis.JedisConverters | stringSetToByteSet | - |
| o.s.d.redis.connection.jedis.JedisConverters | stringMapToByteMap | - |
| o.s.d.redis.connection.jedis.JedisConverters | tupleSetToTupleSet | - |
| o.s.d.redis.connection.jedis.JedisConverters | toTupleSet | - |
| o.s.d.redis.connection.jedis.JedisConverters | toDataAccessException | o.s.d.redis.connection.jedis.JedisExceptionConverter#convert |

<a id="upgrading--upgrading.2-to-3.jedis.transactions"></a>
<a id="upgrading--transactions-pipelining"></a>

### Transactions / Pipelining

Pipelining and Transactions are now mutually exclusive.
The usage of server or connection commands in pipeline/transactions mode is no longer possible.

<a id="upgrading--upgrading.2-to-3.lettuce"></a>
<a id="upgrading--lettuce"></a>

### Lettuce

<a id="upgrading--upgrading.2-to-3.lettuce.pool"></a>
<a id="upgrading--lettuce-pool"></a>

#### Lettuce Pool

`LettucePool` and its implementation `DefaultLettucePool` have been removed without replacement.
Please refer to the [driver documentation](https://lettuce.io/core/release/reference/index.html#_connection_pooling) for driver native pooling capabilities.
Methods accepting pooling parameters have been updated.
This effects methods on `LettuceConnectionFactory` and `LettuceConnection`.

<a id="upgrading--upgrading.2-to-3.lettuce.authentication"></a>
<a id="upgrading--lettuce-authentication"></a>

#### Lettuce Authentication

`AuthenticatingRedisClient` has been removed without replacement.
Please refer to the [driver documentation](https://lettuce.io/core/release/reference/index.html#basic.redisuri) for `RedisURI` to set authentication data.

---

<a id="redis"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis.html -->

<!-- page_index: 4 -->

# Redis

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis--page-title"></a>
<a id="redis--redis"></a>

# Redis

One of the key-value stores supported by Spring Data is [Redis](https://redis.io).
To quote the Redis project home page:

> Redis is an advanced key-value store.
> It is similar to memcached but the dataset is not volatile, and values can be strings, exactly like in memcached, but also lists, sets, and ordered sets.
> All this data types can be manipulated with atomic operations to push/pop elements, add/remove elements, perform server side union, intersection, difference between sets, and so forth.
> Redis supports different kind of sorting abilities.

Spring Data Redis provides easy configuration and access to Redis from Spring applications.
It offers both low-level and high-level abstractions for interacting with the store, freeing the user from infrastructural concerns.

Spring Data support for Redis contains a wide range of features:

- [`RedisTemplate` and `ReactiveRedisTemplate` helper class](#redis-template) that increases productivity when performing common Redis operations.
  Includes integrated serialization between objects and values.
- Exception translation into Spring’s portable Data Access Exception hierarchy.
- Automatic implementation of [Repository interfaces](#repositories), including support for custom query methods.
- Feature-rich [Object Mapping](#redis-redis-repositories-mapping) integrated with Spring’s Conversion Service.
- Annotation-based mapping metadata that is extensible to support other metadata formats.
- [Transactions](#redis-transactions) and [Pipelining](#redis-pipelining).
- [Redis Cache](#redis-redis-cache) integration through Spring’s Cache abstraction.
- [Redis Pub/Sub Messaging](#redis-pubsub) and [Redis Stream](#redis-redis-streams) Listeners.
- [Redis Collection Implementations](#redis-support-classes) for Java such as `RedisList` or `RedisSet`.

<a id="redis--_why_spring_data_redis"></a>
<a id="redis--why-spring-data-redis"></a>

## Why Spring Data Redis?

The Spring Framework is the leading full-stack Java/JEE application framework.
It provides a lightweight container and a non-invasive programming model enabled by the use of dependency injection, AOP, and portable service abstractions.

[NoSQL](https://en.wikipedia.org/wiki/NoSQL) storage systems provide an alternative to classical RDBMS for horizontal scalability and speed.
In terms of implementation, key-value stores represent one of the largest (and oldest) members in the NoSQL space.

The Spring Data Redis (SDR) framework makes it easy to write Spring applications that use the Redis key-value store by eliminating the redundant tasks and boilerplate code required for interacting with the store through Spring’s excellent infrastructure support.

<a id="redis--redis:architecture"></a>
<a id="redis--redis-support-high-level-view"></a>

## Redis Support High-level View

The Redis support provides several components.For most tasks, the high-level abstractions and support services are the best choice.Note that, at any point, you can move between layers.For example, you can get a low-level connection (or even the native library) to communicate directly with Redis.

<a id="redis--section-summary"></a>

## Section Summary

- [Getting Started](#redis-getting-started)
- [Drivers](#redis-drivers)
- [Connection Modes](#redis-connection-modes)
- [RedisTemplate](#redis-template)
- [Redis Cache](#redis-redis-cache)
- [Redis Cluster](#redis-cluster)
- [Hash Mapping](#redis-hash-mappers)
- [Pub/Sub Messaging](#redis-pubsub)
- [Redis Streams](#redis-redis-streams)
- [Scripting](#redis-scripting)
- [Redis Transactions](#redis-transactions)
- [Pipelining](#redis-pipelining)
- [Support Classes](#redis-support-classes)

---

<a id="redis-getting-started"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/getting-started.html -->

<!-- page_index: 5 -->

# Getting Started

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-getting-started--page-title"></a>
<a id="redis-getting-started--getting-started"></a>

# Getting Started

An easy way to bootstrap setting up a working environment is to create a Spring-based project via [start.spring.io](https://start.spring.io/#!type=maven-project&dependencies=data-redis) or create a Spring project in [Spring Tools](https://spring.io/tools).

<a id="redis-getting-started--redis.examples-repo"></a>
<a id="redis-getting-started--examples-repository"></a>

## Examples Repository

The GitHub [spring-data-examples repository](https://github.com/spring-projects/spring-data-examples) hosts several examples that you can download and play around with to get a feel for how the library works.

<a id="redis-getting-started--redis.hello-world"></a>
<a id="redis-getting-started--hello-world"></a>

## Hello World

First, you need to set up a running Redis server.
Spring Data Redis requires Redis 2.6 or above and Spring Data Redis integrates with [Lettuce](https://github.com/lettuce-io/lettuce-core) and [Jedis](https://github.com/redis/jedis), two popular open-source Java libraries for Redis.

Now you can create a simple Java application that stores and reads a value to and from Redis.

Create the main application to run, as the following example shows:

- Imperative
- Reactive

```java
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;

public class RedisApplication {

	private static final Log LOG = LogFactory.getLog(RedisApplication.class);

	public static void main(String[] args) {

		LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory();
		connectionFactory.afterPropertiesSet();

		RedisTemplate<String, String> template = new RedisTemplate<>();
		template.setConnectionFactory(connectionFactory);
		template.setDefaultSerializer(StringRedisSerializer.UTF_8);
		template.afterPropertiesSet();

		template.opsForValue().set("foo", "bar");

		LOG.info("Value at foo:" + template.opsForValue().get("foo"));

		connectionFactory.destroy();
	}
}
```

```java
import reactor.core.publisher.Mono;

import java.time.Duration;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.ReactiveRedisTemplate;
import org.springframework.data.redis.serializer.RedisSerializationContext;

public class ReactiveRedisApplication {

	private static final Log LOG = LogFactory.getLog(ReactiveRedisApplication.class);

	public static void main(String[] args) {

		LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory();
		connectionFactory.afterPropertiesSet();

		ReactiveRedisTemplate<String, String> template = new ReactiveRedisTemplate<>(connectionFactory,
				RedisSerializationContext.string());

		Mono<Boolean> set = template.opsForValue().set("foo", "bar");
		set.block(Duration.ofSeconds(10));

		LOG.info("Value at foo:" + template.opsForValue().get("foo").block(Duration.ofSeconds(10)));

		connectionFactory.destroy();
	}
}
```

Even in this simple example, there are a few notable things to point out:

- You can create an instance of [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html) (or [`ReactiveRedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveRedisTemplate.html)for reactive usage) with a [`RedisConnectionFactory`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisConnectionFactory.html). Connection factories are an abstraction on top of the supported drivers.
- There’s no single way to use Redis as it comes with support for a wide range of data structures such as plain keys ("strings"), lists, sets, sorted sets, streams, hashes and so on.

---

<a id="redis-drivers"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/drivers.html -->

<!-- page_index: 6 -->

# Drivers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-drivers--page-title"></a>
<a id="redis-drivers--drivers"></a>

# Drivers

One of the first tasks when using Redis and Spring is to connect to the store through the IoC container.
To do that, a Java connector (or binding) is required.
No matter the library you choose, you need to use only one set of Spring Data Redis APIs (which behaves consistently across all connectors).
The `org.springframework.data.redis.connection` package and its `RedisConnection` and `RedisConnectionFactory` interfaces for working with and retrieving active connections to Redis.

<a id="redis-drivers--redis:connectors:connection"></a>
<a id="redis-drivers--redisconnection-and-redisconnectionfactory"></a>

## RedisConnection and RedisConnectionFactory

`RedisConnection` provides the core building block for Redis communication, as it handles the communication with the Redis backend.
It also automatically translates underlying connecting library exceptions to Spring’s consistent [DAO exception hierarchy](https://docs.spring.io/spring-framework/reference/7.0/data-access.html#dao-exceptions) so that you can switch connectors without any code changes, as the operation semantics remain the same.

> [!NOTE]
> For the corner cases where the native library API is required, `RedisConnection` provides a dedicated method (`getNativeConnection`) that returns the raw, underlying object used for communication.

Active `RedisConnection` objects are created through `RedisConnectionFactory`.
In addition, the factory acts as `PersistenceExceptionTranslator` objects, meaning that, once declared, they let you do transparent exception translation.
For example, you can do exception translation through the use of the `@Repository` annotation and AOP.
For more information, see the dedicated [section](https://docs.spring.io/spring-framework/reference/7.0/data-access.html#orm-exception-translation) in the Spring Framework documentation.

> [!NOTE]
> `RedisConnection` classes are **not** Thread-safe.
> While the underlying native connection, such as Lettuce’s `StatefulRedisConnection`, may be Thread-safe, Spring Data Redis’s `LettuceConnection` class itself is not.
> Therefore, you should **not** share instances of a `RedisConnection` across multiple Threads.
> This is especially true for transactional, or blocking Redis operations and commands, such as `BLPOP`.
> In transactional and pipelining operations, for instance, `RedisConnection` holds onto unguarded mutable state to complete the operation correctly, thereby making it unsafe to use with multiple Threads.
> This is by design.

> [!TIP]
> If you need to share (stateful) Redis resources, like connections, across multiple Threads, for performance reasons or otherwise, then you should acquire the native connection and use the Redis client library (driver) API directly.
> Alternatively, you can use the `RedisTemplate`, which acquires and manages connections for operations (and Redis commands) in a Thread-safe manner.
> See [documentation](#redis-template) on `RedisTemplate` for more details.

> [!NOTE]
> Depending on the underlying configuration, the factory can return a new connection or an existing connection (when a pool or shared native connection is used).

The easiest way to work with a `RedisConnectionFactory` is to configure the appropriate connector through the IoC container and inject it into the using class.

Unfortunately, currently, not all connectors support all Redis features.
When invoking a method on the Connection API that is unsupported by the underlying library, an `UnsupportedOperationException` is thrown.
The following overview explains features that are supported by the individual Redis connectors:

| Supported Feature | Lettuce | Jedis |
| --- | --- | --- |
| Standalone Connections | X | X |
| [Master/Replica Connections](#redis--redis:write-to-master-read-from-replica) | X |  |
| [Redis Sentinel](#redis--redis:sentinel) | Master Lookup, Sentinel Authentication, Replica Reads | Master Lookup |
| [Redis Cluster](#redis-cluster) | Cluster Connections, Cluster Node Connections, Replica Reads | Cluster Connections, Cluster Node Connections |
| Transport Channels | TCP, OS-native TCP (epoll, kqueue), Unix Domain Sockets | TCP |
| Connection Pooling | X (using `commons-pool2`) | X (using `commons-pool2`) |
| Other Connection Features | Singleton-connection sharing for non-blocking commands | Pipelining and Transactions mutually exclusive. Cannot use server/connection commands in pipeline/transactions. |
| SSL Support | X | X |
| [Pub/Sub](#redis-pubsub) | X | X |
| [Pipelining](#redis-pipelining) | X | X (Pipelining and Transactions mutually exclusive) |
| [Transactions](#redis-transactions) | X | X (Pipelining and Transactions mutually exclusive) |
| Datatype support | Key, String, List, Set, Sorted Set, Hash, Server, Stream, Scripting, Geo, HyperLogLog | Key, String, List, Set, Sorted Set, Hash, Server, Stream, Scripting, Geo, HyperLogLog |
| Reactive (non-blocking) API | X |  |

<a id="redis-drivers--redis:connectors:lettuce"></a>
<a id="redis-drivers--configuring-the-lettuce-connector"></a>

## Configuring the Lettuce Connector

[Lettuce](https://github.com/lettuce-io/lettuce-core) is a [Netty](https://netty.io/)-based open-source connector supported by Spring Data Redis through the `org.springframework.data.redis.connection.lettuce` package.

Add the following to the pom.xml files `dependencies` element:

```xml
<dependencies>

  <!-- other dependency elements omitted -->

  <dependency>
    <groupId>io.lettuce</groupId>
    <artifactId>lettuce-core</artifactId>
    <version>7.5.2.RELEASE</version>
  </dependency>

</dependencies>
```

The following example shows how to create a new Lettuce connection factory:

```java
@Configuration class AppConfig {
@Bean public LettuceConnectionFactory redisConnectionFactory() {
return new LettuceConnectionFactory(new RedisStandaloneConfiguration("server", 6379));}}
```

There are also a few Lettuce-specific connection parameters that can be tweaked.
By default, all `LettuceConnection` instances created by the `LettuceConnectionFactory` share the same thread-safe native connection for all non-blocking and non-transactional operations.
To use a dedicated connection each time, set `shareNativeConnection` to `false`. `LettuceConnectionFactory` can also be configured to use a `LettucePool` for pooling blocking and transactional connections or all connections if `shareNativeConnection` is set to `false`.

The following example shows a more sophisticated configuration, including SSL and timeouts, that uses `LettuceClientConfigurationBuilder`:

```java
@Bean
public LettuceConnectionFactory lettuceConnectionFactory() {

  LettuceClientConfiguration clientConfig = LettuceClientConfiguration.builder()
    .useSsl().and()
    .commandTimeout(Duration.ofSeconds(2))
    .shutdownTimeout(Duration.ZERO)
    .build();

  return new LettuceConnectionFactory(new RedisStandaloneConfiguration("localhost", 6379), clientConfig);
}
```

For more detailed client configuration tweaks, see [`LettuceClientConfiguration`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/lettuce/LettuceClientConfiguration.html).

Lettuce integrates with Netty’s [native transports](https://netty.io/wiki/native-transports.html), letting you use Unix domain sockets to communicate with Redis.
Make sure to include the appropriate native transport dependencies that match your runtime environment.
The following example shows how to create a Lettuce Connection factory for a Unix domain socket at `/var/run/redis.sock`:

```java
@Configuration class AppConfig {
@Bean public LettuceConnectionFactory redisConnectionFactory() {
return new LettuceConnectionFactory(new RedisSocketConfiguration("/var/run/redis.sock"));}}
```

> [!NOTE]
> Netty currently supports the epoll (Linux) and kqueue (BSD/macOS) interfaces for OS-native transport.

<a id="redis-drivers--redis:connectors:jedis"></a>
<a id="redis-drivers--configuring-the-jedis-connector"></a>

## Configuring the Jedis Connector

[Jedis](https://github.com/redis/jedis) is supported by the Spring Data Redis module through the `org.springframework.data.redis.connection.jedis` package.

Add the following to the pom.xml files `dependencies` element:

```xml
<dependencies>

  <!-- other dependency elements omitted -->

  <dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>7.4.1</version>
  </dependency>

</dependencies>
```

In its simplest form, the Jedis configuration looks as follow:

```java
@Configuration class AppConfig {
@Bean public JedisConnectionFactory redisConnectionFactory() {return new JedisConnectionFactory();}}
```

For production use, however, you might want to tweak settings such as the host or password, as shown in the following example:

```java
@Configuration class RedisConfiguration {
@Bean public JedisConnectionFactory redisConnectionFactory() {
RedisStandaloneConfiguration config = new RedisStandaloneConfiguration("server", 6379); return new JedisConnectionFactory(config);}}
```

---

<a id="redis-connection-modes"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/connection-modes.html -->

<!-- page_index: 7 -->

# Connection Modes

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-connection-modes--page-title"></a>
<a id="redis-connection-modes--connection-modes"></a>

# Connection Modes

Redis can be operated in various setups.
Each mode of operation requires specific configuration that is explained in the following sections.

<a id="redis-connection-modes--redis:standalone"></a>
<a id="redis-connection-modes--redis-standalone"></a>

## Redis Standalone

The easiest way to get started is by using Redis Standalone with a single Redis server,

Configure [`LettuceConnectionFactory`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/lettuce/LettuceConnectionFactory.html) or [`JedisConnectionFactory`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/jedis/JedisConnectionFactory.html), as shown in the following example:

```java
@Configuration class RedisStandaloneConfiguration {
/** * Lettuce */ @Bean public RedisConnectionFactory lettuceConnectionFactory() {return new LettuceConnectionFactory(new RedisStandaloneConfiguration("server", 6379));}
/** * Jedis */ @Bean public RedisConnectionFactory jedisConnectionFactory() {return new JedisConnectionFactory(new RedisStandaloneConfiguration("server", 6379));}}
```

<a id="redis-connection-modes--redis:write-to-master-read-from-replica"></a>
<a id="redis-connection-modes--write-to-master-read-from-replica"></a>

## Write to Master, Read from Replica

The Redis Master/Replica setup — without automatic failover (for automatic failover see: [Sentinel](#redis-connection-modes--redis:sentinel)) — not only allows data to be safely stored at more nodes.
It also allows, by using [Lettuce](#redis-drivers--redis:connectors:lettuce), reading data from replicas while pushing writes to the master.
You can set the read/write strategy to be used by using `LettuceClientConfiguration`, as shown in the following example:

```java
@Configuration
class WriteToMasterReadFromReplicaConfiguration {

  @Bean
  public LettuceConnectionFactory redisConnectionFactory() {

    LettuceClientConfiguration clientConfig = LettuceClientConfiguration.builder()
      .readFrom(REPLICA_PREFERRED)
      .build();

    RedisStandaloneConfiguration serverConfig = new RedisStandaloneConfiguration("server", 6379);

    return new LettuceConnectionFactory(serverConfig, clientConfig);
  }
}
```

> [!TIP]
> For environments reporting non-public addresses through the `INFO` command (for example, when using AWS), use [`RedisStaticMasterReplicaConfiguration`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisStaticMasterReplicaConfiguration.html) instead of [`RedisStandaloneConfiguration`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisStandaloneConfiguration.html). Please note that `RedisStaticMasterReplicaConfiguration` does not support Pub/Sub because of missing Pub/Sub message propagation across individual servers.

<a id="redis-connection-modes--redis:sentinel"></a>
<a id="redis-connection-modes--redis-sentinel"></a>

## Redis Sentinel

For dealing with high-availability Redis, Spring Data Redis has support for [Redis Sentinel](https://redis.io/topics/sentinel), using [`RedisSentinelConfiguration`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisSentinelConfiguration.html), as shown in the following example:

```java
/** * Lettuce */ @Bean public RedisConnectionFactory lettuceConnectionFactory() {RedisSentinelConfiguration sentinelConfig = new RedisSentinelConfiguration() .master("mymaster") .sentinel("127.0.0.1", 26379) .sentinel("127.0.0.1", 26380); return new LettuceConnectionFactory(sentinelConfig);}
/** * Jedis */ @Bean public RedisConnectionFactory jedisConnectionFactory() {RedisSentinelConfiguration sentinelConfig = new RedisSentinelConfiguration() .master("mymaster") .sentinel("127.0.0.1", 26379) .sentinel("127.0.0.1", 26380); return new JedisConnectionFactory(sentinelConfig);}
```

> [!TIP]
> `RedisSentinelConfiguration` can also be defined through `RedisSentinelConfiguration.of(PropertySource)`, which lets you pick up the following properties:
>
> Configuration Properties
>
> - `spring.redis.sentinel.master`: name of the master node.
> - `spring.redis.sentinel.nodes`: Comma delimited list of host:port pairs.
> - `spring.redis.sentinel.username`: The username to apply when authenticating with Redis Sentinel (requires Redis 6)
> - `spring.redis.sentinel.password`: The password to apply when authenticating with Redis Sentinel
> - `spring.redis.sentinel.dataNode.username`: The username to apply when authenticating with Redis Data Node
> - `spring.redis.sentinel.dataNode.password`: The password to apply when authenticating with Redis Data Node
> - `spring.redis.sentinel.dataNode.database`: The database index to apply when authenticating with Redis Data Node

Sometimes, direct interaction with one of the Sentinels is required. Using `RedisConnectionFactory.getSentinelConnection()` or `RedisConnection.getSentinelCommands()` gives you access to the first active Sentinel configured.

<a id="redis-connection-modes--cluster.enable"></a>
<a id="redis-connection-modes--redis-cluster"></a>

## Redis Cluster

[Cluster support](#redis-cluster) is based on the same building blocks as non-clustered communication. [`RedisClusterConnection`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisClusterConnection.html), an extension to `RedisConnection`, handles the communication with the Redis Cluster and translates errors into the Spring DAO exception hierarchy.
`RedisClusterConnection` instances are created with the `RedisConnectionFactory`, which has to be set up with the associated [`RedisClusterConfiguration`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisClusterConfiguration.html), as shown in the following example:

Example 1. Sample RedisConnectionFactory Configuration for Redis Cluster

```java
@Component @ConfigurationProperties(prefix = "spring.redis.cluster") public class ClusterConfigurationProperties {
/* * spring.redis.cluster.nodes[0] = 127.0.0.1:7379 * spring.redis.cluster.nodes[1] = 127.0.0.1:7380 * ...*/ List<String> nodes;
/** * Get initial collection of known cluster nodes in format {@code host:port}.* * @return */ public List<String> getNodes() {return nodes;}
public void setNodes(List<String> nodes) {this.nodes = nodes;}}
@Configuration public class AppConfig {
/** * Type safe representation of application.properties */ @Autowired ClusterConfigurationProperties clusterProperties;
public @Bean RedisConnectionFactory connectionFactory() {
return new LettuceConnectionFactory(new RedisClusterConfiguration(clusterProperties.getNodes()));}}
```

> [!TIP]
> `RedisClusterConfiguration` can also be defined through `RedisClusterConfiguration.of(PropertySource)`, which lets you pick up the following properties:
>
> Configuration Properties
>
> - `spring.redis.cluster.nodes`: Comma-delimited list of host:port pairs.
> - `spring.redis.cluster.max-redirects`: Number of allowed cluster redirections.

> [!NOTE]
> The initial configuration points driver libraries to an initial set of cluster nodes. Changes resulting from live cluster reconfiguration are kept only in the native driver and are not written back to the configuration.

---

<a id="redis-template"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/template.html -->

<!-- page_index: 8 -->

# Working with Objects through RedisTemplate

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-template--page-title"></a>
<a id="redis-template--working-with-objects-through-redistemplate"></a>

# Working with Objects through `RedisTemplate`

Most users are likely to use [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html) and its corresponding package, `org.springframework.data.redis.core` or its reactive variant [`ReactiveRedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveRedisTemplate.html).
The template is, in fact, the central class of the Redis module, due to its rich feature set.
The template offers a high-level abstraction for Redis interactions.
While `[Reactive]RedisConnection` offers low-level methods that accept and return binary values (`byte` arrays), the template takes care of serialization and connection management, freeing the user from dealing with such details.

The [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html) class implements the [`RedisOperations`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisOperations.html) interface and its reactive variant [`ReactiveRedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveRedisTemplate.html) implements [`ReactiveRedisOperations`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveRedisOperations.html).

> [!NOTE]
> The preferred way to reference operations on a `[Reactive]RedisTemplate` instance is through the
> `[Reactive]RedisOperations` interface.

Moreover, the template provides operations views (following the grouping from the Redis command [reference](https://redis.io/commands)) that offer rich, generified interfaces for working against a certain type or certain key (through the `KeyBound` interfaces) as described in the following table:

<details>
<summary>Operational views</summary>
<div>
<div id="_tabs_1">
<div>
<div>
<ul>
<li id="_tabs_1_imperative">
<p>Imperative</p>
</li>
<li id="_tabs_1_reactive">
<p>Reactive</p>
</li>
</ul>
</div>
<div id="_tabs_1_imperative--panel">
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Interface</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><em>Key Type Operations</em></p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/GeoOperations.html"><code>GeoOperations</code></a></p></td>
<td><p>Redis geospatial operations, such as <code>GEOADD</code>, <code>GEORADIUS</code>,…</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/HashOperations.html"><code>HashOperations</code></a></p></td>
<td><p>Redis hash operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/HyperLogLogOperations.html"><code>HyperLogLogOperations</code></a></p></td>
<td><p>Redis HyperLogLog operations, such as <code>PFADD</code>, <code>PFCOUNT</code>,…</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ListOperations.html"><code>ListOperations</code></a></p></td>
<td><p>Redis list operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/SetOperations.html"><code>SetOperations</code></a></p></td>
<td><p>Redis set operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ValueOperations.html"><code>ValueOperations</code></a></p></td>
<td><p>Redis string (or value) operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ZSetOperations.html"><code>ZSetOperations</code></a></p></td>
<td><p>Redis zset (or sorted set) operations</p></td>
</tr>
<tr>
<td colspan="2"><p><em>Key Bound Operations</em></p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundGeoOperations.html"><code>BoundGeoOperations</code></a></p></td>
<td><p>Redis key bound geospatial operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundHashOperations.html"><code>BoundHashOperations</code></a></p></td>
<td><p>Redis hash key bound operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundKeyOperations.html"><code>BoundKeyOperations</code></a></p></td>
<td><p>Redis key bound operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundListOperations.html"><code>BoundListOperations</code></a></p></td>
<td><p>Redis list key bound operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundSetOperations.html"><code>BoundSetOperations</code></a></p></td>
<td><p>Redis set key bound operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundValueOperations.html"><code>BoundValueOperations</code></a></p></td>
<td><p>Redis string (or value) key bound operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/BoundZSetOperations.html"><code>BoundZSetOperations</code></a></p></td>
<td><p>Redis zset (or sorted set) key bound operations</p></td>
</tr>
</tbody>
</table>
</div>
<div id="_tabs_1_reactive--panel">
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Interface</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><em>Key Type Operations</em></p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveGeoOperations.html"><code>ReactiveGeoOperations</code></a></p></td>
<td><p>Redis geospatial operations such as <code>GEOADD</code>, <code>GEORADIUS</code>, and others)</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveHashOperations.html"><code>ReactiveHashOperations</code></a></p></td>
<td><p>Redis hash operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveHyperLogLogOperations.html"><code>ReactiveHyperLogLogOperations</code></a></p></td>
<td><p>Redis HyperLogLog operations such as (<code>PFADD</code>, <code>PFCOUNT</code>, and others)</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveListOperations.html"><code>ReactiveListOperations</code></a></p></td>
<td><p>Redis list operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveSetOperations.html"><code>ReactiveSetOperations</code></a></p></td>
<td><p>Redis set operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveValueOperations.html"><code>ReactiveValueOperations</code></a></p></td>
<td><p>Redis string (or value) operations</p></td>
</tr>
<tr>
<td><p><a href="https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveZSetOperations.html"><code>ReactiveZSetOperations</code></a></p></td>
<td><p>Redis zset (or sorted set) operations</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</details>

Once configured, the template is thread-safe and can be reused across multiple instances.

`RedisTemplate` uses a Java-based serializer for most of its operations.
This means that any object written or read by the template is serialized and deserialized through Java.

You can change the serialization mechanism on the template, and the Redis module offers several implementations, which are available in the `org.springframework.data.redis.serializer` package.
See [Serializers](#redis-template--redis:serializer) for more information.
You can also set any of the serializers to null and use RedisTemplate with raw byte arrays by setting the `enableDefaultSerializer` property to `false`.
Note that the template requires all keys to be non-null.
However, values can be null as long as the underlying serializer accepts them.
Read the Javadoc of each serializer for more information.

For cases where you need a certain template view, declare the view as a dependency and inject the template.
The container automatically performs the conversion, eliminating the `opsFor[X]` calls, as shown in the following example:

Configuring Template API

- Java Imperative
- Java Reactive
- XML

```java
@Configuration class MyConfig {
@Bean LettuceConnectionFactory connectionFactory() {return new LettuceConnectionFactory();}
@Bean RedisTemplate<String, String> redisTemplate(RedisConnectionFactory connectionFactory) {
RedisTemplate<String, String> template = new RedisTemplate<>(); template.setConnectionFactory(connectionFactory); return template;}}
```

```java
@Configuration class MyConfig {
@Bean LettuceConnectionFactory connectionFactory() {return new LettuceConnectionFactory();}
@Bean ReactiveRedisTemplate<String, String> ReactiveRedisTemplate(ReactiveRedisConnectionFactory connectionFactory) {return new ReactiveRedisTemplate<>(connectionFactory, RedisSerializationContext.string());}}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:p="http://www.springframework.org/schema/p"
  xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd">

  <bean id="redisConnectionFactory" class="org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory"/>
  <!-- redis template definition -->
  <bean id="redisTemplate" class="org.springframework.data.redis.core.RedisTemplate" p:connection-factory-ref="redisConnectionFactory"/>
  ...

</beans>
```

Pushing an item to a List using `[Reactive]RedisTemplate`

- Imperative
- Reactive

```java
public class Example {

  // inject the actual operations
  @Autowired
  private RedisOperations<String, String> operations;

  // inject the template as ListOperations
  @Resource(name="redisTemplate")
  private ListOperations<String, String> listOps;

  public void addLink(String userId, URL url) {
    listOps.leftPush(userId, url.toExternalForm());
  }
}
```

```java
public class Example {
// inject the actual template @Autowired private ReactiveRedisOperations<String, String> operations;
public Mono<Long> addLink(String userId, URL url) {return operations.opsForList().leftPush(userId, url.toExternalForm());}}
```

<a id="redis-template--redis:string"></a>
<a id="redis-template--string-focused-convenience-classes"></a>

## String-focused Convenience Classes

Since it is quite common for the keys and values stored in Redis to be `java.lang.String`, the Redis modules provides two extensions to `RedisConnection` and `RedisTemplate`, respectively the `StringRedisConnection` (and its `DefaultStringRedisConnection` implementation) and `StringRedisTemplate` as a convenient one-stop solution for intensive String operations.
In addition to being bound to `String` keys, the template and the connection use the `StringRedisSerializer` underneath, which means the stored keys and values are human-readable (assuming the same encoding is used both in Redis and your code).
The following listings show an example:

- Java Imperative
- Java Reactive
- XML

```java
@Configuration class RedisConfiguration {
@Bean LettuceConnectionFactory redisConnectionFactory() {return new LettuceConnectionFactory();}
@Bean StringRedisTemplate stringRedisTemplate(RedisConnectionFactory redisConnectionFactory) {
StringRedisTemplate template = new StringRedisTemplate(); template.setConnectionFactory(redisConnectionFactory); return template;}}
```

```java
@Configuration class RedisConfiguration {
@Bean LettuceConnectionFactory redisConnectionFactory() {return new LettuceConnectionFactory();}
@Bean ReactiveStringRedisTemplate reactiveRedisTemplate(ReactiveRedisConnectionFactory factory) {return new ReactiveStringRedisTemplate<>(factory);}}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:p="http://www.springframework.org/schema/p"
  xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd">

  <bean id="redisConnectionFactory" class="org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory"/>

  <bean id="stringRedisTemplate" class="org.springframework.data.redis.core.StringRedisTemplate" p:connection-factory-ref="redisConnectionFactory"/>

</beans>
```

- Imperative
- Reactive

```java
public class Example {
@Autowired private StringRedisTemplate redisTemplate;
public void addLink(String userId, URL url) {redisTemplate.opsForList().leftPush(userId, url.toExternalForm());}}
```

```java
public class Example {
@Autowired private ReactiveStringRedisTemplate redisTemplate;
public Mono<Long> addLink(String userId, URL url) {return redisTemplate.opsForList().leftPush(userId, url.toExternalForm());}}
```

As with the other Spring templates, `RedisTemplate` and `StringRedisTemplate` let you talk directly to Redis through the `RedisCallback` interface.
This feature gives complete control to you, as it talks directly to the `RedisConnection`.
Note that the callback receives an instance of `StringRedisConnection` when a `StringRedisTemplate` is used.
The following example shows how to use the `RedisCallback` interface:

```java
public void useCallback() {
redisOperations.execute(new RedisCallback<Object>() {public Object doInRedis(RedisConnection connection) throws DataAccessException {Long size = connection.dbSize(); // Can cast to StringRedisConnection if using a StringRedisTemplate ((StringRedisConnection)connection).set("key", "value");} });}
```

<a id="redis-template--redis:serializer"></a>
<a id="redis-template--serializers"></a>

## Serializers

From the framework perspective, the data stored in Redis is only bytes.
While Redis itself supports various types, for the most part, these refer to the way the data is stored rather than what it represents.
It is up to the user to decide whether the information gets translated into strings or any other objects.

In Spring Data, the conversion between the user (custom) types and raw data (and vice-versa) is handled by Spring Data Redis in the `org.springframework.data.redis.serializer` package.

This package contains two types of serializers that, as the name implies, take care of the serialization process:

- Two-way serializers based on [`RedisSerializer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/serializer/RedisSerializer.html).
- Element readers and writers that use `RedisElementReader` and `RedisElementWriter`.

The main difference between these variants is that `RedisSerializer` primarily serializes to `byte[]` while readers and writers use `ByteBuffer`.

Multiple implementations are available (including two that have been already mentioned in this documentation):

- [`JdkSerializationRedisSerializer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/serializer/JdkSerializationRedisSerializer.html), which is used by default for [`RedisCache`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCache.html) and [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html).
- the `StringRedisSerializer`.

However, one can use `OxmSerializer` for Object/XML mapping through Spring [OXM](https://docs.spring.io/spring-framework/reference/7.0/data-access.html#oxm) support or [`JacksonJsonRedisSerializer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/serializer/JacksonJsonRedisSerializer.html) or [`GenericJacksonJsonRedisSerializer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/serializer/GenericJacksonJsonRedisSerializer.html) for storing data in [JSON](https://en.wikipedia.org/wiki/JSON) format.

Do note that the storage format is not limited only to values.
It can be used for keys, values, or hashes without any restrictions.

> [!WARNING]
> By default, [`RedisCache`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCache.html) and [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html) are configured to use Java native serialization.
> Java native serialization is known for allowing the running of remote code caused by payloads that exploit vulnerable libraries and classes injecting unverified bytecode.
> Manipulated input could lead to unwanted code being run in the application during the deserialization step.
> As a consequence, do not use serialization in untrusted environments.
> In general, we strongly recommend any other message format (such as JSON) instead.
>
> If you are concerned about security vulnerabilities due to Java serialization, consider the general-purpose serialization filter mechanism at the core JVM level:
>
> - [Filter Incoming Serialization Data](https://docs.oracle.com/en/java/javase/17/core/serialization-filtering1.html).
> - [JEP 290](https://openjdk.org/jeps/290).
> - [OWASP: Deserialization of untrusted data](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data).

---

<a id="redis-redis-cache"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-cache.html -->

<!-- page_index: 9 -->

# Redis Cache

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-cache--page-title"></a>
<a id="redis-redis-cache--redis-cache"></a>

# Redis Cache

Spring Data Redis provides an implementation of Spring Framework’s [Cache Abstraction](https://docs.spring.io/spring-framework/reference/7.0/integration.html#cache) in the `org.springframework.data.redis.cache` package.
To use Redis as a backing implementation, add [`RedisCacheManager`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCacheManager.html) to your configuration, as follows:

```java
@Bean
public RedisCacheManager cacheManager(RedisConnectionFactory connectionFactory) {
    return RedisCacheManager.create(connectionFactory);
}
```

`RedisCacheManager` behavior can be configured with [`RedisCacheManager.RedisCacheManagerBuilder`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCacheManager.RedisCacheManagerBuilder.html), letting you set the default [`RedisCacheManager`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCacheManager.html), transaction behavior, and predefined caches.

```java
RedisCacheManager cacheManager = RedisCacheManager.builder(connectionFactory)
    .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig())
    .transactionAware()
    .withInitialCacheConfigurations(Collections.singletonMap("predefined",
        RedisCacheConfiguration.defaultCacheConfig().disableCachingNullValues()))
    .build();
```

As shown in the preceding example, `RedisCacheManager` allows custom configuration on a per-cache basis.

The behavior of [`RedisCache`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCache.html) created by [`RedisCacheManager`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCacheManager.html) is defined with `RedisCacheConfiguration`.
The configuration lets you set key expiration times, prefixes, and `RedisSerializer` implementations for converting to and from the binary storage format, as shown in the following example:

```java
RedisCacheConfiguration cacheConfiguration = RedisCacheConfiguration.defaultCacheConfig()
    .entryTtl(Duration.ofSeconds(1))
    .disableCachingNullValues();
```

[`RedisCacheManager`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCacheManager.html) defaults to a lock-free [`RedisCacheWriter`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/cache/RedisCacheWriter.html) for reading and writing binary values.
Lock-free caching improves throughput.
The lack of entry locking can lead to overlapping, non-atomic commands for the `Cache` `putIfAbsent` and `clean` operations, as those require multiple commands to be sent to Redis.
The locking counterpart prevents command overlap by setting an explicit lock key and checking against presence of this key, which leads to additional requests and potential command wait times.

Locking applies on the **cache level**, not per **cache entry**.

It is possible to opt in to the locking behavior as follows:

```java
RedisCacheManager cacheManager = RedisCacheManager
    .builder(RedisCacheWriter.lockingRedisCacheWriter(connectionFactory))
    .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig())
    ...
```

By default, any `key` for a cache entry gets prefixed with the actual cache name followed by two colons (`::`).
This behavior can be changed to a static as well as a computed prefix.

The following example shows how to set a static prefix:

```java
// static key prefix
RedisCacheConfiguration.defaultCacheConfig().prefixCacheNameWith("(͡° ᴥ ͡°)");

The following example shows how to set a computed prefix:

// computed key prefix
RedisCacheConfiguration.defaultCacheConfig()
    .computePrefixWith(cacheName -> "¯\_(ツ)_/¯" + cacheName);
```

The cache implementation defaults to use `KEYS` and `DEL` to clear the cache. `KEYS` can cause performance issues with large keyspaces.
Therefore, the default `RedisCacheWriter` can be created with a `BatchStrategy` to switch to a `SCAN`-based batch strategy.
The `SCAN` strategy requires a batch size to avoid excessive Redis command round trips:

```java
RedisCacheManager cacheManager = RedisCacheManager
    .builder(RedisCacheWriter.nonLockingRedisCacheWriter(connectionFactory, BatchStrategies.scan(1000)))
    .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig())
    ...
```

> [!NOTE]
> The `KEYS` batch strategy is fully supported using any driver and Redis operation mode (Standalone, Clustered).
> `SCAN` is fully supported when using the Lettuce driver.
> Jedis supports `SCAN` only in non-clustered modes.

The following table lists the default settings for `RedisCacheManager`:

| Setting | Value |
| --- | --- |
| Cache Writer | Non-locking, `KEYS` batch strategy |
| Cache Configuration | `RedisCacheConfiguration#defaultConfiguration` |
| Initial Caches | None |
| Transaction Aware | No |

The following table lists the default settings for `RedisCacheConfiguration`:

| Key Expiration | None |
| --- | --- |
| Cache `null` | Yes |
| Prefix Keys | Yes |
| Default Prefix | The actual cache name |
| Key Serializer | `StringRedisSerializer` |
| Value Serializer | `JdkSerializationRedisSerializer` |
| Conversion Service | `DefaultFormattingConversionService` with default cache key converters |

> [!NOTE]
> By default `RedisCache`, statistics are disabled.
> Use `RedisCacheManagerBuilder.enableStatistics()` to collect local *hits* and *misses* through `RedisCache#getStatistics()`, returning a snapshot of the collected data.

<a id="redis-redis-cache--redis:support:cache-abstraction:expiration"></a>
<a id="redis-redis-cache--redis-cache-expiration"></a>

## Redis Cache Expiration

The implementation of time-to-idle (TTI) as well as time-to-live (TTL) varies in definition and behavior even across different data stores.

In general:

- *time-to-live* (TTL) *expiration* - TTL is only set and reset by a create or update data access operation.
  As long as the entry is written before the TTL expiration timeout, including on creation, an entry’s timeout will reset to the configured duration of the TTL expiration timeout.
  For example, if the TTL expiration timeout is set to 5 minutes, then the timeout will be set to 5 minutes on entry creation and reset to 5 minutes anytime the entry is updated thereafter and before the 5-minute interval expires.
  If no update occurs within 5 minutes, even if the entry was read several times, or even just read once during the 5-minute interval, the entry will still expire.
  The entry must be written to prevent the entry from expiring when declaring a TTL expiration policy.
- *time-to-idle* (TTI) *expiration* - TTI is reset anytime the entry is also read as well as for entry updates, and is effectively and extension to the TTL expiration policy.

> [!NOTE]
> Some data stores expire an entry when TTL is configured no matter what type of data access operation occurs on the entry (reads, writes, or otherwise).
> After the set, configured TTL expiration timeout, the entry is evicted from the data store regardless.
> Eviction actions (for example: destroy, invalidate, overflow-to-disk (for persistent stores), etc.) are data store specific.

<a id="redis-redis-cache--redis:support:cache-abstraction:expiration:tti"></a>
<a id="redis-redis-cache--time-to-live-ttl-expiration"></a>

### Time-To-Live (TTL) Expiration

Spring Data Redis’s `Cache` implementation supports *time-to-live* (TTL) expiration on cache entries.
Users can either configure the TTL expiration timeout with a fixed `Duration` or a dynamically computed `Duration` per cache entry by supplying an implementation of the new `RedisCacheWriter.TtlFunction` interface.

> [!TIP]
> The `RedisCacheWriter.TtlFunction` interface was introduced in Spring Data Redis `3.2.0`.

If all cache entries should expire after a set duration of time, then simply configure a TTL expiration timeout with a fixed `Duration`, as follows:

```java
RedisCacheConfiguration fiveMinuteTtlExpirationDefaults =
    RedisCacheConfiguration.defaultCacheConfig().enableTtl(Duration.ofMinutes(5));
```

However, if the TTL expiration timeout should vary by cache entry, then you must provide a custom implementation of the `RedisCacheWriter.TtlFunction` interface:

```java
enum MyCustomTtlFunction implements TtlFunction {
INSTANCE;
@Override public Duration getTimeToLive(Object key, @Nullable Object value) {// compute a TTL expiration timeout (Duration) based on the cache entry key and/or value}}
```

> [!NOTE]
> Under-the-hood, a fixed `Duration` TTL expiration is wrapped in a `TtlFunction` implementation returning the provided `Duration`.

Then, you can either configure the fixed `Duration` or the dynamic, per-cache entry `Duration` TTL expiration on a global basis using:

Global fixed Duration TTL expiration timeout

```java
RedisCacheManager cacheManager = RedisCacheManager.builder(redisConnectionFactory)
    .cacheDefaults(fiveMinuteTtlExpirationDefaults)
    .build();
```

Or, alternatively:

Global, dynamically computed per-cache entry Duration TTL expiration timeout

```java
RedisCacheConfiguration defaults = RedisCacheConfiguration.defaultCacheConfig()
        .entryTtl(MyCustomTtlFunction.INSTANCE);

RedisCacheManager cacheManager = RedisCacheManager.builder(redisConnectionFactory)
    .cacheDefaults(defaults)
    .build();
```

Of course, you can combine both global and per-cache configuration using:

Global fixed Duration TTL expiration timeout

```java
RedisCacheConfiguration predefined = RedisCacheConfiguration.defaultCacheConfig()
                                         .entryTtl(MyCustomTtlFunction.INSTANCE);

Map<String, RedisCacheConfiguration> initialCaches = Collections.singletonMap("predefined", predefined);

RedisCacheManager cacheManager = RedisCacheManager.builder(redisConnectionFactory)
    .cacheDefaults(fiveMinuteTtlExpirationDefaults)
    .withInitialCacheConfigurations(initialCaches)
    .build();
```

<a id="redis-redis-cache--redis:support:cache-abstraction:expiration:tti2"></a>
<a id="redis-redis-cache--time-to-idle-tti-expiration"></a>

### Time-To-Idle (TTI) Expiration

Redis itself does not support the concept of true, time-to-idle (TTI) expiration.
Still, using Spring Data Redis’s Cache implementation, it is possible to achieve time-to-idle (TTI) expiration-like behavior.

The configuration of TTI in Spring Data Redis’s Cache implementation must be explicitly enabled, that is, is opt-in.
Additionally, you must also provide TTL configuration using either a fixed `Duration` or a custom implementation of the `TtlFunction` interface as described above in [Redis Cache Expiration](#redis-redis-cache--redis:support:cache-abstraction:expiration).

For example:

```java
@Configuration
@EnableCaching
class RedisConfiguration {

    @Bean
    RedisConnectionFactory redisConnectionFactory() {
        // ...
    }

    @Bean
    RedisCacheManager cacheManager(RedisConnectionFactory connectionFactory) {

        RedisCacheConfiguration defaults = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(5))
            .enableTimeToIdle();

        return RedisCacheManager.builder(connectionFactory)
            .cacheDefaults(defaults)
            .build();
    }
}
```

Because Redis servers do not implement a proper notion of TTI, then TTI can only be achieved with Redis commands accepting expiration options.
In Redis, the "expiration" is technically a time-to-live (TTL) policy.
However, TTL expiration can be passed when reading the value of a key thereby effectively resetting the TTL expiration timeout, as is now the case in Spring Data Redis’s `Cache.get(key)` operation.

`RedisCache.get(key)` is implemented by calling the Redis `GETEX` command.

> [!WARNING]
> The Redis [`GETEX`](https://redis.io/commands/getex) command is only available in Redis version `6.2.0` and later.
> Therefore, if you are not using Redis `6.2.0` or later, then it is not possible to use Spring Data Redis’s TTI expiration.
> A command execution exception will be thrown if you enable TTI against an incompatible Redis (server) version.
> No attempt is made to determine if the Redis server version is correct and supports the `GETEX` command.

> [!WARNING]
> In order to achieve true time-to-idle (TTI) expiration-like behavior in your Spring Data Redis application, then an entry must be consistently accessed with (TTL) expiration on every read or write operation.
> There are no exceptions to this rule.
> If you are mixing and matching different data access patterns across your Spring Data Redis application (for example: caching, invoking operations using `RedisTemplate` and possibly, or especially when using Spring Data Repository CRUD operations), then accessing an entry may not necessarily prevent the entry from expiring if TTL expiration was set.
> For example, an entry maybe "put" in (written to) the cache during a `@Cacheable` service method invocation with a TTL expiration (i.e. `SET <expiration options>`) and later read using a Spring Data Redis Repository before the expiration timeout (using `GET` without expiration options).
> A simple `GET` without specifying expiration options will not reset the TTL expiration timeout on an entry.
> Therefore, the entry may expire before the next data access operation, even though it was just read.
> Since this cannot be enforced in the Redis server, then it is the responsibility of your application to consistently access an entry when time-to-idle expiration is configured, in and outside of caching, where appropriate.

---

<a id="redis-cluster"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/cluster.html -->

<!-- page_index: 10 -->

# Redis Cluster

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-cluster--page-title"></a>
<a id="redis-cluster--redis-cluster"></a>

# Redis Cluster

Working with [Redis Cluster](https://redis.io/topics/cluster-spec) requires Redis Server version 3.0+.
See the [Cluster Tutorial](https://redis.io/topics/cluster-tutorial) for more information.

> [!NOTE]
> When using [Redis Repositories](#repositories) with Redis Cluster, make yourself familiar with how to [run Redis Repositories on a Cluster](#redis-redis-repositories-cluster).

> [!WARNING]
> Do not rely on keyspace events when using Redis Cluster as keyspace events are not replicated across shards.
> Pub/Sub [subscribes to a random cluster node](https://github.com/spring-projects/spring-data-redis/issues/1111) which only receives keyspace events from a single shard.
> Use single-node Redis to avoid keyspace event loss.

<a id="redis-cluster--cluster.working.with.cluster"></a>
<a id="redis-cluster--working-with-redis-cluster-connection"></a>

## Working With Redis Cluster Connection

Redis Cluster behaves differently from single-node Redis or even a Sentinel-monitored master-replica environment.
This is because the automatic sharding maps a key to one of `16384` slots, which are distributed across the nodes.
Therefore, commands that involve more than one key must assert all keys map to the exact same slot to avoid cross-slot errors.
A single cluster node serves only a dedicated set of keys.
Commands issued against one particular server return results only for those keys served by that server.
As a simple example, consider the `KEYS` command.
When issued to a server in a cluster environment, it returns only the keys served by the node the request is sent to and not necessarily all keys within the cluster.
So, to get all keys in a cluster environment, you must read the keys from all the known master nodes.

While redirects for specific keys to the corresponding slot-serving node are handled by the driver libraries, higher-level functions, such as collecting information across nodes or sending commands to all nodes in the cluster, are covered by `RedisClusterConnection`.
Picking up the keys example from earlier, this means that the `keys(pattern)` method picks up every master node in the cluster and simultaneously runs the `KEYS` command on every master node while picking up the results and returning the cumulated set of keys.
To just request the keys of a single node `RedisClusterConnection` provides overloads for those methods (for example, `keys(node, pattern)`).

A `RedisClusterNode` can be obtained from `RedisClusterConnection.clusterGetNodes` or it can be constructed by using either the host and the port or the node Id.

The following example shows a set of commands being run across the cluster:

Example 1. Sample of Running Commands Across the Cluster

```text
[email protected]:7379 > cluster nodes

6b38bb... 127.0.0.1:7379 master - 0 0 25 connected 0-5460                      (1)
7bb78c... 127.0.0.1:7380 master - 0 1449730618304 2 connected 5461-present2       (2)
164888... 127.0.0.1:7381 master - 0 1449730618304 3 connected 10923-present3      (3)
b8b5ee... 127.0.0.1:7382 slave 6b38bb... 0 1449730618304 25 connected          (4)
```

```java
RedisClusterConnection connection = connectionFactory.getClusterConnection();

connection.set("thing1", value);                                               (5)
connection.set("thing2", value);                                               (6)

connection.keys("*");                                                          (7)

connection.keys(NODE_7379, "*");                                               (8)
connection.keys(NODE_7380, "*");                                               (9)
connection.keys(NODE_7381, "*");                                               (10)
connection.keys(NODE_7382, "*");                                               (11)
```

| **1** | Master node serving slots 0 to 5460 replicated to replica at 7382 |
| --- | --- |
| **2** | Master node serving slots 5461 to 10922 |
| **3** | Master node serving slots 10923 to 16383 |
| **4** | Replica node holding replicants of the master at 7379 |
| **5** | Request routed to node at 7381 serving slot 12182 |
| **6** | Request routed to node at 7379 serving slot 5061 |
| **7** | Request routed to nodes at 7379, 7380, 7381 → [thing1, thing2] |
| **8** | Request routed to node at 7379 → [thing2] |
| **9** | Request routed to node at 7380 → [] |
| **10** | Request routed to node at 7381 → [thing1] |
| **11** | Request routed to node at 7382 → [thing2] |

When all keys map to the same slot, the native driver library automatically serves cross-slot requests, such as `MGET`.
However, once this is not the case, `RedisClusterConnection` runs multiple parallel `GET` commands against the slot-serving nodes and again returns an accumulated result.
This is less performant than the single-slot approach and, therefore, should be used with care.
If in doubt, consider pinning keys to the same slot by providing a prefix in curly brackets, such as `{my-prefix}.thing1` and `{my-prefix}.thing2`, which will both map to the same slot number.
The following example shows cross-slot request handling:

Example 2. Sample of Cross-Slot Request Handling

```text
[email protected]:7379 > cluster nodes

6b38bb... 127.0.0.1:7379 master - 0 0 25 connected 0-5460                      (1)
7bb...
```

```java
RedisClusterConnection connection = connectionFactory.getClusterConnection();

connection.set("thing1", value);           // slot: 12182
connection.set("{thing1}.thing2", value);  // slot: 12182
connection.set("thing2", value);           // slot:  5461

connection.mGet("thing1", "{thing1}.thing2");                                  (2)

connection.mGet("thing1", "thing2");                                           (3)
```

| **1** | Same Configuration as in the sample before. |
| --- | --- |
| **2** | Keys map to same slot → 127.0.0.1:7381 MGET thing1 {thing1}.thing2 |
| **3** | Keys map to different slots and get split up into single slot ones routed to the according nodes → 127.0.0.1:7379 GET thing2 → 127.0.0.1:7381 GET thing1 |

> [!TIP]
> The preceding examples demonstrate the general strategy followed by Spring Data Redis.
> Be aware that some operations might require loading huge amounts of data into memory to compute the desired command.
> Additionally, not all cross-slot requests can safely be ported to multiple single slot requests and error if misused (for example, `PFCOUNT`).

<a id="redis-cluster--cluster.redistemplate"></a>
<a id="redis-cluster--working-with-redistemplate-and-clusteroperations"></a>

## Working with `RedisTemplate` and `ClusterOperations`

See the [Working with Objects through RedisTemplate](#redis-template) section for information about the general purpose, configuration, and usage of `RedisTemplate`.

> [!WARNING]
> Be careful when setting up `RedisTemplate#keySerializer` using any of the JSON `RedisSerializers`, as changing JSON structure has immediate influence on hash slot calculation.

`RedisTemplate` provides access to cluster-specific operations through the `ClusterOperations` interface, which can be obtained from `RedisTemplate.opsForCluster()`.
This lets you explicitly run commands on a single node within the cluster while retaining the serialization and deserialization features configured for the template.
It also provides administrative commands (such as `CLUSTER MEET`) or more high-level operations (for example, resharding).

The following example shows how to access `RedisClusterConnection` with `RedisTemplate`:

Example 3. Accessing `RedisClusterConnection` with `RedisTemplate`

```java
ClusterOperations clusterOps = redisTemplate.opsForCluster();
clusterOps.shutdown(NODE_7379);                                              (1)
```

**1**

Shut down node at 7379 and cross fingers there is a replica in place that can take over.

> [!NOTE]
> Redis Cluster pipelining is currently only supported through the Lettuce driver except for the following commands when using cross-slot keys: `rename`, `renameNX`, `sort`, `bLPop`, `bRPop`, `rPopLPush`, `bRPopLPush`, `info`, `sMove`, `sInter`, `sInterStore`, `sUnion`, `sUnionStore`, `sDiff`, `sDiffStore`.
> Same-slot keys are fully supported.

---

<a id="redis-hash-mappers"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/hash-mappers.html -->

<!-- page_index: 11 -->

# Hash Mapping

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-hash-mappers--page-title"></a>
<a id="redis-hash-mappers--hash-mapping"></a>

# Hash Mapping

Data can be stored by using various data structures within Redis. [`JacksonJsonRedisSerializer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/serializer/JacksonJsonRedisSerializer.html) can convert objects in [JSON](https://en.wikipedia.org/wiki/JSON) format.
Ideally, JSON can be stored as a value by using plain keys.
You can achieve a more sophisticated mapping of structured objects by using Redis hashes.
Spring Data Redis offers various strategies for mapping data to hashes (depending on the use case):

- Direct mapping, by using [`HashOperations`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/HashOperations.html) and a [serializer](#redis--redis:serializer)
- Using [Redis Repositories](#repositories)
- Using [`HashMapper`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/hash/HashMapper.html) and [`HashOperations`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/HashOperations.html)

<a id="redis-hash-mappers--redis.hashmappers.mappers"></a>
<a id="redis-hash-mappers--hash-mappers"></a>

## Hash Mappers

Hash mappers are converters of map objects to a `Map<K, V>` and back. [`HashMapper`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/hash/HashMapper.html) is intended for using with Redis Hashes.

Multiple implementations are available:

- [`BeanUtilsHashMapper`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/hash/BeanUtilsHashMapper.html) using Spring’s [BeanUtils](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/beans/BeanUtils.html).
- [`ObjectHashMapper`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/hash/ObjectHashMapper.html) using [Object-to-Hash Mapping](#redis-redis-repositories-mapping).
- [`JacksonHashMapper`](#redis-hash-mappers--redis.hashmappers.jackson3) using [FasterXML Jackson 3](https://github.com/FasterXML/jackson).
- [`Jackson2HashMapper`](#redis-hash-mappers--redis.hashmappers.jackson2) (deprecated) using [FasterXML Jackson 2](https://github.com/FasterXML/jackson).

The following example shows one way to implement hash mapping:

```java
public class Person {String firstname; String lastname;
// …}
public class HashMapping {
@Resource(name = "redisTemplate") HashOperations<String, byte[], byte[]> hashOperations;
HashMapper<Object, byte[], byte[]> mapper = new ObjectHashMapper();
public void writeHash(String key, Person person) {
Map<byte[], byte[]> mappedHash = mapper.toHash(person); hashOperations.putAll(key, mappedHash);}
public Person loadHash(String key) {
Map<byte[], byte[]> loadedHash = hashOperations.entries(key); return (Person) mapper.fromHash(loadedHash);}}
```

<a id="redis-hash-mappers--redis.hashmappers.jackson3"></a>
<a id="redis-hash-mappers--jacksonhashmapper"></a>

### JacksonHashMapper

[`JacksonHashMapper`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/hash/JacksonHashMapper.html) provides Redis Hash mapping for domain objects by using [FasterXML Jackson 3](https://github.com/FasterXML/jackson).
`JacksonHashMapper` can map top-level properties as Hash field names and, optionally, flatten the structure.
Simple types map to simple values. Complex types (nested objects, collections, maps, and so on) are represented as nested JSON.

Flattening creates individual hash entries for all nested properties and resolves complex types into simple types, as far as possible.

Consider the following class and the data structure it contains:

```java
public class Person {
  String firstname;
  String lastname;
  Address address;
  Date date;
  LocalDateTime localDateTime;
}

public class Address {
  String city;
  String country;
}
```

The following table shows how the data in the preceding class would appear in normal mapping:

| Hash Field | Value |
| --- | --- |
| firstname | `Jon` |
| lastname | `Snow` |
| address | `{ "city" : "Castle Black", "country" : "The North" }` |
| date | 1561543964015 |
| localDateTime | `2018-01-02T12:13:14` |

The following table shows how the data in the preceding class would appear in flat mapping:

| Hash Field | Value |
| --- | --- |
| firstname | `Jon` |
| lastname | `Snow` |
| address.city | `Castle Black` |
| address.country | `The North` |
| date | 1561543964015 |
| localDateTime | `2018-01-02T12:13:14` |

> [!NOTE]
> Flattening requires all property names to not interfere with the JSON path. Using dots or brackets in map keys or as property names is not supported when you use flattening. The resulting hash cannot be mapped back into an Object.

<a id="redis-hash-mappers--redis.hashmappers.jackson2"></a>
<a id="redis-hash-mappers--jackson2hashmapper"></a>

### Jackson2HashMapper

> [!WARNING]
> Jackson 2 based implementations have been deprecated and are subject to removal in a subsequent release.

[`Jackson2HashMapper`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/hash/Jackson2HashMapper.html) provides Redis Hash mapping for domain objects by using [FasterXML Jackson](https://github.com/FasterXML/jackson).
`Jackson2HashMapper` can map top-level properties as Hash field names and, optionally, flatten the structure.
Simple types map to simple values. Complex types (nested objects, collections, maps, and so on) are represented as nested JSON.

Flattening creates individual hash entries for all nested properties and resolves complex types into simple types, as far as possible.

Consider the following class and the data structure it contains:

```java
public class Person {
  String firstname;
  String lastname;
  Address address;
  Date date;
  LocalDateTime localDateTime;
}

public class Address {
  String city;
  String country;
}
```

The following table shows how the data in the preceding class would appear in normal mapping:

| Hash Field | Value |
| --- | --- |
| firstname | `Jon` |
| lastname | `Snow` |
| address | `{ "city" : "Castle Black", "country" : "The North" }` |
| date | `1561543964015` |
| localDateTime | `2018-01-02T12:13:14` |

The following table shows how the data in the preceding class would appear in flat mapping:

| Hash Field | Value |
| --- | --- |
| firstname | `Jon` |
| lastname | `Snow` |
| address.city | `Castle Black` |
| address.country | `The North` |
| date | `1561543964015` |
| localDateTime | `2018-01-02T12:13:14` |

> [!NOTE]
> Flattening requires all property names to not interfere with the JSON path. Using dots or brackets in map keys or as property names is not supported when you use flattening. The resulting hash cannot be mapped back into an Object.

> [!NOTE]
> `java.util.Date` and `java.util.Calendar` are represented with milliseconds. JSR-310 Date/Time types are serialized to their `toString` form if `jackson-datatype-jsr310` is on the class path.

---

<a id="redis-pubsub"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/pubsub.html -->

<!-- page_index: 12 -->

# Pub/Sub Messaging

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-pubsub--page-title"></a>
<a id="redis-pubsub--pub-sub-messaging"></a>

# Pub/Sub Messaging

Spring Data provides dedicated messaging integration for Redis, similar in spirit to the JMS support in Spring Framework.

Redis messaging can be roughly divided into two areas of functionality:

- [Publication or sending messages](#redis-pubsub-sending)
- [Subscription or receiving messages](#redis-pubsub-receiving)

This is an example of the pattern often referred to as Publish/Subscribe (Pub/Sub).
On the sending side, you can publish messages through the low-level `RedisConnection` contract, through
[`RedisOperations`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisOperations.html) (typically backed by [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html)), or through the message-oriented
[`RedisMessageSendingTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/messaging/RedisMessageSendingTemplate.html).
For asynchronous reception similar to Java EE’s message-driven bean style, Spring Data provides a dedicated message listener container that is used to create Message-Driven POJOs (MDPs) and, for synchronous reception, the `RedisConnection` contract.

The `org.springframework.data.redis.connection` and `org.springframework.data.redis.listener` packages provide the core functionality for Redis messaging.

The `org.springframework.data.redis.annotation` package provides the necessary infrastructure to support annotation-driven listener endpoints by using `@RedisListener`.

The `org.springframework.data.redis.config` package provides the parser implementation for the `redis` namespace as well as the Java config support to configure listener endpoints.

---

<a id="redis-pubsub-sending"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/pubsub-sending.html -->

<!-- page_index: 13 -->

# Publishing (Sending a Message)

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-pubsub-sending--page-title"></a>
<a id="redis-pubsub-sending--publishing-sending-a-message"></a>

# Publishing (Sending a Message)

To publish a message, choose the abstraction level that matches your application’s responsibility:

- `[Reactive]RedisConnection` is the low-level contract and operates on already-serialized (`byte[]`) channel and message data.
- `[Reactive]RedisOperations` (typically through `RedisTemplate`) publishes messages by using the template’s configured serializers for conversion.
- `RedisMessageSendingTemplate` integrates with Spring Messaging and delegates payload conversion to a `MessageConverter`, selecting converters according to the payload type and, if present, the `contentType` header.

The imperative API offers all three variants.
The reactive API offers the low-level connection and `ReactiveRedisOperations` variants.

The following table summarizes the differences between the sending options:

| Variant | Responsibility | Conversion model |
| --- | --- | --- |
| `[Reactive]RedisConnection` | Publish binary channel and message data. | Application code provides the binary (`byte[]`/`ByteBuffer`) values. |
| `RedisTemplate` / `[Reactive]RedisOperations` | Publish application values through the Redis data access abstraction. | Uses the configured value serializer for the message body. Publication is therefore bound to the template-specific value serializer. |
| `RedisMessageSendingTemplate` | Publish through Spring’s `Message<?>` abstraction for a flexible message conversion. | Uses `RedisMessageConverters` to select a `MessageConverter` according to the payload type and, if present, the `MessageHeaders.CONTENT_TYPE` header. Useful for applications that already use Spring Messaging or [Annotation-driven Listener Endpoints](#redis-pubsub-annotated). |

The following example shows the available sending variants:

- Imperative
- Reactive
- Spring Messaging

```java
// send message through connection
RedisConnection connection = …
byte[] channel = …
byte[] message = …
connection.pubSubCommands().publish(channel, message);

// send message through RedisOperations
RedisOperations<String, Object> operations = …
Long numberOfClients = operations.convertAndSend("chatroom", "hello!");
```

```java
// send message through connection
ReactiveRedisConnection connection = …
ByteBuffer channel = …
ByteBuffer message = …
connection.pubSubCommands().publish(channel, message);

// send message through ReactiveRedisOperations
ReactiveRedisOperations<String, String> operations = …
Mono<Long> numberOfClients = operations.convertAndSend("chatroom", "hello!");
```

```java
RedisMessageSendingTemplate template = …
template.convertAndSend("chatroom", new Greeting("hello", "world"));

template.convertAndSend("chatroom", new Greeting("hello", "world"),    (1)
     Map.of(MessageHeaders.CONTENT_TYPE, "application/json"));

template.convertAndSend("chatroom", new Greeting("hello", "world"),    (2)
     Map.of(MessageHeaders.CONTENT_TYPE, JdkSerializerMessageConverter.APPLICATION_JAVA_SERIALIZED_OBJECT_VALUE));
```

**1**

Provide a `contentType` as hint for converter selection.
Redis Pub/Sub does not support headers so it transmits only the serialized message.

**2**

Select Java Serialization for the message body.
Requires `JdkSerializerMessageConverter` to use this content type.

---

<a id="redis-pubsub-receiving"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/pubsub-receiving.html -->

<!-- page_index: 14 -->

# Subscribing (Receiving a Message)

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-pubsub-receiving--page-title"></a>
<a id="redis-pubsub-receiving--subscribing-receiving-a-message"></a>

# Subscribing (Receiving a Message)

On the receiving side, one can subscribe to one or multiple channels either by naming them directly or by using pattern matching.
The latter approach is quite useful, as it not only lets multiple subscriptions be created with one command but can also listen on channels not yet created at subscription time (as long as they match the pattern).

At the low-level, `RedisConnection` offers the `subscribe` and `pSubscribe` methods that map the Redis commands for subscribing by channel or by pattern, respectively.
Note that multiple channels or patterns can be used as arguments.
To change the subscription of a connection or query whether it is listening, `RedisConnection` provides the `getSubscription` and `isSubscribed` methods.

> [!NOTE]
> Subscription commands in Spring Data Redis are blocking.
> That is, calling subscribe on a connection causes the current thread to block as it starts waiting for messages.
> The thread is released only if the subscription is canceled, which happens when another thread invokes `unsubscribe` or `pUnsubscribe` on the **same** connection.
> See “[Message Listener Containers](#redis-pubsub--redis:pubsub:subscribe:containers)” (later in this document) for a solution to this problem.

As mentioned earlier, once subscribed, a connection starts waiting for messages.
Only commands that add new subscriptions, modify existing subscriptions, and cancel existing subscriptions are allowed.
Invoking anything other than `subscribe`, `pSubscribe`, `unsubscribe`, or `pUnsubscribe` throws an exception.

In order to subscribe to messages, one needs to implement the `MessageListener` callback.
Each time a new message arrives, the callback gets invoked and the user code gets run by the `onMessage` method.
The interface gives access not only to the actual message but also to the channel it has been received through and the pattern (if any) used by the subscription to match the channel.
This information lets the callee differentiate between various messages not just by content but also examining additional details.

<a id="redis-pubsub-receiving--container"></a>
<a id="redis-pubsub-receiving--message-listener-containers"></a>

## Message Listener Containers

Due to its blocking nature, low-level subscription is not attractive, as it requires connection and thread management for every single listener.
To alleviate this problem, Spring Data offers [`RedisMessageListenerContainer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/RedisMessageListenerContainer.html), which does all the heavy lifting.
If you are familiar with EJB and JMS, you should find the concepts familiar, as it is designed to be as close as possible to the support in Spring Framework and its message-driven POJOs (MDPs).

[`RedisMessageListenerContainer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/RedisMessageListenerContainer.html) acts as a message listener container.
It is used to receive messages from a Redis channel and drive the [`MessageListener`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/MessageListener.html) instances that are injected into it.
The listener container is responsible for all threading of message reception and dispatches into the listener for processing.
A message listener container is the intermediary between an MDP and a messaging provider and takes care of registering to receive messages, resource acquisition and release, exception conversion, and the like.
This lets you as an application developer write the (possibly complex) business logic associated with receiving a message (and reacting to it) and delegates boilerplate Redis infrastructure concerns to the framework.

A [`MessageListener`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/MessageListener.html) can additionally implement [`SubscriptionListener`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/SubscriptionListener.html) to receive notifications upon subscription/unsubscribe confirmation.
Listening to subscription notifications can be useful when synchronizing invocations.

Furthermore, to minimize the application footprint, [`RedisMessageListenerContainer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/RedisMessageListenerContainer.html) lets one connection and one thread be shared by multiple listeners even though they do not share a subscription.
Thus, no matter how many listeners or channels an application tracks, the runtime cost remains the same throughout its lifetime.
Moreover, the container allows runtime configuration changes so that you can add or remove listeners while an application is running without the need for a restart.
Additionally, the container uses a lazy subscription approach, using a `RedisConnection` only when needed.
If all the listeners are unsubscribed, cleanup is automatically performed, and the thread is released.

To help with the asynchronous nature of messages, the container requires a `java.util.concurrent.Executor` (or Spring’s `TaskExecutor`) for dispatching the messages.
Depending on the load, the number of listeners, or the runtime environment, you should change or tweak the executor to better serve your needs.
In particular, in managed environments (such as app servers), it is highly recommended to pick a proper `TaskExecutor` to take advantage of its runtime.

<a id="redis-pubsub-receiving--receiving-async-message-listener-adapter"></a>
<a id="redis-pubsub-receiving--the-messagelisteneradapter"></a>

## The MessageListenerAdapter

The [`MessageListenerAdapter`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/adapter/MessageListenerAdapter.html) class is the final component in Spring’s asynchronous messaging support.
In a nutshell, it lets you expose almost **any** class as a MDP (though there are some constraints).

Consider the following interface definition:

```java
public interface MessageDelegate {
  void handleMessage(String message);
  void handleMessage(Map message);
  void handleMessage(byte[] message);
  void handleMessage(Serializable message);
  // pass the channel/pattern as well
  void handleMessage(Serializable message, String channel);
 }
```

Notice that, although the interface does not extend the `MessageListener` interface, it can still be used as a MDP by using the [`MessageListenerAdapter`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/adapter/MessageListenerAdapter.html) class.
Notice also how the various message handling methods are strongly typed according to the **contents** of the various `Message` types that they can receive and handle.
In addition, the channel or pattern to which a message is sent can be passed in to the method as the second argument of type `String`:

```java
public class DefaultMessageDelegate implements MessageDelegate {
  // implementation elided for clarity...
}
```

```
Notice how the above implementation of the `MessageDelegate` interface (the above `DefaultMessageDelegate` class) has *no* Redis dependencies at all. It truly is a POJO that we make into an MDP with the following configuration:
```

- Java
- XML

```java
@Configuration class MyConfig {
// …
@Bean DefaultMessageDelegate listener() {return new DefaultMessageDelegate();}
@Bean MessageListenerAdapter messageListenerAdapter(DefaultMessageDelegate listener) {return new MessageListenerAdapter(listener, "handleMessage");}
@Bean RedisMessageListenerContainer redisMessageListenerContainer(RedisConnectionFactory connectionFactory, MessageListenerAdapter listener) {
RedisMessageListenerContainer container = new RedisMessageListenerContainer(); container.setConnectionFactory(connectionFactory); container.addMessageListener(listener, ChannelTopic.of("chatroom")); return container;}}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns:redis="http://www.springframework.org/schema/redis"
   xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
   http://www.springframework.org/schema/redis https://www.springframework.org/schema/redis/spring-redis.xsd">

<!-- the default ConnectionFactory -->
<redis:listener-container>
  <!-- the method attribute can be skipped as the default method name is "handleMessage" -->
  <redis:listener ref="listener" method="handleMessage" topic="chatroom" />
</redis:listener-container>

<bean id="listener" class="redisexample.DefaultMessageDelegate"/>
 ...
</beans>
```

> [!NOTE]
> The listener topic can be either a channel (for example, `topic="chatroom"` respective `Topic.channel("chatroom")`) or a pattern (for example, `topic="*room"` respective `Topic.pattern("*room")`).

The preceding example uses the Redis namespace to declare the message listener container and automatically register the POJOs as listeners.
The full-blown beans definition follows:

```xml
<bean id="messageListener" class="org.springframework.data.redis.listener.adapter.MessageListenerAdapter">
  <constructor-arg>
    <bean class="redisexample.DefaultMessageDelegate"/>
  </constructor-arg>
</bean>

<bean id="redisContainer" class="org.springframework.data.redis.listener.RedisMessageListenerContainer">
  <property name="connectionFactory" ref="connectionFactory"/>
  <property name="messageListeners">
    <map>
      <entry key-ref="messageListener">
        <bean class="org.springframework.data.redis.listener.ChannelTopic">
          <constructor-arg value="chatroom"/>
        </bean>
      </entry>
    </map>
  </property>
</bean>
```

Each time a message is received, the adapter automatically and transparently performs translation (using the configured `RedisSerializer`) between the low-level format and the required object type.
Any exception caused by the method invocation is caught and handled by the container (by default, exceptions get logged).

<a id="redis-pubsub-receiving--reactive-container"></a>
<a id="redis-pubsub-receiving--reactive-message-listener-container"></a>

## Reactive Message Listener Container

Spring Data offers [`ReactiveRedisMessageListenerContainer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/ReactiveRedisMessageListenerContainer.html) which does all the heavy lifting of conversion and subscription state management on behalf of the user.

The message listener container itself does not require external threading resources.
It uses the driver threads to publish messages.

```java
ReactiveRedisConnectionFactory factory = …
ReactiveRedisMessageListenerContainer container = new ReactiveRedisMessageListenerContainer(factory);

Flux<ChannelMessage<String, String>> stream = container.receive(ChannelTopic.of("my-channel"));
```

To await and ensure proper subscription, you can use the `receiveLater` method that returns a `Mono<Flux<ChannelMessage>>`.
The resulting `Mono` completes with an inner publisher as a result of completing the subscription to the given topics.
By intercepting `onNext` signals, you can synchronize server-side subscriptions.

```java
ReactiveRedisConnectionFactory factory = …
ReactiveRedisMessageListenerContainer container = new ReactiveRedisMessageListenerContainer(factory);

Mono<Flux<ChannelMessage<String, String>>> stream = container.receiveLater(ChannelTopic.of("my-channel"));

stream.doOnNext(inner -> // notification hook when Redis subscriptions are synchronized with the server)
    .flatMapMany(Function.identity())
    .…;
```

<a id="redis-pubsub-receiving--template-subscribe"></a>
<a id="redis-pubsub-receiving--subscribing-through-the-template-api"></a>

## Subscribing through the Template API

As mentioned above you can directly use [`ReactiveRedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/ReactiveRedisTemplate.html) to subscribe to channels / patterns.
This approach offers a straight forward, though limited solution as you lose the option to add subscriptions after the initial ones.
Nevertheless you still can control the message stream via the returned `Flux` using eg. `take(Duration)`.
When done reading, on error or cancellation all bound resources are freed again.

```java
redisTemplate.listenToChannel("channel1", "channel2").doOnNext(msg -> {
    // message processing ...
}).subscribe();
```

---

<a id="redis-pubsub-annotated"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/pubsub-annotated.html -->

<!-- page_index: 15 -->

# Annotation-driven Listener Endpoints

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-pubsub-annotated--page-title"></a>
<a id="redis-pubsub-annotated--annotation-driven-listener-endpoints"></a>

# Annotation-driven Listener Endpoints

The easiest way to receive a message asynchronously is to use the annotated listener endpoint infrastructure.
In a nutshell, it lets you expose a method of a managed bean as a Redis listener endpoint.
The following example shows how to use it:

```java
@Component
public class MyService {

  @RedisListener(topic = "my-channel")
  public void processOrder(String data) { ... }
}
```

The idea of the preceding example is that, whenever a message is received through a channel `my-channel`, the `processOrder` method is invoked accordingly (in this case, with the content of the Redis Pub/Sub message, similar to what the [`MessageListenerAdapter`](#redis-pubsub-receiving--receiving-async-message-listener-adapter) provides).

The annotated endpoint infrastructure creates a message listener behind the scenes for each annotated method and registering to `RedisMessageListenerContainer`.
Endpoints are not registered against the application context but can be easily located for management purposes by using the `RedisListenerEndpointRegistry` bean.

> [!TIP]
> `@RedisListener` is a repeatable annotation, so you can associate several Redis topics (channels or patterns) with the same method by adding additional `@RedisListener` declarations to it.

<a id="redis-pubsub-annotated--redis-annotated-support"></a>
<a id="redis-pubsub-annotated--enable-listener-endpoint-annotations"></a>

## Enable Listener Endpoint Annotations

To enable support for `@RedisListener` annotations, you can add `@EnableRedisListeners` to one of your `@Configuration` classes, as the following example shows:

- Java
- Kotlin

```java
@Configuration
@EnableRedisListeners
public class RedisConfiguration {

  @Bean
  public RedisMessageListenerContainer redisMessageListenerContainer(RedisConnectionFactory connectionFactory) {

    RedisMessageListenerContainer factory = new RedisMessageListenerContainer();
    factory.setConnectionFactory(connectionFactory);
    return factory;
  }
}
```

```kotlin
@Configuration @EnableRedisListeners class RedisConfiguration {
@Bean fun redisMessageListenerContainer(connectionFactory: RedisConnectionFactory) =RedisMessageListenerContainer().apply {setConnectionFactory(connectionFactory);}}
```

You can customize the [listener registrar](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/config/RedisListenerEndpointRegistrar.html) by implementing the `RedisListenerConfigurer` interface.
See the javadoc of classes that implement [`RedisListenerConfigurer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/config/RedisListenerConfigurer.html) for details and examples.

<a id="redis-pubsub-annotated--redis-annotated-programmatic-registration"></a>
<a id="redis-pubsub-annotated--programmatic-endpoint-registration"></a>

## Programmatic Endpoint Registration

`RedisListenerEndpoint` provides a model of a Redis endpoint and is responsible for configuring the container for that model.
The infrastructure lets you programmatically configure endpoints in addition to the ones that are detected by the `RedisListener` annotation.
The following example shows how to do so:

```java
@Configuration @EnableRedisListeners public class AppConfig implements RedisListenerConfigurer {
@Override public void configureRedisListeners(RedisListenerEndpointRegistrar registrar) {SimpleRedisListenerEndpoint endpoint = new SimpleRedisListenerEndpoint(); endpoint.setId("myRedisEndpoint"); endpoint.setTopic("my-channel"); endpoint.setMessageListener((message, pattern) -> {// processing }); registrar.registerEndpoint(endpoint);}}
```

In the preceding example, we used `SimpleRedisListenerEndpoint`, which provides the actual `MessageListener` to invoke.
However, you could also build your own endpoint variant to describe a custom invocation mechanism.

Note that you could skip the use of `@RedisListener` altogether and programmatically register only your endpoints through `RedisListenerConfigurer`.

<a id="redis-pubsub-annotated--redis-annotated-method-signature"></a>
<a id="redis-pubsub-annotated--annotated-endpoint-method-signature"></a>

## Annotated Endpoint Method Signature

So far, we have been injecting a simple `String` in our endpoint, but it can actually have a very flexible method signature.
In the following example, we rewrite it to inject the `Order` with a header:

```java
@Component public class MyService {
@RedisListener("my-order-channels*") public void processOrder(Order order, @Header("pattern") Topic pattern) {...}}
```

The main elements you can inject in Redis listener endpoints are as follows:

- The `org.springframework.messaging.Message` that represents the incoming Redis message.
  Note that this message holds headers (as defined by `PubSubHeaders`).
- `@Header`-annotated method arguments to extract a specific header value.
  Since Redis Pub/Sub messages do consist only of the body, header values such as the topic or pattern that matched the message are synthetically added as headers.
- A `@Headers`-annotated argument that must also be assignable to `java.util.Map` for getting access to all headers.
- A non-annotated element that is not one of the supported types is considered to be the payload.
  You can make that explicit by annotating the parameter with `@Payload`.
  You can also turn on validation by adding an extra `@Valid`.

The ability to inject Spring’s `Message` abstraction is particularly useful to benefit from all the information stored in the transport-specific message without relying on transport-specific API.
The following example shows how to do so:

```java
@RedisListener("my-channel")
public void processOrder(Message<byte[]> order) { ... }
```

Handling of method arguments is provided by `DefaultMessageHandlerMethodFactory`, which you can further customize to support additional method arguments.
Annotated-based endpoints support flexible message conversion, which is provided by `RedisMessageConverters` along with a default set of converters for String, byte array, and JSON (if a supported library is present on the classpath).
If you wish to customize the message conversion, you can do so by implementing `RedisListenerConfigurer` and overriding the `configureMessageConverters` method, as the following example shows:

```java
@Configuration @EnableRedisListeners public class AppConfig implements RedisListenerConfigurer {
@Override public void configureMessageConverters(RedisMessageConverters.Builder builder) {builder.withStringConverter(StandardCharsets.UTF_8) .addCustomConverter(new JdkSerializationRedisSerializer());}}
```

[`RedisMessageConverters`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/serializer/RedisMessageConverters.html) registers by default the following converters:

- `StringMessageConverter`
- `ByteArrayMessageConverter`
- JSON converters (if a supported library like Jackson, Gson, JSON-B, or Kotlin Serialization is present on the classpath)

> [!NOTE]
> `RedisMessageConverters` uses Spring Data Redis’s RedisSerializers` for JSON serialization.
> Its JSON serialization format and behavior might slightly differ from Spring Messaging’s `JacksonJsonMessageConverter`.
> If you wish to use Spring Messaging’s variant then configure the desired converter through `Builder.addCustomConverter(MessageConverter)`.

`@RedisListener(consumes)` is useful to indicate the desired content type when using different message converters to select the appropriate converter.
The next example shows converter selection for the `JdkSerializationRedisSerializer` converter assuming a registration as per the previous example:

```java
@RedisListener(topic = "my-channel", consumes = JdkSerializerMessageConverter.APPLICATION_JAVA_SERIALIZED_OBJECT_VALUE)
public void processOrder(Person person) { ... }
```

> [!NOTE]
> Payload argument conversion for annotated endpoints that do not specify a content type will be processed by the first converter that can read the message payload.

If you require more control over the method argument resolution, you can also configure a custom `MessageHandlerMethodFactory` through `RedisListenerConfigurer`.
You can customize the conversion and validation support there as well.

For instance, if we want to make sure our `Order` is valid before processing it, we can annotate the payload with `@Valid` and configure the necessary validator, as the following example shows:

```java
@Configuration @EnableRedisListeners public class AppConfig implements RedisListenerConfigurer {
@Override public void configureRedisListeners(RedisListenerEndpointRegistrar registrar) {registrar.setMessageHandlerMethodFactory(myRedisHandlerMethodFactory());}
@Bean public DefaultMessageHandlerMethodFactory myRedisHandlerMethodFactory() {DefaultMessageHandlerMethodFactory factory = new DefaultMessageHandlerMethodFactory(); factory.setValidator(myValidator()); return factory;}}
```

---

<a id="redis-redis-streams"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-streams.html -->

<!-- page_index: 16 -->

# Redis Streams

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-streams--page-title"></a>
<a id="redis-redis-streams--redis-streams"></a>

# Redis Streams

Redis Streams model a log data structure in an abstract approach. Typically, logs are append-only data structures and are consumed from the beginning on, at a random position, or by streaming new messages.

> [!NOTE]
> Learn more about Redis Streams in the [Redis reference documentation](https://redis.io/topics/streams-intro).

Redis Streams can be roughly divided into two areas of functionality:

- Appending records
- Consuming records

Although this pattern has similarities to [Pub/Sub](#redis-pubsub), the main difference lies in the persistence of messages and how they are consumed.

While Pub/Sub relies on the broadcasting of transient messages (i.e. if you don’t listen, you miss a message), Redis Stream use a persistent, append-only data type that retains messages until the stream is trimmed. Another difference in consumption is that Pub/Sub registers a server-side subscription. Redis pushes arriving messages to the client while Redis Streams require active polling.

The `org.springframework.data.redis.connection` and `org.springframework.data.redis.stream` packages provide the core functionality for Redis Streams.

<a id="redis-redis-streams--redis.streams.send"></a>
<a id="redis-redis-streams--appending"></a>

## Appending

To send a record, you can use, as with the other operations, either the low-level `RedisConnection` or the high-level `StreamOperations`. Both entities offer the `add` (`xAdd`) method, which accepts the record and the destination stream as arguments. While `RedisConnection` requires raw data (array of bytes), the `StreamOperations` lets arbitrary objects be passed in as records, as shown in the following example:

```java
// append message through connection
RedisConnection con = …
byte[] stream = …
ByteRecord record = StreamRecords.rawBytes(…).withStreamKey(stream);
con.xAdd(record);

// append message through RedisTemplate
RedisTemplate template = …
StringRecord record = StreamRecords.string(…).withStreamKey("my-stream");
template.opsForStream().add(record);
```

Stream records carry a `Map`, key-value tuples, as their payload. Appending a record to a stream returns the `RecordId` that can be used as further reference.

<a id="redis-redis-streams--redis.streams.receive"></a>
<a id="redis-redis-streams--consuming"></a>

## Consuming

On the consuming side, one can consume one or multiple streams. Redis Streams provide read commands that allow consumption of the stream from an arbitrary position (random access) within the known stream content and beyond the stream end to consume new stream record.

At the low-level, `RedisConnection` offers the `xRead` and `xReadGroup` methods that map the Redis commands for reading and reading within a consumer group, respectively. Note that multiple streams can be used as arguments.

> [!NOTE]
> Subscription commands in Redis can be blocking. That is, calling `xRead` on a connection causes the current thread to block as it starts waiting for messages. The thread is released only if the read command times out or receives a message.

To consume stream messages, one can either poll for messages in application code, or use one of the two [Asynchronous reception through Message Listener Containers](#redis-redis-streams--redis.streams.receive.containers), the imperative or the reactive one. Each time a new records arrives, the container notifies the application code.

<a id="redis-redis-streams--redis.streams.receive.synchronous"></a>
<a id="redis-redis-streams--synchronous-reception"></a>

### Synchronous reception

While stream consumption is typically associated with asynchronous processing, it is possible to consume messages synchronously. The overloaded `StreamOperations.read(…)` methods provide this functionality. During a synchronous receive, the calling thread potentially blocks until a message becomes available. The property `StreamReadOptions.block` specifies how long the receiver should wait before giving up waiting for a message.

```java
// Read message through RedisTemplate
RedisTemplate template = …

List<MapRecord<K, HK, HV>> messages = template.opsForStream().read(StreamReadOptions.empty().count(2),
				StreamOffset.latest("my-stream"));

List<MapRecord<K, HK, HV>> messages = template.opsForStream().read(Consumer.from("my-group", "my-consumer"),
				StreamReadOptions.empty().count(2),
				StreamOffset.create("my-stream", ReadOffset.lastConsumed()))
```

<a id="redis-redis-streams--redis.streams.receive.containers"></a>
<a id="redis-redis-streams--asynchronous-reception-through-message-listener-containers"></a>

### Asynchronous reception through Message Listener Containers

Due to its blocking nature, low-level polling is not attractive, as it requires connection and thread management for every single consumer. To alleviate this problem, Spring Data offers message listeners, which do all the heavy lifting. If you are familiar with EJB and JMS, you should find the concepts familiar, as it is designed to be as close as possible to the support in Spring Framework and its message-driven POJOs (MDPs).

Spring Data ships with two implementations tailored to the used programming model:

- [`StreamMessageListenerContainer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/stream/StreamMessageListenerContainer.html) acts as message listener container for imperative programming models. It is used to consume records from a Redis Stream and drive the [`StreamListener`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/stream/StreamListener.html) instances that are injected into it.
- [`StreamReceiver`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/stream/StreamReceiver.html) provides a reactive variant of a message listener. It is used to consume messages from a Redis Stream as potentially infinite stream and emit stream messages through a `Flux`.

`StreamMessageListenerContainer` and `StreamReceiver` are responsible for all threading of message reception and dispatch into the listener for processing. A message listener container/receiver is the intermediary between an MDP and a messaging provider and takes care of registering to receive messages, resource acquisition and release, exception conversion, and the like. This lets you as an application developer write the (possibly complex) business logic associated with receiving a message (and reacting to it) and delegates boilerplate Redis infrastructure concerns to the framework.

Both containers allow runtime configuration changes so that you can add or remove subscriptions while an application is running without the need for a restart. Additionally, the container uses a lazy subscription approach, using a `RedisConnection` only when needed. If all the listeners are unsubscribed, it automatically performs a cleanup, and the thread is released.

<a id="redis-redis-streams--imperative-streammessagelistenercontainer"></a>

#### Imperative `StreamMessageListenerContainer`

In a fashion similar to a Message-Driven Bean (MDB) in the EJB world, the Stream-Driven POJO (SDP) acts as a receiver for Stream messages. The one restriction on an SDP is that it must implement the [`StreamListener`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/stream/StreamListener.html) interface. Please also be aware that in the case where your POJO receives messages on multiple threads, it is important to ensure that your implementation is thread-safe.

```java
class ExampleStreamListener implements StreamListener<String, MapRecord<String, String, String>> {
@Override public void onMessage(MapRecord<String, String, String> message) {
System.out.println("MessageId: " + message.getId()); System.out.println("Stream: " + message.getStream()); System.out.println("Body: " + message.getValue());}}
```

`StreamListener` represents a functional interface so implementations can be rewritten using their Lambda form:

```java
message -> {

    System.out.println("MessageId: " + message.getId());
    System.out.println("Stream: " + message.getStream());
    System.out.println("Body: " + message.getValue());
};
```

Once you’ve implemented your `StreamListener`, it’s time to create a message listener container and register a subscription:

```java
RedisConnectionFactory connectionFactory = …
StreamListener<String, MapRecord<String, String, String>> streamListener = …

StreamMessageListenerContainerOptions<String, MapRecord<String, String, String>> containerOptions = StreamMessageListenerContainerOptions
			.builder().pollTimeout(Duration.ofMillis(100)).build();

StreamMessageListenerContainer<String, MapRecord<String, String, String>> container = StreamMessageListenerContainer.create(connectionFactory,
				containerOptions);

Subscription subscription = container.receive(StreamOffset.fromStart("my-stream"), streamListener);
```

Please refer to the Javadoc of the various message listener containers for a full description of the features supported by each implementation.

<a id="redis-redis-streams--reactive-streamreceiver"></a>

#### Reactive `StreamReceiver`

Reactive consumption of streaming data sources typically happens through a `Flux` of events or messages. The reactive receiver implementation is provided with `StreamReceiver` and its overloaded `receive(…)` messages. The reactive approach requires fewer infrastructure resources such as threads in comparison to `StreamMessageListenerContainer` as it is leveraging threading resources provided by the driver. The receiving stream is a demand-driven publisher of `StreamMessage`:

```java
Flux<MapRecord<String, String, String>> messages = …

return messages.doOnNext(it -> {
    System.out.println("MessageId: " + message.getId());
    System.out.println("Stream: " + message.getStream());
    System.out.println("Body: " + message.getValue());
});
```

Now we need to create the `StreamReceiver` and register a subscription to consume stream messages:

```java
ReactiveRedisConnectionFactory connectionFactory = …

StreamReceiverOptions<String, MapRecord<String, String, String>> options = StreamReceiverOptions.builder().pollTimeout(Duration.ofMillis(100))
				.build();
StreamReceiver<String, MapRecord<String, String, String>> receiver = StreamReceiver.create(connectionFactory, options);

Flux<MapRecord<String, String, String>> messages = receiver.receive(StreamOffset.fromStart("my-stream"));
```

Please refer to the Javadoc of the various message listener containers for a full description of the features supported by each implementation.

> [!NOTE]
> Demand-driven consumption uses backpressure signals to activate and deactivate polling. `StreamReceiver` subscriptions pause polling if the demand is satisfied until subscribers signal further demand. Depending on the `ReadOffset` strategy, this can cause messages to be skipped.

<a id="redis-redis-streams--redis.streams.acknowledge"></a>
<a id="redis-redis-streams--acknowledge-strategies"></a>

### `Acknowledge` strategies

When you read with messages via a `Consumer Group`, the server will remember that a given message was delivered and add it to the Pending Entries List (PEL). A list of messages delivered but not yet acknowledged.
Messages have to be acknowledged via `StreamOperations.acknowledge` in order to be removed from the Pending Entries List as shown in the snippet below.

```java
StreamMessageListenerContainer<String, MapRecord<String, String, String>> container = ...

container.receive(Consumer.from("my-group", "my-consumer"), (1)
	StreamOffset.create("my-stream", ReadOffset.lastConsumed()),
    msg -> {

	    // ...
	    redisTemplate.opsForStream().acknowledge("my-group", msg); (2)
    });
```

**1**

Read as *my-consumer* from group *my-group*. Received messages are not acknowledged.

**2**

Acknowledged the message after processing.

> [!TIP]
> To auto acknowledge messages on receive use `receiveAutoAck` instead of `receive`.

<a id="redis-redis-streams--redis.streams.receive.readoffset"></a>
<a id="redis-redis-streams--readoffset-strategies"></a>

### `ReadOffset` strategies

Stream read operations accept a read offset specification to consume messages from the given offset on. `ReadOffset` represents the read offset specification. Redis supports 3 variants of offsets, depending on whether you consume the stream standalone or within a consumer group:

- `ReadOffset.latest()` – Read the latest message.
- `ReadOffset.from(…)` – Read after a specific message Id.
- `ReadOffset.lastConsumed()` – Read after the last consumed message Id (consumer-group only).

In the context of a message container-based consumption, we need to advance (or increment) the read offset when consuming a message. Advancing depends on the requested `ReadOffset` and consumption mode (with/without consumer groups). The following matrix explains how containers advance `ReadOffset`:

| Read offset | Standalone | Consumer Group |
| --- | --- | --- |
| Latest | Read latest message | Read latest message |
| Specific Message Id | Use last seen message as the next MessageId | Use last seen message as the next MessageId |
| Last Consumed | Use last seen message as the next MessageId | Last consumed message as per consumer group |

Reading from a specific message id and the last consumed message can be considered safe operations that ensure consumption of all messages that were appended to the stream.
Using the latest message for read can skip messages that were added to the stream while the poll operation was in the state of dead time. Polling introduces a dead time in which messages can arrive between individual polling commands. Stream consumption is not a linear contiguous read but split into repeating `XREAD` calls.

<a id="redis-redis-streams--redis.streams.receive.serialization"></a>
<a id="redis-redis-streams--serialization"></a>

## Serialization

Any Record sent to the stream needs to be serialized to its binary format. Due to the streams closeness to the hash data structure the stream key, field names and values use the according serializers configured on the `RedisTemplate`.

| Stream Property | Serializer | Description |
| --- | --- | --- |
| key | keySerializer | used for `Record#getStream()` |
| field | hashKeySerializer | used for each map key in the payload |
| value | hashValueSerializer | used for each map value in the payload |

Please make sure to review `RedisSerializer`s in use and note that if you decide to not use any serializer you need to make sure those values are binary already.

<a id="redis-redis-streams--redis.streams.hashing"></a>
<a id="redis-redis-streams--object-mapping"></a>

## Object Mapping

<a id="redis-redis-streams--simple-values"></a>

### Simple Values

`StreamOperations` allows to append simple values, via `ObjectRecord`, directly to the stream without having to put those values into a `Map` structure.
The value will then be assigned to an *payload* field and can be extracted when reading back the value.

```java
ObjectRecord<String, String> record = StreamRecords.newRecord()
    .in("my-stream")
    .ofObject("my-value");

redisTemplate()
    .opsForStream()
    .add(record); (1)

List<ObjectRecord<String, String>> records = redisTemplate()
    .opsForStream()
    .read(String.class, StreamOffset.fromStart("my-stream"));
```

**1**

XADD my-stream \* "\_class" "java.lang.String" "\_raw" "my-value"

`ObjectRecord`s pass through the very same serialization process as the all other records, thus the Record can also obtained using the untyped read operation returning a `MapRecord`.

<a id="redis-redis-streams--complex-values"></a>

### Complex Values

Adding a complex value to the stream can be done in 3 ways:

- Convert to simple value using e. g. a String JSON representation.
- Serialize the value with a suitable `RedisSerializer`.
- Convert the value into a `Map` suitable for serialization using a [`HashMapper`](#redis-hash-mappers).

The first variant is the most straight forward one but neglects the field value capabilities offered by the stream structure, still the values in the stream will be readable for other consumers.
The 2nd option holds the same benefits as the first one, but may lead to a very specific consumer limitations as the all consumers must implement the very same serialization mechanism.
The `HashMapper` approach is the a bit more complex one making use of the steams hash structure, but flattening the source. Still other consumers remain able to read the records as long as suitable serializer combinations are chosen.

> [!NOTE]
> [HashMappers](#redis-hash-mappers) convert the payload to a `Map` with specific types. Make sure to use Hash-Key and Hash-Value serializers that are capable of (de-)serializing the hash.

```java
ObjectRecord<String, User> record = StreamRecords.newRecord()
    .in("user-logon")
    .ofObject(new User("night", "angel"));

redisTemplate()
    .opsForStream()
    .add(record); (1)

List<ObjectRecord<String, User>> records = redisTemplate()
    .opsForStream()
    .read(User.class, StreamOffset.fromStart("user-logon"));
```

**1**

XADD user-logon \* "\_class" "com.example.User" "firstname" "night" "lastname" "angel"

`StreamOperations` use by default [ObjectHashMapper](#redis-redis-repositories-mapping).
You may provide a `HashMapper` suitable for your requirements when obtaining `StreamOperations`.

```java
redisTemplate()
    .opsForStream(new JacksonHashMapper(true))
    .add(record); (1)
```

**1**

XADD user-logon \* "firstname" "night" "@class" "com.example.User" "lastname" "angel"

> [!NOTE]
> A `StreamMessageListenerContainer` may not be aware of any `@TypeAlias` used on domain types as those need to be resolved through a `MappingContext`.
> Make sure to initialize `RedisMappingContext` with a `initialEntitySet`.
>
> ```java
> @Bean
> RedisMappingContext redisMappingContext() {
>     RedisMappingContext ctx = new RedisMappingContext();
>     ctx.setInitialEntitySet(Collections.singleton(Person.class));
>     return ctx;
> }
>
> @Bean
> RedisConverter redisConverter(RedisMappingContext mappingContext) {
>     return new MappingRedisConverter(mappingContext);
> }
>
> @Bean
> ObjectHashMapper hashMapper(RedisConverter converter) {
>     return new ObjectHashMapper(converter);
> }
>
> @Bean
> StreamMessageListenerContainer streamMessageListenerContainer(RedisConnectionFactory connectionFactory, ObjectHashMapper hashMapper) {
>     StreamMessageListenerContainerOptions<String, ObjectRecord<String, Object>> options = StreamMessageListenerContainerOptions.builder()
>             .objectMapper(hashMapper)
>             .build();
>
>     return StreamMessageListenerContainer.create(connectionFactory, options);
> }
> ```

---

<a id="redis-scripting"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/scripting.html -->

<!-- page_index: 17 -->

# Scripting

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-scripting--page-title"></a>
<a id="redis-scripting--scripting"></a>

# Scripting

Redis versions 2.6 and higher provide support for running Lua scripts through the [eval](https://redis.io/commands/eval) and [evalsha](https://redis.io/commands/evalsha) commands. Spring Data Redis provides a high-level abstraction for running scripts that handles serialization and automatically uses the Redis script cache.

Scripts can be run by calling the `execute` methods of `RedisTemplate` and `ReactiveRedisTemplate`. Both use a configurable [`ScriptExecutor`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/script/ScriptExecutor.html) (or [`ReactiveScriptExecutor`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/script/ReactiveScriptExecutor.html)) to run the provided script. By default, the [`ScriptExecutor`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/script/ScriptExecutor.html) (or [`ReactiveScriptExecutor`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/script/ReactiveScriptExecutor.html)) takes care of serializing the provided keys and arguments and deserializing the script result. This is done through the key and value serializers of the template. There is an additional overload that lets you pass custom serializers for the script arguments and the result.

The default [`ScriptExecutor`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/script/ScriptExecutor.html) optimizes performance by retrieving the SHA1 of the script and attempting first to run `evalsha`, falling back to `eval` if the script is not yet present in the Redis script cache.

The following example runs a common “check-and-set” scenario by using a Lua script. This is an ideal use case for a Redis script, as it requires that running a set of commands atomically, and the behavior of one command is influenced by the result of another.

```java
@Bean
public RedisScript<Boolean> script() {

  ScriptSource scriptSource = new ResourceScriptSource(new ClassPathResource("META-INF/scripts/checkandset.lua"));
  return RedisScript.of(scriptSource, Boolean.class);
}
```

- Imperative
- Reactive

```java
public class Example {
@Autowired RedisOperations<String, String> redisOperations;
@Autowired RedisScript<Boolean> script;
public boolean checkAndSet(String expectedValue, String newValue) {return redisOperations.execute(script, List.of("key"), expectedValue, newValue);}}
```

```java
public class Example {
@Autowired ReactiveRedisOperations<String, String> redisOperations;
@Autowired RedisScript<Boolean> script;
public Flux<Boolean> checkAndSet(String expectedValue, String newValue) {return redisOperations.execute(script, List.of("key"), expectedValue, newValue);}}
```

```lua
-- checkandset.lua
local current = redis.call('GET', KEYS[1])
if current == ARGV[1]
  then redis.call('SET', KEYS[1], ARGV[2])
  return true
end
return false
```

The preceding code configures a [`RedisScript`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/script/RedisScript.html) pointing to a file called `checkandset.lua`, which is expected to return a boolean value. The script `resultType` should be one of `Long`, `Boolean`, `List`, or a deserialized value type. It can also be `null` if the script returns a throw-away status (specifically, `OK`).

> [!TIP]
> It is ideal to configure a single instance of `DefaultRedisScript` in your application context to avoid re-calculation of the script’s SHA1 on every script run.

The `checkAndSet` method above then runs the scripts. Scripts can be run within a [`SessionCallback`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/SessionCallback.html) as part of a transaction or pipeline. See “[Redis Transactions](#redis-transactions)” and “[Pipelining](#redis-pipelining)” for more information.

The scripting support provided by Spring Data Redis also lets you schedule Redis scripts for periodic running by using the Spring Task and Scheduler abstractions. See the [Spring Framework](https://spring.io/projects/spring-framework/) documentation for more details.

---

<a id="redis-transactions"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/transactions.html -->

<!-- page_index: 18 -->

# Redis Transactions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-transactions--page-title"></a>
<a id="redis-transactions--redis-transactions"></a>

# Redis Transactions

Redis provides support for [transactions](https://redis.io/topics/transactions) through the `multi`, `exec`, and `discard` commands.
These operations are available on [`RedisTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisTemplate.html).
However, `RedisTemplate` is not guaranteed to run all the operations in the transaction with the same connection.

Spring Data Redis provides the [`SessionCallback`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/SessionCallback.html) interface for use when multiple operations need to be performed with the same `connection`, such as when using Redis transactions.The following example uses the `multi` method:

```java
//execute a transaction
List<Object> txResults = redisOperations.execute(new SessionCallback<List<Object>>() {
  public List<Object> execute(RedisOperations operations) throws DataAccessException {
    operations.multi();
    operations.opsForSet().add("key", "value1");

    // This will contain the results of all operations in the transaction
    return operations.exec();
  }
});
System.out.println("Number of items added to set: " + txResults.get(0));
```

`RedisTemplate` uses its value, hash key, and hash value serializers to deserialize all results of `exec` before returning.
There is an additional `exec` method that lets you pass a custom serializer for transaction results.

It is worth mentioning that in case between `multi()` and `exec()` an exception happens (e.g. a timeout exception in case Redis does not respond within the timeout) then the connection may get stuck in a transactional state.
To prevent such a situation need have to discard the transactional state to clear the connection:

```java
List<Object> txResults = redisOperations.execute(new SessionCallback<List<Object>>() {public List<Object> execute(RedisOperations operations) throws DataAccessException {boolean transactionStateIsActive = true; try {operations.multi(); operations.opsForSet().add("key", "value1");
// This will contain the results of all operations in the transaction return operations.exec(); } catch (RuntimeException e) {operations.discard(); throw e;}} });
```

<a id="redis-transactions--tx.spring"></a>
<a id="redis-transactions--transactional-support"></a>

## `@Transactional` Support

By default, `RedisTemplate` does not participate in managed Spring transactions.
If you want `RedisTemplate` to make use of Redis transaction when using `@Transactional` or `TransactionTemplate`, you need to be explicitly enable transaction support for each `RedisTemplate` by setting `setEnableTransactionSupport(true)`.
Enabling transaction support binds `RedisConnection` to the current transaction backed by a `ThreadLocal`.
If the transaction finishes without errors, the Redis transaction gets commited with `EXEC`, otherwise rolled back with `DISCARD`.
Redis transactions are batch-oriented.
Commands issued during an ongoing transaction are queued and only applied when committing the transaction.

Spring Data Redis distinguishes between read-only and write commands in an ongoing transaction.
Read-only commands, such as `KEYS`, are piped to a fresh (non-thread-bound) `RedisConnection` to allow reads.
Write commands are queued by `RedisTemplate` and applied upon commit.

The following example shows how to configure transaction management:

Example 1. Configuration enabling Transaction Management

```java
@Configuration @EnableTransactionManagement                                 (1) public class RedisTxContextConfiguration {
@Bean public StringRedisTemplate redisTemplate() {StringRedisTemplate template = new StringRedisTemplate(redisConnectionFactory()); // explicitly enable transaction support template.setEnableTransactionSupport(true);              (2) return template;}
@Bean public RedisConnectionFactory redisConnectionFactory() {// jedis || Lettuce}
@Bean public PlatformTransactionManager transactionManager() throws SQLException {return new DataSourceTransactionManager(dataSource());   (3)}
@Bean public DataSource dataSource() throws SQLException {// ...}}
```

<table>
<tr>
<td>1</td>
<td>Configures a Spring Context to enable <a href="https://docs.spring.io/spring-framework/reference/7.0/data-access.html#transaction-declarative">declarative transaction management</a>.</td>
</tr>
<tr>
<td>2</td>
<td>Configures <code>RedisTemplate</code> to participate in transactions by binding connections to the current thread.</td>
</tr>
<tr>
<td>3</td>
<td>Transaction management requires a <code>PlatformTransactionManager</code>.
Spring Data Redis does not ship with a <code>PlatformTransactionManager</code> implementation.
Assuming your application uses JDBC, Spring Data Redis can participate in transactions by using existing transaction managers.</td>
</tr>
</table>

The following examples each demonstrate a usage constraint:

Example 2. Usage Constraints

```java
// must be performed on thread-bound connection
template.opsForValue().set("thing1", "thing2");

// read operation must be run on a free (not transaction-aware) connection
template.keys("*");

// returns null as values set within a transaction are not visible
template.opsForValue().get("thing1");
```

---

<a id="redis-pipelining"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/pipelining.html -->

<!-- page_index: 19 -->

# Pipelining

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-pipelining--page-title"></a>
<a id="redis-pipelining--pipelining"></a>

# Pipelining

Redis provides support for [pipelining](https://redis.io/topics/pipelining), which involves sending multiple commands to the server without waiting for the replies and then reading the replies in a single step. Pipelining can improve performance when you need to send several commands in a row, such as adding many elements to the same List.

Spring Data Redis provides several `RedisTemplate` methods for running commands in a pipeline. If you do not care about the results of the pipelined operations, you can use the standard `execute` method, passing `true` for the `pipeline` argument. The `executePipelined` methods run the provided `RedisCallback` or `SessionCallback` in a pipeline and return the results, as shown in the following example:

```java
//pop a specified number of items from a queue List<Object> results = stringRedisTemplate.executePipelined(new RedisCallback<Object>() {public Object doInRedis(RedisConnection connection) throws DataAccessException {StringRedisConnection stringRedisConn = new DefaultStringRedisConnection(connection); for(int i=0; i< batchSize; i++) {stringRedisConn.rPop("myqueue");} return null;} });
```

The preceding example runs a bulk right pop of items from a queue in a pipeline.
The `results` `List` contains all the popped items. `RedisTemplate` uses its value, hash key, and hash value serializers to deserialize all results before returning, so the returned items in the preceding example are Strings.
There are additional `executePipelined` methods that let you pass a custom serializer for pipelined results.

Note that the value returned from the `RedisCallback` is required to be `null`, as this value is discarded in favor of returning the results of the pipelined commands.

> [!TIP]
> The Lettuce driver supports fine-grained flush control that allows to either flush commands as they appear, buffer or send them at connection close.
>
> ```java
> LettuceConnectionFactory factory = // ...
> factory.setPipeliningFlushPolicy(PipeliningFlushPolicy.buffered(3)); (1)
> ```
>
> **1**
>
> Buffer locally and flush after every 3rd command.

> [!NOTE]
> Pipelining is limited to Redis Standalone.
> Redis Cluster is currently only supported through the Lettuce driver except for the following commands when using cross-slot keys: `rename`, `renameNX`, `sort`, `bLPop`, `bRPop`, `rPopLPush`, `bRPopLPush`, `info`, `sMove`, `sInter`, `sInterStore`, `sUnion`, `sUnionStore`, `sDiff`, `sDiffStore`.
> Same-slot keys are fully supported.

---

<a id="redis-support-classes"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/support-classes.html -->

<!-- page_index: 20 -->

# Support Classes

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-support-classes--page-title"></a>
<a id="redis-support-classes--support-classes"></a>

# Support Classes

Package `org.springframework.data.redis.support` offers various reusable components that rely on Redis as a backing store.
Currently, the package contains various JDK-based interface implementations on top of Redis, such as [atomic](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/package-summary.html) counters and JDK [Collections](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html).

> [!NOTE]
> [`RedisList`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/support/collections/RedisList.html) is forward-compatible with Java 21 `SequencedCollection`.

The atomic counters make it easy to wrap Redis key incrementation while the collections allow easy management of Redis keys with minimal storage exposure or API leakage.
In particular, the [`RedisSet`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/support/collections/RedisSet.html) and [`RedisZSet`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/support/collections/RedisZSet.html) interfaces offer easy access to the set operations supported by Redis, such as `intersection` and `union`. [`RedisList`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/support/collections/RedisList.html) implements the `List`, `Queue`, and `Deque` contracts (and their equivalent blocking siblings) on top of Redis, exposing the storage as a FIFO (First-In-First-Out), LIFO (Last-In-First-Out) or capped collection with minimal configuration.
The following example shows the configuration for a bean that uses a [`RedisList`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/support/collections/RedisList.html):

- Java
- XML

```java
@Configuration class MyConfig {
// …
@Bean RedisList<String> stringRedisTemplate(RedisTemplate<String, String> redisTemplate) {return new DefaultRedisList<>(template, "queue-key");}}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:p="http://www.springframework.org/schema/p" xsi:schemaLocation="
  http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd">

  <bean id="queue" class="org.springframework.data.redis.support.collections.DefaultRedisList">
    <constructor-arg ref="redisTemplate"/>
    <constructor-arg value="queue-key"/>
  </bean>

</beans>
```

The following example shows a Java configuration example for a `Deque`:

```java
public class AnotherExample {
// injected private Deque<String> queue;
public void addTag(String tag) {queue.push(tag);}}
```

As shown in the preceding example, the consuming code is decoupled from the actual storage implementation.
In fact, there is no indication that Redis is used underneath.
This makes moving from development to production environments transparent and highly increases testability (the Redis implementation can be replaced with an in-memory one).

---

<a id="repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories.html -->

<!-- page_index: 21 -->

# Redis Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories--page-title"></a>
<a id="repositories--redis-repositories"></a>

# Redis Repositories

This chapter explains the basic foundations of Spring Data repositories and Redis specifics.
Before continuing to the Redis specifics, make sure you have a sound understanding of the basic concepts.

The goal of the Spring Data repository abstraction is to significantly reduce the amount of boilerplate code required to implement data access layers for various persistence stores.

Working with Redis Repositories lets you seamlessly convert and store domain objects in Redis Hashes, apply custom mapping strategies, and use secondary indexes.

> [!IMPORTANT]
> Redis Repositories require at least Redis Server version 2.8.0 and do not work with transactions.
> Make sure to use a `RedisTemplate` with [disabled transaction support](#redis-transactions--tx.spring).

<a id="repositories--section-summary"></a>

## Section Summary

- [Core concepts](#repositories-core-concepts)
- [Defining Repository Interfaces](#repositories-definition)
- [Creating Repository Instances](#repositories-create-instances)
- [Usage](#redis-redis-repositories-usage)
- [Object Mapping Fundamentals](#repositories-object-mapping)
- [Object-to-Hash Mapping](#redis-redis-repositories-mapping)
- [Keyspaces](#redis-redis-repositories-keyspaces)
- [Secondary Indexes](#redis-redis-repositories-indexes)
- [Time To Live](#redis-redis-repositories-expirations)
- [Redis-specific Query Methods](#redis-redis-repositories-queries)
- [Query by Example](#redis-redis-repositories-query-by-example)
- [Redis Repositories Running on a Cluster](#redis-redis-repositories-cluster)
- [Redis Repositories Anatomy](#redis-redis-repositories-anatomy)
- [Projections](#repositories-projections)
- [Custom Repository Implementations](#repositories-custom-implementations)
- [Publishing Events from Aggregate Roots](#repositories-core-domain-events)
- [Null Handling of Repository Methods](#repositories-null-handling)
- [CDI Integration](#redis-redis-repositories-cdi-integration)
- [Repository query keywords](#repositories-query-keywords-reference)
- [Repository query return types](#repositories-query-return-types-reference)

---

<a id="repositories-core-concepts"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/core-concepts.html -->

<!-- page_index: 22 -->

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
> Read more about this in “[Defining Query Methods](https://docs.spring.io/spring-data/redis/reference/repositories/query-methods-details.html#repositories.query-methods.reserved-methods)”.
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

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/definition.html -->

<!-- page_index: 23 -->

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

<a id="repositories-create-instances"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/create-instances.html -->

<!-- page_index: 24 -->

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

Use the store-specific `@EnableRedisRepositories` annotation on a Java configuration class to define a configuration for repository activation.
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

The `basePackages` and `value` attributes in `@EnableRedisRepositories` support `${…}` property placeholders which are resolved against the `Environment` as well as Ant-style package patterns such as `"org.example.**"`.

The following example specifies the `app.scan.packages` property placeholder for the implicit `value` attribute in `@EnableRedisRepositories`.

- Java
- Kotlin

```java
@Configuration
@EnableRedisRepositories("${app.scan.packages}")    (1)
public class ApplicationConfiguration {
  // …
}
```

**1**

`app.scan.packages` property placeholder to be resolved against the `Environment`

```kotlin
@EnableRedisRepositories(["\${app.scan.packages}"]) (1)
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
@EnableRedisRepositories(basePackages = "com.acme.repositories",
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

<a id="redis-redis-repositories-usage"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/usage.html -->

<!-- page_index: 25 -->

# Usage

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-usage--page-title"></a>
<a id="redis-redis-repositories-usage--usage"></a>

# Usage

Spring Data Redis lets you easily implement domain entities, as shown in the following example:

Example 1. Sample Person Entity

```java
@RedisHash("people")
public class Person {

  @Id String id;
  String firstname;
  String lastname;
  Address address;
}
```

We have a pretty simple domain object here.
Note that it has a `@RedisHash` annotation on its type and a property named `id` that is annotated with `org.springframework.data.annotation.Id`.
Those two items are responsible for creating the actual key used to persist the hash.

> [!NOTE]
> Properties annotated with `@Id` as well as those named `id` are considered as the identifier properties.
> Those with the annotation are favored over others.

To now actually have a component responsible for storage and retrieval, we need to define a repository interface, as shown in the following example:

Example 2. Basic Repository Interface To Persist Person Entities

```java
public interface PersonRepository extends CrudRepository<Person, String> {

}
```

As our repository extends `CrudRepository`, it provides basic CRUD and finder operations.
The thing we need in between to glue things together is the corresponding Spring configuration, shown in the following example:

Example 3. JavaConfig for Redis Repositories

```java
@Configuration @EnableRedisRepositories public class ApplicationConfig {
@Bean public RedisConnectionFactory connectionFactory() {return new LettuceConnectionFactory();}
@Bean public RedisTemplate<?, ?> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
RedisTemplate<byte[], byte[]> template = new RedisTemplate<byte[], byte[]>(); template.setConnectionFactory(redisConnectionFactory); return template;}}
```

Given the preceding setup, we can inject `PersonRepository` into our components, as shown in the following example:

Example 4. Access to Person Entities

```java
@Autowired PersonRepository repo;

public void basicCrudOperations() {

  Person rand = new Person("rand", "al'thor");
  rand.setAddress(new Address("emond's field", "andor"));

  repo.save(rand);                                         (1)

  repo.findOne(rand.getId());                              (2)

  repo.count();                                            (3)

  repo.delete(rand);                                       (4)
}
```

**1**

Generates a new `id` if the current value is `null` or reuses an already set `id` value and stores properties of type `Person` inside the Redis Hash with a key that has a pattern of `keyspace:id` — in this case, it might be `people:5d67b7e1-8640-present-beeb-c666fab4c0e5`.

**2**

Uses the provided `id` to retrieve the object stored at `keyspace:id`.

**3**

Counts the total number of entities available within the keyspace, `people`, defined by `@RedisHash` on `Person`.

**4**

Removes the key for the given object from Redis.

<a id="redis-redis-repositories-usage--redis.repositories.references"></a>
<a id="redis-redis-repositories-usage--persisting-references"></a>

## Persisting References

Marking properties with `@Reference` allows storing a simple key reference instead of copying values into the hash itself.
On loading from Redis, references are resolved automatically and mapped back into the object, as shown in the following example:

Example 5. Sample Property Reference

```text
_class = org.example.Person
id = e2c7dcee-b8cd-4424-883e-736ce564363e
firstname = rand
lastname = al’thor
mother = people:a9d4b3a0-50d3-4538-a2fc-f7fc2581ee56      (1)
```

**1**

Reference stores the whole key (`keyspace:id`) of the referenced object.

> [!WARNING]
> Referenced Objects are not persisted when the referencing object is saved.
> You must persist changes on referenced objects separately, since only the reference is stored.
> Indexes set on properties of referenced types are not resolved.

<a id="redis-redis-repositories-usage--redis.repositories.partial-updates"></a>
<a id="redis-redis-repositories-usage--persisting-partial-updates"></a>

## Persisting Partial Updates

In some cases, you need not load and rewrite the entire entity just to set a new value within it.
A session timestamp for the last active time might be such a scenario where you want to alter one property.
`PartialUpdate` lets you define `set` and `delete` actions on existing objects while taking care of updating potential expiration times of both the entity itself and index structures.
The following example shows a partial update:

Example 6. Sample Partial Update

```java
PartialUpdate<Person> update = new PartialUpdate<Person>("e2c7dcee", Person.class)
  .set("firstname", "mat")                                                           (1)
  .set("address.city", "emond's field")                                              (2)
  .del("age");                                                                       (3)

template.update(update);

update = new PartialUpdate<Person>("e2c7dcee", Person.class)
  .set("address", new Address("caemlyn", "andor"))                                   (4)
  .set("attributes", singletonMap("eye-color", "grey"));                             (5)

template.update(update);

update = new PartialUpdate<Person>("e2c7dcee", Person.class)
  .refreshTtl(true);                                                                 (6)
  .set("expiration", 1000);

template.update(update);
```

| **1** | Set the simple `firstname` property to `mat`. |
| --- | --- |
| **2** | Set the simple 'address.city' property to 'emond’s field' without having to pass in the entire object. This does not work when a custom conversion is registered. |
| **3** | Remove the `age` property. |
| **4** | Set complex `address` property. |
| **5** | Set a map of values, which removes the previously existing map and replaces the values with the given ones. |
| **6** | Automatically update the server expiration time when altering [Time To Live](#redis-redis-repositories-expirations). |

> [!NOTE]
> Updating complex objects as well as map (or other collection) structures requires further interaction with Redis to determine existing values, which means that rewriting the entire entity might be faster.

---

<a id="repositories-object-mapping"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/object-mapping.html -->

<!-- page_index: 26 -->

# Object Mapping Fundamentals

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-object-mapping--page-title"></a>
<a id="repositories-object-mapping--object-mapping-fundamentals"></a>

# Object Mapping Fundamentals

This section covers the fundamentals of Spring Data object mapping, object creation, field and property access, mutability and immutability.
Note, that this section only applies to Spring Data modules that do not use the object mapping of the underlying data store (like JPA).
Also be sure to consult the store-specific sections for store-specific object mapping, like indexes, customizing column or field names or the like.

Core responsibility of the Spring Data object mapping is to create instances of domain objects and map the store-native data structures onto those.
This means we need two fundamental steps:

1. Instance creation by using one of the constructors exposed.
2. Instance population to materialize all exposed properties.

<a id="repositories-object-mapping--mapping.object-creation"></a>
<a id="repositories-object-mapping--object-creation"></a>

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

<a id="repositories-object-mapping--mapping.property-population"></a>
<a id="repositories-object-mapping--property-population"></a>

## Property population

Once an instance of the entity has been created, Spring Data populates all remaining persistent properties of that class.
Unless already populated by the entity’s constructor (i.e. consumed through its constructor argument list), the identifier property will be populated first to allow the resolution of cyclic object references.
After that, all non-transient properties that have not already been populated by the constructor are set on the entity instance.
For that we use the following algorithm:

1. If the property is immutable but exposes a `with…` method (see below), we use the `with…` method to create a new entity instance with the new property value.
2. If property access (i.e. access through getters and setters) is defined, we’re invoking the setter method.
3. If the property is mutable we set the field directly.
4. If the property is immutable we’re using the constructor to be used by persistence operations (see [Object creation](#repositories-object-mapping--mapping.object-creation)) to create a copy of the instance.
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

<a id="repositories-object-mapping--mapping.general-recommendations"></a>
<a id="repositories-object-mapping--general-recommendations"></a>

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

<a id="repositories-object-mapping--mapping.general-recommendations.override.properties"></a>
<a id="repositories-object-mapping--overriding-properties"></a>

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

<a id="repositories-object-mapping--mapping.kotlin"></a>
<a id="repositories-object-mapping--kotlin-support"></a>

## Kotlin support

Spring Data adapts specifics of Kotlin to allow object creation and mutation.

<a id="repositories-object-mapping--mapping.kotlin.creation"></a>
<a id="repositories-object-mapping--kotlin-object-creation"></a>

### Kotlin object creation

Kotlin classes are supported to be instantiated, all classes are immutable by default and require explicit property declarations to define mutable properties.

Spring Data automatically tries to detect a persistent entity’s constructor to be used to materialize objects of that type.
The resolution algorithm works as follows:

1. If there is a constructor that is annotated with `@PersistenceCreator`, it is used.
2. If the type is a [Kotlin data class](#repositories-object-mapping--mapping.kotlin) the primary constructor is used.
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

<a id="repositories-object-mapping--property-population-of-kotlin-data-classes"></a>

### Property population of Kotlin data classes

In Kotlin, all classes are immutable by default and require explicit property declarations to define mutable properties.
Consider the following `data` class `Person`:

```kotlin
data class Person(val id: String, val name: String)
```

This class is effectively immutable.
It allows creating new instances as Kotlin generates a `copy(…)` method that creates new object instances copying all property values from the existing object and applying property values provided as arguments to the method.

<a id="repositories-object-mapping--mapping.kotlin.override.properties"></a>
<a id="repositories-object-mapping--kotlin-overriding-properties"></a>

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

<a id="repositories-object-mapping--mapping.kotlin.value.classes"></a>
<a id="repositories-object-mapping--kotlin-value-classes"></a>

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

<a id="redis-redis-repositories-mapping"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/mapping.html -->

<!-- page_index: 27 -->

# Object-to-Hash Mapping

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-mapping--page-title"></a>
<a id="redis-redis-repositories-mapping--object-to-hash-mapping"></a>

# Object-to-Hash Mapping

The Redis Repository support persists Objects to Hashes.
This requires an Object-to-Hash conversion which is done by a `RedisConverter`.
The default implementation uses `Converter` for mapping property values to and from Redis native `byte[]`.

Given the `Person` type from the previous sections, the default mapping looks like the following:

```text
_class = org.example.Person                 (1)
id = e2c7dcee-b8cd-4424-883e-736ce564363e
firstname = rand                            (2)
lastname = al’thor
address.city = emond's field                (3)
address.country = andor
```

**1**

The `_class` attribute is included on the root level as well as on any nested interface or abstract types.

**2**

Simple property values are mapped by path.

**3**

Properties of complex types are mapped by their dot path.

<a id="redis-redis-repositories-mapping--mapping-conversion"></a>
<a id="redis-redis-repositories-mapping--data-mapping-and-type-conversion"></a>

## Data Mapping and Type Conversion

This section explains how types are mapped to and from a Hash representation:

| Type | Sample | Mapped Value |
| --- | --- | --- |
| Simple Type (for example, String) | String firstname = "rand"; | firstname = "rand" |
| Byte array (`byte[]`) | byte[] image = "rand".getBytes(); | image = "rand" |
| Complex Type (for example, Address) | Address address = new Address("emond’s field"); | address.city = "emond’s field" |
| List of Simple Type | List<String> nicknames = asList("dragon reborn", "lews therin"); | nicknames.[0] = "dragon reborn", nicknames.[1] = "lews therin" |
| Map of Simple Type | Map<String, String> atts = asMap({"eye-color", "grey"}, {"… | atts.[eye-color] = "grey", atts.[hair-color] = "… |
| List of Complex Type | List<Address> addresses = asList(new Address("em… | addresses.[0].city = "emond’s field", addresses.[1].city = "… |
| Map of Complex Type | Map<String, Address> addresses = asMap({"home", new Address("em… | addresses.[home].city = "emond’s field", addresses.[work].city = "… |

> [!WARNING]
> Due to the flat representation structure, Map keys need to be simple types, such as `String` or `Number`.

Mapping behavior can be customized by registering the corresponding `Converter` in `RedisCustomConversions`.
Those converters can take care of converting from and to a single `byte[]` as well as `Map<String, byte[]>`.
The first one is suitable for (for example) converting a complex type to (for example) a binary JSON representation that still uses the default mappings hash structure.
The second option offers full control over the resulting hash.

> [!WARNING]
> Writing objects to a Redis hash deletes the content from the hash and re-creates the whole hash, so data that has not been mapped is lost.

The following example shows two sample byte array converters:

Example 1. Sample byte[] Converters

```java
@WritingConverter public class AddressToBytesConverter implements Converter<Address, byte[]> {
private final JacksonJsonRedisSerializer<Address> serializer;
public AddressToBytesConverter() {
serializer = new JacksonJsonRedisSerializer<Address>(Address.class); serializer.setObjectMapper(new ObjectMapper());}
@Override public byte[] convert(Address value) {return serializer.serialize(value);}}
@ReadingConverter public class BytesToAddressConverter implements Converter<byte[], Address> {
private final JacksonJsonRedisSerializer<Address> serializer;
public BytesToAddressConverter() {
serializer = new JacksonJsonRedisSerializer<Address>(Address.class); serializer.setObjectMapper(new ObjectMapper());}
@Override public Address convert(byte[] value) {return serializer.deserialize(value);}}
```

Using the preceding byte array `Converter` produces output similar to the following:

```text
_class = org.example.Person
id = e2c7dcee-b8cd-4424-883e-736ce564363e
firstname = rand
lastname = al’thor
address = { city : "emond's field", country : "andor" }
```

The following example shows two examples of `Map` converters:

Example 2. Sample Map<String, byte[]> Converters

```java
@WritingConverter public class AddressToMapConverter implements Converter<Address, Map<String, byte[]>> {
@Override public Map<String, byte[]> convert(Address source) {return singletonMap("ciudad", source.getCity().getBytes());}}
@ReadingConverter public class MapToAddressConverter implements Converter<Map<String, byte[]>, Address> {
@Override public Address convert(Map<String, byte[]> source) {return new Address(new String(source.get("ciudad")));}}
```

Using the preceding Map `Converter` produces output similar to the following:

```text
_class = org.example.Person
id = e2c7dcee-b8cd-4424-883e-736ce564363e
firstname = rand
lastname = al’thor
ciudad = "emond's field"
```

> [!NOTE]
> Custom conversions have no effect on index resolution. [Secondary Indexes](#redis-redis-repositories-indexes) are still created, even for custom converted types.

<a id="redis-redis-repositories-mapping--customizing-type-mapping"></a>

## Customizing Type Mapping

If you want to avoid writing the entire Java class name as type information and would rather like to use a key, you can use the `@TypeAlias` annotation on the entity class being persisted.
If you need to customize the mapping even more, look at the [`TypeInformationMapper`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/convert/TypeInformationMapper.html) interface.
An instance of that interface can be configured at the `DefaultRedisTypeMapper`, which can be configured on `MappingRedisConverter`.

The following example shows how to define a type alias for an entity:

Example 3. Defining `@TypeAlias` for an entity

```java
@TypeAlias("pers")
class Person {

}
```

The resulting document contains `pers` as the value in a `_class` field.

<a id="redis-redis-repositories-mapping--configuring-custom-type-mapping"></a>

### Configuring Custom Type Mapping

The following example demonstrates how to configure a custom `RedisTypeMapper` in `MappingRedisConverter`:

Example 4. Configuring a custom `RedisTypeMapper` via Spring Java Config

```java
class CustomRedisTypeMapper extends DefaultRedisTypeMapper {
  //implement custom type mapping here
}
```

```java
@Configuration
class SampleRedisConfiguration {

  @Bean
  public MappingRedisConverter redisConverter(RedisMappingContext mappingContext,
        RedisCustomConversions customConversions, ReferenceResolver referenceResolver) {

    MappingRedisConverter mappingRedisConverter = new MappingRedisConverter(mappingContext, null, referenceResolver,
            customTypeMapper());

    mappingRedisConverter.setCustomConversions(customConversions);

    return mappingRedisConverter;
  }

  @Bean
  public RedisTypeMapper customTypeMapper() {
    return new CustomRedisTypeMapper();
  }
}
```

---

<a id="redis-redis-repositories-keyspaces"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/keyspaces.html -->

<!-- page_index: 28 -->

# Keyspaces

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-keyspaces--page-title"></a>
<a id="redis-redis-repositories-keyspaces--keyspaces"></a>

# Keyspaces

Keyspaces define prefixes used to create the actual key for the Redis Hash.
By default, the prefix is set to `getClass().getName()`.
You can alter this default by setting `@RedisHash` on the aggregate root level or by setting up a programmatic configuration.
However, the annotated keyspace supersedes any other configuration.

The following example shows how to set the keyspace configuration with the `@EnableRedisRepositories` annotation:

Example 1. Keyspace Setup via `@EnableRedisRepositories`

```java
@Configuration @EnableRedisRepositories(keyspaceConfiguration = MyKeyspaceConfiguration.class) public class ApplicationConfig {
//... RedisConnectionFactory and RedisTemplate Bean definitions omitted
public static class MyKeyspaceConfiguration extends KeyspaceConfiguration {
@Override protected Iterable<KeyspaceSettings> initialConfiguration() {return Collections.singleton(new KeyspaceSettings(Person.class, "people"));}}}
```

The following example shows how to programmatically set the keyspace:

Example 2. Programmatic Keyspace setup

```java
@Configuration @EnableRedisRepositories public class ApplicationConfig {
//... RedisConnectionFactory and RedisTemplate Bean definitions omitted
@Bean public RedisMappingContext keyValueMappingContext() {return new RedisMappingContext(new MappingConfiguration(new IndexConfiguration(), new MyKeyspaceConfiguration()));}
public static class MyKeyspaceConfiguration extends KeyspaceConfiguration {
@Override protected Iterable<KeyspaceSettings> initialConfiguration() {return Collections.singleton(new KeyspaceSettings(Person.class, "people"));}}}
```

---

<a id="redis-redis-repositories-indexes"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/indexes.html -->

<!-- page_index: 29 -->

# Secondary Indexes

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-indexes--page-title"></a>
<a id="redis-redis-repositories-indexes--secondary-indexes"></a>

# Secondary Indexes

[Secondary indexes](https://redis.io/topics/indexes) are used to enable lookup operations based on native Redis structures.
Values are written to the according indexes on every save and are removed when objects are deleted or [expire](#redis-redis-repositories-expirations).

<a id="redis-redis-repositories-indexes--redis.repositories.indexes.simple"></a>
<a id="redis-redis-repositories-indexes--simple-property-index"></a>

## Simple Property Index

Given the sample `Person` entity shown earlier, we can create an index for `firstname` by annotating the property with `@Indexed`, as shown in the following example:

Example 1. Annotation driven indexing

```java
@RedisHash("people")
public class Person {

  @Id String id;
  @Indexed String firstname;
  String lastname;
  Address address;
}
```

Indexes are built up for actual property values.
Saving two Persons (for example, "rand" and "aviendha") results in setting up indexes similar to the following:

```text
SADD people:firstname:rand e2c7dcee-b8cd-4424-883e-736ce564363e
SADD people:firstname:aviendha a9d4b3a0-50d3-4538-a2fc-f7fc2581ee56
```

It is also possible to have indexes on nested elements.
Assume `Address` has a `city` property that is annotated with `@Indexed`.
In that case, once `person.address.city` is not `null`, we have Sets for each city, as shown in the following example:

```text
SADD people:address.city:tear e2c7dcee-b8cd-4424-883e-736ce564363e
```

Furthermore, the programmatic setup lets you define indexes on map keys and list properties, as shown in the following example:

```java
@RedisHash("people")
public class Person {

  // ... other properties omitted

  Map<String, String> attributes;     (1)
  Map<String, Person> relatives;      (2)
  List<Address> addresses;            (3)
}
```

| **1** | `SADD people:attributes.map-key:map-value e2c7dcee-b8cd-4424-883e-736ce564363e` |
| --- | --- |
| **2** | `SADD people:relatives.map-key.firstname:tam e2c7dcee-b8cd-4424-883e-736ce564363e` |
| **3** | `SADD people:addresses.city:tear e2c7dcee-b8cd-4424-883e-736ce564363e` |

> [!WARNING]
> Indexes cannot be resolved on [References](#redis-redis-repositories-usage--redis.repositories.references).

As with keyspaces, you can configure indexes without needing to annotate the actual domain type, as shown in the following example:

Example 2. Index Setup with @EnableRedisRepositories

```java
@Configuration @EnableRedisRepositories(indexConfiguration = MyIndexConfiguration.class) public class ApplicationConfig {
//... RedisConnectionFactory and RedisTemplate Bean definitions omitted
public static class MyIndexConfiguration extends IndexConfiguration {
@Override protected Iterable<IndexDefinition> initialConfiguration() {return Collections.singleton(new SimpleIndexDefinition("people", "firstname"));}}}
```

Again, as with keyspaces, you can programmatically configure indexes, as shown in the following example:

Example 3. Programmatic Index setup

```java
@Configuration @EnableRedisRepositories public class ApplicationConfig {
//... RedisConnectionFactory and RedisTemplate Bean definitions omitted
@Bean public RedisMappingContext keyValueMappingContext() {return new RedisMappingContext(new MappingConfiguration(new KeyspaceConfiguration(), new MyIndexConfiguration()));}
public static class MyIndexConfiguration extends IndexConfiguration {
@Override protected Iterable<IndexDefinition> initialConfiguration() {return Collections.singleton(new SimpleIndexDefinition("people", "firstname"));}}}
```

<a id="redis-redis-repositories-indexes--redis.repositories.indexes.geospatial"></a>
<a id="redis-redis-repositories-indexes--geospatial-index"></a>

## Geospatial Index

Assume the `Address` type contains a `location` property of type `Point` that holds the geo coordinates of the particular address.
By annotating the property with `@GeoIndexed`, Spring Data Redis adds those values by using Redis `GEO` commands, as shown in the following example:

```java
@RedisHash("people")
public class Person {

  Address address;

  // ... other properties omitted
}

public class Address {

  @GeoIndexed Point location;

  // ... other properties omitted
}

public interface PersonRepository extends CrudRepository<Person, String> {

  List<Person> findByAddressLocationNear(Point point, Distance distance);     (1)
  List<Person> findByAddressLocationWithin(Circle circle);                    (2)
}

Person rand = new Person("rand", "al'thor");
rand.setAddress(new Address(new Point(13.361389D, 38.115556D)));

repository.save(rand);                                                        (3)

repository.findByAddressLocationNear(new Point(15D, 37D), new Distance(200, Metrics.KILOMETERS)); (4)
```

| **1** | Query method declaration on a nested property, using `Point` and `Distance`. |
| --- | --- |
| **2** | Query method declaration on a nested property, using `Circle` to search within. |
| **3** | `GEOADD people:address:location 13.361389 38.115556 e2c7dcee-b8cd-4424-883e-736ce564363e` |
| **4** | `GEORADIUS people:address:location 15.0 37.0 200.0 km` |

In the preceding example the, longitude and latitude values are stored by using `GEOADD` that use the object’s `id` as the member’s name.
The finder methods allow usage of `Circle` or `Point, Distance` combinations for querying those values.

> [!NOTE]
> It is **not** possible to combine `near` and `within` with other criteria.

---

<a id="redis-redis-repositories-expirations"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/expirations.html -->

<!-- page_index: 30 -->

# Time To Live

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-expirations--page-title"></a>
<a id="redis-redis-repositories-expirations--time-to-live"></a>

# Time To Live

Objects stored in Redis may be valid only for a certain amount of time.
This is especially useful for persisting short-lived objects in Redis without having to remove them manually when they reach their end of life.
The expiration time in seconds can be set with `@RedisHash(timeToLive=…)` as well as by using [`KeyspaceConfiguration.KeyspaceSettings`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/convert/KeyspaceConfiguration.KeyspaceSettings.html) (see [Keyspaces](#redis-redis-repositories-keyspaces)).

More flexible expiration times can be set by using the `@TimeToLive` annotation on either a numeric property or a method.
However, do not apply `@TimeToLive` on both a method and a property within the same class.
The following example shows the `@TimeToLive` annotation on a property and on a method:

Example 1. Expirations

```java
public class TimeToLiveOnProperty {
@Id private String id;
@TimeToLive private Long expiration;}
public class TimeToLiveOnMethod {
@Id private String id;
@TimeToLive public long getTimeToLive() {return new Random().nextLong();}}
```

> [!NOTE]
> Annotating a property explicitly with `@TimeToLive` reads back the actual `TTL` or `PTTL` value from Redis. `-1` indicates that the object has no associated expiration.

The repository implementation ensures subscription to [Redis keyspace notifications](https://redis.io/topics/notifications) via [`RedisMessageListenerContainer`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/listener/RedisMessageListenerContainer.html).

When the expiration is set to a positive value, the corresponding `EXPIRE` command is run.
In addition to persisting the original, a phantom copy is persisted in Redis and set to expire five minutes after the original one.
This is done to enable the Repository support to publish [`RedisKeyExpiredEvent`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisKeyExpiredEvent.html), holding the expired value in Spring’s `ApplicationEventPublisher` whenever a key expires, even though the original values have already been removed.
Expiry events are received on all connected applications that use Spring Data Redis repositories.

By default, the key expiry listener is disabled when initializing the application.
The startup mode can be adjusted in `@EnableRedisRepositories` or `RedisKeyValueAdapter` to start the listener with the application or upon the first insert of an entity with a TTL.
See [`RedisKeyValueAdapter.EnableKeyspaceEvents`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisKeyValueAdapter.EnableKeyspaceEvents.html) for possible values.

The `RedisKeyExpiredEvent` holds a copy of the expired domain object as well as the key.

> [!NOTE]
> Delaying or disabling the expiry event listener startup impacts `RedisKeyExpiredEvent` publishing.
> A disabled event listener does not publish expiry events.
> A delayed startup can cause loss of events because of the delayed listener initialization.

> [!NOTE]
> The keyspace notification message listener alters `notify-keyspace-events` settings in Redis, if those are not already set.
> Existing settings are not overridden, so you must set up those settings correctly (or leave them empty).
> Note that `CONFIG` is disabled on AWS ElastiCache, and enabling the listener leads to an error.
> To work around this behavior, set the `keyspaceNotificationsConfigParameter` parameter to an empty string.
> This prevents `CONFIG` command usage.

> [!NOTE]
> Redis repositories rely on Pub/Sub messages for residual index cleanup.
> Redis Pub/Sub messages are not persistent.
> If a key expires while the application is down, the expiry event is not processed, which may lead to secondary indexes containing references to the expired object.
> Redis does not allow for expiration of individual entries of a set that is used as secondary index.

> [!NOTE]
> `@EnableKeyspaceEvents(shadowCopy = OFF)` disable storage of phantom copies and reduces data size within Redis. `RedisKeyExpiredEvent` will only contain the `id` of the expired key.

---

<a id="redis-redis-repositories-queries"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/queries.html -->

<!-- page_index: 31 -->

# Redis-specific Query Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-queries--page-title"></a>
<a id="redis-redis-repositories-queries--redis-specific-query-methods"></a>

# Redis-specific Query Methods

Query methods allow automatic derivation of simple finder queries from the method name, as shown in the following example:

Example 1. Sample Repository finder Method

```java
public interface PersonRepository extends CrudRepository<Person, String> {

  List<Person> findByFirstname(String firstname);
}
```

> [!NOTE]
> Please make sure properties used in finder methods are set up for indexing.

> [!NOTE]
> Query methods for Redis repositories support only queries for entities and collections of entities with paging.

Using derived query methods might not always be sufficient to model the queries to run. `RedisCallback` offers more control over the actual matching of index structures or even custom indexes.
To do so, provide a `RedisCallback` that returns a single or `Iterable` set of `id` values, as shown in the following example:

Example 2. Sample finder using RedisCallback

```java
String user = //...

List<RedisSession> sessionsByUser = template.find(new RedisCallback<Set<byte[]>>() {

  public Set<byte[]> doInRedis(RedisConnection connection) throws DataAccessException {
    return connection
      .sMembers("sessions:securityContext.authentication.principal.username:" + user);
  }}, RedisSession.class);
```

The following table provides an overview of the keywords supported for Redis and what a method containing that keyword essentially translates to:

| Keyword | Sample | Redis snippet |
| --- | --- | --- |
| `And` | `findByLastnameAndFirstname` | `SINTER …:firstname:rand …:lastname:al’thor` |
| `Or` | `findByLastnameOrFirstname` | `SUNION …:firstname:rand …:lastname:al’thor` |
| `Is, Equals` | `findByFirstname`, `findByFirstnameIs`, `findByFirstnameEquals` | `SINTER …:firstname:rand` |
| `IsTrue` | `FindByAliveIsTrue` | `SINTER …:alive:1` |
| `IsFalse` | `findByAliveIsFalse` | `SINTER …:alive:0` |
| `Top,First` | `findFirst10ByFirstname`,`findTop5ByFirstname` |  |

<a id="redis-redis-repositories-queries--redis.repositories.queries.sort"></a>
<a id="redis-redis-repositories-queries--sorting-query-method-results"></a>

## Sorting Query Method results

Redis repositories allow various approaches to define sorting order.
Redis itself does not support in-flight sorting when retrieving hashes or sets.
Therefore, Redis repository query methods construct a `Comparator` that is applied to the result before returning results as `List`.
Let’s take a look at the following example:

Example 3. Sorting Query Results

```java
interface PersonRepository extends RedisRepository<Person, String> {

  List<Person> findByFirstnameOrderByAgeDesc(String firstname); (1)

  List<Person> findByFirstname(String firstname, Sort sort);   (2)
}
```

**1**

Static sorting derived from method name.

**2**

Dynamic sorting using a method argument.

---

<a id="redis-redis-repositories-query-by-example"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/query-by-example.html -->

<!-- page_index: 32 -->

# Query by Example

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-query-by-example--page-title"></a>
<a id="redis-redis-repositories-query-by-example--query-by-example"></a>

# Query by Example

<a id="redis-redis-repositories-query-by-example--query-by-example.introduction"></a>
<a id="redis-redis-repositories-query-by-example--introduction"></a>

## Introduction

This chapter provides an introduction to Query by Example and explains how to use it.

Query by Example (QBE) is a user-friendly querying technique with a simple interface.
It allows dynamic query creation and does not require you to write queries that contain field names.
In fact, Query by Example does not require you to write queries by using store-specific query languages at all.

> [!NOTE]
> This chapter explains the core concepts of Query by Example.
> The information is pulled from the Spring Data Commons module.
> Depending on your database, String matching support can be limited.

<a id="redis-redis-repositories-query-by-example--query-by-example.usage"></a>
<a id="redis-redis-repositories-query-by-example--usage"></a>

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
> Properties using primitive types (`int`, `double`, …) are always included unless the [`ExampleMatcher` ignores the property path](#redis-redis-repositories-query-by-example--query-by-example.matchers).

Examples can be built by either using the `of` factory method or by using [`ExampleMatcher`](#redis-redis-repositories-query-by-example--query-by-example.matchers). `Example` is immutable.
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

<a id="redis-redis-repositories-query-by-example--query-by-example.matchers"></a>
<a id="redis-redis-repositories-query-by-example--example-matchers"></a>

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

<a id="redis-redis-repositories-query-by-example--query-by-example.fluent"></a>
<a id="redis-redis-repositories-query-by-example--fluent-api"></a>

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

<a id="redis-redis-repositories-query-by-example--query-by-example.running"></a>
<a id="redis-redis-repositories-query-by-example--running-an-example"></a>

## Running an Example

The following example uses Query by Example against a repository:

Example 5. Query by Example using a Repository

```java
interface PersonRepository extends ListQueryByExampleExecutor<Person> {}
class PersonService {
@Autowired PersonRepository personRepository;
List<Person> findPeople(Person probe) {return personRepository.findAll(Example.of(probe));}}
```

Redis Repositories support, with their secondary indexes, a subset of Spring Data’s Query by Example features.
In particular, only exact, case-sensitive, and non-null values are used to construct a query.

Secondary indexes use set-based operations (Set intersection, Set union) to determine matching keys. Adding a property to the query that is not indexed returns no result, because no index exists. Query by Example support inspects indexing configuration to include only properties in the query that are covered by an index. This is to prevent accidental inclusion of non-indexed properties.

Case-insensitive queries and unsupported `StringMatcher` instances are rejected at runtime.

The following list shows the supported Query by Example options:

- Case-sensitive, exact matching of simple and nested properties
- Any/All match modes
- Value transformation of the criteria value
- Exclusion of `null` values from the criteria

The following list shows properties not supported by Query by Example:

- Case-insensitive matching
- Regex, prefix/contains/suffix String-matching
- Querying of Associations, Collection, and Map-like properties
- Inclusion of `null` values from the criteria
- `findAll` with sorting

---

<a id="redis-redis-repositories-cluster"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/cluster.html -->

<!-- page_index: 33 -->

# Redis Repositories Running on a Cluster

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-cluster--page-title"></a>
<a id="redis-redis-repositories-cluster--redis-repositories-running-on-a-cluster"></a>

# Redis Repositories Running on a Cluster

You can use the Redis repository support in a clustered Redis environment.
See the “[Redis Cluster](#redis-cluster)” section for `ConnectionFactory` configuration details.
Still, some additional configuration must be done, because the default key distribution spreads entities and secondary indexes through out the whole cluster and its slots.

The following table shows the details of data on a cluster (based on previous examples):

| Key | Type | Slot | Node |
| --- | --- | --- | --- |
| people:e2c7dcee-b8cd-4424-883e-736ce564363e | id for hash | 15171 | 127.0.0.1:7381 |
| people:a9d4b3a0-50d3-4538-a2fc-f7fc2581ee56 | id for hash | 7373 | 127.0.0.1:7380 |
| people:firstname:rand | index | 1700 | 127.0.0.1:7379 |

Some commands (such as `SINTER` and `SUNION`) can only be processed on the server side when all involved keys map to the same slot.
Otherwise, computation has to be done on client side.
Therefore, it is useful to pin keyspaces to a single slot, which lets make use of Redis server side computation right away.
The following table shows what happens when you do (note the change in the slot column and the port value in the node column):

| Key | Type | Slot | Node |
| --- | --- | --- | --- |
| {people}:e2c7dcee-b8cd-4424-883e-736ce564363e | id for hash | 2399 | 127.0.0.1:7379 |
| {people}:a9d4b3a0-50d3-4538-a2fc-f7fc2581ee56 | id for hash | 2399 | 127.0.0.1:7379 |
| {people}:firstname:rand | index | 2399 | 127.0.0.1:7379 |

> [!TIP]
> Define and pin keyspaces by using `@RedisHash("{yourkeyspace}")` to specific slots when you use Redis cluster.

---

<a id="redis-redis-repositories-anatomy"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/anatomy.html -->

<!-- page_index: 34 -->

# Redis Repositories Anatomy

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-anatomy--page-title"></a>
<a id="redis-redis-repositories-anatomy--redis-repositories-anatomy"></a>

# Redis Repositories Anatomy

Redis as a store itself offers a very narrow low-level API leaving higher level functions, such as secondary indexes and query operations, up to the user.

This section provides a more detailed view of commands issued by the repository abstraction for a better understanding of potential performance implications.

Consider the following entity class as the starting point for all operations:

Example 1. Example entity

```java
@RedisHash("people")
public class Person {

  @Id String id;
  @Indexed String firstname;
  String lastname;
  Address hometown;
}

public class Address {

  @GeoIndexed Point location;
}
```

<a id="redis-redis-repositories-anatomy--redis.repositories.anatomy.insert"></a>
<a id="redis-redis-repositories-anatomy--insert-new"></a>

## Insert new

```java
repository.save(new Person("rand", "al'thor"));
```

```text
HMSET "people:19315449-cda2-4f5c-b696-9cb8018fa1f9" "_class" "Person" "id" "19315449-cda2-4f5c-b696-9cb8018fa1f9" "firstname" "rand" "lastname" "al'thor" (1)
SADD  "people" "19315449-cda2-4f5c-b696-9cb8018fa1f9"                           (2)
SADD  "people:firstname:rand" "19315449-cda2-4f5c-b696-9cb8018fa1f9"            (3)
SADD  "people:19315449-cda2-4f5c-b696-9cb8018fa1f9:idx" "people:firstname:rand" (4)
```

| **1** | Save the flattened entry as hash. |
| --- | --- |
| **2** | Add the key of the hash written in <1> to the helper index of entities in the same keyspace. |
| **3** | Add the key of the hash written in <2> to the secondary index of firstnames with the properties value. |
| **4** | Add the index of <3> to the set of helper structures for entry to keep track of indexes to clean on delete/update. |

<a id="redis-redis-repositories-anatomy--redis.repositories.anatomy.replace"></a>
<a id="redis-redis-repositories-anatomy--replace-existing"></a>

## Replace existing

```java
repository.save(new Person("e82908cf-e7d3-47c2-9eec-b4e0967ad0c9", "Dragon Reborn", "al'thor"));
```

```text
DEL       "people:e82908cf-e7d3-47c2-9eec-b4e0967ad0c9"                           (1)
HMSET     "people:e82908cf-e7d3-47c2-9eec-b4e0967ad0c9" "_class" "Person" "id" "e82908cf-e7d3-47c2-9eec-b4e0967ad0c9" "firstname" "Dragon Reborn" "lastname" "al'thor" (2)
SADD      "people" "e82908cf-e7d3-47c2-9eec-b4e0967ad0c9"                         (3)
SMEMBERS  "people:e82908cf-e7d3-47c2-9eec-b4e0967ad0c9:idx"                       (4)
TYPE      "people:firstname:rand"                                                 (5)
SREM      "people:firstname:rand" "e82908cf-e7d3-47c2-9eec-b4e0967ad0c9"          (6)
DEL       "people:e82908cf-e7d3-47c2-9eec-b4e0967ad0c9:idx"                       (7)
SADD      "people:firstname:Dragon Reborn" "e82908cf-e7d3-47c2-9eec-b4e0967ad0c9" (8)
SADD      "people:e82908cf-e7d3-47c2-9eec-b4e0967ad0c9:idx" "people:firstname:Dragon Reborn" (9)
```

**1**

Remove the existing hash to avoid leftovers of hash keys potentially no longer present.

**2**

Save the flattened entry as hash.

**3**

Add the key of the hash written in <1> to the helper index of entities in the same keyspace.

**4**

Get existing index structures that might need to be updated.

**5**

Check if the index exists and what type it is (text, geo, …).

**6**

Remove a potentially existing key from the index.

**7**

Remove the helper holding index information.

**8**

Add the key of the hash added in <2> to the secondary index of firstnames with the properties value.

**9**

Add the index of <6> to the set of helper structures for entry to keep track of indexes to clean on delete/update.

<a id="redis-redis-repositories-anatomy--redis.repositories.anatomy.geo"></a>
<a id="redis-redis-repositories-anatomy--save-geo-data"></a>

## Save Geo Data

Geo indexes follow the same rules as normal text based ones but use geo structure to store values.
Saving an entity that uses a Geo-indexed property results in the following commands:

```text
GEOADD "people:hometown:location" "13.361389" "38.115556" "76900e94-b057-44bc-abcf-8126d51a621b"  (1)
SADD   "people:76900e94-b057-44bc-abcf-8126d51a621b:idx" "people:hometown:location"               (2)
```

**1**

Add the key of the saved entry to the the geo index.

**2**

Keep track of the index structure.

<a id="redis-redis-repositories-anatomy--redis.repositories.anatomy.index"></a>
<a id="redis-redis-repositories-anatomy--find-using-simple-index"></a>

## Find using simple index

```java
repository.findByFirstname("egwene");
```

```text
SINTER  "people:firstname:egwene"                     (1)
HGETALL "people:d70091b5-0b9a-4c0a-9551-519e61bc9ef3" (2)
HGETALL ...
```

**1**

Fetch keys contained in the secondary index.

**2**

Fetch each key returned by <1> individually.

<a id="redis-redis-repositories-anatomy--redis.repositories.anatomy.geo-index"></a>
<a id="redis-redis-repositories-anatomy--find-using-geo-index"></a>

## Find using Geo Index

```java
repository.findByHometownLocationNear(new Point(15, 37), new Distance(200, KILOMETERS));
```

```text
GEORADIUS "people:hometown:location" "15.0" "37.0" "200.0" "km" (1)
HGETALL   "people:76900e94-b057-44bc-abcf-8126d51a621b"         (2)
HGETALL   ...
```

**1**

Fetch keys contained in the secondary index.

**2**

Fetch each key returned by <1> individually.

---

<a id="repositories-projections"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/projections.html -->

<!-- page_index: 35 -->

# Projections

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-projections--page-title"></a>
<a id="repositories-projections--projections"></a>

# Projections

<a id="repositories-projections--projections-2"></a>

## Projections

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

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/custom-implementations.html -->

<!-- page_index: 36 -->

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
Fragments are the base repository, functional aspects (such as [Querydsl](https://docs.spring.io/spring-data/redis/reference/repositories/core-extensions.html#core.extensions.querydsl)), and custom interfaces along with their implementations.
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
@EnableRedisRepositories(repositoryImplementationPostfix = "MyPostfix")
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
@EnableRedisRepositories(repositoryBaseClass = MyRepositoryImpl.class)
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

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/core-domain-events.html -->

<!-- page_index: 37 -->

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

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/null-handling.html -->

<!-- page_index: 38 -->

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

<a id="redis-redis-repositories-cdi-integration"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/redis/redis-repositories/cdi-integration.html -->

<!-- page_index: 39 -->

# CDI Integration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="redis-redis-repositories-cdi-integration--page-title"></a>
<a id="redis-redis-repositories-cdi-integration--cdi-integration"></a>

# CDI Integration

Instances of the repository interfaces are usually created by a container, for which Spring is the most natural choice when working with Spring Data.
Spring offers sophisticated for creating bean instances.
Spring Data Redis ships with a custom CDI extension that lets you use the repository abstraction in CDI environments.
The extension is part of the JAR, so, to activate it, drop the Spring Data Redis JAR into your classpath.

You can then set up the infrastructure by implementing a CDI Producer for the [`RedisConnectionFactory`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/connection/RedisConnectionFactory.html) and [`RedisOperations`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisOperations.html), as shown in the following example:

```java
class RedisOperationsProducer {
@Produces RedisConnectionFactory redisConnectionFactory() {
LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory(new RedisStandaloneConfiguration()); connectionFactory.afterPropertiesSet(); connectionFactory.start();
return connectionFactory;}
void disposeRedisConnectionFactory(@Disposes RedisConnectionFactory redisConnectionFactory) throws Exception {
if (redisConnectionFactory instanceof DisposableBean) {((DisposableBean) redisConnectionFactory).destroy();}}
@Produces @ApplicationScoped RedisOperations<byte[], byte[]> redisOperationsProducer(RedisConnectionFactory redisConnectionFactory) {
RedisTemplate<byte[], byte[]> template = new RedisTemplate<byte[], byte[]>(); template.setConnectionFactory(redisConnectionFactory); template.afterPropertiesSet();
return template;}
}
```

The necessary setup can vary, depending on your JavaEE environment.

The Spring Data Redis CDI extension picks up all available repositories as CDI beans and creates a proxy for a Spring Data repository whenever a bean of a repository type is requested by the container.
Thus, obtaining an instance of a Spring Data repository is a matter of declaring an `@Injected` property, as shown in the following example:

```java
class RepositoryClient {
@Inject PersonRepository repository;
public void businessMethod() {List<Person> people = repository.findAll();}}
```

A Redis Repository requires [`RedisKeyValueAdapter`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisKeyValueAdapter.html) and [`RedisKeyValueTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisKeyValueTemplate.html) instances.
These beans are created and managed by the Spring Data CDI extension if no provided beans are found.
You can, however, supply your own beans to configure the specific properties of [`RedisKeyValueAdapter`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisKeyValueAdapter.html) and [`RedisKeyValueTemplate`](https://docs.spring.io/spring-data/redis/reference/api/java/org/springframework/data/redis/core/RedisKeyValueTemplate.html).

---

<a id="repositories-query-keywords-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/query-keywords-reference.html -->

<!-- page_index: 40 -->

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
See also “[Defining Query Methods](https://docs.spring.io/spring-data/redis/reference/repositories/query-methods-details.html#repositories.query-methods.reserved-methods)”.

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

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/repositories/query-return-types-reference.html -->

<!-- page_index: 41 -->

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
| Types that implement `Streamable` and take a `Streamable` constructor or factory method argument | Types that expose a constructor or `….of(…)`/`….valueOf(…)` factory method taking a `Streamable` as argument. See [Returning Custom Streamable Wrapper Types](https://docs.spring.io/spring-data/redis/reference/repositories/query-methods-details.html#repositories.collections-and-iterables.streamable-wrapper) for details. |
| Vavr `Seq`, `List`, `Map`, `Set` | Vavr collection types. See [Support for Vavr Collections](https://docs.spring.io/spring-data/redis/reference/repositories/query-methods-details.html#repositories.collections-and-iterables.vavr) for details. |
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

<a id="observability"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/observability.html -->

<!-- page_index: 42 -->

# Observability

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="observability--page-title"></a>
<a id="observability--observability"></a>

# Observability

Getting insights from an application component about its operations, timing and relation to application code is crucial to understand latency.
Lettuce ships with a Micrometer integration to collect observations during Redis interaction.
Once the integration is set up, Micrometer will create meters and spans (for distributed tracing) for each Redis command.

We recommend using Spring Boot with its Redis auto-configuration to enable metrics and tracing spans for Redis commands.

<a id="observability--redis.observability.configuration"></a>
<a id="observability--configuration-code"></a>

## Configuration Code

If you are not using Spring Boot or you want to fully customize `ClientResources` or the tracing configuration, you can set up the integration manually.
To enable the integration, apply the following configuration to `LettuceClientConfiguration`:

```java
@Configuration
class ObservabilityConfiguration {

  @Bean
  public ClientResources clientResources(ObservationRegistry observationRegistry) {

    return ClientResources.builder()
              .tracing(new MicrometerTracing(observationRegistry, "my-redis-cache"))
              .build();
  }

  @Bean
  public LettuceConnectionFactory lettuceConnectionFactory(ClientResources clientResources) {

    LettuceClientConfiguration clientConfig = LettuceClientConfiguration.builder()
                                                .clientResources(clientResources).build();
    RedisConfiguration redisConfiguration = …;
    return new LettuceConnectionFactory(redisConfiguration, clientConfig);
  }
}
```

See also for further reference:
\* [Lettuce Tracing](https://redis.github.io/lettuce/advanced-usage/observability/#tracing)
\* [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/database/#redis) .

---

<a id="appendix"></a>

<!-- source_url: https://docs.spring.io/spring-data/redis/reference/appendix.html -->

<!-- page_index: 43 -->

# Appendix

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix--page-title"></a>
<a id="appendix--appendix"></a>

# Appendix

<a id="appendix--schema"></a>

## Schema

[Spring Data Redis Schema (redis-namespace)](https://www.springframework.org/schema/redis/spring-redis-1.0.xsd)

<a id="appendix--supported-commands"></a>

## Supported Commands

| Command | Template Support |
| --- | --- |
| APPEND | X |
| AUTH | X |
| BGREWRITEAOF | X |
| BGSAVE | X |
| BITCOUNT | X |
| BITFIELD | X |
| BITOP | X |
| BLPOP | X |
| BRPOP | X |
| BRPOPLPUSH | X |
| CLIENT KILL | X |
| CLIENT GETNAME | X |
| CLIENT LIST | X |
| CLIENT SETNAME | X |
| CLUSTER SLOTS | - |
| COMMAND | - |
| COMMAND COUNT | - |
| COMMAND GETKEYS | - |
| COMMAND INFO | - |
| CONFIG GET | X |
| CONFIG RESETSTAT | X |
| CONFIG REWRITE | - |
| CONFIG SET | X |
| DBSIZE | X |
| DEBUG OBJECT | - |
| DEBUG SEGFAULT | - |
| DECR | X |
| DECRBY | X |
| DEL | X |
| DISCARD | X |
| DUMP | X |
| ECHO | X |
| EVAL | X |
| EVALSHA | X |
| EXEC | X |
| EXISTS | X |
| EXPIRE | X |
| EXPIREAT | X |
| FLUSHALL | X |
| FLUSHDB | X |
| GEOADD | X |
| GEODIST | X |
| GEOHASH | X |
| GEOPOS | X |
| GEORADIUS | X |
| GEORADIUSBYMEMBER | X |
| GEOSEARCH | X |
| GEOSEARCHSTORE | X |
| GET | X |
| GETBIT | X |
| GETRANGE | X |
| GETSET | X |
| HDEL | X |
| HEXISTS | X |
| HEXPIRE | X |
| HEXPIREAT | X |
| HPEXPIRE | X |
| HPEXPIREAT | X |
| HPERSIST | X |
| HTTL | X |
| HPTTL | X |
| HGET | X |
| HGETALL | X |
| HINCRBY | X |
| HINCRBYFLOAT | X |
| HKEYS | X |
| HLEN | X |
| HMGET | X |
| HMSET | X |
| HSCAN | X |
| HSET | X |
| HSETNX | X |
| HVALS | X |
| INCR | X |
| INCRBY | X |
| INCRBYFLOAT | X |
| INFO | X |
| KEYS | X |
| LASTSAVE | X |
| LINDEX | X |
| LINSERT | X |
| LLEN | X |
| LPOP | X |
| LPUSH | X |
| LPUSHX | X |
| LRANGE | X |
| LREM | X |
| LSET | X |
| LTRIM | X |
| MGET | X |
| MIGRATE | - |
| MONITOR | - |
| MOVE | X |
| MSET | X |
| MSETNX | X |
| MULTI | X |
| OBJECT | - |
| PERSIST | X |
| PEXIPRE | X |
| PEXPIREAT | X |
| PFADD | X |
| PFCOUNT | X |
| PFMERGE | X |
| PING | X |
| PSETEX | X |
| PSUBSCRIBE | X |
| PTTL | X |
| PUBLISH | X |
| PUBSUB | - |
| PUBSUBSCRIBE | - |
| QUIT | X |
| RANDOMKEY | X |
| RENAME | X |
| RENAMENX | X |
| REPLICAOF | X |
| RESTORE | X |
| ROLE | - |
| RPOP | X |
| RPOPLPUSH | X |
| RPUSH | X |
| RPUSHX | X |
| SADD | X |
| SAVE | X |
| SCAN | X |
| SCARD | X |
| SCRIPT EXITS | X |
| SCRIPT FLUSH | X |
| SCRIPT KILL | X |
| SCRIPT LOAD | X |
| SDIFF | X |
| SDIFFSTORE | X |
| SELECT | X |
| SENTINEL FAILOVER | X |
| SENTINEL GET-MASTER-ADD-BY-NAME | - |
| SENTINEL MASTER | - |
| SENTINEL MASTERS | X |
| SENTINEL MONITOR | X |
| SENTINEL REMOVE | X |
| SENTINEL RESET | - |
| SENTINEL SET | - |
| SENTINEL SLAVES | X |
| SET | X |
| SETBIT | X |
| SETEX | X |
| SETNX | X |
| SETRANGE | X |
| SHUTDOWN | X |
| SINTER | X |
| SINTERSTORE | X |
| SISMEMBER | X |
| SLAVEOF | X |
| SLOWLOG | - |
| SMEMBERS | X |
| SMOVE | X |
| SORT | X |
| SPOP | X |
| SRANDMEMBER | X |
| SREM | X |
| SSCAN | X |
| STRLEN | X |
| SUBSCRIBE | X |
| SUNION | X |
| SUNIONSTORE | X |
| SYNC | - |
| TIME | X |
| TTL | X |
| TYPE | X |
| UNSUBSCRIBE | X |
| UNWATCH | X |
| WATCH | X |
| XACK | X |
| XACKDEL | X |
| XADD | X |
| XAUTOCLAIM | X |
| XCLAIM | X |
| XDEL | X |
| XDELEX | X |
| XGROUP | X |
| XINFO | X |
| XLEN | X |
| XPENDING | X |
| XRANGE | X |
| XREAD | X |
| XREADGROUP | X |
| XREVRANGE | X |
| XTRIM | X |
| ZADD | X |
| ZCARD | X |
| ZCOUNT | X |
| ZINCRBY | X |
| ZINTERSTORE | X |
| ZLEXCOUNT | - |
| ZRANGE | X |
| ZRANGEBYLEX | - |
| ZREVRANGEBYLEX | - |
| ZRANGEBYSCORE | X |
| ZRANGESTORE | X |
| ZRANK | X |
| ZREM | X |
| ZREMRANGEBYLEX | - |
| ZREMRANGEBYRANK | X |
| ZREVRANGE | X |
| ZREVRANGEBYSCORE | X |
| ZREVRANK | X |
| ZSCAN | X |
| ZSCORE | X |
| ZUNINONSTORE | X |

---
