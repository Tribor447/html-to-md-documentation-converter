# HttpCore Overview

## Navigation

- Components
  - HttpCore 5.4
    - [Examples](#examples)
    - [Download](#download)
- Other pages
  - [HttpCore Overview](#index)

## Content

<a id="examples"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-core-5.4.x/examples.html -->

<!-- page_index: 1 -->

<a id="examples--httpcore-examples"></a>

# HttpCore Examples

- [Classic (blocking) HTTP/1.1 GET requests](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/ClassicGetExecutionExample.java)

  This example demonstrates synchronous execution of multiple HTTP/1.1 GET requests.
- [Classic (blocking) HTTP/1.1 POST requests](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/ClassicPostExecutionExample.java)

  This example demonstrates synchronous execution of multiple HTTP/1.1 POST requests with enclosed content of various
  types.
- [Asynchronous HTTP/1.1 GET requests](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/AsyncRequestExecutionExample.java)

  This example demonstrates asynchronous execution of multiple HTTP/1.1 requests.
- [Asynchronous HTTP/2 GET requests](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-h2/src/test/java/org/apache/hc/core5/http2/examples/H2RequestExecutionExample.java)

  This example demonstrates asynchronous execution of multiple HTTP/2 requests.
- [HTTP/2 requests over TLS connections with ALPN support on Java 1.7 and Java 1.8](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-h2/src/test/java/org/apache/hc/core5/http2/examples/H2ConscriptRequestExecutionExample.java)

  This example demonstrates how to execute HTTP/2 requests over TLS connections with ALPN support on Java 1.7 and Java
  1.8.
- [Asynchronous HTTP/1.1 GET requests with message pipelining](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/AsyncPipelinedRequestExecutionExample.java)

  This example demonstrates asynchronous, pipelined execution multiple HTTP/1.1 requests.
- [Asynchronous HTTP/2 GET requests with multiple concurrent streams](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-h2/src/test/java/org/apache/hc/core5/http2/examples/H2MultiStreamExecutionExample.java)

  This example demonstrates asynchronous, multistream execution of multiple HTTP/2 requests.
- [Classic (blocking) HTTP/1.1 file server](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/ClassicFileServerExample.java)

  This is an example of an embedded HTTP/1.1 file server with a classic (blocking) message transport.
- [Request filters with classic (blocking) HTTP/1.1 server](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/ClassicServerFilterExample.java)

  This is an example of using synchronous request filters with an embedded HTTP/1.1 server.
- [Asynchronous HTTP/1.1 file server](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/AsyncFileServerExample.java)

  This is an example of an embedded HTTP/1.1 file server with an event driven, non-blocking message transport.
- [Request filters with asynchronous HTTP/1.1 server](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/AsyncServerFilterExample.java)

  This is an example of using asynchronous request filters with an embedded HTTP/1.1 server.
- [Asynchronous HTTP/2 file server](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-h2/src/test/java/org/apache/hc/core5/http2/examples/H2FileServerExample.java)

  This is an example of an embedded HTTP/2 file server with an event driven, non-blocking message transport.
- [Classic (blocking) HTTP reverse proxy](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/ClassicReverseProxyExample.java)

  This is an example of an embedded HTTP/1.1 reverse proxy with a classic (blocking) message transport.
- [Asynchronous HTTP reverse proxy](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/AsyncReverseProxyExample.java)

  This is an example of an embedded HTTP/1.1 reverse proxy with an event driven, non-blocking message transport.
- [Client Reactive Streams](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-reactive/src/test/java/org/apache/hc/core5/reactive/examples/ReactiveFullDuplexClientExample.java)

  This is an example of full-duplex HTTP/1.1 client side message exchanges using reactive streaming.
- [Server Reactive Streams](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-reactive/src/test/java/org/apache/hc/core5/reactive/examples/ReactiveFullDuplexServerExample.java)

  This is an example of full-duplex HTTP/1.1 server side message exchanges using reactive streaming.
- [SNI (Server Name Identification) with classic (blocking) I/O](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/ClassicGetExecutionExample.java)

  This is an example of SNI (Server Name Identification) usage with classic I/O.
- [SNI (Server Name Identification) with async I/O](https://github.com/apache/httpcomponents-core/tree/master/httpcore5/src/test/java/org/apache/hc/core5/http/examples/AsyncClientSNIExample.java)

  This is an example of SNI (Server Name Identification) usage with async I/O.
- [HTTP/2 request priority](https://github.com/apache/httpcomponents-core/tree/master/httpcore5-h2/src/test/java/org/apache/hc/core5/http2/examples/H2RequestExecutionWithPriorityExample.java)

  This is an example of HTTP/2 request that emits H2 Priority via “Priority” header

---

<a id="download"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-core-5.4.x/download.html -->

<!-- page_index: 2 -->

<a id="download--httpcore-downloads"></a>

# HttpCore Downloads

The latest release available for download:

[Release packages](https://hc.apache.org/downloads.html) -
[Release Notes](https://www.apache.org/dist/httpcomponents/httpcore/RELEASE_NOTES-5.4.x.txt) -
[License](https://www.apache.org/licenses/LICENSE-2.0.html)

<a id="download--dependency-management"></a>

## Dependency management

If you are using a dependency manager for your project such as [Apache Maven](https://maven.apache.org), [Gradle](https://gradle.org/) or [Apache Ivy](https://ant.apache.org/projects/ivy.html), you can create a dependency on
HttpCore modules by using this information:

- [HttpCore HTTP/1.1](https://search.maven.org/artifact/org.apache.httpcomponents.core5/httpcore5)
- [HttpCore HTTP/2](https://search.maven.org/artifact/org.apache.httpcomponents.core5/httpcore5-h2)
- [HttpCore Reactive Streams](https://search.maven.org/artifact/org.apache.httpcomponents.core5/httpcore5-reactive)

---

<a id="index"></a>

<!-- source_url: https://hc.apache.org/httpcomponents-core-5.4.x/ -->

<!-- page_index: 3 -->

<a id="index--httpcore-overview"></a>

# HttpCore Overview

HttpCore is a set of low level HTTP transport components that can be used to build custom client and server side HTTP
services with a minimal footprint. HttpCore supports two I/O models: blocking I/O model based on the classic Java I/O
and non-blocking, event driven I/O model based on Java NIO.

<a id="index--documentation"></a>

# Documentation

1. Some examples of HttpCore components in action can be found [here](#examples)
2. Javadocs

   - [HttpCore HTTP/1.1](https://hc.apache.org/httpcomponents-core-5.4.x/current/httpcore5/apidocs/)
   - [HttpCore HTTP/2](https://hc.apache.org/httpcomponents-core-5.4.x/current/httpcore5-h2/apidocs/)
   - [HttpCore Reactive Streams](https://hc.apache.org/httpcomponents-core-5.4.x/current/httpcore5-reactive/apidocs/)
3. API compatibility reports

   - [HttpCore HTTP/1.1](https://hc.apache.org/httpcomponents-core-5.4.x/current/httpcore5/japicmp.html)
   - [HttpCore HTTP/2](https://hc.apache.org/httpcomponents-core-5.4.x/current/httpcore5-h2/japicmp.html)
   - [HttpCore Reactive Streams](https://hc.apache.org/httpcomponents-core-5.4.x/current/httpcore5-reactive/japicmp.html)

<a id="index--standards-compliance"></a>

## Standards Compliance

HttpCore components strive to conform to the following specifications endorsed by the Internet Engineering Task Force
(IETF) and the internet at large:

- [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110) - HTTP Semantics
- [RFC 9112](https://datatracker.ietf.org/doc/html/rfc9112) - Hypertext Transfer Protocol Version 1.1 (HTTP/1.1)
- [RFC 9113](https://datatracker.ietf.org/doc/html/rfc9113) - Hypertext Transfer Protocol Version 2 (HTTP/2)
- [RFC 7541](https://datatracker.ietf.org/doc/html/rfc7541) - HPACK: Header Compression for HTTP/2
- [RFC 1945](https://datatracker.ietf.org/doc/html/rfc1945) - Hypertext Transfer Protocol – HTTP/1.0
- [RFC 2396](https://datatracker.ietf.org/doc/html/rfc2396) - Uniform Resource Identifiers (URI): Generic Syntax
- [RFC 9218](https://datatracker.ietf.org/doc/html/rfc9218) - Extensible Prioritization Scheme for HTTP

---
