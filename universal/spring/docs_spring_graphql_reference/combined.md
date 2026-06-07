# Spring for GraphQL

## Navigation

- Overview
  
- [Overview](#index)
  
- [Server Transports](#transports)
  
- [Request Execution](#request-execution)
  
- [Data Integration](#data)
  
- [Annotated Controllers](#controllers)
  
- [Security](#security)
  
- [Observability](#observability)
  
- [GraalVM Native support](#graalvm-native)
  
- [Federation](#federation)
  
- [Client](#client)
  
- [Code Generation](#codegen)
  
- [GraphiQL](#graphiql)
  
- [Testing](#testing)
  
- [Boot Starter](#boot-starter)
  
- [Standalone Setup](#standalone-setup)
  
- [Samples](#samples)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/index.html -->

<!-- page_index: 1 -->

# Spring for GraphQL

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-for-graphql"></a>

# Spring for GraphQL

Spring for GraphQL provides support for Spring applications built on
[GraphQL Java](https://www.graphql-java.com/). It is a joint collaboration between the
GraphQL Java team and Spring engineering.

Spring for GraphQL is the successor of the
[GraphQL Java Spring](https://github.com/graphql-java/graphql-java-spring) project from
the GraphQL Java team. It aims to be the foundation for all Spring, GraphQL applications.

Please, use our [issue tracker](https://github.com/spring-projects/spring-graphql/issues)
to report a problem, discuss a design issue, or to request a feature.

Check the [Wiki](https://github.com/spring-projects/spring-graphql/wiki) for the latest updates, baseline requirements, upgrade notes, and other cross-version information.

To get started, see the [Boot Starter](#boot-starter) and [Samples](#samples) sections.

[Server Transports](#transports)

---

<a id="transports"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/transports.html -->

<!-- page_index: 2 -->

# Server Transports

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="transports--page-title"></a>
<a id="transports--server-transports"></a>

# Server Transports

Spring for GraphQL supports server handling of GraphQL requests over HTTP, WebSocket, and
RSocket.

<a id="transports--server.transports.http"></a>
<a id="transports--http"></a>

## HTTP

`GraphQlHttpHandler` handles GraphQL over HTTP requests and delegates to the
[Interception](#transports--server.interception) chain for request execution. There are two variants, one for
Spring MVC and one for Spring WebFlux. Both handle requests asynchronously and have
equivalent functionality, but rely on blocking vs non-blocking I/O respectively for
writing the HTTP response.

Requests must use HTTP POST with `"application/json"` as content type and GraphQL request details
included as JSON in the request body. Clients can request the `"application/graphql-response+json"` media type
to get the behavior defined in the official
[GraphQL over HTTP](https://github.com/graphql/graphql-over-http/blob/main/spec/GraphQLOverHTTP.md) specification.
If the client doesn’t express any preference, this will be the content type of choice.
Clients can also request the legacy `"application/json"` media type to get the traditional HTTP behavior.

In practice, GraphQL HTTP clients should expect 4xx/5xx HTTP responses if the server is unavailable, security credentials
are missing or if the request body is not valid JSON. `"application/graphql-response+json"` responses will also use
4xx statuses if the GraphQL document sent by the client cannot be parsed or is considered invalid by the GraphQL engine.
In this case, `"application/json"` responses will still use 200 (OK).
Once the GraphQL request has been successfully validated, the HTTP response status is always 200 (OK), and any errors from GraphQL request execution appear in the "errors" section of the GraphQL response.

`GraphQlHttpHandler` can be exposed as an HTTP endpoint by declaring a `RouterFunction`
bean and using the `RouterFunctions` from Spring MVC or WebFlux to create the route. The
[Boot Starter](#boot-starter) does this, see the
[Web Endpoints](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.transports.http-websocket) section for
details, or check `GraphQlWebMvcAutoConfiguration` or `GraphQlWebFluxAutoConfiguration`
it contains, for the actual config.

By default, the `GraphQlHttpHandler` will serialize and deserialize JSON payloads using the `HttpMessageConverter` (Spring MVC)
and the `DecoderHttpMessageReader/EncoderHttpMessageWriter` (WebFlux) configured in the web framework.
In some cases, the application will configure the JSON codec for the HTTP endpoint in a way that is not compatible with the GraphQL payloads.
Applications can instantiate `GraphQlHttpHandler` with a custom JSON codec that will be used for GraphQL payloads.

<a id="transports--server.transports.sse"></a>
<a id="transports--server-sent-events"></a>

## Server-Sent Events

`GraphQlSseHandler` is very similar to the HTTP handler listed above, but this time handling GraphQL requests over HTTP
using the Server-Sent Events protocol. With this transport, clients must send HTTP POST requests to the endpoint with
`"application/json"` as content type and GraphQL request details included as JSON in the request body; the only
difference with the vanilla HTTP variant is that the client must send `"text/event-stream"` as the `"Accept"` request
header. The response will be sent as one or more Server-Sent Event(s).

This is also defined in the proposed
[GraphQL over HTTP](https://github.com/graphql/graphql-over-http/blob/main/rfcs/GraphQLOverSSE.md) specification.
Spring for GraphQL only implements the "Distinct connections mode", so applications must consider scalability concerns
and whether adopting HTTP/2 as the underlying transport would help.

The main use case for `GraphQlSseHandler` is an alternative to the
[WebSocket transport](#transports--server.transports.websocket), receiving a stream of items as a response to a
subscription operation. Other types of operations, like queries and mutations, are not supported here and should be
using the plain JSON over HTTP transport variant.

<a id="transports--server.transports.http.fileupload"></a>
<a id="transports--file-upload"></a>

### File Upload

As a protocol GraphQL focuses on the exchange of textual data. This doesn’t include binary
data such as images, but there is a separate, informal
[graphql-multipart-request-spec](https://github.com/jaydenseric/graphql-multipart-request-spec)
that allows file uploads with GraphQL over HTTP.

Spring for GraphQL does not support the `graphql-multipart-request-spec` directly.
While the spec does provide the benefit of a unified GraphQL API, the actual experience has
led to a number of issues, and best practice recommendations have evolved, see
[Apollo Server File Upload Best Practices](https://www.apollographql.com/blog/backend/file-uploads/file-upload-best-practices/)
for a more detailed discussion.

If you would like to use `graphql-multipart-request-spec` in your application, you can
do so through the library
[multipart-spring-graphql](https://github.com/nkonev/multipart-spring-graphql).

<a id="transports--server.transports.websocket"></a>
<a id="transports--websocket"></a>

## WebSocket

`GraphQlWebSocketHandler` handles GraphQL over WebSocket requests based on the
[protocol](https://github.com/enisdenjo/graphql-ws/blob/master/PROTOCOL.md) defined in the
[graphql-ws](https://github.com/enisdenjo/graphql-ws) library. The main reason to use
GraphQL over WebSocket is subscriptions which allow sending a stream of GraphQL
responses, but it can also be used for regular queries with a single response.
The handler delegates every request to the [Interception](#transports--server.interception) chain for further
request execution.

> [!TIP]
> GraphQL Over WebSocket Protocols
>
> There are two such protocols, one in the
> [subscriptions-transport-ws](https://github.com/apollographql/subscriptions-transport-ws)
> library and another in the
> [graphql-ws](https://github.com/enisdenjo/graphql-ws) library. The former is not active and
> succeeded by the latter. Read this
> [blog post](https://the-guild.dev/blog/graphql-over-websockets) for the history.

There are two variants of `GraphQlWebSocketHandler`, one for Spring MVC and one for
Spring WebFlux. Both handle requests asynchronously and have equivalent functionality.
The WebFlux handler also uses non-blocking I/O and back pressure to stream messages, which works well since in GraphQL Java a subscription response is a Reactive Streams
`Publisher`.

The `graphql-ws` project lists a number of
[recipes](https://github.com/enisdenjo/graphql-ws#recipes) for client use.

`GraphQlWebSocketHandler` can be exposed as a WebSocket endpoint by declaring a
`SimpleUrlHandlerMapping` bean and using it to map the handler to a URL path. By default, the [Boot Starter](#boot-starter) does not expose a GraphQL over WebSocket endpoint, but you can add a property for the endpoint path to enable it. Please, review
[Web Endpoints](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.transports.http-websocket)
in the Boot reference documentation, and the list of supported `spring.graphql.websocket`
[properties](https://docs.spring.io/spring-boot/appendix/application-properties/index.html#appendix.application-properties.web).
You can also look at `GraphQlWebMvcAutoConfiguration` or `GraphQlWebFluxAutoConfiguration`
for the actual Boot autoconfig details.

The 1.0.x branch of this repository contains a WebFlux
[WebSocket sample](https://github.com/spring-projects/spring-graphql/tree/1.0.x/samples/webflux-websocket) application.

<a id="transports--server.transports.rsocket"></a>
<a id="transports--rsocket"></a>

## RSocket

`GraphQlRSocketHandler` handles GraphQL over RSocket requests. Queries and mutations are
expected and handled as an RSocket `request-response` interaction while subscriptions are
handled as `request-stream`.

`GraphQlRSocketHandler` can be used a delegate from an `@Controller` that is mapped to
the route for GraphQL requests. For example:

```java
import java.util.Map;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import org.springframework.graphql.server.GraphQlRSocketHandler;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.stereotype.Controller;

@Controller
public class GraphQlRSocketController {

	private final GraphQlRSocketHandler handler;

	GraphQlRSocketController(GraphQlRSocketHandler handler) {
		this.handler = handler;
	}

	@MessageMapping("graphql")
	public Mono<Map<String, Object>> handle(Map<String, Object> payload) {
		return this.handler.handle(payload);
	}

	@MessageMapping("graphql")
	public Flux<Map<String, Object>> handleSubscription(Map<String, Object> payload) {
		return this.handler.handleSubscription(payload);
	}
}
```

<a id="transports--server.interception"></a>
<a id="transports--interception"></a>

## Interception

Server transports allow intercepting requests before and after the GraphQL Java engine is
called to process a request.

<a id="transports--server.interception.web"></a>
<a id="transports--webgraphqlinterceptor"></a>

### `WebGraphQlInterceptor`

[HTTP](#transports--server.transports.http) and [WebSocket](#transports--server.transports.websocket)
transports invoke a chain of 0 or more `WebGraphQlInterceptor`, followed by an
`ExecutionGraphQlService` that calls the GraphQL Java engine.
Interceptors allow applications to intercept incoming requests in order to:

- Check HTTP request details
- Customize the `graphql.ExecutionInput`
- Add HTTP response headers
- Customize the `graphql.ExecutionResult`
- and more

Spring for GraphQL provides a built-in `HttpRequestHeaderInterceptor` that copies HTTP headers
from the request to the GraphQL context, which then makes them available to data fetchers
such as annotated controllers. For example in a Spring Boot application this may be done
as follows:

```java
import org.springframework.context.annotation.Bean; import org.springframework.context.annotation.Configuration; import org.springframework.graphql.data.method.annotation.ContextValue; import org.springframework.graphql.data.method.annotation.QueryMapping; import org.springframework.graphql.server.support.HttpRequestHeaderInterceptor; import org.springframework.stereotype.Controller;
@Configuration class RequestHeaderInterceptorConfig {
@Bean public HttpRequestHeaderInterceptor headerInterceptor() { (1) return HttpRequestHeaderInterceptor.builder().mapHeader("myHeader").build();}}
@Controller class MyContextValueController { (2)
@QueryMapping Person person(@ContextValue String myHeader) {...}}
```

**1**

Create interceptor to copy an HTTP request header value into the GraphQLContext

**2**

Data controller method accesses the value

An interceptor can also access values added to the `GraphQLContext` by a controller:

```java
import graphql.GraphQLContext; import reactor.core.publisher.Mono;
import org.springframework.graphql.data.method.annotation.QueryMapping; import org.springframework.graphql.server.WebGraphQlInterceptor; import org.springframework.graphql.server.WebGraphQlRequest; import org.springframework.graphql.server.WebGraphQlResponse; import org.springframework.http.HttpHeaders; import org.springframework.http.ResponseCookie; import org.springframework.stereotype.Controller;
// Subsequent access from a WebGraphQlInterceptor
class ResponseHeaderInterceptor implements WebGraphQlInterceptor {
@Override public Mono<WebGraphQlResponse> intercept(WebGraphQlRequest request, Chain chain) { (2) return chain.next(request).doOnNext((response) -> {String value = response.getExecutionInput().getGraphQLContext().get("cookieName"); ResponseCookie cookie = ResponseCookie.from("cookieName", value).build(); response.getResponseHeaders().add(HttpHeaders.SET_COOKIE, cookie.toString()); });}}
@Controller class MyCookieController {
@QueryMapping Person person(GraphQLContext context) { (1) context.put("cookieName", "123"); ...}}
```

**1**

Controller adds value to the `GraphQLContext`

**2**

Interceptor uses the value to add an HTTP response header

`WebGraphQlHandler` can modify the `ExecutionResult`, for example, to inspect and modify
request validation errors that are raised before execution begins and which cannot be
handled with a `DataFetcherExceptionResolver`:

```java
import java.util.List;

import graphql.GraphQLError;
import graphql.GraphqlErrorBuilder;
import reactor.core.publisher.Mono;

import org.springframework.graphql.server.WebGraphQlInterceptor;
import org.springframework.graphql.server.WebGraphQlRequest;
import org.springframework.graphql.server.WebGraphQlResponse;

class RequestErrorInterceptor implements WebGraphQlInterceptor {

	@Override
	public Mono<WebGraphQlResponse> intercept(WebGraphQlRequest request, Chain chain) {
		return chain.next(request).map((response) -> {
			if (response.isValid()) {
				return response; (1)
			}

			List<GraphQLError> errors = response.getErrors().stream() (2)
					.map((error) -> {
						GraphqlErrorBuilder<?> builder = GraphqlErrorBuilder.newError();
						// ...
						return builder.build();
					})
					.toList();

			return response.transform((builder) -> builder.errors(errors).build()); (3)
		});
	}
}
```

| **1** | Return the same if `ExecutionResult` has a "data" key with non-null value |
| --- | --- |
| **2** | Check and transform the GraphQL errors |
| **3** | Update the `ExecutionResult` with the modified errors |

Use `WebGraphQlHandler` to configure the `WebGraphQlInterceptor` chain. This is supported
by the [Boot Starter](#boot-starter), see
[Web Endpoints](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.transports.http-websocket).

<a id="transports--server.interception.websocket"></a>
<a id="transports--websocketgraphqlinterceptor"></a>

### `WebSocketGraphQlInterceptor`

`WebSocketGraphQlInterceptor` extends `WebGraphQlInterceptor` with additional callbacks
to handle the start and end of a WebSocket connection, in addition to client-side
cancellation of subscriptions. The same also intercepts every GraphQL request on the
WebSocket connection.

Use `WebGraphQlHandler` to configure the `WebGraphQlInterceptor` chain. This is supported
by the [Boot Starter](#boot-starter), see
[Web Endpoints](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.transports.http-websocket).
There can be at most one `WebSocketGraphQlInterceptor` in a chain of interceptors.

There are two built-in WebSocket interceptors called `AuthenticationWebSocketInterceptor`, one for the WebMVC and one for the WebFlux transports. These help to extract authentication
details from the payload of a `"connection_init"` GraphQL over WebSocket message, authenticate, and then propagate the `SecurityContext` to subsequent requests on the WebSocket connection.

> [!TIP]
> There is a websocket-authentication sample in [spring-graphql-examples](https://github.com/spring-projects/spring-graphql-examples).

<a id="transports--server.interception.rsocket"></a>
<a id="transports--rsocketqlinterceptor"></a>

### `RSocketQlInterceptor`

Similar to [`WebGraphQlInterceptor`](#transports--server.interception.web), an `RSocketQlInterceptor` allows intercepting
GraphQL over RSocket requests before and after GraphQL Java engine execution. You can use
this to customize the `graphql.ExecutionInput` and the `graphql.ExecutionResult`.

[Overview](#index)
[Request Execution](#request-execution)

---

<a id="request-execution"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/request-execution.html -->

<!-- page_index: 3 -->

# Request Execution

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="request-execution--page-title"></a>
<a id="request-execution--request-execution"></a>

# Request Execution

`ExecutionGraphQlService` is the main Spring abstraction to call GraphQL Java to execute
requests. Underlying transports, such as the [HTTP](#transports--server.transports.http), delegate to
`ExecutionGraphQlService` to handle requests.

The main implementation, `DefaultExecutionGraphQlService`, is configured with a
`GraphQlSource` for access to the `graphql.GraphQL` instance to invoke.

<a id="request-execution--execution.graphqlsource"></a>
<a id="request-execution--graphqlsource"></a>

## `GraphQLSource`

`GraphQlSource` is a contract to expose the `graphql.GraphQL` instance to use that also
includes a builder API to build that instance. The default builder is available via
`GraphQlSource.schemaResourceBuilder()`.

The [Boot Starter](#boot-starter) creates an instance of this builder and further initializes it
to [load schema files](#request-execution--execution.graphqlsource.schema-resources) from a configurable location, to [expose properties](https://docs.spring.io/spring-boot/appendix/application-properties/index.html#appendix.application-properties.web)
to apply to `GraphQlSource.Builder`, to detect
[`RuntimeWiringConfigurer`](#request-execution--execution.graphqlsource.runtimewiring-configurer) beans, [Instrumentation](https://www.graphql-java.com/documentation/instrumentation) beans for
[GraphQL metrics](#observability--observability), and `DataFetcherExceptionResolver` and `SubscriptionExceptionResolver` beans for
[exception resolution](#request-execution--execution.exceptions). For further customizations, you can also
declare a `GraphQlSourceBuilderCustomizer` bean, for example:

```java
@Configuration(proxyBeanMethods = false) public class GraphQlConfig {
@Bean public GraphQlSourceBuilderCustomizer sourceBuilderCustomizer() {return (builder) -> builder.configureGraphQl((graphQlBuilder) -> graphQlBuilder.executionIdProvider(new CustomExecutionIdProvider()));}
}
```

<a id="request-execution--execution.graphqlsource.schema-resources"></a>
<a id="request-execution--schema-resources"></a>

### Schema Resources

`GraphQlSource.Builder` can be configured with one or more `Resource` instances to be
parsed and merged together. That means schema files can be loaded from just about any
location.

By default, the Boot starter
[looks for schema files](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.schema) with extensions
".graphqls" or ".gqls" under the location `classpath:graphql/**`, which is typically
`src/main/resources/graphql`. You can also use a file system location, or any location
supported by the Spring `Resource` hierarchy, including a custom implementation that
loads schema files from remote locations, from storage, or from memory.

> [!TIP]
> Use `classpath*:graphql/**/` to find schema files across multiple classpath
> locations, e.g. across multiple modules.

<a id="request-execution--execution.graphqlsource.schema-creation"></a>
<a id="request-execution--schema-creation"></a>

### Schema Creation

By default, `GraphQlSource.Builder` uses the GraphQL Java `SchemaGenerator` to create the
`graphql.schema.GraphQLSchema`. This works for typical use, but if you need to use a
different generator, you can register a `schemaFactory` callback:

```java
GraphQlSource.Builder builder = ...

builder.schemaResources(..)
		.configureRuntimeWiring(..)
		.schemaFactory((typeDefinitionRegistry, runtimeWiring) -> {
			// create GraphQLSchema
		})
```

See the [GraphQlSource](#request-execution--execution.graphqlsource) section for how to configure this with Spring Boot.

If interested in federation, please see the [Federation](#federation) section.

<a id="request-execution--execution.graphqlsource.runtimewiring-configurer"></a>
<a id="request-execution--runtimewiringconfigurer"></a>

### `RuntimeWiringConfigurer`

A `RuntimeWiringConfigurer` is useful to register the following:

- Custom scalar types.
- Code that handles [Directives](#request-execution--execution.graphqlsource.directives).
- Direct `DataFetcher` registrations.
- and more…

> [!TIP]
> Spring applications typically do not need to perform direct `DataFetcher` registrations.
> Instead, controller method are registered as `DataFetcher`s via
> `AnnotatedControllerConfigurer`, which is a `RuntimeWiringConfigurer`.

> [!NOTE]
> GraphQL Java, server applications use Jackson only for serialization to and from maps of data.
> Client input is parsed into a map. Server output is assembled into a map based on the field selection set.
> This means you can’t rely on Jackson serialization/deserialization annotations.
> Instead, you can use [custom scalar types](https://www.graphql-java.com/documentation/scalars/).

The [Boot Starter](#boot-starter) detects beans of type `RuntimeWiringConfigurer` and
registers them in the `GraphQlSource.Builder`. That means in most cases, you’ll' have
something like the following in your configuration:

```java
@Configuration
public class GraphQlConfig {

	@Bean
	public RuntimeWiringConfigurer runtimeWiringConfigurer(BookRepository repository) {
		GraphQLScalarType scalarType = ... ;
		SchemaDirectiveWiring directiveWiring = ... ;
		return wiringBuilder -> wiringBuilder
				.scalar(scalarType)
				.directiveWiring(directiveWiring);
	}
}
```

If you need to add a `WiringFactory`, e.g. to make registrations that take into account
schema definitions, implement the alternative `configure` method that accepts both the
`RuntimeWiring.Builder` and an output `List<WiringFactory>`. This allows you to add any
number of factories that are then invoked in sequence.

<a id="request-execution--execution.graphqlsource.default-type-resolver"></a>
<a id="request-execution--typeresolver"></a>

### `TypeResolver`

`GraphQlSource.Builder` registers `ClassNameTypeResolver` as the default `TypeResolver`
to use for GraphQL Interfaces and Unions that don’t already have such a registration
through a [`RuntimeWiringConfigurer`](#request-execution--execution.graphqlsource.runtimewiring-configurer). The purpose of
a `TypeResolver` in GraphQL Java is to determine the GraphQL Object type for values
returned from the `DataFetcher` for a GraphQL Interface or Union field.

`ClassNameTypeResolver` tries to match the simple class name of the value to a GraphQL
Object Type and if it is not successful, it also navigates its super types including
base classes and interfaces, looking for a match. `ClassNameTypeResolver` provides an
option to configure a name extracting function along with `Class` to GraphQL Object type
name mappings that should help to cover more corner cases:

```java
GraphQlSource.Builder builder = ...
ClassNameTypeResolver classNameTypeResolver = new ClassNameTypeResolver();
classNameTypeResolver.setClassNameExtractor((klass) -> {
	// Implement Custom ClassName Extractor here
});
builder.defaultTypeResolver(classNameTypeResolver);
```

See the [GraphQlSource](#request-execution--execution.graphqlsource) section for how to configure this with Spring Boot.

<a id="request-execution--execution.graphqlsource.directives"></a>
<a id="request-execution--directives"></a>

### Directives

The GraphQL language supports directives that "describe alternate runtime execution and
type validation behavior in a GraphQL document". Directives are similar to annotations in
Java but declared on types, fields, fragments and operations in a GraphQL document.

GraphQL Java provides the `SchemaDirectiveWiring` contract to help applications detect
and handle directives. For more details, see
[Schema Directives](https://www.graphql-java.com/documentation/sdl-directives/) in the
GraphQL Java documentation.

In Spring GraphQL you can register a `SchemaDirectiveWiring` through a
[`RuntimeWiringConfigurer`](#request-execution--execution.graphqlsource.runtimewiring-configurer). The [Boot Starter](#boot-starter) detects
such beans, so you might have something like:

```java
@Configuration public class GraphQlConfig {
@Bean public RuntimeWiringConfigurer runtimeWiringConfigurer() {return builder -> builder.directiveWiring(new MySchemaDirectiveWiring());}
}
```

> [!TIP]
> For an example of directives support check out the
> [Extended Validation for Graphql Java](https://github.com/graphql-java/graphql-java-extended-validation)
> library.

<a id="request-execution--execution.graphqlsource.execution-strategy"></a>
<a id="request-execution--executionstrategy"></a>

### `ExecutionStrategy`

An `ExecutionStrategy` in GraphQL Java drives the fetching of requested fields.
To create an `ExecutionStrategy`, you need to provide a `DataFetcherExceptionHandler`.
By default, Spring for GraphQL creates the exception handler to use as described in
[Exceptions](#request-execution--execution.exceptions) and sets it on the
`GraphQL.Builder`. GraphQL Java then uses that to create `AsyncExecutionStrategy`
instances with the configured exception handler.

If you need to create a custom `ExecutionStrategy`, you can detect
`DataFetcherExceptionResolver`s and create an exception handler in the same way, and use
it to create the custom `ExecutionStrategy`. For example, in a Spring Boot application:

```java
@Bean
GraphQlSourceBuilderCustomizer sourceBuilderCustomizer(
		ObjectProvider<DataFetcherExceptionResolver> resolvers) {

	DataFetcherExceptionHandler exceptionHandler =
			DataFetcherExceptionResolver.createExceptionHandler(resolvers.stream().toList());

	AsyncExecutionStrategy strategy = new CustomAsyncExecutionStrategy(exceptionHandler);

	return sourceBuilder -> sourceBuilder.configureGraphQl(builder ->
			builder.queryExecutionStrategy(strategy).mutationExecutionStrategy(strategy));
}
```

<a id="request-execution--execution.graphqlsource.schema-transformation"></a>
<a id="request-execution--schema-transformation"></a>

### Schema Transformation

You can register a `graphql.schema.GraphQLTypeVisitor` via
`builder.schemaResources(..).typeVisitorsToTransformSchema(..)` if you want to traverse
and transform the schema after it is created, and make changes to the schema. Keep in mind
that this is more expensive than [Schema Traversal](#request-execution--execution.graphqlsource.schema-traversal) so generally
prefer traversal to transformation unless you need to make schema changes.

<a id="request-execution--execution.graphqlsource.schema-traversal"></a>
<a id="request-execution--schema-traversal"></a>

### Schema Traversal

You can register a `graphql.schema.GraphQLTypeVisitor` via
`builder.schemaResources(..).typeVisitors(..)` if you want to traverse the schema after
it is created, and possibly apply changes to the `GraphQLCodeRegistry`. Keep in mind, however, that such a visitor cannot change the schema. See
[Schema Transformation](#request-execution--execution.graphqlsource.schema-transformation), if you need to make changes to the schema.

<a id="request-execution--execution.graphqlsource.schema-mapping-inspection"></a>
<a id="request-execution--schema-mapping-inspection"></a>

### Schema Mapping Inspection

If a query, mutation, or subscription operation does not have a `DataFetcher`, it won’t
return any data, and won’t do anything useful. Likewise, fields of schema types that are
neither covered explicitly through a `DataFetcher` registration, nor implicitly by the
default `PropertyDataFetcher` that finds matching `Class` properties, will always be `null`.

GraphQL Java does not perform checks to ensure every schema field is covered, and as a
lower level library, GraphQL Java simply does not know what a `DataFetcher` can return
or what arguments it depends on, and therefore cannot perform such verifications. This can
result in gaps that depending on test coverage may not be discovered until runtime when
clients may experience "silent" `null` values, or non-null field errors.

The `SelfDescribingDataFetcher` interface in Spring for GraphQL allows a `DataFetcher` to
expose information such as return type and expected arguments. All built-in, Spring
`DataFetcher` implementations for [controller methods](#controllers), for
[Querydsl](#data--data.querydsl) and for [Query by Example](#data--data.querybyexample)
are implementations of this interface. For annotated controllers, the return type and
expected arguments are based on the controller method signature. This makes it possible
to inspect schema mappings on startup to ensure the following:

- Schema fields have either a `DataFetcher` registration or a corresponding `Class` property.
- `DataFetcher` registrations refer to a schema field that exists.
- `DataFetcher` arguments have matching schema field arguments.

If the application is written in Kotlin, or is using [Null-safety](https://docs.spring.io/spring-framework/reference/core/null-safety.html)
annotations, further inspections can be performed. The GraphQL schema can declare nullable types (`Book`) and
non-nullable types (`Book!`).
As a result, we can ensure that the application does not break the nullness requirements of the schema.

When schema fields are non-null, we ensure that the relevant `Class` properties and `DataFetcher` return types
are also non-null. The opposite situation is not considered as an error: when the schema has a nullable field `author: Author`
and the application declares a `@NonNull Author getAuthor();`, the inspector does not raise this as an error.
Applications should not necessarily make fields non-null in the schema, as any error during a data fetching operation
will force the GraphQL engine tu null out fields in the hierarchy up until `null` is allowed.
Partial responses is a key GraphQL feature, so the schema should be designed with nullness in mind.

When field arguments are nullable, we ensure that `DataFetcher` parameters are also nullable.
In this case, user input should not be fed to the application if it breaks the nullability contract as this will lead
to runtime failures.

To enable schema inspection, customize `GraphQlSource.Builder` as shown below.
In this case the report is simply logged, but you can choose to take any action:

```java
GraphQlSource.Builder builder = ...

builder.schemaResources(..)
		.inspectSchemaMappings(report -> {
			logger.debug(report);
		});
```

An example report:

```
GraphQL schema inspection:
    Unmapped fields: {Book=[title], Author[firstName, lastName]} (1)
    Unmapped registrations: {Book.reviews=BookController#reviews[1 args]} (2)
    Unmapped arguments: {BookController#bookSearch[1 args]=[myAuthor]} (3)
    Field nullness errors: {Book=[title is NON_NULL -> 'Book#title' is NULLABLE]} (4)
    Argument nullness errors: {BookController#bookById[1 args]=[java.lang.String id should be NULLABLE]} (5)
    Skipped types: [BookOrAuthor] (6)
```

| **1** | Schema fields that are not covered in any way |
| --- | --- |
| **2** | `DataFetcher` registrations to fields that don’t exist |
| **3** | `DataFetcher` expected arguments that don’t exist |
| **4** | "title" schema field is non null, but `Book.getTitle()` is `@Nullable` |
| **5** | `bookById(id: ID)` has a nullable "id" argument, but `Book bookById(@NonNull String id)` is non null. |
| **6** | Schema types that have been skipped (explained next) |

In some cases, the `Class` type for a schema type is unknown. Maybe the `DataFetcher` does not
implement `SelfDescribingDataFetcher`, or the declared return type is too general
(e.g. `Object`) or unknown (e.g. `List<?>`), or a `DataFetcher` could be missing altogether.
In such cases, the schema type is listed as skipped as it could not be verified. For every
skipped type, a DEBUG message explains why it was skipped.

<a id="request-execution--execution.graphqlsource.schema-mapping-inspection-unions-interfaces"></a>
<a id="request-execution--unions-and-interfaces"></a>

#### Unions and Interfaces

For unions, the inspection iterates over member types and tries to find the corresponding
classes. For interfaces, the inspection iterates over implementation types and looks
for the corresponding classes.

By default, corresponding Java classes can be detected out-of-the-box in the following cases:

- The `Class`'s simple name matches the GraphQL union member of interface implementation
  type name, *and* the `Class` is located in the same package as the return type of the
  controller method, or controller class, mapped to the union or interface field.
- The `Class` is inspected in other parts of the schema where the mapped field is of a
  concrete union member or interface implementation type.
- You have registered a
  [TypeResolver](#request-execution--execution.graphqlsource.default-type-resolver)
  that has explicit `Class` to GraphQL type mappings .

In none the above help, and GraphQL types are reported as skipped in the schema inspection
report, you can make the following customizations:

- Explicitly map a GraphQL type name to a Java class or classes.
- Configure a function that customizes how a GraphQL type name is adapted to a simple
  `Class` name. This can help with a specific Java class naming conventions.
- Provide a `ClassNameTypeResolver` to map a GraphQL type a Java classes.

For example:

```java
GraphQlSource.Builder builder = ...

builder.schemaResources(..)
	.inspectSchemaMappings(
		initializer -> initializer.classMapping("Author", Author.class)
		logger::debug);
```

<a id="request-execution--execution.graphqlsource.operation-caching"></a>
<a id="request-execution--operation-caching"></a>

### Operation Caching

GraphQL Java must *parse* and *validate* an operation before executing it. This may impact
performance significantly. To avoid the need to re-parse and validate, an application may
configure a `PreparsedDocumentProvider` that caches and reuses Document instances. The
[GraphQL Java docs](https://www.graphql-java.com/documentation/execution/#query-caching) provide more details on
query caching through a `PreparsedDocumentProvider`.

In Spring GraphQL you can register a `PreparsedDocumentProvider` through
`GraphQlSource.Builder#configureGraphQl`:
.

```java
// Typically, accessed through Spring Boot's GraphQlSourceBuilderCustomizer
GraphQlSource.Builder builder = ...

// Create provider
PreparsedDocumentProvider provider =
        new ApolloPersistedQuerySupport(new InMemoryPersistedQueryCache(Collections.emptyMap()));

builder.schemaResources(..)
		.configureRuntimeWiring(..)
		.configureGraphQl(graphQLBuilder -> graphQLBuilder.preparsedDocumentProvider(provider))
```

See the [GraphQlSource](#request-execution--execution.graphqlsource) section for how to configure this with Spring Boot.

<a id="request-execution--execution.thread-model"></a>
<a id="request-execution--thread-model"></a>

## Thread Model

Most GraphQL requests benefit from concurrent execution in fetching nested fields. This is
why most applications today rely on GraphQL Java’s `AsyncExecutionStrategy`, which allows
data fetchers to return `CompletionStage` and to execute concurrently rather than serially.

Java 21 and virtual threads add an important ability to use more threads efficiently, but
it is still necessary to execute concurrently rather than serially in order for request
execution to complete more quickly.

Spring for GraphQL supports:

- [Reactive data fetchers](#request-execution--execution.reactive-datafetcher), and those are
  adapted to `CompletionStage` as expected by `AsyncExecutionStrategy`.
- `CompletionStage` as return value.
- Controller methods that are Kotlin coroutine methods.
- [@SchemaMapping](#controllers--controllers.schema-mapping) and
  [@BatchMapping](#controllers--controllers.schema-mapping) methods can return
  `Callable` that is submitted to an `Executor` such as the Spring Framework
  `VirtualThreadTaskExecutor`. To enable this, you must configure an `Executor` on
  `AnnotatedControllerConfigurer`.

Spring for GraphQL runs on either Spring MVC or WebFlux as the transport. Spring MVC
uses async request execution, unless the resulting `CompletableFuture` is done
immediately after the GraphQL Java engine returns, which would be the case if the
request is simple enough and did not require asynchronous data fetching.

<a id="request-execution--execution.timeout"></a>
<a id="request-execution--graphql-request-timeout"></a>

## GraphQL Request Timeout

GraphQL clients can send requests that will consume lots of resources on the server side.
There are many ways to protect against this, and one of them is to configure a request timeout.
This ensures that requests are closed on the server side if the response takes too long to materialize.

Spring for GraphQL provides a `TimeoutWebGraphQlInterceptor` for the web transports.
Applications can configure this interceptor with a timeout duration; if the request times out, the server errors with a specific HTTP status.
In this case, the interceptor will send a "cancel" signal up the chain and reactive data fetchers will automatically cancel any ongoing work.

This interceptor can be configured on the `WebGraphQlHandler`:

```java
TimeoutWebGraphQlInterceptor timeoutInterceptor = new TimeoutWebGraphQlInterceptor(Duration.ofSeconds(5));
WebGraphQlHandler webGraphQlHandler = WebGraphQlHandler
		.builder(executionGraphQlService)
		.interceptor(timeoutInterceptor)
		.build();
GraphQlHttpHandler httpHandler = new GraphQlHttpHandler(webGraphQlHandler);
```

In a Spring Boot application, contributing the interceptor as a bean is enough:

```java
import java.time.Duration;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.graphql.server.TimeoutWebGraphQlInterceptor;

@Configuration(proxyBeanMethods = false)
public class HttpTimeoutConfiguration {

	@Bean
	public TimeoutWebGraphQlInterceptor timeoutWebGraphQlInterceptor() {
		return new TimeoutWebGraphQlInterceptor(Duration.ofSeconds(5));
	}

}
```

For more transport-specific timeouts, there are dedicated properties on the handler implementations like
`GraphQlWebSocketHandler` and `GraphQlSseHandler`.

<a id="request-execution--execution.reactivedatafetcher"></a>
<a id="request-execution--reactive-datafetcher"></a>

## Reactive `DataFetcher`

The default `GraphQlSource` builder enables support for a `DataFetcher` to return `Mono`
or `Flux` which adapts those to a `CompletableFuture` where `Flux` values are aggregated
and turned into a List, unless the request is a GraphQL subscription request, in which case the return value remains a Reactive Streams `Publisher` for streaming
GraphQL responses.

A reactive `DataFetcher` can rely on access to Reactor context propagated from the
transport layer, such as from a WebFlux request handling, see
[WebFlux Context](#request-execution--execution.context.webflux).

In the case of subscription requests, GraphQL Java will produce items as soon as they
are available and all their requested fields were fetched. Because this involves several
layers of asynchronous data fetching, items might be sent over the wire out of their
original order. If you wish GraphQL Java to buffer items and retain the original order, you can do so by setting the `SubscriptionExecutionStrategy.KEEP_SUBSCRIPTION_EVENTS_ORDERED`
configuration flag in the `GraphQLContext`. This can be done, for example, with a custom
`Instrumentation`:

```java
import graphql.ExecutionResult;
import graphql.execution.SubscriptionExecutionStrategy;
import graphql.execution.instrumentation.InstrumentationContext;
import graphql.execution.instrumentation.InstrumentationState;
import graphql.execution.instrumentation.SimpleInstrumentationContext;
import graphql.execution.instrumentation.SimplePerformantInstrumentation;
import graphql.execution.instrumentation.parameters.InstrumentationExecutionParameters;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration(proxyBeanMethods = false)
public class GraphQlConfig {

	@Bean
	public SubscriptionOrderInstrumentation subscriptionOrderInstrumentation() {
		return new SubscriptionOrderInstrumentation();
	}

	static class SubscriptionOrderInstrumentation extends SimplePerformantInstrumentation {

		@Override
		public InstrumentationContext<ExecutionResult> beginExecution(InstrumentationExecutionParameters parameters,
																InstrumentationState state) {
			// Enable option for keeping subscription results in upstream order
			parameters.getGraphQLContext().put(SubscriptionExecutionStrategy.KEEP_SUBSCRIPTION_EVENTS_ORDERED, true);
			return SimpleInstrumentationContext.noOp();
		}

	}

}
```

<a id="request-execution--execution.context"></a>
<a id="request-execution--context-propagation"></a>

## Context Propagation

Spring for GraphQL provides support to transparently propagate context from the
[HTTP](#transports--server.transports.http) transport, through GraphQL Java, and to
`DataFetcher` and other components it invokes. This includes both `ThreadLocal` context
from the Spring MVC request handling thread and Reactor `Context` from the WebFlux
processing pipeline.

<a id="request-execution--execution.context.webmvc"></a>
<a id="request-execution--webmvc"></a>

### WebMvc

A `DataFetcher` and other components invoked by GraphQL Java may not always execute on
the same thread as the Spring MVC handler, for example if an asynchronous
[`WebGraphQlInterceptor`](#transports--server.interception) or `DataFetcher` switches to a
different thread.

Spring for GraphQL supports propagating `ThreadLocal` values from the Servlet container
thread to the thread a `DataFetcher` and other components invoked by GraphQL Java to
execute on. To do this, an application needs to implement
`io.micrometer.context.ThreadLocalAccessor` for a `ThreadLocal` values of interest:

```java
public class RequestAttributesAccessor implements ThreadLocalAccessor<RequestAttributes> {
@Override public Object key() {return RequestAttributesAccessor.class.getName();}
@Override public RequestAttributes getValue() {return RequestContextHolder.getRequestAttributes();}
@Override public void setValue(RequestAttributes attributes) {RequestContextHolder.setRequestAttributes(attributes);}
@Override public void reset() {RequestContextHolder.resetRequestAttributes();}
}
```

You can register a `ThreadLocalAccessor` manually on startup with the global
`ContextRegistry` instance, which is accessible via
`io.micrometer.context.ContextRegistry#getInstance()`. You can also register it
automatically through the `java.util.ServiceLoader` mechanism.

<a id="request-execution--execution.context.webflux"></a>
<a id="request-execution--webflux"></a>

### WebFlux

A [Reactive `DataFetcher`](#request-execution--execution.reactive-datafetcher) can rely on access to Reactor context that
originates from the WebFlux request handling chain. This includes Reactor context
added by [WebGraphQlInterceptor](#transports--server.interception) components.

<a id="request-execution--execution.exceptions"></a>
<a id="request-execution--exceptions"></a>

## Exceptions

In GraphQL Java, `DataFetcherExceptionHandler` decides how to represent exceptions from
data fetching in the "errors" section of the response. An application can register a
single handler only.

Spring for GraphQL registers a `DataFetcherExceptionHandler` that provides default
handling and enables the `DataFetcherExceptionResolver` contract. An application can
register any number of resolvers via [`GraphQLSource`](#request-execution--execution.graphqlsource) builder and those are in
order until one them resolves the `Exception` to a `List<graphql.GraphQLError>`.
The Spring Boot starter detects beans of this type.

`DataFetcherExceptionResolverAdapter` is a convenient base class with protected methods
`resolveToSingleError` and `resolveToMultipleErrors`.

The [Annotated Controllers](#controllers) programming model enables handling data fetching exceptions with
annotated exception handler methods with a flexible method signature, see
[`@GraphQlExceptionHandler`](#controllers--controllers.exception-handler) for details.

A `GraphQLError` can be assigned to a category based on the GraphQL Java
`graphql.ErrorClassification`, or the Spring GraphQL `ErrorType`, which defines the following:

- `BAD_REQUEST`
- `UNAUTHORIZED`
- `FORBIDDEN`
- `NOT_FOUND`
- `INTERNAL_ERROR`

If an exception remains unresolved, by default it is categorized as an `INTERNAL_ERROR`
with a generic message that includes the category name and the `executionId` from
`DataFetchingEnvironment`. The message is intentionally opaque to avoid leaking
implementation details. Applications can use a `DataFetcherExceptionResolver` to customize
error details.

Unresolved exception are logged at ERROR level along with the `executionId` to correlate
to the error sent to the client. Resolved exceptions are logged at DEBUG level.

<a id="request-execution--execution.exceptions.request"></a>
<a id="request-execution--request-exceptions"></a>

### Request Exceptions

The GraphQL Java engine may run into validation or other errors when parsing the request
and that in turn prevent request execution. In such cases, the response contains a
"data" key with `null` and one or more request-level "errors" that are global, i.e. not
having a field path.

`DataFetcherExceptionResolver` cannot handle such global errors because they are raised
before execution begins and before any `DataFetcher` is invoked. An application can use
transport level interceptors to inspect and transform errors in the `ExecutionResult`.
See examples under [`WebGraphQlInterceptor`](#transports--server.interception.web).

<a id="request-execution--execution.exceptions.subscription"></a>
<a id="request-execution--subscription-exceptions"></a>

### Subscription Exceptions

The `Publisher` for a subscription request may complete with an error signal in which case
the underlying transport (e.g. WebSocket) sends a final "error" type message with a list
of GraphQL errors.

`DataFetcherExceptionResolver` cannot resolve errors from a subscription `Publisher`, since the data `DataFetcher` only creates the `Publisher` initially. After that, the
transport subscribes to the `Publisher` that may then complete with an error.

An application can register a `SubscriptionExceptionResolver` in order to resolve
exceptions from a subscription `Publisher` in order to resolve those to GraphQL errors
to send to the client.

<a id="request-execution--execution.pagination"></a>
<a id="request-execution--pagination"></a>

## Pagination

The GraphQL [Cursor Connection specification](https://relay.dev/graphql/connections.htm)
defines a way to navigate large result sets by returning a subset of items at a time in
which each item is paired with a cursor that clients can use to request more items before
or after the referenced item.

The specification calls this pattern *"Connections"*, and schema types whose name end
with `~Connection` are a connection type that represents a paginated result set.
All connection types contain a field called "edges" where an `~Edge` type contains
the actual item, a cursor, and a field called "pageInfo" that indicates if more
items exist forward and backward.

<a id="request-execution--execution.pagination.types"></a>
<a id="request-execution--connection-types"></a>

### Connection Types

Connection types require boilerplate definitions that Spring for GraphQL’s
`ConnectionTypeDefinitionConfigurer` can add transparently on startup, if not explicitly
declared. That means you only need the below, and the connection and edge types will
be added for you:

```graphql
type Query {books(first:Int, after:String, last:Int, before:String): BookConnection}
type Book {id: ID! title: String!}
```

The spec defined `first` and `after` arguments for forward pagination allow clients to
request the "first" N items "after" a given cursor. Similarly, the `last` and `before`
arguments for backward pagination arguments allow requesting the "last" N items "before"
a given cursor.

> [!NOTE]
> The spec discourages including both `first` and `last` and also states the outcome
> for pagination becomes unclear. In Spring for GraphQL if `first` or `after` are present, then `last` and `before` are ignored.

To have connection types generated, configure `ConnectionTypeDefinitionConfigurer` as follows:

```java
GraphQlSource.schemaResourceBuilder()
		.schemaResources(..)
		.typeDefinitionConfigurer(new ConnectionTypeDefinitionConfigurer)
```

The above will add the following type definitions:

```graphql
type BookConnection {edges: [BookEdge]! pageInfo: PageInfo!}
type BookEdge {node: Book! cursor: String!}
type PageInfo {hasPreviousPage: Boolean! hasNextPage: Boolean! startCursor: String endCursor: String}
```

The [Boot Starter](#boot-starter) registers `ConnectionTypeDefinitionConfigurer` by default.

<a id="request-execution--execution.pagination.adapters"></a>
<a id="request-execution--connectionadapter"></a>

### `ConnectionAdapter`

In addition to
[Connection Types](#request-execution--execution.pagination.types) in the schema, you will also need equivalent Java types. GraphQL Java provides those, including generic
`Connection` and `Edge` types, and `PageInfo`.

You can return `Connection` from a controller method, but it requires boilerplate code
to adapt your underlying data pagination mechanism to `Connection`, to create cursors, add `~Edge` wrappers, and create a `PageInfo`.

Spring for GraphQL defines the `ConnectionAdapter` contract to adapt a container of items
to `Connection`. Adapters are invoked from a `DataFetcher` decorator that is in turn
added by a `ConnectionFieldTypeVisitor`. You can configure it as follows:

```java
ConnectionAdapter adapter = ... ;
GraphQLTypeVisitor visitor = ConnectionFieldTypeVisitor.create(List.of(adapter)) (1)

GraphQlSource.schemaResourceBuilder()
		.schemaResources(..)
		.typeDefinitionConfigurer(..)
		.typeVisitors(List.of(visitor)) (2)
```

**1**

Create type visitor with one or more `ConnectionAdapter`s.

**2**

Resister the type visitor.

There are built-in [built-in](#data--data.pagination.scroll) `ConnectionAdapter`s
for Spring Data’s `Window` and `Slice`. You can also create your own custom adapter.
`ConnectionAdapter` implementations rely on a
[`CursorStrategy`](#request-execution--execution.pagination.cursor.strategy) to
create cursors for returned items. The same strategy is also used to support the
[`Subrange`](#controllers--controllers.schema-mapping.subrange) controller method
argument that contains pagination input.

<a id="request-execution--execution.pagination.cursor.strategy"></a>
<a id="request-execution--cursorstrategy"></a>

### `CursorStrategy`

`CursorStrategy` is a contract to encode and decode a String cursor that refers to the
position of an item within a large result set. The cursor can be based on an index or
on a keyset.

A [`ConnectionAdapter`](#request-execution--execution.pagination.adapters) uses this to encode cursors for returned items.
[Annotated Controllers](#controllers) methods, [Querydsl](#data--data.querydsl) repositories, and [Query by Example](#data--data.querybyexample)
repositories use it to decode cursors from pagination requests, and create a `Subrange`.

`CursorEncoder` is a related contract that further encodes and decodes String cursors to
make them opaque to clients. `EncodingCursorStrategy` combines `CursorStrategy` with a
`CursorEncoder`. You can use `Base64CursorEncoder`, `NoOpEncoder` or create your own.

There is a [built-in](#data--data.pagination.scroll) `CursorStrategy` for the Spring Data
`ScrollPosition`. The [Boot Starter](#boot-starter) registers a `CursorStrategy<ScrollPosition>` with
`Base64Encoder` when Spring Data is present.

<a id="request-execution--execution.pagination.sort.strategy"></a>
<a id="request-execution--sort"></a>

### Sort

There is no standard way to provide sort information in a GraphQL request. However, pagination depends on a stable sort order. You can use a default order, or otherwise
expose input types and extract sort details from GraphQL arguments.

There is [built-in](#data--data.pagination.sort) support for Spring Data’s `Sort` as a controller
method argument. For this to work, you need to have a `SortStrategy` bean.

<a id="request-execution--execution.batching"></a>
<a id="request-execution--batch-loading"></a>

## Batch Loading

Given a `Book` and its `Author`, we can create one `DataFetcher` for a book and another
for its author. This allows selecting books with or without authors, but it means books
and authors aren’t loaded together, which is especially inefficient when querying multiple
books as the author for each book is loaded individually. This is known as the N+1 select
problem.

<a id="request-execution--execution.batching.dataloader"></a>
<a id="request-execution--dataloader"></a>

### `DataLoader`

GraphQL Java provides a `DataLoader` mechanism for batch loading of related entities.
You can find the full details in the
[GraphQL Java docs](https://www.graphql-java.com/documentation/batching/). Below is a
summary of how it works:

1. Register `DataLoader`s in the `DataLoaderRegistry` that can load entities, given unique keys.
2. `DataFetcher`s can access `DataLoader`s and use them to load entities by id.
3. A `DataLoader` defers loading by returning a future so it can be done in a batch.
4. `DataLoader`s maintain a per request cache of loaded entities that can further
   improve efficiency.

<a id="request-execution--execution.batching.batch-loader-registry"></a>
<a id="request-execution--batchloaderregistry"></a>

### `BatchLoaderRegistry`

The complete batching loading mechanism in GraphQL Java requires implementing one of
several `BatchLoader` interface, then wrapping and registering those as `DataLoader`s
with a name in the `DataLoaderRegistry`.

The API in Spring GraphQL is slightly different. For registration, there is only one, central `BatchLoaderRegistry` exposing factory methods and a builder to create and
register any number of batch loading functions:

```java
@Configuration public class MyConfig {
public MyConfig(BatchLoaderRegistry registry) {
registry.forTypePair(Long.class, Author.class).registerMappedBatchLoader((authorIds, env) -> {// return Mono<Map<Long, Author> });
// more registrations ...}
}
```

The [Boot Starter](#boot-starter) declares a `BatchLoaderRegistry` bean that you can inject into
your configuration, as shown above, or into any component such as a controller in order
register batch loading functions. In turn the `BatchLoaderRegistry` is injected into
`DefaultExecutionGraphQlService` where it ensures `DataLoader` registrations per request.

By default, the `DataLoader` name is based on the class name of the target entity.
This allows an `@SchemaMapping` method to declare a
[DataLoader argument](#controllers--controllers.schema-mapping.data-loader) with a generic type, and
without the need for specifying a name. The name, however, can be customized through the
`BatchLoaderRegistry` builder, if necessary, along with other `DataLoaderOptions`.

To configure default `DataLoaderOptions` globally, to use as a starting point for any
registration, you can override Boot’s `BatchLoaderRegistry` bean and use the constructor
for `DefaultBatchLoaderRegistry` that accepts `Supplier<DataLoaderOptions>`.

For many cases, when loading related entities, you can use
[@BatchMapping](#controllers--controllers.batch-mapping) controller methods, which are a shortcut
for and replace the need to use `BatchLoaderRegistry` and `DataLoader` directly.

`BatchLoaderRegistry` provides other important benefits too. It supports access to
the same `GraphQLContext` from batch loading functions and from `@BatchMapping` methods, as well as ensures [Context Propagation](#request-execution--execution.context) to them. This is why applications are expected
to use it. It is possible to perform your own `DataLoader` registrations directly but
such registrations would forgo the above benefits.

<a id="request-execution--execution.batching.recipes"></a>
<a id="request-execution--batch-loading-recipes"></a>

### Batch Loading Recipes

For straightforward cases, the [@BatchMapping](#controllers--controllers.batch-mapping) annotation is often
the best choice, with minimal boilerplate. For more advanced use cases, the `BatchLoaderRegistry` offers more flexibility.

[As outlined above](#request-execution--execution.batching.dataloader), `DataLoader`s will queue `load()` calls
and might dispatch them all at once, or in batches. This means that a single dispatch can load entities for different
`@SchemaMapping` calls and different GraphQL contexts. Because loaded entities will be cached by their key by GraphQL Java, for the entire lifetime of the request, developers should consider different strategies to optimize memory consumption vs. number of I/O calls.

For the next section, we will consider the following schema for loading information about friends.
Notice that we can filter friends and only load friends with a particular favorite beverage.

```graphql
type Query {me: Person people: [Person]}
input FriendsFilter {favoriteBeverage: String}
type Person {id: ID! name: String favoriteBeverage: String friends(filter: FriendsFilter): [Person]}
```

We can approach this problem by first loading all friends for a given person in the `DataLoader`, then filter out unnecessary ones at the `@SchemaMapping` level. This will load more `Person` instances
in the `DataLoader` cache and use more memory, but it’s likely to perform less I/O calls.

```java
public FriendsControllerFiltering(BatchLoaderRegistry registry) {registry.forTypePair(Integer.class, Person.class).registerMappedBatchLoader((personIds, env) -> {Map<Integer, Person> friends = new HashMap<>(); personIds.forEach((personId) -> friends.put(personId, this.people.get(personId))); (1) return Mono.just(friends); });}
@QueryMapping public Person me() {return ...}
@QueryMapping public Collection<Person> people() {return ...}
@SchemaMapping public CompletableFuture<List<Person>> friends(Person person, @Argument FriendsFilter filter, DataLoader<Integer, Person> dataLoader) {return dataLoader .loadMany(person.friendsId()) .thenApply(filter::apply); (2)}
public record FriendsFilter(String favoriteBeverage) {
List<Person> apply(List<Person> friends) {return friends.stream() .filter((person) -> person.favoriteBeverage.equals(this.favoriteBeverage)) .toList();}}
```

**1**

fetch all friends and do not apply filter, caching Person by their id

**2**

load all friends, then apply the given filter

This is well suited for small groups of well-connected friends and for popular beverages.
If instead we’re dealing with large groups of friends and few friends in common, or more niche beverages, we risk loading large amounts of data in memory for just a few entries actually sent to the client.

Here, we can use a different strategy by batch loading entities with a composed key: the person and the chosen filter.
This approach will load just enough entities in memory, at the cost of possible duplicates `Person` in the cache
and more I/O operations.

```java
public FriendsControllerComposedKey(BatchLoaderRegistry registry) {registry.forTypePair(FriendFilterKey.class, Person[].class).registerMappedBatchLoader((keys, env) -> {return dataStore.load(keys); Map<FriendFilterKey, Person[]> result = new HashMap<>(); keys.forEach((key) -> { (2) Person[] friends = key.person().friendsId().stream() .map(this.people::get) .filter((friend) -> key.friendsFilter().matches(friend)) .toArray(Person[]::new); result.put(key, friends); }); return Mono.just(result); });}
@QueryMapping public Person me() {return ...}
@QueryMapping public Collection<Person> people() {return ...}
@SchemaMapping public CompletableFuture<Person[]> friends(Person person, @Argument FriendsFilter filter, DataLoader<FriendFilterKey, Person[]> dataLoader) {return dataLoader.load(new FriendFilterKey(person, filter));}
public record FriendsFilter(String favoriteBeverage) {boolean matches(Person friend) {return friend.favoriteBeverage.equals(this.favoriteBeverage);}}
public record FriendFilterKey(Person person, FriendsFilter friendsFilter) { (1)}
```

**1**

because this key contains both the person and the filter, we will need to fetch the same friend multiple times

In both cases, the query:

```graphql
query {me {name friends(filter: {favoriteBeverage: "tea"}) {name favoriteBeverage}} people {name friends(filter: {favoriteBeverage: "coffee"}) {name favoriteBeverage}}}
```

Will yield the following result:

```json
{"data": {"me": {"name": "Brian","friends": [{"name": "Donna","favoriteBeverage": "tea"}] },"people": [{"name": "Andi","friends": [{"name": "Rossen","favoriteBeverage": "coffee" },{"name": "Brad","favoriteBeverage": "coffee"}] },{"name": "Brad","friends": [{"name": "Rossen","favoriteBeverage": "coffee" },{"name": "Andi","favoriteBeverage": "coffee"}] },{"name": "Donna","friends": [{"name": "Rossen","favoriteBeverage": "coffee" },{"name": "Brad","favoriteBeverage": "coffee"}] },{"name": "Brian","friends": [{"name": "Rossen","favoriteBeverage": "coffee"}] },{"name": "Rossen","friends": []}]}}
```

<a id="request-execution--execution.batching.testing"></a>
<a id="request-execution--testing-batch-loading"></a>

### Testing Batch Loading

Start by having `BatchLoaderRegistry` perform registrations on a `DataLoaderRegistry`:

```java
BatchLoaderRegistry batchLoaderRegistry = new DefaultBatchLoaderRegistry();
// perform registrations...

DataLoaderRegistry dataLoaderRegistry = DataLoaderRegistry.newRegistry().build();
batchLoaderRegistry.registerDataLoaders(dataLoaderRegistry, graphQLContext);
```

Now you can access and test individual `DataLoader`'s as follows:

```java
DataLoader<Long, Book> loader = dataLoaderRegistry.getDataLoader(Book.class.getName());
loader.load(1L);
loader.loadMany(Arrays.asList(2L, 3L));
List<Book> books = loader.dispatchAndJoin(); // actual loading

assertThat(books).hasSize(3);
assertThat(books.get(0).getName()).isEqualTo("...");
// ...
```

[Server Transports](#transports)
[Data Integration](#data)

---

<a id="data"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/data.html -->

<!-- page_index: 4 -->

# Data Integration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="data--page-title"></a>
<a id="data--data-integration"></a>

# Data Integration

Spring for GraphQL lets you leverage existing Spring technology, following common
programming models to expose underlying data sources through GraphQL.

This section discusses an integration layer for Spring Data that provides an easy way to
adapt a Querydsl or a Query by Example repository to a `DataFetcher`, including the
option for automated detection and GraphQL Query registration for repositories marked
with `@GraphQlRepository`.

<a id="data--data.querydsl"></a>
<a id="data--querydsl"></a>

## Querydsl

Spring for GraphQL supports use of [Querydsl](http://www.querydsl.com/) to fetch data through
the Spring Data
[Querydsl extension](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#core.extensions).
Querydsl provides a flexible yet typesafe approach to express query predicates by
generating a meta-model using annotation processors.

For example, declare a repository as `QuerydslPredicateExecutor`:

```java
public interface AccountRepository extends Repository<Account, Long>,
			QuerydslPredicateExecutor<Account> {
}
```

Then use it to create a `DataFetcher`:

```java
// For single result queries
DataFetcher<Account> dataFetcher =
		QuerydslDataFetcher.builder(repository).single();

// For multi-result queries
DataFetcher<Iterable<Account>> dataFetcher =
		QuerydslDataFetcher.builder(repository).many();

// For paginated queries
DataFetcher<Iterable<Account>> dataFetcher =
		QuerydslDataFetcher.builder(repository).scrollable();
```

You can now register the above `DataFetcher` through a
[`RuntimeWiringConfigurer`](#request-execution--execution.graphqlsource.runtimewiring-configurer).

The `DataFetcher` builds a Querydsl `Predicate` from GraphQL arguments, and uses it to
fetch data. Spring Data supports `QuerydslPredicateExecutor` for JPA, MongoDB, Neo4j, and LDAP.

> [!NOTE]
> For a single argument that is a GraphQL input type, `QuerydslDataFetcher` nests one
> level down, and uses the values from the argument sub-map.

If the repository is `ReactiveQuerydslPredicateExecutor`, the builder returns
`DataFetcher<Mono<Account>>` or `DataFetcher<Flux<Account>>`. Spring Data supports this
variant for MongoDB and Neo4j.

<a id="data--data.querydsl.build"></a>
<a id="data--build-setup"></a>

### Build Setup

To configure Querydsl in your build, follow the
[official reference documentation](https://querydsl.com/static/querydsl/latest/reference/html/ch02.html):

For example:

- Gradle
- Maven

```groovy
dependencies {//...
annotationProcessor "com.querydsl:querydsl-apt:$querydslVersion:jakarta",'jakarta.persistence:jakarta.persistence-api'}
compileJava {options.annotationProcessorPath = configurations.annotationProcessor}
```

```xml
<build>
	<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<configuration>
					<annotationProcessorPaths>
						<!-- Explicit opt-in required via annotationProcessors or
										annotationProcessorPaths on Java 22+, see https://bugs.openjdk.org/browse/JDK-8306819 -->
						<annotationProcessorPath>
							<groupId>com.querydsl</groupId>
							<artifactId>querydsl-apt</artifactId>
							<version>${querydsl.version}</version>
							<classifier>jakarta</classifier>
						</annotationProcessorPath>
						<annotationProcessorPath>
							<groupId>jakarta.persistence</groupId>
							<artifactId>jakarta.persistence-api</artifactId>
						</annotationProcessorPath>
					</annotationProcessorPaths>

					<!-- Recommended: Some IDE's might require this configuration to include generated sources for IDE usage -->
					<generatedTestSourcesDirectory>target/generated-test-sources</generatedTestSourcesDirectory>
					<generatedSourcesDirectory>target/generated-sources</generatedSourcesDirectory>
				</configuration>
			</plugin>
	</plugins>
</build>
```

<a id="data--data.querydsl.customizations"></a>
<a id="data--customizations"></a>

### Customizations

`QuerydslDataFetcher` supports customizing how GraphQL arguments are bound onto properties
to create a Querydsl `Predicate`. By default, arguments are bound as "is equal to" for
each available property. To customize that, you can use `QuerydslDataFetcher` builder
methods to provide a `QuerydslBinderCustomizer`.

A repository may itself be an instance of `QuerydslBinderCustomizer`. This is auto-detected
and transparently applied during [Auto-Registration](#data--data.querydsl.registration). However, when manually
building a `QuerydslDataFetcher` you will need to use builder methods to apply it.

`QuerydslDataFetcher` supports interface and DTO projections to transform query results
before returning these for further GraphQL processing.

> [!TIP]
> To learn what projections are, please refer to the
> [Spring Data docs](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#projections).
> To understand how to use projections in GraphQL, please see [Selection Set vs Projections](#data--data.projections).

To use Spring Data projections with Querydsl repositories, create either a projection interface
or a target DTO class and configure it through the `projectAs` method to obtain a
`DataFetcher` producing the target type:

```java
class Account {

	String name, identifier, description;

	Person owner;
}

interface AccountProjection {

	String getName();

	String getIdentifier();
}

// For single result queries
DataFetcher<AccountProjection> dataFetcher =
		QuerydslDataFetcher.builder(repository).projectAs(AccountProjection.class).single();

// For multi-result queries
DataFetcher<Iterable<AccountProjection>> dataFetcher =
		QuerydslDataFetcher.builder(repository).projectAs(AccountProjection.class).many();
```

<a id="data--data.querydsl.registration"></a>
<a id="data--auto-registration"></a>

### Auto-Registration

If a repository is annotated with `@GraphQlRepository`, it is automatically registered
for queries that do not already have a registered `DataFetcher` and whose return type
matches that of the repository domain type. This includes single value queries, multi-value
queries, and [paginated](#request-execution--execution.pagination) queries.

By default, the name of the GraphQL type returned by the query must match the simple name
of the repository domain type. If needed, you can use the `typeName` attribute of
`@GraphQlRepository` to specify the target GraphQL type name.

For paginated queries, the simple name of the repository domain type must match the
`Connection` type name without the `Connection` ending (e.g. `Book` matches
`BooksConnection`). For auto-registration, pagination is offset-based with 20 items
per page.

Auto-registration detects if a given repository implements `QuerydslBinderCustomizer` and
transparently applies that through `QuerydslDataFetcher` builder methods.

Auto-registration is performed through a built-in `RuntimeWiringConfigurer` that can be
obtained from `QuerydslDataFetcher`. The [Boot Starter](#boot-starter) automatically
detects `@GraphQlRepository` beans and uses them to initialize the
`RuntimeWiringConfigurer` with.

Auto-registration applies [customizations](#data--data.querybyexample.customizations)
by calling `customize(Builder)` on the repository instance if your repository
implements `QuerydslBuilderCustomizer` or `ReactiveQuerydslBuilderCustomizer`
respectively.

<a id="data--data.querybyexample"></a>
<a id="data--query-by-example"></a>

## Query by Example

Spring Data supports the use of
[Query by Example](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#query-by-example)
to fetch data. Query by Example (QBE) is a simple querying technique that does not require
you to write queries through store-specific query languages.

Start by declaring a repository that is `QueryByExampleExecutor`:

```java
public interface AccountRepository extends Repository<Account, Long>,
			QueryByExampleExecutor<Account> {
}
```

Use `QueryByExampleDataFetcher` to turn the repository into a `DataFetcher`:

```java
// For single result queries
DataFetcher<Account> dataFetcher =
		QueryByExampleDataFetcher.builder(repository).single();

// For multi-result queries
DataFetcher<Iterable<Account>> dataFetcher =
		QueryByExampleDataFetcher.builder(repository).many();

// For paginated queries
DataFetcher<Iterable<Account>> dataFetcher =
		QueryByExampleDataFetcher.builder(repository).scrollable();
```

You can now register the above `DataFetcher` through a
[`RuntimeWiringConfigurer`](#request-execution--execution.graphqlsource.runtimewiring-configurer).

The `DataFetcher` uses the GraphQL arguments map to create the domain type of the
repository and use that as the example object to fetch data with. Spring Data supports
`QueryByExampleDataFetcher` for JPA, MongoDB, Neo4j, and Redis.

> [!NOTE]
> For a single argument that is a GraphQL input type, `QueryByExampleDataFetcher`
> nests one level down, and binds with the values from the argument sub-map.

If the repository is `ReactiveQueryByExampleExecutor`, the builder returns
`DataFetcher<Mono<Account>>` or `DataFetcher<Flux<Account>>`. Spring Data supports this
variant for MongoDB, Neo4j, Redis, and R2dbc.

<a id="data--data.querybyexample.build"></a>
<a id="data--build-setup-2"></a>

### Build Setup

Query by Example is already included in the Spring Data modules for the data stores where
it is supported, so no extra setup is required to enable it.

<a id="data--data.querybyexample.customizations"></a>
<a id="data--customizations-2"></a>

### Customizations

`QueryByExampleDataFetcher` supports interface and DTO projections to transform query
results before returning these for further GraphQL processing.

> [!TIP]
> To learn what projections are, please refer to the
> [Spring Data documentation](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#projections).
> To understand the role of projections in GraphQL, please see [Selection Set vs Projections](#data--data.projections).

To use Spring Data projections with Query by Example repositories, create either a projection interface
or a target DTO class and configure it through the `projectAs` method to obtain a
`DataFetcher` producing the target type:

```java
class Account {

	String name, identifier, description;

	Person owner;
}

interface AccountProjection {

	String getName();

	String getIdentifier();
}

// For single result queries
DataFetcher<AccountProjection> dataFetcher =
		QueryByExampleDataFetcher.builder(repository).projectAs(AccountProjection.class).single();

// For multi-result queries
DataFetcher<Iterable<AccountProjection>> dataFetcher =
		QueryByExampleDataFetcher.builder(repository).projectAs(AccountProjection.class).many();
```

<a id="data--data.querybyexample.registration"></a>
<a id="data--auto-registration-2"></a>

### Auto-Registration

If a repository is annotated with `@GraphQlRepository`, it is automatically registered
for queries that do not already have a registered `DataFetcher` and whose return type
matches that of the repository domain type. This includes single value queries, multi-value
queries, and [paginated](#request-execution--execution.pagination) queries.

By default, the name of the GraphQL type returned by the query must match the simple name
of the repository domain type. If needed, you can use the `typeName` attribute of
`@GraphQlRepository` to specify the target GraphQL type name.

For paginated queries, the simple name of the repository domain type must match the
`Connection` type name without the `Connection` ending (e.g. `Book` matches
`BooksConnection`). For auto-registration, pagination is offset-based with 20 items
per page.

Auto-registration is performed through a built-in `RuntimeWiringConfigurer` that can be
obtained from `QueryByExampleDataFetcher`. The [Boot Starter](#boot-starter) automatically
detects `@GraphQlRepository` beans and uses them to initialize the
`RuntimeWiringConfigurer` with.

Auto-registration applies [customizations](#data--data.querybyexample.customizations)
by calling `customize(Builder)` on the repository instance if your repository
implements `QueryByExampleBuilderCustomizer` or
`ReactiveQueryByExampleBuilderCustomizer` respectively.

<a id="data--data.projections"></a>
<a id="data--selection-set-vs-projections"></a>

## Selection Set vs Projections

A common question that arises is, how GraphQL selection sets compare to
[Spring Data projections](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#projections)
and what role does each play?

The short answer is that Spring for GraphQL is not a data gateway that translates GraphQL
queries directly into SQL or JSON queries. Instead, it lets you leverage existing Spring
technology and does not assume a one for one mapping between the GraphQL schema and the
underlying data model. That is why client-driven selection and server-side transformation
of the data model can play complementary roles.

To better understand, consider that Spring Data promotes domain-driven (DDD) design as
the recommended approach to manage complexity in the data layer. In DDD, it is important
to adhere to the constraints of an aggregate. By definition an aggregate is valid only if
loaded in its entirety, since a partially loaded aggregate may impose limitations on
aggregate functionality.

In Spring Data you can choose whether you want your aggregate be exposed as is, or
whether to apply transformations to the data model before returning it as a GraphQL
result. Sometimes it’s enough to do the former, and by default the
[Querydsl](#data--data.querydsl) and the [Query by Example](#data--data.querybyexample) integrations turn the GraphQL
selection set into property path hints that the underlying Spring Data module uses to
limit the selection.

In other cases, it’s useful to reduce or even transform the underlying data model in
order to adapt to the GraphQL schema. Spring Data supports this through Interface
and DTO Projections.

Interface projections define a fixed set of properties to expose where properties may or
may not be `null`, depending on the data store query result. There are two kinds of
interface projections both of which determine what properties to load from the underlying
data source:

- [Closed interface projections](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#projections.interfaces.closed)
  are helpful if you cannot partially materialize the aggregate object, but you still
  want to expose a subset of properties.
- [Open interface projections](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#projections.interfaces.open)
  leverage Spring’s `@Value` annotation and
  [SpEL](https://docs.spring.io/spring-framework/reference/core/expressions.html) expressions to apply lightweight
  data transformations, such as concatenations, computations, or applying static functions
  to a property.

DTO projections offer a higher level of customization as you can place transformation
code either in the constructor or in getter methods.

DTO projections materialize from a query where the individual properties are
determined by the projection itself. DTO projections are commonly used with full-args
constructors (e.g. Java records), and therefore they can only be constructed if all
required fields (or columns) are part of the database query result.

<a id="data--data.pagination.scroll"></a>
<a id="data--scroll"></a>

## Scroll

As explained in [Pagination](#request-execution--execution.pagination), the GraphQL Cursor Connection spec defines a
mechanism for pagination with `Connection`, `Edge`, and `PageInfo` schema types, while
GraphQL Java provides the equivalent Java type representations.

Spring for GraphQL provides built-in `ConnectionAdapter` implementations to adapt the
Spring Data pagination types `Window` and `Slice` transparently. You can configure that
as follows:

```java
CursorStrategy<ScrollPosition> strategy = CursorStrategy.withEncoder(
		new ScrollPositionCursorStrategy(),
		CursorEncoder.base64()); (1)

GraphQLTypeVisitor visitor = ConnectionFieldTypeVisitor.create(List.of(
		new WindowConnectionAdapter(strategy),
		new SliceConnectionAdapter(strategy))); (2)

GraphQlSource.schemaResourceBuilder()
		.schemaResources(..)
		.typeDefinitionConfigurer(..)
		.typeVisitors(List.of(visitor)); (3)
```

| **1** | Create strategy to convert `ScrollPosition` to a Base64 encoded cursor. |
| --- | --- |
| **2** | Create type visitor to adapt `Window` and `Slice` returned from `DataFetcher`s. |
| **3** | Register the type visitor. |

On the request side, a controller method can declare a
[ScrollSubrange](#controllers--controllers.schema-mapping.subrange) method argument to paginate forward
or backward. For this to work, you must declare a [`CursorStrategy`](#request-execution--execution.pagination.cursor.strategy)
supports `ScrollPosition` as a bean.

The [Boot Starter](#boot-starter) declares a `CursorStrategy<ScrollPosition>` bean, and registers the
`ConnectionFieldTypeVisitor` as shown above if Spring Data is on the classpath.

<a id="data--data.pagination.scroll.keyset"></a>
<a id="data--keyset-position"></a>

## Keyset Position

For `KeysetScrollPosition`, the cursor needs to be created from a keyset, which is
essentially a `Map` of key-value pairs. To decide how to create a cursor from a keyset, you can configure `ScrollPositionCursorStrategy` with `CursorStrategy<Map<String, Object>>`.
By default, `JsonKeysetCursorStrategy` writes the keyset `Map` to JSON. That works for
simple like String, Boolean, Integer, and Double, but others cannot be restored back to the
same type without target type information. The Jackson library has a default typing feature
that can include type information in the JSON. To use it safely you must specify a list of
allowed types.

By default, if `JsonKeysetCursorStrategy` is created without a `CodecConfigurer` and the
Jackson library is on the classpath, JSON keyset will support the `Date`, `Calendar`, `UUID`, Java Enums, `Number`, and any type from `java.time`.

Applications can further refine the keyset serialization as JSON by instantiating their own
`JsonKeysetCursorStrategy` with a custom Jackson encoder/decoder pair.
In Spring Boot, contributing an `EncodingCursorStrategy` like the following is enough:

```java
import java.util.Calendar;
import java.util.Date;
import java.util.Map;
import java.util.UUID;

import tools.jackson.databind.DefaultTyping;
import tools.jackson.databind.cfg.DateTimeFeature;
import tools.jackson.databind.json.JsonMapper;
import tools.jackson.databind.jsontype.BasicPolymorphicTypeValidator;
import tools.jackson.databind.jsontype.PolymorphicTypeValidator;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.domain.ScrollPosition;
import org.springframework.graphql.data.pagination.CursorEncoder;
import org.springframework.graphql.data.pagination.CursorStrategy;
import org.springframework.graphql.data.pagination.EncodingCursorStrategy;
import org.springframework.graphql.data.query.JsonKeysetCursorStrategy;
import org.springframework.graphql.data.query.ScrollPositionCursorStrategy;
import org.springframework.http.codec.CodecConfigurer;
import org.springframework.http.codec.ServerCodecConfigurer;
import org.springframework.http.codec.json.JacksonJsonDecoder;
import org.springframework.http.codec.json.JacksonJsonEncoder;

@Configuration
public class KeysetCursorConfiguration {

	@Bean
	// override the EncodingCursorStrategy bean in Spring Boot
	public EncodingCursorStrategy<ScrollPosition> cursorStrategy() {
		JsonKeysetCursorStrategy keysetCursorStrategy = keysetCursorStrategy();
		ScrollPositionCursorStrategy cursorStrategy = new ScrollPositionCursorStrategy(keysetCursorStrategy);
		return CursorStrategy.withEncoder(cursorStrategy, CursorEncoder.base64());
	}

	// create a cursor strategy with a custom CodecConfigurer
	private JsonKeysetCursorStrategy keysetCursorStrategy() {
		JsonMapper mapper = keysetJsonMapper();
		CodecConfigurer codecConfigurer = keysetCodecConfigurer(mapper);
		return new JsonKeysetCursorStrategy(codecConfigurer);
	}

	// use a custom JsonMapper for encoding/decoding JSON
	private CodecConfigurer keysetCodecConfigurer(JsonMapper jsonMapper) {
		CodecConfigurer configurer = ServerCodecConfigurer.create();
		configurer.defaultCodecs().jacksonJsonDecoder(new JacksonJsonDecoder(jsonMapper));
		configurer.defaultCodecs().jacksonJsonEncoder(new JacksonJsonEncoder(jsonMapper));
		return configurer;
	}

	// create a custom JsonMapper
	private JsonMapper keysetJsonMapper() {
		// Configure which types should be allowed for serialization
		// those should include all fields included in the keyset
		PolymorphicTypeValidator validator = BasicPolymorphicTypeValidator.builder()
				.allowIfBaseType(Map.class)
				.allowIfSubType(Calendar.class)
				.allowIfSubType(Date.class)
				.allowIfSubType(UUID.class)
				.allowIfSubType(Number.class)
				.allowIfSubType(Enum.class)
				.allowIfSubType("java.time.")
				.build();

		return JsonMapper.builder()
				.activateDefaultTyping(validator, DefaultTyping.NON_FINAL)
				// as of Jackson 3.0, dates are not written as timestamps by default
				.enable(DateTimeFeature.WRITE_DATES_AS_TIMESTAMPS)
				.build();
	}

}
```

<a id="data--data.pagination.sort"></a>
<a id="data--sort"></a>

## Sort

Spring for GraphQL defines a `SortStrategy` to create `Sort` from GraphQL arguments.
`AbstractSortStrategy` implements the contract with abstract methods to extract the sort
direction and properties. To enable support for `Sort` as a controller method argument, you need to declare a `SortStrategy` bean.

<a id="data--data.transaction-management"></a>
<a id="data--transaction-management"></a>

## Transaction Management

At some point when working with data atomicity and isolation of operations start to
matter. These are both properties of transactions. GraphQL itself does not define any
transaction semantics, so it is up to the server and your application to decide how to
handle transactions.

GraphQL and specifically GraphQL Java are designed to be non-opinionated about how data
is fetched. A core property of GraphQL is that clients drive the request; Fields
can be resolved independently of their original source to allow for composition.
A reduced fieldset can require less data to be fetched resulting in better performance.

Applying the concept of distributed field resolution within transactions is not a good fit:

- Transactions keep a unit of work together resulting typically in fetching the entire
  object graph (like a typical object-relational mapper would behave) within a single
  transaction. This is at odds with GraphQL’s core design to let the client drive queries.
- Keeping a transaction open across multiple data fetchers of which each one would
  fetch only its flat object mitigates the performance aspect and aligns with decoupled
  field resolution, but it can lead to long-running transactions that hold on to resources
  for longer than necessary.

Generally speaking, transactions are best applied to mutations that change state and not
necessarily to queries that just read data. However, there are use cases where
transactional reads are required.

GraphQL is designed to support multiple mutations within a single request. Depending on
the use case, you might want to:

- Run each mutation within its own transaction.
- Keep some mutations within a single transaction to ensure a consistent state.
- Span a single transaction over all involved mutations.

Each approach requires a slightly different transaction management strategy.

When using Spring Framework (e.g. JDBC) or Spring Data, the Template API and repositories
default (without any further instrumentation) to use implicit transactions for individual
operations resulting in starting and commiting a transaction for each repository method
call. This is the normal mode of operation for most databases.

The following sections are outlining two different strategies to manage transactions in a
GraphQL server:

1. [Transaction per Controller Method](#data--data.transaction-management.transactional-service-methods)
2. [Spanning a Transaction programmatically over the entire request](#data--data.transaction-management.transactional-instrumentation)

<a id="data--data.transaction-management.transactional-service-methods"></a>
<a id="data--transactional-controller-methods"></a>

### Transactional Controller Methods

The simplest approach to manage transactions is to use Spring’s Transaction Management
together with `@MutationMapping` controller methods (or any other `@SchemaMapping` method)
for example:

- Declarative
- Programmatic

```java
@Controller public class AccountController {
@MutationMapping @Transactional public Account addAccount(@Argument AccountInput input) {// ...}}
```

```java
@Controller public class AccountController {
private final TransactionOperations transactionOperations;
@MutationMapping public Account addAccount(@Argument AccountInput input) {return transactionOperations.execute(status -> {// ...});}}
```

A transaction spans from entering the `addAccount` method until its return.
All invocations to transactional resources are part of the same transaction resulting in
atomicity and isolation of the mutation.

This is the recommended approach. It gives you full control over transaction boundaries
with a clearly defined entrypoint without the need to instrument GraphQL server
infrastructure.

Cleaning up a transaction after the method call results that subsequent data fetching
(e.g. for nested fields) is not part of the transactional method `addAccount` as
outlined below:

```java
@Controller public class AccountController {
@MutationMapping @Transactional public Account addAccount(@Argument AccountInput input) {    (1) // ...}
@SchemaMapping @Transactional public Person person(Account account) {                      (2) ... // fetching the person within a separate transaction}}
```

**1**

The `addAccount` method invocation runs within its own transaction.

**2**

The `person` method invocation creates its own, separate transaction that is not
tied to the `addAccount` method in case both methods were invoked as part of the same
GraphQL request. A separate transaction comes with all possible drawbacks of not
being part of the same transaction, such as non-repeatable reads or inconsistencies
in case the data has been modified between the `addAcount` and `person` method invocations.

To run multiple mutations in a single transaction maintaining a simple setup we recommend
designing a mutation method that accepts all required inputs. This method can then call
multiple service methods, ensuring they all participate in the same transaction.

<a id="data--data.transaction-management.transactional-instrumentation"></a>
<a id="data--transactional-instrumentation"></a>

### Transactional Instrumentation

Applying a Transactional Instrumentation is a more advanced approach to span a
transaction over the entire execution of a GraphQL request. By stating a transaction
before the first data fetcher is invoked your application can ensure that all data
fetchers can participate in the same transaction.

When instrumenting the server, you need to ensure an `ExecutionStrategy` runs
`DataFetcher` invocations serially so that all invocations are executed on the same
`Thread`. This is mandatory: Synchronous transaction management uses `ThreadLocal` state
to allow participation in transactions. Considering `AsyncSerialExecutionStrategy` as
starting point is a good choice as it executes data fetchers serially.

You have two general options to implement transactional instrumentation:

1. GraphQL Java’s `Instrumentation` contract allows to hook into the execution lifecycle
   at various stages. The Instrumentation SPI was designed with observability in mind, yet it
   serves as execution-agnostic extension points regardless of whether you’re using
   synchronous reactive, or any other asynchronous form to invoke data fetchers and is less
   opinionated in that regard.
2. An `ExecutionStrategy` provides full control over the execution and opens a variety
   of possibilities how to communicate failed transactions or errors during transaction
   cleanup back to the client. It can also serve as good entry point to implement custom
   directives that allow clients specifying transactional attributes through directives or
   using directives in your schema to demarcate transactional boundaries for certain queries
   or mutations.

When manually managing transactions, ensure to clean up the transaction, that is either
commiting or rolling back, after completing the unit of work.
`ExceptionWhileDataFetching` can be a useful `GraphQLError` to obtain an underlying
`Exception`. This error is constructed when using `SimpleDataFetcherExceptionHandler`.
By default, Spring GraphQL falls back to an internal `GraphQLError` that doesn’t expose
the original exception.

Applying transactional instrumentation creates opportunities to rethink transaction
participation: All `@SchemaMapping` controller methods participate in the transaction
regardless whether they are invoked for the root, nested fields, or as part of a mutation.
Transactional controller methods (or service methods within the invocation chain) can
declare transactional attributes such as propagation behavior `REQUIRES_NEW` to start
a new transaction if required.

[Request Execution](#request-execution)
[Annotated Controllers](#controllers)

---

<a id="controllers"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/controllers.html -->

<!-- page_index: 5 -->

# Annotated Controllers

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="controllers--page-title"></a>
<a id="controllers--annotated-controllers"></a>

# Annotated Controllers

Spring for GraphQL provides an annotation-based programming model where `@Controller`
components use annotations to declare handler methods with flexible method signatures to
fetch the data for specific GraphQL fields. For example:

```java
@Controller public class GreetingController {
@QueryMapping (1) public String hello() { (2) return "Hello, world!";}
}
```

**1**

Bind this method to a query, i.e. a field under the Query type.

**2**

Determine the query from the method name if not declared on the annotation.

Spring for GraphQL uses `RuntimeWiring.Builder` to register the above handler method as a
`graphql.schema.DataFetcher` for the query named "hello".

<a id="controllers--controllers-declaration"></a>
<a id="controllers--declaration"></a>

## Declaration

You can define `@Controller` beans as standard Spring bean definitions. The
`@Controller` stereotype allows for auto-detection, aligned with Spring general
support for detecting `@Controller` and `@Component` classes on the classpath and
auto-registering bean definitions for them. It also acts as a stereotype for the annotated
class, indicating its role as a data fetching component in a GraphQL application.

`AnnotatedControllerConfigurer` detects `@Controller` beans and registers their
annotated handler methods as `DataFetcher`s via `RuntimeWiring.Builder`. It is an
implementation of `RuntimeWiringConfigurer` which can be added to `GraphQlSource.Builder`.
The [Boot Starter](#boot-starter) automatically declares `AnnotatedControllerConfigurer` as a bean
and adds all `RuntimeWiringConfigurer` beans to `GraphQlSource.Builder` and that enables
support for annotated `DataFetcher`s, see the
[GraphQL RuntimeWiring](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.runtimewiring) section
in the Boot starter documentation.

<a id="controllers--controllers.schema-mapping"></a>
<a id="controllers--schemamapping"></a>

## `@SchemaMapping`

The `@SchemaMapping` annotation maps a handler method to a field in the GraphQL schema
and declares it to be the `DataFetcher` for that field. The annotation can specify the
parent type name, and the field name:

```java
@Controller public class BookController {
@SchemaMapping(typeName="Book", field="author") public Author getAuthor(Book book) {// ...}}
```

The `@SchemaMapping` annotation can also leave out those attributes, in which case the
field name defaults to the method name, while the type name defaults to the simple class
name of the source/parent object injected into the method. For example, the below
defaults to type "Book" and field "author":

```java
@Controller public class BookController {
@SchemaMapping public Author author(Book book) {// ...}}
```

The `@SchemaMapping` annotation can be declared at the class level to specify a default
type name for all handler methods in the class.

```java
@Controller
@SchemaMapping(typeName="Book")
public class BookController {

	// @SchemaMapping methods for fields of the "Book" type

}
```

`@QueryMapping`, `@MutationMapping`, and `@SubscriptionMapping` are meta annotations that
are themselves annotated with `@SchemaMapping` and have the typeName preset to `Query`, `Mutation`, or `Subscription` respectively. Effectively, these are shortcut annotations
for fields under the Query, Mutation, and Subscription types respectively. For example:

```java
@Controller public class BookController {
@QueryMapping public Book bookById(@Argument Long id) {// ...}
@MutationMapping public Book addBook(@Argument BookInput bookInput) {// ...}
@SubscriptionMapping public Flux<Book> newPublications() {// ...}}
```

`@SchemaMapping` handler methods have flexible signatures and can choose from a range of
method arguments and return values..

<a id="controllers--controllers.schema-mapping.signature"></a>
<a id="controllers--method-arguments"></a>

### Method Arguments

Schema mapping handler methods can have any of the following method arguments:

| Method Argument | Description |
| --- | --- |
| `@Argument` | For access to a named field argument bound to a higher-level, typed Object. See [`@Argument`](#controllers--controllers.schema-mapping.argument). |
| `@Argument Map<String, Object>` | For access to the raw argument value. See [`@Argument`](#controllers--controllers.schema-mapping.argument). |
| `ArgumentValue` | For access to a named field argument bound to a higher-level, typed Object along with a flag to indicate if the input argument was omitted vs set to `null`. See [`ArgumentValue`](#controllers--controllers.schema-mapping.argument-value). |
| `@Arguments` | For access to all field arguments bound to a higher-level, typed Object. See [`@Arguments`](#controllers--controllers.schema-mapping.arguments). |
| `@Arguments Map<String, Object>` | For access to the raw map of arguments. |
| `@ProjectedPayload` Interface | For access to field arguments through a project interface. See [`@ProjectedPayload` Interface](#controllers--controllers.schema-mapping.projectedpayload.argument). |
| "Source" | For access to the source (i.e. parent/container) instance of the field. See [Source](#controllers--controllers.schema-mapping.source). |
| `Subrange` and `ScrollSubrange` | For access to pagination arguments. See [Pagination](#request-execution--execution.pagination), [Scroll](#data--data.pagination.scroll), [`Subrange`](#controllers--controllers.schema-mapping.subrange). |
| `Sort` | For access to sort details. See [Pagination](#request-execution--execution.pagination), [`Sort`](#controllers--controllers.schema-mapping.sort). |
| `DataLoader` | For access to a `DataLoader` in the `DataLoaderRegistry`. See [`DataLoader`](#controllers--controllers.schema-mapping.data-loader). |
| `@ContextValue` | For access to an attribute from the main `GraphQLContext` in `DataFetchingEnvironment`. |
| `@LocalContextValue` | For access to an attribute from the local `GraphQLContext` in `DataFetchingEnvironment`. |
| `GraphQLContext` | For access to the context from the `DataFetchingEnvironment`. |
| `java.security.Principal` | Obtained from the Spring Security context, if available. |
| `@AuthenticationPrincipal` | For access to `Authentication#getPrincipal()` from the Spring Security context. |
| `DataFetchingFieldSelectionSet` | For access to the selection set for the query through the `DataFetchingEnvironment`. |
| `Locale`, `Optional<Locale>` | For access to the `Locale` from the `DataFetchingEnvironment`. |
| `DataFetchingEnvironment` | For direct access to the underlying `DataFetchingEnvironment`. |

<a id="controllers--controllers.schema-mapping.return.values"></a>
<a id="controllers--return-values"></a>

### Return Values

Schema mapping handler methods can return:

| Return Value | Description |
| --- | --- |
| A resolved value `T` | Any application type directly resolved. |
| `Mono<T>` and `Flux<T>` | For asynchronous value(s). Supported for controller methods and for any `DataFetcher` as described in [Reactive `DataFetcher`](#request-execution--execution.reactive-datafetcher). |
| Kotlin `suspend fun` and `Flow` | They are automatically adapted to `Mono` and `Flux`. |
| `java.util.concurrent.Callable<T>` | For producing value(s) asynchronously. For this to work, `AnnotatedControllerConfigurer` must be configured with an `Executor`. On Java 21+, returning `T` directly is enough. Read the paragraph after this table for more details. |
| `graphql.execution.DataFetcherResult<P>` | With `P` being any of the types listed above (`T`, `Mono<T>`, etc.). This is the "full" GraphQL Java return value, containing not only the "data". Useful for completing the result with "extensions" or a ["Local Context"](#controllers--controllers.schema-mapping.localcontext). |

On Java 21+, when `AnnotatedControllerConfigurer` is configured with an `Executor`, controller
methods with a blocking method signature are invoked asynchronously. By default, a controller
method is considered blocking if it does not return an async type such as `Flux`, `Mono`, `CompletableFuture`, and is also not a Kotlin suspending function. You can configure a
blocking controller method `Predicate` on `AnnotatedControllerConfigurer` to help
determine which methods are considered blocking.

> [!TIP]
> The Spring Boot starter for Spring for GraphQL automatically configures
> `AnnotatedControllerConfigurer` with an `Executor` for virtual threads when the property
> `spring.threads.virtual.enabled` is set.

<a id="controllers--controllers.schema-mapping.interfaces"></a>
<a id="controllers--interface-schema-mappings"></a>

### Interface Schema Mappings

When a controller method is mapped to a schema interface field, by default the mapping is
replaced with multiple mappings, one for each schema object type that implements the interface.
This allows use of one controller method for all subtypes.

For example, given:

```graphql
type Query {activities: [Activity!]!}
interface Activity {id: ID! coordinator: User!}
type FooActivity implements Activity {id: ID! coordinator: User!}
type BarActivity implements Activity {id: ID! coordinator: User!}
type User {name: String!}
```

You can write a controller like this:

```java
@Controller public class ActivityController {
@QueryMapping public List<Activity> activities() {// ...}
@SchemaMapping public User coordinator(Activity activity) {// Called for any Activity subtype}
}
```

If necessary, you can take over the mapping for individual subtypes:

```java
@Controller public class ActivityController {
@QueryMapping public List<Activity> activities() {// ...}
@SchemaMapping public User coordinator(Activity activity) {// Called for any Activity subtype except FooActivity}
@SchemaMapping public User coordinator(FooActivity activity) {// ...}
}
```

<a id="controllers--controllers.schema-mapping.argument"></a>
<a id="controllers--argument"></a>

### `@Argument`

In GraphQL Java, `DataFetchingEnvironment` provides access to a map of field-specific
argument values. The values can be simple scalar values (e.g. String, Long), a `Map` of
values for more complex input, or a `List` of values.

Use the `@Argument` annotation to have an argument bound to a target object and
injected into the handler method. If the target object is not a simple Java type, binding
is performed through a primary data constructor, and this is repeated recursively by using
nested argument values to invoke the constructors of nested target objects. For example:

```java
@Controller public class BookController {
@QueryMapping public Book bookById(@Argument Long id) {// ...}
@MutationMapping public Book addBook(@Argument BookInput bookInput) {// ...}}
```

Alternatively, binding can also be done by invoking a default constructor first, and then
applying argument values via setters on the target object.

> [!TIP]
> If the target object doesn’t have setters, you can configure the argument binder to
> fall back on binding via direct field access, see
> [Argument Binding](#controllers--controllers.schema-mapping.argument.binding).

By default, if the method parameter name is available, for example with the `-parameters`
compiler flag in Java 8+ or with debugging info from the compiler, it is used to look up
the argument. If necessary, you can customize the name through the annotation, for example
`@Argument("bookInput")`.

Note that the `@Argument` annotation does not have a "required" flag, nor the option to
specify a default value. Both of these can be specified at the GraphQL schema level and
are enforced by GraphQL Java.

If binding fails, a `BindException` is raised with binding issues accumulated as field
errors where the `field` of each error is the argument path where the issue occurred.

You can use `@Argument` with a `Map<String, Object>` argument, to obtain the raw value of
the argument. For example:

```java
@Controller public class BookController {
@MutationMapping public Book addBook(@Argument Map<String, Object> bookInput) {// ...}}
```

> [!NOTE]
> Prior to 1.2, `@Argument Map<String, Object>` returned the full arguments map when
> the annotation did not specify a name. After 1.2, `@Argument Map<String, Object>` always
> returns the raw argument value, either based on the parameter name or the name in the
> annotation. For access to the full arguments map, please use
> [`@Arguments`](#controllers--controllers.schema-mapping.arguments) instead.

<a id="controllers--controllers.schema-mapping.argument.binding"></a>
<a id="controllers--argument-binding"></a>

#### Argument Binding

Support for `@Argument` binding is provided by `GraphQlArgumentBinder`. This class is
responsible for creating and populating target object from GraphQL argument values.

Argument binding supports several customizations options:

- `nameResolver` — customize the mapping of GraphQL argument names to Object properties,
  which can be useful to deal with naming conventions like the use of "-".
- `fallBackOnDirectFieldAccess` — falls back to direct field access in case the target
  object does not use accessor methods.
- `conversionService` — used for type conversion where needed.

To customize argument binding, use dedicated properties on `AnnotatedControllerConfigurer`
to set `GraphQlArgumentBinder.Options`.

<a id="controllers--controllers.schema-mapping.argument-value"></a>
<a id="controllers--argumentvalue"></a>

### `ArgumentValue`

By default, input arguments in GraphQL are nullable and optional, which means an argument
can be set to the `null` literal, or not provided at all. This distinction is useful for
partial updates with a mutation where the underlying data may also be, either set to
`null` or not changed at all accordingly. When using [`@Argument`](#controllers--controllers.schema-mapping.argument)
there is no way to make such a distinction, because you would get `null` or an empty
`Optional` in both cases.

If you want to know not whether a value was not provided at all, you can declare an
`ArgumentValue` method parameter, which is a simple container for the resulting value, along with a flag to indicate whether the input argument was omitted altogether. You
can use this instead of `@Argument`, in which case the argument name is determined from
the method parameter name, or together with `@Argument` to specify the argument name.

For example:

```java
@Controller public class BookController {
@MutationMapping public void addBook(ArgumentValue<BookInput> bookInput) {if (!bookInput.isOmitted()) {BookInput value = bookInput.value(); // ...}}}
```

`ArgumentValue` is also supported as a field within the object structure of an `@Argument`
method parameter, either initialized via a constructor argument or via a setter, including
as a field of an object nested at any level below the top level object.

This is also supported on the client side with a dedicated Jackson Module, see the [`ArgumentValue` support for clients](#client--client.argumentvalue) section.

<a id="controllers--controllers.schema-mapping.arguments"></a>
<a id="controllers--arguments"></a>

### `@Arguments`

Use the `@Arguments` annotation, if you want to bind the full arguments map onto a single
target Object, in contrast to `@Argument`, which binds a specific, named argument.

For example, `@Argument BookInput bookInput` uses the value of the argument "bookInput"
to initialize `BookInput`, while `@Arguments` uses the full arguments map and in that
case, top-level arguments are bound to `BookInput` properties.

You can use `@Arguments` with a `Map<String, Object>` argument, to obtain the raw map of
all argument values.

<a id="controllers--controllers.schema-mapping.projectedpayload.argument"></a>
<a id="controllers--projectedpayload-interface"></a>

### `@ProjectedPayload` Interface

As an alternative to using complete Objects with [`@Argument`](#controllers--controllers.schema-mapping.argument), you can also use a projection interface to access GraphQL request arguments through a
well-defined, minimal interface. Argument projections are provided by
[Spring Data’s Interface projections](https://docs.spring.io/spring-data/commons/docs/current/reference/html/#projections.interfaces)
when Spring Data is on the class path.

To make use of this, create an interface annotated with `@ProjectedPayload` and declare
it as a controller method parameter. If the parameter is annotated with `@Argument`, it applies to an individual argument within the `DataFetchingEnvironment.getArguments()`
map. When declared without `@Argument`, the projection works on top-level arguments in
the complete arguments map.

For example:

```java
@Controller public class BookController {
@QueryMapping public Book bookById(BookIdProjection bookId) {// ...}
@MutationMapping public Book addBook(@Argument BookInputProjection bookInput) {// ...}}
@ProjectedPayload interface BookIdProjection {
Long getId();}
@ProjectedPayload interface BookInputProjection {
String getName();
@Value("#{target.author + ' ' + target.name}") String getAuthorAndName();}
```

<a id="controllers--controllers.schema-mapping.source"></a>
<a id="controllers--source"></a>

### Source

In GraphQL Java, the `DataFetchingEnvironment` provides access to the source (i.e.
parent/container) instance of the field. To access this, simply declare a method parameter
of the expected target type.

```java
@Controller public class BookController {
@SchemaMapping public Author author(Book book) {// ...}}
```

The source method argument also helps to determine the type name for the mapping.
If the simple name of the Java class matches the GraphQL type, then there is no need to
explicitly specify the type name in the `@SchemaMapping` annotation.

> [!TIP]
> A [`@BatchMapping`](#controllers--controllers.batch-mapping) handler method can batch load all authors for a query, given a list of source/parent books objects.

<a id="controllers--controllers.schema-mapping.subrange"></a>
<a id="controllers--subrange"></a>

### `Subrange`

When there is a [`CursorStrategy`](#request-execution--execution.pagination.cursor.strategy) bean in Spring configuration, controller methods support a `Subrange<P>` argument where `<P>` is a relative position
converted from a cursor. For Spring Data, `ScrollSubrange` exposes `ScrollPosition`.
For example:

```java
@Controller public class BookController {
@QueryMapping public Window<Book> books(ScrollSubrange subrange) {ScrollPosition position = subrange.position().orElse(ScrollPosition.offset()); int count = subrange.count().orElse(20); // ...}
}
```

See [Pagination](#request-execution--execution.pagination) for an overview of pagination and of built-in mechanisms.

<a id="controllers--controllers.schema-mapping.sort"></a>
<a id="controllers--sort"></a>

### `Sort`

When there is a [SortStrategy](#data--data.pagination.scroll) bean in Spring configuration, controller
methods support `Sort` as a method argument. For example:

```java
@Controller public class BookController {
@QueryMapping public Window<Book> books(Optional<Sort> optionalSort) {Sort sort = optionalSort.orElse(Sort.by(..));}
}
```

<a id="controllers--controllers.schema-mapping.data-loader"></a>
<a id="controllers--dataloader"></a>

### `DataLoader`

When you register a batch loading function for an entity, as explained in
[Batch Loading](#request-execution--execution.batching), you can access the `DataLoader` for the entity by declaring a
method argument of type `DataLoader` and use it to load the entity:

```java
@Controller public class BookController {
public BookController(BatchLoaderRegistry registry) {registry.forTypePair(Long.class, Author.class).registerMappedBatchLoader((authorIds, env) -> {// return Map<Long, Author> });}
@SchemaMapping public CompletableFuture<Author> author(Book book, DataLoader<Long, Author> loader) {return loader.load(book.getAuthorId());}
}
```

By default, `BatchLoaderRegistry` uses the full class name of the value type (e.g. the
class name for `Author`) for the key of the registration, and therefore simply declaring
the `DataLoader` method argument with generic types provides enough information
to locate it in the `DataLoaderRegistry`. As a fallback, the `DataLoader` method argument
resolver will also try the method argument name as the key but typically that should not
be necessary.

Note that for many cases with loading related entities, where the `@SchemaMapping` simply
delegates to a `DataLoader`, you can reduce boilerplate by using a
[@BatchMapping](#controllers--controllers.batch-mapping) method as described in the next section.

<a id="controllers--controllers.schema-mapping.validation"></a>
<a id="controllers--validation"></a>

### Validation

When a `javax.validation.Validator` bean is found, `AnnotatedControllerConfigurer` enables support for
[Bean Validation](https://docs.spring.io/spring-framework/reference/core/validation/beanvalidation.html#validation-beanvalidation-overview)
on annotated controller methods. Typically, the bean is of type `LocalValidatorFactoryBean`.

Bean validation lets you declare constraints on types:

```java
public class BookInput {

	@NotNull
	private String title;

	@NotNull
	@Size(max=13)
	private String isbn;
}
```

You can then annotate a controller method parameter with `@Valid` to validate it before
method invocation:

```java
@Controller public class BookController {
@MutationMapping public Book addBook(@Argument @Valid BookInput bookInput) {// ...}}
```

If an error occurs during validation, a `ConstraintViolationException` is raised.
You can use the [Exceptions](#request-execution--execution.exceptions) chain to decide how to present that to clients
by turning it into an error to include in the GraphQL response.

> [!TIP]
> In addition to `@Valid`, you can also use Spring’s `@Validated` that allows
> specifying validation groups.

Bean validation is useful for [`@Argument`](#controllers--controllers.schema-mapping.argument), [`@Arguments`](#controllers--controllers.schema-mapping.arguments), and
[@ProjectedPayload](#controllers--controllers.schema-mapping.projectedpayload.argument)
method parameters, but applies more generally to any method parameter.

> [!WARNING]
> Validation and Kotlin Coroutines
>
> Hibernate Validator is not compatible with Kotlin Coroutine methods and fails when
> introspecting their method parameters. Please see
> [spring-projects/spring-graphql#344 (comment)](https://github.com/spring-projects/spring-graphql/issues/344#issuecomment-1082814093)
> for links to relevant issues and a suggested workaround.

<a id="controllers--controllers.schema-mapping.httpheaders"></a>
<a id="controllers--http-headers"></a>

### HTTP Headers

To access HTTP headers from controller methods, we recommend using a `WebGraphQlInterceptor`
to copy HTTP headers of interest into the `GraphQLContext` from where they are available to
any `DataFetcher`, and to annotated controller methods as `@GraphQlContext` arguments.

There is a built-in `HttpRequestHeaderInterceptor` to help with that.
see [Web Interceptors](#transports--server.interception.web).

<a id="controllers--controllers.schema-mapping.localcontext"></a>
<a id="controllers--local-context"></a>

### Local Context

The main `GraphQlContext` is global for the entire query and can be used to store and retrieve cross-cutting context data for observability, security and more.
There are times when you would like to pass additional information to child fields data fetchers and avoid polluting the main context.
For such use cases, you should consider a local `GraphQLContext` as it is contained to a subset of the data fetching operations.

Controller methods can contribute a local context by returning a `DataFetcherResult<T>` that holds the resolved data and the new context:

```java
@Controller
public class LocalContextBookController {

	@QueryMapping
	public DataFetcherResult<Book> bookById(@Argument Long id) {
		// Our controller method must return a DataFetcherResult
		DataFetcherResult.Builder<Book> resultBuilder = DataFetcherResult.newResult();
		BookAndAuthor bookAndAuthor = this.fetchBookAndAuthorById(id);

		// Create a new local context and store the author value
		GraphQLContext localContext = GraphQLContext.getDefault()
				.put("author", bookAndAuthor.author);
		return resultBuilder
				.data(bookAndAuthor.book)
				.localContext(localContext)
				.build();
	}

	@SchemaMapping
	public List<Book> related(Book book, @LocalContextValue Author author) {
		List<Book> relatedBooks = new ArrayList<>();
		relatedBooks.addAll(fetchBooksByAuthor(author));
		relatedBooks.addAll(fetchSimilarBooks(book));
		return relatedBooks;
	}
```

If you want to see a more detailed example and discussion of using this, have a look at
[the "Building efficient data fetchers by looking ahead" section on the graphql-java documentation](https://www.graphql-java.com/blog/deep-dive-data-fetcher-results).

<a id="controllers--controllers.batch-mapping"></a>
<a id="controllers--batchmapping"></a>

## `@BatchMapping`

[Batch Loading](#request-execution--execution.batching) addresses the N+1 select problem through the use of an
`org.dataloader.DataLoader` to defer the loading of individual entity instances, so they
can be loaded together. For example:

```java
@Controller public class BookController {
public BookController(BatchLoaderRegistry registry) {registry.forTypePair(Long.class, Author.class).registerMappedBatchLoader((authorIds, env) -> {// return Map<Long, Author> });}
@SchemaMapping public CompletableFuture<Author> author(Book book, DataLoader<Long, Author> loader) {return loader.load(book.getAuthorId());}
}
```

For the straight-forward case of loading an associated entity, shown above, the
`@SchemaMapping` method does nothing more than delegate to the `DataLoader`. This is
boilerplate that can be avoided with a `@BatchMapping` method. For example:

```java
@Controller public class BookController {
@BatchMapping public Mono<Map<Book, Author>> author(List<Book> books) {// ...}}
```

The above becomes a batch loading function in the `BatchLoaderRegistry`
where keys are `Book` instances and the loaded values their authors. In addition, a
`DataFetcher` is also transparently bound to the `author` field of the type `Book`, which
simply delegates to the `DataLoader` for authors, given its source/parent `Book` instance.

> [!TIP]
> To be used as a unique key, `Book` must implement `hashcode` and `equals`.

By default, the field name defaults to the method name, while the type name defaults to
the simple class name of the input `List` element type. Both can be customized through
annotation attributes. The type name can also be inherited from a class level
`@SchemaMapping`.

> [!WARNING]
> `@BatchMapping` is effectively a "shortcut" for the straightforward cases, when using `BatchLoaderRegistry`
> adds too much boilerplate for no real benefit.
> If your use case requires more information about the parent `@SchemaMapping` call (such as `@Argument` or context data), for example for filtering the entities to load, using the `BatchLoaderRegistry` is required.
> Please refer to the [Batch Loading Recipes](#request-execution--execution.batching.recipes) section.

<a id="controllers--controllers.batch-mapping.signature"></a>
<a id="controllers--method-arguments-2"></a>

### Method Arguments

Batch mapping methods support the following arguments:

| Method Argument | Description |
| --- | --- |
| `List<K>` | The source/parent objects. |
| `java.security.Principal` | Obtained from Spring Security context, if available. |
| `@ContextValue` | For access to a value from the `GraphQLContext` of `BatchLoaderEnvironment`, which is the same context as the one from the `DataFetchingEnvironment`. |
| `GraphQLContext` | For access to the context from the `BatchLoaderEnvironment`, which is the same context as the one from the `DataFetchingEnvironment`. |
| `BatchLoaderEnvironment` | The environment that is available in GraphQL Java to a `org.dataloader.BatchLoaderWithContext`. The `context` property of `BatchLoaderEnvironment` returns the same `GraphQLContext` instance that is also available to `@SchemaMapping` methods through the `DataFetchingEnvironment`. The `keyContexts` property of `BatchLoaderEnvironment` returns the [localContext](#controllers--controllers.schema-mapping.localcontext) obtained from the `DataFetchingEnvironment` when the `DataLoader` was called for each key. |

<a id="controllers--controllers.batch-mapping.return.values"></a>
<a id="controllers--return-values-2"></a>

### Return Values

Batch mapping methods can return:

| Return Type | Description |
| --- | --- |
| `Mono<Map<K,V>>` | A map with parent objects as keys, and batch loaded objects as values. |
| `Flux<V>` | A sequence of batch loaded objects that must be in the same order as the source/parent objects passed into the method. |
| `Map<K,V>`, `Collection<V>` | Imperative variants, e.g. without remote calls to make. |
| `Callable<Map<K,V>>`, `Callable<Collection<V>>` | Imperative variants to be invoked asynchronously. For this to work, `AnnotatedControllerConfigurer` must be configured with an `Executor`. |
| Kotlin Coroutine with `Map<K,V>`, Kotlin `Flow<K,V>` | Adapted to `Mono<Map<K,V>` and `Flux<V>`. |

On Java 21+, when `AnnotatedControllerConfigurer` is configured with an `Executor`, controller
methods with a blocking method signature are invoked asynchronously. By default, a controller
method is considered blocking if it does not return an async type such as `Flux`, `Mono`, `CompletableFuture`, and is also not a Kotlin suspending function. You can configure a
blocking controller method `Predicate` on `AnnotatedControllerConfigurer` to help
determine which methods are considered blocking.

> [!TIP]
> The Spring Boot starter for Spring for GraphQL automatically configures
> `AnnotatedControllerConfigurer` with an `Executor` for virtual threads when the property
> `spring.threads.virtual.enabled` is set.

<a id="controllers--controllers.batch-mapping.interfaces"></a>
<a id="controllers--interface-batch-mappings"></a>

### Interface Batch Mappings

As is the case with [Interface Schema Mappings](#controllers--controllers.schema-mapping.interfaces), when a batch mapping method is mapped to a schema interface field, the mapping is replaced with
multiple mappings, one for each schema object type that implements the interface.

That means, given the following:

```graphql
type Query {activities: [Activity!]!}
interface Activity {id: ID! coordinator: User!}
type FooActivity implements Activity {id: ID! coordinator: User!}
type BarActivity implements Activity {id: ID! coordinator: User!}
type User {name: String!}
```

You can write a controller like this:

```java
@Controller public class BookController {
@QueryMapping public List<Activity> activities() {// ...}
@BatchMapping Map<Activity, User> coordinator(List<Activity> activities) {// Called for all Activity subtypes}}
```

If necessary, you can take over the mapping for individual subtypes:

```java
@Controller public class BookController {
@QueryMapping public List<Activity> activities() {// ...}
@BatchMapping Map<Activity, User> coordinator(List<Activity> activities) {// Called for all Activity subtypes}
@BatchMapping(field = "coordinator") Map<Activity, User> fooCoordinator(List<FooActivity> activities) {// ...}}
```

<a id="controllers--controllers.exception-handler"></a>
<a id="controllers--graphqlexceptionhandler"></a>

## `@GraphQlExceptionHandler`

Use `@GraphQlExceptionHandler` methods to handle exceptions from data fetching with a
flexible [method signature](#controllers--controllers.exception-handler.signature). When declared in a
controller, exception handler methods apply to exceptions from the same controller:

```java
import graphql.GraphQLError;
import graphql.GraphqlErrorBuilder;

import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.GraphQlExceptionHandler;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.graphql.execution.ErrorType;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindException;

@Controller
public class BookController {

	@QueryMapping
	public Book bookById(@Argument Long id) {
		return ...
	}

	@GraphQlExceptionHandler
	public GraphQLError handle(GraphqlErrorBuilder<?> errorBuilder, BindException ex) {
		return errorBuilder
				.errorType(ErrorType.BAD_REQUEST)
				.message(ex.getMessage())
				.build();
	}

}
```

When declared in an `@ControllerAdvice`, exception handler methods apply across controllers:

```java
import graphql.GraphQLError;
import graphql.GraphqlErrorBuilder;

import org.springframework.graphql.data.method.annotation.GraphQlExceptionHandler;
import org.springframework.graphql.execution.ErrorType;
import org.springframework.validation.BindException;
import org.springframework.web.bind.annotation.ControllerAdvice;

@ControllerAdvice
public class GlobalExceptionHandler {

	@GraphQlExceptionHandler
	public GraphQLError handle(GraphqlErrorBuilder<?> errorBuilder, BindException ex) {
		return errorBuilder
				.errorType(ErrorType.BAD_REQUEST)
				.message(ex.getMessage())
				.build();
	}

}
```

As shown in the examples above, you should build errors by injecting `GraphQlErrorBuilder` in the method signature
because it’s been prepared with the current `DataFetchingEnvironment`.

Exception handling via `@GraphQlExceptionHandler` methods is applied automatically to
controller invocations. To handle exceptions from other `graphql.schema.DataFetcher`
implementations, not based on controller methods, obtain a
`DataFetcherExceptionResolver` from `AnnotatedControllerConfigurer`, and register it in
`GraphQlSource.Builder` as a [DataFetcherExceptionResolver](#request-execution--execution.exceptions).

<a id="controllers--controllers.exception-handler.signature"></a>
<a id="controllers--method-signature"></a>

### Method Signature

Exception handler methods support a flexible method signature with method arguments
resolved from a `DataFetchingEnvironment,` and matching to those of
[@SchemaMapping methods](#controllers--controllers.schema-mapping.arguments).

Supported return types are listed below:

| Return Type | Description |
| --- | --- |
| `graphql.GraphQLError` | Resolve the exception to a single field error. |
| `Collection<GraphQLError>` | Resolve the exception to multiple field errors. |
| `void` | Resolve the exception without response errors. |
| `Object` | Resolve the exception to a single error, to multiple errors, or none. The return value must be `GraphQLError`, `Collection<GraphQLError>`, or `null`. |
| `Mono<T>` | For asynchronous resolution where `<T>` is one of the supported, synchronous, return types. |

<a id="controllers--controllers.namespacing"></a>
<a id="controllers--namespacing"></a>

## Namespacing

At the schema level, query and mutation operations are defined directly under the `Query` and `Mutation` types.
Rich GraphQL APIs can define dozens of operations under those types, making it harder to explore the API and separate concerns.
You can choose to [define Namespaces in your GraphQL schema](https://www.apollographql.com/docs/technotes/TN0012-namespacing-by-separation-of-concern/).
While there are some caveats with this approach, you can implement this pattern with Spring for GraphQL annotated controllers.

With namespacing, your GraphQL schema can, for example, nest query operations under top-level types, instead of listing them directly under `Query`.
Here, we will define `MusicQueries` and `UserQueries` types and make them available under `Query`:

```json
type Query {music: MusicQueries users: UserQueries}
type MusicQueries {album(id: ID!): Album searchForArtist(name: String!): [Artist]}
type Album {id: ID! title: String!}
type Artist {id: ID! name: String!}
type UserQueries {user(login: String): User}
type User {id: ID! login: String!}
```

A GraphQL client would use the `album` query like this:

```graphql
{music {album(id: 42) {id title}}}
```

And get the following response:

```json
{"data": {"music": {"album": {"id": "42","title": "Spring for GraphQL"}}}}
```

This can be implemented in a `@Controller` with the following pattern:

```java
import java.util.List;
import org.springframework.graphql.data.method.annotation.Argument; import org.springframework.graphql.data.method.annotation.QueryMapping; import org.springframework.graphql.data.method.annotation.SchemaMapping; import org.springframework.stereotype.Controller;
@Controller @SchemaMapping(typeName = "MusicQueries") (1) public class MusicController {
@QueryMapping (2) public MusicQueries music() {return new MusicQueries();}
(3) public record MusicQueries() {
}
@SchemaMapping (4) public Album album(@Argument String id) {return new Album(id, "Spring GraphQL");}
@SchemaMapping public List<Artist> searchForArtist(@Argument String name) {return List.of(new Artist("100", "the Spring team"));}
}
```

**1**

Annotate the controller with `@SchemaMapping` and a `typeName` attribute, to avoid repeating it on methods

**2**

Define a `@QueryMapping` for the "music" namespace

**3**

The "music" query returns an "empty" record, but could also return an empty map

**4**

Queries are now declared as fields under the "MusicQueries" type

Instead of declaring wrapping types ("MusicQueries", "UserQueries") explicitly in controllers, you can choose to configure them with the runtime wiring using a `GraphQlSourceBuilderCustomizer` with Spring Boot:

```java
@Configuration public class NamespaceConfiguration {
@Bean public GraphQlSourceBuilderCustomizer customizer() {List<String> queryWrappers = List.of("music", "users"); (1)
return (sourceBuilder) -> sourceBuilder.configureRuntimeWiring((wiringBuilder) -> queryWrappers.forEach((field) -> wiringBuilder.type("Query",(builder) -> builder.dataFetcher(field, (env) -> Collections.emptyMap()))) (2) );}
}
```

**1**

List all the wrapper types for the "Query" type

**2**

Manually declare data fetchers for each of them, returning an empty Map

[Data Integration](#data)
[Security](#security)

---

<a id="security"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/security.html -->

<!-- page_index: 6 -->

# Security

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="security--page-title"></a>
<a id="security--security"></a>

# Security

The path to a [Web](#transports--server.transports.http) GraphQL endpoint can be secured with HTTP
URL security to ensure that only authenticated users can access it. This does not, however, differentiate among different GraphQL requests on such a shared endpoint on
a single URL.

To apply more fine-grained security, add Spring Security annotations such as
`@PreAuthorize` or `@Secured` to service methods involved in fetching specific parts of
the GraphQL response. This should work due to [Context Propagation](#request-execution--execution.context) that aims to make
Security, and other context, available at the data fetching level.

The 1.0.x branch of this repository contains samples for
[Spring MVC](https://github.com/spring-projects/spring-graphql/tree/1.0.x/samples/webmvc-http-security) and for
[WebFlux](https://github.com/spring-projects/spring-graphql/tree/1.0.x/samples/webflux-security).

[Annotated Controllers](#controllers)
[Observability](#observability)

---

<a id="observability"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/observability.html -->

<!-- page_index: 7 -->

# Observability

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="observability--page-title"></a>
<a id="observability--observability"></a>

# Observability

[Observability support with Micrometer](https://docs.micrometer.io/micrometer/reference/observation.html) is directly instrumented in Spring for GraphQL.
This enables both metrics and traces for GraphQL requests and "non-trivial" data fetching operations.
Because the GraphQL engine operates on top of a transport layer, you should also [expect observations from the transport](https://docs.spring.io/spring-framework/reference/integration/observability.html), if supported in Spring Framework.

Observations are only published if an `ObservationRegistry` is configured in the application.
You can learn more about [configuring the observability infrastructure in Spring Boot](https://docs.spring.io/spring-boot/reference/actuator/metrics.html).
If you would like to customize the metadata produced with the GraphQL observations, you can [configure a custom convention on the instrumentation directly](https://docs.spring.io/spring-framework/reference/integration/observability.html#observability.config.conventions).
If your application is using Spring Boot, contributing the custom convention as a bean is the preferred way.

<a id="observability--observability.server.request"></a>
<a id="observability--server-requests-instrumentation"></a>

## Server Requests instrumentation

GraphQL Server Requests observations are created with the name `"graphql.request"` for traditional and Reactive applications and above all supported transports.
This instrumentation assumes that any parent observation must be set as the current one on the GraphQL context with the well-known `"micrometer.observation"` key.
For trace propagation across network boundaries, a separate instrumentation at the transport level must be in charge.
In the case of HTTP, Spring Framework [has dedicated instrumentation that takes care of trace propagation](https://docs.spring.io/spring-framework/reference/integration/observability.html#observability.http-server).

Applications need to configure the `org.springframework.graphql.observation.GraphQlObservationInstrumentation` instrumentation in their application.
It is using the `org.springframework.graphql.observation.DefaultExecutionRequestObservationConvention` by default, backed by the `ExecutionRequestObservationContext`.

By default, the following KeyValues are created:

| Name | Description |
| --- | --- |
| `graphql.operation.type` *(required)* | GraphQL Operation type. |
| `graphql.outcome` *(required)* | Outcome of the GraphQL request. |

The `graphql.operation.type` KeyValue will use the [the standard name for the operation](http://spec.graphql.org/draft/#sec-Language.Operations) (`"query"`, `"mutation"` or `"subscription"`) or `"operation"` if the request document could not be parsed.

The `graphql.outcome` KeyValue will be:

- `"SUCCESS"` if a valid GraphQL response has been sent and it contains no errors
- `"REQUEST_ERROR"` if the request could not be parsed, or if the response contains errors (none of them being of type `org.springframework.graphql.execution.ErrorType.INTERNAL_ERROR`)
- `"INTERNAL_ERROR"` if no valid GraphQL response could be produced, or if the response contains at least one error of type `org.springframework.graphql.execution.ErrorType.INTERNAL_ERROR`

| Name | Description |
| --- | --- |
| `graphql.execution.id` *(required)* | `graphql.execution.ExecutionId` of the GraphQL request. |
| `graphql.operation.name` *(required)* | GraphQL Operation name. |

The `graphql.operation.name` KeyValue will be similar to `graphql.operation.name` will use the operation name provided by the client.

Spring for GraphQL also contributes Events for Server Request Observations.
[Micrometer Observation Events](https://docs.micrometer.io/micrometer/reference/observation/components.html#micrometer-observation-events) are usually handled as span annotations in traces.
This instrumentation records errors listed in the GraphQL response as events.

Name

Contextual Name

the GraphQL error type, e.g. `InvalidSyntax`

the full GraphQL error message, e.g. `"Invalid syntax with offending token 'invalid'…"`

<a id="observability--observability.server.datafetcher"></a>
<a id="observability--datafetcher-instrumentation"></a>

## DataFetcher instrumentation

GraphQL DataFetcher observations are created with the name `"graphql.datafetcher"`, only for data fetching operations that are considered as "non trivial" (property fetching on a Java object is a trivial operation).
Applications need to configure the `org.springframework.graphql.observation.GraphQlObservationInstrumentation` instrumentation in their application.
It is using the `org.springframework.graphql.observation.DefaultDataFetcherObservationConvention` by default, backed by the `DataFetcherObservationContext`.

By default, the following KeyValues are created:

| Name | Description |
| --- | --- |
| `graphql.error.type` *(required)* | Class name of the data fetching error |
| `graphql.field.name` *(required)* | Name of the field being fetched. |
| `graphql.outcome` *(required)* | Outcome of the GraphQL data fetching operation, "SUCCESS" or "ERROR". |

Name

Description

`graphql.field.path` *(required)*

Path to the field being fetched (for example, "/bookById").

<a id="observability--observability.server.dataloader"></a>
<a id="observability--dataloader-instrumentation"></a>

## DataLoader instrumentation

GraphQL DataLoader observations are created with the name `"graphql.dataloader"`, observing calls to `@BatchMapping` controller methods and manually registered `DataLoader` instances.
Applications need to configure the `org.springframework.graphql.observation.GraphQlObservationInstrumentation` instrumentation in their application.
It is using the `org.springframework.graphql.observation.DefaultDataLoaderObservationConvention` by default, backed by the `DataLoaderObservationContext`.

By default, the following KeyValues are created:

| Name | Description |
| --- | --- |
| `graphql.error.type` *(required)* | Class name of the data fetching error |
| `graphql.loader.name` *(required)* | Name of the DataLoader being used. |
| `graphql.outcome` *(required)* | Outcome of the GraphQL data fetching operation, "SUCCESS" or "ERROR". |

Name

Description

`graphql.loader.size` *(required)*

Size of the list of loaded elements.

[Security](#security)
[GraalVM Native support](#graalvm-native)

---

<a id="graalvm-native"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/graalvm-native.html -->

<!-- page_index: 8 -->

# GraalVM Native support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="graalvm-native--page-title"></a>
<a id="graalvm-native--graalvm-native-support"></a>

# GraalVM Native support

Spring Framework 6.0 introduced the support infrastructure for compiling Spring applications to [GraalVM Native images](https://www.graalvm.org/22.3/reference-manual/native-image/).
If you are not familiar with GraalVM in general, how this differs from applications deployed on the JVM and what it means for Spring application, please refer to the dedicated [Spring Boot 3.x GraalVM Native Image support documentation](https://docs.spring.io/spring-boot/reference/packaging/native-image/introducing-graalvm-native-images.html).
Spring Boot also documents the [know limitations with the GraalVM support in Spring](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-with-GraalVM).

<a id="graalvm-native--graalvm.graphql-java"></a>
<a id="graalvm-native--graphql-java-metadata"></a>

## GraphQL Java metadata

Since the [static analysis of your application is done at build time](https://docs.spring.io/spring-boot/reference/packaging/native-image/introducing-graalvm-native-images.html#native-image.introducing-graalvm-native-images.key-differences-with-jvm-deployments), GraalVM might need extra hints if your application is looking up static resources, performing reflection or creating JDK proxies at runtime.

GraphQL Java is performing three tasks at runtime that Native Images are sensible to:

1. Loading resource bundles for message internationalization
2. Some reflection on internal types for schema inspection
3. Reflection on Java types that your application registers with the schema. This happens for example when GraphQL Java is fetching properties from application types

The first two items are handled via reachability metadata that has been contributed by the Spring team to
[the GraalVM reachability metadata repository](https://github.com/oracle/graalvm-reachability-metadata/tree/master/metadata/com.graphql-java/graphql-java).
This metadata is automatically fetched by the native compilation tool when building an application that depends on GraphQL Java.
This doesn’t cover our third item in the list, as those types are provided by the application itself and must be discovered by another mean.

<a id="graalvm-native--graalvm.server"></a>
<a id="graalvm-native--native-server-applications-support"></a>

## Native Server applications support

In typical Spring for GraphQL applications, Java types tied to the GraphQL schema are exposed in `@Controller` method signatures
as parameters or return types. During the [Ahead Of Time processing phase](https://docs.spring.io/spring-framework/reference/core/aot.html) of the build, Spring or GraphQL will use its `o.s.g.data.method.annotation.support.SchemaMappingBeanFactoryInitializationAotProcessor` to discover
the relevant types and register reachability metadata accordingly.
This is all done automatically for you if you are building a Spring Boot application with GraalVM support.

If your application is "manually" registering data fetchers, some types are not discoverable as a result.
You should then register them with Spring Framework’s `@RegisterReflectionForBinding`:

```java
import graphql.schema.DataFetcher;

import org.springframework.aot.hint.annotation.RegisterReflectionForBinding;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.graphql.data.query.QuerydslDataFetcher;
import org.springframework.graphql.execution.RuntimeWiringConfigurer;

@Configuration
@RegisterReflectionForBinding(Book.class) (3)
public class GraphQlConfiguration {

	@Bean
	RuntimeWiringConfigurer customWiringConfigurer(BookRepository bookRepository) { (1)
		DataFetcher<Book> dataFetcher = QuerydslDataFetcher.builder(bookRepository).single();
		return (wiringBuilder) -> wiringBuilder
				.type("Query", (builder) -> builder.dataFetcher("book", dataFetcher)); (2)
	}

}
```

**1**

This application declares a `RuntimeWiringConfigurer` that "manually" adds a `DataFetcher`

**2**

Through this `DataFetcher`, the `BookRepository` will expose a `Book` type

**3**

`@RegisterReflectionForBinding` will register the relevant hints for the `Book` type and all types exposed as fields

<a id="graalvm-native--graalvm.client"></a>
<a id="graalvm-native--client-support"></a>

## Client support

The `GraphQlClient` is not necessarily present as a bean in the application context and it does not expose the Java types used in the schema in method signatures.
The `AotProcessor` strategy described in the section above cannot be used as a result.
For client support, Spring for GraphQL embeds the [relevant reachability metadata for the client infrastructure](https://github.com/spring-projects/spring-graphql/tree/main/spring-graphql/src/main/resources/META-INF/native-image/org.springframework.graphql/spring-graphql).
When it comes to Java types used by the application, applications should use a similar strategy as "manual" data fetchers using `@RegisterReflectionForBinding`:

```java
import reactor.core.publisher.Mono;
import org.springframework.aot.hint.annotation.RegisterReflectionForBinding; import org.springframework.graphql.client.GraphQlClient; import org.springframework.stereotype.Component;
@Component @RegisterReflectionForBinding(Project.class) (2) public class ProjectService {
private final GraphQlClient graphQlClient;
public ProjectService(GraphQlClient graphQlClient) {this.graphQlClient = graphQlClient;}
public Mono<Project> project(String projectSlug) {String document = """ query projectWithReleases($projectSlug: ID!) {project(slug: $projectSlug) {name releases {version}}} """;
return this.graphQlClient.document(document) .variable("projectSlug", projectSlug) .retrieve("project") .toEntity(Project.class); (1)}}
```

**1**

In a Native image, we need to ensure that reflection can be performed on `Project` at runtime

**2**

`@RegisterReflectionForBinding` will register the relevant hints for the `Project` type and all types exposed as fields

[Observability](#observability)
[Federation](#federation)

---

<a id="federation"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/federation.html -->

<!-- page_index: 9 -->

# Federation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="federation--page-title"></a>
<a id="federation--federation"></a>

# Federation

Spring for GraphQL provides an integration for the
[federation-jvm](https://github.com/apollographql/federation-jvm) library, which uses
GraphQL Java to initialize the schema of a sub-graph within a graph of federated services.
See [Apollo Federation](https://www.apollographql.com/docs/federation/) and the
[Subgraph specification](https://www.apollographql.com/docs/federation/subgraph-spec) for details.

<a id="federation--federation.config"></a>
<a id="federation--config"></a>

## Config

To enable the integration, declare a `FederationSchemaFactory` bean in your config, and plug
it into `GraphQlSource.Builder`. For example, with Spring Boot:

```java
@Configuration public class FederationConfig {
@Bean public GraphQlSourceBuilderCustomizer customizer(FederationSchemaFactory factory) {return builder -> builder.schemaFactory(factory::createGraphQLSchema);}
@Bean public FederationSchemaFactory schemaFactory() {return new FederationSchemaFactory();}}
```

Now the schema for the sub-graph service can extend federated types:

```graphql
type Book @key(fields: "id") @extends {id: ID! @external author: Author}
type Author {id: ID firstName: String lastName: String}
```

<a id="federation--federation.entity-mapping"></a>
<a id="federation--entitymapping"></a>

## `@EntityMapping`

An `@EntityMapping` method can load federated type instances in response to an
[\_entities query](https://www.apollographql.com/docs/federation/subgraph-spec/#understanding-query_entities)
from the federation gateway. For example:

```java
@Controller private static class BookController {
@EntityMapping public Book book(@Argument int id) { (1) // ...}
@SchemaMapping public Author author(Book book) { (2) // ...}
}
```

**1**

The `@Argument` method parameter is resolved from the "representation" input map for
the entity. The full "representation" input `Map` can also be resolved. See
[Method Signature](#federation--federation.entity-mapping.signature) for supported
method argument and return value types.

**2**

`@SchemaMapping` methods can be used for the rest of the graph.

You can load federated entities of the same type together by accepting a `List` of id’s, and returning a `List` or `Flux` of entities:

```java
@Controller private static class BookController {
@EntityMapping public List<Book> book(@Argument List<Integer> idList) { (1) // ... return books in the same order}
@BatchMapping public Map<Book, Author> author(List<Book> books) { (2) // ...}}
```

**1**

The `idList` naming convention helps to de-pluralize the parameter name in order to
look up the correct value in the "representation" input map. You can also set the
argument name through the annotation.

**2**

`@BatchMapping` methods can be used for the rest of the graph.

You can load federated entities with a `DataLoader`:

```java
@Controller private static class BookController {
@Autowired public DataLoaderBookController(BatchLoaderRegistry registry) { (1) registry.forTypePair(Integer.class, Book.class).registerBatchLoader((bookIds, environment) -> {// load entities...});}
@EntityMapping public Future<Book> book(@Argument int id, DataLoader<Integer, Book> dataLoader) { (2) return dataLoader.load(id);}
@BatchMapping public Map<Book, Author> author(List<Book> books) { (3) // ...}}
```

| **1** | Register a batch loader for the federated entity type. |
| --- | --- |
| **2** | Declare a `DataLoader` argument to the `@EntityMapping` method. |
| **3** | `@BatchMapping` methods can be used for the rest of the graph. |

<a id="federation--federation.entity-mapping.signature"></a>
<a id="federation--method-signature"></a>

### Method Signature

Entity mapping methods support the following arguments:

| Method Argument | Description |
| --- | --- |
| `@Argument` | For access to a named value from the "representation" input map, also converted to typed Object. |
| `Map<String, Object>` | The full "representation" input map for the entity. |
| `List<Map<String, Object>>` | The list of "representation" input maps when using a single controller method to load all entities of a given type. |
| `@ContextValue` | For access to an attribute from the main `GraphQLContext` in `DataFetchingEnvironment`. |
| `@LocalContextValue` | For access to an attribute from the local `GraphQLContext` in `DataFetchingEnvironment`. |
| `GraphQLContext` | For access to the context from the `DataFetchingEnvironment`. |
| `java.security.Principal` | Obtained from the Spring Security context, if available. |
| `@AuthenticationPrincipal` | For access to `Authentication#getPrincipal()` from the Spring Security context. |
| `DataFetchingFieldSelectionSet` | For access to the selection set for the query through the `DataFetchingEnvironment`. |
| `Locale`, `Optional<Locale>` | For access to the `Locale` from the `DataFetchingEnvironment`. |
| `DataFetchingEnvironment` | For direct access to the underlying `DataFetchingEnvironment`. |
| `DataLoader<I, E>` | To load federated entities with a `DataLoader` where `I` is the id type, and `E` is the entity type. |

`@EntityMapping` methods can return `Mono`, `CompletableFuture`, `Callable`, or the actual entity.

<a id="federation--federation.entity-mapping.exception-handling"></a>
<a id="federation--exception-handling"></a>

### Exception Handling

You can use `@GraphQlExceptionHandler` methods to map exceptions from `@EntityMapping`
methods to `GraphQLError`'s. The errors will be included in the response of the
"\_entities" query. Exception handler methods can be in the same controller or in an
`@ControllerAdvice` class.

[GraalVM Native support](#graalvm-native)
[Client](#client)

---

<a id="client"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/client.html -->

<!-- page_index: 10 -->

# Client

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="client--page-title"></a>
<a id="client--client"></a>

# Client

Spring for GraphQL includes client support to execute GraphQL requests over HTTP, WebSocket, and RSocket.

<a id="client--client.graphqlclient"></a>
<a id="client--graphqlclient"></a>

## `GraphQlClient`

`GraphQlClient` defines a common workflow for GraphQL requests independent of the underlying
transport, so the way you perform requests is the same no matter what transport is in use.

The following transport specific `GraphQlClient` extensions are available:

- [HttpSyncGraphQlClient](#client--client.httpsyncgraphqlclient)
- [HttpGraphQlClient](#client--client.httpgraphqlclient)
- [WebSocketGraphQlClient](#client--client.websocketgraphqlclient)
- [RSocketGraphQlClient](#client--client.rsocketgraphqlclient)

Each defines a `Builder` with options relevant to the transport. All builders extend
from a common, base GraphQlClient [`Builder`](#client--client.graphqlclient.builder)
with options applicable to all transports.

Once `GraphQlClient` is built you can begin to make [requests](#client--client.requests).

Typically, the GraphQL operation for a request is provided as text. Alternatively, you
can use [DGS Codegen](https://github.com/Netflix/dgs-codegen) client API classes through
[DgsGraphQlClient](#client--client.dgsgraphqlclient), which can wrap any of the
above `GraphQlClient` extensions.

<a id="client--client.httpsyncgraphqlclient"></a>
<a id="client--http-sync"></a>

### HTTP Sync

`HttpSyncGraphQlClient` uses
[RestClient](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html#rest-restclient)
to execute GraphQL requests over HTTP through a blocking transport contract and chain of
interceptors.

```java
RestClient restClient = RestClient.create("https://spring.io/graphql");
HttpSyncGraphQlClient graphQlClient = HttpSyncGraphQlClient.create(restClient);
```

Once `HttpSyncGraphQlClient` is created, you can begin to
[execute requests](#client--client.requests) using the same API, independent of the underlying
transport. If you need to change any transport specific details, use `mutate()` on an
existing `HttpSyncGraphQlClient` to create a new instance with customized settings:

```java
RestClient restClient = RestClient.create("https://spring.io/graphql");
HttpSyncGraphQlClient graphQlClient = HttpSyncGraphQlClient.builder(restClient)
		.headers((headers) -> headers.setBasicAuth("joe", "..."))
		.build();

// Perform requests with graphQlClient...

HttpSyncGraphQlClient anotherGraphQlClient = graphQlClient.mutate()
		.headers((headers) -> headers.setBasicAuth("peter", "..."))
		.build();

// Perform requests with anotherGraphQlClient...
```

<a id="client--client.httpgraphqlclient"></a>
<a id="client--http"></a>

### HTTP

`HttpGraphQlClient` uses
[WebClient](https://docs.spring.io/spring-framework/reference/web/webflux-webclient.html) to execute
GraphQL requests over HTTP through a non-blocking transport contract and chain of
interceptors.

```java
WebClient webClient = WebClient.create("https://spring.io/graphql");
HttpGraphQlClient graphQlClient = HttpGraphQlClient.create(webClient);
```

Once `HttpGraphQlClient` is created, you can begin to
[execute requests](#client--client.requests) using the same API, independent of the underlying
transport. If you need to change any transport specific details, use `mutate()` on an
existing `HttpGraphQlClient` to create a new instance with customized settings:

```java
WebClient webClient = WebClient.create("https://spring.io/graphql");

HttpGraphQlClient graphQlClient = HttpGraphQlClient.builder(webClient)
		.headers((headers) -> headers.setBasicAuth("joe", "..."))
		.build();

// Perform requests with graphQlClient...

HttpGraphQlClient anotherGraphQlClient = graphQlClient.mutate()
		.headers((headers) -> headers.setBasicAuth("peter", "..."))
		.build();

// Perform requests with anotherGraphQlClient...
```

<a id="client--client.websocketgraphqlclient"></a>
<a id="client--websocket"></a>

### WebSocket

`WebSocketGraphQlClient` executes GraphQL requests over a shared WebSocket connection.
It is built using the
[WebSocketClient](https://docs.spring.io/spring-framework/reference/web/webflux-websocket.html#webflux-websocket-client)
from Spring WebFlux and you can create it as follows:

```java
String url = "wss://spring.io/graphql";
WebSocketClient client = new ReactorNettyWebSocketClient();

WebSocketGraphQlClient graphQlClient = WebSocketGraphQlClient.builder(url, client).build();
```

In contrast to `HttpGraphQlClient`, the `WebSocketGraphQlClient` is connection oriented, which means it needs to establish a connection before making any requests. As you begin
to make requests, the connection is established transparently. Alternatively, use the
client’s `start()` method to establish the connection explicitly before any requests.

In addition to being connection-oriented, `WebSocketGraphQlClient` is also multiplexed.
It maintains a single, shared connection for all requests. If the connection is lost, it is re-established on the next request or if `start()` is called again. You can also
use the client’s `stop()` method which cancels in-progress requests, closes the
connection, and rejects new requests.

> [!TIP]
> Use a single `WebSocketGraphQlClient` instance for each server in order to have a
> single, shared connection for all requests to that server. Each client instance
> establishes its own connection and that is typically not the intent for a single server.

Once `WebSocketGraphQlClient` is created, you can begin to
[execute requests](#client--client.requests) using the same API, independent of the underlying
transport. If you need to change any transport specific details, use `mutate()` on an
existing `WebSocketGraphQlClient` to create a new instance with customized settings:

```java
String url = "wss://spring.io/graphql";
WebSocketClient client = new ReactorNettyWebSocketClient();

WebSocketGraphQlClient graphQlClient = WebSocketGraphQlClient.builder(url, client)
		.headers((headers) -> headers.setBasicAuth("joe", "..."))
		.build();

// Use graphQlClient...

WebSocketGraphQlClient anotherGraphQlClient = graphQlClient.mutate()
		.headers((headers) -> headers.setBasicAuth("peter", "..."))
		.build();

// Use anotherGraphQlClient...
```

`WebSocketGraphQlClient` supports sending periodic ping messages to keep the connection
active when no other messages are sent or received. You can enable that as follows:

```java
String url = "wss://spring.io/graphql";
WebSocketClient client = new ReactorNettyWebSocketClient();

WebSocketGraphQlClient graphQlClient = WebSocketGraphQlClient.builder(url, client)
		.keepAlive(Duration.ofSeconds(30))
		.build();
```

<a id="client--client.websocketgraphqlclient.interceptor"></a>
<a id="client--interceptor"></a>

#### Interceptor

The [GraphQL over WebSocket](https://github.com/enisdenjo/graphql-ws/blob/master/PROTOCOL.md)
protocol defines a number of connection oriented messages in addition to executing
requests. For example, a client sends `"connection_init"` and the server responds with
`"connection_ack"` at the start of a connection.

For WebSocket transport specific interception, you can create a
`WebSocketGraphQlClientInterceptor`:

```java
static class MyInterceptor implements WebSocketGraphQlClientInterceptor {
@Override public Mono<Object> connectionInitPayload() {// ... the "connection_init" payload to send}
@Override public Mono<Void> handleConnectionAck(Map<String, Object> ackPayload) {// ... the "connection_ack" payload received}
}
```

[Register](#client--client.interception) the above interceptor as any other
`GraphQlClientInterceptor` and use it also to intercept GraphQL requests, but note there
can be at most one interceptor of type `WebSocketGraphQlClientInterceptor`.

<a id="client--client.rsocketgraphqlclient"></a>
<a id="client--rsocket"></a>

### RSocket

`RSocketGraphQlClient` uses
[RSocketRequester](https://docs.spring.io/spring-framework/reference/rsocket.html#rsocket-requester)
to execute GraphQL requests over RSocket requests.

```java
URI uri = URI.create("wss://localhost:8080/rsocket");
WebsocketClientTransport transport = WebsocketClientTransport.create(uri);

RSocketGraphQlClient client = RSocketGraphQlClient.builder()
		.clientTransport(transport)
		.build();
```

In contrast to `HttpGraphQlClient`, the `RSocketGraphQlClient` is connection oriented, which means it needs to establish a session before making any requests. As you begin
to make requests, the session is established transparently. Alternatively, use the
client’s `start()` method to establish the session explicitly before any requests.

`RSocketGraphQlClient` is also multiplexed. It maintains a single, shared session for
all requests. If the session is lost, it is re-established on the next request or if
`start()` is called again. You can also use the client’s `stop()` method which cancels
in-progress requests, closes the session, and rejects new requests.

> [!TIP]
> Use a single `RSocketGraphQlClient` instance for each server in order to have a
> single, shared session for all requests to that server. Each client instance
> establishes its own connection and that is typically not the intent for a single server.

Once `RSocketGraphQlClient` is created, you can begin to
[execute requests](#client--client.requests) using the same API, independent of the underlying
transport.

<a id="client--client.graphqlclient.builder"></a>
<a id="client--builder"></a>

### Builder

`GraphQlClient` defines a parent `BaseBuilder` with common configuration options for the
builders of all extensions. Currently, it has lets you configure:

- `DocumentSource` strategy to load the document for a request from a file
- [Interception](#client--client.interception) of executed requests

`BaseBuilder` is further extended by the following:

- `SyncBuilder` - blocking execution stack with a chain of `SyncGraphQlInterceptor`'s.
- `Builder` - non-blocking execution stack with chain of `GraphQlInterceptor`'s.

<a id="client--client.requests"></a>
<a id="client--requests"></a>

## Requests

Once you have a [`GraphQlClient`](#client--client.graphqlclient), you can begin to perform requests via
[retrieve](#client--client.requests.retrieve) or [execute](#client--client.requests.execute)
methods.

<a id="client--client.requests.retrieve"></a>
<a id="client--retrieve"></a>

### Retrieve

The below retrieves and decodes the data for a query:

- Sync
- Non-Blocking

```java
String document =""" {project(slug:"spring-framework") {name releases {version}}} """;
Project project = graphQlClient.document(document) (1) .retrieveSync("project") (2) .toEntity(Project.class); (3)
```

```java
String document =""" {project(slug:"spring-framework") {name releases {version}}} """;
Mono<Project> project = graphQlClient.document(document) (1) .retrieve("project") (2) .toEntity(Project.class); (3)
```

| **1** | The operation to perform. |
| --- | --- |
| **2** | The path under the "data" key in the response map to decode from. |
| **3** | Decode the data at the path to the target type. |

The input document is a `String` that could be a literal or produced through a code
generated request object. You can also define documents in files and use a
[Document Source](#client--client.requests.document-source) to resole them by file name.

The path is relative to the "data" key and uses a simple dot (".") separated notation
for nested fields with optional array indices for list elements, e.g. `"project.name"`
or `"project.releases[0].version"`.

Decoding can result in `FieldAccessException` if the given path is not present, or the
field value is `null` and has an error. `FieldAccessException` provides access to the
response and the field:

- Sync
- Non-Blocking

```java
try {
	Project project = graphQlClient.document(document)
			.retrieveSync("project")
			.toEntity(Project.class);
	return project;
}
catch (FieldAccessException ex) {
	ClientGraphQlResponse response = ex.getResponse();
	// ...
	ClientResponseField field = ex.getField();
	// return fallback value
	return new Project();
}
```

```java
Mono<Project> projectMono = graphQlClient.document(document)
		.retrieve("project")
		.toEntity(Project.class)
		.onErrorResume(FieldAccessException.class, (ex) -> {
			ClientGraphQlResponse response = ex.getResponse();
			// ...
			ClientResponseField field = ex.getField();
			// return fallback value
			return Mono.just(new Project());
		});
```

If the field is present but cannot be decoded to the requested type, a plain `GraphQlClientException`
is thrown instead.

<a id="client--client.requests.execute"></a>
<a id="client--execute"></a>

### Execute

[Retrieve](#client--client.requests.retrieve) is only a shortcut to decode from a single path in the
response map. For more control, use the `execute` method and handle the response:

For example:

- Sync
- Non-Blocking

```java
ClientGraphQlResponse response = graphQlClient.document(document).executeSync();
if (!response.isValid()) {// Request failure... (1)}
ClientResponseField field = response.field("project"); if (field.getValue() == null) {if (field.getErrors().isEmpty()) {// Optional field set to null... (2)} else {// Field failure... (3)}}
Project project = field.toEntity(Project.class); (4)
```

```java
Mono<Project> projectMono = graphQlClient.document(document) .execute() .map((response) -> {if (!response.isValid()) {// Request failure... (1)}
ClientResponseField field = response.field("project"); if (field.getValue() == null) {if (field.getErrors().isEmpty()) {// Optional field set to null... (2)} else {// Field failure... (3)}}
return field.toEntity(Project.class); (4) });
```

| **1** | The response does not have data, only errors |
| --- | --- |
| **2** | Field that was set to `null` by its `DataFetcher` |
| **3** | Field that is `null` and has an associated error |
| **4** | Decode the data at the given path |

<a id="client--client.requests.document-source"></a>
<a id="client--document-source"></a>

### Document Source

The document for a request is a `String` that may be defined in a local variable or
constant, or it may be produced through a code generated request object.

You can also create document files with extensions `.graphql` or `.gql` under
`"graphql-documents/"` on the classpath and refer to them by file name.

For example, given a file called `projectReleases.graphql` in
`src/main/resources/graphql-documents`, with content:

src/main/resources/graphql-documents/projectReleases.graphql

```graphql
query projectReleases($slug: ID!) {project(slug: $slug) {name releases {version}}}
```

You can then:

```java
Project project = graphQlClient.documentName("projectReleases") (1)
		.variable("slug", "spring-framework") (2)
		.retrieveSync("projectReleases.project")
		.toEntity(Project.class);
```

**1**

Load the document from "projectReleases.graphql"

**2**

Provide variable values.

The "JS GraphQL" plugin for IntelliJ supports GraphQL query files with code completion.

You can use the `GraphQlClient` [Builder](#client--client.graphqlclient.builder) to customize the
`DocumentSource` for loading documents by names.

<a id="client--client.subscriptions"></a>
<a id="client--subscription-requests"></a>

## Subscription Requests

Subscription requests require a client transport that is capable of streaming data.
You will need to create a `GraphQlClient` that support this:

- [HttpGraphQlClient](#client--client.httpgraphqlclient) with Server-Sent Events
- [WebSocketGraphQlClient](#client--client.websocketgraphqlclient) with WebSocket
- [RSocketGraphQlClient](#client--client.rsocketgraphqlclient) with RSocket

<a id="client--client.subscriptions.retrieve"></a>
<a id="client--retrieve-2"></a>

### Retrieve

To start a subscription stream, use `retrieveSubscription` which is similar to
[retrieve](#client--client.requests.retrieve) for a single response but returning a stream of
responses, each decoded to some data:

```java
Flux<String> greetingFlux = client.document("subscription { greetings }")
		.retrieveSubscription("greeting")
		.toEntity(String.class);
```

The `Flux` may terminate with `SubscriptionErrorException` if the subscription ends from
the server side with an "error" message. The exception provides access to GraphQL errors
decoded from the "error" message.

The `Flux` may terminate with `GraphQlTransportException` such as
`WebSocketDisconnectedException` if the underlying connection is closed or lost. In that
case you can use the `retry` operator to restart the subscription.

To end the subscription from the client side, the `Flux` must be cancelled, and in turn
the WebSocket transport sends a "complete" message to the server. How to cancel the
`Flux` depends on how it is used. Some operators such as `take` or `timeout` themselves
cancel the `Flux`. If you subscribe to the `Flux` with a `Subscriber`, you can get a
reference to the `Subscription` and cancel through it. The `onSubscribe` operator also
provides access to the `Subscription`.

<a id="client--client.subscriptions.execute"></a>
<a id="client--execute-2"></a>

### Execute

[Retrieve](#client--client.subscriptions.retrieve) is only a shortcut to decode from a single path in each
response map. For more control, use the `executeSubscription` method and handle each
response directly:

```java
Flux<String> greetingFlux = client.document("subscription { greetings }") .executeSubscription() .map((response) -> {if (!response.isValid()) {// Request failure...}
ClientResponseField field = response.field("project"); if (field.getValue() == null) {if (field.getErrors().isEmpty()) {// Optional field set to null...} else {// Field failure...}}
return field.toEntity(String.class); });
```

<a id="client--client.interception"></a>
<a id="client--interception"></a>

## Interception

For blocking transports created with the `GraphQlClient.SyncBuilder`, you create a
`SyncGraphQlClientInterceptor` to intercept all requests through the client:

```java
import org.springframework.graphql.client.ClientGraphQlRequest;
import org.springframework.graphql.client.ClientGraphQlResponse;
import org.springframework.graphql.client.SyncGraphQlClientInterceptor;

public class SyncInterceptor implements SyncGraphQlClientInterceptor {

	@Override
	public ClientGraphQlResponse intercept(ClientGraphQlRequest request, Chain chain) {
		// ...
		return chain.next(request);
	}
}
```

For non-blocking transports created with `GraphQlClient.Builder`, you create a
`GraphQlClientInterceptor` to intercept all requests through the client:

```java
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import org.springframework.graphql.client.ClientGraphQlRequest;
import org.springframework.graphql.client.ClientGraphQlResponse;
import org.springframework.graphql.client.GraphQlClientInterceptor;

public class MyInterceptor implements GraphQlClientInterceptor {

	@Override
	public Mono<ClientGraphQlResponse> intercept(ClientGraphQlRequest request, Chain chain) {
		// ...
		return chain.next(request);
	}

	@Override
	public Flux<ClientGraphQlResponse> interceptSubscription(ClientGraphQlRequest request, SubscriptionChain chain) {
		// ...
		return chain.next(request);
	}

}
```

Once the interceptor is created, register it through the client builder. For example:

```java
URI url = URI.create("wss://localhost:8080/graphql");
WebSocketClient client = new ReactorNettyWebSocketClient();

WebSocketGraphQlClient graphQlClient = WebSocketGraphQlClient.builder(url, client)
		.interceptor(new MyInterceptor())
		.build();
```

<a id="client--client.argumentvalue"></a>
<a id="client--optional-input"></a>

## Optional input

By default, input types in GraphQL are nullable and optional.
An input value (or any of its fields) can be set to the `null` literal, or not provided at all.
This distinction is useful for partial updates with a mutation where the underlying data may also be, either set to `null` or not changed at all accordingly.

Similar to the [`ArgumentValue<T> support in controllers`](#controllers--controllers.schema-mapping.argument-value), we can wrap an Input type with `ArgumentValue<T>` or use it at the level of class attributes on the client side.
Given a `ProjectInput` class like:

```java
import org.springframework.graphql.data.ArgumentValue;

public record ProjectInput(String id, ArgumentValue<String> name) {

}
```

We can use our client to send a mutation request:

```java
public void updateProject() {ProjectInput projectInput = new ProjectInput("spring-graphql",ArgumentValue.ofNullable("Spring for GraphQL")); (1) ClientGraphQlResponse response = this.graphQlClient.document(""" mutation updateProject($project: ProjectInput!) {updateProject($project: $project) {id name}} """) .variables(Map.of("project", projectInput)) .executeSync();}
```

**1**

we can use `ArgumentValue.omitted()` instead, to ignore this field

For this to work, the client must use Jackson for JSON (de)serialization and must be configured
with the `org.springframework.graphql.client.json.GraphQlJacksonModule`.
This can be registered manually on the underlying HTTP client like so:

```java
public ArgumentValueClient(HttpGraphQlClient graphQlClient) {
	JsonMapper jsonMapper = JsonMapper.builder().addModule(new GraphQlJacksonModule()).build();
	JacksonJsonEncoder jsonEncoder = new JacksonJsonEncoder(jsonMapper);
	WebClient webClient = WebClient.builder()
			.baseUrl("https://example.com/graphql")
			.codecs((codecs) -> codecs.defaultCodecs().jacksonJsonEncoder(jsonEncoder))
			.build();
	this.graphQlClient = HttpGraphQlClient.create(webClient);
}
```

This `GraphQlJacksonModule` can be globally registered in Spring Boot applications by contributing it as a bean:

```java
@Configuration public class GraphQlJsonConfiguration {
@Bean public GraphQlJacksonModule graphQLModule() {return new GraphQlJacksonModule();}
}
```

> [!NOTE]
> Jackson 2.x support is also available with the `GraphQlJackson2Module`.

<a id="client--client.dgsgraphqlclient"></a>
<a id="client--dgs-codegen"></a>

## DGS Codegen

As an alternative to providing the operation such as a mutation, query, or subscription as
text, you can use the [DGS Codegen](https://github.com/Netflix/dgs-codegen) library to
generate client API classes that let you use a fluent API to define the request.

Spring for GraphQL provides [DgsGraphQlClient](#client--client.dgsgraphqlclient)
that wraps any `GraphQlClient` and helps to prepare the request with generated client
API classes.

For example, given the following schema:

```graphql
type Query {books: [Book]}
type Book {id: ID name: String}
```

You can perform a request as follows:

```java
HttpGraphQlClient client = HttpGraphQlClient.create(WebClient.create("https://example.org/graphql"));
DgsGraphQlClient dgsClient = DgsGraphQlClient.create(client); (1)

List<Book> books = dgsClient.request(BookByIdGraphQLQuery.newRequest().id("42").build()) (2)
		.projection(new BooksProjectionRoot<>().id().name()) (3)
		.retrieveSync("books")
		.toEntityList(Book.class);
```

| **1** | Create `DgsGraphQlClient` by wrapping any `GraphQlClient`. |
| --- | --- |
| **2** | Specify the operation for the request. |
| **3** | Define the selection set. |

The `DgsGraphQlClient` also supports multiple queries by chaining `query()` calls:

```java
HttpGraphQlClient client = HttpGraphQlClient.create(WebClient.create("https://example.org/graphql"));
DgsGraphQlClient dgsClient = DgsGraphQlClient.create(client); (1)

ClientGraphQlResponse response = dgsClient
		.request(BookByIdGraphQLQuery.newRequest().id("42").build()) (2)
		.queryAlias("firstBook")  (3)
		.projection(new BooksProjectionRoot<>().id().name())
		.request(BookByIdGraphQLQuery.newRequest().id("53").build()) (4)
		.queryAlias("secondBook")
		.projection(new BooksProjectionRoot<>().id().name())
		.executeSync(); (5)

Book firstBook = response.field("firstBook").toEntity(Book.class); (6)
Book secondBook = response.field("secondBook").toEntity(Book.class);
```

| **1** | Create `DgsGraphQlClient` by wrapping any `GraphQlClient`. |
| --- | --- |
| **2** | Specify the operation for the first request. |
| **3** | When multiple requests are sent, we need to specify an alias for each |
| **4** | Specify the operation for the second request. |
| **5** | Get the complete response |
| **6** | Get the relevant document parts with the configured aliases |

[Federation](#federation)
[Code Generation](#codegen)

---

<a id="codegen"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/codegen.html -->

<!-- page_index: 11 -->

# Code Generation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="codegen--page-title"></a>
<a id="codegen--code-generation"></a>

# Code Generation

You can use tools such as
[DGS Codegen](https://netflix.github.io/dgs/generating-code-from-schema/) to generate
Java types from the GraphQL schema. The following can be generated:

1. Client types for requests (e.g. query, mutation) input types, and response selection types.
2. Data types corresponding to GraphQL schema types.

Code generation may not be ideal for your own application’s data types especially if you
want to add logic to them. Code generation, however, is a good fit for client types since
those define the request, and don’t need to have other logic. As a client, you may also
choose to generate the data types for the response.

Start by following the instructions for the DGS code generation plugin to generate client API types.
Then you can [use client generated types with Spring’s DgsGraphQlClient](#client--client.dgsgraphqlclient).

> [!TIP]
> Spring Initializer at [start.spring.io](https://start.spring.io) can create a Spring project with
> the DGS Codegen Gradle or Maven plugin.

[Client](#client)
[GraphiQL](#graphiql)

---

<a id="graphiql"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/graphiql.html -->

<!-- page_index: 12 -->

# GraphiQL

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="graphiql--page-title"></a>
<a id="graphiql--graphiql"></a>

# GraphiQL

[GraphiQL](https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme) is a graphical interactive in-browser GraphQL IDE.
It is very popular amongst developers as it makes it easy to explore and interactively develop GraphQL APIs.
During development, a stock GraphiQL integration is often enough to help developers work on an API.
In production, applications can require a custom GraphiQL build, that ships with a company logo or specific authentication support.

Spring for GraphQL ships with [a stock GraphiQL `index.html` page](https://github.com/spring-projects/spring-graphql/blob/main/spring-graphql/src/main/resources/graphiql/index.html) that uses static resources hosted on the esm.sh CDN.
Spring Boot applications can easily [enable this page with a configuration property](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html#web.graphql.graphiql).

Your application may need a custom GraphiQL build if it requires a setup that doesn’t rely on a CDN, or if you wish to customize the user interface.
This can be done in two steps:

1. Configure and compile a GraphiQL build
2. Expose the built GraphiQL instance through the Spring web infrastructure

<a id="graphiql--graphiql.custombuild"></a>
<a id="graphiql--creating-a-custom-graphiql-build"></a>

## Creating a custom GraphiQL build

This part is generally outside of the scope of this documentation, as there are several options for custom builds.
You will find more information in the [official GraphiQL documentation](https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme).
You can choose to copy the build result directly in your application resources.
Alternatively, you can integrate the JavaScript build in your project as a separate module by leveraging Node.js [Gradle](https://github.com/node-gradle/gradle-node-plugin) or [Maven](https://github.com/eirslett/frontend-maven-plugin) build plugins.

<a id="graphiql--graphiql.configuration"></a>
<a id="graphiql--exposing-a-graphiql-instance"></a>

## Exposing a GraphiQL instance

Once a GraphiQL build is available on the classpath, you can expose it as an endpoint with the [functional web frameworks](https://docs.spring.io/spring-framework/reference/web/webmvc-functional.html#webmvc-fn-router-functions).

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.core.io.ClassPathResource;
import org.springframework.graphql.server.webmvc.GraphiQlHandler;
import org.springframework.web.servlet.function.RouterFunction;
import org.springframework.web.servlet.function.RouterFunctions;
import org.springframework.web.servlet.function.ServerResponse;

@Configuration
public class GraphiQlConfiguration {

	@Bean
	@Order(0)
	public RouterFunction<ServerResponse> graphiQlRouterFunction() {
		RouterFunctions.Builder builder = RouterFunctions.route();
		ClassPathResource graphiQlPage = new ClassPathResource("graphiql/index.html"); (1)
		GraphiQlHandler graphiQLHandler = new GraphiQlHandler("/graphql", "", graphiQlPage); (2)
		builder = builder.GET("/graphiql", graphiQLHandler::handleRequest); (3)
		return builder.build(); (4)
	}
}
```

**1**

Load the GraphiQL page from the classpath (here, we are using the version shipped with Spring for GraphQL)

**2**

Configure a web handler for processing HTTP requests; you can implement a custom `HandlerFunction` depending on your use case

**3**

Finally, map the handler to a specific HTTP endpoint

**4**

Expose this new route through a `RouterFunction` bean

You might also need to configure your application to [serve the relevant static resources](https://docs.spring.io/spring-boot/reference/web/servlet.html#web.servlet.spring-mvc.static-content).

[Code Generation](#codegen)
[Testing](#testing)

---

<a id="testing"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/testing.html -->

<!-- page_index: 13 -->

# Testing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="testing--page-title"></a>
<a id="testing--testing"></a>

# Testing

Spring for GraphQL provides dedicated support for testing GraphQL requests over HTTP, WebSocket, and RSocket, as well as for testing directly against a server.

To make use of this, add `spring-graphql-test` to your build:

- Gradle
- Maven

```groovy
dependencies {
	// ...
	testImplementation 'org.springframework.graphql:spring-graphql-test:2.0.4'
}
```

```xml
<dependencies>
	<!-- ... -->
	<dependency>
		<groupId>org.springframework.graphql</groupId>
		<artifactId>spring-graphql-test</artifactId>
		<version>2.0.4</version>
		<scope>test</scope>
	</dependency>
</dependencies>
```

<a id="testing--testing.graphqltester"></a>
<a id="testing--graphqltester"></a>

## `GraphQlTester`

`GraphQlTester` is a contract that declares a common workflow for testing GraphQL
requests that is independent of the underlying transport. That means requests are tested
with the same API no matter what the underlying transport, and anything transport
specific is configured at build time.

To create a `GraphQlTester` that performs requests through a client, you need one of the
following extensions:

- [HttpGraphQlTester](#testing--testing.httpgraphqltester)
- [WebSocketGraphQlTester](#testing--testing.websocketgraphqltester)
- [RSocketGraphQlTester](#testing--testing.rsocketgraphqltester)

To create a `GraphQlTester` that performs tests on the server side, without a client:

- [ExecutionGraphQlServiceTester](#testing--testing.graphqlservicetester)
- [WebGraphQlTester](#testing--testing.webgraphqltester)

Each defines a `Builder` with options relevant to the transport. All builders extend
from a common, base GraphQlTester [`Builder`](#testing--testing.graphqltester.builder) with
options relevant to all extensions.

<a id="testing--testing.httpgraphqltester"></a>
<a id="testing--http"></a>

### HTTP

`HttpGraphQlTester` uses
[WebTestClient](https://docs.spring.io/spring-framework/reference/testing/webtestclient.html) to execute
GraphQL requests over HTTP, with or without a live server, depending on how
`WebTestClient` is configured.

To test in Spring WebFlux, without a live server, point to your Spring configuration
that declares the GraphQL HTTP endpoint:

```java
AnnotationConfigWebApplicationContext context = ...

WebTestClient client =
		WebTestClient.bindToApplicationContext(context)
				.configureClient()
				.baseUrl("/graphql")
				.build();

HttpGraphQlTester tester = HttpGraphQlTester.create(client);
```

To test in Spring MVC, without a live server, do the same using `MockMvcWebTestClient`:

```java
AnnotationConfigWebApplicationContext context = ...

WebTestClient client =
		MockMvcWebTestClient.bindToApplicationContext(context)
				.configureClient()
				.baseUrl("/graphql")
				.build();

HttpGraphQlTester tester = HttpGraphQlTester.create(client);
```

Or to test against a live server running on a port:

```java
WebTestClient client =
		WebTestClient.bindToServer()
				.baseUrl("http://localhost:8080/graphql")
				.build();

HttpGraphQlTester tester = HttpGraphQlTester.create(client);
```

Once `HttpGraphQlTester` is created, you can begin to
[execute requests](#testing--testing.requests) using the same API, independent of the underlying
transport. If you need to change any transport specific details, use `mutate()` on an
existing `HttpSocketGraphQlTester` to create a new instance with customized settings:

```java
WebTestClient.Builder clientBuilder =
		WebTestClient.bindToServer()
				.baseUrl("http://localhost:8080/graphql");

HttpGraphQlTester tester = HttpGraphQlTester.builder(clientBuilder)
		.headers((headers) -> headers.setBasicAuth("joe", "..."))
		.build();

// Use tester...

HttpGraphQlTester anotherTester = tester.mutate()
		.headers((headers) -> headers.setBasicAuth("peter", "..."))
		.build();

// Use anotherTester...
```

<a id="testing--testing.websocketgraphqltester"></a>
<a id="testing--websocket"></a>

### WebSocket

`WebSocketGraphQlTester` executes GraphQL requests over a shared WebSocket connection.
It is built using the
[WebSocketClient](https://docs.spring.io/spring-framework/reference/web/webflux-websocket.html#webflux-websocket-client)
from Spring WebFlux and you can create it as follows:

```java
String url = "http://localhost:8080/graphql";
WebSocketClient client = new ReactorNettyWebSocketClient();

WebSocketGraphQlTester tester = WebSocketGraphQlTester.builder(url, client).build();
```

`WebSocketGraphQlTester` is connection oriented and multiplexed. Each instance establishes
its own single, shared connection for all requests. Typically, you’ll want to use a single
instance only per server.

Once `WebSocketGraphQlTester` is created, you can begin to
[execute requests](#testing--testing.requests) using the same API, independent of the underlying
transport. If you need to change any transport specific details, use `mutate()` on an
existing `WebSocketGraphQlTester` to create a new instance with customized settings:

```java
URI url = URI.create("ws://localhost:8080/graphql");
WebSocketClient client = new ReactorNettyWebSocketClient();

WebSocketGraphQlTester tester = WebSocketGraphQlTester.builder(url, client)
		.headers((headers) -> headers.setBasicAuth("joe", "..."))
		.build();

// Use tester...

WebSocketGraphQlTester anotherTester = tester.mutate()
		.headers((headers) -> headers.setBasicAuth("peter", "..."))
		.build();

// Use anotherTester...
```

`WebSocketGraphQlTester` provides a `stop()` method that you can use to have the WebSocket
connection closed, e.g. after a test runs.

<a id="testing--testing.rsocketgraphqltester"></a>
<a id="testing--rsocket"></a>

### RSocket

`RSocketGraphQlTester` uses `RSocketRequester` from spring-messaging to execute GraphQL
requests over RSocket:

```java
URI url = URI.create("wss://localhost:8080/rsocket");
WebsocketClientTransport transport = WebsocketClientTransport.create(url);

RSocketGraphQlTester client = RSocketGraphQlTester.builder()
		.clientTransport(transport)
		.build();
```

`RSocketGraphQlTester` is connection oriented and multiplexed. Each instance establishes
its own single, shared session for all requests. Typically, you’ll want to use a single
instance only per server. You can use the `stop()` method on the tester to close the
session explicitly.

Once `RSocketGraphQlTester` is created, you can begin to
[execute requests](#testing--testing.requests) using the same API, independent of the underlying
transport.

<a id="testing--testing.graphqlservicetester"></a>
<a id="testing--executiongraphqlservice"></a>

### `ExecutionGraphQlService`

Many times it’s enough to test GraphQL requests on the server side, without the use of a
client to send requests over a transport protocol. To test directly against a
`ExecutionGraphQlService`, use the `ExecutionGraphQlServiceTester` extension:

```java
ExecutionGraphQlService service = ...
ExecutionGraphQlServiceTester tester = ExecutionGraphQlServiceTester.create(service);
```

Once `ExecutionGraphQlServiceTester` is created, you can begin to
[execute requests](#testing--testing.requests) using the same API, independent of the underlying
transport.

`ExecutionGraphQlServiceTester.Builder` provides an option to customize `ExecutionInput` details:

```java
ExecutionGraphQlService service = ...
ExecutionId executionId = ExecutionId.generate();
ExecutionGraphQlServiceTester tester = ExecutionGraphQlServiceTester.builder(service)
		.configureExecutionInput((executionInput, builder) -> builder.executionId(executionId).build())
		.build();
```

<a id="testing--testing.webgraphqltester"></a>
<a id="testing--webgraphqlhandler"></a>

### `WebGraphQlHandler`

The [`ExecutionGraphQlService`](#testing--testing.graphqlservicetester) extension lets you test on the server side, without
a client. However, in some cases it’s useful to involve server side transport
handling with given mock transport input.

The `WebGraphQlTester` extension lets you processes request through the
`WebGraphQlInterceptor` chain before handing off to `ExecutionGraphQlService` for
request execution:

```java
WebGraphQlHandler handler = ...
WebGraphQlTester tester = WebGraphQlTester.create(handler);
```

The builder for this extension allows you to define HTTP request details:

```java
WebGraphQlHandler handler = ...
WebGraphQlTester tester = WebGraphQlTester.builder(handler)
		.headers((headers) -> headers.setBasicAuth("joe", "..."))
		.build();
```

Once `WebGraphQlTester` is created, you can begin to
[execute requests](#testing--testing.requests) using the same API, independent of the underlying transport.

<a id="testing--testing.graphqltester.builder"></a>
<a id="testing--builder"></a>

### Builder

`GraphQlTester` defines a parent `Builder` with common configuration options for the builders of all supported transports.
It lets you configure the following:

- `errorFilter` - a predicate to suppress expected errors, so you can inspect the data
  of the response.
- `documentSource` - a strategy for loading the document for a request from a file on
  the classpath or from anywhere else.
- `responseTimeout` - how long to wait for request execution to complete before timing
  out.

```java
GraphQlTransport transport = ...
Predicate<ResponseError> errorFilter = ...
ClassPathResource resource = new ClassPathResource("custom-folder/");
DocumentSource documentSource = new ResourceDocumentSource(resource);

GraphQlTester tester = GraphQlTester.builder(transport)
		.documentSource(documentSource)
		.errorFilter(errorFilter)
		.responseTimeout(Duration.ofSeconds(5))
		.build();
```

<a id="testing--testing.requests"></a>
<a id="testing--requests"></a>

## Requests

Once you have a `GraphQlTester`, you can begin to test requests. The below executes a
query for a project and uses [JsonPath](https://github.com/json-path/JsonPath) to extract
project release versions from the response:

```java
String document =""" {project(slug:"spring-framework") {releases {version}}} """;
graphQlTester.document(document) .execute() .path("project.releases[*].version") .entityList(String.class) .hasSizeGreaterThan(1);
```

The JsonPath is relative to the "data" section of the response.

You can also create document files with extensions `.graphql` or `.gql` under
`"graphql-test/"` on the classpath and refer to them by file name.

For example, given a file called `projectReleases.graphql` in
`src/main/resources/graphql-test`, with content:

```graphql
query projectReleases($slug: ID!) {
	project(slug: $slug) {
		releases {
			version
		}
	}
}
```

You can then use:

```java
graphQlTester.documentName("projectReleases") (1)
		.variable("slug", "spring-framework") (2)
		.execute()
		.path("projectReleases.project.releases[*].version")
		.entityList(String.class)
		.hasSizeGreaterThan(1);
```

**1**

Refer to the document in the file named "project".

**2**

Set the `slug` variable.

This approach also works for loading fragments for your queries.
Fragments are reusable field selection sets that avoid repetition in a request document.
For example, we can use a `…releases` fragment in multiple queries:

src/main/resources/graphql-documents/projectReleases.graphql

```graphql
query frameworkReleases {project(slug: "spring-framework") {name ...releases}} query graphqlReleases {project(slug: "spring-graphql") {name ...releases}}
```

This fragment can be defined in a separate file for reuse:

src/main/resources/graphql-documents/releases.graphql

```graphql
fragment releases on Project {
   	releases {
           version
       }
   }
```

You can then send this fragment along the query document:

```java
graphQlTester.documentName("projectReleases") (1)
		.fragmentName("releases") (2)
		.execute()
		.path("frameworkReleases.project.releases[*].version")
		.entityList(String.class)
		.hasSizeGreaterThan(1);
```

**1**

Load the document from "projectReleases.graphql"

**2**

Load the fragment from "releases.graphql" and append it to the document

> [!TIP]
> The "JS GraphQL" plugin for IntelliJ supports GraphQL query files with code completion.

If a request does not have any response data, e.g. mutation, use `executeAndVerify`
instead of `execute` to verify there are no errors in the response:

```java
graphQlTester.query(query).executeAndVerify();
```

See [Errors](#testing--testing.errors) for more details on error handling.

<a id="testing--testing.requests.nestedpaths"></a>
<a id="testing--nested-paths"></a>

### Nested Paths

By default, paths are relative to the "data" section of the GraphQL response. You can also
nest down to a path, and inspect multiple paths relative to it as follows:

```java
graphQlTester.document(document)
		.execute()
		.path("project", (project) -> project (1)
				.path("name").entity(String.class).isEqualTo("spring-framework")
				.path("releases[*].version").entityList(String.class).hasSizeGreaterThan(1));
```

**1**

Use a callback to inspect paths relative to "project".

<a id="testing--testing.subscriptions"></a>
<a id="testing--subscriptions"></a>

## Subscriptions

To test subscriptions, call `executeSubscription` instead of `execute` to obtain a stream
of responses and then use `StepVerifier` from Project Reactor to inspect the stream:

```java
Flux<String> greetingFlux = tester.document("subscription { greetings }")
		.executeSubscription()
		.toFlux("greetings", String.class);  // decode at JSONPath

StepVerifier.create(greetingFlux)
		.expectNext("Hi")
		.expectNext("Bonjour")
		.expectNext("Hola")
		.verifyComplete();
```

Subscriptions are supported only with [WebSocketGraphQlTester](#testing--testing.websocketgraphqltester)
, or with the server side
[`ExecutionGraphQlService`](#testing--testing.graphqlservicetester) and [`WebGraphQlHandler`](#testing--testing.webgraphqltester) extensions.

<a id="testing--testing.errors"></a>
<a id="testing--errors"></a>

## Errors

When you use `verify()`, any errors under the "errors" key in the response will cause
an assertion failure. To suppress a specific error, use the error filter before
`verify()`:

```java
graphQlTester.document(query)
		.execute()
		.errors()
		.filter((error) -> error.getMessage().equals("ignored error"))
		.verify()
		.path("project.releases[*].version")
		.entityList(String.class)
		.hasSizeGreaterThan(1);
```

You can register an error filter at the builder level, to apply to all tests:

```java
WebGraphQlTester graphQlTester = WebGraphQlTester.builder(handler)
		.errorFilter((error) -> error.getMessage().equals("ignored error"))
		.build();
```

If you want to verify that an error does exist, and in contrast to `filter`, throw an
assertion error if it doesn’t, then use `expect` instead:

```java
graphQlTester.document(query)
		.execute()
		.errors()
		.expect((error) -> error.getMessage().equals("expected error"))
		.verify()
		.path("project.releases[*].version")
		.entityList(String.class)
		.hasSizeGreaterThan(1);
```

You can also inspect all errors through a `Consumer`, and doing so also marks them as
filtered, so you can then also inspect the data in the response:

```java
graphQlTester.document(document)
		.execute()
		.errors()
		.satisfy((errors) ->
				assertThat(errors)
						.anyMatch((error) -> error.getMessage().contains("ignored error"))
		);
```

[GraphiQL](#graphiql)
[Boot Starter](#boot-starter)

---

<a id="boot-starter"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/boot-starter.html -->

<!-- page_index: 14 -->

# Boot Starter

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="boot-starter--page-title"></a>
<a id="boot-starter--boot-starter"></a>

# Boot Starter

Spring Boot provides a starter for building GraphQL applications with Spring for GraphQL.
For version information, see the
[Spring for GraphQL Versions](https://github.com/spring-projects/spring-graphql/wiki/Spring-for-GraphQL-Versions) wiki page.

The easiest way to get started is via [start.spring.io](https://start.spring.io) by selecting
"Spring for GraphQL" along with an underlying transport such as Spring MVC of WebFlux over
HTTP or WebSocket, or over RSocket. Refer to the
[Spring for GraphQL Starter](https://docs.spring.io/spring-boot/reference/web/spring-graphql.html)
section in the Spring Boot reference for details on supported transports, auto-configuration related
features, and more. For testing support, see
[Auto-Configured GraphQL Tests](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html#testing.spring-boot-applications.spring-graphql-tests).

For further reference, check the following GraphQL related:

- [Configuration Properties](https://docs.spring.io/spring-boot/appendix/application-properties/index.html#appendix.application-properties.web)
- [GraphQL Auto-Configuration Classes](https://docs.spring.io/spring-boot/appendix/auto-configuration-classes/spring-boot-autoconfigure.html)
- [GraphQL Actuator Auto-Configuration Classes](https://docs.spring.io/spring-boot/appendix/auto-configuration-classes/spring-boot-actuator-autoconfigure.html)

[Testing](#testing)
[Standalone Setup](#standalone-setup)

---

<a id="standalone-setup"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/standalone-setup.html -->

<!-- page_index: 15 -->

# Standalone Setup

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="standalone-setup--page-title"></a>
<a id="standalone-setup--standalone-setup"></a>

# Standalone Setup

If your application is not using Spring Boot, you are responsible for setting up the relevant Spring for GraphQL components.
Assuming that your application is already configured for Spring MVC controllers, the minimum setup will require several beans.

```java
import java.util.List;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.graphql.ExecutionGraphQlService;
import org.springframework.graphql.data.method.annotation.support.AnnotatedControllerConfigurer;
import org.springframework.graphql.execution.ConnectionTypeDefinitionConfigurer;
import org.springframework.graphql.execution.DefaultBatchLoaderRegistry;
import org.springframework.graphql.execution.DefaultExecutionGraphQlService;
import org.springframework.graphql.execution.GraphQlSource;
import org.springframework.graphql.server.WebGraphQlHandler;
import org.springframework.graphql.server.webmvc.GraphQlHttpHandler;
import org.springframework.graphql.server.webmvc.GraphQlRequestPredicates;
import org.springframework.graphql.server.webmvc.GraphiQlHandler;
import org.springframework.web.servlet.function.RequestPredicate;
import org.springframework.web.servlet.function.RouterFunction;
import org.springframework.web.servlet.function.RouterFunctions;
import org.springframework.web.servlet.function.ServerResponse;

@Configuration(proxyBeanMethods = false)
public class GraphQlConfiguration {

	@Bean (1)
	public AnnotatedControllerConfigurer controllerConfigurer() {
		return new AnnotatedControllerConfigurer();
	}

	@Bean (2)
	public ExecutionGraphQlService executionGraphQlService(AnnotatedControllerConfigurer controllerConfigurer) {
		GraphQlSource graphQlSource = GraphQlSource.schemaResourceBuilder() (3)
				.schemaResources(new ClassPathResource("graphql/schema.graphqls"))
				.configureTypeDefinitions(new ConnectionTypeDefinitionConfigurer())
				.configureRuntimeWiring(controllerConfigurer)
				.exceptionResolvers(List.of(controllerConfigurer.getExceptionResolver()))
				.build();
		DefaultBatchLoaderRegistry batchLoaderRegistry = new DefaultBatchLoaderRegistry();
		DefaultExecutionGraphQlService service = new DefaultExecutionGraphQlService(graphQlSource);
		service.addDataLoaderRegistrar(batchLoaderRegistry);
		return service;
	}


	@Bean (4)
	public RouterFunction<ServerResponse> graphQlRouterFunction(ExecutionGraphQlService graphQlService) {
		WebGraphQlHandler webGraphQlHandler = WebGraphQlHandler.builder(graphQlService).build();
		GraphQlHttpHandler graphQlHttpHandler = new GraphQlHttpHandler(webGraphQlHandler);
		RequestPredicate graphQlPredicate = GraphQlRequestPredicates.graphQlHttp("/graphql");
		GraphiQlHandler graphiQlHandler = new GraphiQlHandler("/graphql", "");
		return RouterFunctions.route() (5)
				.route(graphQlPredicate, graphQlHttpHandler::handleRequest)
				.GET("/graphiql", graphiQlHandler::handleRequest)
				.build();
	}
}
```

**1**

The `AnnotatedControllerConfigurer` bean is responsible for detecting GraphQL `@Controller` handlers.

**2**

The `ExecutionGraphQlService` processes GraphQL requests in a transport-agnostic fashion.

**3**

The `GraphQlSource` builder is the main configuration point. Explore its API for more options.

**4**

The `RouterFunction` exposes the GraphQL routes as [functional endpoints](https://docs.spring.io/spring-framework/reference/web/webmvc-functional.html).

**5**

You can then expose various transports (WebSocket, SSE, HTTP) over different routes.

Spring for GraphQL offers many other options and integrations with Spring projects.
For more on this, you can [explore the Spring Boot auto-configurations](#boot-starter).

[Boot Starter](#boot-starter)
[Samples](#samples)

---

<a id="samples"></a>

<!-- source_url: https://docs.spring.io/spring-graphql/reference/samples.html -->

<!-- page_index: 16 -->

# Samples

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="samples--page-title"></a>
<a id="samples--samples"></a>

# Samples

Please, see the [spring-graphql-examples](https://github.com/spring-projects/spring-graphql-examples) repository.

[Standalone Setup](#standalone-setup)

---
