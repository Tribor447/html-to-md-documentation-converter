# Overview

## Navigation

- [Overview](#index)
  
- [Overview](#index)
  
- [What’s new?](#whats-new)
  
- [Introduction](#intro)
    
- [System Requirements](#intro-system-requirements)
    
- [Building the Project](#intro-building)
    
- [Getting Help](#intro-getting-help)
  
- [Reference](#reference-reference)
    
- [Using Spring for Apache Pulsar](#reference-pulsar)
      
- [Quick Tour](#reference-pulsar-quick-tour)
      
- [Pulsar Client](#reference-pulsar-pulsar-client)
      
- [Message Production](#reference-pulsar-message-production)
      
- [Message Consumption](#reference-pulsar-message-consumption)
      
- [Publishing and Consuming Partitioned Topics](#reference-pulsar-publishing-consuming-partitioned-topics)
      
- [Transactions](#reference-pulsar-transactions)
      
- [Null Payloads and Log Compaction of 'Tombstone' Records](#reference-tombstones)
    
- [Topic Resolution](#reference-topic-resolution)
    
- [Default Tenant / Namespace](#reference-default-tenant-namespace)
    
- [Custom Object Mapper](#reference-custom-object-mapper)
    
- [Pulsar Administration](#reference-pulsar-admin)
    
- [Pulsar Functions](#reference-pulsar-function)
    
- [Observability](#reference-observability)
  
- [Other Resources](#other-resources)
  - Appendices
    
- [Pulsar Clients and Spring Boot Compatibility](#appendix-version-compatibility)
    
- [Override Spring Boot Dependencies](#appendix-override-boot-dependencies)
    
- [Getting Dependencies without Spring Boot](#appendix-getting-dependencies-without-boot)
    
- [Non-GA Versions](#appendix-non-ga-versions)
    
- [GraalVM Native Image Support](#appendix-native-image)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/index.html -->

<!-- page_index: 1 -->

<a id="index--page-title"></a>
<a id="index--overview"></a>

# Overview

Soby Chacko; Chris Bono; Alexander Preuß; Jay Bryant; Christophe Bornet; Jonas Geiregat
(v2.0.7-SNAPSHOT)

> [!WARNING]
> You are viewing documentation for a SNAPSHOT version (2.0.7-SNAPSHOT). While it is usually in-sync with the underlying code, it is subject to change and not guaranteed to be up-to-date with the underlying code.

---

<a id="whats-new"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/whats-new.html -->

<!-- page_index: 2 -->

# What’s new?

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="whats-new--page-title"></a>
<a id="whats-new--what-s-new"></a>

# What’s new?

<a id="whats-new--what-s-new-in-2-0-since-1-2"></a>
<a id="whats-new--what-s-new-in-2.0-since-1.2"></a>

## What’s New in 2.0 Since 1.2

This section covers the changes made from version 1.2 to version 2.0.

<a id="whats-new--_spring_retry_replaced_with_core_retry"></a>
<a id="whats-new--spring-retry-replaced-with-core-retry"></a>

### Spring Retry replaced with Core Retry

All usages of Spring Retry have been replaced with a simpler retry mechanism recently introduced by Spring Framework.

This is mostly an internal implementation detail used when restarting message containers.
This will only affect you if you were providing a custom `RetryTemplate` via a `PulsarContainerFactoryCustomizer` bean.

The `RetryTemplate` class still exists in Core Retry but the package name has changed from `org.springframework.retry.support` to `org.springframework.core.retry` and the API has slightly changed.

See the [commit](https://github.com/spring-projects/spring-pulsar/commit/fc4742f419fb882c7a045a742cae259f8ab45cc5) for more details.

<a id="whats-new--_removals"></a>
<a id="whats-new--removals"></a>

### Removals

<a id="whats-new--_previously_deprecated_apis"></a>
<a id="whats-new--previously-deprecated-apis"></a>

#### Previously deprecated APIs

The following previously deprecated APIs, which were marked for removal in version 2.0.x, have now been removed:

- `org.springframework.pulsar.config.ConcurrentPulsarListenerContainerFactory#setConcurrency`
- `org.springframework.pulsar.config.ConcurrentPulsarListenerContainerFactoryCustomizer`
- `org.springframework.pulsar.config.ListenerContainerFactory#createListenerContainer`
- `org.springframework.pulsar.config.ReaderContainerFactory#createReaderContainer`
- `org.springframework.pulsar.config.ProducerBuilderConfigurationUtil`
- `org.springframework.pulsar.config.PulsarClientProxy#getPartitionsForTopic`
- `org.springframework.pulsar.config.PulsarTopic#builder`
- `org.springframework.pulsar.config.PulsarTopic#getFullyQualifiedTopicName`
- `org.springframework.pulsar.config.Resolved#get`
- `org.springframework.pulsar.test.support.model.UserPojo`
- `org.springframework.pulsar.test.support.model.UserRecord`

<a id="whats-new--_reactive_support"></a>
<a id="whats-new--reactive-support"></a>

#### Reactive Support

Reactive support has been removed from Spring Pulsar `2.0.0` - there is no longer a `spring-pulsar-reactive` module published.

<a id="whats-new--what-s-new-in-1-2-since-1-1"></a>
<a id="whats-new--what-s-new-in-1.2-since-1.1"></a>

## What’s New in 1.2 Since 1.1

This section covers the changes made from version 1.1 to version 1.2.

<a id="whats-new--_custom_object_mapper"></a>
<a id="whats-new--custom-object-mapper"></a>

### Custom Object Mapper

You can provide your own Jackson `ObjectMapper` that Pulsar will use when producing and consuming JSON messages.
See [Custom Object Mapper](#reference-custom-object-mapper) for more details.

<a id="whats-new--_default_tenant_and_namespace"></a>
<a id="whats-new--default-tenant-and-namespace"></a>

### Default Tenant and Namespace

You can specify a default tenant and/or namespace to use when producing or consuming messages against a non-fully-qualified topic URL.
See [Default Tenant / Namespace](#reference-default-tenant-namespace) for more details.

<a id="whats-new--_message_container_startup_policy"></a>
<a id="whats-new--message-container-startup-policy"></a>

### Message Container Startup Policy

You can now configure the message listener container startup failure policy to `stop`, `continue`, or `retry`.
For more details see the corresponding section for one of the supported containers [@PulsarListener](#reference-pulsar-message-consumption--message-listener-startup-failure) or [@PulsarReader](#reference-pulsar-message-consumption--message-reader-startup-failure).

<a id="whats-new--_message_container_factory_customizers_spring_boot"></a>
<a id="whats-new--message-container-factory-customizers-spring-boot"></a>

### Message Container Factory Customizers (Spring Boot)

Spring Boot has introduced a generic message container factory customizer `org.springframework.boot.pulsar.autoconfigure.PulsarContainerFactoryCustomizer<T extends PulsarContainerFactory<?, ?>>` that can be used to further configure one or more of the auto-configured container factories that back the following listener annotations:

- For `@PulsarListener` register one or more PulsarContainerFactoryCustomizer<ConcurrentPulsarListenerContainerFactory<?>> beans.
- For `@PulsarReader` register one or more PulsarContainerFactoryCustomizer<DefaultPulsarReaderContainerFactory<?>> beans.

<a id="whats-new--_deprecations"></a>
<a id="whats-new--deprecations"></a>

### Deprecations

<a id="whats-new--_pulsarclientgetpartitionsfortopicjava_lang_string"></a>
<a id="whats-new--pulsarclient-getpartitionsfortopic-java.lang.string"></a>

#### PulsarClient#getPartitionsForTopic(java.lang.String)

Version `3.3.1` of the Pulsar client deprecates the `getPartitionsForTopic(java.lang.String)` in favor of `getPartitionsForTopic(java.lang.String, boolean metadataAutoCreationEnabled)`.

<a id="whats-new--_pulsartopicbuilder"></a>
<a id="whats-new--pulsartopic-builder"></a>

#### PulsarTopic#builder

When using Spring Boot the `PulsarTopicBuilder` is now a registered bean that is configured with default values for domain, tenant, and namespace.
Therefore, if you are using Spring Boot, you can simply inject the builder where needed.
Otherwise, use one of the `PulsarTopicBuilder` constructors directly.

<a id="whats-new--_listenerreadercontainerfactory"></a>
<a id="whats-new--listener-readercontainerfactory"></a>

#### Listener/ReaderContainerFactory

The `PulsarContainerFactory` common interface was introduced to bridge the gap between listener and reader container factories.
As part of this, the following APIs were deprecated, copied, and renamed:

- `ListenerContainerFactory#createListenerContainer` replaced with `ListenerContainerFactory#createRegisteredContainer`
- `ReaderContainerFactory#createReaderContainer(E endpoint)` replaced with `ReaderContainerFactory#createRegisteredContainer`
- `ReaderContainerFactory#createReaderContainer(String… topics)` replaced with `ReaderContainerFactory#createContainer`

<a id="whats-new--_concurrentpulsarlistenercontainerfactorycustomizer"></a>
<a id="whats-new--concurrentpulsarlistenercontainerfactorycustomizer"></a>

#### ConcurrentPulsarListenerContainerFactoryCustomizer

The purpose of `ConcurrentPulsarListenerContainerFactoryCustomizer` was to customize the Spring Boot auto-configured message container factories.
However, Spring Boot has introduced a generic message container factory customizer `org.springframework.boot.pulsar.autoconfigure.PulsarContainerFactoryCustomizer<T extends PulsarContainerFactory<?, ?>>` that removes the need for this customizer.

Replace all instances of `ConcurrentPulsarListenerContainerFactoryCustomizer` with `org.springframework.boot.pulsar.autoconfigure.PulsarContainerFactoryCustomizer<ConcurrentPulsarListenerContainerFactoryCustomizer<?>>`.

<a id="whats-new--_removals_2"></a>
<a id="whats-new--removals-2"></a>

### Removals

The following previously deprecated listener endpoint adapters have been removed in favor of default methods in the listener endpoint interfaces:

- `org.springframework.pulsar.config.PulsarListenerEndpointAdapter`
- `org.springframework.pulsar.reactive.config.ReactivePulsarListenerEndpointAdapter`

<a id="whats-new--_breaking_changes"></a>
<a id="whats-new--breaking-changes"></a>

### Breaking Changes

<a id="whats-new--_pulsartopicinit"></a>
<a id="whats-new--pulsartopic-init"></a>

#### PulsarTopic#<init>

The `PulsarTopic` constructor now requires a fully qualified topic name (`domain://tenant/namespace/name`).
If you are invoking the constructor you will need to be sure the topic you pass in is fully-qualified.
A better alternative is to instead use the `PulsarTopicBuilder` as it does not require fully qualified names and will add default values for the missing components in the specified name.

<a id="whats-new--_pulsarreaderfactorycreatereader"></a>
<a id="whats-new--pulsarreaderfactory-createreader"></a>

#### PulsarReaderFactory#createReader

The `PulsarReaderFactory#createReader` API now throws an unchecked `PulsarException` rather than a checked `PulsarClientException`.
Replace any `try/catch` blocks on this API accordingly.

<a id="whats-new--what-s-new-in-1-1-since-1-0"></a>
<a id="whats-new--what-s-new-in-1.1-since-1.0"></a>

## What’s New in 1.1 Since 1.0

This section covers the changes made from version 1.0 to version 1.1.

<a id="whats-new--_auto_schema_support"></a>
<a id="whats-new--auto-schema-support"></a>

### Auto Schema support

If there is no chance to know the schema of a Pulsar topic in advance, you can use AUTO Schemas to produce/consume generic records to/from brokers.
See [Producing with AUTO\_SCHEMA](#reference-pulsar-message-production--template-auto-produce) and [Consuming with AUTO\_SCHEMA](#reference-pulsar-message-consumption--listener-auto-consume) for more details.

> [!NOTE]
> While the above links focus on `PulsarTemplate` and `@PulsarListener`, this feature is also supported in `ReactivePulsarTemplate`, `@ReactivePulsarListener`, and `@PulsarReader`.
> Details for each can be found in their respective section of this reference guide.

<a id="whats-new--_default_topicschema_via_message_annotation"></a>
<a id="whats-new--default-topic-schema-via-message-annotation"></a>

### Default topic/schema via message annotation

You can now mark a message class with `@PulsarMessage` to specify the [default topic](#reference-topic-resolution--default-topic-via-annotation) and/or [default schema](#reference-pulsar-message-consumption--listener-default-schema-annotation) to use when producing/consuming messages of that type.

<a id="whats-new--_remove_checked_exceptions"></a>
<a id="whats-new--remove-checked-exceptions"></a>

### Remove checked exceptions

The APIs provided by the framework no longer throw the checked `PulsarClientException`, but rather the unchecked `PulsarException`.

> [!WARNING]
> If you were previously catching or rethrowing `PulsarClientException` just to appease the compiler and were not actually handling the exception, you can simply remove your `catch` or `throws` clause.
> If you were actually handling the exception then you will need to replace `PulsarClientException` with `PulsarException` in your catch clause.

<a id="whats-new--_testing_support"></a>
<a id="whats-new--testing-support"></a>

### Testing support

The `spring-pulsar-test` module is now available to help test your Spring for Apache Pulsar applications.
See [Testing Applications](https://docs.spring.io/spring-pulsar/reference/reference/testing-applications.html#testing-applications) for more details.

---

<a id="intro"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/intro.html -->

<!-- page_index: 3 -->

<a id="intro--page-title"></a>
<a id="intro--introduction"></a>

# Introduction

This project provides a basic Spring-friendly API for developing [Apache Pulsar](https://pulsar.apache.org/) applications.

On a very high level, Spring for Apache Pulsar provides a `PulsarTemplate` for publishing to a Pulsar topic and a `PulsarListener` annotation for consuming from a Pulsar topic.
In addition, it also provides various convenience APIs for Spring developers to ramp up their development journey into Apache Pulsar.

---

<a id="intro-system-requirements"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/intro/system-requirements.html -->

<!-- page_index: 4 -->

<a id="intro-system-requirements--page-title"></a>
<a id="intro-system-requirements--system-requirements"></a>

# System Requirements

Spring for Apache Pulsar `2.0.7-SNAPSHOT` requires the following:

- [Java 17](https://www.java.com) and is compatible up to and including Java 20
- [Spring Framework `7.0.8`](https://spring.io/projects/spring-framework#learn) or above
- [Apache Pulsar Java Client `4.2.2`](https://pulsar.apache.org/docs/4.2.x/client-libraries-java/) or above

The version compatibility matrix (including Spring Boot) can be found in the [appendix](#appendix-version-compatibility--version-compatibility).

---

<a id="intro-building"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/intro/building.html -->

<!-- page_index: 5 -->

<a id="intro-building--page-title"></a>
<a id="intro-building--building-the-project"></a>

# Building the Project

If you have cloned the project locally, follow these steps to build the project from the source code.

> [!NOTE]
> Gradle `8.x (8.3 or above)` is required to build.

Run the following command to do a full build of the project:

```
./gradlew clean build
```

You can build without running tests by using the following command:

```
./gradlew clean build -x test
```

You can build the reference documentation using this command:

```
./gradlew :spring-pulsar-docs:antora
```

You can view the generated HTML in `docs/build/site` directory.

---

<a id="intro-getting-help"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/intro/getting-help.html -->

<!-- page_index: 6 -->

# Getting Help

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="intro-getting-help--page-title"></a>
<a id="intro-getting-help--getting-help"></a>

# Getting Help

If you have trouble with Spring for Apache Pulsar, we would like to help.

- Learn the Spring basics.
  Spring for Apache Pulsar builds on several other Spring projects.
  Check the [spring.io](https://spring.io) web-site for a wealth of reference documentation.
  If you are starting out with Spring, try one of the [guides](https://spring.io/guides).
- Ask a question.
  We monitor [stackoverflow.com](https://stackoverflow.com) for questions tagged with [`spring-pulsar`](https://stackoverflow.com/tags/spring-pulsar).
- Report bugs at [github.com/spring-projects/spring-pulsar/issues](https://github.com/spring-projects/spring-pulsar/issues).

> [!NOTE]
> All of Spring for Apache Pulsar is open source, including the documentation.
> If you find problems with the docs or if you want to improve them, please get involved.

---

<a id="reference-reference"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/reference.html -->

<!-- page_index: 7 -->

<a id="reference-reference--page-title"></a>
<a id="reference-reference--reference"></a>

# Reference

This part of the reference documentation details the various components that comprise Spring for Apache Pulsar.

---

<a id="reference-pulsar"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar.html -->

<!-- page_index: 8 -->

# Using Spring for Apache Pulsar

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar--page-title"></a>
<a id="reference-pulsar--using-spring-for-apache-pulsar"></a>

# Using Spring for Apache Pulsar

<a id="reference-pulsar--preface"></a>

## Preface

> [!NOTE]
> We recommend using a Spring-Boot-First approach for Spring for Apache Pulsar-based applications, as that simplifies things tremendously.
> To do so, you can add the `spring-boot-starter-pulsar` module as a dependency.

> [!NOTE]
> The majority of this reference expects the reader to be using the starter and gives most directions for configuration with that in mind.
> However, an effort is made to call out when instructions are specific to the Spring Boot starter usage.

<a id="reference-pulsar--section-summary"></a>

## Section Summary

- [Quick Tour](#reference-pulsar-quick-tour)
- [Pulsar Client](#reference-pulsar-pulsar-client)
- [Message Production](#reference-pulsar-message-production)
- [Message Consumption](#reference-pulsar-message-consumption)
- [Publishing and Consuming Partitioned Topics](#reference-pulsar-publishing-consuming-partitioned-topics)
- [Transactions](#reference-pulsar-transactions)
- [Null Payloads and Log Compaction of 'Tombstone' Records](#reference-tombstones)

---

<a id="reference-pulsar-quick-tour"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar/quick-tour.html -->

<!-- page_index: 9 -->

# Quick Tour

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-quick-tour--page-title"></a>
<a id="reference-pulsar-quick-tour--quick-tour"></a>

# Quick Tour

We will take a quick tour of Spring for Apache Pulsar by showing a sample Spring Boot application that produces and consumes.
This is a complete application and does not require any additional configuration, as long as you have a Pulsar cluster running on the default location - `localhost:6650`.

<a id="reference-pulsar-quick-tour--_dependencies"></a>
<a id="reference-pulsar-quick-tour--1.-dependencies"></a>

## 1. Dependencies

Spring Boot applications need only the `spring-boot-starter-pulsar` dependency. The following listings show how to define the dependency for Maven and Gradle, respectively:

- Maven
- Gradle

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-pulsar</artifactId>
        <version>4.0.6</version>
    </dependency>
</dependencies>
```

```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-pulsar:4.0.6'
}
```

<a id="reference-pulsar-quick-tour--_application_code"></a>
<a id="reference-pulsar-quick-tour--2.-application-code"></a>

## 2. Application Code

The following listing shows the Spring Boot application case for the example:

```java
@SpringBootApplication public class PulsarBootHelloWorld {
public static void main(String[] args) {SpringApplication.run(PulsarBootHelloWorld.class, args);}
@Bean ApplicationRunner runner(PulsarTemplate<String> pulsarTemplate) {return (args) -> pulsarTemplate.send("hello-pulsar-topic", "Hello Pulsar World!");}
@PulsarListener(subscriptionName = "hello-pulsar-sub", topics = "hello-pulsar-topic") void listen(String message) {System.out.println("Message Received: " + message);}}
```

Let us quickly go through the higher-level details of this application.
Later in the documentation we see these components in much more detail.

In the preceding sample, we heavily rely on Spring Boot auto-configuration.
Spring Boot auto-configures several components for our application.
It automatically provides a `PulsarClient`, which is used by both the producer and the consumer, for the application.

Spring Boot also auto-configures `PulsarTemplate`, which we inject in the application and start sending records to a Pulsar topic.
The application sends messages to a topic named `hello-pulsar`.
Note that the application does not specify any schema information, because Spring for Apache Pulsar library automatically infers the schema type from the type of the data that you send.

We use the `PulsarListener` annotation to consume from the `hello-pulsar` topic where we publish the data.
`PulsarListener` is a convenience annotation that wraps the message listener container infrastructure in Spring for Apache Pulsar.
Behind the scenes, it creates a message listener container to create and manage the Pulsar consumer.
As with a regular Pulsar consumer, the default subscription type when using `PulsarListener` is the `Exclusive` mode.
As records are published in to the `hello-pulsar` topic, the `Pulsarlistener` consumes them and prints them on the console.
The framework also infers the schema type used from the data type that the `PulsarListner` method uses as the payload — `String`, in this case.

---

<a id="reference-pulsar-pulsar-client"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar/pulsar-client.html -->

<!-- page_index: 10 -->

# Pulsar Client

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-pulsar-client--page-title"></a>
<a id="reference-pulsar-pulsar-client--pulsar-client"></a>

# Pulsar Client

When you use the Pulsar Spring Boot Starter, you get the `PulsarClient` auto-configured.

By default, the application tries to connect to a local Pulsar instance at `pulsar://localhost:6650`.
This can be adjusted by setting the `spring.pulsar.client.service-url` property to a different value.

> [!TIP]
> The value must be a valid [Pulsar Protocol](https://pulsar.apache.org/docs/4.2.x/client-libraries-java/#connection-urls) URL

You can further configure the client by specifying any of the [`spring.pulsar.client.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

> [!NOTE]
> If you are not using the starter, you will need to configure and register the `PulsarClient` yourself.
> There is a `DefaultPulsarClientFactory` that accepts a builder customizer that can be used to help with this.

<a id="reference-pulsar-pulsar-client--tls-encryption"></a>
<a id="reference-pulsar-pulsar-client--1.-tls-encryption-ssl"></a>

## 1. TLS Encryption (SSL)

By default, Pulsar clients communicate with Pulsar services in plain text.
The following section describes how to configure Pulsar clients to use TLS encryption (SSL).
A pre-requisite is that the Broker has also been configured to use TLS encryption.

The Spring Boot auto-configuration does not currently support any TLS/SSL configuration properties.
You can instead provide a `PulsarClientBuilderCustomizer` that sets the necessary properties on the Pulsar client builder.
Pulsar supports both Privacy Enhanced Mail (PEM) and Java KeyStore (JKS) certificate formats.

Follow these steps to configure TLS:

1. Adjust the Pulsar client service url to use the `pulsar+ssl://` scheme and TLS port (typically `6651`).
2. Adjust the admin client service url to use the `https://` scheme and TLS web port (typically `8443`).
3. Provide client builder customizer(s) that sets the relevant properties on the builder.

   - [PEM based sample](https://github.com/spring-projects/spring-pulsar/blob/02730275e8d0291525eed9db5babe880c555a7bd/integration-tests/src/intTest/java/org/springframework/pulsar/inttest/app/SamplePemBasedSslConfig.java#L30-L49)
   - [JKS based sample](https://github.com/spring-projects/spring-pulsar/blob/02730275e8d0291525eed9db5babe880c555a7bd/integration-tests/src/intTest/java/org/springframework/pulsar/inttest/app/SampleJksBasedSslConfig.java#L30-L57)

You can find more information on the above in the official [Pulsar TLS Encryption](https://pulsar.apache.org/docs/4.2.x/security-tls-transport/) documentation.

<a id="reference-pulsar-pulsar-client--client-authentication"></a>
<a id="reference-pulsar-pulsar-client--2.-authentication"></a>

## 2. Authentication

To connect to a Pulsar cluster that requires authentication, you need to specify which authentication plugin to use and any parameters required by the specified plugin.
When **using Spring Boot** auto-configuration, you can set the plugin and the plugin parameters via configuration properties (in most cases).

> [!NOTE]
> You need to ensure that names defined under `spring.pulsar.client.authentication.param.*` exactly match those expected by your auth plugin (which is typically camel cased).
> Spring Boot will not attempt any kind of relaxed binding for these entries.
>
> For example, if you want to configure the issuer url for the `AuthenticationOAuth2` auth plugin you must use `spring.pulsar.client.authentication.param.issuerUrl`.
> If you use other forms, such as `issuerurl` or `issuer-url`, the setting will not be applied to the plugin.

> [!TIP]
> Using environment variables for auth parameters is typically problematic because the case sensitivity is lost during translation.
> For example, consider the following `issuerUrl` auth parameter set via an environment variable:
>
> ```properties
> SPRING_PULSAR_CLIENT_AUTHENTICATION_PARAM_ISSUERURL=https://some.server.com
> ```
>
> When Spring Boot loads this property it will use `issuerurl` (lower-cased) rather than the expected `issuerUrl` (camel-cased).
> You can get around this limitation by using the value of the env var as the value of the related auth property in your application.yml.
> Continuing the example above:
>
> ```yaml
> spring:
>   pulsar:
>     client:
>       authentication:
>         param:
>           issuerUrl: ${SPRING_PULSAR_CLIENT_AUTHENTICATION_PARAM_ISSUERURL}
> ```

When **not using Spring Boot** auto-configuration, you can use the `org.apache.pulsar.client.api.AuthenticationFactory` to create the authentication and then set it directly on the Pulsar client builder in a client customizer that you provide to the client factory.

The following listings show how to configure each of the supported authentication mechanisms.

<details id="Athenz">
<summary><span>Click <mark>here</mark> for <strong>Athenz</strong></span></summary>
<div>
<div>
<div>
<pre>spring:
  pulsar:
    client:
      authentication:
        plugin-class-name: org.apache.pulsar.client.impl.auth.AuthenticationAthenz
        param:
          tenantDomain: ...
          tenantService: ...
          providerDomain: ...
          privateKey: ...
          keyId: ...</pre>
</div>
</div>
<div>
<table>
<tr>
<td>
<i title="Note"></i>
</td>
<td>
This also requires <a href="#reference-pulsar-pulsar-client--tls-encryption">TLS encryption</a>.
</td>
</tr>
</table>
</div>
</div>
</details>

<details id="Token">
<summary><span>Click <mark>here</mark> for <strong>Token</strong></span></summary>
<div>
<div>
<div>
<pre>spring:
  pulsar:
    client:
      authentication:
        plugin-class-name: org.apache.pulsar.client.impl.auth.AuthenticationToken
        param:
          token: some-token-goes-here</pre>
</div>
</div>
</div>
</details>

<details id="Basic">
<summary><span>Click <mark>here</mark> for <strong>Basic</strong></span></summary>
<div>
<div>
<div>
<pre>spring:
  pulsar:
    client:
      authentication:
        plugin-class-name: org.apache.pulsar.client.impl.auth.AuthenticationBasic
        param:
          userId: ...
          password: ...</pre>
</div>
</div>
</div>
</details>

<details id="OAuth2">
<summary><span>Click <mark>here</mark> for <strong>OAuth2</strong></span></summary>
<div>
<div>
<div>
<pre>spring:
  pulsar:
    client:
      authentication:
        plugin-class-name: org.apache.pulsar.client.impl.auth.oauth2.AuthenticationOAuth2
        param:
          issuerUrl: ...
          privateKey: ...
          audience: ...
          scope: ...</pre>
</div>
</div>
</div>
</details>

<details id="Sasl">
<summary><span>Click <mark>here</mark> for <strong>Sasl</strong></span></summary>
<div>
<div>
<div>
<pre>spring:
  pulsar:
    client:
      authentication:
        plugin-class-name: org.apache.pulsar.client.impl.auth.AuthenticationSasl
        param:
          saslJaasClientSectionName: ...
          serverType: ...</pre>
</div>
</div>
</div>
</details>

<details id="mTlS-pem">
<summary><span>Click <mark>here</mark> for <strong>mTLS (PEM)</strong></span></summary>
<div>
<div>
<table>
<tr>
<td>
<i title="Note"></i>
</td>
<td>
Because this option requires TLS encryption, which already requires you to <a href="#reference-pulsar-pulsar-client--tls-encryption">provide a client builder customizer</a>, it is recommended to simply add the authentication directly on the client builder in your provided TLS customizer.
You can use the <code>org.apache.pulsar.client.api.AuthenticationFactory</code> to help create the authentication object as follows:
</td>
</tr>
</table>
</div>
<div>
<div>
<pre><code>Authentication auth = AuthenticationFactory.TLS("/path/to/my-role.cert.pem", "/path/to/my-role.key-pk8.pem");</code></pre>
</div>
</div>
<div>
<p>See the official Pulsar documentation on <a href="https://pulsar.apache.org/docs/4.2.x/security-tls-authentication/#configure-mtls-authentication-in-pulsar-clients">mTLS (PEM)</a>.</p>
</div>
</div>
</details>

<details id="mTLS-jks">
<summary><span>Click <mark>here</mark> for <strong>mTLS (JKS)</strong></span></summary>
<div>
<div>
<table>
<tr>
<td>
<i title="Note"></i>
</td>
<td>
Because this option requires TLS encryption, which already requires you to <a href="#reference-pulsar-pulsar-client--tls-encryption">provide a client builder customizer</a>, it is recommended to simply add the authentication directly on the client builder in your provided TLS customizer.
You can use the <code>org.apache.pulsar.client.api.AuthenticationFactory</code> to help create the authentication object as follows:
</td>
</tr>
</table>
</div>
<div>
<div>
<pre><code>Authentication auth = AuthenticationFactory.create(
        "org.apache.pulsar.client.impl.auth.AuthenticationKeyStoreTls",
        Map.of("keyStoreType", "JKS", "keyStorePath", "/path/to/my/keystore.jks", "keyStorePassword", "clientpw"));</code></pre>
</div>
</div>
<div>
<p>See the official Pulsar documentation on <a href="https://pulsar.apache.org/docs/4.2.x/security-tls-authentication/#configure-clients">mTLS (JKS)</a>.</p>
</div>
</div>
</details>

You can find more information on each of the support plugins and their required properties in the official [Pulsar security](https://pulsar.apache.org/docs/4.2.x/security-overview#authentication-providers) documentation.

<a id="reference-pulsar-pulsar-client--auto-cluster-failover"></a>
<a id="reference-pulsar-pulsar-client--3.-automatic-cluster-level-failover"></a>

## 3. Automatic Cluster-Level Failover

The Pulsar Spring Boot Starter also auto-configures the `PulsarClient` for [automatic cluster-level failover](https://pulsar.apache.org/docs/4.2.x/concepts-cluster-level-failover/).

You can use the [`spring.pulsar.client.failover.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties to configure cluster-level failover.

The following example configures the client with a primary and two backup clusters.

application.yml

```yaml
spring:
  pulsar:
    client:
      service-url: "pulsar://my.primary.server:6650"
      failover:
        delay: 30s
        switch-back-delay: 15s
        check-interval: 1s
        backup-clusters:
          - service-url: "pulsar://my.second.server:6650"
            authentication:
              plugin-class-name: org.apache.pulsar.client.impl.auth.AuthenticationToken
              param:
                token: "my-token"
          - service-url: "pulsar://my.third.server:6650"
```

> [!IMPORTANT]
> In addition to the client configuration, there a [few prerequisites](https://pulsar.apache.org/docs/4.2.x/client-libraries-cluster-level-failover/#prerequisites) on the broker that must be satisfied in order to use this feature.

When not using Spring Boot auto-configuration, you can provide a client customizer that configures the client for cluster-level failover.

---

<a id="reference-pulsar-message-production"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar/message-production.html -->

<!-- page_index: 11 -->

# Message Production

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-message-production--page-title"></a>
<a id="reference-pulsar-message-production--message-production"></a>

# Message Production

<a id="reference-pulsar-message-production--pulsar-producer"></a>
<a id="reference-pulsar-message-production--1.-pulsar-template"></a>

## 1. Pulsar Template

On the Pulsar producer side, Spring Boot auto-configuration provides a `PulsarTemplate` for publishing records. The template implements an interface called `PulsarOperations` and provides methods to publish records through its contract.

There are two categories of these send API methods: `send` and `sendAsync`.
The `send` methods block calls by using the synchronous sending capabilities on the Pulsar producer.
They return the `MessageId` of the message that was published once the message is persisted on the broker.
The `sendAsync` method calls are asynchronous calls that are non-blocking.
They return a `CompletableFuture`, which you can use to asynchronously receive the message ID once the messages are published.

> [!NOTE]
> For the API variants that do not include a topic parameter, a [topic resolution process](#reference-topic-resolution--topic-resolution-process) is used to determine the destination topic.

<a id="reference-pulsar-message-production--_simple_api"></a>
<a id="reference-pulsar-message-production--1.1.-simple-api"></a>

### 1.1. Simple API

The template provides a handful of methods ([prefixed with *'send'*](https://docs.spring.io/spring-pulsar/docs/2.0.7-SNAPSHOT/api/org/springframework/pulsar/core/PulsarOperations.html)) for simple send requests. For more complicated send requests, a fluent API lets you configure more options.

<a id="reference-pulsar-message-production--_fluent_api"></a>
<a id="reference-pulsar-message-production--1.2.-fluent-api"></a>

### 1.2. Fluent API

The template provides a [fluent builder](https://docs.spring.io/spring-pulsar/docs/2.0.7-SNAPSHOT/api/org/springframework/pulsar/core/PulsarOperations.html#newMessage(T)) to handle more complicated send requests.

<a id="reference-pulsar-message-production--_message_customization"></a>
<a id="reference-pulsar-message-production--1.3.-message-customization"></a>

### 1.3. Message customization

You can specify a `TypedMessageBuilderCustomizer` to configure the outgoing message. For example, the following code shows how to send a keyed message:

```java
template.newMessage(msg)
    .withMessageCustomizer((mb) -> mb.key("foo-msg-key"))
    .send();
```

<a id="reference-pulsar-message-production--single-producer-customize"></a>
<a id="reference-pulsar-message-production--1.4.-producer-customization"></a>

### 1.4. Producer customization

You can specify a `ProducerBuilderCustomizer` to configure the underlying Pulsar producer builder that ultimately constructs the producer used to send the outgoing message.

> [!WARNING]
> Use with caution as this gives full access to the producer builder and invoking some of its methods (such as `create`) may have unintended side effects.

For example, the following code shows how to disable batching and enable chunking:

```java
template.newMessage(msg)
    .withProducerCustomizer((pb) -> pb.enableChunking(true).enableBatching(false))
    .send();
```

This other example shows how to use custom routing when publishing records to partitioned topics.
Specify your custom `MessageRouter` implementation on the `Producer` builder such as:

```java
template.newMessage(msg)
    .withProducerCustomizer((pb) -> pb.messageRouter(messageRouter))
    .send();
```

> [!TIP]
> Note that, when using a `MessageRouter`, the only valid setting for `spring.pulsar.producer.message-routing-mode` is `custom`.

This other example shows how to add a `ProducerInterceptor` that will intercept and mutate messages received by the producer before being published to the brokers:

```java
template.newMessage(msg)
    .withProducerCustomizer((pb) -> pb.intercept(interceptor))
    .send();
```

The customizer will only apply to the producer used for the send operation.
If you want to apply a customizer to all producers, you must provide them to the producer factory as described in [Global producer customization](#reference-pulsar-message-production--global-producer-customize).

> [!WARNING]
> The rules described in “[Caution on Lambda customizers](#reference-pulsar-message-production--producer-caching-lambdas)” must be followed when using Lambda customizers.

<a id="reference-pulsar-message-production--schema-info-template-imperative"></a>
<a id="reference-pulsar-message-production--2.-specifying-schema-information"></a>

## 2. Specifying Schema Information

If you use Java primitive types, the framework auto-detects the schema for you, and you need not specify any schema types for publishing the data.
For non-primitive types, if the Schema is not explicitly specified when invoking send operations on the `PulsarTemplate`, the Spring for Apache Pulsar framework will try to build a `Schema.JSON` from the type.

> [!IMPORTANT]
> Complex Schema types that are currently supported are JSON, AVRO, PROTOBUF, AUTO\_PRODUCE\_BYTES, and KEY\_VALUE w/ INLINE encoding.

<a id="reference-pulsar-message-production--_custom_schema_mapping"></a>
<a id="reference-pulsar-message-production--2.1.-custom-schema-mapping"></a>

### 2.1. Custom Schema Mapping

As an alternative to specifying the schema when invoking send operations on the `PulsarTemplate` for complex types, the schema resolver can be configured with mappings for the types.
This removes the need to specify the schema as the framework consults the resolver using the outgoing message type.

<a id="reference-pulsar-message-production--_configuration_properties"></a>
<a id="reference-pulsar-message-production--2.1.1.-configuration-properties"></a>

#### 2.1.1. Configuration properties

Schema mappings can be configured with the `spring.pulsar.defaults.type-mappings` property.
The following example uses `application.yml` to add mappings for the `User` and `Address` complex objects using `AVRO` and `JSON` schemas, respectively:

```yaml
spring:
  pulsar:
    defaults:
      type-mappings:
        - message-type: com.acme.User
          schema-info:
            schema-type: AVRO
        - message-type: com.acme.Address
          schema-info:
            schema-type: JSON
```

> [!NOTE]
> The `message-type` is the fully-qualified name of the message class.

<a id="reference-pulsar-message-production--_schema_resolver_customizer"></a>
<a id="reference-pulsar-message-production--2.1.2.-schema-resolver-customizer"></a>

#### 2.1.2. Schema resolver customizer

The preferred method of adding mappings is via the property mentioned above.
However, if more control is needed you can provide a schema resolver customizer to add the mapping(s).

The following example uses a schema resolver customizer to add mappings for the `User` and `Address` complex objects using `AVRO` and `JSON` schemas, respectively:

```java
@Bean
public SchemaResolverCustomizer<DefaultSchemaResolver> schemaResolverCustomizer() {
	return (schemaResolver) -> {
		schemaResolver.addCustomSchemaMapping(User.class, Schema.AVRO(User.class));
		schemaResolver.addCustomSchemaMapping(Address.class, Schema.JSON(Address.class));
	}
}
```

<a id="reference-pulsar-message-production--template-default-schema-annotation"></a>
<a id="reference-pulsar-message-production--2.1.3.-type-mapping-annotation"></a>

#### 2.1.3. Type mapping annotation

Another option for specifying default schema information to use for a particular message type is to mark the message class with the `@PulsarMessage` annotation.
The schema info can be specified via the `schemaType` attribute on the annotation.

The following example configures the system to use JSON as the default schema when producing or consuming messages of type `Foo`:

```java
@PulsarMessage(schemaType = SchemaType.JSON)
record Foo(String value) {
}
```

With this configuration in place, there is no need to set specify the schema on send operations.

<a id="reference-pulsar-message-production--template-auto-produce"></a>
<a id="reference-pulsar-message-production--2.2.-producing-with-auto_schema"></a>

### 2.2. Producing with AUTO\_SCHEMA

If there is no chance to know the type of schema of a Pulsar topic in advance, you can use an [AUTO\_PRODUCE](https://pulsar.apache.org/docs/4.2.x/schema-get-started/#auto_produce) schema to publish a raw JSON or Avro payload as a `byte[]` safely.

In this case, the producer validates whether the outbound bytes are compatible with the schema of the destination topic.

Simply specify a schema of `Schema.AUTO_PRODUCE_BYTES()` on your template send operations as shown in the example below:

```java
void sendUserAsBytes(PulsarTemplate<byte[]> template, byte[] userAsBytes) {
	template.send("user-topic", userAsBytes, Schema.AUTO_PRODUCE_BYTES());
}
```

> [!NOTE]
> This is only supported with Avro and JSON schema types.

<a id="reference-pulsar-message-production--pulsar-producer-factory"></a>
<a id="reference-pulsar-message-production--3.-pulsar-producer-factory"></a>

## 3. Pulsar Producer Factory

The `PulsarTemplate` relies on a `PulsarProducerFactory` to actually create the underlying producer.
Spring Boot auto-configuration also provides this producer factory which you can further configure by specifying any of the [`spring.pulsar.producer.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

> [!NOTE]
> If topic information is not specified when using the producer factory APIs directly, the same [topic resolution process](#reference-topic-resolution--topic-resolution-process) used by the `PulsarTemplate` is used with the one exception that the "Message type default" step is **omitted**.

<a id="reference-pulsar-message-production--global-producer-customize"></a>
<a id="reference-pulsar-message-production--3.1.-global-producer-customization"></a>

### 3.1. Global producer customization

The framework provides the `ProducerBuilderCustomizer` contract which allows you to configure the underlying builder which is used to construct each producer.
To customize all producers, you can pass a list of customizers into the `PulsarProducerFactory` constructor.
When using multiple customizers, they are applied in the order in which they appear in the list.

> [!TIP]
> If you use Spring Boot auto-configuration, you can specify the customizers as beans and they will be passed automatically to the `PulsarProducerFactory`, ordered according to their `@Order` annotation.

If you want to apply a customizer to just a single producer, you can use the Fluent API and [specify the customizer at send time](#reference-pulsar-message-production--single-producer-customize).

<a id="reference-pulsar-message-production--producer-caching"></a>
<a id="reference-pulsar-message-production--4.-pulsar-producer-caching"></a>

## 4. Pulsar Producer Caching

Each underlying Pulsar producer consumes resources.
To improve performance and avoid continual creation of producers, the producer factory caches the producers that it creates.
They are cached in an LRU fashion and evicted when they have not been used within a configured time period.
The [cache key](https://github.com/spring-projects/spring-pulsar/blob/8e33ac0b122bc0e75df299919c956cacabcc9809/spring-pulsar/src/main/java/org/springframework/pulsar/core/CachingPulsarProducerFactory.java#L159) is composed of just enough information to ensure that callers are returned the same producer on subsequent creation requests.

Additionally, you can configure the cache settings by specifying any of the [`spring.pulsar.producer.cache.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

<a id="reference-pulsar-message-production--producer-caching-lambdas"></a>
<a id="reference-pulsar-message-production--4.1.-caution-on-lambda-customizers"></a>

### 4.1. Caution on Lambda customizers

Any user-provided producer customizers are also included in the cache key.
Because the cache key relies on a valid implementation of `equals/hashCode`, one must take caution when using Lambda customizers.

> [!IMPORTANT]
> **RULE:** Two customizers implemented as Lambdas will match on `equals/hashCode` **if and only if** they use the same Lambda instance and do not require any variable defined outside its closure.

To clarify the above rule we will look at a few examples.
In the following example, the customizer is defined as an inline Lambda which means that each call to `sendUser` uses the same Lambda instance. Additionally, it requires no variable outside its closure. Therefore, it **will** match as a cache key.

```java
void sendUser() {
    var user = randomUser();
    template.newMessage(user)
        .withTopic("user-topic")
        .withProducerCustomizer((b) -> b.producerName("user"))
        .send();
}
```

In this next case, the customizer is defined as an inline Lambda which means that each call to `sendUser` uses the same Lambda instance. However, it requires a variable outside its closure. Therefore, it **will not** match as a cache key.

```java
void sendUser() {
    var user = randomUser();
    var name = randomName();
    template.newMessage(user)
        .withTopic("user-topic")
        .withProducerCustomizer((b) -> b.producerName(name))
        .send();
}
```

In this final example, the customizer is defined as an inline Lambda which means that each call to `sendUser` uses the same Lambda instance. While it does use a variable name, it does not originate outside its closure and therefore **will** match as a cache key.
This illustrates that variables can be used **within** the Lambda closure and can even make calls to static methods.

```java
void sendUser() {
    var user = randomUser();
    template.newMessage(user)
        .withTopic("user-topic")
        .withProducerCustomizer((b) -> {
           var name = SomeHelper.someStaticMethod();
           b.producerName(name);
        })
        .send();
}
```

> [!IMPORTANT]
> **RULE:** If your Lambda customizer is not defined **once and only once** (the same instance is used on subsequent calls) **OR** it requires variable(s) defined outside its closure then you must provide a customizer implementation with a valid `equals/hashCode` implementation.

> [!WARNING]
> If these rules are not followed then the producer cache will always miss and your application performance will be negatively affected.

<a id="reference-pulsar-message-production--_intercept_messages_on_the_producer"></a>
<a id="reference-pulsar-message-production--5.-intercept-messages-on-the-producer"></a>

## 5. Intercept Messages on the Producer

Adding a `ProducerInterceptor` lets you intercept and mutate messages received by the producer before they are published to the brokers.
To do so, you can pass a list of interceptors into the `PulsarTemplate` constructor.
When using multiple interceptors, the order they are applied in is the order in which they appear in the list.

If you use Spring Boot auto-configuration, you can specify the interceptors as Beans.
They are passed automatically to the `PulsarTemplate`.
Ordering of the interceptors is achieved by using the `@Order` annotation as follows:

```java
@Bean @Order(100) ProducerInterceptor firstInterceptor() {...}
@Bean @Order(200) ProducerInterceptor secondInterceptor() {...}
```

> [!NOTE]
> If you are not using the starter, you will need to configure and register the aforementioned components yourself.

---

<a id="reference-pulsar-message-consumption"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar/message-consumption.html -->

<!-- page_index: 12 -->

# Message Consumption

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-message-consumption--page-title"></a>
<a id="reference-pulsar-message-consumption--message-consumption"></a>

# Message Consumption

<a id="reference-pulsar-message-consumption--pulsar-listener"></a>
<a id="reference-pulsar-message-consumption--1.-pulsar-listener"></a>

## 1. Pulsar Listener

When it comes to Pulsar consumers, we recommend that end-user applications use the `PulsarListener` annotation.
To use `PulsarListener`, you need to use the `@EnablePulsar` annotation.
When you use Spring Boot support, it automatically enables this annotation and configures all the components necessary for `PulsarListener`, such as the message listener infrastructure (which is responsible for creating the Pulsar consumer).
`PulsarMessageListenerContainer` uses a `PulsarConsumerFactory` to create and manage the Pulsar consumer the underlying Pulsar consumer that it uses to consume messages.

Spring Boot provides this consumer factory which you can further configure by specifying the [`spring.pulsar.consumer.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

Let us revisit the `PulsarListener` code snippet we saw in the quick-tour section:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar")
public void listen(String message) {
    System.out.println("Message Received: " + message);
}
```

You can further simplify this method:

```java
@PulsarListener
public void listen(String message) {
    System.out.println("Message Received: " + message);
}
```

In this most basic form, when the `subscriptionName` is not provided on the `@PulsarListener` annotation an auto-generated subscription name will be used.
Likewise, when the `topics` are not directly provided, a [topic resolution process](#reference-topic-resolution--topic-resolution-process) is used to determine the destination topic.

In the `PulsarListener` method shown earlier, we receive the data as `String`, but we do not specify any schema types.
Internally, the framework relies on Pulsar’s schema mechanism to convert the data to the required type.
The framework detects that you expect the `String` type and then infers the schema type based on that information and provides that schema to the consumer.
The framework does this inference for all primitive types.
For all non-primitive types the default schema is assumed to be JSON.
If a complex type is using anything besides JSON (such as AVRO or KEY\_VALUE) you must provide the schema type on the annotation using the `schemaType` property.

The following example shows another `PulsarListener` method, which takes an `Integer`:

```java
@PulsarListener(subscriptionName = "my-subscription-1", topics = "my-topic-1")
public void listen(Integer message) {
   System.out.println(message);
}
```

The following `PulsarListener` method shows how we can consume complex types from a topic:

```java
@PulsarListener(subscriptionName = "my-subscription-2", topics = "my-topic-2", schemaType = SchemaType.JSON)
public void listen(Foo message) {
    System.out.println(message);
}
```

Let us look at a few more ways.

You can consume the Pulsar message directly:

```java
@PulsarListener(subscriptionName = "my-subscription", topics = "my-topic")
public void listen(org.apache.pulsar.client.api.Message<String> message) {
    System.out.println(message.getValue());
}
```

The following example consumes the record by using the Spring messaging envelope:

```java
@PulsarListener(subscriptionName = "my-subscription", topics = "my-topic")
public void listen(org.springframework.messaging.Message<String> message) {
    System.out.println(message.getPayload());
}
```

Now let us see how we can consume records in batches.
The following example uses `PulsarListener` to consume records in batches as POJOs:

```java
@PulsarListener(subscriptionName = "hello-batch-subscription", topics = "hello-batch", schemaType = SchemaType.JSON, batch = true)
public void listen(List<Foo> messages) {
    System.out.println("records received :" + messages.size());
    messages.forEach((message) -> System.out.println("record : " + message));
}
```

Note that, in this example, we receive the records as a collection (`List`) of objects.
In addition, to enable batch consumption at the `PulsarListener` level, you need to set the `batch` property on the annotation to `true`.

Based on the actual type that the `List` holds, the framework tries to infer the schema to use.
If the `List` contains a complex type besides JSON, you still need to provide the `schemaType` on `PulsarListener`.

The following uses the `Message` envelope provided by the Pulsar Java client:

```java
@PulsarListener(subscriptionName = "hello-batch-subscription", topics = "hello-batch", schemaType = SchemaType.JSON, batch = true)
public void listen(List<Message<Foo>> messages) {
    System.out.println("records received :" + messages.size());
    messages.forEach((message) -> System.out.println("record : " + message.getValue()));
}
```

The following example consumes batch records with an envelope of the Spring messaging `Message` type:

```java
@PulsarListener(subscriptionName = "hello-batch-subscription", topics = "hello-batch", schemaType = SchemaType.JSON, batch = true)
public void listen(List<org.springframework.messaging.Message<Foo>> messages) {
    System.out.println("records received :" + messages.size());
    messages.forEach((message) -> System.out.println("record : " + message.getPayload()));
}
```

Finally, you can also use the `Messages` holder object from Pulsar for the batch listener:

```java
@PulsarListener(subscriptionName = "hello-batch-subscription", topics = "hello-batch", schemaType = SchemaType.JSON, batch = true)
public void listen(org.apache.pulsar.client.api.Messages<Foo>> messages) {
    System.out.println("records received :" + messages.size());
    messages.forEach((message) -> System.out.println("record : " + message.getValue()));
}
```

When you use `PulsarListener`, you can provide Pulsar consumer properties directly on the annotation itself.
This is convenient if you do not want to use the Boot configuration properties mentioned earlier or have multiple `PulsarListener` methods.

The following example uses Pulsar consumer properties directly on `PulsarListener`:

```java
@PulsarListener(properties = { "subscriptionName=subscription-1", "topicNames=foo-1", "receiverQueueSize=5000" })
void listen(String message) {
}
```

> [!TIP]
> The properties used are direct Pulsar consumer properties, not the `spring.pulsar.consumer` application configuration properties

<a id="reference-pulsar-message-consumption--listener-auto-consume"></a>
<a id="reference-pulsar-message-consumption--1.1.-generic-records-with-auto_consume"></a>

### 1.1. Generic records with AUTO\_CONSUME

If there is no chance to know the type of schema of a Pulsar topic in advance, you can use the `AUTO_CONSUME` schema type to consume generic records.
In this case, the topic deserializes messages into `GenericRecord` objects using the schema info associated with the topic.

To consume generic records set the `schemaType = SchemaType.AUTO_CONSUME` on your `@PulsarListener` and use a Pulsar message of type `GenericRecord` as the message parameter as shown below.

```java
@PulsarListener(topics = "my-generic-topic", schemaType = SchemaType.AUTO_CONSUME)
void listen(org.apache.pulsar.client.api.Message<GenericRecord> message) {
    GenericRecord record = message.getValue();
    record.getFields().forEach((f) ->
            System.out.printf("%s = %s%n", f.getName(), record.getField(f)));
}
```

> [!TIP]
> The `GenericRecord` API allows access to the fields and their associated values

<a id="reference-pulsar-message-consumption--_customizing_the_consumerbuilder"></a>
<a id="reference-pulsar-message-consumption--1.2.-customizing-the-consumerbuilder"></a>

### 1.2. Customizing the ConsumerBuilder

You can customize any fields available through `ConsumerBuilder` using a `PulsarListenerConsumerBuilderCustomizer` by providing a `@Bean` of type `PulsarListenerConsumerBuilderCustomizer` and then making it available to the `PulsarListener` as shown below.

```java
@PulsarListener(topics = "hello-topic", consumerCustomizer = "myCustomizer") public void listen(String message) {System.out.println("Message Received: " + message);}
@Bean PulsarListenerConsumerBuilderCustomizer<String> myCustomizer() {return (builder) -> builder.consumerName("myConsumer");}
```

> [!TIP]
> If your application only has a single `@PulsarListener` and a single `PulsarListenerConsumerBuilderCustomizer` bean registered then the customizer will be automatically applied.

<a id="reference-pulsar-message-consumption--schema-info-listener-imperative"></a>
<a id="reference-pulsar-message-consumption--2.-specifying-schema-information"></a>

## 2. Specifying Schema Information

As indicated earlier, for Java primitives, the Spring for Apache Pulsar framework can infer the proper Schema to use on the `PulsarListener`.
For non-primitive types, if the Schema is not explicitly specified on the annotation, the Spring for Apache Pulsar framework will try to build a `Schema.JSON` from the type.

> [!IMPORTANT]
> Complex Schema types that are currently supported are JSON, AVRO, PROTOBUF, AUTO\_CONSUME, KEY\_VALUE w/ INLINE encoding.

<a id="reference-pulsar-message-consumption--_custom_schema_mapping"></a>
<a id="reference-pulsar-message-consumption--2.1.-custom-schema-mapping"></a>

### 2.1. Custom Schema Mapping

As an alternative to specifying the schema on the `PulsarListener` for complex types, the schema resolver can be configured with mappings for the types.
This removes the need to set the schema on the listener as the framework consults the resolver using the incoming message type.

<a id="reference-pulsar-message-consumption--_configuration_properties"></a>
<a id="reference-pulsar-message-consumption--2.1.1.-configuration-properties"></a>

#### 2.1.1. Configuration properties

Schema mappings can be configured with the `spring.pulsar.defaults.type-mappings` property.
The following example uses `application.yml` to add mappings for the `User` and `Address` complex objects using `AVRO` and `JSON` schemas, respectively:

```yaml
spring:
  pulsar:
    defaults:
      type-mappings:
        - message-type: com.acme.User
          schema-info:
            schema-type: AVRO
        - message-type: com.acme.Address
          schema-info:
            schema-type: JSON
```

> [!NOTE]
> The `message-type` is the fully-qualified name of the message class.

<a id="reference-pulsar-message-consumption--_schema_resolver_customizer"></a>
<a id="reference-pulsar-message-consumption--2.1.2.-schema-resolver-customizer"></a>

#### 2.1.2. Schema resolver customizer

The preferred method of adding mappings is via the property mentioned above.
However, if more control is needed you can provide a schema resolver customizer to add the mapping(s).

The following example uses a schema resolver customizer to add mappings for the `User` and `Address` complex objects using `AVRO` and `JSON` schemas, respectively:

```java
@Bean
public SchemaResolverCustomizer<DefaultSchemaResolver> schemaResolverCustomizer() {
	return (schemaResolver) -> {
		schemaResolver.addCustomSchemaMapping(User.class, Schema.AVRO(User.class));
		schemaResolver.addCustomSchemaMapping(Address.class, Schema.JSON(Address.class));
	}
}
```

<a id="reference-pulsar-message-consumption--listener-default-schema-annotation"></a>
<a id="reference-pulsar-message-consumption--2.1.3.-type-mapping-annotation"></a>

#### 2.1.3. Type mapping annotation

Another option for specifying default schema information to use for a particular message type is to mark the message class with the `@PulsarMessage` annotation.
The schema info can be specified via the `schemaType` attribute on the annotation.

The following example configures the system to use JSON as the default schema when producing or consuming messages of type `Foo`:

```java
@PulsarMessage(schemaType = SchemaType.JSON)
record Foo(String value) {
}
```

With this configuration in place, there is no need to set the schema on the listener, for example:

```java
@PulsarListener(subscriptionName = "user-sub", topics = "user-topic")
public void listen(User user) {
    System.out.println(user);
}
```

<a id="reference-pulsar-message-consumption--_accessing_the_pulsar_consumer_object"></a>
<a id="reference-pulsar-message-consumption--3.-accessing-the-pulsar-consumer-object"></a>

## 3. Accessing the Pulsar Consumer Object

Sometimes, you need direct access to the Pulsar Consumer object.
The following example shows how to get it:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar")
public void listen(String message, org.apache.pulsar.client.api.Consumer<String> consumer) {
    System.out.println("Message Received: " + message);
    ConsumerStats stats = consumer.getStats();
    ...
}
```

> [!WARNING]
> When accessing the `Consumer` object this way, do NOT invoke any operations that would change the Consumer’s cursor position by invoking any receive methods.
> All such operations must be done by the container.

<a id="reference-pulsar-message-consumption--pulsar-message-listener-container"></a>
<a id="reference-pulsar-message-consumption--4.-pulsar-message-listener-container"></a>

## 4. Pulsar Message Listener Container

Now that we saw the basic interactions on the consumer side through `PulsarListener`. Let us now dive into the inner workings of how `PulsarListener` interacts with the underlying Pulsar consumer.
Keep in mind that, for end-user applications, in most scenarios, we recommend using the `PulsarListener` annotation directly for consuming from a Pulsar topic when using Spring for Apache Pulsar, as that model covers a broad set of application use cases.
However, it is important to understand how `PulsarListener` works internally. This section goes through those details.

As briefly mentioned earlier, the message listener container is at the heart of message consumption when you use Spring for Apache Pulsar.
`PulsarListener` uses the message listener container infrastructure behind the scenes to create and manage the Pulsar consumer.
Spring for Apache Pulsar provides the contract for this message listener container through `PulsarMessageListenerContainer`.
The default implementation for this message listener container is provided through `DefaultPulsarMessageListenerContainer`.
As its name indicates, `PulsarMessageListenerContainer` contains the message listener.
The container creates the Pulsar consumer and then runs a separate thread to receive and handle the data.
The data is handled by the provided message listener implementation.

The message listener container consumes the data in batch by using the consumer’s `batchReceive` method.
Once data is received, it is handed over to the selected message listener implementation.

The following message listener types are available when you use Spring for Apache Pulsar.

- [PulsarRecordMessageListener](https://github.com/spring-projects/spring-pulsar/blob/8e33ac0b122bc0e75df299919c956cacabcc9809/spring-pulsar/src/main/java/org/springframework/pulsar/listener/PulsarRecordMessageListener.java#L29)
- [PulsarAcknowledgingMessageListener](https://github.com/spring-projects/spring-pulsar/blob/ade2c74482d8ac1407ffe4840fa058475c07bcfc/spring-pulsar/src/main/java/org/springframework/pulsar/listener/PulsarAcknowledgingMessageListener.java#L28)
- [PulsarBatchMessageListener](https://github.com/spring-projects/spring-pulsar/blob/ade2c74482d8ac1407ffe4840fa058475c07bcfc/spring-pulsar/src/main/java/org/springframework/pulsar/listener/PulsarBatchMessageListener.java#L36)
- [PulsarBatchAcknowledgingMessageListener](https://github.com/spring-projects/spring-pulsar/blob/ade2c74482d8ac1407ffe4840fa058475c07bcfc/spring-pulsar/src/main/java/org/springframework/pulsar/listener/PulsarBatchAcknowledgingMessageListener.java#L28)

We see the details about these various message listeners in the following sections.

Before doing so, however, let us take a closer look at the container itself.

<a id="reference-pulsar-message-consumption--_defaultpulsarmessagelistenercontainer"></a>
<a id="reference-pulsar-message-consumption--4.1.-defaultpulsarmessagelistenercontainer"></a>

### 4.1. DefaultPulsarMessageListenerContainer

This is a single consumer-based message listener container.
The following listing shows its constructor:

```java
public DefaultPulsarMessageListenerContainer(PulsarConsumerFactory<? super T> pulsarConsumerFactory,
			PulsarContainerProperties pulsarContainerProperties)
}
```

It receives a `PulsarConsumerFactory` (which it uses to create the consumer) and a `PulsarContainerProperties` object (which contains information about the container properties).
`PulsarContainerProperties` has the following constructors:

```java
public PulsarContainerProperties(String... topics)

public PulsarContainerProperties(Pattern topicPattern)
```

You can provide the topic information through `PulsarContainerProperties` or as a consumer property that is provided to the consumer factory.
The following example uses the `DefaultPulsarMessageListenerContainer`:

```java
Map<String, Object> config = new HashMap<>();
config.put("topics", "my-topic");
PulsarConsumerFactory<String> pulsarConsumerFactorY = DefaultPulsarConsumerFactory<>(pulsarClient, config);

PulsarContainerProperties pulsarContainerProperties = new PulsarContainerProperties();

pulsarContainerProperties.setMessageListener((PulsarRecordMessageListener<?>) (consumer, msg) -> {
		});

DefaultPulsarMessageListenerContainer<String> pulsarListenerContainer = new DefaultPulsarMessageListenerContainer(pulsarConsumerFacotyr,
        pulsarContainerProperties);

return pulsarListenerContainer;
```

> [!NOTE]
> If topic information is not specified when using the listener containers directly, the same
> [topic resolution process](#reference-topic-resolution--topic-resolution-process) used by the `PulsarListener` is used with the one exception that the "Message type default" step is **omitted**.

`DefaultPulsarMessageListenerContainer` creates only a single consumer.
If you want to have multiple consumers managed through multiple threads, you need to use `ConcurrentPulsarMessageListenerContainer`.

<a id="reference-pulsar-message-consumption--_concurrentpulsarmessagelistenercontainer"></a>
<a id="reference-pulsar-message-consumption--4.2.-concurrentpulsarmessagelistenercontainer"></a>

### 4.2. ConcurrentPulsarMessageListenerContainer

`ConcurrentPulsarMessageListenerContainer` has the following constructor:

```java
public ConcurrentPulsarMessageListenerContainer(PulsarConsumerFactory<? super T> pulsarConsumerFactory,
    PulsarContainerProperties pulsarContainerProperties)
```

`ConcurrentPulsarMessageListenerContainer` lets you specify a `concurrency` property through a setter.
Concurrency of more than `1` is allowed only on non-exclusive subscriptions (`failover`, `shared`, and `key-shared`).
You can only have the default `1` for concurrency when you have an exclusive subscription mode.

The following example enables `concurrency` through the `PulsarListener` annotation for a `failover` subscription.

```java
@PulsarListener(topics = "my-topic", subscriptionName = "subscription-1",
				subscriptionType = SubscriptionType.Failover, concurrency = "3")
void listen(String message, Consumer<String> consumer) {
    ...
    System.out.println("Current Thread: " + Thread.currentThread().getName());
    System.out.println("Current Consumer: " + consumer.getConsumerName());
}
```

In the preceding listener, it is assumed that the topic `my-topic` has three partitions.
If it is a non-partitioned topic, having concurrency set to `3` does nothing. You get two idle consumers in addition to the main active one.
If the topic has more than three partitions, messages are load-balanced across the consumers that the container creates.
If you run this `PulsarListener`, you see that messages from different partitions are consumed through different consumers, as implied by the thread name and consumer names printouts in the preceding example.

> [!NOTE]
> When you use the `Failover` subscription this way on partitioned topics, Pulsar guarantees message ordering.

The following listing shows another example of `PulsarListener`, but with `Shared` subscription and `concurrency` enabled.

```java
@PulsarListener(topics = "my-topic", subscriptionName = "subscription-1",
				subscriptionType = SubscriptionType.Shared, concurrency = "5")
void listen(String message) {
    ...
}
```

In the preceding example, the `PulsarListener` creates five different consumers (this time, we assume that the topic has five partitions).

> [!NOTE]
> In this version, there is no message ordering, as `Shared` subscriptions do not guarantee any message ordering in Pulsar.

If you need message ordering and still want a shared subscription types, you need to use the `Key_Shared` subscription type.

<a id="reference-pulsar-message-consumption--consuming-records"></a>
<a id="reference-pulsar-message-consumption--4.3.-consuming-records"></a>

### 4.3. Consuming Records

Let us take a look at how the message listener container enables both single-record and batch-based message consumption.

<a id="reference-pulsar-message-consumption--_single_record_consumption"></a>
<a id="reference-pulsar-message-consumption--single-record-consumption"></a>

### Single Record Consumption

Let us revisit our basic `PulsarListener` for the sake of this discussion:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar")
public void listen(String message) {
    System.out.println("Message Received: " + message);
}
```

With this `PulsarListener` method, we essential ask Spring for Apache Pulsar to invoke the listener method with a single record each time.
We mentioned that the message listener container consumes the data in batches using the `batchReceive` method on the consumer.
The framework detects that the `PulsarListener`, in this case, receives a single record. This means that, on each invocation of the method, it needs a singe record.
Although the records are consumed by the message listener container in batches, it iterates through the received batch and invokes the listener method through an adapter for `PulsarRecordMessageListener`.
As you can see in the previous section, `PulsarRecordMessageListener` extends from the `MessageListener` provided by the Pulsar Java client, and it supports the basic `received` method.

<a id="reference-pulsar-message-consumption--_batch_consumption"></a>
<a id="reference-pulsar-message-consumption--batch-consumption"></a>

### Batch Consumption

The following example shows the `PulsarListener` consuming records in batches:

```java
@PulsarListener(subscriptionName = "hello-batch-subscription", topics = "hello-batch", schemaType = SchemaType.JSON, batch = true)
public void listen4(List<Foo> messages) {
    System.out.println("records received :" + messages.size());
    messages.forEach((message) -> System.out.println("record : " + message));
}
```

When you use this type of `PulsarListener`, the framework detects that you are in batch mode.
Since it already received the data in batches by using the Consumer’s `batchReceive` method, it hands off the entire batch to the listener method through an adapter for `PulsarBatchMessageListener`.

<a id="reference-pulsar-message-consumption--pulsar-headers"></a>
<a id="reference-pulsar-message-consumption--5.-pulsar-headers"></a>

## 5. Pulsar Headers

Pulsar does not have a first-class “header” concept but instead provides a map for custom user properties as well as methods to access the message metadata typically stored in a message header (eg. `id` and `event-time`).
As such, the terms “Pulsar message header” and “Pulsar message metadata” are used interchangeably.
The list of available message metadata (headers) can be found in [PulsarHeaders.java](https://github.com/spring-projects/spring-pulsar/blob/main/spring-pulsar/src/main/java/org/springframework/pulsar/support/PulsarHeaders.java).

<a id="reference-pulsar-message-consumption--_spring_headers"></a>
<a id="reference-pulsar-message-consumption--5.1.-spring-headers"></a>

### 5.1. Spring Headers

Spring Messaging provides first-class “header” support via its `MessageHeaders` abstraction.

The Pulsar message metadata can be consumed as Spring message headers.
The list of available headers can be found in [PulsarHeaders.java](https://github.com/spring-projects/spring-pulsar/blob/main/spring-pulsar/src/main/java/org/springframework/pulsar/support/PulsarHeaders.java).

<a id="reference-pulsar-message-consumption--_accessing_in_single_record_based_consumer"></a>
<a id="reference-pulsar-message-consumption--5.2.-accessing-in-single-record-based-consumer"></a>

### 5.2. Accessing in Single Record based Consumer

The following example shows how you can access the various Pulsar Headers in an application that uses the single record mode of consuming:

```java
@PulsarListener(topics = "simpleListenerWithHeaders")
void simpleListenerWithHeaders(String data, @Header(PulsarHeaders.MESSAGE_ID) MessageId messageId,
                @Header(PulsarHeaders.RAW_DATA) byte[] rawData,
                @Header("foo") String foo) {

}
```

In the preceding example, we access the values for the `messageId` and `rawData` message metadata as well as a custom message property named `foo`.
The Spring `@Header` annotation is used for each header field.

You can also use Pulsar’s `Message` as the envelope to carry the payload.
When doing so, the user can directly call the corresponding methods on the Pulsar message for retrieving the metadata.
However, as a convenience, you can also retrieve it by using the `Header` annotation.
Note that you can also use the Spring messaging `Message` envelope to carry the payload and then retrieve the Pulsar headers by using `@Header`.

<a id="reference-pulsar-message-consumption--_accessing_in_batch_record_based_consumer"></a>
<a id="reference-pulsar-message-consumption--5.3.-accessing-in-batch-record-based-consumer"></a>

### 5.3. Accessing in Batch Record based Consumer

In this section, we see how to access the various Pulsar Headers in an application that uses a batch consumer:

```java
@PulsarListener(topics = "simpleBatchListenerWithHeaders", batch = true)
void simpleBatchListenerWithHeaders(List<String> data,
					@Header(PulsarHeaders.MESSAGE_ID) List<MessageId> messageIds,
					@Header(PulsarHeaders.TOPIC_NAME) List<String> topicNames, @Header("foo") List<String> fooValues) {

}
```

In the preceding example, we consume the data as a `List<String>`.
When extracting the various headers, we do so as a `List<>` as well.
Spring for Apache Pulsar ensures that the headers list corresponds to the data list.

You can also extract headers in the same manner when you use the batch listener and receive payloads as `List<org.apache.pulsar.client.api.Message<?>`, `org.apache.pulsar.client.api.Messages<?>`, or `org.springframework.messaging.Messsge<?>`.

<a id="reference-pulsar-message-consumption--_message_header_mapping"></a>
<a id="reference-pulsar-message-consumption--5.4.-message-header-mapping"></a>

### 5.4. Message Header Mapping

The `PulsarHeaderMapper` strategy is provided to map headers to and from Pulsar user properties and Spring `MessageHeaders`.

Its interface definition is as follows:

```java
public interface PulsarHeaderMapper {

	Map<String, String> toPulsarHeaders(MessageHeaders springHeaders);

	MessageHeaders toSpringHeaders(Message<?> pulsarMessage);
}
```

The framework provides a couple of mapper implementations.

- The `JsonPulsarHeaderMapper` maps headers as JSON in order to support rich header types and is the default when the Jackson JSON library is on the classpath.
- The `ToStringPulsarHeaderMapper` maps headers as strings using the `toString()` method on the header values and is the fallback mapper.

<a id="reference-pulsar-message-consumption--_json_header_mapper"></a>
<a id="reference-pulsar-message-consumption--5.4.1.-json-header-mapper"></a>

#### 5.4.1. JSON Header Mapper

The `JsonPulsarHeaderMapper` uses a “special” header (with a key of `spring_json_header_types`) that contains a JSON map of `<key>:<type>`.
This header is used on the inbound side (Pulsar → Spring) to provide appropriate conversion of each header value to the original type.

<a id="reference-pulsar-message-consumption--_trusted_packages"></a>
<a id="reference-pulsar-message-consumption--trusted-packages"></a>

##### Trusted Packages

By default, the JSON mapper deserializes header types whose package exactly matches one of the following safe defaults: `java.lang`, `java.net`, `java.util`, and `org.springframework.util`.
A class whose package is not in the trusted list is returned to the application as a `NonTrustedHeaderType` wrapper rather than being deserialized.

Trust is evaluated by exact package match.
Sub-packages are not trusted transitively: trusting `java.util` does NOT automatically trust `java.util.concurrent` or `java.util.logging`.
Each package you need must be listed explicitly.

To extend the trusted set for annotation-driven listeners (`@PulsarListener` / `@PulsarReader`) without replacing the entire converter, register a `String[]` bean named `pulsarHeaderTrustedPackages` in your application context:

```java
@Bean(name = "pulsarHeaderTrustedPackages")
String[] pulsarHeaderTrustedPackages() {
    return new String[] { "com.example.events", "com.example.dto" };
}
```

The framework picks up this bean automatically and applies it to every listener and reader endpoint, composing it with any custom `pulsarHeaderObjectMapper` bean you may also have defined.

If you are constructing a `JsonPulsarHeaderMapper` directly via the builder, pass the packages there instead:

```java
@Bean
JsonPulsarHeaderMapper headerMapper() {
    return JsonPulsarHeaderMapper.builder()
        .trustedPackages("com.example.events", "com.example.dto")
        .build();
}
```

To trust all packages — for example, in a fully-controlled, internal messaging environment — pass `"*"` as the sole entry in either approach:

```java
// via bean
@Bean(name = "pulsarHeaderTrustedPackages")
String[] pulsarHeaderTrustedPackages() {
    return new String[] { "*" };
}

// via builder
JsonPulsarHeaderMapper.builder().trustedPackages("*").build();
```

> [!WARNING]
> Using `"*"` allows any class reachable on the classpath to be loaded and partially instantiated during deserialization of incoming message headers.
> Do not use it when consuming messages from untrusted or external sources.

<a id="reference-pulsar-message-consumption--_tostring_classes"></a>
<a id="reference-pulsar-message-consumption--tostring-classes"></a>

##### ToString Classes

Certain types are not suitable for JSON serialization, and a simple `toString()` serialization might be preferred for these types.
The `JsonPulsarHeaderMapper` has a property called `addToStringClasses()` that lets you supply the names of classes that should be treated this way for outbound mapping.
During inbound mapping, they are mapped as `String`.
By default, only `org.springframework.util.MimeType` and `org.springframework.http.MediaType` are mapped this way.

<a id="reference-pulsar-message-consumption--_custom_objectmapper"></a>
<a id="reference-pulsar-message-consumption--custom-objectmapper"></a>

##### Custom ObjectMapper

The JSON mapper uses a reasonable configured Jackson 2 `ObjectMapper` to handle serialization of header values.
However, to provide a custom object mapper one must simply provide an `ObjectMapper` bean with the name `pulsarHeaderObjectMapper`.
For example:

```java
@Configuration(proxyBeanMethods = false) static class PulsarHeadersCustomObjectMapperTestConfig {
@Bean(name = "pulsarHeaderObjectMapper") ObjectMapper customObjectMapper() {var objectMapper = new ObjectMapper(); // do things with your special header object mapper here return objectMapper;}}
```

> [!IMPORTANT]
> The object mapper in the example above should be an instance of `com.fasterxml.jackson.databind.ObjectMapper`, **not** the shaded `org.apache.pulsar.shade.com.fasterxml.jackson.databind.ObjectMapper`.

> [!IMPORTANT]
> The [same limitations](#reference-custom-object-mapper--jackson2vs3) regarding Jackson 2 vs. Jackson 3 apply here }

<a id="reference-pulsar-message-consumption--_inboundoutbound_patterns"></a>
<a id="reference-pulsar-message-consumption--5.5.-inbound-outbound-patterns"></a>

### 5.5. Inbound/Outbound Patterns

On the inbound side, by default, all Pulsar headers (message metadata plus user properties) are mapped to `MessageHeaders`.
On the outbound side, by default, all `MessageHeaders` are mapped, except `id`, `timestamp`, and the headers that represent the Pulsar message metadata (i.e. the headers that are prefixed with `pulsar_message_`).
You can specify which headers are mapped for inbound and outbound messages by configuring the `inboundPatterns` and `outboundPatterns` on a mapper bean you provide.
You can include Pulsar message metadata headers on the outbound messages by adding the exact header name to the `outboundPatterns` as patterns are not supported for metadata headers.
Patterns are rather simple and can contain a leading wildcard (`*`), a trailing wildcard, or both (for example, `*.cat.*`).
You can negate patterns with a leading `!`.
The first pattern that matches a header name (whether positive or negative) wins.

> [!IMPORTANT]
> When you provide your own patterns, we recommend including `!id` and `!timestamp`, since these headers are read-only on the inbound side.

<a id="reference-pulsar-message-consumption--_message_acknowledgment"></a>
<a id="reference-pulsar-message-consumption--6.-message-acknowledgment"></a>

## 6. Message Acknowledgment

When you use Spring for Apache Pulsar, the message acknowledgment is handled by the framework, unless opted out by the application.
In this section, we go through the details of how the framework takes care of message acknowledgment.

<a id="reference-pulsar-message-consumption--message-ack-modes"></a>
<a id="reference-pulsar-message-consumption--6.1.-message-ack-modes"></a>

### 6.1. Message ACK modes

Spring for Apache Pulsar provides the following modes for acknowledging messages:

- `BATCH`
- `RECORD`
- `MANUAL`

`BATCH` acknowledgment mode is the default, but you can change it on the message listener container.
In the following sections, we see how acknowledgment works when you use both single and batch versions of `PulsarListener` and how they translate to the backing message listener container (and, ultimately, to the Pulsar consumer).

<a id="reference-pulsar-message-consumption--_automatic_message_ack_in_single_record_mode"></a>
<a id="reference-pulsar-message-consumption--6.2.-automatic-message-ack-in-single-record-mode"></a>

### 6.2. Automatic Message Ack in Single Record Mode

Let us revisit our basic single message based `PulsarListener`:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar")
public void listen(String message) {
    System.out.println("Message Received: " + message);
}
```

It is natural to wonder, how acknowledgment works when you use `PulsarListener`, especially if you are familiar with using Pulsar consumer directly.
The answer comes down to the message listener container, as that is the central place in Spring for Apache Pulsar that coordinates all the consumer related activities.

Assuming you are not overriding the default behavior, this is what happens behind the scenes when you use the preceding `PulsarListener`:

1. First, the listener container receives messages as batches from the Pulsar consumer.
2. The received messages are handed down to `PulsarListener` one message at a time.
3. When all the records are handed down to the listener method and successfully processed, the container acknowledges all the messages from the original batch.

This is the normal flow. If any records from the original batch throw an exception, Spring for Apache Pulsar track those records separately.
When all the records from the batch are processed, Spring for Apache Pulsar acknowledges all the successful messages and negatively acknowledges (nack) all the failed messages.
In other words, when consuming single records by using `PulsarRecordMessageListener` and the default ack mode of `BATCH` is used, the framework waits for all the records received from the `batchReceive` call to process successfully and then calls the `acknowledge` method on the Pulsar consumer.
If any particular record throws an exception when invoking the handler method, Spring for Apache Pulsar tracks those records and separately calls `negativeAcknowledge` on those records after the entire batch is processed.

If the application wants the acknowledgment or negative acknowledgment to occur per record, the `RECORD` ack mode can be enabled.
In that case, after handling each record, the message is acknowledged if no error and negatively acknowledged if there was an error.
The following example enables `RECORD` ack mode on the Pulsar listener:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar", ackMode = AckMode.RECORD)
public void listen(String message) {
    System.out.println("Message Received: " + message);
}
```

<a id="reference-pulsar-message-consumption--_manual_message_ack_in_single_record_mode"></a>
<a id="reference-pulsar-message-consumption--6.3.-manual-message-ack-in-single-record-mode"></a>

### 6.3. Manual Message Ack in Single Record Mode

You might not always want the framework to send acknowledgments but, rather, do that directly from the application itself.
Spring for Apache Pulsar provides a couple of ways to enable manual message acknowledgments. The following example shows one of them:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar", ackMode = AckMode.MANUAL)
public void listen(Message<String> message, Acknowledgment acknowledgment) {
    System.out.println("Message Received: " + message.getValue());
	acknowledgment.acknowledge();
}
```

A few things merit explanation here. First, we enablE manual ack mode by setting `ackMode` on `PulsarListener`.
When enabling manual ack mode, Spring for Apache Pulsar lets the application inject an `Acknowledgment` object.
The framework achieves this by selecting a compatible message listener container: `PulsarAcknowledgingMessageListener` for single record based consumption, which gives you access to an `Acknowledgment` object.

The `Acknowledgment` object provides the following API methods:

```java
void acknowledge();

void acknowledge(MessageId messageId);

void acknowledge(List<MessageId> messageIds);

void nack();

void nack(MessageId messageId);
```

You can inject this `Acknowledgment` object into your `PulsarListener` while using `MANUAL` ack mode and then call one of the corresponding methods.

In the preceding `PulsarListener` example, we call a parameter-less `acknowledge` method.
This is because the framework knows which `Message` it is currently operating under.
When calling `acknowledge()`, you need not receive the payload with the `Message` enveloper` but, rather, use the target type — `String`, in this example.
You can also call a different variant of `acknowledge` by providing the message ID: `acknowledge.acknowledge(message.getMessageId());`
When you use `acknowledge(messageId)`, you must receive the payload by using the `Message<?>` envelope.

Similar to what is possible for acknowledging, the `Acknowledgment` API also provides options for negatively acknowledging.
See the nack methods shown earlier.

You can also call `acknowledge` directly on the Pulsar consumer:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar", ackMode = AckMode.MANUAL) public void listen(Message<String> message, Consumer<String> consumer) {System.out.println("Message Received: " + message.getValue()); try {consumer.acknowledge(message);} catch (Exception e) {....}}
```

When calling `acknowledge` directly on the underlying consumer, you need to do error handling by yourself.
Using the `Acknowledgment` does not require that, as the framework can do that for you.
Therefore, you should use the `Acknowledgment` object approach when using manual acknowledgment.

> [!IMPORTANT]
> When using manual acknowledgment, it is important to understand that the framework completely stays from any acknowledgment at all.
> Hence, it is extremely important to think through the right acknowledgment strategies when designing applications.

<a id="reference-pulsar-message-consumption--_automatic_message_ack_in_batch_consumption"></a>
<a id="reference-pulsar-message-consumption--6.4.-automatic-message-ack-in-batch-consumption"></a>

### 6.4. Automatic Message Ack in Batch Consumption

When you consume records in batches (see “[Message ACK modes](#reference-pulsar-message-consumption--message-ack-modes)”) and you use the default ack mode of `BATCH` is used, when the entire batch is processed successfully, the entire batch is acknowledged.
If any records throw an exception, the entire batch is negatively acknowledged.
Note that this may not be the same batch that was batched on the producer side. Rather, this is the batch that returned from calling `batchReceive` on the consumer

Consider the following batch listener:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar", batch = true)
public void batchListen(List<Foo> messages) {
    for (Foo foo : messages) {
		...
    }
}
```

When all the messages in the incoming collection (`messages` in this example) are processed, the framework acknowledges all of them.

When consuming in batch mode, `RECORD` is not an allowed ack mode.
This might cause an issue, as an application may not want the entire batch to be re-delivered again.
In such situations, you need to use the `MANUAL` acknowledgement mode.

<a id="reference-pulsar-message-consumption--_manual_message_ack_in_batch_consumption"></a>
<a id="reference-pulsar-message-consumption--6.5.-manual-message-ack-in-batch-consumption"></a>

### 6.5. Manual Message Ack in Batch Consumption

As seen in the previous section, when `MANUAL` ack mode is set on the message listener container, the framework does not do any acknowledgment, positive or negative.
It is entirely up to the application to take care of such concerns.
When `MANUAL` ack mode is set, Spring for Apache Pulsar selects a compatible message listener container: `PulsarBatchAcknowledgingMessageListener` for batch consumption, which gives you access to an `Acknowledgment` object.
The following are the methods available in the `Acknowledgment` API:

```java
void acknowledge();

void acknowledge(MessageId messageId);

void acknowledge(List<MessageId> messageIds);

void nack();

void nack(MessageId messageId);
```

You can inject this `Acknowledgment` object into your `PulsarListener` while using `MANUAL` ack mode.
The following listing shows a basic example for a batch based listener:

```java
@PulsarListener(subscriptionName = "hello-pulsar-subscription", topics = "hello-pulsar") public void listen(List<Message<String>> messgaes, Acknowlegement acknowledgment) {for (Message<String> message : messages) {try {...acknowledgment.acknowledge(message.getMessageId());} catch (Exception e) {acknowledgment.nack(message.getMessageId());}}}
```

When you use a batch listener, the message listener container cannot know which record it is currently operating upon.
Therefore, to manually acknowledge, you need to use one of the overloaded `acknowledge` method that takes a `MessageId` or a `List<MessageId>`.
You can also negatively acknowledge with the `MessageId` for the batch listener.

<a id="reference-pulsar-message-consumption--_message_redelivery_and_error_handling"></a>
<a id="reference-pulsar-message-consumption--7.-message-redelivery-and-error-handling"></a>

## 7. Message Redelivery and Error Handling

Now that we have seen both `PulsarListener` and the message listener container infrastructure and its various functions, let us now try to understand message redelivery and error handling.
Apache Pulsar provides various native strategies for message redelivery and error handling. We take a look at them and see how we can use them through Spring for Apache Pulsar.

<a id="reference-pulsar-message-consumption--_specifying_acknowledgment_timeout_for_message_redelivery"></a>
<a id="reference-pulsar-message-consumption--7.1.-specifying-acknowledgment-timeout-for-message-redelivery"></a>

### 7.1. Specifying Acknowledgment Timeout for Message Redelivery

By default, Pulsar consumers do not redeliver messages unless the consumer crashes, but you can change this behavior by setting an ack timeout on the Pulsar consumer.
If the ack timeout property has a value above zero and if the Pulsar consumer does not acknowledge a message within that timeout period, the message is redelivered.

When you use Spring for Apache Pulsar, you can set this property via a [consumer customizer](#reference-pulsar-message-consumption--_consumer_customization_on_pulsarlistener) or with the native Pulsar `ackTimeoutMillis` property in the `properties` attribute of `@PulsarListener`:

```java
@PulsarListener(subscriptionName = "subscription-1", topics = "topic-1"
                properties = {"ackTimeoutMillis=60000"})
public void listen(String s) {
    ...
}
```

When you specify the ack timeout, if the consumer does not send an acknowledgement within 60 seconds, the message is redelivered by Pulsar to the consumer.

If you want to specify some advanced backoff options for ack timeout with different delays, you can do the following:

```java
@EnablePulsar
@Configuration
class AckTimeoutRedeliveryConfig {

    @PulsarListener(subscriptionName = "withAckTimeoutRedeliveryBackoffSubscription",
            topics = "withAckTimeoutRedeliveryBackoff-test-topic",
            ackTimeoutRedeliveryBackoff = "ackTimeoutRedeliveryBackoff",
            properties = { "ackTimeoutMillis=60000" })
    void listen(String msg) {
        // some long-running process that may cause an ack timeout
    }

    @Bean
    RedeliveryBackoff ackTimeoutRedeliveryBackoff() {
        return MultiplierRedeliveryBackoff.builder().minDelayMs(1000).maxDelayMs(10 * 1000).multiplier(2)
                .build();
    }

}
```

In the preceding example, we specify a bean for Pulsar’s `RedeliveryBackoff` with a minimum delay of 1 second, a maximum delay of 10 seconds, and a backoff multiplier of 2.
After the initial ack timeout occurs, the message redeliveries are controlled through this backoff bean.
We provide the backoff bean to the `PulsarListener` annotation by setting the `ackTimeoutRedeliveryBackoff` property to the actual bean name — `ackTimeoutRedeliveryBackoff`, in this case.

<a id="reference-pulsar-message-consumption--_specifying_negative_acknowledgment_redelivery"></a>
<a id="reference-pulsar-message-consumption--7.2.-specifying-negative-acknowledgment-redelivery"></a>

### 7.2. Specifying Negative Acknowledgment Redelivery

When acknowledging negatively, Pulsar consumer lets you specify how the application wants the message to be re-delivered.
The default is to redeliver the message in one minute, but you can change it via a [consumer customizer](#reference-pulsar-message-consumption--_consumer_customization_on_pulsarlistener) or with the native Pulsar `negativeAckRedeliveryDelay` property in the `properties` attribute of `@PulsarListener`:

```java
@PulsarListener(subscriptionName = "subscription-1", topics = "topic-1"
                properties = {"negativeAckRedeliveryDelay=10ms"})
public void listen(String s) {
    ...
}
```

You can also specify different delays and backoff mechanisms with a multiplier by providing a `RedeliveryBackoff` bean and providing the bean name as the `negativeAckRedeliveryBackoff` property on the PulsarProducer, as follows:

```java
@EnablePulsar
@Configuration
class NegativeAckRedeliveryConfig {

    @PulsarListener(subscriptionName = "withNegRedeliveryBackoffSubscription",
            topics = "withNegRedeliveryBackoff-test-topic", negativeAckRedeliveryBackoff = "redeliveryBackoff",
            subscriptionType = SubscriptionType.Shared)
    void listen(String msg) {
        throw new RuntimeException("fail " + msg);
    }

    @Bean
    RedeliveryBackoff redeliveryBackoff() {
        return MultiplierRedeliveryBackoff.builder().minDelayMs(1000).maxDelayMs(10 * 1000).multiplier(2)
                .build();
    }

}
```

<a id="reference-pulsar-message-consumption--_using_dead_letter_topic_from_apache_pulsar_for_message_redelivery_and_error_handling"></a>
<a id="reference-pulsar-message-consumption--7.3.-using-dead-letter-topic-from-apache-pulsar-for-message-redelivery-and-error-handling"></a>

### 7.3. Using Dead Letter Topic from Apache Pulsar for Message Redelivery and Error Handling

Apache Pulsar lets applications use a dead letter topic on consumers with a `Shared` subscription type.
For the `Exclusive` and `Failover` subscription types, this feature is not available.
The basic idea is that, if a message is retried a certain number of times (maybe due to an ack timeout or nack redelivery), once the number of retries are exhausted, the message can be sent to a special topic called the dead letter queue (DLQ).
Let us see some details around this feature in action by inspecting some code snippets:

```java
@EnablePulsar @Configuration class DeadLetterPolicyConfig {
@PulsarListener(id = "deadLetterPolicyListener", subscriptionName = "deadLetterPolicySubscription",topics = "topic-with-dlp", deadLetterPolicy = "deadLetterPolicy",subscriptionType = SubscriptionType.Shared, properties = { "ackTimeoutMillis=1000" }) void listen(String msg) {throw new RuntimeException("fail " + msg);}
@PulsarListener(id = "dlqListener", topics = "my-dlq-topic") void listenDlq(String msg) {System.out.println("From DLQ: " + msg);}
@Bean DeadLetterPolicy deadLetterPolicy() {return DeadLetterPolicy.builder().maxRedeliverCount(10).deadLetterTopic("my-dlq-topic").build();}
}
```

First, we have a special bean for `DeadLetterPolicy`, and it is named as `deadLetterPolicy` (it can be any name as you wish).
This bean specifies a number of things, such as the max delivery (10, in this case) and the name of the dead letter topic — `my-dlq-topic`, in this case.
If you do not specify a DLQ topic name, it defaults to `<topicname>-<subscriptionname>-DLQ` in Pulsar.
Next, we provide this bean name to `PulsarListener` by setting the `deadLetterPolicy` property.
Note that the `PulsarListener` has a subscription type of `Shared`, as the DLQ feature only works with shared subscriptions.
This code is primarily for demonstration purposes, so we provide an `ackTimeoutMillis` value of 1000.
The idea is that the code throws the exception and, if Pulsar does not receive an ack within 1 second, it does a retry.
If that cycle continues ten times (as that is our max redelivery count in the `DeadLetterPolicy`), the Pulsar consumer publishes the messages to the DLQ topic.
We have another `PulsarListener` that listens on the DLQ topic to receive data as it is published to the DLQ topic.

<a id="reference-pulsar-message-consumption--_native_error_handling_in_spring_for_apache_pulsar"></a>
<a id="reference-pulsar-message-consumption--7.4.-native-error-handling-in-spring-for-apache-pulsar"></a>

### 7.4. Native Error Handling in Spring for Apache Pulsar

As we noted earlier, the DLQ feature in Apache Pulsar works only for shared subscriptions.
What does an application do if it needs to use some similar feature for non-shared subscriptions?
The main reason Pulsar does not support DLQ on exclusive and failover subscriptions is because those subscription types are order-guaranteed.
Allowing redeliveries, DLQ, and so on effectively receives messages out of order.
However, what if an application are okay with that but, more importantly, needs this DLQ feature for non-shared subscriptions?
For that, Spring for Apache Pulsar provides a `PulsarConsumerErrorHandler`, which you can use across any subscription types in Pulsar: `Exclusive`, `Failover`, `Shared`, or `Key_Shared`.

When you use `PulsarConsumerErrorHandler` from Spring for Apache Pulsar, make sure not to set the ack timeout properties on the listener.

Let us see some details by examining a few code snippets:

```java
@EnablePulsar
@Configuration
class PulsarConsumerErrorHandlerConfig {

    @Bean
    PulsarConsumerErrorHandler<String> pulsarConsumerErrorHandler(
            PulsarTemplate<String> pulsarTemplate) {
        return new DefaultPulsarConsumerErrorHandler<>(
                new PulsarDeadLetterPublishingRecoverer<>(pulsarTemplate, (c, m) -> "my-foo-dlt"), new FixedBackOff(100, 10));
    }

    @PulsarListener(id = "pulsarConsumerErrorHandler-id", subscriptionName = "pulsatConsumerErrorHandler-subscription",
                    topics = "pulsarConsumerErrorHandler-topic",
					pulsarConsumerErrorHandler = "pulsarConsumerErrorHandler")
    void listen(String msg) {
        throw new RuntimeException("fail " + msg);
    }

    @PulsarListener(id = "pceh-dltListener", topics = "my-foo-dlt")
    void listenDlt(String msg) {
        System.out.println("From DLT: " + msg);
    }

}
```

Consider the `pulsarConsumerErrorHandler` bean.
This creates a bean of type `PulsarConsumerErrorHandler` and uses the default implementation provided out of the box by Spring for Apache Pulsar: `DefaultPulsarConsumerErrorHandler`.
`DefaultPulsarConsumerErrorHandler` has a constructor that takes a `PulsarMessageRecovererFactory` and a `org.springframework.util.backoff.Backoff`.
`PulsarMessageRecovererFactory` is a functional interface with the following API:

```java
@FunctionalInterface public interface PulsarMessageRecovererFactory<T> {
/** * Provides a message recoverer {@link PulsarMessageRecoverer}.* @param consumer Pulsar consumer * @return {@link PulsarMessageRecoverer}.*/ PulsarMessageRecoverer<T> recovererForConsumer(Consumer<T> consumer);
}
```

The `recovererForConsumer` method takes a Pulsar consumer and returns a `PulsarMessageRecoverer`, which is another functional interface.
Here is the API of `PulsarMessageRecoverer`:

```java
public interface PulsarMessageRecoverer<T> {
/** * Recover a failed message, for e.g. send the message to a DLT.* @param message Pulsar message * @param exception exception from failed message */ void recoverMessage(Message<T> message, Exception exception);
}
```

Spring for Apache Pulsar provides an implementation for `PulsarMessageRecovererFactory` called `PulsarDeadLetterPublishingRecoverer` that provides a default implementation that can recover the message by sending it to a Dead Letter Topic (DLT).
We provide this implementation to the constructor for the preceding `DefaultPulsarConsumerErrorHandler`.
As the second argument, we provide a `FixedBackOff`.
You can also provide the `ExponentialBackoff` from Spring for advanced backoff features.
Then we provide this bean name for the `PulsarConsumerErrorHandler` as a property to the `PulsarListener`.
The property is called `pulsarConsumerErrorHandler`.
Each time the `PulsarListener` method fails for a message, it gets retried.
The number of retries are controlled by the `Backoff` provided implementation values. In our example, we do 10 retries (11 total tries — the first one and then the 10 retries).
Once all the retries are exhausted, the message is sent to the DLT topic.

The `PulsarDeadLetterPublishingRecoverer` implementation we provide uses a `PulsarTemplate` that is used for publishing the message to the DLT.
In most cases, the same auto-configured `PulsarTemplate` from Spring Boot is sufficient with the caveat for partitioned topics.
When using partitioned topics and using custom message routing for the main topic, you must use a different `PulsarTemplate` that does not take the auto-configured `PulsarProducerFactory` that is populated with a value of `custompartition` for `message-routing-mode`.
You can use a `PulsarConsumerErrorHandler` with the following blueprint:

```java
@Bean
PulsarConsumerErrorHandler<Integer> pulsarConsumerErrorHandler(PulsarClient pulsarClient) {
    PulsarProducerFactory<Integer> pulsarProducerFactory = new DefaultPulsarProducerFactory<>(pulsarClient, Map.of());
        PulsarTemplate<Integer> pulsarTemplate = new PulsarTemplate<>(pulsarProducerFactory);

        BiFunction<Consumer<?>, Message<?>, String> destinationResolver =
                (c, m) -> "my-foo-dlt";

        PulsarDeadLetterPublishingRecoverer<Integer> pulsarDeadLetterPublishingRecoverer =
                new PulsarDeadLetterPublishingRecoverer<>(pulsarTemplate, destinationResolver);

        return new DefaultPulsarConsumerErrorHandler<>(pulsarDeadLetterPublishingRecoverer,
                new FixedBackOff(100, 5));
}
```

Note that we are provide a destination resolver to the `PulsarDeadLetterPublishingRecoverer` as the second constructor argument.
If not provided, `PulsarDeadLetterPublishingRecoverer` uses `<subscription-name>-<topic-name>-DLT>` as the DLT topic name.
When using this feature, you should use a proper destination name by setting the destination resolver rather than using the default.

When using a single record message listener, as we did with `PulsarConsumerErrorHnadler`, and if you use manual acknowledgement, make sure to not negatively acknowledge the message when an exception is thrown.
Rather, re-throw the exception back to the container. Otherwise, the container thinks the message is handled separately, and the error handling is not triggered.

Finally, we have a second `PulsarListener` that receives messages from the DLT topic.

In the examples provided in this section so far, we only saw how to use `PulsarConsumerErrorHandler` with a single record message listener.
Next, we look at how you can use this on batch listeners.

<a id="reference-pulsar-message-consumption--_batch_listener_with_pulsarconsumererrorhandler"></a>
<a id="reference-pulsar-message-consumption--7.5.-batch-listener-with-pulsarconsumererrorhandler"></a>

### 7.5. Batch listener with PulsarConsumerErrorHandler

First, let us look at a batch `PulsarListener` method:

```java
@PulsarListener(subscriptionName = "batch-demo-5-sub", topics = "batch-demo-4", batch = true, concurrency = "3",subscriptionType = SubscriptionType.Failover,pulsarConsumerErrorHandler = "pulsarConsumerErrorHandler", ackMode = AckMode.MANUAL) void listen(List<Message<Integer>> data, Consumer<Integer> consumer, Acknowledgment acknowledgment) {for (Message<Integer> datum : data) {if (datum.getValue() == 5) {throw new PulsarBatchListenerFailedException("failed", datum);} acknowledgement.acknowledge(datum.getMessageId());}}
@Bean PulsarConsumerErrorHandler<String> pulsarConsumerErrorHandler(PulsarTemplate<String> pulsarTemplate) {return new DefaultPulsarConsumerErrorHandler<>(new PulsarDeadLetterPublishingRecoverer<>(pulsarTemplate, (c, m) -> "my-foo-dlt"), new FixedBackOff(100, 10));}
@PulsarListener(subscriptionName = "my-dlt-subscription", topics = "my-foo-dlt") void dltReceiver(Message<Integer> message) {System.out.println("DLT - RECEIVED: " + message.getValue());}
```

Once again, we provide the `pulsarConsumerErrorHandler` property with the `PulsarConsumerErrorHandler` bean name.
When you use a batch listener (as shown in the preceding example) and want to use the `PulsarConsumerErrorHandler` from Spring for Apache Pulsar, you need to use manual acknowledgment.
This way, you can acknowledge all the successful individual messages.
For the ones that fail, you must throw a `PulsarBatchListenerFailedException` with the message on which it fails.
Without this exception, the framework does not know what to do with the failure.
On retry, the container sends a new batch of messages, starting with the failed message to the listener.
If it fails again, it is retried, until the retries are exhausted, at which point the message is sent to the DLT.
At that point, the message is acknowledged by the container, and the listener is handed over with the subsequent messages in the original batch.

<a id="reference-pulsar-message-consumption--_consumer_customization_on_pulsarlistener"></a>
<a id="reference-pulsar-message-consumption--8.-consumer-customization-on-pulsarlistener"></a>

## 8. Consumer Customization on PulsarListener

Spring for Apache Pulsar provides a convenient way to customize the consumer created by the container used by the `PulsarListener`.
Applications can provide a bean for `PulsarListenerConsumerBuilderCustomizer`.
Here is an example.

```java
@Bean
public PulsarListenerConsumerBuilderCustomizer<String> myCustomizer() {
    return cb -> {
        cb.subscriptionName("modified-subscription-name");
    };
}
```

Then this customizer bean name can be provided as an attribute on the `PuslarListener` annotation as shown below.

```java
@PulsarListener(subscriptionName = "my-subscription",
        topics = "my-topic", consumerCustomizer = "myCustomizer")
void listen(String message) {

}
```

The framework detects the provided bean through the `PulsarListener` and applies this customizer on the Consumer builder before creating the Pulsar Consumer.

If you have multiple `PulsarListener` methods, and each of them have different customization rules, you should create multiple customizer beans and attach the proper customizers on each `PulsarListener`.

<a id="reference-pulsar-message-consumption--message-listener-lifecycle"></a>
<a id="reference-pulsar-message-consumption--9.-message-listener-container-lifecycle"></a>

## 9. Message Listener Container Lifecycle

<a id="reference-pulsar-message-consumption--message-listener-pause-resume"></a>
<a id="reference-pulsar-message-consumption--9.1.-pausing-and-resuming"></a>

### 9.1. Pausing and Resuming

There are situations in which an application might want to pause message consumption temporarily and then resume later.
Spring for Apache Pulsar provides the ability to pause and resume the underlying message listener containers.
When the Pulsar message listener container is paused, any polling done by the container to receive data from the Pulsar consumer will be paused.
Similarly, when the container is resumed, the next poll starts returning data if the topic has any new records added while paused.

To pause or resume a listener container, first obtain the container instance via the `PulsarListenerEndpointRegistry` bean and then invoke the pause/resume API on the container instance - as shown in the snippet below:

```java
@Autowired
private PulsarListenerEndpointRegistry registry;

void someMethod() {
  PulsarMessageListenerContainer container = registry.getListenerContainer("my-listener-id");
  container.pause();
}
```

> [!TIP]
> The id parameter passed to `getListenerContainer` is the container id - which will be the value of the `@PulsarListener` id attribute when pausing/resuming a `@PulsarListener`.

<a id="reference-pulsar-message-consumption--message-listener-startup-failure"></a>
<a id="reference-pulsar-message-consumption--9.2.-handling-startup-failures"></a>

### 9.2. Handling Startup Failures

Message listener containers are started when the application context is refreshed.
By default, any failures encountered during startup are re-thrown and the application will fail to start.
You can adjust this behavior with the `StartupFailurePolicy` on the corresponding container properties.

The available options are:

- `Stop` (default) - log and re-throw the exception, effectively stopping the application
- `Continue` - log the exception, leave the container in a non-running state, but do not stop the application
- `Retry` - log the exception, retry to start the container asynchronously, but do not stop the application.

The default retry behavior is to retry 3 times with a 10-second delay between
each attempt.
However, a custom retry template can be specified on the corresponding container properties.
If the container fails to restart after the retries are exhausted, it is left in a non-running state.

<a id="reference-pulsar-message-consumption--_configuration"></a>
<a id="reference-pulsar-message-consumption--9.2.1.-configuration"></a>

#### 9.2.1. Configuration

<a id="reference-pulsar-message-consumption--_with_spring_boot"></a>
<a id="reference-pulsar-message-consumption--with-spring-boot"></a>

##### With Spring Boot

When using Spring Boot you can register a `PulsarContainerFactoryCustomizer<ConcurrentPulsarListenerContainerFactory<?>>` bean that sets the container startup properties.

<a id="reference-pulsar-message-consumption--_without_spring_boot"></a>
<a id="reference-pulsar-message-consumption--without-spring-boot"></a>

##### Without Spring Boot

However, if you are instead manually configuring the components, you will have to update the container startup properties accordingly when constructing the message listener container factory.

<a id="reference-pulsar-message-consumption--imperative-pulsar-reader"></a>
<a id="reference-pulsar-message-consumption--10.-pulsar-reader-support"></a>

## 10. Pulsar Reader Support

The framework provides support for using [Pulsar Reader](https://pulsar.apache.org/docs/4.2.x/concepts-clients/#reader-interface) via the `PulsarReaderFactory`.

Spring Boot provides this reader factory which you can further configure by specifying any of the [`spring.pulsar.reader.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

<a id="reference-pulsar-message-consumption--_pulsarreader_annotation"></a>
<a id="reference-pulsar-message-consumption--10.1.-pulsarreader-annotation"></a>

### 10.1. PulsarReader Annotation

While it is possible to use `PulsarReaderFactory` directly, Spring for Apache Pulsar provides the `PulsarReader` annotation that you can use to quickly read from a topic without setting up any reader factories yourselves.
This is similar to the same ideas behind `PulsarListener.`
Here is a quick example.

```java
@PulsarReader(id = "reader-demo-id", topics = "reader-demo-topic", startMessageId = "earliest")
void read(String message) {
    //...
}
```

The `id` attribute is optional, but it is a best practice to provide a value that is meaningful to your application.
When not specified an auto-generated id will be used.
On the other hand, the `topics` and `startMessageId` attributes are mandatory.
The `topics` attribute can be a single topic or a comma-separated list of topics.
The `startMessageId` attribute instructs the reader to start from a particular message in the topic.
The valid values for `startMessageId` are `earliest` or `latest.`
Suppose you want the reader to start reading messages arbitrarily from a topic other than the earliest or latest available messages. In that case, you need to use a `ReaderBuilderCustomizer` to customize the `ReaderBuilder` so it knows the right `MessageId` to start from.

<a id="reference-pulsar-message-consumption--_customizing_the_readerbuilder"></a>
<a id="reference-pulsar-message-consumption--10.2.-customizing-the-readerbuilder"></a>

### 10.2. Customizing the ReaderBuilder

You can customize any fields available through `ReaderBuilder` using a `PulsarReaderReaderBuilderCustomizer` in Spring for Apache Pulsar.
You can provide a `@Bean` of type `PulsarReaderReaderBuilderCustomizer` and then make it available to the `PulsarReader` as below.

```java
@PulsarReader(id = "reader-customizer-demo-id", topics = "reader-customizer-demo-topic",readerCustomizer = "myCustomizer") void read(String message) {//...}
@Bean public PulsarReaderReaderBuilderCustomizer<String> myCustomizer() {return readerBuilder -> {readerBuilder.startMessageId(messageId); // the first message read is after this message id.// Any other customizations on the readerBuilder };}
```

> [!TIP]
> If your application only has a single `@PulsarReader` and a single `PulsarReaderReaderBuilderCustomizer` bean registered then the customizer will be automatically applied.

<a id="reference-pulsar-message-consumption--message-reader-startup-failure"></a>
<a id="reference-pulsar-message-consumption--10.3.-handling-startup-failures"></a>

### 10.3. Handling Startup Failures

Message listener containers are started when the application context is refreshed.
By default, any failures encountered during startup are re-thrown and the application will fail to start.
You can adjust this behavior with the `StartupFailurePolicy` on the corresponding container properties.

The available options are:

- `Stop` (default) - log and re-throw the exception, effectively stopping the application
- `Continue` - log the exception, leave the container in a non-running state, but do not stop the application
- `Retry` - log the exception, retry to start the container asynchronously, but do not stop the application.

The default retry behavior is to retry 3 times with a 10-second delay between
each attempt.
However, a custom retry template can be specified on the corresponding container properties.
If the container fails to restart after the retries are exhausted, it is left in a non-running state.

<a id="reference-pulsar-message-consumption--_configuration_2"></a>
<a id="reference-pulsar-message-consumption--10.3.1.-configuration"></a>

#### 10.3.1. Configuration

<a id="reference-pulsar-message-consumption--_with_spring_boot_2"></a>
<a id="reference-pulsar-message-consumption--with-spring-boot-2"></a>

##### With Spring Boot

When using Spring Boot you can register a `PulsarContainerFactoryCustomizer<DefaultPulsarReaderContainerFactory<?>>` bean that sets the container startup properties.

<a id="reference-pulsar-message-consumption--_without_spring_boot_2"></a>
<a id="reference-pulsar-message-consumption--without-spring-boot-2"></a>

##### Without Spring Boot

However, if you are instead manually configuring the components, you will have to update the container startup properties accordingly when constructing the message listener container factory.

---

<a id="reference-pulsar-publishing-consuming-partitioned-topics"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar/publishing-consuming-partitioned-topics.html -->

<!-- page_index: 13 -->

# Publishing and Consuming Partitioned Topics

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-publishing-consuming-partitioned-topics--page-title"></a>
<a id="reference-pulsar-publishing-consuming-partitioned-topics--publishing-and-consuming-partitioned-topics"></a>

# Publishing and Consuming Partitioned Topics

In the following example, we publish to a topic called `hello-pulsar-partitioned`.
It is a topic that is partitioned, and, for this sample, we assume that the topic is already created with three partitions.

```java
@SpringBootApplication public class PulsarBootPartitioned {
public static void main(String[] args) {SpringApplication.run(PulsarBootPartitioned.class, "--spring.pulsar.producer.message-routing-mode=CustomPartition");}
@Bean public ApplicationRunner runner(PulsarTemplate<String> pulsarTemplate) {pulsarTemplate.setDefaultTopicName("hello-pulsar-partitioned"); return args -> {for (int i = 0; i < 10; i++) {pulsarTemplate.sendAsync("hello john doe 0 ", new FooRouter()); pulsarTemplate.sendAsync("hello alice doe 1", new BarRouter()); pulsarTemplate.sendAsync("hello buzz doe 2", new BuzzRouter());} };}
@PulsarListener(subscriptionName = "hello-pulsar-partitioned-subscription", topics = "hello-pulsar-partitioned") public void listen(String message) {System.out.println("Message Received: " + message);}
static class FooRouter implements MessageRouter {
@Override public int choosePartition(Message<?> msg, TopicMetadata metadata) {return 0;}}
static class BarRouter implements MessageRouter {
@Override public int choosePartition(Message<?> msg, TopicMetadata metadata) {return 1;}}
static class BuzzRouter implements MessageRouter {
@Override public int choosePartition(Message<?> msg, TopicMetadata metadata) {return 2;}}
}
```

In the preceding example, we publish to a partitioned topic, and we would like to publish some data segment to a specific partition.
If you leave it to Pulsar’s default, it follows a round-robin mode of partition assignments, and we would like to override that.
To do so, we provide a message router object with the `send` method.
Consider the three message routers implemented.
`FooRouter` always sends data to partition `0`, `BarRouter` sends to partition `1`, and `BuzzRouter` sends to partition `2`.
Also note that we now use the `sendAsync` method of `PulsarTemplate` that returns a `CompletableFuture`.
When running the application, we also need to set the `messageRoutingMode` on the producer to `CustomPartition` (`spring.pulsar.producer.message-routing-mode`).

On the consumer side, we use a `PulsarListener` with the exclusive subscription type.
This means that data from all the partitions ends up in the same consumer and there is no ordering guarantee.

What can we do if we want each partition to be consumed by a single distinct consumer?
We can switch to the `failover` subscription mode and add three separate consumers:

```java
@PulsarListener(subscriptionName = "hello-pulsar-partitioned-subscription", topics = "hello-pulsar-partitioned", subscriptionType = SubscriptionType.Failover) public void listen1(String foo) {System.out.println("Message Received 1: " + foo);}
@PulsarListener(subscriptionName = "hello-pulsar-partitioned-subscription", topics = "hello-pulsar-partitioned", subscriptionType = SubscriptionType.Failover) public void listen2(String foo) {System.out.println("Message Received 2: " + foo);}
@PulsarListener(subscriptionName = "hello-pulsar-partitioned-subscription",  topics = "hello-pulsar-partitioned", subscriptionType = SubscriptionType.Failover) public void listen3(String foo) {System.out.println("Message Received 3: " + foo);}
```

When you follow this approach, a single partition always gets consumed by a dedicated consumer.

In a similar vein, if you want to use Pulsar’s shared consumer type, you can use the `shared` subscription type.
However, when you use the `shared` mode, you lose any ordering guarantees, as a single consumer may receive messages from all the partitions before another consumer gets a chance.

Consider the following example:

```java
@PulsarListener(subscriptionName = "hello-pulsar-shared-subscription", topics = "hello-pulsar-partitioned", subscriptionType = SubscriptionType.Shared) public void listen1(String foo) {System.out.println("Message Received 1: " + foo);}
@PulsarListener(subscriptionName = "hello-pulsar-shared-subscription", topics = "hello-pulsar-partitioned", subscriptionType = SubscriptionType.Shared) public void listen2(String foo) {System.out.println("Message Received 2: " + foo);}
```

---

<a id="reference-pulsar-transactions"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar/transactions.html -->

<!-- page_index: 14 -->

# Transactions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-transactions--page-title"></a>
<a id="reference-pulsar-transactions--transactions"></a>

# Transactions

This section describes how Spring for Apache Pulsar supports transactions.

<a id="reference-pulsar-transactions--overview"></a>

## Overview

Spring for Apache Pulsar transaction support is built upon the [transaction support](https://docs.spring.io/spring-framework/reference/data-access/transaction.html) provided by Spring Framework.
At a high-level, transactional resources are registered with a transaction manager which in turn handles the transactional state (commit, rollback, etc..) of the registered resources.

Spring for Apache Pulsar provides the following:

- `PulsarTransactionManager` - used with normal Spring transaction support (`@Transactional`, `TransactionTemplate`, etc)
- Transactional `PulsarTemplate`
- Transactional `@PulsarListener`
- Transaction synchronization with other transaction managers

Transaction support is disabled by default.
To enable support when using Spring Boot, simply set the `spring.pulsar.transaction.enabled` property.
Further configuration options are outlined in each component section below.

<a id="reference-pulsar-transactions--_transactional_publishing_with_pulsartemplate"></a>
<a id="reference-pulsar-transactions--transactional-publishing-with-pulsartemplate"></a>

## Transactional Publishing with `PulsarTemplate`

All send operations on a transactional `PulsarTemplate` look for an active transaction and enlist each send operation in the transaction (if one is found).

<a id="reference-pulsar-transactions--_non_transactional_use"></a>
<a id="reference-pulsar-transactions--non-transactional-use"></a>

### Non-transactional use

By default, a transactional `PulsarTemplate` can also be used for non-transactional operations.
When an existing transaction is not found it will continue the send operation in a non-transactional fashion.
However, if the template is configured to require transactions then any attempt to use the template outside the scope of a transaction results in an exception.

> [!TIP]
> A transaction can be started by a `TransactionTemplate`, a `@Transactional` method, calling `executeInTransaction`, or by a transactional listener container.

<a id="reference-pulsar-transactions--_local_transactions"></a>
<a id="reference-pulsar-transactions--local-transactions"></a>

### Local Transactions

We use the term "local" transaction to denote a Pulsar native transaction that is **not managed** by or associated with Spring’s transaction management facility (i.e. `PulsarTransactionManager`).
Conversely, a "synchronized" transaction is one that **is managed** by or associated with the `PulsarTransactionManager`.

You can use the `PulsarTemplate` to execute a series of operations within a local transaction.
The following example shows how to do so:

```java
var results = pulsarTemplate.executeInTransaction((template) -> {
    var rv = new HashMap<String, MessageId>();
    rv.put("msg1", template.send(topic, "msg1"));
    rv.put("msg2", template.send(topic, "msg2"));
    return rv;
});
```

The argument in the callback is the template instance that the `executeInTransaction` method was invoked on.
All operations on the template are enlisted in the current transaction.
If the callback exits normally, the transaction is committed.
If an exception is thrown, the transaction is rolled back.

> [!NOTE]
> If there is a synchronized transaction in process, it is ignored and a new "nested" transaction is used.

<a id="reference-pulsar-transactions--_configuration"></a>
<a id="reference-pulsar-transactions--configuration"></a>

### Configuration

The following transaction settings are available directly on the `PulsarTemplate` (via the `transactions` field):

- `enabled` - whether the template supports transactions (default `false`)
- `required` - whether the template requires transactions (default `false`)
- `timeout` - duration of the transaction timeout (default `null`)

When not using Spring Boot, you can adjust these settings on the template that you provide.
However, when using Spring Boot, the template is auto-configured and there is no mechanism to affect the properties.
In this case you can register a `PulsarTemplateCustomizer` bean that can be used to adjust the settings.
The following example shows how to set the timeout on the auto-configured template:

```java
@Bean
PulsarTemplateCustomizer<?> templateCustomizer() {
    return (template) -> template.transactions().setTimeout(Duration.ofSeconds(45));
}
```

<a id="reference-pulsar-transactions--_transactional_receiving_with_pulsarlistener"></a>
<a id="reference-pulsar-transactions--transactional-receiving-with-pulsarlistener"></a>

## Transactional Receiving with `@PulsarListener`

When listener transactions are enabled, the `@PulsarListener` annotated listener method is invoked in the scope of a synchronized transaction.

The `DefaultPulsarMessageListenerContainer` uses a Spring `TransactionTemplate` configured with a `PulsarTransactionManager` to initiate the transaction prior to method invocation.

The acknowledgment of each received message is enlisted in the scoped transaction.

<a id="reference-pulsar-transactions--_consume_process_produce_scenario"></a>
<a id="reference-pulsar-transactions--consume-process-produce-scenario"></a>

### Consume-Process-Produce Scenario

A common transactional pattern is where a consumer reads messages from a Pulsar topic, transforms the messages, and finally a producer writes the resulting messages to another Pulsar topic.
The framework supports this use case when transactions are enabled and your listener method uses a transactional `PulsarTemplate` to produce the transformed message.

Given the following listener method:

```java
@PulsarListener(topics = "my-input-topic") (1)
void listen(String msg) { (2)
    var transformedMsg = msg.toUpperCase(Locale.ROOT); (3)
    this.transactionalTemplate.send("my-output-topic", transformedMsg); (4)
} (5) (6)
```

The following interactions occur when listener transactions are enabled:

**1**

Listener container initiates new transaction and invokes listener method in scope of transaction

**2**

Listener method receives message

**3**

Listener method transforms message

**4**

Listener method sends transformed message with transactional template which enlists send operation in active transaction

**5**

Listener container auto-acks message and enlists ack operation in active transaction

**6**

Listener container (via `TransactionTemplate`) commits transaction

If you are not using `@PulsarListener` and instead using listener containers directly, the same transaction support is provided as described above.
Remember, the `@PulsarListener` is just a convenience to register a Java method as the listener container message listener.

<a id="reference-pulsar-transactions--_transactions_with_record_listeners"></a>
<a id="reference-pulsar-transactions--transactions-with-record-listeners"></a>

### Transactions with Record Listeners

The above example uses a record listener.
When using a record listener, a new transaction is created on every listener method invocation which equates to a transaction per message.

> [!NOTE]
> Because the transaction boundary is per message and each message acknowledgement is enlisted in each transaction, batch ack mode can not be used with transactional record listeners.

<a id="reference-pulsar-transactions--_transactions_with_batch_listeners"></a>
<a id="reference-pulsar-transactions--transactions-with-batch-listeners"></a>

### Transactions with Batch Listeners

When using a batch listener, a new transaction is created on every listener method invocation which equates to a transaction per batch of messages.

> [!NOTE]
> Transactional batch listeners do not currently support custom error handlers.

<a id="reference-pulsar-transactions--_configuration_2"></a>
<a id="reference-pulsar-transactions--configuration-2"></a>

### Configuration

<a id="reference-pulsar-transactions--_listener_container_factory"></a>
<a id="reference-pulsar-transactions--listener-container-factory"></a>

#### Listener container factory

The following transaction settings are available directly on the `PulsarContainerProperties` used by the `ConcurrentPulsarListenerContainerFactory` when creating listener containers.
These settings affect all listener containers, including the ones used by `@PulsarListener`.

- `enabled` - whether the container supports transactions (default `false`)
- `required` - whether the container requires transactions (default `false`)
- `timeout` - duration of the transaction timeout (default `null`)
- `transactionDefinition` - a blueprint transaction definition with properties that will be copied to the container’s transaction template (default `null`)
- `transactionManager` - the transaction manager used to start transactions

When not using Spring Boot, you can adjust these settings on the container factory that you provide.
However, when using Spring Boot, the container factory is auto-configured.
In this case you can register a `org.springframework.boot.pulsar.autoconfigure.PulsarContainerFactoryCustomizer<ConcurrentPulsarListenerContainerFactory<?>>` bean to access and customize the container properties.
The following example shows how to set the timeout on the container factory:

```java
@Bean
PulsarContainerFactoryCustomizer<ConcurrentPulsarListenerContainerFactory<?>> containerCustomizer() {
    return (containerFactory) -> containerFactory.getContainerProperties().transactions().setTimeout(Duration.ofSeconds(45));
}
```

<a id="reference-pulsar-transactions--_pulsarlistener"></a>
<a id="reference-pulsar-transactions--pulsarlistener"></a>

#### `@PulsarListener`

By default, each listener respects the transactional settings of its corresponding listener container factory.
However, the user can set the `transactional` attribute on each `@PulsarListener` to override the container factory setting as follows:

- If the container factory has transactions enabled then `transactional = false` will disable transactions for the indiviual listener.
- If the container factory has transactions enabled and required, then an attempt to set `transactional = false` will result in an exception being thrown stating that transactions are required.
- If the container factory has transactions disabled then an attempt to set `transactional = true` will be ignored and a warning will be logged.

<a id="reference-pulsar-transactions--_using_pulsartransactionmanager"></a>
<a id="reference-pulsar-transactions--using-pulsartransactionmanager"></a>

## Using `PulsarTransactionManager`

The `PulsarTransactionManager` is an implementation of Spring Framework’s `PlatformTransactionManager`.
You can use the `PulsarTransactionManager` with normal Spring transaction support (`@Transactional`, `TransactionTemplate`, and others).

If a transaction is active, any `PulsarTemplate` operations performed within the scope of the transaction enlist and participate in the ongoing transaction.
The manager commits or rolls back the transaction, depending on success or failure.

> [!TIP]
> You probably will not need to use `PulsarTransactionManager` directly since the majority of transactional use cases are covered by `PulsarTemplate` and `@PulsarListener`.

<a id="reference-pulsar-transactions--_pulsar_transactions_with_other_transaction_managers"></a>
<a id="reference-pulsar-transactions--pulsar-transactions-with-other-transaction-managers"></a>

## Pulsar Transactions with Other Transaction Managers

<a id="reference-pulsar-transactions--_producer_only_transaction"></a>
<a id="reference-pulsar-transactions--producer-only-transaction"></a>

### Producer-only transaction

If you want to send records to Pulsar and perform some database updates in a single transaction, you can use normal Spring transaction management with a `DataSourceTransactionManager`.

> [!NOTE]
> The following examples assume there is a `DataSourceTransactionManager` bean registered under the name "dataSourceTransactionManager"

```java
@Transactional("dataSourceTransactionManager")
public void myServiceMethod() {
    var msg = calculateMessage();
    this.pulsarTemplate.send("my-topic", msg);
    this.jdbcTemplate.execute("insert into my_table (data) values ('%s')".formatted(msg));
}
```

The interceptor for the `@Transactional` annotation starts the database transaction and the `PulsarTemplate` will synchronize a transaction with the DB transaction manager; each send will participate in that transaction.
When the method exits, the database transaction will commit followed by the Pulsar transaction.

If you wish to commit the Pulsar transaction first, and only commit the DB transaction if the Pulsar transaction is successful, use nested `@Transactional` methods, with the outer method configured to use the `DataSourceTransactionManager`, and the inner method configured to use the `PulsarTransactionManager`.

```java
@Transactional("dataSourceTransactionManager")
public void myServiceMethod() {
    var msg = calculateMessage();
    this.jdbcTemplate.execute("insert into my_table (data) values ('%s')".formatted(msg));
    this.sendToPulsar(msg);
}

@Transactional("pulsarTransactionManager")
public void sendToPulsar(String msg) {
    this.pulsarTemplate.send("my-topic", msg);
}
```

<a id="reference-pulsar-transactions--_consumer_producer_transaction"></a>
<a id="reference-pulsar-transactions--consumer-producer-transaction"></a>

### Consumer + Producer transaction

If you want to consume records from Pulsar, send records to Pulsar, and perform some database updates in a transaction, you can combine normal Spring transaction management (using a `DataSourceTransactionManager`) with container initiated transactions.

In the following example, the listener container starts the Pulsar transaction and the `@Transactional` annotation starts the DB transaction.
The DB transaction is committed first; if the Pulsar transaction fails to commit, the record will be redelivered so the DB update should be idempotent.

```java
@PulsarListener(topics = "my-input-topic")
@Transactional("dataSourceTransactionManager")
void listen(String msg) {
    var transformedMsg = msg.toUpperCase(Locale.ROOT);
    this.pulsarTemplate.send("my-output-topic", transformedMsg);
    this.jdbcTemplate.execute("insert into my_table (data) values ('%s')".formatted(transformedMsg));
}
```

---

<a id="reference-tombstones"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/tombstones.html -->

<!-- page_index: 15 -->

# Null Payloads and Log Compaction of 'Tombstone' Records

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-tombstones--page-title"></a>
<a id="reference-tombstones--null-payloads-and-log-compaction-of-tombstone-records"></a>

# Null Payloads and Log Compaction of 'Tombstone' Records

When using log compaction, you can send and receive messages with `null` payloads to identify the deletion of a key.
You can also receive `null` values for other reasons, such as a deserializer that might return `null` when it cannot deserialize a value.

<a id="reference-tombstones--tombstones.produce"></a>
<a id="reference-tombstones--producing-null-payloads"></a>

## Producing Null Payloads

To send a `null` payload by using the `PulsarTemplate`, you can use the fluent API and pass null into the value argument of the `newMessage()` method, for example:

```java
pulsarTemplate
        .newMessage(null)
        .withTopic("my-topic")
        .withSchema(Schema.STRING)
        .withMessageCustomizer((mb) -> mb.key("key:1234"))
        .send();
```

> [!NOTE]
> When sending null values you must specify the schema type as the system can not determine the type of the message from a `null` payload.

<a id="reference-tombstones--tombstones.consume"></a>
<a id="reference-tombstones--consuming-null-payloads"></a>

## Consuming Null Payloads

For `@PulsarListener` and `@PulsarReader`, the `null` payload is passed into the listener method based on the type of its message parameter as follows:

| Parameter type | Passed-in value |
| --- | --- |
| primitive | `null` |
| user-defined | `null` |
| `org.apache.pulsar.client.api.Message<T>` | non-null Pulsar message whose `getValue()` returns `null` |
| `org.springframework.messaging.Message<T>` | non-null Spring message whose `getPayload()` returns `PulsarNull` |
| `List<X>` | non-null list whose entries (`X`) are one of the above types and act accordingly (ie. primitive entries are `null` etc..) |
| `org.apache.pulsar.client.api.Messages<T>` | non-null container of non-null Pulsar messages whose `getValue()` returns `null` |

> [!IMPORTANT]
> When the passed-in value is `null` (ie. single record listeners with primitive or user-defined types) you must use the `@Payload` parameter annotation with `required = false`.

> [!IMPORTANT]
> When using the Spring `org.springframework.messaging.Message` for your listener payload type, its generic type information must be wide enough to accept `Message<PulsarNull>` (eg. `Message`, `Message<?>`, or `Message<Object>`).
> This is due to the fact that the Spring Message does not allow null values for its payload and instead uses the `PulsarNull` placeholder.

If it is a tombstone message for a compacted log, you usually also need the key so that your application can determine which key was "`deleted`".
The following example shows such a configuration:

```java
@PulsarListener(topics = "my-topic",subscriptionName = "my-topic-sub",schemaType = SchemaType.STRING) void myListener(@Payload(required = false) String msg,@Header(PulsarHeaders.KEY) String key) {...}
```

> [!NOTE]
> The `@PulsarReader` does not yet support `@Header` arguments, so it is less useful in the log compaction scenario.

---

<a id="reference-topic-resolution"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/topic-resolution.html -->

<!-- page_index: 16 -->

# Topic Resolution

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-topic-resolution--page-title"></a>
<a id="reference-topic-resolution--topic-resolution"></a>

# Topic Resolution

A destination topic is needed when producing or consuming messages.
The framework looks in the following ordered locations to determine a topic (stopping at the first find):

- User specified
- Message type default
- Global default

When a topic is found via one of the default mechanisms, there is no need to specify the topic on the produce or consume API.

When a topic is not found, the API will throw an exception accordingly.

<a id="reference-topic-resolution--_user_specified"></a>
<a id="reference-topic-resolution--1.-user-specified"></a>

## 1. User specified

A topic passed into the API being used has the highest precedence (eg. `PulsarTemplate.send("my-topic", myMessage)` or `@PulsarListener(topics = "my-topic"`).

<a id="reference-topic-resolution--_message_type_default"></a>
<a id="reference-topic-resolution--2.-message-type-default"></a>

## 2. Message type default

When no topic is passed into the API, the system looks for a message type to topic mapping configured for the type of the message being produced or consumed.

Mappings can be configured with the `spring.pulsar.defaults.type-mappings` property.
The following example uses `application.yml` to configure default topics to use when consuming or producing `Foo` or `Bar` messages:

```yaml
spring:
  pulsar:
    defaults:
      type-mappings:
        - message-type: com.acme.Foo
          topic-name: foo-topic
        - message-type: com.acme.Bar
          topic-name: bar-topic
```

> [!NOTE]
> The `message-type` is the fully-qualified name of the message class.

> [!WARNING]
> If the message (or the first message of a `Publisher` input) is `null`, the framework won’t be able to determine the topic from it. Another method shall be used to specify the topic if your application is likely to send `null` messages.

<a id="reference-topic-resolution--default-topic-via-annotation"></a>
<a id="reference-topic-resolution--2.1.-specified-via-annotation"></a>

### 2.1. Specified via annotation

When no topic is passed into the API and there are no custom topic mappings configured, the system looks for a `@PulsarMessage` annotation on the class of the message being produced or consumed.
The default topic can be specified via the `topic` attribute on the annotation.

The following example configures the default topic to use when producing or consuming messages of type `Foo`:

```java
@PulsarMessage(topic = "foo-topic")
record Foo(String value) {
}
```

Property placeholders and SpEL expressions are supported in the `@PulsarMessage` annotation, for example:

```java
@PulsarMessage(topic = "${app.topics.foo}")
record Foo(String value) {
}

@PulsarMessage(topic = "#{someBean.getTopic()}")
record Bar(String value) {
}
```

<a id="reference-topic-resolution--_custom_topic_resolver"></a>
<a id="reference-topic-resolution--2.2.-custom-topic-resolver"></a>

### 2.2. Custom topic resolver

The preferred method of adding mappings is via the property mentioned above.
However, if more control is needed you can replace the default resolver by proving your own implementation, for example:

```java
@Bean
public MyTopicResolver topicResolver() {
	return new MyTopicResolver();
}
```

<a id="reference-topic-resolution--_producer_global_default"></a>
<a id="reference-topic-resolution--3.-producer-global-default"></a>

## 3. Producer global default

The final location consulted (when producing) is the system-wide producer default topic.
It is configured via the `spring.pulsar.producer.topic-name` property.

<a id="reference-topic-resolution--_consumer_global_default"></a>
<a id="reference-topic-resolution--4.-consumer-global-default"></a>

## 4. Consumer global default

The final location consulted (when consuming) is the system-wide consumer default topic.
It is configured via the `spring.pulsar.consumer.topics` or `spring.pulsar.consumer.topics-pattern` property.

---

<a id="reference-default-tenant-namespace"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/default-tenant-namespace.html -->

<!-- page_index: 17 -->

# Default Tenant / Namespace

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-default-tenant-namespace--page-title"></a>
<a id="reference-default-tenant-namespace--default-tenant-namespace"></a>

# Default Tenant / Namespace

Pulsar has built-in support for [multi-tenancy](https://pulsar.apache.org/docs/4.2.x/concepts-multi-tenancy/).
When producing or consuming messages in Pulsar, the specified topic is actually a topic URL of the following format:

```none
(persistent|non-persistent)://tenant/namespace/topic
```

The URL dictates which tenant and namespace the operation is targeted against.
However, when not fully-qualified (i.e. only topic name is specified), the default tenant of `public` and namespace of `default` is used.

Spring for Apache Pulsar allows you to specify a default tenant and/or namespace to use when producing or consuming messages against a non-fully-qualified topic URL.

<a id="reference-default-tenant-namespace--_configuration"></a>
<a id="reference-default-tenant-namespace--configuration"></a>

## Configuration

<a id="reference-default-tenant-namespace--_with_spring_boot"></a>
<a id="reference-default-tenant-namespace--with-spring-boot"></a>

### With Spring Boot

When using the Spring Boot you can simply set the [`spring.pulsar.defaults.topic.tenant`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) and [`spring.pulsar.defaults.topic.namespace`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties to specify these defaults.

If you want to disable this feature, simply set the `spring.pulsar.defaults.topic.enabled` property to `false`.

<a id="reference-default-tenant-namespace--_without_spring_boot"></a>
<a id="reference-default-tenant-namespace--without-spring-boot"></a>

### Without Spring Boot

However, if you are instead manually configuring the components, you will have to provide a `PulsarTopicBuilder` configured with the desired default topic and namespace when constructing the corresponding producer or consumer factory.
All default consumer/reader/producer factory implementations allow a topic builder to be specified.

> [!NOTE]
> You will need to specify the topic builder on each manually configured factory that you want to use the default tenant/namespace

---

<a id="reference-custom-object-mapper"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/custom-object-mapper.html -->

<!-- page_index: 18 -->

# Custom Object Mapper

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-custom-object-mapper--page-title"></a>
<a id="reference-custom-object-mapper--custom-object-mapper"></a>

# Custom Object Mapper

Pulsar uses an internal shaded Jackson `ObjectMapper` when de/serializing JSON messages.
If you instead want to provide your own Jackson 2 object mapper instance, you can register a `SchemaResolverCustomizer` and set your mapper on the `DefaultSchemaResolver` as follows:

```java
@Bean
SchemaResolverCustomizer<DefaultSchemaResolver> schemaResolverCustomizer() {
    return (DefaultSchemaResolver schemaResolver) -> {
        var myObjectMapper = obtainMyObjectMapper();
        schemaResolver.setObjectMapper(myObjectMapper);
    };
}
```

> [!IMPORTANT]
> The object mapper in the example above should be an instance of `com.fasterxml.jackson.databind.ObjectMapper`, **not** the shaded `org.apache.pulsar.shade.com.fasterxml.jackson.databind.ObjectMapper`.

This results in your object mapper being used to de/serialize all JSON messages that go through the schema resolution process (i.e. in cases where you do not pass a schema in directly when producing/consuming messages).

Under the hood, the resolver creates a special JSON schema which leverages the custom mapper and is used as the schema for all resolved JSON messages.

If you need to pass schema instances directly you can use the `JSONSchemaUtil` to create schemas that respect the custom mapper.
The following example shows how to do this when sending a message with the `PulsarTemplate` variant that takes a schema parameter:

```java
void sendMessage(PulsarTemplate<MyPojo> template, MyPojo toSend) {
    var myObjectMapper = obtainMyObjectMapper();
    var schema = JSONSchemaUtil.schemaForTypeWithObjectMapper(MyPojo.class, myObjectMapper);
    template.send(toSend, schema);
}
```

> [!WARNING]
> Pulsar configures its default object mapper in a particular way.
> Unless you have a specific reason to not do so, it is highly recommended that you configure your mapper with these same options as follows:
>
> ```java
> myObjectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
> myObjectMapper.configure(DeserializationFeature.READ_UNKNOWN_ENUM_VALUES_AS_NULL, false);
> myObjectMapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
> ```

> [!NOTE]
> A later version of the framework may instead provide a customizer that operates on the default mapper rather than requiring a separate instance.

<a id="reference-custom-object-mapper--jackson2vs3"></a>
<a id="reference-custom-object-mapper--jackson-2-jackson-3"></a>

## Jackson 2 / Jackson 3

In Spring Boot 4 the default version of [Jackson is 3](https://docs.spring.io/spring-boot/4.0.6/reference/features/json.html#features.json.jackson) and is auto-configured via the spring-boot-starter-json module.
However, Spring for Apache Pulsar expects a [Jackson 2](https://docs.spring.io/spring-boot/4.0.6/reference/features/json.html#features.json.jackson2) custom mapper.

If you are using Jackson 3 in your Spring Boot 4 application and want to use a custom mapper you will need to add Jackson 2 to the classpath.
Don’t worry, Spring Boot 4 allows Jackson 2 and 3 to co-exist in an application.

> [!NOTE]
> A later version of the framework may support using a Jackson 2 or Jackson 3 custom mapper.

---

<a id="reference-pulsar-admin"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar-admin.html -->

<!-- page_index: 19 -->

# Pulsar Administration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-admin--page-title"></a>
<a id="reference-pulsar-admin--pulsar-administration"></a>

# Pulsar Administration

<a id="reference-pulsar-admin--pulsar-admin-client"></a>
<a id="reference-pulsar-admin--1.-pulsar-admin-client"></a>

## 1. Pulsar Admin Client

On the Pulsar administration side, Spring Boot auto-configuration provides a `PulsarAdministration` to manage Pulsar clusters.
The administration implements an interface called `PulsarAdminOperations` and provides [a `createOrModify` method](https://docs.spring.io/spring-pulsar/docs/2.0.7-SNAPSHOT/api/org/springframework/pulsar/core/PulsarAdminOperations.html) to handle topic administration through its contract.

When you use the Pulsar Spring Boot starter, you get the `PulsarAdministration` auto-configured.

By default, the application tries to connect to a local Pulsar instance at `http://localhost:8080`.
This can be adjusted by setting the `spring.pulsar.admin.service-url` property to a different value in the form `(http|https)://<host>:<port>`.

There are many application properties available to configure the client.
See the [`spring.pulsar.admin.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

<a id="reference-pulsar-admin--pulsar-admin-authentication"></a>
<a id="reference-pulsar-admin--1.1.-authentication"></a>

### 1.1. Authentication

When accessing a Pulsar cluster that requires authentication, the admin client requires the same security configuration as the regular Pulsar client.
You can use the aforementioned [security configuration](#reference-pulsar-pulsar-client--client-authentication) by replacing `spring.pulsar.client` with `spring.pulsar.admin`.

<a id="reference-pulsar-admin--pulsar-auto-topic-creation"></a>
<a id="reference-pulsar-admin--2.-automatic-topic-creation"></a>

## 2. Automatic Topic Creation

On initialization, the `PulsarAdministration` checks if there are any `PulsarTopic` beans in the application context.
For all such beans, the `PulsarAdministration` either creates the corresponding topic or, if necessary, modifies the number of partitions.

The following example shows how to add `PulsarTopic` beans to let the `PulsarAdministration` auto-create topics for you:

```java
@Bean
PulsarTopic simpleTopic(PulsarTopicBuilder topicBuilder) {
    // This will create a non-partitioned persistent topic in the 'public/default' tenant/namespace
    return topicBuilder.name("my-topic").build();
}

@Bean
PulsarTopic partitionedTopic(PulsarTopicBuilder topicBuilder) {
    // This will create a persistent topic with 3 partitions in the provided tenant and namespace
    return topicBuilder
        .name("persistent://my-tenant/my-namespace/partitioned-topic")
        .numberOfPartitions(3)
        .build();
}
```

> [!NOTE]
> When using Spring Boot the `PulsarTopicBuilder` is a registered bean that is configured with default values for domain, tenant, and namespace.
> You can simply inject the builder where needed.
> Otherwise, use one of the `PulsarTopicBuilder` constructors directly.

---

<a id="reference-pulsar-function"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/pulsar-function.html -->

<!-- page_index: 20 -->

# Pulsar Functions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-pulsar-function--page-title"></a>
<a id="reference-pulsar-function--pulsar-functions"></a>

# Pulsar Functions

Spring for Apache Pulsar provides basic suppport for [Pulsar IO](https://pulsar.apache.org/docs/4.2.x/io-connectors/) (connectors) and [Pulsar Functions](https://pulsar.apache.org/docs/4.2.x/functions-overview) which allow users to define stream processing pipelines made up of `sources`, `processors`, and `sinks`.
The `sources` and `sinks` are modeled by *Pulsar IO (connectors)* and the `processors` are represented by *Pulsar Functions*.

> [!NOTE]
> Because connectors are just special functions, and for simplicity, we refer to sources, sinks and functions collectively as "Pulsar Functions".

<a id="reference-pulsar-function--_pulsar_function_administration"></a>
<a id="reference-pulsar-function--1.-pulsar-function-administration"></a>

## 1. Pulsar Function Administration

The framework provides the `PulsarFunctionAdministration` component to manage Pulsar functions.
When you use the Pulsar Spring Boot starter, you get the `PulsarFunctionAdministration` auto-configured.

By default, the application tries to connect to a local Pulsar instance at `localhost:8080`.
However, because it leverages the already configured `PulsarAdministration`, see [Pulsar Admin Client](#reference-pulsar-admin--pulsar-admin-client) for available client options (including authentication).
Additional configuration options are available with the [`spring.pulsar.function.*`](https://docs.spring.io/spring-boot/4.0.6/appendix/application-properties/index.html#appendix.application-properties.integration) application properties.

<a id="reference-pulsar-function--_automatic_function_management"></a>
<a id="reference-pulsar-function--2.-automatic-function-management"></a>

## 2. Automatic Function Management

On application startup, the framework finds all `PulsarFunction`, `PulsarSink`, and `PulsarSource` beans in the application context.
For each bean, the corresponding Pulsar function is either created or updated.
The proper API is called based on function type, function config, and whether the function already exists.

> [!NOTE]
> The `PulsarFunction`, `PulsarSink`, and `PulsarSource` beans are simple wrappers around the Apache Pulsar config objects `FunctionConfig`, `SinkConfig`, and `SourceConfig`, respectively.
> Due to the large number of supported connectors (and their varied configurations) the framework does not attempt to create a configuration properties hierarchy to mirror the varied Apache Pulsar connectors.
> Instead, the burden is on the user to supply the full config object and then the framework handles the management (create/update) using the supplied config.

On application shutdown, all functions that were processed during application startup have their stop policy enforced and are either left alone, stopped, or deleted from the Pulsar server.

<a id="reference-pulsar-function--_limitations"></a>
<a id="reference-pulsar-function--3.-limitations"></a>

## 3. Limitations

<a id="reference-pulsar-function--_no_magic_pulsar_functions"></a>
<a id="reference-pulsar-function--3.1.-no-magic-pulsar-functions"></a>

### 3.1. No Magic Pulsar Functions

Pulsar functions and custom connectors are represented by custom application code (eg. a `java.util.Function`).
There is no magic support to automatically register the custom code.
While this would be amazing, it has some technical challenges and not yet been implemented.
As such, it is up to the user to ensure the function (or custom connector) is available at the location specified in the function config.
For example, if the function config has a `jar` value of `./some/path/MyFunction.jar` then the function jar file must exist at the specified path.

<a id="reference-pulsar-function--_name_identifier"></a>
<a id="reference-pulsar-function--3.2.-name-identifier"></a>

### 3.2. Name Identifier

The `name` property from the function config is used as the identifier to determine if a function already exists in order to decide if an update or create operation is performed.
As such, the name should not be modified if function updates are desired.

<a id="reference-pulsar-function--_configuration"></a>
<a id="reference-pulsar-function--4.-configuration"></a>

## 4. Configuration

<a id="reference-pulsar-function--_pulsar_function_archive"></a>
<a id="reference-pulsar-function--4.1.-pulsar-function-archive"></a>

### 4.1. Pulsar Function Archive

Each Pulsar function is represented by an actual archive (eg. jar file).
The path to the archive is specified via the `archive` property for sources and sinks, and the `jar` property for functions.

The following rules determine the "type" of path:

- The path is a **URL** when it starts w/ `(file|http|https|function|sink|source)://`
- The path is **built-in** when it starts w/ `builtin://` (points to one of the provided out-of-the-box connectors)
- The path is **local** otherwise.

The action that occurs during the create/update operation is dependent on path "type" as follows:

- When the path is a **URL** the content is downloaded by the server
- When the path is **built-in** the content is already available on the server
- When the path is **local** the content is uploaded to the server

<a id="reference-pulsar-function--_built_in_source_and_sinks"></a>
<a id="reference-pulsar-function--4.2.-built-in-source-and-sinks"></a>

### 4.2. Built-in Source and Sinks

Apache Pulsar provides many source and sink connectors out-of-the-box, aka built-in connectors. To use a built-in connector simply set the `archive` to `builtin://<connector-type>` (eg `builtin://rabbit`).

<a id="reference-pulsar-function--_custom_functions"></a>
<a id="reference-pulsar-function--5.-custom-functions"></a>

## 5. Custom functions

The details on how to develop and package custom functions can be found in the [Pulsar docs](https://pulsar.apache.org/docs/4.2.x/functions-develop).
However, at a high-level, the requirements are as follows:

- Code uses Java8
- Code implements either `java.util.Function` or `org.apache.pulsar.functions.api.Function`
- Packaged as uber jar

Once the function is built and packaged, there are several ways to make it available for function registration.

<a id="reference-pulsar-function--_file"></a>
<a id="reference-pulsar-function--5.1.-file:"></a>

### 5.1. file://

The jar file can be uploaded to the server and then referenced via `file://` in the `jar` property of the function config

<a id="reference-pulsar-function--_local"></a>
<a id="reference-pulsar-function--5.2.-local"></a>

### 5.2. local

The jar file can remain local and then referenced via the local path in the `jar` property of the function config.

<a id="reference-pulsar-function--_http"></a>
<a id="reference-pulsar-function--5.3.-http:"></a>

### 5.3. http://

The jar file can be made available via HTTP server and then referenced via `http(s)://` in the `jar` property of the function config

<a id="reference-pulsar-function--_function"></a>
<a id="reference-pulsar-function--5.4.-function:"></a>

### 5.4. function://

The jar file can be uploaded to the Pulsar package manager and then referenced via `function://` in the `jar` property of the function config

<a id="reference-pulsar-function--_examples"></a>
<a id="reference-pulsar-function--6.-examples"></a>

## 6. Examples

Here are some examples that show how to configure a `PulsarSource` bean which results in the `PulsarFunctionAdministration` auto-creating the backing Pulsar source connector.

PulsarSource using built-in Rabbit connector

```java
@Bean
PulsarSource rabbitSource() {
    Map<String, Object> configs = new HashMap<>();
    configs.put("host", "my.rabbit.host");
    configs.put("port", 5672);
    configs.put("virtualHost", "/");
    configs.put("username", "guest");
    configs.put("password", "guest");
    configs.put("queueName", "test_rabbit");
    configs.put("connectionName", "test-connection");
    SourceConfig sourceConfig = SourceConfig.builder()
            .tenant("public")
            .namespace("default")
            .name("rabbit-test-source")
            .archive("builtin://rabbitmq")
            .topicName("incoming_rabbit")
            .configs(configs).build();
    return new PulsarSource(sourceConfig, null);
}
```

This next example is the same as the previous, except that it uses the Spring Boot auto-configured `RabbitProperties` to ease the configuration burden. This of course requires the application to be using Spring Boot with Rabbit auto-configuration enabled.

PulsarSource using built-in Rabbit connector and Spring Boot RabbitProperties

```java
@Bean
PulsarSource rabbitSourceWithBootProps(RabbitProperties props) {
    Map<String, Object> configs = new HashMap<>();
    configs.put("host", props.determineHost());
    configs.put("port", props.determinePort());
    configs.put("virtualHost", props.determineVirtualHost());
    configs.put("username", props.determineUsername());
    configs.put("password", props.determinePassword());
    configs.put("queueName", "test_rabbit");
    configs.put("connectionName", "test-connection");
    SourceConfig sourceConfig = SourceConfig.builder()
            .tenant("public")
            .namespace("default")
            .name("rabbit-test-source")
            .archive("builtin://rabbitmq")
            .topicName("incoming_rabbit")
            .configs(configs).build();
    return new PulsarSource(sourceConfig, null);
}
```

> [!TIP]
> For a more elaborate example see the [Sample Stream Pipeline with Pulsar Functions](https://github.com/spring-projects/spring-pulsar/blob/main/spring-pulsar-sample-apps/sample-pulsar-functions/README.adoc) sample app

---

<a id="reference-observability"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/reference/observability.html -->

<!-- page_index: 21 -->

# Observability

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="reference-observability--page-title"></a>
<a id="reference-observability--observability"></a>

# Observability

Spring for Apache Pulsar includes a way to manage observability through [Micrometer](https://micrometer.io/).

<a id="reference-observability--observation"></a>
<a id="reference-observability--micrometer-observations"></a>

## Micrometer Observations

The `PulsarTemplate` and `PulsarListener` are instrumented with the Micrometer observations API.
When a Micrometer `ObservationRegistry` bean is provided, send and receive operations are traced and timed.

<a id="reference-observability--_custom_tags"></a>
<a id="reference-observability--custom-tags"></a>

### Custom tags

The default implementation adds the `bean.name` tag for template observations and `listener.id` tag for listener observations.
To add other tags to timers and traces, configure a custom `PulsarTemplateObservationConvention` or `PulsarListenerObservationConvention` to the template or listener container, respectively.

> [!TIP]
> You can subclass either `DefaultPulsarTemplateObservationConvention` or `DefaultPulsarListenerObservationConvention` or provide completely new implementations.

<a id="reference-observability--observability-metrics"></a>

### Observability - Metrics

Below you can find a list of all metrics declared by this project.

<a id="reference-observability--observability-metrics-listener-observation"></a>
<a id="reference-observability--listener-observation"></a>

#### Listener Observation

> Observation created when a Pulsar listener receives a message.

**Metric name** `spring.pulsar.listener` (defined by convention class `org.springframework.pulsar.observation.DefaultPulsarListenerObservationConvention`). **Type** `timer`.

**Metric name** `spring.pulsar.listener.active` (defined by convention class `org.springframework.pulsar.observation.DefaultPulsarListenerObservationConvention`). **Type** `long task timer`.

> [!IMPORTANT]
> KeyValues that are added after starting the Observation might be missing from the \*.active metrics.

> [!IMPORTANT]
> Micrometer internally uses `nanoseconds` for the baseunit. However, each backend determines the actual baseunit. (i.e. Prometheus uses seconds)

Fully qualified name of the enclosing class `org.springframework.pulsar.observation.PulsarListenerObservation`.

> [!IMPORTANT]
> All tags must be prefixed with `spring.pulsar.listener` prefix!

Name

Description

`spring.pulsar.listener.id` *(required)*

Id of the listener container that received the message.

<a id="reference-observability--observability-metrics-template-observation"></a>
<a id="reference-observability--template-observation"></a>

#### Template Observation

> Observation created when a Pulsar template sends a message.

**Metric name** `spring.pulsar.template` (defined by convention class `org.springframework.pulsar.observation.DefaultPulsarTemplateObservationConvention`). **Type** `timer`.

**Metric name** `spring.pulsar.template.active` (defined by convention class `org.springframework.pulsar.observation.DefaultPulsarTemplateObservationConvention`). **Type** `long task timer`.

> [!IMPORTANT]
> KeyValues that are added after starting the Observation might be missing from the \*.active metrics.

> [!IMPORTANT]
> Micrometer internally uses `nanoseconds` for the baseunit. However, each backend determines the actual baseunit. (i.e. Prometheus uses seconds)

Fully qualified name of the enclosing class `org.springframework.pulsar.observation.PulsarTemplateObservation`.

> [!IMPORTANT]
> All tags must be prefixed with `spring.pulsar.template` prefix!

Name

Description

`spring.pulsar.template.name` *(required)*

Bean name of the template that sent the message.

<a id="reference-observability--observability-spans"></a>

### Observability - Spans

Below you can find a list of all spans declared by this project.

<a id="reference-observability--observability-spans-listener-observation"></a>
<a id="reference-observability--listener-observation-span"></a>

#### Listener Observation Span

> Observation created when a Pulsar listener receives a message.

**Span name** `spring.pulsar.listener` (defined by convention class `org.springframework.pulsar.observation.DefaultPulsarListenerObservationConvention`).

Fully qualified name of the enclosing class `org.springframework.pulsar.observation.PulsarListenerObservation`.

> [!IMPORTANT]
> All tags must be prefixed with `spring.pulsar.listener` prefix!

Name

Description

`spring.pulsar.listener.id` *(required)*

Id of the listener container that received the message.

<a id="reference-observability--observability-spans-template-observation"></a>
<a id="reference-observability--template-observation-span"></a>

#### Template Observation Span

> Observation created when a Pulsar template sends a message.

**Span name** `spring.pulsar.template` (defined by convention class `org.springframework.pulsar.observation.DefaultPulsarTemplateObservationConvention`).

Fully qualified name of the enclosing class `org.springframework.pulsar.observation.PulsarTemplateObservation`.

> [!IMPORTANT]
> All tags must be prefixed with `spring.pulsar.template` prefix!

Name

Description

`spring.pulsar.template.name` *(required)*

Bean name of the template that sent the message.

See [Micrometer Tracing](https://docs.micrometer.io//tracing/reference) for more information.

<a id="reference-observability--_manual_configuration_without_spring_boot"></a>
<a id="reference-observability--manual-configuration-without-spring-boot"></a>

### Manual Configuration without Spring Boot

If you do not use Spring Boot, you need to configure and provide an `ObservationRegistry` as well as Micrometer Tracing. See [Micrometer Tracing](https://docs.micrometer.io//tracing/reference) for more information.

<a id="reference-observability--_auto_configuration_with_spring_boot"></a>
<a id="reference-observability--auto-configuration-with-spring-boot"></a>

### Auto-Configuration with Spring Boot

If you use Spring Boot, the Spring Boot Actuator auto-configures an instance of `ObservationRegistry` for you.
If `micrometer-core` is on the classpath, every stopped observation leads to a timer.

Spring Boot also auto-configures Micrometer Tracing for you. This includes support for Brave OpenTelemetry, Zipkin, and Wavefront. When using the Micrometer Observation API, finishing observations leads to spans reported to Zipkin or Wavefront. You can control tracing by setting properties under `management.tracing`. You can use Zipkin with `management.zipkin.tracing`, while Wavefront uses `management.wavefront`.

<a id="reference-observability--_example_configuration"></a>
<a id="reference-observability--example-configuration"></a>

#### Example Configuration

The following example shows the steps to configure your Spring Boot application to use Zipkin with Brave.

1. Add the required dependencies to your application (in Maven or Gradle, respectively):

   - Maven


```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-tracing-bridge-brave</artifactId>
    </dependency>
    <dependency>
        <groupId>io.zipkin.reporter2</groupId>
        <artifactId>zipkin-reporter-brave</artifactId>
    </dependency>
    <dependency>
        <groupId>io.zipkin.reporter2</groupId>
        <artifactId>zipkin-sender-urlconnection</artifactId>
    </dependency>
</dependencies>
```

   Gradle


```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-actuator'
    implementation 'io.micrometer:micrometer-tracing-bridge-brave'
    implementation 'io.zipkin.reporter2:zipkin-reporter-brave'
    implementation 'io.zipkin.reporter2:zipkin-sender-urlconnection'
}
```

   NOTE
   You need the `'io.zipkin.reporter2:zipkin-sender-urlconnection'` dependency only if your application does not have a configured WebClient or RestTemplate.
2. Add the required properties to your application:


```yaml
management:
  tracing.enabled: true
  zipkin:
    tracing.endpoint: "http://localhost:9411/api/v2/spans"
```

   The `tracing.endpoint` above expects Zipkin is running locally as described [here](https://zipkin.io/pages/quickstart.html).

At this point, your application should record traces when you send and receive Pulsar messages. You should be able to view them in the Zipkin UI (at [localhost:9411](http://localhost:9411), when running locally).

> [!TIP]
> You can also see the preceding configuration on the [Spring for Apache Pulsar Sample Apps](https://github.com/spring-projects/spring-pulsar/blob/main/spring-pulsar-sample-apps/README.adoc).

The steps are very similar to configuring any of the other supported Tracing environments.

---

<a id="other-resources"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/other-resources.html -->

<!-- page_index: 22 -->

# Other Resources

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="other-resources--page-title"></a>
<a id="other-resources--other-resources"></a>

# Other Resources

In addition to this reference documentation, we recommend a number of other resources that may help you learn about Spring and Apache Pulsar.

- [Spring for Apache Pulsar GitHub Repository](https://github.com/spring-projects/spring-pulsar)
- [Apache Pulsar Project Home Page](https://pulsar.apache.org/)
- [Apache Pulsar Java Client](https://pulsar.apache.org/docs/4.2.x/client-libraries-java/)
- [Apache Pulsar GitHub Repository](https://github.com/apache/pulsar)

---

<a id="appendix-version-compatibility"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/appendix/version-compatibility.html -->

<!-- page_index: 23 -->

# Pulsar Clients and Spring Boot Compatibility

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-version-compatibility--page-title"></a>
<a id="appendix-version-compatibility--pulsar-clients-and-spring-boot-compatibility"></a>

# Pulsar Clients and Spring Boot Compatibility

The following is the compatibility matrix:

| Spring for Apache Pulsar | Pulsar Client | Spring Boot | Java |
| --- | --- | --- | --- |
| 2.0.x | 4.1.x / 4.0.x / 3.3.x | 4.0.x | 17+ |
| 1.2.x | 3.3.x / 4.0.x**(\*)** | 3.4.x / 3.5.x | 17+ |
| 1.1.x | 3.2.x | 3.3.x | 17+ |
| 1.0.x | 3.0.x / 3.1.x | 3.2.x | 17+ |

> [!NOTE]
> **(\*)** The `3.3.x` Pulsar client is the default version specified by Spring for Apache Pulsar `1.2.x` and Spring Boot `3.4.x`.
> However, the `4.0.x` Pulsar client is compatible.
>
> You can follow [these steps](#appendix-override-boot-dependencies--override-boot-deps) to override the Pulsar client version.

> [!NOTE]
> If you are currently using Pulsar `2.11.x` you may notice that it is not present in the above matrix.
> We do not currently test nor officially support running against Pulsar `2.11.x`.
> However, Pulsar is currently compatible across versions and it is likely to work for you.

---

<a id="appendix-override-boot-dependencies"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/appendix/override-boot-dependencies.html -->

<!-- page_index: 24 -->

# Override Spring Boot Dependencies

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-override-boot-dependencies--page-title"></a>
<a id="appendix-override-boot-dependencies--override-spring-boot-dependencies"></a>

# Override Spring Boot Dependencies

When using Spring for Apache Pulsar in a Spring Boot application, the Apache Pulsar dependency versions are determined by Spring Boot’s dependency management.
If you wish to use a different version of `pulsar-client-all` you need to override their version used by Spring Boot dependency management; set the `pulsar.version` property.

Or, to use a different Spring for Apache Pulsar version with a supported Spring Boot version, set the `spring-pulsar.version` property.

In the following example, snapshot version of the Pulsar clients and Spring for Apache Pulsar are being used.

Gradle

```groovy
ext['pulsar.version'] = '4.4.2-SNAPSHOT'
ext['spring-pulsar.version'] = '2.0.1-SNAPSHOT'

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-pulsar'
}
```

- Maven

```xml
<properties>
    <pulsar.version>4.4.2-SNAPSHOT</pulsar.version>
    <spring-pulsar.version>2.0.1-SNAPSHOT</spring-pulsar.version>
</properties>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-pulsar</artifactId>
</dependency>
```

---

<a id="appendix-getting-dependencies-without-boot"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/appendix/getting-dependencies-without-boot.html -->

<!-- page_index: 25 -->

# Getting Dependencies without Spring Boot

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-getting-dependencies-without-boot--page-title"></a>
<a id="appendix-getting-dependencies-without-boot--getting-dependencies-without-spring-boot"></a>

# Getting Dependencies without Spring Boot

We recommend a Spring Boot first approach when using Spring for Apache Pulsar.
However, if you do not use Spring Boot, the preferred way to get the dependencies is to use the provided BOM to ensure a consistent version of modules is used throughout your entire project.
The following example shows how to do so for both Maven and Gradle:

- Maven
- Gradle

pom.xml

```xml
<dependencyManagement>
	<dependencies>
		<!-- ... other dependency elements ... -->
		<dependency>
			<groupId>org.springframework.pulsar</groupId>
			<artifactId>spring-pulsar-bom</artifactId>
			<version>2.0.7-SNAPSHOT</version>
			<type>pom</type>
			<scope>import</scope>
		</dependency>
	</dependencies>
</dependencyManagement>
```

build.gradle

```groovy
plugins {id "io.spring.dependency-management" version "1.1.4"}
dependencyManagement {imports {mavenBom 'org.springframework.pulsar:spring-pulsar-bom:2.0.7-SNAPSHOT'}}
```

A minimal Spring for Apache Pulsar set of dependencies typically looks like the following:

- Maven
- Gradle

pom.xml

```xml
<dependencies>
	<!-- ... other dependency elements ... -->
	<dependency>
		<groupId>org.springframework.pulsar</groupId>
		<artifactId>spring-pulsar</artifactId>
	</dependency>
</dependencies>
```

build.gradle

```groovy
dependencies {
	implementation "org.springframework.pulsar:spring-pulsar"
}
```

If you use additional features you need to also include the appropriate dependencies.

Spring for Apache Pulsar builds against Spring Framework 7.0.8 but should generally work with any newer version of Spring Framework 6.x.
Many users are likely to run afoul of the fact that Spring for Apache Pulsar’s transitive dependencies resolve Spring Framework 7.0.8, which can cause strange classpath problems.
The easiest way to resolve this is to use the `spring-framework-bom` within your `dependencyManagement` section as follows:

- Maven
- Gradle

pom.xml

```xml
<dependencyManagement>
	<dependencies>
		<!-- ... other dependency elements ... -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-framework-bom</artifactId>
			<version>7.0.8</version>
			<type>pom</type>
			<scope>import</scope>
		</dependency>
	</dependencies>
</dependencyManagement>
```

build.gradle

```groovy
plugins {id "io.spring.dependency-management" version "1.1.4"}
dependencyManagement {imports {mavenBom 'org.springframework:spring-framework-bom:7.0.8'}}
```

The preceding example ensures that all the transitive dependencies of Spring for Apache Pulsar use the Spring 7.0.8 modules.

---

<a id="appendix-non-ga-versions"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/appendix/non-ga-versions.html -->

<!-- page_index: 26 -->

# Non-GA Versions

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-non-ga-versions--page-title"></a>
<a id="appendix-non-ga-versions--non-ga-versions"></a>

# Non-GA Versions

You can find snapshot or milestone versions of the dependencies in the following repositories:

- Maven
- Gradle

```xml
<repositories>
    <repository>
        <id>spring-milestones</id>
        <name>Spring Milestones</name>
        <url>https://repo.spring.io/milestone</url>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </repository>
    <repository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
        <releases>
            <enabled>false</enabled>
        </releases>
    </repository>
    <repository>
        <id>apache-snapshots</id>
        <name>Apache Snapshots</name>
        <url>https://repository.apache.org/content/repositories/snapshots</url>
        <releases>
            <enabled>false</enabled>
        </releases>
    </repository>
</repositories>
```

```groovy
repositories {maven {name = 'spring-milestones' url = 'https://repo.spring.io/milestone'} maven {name = 'spring-snapshots' url = 'https://repo.spring.io/snapshot'} maven {name = 'apache-snapshot' url = 'https://repository.apache.org/content/repositories/snapshots'}}
```

---

<a id="appendix-native-image"></a>

<!-- source_url: https://docs.spring.io/spring-pulsar/reference/appendix/native-image.html -->

<!-- page_index: 27 -->

# GraalVM Native Image Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix-native-image--page-title"></a>
<a id="appendix-native-image--graalvm-native-image-support"></a>

# GraalVM Native Image Support

[GraalVM Native Images](https://www.graalvm.org/native-image/) are standalone executables that can be generated by processing compiled Java applications ahead-of-time. Native Images generally have a smaller memory footprint and start faster than their JVM counterparts.

Support

The required [AOT Runtime Hints](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#core.aot.hints) are built-in to Spring for Apache Pulsar so that it can seamlessly be used in native image based Spring applications.

> [!NOTE]
> The native image support in Spring for Apache Pulsar has been tested in basic scenarios, and we expect it to "just work". However, it is possible that more advanced use cases could surface the need to add additional runtime hints to your own application. If this occurs please file a [Github issue](https://github.com/spring-projects/spring-pulsar/issues) with some details.

Next Steps

If you are interested in adding native image support to your own application then an excellent place to start is the [Spring Boot GraalVM Support](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#native-image) section of the Spring Boot reference docs.

Although there is no reference to Spring for Apache Pulsar in the aforementioned guide, you can find specific examples at the following coordinates:

- [Spring for Apache Pulsar](https://github.com/spring-projects/spring-aot-smoke-tests/tree/main/integration/spring-pulsar)

---
