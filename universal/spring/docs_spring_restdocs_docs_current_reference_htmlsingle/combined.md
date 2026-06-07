# Spring REST Docs

## Navigation

- [Introduction](#index--introduction)
- [Getting started](#index--getting-started)
  
- [Sample Applications](#index--getting-started-sample-applications)
  
- [Requirements](#index--getting-started-requirements)
  
- [Build configuration](#index--getting-started-build-configuration)
    
- [Packaging the Documentation](#index--getting-started-build-configuration-packaging-the-documentation)
  
- [Generating Documentation Snippets](#index--getting-started-documentation-snippets)
    
- [Setting up Your Tests](#index--getting-started-documentation-snippets-setup)
      
- [Setting up Your JUnit 5 Tests](#index--getting-started-documentation-snippets-setup-junit-5)
      
- [Setting up Your JUnit 4 Tests](#index--getting-started-documentation-snippets-setup-junit)
      
- [Setting up your tests without JUnit](#index--getting-started-documentation-snippets-setup-manual)
    
- [Invoking the RESTful Service](#index--getting-started-documentation-snippets-invoking-the-service)
  
- [Using the Snippets](#index--getting-started-using-the-snippets)
- [Documenting your API](#index--documenting-your-api)
  
- [Hypermedia](#index--documenting-your-api-hypermedia)
    
- [Hypermedia Link Formats](#index--documenting-your-api-hypermedia-link-formats)
    
- [Ignoring Common Links](#index--documenting-your-api-hypermedia-ignoring-common-links)
  
- [Request and Response Payloads](#index--documenting-your-api-request-response-payloads)
    
- [Request and Response Fields](#index--documenting-your-api-request-response-payloads-fields)
      
- [Fields in JSON Payloads](#index--documenting-your-api-request-response-payloads-fields-json)
        
- [JSON Field Paths](#index--documenting-your-api-request-response-payloads-fields-json-field-paths)
        
- [JSON Field Types](#index--documenting-your-api-request-response-payloads-fields-json-field-types)
      
- [XML payloads](#index--documenting-your-api-request-response-payloads-fields-xml)
        
- [XML Field Paths](#index--documenting-your-api-request-response-payloads-fields-xml-field-paths)
        
- [XML Field Types](#index--documenting-your-api-request-response-payloads-fields-xml-field-types)
      
- [Reusing Field Descriptors](#index--documenting-your-api-request-response-payloads-fields-reusing-field-descriptors)
    
- [Documenting a Subsection of a Request or Response Payload](#index--documenting-your-api-request-response-payloads-subsections)
      
- [Documenting a Subsection of a Request or Response Body](#index--documenting-your-api-request-response-payloads-subsections-body)
      
- [Documenting the Fields of a Subsection of a Request or Response](#index--documenting-your-api-request-response-payloads-subsections-fields)
  
- [Query Parameters](#index--documenting-your-api-query-parameters)
  
- [Form Parameters](#index--documenting-your-api-form-parameters)
  
- [Path Parameters](#index--documenting-your-api-path-parameters)
  
- [Request Parts](#index--documenting-your-api-request-parts)
  
- [Request Part Payloads](#index--documenting-your-api-request-parts-payloads)
    
- [Documenting a Request Part’s Body](#index--documenting-your-api-request-parts-payloads-body)
    
- [Documenting a Request Part’s Fields](#index--documenting-your-api-request-parts-payloads-fields)
  
- [HTTP Headers](#index--documenting-your-api-http-headers)
  
- [HTTP Cookies](#index--documenting-your-api-http-cookies)
  
- [Reusing Snippets](#index--documenting-your-api-reusing-snippets)
  
- [Documenting Constraints](#index--documenting-your-api-constraints)
    
- [Finding Constraints](#index--documenting-your-api-constraints-finding)
    
- [Describing Constraints](#index--documenting-your-api-constraints-describing)
    
- [Using Constraint Descriptions in Generated Snippets](#index--_using_constraint_descriptions_in_generated_snippets)
  
- [Default Snippets](#index--documenting-your-api-default-snippets)
  
- [Using Parameterized Output Directories](#index--documentating-your-api-parameterized-output-directories)
  
- [Customizing the Output](#index--documenting-your-api-customizing)
    
- [Customizing the Generated Snippets](#index--documenting-your-api-customizing-snippets)
    
- [Including Extra Information](#index--documenting-your-api-customizing-including-extra-information)
- [Customizing requests and responses](#index--customizing-requests-and-responses)
  
- [Preprocessors](#index--customizing-requests-and-responses-preprocessors)
    
- [Pretty Printing](#index--customizing-requests-and-responses-preprocessors-pretty-print)
    
- [Masking Links](#index--customizing-requests-and-responses-preprocessors-mask-links)
    
- [Modifying Headers](#index--customizing-requests-and-responses-preprocessors-modify-headers)
    
- [Replacing Patterns](#index--customizing-requests-and-responses-preprocessors-replace-patterns)
    
- [Modifying URIs](#index--customizing-requests-and-responses-preprocessors-modify-uris)
    
- [Writing Your Own Preprocessor](#index--customizing-requests-and-responses-preprocessors-writing-your-own)
- [Configuration](#index--configuration)
  
- [Documented URIs](#index--configuration-uris)
    
- [MockMvc URI Customization](#index--configuration-uris-mockmvc)
    
- [REST Assured URI Customization](#index--configuration-uris-rest-assured)
    
- [WebTestClient URI Customization](#index--configuration-uris-webtestclient)
  
- [Snippet Encoding](#index--configuration-snippet-encoding)
  
- [Snippet Template Format](#index--configuration-snippet-template-format)
  
- [Default Snippets](#index--configuration-default-snippets)
  
- [Default Operation Preprocessors](#index--configuration-default-preprocessors)
- [Working with Asciidoctor](#index--working-with-asciidoctor)
  
- [Resources](#index--working-with-asciidoctor-resources)
  
- [Including Snippets](#index--working-with-asciidoctor-including-snippets)
    
- [Including Multiple Snippets for an Operation](#index--working-with-asciidoctor-including-snippets-operation)
      
- [Section Titles](#index--working-with-asciidoctor-including-snippets-operation-titles)
    
- [Including Individual Snippets](#index--working-with-asciidoctor-including-snippets-individual)
  
- [Customizing Tables](#index--working-with-asciidoctor-customizing-tables)
    
- [Formatting Columns](#index--working-with-asciidoctor-customizing-tables-formatting-columns)
    
- [Configuring the Title](#index--working-with-asciidoctor-customizing-tables-title)
    
- [Avoiding Table Formatting Problems](#index--working-with-asciidoctor-customizing-tables-formatting-problems)
  
- [Further Reading](#index--working-with-asciidoctor-further-reading)
- [Working with Markdown](#index--working-with-markdown)
  
- [Limitations](#index--working-with-markdown-limitations)
  
- [Including Snippets](#index--working-with-markdown-including-snippets)
- [Contributing](#index--contributing)
  
- [Questions](#index--contributing-questions)
  
- [Bugs](#index--contributing-bugs)
  
- [Enhancements](#index--contributing-enhancements)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-restdocs/docs/current/reference/htmlsingle/ -->

<!-- page_index: 1 -->

# Spring REST Docs

Document RESTful services by combining hand-written documentation with auto-generated snippets produced with Spring MVC Test or WebTestClient.

<a id="index--introduction"></a>

## [Introduction](#index--introduction)

The aim of Spring REST Docs is to help you produce accurate and readable documentation for your RESTful services.

Writing high-quality documentation is difficult.
One way to ease that difficulty is to use tools that are well-suited to the job.
To this end, Spring REST Docs uses [Asciidoctor](https://asciidoctor.org) by default.
Asciidoctor processes plain text and produces HTML, styled and laid out to suit your needs.
If you prefer, you can also configure Spring REST Docs to use Markdown.

Spring REST Docs uses snippets produced by tests written with Spring MVC’s [test framework](https://docs.spring.io/spring-framework/reference/6.2/testing/mockmvc.html), Spring WebFlux’s [`WebTestClient`](https://docs.spring.io/spring-framework/reference/6.2/testing/webtestclient.html) or [REST Assured 5](https://rest-assured.io/).
This test-driven approach helps to guarantee the accuracy of your service’s documentation.
If a snippet is incorrect, the test that produces it fails.

Documenting a RESTful service is largely about describing its resources.
Two key parts of each resource’s description are the details of the HTTP requests that it consumes and the HTTP responses that it produces.
Spring REST Docs lets you work with these resources and the HTTP requests and responses, shielding your documentation from the inner-details of your service’s implementation.
This separation helps you document your service’s API rather than its implementation.
It also frees you to evolve the implementation without having to rework the documentation.

<a id="index--getting-started"></a>

## [Getting started](#index--getting-started)

This section describes how to get started with Spring REST Docs.

<a id="index--getting-started-sample-applications"></a>
<a id="index--sample-applications"></a>

### [Sample Applications](#index--getting-started-sample-applications)

If you want to jump straight in, a number of [sample applications are available](https://github.com/spring-projects/spring-restdocs-samples).

<a id="index--getting-started-requirements"></a>
<a id="index--requirements"></a>

### [Requirements](#index--getting-started-requirements)

Spring REST Docs has the following minimum requirements:

- Java 17
- Spring Framework 6

Additionally, the `spring-restdocs-restassured` module requires REST Assured 5.2.

<a id="index--getting-started-build-configuration"></a>
<a id="index--build-configuration"></a>

### [Build configuration](#index--getting-started-build-configuration)

The first step in using Spring REST Docs is to configure your project’s build.
The [Spring HATEOAS](https://github.com/spring-projects/spring-restdocs-samples/tree/main/restful-notes-spring-hateoas) and [Spring Data REST](https://github.com/spring-projects/spring-restdocs-samples/tree/main/restful-notes-spring-data-rest) samples contain a `build.gradle` and `pom.xml`, respectively, that you may wish to use as a reference.
The key parts of the configuration are described in the following listings:

Maven

```xml
<dependency> (1)
	<groupId>org.springframework.restdocs</groupId>
	<artifactId>spring-restdocs-mockmvc</artifactId>
	<version>{project-version}</version>
	<scope>test</scope>
</dependency>

<build>
	<plugins>
		<plugin> (2)
			<groupId>org.asciidoctor</groupId>
			<artifactId>asciidoctor-maven-plugin</artifactId>
			<version>2.2.1</version>
			<executions>
				<execution>
					<id>generate-docs</id>
					<phase>prepare-package</phase> (3)
					<goals>
						<goal>process-asciidoc</goal>
					</goals>
					<configuration>
						<backend>html</backend>
						<doctype>book</doctype>
					</configuration>
				</execution>
			</executions>
			<dependencies>
				<dependency> (4)
					<groupId>org.springframework.restdocs</groupId>
					<artifactId>spring-restdocs-asciidoctor</artifactId>
					<version>{project-version}</version>
				</dependency>
			</dependencies>
		</plugin>
	</plugins>
</build>
```

**1**

Add a dependency on `spring-restdocs-mockmvc` in the `test` scope.
If you want to use `WebTestClient` or REST Assured rather than MockMvc, add a dependency on `spring-restdocs-webtestclient` or `spring-restdocs-restassured` respectively instead.

**2**

Add the Asciidoctor plugin.

**3**

Using `prepare-package` allows the documentation to be [included in the package](#index--getting-started-build-configuration-packaging-the-documentation).

**4**

Add `spring-restdocs-asciidoctor` as a dependency of the Asciidoctor plugin.
This will automatically configure the `snippets` attribute for use in your `.adoc` files to point to `target/generated-snippets`.
It will also allow you to use the `operation` block macro.

Gradle

```
plugins { (1) id "org.asciidoctor.jvm.convert" version "3.3.2"}
configurations {asciidoctorExt (2)}
dependencies {asciidoctorExt 'org.springframework.restdocs:spring-restdocs-asciidoctor:{project-version}' (3) testImplementation 'org.springframework.restdocs:spring-restdocs-mockmvc:{project-version}' (4)}
ext { (5) snippetsDir = file('build/generated-snippets')}
test { (6) outputs.dir snippetsDir}
asciidoctor { (7) inputs.dir snippetsDir (8) configurations 'asciidoctorExt' (9) dependsOn test (10)}
```

| **1** | Apply the Asciidoctor plugin. |
| --- | --- |
| **2** | Declare the `asciidoctorExt` configuration for dependencies that extend Asciidoctor. |
| **3** | Add a dependency on `spring-restdocs-asciidoctor` in the `asciidoctorExt` configuration. This will automatically configure the `snippets` attribute for use in your `.adoc` files to point to `build/generated-snippets`. It will also allow you to use the `operation` block macro. |
| **4** | Add a dependency on `spring-restdocs-mockmvc` in the `testImplementation` configuration. If you want to use `WebTestClient` or REST Assured rather than MockMvc, add a dependency on `spring-restdocs-webtestclient` or `spring-restdocs-restassured` respectively instead. |
| **5** | Configure a `snippetsDir` property that defines the output location for generated snippets. |
| **6** | Make Gradle aware that running the `test` task will write output to the snippetsDir. This is required for [incremental builds](https://docs.gradle.org/current/userguide/incremental_build.html). |
| **7** | Configure the `asciidoctor` task. |
| **8** | Make Gradle aware that running the task will read input from the snippetsDir. This is required for [incremental builds](https://docs.gradle.org/current/userguide/incremental_build.html). |
| **9** | Configure the use of the `asciidoctorExt` configuration for extensions. |
| **10** | Make the task depend on the `test` task so that the tests are run before the documentation is created. |

<a id="index--getting-started-build-configuration-packaging-the-documentation"></a>
<a id="index--packaging-the-documentation"></a>

#### [Packaging the Documentation](#index--getting-started-build-configuration-packaging-the-documentation)

You may want to package the generated documentation in your project’s jar file — for example, to have it [served as static content](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#boot-features-spring-mvc-static-content) by Spring Boot.
To do so, configure your project’s build so that:

1. The documentation is generated before the jar is built
2. The generated documentation is included in the jar

The following listings show how to do so in both Maven and Gradle:

Maven

```xml
<plugin> (1)
	<groupId>org.asciidoctor</groupId>
	<artifactId>asciidoctor-maven-plugin</artifactId>
	<!-- … -->
</plugin>
<plugin> (2)
	<artifactId>maven-resources-plugin</artifactId>
	<executions>
		<execution>
			<id>copy-resources</id>
			<phase>prepare-package</phase>
			<goals>
				<goal>copy-resources</goal>
			</goals>
			<configuration> (3)
				<outputDirectory>
					${project.build.outputDirectory}/static/docs
				</outputDirectory>
				<resources>
					<resource>
						<directory>
							${project.build.directory}/generated-docs
						</directory>
					</resource>
				</resources>
			</configuration>
		</execution>
	</executions>
</plugin>
```

| **1** | The existing declaration for the Asciidoctor plugin. |
| --- | --- |
| **2** | The resource plugin must be declared after the Asciidoctor plugin as they are bound to the same phase (`prepare-package`) and the resource plugin must run after the Asciidoctor plugin to ensure that the documentation is generated before it’s copied. If you are not using Spring Boot and its plugin management, declare the plugin with an appropriate `<version>`. |
| **3** | Copy the generated documentation into the build output’s `static/docs` directory, from where it will be included in the jar file. |

Gradle

```
bootJar {
	dependsOn asciidoctor (1)
	from ("${asciidoctor.outputDir}") { (2)
		into 'static/docs'
	}
}
```

**1**

Ensure that the documentation has been generated before the jar is built.

**2**

Copy the generated documentation into the jar’s `static/docs` directory.

<a id="index--getting-started-documentation-snippets"></a>
<a id="index--generating-documentation-snippets"></a>

### [Generating Documentation Snippets](#index--getting-started-documentation-snippets)

Spring REST Docs uses Spring MVC’s [test framework](https://docs.spring.io/spring-framework/reference/6.2/testing/mockmvc.html), Spring WebFlux’s [`WebTestClient`](https://docs.spring.io/spring-framework/reference/6.2/testing/webtestclient.html), or [REST Assured](https://rest-assured.io/) to make requests to the service that you are documenting.
It then produces documentation snippets for the request and the resulting response.

<a id="index--getting-started-documentation-snippets-setup"></a>
<a id="index--setting-up-your-tests"></a>

#### [Setting up Your Tests](#index--getting-started-documentation-snippets-setup)

Exactly how you set up your tests depends on the test framework that you use.
Spring REST Docs provides first-class support for JUnit 5 and JUnit 4.
JUnit 5 is recommended.
Other frameworks, such as TestNG, are also supported, although slightly more setup is required.

<a id="index--getting-started-documentation-snippets-setup-junit-5"></a>
<a id="index--setting-up-your-junit-5-tests"></a>

##### [Setting up Your JUnit 5 Tests](#index--getting-started-documentation-snippets-setup-junit-5)

When using JUnit 5, the first step in generating documentation snippets is to apply the `RestDocumentationExtension` to your test class.
The following example shows how to do so:

```java
@ExtendWith(RestDocumentationExtension.class)
public class JUnit5ExampleTests {
```

When testing a typical Spring application, you should also apply the `SpringExtension`:

```java
@ExtendWith({RestDocumentationExtension.class, SpringExtension.class})
public class JUnit5ExampleTests {
```

The `RestDocumentationExtension` is automatically configured with an output directory based on your project’s build tool:

| Build tool | Output directory |
| --- | --- |
| Maven | `target/generated-snippets` |
| Gradle | `build/generated-snippets` |

If you are using JUnit 5.1, you can override the default by registering the extension as a field in your test class and providing an output directory when creating it.
The following example shows how to do so:

```java
public class JUnit5ExampleTests {

	@RegisterExtension
	final RestDocumentationExtension restDocumentation = new RestDocumentationExtension ("custom");

}
```

Next, you must provide a `@BeforeEach` method to configure MockMvc or WebTestClient, or REST Assured.
The following listings show how to do so:

MockMvc

```java
private MockMvc mockMvc;

@BeforeEach
void setUp(WebApplicationContext webApplicationContext, RestDocumentationContextProvider restDocumentation) {
	this.mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext)
		.apply(documentationConfiguration(restDocumentation)) (1)
		.build();
}
```

**1**

The `MockMvc` instance is configured by using a `MockMvcRestDocumentationConfigurer`.
You can obtain an instance of this class from the static `documentationConfiguration()` method on `org.springframework.restdocs.mockmvc.MockMvcRestDocumentation`.

WebTestClient

```java
private WebTestClient webTestClient;

@BeforeEach
void setUp(ApplicationContext applicationContext, RestDocumentationContextProvider restDocumentation) {
	this.webTestClient = WebTestClient.bindToApplicationContext(applicationContext)
		.configureClient()
		.filter(documentationConfiguration(restDocumentation)) (1)
		.build();
}
```

**1**

The `WebTestClient` instance is configured by adding a `WebTestClientRestDocumentationConfigurer` as an `ExchangeFilterFunction`.
You can obtain an instance of this class from the static `documentationConfiguration()` method on `org.springframework.restdocs.webtestclient.WebTestClientRestDocumentation`.

REST Assured

```java
private RequestSpecification spec;

@BeforeEach
void setUp(RestDocumentationContextProvider restDocumentation) {
	this.spec = new RequestSpecBuilder().addFilter(documentationConfiguration(restDocumentation)) (1)
		.build();
}
```

**1**

REST Assured is configured by adding a `RestAssuredRestDocumentationConfigurer` as a `Filter`.
You can obtain an instance of this class from the static `documentationConfiguration()` method on `RestAssuredRestDocumentation` in the `org.springframework.restdocs.restassured` package.

The configurer applies sensible defaults and also provides an API for customizing the configuration.
See the [configuration section](#index--configuration) for more information.

<a id="index--getting-started-documentation-snippets-setup-junit"></a>
<a id="index--setting-up-your-junit-4-tests"></a>

##### [Setting up Your JUnit 4 Tests](#index--getting-started-documentation-snippets-setup-junit)

When using JUnit 4, the first step in generating documentation snippets is to declare a `public` `JUnitRestDocumentation` field that is annotated as a JUnit `@Rule`.
The following example shows how to do so:

```java
@Rule
public JUnitRestDocumentation restDocumentation = new JUnitRestDocumentation();
```

By default, the `JUnitRestDocumentation` rule is automatically configured with an output directory based on your project’s build tool:

| Build tool | Output directory |
| --- | --- |
| Maven | `target/generated-snippets` |
| Gradle | `build/generated-snippets` |

You can override the default by providing an output directory when you create the `JUnitRestDocumentation` instance.
The following example shows how to do so:

```java
@Rule
public JUnitRestDocumentation restDocumentation = new JUnitRestDocumentation("custom");
```

Next, you must provide an `@Before` method to configure MockMvc or WebTestClient, or REST Assured.
The following examples show how to do so:

MockMvc

```java
private MockMvc mockMvc;

@Autowired
private WebApplicationContext context;

@Before
public void setUp() {
	this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
		.apply(documentationConfiguration(this.restDocumentation)) (1)
		.build();
}
```

**1**

The `MockMvc` instance is configured by using a `MockMvcRestDocumentationConfigurer`.
You can obtain an instance of this class from the static `documentationConfiguration()` method on `org.springframework.restdocs.mockmvc.MockMvcRestDocumentation`.

WebTestClient

```java
private WebTestClient webTestClient;

@Autowired
private ApplicationContext context;

@Before
public void setUp() {
	this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
		.configureClient()
		.filter(documentationConfiguration(this.restDocumentation)) (1)
		.build();
}
```

**1**

The `WebTestClient` instance is configured by adding a `WebTestclientRestDocumentationConfigurer` as an `ExchangeFilterFunction`.
You can obtain an instance of this class from the static `documentationConfiguration()` method on `org.springframework.restdocs.webtestclient.WebTestClientRestDocumentation`.

REST Assured

```java
private RequestSpecification spec;

@Before
public void setUp() {
	this.spec = new RequestSpecBuilder().addFilter(documentationConfiguration(this.restDocumentation)) (1)
		.build();
}
```

**1**

REST Assured is configured by adding a `RestAssuredRestDocumentationConfigurer` as a `Filter`.
You can obtain an instance of this class from the static `documentationConfiguration()` method on `RestAssuredRestDocumentation` in the `org.springframework.restdocs.restassured` package.

The configurer applies sensible defaults and also provides an API for customizing the configuration.
See the [configuration section](#index--configuration) for more information.

<a id="index--getting-started-documentation-snippets-setup-manual"></a>
<a id="index--setting-up-your-tests-without-junit"></a>

##### [Setting up your tests without JUnit](#index--getting-started-documentation-snippets-setup-manual)

The configuration when JUnit is not being used is largely similar to when it is being used.
This section describes the key differences.
The [TestNG sample](https://github.com/spring-projects/spring-restdocs-samples/tree/main/testng) also illustrates the approach.

The first difference is that you should use `ManualRestDocumentation` in place of `JUnitRestDocumentation`.
Also, you do not need the `@Rule` annotation.
The following example shows how to use `ManualRestDocumentation`:

```java
private ManualRestDocumentation restDocumentation = new ManualRestDocumentation();
```

Secondly, you must call `ManualRestDocumentation.beforeTest(Class, String)` before each test.
You can do so as part of the method that configures MockMvc, WebTestClient, or REST Assured.
The following examples show how to do so:

MockMvc

```java
private MockMvc mockMvc;

@Autowired
private WebApplicationContext context;

@BeforeMethod
public void setUp(Method method) {
	this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
		.apply(documentationConfiguration(this.restDocumentation))
		.build();
	this.restDocumentation.beforeTest(getClass(), method.getName());
}
```

WebTestClient

```java
private WebTestClient webTestClient;

@Autowired
private ApplicationContext context;

@BeforeMethod
public void setUp(Method method) {
	this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
		.configureClient()
		.filter(documentationConfiguration(this.restDocumentation)) (1)
		.build();
	this.restDocumentation.beforeTest(getClass(), method.getName());
}
```

REST Assured

```java
private RequestSpecification spec;

@BeforeMethod
public void setUp(Method method) {
	this.spec = new RequestSpecBuilder().addFilter(documentationConfiguration(this.restDocumentation)).build();
	this.restDocumentation.beforeTest(getClass(), method.getName());
}
```

Finally, you must call `ManualRestDocumentation.afterTest` after each test.
The following example shows how to do so with TestNG:

```java
@AfterMethod
public void tearDown() {
	this.restDocumentation.afterTest();
}
```

<a id="index--getting-started-documentation-snippets-invoking-the-service"></a>
<a id="index--invoking-the-restful-service"></a>

#### [Invoking the RESTful Service](#index--getting-started-documentation-snippets-invoking-the-service)

Now that you have configured the testing framework, you can use it to invoke the RESTful service and document the request and response.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/").accept(MediaType.APPLICATION_JSON)) (1)
	.andExpect(status().isOk()) (2)
	.andDo(document("index")); (3)
```

**1**

Invoke the root (`/`) of the service and indicate that an `application/json` response is required.

**2**

Assert that the service produced the expected response.

**3**

Document the call to the service, writing the snippets into a directory named `index` (which is located beneath the configured output directory).
The snippets are written by a `RestDocumentationResultHandler`.
You can obtain an instance of this class from the static `document` method on `org.springframework.restdocs.mockmvc.MockMvcRestDocumentation`.

WebTestClient

```java
this.webTestClient.get()
	.uri("/")
	.accept(MediaType.APPLICATION_JSON) (1)
	.exchange()
	.expectStatus()
	.isOk() (2)
	.expectBody()
	.consumeWith(document("index")); (3)
```

**1**

Invoke the root (`/`) of the service and indicate that an `application/json` response is required.

**2**

Assert that the service produced the expected response.

**3**

Document the call to the service, writing the snippets into a directory named `index` (which is located beneath the configured output directory).
The snippets are written by a `Consumer` of the `ExchangeResult`.
You can obtain such a consumer from the static `document` method on `org.springframework.restdocs.webtestclient.WebTestClientRestDocumentation`.

REST Assured

```java
RestAssured.given(this.spec) (1)
	.accept("application/json") (2)
	.filter(document("index")) (3)
	.when()
	.get("/") (4)
	.then()
	.assertThat()
	.statusCode(is(200)); (5)
```

| **1** | Apply the specification that was initialized in the `@Before` method. |
| --- | --- |
| **2** | Indicate that an `application/json` response is required. |
| **3** | Document the call to the service, writing the snippets into a directory named `index` (which is located beneath the configured output directory). The snippets are written by a `RestDocumentationFilter`. You can obtain an instance of this class from the static `document` method on `RestAssuredRestDocumentation` in the `org.springframework.restdocs.restassured` package. |
| **4** | Invoke the root (`/`) of the service. |
| **5** | Assert that the service produce the expected response. |

By default, six snippets are written:

- `<output-directory>/index/curl-request.adoc`
- `<output-directory>/index/http-request.adoc`
- `<output-directory>/index/http-response.adoc`
- `<output-directory>/index/httpie-request.adoc`
- `<output-directory>/index/request-body.adoc`
- `<output-directory>/index/response-body.adoc`

See [Documenting your API](#index--documenting-your-api) for more information about these and other snippets that can be produced by Spring REST Docs.

<a id="index--getting-started-using-the-snippets"></a>
<a id="index--using-the-snippets"></a>

### [Using the Snippets](#index--getting-started-using-the-snippets)

Before using the generated snippets, you must create an `.adoc` source file.
You can name the file whatever you like as long as it has a `.adoc` suffix.
The resulting HTML file has the same name but with a `.html` suffix.
The default location of the source files and the resulting HTML files depends on whether you use Maven or Gradle:

| Build tool | Source files | Generated files |
| --- | --- | --- |
| Maven | `src/main/asciidoc/*.adoc` | `target/generated-docs/*.html` |
| Gradle | `src/docs/asciidoc/*.adoc` | `build/asciidoc/html5/*.html` |

You can then include the generated snippets in the manually created Asciidoc file (described earlier in this section) by using the [include macro](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#include-files).
You can use the `snippets` attribute that is automatically set by `spring-restdocs-asciidoctor` configured in the [build configuration](#index--getting-started-build-configuration) to reference the snippets output directory.
The following example shows how to do so:

```adoc
include::{snippets}/index/curl-request.adoc[]
```

<a id="index--documenting-your-api"></a>

## [Documenting your API](#index--documenting-your-api)

This section provides more details about using Spring REST Docs to document your API.

<a id="index--documenting-your-api-hypermedia"></a>
<a id="index--hypermedia"></a>

### [Hypermedia](#index--documenting-your-api-hypermedia)

Spring REST Docs provides support for documenting the links in a [hypermedia-based](https://en.wikipedia.org/wiki/HATEOAS) API.
The following examples show how to use it:

MockMvc

```java
this.mockMvc.perform(get("/").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("index", links((1)
			linkWithRel("alpha").description("Link to the alpha resource"), (2)
			linkWithRel("bravo").description("Link to the bravo resource")))); (3)
```

**1**

Configure Spring REST docs to produce a snippet describing the response’s links.
Uses the static `links` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

**2**

Expect a link whose `rel` is `alpha`.
Uses the static `linkWithRel` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

**3**

Expect a link whose `rel` is `bravo`.

WebTestClient

```java
this.webTestClient.get()
	.uri("/")
	.accept(MediaType.APPLICATION_JSON)
	.exchange()
	.expectStatus()
	.isOk()
	.expectBody()
	.consumeWith(document("index", links((1)
			linkWithRel("alpha").description("Link to the alpha resource"), (2)
			linkWithRel("bravo").description("Link to the bravo resource")))); (3)
```

**1**

Configure Spring REST docs to produce a snippet describing the response’s links.
Uses the static `links` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

**2**

Expect a link whose `rel` is `alpha`.
Uses the static `linkWithRel` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

**3**

Expect a link whose `rel` is `bravo`.

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("index", links((1)
			linkWithRel("alpha").description("Link to the alpha resource"), (2)
			linkWithRel("bravo").description("Link to the bravo resource")))) (3)
	.get("/")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST docs to produce a snippet describing the response’s links.
Uses the static `links` method on
`org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

**2**

Expect a link whose `rel` is `alpha`. Uses the static `linkWithRel` method on
`org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

**3**

Expect a link whose `rel` is `bravo`.

The result is a snippet named `links.adoc` that contains a table describing the resource’s links.

> [!TIP]
> If a link in the response has a `title`, you can omit the description from its descriptor and the `title` is used.
> If you omit the description and the link does not have a `title`, a failure occurs.

When documenting links, the test fails if an undocumented link is found in the response.
Similarly, the test also fails if a documented link is not found in the response and the link has not been marked as optional.

If you do not want to document a link, you can mark it as ignored.
Doing so prevents it from appearing in the generated snippet while avoiding the failure described above.

You can also document links in a relaxed mode, where any undocumented links do not cause a test failure.
To do so, use the `relaxedLinks` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the links.

<a id="index--documenting-your-api-hypermedia-link-formats"></a>
<a id="index--hypermedia-link-formats"></a>

#### [Hypermedia Link Formats](#index--documenting-your-api-hypermedia-link-formats)

Two link formats are understood by default:

- Atom: Links are expected to be in an array named `links`.
  This is used by default when the content type of the response is compatible with `application/json`.
- HAL: Links are expected to be in a map named `_links`.
  This is used by default when the content type of the response is compatible with `application/hal+json`.

If you use Atom- or HAL-format links but with a different content type, you can provide one of the built-in `LinkExtractor` implementations to `links`.
The following examples show how to do so:

MockMvc

```java
.andDo(document("index", links(halLinks(), (1)
		linkWithRel("alpha").description("Link to the alpha resource"),
		linkWithRel("bravo").description("Link to the bravo resource"))));
```

**1**

Indicate that the links are in HAL format.
Uses the static `halLinks` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

WebTestClient

```java
.consumeWith(document("index", links(halLinks(), (1)
		linkWithRel("alpha").description("Link to the alpha resource"),
		linkWithRel("bravo").description("Link to the bravo resource"))));
```

**1**

Indicate that the links are in HAL format.
Uses the static `halLinks` method on `org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

REST Assured

```java
.filter(document("index", links(halLinks(), (1)
		linkWithRel("alpha").description("Link to the alpha resource"),
		linkWithRel("bravo").description("Link to the bravo resource"))))
```

**1**

Indicate that the links are in HAL format. Uses the static `halLinks` method on
`org.springframework.restdocs.hypermedia.HypermediaDocumentation`.

If your API represents its links in a format other than Atom or HAL, you can provide your own implementation of the `LinkExtractor` interface to extract the links from the response.

<a id="index--documenting-your-api-hypermedia-ignoring-common-links"></a>
<a id="index--ignoring-common-links"></a>

#### [Ignoring Common Links](#index--documenting-your-api-hypermedia-ignoring-common-links)

Rather than documenting links that are common to every response, such as `self` and `curies` when using HAL, you may want to document them once in an overview section and then ignore them in the rest of your API’s documentation.
To do so, you can build on the [support for reusing snippets](#index--documenting-your-api-reusing-snippets) to add link descriptors to a snippet that is preconfigured to ignore certain links.
The following example shows how to do so:

```java
public static LinksSnippet links(LinkDescriptor... descriptors) {
	return HypermediaDocumentation.links(linkWithRel("self").ignored().optional(), linkWithRel("curies").ignored())
		.and(descriptors);
}
```

<a id="index--documenting-your-api-request-response-payloads"></a>
<a id="index--request-and-response-payloads"></a>

### [Request and Response Payloads](#index--documenting-your-api-request-response-payloads)

In addition to the hypermedia-specific support [described earlier](#index--documenting-your-api-hypermedia), support for general documentation of request and response payloads is also provided.

By default, Spring REST Docs automatically generates snippets for the body of the request and the body of the response.
These snippets are named `request-body.adoc` and `response-body.adoc` respectively.

<a id="index--documenting-your-api-request-response-payloads-fields"></a>
<a id="index--request-and-response-fields"></a>

#### [Request and Response Fields](#index--documenting-your-api-request-response-payloads-fields)

To provide more detailed documentation of a request or response payload, support for documenting the payload’s fields is provided.

Consider the following payload:

```json
{
	"contact": {
		"name": "Jane Doe",
		"email": "[email protected]"
	}
}
```

You can document the previous example’s fields as follows:

MockMvc

```java
this.mockMvc.perform(get("/user/5").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("index", responseFields((1)
			fieldWithPath("contact.email").description("The user's email address"), (2)
			fieldWithPath("contact.name").description("The user's name")))); (3)
```

**1**

Configure Spring REST docs to produce a snippet describing the fields in the response payload.
To document a request, you can use `requestFields`.
Both are static methods on `org.springframework.restdocs.payload.PayloadDocumentation`.

**2**

Expect a field with the path `contact.email`.
Uses the static `fieldWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

**3**

Expect a field with the path `contact.name`.

WebTestClient

```java
this.webTestClient.get().uri("user/5").accept(MediaType.APPLICATION_JSON)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("user",
		responseFields((1)
			fieldWithPath("contact.email").description("The user's email address"), (2)
			fieldWithPath("contact.name").description("The user's name")))); (3)
```

**1**

Configure Spring REST docs to produce a snippet describing the fields in the response payload.
To document a request, you can use `requestFields`.
Both are static methods on `org.springframework.restdocs.payload.PayloadDocumentation`.

**2**

Expect a field with the path `contact.email`.
Uses the static `fieldWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

**3**

Expect a field with the path `contact.name`.

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("user", responseFields((1)
			fieldWithPath("contact.name").description("The user's name"), (2)
			fieldWithPath("contact.email").description("The user's email address")))) (3)
	.when()
	.get("/user/5")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST docs to produce a snippet describing the fields in the response payload.
To document a request, you can use `requestFields`.
Both are static methods on `org.springframework.restdocs.payload.PayloadDocumentation`.

**2**

Expect a field with the path `contact.email`.
Uses the static `fieldWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

**3**

Expect a field with the path `contact.name`.

The result is a snippet that contains a table describing the fields.
For requests, this snippet is named `request-fields.adoc`.
For responses, this snippet is named `response-fields.adoc`.

When documenting fields, the test fails if an undocumented field is found in the payload.
Similarly, the test also fails if a documented field is not found in the payload and the field has not been marked as optional.

If you do not want to provide detailed documentation for all of the fields, an entire subsection of a payload can be documented.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/user/5").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("index", responseFields((1)
			subsectionWithPath("contact").description("The user's contact details")))); (1)
```

**1**

Document the subsection with the path `contact`.
`contact.email` and `contact.name` are now seen as having also been documented.
Uses the static `subsectionWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

WebTestClient

```java
this.webTestClient.get().uri("user/5").accept(MediaType.APPLICATION_JSON)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("user",
		responseFields(
			subsectionWithPath("contact").description("The user's contact details")))); (1)
```

**1**

Document the subsection with the path `contact`.
`contact.email` and `contact.name` are now seen as having also been documented.
Uses the static `subsectionWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("user",
			responseFields(subsectionWithPath("contact").description("The user's contact details")))) (1)
	.when()
	.get("/user/5")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Document the subsection with the path `contact`. `contact.email` and `contact.name` are now seen as having also been documented.
Uses the static `subsectionWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

`subsectionWithPath` can be useful for providing a high-level overview of a particular section of a payload.
You can then produce separate, more detailed documentation for a subsection.
See [Documenting a Subsection of a Request or Response Payload](#index--documenting-your-api-request-response-payloads-subsections).

If you do not want to document a field or subsection at all, you can mark it as ignored.
This prevents it from appearing in the generated snippet while avoiding the failure described earlier.

You can also document fields in a relaxed mode, where any undocumented fields do not cause a test failure.
To do so, use the `relaxedRequestFields` and `relaxedResponseFields` methods on `org.springframework.restdocs.payload.PayloadDocumentation`.
This can be useful when documenting a particular scenario where you want to focus only on a subset of the payload.

> [!TIP]
> By default, Spring REST Docs assumes that the payload you are documenting is JSON.
> If you want to document an XML payload, the content type of the request or response must be compatible with `application/xml`.

<a id="index--documenting-your-api-request-response-payloads-fields-json"></a>
<a id="index--fields-in-json-payloads"></a>

##### [Fields in JSON Payloads](#index--documenting-your-api-request-response-payloads-fields-json)

This section describes how to work with fields in JSON payloads.

<a id="index--documenting-your-api-request-response-payloads-fields-json-field-paths"></a>
<a id="index--json-field-paths"></a>

###### [JSON Field Paths](#index--documenting-your-api-request-response-payloads-fields-json-field-paths)

JSON field paths use either dot notation or bracket notation.
Dot notation uses '.' to separate each key in the path (for example, `a.b`).
Bracket notation wraps each key in square brackets and single quotation marks (for example, `['a']['b']`).
In either case, `[]` is used to identify an array.
Dot notation is more concise, but using bracket notation enables the use of `.` within a key name (for example, `['a.b']`).
The two different notations can be used in the same path (for example, `a['b']`).

Consider the following JSON payload:

```json
{"a":{"b":[{"c":"one" },{"c":"two" },{"d":"three"} ],"e.dot" : "four"}}
```

In the preceding JSON payload, the following paths are all present:

| Path | Value |
| --- | --- |
| `a` | An object containing `b` |
| `a.b` | An array containing three objects |
| `['a']['b']` | An array containing three objects |
| `a['b']` | An array containing three objects |
| `['a'].b` | An array containing three objects |
| `a.b[]` | An array containing three objects |
| `a.b[].c` | An array containing the strings `one` and `two` |
| `a.b[].d` | The string `three` |
| `a['e.dot']` | The string `four` |
| `['a']['e.dot']` | The string `four` |

You can also document a payload that uses an array at its root.
The path `[]` refers to the entire array.
You can then use bracket or dot notation to identify fields within the array’s entries.
For example, `[].id` corresponds to the `id` field of every object found in the following array:

```json
[{"id":1 },{"id":2}]
```

You can use `*` as a wildcard to match fields with different names.
For example, `users.*.role` could be used to document the role of every user in the following JSON:

```json
{"users":{"ab12cd34":{"role": "Administrator" },"12ab34cd":{"role": "Guest"}}}
```

<a id="index--documenting-your-api-request-response-payloads-fields-json-field-types"></a>
<a id="index--json-field-types"></a>

###### [JSON Field Types](#index--documenting-your-api-request-response-payloads-fields-json-field-types)

When a field is documented, Spring REST Docs tries to determine its type by examining the payload.
Seven different types are supported:

| Type | Description |
| --- | --- |
| `array` | The value of each occurrence of the field is an array. |
| `boolean` | The value of each occurrence of the field is a boolean (`true` or `false`). |
| `object` | The value of each occurrence of the field is an object. |
| `number` | The value of each occurrence of the field is a number. |
| `null` | The value of each occurrence of the field is `null`. |
| `string` | The value of each occurrence of the field is a string. |
| `varies` | The field occurs multiple times in the payload with a variety of different types. |

You can also explicitly set the type by using the `type(Object)` method on `FieldDescriptor`.
The result of the `toString` method of the supplied `Object` is used in the documentation.
Typically, one of the values enumerated by `JsonFieldType` is used.
The following examples show how to do so:

MockMvc

```java
.andDo(document("index", responseFields(fieldWithPath("contact.email").type(JsonFieldType.STRING) (1)
	.description("The user's email address"))));
```

**1**

Set the field’s type to `String`.

WebTestClient

```java
.consumeWith(document("user",
	responseFields(
		fieldWithPath("contact.email")
			.type(JsonFieldType.STRING) (1)
			.description("The user's email address"))));
```

**1**

Set the field’s type to `String`.

REST Assured

```java
.filter(document("user", responseFields(fieldWithPath("contact.email").type(JsonFieldType.STRING) (1)
	.description("The user's email address"))))
```

**1**

Set the field’s type to `String`.

<a id="index--documenting-your-api-request-response-payloads-fields-xml"></a>
<a id="index--xml-payloads"></a>

##### [XML payloads](#index--documenting-your-api-request-response-payloads-fields-xml)

This section describes how to work with XML payloads.

<a id="index--documenting-your-api-request-response-payloads-fields-xml-field-paths"></a>
<a id="index--xml-field-paths"></a>

###### [XML Field Paths](#index--documenting-your-api-request-response-payloads-fields-xml-field-paths)

XML field paths are described using XPath.
`/` is used to descend into a child node.

<a id="index--documenting-your-api-request-response-payloads-fields-xml-field-types"></a>
<a id="index--xml-field-types"></a>

###### [XML Field Types](#index--documenting-your-api-request-response-payloads-fields-xml-field-types)

When documenting an XML payload, you must provide a type for the field by using the `type(Object)` method on `FieldDescriptor`.
The result of the supplied type’s `toString` method is used in the documentation.

<a id="index--documenting-your-api-request-response-payloads-fields-reusing-field-descriptors"></a>
<a id="index--reusing-field-descriptors"></a>

##### [Reusing Field Descriptors](#index--documenting-your-api-request-response-payloads-fields-reusing-field-descriptors)

In addition to the general support for [reusing snippets](#index--documenting-your-api-reusing-snippets), the request and response snippets let additional descriptors be configured with a path prefix.
This lets the descriptors for a repeated portion of a request or response payload be created once and then reused.

Consider an endpoint that returns a book:

```json
{
	"title": "Pride and Prejudice",
	"author": "Jane Austen"
}
```

The paths for `title` and `author` are `title` and `author`, respectively.

Now consider an endpoint that returns an array of books:

```json
[{"title": "Pride and Prejudice","author": "Jane Austen" },{"title": "To Kill a Mockingbird","author": "Harper Lee" }]
```

The paths for `title` and `author` are `[].title` and `[].author`, respectively.
The only difference between the single book and the array of books is that the fields' paths now have a `[].` prefix.

You can create the descriptors that document a book as follows:

```java
FieldDescriptor[] book = new FieldDescriptor[] { fieldWithPath("title").description("Title of the book"),
		fieldWithPath("author").description("Author of the book") };
```

You can then use them to document a single book, as follows:

MockMvc

```java
this.mockMvc.perform(get("/books/1").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("book", responseFields(book))); (1)
```

**1**

Document `title` and `author` by using existing descriptors

WebTestClient

```java
this.webTestClient.get().uri("/books/1").accept(MediaType.APPLICATION_JSON)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("book",
		responseFields(book))); (1)
```

**1**

Document `title` and `author` by using existing descriptors

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("book", responseFields(book))) (1)
	.when()
	.get("/books/1")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Document `title` and `author` by using existing descriptors

You can also use the descriptors to document an array of books, as follows:

MockMvc

```java
this.mockMvc.perform(get("/books").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("book", responseFields(fieldWithPath("[]").description("An array of books")) (1)
		.andWithPrefix("[].", book))); (2)
```

**1**

Document the array.

**2**

Document `[].title` and `[].author` by using the existing descriptors prefixed with `[].`

WebTestClient

```java
this.webTestClient.get().uri("/books").accept(MediaType.APPLICATION_JSON)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("books",
		responseFields(
			fieldWithPath("[]")
				.description("An array of books")) (1)
				.andWithPrefix("[].", book))); (2)
```

**1**

Document the array.

**2**

Document `[].title` and `[].author` by using the existing descriptors prefixed with `[].`

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("books", responseFields(fieldWithPath("[]").description("An array of books")) (1)
		.andWithPrefix("[].", book))) (2)
	.when()
	.get("/books")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Document the array.

**2**

Document `[].title` and `[].author` by using the existing descriptors prefixed with `[].`

<a id="index--documenting-your-api-request-response-payloads-subsections"></a>
<a id="index--documenting-a-subsection-of-a-request-or-response-payload"></a>

#### [Documenting a Subsection of a Request or Response Payload](#index--documenting-your-api-request-response-payloads-subsections)

If a payload is large or structurally complex, it can be useful to document individual sections of the payload.
REST Docs let you do so by extracting a subsection of the payload and then documenting it.

<a id="index--documenting-your-api-request-response-payloads-subsections-body"></a>
<a id="index--documenting-a-subsection-of-a-request-or-response-body"></a>

##### [Documenting a Subsection of a Request or Response Body](#index--documenting-your-api-request-response-payloads-subsections-body)

Consider the following JSON response body:

```json
{"weather": {"wind": {"speed": 15.3,"direction": 287.0 },"temperature": {"high": 21.2,"low": 14.8}}}
```

You can produce a snippet that documents the `temperature` object as follows:

MockMvc

```java
this.mockMvc.perform(get("/locations/1").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("location", responseBody(beneathPath("weather.temperature")))); (1)
```

**1**

Produce a snippet containing a subsection of the response body.
Uses the static `responseBody` and `beneathPath` methods on `org.springframework.restdocs.payload.PayloadDocumentation`.
To produce a snippet for the request body, you can use `requestBody` in place of `responseBody`.

WebTestClient

```java
this.webTestClient.get().uri("/locations/1").accept(MediaType.APPLICATION_JSON)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("temperature",
		responseBody(beneathPath("weather.temperature")))); (1)
```

**1**

Produce a snippet containing a subsection of the response body.
Uses the static `responseBody` and `beneathPath` methods on `org.springframework.restdocs.payload.PayloadDocumentation`.
To produce a snippet for the request body, you can use `requestBody` in place of `responseBody`.

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("location", responseBody(beneathPath("weather.temperature")))) (1)
	.when()
	.get("/locations/1")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Produce a snippet containing a subsection of the response body.
Uses the static `responseBody` and `beneathPath` methods on `org.springframework.restdocs.payload.PayloadDocumentation`.
To produce a snippet for the request body, you can use `requestBody` in place of `responseBody`.

The result is a snippet with the following contents:

```json
{
	"temperature": {
		"high": 21.2,
		"low": 14.8
	}
}
```

To make the snippet’s name distinct, an identifier for the subsection is included.
By default, this identifier is `beneath-${path}`.
For example, the preceding code results in a snippet named `response-body-beneath-weather.temperature.adoc`.
You can customize the identifier by using the `withSubsectionId(String)` method, as follows:

```java
responseBody(beneathPath("weather.temperature").withSubsectionId("temp"));
```

The result is a snippet named `request-body-temp.adoc`.

<a id="index--documenting-your-api-request-response-payloads-subsections-fields"></a>
<a id="index--documenting-the-fields-of-a-subsection-of-a-request-or-response"></a>

##### [Documenting the Fields of a Subsection of a Request or Response](#index--documenting-your-api-request-response-payloads-subsections-fields)

As well as documenting a subsection of a request or response body, you can also document the fields in a particular subsection.
You can produce a snippet that documents the fields of the `temperature` object (`high` and `low`) as follows:

MockMvc

```java
this.mockMvc.perform(get("/locations/1").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("location", responseFields(beneathPath("weather.temperature"), (1)
			fieldWithPath("high").description("The forecast high in degrees celcius"), (2)
			fieldWithPath("low").description("The forecast low in degrees celcius"))));
```

**1**

Produce a snippet describing the fields in the subsection of the response payload beneath the path `weather.temperature`.
Uses the static `beneathPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

**2**

Document the `high` and `low` fields.

WebTestClient

```java
this.webTestClient.get().uri("/locations/1").accept(MediaType.APPLICATION_JSON)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("temperature",
		responseFields(beneathPath("weather.temperature"), (1)
			fieldWithPath("high").description("The forecast high in degrees celcius"), (2)
			fieldWithPath("low").description("The forecast low in degrees celcius"))));
```

**1**

Produce a snippet describing the fields in the subsection of the response payload beneath the path `weather.temperature`.
Uses the static `beneathPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

**2**

Document the `high` and `low` fields.

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("location", responseFields(beneathPath("weather.temperature"), (1)
			fieldWithPath("high").description("The forecast high in degrees celcius"), (2)
			fieldWithPath("low").description("The forecast low in degrees celcius"))))
	.when()
	.get("/locations/1")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Produce a snippet describing the fields in the subsection of the response payload
beneath the path `weather.temperature`. Uses the static `beneathPath` method on
`org.springframework.restdocs.payload.PayloadDocumentation`.

**2**

Document the `high` and `low` fields.

The result is a snippet that contains a table describing the `high` and `low` fields of `weather.temperature`.
To make the snippet’s name distinct, an identifier for the subsection is included.
By default, this identifier is `beneath-${path}`.
For example, the preceding code results in a snippet named `response-fields-beneath-weather.temperature.adoc`.

<a id="index--documenting-your-api-query-parameters"></a>
<a id="index--query-parameters"></a>

### [Query Parameters](#index--documenting-your-api-query-parameters)

You can document a request’s query parameters by using `queryParameters`.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/users?page=2&per_page=100")) (1)
	.andExpect(status().isOk())
	.andDo(document("users", queryParameters((2)
			parameterWithName("page").description("The page to retrieve"), (3)
			parameterWithName("per_page").description("Entries per page") (4)
	)));
```

**1**

Perform a `GET` request with two parameters, `page` and `per_page`, in the query string.
Query parameters should be included in the URL, as shown here, or specified using the request builder’s `queryParam` or `queryParams` method.
The `param` and `params` methods should be avoided as the source of the parameters is then ambiguous.

**2**

Configure Spring REST Docs to produce a snippet describing the request’s query parameters.
Uses the static `queryParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.

**3**

Document the `page` query parameter.
Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`.

**4**

Document the `per_page` query parameter.

WebTestClient

```java
this.webTestClient.get().uri("/users?page=2&per_page=100") (1)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("users", queryParameters((2)
			parameterWithName("page").description("The page to retrieve"), (3)
			parameterWithName("per_page").description("Entries per page") (4)
	)));
```

**1**

Perform a `GET` request with two parameters, `page` and `per_page`, in the query string.

**2**

Configure Spring REST Docs to produce a snippet describing the request’s query parameters.
Uses the static `queryParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.

**3**

Document the `page` parameter.
Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`.

**4**

Document the `per_page` parameter.

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("users", queryParameters((1)
			parameterWithName("page").description("The page to retrieve"), (2)
			parameterWithName("per_page").description("Entries per page")))) (3)
	.when()
	.get("/users?page=2&per_page=100") (4)
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST Docs to produce a snippet describing the request’s query parameters.
Uses the static `queryParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.

**2**

Document the `page` parameter.
Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`.

**3**

Document the `per_page` parameter.

**4**

Perform a `GET` request with two parameters, `page` and `per_page`, in the query string.

When documenting query parameters, the test fails if an undocumented query parameter is used in the request’s query string.
Similarly, the test also fails if a documented query parameter is not found in the request’s query string and the parameter has not been marked as optional.

If you do not want to document a query parameter, you can mark it as ignored.
This prevents it from appearing in the generated snippet while avoiding the failure described above.

You can also document query parameters in a relaxed mode where any undocumented parameters do not cause a test failure.
To do so, use the `relaxedQueryParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the query parameters.

<a id="index--documenting-your-api-form-parameters"></a>
<a id="index--form-parameters"></a>

### [Form Parameters](#index--documenting-your-api-form-parameters)

You can document a request’s form parameters by using `formParameters`.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(post("/users").param("username", "Tester")) (1)
	.andExpect(status().isCreated())
	.andDo(document("create-user", formParameters((2)
			parameterWithName("username").description("The user's username") (3)
	)));
```

| **1** | Perform a `POST` request with a single form parameter, `username`. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s form parameters. Uses the static `formParameters` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **3** | Document the `username` parameter. Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`. |

WebTestClient

```java
MultiValueMap<String, String> formData = new LinkedMultiValueMap<>();
formData.add("username", "Tester");
this.webTestClient.post().uri("/users").body(BodyInserters.fromFormData(formData)) (1)
		.exchange().expectStatus().isCreated().expectBody()
		.consumeWith(document("create-user", formParameters((2)
				parameterWithName("username").description("The user's username") (3)
		)));
```

| **1** | Perform a `POST` request with a single form parameter, `username`. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s form parameters. Uses the static `formParameters` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **3** | Document the `username` parameter. Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`. |

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("create-user", formParameters((1)
			parameterWithName("username").description("The user's username")))) (2)
	.formParam("username", "Tester")
	.when()
	.post("/users") (3)
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST Docs to produce a snippet describing the request’s form parameters.
Uses the static `formParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.

**2**

Document the `username` parameter.
Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`.

**3**

Perform a `POST` request with a single form parameter, `username`.

In all cases, the result is a snippet named `form-parameters.adoc` that contains a table describing the form parameters that are supported by the resource.

When documenting form parameters, the test fails if an undocumented form parameter is used in the request body.
Similarly, the test also fails if a documented form parameter is not found in the request body and the form parameter has not been marked as optional.

If you do not want to document a form parameter, you can mark it as ignored.
This prevents it from appearing in the generated snippet while avoiding the failure described above.

You can also document form parameters in a relaxed mode where any undocumented parameters do not cause a test failure.
To do so, use the `relaxedFormParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the form parameters.

<a id="index--documenting-your-api-path-parameters"></a>
<a id="index--path-parameters"></a>

### [Path Parameters](#index--documenting-your-api-path-parameters)

You can document a request’s path parameters by using `pathParameters`.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/locations/{latitude}/{longitude}", 51.5072, 0.1275)) (1)
	.andExpect(status().isOk())
	.andDo(document("locations", pathParameters((2)
			parameterWithName("latitude").description("The location's latitude"), (3)
			parameterWithName("longitude").description("The location's longitude") (4)
	)));
```

| **1** | Perform a `GET` request with two path parameters, `latitude` and `longitude`. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s path parameters. Uses the static `pathParameters` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **3** | Document the parameter named `latitude`. Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **4** | Document the parameter named `longitude`. |

WebTestClient

```java
this.webTestClient.get().uri("/locations/{latitude}/{longitude}", 51.5072, 0.1275) (1)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("locations",
		pathParameters((2)
			parameterWithName("latitude").description("The location's latitude"), (3)
			parameterWithName("longitude").description("The location's longitude")))); (4)
```

| **1** | Perform a `GET` request with two path parameters, `latitude` and `longitude`. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s path parameters. Uses the static `pathParameters` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **3** | Document the parameter named `latitude`. Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **4** | Document the parameter named `longitude`. |

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("locations", pathParameters((1)
			parameterWithName("latitude").description("The location's latitude"), (2)
			parameterWithName("longitude").description("The location's longitude")))) (3)
	.when()
	.get("/locations/{latitude}/{longitude}", 51.5072, 0.1275) (4)
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST Docs to produce a snippet describing the request’s path parameters.
Uses the static `pathParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.

**2**

Document the parameter named `latitude`.
Uses the static `parameterWithName` method on `org.springframework.restdocs.request.RequestDocumentation`.

**3**

Document the parameter named `longitude`.

**4**

Perform a `GET` request with two path parameters, `latitude` and `longitude`.

The result is a snippet named `path-parameters.adoc` that contains a table describing the path parameters that are supported by the resource.

> [!TIP]
> If you use MockMvc with Spring Framework 6.1 or earlier, to make the path parameters available for documentation, you must build the request by using one of the methods on `RestDocumentationRequestBuilders` rather than `MockMvcRequestBuilders`.

When documenting path parameters, the test fails if an undocumented path parameter is used in the request.
Similarly, the test also fails if a documented path parameter is not found in the request and the path parameter has not been marked as optional.

You can also document path parameters in a relaxed mode, where any undocumented parameters do not cause a test failure.
To do so, use the `relaxedPathParameters` method on `org.springframework.restdocs.request.RequestDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the path parameters.

If you do not want to document a path parameter, you can mark it as ignored.
Doing so prevents it from appearing in the generated snippet while avoiding the failure described earlier.

<a id="index--documenting-your-api-request-parts"></a>
<a id="index--request-parts"></a>

### [Request Parts](#index--documenting-your-api-request-parts)

You can use `requestParts` to document the parts of a multipart request.
The following example shows how to do so:

MockMvc

```java
this.mockMvc.perform(multipart("/upload").file("file", "example".getBytes())) (1)
	.andExpect(status().isOk())
	.andDo(document("upload", requestParts((2)
			partWithName("file").description("The file to upload")) (3)
	));
```

| **1** | Perform a `POST` request with a single part named `file`. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s parts. Uses the static `requestParts` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **3** | Document the part named `file`. Uses the static `partWithName` method on `org.springframework.restdocs.request.RequestDocumentation`. |

WebTestClient

```java
MultiValueMap<String, Object> multipartData = new LinkedMultiValueMap<>();
multipartData.add("file", "example".getBytes());
this.webTestClient.post().uri("/upload").body(BodyInserters.fromMultipartData(multipartData)) (1)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("upload", requestParts((2)
		partWithName("file").description("The file to upload")) (3)
));
```

| **1** | Perform a `POST` request with a single part named `file`. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s parts. Uses the static `requestParts` method on `org.springframework.restdocs.request.RequestDocumentation`. |
| **3** | Document the part named `file`. Uses the static `partWithName` method on `org.springframework.restdocs.request.RequestDocumentation`. |

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("users", requestParts((1)
			partWithName("file").description("The file to upload")))) (2)
	.multiPart("file", "example") (3)
	.when()
	.post("/upload") (4)
	.then()
	.statusCode(is(200));
```

**1**

Configure Spring REST Docs to produce a snippet describing the request’s parts.
Uses the static `requestParts` method on `org.springframework.restdocs.request.RequestDocumentation`.

**2**

Document the part named `file`. Uses the static `partWithName` method on `org.springframework.restdocs.request.RequestDocumentation`.

**3**

Configure the request with the part named `file`.

**4**

Perform the `POST` request to `/upload`.

The result is a snippet named `request-parts.adoc` that contains a table describing the request parts that are supported by the resource.

When documenting request parts, the test fails if an undocumented part is used in the request.
Similarly, the test also fails if a documented part is not found in the request and the part has not been marked as optional.

You can also document request parts in a relaxed mode where any undocumented parts do not cause a test failure.
To do so, use the `relaxedRequestParts` method on `org.springframework.restdocs.request.RequestDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the request parts.

If you do not want to document a request part, you can mark it as ignored.
This prevents it from appearing in the generated snippet while avoiding the failure described earlier.

<a id="index--documenting-your-api-request-parts-payloads"></a>
<a id="index--request-part-payloads"></a>

### [Request Part Payloads](#index--documenting-your-api-request-parts-payloads)

You can document the payload of a request part in much the same way as the [payload of a request](#index--documenting-your-api-request-response-payloads), with support for documenting a request part’s body and its fields.

<a id="index--documenting-your-api-request-parts-payloads-body"></a>
<a id="index--documenting-a-request-part-s-body"></a>

#### [Documenting a Request Part’s Body](#index--documenting-your-api-request-parts-payloads-body)

You can generate a snippet containing the body of a request part as follows:

MockMvc

```java
MockMultipartFile image = new MockMultipartFile("image", "image.png", "image/png", "<<png data>>".getBytes());
MockMultipartFile metadata = new MockMultipartFile("metadata", "", "application/json",
		"{ \"version\": \"1.0\"}".getBytes());

this.mockMvc.perform(multipart("/images").file(image).file(metadata).accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("image-upload", requestPartBody("metadata"))); (1)
```

**1**

Configure Spring REST docs to produce a snippet containing the body of the request part named `metadata`.
Uses the static `requestPartBody` method on `PayloadDocumentation`.

WebTestClient

```java
MultiValueMap<String, Object> multipartData = new LinkedMultiValueMap<>();
Resource imageResource = new ByteArrayResource("<<png data>>".getBytes()) {

	@Override
	public String getFilename() {
		return "image.png";
	}

};
multipartData.add("image", imageResource);
multipartData.add("metadata", Collections.singletonMap("version",  "1.0"));

this.webTestClient.post().uri("/images").body(BodyInserters.fromMultipartData(multipartData))
	.accept(MediaType.APPLICATION_JSON).exchange()
	.expectStatus().isOk().expectBody()
	.consumeWith(document("image-upload",
			requestPartBody("metadata"))); (1)
```

**1**

Configure Spring REST docs to produce a snippet containing the body of the request part named `metadata`.
Uses the static `requestPartBody` method on `PayloadDocumentation`.

REST Assured

```java
Map<String, String> metadata = new HashMap<>();
metadata.put("version", "1.0");
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("image-upload", requestPartBody("metadata"))) (1)
	.when()
	.multiPart("image", new File("image.png"), "image/png")
	.multiPart("metadata", metadata)
	.post("images")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST docs to produce a snippet containing the body of the request part named `metadata`.
Uses the static `requestPartBody` method on `PayloadDocumentation`.

The result is a snippet named `request-part-${part-name}-body.adoc` that contains the part’s body.
For example, documenting a part named `metadata` produces a snippet named `request-part-metadata-body.adoc`.

<a id="index--documenting-your-api-request-parts-payloads-fields"></a>
<a id="index--documenting-a-request-part-s-fields"></a>

#### [Documenting a Request Part’s Fields](#index--documenting-your-api-request-parts-payloads-fields)

You can document a request part’s fields in much the same way as the fields of a request or response, as follows:

MockMvc

```java
MockMultipartFile image = new MockMultipartFile("image", "image.png", "image/png", "<<png data>>".getBytes());
MockMultipartFile metadata = new MockMultipartFile("metadata", "", "application/json",
		"{ \"version\": \"1.0\"}".getBytes());

this.mockMvc.perform(multipart("/images").file(image).file(metadata).accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("image-upload", requestPartFields("metadata", (1)
			fieldWithPath("version").description("The version of the image")))); (2)
```

**1**

Configure Spring REST docs to produce a snippet describing the fields in the payload of the request part named `metadata`.
Uses the static `requestPartFields` method on `PayloadDocumentation`.

**2**

Expect a field with the path `version`.
Uses the static `fieldWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

WebTestClient

```java
MultiValueMap<String, Object> multipartData = new LinkedMultiValueMap<>();
Resource imageResource = new ByteArrayResource("<<png data>>".getBytes()) {

	@Override
	public String getFilename() {
		return "image.png";
	}

};
multipartData.add("image", imageResource);
multipartData.add("metadata", Collections.singletonMap("version",  "1.0"));
this.webTestClient.post().uri("/images").body(BodyInserters.fromMultipartData(multipartData))
	.accept(MediaType.APPLICATION_JSON).exchange()
	.expectStatus().isOk().expectBody()
	.consumeWith(document("image-upload",
		requestPartFields("metadata", (1)
			fieldWithPath("version").description("The version of the image")))); (2)
```

**1**

Configure Spring REST docs to produce a snippet describing the fields in the payload of the request part named `metadata`.
Uses the static `requestPartFields` method on `PayloadDocumentation`.

**2**

Expect a field with the path `version`.
Uses the static `fieldWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

REST Assured

```java
Map<String, String> metadata = new HashMap<>();
metadata.put("version", "1.0");
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("image-upload", requestPartFields("metadata", (1)
			fieldWithPath("version").description("The version of the image")))) (2)
	.when()
	.multiPart("image", new File("image.png"), "image/png")
	.multiPart("metadata", metadata)
	.post("images")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST docs to produce a snippet describing the fields in the payload of the request part named `metadata`.
Uses the static `requestPartFields` method on `PayloadDocumentation`.

**2**

Expect a field with the path `version`.
Uses the static `fieldWithPath` method on `org.springframework.restdocs.payload.PayloadDocumentation`.

The result is a snippet that contains a table describing the part’s fields.
This snippet is named `request-part-${part-name}-fields.adoc`.
For example, documenting a part named `metadata` produces a snippet named `request-part-metadata-fields.adoc`.

When documenting fields, the test fails if an undocumented field is found in the payload of the part.
Similarly, the test also fails if a documented field is not found in the payload of the part and the field has not been marked as optional.
For payloads with a hierarchical structure, documenting a field is sufficient for all of its descendants to also be treated as having been documented.

If you do not want to document a field, you can mark it as ignored.
Doing so prevents it from appearing in the generated snippet while avoiding the failure described above.

You can also document fields in a relaxed mode, where any undocumented fields do not cause a test failure.
To do so, use the `relaxedRequestPartFields` method on `org.springframework.restdocs.payload.PayloadDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the payload of the part.

For further information on describing fields, documenting payloads that use XML, and more, see the [section on documenting request and response payloads](#index--documenting-your-api-request-response-payloads).

<a id="index--documenting-your-api-http-headers"></a>
<a id="index--http-headers"></a>

### [HTTP Headers](#index--documenting-your-api-http-headers)

You can document the headers in a request or response by using `requestHeaders` and `responseHeaders`, respectively.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/people").header("Authorization", "Basic dXNlcjpzZWNyZXQ=")) (1)
	.andExpect(status().isOk())
	.andDo(document("headers", requestHeaders((2)
			headerWithName("Authorization").description("Basic auth credentials")), (3)
			responseHeaders((4)
					headerWithName("X-RateLimit-Limit")
						.description("The total number of requests permitted per period"),
					headerWithName("X-RateLimit-Remaining")
						.description("Remaining requests permitted in current period"),
					headerWithName("X-RateLimit-Reset")
						.description("Time at which the rate limit period will reset"))));
```

**1**

Perform a `GET` request with an `Authorization` header that uses basic authentication.

**2**

Configure Spring REST Docs to produce a snippet describing the request’s headers.
Uses the static `requestHeaders` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

**3**

Document the `Authorization` header.
Uses the static `headerWithName` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

**4**

Produce a snippet describing the response’s headers.
Uses the static `responseHeaders` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

WebTestClient

```java
this.webTestClient
	.get().uri("/people").header("Authorization", "Basic dXNlcjpzZWNyZXQ=") (1)
	.exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("headers",
		requestHeaders((2)
			headerWithName("Authorization").description("Basic auth credentials")), (3)
		responseHeaders((4)
			headerWithName("X-RateLimit-Limit")
				.description("The total number of requests permitted per period"),
			headerWithName("X-RateLimit-Remaining")
				.description("Remaining requests permitted in current period"),
			headerWithName("X-RateLimit-Reset")
				.description("Time at which the rate limit period will reset"))));
```

**1**

Perform a `GET` request with an `Authorization` header that uses basic authentication.

**2**

Configure Spring REST Docs to produce a snippet describing the request’s headers.
Uses the static `requestHeaders` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

**3**

Document the `Authorization` header.
Uses the static `headerWithName` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

**4**

Produce a snippet describing the response’s headers.
Uses the static `responseHeaders` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("headers", requestHeaders((1)
			headerWithName("Authorization").description("Basic auth credentials")), (2)
			responseHeaders((3)
					headerWithName("X-RateLimit-Limit")
						.description("The total number of requests permitted per period"),
					headerWithName("X-RateLimit-Remaining")
						.description("Remaining requests permitted in current period"),
					headerWithName("X-RateLimit-Reset")
						.description("Time at which the rate limit period will reset"))))
	.header("Authorization", "Basic dXNlcjpzZWNyZXQ=") (4)
	.when()
	.get("/people")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST Docs to produce a snippet describing the request’s headers.
Uses the static `requestHeaders` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

**2**

Document the `Authorization` header.
Uses the static `headerWithName` method on `org.springframework.restdocs.headers.HeaderDocumentation.

**3**

Produce a snippet describing the response’s headers.
Uses the static `responseHeaders` method on `org.springframework.restdocs.headers.HeaderDocumentation`.

**4**

Configure the request with an `Authorization` header that uses basic authentication.

The result is a snippet named `request-headers.adoc` and a snippet named `response-headers.adoc`.
Each contains a table describing the headers.

When documenting HTTP Headers, the test fails if a documented header is not found in the request or response.

<a id="index--documenting-your-api-http-cookies"></a>
<a id="index--http-cookies"></a>

### [HTTP Cookies](#index--documenting-your-api-http-cookies)

You can document the cookies in a request or response by using `requestCookies` and `responseCookies`, respectively.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/").cookie(new Cookie("JSESSIONID", "ACBCDFD0FF93D5BB"))) (1)
	.andExpect(status().isOk())
	.andDo(document("cookies", requestCookies((2)
			cookieWithName("JSESSIONID").description("Session token")), (3)
			responseCookies((4)
					cookieWithName("JSESSIONID").description("Updated session token"),
					cookieWithName("logged_in")
						.description("Set to true if the user is currently logged in"))));
```

| **1** | Make a GET request with a `JSESSIONID` cookie. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s cookies. Uses the static `requestCookies` method on `org.springframework.restdocs.cookies.CookieDocumentation`. |
| **3** | Document the `JSESSIONID` cookie. Uses the static `cookieWithName` method on `org.springframework.restdocs.cookies.CookieDocumentation`. |
| **4** | Produce a snippet describing the response’s cookies. Uses the static `responseCookies` method on `org.springframework.restdocs.cookies.CookieDocumentation`. |

WebTestClient

```java
this.webTestClient.get()
	.uri("/people")
	.cookie("JSESSIONID", "ACBCDFD0FF93D5BB=") (1)
	.exchange()
	.expectStatus()
	.isOk()
	.expectBody()
	.consumeWith(document("cookies", requestCookies((2)
			cookieWithName("JSESSIONID").description("Session token")), (3)
			responseCookies((4)
					cookieWithName("JSESSIONID").description("Updated session token"),
					cookieWithName("logged_in").description("User is logged in"))));
```

| **1** | Make a GET request with a `JSESSIONID` cookie. |
| --- | --- |
| **2** | Configure Spring REST Docs to produce a snippet describing the request’s cookies. Uses the static `requestCookies` method on `org.springframework.restdocs.cookies.CookieDocumentation`. |
| **3** | Document the `JSESSIONID` cookie. Uses the static `cookieWithName` method on `org.springframework.restdocs.cookies.CookieDocumentation`. |
| **4** | Produce a snippet describing the response’s cookies. Uses the static `responseCookies` method on `org.springframework.restdocs.cookies.CookieDocumentation`. |

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("cookies", requestCookies((1)
			cookieWithName("JSESSIONID").description("Saved session token")), (2)
			responseCookies((3)
					cookieWithName("logged_in").description("If user is logged in"),
					cookieWithName("JSESSIONID").description("Updated session token"))))
	.cookie("JSESSIONID", "ACBCDFD0FF93D5BB") (4)
	.when()
	.get("/people")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Configure Spring REST Docs to produce a snippet describing the request’s cookies.
Uses the static `requestCookies` method on `org.springframework.restdocs.cookies.CookieDocumentation`.

**2**

Document the `JSESSIONID` cookie.
Uses the static `cookieWithName` method on `org.springframework.restdocs.cookies.CookieDocumentation`.

**3**

Produce a snippet describing the response’s cookies.
Uses the static `responseCookies` method on `org.springframework.restdocs.cookies.CookieDocumentation`.

**4**

Send a `JSESSIONID` cookie with the request.

The result is a snippet named `request-cookies.adoc` and a snippet named `response-cookies.adoc`.
Each contains a table describing the cookies.

When documenting HTTP cookies, the test fails if an undocumented cookie is found in the request or response.
Similarly, the test also fails if a documented cookie is not found and the cookie has not been marked as optional.
You can also document cookies in a relaxed mode, where any undocumented cookies do not cause a test failure.
To do so, use the `relaxedRequestCookies` and `relaxedResponseCookies` methods on `org.springframework.restdocs.cookies.CookieDocumentation`.
This can be useful when documenting a particular scenario where you only want to focus on a subset of the cookies.
If you do not want to document a cookie, you can mark it as ignored.
Doing so prevents it from appearing in the generated snippet while avoiding the failure described earlier.

<a id="index--documenting-your-api-reusing-snippets"></a>
<a id="index--reusing-snippets"></a>

### [Reusing Snippets](#index--documenting-your-api-reusing-snippets)

It is common for an API that is being documented to have some features that are common across several of its resources.
To avoid repetition when documenting such resources, you can reuse a `Snippet` configured with the common elements.

First, create the `Snippet` that describes the common elements.
The following example shows how to do so:

```java
protected final LinksSnippet pagingLinks = links(
		linkWithRel("first").optional().description("The first page of results"),
		linkWithRel("last").optional().description("The last page of results"),
		linkWithRel("next").optional().description("The next page of results"),
		linkWithRel("prev").optional().description("The previous page of results"));
```

Second, use this snippet and add further descriptors that are resource-specific.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/").accept(MediaType.APPLICATION_JSON))
	.andExpect(status().isOk())
	.andDo(document("example", this.pagingLinks.and((1)
			linkWithRel("alpha").description("Link to the alpha resource"),
			linkWithRel("bravo").description("Link to the bravo resource"))));
```

**1**

Reuse the `pagingLinks` `Snippet`, calling `and` to add descriptors that are specific to the resource that is being documented.

WebTestClient

```java
this.webTestClient.get().uri("/").accept(MediaType.APPLICATION_JSON).exchange()
	.expectStatus().isOk().expectBody()
	.consumeWith(document("example", this.pagingLinks.and((1)
		linkWithRel("alpha").description("Link to the alpha resource"),
		linkWithRel("bravo").description("Link to the bravo resource"))));
```

**1**

Reuse the `pagingLinks` `Snippet`, calling `and` to add descriptors that are specific to the resource that is being documented.

REST Assured

```java
RestAssured.given(this.spec)
	.accept("application/json")
	.filter(document("example", this.pagingLinks.and((1)
			linkWithRel("alpha").description("Link to the alpha resource"),
			linkWithRel("bravo").description("Link to the bravo resource"))))
	.get("/")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Reuse the `pagingLinks` `Snippet`, calling `and` to add descriptors that are specific to the resource that is being documented.

The result of the example is that links with `rel` values of `first`, `last`, `next`, `previous`, `alpha`, and `bravo` are all documented.

<a id="index--documenting-your-api-constraints"></a>
<a id="index--documenting-constraints"></a>

### [Documenting Constraints](#index--documenting-your-api-constraints)

Spring REST Docs provides a number of classes that can help you to document constraints.
You can use an instance of `ConstraintDescriptions` to access descriptions of a class’s constraints.
The following example shows how to do so:

```java
public void example() {
	ConstraintDescriptions userConstraints = new ConstraintDescriptions(UserInput.class); (1)
	List<String> descriptions = userConstraints.descriptionsForProperty("name"); (2)
}

static class UserInput {

	@NotNull
	@Size(min = 1)
	String name;

	@NotNull
	@Size(min = 8)
	String password;

}
```

**1**

Create an instance of `ConstraintDescriptions` for the `UserInput` class.

**2**

Get the descriptions of the `name` property’s constraints.
This list contains two descriptions: one for the `NotNull` constraint and one for the `Size` constraint.

The [`ApiDocumentation`](https://github.com/spring-projects/spring-restdocs-samples/tree/main/restful-notes-spring-hateoas/src/test/java/com/example/notes/ApiDocumentation.java) class in the Spring HATEOAS sample shows this functionality in action.

<a id="index--documenting-your-api-constraints-finding"></a>
<a id="index--finding-constraints"></a>

#### [Finding Constraints](#index--documenting-your-api-constraints-finding)

By default, constraints are found by using a Bean Validation `Validator`.
Currently, only property constraints are supported.
You can customize the `Validator` that is used by creating `ConstraintDescriptions` with a custom `ValidatorConstraintResolver` instance.
To take complete control of constraint resolution, you can use your own implementation of `ConstraintResolver`.

<a id="index--documenting-your-api-constraints-describing"></a>
<a id="index--describing-constraints"></a>

#### [Describing Constraints](#index--documenting-your-api-constraints-describing)

Default descriptions are provided for all of Bean Validation 3.0’s constraints:

- `AssertFalse`
- `AssertTrue`
- `DecimalMax`
- `DecimalMin`
- `Digits`
- `Email`
- `Future`
- `FutureOrPresent`
- `Max`
- `Min`
- `Negative`
- `NegativeOrZero`
- `NotBlank`
- `NotEmpty`
- `NotNull`
- `Null`
- `Past`
- `PastOrPresent`
- `Pattern`
- `Positive`
- `PositiveOrZero`
- `Size`

Default descriptions are also provided for the following constraints from Hibernate
Validator:

- `CodePointLength`
- `CreditCardNumber`
- `Currency`
- `EAN`
- `Email`
- `Length`
- `LuhnCheck`
- `Mod10Check`
- `Mod11Check`
- `NotBlank`
- `NotEmpty`
- `Currency`
- `Range`
- `SafeHtml`
- `URL`

To override the default descriptions or to provide a new description, you can create a resource bundle with a base name of `org.springframework.restdocs.constraints.ConstraintDescriptions`.
The Spring HATEOAS-based sample contains [an example of such a resource bundle](https://github.com/spring-projects/spring-restdocs-samples/tree/main/restful-notes-spring-hateoas/src/test/resources/org/springframework/restdocs/constraints/ConstraintDescriptions.properties).

Each key in the resource bundle is the fully-qualified name of a constraint plus a `.description`.
For example, the key for the standard `@NotNull` constraint is `jakarta.validation.constraints.NotNull.description`.

You can use a property placeholder referring to a constraint’s attributes in its description.
For example, the default description of the `@Min` constraint, `Must be at least ${value}`, refers to the constraint’s `value` attribute.

To take more control of constraint description resolution, you can create `ConstraintDescriptions` with a custom `ResourceBundleConstraintDescriptionResolver`.
To take complete control, you can create `ConstraintDescriptions` with a custom `ConstraintDescriptionResolver` implementation.

<a id="index--_using_constraint_descriptions_in_generated_snippets"></a>
<a id="index--using-constraint-descriptions-in-generated-snippets"></a>

#### [Using Constraint Descriptions in Generated Snippets](#index--_using_constraint_descriptions_in_generated_snippets)

Once you have a constraint’s descriptions, you are free to use them however you like in the generated snippets.
For example, you may want to include the constraint descriptions as part of a field’s description.
Alternatively, you could include the constraints as [extra information](#index--documenting-your-api-customizing-including-extra-information) in the request fields snippet.
The [`ApiDocumentation`](https://github.com/spring-projects/spring-restdocs-samples/tree/main/restful-notes-spring-hateoas/src/test/java/com/example/notes/ApiDocumentation.java) class in the Spring HATEOAS-based sample illustrates the latter approach.

<a id="index--documenting-your-api-default-snippets"></a>
<a id="index--default-snippets"></a>

### [Default Snippets](#index--documenting-your-api-default-snippets)

A number of snippets are produced automatically when you document a request and response.

| Snippet | Description |
| --- | --- |
| `curl-request.adoc` | Contains the [`curl`](https://curl.haxx.se) command that is equivalent to the `MockMvc` call that is being documented. |
| `httpie-request.adoc` | Contains the [`HTTPie`](https://httpie.org) command that is equivalent to the `MockMvc` call that is being documented. |
| `http-request.adoc` | Contains the HTTP request that is equivalent to the `MockMvc` call that is being documented. |
| `http-response.adoc` | Contains the HTTP response that was returned. |
| `request-body.adoc` | Contains the body of the request that was sent. |
| `response-body.adoc` | Contains the body of the response that was returned. |

You can configure which snippets are produced by default.
See the [configuration section](#index--configuration) for more information.

<a id="index--documentating-your-api-parameterized-output-directories"></a>
<a id="index--using-parameterized-output-directories"></a>

### [Using Parameterized Output Directories](#index--documentating-your-api-parameterized-output-directories)

You can parameterize the output directory used by `document`.
The following parameters are supported:

| Parameter | Description |
| --- | --- |
| {methodName} | The unmodified name of the test method. |
| {method-name} | The name of the test method, formatted using kebab-case. |
| {method\_name} | The name of the test method, formatted using snake\_case. |
| {ClassName} | The unmodified simple name of the test class. |
| {class-name} | The simple name of the test class, formatted using kebab-case. |
| {class\_name} | The simple name of the test class, formatted using snake\_case. |
| {step} | The count of calls made to the service in the current test. |

For example, `document("{class-name}/{method-name}")` in a test method named `creatingANote` on the test class `GettingStartedDocumentation` writes snippets into a directory named `getting-started-documentation/creating-a-note`.

A parameterized output directory is particularly useful in combination with a `@Before` method.
It lets documentation be configured once in a setup method and then reused in every test in the class.
The following examples show how to do so:

MockMvc

```java
@Before
public void setUp() {
	this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
		.apply(documentationConfiguration(this.restDocumentation))
		.alwaysDo(document("{method-name}/{step}/"))
		.build();
}
```

REST Assured

```java
@Before
public void setUp() {
	this.spec = new RequestSpecBuilder().addFilter(documentationConfiguration(this.restDocumentation))
		.addFilter(document("{method-name}/{step}"))
		.build();
}
```

WebTestClient

```java
@Before
public void setUp() {
	this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
		.configureClient()
		.filter(documentationConfiguration(this.restDocumentation))
		.entityExchangeResultConsumer(document("{method-name}/{step}"))
		.build();
}
```

With this configuration in place, every call to the service you are testing produces the [default snippets](#index--documenting-your-api-default-snippets) without any further configuration.
Take a look at the `GettingStartedDocumentation` classes in each of the sample applications to see this functionality in action.

<a id="index--documenting-your-api-customizing"></a>
<a id="index--customizing-the-output"></a>

### [Customizing the Output](#index--documenting-your-api-customizing)

This section describes how to customize the output of Spring REST Docs.

<a id="index--documenting-your-api-customizing-snippets"></a>
<a id="index--customizing-the-generated-snippets"></a>

#### [Customizing the Generated Snippets](#index--documenting-your-api-customizing-snippets)

Spring REST Docs uses [Mustache](https://mustache.github.io) templates to produce the generated snippets.
[Default templates](https://github.com/spring-projects/spring-restdocs/tree/v3.0.6/spring-restdocs-core/src/main/resources/org/springframework/restdocs/templates) are provided for each of the snippets that Spring REST Docs can produce.
To customize a snippet’s content, you can provide your own template.

Templates are loaded from the classpath from an `org.springframework.restdocs.templates` subpackage.
The name of the subpackage is determined by the ID of the template format that is in use.
The default template format, Asciidoctor, has an ID of `asciidoctor`, so snippets are loaded from `org.springframework.restdocs.templates.asciidoctor`.
Each template is named after the snippet that it produces.
For example, to override the template for the `curl-request.adoc` snippet, create a template named `curl-request.snippet` in `src/test/resources/org/springframework/restdocs/templates/asciidoctor`.

<a id="index--documenting-your-api-customizing-including-extra-information"></a>
<a id="index--including-extra-information"></a>

#### [Including Extra Information](#index--documenting-your-api-customizing-including-extra-information)

There are two ways to provide extra information for inclusion in a generated snippet:

- Use the `attributes` method on a descriptor to add one or more attributes to it.
- Pass in some attributes when calling `curlRequest`, `httpRequest`, `httpResponse`, and so on.
  Such attributes are associated with the snippet as a whole.

Any additional attributes are made available during the template rendering process.
Coupled with a custom snippet template, this makes it possible to include extra information in a generated snippet.

A concrete example is the addition of a constraints column and a title when documenting request fields.
The first step is to provide a `constraints` attribute for each field that you document and to provide a `title` attribute.
The following examples show how to do so:

MockMvc

```java
.andDo(document("create-user", requestFields(attributes(key("title").value("Fields for user creation")), (1)
		fieldWithPath("name").description("The user's name")
			.attributes(key("constraints").value("Must not be null. Must not be empty")), (2)
		fieldWithPath("email").description("The user's email address")
			.attributes(key("constraints").value("Must be a valid email address"))))); (3)
```

| **1** | Configure the `title` attribute for the request fields snippet. |
| --- | --- |
| **2** | Set the `constraints` attribute for the `name` field. |
| **3** | Set the `constraints` attribute for the `email` field. |

WebTestClient

```java
.consumeWith(document("create-user",
	requestFields(
		attributes(key("title").value("Fields for user creation")), (1)
		fieldWithPath("name")
			.description("The user's name")
			.attributes(key("constraints").value("Must not be null. Must not be empty")), (2)
		fieldWithPath("email")
			.description("The user's email address")
			.attributes(key("constraints").value("Must be a valid email address"))))); (3)
```

| **1** | Configure the `title` attribute for the request fields snippet. |
| --- | --- |
| **2** | Set the `constraints` attribute for the `name` field. |
| **3** | Set the `constraints` attribute for the `email` field. |

REST Assured

```java
.filter(document("create-user", requestFields(attributes(key("title").value("Fields for user creation")), (1)
		fieldWithPath("name").description("The user's name")
			.attributes(key("constraints").value("Must not be null. Must not be empty")), (2)
		fieldWithPath("email").description("The user's email address")
			.attributes(key("constraints").value("Must be a valid email address"))))) (3)
```

| **1** | Configure the `title` attribute for the request fields snippet. |
| --- | --- |
| **2** | Set the `constraints` attribute for the `name` field. |
| **3** | Set the `constraints` attribute for the `email` field. |

The second step is to provide a custom template named `request-fields.snippet` that includes the information about the fields' constraints in the generated snippet’s table and adds a title.

```
.{{title}} (1)
|===
|Path|Type|Description|Constraints (2)

{{#fields}}
|{{path}}
|{{type}}
|{{description}}
|{{constraints}} (3)

{{/fields}}
|===
```

| **1** | Add a title to the table. |
| --- | --- |
| **2** | Add a new column named "Constraints". |
| **3** | Include the descriptors' `constraints` attribute in each row of the table. |

<a id="index--customizing-requests-and-responses"></a>

## [Customizing requests and responses](#index--customizing-requests-and-responses)

There may be situations where you do not want to document a request exactly as it was sent or a response exactly as it was received.
Spring REST Docs provides a number of preprocessors that can be used to modify a request or response before it is documented.

Preprocessing is configured by calling `document` with an `OperationRequestPreprocessor` or an `OperationResponsePreprocessor`.
You can obtain instances by using the static `preprocessRequest` and `preprocessResponse` methods on `Preprocessors`.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/"))
	.andExpect(status().isOk())
	.andDo(document("index", preprocessRequest(modifyHeaders().remove("Foo")), (1)
			preprocessResponse(prettyPrint()))); (2)
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

WebTestClient

```java
this.webTestClient.get().uri("/").exchange().expectStatus().isOk().expectBody()
	.consumeWith(document("index",
		preprocessRequest(modifyHeaders().remove("Foo")), (1)
		preprocessResponse(prettyPrint()))); (2)
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("index", preprocessRequest(modifyHeaders().remove("Foo")), (1)
			preprocessResponse(prettyPrint()))) (2)
	.when()
	.get("/")
	.then()
	.assertThat()
	.statusCode(is(200));
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

Alternatively, you may want to apply the same preprocessors to every test.
You can do so by using the `RestDocumentationConfigurer` API in your `@Before` method to configure the preprocessors.
For example, to remove the `Foo` header from all requests and pretty print all responses, you could do one of the following (depending on your testing environment):

MockMvc

```java
private MockMvc mockMvc;

@Before
public void setup() {
	this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
		.apply(documentationConfiguration(this.restDocumentation).operationPreprocessors()
			.withRequestDefaults(modifyHeaders().remove("Foo")) (1)
			.withResponseDefaults(prettyPrint())) (2)
		.build();
}
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

WebTestClient

```java
private WebTestClient webTestClient;

@Before
public void setup() {
	this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
		.configureClient()
		.filter(documentationConfiguration(this.restDocumentation)
			.operationPreprocessors()
				.withRequestDefaults(modifyHeaders().remove("Foo")) (1)
				.withResponseDefaults(prettyPrint())) (2)
		.build();
}
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

REST Assured

```java
private RequestSpecification spec;

@Before
public void setup() {
	this.spec = new RequestSpecBuilder()
		.addFilter(documentationConfiguration(this.restDocumentation).operationPreprocessors()
			.withRequestDefaults(modifyHeaders().remove("Foo")) (1)
			.withResponseDefaults(prettyPrint())) (2)
		.build();
}
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

Then, in each test, you can perform any configuration specific to that test.
The following examples show how to do so:

MockMvc

```java
this.mockMvc.perform(get("/"))
	.andExpect(status().isOk())
	.andDo(document("index", links(linkWithRel("self").description("Canonical self link"))));
```

WebTestClient

```java
this.webTestClient.get().uri("/").exchange().expectStatus().isOk()
	.expectBody().consumeWith(document("index",
		links(linkWithRel("self").description("Canonical self link"))));
```

REST Assured

```java
RestAssured.given(this.spec)
	.filter(document("index", links(linkWithRel("self").description("Canonical self link"))))
	.when()
	.get("/")
	.then()
	.assertThat()
	.statusCode(is(200));
```

Various built-in preprocessors, including those illustrated above, are available through the static methods on `Preprocessors`.
See [below](#index--customizing-requests-and-responses-preprocessors) for further details.

<a id="index--customizing-requests-and-responses-preprocessors"></a>
<a id="index--preprocessors"></a>

### [Preprocessors](#index--customizing-requests-and-responses-preprocessors)

<a id="index--customizing-requests-and-responses-preprocessors-pretty-print"></a>
<a id="index--pretty-printing"></a>

#### [Pretty Printing](#index--customizing-requests-and-responses-preprocessors-pretty-print)

`prettyPrint` on `Preprocessors` formats the content of the request or response to make it easier to read.

<a id="index--customizing-requests-and-responses-preprocessors-mask-links"></a>
<a id="index--masking-links"></a>

#### [Masking Links](#index--customizing-requests-and-responses-preprocessors-mask-links)

If you are documenting a hypermedia-based API, you may want to encourage clients to navigate the API by using links rather than through the use of hard coded URIs.
One way to do so is to limit the use of URIs in the documentation.
`maskLinks` on `Preprocessors` replaces the `href` of any links in the response with `…`.
You can also specify a different replacement if you wish.

<a id="index--customizing-requests-and-responses-preprocessors-modify-headers"></a>
<a id="index--modifying-headers"></a>

#### [Modifying Headers](#index--customizing-requests-and-responses-preprocessors-modify-headers)

You can use `modifyHeaders` on `Preprocessors` to add, set, and remove request or response headers.

<a id="index--customizing-requests-and-responses-preprocessors-replace-patterns"></a>
<a id="index--replacing-patterns"></a>

#### [Replacing Patterns](#index--customizing-requests-and-responses-preprocessors-replace-patterns)

`replacePattern` on `Preprocessors` provides a general purpose mechanism for replacing content in a request or response.
Any occurrences that match a regular expression are replaced.

<a id="index--customizing-requests-and-responses-preprocessors-modify-uris"></a>
<a id="index--modifying-uris"></a>

#### [Modifying URIs](#index--customizing-requests-and-responses-preprocessors-modify-uris)

> [!TIP]
> If you use MockMvc or a WebTestClient that is not bound to a server, you should customize URIs by [changing the configuration](#index--configuration-uris).

You can use `modifyUris` on `Preprocessors` to modify any URIs in a request or a response.
When using REST Assured or WebTestClient bound to a server, this lets you customize the URIs that appear in the documentation while testing a local instance of the service.

<a id="index--customizing-requests-and-responses-preprocessors-writing-your-own"></a>
<a id="index--writing-your-own-preprocessor"></a>

#### [Writing Your Own Preprocessor](#index--customizing-requests-and-responses-preprocessors-writing-your-own)

If one of the built-in preprocessors does not meet your needs, you can write your own by implementing the `OperationPreprocessor` interface.
You can then use your custom preprocessor in exactly the same way as any of the built-in preprocessors.

If you want to modify only the content (body) of a request or response, consider implementing the `ContentModifier` interface and using it with the built-in `ContentModifyingOperationPreprocessor`.

<a id="index--configuration"></a>

## [Configuration](#index--configuration)

This section covers how to configure Spring REST Docs.

<a id="index--configuration-uris"></a>
<a id="index--documented-uris"></a>

### [Documented URIs](#index--configuration-uris)

This section covers configuring documented URIs.

<a id="index--configuration-uris-mockmvc"></a>
<a id="index--mockmvc-uri-customization"></a>

#### [MockMvc URI Customization](#index--configuration-uris-mockmvc)

When using MockMvc, the default configuration for URIs documented by Spring REST Docs is as follows:

| Setting | Default |
| --- | --- |
| Scheme | `http` |
| Host | `localhost` |
| Port | `8080` |

This configuration is applied by `MockMvcRestDocumentationConfigurer`.
You can use its API to change one or more of the defaults to suit your needs.
The following example shows how to do so:

```java
this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
	.apply(documentationConfiguration(this.restDocumentation).uris()
		.withScheme("https")
		.withHost("example.com")
		.withPort(443))
	.build();
```

> [!NOTE]
> If the port is set to the default for the configured scheme (port 80 for HTTP or port 443 for HTTPS), it is omitted from any URIs in the generated snippets.

> [!TIP]
> To configure a request’s context path, use the `contextPath` method on `MockHttpServletRequestBuilder`.

<a id="index--configuration-uris-rest-assured"></a>
<a id="index--rest-assured-uri-customization"></a>

#### [REST Assured URI Customization](#index--configuration-uris-rest-assured)

REST Assured tests a service by making actual HTTP requests. As a result, URIs must be
customized once the operation on the service has been performed but before it is
documented. A
[REST-Assured-specific
preprocessor](#index--customizing-requests-and-responses-preprocessors-modify-uris) is provided for this purpose.

<a id="index--configuration-uris-webtestclient"></a>
<a id="index--webtestclient-uri-customization"></a>

#### [WebTestClient URI Customization](#index--configuration-uris-webtestclient)

When using WebTestClient, the default base for URIs documented by Spring REST Docs is `http://localhost:8080`.
You can customize this base by using the  [`baseUrl(String)` method on `WebTestClient.Builder`](https://docs.spring.io/spring-framework/docs/6.2.19/javadoc-api/org/springframework/test/web/reactive/server/WebTestClient.Builder.html#baseUrl-java.lang.String-).
The following example shows how to do so:

```java
@Before
public void setUp() {
	this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
		.configureClient()
		.baseUrl("https://api.example.com") (1)
		.filter(documentationConfiguration(this.restDocumentation))
		.build();
}
```

**1**

Configure the base of documented URIs to be `https://api.example.com`.

<a id="index--configuration-snippet-encoding"></a>
<a id="index--snippet-encoding"></a>

### [Snippet Encoding](#index--configuration-snippet-encoding)

The default snippet encoding is `UTF-8`.
You can change the default snippet encoding by using the `RestDocumentationConfigurer` API.
For example, the following examples use `ISO-8859-1`:

MockMvc

```java
this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
	.apply(documentationConfiguration(this.restDocumentation).snippets().withEncoding("ISO-8859-1"))
	.build();
```

WebTestClient

```java
this.webTestClient = WebTestClient.bindToApplicationContext(this.context).configureClient()
	.filter(documentationConfiguration(this.restDocumentation)
		.snippets().withEncoding("ISO-8859-1"))
	.build();
```

REST Assured

```java
this.spec = new RequestSpecBuilder()
	.addFilter(documentationConfiguration(this.restDocumentation).snippets().withEncoding("ISO-8859-1"))
	.build();
```

> [!TIP]
> When Spring REST Docs converts the content of a request or a response to a `String`, the `charset` specified in the `Content-Type` header is used if it is available.
> In its absence, the JVM’s default `Charset` is used.
> You can configure the JVM’s default `Charset` by using the `file.encoding` system property.

<a id="index--configuration-snippet-template-format"></a>
<a id="index--snippet-template-format"></a>

### [Snippet Template Format](#index--configuration-snippet-template-format)

The default snippet template format is Asciidoctor.
Markdown is also supported out of the box.
You can change the default format by using the `RestDocumentationConfigurer` API.
The following examples show how to do so:

MockMvc

```java
this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
	.apply(documentationConfiguration(this.restDocumentation).snippets()
		.withTemplateFormat(TemplateFormats.markdown()))
	.build();
```

WebTestClient

```java
this.webTestClient = WebTestClient.bindToApplicationContext(this.context).configureClient()
	.filter(documentationConfiguration(this.restDocumentation)
		.snippets().withTemplateFormat(TemplateFormats.markdown()))
	.build();
```

REST Assured

```java
this.spec = new RequestSpecBuilder()
	.addFilter(documentationConfiguration(this.restDocumentation).snippets()
		.withTemplateFormat(TemplateFormats.markdown()))
	.build();
```

<a id="index--configuration-default-snippets"></a>
<a id="index--default-snippets-2"></a>

### [Default Snippets](#index--configuration-default-snippets)

Six snippets are produced by default:

- `curl-request`
- `http-request`
- `http-response`
- `httpie-request`
- `request-body`
- `response-body`

You can change the default snippet configuration during setup by using the `RestDocumentationConfigurer` API.
The following examples produce only the `curl-request` snippet by default:

MockMvc

```java
this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
	.apply(documentationConfiguration(this.restDocumentation).snippets().withDefaults(curlRequest()))
	.build();
```

WebTestClient

```java
this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
	.configureClient().filter(
		documentationConfiguration(this.restDocumentation)
			.snippets().withDefaults(curlRequest()))
	.build();
```

REST Assured

```java
this.spec = new RequestSpecBuilder()
	.addFilter(documentationConfiguration(this.restDocumentation).snippets().withDefaults(curlRequest()))
	.build();
```

<a id="index--configuration-default-preprocessors"></a>
<a id="index--default-operation-preprocessors"></a>

### [Default Operation Preprocessors](#index--configuration-default-preprocessors)

You can configure default request and response preprocessors during setup by using the `RestDocumentationConfigurer` API.
The following examples remove the `Foo` headers from all requests and pretty print all responses:

MockMvc

```java
this.mockMvc = MockMvcBuilders.webAppContextSetup(this.context)
	.apply(documentationConfiguration(this.restDocumentation).operationPreprocessors()
		.withRequestDefaults(modifyHeaders().remove("Foo")) (1)
		.withResponseDefaults(prettyPrint())) (2)
	.build();
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

WebTestClient

```java
this.webTestClient = WebTestClient.bindToApplicationContext(this.context)
	.configureClient()
	.filter(documentationConfiguration(this.restDocumentation)
		.operationPreprocessors()
			.withRequestDefaults(modifyHeaders().remove("Foo")) (1)
			.withResponseDefaults(prettyPrint())) (2)
	.build();
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

REST Assured

```java
this.spec = new RequestSpecBuilder()
	.addFilter(documentationConfiguration(this.restDocumentation).operationPreprocessors()
		.withRequestDefaults(modifyHeaders().remove("Foo")) (1)
		.withResponseDefaults(prettyPrint())) (2)
	.build();
```

**1**

Apply a request preprocessor that removes the header named `Foo`.

**2**

Apply a response preprocessor that pretty prints its content.

<a id="index--working-with-asciidoctor"></a>

## [Working with Asciidoctor](#index--working-with-asciidoctor)

This section describes the aspects of working with Asciidoctor that are particularly relevant to Spring REST Docs.

> [!NOTE]
> Asciidoc is the document format.
> Asciidoctor is the tool that produces content (usually as HTML) from Asciidoc files (which end with `.adoc`).

<a id="index--working-with-asciidoctor-resources"></a>
<a id="index--resources"></a>

### [Resources](#index--working-with-asciidoctor-resources)

- [Syntax quick reference](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference)
- [User manual](https://asciidoctor.org/docs/user-manual)

<a id="index--working-with-asciidoctor-including-snippets"></a>
<a id="index--including-snippets"></a>

### [Including Snippets](#index--working-with-asciidoctor-including-snippets)

This section covers how to include Asciidoc snippets.

<a id="index--working-with-asciidoctor-including-snippets-operation"></a>
<a id="index--including-multiple-snippets-for-an-operation"></a>

#### [Including Multiple Snippets for an Operation](#index--working-with-asciidoctor-including-snippets-operation)

You can use a macro named `operation` to import all or some of the snippets that have been generated for a specific operation.
It is made available by including `spring-restdocs-asciidoctor` in your project’s [build configuration](#index--getting-started-build-configuration).

The target of the macro is the name of the operation.
In its simplest form, you can use the macro to include all of the snippets for an operation, as shown in the following example:

```
operation::index[]
```

The operation macro also supports a `snippets` attribute.
You can use it to select the snippets that should be included.
The attribute’s value is a comma-separated list.
Each entry in the list should be the name of a snippet file (minus the `.adoc` suffix) to include.
For example, only the curl, HTTP request, and HTTP response snippets can be included, as shown in the following example:

```
operation::index[snippets='curl-request,http-request,http-response']
```

The preceding example is the equivalent of the following:

```adoc
[[example_curl_request]]
== Curl request

include::{snippets}/index/curl-request.adoc[]

[[example_http_request]]
== HTTP request

include::{snippets}/index/http-request.adoc[]

[[example_http_response]]
== HTTP response

include::{snippets}/index/http-response.adoc[]
```

<a id="index--working-with-asciidoctor-including-snippets-operation-titles"></a>
<a id="index--section-titles"></a>

##### [Section Titles](#index--working-with-asciidoctor-including-snippets-operation-titles)

For each snippet that is included by using the `operation` macro, a section with a title is created.
Default titles are provided for the following built-in snippets:

| Snippet | Title |
| --- | --- |
| `curl-request` | Curl Request |
| `http-request` | HTTP request |
| `http-response` | HTTP response |
| `httpie-request` | HTTPie request |
| `links` | Links |
| `request-body` | Request body |
| `request-fields` | Request fields |
| `response-body` | Response body |
| `response-fields` | Response fields |

For snippets not listed in the preceding table, a default title is generated by replacing `-` characters with spaces and capitalizing the first letter.
For example, the title for a snippet named `custom-snippet` `will be` “Custom snippet”.

You can customize the default titles by using document attributes.
The name of the attribute should be `operation-{snippet}-title`.
For example, to customize the title of the `curl-request` snippet to be "Example request", you can use the following attribute:

```
:operation-curl-request-title: Example request
```

<a id="index--working-with-asciidoctor-including-snippets-individual"></a>
<a id="index--including-individual-snippets"></a>

#### [Including Individual Snippets](#index--working-with-asciidoctor-including-snippets-individual)

The [include macro](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#include-files) is used to include individual snippets in your documentation.
You can use the `snippets` attribute (which is automatically set by `spring-restdocs-asciidoctor` configured in the [build configuration](#index--getting-started-build-configuration)) to reference the snippets output directory.
The following example shows how to do so:

```
include::{snippets}/index/curl-request.adoc[]
```

<a id="index--working-with-asciidoctor-customizing-tables"></a>
<a id="index--customizing-tables"></a>

### [Customizing Tables](#index--working-with-asciidoctor-customizing-tables)

Many of the snippets contain a table in its default configuration.
The appearance of the table can be customized, either by providing some additional configuration when the snippet is included or by using a custom snippet template.

<a id="index--working-with-asciidoctor-customizing-tables-formatting-columns"></a>
<a id="index--formatting-columns"></a>

#### [Formatting Columns](#index--working-with-asciidoctor-customizing-tables-formatting-columns)

Asciidoctor has rich support for [formatting a table’s columns](https://asciidoctor.org/docs/user-manual/#cols-format).
As the following example shows, you can specify the widths of a table’s columns by using the `cols` attribute:

```
[cols="1,3"] (1)
include::{snippets}/index/links.adoc[]
```

**1**

The table’s width is split across its two columns, with the second column being three times as wide as the first.

<a id="index--working-with-asciidoctor-customizing-tables-title"></a>
<a id="index--configuring-the-title"></a>

#### [Configuring the Title](#index--working-with-asciidoctor-customizing-tables-title)

You can specify the title of a table by using a line prefixed by a `.`.
The following example shows how to do so:

```
.Links (1)
include::{snippets}/index/links.adoc[]
```

**1**

The table’s title will be `Links`.

<a id="index--working-with-asciidoctor-customizing-tables-formatting-problems"></a>
<a id="index--avoiding-table-formatting-problems"></a>

#### [Avoiding Table Formatting Problems](#index--working-with-asciidoctor-customizing-tables-formatting-problems)

Asciidoctor uses the `|` character to delimit cells in a table.
This can cause problems if you want a `|` to appear in a cell’s contents.
You can avoid the problem by escaping the `|` with a backslash — in other words, by using `\|` rather than `|`.

All of the default Asciidoctor snippet templates perform this escaping automatically by using a Mustache lamba named `tableCellContent`.
If you write your own custom templates you may want to use this lamba.
The following example shows how to escape `|` characters in a cell that contains the value of a `description` attribute:

```
| {{#tableCellContent}}{{description}}{{/tableCellContent}}
```

<a id="index--working-with-asciidoctor-further-reading"></a>
<a id="index--further-reading"></a>

### [Further Reading](#index--working-with-asciidoctor-further-reading)

See the [Tables section of the Asciidoctor user manual](https://asciidoctor.org/docs/user-manual/#tables) for more information about customizing tables.

<a id="index--working-with-markdown"></a>

## [Working with Markdown](#index--working-with-markdown)

This section describes the aspects of working with Markdown that are particularly relevant to Spring REST Docs.

<a id="index--working-with-markdown-limitations"></a>
<a id="index--limitations"></a>

### [Limitations](#index--working-with-markdown-limitations)

Markdown was originally designed for people writing for the web and, as such, is not as well-suited to writing documentation as Asciidoctor.
Typically, these limitations are overcome by using another tool that builds on top of Markdown.

Markdown has no official support for tables.
Spring REST Docs' default Markdown snippet templates use [Markdown Extra’s table format](https://michelf.ca/projects/php-markdown/extra/#table).

<a id="index--working-with-markdown-including-snippets"></a>
<a id="index--including-snippets-2"></a>

### [Including Snippets](#index--working-with-markdown-including-snippets)

Markdown has no built-in support for including one Markdown file in another.
To include the generated snippets of Markdown in your documentation, you should use an additional tool that supports this functionality.

<a id="index--contributing"></a>

## [Contributing](#index--contributing)

Spring REST Docs is intended to make it easy for you to produce high-quality documentation for your RESTful services.
However, we cannot achieve that goal without your contributions.

<a id="index--contributing-questions"></a>
<a id="index--questions"></a>

### [Questions](#index--contributing-questions)

You can ask questions about Spring REST Docs on [Stack Overflow](https://stackoverflow.com) by using the `spring-restdocs` tag.
Similarly, we encourage you to help your fellow Spring REST Docs users by answering questions.

<a id="index--contributing-bugs"></a>
<a id="index--bugs"></a>

### [Bugs](#index--contributing-bugs)

If you believe you have found a bug, please take a moment to search the [existing issues](https://github.com/spring-projects/spring-restdocs/issues?q=is%3Aissue).
If no one else has reported the problem, please [open a new issue](https://github.com/spring-projects/spring-restdocs/issues/new) that describes the problem in detail and, ideally, includes a test that reproduces it.

<a id="index--contributing-enhancements"></a>
<a id="index--enhancements"></a>

### [Enhancements](#index--contributing-enhancements)

If you would like an enhancement to be made to Spring REST Docs, pull requests are most welcome.
The source code is on [GitHub](https://github.com/spring-projects/spring-restdocs).
You may want to search the [existing issues](https://github.com/spring-projects/spring-restdocs/issues?q=is%3Aissue) and [pull requests](https://github.com/spring-projects/spring-restdocs/pulls?q=is%3Apr) to see if the enhancement has already been proposed.
You may also want to [open a new issue](https://github.com/spring-projects/spring-restdocs/issues/new) to discuss a possible enhancement before work on it begins.

---
