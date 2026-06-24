# Apache Johnzon – Project Information

## Navigation

- User Guide
  - [Home](#index)
  - [Download](#download)
  - [Source Code](#scm)
  - [Changelog](#changelog)
  - [Mailing Lists](#mailing-lists)
- Old Releases
  - [Johnzon 0.7-incubating](#archives-0.7-incubating)
  - [Johnzon 0.2-incubating](#archives-0.2-incubating)
  - [Johnzon 0.1-incubating](#archives-0.1-incubating)
- Project Documentation
  - [Project Information](#project-info)
    - [CI Management](#ci-management)
    - [About](#index)
    - [Mailing Lists](#mailing-lists)
    - [Project Modules](#modules)
    - [Source Code Management](#scm)
    - [Summary](#summary)
    - [Team](#team)
    - [Issue Tracking](#archives-0.1-incubating-issue-tracking)
    - [Continuous Integration](#archives-0.1-incubating-integration)
    - [Project Summary](#archives-0.1-incubating-project-summary)
  - Project Reports
    - [Dependency Updates Report](#dependency-updates-report)
    - [Plugin Updates Report](#plugin-updates-report)
    - [Property Updates Report](#property-updates-report)
    - [Change Log](#changelog)
    - [File Activity](#file-activity)
    - [Developer Activity](#dev-activity)
- Security
  - [Report vulnerability](#security)
- Project Information
  - [About](#archives-0.2-incubating)
  - [Issue Tracking](#archives-0.2-incubating-issue-tracking)
  - [Continuous Integration](#archives-0.2-incubating-integration)
  - [Project Modules](#archives-0.2-incubating-modules)
  - [Project Summary](#archives-0.2-incubating-project-summary)
- Project Reports
  - [Dependency Updates Report](#archives-0.2-incubating-dependency-updates-report)
  - [Plugin Updates Report](#archives-0.2-incubating-plugin-updates-report)
  - [Property Updates Report](#archives-0.2-incubating-property-updates-report)
  - [Change Log](#archives-0.2-incubating-changelog)
  - [File Activity](#archives-0.2-incubating-file-activity)
  - [Developer Activity](#archives-0.2-incubating-dev-activity)
  - [JIRA Report](#archives-0.2-incubating-jira-report)
- Other pages
  - [Apache Johnzon - Project Modules](#archives-0.1-incubating-modules)
  - [Apache Johnzon - Change Log Report](#archives-0.7-incubating-changelog)
  - [Apache Johnzon - Dependency Updates Report](#archives-0.7-incubating-dependency-updates-report)
  - [Apache Johnzon - Developer Activity Report](#archives-0.7-incubating-dev-activity)
  - [Apache Johnzon - File Activity Report](#archives-0.7-incubating-file-activity)
  - [Apache Johnzon - Continuous Integration](#archives-0.7-incubating-integration)
  - [Apache Johnzon - Issue Tracking](#archives-0.7-incubating-issue-tracking)
  - [Apache Johnzon - Project Modules](#archives-0.7-incubating-modules)
  - [Apache Johnzon - Plugin Updates Report](#archives-0.7-incubating-plugin-updates-report)
  - [Apache Johnzon - Project Summary](#archives-0.7-incubating-project-summary)
  - [Apache Johnzon - Property Updates Report](#archives-0.7-incubating-property-updates-report)

## Content

<a id="index"></a>

<!-- source_url: https://johnzon.apache.org/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-johnzon"></a>

# Apache Johnzon

Apache Johnzon is a project providing an implementation of JsonProcessing (aka JSR-353) and a set of useful extension
for this specification like an Object mapper, some JAX-RS providers and a WebSocket module provides a basic integration with Java WebSocket API (JSR-356).

<a id="index--status"></a>

## Status

Apache Johnzon is a Top Level Project at the Apache Software Foundation (ASF).
It fully implements the [JSON-P 2.1](https://jakarta.ee/specifications/jsonp/2.1/) and [JSON-B 3.0](https://jakarta.ee/specifications/jsonb/3.0/) specifications.

<a id="index--get-started"></a>

## Get started

Johnzon comes with four main modules.

<a id="index--core-stable"></a>

### Core (stable)

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-core</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This is the implementation of the JSON-P 2.1 specification.
You'll surely want to add the API as dependency too:

```

<dependency>
  <groupId>jakarta.json</groupId>
  <artifactId>jakarta.json-api</artifactId>
  <version>2.1.2</version>
  <scope>provided</scope> <!-- or compile if your environment doesn't provide it -->
</dependency>
```

**Please note**: The jakarta JSON-P API jar has [hardcoded parsson](https://github.com/jakartaee/jsonp-api/blob/2.1.2/api/src/main/java/jakarta/json/spi/JsonProvider.java#L74-L79) as the default JSON-P implementation.
This might cause unintended behaviour in cases where standard Java service loading is not possible.

<a id="index--johnzon-factory-configurations"></a>

#### Johnzon Factory Configurations

<a id="index--jsongeneratorfactory"></a>

##### JsonGeneratorFactory

The generator factory supports the standard properties (pretty one for example) but also:

- `org.apache.johnzon.encoding`: encoding to use for the generator when converting an OutputStream to a Writer.
- `org.apache.johnzon.buffer-strategy`: how to get buffers (char buffer), default strategy is a queue/pool based one but you can switch it to a `THREAD_LOCAL` one. `BY_INSTANCE` (per call/prototype) and `SINGLETON` (single instance) are also supported but first one is generally slower and last one does not enable overflows.
- `org.apache.johnzon.default-char-buffer-generator` (int): buffer size of the generator, it enables to work in memory to flush less often (for performances).
- `org.apache.johnzon.boundedoutputstreamwriter` (int): when converting an `OuputStream` to a `Writer` it defines the buffer size (if > 0) +- 2 charaters (for the encoding logic). It enables a faster flushing to the actual underlying output stream combined with `org.apache.johnzon.default-char-buffer-generator`.

<a id="index--json-p-strict-compliance-stable"></a>

### JSON-P Strict Compliance (stable)

**This has been removed with Johnzon 2.0.x, johnzon-core is now JSON-P compliant by default.**

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jsonp-strict</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This module enables to enforce a strict compliance of JsonPointer behavior on `/-` usage.
Johnzon default implementation enables an extended usage of it for replace/remove and get operations.
In that case, it will point to the last element of the array so it's easy to replace/remove or get the last element of the array.
For add operation, it remains the same, aka points to the element right after the last element of the array.

This module enforces Johnzon to be JSONP compliant and fail if `/-` is used for anything but add.

Note that you can even customize this behavior implementing your own `JsonPointerFactory` and changing the ordinal value to take a highest priority.

<a id="index--mapper-stable"></a>

### Mapper (stable)

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-mapper</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

The mapper module allows you to use the implementation you want of Json Processing specification to map
Json to Object and the opposite.

```

final MySuperObject object = createObject();

final Mapper mapper = new MapperBuilder().build();
mapper.writeObject(object, outputStream);

final MySuperObject otherObject = mapper.readObject(inputStream, MySuperObject.class);
```

The mapper uses a direct java to json representation.

For instance this java bean:

```

public class MyModel {
  private int id;
  private String name;
  
  // getters/setters
}
```

will be mapped to:

```

{
  "id": 1234,
  "name": "Johnzon doc"
}
```

Note that Johnzon supports several customization either directly on the MapperBuilder of through annotations.

<a id="index--johnzonignore"></a>

#### @JohnzonIgnore

@JohnzonIgnore is used to ignore a field. You can optionally say you ignore the field until some version
if the mapper has a version:

```

public class MyModel {
  @JohnzonIgnore
  private String name;
  
  // getters/setters
}
```

Or to support name for version 3, 4, … but ignore it for 1 and 2:

```

public class MyModel {
  @JohnzonIgnore(minVersion = 3)
  private String name;
  
  // getters/setters
}
```

<a id="index--johnzonconverter"></a>

#### @JohnzonConverter

Converters are used for advanced mapping between java and json.

There are several converter types:

1. Converter: map java to json and the opposite based on the string representation
2. Adapter: a converter not limited to String
3. ObjectConverter.Reader: to converter from json to java at low level
4. ObjectConverter.Writer: to converter from java to json at low level
5. ObjectConverter.Codec: a Reader and Writer

The most common is to customize date format but they all take. For that simple case we often use a Converter:

```
public class LocalDateConverter implements Converter<LocalDate> {@Override public String toString(final LocalDate instance) {return instance.toString();}
@Override public LocalDate fromString(final String text) {return LocalDate.parse(text);}}
```

If you need a more advanced use case and modify the structure of the json (wrapping the value for instance)
you will likely need Reader/Writer or a Codec.

Then once your converter developed you can either register globally on the MapperBuilder or simply decorate
the field you want to convert with @JohnzonConverter:

```

public class MyModel {
  @JohnzonConverter(LocalDateConverter.class)
  private LocalDate date;
  
  // getters/setters
}
```

<a id="index--johnzonproperty"></a>

#### @JohnzonProperty

Sometimes the json name is not java friendly (\_foo or foo-bar or even 200 for instance). For that cases
@JohnzonProperty allows to customize the name used:

```

public class MyModel {
  @JohnzonProperty("__date")
  private LocalDate date;
  
  // getters/setters
}
```

<a id="index--johnzonany"></a>

#### @JohnzonAny

If you don't fully know your model but want to handle all keys you can use @JohnzonAny to capture/serialize them all:

```
public class AnyMe {private String name; // Regular serialization for the known 'name' field
/* This example uses a TreeMap to store and retrieve the other unknown fields for the @JohnzonAny annotated methods, but you can choose anything you want. Use @JohnzonIgnore to avoid exposing this as an actual 'unknownFields' property in JSON.*/ @JohnzonIgnore private Map<String, Object> unknownFields = new TreeMap<String, Object>();
public String getName() {return name;}
public void setName(final String name) {this.name = name;}
@JohnzonAny public Map<String, Object> getAny() {return unknownFields;}
@JohnzonAny public void handle(final String key, final Object val) {this.unknownFields.put(key, val);}}
```

<a id="index--accessmode"></a>

#### AccessMode

On MapperBuilder you have several AccessMode available by default but you can also create your own one.

The default available names are:

- field: to use fields model and ignore getters/setters
- method: use getters/setters (means if you have a getter but no setter you will serialize the property but not read it)
- strict-method (default based on Pojo convention): same as method but getters for collections are not used to write
- both: field and method accessors are merged together

You can use these names with setAccessModeName().

<a id="index--jax-rs-stable"></a>

### JAX-RS (stable)

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jaxrs</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

JAX-RS module provides two providers (and underlying MessageBodyReaders and MessageBodyWriters):

- org.apache.johnzon.jaxrs.[Wildcard]JohnzonProvider: use Johnzon Mapper to map Object to Json and the opposite
- org.apache.johnzon.jaxrs.[Wildcard]ConfigurableJohnzonProvider: same as JohnzonProvider but with setters to ease the configuration of the provider in most servers/containers
- org.apache.johnzon.jaxrs.[Wildcard]JsrProvider: allows you to use JsrArray, JsrObject (more generally JsonStructure)

Note: Wildcard providers are basically the same as other provider but instead of application/json they support \*/json, */*+json, \*/x-json, \*/javascript, \*/x-javascript. This
split makes it easier to mix json and other MediaType in the same resource (like text/plain, xml etc since JAX-RS API always matches as true wildcard type in some version whatever the subtype is).

Tip: ConfigurableJohnzonProvider maps most of MapperBuilder configuration letting you configure it through any IoC including not programming language based formats.

IMPORTANT: when used with `johnzon-core`, `NoContentException` is not thrown in case of an empty incoming input stream by these providers except `JsrProvider` to limit the breaking changes.

<a id="index--tomee-configuration"></a>

### TomEE Configuration

TomEE uses by default Johnzon as JAX-RS provider for versions 7.x. If you want however to customize it you need to follow this procedure:

1. Create a WEB-INF/openejb-jar.xml:

```

<?xml version="1.0" encoding="UTF-8"?>
<openejb-jar>
  <pojo-deployment class-name="jaxrs-application">
    <properties>
      # optional but requires to skip scanned providers if set to true
      cxf.jaxrs.skip-provider-scanning = true
      # list of providers we want
      cxf.jaxrs.providers = johnzon,org.apache.openejb.server.cxf.rs.EJBAccessExceptionMapper
    </properties>
  </pojo-deployment>
</openejb-jar>
```

1. Create a WEB-INF/resources.xml to define johnzon service which will be use to instantiate the provider

```

<?xml version="1.0" encoding="UTF-8"?>
<resources>
  <Service id="johnzon" class-name="org.apache.johnzon.jaxrs.ConfigurableJohnzonProvider">
    # 1M
    maxSize = 1048576
    bufferSize = 1048576

    # ordered attributes
    attributeOrder = $order

    # Additional types to ignore
    ignores = org.apache.cxf.jaxrs.ext.multipart.MultipartBody
  </Service>

  <Service id="order" class-name="com.company.MyAttributeSorter" />

</resources>
```

Note: as you can see you mainly just need to define a service with the id johnzon (same as in openejb-jar.xml)
and you can reference other instances using $id for services and @id for resources.

<a id="index--json-b-json-b-3.0-compliant"></a>

### JSON-B (JSON-B 3.0 compliant)

Johnzon provides a module johnzon-jsonb implementing JSON-B standard based on Johnzon Mapper.

It fully reuses the JSON-B as API.

However it supports some specific properties to wire to the native johnzon configuration - see `JohnzonBuilder` for details.
One example is `johnzon.interfaceImplementationMapping` which will support a `Map<Class,Class>` to map interfaces to implementations
to use for deserialization.

JsonbConfig specific properties:

- johnzon.use-big-decimal-for-object: true to use BigDecimal for numbers not typed (Object), false to adjust the type to the number size, true by default.
- johnzon.support-enum-container-deserialization: prevent EnumMap/EnumSet instantiation, true by default.
- johnzon.attributeOrder: Comparator instance to sort properties by name.
- johnzon.deduplicateObjects: should instances be deduplicated.
- johnzon.supportsPrivateAccess: should private constructors/methods with `@JsonbCreator` be used too.
- johnzon.fail-on-unknown-properties: should unmapped properties fail the mapping. Similar to `jsonb.fail-on-unknown-properties`.
- johnzon.readAttributeBeforeWrite: should collection be read before being written, it enables to have an “append” mode.
- johnzon.autoAdjustBuffer: should internal read buffers be autoadjusted to stay fixed.
- johnzon.serialize-value-filter: enable to set a filter to not serialize some values.
- johnzon.cdi.activated: should cdi support be active.
- johnzon.accessMode: custom access mode, note that it can disable some JSON-B feature (annotations support).
- johnzon.accessModeDelegate: delegate access mode used by JsonbAccessModel. Enables to enrich default access mode.
- johnzon.failOnMissingCreatorValues: should the mapping fail when a `@JsonbCreator` misses some values.
- johnzon.use-biginteger-stringadapter: Whether or not `BigInteger` is mapped as a string. `true` by default, set to `false` to ensure strict JSON-B 3 compliance
- johnzon.use-bigdecimal-stringadapter: Whether or not `BigDecimal` is mapped as a string. `true` by default, set to `false` to ensure strict JSON-B 3 compliance

TIP: more in JohnzonBuilder class.

A JAX-RS provider based on JSON-B is provided in the module as well. It is `org.apache.johnzon.jaxrs.jsonb.jaxrs.JsonbJaxrsProvider`.

IMPORTANT: in JAX-RS 1.0 the provider can throw any exception he wants for an empty incoming stream on reader side. This had been broken in JAX-RS 2.x where it must throw a `jakarta.ws.rs.core.NoContentException`.
To ensure you can pick the implementation you can and limit the breaking changes, you can set ̀throwNoContentExceptionOnEmptyStreams`on the provider to switch between both behaviors. Default will be picked from the current available API. Finally, this behavior only works with`johnzon-core`.

<a id="index--integration-with-jsonvalue"></a>

#### Integration with `JsonValue`

You can use some optimization to map a `JsonObject` to a POJO using Johnzon `JsonValueReader` - or any implementation of `Reader` implementing `Supplier<JsonStructure>` - and `JsonValueWriter` - or any implementation of `Writer` implementing `Consumer<JsonValue>` -:

```

final JsonValueReader<Simple> reader = new JsonValueReader<>(Json.createObjectBuilder().add("value", "simple").build());
final Jsonb jsonb = getJohnzonJsonb();
final Simple simple = jsonb.fromJson(reader, SomeModel.class);
```

```

final JsonValueWriter writer = new JsonValueWriter();
final Jsonb jsonb = getJohnzonJsonb();
jsonb.toJson(object, writer);
final JsonObject jsonObject = writer.getObject();
```

These two example will not use any IO and directly map the `JsonValue` to/from a POJO.

Also note that, as an experimental extension and pre-available feature of the next specification version, `org.apache.johnzon.jsonb.api.experimental.JsonbExtension` enables
to map POJO to `JsonValue` and the opposite.

<a id="index--websocket"></a>

### Websocket

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-websocket</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

WebSocket module provides a basic integration with Java WebSocket API (JSR 356).

Integration is at codec level (encoder/decoder). There are two families of codecs:

- The ones based on JSON-P (JsonObject, JsonArray, JsonStructure)
- The ones based on Johnzon Mapper

Note that if you want to control the Mapper or JSON-B instance used by decoders you can set up the associated servlet listeners:

- org.apache.johnzon.websocket.internal.mapper.MapperLocator for johnzon-mapper
- org.apache.johnzon.websocket.jsonb.JsonbLocator for JSON-B

if you write in the servlet context an attribute named `org.apache.johnzon.websocket.internal.mapper.MapperLocator.mapper` (it is a `Supplier<Mapper>`) or `org.apache.johnzon.websocket.jsonb.JsonbLocator.jsonb` (depending the implementation you use) it will be used instead of the default instance.

<a id="index--json-p-integration"></a>

#### JSON-P integration

Encoders:

- `org.apache.johnzon.websocket.jsr.JsrObjectEncoder`
- `org.apache.johnzon.websocket.jsr.JsrArrayEncoder`
- `org.apache.johnzon.websocket.jsr.JsrStructureEncoder`

Decoders:

- `org.apache.johnzon.websocket.jsr.JsrObjectDecoder`
- `org.apache.johnzon.websocket.jsr.JsrArrayDecoder`
- `org.apache.johnzon.websocket.jsr.JsrStructureDecoder`

<a id="index--mapper-integration"></a>

#### Mapper integration

Encoder:

- `org.apache.johnzon.websocket.mapper.JohnzonTextEncoder`

Decoder:

- `org.apache.johnzon.websocket.mapper.JohnzonTextDecoder`

<a id="index--json-b-integration"></a>

#### JSON-B integration

Encoder:

- `org.apache.johnzon.websocket.jsonb.JsonbTextEncoder`

Decoder:

- `org.apache.johnzon.websocket.jsonb.JsonbTextDecoder`

<a id="index--sample"></a>

#### Sample

<a id="index--json-p-samples"></a>

##### JSON-P Samples

On server and client side configuration is easy: just provide the `encoders` and `decoders` parameters to `@[Server|Client]Endpoint`
(or `EndpointConfig` if you use programmatic API)):

```
@ClientEndpoint(encoders = JsrObjectEncoder.class, decoders = JsrObjectDecoder.class) public class JsrClientEndpointImpl {@OnMessage public void on(final JsonObject message) {// ...}}
@ServerEndpoint(value = "/my-server", encoders = JsrObjectEncoder.class, decoders = JsrObjectDecoder.class) public class JsrClientEndpointImpl {@OnMessage public void on(final JsonObject message) {// ...}}
```

<a id="index--websocket-samples"></a>

##### WebSocket Samples

Server configuration is as simple as providing `encoders` and `decoders` parameters to `@ServerEndpoint`:

```
@ServerEndpoint(value = "/server", encoders = JohnzonTextEncoder.class, decoders = JohnzonTextDecoder.class)
public class ServerEndpointImpl {
    @OnMessage
    public void on(final Session session, final Message message) {
        // ...
    }
}
```

Client configuration is almost the same excepted in this case it is not possible for Johnzon
to guess the type you expect so you'll need to provide it. In next sample it is done just extending `JohnzonTextDecoder`
in `MessageDecoder`.

```
@ClientEndpoint(encoders = JohnzonTextEncoder.class, decoders = ClientEndpointImpl.MessageDecoder.class) public class ClientEndpointImpl {@OnMessage public void on(final Message message) {// ...}
public static class MessageDecoder extends JohnzonTextDecoder {public MessageDecoder() {super(Message.class);}}}
```

<a id="index--json-b-extra"></a>

### JSON-B Extra

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jsonb-extras</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This module provides some extension to JSON-B.

<a id="index--polymorphism"></a>

#### Polymorphism

This extension shouldn't be used anymore if you don't absolutely rely on the JSON format it generates/parses.
Use JSON-B 3 polymorphism instead. It provides a way to handle polymorphism:

For the deserialization side you have to list the potential children
on the root class:

```
@Polymorphic.JsonChildren({
        Child1.class,
        Child2.class
})
public abstract class Root {
    public String name;
}
```

Then on children you bind an “id” for each of them (note that if you don't give one, the simple name is used):

```
@Polymorphic.JsonId("first")
public class Child1 extends Root {
    public String type;
}
```

Finally on the field using the root type (polymorphic type) you can
bind the corresponding serializer and/or deserializer:

```
public class Wrapper {
    @JsonbTypeSerializer(Polymorphic.Serializer.class)
    @JsonbTypeDeserializer(Polymorphic.DeSerializer.class)
    public Root root;

    @JsonbTypeSerializer(Polymorphic.Serializer.class)
    @JsonbTypeDeserializer(Polymorphic.DeSerializer.class)
    public List<Root> roots;
}
```

Binding the polymophic serializer and/or deserializer *must not* be done using `JsonbConfig.withSerializers` / `JsonbConfig.withDeserializers`, as it is designed to work *only* with binding performed *using annotations*.

<a id="index--json-schema"></a>

### JSON Schema

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jsonschema</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This module provides a way to validate an instance against a [JSON Schema](http://json-schema.org/).

```

// long live instances (@ApplicationScoped/@Singleton)
JsonObject schema = getJsonSchema();
JsonSchemaValidatorFactory factory = new JsonSchemaValidatorFactory();
JsonSchemaValidator validator = factory.newInstance(schema);

// runtime starts here
JsonObject objectToValidateAgainstSchema = getObject();
ValidatinResult result = validator.apply(objectToValidateAgainstSchema);
// if result.isSuccess, result.getErrors etc...

// end of runtime
validator.close();
factory.close();
```

Known limitations are (feel free to do a PR on github to add these missing features):

- Doesn't support references in the schema
- Doesn't support: dependencies, propertyNames, if/then/else, allOf/anyOf/oneOf/not, format validations

<a id="index--json-logic"></a>

### JSON Logic

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jsonlogic</artifactId>
  <version>${johnzon.version}</version>
</dependency>
<dependency> <!-- requires an implementation of JSON-P -->
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-core</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This module provides a way to execute any [JSON Logic](http://jsonlogic.com/) expression.

```

final JohnzonJsonLogic jsonLogic = new JohnzonJsonLogic();
final JsonValue result = jsonLogic.apply(
        builderFactory.createObjectBuilder()
                .add("merge", builderFactory.createArrayBuilder()
                        .add(builderFactory.createArrayBuilder()
                                .add(1)
                                .add(2))
                        .add(3)
                        .add("4"))
                .build(),
        JsonValue.EMPTY_JSON_ARRAY);
```

Default operators are supported - except “log” one to let you pick the logger (impl + name) you want.

To register a custom operator just do it on your json logic instance:

```

final JohnzonJsonLogic jsonLogic = new JohnzonJsonLogic();
jsonLogic.registerOperator(
  "log",
  (jsonLogic, config, args) -> log.info(String.valueOf(jsonLogic.apply(config, args)));
```

Note that by default the set of standard JSON Logic operators is enriched with JSON-P jsonpatch, json merge diff and json merge patch operators.

<a id="index--osgi-jax-rs-whiteboard"></a>

### OSGi JAX-RS Whiteboard

Though Johnzon artifacts are OSGi bundles to begin with, this module provides further integration with the [OSGi JAX-RS Whiteboard](https://osgi.org/specification/osgi.cmpn/7.0.0/service.jaxrs.html) and [OSGi CDI Integration](https://osgi.org/specification/osgi.enterprise/7.0.0/service.cdi.html) specifications.

<a id="index--jax-rs-json-b"></a>

##### JAX-RS JSON-B

This module provides `MessageBodyWriter` and `MessageBodyReader` extensions for the media type `application/json` (by default) to whiteboard JAX-RS Applications.

Configuration of this extension is managed via Configuration Admin using the **pid** `org.apache.johnzon.jaxrs.jsonb` and defines a Metatype schema with the following properties:

| Property | Synopsis | Type | Default |
| —- | ————- | – | – |
| `ignores` | List of fully qualified class names to ignore | String[] | empty |
| `osgi.jaxrs.application.select` | Filter expression used to match the extension to JAX-RS Whiteboard Applications | String | `(!(johnzon.jsonb=false))` *(which is a convention allowing the extension to bind to all applications unless the application is configured with `johnzon.jsonb=false`)* |
| `osgi.jaxrs.media.type` | List of media types handled by the extension | String[] | `application/json` |
| `throw.no.content.exception.on.empty.streams` | | boolean | `false` |
| `fail.on.unknown.properties` | | boolean | `false` |
| `use.js.range` | | boolean | `false` |
| `other.properties` | | String | empty |
| `ijson` | | boolean | `false` |
| `encoding` | | String | empty |
| `binary.datastrategy` | | String | empty |
| `property.naming.strategy` | | String | empty |
| `property.order.strategy` | | String | empty |
| `null.values` | | boolean | `false` |
| `pretty` | | boolean | `false` |
| `fail.on.missing.creator.values` | | boolean | `false` |
| `polymorphic.serialization.predicate` | | String | empty |
| `polymorphic.deserialization.predicate` | | String | empty |
| `polymorphic.discriminator` | | String | empty |

<a id="index--cdi"></a>

##### CDI

Since JSON-B specification provides an integration with the CDI specification to handle caching, this module also provides such integration for OSGi CDI Integration specification by providing an `jakarta.enterprise.inject.spi.Extension` service with the required service property `osgi.cdi.extension` with the value `JavaJSONB`.

<a id="index--implicit-extensions"></a>

##### Implicit Extensions

In order to reduce the burden of configuration Apache Aries CDI (the OSGi CDI Integration RI) provides a feature of implicit extensions. These are extensions which the developer doesn't have to configure a requirement for in their CDI bundle. The Johnzon JSON-B CDI extension is such an extension and as such when running in Aries CDI does not need to be required.

This is achieve using the service property `aries.cdi.extension.mode=implicit`.

---

<a id="download"></a>

<!-- source_url: https://johnzon.apache.org/download.html -->

<!-- page_index: 2 -->

<a id="download--apache-johnzon-releases"></a>

# Apache Johnzon Releases

This page contains download links to the latest Apache Johnzon releases.

All maven artifacts are available in the Maven.Central repository with the groupId `org.apache.johnzon`.
The dependencies you can use are listed at the bottom of this page: [Maven Dependencies](#download--maven_dependencies).

should be addressed to the [mailing list](http://johnzon.apache.org/mail-lists.html).

<a id="download--keys-for-verifying-apache-releases"></a>

## KEYS for verifying Apache releases

Please use the Johnzon [KEYS](https://www.apache.org/dyn/closer.lua/johnzon/KEYS) file to validate our releases.
Read more about [how we sign Apache Releases](http://www.apache.org/info/verification.html)

---

<a id="download--johnzon-2.0.x"></a>

## Johnzon-2.0.x

Apache Johnzon 2.0.x implements the JSON-P 2.1 and JSON-B 3.0 specifications which are in line with the Jakarta EE Platform 10. This version is not backward compatible due to the namespace change from `javax` to `jakarta`.
Apache Johnzon does not implement Jakarta EE 9 per se, because there was no change in terms of APIs except the namespace change.
So we decided to use Apache Johnzon 1.2.x bellow and publish a Jakarta compatible version using bytecode transformation. All artifacts can be used with the classifier `jakarta`.

<a id="download--binaries"></a>

#### Binaries

Binaries should be obtained from [maven central](https://repo.maven.apache.org/maven2/org/apache/johnzon/).

<a id="download--source"></a>

#### Source

Should you want to build any of the above binaries, this source bundle is the right one and covers them all.

- [apache-johnzon-2.0.1-src.zip](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-2.0.1/apache-johnzon-2.0.1-src.zip)
- [apache-johnzon-2.0.1-src.zip.sha512](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-2.0.1/apache-johnzon-2.0.1-src.zip.sha512)
- [apache-johnzon-2.0.1-src.zip.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-2.0.1/apache-johnzon-2.0.1-src.zip.asc)
- [apache-johnzon-2.0.1-src.tar.gz](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-2.0.1/apache-johnzon-2.0.1-src.tar.gz)
- [apache-johnzon-2.0.1-src.tar.gz.sha512](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-2.0.1/apache-johnzon-2.0.1-src.tar.gz.sha512)
- [apache-johnzon-2.0.1-src.tar.gz.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-2.0.1/apache-johnzon-2.0.1-src.tar.gz.asc)

<a id="download--johnzon-1.2.x"></a>

## Johnzon-1.2.x

Apache Johnzon 1.2.x implements the JSON-P 1.1 and JSON-B 1.0 specifications which are in line with the Jakarta EE Platform 8.

<a id="download--binaries-2"></a>

#### Binaries

Binaries should be obtained from [maven central](https://repo.maven.apache.org/maven2/org/apache/johnzon/).

<a id="download--source-2"></a>

#### Source

Should you want to build any of the above binaries, this source bundle is the right one and covers them all.

- [apache-johnzon-1.2.21-src.zip](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.2.21/apache-johnzon-1.2.21-src.zip)
- [apache-johnzon-1.2.21-src.zip.sha512](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.2.21/apache-johnzon-1.2.21-src.zip.sha512)
- [apache-johnzon-1.2.21-src.zip.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.2.21/apache-johnzon-1.2.21-src.zip.asc)
- [apache-johnzon-1.2.21-src.tar.gz](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.2.21/apache-johnzon-1.2.21-src.tar.gz)
- [apache-johnzon-1.2.21-src.tar.gz.sha512](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.2.21/apache-johnzon-1.2.21-src.tar.gz.sha512)
- [apache-johnzon-1.2.21-src.tar.gz.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.2.21/apache-johnzon-1.2.21-src.tar.gz.asc)

<a id="download--johnzon-1.0.x"></a>

## Johnzon-1.0.x

Apache Johnzon 1.0.x implements the JSON-P 1.0 specification and a preliminary version of the JSON-B 1.0.
This corresponds to JavaEE 7 level.

<a id="download--binaries-3"></a>

#### Binaries

The binary distribution contains all Johnzon modules.

- [apache-johnzon-1.0.2-bin.zip](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-bin.zip)
- [apache-johnzon-1.0.2-bin.zip.sha256](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-bin.zip.sha256)
- [apache-johnzon-1.0.2-bin.zip.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-bin.zip.asc)
- [apache-johnzon-1.0.2-bin.tar.gz](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-bin.tar.gz)
- [apache-johnzon-1.0.2-bin.tar.gz.sha256](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-bin.tar.gz.sha256)
- [apache-johnzon-1.0.2-bin.tar.gz.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-bin.tar.gz.asc)

<a id="download--source-3"></a>

#### Source

Should you want to build any of the above binaries, this source bundle is the right one and covers them all.

- [apache-johnzon-1.0.2-src.zip](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-src.zip)
- [apache-johnzon-1.0.2-src.zip.sha256](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-src.zip.sha256)
- [apache-johnzon-1.0.2-src.zip.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-src.zip.asc)
- [apache-johnzon-1.0.2-src.tar.gz](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-src.tar.gz)
- [apache-johnzon-1.0.2-src.tar.gz.sha256](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-src.tar.gz.sha256)
- [apache-johnzon-1.0.2-src.tar.gz.asc](https://www.apache.org/dyn/closer.lua/johnzon/johnzon-1.0.2/apache-johnzon-1.0.2-src.tar.gz.asc)

---

<a id="download--maven-dependencies"></a>

### Maven Dependencies

<a id="download--apis-for-johnzon-2.0.x-jakarta-ee-10"></a>

#### APIs for Johnzon-2.0.x (Jakarta EE 10)

Since Java EE got open sourced to become Jakarta EE, the APIs can be used without license restrictions, so we moved away from our Apache APIs.

```
<dependency>
    <groupId>jakarta.json</groupId>
    <artifactId>jakarta.json-api</artifactId>
    <version>2.1.1</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>jakarta.json.bind</groupId>
    <artifactId>jakarta.json.bind-api</artifactId>
    <version>3.0</version>
    <scope>provided</scope>
</dependency>
```

<a id="download--apis-for-johnzon-1.1.x-javaee-8"></a>

#### APIs for Johnzon-1.1.x (JavaEE 8)

```
<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-json_1.1_spec</artifactId>
    <version>1.0</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-jsonb_1.0_spec</artifactId>
    <version>1.2</version>
</dependency>
```

<a id="download--apis-for-johnzon-1.0.x-javaee-7"></a>

#### APIs for Johnzon-1.0.x (JavaEE 7)

```
<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-json_1.0_spec</artifactId>
    <version>1.0-alpha-1</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-jsonb_1.0_spec</artifactId>
    <version>1.0</version>
</dependency>
```

Note that you should set the scope of those dependencies to either `provided` or `compile` depending on whether your environment already provide them or not.

---

<a id="scm"></a>

<!-- source_url: https://johnzon.apache.org/scm.html -->

<!-- page_index: 3 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://git-wip-us.apache.org/repos/asf?p=johnzon.git
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://git-wip-us.apache.org/repos/asf/johnzon.git
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://git-wip-us.apache.org/repos/asf/johnzon.git
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="changelog"></a>

<!-- source_url: https://johnzon.apache.org/changelog.html -->

<!-- page_index: 4 -->

<a id="changelog--change-log-report"></a>

## Change Log Report

Total number of changed sets: 1

<a id="changelog--changes-between-02-mar-2024-and-02-apr-2024"></a>

### Changes between 02 Mar, 2024 and 02 Apr, 2024

Total commits: 8 Total number of files changed: 19

| Timestamp | Author | Details |
| --- | --- | --- |
| 2024-04-01 20:50:30 | Markus Jung <jungm@apache.org> | [src/site/markdown/**download.md**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/src/site/markdown/download.md?p=johnzon.git) [v 21f3165c499e23e254da888d04dc0930adc3a8d0](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/src/site/markdown/download.md?rev=21f3165c499e23e254da888d04dc0930adc3a8d0&content-type=text/vnd.viewcvs-markup&p=johnzon.git) johnzon 2.0.1 released |
| 2024-03-23 21:01:43 | Markus Jung <jungm@apache.org> | [**KEYS**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/KEYS?p=johnzon.git) [v 856e3b26446454a3002333963580c87517a60589](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/KEYS?rev=856e3b26446454a3002333963580c87517a60589&content-type=text/vnd.viewcvs-markup&p=johnzon.git) Add jungm code signing key |
| 2024-03-23 08:25:58 | Markus Jung <jungm@apache.org> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-core/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-core/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-distribution/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-distribution/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-distribution/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jaxrs/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jaxrs/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-json-extras/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-json-extras/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-json-extras/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jsonb/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonb/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonb/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jsonlogic/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonlogic/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonlogic/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jsonschema/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonschema/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonschema/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-maven-plugin/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-osgi/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-osgi/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-osgi/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-websocket/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-websocket/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-websocket/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?p=johnzon.git) [v 9b4e43b43cdfd7ffcd4274d958e02da7e9243572](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?rev=9b4e43b43cdfd7ffcd4274d958e02da7e9243572&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [maven-release-plugin] prepare for next development iteration |
| 2024-03-23 08:25:57 | Markus Jung <jungm@apache.org> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-core/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-core/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-distribution/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-distribution/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-distribution/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jaxrs/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jaxrs/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-json-extras/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-json-extras/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-json-extras/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jsonb/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonb/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonb/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jsonlogic/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonlogic/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonlogic/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-jsonschema/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonschema/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonschema/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-maven-plugin/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-osgi/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-osgi/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-osgi/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-websocket/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-websocket/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-websocket/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?p=johnzon.git) [v 69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?rev=69d8185b99b1fcaf91ac77d9e309a3d6e0e1383c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [maven-release-plugin] prepare release v2.0.1 |
| 2024-03-19 22:44:02 | Heewon Lee <94441510+pingpingy1@users.noreply.github.com> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingInputStream.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingInputStream.java?p=johnzon.git) [v baa4f3d47f79b048b5d473124e2e479fe8b8ec6c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingInputStream.java?rev=baa4f3d47f79b048b5d473124e2e479fe8b8ec6c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingOutputStream.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingOutputStream.java?p=johnzon.git) [v baa4f3d47f79b048b5d473124e2e479fe8b8ec6c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingOutputStream.java?rev=baa4f3d47f79b048b5d473124e2e479fe8b8ec6c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingReader.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingReader.java?p=johnzon.git) [v baa4f3d47f79b048b5d473124e2e479fe8b8ec6c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingReader.java?rev=baa4f3d47f79b048b5d473124e2e479fe8b8ec6c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingWriter.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingWriter.java?p=johnzon.git) [v baa4f3d47f79b048b5d473124e2e479fe8b8ec6c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingWriter.java?rev=baa4f3d47f79b048b5d473124e2e479fe8b8ec6c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**Streams.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/Streams.java?p=johnzon.git) [v baa4f3d47f79b048b5d473124e2e479fe8b8ec6c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/Streams.java?rev=baa4f3d47f79b048b5d473124e2e479fe8b8ec6c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) Guard Mapper.write against null writer (#123) \* Expose anonymous classes to DelegatingX classes Applies the suggestions by @jungm and @rmannibucau \* Modify code style |
| 2024-03-17 18:45:07 | dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> | [johnzon-maven-plugin/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?p=johnzon.git) [v 3f600cfca70c75fd6447b83a14f39754d574b5f5](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?rev=3f600cfca70c75fd6447b83a14f39754d574b5f5&content-type=text/vnd.viewcvs-markup&p=johnzon.git) Bump org.apache.maven:maven-core in /johnzon-maven-plugin (#124) Bumps [org.apache.maven:maven-core](https://github.com/apache/maven) from 3.6.0 to 3.8.1. - [Release notes](https://github.com/apache/maven/releases) - [Commits](https://github.com/apache/maven/compare/[maven-3](http://jira.codehaus.org/browse/maven-3).6.0...[maven-3](http://jira.codehaus.org/browse/maven-3).8.1) --- updated-dependencies: - dependency-name: org.apache.maven:maven-core dependency-type: direct:production ... Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> |
| 2024-03-17 18:16:55 | dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> | [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?p=johnzon.git) [v eb2362aed4606fd7d8740fc750cafe79a1252c6c](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?rev=eb2362aed4606fd7d8740fc750cafe79a1252c6c&content-type=text/vnd.viewcvs-markup&p=johnzon.git) Bump h2 from 2.1.214 to 2.2.220 in /johnzon-mapper (#108) Bumps [h2](https://github.com/h2database/h2database) from 2.1.214 to 2.2.220. - [Release notes](https://github.com/h2database/h2database/releases) - [Commits](https://github.com/h2database/h2database/compare/[version-2](http://jira.codehaus.org/browse/version-2).1.214...[version-2](http://jira.codehaus.org/browse/version-2).2.220) --- updated-dependencies: - dependency-name: com.h2database:h2 dependency-type: direct:development ... Signed-off-by: dependabot[bot] <support@github.com> Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> |
| 2024-03-17 18:16:40 | Hervé Boutemy <hboutemy@apache.org> | [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?p=johnzon.git) [v 86acf0f57e0ccc23b571fffa5220e4dde816a389](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?rev=86acf0f57e0ccc23b571fffa5220e4dde816a389&content-type=text/vnd.viewcvs-markup&p=johnzon.git) upgrade Felix maven-bundle-plugin (#114) |

---

<a id="mailing-lists"></a>

<!-- source_url: https://johnzon.apache.org/mailing-lists.html -->

<!-- page_index: 5 -->

<a id="mailing-lists--project-mailing-lists"></a>

## Project Mailing Lists

These are the mailing lists that have been established for this project. For each list, there is a subscribe, unsubscribe, and an archive link.

| Name | Subscribe | Unsubscribe | Post | Archive | Other Archives |
| --- | --- | --- | --- | --- | --- |
| Johnzon Commits List | [Subscribe](mailto:commits-subscribe@johnzon.apache.org) | [Unsubscribe](mailto:commits-unsubscribe@johnzon.apache.org) | [Post](mailto:commits@johnzon.apache.org) | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/johnzon-commits/) | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/incubator-johnzon-commits/) |
|  |  |  |  |  | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/incubator-fleece-commits/) |
| Johnzon Developer List | [Subscribe](mailto:dev-subscribe@johnzon.apache.org) | [Unsubscribe](mailto:dev-unsubscribe@johnzon.apache.org) | [Post](mailto:dev@johnzon.apache.org) | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/johnzon-dev/) | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/incubator-johnzon-dev/) |
|  |  |  |  |  | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/incubator-fleece-dev/) |

---

<a id="archives-0.7-incubating"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/index.html -->

<!-- page_index: 6 -->

<a id="archives-0.7-incubating--apache-johnzon"></a>

# Apache johnzon

Apache Johnzon is a project providing an implementation of JsonProcessing (aka jsr-353) and a set of useful extension for this specification like an Object mapper and some JAX-RS providers.

Johnzon comes with three main modules.

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-core</artifactId>
  <version>0.8-incubating-SNAPSHOT</version>
</dependency>
```

This is the implementation of the specification. You’ll surely want to add the API as dependency too:

```

<dependency>
  <groupId>org.apache.geronimo.specs</groupId>
  <artifactId>geronimo-json_1.0_spec</artifactId>
  <version>1.0-alpha-1</version>
  <scope>provided</scope> <!-- or compile if your environment doesn't provide it -->
</dependency>
```

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-mapper</artifactId>
  <version>0.8-incubating-SNAPSHOT</version>
</dependency>
```

The mapper module allows you to use the implementation you want of Json Processing specification to map Json to Object and the opposite.

```

final MySuperObject object = createObject();

final Mapper mapper = new MapperBuilder().build();
mapper.writeObject(object, outputStream);

final MySuperObject otherObject = mapper.readObject(inputStream, MySuperObject.class);
```

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jaxrs</artifactId>
  <version>0.8-incubating-SNAPSHOT</version>
</dependency>
```

JAX-RS module provides two providers (and underlying MessageBodyReaders and MessageBodyWriters):

- org.apache.johnzon.jaxrs.JohnzonProvider: use Johnzon Mapper to map Object to Json and the opposite
- org.apache.johnzon.jaxrs.ConfigurableJohnzonProvider: same as JohnzonProvider but with setters to ease the configuration of the provider in most servers/containers
- org.apache.johnzon.jaxrs.JsrProvider: allows you to use JsrArray, JsrObject (more generally JsonStructure)

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-websocket</artifactId>
  <version>0.8-incubating-SNAPSHOT</version>
</dependency>
```

WebSocket module provides a basic integration with Java WebSocket API (JSR 356).

Integration is at codec level (encoder/decoder). There are two families of codecs:

- The ones based on JSON-P (JsonObject, JsonArray, JsonStructure)
- The ones based on Johnzon Mapper

Encoders:

- org.apache.johnzon.websocket.jsr.JsrObjectEncoder
- org.apache.johnzon.websocket.jsr.JsrArrayEncoder
- org.apache.johnzon.websocket.jsr.JsrStructureEncoder

Decoders:

- org.apache.johnzon.websocket.jsr.JsrObjectDecoder
- org.apache.johnzon.websocket.jsr.JsrArrayDecoder
- org.apache.johnzon.websocket.jsr.JsrStructureDecoder

Encoder:

- org.apache.johnzon.websocket.mapper.JohnzonTextEncoder

Decoder:

- org.apache.johnzon.websocket.mapper.JohnzonTextDecoder

On server and client side configuration is easy: just provide the encoders and decoders parameters to @[Server|Client]Endpoint (or EndpointConfig if you use programmatic API)):

```
@ClientEndpoint(encoders = JsrObjectEncoder.class, decoders = JsrObjectDecoder.class) public class JsrClientEndpointImpl {@OnMessage public void on(final JsonObject message) {// ...}}
@ServerEndpoint(value = "/my-server", encoders = JsrObjectEncoder.class, decoders = JsrObjectDecoder.class) public class JsrClientEndpointImpl {@OnMessage public void on(final JsonObject message) {// ...}}
```

Server configuration is as simple as providing encoders and decoders parameters to @ServerEndpoint:

```
@ServerEndpoint(value = "/server", encoders = JohnzonTextEncoder.class, decoders = JohnzonTextDecoder.class)
public class ServerEndpointImpl {
    @OnMessage
    public void on(final Session session, final Message message) {
        // ...
    }
}
```

Client configuration is almost the same excepted in this case it is not possible for Johnzon to guess the type you expect so you’ll need to provide it. In next sample it is done just extending JohnzonTextDecoder in MessageDecoder.

```
@ClientEndpoint(encoders = JohnzonTextEncoder.class, decoders = ClientEndpointImpl.MessageDecoder.class) public class ClientEndpointImpl {@OnMessage public void on(final Message message) {// ...}
public static class MessageDecoder extends JohnzonTextDecoder {public MessageDecoder() {super(Message.class);}}}
```

We would like to thank ej-technologies for their [Java profiler JProfiler](http://www.ej-technologies.com/products/jprofiler/overview.html) which helped us a lot optimizing memory footprint and speed. ![JProfiler](http://www.ej-technologies.com/images/banners/jprofiler_small.png)

---

<a id="archives-0.2-incubating"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/index.html -->

<!-- page_index: 7 -->

<a id="archives-0.2-incubating--apache-johnzon"></a>

# Apache johnzon

Apache Johnzon is a project providing an implementation of JsonProcessing (aka jsr-353) and a set of useful extension for this specification like an Object mapper and some JAX-RS providers.

<a id="archives-0.2-incubating--get-started"></a>

## Get started

Johnzon comes with three main modules.

<a id="archives-0.2-incubating--core"></a>

### Core

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-core</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This is the implementation of the specification. You’ll surely want to add the API as dependency too:

```

<dependency>
  <groupId>org.apache.geronimo.specs</groupId>
  <artifactId>geronimo-json_1.0_spec</artifactId>
  <version>${json-processing.version}</version>
  <scope>provided</scope> <!-- or compile if your environment doesn't provide it -->
</dependency>
```

<a id="archives-0.2-incubating--mapper"></a>

### Mapper

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-mapper</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

The mapper module allows you to use the implementation you want of Json Processing specification to map Json to Object and the opposite.

```

final MySuperObject object = createObject();

final Mapper mapper = new MapperBuilder().build();
mapper.writeObject(object, outputStream);

final MySuperObject otherObject = mapper.readObject(inputStream, MySuperObject.class);
```

<a id="archives-0.2-incubating--jax-rs"></a>

### JAX-RS

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jaxrs</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

JAX-RS module provides two providers (and underlying MessageBodyReaders and MessageBodyWriters):

- org.apache.johnzon.jaxrs.JohnzonProvider: use Johnzon Mapper to map Object to Json and the opposite
- org.apache.johnzon.jaxrs.ConfigurableJohnzonProvider: same as JohnzonProvider but with setters to ease the configuration of the provider in most servers/containers
- org.apache.johnzon.jaxrs.JsrProvider: allows you to use JsrArray, JsrObject (more generally JsonStructure)

<a id="archives-0.2-incubating--thanks"></a>

## Thanks

We would like to thank ej-technologies for their [Java profiler JProfiler](http://www.ej-technologies.com/products/jprofiler/overview.html) which helped us a lot optimizing memory footprint and speed. ![JProfiler](http://www.ej-technologies.com/images/banners/jprofiler_small.png)

---

<a id="archives-0.1-incubating"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.1-incubating/index.html -->

<!-- page_index: 8 -->

<a id="archives-0.1-incubating--apache-johnzon"></a>

# Apache johnzon

Apache Johnzon is a project providing an implementation of JsonProcessing (aka jsr-353) and a set of useful extension for this specification like an Object mapper and some JAX-RS providers.

<a id="archives-0.1-incubating--get-started"></a>

## Get started

Johnzon comes with three main modules.

<a id="archives-0.1-incubating--core"></a>

### Core

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-core</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

This is the implementation of the specification. You’ll surely want to add the API as dependency too:

```

<dependency>
  <groupId>org.apache.geronimo.specs</groupId>
  <artifactId>geronimo-json_1.0_spec</artifactId>
  <version>${json-processing.version}</version>
  <scope>provided</scope> <!-- or compile if your environment doesn't provide it -->
</dependency>
```

<a id="archives-0.1-incubating--mapper"></a>

### Mapper

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-mapper</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

The mapper module allows you to use the implementation you want of Json Processing specification to map Json to Object and the opposite.

```

final MySuperObject object = createObject();

final Mapper mapper = new MapperBuilder().build();
mapper.writeObject(object, outputStream);

final MySuperObject otherObject = mapper.readObject(inputStream, MySuperObject.class);
```

<a id="archives-0.1-incubating--jax-rs"></a>

### JAX-RS

```

<dependency>
  <groupId>org.apache.johnzon</groupId>
  <artifactId>johnzon-jaxrs</artifactId>
  <version>${johnzon.version}</version>
</dependency>
```

JAX-RS module provides two providers (and underlying MessageBodyReaders and MessageBodyWriters):

- org.apache.johnzon.jaxrs.JohnzonProvider.JohnzonProvider: use Johnzon Mapper to map Object to Json and the opposite
- org.apache.johnzon.jaxrs.JsrProvider: allows you to use JsrArray, JsrObject (more generally JsonStructure)

---

<a id="project-info"></a>

<!-- source_url: https://johnzon.apache.org/project-info.html -->

<!-- page_index: 9 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Dependencies](https://johnzon.apache.org/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://johnzon.apache.org/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [Dependency Information](https://johnzon.apache.org/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://johnzon.apache.org/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Distribution Management](https://johnzon.apache.org/distribution-management.html) | This document provides informations on the distribution management of this project. |
| [About](#index) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Issue Management](https://johnzon.apache.org/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Licenses](https://johnzon.apache.org/licenses.html) | This document lists the project license(s). |
| [Mailing Lists](#mailing-lists) | This document provides subscription and archive information for this project's mailing lists. |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Plugin Management](https://johnzon.apache.org/plugin-management.html) | This document lists the plugins that are defined through pluginManagement. |
| [Plugins](https://johnzon.apache.org/plugins.html) | This document lists the build plugins and the report plugins used by this project. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |

---

<a id="ci-management"></a>

<!-- source_url: https://johnzon.apache.org/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [Jenkins](https://www.jenkins.io/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://builds.apache.org/job/johnzon/
```

<a id="ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="modules"></a>

<!-- source_url: https://johnzon.apache.org/modules.html -->

<!-- page_index: 11 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Johnzon :: Core](https://johnzon.apache.org/johnzon-core/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Mapper](https://johnzon.apache.org/johnzon-mapper/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JAX-RS](https://johnzon.apache.org/johnzon-jaxrs/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Distribution](https://johnzon.apache.org/apache-johnzon/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Maven Plugin](https://johnzon.apache.org/johnzon-maven-plugin/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: WebSocket](https://johnzon.apache.org/johnzon-websocket/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JSON-B Implementation](https://johnzon.apache.org/johnzon-jsonb/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JSON-B Extensions](https://johnzon.apache.org/johnzon-jsonb-extras/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JSON Schema](https://johnzon.apache.org/johnzon-jsonschema/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Support for OSGI Jaxrs Whiteboard](https://johnzon.apache.org/johnzon-osgi/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JSON Logic](https://johnzon.apache.org/johnzon-jsonlogic/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |

---

<a id="summary"></a>

<!-- source_url: https://johnzon.apache.org/summary.html -->

<!-- page_index: 12 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Johnzon |
| Description | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| Homepage | [https://johnzon.apache.org](#index) |

<a id="summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.johnzon |
| ArtifactId | johnzon |
| Version | 2.0.2-SNAPSHOT |
| Type | pom |

---

<a id="team"></a>

<!-- source_url: https://johnzon.apache.org/team.html -->

<!-- page_index: 13 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Roles |
| --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/69cba8fe866d6fa5cab1f001eae7cd14?d=mm&s=60) | jmclean | Justin Mclean | [jmclean AT apache.org](mailto:jmclean AT apache.org) | Mentor |
| ![](https://www.gravatar.com/avatar/a1efc4e0c2b99e0e61d8472419ea1bcc?d=mm&s=60) | grobmeier | Christian Grobmeier | [grobmeier AT apache.org](mailto:grobmeier AT apache.org) | - |
| ![](https://www.gravatar.com/avatar/16efdbd7a08c98658caf9d1aba7f2c3d?d=mm&s=60) | dkulp | Daniel Kulp | [dkulp AT apache.org](mailto:dkulp AT apache.org) | Mentor |
| ![](https://www.gravatar.com/avatar/c3ef61edda56f280571e691eacb3be95?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau AT apache.org](mailto:rmannibucau AT apache.org) | PMC |
| ![](https://www.gravatar.com/avatar/8a67544f497bc5e0d8cd345841844c67?d=mm&s=60) | jlmonteiro | Jean-Louis Monteiro | [jlmonteiro AT apache.org](mailto:jlmonteiro AT apache.org) | PMC |
| ![](https://www.gravatar.com/avatar/5addda66a07702e0a84087e049bf1f81?d=mm&s=60) | struberg | Mark Struberg | [struberg AT apache.org](mailto:struberg AT apache.org) | PMC |
| ![](https://www.gravatar.com/avatar/a70c5391084b90d43d52353c848f8fe5?d=mm&s=60) | rsandtner | Reinhard Sandtner | [rsandtner AT apache.org](mailto:rsandtner AT apache.org) | PMC |
| ![](https://www.gravatar.com/avatar/364183ba68e8b5bd78bab1c353ebb335?d=mm&s=60) | dblevins | David Blevins | [dblevins AT apache.org](mailto:dblevins AT apache.org) | PMC |
| ![](https://www.gravatar.com/avatar/95188e8922f201996273ca9b450b1977?d=mm&s=60) | sagara | Sagara Gunathunga | [sagara AT apache.org](mailto:sagara AT apache.org) | - |
| ![](http://www.gravatar.com/avatar/af23e69dbed585db0ce6445d0adb4985.png) | salyh | Hendrik Saly | [salyh AT apache.org](mailto:salyh AT apache.org) | PMC |
| ![](https://www.gravatar.com/avatar/4d398cca06964961b358d561ef7db943?d=mm&s=60) | jungm | Markus Jung | [jungm AT apache.org](mailto:jungm AT apache.org) | - |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Thiago Veronezi

Karl Grosse

---

<a id="archives-0.1-incubating-issue-tracking"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.1-incubating/issue-tracking.html -->

<!-- page_index: 14 -->

<a id="archives-0.1-incubating-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="archives-0.1-incubating-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/JOHNZON
```

---

<a id="archives-0.1-incubating-integration"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.1-incubating/integration.html -->

<!-- page_index: 15 -->

<a id="archives-0.1-incubating-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="archives-0.1-incubating-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/johnzon/
```

<a id="archives-0.1-incubating-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="archives-0.1-incubating-project-summary"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.1-incubating/project-summary.html -->

<!-- page_index: 16 -->

<a id="archives-0.1-incubating-project-summary--project-summary"></a>

## Project Summary

<a id="archives-0.1-incubating-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Johnzon |
| Description | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| Homepage | <http://incubator.apache.org/projects/johnzon.html> |

<a id="archives-0.1-incubating-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="archives-0.1-incubating-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.johnzon |
| ArtifactId | johnzon |
| Version | 0.1-incubating |
| Type | pom |

---

<a id="dependency-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/dependency-updates-report.html -->

<!-- page_index: 17 -->

<a id="dependency-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various dependencies.

| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of dependencies using the latest version available | 2 |
| --- | --- | --- |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of dependencies where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of dependencies where the next version available is an incremental version update | 2 |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of dependencies where the next version available is a minor version update | 0 |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of dependencies where the next version available is a major version update | 0 |

<a id="dependency-updates-report--dependency-management"></a>

### Dependency Management

| Status | Group Id | Artifact Id | Current Version | Scope | Classifier | Type | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | jakarta.json | jakarta.json-api | 2.1.1 | provided |  | jar |  | **2.1.3** |  |  |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | jakarta.json.bind | jakarta.json.bind-api | 3.0.0 | provided |  | jar |  |  |  |  |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | junit | junit | 4.13.2 | test |  | jar |  |  |  |  |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugin-tools | maven-plugin-annotations | 3.7.0 |  |  | jar |  | **3.7.1** | **3.11.0** |  |
| Status | Group Id | Artifact Id | Current Version | Scope | Classifier | Type | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major |

<a id="dependency-updates-report--dependencies"></a>

### Dependencies

This project does not declare any dependencies.

<a id="dependency-updates-report--dependency-updates"></a>

## Dependency Updates

<a id="dependency-updates-report--jakarta.json:jakarta.json-api"></a>

### jakarta.json:jakarta.json-api

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | jakarta.json |
| Artifact Id | jakarta.json-api |
| Current Version | 2.1.1 |
| Scope | provided |
| Classifier |  |
| Type | jar |
| Newer versions | 2.1.2 **2.1.3** *Latest Incremental* |

<a id="dependency-updates-report--jakarta.json.bind:jakarta.json.bind-api"></a>

### jakarta.json.bind:jakarta.json.bind-api

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | jakarta.json.bind |
| Artifact Id | jakarta.json.bind-api |
| Current Version | 3.0.0 |
| Scope | provided |
| Classifier |  |
| Type | jar |

<a id="dependency-updates-report--junit:junit"></a>

### junit:junit

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | junit |
| Artifact Id | junit |
| Current Version | 4.13.2 |
| Scope | test |
| Classifier |  |
| Type | jar |

<a id="dependency-updates-report--org.apache.maven.plugin-tools:maven-plugin-annotations"></a>

### org.apache.maven.plugin-tools:maven-plugin-annotations

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugin-tools |
| Artifact Id | maven-plugin-annotations |
| Current Version | 3.7.0 |
| Scope |  |
| Classifier |  |
| Type | jar |
| Newer versions | **3.7.1** *Latest Incremental* 3.8.1 3.8.2 3.9.0 3.10.1 3.10.2 **3.11.0** *Latest Minor* |

---

<a id="plugin-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/plugin-updates-report.html -->

<!-- page_index: 18 -->

<a id="plugin-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various plugins.

| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of plugins using the latest version available | 9 |
| --- | --- | --- |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of plugins where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of plugins where the next version available is an incremental version update | 7 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of plugins where the next version available is a minor version update | 17 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of plugins where the next version available is a major version update | 6 |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of plugins where a dependencies section containes a dependency with an updated version | 0 |

<a id="plugin-updates-report--plugin-management"></a>

### Plugin Management

| Status | Group Id | Artifact Id | Current Version | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | com.github.spotbugs | spotbugs-maven-plugin | 3.1.12.2 |  |  |  | **4.8.3.1** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.felix | maven-bundle-plugin | **5.1.9** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-antrun-plugin | **3.1.0** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-assembly-plugin | 3.4.2 |  |  | **3.7.1** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-changelog-plugin | **2.3** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-changes-plugin | **2.12.1** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-checkstyle-plugin | 3.0.0 |  |  | **3.3.1** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-clean-plugin | 3.2.0 |  |  | **3.3.2** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-compiler-plugin | 3.11.0 |  |  | **3.13.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-dependency-plugin | 3.4.0 |  |  | **3.6.1** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-deploy-plugin | 2.8.2 |  |  |  | **3.1.1** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-ear-plugin | **3.3.0** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-enforcer-plugin | 3.4.0 |  | **3.4.1** |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-failsafe-plugin | 2.22.2 |  |  |  | **3.2.5** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-gpg-plugin | 3.0.1 |  |  | **3.2.2** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-help-plugin | 3.3.0 |  |  | **3.4.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-install-plugin | 3.1.0 |  | **3.1.1** |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-invoker-plugin | 3.3.0 |  |  | **3.6.1** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-jar-plugin | **3.3.0** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-javadoc-plugin | **3.6.3** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-plugin-plugin | 3.7.0 |  | **3.7.1** | **3.11.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-plugin-report-plugin | 3.7.0 |  | **3.7.1** | **3.11.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-pmd-plugin | 3.21.0 |  | **3.21.2** |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-project-info-reports-plugin | 3.4.5 |  |  | **3.5.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.apache.maven.plugins | maven-release-plugin | **3.0.1** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-remote-resources-plugin | 1.7.0 |  |  |  | **3.2.0** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-resources-plugin | 3.3.0 |  | **3.3.1** |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-scm-plugin | 1.13.0 |  |  |  | **2.0.1** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-scm-publish-plugin | 3.1.0 |  |  | **3.2.1** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-shade-plugin | 3.4.1 |  |  | **3.5.2** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-site-plugin | 3.12.1 |  |  |  | **4.0.0-M13** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-source-plugin | 3.2.1 |  |  | **3.3.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-surefire-plugin | 3.1.2 |  |  | **3.2.5** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-surefire-report-plugin | 3.1.2 |  |  | **3.2.5** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.maven.plugins | maven-war-plugin | 3.3.2 |  |  | **3.4.0** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.apache.rat | apache-rat-plugin | 0.15 |  |  | **0.16.1** |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | org.codehaus.mojo | taglist-maven-plugin | **3.0.0** |  |  |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.codehaus.mojo | versions-maven-plugin | 2.16.0 |  | **2.16.2** |  |  | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| Status | Group Id | Artifact Id | Current Version | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major | Dependency status |

<a id="plugin-updates-report--plugins"></a>

### Plugins

| Status | Group Id | Artifact Id | Current Version | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | org.eluder.coveralls | coveralls-maven-plugin | 3.0.1 |  |  | **3.2.1** | **4.3.0** | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) |
| Status | Group Id | Artifact Id | Current Version | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major | Dependency status |

<a id="plugin-updates-report--plugin-updates"></a>

## Plugin Updates

<a id="plugin-updates-report--plugin-com.github.spotbugs:spotbugs-maven-plugin"></a>

### Plugin com.github.spotbugs:spotbugs-maven-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Group Id | com.github.spotbugs |
| Artifact Id | spotbugs-maven-plugin |
| Current Version | 3.1.12.2 |
| Newer versions | 4.0.0 4.0.4 4.1.3 4.1.4 4.2.0 4.2.2 4.2.3 4.3.0 4.4.1 4.4.2 4.4.2.1 4.4.2.2 4.5.0.0 4.5.2.0 4.5.3.0 4.6.0.0 4.7.0.0 4.7.1.0 4.7.1.1 4.7.2.0 4.7.2.1 4.7.2.2 4.7.3.0 4.7.3.1 4.7.3.2 4.7.3.3 4.7.3.4 4.7.3.5 4.7.3.6 4.8.0.0 4.8.1.0 4.8.2.0 4.8.3.0 **4.8.3.1** *Latest Major* |

<a id="plugin-updates-report--plugin-org.apache.felix:maven-bundle-plugin"></a>

### Plugin org.apache.felix:maven-bundle-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.felix |
| Artifact Id | maven-bundle-plugin |
| Current Version | 5.1.9 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-antrun-plugin"></a>

### Plugin org.apache.maven.plugins:maven-antrun-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-antrun-plugin |
| Current Version | 3.1.0 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-assembly-plugin"></a>

### Plugin org.apache.maven.plugins:maven-assembly-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-assembly-plugin |
| Current Version | 3.4.2 |
| Newer versions | 3.5.0 3.6.0 3.7.0 **3.7.1** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-changelog-plugin"></a>

### Plugin org.apache.maven.plugins:maven-changelog-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-changelog-plugin |
| Current Version | 2.3 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-changes-plugin"></a>

### Plugin org.apache.maven.plugins:maven-changes-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-changes-plugin |
| Current Version | 2.12.1 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-checkstyle-plugin"></a>

### Plugin org.apache.maven.plugins:maven-checkstyle-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-checkstyle-plugin |
| Current Version | 3.0.0 |
| Newer versions | 3.1.0 3.1.1 3.1.2 3.2.0 3.2.1 3.2.2 3.3.0 **3.3.1** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-clean-plugin"></a>

### Plugin org.apache.maven.plugins:maven-clean-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-clean-plugin |
| Current Version | 3.2.0 |
| Newer versions | 3.3.1 **3.3.2** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-compiler-plugin"></a>

### Plugin org.apache.maven.plugins:maven-compiler-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-compiler-plugin |
| Current Version | 3.11.0 |
| Newer versions | 3.12.0 3.12.1 **3.13.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-dependency-plugin"></a>

### Plugin org.apache.maven.plugins:maven-dependency-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-dependency-plugin |
| Current Version | 3.4.0 |
| Newer versions | 3.5.0 3.6.0 **3.6.1** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-deploy-plugin"></a>

### Plugin org.apache.maven.plugins:maven-deploy-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-deploy-plugin |
| Current Version | 2.8.2 |
| Newer versions | 3.0.0-M1 3.0.0-M2 3.0.0 3.1.0 **3.1.1** *Latest Major* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-ear-plugin"></a>

### Plugin org.apache.maven.plugins:maven-ear-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-ear-plugin |
| Current Version | 3.3.0 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-enforcer-plugin"></a>

### Plugin org.apache.maven.plugins:maven-enforcer-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-enforcer-plugin |
| Current Version | 3.4.0 |
| Newer versions | **3.4.1** *Latest Incremental* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-failsafe-plugin"></a>

### Plugin org.apache.maven.plugins:maven-failsafe-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-failsafe-plugin |
| Current Version | 2.22.2 |
| Newer versions | 3.0.0-M1 3.0.0-M2 3.0.0-M3 3.0.0-M4 3.0.0-M5 3.0.0-M6 3.0.0-M7 3.0.0-M8 3.0.0-M9 3.0.0 3.1.0 3.1.2 3.2.1 3.2.2 3.2.3 **3.2.5** *Latest Major* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-gpg-plugin"></a>

### Plugin org.apache.maven.plugins:maven-gpg-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-gpg-plugin |
| Current Version | 3.0.1 |
| Newer versions | 3.1.0 3.2.0 3.2.1 **3.2.2** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-help-plugin"></a>

### Plugin org.apache.maven.plugins:maven-help-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-help-plugin |
| Current Version | 3.3.0 |
| Newer versions | **3.4.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-install-plugin"></a>

### Plugin org.apache.maven.plugins:maven-install-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-install-plugin |
| Current Version | 3.1.0 |
| Newer versions | **3.1.1** *Latest Incremental* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-invoker-plugin"></a>

### Plugin org.apache.maven.plugins:maven-invoker-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-invoker-plugin |
| Current Version | 3.3.0 |
| Newer versions | 3.4.0 3.5.0 3.5.1 3.6.0 **3.6.1** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-jar-plugin"></a>

### Plugin org.apache.maven.plugins:maven-jar-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-jar-plugin |
| Current Version | 3.3.0 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-javadoc-plugin"></a>

### Plugin org.apache.maven.plugins:maven-javadoc-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-javadoc-plugin |
| Current Version | 3.6.3 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-plugin-plugin"></a>

### Plugin org.apache.maven.plugins:maven-plugin-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-plugin-plugin |
| Current Version | 3.7.0 |
| Newer versions | **3.7.1** *Latest Incremental* 3.8.1 3.8.2 3.9.0 3.10.1 3.10.2 **3.11.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-plugin-report-plugin"></a>

### Plugin org.apache.maven.plugins:maven-plugin-report-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-plugin-report-plugin |
| Current Version | 3.7.0 |
| Newer versions | **3.7.1** *Latest Incremental* 3.8.1 3.8.2 3.9.0 3.10.1 3.10.2 **3.11.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-pmd-plugin"></a>

### Plugin org.apache.maven.plugins:maven-pmd-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-pmd-plugin |
| Current Version | 3.21.0 |
| Newer versions | **3.21.2** *Latest Incremental* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-project-info-reports-plugin"></a>

### Plugin org.apache.maven.plugins:maven-project-info-reports-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-project-info-reports-plugin |
| Current Version | 3.4.5 |
| Newer versions | **3.5.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-release-plugin"></a>

### Plugin org.apache.maven.plugins:maven-release-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-release-plugin |
| Current Version | 3.0.1 |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-remote-resources-plugin"></a>

### Plugin org.apache.maven.plugins:maven-remote-resources-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-remote-resources-plugin |
| Current Version | 1.7.0 |
| Newer versions | 3.0.0 3.1.0 **3.2.0** *Latest Major* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-resources-plugin"></a>

### Plugin org.apache.maven.plugins:maven-resources-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-resources-plugin |
| Current Version | 3.3.0 |
| Newer versions | **3.3.1** *Latest Incremental* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-scm-plugin"></a>

### Plugin org.apache.maven.plugins:maven-scm-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-scm-plugin |
| Current Version | 1.13.0 |
| Newer versions | 2.0.0-M1 2.0.0-M2 2.0.0-M3 2.0.0 **2.0.1** *Latest Major* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-scm-publish-plugin"></a>

### Plugin org.apache.maven.plugins:maven-scm-publish-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-scm-publish-plugin |
| Current Version | 3.1.0 |
| Newer versions | **3.2.1** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-shade-plugin"></a>

### Plugin org.apache.maven.plugins:maven-shade-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-shade-plugin |
| Current Version | 3.4.1 |
| Newer versions | 3.5.0 3.5.1 **3.5.2** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-site-plugin"></a>

### Plugin org.apache.maven.plugins:maven-site-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-site-plugin |
| Current Version | 3.12.1 |
| Newer versions | 4.0.0-M1 4.0.0-M2 4.0.0-M3 4.0.0-M4 4.0.0-M5 4.0.0-M6 4.0.0-M7 4.0.0-M8 4.0.0-M9 4.0.0-M10 4.0.0-M11 4.0.0-M12 **4.0.0-M13** *Latest Major* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-source-plugin"></a>

### Plugin org.apache.maven.plugins:maven-source-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-source-plugin |
| Current Version | 3.2.1 |
| Newer versions | **3.3.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-surefire-plugin"></a>

### Plugin org.apache.maven.plugins:maven-surefire-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-surefire-plugin |
| Current Version | 3.1.2 |
| Newer versions | 3.2.1 3.2.2 3.2.3 **3.2.5** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-surefire-report-plugin"></a>

### Plugin org.apache.maven.plugins:maven-surefire-report-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-surefire-report-plugin |
| Current Version | 3.1.2 |
| Newer versions | 3.2.1 3.2.2 3.2.3 **3.2.5** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.maven.plugins:maven-war-plugin"></a>

### Plugin org.apache.maven.plugins:maven-war-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-war-plugin |
| Current Version | 3.3.2 |
| Newer versions | **3.4.0** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.apache.rat:apache-rat-plugin"></a>

### Plugin org.apache.rat:apache-rat-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.rat |
| Artifact Id | apache-rat-plugin |
| Current Version | 0.15 |
| Newer versions | 0.16 **0.16.1** *Latest Minor* |

<a id="plugin-updates-report--plugin-org.codehaus.mojo:taglist-maven-plugin"></a>

### Plugin org.codehaus.mojo:taglist-maven-plugin

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Group Id | org.codehaus.mojo |
| Artifact Id | taglist-maven-plugin |
| Current Version | 3.0.0 |

<a id="plugin-updates-report--plugin-org.codehaus.mojo:versions-maven-plugin"></a>

### Plugin org.codehaus.mojo:versions-maven-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | org.codehaus.mojo |
| Artifact Id | versions-maven-plugin |
| Current Version | 2.16.0 |
| Newer versions | 2.16.1 **2.16.2** *Latest Incremental* |

<a id="plugin-updates-report--plugin-org.eluder.coveralls:coveralls-maven-plugin"></a>

### Plugin org.eluder.coveralls:coveralls-maven-plugin

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.eluder.coveralls |
| Artifact Id | coveralls-maven-plugin |
| Current Version | 3.0.1 |
| Newer versions | 3.1.0 3.2.0 **3.2.1** *Latest Minor* 4.0.0 4.1.0 4.2.0 **4.3.0** *Latest Major* |

---

<a id="property-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/property-updates-report.html -->

<!-- page_index: 19 -->

<a id="property-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various properties associated with artifacts.

| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of properties using the latest version available | 2 |
| --- | --- | --- |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | # of properties where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of properties where the next version available is an incremental version update | 2 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of properties where the next version available is a minor version update | 2 |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | # of properties where the next version available is a major version update | 1 |

<a id="property-updates-report--summary-of-properties-associated-with-artifact-versions"></a>

### Summary of properties associated with artifact versions

| Status | Property | Current Version | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major |
| --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | ${bnd.version} | 6.1.0 |  |  | **6.4.1** | **7.0.0** |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | ${checkstyle.version} | 3.0.0 |  |  | **3.3.1** |  |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | ${felix.plugin.version} | 5.1.9 |  |  |  |  |
| ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) | ${jakarta-jsonb-api.version} | 3.0.0 |  |  |  |  |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | ${jakarta-jsonp-api.version} | 2.1.1 |  | **2.1.3** |  |  |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | ${maven.plugin.tools.version} | 3.7.0 |  | **3.7.1** | **3.11.0** |  |
| ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) | ${surefire.version} | 2.22.2 |  |  |  | **3.2.5** |
| Status | Property | Current Version | Latest Subincremental | Latest Incremental | Latest Minor | Latest Major |

<a id="property-updates-report--properties-associated-with-artifact-versions"></a>

## Properties associated with artifact versions

<a id="property-updates-report--bnd.version"></a>

### ${bnd.version}

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Property | ${bnd.version} |
| Associated artifacts | biz.aQute.bnd:biz.aQute.bndlib |
| Current Version | 6.1.0 |
| Newer versions | 6.2.0 6.3.0 6.3.1 6.4.0 **6.4.1** *Latest Minor* **7.0.0** *Latest Major* |
| Allowed version range | 6.1.0 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

<a id="property-updates-report--checkstyle.version"></a>

### ${checkstyle.version}

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Property | ${checkstyle.version} |
| Associated artifacts | org.apache.maven.plugins:maven-checkstyle-plugin |
| Current Version | 3.0.0 |
| Newer versions | 3.1.0 3.1.1 3.1.2 3.2.0 3.2.1 3.2.2 3.3.0 **3.3.1** *Latest Minor* |
| Allowed version range | 3.0.0 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

<a id="property-updates-report--felix.plugin.version"></a>

### ${felix.plugin.version}

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Property | ${felix.plugin.version} |
| Associated artifacts | org.apache.felix:maven-bundle-plugin |
| Current Version | 5.1.9 |
| Allowed version range | 5.1.9 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

<a id="property-updates-report--jakarta-jsonb-api.version"></a>

### ${jakarta-jsonb-api.version}

| Status | ![](assets/images/icon-success-sml_e7a3ea5b595cee69.gif) No newer versions available. |
| --- | --- |
| Property | ${jakarta-jsonb-api.version} |
| Associated artifacts | jakarta.json.bind:jakarta.json.bind-api |
| Current Version | 3.0.0 |
| Allowed version range | 3.0.0 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

<a id="property-updates-report--jakarta-jsonp-api.version"></a>

### ${jakarta-jsonp-api.version}

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Property | ${jakarta-jsonp-api.version} |
| Associated artifacts | jakarta.json:jakarta.json-api |
| Current Version | 2.1.1 |
| Newer versions | 2.1.2 **2.1.3** *Latest Incremental* |
| Allowed version range | 2.1.1 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

<a id="property-updates-report--maven.plugin.tools.version"></a>

### ${maven.plugin.tools.version}

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Property | ${maven.plugin.tools.version} |
| Associated artifacts | org.apache.maven.plugin-tools:maven-plugin-annotations org.apache.maven.plugins:maven-plugin-plugin org.apache.maven.plugins:maven-plugin-report-plugin |
| Current Version | 3.7.0 |
| Newer versions | **3.7.1** *Latest Incremental* 3.8.1 3.8.2 3.9.0 3.10.1 3.10.2 **3.11.0** *Latest Minor* |
| Allowed version range | 3.7.0 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

<a id="property-updates-report--surefire.version"></a>

### ${surefire.version}

| Status | ![](assets/images/icon-warning-sml_e45f474902ecfd9b.gif) There is at least one newer major version available. Major updates are rarely passive. |
| --- | --- |
| Property | ${surefire.version} |
| Associated artifacts | org.apache.maven.plugins:maven-failsafe-plugin org.apache.maven.plugins:maven-surefire-plugin org.apache.maven.plugins:maven-surefire-report-plugin |
| Current Version | 2.22.2 |
| Newer versions | 3.0.0-M1 3.0.0-M2 3.0.0-M3 3.0.0-M4 3.0.0-M5 3.0.0-M6 3.0.0-M7 3.0.0-M8 3.0.0-M9 3.0.0 3.1.0 3.1.2 3.2.1 3.2.2 3.2.3 **3.2.5** *Latest Major* |
| Allowed version range | 2.22.2 |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

---

<a id="file-activity"></a>

<!-- source_url: https://johnzon.apache.org/file-activity.html -->

<!-- page_index: 20 -->

<a id="file-activity--file-activity-report"></a>

## File Activity Report

<a id="file-activity--changes-between-02-mar-2024-and-02-apr-2024"></a>

### Changes between 02 Mar, 2024 and 02 Apr, 2024

Total commits: 8 Total number of files changed: 19

| Filename | Number of Times Changed |
| --- | --- |
| [johnzon-maven-plugin/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-maven-plugin/pom.xml?p=johnzon.git) | 3 |
| [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/pom.xml?p=johnzon.git) | 3 |
| [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/pom.xml?p=johnzon.git) | 3 |
| [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-core/pom.xml?p=johnzon.git) | 2 |
| [johnzon-distribution/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-distribution/pom.xml?p=johnzon.git) | 2 |
| [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jaxrs/pom.xml?p=johnzon.git) | 2 |
| [johnzon-json-extras/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-json-extras/pom.xml?p=johnzon.git) | 2 |
| [johnzon-jsonb/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonb/pom.xml?p=johnzon.git) | 2 |
| [johnzon-jsonlogic/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonlogic/pom.xml?p=johnzon.git) | 2 |
| [johnzon-jsonschema/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-jsonschema/pom.xml?p=johnzon.git) | 2 |
| [johnzon-osgi/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-osgi/pom.xml?p=johnzon.git) | 2 |
| [johnzon-websocket/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-websocket/pom.xml?p=johnzon.git) | 2 |
| [src/site/markdown/**download.md**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/src/site/markdown/download.md?p=johnzon.git) | 1 |
| [**KEYS**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/KEYS?p=johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingInputStream.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingInputStream.java?p=johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingOutputStream.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingOutputStream.java?p=johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingReader.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingReader.java?p=johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**DelegatingWriter.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/DelegatingWriter.java?p=johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/**Streams.java**](https://git-wip-us.apache.org/repos/asf?p=johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/internal/Streams.java?p=johnzon.git) | 1 |

---

<a id="dev-activity"></a>

<!-- source_url: https://johnzon.apache.org/dev-activity.html -->

<!-- page_index: 21 -->

<a id="dev-activity--developer-activity-report"></a>

## Developer Activity Report

<a id="dev-activity--changes-between-02-mar-2024-and-02-apr-2024"></a>

### Changes between 02 Mar, 2024 and 02 Apr, 2024

Total commits: 8 Total number of files changed: 19

| Developer | Total commits | Total Number of Files Changed |
| --- | --- | --- |
| Hervé Boutemy <hboutemy@apache.org> | 1 | 1 |
| Markus Jung <jungm@apache.org> | 4 | 14 |
| dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> | 2 | 2 |
| Heewon Lee <94441510+pingpingy1@users.noreply.github.com> | 1 | 5 |

---

<a id="security"></a>

<!-- source_url: https://johnzon.apache.org/security.html -->

<!-- page_index: 22 -->

<a id="security--reporting-new-security-problems-with-apache-johnzon"></a>

# Reporting New Security Problems with Apache Johnzon

The Apache Software Foundation takes a very active stance in eliminating security problems and denial of service attacks against Apache projects.

We strongly encourage folks to report such problems to the [private security mailing list](http://www.apache.org/security/) first, before disclosing them in a public forum.

Please note that the security mailing list should only be used for reporting undisclosed security vulnerabilities in Apache projects and managing the process of fixing such vulnerabilities.
We cannot accept regular bug reports or other queries at this address. All mail sent to this address that does not relate to an undisclosed security problem will be ignored.

If you need to report a bug that isn't an undisclosed security vulnerability, please use the [bug reporting](https://issues.apache.org/jira/browse/JOHNZON) system.

###Questions about:

- how to configure Johnzon securely
- if a vulnerability applies to your particular application
- obtaining further information on a published vulnerability
- availability of patches and/or new releases

should be addressed to the [mailing list](http://johnzon.apache.org/mail-lists.html).

The private security mailing address is: security (at) apache (dot) org

<a id="security--biginteger-and-java"></a>

## BigInteger and Java

JSON-P/JSON-B exposes API using `BigDecimal` and `BigInteger`.
The bridge between these two types is `BigDecimal#toBigInteger` which has a slow implementation in Java without careness or scale max validation.

Johnzon does some sanity checks on this value but at some point we recommend you to stay away from these API and handle big numbers using `String` type and parse them yourself since you are the only ones knowing the correct functional and relevant validation of the scale before a instantiation.

If you know you don't need such big types, prefer using plain primitives (or wrappers).

---

<a id="archives-0.2-incubating-issue-tracking"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/issue-tracking.html -->

<!-- page_index: 23 -->

<a id="archives-0.2-incubating-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="archives-0.2-incubating-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/JOHNZON
```

---

<a id="archives-0.2-incubating-integration"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/integration.html -->

<!-- page_index: 24 -->

<a id="archives-0.2-incubating-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="archives-0.2-incubating-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/johnzon/
```

<a id="archives-0.2-incubating-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="archives-0.2-incubating-modules"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/modules.html -->

<!-- page_index: 25 -->

<a id="archives-0.2-incubating-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Johnzon :: Core](https://johnzon.apache.org/archives/0.2-incubating/johnzon-core/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Mapper](https://johnzon.apache.org/archives/0.2-incubating/johnzon-mapper/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JAX-RS](https://johnzon.apache.org/archives/0.2-incubating/johnzon-jaxrs/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |

---

<a id="archives-0.2-incubating-project-summary"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/project-summary.html -->

<!-- page_index: 26 -->

<a id="archives-0.2-incubating-project-summary--project-summary"></a>

## Project Summary

<a id="archives-0.2-incubating-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Johnzon |
| Description | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| Homepage | <http://incubator.apache.org/projects/johnzon.html> |

<a id="archives-0.2-incubating-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="archives-0.2-incubating-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.johnzon |
| ArtifactId | johnzon |
| Version | 0.2-incubating |
| Type | pom |

---

<a id="archives-0.2-incubating-dependency-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/dependency-updates-report.html -->

<!-- page_index: 27 -->

<a id="archives-0.2-incubating-dependency-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various dependencies.

| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | # of dependencies using the latest version available | 1 |
| --- | --- | --- |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of dependencies where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of dependencies where the next version available is an incremental version update | 1 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of dependencies where the next version available is a minor version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of dependencies where the next version available is a major version update | 0 |

<a id="archives-0.2-incubating-dependency-updates-report--dependency-management"></a>

### Dependency Management

This project does not declare any dependencies in a dependencyManagement section.

<a id="archives-0.2-incubating-dependency-updates-report--dependencies"></a>

### Dependencies

| Status | Group Id | Artifact Id | Current Version | Scope | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | junit | junit | 4.11 | test |  | jar |  | **4.12-beta-1** |  |  |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.geronimo.specs | geronimo-json\_1.0\_spec | 1.0-alpha-1 | provided |  | jar |  |  |  |  |
| Status | Group Id | Artifact Id | Current Version | Scope | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |

<a id="archives-0.2-incubating-dependency-updates-report--dependency-updates"></a>

## Dependency Updates

<a id="archives-0.2-incubating-dependency-updates-report--junit:junit"></a>

### junit:junit

| Status | ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | junit |
| Artifact Id | junit |
| Current Version | 4.11 |
| Scope | test |
| Classifier |  |
| Type | jar |
| Newer versions | **4.12-beta-1** *Next Incremental* 4.12-beta-2 **4.12-beta-3** *Latest Incremental* |

<a id="archives-0.2-incubating-dependency-updates-report--org.apache.geronimo.specs:geronimo-json_1.0_spec"></a>

### org.apache.geronimo.specs:geronimo-json\_1.0\_spec

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.geronimo.specs |
| Artifact Id | geronimo-json\_1.0\_spec |
| Current Version | 1.0-alpha-1 |
| Scope | provided |
| Classifier |  |
| Type | jar |

---

<a id="archives-0.2-incubating-plugin-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/plugin-updates-report.html -->

<!-- page_index: 28 -->

<a id="archives-0.2-incubating-plugin-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various plugins.

| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | # of plugins using the latest version available | 27 |
| --- | --- | --- |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of plugins where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of plugins where the next version available is an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of plugins where the next version available is a minor version update | 1 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of plugins where the next version available is a major version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of plugins where a dependencies section containes a dependency with an updated version | 1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-management"></a>

### Plugin Management

| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-antrun-plugin | **1.7** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-assembly-plugin | **2.4.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-clean-plugin | **2.5** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-compiler-plugin | **3.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | org.apache.maven.plugins | maven-dependency-plugin | 2.8 |  |  | **2.9** |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-deploy-plugin | **2.8.2** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-docck-plugin | **1.0** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-enforcer-plugin | **1.3.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-failsafe-plugin | **2.17** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-gpg-plugin | **1.5** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-install-plugin | **2.5.2** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-invoker-plugin | **1.9** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-jar-plugin | **2.5** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-javadoc-plugin | **2.9.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-plugin-plugin | **3.3** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-release-plugin | **2.5.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-remote-resources-plugin | **1.5** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-resources-plugin | **2.6** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-scm-plugin | **1.9.2** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-scm-publish-plugin | **1.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | org.apache.maven.plugins | maven-site-plugin | **3.4** |  |  |  |  | ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-source-plugin | **2.3** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-surefire-plugin | **2.17** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.rat | apache-rat-plugin | **0.11** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.codehaus.mojo | clirr-maven-plugin | **2.6.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |

<a id="archives-0.2-incubating-plugin-updates-report--plugins"></a>

### Plugins

| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.apache.maven.plugins | maven-checkstyle-plugin | **2.13** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.codehaus.mojo | cobertura-maven-plugin | **2.6** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | org.eluder.coveralls | coveralls-maven-plugin | **3.0.1** |  |  |  |  | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) |
| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-updates"></a>

## Plugin Updates

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-antrun-plugin"></a>

### Plugin org.apache.maven.plugins:maven-antrun-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-antrun-plugin |
| Current Version | 1.7 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-assembly-plugin"></a>

### Plugin org.apache.maven.plugins:maven-assembly-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-assembly-plugin |
| Current Version | 2.4.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-checkstyle-plugin"></a>

### Plugin org.apache.maven.plugins:maven-checkstyle-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-checkstyle-plugin |
| Current Version | 2.13 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-clean-plugin"></a>

### Plugin org.apache.maven.plugins:maven-clean-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-clean-plugin |
| Current Version | 2.5 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-compiler-plugin"></a>

### Plugin org.apache.maven.plugins:maven-compiler-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-compiler-plugin |
| Current Version | 3.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-dependency-plugin"></a>

### Plugin org.apache.maven.plugins:maven-dependency-plugin

| Status | ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-dependency-plugin |
| Current Version | 2.8 |
| Newer versions | **2.9** *Next Minor* |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-deploy-plugin"></a>

### Plugin org.apache.maven.plugins:maven-deploy-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-deploy-plugin |
| Current Version | 2.8.2 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-docck-plugin"></a>

### Plugin org.apache.maven.plugins:maven-docck-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-docck-plugin |
| Current Version | 1.0 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-enforcer-plugin"></a>

### Plugin org.apache.maven.plugins:maven-enforcer-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-enforcer-plugin |
| Current Version | 1.3.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-failsafe-plugin"></a>

### Plugin org.apache.maven.plugins:maven-failsafe-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-failsafe-plugin |
| Current Version | 2.17 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-gpg-plugin"></a>

### Plugin org.apache.maven.plugins:maven-gpg-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-gpg-plugin |
| Current Version | 1.5 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-install-plugin"></a>

### Plugin org.apache.maven.plugins:maven-install-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-install-plugin |
| Current Version | 2.5.2 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-invoker-plugin"></a>

### Plugin org.apache.maven.plugins:maven-invoker-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-invoker-plugin |
| Current Version | 1.9 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-jar-plugin"></a>

### Plugin org.apache.maven.plugins:maven-jar-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-jar-plugin |
| Current Version | 2.5 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-javadoc-plugin"></a>

### Plugin org.apache.maven.plugins:maven-javadoc-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-javadoc-plugin |
| Current Version | 2.9.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-plugin-plugin"></a>

### Plugin org.apache.maven.plugins:maven-plugin-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-plugin-plugin |
| Current Version | 3.3 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-release-plugin"></a>

### Plugin org.apache.maven.plugins:maven-release-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-release-plugin |
| Current Version | 2.5.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-remote-resources-plugin"></a>

### Plugin org.apache.maven.plugins:maven-remote-resources-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-remote-resources-plugin |
| Current Version | 1.5 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-resources-plugin"></a>

### Plugin org.apache.maven.plugins:maven-resources-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-resources-plugin |
| Current Version | 2.6 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-scm-plugin"></a>

### Plugin org.apache.maven.plugins:maven-scm-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-scm-plugin |
| Current Version | 1.9.2 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-scm-publish-plugin"></a>

### Plugin org.apache.maven.plugins:maven-scm-publish-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-scm-publish-plugin |
| Current Version | 1.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-site-plugin"></a>

### Plugin org.apache.maven.plugins:maven-site-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-site-plugin |
| Current Version | 3.4 |

<a id="archives-0.2-incubating-plugin-updates-report--dependencies-of-org.apache.maven.plugins:maven-site-plugin"></a>

#### Dependencies of org.apache.maven.plugins:maven-site-plugin

| Status | Group Id | Artifact Id | Current Version | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | org.apache.maven | maven-archiver | 2.5 |  | jar |  |  | **2.6** |  |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | org.codehaus.plexus | plexus-archiver | 2.4.4 |  | jar |  |  | **2.5** |  |
| Status | Group Id | Artifact Id | Current Version | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |

<a id="archives-0.2-incubating-plugin-updates-report--dependency-org.apache.maven:maven-archiver"></a>

#### Dependency org.apache.maven:maven-archiver

| Status | ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven |
| Artifact Id | maven-archiver |
| Current Version | 2.5 |
| Classifier |  |
| Type | jar |
| Newer versions | **2.6** *Next Minor* |

<a id="archives-0.2-incubating-plugin-updates-report--dependency-org.codehaus.plexus:plexus-archiver"></a>

#### Dependency org.codehaus.plexus:plexus-archiver

| Status | ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.codehaus.plexus |
| Artifact Id | plexus-archiver |
| Current Version | 2.4.4 |
| Classifier |  |
| Type | jar |
| Newer versions | **2.5** *Next Minor* 2.6 2.6.1 2.6.2 2.6.3 2.6.4 2.7 2.7.1 2.8 2.8.1 2.8.2 2.8.3 **2.8.4** *Latest Minor* |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-source-plugin"></a>

### Plugin org.apache.maven.plugins:maven-source-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-source-plugin |
| Current Version | 2.3 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-surefire-plugin"></a>

### Plugin org.apache.maven.plugins:maven-surefire-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-surefire-plugin |
| Current Version | 2.17 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.apache.rat:apache-rat-plugin"></a>

### Plugin org.apache.rat:apache-rat-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.rat |
| Artifact Id | apache-rat-plugin |
| Current Version | 0.11 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.codehaus.mojo:clirr-maven-plugin"></a>

### Plugin org.codehaus.mojo:clirr-maven-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.codehaus.mojo |
| Artifact Id | clirr-maven-plugin |
| Current Version | 2.6.1 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.codehaus.mojo:cobertura-maven-plugin"></a>

### Plugin org.codehaus.mojo:cobertura-maven-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.codehaus.mojo |
| Artifact Id | cobertura-maven-plugin |
| Current Version | 2.6 |

<a id="archives-0.2-incubating-plugin-updates-report--plugin-org.eluder.coveralls:coveralls-maven-plugin"></a>

### Plugin org.eluder.coveralls:coveralls-maven-plugin

| Status | ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) No newer versions available. |
| --- | --- |
| Group Id | org.eluder.coveralls |
| Artifact Id | coveralls-maven-plugin |
| Current Version | 3.0.1 |

---

<a id="archives-0.2-incubating-property-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/property-updates-report.html -->

<!-- page_index: 29 -->

<a id="archives-0.2-incubating-property-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various properties associated with artifacts.

| ![](assets/images/icon-success-sml_bb950c4f6bb2db03.gif) | # of properties using the latest version available | 0 |
| --- | --- | --- |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of properties where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of properties where the next version available is an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of properties where the next version available is a minor version update | 0 |
| ![](assets/images/icon-warning-sml_5becd8cba919d64f.gif) | # of properties where the next version available is a major version update | 0 |

<a id="archives-0.2-incubating-property-updates-report--summary-of-properties-associated-with-artifact-versions"></a>

### Summary of properties associated with artifact versions

report.overview.noProperty

<a id="archives-0.2-incubating-property-updates-report--properties-associated-with-artifact-versions"></a>

## Properties associated with artifact versions

---

<a id="archives-0.2-incubating-changelog"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/changelog.html -->

<!-- page_index: 30 -->

<a id="archives-0.2-incubating-changelog--change-log-report"></a>

## Change Log Report

Total number of changed sets: 1

<a id="archives-0.2-incubating-changelog--changes-between-14-oct-2014-and-14-nov-2014"></a>

### Changes between 14 Oct, 2014 and 14 Nov, 2014

Total commits: 29 Total number of files changed: 33

| Timestamp | Author | Details |
| --- | --- | --- |
| 2014-11-13 20:26:20 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) [v 56c9789b3de1fbdcbf0a260ba2f26fce70171ffa](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?rev=56c9789b3de1fbdcbf0a260ba2f26fce70171ffa&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) [v 56c9789b3de1fbdcbf0a260ba2f26fce70171ffa](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?rev=56c9789b3de1fbdcbf0a260ba2f26fce70171ffa&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) [v 56c9789b3de1fbdcbf0a260ba2f26fce70171ffa](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?rev=56c9789b3de1fbdcbf0a260ba2f26fce70171ffa&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 56c9789b3de1fbdcbf0a260ba2f26fce70171ffa](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=56c9789b3de1fbdcbf0a260ba2f26fce70171ffa&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [maven-release-plugin] prepare release v0.2-incubating |
| 2014-11-12 18:30:29 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 8f5b8bdd24a79b45dad4bdaf2c9651df3e8192fc](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=8f5b8bdd24a79b45dad4bdaf2c9651df3e8192fc&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) typo |
| 2014-11-12 11:40:10 | Romain Manni-Bucau <rmannibucau@apache.org> | [src/site/markdown/**index.md**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/src/site/markdown/index.md?p=incubator-johnzon.git) [v 977e3c7e1ccf049f6905425f64eadb07b73de437](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/src/site/markdown/index.md?rev=977e3c7e1ccf049f6905425f64eadb07b73de437&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) adding ConfigurableJohnzonProvider in doc |
| 2014-11-12 11:38:28 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?p=incubator-johnzon.git) [v e45db5c6a492ee6c4c9238d987bb90f57238db71](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?rev=e45db5c6a492ee6c4c9238d987bb90f57238db71&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**IgnorableTypes.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/IgnorableTypes.java?p=incubator-johnzon.git) [v e45db5c6a492ee6c4c9238d987bb90f57238db71](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/IgnorableTypes.java?rev=e45db5c6a492ee6c4c9238d987bb90f57238db71&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonMessageBodyReader.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyReader.java?p=incubator-johnzon.git) [v e45db5c6a492ee6c4c9238d987bb90f57238db71](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyReader.java?rev=e45db5c6a492ee6c4c9238d987bb90f57238db71&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonMessageBodyWriter.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyWriter.java?p=incubator-johnzon.git) [v e45db5c6a492ee6c4c9238d987bb90f57238db71](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyWriter.java?rev=e45db5c6a492ee6c4c9238d987bb90f57238db71&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonProvider.java?p=incubator-johnzon.git) [v e45db5c6a492ee6c4c9238d987bb90f57238db71](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonProvider.java?rev=e45db5c6a492ee6c4c9238d987bb90f57238db71&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProviderTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProviderTest.java?p=incubator-johnzon.git) [v e45db5c6a492ee6c4c9238d987bb90f57238db71](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProviderTest.java?rev=e45db5c6a492ee6c4c9238d987bb90f57238db71&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-24](http://jira.codehaus.org/browse/JOHNZON-24) ConfigurableJohnzonProvider |
| 2014-11-12 11:11:56 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 222c5df80b6999301a49bfb4e27fbbb50301e4ca](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=222c5df80b6999301a49bfb4e27fbbb50301e4ca&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) if raw type is Collection we have to handle it. Whatever type we use would be fnie, using ArrayList for now since it looks the most common. If we don't handle it then we can't ask for Collection<xxx> which would be a pain in a lot of cases |
| 2014-11-12 07:48:13 | Romain Manni-Bucau <rmannibucau@apache.org> | [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v c87e427c530ac48e84551e9f1021732882d91914](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=c87e427c530ac48e84551e9f1021732882d91914&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) not sure why spec jar was insnapshot |
| 2014-11-11 22:42:24 | Hendrik Saly <hendrikdev22@gmail.com> | [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 51c524dbba5849107abccf0ab3b122a84bb54928](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=51c524dbba5849107abccf0ab3b122a84bb54928&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) maven taglist-, changelog- and changes-plugin added to pom |
| 2014-11-11 20:36:49 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) [v bcf51d2e5b1267dcf317816b7db759460cb3c715](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?rev=bcf51d2e5b1267dcf317816b7db759460cb3c715&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) [v bcf51d2e5b1267dcf317816b7db759460cb3c715](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?rev=bcf51d2e5b1267dcf317816b7db759460cb3c715&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) more global exclude rules for fields and methods |
| 2014-11-11 20:33:14 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonIgnore.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonIgnore.java?p=incubator-johnzon.git) [v 8e253a052c7cbf6214b6ae7f1f324766b4344355](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonIgnore.java?rev=8e253a052c7cbf6214b6ae7f1f324766b4344355&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) JohnzonIgnore can now be on fields |
| 2014-11-11 20:27:25 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) [v 9b6ad074dfe7922b5f64b7e54f952936ebd45eaa](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?rev=9b6ad074dfe7922b5f64b7e54f952936ebd45eaa&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAndMethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAndMethodAccessMode.java?p=incubator-johnzon.git) [v 9b6ad074dfe7922b5f64b7e54f952936ebd45eaa](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAndMethodAccessMode.java?rev=9b6ad074dfe7922b5f64b7e54f952936ebd45eaa&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) adding FieldAndMethodAccessMode access mode |
| 2014-11-11 20:23:45 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) [v 2ce282b46649ba73f67daedc2e927e265e040439](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?rev=2ce282b46649ba73f67daedc2e927e265e040439&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) skipping transient fields with FieldAccessMode |
| 2014-11-11 20:22:18 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) [v 8f8565791cd71dfabfd7312630874d9ee4f6c5ce](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?rev=8f8565791cd71dfabfd7312630874d9ee4f6c5ce&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) skipping static fields with FieldAccessMode |
| 2014-11-11 20:05:55 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) [v deaea89fb84bddbed38b17c088fedc6bb2a84b96](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?rev=deaea89fb84bddbed38b17c088fedc6bb2a84b96&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) [v deaea89fb84bddbed38b17c088fedc6bb2a84b96](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?rev=deaea89fb84bddbed38b17c088fedc6bb2a84b96&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) ignore and allow to override easily isIgnored in our access modes |
| 2014-11-11 16:27:59 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**AccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/AccessMode.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/AccessMode.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v bb96f71eb40c79a824e0688d3826994e4ebc3c06](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=bb96f71eb40c79a824e0688d3826994e4ebc3c06&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-23](http://jira.codehaus.org/browse/JOHNZON-23) field access support |
| 2014-11-11 11:51:17 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 6fa15005996dc00df5439d467a2d75ac9f250600](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=6fa15005996dc00df5439d467a2d75ac9f250600&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) [v 6fa15005996dc00df5439d467a2d75ac9f250600](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?rev=6fa15005996dc00df5439d467a2d75ac9f250600&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v 6fa15005996dc00df5439d467a2d75ac9f250600](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=6fa15005996dc00df5439d467a2d75ac9f250600&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperEnhancedTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperEnhancedTest.java?p=incubator-johnzon.git) [v 6fa15005996dc00df5439d467a2d75ac9f250600](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperEnhancedTest.java?rev=6fa15005996dc00df5439d467a2d75ac9f250600&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 6fa15005996dc00df5439d467a2d75ac9f250600](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=6fa15005996dc00df5439d467a2d75ac9f250600&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-22](http://jira.codehaus.org/browse/JOHNZON-22) supporting private constructors in Mapper |
| 2014-11-09 21:28:38 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 8bc90136178f915603f43be7ed1b6a25724754e8](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=8bc90136178f915603f43be7ed1b6a25724754e8&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 8bc90136178f915603f43be7ed1b6a25724754e8](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=8bc90136178f915603f43be7ed1b6a25724754e8&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-20](http://jira.codehaus.org/browse/JOHNZON-20) basic Map<String, Object> support |
| 2014-11-09 21:11:45 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonMessageBodyReader.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyReader.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyReader.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**JohnzonCollectionType.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonCollectionType.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonCollectionType.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**JohnzonListType.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonListType.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonListType.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**JohnzonParameterizedType.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonParameterizedType.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonParameterizedType.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 09bfdc4a6a95bb5c15b923ae1a73010aacf13211](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=09bfdc4a6a95bb5c15b923ae1a73010aacf13211&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-19](http://jira.codehaus.org/browse/JOHNZON-19) fixing reflection for readCollection in Mapper |
| 2014-11-08 14:00:07 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/src/main/java/org/apache/johnzon/core/**JsonGeneratorImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonGeneratorImpl.java?p=incubator-johnzon.git) [v 35f5d7765642000d5abcc9edaad876192576a603](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonGeneratorImpl.java?rev=35f5d7765642000d5abcc9edaad876192576a603&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-core/src/main/java/org/apache/johnzon/core/**JsonInMemoryParser.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonInMemoryParser.java?p=incubator-johnzon.git) [v 35f5d7765642000d5abcc9edaad876192576a603](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonInMemoryParser.java?rev=35f5d7765642000d5abcc9edaad876192576a603&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) Fixed some minor possible bugs reported by FindBugs |
| 2014-11-06 11:19:39 | salyh <hendrikdev22@gmail.com> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v 64ddab0df40a57b33ad39e8f0b35710ad0a801d0](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=64ddab0df40a57b33ad39e8f0b35710ad0a801d0&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 64ddab0df40a57b33ad39e8f0b35710ad0a801d0](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=64ddab0df40a57b33ad39e8f0b35710ad0a801d0&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) revert hashmap -> linkedhashmap |
| 2014-11-05 20:55:37 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 1b23891042ede1b3bf461026c10c80b85a4087a2](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=1b23891042ede1b3bf461026c10c80b85a4087a2&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) clean up testcase, remove unnecessary code |
| 2014-11-05 20:42:47 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/src/main/java/org/apache/johnzon/core/**JsonStreamParserImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonStreamParserImpl.java?p=incubator-johnzon.git) [v b5b99cf4046bb73e37cd6921417a20deea2fd921](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonStreamParserImpl.java?rev=b5b99cf4046bb73e37cd6921417a20deea2fd921&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-core/src/test/java/org/apache/johnzon/core/**JsonParserTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?p=incubator-johnzon.git) [v b5b99cf4046bb73e37cd6921417a20deea2fd921](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?rev=b5b99cf4046bb73e37cd6921417a20deea2fd921&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-18](http://jira.codehaus.org/browse/JOHNZON-18), applied patch from Thiago Veronezi: JsonStreamParserImpl not filling up buffer consistently - thanks a lot for this issue report and patch! |
| 2014-11-04 23:53:29 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) [v c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?rev=c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**NullTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/NullTest.java?p=incubator-johnzon.git) [v c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/NullTest.java?rev=c0ebe9d2acbd8515a6169e7c1c80ecbe3ae67988&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-21](http://jira.codehaus.org/browse/JOHNZON-21) (renamed setter/getter to method), implemented basic null and empty array handling (allow to have nulls in the serialization, allow to have/skip empty arrays in the serialization) |
| 2014-11-04 21:15:29 | Hendrik Saly <hendrikdev22@gmail.com> | [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 7176fdecdccf947421c2d8de25cf61ca996a2803](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=7176fdecdccf947421c2d8de25cf61ca996a2803&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) corrected site plugin version, added some update-reports |
| 2014-11-04 18:38:50 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/src/test/java/org/apache/johnzon/core/**JsonParserTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?p=incubator-johnzon.git) [v 87dae26355287f176881b8e7a0e8d2705a76a996](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?rev=87dae26355287f176881b8e7a0e8d2705a76a996&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) Testcase for attempting input stream behaviour added |
| 2014-10-30 17:45:45 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/xml/**WadlDocumentToJsonTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/xml/WadlDocumentToJsonTest.java?p=incubator-johnzon.git) [v b7948d5174018ddf04c95a4abd8107720d20155e](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/xml/WadlDocumentToJsonTest.java?rev=b7948d5174018ddf04c95a4abd8107720d20155e&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**LiteralTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/LiteralTest.java?p=incubator-johnzon.git) [v b7948d5174018ddf04c95a4abd8107720d20155e](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/LiteralTest.java?rev=b7948d5174018ddf04c95a4abd8107720d20155e&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperEnhancedTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperEnhancedTest.java?p=incubator-johnzon.git) [v b7948d5174018ddf04c95a4abd8107720d20155e](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperEnhancedTest.java?rev=b7948d5174018ddf04c95a4abd8107720d20155e&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v b7948d5174018ddf04c95a4abd8107720d20155e](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=b7948d5174018ddf04c95a4abd8107720d20155e&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v b7948d5174018ddf04c95a4abd8107720d20155e](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=b7948d5174018ddf04c95a4abd8107720d20155e&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) Update checkstyle configuration (and fixed some check style errors), update contributorsrs, some minor pom.xml changes |
| 2014-10-30 16:22:34 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/src/main/java/org/apache/johnzon/core/**RFC4627AwareInputStreamReader.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/RFC4627AwareInputStreamReader.java?p=incubator-johnzon.git) [v 399a368c4a15e2e6b53b7f87f1cfc9d16a2132d7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/RFC4627AwareInputStreamReader.java?rev=399a368c4a15e2e6b53b7f87f1cfc9d16a2132d7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-core/src/test/java/org/apache/johnzon/core/**JsonParserTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?p=incubator-johnzon.git) [v 399a368c4a15e2e6b53b7f87f1cfc9d16a2132d7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?rev=399a368c4a15e2e6b53b7f87f1cfc9d16a2132d7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-17](http://jira.codehaus.org/browse/JOHNZON-17) Thiago Veronezi: RFC4627AwareInputStreamReader - Make sure that we read all the bytes before throwing an exception |
| 2014-10-29 16:35:12 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/src/main/java/org/apache/johnzon/core/**RFC4627AwareInputStreamReader.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/RFC4627AwareInputStreamReader.java?p=incubator-johnzon.git) [v 80cf6a02f0d5377113856986c8f9edeaea911cde](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/RFC4627AwareInputStreamReader.java?rev=80cf6a02f0d5377113856986c8f9edeaea911cde&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-core/src/test/java/org/apache/johnzon/core/**JsonParserTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?p=incubator-johnzon.git) [v 80cf6a02f0d5377113856986c8f9edeaea911cde](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?rev=80cf6a02f0d5377113856986c8f9edeaea911cde&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-16](http://jira.codehaus.org/browse/JOHNZON-16) Fix BOM detection for [UTF-8](http://jira.codehaus.org/browse/UTF-8), new testcase for stream that throws an exception by Thiago Veronezi |
| 2014-10-21 00:00:07 | salyh <hendrikdev22@gmail.com> | [**.travis.yml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/.travis.yml?p=incubator-johnzon.git) [v 0fdbca31d1f4964a11e73cc6756f6d59bd945723](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/.travis.yml?rev=0fdbca31d1f4964a11e73cc6756f6d59bd945723&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 0fdbca31d1f4964a11e73cc6756f6d59bd945723](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=0fdbca31d1f4964a11e73cc6756f6d59bd945723&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) Cobertura code coverage settings adjusted, pmd plugin version update |
| 2014-10-20 10:44:45 | salyh <hendrikdev22@gmail.com> | [**.travis.yml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/.travis.yml?p=incubator-johnzon.git) [v 100095f92a52a9c40602592203e8882a88985ed9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/.travis.yml?rev=100095f92a52a9c40602592203e8882a88985ed9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) coveralls.io support |

---

<a id="archives-0.2-incubating-file-activity"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/file-activity.html -->

<!-- page_index: 31 -->

<a id="archives-0.2-incubating-file-activity--file-activity-report"></a>

## File Activity Report

<a id="archives-0.2-incubating-file-activity--changes-between-14-oct-2014-and-14-nov-2014"></a>

### Changes between 14 Oct, 2014 and 14 Nov, 2014

Total commits: 29 Total number of files changed: 33

| Filename | Number of Times Changed |
| --- | --- |
| [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) | 8 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) | 7 |
| [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) | 6 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) | 5 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) | 5 |
| [johnzon-core/src/test/java/org/apache/johnzon/core/**JsonParserTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/test/java/org/apache/johnzon/core/JsonParserTest.java?p=incubator-johnzon.git) | 4 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) | 4 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) | 3 |
| [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonMessageBodyReader.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyReader.java?p=incubator-johnzon.git) | 2 |
| [**.travis.yml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/.travis.yml?p=incubator-johnzon.git) | 2 |
| [johnzon-core/src/main/java/org/apache/johnzon/core/**RFC4627AwareInputStreamReader.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/RFC4627AwareInputStreamReader.java?p=incubator-johnzon.git) | 2 |
| [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperEnhancedTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperEnhancedTest.java?p=incubator-johnzon.git) | 2 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**JohnzonCollectionType.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonCollectionType.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**JohnzonListType.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonListType.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**JohnzonParameterizedType.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/JohnzonParameterizedType.java?p=incubator-johnzon.git) | 1 |
| [johnzon-core/src/main/java/org/apache/johnzon/core/**JsonGeneratorImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonGeneratorImpl.java?p=incubator-johnzon.git) | 1 |
| [johnzon-core/src/main/java/org/apache/johnzon/core/**JsonInMemoryParser.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonInMemoryParser.java?p=incubator-johnzon.git) | 1 |
| [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonIgnore.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonIgnore.java?p=incubator-johnzon.git) | 1 |
| [src/site/markdown/**index.md**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/src/site/markdown/index.md?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAndMethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAndMethodAccessMode.java?p=incubator-johnzon.git) | 1 |
| [johnzon-core/src/main/java/org/apache/johnzon/core/**JsonStreamParserImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/src/main/java/org/apache/johnzon/core/JsonStreamParserImpl.java?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/xml/**WadlDocumentToJsonTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/xml/WadlDocumentToJsonTest.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**LiteralTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/LiteralTest.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**AccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/AccessMode.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**NullTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/NullTest.java?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**IgnorableTypes.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/IgnorableTypes.java?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonMessageBodyWriter.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonMessageBodyWriter.java?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**JohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/JohnzonProvider.java?p=incubator-johnzon.git) | 1 |
| [johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProviderTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/test/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProviderTest.java?p=incubator-johnzon.git) | 1 |

---

<a id="archives-0.2-incubating-dev-activity"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/dev-activity.html -->

<!-- page_index: 32 -->

<a id="archives-0.2-incubating-dev-activity--developer-activity-report"></a>

## Developer Activity Report

<a id="archives-0.2-incubating-dev-activity--changes-between-14-oct-2014-and-14-nov-2014"></a>

### Changes between 14 Oct, 2014 and 14 Nov, 2014

Total commits: 29 Total number of files changed: 33

| Developer | Total commits | Total Number of Files Changed |
| --- | --- | --- |
| Hendrik Saly <hendrikdev22@gmail.com> | 11 | 17 |
| Romain Manni-Bucau <rmannibucau@apache.org> | 15 | 21 |
| salyh <hendrikdev22@gmail.com> | 3 | 4 |

---

<a id="archives-0.2-incubating-jira-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.2-incubating/jira-report.html -->

<!-- page_index: 33 -->

<a id="archives-0.2-incubating-jira-report--jira-report"></a>

## JIRA Report

| Type | Key | Summary | By | Status | Resolution | Created |
| --- | --- | --- | --- | --- | --- | --- |
| Bug | [JOHNZON-17](https://issues.apache.org/jira/browse/JOHNZON-17) | RFC4627AwareInputStreamReader - Make sure that we read all the bytes before throwing an exception | Hendrik Saly | Closed | Fixed | 2014-10-30 |
| Bug | [JOHNZON-18](https://issues.apache.org/jira/browse/JOHNZON-18) | JsonStreamParserImpl not filling up buffer consistently | Hendrik Saly | Closed | Fixed | 2014-11-04 |
| Bug | [JOHNZON-19](https://issues.apache.org/jira/browse/JOHNZON-19) | rework readCollection() generics |  | Closed | Fixed | 2014-11-04 |
| Bug | [JOHNZON-20](https://issues.apache.org/jira/browse/JOHNZON-20) | support Map<String, Object> |  | Closed | Fixed | 2014-11-04 |
| Improvement | [JOHNZON-15](https://issues.apache.org/jira/browse/JOHNZON-15) | Remove duplicated method on Johzon Mapper. |  | Closed | Fixed | 2014-10-07 |
| Improvement | [JOHNZON-21](https://issues.apache.org/jira/browse/JOHNZON-21) | org.apache.johnzon.mapper.reflection.Mappings.Getter#Getter |  | Closed | Fixed | 2014-11-04 |
| New Feature | [JOHNZON-22](https://issues.apache.org/jira/browse/JOHNZON-22) | support private/protected constructor in Mapper |  | Closed | Fixed | 2014-11-11 |
| New Feature | [JOHNZON-23](https://issues.apache.org/jira/browse/JOHNZON-23) | support field access |  | Closed | Fixed | 2014-11-11 |
| New Feature | [JOHNZON-24](https://issues.apache.org/jira/browse/JOHNZON-24) | add a ConfigurableJohnzonProvider to ease configuration of the jaxrs provider |  | Closed | Fixed | 2014-11-12 |

---

<a id="archives-0.1-incubating-modules"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.1-incubating/modules.html -->

<!-- page_index: 34 -->

<a id="archives-0.1-incubating-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Johnzon :: Core](https://johnzon.apache.org/archives/0.1-incubating/johnzon-core/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Mapper](https://johnzon.apache.org/archives/0.1-incubating/johnzon-mapper/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JAX-RS](https://johnzon.apache.org/archives/0.1-incubating/johnzon-jaxrs/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |

---

<a id="archives-0.7-incubating-changelog"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/changelog.html -->

<!-- page_index: 35 -->

<a id="archives-0.7-incubating-changelog--change-log-report"></a>

## Change Log Report

Total number of changed sets: 1

<a id="archives-0.7-incubating-changelog--changes-between-22-feb-2015-and-25-mar-2015"></a>

### Changes between 22 Feb, 2015 and 25 Mar, 2015

Total commits: 12 Total number of files changed: 39

| Timestamp | Author | Details |
| --- | --- | --- |
| 2015-03-24 16:51:59 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/**JsrCodecTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/JsrCodecTest.java?p=incubator-johnzon.git) [v 0a336cc1d2098b686c02b4c5fceb14414100de9f](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/JsrCodecTest.java?rev=0a336cc1d2098b686c02b4c5fceb14414100de9f&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/**MapperCodecTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/MapperCodecTest.java?p=incubator-johnzon.git) [v 0a336cc1d2098b686c02b4c5fceb14414100de9f](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/MapperCodecTest.java?rev=0a336cc1d2098b686c02b4c5fceb14414100de9f&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) dont use jar dependency in maven reactor |
| 2015-03-24 16:40:20 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ClientEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ClientEndpointImpl.java?p=incubator-johnzon.git) [v 622f4a495e29a01fe239399d2f88097fad1484c4](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ClientEndpointImpl.java?rev=622f4a495e29a01fe239399d2f88097fad1484c4&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [src/site/markdown/**index.md.vm**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/src/site/markdown/index.md.vm?p=incubator-johnzon.git) [v 622f4a495e29a01fe239399d2f88097fad1484c4](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/src/site/markdown/index.md.vm?rev=622f4a495e29a01fe239399d2f88097fad1484c4&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) minor cleanup + adding few doc about websocket codecs |
| 2015-03-24 16:29:57 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-websocket/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/pom.xml?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/pom.xml?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/**FactoryLocator.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/FactoryLocator.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/FactoryLocator.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/**JsrDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/JsrDecoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/JsrDecoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/**JsrEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/JsrEncoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/JsrEncoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/mapper/**MapperLocator.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/mapper/MapperLocator.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/mapper/MapperLocator.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrArrayDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrArrayDecoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrArrayDecoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrArrayEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrArrayEncoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrArrayEncoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrObjectDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrObjectDecoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrObjectDecoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrObjectEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrObjectEncoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrObjectEncoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrStructureDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrStructureDecoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrStructureDecoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrStructureEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrStructureEncoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrStructureEncoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/**JohnzonTextDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/JohnzonTextDecoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/JohnzonTextDecoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/**JohnzonTextEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/JohnzonTextEncoder.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/JohnzonTextEncoder.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/**JsrCodecTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/JsrCodecTest.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/JsrCodecTest.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/**MapperCodecTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/MapperCodecTest.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/MapperCodecTest.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ClientEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ClientEndpointImpl.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ClientEndpointImpl.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**JsrClientEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/JsrClientEndpointImpl.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/JsrClientEndpointImpl.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**JsrServerEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/JsrServerEndpointImpl.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/JsrServerEndpointImpl.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**Message.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/Message.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/Message.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ServerEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ServerEndpointImpl.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ServerEndpointImpl.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ServerReport.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ServerReport.java?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ServerReport.java?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-websocket/src/test/resources/**arquillian.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/resources/arquillian.xml?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/resources/arquillian.xml?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 29a79edb9a9845a01098188c418331319079009d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=29a79edb9a9845a01098188c418331319079009d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-41](http://jira.codehaus.org/browse/JOHNZON-41) jsr 356 integration, note: still some work to do on client annotation endpoint integration but didnt find a right api yet |
| 2015-03-24 15:21:00 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) [v e9891591423c78615daf8b53e91737ff3c2c409d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?rev=e9891591423c78615daf8b53e91737ff3c2c409d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) [v e9891591423c78615daf8b53e91737ff3c2c409d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?rev=e9891591423c78615daf8b53e91737ff3c2c409d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) [v e9891591423c78615daf8b53e91737ff3c2c409d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?rev=e9891591423c78615daf8b53e91737ff3c2c409d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v e9891591423c78615daf8b53e91737ff3c2c409d](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=e9891591423c78615daf8b53e91737ff3c2c409d&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) having aprent named apache-johnzon makes source assembly well named and doesnt bother children with apache prefix |
| 2015-03-24 15:00:37 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) [v d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?rev=d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) [v d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?rev=d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) [v d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?rev=d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=d47edcc559a5b13b2a83a4efdc9b720bdaeb9e56&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) Revert "Prefix artifactId with "apache-". !!Note: This will change the maven coordinates for 0.8!!" This reverts commit adb483f6269e3b87aa5b3811c9999327f4bdb702. |
| 2015-03-23 16:24:47 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) [v adb483f6269e3b87aa5b3811c9999327f4bdb702](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?rev=adb483f6269e3b87aa5b3811c9999327f4bdb702&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) [v adb483f6269e3b87aa5b3811c9999327f4bdb702](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?rev=adb483f6269e3b87aa5b3811c9999327f4bdb702&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) [v adb483f6269e3b87aa5b3811c9999327f4bdb702](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?rev=adb483f6269e3b87aa5b3811c9999327f4bdb702&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v adb483f6269e3b87aa5b3811c9999327f4bdb702](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=adb483f6269e3b87aa5b3811c9999327f4bdb702&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) Prefix artifactId with "apache-". !!Note: This will change the maven coordinates for 0.8!! |
| 2015-03-23 15:56:10 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) [v 30cc08715d9b70e6bce57680999f92ce13508a65](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?rev=30cc08715d9b70e6bce57680999f92ce13508a65&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) [v 30cc08715d9b70e6bce57680999f92ce13508a65](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?rev=30cc08715d9b70e6bce57680999f92ce13508a65&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) [v 30cc08715d9b70e6bce57680999f92ce13508a65](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?rev=30cc08715d9b70e6bce57680999f92ce13508a65&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 30cc08715d9b70e6bce57680999f92ce13508a65](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=30cc08715d9b70e6bce57680999f92ce13508a65&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [maven-release-plugin] prepare for next development iteration |
| 2015-03-23 15:56:00 | Hendrik Saly <hendrikdev22@gmail.com> | [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) [v 97930e2a8447c330115263afc83c094d48b163c8](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?rev=97930e2a8447c330115263afc83c094d48b163c8&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) [v 97930e2a8447c330115263afc83c094d48b163c8](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?rev=97930e2a8447c330115263afc83c094d48b163c8&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) [v 97930e2a8447c330115263afc83c094d48b163c8](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?rev=97930e2a8447c330115263afc83c094d48b163c8&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) [v 97930e2a8447c330115263afc83c094d48b163c8](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?rev=97930e2a8447c330115263afc83c094d48b163c8&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [maven-release-plugin] prepare release v0.7-incubating |
| 2015-03-15 20:25:35 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Experimental.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Experimental.java?p=incubator-johnzon.git) [v 5d656c825e6351f26a93cbffcf10ef49b310ded9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Experimental.java?rev=5d656c825e6351f26a93cbffcf10ef49b310ded9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonVirtualObject.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonVirtualObject.java?p=incubator-johnzon.git) [v 5d656c825e6351f26a93cbffcf10ef49b310ded9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonVirtualObject.java?rev=5d656c825e6351f26a93cbffcf10ef49b310ded9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonVirtualObjects.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonVirtualObjects.java?p=incubator-johnzon.git) [v 5d656c825e6351f26a93cbffcf10ef49b310ded9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonVirtualObjects.java?rev=5d656c825e6351f26a93cbffcf10ef49b310ded9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 5d656c825e6351f26a93cbffcf10ef49b310ded9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=5d656c825e6351f26a93cbffcf10ef49b310ded9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v 5d656c825e6351f26a93cbffcf10ef49b310ded9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=5d656c825e6351f26a93cbffcf10ef49b310ded9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 5d656c825e6351f26a93cbffcf10ef49b310ded9](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=5d656c825e6351f26a93cbffcf10ef49b310ded9&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-40](http://jira.codehaus.org/browse/JOHNZON-40) virtual object support for our mapper |
| 2015-02-25 09:52:47 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v dcc3a2c2a96d095251328740c03ebc0c053077c6](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=dcc3a2c2a96d095251328740c03ebc0c053077c6&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) [v dcc3a2c2a96d095251328740c03ebc0c053077c6](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?rev=dcc3a2c2a96d095251328740c03ebc0c053077c6&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) [v dcc3a2c2a96d095251328740c03ebc0c053077c6](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?rev=dcc3a2c2a96d095251328740c03ebc0c053077c6&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v dcc3a2c2a96d095251328740c03ebc0c053077c6](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=dcc3a2c2a96d095251328740c03ebc0c053077c6&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) avoiding npe + checkstyle |
| 2015-02-25 09:11:14 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?p=incubator-johnzon.git) [v fee273e274bdf959e14516508c43ec280b1f4bd7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?rev=fee273e274bdf959e14516508c43ec280b1f4bd7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonConverter.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonConverter.java?p=incubator-johnzon.git) [v fee273e274bdf959e14516508c43ec280b1f4bd7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonConverter.java?rev=fee273e274bdf959e14516508c43ec280b1f4bd7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v fee273e274bdf959e14516508c43ec280b1f4bd7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=fee273e274bdf959e14516508c43ec280b1f4bd7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) [v fee273e274bdf959e14516508c43ec280b1f4bd7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?rev=fee273e274bdf959e14516508c43ec280b1f4bd7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) [v fee273e274bdf959e14516508c43ec280b1f4bd7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?rev=fee273e274bdf959e14516508c43ec280b1f4bd7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v fee273e274bdf959e14516508c43ec280b1f4bd7](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=fee273e274bdf959e14516508c43ec280b1f4bd7&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-39](http://jira.codehaus.org/browse/JOHNZON-39) constructor instantiation using @ConstructorProperties |
| 2015-02-25 08:49:47 | Romain Manni-Bucau <rmannibucau@apache.org> | [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?p=incubator-johnzon.git) [v 40575520f697e370a4e94b17743dbf2cdd04bcd1](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?rev=40575520f697e370a4e94b17743dbf2cdd04bcd1&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) [v 40575520f697e370a4e94b17743dbf2cdd04bcd1](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?rev=40575520f697e370a4e94b17743dbf2cdd04bcd1&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) [v 40575520f697e370a4e94b17743dbf2cdd04bcd1](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?rev=40575520f697e370a4e94b17743dbf2cdd04bcd1&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAndMethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAndMethodAccessMode.java?p=incubator-johnzon.git) [v 40575520f697e370a4e94b17743dbf2cdd04bcd1](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAndMethodAccessMode.java?rev=40575520f697e370a4e94b17743dbf2cdd04bcd1&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) [v 40575520f697e370a4e94b17743dbf2cdd04bcd1](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?rev=40575520f697e370a4e94b17743dbf2cdd04bcd1&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) [v 40575520f697e370a4e94b17743dbf2cdd04bcd1](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?rev=40575520f697e370a4e94b17743dbf2cdd04bcd1&content-type=text/vnd.viewcvs-markup&p=incubator-johnzon.git) [JOHNZON-38](http://jira.codehaus.org/browse/JOHNZON-38) also use Collection getter as writer is flag is set |

---

<a id="archives-0.7-incubating-dependency-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/dependency-updates-report.html -->

<!-- page_index: 36 -->

<a id="archives-0.7-incubating-dependency-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various dependencies.

| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | # of dependencies using the latest version available | 1 |
| --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of dependencies where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of dependencies where the next version available is an incremental version update | 1 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of dependencies where the next version available is a minor version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of dependencies where the next version available is a major version update | 0 |

<a id="archives-0.7-incubating-dependency-updates-report--dependency-management"></a>

### Dependency Management

This project does not declare any dependencies in a dependencyManagement section.

<a id="archives-0.7-incubating-dependency-updates-report--dependencies"></a>

### Dependencies

| Status | Group Id | Artifact Id | Current Version | Scope | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | junit | junit | 4.11 | test |  | jar |  | **4.12-beta-1** | **4.12** |  |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.geronimo.specs | geronimo-json\_1.0\_spec | 1.0-alpha-1 | provided |  | jar |  |  |  |  |
| Status | Group Id | Artifact Id | Current Version | Scope | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |

<a id="archives-0.7-incubating-dependency-updates-report--dependency-updates"></a>

## Dependency Updates

<a id="archives-0.7-incubating-dependency-updates-report--junit:junit"></a>

### junit:junit

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer incremental version available. Incremental updates are typically passive. |
| --- | --- |
| Group Id | junit |
| Artifact Id | junit |
| Current Version | 4.11 |
| Scope | test |
| Classifier |  |
| Type | jar |
| Newer versions | **4.12-beta-1** *Next Incremental* 4.12-beta-2 **4.12-beta-3** *Latest Incremental* **4.12** *Next Minor* |

<a id="archives-0.7-incubating-dependency-updates-report--org.apache.geronimo.specs:geronimo-json_1.0_spec"></a>

### org.apache.geronimo.specs:geronimo-json\_1.0\_spec

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.geronimo.specs |
| Artifact Id | geronimo-json\_1.0\_spec |
| Current Version | 1.0-alpha-1 |
| Scope | provided |
| Classifier |  |
| Type | jar |

---

<a id="archives-0.7-incubating-dev-activity"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/dev-activity.html -->

<!-- page_index: 37 -->

<a id="archives-0.7-incubating-dev-activity--developer-activity-report"></a>

## Developer Activity Report

<a id="archives-0.7-incubating-dev-activity--changes-between-22-feb-2015-and-25-mar-2015"></a>

### Changes between 22 Feb, 2015 and 25 Mar, 2015

Total commits: 12 Total number of files changed: 39

| Developer | Total commits | Total Number of Files Changed |
| --- | --- | --- |
| Hendrik Saly <hendrikdev22@gmail.com> | 4 | 4 |
| Romain Manni-Bucau <rmannibucau@apache.org> | 8 | 39 |

---

<a id="archives-0.7-incubating-file-activity"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/file-activity.html -->

<!-- page_index: 38 -->

<a id="archives-0.7-incubating-file-activity--file-activity-report"></a>

## File Activity Report

<a id="archives-0.7-incubating-file-activity--changes-between-22-feb-2015-and-25-mar-2015"></a>

### Changes between 22 Feb, 2015 and 25 Mar, 2015

Total commits: 12 Total number of files changed: 39

| Filename | Number of Times Changed |
| --- | --- |
| [**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/pom.xml?p=incubator-johnzon.git) | 6 |
| [johnzon-core/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-core/pom.xml?p=incubator-johnzon.git) | 5 |
| [johnzon-jaxrs/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/pom.xml?p=incubator-johnzon.git) | 5 |
| [johnzon-mapper/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/pom.xml?p=incubator-johnzon.git) | 5 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Mapper.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Mapper.java?p=incubator-johnzon.git) | 4 |
| [johnzon-mapper/src/test/java/org/apache/johnzon/mapper/**MapperTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/test/java/org/apache/johnzon/mapper/MapperTest.java?p=incubator-johnzon.git) | 3 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/**Mappings.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/reflection/Mappings.java?p=incubator-johnzon.git) | 3 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/**JsrCodecTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/JsrCodecTest.java?p=incubator-johnzon.git) | 2 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/**MapperCodecTest.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/MapperCodecTest.java?p=incubator-johnzon.git) | 2 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ClientEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ClientEndpointImpl.java?p=incubator-johnzon.git) | 2 |
| [johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/**ConfigurableJohnzonProvider.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-jaxrs/src/main/java/org/apache/johnzon/jaxrs/ConfigurableJohnzonProvider.java?p=incubator-johnzon.git) | 2 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**MapperBuilder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/MapperBuilder.java?p=incubator-johnzon.git) | 2 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**MethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/MethodAccessMode.java?p=incubator-johnzon.git) | 2 |
| [johnzon-websocket/**pom.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/pom.xml?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/**FactoryLocator.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/FactoryLocator.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/**JsrDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/JsrDecoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/**JsrEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/jsr/JsrEncoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/mapper/**MapperLocator.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/internal/mapper/MapperLocator.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrArrayDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrArrayDecoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrArrayEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrArrayEncoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrObjectDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrObjectDecoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrObjectEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrObjectEncoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrStructureDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrStructureDecoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/**JsrStructureEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/jsr/JsrStructureEncoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/**JohnzonTextDecoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/JohnzonTextDecoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/**JohnzonTextEncoder.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/main/java/org/apache/johnzon/websocket/mapper/JohnzonTextEncoder.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**JsrClientEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/JsrClientEndpointImpl.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**JsrServerEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/JsrServerEndpointImpl.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**Message.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/Message.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ServerEndpointImpl.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ServerEndpointImpl.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/**ServerReport.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/java/org/apache/johnzon/websocket/endpoint/ServerReport.java?p=incubator-johnzon.git) | 1 |
| [johnzon-websocket/src/test/resources/**arquillian.xml**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-websocket/src/test/resources/arquillian.xml?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAndMethodAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAndMethodAccessMode.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**Experimental.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/Experimental.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonVirtualObject.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonVirtualObject.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonVirtualObjects.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonVirtualObjects.java?p=incubator-johnzon.git) | 1 |
| [src/site/markdown/**index.md.vm**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/src/site/markdown/index.md.vm?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/**FieldAccessMode.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/access/FieldAccessMode.java?p=incubator-johnzon.git) | 1 |
| [johnzon-mapper/src/main/java/org/apache/johnzon/mapper/**JohnzonConverter.java**](https://git-wip-us.apache.org/repos/asf?p=incubator-johnzon.git/johnzon-mapper/src/main/java/org/apache/johnzon/mapper/JohnzonConverter.java?p=incubator-johnzon.git) | 1 |

---

<a id="archives-0.7-incubating-integration"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/integration.html -->

<!-- page_index: 39 -->

<a id="archives-0.7-incubating-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="archives-0.7-incubating-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/johnzon/
```

<a id="archives-0.7-incubating-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="archives-0.7-incubating-issue-tracking"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/issue-tracking.html -->

<!-- page_index: 40 -->

<a id="archives-0.7-incubating-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="archives-0.7-incubating-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/JOHNZON
```

---

<a id="archives-0.7-incubating-modules"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/modules.html -->

<!-- page_index: 41 -->

<a id="archives-0.7-incubating-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Johnzon :: Core](https://johnzon.apache.org/archives/0.7-incubating/johnzon-core/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: Mapper](https://johnzon.apache.org/archives/0.7-incubating/johnzon-mapper/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: JAX-RS](https://johnzon.apache.org/archives/0.7-incubating/johnzon-jaxrs/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| [Johnzon :: WebSocket](https://johnzon.apache.org/archives/0.7-incubating/johnzon-websocket/index.html) | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |

---

<a id="archives-0.7-incubating-plugin-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/plugin-updates-report.html -->

<!-- page_index: 42 -->

<a id="archives-0.7-incubating-plugin-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various plugins.

| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | # of plugins using the latest version available | 11 |
| --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of plugins where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of plugins where the next version available is an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of plugins where the next version available is a minor version update | 17 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of plugins where the next version available is a major version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of plugins where a dependencies section containes a dependency with an updated version | 1 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-management"></a>

### Plugin Management

| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-antrun-plugin | 1.7 |  |  | **1.8** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-assembly-plugin | 2.4.1 |  |  | **2.5** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-clean-plugin | 2.5 |  |  | **2.6** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-compiler-plugin | 3.1 |  |  | **3.2** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-dependency-plugin | 2.8 |  |  | **2.9** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-deploy-plugin | **2.8.2** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-docck-plugin | **1.0** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-enforcer-plugin | 1.3.1 |  |  | **1.4** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-failsafe-plugin | 2.17 |  |  | **2.18** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-gpg-plugin | 1.5 |  |  | **1.6** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-install-plugin | **2.5.2** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-invoker-plugin | **1.9** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-jar-plugin | 2.5 |  |  | **2.6** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-javadoc-plugin | 2.9.1 |  |  | **2.10** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-plugin-plugin | 3.3 |  |  | **3.4** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-release-plugin | **2.5.1** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-remote-resources-plugin | **1.5** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-resources-plugin | 2.6 |  |  | **2.7** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-scm-plugin | **1.9.2** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.maven.plugins | maven-scm-publish-plugin | **1.1** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-site-plugin | **3.4** |  |  |  |  | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-source-plugin | 2.3 |  |  | **2.4** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-surefire-plugin | 2.17 |  |  | **2.18** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.apache.rat | apache-rat-plugin | **0.11** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | org.codehaus.mojo | clirr-maven-plugin | **2.6.1** |  |  |  |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |

<a id="archives-0.7-incubating-plugin-updates-report--plugins"></a>

### Plugins

| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven.plugins | maven-checkstyle-plugin | 2.13 |  |  | **2.14** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.codehaus.mojo | cobertura-maven-plugin | 2.6 |  |  | **2.7** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.eluder.coveralls | coveralls-maven-plugin | 3.0.1 |  |  | **3.1.0** |  | ![](assets/images/icon-success-sml_17def3475b38b738.gif) |
| Status | Group Id | Artifact Id | Current Version | Next Version | Next Incremental | Next Minor | Next Major | Dependency status |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-updates"></a>

## Plugin Updates

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-antrun-plugin"></a>

### Plugin org.apache.maven.plugins:maven-antrun-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-antrun-plugin |
| Current Version | 1.7 |
| Newer versions | **1.8** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-assembly-plugin"></a>

### Plugin org.apache.maven.plugins:maven-assembly-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-assembly-plugin |
| Current Version | 2.4.1 |
| Newer versions | **2.5** *Next Minor* 2.5.1 2.5.2 **2.5.3** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-checkstyle-plugin"></a>

### Plugin org.apache.maven.plugins:maven-checkstyle-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-checkstyle-plugin |
| Current Version | 2.13 |
| Newer versions | **2.14** *Next Minor* **2.15** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-clean-plugin"></a>

### Plugin org.apache.maven.plugins:maven-clean-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-clean-plugin |
| Current Version | 2.5 |
| Newer versions | **2.6** *Next Minor* **2.6.1** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-compiler-plugin"></a>

### Plugin org.apache.maven.plugins:maven-compiler-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-compiler-plugin |
| Current Version | 3.1 |
| Newer versions | **3.2** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-dependency-plugin"></a>

### Plugin org.apache.maven.plugins:maven-dependency-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-dependency-plugin |
| Current Version | 2.8 |
| Newer versions | **2.9** *Next Minor* **2.10** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-deploy-plugin"></a>

### Plugin org.apache.maven.plugins:maven-deploy-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-deploy-plugin |
| Current Version | 2.8.2 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-docck-plugin"></a>

### Plugin org.apache.maven.plugins:maven-docck-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-docck-plugin |
| Current Version | 1.0 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-enforcer-plugin"></a>

### Plugin org.apache.maven.plugins:maven-enforcer-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-enforcer-plugin |
| Current Version | 1.3.1 |
| Newer versions | **1.4** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-failsafe-plugin"></a>

### Plugin org.apache.maven.plugins:maven-failsafe-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-failsafe-plugin |
| Current Version | 2.17 |
| Newer versions | **2.18** *Next Minor* **2.18.1** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-gpg-plugin"></a>

### Plugin org.apache.maven.plugins:maven-gpg-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-gpg-plugin |
| Current Version | 1.5 |
| Newer versions | **1.6** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-install-plugin"></a>

### Plugin org.apache.maven.plugins:maven-install-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-install-plugin |
| Current Version | 2.5.2 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-invoker-plugin"></a>

### Plugin org.apache.maven.plugins:maven-invoker-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-invoker-plugin |
| Current Version | 1.9 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-jar-plugin"></a>

### Plugin org.apache.maven.plugins:maven-jar-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-jar-plugin |
| Current Version | 2.5 |
| Newer versions | **2.6** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-javadoc-plugin"></a>

### Plugin org.apache.maven.plugins:maven-javadoc-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-javadoc-plugin |
| Current Version | 2.9.1 |
| Newer versions | **2.10** *Next Minor* 2.10.1 **2.10.2** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-plugin-plugin"></a>

### Plugin org.apache.maven.plugins:maven-plugin-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-plugin-plugin |
| Current Version | 3.3 |
| Newer versions | **3.4** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-release-plugin"></a>

### Plugin org.apache.maven.plugins:maven-release-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-release-plugin |
| Current Version | 2.5.1 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-remote-resources-plugin"></a>

### Plugin org.apache.maven.plugins:maven-remote-resources-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-remote-resources-plugin |
| Current Version | 1.5 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-resources-plugin"></a>

### Plugin org.apache.maven.plugins:maven-resources-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-resources-plugin |
| Current Version | 2.6 |
| Newer versions | **2.7** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-scm-plugin"></a>

### Plugin org.apache.maven.plugins:maven-scm-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-scm-plugin |
| Current Version | 1.9.2 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-scm-publish-plugin"></a>

### Plugin org.apache.maven.plugins:maven-scm-publish-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-scm-publish-plugin |
| Current Version | 1.1 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-site-plugin"></a>

### Plugin org.apache.maven.plugins:maven-site-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-site-plugin |
| Current Version | 3.4 |

<a id="archives-0.7-incubating-plugin-updates-report--dependencies-of-org.apache.maven.plugins:maven-site-plugin"></a>

#### Dependencies of org.apache.maven.plugins:maven-site-plugin

| Status | Group Id | Artifact Id | Current Version | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.apache.maven | maven-archiver | 2.5 |  | jar |  |  | **2.6** |  |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | org.codehaus.plexus | plexus-archiver | 2.4.4 |  | jar |  |  | **2.5** | **3.0** |
| Status | Group Id | Artifact Id | Current Version | Classifier | Type | Next Version | Next Incremental | Next Minor | Next Major |

<a id="archives-0.7-incubating-plugin-updates-report--dependency-org.apache.maven:maven-archiver"></a>

#### Dependency org.apache.maven:maven-archiver

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven |
| Artifact Id | maven-archiver |
| Current Version | 2.5 |
| Classifier |  |
| Type | jar |
| Newer versions | **2.6** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--dependency-org.codehaus.plexus:plexus-archiver"></a>

#### Dependency org.codehaus.plexus:plexus-archiver

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.codehaus.plexus |
| Artifact Id | plexus-archiver |
| Current Version | 2.4.4 |
| Classifier |  |
| Type | jar |
| Newer versions | **2.5** *Next Minor* 2.6 2.6.1 2.6.2 2.6.3 2.6.4 2.7 2.7.1 2.8 2.8.1 2.8.2 2.8.3 2.8.4 2.9 2.9.1 **2.10-beta-1** *Latest Minor* **3.0** *Next Major* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-source-plugin"></a>

### Plugin org.apache.maven.plugins:maven-source-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-source-plugin |
| Current Version | 2.3 |
| Newer versions | **2.4** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.maven.plugins:maven-surefire-plugin"></a>

### Plugin org.apache.maven.plugins:maven-surefire-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.apache.maven.plugins |
| Artifact Id | maven-surefire-plugin |
| Current Version | 2.17 |
| Newer versions | **2.18** *Next Minor* **2.18.1** *Latest Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.apache.rat:apache-rat-plugin"></a>

### Plugin org.apache.rat:apache-rat-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.apache.rat |
| Artifact Id | apache-rat-plugin |
| Current Version | 0.11 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.codehaus.mojo:clirr-maven-plugin"></a>

### Plugin org.codehaus.mojo:clirr-maven-plugin

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Group Id | org.codehaus.mojo |
| Artifact Id | clirr-maven-plugin |
| Current Version | 2.6.1 |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.codehaus.mojo:cobertura-maven-plugin"></a>

### Plugin org.codehaus.mojo:cobertura-maven-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.codehaus.mojo |
| Artifact Id | cobertura-maven-plugin |
| Current Version | 2.6 |
| Newer versions | **2.7** *Next Minor* |

<a id="archives-0.7-incubating-plugin-updates-report--plugin-org.eluder.coveralls:coveralls-maven-plugin"></a>

### Plugin org.eluder.coveralls:coveralls-maven-plugin

| Status | ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) There is at least one newer minor version available. Minor updates are sometimes passive. |
| --- | --- |
| Group Id | org.eluder.coveralls |
| Artifact Id | coveralls-maven-plugin |
| Current Version | 3.0.1 |
| Newer versions | **3.1.0** *Next Minor* |

---

<a id="archives-0.7-incubating-project-summary"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/project-summary.html -->

<!-- page_index: 43 -->

<a id="archives-0.7-incubating-project-summary--project-summary"></a>

## Project Summary

<a id="archives-0.7-incubating-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Johnzon |
| Description | Apache Johnzon is an implementation of JSR-353 (JavaTM API for JSON Processing). |
| Homepage | <http://incubator.apache.org/projects/johnzon.html> |

<a id="archives-0.7-incubating-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="archives-0.7-incubating-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.johnzon |
| ArtifactId | apache-johnzon |
| Version | 0.8-incubating-SNAPSHOT |
| Type | pom |

---

<a id="archives-0.7-incubating-property-updates-report"></a>

<!-- source_url: https://johnzon.apache.org/archives/0.7-incubating/property-updates-report.html -->

<!-- page_index: 44 -->

<a id="archives-0.7-incubating-property-updates-report--overview"></a>

## Overview

This report summarizes newer versions that may be available for your project's various properties associated with artifacts.

| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | # of properties using the latest version available | 1 |
| --- | --- | --- |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of properties where the next version available is smaller than an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of properties where the next version available is an incremental version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of properties where the next version available is a minor version update | 0 |
| ![](assets/images/icon-warning-sml_cae6181d51ecd3f0.gif) | # of properties where the next version available is a major version update | 0 |

<a id="archives-0.7-incubating-property-updates-report--summary-of-properties-associated-with-artifact-versions"></a>

### Summary of properties associated with artifact versions

| Status | Property | Current Version | Next Version | Next Incremental | Next Minor | Next Major |
| --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/icon-success-sml_17def3475b38b738.gif) | ${jsonspecversion} | 1.0-alpha-1 |  |  |  |  |
| Status | Property | Current Version | Next Version | Next Incremental | Next Minor | Next Major |

<a id="archives-0.7-incubating-property-updates-report--properties-associated-with-artifact-versions"></a>

## Properties associated with artifact versions

<a id="archives-0.7-incubating-property-updates-report--jsonspecversion"></a>

### ${jsonspecversion}

| Status | ![](assets/images/icon-success-sml_17def3475b38b738.gif) No newer versions available. |
| --- | --- |
| Property | ${jsonspecversion} |
| Associated artifacts | org.apache.geronimo.specs:geronimo-json\_1.0\_spec |
| Current Version | 1.0-alpha-1 |
| Allowed version range | [,) |
| Infer associations from project | Yes |
| Only use release versions | No |
| Include projects from reactor | Yes |
| Always use reactor projects (even if older or -SNAPSHOT) | Yes |

---
