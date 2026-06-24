# Spring GRPC

## Navigation

- Overview
  
- [Overview](#index)
  
- [What’s new?](#whats-new)
  
- [System Requirements](#system-requirements)
  
- [Getting Started](#getting-started)
  
- [GRPC Server](#server)
  
- [GRPC Clients](#client)
  
- [Contribution Guidelines](#contribution-guidelines)
  
- [Common application properties](#appendix)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/index.html -->

<!-- page_index: 1 -->

<a id="index--page-title"></a>
<a id="index--spring-grpc"></a>

# Spring GRPC

The `Spring gRPC` project aims to streamline the development of gRPC applications.

The [Getting Started](#getting-started) section shows you how to create your first gRPC application.
Subsequent sections delve into each component and common use cases with a code-focused approach.

The [server section](#server) provides a high-level overview of gRPC servers and their representation in Spring gRPC.

The [client section](#client) does the same for gRPC clients. A gRPC application can be a client and a server at the same time.

[What’s new?](#whats-new)

---

<a id="whats-new"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/whats-new.html -->

<!-- page_index: 2 -->

# What’s new?

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="whats-new--page-title"></a>
<a id="whats-new--what-s-new"></a>

# What’s new?

<a id="whats-new--what-s-new-in-1.0.0-since-0-9-0"></a>
<a id="whats-new--what-s-new-in-1.0.0-since-0.9.0"></a>

## What’s New in 1.0.0 Since 0.9.0

This section covers the changes made from version 0.9.0 to version 1.0.0.

- Default stub factory now configurable via properties
- Update to Spring Boot 4 / Spring Framework 7 and the corresponding Spring Portfolio updates (e.g. Spring Security 6)
- JSpecify for nullability constraints
- Java 25 support

<a id="whats-new--what-s-new-in-0.9.0-since-0-8-0"></a>
<a id="whats-new--what-s-new-in-0.9.0-since-0.8.0"></a>

## What’s New in 0.9.0 Since 0.8.0

This section covers the changes made from version 0.8.0 to version 0.9.0.

- Upgrade to Spring Boot 3.5.0.
- `StubFactory` contract changes: the "supports" method is now a static method (it is called before an instance is created).
- Removed `GrpcClientFactoryCustomizer` in favour of `GrpcChannelBuilderCustomizer`.
- Added ability to filter interceptors in in-process gRPC clients.
- Added ability to filter global interceptors and service definitions - easy to do for `InProcessGrpcServer` and possible to do for `NettyGrpcServer` by registering a customizer.

<a id="whats-new--what-s-new-in-0-6-0-since-0-5-0"></a>
<a id="whats-new--what-s-new-in-0.6.0-since-0.5.0"></a>

## What’s New in 0.6.0 Since 0.5.0

This section covers the changes made from version 0.5.0 to version 0.6.0.

<a id="whats-new--_renamed_client_autowired_annotations"></a>
<a id="whats-new--renamed-client-autowired-annotations"></a>

### Renamed Client Autowired Annotations

The old `@GrpcClient` annotation has been renamed to `@ImportGrpcClients` to better reflect its purpose, and to be more consistent with changes in the Spring framework.
The customizer that is applied to generated gRPC clients is now a `GrpcClientFactoryCustomizer` - it’s main use is to modify the channel that a client is created with beyond the limits of what can be configured with `spring.grpc.client.*` properties.

<a id="whats-new--what-s-new-in-0-5-0-since-0-4-0"></a>
<a id="whats-new--what-s-new-in-0.5.0-since-0.4.0"></a>

## What’s New in 0.5.0 Since 0.4.0

This section covers the changes made from version 0.4.0 to version 0.5.0.

<a id="whats-new--_automatic_configuration_of_grpc_clients"></a>
<a id="whats-new--automatic-configuration-of-grpc-clients"></a>

### Automatic Configuration of gRPC Clients

The `@EnableGrpcClients` and nested `@GrpcClient` annotations can now be used to automatically configure gRPC clients.
Each `@GrpcClient` can be used to enumerate the stub types explicitly, or to scan a base package for stubs.

<a id="whats-new--what-s-new-in-0-4-0-since-0-3-0"></a>
<a id="whats-new--what-s-new-in-0.4.0-since-0.3.0"></a>

## What’s New in 0.4.0 Since 0.3.0

This section covers the changes made from version 0.3.0 to version 0.4.0.

<a id="whats-new--_fine_grained_starter_modules"></a>
<a id="whats-new--fine-grained-starter-modules"></a>

### Fine-grained starter modules

The following fine-grained Spring Boot starter modules have been added:

- `spring-grpc-client-spring-boot-starter` provides Netty gRPC client
- `spring-grpc-server-spring-boot-starter` provides Netty gRPC server
- `spring-grpc-server-web-spring-boot-starter` provides Servlet gRPC server

The current coarse-grained starter `spring-grpc-spring-boot-starter` still provides Netty gRPC server and client.

[Overview](#index)
[System Requirements](#system-requirements)

---

<a id="system-requirements"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/system-requirements.html -->

<!-- page_index: 3 -->

<a id="system-requirements--page-title"></a>
<a id="system-requirements--system-requirements"></a>

# System Requirements

Spring gRPC `1.0.x` requires the following:

- [Java 17](https://www.java.com) and is compatible up to and including Java 25
- [Spring Framework `7.0.1`](https://spring.io/projects/spring-framework#learn) or above

We recommend a Spring Boot first approach and Spring gRPC `1.0.x` supports [Spring Boot](https://spring.io/projects/spring-boot#learn) `4.0.x.`

[What’s new?](#whats-new)
[Getting Started](#getting-started)

---

<a id="getting-started"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/getting-started.html -->

<!-- page_index: 4 -->

# Getting Started

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="getting-started--page-title"></a>
<a id="getting-started--getting-started"></a>

# Getting Started

> [!NOTE]
> Spring gRPC `1.0.x` supports Spring Boot `4.0.x`

This section offers jumping off points for how to get started using Spring gRPC. There is a simple sample project in the `samples` directory (e.g. [`grpc-server`](https://github.com/spring-projects/spring-grpc/tree/main/samples/grpc-server)). You can run it with `mvn spring-boot:run` or `gradle bootRun`. You will see the following code in that sample.

Want to get started? Let’s speedrun a working service.

Go to the [Spring Initializr](https://start.spring.io) and select the `gRPC` dependency.

Generate the project and unzip the downloaded result.

Open it in your IDE in the usual way. E.g. if you’re using IntelliJ IDEA: `idea pom.xml`; or for VSCode `code .`.

Define a `.proto` service definition file `src/main/proto/hello.proto` with the following contents:

> [!IMPORTANT]
> Be sure to change the `java_package` to the one you chose in Spring Initializr

```proto
syntax = "proto3";

option java_multiple_files = true;
option java_package = "<your-package-name-goes-here>.proto";
option java_outer_classname = "HelloWorldProto";

// The greeting service definition.
service Simple {
  // Sends a greeting
  rpc SayHello(HelloRequest) returns (HelloReply) {}
  rpc StreamHello(HelloRequest) returns (stream HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

We’ll want to define the stubs for a Java service based on this definition:

```shell
./mvnw clean package
```

or

```shell
./gradlew build
```

Two new folders will be generated containing the source code for the stubs.

*For Maven*: `target/generated-sources/protobuf/grpc-java` and `target/generated-sources/protobuf/java`

*For Gradle*: `build/generated/source/proto/main/grpc` and `build/generated/source/proto/main/java`

You may need to instruct your IDE to mark them as source roots.
In IntelliJ IDEA, right-click the folder, choose `Mark Directory As` → `Generated Source Root`.
Eclipse or VSCode will add them automatically for you.

Now you can implement a service based on the generated stubs:

```java
@Service
class GrpcServerService extends SimpleGrpc.SimpleImplBase {

    private static Log log = LogFactory.getLog(GrpcServerService.class);

    @Override
    public void sayHello(HelloRequest req, StreamObserver<HelloReply> responseObserver) {
        log.info("Hello " + req.getName());
        if (req.getName().startsWith("error")) {
            throw new IllegalArgumentException("Bad name: " + req.getName());
        }
        if (req.getName().startsWith("internal")) {
            throw new RuntimeException();
        }
        HelloReply reply = HelloReply.newBuilder().setMessage("Hello ==> " + req.getName()).build();
        responseObserver.onNext(reply);
        responseObserver.onCompleted();
    }

    @Override
    public void streamHello(HelloRequest req, StreamObserver<HelloReply> responseObserver) {
        log.info("Hello " + req.getName());
        int count = 0;
        while (count < 10) {
            HelloReply reply = HelloReply.newBuilder().setMessage("Hello(" + count + ") ==> " + req.getName()).build();
            responseObserver.onNext(reply);
            count++;
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                responseObserver.onError(e);
                return;
            }
        }
        responseObserver.onCompleted();
    }
}
```

Run the program in the usual way:

```shell
./mvnw spring-boot:run
```

or

```shell
./gradlew bootRun
```

You can try it out using a gRPC client like `grpcurl`:

```shell
grpcurl -d '{"name":"Hi"}' -plaintext localhost:9090 Simple.SayHello
```

You should get a response like this:

```shell
{
  "message": "Hello ==\u003e Hi"
}
```

More details on what is going on in the next section.

<a id="getting-started--_details"></a>
<a id="getting-started--details"></a>

## Details

You should follow the steps in each of the following section according to your needs.

<a id="getting-started--repositories"></a>
<a id="getting-started--add-milestone-and-snapshot-repositories"></a>

### Add Milestone and Snapshot Repositories

If you prefer to add the dependency snippets by hand, follow the directions in the following sections.

To use the Milestone and Snapshot version, you need to add references to the Spring Milestone and/or Snapshot repositories in your build file.

For Maven, add the following repository definitions as needed (if you are using snapshots or milestones):

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
  </repositories>
```

For Gradle, add the following repository definitions as needed:

```groovy
repositories {
  mavenCentral()
  maven { url 'https://repo.spring.io/milestone' }
  maven { url 'https://repo.spring.io/snapshot' }
}
```

<a id="getting-started--dependency-management"></a>

### Dependency Management

The `spring-grpc-dependencies` artifact declares the recommended versions of the dependencies used by a given release of Spring gRPC, excluding dependencies already managed by Spring Boot dependency management.

The `spring-grpc-build-dependencies` artifact declares the recommended versions of all the dependencies used by a given release of Spring gRPC, including dependencies already managed by Spring Boot dependency management.

If you are running Spring gRPC in a Spring Boot application then use `spring-grpc-dependencies`, otherwise use `spring-grpc-build-dependencies`.

Using one of these dependency modules avoids the need for you to specify and maintain the dependency versions yourself.
Instead, the version of the dependency module you are using determines the utilized dependency versions.
It also ensures that you’re using supported and tested versions of the dependencies by default, unless you choose to override them.

> [!NOTE]
> The examples below assume you are running inside a Spring Boot application and therefore use `spring-grpc-dependencies`.

If you’re a Maven user, you can use the dependencies by adding the following to your pom.xml file -

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.grpc</groupId>
            <artifactId>spring-grpc-dependencies</artifactId>
            <version>1.0.3</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Gradle users can also use the dependencies by leveraging Gradle (5.0+) native support for declaring dependency constraints using a Maven BOM.
This is implemented by adding a 'platform' dependency handler method to the dependencies section of your Gradle build script.
As shown in the snippet below this can then be followed by version-less declarations of the Starter Dependencies for the one or more spring-grpc modules you wish to use, e.g. spring-grpc-openai.

```gradle
dependencies {
  implementation platform("org.springframework.grpc:spring-grpc-dependencies:1.0.3")
}
```

You need a Protobuf file that defines your service and messages, and you will need to configure your build tools to compile it into Java sources. This is a standard part of gRPC development (i.e. nothing to do with Spring). We now come to the Spring gRPC features.

<a id="getting-started--_gprc_server"></a>
<a id="getting-started--gprc-server"></a>

### gPRC Server

Create a `@Bean` of type `BindableService`. For example:

```java
@Service
public class GrpcServerService extends SimpleGrpc.SimpleImplBase {
...
}
```

(`BindableService` is the interface that gRPC uses to bind services to the server and `SimpleImplBase` was created for you from your Protobuf file.)

Then, you can just run your application and the gRPC server will be started on the default port (9090). Here’s a simple example (standard Spring Boot application):

```java
@SpringBootApplication
public class GrpcServerApplication {
	public static void main(String[] args) {
		SpringApplication.run(GrpcServerApplication.class, args);
	}
}
```

Run it from your IDE, or on the command line with `./mvnw spring-boot:run` or `./gradlew bootRun`.

<a id="getting-started--_grpc_client"></a>
<a id="getting-started--grpc-client"></a>

### gRPC Client

To create a simple gRPC client, you can use the Spring Boot starter (see above - it’s the same as for the server). Then you can inject a bean of type `GrpcChannelFactory` and use it to create a gRPC channel. The most common usage of a channel is to create a client that binds to a service, such as the one above. The Protobuf-generated sources in your project will contain the stub classes, and they just need to be bound to a channel. For example, to bind to the `SimpleGrpc` service on a local server:

```java
@Bean
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channels) {
	return SimpleGrpc.newBlockingStub(channels.createChannel("0.0.0.0:9090"));
}
```

Then you can inject the stub and use it in your application.

The default `GrpcChannelFactory` implementation can also create a "named" channel, which you can then use to extract the configuration to connect to the server. For example:

```java
@Bean
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channels) {
	return SimpleGrpc.newBlockingStub(channels.createChannel("local"));
}
```

then in `application.properties`:

```properties
spring.grpc.client.channels.local.address=0.0.0.0:9090
```

There is a default named channel that you can configure in the same way via `spring.grpc.client.default-channel.*`. It will be used by default if there is no channel with the name specified in the channel creation.

<a id="getting-started--_native_images"></a>
<a id="getting-started--native-images"></a>

### Native Images

Native images are supported for gRPC servers and clients. You can build in the [normal Spring Boot](https://docs.spring.io/spring-boot/how-to/native-image/developing-your-first-application.html) way for your build tool (Maven or Gradle).

[System Requirements](#system-requirements)
[GRPC Server](#server)

---

<a id="server"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/server.html -->

<!-- page_index: 5 -->

# GRPC Server

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server--page-title"></a>
<a id="server--grpc-server"></a>

# GRPC Server

This section describes core concepts that Spring gRPC uses on the server side. We recommend reading it closely to understand the ideas behind how Spring gRPC is implemented.
You only need to provide one or more beans of type `BindableService` to create a gRPC server, provided the classpath contains an implementation of a `Server`. The `BindableService` is a gRPC service that can be bound to a server.
The `Server` is the gRPC server that listens for incoming requests and routes them to the appropriate service implementation.

<a id="server--_create_a_grpc_service"></a>
<a id="server--create-a-grpc-service"></a>

## Create a gRPC Service

To create a gRPC server, you need to provide one or more beans of type `BindableService`.
There are some `BindableServices` available off the shelf that you could include in your application (e.g. the [gRPC Reflection](#server--reflection-service) or [gRPC Health](#server--health-service) services).
Very commonly, you will create your own `BindableService` by extending the generated service implementation from your Protobuf file.
The easiest way to activate it is to simply add a Spring `@Service` annotation to the implementation class and have it picked up by the `@ComponentScan` in your Spring Boot application.

<a id="server--service-filtering"></a>

### Service Filtering

All available `BindableService` beans are bound to all running gRPC servers.
However, you can register a `ServerServiceDefinitionFilter` bean to decide which services are bound to which server factories.

The following example prevents the "health" and "reflection" service from being bound to the server created by the server factory that the filter is applied to (e.g. the `InProcessGrpcServerFactory`).

```java
@Bean
ServerServiceDefinitionFilter myServiceFilter() {
    return (serviceDefinition, __) ->
            !Set.of(HealthGrpc.SERVICE_NAME, ServerReflectionGrpc.SERVICE_NAME)
                    .contains(serviceDefinition.getServiceDescriptor().getName());
}
```

The `InProcessGrpcServerFactory` picks up the `ServerServiceDefinitionFilter` automatically.
Any other server factory will require you to provide a `GrpcServerFactoryCustomizer` in which you can modify the factory by adding a filter, as shown in the following example:

```java
@Bean GrpcServerFactoryCustomizer myServerFactoryCustomizer(ServerServiceDefinitionFilter myServiceFilter) {return factory -> {if (factory instanceof NettyGrpcServerFactory nettyServerFactory) {nettyServerFactory.setServiceFilter(myServiceFilter);} };}
```

<a id="server--_netty_server"></a>
<a id="server--netty-server"></a>

## Netty Server

If you use the `spring-grpc-spring-boot-starter` dependency on its own, the `Server` is a Netty-based implementation.
You can configure common features of the server by using the `grpc.server` prefix in `application.properties` or `application.yml`.
For instance, to set the port to listen on, use `spring.grpc.server.port` (defaults to 9090).
For more specialized configuration, you can provide a `ServerBuilderCustomizer` bean to customize the `ServerBuilder` before it is used to create the server.

<a id="server--_shaded_netty"></a>
<a id="server--shaded-netty"></a>

### Shaded Netty

You can switch to a shaded Netty provided by the gRPC team by adding the `grpc-netty-shaded` dependency and excluding the `grpc-netty` dependency.

```xml
<dependency>
	<groupId>org.springframework.grpc</groupId>
	<artifactId>spring-grpc-spring-boot-starter</artifactId>
	<exclusions>
		<exclusion>
			<groupId>io.grpc</groupId>
			<artifactId>grpc-netty</artifactId>
		</exclusion>
	</exclusions>
</dependency>
<dependency>
	<groupId>io.grpc</groupId>
	<artifactId>grpc-netty-shaded</artifactId>
</dependency>
```

For Gradle users

```gradle
dependencies {implementation "org.springframework.grpc:spring-grpc-spring-boot-starter" implementation 'io.grpc:grpc-netty-shaded' modules {module("io.grpc:grpc-netty") {replacedBy("io.grpc:grpc-netty-shaded", "Use Netty shaded instead of regular Netty")}}}
```

<a id="server--_servlet_server"></a>
<a id="server--servlet-server"></a>

## Servlet Server

Any servlet container can be used to run a gRPC server.
Spring gRPC includes autoconfiguration that configures the server to use the servlet container if it detects that it is in a web application.
Spring gRPC also provides a convenience starter that includes the required dependencies (`spring-boot-starter-web` and the `grpc-servlet-jakarta`) for this scenario.
So all you have to do is include the `spring-boot-starter-web` dependency as follows:

```xml
<dependency>
	<groupId>org.springframework.grpc</groupId>
	<artifactId>spring-grpc-server-web-spring-boot-starter</artifactId>
</dependency>
```

For Gradle users

```gradle
dependencies {
    implementation "org.springframework.grpc:spring-grpc-server-web-spring-boot-starter"
}
```

The `spring.grpc.server.` properties will be ignored in favour of the regular `server.` properties in this case (with the exception of `spring.grpc.server.max-inbound-message-size`).
The servlet that is created is mapped to process HTTP POST requests to the paths defined by the registered services, as `/<service-name>/*`.
Clients can connect to the server using that path, which is what any gRPC client library will do.

The gRPC server has fewer configuration options when running in a servlet container, as the servlet container is responsible for the network layer.
You can still add `ServerBuilderCustomizer` beans to customize the server as it is built, but some features common in the "native" builders are not available and may throw exceptions at runtime.

<a id="server--_native_grpc_server_inside_a_servlet_container"></a>
<a id="server--native-grpc-server-inside-a-servlet-container"></a>

## Native gRPC Server inside a Servlet Container

The native gRPC server (with netty etc.) will run happily inside a web application, listening on a different port.
If you want to do that in any Spring Boot application, it should be sufficient **not** to include the `grpc-servlet-jakarta` dependency on your classpath.
This dependency is only provided by the `spring-grpc-server-web-spring-boot-starter` (or if you include it explicitly yourself), but if you need to be explicit you can set `spring.grpc.server.servlet.enabled=false` in your application configuration.

<a id="server--in-process-server"></a>
<a id="server--inprocess-server"></a>

## InProcess Server

You can run an in-process server (i.e. not listening on a network port) by including the `io.grpc.grpc-inprocess` dependency on your classpath and specifying the `spring.grpc.server.inprocess.name` property which is used as the identity of the server for clients to connect to.

In this mode, the in-process server factory is auto-configured in **addition** to the regular server factory (e.g. Netty).

> [!NOTE]
> To use the inprocess server the channel target must be set to `in-process:<in-process-name>`

<a id="server--server-interceptor"></a>
<a id="server--server-interceptors"></a>

## Server Interceptors

<a id="server--_global"></a>
<a id="server--global"></a>

### Global

To add a server interceptor to be applied to all services you can simply register a server interceptor bean and then annotate it with `@GlobalServerInterceptor`.
The interceptors are ordered according to their bean natural ordering (i.e. `@Order`).

```java
@Bean
@Order(100)
@GlobalServerInterceptor
ServerInterceptor myGlobalLoggingInterceptor() {
    return new MyLoggingInterceptor();
}
```

<a id="server--global-server-interceptor-filtering"></a>
<a id="server--filtering"></a>

#### Filtering

All global interceptors are applied to all created services by default.
However, you can register a `ServerInterceptorFilter` bean to decide which interceptors are applied to which server factories.

The following example prevents the `ExtraThingsInterceptor` interceptor from being applied to any servers created by the server factory that the filter is applied to.

```java
@Bean
ServerInterceptorFilter myInterceptorFilter() {
	return (interceptor, service) ->
			!(interceptor instanceof ExtraThingsInterceptor);
}
```

An `InProcessGrpcServerFactory` picks up the `ServerInterceptorFilter` automatically.
Any other server factory will require you to provide a `GrpcServerFactoryCustomizer` in which you can modify the factory by adding a filter, as shown in the following example:

```java
@Bean GrpcServerFactoryCustomizer myServerFactoryCustomizer() {return factory -> {if (factory instanceof NettyGrpcServerFactory) {((DefaultGrpcServerFactory)factory).setInterceptorFilter(myInterceptorFilter());} };}
```

<a id="server--_per_service"></a>
<a id="server--per-service"></a>

### Per-Service

To add a server interceptor to be applied to a single service you can simply register a server interceptor bean and then annotate your `BindableService` bean with `@GrpcService`, specifying the interceptor using either the `interceptors` or `interceptorNames` attribute.

The interceptors are ordered according to their position in the attribute list.
When using both `interceptors` and `interceptorNames`, the former entries precede the latter.

In the following example, the `myServerInterceptor` will be applied to the `myService` service.

```java
@Bean MyServerInterceptor myServerInterceptor() {return new MyServerInterceptor();}
@GrpcService(interceptors = MyServerInterceptor.class) BindableService myService() {...}
```

> [!TIP]
> When a service is configured with both global and per-service interceptors, the global interceptors are first applied in their sorted order followed by the per-service interceptors in their sorted order.
>
> However, by setting the `blendWithGlobalInterceptors` attribute on the `@GrpcService` annotation to `"true"` you can change this behavior so that the interceptors are all combined and then sorted according to their bean natural ordering (i.e. `@Order`).
>
> You can use this option if you want to add a per-service interceptor between global interceptors.

<a id="server--reflection-service"></a>
<a id="server--reflection"></a>

## Reflection

Spring gRPC autoconfigures the standard [gRPC Reflection service](https://grpc.io/docs/guides/reflection/) which allows clients to browse the metadata of your services and download the Protobuf files.

> [!IMPORTANT]
> The reflection service resides in the `io.grpc:grpc-services` library which is marked as `optional` by Spring gRPC. You must add this dependency to your application in order for it to be autoconfigured.

<a id="server--health-service"></a>
<a id="server--health"></a>

## Health

Spring gRPC autoconfigures the standard [gRPC Health service](https://grpc.io/docs/guides/health-checking/) for performing health check calls against gRPC servers.
The health service is registered with the gRPC server and a `HealthStatusManager` bean is provided that can be used to update the health status of your services.

> [!IMPORTANT]
> The health service resides in the `io.grpc:grpc-services` library which is marked as `optional` by Spring gRPC. You must add this dependency to your application in order for it to be autoconfigured.

> [!NOTE]
> Server-side gRPC health is enabled by default when the application defines at least one `BindableService`. If no server-side gRPC services are present, health is disabled by default and must be explicitly enabled using `spring.grpc.server.health.enabled=true`.

<a id="server--_actuator_health"></a>
<a id="server--actuator-health"></a>

### Actuator Health

When Spring Boot Actuator is added to your project and the [Health endpoint](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html#actuator.endpoints.health) is available, the framework will automatically periodically update the health status of a configured list of Spring Boot [health indicators](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html#actuator.endpoints.health.auto-configured-health-indicators), including any ([custom indicators](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html#actuator.endpoints.health.writing-custom-health-indicators)).
By default, the aggregate status of the individual indicators is also used to update the overall server status (`""`).

The following example uses `application.yml` to include the health status of the `db` and `redis` autoconfigured health indicators.

```yaml
spring:
  grpc:
    server:
      health:
        actuator:
          health-indicator-paths:
            - db
            - redis
```

> [!NOTE]
> The items in the `health-indicator-paths` are the identifiers of the indicator which is typically the name of the indicator bean without the `HealthIndicator` suffix.

You can use the ["spring.grpc.server.health.\*"](#appendix--common-application-properties) application properties to further configure the health feature.

<a id="server--_client_side"></a>
<a id="server--client-side"></a>

### Client-side

Spring gRPC can also autoconfigure the [client-side](https://grpc.io/docs/guides/health-checking/) health check feature to your gRPC clients.
To enable health checks on a named channel, simply set the `spring.grpc.client.channels.<channel-name>.health.enabled` application property to `true`.
To enable health checks for all channels, set the `spring.grpc.client.default-channel.enabled` application property to `true`.

By default, the health check will consult the overall status service (i.e. `""`).
To use a specific service, use the `health.service-name` application property on the desired channel.

> [!NOTE]
> The `default-load-balancing-policy` must be set to `round_robin` to participate in the health checking. This is the default used by Spring gRPC but if you change the setting you will not get health checks

The following example enables health checks for all unknown channels (using the overall server status) and for the channel named `one` (using the service `service-one` health check).

```yaml
spring:
  grpc:
    client:
      default-channel:
      health:
        enabled: true
      channels:
        one:
          health:
            enabled: true
            service-name: service-one
```

<a id="server--_observability"></a>
<a id="server--observability"></a>

## Observability

Spring gRPC provides an autoconfigured interceptor that can be used to provide observability to your gRPC services.
All you need to do is add Spring Boot actuators to your project, and optionally a bridge to your observability platform of choice (just like [any other Spring Boot application](https://docs.spring.io/spring-boot/reference/actuator/observability.html)).
The `grpc-tomcat` sample in the Spring gRPC repository shows how to do it, and you should see trace logging and metrics when you connect to the server.

<a id="server--_exception_handling"></a>
<a id="server--exception-handling"></a>

## Exception Handling

Spring gRPC provides an autoconfigured exception handler that can be used to provide a consistent way to handle exceptions in your gRPC services.
All you need to do is add `@Beans` of type `GrpcExceptionHandler` to your application context, and they will be used to handle exceptions thrown by your services.
A `GrpcExceptionHandler` can be used to handle exceptions of a specific type, returning null for those it does not support, or to handle all exceptions.

<a id="server--_testing"></a>
<a id="server--testing"></a>

## Testing

If you include `spring-grpc-test` in your project, your gRPC server in a `@SpringBootTest` can be started in-process (i.e. not listening on a network port) by enabling the in-process server.
All clients that connect to any server via the autoconfigured `GrpcChannelFactory` will be able to connect to it.
You can switch the in-process server on by setting `spring.grpc.test.inprocess.enabled` to `true` or by adding the `@AutoConfigureInProcessTransport` annotation to your `@SpringBootTest` class.

The in-process transport is an opt-in feature, so it requires an explicit configuration.
You can switch it on by setting `spring.grpc.test.inprocess.enabled` to `true` or by adding the `@AutoConfigureInProcessTransport` annotation to your `@SpringBootTest` class.
There is no need to set `spring.grpc.server.inprocess.name` as that is done automatically.
Using the annotation is equivalent to setting the "enabled" property to true, and in addition marking the in-process transport as "exclusive", meaning that no other transport will be used.

The `@AutoConfigureInProcessTransport` annotation works even if the test is not a `@SpringBootTest`, so if you only want to test the gRPC server layer you can use `@SpringJUnitConfig` with `@EnableAutoconfiguration` and add the `BindableService` beans that you want to test, either manually or as a `@ComponentScan`.
Here’s an example from the samples:

```java
@TestPropertySource(properties = { "spring.grpc.client.default-channel.address=localhost:9090" })
@SpringJUnitConfig(TestConfig.class)
@AutoConfigureInProcessTransport
public class GrpcServerSideTests {

	@Autowired
	private SimpleBlockingStub stub;

	@Test
	void contextLoads() {
		// Test the service using the stub...
	}

	@TestConfiguration
	@Import({ GrpcServerService.class })
	@EnableAutoConfiguration
	static class TestConfig {

	}

}
```

> [!NOTE]
> When the in-process server is run in test mode (as opposed to [running normally](#server--in-process-server)) it replaces the regular server and channel factories (e.g. Netty).
> All channel target addresses are magically replaced with the in-process server name, so that clients can connect to it without any special configuration (hence the "default-channel" configuration in the example above, which is there purely to trigger automatic stub creation).

<a id="server--_security"></a>
<a id="server--security"></a>

## Security

<a id="server--_netty"></a>
<a id="server--netty"></a>

### Netty

The netty-based server supports TLS and mTLS out of the box.
To configure the server you can configure an SSL Bundle in the `application.properties` or `application.yml` file.
An example would be:

```properties
spring.grpc.server.ssl.bundle=ssltest
spring.ssl.bundle.jks.ssltest.keystore.location=classpath:test.jks
spring.ssl.bundle.jks.ssltest.keystore.password=secret
spring.ssl.bundle.jks.ssltest.keystore.type=JKS
spring.ssl.bundle.jks.ssltest.key.password=password
```

Here we configure a bundle named "ssltest" that uses a JKS keystore, similar to what you do with TLS support for [Spring Boot in other areas](https://docs.spring.io/spring-boot/how-to/webserver.html#howto.webserver.configure-ssl).
It is then applied to the gRPC server using the `spring.grpc.server.ssl.bundle` property.
To use self-signed certificates, for testing purposes only, you also need to set `spring.grpc.server.ssl.secure=false`.

<a id="server--_declarative_security_with_spring_security"></a>
<a id="server--declarative-security-with-spring-security"></a>

#### Declarative Security with Spring Security

If you want to enhance the security of your gRPC server, you can use Spring Security by employing similar mechanisms to those used for regular HTTP security.
If Spring Security is on the classpath, some autoconfiguration will be automatically added to your project.
By default, just [like in a servlet application](https://docs.spring.io/spring-boot/reference/web/spring-security.html), you will get a `UserDetailsService` from Spring Boot and an `AuthenticationManager` that will authenticate requests using HTTP Basic authentication.
Basic authentication is enabled by default, as well as "preauthentication" via mTLS.
Preauthentication works by extracting a user details object from the client’s TLS certificate, matching the principal name with the user in the `UserDetailsService` (just like in a normal web application).
You can then use `@Preauthorize` on your `BindableService` beans to enforce authorization rules with roles (more precisely authorities in Spring Security terminology).

You can change the defaults and add your own rules by configuring beans of type `UserDetailsService` and/or `AuthenticationServerInterceptor`.
In this way you can move the authorization rules to a central place, and you can also add your own authentication mechanisms.
The `AuthenticationServerInterceptor` can be created from a Spring Security configurer of type `GrpcSecurity`.
Its usage will be familiar to anyone who has used Spring Security before.
Here’s an example:

```java
@Bean
@GlobalServerInterceptor
AuthenticationProcessInterceptor jwtSecurityFilterChain(GrpcSecurity grpc) throws Exception {
	return grpc
			.authorizeRequests(requests -> requests
					.methods("Simple/StreamHello").hasAuthority("ROLE_ADMIN")
					.methods("Simple/SayHello").hasAuthority("ROLE_USER")
					.methods("grpc.*/*").permitAll()
					.allRequests().denyAll())
			.httpBasic(withDefaults())
			.preauth(withDefaults())
			.build();
}
```

Here we configure a filter that allows access to one method only to admin users, and another to users with the "USER" role;
access to all gRPC services (e.g. reflection and health indicators) is allowed to all; and all other requests are denied.
We also enable HTTP Basic authentication and preauthentication (mTLS) (`withDefaults()` is a static import from the `Customizer` in Spring Security).

<a id="server--_oauth2_resource_server"></a>
<a id="server--oauth2-resource-server"></a>

#### OAuth2 Resource Server

Similar to the way Spring Boot works [with normal web applications](https://docs.spring.io/spring-boot/reference/web/spring-security.html#web.security.oauth2.server), if you have the `spring-security-oauth2-resource-server` dependency on the classpath, Spring gRPC will be able to automatically configure an OAuth2 resource server.
There are 2 choices for the token types, just the same as in Spring Boot, and they are configured with the same application properties and optional custom beans.

For JWT you need to set up either the JWK Set or OIDC Issuer URI.
The JWK Set URI is set via `spring.security.oauth2.resourceserver.jwt.jwk-set-uri` (it’s an endpoint in the authorization server).
You also need to have the `spring-security-oauth2-jose` dependency on the classpath to handle the JWT decoding.

For opaque tokens, it works exactly the same as with a regular web application, with the same application properties. E.g.

```properties
spring.security.oauth2.resourceserver.opaquetoken.introspection-uri=https://example.com/check-token
spring.security.oauth2.resourceserver.opaquetoken.client-id=my-client-id
spring.security.oauth2.resourceserver.opaquetoken.client-secret=my-client-secret
```

<a id="server--_servlet"></a>
<a id="server--servlet"></a>

### Servlet

The servlet-based server supports any security configuration that the servlet container supports, including Spring Security.
This means that you can easily implement your favourite authentication and authorization mechanisms.
The server will reject unauthenticated requests with a 401 status code and unauthenticated requests with an invalid token with a 403 status code, as with a normal HTTP API.
It will also send an appropriate `WWW-Authenticate` header, e.g. with the value `Bearer` to indicate that it is expecting a token (for example).
The gRPC response will also contain a `Status` with the appropriate error code and message.
For authorization checking, e.g. role-based access control, your `BindableService` beans can be annotated with `@PreAuthorize`.

N.B. if you customize the gRPC server call executors, you will need to ensure that you wrap them in a `DelegatingSecurityContextExecutor` (from Spring Security).
Spring gRPC handles this for the default configuration.

Spring gRPC will automatically configure the gRPC server interceptors, and [Spring Boot will provide defaults](https://docs.spring.io/spring-boot/reference/web/spring-security.html) for an `AuthenticationManager` and a `UserDetailsService`.
Spring Boot will also provide default configuration for an OAuth2 resource server, if you set the classpath up correctly (following the [Spring Boot documentation](https://docs.spring.io/spring-boot/reference/web/spring-security.html#web.security.oauth2.server)) which will be used to validate the token.
You may still want to provide your own `SecurityFilterChain`, but you can use the defaults just to get started.
Here’s an example with HTTP Basic authentication:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
	return http.httpBasic(Customizer.withDefaults())
		.authorizeHttpRequests((requests) -> requests.anyRequest().authenticated())
		.build();
}
```

By default, CSRF protection is automatically disabled for gRPC requests because it is incompatible with the protocol.
You can switch off that behaviour and configure your own CSRF protection if you want to by explicitly setting `spring.grpc.server.security.csrf.enabled=true`.
A servlet application that exposes gRPC endpoints on a different port (with `spring.grpc.server.servlet.enabled=false`) will also not have CSRF protection disabled by default.

<a id="server--_securing_individual_methods"></a>
<a id="server--securing-individual-methods"></a>

#### Securing Individual Methods

Individual gRPC methods can be secured by adding `@PreAuthorize` to the method definition.
Or you can use the knowledge that the HTTP endpoint is `<service>/<method>` to configure the security using the usual `HttpSecurity` configuration.
Example:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
	return http.authorizeHttpRequests((requests) -> requests
		.requestMatchers("/Simple/SayHello").hasRole("USER")
		.requestMatchers("/Simple/StreamHello").hasRole("ADMIN")
		.requestMatchers("/grpc.*/*").permitAll()
		.anyRequest().authenticated())
		.build();
}
```

Here we allow access to the `Simple/SayHello` method to users with the `USER` role, and to the `Simple/StreamHello` method to users with the `ADMIN` role, and allow access to all gRPC-provided services (like reflection and health indicators), while disallowing access to all other methods unless authenticated.

[Getting Started](#getting-started)
[GRPC Clients](#client)

---

<a id="client"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/client.html -->

<!-- page_index: 6 -->

# GRPC Client

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="client--page-title"></a>
<a id="client--grpc-client"></a>

# GRPC Client

This section describes core concepts that Spring gRPC uses on the client side.
The Protobuf-generated sources in your project will contain the stub classes, and they just need to be bound to a channel.
The Protobuf files will be provided by the service you are connecting to.

<a id="client--_application_properties"></a>
<a id="client--application-properties"></a>

## Application Properties

You can inject a `GrpcChannelFactory` into your application configuration and use it to create a gRPC channel.
The default `GrpcChannelFactory` implementation can create a "named" channel, which you can then use to extract the configuration to connect to the server.
For example:

```java
@Bean
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channels) {
	return SimpleGrpc.newBlockingStub(channels.createChannel("local"));
}
```

then in `application.properties`:

```properties
spring.grpc.client.channels.local.address=0.0.0.0:9090
```

There is a default named channel that you can configure as `spring.grpc.client.default-channel.*`, and then it will be used by default if there is no channel with the name specified in the channel creation.

<a id="client--_automatic_client_configuration"></a>
<a id="client--automatic-client-configuration"></a>

## Automatic Client Configuration

The automatic creation of beans for gRPC stubs is switched on by the `@ImportGrpcClients` annotation.
A Spring Boot application will have one of these by default, but you can add your own safely if you want to change the defaults, for instance to change the base type of the stubs or to scan a different package.
Spring gRPC will scan the application packages for gRPC stubs and automatically create bean definitions, as long as the default channel is configured via `spring.grpc.client.default-channel.*` (it needs at least a target URL to work).

<a id="client--_package_scanning"></a>
<a id="client--package-scanning"></a>

### Package Scanning

The `@ImportGrpcClients` annotation can be used to control the scan for gRPC stub implementations.
To scan a package you can specify the `basePackages` or `basePackageClasses` attribute.
Then elsewhere in the application you can `@Autowired` the generated gRPC stubs (the blocking sub-type by default).
You can change the factory used to create the stubs from `BlockingStubFactory` by setting the `factory` attribute.
There are standard factories pre-registered for common stub types, and if you want to register additional factories you can add a bean of type `StubFactory` (see below for details).

The default behaviour in a Spring Boot application is equivalent to the following configuration on your `@SpringBootApplication` class:

```java
// This is the default behaviour, so not necessary to add this annotation unless you change its attributes
@ImportGrpcClients(basePackageClasses = MyApplication.class)
@SpringBootApplication
class MyApplication {
	// ...
}
```

You can enhance and modify the configuration by providing `spring.grpc.client.*` application properties or by defining your own `GrpcChannelBuilderCustomizer` beans.

<a id="client--_more_complex_examples"></a>
<a id="client--more-complex-examples"></a>

### More Complex Examples

A `GrpcChannelBuilderCustomizer` can also control the creation of the channels and add custom behaviour to stubs (individually or via a scan).
For example, to add a custom security interceptor to only clients using the "stub" channel:

```java
@ImportGrpcClients(target = "stub", prefix = "secure", types = SimpleBlockingStub.class) @Configuration class ExtraConfiguration {
@Bean GrpcChannelBuilderCustomizer<?> stubs() {return GrpcChannelBuilderCustomizer.matches("stub", builder -> builder.intercept(new BearerTokenAuthenticationInterceptor(() -> token(context))));}
}
```

In this example, instead of scanning for all stubs, we register a specific stub class `SimpleBlockingStub` with the channel named `stub`.
The prefix `secure` is used as a bean definition name prefix, so the resulting bean definition in this case is "secureSimpleBlockingStub".
This feature is useful when you want to have multiple instances of the same stub class with different configurations.

If you have a custom `StubFactory` then add it as a `@Bean` and ensure that the bean definition has the correct concrete type. Then refer to that in the `@ImportGrpcClients` as its factory type. A custom factory type usually has a static method `supports(Class<?> type)` returning a boolean indicating whether the factory can create a stub of the given type. If it does not have the static method, then the factory will be used for all explicit stub types listed (but it cannot be used in a scan). The `supports` method has to be
static because it is used before the factory is created, to generate bean definitions for the stubs.

<a id="client--_create_a_client_manually"></a>
<a id="client--create-a-client-manually"></a>

## Create a Client Manually

Instead of using the `@ImportGrpcClients` or `GrpcClientFactory` features, we can create a client `@Bean` manually.
The most common usage of a channel is to create a client that binds to a service.
For example:

```java
@Bean
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channels) {
	return SimpleGrpc.newBlockingStub(channels.createChannel("0.0.0.0:9090"));
}
```

<a id="client--_shaded_netty_client"></a>
<a id="client--shaded-netty-client"></a>

### Shaded Netty Client

The default client implementation uses the Netty client.
You can switch to a shaded Netty implementation provided by the gRPC team by adding the `grpc-netty-shaded` dependency and excluding the `grpc-netty` dependency.

```xml
<dependency>
	<groupId>org.springframework.grpc</groupId>
	<artifactId>spring-grpc-spring-boot-starter</artifactId>
	<exclusions>
		<exclusion>
			<groupId>io.grpc</groupId>
			<artifactId>grpc-netty</artifactId>
		</exclusion>
	</exclusions>
</dependency>
<dependency>
	<groupId>io.grpc</groupId>
	<artifactId>grpc-netty-shaded</artifactId>
</dependency>
```

For Gradle users

```gradle
dependencies {implementation "org.springframework.grpc:spring-grpc-spring-boot-starter" implementation 'io.grpc:grpc-netty-shaded' modules {module("io.grpc:grpc-netty") {replacedBy("io.grpc:grpc-netty-shaded", "Use Netty shaded instead of regular Netty")}}}
```

<a id="client--in-process-channel"></a>
<a id="client--inprocess-channel"></a>

## InProcess Channel

You can communicate with an [in-process server](https://docs.spring.io/spring-grpc/reference/server.adoc#in-process-server) (i.e. not listening on a network port) by including the `io.grpc.grpc-inprocess` dependency on your classpath.

In this mode, the in-process channel factory is auto-configured in **addition** to the regular channel factories (e.g. Netty).
However, to prevent users from having to deal with multiple channel factories, a composite channel factory is configured as the primary channel factory bean.
The composite consults its composed factories to find the first one that supports the channel target.

> [!NOTE]
> To use the inprocess server the channel target must be set to `in-process:<in-process-name>`

To disable the inprocess channel factory, you can set the `spring.grpc.client.inprocess.enabled` property to false.

<a id="client--_channel_configuration"></a>
<a id="client--channel-configuration"></a>

## Channel Configuration

The channel factory provides an API to create channels.
The channel creation process can be configured as follows.

<a id="client--_channel_builder_customizer"></a>
<a id="client--channel-builder-customizer"></a>

### Channel Builder Customizer

The `ManagedChannelBuilder` used by the factory to create the channel can be customized prior to channel creation.

<a id="client--_global"></a>
<a id="client--global"></a>

#### Global

To customize the builder used for all created channels you can register one more `GrpcChannelBuilderCustomizer` beans.
The customizers are applied to the auto-configured `GrpcChannelFactory` in order according to their bean natural ordering (i.e. `@Order`).

```java
@Bean
@Order(100)
GrpcChannelBuilderCustomizer<NettyChannelBuilder> flowControlCustomizer() {
    return (name, builder) -> builder.flowControlWindow(1024 * 1024);
}

@Bean
@Order(200)
<T extends ManagedChannelBuilder<T>> GrpcChannelBuilderCustomizer<T> retryChannelCustomizer() {
	return (name, builder) -> builder.enableRetry().maxRetryAttempts(5);
}
```

In the preceding example, the `flowControlCustomizer` customizer is applied prior to the `retryChannelCustomizer`.
Furthermore, the `flowControlCustomizer` is only applied if the auto-configured channel factory is a `NettyGrpcChannelFactory`.

<a id="client--_per_channel"></a>
<a id="client--per-channel"></a>

#### Per-channel

To customize an individual channel you can specify a `GrpcChannelBuilderCustomizer` on the options passed to the factory during channel creation.
The per-channel customizer will be applied after any global customizers.

```java
@Bean
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channelFactory) {
    ChannelBuilderOptions options = ChannelBuilderOptions.defaults()
            .withCustomizer((__, b) -> b.disableRetry());
    ManagedChannel channel = channelFactory.createChannel("localhost", options);
    return SimpleGrpc.newBlockingStub(channel);
}
```

The above example disables retries for the single created channel only.

> [!WARNING]
> While the channel builder customizer gives you full access to the native channel builder, you should not call `build` on the customized builder as the channel factory handles the `build` call for you and doing so will create orphaned channels.

<a id="client--_the_local_server_port"></a>
<a id="client--the-local-server-port"></a>

## The Local Server Port

If you are running a gRPC server locally as part of your application, you will often want to connect to it in an integration test.
It can be convenient in that case to use an ephemeral port for the server (`spring.grpc.server.port=0`) and then use the port that is allocated to connect to it.
You can discover the port that the server is running on by injecting the `@LocalGrpcPort` bean into your test.
The `@Bean` has to be marked as `@Lazy` to ensure that the port is available when the bean is created (it is only known when the server starts which is part of the startup process).

```java
@Bean
@Lazy
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channels, @LocalGrpcPort int port) {
	return SimpleGrpc.newBlockingStub(channels.createChannel("0.0.0.0:" + port));
}
```

The channel can be configured via `application.properties` as well, by using the `${local.grpc.port}` property placeholder.
The `@Bean` where you create the stub must still be `@Lazy` for the same reason as above.
For example:

```properties
spring.grpc.client.channels.local.address=0.0.0.0:${local.grpc.port}
```

You can’t use `@LocalGrpcPort` in a bean that creates a stub, unless it is marked `@Lazy`, because it is not available until the server starts.
You can lazily resolve `local.grpc.port` in the customizer by using the `Environment` when the channel is created, either directly via its API or through placeholders like in the properties file example above.

<a id="client--client-interceptor"></a>
<a id="client--client-interceptors"></a>

## Client Interceptors

<a id="client--_global_2"></a>
<a id="client--global-2"></a>

### Global

To add a client interceptor to be applied to all created channels you can simply register a client interceptor bean and then annotate it with `@GlobalClientInterceptor`.
When you register multiple interceptor beans they are ordered according to their bean natural ordering (i.e. `@Order`).

```java
@Bean
@Order(100)
@GlobalClientInterceptor
ClientInterceptor globalLoggingInterceptor() {
    return new LoggingInterceptor();
}

@Bean
@Order(200)
@GlobalClientInterceptor
ClientInterceptor globalExtraThingsInterceptor() {
    return new ExtraThingsInterceptor();
}
```

In the preceding example, the `globalLoggingInterceptor` is applied prior to the `globalExtraThingsInterceptor`.

<a id="client--global-client-interceptor-filtering"></a>
<a id="client--filtering"></a>

#### Filtering

All global interceptors are applied to all created channels by default.
However, you can register a `ClientInterceptorFilter` to decide which interceptors are applied to which channel factories.

The following example prevents the `ExtraThingsInterceptor` interceptor from being applied to any channels created by the `InProcessGrpcChannelFactory` channel factory.

```java
@Bean
ClientInterceptorFilter myInterceptorFilter() {
    return (interceptor, factory) -> !(interceptor instanceof ExtraThingsInterceptor
            && factory instanceof InProcessGrpcChannelFactory);
}
```

The `InProcessGrpcChannelFactory` picks up the `ClientInterceptorFilter` bean automatically and applies it to the global interceptors.
For other channel factories, you can set the `interceptorFilter` property on the `GrpcChannelFactory` bean to the filter bean using a `GrpcChannelFactoryCustomizer`.

<a id="client--_per_channel_2"></a>
<a id="client--per-channel-2"></a>

### Per-Channel

To add one or more client interceptors to be applied to a single client channel you can simply set the interceptor instance(s) on the options passed to the channel factory when creating the channel.

```java
@Bean
SimpleGrpc.SimpleBlockingStub stub(GrpcChannelFactory channelFactory) {
    ClientInterceptor interceptor1 = getChannelInterceptor1();
    ClientInterceptor interceptor2 = getChannelInterceptor2();
    ChannelBuilderOptions options = ChannelBuilderOptions.defaults()
            .withInterceptors(List.of(interceptor1, interceptor2));
    ManagedChannel channel = channelFactory.createChannel("localhost", options);
    return SimpleGrpc.newBlockingStub(channel);
}
```

The above example applies `interceptor1` then `interceptor2` to the single created channel.

> [!WARNING]
> While the channel builder customizer gives you full access to the native channel builder, we recommend not calling `intercept` on the customized builder but rather set the per-channel interceptors using the `ChannelBuilderOptions` as described above.
> If you do call `intercept` directly on the builder then those interceptors will be applied before the above described `global` and `per-channel` interceptors.

<a id="client--_blended"></a>
<a id="client--blended"></a>

### Blended

When a channel is constructed with both global and per-channel interceptors, the global interceptors are first applied in their sorted order followed by the per-channel interceptors in their sorted order.

However, by setting the `withInterceptorsMerge` parameter on the `ChannelBuilderOptions` passed to the channel factory to `"true"` you can change this behavior so that the interceptors are all combined and then sorted according to their bean natural ordering (i.e. `@Order` or `Ordered` interface).

You can use this option if you want to add a per-client interceptor between global interceptors.

> [!IMPORTANT]
> The per-channel interceptors you pass in must either be bean instances marked with `@Order` or regular objects that implement the `Ordered` interface to be properly merged/ordered with the global interceptors.

<a id="client--_observability"></a>
<a id="client--observability"></a>

## Observability

Spring gRPC provides an autoconfigured interceptor that can be used to provide observability to your gRPC clients.

<a id="client--_security"></a>
<a id="client--security"></a>

## Security

If your remote gRPC server expects requests to be authenticated you will need to configure the client to provide authentication credentials.

<a id="client--_mutual_tls"></a>
<a id="client--mutual-tls"></a>

### Mutual TLS

Mutual TLS (mTLS) is a security protocol that requires both the client and the server to present certificates to each other.
A Spring gRPC client can use mTLS by configuring the client in `application.properties`.
The mechanism is through the use of [SSL Bundles](https://docs.spring.io/spring-boot/reference/features/ssl.html#features.ssl.bundles) (from Spring Boot).
Here’s an example:

```properties
spring.grpc.client.channels.my-channel.ssl.bundle=sslclient
spring.grpc.client.channels.my-channel.negotiation-type=TLS
spring.ssl.bundle.jks.sslclient.keystore.location=classpath:client.jks
spring.ssl.bundle.jks.sslclient.keystore.password=secret
spring.ssl.bundle.jks.sslclient.keystore.type=JKS
spring.ssl.bundle.jks.sslclient.key.password=password
```

The first two lines configure a channel named `my-channel` so that it has an SSL bundle named `sslclient`.
The rest is the configuration of the SSL bundle itself, in this case using JKS encoding (other options are available).

<a id="client--_http_headers"></a>
<a id="client--http-headers"></a>

### HTTP Headers

Spring gRPC provides a couple of interceptor that can be used to provide security to your gRPC clients.
There is one for Basic HTTP authentication and one for OAuth2 (bearer tokens).
Here’s an example of creating a channel that uses Basic HTTP authentication:

```java
@Bean
@Lazy
Channel basic(GrpcChannelFactory channels) {
	return channels.createChannel("my-channel", ChannelBuilderOptions.defaults()
		.withInterceptors(List.of(new BasicAuthenticationInterceptor("user", "password"))));
}
```

Usage of the bearer token interceptor is similar.
You can look at the implementation of those interceptors to see how to create your own for custom headers.

<a id="client--_oauth2_clients"></a>
<a id="client--oauth2-clients"></a>

### OAuth2 Clients

Spring gRPC provides an autoconfigured OAuth2 client that can be used to provide authentication to your gRPC clients.
It works the same as in any Spring Boot application, in that if you configure properties in `spring.security.oauth2.authorizationserver.client.*` you will be able to inject an `ClientRegistrationRepository` and use it to create an `OAuth2AuthorizedClient` for a given client registration.
Here’s an example showing how to plug the client registration into a `BearerTokenAuthenticationInterceptor` in the gRPC client:

```java
@Bean
@Lazy
SimpleGrpc.SimpleBlockingStub basic(GrpcChannelFactory channels, ClientRegistrationRepository registry) {
	ClientRegistration reg = registry.findByRegistrationId("spring");
	return SimpleGrpc.newBlockingStub(channels.createChannel("0.0.0.0:9090", ChannelBuilderOptions.defaults()
		.withInterceptors(List.of(new BearerTokenAuthenticationInterceptor(() -> token(reg))))));
}

private String token(ClientRegistration reg) {
	RestClientClientCredentialsTokenResponseClient creds = new RestClientClientCredentialsTokenResponseClient();
	String token = creds.getTokenResponse(new OAuth2ClientCredentialsGrantRequest(reg))
		.getAccessToken()
		.getTokenValue();
	return token;
}
```

[GRPC Server](#server)
[Contribution Guidelines](#contribution-guidelines)

---

<a id="contribution-guidelines"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/contribution-guidelines.html -->

<!-- page_index: 7 -->

# Contribution Guidelines

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="contribution-guidelines--page-title"></a>
<a id="contribution-guidelines--contribution-guidelines"></a>

# Contribution Guidelines

<a id="contribution-guidelines--_building_from_source"></a>
<a id="contribution-guidelines--building-from-source"></a>

## Building from Source

Java 25 is the preferred version to build with as we leverage [JSpecify](https://jspecify.dev/docs/start-here/) to validate nullability constraints in the source code.

However, if you can not use Java 25 for some reason, you can still build locally with Java 17.
In this scenario the nullability constraints will not be validated locally but rather via the continuous integration pull request workflow.

<a id="contribution-guidelines--_code_formatting_and_javadoc"></a>
<a id="contribution-guidelines--code-formatting-and-javadoc"></a>

## Code Formatting and Javadoc

Before submitting a PR, please run the following commands to ensure proper formatting and Javadoc processing

```none
./mvnw spring-javaformat:apply javadoc:javadoc -Pjavadoc
```

The `-Pjavadoc` is a profile that enables Javadoc processing so as to avoid a long build time when developing.

> [!NOTE]
> We use the [Spring JavaFormat](https://github.com/spring-io/spring-javaformat) project to apply code formatting conventions as well as checkstyle rules for many of our code conventions.
>
> The code can also be formatted from your IDE when the formatter plugin [has been installed](https://github.com/spring-projects/spring-grpc/wiki/Working-with-the-Code#install-the-spring-formatter-plugin).

<a id="contribution-guidelines--_contributing_a_new_grpc_features"></a>
<a id="contribution-guidelines--contributing-a-new-grpc-features"></a>

## Contributing a New GRPC Features

To contribute a new feature, adhere to the following steps:

1. **Implement Auto-Configuration and a Spring Boot Starter**: This step involves creating the
   necessary auto-configuration and Spring Boot Starter to easily instantiate the new model with
   Spring Boot applications.
2. **Write Tests**: All new classes should be accompanied by comprehensive tests.
   Existing tests can serve as a useful reference for structuring and implementing your tests.
3. **Document Your Contribution**: Ensure your documentation follows the existing format,
   using the `spring-javaformat` plugin to format your code and Javadoc comments.

By following these guidelines, we can greatly expand the framework’s range of supported models
while following a common implementation and documentation pattern.

<a id="contribution-guidelines--how-to-contribute"></a>

## How to Contribute

<a id="contribution-guidelines--discuss"></a>

### Discuss

If you have a question, check [StackOverflow](https://stackoverflow.com/tags/spring) using the [grpc-java](https://stackoverflow.com/tags/grpc-java) tag.
Find an existing discussion or start a new one if necessary.

If you suspect an issue, perform a search in the GitHub tracker of the Spring gRPC project, using a few different keywords.
When you find related issues and discussions, prior or current, it helps you to learn and it helps us to make a decision.

<a id="contribution-guidelines--_create_a_ticket"></a>
<a id="contribution-guidelines--create-a-ticket"></a>

### Create a Ticket

Reporting an issue or making a feature request is a great way to contribute.
Your feedback and the conversations that result from it provide a continuous flow of ideas.

Before you create a ticket, please take the time to [research first](#contribution-guidelines--discuss).

If creating a ticket after a discussion on StackOverflow or the Mailing List, please provide a self-sufficient description in the ticket.
We understand this is extra work but the issue tracker is an important place of record for design discussions and decisions that can often be referenced long after the fix version, for example to revisit decisions, to understand the origin of a feature, and so on.

When ready create a ticket in GitHub.

<a id="contribution-guidelines--ticket-lifecycle"></a>

### Ticket Lifecycle

When an issue is first created, it may not be assigned and will not have a fix version.
Within a day or two, the issue is assigned to a specific committer.
The committer will then review the issue, ask for further information if needed, and based on the findings, the issue is either assigned a fix
version or rejected.

When a fix is ready, the issue is marked "Resolved" and may still be re-opened.
Once the fix is released, you will need to create a new, related ticket with a fresh description, if necessary.

<a id="contribution-guidelines--_submit_a_pull_request"></a>
<a id="contribution-guidelines--submit-a-pull-request"></a>

## Submit a Pull Request

You can contribute a source code change by submitting a pull request.

1. You must have the right to submit code changes. Spring gRPC follows [Developer Certificate of Origin (DCO)](https://developercertificate.org/) rules. Commit messages must contain a `Signed-off-by` line. Git even has a `-s` command line option to append this automatically to your commit message:


```
This is my commit message

Signed-off-by: Random J Developer <[email protected]>

[resolves #1234]
```

   You will also be reminded automatically when you submit a pull request.
2. For all but the most trivial of contributions, please [create a ticket](#contribution-guidelines--create-a-ticket).
   The purpose of the ticket is to understand and discuss the underlying issue or feature.
   We use the GitHub issue tracker as the preferred place of record for conversations and conclusions.
   In that sense discussions directly under a PR are more implementation detail oriented and transient in nature.
3. Always check out the `main` branch and submit pull requests against it.
   Backports to prior versions will be considered on a case-by-case basis and reflected as the fix version in the issue tracker.
4. Use short branch names, preferably based on the GitHub issue (e.g. `gh-1234`), or otherwise using succinct, lower-case, dash (-) delimited names, such as `fix-warnings`.
5. Choose the granularity of your commits consciously and squash commits that represent multiple edits or corrections of the same logical change.
   See [Rewriting History section of Pro Git](https://git-scm.com/book/en/Git-Tools-Rewriting-History) for an overview of streamlining commit history.
6. Format commit messages using 55 characters for the subject line, 72 lines for the description, followed by related issues, e.g. `[resolves #1234]`
   See the [Commit Guidelines section of Pro Git](https://git-scm.com/book/en/Distributed-Git-Contributing-to-a-Project#Commit-Guidelines) for best practices around commit messages and use `git log` to see some examples.
7. List the GitHub issue number in the PR description.

If accepted, your contribution may be heavily modified as needed prior to merging.
You will likely retain author attribution for your Git commits granted that the bulk of your changes remain intact.
You may also be asked to rework the submission.

If asked to make corrections, simply push the changes against the same branch, and your pull request will be updated.
In other words, you do not need to create a new pull request when asked to make changes.

[GRPC Clients](#client)
[Common application properties](#appendix)

---

<a id="appendix"></a>

<!-- source_url: https://docs.spring.io/spring-grpc/reference/appendix.html -->

<!-- page_index: 8 -->

# Common application properties

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendix--page-title"></a>
<a id="appendix--common-application-properties"></a>

# Common application properties

Various properties can be specified inside your `application.properties` file, inside your `application.yml` file, or as command line switches.
This appendix provides a list of common `Spring gRPC` properties.

| Name | Default | Description |
| --- | --- | --- |
| spring.grpc.client.channels |  | Map of channels configured by name. |
| spring.grpc.client.default-channel.address | `static://localhost:9090` | The target address uri to connect to. |
| spring.grpc.client.default-channel.default-deadline |  | The default deadline for RPCs performed on this channel. |
| spring.grpc.client.default-channel.default-load-balancing-policy | `round_robin` | The load balancing policy the channel should use. |
| spring.grpc.client.default-channel.enable-keep-alive | `false` | Whether keep alive is enabled on the channel. |
| spring.grpc.client.default-channel.health.enabled | `false` | Whether to enable client-side health check for the channel. |
| spring.grpc.client.default-channel.health.service-name |  | Name of the service to check health on. |
| spring.grpc.client.default-channel.idle-timeout | `20s` | The duration without ongoing RPCs before going to idle mode. |
| spring.grpc.client.default-channel.keep-alive-time | `5m` | The delay before sending a keepAlive. Note that shorter intervals increase the network burden for the server and this value can not be lower than 'permitKeepAliveTime' on the server. |
| spring.grpc.client.default-channel.keep-alive-timeout | `20s` | The default timeout for a keepAlives ping request. |
| spring.grpc.client.default-channel.keep-alive-without-calls | `false` | Whether a keepAlive will be performed when there are no outstanding RPC on a connection. |
| spring.grpc.client.default-channel.max-inbound-message-size | `4194304B` | Maximum message size allowed to be received by the channel (default 4MiB). Set to '-1' to use the highest possible limit (not recommended). |
| spring.grpc.client.default-channel.max-inbound-metadata-size | `8192B` | Maximum metadata size allowed to be received by the channel (default 8KiB). Set to '-1' to use the highest possible limit (not recommended). |
| spring.grpc.client.default-channel.negotiation-type | `plaintext` | The negotiation type for the channel. |
| spring.grpc.client.default-channel.secure | `true` | Flag to say that strict SSL checks are not enabled (so the remote certificate could be anonymous). |
| spring.grpc.client.default-channel.service-config |  | Map representation of the service config to use for the channel. |
| spring.grpc.client.default-channel.ssl.bundle |  | SSL bundle name. |
| spring.grpc.client.default-channel.ssl.enabled |  | Whether to enable SSL support. Enabled automatically if "bundle" is provided unless specified otherwise. |
| spring.grpc.client.default-channel.user-agent |  | The custom User-Agent for the channel. |
| spring.grpc.client.default-stub-factory |  | Default stub factory to use for all channels. |
| spring.grpc.client.enabled | `true` | Whether to enable client autoconfiguration. |
| spring.grpc.client.inprocess.enabled | `true` | Whether to configure the in-process channel factory. |
| spring.grpc.client.inprocess.exclusive | `true` | Whether the inprocess channel factory should be the only channel factory available. When the value is true, no other channel factory will be configured. |
| spring.grpc.client.observation.enabled | `true` | Whether to enable Observations on the client. |
| spring.grpc.server.address |  | The address to bind to in the form 'host:port' or a pseudo URL like 'static://host:port'. When the address is set it takes precedence over any configured host/port values. |
| spring.grpc.server.enabled | `true` | Whether to enable server autoconfiguration. |
| spring.grpc.server.exception-handling.enabled | `true` | Whether to enable user-defined global exception handling on the gRPC server. |
| spring.grpc.server.health.actuator.enabled | `true` | Whether to adapt Actuator health indicators into gRPC health checks. |
| spring.grpc.server.health.actuator.health-indicator-paths |  | List of Actuator health indicator paths to adapt into gRPC health checks. |
| spring.grpc.server.health.actuator.update-initial-delay | `5s` | The initial delay before updating the health status the very first time. |
| spring.grpc.server.health.actuator.update-overall-health | `true` | Whether to update the overall gRPC server health (the '' service) with the aggregate status of the configured health indicators. |
| spring.grpc.server.health.actuator.update-rate | `5s` | How often to update the health status. |
| spring.grpc.server.health.enabled | `true` | Whether to auto-configure Health feature on the gRPC server. |
| spring.grpc.server.host | `*` | Server host to bind to. The default is any IP address ('\*'). |
| spring.grpc.server.inprocess.exclusive | `true` | Whether the inprocess server factory should be the only server factory available. When the value is true, no other server factory will be configured. |
| spring.grpc.server.inprocess.name |  | The name of the in-process server or null to not start the in-process server. |
| spring.grpc.server.keep-alive.max-age |  | Maximum time a connection may exist before being gracefully terminated (default infinite). |
| spring.grpc.server.keep-alive.max-age-grace |  | Maximum time for graceful connection termination (default infinite). |
| spring.grpc.server.keep-alive.max-idle |  | Maximum time a connection can remain idle before being gracefully terminated (default infinite). |
| spring.grpc.server.keep-alive.permit-time | `5m` | Maximum keep-alive time clients are permitted to configure (default 5m). |
| spring.grpc.server.keep-alive.permit-without-calls | `false` | Whether clients are permitted to send keep alive pings when there are no outstanding RPCs on the connection (default false). |
| spring.grpc.server.keep-alive.time | `2h` | Duration without read activity before sending a keep alive ping (default 2h). |
| spring.grpc.server.keep-alive.timeout | `20s` | Maximum time to wait for read activity after sending a keep alive ping. If sender does not receive an acknowledgment within this time, it will close the connection (default 20s). |
| spring.grpc.server.max-inbound-message-size | `4194304B` | Maximum message size allowed to be received by the server (default 4MiB). |
| spring.grpc.server.max-inbound-metadata-size | `8192B` | Maximum metadata size allowed to be received by the server (default 8KiB). |
| spring.grpc.server.observation.enabled | `true` | Whether to enable Observations on the server. |
| spring.grpc.server.port | `9090` | Server port to listen on. When the value is 0, a random available port is selected. |
| spring.grpc.server.reflection.enabled | `true` | Whether to enable Reflection on the gRPC server. |
| spring.grpc.server.security.csrf.enabled | `false` | Whether to enable CSRF protection on gRPC requests. |
| spring.grpc.server.servlet.enabled | `true` | Whether to use a servlet server in a servlet-based web application. When the value is false, a native gRPC server will be created as long as one is available, and it will listen on its own port. Should only be needed if the GrpcServlet is on the classpath |
| spring.grpc.server.shutdown-grace-period | `30s` | Maximum time to wait for the server to gracefully shutdown. When the value is negative, the server waits forever. When the value is 0, the server will force shutdown immediately. The default is 30 seconds. |
| spring.grpc.server.ssl.bundle |  | SSL bundle name. Should match a bundle configured in spring.ssl.bundle. |
| spring.grpc.server.ssl.client-auth | `none` | Client authentication mode. |
| spring.grpc.server.ssl.enabled |  | Whether to enable SSL support. |
| spring.grpc.server.ssl.secure | `true` | Flag to indicate that client authentication is secure (i.e. certificates are checked). Do not set this to false in production. |
| spring.grpc.test.inprocess.enabled | `false` | Whether to enable the in-process server and client for testing. Consider using @AutoConfigInProcessTransport instead. |

[Contribution Guidelines](#contribution-guidelines)

---
