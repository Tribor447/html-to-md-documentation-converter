# Overview

## Navigation

- [Overview](#index)
  
- [Overview](#index)
  
- [What’s new?](#whats-new)
  
- [Introduction](#introduction)
    
- [Quick Tour](#quick-tour)
  
- [Reference](#reference)
    
- [Using Spring for Apache Kafka](#kafka)
      
- [Connecting to Kafka](#kafka-connecting)
      
- [Configuring Topics](#kafka-configuring-topics)
      
- [Sending Messages](#kafka-sending-messages)
      
- [Receiving Messages](#kafka-receiving-messages)
        
- [Message Listeners](#kafka-receiving-messages-message-listeners)
        
- [Message Listener Containers](#kafka-receiving-messages-message-listener-container)
        
- [Manually Committing Offsets](#kafka-receiving-messages-ooo-commits)
        
- [Asynchronous @KafkaListener Return Types](#kafka-receiving-messages-async-returns)
        
- [@KafkaListener Annotation](#kafka-receiving-messages-listener-annotation)
        
- [Obtaining the Consumer group.id](#kafka-receiving-messages-listener-group-id)
        
- [Container Thread Naming](#kafka-receiving-messages-container-thread-naming)
        
- [@KafkaListener as a Meta Annotation](#kafka-receiving-messages-listener-meta)
        
- [@KafkaListener on a Class](#kafka-receiving-messages-class-level-kafkalistener)
        
- [@KafkaListener Attribute Modification](#kafka-receiving-messages-kafkalistener-attrs)
        
- [@KafkaListener Lifecycle Management](#kafka-receiving-messages-kafkalistener-lifecycle)
        
- [@KafkaListener @Payload Validation](#kafka-receiving-messages-validation)
        
- [Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners)
        
- [Enforcing Consumer Rebalance](#kafka-receiving-messages-enforced-rebalance)
        
- [Forwarding Listener Results using @SendTo](#kafka-receiving-messages-annotation-send-to)
        
- [Filtering Messages](#kafka-receiving-messages-filtering)
        
- [Retrying Deliveries](#kafka-receiving-messages-retrying-deliveries)
        
- [Starting @KafkaListener s in Sequence](#kafka-receiving-messages-sequencing)
        
- [Using KafkaTemplate to Receive](#kafka-receiving-messages-template-receive)
      
- [Listener Container Properties](#kafka-container-props)
      
- [Dynamically Creating Containers](#kafka-dynamic-containers)
      
- [Application Events](#kafka-events)
      
- [Topic/Partition Initial Offset](#kafka-topic-partition-initial-offset)
      
- [Seeking to a Specific Offset](#kafka-seek)
      
- [Container factory](#kafka-container-factory)
      
- [Thread Safety](#kafka-thread-safety)
      
- [Monitoring](#kafka-micrometer)
      
- [Transactions](#kafka-transactions)
      
- [Exactly Once Semantics](#kafka-exactly-once)
      
- [Wiring Spring Beans into Producer/Consumer Interceptors](#kafka-interceptors)
      
- [Producer Interceptor Managed in Spring](#kafka-producer-interceptor-managed-in-spring)
      
- [Pausing and Resuming Listener Containers](#kafka-pause-resume)
      
- [Pausing and Resuming Partitions on Listener Containers](#kafka-pause-resume-partitions)
      
- [Serialization, Deserialization, and Message Conversion](#kafka-serdes)
      
- [Message Headers](#kafka-headers)
      
- [Null Payloads and Log Compaction of 'Tombstone' Records](#kafka-tombstones)
      
- [Handling Exceptions](#kafka-annotation-error-handling)
      
- [JAAS and Kerberos](#kafka-kerberos)
      
- [Kafka Queues (Share Consumer)](#kafka-kafka-queues)
    
- [Non-Blocking Retries](#retrytopic)
      
- [How the Pattern Works](#retrytopic-how-the-pattern-works)
      
- [Back Off Delay Precision](#retrytopic-back-off-delay-precision)
      
- [Configuration](#retrytopic-retry-config)
      
- [Programmatic Construction](#retrytopic-programmatic-construction)
      
- [Features](#retrytopic-features)
      
- [Combining Blocking and Non-Blocking Retries](#retrytopic-retry-topic-combine-blocking)
      
- [Accessing Delivery Attempts](#retrytopic-accessing-delivery-attempts)
      
- [Topic Naming](#retrytopic-topic-naming)
      
- [Multiple Listeners, Same Topic(s)](#retrytopic-multi-retry)
      
- [DLT Strategies](#retrytopic-dlt-strategies)
      
- [Specifying a ListenerContainerFactory](#retrytopic-retry-topic-lcf)
      
- [Accessing Topics' Information at Runtime](#retrytopic-access-topic-info-runtime)
      
- [Changing KafkaBackOffException Logging Level](#retrytopic-change-kboe-logging-level)
    
- [Apache Kafka Streams Support](#streams)
    
- [Testing Applications](#testing)
  
- [Tips, Tricks and Examples](#tips)
  
- [Other Resources](#other-resources)
  
- [Override Spring Boot Dependencies](#appendix-override-boot-dependencies)
  
- [Micrometer Observation Documentation](#appendix-micrometer)
  
- [Native Images](#appendix-native-images)
  
- [Change History](#appendix-change-history)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/index.html -->

<!-- page_index: 1 -->

<a id="index--page-title"></a>
<a id="index--overview"></a>

# Overview

**4.1.0**

The Spring for Apache Kafka project applies core Spring concepts to the development of Kafka-based messaging solutions.
We provide a “template” as a high-level abstraction for sending messages.
We also provide support for Message-driven POJOs.

[What’s new?](#whats-new)

---

<a id="whats-new"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/whats-new.html -->

<!-- page_index: 2 -->

# What’s new?

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="whats-new--page-title"></a>
<a id="whats-new--what-s-new"></a>

# What’s new?

<a id="whats-new--whats-new-in-4-1-since-4.0"></a>
<a id="whats-new--what-s-new-in-4.1-since-4.0"></a>

## What’s New in 4.1 Since 4.0

This section covers the changes made from version 4.0 to version 4.1.
For changes in earlier versions, see [Change History](#appendix-change-history).

<a id="whats-new--x41-kafka-listener-ack-mode"></a>
<a id="whats-new--kafkalistener-changes"></a>

### `@KafkaListener` Changes

The `@KafkaListener` annotation now supports an `ackMode` attribute, allowing individual listeners to override the container factory’s default acknowledgment mode without creating separate container factory beans.
The attribute also supports SpEL expressions and property placeholders.
See [`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation) for more information.

<a id="whats-new--x41-share-ack-mode"></a>
<a id="whats-new--share-consumer-acknowledgment-modes"></a>

### Share Consumer Acknowledgment Modes

The boolean `setExplicitShareAcknowledgment(boolean)` property on `ContainerProperties` has been replaced by the `ShareAckMode` enum (`EXPLICIT`, `MANUAL`, `IMPLICIT`).
The deprecated method still works: `true` maps to `MANUAL`, `false` maps to `EXPLICIT`.
Default behavior is unchanged — applications using the default require no migration.
See [Record Acknowledgment](#kafka-kafka-queues--share-record-acknowledgment) for mode descriptions and [Migration from 4.0](#kafka-kafka-queues--share-ack-mode-migration) for upgrade details.

<a id="whats-new--x41-share-sync-async-commits"></a>
<a id="whats-new--share-consumer-async-commits"></a>

### Share Consumer Async Commits

A new `syncShareCommits` property on `ContainerProperties` controls whether the share container uses `commitSync()` (default) or `commitAsync()` for acknowledgment commits.
Set to `false` for higher throughput when slight ack-durability lag is acceptable.
See [Synchronous vs Asynchronous Commits](#kafka-kafka-queues--share-sync-async-commits) for details.

<a id="whats-new--x41-share-consumer-error-handling"></a>
<a id="whats-new--share-consumer-error-handling"></a>

### Share Consumer Error Handling

Share consumer containers now provide configurable error handling:

- **Poll-level**: `RecordDeserializationException` and `CorruptRecordException` from `poll()` are caught so the consumer thread continues; undeserializable records are REJECTed and the next poll proceeds.
- **Listener-level**: A `ShareConsumerRecordRecoverer` interface decides whether to ACCEPT, RELEASE, or REJECT when the listener throws.
  The default is `ShareConsumerRecordRecoverer.REJECTING`; `RELEASING` is also available.
  You can set a custom recoverer on the factory or container.
- See [Share consumer error handling](#kafka-kafka-queues--share-error-handling) in the Kafka Queues documentation.

<a id="whats-new--x41-share-consumer-lifecycle-events"></a>
<a id="whats-new--share-consumer-lifecycle-events"></a>

### Share Consumer Lifecycle Events

`ShareKafkaMessageListenerContainer` now publishes stop and failure lifecycle events in addition to `ConsumerStartingEvent` and `ConsumerStartedEvent`:

- `ShareConsumerStoppingEvent` (new): published before the underlying `ShareConsumer` is closed.
  A new event class is introduced because `ShareConsumer` is a separate client API from `Consumer`, so the existing `ConsumerStoppingEvent` is not reusable.
- `ConsumerStoppedEvent`: published after the share consumer is closed, with a `reason` of `NORMAL`, `ABNORMAL`, or `ERROR`.
- `ConsumerFailedToStartEvent`: published when a share consumer fails to start.
  Any already-constructed consumers from the same startup attempt are closed quietly.

See [Lifecycle Events](#kafka-kafka-queues--share-container-lifecycle-events) for details.

<a id="whats-new--x41-share-acknowledgment-renew"></a>
<a id="whats-new--shareacknowledgment.renew"></a>

### ShareAcknowledgment.renew()

`ShareAcknowledgment` now supports `renew()` to extend the acquisition lock when processing exceeds the broker’s lock duration (KIP-1222, Kafka 4.2).
See [ShareAcknowledgment API](#kafka-kafka-queues--share-acknowledgment-api) in the Kafka Queues documentation for details.

<a id="whats-new--x41-retry-topic-builder-default"></a>
<a id="whats-new--retrytopicconfigurationbuilder-default-strategy-change"></a>

### `RetryTopicConfigurationBuilder` Default Strategy Change

The default value of `sameIntervalTopicReuseStrategy` in `RetryTopicConfigurationBuilder` has been changed from `MULTIPLE_TOPICS` to `SINGLE_TOPIC` to align with the `@RetryableTopic` annotation default.
See [Topic Naming](#retrytopic-topic-naming) for more information.

<a id="whats-new--x41-kafka-streams-native-dlq"></a>
<a id="whats-new--kafka-streams-native-dlq-support"></a>

### Kafka Streams Native DLQ Support

Spring for Apache Kafka now provides exception handlers that support Kafka Streams DLQ (KIP-1034, Kafka 4.2):

- [`RecoveringDeserializationExceptionHandler`](#streams--streams-deser-recovery) (updated).
- [`RecoveringProcessingExceptionHandler`](#streams--streams-processing-recovery) (new).
- [`RecoveringProductionExceptionHandler`](#streams--streams-production-recovery) (new).

The provided exception handlers support multiple Kafka Streams DLQ enabling strategies and dead-letter topic resolution options:

- The Kafka Streams property [`errors.dead.letter.queue.topic.name`](#streams--dead-letter-queue-topic-name-property).
- An implementation of the new [`KafkaStreamsDeadLetterDestinationResolver`](#streams--dead-letter-destination-resolver) functional interface for dynamic resolution.
- The `setDeadLetterTopicName()` method of the [`StreamsBuilderFactoryBean`](#streams--dead-letter-queue-topic-name-property).

`RecoveringDeserializationExceptionHandler.KSTREAM_DESERIALIZATION_RECOVERER` has been deprecated in favor of `RecoveringDeserializationExceptionHandler.RECOVERER` to align with the new handlers properties.

<a id="whats-new--x41-kafka-streams-group-protocol"></a>
<a id="whats-new--kafka-streams-group-protocol-configuration"></a>

### Kafka Streams Group Protocol Configuration

The `StreamsBuilderFactoryBean` now supports configuring the `groupProtocol` property.
This allows you to explicitly manage whether the underlying Kafka Streams consumers rely on the `classic` protocol or opt into the newer `streams` group protocol (KIP-1071: Server-side rebalance for Streams).

See [Configuration](#streams--streams-config) in the Kafka Streams documentation for more details.

<a id="whats-new--x41-back-off-function"></a>
<a id="whats-new--backofffunction-support-in-failedbatchprocessor"></a>

### BackOffFunction Support in FailedBatchProcessor

`FailedBatchProcessor` now supports `setBackOffFunction` and `setResetStateOnExceptionChange` for batch message processing, the same way `FailedRecordProcessor` already does for single message processing.
This enables consistent exception classification across both single and batch processing when using [DefaultErrorHandler](#kafka-annotation-error-handling--default-eh).

Note that to preserve backward compatibility, the default value for `resetStateOnExceptionChange` is `false` in `FailedBatchProcessor`, unlike `FailedRecordProcessor` where it defaults to `true`.
If you want consistent behavior across both, call `setResetStateOnExceptionChange(true)` on your `DefaultErrorHandler` instance.

[Overview](#index)
[Introduction](#introduction)

---

<a id="introduction"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/introduction.html -->

<!-- page_index: 3 -->

<a id="introduction--page-title"></a>
<a id="introduction--introduction"></a>

# Introduction

This first part of the reference documentation is a high-level overview of Spring for Apache Kafka and the underlying concepts and some code snippets that can help you get up and running as quickly as possible.

[What’s new?](#whats-new)
[Quick Tour](#quick-tour)

---

<a id="quick-tour"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/quick-tour.html -->

<!-- page_index: 4 -->

# Quick Tour

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="quick-tour--page-title"></a>
<a id="quick-tour--quick-tour"></a>

# Quick Tour

Prerequisites: You must install and run Apache Kafka.
Then you must put the Spring for Apache Kafka (`spring-kafka`) JAR and all of its dependencies on your classpath.
The easiest way to do that is to declare a dependency in your build tool.

If you are not using Spring Boot, declare the `spring-kafka` jar as a dependency in your project.

- Maven
- Gradle

```xml
<dependency>
  <groupId>org.springframework.kafka</groupId>
  <artifactId>spring-kafka</artifactId>
  <version>4.1.0</version>
</dependency>
```

```groovy
implementation 'org.springframework.kafka:spring-kafka:4.1.0'
```

> [!IMPORTANT]
> When using Spring Boot, (and you haven’t used start.spring.io to create your project), use the `spring-boot-starter-kafka` dependency and omit the version; Boot will automatically bring in the correct version that is compatible with your Boot version:

- Maven
- Gradle

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-kafka</artifactId>
</dependency>
```

```groovy
implementation 'org.springframework.boot:spring-boot-starter-kafka'
```

However, the quickest way to get started is to use [start.spring.io](https://start.spring.io) (or the wizards in Spring Tool Suits and Intellij IDEA) and create a project, selecting 'Spring for Apache Kafka' as a dependency.

<a id="quick-tour--compatibility"></a>

## Compatibility

This quick tour works with the following versions:

- Apache Kafka Clients 4.0.x
- Spring Framework 7.0.0
- Minimum Java version: 17

<a id="quick-tour--getting-started"></a>

## Getting Started

The simplest way to get started is to use [start.spring.io](https://start.spring.io) (or the wizards in Spring Tool Suits and Intellij IDEA) and create a project, selecting 'Spring for Apache Kafka' as a dependency.
Refer to the [Spring Boot documentation](https://docs.spring.io/spring-boot/4.0/reference/messaging/kafka.html) for more information about its opinionated auto configuration of the infrastructure beans.

Here is a minimal consumer application.

<a id="quick-tour--spring-boot-consumer-app"></a>

### Spring Boot Consumer App

Application

- Java
- Kotlin

```java
@SpringBootApplication public class Application {
public static void main(String[] args) {SpringApplication.run(Application.class, args);}
@Bean public NewTopic topic() {return TopicBuilder.name("topic1") .partitions(10) .replicas(1) .build();}
@KafkaListener(id = "myId", topics = "topic1") public void listen(String in) {System.out.println(in);}
}
```

```kotlin
@SpringBootApplication
class Application {

    @Bean
    fun topic() = NewTopic("topic1", 10, 1)

    @KafkaListener(id = "myId", topics = ["topic1"])
    fun listen(value: String?) {
        println(value)
    }

}

fun main(args: Array<String>) = runApplication<Application>(*args)
```

application.properties

```properties
spring.kafka.consumer.auto-offset-reset=earliest
```

The `NewTopic` bean causes the topic to be created on the broker; it is not needed if the topic already exists.

<a id="quick-tour--spring-boot-producer-app"></a>

### Spring Boot Producer App

Application

- Java
- Kotlin

```java
@SpringBootApplication public class Application {
public static void main(String[] args) {SpringApplication.run(Application.class, args);}
@Bean public NewTopic topic() {return TopicBuilder.name("topic1") .partitions(10) .replicas(1) .build();}
@Bean public ApplicationRunner runner(KafkaTemplate<String, String> template) {return args -> {template.send("topic1", "test"); };}
}
```

```kotlin
@SpringBootApplication
class Application {

    @Bean
    fun topic() = NewTopic("topic1", 10, 1)

    @Bean
    fun runner(template: KafkaTemplate<String, String>) =
        ApplicationRunner { template.send("topic1", "test") }
    
    companion object {
        @JvmStatic
        fun main(args: Array<String>) = runApplication<Application>(*args)
    }

}
```

<a id="quick-tour--with-java-configuration-no-spring-boot"></a>

### With Java Configuration (No Spring Boot)

> [!IMPORTANT]
> Spring for Apache Kafka is designed to be used in a Spring Application Context.
> For example, if you create the listener container yourself outside of a Spring context, not all functions will work unless you satisfy all of the `...Aware` interfaces that the container implements.

Here is an example of an application that does not use Spring Boot; it has both a `Consumer` and `Producer`.

Without Spring Boot

- Java
- Kotlin

```java
public class Sender {
public static void main(String[] args) {AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class); context.getBean(Sender.class).send("test", 42);}
private final KafkaTemplate<Integer, String> template;
public Sender(KafkaTemplate<Integer, String> template) {this.template = template;}
public void send(String toSend, int key) {this.template.send("topic1", key, toSend);}
}
public class Listener {
@KafkaListener(id = "listen1", topics = "topic1") public void listen1(String in) {System.out.println(in);}
}
@Configuration @EnableKafka public class Config {
@Bean ConcurrentKafkaListenerContainerFactory<Integer, String> kafkaListenerContainerFactory(ConsumerFactory<Integer, String> consumerFactory) {ConcurrentKafkaListenerContainerFactory<Integer, String> factory =new ConcurrentKafkaListenerContainerFactory<>(); factory.setConsumerFactory(consumerFactory); return factory;}
@Bean public ConsumerFactory<Integer, String> consumerFactory() {return new DefaultKafkaConsumerFactory<>(consumerProps());}
private Map<String, Object> consumerProps() {Map<String, Object> props = new HashMap<>(); props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092"); props.put(ConsumerConfig.GROUP_ID_CONFIG, "group"); props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, IntegerDeserializer.class); props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class); props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest"); // ...return props;}
@Bean public Sender sender(KafkaTemplate<Integer, String> template) {return new Sender(template);}
@Bean public Listener listener() {return new Listener();}
@Bean public ProducerFactory<Integer, String> producerFactory() {return new DefaultKafkaProducerFactory<>(senderProps());}
private Map<String, Object> senderProps() {Map<String, Object> props = new HashMap<>(); props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092"); props.put(ProducerConfig.LINGER_MS_CONFIG, 10); props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerSerializer.class); props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class); //...return props;}
@Bean public KafkaTemplate<Integer, String> kafkaTemplate(ProducerFactory<Integer, String> producerFactory) {return new KafkaTemplate<>(producerFactory);}
}
```

```kotlin
class Sender(private val template: KafkaTemplate<Int, String>) {

    fun send(toSend: String, key: Int) {
        template.send("topic1", key, toSend)
    }

}

class Listener {

    @KafkaListener(id = "listen1", topics = ["topic1"])
    fun listen1(`in`: String) {
        println(`in`)
    }

}

@Configuration
@EnableKafka
class Config {

    @Bean
    fun kafkaListenerContainerFactory(consumerFactory: ConsumerFactory<Int, String>) =
        ConcurrentKafkaListenerContainerFactory<Int, String>().apply {
            setConsumerFactory(consumerFactory)
        }

    @Bean
    fun consumerFactory() = DefaultKafkaConsumerFactory<Int, String>(consumerProps)

    val consumerProps = mapOf(
        ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG to "localhost:9092",
        ConsumerConfig.GROUP_ID_CONFIG to "group",
        ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG to IntegerDeserializer::class.java,
        ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG to StringDeserializer::class.java,
        ConsumerConfig.AUTO_OFFSET_RESET_CONFIG to "earliest"
    )

    @Bean
    fun sender(template: KafkaTemplate<Int, String>) = Sender(template)

    @Bean
    fun listener() = Listener()

    @Bean
    fun producerFactory() = DefaultKafkaProducerFactory<Int, String>(senderProps)

    val senderProps = mapOf(
        ProducerConfig.BOOTSTRAP_SERVERS_CONFIG to "localhost:9092",
        ProducerConfig.LINGER_MS_CONFIG to 10,
        ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG to IntegerSerializer::class.java,
        ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG to StringSerializer::class.java
    )

    @Bean
    fun kafkaTemplate(producerFactory: ProducerFactory<Int, String>) = KafkaTemplate(producerFactory)

}
```

As you can see, you have to define several infrastructure beans when not using Spring Boot.

[Introduction](#introduction)
[Reference](#reference)

---

<a id="reference"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/reference.html -->

<!-- page_index: 5 -->

<a id="reference--page-title"></a>
<a id="reference--reference"></a>

# Reference

This part of the reference documentation details the various components that comprise Spring for Apache Kafka.
The [main chapter](#kafka) covers the core classes to develop a Kafka application with Spring.

[Quick Tour](#quick-tour)
[Using Spring for Apache Kafka](#kafka)

---

<a id="kafka"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka.html -->

<!-- page_index: 6 -->

# Using Spring for Apache Kafka

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka--page-title"></a>
<a id="kafka--using-spring-for-apache-kafka"></a>

# Using Spring for Apache Kafka

This section offers detailed explanations of the various concerns that impact using Spring for Apache Kafka.
For a quick but less detailed introduction, see [Quick Tour](#quick-tour).

<a id="kafka--section-summary"></a>

## Section Summary

- [Connecting to Kafka](#kafka-connecting)
- [Configuring Topics](#kafka-configuring-topics)
- [Sending Messages](#kafka-sending-messages)
- [Receiving Messages](#kafka-receiving-messages)
- [Listener Container Properties](#kafka-container-props)
- [Dynamically Creating Containers](#kafka-dynamic-containers)
- [Application Events](#kafka-events)
- [Topic/Partition Initial Offset](#kafka-topic-partition-initial-offset)
- [Seeking to a Specific Offset](#kafka-seek)
- [Container factory](#kafka-container-factory)
- [Thread Safety](#kafka-thread-safety)
- [Monitoring](#kafka-micrometer)
- [Transactions](#kafka-transactions)
- [Exactly Once Semantics](#kafka-exactly-once)
- [Wiring Spring Beans into Producer/Consumer Interceptors](#kafka-interceptors)
- [Producer Interceptor Managed in Spring](#kafka-producer-interceptor-managed-in-spring)
- [Pausing and Resuming Listener Containers](#kafka-pause-resume)
- [Pausing and Resuming Partitions on Listener Containers](#kafka-pause-resume-partitions)
- [Serialization, Deserialization, and Message Conversion](#kafka-serdes)
- [Message Headers](#kafka-headers)
- [Null Payloads and Log Compaction of 'Tombstone' Records](#kafka-tombstones)
- [Handling Exceptions](#kafka-annotation-error-handling)
- [JAAS and Kerberos](#kafka-kerberos)
- [Kafka Queues (Share Consumer)](#kafka-kafka-queues)

[Reference](#reference)
[Connecting to Kafka](#kafka-connecting)

---

<a id="kafka-connecting"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/connecting.html -->

<!-- page_index: 7 -->

# Connecting to Kafka

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-connecting--page-title"></a>
<a id="kafka-connecting--connecting-to-kafka"></a>

# Connecting to Kafka

- `KafkaAdmin` - see [Configuring Topics](#kafka-configuring-topics)
- `ProducerFactory` - see [Sending Messages](#kafka-sending-messages)
- `ConsumerFactory` - see [Receiving Messages](#kafka-receiving-messages)

Starting with version 2.5, each of these extends `KafkaResourceFactory`.
This allows changing the bootstrap servers at runtime by adding a `Supplier<String>` to their configuration: `setBootstrapServersSupplier(() -> …)`.
This will be called for all new connections to get the list of servers.
Consumers and Producers are generally long-lived.
To close existing Producers, call `reset()` on the `DefaultKafkaProducerFactory`.
To close existing Consumers, call `stop()` (and then `start()`) on the `KafkaListenerEndpointRegistry` and/or `stop()` and `start()` on any other listener container beans.

For convenience, the framework also provides an `ABSwitchCluster` which supports two sets of bootstrap servers; one of which is active at any time.
Configure the `ABSwitchCluster` and add it to the producer and consumer factories, and the `KafkaAdmin`, by calling `setBootstrapServersSupplier()`.
When you want to switch, call `primary()` or `secondary()` and call `reset()` on the producer factory to establish new connection(s); for consumers, `stop()` and `start()` all listener containers.
When using `@KafkaListener`s, `stop()` and `start()` the `KafkaListenerEndpointRegistry` bean.

See the Javadocs for more information.

<a id="kafka-connecting--factory-listeners"></a>

## Factory Listeners

Starting with version 2.5, the `DefaultKafkaProducerFactory` and `DefaultKafkaConsumerFactory` can be configured with a `Listener` to receive notifications whenever a producer or consumer is created or closed.

Producer Factory Listener

```java
interface Listener<K, V> {
default void producerAdded(String id, Producer<K, V> producer) {}
default void producerRemoved(String id, Producer<K, V> producer) {}
}
```

Consumer Factory Listener

```java
interface Listener<K, V> {
default void consumerAdded(String id, Consumer<K, V> consumer) {}
default void consumerRemoved(String id, Consumer<K, V> consumer) {}
}
```

In each case, the `id` is created by appending the `client-id` property (obtained from the `metrics()` after creation) to the factory `beanName` property, separated by `.`.

These listeners can be used, for example, to create and bind a Micrometer `KafkaClientMetrics` instance when a new client is created (and close it when the client is closed).

The framework provides listeners that do exactly that; see [Micrometer Native Metrics](#kafka-micrometer--micrometer-native).

<a id="kafka-connecting--default-client-id-prefixes"></a>

## Default client ID prefixes

Starting with version 3.2, for Spring Boot applications which define an application name using the `spring.application.name` property, this name is now used
as a default prefix for auto-generated client IDs for these client types:

- consumer clients which don’t use a consumer group
- producer clients
- admin clients

This makes it easier to identify these clients at server side for troubleshooting or applying quotas.

| Client Type | Without application name | With application name |
| --- | --- | --- |
| consumer without consumer group | consumer-null-1 | myapp-consumer-1 |
| consumer with consumer group "mygroup" | consumer-mygroup-1 | consumer-mygroup-1 |
| producer | producer-1 | myapp-producer-1 |
| admin | adminclient-1 | myapp-admin-1 |

[Using Spring for Apache Kafka](#kafka)
[Configuring Topics](#kafka-configuring-topics)

---

<a id="kafka-configuring-topics"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/configuring-topics.html -->

<!-- page_index: 8 -->

# Configuring Topics

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-configuring-topics--page-title"></a>
<a id="kafka-configuring-topics--configuring-topics"></a>

# Configuring Topics

If you define a `KafkaAdmin` bean in your application context, it can automatically add topics to the broker.
To do so, you can add a `NewTopic` `@Bean` for each topic to the application context.
Version 2.3 introduced a new class `TopicBuilder` to make creation of such beans more convenient.
The following example shows how to do so:

- Java
- Kotlin

```java
@Bean
public KafkaAdmin admin() {
    Map<String, Object> configs = new HashMap<>();
    configs.put(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    return new KafkaAdmin(configs);
}

@Bean
public NewTopic topic1() {
    return TopicBuilder.name("thing1")
            .partitions(10)
            .replicas(3)
            .compact()
            .build();
}

@Bean
public NewTopic topic2() {
    return TopicBuilder.name("thing2")
            .partitions(10)
            .replicas(3)
            .config(TopicConfig.COMPRESSION_TYPE_CONFIG, "zstd")
            .build();
}

@Bean
public NewTopic topic3() {
    return TopicBuilder.name("thing3")
            .assignReplicas(0, List.of(0, 1))
            .assignReplicas(1, List.of(1, 2))
            .assignReplicas(2, List.of(2, 0))
            .config(TopicConfig.COMPRESSION_TYPE_CONFIG, "zstd")
            .build();
}
```

```kotlin
@Bean
fun admin() = KafkaAdmin(mapOf(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG to "localhost:9092"))

@Bean
fun topic1() =
    TopicBuilder.name("thing1")
        .partitions(10)
        .replicas(3)
        .compact()
        .build()

@Bean
fun topic2() =
    TopicBuilder.name("thing2")
        .partitions(10)
        .replicas(3)
        .config(TopicConfig.COMPRESSION_TYPE_CONFIG, "zstd")
        .build()

@Bean
fun topic3() =
    TopicBuilder.name("thing3")
        .assignReplicas(0, Arrays.asList(0, 1))
        .assignReplicas(1, Arrays.asList(1, 2))
        .assignReplicas(2, Arrays.asList(2, 0))
        .config(TopicConfig.COMPRESSION_TYPE_CONFIG, "zstd")
        .build()
```

Starting with version 2.6, you can omit `partitions()` and/or `replicas()` and the broker defaults will be applied to those properties.
The broker version must be at least 2.4.0 to support this feature - see [KIP-464](https://cwiki.apache.org/confluence/display/KAFKA/KIP-464%3A+Defaults+for+AdminClient%23createTopic).

- Java
- Kotlin

```java
@Bean
public NewTopic topic4() {
    return TopicBuilder.name("defaultBoth")
            .build();
}

@Bean
public NewTopic topic5() {
    return TopicBuilder.name("defaultPart")
            .replicas(1)
            .build();
}

@Bean
public NewTopic topic6() {
    return TopicBuilder.name("defaultRepl")
            .partitions(3)
            .build();
}
```

```kotlin
@Bean
fun topic4() = TopicBuilder.name("defaultBoth").build()

@Bean
fun topic5() = TopicBuilder.name("defaultPart").replicas(1).build()

@Bean
fun topic6() = TopicBuilder.name("defaultRepl").partitions(3).build()
```

Starting with version 2.7, you can declare multiple `NewTopic`s in a single `KafkaAdmin.NewTopics` bean definition:

- Java
- Kotlin

```java
@Bean
public KafkaAdmin.NewTopics topics456() {
    return new NewTopics(
            TopicBuilder.name("defaultBoth")
                .build(),
            TopicBuilder.name("defaultPart")
                .replicas(1)
                .build(),
            TopicBuilder.name("defaultRepl")
                .partitions(3)
                .build());
}
```

```kotlin
@Bean
fun topics456() = KafkaAdmin.NewTopics(
    TopicBuilder.name("defaultBoth")
        .build(),
    TopicBuilder.name("defaultPart")
        .replicas(1)
        .build(),
    TopicBuilder.name("defaultRepl")
        .partitions(3)
        .build()
)
```

> [!IMPORTANT]
> When using Spring Boot, a `KafkaAdmin` bean is automatically registered so you only need the `NewTopic` (and/or `NewTopics`) `@Bean`s.

By default, if the broker is not available, a message is logged, but the context continues to load.
You can programmatically invoke the admin’s `initialize()` method to try again later.
If you wish this condition to be considered fatal, set the admin’s `fatalIfBrokerNotAvailable` property to `true`.
The context then fails to initialize.

> [!NOTE]
> If the broker supports it (1.0.0 or higher), the admin increases the number of partitions if it is found that an existing topic has fewer partitions than the `NewTopic.numPartitions`.

Starting with version 2.7, the `KafkaAdmin` provides methods to create and examine topics at runtime.
Starting with version 4.0, it also provides a method to delete topics.

- `createOrModifyTopics`
- `describeTopics`
- `deleteTopics` (since 4.0)

For more advanced administrative features, you can use the `AdminClient` directly.
The following example shows how to do so:

```java
@Autowired private KafkaAdmin admin;
...
AdminClient client = AdminClient.create(admin.getConfigurationProperties()); ...client.close();
```

Starting with versions 2.9.10, 3.0.9, you can provide a `Predicate<NewTopic>` which can be used to determine whether a particular `NewTopic` bean should be considered for creation or modification.
This is useful, for example, if you have multiple `KafkaAdmin` instances pointing to different clusters and you wish to select those topics that should be created or modified by each admin.

```java
admin.setCreateOrModifyTopic(nt -> !nt.name().equals("dontCreateThisOne"));
```

[Connecting to Kafka](#kafka-connecting)
[Sending Messages](#kafka-sending-messages)

---

<a id="kafka-sending-messages"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/sending-messages.html -->

<!-- page_index: 9 -->

# Sending Messages

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-sending-messages--page-title"></a>
<a id="kafka-sending-messages--sending-messages"></a>

# Sending Messages

This section covers how to send messages.

<a id="kafka-sending-messages--kafka-template"></a>
<a id="kafka-sending-messages--using-kafkatemplate"></a>

## Using `KafkaTemplate`

This section covers how to use `KafkaTemplate` to send messages.

<a id="kafka-sending-messages--overview"></a>

### Overview

The `KafkaTemplate` wraps a producer and provides convenience methods to send data to Kafka topics.
The following listing shows the relevant methods from `KafkaTemplate`:

```java
CompletableFuture<SendResult<K, V>> sendDefault(V data);

CompletableFuture<SendResult<K, V>> sendDefault(K key, V data);

CompletableFuture<SendResult<K, V>> sendDefault(Integer partition, K key, V data);

CompletableFuture<SendResult<K, V>> sendDefault(Integer partition, Long timestamp, K key, V data);

CompletableFuture<SendResult<K, V>> send(String topic, V data);

CompletableFuture<SendResult<K, V>> send(String topic, K key, V data);

CompletableFuture<SendResult<K, V>> send(String topic, Integer partition, K key, V data);

CompletableFuture<SendResult<K, V>> send(String topic, Integer partition, Long timestamp, K key, V data);

CompletableFuture<SendResult<K, V>> send(ProducerRecord<K, V> record);

CompletableFuture<SendResult<K, V>> send(Message<?> message);

Map<MetricName, ? extends Metric> metrics();

List<PartitionInfo> partitionsFor(String topic);

<T> T execute(ProducerCallback<K, V, T> callback);

<T> T executeInTransaction(OperationsCallback<K, V, T> callback);

// Flush the producer.
void flush();

interface ProducerCallback<K, V, T> {

    T doInKafka(Producer<K, V> producer);

}

interface OperationsCallback<K, V, T> {

    T doInOperations(KafkaOperations<K, V> operations);

}
```

See the [Javadoc](https://docs.spring.io/spring-kafka/docs/4.1.0/api/org/springframework/kafka/core/KafkaTemplate.html) for more detail.

The `sendDefault` API requires that a default topic has been provided to the template.

The API takes in a `timestamp` as a parameter and stores this timestamp in the record.
How the user-provided timestamp is stored depends on the timestamp type configured on the Kafka topic.
If the topic is configured to use `CREATE_TIME`, the user-specified timestamp is recorded (or generated if not specified).
If the topic is configured to use `LOG_APPEND_TIME`, the user-specified timestamp ignored and the broker adds in the local broker time.

The `metrics` and `partitionsFor` methods delegate to the same methods on the underlying [`Producer`](https://kafka.apache.org/42/javadoc/org/apache/kafka/clients/producer/Producer.html).
The `execute` method provides direct access to the underlying [`Producer`](https://kafka.apache.org/42/javadoc/org/apache/kafka/clients/producer/Producer.html).

> [!NOTE]
> When sending messages from Spring components, avoid using `@PostConstruct` methods if relying on automatic topic creation via `NewTopic` beans.
> `@PostConstruct` runs before the application context is fully ready, which may cause `UnknownTopicOrPartitionException` on clean brokers.
>
> Instead, consider these alternatives:
>
> - Use an `ApplicationListener<ContextRefreshedEvent>` to ensure the context is fully refreshed before sending.
> - Implement `SmartLifecycle` to start after the `KafkaAdmin` bean has completed its initialization.
> - Pre-create topics externally.

To use the template, you can configure a producer factory and provide it in the template’s constructor.
The following example shows how to do so:

```java
@Bean
public ProducerFactory producerFactory() {
    return new DefaultKafkaProducerFactory<>(producerConfigs());
}

@Bean
public Map producerConfigs() {
    Map props = new HashMap<>();
    props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerSerializer.class);
    props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
    // See https://kafka.apache.org/42/documentation/#producerconfigs for more properties
    return props;
}

@Bean
public KafkaTemplate kafkaTemplate() {
    return new KafkaTemplate(producerFactory());
}
```

Starting with version 2.5, you can now override the factory’s `ProducerConfig` properties to create templates with different producer configurations from the same factory.

```java
@Bean public KafkaTemplate<String, String> stringTemplate(ProducerFactory<String, String> pf) {return new KafkaTemplate<>(pf);}
@Bean public KafkaTemplate<String, byte[]> bytesTemplate(ProducerFactory<String, byte[]> pf) {return new KafkaTemplate<>(pf,Collections.singletonMap(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, ByteArraySerializer.class));}
```

Note that a bean of type `ProducerFactory<?, ?>` (such as the one auto-configured by Spring Boot) can be referenced with different narrowed generic types.

You can also configure the template by using standard `<bean/>` definitions.

Then, to use the template, you can invoke one of its methods.

When you use the methods with a `Message<?>` parameter, the topic, partition, key and timestamp information is provided in a message header that includes the following items:

- `KafkaHeaders.TOPIC`
- `KafkaHeaders.PARTITION`
- `KafkaHeaders.KEY`
- `KafkaHeaders.TIMESTAMP`

The message payload is the data.

Optionally, you can configure the `KafkaTemplate` with a `ProducerListener` to get an asynchronous callback with the results of the send (success or failure) instead of waiting for the `Future` to complete.
The following listing shows the definition of the `ProducerListener` interface:

```java
public interface ProducerListener<K, V> {
default void onSuccess(ProducerRecord<K, V> producerRecord, RecordMetadata recordMetadata) {}
default void onError(ProducerRecord<K, V> producerRecord, RecordMetadata recordMetadata, Exception exception) {}
}
```

By default, the template is configured with a `LoggingProducerListener`, which logs errors and does nothing when the send is successful.

For convenience, default method implementations are provided in case you want to implement only one of the methods.

Notice that the send methods return a `CompletableFuture<SendResult>`.
You can register a callback with the listener to receive the result of the send asynchronously.
The following example shows how to do so:

```java
CompletableFuture<SendResult<Integer, String>> future = template.send("myTopic", "something");
future.whenComplete((result, ex) -> {
    ...
});
```

`SendResult` has two properties, a `ProducerRecord` and `RecordMetadata`.
See the Kafka API documentation for information about those objects.

The `Throwable` can be cast to a `KafkaProducerException`; its `producerRecord` property contains the failed record.

If you wish to block the sending thread to await the result, you can invoke the future’s `get()` method; using the method with a timeout is recommended.
If you have set a `linger.ms`, you may wish to invoke `flush()` before waiting or, for convenience, the template has a constructor with an `autoFlush` parameter that causes the template to `flush()` on each send.
Flushing is only needed if you have set the `linger.ms` producer property and want to immediately send a partial batch.

<a id="kafka-sending-messages--examples"></a>

### Examples

This section shows examples of sending messages to Kafka:

Example 1. Non Blocking (Async)

```java
public void sendToKafka(final MyOutputData data) {final ProducerRecord<String, String> record = createRecord(data);
CompletableFuture<SendResult<String, String>> future = template.send(record); future.whenComplete((result, ex) -> {if (ex == null) {handleSuccess(data);} else {handleFailure(data, record, ex);} });}
```

Example 2. Blocking (Sync)

```java
public void sendToKafka(final MyOutputData data) {final ProducerRecord<String, String> record = createRecord(data);
try {template.send(record).get(10, TimeUnit.SECONDS); handleSuccess(data);} catch (ExecutionException e) {handleFailure(data, record, e.getCause());} catch (TimeoutException | InterruptedException e) {handleFailure(data, record, e);}}
```

Note that the cause of the `ExecutionException` is `KafkaProducerException` with the `producerRecord` property.

<a id="kafka-sending-messages--routing-template"></a>
<a id="kafka-sending-messages--using-routingkafkatemplate"></a>

## Using `RoutingKafkaTemplate`

Starting with version 2.5, you can use a `RoutingKafkaTemplate` to select the producer at runtime, based on the destination `topic` name.

> [!IMPORTANT]
> The routing template does **not** support transactions, `execute`, `flush`, or `metrics` operations because the topic is not known for those operations.

The template requires a map of `java.util.regex.Pattern` to `ProducerFactory<Object, Object>` instances.
This map should be ordered (e.g. a `LinkedHashMap`) because it is traversed in order; you should add more specific patterns at the beginning.

The following simple Spring Boot application provides an example of how to use the same template to send to different topics, each using a different value serializer.

```java
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public RoutingKafkaTemplate routingTemplate(GenericApplicationContext context,
            ProducerFactory<Object, Object> pf) {

        // Clone the PF with a different Serializer, register with Spring for shutdown
        Map<String, Object> configs = new HashMap<>(pf.getConfigurationProperties());
        configs.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, ByteArraySerializer.class);
        DefaultKafkaProducerFactory<Object, Object> bytesPF = new DefaultKafkaProducerFactory<>(configs);
        context.registerBean("bytesPF", DefaultKafkaProducerFactory.class, () -> bytesPF);

        Map<Pattern, ProducerFactory<Object, Object>> map = new LinkedHashMap<>();
        map.put(Pattern.compile("two"), bytesPF);
        map.put(Pattern.compile(".+"), pf); // Default PF with StringSerializer
        return new RoutingKafkaTemplate(map);
    }

    @Bean
    public ApplicationRunner runner(RoutingKafkaTemplate routingTemplate) {
        return args -> {
            routingTemplate.send("one", "thing1");
            routingTemplate.send("two", "thing2".getBytes());
        };
    }

}
```

The corresponding `@KafkaListener`s for this example are shown in [Annotation Properties](#kafka-receiving-messages-listener-annotation--annotation-properties).

For another technique to achieve similar results, but with the additional capability of sending different types to the same topic, see [Delegating Serializer and Deserializer](#kafka-serdes--delegating-serialization).

<a id="kafka-sending-messages--producer-factory"></a>
<a id="kafka-sending-messages--using-defaultkafkaproducerfactory"></a>

## Using `DefaultKafkaProducerFactory`

As seen in [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template), a `ProducerFactory` is used to create the producer.

When not using [Transactions](#kafka-transactions), by default, the `DefaultKafkaProducerFactory` creates a singleton producer used by all clients, as recommended in the `KafkaProducer` JavaDocs.
However, if you call `flush()` on the template, this can cause delays for other threads using the same producer.
Starting with version 2.3, the `DefaultKafkaProducerFactory` has a new property `producerPerThread`.
When set to `true`, the factory will create (and cache) a separate producer for each thread, to avoid this issue.

> [!IMPORTANT]
> When `producerPerThread` is `true`, user code **must** call `closeThreadBoundProducer()` on the factory when the producer is no longer needed.
> This will physically close the producer and remove it from the `ThreadLocal`.
> Calling `reset()` or `destroy()` will not clean up these producers.

Also see [`KafkaTemplate` Transactional and non-Transactional Publishing](#kafka-transactions--tx-template-mixed).

When creating a `DefaultKafkaProducerFactory`, key and/or value `Serializer` classes can be picked up from configuration by calling the constructor that only takes in a Map of properties (see example in [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template)), or `Serializer` instances may be passed to the `DefaultKafkaProducerFactory` constructor (in which case all `Producer`s share the same instances).
Alternatively you can provide `Supplier<Serializer>`s (starting with version 2.3) that will be used to obtain separate `Serializer` instances for each `Producer`:

```java
@Bean public ProducerFactory<Integer, CustomValue> producerFactory() {return new DefaultKafkaProducerFactory<>(producerConfigs(), null, () -> new CustomValueSerializer());}
@Bean public KafkaTemplate<Integer, CustomValue> kafkaTemplate() {return new KafkaTemplate<Integer, CustomValue>(producerFactory());}
```

Starting with version 2.5.10, you can now update the producer properties after the factory is created.
This might be useful, for example, if you have to update SSL key/trust store locations after a credentials change.
The changes will not affect existing producer instances; call `reset()` to close any existing producers so that new producers will be created using the new properties.

> [!NOTE]
> You cannot change a transactional producer factory to non-transactional, and vice-versa.

Two new methods are now provided:

```java
void updateConfigs(Map<String, Object> updates);

void removeConfig(String configKey);
```

Starting with version 2.8, if you provide serializers as objects (in the constructor or via the setters), the factory will invoke the `configure()` method to configure them with the configuration properties.

<a id="kafka-sending-messages--replying-template"></a>
<a id="kafka-sending-messages--using-replyingkafkatemplate"></a>

## Using `ReplyingKafkaTemplate`

Version 2.1.3 introduced a subclass of `KafkaTemplate` to provide request/reply semantics.
The class is named `ReplyingKafkaTemplate` and has two additional methods; the following shows the method signatures:

```java
RequestReplyFuture<K, V, R> sendAndReceive(ProducerRecord<K, V> record);

RequestReplyFuture<K, V, R> sendAndReceive(ProducerRecord<K, V> record,
    Duration replyTimeout);
```

(Also see [Request/Reply with `Message<?>`s](#kafka-sending-messages--exchanging-messages)).

The result is a `CompletableFuture` that is asynchronously populated with the result (or an exception, for a timeout).
The result also has a `sendFuture` property, which is the result of calling `KafkaTemplate.send()`.
You can use this future to determine the result of the send operation.

If the first method is used, or the `replyTimeout` argument is `null`, the template’s `defaultReplyTimeout` property is used (5 seconds by default).

Starting with version 2.8.8, the template has a new method `waitForAssignment`.
This is useful if the reply container is configured with `auto.offset.reset=latest` to avoid sending a request and a reply sent before the container is initialized.

> [!IMPORTANT]
> When using manual partition assignment (no group management), the duration for the wait must be greater than the container’s `pollTimeout` property because the notification will not be sent until after the first poll is completed.

The following Spring Boot application shows an example of how to use the feature:

```java
@SpringBootApplication
public class KRequestingApplication {

    public static void main(String[] args) {
        SpringApplication.run(KRequestingApplication.class, args).close();
    }

    @Bean
    public ApplicationRunner runner(ReplyingKafkaTemplate<String, String, String> template) {
        return args -> {
            if (!template.waitForAssignment(Duration.ofSeconds(10))) {
                throw new IllegalStateException("Reply container did not initialize");
            }
            ProducerRecord<String, String> record = new ProducerRecord<>("kRequests", "foo");
            RequestReplyFuture<String, String, String> replyFuture = template.sendAndReceive(record);
            SendResult<String, String> sendResult = replyFuture.getSendFuture().get(10, TimeUnit.SECONDS);
            System.out.println("Sent ok: " + sendResult.getRecordMetadata());
            ConsumerRecord<String, String> consumerRecord = replyFuture.get(10, TimeUnit.SECONDS);
            System.out.println("Return value: " + consumerRecord.value());
        };
    }

    @Bean
    public ReplyingKafkaTemplate<String, String, String> replyingTemplate(
            ProducerFactory<String, String> pf,
            ConcurrentMessageListenerContainer<String, String> repliesContainer) {

        return new ReplyingKafkaTemplate<>(pf, repliesContainer);
    }

    @Bean
    public ConcurrentMessageListenerContainer<String, String> repliesContainer(
            ConcurrentKafkaListenerContainerFactory<String, String> containerFactory) {

        ConcurrentMessageListenerContainer<String, String> repliesContainer =
                containerFactory.createContainer("kReplies");
        repliesContainer.getContainerProperties().setGroupId("repliesGroup");
        repliesContainer.setAutoStartup(false);
        return repliesContainer;
    }

    @Bean
    public NewTopic kRequests() {
        return TopicBuilder.name("kRequests")
            .partitions(10)
            .replicas(2)
            .build();
    }

    @Bean
    public NewTopic kReplies() {
        return TopicBuilder.name("kReplies")
            .partitions(10)
            .replicas(2)
            .build();
    }

}
```

Note that we can use Boot’s auto-configured container factory to create the reply container.

If a non-trivial deserializer is being used for replies, consider using an [`ErrorHandlingDeserializer`](#kafka-serdes--error-handling-deserializer) that delegates to your configured deserializer.
When so configured, the `RequestReplyFuture` will be completed exceptionally and you can catch the `ExecutionException`, with the `DeserializationException` in its `cause` property.

Starting with version 2.6.7, in addition to detecting `DeserializationException`s, the template will call the `replyErrorChecker` function, if provided.
If it returns an exception, the future will be completed exceptionally.

Here is an example:

```java
template.setReplyErrorChecker(record -> {Header error = record.headers().lastHeader("serverSentAnError"); if (error != null) {return new MyException(new String(error.value()));} else {return null;} });
...
RequestReplyFuture<Integer, String, String> future = template.sendAndReceive(record); try {future.getSendFuture().get(10, TimeUnit.SECONDS); // send ok ConsumerRecord<Integer, String> consumerRecord = future.get(10, TimeUnit.SECONDS); ...} catch (InterruptedException e) {...} catch (ExecutionException e) {if (e.getCause() instanceof MyException) {...}} catch (TimeoutException e) {...}
```

The template sets a header (named `KafkaHeaders.CORRELATION_ID` by default), which must be echoed back by the server side.

In this case, the following `@KafkaListener` application responds:

```java
@SpringBootApplication
public class KReplyingApplication {

    public static void main(String[] args) {
        SpringApplication.run(KReplyingApplication.class, args);
    }

    @KafkaListener(id="server", topics = "kRequests")
    @SendTo // use default replyTo expression
    public String listen(String in) {
        System.out.println("Server received: " + in);
        return in.toUpperCase();
    }

    @Bean
    public NewTopic kRequests() {
        return TopicBuilder.name("kRequests")
            .partitions(10)
            .replicas(2)
            .build();
    }

    @Bean // not required if Jackson is on the classpath
    public MessagingMessageConverter simpleMapperConverter() {
        MessagingMessageConverter messagingMessageConverter = new MessagingMessageConverter();
        messagingMessageConverter.setHeaderMapper(new SimpleKafkaHeaderMapper());
        return messagingMessageConverter;
    }

}
```

The `@KafkaListener` infrastructure echoes the correlation ID and determines the reply topic.

See [Forwarding Listener Results using `@SendTo`](#kafka-receiving-messages-annotation-send-to) for more information about sending replies.
The template uses the default header `KafKaHeaders.REPLY_TOPIC` to indicate the topic to which the reply goes.

Starting with version 2.2, the template tries to detect the reply topic or partition from the configured reply container.
If the container is configured to listen to a single topic or a single `TopicPartitionOffset`, it is used to set the reply headers.
If the container is configured otherwise, the user must set up the reply headers.
In this case, an `INFO` log message is written during initialization.
The following example uses `KafkaHeaders.REPLY_TOPIC`:

```java
record.headers().add(new RecordHeader(KafkaHeaders.REPLY_TOPIC, "kReplies".getBytes()));
```

When you configure with a single reply `TopicPartitionOffset`, you can use the same reply topic for multiple templates, as long as each instance listens on a different partition.
When configuring with a single reply topic, each instance must use a different `group.id`.
In this case, all instances receive each reply, but only the instance that sent the request finds the correlation ID.
This may be useful for auto-scaling, but with the overhead of additional network traffic and the small cost of discarding each unwanted reply.
When you use this setting, we recommend that you set the template’s `sharedReplyTopic` to `true`, which reduces the logging level of unexpected replies to DEBUG instead of the default ERROR.

The following is an example of configuring the reply container to use the same shared reply topic:

```java
@Bean
public ConcurrentMessageListenerContainer<String, String> replyContainer(
        ConcurrentKafkaListenerContainerFactory<String, String> containerFactory) {

    ConcurrentMessageListenerContainer<String, String> container = containerFactory.createContainer("topic2");
    container.getContainerProperties().setGroupId(UUID.randomUUID().toString()); // unique
    Properties props = new Properties();
    props.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "latest"); // so the new group doesn't get old replies
    container.getContainerProperties().setKafkaConsumerProperties(props);
    return container;
}
```

> [!IMPORTANT]
> If you have multiple client instances and you do not configure them as discussed in the preceding paragraph, each instance needs a dedicated reply topic.
> An alternative is to set the `KafkaHeaders.REPLY_PARTITION` and use a dedicated partition for each instance.
> The `Header` contains a four-byte int (big-endian).
> The server must use this header to route the reply to the correct partition (`@KafkaListener` does this).
> In this case, though, the reply container must not use Kafka’s group management feature and must be configured to listen on a fixed partition (by using a `TopicPartitionOffset` in its `ContainerProperties` constructor).

> [!NOTE]
> The `JsonKafkaHeaderMapper` requires Jackson to be on the classpath (for the `@KafkaListener`).
> If it is not available, the message converter has no header mapper, so you must configure a `MessagingMessageConverter` with a `SimpleKafkaHeaderMapper`, as shown earlier.

By default, 3 headers are used:

- `KafkaHeaders.CORRELATION_ID` - used to correlate the reply to a request
- `KafkaHeaders.REPLY_TOPIC` - used to tell the server where to reply
- `KafkaHeaders.REPLY_PARTITION` - (optional) used to tell the server which partition to reply to

These header names are used by the `@KafkaListener` infrastructure to route the reply.

Starting with version 2.3, you can customize the header names - the template has 3 properties `correlationHeaderName`, `replyTopicHeaderName`, and `replyPartitionHeaderName`.
This is useful if your server is not a Spring application (or does not use the `@KafkaListener`).

> [!NOTE]
> Conversely, if the requesting application is not a spring application and puts correlation information in a different header, starting with version 3.0, you can configure a custom `correlationHeaderName` on the listener container factory and that header will be echoed back.
> Previously, the listener had to echo custom correlation headers.

<a id="kafka-sending-messages--exchanging-messages"></a>
<a id="kafka-sending-messages--request-reply-with-message-s"></a>

### Request/Reply with `Message<?>`s

Version 2.7 added methods to the `ReplyingKafkaTemplate` to send and receive `spring-messaging`'s `Message<?>` abstraction:

```java
RequestReplyMessageFuture<K, V> sendAndReceive(Message<?> message);

<P> RequestReplyTypedMessageFuture<K, V, P> sendAndReceive(Message<?> message,
        ParameterizedTypeReference<P> returnType);
```

These will use the template’s default `replyTimeout`, there are also overloaded versions that can take a timeout in the method call.

Use the first method if the consumer’s `Deserializer` or the template’s `MessageConverter` can convert the payload without any additional information, either via configuration or type metadata in the reply message.

Use the second method if you need to provide type information for the return type, to assist the message converter.
This also allows the same template to receive different types, even if there is no type metadata in the replies, such as when the server side is not a Spring application.
The following is an example of the latter:

Template Bean

- Java
- Kotlin

```java
@Bean
ReplyingKafkaTemplate<String, String, String> template(
        ProducerFactory<String, String> pf,
        ConcurrentKafkaListenerContainerFactory<String, String> factory) {

    ConcurrentMessageListenerContainer<String, String> replyContainer =
            factory.createContainer("replies");
    replyContainer.getContainerProperties().setGroupId("request.replies");
    ReplyingKafkaTemplate<String, String, String> template =
            new ReplyingKafkaTemplate<>(pf, replyContainer);
    template.setMessageConverter(new ByteArrayJacksonJsonMessageConverter());
    template.setDefaultTopic("requests");
    return template;
}
```

```kotlin
@Bean
fun template(
    pf: ProducerFactory<String, String>,
    factory: ConcurrentKafkaListenerContainerFactory<String, String>
): ReplyingKafkaTemplate<String, String, String> {
    val replyContainer = factory.createContainer("replies")
    replyContainer.containerProperties.setGroupId("request.replies")
    val template = ReplyingKafkaTemplate<String, String, String>(pf, replyContainer)
    template.messageConverter = ByteArrayJacksonJsonMessageConverter()
    template.setDefaultTopic("requests")
    return template
}
```

Using the template

- Java
- Kotlin

```java
RequestReplyTypedMessageFuture<String, String, Thing> future1 =
        template.sendAndReceive(MessageBuilder.withPayload("getAThing").build(),
                new ParameterizedTypeReference<Thing>() { });
log.info(future1.getSendFuture().get(10, TimeUnit.SECONDS).getRecordMetadata().toString());
Thing thing = future1.get(10, TimeUnit.SECONDS).getPayload();
log.info(thing.toString());

RequestReplyTypedMessageFuture<String, String, List<Thing>> future2 =
        template.sendAndReceive(MessageBuilder.withPayload("getThings").build(),
                new ParameterizedTypeReference<List<Thing>>() { });
log.info(future2.getSendFuture().get(10, TimeUnit.SECONDS).getRecordMetadata().toString());
List<Thing> things = future2.get(10, TimeUnit.SECONDS).getPayload();
things.forEach(thing1 -> log.info(thing1.toString()));
```

```kotlin
val future1: RequestReplyTypedMessageFuture<String, String, Thing> =
    template.sendAndReceive(MessageBuilder.withPayload("getAThing").build(),
        object : ParameterizedTypeReference<Thing>() {})
log.info(future1.sendFuture?.get(10, TimeUnit.SECONDS)?.recordMetadata.toString())
val thing = future1.get(10, TimeUnit.SECONDS).payload
log.info(thing.toString())

val future2: RequestReplyTypedMessageFuture<String, String, List<Thing>> =
    template.sendAndReceive(MessageBuilder.withPayload("getThings").build(),
        object : ParameterizedTypeReference<List<Thing>>() {})
log.info(future2.sendFuture?.get(10, TimeUnit.SECONDS)?.recordMetadata.toString())
val things = future2.get(10, TimeUnit.SECONDS).payload
things.forEach { thing1 -> log.info(thing1.toString()) }
```

<a id="kafka-sending-messages--reply-message"></a>
<a id="kafka-sending-messages--reply-type-message"></a>

## Reply Type Message<?>

When the `@KafkaListener` returns a `Message<?>`, with versions before 2.5, it was necessary to populate the reply topic and correlation id headers.
In this example, we use the reply topic header from the request:

```java
@KafkaListener(id = "requestor", topics = "request")
@SendTo
public Message<?> messageReturn(String in) {
    return MessageBuilder.withPayload(in.toUpperCase())
            .setHeader(KafkaHeaders.TOPIC, replyTo)
            .setHeader(KafkaHeaders.KEY, 42)
            .setHeader(KafkaHeaders.CORRELATION_ID, correlation)
            .build();
}
```

This also shows how to set a key on the reply record.

Starting with version 2.5, the framework will detect if these headers are missing and populate them with the topic - either the topic determined from the `@SendTo` value or the incoming `KafkaHeaders.REPLY_TOPIC` header (if present).
It will also echo the incoming `KafkaHeaders.CORRELATION_ID` and `KafkaHeaders.REPLY_PARTITION`, if present.

```java
@KafkaListener(id = "requestor", topics = "request")
@SendTo  // default REPLY_TOPIC header
public Message<?> messageReturn(String in) {
    return MessageBuilder.withPayload(in.toUpperCase())
            .setHeader(KafkaHeaders.KEY, 42)
            .build();
}
```

<a id="kafka-sending-messages--_original_record_key_in_reply"></a>
<a id="kafka-sending-messages--original-record-key-in-reply"></a>

### Original Record Key in Reply

Starting with version 3.3, the Kafka record key from the incoming request (if it exists) will be preserved in the reply record.
This is only applicable for single record request/reply scenario.
When the listener is batch or when the return type is a collection, it is up to the application to specify which keys to use by wrapping the reply record in a `Message` type.

<a id="kafka-sending-messages--aggregating-request-reply"></a>
<a id="kafka-sending-messages--aggregating-multiple-replies"></a>

## Aggregating Multiple Replies

The template in [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template) is strictly for a single request/reply scenario.
For cases where multiple receivers of a single message return a reply, you can use the `AggregatingReplyingKafkaTemplate`.
This is an implementation of the client-side of the [Scatter-Gather Enterprise Integration Pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html).

Like the `ReplyingKafkaTemplate`, the `AggregatingReplyingKafkaTemplate` constructor takes a producer factory and a listener container to receive the replies; it has a third parameter `BiPredicate<List<ConsumerRecord<K, R>>, Boolean> releaseStrategy` which is consulted each time a reply is received; when the predicate returns `true`, the collection of `ConsumerRecord`s is used to complete the `Future` returned by the `sendAndReceive` method.

There is an additional property `returnPartialOnTimeout` (default false).
When this is set to `true`, instead of completing the future with a `KafkaReplyTimeoutException`, a partial result completes the future normally (as long as at least one reply record has been received).

Starting with version 2.3.5, the predicate is also called after a timeout (if `returnPartialOnTimeout` is `true`).
The first argument is the current list of records; the second is `true` if this call is due to a timeout.
The predicate can modify the list of records.

```java
AggregatingReplyingKafkaTemplate<Integer, String, String> template =
        new AggregatingReplyingKafkaTemplate<>(producerFactory, container,
                        coll -> coll.size() == releaseSize);
...
RequestReplyFuture<Integer, String, Collection<ConsumerRecord<Integer, String>>> future =
        template.sendAndReceive(record);
future.getSendFuture().get(10, TimeUnit.SECONDS); // send ok
ConsumerRecord<Integer, Collection<ConsumerRecord<Integer, String>>> consumerRecord =
        future.get(30, TimeUnit.SECONDS);
```

Notice that the return type is a `ConsumerRecord` with a value that is a collection of `ConsumerRecord`s.
The "outer" `ConsumerRecord` is not a "real" record, it is synthesized by the template, as a holder for the actual reply records received for the request.
When a normal release occurs (release strategy returns true), the topic is set to `aggregatedResults`; if `returnPartialOnTimeout` is true, and timeout occurs (and at least one reply record has been received), the topic is set to `partialResultsAfterTimeout`.
The template provides constant static variables for these "topic" names:

```java
/** * Pseudo topic name for the "outer" {@link ConsumerRecords} that has the aggregated * results in its value after a normal release by the release strategy.*/ public static final String AGGREGATED_RESULTS_TOPIC = "aggregatedResults";
/** * Pseudo topic name for the "outer" {@link ConsumerRecords} that has the aggregated * results in its value after a timeout.*/ public static final String PARTIAL_RESULTS_AFTER_TIMEOUT_TOPIC = "partialResultsAfterTimeout";
```

The real `ConsumerRecord`s in the `Collection` contain the actual topic(s) from which the replies are received.

> [!IMPORTANT]
> The listener container for the replies **must** be configured with `AckMode.MANUAL` or `AckMode.MANUAL_IMMEDIATE`; the consumer property `enable.auto.commit` must be `false` (the default since version 2.3).
> To avoid any possibility of losing messages, the template only commits offsets when there are zero requests outstanding, i.e. when the last outstanding request is released by the release strategy.
> After a rebalance, it is possible for duplicate reply deliveries; these will be ignored for any in-flight requests; you may see error log messages when duplicate replies are received for already released replies.

> [!NOTE]
> If you use an [`ErrorHandlingDeserializer`](#kafka-serdes--error-handling-deserializer) with this aggregating template, the framework will not automatically detect `DeserializationException`s.
> Instead, the record (with a `null` value) will be returned intact, with the deserialization exception(s) in headers.
> It is recommended that applications call the utility method `ReplyingKafkaTemplate.checkDeserialization()` method to determine if a deserialization exception occurred.
> See its JavaDocs for more information.
> The `replyErrorChecker` is also not called for this aggregating template; you should perform the checks on each element of the reply.

[Configuring Topics](#kafka-configuring-topics)
[Receiving Messages](#kafka-receiving-messages)

---

<a id="kafka-receiving-messages"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages.html -->

<!-- page_index: 10 -->

# Receiving Messages

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages--page-title"></a>
<a id="kafka-receiving-messages--receiving-messages"></a>

# Receiving Messages

You can receive messages by configuring a `MessageListenerContainer` and providing a message listener or by using the `@KafkaListener` annotation.

<a id="kafka-receiving-messages--section-summary"></a>

## Section Summary

- [Message Listeners](#kafka-receiving-messages-message-listeners)
- [Message Listener Containers](#kafka-receiving-messages-message-listener-container)
- [Manually Committing Offsets](#kafka-receiving-messages-ooo-commits)
- [Asynchronous `@KafkaListener` Return Types](#kafka-receiving-messages-async-returns)
- [`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation)
- [Obtaining the Consumer `group.id`](#kafka-receiving-messages-listener-group-id)
- [Container Thread Naming](#kafka-receiving-messages-container-thread-naming)
- [`@KafkaListener` as a Meta Annotation](#kafka-receiving-messages-listener-meta)
- [`@KafkaListener` on a Class](#kafka-receiving-messages-class-level-kafkalistener)
- [`@KafkaListener` Attribute Modification](#kafka-receiving-messages-kafkalistener-attrs)
- [`@KafkaListener` Lifecycle Management](#kafka-receiving-messages-kafkalistener-lifecycle)
- [`@KafkaListener` `@Payload` Validation](#kafka-receiving-messages-validation)
- [Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners)
- [Enforcing Consumer Rebalance](#kafka-receiving-messages-enforced-rebalance)
- [Forwarding Listener Results using `@SendTo`](#kafka-receiving-messages-annotation-send-to)
- [Filtering Messages](#kafka-receiving-messages-filtering)
- [Retrying Deliveries](#kafka-receiving-messages-retrying-deliveries)
- [Starting `@KafkaListener`s in Sequence](#kafka-receiving-messages-sequencing)
- [Using `KafkaTemplate` to Receive](#kafka-receiving-messages-template-receive)

[Sending Messages](#kafka-sending-messages)
[Message Listeners](#kafka-receiving-messages-message-listeners)

---

<a id="kafka-receiving-messages-message-listeners"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/message-listeners.html -->

<!-- page_index: 11 -->

# Message Listeners

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-message-listeners--page-title"></a>
<a id="kafka-receiving-messages-message-listeners--message-listeners"></a>

# Message Listeners

When you use a [message listener container](#kafka-receiving-messages-message-listener-container), you must provide a listener to receive data.
There are currently eight supported interfaces for message listeners.
The following listing shows these interfaces:

```java
public interface MessageListener<K, V> { (1)
void onMessage(ConsumerRecord<K, V> data);
}
public interface AcknowledgingMessageListener<K, V> extends MessageListener<K, V> { (2)
void onMessage(ConsumerRecord<K, V> data, Acknowledgment acknowledgment);
}
public interface ConsumerAwareMessageListener<K, V> extends MessageListener<K, V> { (3)
void onMessage(ConsumerRecord<K, V> data, Consumer<?, ?> consumer);
}
public interface AcknowledgingConsumerAwareMessageListener<K, V> extends MessageListener<K, V> { (4)
void onMessage(ConsumerRecord<K, V> data, Acknowledgment acknowledgment, Consumer<?, ?> consumer);
}
public interface BatchMessageListener<K, V> { (5)
void onMessage(List<ConsumerRecord<K, V>> data);
}
public interface BatchAcknowledgingMessageListener<K, V> { (6)
void onMessage(List<ConsumerRecord<K, V>> data, Acknowledgment acknowledgment);
}
public interface BatchConsumerAwareMessageListener<K, V> extends BatchMessageListener<K, V> { (7)
void onMessage(List<ConsumerRecord<K, V>> data, Consumer<?, ?> consumer);
}
public interface BatchAcknowledgingConsumerAwareMessageListener<K, V> extends BatchMessageListener<K, V> { (8)
void onMessage(List<ConsumerRecord<K, V>> data, Acknowledgment acknowledgment, Consumer<?, ?> consumer);
}
```

**1**

Use this interface for processing individual `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using auto-commit or one of the container-managed [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).

**2**

Use this interface for processing individual `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using one of the manual [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).

**3**

Use this interface for processing individual `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using auto-commit or one of the container-managed [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).
Access to the `Consumer` object is provided.

**4**

Use this interface for processing individual `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using one of the manual [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).
Access to the `Consumer` object is provided.

**5**

Use this interface for processing all `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using auto-commit or one of the container-managed [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).
`AckMode.RECORD` is not supported when you use this interface, since the listener is given the complete batch.

**6**

Use this interface for processing all `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using one of the manual [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).

**7**

Use this interface for processing all `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using auto-commit or one of the container-managed [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).
`AckMode.RECORD` is not supported when you use this interface, since the listener is given the complete batch.
Access to the `Consumer` object is provided.

**8**

Use this interface for processing all `ConsumerRecord` instances received from the Kafka consumer `poll()` operation when using one of the manual [commit methods](#kafka-receiving-messages-message-listener-container--committing-offsets).
Access to the `Consumer` object is provided.

> [!IMPORTANT]
> The `Consumer` object is not thread-safe.
> You must only invoke its methods on the thread that calls the listener.

> [!IMPORTANT]
> You should not execute any `Consumer<?, ?>` methods that affect the consumer’s positions or committed offsets in your listener; the container needs to manage such information.

[Receiving Messages](#kafka-receiving-messages)
[Message Listener Containers](#kafka-receiving-messages-message-listener-container)

---

<a id="kafka-receiving-messages-message-listener-container"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/message-listener-container.html -->

<!-- page_index: 12 -->

# Message Listener Containers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-message-listener-container--page-title"></a>
<a id="kafka-receiving-messages-message-listener-container--message-listener-containers"></a>

# Message Listener Containers

Two `MessageListenerContainer` implementations are provided:

- `KafkaMessageListenerContainer`
- `ConcurrentMessageListenerContainer`

The `KafkaMessageListenerContainer` receives all messages from all topics or partitions on a single thread.
The `ConcurrentMessageListenerContainer` delegates to one or more `KafkaMessageListenerContainer` instances to provide multi-threaded consumption.

Starting with version 2.2.7, you can add a `RecordInterceptor` to the listener container; it will be invoked before calling the listener allowing inspection or modification of the record.
If the interceptor returns null, the listener is not called.
Starting with version 2.7, it has additional methods which are called after the listener exits (normally, or by throwing an exception).
Also, starting with version 2.7, there is now a `BatchInterceptor`, providing similar functionality for [Batch Listeners](#kafka-receiving-messages-listener-annotation--batch-listeners).
In addition, the `ConsumerAwareRecordInterceptor` (and `BatchInterceptor`) provide access to the `Consumer<?, ?>`.
This might be used, for example, to access the consumer metrics in the interceptor.

> [!IMPORTANT]
> You should not execute any methods that affect the consumer’s positions and/or committed offsets in these interceptors; the container needs to manage such information.

> [!IMPORTANT]
> If the interceptor mutates the record (by creating a new one), the `topic`, `partition`, and `offset` must remain the same to avoid unexpected side effects such as record loss.

The `CompositeRecordInterceptor` and `CompositeBatchInterceptor` can be used to invoke multiple interceptors.

Starting with version 4.0, `AbstractKafkaListenerContainerFactory` and `AbstractMessageListenerContainer` exposes `getRecordInterceptor()` and `getBatchInterceptor()` as public methods.
If the returned interceptor is an instance of `CompositeRecordInterceptor` or `CompositeBatchInterceptor`, additional `RecordInterceptor` or `BatchInterceptor` instances can be added to it even after the container instance extending `AbstractMessageListenerContainer` has been created and a `RecordInterceptor` or `BatchInterceptor` has already been configured.
The following example shows how to do so:

```java
public void configureRecordInterceptor(AbstractKafkaListenerContainerFactory<Integer, String> containerFactory) {
    CompositeRecordInterceptor compositeInterceptor;

    RecordInterceptor<Integer, String> previousInterceptor = containerFactory.getRecordInterceptor();
    if (previousInterceptor instanceof CompositeRecordInterceptor interceptor) {
        compositeInterceptor = interceptor;
    } else {
        compositeInterceptor = new CompositeRecordInterceptor<>();
        containerFactory.setRecordInterceptor(compositeInterceptor);
        if (previousInterceptor != null) {
            compositeInterceptor.addRecordInterceptor(previousInterceptor);
        }
    }

    RecordInterceptor<Integer, String> recordInterceptor1 = new RecordInterceptor() {...};
    RecordInterceptor<Integer, String> recordInterceptor2 = new RecordInterceptor() {...};

    compositeInterceptor.addRecordInterceptor(recordInterceptor1);
    compositeInterceptor.addRecordInterceptor(recordInterceptor2);
}
```

By default, starting with version 2.8, when using transactions, the interceptor is invoked before the transaction has started.
You can set the listener container’s `interceptBeforeTx` property to `false` to invoke the interceptor after the transaction has started instead.
Starting with version 2.9, this will apply to any transaction manager, not just `KafkaAwareTransactionManager`s.
This allows, for example, the interceptor to participate in a JDBC transaction started by the container.

Starting with versions 2.3.8, 2.4.6, the `ConcurrentMessageListenerContainer` now supports [Static Membership](https://kafka.apache.org/42/documentation/#static_membership) when the concurrency is greater than one.
The `group.instance.id` is suffixed with `-n` with `n` starting at `1`.
This, together with an increased `session.timeout.ms`, can be used to reduce rebalance events, for example, when application instances are restarted.

<a id="kafka-receiving-messages-message-listener-container--kafka-container"></a>
<a id="kafka-receiving-messages-message-listener-container--using-kafkamessagelistenercontainer"></a>

## Using `KafkaMessageListenerContainer`

The following constructor is available:

```java
public KafkaMessageListenerContainer(ConsumerFactory<K, V> consumerFactory,
                    ContainerProperties containerProperties)
```

It receives a `ConsumerFactory` and information about topics and partitions, as well as other configuration, in a `ContainerProperties`
object.
`ContainerProperties` has the following constructors:

```java
public ContainerProperties(TopicPartitionOffset... topicPartitions)

public ContainerProperties(String... topics)

public ContainerProperties(Pattern topicPattern)
```

The first constructor takes an array of `TopicPartitionOffset` arguments to explicitly instruct the container about which partitions to use (using the consumer `assign()` method) and with an optional initial offset.
A positive value is an absolute offset by default.
A negative value is relative to the current last offset within a partition by default.
A constructor for `TopicPartitionOffset` that takes an additional `boolean` argument is provided.
If this is `true`, the initial offsets (positive or negative) are relative to the current position for this consumer.
The offsets are applied when the container is started.
The second takes an array of topics, and Kafka allocates the partitions based on the `group.id` property — distributing partitions across the group.
The third uses a regex `Pattern` to select the topics.

To assign a `MessageListener` to a container, you can use the `ContainerProps.setMessageListener` method when creating the Container.
The following example shows how to do so:

```java
ContainerProperties containerProps = new ContainerProperties("topic1", "topic2"); containerProps.setMessageListener(new MessageListener<Integer, String>() {...}); DefaultKafkaConsumerFactory<Integer, String> cf =new DefaultKafkaConsumerFactory<>(consumerProps()); KafkaMessageListenerContainer<Integer, String> container =new KafkaMessageListenerContainer<>(cf, containerProps); return container;
```

Note that when creating a `DefaultKafkaConsumerFactory`, using the constructor that just takes in the properties as above means that key and value `Deserializer` classes are picked up from configuration.
Alternatively, `Deserializer` instances may be passed to the `DefaultKafkaConsumerFactory` constructor for key and/or value, in which case all Consumers share the same instances.
Another option is to provide `Supplier<Deserializer>`s (starting with version 2.3) that will be used to obtain separate `Deserializer` instances for each `Consumer`:

```java
DefaultKafkaConsumerFactory<Integer, CustomValue> cf =
                        new DefaultKafkaConsumerFactory<>(consumerProps(), null, () -> new CustomValueDeserializer());
KafkaMessageListenerContainer<Integer, String> container =
                        new KafkaMessageListenerContainer<>(cf, containerProps);
return container;
```

Refer to the [Javadoc](https://docs.spring.io/spring-kafka/docs/4.1.0/api/org/springframework/kafka/listener/ContainerProperties.html) for `ContainerProperties` for more information about the various properties that you can set.

Since version 2.1.1, a new property called `logContainerConfig` is available.
When `true` and `INFO` logging is enabled each listener container writes a log message summarizing its configuration properties.

By default, logging of topic offset commits is performed at the `DEBUG` logging level.
Starting with version 2.1.2, a property in `ContainerProperties` called `commitLogLevel` lets you specify the log level for these messages.
For example, to change the log level to `INFO`, you can use `containerProperties.setCommitLogLevel(LogIfLevelEnabled.Level.INFO);`.

Starting with version 2.2, a new container property called `missingTopicsFatal` has been added (default: `false` since 2.3.4).
This prevents the container from starting if any of the configured topics are not present on the broker.
It does not apply if the container is configured to listen to a topic pattern (regex).
Previously, the container threads looped within the `consumer.poll()` method waiting for the topic to appear while logging many messages.
Aside from the logs, there was no indication that there was a problem.

As of version 2.8, a new container property `authExceptionRetryInterval` has been introduced.
This causes the container to retry fetching messages after getting any `AuthenticationException` or `AuthorizationException` from the `KafkaConsumer`.
This can happen when, for example, the configured user is denied access to read a certain topic or credentials are incorrect.
Defining `authExceptionRetryInterval` allows the container to recover when proper permissions are granted.

> [!NOTE]
> By default, no interval is configured - authentication and authorization errors are considered fatal, which causes the container to stop.

Starting with version 2.8, when creating the consumer factory, if you provide deserializers as objects (in the constructor or via the setters), the factory will invoke the `configure()` method to configure them with the configuration properties.

<a id="kafka-receiving-messages-message-listener-container--using-concurrentmessagelistenercontainer"></a>

## Using `ConcurrentMessageListenerContainer`

The single constructor is similar to the `KafkaListenerContainer` constructor.
The following listing shows the constructor’s signature:

```java
public ConcurrentMessageListenerContainer(ConsumerFactory<K, V> consumerFactory,
                            ContainerProperties containerProperties)
```

It also has a `concurrency` property.
For example, `container.setConcurrency(3)` creates three `KafkaMessageListenerContainer` instances.

If the container properties are configured for topics (or topic pattern), Kafka distributes the partitions across the consumers using its group management capabilities.

> [!IMPORTANT]
> When listening to multiple topics, the default partition distribution may not be what you expect.
> For example, if you have three topics with five partitions each and you want to use `concurrency=15`, you see only five active consumers, each assigned one partition from each topic, with the other 10 consumers being idle.
> This is because the default Kafka `ConsumerPartitionAssignor` is the `RangeAssignor` (see its Javadoc).
> For this scenario, you may want to consider using the `RoundRobinAssignor` instead, which distributes the partitions across all of the consumers.
> Then, each consumer is assigned one topic or partition.
> To change the `ConsumerPartitionAssignor`, you can set the `partition.assignment.strategy` consumer property (`ConsumerConfig.PARTITION_ASSIGNMENT_STRATEGY_CONFIG`) in the properties provided to the `DefaultKafkaConsumerFactory`.
>
> When using Spring Boot, you can assign set the strategy as follows:
>
> ```none
> spring.kafka.consumer.properties.partition.assignment.strategy=\
> org.apache.kafka.clients.consumer.RoundRobinAssignor
> ```

When the container properties are configured with `TopicPartitionOffset`s, the `ConcurrentMessageListenerContainer` distributes the `TopicPartitionOffset` instances across the delegate `KafkaMessageListenerContainer` instances.

If, say, six `TopicPartitionOffset` instances are provided and the `concurrency` is `3`; each container gets two partitions.
For five `TopicPartitionOffset` instances, two containers get two partitions, and the third gets one.
If the `concurrency` is greater than the number of `TopicPartitions`, the `concurrency` is adjusted down such that each container gets one partition.

> [!NOTE]
> The `client.id` property (if set) is appended with `-n` where `n` is the consumer instance that corresponds to the concurrency.
> This is required to provide unique names for MBeans when JMX is enabled.

Starting with version 1.3, the `MessageListenerContainer` provides access to the metrics of the underlying `KafkaConsumer`.
In the case of `ConcurrentMessageListenerContainer`, the `metrics()` method returns the metrics for all the target `KafkaMessageListenerContainer` instances.
The metrics are grouped into the `Map<MetricName, ? extends Metric>` by the `client-id` provided for the underlying `KafkaConsumer`.

Starting with version 2.3, the `ContainerProperties` provides an `idleBetweenPolls` option to let the main loop in the listener container to sleep between `KafkaConsumer.poll()` calls.
An actual sleep interval is selected as the minimum from the provided option and difference between the `max.poll.interval.ms` consumer config and the current records batch processing time.

<a id="kafka-receiving-messages-message-listener-container--committing-offsets"></a>

## Committing Offsets

Several options are provided for committing offsets.
If the `enable.auto.commit` consumer property is `true`, Kafka auto-commits the offsets according to its configuration.
If it is `false`, the containers support several `AckMode` settings (described in the next list).
The default `AckMode` is `BATCH`.
Starting with version 2.3, the framework sets `enable.auto.commit` to `false` unless explicitly set in the configuration.
Previously, the Kafka default (`true`) was used if the property was not set.

The consumer `poll()` method returns one or more `ConsumerRecords`.
The `MessageListener` is called for each record.
The following lists describes the action taken by the container for each `AckMode` (when transactions are not being used):

- `RECORD`: Commit the offset when the listener returns after processing the record.
- `BATCH`: Commit the offset when all the records returned by the `poll()` have been processed.
- `TIME`: Commit the offset when all the records returned by the `poll()` have been processed, as long as the `ackTime` since the last commit has been exceeded.
- `COUNT`: Commit the offset when all the records returned by the `poll()` have been processed, as long as `ackCount` records have been received since the last commit.
- `COUNT_TIME`: Similar to `TIME` and `COUNT`, but the commit is performed if either condition is `true`.
- `MANUAL`: The message listener is responsible to `acknowledge()` the `Acknowledgment`.
  After that, the same semantics as `BATCH` are applied.
- `MANUAL_IMMEDIATE`: Commit the offset immediately when the `Acknowledgment.acknowledge()` method is called by the listener.

When using [transactions](#kafka-transactions), the offset(s) are sent to the transaction and the semantics are equivalent to `RECORD` or `BATCH`, depending on the listener type (record or batch).

> [!NOTE]
> `MANUAL` and `MANUAL_IMMEDIATE` require the listener to be an `AcknowledgingMessageListener` or a `BatchAcknowledgingMessageListener`.
> See [Message Listeners](#kafka-receiving-messages-message-listeners).

Depending on the `syncCommits` container property, the `commitSync()` or `commitAsync()` method on the consumer is used.
`syncCommits` is `true` by default; also see `setSyncCommitTimeout`.
See `setCommitCallback` to get the results of asynchronous commits; the default callback is the `LoggingCommitCallback` which logs errors (and successes at debug level).

Because the listener container has its own mechanism for committing offsets, it prefers the Kafka `ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG` to be `false`.
Starting with version 2.3, it unconditionally sets it to false unless specifically set in the consumer factory or the container’s consumer property overrides.

The `Acknowledgment` has the following method:

```java
public interface Acknowledgment {

    void acknowledge();

}
```

This method gives the listener control over when offsets are committed.

Starting with version 2.3, the `Acknowledgment` interface has two additional methods `nack(long sleep)` and `nack(int index, long sleep)`.
The first one is used with a record listener, the second with a batch listener.
Calling the wrong method for your listener type will throw an `IllegalStateException`.

> [!NOTE]
> If you want to commit a partial batch, using `nack()`, When using transactions, set the `AckMode` to `MANUAL`; invoking `nack()` will send the offsets of the successfully processed records to the transaction.

> [!IMPORTANT]
> `nack()` can only be called on the consumer thread that invokes your listener.

> [!IMPORTANT]
> `nack()` is not allowed when using [Out of Order Commits](#kafka-receiving-messages-ooo-commits).

With a record listener, when `nack()` is called, any pending offsets are committed, the remaining records from the last poll are discarded, and seeks are performed on their partitions so that the failed record and unprocessed records are redelivered on the next `poll()`.
The consumer can be paused before redelivery, by setting the `sleep` argument.
This is similar functionality to throwing an exception when the container is configured with a `DefaultErrorHandler`.

> [!IMPORTANT]
> `nack()` pauses the entire listener for the specified sleep duration including all assigned partitions.

When using a batch listener, you can specify the index within the batch where the failure occurred.
When `nack()` is called, offsets will be committed for records before the index and seeks are performed on the partitions for the failed and discarded records so that they will be redelivered on the next `poll()`.

See [Container Error Handlers](#kafka-annotation-error-handling--error-handlers) for more information.

> [!IMPORTANT]
> The consumer is paused during the sleep so that we continue to poll the broker to keep the consumer alive.
> The actual sleep time, and its resolution, depends on the container’s `pollTimeout` which defaults to 5 seconds.
> The minimum sleep time is equal to the `pollTimeout` and all sleep times will be a multiple of it.
> For small sleep times or, to increase its accuracy, consider reducing the container’s `pollTimeout`.

Starting with version 3.0.10, batch listeners can commit the offsets of parts of the batch, using `acknowledge(index)` on the `Acknowledgment` argument.
When this method is called, the offset of the record at the index (as well as all previous records) will be committed.
Calling `acknowledge()` after a partial batch commit is performed will commit the offsets of the remainder of the batch.
The following limitations apply:

- `AckMode.MANUAL_IMMEDIATE` is required
- The method must be called on the listener thread
- The listener must consume a `List` rather than the raw `ConsumerRecords`
- The index must be in the range of the list’s elements
- The index must be larger than that used in a previous call

These restrictions are enforced and the method will throw an `IllegalArgumentException` or `IllegalStateException`, depending on the violation.

<a id="kafka-receiving-messages-message-listener-container--container-auto-startup"></a>
<a id="kafka-receiving-messages-message-listener-container--listener-container-auto-startup"></a>

## Listener Container Auto Startup

The listener containers implement `SmartLifecycle`, and `autoStartup` is `true` by default.
The containers are started in a late phase (`Integer.MAX-VALUE - 100`).
Other components that implement `SmartLifecycle`, to handle data from listeners, should be started in an earlier phase.
The `- 100` leaves room for later phases to enable components to be auto-started after the containers.

[Message Listeners](#kafka-receiving-messages-message-listeners)
[Manually Committing Offsets](#kafka-receiving-messages-ooo-commits)

---

<a id="kafka-receiving-messages-ooo-commits"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/ooo-commits.html -->

<!-- page_index: 13 -->

# Manually Committing Offsets

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-ooo-commits--page-title"></a>
<a id="kafka-receiving-messages-ooo-commits--manually-committing-offsets"></a>

# Manually Committing Offsets

Normally, when using `AckMode.MANUAL` or `AckMode.MANUAL_IMMEDIATE`, the acknowledgments must be acknowledged in order, because Kafka does not maintain state for each record, only a committed offset for each group/partition.
Starting with version 2.8, you can now set the container property `asyncAcks`, which allows the acknowledgments for records returned by the poll to be acknowledged in any order.
The listener container will defer the out-of-order commits until the missing acknowledgments are received.
The consumer will be paused (no new records delivered) until all the offsets for the previous poll have been committed.

> [!IMPORTANT]
> While this feature allows applications to process records asynchronously, it should be understood that it increases the possibility of duplicate deliveries after a failure.

> [!IMPORTANT]
> When `asyncAcks` is activated, it is not possible to use `nack()` (negative acknowledgments) when [Committing Offsets](#kafka-receiving-messages-message-listener-container--committing-offsets).

[Message Listener Containers](#kafka-receiving-messages-message-listener-container)
[Asynchronous `@KafkaListener` Return Types](#kafka-receiving-messages-async-returns)

---

<a id="kafka-receiving-messages-async-returns"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/async-returns.html -->

<!-- page_index: 14 -->

# Asynchronous @KafkaListener Return Types

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-async-returns--page-title"></a>
<a id="kafka-receiving-messages-async-returns--asynchronous-kafkalistener-return-types"></a>

# Asynchronous `@KafkaListener` Return Types

Starting with version 3.2, `@KafkaListener` (and `@KafkaHandler`) methods can be specified with asynchronous return types, letting the reply be sent asynchronously.
return types include `CompletableFuture<?>`, `Mono<?>` and Kotlin `suspend` functions.

```java
@KafkaListener(id = "myListener", topics = "myTopic")
public CompletableFuture<String> listen(String data) {
    ...
    CompletableFuture<String> future = new CompletableFuture<>();
    future.complete("done");
    return future;
}
```

```java
@KafkaListener(id = "myListener", topics = "myTopic")
public Mono<Void> listen(String data) {
    ...
    return Mono.empty();
}
```

> [!IMPORTANT]
> The `AckMode` will be automatically set the `MANUAL` and enable out-of-order commits when async return types are detected; instead, the asynchronous completion will ack when the async operation completes.
> When the async result is completed with an error, whether the message is recover or not depends on the container error handler.
> If some exception occurs within the listener method that prevents creation of the async result object, you MUST catch that exception and return an appropriate return object that will cause the message to be ack or recover.

If a `KafkaListenerErrorHandler` is configured on a listener with an async return type (including Kotlin suspend functions), the error handler is invoked after a failure.
See [Handling Exceptions](#kafka-annotation-error-handling) for more information about this error handler and its purpose.

[Manually Committing Offsets](#kafka-receiving-messages-ooo-commits)
[`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation)

---

<a id="kafka-receiving-messages-listener-annotation"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/listener-annotation.html -->

<!-- page_index: 15 -->

# @KafkaListener Annotation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-listener-annotation--page-title"></a>
<a id="kafka-receiving-messages-listener-annotation--kafkalistener-annotation"></a>

# `@KafkaListener` Annotation

The `@KafkaListener` annotation is used to designate a bean method as a listener for a listener container.
The bean is wrapped in a `MessagingMessageListenerAdapter` configured with various features, such as converters to convert the data, if necessary, to match the method parameters.

You can configure most attributes on the annotation with SpEL by using `#{…}` or property placeholders (`${…}`).
See the [Javadoc](https://docs.spring.io/spring-kafka/docs/4.1.0/api/org/springframework/kafka/annotation/KafkaListener.html) for more information.

<a id="kafka-receiving-messages-listener-annotation--record-listener"></a>
<a id="kafka-receiving-messages-listener-annotation--record-listeners"></a>

## Record Listeners

The `@KafkaListener` annotation provides a mechanism for simple POJO listeners.
The following example shows how to use it:

```java
public class Listener {
@KafkaListener(id = "foo", topics = "myTopic", clientIdPrefix = "myClientId") public void listen(String data) {...}
}
```

This mechanism requires an `@EnableKafka` annotation on one of your `@Configuration` classes and a listener container factory, which is used to configure the underlying `ConcurrentMessageListenerContainer`.
By default, a bean with name `kafkaListenerContainerFactory` is expected.
The following example shows how to use `ConcurrentMessageListenerContainer`:

```java
@Configuration
@EnableKafka
public class KafkaConfig {

    @Bean
    KafkaListenerContainerFactory<ConcurrentMessageListenerContainer<Integer, String>>
                        kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<Integer, String> factory =
                                new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.setConcurrency(3);
        factory.getContainerProperties().setPollTimeout(3000);
        return factory;
    }

    @Bean
    public ConsumerFactory<Integer, String> consumerFactory() {
        return new DefaultKafkaConsumerFactory<>(consumerConfigs());
    }

    @Bean
    public Map<String, Object> consumerConfigs() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        ...
        return props;
    }
}
```

Notice that, to set container properties, you must use the `getContainerProperties()` method on the factory.
It is used as a template for the actual properties injected into the container.

Starting with version 2.1.1, you can now set the `client.id` property for consumers created by the annotation.
The `clientIdPrefix` is suffixed with `-n`, where `n` is an integer representing the container number when using concurrency.

Starting with version 2.2, you can now override the container factory’s `concurrency` and `autoStartup` properties by using properties on the annotation itself.
The properties can be simple values, property placeholders, or SpEL expressions.
The following example shows how to do so:

```java
@KafkaListener(id = "myListener", topics = "myTopic",
        autoStartup = "${listen.auto.start:true}", concurrency = "${listen.concurrency:3}")
public void listen(String data) {
    ...
}
```

<a id="kafka-receiving-messages-listener-annotation--topic-partition-assignment"></a>

## Topic Partition Assignment

You can configure the topic for `@KafkaListener` in three ways.
You must configure the topic in one of these ways.

```java
@KafkaListener(id = "myListener", topics = "myTopic") public void listen(String data) {...}
@KafkaListener(id = "myListener", topicPattern = "my.*") public void listen(String data) {...}
@KafkaListener(id = "myListener", topicPartitions = { @TopicPartition(topic = "myTopic", partitions = { "0", "1" })}) public void listen(String data) {...}
```

You can simply configure the topic directly by name.
In this case, you can also configure the multiple topics like `topics = {"myTopic1", myTopic2"}`.

You can also configure topics using topicPattern, which enables topic subscription based on a regular expression.

When you configure topics using either of these ways (topic or topic pattern), Kafka automatically assigns partitions according to the consumer group.
Alternatively, you can configure POJO listeners with explicit topics and partitions (and, optionally, their initial offsets).
The following example shows how to do so:

```java
@KafkaListener(id = "thing2", topicPartitions ={ @TopicPartition(topic = "topic1", partitions = { "0", "1" }),@TopicPartition(topic = "topic2", partitions = "0",partitionOffsets = @PartitionOffset(partition = "1", initialOffset = "100")) }) public void listen(ConsumerRecord<?, ?> record) {...}
```

You can specify each partition in the `partitions` or `partitionOffsets` attribute but not both.

As with most annotation properties, you can use SpEL expressions; for an example of how to generate a large list of partitions, see [Manually Assigning All Partitions](#tips).

Starting with version 2.5.5, you can apply an initial offset to all assigned partitions:

```java
@KafkaListener(id = "thing3", topicPartitions =
        { @TopicPartition(topic = "topic1", partitions = { "0", "1" },
             partitionOffsets = @PartitionOffset(partition = "*", initialOffset = "0"))
        })
public void listen(ConsumerRecord<?, ?> record) {
    ...
}
```

The `*` wildcard represents all partitions in the `partitions` attribute.
There must only be one `@PartitionOffset` with the wildcard in each `@TopicPartition`.

In addition, when the listener implements `ConsumerSeekAware`, `onPartitionsAssigned` is now called, even when using manual assignment.
This allows, for example, any arbitrary seek operations at that time.

Starting with version 2.6.4, you can specify a comma-delimited list of partitions, or partition ranges:

```java
@KafkaListener(id = "pp", autoStartup = "false",
        topicPartitions = @TopicPartition(topic = "topic1",
                partitions = "0-5, 7, 10-15"))
public void process(String in) {
    ...
}
```

The range is inclusive; the example above will assign partitions `0, 1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15`.

The same technique can be used when specifying initial offsets:

```java
@KafkaListener(id = "thing3", topicPartitions =
        { @TopicPartition(topic = "topic1",
             partitionOffsets = @PartitionOffset(partition = "0-5", initialOffset = "0"))
        })
public void listen(ConsumerRecord<?, ?> record) {
    ...
}
```

The initial offset will be applied to all 6 partitions.

Since 3.2, `@PartitionOffset` support `SeekPosition.END`, `SeekPosition.BEGINNING`, `SeekPosition.TIMESTAMP`, `seekPosition` match `SeekPosition` enum name:

```java
@KafkaListener(id = "seekPositionTime", topicPartitions = {@TopicPartition(topic = TOPIC_SEEK_POSITION, partitionOffsets = {@PartitionOffset(partition = "0", initialOffset = "723916800000", seekPosition = "TIMESTAMP"),@PartitionOffset(partition = "1", initialOffset = "0", seekPosition = "BEGINNING"),@PartitionOffset(partition = "2", initialOffset = "0", seekPosition = "END") }) }) public void listen(ConsumerRecord<?, ?> record) {...}
```

If seekPosition set `END` or `BEGINNING` will ignore `initialOffset` and `relativeToCurrent`.
If seekPosition set `TIMESTAMP`, `initialOffset` means timestamp.

<a id="kafka-receiving-messages-listener-annotation--manual-acknowledgment"></a>

## Manual Acknowledgment

When using manual `AckMode`, you can also provide the listener with the `Acknowledgment`.
To activate the manual `AckMode`, you need to set the ack-mode in `ContainerProperties` to the appropriate manual mode.
The following example also shows how to use a different container factory.
This custom container factory must set the `AckMode` to a manual type by calling the `getContainerProperties()` and then calling `setAckMode` on it.
Otherwise, the `Acknowledgment` object will be null.

```java
@KafkaListener(id = "cat", topics = "myTopic",
          containerFactory = "kafkaManualAckListenerContainerFactory")
public void listen(String data, Acknowledgment ack) {
    ...
    ack.acknowledge();
}
```

Starting with version 4.1, you can override the container factory’s default `AckMode` directly on the `@KafkaListener` annotation using the `ackMode` attribute:

```java
@KafkaListener(id = "manual", topics = "myTopic", ackMode = "MANUAL")
public void listen(String data, Acknowledgment ack) {
    ...
    ack.acknowledge();
}
```

The `ackMode` attribute accepts string values corresponding to `ContainerProperties.AckMode` enum values.
This eliminates the need to create separate container factories solely for different acknowledgment modes.
The attribute can also be configured as SpEL expression (`#{…}`) or property placeholders (`${…}`).

<a id="kafka-receiving-messages-listener-annotation--consumer-record-metadata"></a>

## Consumer Record Metadata

Finally, metadata about the record is available from message headers.
You can use the following header names to retrieve the headers of the message:

- `KafkaHeaders.OFFSET`
- `KafkaHeaders.RECEIVED_KEY`
- `KafkaHeaders.RECEIVED_TOPIC`
- `KafkaHeaders.RECEIVED_PARTITION`
- `KafkaHeaders.RECEIVED_TIMESTAMP`
- `KafkaHeaders.TIMESTAMP_TYPE`

Starting with version 2.5 the `RECEIVED_KEY` is not present if the incoming record has a `null` key; previously the header was populated with a `null` value.
This change is to make the framework consistent with `spring-messaging` conventions where `null` valued headers are not present.

The following example shows how to use the headers:

```java
@KafkaListener(id = "qux", topics = "myTopic1") public void listen(@Payload String foo,@Header(name = KafkaHeaders.RECEIVED_KEY, required = false) Integer key,@Header(KafkaHeaders.RECEIVED_PARTITION) int partition,@Header(KafkaHeaders.RECEIVED_TOPIC) String topic,@Header(KafkaHeaders.RECEIVED_TIMESTAMP) long ts ) {...}
```

> [!IMPORTANT]
> Parameter annotations (`@Payload`, `@Header`) must be specified on the concrete implementation of the listener method; they will not be detected if they are defined on an interface.

Starting with version 2.5, instead of using discrete headers, you can receive record metadata in a `ConsumerRecordMetadata` parameter.

```java
@KafkaListener(...)
public void listen(String str, ConsumerRecordMetadata meta) {
    ...
}
```

This contains all the data from the `ConsumerRecord` except the key and value.

<a id="kafka-receiving-messages-listener-annotation--batch-listeners"></a>

## Batch Listeners

Starting with version 1.1, you can configure `@KafkaListener` methods to receive the entire batch of consumer records received from the consumer poll.

> [!IMPORTANT]
> [Non-Blocking Retries](#retrytopic) are not supported with batch listeners.

To configure the listener container factory to create batch listeners, you can set the `batchListener` property.
The following example shows how to do so:

```java
@Bean
public KafkaListenerContainerFactory<?> batchFactory() {
    ConcurrentKafkaListenerContainerFactory<Integer, String> factory =
            new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.setBatchListener(true);
   return factory;
}
```

> [!NOTE]
> Starting with version 2.8, you can override the factory’s `batchListener` property using the `batch` property on the `@KafkaListener` annotation.
> This, together with the changes to [Container Error Handlers](#kafka-annotation-error-handling--error-handlers) allows the same factory to be used for both record and batch listeners.

> [!NOTE]
> Starting with version 2.9.6, the container factory has separate setters for the `recordMessageConverter` and `batchMessageConverter` properties.
> Previously, there was only one property `messageConverter` which applied to both record and batch listeners.

The following example shows how to receive a list of payloads:

```java
@KafkaListener(id = "list", topics = "myTopic", containerFactory = "batchFactory")
public void listen(List<String> list) {
    ...
}
```

The topic, partition, offset, and so on are available in headers that parallel the payloads.
The following example shows how to use the headers:

```java
@KafkaListener(id = "list", topics = "myTopic", containerFactory = "batchFactory") public void listen(List<String> list,@Header(KafkaHeaders.RECEIVED_KEY) List<Integer> keys,@Header(KafkaHeaders.RECEIVED_PARTITION) List<Integer> partitions,@Header(KafkaHeaders.RECEIVED_TOPIC) List<String> topics,@Header(KafkaHeaders.OFFSET) List<Long> offsets) {...}
```

Alternatively, you can receive a `List` of `Message<?>` objects with each offset and other details in each message, but it must be the only parameter (aside from optional `Acknowledgment`, when using manual commits, and/or `Consumer<?, ?>` parameters) defined on the method.
The following example shows how to do so:

```java
@KafkaListener(id = "listMsg", topics = "myTopic", containerFactory = "batchFactory") public void listen1(List<Message<?>> list) {...}
@KafkaListener(id = "listMsgAck", topics = "myTopic", containerFactory = "batchFactory") public void listen2(List<Message<?>> list, Acknowledgment ack) {...}
@KafkaListener(id = "listMsgAckConsumer", topics = "myTopic", containerFactory = "batchFactory") public void listen3(List<Message<?>> list, Acknowledgment ack, Consumer<?, ?> consumer) {...}
```

No conversion is performed on the payloads in this case.

If the `BatchMessagingMessageConverter` is configured with a `RecordMessageConverter`, you can also add a generic type to the `Message` parameter and the payloads are converted.
See [Payload Conversion with Batch Listeners](#kafka-serdes--payload-conversion-with-batch) for more information.

You can also receive a list of `ConsumerRecord<?, ?>` objects, but it must be the only parameter (aside from optional `Acknowledgment`, when using manual commits and `Consumer<?, ?>` parameters) defined on the method.
The following example shows how to do so:

```java
@KafkaListener(id = "listCRs", topics = "myTopic", containerFactory = "batchFactory") public void listen(List<ConsumerRecord<Integer, String>> list) {...}
@KafkaListener(id = "listCRsAck", topics = "myTopic", containerFactory = "batchFactory") public void listen(List<ConsumerRecord<Integer, String>> list, Acknowledgment ack) {...}
```

Starting with version 2.2, the listener can receive the complete `ConsumerRecords<?, ?>` object returned by the `poll()` method, letting the listener access additional methods, such as `partitions()` (which returns the `TopicPartition` instances in the list) and `records(TopicPartition)` (which gets selective records).
Again, this must be the only parameter (aside from optional `Acknowledgment`, when using manual commits or `Consumer<?, ?>` parameters) on the method.
The following example shows how to do so:

```java
@KafkaListener(id = "pollResults", topics = "myTopic", containerFactory = "batchFactory")
public void pollResults(ConsumerRecords<?, ?> records) {
    ...
}
```

> [!IMPORTANT]
> If the container factory has a `RecordFilterStrategy` configured, it is ignored for `ConsumerRecords<?, ?>` listeners, with a `WARN` log message emitted.
> Records can only be filtered with a batch listener if the `List<?>` form of listener is used.
> By default, records are filtered one-at-a-time; starting with version 2.8, you can override `filterBatch` to filter the entire batch in one call.

<a id="kafka-receiving-messages-listener-annotation--annotation-properties"></a>

## Annotation Properties

Starting with version 2.0, the `id` property (if present) is used as the Kafka consumer `group.id` property, overriding the configured property in the consumer factory, if present.
You can also set `groupId` explicitly or set `idIsGroup` to false to restore the previous behavior of using the consumer factory `group.id`.

You can use property placeholders or SpEL expressions within most annotation properties, as the following example shows:

```java
@KafkaListener(topics = "${some.property}")

@KafkaListener(topics = "#{someBean.someProperty}",
    groupId = "#{someBean.someProperty}.group")
```

Starting with version 2.1.2, the SpEL expressions support a special token: `__listener`.
It is a pseudo bean name that represents the current bean instance within which this annotation exists.

Consider the following example:

```java
@Bean public Listener listener1() {return new Listener("topic1");}
@Bean public Listener listener2() {return new Listener("topic2");}
```

Given the beans in the previous example, we can then use the following:

```java
public class Listener {
private final String topic;
public Listener(String topic) {this.topic = topic;}
@KafkaListener(topics = "#{__listener.topic}",groupId = "#{__listener.topic}.group") public void listen(...) {...}
public String getTopic() {return this.topic;}
}
```

If, in the unlikely event that you have an actual bean called `__listener`, you can change the expression token by using the `beanRef` attribute.
The following example shows how to do so:

```java
@KafkaListener(beanRef = "__x", topics = "#{__x.topic}", groupId = "#{__x.topic}.group")
```

Starting with version 2.2.4, you can specify Kafka consumer properties directly on the annotation, these will override any properties with the same name configured in the consumer factory. You **cannot** specify the `group.id` and `client.id` properties this way; they will be ignored; use the `groupId` and `clientIdPrefix` annotation properties for those.

The properties are specified as individual strings with the normal Java `Properties` file format: `foo:bar`, `foo=bar`, or `foo bar`, as the following example shows:

```java
@KafkaListener(topics = "myTopic", groupId = "group", properties = {
    "max.poll.interval.ms:60000",
    ConsumerConfig.MAX_POLL_RECORDS_CONFIG + "=100"
})
```

The following is an example of the corresponding listeners for the example in [Using `RoutingKafkaTemplate`](#kafka-sending-messages--routing-template).

```java
@KafkaListener(id = "one", topics = "one") public void listen1(String in) {System.out.println("1: " + in);}
@KafkaListener(id = "two", topics = "two",properties = "value.deserializer:org.apache.kafka.common.serialization.ByteArrayDeserializer") public void listen2(byte[] in) {System.out.println("2: " + new String(in));}
```

[Asynchronous `@KafkaListener` Return Types](#kafka-receiving-messages-async-returns)
[Obtaining the Consumer `group.id`](#kafka-receiving-messages-listener-group-id)

---

<a id="kafka-receiving-messages-listener-group-id"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/listener-group-id.html -->

<!-- page_index: 16 -->

# Obtaining the Consumer group.id

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-listener-group-id--page-title"></a>
<a id="kafka-receiving-messages-listener-group-id--obtaining-the-consumer-group.id"></a>

# Obtaining the Consumer `group.id`

When running the same listener code in multiple containers, it may be useful to be able to determine which container (identified by its `group.id` consumer property) that a record came from.

You can call `KafkaUtils.getConsumerGroupId()` on the listener thread to do this.
Alternatively, you can access the group id in a method parameter.

```java
@KafkaListener(id = "id", topics = "someTopic")
public void listener(@Payload String payload, @Header(KafkaHeaders.GROUP_ID) String groupId) {
    ...
}
```

> [!IMPORTANT]
> This is available in record listeners and batch listeners that receive a `List<?>` of records.
> It is **not** available in a batch listener that receives a `ConsumerRecords<?, ?>` argument.
> Use the `KafkaUtils` mechanism in that case.

[`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation)
[Container Thread Naming](#kafka-receiving-messages-container-thread-naming)

---

<a id="kafka-receiving-messages-container-thread-naming"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/container-thread-naming.html -->

<!-- page_index: 17 -->

# Container Thread Naming

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-container-thread-naming--page-title"></a>
<a id="kafka-receiving-messages-container-thread-naming--container-thread-naming"></a>

# Container Thread Naming

A `TaskExecutor` is used to invoke the consumer and the listener.
You can provide a custom executor by setting the `consumerExecutor` property of the container’s `ContainerProperties`.
When using pooled executors, be sure that enough threads are available to handle the concurrency across all the containers in which they are used.
When using the `ConcurrentMessageListenerContainer`, a thread from the executor is used for each consumer (`concurrency`).

If you do not provide a consumer executor, a `SimpleAsyncTaskExecutor` is used for each container.
This executor creates threads with names similar to `<beanName>-C-<n>`.
For the `ConcurrentMessageListenerContainer`, the `<beanName>` part of the thread name becomes `<beanName>-m`, where `m` represents the consumer instance.
`n` increments each time the container is started.
So, with a bean name of `container`, threads in this container will be named `container-0-C-1`, `container-1-C-1` etc., after the container is started the first time; `container-0-C-2`, `container-1-C-2` etc., after a stop and subsequent start.

Starting with version `3.0.1`, you can now change the name of the thread, regardless of which executor is used.
Set the `AbstractMessageListenerContainer.changeConsumerThreadName` property to `true` and the `AbstractMessageListenerContainer.threadNameSupplier` will be invoked to obtain the thread name.
This is a `Function<MessageListenerContainer, String>`, with the default implementation returning `container.getListenerId()`.

[Obtaining the Consumer `group.id`](#kafka-receiving-messages-listener-group-id)
[`@KafkaListener` as a Meta Annotation](#kafka-receiving-messages-listener-meta)

---

<a id="kafka-receiving-messages-listener-meta"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/listener-meta.html -->

<!-- page_index: 18 -->

# @KafkaListener as a Meta Annotation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-listener-meta--page-title"></a>
<a id="kafka-receiving-messages-listener-meta--kafkalistener-as-a-meta-annotation"></a>

# `@KafkaListener` as a Meta Annotation

Starting with version 2.2, you can now use `@KafkaListener` as a meta annotation.
The following example shows how to do so:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@KafkaListener
public @interface MyThreeConsumersListener {

    @AliasFor(annotation = KafkaListener.class, attribute = "id")
    String id();

    @AliasFor(annotation = KafkaListener.class, attribute = "topics")
    String[] topics();

    @AliasFor(annotation = KafkaListener.class, attribute = "concurrency")
    String concurrency() default "3";

}
```

You must alias at least one of `topics`, `topicPattern`, or `topicPartitions` (and, usually, `id` or `groupId` unless you have specified a `group.id` in the consumer factory configuration).
The following example shows how to do so:

```java
@MyThreeConsumersListener(id = "my.group", topics = "my.topic")
public void listen1(String in) {
    ...
}
```

[Container Thread Naming](#kafka-receiving-messages-container-thread-naming)
[`@KafkaListener` on a Class](#kafka-receiving-messages-class-level-kafkalistener)

---

<a id="kafka-receiving-messages-class-level-kafkalistener"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/class-level-kafkalistener.html -->

<!-- page_index: 19 -->

# @KafkaListener on a Class

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-class-level-kafkalistener--page-title"></a>
<a id="kafka-receiving-messages-class-level-kafkalistener--kafkalistener-on-a-class"></a>

# `@KafkaListener` on a Class

When you use `@KafkaListener` at the class-level, you must specify `@KafkaHandler` at the method level.
If no `@KafkaHandler` on any methods of this class or its sub-classes, the framework will reject such a configuration.
The `@KafkaHandler` annotation is required for explicit and concise purpose of the method.
Otherwise it is hard to make a decision about this or other method without extra restrictions.

When messages are delivered, the converted message payload type is used to determine which method to call.
The following example shows how to do so:

```java
@KafkaListener(id = "multi", topics = "myTopic") static class MultiListenerBean {
@KafkaHandler public void listen(String foo) {...}
@KafkaHandler public void listen(Integer bar) {...}
@KafkaHandler(isDefault = true) public void listenDefault(Object object) {...}
}
```

Starting with version 2.1.3, you can designate a `@KafkaHandler` method as the default method that is invoked if there is no match on other methods.
At most, one method can be so designated.
When using `@KafkaHandler` methods, the payload must have already been converted to the domain object (so the match can be performed).
Use a custom deserializer, the `JacksonJsonDeserializer`, or the `JacksonJsonMessageConverter` with its `TypePrecedence` set to `TYPE_ID`.
See [Serialization, Deserialization, and Message Conversion](#kafka-serdes) for more information.

> [!IMPORTANT]
> Due to some limitations in the way Spring resolves method arguments, a default `@KafkaHandler` cannot receive discrete headers; it must use the `ConsumerRecordMetadata` as discussed in [Consumer Record Metadata](#kafka-receiving-messages-listener-annotation--consumer-record-metadata).

For example:

```java
@KafkaHandler(isDefault = true)
public void listenDefault(Object object, @Header(KafkaHeaders.RECEIVED_TOPIC) String topic) {
    ...
}
```

This won’t work if the object is a `String`; the `topic` parameter will also get a reference to `object`.

If you need metadata about the record in a default method, use this:

```java
@KafkaHandler(isDefault = true)
void listen(Object in, @Header(KafkaHeaders.RECORD_METADATA) ConsumerRecordMetadata meta) {
    String topic = meta.topic();
    ...
}
```

Also, this won’t work as well.
The `topic` is resolved to the `payload`.

```java
@KafkaHandler(isDefault = true)
public void listenDefault(String payload, @Header(KafkaHeaders.RECEIVED_TOPIC) String topic) {
    // payload.equals(topic) is True.
    ...
}
```

If there are use cases in which discrete custom headers are required in a default method, use this:

```java
@KafkaHandler(isDefault = true)
void listenDefault(String payload, @Headers Map<String, Object> headers) {
    Object myValue = headers.get("MyCustomHeader");
    ...
}
```

[`@KafkaListener` as a Meta Annotation](#kafka-receiving-messages-listener-meta)
[`@KafkaListener` Attribute Modification](#kafka-receiving-messages-kafkalistener-attrs)

---

<a id="kafka-receiving-messages-kafkalistener-attrs"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/kafkalistener-attrs.html -->

<!-- page_index: 20 -->

# @KafkaListener Attribute Modification

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-kafkalistener-attrs--page-title"></a>
<a id="kafka-receiving-messages-kafkalistener-attrs--kafkalistener-attribute-modification"></a>

# `@KafkaListener` Attribute Modification

Starting with version 2.7.2, you can now programmatically modify annotation attributes before the container is created.
To do so, add one or more `KafkaListenerAnnotationBeanPostProcessor.AnnotationEnhancer` to the application context.
`AnnotationEnhancer` is a `BiFunction<Map<String, Object>, AnnotatedElement, Map<String, Object>` and must return a map of attributes.
The attribute values can contain SpEL and/or property placeholders; the enhancer is called before any resolution is performed.
If more than one enhancer is present, and they implement `Ordered`, they will be invoked in order.

> [!IMPORTANT]
> `AnnotationEnhancer` bean definitions must be declared `static` because they are required very early in the application context’s lifecycle.

An example follows:

```java
@Bean
public static AnnotationEnhancer groupIdEnhancer() {
    return (attrs, element) -> {
        attrs.put("groupId", attrs.get("id") + "." + (element instanceof Class
                ? ((Class<?>) element).getSimpleName()
                : ((Method) element).getDeclaringClass().getSimpleName()
                        +  "." + ((Method) element).getName()));
        return attrs;
    };
}
```

[`@KafkaListener` on a Class](#kafka-receiving-messages-class-level-kafkalistener)
[`@KafkaListener` Lifecycle Management](#kafka-receiving-messages-kafkalistener-lifecycle)

---

<a id="kafka-receiving-messages-kafkalistener-lifecycle"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/kafkalistener-lifecycle.html -->

<!-- page_index: 21 -->

# @KafkaListener Lifecycle Management

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-kafkalistener-lifecycle--page-title"></a>
<a id="kafka-receiving-messages-kafkalistener-lifecycle--kafkalistener-lifecycle-management"></a>

# `@KafkaListener` Lifecycle Management

The listener containers created for `@KafkaListener` annotations are not beans in the application context.
Instead, they are registered with an infrastructure bean of type `KafkaListenerEndpointRegistry`.
This bean is automatically declared by the framework and manages the containers' lifecycles; it will auto-start any containers that have `autoStartup` set to `true`.
All containers created by all container factories must be in the same `phase`.
See [Listener Container Auto Startup](#kafka-receiving-messages-message-listener-container--container-auto-startup) for more information.
You can manage the lifecycle programmatically by using the registry.
Starting or stopping the registry will start or stop all the registered containers.
Alternatively, you can get a reference to an individual container by using its `id` attribute.
You can set `autoStartup` on the annotation, which overrides the default setting configured into the container factory.
You can get a reference to the bean from the application context, such as auto-wiring, to manage its registered containers.
The following examples show how to do so:

```java
@KafkaListener(id = "myContainer", topics = "myTopic", autoStartup = "false")
public void listen(...) { ... }
```

```java
@Autowired private KafkaListenerEndpointRegistry registry;
...
this.registry.getListenerContainer("myContainer").start();
...
```

The registry only maintains the life cycle of containers it manages; containers declared as beans are not managed by the registry and can be obtained from the application context.
A collection of managed containers can be obtained by calling the registry’s `getListenerContainers()` method.
Version 2.2.5 added a convenience method `getAllListenerContainers()`, which returns a collection of all containers, including those managed by the registry and those declared as beans.
The collection returned will include any prototype beans that have been initialized, but it will not initialize any lazy bean declarations.

> [!IMPORTANT]
> Endpoints registered after the application context has been refreshed will start immediately, regardless of their `autoStartup` property, to comply with the `SmartLifecycle` contract, where `autoStartup` is only considered during application context initialization.
> An example of late registration is a bean with a `@KafkaListener` in prototype scope where an instance is created after the context is initialized.
> Starting with version 2.8.7, you can set the registry’s `alwaysStartAfterRefresh` property to `false` and then the container’s `autoStartup` property will define whether or not the container is started.

<a id="kafka-receiving-messages-kafkalistener-lifecycle--retrieving-message-listener-containers"></a>
<a id="kafka-receiving-messages-kafkalistener-lifecycle--retrieving-messagelistenercontainers-from-kafkalistenerendpointregistry"></a>

## Retrieving MessageListenerContainers from KafkaListenerEndpointRegistry

The `KafkaListenerEndpointRegistry` provides methods for retrieving `MessageListenerContainer` instances to accommodate a range of management scenarios:

**All Containers**: For operations that cover all listener containers, use `getListenerContainers()` to retrieve a comprehensive collection.

```java
Collection<MessageListenerContainer> allContainers = registry.getListenerContainers();
```

**Specific Container by ID**: To manage an individual container, `getListenerContainer(String id)` enables retrieval by its id.

```java
MessageListenerContainer specificContainer = registry.getListenerContainer("myContainerId");
```

**Dynamic Container Filtering**: Introduced in version 3.2, two overloaded `getListenerContainersMatching` methods enable refined selection of containers.
One method takes a `Predicate<String>` for ID-based filtering as a parameter, while the other takes a `BiPredicate<String, MessageListenerContainer>`
for more advanced criteria that may include container properties or state as a parameter.

```java
// Prefix matching (Predicate<String>)
Collection<MessageListenerContainer> filteredContainers =
    registry.getListenerContainersMatching(id -> id.startsWith("productListener-retry-"));

// Regex matching (Predicate<String>)
Collection<MessageListenerContainer> regexFilteredContainers =
    registry.getListenerContainersMatching(myPattern::matches);

// Pre-built Set of IDs (Predicate<String>)
Collection<MessageListenerContainer> setFilteredContainers =
    registry.getListenerContainersMatching(myIdSet::contains);

// Advanced Filtering: ID prefix and running state (BiPredicate<String, MessageListenerContainer>)
Collection<MessageListenerContainer> advancedFilteredContainers =
    registry.getListenerContainersMatching(
        (id, container) -> id.startsWith("specificPrefix-") && container.isRunning()
    );
```

Utilize these methods to efficiently manage and query `MessageListenerContainer` instances within your application.

[`@KafkaListener` Attribute Modification](#kafka-receiving-messages-kafkalistener-attrs)
[`@KafkaListener` `@Payload` Validation](#kafka-receiving-messages-validation)

---

<a id="kafka-receiving-messages-validation"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/validation.html -->

<!-- page_index: 22 -->

# @KafkaListener @Payload Validation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-validation--page-title"></a>
<a id="kafka-receiving-messages-validation--kafkalistener-payload-validation"></a>

# `@KafkaListener` `@Payload` Validation

Starting with version 2.2, it is now easier to add a `Validator` to validate `@KafkaListener` `@Payload` arguments.
Previously, you had to configure a custom `DefaultMessageHandlerMethodFactory` and add it to the registrar.
Now, you can add the validator to the registrar itself.
The following code shows how to do so:

```java
@Configuration @EnableKafka public class Config implements KafkaListenerConfigurer {
...
@Override public void configureKafkaListeners(KafkaListenerEndpointRegistrar registrar) {registrar.setValidator(new MyValidator());}
}
```

> [!NOTE]
> When you use Spring Boot with the validation starter, a `LocalValidatorFactoryBean` is auto-configured, as the following example shows:

```java
@Configuration @EnableKafka public class Config implements KafkaListenerConfigurer {
@Autowired private LocalValidatorFactoryBean validator; ...
@Override public void configureKafkaListeners(KafkaListenerEndpointRegistrar registrar) {registrar.setValidator(this.validator);}}
```

The following examples show how to validate:

```java
public static class ValidatedClass {
@Max(10) private int bar;
public int getBar() {return this.bar;}
public void setBar(int bar) {this.bar = bar;}
}
```

```java
@KafkaListener(id="validated", topics = "annotated35", errorHandler = "validationErrorHandler",containerFactory = "kafkaJsonListenerContainerFactory") public void validatedListener(@Payload @Valid ValidatedClass val) {...}
@Bean public KafkaListenerErrorHandler validationErrorHandler() {return (m, e) -> {...};}
```

Starting with version 2.5.11, validation now works on payloads for `@KafkaHandler` methods in a class-level listener.
See [`@KafkaListener` on a Class](#kafka-receiving-messages-class-level-kafkalistener).

Starting with version 3.1, you can perform validation in an `ErrorHandlingDeserializer` instead.
See [Using `ErrorHandlingDeserializer`](#kafka-serdes--error-handling-deserializer) for more information.

[`@KafkaListener` Lifecycle Management](#kafka-receiving-messages-kafkalistener-lifecycle)
[Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners)

---

<a id="kafka-receiving-messages-rebalance-listeners"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/rebalance-listeners.html -->

<!-- page_index: 23 -->

# Rebalancing Listeners

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-rebalance-listeners--page-title"></a>
<a id="kafka-receiving-messages-rebalance-listeners--rebalancing-listeners"></a>

# Rebalancing Listeners

`ContainerProperties` has a property called `consumerRebalanceListener`, which takes an implementation of the Kafka client’s `ConsumerRebalanceListener` interface.
If this property is not provided, the container configures a logging listener that logs rebalance events at the `INFO` level.
The framework also adds a sub-interface `ConsumerAwareRebalanceListener`.
The following listing shows the `ConsumerAwareRebalanceListener` interface definition:

```java
public interface ConsumerAwareRebalanceListener extends ConsumerRebalanceListener {

    void onPartitionsRevokedBeforeCommit(Consumer<?, ?> consumer, Collection<TopicPartition> partitions);

    void onPartitionsRevokedAfterCommit(Consumer<?, ?> consumer, Collection<TopicPartition> partitions);

    void onPartitionsAssigned(Consumer<?, ?> consumer, Collection<TopicPartition> partitions);

    void onPartitionsLost(Consumer<?, ?> consumer, Collection<TopicPartition> partitions);

}
```

Notice that there are two callbacks when partitions are revoked.
The first is called immediately.
The second is called after any pending offsets are committed.
This is useful if you wish to maintain offsets in some external repository, as the following example shows:

```java
containerProperties.setConsumerRebalanceListener(new ConsumerAwareRebalanceListener() {
@Override public void onPartitionsRevokedBeforeCommit(Consumer<?, ?> consumer, Collection<TopicPartition> partitions) {// acknowledge any pending Acknowledgments (if using manual acks)}
@Override public void onPartitionsRevokedAfterCommit(Consumer<?, ?> consumer, Collection<TopicPartition> partitions) {// ...store(consumer.position(partition)); // ...}
@Override public void onPartitionsAssigned(Collection<TopicPartition> partitions) {// ...consumer.seek(partition, offsetTracker.getOffset() + 1); // ...} });
```

> [!IMPORTANT]
> Starting with version 2.4, a new method `onPartitionsLost()` has been added (similar to a method with the same name in `ConsumerRebalanceLister`).
> The default implementation on `ConsumerRebalanceLister` simply calls `onPartitionsRevoked`.
> The default implementation on `ConsumerAwareRebalanceListener` does nothing.
> When supplying the listener container with a custom listener (of either type), it is important that your implementation does not call `onPartitionsRevoked` from `onPartitionsLost`.
> If you implement `ConsumerRebalanceListener` you should override the default method.
> This is because the listener container will call its own `onPartitionsRevoked` from its implementation of `onPartitionsLost` after calling the method on your implementation.
> If you implementation delegates to the default behavior, `onPartitionsRevoked` will be called twice each time the `Consumer` calls that method on the container’s listener.

<a id="kafka-receiving-messages-rebalance-listeners--new-rebalance-protocol"></a>
<a id="kafka-receiving-messages-rebalance-listeners--kafka-4.0-consumer-rebalance-protocol"></a>

## Kafka 4.0 Consumer Rebalance Protocol

Spring for Apache Kafka 4.0 supports Apache [Kafka 4.0’s new consumer rebalance protocol](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol) (KIP-848), which enhances performance with server-driven, incremental partition assignments.
This reduces rebalancing downtime for consumer groups.

To enable the new protocol, configure the `group.protocol` property:

```properties
spring.kafka.consumer.properties.group.protocol=consumer
```

Keep in mind that, the above property is a Spring Boot property.
If you are not using Spring Boot, you may want to set it manually as shown below.

Alternatively, set it programmatically:

```java
Map<String, Object> props = new HashMap<>();
props.put("group.protocol", "consumer");
ConsumerFactory<String, String> factory = new DefaultKafkaConsumerFactory<>(props);
```

The new protocol works seamlessly with `ConsumerAwareRebalanceListener`.
Due to incremental rebalancing, `onPartitionsAssigned` may be called multiple times with smaller partition sets, unlike the single callback typical of the legacy protocol.

The new protocol uses server-side partition assignments, ignoring client-side custom assignors set via `spring.kafka.consumer.partition-assignment-strategy`.
A warning is logged if a custom assignor is detected.
To use custom assignors, set `group.protocol=classic` (which is the default if you don’t specify a value for `group.protocol`).

[`@KafkaListener` `@Payload` Validation](#kafka-receiving-messages-validation)
[Enforcing Consumer Rebalance](#kafka-receiving-messages-enforced-rebalance)

---

<a id="kafka-receiving-messages-enforced-rebalance"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/enforced-rebalance.html -->

<!-- page_index: 24 -->

# Enforcing Consumer Rebalance

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-enforced-rebalance--page-title"></a>
<a id="kafka-receiving-messages-enforced-rebalance--enforcing-consumer-rebalance"></a>

# Enforcing Consumer Rebalance

Kafka clients now support an option to trigger an [enforced rebalance](https://cwiki.apache.org/confluence/display/KAFKA/KIP-568%3A+Explicit+rebalance+triggering+on+the+Consumer).
Starting with version `3.1.2`, Spring for Apache Kafka provides an option to invoke this API on the Kafka consumer via the message listener container.
When calling this API, it is simply alerting the Kafka consumer to trigger an enforced rebalance; the actual rebalance will only occur as part of the next `poll()` operation.
If there is already a rebalance in progress, calling an enforced rebalance is a NO-OP.
The caller must wait for the current rebalance to complete before invoking another one.
See the javadocs for `enforceRebalance` for more details.

The following code snippet shows the essence of enforcing a rebalance using the message listener container.

```java
@KafkaListener(id = "my.id", topics = "my-topic") void listen(ConsumerRecord<String, String> in) {System.out.println("From KafkaListener: " + in);}
@Bean public ApplicationRunner runner(KafkaTemplate<String, Object> template, KafkaListenerEndpointRegistry registry) {return args -> {final MessageListenerContainer listenerContainer = registry.getListenerContainer("my.id"); System.out.println("Enforcing a rebalance"); Thread.sleep(5_000); listenerContainer.enforceRebalance(); Thread.sleep(5_000); };}
```

As the code above shows, the application uses the `KafkaListenerEndpointRegistry` to gain access to the message listener container and then calling the `enforceRebalance` API on it.
When calling the `enforceRebalance` on the listener container, it delegates the call to the underlying Kafka consumer.
The Kafka consumer will trigger a rebalance as part of the next `poll()` operation.

[Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners)
[Forwarding Listener Results using `@SendTo`](#kafka-receiving-messages-annotation-send-to)

---

<a id="kafka-receiving-messages-annotation-send-to"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/annotation-send-to.html -->

<!-- page_index: 25 -->

# Forwarding Listener Results using @SendTo

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-annotation-send-to--page-title"></a>
<a id="kafka-receiving-messages-annotation-send-to--forwarding-listener-results-using-sendto"></a>

# Forwarding Listener Results using `@SendTo`

Starting with version 2.0, if you also annotate a `@KafkaListener` with a `@SendTo` annotation and the method invocation returns a result, the result is forwarded to the topic specified by the `@SendTo`.

The `@SendTo` value can have several forms:

- `@SendTo("someTopic")` routes to the literal topic.
- `@SendTo("#{someExpression}")` routes to the topic determined by evaluating the expression once during application context initialization.
- `@SendTo("!{someExpression}")` routes to the topic determined by evaluating the expression at runtime.
  The `#root` object for the evaluation has three properties:

  - `request`: The inbound `ConsumerRecord` (or `ConsumerRecords` object for a batch listener).
  - `source`: The `org.springframework.messaging.Message<?>` converted from the `request`.
  - `result`: The method return result.
- `@SendTo` (no properties): This is treated as `!{source.headers['kafka_replyTopic']}` (since version 2.1.3).

Starting with versions 2.1.11 and 2.2.1, property placeholders are resolved within `@SendTo` values.

The result of the expression evaluation must be a `String` that represents the topic name.
The following examples show the various ways to use `@SendTo`:

```java
@KafkaListener(topics = "annotated21") @SendTo("!{request.value()}") // runtime SpEL public String replyingListener(String in) {...}
@KafkaListener(topics = "${some.property:annotated22}") @SendTo("#{myBean.replyTopic}") // config time SpEL public Collection<String> replyingBatchListener(List<String> in) {...}
@KafkaListener(topics = "annotated23", errorHandler = "replyErrorHandler") @SendTo("annotated23reply") // static reply topic definition public String replyingListenerWithErrorHandler(String in) {...} ...@KafkaListener(topics = "annotated25") @SendTo("annotated25reply1") public class MultiListenerSendTo {
@KafkaHandler public String foo(String in) {...}
@KafkaHandler @SendTo("!{'annotated25reply2'}") public String bar(@Payload(required = false) KafkaNull nul,@Header(KafkaHeaders.RECEIVED_KEY) int key) {...}
}
```

> [!IMPORTANT]
> In order to support `@SendTo`, the listener container factory must be provided with a `KafkaTemplate` (in its `replyTemplate` property), which is used to send the reply.
> This should be a `KafkaTemplate` and not a `ReplyingKafkaTemplate` which is used on the client-side for request/reply processing.
> When using Spring Boot, it will auto-configure the template into the factory; when configuring your own factory, it must be set as shown in the examples below.

Starting with version 2.2, you can add a `ReplyHeadersConfigurer` to the listener container factory.
This is consulted to determine which headers you want to set in the reply message.
The following example shows how to add a `ReplyHeadersConfigurer`:

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<Integer, String> kafkaListenerContainerFactory() {
    ConcurrentKafkaListenerContainerFactory<Integer, String> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(cf());
    factory.setReplyTemplate(template());
    factory.setReplyHeadersConfigurer((k, v) -> k.equals("cat"));
    return factory;
}
```

You can also add more headers if you wish.
The following example shows how to do so:

```java
@Bean public ConcurrentKafkaListenerContainerFactory<Integer, String> kafkaListenerContainerFactory() {ConcurrentKafkaListenerContainerFactory<Integer, String> factory =new ConcurrentKafkaListenerContainerFactory<>(); factory.setConsumerFactory(cf()); factory.setReplyTemplate(template()); factory.setReplyHeadersConfigurer(new ReplyHeadersConfigurer() {
@Override public boolean shouldCopy(String headerName, Object headerValue) {return false;}
@Override public Map<String, Object> additionalHeaders() {return Collections.singletonMap("qux", "fiz");}
}); return factory;}
```

When you use `@SendTo`, you must configure the `ConcurrentKafkaListenerContainerFactory` with a `KafkaTemplate` in its `replyTemplate` property to perform the send.
Spring Boot will automatically wire in its auto-configured template (or any if a single instance is present).

> [!NOTE]
> Unless you use [request/reply semantics](#kafka-sending-messages--replying-template), only the simple `send(topic, value)` method is used, so you may wish to create a subclass to generate the partition or key.
> The following example shows how to do so:

```java
@Bean public KafkaTemplate<String, String> myReplyingTemplate() {return new KafkaTemplate<String, String>(producerFactory()) {
@Override public CompletableFuture<SendResult<String, String>> send(String topic, String data) {return super.send(topic, partitionForData(data), keyForData(data), data);}
...
};}
```

> [!IMPORTANT]
> If the listener method returns `Message<?>` or `Collection<Message<?>>`, the listener method is responsible for setting up the message headers for the reply.
> For example, when handling a request from a `ReplyingKafkaTemplate`, you might do the following:
>
> ```java
> @KafkaListener(id = "messageReturned", topics = "someTopic")
> public Message<?> listen(String in, @Header(KafkaHeaders.REPLY_TOPIC) byte[] replyTo,
>         @Header(KafkaHeaders.CORRELATION_ID) byte[] correlation) {
>     return MessageBuilder.withPayload(in.toUpperCase())
>             .setHeader(KafkaHeaders.TOPIC, replyTo)
>             .setHeader(KafkaHeaders.KEY, 42)
>             .setHeader(KafkaHeaders.CORRELATION_ID, correlation)
>             .setHeader("someOtherHeader", "someValue")
>             .build();
> }
> ```

When using request/reply semantics, the target partition can be requested by the sender.

> [!NOTE]
> You can annotate a `@KafkaListener` method with `@SendTo` even if no result is returned.
> This is to allow the configuration of an `errorHandler` that can forward information about a failed message delivery to some topic.
> The following example shows how to do so:
>
> ```java
> @KafkaListener(id = "voidListenerWithReplyingErrorHandler", topics = "someTopic",errorHandler = "voidSendToErrorHandler") @SendTo("failures") public void voidListenerWithReplyingErrorHandler(String in) {throw new RuntimeException("fail");}
> @Bean public KafkaListenerErrorHandler voidSendToErrorHandler() {return (m, e) -> {return ... // some information about the failure and input data };}
> ```
>
> See [Handling Exceptions](#kafka-annotation-error-handling) for more information.

> [!NOTE]
> If a listener method returns an `Iterable`, by default a record for each element as the value is sent.
> Starting with version 2.3.5, set the `splitIterables` property on `@KafkaListener` to `false` and the entire result will be sent as the value of a single `ProducerRecord`.
> This requires a suitable serializer in the reply template’s producer configuration.
> However, if the reply is `Iterable<Message<?>>` the property is ignored and each message is sent separately.

[Enforcing Consumer Rebalance](#kafka-receiving-messages-enforced-rebalance)
[Filtering Messages](#kafka-receiving-messages-filtering)

---

<a id="kafka-receiving-messages-filtering"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/filtering.html -->

<!-- page_index: 26 -->

# Filtering Messages

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-filtering--page-title"></a>
<a id="kafka-receiving-messages-filtering--filtering-messages"></a>

# Filtering Messages

In certain scenarios, such as rebalancing, a message that has already been processed may be redelivered.
The framework cannot know whether such a message has been processed or not.
That is an application-level function.
This is known as the [Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) pattern and Spring Integration provides an [implementation](https://docs.spring.io/spring-integration/reference/handler-advice/idempotent-receiver.html) of it.

The Spring for Apache Kafka project also provides some assistance by means of the `FilteringMessageListenerAdapter` class, which can wrap your `MessageListener`.
This class takes an implementation of `RecordFilterStrategy` in which you implement the `filter` method to signal that a message is a duplicate and should be discarded.
This has an additional property called `ackDiscarded`, which indicates whether the adapter should acknowledge the discarded record.
It is `false` by default.

When you use `@KafkaListener`, set the `RecordFilterStrategy` (and optionally `ackDiscarded`) on the container factory so that the listener is wrapped in the appropriate filtering adapter.

In addition, a `FilteringBatchMessageListenerAdapter` is provided, for when you use a batch [message listener](#kafka-receiving-messages-message-listeners).

> [!IMPORTANT]
> The `FilteringBatchMessageListenerAdapter` is ignored if your `@KafkaListener` receives a `ConsumerRecords<?, ?>` instead of `List<ConsumerRecord<?, ?>>`, because `ConsumerRecords` is immutable.

Starting with version 2.8.4, you can override the listener container factory’s default `RecordFilterStrategy` by using the `filter` property on the listener annotations.

```java
@KafkaListener(id = "filtered", topics = "topic", filter = "differentFilter")
public void listen(Thing thing) {
    ...
}
```

Starting with version 3.3, Ignoring empty batches that result from filtering by `RecordFilterStrategy` is supported.
When implementing `RecordFilterStrategy`, it can be configured through `ignoreEmptyBatch()`.
The default setting is `false`, indicating `KafkaListener` will be invoked even if all `ConsumerRecord`s are filtered out.

If `true` is returned, the `KafkaListener` will not be invoked when all `ConsumerRecord` are filtered out.
However, commit to broker, will still be executed.

If `false` is returned, the `KafkaListener` will be invoked when all `ConsumerRecord` are filtered out.

Here are some examples.

```java
public class IgnoreEmptyBatchRecordFilterStrategy implements RecordFilterStrategy {...@Override public List<ConsumerRecord<String, String>> filterBatch(List<ConsumerRecord<String, String>> consumerRecords) {return List.of();}
@Override public boolean ignoreEmptyBatch() {return true;}}
// NOTE: ignoreEmptyBatchRecordFilterStrategy is bean name of IgnoreEmptyBatchRecordFilterStrategy instance.@KafkaListener(id = "filtered", topics = "topic", filter = "ignoreEmptyBatchRecordFilterStrategy") public void listen(List<Thing> things) {...}
```

In this case, `IgnoreEmptyBatchRecordFilterStrategy` always returns empty list and return `true` as result of `ignoreEmptyBatch()`.
Thus `KafkaListener#listen(…)` never will be invoked at all.

```java
public class NotIgnoreEmptyBatchRecordFilterStrategy implements RecordFilterStrategy {...@Override public List<ConsumerRecord<String, String>> filterBatch(List<ConsumerRecord<String, String>> consumerRecords) {return List.of();}
@Override public boolean ignoreEmptyBatch() {return false;}}
// NOTE: notIgnoreEmptyBatchRecordFilterStrategy is bean name of NotIgnoreEmptyBatchRecordFilterStrategy instance.@KafkaListener(id = "filtered", topics = "topic", filter = "notIgnoreEmptyBatchRecordFilterStrategy") public void listen(List<Thing> things) {...}
```

However, in this case, `NotIgnoreEmptyBatchRecordFilterStrategy` always returns empty list and return `false` as result of `ignoreEmptyBatch()`.
Thus `KafkaListener#listen(…)` always will be invoked.

[Forwarding Listener Results using `@SendTo`](#kafka-receiving-messages-annotation-send-to)
[Retrying Deliveries](#kafka-receiving-messages-retrying-deliveries)

---

<a id="kafka-receiving-messages-retrying-deliveries"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/retrying-deliveries.html -->

<!-- page_index: 27 -->

# Retrying Deliveries

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-retrying-deliveries--page-title"></a>
<a id="kafka-receiving-messages-retrying-deliveries--retrying-deliveries"></a>

# Retrying Deliveries

See the `DefaultErrorHandler` in [Handling Exceptions](#kafka-annotation-error-handling).

[Filtering Messages](#kafka-receiving-messages-filtering)
[Starting `@KafkaListener`s in Sequence](#kafka-receiving-messages-sequencing)

---

<a id="kafka-receiving-messages-sequencing"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/sequencing.html -->

<!-- page_index: 28 -->

# Starting @KafkaListener s in Sequence

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-sequencing--page-title"></a>
<a id="kafka-receiving-messages-sequencing--starting-kafkalistener-s-in-sequence"></a>

# Starting `@KafkaListener`s in Sequence

A common use case is to start a listener after another listener has consumed all the records in a topic.
For example, you may want to load the contents of one or more compacted topics into memory before processing records from other topics.
Starting with version 2.7.3, a new component `ContainerGroupSequencer` has been introduced.
It uses the `@KafkaListener`'s `containerGroup` property to group containers together and start the containers in the next group, when all the containers in the current group have gone idle.

It is best illustrated with an example.

```java
@KafkaListener(id = "listen1", topics = "topic1", containerGroup = "g1", concurrency = "2") public void listen1(String in) {}
@KafkaListener(id = "listen2", topics = "topic2", containerGroup = "g1", concurrency = "2") public void listen2(String in) {}
@KafkaListener(id = "listen3", topics = "topic3", containerGroup = "g2", concurrency = "2") public void listen3(String in) {}
@KafkaListener(id = "listen4", topics = "topic4", containerGroup = "g2", concurrency = "2") public void listen4(String in) {}
@Bean ContainerGroupSequencer sequencer(KafkaListenerEndpointRegistry registry) {return new ContainerGroupSequencer(registry, 5000, "g1", "g2");}
```

Here, we have 4 listeners in two groups, `g1` and `g2`.

During application context initialization, the sequencer sets the `autoStartup` property of all the containers in the provided groups to `false`.
It also sets the `idleEventInterval` for any containers (that do not already have one set) to the supplied value (5000ms in this case).
Then, when the sequencer is started by the application context, the containers in the first group are started.
As `ListenerContainerIdleEvent`s are received, each individual child container in each container is stopped.
When all child containers in a `ConcurrentMessageListenerContainer` are stopped, the parent container is stopped.
When all containers in a group have been stopped, the containers in the next group are started.
There is no limit to the number of groups or containers in a group.

By default, the containers in the final group (`g2` above) are not stopped when they go idle.
To modify that behavior, set `stopLastGroupWhenIdle` to `true` on the sequencer.

As an aside, previously containers in each group were added to a bean of type `Collection<MessageListenerContainer>` with the bean name being the `containerGroup`.
These collections are now deprecated in favor of beans of type `ContainerGroup` with a bean name that is the group name, suffixed with `.group`; in the example above, there would be 2 beans `g1.group` and `g2.group`.
The `Collection` beans will be removed in a future release.

[Retrying Deliveries](#kafka-receiving-messages-retrying-deliveries)
[Using `KafkaTemplate` to Receive](#kafka-receiving-messages-template-receive)

---

<a id="kafka-receiving-messages-template-receive"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/template-receive.html -->

<!-- page_index: 29 -->

# Using KafkaTemplate to Receive

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-receiving-messages-template-receive--page-title"></a>
<a id="kafka-receiving-messages-template-receive--using-kafkatemplate-to-receive"></a>

# Using `KafkaTemplate` to Receive

This section covers how to use `KafkaTemplate` to receive messages.

Starting with version 2.8, the template has four `receive()` methods:

```java
ConsumerRecord<K, V> receive(String topic, int partition, long offset);

ConsumerRecord<K, V> receive(String topic, int partition, long offset, Duration pollTimeout);

ConsumerRecords<K, V> receive(Collection<TopicPartitionOffset> requested);

ConsumerRecords<K, V> receive(Collection<TopicPartitionOffset> requested, Duration pollTimeout);
```

As you can see, you need to know the partition and offset of the record(s) you need to retrieve; a new `Consumer` is created (and closed) for each operation.

With the last two methods, each record is retrieved individually and the results assembled into a `ConsumerRecords` object.
When creating the `TopicPartitionOffset`s for the request, only positive, absolute offsets are supported.

[Starting `@KafkaListener`s in Sequence](#kafka-receiving-messages-sequencing)
[Listener Container Properties](#kafka-container-props)

---

<a id="kafka-container-props"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/container-props.html -->

<!-- page_index: 30 -->

# Listener Container Properties

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-container-props--page-title"></a>
<a id="kafka-container-props--listener-container-properties"></a>

# Listener Container Properties

| Property | Default | Description |
| --- | --- | --- |
| [`ackCount`](#kafka-container-props--ackcount) | 1 | The number of records before committing pending offsets when the `ackMode` is `COUNT` or `COUNT_TIME`. |
| [`adviceChain`](#kafka-container-props--advicechain) | `null` | A chain of `Advice` objects (e.g. `MethodInterceptor` around advice) wrapping the message listener, invoked in order. |
| [`ackMode`](#kafka-container-props--ackmode) | BATCH | Controls how often offsets are committed - see [Committing Offsets](#kafka-receiving-messages-message-listener-container--committing-offsets). |
| [`ackTime`](#kafka-container-props--acktime) | 5000 | The time in milliseconds after which pending offsets are committed when the `ackMode` is `TIME` or `COUNT_TIME`. |
| [`assignmentCommitOption`](#kafka-container-props--assignmentcommitoption) | LATEST\_ONLY \_NO\_TX | Whether or not to commit the initial position on assignment; by default, the initial offset will only be committed if the `ConsumerConfig.AUTO_OFFSET_RESET_CONFIG` is `latest` and it won’t run in a transaction even if there is a transaction manager present. See the JavaDocs for `ContainerProperties.AssignmentCommitOption` for more information about the available options. |
| [`asyncAcks`](#kafka-container-props--asyncacks) | `false` | Enable out-of-order commits (see [Manually Committing Offsets](#kafka-receiving-messages-ooo-commits)); the consumer is paused and commits are deferred until gaps are filled. |
| [`authExceptionRetryInterval`](#kafka-container-props--authexceptionretryinterval) | `null` | When not null, a `Duration` to sleep between polls when an `AuthenticationException` or `AuthorizationException` is thrown by the Kafka client. When null, such exceptions are considered fatal and the container will stop. |
| [`batchRecoverAfterRollback`](#kafka-container-props--batchrecoverafterrollback) | `false` | Set to `true` to enable batch recovery, See [After Rollback Processor](#kafka-annotation-error-handling--after-rollback). |
| [`clientId`](#kafka-container-props--clientid) | (empty string) | A prefix for the `client.id` consumer property. Overrides the consumer factory `client.id` property; in a concurrent container, `-n` is added as a suffix for each consumer instance. |
| [`checkDeserExWhenKeyNull`](#kafka-container-props--checkdeserexwhenkeynull) | false | Set to `true` to always check for a `DeserializationException` header when a `null` `key` is received. Useful when the consumer code cannot determine that an `ErrorHandlingDeserializer` has been configured, such as when using a delegating deserializer. |
| [`checkDeserExWhenValueNull`](#kafka-container-props--checkdeserexwhenvaluenull) | false | Set to `true` to always check for a `DeserializationException` header when a `null` `value` is received. Useful when the consumer code cannot determine that an `ErrorHandlingDeserializer` has been configured, such as when using a delegating deserializer. |
| [`commitCallback`](#kafka-container-props--commitcallback) | `null` | When present and `syncCommits` is `false` a callback invoked after the commit completes. |
| [`commitLogLevel`](#kafka-container-props--commitloglevel) | DEBUG | The logging level for logs pertaining to committing offsets. |
| [`consumerRebalanceListener`](#kafka-container-props--consumerrebalancelistener) | `null` | A rebalance listener; see [Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners). |
| [`commitRetries`](#kafka-container-props--commitretries) | 3 | Set the number of retries `RetriableCommitFailedException` when using `syncCommits` set to true. Default 3 (4-attempt total). |
| [`consumerStartTimeout`](#kafka-container-props--consumerstarttimeout) | 30s | The time to wait for the consumer to start before logging an error; this might happen if, say, you use a task executor with insufficient threads. |
| [`deliveryAttemptHeader`](#kafka-container-props--deliveryattemptheader) | `false` | See [Delivery Attempts Header](#kafka-annotation-error-handling--delivery-header). |
| [`eosMode`](#kafka-container-props--eosmode) | `V2` | Exactly Once Semantics mode; see [Exactly Once Semantics](#kafka-exactly-once). |
| [`fixTxOffsets`](#kafka-container-props--fixtxoffsets) | `false` | When consuming records produced by a transactional producer, and the consumer is positioned at the end of a partition, the lag can incorrectly be reported as greater than zero, due to the pseudo record used to indicate transaction commit/rollback and, possibly, the presence of rolled-back records. This does not functionally affect the consumer but some users have expressed concern that the "lag" is non-zero. Set this property to `true` and the container will correct such mis-reported offsets. The check is performed before the next poll to avoid adding significant complexity to the commit processing. At the time of writing, the lag will only be corrected if the consumer is configured with `isolation.level=read_committed` and `max.poll.records` is greater than 1. See [KAFKA-10683](https://issues.apache.org/jira/browse/KAFKA-10683) for more information. |
| [`groupId`](#kafka-container-props--groupid) | `null` | Overrides the consumer `group.id` property; automatically set by the `@KafkaListener` `id` or `groupId` property. |
| [`idleBeforeDataMultiplier`](#kafka-container-props--idlebeforedatamultiplier) | 5.0 | Multiplier for `idleEventInterval` that is applied before any records are received. After a record is received, the multiplier is no longer applied. Available since version 2.8. |
| [`idleBetweenPolls`](#kafka-container-props--idlebetweenpolls) | 0 | Used to slow down deliveries by sleeping the thread between polls. The time to process a batch of records plus this value must be less than the `max.poll.interval.ms` consumer property. |
| [`idleEventInterval`](#kafka-container-props--idleeventinterval) | `null` | When set, enables publication of `ListenerContainerIdleEvent`s, see [Application Events](#kafka-events) and [Detecting Idle and Non-Responsive Consumers](#kafka-events--idle-containers). Also see `idleBeforeDataMultiplier`. |
| [`idlePartitionEventInterval`](#kafka-container-props--idlepartitioneventinterval) | `null` | When set, enables publication of `ListenerContainerIdlePartitionEvent`s, see [Application Events](#kafka-events) and [Detecting Idle and Non-Responsive Consumers](#kafka-events--idle-containers). |
| [`kafkaConsumerProperties`](#kafka-container-props--kafkaconsumerproperties) | None | Used to override any arbitrary consumer properties configured on the consumer factory. |
| [`kafkaAwareTransactionManager`](#kafka-container-props--kafkaawaretransactionmanager) | `null` | See [Transactions](#kafka-transactions). |
| [`listenerTaskExecutor`](#kafka-container-props--listenertaskexecutor) | `SimpleAsyncTaskExecutor` | A task executor to run the consumer threads. The default executor creates threads named `<name>-C-n`; with the `KafkaMessageListenerContainer`, the name is the bean name; with the `ConcurrentMessageListenerContainer` the name is the bean name suffixed with `-m` where `m` is incremented for each child container. See [Container Thread Naming](#kafka-receiving-messages-container-thread-naming--container-thread-naming). |
| [`logContainerConfig`](#kafka-container-props--logcontainerconfig) | `false` | Set to `true` to log at INFO level all container properties. |
| [`messageListener`](#kafka-container-props--messagelistener) | `null` | The message listener that processes records consumed from Kafka topics. |
| [`micrometerEnabled`](#kafka-container-props--micrometerenabled) | `true` | Whether or not to maintain Micrometer timers for the consumer threads. |
| [`micrometerTags`](#kafka-container-props--micrometertags) | empty | A map of static tags to be added to micrometer metrics. |
| [`micrometerTagsProvider`](#kafka-container-props--micrometertagsprovider) | `null` | A function that provides dynamic tags, based on the consumer record. |
| [`missingTopicsFatal`](#kafka-container-props--missingtopicsfatal) | `false` | When true prevents the container from starting if the configured topic(s) are not present on the broker. |
| [`monitorInterval`](#kafka-container-props--monitorinterval) | 30s | How often to check the state of the consumer threads for `NonResponsiveConsumerEvent`s. See `noPollThreshold` and `pollTimeout`. |
| [`noPollThreshold`](#kafka-container-props--nopollthreshold) | 3.0 | Multiplied by `pollTimeOut` to determine whether to publish a `NonResponsiveConsumerEvent`. See `monitorInterval`. |
| [`observationConvention`](#kafka-container-props--observationconvention) | `null` | When set, add dynamic tags to the timers and traces, based on information in the consumer records. |
| [`observationEnabled`](#kafka-container-props--observationenabled) | `false` | Set to `true` to enable observation via Micrometer. |
| [`offsetAndMetadataProvider`](#kafka-container-props--offsetandmetadataprovider) | `null` | A provider for `OffsetAndMetadata`; by default, the provider creates an offset and metadata with empty metadata. The provider gives a way to customize the metadata. |
| [`onlyLogRecordMetadata`](#kafka-container-props--onlylogrecordmetadata) | `false` | Set to `false` to log the complete consumer record (in error, debug logs etc.) instead of just `topic-partition@offset`. |
| [`pauseImmediate`](#kafka-container-props--pauseimmediate) | `false` | When the container is paused, stop processing after the current record instead of after processing all the records from the previous poll; the remaining records are retained in memory and will be passed to the listener when the container is resumed. |
| [`pollTimeout`](#kafka-container-props--polltimeout) | 5000 | The timeout passed into `Consumer.poll()` in milliseconds. |
| [`pollTimeoutWhilePaused`](#kafka-container-props--polltimeoutwhilepaused) | 100 | The timeout passed into `Consumer.poll()` (in milliseconds) when the container is in a paused state. |
| [`restartAfterAuthExceptions`](#kafka-container-props--restartafterauthexceptions) | false | True to restart the container if it is stopped due to authorization/authentication exceptions. |
| [`scheduler`](#kafka-container-props--scheduler) | `ThreadPoolTaskScheduler` | A scheduler on which to run the consumer monitor task. |
| [`shutdownTimeout`](#kafka-container-props--shutdowntimeout) | 10000 | The maximum time in ms to block the `stop()` method until all consumers stop and before publishing the container stopped event. |
| [`stopContainerWhenFenced`](#kafka-container-props--stopcontainerwhenfenced) | `false` | Stop the listener container if a `ProducerFencedException` is thrown. See [After-rollback Processor](#kafka-annotation-error-handling--after-rollback) for more information. |
| [`stopImmediate`](#kafka-container-props--stopimmediate) | `false` | When the container is stopped, stop processing after the current record instead of after processing all the records from the previous poll. |
| [`subBatchPerPartition`](#kafka-container-props--subbatchperpartition) | See desc. | When using a batch listener, if this is `true`, the listener is called with the results of the poll split into sub batches, one per partition. Default `false`. |
| [`syncCommitTimeout`](#kafka-container-props--synccommittimeout) | `null` | The timeout to use when `syncCommits` is `true`. When not set, the container will attempt to determine the `default.api.timeout.ms` consumer property and use that; otherwise it will use 60 seconds. |
| [`syncCommits`](#kafka-container-props--synccommits) | `true` | Whether to use sync or async commits for offsets; see `commitCallback`. |
| [`topics` `topicPattern` `topicPartitions`](#kafka-container-props--topics) | n/a | The configured topics, topic pattern or explicitly assigned topics/partitions. Mutually exclusive; at least one must be provided; enforced by `ContainerProperties` constructors. |
| [`transactionManager`](#kafka-container-props--transactionmanager) | `null` | Deprecated since 3.2, see [[kafkaAwareTransactionManager]](#kafka-container-props--kafkaawaretransactionmanager), [Other transaction managers](#kafka-transactions--transaction-synchronization). |

| Property | Default | Description |
| --- | --- | --- |
| [`afterRollbackProcessor`](#kafka-container-props--afterrollbackprocessor) | `DefaultAfterRollbackProcessor` | An `AfterRollbackProcessor` to invoke after a transaction is rolled back. |
| [`applicationEventPublisher`](#kafka-container-props--applicationeventpublisher) | application context | The event publisher. |
| [`batchErrorHandler`](#kafka-container-props--batcherrorhandler) | See desc. | Deprecated - see `commonErrorHandler`. |
| > [!NOTE] > [`batchInterceptor`](#kafka-container-props--batchinterceptor) | `null` | Set a `BatchInterceptor` to call before invoking the batch listener; does not apply to record listeners. Also see `interceptBeforeTx`. |
| [`beanName`](#kafka-container-props--beanname) | bean name | The bean name of the container; suffixed with `-n` for child containers. |
| [`commonErrorHandler`](#kafka-container-props--commonerrorhandler) | See desc. | `DefaultErrorHandler` or `null` when a `transactionManager` is provided when a `DefaultAfterRollbackProcessor` is used. See [Container Error Handlers](#kafka-annotation-error-handling--error-handlers). |
| [`containerProperties`](#kafka-container-props--containerproperties) | `ContainerProperties` | The container properties instance. |
| [`groupId`](#kafka-container-props--groupid2) | See desc. | The `containerProperties.groupId`, if present, otherwise the `group.id` property from the consumer factory. |
| [`interceptBeforeTx`](#kafka-container-props--interceptbeforetx) | `true` | Determines whether the `recordInterceptor` is called before or after a transaction starts. |
| [`listenerId`](#kafka-container-props--listenerid) | See desc. | The bean name for user-configured containers or the `id` attribute of `@KafkaListener`s. |
| [`listenerInfo`](#kafka-container-props--listenerinfo) | null | A value to populate in the `KafkaHeaders.LISTENER_INFO` header. With `@KafkaListener`, this value is obtained from the `info` attribute. This header can be used in various places, such as a `RecordInterceptor`, `RecordFilterStrategy` and in the listener code itself. |
| [`pauseRequested`](#kafka-container-props--pauserequested) | (read only) | True if a consumer pause has been requested. |
| [`recordInterceptor`](#kafka-container-props--recordinterceptor) | `null` | Set a `RecordInterceptor` to call before invoking the record listener; does not apply to batch listeners. Also see `interceptBeforeTx`. |
| [`topicCheckTimeout`](#kafka-container-props--topicchecktimeout) | 30s | When the `missingTopicsFatal` container property is `true`, how long to wait, in seconds, for the `describeTopics` operation to complete. |

| Property | Default | Description |
| --- | --- | --- |
| [`assignedPartitions`](#kafka-container-props--assignedpartitions) | (read only) | The partitions currently assigned to this container (explicitly or not). |
| [`clientIdSuffix`](#kafka-container-props--clientidsuffix) | `null` | Used by the concurrent container to give each child container’s consumer a unique `client.id`. |
| [`containerPaused`](#kafka-container-props--containerpaused) | n/a | True if pause has been requested and the consumer has actually paused. |

| Property | Default | Description |
| --- | --- | --- |
| [`alwaysClientIdSuffix`](#kafka-container-props--alwaysclientidsuffix) | `true` | Set to false to suppress adding a suffix to the `client.id` consumer property, when the `concurrency` is only 1. |
| [`assignedPartitions`](#kafka-container-props--assignedpartitions2) | (read only) | The aggregate of partitions currently assigned to this container’s child `KafkaMessageListenerContainer`s (explicitly or not). |
| [`concurrency`](#kafka-container-props--concurrency) | 1 | The number of child `KafkaMessageListenerContainer`s to manage. |
| [`containerPaused`](#kafka-container-props--containerpaused2) | n/a | True if pause has been requested and all child containers' consumer has actually paused. |
| [`containers`](#kafka-container-props--containers) | n/a | A reference to all child `KafkaMessageListenerContainer`s. |

[Using `KafkaTemplate` to Receive](#kafka-receiving-messages-template-receive)
[Dynamically Creating Containers](#kafka-dynamic-containers)

---

<a id="kafka-dynamic-containers"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/dynamic-containers.html -->

<!-- page_index: 31 -->

# Dynamically Creating Containers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-dynamic-containers--page-title"></a>
<a id="kafka-dynamic-containers--dynamically-creating-containers"></a>

# Dynamically Creating Containers

There are several techniques that can be used to create listener containers at runtime.
This section explores some of those techniques.

<a id="kafka-dynamic-containers--messagelistener-implementations"></a>

## MessageListener Implementations

If you implement your own listener directly, you can simply use the container factory to create a raw container for that listener:

User Listener

- Java
- Kotlin

```java
public class MyListener implements MessageListener<String, String> {

    @Override
    public void onMessage(ConsumerRecord<String, String> data) {
        // ...
    }

}

private ConcurrentMessageListenerContainer<String, String> createContainer(
        ConcurrentKafkaListenerContainerFactory<String, String> factory, String topic, String group) {

    ConcurrentMessageListenerContainer<String, String> container = factory.createContainer(topic);
    container.getContainerProperties().setMessageListener(new MyListener());
    container.getContainerProperties().setGroupId(group);
    container.setBeanName(group);
    container.start();
    return container;
}
```

```kotlin
class MyListener : MessageListener<String, String> {

    override fun onMessage(data: ConsumerRecord<String, String>) {

        // ...
    }

}

private fun createContainer(
    factory: ConcurrentKafkaListenerContainerFactory<String, String>, topic: String, group: String
): ConcurrentMessageListenerContainer<String, String> {
    val container = factory.createContainer(topic)
    container.containerProperties.setMessageListener(MyListener())
    container.containerProperties.setGroupId(group)
    container.beanName = group
    container.start()
    return container
}
```

<a id="kafka-dynamic-containers--prototype-beans"></a>

## Prototype Beans

Containers for methods annotated with `@KafkaListener` can be created dynamically by declaring the bean as prototype:

Prototype

- Java
- Kotlin

```java
public class MyPojo {
private final String id;
private final String topic;
public MyPojo(String id, String topic) {this.id = id; this.topic = topic;}
public String getId() {return this.id;}
public String getTopic() {return this.topic;}
@KafkaListener(id = "#{__listener.id}", topics = "#{__listener.topic}") public void listen(String in) {System.out.println(in);}
}
@Bean @Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE) MyPojo pojo(String id, String topic) {return new MyPojo(id, topic);}
applicationContext.getBean(MyPojo.class, "one", "topic2"); applicationContext.getBean(MyPojo.class, "two", "topic3");
```

```kotlin
class MyPojo(val id: String, val topic: String) {
@KafkaListener(id = "#{__listener.id}", topics = ["#{__listener.topic}"]) fun listen(`in`: String?) {println(`in`)}
}
@Bean @Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE) fun pojo(id: String, topic: String): MyPojo {return MyPojo(id, topic)}
applicationContext.getBean(MyPojo::class.java, "one", "topic2") applicationContext.getBean(MyPojo::class.java, "two", "topic3")
```

> [!IMPORTANT]
> Listeners must have unique IDs.
> Starting with version 2.8.9, the `KafkaListenerEndpointRegistry` has a new method `unregisterListenerContainer(String id)` to allow you to re-use an id.
> Unregistering a container does not `stop()` the container, you must do that yourself.

[Listener Container Properties](#kafka-container-props)
[Application Events](#kafka-events)

---

<a id="kafka-events"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/events.html -->

<!-- page_index: 32 -->

# Application Events

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-events--page-title"></a>
<a id="kafka-events--application-events"></a>

# Application Events

The following Spring application events are published by listener containers and their consumers:

- `ConsumerStartingEvent`: published when a consumer thread is first started, before it starts polling.
- `ConsumerStartedEvent`: published when a consumer is about to start polling.
- `ConsumerFailedToStartEvent`: published if no `ConsumerStartingEvent` is published within the `consumerStartTimeout` container property.
  This event might signal that the configured task executor has insufficient threads to support the containers it is used in and their concurrency.
  An error message is also logged when this condition occurs.
- `ListenerContainerIdleEvent`: published when no messages have been received in `idleEventInterval` (if configured).
- `ListenerContainerNoLongerIdleEvent`: published when a record is consumed after previously publishing a `ListenerContainerIdleEvent`.
- `ListenerContainerPartitionIdleEvent`: published when no messages have been received from that partition in `idlePartitionEventInterval` (if configured).
- `ListenerContainerPartitionNoLongerIdleEvent`: published when a record is consumed from a partition that has previously published a `ListenerContainerPartitionIdleEvent`.
- `NonResponsiveConsumerEvent`: published when the consumer appears to be blocked in the `poll` method.
- `ConsumerPartitionPausedEvent`: published by each consumer when a partition is paused.
- `ConsumerPartitionResumedEvent`: published by each consumer when a partition is resumed.
- `ConsumerPausedEvent`: published by each consumer when the container is paused.
- `ConsumerResumedEvent`: published by each consumer when the container is resumed.
- `ConsumerStoppingEvent`: published by each consumer just before stopping.
- `ConsumerStoppedEvent`: published after the consumer is closed.
  See [Thread Safety](#kafka-thread-safety).
- `ConsumerRetryAuthEvent`: published when authentication or authorization of a consumer fails and is being retried.
- `ConsumerRetryAuthSuccessfulEvent`: published when authentication or authorization has been retried successfully. Can only occur when there has been a `ConsumerRetryAuthEvent` before.
- `ContainerStoppedEvent`: published when all consumers have stopped.
- `ConcurrentContainerStoppedEvent`: published when the `ConcurrentMessageListenerContainer` has stopped.

> [!IMPORTANT]
> By default, the application context’s event multicaster invokes event listeners on the calling thread.
> If you change the multicaster to use an async executor, you must not invoke any `Consumer` methods when the event contains a reference to the consumer.

The `ListenerContainerIdleEvent` has the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.
- `id`: The listener ID (or container bean name).
- `idleTime`: The time the container had been idle when the event was published.
- `topicPartitions`: The topics and partitions that the container was assigned at the time the event was generated.
- `consumer`: A reference to the Kafka `Consumer` object.
  For example, if the consumer’s `pause()` method was previously called, it can `resume()` when the event is received.
- `paused`: Whether the container is currently paused.
  See [Pausing and Resuming Listener Containers](#kafka-pause-resume) for more information.

The `ListenerContainerNoLongerIdleEvent` has the same properties, except `idleTime` and `paused`.

The `ListenerContainerPartitionIdleEvent` has the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.
- `id`: The listener ID (or container bean name).
- `idleTime`: The time partition consumption had been idle when the event was published.
- `topicPartition`: The topic and partition that triggered the event.
- `consumer`: A reference to the Kafka `Consumer` object.
  For example, if the consumer’s `pause()` method was previously called, it can `resume()` when the event is received.
- `paused`: Whether that partition consumption is currently paused for that consumer.
  See [Pausing and Resuming Listener Containers](#kafka-pause-resume) for more information.

The `ListenerContainerPartitionNoLongerIdleEvent` has the same properties, except `idleTime` and `paused`.

The `NonResponsiveConsumerEvent` has the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.
- `id`: The listener ID (or container bean name).
- `timeSinceLastPoll`: The time just before the container last called `poll()`.
- `topicPartitions`: The topics and partitions that the container was assigned at the time the event was generated.
- `consumer`: A reference to the Kafka `Consumer` object.
  For example, if the consumer’s `pause()` method was previously called, it can `resume()` when the event is received.
- `paused`: Whether the container is currently paused.
  See [Pausing and Resuming Listener Containers](#kafka-pause-resume) for more information.

The `ConsumerPausedEvent`, `ConsumerResumedEvent`, and `ConsumerStopping` events have the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.
- `partitions`: The `TopicPartition` instances involved.

The `ConsumerPartitionPausedEvent`, `ConsumerPartitionResumedEvent` events have the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.
- `partition`: The `TopicPartition` instance involved.

The `ConsumerRetryAuthEvent` event has the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.
- `reason`:

  - `AUTHENTICATION` - the event was published because of an authentication exception.
  - `AUTHORIZATION` - the event was published because of an authorization exception.

The `ConsumerStartingEvent`, `ConsumerStartedEvent`, `ConsumerFailedToStartEvent`, `ConsumerStoppedEvent`, `ConsumerRetryAuthSuccessfulEvent` and `ContainerStoppedEvent` events have the following properties:

- `source`: The listener container instance that published the event.
- `container`: The listener container or the parent listener container, if the source container is a child.

All containers (whether a child or a parent) publish `ContainerStoppedEvent`.
For a parent container, the source and container properties are identical.

In addition, the `ConsumerStoppedEvent` has the following additional property:

- `reason`:

  - `NORMAL` - the consumer stopped normally (container was stopped).
  - `ABNORMAL` - the consumer stopped abnormally (container was stopped abnormally).
  - `ERROR` - a `java.lang.Error` was thrown.
  - `FENCED` - the transactional producer was fenced and the `stopContainerWhenFenced` container property is `true`.
  - `AUTH` - an `AuthenticationException` or `AuthorizationException` was thrown and the `authExceptionRetryInterval` is not configured.
  - `NO_OFFSET` - there is no offset for a partition and the `auto.offset.reset` policy is `none`.

You can use this event to restart the container after such a condition:

```java
if (event.getReason().equals(Reason.FENCED)) {
    event.getSource(MessageListenerContainer.class).start();
}
```

<a id="kafka-events--idle-containers"></a>
<a id="kafka-events--detecting-idle-and-non-responsive-consumers"></a>

## Detecting Idle and Non-Responsive Consumers

While efficient, one problem with asynchronous consumers is detecting when they are idle.
You might want to take some action if no messages arrive for some period of time.

You can configure the listener container to publish a `ListenerContainerIdleEvent` when some time passes with no message delivery.
While the container is idle, an event is published every `idleEventInterval` milliseconds.

To configure this feature, set the `idleEventInterval` on the container.
The following example shows how to do so:

```java
@Bean public KafkaMessageListenerContainer(ConsumerFactory<String, String> consumerFactory) {ContainerProperties containerProps = new ContainerProperties("topic1", "topic2"); ...containerProps.setIdleEventInterval(60000L); ...KafkaMessageListenerContainer<String, String> container = new KafKaMessageListenerContainer<>(consumerFactory, containerProps); return container;}
```

The following example shows how to set the `idleEventInterval` for a `@KafkaListener`:

```java
@Bean public ConcurrentKafkaListenerContainerFactory kafkaListenerContainerFactory() {ConcurrentKafkaListenerContainerFactory<String, String> factory =new ConcurrentKafkaListenerContainerFactory<>(); ...factory.getContainerProperties().setIdleEventInterval(60000L); ...return factory;}
```

In each of these cases, an event is published once per minute while the container is idle.

If, for some reason, the consumer `poll()` method does not exit, no messages are received and idle events cannot be generated (this was a problem with early versions of the `kafka-clients` when the broker wasn’t reachable).
In this case, the container publishes a `NonResponsiveConsumerEvent` if a poll does not return within `3x` the `pollTimeout` property.
By default, this check is performed once every 30 seconds in each container.
You can modify this behavior by setting the `monitorInterval` (default 30 seconds) and `noPollThreshold` (default 3.0) properties in the `ContainerProperties` when configuring the listener container.
The `noPollThreshold` should be greater than `1.0` to avoid getting spurious events due to a race condition.
Receiving such an event lets you stop the containers, thus waking the consumer so that it can stop.

Starting with version 2.6.2, if a container has published a `ListenerContainerIdleEvent`, it will publish a `ListenerContainerNoLongerIdleEvent` when a record is subsequently received.

<a id="kafka-events--event-consumption"></a>

## Event Consumption

You can capture these events by implementing `ApplicationListener` — either a general listener or one narrowed to only receive this specific event.
You can also use `@EventListener`, introduced in Spring Framework 4.2.

The next example combines `@KafkaListener` and `@EventListener` into a single class.
You should understand that the application listener gets events for all containers, so you may need to check the listener ID if you want to take specific action based on which container is idle.
You can also use the `@EventListener`'s `condition` for this purpose.

See [Application Events](#kafka-events) for information about event properties.

The event is normally published on the consumer thread, so it is safe to interact with the `Consumer` object.

The following example uses both `@KafkaListener` and `@EventListener`:

```java
public class Listener {
@KafkaListener(id = "qux", topics = "annotated") public void listen4(@Payload String foo, Acknowledgment ack) {...}
@EventListener(condition = "event.listenerId.startsWith('qux-')") public void eventHandler(ListenerContainerIdleEvent event) {...}
}
```

> [!IMPORTANT]
> Event listeners see events for all containers.
> Consequently, in the preceding example, we narrow the events received based on the listener ID.
> Since containers created for the `@KafkaListener` support concurrency, the actual containers are named `id-n` where the `n` is a unique value for each instance to support the concurrency.
> That is why we use `startsWith` in the condition.

> [!WARNING]
> If you wish to use the idle event to stop the listener container, you should not call `container.stop()` on the thread that calls the listener.
> Doing so causes delays and unnecessary log messages.
> Instead, you should hand off the event to a different thread that can then stop the container.
> Also, you should not `stop()` the container instance if it is a child container.
> You should stop the concurrent container instead.

<a id="kafka-events--current-positions-when-idle"></a>

### Current Positions when Idle

Note that you can obtain the current positions when idle is detected by implementing `ConsumerSeekAware` in your listener.
See `onIdleContainer()` in [seek](#kafka-seek).

[Dynamically Creating Containers](#kafka-dynamic-containers)
[Topic/Partition Initial Offset](#kafka-topic-partition-initial-offset)

---

<a id="kafka-topic-partition-initial-offset"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/topic/partition-initial-offset.html -->

<!-- page_index: 33 -->

# Topic/Partition Initial Offset

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-topic-partition-initial-offset--page-title"></a>
<a id="kafka-topic-partition-initial-offset--topic-partition-initial-offset"></a>

# Topic/Partition Initial Offset

There are several ways to set the initial offset for a partition.

When manually assigning partitions, you can set the initial offset (if desired) in the configured `TopicPartitionOffset` arguments (see [Message Listener Containers](#kafka-receiving-messages-message-listener-container)).
You can also seek to a specific offset at any time.

When you use group management where the broker assigns partitions:

- For a new `group.id`, the initial offset is determined by the `auto.offset.reset` consumer property (`earliest` or `latest`).
- For an existing group ID, the initial offset is the current offset for that group ID.
  You can, however, seek to a specific offset during initialization (or at any time thereafter).

[Application Events](#kafka-events)
[Seeking to a Specific Offset](#kafka-seek)

---

<a id="kafka-seek"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/seek.html -->

<!-- page_index: 34 -->

# Seeking to a Specific Offset

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-seek--page-title"></a>
<a id="kafka-seek--seeking-to-a-specific-offset"></a>

# Seeking to a Specific Offset

In order to seek, your listener must implement `ConsumerSeekAware`, which has the following methods:

```java
void registerSeekCallback(ConsumerSeekCallback callback);

void onPartitionsAssigned(Map<TopicPartition, Long> assignments, ConsumerSeekCallback callback);

void onPartitionsRevoked(Collection<TopicPartition> partitions);

void onIdleContainer(Map<TopicPartition, Long> assignments, ConsumerSeekCallback callback);
```

The `registerSeekCallback` is called when the container is started and whenever partitions are assigned.
You should use this callback when seeking at some arbitrary time after initialization.
You should save a reference to the callback.
If you use the same listener in multiple containers (or in a `ConcurrentMessageListenerContainer`), you should store the callback in a `ThreadLocal` or some other structure keyed by the listener `Thread`.

When using group management, `onPartitionsAssigned` is called when partitions are assigned.
You can use this method, for example, for setting initial offsets for the partitions, by calling the callback.
You can also use this method to associate this thread’s callback with the assigned partitions (see the example below).
You must use the callback argument, not the one passed into `registerSeekCallback`.
Starting with version 2.5.5, this method is called, even when using [manual partition assignment](#kafka-receiving-messages-listener-annotation--manual-assignment).

`onPartitionsRevoked` is called when the container is stopped or Kafka revokes assignments.
You should discard this thread’s callback and remove any associations to the revoked partitions.

The callback has the following methods:

```java
void seek(String topic, int partition, long offset);

void seek(String topic, int partition, Function<Long, Long> offsetComputeFunction);

void seekToBeginning(String topic, int partition);

void seekToBeginning(Collection<TopicPartitions> partitions);

void seekToEnd(String topic, int partition);

void seekToEnd(Collection<TopicPartitions> partitions);

void seekRelative(String topic, int partition, long offset, boolean toCurrent);

void seekToTimestamp(String topic, int partition, long timestamp);

void seekToTimestamp(Collection<TopicPartition> topicPartitions, long timestamp);

String getGroupId();
```

The two different variants of the `seek` methods provide a way to seek to an arbitrary offset.
The method that takes a `Function` as an argument to compute the offset was added in version 3.2 of the framework.
This function provides access to the current offset (the current position returned by the consumer, which is the next offset to be fetched).
The user can decide what offset to seek to based on the current offset in the consumer as part of the function definition.

`seekRelative` was added in version 2.3, to perform relative seeks.

- `offset` negative and `toCurrent` `false` - seek relative to the end of the partition.
- `offset` positive and `toCurrent` `false` - seek relative to the beginning of the partition.
- `offset` negative and `toCurrent` `true` - seek relative to the current position (rewind).
- `offset` positive and `toCurrent` `true` - seek relative to the current position (fast forward).

The `seekToTimestamp` methods were also added in version 2.3.

> [!NOTE]
> When seeking to the same timestamp for multiple partitions in the `onIdleContainer` or `onPartitionsAssigned` methods, the second method is preferred because it is more efficient to find the offsets for the timestamps in a single call to the consumer’s `offsetsForTimes` method.
> When called from other locations, the container will gather all timestamp seek requests and make one call to `offsetsForTimes`.

You can also perform seek operations from `onIdleContainer()` when an idle container is detected.
See [Detecting Idle and Non-Responsive Consumers](#kafka-events--idle-containers) for how to enable idle container detection.

> [!NOTE]
> The `seekToBeginning` method that accepts a collection is useful, for example, when processing a compacted topic and you wish to seek to the beginning every time the application is started:

```java
public class MyListener implements ConsumerSeekAware {
...
@Override public void onPartitionsAssigned(Map<TopicPartition, Long> assignments, ConsumerSeekCallback callback) {callback.seekToBeginning(assignments.keySet());}
}
```

To arbitrarily seek at runtime, use the callback reference from the `registerSeekCallback` for the appropriate thread.

Here is a trivial Spring Boot application that demonstrates how to use the callback; it sends 10 records to the topic; hitting `<Enter>` in the console causes all partitions to seek to the beginning.

```java
@SpringBootApplication public class SeekExampleApplication {
public static void main(String[] args) {SpringApplication.run(SeekExampleApplication.class, args);}
@Bean public ApplicationRunner runner(Listener listener, KafkaTemplate<String, String> template) {return args -> {IntStream.range(0, 10).forEach(i -> template.send(new ProducerRecord<>("seekExample", i % 3, "foo", "bar"))); while (true) {System.in.read(); listener.seekToStart();} };}
@Bean public NewTopic topic() {return new NewTopic("seekExample", 3, (short) 1);}
}
@Component class Listener implements ConsumerSeekAware {
private static final Logger logger = LoggerFactory.getLogger(Listener.class);
private final ThreadLocal<ConsumerSeekCallback> callbackForThread = new ThreadLocal<>();
private final Map<TopicPartition, ConsumerSeekCallback> callbacks = new ConcurrentHashMap<>();
@Override public void registerSeekCallback(ConsumerSeekCallback callback) {this.callbackForThread.set(callback);}
@Override public void onPartitionsAssigned(Map<TopicPartition, Long> assignments, ConsumerSeekCallback callback) {assignments.keySet().forEach(tp -> this.callbacks.put(tp, this.callbackForThread.get()));}
@Override public void onPartitionsRevoked(Collection<TopicPartition> partitions) {partitions.forEach(tp -> this.callbacks.remove(tp)); this.callbackForThread.remove();}
@Override public void onIdleContainer(Map<TopicPartition, Long> assignments, ConsumerSeekCallback callback) {}
@KafkaListener(id = "seekExample", topics = "seekExample", concurrency = "3") public void listen(ConsumerRecord<String, String> in) {logger.info(in.toString());}
public void seekToStart() {this.callbacks.forEach((tp, callback) -> callback.seekToBeginning(tp.topic(), tp.partition()));}
}
```

To make things simpler, version 2.3 added the `AbstractConsumerSeekAware` class, which keeps track of which callback is to be used for a topic/partition.
The following example shows how to seek to the last record processed, in each partition, each time the container goes idle.
It also has methods that allow arbitrary external calls to rewind partitions by one record.

```java
public class SeekToLastOnIdleListener extends AbstractConsumerSeekAware {
@KafkaListener(id = "seekOnIdle", topics = "seekOnIdle") public void listen(String in) {...}
@Override public void onIdleContainer(Map<TopicPartition, Long> assignments,ConsumerSeekCallback callback) {
assignments.keySet().forEach(tp -> callback.seekRelative(tp.topic(), tp.partition(), -1, true));}
/** * Rewind all partitions one record.*/ public void rewindAllOneRecord() {getTopicsAndCallbacks() .forEach((tp, callbacks) -> callbacks.forEach(callback -> callback.seekRelative(tp.topic(), tp.partition(), -1, true)) );}
/** * Rewind one partition one record.*/ public void rewindOnePartitionOneRecord(String topic, int partition) {getSeekCallbacksFor(new TopicPartition(topic, partition)) .forEach(callback -> callback.seekRelative(topic, partition, -1, true));}
}
```

Version 2.6 added convenience methods to the abstract class:

- `seekToBeginning()` - seeks all assigned partitions to the beginning.
- `seekToEnd()` - seeks all assigned partitions to the end.
- `seekToTimestamp(long timestamp)` - seeks all assigned partitions to the offset represented by that timestamp.

Example:

```java
public class MyListener extends AbstractConsumerSeekAware {
@KafkaListener(...) void listen(...) {...}}
public class SomeOtherBean {
MyListener listener;
...
void someMethod() {this.listener.seekToTimestamp(System.currentTimeMillis() - 60_000);}
}
```

As of version 3.3, a new method `getGroupId()` was introduced in the `ConsumerSeekAware.ConsumerSeekCallback` interface.
This method is particularly useful when you need to identify the consumer group associated with a specific seek callback.

> [!NOTE]
> When using a class that extends `AbstractConsumerSeekAware`, a seek operation performed in one listener may impact all listeners in the same class.
> This might not always be the desired behavior.
> To address this, you can use the `getGroupId()` method provided by the callback.
> This allows you to perform seek operations selectively, targeting only the consumer group of interest.

[Topic/Partition Initial Offset](#kafka-topic-partition-initial-offset)
[Container factory](#kafka-container-factory)

---

<a id="kafka-container-factory"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/container-factory.html -->

<!-- page_index: 35 -->

# Container factory

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-container-factory--page-title"></a>
<a id="kafka-container-factory--container-factory"></a>

# Container factory

As discussed in [`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation), a `ConcurrentKafkaListenerContainerFactory` is used to create containers for annotated methods.

Starting with version 2.2, you can use the same factory to create any `ConcurrentMessageListenerContainer`.
This might be useful if you want to create several containers with similar properties or you wish to use some externally configured factory, such as the one provided by Spring Boot auto-configuration.
Once the container is created, you can further modify its properties, many of which are set by using `container.getContainerProperties()`.
The following example configures a `ConcurrentMessageListenerContainer`:

```java
@Bean
public ConcurrentMessageListenerContainer<String, String>(
        ConcurrentKafkaListenerContainerFactory<String, String> factory) {

    ConcurrentMessageListenerContainer<String, String> container =
        factory.createContainer("topic1", "topic2");
    container.setMessageListener(m -> { ... } );
    return container;
}
```

> [!IMPORTANT]
> Containers created this way are not added to the endpoint registry.
> They should be created as `@Bean` definitions so that they are registered with the application context.

Starting with version 2.3.4, you can add a `ContainerCustomizer` to the factory to further configure each container after it has been created and configured.

```java
@Bean public KafkaListenerContainerFactory<?> kafkaListenerContainerFactory() {ConcurrentKafkaListenerContainerFactory<Integer, String> factory =new ConcurrentKafkaListenerContainerFactory<>(); ...factory.setContainerCustomizer(container -> { /* customize the container */ }); return factory;}
```

Starting with version 3.1, it’s also possible to apply the same kind of customization on a single listener by specifying the bean name of a 'ContainerPostProcessor' on the KafkaListener annotation.

```java
@Bean public ContainerPostProcessor<String, String, AbstractMessageListenerContainer<String, String>> customContainerPostProcessor() {return container -> { /* customize the container */ };}
...
@KafkaListener(..., containerPostProcessor="customContainerPostProcessor", ...)
```

[Seeking to a Specific Offset](#kafka-seek)
[Thread Safety](#kafka-thread-safety)

---

<a id="kafka-thread-safety"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/thread-safety.html -->

<!-- page_index: 36 -->

# Thread Safety

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-thread-safety--page-title"></a>
<a id="kafka-thread-safety--thread-safety"></a>

# Thread Safety

When using a concurrent message listener container, a single listener instance is invoked on all consumer threads.
Listeners, therefore, need to be thread-safe, and it is preferable to use stateless listeners.
If it is not possible to make your listener thread-safe or adding synchronization would significantly reduce the benefit of adding concurrency, you can use one of a few techniques:

- Use `n` containers with `concurrency=1` with a prototype scoped `MessageListener` bean so that each container gets its own instance (this is not possible when using `@KafkaListener`).
- Keep the state in `ThreadLocal<?>` instances.
- Have the singleton listener delegate to a bean that is declared in `SimpleThreadScope` (or a similar scope).

To facilitate cleaning up thread state (for the second and third items in the preceding list), starting with version 2.2, the listener container publishes a `ConsumerStoppedEvent` when each thread exits.
You can consume these events with an `ApplicationListener` or `@EventListener` method to remove `ThreadLocal<?>` instances or `remove()` thread-scoped beans from the scope.
Note that `SimpleThreadScope` does not destroy beans that have a destruction interface (such as `DisposableBean`), so you should `destroy()` the instance yourself.

> [!IMPORTANT]
> By default, the application context’s event multicaster invokes event listeners on the calling thread.
> If you change the multicaster to use an async executor, thread cleanup is not effective.

<a id="kafka-thread-safety--_special_note_on_virtual_threads_and_concurrent_message_listener_containers"></a>
<a id="kafka-thread-safety--special-note-on-virtual-threads-and-concurrent-message-listener-containers"></a>

## Special Note on Virtual Threads and Concurrent Message Listener Containers

Because of certain limitations in the underlying library classes still using `synchronized` blocks for thread coordination, applications need to be cautious when using virtual threads with concurrent message listener containers.
When virtual threads are enabled, if the concurrency exceeds the available number of platform threads, it is very likely for the virtual threads to be pinned on the platform threads and possible race conditions.
Therefore, as the 3rd party libraries that Spring for Apache Kafka uses evolves to fully support virtual threads, it is recommended to keep the concurrency on the message listener container to be equal to or less than the number of platform threads.
This way, the applications avoid any race conditions between the threads and the virtual threads being pinned on platform threads.

[Container factory](#kafka-container-factory)
[Monitoring](#kafka-micrometer)

---

<a id="kafka-micrometer"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/micrometer.html -->

<!-- page_index: 37 -->

# Monitoring

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-micrometer--page-title"></a>
<a id="kafka-micrometer--monitoring"></a>

# Monitoring

<a id="kafka-micrometer--monitoring-listener-performance"></a>

## Monitoring Listener Performance

Starting with version 2.3, the listener container will automatically create and update Micrometer `Timer`s for the listener, if `Micrometer` is detected on the classpath, and a single `MeterRegistry` is present in the application context.
The timers can be disabled by setting the `ContainerProperty`'s `micrometerEnabled` to `false`.

Two timers are maintained - one for successful calls to the listener and one for failures.

The timers are named `spring.kafka.listener` and have the following tags:

- `name` : (container bean name)
- `result` : `success` or `failure`
- `exception` : `none` or `ListenerExecutionFailedException`

You can add additional tags using the `ContainerProperties`'s `micrometerTags` property.

Starting with versions 2.9.8, 3.0.6, you can provide a function in `ContainerProperties`'s `micrometerTagsProvider`; the function receives the `ConsumerRecord<?, ?>` and returns tags which can be based on that record, and merged with any static tags in `micrometerTags`.

> [!NOTE]
> With the concurrent container, timers are created for each thread and the `name` tag is suffixed with `-n` where n is `0` to `concurrency-1`.

<a id="kafka-micrometer--monitoring-kafkatemplate-performance"></a>

## Monitoring KafkaTemplate Performance

Starting with version 2.5, the template will automatically create and update Micrometer `Timer`s for send operations, if `Micrometer` is detected on the classpath, and a single `MeterRegistry` is present in the application context.
The timers can be disabled by setting the template’s `micrometerEnabled` property to `false`.

Two timers are maintained - one for successful calls to the listener and one for failures.

The timers are named `spring.kafka.template` and have the following tags:

- `name` : (template bean name)
- `result` : `success` or `failure`
- `exception` : `none` or the exception class name for failures

You can add additional tags using the template’s `micrometerTags` property.

Starting with versions 2.9.8, 3.0.6, you can provide a `KafkaTemplate.setMicrometerTagsProvider(Function<ProducerRecord<?, ?>, Map<String, String>>)` property; the function receives the `ProducerRecord<?, ?>` and returns tags which can be based on that record, and merged with any static tags in `micrometerTags`.

<a id="kafka-micrometer--micrometer-native"></a>
<a id="kafka-micrometer--micrometer-native-metrics"></a>

## Micrometer Native Metrics

Starting with version 2.5, the framework provides [Factory Listeners](#kafka-connecting--factory-listeners) to manage a Micrometer `KafkaClientMetrics` instance whenever producers and consumers are created and closed.

To enable this feature, simply add the listeners to your producer and consumer factories:

```java
@Bean public ConsumerFactory<String, String> myConsumerFactory() {Map<String, Object> configs = consumerConfigs(); ...DefaultKafkaConsumerFactory<String, String> cf = new DefaultKafkaConsumerFactory<>(configs); ...cf.addListener(new MicrometerConsumerListener<String, String>(meterRegistry(),Collections.singletonList(new ImmutableTag("customTag", "customTagValue")))); ...return cf;}
@Bean public ProducerFactory<String, String> myProducerFactory() {Map<String, Object> configs = producerConfigs(); configs.put(ProducerConfig.CLIENT_ID_CONFIG, "myClientId"); ...DefaultKafkaProducerFactory<String, String> pf = new DefaultKafkaProducerFactory<>(configs); ...pf.addListener(new MicrometerProducerListener<String, String>(meterRegistry(),Collections.singletonList(new ImmutableTag("customTag", "customTagValue")))); ...return pf;}
```

The consumer/producer `id` passed to the listener is added to the meter’s tags with tag name `spring.id`.

An example of obtaining one of the Kafka metrics

```java
double count = this.meterRegistry.get("kafka.producer.node.incoming.byte.total")
                .tag("customTag", "customTagValue")
                .tag("spring.id", "myProducerFactory.myClientId-1")
                .functionCounter()
                .count();
```

A similar listener is provided for the `StreamsBuilderFactoryBean` - see [KafkaStreams Micrometer Support](#streams--streams-micrometer).

Starting with version 3.3, a `KafkaMetricsSupport` abstract class is introduced to manage `io.micrometer.core.instrument.binder.kafka.KafkaMetrics` binding into a `MeterRegistry` for provided Kafka client.
This class is a super for the mentioned above `MicrometerConsumerListener`, `MicrometerProducerListener` and `KafkaStreamsMicrometerListener`.
However, it can be used for any Kafka client use-cases.
The class needs to be extended and its `bindClient()` and `unbindClient()` API have to be called to connect Kafka client metrics with a Micrometer collector.

<a id="kafka-micrometer--observation"></a>
<a id="kafka-micrometer--micrometer-observation"></a>

## Micrometer Observation

Using Micrometer for observation is now supported, since version 3.0, for the `KafkaTemplate` and listener containers.

Set `observationEnabled` to `true` on the `KafkaTemplate` and `ContainerProperties` to enable observation; this will disable [Micrometer Timers](#kafka-micrometer) because the timers will now be managed with each observation.

> [!IMPORTANT]
> Micrometer Observation does not support batch listener; this will enable Micrometer Timers

Refer to [Micrometer Tracing](https://docs.micrometer.io/tracing/reference/1.7) for more information.

To add tags to timers/traces, configure a custom `KafkaTemplateObservationConvention` or `KafkaListenerObservationConvention` to the template or listener container, respectively.

The default implementations add the `bean.name` tag for template observations and `listener.id` tag for containers.

You can either subclass `DefaultKafkaTemplateObservationConvention` or `DefaultKafkaListenerObservationConvention` or provide completely new implementations.

See [Micrometer Observation Documentation](#appendix-micrometer--observation-gen) for details of the default observations that are recorded.

Starting with version 3.0.6, you can add dynamic tags to the timers and traces, based on information in the consumer or producer records.
To do so, add a custom `KafkaListenerObservationConvention` and/or `KafkaTemplateObservationConvention` to the listener container properties or `KafkaTemplate` respectively.
The `record` property in both observation contexts contains the `ConsumerRecord` or `ProducerRecord` respectively.

The sender and receiver contexts `remoteServiceName` properties are set to the Kafka `clusterId` property; this is retrieved by a `KafkaAdmin`.
If, for some reason - perhaps lack of admin permissions, you cannot retrieve the cluster id, starting with version 3.1, you can set a manual `clusterId` on the `KafkaAdmin` and inject it into `KafkaTemplate`s and listener containers.
When it is `null` (default), the admin will invoke the `describeCluster` admin operation to retrieve it from the broker.

<a id="kafka-micrometer--batch-listener-obs"></a>
<a id="kafka-micrometer--batch-listener-observations"></a>

### Batch Listener Observations

When using a batch listener, by default, no observations are created, even if a `ObservationRegistry` is present.
This is because the scope of an observation is tied to the thread, and with a batch listener, there is no one-to-one mapping between an observation and a record.

To enable per-record observations in a batch listener, set the container factory property `recordObservationsInBatch` to `true`.

```java
@Bean
ConcurrentKafkaListenerContainerFactory<?, ?> kafkaListenerContainerFactory(
        ConcurrentKafkaListenerContainerFactoryConfigurer configurer,
        ConsumerFactory<Object, Object> kafkaConsumerFactory) {

    ConcurrentKafkaListenerContainerFactory<Object, Object> factory = new ConcurrentKafkaListenerContainerFactory<>();
    configurer.configure(factory, kafkaConsumerFactory);
    factory.getContainerProperties().setRecordObservationsInBatch(true);
    return factory;
}
```

When this property is `true`, an observation will be created for each record in the batch, but the observation is not propagated to the listener method.
The application can then use the observation context to track the processing of each record in the batch.
This allows you to have visibility into the processing of each record, even within a batch context.

[Thread Safety](#kafka-thread-safety)
[Transactions](#kafka-transactions)

---

<a id="kafka-transactions"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/transactions.html -->

<!-- page_index: 38 -->

# Transactions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-transactions--page-title"></a>
<a id="kafka-transactions--transactions"></a>

# Transactions

This section describes how Spring for Apache Kafka supports transactions.

<a id="kafka-transactions--overview"></a>

## Overview

The 0.11.0.0 client library added support for transactions.
Spring for Apache Kafka adds support in the following ways:

- `KafkaTransactionManager`: Used with normal Spring transaction support (`@Transactional`, `TransactionTemplate`, etc.)
- Transactional `KafkaMessageListenerContainer`
- Local transactions with `KafkaTemplate`
- Transaction synchronization with other transaction managers

Transactions are enabled by providing the `DefaultKafkaProducerFactory` with a `transactionIdPrefix`.
In that case, instead of managing a single shared `Producer`, the factory maintains a cache of transactional producers.
When the user calls `close()` on a producer, it is returned to the cache for reuse instead of actually being closed.
The `transactional.id` property of each producer is `transactionIdPrefix` + `n`, where `n` starts with `0` and is incremented for each new producer.
In previous versions of Spring for Apache Kafka, the `transactional.id` was generated differently for transactions started by a listener container with a record-based listener, to support fencing zombies, which is not necessary anymore, with `EOSMode.V2` being the only option starting with 3.0.
For applications running with multiple instances, the `transactionIdPrefix` must be unique per instance.

Also see [Exactly Once Semantics](#kafka-exactly-once).

Also see [`transactionIdPrefix`](#kafka-transactions--transaction-id-prefix).

With Spring Boot, it is only necessary to set the `spring.kafka.producer.transaction-id-prefix` property - Spring Boot will automatically configure a `KafkaTransactionManager` bean and wire it into the listener container.

> [!IMPORTANT]
> Starting with version 2.5.8, you can now configure the `maxAge` property on the producer factory.
> This is useful when using transactional producers that might lay idle for the broker’s `transactional.id.expiration.ms`.
> With current `kafka-clients`, this can cause a `ProducerFencedException` without a rebalance.
> By setting the `maxAge` to less than `transactional.id.expiration.ms`, the factory will refresh the producer if it is past its max age.

<a id="kafka-transactions--using-kafkatransactionmanager"></a>

## Using `KafkaTransactionManager`

The `KafkaTransactionManager` is an implementation of Spring Framework’s `PlatformTransactionManager`.
It is provided with a reference to the producer factory in its constructor.
If you provide a custom producer factory, it must support transactions.
See `ProducerFactory.transactionCapable()`.

You can use the `KafkaTransactionManager` with normal Spring transaction support (`@Transactional`, `TransactionTemplate`, and others).
If a transaction is active, any `KafkaTemplate` operations performed within the scope of the transaction use the transaction’s `Producer`.
The manager commits or rolls back the transaction, depending on success or failure.
You must configure the `KafkaTemplate` to use the same `ProducerFactory` as the transaction manager.

<a id="kafka-transactions--transaction-synchronization"></a>

## Transaction Synchronization

This section refers to producer-only transactions (those not started by a listener container); see [Using Consumer-Initiated Transactions](#kafka-transactions--container-transaction-manager) for information about chaining transactions when the container starts the transaction.

If you want to send records to kafka and perform some database updates, you can use normal Spring transaction management with, say, a `DataSourceTransactionManager`.

```java
@Transactional
public void process(List<Thing> things) {
    things.forEach(thing -> this.kafkaTemplate.send("topic", thing));
    updateDb(things);
}
```

The interceptor for the `@Transactional` annotation starts the transaction and the `KafkaTemplate` will synchronize a transaction with that transaction manager; each send will participate in that transaction.
When the method exits, the database transaction will commit followed by the Kafka transaction.
If you wish the commits to be performed in the reverse order (Kafka first), use nested `@Transactional` methods, with the outer method configured to use the `DataSourceTransactionManager`, and the inner method configured to use the `KafkaTransactionManager`.

See [Examples of Kafka Transactions with Other Transaction Managers](#tips--ex-jdbc-sync) for examples of an application that synchronizes JDBC and Kafka transactions in Kafka-first or DB-first configurations.

> [!NOTE]
> Starting with versions 2.5.17, 2.6.12, 2.7.9 and 2.8.0, if the commit fails on the synchronized transaction (after the primary transaction has committed), the exception will be thrown to the caller.
> Previously, this was silently ignored (logged at debug level).
> Applications should take remedial action, if necessary, to compensate for the committed primary transaction.

<a id="kafka-transactions--container-transaction-manager"></a>
<a id="kafka-transactions--using-consumer-initiated-transactions"></a>

## Using Consumer-Initiated Transactions

The `ChainedKafkaTransactionManager` is now deprecated, since version 2.7; see the JavaDocs for its super class `ChainedTransactionManager` for more information.
Instead, use a `KafkaTransactionManager` in the container to start the Kafka transaction and annotate the listener method with `@Transactional` to start the other transaction.

See [Examples of Kafka Transactions with Other Transaction Managers](#tips--ex-jdbc-sync) for an example application that chains JDBC and Kafka transactions.

> [!IMPORTANT]
> [Non-Blocking Retries](#retrytopic) cannot combine with [Container Transactions](#kafka-transactions--container-transaction-manager).
> When the listener code throws an exception, the container transaction commit succeeds, and the record is sent to the retryable topic.

<a id="kafka-transactions--kafkatemplate-local-transactions"></a>

## `KafkaTemplate` Local Transactions

You can use the `KafkaTemplate` to execute a series of operations within a local transaction.
The following example shows how to do so:

```java
boolean result = template.executeInTransaction(t -> {
    t.sendDefault("thing1", "thing2");
    t.sendDefault("cat", "hat");
    return true;
});
```

The argument in the callback is the template itself (`this`).
If the callback exits normally, the transaction is committed.
If an exception is thrown, the transaction is rolled back.

> [!NOTE]
> If there is a `KafkaTransactionManager` (or synchronized) transaction in process, it is not used.
> Instead, a new "nested" transaction is used.

<a id="kafka-transactions--transaction-id-prefix"></a>
<a id="kafka-transactions--transactionidprefix"></a>

## `TransactionIdPrefix`

With `EOSMode.V2` (aka `BETA`), the only supported mode, it is no longer necessary to use the same `transactional.id`, even for consumer-initiated transactions; in fact, it must be unique on each instance the same as for producer-initiated transactions.
This property must have a different value on each application instance.

<a id="kafka-transactions--transaction-id-suffix-fixed"></a>
<a id="kafka-transactions--transactionidsuffix-fixed"></a>

## `TransactionIdSuffix` Fixed

Since 3.2, a new `TransactionIdSuffixStrategy` interface was introduced to manage `transactional.id` suffix.
The default implementation is `DefaultTransactionIdSuffixStrategy` when setting `maxCache` greater than zero can reuse `transactional.id` within a specific range, otherwise suffixes will be generated on the fly by incrementing a counter.
When a transaction producer is requested and `transactional.id` all in use, throw a `NoProducerAvailableException`.
User can then use a `RetryTemplate` configured to retry that exception, with a suitably configured back off.

```java
public static class Config {
@Bean public ProducerFactory<String, String> myProducerFactory() {Map<String, Object> configs = producerConfigs(); configs.put(ProducerConfig.CLIENT_ID_CONFIG, "myClientId"); ...DefaultKafkaProducerFactory<String, String> pf = new DefaultKafkaProducerFactory<>(configs); ...TransactionIdSuffixStrategy ss = new DefaultTransactionIdSuffixStrategy(5); pf.setTransactionIdSuffixStrategy(ss); return pf;}
}
```

When setting `maxCache` to 5, `transactional.id` is `my.txid.`+`{0-4}`.

> [!IMPORTANT]
> When using `KafkaTransactionManager` with the `ConcurrentMessageListenerContainer` and enabling `maxCache`, it is necessary to set `maxCache` to a value greater than or equal to `concurrency`.
> If a `MessageListenerContainer` is unable to acquire a `transactional.id` suffix, it will throw a `NoProducerAvailableException`.
> When using nested transactions in the `ConcurrentMessageListenerContainer`, it is necessary to adjust the maxCache setting to handle the increased number of nested transactions.

<a id="kafka-transactions--tx-template-mixed"></a>
<a id="kafka-transactions--kafkatemplate-transactional-and-non-transactional-publishing"></a>

## `KafkaTemplate` Transactional and non-Transactional Publishing

Normally, when a `KafkaTemplate` is transactional (configured with a transaction-capable producer factory), transactions are required.
The transaction can be started by a `TransactionTemplate`, a `@Transactional` method, calling `executeInTransaction`, or by a listener container, when configured with a `KafkaTransactionManager`.
Any attempt to use the template outside the scope of a transaction results in the template throwing an `IllegalStateException`.
Starting with version 2.4.3, you can set the template’s `allowNonTransactional` property to `true`.
In that case, the template will allow the operation to run without a transaction, by calling the `ProducerFactory`'s `createNonTransactionalProducer()` method; the producer will be cached, or thread-bound, as normal for reuse.
See [Using `DefaultKafkaProducerFactory`](#kafka-sending-messages--producer-factory).

<a id="kafka-transactions--transactions-batch"></a>
<a id="kafka-transactions--transactions-with-batch-listeners"></a>

## Transactions with Batch Listeners

When a listener fails while transactions are being used, the `AfterRollbackProcessor` is invoked to take some action after the rollback occurs.
When using the default `AfterRollbackProcessor` with a record listener, seeks are performed so that the failed record will be redelivered.
With a batch listener, however, the whole batch will be redelivered because the framework doesn’t know which record in the batch failed.
See the [After-rollback Processor](#kafka-annotation-error-handling--after-rollback) for more information.

When using a batch listener, version 2.4.2 introduced an alternative mechanism to deal with failures while processing a batch: `BatchToRecordAdapter`.
When a container factory with `batchListener` set to true is configured with a `BatchToRecordAdapter`, the listener is invoked with one record at a time.
This enables error handling within the batch, while still making it possible to stop processing the entire batch, depending on the exception type.
A default `BatchToRecordAdapter` is provided, that can be configured with a standard `ConsumerRecordRecoverer` such as the `DeadLetterPublishingRecoverer`.
The following test case configuration snippet illustrates how to use this feature:

```java
public static class TestListener {
final List<String> values = new ArrayList<>();
@KafkaListener(id = "batchRecordAdapter", topics = "test") public void listen(String data) {values.add(data); if ("bar".equals(data)) {throw new RuntimeException("reject partial");}}
}
@Configuration @EnableKafka public static class Config {
ConsumerRecord<?, ?> failed;
@Bean public TestListener test() {return new TestListener();}
@Bean public ConsumerFactory<?, ?> consumerFactory() {return mock(ConsumerFactory.class);}
@Bean public ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory() {ConcurrentKafkaListenerContainerFactory factory = new ConcurrentKafkaListenerContainerFactory(); factory.setConsumerFactory(consumerFactory()); factory.setBatchListener(true); factory.setBatchToRecordAdapter(new DefaultBatchToRecordAdapter<>((record, ex) ->  {this.failed = record; })); return factory;}
}
```

[Monitoring](#kafka-micrometer)
[Exactly Once Semantics](#kafka-exactly-once)

---

<a id="kafka-exactly-once"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/exactly-once.html -->

<!-- page_index: 39 -->

# Exactly Once Semantics

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-exactly-once--page-title"></a>
<a id="kafka-exactly-once--exactly-once-semantics"></a>

# Exactly Once Semantics

You can provide a listener container with a `KafkaAwareTransactionManager` instance.
When so configured, the container starts a transaction before invoking the listener.
Any `KafkaTemplate` operations performed by the listener participate in the transaction.
If the listener successfully processes the record (or multiple records, when using a `BatchMessageListener`), the container sends the offset(s) to the transaction by using `producer.sendOffsetsToTransaction()`), before the transaction manager commits the transaction.
If the listener throws an exception, the transaction is rolled back and the consumer is repositioned so that the rolled-back record(s) can be retrieved on the next poll.
See [After-rollback Processor](#kafka-annotation-error-handling--after-rollback) for more information and for handling records that repeatedly fail.

Using transactions enables Exactly Once Semantics (EOS).

This means that, for a `read → process → write` sequence, it is guaranteed that the **sequence** is completed exactly once.
(The read and process have at least once semantics).

Spring for Apache Kafka version 3.0 and later only supports `EOSMode.V2`:

- `V2` - aka fetch-offset-request fencing (since version 2.5)

> [!IMPORTANT]
> This requires the brokers to be version 2.5 or later.

With mode `V2`, it is not necessary to have a producer for each `group.id/topic/partition` because consumer metadata is sent along with the offsets to the transaction and the broker can determine if the producer is fenced using that information instead.

Refer to [KIP-447](https://cwiki.apache.org/confluence/display/KAFKA/KIP-447%3A+Producer+scalability+for+exactly+once+semantics) for more information.

`V2` was previously `BETA`; the `EOSMode` has been changed to align the framework with [KIP-732](https://cwiki.apache.org/confluence/display/KAFKA/KIP-732%3A+Deprecate+eos-alpha+and+replace+eos-beta+with+eos-v2).

[Transactions](#kafka-transactions)
[Wiring Spring Beans into Producer/Consumer Interceptors](#kafka-interceptors)

---

<a id="kafka-interceptors"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/interceptors.html -->

<!-- page_index: 40 -->

# Wiring Spring Beans into Producer/Consumer Interceptors

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-interceptors--page-title"></a>
<a id="kafka-interceptors--wiring-spring-beans-into-producer-consumer-interceptors"></a>

# Wiring Spring Beans into Producer/Consumer Interceptors

Apache Kafka provides a mechanism to add interceptors to producers and consumers.
These objects are managed by Kafka, not Spring, and so normal Spring dependency injection won’t work for wiring in dependent Spring Beans.
However, you can manually wire in those dependencies using the interceptor `config()` method.
The following Spring Boot application shows how to do this by overriding Spring Boot’s default factories to add some dependent bean into the configuration properties.

```java
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public ConsumerFactory<?, ?> kafkaConsumerFactory(SomeBean someBean) {
        Map<String, Object> consumerProperties = new HashMap<>();
        // consumerProperties.put(..., ...)
        // ...
        consumerProperties.put(ConsumerConfig.INTERCEPTOR_CLASSES_CONFIG, MyConsumerInterceptor.class.getName());
        consumerProperties.put("some.bean", someBean);
        return new DefaultKafkaConsumerFactory<>(consumerProperties);
    }

    @Bean
    public ProducerFactory<?, ?> kafkaProducerFactory(SomeBean someBean) {
        Map<String, Object> producerProperties = new HashMap<>();
        // producerProperties.put(..., ...)
        // ...
        producerProperties.put(ProducerConfig.INTERCEPTOR_CLASSES_CONFIG, MyProducerInterceptor.class.getName());
        producerProperties.put("some.bean", someBean);
        return new DefaultKafkaProducerFactory<>(producerProperties);
    }

    @Bean
    public SomeBean someBean() {
        return new SomeBean();
    }

    @KafkaListener(id = "kgk897", topics = "kgh897")
    public void listen(String in) {
        System.out.println("Received " + in);
    }

    @Bean
    public ApplicationRunner runner(KafkaTemplate<String, String> template) {
        return args -> template.send("kgh897", "test");
    }

    @Bean
    public NewTopic kRequests() {
        return TopicBuilder.name("kgh897")
            .partitions(1)
            .replicas(1)
            .build();
    }

}
```

```java
public class SomeBean {

    public void someMethod(String what) {
        System.out.println(what + " in my foo bean");
    }

}
```

```java
public class MyProducerInterceptor implements ProducerInterceptor<String, String> {
private SomeBean bean;
@Override public void configure(Map<String, ?> configs) {this.bean = (SomeBean) configs.get("some.bean");}
@Override public ProducerRecord<String, String> onSend(ProducerRecord<String, String> record) {this.bean.someMethod("producer interceptor"); return record;}
@Override public void onAcknowledgement(RecordMetadata metadata, Exception exception) {}
@Override public void close() {}
}
```

```java
public class MyConsumerInterceptor implements ConsumerInterceptor<String, String> {
private SomeBean bean;
@Override public void configure(Map<String, ?> configs) {this.bean = (SomeBean) configs.get("some.bean");}
@Override public ConsumerRecords<String, String> onConsume(ConsumerRecords<String, String> records) {this.bean.someMethod("consumer interceptor"); return records;}
@Override public void onCommit(Map<TopicPartition, OffsetAndMetadata> offsets) {}
@Override public void close() {}
}
```

Result:

```none
producer interceptor in my foo bean
consumer interceptor in my foo bean
Received test
```

[Exactly Once Semantics](#kafka-exactly-once)
[Producer Interceptor Managed in Spring](#kafka-producer-interceptor-managed-in-spring)

---

<a id="kafka-producer-interceptor-managed-in-spring"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/producer-interceptor-managed-in-spring.html -->

<!-- page_index: 41 -->

# Producer Interceptor Managed in Spring

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-producer-interceptor-managed-in-spring--page-title"></a>
<a id="kafka-producer-interceptor-managed-in-spring--producer-interceptor-managed-in-spring"></a>

# Producer Interceptor Managed in Spring

Starting with version 3.0.0, when it comes to a producer interceptor, you can let Spring manage it directly as a bean instead of providing the class name of the interceptor to the Apache Kafka producer configuration.
If you go with this approach, then you need to set this producer interceptor on `KafkaTemplate`.
Following is an example using the same `MyProducerInterceptor` from above, but changed to not use the internal config property.

```java
public class MyProducerInterceptor implements ProducerInterceptor<String, String> {
private final SomeBean bean;
public MyProducerInterceptor(SomeBean bean) {this.bean = bean;}
@Override public void configure(Map<String, ?> configs) {}
@Override public ProducerRecord<String, String> onSend(ProducerRecord<String, String> record) {this.bean.someMethod("producer interceptor"); return record;}
@Override public void onAcknowledgement(RecordMetadata metadata, Exception exception) {}
@Override public void close() {}
}
```

```none
@Bean public MyProducerInterceptor myProducerInterceptor(SomeBean someBean) {return new MyProducerInterceptor(someBean);}
@Bean public KafkaTemplate<String, String> kafkaTemplate(ProducerFactory<String, String> pf, MyProducerInterceptor myProducerInterceptor) {KafkaTemplate<String, String> kafkaTemplate = new KafkaTemplate<>(pf); kafkaTemplate.setProducerInterceptor(myProducerInterceptor);}
```

Right before the records are sent, the `onSend` method of the producer interceptor is invoked.
Once the server sends an acknowledgement on publishing the data, then the `onAcknowledgement` method is invoked.
The `onAcknowledgement` is called right before the producer invokes any user callbacks.

If you have multiple such producer interceptors managed through Spring that need to be applied on the `KafkaTemplate`, you need to use `CompositeProducerInterceptor` instead.
`CompositeProducerInterceptor` allows individual producer interceptors to be added in order.
The methods from the underlying `ProducerInterceptor` implementations are invoked in the order as they were added to the `CompositeProducerInterceptor`.

[Wiring Spring Beans into Producer/Consumer Interceptors](#kafka-interceptors)
[Pausing and Resuming Listener Containers](#kafka-pause-resume)

---

<a id="kafka-pause-resume"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/pause-resume.html -->

<!-- page_index: 42 -->

# Pausing and Resuming Listener Containers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-pause-resume--page-title"></a>
<a id="kafka-pause-resume--pausing-and-resuming-listener-containers"></a>

# Pausing and Resuming Listener Containers

Version 2.1.3 added `pause()` and `resume()` methods to listener containers.
Previously, you could pause a consumer within a `ConsumerAwareMessageListener` and resume it by listening for a `ListenerContainerIdleEvent`, which provides access to the `Consumer` object.
While you could pause a consumer in an idle container by using an event listener, in some cases, this was not thread-safe, since there is no guarantee that the event listener is invoked on the consumer thread.
To safely pause and resume consumers, you should use the `pause` and `resume` methods on the listener containers.
A `pause()` takes effect just before the next `poll()`; a `resume()` takes effect just after the current `poll()` returns.
When a container is paused, it continues to `poll()` the consumer, avoiding a rebalance if group management is being used, but it does not retrieve any records.
See the Kafka documentation for more information.

Starting with version 2.1.5, you can call `isPauseRequested()` to see if `pause()` has been called.
However, the consumers might not have actually paused yet.
`isConsumerPaused()` returns true if all `Consumer` instances have actually paused.

In addition(also since 2.1.5), `ConsumerPausedEvent` and `ConsumerResumedEvent` instances are published with the container as the `source` property and the `TopicPartition` instances involved in the `partitions` property.

Starting with version 2.9, a new container property `pauseImmediate`, when set to true, causes the pause to take effect after the current record is processed.
By default, the pause takes effect when all the records from the previous poll have been processed.
See [pauseImmediate](#kafka-container-props--pauseimmediate).

The following simple Spring Boot application demonstrates by using the container registry to get a reference to a `@KafkaListener` method’s container and pausing or resuming its consumers as well as receiving the corresponding events:

```java
@SpringBootApplication
public class Application implements ApplicationListener<KafkaEvent> {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args).close();
    }

    @Override
    public void onApplicationEvent(KafkaEvent event) {
        System.out.println(event);
    }

    @Bean
    public ApplicationRunner runner(KafkaListenerEndpointRegistry registry,
            KafkaTemplate<String, String> template) {
        return args -> {
            template.send("pause.resume.topic", "thing1");
            Thread.sleep(10_000);
            System.out.println("pausing");
            registry.getListenerContainer("pause.resume").pause();
            Thread.sleep(10_000);
            template.send("pause.resume.topic", "thing2");
            Thread.sleep(10_000);
            System.out.println("resuming");
            registry.getListenerContainer("pause.resume").resume();
            Thread.sleep(10_000);
        };
    }

    @KafkaListener(id = "pause.resume", topics = "pause.resume.topic")
    public void listen(String in) {
        System.out.println(in);
    }

    @Bean
    public NewTopic topic() {
        return TopicBuilder.name("pause.resume.topic")
            .partitions(2)
            .replicas(1)
            .build();
    }

}
```

The following listing shows the results of the preceding example:

```none
partitions assigned: [pause.resume.topic-1, pause.resume.topic-0]
thing1
pausing
ConsumerPausedEvent [partitions=[pause.resume.topic-1, pause.resume.topic-0]]
resuming
ConsumerResumedEvent [partitions=[pause.resume.topic-1, pause.resume.topic-0]]
thing2
```

[Producer Interceptor Managed in Spring](#kafka-producer-interceptor-managed-in-spring)
[Pausing and Resuming Partitions on Listener Containers](#kafka-pause-resume-partitions)

---

<a id="kafka-pause-resume-partitions"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/pause-resume-partitions.html -->

<!-- page_index: 43 -->

# Pausing and Resuming Partitions on Listener Containers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-pause-resume-partitions--page-title"></a>
<a id="kafka-pause-resume-partitions--pausing-and-resuming-partitions-on-listener-containers"></a>

# Pausing and Resuming Partitions on Listener Containers

Since version 2.7 you can pause and resume the consumption of specific partitions assigned to that consumer by using the `pausePartition(TopicPartition topicPartition)` and `resumePartition(TopicPartition topicPartition)` methods in the listener containers.
The pausing and resuming take place respectively before and after the `poll()` similar to the `pause()` and `resume()` methods.
The `isPartitionPauseRequested()` method returns true if pause for that partition has been requested.
The `isPartitionPaused()` method returns true if that partition has effectively been paused.

Also since version 2.7 `ConsumerPartitionPausedEvent` and `ConsumerPartitionResumedEvent` instances are published with the container as the `source` property and the `TopicPartition` instance.

[Pausing and Resuming Listener Containers](#kafka-pause-resume)
[Serialization, Deserialization, and Message Conversion](#kafka-serdes)

---

<a id="kafka-serdes"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/serdes.html -->

<!-- page_index: 44 -->

# Serialization, Deserialization, and Message Conversion

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-serdes--page-title"></a>
<a id="kafka-serdes--serialization-deserialization-and-message-conversion"></a>

# Serialization, Deserialization, and Message Conversion

<a id="kafka-serdes--overview"></a>

## Overview

Apache Kafka provides a high-level API for serializing and deserializing record values as well as their keys.
It is present with the `org.apache.kafka.common.serialization.Serializer<T>` and
`org.apache.kafka.common.serialization.Deserializer<T>` abstractions with some built-in implementations.
Meanwhile, we can specify serializer and deserializer classes by using `Producer` or `Consumer` configuration properties.
The following example shows how to do so:

```java
props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, IntegerDeserializer.class);
props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
...
props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerSerializer.class);
props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
```

For more complex or particular cases, the `KafkaConsumer` (and, therefore, `KafkaProducer`) provides overloaded
constructors to accept `Serializer` and `Deserializer` instances for `keys` and `values`, respectively.

When you use this API, the `DefaultKafkaProducerFactory` and `DefaultKafkaConsumerFactory` also provide properties (through constructors or setter methods) to inject custom `Serializer` and `Deserializer` instances into the target `Producer` or `Consumer`.
Also, you can pass in `Supplier<Serializer>` or `Supplier<Deserializer>` instances through constructors - these `Supplier`s are called on creation of each `Producer` or `Consumer`.

<a id="kafka-serdes--string-serde"></a>
<a id="kafka-serdes--string-serialization"></a>

## String serialization

Since version 2.5, Spring for Apache Kafka provides `ToStringSerializer` and `ParseStringDeserializer` classes that use String representation of entities.
They rely on methods `toString` and some `Function<String>` or `BiFunction<String, Headers>` to parse the String and populate properties of an instance.
Usually, this would invoke some static method on the class, such as `parse`:

```java
ToStringSerializer<Thing> thingSerializer = new ToStringSerializer<>();
//...
ParseStringDeserializer<Thing> deserializer = new ParseStringDeserializer<>(Thing::parse);
```

By default, the `ToStringSerializer` is configured to convey type information about the serialized entity in the record `Headers`.
You can disable this by setting the `addTypeInfo` property to `false`.
This information can be used by `ParseStringDeserializer` on the receiving side.

- `ToStringSerializer.ADD_TYPE_INFO_HEADERS` (default `true`): You can set it to `false` to disable this feature on the `ToStringSerializer` (sets the `addTypeInfo` property).

```java
ParseStringDeserializer<Object> deserializer = new ParseStringDeserializer<>((str, headers) -> {byte[] header = headers.lastHeader(ToStringSerializer.VALUE_TYPE).value(); String entityType = new String(header);
if (entityType.contains("Thing")) {return Thing.parse(str);} else {// ...parsing logic} });
```

You can configure the `Charset` used to convert `String` to/from `byte[]` with the default being `UTF-8`.

You can configure the deserializer with the name of the parser method using `ConsumerConfig` properties:

- `ParseStringDeserializer.KEY_PARSER`
- `ParseStringDeserializer.VALUE_PARSER`

The properties must contain the fully qualified name of the class followed by the method name, separated by a period `.`.
The method must be static and have a signature of either `(String, Headers)` or `(String)`.

A `ToFromStringSerde` is also provided, for use with Kafka Streams.

<a id="kafka-serdes--json-serde"></a>
<a id="kafka-serdes--json"></a>

## JSON

Spring for Apache Kafka also provides `JacksonJsonSerializer` and `JacksonJsonDeserializer` implementations that are based on the
Jackson JSON object mapper.
The `JacksonJsonSerializer` allows writing any Java object as a JSON `byte[]`.
The `JacksonJsonDeserializer` requires an additional `Class<?> targetType` argument to allow the deserialization of a consumed `byte[]` to the proper target object.
The following example shows how to create a `JacksonJsonDeserializer`:

```java
JacksonJsonDeserializer<Thing> thingDeserializer = new JacksonJsonDeserializer<>(Thing.class);
```

You can customize both `JacksonJsonSerializer` and `JacksonJsonDeserializer` with an `ObjectMapper`.
You can also extend them to implement some particular configuration logic in the `configure(Map<String, ?> configs, boolean isKey)` method.

Starting with version 2.3, all the JSON-aware components are configured by default with a `JacksonUtils.enhancedObjectMapper()` instance, which comes with the `MapperFeature.DEFAULT_VIEW_INCLUSION` and `DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES` features disabled.
Also such an instance is supplied with well-known modules for custom data types, such a Java time and Kotlin support.
See `JacksonUtils.enhancedObjectMapper()` JavaDocs for more information.
This method also registers a `org.springframework.kafka.support.JacksonMimeTypeModule` for `org.springframework.util.MimeType` objects serialization into the plain string for inter-platform compatibility over the network.
A `JacksonMimeTypeModule` can be registered as a bean in the application context and it will be auto-configured into the [Spring Boot `ObjectMapper` instance](https://docs.spring.io/spring-boot/4.0/how-to/spring-mvc.html#howto.spring-mvc.customize-jackson-objectmapper).

Also starting with version 2.3, the `JsonDeserializer` provides `TypeReference`-based constructors for better handling of target generic container types.

Starting with version 2.1, you can convey type information in record `Headers`, allowing the handling of multiple types.
In addition, you can configure the serializer and deserializer by using the following Kafka properties.
They have no effect if you have provided `Serializer` and `Deserializer` instances for `KafkaConsumer` and `KafkaProducer`, respectively.

<a id="kafka-serdes--serdes-json-config"></a>
<a id="kafka-serdes--configuration-properties"></a>

### Configuration Properties

- `JacksonJsonSerializer.ADD_TYPE_INFO_HEADERS` (default `true`): You can set it to `false` to disable this feature on the `JacksonJsonSerializer` (sets the `addTypeInfo` property).
- `JacksonJsonSerializer.TYPE_MAPPINGS` (default `empty`): See [Mapping Types](#kafka-serdes--serdes-mapping-types).
- `JacksonJsonDeserializer.USE_TYPE_INFO_HEADERS` (default `true`): You can set it to `false` to ignore headers set by the serializer.
- `JacksonJsonDeserializer.REMOVE_TYPE_INFO_HEADERS` (default `true`): You can set it to `false` to retain headers set by the serializer.
- `JacksonJsonDeserializer.KEY_DEFAULT_TYPE`: Fallback type for deserialization of keys if no header information is present.
- `JacksonJsonDeserializer.VALUE_DEFAULT_TYPE`: Fallback type for deserialization of values if no header information is present.
- `JacksonJsonDeserializer.TRUSTED_PACKAGES` (default `java.util`, `java.lang`): Comma-delimited list of package patterns allowed for deserialization.
  `*` means deserializing all.
- `JacksonJsonDeserializer.TYPE_MAPPINGS` (default `empty`): See [Mapping Types](#kafka-serdes--serdes-mapping-types).
- `JacksonJsonDeserializer.KEY_TYPE_METHOD` (default `empty`): See [Using Methods to Determine Types](#kafka-serdes--serdes-type-methods).
- `JacksonJsonDeserializer.VALUE_TYPE_METHOD` (default `empty`): See [Using Methods to Determine Types](#kafka-serdes--serdes-type-methods).

Starting with version 2.2, the type information headers (if added by the serializer) are removed by the deserializer.
You can revert to the previous behavior by setting the `removeTypeHeaders` property to `false`, either directly on the deserializer or with the configuration property described earlier.

See also [Customizing the JacksonJsonSerializer and JacksonJsonDeserializer](#tips--tip-json).

> [!IMPORTANT]
> Starting with version 2.8, if you construct the serializer or deserializer programmatically as shown in [Programmatic Construction](#kafka-serdes--prog-json), the above properties will be applied by the factories, as long as you have not set any properties explicitly (using `set*()` methods or using the fluent API).
> Previously, when creating programmatically, the configuration properties were never applied; this is still the case if you explicitly set properties on the object directly.

<a id="kafka-serdes--serdes-mapping-types"></a>
<a id="kafka-serdes--mapping-types"></a>

### Mapping Types

Starting with version 2.2, when using JSON, you can now provide type mappings by using the properties in the preceding list.
Previously, you had to customize the type mapper within the serializer and deserializer.
Mappings consist of a comma-delimited list of `token:className` pairs.
On outbound, the payload’s class name is mapped to the corresponding token.
On inbound, the token in the type header is mapped to the corresponding class name.

The following example creates a set of mappings:

```java
senderProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
senderProps.put(JsonSerializer.TYPE_MAPPINGS, "cat:com.mycat.Cat, hat:com.myhat.Hat");
...
consumerProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, JsonDeserializer.class);
consumerProps.put(JsonDeserializer.TYPE_MAPPINGS, "cat:com.yourcat.Cat, hat:com.yourhat.Hat");
```

> [!IMPORTANT]
> The corresponding objects must be compatible.

If you use [Spring Boot](https://docs.spring.io/spring-boot/4.0/reference/messaging/kafka.html), you can provide these properties in the `application.properties` (or yaml) file.
The following example shows how to do so:

```none
spring.kafka.producer.value-serializer=org.springframework.kafka.support.serializer.JsonSerializer
spring.kafka.producer.properties.spring.json.type.mapping=cat:com.mycat.Cat,hat:com.myhat.Hat
```

> [!IMPORTANT]
> You can perform only simple configuration with properties.
> For more advanced configuration (such as using a custom `ObjectMapper` in the serializer and deserializer), you should use the producer and consumer factory constructors that accept a pre-built serializer and deserializer.
> The following Spring Boot example overrides the default factories:
>
> ```java
> @Bean
> public ConsumerFactory<?, ?> kafkaConsumerFactory(JsonDeserializer customValueDeserializer) {
>     Map<String, Object> properties = new HashMap<>();
>     // properties.put(..., ...)
>     // ...
>     return new DefaultKafkaConsumerFactory<>(properties,
>         new StringDeserializer(), customValueDeserializer);
> }
>
> @Bean
> public ProducerFactory<?, ?> kafkaProducerFactory(JsonSerializer customValueSerializer) {
>     return new DefaultKafkaProducerFactory<>(properties.buildProducerProperties(),
>         new StringSerializer(), customValueSerializer);
> }
> ```
>
> Setters are also provided, as an alternative to using these constructors.

> [!NOTE]
> When using Spring Boot and overriding the `ConsumerFactory` and `ProducerFactory` as shown above, wild card generic types need to be used with the bean method return type.
> If concrete generic types are provided instead, then Spring Boot will ignore these beans and still use the default ones.

Starting with version 2.2, you can explicitly configure the deserializer to use the supplied target type and ignore type information in headers by using one of the overloaded constructors that have a boolean `useHeadersIfPresent` argument (which is `true` by default).
The following example shows how to do so:

```java
DefaultKafkaConsumerFactory<Integer, Cat1> cf = new DefaultKafkaConsumerFactory<>(props,
        new IntegerDeserializer(), new JacksonJsonDeserializer<>(Cat1.class, false));
```

<a id="kafka-serdes--serdes-type-methods"></a>
<a id="kafka-serdes--using-methods-to-determine-types"></a>

### Using Methods to Determine Types

Starting with version 2.5, you can now configure the deserializer, via properties, to invoke a method to determine the target type.
If present, this will override any of the other techniques discussed above.
This can be useful if the data is published by an application that does not use the Spring serializer and you need to deserialize to different types depending on the data, or other headers.
Set these properties to the method name - a fully qualified class name followed by the method name, separated by a period `.`.
The method must be declared as `public static`, have one of three signatures `(String topic, byte[] data, Headers headers)`, `(byte[] data, Headers headers)` or `(byte[] data)` and return a Jackson `JavaType`.

- `JsonDeserializer.KEY_TYPE_METHOD` : `spring.json.key.type.method`
- `JsonDeserializer.VALUE_TYPE_METHOD` : `spring.json.value.type.method`

You can use arbitrary headers or inspect the data to determine the type.

```java
JavaType thing1Type = TypeFactory.defaultInstance().constructType(Thing1.class);
JavaType thing2Type = TypeFactory.defaultInstance().constructType(Thing2.class);
public static JavaType thingOneOrThingTwo(byte[] data, Headers headers) {// {"thisIsAFieldInThing1":"value", ...if (data[21] == '1') {return thing1Type;} else {return thing2Type;}}
```

For more sophisticated data inspection consider using `JsonPath` or similar but, the simpler the test to determine the type, the more efficient the process will be.

The following is an example of creating the deserializer programmatically (when providing the consumer factory with the deserializer in the constructor):

```java
JacksonJsonDeserializer<Object> deser = new JacksonJsonDeserializer<>() .trustedPackages("*") .typeResolver(SomeClass::thing1Thing2JavaTypeForTopic);
...
public static JavaType thing1Thing2JavaTypeForTopic(String topic, byte[] data, Headers headers) {...}
```

<a id="kafka-serdes--prog-json"></a>
<a id="kafka-serdes--programmatic-construction"></a>

### Programmatic Construction

When constructing the serializer/deserializer programmatically for use in the producer/consumer factory, since version 2.3, you can use the fluent API, which simplifies configuration.

```java
@Bean
public ProducerFactory<MyKeyType, MyValueType> pf() {
    Map<String, Object> props = new HashMap<>();
    // props.put(..., ...)
    // ...
    DefaultKafkaProducerFactory<MyKeyType, MyValueType> pf = new DefaultKafkaProducerFactory<>(props,
        new JacksonJsonSerializer<MyKeyType>()
            .forKeys()
            .noTypeInfo(),
        new JacksonJsonSerializer<MyValueType>()
            .noTypeInfo());
    return pf;
}

@Bean
public ConsumerFactory<MyKeyType, MyValueType> cf() {
    Map<String, Object> props = new HashMap<>();
    // props.put(..., ...)
    // ...
    DefaultKafkaConsumerFactory<MyKeyType, MyValueType> cf = new DefaultKafkaConsumerFactory<>(props,
        new JacksonJsonDeserializer<>(MyKeyType.class)
            .forKeys()
            .ignoreTypeHeaders(),
        new JacksonJsonDeserializer<>(MyValueType.class)
            .ignoreTypeHeaders());
    return cf;
}
```

To provide type mapping programmatically, similar to [Using Methods to Determine Types](#kafka-serdes--serdes-type-methods), use the `typeFunction` property.

```java
JacksonJsonDeserializer<Object> deser = new JacksonJsonDeserializer<>()
        .trustedPackages("*")
        .typeFunction(MyUtils::thingOneOrThingTwo);
```

Alternatively, as long as you don’t use the fluent API to configure properties, or set them using `set*()` methods, the factories will configure the serializer/deserializer using the configuration properties; see [Configuration Properties](#kafka-serdes--serdes-json-config).

<a id="kafka-serdes--delegating-serialization"></a>
<a id="kafka-serdes--delegating-serializer-and-deserializer"></a>

## Delegating Serializer and Deserializer

<a id="kafka-serdes--using-headers"></a>

### Using Headers

Version 2.3 introduced the `DelegatingSerializer` and `DelegatingDeserializer`, which allow producing and consuming records with different key and/or value types.
Producers must set a header `DelegatingSerializer.VALUE_SERIALIZATION_SELECTOR` to a selector value that is used to select which serializer to use for the value and `DelegatingSerializer.KEY_SERIALIZATION_SELECTOR` for the key; if a match is not found, an `IllegalStateException` is thrown.

For incoming records, the deserializer uses the same headers to select the deserializer to use; if a match is not found or the header is not present, the raw `byte[]` is returned.

You can configure the map of selector to `Serializer` / `Deserializer` via a constructor, or you can configure it via Kafka producer/consumer properties with the keys `DelegatingSerializer.VALUE_SERIALIZATION_SELECTOR_CONFIG` and `DelegatingSerializer.KEY_SERIALIZATION_SELECTOR_CONFIG`.
For the serializer, the producer property can be a `Map<String, Object>` where the key is the selector and the value is a `Serializer` instance, a serializer `Class` or the class name.
The property can also be a String of comma-delimited map entries, as shown below.

For the deserializer, the consumer property can be a `Map<String, Object>` where the key is the selector and the value is a `Deserializer` instance, a deserializer `Class` or the class name.
The property can also be a String of comma-delimited map entries, as shown below.

To configure using properties, use the following syntax:

```java
producerProps.put(DelegatingSerializer.VALUE_SERIALIZATION_SELECTOR_CONFIG,
    "thing1:com.example.MyThing1Serializer, thing2:com.example.MyThing2Serializer")

consumerProps.put(DelegatingDeserializer.VALUE_SERIALIZATION_SELECTOR_CONFIG,
    "thing1:com.example.MyThing1Deserializer, thing2:com.example.MyThing2Deserializer")
```

Producers would then set the `DelegatingSerializer.VALUE_SERIALIZATION_SELECTOR` header to `thing1` or `thing2`.

This technique supports sending different types to the same topic (or different topics).

> [!NOTE]
> Starting with version 2.5.1, it is not necessary to set the selector header, if the type (key or value) is one of the standard types supported by `Serdes` (`Long`, `Integer`, etc).
> Instead, the serializer will set the header to the class name of the type.
> It is not necessary to configure serializers or deserializers for these types, they will be created (once) dynamically.

For another technique to send different types to different topics, see [Using `RoutingKafkaTemplate`](#kafka-sending-messages--routing-template).

<a id="kafka-serdes--by-type"></a>

### By Type

Version 2.8 introduced the `DelegatingByTypeSerializer`.

```java
@Bean
public ProducerFactory<Integer, Object> producerFactory(Map<String, Object> config) {
    return new DefaultKafkaProducerFactory<>(config,
            null, new DelegatingByTypeSerializer(Map.of(
                    byte[].class, new ByteArraySerializer(),
                    Bytes.class, new BytesSerializer(),
                    String.class, new StringSerializer())));
}
```

Starting with version 2.8.3, you can configure the serializer to check if the map key is assignable from the target object, useful when a delegate serializer can serialize sub classes.
In this case, if there are ambiguous matches, an ordered `Map`, such as a `LinkedHashMap` should be provided.

<a id="kafka-serdes--by-topic"></a>

### By Topic

Starting with version 2.8, the `DelegatingByTopicSerializer` and `DelegatingByTopicDeserializer` allow selection of a serializer/deserializer based on the topic name.
Regex `Pattern`s are used to lookup the instance to use.
The map can be configured using a constructor, or via properties (a comma delimited list of `pattern:serializer`).

```java
producerConfigs.put(DelegatingByTopicSerializer.VALUE_SERIALIZATION_TOPIC_CONFIG,
            "topic[0-4]:" + ByteArraySerializer.class.getName()
        + ", topic[5-9]:" + StringSerializer.class.getName());
...
consumerConfigs.put(DelegatingByTopicDeserializer.VALUE_SERIALIZATION_TOPIC_CONFIG,
            "topic[0-4]:" + ByteArrayDeserializer.class.getName()
        + ", topic[5-9]:" + StringDeserializer.class.getName());
```

Use `KEY_SERIALIZATION_TOPIC_CONFIG` when using this for keys.

```java
@Bean
public ProducerFactory<Integer, Object> producerFactory(Map<String, Object> config) {
    return new DefaultKafkaProducerFactory<>(config,
            new IntegerSerializer(),
            new DelegatingByTopicSerializer(Map.of(
                    Pattern.compile("topic[0-4]"), new ByteArraySerializer(),
                    Pattern.compile("topic[5-9]"), new StringSerializer())),
                    new JacksonJsonSerializer<Object>());  // default
}
```

You can specify a default serializer/deserializer to use when there is no pattern match using `DelegatingByTopicSerialization.KEY_SERIALIZATION_TOPIC_DEFAULT` and `DelegatingByTopicSerialization.VALUE_SERIALIZATION_TOPIC_DEFAULT`.

An additional property `DelegatingByTopicSerialization.CASE_SENSITIVE` (default `true`), when set to `false` makes the topic lookup case insensitive.

<a id="kafka-serdes--retrying-deserialization"></a>
<a id="kafka-serdes--retrying-deserializer"></a>

## Retrying Deserializer

The `RetryingDeserializer` uses a delegate `Deserializer` and `RetryTemplate` to retry deserialization when the delegate might have transient errors, such as network issues, during deserialization.

```java
ConsumerFactory cf = new DefaultKafkaConsumerFactory(myConsumerConfigs,
    new RetryingDeserializer(myUnreliableKeyDeserializer, retryTemplate),
    new RetryingDeserializer(myUnreliableValueDeserializer, retryTemplate));
```

A recovery callback be set on the `RetryingDeserializer`, to return a fallback object if all retries are exhausted.

Refer to the [Spring Framework](https://github.com/spring-projects/spring-framework) project for configuration of the `RetryTemplate` with a retry policy, back off, etc.

<a id="kafka-serdes--messaging-message-conversion"></a>
<a id="kafka-serdes--spring-messaging-message-conversion"></a>

## Spring Messaging Message Conversion

Although the `Serializer` and `Deserializer` API is quite simple and flexible from the low-level Kafka `Consumer` and `Producer` perspective, you might need more flexibility at the Spring Messaging level, when using either `@KafkaListener` or [Spring Integration’s Apache Kafka Support](https://docs.spring.io/spring-integration/reference/kafka.html).
To let you easily convert to and from `org.springframework.messaging.Message`, Spring for Apache Kafka provides a `MessageConverter` abstraction with the `MessagingMessageConverter` implementation and its `JacksonJsonMessageConverter` (and subclasses) customization.
You can inject the `MessageConverter` into a `KafkaTemplate` instance directly and by using `AbstractKafkaListenerContainerFactory` bean definition for the `@KafkaListener.containerFactory()` property.
The following example shows how to do so:

```java
@Bean public KafkaListenerContainerFactory<?> kafkaJsonListenerContainerFactory() {ConcurrentKafkaListenerContainerFactory<Integer, String> factory =new ConcurrentKafkaListenerContainerFactory<>(); factory.setConsumerFactory(consumerFactory()); factory.setRecordMessageConverter(new JacksonJsonMessageConverter()); return factory;} ...@KafkaListener(topics = "jsonData",containerFactory = "kafkaJsonListenerContainerFactory") public void jsonListener(Cat cat) {...}
```

When using Spring Boot, simply define the converter as a `@Bean` and Spring Boot auto configuration will wire it into the auto-configured template and container factory.

When you use a `@KafkaListener`, the parameter type is provided to the message converter to assist with the conversion.

> [!NOTE]
> This type inference can be achieved only when the `@KafkaListener` annotation is declared at the method level.
> With a class-level `@KafkaListener`, the payload type is used to select which `@KafkaHandler` method to invoke, so it must already have been converted before the method can be chosen.

> [!NOTE]
> On the consumer side, you can configure a `JacksonJsonMessageConverter`; it can handle `ConsumerRecord` values of type `byte[]`, `Bytes` and `String` so should be used in conjunction with a `ByteArrayDeserializer`, `BytesDeserializer` or `StringDeserializer`.
> (`byte[]` and `Bytes` are more efficient because they avoid an unnecessary `byte[]` to `String` conversion).
> You can also configure the specific subclass of `JacksonJsonMessageConverter` corresponding to the deserializer, if you so wish.
>
> On the producer side, when you use Spring Integration or the `KafkaTemplate.send(Message<?> message)` method (see [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template)), you must configure a message converter that is compatible with the configured Kafka `Serializer`.
>
> - `StringJacksonJsonMessageConverter` with `StringSerializer`
> - `BytesJacksonJsonMessageConverter` with `BytesSerializer`
> - `ByteArrayJacksonJsonMessageConverter` with `ByteArraySerializer`
>
> Again, using `byte[]` or `Bytes` is more efficient because they avoid a `String` to `byte[]` conversion.
>
> For convenience, starting with version 2.3, the framework also provides a `StringOrBytesSerializer` which can serialize all three value types so it can be used with any of the message converters.

Starting with version 2.7.1, message payload conversion can be delegated to a `spring-messaging` `SmartMessageConverter`; this enables conversion, for example, to be based on the `MessageHeaders.CONTENT_TYPE` header.

> [!IMPORTANT]
> The `KafkaMessageConverter.fromMessage()` method is called for outbound conversion to a `ProducerRecord` with the message payload in the `ProducerRecord.value()` property.
> The `KafkaMessageConverter.toMessage()` method is called for inbound conversion from `ConsumerRecord` with the payload being the `ConsumerRecord.value()` property.
> The `SmartMessageConverter.toMessage()` method is called to create a new outbound `Message<?>` from the `Message` passed to `fromMessage()` (usually by `KafkaTemplate.send(Message<?> msg)`).
> Similarly, in the `KafkaMessageConverter.toMessage()` method, after the converter has created a new `Message<?>` from the `ConsumerRecord`, the `SmartMessageConverter.fromMessage()` method is called and then the final inbound message is created with the newly converted payload.
> In either case, if the `SmartMessageConverter` returns `null`, the original message is used.

When the default converter is used in the `KafkaTemplate` and listener container factory, you configure the `SmartMessageConverter` by calling `setMessagingConverter()` on the template and via the `contentTypeConverter` property on `@KafkaListener` methods.

Examples:

```java
template.setMessagingConverter(mySmartConverter);
```

```java
@KafkaListener(id = "withSmartConverter", topics = "someTopic",
    contentTypeConverter = "mySmartConverter")
public void smart(Thing thing) {
    ...
}
```

<a id="kafka-serdes--data-projection"></a>
<a id="kafka-serdes--using-spring-data-projection-interfaces"></a>

### Using Spring Data Projection Interfaces

Starting with version 2.1.1, you can convert JSON to a Spring Data Projection interface instead of a concrete type.
This allows very selective, and low-coupled bindings to data, including the lookup of values from multiple places inside the JSON document.
For example the following interface can be defined as message payload type:

```java
interface SomeSample {

  @JsonPath({ "$.username", "$.user.name" })
  String getUsername();

}
```

```java
@KafkaListener(id="projection.listener", topics = "projection")
public void projection(SomeSample in) {
    String username = in.getUsername();
    ...
}
```

Accessor methods will be used to lookup the property name as field in the received JSON document by default.
The `@JsonPath` expression allows customization of the value lookup, and even to define multiple JSON Path expressions, to look up values from multiple places until an expression returns an actual value.

To enable this feature, use a `JacksonProjectingMessageConverter` configured with an appropriate delegate converter (used for outbound conversion and converting non-projection interfaces).
You must also add `spring-data:spring-data-commons` and `com.jayway.jsonpath:json-path` to the classpath.

When used as the parameter to a `@KafkaListener` method, the interface type is automatically passed to the converter as normal.

<a id="kafka-serdes--error-handling-deserializer"></a>
<a id="kafka-serdes--using-errorhandlingdeserializer"></a>

## Using `ErrorHandlingDeserializer`

When a deserializer fails to deserialize a message, Spring has no way to handle the problem, because it occurs before the `poll()` returns.
To solve this problem, the `ErrorHandlingDeserializer` has been introduced.
This deserializer delegates to a real deserializer (key or value).
If the delegate fails to deserialize the record content, the `ErrorHandlingDeserializer` returns a `null` value and a `DeserializationException` in a header that contains the cause and the raw bytes.
When you use a record-level `MessageListener`, if the `ConsumerRecord` contains a `DeserializationException` header for either the key or value, the container’s `ErrorHandler` is called with the failed `ConsumerRecord`.
The record is not passed to the listener.

Alternatively, you can configure the `ErrorHandlingDeserializer` to create a custom value by providing a `failedDeserializationFunction`, which is a `Function<FailedDeserializationInfo, T>`.
This function is invoked to create an instance of `T`, which is passed to the listener in the usual fashion.
An object of type `FailedDeserializationInfo`, which contains all the contextual information is provided to the function.
You can find the `DeserializationException` (as a serialized Java object) in headers.
See the [Javadoc](https://docs.spring.io/spring-kafka/docs/4.1.0/api/org/springframework/kafka/support/serializer/ErrorHandlingDeserializer.html) for the `ErrorHandlingDeserializer` for more information.

You can use the `DefaultKafkaConsumerFactory` constructor that takes key and value `Deserializer` objects and wire in appropriate `ErrorHandlingDeserializer` instances that you have configured with the proper delegates.
Alternatively, you can use consumer configuration properties (which are used by the `ErrorHandlingDeserializer`) to instantiate the delegates.
The property names are `ErrorHandlingDeserializer.KEY_DESERIALIZER_CLASS` and `ErrorHandlingDeserializer.VALUE_DESERIALIZER_CLASS`.
The property value can be a class or class name.
The following example shows how to set these properties:

```java
... // other props
props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ErrorHandlingDeserializer.class);
props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, ErrorHandlingDeserializer.class);
props.put(ErrorHandlingDeserializer.KEY_DESERIALIZER_CLASS, JsonDeserializer.class);
props.put(JsonDeserializer.KEY_DEFAULT_TYPE, "com.example.MyKey")
props.put(ErrorHandlingDeserializer.VALUE_DESERIALIZER_CLASS, JsonDeserializer.class.getName());
props.put(JsonDeserializer.VALUE_DEFAULT_TYPE, "com.example.MyValue")
props.put(JsonDeserializer.TRUSTED_PACKAGES, "com.example")
return new DefaultKafkaConsumerFactory<>(props);
```

The following example uses a `failedDeserializationFunction`.

```java
public class BadThing extends Thing {
private final FailedDeserializationInfo failedDeserializationInfo;
public BadThing(FailedDeserializationInfo failedDeserializationInfo) {this.failedDeserializationInfo = failedDeserializationInfo;}
public FailedDeserializationInfo getFailedDeserializationInfo() {return this.failedDeserializationInfo;}
}
public class FailedThingProvider implements Function<FailedDeserializationInfo, Thing> {
@Override public Thing apply(FailedDeserializationInfo info) {return new BadThing(info);}
}
```

The preceding example uses the following configuration:

```java
...
consumerProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ErrorHandlingDeserializer.class);
consumerProps.put(ErrorHandlingDeserializer.VALUE_DESERIALIZER_CLASS, JsonDeserializer.class);
consumerProps.put(ErrorHandlingDeserializer.VALUE_FUNCTION, FailedThingProvider.class);
...
```

> [!IMPORTANT]
> If the consumer is configured with an `ErrorHandlingDeserializer`, it is important to configure the `KafkaTemplate` and its producer with a serializer that can handle normal objects as well as raw `byte[]` values, which result from deserialization exceptions.
> The generic value type of the template should be `Object`.
> One technique is to use the `DelegatingByTypeSerializer`; an example follows:

```java
@Bean
public ProducerFactory<String, Object> producerFactory() {
  return new DefaultKafkaProducerFactory<>(producerConfiguration(), new StringSerializer(),
    new DelegatingByTypeSerializer(Map.of(byte[].class, new ByteArraySerializer(),
          MyNormalObject.class, new JacksonJsonSerializer<Object>())));
}

@Bean
public KafkaTemplate<String, Object> kafkaTemplate() {
  return new KafkaTemplate<>(producerFactory());
}
```

When using an `ErrorHandlingDeserializer` with a batch listener, you must check for the deserialization exceptions in message headers.
When used with a `DefaultBatchErrorHandler`, you can use that header to determine which record the exception failed on and communicate to the error handler via a `BatchListenerFailedException`.

```java
@KafkaListener(id = "test", topics = "test") void listen(List<Thing> in, @Header(KafkaHeaders.BATCH_CONVERTED_HEADERS) List<Map<String, Object>> headers) {for (int i = 0; i < in.size(); i++) {Thing thing = in.get(i); if (thing == null && headers.get(i).get(SerializationUtils.VALUE_DESERIALIZER_EXCEPTION_HEADER) != null) {try {DeserializationException deserEx = SerializationUtils.byteArrayToDeserializationException(this.logger,headers.get(i).get(SerializationUtils.VALUE_DESERIALIZER_EXCEPTION_HEADER)); if (deserEx != null) {logger.error(deserEx, "Record at index " + i + " could not be deserialized");}} catch (Exception ex) {logger.error(ex, "Record at index " + i + " could not be deserialized");} throw new BatchListenerFailedException("Deserialization", deserEx, i);} process(thing);}}
```

`SerializationUtils.byteArrayToDeserializationException()` can be used to convert the header to a `DeserializationException`.

When consuming `List<ConsumerRecord<?, ?>`, `SerializationUtils.getExceptionFromHeader()` is used instead:

```java
@KafkaListener(id = "kgh2036", topics = "kgh2036") void listen(List<ConsumerRecord<String, Thing>> in) {for (int i = 0; i < in.size(); i++) {ConsumerRecord<String, Thing> rec = in.get(i); if (rec.value() == null) {DeserializationException deserEx = SerializationUtils.getExceptionFromHeader(rec,SerializationUtils.VALUE_DESERIALIZER_EXCEPTION_HEADER, this.logger); if (deserEx != null) {logger.error(deserEx, "Record at offset " + rec.offset() + " could not be deserialized"); throw new BatchListenerFailedException("Deserialization", deserEx, i);}} process(rec.value());}}
```

> [!IMPORTANT]
> If you are also using a `DeadLetterPublishingRecoverer`, the record published for a `DeserializationException` will have a `record.value()` of type `byte[]`; this should not be serialized.
> Consider using a `DelegatingByTypeSerializer` configured to use a `ByteArraySerializer` for `byte[]` and the normal serializer (Json, Avro, etc) for all other types.

Starting with version 3.1, you can add a `Validator` to the `ErrorHandlingDeserializer`.
If the delegate `Deserializer` successfully deserializes the object, but that object fails validation, an exception is thrown similar to a deserialization exception occurring.
This allows the original raw data to be passed to the error handler.
When creating the deserializer yourself, simply call `setValidator`; if you configure the serializer using properties, set the consumer configuration property `ErrorHandlingDeserializer.VALIDATOR_CLASS` to the class or fully qualified class name for your `Validator`.
When using Spring Boot, this property name is `spring.kafka.consumer.properties.spring.deserializer.validator.class`.

<a id="kafka-serdes--payload-conversion-with-batch"></a>
<a id="kafka-serdes--payload-conversion-with-batch-listeners"></a>

## Payload Conversion with Batch Listeners

You can also use a `JacksonJsonMessageConverter` within a `BatchMessagingMessageConverter` to convert batch messages when you use a batch listener container factory.
See [Serialization, Deserialization, and Message Conversion](#kafka-serdes) and [Spring Messaging Message Conversion](#kafka-serdes--messaging-message-conversion) for more information.

By default, the type for the conversion is inferred from the listener argument.
If you configure the `JacksonJsonMessageConverter` with a `DefaultJackson2TypeMapper` that has its `TypePrecedence` set to `TYPE_ID` (instead of the default `INFERRED`), the converter uses the type information in headers (if present) instead.
This allows, for example, listener methods to be declared with interfaces instead of concrete classes.
Also, the type converter supports mapping, so the deserialization can be to a different type than the source (as long as the data is compatible).
This is also useful when you use [class-level `@KafkaListener` instances](#kafka-receiving-messages-class-level-kafkalistener) where the payload must have already been converted to determine which method to invoke.
The following example creates beans that use this method:

```java
@Bean
public KafkaListenerContainerFactory<?> kafkaListenerContainerFactory() {
    ConcurrentKafkaListenerContainerFactory<Integer, String> factory =
            new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.setBatchListener(true);
    factory.setBatchMessageConverter(new BatchMessagingMessageConverter(converter()));
    return factory;
}

@Bean
public JacksonJsonMessageConverter converter() {
    return new JacksonJsonMessageConverter();
}
```

Note that, for this to work, the method signature for the conversion target must be a container object with a single generic parameter type, such as the following:

```java
@KafkaListener(topics = "blc1")
public void listen(List<Foo> foos, @Header(KafkaHeaders.OFFSET) List<Long> offsets) {
    ...
}
```

Note that you can still access the batch headers.

If the batch converter has a record converter that supports it, you can also receive a list of messages where the payloads are converted according to the generic type.
The following example shows how to do so:

```java
@KafkaListener(topics = "blc3", groupId = "blc3")
public void listen(List<Message<Foo>> fooMessages) {
    ...
}
```

If record in the batch cannot be converted, its payload is set as `null` into the target `payloads` list.
The conversion exception is logged as warning for this record and also stored into a `KafkaHeaders.CONVERSION_FAILURES` header as an item of the `List<ConversionException>`.
The target `@KafkaListener` method may perform Java `Stream` API to filter out those `null` values from the payload list or do something with the conversion exceptions header:

```java
@KafkaListener(id = "foo", topics = "foo", autoStartup = "false") public void listen(List<Foo> list,@Header(KafkaHeaders.CONVERSION_FAILURES) List<ConversionException> conversionFailures) {
for (int i = 0; i < list.size(); i++) {if (conversionFailures.get(i) != null) {throw new BatchListenerFailedException("Conversion Failed", conversionFailures.get(i), i);}}}
```

<a id="kafka-serdes--conversionservice-customization"></a>

## `ConversionService` Customization

Starting with version 2.1.1, the `org.springframework.core.convert.ConversionService` used by the default `org.springframework.messaging.handler.annotation.support.MessageHandlerMethodFactory` to resolve parameters for the invocation of a listener method is supplied with all beans that implement any of the following interfaces:

- `org.springframework.core.convert.converter.Converter`
- `org.springframework.core.convert.converter.GenericConverter`
- `org.springframework.format.Formatter`

This lets you further customize listener deserialization without changing the default configuration for `ConsumerFactory` and `KafkaListenerContainerFactory`.

> [!IMPORTANT]
> Setting a custom `MessageHandlerMethodFactory` on the `KafkaListenerEndpointRegistrar` through a `KafkaListenerConfigurer` bean disables this feature.

<a id="kafka-serdes--custom-arg-resolve"></a>
<a id="kafka-serdes--adding-custom-handlermethodargumentresolver-to-kafkalistener"></a>

## Adding Custom `HandlerMethodArgumentResolver` to `@KafkaListener`

Starting with version 2.4.2 you are able to add your own `HandlerMethodArgumentResolver` and resolve custom method parameters.
All you need is to implement `KafkaListenerConfigurer` and use method `setCustomMethodArgumentResolvers()` from class `KafkaListenerEndpointRegistrar`.

```java
@Configuration class CustomKafkaConfig implements KafkaListenerConfigurer {
@Override public void configureKafkaListeners(KafkaListenerEndpointRegistrar registrar) {registrar.setCustomMethodArgumentResolvers(new HandlerMethodArgumentResolver() {
@Override public boolean supportsParameter(MethodParameter parameter) {return CustomMethodArgument.class.isAssignableFrom(parameter.getParameterType());}
@Override public Object resolveArgument(MethodParameter parameter, Message<?> message) {return new CustomMethodArgument(message.getHeaders().get(KafkaHeaders.RECEIVED_TOPIC, String.class) );}} );}
}
```

You can also completely replace the framework’s argument resolution by adding a custom `MessageHandlerMethodFactory` to the `KafkaListenerEndpointRegistrar` bean.
If you do this, and your application needs to handle tombstone records, with a `null` `value()` (e.g. from a compacted topic), you should add a `KafkaNullAwarePayloadArgumentResolver` to the factory; it must be the last resolver because it supports all types and can match arguments without a `@Payload` annotation.
If you are using a `DefaultMessageHandlerMethodFactory`, set this resolver as the last custom resolver; the factory will ensure that this resolver will be used before the standard `PayloadMethodArgumentResolver`, which has no knowledge of `KafkaNull` payloads.

See also [Null Payloads and Log Compaction of `Tombstone` Records](#kafka-tombstones).

[Pausing and Resuming Partitions on Listener Containers](#kafka-pause-resume-partitions)
[Message Headers](#kafka-headers)

---

<a id="kafka-headers"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/headers.html -->

<!-- page_index: 45 -->

# Message Headers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-headers--page-title"></a>
<a id="kafka-headers--message-headers"></a>

# Message Headers

The 0.11.0.0 client introduced support for headers in messages.
As of version 2.0, Spring for Apache Kafka now supports mapping these headers to and from `spring-messaging` `MessageHeaders`.

> [!NOTE]
> Previous versions mapped `ConsumerRecord` and `ProducerRecord` to spring-messaging `Message<?>`, where the value property is mapped to and from the `payload` and other properties (`topic`, `partition`, and so on) were mapped to headers.
> This is still the case, but additional (arbitrary) headers can now be mapped.

Apache Kafka headers have a simple API, shown in the following interface definition:

```java
public interface Header {

    String key();

    byte[] value();

}
```

The `KafkaHeaderMapper` strategy is provided to map header entries between Kafka `Headers` and `MessageHeaders`.
Its interface definition is as follows:

```java
public interface KafkaHeaderMapper {

    void fromHeaders(MessageHeaders headers, Headers target);

    void toHeaders(Headers source, Map<String, Object> target);

}
```

The `SimpleKafkaHeaderMapper` maps raw headers as `byte[]`, with configuration options for conversion to `String` values.

The `JsonKafkaHeaderMapper` maps the key to the `MessageHeaders` header name and, in order to support rich header types for outbound messages, JSON conversion is performed.
A "`special`" header (with a key of `spring_json_header_types`) contains a JSON map of `<key>:<type>`.
This header is used on the inbound side to provide appropriate conversion of each header value to the original type.

On the inbound side, all Kafka `Header` instances are mapped to `MessageHeaders`.
On the outbound side, by default, all `MessageHeaders` are mapped, except `id`, `timestamp`, and the headers that map to `ConsumerRecord` properties.

You can specify which headers are to be mapped for outbound messages, by providing patterns to the mapper.
The following listing shows a number of example mappings:

```java
public JsonKafkaHeaderMapper() { (1) ...}
public JsonKafkaHeaderMapper(ObjectMapper objectMapper) { (2) ...}
public JsonKafkaHeaderMapper(String... patterns) { (3) ...}
public JsonKafkaHeaderMapper(ObjectMapper objectMapper, String... patterns) { (4) ...}
```

**1**

Uses a default Jackson `ObjectMapper` and maps most headers, as discussed before the example.

**2**

Uses the provided Jackson `ObjectMapper` and maps most headers, as discussed before the example.

**3**

Uses a default Jackson `ObjectMapper` and maps headers according to the provided patterns.

**4**

Uses the provided Jackson `ObjectMapper` and maps headers according to the provided patterns.

Patterns are rather simple and can contain a leading wildcard (`*`), a trailing wildcard, or both (for example, `*.cat.*`).
You can negate patterns with a leading `!`.
The first pattern that matches a header name (whether positive or negative) wins.

When you provide your own patterns, we recommend including `!id` and `!timestamp`, since these headers are read-only on the inbound side.

> [!IMPORTANT]
> By default, the mapper deserializes only classes whose package is exactly `java.lang`, `java.net`, `java.util`, or `org.springframework.util`.
> You can trust additional packages with the `addTrustedPackages` method.
> Trust is **exact-package-name only**: a class is trusted only when its declaring package appears verbatim in the trusted list.
> Subpackages are **not** trusted transitively; each must be registered explicitly.
> If you receive messages from untrusted sources, register only the specific packages you need.
> To trust all packages without restriction, use `mapper.addTrustedPackages("*")` — though this is not recommended with untrusted sources.
> Classes in a non-trusted package are returned to the application as a `NonTrustedHeaderType` value instead of being deserialized.

```java
// Trusts com.example but NOT com.example.events
mapper.addTrustedPackages("com.example");

// Both must be listed explicitly
mapper.addTrustedPackages("com.example", "com.example.events");
```

> [!NOTE]
> Mapping `String` header values in a raw form is useful when communicating with systems that are not aware of the mapper’s JSON format.

Starting with version 2.2.5, you can specify that certain string-valued headers should not be mapped using JSON, but to/from a raw `byte[]`.
The `AbstractKafkaHeaderMapper` has new properties; `mapAllStringsOut` when set to true, all string-valued headers will be converted to `byte[]` using the `charset` property (default `UTF-8`).
In addition, there is a property `rawMappedHeaders`, which is a map of `header name : boolean`; if the map contains a header name, and the header contains a `String` value, it will be mapped as a raw `byte[]` using the charset.
This map is also used to map raw incoming `byte[]` headers to `String` using the charset if, and only if, the boolean in the map value is `true`.
If the boolean is `false`, or the header name is not in the map with a `true` value, the incoming header is simply mapped as the raw unmapped header.

The following test case illustrates this mechanism.

```java
@Test
public void testSpecificStringConvert() {
    JsonKafkaHeaderMapper mapper = new JsonKafkaHeaderMapper();
    Map<String, Boolean> rawMappedHeaders = new HashMap<>();
    rawMappedHeaders.put("thisOnesAString", true);
    rawMappedHeaders.put("thisOnesBytes", false);
    mapper.setRawMappedHeaders(rawMappedHeaders);
    Map<String, Object> headersMap = new HashMap<>();
    headersMap.put("thisOnesAString", "thing1");
    headersMap.put("thisOnesBytes", "thing2");
    headersMap.put("alwaysRaw", "thing3".getBytes());
    MessageHeaders headers = new MessageHeaders(headersMap);
    Headers target = new RecordHeaders();
    mapper.fromHeaders(headers, target);
    assertThat(target).containsExactlyInAnyOrder(
            new RecordHeader("thisOnesAString", "thing1".getBytes()),
            new RecordHeader("thisOnesBytes", "thing2".getBytes()),
            new RecordHeader("alwaysRaw", "thing3".getBytes()));
    headersMap.clear();
    mapper.toHeaders(target, headersMap);
    assertThat(headersMap).contains(
            entry("thisOnesAString", "thing1"),
            entry("thisOnesBytes", "thing2".getBytes()),
            entry("alwaysRaw", "thing3".getBytes()));
}
```

Both header mappers map all inbound headers, by default.
Starting with version 2.8.8, the patterns, can also applied to inbound mapping.
To create a mapper for inbound mapping, use one of the static methods on the respective mapper:

```java
public static JsonKafkaHeaderMapper forInboundOnlyWithMatchers(String... patterns) {}
public static JsonKafkaHeaderMapper forInboundOnlyWithMatchers(ObjectMapper objectMapper, String... patterns) {}
public static SimpleKafkaHeaderMapper forInboundOnlyWithMatchers(String... patterns) {}
```

For example:

```java
JsonKafkaHeaderMapper inboundMapper = JsonKafkaHeaderMapper.forInboundOnlyWithMatchers("!abc*", "*");
```

This will exclude all headers beginning with `abc` and include all others.

By default, the `JsonKafkaHeaderMapper` is used in the `MessagingMessageConverter` and `BatchMessagingMessageConverter`, as long as Jackson is on the classpath.

With the batch converter, the converted headers are available in the `KafkaHeaders.BATCH_CONVERTED_HEADERS` as a `List<Map<String, Object>>` where the map in a position of the list corresponds to the data position in the payload.

If there is no converter (either because Jackson is not present or it is explicitly set to `null`), the headers from the consumer record are provided unconverted in the `KafkaHeaders.NATIVE_HEADERS` header.
This header is a `Headers` object (or a `List<Headers>` in the case of the batch converter), where the position in the list corresponds to the data position in the payload.

> [!IMPORTANT]
> Certain types are not suitable for JSON serialization, and a simple `toString()` serialization might be preferred for these types.
> The `JsonKafkaHeaderMapper` has a method called `addToStringClasses()` that lets you supply the names of classes that should be treated this way for outbound mapping.
> During inbound mapping, they are mapped as `String`.
> By default, only `org.springframework.util.MimeType` and `org.springframework.http.MediaType` are mapped this way.

> [!NOTE]
> Starting with version 2.3, handling of String-valued headers is simplified.
> Such headers are no longer JSON encoded, by default (i.e. they do not have enclosing `"..."` added).
> The type is still added to the JSON\_TYPES header so the receiving system can convert back to a String (from `byte[]`).
> The mapper can handle (decode) headers produced by older versions (it checks for a leading `"`); in this way an application using 2.3 can consume records from older versions.

> [!IMPORTANT]
> To be compatible with earlier versions, set `encodeStrings` to `true`, if records produced by a version using 2.3 might be consumed by applications using earlier versions.
> When all applications are using 2.3 or higher, you can leave the property at its default value of `false`.

```java
@Bean
MessagingMessageConverter converter() {
    MessagingMessageConverter converter = new MessagingMessageConverter();
    JsonKafkaHeaderMapper mapper = new JsonKafkaHeaderMapper();
    mapper.setEncodeStrings(true);
    converter.setHeaderMapper(mapper);
    return converter;
}
```

If using Spring Boot, it will auto configure this converter bean into the auto-configured `KafkaTemplate`; otherwise you should add this converter to the template.

<a id="kafka-headers--multi-value-header"></a>
<a id="kafka-headers--support-multi-value-header-mapping"></a>

## Support multi-value header mapping

Starting with 4.0, multi-value header mapping is supported, where the same logical header key appears more than once in a Kafka record.

By default, the `HeaderMapper` does **not** create multiple Kafka headers with the same name.
Instead, when it encounters a collection value (e.g., a `List<byte[]>`), it serializes the entire collection into **one** Kafka header whose value is a JSON array.

- **Producer side:** `JsonKafkaHeaderMapper` writes the JSON bytes, while `SimpleKafkaHeaderMapper` ignore it.
- **Consumer side:** the mapper exposes the header as a single value—the **last occurrence wins**; earlier duplicates are silently discarded.

Preserving each individual header requires explicit registration of patterns that designate the header as multi‑valued.

`JsonKafkaHeaderMapper#setMultiValueHeaderPatterns(String… patterns)` accepts a list of patterns, which can be either wildcard expressions or exact header names.

```java
JsonKafkaHeaderMapper mapper = new JsonKafkaHeaderMapper();

// Explicit header names
mapper.setMultiValueHeaderPatterns("test-multi-value1", "test-multi-value2");

// Wildcard patterns for test-multi-value1, test-multi-value2
mapper.setMultiValueHeaderPatterns("test-multi-*");
```

Any header whose name matches one of the supplied patterns is

- **Producer side:** written as separate Kafka headers, one per element.
- **Consumer side:** collected into a `List<?>` that contains the individual header values; each element is returned to the application **after the usual deserialization or type conversion performed by the configured `HeaderMapper`.**

> [!NOTE]
> Regular expressions are **not** supported; only the \* wildcard is allowed in simple patterns—supporting direct equality and forms such as: xxx\*, \*xxx, \*xxx\*, xxx\*yyy.

> [!IMPORTANT]
> On the **Producer Side**, When `JsonKafkaHeaderMapper` serializes a multi-value header, every element in that collection must be of a single Java type—mixing, for example, `String` and `byte[]` values under a single header key will lead to a conversion error.

[Serialization, Deserialization, and Message Conversion](#kafka-serdes)
[Null Payloads and Log Compaction of 'Tombstone' Records](#kafka-tombstones)

---

<a id="kafka-tombstones"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/tombstones.html -->

<!-- page_index: 46 -->

# Null Payloads and Log Compaction of 'Tombstone' Records

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-tombstones--page-title"></a>
<a id="kafka-tombstones--null-payloads-and-log-compaction-of-tombstone-records"></a>

# Null Payloads and Log Compaction of 'Tombstone' Records

When you use [Log Compaction](https://kafka.apache.org/42/documentation/#compaction), you can send and receive messages with `null` payloads to identify the deletion of a key.

You can also receive `null` values for other reasons, such as a `Deserializer` that might return `null` when it cannot deserialize a value.

To send a `null` payload by using the `KafkaTemplate`, you can pass null into the value argument of the `send()` methods.
One exception to this is the `send(Message<?> message)` variant.
Since `spring-messaging` `Message<?>` cannot have a `null` payload, you can use a special payload type called `KafkaNull`, and the framework sends `null`.
For convenience, the static `KafkaNull.INSTANCE` is provided.

When you use a message listener container, the received `ConsumerRecord` has a `null` `value()`.

To configure the `@KafkaListener` to handle `null` payloads, you must use the `@Payload` annotation with `required = false`.
If it is a tombstone message for a compacted log, you usually also need the key so that your application can determine which key was "`deleted`".
The following example shows such a configuration:

```java
@KafkaListener(id = "deletableListener", topics = "myTopic")
public void listen(@Payload(required = false) String value, @Header(KafkaHeaders.RECEIVED_KEY) String key) {
    // value == null represents key deletion
}
```

When you use a class-level `@KafkaListener` with multiple `@KafkaHandler` methods, some additional configuration is needed.
Specifically, you need a `@KafkaHandler` method with a `KafkaNull` payload.
The following example shows how to configure one:

```java
@KafkaListener(id = "multi", topics = "myTopic") static class MultiListenerBean {
@KafkaHandler public void listen(String cat) {...}
@KafkaHandler public void listen(Integer hat) {...}
@KafkaHandler public void delete(@Payload(required = false) KafkaNull nul, @Header(KafkaHeaders.RECEIVED_KEY) int key) {...}
}
```

Note that the argument is `null`, not `KafkaNull`.

> [!TIP]
> See [Manually Assigning All Partitions](#tips).

> [!IMPORTANT]
> This feature requires the use of a `KafkaNullAwarePayloadArgumentResolver` which the framework will configure when using the default `MessageHandlerMethodFactory`.
> When using a custom `MessageHandlerMethodFactory`, see [Adding custom `HandlerMethodArgumentResolver` to `@KafkaListener`](#kafka-serdes--custom-arg-resolve).

[Message Headers](#kafka-headers)
[Handling Exceptions](#kafka-annotation-error-handling)

---

<a id="kafka-annotation-error-handling"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/annotation-error-handling.html -->

<!-- page_index: 47 -->

# Handling Exceptions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-annotation-error-handling--page-title"></a>
<a id="kafka-annotation-error-handling--handling-exceptions"></a>

# Handling Exceptions

This section describes how to handle various exceptions that may arise when you use Spring for Apache Kafka.

<a id="kafka-annotation-error-handling--listener-error-handlers"></a>

## Listener Error Handlers

Starting with version 2.0, the `@KafkaListener` annotation has a new attribute: `errorHandler`.

You can use the `errorHandler` to provide the bean name of a `KafkaListenerErrorHandler` implementation.
This functional interface has one method, as the following listing shows:

```java
@FunctionalInterface
public interface KafkaListenerErrorHandler {

    Object handleError(Message<?> message, ListenerExecutionFailedException exception) throws Exception;

}
```

You have access to the spring-messaging `Message<?>` object produced by the message converter and the exception that was thrown by the listener, which is wrapped in a `ListenerExecutionFailedException`.
The error handler can throw the original or a new exception, which is thrown to the container.
Anything returned by the error handler is ignored.

Starting with version 2.7, you can set the `rawRecordHeader` property on the `MessagingMessageConverter` and `BatchMessagingMessageConverter` which causes the raw `ConsumerRecord` to be added to the converted `Message<?>` in the `KafkaHeaders.RAW_DATA` header.
This is useful, for example, if you wish to use a `DeadLetterPublishingRecoverer` in a listener error handler.
It might be used in a request/reply scenario where you wish to send a failure result to the sender, after some number of retries, after capturing the failed record in a dead letter topic.

```java
@Bean public KafkaListenerErrorHandler eh(DeadLetterPublishingRecoverer recoverer) {return (msg, ex) -> {if (msg.getHeaders().get(KafkaHeaders.DELIVERY_ATTEMPT, Integer.class) > 9) {recoverer.accept(msg.getHeaders().get(KafkaHeaders.RAW_DATA, ConsumerRecord.class), ex); return "FAILED";} throw ex; };}
```

It has a sub-interface (`ConsumerAwareListenerErrorHandler`) that has access to the consumer object, through the following method:

```java
Object handleError(Message<?> message, ListenerExecutionFailedException exception, Consumer<?, ?> consumer);
```

Another sub-interface (`ManualAckListenerErrorHandler`) provides access to the `Acknowledgment` object when using manual `AckMode`s.

```java
Object handleError(Message<?> message, ListenerExecutionFailedException exception,
			Consumer<?, ?> consumer, @Nullable Acknowledgment ack);
```

In either case, you should NOT perform any seeks on the consumer because the container would be unaware of them.

<a id="kafka-annotation-error-handling--error-handlers"></a>
<a id="kafka-annotation-error-handling--container-error-handlers"></a>

## Container Error Handlers

Starting with version 2.8, the legacy `ErrorHandler` and `BatchErrorHandler` interfaces have been superseded by a new `CommonErrorHandler`.
These error handlers can handle errors for both record and batch listeners, allowing a single listener container factory to create containers for both types of listener.
`CommonErrorHandler` implementations to replace most legacy framework error handler implementations are provided.

See [Migrating Custom Legacy Error Handler Implementations to `CommonErrorHandler`](#kafka-annotation-error-handling--migrating-legacy-eh) for information to migrate custom error handlers to `CommonErrorHandler`.

When transactions are being used, no error handlers are configured, by default, so that the exception will roll back the transaction.
Error handling for transactional containers are handled by the [`AfterRollbackProcessor`](#kafka-annotation-error-handling--after-rollback).
If you provide a custom error handler when using transactions, it must throw an exception if you want the transaction rolled back.

This interface has a default method `isAckAfterHandle()` which is called by the container to determine whether the offset(s) should be committed if the error handler returns without throwing an exception; it returns true by default.

Typically, the error handlers provided by the framework will throw an exception when the error is not "handled" (e.g. after performing a seek operation).
By default, such exceptions are logged by the container at `ERROR` level.
All of the framework error handlers extend `KafkaExceptionLogLevelAware` which allows you to control the level at which these exceptions are logged.

```java
/**
 * Set the level at which the exception thrown by this handler is logged.
 * @param logLevel the level (default ERROR).
 */
public void setLogLevel(KafkaException.Level logLevel) {
    ...
}
```

You can specify a global error handler to be used for all listeners in the container factory.
The following example shows how to do so:

```java
@Bean public KafkaListenerContainerFactory<ConcurrentMessageListenerContainer<Integer, String>> kafkaListenerContainerFactory() {ConcurrentKafkaListenerContainerFactory<Integer, String> factory =new ConcurrentKafkaListenerContainerFactory<>(); ...factory.setCommonErrorHandler(myErrorHandler); ...return factory;}
```

By default, if an annotated listener method throws an exception, it is thrown to the container, and the message is handled according to the container configuration.

The container commits any pending offset commits before calling the error handler.

If you are using Spring Boot, you simply need to add the error handler as a `@Bean` and Boot will add it to the auto-configured factory.

<a id="kafka-annotation-error-handling--backoff-handlers"></a>
<a id="kafka-annotation-error-handling--back-off-handlers"></a>

## Back Off Handlers

Error handlers such as the [DefaultErrorHandler](#kafka-annotation-error-handling--default-eh) use a `BackOff` to determine how long to wait before retrying a delivery.
Starting with version 2.9, you can configure a custom `BackOffHandler`.
The default handler simply suspends the thread until the back off time passes (or the container is stopped).
The framework also provides the `ContainerPausingBackOffHandler` which pauses the listener container until the back off time passes and then resumes the container.
This is useful when the delays are longer than the `max.poll.interval.ms` consumer property.
Note that the resolution of the actual back off time will be affected by the `pollTimeout` container property.

<a id="kafka-annotation-error-handling--default-eh"></a>
<a id="kafka-annotation-error-handling--defaulterrorhandler"></a>

## DefaultErrorHandler

This new error handler replaces the `SeekToCurrentErrorHandler` and `RecoveringBatchErrorHandler`, which have been the default error handlers for several releases now.
One difference is that the fallback behavior for batch listeners (when an exception other than a `BatchListenerFailedException` is thrown) is the equivalent of the [Retrying Complete Batches](#kafka-annotation-error-handling--retrying-batch-eh).

> [!IMPORTANT]
> Starting with version 2.9, the `DefaultErrorHandler` can be configured to provide the same semantics as seeking the unprocessed record offsets as discussed below, but without actually seeking.
> Instead, the records are retained by the listener container and resubmitted to the listener after the error handler exits (and after performing a single paused `poll()`, to keep the consumer alive; if [Non-Blocking Retries](#retrytopic) or a `ContainerPausingBackOffHandler` are being used, the pause may extend over multiple polls).
> The error handler returns a result to the container that indicates whether the current failing record can be resubmitted, or if it was recovered and then it will not be sent to the listener again.
> To enable this mode, set the property `seekAfterError` to `false`.

The error handler can recover (skip) a record that keeps failing.
By default, after ten failures, the failed record is logged (at the `ERROR` level).
You can configure the handler with a custom recoverer (`BiConsumer`) and a `BackOff` that controls the delivery attempts and delays between each.
Using a `FixedBackOff` with `FixedBackOff.UNLIMITED_ATTEMPTS` causes (effectively) infinite retries.
The following example configures recovery after three tries:

```java
DefaultErrorHandler errorHandler =
    new DefaultErrorHandler((record, exception) -> {
        // recover after 3 failures, with no back off - e.g. send to a dead-letter topic
    }, new FixedBackOff(0L, 2L));
```

To configure the listener container with a customized instance of this handler, add it to the container factory.

For example, with the `@KafkaListener` container factory, you can add `DefaultErrorHandler` as follows:

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory() {
    ConcurrentKafkaListenerContainerFactory<String, String> factory = new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.getContainerProperties().setAckMode(AckMode.RECORD);
    factory.setCommonErrorHandler(new DefaultErrorHandler(new FixedBackOff(1000L, 2L)));
    return factory;
}
```

For a record listener, this will retry a delivery up to 2 times (3 delivery attempts) with a back off of 1 second, instead of the default configuration (`FixedBackOff(0L, 9)`).
Failures are simply logged after retries are exhausted.

As an example, if the `poll` returns six records (two from each partition 0, 1, 2) and the listener throws an exception on the fourth record, the container acknowledges the first three messages by committing their offsets.
The `DefaultErrorHandler` seeks to offset 1 for partition 1 and offset 0 for partition 2.
The next `poll()` returns the three unprocessed records.

If the `AckMode` was `BATCH`, the container commits the offsets for the first two partitions before calling the error handler.

For a batch listener, the listener must throw a `BatchListenerFailedException` indicating which records in the batch failed.

The sequence of events is:

- Commit the offsets of the records before the index.
- If retries are not exhausted, perform seeks so that all the remaining records (including the failed record) will be redelivered.
- If retries are exhausted, attempt recovery of the failed record (default log only) and perform seeks so that the remaining records (excluding the failed record) will be redelivered.
  The recovered record’s offset is committed.
- If retries are exhausted and recovery fails, seeks are performed as if retries are not exhausted.

> [!IMPORTANT]
> Starting with version 2.9, the `DefaultErrorHandler` can be configured to provide the same semantics as seeking the unprocessed record offsets as discussed above, but without actually seeking.
> Instead, error handler creates a new `ConsumerRecords<?, ?>` containing just the unprocessed records which will then be submitted to the listener (after performing a single paused `poll()`, to keep the consumer alive).
> To enable this mode, set the property `seekAfterError` to `false`.

The default recoverer logs the failed record after retries are exhausted.
You can use a custom recoverer, or one provided by the framework such as the [`DeadLetterPublishingRecoverer`](#kafka-annotation-error-handling--dead-letters).

When using a POJO batch listener (e.g. `List<Thing>`), and you don’t have the full consumer record to add to the exception, you can just add the index of the record that failed:

```java
@KafkaListener(id = "recovering", topics = "someTopic") public void listen(List<Thing> things) {for (int i = 0; i < things.size(); i++) {try {process(things.get(i));} catch (Exception e) {throw new BatchListenerFailedException("Failed to process", i);}}}
```

When the container is configured with `AckMode.MANUAL_IMMEDIATE`, the error handler can be configured to commit the offset of recovered records; set the `commitRecovered` property to `true`.

See also [Publishing Dead-letter Records](#kafka-annotation-error-handling--dead-letters).

When using transactions, similar functionality is provided by the `DefaultAfterRollbackProcessor`.
See [After-rollback Processor](#kafka-annotation-error-handling--after-rollback).

The `DefaultErrorHandler` considers certain exceptions to be fatal, and retries are skipped for such exceptions; the recoverer is invoked on the first failure.
The exceptions that are considered fatal, by default, are:

- `DeserializationException`
- `MessageConversionException`
- `ConversionException`
- `MethodArgumentResolutionException`
- `NoSuchMethodException`
- `ClassCastException`

since these exceptions are unlikely to be resolved on a retried delivery.

You can add more exception types to the not-retryable category, or completely replace the map of classified exceptions.
See the Javadocs for `DefaultErrorHandler.addNotRetryableException()` and `DefaultErrorHandler.setClassifications()` for more information, as well as `ExceptionMatcher`.

Here is an example that adds `IllegalArgumentException` to the not-retryable exceptions:

```java
@Bean
public DefaultErrorHandler errorHandler(ConsumerRecordRecoverer recoverer) {
    DefaultErrorHandler handler = new DefaultErrorHandler(recoverer);
    handler.addNotRetryableExceptions(IllegalArgumentException.class);
    return handler;
}
```

> [!IMPORTANT]
> The `DefaultErrorHandler` only processes exceptions that inherit from `RuntimeException`.
> Exceptions inheriting from `Error` bypass the error handler entirely, causing the consumer to terminate immediately, close the Kafka connection, and skip all retry/recovery mechanisms.
> This critical distinction means applications may report healthy status despite having terminated consumers that no longer process messages.
> Always ensure that exceptions thrown in message processing code explicitly extend from `RuntimeException` rather than `Error` to allow proper error handling.
> In other words, if the application throws an exception, ensure that it is extended from `RuntimeException` and not inadvertently inherited from `Error`.
> Standard errors like `OutOfMemoryError`, `IllegalAccessError`, and other errors beyond the control of the application are still treated as `Error`s and not retried.

The error handler can be configured with one or more `RetryListener`s, receiving notifications of retry and recovery progress.
Starting with version 2.8.10, methods for batch listeners were added.

```java
@FunctionalInterface public interface RetryListener {
void failedDelivery(ConsumerRecord<?, ?> record, Exception ex, int deliveryAttempt);
default void recovered(ConsumerRecord<?, ?> record, Exception ex) {}
default void recoveryFailed(ConsumerRecord<?, ?> record, Exception original, Exception failure) {}
default void failedDelivery(ConsumerRecords<?, ?> records, Exception ex, int deliveryAttempt) {}
default void recovered(ConsumerRecords<?, ?> records, Exception ex) {}
default void recoveryFailed(ConsumerRecords<?, ?> records, Exception original, Exception failure) {}
}
```

See the JavaDocs for more information.

> [!IMPORTANT]
> If the recoverer fails (throws an exception), the failed record will be included in the seeks.
> If the recoverer fails, the `BackOff` will be reset by default and redeliveries will again go through the back offs before recovery is attempted again.
> To skip retries after a recovery failure, set the error handler’s `resetStateOnRecoveryFailure` to `false`.

You can provide the error handler with a `BiFunction<ConsumerRecord<?, ?>, Exception, BackOff>` to determine the `BackOff` to use, based on the failed record and/or the exception:

```java
handler.setBackOffFunction((record, ex) -> { ... });
```

If the function returns `null`, the handler’s default `BackOff` will be used.

Set `resetStateOnExceptionChange` to `true` and the retry sequence will be restarted (including the selection of a new `BackOff`, if so configured) if the exception type changes between failures.
When `false` (the default before version 2.9), the exception type is not considered.

Starting with version 2.9, this is now `true` by default.

Also see [Delivery Attempts Header](#kafka-annotation-error-handling--delivery-header).

<a id="kafka-annotation-error-handling--batch-listener-error-handling-dlt"></a>
<a id="kafka-annotation-error-handling--batch-listener-error-handling-with-dead-letter-topics"></a>

## Batch Listener Error Handling with Dead Letter Topics

> [!IMPORTANT]
> [Non-Blocking Retries](#retrytopic) (the `@RetryableTopic` annotation) are NOT supported with batch listeners.
> For Dead Letter Topic functionality with batch listeners, use `DefaultErrorHandler` with `DeadLetterPublishingRecoverer`.

<a id="kafka-annotation-error-handling--batch-listener-failed-exception"></a>
<a id="kafka-annotation-error-handling--using-batchlistenerfailedexception"></a>

### Using BatchListenerFailedException

To indicate which specific record in a batch failed, throw a `BatchListenerFailedException`:

```java
@KafkaListener(id = "batch-listener", topics = "myTopic", containerFactory = "batchFactory") public void listen(List<ConsumerRecord<String, Order>> records) {for (ConsumerRecord<String, Order> record : records) {try {process(record.value());} catch (Exception e) {// Identifies the failed record for error handling throw new BatchListenerFailedException("Failed to process", e, record);}}}
```

For POJO batch listeners where you don’t have the `ConsumerRecord`, use the index instead:

```java
@KafkaListener(id = "batch-listener", topics = "myTopic", containerFactory = "batchFactory") public void listen(List<Order> orders) {for (int i = 0; i < orders.size(); i++) {try {process(orders.get(i));} catch (Exception e) {throw new BatchListenerFailedException("Failed to process", e, i);}}}
```

<a id="kafka-annotation-error-handling--batch-listener-dlt-config"></a>
<a id="kafka-annotation-error-handling--configuring-dead-letter-topics-for-batch-listeners"></a>

### Configuring Dead Letter Topics for Batch Listeners

Configure a `DefaultErrorHandler` with a `DeadLetterPublishingRecoverer` on your batch listener container factory:

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<String, Order> batchFactory(
        ConsumerFactory<String, Order> consumerFactory,
        KafkaTemplate<String, Order> kafkaTemplate) {

    ConcurrentKafkaListenerContainerFactory<String, Order> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory);
    factory.setBatchListener(true);

    // Configure Dead Letter Publishing
    DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(kafkaTemplate,
            (record, ex) -> new TopicPartition(record.topic() + "-dlt", record.partition()));

    // Configure retries: 3 attempts with 1 second between each
    DefaultErrorHandler errorHandler = new DefaultErrorHandler(recoverer,
            new FixedBackOff(1000L, 2L)); // 2 retries = 3 total attempts

    factory.setCommonErrorHandler(errorHandler);
    return factory;
}
```

<a id="kafka-annotation-error-handling--batch-listener-error-flow"></a>
<a id="kafka-annotation-error-handling--how-batch-error-handling-works"></a>

### How Batch Error Handling Works

When a `BatchListenerFailedException` is thrown, the `DefaultErrorHandler`:

1. **Commits offsets** for all records before the failed record
2. **Retries** the failed record (and subsequent records) according to the `BackOff` configuration
3. **Publishes to DLT** when retries are exhausted - only the failed record is sent to the DLT
4. **Commits the failed record’s offset** and redelivers remaining records for processing

Example flow with a batch of 6 records where record at index 2 fails:

- First attempt: Records 0, 1 processed successfully; record 2 fails
- Container commits offsets for records 0, 1
- Retry attempt 1: Records 2, 3, 4, 5 are retried
- Retry attempt 2: Records 2, 3, 4, 5 are retried again
- After retries exhausted: Record 2 is published to DLT and its offset is committed
- Container continues with records 3, 4, 5

<a id="kafka-annotation-error-handling--batch-listener-skip-retries"></a>
<a id="kafka-annotation-error-handling--skipping-retries-for-specific-exceptions"></a>

### Skipping Retries for Specific Exceptions

By default, the `DefaultErrorHandler` retries all exceptions except for fatal ones (like `DeserializationException`, `MessageConversionException`, etc.).
To skip retries for your own exception types, configure the error handler with exception classifications.

The error handler examines the **cause** of the `BatchListenerFailedException` to determine if it should skip retries:

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<String, Order> batchFactory(
        ConsumerFactory<String, Order> consumerFactory,
        KafkaTemplate<String, Order> kafkaTemplate) {

    ConcurrentKafkaListenerContainerFactory<String, Order> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory);
    factory.setBatchListener(true);

    DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(kafkaTemplate);
    DefaultErrorHandler errorHandler = new DefaultErrorHandler(recoverer,
            new FixedBackOff(1000L, 2L));

    // Add custom exception types that should skip retries and go directly to DLT
    errorHandler.addNotRetryableExceptions(ValidationException.class, InvalidFormatException.class);

    factory.setCommonErrorHandler(errorHandler);
    return factory;
}
```

Now in your listener:

```java
@KafkaListener(id = "batch-listener", topics = "orders", containerFactory = "batchFactory") public void processOrders(List<ConsumerRecord<String, Order>> records) {for (ConsumerRecord<String, Order> record : records) {try {process(record.value());} catch (DatabaseException e) {// Will be retried 3 times (according to BackOff configuration) throw new BatchListenerFailedException("Database error", e, record);} catch (ValidationException e) {// Skips retries - goes directly to DLT // (because ValidationException is configured as not retryable) throw new BatchListenerFailedException("Validation failed", e, record);}}}
```

> [!IMPORTANT]
> The error handler checks the **cause** (the second parameter) of the `BatchListenerFailedException`.
> If the cause is classified as not retryable, the record is immediately sent to the DLT without retries.

<a id="kafka-annotation-error-handling--batch-listener-offset-commits"></a>
<a id="kafka-annotation-error-handling--offset-commit-behavior"></a>

### Offset Commit Behavior

Understanding offset commits is important for batch error handling:

- **AckMode.BATCH** (most common for batch listeners):

  - Offsets before the failed record are committed before error handling
  - The failed record’s offset is committed after successful recovery (DLT publishing)
- **AckMode.MANUAL\_IMMEDIATE**:

  - Set `errorHandler.setCommitRecovered(true)` to commit recovered record offsets
  - You control acknowledgment timing in your listener

Example with manual acknowledgment:

```java
@KafkaListener(id = "manual-batch", topics = "myTopic", containerFactory = "manualBatchFactory") public void listen(List<ConsumerRecord<String, Order>> records, Acknowledgment ack) {for (ConsumerRecord<String, Order> record : records) {try {process(record.value());} catch (Exception e) {throw new BatchListenerFailedException("Processing failed", e, record);}} ack.acknowledge();}
```

<a id="kafka-annotation-error-handling--batch-listener-conv-errors"></a>
<a id="kafka-annotation-error-handling--conversion-errors-with-batch-error-handlers"></a>

### Conversion Errors with Batch Error Handlers

Starting with version 2.8, batch listeners can now properly handle conversion errors, when using a `MessageConverter` with a `ByteArrayDeserializer`, a `BytesDeserializer` or a `StringDeserializer`, as well as a `DefaultErrorHandler`.
When a conversion error occurs, the payload is set to null and a deserialization exception is added to the record headers, similar to the `ErrorHandlingDeserializer`.
A list of `ConversionException`s is available in the listener so the listener can throw a `BatchListenerFailedException` indicating the first index at which a conversion exception occurred.

Example:

```java
@KafkaListener(id = "test", topics = "topic") void listen(List<Thing> in, @Header(KafkaHeaders.CONVERSION_FAILURES) List<ConversionException> exceptions) {for (int i = 0; i < in.size(); i++) {Foo foo = in.get(i); if (foo == null && exceptions.get(i) != null) {throw new BatchListenerFailedException("Conversion error", exceptions.get(i), i);} process(foo);}}
```

<a id="kafka-annotation-error-handling--batch-listener-deser-errors"></a>
<a id="kafka-annotation-error-handling--deserialization-errors-with-batch-listeners"></a>

### Deserialization Errors with Batch Listeners

> [!IMPORTANT]
> Batch listeners require **manual handling** of deserialization errors.
> Unlike record listeners, there is no automatic error handler that detects and routes deserialization failures to the DLT.
> You must explicitly check for failed records and throw `BatchListenerFailedException`.

Use `ErrorHandlingDeserializer` to prevent deserialization failures from stopping the entire batch:

```java
@Bean
public ConsumerFactory<String, Order> consumerFactory() {
    Map<String, Object> props = new HashMap<>();
    props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
    props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);

    // Wrap your deserializer with ErrorHandlingDeserializer
    props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ErrorHandlingDeserializer.class);
    props.put(ErrorHandlingDeserializer.VALUE_DESERIALIZER_CLASS, JsonDeserializer.class.getName());

    return new DefaultKafkaConsumerFactory<>(props);
}
```

In your listener, you must manually check for `null` values which indicate deserialization failures:

```java
@KafkaListener(id = "batch-deser", topics = "orders", containerFactory = "batchFactory") public void listen(List<ConsumerRecord<String, Order>> records) {for (ConsumerRecord<String, Order> record : records) {if (record.value() == null) {// Deserialization failed - throw exception to send to DLT throw new BatchListenerFailedException("Deserialization failed", record);} process(record.value());}}
```

When `DeadLetterPublishingRecoverer` publishes a deserialization failure to the DLT:

- The original `byte[]` data that failed to deserialize is restored as the record value
- Exception information (class name, message, stacktrace) is added to standard DLT exception headers
- The original `ErrorHandlingDeserializer` exception header is removed by default (set `setRetainExceptionHeader(true)` on the recoverer to keep it)

<a id="kafka-annotation-error-handling--retrying-batch-eh"></a>
<a id="kafka-annotation-error-handling--retrying-complete-batches"></a>

## Retrying Complete Batches

This is now the fallback behavior of the `DefaultErrorHandler` for a batch listener where the listener throws an exception other than a `BatchListenerFailedException`.

There is no guarantee that, when a batch is redelivered, the batch has the same number of records and/or the redelivered records are in the same order.
It is impossible, therefore, to easily maintain retry state for a batch.
The `FallbackBatchErrorHandler` takes the following approach.
If a batch listener throws an exception that is not a `BatchListenerFailedException`, the retries are performed from the in-memory batch of records.
In order to avoid a rebalance during an extended retry sequence, the error handler pauses the consumer, polls it before sleeping for the back off, for each retry, and calls the listener again.
If/when retries are exhausted, the `ConsumerRecordRecoverer` is called for each record in the batch.
If the recoverer throws an exception, or the thread is interrupted during its sleep, the batch of records will be redelivered on the next poll.
Before exiting, regardless of the outcome, the consumer is resumed.

> [!IMPORTANT]
> This mechanism cannot be used with transactions.

While waiting for a `BackOff` interval, the error handler will loop with a short sleep until the desired delay is reached, while checking to see if the container has been stopped, allowing the sleep to exit soon after the `stop()` rather than causing a delay.

<a id="kafka-annotation-error-handling--container-stopping-error-handlers"></a>

## Container Stopping Error Handlers

The `CommonContainerStoppingErrorHandler` stops the container if the listener throws an exception.
For record listeners, when the `AckMode` is `RECORD`, offsets for already processed records are committed.
For record listeners, when the `AckMode` is any manual value, offsets for already acknowledged records are committed.
For record listeners, when the `AckMode` is `BATCH`, or for batch listeners, the entire batch is replayed when the container is restarted.

After the container stops, an exception that wraps the `ListenerExecutionFailedException` is thrown.
This is to cause the transaction to roll back (if transactions are enabled).

<a id="kafka-annotation-error-handling--cond-eh"></a>
<a id="kafka-annotation-error-handling--delegating-error-handler"></a>

## Delegating Error Handler

The `CommonDelegatingErrorHandler` can delegate to different error handlers, depending on the exception type.
For example, you may wish to invoke a `DefaultErrorHandler` for most exceptions, or a `CommonContainerStoppingErrorHandler` for others.

All delegates must share the same compatible properties (`ackAfterHandle`, `seekAfterError` …).

<a id="kafka-annotation-error-handling--log-eh"></a>
<a id="kafka-annotation-error-handling--logging-error-handler"></a>

## Logging Error Handler

The `CommonLoggingErrorHandler` simply logs the exception; with a record listener, the remaining records from the previous poll are passed to the listener.
For a batch listener, all the records in the batch are logged.

<a id="kafka-annotation-error-handling--mixed-eh"></a>
<a id="kafka-annotation-error-handling--using-different-common-error-handlers-for-record-and-batch-listeners"></a>

## Using Different Common Error Handlers for Record and Batch Listeners

If you wish to use a different error handling strategy for record and batch listeners, the `CommonMixedErrorHandler` is provided allowing the configuration of a specific error handler for each listener type.

<a id="kafka-annotation-error-handling--eh-summary"></a>
<a id="kafka-annotation-error-handling--common-error-handler-summary"></a>

## Common Error Handler Summary

- `DefaultErrorHandler`
- `CommonContainerStoppingErrorHandler`
- `CommonDelegatingErrorHandler`
- `CommonLoggingErrorHandler`
- `CommonMixedErrorHandler`

<a id="kafka-annotation-error-handling--legacy-eh"></a>
<a id="kafka-annotation-error-handling--legacy-error-handlers-and-their-replacements"></a>

## Legacy Error Handlers and Their Replacements

| Legacy Error Handler | Replacement |
| --- | --- |
| `LoggingErrorHandler` | `CommonLoggingErrorHandler` |
| `BatchLoggingErrorHandler` | `CommonLoggingErrorHandler` |
| `ConditionalDelegatingErrorHandler` | `DelegatingErrorHandler` |
| `ConditionalDelegatingBatchErrorHandler` | `DelegatingErrorHandler` |
| `ContainerStoppingErrorHandler` | `CommonContainerStoppingErrorHandler` |
| `ContainerStoppingBatchErrorHandler` | `CommonContainerStoppingErrorHandler` |
| `SeekToCurrentErrorHandler` | `DefaultErrorHandler` |
| `SeekToCurrentBatchErrorHandler` | No replacement, use `DefaultErrorHandler` with an infinite `BackOff`. |
| `RecoveringBatchErrorHandler` | `DefaultErrorHandler` |
| `RetryingBatchErrorHandler` | No replacements, use `DefaultErrorHandler` and throw an exception other than `BatchListenerFailedException`. |

<a id="kafka-annotation-error-handling--migrating-legacy-eh"></a>
<a id="kafka-annotation-error-handling--migrating-custom-legacy-error-handler-implementations-to-commonerrorhandler"></a>

### Migrating Custom Legacy Error Handler Implementations to `CommonErrorHandler`

Refer to the JavaDocs in `CommonErrorHandler`.

To replace an `ErrorHandler` or `ConsumerAwareErrorHandler` implementation, you should implement `handleOne()` and leave `seeksAfterHandle()` to return `false` (default).
You should also implement `handleOtherException()` to handle exceptions that occur outside the scope of record processing (e.g. consumer errors).

To replace a `RemainingRecordsErrorHandler` implementation, you should implement `handleRemaining()` and override `seeksAfterHandle()` to return `true` (the error handler must perform the necessary seeks).
You should also implement `handleOtherException()` - to handle exceptions that occur outside the scope of record processing (e.g. consumer errors).

To replace any `BatchErrorHandler` implementation, you should implement `handleBatch()`
You should also implement `handleOtherException()` - to handle exceptions that occur outside the scope of record processing (e.g. consumer errors).

<a id="kafka-annotation-error-handling--after-rollback"></a>
<a id="kafka-annotation-error-handling--after-rollback-processor"></a>

## After Rollback Processor

When using transactions, if the listener throws an exception (and an error handler, if present, throws an exception), the transaction is rolled back.
By default, any unprocessed records (including the failed record) are re-fetched on the next poll.
This is achieved by performing `seek` operations in the `DefaultAfterRollbackProcessor`.
With a batch listener, the entire batch of records is reprocessed (the container has no knowledge of which record in the batch failed).
To modify this behavior, you can configure the listener container with a custom `AfterRollbackProcessor`.
For example, with a record-based listener, you might want to keep track of the failed record and give up after some number of attempts, perhaps by publishing it to a dead-letter topic.

Starting with version 2.2, the `DefaultAfterRollbackProcessor` can now recover (skip) a record that keeps failing.
By default, after ten failures, the failed record is logged (at the `ERROR` level).
You can configure the processor with a custom recoverer (`BiConsumer`) and maximum failures.
Setting the `maxFailures` property to a negative number causes infinite retries.
The following example configures recovery after three tries:

```java
AfterRollbackProcessor<String, String> processor =
    new DefaultAfterRollbackProcessor((record, exception) -> {
        // recover after 3 failures, with no back off - e.g. send to a dead-letter topic
    }, new FixedBackOff(0L, 2L));
```

When you do not use transactions, you can achieve similar functionality by configuring a `DefaultErrorHandler`.
See [Container Error Handlers](#kafka-annotation-error-handling--error-handlers).

Starting with version 3.2, Recovery can now recover (skip) entire batch of records that keeps failing.
Set `ContainerProperties.setBatchRecoverAfterRollback(true)` to enable this feature.

> [!IMPORTANT]
> Default behavior, recovery is not possible with a batch listener, since the framework has no knowledge about which record in the batch keeps failing.
> In such cases, the application listener must handle a record that keeps failing.

See also [Publishing Dead-letter Records](#kafka-annotation-error-handling--dead-letters).

Starting with version 2.2.5, the `DefaultAfterRollbackProcessor` can be invoked in a new transaction (started after the failed transaction rolls back).
Then, if you are using the `DeadLetterPublishingRecoverer` to publish a failed record, the processor will send the recovered record’s offset in the original topic/partition to the transaction.
To enable this feature, set the `commitRecovered` and `kafkaTemplate` properties on the `DefaultAfterRollbackProcessor`.

> [!IMPORTANT]
> If the recoverer fails (throws an exception), the failed record will be included in the seeks.
> Starting with version 2.5.5, if the recoverer fails, the `BackOff` will be reset by default and redeliveries will again go through the back offs before recovery is attempted again.
> With earlier versions, the `BackOff` was not reset and recovery was re-attempted on the next failure.
> To revert to the previous behavior, set the processor’s `resetStateOnRecoveryFailure` property to `false`.

Starting with version 2.6, you can now provide the processor with a `BiFunction<ConsumerRecord<?, ?>, Exception, BackOff>` to determine the `BackOff` to use, based on the failed record and/or the exception:

```java
handler.setBackOffFunction((record, ex) -> { ... });
```

If the function returns `null`, the processor’s default `BackOff` will be used.

Starting with version 2.6.3, set `resetStateOnExceptionChange` to `true` and the retry sequence will be restarted (including the selection of a new `BackOff`, if so configured) if the exception type changes between failures.
By default, the exception type is not considered.

Starting with version 2.3.1, similar to the `DefaultErrorHandler`, the `DefaultAfterRollbackProcessor` considers certain exceptions to be fatal, and retries are skipped for such exceptions; the recoverer is invoked on the first failure.
The exceptions that are considered fatal, by default, are:

- `DeserializationException`
- `MessageConversionException`
- `ConversionException`
- `MethodArgumentResolutionException`
- `NoSuchMethodException`
- `ClassCastException`

since these exceptions are unlikely to be resolved on a retried delivery.

You can add more exception types to the not-retryable category, or completely replace the map of classified exceptions.
See the Javadocs for `DefaultAfterRollbackProcessor.setClassifications()` for more information, as well as `ExceptionMatcher`.

Here is an example that adds `IllegalArgumentException` to the not-retryable exceptions:

```java
@Bean
public DefaultAfterRollbackProcessor errorHandler(BiConsumer<ConsumerRecord<?, ?>, Exception> recoverer) {
    DefaultAfterRollbackProcessor processor = new DefaultAfterRollbackProcessor(recoverer);
    processor.addNotRetryableException(IllegalArgumentException.class);
    return processor;
}
```

Also see [Delivery Attempts Header](#kafka-annotation-error-handling--delivery-header).

> [!IMPORTANT]
> With current `kafka-clients`, the container cannot detect whether a `ProducerFencedException` is caused by a rebalance or if the producer’s `transactional.id` has been revoked due to a timeout or expiry.
> Because, in most cases, it is caused by a rebalance, the container does not call the `AfterRollbackProcessor` (because it’s not appropriate to seek the partitions because we no longer are assigned them).
> If you ensure the timeout is large enough to process each transaction and periodically perform an "empty" transaction (e.g. via a `ListenerContainerIdleEvent`) you can avoid fencing due to timeout and expiry.
> Or, you can set the `stopContainerWhenFenced` container property to `true` and the container will stop, avoiding the loss of records.
> You can consume a `ConsumerStoppedEvent` and check the `Reason` property for `FENCED` to detect this condition.
> Since the event also has a reference to the container, you can restart the container using this event.

Starting with version 2.7, while waiting for a `BackOff` interval, the error handler will loop with a short sleep until the desired delay is reached, while checking to see if the container has been stopped, allowing the sleep to exit soon after the `stop()` rather than causing a delay.

Starting with version 2.7, the processor can be configured with one or more `RetryListener`s, receiving notifications of retry and recovery progress.

```java
@FunctionalInterface public interface RetryListener {
void failedDelivery(ConsumerRecord<?, ?> record, Exception ex, int deliveryAttempt);
default void recovered(ConsumerRecord<?, ?> record, Exception ex) {}
default void recoveryFailed(ConsumerRecord<?, ?> record, Exception original, Exception failure) {}
}
```

See the JavaDocs for more information.

<a id="kafka-annotation-error-handling--delivery-header"></a>
<a id="kafka-annotation-error-handling--delivery-attempts-header"></a>

## Delivery Attempts Header

The following applies to record listeners only, not batch listeners.

Starting with version 2.5, when using an `ErrorHandler` or `AfterRollbackProcessor` that implements `DeliveryAttemptAware`, it is possible to enable the addition of the `KafkaHeaders.DELIVERY_ATTEMPT` header (`kafka_deliveryAttempt`) to the record.
The value of this header is an incrementing integer starting at 1.
When receiving a raw `ConsumerRecord<?, ?>` the integer is in a `byte[4]`.

```java
int delivery = ByteBuffer.wrap(record.headers()
    .lastHeader(KafkaHeaders.DELIVERY_ATTEMPT).value())
    .getInt();
```

When using `@KafkaListener` with the `JsonKafkaHeaderMapper` or `SimpleKafkaHeaderMapper`, it can be obtained by adding `@Header(KafkaHeaders.DELIVERY_ATTEMPT) int delivery` as a parameter to the listener method.

To enable population of this header, set the container property `deliveryAttemptHeader` to `true`.
It is disabled by default to avoid the (small) overhead of looking up the state for each record and adding the header.

The `DefaultErrorHandler` and `DefaultAfterRollbackProcessor` support this feature.

<a id="kafka-annotation-error-handling--delivery-attempts-header-for-batch-listener"></a>

## Delivery Attempts Header for batch listener

When processing `ConsumerRecord` with the `BatchListener`, the `KafkaHeaders.DELIVERY_ATTEMPT` header can be present in a different way compared to `SingleRecordListener`.

Starting with version 3.3, if you want to inject the `KafkaHeaders.DELIVERY_ATTEMPT` header into the `ConsumerRecord` when using the `BatchListener`, set the `DeliveryAttemptAwareRetryListener` as the `RetryListener` in the `ErrorHandler`.

Please refer to the code below.

```java
final FixedBackOff fixedBackOff = new FixedBackOff(1, 10);
final DefaultErrorHandler errorHandler = new DefaultErrorHandler(fixedBackOff);
errorHandler.setRetryListeners(new DeliveryAttemptAwareRetryListener());

ConcurrentKafkaListenerContainerFactory<String, String> factory = new ConcurrentKafkaListenerContainerFactory<>();
factory.setConsumerFactory(consumerFactory);
factory.setCommonErrorHandler(errorHandler);
```

Then, whenever a batch fails to complete, the `DeliveryAttemptAwareRetryListener` will inject a `KafkaHeaders.DELIVERY_ATTMPT` header into the `ConsumerRecord`.

<a id="kafka-annotation-error-handling--li-header"></a>
<a id="kafka-annotation-error-handling--listener-info-header"></a>

## Listener Info Header

In some cases, it is useful to be able to know which container a listener is running in.

Starting with version 2.8.4, you can now set the `listenerInfo` property on the listener container, or set the `info` attribute on the `@KafkaListener` annotation.
Then, the container will add this in the `KafkaListener.LISTENER_INFO` header to all incoming messages; it can then be used in record interceptors, filters, etc., or in the listener itself.

```java
@KafkaListener(id = "something", topics = "topic", filter = "someFilter",
        info = "this is the something listener")
public void listen(@Payload Thing thing,
        @Header(KafkaHeaders.LISTENER_INFO) String listenerInfo) {
    ...
}
```

When used in a `RecordInterceptor` or `RecordFilterStrategy` implementation, the header is in the consumer record as a byte array, converted using the `KafkaListenerAnnotationBeanPostProcessor`'s `charSet` property.

The header mappers also convert to `String` when creating `MessageHeaders` from the consumer record and never map this header on an outbound record.

For POJO batch listeners, starting with version 2.8.6, the header is copied into each member of the batch and is also available as a single `String` parameter after conversion.

```java
@KafkaListener(id = "list2", topics = "someTopic", containerFactory = "batchFactory",
        info = "info for batch")
public void listen(List<Thing> list,
        @Header(KafkaHeaders.RECEIVED_KEY) List<Integer> keys,
        @Header(KafkaHeaders.RECEIVED_PARTITION) List<Integer> partitions,
        @Header(KafkaHeaders.RECEIVED_TOPIC) List<String> topics,
        @Header(KafkaHeaders.OFFSET) List<Long> offsets,
        @Header(KafkaHeaders.LISTENER_INFO) String info) {
            ...
}
```

> [!NOTE]
> If the batch listener has a filter and the filter results in an empty batch, you will need to add `required = false` to the `@Header` parameter because the info is not available for an empty batch.

If you receive `List<Message<Thing>>` the info is in the `KafkaHeaders.LISTENER_INFO` header of each `Message<?>`.

See [Batch Listeners](#kafka-receiving-messages-listener-annotation--batch-listeners) for more information about consuming batches.

<a id="kafka-annotation-error-handling--dead-letters"></a>
<a id="kafka-annotation-error-handling--publishing-dead-letter-records"></a>

## Publishing Dead-letter Records

You can configure the `DefaultErrorHandler` and `DefaultAfterRollbackProcessor` with a record recoverer when the maximum number of failures is reached for a record.
The framework provides the `DeadLetterPublishingRecoverer`, which publishes the failed message to another topic.
The recoverer requires a `KafkaTemplate<Object, Object>`, which is used to send the record.
You can also, optionally, configure it with a `BiFunction<ConsumerRecord<?, ?>, Exception, TopicPartition>`, which is called to resolve the destination topic and partition.

> [!IMPORTANT]
> By default, the dead-letter record is sent to a topic named `<originalTopic>-dlt` (the original topic name suffixed with `-dlt`) and to the same partition as the original record.
> Therefore, when you use the default resolver, the dead-letter topic **must have at least as many partitions as the original topic.**

If the returned `TopicPartition` has a negative partition, the partition is not set in the `ProducerRecord`, so the partition is selected by Kafka.
Starting with version 2.2.4, any `ListenerExecutionFailedException` (thrown, for example, when an exception is detected in a `@KafkaListener` method) is enhanced with the `groupId` property.
This allows the destination resolver to use this, in addition to the information in the `ConsumerRecord` to select the dead letter topic.

The following example shows how to wire a custom destination resolver:

```java
DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(template,(r, e) -> {if (e instanceof FooException) {return new TopicPartition(r.topic() + ".Foo.failures", r.partition());} else {return new TopicPartition(r.topic() + ".other.failures", r.partition());} }); CommonErrorHandler errorHandler = new DefaultErrorHandler(recoverer, new FixedBackOff(0L, 2L));
```

The record sent to the dead-letter topic is enhanced with the following headers:

- `KafkaHeaders.DLT_EXCEPTION_FQCN`: The Exception class name (generally a `ListenerExecutionFailedException`, but can be others).
- `KafkaHeaders.DLT_EXCEPTION_CAUSE_FQCN`: The Exception cause class name, if present (since version 2.8).
- `KafkaHeaders.DLT_EXCEPTION_STACKTRACE`: The Exception stack trace.
- `KafkaHeaders.DLT_EXCEPTION_MESSAGE`: The Exception message.
- `KafkaHeaders.DLT_KEY_EXCEPTION_FQCN`: The Exception class name (key deserialization errors only).
- `KafkaHeaders.DLT_KEY_EXCEPTION_STACKTRACE`: The Exception stack trace (key deserialization errors only).
- `KafkaHeaders.DLT_KEY_EXCEPTION_MESSAGE`: The Exception message (key deserialization errors only).
- `KafkaHeaders.DLT_ORIGINAL_TOPIC`: The original topic.
- `KafkaHeaders.DLT_ORIGINAL_PARTITION`: The original partition.
- `KafkaHeaders.DLT_ORIGINAL_OFFSET`: The original offset.
- `KafkaHeaders.DLT_ORIGINAL_TIMESTAMP`: The original timestamp.
- `KafkaHeaders.DLT_ORIGINAL_TIMESTAMP_TYPE`: The original timestamp type.
- `KafkaHeaders.DLT_ORIGINAL_CONSUMER_GROUP`: The original consumer group that failed to process the record (since version 2.8).

Key exceptions are only caused by `DeserializationException`s so there is no `DLT_KEY_EXCEPTION_CAUSE_FQCN`.

There are two mechanisms to add more headers.

1. Subclass the recoverer and override `createProducerRecord()` - call `super.createProducerRecord()` and add more headers.
2. Provide a `BiFunction` to receive the consumer record and exception, returning a `Headers` object; headers from there will be copied to the final producer record; also see [Managing Dead Letter Record Headers](#kafka-annotation-error-handling--dlpr-headers).
   Use `setHeadersFunction()` to set the `BiFunction`.

The second is simpler to implement but the first has more information available, including the already assembled standard headers.

Starting with version 2.3, when used in conjunction with an `ErrorHandlingDeserializer`, the publisher will restore the record `value()`, in the dead-letter producer record, to the original value that failed to be deserialized.
Previously, the `value()` was null and user code had to decode the `DeserializationException` from the message headers.
In addition, you can provide multiple `KafkaTemplate`s to the publisher; this might be needed, for example, if you want to publish the `byte[]` from a `DeserializationException`, as well as values using a different serializer from records that were deserialized successfully.
Here is an example of configuring the publisher with `KafkaTemplate`s that use a `String` and `byte[]` serializer:

```java
@Bean
public DeadLetterPublishingRecoverer publisher(KafkaTemplate<?, ?> stringTemplate,
        KafkaTemplate<?, ?> bytesTemplate) {
    Map<Class<?>, KafkaOperations<?, ?>> templates = new LinkedHashMap<>();
    templates.put(String.class, stringTemplate);
    templates.put(byte[].class, bytesTemplate);
    return new DeadLetterPublishingRecoverer(templates);
}
```

The publisher uses the map keys to locate a template that is suitable for the `value()` about to be published.
A `LinkedHashMap` is recommended so that the keys are examined in order.

When publishing `null` values, and there are multiple templates, the recoverer will look for a template for the `Void` class; if none is present, the first template from the `values().iterator()` will be used.

Since 2.7 you can use the `setFailIfSendResultIsError` method so that an exception is thrown when message publishing fails.
You can also set a timeout for the verification of the sender success with `setWaitForSendResultTimeout`.

> [!IMPORTANT]
> If the recoverer fails (throws an exception), the failed record will be included in the seeks.
> Starting with version 2.5.5, if the recoverer fails, the `BackOff` will be reset by default and redeliveries will again go through the back offs before recovery is attempted again.
> With earlier versions, the `BackOff` was not reset and recovery was re-attempted on the next failure.
> To revert to the previous behavior, set the error handler’s `resetStateOnRecoveryFailure` property to `false`.

Starting with version 2.6.3, set `resetStateOnExceptionChange` to `true` and the retry sequence will be restarted (including the selection of a new `BackOff`, if so configured) if the exception type changes between failures.
By default, the exception type is not considered.

Starting with version 2.3, the recoverer can also be used with Kafka Streams - see [Recovery from Deserialization Exceptions](#streams--streams-deser-recovery) for more information.

The `ErrorHandlingDeserializer` adds the deserialization exception(s) in headers `ErrorHandlingDeserializer.VALUE_DESERIALIZER_EXCEPTION_HEADER` and `ErrorHandlingDeserializer.KEY_DESERIALIZER_EXCEPTION_HEADER` (using Java serialization).
By default, these headers are not retained in the message published to the dead letter topic.
Starting with version 2.7, if both the key and value fail deserialization, the original values of both are populated in the record sent to the DLT.

If incoming records are dependent on each other, but may arrive out of order, it may be useful to republish a failed record to the tail of the original topic (for some number of times), instead of sending it directly to the dead letter topic.
See [this Stack Overflow Question](https://stackoverflow.com/questions/64646996) for an example.

The following error handler configuration will do exactly that:

```java
@Bean
public ErrorHandler eh(KafkaOperations<String, String> template) {
    return new DefaultErrorHandler(new DeadLetterPublishingRecoverer(template,
            (rec, ex) -> {
                org.apache.kafka.common.header.Header retries = rec.headers().lastHeader("retries");
                if (retries == null) {
                    retries = new RecordHeader("retries", new byte[] { 1 });
                    rec.headers().add(retries);
                }
                else {
                    retries.value()[0]++;
                }
                return retries.value()[0] > 5
                        ? new TopicPartition("topic-dlt", rec.partition())
                        : new TopicPartition("topic", rec.partition());
            }), new FixedBackOff(0L, 0L));
}
```

Starting with version 2.7, the recoverer checks that the partition selected by the destination resolver actually exists.
If the partition is not present, the partition in the `ProducerRecord` is set to `null`, allowing the `KafkaProducer` to select the partition.
You can disable this check by setting the `verifyPartition` property to `false`.

Starting with version 3.1, setting the `logRecoveryRecord` property to `true` will log the recovery record and exception.

<a id="kafka-annotation-error-handling--dlpr-headers"></a>
<a id="kafka-annotation-error-handling--managing-dead-letter-record-headers"></a>

## Managing Dead Letter Record Headers

Referring to [Publishing Dead-letter Records](#kafka-annotation-error-handling--dead-letters) above, the `DeadLetterPublishingRecoverer` has two properties used to manage headers when those headers already exist (such as when reprocessing a dead letter record that failed, including when using [Non-Blocking Retries](#retrytopic)).

- `appendOriginalHeaders` (default `true`)
- `stripPreviousExceptionHeaders` (default `true` since version 2.8)

Apache Kafka supports multiple headers with the same name; to obtain the "latest" value, you can use `headers.lastHeader(headerName)`; to get an iterator over multiple headers, use `headers.headers(headerName).iterator()`.

When repeatedly republishing a failed record, these headers can grow (and eventually cause publication to fail due to a `RecordTooLargeException`); this is especially true for the exception headers and particularly for the stack trace headers.

The reason for the two properties is because, while you might want to retain only the last exception information, you might want to retain the history of which topic(s) the record passed through for each failure.

`appendOriginalHeaders` is applied to all headers named `ORIGINAL` while `stripPreviousExceptionHeaders` is applied to all headers named `EXCEPTION`.

Starting with version 2.8.4, you now can control which of the standard headers will be added to the output record.
See the `enum HeadersToAdd` for the generic names of the (currently) 10 standard headers that are added by default (these are not the actual header names, just an abstraction; the actual header names are set up by the `getHeaderNames()` method which subclasses can override.

To exclude headers, use the `excludeHeaders()` method; for example, to suppress adding the exception stack trace in a header, use:

```java
DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(template);
recoverer.excludeHeaders(HeaderNames.HeadersToAdd.EX_STACKTRACE);
```

In addition, you can completely customize the addition of exception headers by adding an `ExceptionHeadersCreator`; this also disables all standard exception headers.

```java
DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(template);
recoverer.setExceptionHeadersCreator((kafkaHeaders, exception, isKey, headerNames) -> {
    kafkaHeaders.add(new RecordHeader(..., ...));
});
```

Also starting with version 2.8.4, you can now provide multiple headers functions, via the `addHeadersFunction` method.
This allows additional functions to apply, even if another function has already been registered, for example, when using [Non-Blocking Retries](#retrytopic).

Also see [Failure Header Management](#retrytopic-features--retry-headers) with [Non-Blocking Retries](#retrytopic).

<a id="kafka-annotation-error-handling--exp-backoff"></a>
<a id="kafka-annotation-error-handling--exponentialbackoffwithmaxretries-implementation"></a>

## `ExponentialBackOffWithMaxRetries` Implementation

Spring Framework provides a number of `BackOff` implementations.
By default, the `ExponentialBackOff` will retry indefinitely; to give up after some number of retry attempts requires calculating the `maxElapsedTime`.
Since version 2.7.3, Spring for Apache Kafka provides the `ExponentialBackOffWithMaxRetries` which is a subclass that receives the `maxRetries` property and automatically calculates the `maxElapsedTime`, which is a little more convenient.

```java
@Bean
DefaultErrorHandler handler() {
    ExponentialBackOffWithMaxRetries bo = new ExponentialBackOffWithMaxRetries(6);
    bo.setInitialInterval(1_000L);
    bo.setMultiplier(2.0);
    bo.setMaxInterval(10_000L);
    return new DefaultErrorHandler(myRecoverer, bo);
}
```

This will retry after `1, 2, 4, 8, 10, 10` seconds, before calling the recoverer.

[Null Payloads and Log Compaction of 'Tombstone' Records](#kafka-tombstones)
[JAAS and Kerberos](#kafka-kerberos)

---

<a id="kafka-kerberos"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/kerberos.html -->

<!-- page_index: 48 -->

# JAAS and Kerberos

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-kerberos--page-title"></a>
<a id="kafka-kerberos--jaas-and-kerberos"></a>

# JAAS and Kerberos

Starting with version 2.0, a `KafkaJaasLoginModuleInitializer` class has been added to assist with Kerberos configuration.
You can add this bean, with the desired configuration, to your application context.
The following example configures such a bean:

```java
@Bean
public KafkaJaasLoginModuleInitializer jaasConfig() throws IOException {
    KafkaJaasLoginModuleInitializer jaasConfig = new KafkaJaasLoginModuleInitializer();
    jaasConfig.setControlFlag("REQUIRED");
    Map<String, String> options = new HashMap<>();
    options.put("useKeyTab", "true");
    options.put("storeKey", "true");
    options.put("keyTab", "/etc/security/keytabs/kafka_client.keytab");
    options.put("principal", "[email protected]");
    jaasConfig.setOptions(options);
    return jaasConfig;
}
```

[Handling Exceptions](#kafka-annotation-error-handling)
[Kafka Queues (Share Consumer)](#kafka-kafka-queues)

---

<a id="kafka-kafka-queues"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/kafka/kafka-queues.html -->

<!-- page_index: 49 -->

# Kafka Queues (Share Consumer)

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="kafka-kafka-queues--page-title"></a>
<a id="kafka-kafka-queues--kafka-queues-share-consumer"></a>

# Kafka Queues (Share Consumer)

Starting with version 4.0, Spring for Apache Kafka provides support for Kafka Queues through share consumers, implementing [KIP-932 (Queues for Kafka)](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka).
As of Spring for Apache Kafka 4.1, backed by Apache Kafka 4.2, share consumers are promoted to full production support.

Kafka Queues enable a different consumption model compared to traditional consumer groups.
Instead of the partition-based assignment model where each partition is exclusively assigned to one consumer, share consumers can cooperatively consume from the same partitions, with records being distributed among the consumers in the share group.

<a id="kafka-kafka-queues--share-consumer-factory"></a>

## Share Consumer Factory

The `ShareConsumerFactory` is responsible for creating share consumer instances.
Spring Kafka provides the `DefaultShareConsumerFactory` implementation.

<a id="kafka-kafka-queues--share-consumer-factory-configuration"></a>
<a id="kafka-kafka-queues--configuration"></a>

### Configuration

You can configure a `DefaultShareConsumerFactory` similar to how you configure a regular `ConsumerFactory`:

```java
@Bean
public ShareConsumerFactory<String, String> shareConsumerFactory() {
    Map<String, Object> props = new HashMap<>();
    props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
    props.put(ConsumerConfig.GROUP_ID_CONFIG, "my-share-group");
    props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
    props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
    return new DefaultShareConsumerFactory<>(props);
}
```

<a id="kafka-kafka-queues--share-consumer-factory-constructors"></a>
<a id="kafka-kafka-queues--constructor-options"></a>

### Constructor Options

The `DefaultShareConsumerFactory` provides several constructor options:

```java
// Basic configuration
new DefaultShareConsumerFactory<>(configs);

// With deserializer suppliers
new DefaultShareConsumerFactory<>(configs, keyDeserializerSupplier, valueDeserializerSupplier);

// With deserializer instances
new DefaultShareConsumerFactory<>(configs, keyDeserializer, valueDeserializer, configureDeserializers);
```

<a id="kafka-kafka-queues--share-consumer-factory-deserializers"></a>
<a id="kafka-kafka-queues--deserializer-configuration"></a>

### Deserializer Configuration

You can configure deserializers in several ways:

1. **Via Configuration Properties** (recommended for simple cases):


```java
props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
```

2. **Via Setters**:


```java
factory.setKeyDeserializer(new StringDeserializer());
factory.setValueDeserializer(new StringDeserializer());
```

3. **Via Suppliers** (for cases where deserializers need to be created per consumer):


```java
factory.setKeyDeserializerSupplier(() -> new StringDeserializer());
factory.setValueDeserializerSupplier(() -> new StringDeserializer());
```

Set `configureDeserializers` to `false` if your deserializers are already fully configured and should not be reconfigured by the factory.

<a id="kafka-kafka-queues--share-consumer-factory-listeners"></a>
<a id="kafka-kafka-queues--lifecycle-listeners"></a>

### Lifecycle Listeners

You can add listeners to monitor the lifecycle of share consumers:

```java
factory.addListener(new ShareConsumerFactory.Listener<String, String>() {@Override public void consumerAdded(String id, ShareConsumer<String, String> consumer) {// Called when a new consumer is created System.out.println("Consumer added: " + id);}
@Override public void consumerRemoved(String id, ShareConsumer<String, String> consumer) {// Called when a consumer is closed System.out.println("Consumer removed: " + id);} });
```

<a id="kafka-kafka-queues--share-message-listener-containers"></a>

## Share Message Listener Containers

<a id="kafka-kafka-queues--share-kafka-message-listener-container"></a>
<a id="kafka-kafka-queues--sharekafkamessagelistenercontainer"></a>

### ShareKafkaMessageListenerContainer

The `ShareKafkaMessageListenerContainer` provides a container for share consumers with support for concurrent processing:

```java
@Bean
public ShareKafkaMessageListenerContainer<String, String> container(
        ShareConsumerFactory<String, String> shareConsumerFactory) {

    ContainerProperties containerProps = new ContainerProperties("my-topic");
    containerProps.setGroupId("my-share-group");

    ShareKafkaMessageListenerContainer<String, String> container =
        new ShareKafkaMessageListenerContainer<>(shareConsumerFactory, containerProps);

    container.setupMessageListener(new MessageListener<String, String>() {
        @Override
        public void onMessage(ConsumerRecord<String, String> record) {
            System.out.println("Received: " + record.value());
        }
    });

    return container;
}
```

<a id="kafka-kafka-queues--share-container-properties"></a>
<a id="kafka-kafka-queues--container-properties"></a>

### Container Properties

Share containers support a subset of the container properties available for regular consumers:

- `topics`: Array of topic names to subscribe to
- `groupId`: The share group ID
- `clientId`: The client ID for the consumer
- `shareAckMode`: The acknowledgment mode (`EXPLICIT`, `MANUAL`, or `IMPLICIT`; see [Record Acknowledgment](#kafka-kafka-queues--share-record-acknowledgment))
- `shareAcknowledgmentTimeout`: Timeout for detecting unacknowledged records in `MANUAL` mode
- `syncShareCommits`: Whether to use `commitSync()` (default) or `commitAsync()` for share consumer acknowledgments (see [Synchronous vs Asynchronous Commits](#kafka-kafka-queues--share-sync-async-commits))
- `kafkaConsumerProperties`: Additional consumer properties

> [!IMPORTANT]
> Share consumers do not support:
>
> - Explicit partition assignment (`TopicPartitionOffset`)
> - Topic patterns
> - Manual offset management

<a id="kafka-kafka-queues--share-container-lifecycle-events"></a>
<a id="kafka-kafka-queues--lifecycle-events"></a>

### Lifecycle Events

The `ShareKafkaMessageListenerContainer` publishes Spring application events across the consumer lifecycle:

- `ConsumerStartingEvent`: published when a share consumer thread is first started, before it starts polling.
- `ConsumerStartedEvent`: published when a share consumer is about to start polling.
- `ConsumerFailedToStartEvent`: published when a share consumer fails to start (for example, the underlying `ShareConsumer` could not be created).
  Any already-constructed `ShareConsumer` instances from the same startup attempt are closed quietly and do not publish stopping or stopped events because they never reached the poll loop.
- `ShareConsumerStoppingEvent`: published by each share consumer just before its underlying `ShareConsumer` is closed.
  Unlike `ConsumerStoppingEvent`, this event carries a `ShareConsumer` reference (not a `Consumer`) because `ShareConsumer` is a separate client API and is not assigned to specific partitions.
- `ConsumerStoppedEvent`: published after the share consumer is closed, with a `reason`:

  - `NORMAL` - the container was stopped.
  - `ABNORMAL` - the consumer thread exited because of an `Exception`.
  - `ERROR` - a `java.lang.Error` was thrown.

These events can be consumed with `@EventListener` (see [Event Consumption](#kafka-events--event-consumption)) to integrate share containers with the same monitoring and restart patterns available for regular containers.

<a id="kafka-kafka-queues--share-container-concurrency"></a>
<a id="kafka-kafka-queues--concurrency"></a>

### Concurrency

The `ShareKafkaMessageListenerContainer` supports concurrent processing by creating multiple consumer threads within a single container.
Each thread runs its own `ShareConsumer` instance that participates in the same share group.

Unlike traditional consumer groups where concurrency involves partition distribution, share consumers leverage Kafka’s record-level distribution at the broker.
This means multiple consumer threads in the same container work together as part of the share group, with the Kafka broker distributing records across all consumer instances.

> [!IMPORTANT]
> **Concurrency is Additive Across Application Instances**
>
> From the share group’s perspective, each `ShareConsumer` instance is an independent member, regardless of where it runs.
> Setting `concurrency=3` in a single container creates 3 share group members.
> If you run multiple application instances with the same share group ID, all their consumer threads combine into one pool.
>
> For example:
> \* Application Instance 1: `concurrency=3` → 3 share group members
> \* Application Instance 2: `concurrency=3` → 3 share group members
> \* **Total**: 6 share group members available for the broker to distribute records to
>
> This means setting `concurrency=5` in a single container is operationally equivalent to running 5 separate application instances with `concurrency=1` each (all using the same `group.id`).
> The Kafka broker treats all consumer instances equally and distributes records across the entire pool.

<a id="kafka-kafka-queues--_configuring_concurrency_programmatically"></a>
<a id="kafka-kafka-queues--configuring-concurrency-programmatically"></a>

#### Configuring Concurrency Programmatically

```java
@Bean
public ShareKafkaMessageListenerContainer<String, String> concurrentContainer(
        ShareConsumerFactory<String, String> shareConsumerFactory) {

    ContainerProperties containerProps = new ContainerProperties("my-topic");
    containerProps.setGroupId("my-share-group");

    ShareKafkaMessageListenerContainer<String, String> container =
        new ShareKafkaMessageListenerContainer<>(shareConsumerFactory, containerProps);

    // Set concurrency to create 5 consumer threads
    container.setConcurrency(5);

    container.setupMessageListener(new MessageListener<String, String>() {
        @Override
        public void onMessage(ConsumerRecord<String, String> record) {
            System.out.println("Received on " + Thread.currentThread().getName() + ": " + record.value());
        }
    });

    return container;
}
```

<a id="kafka-kafka-queues--_configuring_concurrency_via_factory"></a>
<a id="kafka-kafka-queues--configuring-concurrency-via-factory"></a>

#### Configuring Concurrency via Factory

You can set default concurrency at the factory level, which applies to all containers created by that factory:

```java
@Bean
public ShareKafkaListenerContainerFactory<String, String> shareKafkaListenerContainerFactory(
        ShareConsumerFactory<String, String> shareConsumerFactory) {

    ShareKafkaListenerContainerFactory<String, String> factory =
        new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);

    // Set default concurrency for all containers created by this factory
    factory.setConcurrency(3);

    return factory;
}
```

<a id="kafka-kafka-queues--_per_listener_concurrency"></a>
<a id="kafka-kafka-queues--per-listener-concurrency"></a>

#### Per-Listener Concurrency

The concurrency setting can be overridden per listener using the `concurrency` attribute:

```java
@Component public class ConcurrentShareListener {
@KafkaListener(topics = "high-throughput-topic",containerFactory = "shareKafkaListenerContainerFactory",groupId = "my-share-group",concurrency = "10"  // Override factory default) public void listen(ConsumerRecord<String, String> record) {// This listener will use 10 consumer threads System.out.println("Processing: " + record.value());}}
```

<a id="kafka-kafka-queues--_concurrency_considerations"></a>
<a id="kafka-kafka-queues--concurrency-considerations"></a>

#### Concurrency Considerations

- **Thread Safety**: Each consumer thread has its own `ShareConsumer` instance and manages its own acknowledgments independently
- **Client IDs**: Each consumer thread receives a unique client ID with a numeric suffix (e.g., `myContainer-0`, `myContainer-1`, etc.)
- **Metrics**: Metrics from all consumer threads are aggregated and accessible via `container.metrics()`
- **Lifecycle**: All consumer threads start and stop together as a unit
- **Work Distribution**: The Kafka broker handles record distribution across all consumer instances in the share group
- **Acknowledgment**: Each thread independently manages acknowledgments for its own records; unacknowledged records in one thread do not block other threads

<a id="kafka-kafka-queues--_concurrency_with_manual_acknowledgment"></a>
<a id="kafka-kafka-queues--concurrency-with-manual-acknowledgment"></a>

#### Concurrency with MANUAL Acknowledgment

Concurrency works seamlessly with `ShareAckMode.MANUAL`.
Each consumer thread independently tracks and acknowledges its own records:

```java
@KafkaListener(topics = "order-queue",containerFactory = "manualShareKafkaListenerContainerFactory",groupId = "order-processors",concurrency = "5") public void processOrder(ConsumerRecord<String, String> record, ShareAcknowledgment acknowledgment) {try {processOrderLogic(record.value()); acknowledgment.acknowledge(); // ACCEPT} catch (RetryableException e) {acknowledgment.release(); // Will be redelivered} catch (Exception e) {acknowledgment.reject(); // Permanent failure}}
```

> [!NOTE]
> **Record Acquisition and Distribution Behavior:**
>
> Share consumers use a pull-based model where each consumer thread calls `poll()` to fetch records from the broker.
> When a consumer polls, the broker’s share-partition leader:
>
> - Selects records in "Available" state
> - Moves them to "Acquired" state with a time-limited acquisition lock (default 30 seconds, configurable via `group.share.record.lock.duration.ms`)
> - Prefers to return complete record batches for efficiency
> - Applies `max.poll.records` as a soft limit by default, meaning complete record batches will be acquired even if it exceeds this value
>
> ===== Acquire Mode (KIP-1206)
>
> Apache Kafka 4.2 introduces the `share.acquire.mode` consumer property that controls how strictly `max.poll.records` is enforced:
>
> - `batch_optimized` (default) — soft limit.
>   The broker may return more records than `max.poll.records` to align with batch boundaries for better throughput.
> - `record_limit` — strict limit.
>   The broker will never return more records than `max.poll.records` per `poll()` call.
>   Useful when you need precise control over memory usage or processing rate.
>
> This is a pass-through consumer property.
> Configure it directly in the consumer properties:
>
> ```java
> Map<String, Object> props = new HashMap<>();
> props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
> props.put("share.acquire.mode", "record_limit");
> props.put("max.poll.records", 5);
> // ... other properties
>
> DefaultShareConsumerFactory<String, String> factory = new DefaultShareConsumerFactory<>(props);
> ```
>
> > [!NOTE]
> > No additional Spring Kafka configuration is needed.
> > The property is passed directly to the underlying `KafkaShareConsumer`.
>
> While records are acquired by one consumer, they are not available to other consumers.
> When the acquisition lock expires, unacknowledged records automatically return to "Available" state and can be delivered to another consumer.
>
> The broker limits the number of records that can be acquired per partition using `group.share.partition.max.record.locks`.
> Once this limit is reached, subsequent polls temporarily return no records until locks expire.
>
> **Implications for Concurrency:**
>
> - Each consumer thread independently polls and may acquire different numbers of records per poll
> - Record distribution across threads depends on polling timing and batch availability
> - Multiple threads increase the pool of consumers available to acquire records
> - With low message volume or single partitions, records may concentrate on fewer threads
> - For long-running workloads, distribution tends to be more even
>
> **Configuration:**
>
> - Each thread polls and processes records independently
> - Acknowledgment constraints apply per-thread (one thread’s unacknowledged records don’t block other threads)
> - Concurrency setting must be greater than 0 and cannot be changed while the container is running

<a id="kafka-kafka-queues--share-annotation-driven-listeners"></a>
<a id="kafka-kafka-queues--annotation-driven-listeners"></a>

## Annotation-Driven Listeners

<a id="kafka-kafka-queues--share-kafka-listener"></a>
<a id="kafka-kafka-queues--kafkalistener-with-share-consumers"></a>

### @KafkaListener with Share Consumers

You can use `@KafkaListener` with share consumers by configuring a `ShareKafkaListenerContainerFactory`:

```java
@Configuration
@EnableKafka
public class ShareConsumerConfig {

    @Bean
    public ShareConsumerFactory<String, String> shareConsumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        return new DefaultShareConsumerFactory<>(props);
    }

    @Bean
    public ShareKafkaListenerContainerFactory<String, String> shareKafkaListenerContainerFactory(
            ShareConsumerFactory<String, String> shareConsumerFactory) {
        return new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);
    }
}
```

Then use it in your listener:

```java
@Component public class ShareMessageListener {
@KafkaListener(topics = "my-queue-topic",containerFactory = "shareKafkaListenerContainerFactory",groupId = "my-share-group") public void listen(ConsumerRecord<String, String> record) {System.out.println("Received from queue: " + record.value()); // Record is automatically acknowledged with ACCEPT}}
```

<a id="kafka-kafka-queues--share-group-offset-reset"></a>

### Share Group Offset Reset

Unlike regular consumer groups, share groups use a different configuration for offset reset behavior.
You can configure this programmatically:

```java
private void configureShareGroup(String bootstrapServers, String groupId) throws Exception {Map<String, Object> adminProps = new HashMap<>(); adminProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
try (Admin admin = Admin.create(adminProps)) {ConfigResource configResource = new ConfigResource(ConfigResource.Type.GROUP, groupId); ConfigEntry configEntry = new ConfigEntry("share.auto.offset.reset", "earliest");
Map<ConfigResource, Collection<AlterConfigOp>> configs = Map.of(configResource, List.of(new AlterConfigOp(configEntry, AlterConfigOp.OpType.SET)) );
admin.incrementalAlterConfigs(configs).all().get();}}
```

<a id="kafka-kafka-queues--share-record-acknowledgment"></a>
<a id="kafka-kafka-queues--record-acknowledgment"></a>

## Record Acknowledgment

Spring Kafka exposes three acknowledgment modes through `ContainerProperties.ShareAckMode`, controlling how records are acknowledged after processing.

<a id="kafka-kafka-queues--share-ack-mode-explicit"></a>
<a id="kafka-kafka-queues--explicit-default-:-container-managed-acknowledgment"></a>

### EXPLICIT (Default): Container-Managed Acknowledgment

In `EXPLICIT` mode the container takes full responsibility for acknowledgment.
After the listener returns normally, the container sends `ACCEPT` for the record.
On listener exceptions, the [`ShareConsumerRecordRecoverer`](#kafka-kafka-queues--share-error-handling) decides the outcome (`ACCEPT`, `RELEASE`, or `REJECT`; default: `REJECT`).
This is the closest analogue to disabling `auto.commit` on a regular consumer — the container manages all acknowledgment decisions without any listener involvement.

This is the default mode; no additional configuration is required:

```java
@Bean
public ShareKafkaListenerContainerFactory<String, String> shareKafkaListenerContainerFactory(
        ShareConsumerFactory<String, String> shareConsumerFactory) {
    // EXPLICIT is the default — no shareAckMode configuration needed
    return new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);
}
```

```java
@KafkaListener(topics = "my-queue-topic", containerFactory = "shareKafkaListenerContainerFactory",
               groupId = "my-share-group")
public void listen(ConsumerRecord<String, String> record) {
    // Container sends ACCEPT on success; recoverer decides on error (default: REJECT)
    process(record.value());
}
```

<a id="kafka-kafka-queues--share-ack-mode-manual"></a>
<a id="kafka-kafka-queues--manual:-listener-managed-acknowledgment"></a>

### MANUAL: Listener-Managed Acknowledgment

In `MANUAL` mode the listener drives every per-record acknowledgment decision.
Each record is delivered with a non-null `ShareAcknowledgment` instance that the listener must call exactly once with a terminal operation (`acknowledge()`, `release()`, or `reject()`).
Subsequent polls are blocked until all records from the previous poll are acknowledged.

Use `MANUAL` mode when your business logic determines the acknowledgment outcome record by record.

```java
@Bean
public ShareKafkaListenerContainerFactory<String, String> manualShareKafkaListenerContainerFactory(
        ShareConsumerFactory<String, String> shareConsumerFactory) {
    ShareKafkaListenerContainerFactory<String, String> factory =
        new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);
    factory.getContainerProperties().setShareAckMode(ContainerProperties.ShareAckMode.MANUAL);
    return factory;
}
```

The listener must accept a `ShareAcknowledgment` parameter (that is, implement `AcknowledgingShareConsumerAwareMessageListener`):

```java
@KafkaListener(topics = "order-queue", containerFactory = "manualShareKafkaListenerContainerFactory") public void processOrder(ConsumerRecord<String, String> record, ShareAcknowledgment acknowledgment) {try {processOrderLogic(record.value()); acknowledgment.acknowledge(); // ACCEPT — success} catch (TransientException e) {acknowledgment.release();     // RELEASE — redelivery} catch (Exception e) {acknowledgment.reject();      // REJECT — permanent failure}}
```

> [!IMPORTANT]
> `ShareAckMode.MANUAL` requires the listener to accept a `ShareAcknowledgment` parameter
> (that is, implement `AcknowledgingShareConsumerAwareMessageListener`).
> The container validates this at startup and throws `IllegalStateException` if a plain `MessageListener` is used.

<a id="kafka-kafka-queues--share-ack-mode-implicit"></a>
<a id="kafka-kafka-queues--implicit:-kafka-client-implicit-mode"></a>

### IMPLICIT: Kafka Client Implicit Mode

In `IMPLICIT` mode, acknowledgment is delegated entirely to the Kafka broker, which automatically accepts all acquired records regardless of processing outcome.
No per-record acknowledgment API is available; the `ShareAcknowledgment` argument is always `null`.
This maps directly to setting `share.acknowledgement.mode=implicit` in the Kafka client configuration.

```java
@Bean
public ShareKafkaListenerContainerFactory<String, String> implicitShareKafkaListenerContainerFactory(
        ShareConsumerFactory<String, String> shareConsumerFactory) {
    ShareKafkaListenerContainerFactory<String, String> factory =
        new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);
    factory.getContainerProperties().setShareAckMode(ContainerProperties.ShareAckMode.IMPLICIT);
    return factory;
}
```

> [!WARNING]
> In `IMPLICIT` mode the `ShareConsumerRecordRecoverer` is not consulted.
> Processing errors are silently absorbed from the broker’s perspective — all records are always ACCEPTed.
> Use this mode only when per-record delivery guarantees are not required.

<a id="kafka-kafka-queues--share-ack-mode-comparison"></a>
<a id="kafka-kafka-queues--acknowledgment-mode-comparison"></a>

### Acknowledgment Mode Comparison

| Mode | Who acknowledges | On success | On listener error |
| --- | --- | --- | --- |
| `EXPLICIT` (default) | Container | Container sends `ACCEPT` | Recoverer decides (`REJECT` by default) |
| `MANUAL` | Listener code | Listener calls `acknowledge()` | Listener calls `release()` or `reject()` |
| `IMPLICIT` | Kafka broker | Broker auto-ACCEPTs | Broker auto-ACCEPTs (no recovery) |

<a id="kafka-kafka-queues--share-ack-mode-migration"></a>
<a id="kafka-kafka-queues--migration-from-4.0"></a>

### Migration from 4.0

In 4.0, share consumer acknowledgment was controlled by `setExplicitShareAcknowledgment(boolean)`.
In 4.1, this is replaced by `setShareAckMode(ShareAckMode)`.
The deprecated method still works: `true` maps to `MANUAL`, `false` maps to `EXPLICIT`.

**Default behavior is unchanged.**
The 4.0 default (`setExplicitShareAcknowledgment(false)`) was container-managed acknowledgment, which is exactly what `ShareAckMode.EXPLICIT` does.
No action is required for applications using the default.

**If you used `setExplicitShareAcknowledgment(true)`**, replace it:

```java
// Before (4.0)
factory.getContainerProperties().setExplicitShareAcknowledgment(true);

// After (4.1)
factory.getContainerProperties().setShareAckMode(ContainerProperties.ShareAckMode.MANUAL);
```

**If you set `share.acknowledgement.mode=implicit` in the factory configuration** (via `ConsumerConfig.SHARE_ACKNOWLEDGEMENT_MODE_CONFIG`), note that in 4.0 this setting had no effect because the container always called `consumer.acknowledge()` regardless.
In 4.1, the container detects this conflict, logs a warning, and overrides the factory setting with explicit mode.
To use Kafka client implicit mode, set it explicitly on the container:

```java
factory.getContainerProperties().setShareAckMode(ContainerProperties.ShareAckMode.IMPLICIT);
```

<a id="kafka-kafka-queues--share-acknowledgment-types"></a>
<a id="kafka-kafka-queues--acknowledgment-types"></a>

### Acknowledgment Types

Share consumers support four acknowledgment types:

- `ACCEPT` — Record processed successfully; mark as completed.
- `RELEASE` — Temporary failure; make the record available for redelivery to this or another consumer.
- `REJECT` — Permanent failure; archive the record and do not redeliver.
- `RENEW` — Extend the acquisition lock (non-terminal).
  Use `renew()` when processing may exceed the broker’s lock duration (`group.share.record.lock.duration.ms`, default 30 seconds).
  A terminal acknowledgment (`acknowledge()`, `release()`, or `reject()`) is still required.

<a id="kafka-kafka-queues--share-acknowledgment-api"></a>
<a id="kafka-kafka-queues--shareacknowledgment-api"></a>

### ShareAcknowledgment API

The `ShareAcknowledgment` interface is only non-null in `ShareAckMode.MANUAL` mode:

```java
public interface ShareAcknowledgment {
    void acknowledge(); // ACCEPT — record successfully processed
    void release();     // RELEASE — redelivery on transient failure
    void reject();      // REJECT — permanent failure, do not retry
    void renew();       // RENEW (non-terminal) — extend acquisition lock
}
```

<a id="kafka-kafka-queues--share-listener-interfaces"></a>
<a id="kafka-kafka-queues--listener-interfaces"></a>

### Listener Interfaces

<a id="kafka-kafka-queues--share-basic-listener"></a>
<a id="kafka-kafka-queues--basic-message-listener"></a>

#### Basic Message Listener

Use the standard `MessageListener` in `EXPLICIT` (default) or `IMPLICIT` mode:

```java
@KafkaListener(topics = "my-topic", containerFactory = "shareKafkaListenerContainerFactory")
public void listen(ConsumerRecord<String, String> record) {
    // In EXPLICIT mode (default): container sends ACCEPT on success, REJECT on error
    process(record.value());
}
```

<a id="kafka-kafka-queues--share-acknowledging-listener"></a>
<a id="kafka-kafka-queues--acknowledgingshareconsumerawaremessagelistener"></a>

#### AcknowledgingShareConsumerAwareMessageListener

This interface provides access to the `ShareConsumer` instance and, in `MANUAL` mode, to the `ShareAcknowledgment`.
The `acknowledgment` parameter is non-null only in `MANUAL` mode; it is `null` in `EXPLICIT` and `IMPLICIT` modes.

<a id="kafka-kafka-queues--_explicit_mode_default_acknowledgment_is_null"></a>
<a id="kafka-kafka-queues--explicit-mode-default-acknowledgment-is-null"></a>

##### EXPLICIT Mode (Default — acknowledgment is null)

```java
@KafkaListener(
    topics = "my-topic",
    containerFactory = "shareKafkaListenerContainerFactory"  // EXPLICIT by default
)
public void listen(ConsumerRecord<String, String> record,
                  @Nullable ShareAcknowledgment acknowledgment,
                  ShareConsumer<?, ?> consumer) {

    // acknowledgment is null in EXPLICIT mode — container handles ACCEPT/REJECT automatically
    process(record.value());

    // Access consumer metrics if needed
    Map<MetricName, ? extends Metric> metrics = consumer.metrics();
}
```

<a id="kafka-kafka-queues--_manual_mode_acknowledgment_is_non_null"></a>
<a id="kafka-kafka-queues--manual-mode-acknowledgment-is-non-null"></a>

##### MANUAL Mode (acknowledgment is non-null)

```java
@KafkaListener(topics = "my-topic",containerFactory = "manualShareKafkaListenerContainerFactory" // ShareAckMode.MANUAL) public void listen(ConsumerRecord<String, String> record,@Nullable ShareAcknowledgment acknowledgment,ShareConsumer<?, ?> consumer) {
// acknowledgment is non-null in MANUAL mode try {processRecord(record); acknowledgment.acknowledge(); // ACCEPT} catch (RetryableException e) {acknowledgment.release(); // Will be redelivered} catch (Exception e) {acknowledgment.reject(); // Permanent failure}}
```

<a id="kafka-kafka-queues--share-acknowledgment-constraints"></a>
<a id="kafka-kafka-queues--acknowledgment-constraints-manual-mode"></a>

### Acknowledgment Constraints (MANUAL Mode)

In `ShareAckMode.MANUAL`, the container enforces the following constraints:

- **Poll Blocking**: Subsequent polls are blocked until all records from the previous poll are acknowledged.
- **Terminal Acknowledgment**: Each record must receive exactly one terminal acknowledgment (`acknowledge()`, `release()`, or `reject()`).
  You may call `renew()` zero or more times before that to extend the acquisition lock.
- **Error Handling**: If processing throws an exception, the outcome is determined by the [ShareConsumerRecordRecoverer](#kafka-kafka-queues--share-error-handling) (default: `REJECT`).

> [!WARNING]
> In `ShareAckMode.MANUAL`, failing to acknowledge records will block further message processing.
> Always ensure records are acknowledged in all code paths, including exception handlers.

<a id="kafka-kafka-queues--share-acknowledgment-timeout"></a>
<a id="kafka-kafka-queues--acknowledgment-timeout-detection"></a>

#### Acknowledgment Timeout Detection

To help identify missing acknowledgments, Spring Kafka provides configurable timeout detection in `MANUAL` mode.
When a record is not acknowledged within the specified timeout, a warning is logged with details about the unacknowledged record.

```java
@Bean
public ShareKafkaListenerContainerFactory<String, String> manualShareKafkaListenerContainerFactory(
    ShareConsumerFactory<String, String> shareConsumerFactory) {
    ShareKafkaListenerContainerFactory<String, String> factory =
        new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);
    factory.getContainerProperties().setShareAckMode(ContainerProperties.ShareAckMode.MANUAL);

    // Set acknowledgment timeout (default is 30 seconds)
    factory.getContainerProperties().setShareAcknowledgmentTimeout(Duration.ofSeconds(30));

    return factory;
}
```

When a record exceeds the timeout, you’ll see a warning like:

```
WARN: Record not acknowledged within timeout (30 seconds).
In ShareAckMode.MANUAL you must call ack.acknowledge(), ack.release(),
or ack.reject() for every record (call ack.renew() to extend the lock; a terminal ack is still required).
Unacknowledged record: topic='my-topic', partition=0, offset=42
```

This feature helps identify missing acknowledgment calls before they cause "no new records consumed" symptoms due to blocked polls.

<a id="kafka-kafka-queues--share-sync-async-commits"></a>
<a id="kafka-kafka-queues--synchronous-vs-asynchronous-commits"></a>

### Synchronous vs Asynchronous Commits

By default, the share container uses `commitSync()` to ensure acknowledgments are durable before proceeding.
Set `syncShareCommits` to `false` to use `commitAsync()` when slightly relaxed ack-durability is acceptable in exchange for higher throughput.

```java
@Bean
public ShareKafkaListenerContainerFactory<String, String> asyncCommitFactory(
        ShareConsumerFactory<String, String> consumerFactory) {
    ShareKafkaListenerContainerFactory<String, String> factory =
        new ShareKafkaListenerContainerFactory<>(consumerFactory);
    factory.getContainerProperties().setSyncShareCommits(false); // use commitAsync()
    return factory;
}
```

| Property value | Kafka API called | Trade-off |
| --- | --- | --- |
| `true` (default) | `consumer.commitSync()` | Durable — acknowledgments are guaranteed persisted before the next poll |
| `false` | `consumer.commitAsync()` | Higher throughput — slight risk of redelivery if the consumer crashes before the async commit completes |

<a id="kafka-kafka-queues--share-error-handling"></a>
<a id="kafka-kafka-queues--error-handling"></a>

### Error Handling

The share container handles errors at two levels: during `poll()` (poll-level) and when the listener throws (listener-level).

<a id="kafka-kafka-queues--_poll_level_error_handling"></a>
<a id="kafka-kafka-queues--poll-level-error-handling"></a>

#### Poll-Level Error Handling

If `consumer.poll()` throws an exception, the container handles it so the consumer thread does not stop:

- **RecordDeserializationException**: Thrown when a record cannot be deserialized (for example, invalid UTF-8 for `StringDeserializer`).
  The container catches it, logs a warning, and continues polling.
  In `EXPLICIT` and `MANUAL` modes, the container REJECTs the affected record using the topic, partition, and offset from the exception.
  In `IMPLICIT` mode no explicit acknowledgment call is made — the broker auto-accepts the record.
  Subsequent records are processed normally.
- **CorruptRecordException**: Thrown when CRC validation fails (for example, with `check.crcs` enabled).
  The Kafka client automatically rejects the corrupt batch.
  The container catches the exception, logs it, and continues polling.

Without this handling, a single bad record would terminate the consumer thread.

<a id="kafka-kafka-queues--_listener_level_error_handling_shareconsumerrecordrecoverer"></a>
<a id="kafka-kafka-queues--listener-level-error-handling:-shareconsumerrecordrecoverer"></a>

#### Listener-Level Error Handling: ShareConsumerRecordRecoverer

When the listener throws an exception, the container delegates to a `ShareConsumerRecordRecoverer` to decide whether to ACCEPT, RELEASE, or REJECT the failed record.
The default is `ShareConsumerRecordRecoverer.REJECTING` (log and REJECT); `ShareConsumerRecordRecoverer.RELEASING` is also available (log and RELEASE for redelivery).

You can provide a custom recoverer to RELEASE records for transient failures (for example, downstream timeouts) so they can be redelivered to another consumer, while REJECTing permanent failures.

<a id="kafka-kafka-queues--_configuring_a_custom_recoverer"></a>
<a id="kafka-kafka-queues--configuring-a-custom-recoverer"></a>

##### Configuring a Custom Recoverer

Set the recoverer on the container or on the factory so it applies to all containers created by that factory:

```java
@Bean public ShareKafkaListenerContainerFactory<String, String> shareKafkaListenerContainerFactory(ShareConsumerFactory<String, String> shareConsumerFactory) {
ShareKafkaListenerContainerFactory<String, String> factory =new ShareKafkaListenerContainerFactory<>(shareConsumerFactory);
factory.setShareConsumerRecordRecoverer((record, ex) -> {if (ex instanceof TransientException || ex.getCause() instanceof TimeoutException) {return AcknowledgeType.RELEASE;} return AcknowledgeType.REJECT; });
return factory;}
```

You can also set the recoverer on an individual container via `container.setShareConsumerRecordRecoverer(recoverer)`.

<a id="kafka-kafka-queues--_recoverer_behavior"></a>
<a id="kafka-kafka-queues--recoverer-behavior"></a>

##### Recoverer Behavior

- The recoverer must not return `RENEW`; the container treats it as REJECT.
- If the recoverer itself throws, the container falls back to REJECT for that record.
- The default recoverer logs at `ERROR` and returns `REJECT` for every exception.

<a id="kafka-kafka-queues--_relation_to_poison_message_protection"></a>
<a id="kafka-kafka-queues--relation-to-poison-message-protection"></a>

##### Relation to Poison Message Protection

Broker-side delivery count (see [Poison Message Protection and Delivery Count](#kafka-kafka-queues--share-poison-message-protection)) limits how many times a record can be acquired.
Even if your recoverer always returns `RELEASE`, the broker will eventually archive the record after the configured limit (default 5), so poison messages cannot loop forever.

<a id="kafka-kafka-queues--_difference_from_traditional_container_error_handling"></a>
<a id="kafka-kafka-queues--difference-from-traditional-container-error-handling"></a>

#### Difference from Traditional Container Error Handling

Share consumers do not use `CommonErrorHandler`.
That interface is designed for partition-based consumers (seek, remaining records, offset commit).
Share consumers use acknowledgment-based recovery: the recoverer only decides ACCEPT, RELEASE, or REJECT; the container performs the acknowledgment.
There is no seek or dead-letter topic integration in the share container.

<a id="kafka-kafka-queues--share-acknowledgment-examples"></a>
<a id="kafka-kafka-queues--acknowledgment-examples-manual-mode"></a>

### Acknowledgment Examples (MANUAL Mode)

<a id="kafka-kafka-queues--share-mixed-acknowledgment-example"></a>
<a id="kafka-kafka-queues--mixed-acknowledgment-patterns"></a>

#### Mixed Acknowledgment Patterns

```java
@KafkaListener(topics = "order-processing", containerFactory = "manualShareKafkaListenerContainerFactory") public void processOrder(ConsumerRecord<String, String> record, ShareAcknowledgment acknowledgment) {String orderData = record.value(); try {if (isValidOrder(orderData)) {if (processOrder(orderData)) {acknowledgment.acknowledge(); // ACCEPT — success} else {acknowledgment.release(); // RELEASE — temporary failure, retry later}} else {acknowledgment.reject(); // REJECT — invalid order, don't retry}} catch (Exception e) {acknowledgment.reject(); // REJECT — unexpected failure}}
```

<a id="kafka-kafka-queues--share-conditional-acknowledgment-example"></a>
<a id="kafka-kafka-queues--conditional-acknowledgment"></a>

#### Conditional Acknowledgment

```java
@KafkaListener(topics = "data-validation", containerFactory = "manualShareKafkaListenerContainerFactory") public void validateData(ConsumerRecord<String, String> record, ShareAcknowledgment acknowledgment) {ValidationResult result = validator.validate(record.value()); switch (result.getStatus()) {case VALID -> acknowledgment.acknowledge();        // ACCEPT case INVALID_RETRYABLE -> acknowledgment.release(); // RELEASE case INVALID_PERMANENT -> acknowledgment.reject();  // REJECT}}
```

<a id="kafka-kafka-queues--share-poison-message-protection"></a>
<a id="kafka-kafka-queues--poison-message-protection-and-delivery-count"></a>

## Poison Message Protection and Delivery Count

KIP-932 includes broker-side poison message protection to prevent unprocessable records from being endlessly redelivered.

<a id="kafka-kafka-queues--_how_it_works"></a>
<a id="kafka-kafka-queues--how-it-works"></a>

### How It Works

Every time a record is acquired by a consumer in a share group, the broker increments an internal delivery count.
The first acquisition sets the delivery count to 1, and each subsequent acquisition increments it.
When the delivery count reaches the configured limit (default: 5), the record moves to **Archived** state and is not eligible for additional delivery attempts.

> [!IMPORTANT]
> **Delivery Count is Not Exposed to Applications**
> The delivery count is maintained internally by the broker and is **not exposed to consumer applications**.
> This is an intentional design decision in KIP-932.
> The delivery count is approximate and serves as a poison message protection mechanism, not a precise redelivery counter.
> Applications cannot query or access this value through any API.

For application-level retry logic, use the acknowledgment types:

- `RELEASE` - Make record available for redelivery (contributes to delivery count)
- `REJECT` - Mark as permanently failed (does not cause redelivery)
- `ACCEPT` - Successfully processed (does not cause redelivery)

The broker automatically prevents endless redelivery once `group.share.delivery.count.limit` is reached, moving the record to Archived state.

<a id="kafka-kafka-queues--_retry_strategy_recommendations"></a>
<a id="kafka-kafka-queues--retry-strategy-recommendations"></a>

### Retry Strategy Recommendations

Here is an example of how to use the various acknowledgement types based exception types.

```java
@KafkaListener(topics = "orders", containerFactory = "manualShareKafkaListenerContainerFactory")
public void processOrder(ConsumerRecord<String, String> record, ShareAcknowledgment ack) {
    try {
        // Attempt to process the order
        orderService.process(record.value());
        ack.acknowledge(); // ACCEPT - successfully processed
    }
    catch (TransientException e) {
        // Temporary failure (network issue, service unavailable, etc.)
        // Release the record for redelivery
        // Broker will retry up to group.share.delivery.count.limit times
        logger.warn("Transient error processing order, will retry: {}", e.getMessage());
        ack.release(); // RELEASE - make available for retry
    }
    catch (ValidationException e) {
        // Permanent semantic error (invalid data format, business rule violation, etc.)
        // Do not retry - this record will never succeed
        logger.error("Invalid order data, rejecting: {}", e.getMessage());
        ack.reject(); // REJECT - permanent failure, do not retry
    }
    catch (Exception e) {
        // Unknown error - typically safer to reject to avoid infinite loops
        // But could also release if you suspect it might be transient
        logger.error("Unexpected error processing order, rejecting: {}", e.getMessage());
        ack.reject(); // REJECT - avoid poison message loops
    }
}
```

The broker’s poison message protection ensures that even if you always use `RELEASE` for errors, records won’t be retried endlessly.
They will automatically be archived after reaching the delivery attempt limit.

<a id="kafka-kafka-queues--share-differences-from-regular-consumers"></a>
<a id="kafka-kafka-queues--differences-from-regular-consumers"></a>

## Differences from Regular Consumers

Share consumers differ from regular consumers in several key ways:

1. **No Partition Assignment**: Share consumers cannot be assigned specific partitions
2. **No Topic Patterns**: Share consumers do not support subscribing to topic patterns
3. **Cooperative Consumption**: Multiple consumers in the same share group can consume from the same partitions simultaneously
4. **Record-Level Acknowledgment**: Supports explicit acknowledgment with `ACCEPT`, `RELEASE`, and `REJECT` types
5. **Different Group Management**: Share groups use different coordinator protocols
6. **No Batch Processing**: Share consumers process records individually, not in batches
7. **Broker-Side Retry Management**: Delivery count tracking and poison message protection are managed by the broker, not exposed to applications

<a id="kafka-kafka-queues--share-limitations-and-considerations"></a>
<a id="kafka-kafka-queues--limitations-and-considerations"></a>

## Limitations and Considerations

<a id="kafka-kafka-queues--share-current-limitations"></a>
<a id="kafka-kafka-queues--current-limitations"></a>

### Current Limitations

- **No Message Converters**: Message converters are not yet supported for share consumers
- **No Batch Listeners**: Batch processing is not supported with share consumers
- **Poll Constraints**: In `ShareAckMode.MANUAL`, unacknowledged records block subsequent polls within each consumer thread

[JAAS and Kerberos](#kafka-kerberos)
[Non-Blocking Retries](#retrytopic)

---

<a id="retrytopic"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic.html -->

<!-- page_index: 50 -->

# Non-Blocking Retries

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic--page-title"></a>
<a id="retrytopic--non-blocking-retries"></a>

# Non-Blocking Retries

Version 2.9 changed the mechanism to bootstrap infrastructure beans; see [Configuration](#retrytopic-retry-config) for the two mechanisms that are now required to bootstrap the feature.

Achieving non-blocking retry / dlt functionality with Kafka usually requires setting up extra topics and creating and configuring the corresponding listeners.
Since 2.7 Spring for Apache Kafka offers support for that via the `@RetryableTopic` annotation and `RetryTopicConfiguration` class to simplify that bootstrapping.

Since 3.2, Spring for Apache Kafka supports non-blocking retries with [@KafkaListener on a Class](#kafka-receiving-messages-class-level-kafkalistener).

> [!IMPORTANT]
> Non-blocking retries are not supported with [Batch Listeners](#kafka-receiving-messages-listener-annotation--batch-listeners).

> [!IMPORTANT]
> Non-Blocking Retries cannot combine with [Container Transactions](#kafka-transactions--container-transaction-manager).

<a id="retrytopic--section-summary"></a>

## Section Summary

- [How the Pattern Works](#retrytopic-how-the-pattern-works)
- [Back Off Delay Precision](#retrytopic-back-off-delay-precision)
- [Configuration](#retrytopic-retry-config)
- [Programmatic Construction](#retrytopic-programmatic-construction)
- [Features](#retrytopic-features)
- [Combining Blocking and Non-Blocking Retries](#retrytopic-retry-topic-combine-blocking)
- [Accessing Delivery Attempts](#retrytopic-accessing-delivery-attempts)
- [Topic Naming](#retrytopic-topic-naming)
- [Multiple Listeners, Same Topic(s)](#retrytopic-multi-retry)
- [DLT Strategies](#retrytopic-dlt-strategies)
- [Specifying a ListenerContainerFactory](#retrytopic-retry-topic-lcf)
- [Accessing Topics' Information at Runtime](#retrytopic-access-topic-info-runtime)
- [Changing KafkaBackOffException Logging Level](#retrytopic-change-kboe-logging-level)

[Kafka Queues (Share Consumer)](#kafka-kafka-queues)
[How the Pattern Works](#retrytopic-how-the-pattern-works)

---

<a id="retrytopic-how-the-pattern-works"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/how-the-pattern-works.html -->

<!-- page_index: 51 -->

# How the Pattern Works

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-how-the-pattern-works--page-title"></a>
<a id="retrytopic-how-the-pattern-works--how-the-pattern-works"></a>

# How the Pattern Works

If message processing fails, the message is forwarded to a retry topic with a back off timestamp.
The retry topic consumer then checks the timestamp and if it’s not due it pauses the consumption for that topic’s partition.
When it is due the partition consumption is resumed, and the message is consumed again.
If the message processing fails again the message will be forwarded to the next retry topic, and the pattern is repeated until a successful processing occurs, or the attempts are exhausted, and the message is sent to the Dead Letter Topic (if configured).

To illustrate, if you have a "main-topic" topic, and want to set up non-blocking retry with an exponential backoff of 1000ms with a multiplier of 2 and 4 max attempts, it will create the main-topic-retry-1000, main-topic-retry-2000, main-topic-retry-4000 and main-topic-dlt topics and configure the respective consumers.
The framework also takes care of creating the topics and setting up and configuring the listeners.

> [!IMPORTANT]
> By using this strategy you lose Kafka’s ordering guarantees for that topic.

> [!IMPORTANT]
> You can set the `AckMode` mode you prefer, but `RECORD` is suggested.

When using a manual `AckMode` with `asyncAcks` set to true, the `DefaultErrorHandler` must be configured with `seekAfterError` set to `false`.
Starting with versions 2.9.10, 3.0.8, this will be set to `false` unconditionally for such configurations.
With earlier versions, it was necessary to override the `RetryTopicConfigurationSupport.configureCustomizers()` method to set the property to `false`.

```java
@Override
protected void configureCustomizers(CustomizersConfigurer customizersConfigurer) {
    customizersConfigurer.customizeErrorHandler(eh -> eh.setSeekAfterError(false));
}
```

In addition, before those versions, using the default (logging) DLT handler was not compatible with any kind of manual `AckMode`, regardless of the `asyncAcks` property.

[Non-Blocking Retries](#retrytopic)
[Back Off Delay Precision](#retrytopic-back-off-delay-precision)

---

<a id="retrytopic-back-off-delay-precision"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/back-off-delay-precision.html -->

<!-- page_index: 52 -->

# Back Off Delay Precision

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-back-off-delay-precision--page-title"></a>
<a id="retrytopic-back-off-delay-precision--back-off-delay-precision"></a>

# Back Off Delay Precision

<a id="retrytopic-back-off-delay-precision--overview-and-guarantees"></a>

## Overview and Guarantees

All message processing and backing off is handled by the consumer thread, and, as such, delay precision is guaranteed on a best-effort basis.
If one message’s processing takes longer than the next message’s back off period for that consumer, the next message’s delay will be higher than expected.
Also, for short delays (about 1s or less), the maintenance work the thread has to do, such as committing offsets, may delay the message processing execution.
The precision can also be affected if the retry topic’s consumer is handling more than one partition, because we rely on waking up the consumer from polling and having full pollTimeouts to make timing adjustments.

That being said, for consumers handling a single partition the message’s processing should occur approximately at its exact due time for most situations.

> [!IMPORTANT]
> It is guaranteed that a message will never be processed before its due time.

[How the Pattern Works](#retrytopic-how-the-pattern-works)
[Configuration](#retrytopic-retry-config)

---

<a id="retrytopic-retry-config"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/retry-config.html -->

<!-- page_index: 53 -->

# Configuration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-retry-config--page-title"></a>
<a id="retrytopic-retry-config--configuration"></a>

# Configuration

For the default setup, enable non-blocking retries by adding the `@RetryableTopic` annotation to a `@KafkaListener` method.
This is the recommended and simplest approach, as it automatically configures the required retry infrastructure and creates the retry and DLT topics with default settings.

To import the non-blocking retry infrastructure and expose its components as beans, annotate a `@Configuration` class with `@EnableKafkaRetryTopic`.
This enables injection and runtime lookup of the feature’s components and serves as a foundation for advanced and global configuration.

> [!NOTE]
> It is not necessary to also add `@EnableKafka`, if you add this annotation, because `@EnableKafkaRetryTopic` is meta-annotated with `@EnableKafka`.

For advanced and global customization, extend `RetryTopicConfigurationSupport` in a single `@Configuration` class and override the relevant methods.
For more details refer to [Configuring Global Settings and Features](#retrytopic-retry-config--retry-topic-global-settings).

By default, the containers for the retry topics will have the same concurrency as the main container.
Starting with version 3.0, you can set a different `concurrency` for the retry containers (either on the annotation, or in `RetryTopicConfigurationBuilder`).

> [!IMPORTANT]
> Use only one of the two global configuration approaches above (`@EnableKafkaRetryTopic` or extending `RetryTopicConfigurationSupport`).
> In addition, only one `@Configuration` class should extend `RetryTopicConfigurationSupport`.

<a id="retrytopic-retry-config--using-the-retryabletopic-annotation"></a>

## Using the `@RetryableTopic` annotation

To configure the retry topic and dlt for a `@KafkaListener` annotated method, you just have to add the `@RetryableTopic` annotation to it and Spring for Apache Kafka will bootstrap all the necessary topics and consumers with the default configurations.

```java
@RetryableTopic(kafkaTemplate = "myRetryableTopicKafkaTemplate")
@KafkaListener(topics = "my-annotated-topic", groupId = "myGroupId")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

Since 3.2, `@RetryableTopic` support for @KafkaListener on a class would be:

```java
@RetryableTopic(listenerContainerFactory = "my-retry-topic-factory") @KafkaListener(topics = "my-annotated-topic") public class ClassLevelRetryListener {
@KafkaHandler public void processMessage(MyPojo message) {// ... message processing}
}
```

You can specify a method in the same class to process the dlt messages by annotating it with the `@DltHandler` annotation.
If no DltHandler method is provided a default consumer is created which only logs the consumption.

```java
@DltHandler
public void processMessage(MyPojo message) {
    // ... message processing, persistence, etc
}
```

> [!NOTE]
> If you don’t specify a kafkaTemplate name a bean with name `defaultRetryTopicKafkaTemplate` will be looked up.
> If no bean is found an exception is thrown.

Starting with version 3.0, the `@RetryableTopic` annotation can be used as a meta-annotation on custom annotations; for example:

```java
@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@RetryableTopic
static @interface MetaAnnotatedRetryableTopic {

    @AliasFor(attribute = "concurrency", annotation = RetryableTopic.class)
    String parallelism() default "3";

}
```

<a id="retrytopic-retry-config--using-retrytopicconfiguration-beans"></a>

## Using `RetryTopicConfiguration` beans

You can also configure the non-blocking retry support by creating `RetryTopicConfiguration` beans in a `@Configuration` annotated class.

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, Object> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .create(template);
}
```

This will create retry topics and a dlt, as well as the corresponding consumers, for all topics in methods annotated with `@KafkaListener` using the default configurations. The `KafkaTemplate` instance is required for message forwarding.

To achieve more fine-grained control over how to handle non-blocking retrials for each topic, more than one `RetryTopicConfiguration` bean can be provided.

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .fixedBackOff(3000)
            .maxAttempts(5)
            .concurrency(1)
            .includeTopics(List.of("my-topic", "my-other-topic"))
            .create(template);
}

@Bean
public RetryTopicConfiguration myOtherRetryTopic(KafkaTemplate<String, MyOtherPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .exponentialBackoff(1000, 2, 5000)
            .maxAttempts(4)
            .excludeTopics(List.of("my-topic", "my-other-topic"))
            .retryOn(MyException.class)
            .create(template);
}
```

> [!NOTE]
> The retry topics' and dlt’s consumers will be assigned to a consumer group with a group id that is the combination of the one which you provide in the `groupId` parameter of the `@KafkaListener` annotation with the topic’s suffix.
> If you don’t provide any they’ll all belong to the same group, and rebalance on a retry topic will cause an unnecessary rebalance on the main topic.

> [!IMPORTANT]
> If the consumer is configured with an [`ErrorHandlingDeserializer`](#kafka-serdes--error-handling-deserializer), to handle deserialization exceptions, it is important to configure the `KafkaTemplate` and its producer with a serializer that can handle normal objects as well as raw `byte[]` values, which result from deserialization exceptions.
> The generic value type of the template should be `Object`.
> One technique is to use the `DelegatingByTypeSerializer`; an example follows:

```java
@Bean
public ProducerFactory<String, Object> producerFactory() {
    return new DefaultKafkaProducerFactory<>(producerConfiguration(), new StringSerializer(),
        new DelegatingByTypeSerializer(Map.of(byte[].class, new ByteArraySerializer(),
               MyNormalObject.class, new JacksonJsonSerializer<Object>())));
}

@Bean
public KafkaTemplate<String, Object> kafkaTemplate() {
    return new KafkaTemplate<>(producerFactory());
}
```

> [!IMPORTANT]
> Multiple `@KafkaListener` annotations can be used for the same topic with or without manual partition assignment along with non-blocking retries, but only one configuration will be used for a given topic.
> It’s best to use a single `RetryTopicConfiguration` bean for configuration of such topics; if multiple `@RetryableTopic` annotations are being used for the same topic, all of them should have the same values, otherwise one of them will be applied to all of that topic’s listeners and the other annotations' values will be ignored.

<a id="retrytopic-retry-config--retry-topic-global-settings"></a>
<a id="retrytopic-retry-config--configuring-global-settings-and-features"></a>

## Configuring Global Settings and Features

Since 2.9, the previous bean overriding approach for configuring components has been removed (without deprecation, due to the aforementioned experimental nature of the API).
This does not change the `RetryTopicConfiguration` beans approach - only infrastructure components' configurations.
Now the `RetryTopicConfigurationSupport` class should be extended in a (single) `@Configuration` class, and the proper methods overridden.
An example follows:

```java
@EnableKafka @Configuration public class MyRetryTopicConfiguration extends RetryTopicConfigurationSupport {
@Override protected void configureBlockingRetries(BlockingRetriesConfigurer blockingRetries) {blockingRetries .retryOn(MyBlockingRetriesException.class, MyOtherBlockingRetriesException.class) .backOff(new FixedBackOff(3000, 3));}
@Override protected void manageNonBlockingFatalExceptions(List<Class<? extends Throwable>> nonBlockingFatalExceptions) {nonBlockingFatalExceptions.add(MyNonBlockingException.class);}
@Override protected void configureCustomizers(CustomizersConfigurer customizersConfigurer) {// Use the new 2.9 mechanism to avoid re-fetching the same records after a pause customizersConfigurer.customizeErrorHandler(eh -> {eh.setSeekAfterError(false); });}
}
```

> [!IMPORTANT]
> When using this configuration approach, the `@EnableKafkaRetryTopic` annotation should not be used to prevent context failing to start due to duplicated beans.
> Use the simple `@EnableKafka` annotation instead.

When `autoCreateTopics` is true, the main and retry topics will be created with the specified number of partitions and replication factor.
Starting with version 3.0, the default replication factor is `-1`, meaning using the broker default.
If your broker version is earlier than 2.4, you will need to set an explicit value.
To override these values for a particular topic (e.g. the main topic or DLT), simply add a `NewTopic` `@Bean` with the required properties; that will override the auto creation properties.

> [!IMPORTANT]
> By default, records are published to the retry topic(s) using the original partition of the received record.
> If the retry topics have fewer partitions than the main topic, you should configure the framework appropriately; an example follows.

```java
@EnableKafka @Configuration public class Config extends RetryTopicConfigurationSupport {
@Override protected Consumer<DeadLetterPublishingRecovererFactory> configureDeadLetterPublishingContainerFactory() {return dlprf -> dlprf.setPartitionResolver((cr, nextTopic) -> null);}
...
}
```

The parameters to the function are the consumer record and the name of the next topic.
You can return a specific partition number, or `null` to indicate that the `KafkaProducer` should determine the partition.

By default, all values of retry headers (number of attempts, timestamps) are retained when a record transitions through the retry topics.
Starting with version 2.9.6, if you want to retain just the last value of these headers, use the `configureDeadLetterPublishingContainerFactory()` method shown above to set the factory’s `retainAllRetryHeaderValues` property to `false`.

<a id="retrytopic-retry-config--find-retry-topic-config"></a>
<a id="retrytopic-retry-config--find-retrytopicconfiguration"></a>

## Find RetryTopicConfiguration

Attempts to provide an instance of `RetryTopicConfiguration` by either creating one from a `@RetryableTopic` annotation, or from the bean container if no annotation is available.

If beans are found in the container, there’s a check to determine whether the provided topics should be handled by any of such instances.

If `@RetryableTopic` annotation is provided, a `DltHandler` annotated method is looked up.

since 3.2, provide new API to Create `RetryTopicConfiguration` when `@RetryableTopic` annotated on a class:

```java
@Bean public RetryTopicConfiguration myRetryTopic() {RetryTopicConfigurationProvider provider = new RetryTopicConfigurationProvider(beanFactory); return provider.findRetryConfigurationFor(topics, null, AnnotatedClass.class, bean);}
@RetryableTopic public static class AnnotatedClass {// NoOps}
```

[Back Off Delay Precision](#retrytopic-back-off-delay-precision)
[Programmatic Construction](#retrytopic-programmatic-construction)

---

<a id="retrytopic-programmatic-construction"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/programmatic-construction.html -->

<!-- page_index: 54 -->

# Programmatic Construction

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-programmatic-construction--page-title"></a>
<a id="retrytopic-programmatic-construction--programmatic-construction"></a>

# Programmatic Construction

The feature is designed to be used with `@KafkaListener`; however, several users have requested information on how to configure non-blocking retries programmatically.
The following Spring Boot application provides an example of how to do so.

```java
@SpringBootApplication public class Application extends RetryTopicConfigurationSupport {
public static void main(String[] args) {SpringApplication.run(Application.class, args);}
@Bean RetryTopicConfiguration retryConfig(KafkaTemplate<String, String> template) {return RetryTopicConfigurationBuilder.newInstance() .maxAttempts(4) .autoCreateTopicsWith(2, (short) 1) .create(template);}
@Bean TaskScheduler scheduler() {return new ThreadPoolTaskScheduler();}
@Bean @Order(0) SmartInitializingSingleton dynamicRetry(RetryTopicConfigurer configurer, RetryTopicConfiguration config,KafkaListenerAnnotationBeanPostProcessor<?, ?> bpp, KafkaListenerContainerFactory<?> factory,Listener listener, KafkaListenerEndpointRegistry registry) {
return () -> {KafkaListenerEndpointRegistrar registrar = bpp.getEndpointRegistrar(); MethodKafkaListenerEndpoint<String, String> mainEndpoint = new MethodKafkaListenerEndpoint<>(); EndpointProcessor endpointProcessor = endpoint -> {// customize as needed (e.g. apply attributes to retry endpoints).if (!endpoint.equals(mainEndpoint)) {endpoint.setConcurrency(1);} // these are required endpoint.setMessageHandlerMethodFactory(bpp.getMessageHandlerMethodFactory()); endpoint.setTopics("topic"); endpoint.setId("id"); endpoint.setGroupId("group"); }; mainEndpoint.setBean(listener); try {mainEndpoint.setMethod(Listener.class.getDeclaredMethod("onMessage", ConsumerRecord.class));} catch (NoSuchMethodException | SecurityException ex) {throw new IllegalStateException(ex);} mainEndpoint.setConcurrency(2); mainEndpoint.setTopics("topic"); mainEndpoint.setId("id"); mainEndpoint.setGroupId("group"); configurer.processMainAndRetryListeners(endpointProcessor, mainEndpoint, config, registrar, factory,"kafkaListenerContainerFactory"); };}
@Bean ApplicationRunner runner(KafkaTemplate<String, String> template) {return args -> {template.send("topic", "test"); };}
}
@Component class Listener implements MessageListener<String, String> {
@Override public void onMessage(ConsumerRecord<String, String> record) {System.out.println(KafkaUtils.format(record)); throw new RuntimeException("test");}
}
```

> [!IMPORTANT]
> Auto creation of topics will only occur if the configuration is processed before the application context is refreshed, as in the above example.
> To configure containers at runtime, the topics will need to be created using some other technique.

[Configuration](#retrytopic-retry-config)
[Features](#retrytopic-features)

---

<a id="retrytopic-features"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/features.html -->

<!-- page_index: 55 -->

# Features

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-features--page-title"></a>
<a id="retrytopic-features--features"></a>

# Features

Most of the features are available both for the `@RetryableTopic` annotation and the `RetryTopicConfiguration` beans.

<a id="retrytopic-features--backoff-configuration"></a>

## BackOff Configuration

The BackOff configuration relies on the `BackOffPolicy` interface from the `Spring Retry` project.

It includes:

- Fixed Back Off
- Exponential Back Off
- Random Exponential Back Off
- Uniform Random Back Off
- No Back Off
- Custom Back Off

```java
@RetryableTopic(attempts = 5,
    backOff = @BackOff(delay = 1000, multiplier = 2, maxDelay = 5000))
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .fixedBackOff(3_000)
            .maxAttempts(4)
            .create(template);
}
```

You can also provide a custom implementation of Spring Retry’s `SleepingBackOffPolicy` interface:

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .customBackoff(new MyCustomBackOffPolicy())
            .maxAttempts(5)
            .create(template);
}
```

> [!NOTE]
> The default back off policy is `FixedBackOffPolicy` with a maximum of 3 attempts and 1000ms intervals.

> [!NOTE]
> There is a 30-second default maximum delay for the `ExponentialBackOffPolicy`.
> If your back off policy requires delays with values bigger than that, adjust the `maxDelay` property accordingly.

> [!IMPORTANT]
> The first attempt counts against `maxAttempts`, so if you provide a `maxAttempts` value of 4 there’ll be the original attempt plus 3 retries.

<a id="retrytopic-features--global-timeout"></a>

## Global Timeout

You can set the global timeout for the retrying process.
If that time is reached, the next time the consumer throws an exception the message goes straight to the DLT, or just ends the processing if no DLT is available.

```java
@RetryableTopic(backOff = @BackOff(2_000), timeout = 5_000)
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .fixedBackOff(2_000)
            .timeoutAfter(5_000)
            .create(template);
}
```

> [!NOTE]
> The default is having no timeout set, which can also be achieved by providing -1 as the timeout value.

<a id="retrytopic-features--retry-topic-ex-classifier"></a>
<a id="retrytopic-features--exception-classifier"></a>

## Exception Classifier

You can specify which exceptions you want to retry on and which not to.
You can also set it to traverse the causes to lookup nested exceptions.

```java
@RetryableTopic(include = {MyRetryException.class, MyOtherRetryException.class}, traversingCauses = "true")
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    throw new RuntimeException(new MyRetryException()); // will retry
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyOtherPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .notRetryOn(MyDontRetryException.class)
            .create(template);
}
```

> [!NOTE]
> The default behavior is retrying on all exceptions and not traversing causes.

Since 2.8.3 there’s a global list of fatal exceptions which will cause the record to be sent to the DLT without any retries.
See [DefaultErrorHandler](#kafka-annotation-error-handling--default-eh) for the default list of fatal exceptions.
You can add or remove exceptions to and from this list by overriding the `configureNonBlockingRetries` method in a `@Configuration` class that extends `RetryTopicConfigurationSupport`.
See [Configuring Global Settings and Features](#retrytopic-retry-config--retry-topic-global-settings) for more information.

```java
@Override
protected void manageNonBlockingFatalExceptions(List<Class<? extends Throwable>> nonBlockingFatalExceptions) {
    nonBlockingFatalExceptions.add(MyNonBlockingException.class);
}
```

> [!NOTE]
> To disable fatal exceptions' classification, just clear the provided list.

<a id="retrytopic-features--include-and-exclude-topics"></a>

## Include and Exclude Topics

You can decide which topics will and will not be handled by a `RetryTopicConfiguration` bean via the .includeTopic(String topic), .includeTopics(Collection<String> topics) .excludeTopic(String topic) and .excludeTopics(Collection<String> topics) methods.

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .includeTopics(List.of("my-included-topic", "my-other-included-topic"))
            .create(template);
}

@Bean
public RetryTopicConfiguration myOtherRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .excludeTopic("my-excluded-topic")
            .create(template);
}
```

> [!NOTE]
> The default behavior is to include all topics.

<a id="retrytopic-features--topics-autocreation"></a>

## Topics AutoCreation

Unless otherwise specified the framework will auto create the required topics using `NewTopic` beans that are consumed by the `KafkaAdmin` bean.
You can specify the number of partitions and the replication factor with which the topics will be created, and you can turn this feature off.
Starting with version 3.0, the default replication factor is `-1`, meaning using the broker default.
If your broker version is earlier than 2.4, you will need to set an explicit value.

> [!IMPORTANT]
> Note that if you’re not using Spring Boot you’ll have to provide a KafkaAdmin bean in order to use this feature.

```java
@RetryableTopic(numPartitions = "2", replicationFactor = "3")
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}

@RetryableTopic(autoCreateTopics = "false")
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .autoCreateTopicsWith(2, 3)
            .create(template);
}

@Bean
public RetryTopicConfiguration myOtherRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .doNotAutoCreateRetryTopics()
            .create(template);
}
```

> [!NOTE]
> By default the topics are autocreated with one partition and a replication factor of -1 (meaning using the broker default).
> If your broker version is earlier than 2.4, you will need to set an explicit value.

<a id="retrytopic-features--retry-headers"></a>
<a id="retrytopic-features--failure-header-management"></a>

## Failure Header Management

When considering how to manage failure headers (original headers and exception headers), the framework delegates to the `DeadLetterPublishingRecoverer` to decide whether to append or replace the headers.

By default, it explicitly sets `appendOriginalHeaders` to `false` and leaves `stripPreviousExceptionHeaders` to the default used by the `DeadLetterPublishingRecover`.

This means that only the first "original" and last exception headers are retained with the default configuration.
This is to avoid creation of excessively large messages (due to the stack trace header, for example) when many retry steps are involved.

See [Managing Dead Letter Record Headers](#kafka-annotation-error-handling--dlpr-headers) for more information.

To reconfigure the framework to use different settings for these properties, configure a `DeadLetterPublishingRecoverer` customizer by overriding the `configureCustomizers` method in a `@Configuration` class that extends `RetryTopicConfigurationSupport`.
See [Configuring Global Settings and Features](#retrytopic-retry-config--retry-topic-global-settings) for more details.

```java
@Override
protected void configureCustomizers(CustomizersConfigurer customizersConfigurer) {
    customizersConfigurer.customizeDeadLetterPublishingRecoverer(dlpr -> {
        dlpr.setAppendOriginalHeaders(true);
        dlpr.setStripPreviousExceptionHeaders(false);
    });
}
```

Starting with version 2.8.4, if you wish to add custom headers (in addition to the retry information headers added by the factory, you can add a `headersFunction` to the factory - `factory.setHeadersFunction((rec, ex) -> { ... })`.

By default, any headers added will be cumulative - Kafka headers can contain multiple values.
Starting with version 2.9.5, if the `Headers` returned by the function contains a header of type `DeadLetterPublishingRecoverer.SingleRecordHeader`, then any existing values for that header will be removed and only the new single value will remain.

<a id="retrytopic-features--custom-dlpr"></a>
<a id="retrytopic-features--custom-deadletterpublishingrecoverer"></a>

## Custom DeadLetterPublishingRecoverer

As can be seen in [Failure Header Management](#retrytopic-features--retry-headers) it is possible to customize the default `DeadLetterPublishingRecoverer` instances created by the framework.
However, for some use cases, it is necessary to subclass the `DeadLetterPublishingRecoverer`, for example to override `createProducerRecord()` to modify the contents sent to the retry (or dead-letter) topics.
Starting with version 3.0.9, you can override the `RetryTopicConfigurationSupport.configureDeadLetterPublishingContainerFactory()` method to provide a `DeadLetterPublisherCreator` instance, for example:

```java
@Override
protected Consumer<DeadLetterPublishingRecovererFactory>
        configureDeadLetterPublishingContainerFactory() {

    return (factory) -> factory.setDeadLetterPublisherCreator(
            (templateResolver, destinationResolver) ->
                    new CustomDLPR(templateResolver, destinationResolver));
}
```

It is recommended that you use the provided resolvers when constructing the custom instance.

<a id="retrytopic-features--exc-based-custom-dlt-routing"></a>
<a id="retrytopic-features--routing-of-messages-to-custom-dlts-based-on-thrown-exceptions"></a>

## Routing of messages to custom DLTs based on thrown exceptions

Starting with version 3.2.0, it’s possible to route messages to custom DLTs based on the type of the exception, which has been thrown during their processing.
In order to do that, there’s a need to specify the routing.
Routing customization consists of the specification of the additional destinations.
Destinations in turn consist of two settings: the `suffix` and `exceptions`.
When the exception type specified in `exceptions` has been thrown, the DLT containing the `suffix` will be considered as the target topic for the message before the general purpose DLT is considered.
Examples of configuration using either annotations or `RetryTopicConfiguration` beans:

```java
@RetryableTopic(exceptionBasedDltRouting = {@ExceptionBasedDltDestination(suffix = "-deserialization", exceptions = {DeserializationException.class} )}) @KafkaListener(topics = "my-annotated-topic") public void processMessage(MyPojo message) {// ... message processing}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .dltRoutingRules(Map.of("-deserialization", Set.of(DeserializationException.class)))
            .create(template);
}
```

`suffix` takes place before the general `dltTopicSuffix` in the custom DLT name.
Considering presented examples, the message, which caused the `DeserializationException` will be routed to the `my-annotated-topic-deserialization-dlt` instead of the `my-annotated-topic-dlt`.
Custom DLTs will be created following the same rules as stated in the [Topics AutoCreation](#retrytopic-features--topics-autocreation).

[Programmatic Construction](#retrytopic-programmatic-construction)
[Combining Blocking and Non-Blocking Retries](#retrytopic-retry-topic-combine-blocking)

---

<a id="retrytopic-retry-topic-combine-blocking"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/retry-topic-combine-blocking.html -->

<!-- page_index: 56 -->

# Combining Blocking and Non-Blocking Retries

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-retry-topic-combine-blocking--page-title"></a>
<a id="retrytopic-retry-topic-combine-blocking--combining-blocking-and-non-blocking-retries"></a>

# Combining Blocking and Non-Blocking Retries

Starting in 2.8.4 you can configure the framework to use both blocking and non-blocking retries in conjunction.
For example, you can have a set of exceptions that would likely trigger errors on the next records as well, such as `DatabaseAccessException`, so you can retry the same record a few times before sending it to the retry topic, or straight to the DLT.

To configure blocking retries, override the `configureBlockingRetries` method in a `@Configuration` class that extends `RetryTopicConfigurationSupport` and add the exceptions you want to retry, along with the `BackOff` to be used.
The default `BackOff` is a `FixedBackOff` with no delay and 9 attempts.
See [Configuring Global Settings and Features](#retrytopic-retry-config--retry-topic-global-settings) for more information.

```java
@Override
protected void configureBlockingRetries(BlockingRetriesConfigurer blockingRetries) {
    blockingRetries
            .retryOn(MyBlockingRetryException.class, MyOtherBlockingRetryException.class)
            .backOff(new FixedBackOff(3_000, 5));
}
```

> [!NOTE]
> In combination with the global retryable topic’s fatal exceptions classification, you can configure the framework for any behavior you’d like, such as having some exceptions trigger both blocking and non-blocking retries, trigger only one kind or the other, or go straight to the DLT without retries of any kind.

Here’s an example with both configurations working together:

```java
@Override
protected void configureBlockingRetries(BlockingRetriesConfigurer blockingRetries) {
    blockingRetries
            .retryOn(ShouldRetryOnlyBlockingException.class, ShouldRetryViaBothException.class)
            .backOff(new FixedBackOff(50, 3));
}

@Override
protected void manageNonBlockingFatalExceptions(List<Class<? extends Throwable>> nonBlockingFatalExceptions) {
    nonBlockingFatalExceptions.add(ShouldSkipBothRetriesException.class);
}
```

In this example:

- `ShouldRetryOnlyBlockingException.class` would retry only via blocking and, if all retries fail, would go straight to the DLT.
- `ShouldRetryViaBothException.class` would retry via blocking, and if all blocking retries fail would be forwarded to the next retry topic for another set of attempts.
- `ShouldSkipBothRetriesException.class` would never be retried in any way and would go straight to the DLT if the first processing attempt failed.

> [!IMPORTANT]
> Note that the blocking retries behavior is allowlist - you add the exceptions you do want to retry that way; while the non-blocking retries classification is geared towards FATAL exceptions and as such is denylist - you add the exceptions you don’t want to do non-blocking retries, but to send directly to the DLT instead.

> [!IMPORTANT]
> The non-blocking exception classification behavior also depends on the specific topic’s configuration.

[Features](#retrytopic-features)
[Accessing Delivery Attempts](#retrytopic-accessing-delivery-attempts)

---

<a id="retrytopic-accessing-delivery-attempts"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/accessing-delivery-attempts.html -->

<!-- page_index: 57 -->

# Accessing Delivery Attempts

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-accessing-delivery-attempts--page-title"></a>
<a id="retrytopic-accessing-delivery-attempts--accessing-delivery-attempts"></a>

# Accessing Delivery Attempts

To access blocking and non-blocking delivery attempts, add these headers to your `@KafkaListener` method signature:

```java
@Header(KafkaHeaders.DELIVERY_ATTEMPT) int blockingAttempts,
@Header(name = RetryTopicHeaders.DEFAULT_HEADER_ATTEMPTS, required = false) Integer nonBlockingAttempts
```

Blocking delivery attempts are only provided if you set `ContainerProperties`'s [deliveryAttemptHeader](#kafka-container-props--deliveryattemptheader) to `true`.

Note that the non blocking attempts will be `null` for the initial delivery.

Starting with version 3.0.10, a convenient `KafkaMessageHeaderAccessor` is provided to allow simpler access to these headers; the accessor can be provided as a parameter for the listener method:

```
@RetryableTopic(backOff = @BackOff(...))
@KafkaListener(id = "dh1", topics = "dh1")
void listen(Thing thing, KafkaMessageHeaderAccessor accessor) {
    ...
}
```

Use `accessor.getBlockingRetryDeliveryAttempt()` and `accessor.getNonBlockingRetryDeliveryAttempt()` to get the values.
The accessor will throw an `IllegalStateException` if blocking retries are not enabled; for non-blocking retries, the accessor returns `1` for the initial delivery.

[Combining Blocking and Non-Blocking Retries](#retrytopic-retry-topic-combine-blocking)
[Topic Naming](#retrytopic-topic-naming)

---

<a id="retrytopic-topic-naming"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/topic-naming.html -->

<!-- page_index: 58 -->

# Topic Naming

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-topic-naming--page-title"></a>
<a id="retrytopic-topic-naming--topic-naming"></a>

# Topic Naming

Retry topics and DLT are named by suffixing the main topic with a provided or default value, appended by either the delay or index for that topic.

Examples:

"my-topic" → "my-topic-retry-0", "my-topic-retry-1", …, "my-topic-dlt"

"my-other-topic" → "my-topic-myRetrySuffix-1000", "my-topic-myRetrySuffix-2000", …, "my-topic-myDltSuffix"

> [!NOTE]
> Starting with version 4.1, the default behavior is to reuse a single retry topic for the same delay intervals.
> To create separate retry topics for each attempt, set `sameIntervalTopicReuseStrategy` to `MULTIPLE_TOPICS`.

You can [configure the suffixes](#retrytopic-topic-naming--retry-topics-and-dlt-suffixes), choose whether to append [the attempt index or delay](#retrytopic-topic-naming--append-index-or-delay), use a [single retry topic when using fixed backoff](#retrytopic-topic-naming--single-topic-fixed-delay), and use a [single retry topic for the attempts with the maxInterval](#retrytopic-topic-naming--single-topic-maxinterval-delay) when using exponential backoffs.

<a id="retrytopic-topic-naming--retry-topics-and-dlt-suffixes"></a>

## Retry Topics and DLT Suffixes

You can specify the suffixes that will be used by the retry and DLT topics.

```java
@RetryableTopic(retryTopicSuffix = "-my-retry-suffix", dltTopicSuffix = "-my-dlt-suffix")
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyOtherPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .retryTopicSuffix("-my-retry-suffix")
            .dltTopicSuffix("-my-dlt-suffix")
            .create(template);
}
```

> [!NOTE]
> The default suffixes are "-retry" and "-dlt", for retry topics and dlt respectively.

<a id="retrytopic-topic-naming--append-index-or-delay"></a>
<a id="retrytopic-topic-naming--appending-the-topic-s-index-or-delay"></a>

## Appending the Topic’s Index or Delay

You can either append the topic’s index or delay values after the suffix.

```java
@RetryableTopic(topicSuffixingStrategy = TopicSuffixingStrategy.SUFFIX_WITH_INDEX_VALUE)
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .suffixTopicsWithIndexValues()
            .create(template);
    }
```

> [!NOTE]
> The default behavior is to suffix with the delay values, except for fixed delay configurations with multiple topics, in which case the topics are suffixed with the topic’s index.

<a id="retrytopic-topic-naming--single-topic-fixed-delay"></a>
<a id="retrytopic-topic-naming--single-topic-for-fixed-delay-retries"></a>

## Single Topic for Fixed Delay Retries

If you’re using fixed delay policies such as `FixedBackOffPolicy` or `NoBackOffPolicy` you can use a single topic to accomplish the non-blocking retries.
This topic will be suffixed with the provided or default suffix, and will not have either the index or the delay values appended.

> [!NOTE]
> The previous `FixedDelayStrategy` is now deprecated, and can be replaced by `SameIntervalTopicReuseStrategy`.

```java
@RetryableTopic(backOff = @BackOff(2_000), sameIntervalTopicReuseStrategy = SameIntervalTopicReuseStrategy.SINGLE_TOPIC)
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .fixedBackOff(3_000)
            .maxAttempts(5)
            .useSingleTopicForSameIntervals()
            .create(template);
}
```

> [!NOTE]
> Starting with version 4.1, the default behavior is to use a single topic for fixed delay retries.
> To use multiple topics, set `sameIntervalTopicReuseStrategy` to `MULTIPLE_TOPICS`.

<a id="retrytopic-topic-naming--single-topic-maxinterval-delay"></a>
<a id="retrytopic-topic-naming--single-topic-for-maxinterval-exponential-delay"></a>

## Single Topic for maxInterval Exponential Delay

If you’re using exponential backoff policy (`ExponentialBackOffPolicy`), you can use a single retry topic to accomplish the non-blocking retries of the attempts whose delays are the configured `maxInterval`.

This "final" retry topic will be suffixed with the provided or default suffix, and will have either the index or the `maxInterval` value appended.

> [!NOTE]
> By opting to use a single topic for the retries with the `maxInterval` delay, it may become more viable to configure an exponential retry policy that keeps retrying for a long time, because in this approach you do not need a large amount of topics.

Starting 3.2, the default behavior is reuses the retry topic for the same intervals, when using exponential backoff, the retry topics are suffixed with the delay values, with the last retry topic reuses for the same intervals(corresponding to the `maxInterval` delay).

For instance, when configuring the exponential backoff with `initialInterval=1_000`, `multiplier=2`, and `maxInterval=16_000`, in order to keep trying for one hour, one would need to configure `maxAttempts` as 229, and by default the needed retry topics would be:

- -retry-1000
- -retry-2000
- -retry-4000
- -retry-8000
- -retry-16000

When using the strategy that work with the number of retry topics equal to the configured `maxAttempts` minus 1, the last retry topic (corresponding to the `maxInterval` delay) being suffixed with an additional index would be:

- -retry-1000
- -retry-2000
- -retry-4000
- -retry-8000
- -retry-16000-0
- -retry-16000-1
- -retry-16000-2
- …
- -retry-16000-224

If multiple topics are required, then that can be done using the following configuration.

```java
@RetryableTopic(attempts = 230,
    backOff = @BackOff(delay = 1_000, multiplier = 2, maxDelay = 16_000),
    sameIntervalTopicReuseStrategy = SameIntervalTopicReuseStrategy.MULTIPLE_TOPICS)
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<String, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .exponentialBackoff(1_000, 2, 16_000)
            .maxAttempts(230)
            .useSingleTopicForSameIntervals()
            .create(template);
}
```

<a id="retrytopic-topic-naming--custom-naming-strategies"></a>

## Custom Naming Strategies

More complex naming strategies can be accomplished by registering a bean that implements `RetryTopicNamesProviderFactory`.
The default implementation is `SuffixingRetryTopicNamesProviderFactory` and a different implementation can be registered in the following way:

```java
@Override protected RetryTopicComponentFactory createComponentFactory() {return new RetryTopicComponentFactory() {@Override public RetryTopicNamesProviderFactory retryTopicNamesProviderFactory() {return new CustomRetryTopicNamesProviderFactory();} };}
```

As an example, the following implementation, in addition to the standard suffix, adds a prefix to retry/dlt topics names:

```java
public class CustomRetryTopicNamesProviderFactory implements RetryTopicNamesProviderFactory {
@Override public RetryTopicNamesProvider createRetryTopicNamesProvider(DestinationTopic.Properties properties) {
if (properties.isMainEndpoint()) {return new SuffixingRetryTopicNamesProvider(properties);} else {return new SuffixingRetryTopicNamesProvider(properties) {
@Override public String getTopicName(String topic) {return "my-prefix-" + super.getTopicName(topic);}
};}}
}
```

[Accessing Delivery Attempts](#retrytopic-accessing-delivery-attempts)
[Multiple Listeners, Same Topic(s)](#retrytopic-multi-retry)

---

<a id="retrytopic-multi-retry"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/multi-retry.html -->

<!-- page_index: 59 -->

# Multiple Listeners, Same Topic(s)

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-multi-retry--page-title"></a>
<a id="retrytopic-multi-retry--multiple-listeners-same-topic-s"></a>

# Multiple Listeners, Same Topic(s)

Starting with version 3.0, it is now possible to configure multiple listeners on the same topic(s).
In order to do this, you must use custom topic naming to isolate the retry topics from each other.
This is best shown with an example:

```java
@RetryableTopic(...retryTopicSuffix = "-listener1", dltTopicSuffix = "-listener1-dlt",topicSuffixingStrategy = TopicSuffixingStrategy.SUFFIX_WITH_INDEX_VALUE) @KafkaListener(id = "listener1", groupId = "group1", topics = TWO_LISTENERS_TOPIC, ...) void listen1(String message, @Header(KafkaHeaders.RECEIVED_TOPIC) String receivedTopic) {...}
@RetryableTopic(...retryTopicSuffix = "-listener2", dltTopicSuffix = "-listener2-dlt",topicSuffixingStrategy = TopicSuffixingStrategy.SUFFIX_WITH_INDEX_VALUE) @KafkaListener(id = "listener2", groupId = "group2", topics = TWO_LISTENERS_TOPIC, ...) void listen2(String message, @Header(KafkaHeaders.RECEIVED_TOPIC) String receivedTopic) {...}
```

The `topicSuffixingStrategy` is optional.
The framework will configure and use a separate set of retry topics for each listener.

[Topic Naming](#retrytopic-topic-naming)
[DLT Strategies](#retrytopic-dlt-strategies)

---

<a id="retrytopic-dlt-strategies"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/dlt-strategies.html -->

<!-- page_index: 60 -->

# DLT Strategies

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-dlt-strategies--page-title"></a>
<a id="retrytopic-dlt-strategies--dlt-strategies"></a>

# DLT Strategies

The framework provides a few strategies for working with DLTs.
You can provide a method for DLT processing, use the default logging method, or have no DLT at all.
Also you can choose what happens if DLT processing fails.

<a id="retrytopic-dlt-strategies--dlt-processing-method"></a>

## DLT Processing Method

You can specify the method used to process the DLT for the topic, as well as the behavior if that processing fails.

To do that you can use the `@DltHandler` annotation in a method of the class with the `@RetryableTopic` annotation(s).
Note that the same method will be used for all the `@RetryableTopic` annotated methods within that class.

```java
@RetryableTopic @KafkaListener(topics = "my-annotated-topic") public void processMessage(MyPojo message) {// ... message processing}
@DltHandler public void processDltMessage(MyPojo message) {// ... message processing, persistence, etc}
```

The DLT handler method can also be provided through the `RetryTopicConfigurationBuilder.dltHandlerMethod(String, String)` method, passing as arguments the bean name and method name that should process the DLT’s messages.

```java
@Bean public RetryTopicConfiguration myRetryTopic(KafkaTemplate<Integer, MyPojo> template) {return RetryTopicConfigurationBuilder .newInstance() .dltHandlerMethod("myCustomDltProcessor", "processDltMessage") .create(template);}
@Component public class MyCustomDltProcessor {
private final MyDependency myDependency;
public MyCustomDltProcessor(MyDependency myDependency) {this.myDependency = myDependency;}
public void processDltMessage(MyPojo message) {// ... message processing, persistence, etc}}
```

> [!NOTE]
> If no DLT handler is provided, the default `RetryTopicConfigurer.LoggingDltListenerHandlerMethod` is used.

Starting with version 2.8, if you don’t want to consume from the DLT in this application at all, including by the default handler (or you wish to defer consumption), you can control whether or not the DLT container starts, independent of the container factory’s `autoStartup` property.

When using the `@RetryableTopic` annotation, set the `autoStartDltHandler` property to `false`; when using the configuration builder, use `autoStartDltHandler(false)` .

You can later start the DLT handler via the `KafkaListenerEndpointRegistry`.

<a id="retrytopic-dlt-strategies--dlt-failure-behavior"></a>

## DLT Failure Behavior

Should the DLT processing fail, there are two possible behaviors available: `ALWAYS_RETRY_ON_ERROR` and `FAIL_ON_ERROR`.

In the former the record is forwarded back to the DLT topic so it doesn’t block other DLT records' processing.
In the latter the consumer ends the execution without forwarding the message.

```java
@RetryableTopic(dltProcessingFailureStrategy =
            DltStrategy.FAIL_ON_ERROR)
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .dltHandlerMethod("myCustomDltProcessor", "processDltMessage")
            .doNotRetryOnDltFailure()
            .create(template);
}
```

> [!NOTE]
> The default behavior is to `ALWAYS_RETRY_ON_ERROR`.

> [!IMPORTANT]
> Starting with version 2.8.3, `ALWAYS_RETRY_ON_ERROR` will NOT route a record back to the DLT if the record causes a fatal exception to be thrown, such as a `DeserializationException`, because, generally, such exceptions will always be thrown.

Exceptions that are considered fatal are:

- `DeserializationException`
- `MessageConversionException`
- `ConversionException`
- `MethodArgumentResolutionException`
- `NoSuchMethodException`
- `ClassCastException`

You can add exceptions to and remove exceptions from this list using methods on the `DestinationTopicResolver` bean.

See [Exception Classifier](#retrytopic-features--retry-topic-ex-classifier) for more information.

<a id="retrytopic-dlt-strategies--configuring-no-dlt"></a>

## Configuring No DLT

The framework also provides the possibility of not configuring a DLT for the topic.
In this case after retrials are exhausted the processing simply ends.

```java
@RetryableTopic(dltProcessingFailureStrategy =
            DltStrategy.NO_DLT)
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .doNotConfigureDlt()
            .create(template);
}
```

[Multiple Listeners, Same Topic(s)](#retrytopic-multi-retry)
[Specifying a ListenerContainerFactory](#retrytopic-retry-topic-lcf)

---

<a id="retrytopic-retry-topic-lcf"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/retry-topic-lcf.html -->

<!-- page_index: 61 -->

# Specifying a ListenerContainerFactory

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-retry-topic-lcf--page-title"></a>
<a id="retrytopic-retry-topic-lcf--specifying-a-listenercontainerfactory"></a>

# Specifying a ListenerContainerFactory

By default the RetryTopic configuration will use the provided factory from the `@KafkaListener` annotation, but you can specify a different one to be used to create the retry topic and dlt listener containers.

For the `@RetryableTopic` annotation you can provide the factory’s bean name, and using the `RetryTopicConfiguration` bean you can either provide the bean name or the instance itself.

```java
@RetryableTopic(listenerContainerFactory = "my-retry-topic-factory")
@KafkaListener(topics = "my-annotated-topic")
public void processMessage(MyPojo message) {
    // ... message processing
}
```

```java
@Bean
public RetryTopicConfiguration myRetryTopic(KafkaTemplate<Integer, MyPojo> template,
        ConcurrentKafkaListenerContainerFactory<Integer, MyPojo> factory) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .listenerFactory(factory)
            .create(template);
}

@Bean
public RetryTopicConfiguration myOtherRetryTopic(KafkaTemplate<Integer, MyPojo> template) {
    return RetryTopicConfigurationBuilder
            .newInstance()
            .listenerFactory("my-retry-topic-factory")
            .create(template);
}
```

> [!IMPORTANT]
> Since 2.8.3 you can use the same factory for retryable and non-retryable topics.

[DLT Strategies](#retrytopic-dlt-strategies)
[Accessing Topics' Information at Runtime](#retrytopic-access-topic-info-runtime)

---

<a id="retrytopic-access-topic-info-runtime"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/access-topic-info-runtime.html -->

<!-- page_index: 62 -->

# Accessing Topics' Information at Runtime

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-access-topic-info-runtime--page-title"></a>
<a id="retrytopic-access-topic-info-runtime--accessing-topics-information-at-runtime"></a>

# Accessing Topics' Information at Runtime

Since 2.9, you can access information regarding the topic chain at runtime by injecting the provided `DestinationTopicContainer` bean.
This interface provides methods to look up the next topic in the chain or the DLT for a topic if configured, as well as useful properties such as the topic’s name, delay and type.

As a real-world use-case example, you can use such information so a console application can resend a record from the DLT to the first retry topic in the chain after the cause of the failed processing, e.g. bug / inconsistent state, has been resolved.

> [!IMPORTANT]
> The `DestinationTopic` provided by the `DestinationTopicContainer#getNextDestinationTopicFor()` method corresponds to the next topic registered in the chain for the input topic.
> The actual topic the message will be forwarded to may differ due to different factors such as exception classification, number of attempts or single-topic fixed-delay strategies.
> Use the `DestinationTopicResolver` interface if you need to weigh in these factors.

[Specifying a ListenerContainerFactory](#retrytopic-retry-topic-lcf)
[Changing KafkaBackOffException Logging Level](#retrytopic-change-kboe-logging-level)

---

<a id="retrytopic-change-kboe-logging-level"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/retrytopic/change-kboe-logging-level.html -->

<!-- page_index: 63 -->

# Changing KafkaBackOffException Logging Level

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="retrytopic-change-kboe-logging-level--page-title"></a>
<a id="retrytopic-change-kboe-logging-level--changing-kafkabackoffexception-logging-level"></a>

# Changing KafkaBackOffException Logging Level

When a message in the retry topic is not due for consumption, a `KafkaBackOffException` is thrown.
Such exceptions are logged by default at `DEBUG` level, but you can change this behavior by setting an error handler customizer in the `ListenerContainerFactoryConfigurer` in a `@Configuration` class.

For example, to change the logging level to WARN you might add:

```java
@Override
protected void configureCustomizers(CustomizersConfigurer customizersConfigurer) {
    customizersConfigurer.customizeErrorHandler(defaultErrorHandler ->
            defaultErrorHandler.setLogLevel(KafkaException.Level.WARN))
}
```

[Accessing Topics' Information at Runtime](#retrytopic-access-topic-info-runtime)
[Apache Kafka Streams Support](#streams)

---

<a id="streams"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/streams.html -->

<!-- page_index: 64 -->

# Apache Kafka Streams Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="streams--page-title"></a>
<a id="streams--apache-kafka-streams-support"></a>

# Apache Kafka Streams Support

Starting with version 1.1.4, Spring for Apache Kafka provides first-class support for [Kafka Streams](https://kafka.apache.org/42/documentation/streams).
To use it from a Spring application, the `kafka-streams` jar must be present on classpath.
It is an optional dependency of the Spring for Apache Kafka project and is not downloaded transitively.

<a id="streams--basics"></a>

## Basics

The reference Apache Kafka Streams documentation suggests the following way of using the API:

```java
// Use the builders to define the actual processing topology, e.g. to specify
// from which input topics to read, which stream operations (filter, map, etc.)
// should be called, and so on.

StreamsBuilder builder = ...;  // when using the Kafka Streams DSL

// Use the configuration to tell your application where the Kafka cluster is,
// which serializers/deserializers to use by default, to specify security settings,
// and so on.
StreamsConfig config = ...;

KafkaStreams streams = new KafkaStreams(builder, config);

// Start the Kafka Streams instance
streams.start();

// Stop the Kafka Streams instance
streams.close();
```

So, we have two main components:

- `StreamsBuilder`: With an API to build `KStream` (or `KTable`) instances.
- `KafkaStreams`: To manage the lifecycle of those instances.

> [!NOTE]
> All `KStream` instances exposed to a `KafkaStreams` instance by a single `StreamsBuilder` are started and stopped at the same time, even if they have different logic.
> In other words, all streams defined by a `StreamsBuilder` are tied with a single lifecycle control.
> Once a `KafkaStreams` instance has been closed by `streams.close()`, it cannot be restarted.
> Instead, a new `KafkaStreams` instance to restart stream processing must be created.

<a id="streams--streams-spring"></a>
<a id="streams--spring-management"></a>

## Spring Management

To simplify using Kafka Streams from the Spring application context perspective and use the lifecycle management through a container, Spring for Apache Kafka introduces `StreamsBuilderFactoryBean`.
This is an `AbstractFactoryBean` implementation to expose a `StreamsBuilder` singleton instance as a bean.
The following example creates such a bean:

```java
@Bean
public FactoryBean<StreamsBuilder> myKStreamBuilder(KafkaStreamsConfiguration streamsConfig) {
    return new StreamsBuilderFactoryBean(streamsConfig);
}
```

> [!IMPORTANT]
> Starting with version 2.2, the stream configuration is now provided as a `KafkaStreamsConfiguration` object rather than a `StreamsConfig`.

The `StreamsBuilderFactoryBean` also implements `SmartLifecycle` to manage the lifecycle of an internal `KafkaStreams` instance.
Similar to the Kafka Streams API, you must define the `KStream` instances before you start the `KafkaStreams`.
That also applies for the Spring API for Kafka Streams.
Therefore, when you use default `autoStartup = true` on the `StreamsBuilderFactoryBean`, you must declare `KStream` instances on the `StreamsBuilder` before the application context is refreshed.
For example, `KStream` can be a regular bean definition, while the Kafka Streams API is used without any impacts.
The following example shows how to do so:

```java
@Bean
public KStream<?, ?> kStream(StreamsBuilder kStreamBuilder) {
    KStream<Integer, String> stream = kStreamBuilder.stream(STREAMING_TOPIC1);
    // Fluent KStream API
    return stream;
}
```

If you would like to control the lifecycle manually (for example, stopping and starting by some condition), you can reference the `StreamsBuilderFactoryBean` bean directly by using the factory bean (`&`) [prefix](https://docs.spring.io/spring-framework/reference/7.0/core/beans/factory-extension.html#beans-factory-extension-factorybean).
Since `StreamsBuilderFactoryBean` uses its internal `KafkaStreams` instance, it is safe to stop and restart it again.
A new `KafkaStreams` is created on each `start()`.
You might also consider using different `StreamsBuilderFactoryBean` instances, if you would like to control the lifecycles for `KStream` instances separately.

You also can specify `KafkaStreams.StateListener`, `Thread.UncaughtExceptionHandler`, and `StateRestoreListener` options on the `StreamsBuilderFactoryBean`, which are delegated to the internal `KafkaStreams` instance.

Also, apart from setting those options indirectly on `StreamsBuilderFactoryBean`, you can use a `KafkaStreamsCustomizer` callback interface to:

1. (from *version 2.1.5*) configure an inner `KafkaStreams` instance using `customize(KafkaStreams)`
2. (from *version 3.3.0*) instantiate a custom implementation of `KafkaStreams` using `initKafkaStreams(Topology, Properties, KafkaClientSupplier)`

Note that `KafkaStreamsCustomizer` overrides the options provided by `StreamsBuilderFactoryBean`.

If you need to perform some `KafkaStreams` operations directly, you can access that internal `KafkaStreams` instance by using `StreamsBuilderFactoryBean.getKafkaStreams()`.

You can autowire `StreamsBuilderFactoryBean` bean by type, but you should be sure to use the full type in the bean definition, as the following example shows:

```java
@Bean
public StreamsBuilderFactoryBean myKStreamBuilder(KafkaStreamsConfiguration streamsConfig) {
    return new StreamsBuilderFactoryBean(streamsConfig);
}
...
@Autowired
private StreamsBuilderFactoryBean myKStreamBuilderFactoryBean;
```

Alternatively, you can add `@Qualifier` for injection by name if you use interface bean definition.
The following example shows how to do so:

```java
@Bean public FactoryBean<StreamsBuilder> myKStreamBuilder(KafkaStreamsConfiguration streamsConfig) {return new StreamsBuilderFactoryBean(streamsConfig);} ...@Autowired @Qualifier("&myKStreamBuilder") private StreamsBuilderFactoryBean myKStreamBuilderFactoryBean;
```

Starting with version 2.4.1, the factory bean has a new property `infrastructureCustomizer` with type `KafkaStreamsInfrastructureCustomizer`; this allows customization of the `StreamsBuilder` (e.g. to add a state store) and/or the `Topology` before the stream is created.

```java
public interface KafkaStreamsInfrastructureCustomizer {

    void configureBuilder(StreamsBuilder builder);

    void configureTopology(Topology topology);

}
```

Default no-op implementations are provided to avoid having to implement both methods if one is not required.

A `CompositeKafkaStreamsInfrastructureCustomizer` is provided, for when you need to apply multiple customizers.

<a id="streams--streams-micrometer"></a>
<a id="streams--kafkastreams-micrometer-support"></a>

## KafkaStreams Micrometer Support

Introduced in version 2.5.3, you can configure a `KafkaStreamsMicrometerListener` to automatically register micrometer meters for the `KafkaStreams` object managed by the factory bean:

```java
streamsBuilderFactoryBean.addListener(new KafkaStreamsMicrometerListener(meterRegistry,
        Collections.singletonList(new ImmutableTag("customTag", "customTagValue"))));
```

<a id="streams--serde"></a>
<a id="streams--streams-json-serialization-and-deserialization"></a>

## Streams JSON Serialization and Deserialization

For serializing and deserializing data when reading or writing to topics or state stores in JSON format, Spring for Apache Kafka provides a `JacksonJsonSerde` implementation that uses JSON, delegating to the `JacksonJsonSerializer` and `JacksonJsonDeserializer` described in [Serialization, Deserialization, and Message Conversion](#kafka-serdes).
The `JacksonJsonSerde` implementation provides the same configuration options through its constructor (target type or `ObjectMapper`).
In the following example, we use the `JacksonJsonSerde` to serialize and deserialize the `Cat` payload of a Kafka stream (the `JacksonJsonSerde` can be used in a similar fashion wherever an instance is required):

```java
stream.through(Serdes.Integer(), new JacksonJsonSerde<>(Cat.class), "cats");
```

When constructing the serializer/deserializer programmatically for use in the producer/consumer factory, since version 2.3, you can use the fluent API, which simplifies configuration.

```java
stream.through(
    new JacksonJsonSerde<>(MyKeyType.class)
        .forKeys()
        .noTypeInfo(),
    new JacksonJsonSerde<>(MyValueType.class)
        .noTypeInfo(),
    "myTypes");
```

<a id="streams--using-kafkastreambrancher"></a>

## Using `KafkaStreamBrancher`

The `KafkaStreamBrancher` class introduces a more convenient way to build conditional branches on top of `KStream`.

Consider the following example that does not use `KafkaStreamBrancher`:

```java
KStream<String, String>[] branches = builder.stream("source").branch(
        (key, value) -> value.contains("A"),
        (key, value) -> value.contains("B"),
        (key, value) -> true
);
branches[0].to("A");
branches[1].to("B");
branches[2].to("C");
```

The following example uses `KafkaStreamBrancher`:

```java
new KafkaStreamBrancher<String, String>()
        .branch((key, value) -> value.contains("A"), ks -> ks.to("A"))
        .branch((key, value) -> value.contains("B"), ks -> ks.to("B"))
        //default branch should not necessarily be defined in the end of the chain!
        .defaultBranch(ks -> ks.to("C"))
        .onTopOf(builder.stream("source"));
        //onTopOf method returns the provided stream so we can continue with method chaining
```

<a id="streams--streams-config"></a>
<a id="streams--configuration"></a>

## Configuration

To configure the Kafka Streams environment, the `StreamsBuilderFactoryBean` requires a `KafkaStreamsConfiguration` instance.
See the Apache Kafka [documentation](https://kafka.apache.org/42/documentation/#streamsconfigs) for all possible options.

> [!IMPORTANT]
> Starting with version 2.2, the stream configuration is now provided as a `KafkaStreamsConfiguration` object, rather than as a `StreamsConfig`.

To avoid boilerplate code for most cases, especially when you develop microservices, Spring for Apache Kafka provides the `@EnableKafkaStreams` annotation, which you should place on a `@Configuration` class.
All you need is to declare a `KafkaStreamsConfiguration` bean named `defaultKafkaStreamsConfig`.
A `StreamsBuilderFactoryBean` bean, named `defaultKafkaStreamsBuilder`, is automatically declared in the application context.
You can declare and use any additional `StreamsBuilderFactoryBean` beans as well.
You can perform additional customization of that bean, by providing a bean that implements `StreamsBuilderFactoryBeanConfigurer`.
If there are multiple such beans, they will be applied according to their `Ordered.order` property.

<a id="streams--_cleanup_stop_configuration"></a>
<a id="streams--cleanup-stop-configuration"></a>

### Cleanup & Stop configuration

When the factory is stopped, the `KafkaStreams.close()` is called with 2 parameters :

- closeTimeout : how long to wait for the threads to shutdown (defaults to `DEFAULT_CLOSE_TIMEOUT` set to 10 seconds). Can be configured using `StreamsBuilderFactoryBean.setCloseTimeout()`.
- leaveGroupOnClose : to trigger consumer leave call from the group (defaults to `false`). Can be configured using `StreamsBuilderFactoryBean.setLeaveGroupOnClose()`.

By default, when the factory bean is stopped, the `KafkaStreams.cleanUp()` method is called.
Starting with version 2.1.2, the factory bean has additional constructors, taking a `CleanupConfig` object that has properties to let you control whether the `cleanUp()` method is called during `start()` or `stop()` or neither.
Starting with version 2.7, the default is to never clean up local state.

<a id="streams--streams-group-protocol"></a>
<a id="streams--group-protocol-configuration"></a>

## Group Protocol Configuration

Starting with version 4.1, you can configure the consumer group protocol used by the underlying Kafka Streams consumers by setting the `groupProtocol` property.
This allows you to explicitly manage whether the consumers rely on the `classic` protocol or opt into the newer `streams` group protocol introduced in KIP-1071 (Server-side rebalance for Streams, GA in Kafka 4.2).
While this is enabled by default on new clusters, existing clusters can opt-in using this property.
It can be configured using `StreamsBuilderFactoryBean.setGroupProtocol()`.

The following example shows how to configure the group protocol using a `StreamsBuilderFactoryBeanConfigurer`:

```java
@Bean
public StreamsBuilderFactoryBeanConfigurer groupProtocolConfigurer() {
    return fb -> fb.setGroupProtocol(GroupProtocol.STREAMS);
}
```

<a id="streams--streams-header-enricher"></a>
<a id="streams--header-enricher"></a>

## Header Enricher

Version 3.0 added the `HeaderEnricherProcessor` extension of `ContextualProcessor`; providing the same functionality as the deprecated `HeaderEnricher` which implemented the deprecated `Transformer` interface.
This can be used to add headers within the stream processing; the header values are SpEL expressions; the root object of the expression evaluation has 3 properties:

- `record` - the `org.apache.kafka.streams.processor.api.Record` (`key`, `value`, `timestamp`, `headers`)
- `key` - the key of the current record
- `value` - the value of the current record
- `context` - the `ProcessorContext`, allowing access to the current record metadata

The expressions must return a `byte[]` or a `String` (which will be converted to `byte[]` using `UTF-8`).

To use the enricher within a stream:

```java
.process(() -> new HeaderEnricherProcessor(expressions))
```

The processor does not change the `key` or `value`; it simply adds headers.

> [!IMPORTANT]
> You need a new instance for each record.

```java
.process(() -> new HeaderEnricherProcessor<..., ...>(expressionMap))
```

Here is a simple example, adding one literal header and one variable:

```java
Map<String, Expression> headers = new HashMap<>();
headers.put("header1", new LiteralExpression("value1"));
SpelExpressionParser parser = new SpelExpressionParser();
headers.put("header2", parser.parseExpression("record.timestamp() + ' @' + record.offset()"));
ProcessorSupplier supplier = () -> new HeaderEnricher<String, String>(headers);
KStream<String, String> stream = builder.stream(INPUT);
stream
        .process(() -> supplier)
        .to(OUTPUT);
```

<a id="streams--streams-messaging"></a>
<a id="streams--messagingprocessor"></a>

## `MessagingProcessor`

Version 3.0 added the `MessagingProcessor` extension of `ContextualProcessor`, providing the same functionality as the deprecated `MessagingTransformer` which implemented the deprecated `Transformer` interface.
This allows a Kafka Streams topology to interact with a Spring Messaging component, such as a Spring Integration flow.
The transformer requires an implementation of `MessagingFunction`.

```java
@FunctionalInterface
public interface MessagingFunction {

    Message<?> exchange(Message<?> message);

}
```

Spring Integration automatically provides an implementation using its `GatewayProxyFactoryBean`.
It also requires a `MessagingMessageConverter` to convert the key, value and metadata (including headers) to/from a Spring Messaging `Message<?>`.
See [Calling a Spring Integration Flow from a `KStream`](https://docs.spring.io/spring-integration/reference/kafka.html#streams-integration) for more information.

<a id="streams--recovery-strategies"></a>

## Recovery Strategies

The framework provides the following exception handlers, which follow the same recovery strategies:

- [`RecoveringDeserializationExceptionHandler`](#streams--streams-deser-recovery)
- [`RecoveringProcessingExceptionHandler`](#streams--streams-processing-recovery)
- [`RecoveringProductionExceptionHandler`](#streams--streams-production-recovery)

The recovery strategies are as follows, by priority order:

- If a [`KafkaStreamsDeadLetterDestinationResolver`](#streams--dead-letter-destination-resolver) is defined, resume the stream and forward the failed record to the resolved topic-partition using the native Kafka Streams DLQ.
- If [`errors.dead.letter.queue.topic.name`](#streams--dead-letter-queue-topic-name-property) is defined and set to a topic name, resume the stream and forward the failed record to that topic using the native Kafka Streams DLQ.
- If a `ConsumerRecordRecoverer` implementation is defined, invoke it and resume the stream without producing dead-letter records, as handling is delegated to the `ConsumerRecordRecoverer`. For example, the provided [`DeadLetterPublishingRecoverer`](#streams--dead-letter-publishing-recoverer) implementation can be used.
- Fail the stream without producing dead-letter records.

When a dead-letter record is published to a dead-letter topic, whether through the native Kafka Streams DLQ or via a `ConsumerRecordRecoverer` implementation:

- The source raw key, source raw value and source headers are used to build the record.
- The record is enriched with the [Spring for Apache Kafka DLT headers](#kafka-annotation-error-handling--dead-letters).

<a id="streams--streams-deser-recovery"></a>
<a id="streams--recovery-from-deserialization-exceptions"></a>

## Recovery from Deserialization Exceptions

Version 2.3 introduced the `RecoveringDeserializationExceptionHandler`, which can take some action when a deserialization exception occurs.
It implements the `DeserializationExceptionHandler` interface (refer to the Kafka documentation for details) and follows the [Spring for Apache Kafka recovery strategies](#streams--recovery-strategies).

To configure the `RecoveringDeserializationExceptionHandler`, add the following property to your streams configuration:

```java
@Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME) public KafkaStreamsConfiguration kStreamsConfigs() {Map<String, Object> props = new HashMap<>(); ...props.put(StreamsConfig.DESERIALIZATION_EXCEPTION_HANDLER_CLASS_CONFIG,RecoveringDeserializationExceptionHandler.class); ...return new KafkaStreamsConfiguration(props);}
```

<a id="streams--streams-processing-recovery"></a>
<a id="streams--recovery-from-processing-exceptions"></a>

## Recovery from Processing Exceptions

Version 4.1 introduces the `RecoveringProcessingExceptionHandler`, which can take some action when an exception occurs during stream processing.
It implements the `ProcessingExceptionHandler` interface (refer to the Kafka documentation for details), introduced by [KIP-1033](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1033%3A+Add+Kafka+Streams+exception+handler+for+exceptions+occurring+during+processing)
and follows the [Spring for Apache Kafka recovery strategies](#streams--recovery-strategies).

To enable the `RecoveringProcessingExceptionHandler`, add the following property to your streams configuration:

```java
@Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME) public KafkaStreamsConfiguration kStreamsConfigs() {Map<String, Object> props = new HashMap<>(); ...props.put(StreamsConfig.PROCESSING_EXCEPTION_HANDLER_CLASS_CONFIG,RecoveringProcessingExceptionHandler.class); ...}
```

<a id="streams--streams-production-recovery"></a>
<a id="streams--recovery-from-production-exceptions"></a>

## Recovery from Production Exceptions

Version 4.1 introduces the `RecoveringProductionExceptionHandler`, which can take some action when an exception occurs during record production or serialization.
It implements the `ProductionExceptionHandler` interface (refer to the Kafka documentation for details) and follows the [Spring for Apache Kafka recovery strategies](#streams--recovery-strategies).

To configure the `RecoveringProductionExceptionHandler`, add the following property to your streams configuration:

```java
@Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME) public KafkaStreamsConfiguration kStreamsConfigs() {Map<String, Object> props = new HashMap<>(); ...props.put(StreamsConfig.PRODUCTION_EXCEPTION_HANDLER_CLASS_CONFIG,RecoveringProductionExceptionHandler.class); ...}
```

<a id="streams--dead-letter-publishing-recoverer"></a>

## Dead Letter Publishing Recoverer

The framework provides the `DeadLetterPublishingRecoverer`, which sends the failed record to a dead-letter topic.
See [Publishing Dead-letter records](#kafka-annotation-error-handling--dead-letters) for more information about this recoverer.

To configure the recoverer for an exception handler, add the following properties to your streams configuration:

```java
@Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME) public KafkaStreamsConfiguration kStreamsConfigs() {Map<String, Object> props = new HashMap<>(); ...props.put(StreamsConfig.DESERIALIZATION_EXCEPTION_HANDLER_CLASS_CONFIG,RecoveringDeserializationExceptionHandler.class); props.put(RecoveringDeserializationExceptionHandler.RECOVERER, recoverer()); ...return new KafkaStreamsConfiguration(props);}
@Bean public DeadLetterPublishingRecoverer recoverer() {return new DeadLetterPublishingRecoverer(kafkaTemplate(),(record, ex) -> new TopicPartition("recovererDLQ", -1));}
```

Of course, the `recoverer()` bean can be your own implementation of `ConsumerRecordRecoverer`.

<a id="streams--dead-letter-destination-resolver"></a>

## Dead Letter Destination Resolver

A bean of type `KafkaStreamsDeadLetterDestinationResolver` can be defined to activate native DLQ routing in the exception handlers.

It determines the DLQ topic name and partition resolution logic to use, based on the error handler context, the input record of the failed processor, and the exception thrown:

```java
@Bean public KafkaStreamsDeadLetterDestinationResolver resolver() {return (context, record, ex) -> {if (ex instanceof FooException) return new TopicPartition("dlqTopic1", -1); if (record instanceof Foo) return new TopicPartition("dlqTopic2", -1); if (context.processorNodeId().equals("processor-1")) return new TopicPartition("dlqTopic3", -1); return new TopicPartition("defaultDlqTopic", -1); };}
```

A negative partition number indicates that the partition will be determined by the default partitioner.

The `KafkaStreamsDeadLetterDestinationResolver` can then be injected into the exception handlers as follows:

```java
@Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME) public KafkaStreamsConfiguration kStreamsConfigs() {Map<String, Object> props = new HashMap<>(); ...props.put(StreamsConfig.PROCESSING_EXCEPTION_HANDLER_CLASS_CONFIG,RecoveringProcessingExceptionHandler.class); props.put(RecoveringProcessingExceptionHandler.DLQ_DESTINATION_RESOLVER, resolver()); ...return new KafkaStreamsConfiguration(props);}
```

<a id="streams--dead-letter-queue-topic-name-property"></a>

## Dead Letter Queue Topic Name Property

The Kafka Streams property `errors.dead.letter.queue.topic.name` can be defined and set to a topic name to activate native DLQ routing in the exception handlers.
This directly specifies the DLQ topic to which the enabled exception handlers will route all failed records.

Alternatively, this can be set programmatically through the `StreamsBuilderFactoryBean`:

```java
@Bean
public StreamsBuilderFactoryBeanConfigurer streamsBuilderFactoryBeanConfigurer() {
    return sfb -> sfb.setDeadLetterTopicName("deadLetterQueueTopic");
}
```

<a id="streams--kafka-streams-iq-support"></a>
<a id="streams--interactive-query-support"></a>

## Interactive Query Support

Starting with version 3.2, Spring for Apache Kafka provides basic facilities required for interactive queries in Kafka Streams.
Interactive queries are useful in stateful Kafka Streams applications since they provide a way to constantly query the stateful stores in the application.
Thus, if an application wants to materialize the current view of the system under consideration, interactive queries provide a way to do that.
To learn more about interactive queries, see this [article](https://kafka.apache.org/42/documentation/streams/developer-guide/interactive-queries.html).
The support in Spring for Apache Kafka is centered around an API called `KafkaStreamsInteractiveQueryService` which is a facade around interactive queries APIs in Kafka Streams library.
An application can create an instance of this service as a bean and then later on use it to retrieve the state store by its name.

The following code snippet shows an example.

```java
@Bean
public KafkaStreamsInteractiveQueryService kafkaStreamsInteractiveQueryService(StreamsBuilderFactoryBean streamsBuilderFactoryBean) {
    final KafkaStreamsInteractiveQueryService kafkaStreamsInteractiveQueryService =
            new KafkaStreamsInteractiveQueryService(streamsBuilderFactoryBean);
    return kafkaStreamsInteractiveQueryService;
}
```

Assuming that a Kafka Streams application has a state store called `app-store`, then that store can be retrieved via the `KafkaStreamsInteractiveQuery` API as shown below.

```java
@Autowired
private KafkaStreamsInteractiveQueryService interactiveQueryService;

ReadOnlyKeyValueStore<Object, Object>  appStore = interactiveQueryService.retrieveQueryableStore("app-store", QueryableStoreTypes.keyValueStore());
```

Once an application gains access to the state store, then it can query from it for key-value information.

In this case, the state store that the application uses is a read-only key value store.
There are other types of state stores that a Kafka Streams application can use.
For instance, if an application prefers to query a window based store, it can build that store in the Kafka Streams application business logic and then later on retrieve it.
Because of this reason, the API to retrieve the queryable store in `KafkaStreamsInteractiveQueryService` has a generic store type signature, so that the end-user can assign the proper type.

Here is the type signature from the API.

```java
public <T> T retrieveQueryableStore(String storeName, QueryableStoreType<T> storeType)
```

When calling this method, the user can specifically ask for the proper state store type, as we have done in the above example.

<a id="streams--_retrying_state_store_retrieval"></a>
<a id="streams--retrying-state-store-retrieval"></a>

### Retrying State Store Retrieval

When trying to retrieve the state store using the `KafkaStreamsInteractiveQueryService`, there is a chance that the state store might not be found for various reasons.
If those reasons are transitory, `KafkaStreamsInteractiveQueryService` provides an option to retry the retrieval of the state store by allowing to inject a custom `RetryTemplate`.
By default, the `RetryTemplate` that is used in `KafkaStreamsInteractiveQueryService` uses a maximum attempts of three with a fixed backoff of one second.

Here is how you can inject a custom `RetryTemplate` into `KafkaStreamsInteractiveQueryService` with the maximum attempts of ten.

```java
@Bean
public KafkaStreamsInteractiveQueryService kafkaStreamsInteractiveQueryService(StreamsBuilderFactoryBean streamsBuilderFactoryBean) {
    final KafkaStreamsInteractiveQueryService kafkaStreamsInteractiveQueryService =
            new KafkaStreamsInteractiveQueryService(streamsBuilderFactoryBean);
    RetryTemplate retryTemplate = new RetryTemplate();
    retryTemplate.setBackOffPolicy(new FixedBackOffPolicy());
    RetryPolicy retryPolicy = new SimpleRetryPolicy(10);
    retryTemplate.setRetryPolicy(retryPolicy);
    kafkaStreamsInteractiveQueryService.setRetryTemplate(retryTemplate);
    return kafkaStreamsInteractiveQueryService;
}
```

<a id="streams--_querying_remote_state_stores"></a>
<a id="streams--querying-remote-state-stores"></a>

### Querying Remote State Stores

The API shown above for retrieving the state store - `retrieveQueryableStore` is intended for locally available key-value state stores.
In productions settings, Kafka Streams applications are most likely distributed based on the number of partitions.
If a topic has four partitions and there are four instances of the same Kafka Streams processor running, then each instance maybe responsible for processing a single partition from the topic.
In this scenario, calling `retrieveQueryableStore` may not give the correct result that an instance is looking for, although it might return a valid store.
Let’s assume that the topic with four partitions has data about various keys and a single partition is always responsible for a specific key.
If the instance that is calling `retrieveQueryableStore` is looking for information about a key that this instance does not host, then it will not receive any data.
This is because the current Kafka Streams instance does not know anything about this key.
To fix this, the calling instance first needs to make sure that they have the host information for the Kafka Streams processor instance where the particular key is hosted.
This can be retrieved from any Kafka Streams instance under the same `application.id` as below.

```java
@Autowired
private KafkaStreamsInteractiveQueryService interactiveQueryService;

HostInfo kafkaStreamsApplicationHostInfo = this.interactiveQueryService.getKafkaStreamsApplicationHostInfo("app-store", 12345, new IntegerSerializer());
```

In the example code above, the calling instance is querying for a particular key `12345` from the state-store named `app-store`.
The API also needs a corresponding key serializer, which in this case is the `IntegerSerializer`.
Kafka Streams looks through all it’s instances under the same `application.id` and tries to find which instance hosts this particular key, Once found, it returns that host information as a `HostInfo` object.

This is how the API looks like:

```java
public <K> HostInfo getKafkaStreamsApplicationHostInfo(String store, K key, Serializer<K> serializer)
```

When using multiple instances of the Kafka Streams processors of the same `application.id` in a distributed way like this, the application is supposed to provide an RPC layer where the state stores can be queried over an RPC endpoint such as a REST one.
See this [article](https://kafka.apache.org/42/documentation/streams/developer-guide/interactive-queries.html#querying-remote-state-stores-for-the-entire-app) for more details on this.
When using Spring for Apache Kafka, it is very easy to add a Spring based REST endpoint by using the spring-web technologies.
Once there is a REST endpoint, then that can be used to query the state stores from any Kafka Streams instance, given the `HostInfo` where the key is hosted is known to the instance.

If the key hosting the instance is the current instance, then the application does not need to call the RPC mechanism, but rather make an in-JVM call.
However, the trouble is that an application may not know that the instance that is making the call is where the key is hosted because a particular server may lose a partition due to a consumer rebalance.
To fix this issue, `KafkaStreamsInteractiveQueryService` provides a convenient API for querying the current host information via an API method `getCurrentKafkaStreamsApplicationHostInfo()` that returns the current `HostInfo`.
The idea is that the application can first acquire information about where the key is held, and then compare the `HostInfo` with the one about the current instance.
If the `HostInfo` data matches, then it can proceed with a simple JVM call via the `retrieveQueryableStore`, otherwise go with the RPC option.

<a id="streams--kafka-streams-example"></a>

## Kafka Streams Example

The following example combines the various topics we have covered in this chapter:

```java
@Configuration
@EnableKafka
@EnableKafkaStreams
public class KafkaStreamsConfig {

    @Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME)
    public KafkaStreamsConfiguration kStreamsConfigs() {
        Map<String, Object> props = new HashMap<>();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "testStreams");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.Integer().getClass().getName());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass().getName());
        props.put(StreamsConfig.DEFAULT_TIMESTAMP_EXTRACTOR_CLASS_CONFIG, WallclockTimestampExtractor.class.getName());
        return new KafkaStreamsConfiguration(props);
    }

    @Bean
    public StreamsBuilderFactoryBeanConfigurer configurer() {
        return fb -> fb.setStateListener((newState, oldState) -> {
            System.out.println("State transition from " + oldState + " to " + newState);
        });
    }

    @Bean
    public KStream<Integer, String> kStream(StreamsBuilder kStreamBuilder) {
        KStream<Integer, String> stream = kStreamBuilder.stream("streamingTopic1");
        stream
                .mapValues((ValueMapper<String, String>) String::toUpperCase)
                .groupByKey()
                .windowedBy(TimeWindows.ofSizeWithNoGrace(Duration.ofMillis(1_000)))
                .reduce((String value1, String value2) -> value1 + value2,
                		Named.as("windowStore"))
                .toStream()
                .map((windowedId, value) -> new KeyValue<>(windowedId.key(), value))
                .filter((i, s) -> s.length() > 40)
                .to("streamingTopic2");

        stream.print(Printed.toSysOut());

        return stream;
    }

}
```

[Changing KafkaBackOffException Logging Level](#retrytopic-change-kboe-logging-level)
[Testing Applications](#testing)

---

<a id="testing"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/testing.html -->

<!-- page_index: 65 -->

# Testing Applications

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="testing--page-title"></a>
<a id="testing--testing-applications"></a>

# Testing Applications

The `spring-kafka-test` jar contains some useful utilities to assist with testing your applications.

> [!IMPORTANT]
> When using Spring Boot, use the `spring-boot-starter-kafka-test` dependency instead:

- Maven
- Gradle

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-kafka-test</artifactId>
  <scope>test</scope>
</dependency>
```

```groovy
testImplementation 'org.springframework.boot:spring-boot-starter-kafka-test'
```

<a id="testing--ekb"></a>
<a id="testing--embedded-kafka-broker"></a>

## Embedded Kafka Broker

Since Kafka 4.0 has fully transitioned to KRaft mode, only the `EmbeddedKafkaKraftBroker` implementation is now available:

- `EmbeddedKafkaKraftBroker` - uses `Kraft` in combined controller and broker modes.

There are several techniques to configure the broker as discussed in the following sections.

<a id="testing--ktu"></a>
<a id="testing--kafkatestutils"></a>

## KafkaTestUtils

`org.springframework.kafka.test.utils.KafkaTestUtils` provides a number of static helper methods to consume records, retrieve various record offsets, and others.
Refer to its [Javadocs](https://docs.spring.io/spring-kafka/docs/4.1.0/api/org/springframework/kafka/test/utils/KafkaTestUtils.html) for complete details.

<a id="testing--junit"></a>

## JUnit

`org.springframework.kafka.test.utils.KafkaTestUtils` provides some static methods to set up producer and consumer properties.
The following listing shows those method signatures:

```java
/** * Set up test properties for an {@code <Integer, String>} consumer.* @param group the group id.* @param autoCommit the auto commit.* @param embeddedKafka a {@link EmbeddedKafkaBroker} instance.* @return the properties.*/ public static Map<String, Object> consumerProps(String group, String autoCommit,EmbeddedKafkaBroker embeddedKafka) { ... }
/** * Set up test properties for an {@code <Integer, String>} producer.* @param embeddedKafka a {@link EmbeddedKafkaBroker} instance.* @return the properties.*/ public static Map<String, Object> producerProps(EmbeddedKafkaBroker embeddedKafka) { ... }
```

> [!NOTE]
> Starting with version 2.5, the `consumerProps` method sets the `ConsumerConfig.AUTO_OFFSET_RESET_CONFIG` to `earliest`.
> This is because, in most cases, you want the consumer to consume any messages sent in a test case.
> The `ConsumerConfig` default is `latest` which means that messages already sent by a test, before the consumer starts, will not receive those records.
> To revert to the previous behavior, set the property to `latest` after calling the method.
>
> When using the embedded broker, it is generally best practice using a different topic for each test, to prevent cross-talk.
> If this is not possible for some reason, note that the `consumeFromEmbeddedTopics` method’s default behavior is to seek the assigned partitions to the beginning after assignment.
> Since it does not have access to the consumer properties, you must use the overloaded method that takes a `seekToEnd` boolean parameter to seek to the end instead of the beginning.

> [!NOTE]
> Spring for Apache Kafka no longer supports JUnit 4.
> Migration to JUnit Jupiter is recommended.

The `EmbeddedKafkaBroker` class has a utility method that lets you consume for all the topics it created.
The following example shows how to use it:

```java
Map<String, Object> consumerProps = KafkaTestUtils.consumerProps("testT", "false", embeddedKafka);
DefaultKafkaConsumerFactory<Integer, String> cf = new DefaultKafkaConsumerFactory<>(consumerProps);
Consumer<Integer, String> consumer = cf.createConsumer();
embeddedKafka.consumeFromAllEmbeddedTopics(consumer);
```

The `KafkaTestUtils` has some utility methods to fetch results from the consumer.
The following listing shows those method signatures:

```java
/** * Poll the consumer, expecting a single record for the specified topic.* @param consumer the consumer.* @param topic the topic.* @return the record.* @throws org.junit.ComparisonFailure if exactly one record is not received.*/ public static <K, V> ConsumerRecord<K, V> getSingleRecord(Consumer<K, V> consumer, String topic) { ... }
/** * Poll the consumer for records.* @param consumer the consumer.* @return the records.*/ public static <K, V> ConsumerRecords<K, V> getRecords(Consumer<K, V> consumer) { ... }
```

The following example shows how to use `KafkaTestUtils`:

```java
...
template.sendDefault(0, 2, "bar");
ConsumerRecord<Integer, String> received = KafkaTestUtils.getSingleRecord(consumer, "topic");
...
```

When the embedded Kafka broker is started by the `EmbeddedKafkaBroker`, a system property named `spring.embedded.kafka.brokers` is set to the address of the Kafka brokers.
Convenient constants (`EmbeddedKafkaBroker.SPRING_EMBEDDED_KAFKA_BROKERS`) are provided for this property.

Instead of default `spring.embedded.kafka.brokers` system property, the address of the Kafka brokers can be exposed to any arbitrary and convenient property.
For this purpose a `spring.embedded.kafka.brokers.property` (`EmbeddedKafkaBroker.BROKER_LIST_PROPERTY`) system property can be set before starting an embedded Kafka.
For example, with Spring Boot a `spring.kafka.bootstrap-servers` configuration property is expected to be set for auto-configuring Kafka client, respectively.
So, before running tests with an embedded Kafka on random ports, we can set `spring.embedded.kafka.brokers.property=spring.kafka.bootstrap-servers` as a system property - and the `EmbeddedKafkaBroker` will use it to expose its broker addresses.
This is now the default value for this property (starting with version 3.0.10).

With the `EmbeddedKafkaBroker.brokerProperties(Map<String, String>)`, you can provide additional properties for the Kafka servers.
See [Kafka Config](https://kafka.apache.org/42/documentation/#brokerconfigs) for more information about possible broker properties.

<a id="testing--configuring-topics"></a>

## Configuring Topics

The following example configuration creates topics called `cat` and `hat` with five partitions, a topic called `thing1` with 10 partitions, and a topic called `thing2` with 15 partitions:

```java
@SpringJUnitConfig @EmbeddedKafka(partitions = 5,topics = {"cat", "hat"}) public class MyTests {
@Autowired private EmbeddedKafkaBroker broker;
@Test public void test() {broker.addTopics(new NewTopic("thing1", 10, (short) 1), new NewTopic("thing2", 15, (short) 1)); ...}
}
```

By default, `addTopics` will throw an exception when problems arise (such as adding a topic that already exists).
Version 2.6 added a new version of that method that returns a `Map<String, Exception>`; the key is the topic name and the value is `null` for success, or an `Exception` for a failure.

<a id="testing--same-broker-multiple-tests"></a>
<a id="testing--using-the-same-broker-s-for-multiple-test-classes"></a>

## Using the Same Broker(s) for Multiple Test Classes

You can use the same broker for multiple test classes with something similar to the following:

```java
public final class EmbeddedKafkaHolder {
private static EmbeddedKafkaBroker embeddedKafka = new EmbeddedKafkaZKBroker(1, false) .brokerListProperty("spring.kafka.bootstrap-servers");
private static volatile boolean started;
public static EmbeddedKafkaBroker getEmbeddedKafka() {if (!started) {synchronized (EmbeddedKafkaBroker.class) {try {embeddedKafka.afterPropertiesSet();} catch (Exception e) {throw new KafkaException("Embedded broker failed to start", e);} started = true;}} return embeddedKafka;}}
```

This assumes a Spring Boot environment and the embedded broker replaces the bootstrap servers property.

Then, in each test class, you can use something similar to the following:

```java
static {
    EmbeddedKafkaHolder.getEmbeddedKafka().addTopics("topic1", "topic2");
}

private static final EmbeddedKafkaBroker broker = EmbeddedKafkaHolder.getEmbeddedKafka();
```

If you are not using Spring Boot, you can obtain the bootstrap servers using `broker.getBrokersAsString()`.

> [!IMPORTANT]
> The preceding example provides no mechanism for shutting down the broker(s) when all tests are complete.
> This could be a problem if, say, you run your tests in a Gradle daemon.
> You should not use this technique in such a situation, or you should use something to call `destroy()` on the `EmbeddedKafkaBroker` when your tests are complete.

Starting with version 3.0, the framework exposes a `GlobalEmbeddedKafkaTestExecutionListener` for the JUnit Platform; it is disabled by default.
This requires JUnit Platform 1.8 or greater.
The purpose of this listener is to start one global `EmbeddedKafkaBroker` for the whole test plan and stop it at the end of the plan.
To enable this listener, and therefore have a single global embedded Kafka cluster for all the tests in the project, the `spring.kafka.global.embedded.enabled` property must be set to `true` via system properties or JUnit Platform configuration.
In addition, these properties can be provided:

- `spring.kafka.embedded.count` - the number of Kafka brokers to manage;
- `spring.kafka.embedded.ports` - ports (comma-separated value) for every Kafka broker to start, `0` if random port is preferred; the number of values must be equal to the `count` mentioned above;
- `spring.kafka.embedded.topics` - topics (comma-separated value) to create in the started Kafka cluster;
- `spring.kafka.embedded.partitions` - number of partitions to provision for the created topics;
- `spring.kafka.embedded.broker.properties.location` - the location of the file for additional Kafka broker configuration properties; the value of this property must follow the Spring resource abstraction pattern.

Essentially these properties mimic some of the `@EmbeddedKafka` attributes.

See more information about configuration properties and how to provide them in the [JUnit Jupiter User Guide](https://junit.org/junit5/docs/current/user-guide/#running-tests-config-params).
For example, a `spring.embedded.kafka.brokers.property=my.bootstrap-servers` entry can be added into a `junit-platform.properties` file in the testing classpath.
Starting with version 3.0.10, the broker automatically sets this to `spring.kafka.bootstrap-servers`, by default, for testing with Spring Boot applications.

> [!NOTE]
> It is recommended to not combine a global embedded Kafka and per-test class in a single test suite.
> Both of them share the same system properties, so it is very likely going to lead to unexpected behavior.

> [!NOTE]
> `spring-kafka-test` has transitive dependencies on `junit-jupiter-api` and `junit-platform-launcher` (the latter to support the global embedded broker).
> If you wish to use the embedded broker and are NOT using JUnit, you may wish to exclude these dependencies.

<a id="testing--embedded-kafka-annotation"></a>
<a id="testing--embeddedkafka-annotation"></a>

## `@EmbeddedKafka` Annotation

We generally recommend that you use a single broker instance to avoid starting and stopping the broker between tests (and use a different topic for each test).
Starting with version 2.0, if you use Spring’s test application context caching, you can also declare a `EmbeddedKafkaBroker` bean, so a single broker can be used across multiple test classes.
For convenience, we provide a test class-level annotation called `@EmbeddedKafka` to register the `EmbeddedKafkaBroker` bean.
The following example shows how to use it:

```java
@SpringJUnitConfig
@DirtiesContext
@EmbeddedKafka(partitions = 1,
         topics = {
                 KafkaStreamsTests.STREAMING_TOPIC1,
                 KafkaStreamsTests.STREAMING_TOPIC2 })
public class KafkaStreamsTests {

    @Autowired
    private EmbeddedKafkaBroker embeddedKafka;

    @Test
    void someTest() {
        Map<String, Object> consumerProps = KafkaTestUtils.consumerProps("testGroup", "true", this.embeddedKafka);
        consumerProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        ConsumerFactory<Integer, String> cf = new DefaultKafkaConsumerFactory<>(consumerProps);
        Consumer<Integer, String> consumer = cf.createConsumer();
        this.embeddedKafka.consumeFromAnEmbeddedTopic(consumer, KafkaStreamsTests.STREAMING_TOPIC2);
        ConsumerRecords<Integer, String> replies = KafkaTestUtils.getRecords(consumer);
        assertThat(replies.count()).isGreaterThanOrEqualTo(1);
    }

    @Configuration
    @EnableKafkaStreams
    public static class TestKafkaStreamsConfiguration {

        @Value("${" + EmbeddedKafkaBroker.SPRING_EMBEDDED_KAFKA_BROKERS + "}")
        private String brokerAddresses;

        @Bean(name = KafkaStreamsDefaultConfiguration.DEFAULT_STREAMS_CONFIG_BEAN_NAME)
        public KafkaStreamsConfiguration kStreamsConfigs() {
            Map<String, Object> props = new HashMap<>();
            props.put(StreamsConfig.APPLICATION_ID_CONFIG, "testStreams");
            props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, this.brokerAddresses);
            return new KafkaStreamsConfiguration(props);
        }

    }

}
```

Starting with version 2.2.4, you can also use the `@EmbeddedKafka` annotation to specify the Kafka ports property.

> [!NOTE]
> As of version 4.0, all ZooKeeper-related properties have been removed from the `@EmbeddedKafka` annotation since Kafka 4.0 uses KRaft exclusively.

The following example sets the `topics`, `brokerProperties`, and `brokerPropertiesLocation` attributes of `@EmbeddedKafka` support property placeholder resolutions:

```java
@TestPropertySource(locations = "classpath:/test.properties")
@EmbeddedKafka(topics = { "any-topic", "${kafka.topics.another-topic}" },
        brokerProperties = { "log.dir=${kafka.broker.logs-dir}",
                            "listeners=PLAINTEXT://localhost:${kafka.broker.port}",
                            "auto.create.topics.enable=${kafka.broker.topics-enable:true}" },
        brokerPropertiesLocation = "classpath:/broker.properties")
```

In the preceding example, the property placeholders `${kafka.topics.another-topic}`, `${kafka.broker.logs-dir}`, and `${kafka.broker.port}` are resolved from the Spring `Environment`.
In addition, the broker properties are loaded from the `broker.properties` classpath resource specified by the `brokerPropertiesLocation`.
Property placeholders are resolved for the `brokerPropertiesLocation` URL and for any property placeholders found in the resource.
Properties defined by `brokerProperties` override properties found in `brokerPropertiesLocation`.

You can use the `@EmbeddedKafka` annotation with JUnit Jupiter.

<a id="testing--embedded-kafka-junit-jupiter"></a>
<a id="testing--embeddedkafka-annotation-with-junit-jupiter"></a>

## `@EmbeddedKafka` Annotation with JUnit Jupiter

Starting with version 2.3, there are two ways to use the `@EmbeddedKafka` annotation with JUnit Jupiter.
When used with the `@SpringJunitConfig` annotation, the embedded broker is added to the test application context.
You can auto wire the broker into your test, at the class or method level, to get the broker address list.

When **not** using the spring test context, the `EmbdeddedKafkaCondition` creates a broker; the condition includes a parameter resolver so you can access the broker in your test method.

```java
@EmbeddedKafka public class EmbeddedKafkaConditionTests {
@Test public void test(EmbeddedKafkaBroker broker) {String brokerList = broker.getBrokersAsString(); ...}
}
```

A standalone broker (outside the Spring’s TestContext) will be created unless a class annotated `@EmbeddedKafka` is also annotated (or meta-annotated) with `ExtendWith(SpringExtension.class)`.
`@SpringJunitConfig` and `@SpringBootTest` are so meta-annotated and the context-based broker will be used when either of those annotations are also present.

> [!IMPORTANT]
> When there is a Spring test application context available, the topics and broker properties can contain property placeholders, which will be resolved as long as the property is defined somewhere.
> If there is no Spring context available, these placeholders won’t be resolved.

<a id="testing--embedded-broker-in-springboottest-annotations"></a>

## Embedded Broker in `@SpringBootTest` Annotations

[Spring Initializr](https://start.spring.io/) now automatically adds the `spring-kafka-test` dependency in test scope to the project configuration.

> [!IMPORTANT]
> If your application uses the Kafka binder in `spring-cloud-stream` and if you want to use an embedded broker for tests, you must remove the `spring-cloud-stream-test-support` dependency, because it replaces the real binder with a test binder for test cases.
> If you wish some tests to use the test binder and some to use the embedded broker, tests that use the real binder need to disable the test binder by excluding the binder auto configuration in the test class.
> The following example shows how to do so:
>
> ```java
> @SpringJUnitConfig
> @SpringBootTest(properties = "spring.autoconfigure.exclude="
>     + "org.springframework.cloud.stream.test.binder.TestSupportBinderAutoConfiguration")
> public class MyApplicationTests {
>     ...
> }
> ```

There are several ways to use an embedded broker in a Spring Boot application test.

They include:

- [`@EmbeddedKafka` Annotation or `EmbeddedKafkaBroker` Bean](#testing--kafka-testing-embeddedkafka-annotation)

<a id="testing--embedded-broker-with-springjunitconfig-annotations"></a>
<a id="testing--embeddedkafka-with-springjunitconfig"></a>

## `@EmbeddedKafka` with `@SpringJunitConfig`

When using `@EmbeddedKafka` with `@SpringJUnitConfig`, it is recommended to use `@DirtiesContext` on the test class.
This is to prevent potential race conditions occurring during the JVM shutdown after running multiple tests in a test suite.
For example, without using `@DirtiesContext`, the `EmbeddedKafkaBroker` may shutdown earlier while the application context still needs resources from it.
Since every `EmbeddedKafka` test-runs create its own temporary directory, when this race condition occurs, it will produce error log messages indicating that the files that it is trying to delete or cleanup are not available anymore.
Adding `@DirtiesContext` will ensure that the application context is cleaned up after each test and not cached, making it less vulnerable to potential resource race conditions like these.

<a id="testing--kafka-testing-embeddedkafka-annotation"></a>
<a id="testing--embeddedkafka-annotation-or-embeddedkafkabroker-bean"></a>

### `@EmbeddedKafka` Annotation or `EmbeddedKafkaBroker` Bean

The following example shows how to use an `@EmbeddedKafka` Annotation to create an embedded broker:

```java
@SpringJUnitConfig @EmbeddedKafka(topics = "someTopic",bootstrapServersProperty = "spring.kafka.bootstrap-servers") // this is now the default public class MyApplicationTests {
@Autowired private KafkaTemplate<String, String> template;
@Test void test() {...}
}
```

> [!NOTE]
> The `bootstrapServersProperty` is automatically set to `spring.kafka.bootstrap-servers` by default, starting with version 3.0.10.

<a id="testing--hamcrest-matchers"></a>

## Hamcrest Matchers

The `org.springframework.kafka.test.hamcrest.KafkaMatchers` provides the following matchers:

```java
/** * @param key the key * @param <K> the type.* @return a Matcher that matches the key in a consumer record.*/ public static <K> Matcher<ConsumerRecord<K, ?>> hasKey(K key) { ... }
/** * @param value the value.* @param <V> the type.* @return a Matcher that matches the value in a consumer record.*/ public static <V> Matcher<ConsumerRecord<?, V>> hasValue(V value) { ... }
/** * @param partition the partition.* @return a Matcher that matches the partition in a consumer record.*/ public static Matcher<ConsumerRecord<?, ?>> hasPartition(int partition) { ... }
/** * Matcher testing the timestamp of a {@link ConsumerRecord} assuming the topic has been set with * {@link org.apache.kafka.common.record.TimestampType#CREATE_TIME CreateTime}.* * @param ts timestamp of the consumer record.* @return a Matcher that matches the timestamp in a consumer record.*/ public static Matcher<ConsumerRecord<?, ?>> hasTimestamp(long ts) {return hasTimestamp(TimestampType.CREATE_TIME, ts);}
/** * Matcher testing the timestamp of a {@link ConsumerRecord} * @param type timestamp type of the record * @param ts timestamp of the consumer record.* @return a Matcher that matches the timestamp in a consumer record.*/ public static Matcher<ConsumerRecord<?, ?>> hasTimestamp(TimestampType type, long ts) {return new ConsumerRecordTimestampMatcher(type, ts);}
```

<a id="testing--assertj-conditions"></a>

## AssertJ Conditions

You can use the following AssertJ conditions:

```java
/** * @param key the key * @param <K> the type.* @return a Condition that matches the key in a consumer record.*/ public static <K> Condition<ConsumerRecord<K, ?>> key(K key) { ... }
/** * @param value the value.* @param <V> the type.* @return a Condition that matches the value in a consumer record.*/ public static <V> Condition<ConsumerRecord<?, V>> value(V value) { ... }
/** * @param key the key.* @param value the value.* @param <K> the key type.* @param <V> the value type.* @return a Condition that matches the key in a consumer record.* @since 2.2.12 */ public static <K, V> Condition<ConsumerRecord<K, V>> keyValue(K key, V value) { ... }
/** * @param partition the partition.* @return a Condition that matches the partition in a consumer record.*/ public static Condition<ConsumerRecord<?, ?>> partition(int partition) { ... }
/** * @param value the timestamp.* @return a Condition that matches the timestamp value in a consumer record.*/ public static Condition<ConsumerRecord<?, ?>> timestamp(long value) {return new ConsumerRecordTimestampCondition(TimestampType.CREATE_TIME, value);}
/** * @param type the type of timestamp * @param value the timestamp.* @return a Condition that matches the timestamp value in a consumer record.*/ public static Condition<ConsumerRecord<?, ?>> timestamp(TimestampType type, long value) {return new ConsumerRecordTimestampCondition(type, value);}
```

<a id="testing--example"></a>

## Example

The following example brings together most of the topics covered in this chapter:

```java
@EmbeddedKafka(topics = KafkaTemplateTests.TEMPLATE_TOPIC)
public class KafkaTemplateTests {

    public static final String TEMPLATE_TOPIC = "templateTopic";
    public static EmbeddedKafkaBroker embeddedKafka;

    @BeforeAll
	public static void setUp() {
		embeddedKafka = EmbeddedKafkaCondition.getBroker();
	}

    @Test
    public void testTemplate() throws Exception {
        Map<String, Object> consumerProps = KafkaTestUtils.consumerProps("testT", "false",
            embeddedKafka);
        DefaultKafkaConsumerFactory<Integer, String> cf =
                            new DefaultKafkaConsumerFactory<>(consumerProps);
        ContainerProperties containerProperties = new ContainerProperties(TEMPLATE_TOPIC);
        KafkaMessageListenerContainer<Integer, String> container =
                            new KafkaMessageListenerContainer<>(cf, containerProperties);
        final BlockingQueue<ConsumerRecord<Integer, String>> records = new LinkedBlockingQueue<>();
        container.setupMessageListener(new MessageListener<Integer, String>() {

            @Override
            public void onMessage(ConsumerRecord<Integer, String> record) {
                System.out.println(record);
                records.add(record);
            }

        });
        container.setBeanName("templateTests");
        container.start();
        ContainerTestUtils.waitForAssignment(container,
                            embeddedKafka.getPartitionsPerTopic());
        Map<String, Object> producerProps =
                            KafkaTestUtils.producerProps(embeddedKafka);
        ProducerFactory<Integer, String> pf =
                            new DefaultKafkaProducerFactory<>(producerProps);
        KafkaTemplate<Integer, String> template = new KafkaTemplate<>(pf);
        template.setDefaultTopic(TEMPLATE_TOPIC);
        template.sendDefault("foo");
        assertThat(records.poll(10, TimeUnit.SECONDS), hasValue("foo"));
        template.sendDefault(0, 2, "bar");
        ConsumerRecord<Integer, String> received = records.poll(10, TimeUnit.SECONDS);
        assertThat(received, hasKey(2));
        assertThat(received, hasPartition(0));
        assertThat(received, hasValue("bar"));
        template.send(TEMPLATE_TOPIC, 0, 2, "baz");
        received = records.poll(10, TimeUnit.SECONDS);
        assertThat(received, hasKey(2));
        assertThat(received, hasPartition(0));
        assertThat(received, hasValue("baz"));
    }
}
```

The preceding example uses the Hamcrest matchers.
With `AssertJ`, the final part looks like the following code:

```java
assertThat(records.poll(10, TimeUnit.SECONDS)).has(value("foo"));
template.sendDefault(0, 2, "bar");
ConsumerRecord<Integer, String> received = records.poll(10, TimeUnit.SECONDS);
// using individual assertions
assertThat(received).has(key(2));
assertThat(received).has(value("bar"));
assertThat(received).has(partition(0));
template.send(TEMPLATE_TOPIC, 0, 2, "baz");
received = records.poll(10, TimeUnit.SECONDS);
// using allOf()
assertThat(received).has(allOf(keyValue(2, "baz"), partition(0)));
```

<a id="testing--mock-cons-prod"></a>
<a id="testing--mock-consumer-and-producer"></a>

## Mock Consumer and Producer

The `kafka-clients` library provides `MockConsumer` and `MockProducer` classes for testing purposes.

If you wish to use these classes in some of your tests with listener containers or `KafkaTemplate` respectively, starting with version 3.0.7, the framework now provides `MockConsumerFactory` and `MockProducerFactory` implementations.

These factories can be used in the listener container and template instead of the default factories, which require a running (or embedded) broker.

Here is an example of a simple implementation returning a single consumer:

```java
@Bean
ConsumerFactory<String, String> consumerFactory() {
    MockConsumer<String, String> consumer = new MockConsumer<>(OffsetResetStrategy.EARLIEST);
    TopicPartition topicPartition0 = new TopicPartition("topic", 0);
    List<TopicPartition> topicPartitions = Collections.singletonList(topicPartition0);
    Map<TopicPartition, Long> beginningOffsets = topicPartitions.stream().collect(Collectors
            .toMap(Function.identity(), tp -> 0L));
    consumer.updateBeginningOffsets(beginningOffsets);
    consumer.schedulePollTask(() -> {
        consumer.addRecord(
                new ConsumerRecord<>("topic", 0, 0L, 0L, TimestampType.NO_TIMESTAMP_TYPE, 0, 0, null, "test1",
                        new RecordHeaders(), Optional.empty()));
        consumer.addRecord(
                new ConsumerRecord<>("topic", 0, 1L, 0L, TimestampType.NO_TIMESTAMP_TYPE, 0, 0, null, "test2",
                        new RecordHeaders(), Optional.empty()));
    });
    return new MockConsumerFactory(() -> consumer);
}
```

If you wish to test with concurrency, the `Supplier` lambda in the factory’s constructor would need to create a new instance each time.

With the `MockProducerFactory`, there are two constructors; one to create a simple factory, and one to create factory that supports transactions.

Here are examples:

```java
@Bean
ProducerFactory<String, String> nonTransFactory() {
    return new MockProducerFactory<>(() ->
            new MockProducer<>(true, new StringSerializer(), new StringSerializer()));
}

@Bean
ProducerFactory<String, String> transFactory() {
    MockProducer<String, String> mockProducer =
            new MockProducer<>(true, new StringSerializer(), new StringSerializer());
    mockProducer.initTransactions();
    return new MockProducerFactory<String, String>((tx, id) -> mockProducer, "defaultTxId");
}
```

Notice in the second case, the lambda is a `BiFunction<Boolean, String>` where the first parameter is true if the caller wants a transactional producer; the optional second parameter contains the transactional id.
This can be the default (as provided in the constructor), or can be overridden by the `KafkaTransactionManager` (or `KafkaTemplate` for local transactions), if so configured.
The transactional id is provided in case you wish to use a different `MockProducer` based on this value.

If you are using producers in a multi-threaded environment, the `BiFunction` should return multiple producers (perhaps thread-bound using a `ThreadLocal`).

> [!IMPORTANT]
> Transactional `MockProducer`s must be initialized for transactions by calling `initTransaction()`.

When using the `MockProducer`, if you do not want to close the producer after each send, then you can provide a custom `MockProducer` implementation that overrides the `close` method that does not call the `close` method from the super class.
This is convenient for testing, when verifying multiple publishing on the same producer without closing it.

Here is an example:

```java
@Bean MockProducer<String, String> mockProducer() {return new MockProducer<>(false, new StringSerializer(), new StringSerializer()) {@Override public void close() {
} };}
@Bean ProducerFactory<String, String> mockProducerFactory(MockProducer<String, String> mockProducer) {return new MockProducerFactory<>(() -> mockProducer);}
```

[Apache Kafka Streams Support](#streams)
[Tips, Tricks and Examples](#tips)

---

<a id="tips"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/tips.html -->

<!-- page_index: 66 -->

# Tips, Tricks and Examples

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tips--page-title"></a>
<a id="tips--tips-tricks-and-examples"></a>

# Tips, Tricks and Examples

<a id="tips--tip-assign-all-parts"></a>
<a id="tips--manually-assigning-all-partitions"></a>

## Manually Assigning All Partitions

Let’s say you want to always read all records from all partitions (such as when using a compacted topic to load a distributed cache), it can be useful to manually assign the partitions and not use Kafka’s group management.
Doing so can be unwieldy when there are many partitions, because you have to list the partitions.
It’s also an issue if the number of partitions changes over time, because you would have to recompile your application each time the partition count changes.

The following is an example of how to use the power of a SpEL expression to create the partition list dynamically when the application starts:

```java
@KafkaListener(topicPartitions = @TopicPartition(topic = "compacted",partitions = "#{@finder.partitions('compacted')}",partitionOffsets = @PartitionOffset(partition = "*", initialOffset = "0"))) public void listen(@Header(KafkaHeaders.RECEIVED_KEY) String key, String payload) {...}
@Bean public PartitionFinder finder(ConsumerFactory<String, String> consumerFactory) {return new PartitionFinder(consumerFactory);}
public static class PartitionFinder {
private final ConsumerFactory<String, String> consumerFactory;
public PartitionFinder(ConsumerFactory<String, String> consumerFactory) {this.consumerFactory = consumerFactory;}
public String[] partitions(String topic) {try (Consumer<String, String> consumer = consumerFactory.createConsumer()) {return consumer.partitionsFor(topic).stream() .map(pi -> "" + pi.partition()) .toArray(String[]::new);}}
}
```

Using this in conjunction with `ConsumerConfig.AUTO_OFFSET_RESET_CONFIG=earliest` will load all records each time the application is started.
You should also set the container’s `AckMode` to `MANUAL` to prevent the container from committing offsets for a `null` consumer group.
Starting with version 3.1, the container will automatically coerce the `AckMode` to `MANUAL` when manual topic assignment is used with no consumer `group.id`.
However, starting with version 2.5.5, as shown above, you can apply an initial offset to all partitions; see [Explicit Partition Assignment](#kafka-receiving-messages-listener-annotation--manual-assignment) for more information.

<a id="tips--ex-jdbc-sync"></a>
<a id="tips--examples-of-kafka-transactions-with-other-transaction-managers"></a>

## Examples of Kafka Transactions with Other Transaction Managers

The following Spring Boot application is an example of chaining database and Kafka transactions.
The listener container starts the Kafka transaction and the `@Transactional` annotation starts the DB transaction.
The DB transaction is committed first; if the Kafka transaction fails to commit, the record will be redelivered so the DB update should be idempotent.

```java
@SpringBootApplication public class Application {
public static void main(String[] args) {SpringApplication.run(Application.class, args);}
@Bean public ApplicationRunner runner(KafkaTemplate<String, String> template) {return args -> template.executeInTransaction(t -> t.send("topic1", "test"));}
@Bean public DataSourceTransactionManager dstm(DataSource dataSource) {return new DataSourceTransactionManager(dataSource);}
@Component public static class Listener {
private final JdbcTemplate jdbcTemplate;
private final KafkaTemplate<String, String> kafkaTemplate;
public Listener(JdbcTemplate jdbcTemplate, KafkaTemplate<String, String> kafkaTemplate) {this.jdbcTemplate = jdbcTemplate; this.kafkaTemplate = kafkaTemplate;}
@KafkaListener(id = "group1", topics = "topic1") @Transactional("dstm") public void listen1(String in) {this.kafkaTemplate.send("topic2", in.toUpperCase()); this.jdbcTemplate.execute("insert into mytable (data) values ('" + in + "')");}
@KafkaListener(id = "group2", topics = "topic2") public void listen2(String in) {System.out.println(in);}
}
@Bean public NewTopic topic1() {return TopicBuilder.name("topic1").build();}
@Bean public NewTopic topic2() {return TopicBuilder.name("topic2").build();}
}
```

```properties
spring.datasource.url=jdbc:mysql://localhost/integration?serverTimezone=UTC
spring.datasource.username=root
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

spring.kafka.consumer.auto-offset-reset=earliest
spring.kafka.consumer.enable-auto-commit=false
spring.kafka.consumer.properties.isolation.level=read_committed

spring.kafka.producer.transaction-id-prefix=tx-

#logging.level.org.springframework.transaction=trace
#logging.level.org.springframework.kafka.transaction=debug
#logging.level.org.springframework.jdbc=debug
```

```sql
create table mytable (data varchar(20));
```

For producer-only transactions, transaction synchronization works:

```java
@Transactional("dstm")
public void someMethod(String in) {
    this.kafkaTemplate.send("topic2", in.toUpperCase());
    this.jdbcTemplate.execute("insert into mytable (data) values ('" + in + "')");
}
```

The `KafkaTemplate` will synchronize its transaction with the DB transaction and the commit/rollback occurs after the database.

If you wish to commit the Kafka transaction first, and only commit the DB transaction if the Kafka transaction is successful, use nested `@Transactional` methods:

```java
@Transactional("dstm") public void someMethod(String in) {this.jdbcTemplate.execute("insert into mytable (data) values ('" + in + "')"); sendToKafka(in);}
@Transactional("kafkaTransactionManager") public void sendToKafka(String in) {this.kafkaTemplate.send("topic2", in.toUpperCase());}
```

<a id="tips--tip-json"></a>
<a id="tips--customizing-the-jsonserializer-and-jsondeserializer"></a>

## Customizing the JsonSerializer and JsonDeserializer

The serializer and deserializer support a number of customizations using properties, see [JSON](#kafka-serdes--json-serde) for more information.
The `kafka-clients` code, not Spring, instantiates these objects, unless you inject them directly into the consumer and producer factories.
If you wish to configure the (de)serializer using properties, but wish to use, say, a custom `JsonMapper`, simply create a subclass and pass the custom mapper into the `super` constructor. For example:

```java
public class CustomJsonSerializer extends JacksonJsonSerializer<Object> {
public CustomJsonSerializer() {super(customizedJsonMapper());}
private static JsonMapper customizedJsonMapper() {return JacksonMapperUtils.enhancedJsonMapper() .rebuild() // .enable() and/or .disable() features according to your needs .build();}}
```

[Testing Applications](#testing)
[Other Resources](#other-resources)

---

<a id="other-resources"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/other-resources.html -->

<!-- page_index: 67 -->

# Other Resources

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="other-resources--page-title"></a>
<a id="other-resources--other-resources"></a>

# Other Resources

In addition to this reference documentation, we recommend a number of other resources that may help you learn about Spring and Apache Kafka.

- [Apache Kafka Project Home Page](https://kafka.apache.org)
- [Spring for Apache Kafka Home Page](https://projects.spring.io/spring-kafka/)
- [Spring for Apache Kafka GitHub Repository](https://github.com/spring-projects/spring-kafka)
- [Spring Integration GitHub Repository (Apache Kafka Module)](https://github.com/spring-projects/spring-integration)

[Tips, Tricks and Examples](#tips)
[Override Spring Boot Dependencies](#appendix-override-boot-dependencies)

---

<a id="appendix-override-boot-dependencies"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/appendix/override-boot-dependencies.html -->

<!-- page_index: 68 -->

# Override Spring Boot Dependencies

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-override-boot-dependencies--page-title"></a>
<a id="appendix-override-boot-dependencies--override-spring-boot-dependencies"></a>

# Override Spring Boot Dependencies

When using Spring for Apache Kafka in a Spring Boot application, the Apache Kafka dependency versions are determined by Spring Boot’s dependency management.
If you wish to use a different version of `kafka-clients` or `kafka-streams`, and use the embedded kafka broker for testing, you need to override their version used by Spring Boot dependency management; set the `kafka.version` property.

> [!NOTE]
> Both Spring Boot 3.5.x and 3.4.x use the `kafka-clients` version 3.8.x and if users need to use 3.9.x client, they have to manually upgrade it using the method below.

Or, to use a different Spring for Apache Kafka version with a supported Spring Boot version, set the `spring-kafka.version` property.

- Maven
- Gradle

```xml
<properties>
    <kafka.version>4.0.0</kafka.version>
    <spring-kafka.version>4.1.0</spring-kafka.version>
</properties>

<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>
<!-- optional - only needed when using kafka-streams -->
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka-test</artifactId>
    <scope>test</scope>
</dependency>
```

```groovy
ext['kafka.version'] = '3.5.0'
ext['spring-kafka.version'] = '4.1.0'

dependencies {
    implementation 'org.springframework.kafka:spring-kafka'
    implementation 'org.apache.kafka:kafka-streams' // optional - only needed when using kafka-streams
    testImplementation 'org.springframework.kafka:spring-kafka-test'
}
```

The test scope dependencies are only needed if you are using the embedded Kafka broker in tests.

[Other Resources](#other-resources)
[Micrometer Observation Documentation](#appendix-micrometer)

---

<a id="appendix-micrometer"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/appendix/micrometer.html -->

<!-- page_index: 69 -->

# Micrometer Observation Documentation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-micrometer--page-title"></a>
<a id="appendix-micrometer--micrometer-observation-documentation"></a>

# Micrometer Observation Documentation

<a id="appendix-micrometer--observability-metrics"></a>

## Observability - Metrics

Below you can find a list of all metrics declared by this project.

<a id="appendix-micrometer--observability-metrics-listener-observation"></a>
<a id="appendix-micrometer--listener-observation"></a>

### Listener Observation

> Observation for Apache Kafka listeners.

**Metric name** `spring.kafka.listener` (defined by convention class `KafkaListenerObservation$DefaultKafkaListenerObservationConvention`). **Type** `timer`.

**Metric name** `spring.kafka.listener.active` (defined by convention class `KafkaListenerObservation$DefaultKafkaListenerObservationConvention`). **Type** `long task timer`.

> [!IMPORTANT]
> KeyValues that are added after starting the Observation might be missing from the \*.active metrics.

> [!IMPORTANT]
> Micrometer internally uses `nanoseconds` for the baseunit. However, each backend determines the actual baseunit. (i.e. Prometheus uses seconds)

Name of the enclosing class `KafkaListenerObservation`.

| Name | Description |
| --- | --- |
| `messaging.kafka.consumer.group` *(required)* | Messaging the consumer group. |
| `messaging.operation` *(required)* | Messaging operation. |
| `messaging.source.kind` *(required)* | Messaging source kind. |
| `messaging.source.name` *(required)* | Messaging source name. |
| `messaging.system` *(required)* | Messaging system. |
| `spring.kafka.listener.id` *(required)* | Listener id (or listener container bean name). |

<a id="appendix-micrometer--observability-metrics-template-observation"></a>
<a id="appendix-micrometer--template-observation"></a>

### Template Observation

> Observation for KafkaTemplates.

**Metric name** `spring.kafka.template` (defined by convention class `KafkaTemplateObservation$DefaultKafkaTemplateObservationConvention`). **Type** `timer`.

**Metric name** `spring.kafka.template.active` (defined by convention class `KafkaTemplateObservation$DefaultKafkaTemplateObservationConvention`). **Type** `long task timer`.

> [!IMPORTANT]
> KeyValues that are added after starting the Observation might be missing from the \*.active metrics.

> [!IMPORTANT]
> Micrometer internally uses `nanoseconds` for the baseunit. However, each backend determines the actual baseunit. (i.e. Prometheus uses seconds)

Name of the enclosing class `KafkaTemplateObservation`.

| Name | Description |
| --- | --- |
| `messaging.destination.kind` *(required)* | Messaging destination kind. |
| `messaging.destination.name` *(required)* | Messaging destination name. |
| `messaging.operation` *(required)* | Messaging operation. |
| `messaging.system` *(required)* | Messaging system. |
| `spring.kafka.template.name` *(required)* | Bean name of the template. |

<a id="appendix-micrometer--observability-spans"></a>

## Observability - Spans

Below you can find a list of all spans declared by this project.

<a id="appendix-micrometer--observability-spans-listener-observation"></a>
<a id="appendix-micrometer--listener-observation-span"></a>

### Listener Observation Span

> Observation for Apache Kafka listeners.

**Span name** `spring.kafka.listener` (defined by convention class `KafkaListenerObservation$DefaultKafkaListenerObservationConvention`).

Name of the enclosing class `KafkaListenerObservation`.

| Name | Description |
| --- | --- |
| `messaging.consumer.id` *(required)* | Messaging consumer id (consumer group and client id). |
| `messaging.kafka.client_id` *(required)* | Messaging client id. |
| `messaging.kafka.consumer.group` *(required)* | Messaging the consumer group. |
| `messaging.kafka.message.offset` *(required)* | Messaging message offset. |
| `messaging.kafka.source.partition` *(required)* | Messaging partition. |
| `messaging.operation` *(required)* | Messaging operation. |
| `messaging.source.kind` *(required)* | Messaging source kind. |
| `messaging.source.name` *(required)* | Messaging source name. |
| `messaging.system` *(required)* | Messaging system. |
| `spring.kafka.listener.id` *(required)* | Listener id (or listener container bean name). |

<a id="appendix-micrometer--observability-spans-template-observation"></a>
<a id="appendix-micrometer--template-observation-span"></a>

### Template Observation Span

> Observation for KafkaTemplates.

**Span name** `spring.kafka.template` (defined by convention class `KafkaTemplateObservation$DefaultKafkaTemplateObservationConvention`).

Name of the enclosing class `KafkaTemplateObservation`.

| Name | Description |
| --- | --- |
| `messaging.destination.kind` *(required)* | Messaging destination kind. |
| `messaging.destination.name` *(required)* | Messaging destination name. |
| `messaging.operation` *(required)* | Messaging operation. |
| `messaging.system` *(required)* | Messaging system. |
| `spring.kafka.template.name` *(required)* | Bean name of the template. |

<a id="appendix-micrometer--observability-conventions"></a>

## Observability - Conventions

Below you can find a list of all `GlobalObservationConvention` and `ObservationConvention` declared by this project.

| ObservationConvention Class Name | Applicable ObservationContext Class Name |
| --- | --- |
| `KafkaListenerObservation` | `KafkaRecordReceiverContext` |
| `KafkaListenerObservation.DefaultKafkaListenerObservationConvention` | `KafkaRecordReceiverContext` |
| `KafkaListenerObservationConvention` | `KafkaRecordReceiverContext` |
| `KafkaTemplateObservation` | `KafkaRecordSenderContext` |
| `KafkaTemplateObservation.DefaultKafkaTemplateObservationConvention` | `KafkaRecordSenderContext` |
| `KafkaTemplateObservationConvention` | `KafkaRecordSenderContext` |

[Override Spring Boot Dependencies](#appendix-override-boot-dependencies)
[Native Images](#appendix-native-images)

---

<a id="appendix-native-images"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/appendix/native-images.html -->

<!-- page_index: 70 -->

# Native Images

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-native-images--page-title"></a>
<a id="appendix-native-images--native-images"></a>

# Native Images

[Spring AOT](https://docs.spring.io/spring-framework/reference/7.0/core/aot.html) native hints are provided to assist in developing native images for Spring applications that use Spring for Apache Kafka, including hints for AVRO generated classes used in `@KafkaListener`s.

> [!IMPORTANT]
> `spring-kafka-test` (and, specifically, its `EmbeddedKafkaBroker`) is not supported in native images.

Some examples can be seen in the [`spring-aot-smoke-tests` GitHub repository](https://github.com/spring-projects/spring-aot-smoke-tests/tree/main/integration).

[Micrometer Observation Documentation](#appendix-micrometer)
[Change History](#appendix-change-history)

---

<a id="appendix-change-history"></a>

<!-- source_url: https://docs.spring.io/spring-kafka/reference/appendix/change-history.html -->

<!-- page_index: 71 -->

# Change History

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-change-history--page-title"></a>
<a id="appendix-change-history--change-history"></a>

# Change History

<a id="appendix-change-history--whats-new-in-4-0-since-3-3"></a>
<a id="appendix-change-history--what-s-new-in-4.0-since-3.3"></a>

## What’s New in 4.0 Since 3.3

This section covers the changes made from version 3.3 to version 4.0.
For changes in earlier versions, see [Change History](#appendix-change-history).

<a id="appendix-change-history--x40-apache-kafka-4-0-upgrade"></a>
<a id="appendix-change-history--apache-kafka-4.0-client-upgrade"></a>

### Apache Kafka 4.0 Client Upgrade

Spring for Apache Kafka has been upgraded to use Apache Kafka client version `4.0.0`.
This upgrade brings several important changes:

- All ZooKeeper-based functionality has been removed as Kafka 4.0 fully transitions to KRaft mode
- The ZooKeeper dependency has been removed from the project
- The embedded Kafka test framework now exclusively uses KRaft mode
- The `EmbeddedKafkaZKBroker` class has been removed, and all functionality is now handled by `EmbeddedKafkaKraftBroker`

<a id="appendix-change-history--x40-embedded-kafka-test-changes"></a>
<a id="appendix-change-history--embedded-kafka-test-framework-changes"></a>

### Embedded Kafka Test Framework Changes

The test infrastructure has been significantly updated:

- The `EmbeddedKafkaRule` JUnit 4 rule has been removed
- The `@EmbeddedKafka` annotation has been simplified with the removal of ZooKeeper-related properties:
- The `kraft` property has been removed as KRaft mode is now the only option
- ZooKeeper-specific properties like `zookeeperPort`, `zkConnectionTimeout`, and `zkSessionTimeout` have been removed
- KafkaClusterTestKit imports now use new packages for KRaft mode
- Some tests have been updated to address limitations with static port assignments in KRaft mode
- Adjustments have been made to replication factors in tests to accommodate KRaft requirements

<a id="appendix-change-history--x40-consumer-records-constructor-changes"></a>
<a id="appendix-change-history--consumerrecords-constructor-changes"></a>

### ConsumerRecords Constructor Changes

The `ConsumerRecords` constructor now requires an additional `Map` parameter, which has been addressed throughout the framework.
Applications that directly use this constructor will need to update their code.

<a id="appendix-change-history--x40-producer-interface-updates"></a>
<a id="appendix-change-history--producer-interface-updates"></a>

### Producer Interface Updates

New methods from the Kafka Producer interface have been implemented:

- `registerMetricForSubscription`
- `unregisterMetricFromSubscription`

<a id="appendix-change-history--x40-removed-deprecated-functionality"></a>
<a id="appendix-change-history--removed-deprecated-functionality"></a>

### Removed Deprecated Functionality

Several deprecated items have been removed:

- The deprecated `partitioner` classes have been removed from runtime hints
- The deprecated `sendOffsetsToTransaction` method that used `String consumerGroupId` has been removed

<a id="appendix-change-history--x40-kafka-streams-updates"></a>
<a id="appendix-change-history--kafka-streams-api-changes"></a>

### Kafka Streams API Changes

- `KafkaStreamBrancher` has been updated to use the new `split()` and `branch()` methods instead of the deprecated `branch()` method
- The `DeserializationExceptionHandler` has been updated to use the new `ErrorHandlerContext`

<a id="appendix-change-history--x40-internal-api-updates"></a>
<a id="appendix-change-history--internal-api-updates-related-to-apache-kafka-4.0.0"></a>

### Internal API Updates related to Apache Kafka 4.0.0

- The `BrokerAddress` class now uses `org.apache.kafka.server.network.BrokerEndPoint` instead of the deprecated `kafka.cluster.BrokerEndPoint`
- The `GlobalEmbeddedKafkaTestExecutionListener` has been updated to work solely with KRaft mode

<a id="appendix-change-history--x40-new-consumer-rebalance-protocol"></a>
<a id="appendix-change-history--new-consumer-rebalance-protocol"></a>

### New Consumer Rebalance Protocol

Spring for Apache Kafka 4.0 supports Kafka 4.0’s new consumer rebalance protocol - [KIP-848](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol).
For details, see [New Consumer Rebalance Protocol docs](#kafka-receiving-messages-rebalance-listeners--new-rebalance-protocol).

<a id="appendix-change-history--x40-multi-value-header"></a>
<a id="appendix-change-history--support-multi-value-header"></a>

### Support multi-value header

The `JsonKafkaHeaderMapper` and `SimpleKafkaHeaderMapper` support multi-value header mapping for Kafka records.
More details are available in [Support multi-value header mapping](#kafka-headers--multi-value-header).

<a id="appendix-change-history--x40-add-record-interceptor"></a>
<a id="appendix-change-history--configure-additional-recordinterceptor"></a>

### Configure additional `RecordInterceptor`

Listener containers now support interceptor customization via `getRecordInterceptor()`.
See the [Message Listener Containers](#kafka-receiving-messages-message-listener-container--message-listener-container) section for details.

<a id="appendix-change-history--x40-batch-observability"></a>
<a id="appendix-change-history--per-record-observation-in-batch-listeners"></a>

### Per-Record Observation in Batch Listeners

It is now possible to get an observation for each record when using a batch listener.
See [Observability for Batch Listeners](#kafka-micrometer--batch-listener-obs) for more information.

<a id="appendix-change-history--x40-kafka-queues"></a>
<a id="appendix-change-history--kafka-queues-share-consumer-support"></a>

### Kafka Queues (Share Consumer) Support

Spring for Apache Kafka now provides early access support for Kafka Queues through share consumers, which are part of Apache Kafka 4.0.0 and implement KIP-932.
This enables cooperative consumption where multiple consumers can consume from the same partitions simultaneously, providing better load distribution compared to traditional consumer groups.
See [Kafka Queues (Share Consumer)](#kafka-kafka-queues) for more information.

<a id="appendix-change-history--x40-jackson3-support"></a>
<a id="appendix-change-history--jackson-3-support"></a>

### Jackson 3 Support

Spring for Apache Kafka now provides comprehensive support for Jackson 3 alongside existing Jackson 2 support.
Jackson 3 is automatically detected and preferred when available, providing enhanced performance and modern JSON processing capabilities.

All Jackson 2 classes now have Jackson 3 counterparts with consistent naming and improved type safety:

- `JsonKafkaHeaderMapper` replaces `DefaultKafkaHeaderMapper`
- `JacksonJsonSerializer/Deserializer` replaces `JsonSerializer/Deserializer`
- `JacksonJsonSerde` replaces `JsonSerde`
- `JacksonJsonMessageConverter` family replaces `JsonMessageConverter` family
- `JacksonProjectingMessageConverter` replaces `ProjectingMessageConverter`
- `DefaultJacksonJavaTypeMapper` replaces `DefaultJackson2JavaTypeMapper`

The new Jackson 3 classes use `JsonMapper` instead of generic `ObjectMapper` for enhanced type safety and leverage Jackson 3’s improved module system and performance optimizations.

**Migration Path**: Existing applications continue to work unchanged with Jackson 2.
To migrate to Jackson 3, simply add Jackson 3 to your classpath and update class references to use the new Jackson 3 equivalents.
The framework automatically detects and prefers Jackson 3 when both versions are present.

**Backward Compatibility**: All Jackson 2 classes are deprecated but remain fully functional.
They will be removed in a future major version.

See [Serialization, Deserialization, and Message Conversion](#kafka-serdes) for configuration examples.

<a id="appendix-change-history--x40-spring-retry-replacement"></a>
<a id="appendix-change-history--spring-retry-dependency-removal"></a>

### Spring Retry Dependency Removal

Spring for Apache Kafka has removed its dependency on Spring Retry in favor of the core retry support introduced in Spring Framework 7.
This is a breaking change that affects retry configuration and APIs throughout the framework.

`BackOffValuesGenerator` that generates the required `BackOff` values upfront, now works directly with Spring Framework’s `BackOff` interface instead of `BackOffPolicy`.
These values are then managed by the listener infrastructure and Spring Retry is no longer involved.

From a configuration standpoint, Spring Kafka relied heavily on Spring Retry’s `@Backoff` annotation.
As there is no equivalent in Spring Framework, the annotation has been moved to Spring Kafka as `@BackOff` with the following improvements:

- Harmonized naming: Uses `@BackOff` instead of `@Backoff` for consistency
- Expression evaluation: All string attributes support SpEL expressions and property placeholders
- Duration format support: String attributes accept `java.util.Duration` formats (e.g., "2s", "500ms")
- Enhanced documentation: Improved Javadoc with clearer explanations

Migration example:

```java
// Before
@RetryableTopic(backoff = @Backoff(delay = 2000, maxDelay = 10000, multiplier = 2))

// After
@RetryableTopic(backOff = @BackOff(delay = 2000, maxDelay = 10000, multiplier = 2))

// With new duration format support
@RetryableTopic(backOff = @BackOff(delayString = "2s", maxDelayString = "10s", multiplier = 2))

// With property placeholders
@RetryableTopic(backOff = @BackOff(delayString = "${retry.delay}", multiplierString = "${retry.multiplier}"))
```

`RetryingDeserializer` no longer offers a `RecoveryCallback` but an equivalent function that takes `RetryException` as input.
This contains the exceptions thrown as well as the number of retry attempts:

```java
// Before retryingDeserializer.setRecoveryCallback(context -> {return fallbackValue; });
// After retryingDeserializer.setRecoveryCallback(retryException -> {return fallbackValue; });
```

The use of `BinaryExceptionClassifier` has been replaced by the newly introduced `ExceptionMatcher`, which provides a polished API.

Additional changes include:

- `DestinationTopicPropertiesFactory` uses `ExceptionMatcher` instead of `BinaryExceptionClassifier`
- The `uniformRandomBackoff` method in `RetryTopicConfigurationBuilder` has been deprecated in favor of jitter support
- Error handling utilities have been updated to work with the new exception matching system
- Kafka Streams retry templates now use Spring Framework’s retry support

Applications must update their configuration to use the new Spring Framework retry APIs, but the retry behavior and functionality remain the same.

<a id="appendix-change-history--what-s-new-in-3-3-since-3-2"></a>
<a id="appendix-change-history--what-s-new-in-3.3-since-3.2"></a>

## What’s New in 3.3 Since 3.2

This section covers the changes made from version 3.2 to version 3.3.
For changes in earlier version, see [Change History](#appendix-change-history).

<a id="appendix-change-history--x33-dlt-topic-naming"></a>
<a id="appendix-change-history--dlt-topic-naming-convention"></a>

### DLT Topic Naming Convention

The naming convention for DLT topics has been standardized to use the "-dlt" suffix consistently. This change ensures compatibility and avoids conflicts when transitioning between different retry solutions. Users who wish to retain the ".DLT" suffix behavior need to opt-in explicitly by setting the appropriate DLT name property.

<a id="appendix-change-history--x33-seek-with-group-id"></a>
<a id="appendix-change-history--enhanced-seek-operations-for-consumer-groups"></a>

### Enhanced Seek Operations for Consumer Groups

A new method, `getGroupId()`, has been added to the `ConsumerSeekCallback` interface.
This method allows for more selective seek operations by targeting only the desired consumer group.
The `AbstractConsumerSeekAware` can also now register, retrieve, and remove all callbacks for each topic partition in a multi-group listener scenario without missing any.
See the new APIs (`getSeekCallbacksFor(TopicPartition topicPartition)`, `getTopicsAndCallbacks()`) for more details.
For more details, see [Seek API Docs](#kafka-seek--seek).

<a id="appendix-change-history--x33-new-option-ignore-empty-batch"></a>
<a id="appendix-change-history--configurable-handling-of-empty-batches-in-kafka-listener-with-recordfilterstrategy"></a>

### Configurable Handling of Empty Batches in Kafka Listener with RecordFilterStrategy

`RecordFilterStrategy` now supports ignoring empty batches that result from filtering.
This can be configured through overriding default method `ignoreEmptyBatch()`, which defaults to false, ensuring `KafkaListener` is invoked even if all `ConsumerRecords` are filtered out.
For more details, see [Message receive filtering Docs](#kafka-receiving-messages-filtering).

<a id="appendix-change-history--x33-concurrent-container-stopped-event"></a>
<a id="appendix-change-history--concurrentcontainerstoppedevent"></a>

### ConcurrentContainerStoppedEvent

The `ConcurentContainerMessageListenerContainer` emits now a `ConcurrentContainerStoppedEvent` when all of its child containers are stopped.
For more details, see [Application Events](#kafka-events) and `ConcurrentContainerStoppedEvent` Javadocs.

<a id="appendix-change-history--x33-original-record-key-in-reply"></a>
<a id="appendix-change-history--original-record-key-in-reply"></a>

### Original Record Key in Reply

When using `ReplyingKafkaTemplate`, if the original record from the request contains a key, then that same key will be part of the reply as well.
For more details, see [Sending Messages](#kafka-sending-messages) section of the reference docs.

<a id="appendix-change-history--x33-customize-logging-in-deadletterpublishingrecovererfactory"></a>
<a id="appendix-change-history--customizing-logging-in-deadletterpublishingrecovererfactory"></a>

### Customizing Logging in DeadLetterPublishingRecovererFactory

When using `DeadLetterPublishingRecovererFactory`, the user applications can override the `maybeLogListenerException` method to customize the logging behavior.

<a id="appendix-change-history--x33-customize-admin-client-in-kafkaadmin"></a>
<a id="appendix-change-history--customize-admin-client-in-kafkaadmin"></a>

### Customize Admin client in KafkaAdmin

When extending `KafkaAdmin`, user applications may override the `createAdmin` method to customize Admin client creation.

<a id="appendix-change-history--x33-customize-kafka-streams-implementation"></a>
<a id="appendix-change-history--customizing-the-implementation-of-kafka-streams"></a>

### Customizing The Implementation of Kafka Streams

When using `KafkaStreamsCustomizer` it is now possible to return a custom implementation of the `KafkaStreams` object by overriding the `initKafkaStreams` method.

<a id="appendix-change-history--x33-kafka-headers-for-batch-listeners"></a>
<a id="appendix-change-history--kafkaheaders.delivery_attempt-for-batch-listeners"></a>

### KafkaHeaders.DELIVERY\_ATTEMPT for batch listeners

When using a `BatchListener`, the `ConsumerRecord` can have the `KafkaHeaders.DELIVERY_ATTMPT` header in its headers fields.
If the `DeliveryAttemptAwareRetryListener` is set to error handler as retry listener, each `ConsumerRecord` has delivery attempt header.
For more details, see [Kafka Headers for Batch Listener](#kafka-annotation-error-handling--delivery-attempts-header-for-batch-listener).

<a id="appendix-change-history--x33-task-scheduler-for-kafka-metrics"></a>
<a id="appendix-change-history--kafka-metrics-listeners-and-taskscheduler"></a>

### Kafka Metrics Listeners and `TaskScheduler`

The `MicrometerProducerListener`, `MicrometerConsumerListener` and `KafkaStreamsMicrometerListener` can now be configured with a `TaskScheduler`.
See `KafkaMetricsSupport` JavaDocs and [Micrometer Support](#kafka-micrometer) for more information.

<a id="appendix-change-history--what-s-new-in-3-2-since-3-1"></a>
<a id="appendix-change-history--what-s-new-in-3.2-since-3.1"></a>

## What’s New in 3.2 Since 3.1

This section covers the changes made from version 3.1 to version 3.2.
For changes in earlier version, see [Change History](#appendix-change-history).

<a id="appendix-change-history--x32-kafka-client-version"></a>
<a id="appendix-change-history--kafka-client-version"></a>

### Kafka Client Version

This version requires 3.7.0 `kafka-clients`.
The 3.7.0 version of Kafka client introduces the new consumer group protocol.
Fore more details and it’s limitations see [KIP-848](https://cwiki.apache.org/confluence/display/KAFKA/The+Next+Generation+of+the+Consumer+Rebalance+Protocol+%28KIP-848%29+-+Early+Access+Release+Notes).
The new consumer group protocol is an early access release and not meant to be used in production.
It is only recommended to use for testing purposes in this version.
Therefore, Spring for Apache Kafka supports this new consumer group protocol only to the extent of such testing level support available in the `kafka-client` itself.
By default, Spring for Apache Kafka uses the classic consumer group protocol and when testing the new consumer group protocol, that needs to be opted-in via the `group.protocol` property on the consumer.

<a id="appendix-change-history--x32-testing-support-changes"></a>
<a id="appendix-change-history--testing-support-changes"></a>

### Testing Support Changes

The `kraft` mode is disabled in `EmbeddedKafka` by default and users wanting to use the `kraft` mode must enable it.
This is due to certain instabilities observed while using `EmbeddedKafka` in `kraft` mode, especially when testing the new consumer group protocol.
The new consumer group protocol is only supported in `kraft` mode and because of this, when testing the new protocol, that needs to be done against a real Kafka cluster and not the one based on the `KafkaClusterTestKit`, which `EmbeddedKafka` is based upon.
In addition, there were some other race conditions observed, while running multiple `KafkaListener` methods with `EmbeddedKafka` in `kraft` mode.
Until these issues are resolved, the `kraft` default on `EmbeddedKafka` will remain as `false`.

<a id="appendix-change-history--x32-kafka-streams-iqs-support"></a>
<a id="appendix-change-history--kafka-streams-interactive-query-support"></a>

### Kafka Streams Interactive Query Support

A new API `KafkaStreamsInteractiveQuerySupport` for accessing queryable stores used in Kafka Streams interactive queries.
See [Kafka Streams Interactive Support](#streams--kafka-streams-iq-support) for more details.

<a id="appendix-change-history--x32-tiss"></a>
<a id="appendix-change-history--transactionidsuffixstrategy"></a>

### TransactionIdSuffixStrategy

A new `TransactionIdSuffixStrategy` interface was introduced to manage `transactional.id` suffix.
The default implementation is `DefaultTransactionIdSuffixStrategy` when setting `maxCache` greater than zero can reuse `transactional.id` within a specific range, otherwise suffixes will be generated on the fly by incrementing a counter.
See [Fixed TransactionIdSuffix](#kafka-transactions--transaction-id-suffix-fixed) for more information.

<a id="appendix-change-history--x32-async-return"></a>
<a id="appendix-change-history--async-kafkalistener-return"></a>

### Async @KafkaListener Return

`@KafkaListener` (and `@KafkaHandler`) methods can now return asynchronous return types include `CompletableFuture<?>`, `Mono<?>` and Kotlin `suspend` functions.
See [Async Returns](#kafka-receiving-messages-async-returns) for more information.

<a id="appendix-change-history--x32-customizable-dlt-routing"></a>
<a id="appendix-change-history--routing-of-messages-to-custom-dlts-based-on-thrown-exceptions"></a>

### Routing of messages to custom DLTs based on thrown exceptions

It’s now possible to redirect messages to the custom DLTs based on the type of the exception, which has been thrown during the message processing.
Rules for the redirection are set either via the `RetryableTopic.exceptionBasedDltRouting` or the `RetryTopicConfigurationBuilder.dltRoutingRules`.
Custom DLTs are created automatically as well as other retry and dead-letter topics.
See [Routing of messages to custom DLTs based on thrown exceptions](#retrytopic-features--exc-based-custom-dlt-routing) for more information.

<a id="appendix-change-history--x32-cp-ptm"></a>
<a id="appendix-change-history--deprecating-containerproperties-transactionmanager-property"></a>

### Deprecating ContainerProperties transactionManager property

Deprecating the `transactionManager` property in `ContainerProperties` in favor of `KafkaAwareTransactionManager`, a narrower type compared to the general `PlatformTransactionManager`. See [ContainerProperties](#kafka-container-props--kafkaawaretransactionmanager) and [Transaction Synchronization](#kafka-transactions--transaction-synchronization).

<a id="appendix-change-history--x32-after-rollback-processing"></a>
<a id="appendix-change-history--after-rollback-processing"></a>

### After Rollback Processing

A new `AfterRollbackProcessor` API `processBatch` is provided.
See [After-rollback Processor](#kafka-annotation-error-handling--after-rollback) for more information.

<a id="appendix-change-history--x32-retry-topic"></a>
<a id="appendix-change-history--change-retryabletopic-sameintervaltopicreusestrategy-default-value"></a>

### Change @RetryableTopic SameIntervalTopicReuseStrategy default value

Change `@RetryableTopic` property `SameIntervalTopicReuseStrategy` default value to `SINGLE_TOPIC`.
See [Single Topic for maxInterval Exponential Delay](#retrytopic-topic-naming--single-topic-maxinterval-delay).

<a id="appendix-change-history--_non_blocking_retries_support_class_level_kafkalistener"></a>
<a id="appendix-change-history--non-blocking-retries-support-class-level-kafkalistener"></a>

### Non-blocking retries support class level @KafkaListener

Non-blocking retries support [@KafkaListener on a Class](#kafka-receiving-messages-class-level-kafkalistener).
See [Non-Blocking Retries](#retrytopic).

<a id="appendix-change-history--_support_process_retryabletopic_on_a_class_in_retrytopicconfigurationprovider"></a>
<a id="appendix-change-history--support-process-retryabletopic-on-a-class-in-retrytopicconfigurationprovider."></a>

### Support process @RetryableTopic on a class in RetryTopicConfigurationProvider.

Provides a new public API to find `RetryTopicConfiguration`.
See [Find RetryTopicConfiguration](#retrytopic-retry-config--find-retry-topic-config)

<a id="appendix-change-history--_retrytopicconfigurer_support_process_multimethodkafkalistenerendpoint"></a>
<a id="appendix-change-history--retrytopicconfigurer-support-process-multimethodkafkalistenerendpoint."></a>

### RetryTopicConfigurer support process MultiMethodKafkaListenerEndpoint.

The `RetryTopicConfigurer` support process and register `MultiMethodKafkaListenerEndpoint`.
The `MultiMethodKafkaListenerEndpoint` provides `getter/setter` for properties `defaultMethod` and `methods`.
Modify the `EndpointCustomizer` that strictly for `MethodKafkaListenerEndpoint` types.
The `EndpointHandlerMethod` add new constructors construct an instance for the provided bean.
Provides new class `EndpointHandlerMultiMethod` to handler multi method for retrying endpoints.

<a id="appendix-change-history--x32-seek-offset-compute-fn"></a>
<a id="appendix-change-history--new-api-method-to-seek-to-an-offset-based-on-a-user-provided-function"></a>

### New API method to seek to an offset based on a user provided function

`ConsumerCallback` provides a new API to seek to an offset based on a user-defined function, which takes the current offset in the consumer as an argument.
See [Seek API Docs](#kafka-seek--seek) for more details.

<a id="appendix-change-history--x32-annotation-partition-offset-seek-position"></a>
<a id="appendix-change-history--partitionoffset-support-for-seekposition"></a>

### @PartitionOffset support for SeekPosition

Adding `seekPosition` property to `@PartitionOffset` support for `TopicPartitionOffset.SeekPosition`.
See [manual-assignment](#kafka-receiving-messages-listener-annotation--manual-assignment) for more details.

<a id="appendix-change-history--x32-topic-partition-offset-constructor"></a>
<a id="appendix-change-history--new-constructor-in-topicpartitionoffset-that-accepts-a-function-to-compute-the-offset-to-seek-to"></a>

### New constructor in TopicPartitionOffset that accepts a function to compute the offset to seek to

`TopicPartitionOffset` has a new constructor that takes a user-provided function to compute the offset to seek to.
When this constructor is used, the framework calls the function with the input argument of the current consumer offset position.
See [Seek API Docs](#kafka-seek--seek) for more details.

<a id="appendix-change-history--x32-default-clientid-prefix"></a>
<a id="appendix-change-history--spring-boot-application-name-as-default-client-id-prefix"></a>

### Spring Boot application name as default client ID prefix

For Spring Boot applications which define an application name, this name is now used
as a default prefix for auto-generated client IDs for certain client types.
See [Default client ID prefixes](#kafka-connecting--default-client-id-prefixes) for more details.

<a id="appendix-change-history--get-listener-containers-matching"></a>
<a id="appendix-change-history--enhanced-retrieval-of-messagelistenercontainers"></a>

## Enhanced Retrieval of MessageListenerContainers

`ListenerContainerRegistry` provides two new API’s dynamically find and filter `MessageListenerContainer` instances.
`getListenerContainersMatching(Predicate<String> idMatcher)` to filter by ID and the other is
`getListenerContainersMatching(BiPredicate<String, MessageListenerContainer> matcher)` to filter by ID and container properties.

See [`@KafkaListener` Lifecycle Management’s API Docs](#kafka-receiving-messages-kafkalistener-lifecycle--retrieving-message-listener-containers) for more information.

<a id="appendix-change-history--x32-observation"></a>
<a id="appendix-change-history--enhanced-observation-by-providing-more-tracing-tags"></a>

## Enhanced observation by providing more tracing tags

`KafkaTemplateObservation` provides more tracing tags(low cardinality).
`KafkaListenerObservation` provides a new API to find high cardinality key names and more tracing tags(high or low cardinality).
See [Micrometer Observation](#kafka-micrometer--observation)

<a id="appendix-change-history--what-s-new-in-3-1-since-3-0"></a>
<a id="appendix-change-history--what-s-new-in-3.1-since-3.0"></a>

## What’s New in 3.1 Since 3.0

This section covers the changes made from version 3.0 to version 3.1.
For changes in earlier version, see [Change History](#appendix-change-history).

<a id="appendix-change-history--x31-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-2"></a>

### Kafka Client Version

This version requires the 3.6.0 `kafka-clients`.

<a id="appendix-change-history--x31-ekb"></a>
<a id="appendix-change-history--embeddedkafkabroker"></a>

### EmbeddedKafkaBroker

An additional implementation is now provided to use `Kraft` instead of Zookeeper.
See [Embedded Kafka Broker](#testing--ekb) for more information.

<a id="appendix-change-history--x31-jd"></a>
<a id="appendix-change-history--jsondeserializer"></a>

### JsonDeserializer

When a deserialization exception occurs, the `SerializationException` message no longer contains the data with the form `Can’t deserialize data [[123, 34, 98, 97, 122, …`; an array of numerical values for each data byte is not useful and can be verbose for large data.
When used with an `ErrorHandlingDeserializer`, the `DeserializationException` sent to the error handler contains the `data` property which contains the raw data that could not be deserialized.
When not used with an `ErrorHandlingDeserializer`, the `KafkaConsumer` will continually emit exceptions for the same record showing the topic/partition/offset and the cause thrown by Jackson.

<a id="appendix-change-history--x31-cpp"></a>
<a id="appendix-change-history--containerpostprocessor"></a>

### ContainerPostProcessor

Post-processing can be applied on a listener container by specifying the bean name of a `ContainerPostProcessor` on the `@KafkaListener` annotation.
This occurs after the container has been created and after any configured `ContainerCustomizer` configured on the container factory.
See [Container Factory](#kafka-container-factory) for more information.

<a id="appendix-change-history--x31-ehd"></a>
<a id="appendix-change-history--errorhandlingdeserializer"></a>

### ErrorHandlingDeserializer

You can now add a `Validator` to this deserializer; if the delegate `Deserializer` successfully deserializes the object, but that object fails validation, an exception is thrown similar to a deserialization exception occurring.
This allows the original raw data to be passed to the error handler.
See [Using `ErrorHandlingDeserializer`](#kafka-serdes--error-handling-deserializer) for more information.

<a id="appendix-change-history--x31-retryable"></a>
<a id="appendix-change-history--retryable-topics"></a>

### Retryable Topics

Change suffix `-retry-5000` to `-retry` when `@RetryableTopic(backOff = @BackOff(delay = 5000), attempts = "2", fixedDelayTopicStrategy = FixedDelayStrategy.SINGLE_TOPIC)`.
If you want to keep suffix `-retry-5000`, use `@RetryableTopic(backOff = @BackOff(delay = 5000), attempts = "2")`.
See [Topic Naming](#retrytopic-topic-naming) for more information.

<a id="appendix-change-history--x31-c"></a>
<a id="appendix-change-history--listener-container-changes"></a>

### Listener Container Changes

When manually assigning partitions, with a `null` consumer `group.id`, the `AckMode` is now automatically coerced to `MANUAL`.
See [Manually Assigning All Partitions](#tips--tip-assign-all-parts) for more information.

<a id="appendix-change-history--what-s-new-in-3-0-since-2-9"></a>
<a id="appendix-change-history--what-s-new-in-3.0-since-2.9"></a>

## What’s New in 3.0 Since 2.9

<a id="appendix-change-history--x30-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-3"></a>

### Kafka Client Version

This version requires the 3.3.1 `kafka-clients`.

<a id="appendix-change-history--x30-eos"></a>
<a id="appendix-change-history--exactly-once-semantics"></a>

### Exactly Once Semantics

`EOSMode.V1` (aka `ALPHA`) is no longer supported.

> [!IMPORTANT]
> When using transactions, the minimum broker version is 2.5.

See [Exactly Once Semantics](#kafka-exactly-once) and [KIP-447](https://cwiki.apache.org/confluence/display/KAFKA/KIP-447%3A+Producer+scalability+for+exactly+once+semantics) for more information.

<a id="appendix-change-history--x30-obs"></a>
<a id="appendix-change-history--observation"></a>

### Observation

Enabling observation for timers and tracing using Micrometer is now supported.
See [Observation](#appendix-change-history--x30-obs) for more information.

<a id="appendix-change-history--x30-native"></a>
<a id="appendix-change-history--native-images"></a>

### Native Images

Support for creating native images is provided.
See [Native Images](#appendix-change-history--x30-native) for more information.

<a id="appendix-change-history--x30-global-embedded-kafka"></a>
<a id="appendix-change-history--global-single-embedded-kafka"></a>

### Global Single Embedded Kafka

The embedded Kafka (`EmbeddedKafkaBroker`) can now be start as a single global instance for the whole test plan.
See [Using the Same Broker(s) for Multiple Test Classes](#testing--same-broker-multiple-tests) for more information.

<a id="appendix-change-history--x30-retryable"></a>
<a id="appendix-change-history--retryable-topics-changes"></a>

### Retryable Topics Changes

This feature is no longer considered experimental (as far as its API is concerned), the feature itself has been supported since 2.7, but with a greater than normal possibility of breaking API changes.

The bootstrapping of [Non-Blocking Retries](#retrytopic) infrastructure beans has changed in this release to avoid some timing problems that occurred in some application regarding application initialization.

You can now set a different `concurrency` for the retry containers; by default, the concurrency is the same as the main container.

`@RetryableTopic` can now be used as a meta-annotation on custom annotations, including support for `@AliasFor` properties.

See [Configuration](#retrytopic-retry-config) for more information.

The default replication factor for the retry topics is now `-1` (use broker default).
If your broker is earlier that version 2.4, you will now need to explicitly set the property.

You can now configure multiple `@RetryableTopic` listeners on the same topic in the same application context.
Previously, this was not possible.
See [Multiple Listeners, Same Topic(s)](#retrytopic-multi-retry) for more information.

There are breaking API changes in `RetryTopicConfigurationSupport`; specifically, if you override the bean definition methods for `destinationTopicResolver`, `kafkaConsumerBackoffManager` and/or `retryTopicConfigurer`;
these methods now require an `ObjectProvider<RetryTopicComponentFactory>` parameter.

<a id="appendix-change-history--x30-lc-changes"></a>
<a id="appendix-change-history--listener-container-changes-2"></a>

### Listener Container Changes

Events related to consumer authentication and authorization failures are now published by the container.
See [Application Events](#kafka-events) for more information.

You can now customize the thread names used by consumer threads.
See [Container Thread Naming](#kafka-receiving-messages-container-thread-naming) for more information.

The container property `restartAfterAuthException` has been added.
See [Listener Container Properties](#kafka-container-props) for more information.

<a id="appendix-change-history--x30-template-changes"></a>
<a id="appendix-change-history--kafkatemplate-changes"></a>

### `KafkaTemplate` Changes

The futures returned by this class are now `CompletableFuture`s instead of `ListenableFuture`s.
See [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template).

<a id="appendix-change-history--x30-rkt-changes"></a>
<a id="appendix-change-history--replyingkafkatemplate-changes"></a>

### `ReplyingKafkaTemplate` Changes

The futures returned by this class are now `CompletableFuture`s instead of `ListenableFuture`s.
See [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template) and [Request/Reply with `Message<?>`s](#kafka-sending-messages--exchanging-messages).

<a id="appendix-change-history--x30-listener"></a>
<a id="appendix-change-history--kafkalistener-changes"></a>

### `@KafkaListener` Changes

You can now use a custom correlation header which will be echoed in any reply message.
See the note at the end of [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template) for more information.

You can now manually commit parts of a batch before the entire batch is processed.
See [Committing Offsets](#kafka-receiving-messages-message-listener-container--committing-offsets) for more information.

<a id="appendix-change-history--x30-headers"></a>
<a id="appendix-change-history--kafkaheaders-changes"></a>

### `KafkaHeaders` Changes

Four constants in `KafkaHeaders` that were deprecated in 2.9.x have now been removed.

- Instead of `MESSAGE_KEY`, use `KEY`.
- Instead of `PARTITION_ID`, use `PARTITION`

Similarly, `RECEIVED_MESSAGE_KEY` is replaced by `RECEIVED_KEY` and `RECEIVED_PARTITION_ID` is replaced by `RECEIVED_PARTITION`.

<a id="appendix-change-history--x30-testing"></a>
<a id="appendix-change-history--testing-changes"></a>

### Testing Changes

Version 3.0.7 introduced a `MockConsumerFactory` and `MockProducerFactory`.
See [Mock Consumer and Producer](#testing--mock-cons-prod) for more information.

Starting with version 3.0.10, the embedded Kafka broker, by default, sets the Spring Boot property `spring.kafka.bootstrap-servers` to the address(es) of the embedded broker(s).

<a id="appendix-change-history--what-s-new-in-2-9-since-2-8"></a>
<a id="appendix-change-history--what-s-new-in-2.9-since-2.8"></a>

## What’s New in 2.9 since 2.8

<a id="appendix-change-history--x29-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-4"></a>

### Kafka Client Version

This version requires the 3.2.0 `kafka-clients`.

<a id="appendix-change-history--x29-eh-changes"></a>
<a id="appendix-change-history--error-handler-changes"></a>

### Error Handler Changes

The `DefaultErrorHandler` can now be configured to pause the container for one poll and use the remaining results from the previous poll, instead of seeking to the offsets of the remaining records.
See [DefaultErrorHandler](#kafka-annotation-error-handling--default-eh) for more information.

The `DefaultErrorHandler` now has a `BackOffHandler` property.
See [Back Off Handlers](#kafka-annotation-error-handling--backoff-handlers) for more information.

<a id="appendix-change-history--x29-lc-changes"></a>
<a id="appendix-change-history--listener-container-changes-3"></a>

### Listener Container Changes

`interceptBeforeTx` now works with all transaction managers (previously it was only applied when a `KafkaAwareTransactionManager` was used).
See [[interceptBeforeTx]](#appendix-change-history--interceptbeforetx).

A new container property `pauseImmediate` is provided which allows the container to pause the consumer after the current record is processed, instead of after all the records from the previous poll have been processed.
See [[pauseImmediate]](#appendix-change-history--pauseimmediate).

Events related to consumer authentication and authorization

<a id="appendix-change-history--x29-hm-changes"></a>
<a id="appendix-change-history--header-mapper-changes"></a>

### Header Mapper Changes

You can now configure which inbound headers should be mapped.
Also available in version 2.8.8 or later.
See [Message Headers](#kafka-headers) for more information.

<a id="appendix-change-history--x29-template-changes"></a>
<a id="appendix-change-history--kafkatemplate-changes-2"></a>

### `KafkaTemplate` Changes

In 3.0, the futures returned by this class will be `CompletableFuture`s instead of `ListenableFuture`s.
See [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template) for assistance in transitioning when using this release.

<a id="appendix-change-history--x29-rkt-changes"></a>
<a id="appendix-change-history--replyingkafkatemplate-changes-2"></a>

### `ReplyingKafkaTemplate` Changes

The template now provides a method to wait for assignment on the reply container, to avoid a race when sending a request before the reply container is initialized.
Also available in version 2.8.8 or later.
See [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template).

In 3.0, the futures returned by this class will be `CompletableFuture`s instead of `ListenableFuture`s.
See [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template) and [Request/Reply with `Message<?>`s](#kafka-sending-messages--exchanging-messages) for assistance in transitioning when using this release.

<a id="appendix-change-history--what-s-new-in-2-8-since-2-7"></a>
<a id="appendix-change-history--what-s-new-in-2.8-since-2.7"></a>

## What’s New in 2.8 Since 2.7

This section covers the changes made from version 2.7 to version 2.8.
For changes in earlier version, see [Change History](https://docs.spring.io/spring-kafka/reference/appendix.html#history).

<a id="appendix-change-history--x28-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-5"></a>

### Kafka Client Version

This version requires the 3.0.0 `kafka-clients`

<a id="appendix-change-history--x28-packages"></a>
<a id="appendix-change-history--package-changes"></a>

### Package Changes

Classes and interfaces related to type mapping have been moved from `…support.converter` to `…support.mapping`.

- `AbstractJavaTypeMapper`
- `ClassMapper`
- `DefaultJackson2JavaTypeMapper`
- `Jackson2JavaTypeMapper`

<a id="appendix-change-history--x28-ooo-commits"></a>
<a id="appendix-change-history--out-of-order-manual-commits"></a>

### Out of Order Manual Commits

The listener container can now be configured to accept manual offset commits out of order (usually asynchronously).
The container will defer the commit until the missing offset is acknowledged.
See [Manually Committing Offsets](#kafka-receiving-messages-ooo-commits) for more information.

<a id="appendix-change-history--x28-batch-overrude"></a>
<a id="appendix-change-history--kafkalistener-changes-2"></a>

### `@KafkaListener` Changes

It is now possible to specify whether the listener method is a batch listener on the method itself.
This allows the same container factory to be used for both record and batch listeners.

See [[batch-listeners]](#appendix-change-history--batch-listeners) for more information.

Batch listeners can now handle conversion exceptions.

See [Conversion Errors with Batch Error Handlers](#kafka-annotation-error-handling--batch-listener-conv-errors) for more information.

`RecordFilterStrategy`, when used with batch listeners, can now filter the entire batch in one call.
See the note at the end of [[batch-listeners]](#appendix-change-history--batch-listeners) for more information.

The `@KafkaListener` annotation now has the `filter` attribute, to override the container factory’s `RecordFilterStrategy` for just this listener.

The `@KafkaListener` annotation now has the `info` attribute; this is used to populate the new listener container property `listenerInfo`.
This is then used to populate a `KafkaHeaders.LISTENER_INFO` header in each record which can be used in `RecordInterceptor`, `RecordFilterStrategy`, or the listener itself.
See [Listener Info Header](#kafka-annotation-error-handling--li-header) and [AbstractMessageListenerContainer Properties](#kafka-container-props--amlc-props) for more information.

<a id="appendix-change-history--x28-template"></a>
<a id="appendix-change-history--kafkatemplate-changes-3"></a>

### `KafkaTemplate` Changes

You can now receive a single record, given the topic, partition and offset.
See [Using `KafkaTemplate` to Receive](#kafka-receiving-messages-template-receive) for more information.

<a id="appendix-change-history--x28-eh"></a>
<a id="appendix-change-history--commonerrorhandler-added"></a>

### `CommonErrorHandler` Added

The legacy `GenericErrorHandler` and its sub-interface hierarchies for record an batch listeners have been replaced by a new single interface `CommonErrorHandler` with implementations corresponding to most legacy implementations of `GenericErrorHandler`.
See [Container Error Handlers](#kafka-annotation-error-handling--error-handlers) and [Migrating Custom Legacy Error Handler Implementations to `CommonErrorHandler`](#kafka-annotation-error-handling--migrating-legacy-eh) for more information.

<a id="appendix-change-history--x28-lcc"></a>
<a id="appendix-change-history--listener-container-changes-4"></a>

### Listener Container Changes

The `interceptBeforeTx` container property is now `true` by default.

The `authorizationExceptionRetryInterval` property has been renamed to `authExceptionRetryInterval` and now applies to `AuthenticationException`s in addition to `AuthorizationException`s previously.
Both exceptions are considered fatal and the container will stop by default, unless this property is set.

See [Using `KafkaMessageListenerContainer`](#kafka-receiving-messages-message-listener-container--kafka-container) and [Listener Container Properties](#kafka-container-props) for more information.

<a id="appendix-change-history--x28-serializers"></a>
<a id="appendix-change-history--serializer-deserializer-changes"></a>

### Serializer/Deserializer Changes

The `DelegatingByTopicSerializer` and `DelegatingByTopicDeserializer` are now provided.
See [Delegating Serializer and Deserializer](#kafka-serdes--delegating-serialization) for more information.

<a id="appendix-change-history--x28-dlpr"></a>
<a id="appendix-change-history--deadletterpublishingrecover-changes"></a>

### `DeadLetterPublishingRecover` Changes

The property `stripPreviousExceptionHeaders` is now `true` by default.

There are now several techniques to customize which headers are added to the output record.

See [Managing Dead Letter Record Headers](#kafka-annotation-error-handling--dlpr-headers) for more information.

<a id="appendix-change-history--x28-retryable-topics-changes"></a>
<a id="appendix-change-history--retryable-topics-changes-2"></a>

### Retryable Topics Changes

Now you can use the same factory for retryable and non-retryable topics.
See [Specifying a ListenerContainerFactory](#retrytopic-retry-topic-lcf) for more information.

There’s now a manageable global list of fatal exceptions that will make the failed record go straight to the DLT.
Refer to [Exception Classifier](#retrytopic-features--retry-topic-ex-classifier) to see how to manage it.

You can now use blocking and non-blocking retries in conjunction.
See [Combining Blocking and Non-Blocking Retries](#retrytopic-retry-topic-combine-blocking) for more information.

The KafkaBackOffException thrown when using the retryable topics feature is now logged at DEBUG level.
See [Changing KafkaBackOffException Logging Level](#retrytopic-change-kboe-logging-level) if you need to change the logging level back to WARN or set it to any other level.

<a id="appendix-change-history--changes-between-2-6-and-2-7"></a>
<a id="appendix-change-history--changes-between-2.6-and-2.7"></a>

## Changes between 2.6 and 2.7

<a id="appendix-change-history--x27-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-6"></a>

### Kafka Client Version

This version requires the 2.7.0 `kafka-clients`.
It is also compatible with the 2.8.0 clients, since version 2.7.1; see [Override Spring Boot Dependencies](https://docs.spring.io/spring-kafka/reference/appendix.html).

<a id="appendix-change-history--x-27-nonblock-retry"></a>
<a id="appendix-change-history--non-blocking-delayed-retries-using-topics"></a>

### Non-Blocking Delayed Retries Using Topics

This significant new feature is added in this release.
When strict ordering is not important, failed deliveries can be sent to another topic to be consumed later.
A series of such retry topics can be configured, with increasing delays.
See [Non-Blocking Retries](#retrytopic) for more information.

<a id="appendix-change-history--x27-container"></a>
<a id="appendix-change-history--listener-container-changes-5"></a>

### Listener Container Changes

The `onlyLogRecordMetadata` container property is now `true` by default.

A new container property `stopImmediate` is now available.

See [Listener Container Properties](#kafka-container-props) for more information.

Error handlers that use a `BackOff` between delivery attempts (e.g. `SeekToCurrentErrorHandler` and `DefaultAfterRollbackProcessor`) will now exit the back off interval soon after the container is stopped, rather than delaying the stop.

Error handlers and after rollback processors that extend `FailedRecordProcessor` can now be configured with one or more `RetryListener`s to receive information about retry and recovery progress.

The `RecordInterceptor` now has additional methods called after the listener returns (normally, or by throwing an exception).
It also has a sub-interface `ConsumerAwareRecordInterceptor`.
In addition, there is now a `BatchInterceptor` for batch listeners.
See [Message Listener Containers](#kafka-receiving-messages-message-listener-container) for more information.

<a id="appendix-change-history--x27-listener"></a>
<a id="appendix-change-history--kafkalistener-changes-3"></a>

### `@KafkaListener` Changes

You can now validate the payload parameter of `@KafkaHandler` methods (class-level listeners).
See [`@KafkaListener` `@Payload` Validation](#kafka-receiving-messages-validation) for more information.

You can now set the `rawRecordHeader` property on the `MessagingMessageConverter` and `BatchMessagingMessageConverter` which causes the raw `ConsumerRecord` to be added to the converted `Message<?>`.
This is useful, for example, if you wish to use a `DeadLetterPublishingRecoverer` in a listener error handler.
See [Listener Error Handlers](#kafka-annotation-error-handling--listener-error-handlers) for more information.

You can now modify `@KafkaListener` annotations during application initialization.
See [`@KafkaListener` Attribute Modification](#kafka-receiving-messages-kafkalistener-attrs) for more information.

<a id="appendix-change-history--x27-dlt"></a>
<a id="appendix-change-history--deadletterpublishingrecover-changes-2"></a>

### `DeadLetterPublishingRecover` Changes

Now, if both the key and value fail deserialization, the original values are published to the DLT.
Previously, the value was populated but the key `DeserializationException` remained in the headers.
There is a breaking API change, if you subclassed the recoverer and overrode the `createProducerRecord` method.

In addition, the recoverer verifies that the partition selected by the destination resolver actually exists before publishing to it.

See [Publishing Dead-letter Records](#kafka-annotation-error-handling--dead-letters) for more information.

<a id="appendix-change-history--x27-cktm"></a>
<a id="appendix-change-history--chainedkafkatransactionmanager-is-deprecated"></a>

### `ChainedKafkaTransactionManager` is Deprecated

See [Transactions](#kafka-transactions) for more information.

<a id="appendix-change-history--x27-rkt"></a>
<a id="appendix-change-history--replyingkafkatemplate-changes-3"></a>

### `ReplyingKafkaTemplate` Changes

There is now a mechanism to examine a reply and fail the future exceptionally if some condition exists.

Support for sending and receiving `spring-messaging` `Message<?>`s has been added.

See [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template) for more information.

<a id="appendix-change-history--x27-streams"></a>
<a id="appendix-change-history--kafka-streams-changes"></a>

### Kafka Streams Changes

By default, the `StreamsBuilderFactoryBean` is now configured to not clean up local state.
See [Configuration](#streams--streams-config) for more information.

<a id="appendix-change-history--x27-admin"></a>
<a id="appendix-change-history--kafkaadmin-changes"></a>

### `KafkaAdmin` Changes

New methods `createOrModifyTopics` and `describeTopics` have been added.
`KafkaAdmin.NewTopics` has been added to facilitate configuring multiple topics in a single bean.
See [[configuring-topics]](#appendix-change-history--configuring-topics) for more information.

<a id="appendix-change-history--x27-conv"></a>
<a id="appendix-change-history--messageconverter-changes"></a>

### `MessageConverter` Changes

It is now possible to add a `spring-messaging` `SmartMessageConverter` to the `MessagingMessageConverter`, allowing content negotiation based on the `contentType` header.
See [Spring Messaging Message Conversion](#kafka-serdes--messaging-message-conversion) for more information.

<a id="appendix-change-history--x27-sequencing"></a>
<a id="appendix-change-history--sequencing-kafkalistener-s"></a>

### Sequencing `@KafkaListener`s

See [Starting `@KafkaListener`s in Sequence](#kafka-receiving-messages-sequencing) for more information.

<a id="appendix-change-history--x27-exp-backoff"></a>
<a id="appendix-change-history--exponentialbackoffwithmaxretries"></a>

### `ExponentialBackOffWithMaxRetries`

A new `BackOff` implementation is provided, making it more convenient to configure the max retries.
See [`ExponentialBackOffWithMaxRetries` Implementation](#kafka-annotation-error-handling--exp-backoff) for more information.

<a id="appendix-change-history--x27-delegating-eh"></a>
<a id="appendix-change-history--conditional-delegating-error-handlers"></a>

### Conditional Delegating Error Handlers

These new error handlers can be configured to delegate to different error handlers, depending on the exception type.
See [Delegating Error Handler](#kafka-annotation-error-handling--cond-eh) for more information.

<a id="appendix-change-history--changes-between-2-5-and-2-6"></a>
<a id="appendix-change-history--changes-between-2.5-and-2.6"></a>

## Changes between 2.5 and 2.6

<a id="appendix-change-history--x26-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-7"></a>

### Kafka Client Version

This version requires the 2.6.0 `kafka-clients`.

<a id="appendix-change-history--listener-container-changes-6"></a>

### Listener Container Changes

The default `EOSMode` is now `BETA`.
See [Exactly Once Semantics](#kafka-exactly-once) for more information.

Various error handlers (that extend `FailedRecordProcessor`) and the `DefaultAfterRollbackProcessor` now reset the `BackOff` if recovery fails.
In addition, you can now select the `BackOff` to use based on the failed record and/or exception.

You can now configure an `adviceChain` in the container properties.
See [Listener Container Properties](#kafka-container-props) for more information.

When the container is configured to publish `ListenerContainerIdleEvent`s, it now publishes a `ListenerContainerNoLongerIdleEvent` when a record is received after publishing an idle event.
See [Application Events](#kafka-events) and [Detecting Idle and Non-Responsive Consumers](#kafka-events--idle-containers) for more information.

<a id="appendix-change-history--kafkalistener-changes-4"></a>

### @KafkaListener Changes

When using manual partition assignment, you can now specify a wildcard for determining which partitions should be reset to the initial offset.
In addition, if the listener implements `ConsumerSeekAware`, `onPartitionsAssigned()` is called after the manual assignment.
(Also added in version 2.5.5).
See [Explicit Partition Assignment](#kafka-receiving-messages-listener-annotation--manual-assignment) for more information.

Convenience methods have been added to `AbstractConsumerSeekAware` to make seeking easier.
See [[seek]](#appendix-change-history--seek) for more information.

<a id="appendix-change-history--errorhandler-changes"></a>

### ErrorHandler Changes

Subclasses of `FailedRecordProcessor` (e.g. `SeekToCurrentErrorHandler`, `DefaultAfterRollbackProcessor`, `RecoveringBatchErrorHandler`) can now be configured to reset the retry state if the exception is a different type to that which occurred previously with this record.

<a id="appendix-change-history--producer-factory-changes"></a>

### Producer Factory Changes

You can now set a maximum age for producers after which they will be closed and recreated.
See [Transactions](#kafka-transactions) for more information.

You can now update the configuration map after the `DefaultKafkaProducerFactory` has been created.
This might be useful, for example, if you have to update SSL key/trust store locations after a credentials change.
See [Using `DefaultKafkaProducerFactory`](#kafka-sending-messages--producer-factory) for more information.

<a id="appendix-change-history--changes-between-2-4-and-2-5"></a>
<a id="appendix-change-history--changes-between-2.4-and-2.5"></a>

## Changes between 2.4 and 2.5

This section covers the changes made from version 2.4 to version 2.5.
For changes in earlier version, see [Change History](https://docs.spring.io/spring-kafka/reference/appendix.html#history).

<a id="appendix-change-history--x25-factory-listeners"></a>
<a id="appendix-change-history--consumer-producer-factory-changes"></a>

### Consumer/Producer Factory Changes

The default consumer and producer factories can now invoke a callback whenever a consumer or producer is created or closed.
Implementations for native Micrometer metrics are provided.
See [Factory Listeners](#kafka-connecting--factory-listeners) for more information.

You can now change bootstrap server properties at runtime, enabling failover to another Kafka cluster.
See [Connecting to Kafka](#kafka-connecting) for more information.

<a id="appendix-change-history--x25-streams-listeners"></a>
<a id="appendix-change-history--streamsbuilderfactorybean-changes"></a>

### `StreamsBuilderFactoryBean` Changes

The factory bean can now invoke a callback whenever a `KafkaStreams` created or destroyed.
An Implementation for native Micrometer metrics is provided.
See [KafkaStreams Micrometer Support](#streams--streams-micrometer) for more information.

<a id="appendix-change-history--x25-kafka-client"></a>
<a id="appendix-change-history--kafka-client-version-8"></a>

### Kafka Client Version

This version requires the 2.5.0 `kafka-clients`.

<a id="appendix-change-history--class-package-changes"></a>

### Class/Package Changes

`SeekUtils` has been moved from the `o.s.k.support` package to `o.s.k.listener`.

<a id="appendix-change-history--x25-delivery"></a>
<a id="appendix-change-history--delivery-attempts-header"></a>

### Delivery Attempts Header

There is now an option to to add a header which tracks delivery attempts when using certain error handlers and after rollback processors.
See [Delivery Attempts Header](#kafka-annotation-error-handling--delivery-header) for more information.

<a id="appendix-change-history--x25-message-return"></a>
<a id="appendix-change-history--kafkalistener-changes-5"></a>

### @KafkaListener Changes

Default reply headers will now be populated automatically if needed when a `@KafkaListener` return type is `Message<?>`.
See [Reply Type Message<?>](#kafka-sending-messages--reply-message) for more information.

The `KafkaHeaders.RECEIVED_MESSAGE_KEY` is no longer populated with a `null` value when the incoming record has a `null` key; the header is omitted altogether.

`@KafkaListener` methods can now specify a `ConsumerRecordMetadata` parameter instead of using discrete headers for metadata such as topic, partition, etc.
See [Consumer Record Metadata](#kafka-receiving-messages-listener-annotation--consumer-record-metadata) for more information.

<a id="appendix-change-history--x25-container"></a>
<a id="appendix-change-history--listener-container-changes-7"></a>

### Listener Container Changes

The `assignmentCommitOption` container property is now `LATEST_ONLY_NO_TX` by default.
See [Listener Container Properties](#kafka-container-props) for more information.

The `subBatchPerPartition` container property is now `true` by default when using transactions.
See [Transactions](#kafka-transactions) for more information.

A new `RecoveringBatchErrorHandler` is now provided.

Static group membership is now supported.
See [Message Listener Containers](#kafka-receiving-messages-message-listener-container) for more information.

When incremental/cooperative rebalancing is configured, if offsets fail to commit with a non-fatal `RebalanceInProgressException`, the container will attempt to re-commit the offsets for the partitions that remain assigned to this instance after the rebalance is completed.

The default error handler is now the `SeekToCurrentErrorHandler` for record listeners and `RecoveringBatchErrorHandler` for batch listeners.
See [Container Error Handlers](#kafka-annotation-error-handling--error-handlers) for more information.

You can now control the level at which exceptions intentionally thrown by standard error handlers are logged.
See [Container Error Handlers](#kafka-annotation-error-handling--error-handlers) for more information.

The `getAssignmentsByClientId()` method has been added, making it easier to determine which consumers in a concurrent container are assigned which partition(s).
See [Listener Container Properties](#kafka-container-props) for more information.

You can now suppress logging entire `ConsumerRecord`s in error, debug logs etc.
See `onlyLogRecordMetadata` in [Listener Container Properties](#kafka-container-props).

<a id="appendix-change-history--x25-template"></a>
<a id="appendix-change-history--kafkatemplate-changes-4"></a>

### KafkaTemplate Changes

The `KafkaTemplate` can now maintain micrometer timers.
See [Monitoring](#kafka-micrometer) for more information.

The `KafkaTemplate` can now be configured with `ProducerConfig` properties to override those in the producer factory.
See [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template) for more information.

A `RoutingKafkaTemplate` has now been provided.
See [Using `RoutingKafkaTemplate`](#kafka-sending-messages--routing-template) for more information.

You can now use `KafkaSendCallback` instead of `ListenerFutureCallback` to get a narrower exception, making it easier to extract the failed `ProducerRecord`.
See [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template) for more information.

<a id="appendix-change-history--x25-string-serializer"></a>
<a id="appendix-change-history--kafka-string-serializer-deserializer"></a>

### Kafka String Serializer/Deserializer

New `ToStringSerializer`/`StringDeserializer`s as well as an associated `SerDe` are now provided.
See [String serialization](#kafka-serdes--string-serde) for more information.

<a id="appendix-change-history--x25-json-deser"></a>
<a id="appendix-change-history--jsondeserializer-2"></a>

### JsonDeserializer

The `JsonDeserializer` now has more flexibility to determine the deserialization type.
See [Using Methods to Determine Types](#kafka-serdes--serdes-type-methods) for more information.

<a id="appendix-change-history--x25-delegate-serde"></a>
<a id="appendix-change-history--delegating-serializer-deserializer"></a>

### Delegating Serializer/Deserializer

The `DelegatingSerializer` can now handle "standard" types, when the outbound record has no header.
See [Delegating Serializer and Deserializer](#kafka-serdes--delegating-serialization) for more information.

<a id="appendix-change-history--x25-testing"></a>
<a id="appendix-change-history--testing-changes-2"></a>

### Testing Changes

The `KafkaTestUtils.consumerProps()` helper record now sets `ConsumerConfig.AUTO_OFFSET_RESET_CONFIG` to `earliest` by default.
See [JUnit](#testing--junit) for more information.

<a id="appendix-change-history--changes-between-2-3-and-2-4"></a>
<a id="appendix-change-history--changes-between-2.3-and-2.4"></a>

## Changes between 2.3 and 2.4

<a id="appendix-change-history--kafka-client-2.4"></a>
<a id="appendix-change-history--kafka-client-version-9"></a>

### Kafka Client Version

This version requires the 2.4.0 `kafka-clients` or higher and supports the new incremental rebalancing feature.

<a id="appendix-change-history--x24-carl"></a>
<a id="appendix-change-history--consumerawarerebalancelistener"></a>

### ConsumerAwareRebalanceListener

Like `ConsumerRebalanceListener`, this interface now has an additional method `onPartitionsLost`.
Refer to the Apache Kafka documentation for more information.

Unlike the `ConsumerRebalanceListener`, The default implementation does **not** call `onPartitionsRevoked`.
Instead, the listener container will call that method after it has called `onPartitionsLost`; you should not, therefore, do the same when implementing `ConsumerAwareRebalanceListener`.

See the IMPORTANT note at the end of [Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners) for more information.

<a id="appendix-change-history--x24-eh"></a>
<a id="appendix-change-history--genericerrorhandler"></a>

### GenericErrorHandler

The `isAckAfterHandle()` default implementation now returns true by default.

<a id="appendix-change-history--x24-template"></a>
<a id="appendix-change-history--kafkatemplate"></a>

### KafkaTemplate

The `KafkaTemplate` now supports non-transactional publishing alongside transactional.
See [`KafkaTemplate` Transactional and non-Transactional Publishing](#kafka-transactions--tx-template-mixed) for more information.

<a id="appendix-change-history--x24-agg"></a>
<a id="appendix-change-history--aggregatingreplyingkafkatemplate"></a>

### AggregatingReplyingKafkaTemplate

The `releaseStrategy` is now a `BiConsumer`.
It is now called after a timeout (as well as when records arrive); the second parameter is `true` in the case of a call after a timeout.

See [Aggregating Multiple Replies](#kafka-sending-messages--aggregating-request-reply) for more information.

<a id="appendix-change-history--listener-container"></a>

### Listener Container

The `ContainerProperties` provides an `authorizationExceptionRetryInterval` option to let the listener container to retry after any `AuthorizationException` is thrown by the `KafkaConsumer`.
See its JavaDocs and [Using `KafkaMessageListenerContainer`](#kafka-receiving-messages-message-listener-container--kafka-container) for more information.

<a id="appendix-change-history--kafkalistener"></a>

### @KafkaListener

The `@KafkaListener` annotation has a new property `splitIterables`; default true.
When a replying listener returns an `Iterable` this property controls whether the return result is sent as a single record or a record for each element is sent.
See [Forwarding Listener Results using `@SendTo`](#kafka-receiving-messages-annotation-send-to) for more information

Batch listeners can now be configured with a `BatchToRecordAdapter`; this allows, for example, the batch to be processed in a transaction while the listener gets one record at a time.
With the default implementation, a `ConsumerRecordRecoverer` can be used to handle errors within the batch, without stopping the processing of the entire batch - this might be useful when using transactions.
See [Transactions with Batch Listeners](#kafka-transactions--transactions-batch) for more information.

<a id="appendix-change-history--kafka-streams"></a>

### Kafka Streams

The `StreamsBuilderFactoryBean` accepts a new property `KafkaStreamsInfrastructureCustomizer`.
This allows configuration of the builder and/or topology before the stream is created.
See [Spring Management](#streams--streams-spring) for more information.

<a id="appendix-change-history--changes-between-2-2-and-2-3"></a>
<a id="appendix-change-history--changes-between-2.2-and-2.3"></a>

## Changes Between 2.2 and 2.3

This section covers the changes made from version 2.2 to version 2.3.

<a id="appendix-change-history--cb-2-2-and-2-3-tips-tricks-and-examples"></a>
<a id="appendix-change-history--tips-tricks-and-examples"></a>

### Tips, Tricks and Examples

A new chapter [Tips, Tricks and Examples](#index--tips-n-tricks) has been added.
Please submit GitHub issues and/or pull requests for additional entries in that chapter.

<a id="appendix-change-history--cb-2-2-and-2-3-kafka-client-2.2"></a>
<a id="appendix-change-history--kafka-client-version-10"></a>

### Kafka Client Version

This version requires the 2.3.0 `kafka-clients` or higher.

<a id="appendix-change-history--cb-2-2-and-2-3-class-package-changes"></a>
<a id="appendix-change-history--class-package-changes-2"></a>

### Class/Package Changes

`TopicPartitionInitialOffset` is deprecated in favor of `TopicPartitionOffset`.

<a id="appendix-change-history--cb-2-2-and-2-3-configuration-changes"></a>
<a id="appendix-change-history--configuration-changes"></a>

### Configuration Changes

Starting with version 2.3.4, the `missingTopicsFatal` container property is false by default.
When this is true, the application fails to start if the broker is down; many users were affected by this change; given that Kafka is a high-availability platform, we did not anticipate that starting an application with no active brokers would be a common use case.

<a id="appendix-change-history--cb-2-2-and-2-3-producer-and-consumer-factory-changes"></a>
<a id="appendix-change-history--producer-and-consumer-factory-changes"></a>

### Producer and Consumer Factory Changes

The `DefaultKafkaProducerFactory` can now be configured to create a producer per thread.
You can also provide `Supplier<Serializer>` instances in the constructor as an alternative to either configured classes (which require no-arg constructors), or constructing with `Serializer` instances, which are then shared between all Producers.
See [Using `DefaultKafkaProducerFactory`](#kafka-sending-messages--producer-factory) for more information.

The same option is available with `Supplier<Deserializer>` instances in `DefaultKafkaConsumerFactory`.
See [Using `KafkaMessageListenerContainer`](#kafka-receiving-messages-message-listener-container--kafka-container) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-listener-container-changes"></a>
<a id="appendix-change-history--listener-container-changes-8"></a>

### Listener Container Changes

Previously, error handlers received `ListenerExecutionFailedException` (with the actual listener exception as the `cause`) when the listener was invoked using a listener adapter (such as `@KafkaListener`s).
Exceptions thrown by native `GenericMessageListener`s were passed to the error handler unchanged.
Now a `ListenerExecutionFailedException` is always the argument (with the actual listener exception as the `cause`), which provides access to the container’s `group.id` property.

Because the listener container has it’s own mechanism for committing offsets, it prefers the Kafka `ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG` to be `false`.
It now sets it to false automatically unless specifically set in the consumer factory or the container’s consumer property overrides.

The `ackOnError` property is now `false` by default.

It is now possible to obtain the consumer’s `group.id` property in the listener method.
See [Obtaining the Consumer `group.id`](#kafka-receiving-messages-listener-group-id) for more information.

The container has a new property `recordInterceptor` allowing records to be inspected or modified before invoking the listener.
A `CompositeRecordInterceptor` is also provided in case you need to invoke multiple interceptors.
See [Message Listener Containers](#kafka-receiving-messages-message-listener-container) for more information.

The `ConsumerSeekAware` has new methods allowing you to perform seeks relative to the beginning, end, or current position and to seek to the first offset greater than or equal to a time stamp.
See [[seek]](#appendix-change-history--seek) for more information.

A convenience class `AbstractConsumerSeekAware` is now provided to simplify seeking.
See [[seek]](#appendix-change-history--seek) for more information.

The `ContainerProperties` provides an `idleBetweenPolls` option to let the main loop in the listener container to sleep between `KafkaConsumer.poll()` calls.
See its JavaDocs and [Using `KafkaMessageListenerContainer`](#kafka-receiving-messages-message-listener-container--kafka-container) for more information.

When using `AckMode.MANUAL` (or `MANUAL_IMMEDIATE`) you can now cause a redelivery by calling `nack` on the `Acknowledgment`.
See [Committing Offsets](#kafka-receiving-messages-message-listener-container--committing-offsets) for more information.

Listener performance can now be monitored using Micrometer `Timer`s.
See [Monitoring](#kafka-micrometer) for more information.

The containers now publish additional consumer lifecycle events relating to startup.
See [Application Events](#kafka-events) for more information.

Transactional batch listeners can now support zombie fencing.
See [Transactions](#kafka-transactions) for more information.

The listener container factory can now be configured with a `ContainerCustomizer` to further configure each container after it has been created and configured.
See [Container factory](#kafka-container-factory) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-errorhandler-changes"></a>
<a id="appendix-change-history--errorhandler-changes-2"></a>

### ErrorHandler Changes

The `SeekToCurrentErrorHandler` now treats certain exceptions as fatal and disables retry for those, invoking the recoverer on first failure.

The `SeekToCurrentErrorHandler` and `SeekToCurrentBatchErrorHandler` can now be configured to apply a `BackOff` (thread sleep) between delivery attempts.

Starting with version 2.3.2, recovered records' offsets will be committed when the error handler returns after recovering a failed record.

The `DeadLetterPublishingRecoverer`, when used in conjunction with an `ErrorHandlingDeserializer`, now sets the payload of the message sent to the dead-letter topic, to the original value that could not be deserialized.
Previously, it was `null` and user code needed to extract the `DeserializationException` from the message headers.
See [Publishing Dead-letter Records](#kafka-annotation-error-handling--dead-letters) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-topicbuilder"></a>
<a id="appendix-change-history--topicbuilder"></a>

### TopicBuilder

A new class `TopicBuilder` is provided for more convenient creation of `NewTopic` `@Bean`s for automatic topic provisioning.
See [[configuring-topics]](#appendix-change-history--configuring-topics) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-kafka-streams-changes"></a>
<a id="appendix-change-history--kafka-streams-changes-2"></a>

### Kafka Streams Changes

You can now perform additional configuration of the `StreamsBuilderFactoryBean` created by `@EnableKafkaStreams`.
See [Streams Configuration](#streams--streams-config) for more information.

A `RecoveringDeserializationExceptionHandler` is now provided which allows records with deserialization errors to be recovered.
It can be used in conjunction with a `DeadLetterPublishingRecoverer` to send these records to a dead-letter topic.
See [Recovery from Deserialization Exceptions](#streams--streams-deser-recovery) for more information.

The `HeaderEnricher` transformer has been provided, using SpEL to generate the header values.
See [Header Enricher](#streams--streams-header-enricher) for more information.

The `MessagingTransformer` has been provided.
This allows a Kafka streams topology to interact with a spring-messaging component, such as a Spring Integration flow.
See [`MessagingProcessor`](#streams--streams-messaging) and See [Calling a Spring Integration Flow from a `KStream`](https://docs.spring.io/spring-integration/reference/kafka.html#streams-integration) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-json-component-changes"></a>
<a id="appendix-change-history--json-component-changes"></a>

### JSON Component Changes

Now all the JSON-aware components are configured by default with a Jackson `ObjectMapper` produced by the `JacksonUtils.enhancedObjectMapper()`.
The `JsonDeserializer` now provides `TypeReference`-based constructors for better handling of target generic container types.
Also a `JacksonMimeTypeModule` has been introduced for serialization of `org.springframework.util.MimeType` to plain string.
See its JavaDocs and [Serialization, Deserialization, and Message Conversion](#kafka-serdes) for more information.

A `ByteArrayJsonMessageConverter` has been provided as well as a new super class for all Json converters, `JsonMessageConverter`.
Also, a `StringOrBytesSerializer` is now available; it can serialize `byte[]`, `Bytes` and `String` values in `ProducerRecord`s.
See [Spring Messaging Message Conversion](#kafka-serdes--messaging-message-conversion) for more information.

The `JsonSerializer`, `JsonDeserializer` and `JsonSerde` now have fluent APIs to make programmatic configuration simpler.
See the javadocs, [Serialization, Deserialization, and Message Conversion](#kafka-serdes), and [Streams JSON Serialization and Deserialization](#streams--serde) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-replyingkafkatemplate"></a>
<a id="appendix-change-history--replyingkafkatemplate"></a>

### ReplyingKafkaTemplate

When a reply times out, the future is completed exceptionally with a `KafkaReplyTimeoutException` instead of a `KafkaException`.

Also, an overloaded `sendAndReceive` method is now provided that allows specifying the reply timeout on a per message basis.

<a id="appendix-change-history--aggregatingreplyingkafkatemplate-2"></a>

### AggregatingReplyingKafkaTemplate

Extends the `ReplyingKafkaTemplate` by aggregating replies from multiple receivers.
See [Aggregating Multiple Replies](#kafka-sending-messages--aggregating-request-reply) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-transaction-changes"></a>
<a id="appendix-change-history--transaction-changes"></a>

### Transaction Changes

You can now override the producer factory’s `transactionIdPrefix` on the `KafkaTemplate` and `KafkaTransactionManager`.
See [`transactionIdPrefix`](#kafka-transactions--transaction-id-prefix) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-new-delegating-serializerdeserializer"></a>
<a id="appendix-change-history--new-delegating-serializer-deserializer"></a>

### New Delegating Serializer/Deserializer

The framework now provides a delegating `Serializer` and `Deserializer`, utilizing a header to enable producing and consuming records with multiple key/value types.
See [Delegating Serializer and Deserializer](#kafka-serdes--delegating-serialization) for more information.

<a id="appendix-change-history--cb-2-2-and-2-3-new-retrying-deserializer"></a>
<a id="appendix-change-history--new-retrying-deserializer"></a>

### New Retrying Deserializer

The framework now provides a delegating `RetryingDeserializer`, to retry serialization when transient errors such as network problems might occur.
See [Retrying Deserializer](#kafka-serdes--retrying-deserialization) for more information.

<a id="appendix-change-history--changes-between-2-1-and-2-2"></a>
<a id="appendix-change-history--changes-between-2.1-and-2.2"></a>

## Changes Between 2.1 and 2.2

<a id="appendix-change-history--cb-2-1-and-2-2-kafka-client-2.0"></a>
<a id="appendix-change-history--kafka-client-version-11"></a>

### Kafka Client Version

This version requires the 2.0.0 `kafka-clients` or higher.

<a id="appendix-change-history--cb-2-1-and-2-2-class-and-package-changes"></a>
<a id="appendix-change-history--class-and-package-changes"></a>

### Class and Package Changes

The `ContainerProperties` class has been moved from `org.springframework.kafka.listener.config` to `org.springframework.kafka.listener`.

The `AckMode` enum has been moved from `AbstractMessageListenerContainer` to `ContainerProperties`.

The `setBatchErrorHandler()` and `setErrorHandler()` methods have been moved from `ContainerProperties` to both `AbstractMessageListenerContainer` and `AbstractKafkaListenerContainerFactory`.

<a id="appendix-change-history--cb-2-1-and-2-2-after-rollback-processing"></a>
<a id="appendix-change-history--after-rollback-processing-2"></a>

### After Rollback Processing

A new `AfterRollbackProcessor` strategy is provided.
See [After-rollback Processor](#kafka-annotation-error-handling--after-rollback) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-concurrentkafkalistenercontainerfactory-changes"></a>
<a id="appendix-change-history--concurrentkafkalistenercontainerfactory-changes"></a>

### `ConcurrentKafkaListenerContainerFactory` Changes

You can now use the `ConcurrentKafkaListenerContainerFactory` to create and configure any `ConcurrentMessageListenerContainer`, not only those for `@KafkaListener` annotations.
See [Container factory](#kafka-container-factory) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-listener-container-changes"></a>
<a id="appendix-change-history--listener-container-changes-9"></a>

### Listener Container Changes

A new container property (`missingTopicsFatal`) has been added.
See [Using `KafkaMessageListenerContainer`](#kafka-receiving-messages-message-listener-container--kafka-container) for more information.

A `ConsumerStoppedEvent` is now emitted when a consumer stops.
See [Thread Safety](#kafka-thread-safety) for more information.

Batch listeners can optionally receive the complete `ConsumerRecords<?, ?>` object instead of a `List<ConsumerRecord<?, ?>`.
See [[batch-listeners]](#appendix-change-history--batch-listeners) for more information.

The `DefaultAfterRollbackProcessor` and `SeekToCurrentErrorHandler` can now recover (skip) records that keep failing, and, by default, does so after 10 failures.
They can be configured to publish failed records to a dead-letter topic.

Starting with version 2.2.4, the consumer’s group ID can be used while selecting the dead letter topic name.

The `ConsumerStoppingEvent` has been added.
See [Application Events](#kafka-events) for more information.

The `SeekToCurrentErrorHandler` can now be configured to commit the offset of a recovered record when the container is configured with `AckMode.MANUAL_IMMEDIATE` (since 2.2.4).

<a id="appendix-change-history--cb-2-1-and-2-2-kafkalistener-changes"></a>
<a id="appendix-change-history--kafkalistener-changes-6"></a>

### @KafkaListener Changes

You can now override the `concurrency` and `autoStartup` properties of the listener container factory by setting properties on the annotation.
You can now add configuration to determine which headers (if any) are copied to a reply message.
See [`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation) for more information.

You can now use `@KafkaListener` as a meta-annotation on your own annotations.
See [`@KafkaListener` as a Meta Annotation](#kafka-receiving-messages-listener-meta) for more information.

It is now easier to configure a `Validator` for `@Payload` validation.
See [`@KafkaListener` `@Payload` Validation](#kafka-receiving-messages-validation) for more information.

You can now specify kafka consumer properties directly on the annotation; these will override any properties with the same name defined in the consumer factory (since version 2.2.4).
See [Annotation Properties](#kafka-receiving-messages-listener-annotation--annotation-properties) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-header-mapping-changes"></a>
<a id="appendix-change-history--header-mapping-changes"></a>

### Header Mapping Changes

Headers of type `MimeType` and `MediaType` are now mapped as simple strings in the `RecordHeader` value.
Previously, they were mapped as JSON and only `MimeType` was decoded.
`MediaType` could not be decoded.
They are now simple strings for interoperability.

Also, the `JsonKafkaHeaderMapper` has a new `addToStringClasses` method, allowing the specification of types that should be mapped by using `toString()` instead of JSON.
See [Message Headers](#kafka-headers) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-embedded-kafka-changes"></a>
<a id="appendix-change-history--embedded-kafka-changes"></a>

### Embedded Kafka Changes

The `KafkaEmbedded` class and its `KafkaRule` interface have been deprecated in favor of the `EmbeddedKafkaBroker` and its JUnit 4 `EmbeddedKafkaRule` wrapper.
The `@EmbeddedKafka` annotation now populates an `EmbeddedKafkaBroker` bean instead of the deprecated `KafkaEmbedded`.
This change allows the use of `@EmbeddedKafka` in JUnit 5 tests.
The `@EmbeddedKafka` annotation now has the attribute `ports` to specify the port that populates the `EmbeddedKafkaBroker`.
See [Testing Applications](#testing) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-jsonserializer-deserializer-enhancements"></a>
<a id="appendix-change-history--jsonserializer-deserializer-enhancements"></a>

### JsonSerializer/Deserializer Enhancements

You can now provide type mapping information by using producer and consumer properties.

New constructors are available on the deserializer to allow overriding the type header information with the supplied target type.

The `JsonDeserializer` now removes any type information headers by default.

You can now configure the `JsonDeserializer` to ignore type information headers by using a Kafka property (since 2.2.3).

See [Serialization, Deserialization, and Message Conversion](#kafka-serdes) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-kafka-streams-changes"></a>
<a id="appendix-change-history--kafka-streams-changes-3"></a>

### Kafka Streams Changes

The streams configuration bean must now be a `KafkaStreamsConfiguration` object instead of a `StreamsConfig` object.

The `StreamsBuilderFactoryBean` has been moved from package `…core` to `…config`.

The `KafkaStreamBrancher` has been introduced for better end-user experience when conditional branches are built on top of `KStream` instance.

See [Apache Kafka Streams Support](#streams) and [Configuration](#streams--streams-config) for more information.

<a id="appendix-change-history--cb-2-1-and-2-2-transactional-id"></a>
<a id="appendix-change-history--transactional-id"></a>

### Transactional ID

When a transaction is started by the listener container, the `transactional.id` is now the `transactionIdPrefix` appended with `<group.id>.<topic>.<partition>`.
This change allows proper fencing of zombies, [as described here](https://www.confluent.io/blog/transactions-apache-kafka/).

<a id="appendix-change-history--changes-between-2-0-and-2-1"></a>
<a id="appendix-change-history--changes-between-2.0-and-2.1"></a>

## Changes Between 2.0 and 2.1

<a id="appendix-change-history--cb-2-0-and-2-1-kafka-client-1.0"></a>
<a id="appendix-change-history--kafka-client-version-12"></a>

### Kafka Client Version

This version requires the 1.0.0 `kafka-clients` or higher.

The 1.1.x client is supported natively in version 2.2.

<a id="appendix-change-history--cb-2-0-and-2-1-json-improvements"></a>
<a id="appendix-change-history--json-improvements"></a>

### JSON Improvements

The `StringJsonMessageConverter` and `JsonSerializer` now add type information in `Headers`, letting the converter and `JsonDeserializer` create specific types on reception, based on the message itself rather than a fixed configured type.
See [Serialization, Deserialization, and Message Conversion](#kafka-serdes) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-container-stopping-error-handlers"></a>
<a id="appendix-change-history--container-stopping-error-handlers"></a>

### Container Stopping Error Handlers

Container error handlers are now provided for both record and batch listeners that treat any exceptions thrown by the listener as fatal/
They stop the container.
See [Handling Exceptions](#kafka-annotation-error-handling) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-pausing-and-resuming-containers"></a>
<a id="appendix-change-history--pausing-and-resuming-containers"></a>

### Pausing and Resuming Containers

The listener containers now have `pause()` and `resume()` methods (since version 2.1.3).
See [Pausing and Resuming Listener Containers](#kafka-pause-resume) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-stateful-retry"></a>
<a id="appendix-change-history--stateful-retry"></a>

### Stateful Retry

Starting with version 2.1.3, you can configure stateful retry.
See [Stateful Retry](#appendix-change-history--cb-2-0-and-2-1-stateful-retry) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-client-id"></a>
<a id="appendix-change-history--client-id"></a>

### Client ID

Starting with version 2.1.1, you can now set the `client.id` prefix on `@KafkaListener`.
Previously, to customize the client ID, you needed a separate consumer factory (and container factory) per listener.
The prefix is suffixed with `-n` to provide unique client IDs when you use concurrency.

<a id="appendix-change-history--cb-2-0-and-2-1-logging-offset-commits"></a>
<a id="appendix-change-history--logging-offset-commits"></a>

### Logging Offset Commits

By default, logging of topic offset commits is performed with the `DEBUG` logging level.
Starting with version 2.1.2, a new property in `ContainerProperties` called `commitLogLevel` lets you specify the log level for these messages.
See [Using `KafkaMessageListenerContainer`](#kafka-receiving-messages-message-listener-container--kafka-container) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-default-kafkahandler"></a>
<a id="appendix-change-history--default-kafkahandler"></a>

### Default @KafkaHandler

Starting with version 2.1.3, you can designate one of the `@KafkaHandler` annotations on a class-level `@KafkaListener` as the default.
See [`@KafkaListener` on a Class](#kafka-receiving-messages-class-level-kafkalistener) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-replyingkafkatemplate"></a>
<a id="appendix-change-history--replyingkafkatemplate-2"></a>

### ReplyingKafkaTemplate

Starting with version 2.1.3, a subclass of `KafkaTemplate` is provided to support request/reply semantics.
See [Using `ReplyingKafkaTemplate`](#kafka-sending-messages--replying-template) for more information.

<a id="appendix-change-history--cb-2-0-and-2-1-chainedkafkatransactionmanager"></a>
<a id="appendix-change-history--chainedkafkatransactionmanager"></a>

### ChainedKafkaTransactionManager

Version 2.1.3 introduced the `ChainedKafkaTransactionManager`.
(It is now deprecated).

<a id="appendix-change-history--cb-2-0-and-2-1-migration-guide-from-2-0"></a>
<a id="appendix-change-history--migration-guide-from-2.0"></a>

### Migration Guide from 2.0

See the [2.0 to 2.1 Migration](https://github.com/spring-projects/spring-kafka/wiki/Spring-for-Apache-Kafka-2.0-to-2.1-Migration-Guide) guide.

<a id="appendix-change-history--changes-between-1-3-and-2-0"></a>
<a id="appendix-change-history--changes-between-1.3-and-2.0"></a>

## Changes Between 1.3 and 2.0

<a id="appendix-change-history--cb-1-3-and-2-0-spring-framework-and-java-versions"></a>
<a id="appendix-change-history--spring-framework-and-java-versions"></a>

### Spring Framework and Java Versions

The Spring for Apache Kafka project now requires Spring Framework 5.0 and Java 8.

<a id="appendix-change-history--cb-1-3-and-2-0-kafkalistener-changes"></a>
<a id="appendix-change-history--kafkalistener-changes-7"></a>

### `@KafkaListener` Changes

You can now annotate `@KafkaListener` methods (and classes and `@KafkaHandler` methods) with `@SendTo`.
If the method returns a result, it is forwarded to the specified topic.
See [Forwarding Listener Results using `@SendTo`](#kafka-receiving-messages-annotation-send-to) for more information.

<a id="appendix-change-history--cb-1-3-and-2-0-message-listeners"></a>
<a id="appendix-change-history--message-listeners"></a>

### Message Listeners

Message listeners can now be aware of the `Consumer` object.
See [[message-listeners]](#appendix-change-history--message-listeners) for more information.

<a id="appendix-change-history--cb-1-3-and-2-0-using-consumerawarerebalancelistener"></a>
<a id="appendix-change-history--using-consumerawarerebalancelistener"></a>

### Using `ConsumerAwareRebalanceListener`

Rebalance listeners can now access the `Consumer` object during rebalance notifications.
See [Rebalancing Listeners](#kafka-receiving-messages-rebalance-listeners) for more information.

<a id="appendix-change-history--changes-between-1-2-and-1-3"></a>
<a id="appendix-change-history--changes-between-1.2-and-1.3"></a>

## Changes Between 1.2 and 1.3

<a id="appendix-change-history--cb-1-2-and-1-3-support-for-transactions"></a>
<a id="appendix-change-history--support-for-transactions"></a>

### Support for Transactions

The 0.11.0.0 client library added support for transactions.
The `KafkaTransactionManager` and other support for transactions have been added.
See [Transactions](#kafka-transactions) for more information.

<a id="appendix-change-history--cb-1-2-and-1-3-support-for-headers"></a>
<a id="appendix-change-history--support-for-headers"></a>

### Support for Headers

The 0.11.0.0 client library added support for message headers.
These can now be mapped to and from `spring-messaging` `MessageHeaders`.
See [Message Headers](#kafka-headers) for more information.

<a id="appendix-change-history--cb-1-2-and-1-3-creating-topics"></a>
<a id="appendix-change-history--creating-topics"></a>

### Creating Topics

The 0.11.0.0 client library provides an `AdminClient`, which you can use to create topics.
The `KafkaAdmin` uses this client to automatically add topics defined as `@Bean` instances.

<a id="appendix-change-history--cb-1-2-and-1-3-support-for-kafka-timestamps"></a>
<a id="appendix-change-history--support-for-kafka-timestamps"></a>

### Support for Kafka Timestamps

`KafkaTemplate` now supports an API to add records with timestamps.
New `KafkaHeaders` have been introduced regarding `timestamp` support.
Also, new `KafkaConditions.timestamp()` and `KafkaMatchers.hasTimestamp()` testing utilities have been added.
See [Using `KafkaTemplate`](#kafka-sending-messages--kafka-template), [`@KafkaListener` Annotation](#kafka-receiving-messages-listener-annotation), and [Testing Applications](#testing) for more details.

<a id="appendix-change-history--cb-1-2-and-1-3-kafkalistener-changes"></a>
<a id="appendix-change-history--kafkalistener-changes-8"></a>

### `@KafkaListener` Changes

You can now configure a `KafkaListenerErrorHandler` to handle exceptions.
See [Handling Exceptions](#kafka-annotation-error-handling) for more information.

By default, the `@KafkaListener` `id` property is now used as the `group.id` property, overriding the property configured in the consumer factory (if present).
Further, you can explicitly configure the `groupId` on the annotation.
Previously, you would have needed a separate container factory (and consumer factory) to use different `group.id` values for listeners.
To restore the previous behavior of using the factory configured `group.id`, set the `idIsGroup` property on the annotation to `false`.

<a id="appendix-change-history--cb-1-2-and-1-3-embeddedkafka-annotation"></a>
<a id="appendix-change-history--embeddedkafka-annotation"></a>

### `@EmbeddedKafka` Annotation

For convenience, a test class-level `@EmbeddedKafka` annotation is provided, to register `KafkaEmbedded` as a bean.
See [Testing Applications](#testing) for more information.

<a id="appendix-change-history--cb-1-2-and-1-3-kerberos-configuration"></a>
<a id="appendix-change-history--kerberos-configuration"></a>

### Kerberos Configuration

Support for configuring Kerberos is now provided.
See [JAAS and Kerberos](#kafka-kerberos) for more information.

<a id="appendix-change-history--changes-between-1-1-and-1-2"></a>
<a id="appendix-change-history--changes-between-1.1-and-1.2"></a>

## Changes Between 1.1 and 1.2

This version uses the 0.10.2.x client.

<a id="appendix-change-history--cb-1-1-and-1-2-changes-between-1-0-and-1-1"></a>
<a id="appendix-change-history--changes-between-1.0-and-1.1"></a>

## Changes Between 1.0 and 1.1

<a id="appendix-change-history--cb-1-1-and-1-2-kafka-client"></a>
<a id="appendix-change-history--kafka-client"></a>

### Kafka Client

This version uses the Apache Kafka 0.10.x.x client.

<a id="appendix-change-history--cb-1-1-and-1-2-batch-listeners"></a>
<a id="appendix-change-history--batch-listeners"></a>

### Batch Listeners

Listeners can be configured to receive the entire batch of messages returned by the `consumer.poll()` operation, rather than one at a time.

<a id="appendix-change-history--cb-1-1-and-1-2-null-payloads"></a>
<a id="appendix-change-history--null-payloads"></a>

### Null Payloads

Null payloads are used to “delete” keys when you use log compaction.

<a id="appendix-change-history--cb-1-1-and-1-2-initial-offset"></a>
<a id="appendix-change-history--initial-offset"></a>

### Initial Offset

When explicitly assigning partitions, you can now configure the initial offset relative to the current position for the consumer group, rather than absolute or relative to the current end.

<a id="appendix-change-history--cb-1-1-and-1-2-seek"></a>
<a id="appendix-change-history--seek"></a>

### Seek

You can now seek the position of each topic or partition.
You can use this to set the initial position during initialization when group management is in use and Kafka assigns the partitions.
You can also seek when an idle container is detected or at any arbitrary point in your application’s execution.
See [[seek]](#appendix-change-history--seek) for more information.

[Native Images](#appendix-native-images)

---
