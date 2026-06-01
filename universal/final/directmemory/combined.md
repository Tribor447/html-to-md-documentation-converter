# Apache DirectMemory - Project Information

## Navigation

- Apache DirectMemory
  - [About](#index)
  - [Simple Usage](#simple-usage)
  - [Server](#server)
  - [Server Instance](#server-instance)
  - [Javascript Caching](#javascript-caching)
  - [EHCache integration](#ehcache-integration)
  - [Download Release sources](#downloads)
  - [Last Release](#releases-release-notes-0.2)
  - [Releases](#index)
    - [0.2 Release Notes](#releases-release-notes-0.2)
    - [0.1-incubating Release Notes](#releases-release-notes-0.1-incubating)
  - [Apache Lightning](#lightning)
- Get Involved
  - [Issues](#issue-tracking)
  - [Continuous Integration](#integration)
  - [Building Guide](#involved-building)
  - [Committer Environment](#committer-environment)
  - [Release Guide](#involved-release)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Issue Tracking](#issue-tracking)
    - [Continuous Integration](#integration)
    - [Project Modules](#modules)
    - [Project Summary](#project-summary)
- Modules
  - [Apache DirectMemory :: Commons](#directmemory-common)
  - [Apache DirectMemory :: Cache](#directmemory-cache)
  - [Apache DirectMemory :: Tests](#directmemory-tests)
  - [Apache DirectMemory :: Server](#server)
  - [Apache DirectMemory :: Platforms](#platforms)
  - [Apache DirectMemory :: Integrations](#directmemory-integrations)
  - [Apache DirectMemory :: Serializers](#directmemory-serializers)
  - [Apache DirectMemory :: Integration Tests](#itests)
  - [Apache DirectMemory :: Examples](#examples)
  - [Apache Lightning :: Core](#lightning-lightning-core)
  - [Apache Lightning :: Maven Plugin](#lightning-lightning-maven-plugin)
  - [Apache Lightning :: Maven Integration Test](#lightning-lightning-maven-integration-test)
  - [Apache Lightning :: Maven Eclipse Helper](#lightning-lightning-maven-eclipse-helper)
  - [Apache Lightning :: Maven Eclipse Helper Feature](#lightning-lightning-maven-eclipse-helper-feature)
  - [Apache Lightning :: Integration](#lightning-lightning-integration)
  - [Apache DirectMemory :: Server :: Commons](#server-directmemory-server-commons)
  - [Apache DirectMemory :: Server :: Server Implementation](#server-directmemory-server)
  - [Apache DirectMemory :: Server :: Client](#server-directmemory-server-client)
  - [Apache DirectMemory :: Server :: Server Archetype](#server-server-example-archetype)
  - [Apache DirectMemory :: Serializers :: Protobuf](#directmemory-serializers-directmemory-protobuf)
  - [Apache DirectMemory :: Serializers :: Protostuff](#directmemory-serializers-directmemory-protostuff)
  - [Apache DirectMemory :: Serializers :: MessagePack](#directmemory-serializers-directmemory-msgpack)
  - [Apache DirectMemory :: Serializers :: Kryo](#directmemory-serializers-directmemory-kryo)
  - [Apache DirectMemory :: Integrations :: Apache Solr](#directmemory-integrations-directmemory-solr)
  - [Apache DirectMemory :: Integrations :: EHCache](#directmemory-integrations-directmemory-ehcache)
  - [Apache DirectMemory :: Integrations :: Guava](#directmemory-integrations-directmemory-guava)
  - [Apache Lightning :: JGroups Integration](#lightning-lightning-integration-lightning-integration-jgroups)
  - [Apache Lightning :: Spring Integration](#lightning-lightning-integration-lightning-integration-spring)
  - [Apache DirectMemory :: Platforms :: Karaf](#platforms-apache-directmemory)
  - [Apache DirectMemory :: Integration Tests :: OSGi](#itests-osgi)
  - [Apache DirectMemory :: Examples :: Server Javascript](#examples-server-example)
- Other pages
  - [Apache DirectMemory :: Cache - Continuous Integration](#directmemory-cache-integration)
  - [Apache DirectMemory :: Cache - Issue Tracking](#directmemory-cache-issue-tracking)
  - [Apache DirectMemory :: Cache - Project Summary](#directmemory-cache-project-summary)
  - [Apache DirectMemory :: Commons - Continuous Integration](#directmemory-common-integration)
  - [Apache DirectMemory :: Commons - Issue Tracking](#directmemory-common-issue-tracking)
  - [Apache DirectMemory :: Commons - Project Summary](#directmemory-common-project-summary)
  - [Apache DirectMemory :: Integrations :: EHCache - Continuous Integration](#directmemory-integrations-directmemory-ehcache-integration)
  - [Apache DirectMemory :: Integrations :: EHCache - Issue Tracking](#directmemory-integrations-directmemory-ehcache-issue-tracking)
  - [Apache DirectMemory :: Integrations :: EHCache - Project Summary](#directmemory-integrations-directmemory-ehcache-project-summary)
  - [Apache DirectMemory :: Integrations :: Guava - Continuous Integration](#directmemory-integrations-directmemory-guava-integration)
  - [Apache DirectMemory :: Integrations :: Guava - Issue Tracking](#directmemory-integrations-directmemory-guava-issue-tracking)
  - [Apache DirectMemory :: Integrations :: Guava - Project Summary](#directmemory-integrations-directmemory-guava-project-summary)
  - [Apache DirectMemory :: Integrations :: Apache Solr - Continuous Integration](#directmemory-integrations-directmemory-solr-integration)
  - [Apache DirectMemory :: Integrations :: Apache Solr - Issue Tracking](#directmemory-integrations-directmemory-solr-issue-tracking)
  - [Apache DirectMemory :: Integrations :: Apache Solr - Project Summary](#directmemory-integrations-directmemory-solr-project-summary)
  - [Apache DirectMemory :: Integrations - Continuous Integration](#directmemory-integrations-integration)
  - [Apache DirectMemory :: Integrations - Issue Tracking](#directmemory-integrations-issue-tracking)
  - [Apache DirectMemory :: Integrations - Project Modules](#directmemory-integrations-modules)
  - [Apache DirectMemory :: Integrations - Project Summary](#directmemory-integrations-project-summary)
  - [Apache DirectMemory :: Serializers :: Kryo - Continuous Integration](#directmemory-serializers-directmemory-kryo-integration)
  - [Apache DirectMemory :: Serializers :: Kryo - Issue Tracking](#directmemory-serializers-directmemory-kryo-issue-tracking)
  - [Apache DirectMemory :: Serializers :: Kryo - Project Summary](#directmemory-serializers-directmemory-kryo-project-summary)
  - [Apache DirectMemory :: Serializers :: MessagePack - Continuous Integration](#directmemory-serializers-directmemory-msgpack-integration)
  - [Apache DirectMemory :: Serializers :: MessagePack - Issue Tracking](#directmemory-serializers-directmemory-msgpack-issue-tracking)
  - [Apache DirectMemory :: Serializers :: MessagePack - Project Summary](#directmemory-serializers-directmemory-msgpack-project-summary)
  - [Apache DirectMemory :: Serializers :: Protobuf - Continuous Integration](#directmemory-serializers-directmemory-protobuf-integration)
  - [Apache DirectMemory :: Serializers :: Protobuf - Issue Tracking](#directmemory-serializers-directmemory-protobuf-issue-tracking)
  - [Apache DirectMemory :: Serializers :: Protobuf - Project Summary](#directmemory-serializers-directmemory-protobuf-project-summary)
  - [Apache DirectMemory :: Serializers :: Protostuff - Continuous Integration](#directmemory-serializers-directmemory-protostuff-integration)
  - [Apache DirectMemory :: Serializers :: Protostuff - Issue Tracking](#directmemory-serializers-directmemory-protostuff-issue-tracking)
  - [Apache DirectMemory :: Serializers :: Protostuff - Project Summary](#directmemory-serializers-directmemory-protostuff-project-summary)
  - [Apache DirectMemory :: Serializers - Continuous Integration](#directmemory-serializers-integration)
  - [Apache DirectMemory :: Serializers - Issue Tracking](#directmemory-serializers-issue-tracking)
  - [Apache DirectMemory :: Serializers - Project Modules](#directmemory-serializers-modules)
  - [Apache DirectMemory :: Serializers - Project Summary](#directmemory-serializers-project-summary)
  - [Apache DirectMemory :: Tests - Continuous Integration](#directmemory-tests-integration)
  - [Apache DirectMemory :: Tests - Issue Tracking](#directmemory-tests-issue-tracking)
  - [Apache DirectMemory :: Tests - Project Summary](#directmemory-tests-project-summary)
  - [Apache DirectMemory :: Examples - Continuous Integration](#examples-integration)
  - [Apache DirectMemory :: Examples - Issue Tracking](#examples-issue-tracking)
  - [Apache DirectMemory :: Examples - Project Modules](#examples-modules)
  - [Apache DirectMemory :: Examples - Project Summary](#examples-project-summary)
  - [Apache DirectMemory :: Examples :: Server Javascript - Continuous Integration](#examples-server-example-integration)
  - [Apache DirectMemory :: Examples :: Server Javascript - Issue Tracking](#examples-server-example-issue-tracking)
  - [Apache DirectMemory :: Examples :: Server Javascript - Project Summary](#examples-server-example-project-summary)
  - [Apache DirectMemory :: Integration Tests - Continuous Integration](#itests-integration)
  - [Apache DirectMemory :: Integration Tests - Issue Tracking](#itests-issue-tracking)
  - [Apache DirectMemory :: Integration Tests - Project Modules](#itests-modules)
  - [Apache DirectMemory :: Integration Tests :: OSGi - Continuous Integration](#itests-osgi-integration)
  - [Apache DirectMemory :: Integration Tests :: OSGi - Issue Tracking](#itests-osgi-issue-tracking)
  - [Apache DirectMemory :: Integration Tests :: OSGi - Project Summary](#itests-osgi-project-summary)
  - [Apache DirectMemory :: Integration Tests - Project Summary](#itests-project-summary)
  - [Apache Lightning - Continuous Integration](#lightning-integration)
  - [Apache Lightning - Issue Tracking](#lightning-issue-tracking)
  - [Apache Lightning :: Core - Continuous Integration](#lightning-lightning-core-integration)
  - [Apache Lightning :: Core - Issue Tracking](#lightning-lightning-core-issue-tracking)
  - [Apache Lightning :: Core - Project Summary](#lightning-lightning-core-project-summary)
  - [Apache Lightning :: Integration - Continuous Integration](#lightning-lightning-integration-integration)
  - [Apache Lightning :: Integration - Issue Tracking](#lightning-lightning-integration-issue-tracking)
  - [Apache Lightning :: JGroups Integration - Continuous Integration](#lightning-lightning-integration-lightning-integration-jgroups-integration)
  - [Apache Lightning :: JGroups Integration - Issue Tracking](#lightning-lightning-integration-lightning-integration-jgroups-issue-tracking)
  - [Apache Lightning :: JGroups Integration - Project Summary](#lightning-lightning-integration-lightning-integration-jgroups-project-summary)
  - [Apache Lightning :: JGroups Integration - Sonar](#lightning-lightning-integration-lightning-integration-jgroups-sonar)
  - [Apache Lightning :: Spring Integration - Continuous Integration](#lightning-lightning-integration-lightning-integration-spring-integration)
  - [Apache Lightning :: Spring Integration - Issue Tracking](#lightning-lightning-integration-lightning-integration-spring-issue-tracking)
  - [Apache Lightning :: Spring Integration - Project Summary](#lightning-lightning-integration-lightning-integration-spring-project-summary)
  - [Apache Lightning :: Spring Integration - Sonar](#lightning-lightning-integration-lightning-integration-spring-sonar)
  - [Apache Lightning :: Integration - Project Modules](#lightning-lightning-integration-modules)
  - [Apache Lightning :: Integration - Project Summary](#lightning-lightning-integration-project-summary)
  - [Apache Lightning :: Maven Eclipse Helper Feature - Continuous Integration](#lightning-lightning-maven-eclipse-helper-feature-integration)
  - [Apache Lightning :: Maven Eclipse Helper Feature - Issue Tracking](#lightning-lightning-maven-eclipse-helper-feature-issue-tracking)
  - [Apache Lightning :: Maven Eclipse Helper Feature - Project Summary](#lightning-lightning-maven-eclipse-helper-feature-project-summary)
  - [Apache Lightning :: Maven Eclipse Helper Feature - Sonar](#lightning-lightning-maven-eclipse-helper-feature-sonar)
  - [Apache Lightning :: Maven Eclipse Helper - Continuous Integration](#lightning-lightning-maven-eclipse-helper-integration)
  - [Apache Lightning :: Maven Eclipse Helper - Issue Tracking](#lightning-lightning-maven-eclipse-helper-issue-tracking)
  - [Apache Lightning :: Maven Eclipse Helper - Project Summary](#lightning-lightning-maven-eclipse-helper-project-summary)
  - [Apache Lightning :: Maven Eclipse Helper - Sonar](#lightning-lightning-maven-eclipse-helper-sonar)
  - [Apache Lightning :: Maven Integration Test - Continuous Integration](#lightning-lightning-maven-integration-test-integration)
  - [Apache Lightning :: Maven Integration Test - Issue Tracking](#lightning-lightning-maven-integration-test-issue-tracking)
  - [Apache Lightning :: Maven Integration Test - Project Summary](#lightning-lightning-maven-integration-test-project-summary)
  - [Apache Lightning :: Maven Integration Test - Sonar](#lightning-lightning-maven-integration-test-sonar)
  - [Apache Lightning :: Maven Plugin - Continuous Integration](#lightning-lightning-maven-plugin-integration)
  - [Apache Lightning :: Maven Plugin - Issue Tracking](#lightning-lightning-maven-plugin-issue-tracking)
  - [Apache Lightning :: Maven Plugin - Project Summary](#lightning-lightning-maven-plugin-project-summary)
  - [Apache Lightning - Project Modules](#lightning-modules)
  - [Apache Lightning - Project Summary](#lightning-project-summary)
  - [Apache DirectMemory :: Platforms :: Karaf - Continuous Integration](#platforms-apache-directmemory-integration)
  - [Apache DirectMemory :: Platforms :: Karaf - Issue Tracking](#platforms-apache-directmemory-issue-tracking)
  - [Apache DirectMemory :: Platforms :: Karaf - Project Summary](#platforms-apache-directmemory-project-summary)
  - [Apache DirectMemory :: Platforms - Continuous Integration](#platforms-integration)
  - [Apache DirectMemory :: Platforms - Issue Tracking](#platforms-issue-tracking)
  - [Apache DirectMemory :: Platforms - Project Modules](#platforms-modules)
  - [Apache DirectMemory :: Platforms - Project Summary](#platforms-project-summary)
  - [Apache DirectMemory :: Server :: Client - Continuous Integration](#server-directmemory-server-client-integration)
  - [Apache DirectMemory :: Server :: Client - Issue Tracking](#server-directmemory-server-client-issue-tracking)
  - [Apache DirectMemory :: Server :: Client - Project Summary](#server-directmemory-server-client-project-summary)
  - [Apache DirectMemory :: Server :: Client - Sonar](#server-directmemory-server-client-sonar)
  - [Apache DirectMemory :: Server :: Commons - Continuous Integration](#server-directmemory-server-commons-integration)
  - [Apache DirectMemory :: Server :: Commons - Issue Tracking](#server-directmemory-server-commons-issue-tracking)
  - [Apache DirectMemory :: Server :: Commons - Project Summary](#server-directmemory-server-commons-project-summary)
  - [Apache DirectMemory :: Server :: Commons - Sonar](#server-directmemory-server-commons-sonar)
  - [Apache DirectMemory :: Server :: Server Implementation - Continuous Integration](#server-directmemory-server-integration)
  - [Apache DirectMemory :: Server :: Server Implementation - Issue Tracking](#server-directmemory-server-issue-tracking)
  - [Apache DirectMemory :: Server :: Server Implementation - Project Summary](#server-directmemory-server-project-summary)
  - [Apache DirectMemory :: Server - Continuous Integration](#server-integration)
  - [Apache DirectMemory :: Server - Issue Tracking](#server-issue-tracking)
  - [Apache DirectMemory :: Server - Project Modules](#server-modules)
  - [Apache DirectMemory :: Server - Project Summary](#server-project-summary)
  - [Apache DirectMemory :: Server :: Server Archetype - Continuous Integration](#server-server-example-archetype-integration)
  - [Apache DirectMemory :: Server :: Server Archetype - Issue Tracking](#server-server-example-archetype-issue-tracking)
  - [Apache DirectMemory :: Server :: Server Archetype - Project Summary](#server-server-example-archetype-project-summary)

## Content

<a id="index"></a>

<!-- source_url: https://directmemory.apache.org/index.html -->

<!-- page_index: 1 -->

# Apache DirectMemory - Apache DirectMemory Home

![](assets/images/apache-directmemory-logo-medium_9d9ffb8391e37e59.png)

Apache DirectMemory is a off-heap cache for the Java Virtual Machine.

Last release 0.2 - 2013-09-17. See [release notes](#releases-release-notes-0.2).

---

<a id="simple-usage"></a>

<!-- source_url: https://directmemory.apache.org/simple-usage.html -->

<!-- page_index: 2 -->

<a id="simple-usage--directmemory-simple-usage"></a>

## DirectMemory Simple Usage

Add a dependency to the DirectMemory cache artifact:

```
  <dependency>
    <groupId>org.apache.directmemory</groupId>
    <artifactId>directmemory-cache</artifactId>
    <version>0.2</version>
  </dependency>
```

Create your [CacheService](https://directmemory.apache.org/apidocs/reference/org/apache/directmemory/cache/CacheService.html) instance:

```
  CacheService<Object, Object> cacheService = new DirectMemory<Object, Object>()
    .setNumberOfBuffers( 10 )
    .setSize( 1000 )
    .setInitialCapacity( 100000 )
    .setConcurrencyLevel( 4 )
    .newCacheService();
```

Use the cache service to store object, Those methods returns a [Pointer](https://directmemory.apache.org/apidocs/reference/org/apache/directmemory/memory/Pointer.html) if this pointer is null your object has not been stored:

```
  put( K key, V value )
  put( K key, V value, int expiresIn )
```

Retrieve an Object from the cache service:

```
  V retrieve( K key );
```

Clear at the end of usage and close the CacheService

```
  cacheService.clear();
  cacheService.close(); // close() is available in 0.2+ only
```

---

<a id="server"></a>

<!-- source_url: https://directmemory.apache.org/server.html -->

<!-- page_index: 3 -->

# Apache DirectMemory - Apache DirectMemory Server Side

- [DirectMemory Server](#server--directmemory_server)
- [Exchange formats](#server--exchange_formats)
  - [HTTP Methods](#server--http_methods)
  - [PUT/POST](#server--putpost)
  - [GET](#server--get)
  - [DELETE](#server--delete)
  - [Http Headers](#server--http_headers)
- [JSON Exchange](#server--json_exchange)
  - [JSON PUT Content](#server--json_put_content)
  - [JSON GET Content](#server--json_get_content)
  - [JSON DELETE Content](#server--json_delete_content)
- [Binary Exchange](#server--binary_exchange)
  - [Binary PUT Content](#server--binary_put_content)
  - [Binary GET Content](#server--binary_get_content)
  - [Binary DELETE Content](#server--binary_delete_content)
- [text/plain Exchange](#server--textplain_exchange)
  - [text/plain PUT Content](#server--textplain_put_content)
  - [text/plain GET Content](#server--textplain_get_content)
  - [text/plain DELETE Content](#server--textplain_delete_content)
- [Java Client API](#server--java_client_api)
  - [Client Configuration](#server--client_configuration)
  - [PUT Content](#server--put_content)
  - [GET Content](#server--get_content)
  - [DELETE Content](#server--delete_content)

<a id="server--directmemory-server"></a>

## DirectMemory Server

Apache DirectMemory has a server implementation (a servlet) to provide you a way to store your project remotely and to share those cached objects with various applications.

Server side and client side (Java only) are provided.

The exchange are based on http(s) exchange with the following implementations/format:

- JSON format
- "binary" format: parameters are send via http headers
- text/plain format: you can send a text value(json object, xml etc..), the server will serialize the content and store it for you.

<a id="server--exchange-formats"></a>

## Exchange formats

We simply use HTTP method names to resolve the action to proceed and depends on the Accept or Content-Type headers the format will be different :

- GET to retrieve content ${webPath}/${key}
- DELETE to delete content ${webPath}/${key}
- PUT/POST to add some content in cache ${webPath}/${key}

<a id="server--http-methods"></a>

### HTTP Methods

<a id="server--put-post"></a>

### PUT/POST

PUT/POST are used for adding/updating content in cache.
Note: if the content was not put in cache, you will receive a 204 (Not Content)

<a id="server--get"></a>

### GET

GET is used to retrieve content from the cache.
**If not content is found for the key, you will receive the http code 204 (No content)**

<a id="server--delete"></a>

### DELETE

DELETE is used to removed content from cache
Note: if the entry was not available in the server you will receive a 204 (Not Content)

<a id="server--http-headers"></a>

### Http Headers

see various exchange type for dedicated http headers

Common http headers:

- X-DirectMemory-SerializeSize: returns bytes number stored on server side.

<a id="server--json-exchange"></a>

## JSON Exchange

<a id="server--json-put-content"></a>

### JSON PUT Content

JSON Request to put content in cache Content-Type: application/json

```

  {"expiresIn":123,
    "cacheContent":"rO0ABXNydmEvbGFuZy9TdHJpbmc7eHB0AAhCb3JkZWF1eA=="}
          
```

To put this content in DirectMemory Cache Server, just use a PUT request on path ${webPath}/DirectMemoryServlet/${key}.

<a id="server--json-get-content"></a>

### JSON GET Content

Use a GET request on ${webPath}/DirectMemoryServlet/${key} and you will receive the JSON response:

```

            {"key":"foo","cacheContent":"Zm9vIGJhcg=="}
          
```

<a id="server--json-delete-content"></a>

### JSON DELETE Content

Use a DELETE request on ${webPath}/DirectMemoryServlet/${key}.

<a id="server--binary-exchange"></a>

## Binary Exchange

<a id="server--binary-put-content"></a>

### Binary PUT Content

PUT Request to put content in cache Content-Type: application/x-java-serialized-object.
To put this content in DirectMemory Cache Server, just use a PUT request on path ${webPath}/DirectMemoryServlet/${key}.
ExpiresIn value can be set with http header: X-DirectMemory-ExpiresIn
The http request body will contains the serialized object value.

<a id="server--binary-get-content"></a>

### Binary GET Content

Use a GET request on ${webPath}/DirectMemoryServlet/${key} and you will receive the binary form of the object.

<a id="server--binary-delete-content"></a>

### Binary DELETE Content

Use a DELETE request on ${webPath}/DirectMemoryServlet/${key}.

<a id="server--text-plain-exchange"></a>

## text/plain Exchange

<a id="server--text-plain-put-content"></a>

### text/plain PUT Content

PUT Request to put content in cache Content-Type: text/plain.
To put this content in DirectMemory Cache Server, just use a PUT request on path ${webPath}/DirectMemoryServlet/${key}.
ExpiresIn value can be set with http header: X-DirectMemory-ExpiresIn
The http request body will contains a String value which will be serialized on server side and stored in directMemory.
You can specify the Serializer to use with the http header: "X-DirectMemory-Serializer" (must contains the full class name).

<a id="server--text-plain-get-content"></a>

### text/plain GET Content

Use a GET request on ${webPath}/DirectMemoryServlet/${key} and you will receive the stored String.

<a id="server--text-plain-delete-content"></a>

### text/plain DELETE Content

Use a DELETE request on ${webPath}/DirectMemoryServlet/${key}.

<a id="server--java-client-api"></a>

## Java Client API

<a id="server--client-configuration"></a>

### Client Configuration

Before using the client api, you must configure it using the following pattern:

```
        DirectMemoryClientConfiguration configuration =
            new DirectMemoryClientConfiguration()
                .setHost( "localhost" )
                .setPort( port )
                .setHttpPath( "/direct-memory/DirectMemoryServlet" )
                .setSerializer( SerializerFactory.createNewSerializer() )
                .setHttpClientClassName( httpClientClassName )
                .setExchangeType( getExchangeType() );

        client = DirectMemoryClientBuilder.newBuilder( configuration ).buildClient();

        // or

        client = DirectMemoryClientBuilder
            .newBuilder()
            .toHost( "localhost" )
            .onPort( port )
            .toHttpPath( "/direct-memory/DirectMemoryServlet" )
            .withSerializer( SerializerFactory.createNewSerializer() )
            .forExchangeType( getExchangeType() )
            .withHttpClientClassName( httpClientClassName )
            .buildClient();
```

Here you have a configured client. Have a look at DirectMemoryServerClientConfiguration javadoc for advanced options.

<a id="server--put-content"></a>

### PUT Content

With the Java client is something like:

```

        Wine bordeaux = new Wine( "Bordeaux", "very great wine" );
        assertTrue( client.put( new DirectMemoryRequest<Wine>( "bordeaux", bordeaux ) ).isStored() );
```

<a id="server--get-content"></a>

### GET Content

With the Java api:

```
        DirectMemoryRequest rq = new DirectMemoryRequest( "bordeaux", Wine.class );

        DirectMemoryResponse<Wine> response = client.retrieve( rq );

        assertTrue( response.isFound() );
        Wine wine = response.getResponse();
```

You must check the method (response.isFound()) if true retrieve the object with: Wine wine = response.getResponse();

<a id="server--delete-content"></a>

### DELETE Content

With the Java api:

```

        DirectMemoryResponse deleteResponse = client.delete( new DirectMemoryRequest<Wine>( "bordeaux" ) );
        assertTrue( deleteResponse.isDeleted() );
```

---

<a id="server-instance"></a>

<!-- source_url: https://directmemory.apache.org/server-instance.html -->

<!-- page_index: 4 -->

<a id="server-instance--create-your-server-instance"></a>

## Create your server instance

In order to create a war file to serve a DirectMemory instance, you can:

- package in a maven war project type
- create it from the archetype

<a id="server-instance--server-configuration"></a>

### Server Configuration

In the first release, the DirectMemory Server use a single instance of DirectMemory cache and configured via System Properties:

- numberOfBuffers: "directMemory.numberOfBuffers" (default: 10)
- size: "directMemory.size" (default: 1000)
- initialCapacity: "directMemory.initialCapacity" (default: 100000)
- concurrencyLevel: "directMemory.concurrencyLevel" (default: 4)

<a id="server-instance--maven-war-project"></a>

### Maven War project

Add a dependency to the server core artifact:

```
  <dependency>
    <groupId>org.apache.directmemory.server</groupId>
    <artifactId>directmemory-server</artifactId>
    <version>0.2</version>
  </dependency>
```

Map the DirectMemory servlet in your web.xml:

```
  <servlet>
    <servlet-name>DirectMemoryServlet</servlet-name>
    <servlet-class>org.apache.directmemory.server.services.DirectMemoryServlet</servlet-class>
    <load-on-startup>1</load-on-startup>
  </servlet>

  <servlet-mapping>
    <servlet-name>DirectMemoryServlet</servlet-name>
    <url-pattern>/cache/*</url-pattern>
  </servlet-mapping>
```

<a id="server-instance--create-from-archetype"></a>

### Create from archetype

Use the following command line.

```
mvn archetype:generate \
   -DarchetypeGroupId=org.apache.directmemory.server \
   -DarchetypeArtifactId=server-example-archetype \
   -DarchetypeVersion=0.2
```

If you want to use a SNAPSHOT version you must add: -DarchetypeRepository=https://repository.apache.org/content/repositories/snapshots/

Now you have a simple war project configured to be a DirectMemory Server.

Try the provided sample with running mvn tomcat7:run and hit your browser to http://localhost:9091/dm/

---

<a id="javascript-caching"></a>

<!-- source_url: https://directmemory.apache.org/javascript-caching.html -->

<!-- page_index: 5 -->

<a id="javascript-caching--javascript-caching-with-directmemory"></a>

## Javascript caching with DirectMemory

First you must have a server instance installed and available see [server instance](#server-instance). Sample here are based on using JQuery library.

Now you will be able to store/get/delete your json objects in an Apache DirectMemory instance.

- [Store your object](#javascript-caching--store_your_object)
- [Get your object](#javascript-caching--get_your_object)
- [Delete your object](#javascript-caching--delete_your_object)

<a id="javascript-caching--store-your-object"></a>

### Store your object

Note the header X-DirectMemory-ExpiresIn to specify the ttl value in ms.

```
putObjectInCache=function(key,javascriptBean,expiresIn,serializer){$.ajax({url: 'cache/'+encodeURIComponent(key),data:JSON.stringify( javascriptBean ),cache: false,type: 'PUT',headers:{'X-DirectMemory-ExpiresIn':expiresIn,'X-DirectMemory-Serializer':serializer},contentType: "text/plain",statusCode: {204: function() {displayWarning("not put in cache"); },200:function( data, textStatus, jqXHR ) {var size = jqXHR.getResponseHeader('X-DirectMemory-SerializeSize'); displayInfo('put in cache with key:'+key+ " bytes stored:"+size);
},500:function(data){displayError("error put in cache");}} });}
```

<a id="javascript-caching--get-your-object"></a>

### Get your object

```
$.ajax({url: 'cache/'+encodeURIComponent(key),cache: false,type: 'GET',headers:{'X-DirectMemory-Serializer':$("#serializer" ).val()},dataType: 'text',statusCode: {204: function() {displayWarning("not found in cache"); },200:function( data ) {var wine = $.parseJSON(data); displayInfo('get from cache with key:'+key+",value:"+wine.description); },500:function(data){displayError("error get from cache");}} });
```

<a id="javascript-caching--delete-your-object"></a>

### Delete your object

```
deleteFromCache=function(key){$.ajax({url: 'cache/'+encodeURIComponent(key),cache: false,type: 'DELETE',dataType: 'text',statusCode: {204: function() {displayWarning("not found in cache"); },200:function( data ) {displayInfo(' key '+key+ ' deleted from cache'); },500:function(data){displayError("error delete from cache");}} });}
```

---

<a id="ehcache-integration"></a>

<!-- source_url: https://directmemory.apache.org/ehcache-integration.html -->

<!-- page_index: 6 -->

<a id="ehcache-integration--ehcache-integration"></a>

## EHCache Integration

You can mix the use of the ehcache framework with DirectMemory. Recent versions of ehcache have some features to store elements in a heap off storage when overflow a number of objects or bytes in heap cache.

First you need to declare dependency to the DirectMemory ehcache integration:

```
  <dependency>
    <groupId>org.apache.directmemory</groupId>
    <artifactId>directmemory-ehcache</artifactId>
    <version>0.2</version>
  </dependency>
```

Note the heap off cache class to use is not currently configurable in ehcahce see issue <https://jira.terracotta.org/jira/browse/EHC-940>. So Apache DirectMemory contains same package/class name as needed by ehcache.

Activate the feature in ehcache:

```
  CacheConfiguration cacheConfiguration = new CacheConfiguration();
  cacheConfiguration.setName( "foo" );

  cacheConfiguration.setOverflowToOffHeap( true );

  cacheConfiguration.setMaxBytesLocalHeap( Long.valueOf( 100 * 1024 * 1024 ) );
  cacheConfiguration.setMaxBytesLocalOffHeap( Long.valueOf( 100 * 1024 * 1024 ) );

  Cache cache = new Cache( cacheConfiguration );
  CacheManager.getInstance().addCache( cache );
```

---

<a id="downloads"></a>

<!-- source_url: https://directmemory.apache.org/downloads.html -->

<!-- page_index: 7 -->

<a id="downloads--introduction"></a>

## Introduction

Apache DirectMemory artifacts are distributed in source and binary form under the terms of the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
See the included LICENSE and NOTICE files included in each artifact for additional license
information.

Use the links below to download a source distribution of Apache DirectMemory.
It is good practice to [verify the integrity](#downloads--verifying_releases) of the distribution files.

<a id="downloads--last-release"></a>

## Last Release

<a id="downloads--0.2"></a>

### 0.2

Release date: 2013-09-17

[Release notes](#releases-release-notes-0.2)

| Artifact | Signatures |
| --- | --- |
| [apache-directmemory-0.2-source-release.zip](http://www.apache.org/dyn/closer.cgi/directmemory/0.2/apache-directmemory-0.2-source-release.zip) | [asc](http://www.apache.org/dist/directmemory/0.2/apache-directmemory-0.2-source-release.zip.asc) [md5](http://www.apache.org/dist/directmemory/0.2/apache-directmemory-0.2-source-release.zip.md5) [sha1](http://www.apache.org/dist/directmemory/0.2/apache-directmemory-0.2-source-release.zip.sha1) |

<a id="downloads--verifying-releases"></a>

## Verifying Releases

We strongly recommend you verify the integrity of the downloaded files with both PGP and MD5.

The PGP signatures can be verified using [PGP](http://www.pgpi.org/) or
[GPG](http://www.gnupg.org/).
First download the [KEYS](http://apache.org/dist/directmemory/KEYS) as well as the
\*.asc signature file for the particular distribution. Make sure you get these files from the main
distribution directory, rather than from a mirror. Then verify the signatures using one of the following sets of
commands:

```
$ pgpk -a KEYS
$ pgpv directmemory-*.tar.gz.asc
$ pgpv directmemory-*.zip.asc
```

```
$ pgp -ka KEYS
$ pgp directmemory-*.tar.gz.asc
$ pgp directmemory-*.zip.asc
```

```
$ gpg --import KEYS
$ gpg --verify directmemory-*.tar.gz.asc
$ gpg --verify directmemory-*.zip.asc
```

Alternatively, you can verify the MD5 signature on the files. A Unix/Linux program called
md5 or
md5sum is included in most distributions. It is also available as part of
[GNU Textutils](http://www.gnu.org/software/textutils/textutils.html).
Windows users can get binary md5 programs from these (and likely other) places:

- <http://www.md5summer.org/>
- <http://www.fourmilab.ch/md5/>
- <http://www.pc-tools.net/win32/md5sums/>

---

<a id="releases-release-notes-0.2"></a>

<!-- source_url: https://directmemory.apache.org/releases/release-notes-0.2.html -->

<!-- page_index: 8 -->

<a id="releases-release-notes-0.2--apache-directmemory-0.2"></a>

## Apache DirectMemory 0.2

The Apache DirectMemory Team would like to announce the 0.2 release.

Apache DirectMemory is a multi layered cache implementation featuring off-heap memory management to enable efficient handling of a large number of java objects without affecting jvm garbage collection performance

It's a technology preview release. So some APIs can be change in the future.

We hope you enjoy using Apache DirectMemory! If you have any questions, please consult:

- the web site: <http://directmemory.apache.org//>
- the directmemory-user mailing list: <http://directmemory.apache.org/mail-lists.html>

Release date: 2013-09-15.

<a id="releases-release-notes-0.2--apache-directmemory-0.2-release-notes"></a>

### Apache DirectMemory 0.2 release notes

<a id="releases-release-notes-0.2--improvement"></a>

#### Improvement

- [DIRECTMEMORY-28] - Create an alternative MemoryService using sun.misc.Unsafe
- [DIRECTMEMORY-69] - Expose InputStream and OutputStream Interfaces instead of internal Pointer.directBuffer
- [DIRECTMEMORY-104] - Precise correct DirectMemory usage and fix typo in documentation
- [DIRECTMEMORY-124] - Create an utility class Iterable*V* over Cache*K,V*
- [DIRECTMEMORY-125] - General code improvements
- [DIRECTMEMORY-131] - Using DirectMemory as level 2 cache for Guava Cache

<a id="releases-release-notes-0.2--new-feature"></a>

#### New Feature

- [DIRECTMEMORY-60] - EHCache Integration

<a id="releases-release-notes-0.2--bug"></a>

#### Bug

- [DIRECTMEMORY-49] - MemoryManagerService.update does not reuse the same pointer
- [DIRECTMEMORY-57] - Pointer.free should be atomic / thread safe
- [DIRECTMEMORY-82] - CacheService should implement Closable / Review the livecycle of the CacheService/MemoryService/ByteBufferAllocator objects
- [DIRECTMEMORY-103] - Add Kryo serializer
- [DIRECTMEMORY-105] - Kryo Serializer adapter isn't threadsafe
- [DIRECTMEMORY-126] - upgrade to ehcache 2.6.6
- [DIRECTMEMORY-127] - ehcache integration OSGI tests no longer work
- [DIRECTMEMORY-128] - Mark aspectj package import as optional and other Import-Package fixes
- [DIRECTMEMORY-129] - Kryo serializer usage is not thread safe
- [DIRECTMEMORY-130] - MemoryManagerService does not reset the used memory count to zero in clear
- [DIRECTMEMORY-132] - incorrect case name in bench.sh
- [DIRECTMEMORY-133] - "DirectMemory Simple Usage" doc improvement

---

<a id="releases-release-notes-0.1-incubating"></a>

<!-- source_url: https://directmemory.apache.org/releases/release-notes-0.1-incubating.html -->

<!-- page_index: 9 -->

<a id="releases-release-notes-0.1-incubating--apache-directmemory-0.1-incubating"></a>

## Apache DirectMemory 0.1-incubating

The Apache DirectMemory Team would like to announce the 0.1-incubating release.

Apache DirectMemory is a multi layered cache implementation featuring off-heap memory management to enable efficient handling of a large number of java objects without affecting jvm garbage collection performance

It's a technology preview release. So some APIs can be change in the future.

We hope you enjoy using Apache DirectMemory! If you have any questions, please consult:

- the web site: <http://directmemory.apache.org//>
- the directmemory-user mailing list: <http://directmemory.apache.org/mail-lists.html>

Release date: 2012-07-09.

<a id="releases-release-notes-0.1-incubating--apache-directmemory-0.1-incubating-release-notes"></a>

### Apache DirectMemory 0.1-incubating release notes

<a id="releases-release-notes-0.1-incubating--new-feature"></a>

#### New Feature

- [DIRECTMEMORY-37] - Update the MemoryManager API so it can be used in conjunction with NIO to provide efficient buffer management
- [DIRECTMEMORY-61] - Create Server module to receive data to cache and a client api to send datas to cache
- [DIRECTMEMORY-62] - Adopt fluent APIs for bootstrapping the Cache (and optionally manage stored objects)

<a id="releases-release-notes-0.1-incubating--improvement"></a>

#### Improvement

- [DIRECTMEMORY-12] - package DirectMemory as a OSGI bundle
- [DIRECTMEMORY-16] - Create a non Singleton MemoryStorage alternative
- [DIRECTMEMORY-19] - Remove deprecated MethodRule from unit tests (use @Rule)
- [DIRECTMEMORY-20] - Remove @SuppressWarnings("rawtypes","unchecked" from serializers and fix style
- [DIRECTMEMORY-27] - Upgrade to protostuff 1.0.4 and switch again to off-heap buffer
- [DIRECTMEMORY-39] - Create an 'example' module
- [DIRECTMEMORY-40] - Pointers merging with adjacent free pointers when freeing.
- [DIRECTMEMORY-42] - OffHeapMemoryBuffer store, allocate and free function's parameters consistency
- [DIRECTMEMORY-43] - Cache should allow key objects instead of plain string
- [DIRECTMEMORY-48] - Add OffHeapMemoryBuffer interface and abstraction
- [DIRECTMEMORY-53] - MemoryManagerService buffers allocation policy
- [DIRECTMEMORY-56] - Moving unused class from org.apache.directmemory.serialization to test
- [DIRECTMEMORY-58] - OffHeapMemoryBuffer.allocate should return a ByteBuffer with capacity = limit = allocatedSize to avoid overwriting
- [DIRECTMEMORY-67] - Serializer Factory should be able to load specific serializers
- [DIRECTMEMORY-71] - SerializerFactory#createNewSerializer( Class*S*|String ) should throw appropriate exceptions instead of returning null
- [DIRECTMEMORY-72] - Pointer should be an interface
- [DIRECTMEMORY-75] - Create a CacheService builder to simplify the bootstrap process
- [DIRECTMEMORY-77] - Make MemoryManagerServiceWithAllocationPolicyImpl the default MemoryManagerService implementation
- [DIRECTMEMORY-78] - Completely remove the deprecated OffHeapMemoryBuffer
- [DIRECTMEMORY-80] - Build fails on Windows
- [DIRECTMEMORY-89] - Update DM-Solr integration to user Solr 3.6
- [DIRECTMEMORY-90] - Add OSGi support for directmemory-ehcache integration.
- [DIRECTMEMORY-91] - Add OSGi support for directmemory-solr

<a id="releases-release-notes-0.1-incubating--bug"></a>

#### Bug

- [DIRECTMEMORY-17] - Element Eviction/Expiry issue
- [DIRECTMEMORY-18] - The expiry value is not passed to the underlying store to check the expiry of the element.
- [DIRECTMEMORY-46] - OffHeapMemoryBuffer.free do an unnecessary pointers.add
- [DIRECTMEMORY-47] - OffHeapMemoryBuffer.allocate need to be synchronized
- [DIRECTMEMORY-54] - OffHeapMemoryBuffer.clear should set to free all pointers to avoid misusage
- [DIRECTMEMORY-55] - OffHeapMemoryBuffer leaks 1 byte at every allocation
- [DIRECTMEMORY-59] - Fix statistics code for SolrOffHeapCache in examples module
- [DIRECTMEMORY-68] - Standard Serializer is broken under OSGi
- [DIRECTMEMORY-73] - NPE on put method in CacheServiceImpl when cache is full.
- [DIRECTMEMORY-81] - Disposal process run only once
- [DIRECTMEMORY-85] - Method to format in Gb has a typo
- [DIRECTMEMORY-86] - Tomcat is never stopped during the server tests
- [DIRECTMEMORY-87] - collectExpired frees not expired items instead of expired ones
- [DIRECTMEMORY-88] - Unable to retrieve JDK types (Integer, byte, ..) with the StandardSerializer
- [DIRECTMEMORY-93] - There is a typo in the ehcache feature of directmemory
- [DIRECTMEMORY-94] - directmemory-solr fails to resolve in some cases

<a id="releases-release-notes-0.1-incubating--task"></a>

#### Task

- [DIRECTMEMORY-1] - Import the codebase
- [DIRECTMEMORY-2] - Create Website for URL http://incubator.apache.org/directmemory/
- [DIRECTMEMORY-3] - Remove Dependencies from SVN
- [DIRECTMEMORY-4] - Remove eclipse project files
- [DIRECTMEMORY-5] - Remove Generated Classes from SVN
- [DIRECTMEMORY-6] - Change Package Names to get adopted
- [DIRECTMEMORY-38] - Add "TM" to project logos
- [DIRECTMEMORY-45] - Add (TM) symbol to the project logo

<a id="releases-release-notes-0.1-incubating--test"></a>

#### Test

- [DIRECTMEMORY-29] - Fix a payload size assertion in MemoryManagerTests.smokeTest()

<a id="releases-release-notes-0.1-incubating--wish"></a>

#### Wish

- [DIRECTMEMORY-65] - put vs update - not consistent

<a id="releases-release-notes-0.1-incubating--sub-task"></a>

#### Sub-task

- [DIRECTMEMORY-22] - Add OSGi integration test for directmemory
- [DIRECTMEMORY-23] - Provide a feature descriptor for Karaf

---

<a id="lightning"></a>

<!-- source_url: https://directmemory.apache.org/lightning/ -->

<!-- page_index: 10 -->

<a id="lightning--about-apache-lightning"></a>

## About Apache Lightning

Lightning fast Java Serialization

---

<a id="issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/issue-tracking.html -->

<!-- page_index: 11 -->

<a id="issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="integration"></a>

<!-- source_url: https://directmemory.apache.org/integration.html -->

<!-- page_index: 12 -->

<a id="integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="involved-building"></a>

<!-- source_url: https://directmemory.apache.org/involved/building.html -->

<!-- page_index: 13 -->

<a id="involved-building--build-apache-directmemory"></a>

## Build Apache DirectMemory

TODO

---

<a id="committer-environment"></a>

<!-- source_url: https://directmemory.apache.org/committer-environment.html -->

<!-- page_index: 14 -->

<a id="committer-environment--introduction"></a>

## Introduction

This document is intended to set up the Apache DirectMemory committer environment.

<a id="committer-environment--source-file-encoding"></a>

## Source File Encoding

When editing source files, make sure you use the right file encoding. For the Apache DirectMemory project, UTF-8 has been chosen as the default file encoding. UTF-8 is an encoding scheme for the Unicode character set and as such allows to encode all characters that Java can handle. The source files should not contain the byte order mark (BOM). There can be exceptions to this general rule, e.g. properties files are usually encoded using ISO-8859-1 as per the JRE API, so please keep this in mind, too.

<a id="committer-environment--subversion-configuration"></a>

## Subversion Configuration

Before committing files in subversion repository, you need to read the [Committer Subversion Access](http://www.apache.org/dev/version-control.html#https-svn) document and you must set your svn client with this properties file: [svn-eol-style.txt](https://directmemory.apache.org/svn-eol-style.txt)

<a id="committer-environment--directmemory-code-style"></a>

## DirectMemory Code Style

The following sections show how to set up the code style for DirectMemory in IDEA and Eclipse. It is strongly preferred that patches use this style before they are supplied.

<a id="committer-environment--intellij-idea-4.5"></a>

### IntelliJ IDEA 4.5+

Download [directmemory-idea-codestyle.xml](assets/files/directmemory-idea-codestyle_3c70ce821a1c6bf8.xml) and copy it to ~/.IntelliJIDEA/config/codestyles then restart IDEA. On Windows, try C:\Documents and Settings\<username>\.IntelliJIDEA\config\codestyles

After this, restart IDEA and open the settings to select the new code style.

<a id="committer-environment--eclipse-3.2"></a>

### Eclipse 3.2+

Download [directmemory-eclipse-codestyle.xml](assets/files/directmemory-eclipse-codestyle_c4c31c70e7d1e367.xml).

After this, select Window > Preferences, and open up the configuration for Java > Code Style > Code Formatter. Click on the button labeled Import... and select the file you downloaded. Give the style a name, and click OK.

---

<a id="involved-release"></a>

<!-- source_url: https://directmemory.apache.org/involved/release.html -->

<!-- page_index: 15 -->

<a id="involved-release--apache-directmemory-release-process"></a>

## Apache DirectMemory release process

1. Post to the dev list a few days before you plan to do a release
2. Your maven setting must contains the entry to be able to deploy.

   ~/.m2/settings.xml


```
   <server>
     <id>apache.releases.https</id>
     <username></username>
     <password></password>
   </server>
```

3. Release You should have a GPG agent running in the session you will run the maven release commands(preferred), and confirm it works by running "gpg -ab" (type some text and press Ctrl-D). If you do not have a GPG agent running, make sure that you have the "apache-release" profile set in your settings.xml as shown below.

   Run the release


```
mvn release:prepare release:perform -B
```

   GPG configuration in maven settings xml:


```
<profile>
  <id>apache-release</id>
  <properties>
    <gpg.passphrase>[GPG_PASSWORD]</gpg.passphrase>
  </properties>
</profile>
```

4. go to https://repository.apache.org and close your staged repository. Note the repository url (format https://repository.apache.org/content/repositories/orgapachedirectmemory-028)


```
svn co https://dist.apache.org/repos/dist/dev/directmemory directmemory-dev-release
cd directmemory-dev-release
sh ./release-script-svn.sh version stagingRepoUrl
then svn add <new directory created with new version as name>
then svn ci 
```

5. Validating the release


```
  * Download sources, extract, build and run tests - mvn clean package
  * Verify license headers - mvn -Prat -DskipTests
  * Download binaries and .asc files
  * Download release manager's public key - From the KEYS file, get the release manager's public key finger print and run  gpg --keyserver pgpkeys.mit.edu --recv-key <key>
  * Validate authenticity of key - run  gpg --fingerprint <key>
  * Check signatures of all the binaries using gpg <binary>
```

6. Call for a vote in the dev list and wait for 72 hrs. for the vote results. 3 binding votes are necessary for the release to be finalized. example After the vote has passed, move the files from dist dev to dist release: svn mv https://dist.apache.org/repos/dist/dev/directmemory/version to https://dist.apache.org/repos/dist/release/directmemory/
7. Prepare release note. Add a page in src/site/apt/releasenotes/ and change value of <currentRelease> in parent pom.
8. Send out an announcement of the release to:
   - users@directmemory.apache.org
   - dev@directmemory.apache.org
9. Celebrate !

---

<a id="project-info"></a>

<!-- source_url: https://directmemory.apache.org/project-info.html -->

<!-- page_index: 16 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache DirectMemory Cache :: Parent pom |
| [Plugin Management](https://directmemory.apache.org/plugin-management.html) | This document lists the plugins that are defined through pluginManagement. |
| [Distribution Management](https://directmemory.apache.org/distribution-management.html) | This document provides informations on the distribution management of this project. |
| [Dependency Information](https://directmemory.apache.org/dependency-info.html) | This document describes how to to include this project as a dependency using various dependency management tools. |
| [Dependency Convergence](https://directmemory.apache.org/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [Source Repository](https://directmemory.apache.org/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |
| [Mailing Lists](https://directmemory.apache.org/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Project Plugins](https://directmemory.apache.org/plugins.html) | This document lists the build plugins and the report plugins used by this project. |
| [Project License](https://directmemory.apache.org/license.html) | This is a link to the definitions of project licenses. |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Dependency Management](https://directmemory.apache.org/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Project Team](https://directmemory.apache.org/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Dependencies](https://directmemory.apache.org/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |

---

<a id="modules"></a>

<!-- source_url: https://directmemory.apache.org/modules.html -->

<!-- page_index: 17 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Commons](#directmemory-common) | DirectMemory Commons is a collection of base utilities that are shared amongst the various modules of DirectMemory. |
| [Apache DirectMemory :: Cache](#directmemory-cache) | DirectMemory Cache is a multi layered cache implementation featuring off-heap memory management (a-la BigMemory) to enable efficient handling of a large number of java objects without affecting jvm garbage collection performance |
| [Apache DirectMemory :: Tests](#directmemory-tests) | Apache DirectMemory :: Tests |
| [Apache DirectMemory :: Server :: Commons](#server-directmemory-server-commons) | Apache DirectMemory :: Server :: Commons |
| [Apache DirectMemory :: Server :: Server Implementation](#server-directmemory-server) | Apache DirectMemory :: Server :: Server Implementation |
| [Apache DirectMemory :: Server :: Client](#server-directmemory-server-client) | Apache DirectMemory :: Server :: Client |
| [Apache DirectMemory :: Server :: Server Archetype](#server-server-example-archetype) | Apache DirectMemory :: Server :: Server Archetype |
| [Apache DirectMemory :: Server](#server) | Apache DirectMemory :: Server |
| [Apache DirectMemory :: Platforms :: Karaf](#platforms-apache-directmemory) | Apache DirectMemory :: Platforms :: Karaf |
| [Apache DirectMemory :: Platforms](#platforms) | Apache DirectMemory :: Platforms |
| [Apache DirectMemory :: Integrations :: Apache Solr](#directmemory-integrations-directmemory-solr) | Apache DirectMemory :: Integrations :: Apache Solr |
| [Apache DirectMemory :: Integrations :: EHCache](#directmemory-integrations-directmemory-ehcache) | EHCache CacheStore Implementation to integrate DirectMemory Cache as OffHeapStore. |
| [Apache DirectMemory :: Integrations :: Guava](#directmemory-integrations-directmemory-guava) | Provides second level cache implementation for Guava Cache |
| [Apache DirectMemory :: Integrations](#directmemory-integrations) | Apache DirectMemory :: Integrations |
| [Apache DirectMemory :: Serializers :: Protobuf](#directmemory-serializers-directmemory-protobuf) | Protobuf serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: Protostuff](#directmemory-serializers-directmemory-protostuff) | Protostuff serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: MessagePack](#directmemory-serializers-directmemory-msgpack) | MessagePack serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: Kryo](#directmemory-serializers-directmemory-kryo) | Kryo serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers](#directmemory-serializers) | Apache DirectMemory :: Serializers |
| [Apache DirectMemory :: Integration Tests :: OSGi](#itests-osgi) | Apache DirectMemory :: Integration Tests :: OSGi |
| [Apache DirectMemory :: Integration Tests](#itests) | Apache DirectMemory :: Integration Tests |
| [Apache DirectMemory :: Examples :: Server Javascript](#examples-server-example) | Apache DirectMemory :: Examples :: Server Javascript |
| [Apache DirectMemory :: Examples](#examples) | Apache DirectMemory :: Examples |

---

<a id="project-summary"></a>

<!-- source_url: https://directmemory.apache.org/project-summary.html -->

<!-- page_index: 18 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory |
| Description | Apache DirectMemory Cache :: Parent pom |
| Homepage | <http://directmemory.apache.org/> |

<a id="project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="directmemory-common"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-common/index.html -->

<!-- page_index: 19 -->

<a id="directmemory-common--about-apache-directmemory-::-commons"></a>

## About Apache DirectMemory :: Commons

DirectMemory Commons is a collection of base utilities that are shared amongst the various modules of
DirectMemory.

---

<a id="directmemory-cache"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-cache/index.html -->

<!-- page_index: 20 -->

<a id="directmemory-cache--about-apache-directmemory-::-cache"></a>

## About Apache DirectMemory :: Cache

DirectMemory Cache is a multi layered cache implementation featuring off-heap memory management (a-la
BigMemory) to enable efficient handling of a large number of java objects without affecting jvm garbage collection
performance

---

<a id="directmemory-tests"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-tests/index.html -->

<!-- page_index: 21 -->

<a id="directmemory-tests--about-apache-directmemory-::-tests"></a>

## About Apache DirectMemory :: Tests

Apache DirectMemory :: Tests

---

<a id="platforms"></a>

<!-- source_url: https://directmemory.apache.org/platforms/index.html -->

<!-- page_index: 22 -->

<a id="platforms--about-apache-directmemory-::-platforms"></a>

## About Apache DirectMemory :: Platforms

Apache DirectMemory :: Platforms

<a id="platforms--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Platforms :: Karaf](#platforms-apache-directmemory) | Apache DirectMemory :: Platforms :: Karaf |

---

<a id="directmemory-integrations"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/index.html -->

<!-- page_index: 23 -->

<a id="directmemory-integrations--about-apache-directmemory-::-integrations"></a>

## About Apache DirectMemory :: Integrations

Apache DirectMemory :: Integrations

<a id="directmemory-integrations--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Integrations :: Apache Solr](#directmemory-integrations-directmemory-solr) | Apache DirectMemory :: Integrations :: Apache Solr |
| [Apache DirectMemory :: Integrations :: EHCache](#directmemory-integrations-directmemory-ehcache) | EHCache CacheStore Implementation to integrate DirectMemory Cache as OffHeapStore. |
| [Apache DirectMemory :: Integrations :: Guava](#directmemory-integrations-directmemory-guava) | Provides second level cache implementation for Guava Cache |

---

<a id="directmemory-serializers"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/index.html -->

<!-- page_index: 24 -->

<a id="directmemory-serializers--about-apache-directmemory-::-serializers"></a>

## About Apache DirectMemory :: Serializers

Apache DirectMemory :: Serializers

<a id="directmemory-serializers--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Serializers :: Protobuf](#directmemory-serializers-directmemory-protobuf) | Protobuf serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: Protostuff](#directmemory-serializers-directmemory-protostuff) | Protostuff serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: MessagePack](#directmemory-serializers-directmemory-msgpack) | MessagePack serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: Kryo](#directmemory-serializers-directmemory-kryo) | Kryo serializer adapter for DirectMemory Cache |

---

<a id="itests"></a>

<!-- source_url: https://directmemory.apache.org/itests/index.html -->

<!-- page_index: 25 -->

<a id="itests--about-apache-directmemory-::-integration-tests"></a>

## About Apache DirectMemory :: Integration Tests

Apache DirectMemory :: Integration Tests

<a id="itests--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Integration Tests :: OSGi](#itests-osgi) | Apache DirectMemory :: Integration Tests :: OSGi |

---

<a id="examples"></a>

<!-- source_url: https://directmemory.apache.org/examples/index.html -->

<!-- page_index: 26 -->

<a id="examples--about-apache-directmemory-::-examples"></a>

## About Apache DirectMemory :: Examples

Apache DirectMemory :: Examples

<a id="examples--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Examples :: Server Javascript](#examples-server-example) | Apache DirectMemory :: Examples :: Server Javascript |

---

<a id="lightning-lightning-core"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-core/index.html -->

<!-- page_index: 27 -->

<a id="lightning-lightning-core--about-apache-lightning-::-core"></a>

## About Apache Lightning :: Core

Lightning fast Java Serialization

---

<a id="lightning-lightning-maven-plugin"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-plugin/index.html -->

<!-- page_index: 28 -->

<a id="lightning-lightning-maven-plugin--about-apache-lightning-::-maven-plugin"></a>

## About Apache Lightning :: Maven Plugin

Lightning fast Java Serialization

---

<a id="lightning-lightning-maven-integration-test"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-integration-test/index.html -->

<!-- page_index: 29 -->

<a id="lightning-lightning-maven-integration-test--about-apache-lightning-::-maven-integration-test"></a>

## About Apache Lightning :: Maven Integration Test

Lightning fast Java Serialization

---

<a id="lightning-lightning-maven-eclipse-helper"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper/index.html -->

<!-- page_index: 30 -->

<a id="lightning-lightning-maven-eclipse-helper--about-apache-lightning-::-maven-eclipse-helper"></a>

## About Apache Lightning :: Maven Eclipse Helper

Lightning fast Java Serialization

---

<a id="lightning-lightning-maven-eclipse-helper-feature"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper-feature/index.html -->

<!-- page_index: 31 -->

<a id="lightning-lightning-maven-eclipse-helper-feature--about-apache-lightning-::-maven-eclipse-helper-feature"></a>

## About Apache Lightning :: Maven Eclipse Helper Feature

Lightning fast Java Serialization

---

<a id="lightning-lightning-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/index.html -->

<!-- page_index: 32 -->

<a id="lightning-lightning-integration--about-apache-lightning-::-integration"></a>

## About Apache Lightning :: Integration

Lightning fast Java Serialization

---

<a id="server-directmemory-server-commons"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-commons/index.html -->

<!-- page_index: 33 -->

<a id="server-directmemory-server-commons--about-apache-directmemory-::-server-::-commons"></a>

## About Apache DirectMemory :: Server :: Commons

Apache DirectMemory :: Server :: Commons

---

<a id="server-directmemory-server"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server/index.html -->

<!-- page_index: 34 -->

<a id="server-directmemory-server--about-apache-directmemory-::-server-::-server-implementation"></a>

## About Apache DirectMemory :: Server :: Server Implementation

Apache DirectMemory :: Server :: Server Implementation

---

<a id="server-directmemory-server-client"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-client/index.html -->

<!-- page_index: 35 -->

<a id="server-directmemory-server-client--about-apache-directmemory-::-server-::-client"></a>

## About Apache DirectMemory :: Server :: Client

Apache DirectMemory :: Server :: Client

---

<a id="server-server-example-archetype"></a>

<!-- source_url: https://directmemory.apache.org/server/server-example-archetype/index.html -->

<!-- page_index: 36 -->

<a id="server-server-example-archetype--about-apache-directmemory-::-server-::-server-archetype"></a>

## About Apache DirectMemory :: Server :: Server Archetype

Apache DirectMemory :: Server :: Server Archetype

---

<a id="directmemory-serializers-directmemory-protobuf"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protobuf/index.html -->

<!-- page_index: 37 -->

<a id="directmemory-serializers-directmemory-protobuf--about-apache-directmemory-::-serializers-::-protobuf"></a>

## About Apache DirectMemory :: Serializers :: Protobuf

Protobuf serializer adapter for DirectMemory Cache

---

<a id="directmemory-serializers-directmemory-protostuff"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protostuff/index.html -->

<!-- page_index: 38 -->

<a id="directmemory-serializers-directmemory-protostuff--about-apache-directmemory-::-serializers-::-protostuff"></a>

## About Apache DirectMemory :: Serializers :: Protostuff

Protostuff serializer adapter for DirectMemory Cache

---

<a id="directmemory-serializers-directmemory-msgpack"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-msgpack/index.html -->

<!-- page_index: 39 -->

<a id="directmemory-serializers-directmemory-msgpack--about-apache-directmemory-::-serializers-::-messagepack"></a>

## About Apache DirectMemory :: Serializers :: MessagePack

MessagePack serializer adapter for DirectMemory Cache

---

<a id="directmemory-serializers-directmemory-kryo"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-kryo/index.html -->

<!-- page_index: 40 -->

<a id="directmemory-serializers-directmemory-kryo--about-apache-directmemory-::-serializers-::-kryo"></a>

## About Apache DirectMemory :: Serializers :: Kryo

Kryo serializer adapter for DirectMemory Cache

---

<a id="directmemory-integrations-directmemory-solr"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-solr/index.html -->

<!-- page_index: 41 -->

<a id="directmemory-integrations-directmemory-solr--about-apache-directmemory-::-integrations-::-apache-solr"></a>

## About Apache DirectMemory :: Integrations :: Apache Solr

Apache DirectMemory :: Integrations :: Apache Solr

---

<a id="directmemory-integrations-directmemory-ehcache"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-ehcache/index.html -->

<!-- page_index: 42 -->

<a id="directmemory-integrations-directmemory-ehcache--about-apache-directmemory-::-integrations-::-ehcache"></a>

## About Apache DirectMemory :: Integrations :: EHCache

EHCache CacheStore Implementation to integrate DirectMemory Cache as OffHeapStore.

---

<a id="directmemory-integrations-directmemory-guava"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-guava/index.html -->

<!-- page_index: 43 -->

<a id="directmemory-integrations-directmemory-guava--about-apache-directmemory-::-integrations-::-guava"></a>

## About Apache DirectMemory :: Integrations :: Guava

Provides second level cache implementation for Guava Cache

---

<a id="lightning-lightning-integration-lightning-integration-jgroups"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-jgroups/index.html -->

<!-- page_index: 44 -->

<a id="lightning-lightning-integration-lightning-integration-jgroups--about-apache-lightning-::-jgroups-integration"></a>

## About Apache Lightning :: JGroups Integration

Lightning fast Java Serialization

---

<a id="lightning-lightning-integration-lightning-integration-spring"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-spring/index.html -->

<!-- page_index: 45 -->

<a id="lightning-lightning-integration-lightning-integration-spring--about-apache-lightning-::-spring-integration"></a>

## About Apache Lightning :: Spring Integration

Lightning fast Java Serialization

---

<a id="platforms-apache-directmemory"></a>

<!-- source_url: https://directmemory.apache.org/platforms/apache-directmemory/index.html -->

<!-- page_index: 46 -->

<a id="platforms-apache-directmemory--about-apache-directmemory-::-platforms-::-karaf"></a>

## About Apache DirectMemory :: Platforms :: Karaf

Apache DirectMemory :: Platforms :: Karaf

---

<a id="itests-osgi"></a>

<!-- source_url: https://directmemory.apache.org/itests/osgi/index.html -->

<!-- page_index: 47 -->

<a id="itests-osgi--about-apache-directmemory-::-integration-tests-::-osgi"></a>

## About Apache DirectMemory :: Integration Tests :: OSGi

Apache DirectMemory :: Integration Tests :: OSGi

---

<a id="examples-server-example"></a>

<!-- source_url: https://directmemory.apache.org/examples/server-example/index.html -->

<!-- page_index: 48 -->

<a id="examples-server-example--about-apache-directmemory-::-examples-::-server-javascript"></a>

## About Apache DirectMemory :: Examples :: Server Javascript

Apache DirectMemory :: Examples :: Server Javascript

---

<a id="directmemory-cache-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-cache/integration.html -->

<!-- page_index: 49 -->

<a id="directmemory-cache-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-cache-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-cache-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-cache-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-cache/issue-tracking.html -->

<!-- page_index: 50 -->

<a id="directmemory-cache-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-cache-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-cache-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-cache/project-summary.html -->

<!-- page_index: 51 -->

<a id="directmemory-cache-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-cache-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Cache |
| Description | DirectMemory Cache is a multi layered cache implementation featuring off-heap memory management (a-la BigMemory) to enable efficient handling of a large number of java objects without affecting jvm garbage collection performance |
| Homepage | <http://directmemory.apache.org/directmemory-cache/> |

<a id="directmemory-cache-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-cache-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-cache |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-common-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-common/integration.html -->

<!-- page_index: 52 -->

<a id="directmemory-common-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-common-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-common-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-common-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-common/issue-tracking.html -->

<!-- page_index: 53 -->

<a id="directmemory-common-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-common-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-common-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-common/project-summary.html -->

<!-- page_index: 54 -->

<a id="directmemory-common-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-common-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Commons |
| Description | DirectMemory Commons is a collection of base utilities that are shared amongst the various modules of DirectMemory. |
| Homepage | <http://directmemory.apache.org/directmemory-common/> |

<a id="directmemory-common-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-common-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-common |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-integrations-directmemory-ehcache-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-ehcache/integration.html -->

<!-- page_index: 55 -->

<a id="directmemory-integrations-directmemory-ehcache-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-integrations-directmemory-ehcache-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-integrations-directmemory-ehcache-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-integrations-directmemory-ehcache-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-ehcache/issue-tracking.html -->

<!-- page_index: 56 -->

<a id="directmemory-integrations-directmemory-ehcache-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-integrations-directmemory-ehcache-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-integrations-directmemory-ehcache-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-ehcache/project-summary.html -->

<!-- page_index: 57 -->

<a id="directmemory-integrations-directmemory-ehcache-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-integrations-directmemory-ehcache-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Integrations :: EHCache |
| Description | EHCache CacheStore Implementation to integrate DirectMemory Cache as OffHeapStore. |
| Homepage | <http://directmemory.apache.org/directmemory-integrations/directmemory-ehcache/> |

<a id="directmemory-integrations-directmemory-ehcache-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-integrations-directmemory-ehcache-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-ehcache |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-integrations-directmemory-guava-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-guava/integration.html -->

<!-- page_index: 58 -->

<a id="directmemory-integrations-directmemory-guava-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-integrations-directmemory-guava-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-integrations-directmemory-guava-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-integrations-directmemory-guava-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-guava/issue-tracking.html -->

<!-- page_index: 59 -->

<a id="directmemory-integrations-directmemory-guava-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-integrations-directmemory-guava-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-integrations-directmemory-guava-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-guava/project-summary.html -->

<!-- page_index: 60 -->

<a id="directmemory-integrations-directmemory-guava-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-integrations-directmemory-guava-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Integrations :: Guava |
| Description | Provides second level cache implementation for Guava Cache |
| Homepage | <http://directmemory.apache.org/directmemory-integrations/directmemory-guava/> |

<a id="directmemory-integrations-directmemory-guava-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-integrations-directmemory-guava-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-guava |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-integrations-directmemory-solr-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-solr/integration.html -->

<!-- page_index: 61 -->

<a id="directmemory-integrations-directmemory-solr-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-integrations-directmemory-solr-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-integrations-directmemory-solr-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-integrations-directmemory-solr-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-solr/issue-tracking.html -->

<!-- page_index: 62 -->

<a id="directmemory-integrations-directmemory-solr-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-integrations-directmemory-solr-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-integrations-directmemory-solr-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/directmemory-solr/project-summary.html -->

<!-- page_index: 63 -->

<a id="directmemory-integrations-directmemory-solr-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-integrations-directmemory-solr-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Integrations :: Apache Solr |
| Description | Apache DirectMemory :: Integrations :: Apache Solr |
| Homepage | <http://directmemory.apache.org/directmemory-integrations/directmemory-solr/> |

<a id="directmemory-integrations-directmemory-solr-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-integrations-directmemory-solr-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-solr |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-integrations-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/integration.html -->

<!-- page_index: 64 -->

<a id="directmemory-integrations-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-integrations-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-integrations-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-integrations-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/issue-tracking.html -->

<!-- page_index: 65 -->

<a id="directmemory-integrations-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-integrations-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-integrations-modules"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/modules.html -->

<!-- page_index: 66 -->

<a id="directmemory-integrations-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Integrations :: Apache Solr](#directmemory-integrations-directmemory-solr) | Apache DirectMemory :: Integrations :: Apache Solr |
| [Apache DirectMemory :: Integrations :: EHCache](#directmemory-integrations-directmemory-ehcache) | EHCache CacheStore Implementation to integrate DirectMemory Cache as OffHeapStore. |
| [Apache DirectMemory :: Integrations :: Guava](#directmemory-integrations-directmemory-guava) | Provides second level cache implementation for Guava Cache |

---

<a id="directmemory-integrations-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-integrations/project-summary.html -->

<!-- page_index: 67 -->

<a id="directmemory-integrations-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-integrations-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Integrations |
| Description | Apache DirectMemory :: Integrations |
| Homepage | <http://directmemory.apache.org/directmemory-integrations/> |

<a id="directmemory-integrations-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-integrations-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-integrations |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="directmemory-serializers-directmemory-kryo-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-kryo/integration.html -->

<!-- page_index: 68 -->

<a id="directmemory-serializers-directmemory-kryo-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-serializers-directmemory-kryo-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-serializers-directmemory-kryo-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-serializers-directmemory-kryo-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-kryo/issue-tracking.html -->

<!-- page_index: 69 -->

<a id="directmemory-serializers-directmemory-kryo-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-serializers-directmemory-kryo-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-serializers-directmemory-kryo-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-kryo/project-summary.html -->

<!-- page_index: 70 -->

<a id="directmemory-serializers-directmemory-kryo-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-serializers-directmemory-kryo-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Serializers :: Kryo |
| Description | Kryo serializer adapter for DirectMemory Cache |
| Homepage | <http://directmemory.apache.org/directmemory-serializers/directmemory-kryo/> |

<a id="directmemory-serializers-directmemory-kryo-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-serializers-directmemory-kryo-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-kryo |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-serializers-directmemory-msgpack-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-msgpack/integration.html -->

<!-- page_index: 71 -->

<a id="directmemory-serializers-directmemory-msgpack-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-serializers-directmemory-msgpack-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-serializers-directmemory-msgpack-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-serializers-directmemory-msgpack-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-msgpack/issue-tracking.html -->

<!-- page_index: 72 -->

<a id="directmemory-serializers-directmemory-msgpack-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-serializers-directmemory-msgpack-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-serializers-directmemory-msgpack-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-msgpack/project-summary.html -->

<!-- page_index: 73 -->

<a id="directmemory-serializers-directmemory-msgpack-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-serializers-directmemory-msgpack-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Serializers :: MessagePack |
| Description | MessagePack serializer adapter for DirectMemory Cache |
| Homepage | <http://directmemory.apache.org/directmemory-serializers/directmemory-msgpack/> |

<a id="directmemory-serializers-directmemory-msgpack-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-serializers-directmemory-msgpack-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-msgpack |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-serializers-directmemory-protobuf-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protobuf/integration.html -->

<!-- page_index: 74 -->

<a id="directmemory-serializers-directmemory-protobuf-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-serializers-directmemory-protobuf-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-serializers-directmemory-protobuf-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-serializers-directmemory-protobuf-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protobuf/issue-tracking.html -->

<!-- page_index: 75 -->

<a id="directmemory-serializers-directmemory-protobuf-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-serializers-directmemory-protobuf-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-serializers-directmemory-protobuf-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protobuf/project-summary.html -->

<!-- page_index: 76 -->

<a id="directmemory-serializers-directmemory-protobuf-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-serializers-directmemory-protobuf-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Serializers :: Protobuf |
| Description | Protobuf serializer adapter for DirectMemory Cache |
| Homepage | <http://directmemory.apache.org/directmemory-serializers/directmemory-protobuf/> |

<a id="directmemory-serializers-directmemory-protobuf-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-serializers-directmemory-protobuf-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-protobuf |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-serializers-directmemory-protostuff-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protostuff/integration.html -->

<!-- page_index: 77 -->

<a id="directmemory-serializers-directmemory-protostuff-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-serializers-directmemory-protostuff-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-serializers-directmemory-protostuff-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-serializers-directmemory-protostuff-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protostuff/issue-tracking.html -->

<!-- page_index: 78 -->

<a id="directmemory-serializers-directmemory-protostuff-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-serializers-directmemory-protostuff-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-serializers-directmemory-protostuff-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/directmemory-protostuff/project-summary.html -->

<!-- page_index: 79 -->

<a id="directmemory-serializers-directmemory-protostuff-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-serializers-directmemory-protostuff-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Serializers :: Protostuff |
| Description | Protostuff serializer adapter for DirectMemory Cache |
| Homepage | <http://directmemory.apache.org/directmemory-serializers/directmemory-protostuff/> |

<a id="directmemory-serializers-directmemory-protostuff-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-serializers-directmemory-protostuff-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-protostuff |
| Version | 0.3-SNAPSHOT |
| Type | bundle |
| JDK Rev | 1.6 |

---

<a id="directmemory-serializers-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/integration.html -->

<!-- page_index: 80 -->

<a id="directmemory-serializers-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-serializers-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-serializers-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-serializers-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/issue-tracking.html -->

<!-- page_index: 81 -->

<a id="directmemory-serializers-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-serializers-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-serializers-modules"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/modules.html -->

<!-- page_index: 82 -->

<a id="directmemory-serializers-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Serializers :: Protobuf](#directmemory-serializers-directmemory-protobuf) | Protobuf serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: Protostuff](#directmemory-serializers-directmemory-protostuff) | Protostuff serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: MessagePack](#directmemory-serializers-directmemory-msgpack) | MessagePack serializer adapter for DirectMemory Cache |
| [Apache DirectMemory :: Serializers :: Kryo](#directmemory-serializers-directmemory-kryo) | Kryo serializer adapter for DirectMemory Cache |

---

<a id="directmemory-serializers-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-serializers/project-summary.html -->

<!-- page_index: 83 -->

<a id="directmemory-serializers-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-serializers-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Serializers |
| Description | Apache DirectMemory :: Serializers |
| Homepage | <http://directmemory.apache.org/directmemory-serializers/> |

<a id="directmemory-serializers-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-serializers-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-serializers |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="directmemory-tests-integration"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-tests/integration.html -->

<!-- page_index: 84 -->

<a id="directmemory-tests-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="directmemory-tests-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="directmemory-tests-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="directmemory-tests-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-tests/issue-tracking.html -->

<!-- page_index: 85 -->

<a id="directmemory-tests-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="directmemory-tests-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="directmemory-tests-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/directmemory-tests/project-summary.html -->

<!-- page_index: 86 -->

<a id="directmemory-tests-project-summary--project-summary"></a>

## Project Summary

<a id="directmemory-tests-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Tests |
| Description | Apache DirectMemory :: Tests |
| Homepage | <http://directmemory.apache.org/directmemory-tests/> |

<a id="directmemory-tests-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="directmemory-tests-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | directmemory-tests |
| Version | 0.3-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="examples-integration"></a>

<!-- source_url: https://directmemory.apache.org/examples/integration.html -->

<!-- page_index: 87 -->

<a id="examples-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="examples-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="examples-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="examples-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/examples/issue-tracking.html -->

<!-- page_index: 88 -->

<a id="examples-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="examples-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="examples-modules"></a>

<!-- source_url: https://directmemory.apache.org/examples/modules.html -->

<!-- page_index: 89 -->

<a id="examples-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Examples :: Server Javascript](#examples-server-example) | Apache DirectMemory :: Examples :: Server Javascript |

---

<a id="examples-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/examples/project-summary.html -->

<!-- page_index: 90 -->

<a id="examples-project-summary--project-summary"></a>

## Project Summary

<a id="examples-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Examples |
| Description | Apache DirectMemory :: Examples |
| Homepage | <http://directmemory.apache.org/examples/> |

<a id="examples-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="examples-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | examples |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="examples-server-example-integration"></a>

<!-- source_url: https://directmemory.apache.org/examples/server-example/integration.html -->

<!-- page_index: 91 -->

<a id="examples-server-example-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="examples-server-example-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="examples-server-example-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="examples-server-example-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/examples/server-example/issue-tracking.html -->

<!-- page_index: 92 -->

<a id="examples-server-example-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="examples-server-example-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="examples-server-example-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/examples/server-example/project-summary.html -->

<!-- page_index: 93 -->

<a id="examples-server-example-project-summary--project-summary"></a>

## Project Summary

<a id="examples-server-example-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Examples :: Server Javascript |
| Description | Apache DirectMemory :: Examples :: Server Javascript |
| Homepage | <http://directmemory.apache.org/examples/server-example/> |

<a id="examples-server-example-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="examples-server-example-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | server-example |
| Version | 0.3-SNAPSHOT |
| Type | war |
| JDK Rev | 1.6 |

---

<a id="itests-integration"></a>

<!-- source_url: https://directmemory.apache.org/itests/integration.html -->

<!-- page_index: 94 -->

<a id="itests-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="itests-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="itests-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="itests-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/itests/issue-tracking.html -->

<!-- page_index: 95 -->

<a id="itests-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="itests-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="itests-modules"></a>

<!-- source_url: https://directmemory.apache.org/itests/modules.html -->

<!-- page_index: 96 -->

<a id="itests-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Integration Tests :: OSGi](#itests-osgi) | Apache DirectMemory :: Integration Tests :: OSGi |

---

<a id="itests-osgi-integration"></a>

<!-- source_url: https://directmemory.apache.org/itests/osgi/integration.html -->

<!-- page_index: 97 -->

<a id="itests-osgi-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="itests-osgi-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="itests-osgi-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="itests-osgi-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/itests/osgi/issue-tracking.html -->

<!-- page_index: 98 -->

<a id="itests-osgi-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="itests-osgi-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="itests-osgi-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/itests/osgi/project-summary.html -->

<!-- page_index: 99 -->

<a id="itests-osgi-project-summary--project-summary"></a>

## Project Summary

<a id="itests-osgi-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Integration Tests :: OSGi |
| Description | Apache DirectMemory :: Integration Tests :: OSGi |
| Homepage | <http://directmemory.apache.org/itests/osgi/> |

<a id="itests-osgi-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="itests-osgi-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.itests |
| ArtifactId | osgi |
| Version | 0.3-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="itests-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/itests/project-summary.html -->

<!-- page_index: 100 -->

<a id="itests-project-summary--project-summary"></a>

## Project Summary

<a id="itests-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Integration Tests |
| Description | Apache DirectMemory :: Integration Tests |
| Homepage | <http://directmemory.apache.org/itests/> |

<a id="itests-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="itests-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | itests |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="lightning-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/integration.html -->

<!-- page_index: 101 -->

<a id="lightning-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/issue-tracking.html -->

<!-- page_index: 102 -->

<a id="lightning-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-core-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-core/integration.html -->

<!-- page_index: 103 -->

<a id="lightning-lightning-core-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-core-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-core-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-core-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-core/issue-tracking.html -->

<!-- page_index: 104 -->

<a id="lightning-lightning-core-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-core-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-core-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-core/project-summary.html -->

<!-- page_index: 105 -->

<a id="lightning-lightning-core-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-core-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Core |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-core> |

<a id="lightning-lightning-core-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-core-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-core |
| Version | 0.0.1-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="lightning-lightning-integration-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/integration.html -->

<!-- page_index: 106 -->

<a id="lightning-lightning-integration-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-integration-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-integration-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-integration-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/issue-tracking.html -->

<!-- page_index: 107 -->

<a id="lightning-lightning-integration-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-integration-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-integration-lightning-integration-jgroups-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-jgroups/integration.html -->

<!-- page_index: 108 -->

<a id="lightning-lightning-integration-lightning-integration-jgroups-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-integration-lightning-integration-jgroups-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-integration-lightning-integration-jgroups-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-integration-lightning-integration-jgroups-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-jgroups/issue-tracking.html -->

<!-- page_index: 109 -->

<a id="lightning-lightning-integration-lightning-integration-jgroups-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-integration-lightning-integration-jgroups-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-integration-lightning-integration-jgroups-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-jgroups/project-summary.html -->

<!-- page_index: 110 -->

<a id="lightning-lightning-integration-lightning-integration-jgroups-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-integration-lightning-integration-jgroups-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: JGroups Integration |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-integration/lightning-integration-jgroups> |

<a id="lightning-lightning-integration-lightning-integration-jgroups-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-integration-lightning-integration-jgroups-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-integration-jgroups |
| Version | 0.0.1-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="lightning-lightning-integration-lightning-integration-jgroups-sonar"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-jgroups/sonar.html -->

<!-- page_index: 111 -->

<a id="lightning-lightning-integration-lightning-integration-jgroups-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.lightning:lightning-integration-jgroups>

---

<a id="lightning-lightning-integration-lightning-integration-spring-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-spring/integration.html -->

<!-- page_index: 112 -->

<a id="lightning-lightning-integration-lightning-integration-spring-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-integration-lightning-integration-spring-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-integration-lightning-integration-spring-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-integration-lightning-integration-spring-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-spring/issue-tracking.html -->

<!-- page_index: 113 -->

<a id="lightning-lightning-integration-lightning-integration-spring-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-integration-lightning-integration-spring-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-integration-lightning-integration-spring-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-spring/project-summary.html -->

<!-- page_index: 114 -->

<a id="lightning-lightning-integration-lightning-integration-spring-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-integration-lightning-integration-spring-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Spring Integration |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-integration/lightning-integration-spring> |

<a id="lightning-lightning-integration-lightning-integration-spring-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-integration-lightning-integration-spring-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-integration-spring |
| Version | 0.0.1-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="lightning-lightning-integration-lightning-integration-spring-sonar"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/lightning-integration-spring/sonar.html -->

<!-- page_index: 115 -->

<a id="lightning-lightning-integration-lightning-integration-spring-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.lightning:lightning-integration-spring>

---

<a id="lightning-lightning-integration-modules"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/modules.html -->

<!-- page_index: 116 -->

<a id="lightning-lightning-integration-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Lightning :: JGroups Integration](#lightning-lightning-integration-lightning-integration-jgroups) | - |
| [Apache Lightning :: Spring Integration](#lightning-lightning-integration-lightning-integration-spring) | - |

---

<a id="lightning-lightning-integration-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-integration/project-summary.html -->

<!-- page_index: 117 -->

<a id="lightning-lightning-integration-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-integration-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Integration |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-integration> |

<a id="lightning-lightning-integration-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-integration-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-integration |
| Version | 0.0.1-SNAPSHOT |
| Type | pom |

---

<a id="lightning-lightning-maven-eclipse-helper-feature-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper-feature/integration.html -->

<!-- page_index: 118 -->

<a id="lightning-lightning-maven-eclipse-helper-feature-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-maven-eclipse-helper-feature-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-maven-eclipse-helper-feature-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-maven-eclipse-helper-feature-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper-feature/issue-tracking.html -->

<!-- page_index: 119 -->

<a id="lightning-lightning-maven-eclipse-helper-feature-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-maven-eclipse-helper-feature-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-maven-eclipse-helper-feature-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper-feature/project-summary.html -->

<!-- page_index: 120 -->

<a id="lightning-lightning-maven-eclipse-helper-feature-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-maven-eclipse-helper-feature-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Maven Eclipse Helper Feature |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-maven-eclipse-helper-feature> |

<a id="lightning-lightning-maven-eclipse-helper-feature-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-maven-eclipse-helper-feature-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-maven-eclipse-helper-feature |
| Version | 0.0.1-SNAPSHOT |
| Type | eclipse-feature |
| JDK Rev | 1.6 |

---

<a id="lightning-lightning-maven-eclipse-helper-feature-sonar"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper-feature/sonar.html -->

<!-- page_index: 121 -->

<a id="lightning-lightning-maven-eclipse-helper-feature-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.lightning:lightning-maven-eclipse-helper-feature>

---

<a id="lightning-lightning-maven-eclipse-helper-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper/integration.html -->

<!-- page_index: 122 -->

<a id="lightning-lightning-maven-eclipse-helper-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-maven-eclipse-helper-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-maven-eclipse-helper-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-maven-eclipse-helper-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper/issue-tracking.html -->

<!-- page_index: 123 -->

<a id="lightning-lightning-maven-eclipse-helper-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-maven-eclipse-helper-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-maven-eclipse-helper-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper/project-summary.html -->

<!-- page_index: 124 -->

<a id="lightning-lightning-maven-eclipse-helper-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-maven-eclipse-helper-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Maven Eclipse Helper |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-maven-eclipse-helper> |

<a id="lightning-lightning-maven-eclipse-helper-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-maven-eclipse-helper-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-maven-eclipse-helper |
| Version | 0.0.1-SNAPSHOT |
| Type | eclipse-plugin |
| JDK Rev | 1.6 |

---

<a id="lightning-lightning-maven-eclipse-helper-sonar"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-eclipse-helper/sonar.html -->

<!-- page_index: 125 -->

<a id="lightning-lightning-maven-eclipse-helper-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.lightning:lightning-maven-eclipse-helper>

---

<a id="lightning-lightning-maven-integration-test-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-integration-test/integration.html -->

<!-- page_index: 126 -->

<a id="lightning-lightning-maven-integration-test-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-maven-integration-test-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-maven-integration-test-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-maven-integration-test-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-integration-test/issue-tracking.html -->

<!-- page_index: 127 -->

<a id="lightning-lightning-maven-integration-test-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-maven-integration-test-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-maven-integration-test-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-integration-test/project-summary.html -->

<!-- page_index: 128 -->

<a id="lightning-lightning-maven-integration-test-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-maven-integration-test-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Maven Integration Test |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-maven-integration-test> |

<a id="lightning-lightning-maven-integration-test-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-maven-integration-test-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-maven-integration-test |
| Version | 0.0.1-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="lightning-lightning-maven-integration-test-sonar"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-integration-test/sonar.html -->

<!-- page_index: 129 -->

<a id="lightning-lightning-maven-integration-test-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.lightning:lightning-maven-integration-test>

---

<a id="lightning-lightning-maven-plugin-integration"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-plugin/integration.html -->

<!-- page_index: 130 -->

<a id="lightning-lightning-maven-plugin-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="lightning-lightning-maven-plugin-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/view/A-F/view/Directmemory/
```

<a id="lightning-lightning-maven-plugin-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="lightning-lightning-maven-plugin-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-plugin/issue-tracking.html -->

<!-- page_index: 131 -->

<a id="lightning-lightning-maven-plugin-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="lightning-lightning-maven-plugin-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="lightning-lightning-maven-plugin-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/lightning-maven-plugin/project-summary.html -->

<!-- page_index: 132 -->

<a id="lightning-lightning-maven-plugin-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-lightning-maven-plugin-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning :: Maven Plugin |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning/lightning-maven-plugin> |

<a id="lightning-lightning-maven-plugin-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-lightning-maven-plugin-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning-maven-plugin |
| Version | 0.0.1-SNAPSHOT |
| Type | maven-plugin |
| JDK Rev | 1.6 |

---

<a id="lightning-modules"></a>

<!-- source_url: https://directmemory.apache.org/lightning/modules.html -->

<!-- page_index: 133 -->

<a id="lightning-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Lightning :: Core](#lightning-lightning-core) | - |
| [Apache Lightning :: Maven Plugin](#lightning-lightning-maven-plugin) | - |
| [Apache Lightning :: Maven Integration Test](#lightning-lightning-maven-integration-test) | - |
| [Apache Lightning :: Maven Eclipse Helper](#lightning-lightning-maven-eclipse-helper) | - |
| [Apache Lightning :: Maven Eclipse Helper Feature](#lightning-lightning-maven-eclipse-helper-feature) | - |
| [Apache Lightning :: Integration](#lightning-lightning-integration) | - |

---

<a id="lightning-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/lightning/project-summary.html -->

<!-- page_index: 134 -->

<a id="lightning-project-summary--project-summary"></a>

## Project Summary

<a id="lightning-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Lightning |
| Description | Lightning fast Java Serialization |
| Homepage | <http://directmemory.apache.org/lightning> |

<a id="lightning-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="lightning-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.lightning |
| ArtifactId | lightning |
| Version | 0.0.1-SNAPSHOT |
| Type | pom |

---

<a id="platforms-apache-directmemory-integration"></a>

<!-- source_url: https://directmemory.apache.org/platforms/apache-directmemory/integration.html -->

<!-- page_index: 135 -->

<a id="platforms-apache-directmemory-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="platforms-apache-directmemory-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="platforms-apache-directmemory-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="platforms-apache-directmemory-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/platforms/apache-directmemory/issue-tracking.html -->

<!-- page_index: 136 -->

<a id="platforms-apache-directmemory-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="platforms-apache-directmemory-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="platforms-apache-directmemory-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/platforms/apache-directmemory/project-summary.html -->

<!-- page_index: 137 -->

<a id="platforms-apache-directmemory-project-summary--project-summary"></a>

## Project Summary

<a id="platforms-apache-directmemory-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Platforms :: Karaf |
| Description | Apache DirectMemory :: Platforms :: Karaf |
| Homepage | <http://directmemory.apache.org/platforms/apache-directmemory/> |

<a id="platforms-apache-directmemory-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="platforms-apache-directmemory-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.karaf |
| ArtifactId | apache-directmemory |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="platforms-integration"></a>

<!-- source_url: https://directmemory.apache.org/platforms/integration.html -->

<!-- page_index: 138 -->

<a id="platforms-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="platforms-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="platforms-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="platforms-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/platforms/issue-tracking.html -->

<!-- page_index: 139 -->

<a id="platforms-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="platforms-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="platforms-modules"></a>

<!-- source_url: https://directmemory.apache.org/platforms/modules.html -->

<!-- page_index: 140 -->

<a id="platforms-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Platforms :: Karaf](#platforms-apache-directmemory) | Apache DirectMemory :: Platforms :: Karaf |

---

<a id="platforms-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/platforms/project-summary.html -->

<!-- page_index: 141 -->

<a id="platforms-project-summary--project-summary"></a>

## Project Summary

<a id="platforms-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Platforms |
| Description | Apache DirectMemory :: Platforms |
| Homepage | <http://directmemory.apache.org/platforms/> |

<a id="platforms-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="platforms-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory |
| ArtifactId | platforms |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="server-directmemory-server-client-integration"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-client/integration.html -->

<!-- page_index: 142 -->

<a id="server-directmemory-server-client-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="server-directmemory-server-client-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="server-directmemory-server-client-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="server-directmemory-server-client-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-client/issue-tracking.html -->

<!-- page_index: 143 -->

<a id="server-directmemory-server-client-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="server-directmemory-server-client-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="server-directmemory-server-client-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-client/project-summary.html -->

<!-- page_index: 144 -->

<a id="server-directmemory-server-client-project-summary--project-summary"></a>

## Project Summary

<a id="server-directmemory-server-client-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Server :: Client |
| Description | Apache DirectMemory :: Server :: Client |
| Homepage | <http://directmemory.apache.org/server/directmemory-server-client/> |

<a id="server-directmemory-server-client-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="server-directmemory-server-client-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.server |
| ArtifactId | directmemory-server-client |
| Version | 0.3-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="server-directmemory-server-client-sonar"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-client/sonar.html -->

<!-- page_index: 145 -->

<a id="server-directmemory-server-client-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.server:directmemory-server-client>

---

<a id="server-directmemory-server-commons-integration"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-commons/integration.html -->

<!-- page_index: 146 -->

<a id="server-directmemory-server-commons-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="server-directmemory-server-commons-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="server-directmemory-server-commons-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="server-directmemory-server-commons-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-commons/issue-tracking.html -->

<!-- page_index: 147 -->

<a id="server-directmemory-server-commons-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="server-directmemory-server-commons-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="server-directmemory-server-commons-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-commons/project-summary.html -->

<!-- page_index: 148 -->

<a id="server-directmemory-server-commons-project-summary--project-summary"></a>

## Project Summary

<a id="server-directmemory-server-commons-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Server :: Commons |
| Description | Apache DirectMemory :: Server :: Commons |
| Homepage | <http://directmemory.apache.org/server/directmemory-server-commons/> |

<a id="server-directmemory-server-commons-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="server-directmemory-server-commons-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.server |
| ArtifactId | directmemory-server-commons |
| Version | 0.3-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="server-directmemory-server-commons-sonar"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server-commons/sonar.html -->

<!-- page_index: 149 -->

<a id="server-directmemory-server-commons-sonar--sonar"></a>

## Sonar

Redirecting to <https://analysis.apache.org/project/index/org.apache.directmemory.server:directmemory-server-commons>

---

<a id="server-directmemory-server-integration"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server/integration.html -->

<!-- page_index: 150 -->

<a id="server-directmemory-server-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="server-directmemory-server-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="server-directmemory-server-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="server-directmemory-server-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server/issue-tracking.html -->

<!-- page_index: 151 -->

<a id="server-directmemory-server-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="server-directmemory-server-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="server-directmemory-server-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/server/directmemory-server/project-summary.html -->

<!-- page_index: 152 -->

<a id="server-directmemory-server-project-summary--project-summary"></a>

## Project Summary

<a id="server-directmemory-server-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Server :: Server Implementation |
| Description | Apache DirectMemory :: Server :: Server Implementation |
| Homepage | <http://directmemory.apache.org/server/directmemory-server/> |

<a id="server-directmemory-server-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="server-directmemory-server-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.server |
| ArtifactId | directmemory-server |
| Version | 0.3-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="server-integration"></a>

<!-- source_url: https://directmemory.apache.org/server/integration.html -->

<!-- page_index: 153 -->

<a id="server-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="server-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="server-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="server-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/server/issue-tracking.html -->

<!-- page_index: 154 -->

<a id="server-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="server-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="server-modules"></a>

<!-- source_url: https://directmemory.apache.org/server/modules.html -->

<!-- page_index: 155 -->

<a id="server-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache DirectMemory :: Server :: Commons](#server-directmemory-server-commons) | Apache DirectMemory :: Server :: Commons |
| [Apache DirectMemory :: Server :: Server Implementation](#server-directmemory-server) | Apache DirectMemory :: Server :: Server Implementation |
| [Apache DirectMemory :: Server :: Client](#server-directmemory-server-client) | Apache DirectMemory :: Server :: Client |
| [Apache DirectMemory :: Server :: Server Archetype](#server-server-example-archetype) | Apache DirectMemory :: Server :: Server Archetype |

---

<a id="server-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/server/project-summary.html -->

<!-- page_index: 156 -->

<a id="server-project-summary--project-summary"></a>

## Project Summary

<a id="server-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Server |
| Description | Apache DirectMemory :: Server |
| Homepage | <http://directmemory.apache.org/server/> |

<a id="server-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="server-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.server |
| ArtifactId | server |
| Version | 0.3-SNAPSHOT |
| Type | pom |

---

<a id="server-server-example-archetype-integration"></a>

<!-- source_url: https://directmemory.apache.org/server/server-example-archetype/integration.html -->

<!-- page_index: 157 -->

<a id="server-server-example-archetype-integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="server-server-example-archetype-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/directmemory-trunk/
```

<a id="server-server-example-archetype-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="server-server-example-archetype-issue-tracking"></a>

<!-- source_url: https://directmemory.apache.org/server/server-example-archetype/issue-tracking.html -->

<!-- page_index: 158 -->

<a id="server-server-example-archetype-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="server-server-example-archetype-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/DIRECTMEMORY
```

---

<a id="server-server-example-archetype-project-summary"></a>

<!-- source_url: https://directmemory.apache.org/server/server-example-archetype/project-summary.html -->

<!-- page_index: 159 -->

<a id="server-server-example-archetype-project-summary--project-summary"></a>

## Project Summary

<a id="server-server-example-archetype-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache DirectMemory :: Server :: Server Archetype |
| Description | Apache DirectMemory :: Server :: Server Archetype |
| Homepage | <http://directmemory.apache.org/server/server-example-archetype/> |

<a id="server-server-example-archetype-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="server-server-example-archetype-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.directmemory.server |
| ArtifactId | server-example-archetype |
| Version | 0.3-SNAPSHOT |
| Type | maven-archetype |
| JDK Rev | 1.6 |

---
