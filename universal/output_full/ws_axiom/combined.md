# Documentation – Axiom

## Navigation

- About
  - [Introduction](#index)
  - [Mailing Lists](#mail-lists)
  - [Project Team](#team)
  - [Issue Tracking](#issue-management)
- Downloads
  - [Releases](#download)
  - [Source Code](#scm)
- Documentation
  - [Overview](#documentation)
  - [Release notes](https://ws.apache.org/axiom/release-notes/index.html)
  - [Quick start samples](#quickstart-samples)
  - [User guide](#userguide-userguide)
  - [Developer guide](#devguide-devguide)
  - [Design documents](#design)
    - [OSGi integration](#design-osgi-integration)
    - [Fluent builders](#design-fluent-builder)
  - [Articles](#articles)
  - [Javadocs](https://ws.apache.org/axiom/apidocs/index.html)
  - [FAQ](#faq)
  - [View Source](https://github.com/apache/ws-axiom)
  - [Code Coverage](https://codecov.io/gh/apache/ws-axiom)
- Modules
  - [Implementations](#implementations)
  - [Compatibility classes](#axiom-compat)
  - [Google Truth extension for XML](#testing-xml-truth)
- [Apache](http://www.apache.org/)
  - [License](http://www.apache.org/licenses/LICENSE-2.0.html)
  - [Sponsorship](http://www.apache.org/foundation/sponsorship.html)
  - [Thanks](http://www.apache.org/foundation/thanks.html)
  - [Security](http://www.apache.org/security/)
  - [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
- [Web Services](https://ws.apache.org/)
- [Axiom](#index)
- [Testing](#testing)
- [Introduction](#testing-xml-truth)
- |
- Version: 2.0.0

## Content

<a id="index"></a>

<!-- source_url: https://ws.apache.org/axiom/index.html -->

<!-- page_index: 1 -->

# Welcome to Apache Axiom

The Apache Axiom™ library provides an XML Infoset compliant object model implementation which supports on-demand building of the object tree. It supports a novel "pull-through" model which allows one to turn off the tree building and directly access the underlying pull event stream using the StAX API. It also has built in support for XML Optimized Packaging (XOP) and MTOM, the combination of which allows XML to carry binary data efficiently and in a transparent manner. The combination of these is an easy to use API with a very high performant architecture!

Developed as part of Apache Axis2, Apache Axiom is the core of Apache Axis2. However, it is a pure standalone XML Infoset model with novel features and can be used independently of Apache Axis2.

Apache Axiom, Axiom, Apache, the Apache feather logo, and the Apache Axiom project logo are trademarks of [The Apache Software Foundation](http://apache.org/).

# Key Features

- Full XML Infoset compliant XML object model
- StAX based builders with on-demand building and pull-through
- XOP/MTOM support offering direct binary support
- Convenient SOAP Infoset API on top of Axiom
- Two implementations included:
  - Linked list based implementation
  - W3C DOM supporting implementation
- Highly performant

---

<a id="mail-lists"></a>

<!-- source_url: https://ws.apache.org/axiom/mail-lists.html -->

<!-- page_index: 2 -->

# Project Mailing Lists

The Apache Axiom project doesn't have dedicated mailing lists. Please use the [mailing lists of the Web Services project](http://ws.apache.org/mail-lists.html). When posting messages to these lists, please prefix the subject with [Axiom].

Note that the Axiom project formerly used the `commons-dev@ws.apache.org` mailing list, which no longer exists. However, the archives of that list can still be consulted [here](http://mail-archives.apache.org/mod_mbox/ws-commons-dev/).

---

<a id="team"></a>

<!-- source_url: https://ws.apache.org/axiom/team.html -->

<!-- page_index: 3 -->

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization |
| --- | --- | --- | --- | --- | --- |
|  | saminda | Saminda Abeyruwan | [saminda AT wso2.com](mailto:saminda AT wso2.com) | - | WSO2 |
|  | azeez | Afkham Azeez | [azeez AT wso2.com](mailto:azeez AT wso2.com) | - | WSO2 |
|  | chinthaka | Eran Chinthaka | [chinthaka AT wso2.com](mailto:chinthaka AT wso2.com) | <http://www.apache.org/~chinthaka> | WSO2 |
|  | gdaniels | Glen Daniels | [gdaniels AT apache.org](mailto:gdaniels AT apache.org) | - | Sonic Software |
|  | jaliya | Jaliya Ekanayake | [jaliya AT opensource.lk](mailto:jaliya AT opensource.lk) | <http://www.apache.org/~jaliya> | Virtusa / Lanka Software Foundation |
|  | senaka | Senaka Fernando | [senaka AT apache.org](mailto:senaka AT apache.org) | - | WSO2 |
|  | nandana | Nandana Mihindukulasooriya | [nandana AT wso2.com](mailto:nandana AT wso2.com) | - | WSO2 |
|  | ruchith | Ruchith Fernando | [ruchith AT wso2.com](mailto:ruchith AT wso2.com) | - | WSO2 |
|  | thilina | Thilina Gunarathne | [thilina AT wso2.com](mailto:thilina AT wso2.com) | <http://www.apache.org/~thilina> | WSO2 |
|  | chathura | Chathura Herath | [chathura AT opensource.lk](mailto:chathura AT opensource.lk) | <http://www.apache.org/~chathura> | LSF/MIT |
|  | deepal | Deepal Jayasinghe | [deepal AT wso2.com](mailto:deepal AT wso2.com) | <http://www.apache.org/~deepal> | WSO2 |
|  | robertlazarski | Robert Lazarski | [robertlazarski AT gmail.com](mailto:robertlazarski AT gmail.com) | - | Alpha Theory |
|  | chatra | Chatra Nakkawita | [chatra AT WSO2.com](mailto:chatra AT WSO2.com) | - | WSO2 |
|  | hemapani | Srinath Perera | [hemapani AT apache.org](mailto:hemapani AT apache.org) | <http://www.apache.org/~hemapani> | Lanka Software Foundation |
|  | ajith | Ajith Ranabahu | [ajith AT wso2.com](mailto:ajith AT wso2.com) | <http://www.apache.org/~ajith> | WSO2 |
|  | venkat | Venkat Reddy | [vreddyp AT gmail.com](mailto:vreddyp AT gmail.com) | - | Computer Associates |
|  | scheu | Rich Scheuerle | [scheu AT us.ibm.com](mailto:scheu AT us.ibm.com) | - | IBM |
|  | ashu | Ashutosh Shahi | [Ashutosh.Shahi AT ca.com](mailto:Ashutosh.Shahi AT ca.com) | - | Computer Associates |
|  | alek | Aleksander Slominski | [aslom AT cs.indiana.edu](mailto:aslom AT cs.indiana.edu) | - | Indiana University Extreme! Computing Lab |
|  | dims | Davanum Srinivas | [davanum AT gmail.com](mailto:davanum AT gmail.com) | - | IBM |
|  | jaya | Jayachandra Sekhara Rao Sunkara | [jayachandra AT gmail.com](mailto:jayachandra AT gmail.com) | - | Computer Associates |
|  | veithen | Andreas Veithen | [veithen AT google.com](mailto:veithen AT google.com) | <http://veithen.github.io> | Google |
|  | dasarath | Dasarath Weerathunga | [dasarath AT opensource.lk](mailto:dasarath AT opensource.lk) | - | Lanka Software Foundation |
|  | sanjiva | Sanjiva Weerawarana | [sanjiva AT wso2.com](mailto:sanjiva AT wso2.com) | - | WSO2 |

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization |
| --- | --- | --- | --- |
|  | Dharshana Dias | [-](mailto:) | Lanka Software Foundation / University of Moratuwa |
|  | Anushka Kumara | [anushkakumar AT gmail.com](mailto:anushkakumar AT gmail.com) | Lanka Software Foundation / University of Moratuwa |
|  | Chinthaka Thilakarathne | [-](mailto:) | Lanka Software Foundation / University of Moratuwa |
|  | Jochen Wiedmann | [jochen.wiedmann AT gmail.com](mailto:jochen.wiedmann AT gmail.com) | - |

---

<a id="issue-management"></a>

<!-- source_url: https://ws.apache.org/axiom/issue-management.html -->

<!-- page_index: 4 -->

# Overview

This project uses [JIRA](http://www.atlassian.com/software/jira).

# Issue Management

Issues, bugs, and feature requests should be submitted to the following issue management system for this project.

```
http://issues.apache.org/jira/browse/AXIOM
```

---

<a id="download"></a>

<!-- source_url: https://ws.apache.org/axiom/download.html -->

<!-- page_index: 5 -->

# Releases

The current release is 2.0.0 and was published on January 27, 2025. The release note for this
release can be found [here](https://ws.apache.org/axiom/release-notes/2.0.0.html).

The following distributions are available for download:

|  | Link | Checksums and signatures |
| --- | --- | --- |
| Binary distribution | [axiom-2.0.0-bin.zip](http://www.apache.org/dyn/closer.lua/ws/axiom/2.0.0/axiom-2.0.0-bin.zip) | [SHA512](https://downloads.apache.org/ws/axiom/2.0.0/axiom-2.0.0-bin.zip.sha512) [PGP](https://downloads.apache.org/ws/axiom/2.0.0/axiom-2.0.0-bin.zip.asc) |
| Source distribution | [axiom-2.0.0-src.zip](http://www.apache.org/dyn/closer.lua/ws/axiom/2.0.0/axiom-2.0.0-src.zip) | [SHA512](https://downloads.apache.org/ws/axiom/2.0.0/axiom-2.0.0-src.zip.sha512) [PGP](https://downloads.apache.org/ws/axiom/2.0.0/axiom-2.0.0-src.zip.asc) |

The signatures of the distributions can be [verified](http://www.apache.org/dev/release-signing#verifying-signature) against the public keys in the [KEYS](https://downloads.apache.org/ws/axiom/KEYS) file.

Distributions for older releases can be found in the archive, either [here](http://archive.apache.org/dist/ws/axiom/) or [here](http://archive.apache.org/dist/ws/commons/axiom/).

All releases are also available as Maven artifacts in the [central repository](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.apache.ws.commons.axiom%22).

---

<a id="scm"></a>

<!-- source_url: https://ws.apache.org/axiom/scm.html -->

<!-- page_index: 6 -->

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=ws-axiom.git;a=summary
```

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch 2.0.0 https://gitbox.apache.org/repos/asf/ws-axiom.git
```

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch 2.0.0 https://gitbox.apache.org/repos/asf/ws-axiom.git
```

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="documentation"></a>

<!-- source_url: https://ws.apache.org/axiom/documentation.html -->

<!-- page_index: 7 -->

# Documentation – Axiom

The following documentation for the Axiom framework is available:

- A [User Guide](#userguide-userguide) explaining how to use Axiom in your project.
- A [Developer Guide](#devguide-devguide) containing information for committers and contributors.
- The [Javadoc](https://ws.apache.org/axiom/apidocs/index.html) for the Axiom API.

The user and developer guides are also available in PDF format in the binary distribution and as individual Maven artifacts that can be downloaded from the central repository or the Apache snapshot repository.

---

<a id="quickstart-samples"></a>

<!-- source_url: https://ws.apache.org/axiom/quickstart-samples.html -->

<!-- page_index: 8 -->

# Quick Start Samples

Content:

- [Quick Start Samples](#quickstart-samples--quick_start_samples)
  - [Adding Axiom as a Maven dependency](#quickstart-samples--adding_axiom_as_a_maven_dependency)
  - [Parsing and processing an XML document](#quickstart-samples--parsing_and_processing_an_xml_document)
  - [Schema validation using javax.xml.validation](#quickstart-samples--schema_validation_using_javax.xml.validation)
  - [Loading local chunks from a large XML document](#quickstart-samples--loading_local_chunks_from_a_large_xml_document)
  - [Processing MTOM messages](#quickstart-samples--processing_mtom_messages)
  - [Logging MTOM messages without inlining optimized binary data](#quickstart-samples--logging_mtom_messages_without_inlining_optimized_binary_data)

## Adding Axiom as a Maven dependency

To use Axiom in a project built using Maven, add the following dependencies:

```
<dependency>
    <groupId>org.apache.ws.commons.axiom</groupId>
    <artifactId>axiom-api</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.ws.commons.axiom</groupId>
    <artifactId>axiom-impl</artifactId>
    <version>2.0.0</version>
    <scope>runtime</scope>
</dependency>
```

Note that the `axiom-impl` dependency is added in scope `runtime`
because application code should not refer to implementation classes directly.
All Axiom features are accessible through the public API which is provided
by `axiom-api`.

If the application code requires a DOM compliant Axiom implementation, then the following dependency needs to be added too:

```
<dependency>
    <groupId>org.apache.ws.commons.axiom</groupId>
    <artifactId>axiom-dom</artifactId>
    <version>2.0.0</version>
    <scope>runtime</scope>
</dependency>
```

## Parsing and processing an XML document

The following sample shows how to parse and process an XML document using Axiom.
It is pretty much self-explaining:

```
    public void processFile(File file) throws IOException, OMException {
        // Create a builder for the file and get the root element
        InputStream in = new FileInputStream(file);
        OMElement root = OMXMLBuilderFactory.createOMBuilder(in).getDocumentElement();

        // Process the content of the file
        OMElement urlElement =
                root.getFirstChildWithName(new QName("http://maven.apache.org/POM/4.0.0", "url"));
        if (urlElement == null) {
            System.out.println("No <url> element found");
        } else {
            System.out.println("url = " + urlElement.getText());
        }

        // Because Axiom uses deferred parsing, the stream must be closed AFTER
        // processing the document (unless OMElement#build() is called)
        in.close();
    }
```

## Schema validation using javax.xml.validation

This sample demonstrates how to validate a part of an Axiom tree (actually the body of a SOAP message)
using the `javax.xml.validation` API:

```
    public void validate(InputStream in, URL schemaUrl) throws Exception {
        SOAPModelBuilder builder = OMXMLBuilderFactory.createSOAPModelBuilder(in, "UTF-8");
        SOAPEnvelope envelope = builder.getSOAPEnvelope();
        OMElement bodyContent = envelope.getBody().getFirstElement();
        SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        Schema schema = schemaFactory.newSchema(schemaUrl);
        Validator validator = schema.newValidator();
        validator.validate(bodyContent.getSAXSource(true));
    }
```

It leverages the fact that Axiom is capable of constructing a `SAXSource` from an `OMDocument`
or `OMElement`.

Alternatively, one can use a DOM compliant Axiom implementation and use a
`DOMSource` to pass the XML fragment to the validator:

```
    public void validateUsingDOM(InputStream in, URL schemaUrl) throws Exception {
        OMMetaFactory mf = OMAbstractFactory.getMetaFactory(OMAbstractFactory.FEATURE_DOM);
        SOAPModelBuilder builder = OMXMLBuilderFactory.createSOAPModelBuilder(mf, in, "UTF-8");
        SOAPEnvelope envelope = builder.getSOAPEnvelope();
        OMElement bodyContent = envelope.getBody().getFirstElement();
        SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        Schema schema = schemaFactory.newSchema(schemaUrl);
        Validator validator = schema.newValidator();
        validator.validate(new DOMSource((Element) bodyContent));
    }
```

## Loading local chunks from a large XML document

Here the goal is to process a large XML document “by chunks”, i.e.

1. Parse the file and find a relevant element (e.g. by name)
2. Load this element into memory as an `OMElement`.
3. Process the `OMElement` (the “chunk”).

The process is repeated until the end of the document is reached.

This can be achieved without loading the entire document into memory (and without loading all the
chunks in memory) by scanning the document using the StAX API and switching to Axiom when a
matching element is found:

```
    public void processFragments(InputStream in) throws XMLStreamException {
        // Create an XMLStreamReader without building the object model
        XMLStreamReader reader =
                OMXMLBuilderFactory.createOMBuilder(in).getDocument().getXMLStreamReader(false);
        while (reader.hasNext()) {
            if (reader.getEventType() == XMLStreamReader.START_ELEMENT
                    && reader.getName().equals(new QName("tag"))) {
                // A matching START_ELEMENT event was found. Build a corresponding OMElement.
                OMElement element =
                        OMXMLBuilderFactory.createStAXOMBuilder(reader).getDocumentElement();
                // Make sure that all events belonging to the element are consumed so
                // that the XMLStreamReader points to a well defined location (namely the
                // event immediately following the END_ELEMENT event).
                element.build();
                // Now process the element.
                processFragment(element);
            } else {
                reader.next();
            }
        }
    }
```

The code leverages the fact that `createStAXOMBuilder` can be used to build a fragment
(corresponding to a given element) from a StAX stream reader, simply by passing an
`XMLStreamReader` that is positioned on a `START_ELEMENT` event.

## Processing MTOM messages

This sample shows how to process MTOM messages with Axiom. The code actually sends a request to
the following JAX-WS service:

```
@WebService(targetNamespace = "urn:test")
@MTOM
public class MTOMService {
    @WebMethod
    @WebResult(name = "content")
    public DataHandler retrieveContent(@WebParam(name = "fileId") String fileId) {
        return new DataHandler(new URLDataSource(MTOMService.class.getResource("test.txt")));
    }
}
```

It then extracts the binary content from the response and writes it to a given `OutputStream`:

```
    public void retrieveContent(URL serviceURL, String id, OutputStream result) throws Exception {
        // Build the SOAP request
        SOAPFactory soapFactory = OMAbstractFactory.getSOAP11Factory();
        SOAPEnvelope request = soapFactory.getDefaultEnvelope();
        OMElement retrieveContent =
                soapFactory.createOMElement(
                        new QName("urn:test", "retrieveContent"), request.getBody());
        OMElement fileId = soapFactory.createOMElement(new QName("fileId"), retrieveContent);
        fileId.setText(id);

        // Use the java.net.URL API to connect to the service and send the request
        URLConnection connection = serviceURL.openConnection();
        connection.setDoOutput(true);
        OMOutputFormat format = new OMOutputFormat();
        format.setDoOptimize(true);
        format.setCharSetEncoding("UTF-8");
        connection.addRequestProperty("Content-Type", format.getContentType());
        OutputStream out = connection.getOutputStream();
        request.serialize(out, format);
        out.close();

        // Get the SOAP response
        InputStream in = connection.getInputStream();
        MultipartBody multipartBody =
                MultipartBody.builder()
                        .setInputStream(in)
                        .setContentType(connection.getContentType())
                        .build();
        SOAPEnvelope response =
                OMXMLBuilderFactory.createSOAPModelBuilder(multipartBody).getSOAPEnvelope();
        OMElement retrieveContentResponse = response.getBody().getFirstElement();
        OMElement content = retrieveContentResponse.getFirstElement();
        // Extract the Blob representing the optimized binary data
        Blob blob = ((OMText) content.getFirstOMChild()).getBlob();
        // Stream the content of the MIME part
        InputStream contentStream = ((PartBlob) blob).getPart().getInputStream(false);
        // Write the content to the result stream
        IOUtils.copy(contentStream, result);
        contentStream.close();

        in.close();
    }
```

The sample code shows that in order to parse an MTOM message one first needs to construct an
`MultipartBody` object that is then passed to the relevant method in `OMXMLBuilderFactory`.
In the object model, an XOP/MTOM attachment is represented as an `OMText` node for which `isBinary()` returns
`true`. Such a node is created for each `xop:Include` element in the original message.
The binary data is stored in a `DataHandler` object that can be obtained by a call to the
`getDataHandler()` method of the `OMText` node.

By default attachments are loaded into memory, but the `MultipartBody` can be configured to buffer
data on disk. The sample actually shows an alternative method to reduce the
memory footprint of the MTOM processing, which is to enable streaming.

## Logging MTOM messages without inlining optimized binary data

A common way to log a SOAP message is to invoke the `toString` method on the corresponding `SOAPEnvelope`
object and send the result to the logger. However, this is problematic for MTOM messages because the
`toString` method will always serialize the message as plain XML and therefore inline optimized
binary data using base64 encoding.

Except for this particular use case, serializing a message using MTOM without actually producing
the MIME parts for the binary data is not meaningful and is therefore not directly supported by
the Axiom API. The solution is to use a custom `XMLStreamWriter` implementation that uses an
Axiom specific extension to accept `DataHandler` objects and replaces them by some
placeholder text:

```
public class LogWriter extends XMLStreamWriterWrapper implements BlobWriter {
    public LogWriter(XMLStreamWriter parent) {
        super(parent);
    }

    @Override
    public Object getProperty(String name) throws IllegalArgumentException {
        if (name.equals(BlobWriter.PROPERTY)) {
            return this;
        } else {
            return super.getProperty(name);
        }
    }

    @Override
    public void writeBlob(Blob blob, String contentID, boolean optimize)
            throws IOException, XMLStreamException {
        super.writeCharacters("[base64 encoded data]");
    }

    @Override
    public void writeBlob(BlobProvider blobProvider, String contentID, boolean optimize)
            throws IOException, XMLStreamException {
        super.writeCharacters("[base64 encoded data]");
    }
}
```

The following code shows how this class would be used to log the MTOM message:

```
    private void logMessage(SOAPEnvelope env) throws XMLStreamException {
        StringWriter sw = new StringWriter();
        XMLStreamWriter writer =
                new LogWriter(XMLOutputFactory.newInstance().createXMLStreamWriter(sw));
        env.serialize(writer);
        writer.flush();
        log.info("Message: " + sw.toString());
    }
```

---

<a id="userguide-userguide"></a>

<!-- source_url: https://ws.apache.org/axiom/userguide/userguide.html -->

<!-- page_index: 9 -->

# Axiom User Guide

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">Axiom User Guide</th></tr><tr><td align="left" width="20%"> </td><th align="center" width="60%"> </th><td align="right" width="20%"> <a href="https://ws.apache.org/axiom/userguide/ch01.html">Next</a></td></tr></table>

---

# Axiom User Guide

2.0.0

> [!NOTE]
> **http://www.apache.org/licenses/LICENSE-2.0**
> Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See
> the NOTICE file distributed with this work for additional information regarding copyright ownership. The
> ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use
> this file except in compliance with the License. You may obtain a copy of the License at
>
> Unless required by applicable law or agreed to in writing, software distributed under the License is
> distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
> implied. See the License for the specific language governing permissions and limitations under the
> License.

---

**Table of Contents**

[1. Introduction](https://ws.apache.org/axiom/userguide/ch01.html)
:   [What is Axiom?](https://ws.apache.org/axiom/userguide/ch01.html#d0e21)

    [For whom is this Tutorial?](https://ws.apache.org/axiom/userguide/ch01.html#d0e35)

    [What is Pull Parsing?](https://ws.apache.org/axiom/userguide/ch01.html#d0e48)

    [A Bit of History](https://ws.apache.org/axiom/userguide/ch01.html#d0e62)

    [Features of Axiom](https://ws.apache.org/axiom/userguide/ch01.html#d0e76)

    [Relation with StAX](https://ws.apache.org/axiom/userguide/ch01.html#d0e111)

    [A Bit About Caching](https://ws.apache.org/axiom/userguide/ch01.html#d0e128)

    [Where Does SOAP Come into Play?](https://ws.apache.org/axiom/userguide/ch01.html#d0e135)

[2. Working with Axiom](https://ws.apache.org/axiom/userguide/ch02.html)
:   [Obtaining the Axiom Binary](https://ws.apache.org/axiom/userguide/ch02.html#d0e146)

    [Creating an object model programmatically](https://ws.apache.org/axiom/userguide/ch02.html#d0e183)

    [Creating an object model by parsing an XML document](https://ws.apache.org/axiom/userguide/ch02.html#d0e257)

    [Namespaces](https://ws.apache.org/axiom/userguide/ch02.html#d0e325)

    [Traversing](https://ws.apache.org/axiom/userguide/ch02.html#d0e367)

    [Serializer](https://ws.apache.org/axiom/userguide/ch02.html#serializer)

    [Complete Code for the Axiom based Document Building and Serialization](https://ws.apache.org/axiom/userguide/ch02.html#d0e477)

    [Creating stream readers and writers using `StAXUtils`](https://ws.apache.org/axiom/userguide/ch02.html#StAXUtils)

    [Releasing the parser](https://ws.apache.org/axiom/userguide/ch02.html#d0e580)

    [Exception handling](https://ws.apache.org/axiom/userguide/ch02.html#d0e608)

[3. Advanced Operations with Axiom](https://ws.apache.org/axiom/userguide/ch03.html)
:   [Accessing the Pull Parser](https://ws.apache.org/axiom/userguide/ch03.html#d0e672)

[4. Integrating Axiom into your project](https://ws.apache.org/axiom/userguide/ch04.html)
:   [Using Axiom in a Maven 2 project](https://ws.apache.org/axiom/userguide/ch04.html#using-maven2)

    [Applying application wide configuration](https://ws.apache.org/axiom/userguide/ch04.html#d0e729)
    :   [Changing the default StAX factory settings](https://ws.apache.org/axiom/userguide/ch04.html#factory.properties)

    [Migrating from older Axiom versions](https://ws.apache.org/axiom/userguide/ch04.html#d0e863)

[5. Common mistakes, problems and anti-patterns](https://ws.apache.org/axiom/userguide/ch05.html)
:   [Violating the `javax.activation.DataSource` contract](https://ws.apache.org/axiom/userguide/ch05.html#d0e873)

    [Issues that “magically” disappear](https://ws.apache.org/axiom/userguide/ch05.html#d0e943)

    [The OM-inside-OMDataSource anti-pattern](https://ws.apache.org/axiom/userguide/ch05.html#d0e985)
    :   [Weak version](https://ws.apache.org/axiom/userguide/ch05.html#d0e988)

        [Strong version](https://ws.apache.org/axiom/userguide/ch05.html#d0e1127)

[6. Appendix](https://ws.apache.org/axiom/userguide/ch06.html)
:   [Program Listing for Build and Serialize](https://ws.apache.org/axiom/userguide/ch06.html#d0e1206)

    [Links](https://ws.apache.org/axiom/userguide/ch06.html#links)

[References](https://ws.apache.org/axiom/userguide/bi01.html)

**List of Figures**

1.1. [Architecture overview](https://ws.apache.org/axiom/userguide/ch01.html#d0e105)

2.1. [The Axiom API with different implementations](https://ws.apache.org/axiom/userguide/ch02.html#fig_api)

**List of Examples**

2.1. [Creating an object model programmatically](https://ws.apache.org/axiom/userguide/ch02.html#list2)

2.2. [Usage of `addChild`](https://ws.apache.org/axiom/userguide/ch02.html#ex-addChild)

2.3. [Creating an object model from an input stream](https://ws.apache.org/axiom/userguide/ch02.html#list1)

2.4. [Creating an OM document with namespaces](https://ws.apache.org/axiom/userguide/ch02.html#list6)

5.1. [`DataSource` implementation that violates the interface contract](https://ws.apache.org/axiom/userguide/ch05.html#InputStreamDataSource)

5.2. [`OMDataSource#getReader()` implementation used in older ADB versions](https://ws.apache.org/axiom/userguide/ch05.html#adb-getReader)

---

|  |  |  |
| --- | --- | --- |
|  |  | [Next](https://ws.apache.org/axiom/userguide/ch01.html) |
|  |  | Chapter 1. Introduction |

---

<a id="devguide-devguide"></a>

<!-- source_url: https://ws.apache.org/axiom/devguide/devguide.html -->

<!-- page_index: 10 -->

# Axiom Developer Guide

<table summary="Navigation header" width="100%"><tr><th align="center" colspan="3">Axiom Developer Guide</th></tr><tr><td align="left" width="20%"> </td><th align="center" width="60%"> </th><td align="right" width="20%"> <a href="https://ws.apache.org/axiom/devguide/ch01.html">Next</a></td></tr></table>

---

# Axiom Developer Guide

2.0.0

> [!NOTE]
> **http://www.apache.org/licenses/LICENSE-2.0**
> Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See
> the NOTICE file distributed with this work for additional information regarding copyright ownership. The
> ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use
> this file except in compliance with the License. You may obtain a copy of the License at
>
> Unless required by applicable law or agreed to in writing, software distributed under the License is
> distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
> implied. See the License for the specific language governing permissions and limitations under the
> License.

---

**Table of Contents**

[1. Working with the Axiom source code](https://ws.apache.org/axiom/devguide/ch01.html)
:   [Importing the Axiom source code into Eclipse](https://ws.apache.org/axiom/devguide/ch01.html#d0e21)

    [Testing](https://ws.apache.org/axiom/devguide/ch01.html#d0e52)
    :   [Unit test organization](https://ws.apache.org/axiom/devguide/ch01.html#d0e55)

        [Testing Axiom with different StAX implementations](https://ws.apache.org/axiom/devguide/ch01.html#d0e151)

[2. Design](https://ws.apache.org/axiom/devguide/ch02.html)
:   [General design principles and goals](https://ws.apache.org/axiom/devguide/ch02.html#d0e212)

    [`LifecycleManager` design (Axiom 1.3)](https://ws.apache.org/axiom/devguide/ch02.html#d0e236)
    :   [Issues with the `LifecycleManager` API in Axiom 1.2.x](https://ws.apache.org/axiom/devguide/ch02.html#d0e249)

        [Cleanup strategy for temporary files](https://ws.apache.org/axiom/devguide/ch02.html#d0e361)

[3. Release process](https://ws.apache.org/axiom/devguide/ch03.html)
:   [Release preparation](https://ws.apache.org/axiom/devguide/ch03.html#d0e462)

    [Prerequisites](https://ws.apache.org/axiom/devguide/ch03.html#d0e529)

    [Release](https://ws.apache.org/axiom/devguide/ch03.html#d0e560)

    [Post-release actions](https://ws.apache.org/axiom/devguide/ch03.html#d0e783)

    [References](https://ws.apache.org/axiom/devguide/ch03.html#d0e801)

[A. Appendix](https://ws.apache.org/axiom/devguide/apa.html)
:   [Installing IBM's JDK on Debian Linux](https://ws.apache.org/axiom/devguide/apa.html#install.ibm.jdk)

---

|  |  |  |
| --- | --- | --- |
|  |  | [Next](https://ws.apache.org/axiom/devguide/ch01.html) |
|  |  | Chapter 1. Working with the Axiom source code |

---

<a id="design"></a>

<!-- source_url: https://ws.apache.org/axiom/design/index.html -->

<!-- page_index: 11 -->

# Design documents

| Title/link | Status |
| --- | --- |
| [OSGi integration and separation between API and implementation](#design-osgi-integration) | Implemented |
| [Fluent builders](#design-fluent-builder) | Implemented |

---

<a id="design-osgi-integration"></a>

<!-- source_url: https://ws.apache.org/axiom/design/osgi-integration.html -->

<!-- page_index: 12 -->

# OSGi integration and separation between API and implementation

## Introduction

This section addresses two related architectural questions:

- OSGi support was originally introduced in Axiom 1.2.9, but the implementation had
  a couple of flaws. This section discusses the rationale behind the new OSGi
  support introduced in Axiom 1.2.13.
- Axiom is designed as a set of abstract APIs for which two implementations are
  provided: LLOM and DOOM. It is important to make a clear distinction between what
  is part of the public API and what should be considered implementation classes that
  must not be used by application code directly. This also implies that Axiom must
  provide the necessary APIs to allow application code to access all features without
  the need to access implementation classes directly. This section in particular
  discusses the question how application code can request factories that support DOM
  without the need to refer directly to DOOM.

These two questions are closely related because OSGi allows to enforce the distinction
between public API and implementation classes by carefully selecting the packages
exported by the different bundles: only classes belonging to the public API
should be exported, while implementation classes should be private to the bundles
containing them. This in turn has implications for the packaging of these artifacts.

## Requirements

**Requirement 1**: *The Axiom artifacts SHOULD be usable both as normal JAR files and as OSGi bundles.*

The alternative would be to produce two sets of artifacts during the build. This
should be avoided in order to keep the build process as simple as possible.
It should also be noted that the Geronimo Spec artifacts also meet this requirement.

**Requirement 2**: *All APIs defined by the `axiom-api` module, and in particular the
`OMAbstractFactory` API MUST continue to work as expected in an OSGi environment, so that code
in downstream projects doesn't need to be rewritten.*

This requirement was already satisfied by the OSGi support introduced in Axiom 1.2.9.
It therefore also ensures that the transition to the new OSGi support in Axiom 1.2.13
is transparent for applications that already use Axiom in an OSGi container.

**Requirement 3**: *`OMAbstractFactory` MUST select the same implementation
regardless of the type of container (OSGi or non OSGi). The only exception is
related to the usage of system properties to specify the default `OMMetaFactory`
implementation: in an OSGi environment, selecting an implementation class using
a system property is not meaningful.*

**Requirement 4**: *Only classes belonging to the public API should be exported by the OSGi bundles.
Implementation classes should not be exported. In particular, the bundles for the LLOM and DOOM implementations MUST NOT export any packages.
This is required to keep a clean separation between the public API and implementation
specific classes and to make sure that the implementations can be modified without the
risk of breaking existing code.
An exception MAY be made for factory classes related to foreign APIs, such as the
`DocumentBuilderFactory` implementation for an Axiom implementation
supporting DOM.*

When the Axiom artifacts are used as normal JAR files in a Maven build, this requirement implies that
they should be used in scope `runtime`.

Although this requirement is easy to implement for the Axiom project, it requires
changes to downstreams project to make this actually work:

- As explained in [AXIS2-4902](https://issues.apache.org/jira/browse/AXIS2-4902),
  there used to be many places in Axis2 that still referred directly to Axiom implementation classes.
  The same was true for Rampart and Sandesha2. This has now been fixed and all three projects
  use `axiom-impl` and `axiom-dom` as dependencies in scope
  `runtime`.
- Abdera extends the LLOM implementation. Probably, some `maven-shade-plugin`
  magic will be required here to create Abdera OSGi bundles that work properly with
  the Axiom bundles.
- For Spring Web Services this issue is addressed by
  [SWS-822](https://jira.springsource.org/browse/SWS-822).

**Requirement 5**: *It MUST be possible to use a non standard (third party) Axiom implementation as a drop-in replacement
for the standard LLOM and DOOM implementation, i.e. the `axiom-impl`
and `axiom-dom` bundles. It MUST be possible to replace `axiom-impl`
(resp. `axiom-dom`) by any Axiom implementation that supports the full Axiom API
(resp. that supports DOM in addition to the Axiom API), without the need to change any application code.*

This requirement has several important implications:

- It restricts the allowable exceptions to [Requirement 4](#design-osgi-integration--req4).
- It implies that there must be an API that allows application code to select an Axiom
  implementation based on its capabilities (e.g. DOM support) without introducing a
  hard dependency on a particular Axiom implementation.
- In accordance with [Requirement 2](#design-osgi-integration--req2) and [Requirement 3](#design-osgi-integration--req3)
  this requirement not only applies to an OSGi environment, but extends to non OSGi environments as well.

**Requirement 6**: *The OSGi integration SHOULD remove the necessity for downstreams projects
to produce their own custom OSGi bundles for Axiom. There SHOULD be one
and only one set of OSGi bundles for Axiom, namely the ones released by the Axiom project.*

Currently there are at least two projects that create their own modified Axiom bundles:

- Apache Geronimo has a custom Axiom bundle to support the Axis2 integration.
- ServiceMix also has a custom bundles for Axiom. However, this bundle only seem to exist to
  support their own custom Abdera bundle, which is basically an incorrect repackaging of the
  original Abdera code. See
  [SMX4-877](https://issues.apache.org/jira/browse/SMX4-877) for more details.

Note that this requirement can't be satisfied directly by Axiom. It requires that
the above mentioned projects (Geronimo, Axis2 and Abdera) use Axiom in a way that is
compatible with its design, and in particular with [Requirement 4](#design-osgi-integration--req4).
Nevertheless, Axiom must provide the necessary APIs and features to meet the needs
of these projects.

**Requirement 7**: *The Axiom OSGi integration SHOULD NOT rely on any particular OSGi framework such
as Felix SCR (Declarative Services). When deployed in an OSGi environment, Axiom should have the same
runtime dependencies as in a non OSGi environment (i.e. StAX, Activation and JavaMail).*

Axiom 1.2.12 relies on Felix SCR. Although there is no real issue with that, getting rid
of this extra dependency is seen as a nice to have. One of the reasons for using Felix SCR
was to avoid introducing OSGi specific code into Axiom. However, there is no issue with
having such code, provided that [Requirement 8](#design-osgi-integration--req8) is satisfied.

**Requirement 8**: *In a non OSGi environment, Axiom MUST NOT have any OSGi related dependencies. That means
that the OSGi integration must be written in such a way that no OSGi specific classes are
ever loaded in a non OSGi environment.*

**Requirement 9**: *The OSGi integration MUST follow established best practices. It SHOULD be inspired by
what has been done to add OSGi integration to APIs that have a similar structure as Axiom.*

Axiom is designed around an abstract API and allows for the existence of multiple
independent implementations. A factory (`OMAbstractFactory`) is used to
locate and instantiate the desired implementation. This is similar to APIs such as
JAXP (`DocumentBuilderFactory`, etc.) and JAXB (`JAXBContext`).
These APIs have been successfully “OSGi-fied” e.g. by the Apache Geronimo project.
Instead of reinventing the wheel, we should leverage that work and adapt it to
Axiom's specific requirements.

It should be noted that because of the way the Axiom API is designed and taking into account
[Requirement 2](#design-osgi-integration--req2), it is not possible to make Axiom entirely compatible
with OSGi paradigms (the same is true for JAXB). In an OSGi-only world, each Axiom
implementation would simply expose itself as an OSGi service (of type `OMMetaFactory` e.g.)
and code depending on Axiom would bind to one (or more) of these services depending on its needs.
That is not possible because it would conflict with [Requirement 2](#design-osgi-integration--req2).

**Non-Requirement 1**: *APIs such as JAXP and JAXB have been designed from the start for inclusion into the JRE.
They need to support scenarios where an application bundles its own implementation
(e.g. an application may package a version of Apache Xerces, which would then be
instantiated by the `newInstance` method in
`DocumentBuilderFactory`). That implies that the selected implementation
depends on the thread context class loader. It is assumed that there is no such requirement
for Axiom, which means that in a non OSGi environment, the Axiom implementations are always loaded from the same
class loader as the `axiom-api` JAR.*

This (non-)requirement is actually not directly relevant for the OSGi support, but it
nevertheless has some importance because of [Requirement 3](#design-osgi-integration--req3)
(which implies that the OSGi support needs to be designed in parallel with the implementation
discovery strategy applicable in a non OSGi environment).

## Analysis of the Geronimo JAXB bundles

As noted in [Requirement 9](#design-osgi-integration--req9) the Apache Geronimo has successfully
added OSGi support to the JAXB API which has a structure similar to the Axiom API. This section briefly describes
how this works. The analysis refers to the following Geronimo artifacts:
`org.apache.geronimo.specs:geronimo-jaxb_2.2_spec:1.0.1` (called the “API bundle” hereafter), `org.apache.geronimo.bundles:jaxb-impl:2.2.3-1_1` (the “implementation bundle”), `org.apache.geronimo.specs:geronimo-osgi-locator:1.0` (the “locator bundle”) and
`org.apache.geronimo.specs:geronimo-osgi-registry:1.0` (the “registry bundle”):

- The implementation bundle retains the `META-INF/services/javax.xml.bind.JAXBContext`
  resource from the original artifact (`com.sun.xml.bind:jaxb-impl`).
  In a non OSGi environment, that resource will be used to discover the implementation, following
  the standard JDK 1.3 service discovery algorithm will (as required by the JAXB specification).
  This is the equivalent of our [Requirement 1](#design-osgi-integration--req1).
- The manifest of the implementation bundle has an attribute `SPI-Provider: true` that indicates
  that it contains provider implementations that are discovered using the JDK 1.3 service discovery.
- The registry bundle creates a `BundleTracker` that looks for
  the `SPI-Provider` attribute in active bundles. For each bundle
  that has this attribute set to `true`, it will scan the content of
  `META-INF/services` and add the discovered services to a registry
  (Note that the registry bundle supports other ways to declare SPI providers,
  but this is not really relevant for the present discussion).
- The `ContextFinder` class (the interface of which is defined by
  the JAXB specification and that is used by the `newInstance`
  method in `JAXBContext`) in the API bundle delegates the discovery
  of the SPI implementation to a static method of the `ProviderLocator`
  class defined by the locator bundle (which is not specific to JAXB and is used by other
  API bundles as well). This is true both in an OSGi environment and in a non OSGi environment.

  The build is configured (using a `Private-Package` instruction)
  such that the classes of the locator bundle are actually included into the API bundle, thus
  avoiding an additional dependency.
- The `ProviderLocator` class and related code provided by the locator bundle is designed
  such that in a non OSGi environment, it will simply use JDK 1.3 service discovery to locate
  the SPI implementation, without ever loading any OSGi specific class. On the other hand,
  in an OSGi environment, it will query the registry maintained by the registry bundle to locate
  the provider. The reference to the registry is injected into the `ProviderLocator`
  class using a bundle activator.
- Finally, it should also be noted that the API bundle is configured with `singleton=true`.
  There is indeed no meaningful way how providers could be matched with different versions of the same API
  bundle.

This is an example of a particularly elegant way to satisfy [Requirement 1](#design-osgi-integration--req1), [Requirement 2](#design-osgi-integration--req2) and [Requirement 3](#design-osgi-integration--req3), especially because
it relies on the same metadata (the `META-INF/services/javax.xml.bind.JAXBContext` resources)
in OSGi and non OSGi environments.

Obviously, Axiom could reuse the registry and locator bundles developed by Geronimo. This however would
contradict [Requirement 7](#design-osgi-integration--req7). In addition, for Axiom there is no requirement to
strictly follow the JDK 1.3 service discovery algorithm. Therefore Axiom should reuse the pattern
developed by Geronimo, but not the actual implementation.

## New abstract APIs

Application code rarely uses DOOM as the default Axiom implementation. Several downstream projects
(e.g. the Axis2/Rampart combination) use both the default (LLOM) implementation and DOOM. They select
the implementation based on the particular context. As of Axiom 1.2.12, the only way to create an object
model instance with the DOOM implementation is to use the `DOOMAbstractFactory` API
or to instantiate one of the factory classes (`OMDOMMetaFactory`, `OMDOMFactory`
or one of the subclasses of `DOMSOAPFactory`). All these classes are part of
the `axiom-dom` artifact. This is clearly in contradiction with [Requirement 4](#design-osgi-integration--req4)
and [Requirement 5](#design-osgi-integration--req5).

To overcome this problem the Axiom API must be enhanced to make it possible to select an Axiom
implementation based on capabilities/features requested by the application code. E.g. in the case
of DOOM, the application code would request a factory that implements the DOM API. It is then up
to the Axiom API classes to locate an appropriate implementation, which may be DOOM or another
drop-in replacement, as per [Requirement 5](#design-osgi-integration--req5).

If multiple Axiom implementations are available (on the class path in non OSGi environment or
deployed as bundles in an OSGi environment), then the Axiom API must also be able to select an
appropriate default implementation if no specific feature is requested by the application code.
This can be easily implemented by defining a special feature called “default” that would be
declared by any Axiom implementation that is suitable as a default implementation.

**Note:** DOOM is generally not considered suitable as a default implementation because it doesn't
implement the complete Axiom API (e.g. it doesn't support `OMSourcedElement`).
In addition, in earlier versions of Axiom, the factory classes for DOOM were not stateless
(see [AXIOM-412](https://issues.apache.org/jira/browse/AXIOM-412)).

Finally, to make the selection algorithm deterministic, there should also be a concept
of priority: if multiple Axiom implementations are found for the same feature, then the Axiom API
would select the one with the highest priority.

This leads to the following design:

1. Every Axiom implementation declares a set of features that it supports. A feature is
   simply identified by a string. Two features are predefined by the Axiom API:

   - `default`: indicates that the implementation is a complete
     implementation of the Axiom API and may be used as a default implementation.
   - `dom`: indicates that the implementation supports DOM
     in addition to the Axiom API.

   For every feature it declares, the Axiom implementation specifies a priority,
   which is a positive integer.
2. The relevant Axiom APIs are enhanced so that they take an optional argument
   specifying the feature requested by the application code. If no explicit feature
   is requested, then Axiom will use the `default` feature.
3. To determine the `OMMetaFactory` to be used, Axiom locates
   the implementations declaring the requested feature and selects the one that
   has the highest priority for that feature.

A remaining question is how the implementation declares the feature/priority information.
There are two options:

- Add a method to `OMMetaFactory` that allows the Axiom API
  to query the feature/priority information from the implementation (i.e. the
  features and priorities are hardcoded in the implementation).
- Let the implementation provide this information declaratively in its metadata
  (either in the manifest or in a separate resource with a well defined name).
  Note that in a non OSGi environment, such a metadata resource must be used anyway
  to enable the Axiom API to locate the `OMMetaFactory` implementations.
  Therefore this would be a natural place to declare the features as well.

The second option has the advantage to make it easier for users to debug and tweak
the implementation discovery process (e.g. there may be a need to
customize the features and priorities declared by the different implementations to ensure
that the right implementation is chosen in a particular use case).

This leads to the following design decision:
the features and priorities (together with the class name of the `OMMetaFactory`
implementation) will be defined in an XML descriptor with resource name `META-INF/axiom.xml`.
The format of that descriptor must take into account that a single JAR may contain several
Axiom implementations (e.g. if the JAR is an uber-JAR repackaged from the standard Axiom JARs).

## Common implementation classes

Obviously the LLOM and DOOM implementations share some amount of common code. Historically, implementation classes reusable between LLOM and DOOM were placed in `axiom-api`.
This however tends to blur the distinction between the public API and implementation classes.
Starting with Axiom 1.2.13 such classes are placed into a separate module called
`axiom-common-impl`. However, `axiom-common-impl` cannot simply
be a dependency of `axiom-impl` and `axiom-dom`.
The reason is that in an OSGi environment, the `axiom-common-impl` bundle
would have to export these shared classes, which is in contradiction with [Requirement 4](#design-osgi-integration--req4).
Therefore the code from `axiom-common-impl` needs to be packaged into
`axiom-impl` and `axiom-dom` by the build process so that
the `axiom-common-impl` artifact is not required at runtime.
[Requirement 1](#design-osgi-integration--req1) forbids using embedded JARs to achieve this.
Instead `maven-shade-plugin` is used to include the classes
from `axiom-common-impl` into `axiom-impl` and `axiom-dom`
(and to modify the POMs to remove the dependencies on `axiom-common-impl`).

This raises the question whether `maven-shade-plugin` should be configured to
simply copy the classes or to relocate them (i.e. to change their package names). There are a couple
of arguments in favor of relocating them:

- According to [Requirement 1](#design-osgi-integration--req1), the Axiom artifacts should be
  usable both as normal JARs and as OSGi bundles. Obviously the expectation is that from the
  point of view of application code, they should work in the same in OSGi and non OSGi environments.
  Relocation is required if one wants to strictly satisfy this requirement even if different versions
  of `axiom-impl` and `axiom-dom` are mixed.
  Since the container creates separate class loaders for the `axiom-impl` and `axiom-dom` bundles,
  it is always possible to do that in an OSGi environment: even if the shared classes
  included in `axiom-impl` and `axiom-dom` are
  not relocated, but have the same names, this will not result in conflicts.
  The situation is different in a non OSGi environment where the classes in `axiom-impl`
  and `axiom-dom` are loaded by the same class loader. If the shared classes
  are not relocated, then there may be a conflict if the versions don't match.

  However, in practice it is unlikely that there are valid use case where one would use
  `axiom-impl` and `axiom-dom` artifacts from different Axiom versions.
- Relocation allows to preserve compatibility when duplicate code from
  `axiom-impl` and `axiom-dom` is merged and moved
  to `axiom-common-impl`. The `OMNamespaceImpl`,
  `OMNavigator` and `OMStAXWrapper` classes
  from `axiom-impl` and the `NamespaceImpl`,
  `DOMNavigator` and `DOMStAXWrapper`
  classes from `axiom-dom` that existed in earlier versions of Axiom
  are examples of this. The classes in `axiom-dom` were almost identical
  to the corresponding classes in `axiom-impl`. These classes have been
  merged and moved to `axiom-common-impl`. Relocation then allows them
  to retain their original name (including the original package name) in the
  `axiom-impl` and `axiom-dom` artifacts.

  However, this is only a concern if one wants to preserve compatibility with existing
  code that directly uses these implementation specific classes (which is something that is
  strongly discouraged). One example where this was relevant was the SAAJ implementation
  in Axis2 which used to be very strongly coupled to the DOOM implementation. This however
  has been fixed now.

Using relocation also has some serious disadvantages:

- Stack traces may contain class names that don't match class names in the Axiom source
  code, making debugging harder.
- Axiom now uses JaCoCo to produce code coverage reports. However these reports are
  incomplete if relocation is used. This doesn't affect test cases executed in
  the `axiom-impl` and `axiom-dom` modules
  (because they are executed with the original classes), but tests in separate modules
  (such as integration tests). There are actually two issues:

  - For the relocated classes, JaCoCo is unable to find the corresponding source code.
    This means that the reported code coverage is inaccurate for classes in
    `axiom-common-impl`.
  - Relocation not only modifies the classes in `axiom-common-impl`, but
    also the classes in `axiom-impl` and `axiom-dom`
    that use them. JaCoCo [detects this](https://github.com/jacoco/jacoco/issues/51)
    and excludes the data from the coverage analysis. This means that the
    reported code coverage will also be inaccurate for classes in
    `axiom-impl` and `axiom-dom`.

In Axiom 1.2.14 relocation was used, but this has been changed in Axiom 1.2.15 because the disadvantages
outweigh the advantages.

---

<a id="design-fluent-builder"></a>

<!-- source_url: https://ws.apache.org/axiom/design/fluent-builder.html -->

<!-- page_index: 13 -->

# Fluent builder conventions

Builders are mutable objects which create other (often immutable) objects.
They are used as an alternative to public constructors in order to avoid
constructors with long argument lists and classes with many different constructors.
Builders generally use the fluent pattern so that method calls to the setters
of the builder can be chained.

Axiom uses the following coding conventions for builders:

- A builder type is implemented as a public static final inner class of the class
  to be built. The name of the class is `Builder` and it's constructor must not be public.
- A builder instance is created using a static method named `builder` defined on the
  type being built.
- The builder has a method named `build` that builds the object. This method takes no
  arguments.
- The setter methods on the builder have names that follow the JavaBeans conventions.
  They return `this` so that they can be chained. As a general rule the builder type should not
  have getter methods.
- The built type may also have an instance method called `toBuilder` returning a new
  builder initialized with the property values from the existing instance. This can then
  be used to create a new instance similar to an existing one, and the expectation is that
  `someInstance.toBuilder().build()` would produce an instance that is equal (in the
  relevant sense) to `someInstance`.

  If the build type has a `toBuilder` method, then the builder type may need additional
  methods allowing the caller to unset properties. In certain cases it may also be pertinent
  to add getter methods to support complex state transitions.

---

<a id="articles"></a>

<!-- source_url: https://ws.apache.org/axiom/articles.html -->

<!-- page_index: 14 -->

# Articles about Axiom

- Eran Chinthaka: *[Introducing AXIOM: The Axis Object Model](http://today.java.net/pub/a/today/2005/05/10/axiom.html)*, 10 May 2005.
- Eran Chinthaka: *[Get the most out of XML processing with AXIOM](http://www.ibm.com/developerworks/library/x-axiom/)*, 13 Sep 2005.
- Eran Chinthaka: *[Introducing Axiom](http://www.theserverside.com/news/1365335/Introducing-Axiom)*, 01 Jul 2006.
- Eran Chinthaka: *[AXIOM - Fast and Lightweight Object Model for XML](http://wso2.org/library/291)*, 14 Nov 2006.
- Dennis Sosnoski: *[Java web services: Digging into Axis2: AXIOM](http://www.ibm.com/developerworks/webservices/library/ws-java2/)*, 30 Nov 2006.
- Dapeng Wang: *[Apache Axis2: AXIOM — das neue Objektmodell für XML-Verarbeitung](http://entwickler.de/zonen/portale/psecom,id,101,online,1195.html)*, Jan 2007.
- Matthias Farwick, Michael Hafner: *[XML Parser Benchmarks: Part 2](http://www.xml.com/pub/a/2007/05/16/xml-parser-benchmarks-part-2.html)*, 16 May 2007.
- Deepal Jayasinghe: *[XML Manipulation with Apache AXIOM](http://www.developer.com/xml/article.php/3799851/XML-Manipulation-with-Apache-AXIOM.htm)*, 30 Jan 2009.

---

<a id="faq"></a>

<!-- source_url: https://ws.apache.org/axiom/faq.html -->

<!-- page_index: 15 -->

# Frequently (and less frequently) Asked Questions

1. [I'm using Axiom, but I need to integrate with a library using DOM. What can I do?](#faq--dom)

I'm using Axiom, but I need to integrate with a library using DOM. What can I do?
:   There are currently two solutions:

    1. Axiom separates API and implementation. The default implementation is called
       LLOM (Linked List Object Model) and provided by the `axiom-impl`
       artifact. There is also a second implementation called DOOM (DOM over OM) that
       implements both the Axiom API and DOM. It is provided by the `axiom-dom`
       artifact. You can use this implementation to integrate with DOM based code.
       Note however that the DOM implementation provided by DOOM is not perfect. In
       particular it doesn't implement (all of) DOM 3.
    2. The Axiom API now has
       [`getSAXSource`](https://ws.apache.org/axiom/apidocs/org/apache/axiom/om/OMContainer.html#getSAXSource.28boolean.29) and
       [`getSAXResult`](https://ws.apache.org/axiom/apidocs/org/apache/axiom/om/impl/jaxp/OMResult.html)
       methods that (as their names imply) return instances of JAXP's
       [`SAXSource`](http://docs.oracle.com/javase/7/docs/api/javax/xml/transform/sax/SAXSource.html) and
       [`SAXResult`](http://docs.oracle.com/javase/7/docs/api/javax/xml/transform/sax/SAXResult.html)
       classes. You can use these to transform an Axiom tree into DOM (using
       a standard implementation of DOM) and vice-versa. Note that since they use the SAX API,
       you will loose the deferred parsing capabilities of Axiom, but in many cases this will be
       acceptable.

---

<a id="implementations"></a>

<!-- source_url: https://ws.apache.org/axiom/implementations/index.html -->

<!-- page_index: 16 -->

# About Implementations

Object model implementations built using Axiom

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [LLOM](https://ws.apache.org/axiom/implementations/axiom-impl/index.html) | The default implementation of the Axiom API. |
| [DOOM](https://ws.apache.org/axiom/implementations/axiom-dom/index.html) | An implementation of the Axiom API that also implements DOM. |

---

<a id="axiom-compat"></a>

<!-- source_url: https://ws.apache.org/axiom/axiom-compat/index.html -->

<!-- page_index: 17 -->

# Introduction

`axiom-compat` contains deprecated classes that will be removed in a future Axiom
version. Add this module as a dependencies to projects with legacy code.

---

<a id="testing-xml-truth"></a>

<!-- source_url: https://ws.apache.org/axiom/testing/xml-truth/index.html -->

<!-- page_index: 18 -->

# Introduction

This `xml-truth` module provides a [Google Truth](https://github.com/google/truth) extension to
compare XML data. It can be used as an alternative to [XMLUnit](http://www.xmlunit.org/). The basic
usage is as follows:

```
assertAbout(xml()).that(actual).hasSameContentAs(expected);
```

This relies on the following static imports being present:

```
import static com.google.common.truth.Truth.assertAbout;
import static org.apache.axiom.truth.xml.XMLTruth.xml;
```

`actual` and `expected` are objects that represent XML data. The following types are currently
supported:

- `InputStream`, `Reader`, `String` and `byte[]` with XML data to be parsed
- `javax.xml.transform.stream.StreamSource` and `org.xml.sax.InputSource`
- DOM `Document` or `Element` nodes
- `java.net.URL`
- `javax.xml.stream.XMLStreamReader`

By default, comparison is strict. E.g. the following assertion would fail:

```
assertAbout(xml()).that("<p:a xmlns:p='urn:ns'/>").hasSameContentAs("<a xmlns='urn:ns'/>");
```

To control how the comparison is performed, use the relevant methods on the
[`XMLSubject`](https://ws.apache.org/axiom/testing/xml-truth/apidocs/org/apache/axiom/truth/xml/XMLSubject.html) object returned by `that()`:

```
assertAbout(xml())
        .that("<p:a xmlns:p='urn:ns'/>")
        .ignoringNamespacePrefixes()
        .ignoringNamespaceDeclarations()
        .hasSameContentAs("<a xmlns='urn:ns'/>");
```

---

<a id="testing"></a>

<!-- source_url: https://ws.apache.org/axiom/testing/index.html -->

<!-- page_index: 19 -->

# Testing

---
