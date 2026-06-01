# HttpClient Overview

## Navigation

- Documentation
  - [Quick Start](#quickstart)
  - [Architecture](#architecture)
  - Guides
    - [Migration](#migration-guide)
    - [Configuration](#configuration)
    - [Logging](#logging)
    - [Connection management](#connection-management)
    - [Connection pooling](#connection-pooling)
    - [Async content compression / decompression](#async-compression)
    - [Android support](#android)
    - [Early Hints](#early-hints)
    - [Observation](#observation)
    - [SCRAM-SHA-256](#scram-sha-256)
    - [SPKI pinning TLS strategy](#spki-pinning)
  - Examples demonstrating some common as well as more complex use cases
    - [HttpClient Classic APIs](#examples)
    - [HttpClient Async APIs](#examples-async)
    - [HttpClient Reactive Streams APIs](#examples-reactive)
    - [HttpClient Observation APIs](#examples-observation)
- Components
  - [HttpClient 5.6](#index)
    - [Quick Start](#quickstart)
    - [Architecture](#architecture)
    - [Configuration Guide](#configuration)
    - [Migration Guide](#migration-guide)
      - [Preparation](#migration-guide-preparation)
      - [Classic](#migration-guide-migration-to-classic)
      - [Async Simple](#migration-guide-migration-to-async-simple)
      - [Async Streaming](#migration-guide-migration-to-async-streaming)
      - [Async HTTP/2 only](#migration-guide-migration-to-async-http2)
    - [Logging Guide](#logging)
    - [Android](#android)
    - [Examples (Classic)](#examples)
    - [Examples (Async)](#examples-async)
    - [Examples (Reactive)](#examples-reactive)
    - [Related](#related-projects)
    - [Download](#download)

## Content

<a id="quickstart"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/quickstart.html -->

<!-- page_index: 1 -->

<a id="quickstart--httpclient-quick-start"></a>

# HttpClient Quick Start

- Download ‘Binary’ package of the latest HttpClient 5.5 release or configure dependency on `HttpClient` and `Fluent HC`
  modules using a dependency manager of your choice as described [here](https://hc.apache.org/downloads.html).
- HttpClient 5.5 requires Java 1.8 or newer.
- The below code fragment illustrates the execution of HTTP GET and POST requests using the HttpClient native API.


```
try (CloseableHttpClient httpclient = HttpClients.createDefault()) {
    ClassicHttpRequest httpGet = ClassicRequestBuilder.get("http://httpbin.org/get")
            .build();
    // The underlying HTTP connection is still held by the response object
    // to allow the response content to be streamed directly from the network socket.
    // In order to ensure correct deallocation of system resources
    // the user MUST call CloseableHttpResponse#close() from a finally clause.
    // Please note that if response content is not fully consumed the underlying
    // connection cannot be safely re-used and will be shut down and discarded
    // by the connection manager.
    httpclient.execute(httpGet, response -> {
        System.out.println(response.getCode() + " " + response.getReasonPhrase());
        final HttpEntity entity1 = response.getEntity();
        // do something useful with the response body
        // and ensure it is fully consumed
        EntityUtils.consume(entity1);
        return null;
    });

    ClassicHttpRequest httpPost = ClassicRequestBuilder.post("http://httpbin.org/post")
            .setEntity(new UrlEncodedFormEntity(Arrays.asList(
                    new BasicNameValuePair("username", "vip"),
                    new BasicNameValuePair("password", "secret"))))
            .build();
    httpclient.execute(httpPost, response -> {
        System.out.println(response.getCode() + " " + response.getReasonPhrase());
        final HttpEntity entity2 = response.getEntity();
        // do something useful with the response body
        // and ensure it is fully consumed
        EntityUtils.consume(entity2);
        return null;
    });
}
```

- The same requests can be executed using a simpler, albeit less flexible, fluent API.


```
// The fluent API relieves the user from having to deal with manual deallocation of system
// resources at the cost of having to buffer response content in memory in some cases.

Request.Get("http://targethost/homepage")
    .execute().returnContent();
Request.Post("http://targethost/login")
    .bodyForm(Form.form().add("username",  "vip").add("password",  "secret").build())
    .execute().returnContent();
```

- The below code fragment illustrates the execution of HTTP requests using HttpClient async API.


```
try (CloseableHttpAsyncClient httpclient = HttpAsyncClients.createDefault()) {
    // Start the client
    httpclient.start();

    // Execute request
    SimpleHttpRequest request1 = SimpleRequestBuilder.get("http://httpbin.org/get").build();
    Future<SimpleHttpResponse> future = httpclient.execute(request1, null);
    // and wait until response is received
    SimpleHttpResponse response1 = future.get();
    System.out.println(request1.getRequestUri() + "->" + response1.getCode());

    // One most likely would want to use a callback for operation result
    CountDownLatch latch1 = new CountDownLatch(1);
    SimpleHttpRequest request2 = SimpleRequestBuilder.get("http://httpbin.org/get").build();
    httpclient.execute(request2, new FutureCallback<SimpleHttpResponse>() {

        @Override
        public void completed(SimpleHttpResponse response2) {
            latch1.countDown();
            System.out.println(request2.getRequestUri() + "->" + response2.getCode());
        }

        @Override
        public void failed(Exception ex) {
            latch1.countDown();
            System.out.println(request2.getRequestUri() + "->" + ex);
        }

        @Override
        public void cancelled() {
            latch1.countDown();
            System.out.println(request2.getRequestUri() + " cancelled");
        }

    });
    latch1.await();

    // In real world one most likely would want also want to stream
    // request and response body content
    CountDownLatch latch2 = new CountDownLatch(1);
    AsyncRequestProducer producer3 = AsyncRequestBuilder.get("http://httpbin.org/get").build();
    AbstractCharResponseConsumer<HttpResponse> consumer3 = new AbstractCharResponseConsumer<HttpResponse>() {

        HttpResponse response;

        @Override
        protected void start(HttpResponse response, ContentType contentType) throws HttpException, IOException {
            this.response = response;
        }

        @Override
        protected int capacityIncrement() {
            return Integer.MAX_VALUE;
        }

        @Override
        protected void data(CharBuffer data, boolean endOfStream) throws IOException {
            // Do something useful
        }

        @Override
        protected HttpResponse buildResult() throws IOException {
            return response;
        }

        @Override
        public void releaseResources() {
        }

    };
    httpclient.execute(producer3, consumer3, new FutureCallback<HttpResponse>() {

        @Override
        public void completed(HttpResponse response3) {
            latch2.countDown();
            System.out.println(request2.getRequestUri() + "->" + response3.getCode());
        }

        @Override
        public void failed(Exception ex) {
            latch2.countDown();
            System.out.println(request2.getRequestUri() + "->" + ex);
        }

        @Override
        public void cancelled() {
            latch2.countDown();
            System.out.println(request2.getRequestUri() + " cancelled");
        }

    });
    latch2.await();

}
```

---

<a id="architecture"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/architecture.html -->

<!-- page_index: 2 -->

<a id="architecture--architecture"></a>

# Architecture

<a id="architecture--layering-principles"></a>

## Layering Principles

<a id="architecture--network-i-o-layer"></a>

### Network I/O layer

This layer is responsible for transmitting octets of data between endpoints (local and
remote)

- Classic: based on `java.net.Socket` / `java.io.OutputStream` / `java.io.InputStream`
  APIs.
- Event-driven (async): based on `java.nio.channels.Selector` and
  `java.nio.channels.Channel` APIs

Both implementations are provided by HttpCore.

Potentially there can be other network layer implementations, for example, QUIC based
or Netty based.

<a id="architecture--transport-security-layer"></a>

### Transport Security Layer

This layer implements Transport Layer Security on top of the network I/O layer as defined
by the TLS protocol. Both the classic and async implementations rely on the TLS protocol
functionality provided by the standard JSSE security provider. Alternative JSSE providers
such as Conscrypt can be used as well.

<a id="architecture--protocol-transport-layer"></a>

### Protocol Transport Layer

This layer is responsible for transport of messages between endpoints based on a
communication protocol.

- HTTP/1.1 with HTTP/1.0 compatibility
- HTTP/2

The classic implementation supports HTTP/1.1. The async implementation supports HTTP/1.1
and HTTP/2.

Both implementations are provided by HttpCore.

Please note that the classic I/O model work well with request / response oriented
protocols such as HTTP/1.1 but does not lend itself well to multiplexing protocols such as
HTTP/2. This is the reason the classic I/O based clients presently support HTTP/1.1 only.

<a id="architecture--connection-management-layer"></a>

### Connection Management Layer

This layer facilitates efficient creation and re-use of connections. It also aims at
harmonising the connection management APIs across different netweok I/O models and
protocols and making those APIs as compatible and consistent as possible. This layer is
responsible for connection creation, initialization, upgrade to TLS and re-use by
maintaining pools of reusable persistent connection that can be leased to execute message
exchanges and released back to the pool.

Both Classic and Async I/O models are supported.

Connection pool implementations are provided by HttpCore.

<a id="architecture--message-exchange-protocol-layer"></a>

### Message Exchange Protocol Layer

This layer is responsible for execution of complex message exchanges that may involve
complex routing, authentication, state management, automatic re-execution or recovery and
transparent compression / decompression of content. It also aims at harmonising the
request execution APIs across different transport models and protocols and making those
APIs as compatible and consistent as possible.

Both Classic and Async I/O models are supported.

<a id="architecture--caching-protocol-layer"></a>

### Caching Protocol Layer

This layer implements HTTP caching protocol on top of a message exchange protocol layer.

Both Classic and Async I/O models are supported.

This layer is optional.

<a id="architecture--reactive-streams-layer"></a>

### Reactive Streams Layer

This layer provides [Reactive Streams Bindings](https://www.reactive-streams.org/) on top
of the async message exchange protocol layer.

The bindings implementation is provided by HttpCore.

This layer is optional.

<a id="architecture--classic-over-async-facade"></a>

### Classic Over Async Facade

This layer provides compatibility bindings with the classic `java.io.OutputStream` /
`java.io.InputStream` based APIs on top of the asnyc message exchange protocol layer.

This layer is optional and is still considered experimental.

---

<a id="migration-guide"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/migration-guide/index.html -->

<!-- page_index: 3 -->

<a id="migration-guide--apache-httpclient-5.x-migration-guide"></a>

# Apache HttpClient 5.x migration guide

1. [Migration from HttpClient 4.x](#migration-guide-preparation)

   Prior to migration from HttpClient 4.x to HttpClient 5.x it is highly recommended to ensure that HttpClient 4.x is up
   to date and is being used in accordance with the best practices and recommendations.
2. [Migration to HttpClient 5.x classic APIs](#migration-guide-migration-to-classic)

   When migrating from HttpClient 4.x to HttpClient 5.x it is generally recommended to migrate to the classic APIs as
   the first step.
3. [Migration to HttpClient 5.x async APIs with simple handlers](#migration-guide-migration-to-async-simple)

   When migrating to HttpClient 5.x async APIs it might be easier to start off by using simple (using in-memory buffers)
   asynchronous handlers.
4. [Migration to HttpClient 5.x async APIs](#migration-guide-migration-to-async-streaming)

   The ultimate goal of the migration process should be to use HttpClient 5.x async APIs with full content streaming
   over full-duplex HTTP/1.1 or HTTP/2 connections.
5. [Migration to HttpClient 5.x async APIs for HTTP/2 only](#migration-guide-migration-to-async-http2)

   For those scenarios where HTTP/1.1 compatibility is no longer required HttpClient 5.x provides HTTP/2 optimized
   clients.

---

<a id="configuration"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/configuration.html -->

<!-- page_index: 4 -->

<a id="configuration--configuration-guide"></a>

# Configuration Guide

The concept of HttpClient configuration APIs is closely aligned with
its [Architecture](#architecture) layering principles. Configuration parameters are
grouped by the architecture layer they apply to. Those groups of configuration parameters
are modelled as immutable bean classes referred to as config beans. Config beans are safe
to pass around to different classes as those beans cannot be modified at runtime.

A config beans class always represents logically related properties of a single
architecture layer. There can be however properties shared by multiple layers applicable
to the underlying connection or ongoing message exchange at a different points of their
life-cycle. Socket timeout is one of such parameters. For example, connections can start
off with a default value of the socket timeout which can later be overridden at a higher
level or at a specific phase of connection life-cycle such as TLS handshake.

<a id="configuration--configuration-levels"></a>

## Configuration Levels

<a id="configuration--network-i-o-level"></a>

### Network I/O Level

- [SocketConfig](https://hc.apache.org/httpcomponents-core-5.3.x/current/httpcore5/apidocs/org/apache/hc/core5/http/io/SocketConfig.html):
  these parameters apply to the Classic Network I/O layer and define connection socket
  properties.

  Socket configuration applies on a per-socket basis.
- [IOReactorConfig](https://hc.apache.org/httpcomponents-core-5.3.x/current/httpcore5/apidocs/org/apache/hc/core5/reactor/IOReactorConfig.html):
  these parameters apply to the Async Network I/O layer and define I/O reactor properties.

<a id="configuration--protocol-transport-level"></a>

### Protocol Transport Level

- [Http1Config](https://hc.apache.org/httpcomponents-core-5.3.x/current/httpcore5/apidocs/org/apache/hc/core5/http/config/Http1Config.html):
  these parameters apply to the HTTP/1.1 protocol handlers and define common aspects of
  HTTP/1.1 message transmission.

  HTTP/1.1 configuration applies on a per-connection basis.
- [H2Config](https://hc.apache.org/httpcomponents-core-5.3.x/current/httpcore5-h2/apidocs/org/apache/hc/core5/http2/config/H2Config.html):
  these parameters apply to the HTTP/2 protocol handlers and define common aspects of
  HTTP/2 message transmission and message multiplexing.

  HTTP/2 configuration applies on a per-connection basis.
- [CharCodingConfig](https://hc.apache.org/httpcomponents-core-5.3.x/current/httpcore5/apidocs/org/apache/hc/core5/http/config/CharCodingConfig.html):
  these parameters apply to text based protocols such as HTTP/1.1 and define properties of
  binary to text coding.

  Character coding configuration applies on a per-connection basis.

<a id="configuration--connection-management-level"></a>

### Connection Management Level

- [ConnectionConfig](https://hc.apache.org/httpcomponents-client-5.5.x/current/httpclient5/apidocs/org/apache/hc/client5/http/config/ConnectionConfig.html):
  these parameters apply to connections managed by connection managers. Connection
  configuration is expected to work consistently across all supported network I/O
  implementations.

  Connection configuration applies on a per-route basis.

  An example of per-route connection configuration for the classic transport can be found
  here: [classic](https://github.com/apache/httpcomponents-client/blob/5.5.x/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientConnectionConfig.java)
  and [async](https://github.com/apache/httpcomponents-client/blob/5.5.x/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientConnectionConfig.java).

<a id="configuration--tls-level"></a>

### TLS Level

- [TlsConfig](https://hc.apache.org/httpcomponents-client-5.5.x/current/httpclient5/apidocs/org/apache/hc/client5/http/config/TlsConfig.html):
  these parameters apply to connections at the time of TLS handshake
  execution and session negotiation. TLS configuration is expected to work consistently
  across all supported network I/O implementations.

  TLS configuration applies on a per-host basis.

  An example of per-host TLS configuration for the classic transport can be found
  here: [classic](https://github.com/apache/httpcomponents-client/blob/5.5.x/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientConnectionConfig.java)
  and [async](https://github.com/apache/httpcomponents-client/blob/5.5.x/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientConnectionConfig.java).

<a id="configuration--message-exchange-protocol-level"></a>

### Message Exchange Protocol Level

- [RequestConfig](https://hc.apache.org/httpcomponents-client-5.5.x/current/httpclient5/apidocs/org/apache/hc/client5/http/config/RequestConfig.html):
  these parameters apply to individual HTTP message exchanges. Request execution
  parameters are generally expected to work consistently to all HTTP protocol versions
  with a few exceptions when certain functionality is not applicable due to differences in
  message transport between different HTTP protocol versions.

  Request configuration applies on a per-request basis.

<a id="configuration--caching-protocol-level"></a>

### Caching Protocol Level

- [CacheConfig](https://hc.apache.org/httpcomponents-client-5.5.x/current/httpclient5-cache/apidocs/org/apache/hc/client5/http/impl/cache/CacheConfig.html):
  these parameters apply to the caching protocol layer. They also define the most common
  properties shared by different cache storage implementations. Individual caching
  backends may still expose configuration options specific to those backends.

  Cache configuration applies on a per-instance basis.

---

<a id="logging"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/logging.html -->

<!-- page_index: 5 -->

<a id="logging--logging-practices"></a>

# Logging Practices

Being a library HttpClient is not to dictate which logging framework the user has to use. Therefore HttpClient utilizes
the logging facade provided by the [Simple Logging Facade for Java (SLF4J)](https://slf4j.org/) package. `SLF4J` provides
a simple and generalized [log interface](https://slf4j.org/manual.html) to various logging packages. By using `SLF4J`, HttpClient can be configured for a variety of different logging behaviours. That means the user will have to make a
choice which logging implementation to use. There are several popular logging backends that can be used through
the `SLF4J` facade APIs:

- [Logback](https://logback.qos.ch/)
- [Log4j 2](https://logging.apache.org/log4j/2.x/index.html)
- [SimpleLogger](http://slf4j.org/api/org/slf4j/impl/SimpleLogger.html) (internal to `SLF4J`)
- [java.util.logging](http://slf4j.org/api/org/slf4j/impl/JDK14LoggerAdapter.html) (internal to `SLF4J`)

HttpComponents project however mostly works with [Log4j 2](https://logging.apache.org/log4j/2.x/index.html) backend and
recommends it to our users.

HttpClient performs three different kinds of logging: the standard context logging used within each class, HTTP header
logging and full wire logging.

<a id="logging--understanding-logger-names"></a>

## Understanding Logger Names

Most logging implementations use a hierarchical scheme for matching logger names with logging configuration. In this
scheme, the logger name hierarchy is represented by ‘`.`’ characters in the logger name, in a fashion very similar to
the hierarchy used for Java package names. For example, `org.apache.logging.appender` and `org.apache.logging.filter`
both have `org.apache.logging` as their parent. In most cases, applications name their loggers by passing the current
class's name to `LogManager.getLogger(...)`.

<a id="logging--context-logging"></a>

### Context Logging

Context logging contains information about the internal operation of HttpClient as it performs HTTP requests. Each class
has its own logger named according to the class's fully qualified name. For example the class `DefaultHttpClient` has a
logger named `org.apache.http.impl.client.DefaultHttpClient`. Since all classes follow this convention it is possible to
configure context logging for all classes using the single logger named
`org.apache.hc.client5.http`.

<a id="logging--wire-logging"></a>

### Wire Logging

The wire logger is used to log all data transmitted to and from servers when executing HTTP requests. The wire logger
uses the `org.apache.hc.client5.http.wire` logger name. This logger should only be enabled to debug problems, as it will
produce an extremely large amount of log data.

<a id="logging--http-header-logging"></a>

### HTTP header Logging

Because the content of HTTP requests is usually less important for debugging than the HTTP headers, use the `org.apache.hc.client5.http.headers` logger for capturing HTTP headers only.

<a id="logging--configuration-examples"></a>

## Configuration Examples

`SLF4J` can delegate to a variety of logging implementations for processing the actual output. Below are configuration
examples for `Log4j 2`, `Commons Logging`, and `java.util.logging`.

<a id="logging--log4j-2-examples"></a>

### Log4j 2 Examples

The simplest way to [configure](https://logging.apache.org/log4j/2.x/manual/configuration.html) `Log4j 2` is via
a `log4j2.xml` file. `Log4j 2`
will [automatically](https://logging.apache.org/log4j/2.x/manual/configuration.html#AutomaticConfiguration) configure
itself using a file named `log4j2.xml` when it's present at the root of the application classpath.

Below are some `Log4j` configuration examples.

**Note:** The `Log4j 2` implementation a.k.a “core” is not included in the `HttpClient` distribution. You can include it
in your project using [Maven, Ivy, Gradle, or SBT](https://logging.apache.org/log4j/2.x/maven-artifacts.html).

- Enable header wire + context logging - **Best for Debugging**


```
<Configuration>
  <Appenders>
    <Console name="Console">
      <PatternLayout pattern="%d %-5level [%logger] %msg%n%xThrowable" />
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="org.apache.hc.client5.http" level="DEBUG">
      <AppenderRef ref="Console"/>
    </Logger>
    <Logger name="org.apache.hc.client5.http.wire" level="DEBUG">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="INFO">
      <AppenderRef ref="Console" />
    </Root>
  </Loggers>
</Configuration>
```

- Enable full wire + context logging


```
<Configuration>
  <Appenders>
    <Console name="Console">
      <PatternLayout pattern="%d %-5level [%logger] %msg%n%xThrowable" />
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="org.apache.hc.client5.http" level="DEBUG">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="INFO">
      <AppenderRef ref="Console" />
    </Root>
  </Loggers>
</Configuration>
```

- Enable context logging for connection management


```
<Configuration>
  <Appenders>
    <Console name="Console">
      <PatternLayout pattern="%d %-5level [%logger] %msg%n%xThrowable" />
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="org.apache.hc.client5.http.impl.io" level="DEBUG">
      <AppenderRef ref="Console"/>
    </Logger>
    <Logger name="org.apache.hc.client5.http.impl.nio" level="DEBUG">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="INFO">
      <AppenderRef ref="Console" />
    </Root>
  </Loggers>
</Configuration>
```

- Enable context logging for connection management / request execution


```
<Configuration>
  <Appenders>
    <Console name="Console">
      <PatternLayout pattern="%d %-5level [%logger] %msg%n%xThrowable" />
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="org.apache.hc.client5.http.impl" level="DEBUG">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="INFO">
      <AppenderRef ref="Console" />
    </Root>
  </Loggers>
</Configuration>
```

The `Log4J 2` manual is the best reference for how to configure `Log4J 2`. It is available at
<https://logging.apache.org/log4j/2.x/manual/>.

---

<a id="connection-management"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/connection-management.html -->

<!-- page_index: 6 -->

<a id="connection-management--connection-management"></a>

# Connection management

HttpClient reuses persistent connections to reduce latency and resource usage.
Connection management is handled by dedicated connection managers for classic
(blocking) and async I/O.

<a id="connection-management--connection-managers"></a>

## Connection managers

The main connection managers are:

- `PoolingHttpClientConnectionManager` (classic I/O)
- `PoolingAsyncClientConnectionManager` (async I/O)

Both managers:

- Maintain per-route and total connection limits.
- Reuse persistent connections when possible.
- Enforce connection time-to-live (TTL) and idle expiry.
- Provide APIs to close idle or expired connections explicitly.

For a detailed description of pooling policies see
[Connection pooling](#connection-pooling).

<a id="connection-management--per-route-and-total-limits"></a>

## Per-route and total limits

Connection limits are expressed in terms of:

- **Per-route limit** – maximum number of connections for a single `HttpRoute`.
- **Total limit** – maximum number of connections across all routes.

Classic:

```java
final PoolingHttpClientConnectionManager cm =
        PoolingHttpClientConnectionManagerBuilder.create()
                .setMaxConnTotal(200)
                .setMaxConnPerRoute(50)
                .build();
```

Async:

```java
final PoolingAsyncClientConnectionManager cm =
        PoolingAsyncClientConnectionManagerBuilder.create()
                .setMaxConnTotal(200)
                .setMaxConnPerRoute(50)
                .build();
```

These limits should reflect expected concurrency and the capacity of the remote
services and network.

<a id="connection-management--connection-lifetime-and-idle-timeout"></a>

## Connection lifetime and idle timeout

Connection lifetime (TTL) limits how long a persistent connection can be reused
regardless of its keep-alive semantics. Idle timeout limits how long a
connection may stay idle in the pool before being considered stale.

Both are configured via `ConnectionConfig`:

```java
final ConnectionConfig connectionConfig = ConnectionConfig.custom()
        .setTimeToLive(TimeValue.ofMinutes(5))
        .setIdleTimeout(TimeValue.ofMinutes(1))
        .build();
```

Classic:

```java
final PoolingHttpClientConnectionManager cm =
        PoolingHttpClientConnectionManagerBuilder.create()
                .setDefaultConnectionConfig(connectionConfig)
                .build();
```

Async:

```java
final PoolingAsyncClientConnectionManager cm =
        PoolingAsyncClientConnectionManagerBuilder.create()
                .setDefaultConnectionConfig(connectionConfig)
                .build();
```

Connections that exceed their TTL or idle timeout are discarded when leased or
by explicit eviction.

<a id="connection-management--evicting-idle-and-expired-connections"></a>

## Evicting idle and expired connections

Applications are encouraged to run a background task to evict idle and expired
connections from the pool.

Classic:

```java
cm.closeExpired();
cm.closeIdle(TimeValue.ofMinutes(1));
```

Async:

```java
asyncManager.closeExpired();
asyncManager.closeIdle(TimeValue.ofMinutes(1));
```

This keeps the pool clean in long-lived applications and reduces the probability
of using dead connections after long periods of inactivity.

<a id="connection-management--validation-after-inactivity"></a>

## Validation after inactivity

Persistent connections kept idle for a long time can become half-closed by
intermediaries (stale connections). HttpClient can validate such connections
before re-use based on a configurable inactivity threshold:

```java
final ConnectionConfig connectionConfig = ConnectionConfig.custom()
        .setValidateAfterInactivity(TimeValue.ofSeconds(2))
        .build();
```

When the inactivity period of a connection exceeds this threshold, the manager
will perform a lightweight `isStale()` check before leasing it.

- A small positive value (e.g. 1–2 seconds) is often a good compromise.
- A non-positive value disables validation and may increase the risk of
  encountering stale connections on the first request after a long idle period.

Classic and async managers both honour `validateAfterInactivity` when leasing
connections.

<a id="connection-management--concurrency-policies-and-off-lock-disposal"></a>

## Concurrency policies and off-lock disposal

Connection managers support different pool concurrency policies via
`PoolConcurrencyPolicy`:

- `STRICT` – per-route queues and strong fairness (default).
- `LAX` – relaxed fairness in favour of higher throughput.
- `OFFLOCK` – experimental route-segmented policy reducing contention on shared
  structures.

See [Connection pooling](#connection-pooling) for details and examples.

Blocking connection pools can optionally move slow graceful closes off the hot
pool locks:

```java
final PoolingHttpClientConnectionManager cm =
        PoolingHttpClientConnectionManagerBuilder.create()
                .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.STRICT)
                .setOffLockDisposalEnabled(true)
                .build();
```

With off-lock disposal enabled, removal from the pool happens immediately, while
the actual graceful close is performed outside the core pool synchronisation.

<a id="connection-management--practical-recommendations"></a>

## Practical recommendations

- Start with the default `STRICT` policy and conservative limits.
- Size `maxConnTotal` and `maxConnPerRoute` based on expected concurrency and
  backend capacity; monitor and adjust.
- Always run periodic eviction of idle and expired connections in long-lived
  applications.
- Enable `validateAfterInactivity` with a small positive value if connections
  are kept idle for extended periods.
- Consider `LAX` or `OFFLOCK` (experimental) for highly concurrent workloads
  where reducing contention is more important than strict per-route fairness.

---

<a id="connection-pooling"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/connection-pooling.html -->

<!-- page_index: 7 -->

<a id="connection-pooling--connection-pooling"></a>

# Connection pooling

HttpClient uses connection pools to reuse persistent connections between requests and reduce connection setup overhead.

The main pool implementations are:

- `PoolingHttpClientConnectionManager` for classic (blocking) I/O
- `PoolingAsyncClientConnectionManager` for async I/O

Both managers:

- Maintain per-route and total connection limits.
- Reuse idle persistent connections when possible.
- Enforce time-to-live (TTL) and idle expiry.

<a id="connection-pooling--pool-concurrency-policies"></a>

## Pool concurrency policies

The concurrency behaviour of the underlying pool is controlled by
`PoolConcurrencyPolicy`:

- **STRICT** (default)
  Per-route queues and strong fairness. Each route has its own waiter queue;
  connections are handed out in FIFO order per route. This is the safest choice
  for most applications.
- **LAX**
  More relaxed fairness in favour of throughput. Waiters share a global queue
  and busy routes can get more connections under load. This can improve
  utilisation at the cost of strict per-route fairness.
- **OFFLOCK** *(experimental)*
  Uses the route-segmented pool implementation (`RouteSegmentedConnPool`) which
  keeps per-route state in independent segments and reduces contention on shared
  structures. The implementation still uses locking where needed; the goal is
  to minimise time spent under hot pool locks. As an experimental policy its
  behaviour and configuration may change in future releases.

You can select the policy with the builder:

```java
final PoolingHttpClientConnectionManager connManager =
        PoolingHttpClientConnectionManagerBuilder.create()
                .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.OFFLOCK)
                .build();
```

<a id="connection-pooling--off-lock-disposal-blocking-pools"></a>

## Off-lock disposal (blocking pools)

Closing a connection gracefully can be slow (TLS shutdown, FIN/ACK, etc.). If
this work is done while holding internal pool locks, it can increase latency
for other threads leasing or releasing connections.

Blocking pools provide an option to move slow graceful closes *off* the hot
pool locks:

- Immediate closes (`CloseMode.IMMEDIATE`) are always executed on the caller
  thread.
- Graceful closes can be deferred and performed outside the core pool
  synchronisation.

This behaviour is enabled in the classic manager via:

```java
final PoolingHttpClientConnectionManager connManager =
        PoolingHttpClientConnectionManagerBuilder.create()
                .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.STRICT)
                .setOffLockDisposalEnabled(true)
                .build();
```

With off-lock disposal enabled:

- The connection is removed from the pool immediately.
- The actual graceful close is performed later, outside the critical sections
  used by `lease` / `release`.
- From the caller’s point of view, pool semantics (keep-alive, TTL, idle timeout)
  remain the same.

<a id="connection-pooling--configuration-hints"></a>

## Configuration hints

- Start with `STRICT` and default disposal behaviour.
- Consider `LAX` for high-throughput workloads where strict per-route fairness
  is not required.
- Consider `OFFLOCK` for highly concurrent applications with many routes and
  contention on the pool.
- Enable off-lock disposal for classic I/O if profiling shows slow graceful
  closes affecting lease/release latency under load.

---

<a id="async-compression"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/async-compression.html -->

<!-- page_index: 8 -->

<a id="async-compression--async-content-compression-decompression"></a>

# Async content compression & decompression

Starting with HttpClient 5.6 the async transport can transparently **compress**
request bodies and **decompress** response bodies. The logic lives in the
message-exchange layer, so application code keeps working with plain (already
decoded) entities.

<a id="async-compression--capabilities"></a>

## Capabilities

- Automatic `Accept-Encoding` negotiation when content compression is enabled
  and the request does not already carry this header.
- Transparent response decompression for `Content-Encoding` values
  `deflate`, `gzip`, and `x-gzip`.
- Optional support for `zstd` and `br` (Brotli) encodings when the
  corresponding libraries are present on the classpath.
- Streaming request compression via `DeflatingAsyncEntityProducer` and the
  codec-specific wrappers (for example `DeflatingGzipEntityProducer`).

<a id="async-compression--supported-codecs-and-dependencies"></a>

## Supported codecs and dependencies

Deflate and GZIP are available out of the box.

Zstandard and Brotli are only wired in when their optional dependencies are
present:

- **Zstandard** – `com.github.luben:zstd-jni`
- **Brotli** – `com.aayushatharva.brotli4j:brotli4j` (plus a matching
  `brotli4j-native` artefact for the target platform)

At runtime the async client checks the classpath and registers the extra codecs
without creating a hard dependency on either library.

<a id="async-compression--basic-usage-transparent-response-decompression"></a>

## Basic usage – transparent response decompression

By default async clients send an `Accept-Encoding` header and automatically
decode compressed responses before handing them to the application.
No extra code is required:

```java
try (final CloseableHttpAsyncClient client = HttpAsyncClients.createDefault()) {
    client.start();

    final SimpleHttpRequest request = SimpleRequestBuilder.get("https://httpbin.org/gzip")
            .build();

    final Future<Message<HttpResponse, String>> future = client.execute(
            SimpleRequestProducer.create(request),
            new BasicResponseConsumer<>(new StringAsyncEntityConsumer()),
            null);

    final Message<HttpResponse, String> message = future.get();
    System.out.println("status=" + message.getHead().getCode());
    System.out.println("body:\n" + message.getBody());
}
```

<a id="async-compression--mapping-codecs-to-examples"></a>

## Mapping codecs to examples

The async examples in the `org.apache.hc.client5.http.examples` package exercise
the same codecs that are registered in `ContentCompressionAsyncExec`:

```java
.register(ContentCoding.GZIP.token(),    InflatingGzipDataConsumer::new)
.register(ContentCoding.X_GZIP.token(),  InflatingGzipDataConsumer::new)
.register(ContentCoding.DEFLATE.token(), d -> new InflatingAsyncDataConsumer(d, null))

// Optional – only when the libraries are present
.register(ContentCoding.ZSTD.token(),    InflatingZstdDataConsumer::new)
.register(ContentCoding.BROTLI.token(),  InflatingBrotliDataConsumer::new);
```

The sections below link each `ContentCoding` token to a concrete runnable
example, in the same spirit as the Observation examples page.

<a id="async-compression--gzip-gzip-x-gzip"></a>

## GZIP (`gzip`, `x-gzip`)

- [AsyncClientGzipCompressionExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientGzipCompressionExample.java)

  Demonstrates streaming a request body compressed with **GZIP** using
  `DeflatingGzipEntityProducer`. The client sends a compressed POST while the
  async pipeline adds `Content-Encoding: gzip` automatically.
- [AsyncClientGzipDecompressionExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientGzipDecompressionExample.java)

  Demonstrates **transparent GZIP response decompression**. The server returns
  `Content-Encoding: gzip`, the async chain wraps the downstream consumer with
  `InflatingGzipDataConsumer`, and application code only sees the plain body.

These examples correspond directly to:

```java
.register(ContentCoding.GZIP.token(),   InflatingGzipDataConsumer::new)
.register(ContentCoding.X_GZIP.token(), InflatingGzipDataConsumer::new)
```

<a id="async-compression--deflate-deflate"></a>

## DEFLATE (`deflate`)

- [AsyncClientDeflateCompressionExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientDeflateCompressionExample.java)

  Demonstrates streaming a request body compressed with **deflate** using
  `DeflatingAsyncEntityProducer` wrapped around an arbitrary `AsyncEntityProducer`.
- [AsyncClientInflateDecompressionExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientInflateDecompressionExample.java)

  Demonstrates **transparent deflate response decompression**. When the server
  responds with `Content-Encoding: deflate`, the async execution chain wraps
  the downstream consumer in `InflatingAsyncDataConsumer`.

These examples correspond to:

```java
.register(ContentCoding.DEFLATE.token(), d -> new InflatingAsyncDataConsumer(d, null))
```

<a id="async-compression--zstandard-zstd"></a>

## Zstandard (`zstd`)

- [AsyncClientZstdCompressionExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientZstdCompressionExample.java)

  Shows streaming a request body compressed with **Zstandard** using
  `DeflatingZstdEntityProducer`, backed by the `zstd-jni` library.
- [AsyncClientServerZstdExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientServerZstdExample.java)

  End-to-end client/server demo where the classic server always responds with
  `Content-Encoding: zstd` and the async client transparently decodes it via
  `InflatingZstdDataConsumer`.

These examples correspond to the optional Zstandard decoder:

```java
.register(ContentCoding.ZSTD.token(), InflatingZstdDataConsumer::new)
```

<a id="async-compression--brotli-br"></a>

## Brotli (`br`)

- [AsyncClientServerBrotliRoundTrip](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientServerBrotliRoundTrip.java)

  Async client/server demo using **Brotli** in both directions:
  the client sends a Brotli-compressed request and the server responds with a
  Brotli-compressed body. The example uses `brotli4j` on the client side and
  Commons Compress for server-side decoding/encoding.

This example matches the optional Brotli decoder registration (and the extra
`Accept-Encoding: br` token):

```java
.register(ContentCoding.BROTLI.token(), InflatingBrotliDataConsumer::new);
// ...
tokens.add(ContentCoding.BROTLI.token());
```

Together, these examples show how each `ContentEncoding` registered in
`ContentCompressionAsyncExec` maps to a concrete usage pattern in the async
client.

---

<a id="android"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/android.html -->

<!-- page_index: 9 -->

<a id="android--httpclient-for-android"></a>

# HttpClient for Android

Apache HttpCLient 5.x is expected to work well with Android API 19 and newer.

There is a companion project [Android extensions](https://ok2c.github.io/httpclient-android-ext/) which is a third party
library that provides extra functionality simplifying application of Apache HttpClient on Google Android platform.

---

<a id="early-hints"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/early-hints.html -->

<!-- page_index: 10 -->

<a id="early-hints--103-early-hints-async"></a>

# 103 Early Hints (async)

HttpClient 5.6 adds async support for **103 Early Hints** via a callback interface:

- `EarlyHintsListener` – functional interface invoked for each `103` response.
- `HttpAsyncClientBuilder#setEarlyHintsListener(...)` – registers a global
  listener on the async client.
- `EarlyHintsAsyncExec` – internal exec-chain handler that taps informational
  responses without changing final response processing.

This allows applications to observe Early Hints (for example, `Link` headers
with `rel=preload` / `rel=preconnect`) while leaving the normal response path
untouched.

<a id="early-hints--when-is-the-listener-called"></a>

## When is the listener called?

- Called **once per `103`** informational response.
- Never called for the final non-1xx response.
- May be called **multiple times** for a single request if the server sends
  multiple `103` responses.
- Runs on the I/O thread, so implementations must be **fast and non-blocking**;
  offload heavier work to your own executor.

<a id="early-hints--api-surface"></a>

## API surface

The public entry point is the listener:

```java
@FunctionalInterface
public interface EarlyHintsListener {

    void onEarlyHints(HttpResponse hints, HttpContext context)
            throws HttpException, IOException;
}
```

You register it on the async client builder:

```java
final EarlyHintsListener listener = (hints, ctx) -> {
    // Only 103s will be forwarded here
    System.out.println("Early Hints: " + hints.getCode());
    for (final Header h : hints.getHeaders("Link")) {
        System.out.println("  Link: " + h.getValue());
    }
};

final CloseableHttpAsyncClient client = HttpAsyncClients.custom()
        .setEarlyHintsListener(listener)
        .build();
```

If the listener is `null` no extra handler is added to the exec chain.

<a id="early-hints--minimal-usage-example"></a>

## Minimal usage example

This is a cut-down version of the `AsyncClientEarlyHintsEndToEnd` example. It
shows how to register the listener and consume the final response as usual.

```java
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

import org.apache.hc.client5.http.EarlyHintsListener;
import org.apache.hc.client5.http.async.methods.SimpleHttpRequest;
import org.apache.hc.client5.http.async.methods.SimpleHttpResponse;
import org.apache.hc.client5.http.async.methods.SimpleRequestBuilder;
import org.apache.hc.client5.http.impl.async.CloseableHttpAsyncClient;
import org.apache.hc.client5.http.impl.async.HttpAsyncClients;
import org.apache.hc.core5.http.Header;

public class AsyncClientEarlyHintsExample {

    public static void main(final String[] args) throws Exception {
        final EarlyHintsListener hintsListener = (hints, ctx) -> {
            System.out.println("[client] 103 Early Hints:");
            for (final Header h : hints.getHeaders("Link")) {
                System.out.println("  " + h.getValue());
            }
        };

        try (final CloseableHttpAsyncClient client = HttpAsyncClients.custom()
                .setEarlyHintsListener(hintsListener)
                .build()) {

            client.start();

            final SimpleHttpRequest req = SimpleRequestBuilder
                    .get("https://example.com/with-early-hints")
                    .build();

            final Future<SimpleHttpResponse> f = client.execute(req, null);
            final SimpleHttpResponse resp = f.get(10, TimeUnit.SECONDS);

            System.out.println("[client] final: " + resp.getCode() + " " + resp.getReasonPhrase());
            System.out.println("[client] body: " + resp.getBodyText());
        }
    }
}
```

Notes:

- The **final response** (e.g. `200 OK`) is handled by the normal async flow.
- Early Hints are purely **side-band** notifications.

<a id="early-hints--end-to-end-example"></a>

## End-to-end example

The full end-to-end demo lives in the examples package:

- [AsyncClientEarlyHintsEndToEnd](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientEarlyHintsEndToEnd.java)

This example:

1. Starts a local async HTTP server that:
   - sends one `103 Early Hints` with two `Link` headers, then
   - completes the exchange with `200 OK` and a short body.
2. Builds an async client with `setEarlyHintsListener(...)`.
3. Prints:
   - all `Link` headers from `103` responses, and
   - the final status and body for the main response.

This is the canonical reference for wiring Early Hints support end-to-end.

<a id="early-hints--interaction-with-the-exec-chain"></a>

## Interaction with the exec chain

When `setEarlyHintsListener(...)` is used, the builder inserts an internal
`EarlyHintsAsyncExec` handler **before** the protocol handler:

```java
if (earlyHintsListener != null) {
    addExecInterceptorBefore(
            ChainElement.PROTOCOL.name(),
            "early-hints",
            new EarlyHintsAsyncExec(earlyHintsListener));
}
```

This handler:

- intercepts `handleInformationResponse(...)` callbacks,
- forwards each `103` to the listener,
- delegates all other informational responses and the final response unchanged.

If you never register a listener, no extra handler is added and the async exec
chain behaves as before.

<a id="early-hints--summary"></a>

## Summary

- Use `EarlyHintsListener` + `setEarlyHintsListener(...)` to observe `103` responses.
- Normal response processing is unaffected; Early Hints are side-band.
- Keep listener logic lightweight; bounce heavy work to your own executor.
- Use `AsyncClientEarlyHintsEndToEnd` as a reference for testing and wiring.

---

<a id="observation"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/observation.html -->

<!-- page_index: 11 -->

<a id="observation--observability-micrometer-opentelemetry"></a>

# Observability (Micrometer / OpenTelemetry)

Since **5.6**, HttpClient ships an **optional** module, `httpclient5-observation`, that plugs straight into
**Micrometer** (metrics + observations) and can bridge to **OpenTelemetry** (traces). The goal is simple:
give you **drop-in visibility** of latency, throughput, I/O, connection-pool health, DNS, and TLS—without
rewriting application code or coupling the core client to any monitoring stack.

What you get out of the box:

- Request latency **timers** and response **counters** for classic and async clients
- Request/response **I/O byte** counters (opt-in URI tagging to control cardinality)
- Connection pool **gauges** (leased / available / pending) for classic and async managers
- **DNS** resolution timers/counters (resolve + canonical lookups)
- **TLS** handshake timers/counters (ok / error / cancel outcomes)
- Micrometer **Observation** interceptors that you can bridge to OpenTelemetry for end-to-end traces

How it fits:

- **Opt-in by design.** Nothing changes unless you add Micrometer to the classpath and call the provided
  `enable(...)` helpers. The observation module is separate; core HttpClient has no hard dependency.
- **Classic, Async, and Caching** are all supported. For caching builders, interceptors are inserted **after**
  the caching stage so metrics reflect the effective exchange.
- **Low friction.** A single call wires timers/counters and, if you want them, pool gauges, DNS/TLS meters,
  and observation spans. You keep full control via two small configs:
  - `ObservingOptions` – choose metric groups (BASIC, IO, CONN\_POOL, TLS, DNS), tag level (`LOW` for minimal,
    `EXTENDED` for richer tags), per-URI sampling, and a tag customizer hook.
  - `MetricConfig` – set the metric name prefix (`http.client` by default), SLO bucket(s), percentiles, optional
    per-URI I/O tagging, and common tags to stamp on every meter.
- **Safe by default.** Per-URI I/O tagging is **off** to avoid high cardinality. Turn it on only where you know
  it’s useful (e.g., controlled path templates).
- **Thread-safe & lightweight.** The helpers are stateless. Interceptors register meters lazily, and pool gauges
  bind once to the connection manager (no reflection).
- **Your registry, your rules.** Use any Micrometer registry (Prometheus, OTLP, Cloud vendor). If you also enable
  `ObservationRegistry` with Micrometer Tracing, you can export **spans** via `micrometer-tracing-bridge-otel`.

Typical flow:

1. Add `httpclient5-observation` and whichever Micrometer bits you actually use (all Micrometer deps can stay `optional`).
2. Build your client as usual; call `HttpClientObservationSupport.enable(...)` on the builder
   (classic/async/caching variants provided).
3. (Optional) Bind **pool gauges** after you’ve attached a pooling connection manager.
4. (Optional) Wrap your DNS resolver with `MeteredDnsResolver` and your TLS strategy with `MeteredTlsStrategy`
   if you want those timing/outcome meters as well.
5. (Optional) Bridge the `ObservationRegistry` to OpenTelemetry to get client spans alongside metrics.

Practical notes:

- **Naming:** all meters are prefixed by `MetricConfig.prefix` (default `http.client`). Examples:
  `http.client.request` (timer), `http.client.response` (counter), `http.client.inflight{kind=classic|async}` (gauge),
  `http.client.pool.*` (gauges), `http.client.dns.*`, `http.client.tls.*`.
- **Tagging:** minimal set is `method` and `status`. `EXTENDED` adds `protocol` and `target`; DNS/TLS add `host`/`sni`.
  You can append `commonTags` globally and mutate per-request tags with a `TagCustomizer`.
- **Overhead:** the fast path short-circuits when `spanSampling` says “skip” (no timer/counter work). Publishing
  percentiles and fine-grained SLOs costs more—configure only what you need.
- **Compatibility:** works with existing client code; you instrument the **builder**, not call sites. Suitable for
  libraries: you can expose an instrumented `CloseableHttpClient`/`CloseableHttpAsyncClient` to callers without
  leaking Micrometer types into their APIs.

Nothing is enabled unless you add Micrometer and call the opt-in helpers.

> **Status:** Introduced in 5.6 (`@since 5.6`). Artifacts are optional; core modules do not depend on Micrometer/OTel.

---

<a id="observation--dependency"></a>

## Dependency

**Maven**

````xml
<dependency>
  <groupId>org.apache.httpcomponents.client5</groupId>
  <artifactId>httpclient5-observation</artifactId>
  <version>5.6-alpha1</version>
</dependency>

## Dependency

**Maven**

```xml
<!-- Required: the optional observability module itself -->
<dependency>
  <groupId>org.apache.httpcomponents.client5</groupId>
  <artifactId>httpclient5-observation</artifactId>
  <version>5.6-alpha1</version>
</dependency>

<!-- Optional: add only if you actually use Micrometer metrics / observations / Prometheus / tracing -->

<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-core</artifactId>
  <version>${micrometer.version}</version>
  <optional>true</optional>
</dependency>

<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-observation</artifactId>
  <version>${micrometer.version}</version>
  <optional>true</optional>
</dependency>

<!-- Choose one or more registries you use (e.g., Prometheus) -->
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-registry-prometheus</artifactId>
  <version>${micrometer.version}</version>
  <optional>true</optional>
</dependency>

<!-- Optional Micrometer→OpenTelemetry bridge for tracing spans -->
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-tracing-bridge-otel</artifactId>
  <version>${micrometer.tracing.version}</version>
  <optional>true</optional>
</dependency>
````

---

<a id="scram-sha-256"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/scram-sha-256.html -->

<!-- page_index: 12 -->

<a id="scram-sha-256--scram-sha-256-authentication"></a>

# SCRAM-SHA-256 authentication

HttpClient 5.6 adds support for **SCRAM-SHA-256** as defined by
[RFC 7804] and [RFC 7677]. The scheme is exposed as:

- `StandardAuthScheme.SCRAM_SHA_256` (scheme name `"SCRAM-SHA-256"`)
- `ScramSchemeFactory` (client-side implementation)
- `ScramException` (specialised `AuthenticationException` for SCRAM errors)

The default async and classic client builders register the scheme alongside
existing ones (Basic, Digest, Bearer), so that it can be selected through the
normal HTTP authentication negotiation process.

<a id="scram-sha-256--why-scram"></a>

## Why SCRAM?

SCRAM is a challenge-response mechanism that:

- avoids sending the plaintext password over the wire,
- supports salted password storage on the server,
- offers channel binding variants when used over TLS (not covered here),
- is widely deployed in modern services (databases, HTTP gateways, etc.).

Compared to `Basic`, SCRAM provides much stronger protection for credentials
and server-side password databases. Compared to legacy `Digest`, it has a
cleaner design and better password hashing support.

<a id="scram-sha-256--scheme-name"></a>

## Scheme name

The wire-level auth scheme name is:

```text
SCRAM-SHA-256
```

In code, use the constant from `StandardAuthScheme`:

```java
StandardAuthScheme.SCRAM_SHA_256
```

<a id="scram-sha-256--enabling-scram-sha-256"></a>

## Enabling SCRAM-SHA-256

The default builders already register the scheme:

```java
Lookup<AuthSchemeFactory> authSchemeRegistry = RegistryBuilder.<AuthSchemeFactory>create()
        .register(StandardAuthScheme.BASIC,  BasicSchemeFactory.INSTANCE)
        .register(StandardAuthScheme.DIGEST, DigestSchemeFactory.INSTANCE)
        .register(StandardAuthScheme.BEARER, BearerSchemeFactory.INSTANCE)
        .register(StandardAuthScheme.SCRAM_SHA_256, ScramSchemeFactory.INSTANCE)
        .build();
```

If you build your own registry, make sure to add the SCRAM factory as above.

<a id="scram-sha-256--classic-client-example"></a>

## Classic client example

The following snippet shows a typical setup with `CloseableHttpClient` where
the target server advertises `WWW-Authenticate: SCRAM-SHA-256` and the client
responds with the appropriate `Authorization` header.

```java
import org.apache.hc.client5.http.auth.AuthScope;
import org.apache.hc.client5.http.auth.StandardAuthScheme;
import org.apache.hc.client5.http.auth.UsernamePasswordCredentials;
import org.apache.hc.client5.http.impl.auth.ScramSchemeFactory;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.client5.http.impl.auth.BasicCredentialsProvider;
import org.apache.hc.core5.http.io.support.ClassicRequestBuilder;
import org.apache.hc.core5.http.ClassicHttpResponse;

public class ClassicScramExample {

    public static void main(final String[] args) throws Exception {
        final BasicCredentialsProvider credsProvider = new BasicCredentialsProvider();
        credsProvider.setCredentials(
                new AuthScope("example.com", 443),
                new UsernamePasswordCredentials("user", "p4ssw0rd".toCharArray()));

        try (final CloseableHttpClient client = HttpClients.custom()
                // SCRAM-SHA-256 is included by default; explicit registration shown for clarity
                .setDefaultCredentialsProvider(credsProvider)
                .build()) {

            final ClassicHttpResponse response = client.executeOpen(null,
                    ClassicRequestBuilder.get("https://example.com/protected").build(),
                    null);

            System.out.println(response.getCode() + " " + response.getReasonPhrase());
        }
    }
}
```

As long as the server prefers `SCRAM-SHA-256` in `WWW-Authenticate`, the
`DefaultAuthenticationStrategy` will select it and the `ScramSchemeFactory`
will drive the handshake.

<a id="scram-sha-256--async-client-example"></a>

## Async client example

For the async API, configuration is similar: register credentials and let the
auth strategy select SCRAM when the server advertises it.

```java
import java.util.concurrent.Future;

import org.apache.hc.client5.http.auth.AuthScope;
import org.apache.hc.client5.http.auth.UsernamePasswordCredentials;
import org.apache.hc.client5.http.async.methods.SimpleHttpRequest;
import org.apache.hc.client5.http.async.methods.SimpleHttpResponse;
import org.apache.hc.client5.http.async.methods.SimpleRequestBuilder;
import org.apache.hc.client5.http.impl.async.CloseableHttpAsyncClient;
import org.apache.hc.client5.http.impl.async.HttpAsyncClients;
import org.apache.hc.client5.http.impl.auth.BasicCredentialsProvider;

public class AsyncScramExample {

    public static void main(final String[] args) throws Exception {
        final BasicCredentialsProvider credsProvider = new BasicCredentialsProvider();
        credsProvider.setCredentials(
                new AuthScope("example.com", 443),
                new UsernamePasswordCredentials("user", "p4ssw0rd".toCharArray()));

        try (final CloseableHttpAsyncClient client = HttpAsyncClients.custom()
                .setDefaultCredentialsProvider(credsProvider)
                .build()) {

            client.start();

            final SimpleHttpRequest request = SimpleRequestBuilder
                    .get("https://example.com/protected")
                    .build();

            final Future<SimpleHttpResponse> future = client.execute(request, null);
            final SimpleHttpResponse response = future.get();

            System.out.println(response.getCode() + " " + response.getReasonPhrase());
        }
    }
}
```

If the server supports both SCRAM and weaker schemes, you can influence the
selection order via a custom `AuthenticationStrategy` if needed.

<a id="scram-sha-256--error-handling"></a>

## Error handling

SCRAM-specific problems (bad server messages, invalid channel binding, etc.)
are reported as `ScramException`, which extends `AuthenticationException`:

```java
try {
    // execute request…
} catch (final ScramException ex) {
    // SCRAM handshake failed (protocol-level issue)
} catch (final AuthenticationException ex) {
    // generic auth failure
}
```

<a id="scram-sha-256--operational-notes"></a>

## Operational notes

- SCRAM-SHA-256 should normally be used over **TLS** (`https:`) to protect the
  rest of the HTTP exchange.
- The server must implement RFC 7804 / 7677 correctly; misconfigured servers
  may fall back to other schemes or fail the handshake.
- Credentials are provided through the standard HttpClient
  `CredentialsProvider` mechanism; there is no SCRAM-specific credential type
  for the common username/password case.

<a id="scram-sha-256--summary"></a>

## Summary

- Scheme name: `SCRAM-SHA-256` (`StandardAuthScheme.SCRAM_SHA_256`).
- Registered on both classic and async clients through `ScramSchemeFactory`.
- Negotiated via the usual HTTP auth challenge/response flow.
- Use `UsernamePasswordCredentials` + `CredentialsProvider` as with other
  built-in schemes; HttpClient handles the SCRAM details.

---

<a id="spki-pinning"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/spki-pinning.html -->

<!-- page_index: 13 -->

<a id="spki-pinning--spki-pinning-tls-strategy"></a>

# SPKI pinning TLS strategy

HttpClient 5.6 adds an **opt-in SPKI pinning TLS strategy** for clients that
need an additional defence layer on top of the normal PKI and hostname
verification.

The implementation lives in:

- `org.apache.hc.client5.http.ssl.SpkiPinningClientTlsStrategy`

and is used as a drop-in replacement for the regular client-side TLS strategy
in both classic and async connection managers.

> :warning: **Warning:** Certificate pinning increases operational risk.
> Misconfigured pins can brick your client fleet until you ship an update.
> Always keep normal PKI and hostname verification enabled, and ship at least
> one backup pin for each host.

<a id="spki-pinning--what-is-pinned"></a>

## What is pinned?

Pins are applied to the **SubjectPublicKeyInfo (SPKI)** of certificates in the
peer chain, not to raw certificate bytes.

Each pin has the form:

```text
sha256/<base64(SPKI)>
```

For example:

```text
sha256/qrvdF0L7Kp5l3H8k0m3x7VZq3p5O6s4L4kC2Z7tZt+Q=
```

Only `sha256/…` pins are accepted. Any other prefix, invalid Base64, or wrong
decoded length (not 32 bytes) will cause an `IllegalArgumentException` during
builder configuration.

<a id="spki-pinning--host-patterns-and-wildcards"></a>

## Host patterns and wildcards

Pins are configured per **host pattern**, which can be:

- an exact host (for example `api.example.com`), or
- a **single-label wildcard** (for example `*.example.com`).

Behaviour:

- Host names are normalised to IDNA ASCII (Punycode) and lowercased.
- `*.example.com` matches `a.example.com`, `b.example.com`, etc.
- `*.example.com` does **not** match `a.b.example.com`.
- Wildcards must be single-label; patterns like `"*."` are rejected.

<a id="spki-pinning--how-enforcement-works"></a>

## How enforcement works

`SpkiPinningClientTlsStrategy` decorates the default client TLS strategy:

1. The normal trust manager and hostname verification run first.
2. If neither of those fails, pinning logic is applied:
   - It finds all rules whose host pattern matches the target host.
   - It computes `SHA-256(SPKI)` for all `X509Certificate` entries in the peer
     chain.
   - If at least one configured pin matches at least one SPKI hash, pinning
     passes.
   - Otherwise an `SSLException` is thrown and the connection fails.

If no rules match the host, pinning is **skipped** and only normal PKI rules
apply.

<a id="spki-pinning--classic-client-configuration"></a>

## Classic client configuration

To enable SPKI pinning for the classic (`CloseableHttpClient`) API, plug the
strategy into a `PoolingHttpClientConnectionManager`:

```java
import javax.net.ssl.SSLContext;

import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.client5.http.impl.io.PoolingHttpClientConnectionManager;
import org.apache.hc.client5.http.impl.io.PoolingHttpClientConnectionManagerBuilder;
import org.apache.hc.client5.http.ssl.SpkiPinningClientTlsStrategy;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.message.StatusLine;
import org.apache.hc.core5.ssl.SSLContexts;

public final class ClientSpkiPinningExample {

    public static void main(final String[] args) throws Exception {
        final SSLContext sslContext = SSLContexts.createSystemDefault();

        final SpkiPinningClientTlsStrategy pinning = SpkiPinningClientTlsStrategy
                .newBuilder(sslContext)
                // Replace these with real host(s) and real pins (sha256/<base64(SPKI)>)
                .add("example.com",
                        "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
                        "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=") // backup
                .add("*.example.net",
                        "sha256/CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC=")
                .build();

        final PoolingHttpClientConnectionManager cm =
                PoolingHttpClientConnectionManagerBuilder.create()
                        .setTlsSocketStrategy(pinning)
                        .build();

        try (final CloseableHttpClient httpclient = HttpClients.custom()
                .setConnectionManager(cm)
                .build()) {

            final HttpGet httpget = new HttpGet("https://example.com/");
            System.out.println("Executing: " + httpget.getMethod() + " " + httpget.getUri());

            httpclient.execute(httpget, response -> {
                System.out.println("----------------------------------------");
                System.out.println(httpget + " -> " + new StatusLine(response));
                EntityUtils.consume(response.getEntity());
                return null;
            });
        }
    }
}
```

If the peer certificate chain does not contain any of the configured pins for
`example.com`, the TLS handshake will fail with an `SSLException` explaining
which pins were configured and which SPKI hashes were observed.

<a id="spki-pinning--async-client-configuration"></a>

## Async client configuration

For the async client (`CloseableHttpAsyncClient`) the approach is analogous, but you plug the strategy into `PoolingAsyncClientConnectionManagerBuilder`:

```java
import javax.net.ssl.SSLContext;

import org.apache.hc.client5.http.async.methods.SimpleHttpRequest;
import org.apache.hc.client5.http.async.methods.SimpleHttpResponse;
import org.apache.hc.client5.http.async.methods.SimpleRequestBuilder;
import org.apache.hc.client5.http.impl.async.CloseableHttpAsyncClient;
import org.apache.hc.client5.http.impl.async.HttpAsyncClients;
import org.apache.hc.client5.http.impl.nio.PoolingAsyncClientConnectionManager;
import org.apache.hc.client5.http.impl.nio.PoolingAsyncClientConnectionManagerBuilder;
import org.apache.hc.client5.http.ssl.SpkiPinningClientTlsStrategy;
import org.apache.hc.core5.http.HttpHost;
import org.apache.hc.core5.http.nio.support.BasicRequestProducer;
import org.apache.hc.core5.http.nio.support.BasicResponseConsumer;
import org.apache.hc.core5.http.nio.entity.StringAsyncEntityConsumer;
import org.apache.hc.core5.reactor.IOReactorConfig;
import org.apache.hc.core5.util.Timeout;
import org.apache.hc.core5.ssl.SSLContexts;

public final class AsyncSpkiPinningExample {

    public static void main(final String[] args) throws Exception {
        final SSLContext sslContext = SSLContexts.createSystemDefault();

        final SpkiPinningClientTlsStrategy pinning = SpkiPinningClientTlsStrategy
                .newBuilder(sslContext)
                .add("api.example.com",
                        "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
                        "sha256/BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=")
                .build();

        final PoolingAsyncClientConnectionManager cm =
                PoolingAsyncClientConnectionManagerBuilder.create()
                        .setTlsStrategy(pinning)
                        .setIoReactorConfig(IOReactorConfig.custom()
                                .setSoTimeout(Timeout.ofSeconds(5))
                                .build())
                        .build();

        try (final CloseableHttpAsyncClient client = HttpAsyncClients.custom()
                .setConnectionManager(cm)
                .build()) {

            client.start();

            final SimpleHttpRequest request = SimpleRequestBuilder
                    .get("https://api.example.com/data")
                    .build();

            final SimpleHttpResponse response = client.execute(
                    HttpHost.create("https://api.example.com"),
                    new BasicRequestProducer(request, null),
                    new BasicResponseConsumer<>(new StringAsyncEntityConsumer()),
                    null).get();

            System.out.println(response.getCode() + " " + response.getReasonPhrase());
        }
    }
}
```

(Adjust host, pins and request details to your environment.)

<a id="spki-pinning--failure-modes"></a>

## Failure modes

- **Pinning failure**: if no configured pin matches any SPKI in the peer
  chain, `SpkiPinningClientTlsStrategy` throws an `SSLException` with a
  message containing:
  - the computed peer pins, and
  - the configured pins for the matching rules.
- **Configuration errors** (invalid Base64, wrong length, invalid wildcard,
  empty pin list, etc.) are signalled as `IllegalArgumentException` at build
  time.
- **No matching rules**: pinning is skipped and only the normal trust /
  hostname checks apply.

<a id="spki-pinning--testing-and-reference-implementation"></a>

## Testing and reference implementation

The behaviour of `SpkiPinningClientTlsStrategy` is covered by:

- [ClientSpkiPinningExample](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientSpkiPinningExample.java)
- [SpkiPinningClientTlsStrategyTest](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/ssl/SpkiPinningClientTlsStrategyTest.java)

These tests validate:

- exact host and wildcard matches,
- IDN normalisation (`bücher.example`),
- backup pins,
- invalid or missing pins,
- cases where no rules apply and pinning is bypassed.

<a id="spki-pinning--summary"></a>

## Summary

- Opt-in, immutable TLS strategy for SPKI pinning: `SpkiPinningClientTlsStrategy`.
- Pins are `sha256/<base64(SPKI)>` over `SubjectPublicKeyInfo`.
- Supports exact hosts and single-label wildcards with IDN handling.
- Applied **after** normal PKI and hostname verification.
- Integrates with both classic and async connection managers.

---

<a id="examples"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/examples.html -->

<!-- page_index: 14 -->

<a id="examples--httpclient-examples-classic"></a>

# HttpClient Examples (Classic)

- [Response handling](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientResponseProcessing.java)

  This example demonstrates how to process HTTP responses using a response handler. This is the recommended way of
  executing HTTP requests and processing HTTP responses. This approach enables the caller to concentrate on the process
  of digesting HTTP responses and to delegate the task of system resource deallocation to HttpClient. The use of an HTTP
  response handler guarantees that the underlying HTTP connection will be released back to the connection manager
  automatically in all cases.
- [Manual connection release](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientConnectionRelease.java)

  This example demonstrates how to ensure the release of the underlying HTTP connection back to the connection manager
  in case of a manual processing of HTTP responses.
- [HttpClient configuration](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientConfiguration.java)

  This example demonstrates how to customize and configure the most common aspects of HTTP request execution and
  connection management.
- [Request execution interceptors](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientInterceptors.java)

  This example demonstrates how to insert custom request interceptor and an execution interceptor to the request
  execution chain.
- [Classic APIs over async HttpClient](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientClassicOverAsync.java)

  This example demonstrates create a classic HttpClient adaptor over an async HttpClient providing compatibility
  with the classic APIs based on the InputStream / OutputStream model.
- [Abort method](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientAbortMethod.java)

  This example demonstrates how to abort an HTTP request before its normal completion.
- [Client authentication](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientAuthentication.java)

  This example uses HttpClient to execute an HTTP request against a target site that requires user authentication.
- [Request via a proxy](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientExecuteProxy.java)

  This example demonstrates how to send an HTTP request via a proxy.
- [Proxy authentication](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientProxyAuthentication.java)

  A simple example showing execution of an HTTP request over a secure connection tunneled through an authenticating
  proxy.
- [Chunk encoded POST](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientChunkEncodedPost.java)

  This example shows how to stream out a request entity using chunk encoding.
- [Custom execution context](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientCustomContext.java)

  This example demonstrates the use of a local HTTP context populated custom attributes.
- [Form based logon](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientFormLogin.java)

  This example demonstrates how HttpClient can be used to perform form-based logon.
- [Threaded request execution](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientMultiThreadedExecution.java)

  An example that executes HTTP requests from multiple worker threads.
- [Custom SSL context](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientCustomSSL.java)

  This example demonstrates how to create secure connections with a custom SSL context.
- [Connection / TLS configuation per route / host](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientConnectionConfig.java)

  This example demonstrates how to use connection configuration on a per-route or a per-host basis.
- [Preemptive BASIC authentication](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientPreemptiveBasicAuthentication.java)

  This example shows how HttpClient can be customized to authenticate preemptively using BASIC scheme. Generally,
  preemptive authentication can be considered less secure than a response to an authentication challenge and therefore
  discouraged.
- [Preemptive DIGEST authentication](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientPreemptiveDigestAuthentication.java)

  This example shows how HttpClient can be customized to authenticate preemptively using DIGEST scheme. Generally,
  preemptive authentication can be considered less secure than a response to an authentication challenge and therefore
  discouraged.
- [Proxy tunnel](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ProxyTunnelDemo.java)

  This example shows how to use ProxyClient in order to establish a tunnel through an HTTP proxy for an arbitrary
  protocol.
- [Multipart encoded request entity](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientMultipartFormPost.java)

  This example shows how to execute requests enclosing a multipart encoded entity.
- [Connection endpoint details](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientRemoteEndpointDetails.java)

  This example demonstrates how to get details of the underlying connection endpoint.
- [Virtual HTTPS / SNI](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/ClientSNI.java)

  This example demonstrates how to use SNI to send requests to a virtual HTTPS endpoint using the classic I/O.
- [HTTP/2 Priority (RFC 9218)](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-h2/src/test/java/org/apache/hc/core5/http2/examples/ClassicH2PriorityExample.java)

  Demonstrates emitting the RFC 9218 Priority request header (u / i) via H2RequestPriority and context. Requires HTTP/2 and H2Processors.client() (which includes the interceptor).
- [Unix domain sockets](https://github.com/apache/httpcomponents-client/blob/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/UnixDomainSocket.java)

  This example demonstrates how to connect to a local daemon (in this case, the Docker daemon) over a Unix domain socket. Note that this requires either Java 17+ or a dependency on [JUnixSocket](https://mvnrepository.com/artifact/com.kohlschutter.junixsocket/junixsocket-core).

---

<a id="examples-async"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/examples-async.html -->

<!-- page_index: 15 -->

<a id="examples-async--httpclient-examples-async"></a>

# HttpClient Examples (Async)

- [Asynchronous HTTP exchange](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientHttpExchange.java)

  This example demonstrates a basic asynchronous HTTP request / response exchange. Response content is buffered in
  memory for simplicity.
- [Asynchronous HTTP exchange with content streaming](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientHttpExchangeStreaming.java)

  This example demonstrates an asynchronous HTTP request / response exchange with a full content streaming.
- [Pipelined HTTP/1.1 exchanges](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientHttp1Pipelining.java)

  This example demonstrates a pipelined execution of multiple HTTP/1.1 request / response exchanges. Response content is
  buffered in memory for simplicity.
- [Multiplexed HTTP/2 exchanges](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientH2Multiplexing.java)

  This example demonstrates a multiplexed execution of multiple HTTP/2 request / response exchanges. Response content is
  buffered in memory for simplicity.
- [Request execution interceptors](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientInterceptors.java)

  This example demonstrates how to insert custom request interceptor and an execution interceptor to the request
  execution chain.
- [Message trailers](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientMessageTrailers.java)

  This example demonstrates how to use a custom execution interceptor to add trailers to all outgoing request enclosing
  an entity..
- [Multiplexed HTTP/2 exchanges](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientHttp2ServerPush.java)

  This example demonstrates handling of HTTP/2 message exchanges pushed by the server.
- [Client authentication](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientAuthentication.java)

  This example demonstrates execution of an HTTP request against a target site that requires user authentication.
- [Custom SSL context](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientCustomSSL.java)

  This example demonstrates how to create secure connections with a custom SSL context.
- [Connection / TLS configuation per route / host](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientConnectionConfig.java)

  This example demonstrates how to use connection configuration on a per-route or a per-host basis.
- [Connection eviction](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientConnectionEviction.java)

  This example demonstrates how to evict expired and idle connections from the connection pool.
- [Preemptive BASIC authentication](https://github.com/apache/httpcomponents-client/blob/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncPreemptiveBasicClientAuthentication.java)

  This example shows how HttpClient can be customized to authenticate preemptively using BASIC scheme. Generally,
  preemptive authentication can be considered less secure than a response to an authentication challenge and therefore
  discouraged.
- [HTTP version negotiation](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientHttpVersionPolicy.java)

  This example demonstrates how to make HttpClient negotiate or force a particular version of HTTP protocol during
  the TLS handshake. Please note that protocol version policy setting also applies to non-HTTPS connections.
- [Virtual HTTPS / SNI](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientSNI.java)

  This example demonstrates how to use SNI to send requests to a virtual HTTPS endpoint using the async I/O.
- [Unix domain sockets](https://github.com/apache/httpcomponents-client/blob/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/UnixDomainSocketAsync.java)

  This example demonstrates how to connect to a local daemon (in this case, the Docker daemon) over a Unix domain socket. Note that this requires Java 17+. On older versions of Java, Unix domain sockets are only supported with [classic I/O](#examples) and require an additional dependency on JUnixSocket.

---

<a id="examples-reactive"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/examples-reactive.html -->

<!-- page_index: 16 -->

<a id="examples-reactive--httpclient-examples-reactive-streams"></a>

# HttpClient Examples (Reactive Streams)

- [HTTP exchange with Reactive Streams](https://github.com/apache/httpcomponents-client/tree/master/httpclient5/src/test/java/org/apache/hc/client5/http/examples/AsyncClientHttpExchange.java)

  This example demonstrates a reactive, full-duplex HTTP/1.1 message exchange using RxJava.

---

<a id="examples-observation"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/examples-observation.html -->

<!-- page_index: 17 -->

<a id="examples-observation--httpclient-examples-observation"></a>

# HttpClient Examples (Observation)

- [Observability quick start (classic)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/ClassicWithMetricConfigDemo.java)

  This example demonstrates enabling Micrometer observations and metrics on a classic client using `HttpClientObservationSupport.enable(...)`, with a custom `MetricConfig` (prefix, SLO, percentiles) and a Prometheus scrape.
- [Observability quick start (async)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/AsyncMetricsDemo.java)

  This example demonstrates enabling observations and metrics on the async client, firing concurrent requests to show the `http.client.inflight{kind=async}` gauge and printing a Prometheus scrape.
- [Connection pool gauges (classic)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/PoolGaugesDemo.java)

  This example demonstrates exposing connection pool gauges (`<prefix>.pool.leased`, `<prefix>.pool.available`, `<prefix>.pool.pending`) by binding a pooling manager via `ConnPoolMeters.bindTo(...)`.
- [DNS metrics (classic)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/DnsMetricsDemo.java)

  This example demonstrates wrapping the system DNS resolver with `MeteredDnsResolver` to record resolution timers and counters for `resolve` and `resolveCanonicalHostname` with `result` and optional `host` tags.
- [TLS handshake metrics (async)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/TlsMetricsDemo.java)

  This example demonstrates recording TLS handshake latency and outcome counters by wrapping an async `TlsStrategy` with `MeteredTlsStrategy` on the connection manager (`<prefix>.tls.handshake`, `<prefix>.tls.handshakes`).
- [Span sampling & I/O counters](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/SpanSamplingDemo.java)

  This example demonstrates using `ObservingOptions.spanSampling` to skip observations/metrics for selected URIs and recording request/response byte counters (`<prefix>.request.bytes`, `<prefix>.response.bytes`).
- [Tag levels (LOW vs EXTENDED)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/TagLevelDemo.java)

  This example demonstrates minimal vs extended metric tagging (adding `protocol` and `target` when `EXTENDED`) using different metric prefixes to avoid label-set clashes.
- [Tracing + metrics (classic, OpenTelemetry bridge)](https://github.com/apache/httpcomponents-client/tree/master/httpclient5-observation/src/test/java/org/apache/hc/client5/http/observation/example/TracingAndMetricsDemo.java)

  This example demonstrates wiring Micrometer `ObservationRegistry` to OpenTelemetry (in-memory exporter) while recording HttpClient timers/counters, printing an exported span and a Prometheus scrape.

---

<a id="index"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/ -->

<!-- page_index: 18 -->

<a id="index--httpclient-overview"></a>

# HttpClient Overview

The Hyper-Text Transfer Protocol (HTTP) is perhaps the most significant protocol used on the Internet today. Web
services, network-enabled appliances and the growth of network computing continue to expand the role of the HTTP
protocol beyond user-driven web browsers, while increasing the number of applications that require HTTP support.

Although the java.net package provides basic functionality for accessing resources via HTTP, it doesn't provide the full
flexibility or functionality needed by many applications. HttpClient seeks to fill this void by providing an efficient, up-to-date, and feature-rich package implementing the client side of the most recent HTTP standards and recommendations.

Designed for extension while providing robust support for the base HTTP protocol, HttpClient may be of interest to
anyone building HTTP-aware client applications such as web browsers, web service clients, or systems that leverage or
extend the HTTP protocol for distributed communication.

<a id="index--documentation"></a>

## Documentation

1. [Quick Start](#quickstart) - contains simple, complete examples of request execution
   with the classic, fluent and async APIs.
2. [Architecture](#architecture) - describes HttpClient architecture pronciples such as
   the layering concept.
3. Guides

   - [Migration](#migration-guide) - helps choose the best migration path from
     older version of Apache HttpClient, different i/o models supported by Apache HttpClient
     or other HTTP clients.
   - [Configuration](#configuration) - describes principles of HttpClient configuration.
   - [Logging](#logging)
   - [Connection management](#connection-management)
   - [Connection pooling](#connection-pooling)
   - [Async content compression / decompression](#async-compression)
   - [Android support](#android)
   - [Early Hints](#early-hints)
   - [Observation](#observation)
   - [SCRAM-SHA-256](#scram-sha-256)
   - [SPKI pinning TLS strategy](#spki-pinning)
4. Examples demonstrating some common as well as more complex use cases

   - [HttpClient Classic APIs](#examples)
   - [HttpClient Async APIs](#examples-async)
   - [HttpClient Reactive Streams APIs](#examples-reactive)
   - [HttpClient Observation APIs](#examples-observation)
5. Javadocs

   - [HttpClient](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5/apidocs/)
   - [HC Fluent](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5-fluent/apidocs/)
   - [HttpClient Cache](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5-cache/apidocs/)
   - [HttpClient Observation](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5-observation/apidocs/)
6. API compatibility reports

   - [HttpClient](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5/japicmp.html)
   - [HC Fluent](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5-fluent/japicmp.html)
   - [HttpClient Cache](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5-cache/japicmp.html)
   - [HC Observation](https://hc.apache.org/httpcomponents-client-5.6.x/current/httpclient5-observation/japicmp.html)

<a id="index--features"></a>

## Features

- Standards based, pure Java, implementation of HTTP versions 1.0, 1.1, 2.0
- Supports encryption with HTTPS (HTTP over SSL) protocol.
- Pluggable TLS strategies.
- Transparent message exchanges through HTTP/1.1, HTTP/1.0 and SOCKS proxies.
- Tunneled HTTPS connections through HTTP/1.1 and HTTP/1.0 proxies, via the CONNECT method.
- Basic, Digest, Bearer, SCRAM-SHA-256 authentication schemes.
- HTTP state management and cookie support.
- Flexible connection management and pooling with STRICT, LAX and OFFLOCK concurrency policies.
- Optional off-lock disposal for blocking connection pools to move slow graceful closes off hot pool locks.
- Basic, Digest, Bearer, and SCRAM-SHA-256 authentication schemes.
- Support for HTTP response caching. Pluggable storage backends based on Ehcache, Memcached, Caffeine.
- Transparent content decompression with deflate, gzip, and optional zstd / brotli codecs.
- Support for Unix domain sockets.
- Experimental RFC 9218 prioritization (Priority header & PRIORITY\_UPDATE for HTTP/2).
- I/O byte counters, connection-pool gauges, and DNS/TLS meters for classic and async clients.
- Optional SPKI pinning TLS strategy for host / wildcard public-key pinning.
- Async support for 103 Early Hints via a pluggable
- Optional Observability nodule with Micrometer / OpenTelemetry support for request timers/counters,
- Optional Server-Sent Events (SSE) module for consuming long-lived event
  streams over HTTP/1.1 and HTTP/2 using the async transport.
- Source code is freely available under the Apache License.

<a id="index--standards-compliance"></a>

## Standards Compliance

HttpClient strives to conform to the following specifications endorsed by the Internet Engineering Task Force (IETF) and
the internet at large:

- [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110) - HTTP Semantics
- [RFC 9111](https://datatracker.ietf.org/doc/html/rfc9111) - HTTP Caching
- [RFC 9112](https://datatracker.ietf.org/doc/html/rfc9112) - Hypertext Transfer Protocol Version 1.1 (HTTP/1.1)
- [RFC 7540](https://datatracker.ietf.org/doc/html/rfc7540) - Hypertext Transfer Protocol Version 2 (HTTP/2)
- [RFC 7541](https://datatracker.ietf.org/doc/html/rfc7541) - HPACK: Header Compression for HTTP/2
- [RFC 1945](https://datatracker.ietf.org/doc/html/rfc1945) - Hypertext Transfer Protocol – HTTP/1.0
- [RFC 2396](https://datatracker.ietf.org/doc/html/rfc2396) - Uniform Resource Identifiers (URI): Generic Syntax
- [RFC 6265](https://datatracker.ietf.org/doc/html/rfc6265) - HTTP State Management Mechanism (Cookies)
- [RFC 7616](https://datatracker.ietf.org/doc/html/rfc7616) - HTTP Digest Access Authentication
- [RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617) - HTTP ‘Basic’ Authentication Scheme
- [RFC 5861](https://datatracker.ietf.org/doc/html/rfc5861) - HTTP Cache-Control Extensions for Stale Content
- [RFC 2817](https://datatracker.ietf.org/doc/html/rfc2817) - Upgrading to TLS Within HTTP/1.1
- [RFC 9218](https://datatracker.ietf.org/doc/html/rfc9218) - Extensible Prioritization Scheme for HTTP
- [RFC 7804](https://datatracker.ietf.org/doc/html/rfc7804) - Salted Challenge Response HTTP Authentication Mechanism
- [RFC 8297](https://datatracker.ietf.org/doc/html/rfc8297) – Early Hints status code

---

<a id="migration-guide-preparation"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/migration-guide/preparation.html -->

<!-- page_index: 19 -->

<a id="migration-guide-preparation--migration-from-apache-httpclient-4.x-apis"></a>

# Migration from Apache HttpClient 4.x APIs

It is strongly encouraged to follow the best practices and common use patterns in programming with Apache HttpClient
4.x. They remain largely unchanged between 4.x and 5.x release series. Correctly written code will be easier to port to
5.x APIs and from the classic I/O model to the async I/O model.

<a id="migration-guide-preparation--preparation-steps"></a>

## Preparation steps

1. Make sure there are no references to deprecated functions or classes
2. HttpClient uses tries to use sensible defaults but it is generally recommended to adjust SSL/TLS parameters and
   timeout settings for the specific application context.
3. Explicitly specify TLSv1.2 in order to disable older, less secure versions of the SSL/TLS protocol. Please note
   HttpClient 4.5 disables all SSL versions by default.
4. Set finite socket and connect timeouts.
5. Set a finite connection total time to live (TTL). Use a negative value for connections with unlimited / infinite
   time to live. Please note as of version 5.0 HttpClient treats zero TTL as an instruction that connections
   are not meant to be re-used.
6. Favor the `strict` cookie policy.
7. IMPORTANT: Always re-use `CloseableHttpClient` instances. They are expensive to create, but they are also fully
   thread safe, so multiple threads can use the same instance of `CloseableHttpClient` to execute multiple requests
   concurrently taking full advantage of persistent connection re-use and connection pooling.


```java
CloseableHttpClient client = HttpClients.custom()
        .setSSLSocketFactory(new SSLConnectionSocketFactory(
                SSLContexts.createSystemDefault(),
                new String[] { "TLSv1.2" },
                null,
                SSLConnectionSocketFactory.getDefaultHostnameVerifier()))
        .setConnectionTimeToLive(1, TimeUnit.MINUTES)
        .setDefaultSocketConfig(SocketConfig.custom()
                .setSoTimeout(60000)
                .build())
        .setDefaultRequestConfig(RequestConfig.custom()
                .setConnectTimeout(60000)
                .setSocketTimeout(60000)
                .setCookieSpec(StandardCookieSpec.STRICT)
                .build())
        .build();
```

8. Cookie store and credentials providers can be shared by multiple execution threads. They can still be shared by
   multiple message exchnages without being set at
   `CloseableHttpClient` construction time.


```java
CookieStore cookieStore = new BasicCookieStore();
CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
```

9. While `CloseableHttpClient` should have the default configuration applicable to all all messages exchanges one can
   use `HttpContext` to customize individual request execution parameters.


```java
HttpClientContext clientContext = HttpClientContext.create();
clientContext.setCookieStore(cookieStore);
clientContext.setCredentialsProvider(credentialsProvider);
clientContext.setRequestConfig(RequestConfig.custom()
        .setConnectTimeout(60000)
        .setSocketTimeout(60000)
        .setCookieSpec(StandardCookieSpec.STRICT)
        .build());
```

10. Always set content type and content encoding on the entity and let HttpClient generate request headers automatically.


```java
JsonFactory jsonFactory = new JsonFactory();
ObjectMapper objectMapper = new ObjectMapper(jsonFactory);

HttpPost httpPost = new HttpPost("https://httpbin.org/post");
List<NameValuePair> requestData = Arrays.asList(
        new BasicNameValuePair("name1", "value1"),
        new BasicNameValuePair("name2", "value2"));

EntityTemplate requestEntity = new EntityTemplate(outstream -> {
    objectMapper.writeValue(outstream, requestData);
    outstream.flush();

});
requestEntity.setContentType(ContentType.APPLICATION_JSON.toString());
httpPost.setEntity(requestEntity);
```

11. Consume response content directly from the content stream and convert it to a higher level object without converting
    it to an intermediate string or byte array.
12. Favor HTTP response handlers for response processing, thus making connection release automatic.


```java
JsonNode responseData = client.execute(httpPost, response -> {if (response.getStatusLine().getStatusCode() >= 300) {throw new ClientProtocolException(Objects.toString(response.getStatusLine()));} final HttpEntity responseEntity = response.getEntity(); if (responseEntity == null) {return null;} try (InputStream inputStream = responseEntity.getContent()) {return objectMapper.readTree(inputStream);} }); System.out.println(responseData);
```

13. `CloseableHttpClient` instances should be closed when no longer needed or about to go out of scope.


```java
client.close();
```

---

<a id="migration-guide-migration-to-classic"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/migration-guide/migration-to-classic.html -->

<!-- page_index: 20 -->

<a id="migration-guide-migration-to-classic--migration-to-apache-httpclient-5.x-classic-apis"></a>

# Migration to Apache HttpClient 5.x classic APIs

HttpClient 5.x releases can be co-located with earlier major versions on the same classpath due to versioned package
namespace and Maven module coordinates.

HttpClient 5.x classic APIs are largely compatible with HttpClient 4.0 APIs. Major differences are related to connection
management configuration, SSL/TLS and timeout settings when building HttpClient instances.
There are also some important differences with URL normalization and encoding.

<a id="migration-guide-migration-to-classic--migration-steps"></a>

## Migration steps

- Add HttpClient 5.x as a new dependency to the project and optionally remove HttpClient 4.x
- Remove old `org.apache.http` imports and re-import HttpClient classes from
  `org.apache.hc.httpclient5` package namespace. Most old interfaces and classes should resolve automatically. One
  notable exception is `HttpEntityEnclosingRequest` interface In HttpClient 5.x one can enclose a request entity with
  any HTTP method even if violates semantic of the method.
- There will be compilation errors due to API incompatibilities between version series 4.x and 5.x mostly related to
  SSL/TLS and timeout settings and `CloseableHttpClient` instance creation. Several modifications are likely to be
  necessary.
- Use `PoolingHttpClientConnectionManagerBuilder` class to create connection managers with custom parameters
- Use `DefaultClientTlsStrategy` class to create SSL connection socket factories with custom parameters
- While HttpClient 5 automatically disables all SSL versions and weak TLS versions it may still be advisable to
  explicitly specify TLSv1.3 as the only enabled version.
- Use `Timeout` class to define timeouts.
- Use `TimeValue` class to define time values (duration).
- Optionally choose a connection pool concurrency policy: `STRICT` for strict connection max limit guarantees; `LAX`
  for higher concurrency but with lax connection maximum limit guarantees. With `LAX` policy HttpClient can exceed the
  per route maximum limit under high load and does not enforce the total maximum limit.
- Optionally choose a connection pool re-use policy: `LIFO` to re-use as few connections as possible making it possible
  for connections to become idle and expire; `FIFO` to re-use all connections equally preventing them from becoming
  idle and expiring.
- Optionally choose a finite total time to live for connections.


```java
PoolingHttpClientConnectionManager connectionManager = PoolingHttpClientConnectionManagerBuilder.create()
   .setTlsSocketStrategy(ClientTlsStrategyBuilder.create()
              .setSslContext(SSLContexts.createSystemDefault())
              .setTlsVersions(TLS.V_1_3)
              .buildClassic())
      .setDefaultSocketConfig(SocketConfig.custom()
              .setSoTimeout(Timeout.ofMinutes(1))
              .build())
      .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.STRICT)
      .setConnPoolPolicy(PoolReusePolicy.LIFO)
      .setDefaultConnectionConfig(ConnectionConfig.custom()
              .setSocketTimeout(Timeout.ofMinutes(1))
              .setConnectTimeout(Timeout.ofMinutes(1))
              .setTimeToLive(TimeValue.ofMinutes(10))
              .build())
      .build();
```

- Favor the `strict` cookie policy when using HttpClient 5.0.
- Use response timeout to define the maximum period of inactivity until receipt of response data.
- All base principles and good practices of HttpClient programing still apply. Always re-use client instances. Client
  instances are expensive to create and are thread safe in both HttpClient 4.x and 5.x series.


```java
CloseableHttpClient client = HttpClients.custom()
      .setConnectionManager(connectionManager)
      .setDefaultRequestConfig(RequestConfig.custom()
              .setCookieSpec(StandardCookieSpec.STRICT)
              .build())
      .build();

CookieStore cookieStore = new BasicCookieStore();

CredentialsProvider credentialsProvider = new BasicCredentialsProvider();

HttpClientContext clientContext = HttpClientContext.create();
clientContext.setCookieStore(cookieStore);
clientContext.setCredentialsProvider(credentialsProvider);
clientContext.setRequestConfig(RequestConfig.custom()
      .setCookieSpec(StandardCookieSpec.STRICT)
      .build());

JsonFactory jsonFactory = new JsonFactory();
ObjectMapper objectMapper = new ObjectMapper(jsonFactory);

ClassicHttpRequest httpPost = ClassicRequestBuilder.post("https://httpbin.org/post")
       .setEntity(HttpEntities.create(outstream -> {
           objectMapper.writeValue(outstream, Arrays.asList(
                   new BasicNameValuePair("name1", "value1"),
                   new BasicNameValuePair("name2", "value2")));
           outstream.flush();
       }, ContentType.APPLICATION_JSON))
       .build();
```

- HTTP response messages in HttpClient 5.x no longer have a status line. Use response code directly.


```java
JsonNode responseData = client.execute(httpPost, response -> {if (response.getCode() >= 300) {throw new ClientProtocolException(new StatusLine(response).toString());} final HttpEntity responseEntity = response.getEntity(); if (responseEntity == null) {return null;} try (InputStream inputStream = responseEntity.getContent()) {return objectMapper.readTree(inputStream);} }); System.out.println(responseData);
```

- `CloseableHttpClient` instances should be closed when no longer needed or about to go out of scope.


```java
client.close();
```

- The 4.x `RequestConfig` property `normalizeUri` has been removed, and `URIUtils.normalizeSyntax` is no longer public.
  In 4.x, these only supported limited normalization from [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
  including removal of dot segments (section 5.2.4), and syntax-based normalization (section 6.2.2).
  The 5.x `URIBuilder` in [httpcomponents-core](https://hc.apache.org/httpcomponents-core-5.3.x/index.html) has a new
  public `normalizeSyntax` method, but it strives for more thorough support of RFC 3986,
  specifically percent-encoding all components.
  Since 5.3, `normalizeSyntax` has been deprecated and renamed to `optimize` to emphasize the difference in behaviour.

<a id="migration-guide-migration-to-classic--migration-recipes"></a>

## Migration recipes

The following table provides some migration recipes from HttpClient 4.x to HttpClient 5.x classic APIs.

**Note:** the list of recipes is by no means complete and users are encouraged to contribute other recipes based on their experience.

| HttpClient 4.x | HttpClient 5.x |
| --- | --- |
| `BasicHttpContext` | `HttpCoreContext`/ `HttpClientContext` |
| `HttpClientConnectionManager.closeExpiredConnections()` | `ConnPoolControl.closeExpired()` |
| `HttpClientConnectionManager.closeIdleConnections()` | `ConnPoolControl.closeIdle()` |
| `HttpClients.custom().addInterceptorLast(<some logging interceptor>)` | `HttpClients.custom().addExecInterceptorFirst("...", <some logging interceptor>)` (otherwise, compressed payload may be logged) |
| `HttpClients.custom().setDefaultSocketConfig(...)` | `PoolingHttpClientConnectionManagerBuilder.create().setDefaultSocketConfig(...)`/ `BasicHttpClientConnectionManager.setSocketConfig(...)` `HttpClients.custom().setConnectionManager(...)` |
| `HttpClients.custom().setRetryHandler()` | `HttpClients.custom().setRetryStrategy()` |
| `HttpContext.getAttribute(HttpCoreContext.HTTP_TARGET_HOST)` | `HttpClientContext.getHttpRoute().getTargetHost()` |
| `((ManagedHttpClientConnection) HttpContext.getAttribute(HttpCoreContext.HTTP_CONNECTION)).getSSLSession()` | `HttpCoreContext.getSSLSession()` |
| `HttpEntityEnclosingRequest` | `HttpEntityContainer` |
| `HttpMessage.getAllHeaders()` | `MessageHeaders.getHeaders()` |
| `HttpRequest.getRequestLine()` | `new RequestLine(request)` |
| `HttpRequestBase` | `HttpUriRequestBase` |
| `HttpResponse.getEntity()` | `ClassicHttpResponse.getEntity()` |
| `HttpResponse.getStatusLine()` | `new StatusLine(response)` |
| `HttpResponse.getStatusLine().getStatusCode()` | `HttpResponse.getCode()` |
| `RequestConfig.custom().setConnectTimeout()` `HttpClients.custom().setDefaultRequestConfig(...)` | `ConnectionConfig.custom().setConnectTimeout()` `PoolingHttpClientConnectionManager.setDefaultConnectionConfig(...)` / `BasicHttpClientConnectionManager.setConnectionConfig(...)` `HttpClients.custom().setConnectionManager(...)` |
| `RequestConfig.custom().setSocketTimeout()` `HttpClients.custom().setDefaultRequestConfig(...)` | `ConnectionConfig.custom().setSocketTimeout()` `PoolingHttpClientConnectionManager.setDefaultConnectionConfig(...)` / `BasicHttpClientConnectionManager.setConnectionConfig(...)` `HttpClients.custom().setConnectionManager(...)` |

---

<a id="migration-guide-migration-to-async-simple"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/migration-guide/migration-to-async-simple.html -->

<!-- page_index: 21 -->

<a id="migration-guide-migration-to-async-simple--migration-to-apache-httpclient-5.x-async-apis-with-simple-message-handlers"></a>

# Migration to Apache HttpClient 5.x async APIs with simple message handlers

While HttpClient 5.x classic APIs are largely compatible with HttpClient 4.0 APIs and can work with
any `InputStream / OutputStream` based content processing library, the HttpClient 5.x async APIs are completely
different.

HttpClient 5.x async APIs use an event-driven, reactive programming model based on the concept of channels and event
handlers. The channels act as conduits for asynchronous data output. The event handlers react to asynchronous signals or
events and communicate with the opposite endpoint through available channels.

Both the classic and the async models have their merits. The event-driven, reactive model tends to be efficient and
convenient for communication protocols with message multiplexing such as HTTP/2. However async APIs generally not
integrate well with `InputStream / OutputStream` based content processing libraries.

HttpClient 5.x provides simplified request and response handlers that hide the complexity of the event-driven model by
buffering message content in memory. Simplified APIs are intended as a temporary, intermediate step in the migration
process or for productive use in scenarios where messages known to be limited in length and the opposite endpoints are
either known to be well-behaved or specifically designed for simple message handlers.

<a id="migration-guide-migration-to-async-simple--migration-steps"></a>

## Migration steps

- Replace `PoolingHttpClientConnectionManager` with `PoolingAsyncClientConnectionManager`


```java
PoolingAsyncClientConnectionManager connectionManager = PoolingAsyncClientConnectionManagerBuilder.create()
      .setTlsStrategy(ClientTlsStrategyBuilder.create()
              .setSslContext(SSLContexts.createSystemDefault())
              .setTlsVersions(TLS.V_1_3)
              .buildAsync())
      .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.STRICT)
      .setConnPoolPolicy(PoolReusePolicy.LIFO)
      .setDefaultConnectionConfig(ConnectionConfig.custom()
             .setSocketTimeout(Timeout.ofMinutes(1))
             .setConnectTimeout(Timeout.ofMinutes(1))
             .setTimeToLive(TimeValue.ofMinutes(10))
             .build())
      .setDefaultTlsConfig(TlsConfig.custom()
             .setVersionPolicy(HttpVersionPolicy.NEGOTIATE)
             .setHandshakeTimeout(Timeout.ofMinutes(1))
             .build())
      .build();
```

  Please note that `PoolingAsyncClientConnectionManager` uses different `TLS/SSL` configuration. It also does not
  support `SocketConfig` configuration due to differences in the I/O model.
- Select appropriate HTTP version policy. Presently supported policies are: `NEGOTIATE`, `FORCE_HTTP_1`
  and `FORCE_HTTP_2`. When the `NEGOTIATE` policy is chosen, HttpClient attempts to negotiate the use of HTTP/2 through
  the TLS ALPN (application protocol negotiation) extension as long as it is supported by the default JSSE .
- Replace `CloseableHttpClient` with `CloseableHttpAsyncClient`.


```java
CloseableHttpAsyncClient client = HttpAsyncClients.custom()
      .setConnectionManager(connectionManager)
      .setIOReactorConfig(IOReactorConfig.custom()
              .setSoTimeout(Timeout.ofMinutes(1))
              .build())
      .setDefaultRequestConfig(RequestConfig.custom()
              .setCookieSpec(StandardCookieSpec.STRICT)
              .build())
      .build();
```

- Unlike the classic client the asynchronous one needs to be started in order to be able to execute requests.


```java
client.start();
```

- Request execution with simple asynchronous handlers is not that radically different than with the classic APIs. The
  major difference is that the result of the operation is controlled with a `Future` interface and is signalled
  with `FutureCallback` events.

  Message content processing for simple asynchronous handlers can be implemented with any library that can work with
  I/O streams (`InputStream`/`OutputStream`) or strings.


```java
CookieStore cookieStore = new BasicCookieStore();

CredentialsProvider credentialsProvider = new BasicCredentialsProvider();

HttpClientContext clientContext = HttpClientContext.create();
clientContext.setCookieStore(cookieStore);
clientContext.setCredentialsProvider(credentialsProvider);
clientContext.setRequestConfig(RequestConfig.custom()
      .setCookieSpec(StandardCookieSpec.STRICT)
      .build());

JsonFactory jsonFactory = new JsonFactory();
ObjectMapper objectMapper = new ObjectMapper(jsonFactory);

SimpleHttpRequest httpPost = SimpleRequestBuilder.post("https://httpbin.org/post")
     .setBody(objectMapper.writeValueAsString(Arrays.asList(
             new BasicNameValuePair("name1", "value1"),
             new BasicNameValuePair("name2", "value2"))), ContentType.APPLICATION_JSON)
     .build();

Future<?> future = client.execute(httpPost, new FutureCallback<SimpleHttpResponse>() {

  @Override
  public void completed(SimpleHttpResponse response) {
      try {
          JsonNode responseData = objectMapper.readTree(response.getBodyText());
          System.out.println(responseData);
      } catch (IOException ex) {
          System.out.println("Error processing jSON content: " + ex.getMessage());
      }
  }

  @Override
  public void failed(Exception ex) {
      System.out.println("Error executing HTTP request: " + ex.getMessage());
  }

  @Override
  public void cancelled() {
      System.out.println("HTTP request execution cancelled");
  }

});
```

- `CloseableHttpAsyncClient` instances should be closed when no longer needed or about to go out of scope.


```java
client.close(CloseMode.GRACEFUL);
```

---

<a id="migration-guide-migration-to-async-streaming"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/migration-guide/migration-to-async-streaming.html -->

<!-- page_index: 22 -->

<a id="migration-guide-migration-to-async-streaming--migration-to-apache-httpclient-5.x-async-apis"></a>

# Migration to Apache HttpClient 5.x async APIs

HttpClient ships with a number of standard message handlers for the most common scenarios as well as a number of
abstract classes that can be used as a base for custom handlers.

- `BasicAsyncEntityConsumer`, `BasicAsyncEntityProducer` entity handlers that buffer entity content in memory and
  therefore are not much different than simple handlers.
- `AbstractBinAsyncEntityConsumer` and `AbstractBinAsyncEntityProducer` handlers can serve as the base classes for
  custom binary entity consumers or producers.
- `AbstractCharAsyncEntityConsumer` and `AbstractCharAsyncEntityProducer` handlers can serve as the base classes for
  custom character entity consumers or producers.
- `FileEntityProducer` entity handler that generates data stream from a file.
- `AbstractClassicEntityConsumer` and `AbstractClassicEntityProducer` entity handlers that acts as a compatibility layer
  for classic `InputStream` / `OutputStream` based interfaces. Blocking input / output processing is executed through
  an `Executor`.
- `BasicRequestProducer` and `BasicResponseConsumer` messages handlers that perform no message head transformation and
  can use any custom entity producer or consumer to handle the message body.
- `AbstractBinResponseConsumer` response handler can serve as the base class for custom binary response consumers.
- `AbstractCharResponseConsumer` response handler can serve as the base class for custom character response consumers.

There are also third-party libraries that can provide specialized message handlers, for instance, for [JSON message processing](https://github.com/ok2c/httpcomponents-jackson) using
[Jackson JSON processor](https://github.com/FasterXML/jackson).

<a id="migration-guide-migration-to-async-streaming--migration-steps"></a>

## Migration steps

- Depending on the preferred migration path it one might consider migrating to HttpClient 5.x classic APIs or
  HttpClient 5.x async APIs with simple message handlers as the first step.
- Replace the existing request generation and response processing code with optimized message handlers shipped with
  HttpClient 5.x or custom-built handlers.

  In this particular instance [JSON message handlers](https://github.com/ok2c/httpcomponents-jackson)
  are used to process JSON messages of arbitrary length without intermediate buffering of the entire message.

  The general use pattern remains the same as with simple message handlers.


```java
PoolingAsyncClientConnectionManager connectionManager = PoolingAsyncClientConnectionManagerBuilder.create()
     .setTlsStrategy(ClientTlsStrategyBuilder.create()
             .setSslContext(SSLContexts.createSystemDefault())
             .setTlsVersions(TLS.V_1_3)
             .buildAsync())
     .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.STRICT)
     .setConnPoolPolicy(PoolReusePolicy.LIFO)
     .setDefaultConnectionConfig(ConnectionConfig.custom()
             .setSocketTimeout(Timeout.ofMinutes(1))
             .setConnectTimeout(Timeout.ofMinutes(1))
             .setTimeToLive(TimeValue.ofMinutes(10))
             .build())
     .setDefaultTlsConfig(TlsConfig.custom()
             .setVersionPolicy(HttpVersionPolicy.NEGOTIATE)
             .setHandshakeTimeout(Timeout.ofMinutes(1))
             .build())
     .build();

CloseableHttpAsyncClient client = HttpAsyncClients.custom()
     .setConnectionManager(connectionManager)
     .setIOReactorConfig(IOReactorConfig.custom()
             .setSoTimeout(Timeout.ofMinutes(1))
             .build())
     .setDefaultRequestConfig(RequestConfig.custom()
             .setCookieSpec(StandardCookieSpec.STRICT)
             .build())
     .build();
client.start();

CookieStore cookieStore = new BasicCookieStore();

CredentialsProvider credentialsProvider = new BasicCredentialsProvider();

HttpClientContext clientContext = HttpClientContext.create();
clientContext.setCookieStore(cookieStore);
clientContext.setCredentialsProvider(credentialsProvider);
clientContext.setRequestConfig(RequestConfig.custom()
     .setCookieSpec(StandardCookieSpec.STRICT)
     .build());

JsonFactory jsonFactory = new JsonFactory();
ObjectMapper objectMapper = new ObjectMapper(jsonFactory);

Future<?> future = client.execute(
     JsonRequestProducers.create(
             BasicRequestBuilder.post("https://httpbin.org/post").build(),
             Arrays.asList(
                     new org.apache.http.message.BasicNameValuePair("name1", "value1"),
                     new org.apache.http.message.BasicNameValuePair("name2", "value2")),
             objectMapper),
     JsonResponseConsumers.create(jsonFactory),
     new FutureCallback<Message<HttpResponse, JsonNode>>() {

         @Override
         public void completed(Message<HttpResponse, JsonNode> message) {
             System.out.println(message.getBody());
         }

         @Override
         public void failed(Exception ex) {
             System.out.println("Error executing HTTP request: " + ex.getMessage());
         }

         @Override
         public void cancelled() {
             System.out.println("HTTP request execution cancelled");
         }

     });

future.get();
client.close(CloseMode.GRACEFUL);
```

---

<a id="migration-guide-migration-to-async-http2"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/migration-guide/migration-to-async-http2.html -->

<!-- page_index: 23 -->

<a id="migration-guide-migration-to-async-http2--migration-to-apache-httpclient-5.x-async-apis-for-http-2-only"></a>

# Migration to Apache HttpClient 5.x async APIs for HTTP/2 only

For those scenarios where HTTP/1.1 compatibility is no longer required HttpClient 5.0
provides `CloseableHttpAsyncClient` optimized for HTTP/2 protocol with full support for multiplexed request execution
over a single HTTP/2 connection.

<a id="migration-guide-migration-to-async-http2--migration-steps"></a>

## Migration steps

- Replace the default client builder with HTTP/2 specific one. Request and response handlers do not require any
  modification.

  Please note HTTP/2 clients do not have a connection manager. They maintain an internal map of active connections,
  one per distinct origin host. Therefore, TLS settings can be applied directly to the client instance, not a
  connection manager.

  Please note that presently HTTP/2 clients do not support request execution via an HTTP proxy.


```java
CloseableHttpAsyncClient client = HttpAsyncClients.customHttp2()
      .setTlsStrategy(ClientTlsStrategyBuilder.create()
              .setSslContext(SSLContexts.createSystemDefault())
              .setTlsVersions(TLS.V_1_3)
              .buildAsync())
      .setIOReactorConfig(IOReactorConfig.custom()
              .setSoTimeout(Timeout.ofMinutes(1))
              .build())
      .setDefaultConnectionConfig(ConnectionConfig.custom()
              .setSocketTimeout(Timeout.ofMinutes(1))
              .setConnectTimeout(Timeout.ofMinutes(1))
              .setTimeToLive(TimeValue.ofMinutes(10))
              .build())
      .setDefaultRequestConfig(RequestConfig.custom()
              .setCookieSpec(StandardCookieSpec.STRICT)
              .build())
      .build();
client.start();

CookieStore cookieStore = new BasicCookieStore();

CredentialsProvider credentialsProvider = new BasicCredentialsProvider();

HttpClientContext clientContext = HttpClientContext.create();
clientContext.setCookieStore(cookieStore);
clientContext.setCredentialsProvider(credentialsProvider);
clientContext.setRequestConfig(RequestConfig.custom()
      .setCookieSpec(StandardCookieSpec.STRICT)
      .build());

JsonFactory jsonFactory = new JsonFactory();
ObjectMapper objectMapper = new ObjectMapper(jsonFactory);

Future<?> future = client.execute(
     JsonRequestProducers.create(
             BasicRequestBuilder.post("https://httpbin.org/post").build(),
             Arrays.asList(
                  new BasicNameValuePair("name1", "value1"),
                  new BasicNameValuePair("name2", "value2")),
             objectMapper),
      JsonResponseConsumers.create(jsonFactory),
      new FutureCallback<Message<HttpResponse, JsonNode>>() {

          @Override
          public void completed(Message<HttpResponse, JsonNode> message) {
              System.out.println(message.getBody());
          }

          @Override
          public void failed(Exception ex) {
              System.out.println("Error executing HTTP request: " + ex.getMessage());
          }

          @Override
          public void cancelled() {
              System.out.println("HTTP request execution cancelled");
          }

      });

future.get();
client.close(CloseMode.GRACEFUL);
```

---

<a id="related-projects"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/related-projects.html -->

<!-- page_index: 24 -->

<a id="related-projects--related-projects"></a>

# Related projects

<a id="related-projects--asynchronous-json-message-processors"></a>

## Asynchronous JSON message processors

[Asynchronous JSON message processors](https://ok2c.github.io/httpcomponents-jackson/) library is a companion project
for HttpClient 5.0 developed outside the Apache Software Foundation.

The library provides a number of asynchronous message consumers and producers for efficient, reactive processing of HTTP
messages with enclosed JSON content using [Jackson JSON processor](https://github.com/FasterXML/jackson).

<a id="related-projects--android-extensions"></a>

## Android extensions

[Android extensions for Apache HttpClient 5.x](https://ok2c.github.io/httpclient-android-ext/) is a third party library
that provides extra functionality simplifying application of Apache HttpClient on Google Android platform.

---

<a id="download"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-client-5.6.x/download.html -->

<!-- page_index: 25 -->

<a id="download--httpclient-downloads"></a>

# HttpClient Downloads

The latest release available for download:

[Release packages](https://hc.apache.org/downloads.html) -
[Release Notes](https://www.apache.org/dist/httpcomponents/httpclient/RELEASE_NOTES-5.6.x.txt) -
[License](https://www.apache.org/licenses/LICENSE-2.0.html)

<a id="download--dependency-management"></a>

## Dependency management

If you are using a dependency manager for your project such as [Apache Maven](https://maven.apache.org), [Gradle](https://gradle.org/) or [Apache Ivy](https://ant.apache.org/projects/ivy.html), you can create a dependency on
HttpClient modules by using this information:

- [HttpClient](https://search.maven.org/artifact/org.apache.httpcomponents.client5/httpclient5)
- [HttpClient Fluent](https://search.maven.org/artifact/org.apache.httpcomponents.client5/httpclient5-fluent)
- [HttpClient Cache](https://search.maven.org/artifact/org.apache.httpcomponents.client5/httpclient5-cache)
- [HttpClient Observation](https://central.sonatype.com/artifact/org.apache.httpcomponents.client5/httpclient5-observation)

---
