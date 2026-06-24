# Table of Contents

## Navigation

- [Introduction](#docs-contents)
- [Installation Guide](#docs-installationguide)
- [Add-on Modules](#modules)
- [Application Server Specific Configuration Guide](#docs-app_server)
- [Quick Start Guide](#docs-quickstartguide)
- [User's Guide](#docs-userguide)
- [Advanced User's Guide](#docs-adv-userguide)
- [Configuration Guide](#docs-axis2config)
- [Web Administrator's Guide](#docs-webadminguide)
- [Architecture Guide](#docs-axis2architectureguide)
- [JAXWS Guide](#docs-jaxws-guide)
- [POJO Guide](#docs-pojoguide)
- [Spring Guide](#docs-spring)
- [ModulesGuide](#docs-modules)
- [Clustering Guide](#docs-clustering-guide)
- ADB Data Binding
  - [14.1](#docs-adb-adb-howto)
  - [14.2](#docs-adb-adb-advanced)
  - [14.3](#docs-adb-adb-codegen-integration)
  - [14.4](#docs-adb-adb-tweaking)
- JiBX Data Binding
  - [15.1](#docs-jibx-jibx-codegen-integration)
  - [15.2](#docs-jibx-jibx-doclit-example)
  - [15.3](#docs-jibx-jibx-unwrapped-example)
- Advanced
  - [16.1](#docs-xmlbased-server)
  - [16.2](#docs-dii)
- [Attachments/MTOM Guide](#docs-mtom-guide)
- Transports
  - [18.1](#docs-http-transport)
  - [18.2](#docs-servlet-transport)
  - [18.3](#docs-jms-transport)
  - [18.4](#docs-tcp-transport)
  - [18.5](#docs-mail-transport)
  - [18.6](#docs-udp-transport)
  - [18.7](#docs-xmpp-transport)
  - [18.8](#docs-transport_howto)
- [WS-Policy Support](#docs-ws_policy)
- [REST Support](#docs-rest-ws)
- JSON support
  - [23.1](#docs-json_support)
  - [23.2](#docs-json_support_gson)
    - [Native Approach](#docs-json_support_gson)
    - [XML Stream API Base Approach](#docs-json_support_gson)
    - [User Guide](#docs-json_gson_user_guide)
    - [JSON and REST with Spring Boot User's Guide](#docs-json-springboot-userguide)
- [Exposing CORBA Services as Web Services](#docs-corba-deployer)
- [Guide to using EJB Provider in Axis2](#docs-ejb-provider)
- [SOAP Monitor](#docs-soapmonitor-module)
- [Command Line Tools](#docs-reference)
- [Tools/Plug-ins](#tools)
  - [25.1](#tools-codegentoolreference)
  - [25.2](#tools-idea-idea_plug-in_userguide)
  - [25.3](#tools-eclipse-servicearchiver-plugin)
  - [25.4](#tools-eclipse-wsdl2java-plugin)
  - [25.5](#tools-maven-plugins-maven-aar-plugin)
  - [25.6](#tools-maven-plugins-maven-java2wsdl-plugin)
  - [25.7](#tools-maven-plugins-axis2-wsdl2code-maven-plugin)
- [Migration Guide (from Axis1)](#docs-migration)
- Design Notes
  - [27.1](#docs-axis2-rpc-support)
- Axis2/Java
  - [Home](#index)
  - [Downloads](#download)
  - Release Notes
    - [1.6.1](https://axis.apache.org/axis2/java/core/release-notes/1.6.1.html)
    - [1.6.2](https://axis.apache.org/axis2/java/core/release-notes/1.6.2.html)
    - [1.6.3](https://axis.apache.org/axis2/java/core/release-notes/1.6.3.html)
    - [1.6.4](https://axis.apache.org/axis2/java/core/release-notes/1.6.4.html)
    - [1.7.0](https://axis.apache.org/axis2/java/core/release-notes/1.7.0.html)
    - [1.7.1](https://axis.apache.org/axis2/java/core/release-notes/1.7.1.html)
    - [1.7.2](https://axis.apache.org/axis2/java/core/release-notes/1.7.2.html)
    - [1.7.3](https://axis.apache.org/axis2/java/core/release-notes/1.7.3.html)
    - [1.7.4](https://axis.apache.org/axis2/java/core/release-notes/1.7.4.html)
    - [1.7.5](https://axis.apache.org/axis2/java/core/release-notes/1.7.5.html)
    - [1.7.6](https://axis.apache.org/axis2/java/core/release-notes/1.7.6.html)
    - [1.7.7](https://axis.apache.org/axis2/java/core/release-notes/1.7.7.html)
    - [1.7.8](https://axis.apache.org/axis2/java/core/release-notes/1.7.8.html)
    - [1.7.9](https://axis.apache.org/axis2/java/core/release-notes/1.7.9.html)
    - [1.8.0](https://axis.apache.org/axis2/java/core/release-notes/1.8.0.html)
    - [1.8.1](https://axis.apache.org/axis2/java/core/release-notes/1.8.1.html)
    - [1.8.2](https://axis.apache.org/axis2/java/core/release-notes/1.8.2.html)
    - [2.0.0](https://axis.apache.org/axis2/java/core/release-notes/2.0.0.html)
  - [Modules](#modules)
  - [Tools](#tools)
- Documentation
  - [Table of Contents](#docs-toc)
  - [Installation Guide](#docs-installationguide)
  - [QuickStart Guide](#docs-quickstartguide)
  - [User Guide](#docs-userguide)
  - [JAXWS Guide](#docs-jaxws-guide)
  - [POJO Guide](#docs-pojoguide)
  - [Spring Guide](#docs-spring)
  - [Web Administrator's Guide](#docs-webadminguide)
  - [Migration Guide (from Axis1)](#docs-migration)
- Resources
  - [FAQ](#faq)
  - [Articles](#articles)
  - [Wiki](http://wiki.apache.org/ws/FrontPage/Axis2/)
  - [Reference Library](#reflib)
  - [Online Java Docs](https://axis.apache.org/axis2/java/core/apidocs/index.html)
- Get Involved
  - [Overview](#overview)
  - [Checkout the Source](#git)
  - [Mailing Lists](#mail-lists)
  - [Release Process](#release-process)
  - [Developer Guidelines](#guidelines)
  - [Build the Site](#sitehowto)
- Project Information
  - [Project Team](#team-list)
  - [Issue Tracking](#issue-tracking)
  - [Source Code](https://github.com/apache/axis-axis2-java-core)
  - [Acknowledgements](#thanks)
- Apache
  - [License](http://www.apache.org/licenses/LICENSE-2.0.html)
  - [Sponsorship](http://www.apache.org/foundation/sponsorship.html)
  - [Thanks](http://www.apache.org/foundation/thanks.html)
  - [Security](http://www.apache.org/security/)
- Overview
  - [About](#tools-maven-plugins-axis2-wsdl2code-maven-plugin)
  - [Usage](#tools-maven-plugins-axis2-wsdl2code-maven-plugin-usage)
  - [Plugin Documentation](#tools-maven-plugins-axis2-wsdl2code-maven-plugin-plugin-info)
    - [wsdl2code](#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo)

## Content

<a id="docs-contents"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/contents.html -->

<!-- page_index: 1 -->

# Apache Axis2/Java Version 2.0.0 Documentation Index

## Introduction

Apache Axis2, the third generation Web services engine is more
efficient, more modular and more XML-oriented than its predecessor
[Apache Axis](http://ws.apache.org/axis/). It is
carefully designed to support the easy addition of plug-in modules
that extend its functionality for features such as security and
increased reliability.

Apache Axis2 Version 2.0.0 is a bugfix release, fixing several
problems in version 1.5. Please see the release notes for more
details.

This page describes our list of available documents.

## Apache Axis2 User's Guide

You can get started with Axis2 with the assistance of the
following documents. They will guide you through the Axis2
download, installation (both as a standalone Web services engine
and as part of a J2EE compliant servlet container), and
instructions on how to write Web services and Web services client
using Apache Axis2.

- [Introduction](#docs-userguide--intro)- Gives you an
  introduction to what Axis2 is, the life cycle of a Web services
  message, how Axis2 handles SOAP messages and also includes a basic
  description on Axis2 distributions, and how Axis2 behaves as part
  of a Web application or as a standalone client that is not part of
  a J2EE application.
- [Download and Installation](#docs-installationguide)-
  Lists the different distribution packages offered by Axis2 and
  gives in-depth instructions on the installation of the standalone
  method and as part of a J2EE servlet container.
- [Testing Client
  Code](https://axis.apache.org/axis2/java/core/docs/userguide-installingtesting.html) - The best way to make sure that your system is running
  Axis2 is to install and test both a service and a client. This
  document describes this process in easy to understand steps.
- [Introduction to
  Services](https://axis.apache.org/axis2/java/core/docs/userguide-introtoservices.html) - The term "Web services" can apply to a number of
  different ways of sending information back and forth. However, this
  guide focuses on the sending and receiving of SOAP messages and
  Message Exchange Patterns (MEPs).
- [Creating Clients from
  WSDL](https://axis.apache.org/axis2/java/core/docs/userguide-creatingclients.html) - When it comes to creating a Web service client, you can
  do it manually as described in the next document. However, in most
  cases, you will have a Web Service Description Language (WSDL)
  definition that describes the messages that clients should send and
  expect to receive. Axis2 provides several ways to use this
  definition to automatically generate a client. This document
  explains how to create a client using WSDL definitions.
- [Building Services
  from Scratch](https://axis.apache.org/axis2/java/core/docs/userguide-buildingservices.html) - Now that you know how to use Axis2 to generate
  clients from WSDL as described in the document before, this
  document digs a little deeper, showing you how to create services,
  and how to create both services and clients "from scratch", so to
  speak.
- [Samples](https://axis.apache.org/axis2/java/core/docs/userguide-samples.html) - The Axis2
  Standard Distribution provides a number of samples you can use as a
  guide for implementing specific features and capabilities. These
  services are listed in this document along with basic introductions
  for each one.
- [For Further Study](https://axis.apache.org/axis2/java/core/docs/userguide-forfurtherstudy.html)
  - This section lists resource documents for further study.
  - [POJO Web Services using Apache
    Axis2](#docs-pojoguide)-This guide will show you how to create a Plain Old Java
    Object (POJO) for deploying using Apache Axis2 on Apache Tomcat.
    POJOs are fast to build and easy to maintain, which means you'll
    save a lot of time building and debugging your code
  - [Axis2 Quick Start Guide](#docs-quickstartguide)-The
    purpose of this guide is to get you started on creating services
    and clients using Axis2 as quickly as possible. It demonstrates how
    to create Web services using a variety of different
    technologies.</>

Also see our [FAQ page](#faq) to answer those
common questions in mind.

## How To

This section deals with more advanced topics including Axis2
support features such as Transports, Attachments, Pluggable Data
Binding, Security, and REST Web services in detail.

- [Web Administrator's Guide](#docs-webadminguide) -
  Detailed instructions on the administration console of Axis2 Web
  application, which provides run-time configuration of Axis2.
- [Migrating from Axis 1.x to Axis 2](#docs-migration)
  - Guiding Axis 1.x users in upgrading to Axis2
- [Application Server Specific
  Configuration Guide](#docs-app_server) - Provides extra configuration information
  required for application servers to run Axis2 to its fullest
  potential
- [Axiom User Guide](http://ws.apache.org/axiom/userguide/userguide.html) -
  An introduction to Axis2's Object Model
- [REST Support](#docs-rest-ws)-Introduction on
  Representational State Transfer
- [Axis2 RPC Support](#docs-axis2-rpc-support) - This
  document talks about the Axis2's Remote Procedure Calls support in
  a set of easy to understand implementation steps
- [MTOM Guide -Sending Binary Data with
  SOAP](#docs-mtom-guide) - Explains how to send binary data using the SOAP Message
  Transmission Optimization Mechanism
- [Axis2 Configuration Guide](#docs-axis2config) -
  Explains the three configurations in Axis2: global, service, and
  module
- [SOAP Monitor How-to](#docs-soapmonitor-module) - A
  guide on the utilities used to monitor the SOAP messages that
  invoke Web services, along with the results of those messages
- [Web Services Policy Support In
  Axis2](#docs-ws_policy) - Introduction to the role of Web services policy in
  Axis2
- [Spring Framework](#docs-spring) - A guide on how to
  use Axis2 with the Spring Framework
- [JSON Support](#docs-json_support) - This document
  explains how to use JSON support implementation in Axis2. Includes
  details on test cases and samples
- [Exposing CORBA Services as Web Services](#docs-corba-deployer) - This guide explains how to expose a CORBA Services as a Web Services in Axis2
  using an example
- [Guide to using EJB Provider in
  Axis2](#docs-ejb-provider) - This guide explains how to use an EJB provider in Axis2
  using an example
- [Clustering Guide](#docs-clustering-guide) - This guide will show how you can leverage clustering support to improve Scalability, Failover and High Availability of your Web Services

**Data Bindings:**

- [ADB How-to](#docs-adb-adb-howto) - A guide on the
  Axis2 Databinding Framework (ADB)
- [Advanced ADB Framework
  Features](#docs-adb-adb-advanced) - Provides an insight into the newly added advanced
  features of ADB
- [Tweaking the ADB Code
  Generator](#docs-adb-adb-tweaking) - Explains the available mechanisms to extend
  ADB
- [ADB Integration with
  Axis2](#docs-adb-adb-codegen-integration) - A guide to writing an extension using the integrator in
  order to integrate ADB with Axis2
- [JiBX Integration
  With Axis2](#docs-jibx-jibx-codegen-integration) - A guide to using JiBX with Axis2 in order to
  expose existing Java code as a Web service and to implement a
  client for an existing Web service

**Transports:**

- [HTTP Transports](#docs-http-transport) - A description on HTTP sender and HTTP
  receiver in Axis2
- [Write Your Own Axis2
  Transport](#docs-transport_howto) - A quick and easy guide to create your own Axis2
  Transport protocol

**Axis2 Tools:**

- [Code
  Generator Tool Guide for Command Line and Ant Tasks](#tools-codegentoolreference) - Lists
  command line and Ant task references. How to build a file using
  custom Ant tasks and how to invoke a Code Generator from Ant
- [Code
  Generator Wizard Guide for Eclipse Plug-in](#tools-eclipse-wsdl2java-plugin) - Explains the usage
  of the code generator Eclipse plug-in for WSDL2Java and/or
  Java2WSDL operations
- [Service
  Archive Generator Wizard Guide for Eclipse Plug-in](#tools-eclipse-servicearchiver-plugin) - Describes
  the functionality of the Eclipse plugin service archive generator
  tool
- [Code
  Generator Wizard Guide for IntelliJ IDEA Plug-in](#tools-idea-idea_plug-in_userguide) - A guide on
  the usage of the IDEA code generation plug-in to create service
  archives and generate Java class files from WSDL files
- [Maven2
  AAR Plug-in Guide](#tools-maven-plugins-maven-aar-plugin) - A guide to generate an Axis 2 service file
  (AAR file) using the Maven plug-in.
- [Maven2 Java2WSDL Plug-in Guide](#tools-maven-plugins-maven-java2wsdl-plugin) - A guide to using Java2WSDL
  Maven 2 Plug-in that takes a Java class as input and generates a
  WSDL, which describes a Web service for invoking the class
  methods
- [Maven2 WSDL2Code Plug-in Guide](#tools-maven-plugins-axis2-wsdl2code-maven-plugin) - A guide to using this plugin
  that takes as input a WSDL and generates client and server stubs
  for calling or implementing a Web service matching the WSDL.

## Apache Axis2 Developers

- [Advanced User's Guide](#docs-adv-userguide) - A
  quick start user's guide for more experienced users and developers
  on how to install, create Web services and Web service clients
  using Axis2.
  - [Introduction](#docs-adv-userguide--introduction) -
    Outlines the overall direction of the user guide, with a high level
    introduction on Axis2
  - [Download and Installation](#docs-installationguide)
    - Lists the different distribution packages offered by Axis2, and
    the installations for the standalone and as part of a J2EE servlet
    container methods.
  - [Creating a new Web
    Service with Code Generation](#docs-adv-userguide--ws_codegen) - Axis2 provides two ways to
    create new Web Services: using code generation and XML based
    primary APIs. This section explains how to start from a WSDL, and
    create a new Service with code generation
  - [Writing Web Services Using
    Axis2's Primary APIs](#docs-xmlbased-server) - Explains how to create new Web Services
    using XML based primary APIs
  - [Writing a Web Service
    Client with Code Generation](#docs-adv-userguide--client) - Axis2 also provides a more
    complex, yet powerful XML based client API that is intended for
    advanced users. However, if you are a new user we recommend using
    the code generation approach presented below
  - [Writing Web Service Clients Using Axis2's
    Primary APIs](#docs-dii) - This section presents complex yet powerful XML
    based client APIs, which is intended for advanced users to write
    Web services clients
  - [Configuring Axis2](#docs-adv-userguide--config) -
    Axis2 configuration is based on a repository and standard archive
    formats. Here you will find details on how to configure Axis2. You
    will also find reference documents that lead to greater detail in
    this area.
- [Axis2 Architecture
  Guide](#docs-axis2architectureguide) - Introduction to Axis2's modular architecture
- [Online
  Java Docs](https://axis.apache.org/axis2/java/core/api/index.html) - Java API documentation
- [Reference Library](#reflib) - This document
  provides additional information to developers on WS-\*
  specifications, Java language specifications, Subversion (SVN)
  control etc.

## References

Gives you a list of published articles, tutorials and
Questions-Answers on Apache Axis2. [Check
them out](#articles) for that extra knowledge on the next generation Web
services engine Apache Axis2. Be informed and up-to-date!

---

<a id="docs-installationguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/installationguide.html -->

<!-- page_index: 2 -->

# Apache Axis2 Installation Guide

This document provides information on Axis2 distribution
packages, system prerequisites and setting up environment variables
and tools followed by detailed instructions on installation
methods.

*Send your feedback to: [java-dev@axis.apache.org](mailto:java-dev@axis.apache.org?subject=[Axis2])*
mailing list. (Subscription details are available on [Axis2 site](#mail-lists).)
Kindly prefix every email subject with [Axis2].

## Contents

- [Axis2 Distributions](#docs-installationguide--download_axis2)
- [System Requirements](#docs-installationguide--requirements)
- [Installing Axis2 as a Standalone Server
  using the Standard Binary Distribution](#docs-installationguide--standalone)
  - [Installing the Apache Axis2 Binary
    Distribution](#docs-installationguide--standalone1)
  - [Starting up Axis2 Standalone
    Server](#docs-installationguide--standalone2)
  - [Building the Axis2 WAR File Using the
    Standard Binary Distribution](#docs-installationguide--standalone3)
  - [Getting Familiar with Convenient Axis2
    Scripts](#docs-installationguide--standalone4)
- [Installing Axis2 in a Servlet
  Container](#docs-installationguide--servlet_container)
- [Uploading Services](#docs-installationguide--upload)
- [Advanced](#docs-installationguide--advanced)
  - [Axis2 Source Distribution](#docs-installationguide--source)
    - [Setting up the Environment and
      Tools](#docs-installationguide--_toc96698083)
    - [Building Axis2 Binaries and the WAR
      file Using the Source Distribution](#docs-installationguide--_toc96698085)

## Axis2 Distributions

Axis2 is distributed in several convenient distribution packages
and can be installed either as a standalone server or as part of a
J2EE compliant servlet container. Axis2 is distributed under the
Apache License, version 2.0. This Installation Guide will mainly
focus on running Apache Axis2 using the Standard Binary
Distribution.

[Download](https://axis.apache.org/axis2/java/core/download.cgi) distribution packages of the Apache Axis2
2.0.0 version (latest).

[Download](https://axis.apache.org/axis2/java/core/download.cgi)
distribution packages of all versions of Apache Axis2.

The distribution packages provided are as follows:

### 1. Standard Binary Distribution

This is the complete version of Axis2 and includes samples and
convenient scripts as well.

[Download](https://axis.apache.org/axis2/java/core/download.cgi) Standard Binary Distribution

### 2. WAR (Web Archive) Distribution

This is the Web application of Axis2, which can be deployed in
most of the servlet containers.

[Download](https://axis.apache.org/axis2/java/core/download.cgi) WAR (Web Archive) Distribution

### 3. Documents Distribution

This contains all the documentation in one package. The package
includes the xdocs and the Java API docs of this project.

[Download](https://axis.apache.org/axis2/java/core/download.cgi) Documents Distribution

### 4. Source Distribution

This contains the sources of Axis2 standard distribution, and is
mainly for the benefit of advanced users. One can generate a binary
distribution using the source by typing $mvn
-Drelease install. You need to set up the Axis2 environment before
running this command. Step by step details on how to create the
binary distribution is available in the [Advanced](#docs-installationguide--advanced) section.

[Download](https://axis.apache.org/axis2/java/core/download.cgi) Source Distribution

## System Requirements

|  |  |
| --- | --- |
| Java Development Kit (JDK) | 1.8 or later (For instructions on setting up the JDK in different operating systems, visit [http://java.sun.com](http://java.sun.com/)) |
| Disk | Approximately 35 MB separately for standard binary distribution |
| Operating system | Tested on Windows, Mac OS X, Ubuntu(Linux) |
| **Build Tool**-[Apache Ant](http://ant.apache.org/) To run samples and to build WAR files from Axis2 binary distribution. | Version 1.10 or higher ([download](http://ant.apache.org/bindownload.cgi)). |
| **Build Tool**- [Apache Maven 2.x](http://maven.apache.org/) Required *only* for building Axis2 from Source Distribution | 3.6.3 or higher in Maven 3.x series ([download](http://maven.apache.org/download.html)). **Please download Maven 3.x version. Axis2 does not support Maven 1.x nor 2.x anymore.** |

Make sure that the above prerequisites are available for the
Axis2 installation.

## Installing Axis2 as a Standalone Server using the Standard Binary Distribution

This section provides you with the following information

1. Install Axis2 as a standalone server using the Standard Binary
   Distribution
2. Start up the Axis2 standalone server
3. Building the axis2.war file (using the Standard Binary
   Distribution) which is required to run Axis2 as part of a J2EE
   compliant servlet container
4. Running Axis2 convenient scripts

### 1. Download and Install the Apache Axis2 Binary Distribution

[Download](http://java.sun.com/j2se/) and install a
Java Development Kit (JDK) release (version 1.8 or later). Install
the JDK according to the instructions included with the release.
Set an environment variable JAVA\_HOME to the pathname of the
directory into which you installed the JDK release.

Download and unpack the [Axis2 Standard Binary Distribution](https://axis.apache.org/axis2/java/core/download.cgi) into a convenient location
so that the distribution resides in its own directory. Set an
environment variable AXIS2\_HOME to the pathname of the extracted
directory of Axis2 (Eg: /opt/axis2-2.0.0). Linux users
can alternatively run the setenv.sh file available in the
AXIS2\_HOME/bin directory to set the AXIS2\_HOME environment variable
to the Axis2 classpath.

### 2. Starting up Axis2 Standalone Server

The standalone Axis2 server can be started by executing the
following commands:
%AXIS2\_HOME%\bin\axis2server.bat (Windows)
$AXIS2\_HOME/bin/axis2server.sh (Unix)

After startup, the default web services included with Axis2 will
be available by visiting http://localhost:8080/axis2/services/

### 3. Building the Axis2 Web Application (axis2.war) Using Standard Binary Distribution

[Download](http://ant.apache.org/bindownload.cgi) and
install Apache Ant (version 1.10 or later). Install Apache Ant
according to the instructions included with the Ant release.

Locate the Ant build file (build.xml) inside the webapp
directory, which resides in your Axis2 home directory (i.e:-
$AXIS\_HOME/webapp)". Run the Ant build by executing "ant
create.war" inside the AXIS2\_HOME/webapps folder. You can find the
generated axis2.war inside the AXIS2\_HOME/dist directory. All the
services and modules that are present in the AXIS2\_HOME/repository
will be packed into the created axis2.war together with the Axis2
configuration found at AXIS2\_HOME/conf/axis2.xml.

Read [Installing Axis2 in a Servlet
Container](#docs-installationguide--servlet_container) to find out how to deploy the Axis2 Web application
in a servlet container.

### 4. Getting Familiar with the Convenient Axis2 Scripts

It is advised to add the AXIS2\_HOME/bin to the PATH, so that
you'll be able to run the following scripts from anywhere.

|  |  |
| --- | --- |
| **Script Name** | **Description** |
| axis2.{bat|sh} | You can use this script to run web service clients written using Axis2. This script calls the "java" command after adding the classpath for Axis2 dependent libraries (\*.jar files present in your AXIS2\_HOME/lib), setting the Axis2 repository location (AXIS2\_HOME/repository) and setting the Axis2 configuration file location(AXIS2\_HOME/conf/axis2.xml) for you. With this you can be relieved from setting all the above Axis2 specific parameters. *Usage : axis2.{sh.bat} [-options] class [args...]* |
| axis2server.{sh|bat} | This script will start a standalone Axis2 server using the AXIS2\_HOME/repository as the Axis2 repository and the AXIS2\_HOME/conf/axis2.xml as the Axis2 configuration file. This will start all the transport listeners listed in the AXIS2\_HOME/conf/axis2.xml. For example, if you want to deploy a service using a standalone Axis2 server,then copy your service archive to the AXIS2\_HOME/repository/services directory. Next, go to the "Transport Ins" section of the AXIS2\_HOME/conf/axis2.xml and configure the transport receivers (simpleHttpServer in port 8080 is listed by default). Then invoke this script.  The server can be started in debug mode by adding the `-xdebug` option to the command line. A remote debugger can then be attached by connecting to port 8000. |
| wsdl2java.{bat|sh} | This script generates Java code according to a given WSDL file to handle Web service invocations (client-side stubs). This script also has the ability to generate web service skeletons according to the given WSDL. *Usage: wsdl2java.{sh|bat} [OPTION]... -uri <Location of WSDL>*  e.g., wsdl2java.sh -uri ../wsdl/Axis2Sample.wsdl  A more detailed reference about this script can be found [here](#docs-reference) |
| java2wsdl.{bat|sh} | This script generates the appropriate WSDL file for a given Java class. *Usage: Java2WSDL.{sh|bat} [OPTION]... -cn <fully qualified class name>*  e.g., Java2WSDL.sh -cn ../samples/test/searchTool.Search  A more detailed reference about this script can be found [here](#docs-reference) |

## Installing Axis2 in a Servlet Container

Whichever the distribution, installing Axis2 in a J2EE compliant
servlet container is as follows:

1. Build the Axis2 WAR file using the Axis2 [Standard Binary Distribution](#docs-installationguide--standalone3). (Alternatively you
   can [download](https://axis.apache.org/axis2/java/core/download.cgi) the axis2.war file or you can build axis2.war using
   the [Source Distribution](#docs-installationguide--war).
2. Drop the WAR file in the webapps folder of the servlet
   container. Most servlet containers will automatically install the
   WAR file. (Some servlet containers may require a restart in order
   to capture the new web application. Refer to your servlet container
   documentation for more information.)
3. Once the WAR is successfully installed, test it by pointing the
   web browser to the **http://<host
   :port>/axis2.** It should produce the following page
   which is the **Axis2 Web Application Home Page**.
   ![](assets/images/clip-image006_c10a6267117859bb.jpg)
4. Use the link "Validate" to ensure that everything is running
   correctly. If the validation fails then the WAR has failed to
   install properly or some essential jars are missing. In such a
   situation, refer to the documentation of the particular servlet
   container to find the problem. The following page shows a
   successful validation. Note the statement that indicates the core
   Axis2 libraries are present.
   ![](assets/images/happyaxis_9d43dfed54925c97.jpg)

**Note:** For any Application server specific
installation information please refer to the [Application Server Specific Configuration
Guide](#docs-app_server).

## Uploading Services

The Axis2 Web application also provides an interface to upload
services. Once a service archive file is created according to the
service specification as described in the Advanced User's Guide, that .aar file can
be uploaded using the upload page.

**![](assets/images/clip-image010_33e6bbf8fc6f0a24.jpg)**

The uploaded .aar files will be stored in the default service
directory. For Axis2, this will be the
<webapps>/axis2/WEB-INF/services directory. Once a service is
uploaded, it will be installed instantly.

Since Axis2 supports **hot deployment**, you can
drop the service archive directly through the file system to the
above mentioned services directory. It will also cause the service
to be automatically installed without the container being
restarted.

Use the 'Services' link on the Web Application home page to
check the successful installation of a service. The services and
the operations of successfully installed services will be displayed
on the available services page.

![](assets/images/clip-image012_86447e39366c058e.jpg)

If the service has deployment time errors it will list those
services as faulty services. If you click on the link, you will see
the deployment fault error messages.

![](assets/images/faultservice_ab20d718f4982b1e.jpg)

Deployment time error message

**![](assets/images/faultmsg_40ebbe419f0212b3.jpg)**

Axis2 Administration is all about configuring Axis2 at the run
time and the configuration will be transient. More descriptions are
available in the [Axis2
Web Administration Guide](#docs-webadminguide)

## Advanced

## Axis2 Source Distribution

 By using the Source Distribution, both
binary files (which can be downloaded as the [Standard Binary Distribution](#docs-installationguide--std-bin)) and the axis2.war file
(which can be downloaded as the [WAR
distribution](#docs-installationguide--war1)) can be built using Maven commands.

Required jar files do not come with the distribution and they
will also have to be built by running the maven command. Before we
go any further, it is necessary to install [Maven3](http://maven.apache.org/) and
set up its environment, as explained below.

### Setting Up the Environment and Tools

#### Maven

The Axis2 build is based on [Maven3](http://maven.apache.org/) .
Hence the only prerequisite to build Axis2 from the source
distribution is to have Maven installed. Extensive instruction
guides are available at the Maven site. This guide however contains
the easiest path for quick environment setting. Advanced users who
wish to know more about Maven can visit [this site.](http://maven.apache.org/users/index.html)

- MS Windows

1. Download and run the Windows installer package for Maven.
2. Set the 'Environment Variables' ( create system variable
   MAVEN\_HOME and edit path. eg: "C:\Program Files\Apache Software
   Foundation\maven-2.0.7"; path %MAVEN\_HOME%\bin)
3. Make sure that the system variable JAVA\_HOME is set to the
   location of your JDK, eg. C:\Program Files\Java\jdk1.5.0\_11
4. Run mvn -v or mvn -version to verify that it is correctly
   installed.

![clip_image002 (15K)](assets/images/clip-image002_43ffdce679ce48d6.jpg)

- Unix based OS (Linux etc)

The tar ball or the zip archive is the best option. Once the
archive is downloaded expand it to a directory of choice and set
the environment variable MAVEN\_HOME and add MAVEN\_HOME/bin to the
path as well. [More
instructions](http://maven.apache.org/download.html) for installing Maven in Unix based operating
systems.

Once Maven is properly installed, you can start building
Axis2.

[Maven commands that are frequently
used](#faq--d4) in Axis2 are listed on the [FAQs](#faq)
page.

### Building Binaries and the WAR File Using the Source Distribution

The Source Distribution is available as a zipped archive. All
the necessary build scripts are included with the source
distribution. Once the source archive is expanded into a directory
of choice, moving to the particular directory and running
`mvn install` command will build the Axis2 jar file.

Once the command completes, the binaries (jar files in this
case) can be found at a newly created "target" directory.

**Note: For the first Maven build (if the maven repository
is not built first) it will take a while since the required jars
need to be downloaded. However, this is a once only process and
will not affect any successive builds.**

The default maven build will generate the war under modules/webapp/target directory

---

<a id="modules"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/modules/index.html -->

<!-- page_index: 3 -->

# Apache Axis2 Modules

Axis2 architecture is flexible enough to extend its
functionalities using modules. This page is maintained to keep
track of the relevant modules that are developed on top of
Axis2.

| Name | Description | Where to get it |
| --- | --- | --- |
| [Addressing](https://axis.apache.org/axis2/java/core/modules/addressing/index.html) | This is an implementation of WS-Addressing submission version (2004-08) and WS-Addressing 2005-08 versions. | Bundled with the [Standard Binary Distribution](#download). |
| [SOAP Monitor](#docs-soapmonitor-module) | SOAP Monitor utility provides a way for Web services developers to monitor the SOAP messages being sent/received without requiring any special configuration or restarting of the server | Bundled with the [Standard Binary Distribution](#download). |
| [Rampart](http://ws.apache.org/rampart/) | The WS-Security and WS-SecureConversation implementation for axis2. Now with a new configuration model based on WS-SecurityPolicy | <http://axis.apache.org/axis2/java/rampart/> |

---

<a id="docs-app_server"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/app_server.html -->

<!-- page_index: 4 -->

# Application Server Specific Configuration Guide

This document provides configuration information required for
your Application Server to run Apache Axis2 to its fullest
potential.

# WebLogic

## Use exploded configuration to deploy Axis2 WAR

We recommend using the exploded configuration to deploy Axis2
WAR in WebLogic application server to support the
hotupdate/ hotdeployment features in Axis2. However, if you want to
deploy custom WARs, say in a clustering environment, you need to
add two additional files into the WEB-INF named "services.list" and
"modules.list" under the modules and services directory
respectively.

- **WEB-INF/services/services.list** : should list all the
  services (aar files) that you want to expose.
- **WEB-INF/modules/modules.list** : should list all the
  modules (mar files) that you want to use.

NOTE: In both cases, please list one entry per line.

WebLogic ships with JARs that conflict with JARs present in
Axis2. Therefore use <prefer-web-inf-classes> to ensure that
JARs packaged in Axis2 WAR are picked up from WEB-INF/lib. You can
do this by setting the <prefer-web-inf-classes> element in
WEB-INF/weblogic.xml to true. An example of weblogic.xml is shown
below:

```

<weblogic-web-app>
 <container-descriptor>
    <prefer-web-inf-classes>true</prefer-web-inf-classes>
  </container-descriptor>
</weblogic-web-app>
```

If set to true, the <prefer-web-inf-classes> element will
force WebLogic's classloader to load classes located in the WEB-INF
directory of a Web application in preference to application or
system classes. This is a recommended approach since it only
impacts a single Web module.

Please refer to the following documents in WebLogic
for more information:

- [WebLogic
  ServerApplication Classloading](http://e-docs.bea.com/wls/docs81/programming/classloading.html)- For more information on how
  WebLogic's class loader works
- [Redeploying
  a Web Application in Exploded Directory Format](http://e-docs.bea.com/wls/docs81/webapp/deployment.html)

## Lack of namespacing on serialised items

BEA WebLogic Server 9.0 comes with its own StAX implementation.
This results in lack of namespacing on serialised items. In turn, WebLogic server (WLS) breaks with AXIOM on the WLS classpath. Hence
a filtering classloader is required:

Adding the following to weblogic-application.xml should resolve
this issue:

```

<prefer-application-packages>
<package-name>com.ctc.wstx.*</package-name>
<package-name>javax.xml.*</package-name>
<package-name>org.apache.*</package-name>
</prefer-application-packages>
```

Note that the libraries listed--Xerces, StAX API, Woodstox--need
to be on the application classpath.

# WebSphere

## Avoiding conflicts with WebSphere's JAX-WS runtime

The JAX-WS runtime in WebSphere Application Server is based on a modified version of Axis2 and these
classes are visible to application class loaders. This means that when deploying
a standard version of Axis2 on WAS 7.0 (and WAS 6.1 with the Web Services feature pack installed), special configuration is required to avoid conflicts with the Axis2 classes used internally by WebSphere.
In particular it is necessary to change the class loader policy of the Web module to parent last. However, this is not sufficient because Axis2 creates additional class loaders for modules and services, and
these use parent first class loading by default. Therefore, two things must be done to make a standard
Axis2 distribution work with WebSphere:

1. Before deploying the Axis2 WAR, edit the `axis2.xml` file and set the
   `EnableChildFirstClassLoading` parameter to `true`.
   Please note that this parameter is only supported in Axis2 1.5.5 or higher.
   The parameter is already present in the default `axis2.xml` file included in the
   WAR distribution, but its value is set to `false`. Therefore it is enough to change
   the parameter value.
2. After deployment, modify the application configuration to enable parent last class loading
   for the Web module: in the WebSphere admin console, go the the configuration page for
   the enterprise application, click on *Manage Modules* and locate the WAR containing
   Axis2 (in the default WAR distribution, the module is called *Apache-Axis2*), then
   change the *Class loader order* option to *Classes loaded with local class
   loader first (parent last)*. Note that the class loader policy for the enterprise
   application itself (which can be specified under *Class loading and update detection*)
   is irrelevant, unless a custom EAR distribution is used that includes the Axis2 libraries
   in the EAR instead of the WAR.

## Deploying services and modules

By default (i.e. if the *Distribute application* option has not been disabled explicitly)
WebSphere will deploy the application in exploded form. The standard location for these files is
in the `installedApps` subdirectory in the WebSphere profile directory. This means that AAR
and MAR files can simply be deployed by dropping them into the corresponding folders. In this
scenario, hot deployment is supported and there is no need to update the `services.list`
and `modules.list` files.

However, the directory is still under control of WebSphere and manually deployed AAR and MAR files
will be removed e.g. when the application is upgraded. It may therefore be a good idea to configure
Axis2 to use a repository location outside of the `installedApps` directory.

## Deploying older Axis2 versions

The instructions given above apply to Axis2 1.5.5 or higher. Older versions don't support
the `EnableChildFirstClassLoading` parameter, and we don't provide any support for
deploying these versions on WAS 6.1 (with the Web Services feature pack installed) or 7.0.
However, IBM has published a [technote](https://www-304.ibm.com/support/docview.wss?uid=swg21315686)
with an alternative approach that may work for older Axis2 versions.

## Known issues

On some WAS versions the following error may occur, e.g. when accessing a WSDL exposed by Axis2:

```
java.lang.VerifyError: JVMVRFY013 class loading constraint violated;
class=org/apache/xerces/dom/CoreDocumentImpl, method=getDomConfig()Lorg/w3c/dom/DOMConfiguration
```

This is caused by the XmlBeans library
packaged with Axis2. This library contains a set of interfaces in the `org.w3c.dom` package
and this may cause issues with class loaders that don't use a simple parent-first policy.
To avoid this issue, upgrade your WAS to a more recent fix pack level, remove the XmlBeans library
from the Axis2 WAR or remove the content of the `org.w3c.dom` package from the XmlBeans library.

---

<a id="docs-quickstartguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/quickstartguide.html -->

<!-- page_index: 5 -->

# Axis2 Quick Start Guide

The purpose of this guide is to get you started on creating
services and clients using Axis2 as quickly as possible. We'll take
a simple StockQuote Service and show you some of the different ways
in which you can create and deploy it, as well as take a quick look
at one or two utilities that come with Axis2. We'll then look at
creating clients to access those services.

## Content

- [Introduction](#docs-quickstartguide--introduction)
- [Getting Ready](#docs-quickstartguide--ready)
- [Axis2 services](#docs-quickstartguide--services)
- [Creating services](#docs-quickstartguide--create)
  - [Deploying POJOs](#docs-quickstartguide--deploy)
  - [Building the service using AXIOM](#docs-quickstartguide--axiom)
  - [Generating the service using ADB](#docs-quickstartguide--adb)
  - [Generating the service using
    XMLBeans](#docs-quickstartguide--xmlbeans)
  - [Generating the service using JiBX](#docs-quickstartguide--jibx)
- [Generating Clients](#docs-quickstartguide--clients)
  - [Creating a client using AXIOM](#docs-quickstartguide--clientaxiom)
  - [Generating a client using ADB](#docs-quickstartguide--clientadb)
  - [Generating a client using XML
    Beans](#docs-quickstartguide--clientxmlbeans)
  - [Generating a client using JiBX](#docs-quickstartguide--clientjibx)
- [Summary](#docs-quickstartguide--summary)
- [For Further Study](#docs-quickstartguide--furtherstudy)

### A Quick Setup Note:

The code for the document can be found in the extracted [Standard
Binary Distribution](https://axis.apache.org/axis2/java/core/download.cgi), more specifically at Axis2\_HOME/samples/
inside the directories- quickstart, quickstartadb, quickstartaxiom, quickstartjibx and quickstartxmlbeans. (Consider getting it now as
it will help you to follow along.) It includes Ant buildfiles
(build.xml) that we'll refer to throughout the examples to make
compilation easier.

## Introduction

Let's start with the service itself. We'll make it simple so you
can see what is going on when we build and deploy the services. A
StockQuoteService example seems to be mandatory in instances like
this one, so let's use the following (see Code Listing 1).

**Code Listing 1: The StockQuoteService class**

```

package samples.quickstart.service.pojo;

import java.util.HashMap;

public class StockQuoteService {
    private HashMap map = new HashMap();

    public double getPrice(String symbol) {
        Double price = (Double) map.get(symbol);
        if(price != null){
            return price.doubleValue();
        }
        return 42.00;
    }

    public void update(String symbol, double price) {
        map.put(symbol, new Double(price));
    }
}
```

It will be a simple service with two possible calls. One of
which is an in/out message, and the other is an in-only service.
Ultimately, we'll package the service and deploy it in four
different ways.

First, let's look at how this simple Java class corresponds to a
service.

## Getting Ready

Before we build anything using Axis2, we have to take care of a
little housekeeping. First off, you'll need to get your environment
ready for working with Axis2. Fortunately, it involves just a few
simple steps:

1. Download and install Java (Minimum version is JDK1.5). Set the
   JAVA\_HOME environment variable to the pathname of the directory
   into which you installed the JDK release.
2. Download Axis2 and extract it to a target directory.
3. Copy the axis2.war file to the webapps directory of your
   servlet engine.
4. Set the AXIS2\_HOME environment variable to point to the target
   directory in step. Note that all of the scripts and build files
   Axis2 generates depend on this value, so don't skip this step!
   Linux users can alternatively run the setenv.sh file in the
   AXIS2\_HOME/bin directory to set the AXIS2\_HOME environment variable
   to the pathname of the extracted directory of Axis2.

In most cases, we're also going to need a WSDL file for our
service. Axis2's Java2WSDL can be used to bootstrap a WSDL. To
generate a WSDL file from a Java class, perform the following
steps:

1. Create and compile the Java class.

```

(Windows)
%AXIS2_HOME%\bin\java2wsdl.bat -cp . -cn samples.quickstart.service.pojo.StockQuoteService -of StockQuoteService.wsdl

(Linux)
$AXIS2_HOME/bin/java2wsdl.sh -cp . -cn samples.quickstart.service.pojo.StockQuoteService -of StockQuoteService.wsdl
```

2. Generate the WSDL using the command:

Once you've generated the WSDL file, you can make the changes
you need. For example, you might add custom faults or change the
name of the generated elements. For example, this
StockQuoteService.wsdl is in
AXIS2\_HOME/samples/quickstartadb/resources/META-INF folder, which
we'll be using throughout the rest of this guide, replaces the
generic parameters created by the generation process.

## Axis2 Services

Before we build anything, it's helpful to understand what the
finished product looks like.

The server side of Axis2 can be deployed on any Servlet engine, and has the following structure. Shown in Code Listing 2.

**Code Listing 2: The Directory Structure of axis2.war**

```

axis2-web 
META-INF
WEB-INF
    classes 
    conf
        axis2.xml 
    lib
        activation.jar
        ...
        xmlSchema.jar
    modules
        modules.list 
        addressing.mar
        ...
        soapmonitor.mar
    services
        services.list
        aservice.aar
        ...
        version.aar
    web.xml
```

Starting at the top, axis2-web is a collection of JSPs that make
up the Axis2 administration application, through which you can
perform any action such as adding services and engaging and
dis-engaging modules. The WEB-INF directory contains the actual
java classes and other support files to run any services deployed
to the services directory.

The main file in all this is axis2.xml, which controls how the
application deals with the received messages, determining whether
Axis2 needs to apply any of the modules defined in the modules
directory.

Services can be deployed as \*.aar files, as you can see here, but their contents must be arranged in a specific way. For example, the structure of this service will be as follows:

```

- StockQuoteService
   - META-INF
     - services.xml
   - lib
   - samples
     - quickstart
       - service
         - pojo
           - StockQuoteService.class
```

Here, the name of the service is StockQuoteService, which is
specified in the services.xml file and corresponds to the top-level
folder of this service. Compiled Java classes are placed underneath
this in their proper place based on the package name. The lib
directory holds any service-specific JAR files needed for the
service to run (none in this case) besides those already stored
with the Axis2 WAR file and the servlet container's common JAR
directories. Finally, the META-INF directory contains any
additional information about the service that Axis2 needs to
execute it properly. The services.xml file defines the service
itself and links the Java class to it (See Code Listing 3).

**Code Listing 3: The Service Definition File**

```

<service name="StockQuoteService" scope="application">
    <description>
        Stock Quote Sample Service
    </description>
    <messageReceivers>
        <messageReceiver 
            mep="http://www.w3.org/ns/wsdl/in-only"
    class="org.apache.axis2.rpc.receivers.RPCInOnlyMessageReceiver"/>
        <messageReceiver
            mep="http://www.w3.org/ns/wsdl/in-out"
    class="org.apache.axis2.rpc.receivers.RPCMessageReceiver"/>
    </messageReceivers>
    <parameter name="ServiceClass">
        samples.quickstart.service.pojo.StockQuoteService
    </parameter>
</service>
```

Here the service is defined, along with the relevant
messageReceiver types for the different message exchange
patterns.

The META-INF directory is also the location for any custom WSDL
files you intend to include for this application.

You can deploy a service by simply taking this hierarchy of
files and copying it to the webapps/axis2/WEB-INF/services
directory of your servlet engine. (Note the Axis2 WAR file must be
installed first in the servlet engine.) This is known as the
"exploded" format. You can also compress your documents into an
\*.aar file, similar to a \*.jar file, and place the \*.aar file
directly in the servlet engine's webapps/axis2/WEB-INF/services
directory.

Now that you understand what we're trying to accomplish, we're
almost ready to start building.

First, [download](https://axis.apache.org/axis2/java/core/download.cgi)
and unzip the appropriate version of Axis2 Standard Binary
Distribution. Make sure that you set the value of the AXIS2\_HOME
variable to match the location into which you extracted the
contents of this release.

Let's look at some different ways to create clients and
services.

## Creating Services

In this section, we'll look at five ways to create a service
based on the StockQuoteService class: deploying Plain Old Java
Objects (POJO), building the service using AXIOM's OMElement, generating the service using Axis2 Databinding Framework (ADB), generating the service using XMLBeans, and generating the service
using JiBX.

### Deploying POJOs

To deploy the service using POJOs (Plain Old Java Objects), execute the following steps.

Note the directory structure contained at
AXIS2\_HOME/samples/quickstart (the services.xml file is
from the first section of this guide):

```

- quickstart
   - README.txt
   - build.xml
   - resources
     - META-INF
       - services.xml
   - src
     - samples
       - quickstart
         - service
           - pojo
             - StockQuoteService.java
```

Note that you can generate a WSDL from the quickstart directory
by typing:

```

ant generate.wsdl
```

However, creating StockQuoteService.wsdl is optional. It can be the
version generated directly from the Java class, or a customized
version of that file, and that services.xml is the same file
referenced earlier in this document.

Now build the project by typing ant generate.service in the
quickstart directory, which creates the following directory
structure:

```

- quickstart/build/classes
   - META-INF
     - services.xml
   - samples
     - quickstart
       - service
         - pojo
           - StockQuoteService.class
```

If you want to deploy the service in an exploded directory
format, rename the classes directory to StockQuoteService, and copy
it to the webapps/axis2/WEB-INF/services directory in your servlet
engine. Otherwise, copy the build/StockQuoteService.aar file to the
webapps/axis2/WEB-INF/services directory in your servlet engine.
Then check to make sure that the service has been properly deployed
by viewing the list of services at:

```

http://localhost:8080/axis2/services/listServices
```

You can also checkout the WSDL at:

```

http://localhost:8080/axis2/services/StockQuoteService?wsdl
```

And the schema at:

```

http://localhost:8080/axis2/services/StockQuoteService?xsd
```

Once the URLs are working, quickly test the service. Try
pointing your browser to the following URL:

```

http://localhost:8080/axis2/services/StockQuoteService/getPrice?symbol=IBM
```

You will get the following response:

```

<ns:getPriceResponse xmlns:ns="http://pojo.service.quickstart.samples/xsd"><ns:return>42</ns:return></ns:getPriceResponse>
```

If you invoke the update method as,

```

http://localhost:8080/axis2/services/StockQuoteService/update?symbol=IBM&price=100
```

and then execute the first getPrice URL, you will see that the
price has got updated.

### Building the Service using AXIOM

To build a service "from scratch" using AXIOM, execute the
following steps.

Note the directory structure contained at
/samples/quickstartaxiom:

```

- quickstartaxiom
   - README.txt
   - build.xml
   - resources
     - META-INF
       - services.xml
       - StockQuoteService.wsdl
   - src
     - samples
       - quickstart
         - service
           - axiom
             - StockQuoteService.java
         - clients
           - AXIOMClient.java
```

Since AXIOM is a little different, you're going to need a
different services.xml file from the one used for POJO. Define it, as shown in Code Listing 4.

**Code Listing 4: The Service Definition File.**

```

<service name="StockQuoteService" scope="application">
    <description>
        Stock Quote Service
    </description>
    <operation name="getPrice">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
    <operation name="update">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOnlyMessageReceiver"/>
    </operation>
    <parameter name="ServiceClass">samples.quickstart.service.axiom.StockQuoteService</parameter>
</service>
```

Note that it's almost the same, except that the operations are
explicitly defined in the service.xml file, and the
MessageReceivers are now RawXML.

Now, the above referenced StockQuoteService.java class, a plain
Java class that uses classes from the Axis2 libraries, is defined
as shown in Code Listing 5.

**Code Listing 5: The StockQuoteService Class using
AXIOM**

```

package samples.quickstart.service.axiom;

import javax.xml.stream.XMLStreamException;
import org.apache.axiom.om.OMAbstractFactory;
import org.apache.axiom.om.OMElement;
import org.apache.axiom.om.OMFactory;
import org.apache.axiom.om.OMNamespace;

import java.util.HashMap;
public class StockQuoteService {
    private HashMap map = new HashMap();

    public OMElement getPrice(OMElement element) throws XMLStreamException {
        element.build();
        element.detach();

        OMElement symbolElement = element.getFirstElement();
        String symbol = symbolElement.getText();

        String returnText = "42";
        Double price = (Double) map.get(symbol);
        if(price != null){
            returnText  = "" + price.doubleValue();
        }
        OMFactory fac = OMAbstractFactory.getOMFactory();
        OMNamespace omNs =
            fac.createOMNamespace("http://axiom.service.quickstart.samples/xsd", "tns");
        OMElement method = fac.createOMElement("getPriceResponse", omNs);
        OMElement value = fac.createOMElement("price", omNs);
        value.addChild(fac.createOMText(value, returnText));
        method.addChild(value);
        return method;
    }

    public void update(OMElement element) throws XMLStreamException {
        element.build();
        element.detach();

        OMElement symbolElement = element.getFirstElement();
        String symbol = symbolElement.getText();

        OMElement priceElement = (OMElement)symbolElement.getNextOMSibling();
        String price = priceElement.getText();

        map.put(symbol, new Double(price));
    }
}
```

Axis2 uses AXIOM, or the AXIs Object Model, a [DOM](http://www.w3.org/DOM/) (Document Object Model)-like
structure that is based on the StAX API (Streaming API for XML).
Methods that act as services must take as their argument an
OMElement, which represents an XML element that happens, in this
case, to be the payload of the incoming SOAP message. Method
getPrice(OMElement), for example, extracts the contents of the
first child of the payload element, which corresponds to the stock
symbol, and uses this to look up the current price of the stock.
Unless this is an "in only" service, these methods must return an
OMElement, because that becomes the payload of the return SOAP
message.

Now build the project by typing ant generate.service in the
Axis2\_HOME/samples/quickstartaxiom directory.

Place the StockQuoteService.aar file in the
webapps/axis2/WEB-INF/services directory of the servlet engine, and
check to make sure that the service has been properly deployed by
viewing the list of services at,

```

http://localhost:8080/axis2/services/listServices
```

You can also check the custom WSDL at,

```

http://localhost:8080/axis2/services/StockQuoteService?wsdl
```

and the schema at,

```

http://localhost:8080/axis2/services/StockQuoteService?xsd
```

### Generating the Service using ADB

To generate and deploy the service using the Axis2 Databinding
Framework (ADB), execute the following steps.

Generate the skeleton using the WSDL2Java utility by typing the
following in the Axis2\_HOME/samples/quickstartadb directory:

```

(Windows)
%AXIS2_HOME%\bin\wsdl2java.bat -uri resources\META-INF\StockQuoteService.wsdl -p samples.quickstart.service.adb -d adb -s -ss -sd -ssi -o build\service

(Linux)
$AXIS2_HOME/bin/wsdl2java.sh -uri resources/META-INF/StockQuoteService.wsdl -p samples.quickstart.service.adb -d adb -s -ss -sd -ssi -o build/service
```

Else, simply type ant generate.service in the
Axis2\_HOME/samples/quickstartadb directory.

The option -d adb specifies Axis Data Binding (ADB). The -s
switch specifies synchronous or blocking calls only. The -ss switch
creates the server side code (skeleton and related files). The -sd
switch creates a service descriptor (services.xml file). The -ssi
switch creates an interface for the service skeleton. The service
files should now be located at build/service.

If you generated the code by using WSDL2Java directly, next you
have to modify the generated skeleton to implement the service (if
you used "ant generate.service", a completed skeleton will be
copied over the generated one automatically).

Open the
build/service/src/samples/quickstart/adb/service/StockQuoteServiceSkeleton.java
file and modify it to add the functionality of your service to the
generated methods; shown in Code Listing 6.

**Code Listing 6: Defining the Service Skeleton File**

```

package samples.quickstart.service.adb;

import samples.quickstart.service.adb.xsd.GetPriceResponse;
import samples.quickstart.service.adb.xsd.Update;
import samples.quickstart.service.adb.xsd.GetPrice;

import java.util.HashMap;

public class StockQuoteServiceSkeleton implements StockQuoteServiceSkeletonInterface {

    private static HashMap map;

    static{ map = new HashMap(); }

    public void update(Update param0) {
        map.put(param0.getSymbol(), new Double(param0.getPrice()));
    }

    public GetPriceResponse getPrice(GetPrice param1) {
        Double price = (Double) map.get(param1.getSymbol());
        double ret = 42;
        if(price != null){
            ret = price.doubleValue();
        }
        GetPriceResponse res =
                new GetPriceResponse();
        res.set_return(ret);
        return res;
    }
}
```

Now you can build the project by typing the following command in
the build/service directory:

```

ant jar.server
```

If all goes well, you should see the BUILD SUCCESSFUL message in
your window, and the StockQuoteService.aar file in the
build/service/build/lib directory. Copy this file to the
webapps/axis2/WEB-INF/services directory of the servlet engine.

You can check to make sure that the service has been properly
deployed by viewing the list of services at,

```

http://localhost:8080/axis2/services/listServices
```

You can also check the custom WSDL at,

```

http://localhost:8080/axis2/services/StockQuoteService?wsdl
```

and the schema at,

```

http://localhost:8080/axis2/services/StockQuoteService?xsd
```

### Generating the Service using XMLBeans

To generate a service using XMLBeans, execute the following
steps.

Generate the skeleton using the WSDL2Java utility by typing the
following in the Axis2\_HOME/samples/quickstartxmlbeans
directory.

```

%AXIS2_HOME%\bin\wsdl2java.bat -uri resources\META-INF\StockQuoteService.wsdl -p samples.quickstart.service.xmlbeans -d xmlbeans -s -ss -sd -ssi -o build\service
```

Else simply type ant generate.service in the
Axis2\_HOME/samples/quickstartxmlbeans directory.

The option -d xmlbeans specifies XML Beans data binding. The -s
switch specifies synchronous or blocking calls only. The -ss switch
creates the server side code (skeleton and related files). The -sd
switch creates a service descriptor (services.xml file). The -ssi
switch creates an interface for the service skeleton. The service
files should now be located at build/service.

If you generated the code by using WSDL2Java directly, next you
have to modify the generated skeleton to implement the service (if
you used "ant generate.service", a completed skeleton will be
copied over the generated one automatically).

Next open the
build/service/src/samples/quickstart/service/xmlbeans/StockQuoteServiceSkeleton.java
file and modify it to add the functionality of your service to the
generated methods (see Code Listing 7).

**Code Listing 7: Defining the Service Skeleton**

```

package samples.quickstart.service.xmlbeans;

import samples.quickstart.service.xmlbeans.xsd.GetPriceDocument;
import samples.quickstart.service.xmlbeans.xsd.GetPriceResponseDocument;
import samples.quickstart.service.xmlbeans.xsd.UpdateDocument;

import java.util.HashMap;

public class StockQuoteServiceSkeleton implements StockQuoteServiceSkeletonInterface {

    private static HashMap map;

    static{ map = new HashMap(); }

    public void update(UpdateDocument param0) {
        map.put(param0.getUpdate().getSymbol(), new Double(param0.getUpdate().getPrice()));
    }

    public GetPriceResponseDocument getPrice(GetPriceDocument param1) {
        Double price = (Double) map.get(param1.getGetPrice().getSymbol());
        double ret = 42;
        if(price != null){
            ret = price.doubleValue();
        }
        System.err.println();
        GetPriceResponseDocument resDoc =
                GetPriceResponseDocument.Factory.newInstance();
        GetPriceResponseDocument.GetPriceResponse res =
                resDoc.addNewGetPriceResponse();
        res.setReturn(ret);
        return resDoc;
    }
}
```

Build the project by typing the following command in the
build/service directory, which contains the build.xml file:

```

ant jar.server
```

If all goes well, you should see the BUILD SUCCESSFUL message in
your window, and the StockQuoteService.aar file in the newly
created build/service/build/lib directory. Copy this file to the
webapps/axis2/WEB-INF/services directory of the servlet engine.

You can check to make sure that the service has been properly
deployed by viewing the list of services at,

```

http://localhost:8080/axis2/services/listServices
```

You can also check the custom WSDL at,

```

http://localhost:8080/axis2/services/StockQuoteService?wsdl
```

and the schema at,

```

http://localhost:8080/axis2/services/StockQuoteService?xsd
```

### Generating the Service using JiBX

To generate and deploy the service using [JiBX data binding](http://www.jibx.org), execute the following
steps.

Generate the skeleton using the WSDL2Java utility by typing the
following at a console in the Axis2\_HOME/samples/quickstartjibx
directory:

```

%AXIS2_HOME%\bin\wsdl2java.bat -uri resources\META-INF\StockQuoteService.wsdl -p samples.quickstart.service.jibx -d jibx -s -ss -sd -ssi -uw -o build\service
```

Else, simply type "ant generate.service" in the
Axis2\_HOME/samples/quickstartjibx directory.

The option -d jibx specifies JiBX data binding. The -s switch
specifies synchronous or blocking calls only. The -ss switch
creates the server side code (skeleton and related files). The -sd
switch creates a service descriptor (services.xml file). The -ssi
switch creates an interface for the service skeleton. The -uw
switch unwraps the parameters passed to and from the service
operations in order to create a more natural programming
interface.

After running WSDL2Java, the service files should be located at
build/service. If you generated the code by using WSDL2Java
directly, you need to modify the generated skeleton to implement
the service (if you used "ant generate.service" a completed
skeleton will be copied over the generated one automatically). Open
the
build/service/src/samples/quickstart/service/jibx/StockQuoteServiceSkeleton.java
file and modify it to add the functionality of your service to the
generated methods, as shown in Code Listing 8.

**Code Listing 8: Defining the Service Skeleton File**

```

package samples.quickstart.service.jibx;

import java.util.HashMap;

public class StockQuoteServiceSkeleton implements StockQuoteServiceSkeletonInterface {
    private HashMap map = new HashMap();

    public void update(String symbol, Double price) {
        map.put(symbol, price);
    }

    public Double getPrice(String symbol) {
        Double ret = (Double) map.get(symbol);
        if (ret == null) {
            ret = new Double(42.0);
        }
        return ret;
    }
}
```

Now you can build the project by typing the following command in
the build/service directory:

```

ant jar.server
```

If all goes well, you should see the BUILD SUCCESSFUL message in
your window, and the StockQuoteService.aar file in the
build/service/build/lib directory. Copy this file to the
webapps/axis2/WEB-INF/services directory of the servlet engine.

You can check to make sure that the service has been properly
deployed by viewing the list of services at,

```

http://localhost:8080/axis2/services/listServices
```

You can also check the custom WSDL at,

```

http://localhost:8080/axis2/services/StockQuoteService?wsdl
```

and the schema at,

```

http://localhost:8080/axis2/services/StockQuoteService?xsd
```

For more information on using JiBX with Axis2, see the [JiBX code generation
integration](#docs-jibx-jibx-codegen-integration) details.

## Creating Clients

In this section, we'll look at four ways to create clients based
on the StockQuoteService class: building an AXIOM based client, generating a client using Axis2 Databinding Framework (ADB), generating a client using XMLBeans, and generating a client using
JiBX.

### Creating a Client with AXIOM

To build a client using AXIOM, execute the following steps.

Also, note the directory structure shown in the Creating a
service with AXIOM section, duplicated below for completeness.

```

- quickstartaxiom
   - README.txt
   - build.xml
   - resources
     - META-INF
       - services.xml
       - StockQuoteService.wsdl
   - src
     - samples
       - quickstart
         - service
           - axiom
             - StockQuoteService.java
         - clients
           - AXIOMClient.java
```

The above referenced AXIOMClient.java class is defined as
follows, shown in Code Listing 9.

**Code Listing 9: The AXIOMClient class using AXIOM**

```

package samples.quickstart.clients;

import org.apache.axiom.om.OMAbstractFactory;
import org.apache.axiom.om.OMElement;
import org.apache.axiom.om.OMFactory;
import org.apache.axiom.om.OMNamespace;
import org.apache.axis2.Constants;
import org.apache.axis2.addressing.EndpointReference;
import org.apache.axis2.client.Options;
import org.apache.axis2.client.ServiceClient;

public class AXIOMClient {

    private static EndpointReference targetEPR = 
        new EndpointReference("http://localhost:8080/axis2/services/StockQuoteService");

    public static OMElement getPricePayload(String symbol) {
        OMFactory fac = OMAbstractFactory.getOMFactory();
        OMNamespace omNs = fac.createOMNamespace("http://axiom.service.quickstart.samples/xsd", "tns");

        OMElement method = fac.createOMElement("getPrice", omNs);
        OMElement value = fac.createOMElement("symbol", omNs);
        value.addChild(fac.createOMText(value, symbol));
        method.addChild(value);
        return method;
    }

    public static OMElement updatePayload(String symbol, double price) {
        OMFactory fac = OMAbstractFactory.getOMFactory();
        OMNamespace omNs = fac.createOMNamespace("http://axiom.service.quickstart.samples/xsd", "tns");

        OMElement method = fac.createOMElement("update", omNs);

        OMElement value1 = fac.createOMElement("symbol", omNs);
        value1.addChild(fac.createOMText(value1, symbol));
        method.addChild(value1);

        OMElement value2 = fac.createOMElement("price", omNs);
        value2.addChild(fac.createOMText(value2,
                                         Double.toString(price)));
        method.addChild(value2);
        return method;
    }

    public static void main(String[] args) {
        try {
            OMElement getPricePayload = getPricePayload("WSO");
            OMElement updatePayload = updatePayload("WSO", 123.42);
            Options options = new Options();
            options.setTo(targetEPR);
            options.setTransportInProtocol(Constants.TRANSPORT_HTTP);

            ServiceClient sender = new ServiceClient();
            sender.setOptions(options);

            sender.fireAndForget(updatePayload);
            System.err.println("price updated");
            OMElement result = sender.sendReceive(getPricePayload);

            String response = result.getFirstElement().getText();
            System.err.println("Current price of WSO: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
```

Axis2 uses AXIOM, or the AXIs Object Model, a DOM (Document
Object Model)-like structure that is based on the StAX API
(Streaming API for XML). Here you setup the payload for the update
and getPrice methods of the service. The payloads are created
similar to how you created the getPriceResponse payload for the
AXIOM service. Then you setup the Options class, and create a
ServiceClient that you'll use to communicate with the service.
First you call the update method, which is a fireAndForget method
that returns nothing. Lastly, you call the getPrice method, and
retrieve the current price from the service and display it.

Now you can build and run the AXIOM client by typing ant
run.client in the Axis2\_HOME/samples/quickstartaxiom directory.

You should get the following as output:

```

done
Current price of WSO: 123.42
```

### Generating a Client using ADB

To build a client using Axis Data Binding (ADB), execute the
following steps.

Generate the client data bindings by typing the following in the
Axis2\_HOME/samples/quickstartadb directory:

```

%AXIS2_HOME%\bin\wsdl2java.bat -uri resources\META-INF\StockQuoteService.wsdl -p samples.quickstart.clients -d adb -s -o build\client
```

Else, simply type ant generate.client in the
Axis2\_HOME/samples/quickstartadb directory.

Next take a look at
quickstartadb/src/samples/quickstart/clients/ADBClient.java, and
see how it's defined in Code Listing 10.

**Code Listing 10: The ADBClient Class**

```

package samples.quickstart.clients;

import samples.quickstart.service.adb.StockQuoteServiceStub;

public class ADBClient{
    public static void main(java.lang.String args[]){
        try{
            StockQuoteServiceStub stub =
                new StockQuoteServiceStub
                ("http://localhost:8080/axis2/services/StockQuoteService");

            getPrice(stub);
            update(stub);
            getPrice(stub);

        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

    /* fire and forget */
    public static void update(StockQuoteServiceStub stub){
        try{
            StockQuoteServiceStub.Update req = new StockQuoteServiceStub.Update();
            req.setSymbol ("ABC");
            req.setPrice (42.35);

            stub.update(req);
            System.err.println("price updated");
        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

    /* two way call/receive */
    public static void getPrice(StockQuoteServiceStub stub){
        try{
            StockQuoteServiceStub.GetPrice req = new StockQuoteServiceStub.GetPrice();

            req.setSymbol("ABC");

            StockQuoteServiceStub.GetPriceResponse res =
                stub.getPrice(req);

            System.err.println(res.get_return());
        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

}
```

This class creates a client stub using the Axis Data Bindings
you created. Then it calls the getPrice and update operations on
the Web service. The getPrice method operation creates the GetPrice
payload and sets the symbol to ABC. It then sends the request and
displays the current price. The update method creates an Update
payload, setting the symbol to ABC and the price to 42.35.

Now build and run the client by typing ant run.client in the
Axis2\_HOME/samples/quickstartadb directory.

You should get the following as output:

```

42
price updated
42.35
```

### Generating a Client using XMLBeans

To build a client using the XML Beans data bindings, execute the
following steps.

Generate the databings by typing the following in the
xmlbeansClient directory.

```

%AXIS2_HOME%\bin\wsdl2java.bat -uri resources\META-INF\StockQuoteService.wsdl -p samples.quickstart.service.xmlbeans -d xmlbeans -s -o build\client
```

Else, simply type ant generate.client in the
Axis2\_HOME/samples/quickstartxmlbeans directory.

Note that this creates a client stub code and no server side
code.

Next take a look at
quickstartxmlbeans/src/samples/quickstart/clients/XMLBEANSClient.java, and see how it's defined in Code Listing 11.

**Code Listing 11: The XMLBEANSClient class**

```

package samples.quickstart.clients;

import samples.quickstart.service.xmlbeans.StockQuoteServiceStub;
import samples.quickstart.service.xmlbeans.xsd.GetPriceDocument;
import samples.quickstart.service.xmlbeans.xsd.GetPriceResponseDocument;
import samples.quickstart.service.xmlbeans.xsd.UpdateDocument;

public class XMLBEANSClient{

    public static void main(java.lang.String args[]){
        try{
            StockQuoteServiceStub stub =
                new StockQuoteServiceStub
                ("http://localhost:8080/axis2/services/StockQuoteService");

            getPrice(stub);
            update(stub);
            getPrice(stub);

        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

    /* fire and forget */
    public static void update(StockQuoteServiceStub stub){
        try{
            UpdateDocument reqDoc = UpdateDocument.Factory.newInstance();
            UpdateDocument.Update req = reqDoc.addNewUpdate();
            req.setSymbol ("BCD");
            req.setPrice (42.32);

            stub.update(reqDoc);
            System.err.println("price updated");
        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

    /* two way call/receive */
    public static void getPrice(StockQuoteServiceStub stub){
        try{
            GetPriceDocument reqDoc = GetPriceDocument.Factory.newInstance();
            GetPriceDocument.GetPrice req = reqDoc.addNewGetPrice();
            req.setSymbol("BCD");

            GetPriceResponseDocument res =
                stub.getPrice(reqDoc);

            System.err.println(res.getGetPriceResponse().getReturn());
        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }
}
```

This class creates a client stub using the XML Beans data
bindings you created. Then it calls the getPrice and the update
operations on the Web service. The getPrice method operation
creates the GetPriceDocument, its inner GetPrice classes and sets
the symbol to ABC. It then sends the request and retrieves a
GetPriceResponseDocument and displays the current price. The update
method creates an UpdateDocument, updates and sets the symbol to
ABC and price to 42.32, displaying 'done' when complete.

Now build and run the the project by typing ant run.client in
the Axis2\_HOME/samples/quickstartxmlbeans directory.

You should get the following as output:

```

42
price updated
42.32
```

### Generating a Client using JiBX

To build a client using JiBX, execute the following steps.

Generate the client stub by typing the following at a console in
the Axis2\_HOME/samples/quickstartjibx directory.

```

%AXIS2_HOME%\bin\wsdl2java.bat -uri resources\META-INF\StockQuoteService.wsdl -p samples.quickstart.clients -d jibx -s -uw -o build\client
```

Else, simply type "ant generate.client".

Next take a look at
quickstartjibx/src/samples/quickstart/clients/JiBXClient.java, shown below in Code Listing 12.

**Code Listing 12: The JiBXClient class**

```

package samples.quickstart.clients;

import samples.quickstart.service.jibx.StockQuoteServiceStub;

public class JiBXClient{
    public static void main(java.lang.String args[]){
        try{
            StockQuoteServiceStub stub =
                new StockQuoteServiceStub
                ("http://localhost:8080/axis2/services/StockQuoteService");

            getPrice(stub);
            update(stub);
            getPrice(stub);

        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

    /* fire and forget */
    public static void update(StockQuoteServiceStub stub){
        try{
            stub.update("CDE", new Double(42.35));
            System.err.println("price updated");
        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

    /* two way call/receive */
    public static void getPrice(StockQuoteServiceStub stub){
        try{
            System.err.println(stub.getPrice("CDE"));
        } catch(Exception e){
            e.printStackTrace();
            System.err.println("\n\n\n");
        }
    }

}
```

This class uses the created JiBX client stub to access the
getPrice and the update operations on the Web service. The getPrice
method sends a request for the stock "ABC" and displays the current
price. The update method setsnex the price for stock "ABC" to
42.35.

Now build and run the client by typing "ant run.client" at a
console in the Axis2\_HOME/samples/quickstartjibx directory.

You should get the following as output:

```

42
price updated
42.35
```

For more information on using JiBX with Axis2, see the [JiBX code generation
integration](#docs-jibx-jibx-codegen-integration) details.

## Summary

Axis2 provides a slick and robust way to get web services up and
running in no time. This guide presented five methods of creating a
service deployable on Axis2, and four methods of creating a client
to communicate with the services. You now have the flexibility to
create Web services using a variety of different technologies.

## For Further Study

[Apache Axis2](#index)

[Axis2 Architecture](#docs-axis2architectureguide)

Introduction to Apache Axis2-<http://www.redhat.com/magazine/021jul06/features/apache_axis2/>

---

<a id="docs-userguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/userguide.html -->

<!-- page_index: 6 -->

# Apache Axis2 User's Guide

This guide provides a starting place for users who are new to
Apache Axis2. It also covers some advanced topics, such as how to
use Axis2 to create and deploy Web services as well as how to use
WSDL to generate both clients and services.

For experienced users of Apache Axis2, we recommend the [Advanced User's Guide.](#docs-adv-userguide)
For users of JSON and Spring Boot, see the sample application in the [JSON and Spring Boot User's Guide.](#docs-json-springboot-userguide)

# Introducing Axis2

This section introduces Axis2 and its structure, including an
explanation of various directories/files included in the latest
Axis2 [download](https://axis.apache.org/axis2/java/core/download.cgi).

## Content

- [**Introducing
  Axis2**](#docs-userguide--intro)
  - [**What is
    Axis2?**](#docs-userguide--whatis)
  - [**What's under the
    hood?**](#docs-userguide--underhood)
  - [**How Axis2 handles
    SOAP messages**](#docs-userguide--handlessoap)
  - [How Axis2 handles JSON
    messages](#docs-userguide--handlesjson)
  - [**Axis2
    Distributions**](#docs-userguide--distributions)
  - [**The Axis2 Standard Binary
    Distribution**](#docs-userguide--sbd)
  - [**Axis2.war Directory
    Hierarchy**](#docs-userguide--hierarchy)
  - [**Axis2 Documents
    Distribution**](#docs-userguide--docs)
  - [**Axis2 and
    Clients**](#docs-userguide--clients)
- [Installing and
  Testing Client Code](https://axis.apache.org/axis2/java/core/docs/userguide-installingtesting.html#installingtesting)
- [Introduction to
  Services](https://axis.apache.org/axis2/java/core/docs/userguide-introtoservices.html#introservices)
  - [Message Exchange
    Patterns](https://axis.apache.org/axis2/java/core/docs/userguide-introtoservices.html#messageexchange)
- [Creating
  Clients](https://axis.apache.org/axis2/java/core/docs/userguide-creatingclients.html#createclients)
  - [Choosing a Client
    Generation Method](https://axis.apache.org/axis2/java/core/docs/userguide-creatingclients.html#choosingclient)
  - [Generating
    Clients](https://axis.apache.org/axis2/java/core/docs/userguide-creatingclients.html#generating)
  - [Axis Data Binding
    (ADB)](https://axis.apache.org/axis2/java/core/docs/userguide-creatingclients.html#adb)
- [Building
  Services](https://axis.apache.org/axis2/java/core/docs/userguide-buildingservices.html#buildservices)
  - [Getting
    Comfortable with Available Options](https://axis.apache.org/axis2/java/core/docs/userguide-buildingservices.html#getcomfortable)
  - [Creating a Service
    from Scratch](https://axis.apache.org/axis2/java/core/docs/userguide-buildingservices.html#createscratch)
  - [Deploying
    Plain Old Java Objects](https://axis.apache.org/axis2/java/core/docs/userguide-buildingservices.html#deploypojo)
  - [Deploying
    and Running an Axis2 Service Created from WSDL](https://axis.apache.org/axis2/java/core/docs/userguide-buildingservices.html#deployrun)
- [Samples](https://axis.apache.org/axis2/java/core/docs/userguide-samples.html)
- [For Further
  Study](https://axis.apache.org/axis2/java/core/docs/userguide-forfurtherstudy.html)

## What is Axis2?

The Apache Axis2 project is a Java-based implementation of both
the client and server sides of the Web services equation. Designed
to take advantage of the lessons learned from Apache Axis 1.0, Apache Axis2 provides a complete object model and a modular
architecture that makes it easy to add functionality and support
for new Web services-related specifications and
recommendations.

Axis2 enables you to easily perform the following tasks:

- Send SOAP messages
- Receive and process SOAP messages
- Receive and process JSON messages
- Create a Web service out of a plain Java class
- Create implementation classes for both the server and client
  using WSDL
- Easily retrieve the WSDL for a service
- Send and receive SOAP messages with attachments
- Create or utilize a REST-based Web service
- Create or utilize services that take advantage of [WS-Security](http://www.oasis-open.org/committees/download.php/16790/wss-v1.1-spec-os-SOAPMessageSecurity.pdf) and [WS-Addressing](http://www.w3.org/2002/ws/addr/)

Many more features exist as well, but this user guide
concentrates on showing you how to accomplish the first five tasks
on this list.

## What's Under the Hood?

To understand Axis2 and what it does, you must have a good idea
of the life cycle of a Web services message. Typically, it looks
something like this:

![Lifecycle of a Web services message](assets/images/fig01_770b49c8c953ec2a.jpg)

The sending application creates the original SOAP message, an
XML message that consists of headers and a body. (For more
information on SOAP, see "[Introduction to Services](https://axis.apache.org/axis2/java/core/docs/userguide-introtoservices.html)".)
If the system requires the use of WS\* recommendations such as
WS-Addressing or WS-Security, the message may undergo additional
processing before it leaves the sender. Once the message is ready, it is sent via a particular transport such as HTTP, JMS, and so
on.

The message works its way over to the receiver, which takes in
the message via the transport listener. (In other words, if the
application doesn't have an HTTP listener running, it's not going
to receive any HTTP messages.) Again, if the message is part of a
system that requires the use of WS-Security or other
recommendations, it may need additional processing for the purpose
of checking credentials or decrypting sensitive information.
Finally, a dispatcher determines the specific application (or other
component, such as a Java method) for which the message was
intended, and sends it to that component. That component is part of
an overall application designed to work with the data being sent
back and forth.

## How Axis2 Handles SOAP Messages

Axis2 can handle processing for both the sender and the receiver
in a transaction. From the Axis2 perspective, the structure looks
like this:

![Axis2 handles SOAP messages](assets/images/fig02_871fa58d2d39620a.jpg)

On each end, you have an application designed to deal with the
(sent or received) messages. In the middle, you have Axis2, or
rather, you *can* have Axis2. The value of Web services is
that the sender and receiver (each of which can be either the
server or the client) don't even have to be on the same platform, much less running the same application. Assuming that Axis2 is
running on both sides, the process looks like this:

- The sender creates the SOAP message.
- Axis "handlers" perform any necessary actions on that message
  such as encryption of WS-Security related messages.
- The transport sender sends the message.
- On the receiving end, the transport listener detects the
  message.
- The transport listener passes the message on to any handlers on
  the receiving side.
- Once the message has been processed in the "pre-dispatch"
  phase, it is handed off to the dispatchers, which pass it on to the
  appropriate application.

In Axis2, these actions are broken down into "phases", with
several pre-defined phases, such as the "pre-dispatch", "dispatch,"
and "message processing", being built into Axis2. Each phase is a
collection of "handlers". Axis2 enables you to control what
handlers go into which phases, and the order in which the handlers
are executed within the phases. You can also add your own phases
and handlers.

Handlers come from "modules" that can be plugged into a running
Axis2 system. These modules, such as Rampart, which provides an
implementation of WS-Security, are the main extensibility
mechanisms in Axis2.

## How Axis2 Handles JSON Messages

Axis2 with REST provides GSON or the newer Moshi library as the JSON parser.
With the proper axis2.xml configuration, this support is triggered by the HTTP header
"Content-Type: application/json".

More docs concerning Axis2 and JSON can be found in the [Pure JSON Support](#docs-json_support_gson) and [JSON User Guide.](#docs-json_gson_user_guide)

For users of JSON and Spring Boot - or anyone interesed in a complete JSON example that
includes Spring Security - see the sample application in the [JSON and Spring Boot User's Guide.](#docs-json-springboot-userguide)

## Axis2 Distributions

Axis2 is released in several [distributions](https://axis.apache.org/axis2/java/core/download.cgi). Which one you need depends on what you'll be
doing with it.

### The Axis2 Standard Binary Distribution

If you're developing services and applications, you'll need the
Axis2 Standard Binary Distribution. The distribution includes all the
necessary \*.jar files, as well as a variety of scripts that ease
development. It has the following structure.

**Code Listing 1: Axis2 Standard Binary Distribution**

```

bin
      axis2.bat
      axis2.sh
      axis2server.bat
      axis2server.sh
      java2wsdl.bat
      java2wsdl.sh
      wsdl2java.bat
      wsdl2java.sh
      setenv.sh
lib
      activation-1.1.jar
      ...
      XmlSchema.jar
repository
             modules
         modules.list 
                addressing-1.1.mar
               ..
             services
         services.list
                version.aar
         ..
samples
      ...
webapp
      ...
conf
    axis2.xml

LICENSE.txt
README.txt
NOTICE.txt
INSTALL.txt
release-notes.html
```

The bin directory includes a number of useful scripts. They
include axis2.bat (or axis2.sh), which enables you to easily
execute a Java command without having to manually add all the Axis2
jar files to the classpath, java2wsdl.bat (and .sh) and
wsdl2java.bat (and .sh), which enable you to easily generate Java
code from a WSDL file and vice versa, and axis2server.bat (and sh), a simple Web server that enables you to build Axis2's capability to
send and receive messages into your own application.

As expected, the lib directory includes all the necessary .jar
files. Services and modules are added to the repository directory.
Axis2 comes with a standard module implementing WS-Addressing, and
you can add any other necessary module such as Rampart to the
repository/modules directory.

conf directory includes the axis2.xml which is the global
deployment descriptor.

Finally, the samples directory includes all the sample code
distributed with Axis2. See the list of [samples and their descriptions](https://axis.apache.org/axis2/java/core/docs/userguide-samples.html).

## axis2.war Distribution Directory Hierarchy

axis2.war is available in [WAR (Web Archive) Distribution](https://axis.apache.org/axis2/java/core/download.cgi). The server side of Axis2 ships
as a J2EE application, and has the following structure shown in
Code Listing 2.

**Code Listing 2: Server Side of Axis2**

```

axis2-web 
META-INF
WEB-INF
    classes 
    conf
        axis2.xml 
    lib
        activation.jar
        ...
        xmlSchema.jar
    modules
        modules.list 
        addressing.mar
        ...
        soapmonitor.mar
    services
        services.list
        aservice.aar
        ...
        version.aar
    web.xml
```

Starting at the top, axis2-web is a collection of JSPs that make
up the [Axis2 administration
application](#docs-webadminguide), through which you can perform any needed actions
such as adding services and engaging and dis-engaging modules. The
WEB-INF directory represents the actual Axis2 application, including all the \*.jar files, any included modules, and even the
deployed services themselves.

The classes directory holds any class or property files that are
needed by Axis2 itself, such as log4j2.xml. Any actual
services to be handled by the system reside in the services
directory in the form of an axis archive, or \*.aar file. This file
contains any classes related to the service, as well as the
services.xml file, which controls any additional requirements, such
as the definition of message senders and message receivers.

The main file in all this is axis2.xml, which controls how the
application deals with received messages. It defines message
receivers and transport receivers, as well as defining transport
senders and determining which modules are active. It also defines
the order of phases, and the handlers to be executed within each
phase.

You can control all of this information through the use of the
Web application, but if you restart the Axis2 application, these
changes are lost and the server goes back to the definitions in the
axis2.xml file.

Axis2 also provides a third distribution, the [source distribution](https://axis.apache.org/axis2/java/core/download.cgi), which enables you to generate this .war
file yourself.

## Axis2 Documentation Distribution Directory Hierarchy

The Documents distribution includes all Axis2 documentation
including the xdcos and javadocs. It has the following
structure:

**Code Listing 3: Axis2 Documents Distribution**

```

docs
      javadocs
      xdocs

LICENSE.txt
README.txt
release-notes.html
```

The javadocs directory includes all the standard [API documentation](https://axis.apache.org/axis2/java/core/api/index.html) for the Axis2
API, with other documentation (like this document) in the xdocs
directory.

## Axis2 and Clients

Now that explains how Axis2 behaves as part of a Web
application. What about a standalone client that is not part of a
J2EE application? In that case, a sender can use the Axis2 default
properties, in other words, no special handlers, and so on. But you
also have the option to tell the client to load its own copy of the
axis2.xml file and behave accordingly.

**See Next Section** - [Installing and
Testing Client Code](https://axis.apache.org/axis2/java/core/docs/userguide-installingtesting.html#installingtesting)

---

<a id="docs-adv-userguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/adv-userguide.html -->

<!-- page_index: 7 -->

# Apache Axis2 Advanced User's Guide

This guide will help you get started with Axis2, the next generation of
Apache Axis! It gives a detailed description on how to write Web services and
Web service clients using Axis2, how to write custom modules, and how to use
them with a Web service. Advanced topics and samples that are shipped with
the binary distribution of Axis2 are also discussed.

## Introduction

This user guide is written based on the Axis2 Standard Binary
Distribution. The Standard Binary Distribution can be directly [downloaded](https://axis.apache.org/axis2/java/core/download.cgi) or built using
the Source Distribution. If
you choose the latter, then the [Installation
Guide](#docs-installationguide) will instruct you on how to build Axis2 Standard Binary
Distribution using the source.

Please note that Axis2 is an open-source effort. If you feel the code
could use some new features or fixes, please get involved and lend us a hand!
The Axis developer community welcomes your participation.

Let us know what you think! Send your feedback to "[java-user@axis.apache.org](mailto:java-user@axis.apache.org?subject=[Axis2])".
(Subscription details are available on the [Axis2 site](#mail-lists).) Kindly
prefix the subject of the mail with [Axis2].

## Getting Started

The first two sections of the user guide explain how to write and deploy a
new Web Service using Axis2, and how to write a Web Service client using
Axis2. The next section -  [Configuring Axis2](#docs-adv-userguide--config) - provides
an introduction to important configuration options in Axis2. The final
section - [Advanced Topics](#docs-adv-userguide--advanced) - provides references to
other features.

In this (first) section, we will learn how to write and deploy Web
services using Axis2. All the samples mentioned in this guide are located in
the **"samples/userguide/src"** directory of [Axis2 standard binary
distribution](https://axis.apache.org/axis2/java/core/download.cgi).

Please deploy axis2.war in your servlet container and ensure that it works
fine. The [Installation
Guide](#docs-installationguide) gives you step-by-step instructions on just how to build axis2.war
and deploy it in your servlet container.

## Creating a New Web Service

If you are interested in how to write a Web Service client using Axis2, it
is described under [Writing a Web Service Client](#docs-adv-userguide--client). Axis2
provides two ways to create new Web Services, using **code
generation** and using **XML based primary APIs**. The
following section explains how to start from a WSDL, and create a new service
with code generation. For the XML based primary API, please refer to the
section [Writing Web Services Using Axis2's
Primary APIs](#docs-xmlbased-server) for more information. However, if you are a new user, it is
better to follow the code generation approach first (given below)

### Starting with WSDL, Creating and Deploying a Service

We start with a WSDL, however if you do not have a WSDL and need to create
a WSDL from a java class, please use the [Java2WSDL tool](#docs-reference--wsdl2java) to create the WSDL. As you
might already know, a WSDL description of a service provides a precise
definition of that web service. Axis2 can process the WSDL and generate java
code that does most of the work for you. At the server side, we call them
Skeletons, and at the client side, Stubs.

This method of writing a Web service with Axis2 involves four steps:

1. Generate the skeleton code.
2. Add business logic.
3. Create a \*.aar archive (Axis Archive) for the Web service.
4. Deploy the Web service.

### Step1: Generate Skeleton Code

To generate the skeleton and required classes, you can use the WSDL2Java
tool provided in Axis2. This tool is located in the bin directory of the
distribution and can be executed using the provided scripts (.bat or .sh).
The tool's parameter list can be found in the [Axis2 Reference Document](#docs-reference--wsdl2code).

The parameters for the wsdl2java tool in our example are as follows.
Please note that, for this example, we are using xmlbeans as the data binding framework, and the generated
code will be placed in a "samples" directory.

```
wsdl2java.sh -uri ../samples/wsdl/Axis2SampleDocLit.wsdl -ss -sd -d xmlbeans 
-o ../samples -p org.apache.axis2.userguide
```

This will generate the required classes in the **"sample/src"**
directory, and the schema classes in the
**"samples/resources/schemaorg\_apache\_xmlbeans"**
directory. Note that these are not source files and should
be available in the class path in order to compile the generated classes.

### Step 2: Implement Business Logic

Now you should fill the business logic in the skeleton class. You can find
the skeleton class -Axis2SampleDocLitServiceSkeleton.java- among the
generated classes in the
**"samples/src/org/apache/axis2/userguide** directory. Let's
fill the `echoString(..)` method in the skeleton as shown below.
Our sample WSDL-Axis2SampleDocLit.wsdl in **"samples/wsdl"**
directory has three operations: echoString, echoStringArray, echoStruct. To
see how the others will look when they are filled up, see [Code Listing For
Axis2SampleDocLitService Service](https://axis.apache.org/axis2/java/core/docs/src/Axis2SampleDocLitServiceCode.html)

```
public org.apache.axis2.userguide.xsd.EchoStringReturnDocument 
    echoString(org.apache.axis2.userguide.xsd.EchoStringParamDocument param4) throws Exception {
    //Use the factory to create the output document.
    org.apache.axis2.userguide.xsd.EchoStringReturnDocument retDoc = 
           org.apache.axis2.userguide.xsd.EchoStringReturnDocument.Factory.newInstance();
    //send the string back.
    retDoc.setEchoStringReturn(param4.getEchoStringParam());
   return retDoc;
```

### Step 3: Create Archive File

An Axis2 service must be bundled as a service archive. The next step is to
package the classes in an .aar (axis2 archive) and deploy it in Axis2. There
is an ant file generated with the code; it will generate the Axis2 service
archive for you. However, if you do not want to use ant, you can create an
archive with the following steps :

1. Compile the generated code.
2. Copy **"resources/schemaorg\_apache\_xmlbeans**" xmlbeans
   classes to your class folder.
3. Among the generated files, there will be a services.xml file, which is
   the deployment descriptor for Axis2 service.[[learn more about it](#docs-reference--servicedd)]. Copy the
   resources/service.xml to META-INF/services.xml

(To write your own service.xml file, see the sub section in [Writing Web
Services Using Axis2's Primary APIs](#docs-xmlbased-server--step2_.3awrite_the_services_xml_file) )

4. Create the archive using content of the class folder. Change the
   directory to the class folder and run `jar -cf
   <service-name>.aar` to create the archive.

Once the archive is created, the content of the JAR should look like
this:

![](assets/images/directorystructure_151b6bd5c19f0119.jpg)

### Step 4: Deploy Web Service

The service can be deployed by simply dropping the ".aar" file into the
"services" directory in "/webapps/axis2/WEB-INF" of your servlet container.
We recommend using [Apache Tomcat](http://tomcat.apache.org/) as
the servlet container. **Please Note that the services directory is
available only after axis2.war has been exploded by Tomcat. However, the easiest
way to do it is to start Tomcat after axis2.war is copied to the webapps
directory** (if you have not already started it). Check the "Services"
link on the [Home page
of Axis2 Web Application](http://localhost:8080/axis2/) (http://localhost:8080/axis2) and see whether
the Axis2SampleDocLitService is displayed under the deployed services.

We recommend using the exploded configuration to deploy Axis2 WAR in
**WebLogic and WebSphere** application servers to support the
hotupdate/hotdeployment features of Axis2. See [Application Server Specific
Configuration Guide](#docs-app_server--weblogic_websphere) for details.

Note: Axis2 provides an easy way to deploy Web Services using the "Upload
Service" tool in the Axis2 Web Application's Administration module. (See the
[Web Administration Guide](#docs-webadminguide) for
more information)

## Writing a Web Service Client

Axis2 also provides a more complex, yet powerful XML based client API
which is intended for advanced users. Read [Writing Web
Service Clients Using Axis2's Primary APIs](#docs-dii) to learn more about it.
However, if you are a new user, we recommend using the **code
generation** approach presented below.

### Generate Stubs

Let's see how we could generate java code (Stub) to handle the client side
Web Service invocation for you. This can be done by running the WSDL2Java
tool using the following arguments

```
wsdl2java.sh -uri ../samples/wsdl/Axis2SampleDocLit.wsdl -d xmlbeans 
     -o ../samples/src -p org.apache.axis2.userguide
```

This will generate client side stubs and xmlbeans types for your types.
The Stub class that you need to use will be of the form
**<service-name>Stub**. In our example, it will be called
"Axis2SampleDocLitServiceStub.java"

Axis2 clients can invoke Web Services both in a blocking and non-blocking
manner. In a blocking invocation, the client waits till the service performs
its task without proceeding to the next step. Normally, the client waits till
the response to its particular request arrives. In a non-blocking invocation, the client proceeds to the next step immediately, and the responses (if any)
are handled using a Callback mechanism. Please note that some explanations
use the terms Synchronous and Asynchronous to describe the similar invocation
strategies.

### Do a Blocking Invocation

The following code fragment shows the necessary code calling
`echoString` operation of the
`Axis2SampleDocLitService` that we have already deployed. The code
is extremely simple to understand and the explanations are in the form of
comments.

```
     try {
               org.apache.axis2.userguide.Axis2SampleDocLitServiceStub stub 
                  = new org.apache.axis2.userguide.Axis2SampleDocLitServiceStub(null,
                    "http://localhost:8080/axis2/services/Axis2SampleDocLitService");
                //Create the request document to be sent.
                org.apache.axis2.userguide.xsd.EchoStringParamDocument reqDoc =
                org.apache.axis2.userguide.xsd.EchoStringParamDocument.Factory.newInstance();
                reqDoc.setEchoStringParam("Axis2 Echo");
                //invokes the Web service.
                org.apache.axis2.userguide.xsd.EchoStringReturnDocument resDoc = 
                stub.echoString(reqDoc);
                System.out.println(resDoc.getEchoStringReturn());
               } catch (java.rmi.RemoteException e) {
                  e.printStackTrace();
              }
```

First argument of `Axis2SampleDocLitPortTypeStub` should be the
Axis2 repository for the client. Here we use null to make the stub use
default configurations. However, you can make Axis2 use your own repository
by providing it here. You can find more information about this from the [Axis2 Configuration section](#docs-adv-userguide--config). You can find code to invoke
other operations from [Code
Listing For Axis2SampleDocLitService Service](https://axis.apache.org/axis2/java/core/docs/src/Axis2SampleDocLitServiceCode.html)

### Do a Non-Blocking Invocation

The stubs also include a method that allows you to do a non-blocking
innovation. For each method in the Service, there will be a method
**start<method-name>**. These methods accept a callback
object, which would be called when the response is received. Sample code that
does an asynchronous interaction is given below.

```
try {
         org.apache.axis2.userguide.Axis2SampleDocLitServiceStub stub
           = new org.apache.axis2.userguide.Axis2SampleDocLitServiceStub(null,
             "http://localhost:8080/axis2/services/Axis2SampleDocLitService");
             //implementing the callback online
            org.apache.axis2.userguide.Axis2SampleDocLitServiceCallbackHandler callback =
            new org.apache.axis2.userguide.Axis2SampleDocLitServiceCallbackHandler() {
                    public void receiveResultechoString(
                      org.apache.axis2.userguide.xsd.EchoStringReturnDocument resDoc) {
                       System.out.println(resDoc.getEchoStringReturn());
                       }
            };
        org.apache.axis2.userguide.xsd.EchoStringParamDocument reqDoc = 
          org.apache.axis2.userguide.xsd.EchoStringParamDocument.Factory.newInstance();
           reqDoc.setEchoStringParam("Axis2 Echo");
           stub.startechoString(reqDoc, callback);
        } catch (java.rmi.RemoteException e) {
          e.printStackTrace();
       }
```

Even though the above code does a non-blocking invocation at the client
API, the transport connection may still operate in a blocking fashion. For
example, a single HTTP connection can be used to create a Web Service request
and to get the response when a blocking invocation happens at the transport
level. To perform a "true" non-blocking invocation in which two separate
transport connections are used for the request and the response, please add
the following code segment after creating the stub. It will force Axis2 to
use two transport connections for the request and the response while the
client uses a Callback to process the response.

```
stub._getServiceClient().engageModule(new QName("addressing"));
stub._getServiceClient().getOptions().setUseSeparateListener(true);
```

Once those options are set, Axis2 client does the following:

1. Starts a new Transport Listener(Server) at the client side.
2. Sets the address of the Transport Listener, as the ReplyTo
   WS-Addressing Header of the request message
3. According to the WS-Addressing rules, the Server will process the
   request message and send the response back to the ReplyTo address.
4. Client accepts the response, processes it and invokes the callback with
   the response parameters.

### Using Your Own Repository

You can also use your own repository with an Axis2 Client. The code below shows how
to do this.

```
String axis2Repo = ...
String axis2xml = ...
ConfigurationContext configContext =
ConfigurationContextFactory.createConfigurationContextFromFileSystem(axis2Repo, axis2xml);
Service1Stub stub1 = new Service1Stub(configContext,...);
//invoke Service1
Service2Stub stub2 = new Service2Stub(configContext,...);
//invoke Service2
```

Note by creating the `ConfigurationContext` outside and passing
it to the stubs, you could make number of stubs to use same repository, thus
saving the configuration loading overhead from each request.

## Configuring Axis2

### Axis2 Repository

Axis2 configuration is based on a repository and standard archive format.
A repository is a directory in the file system, and it should have the
following:

1. **axis2.xml**, the Axis2 global deployment descriptor in
   conf/axis2.xml file
2. **services** directory, which will have the service
   archives
3. **modules** directory (optional), which will have the
   module archives

Both services and modules will be identified and deployed once their
archives are copied to the corresponding directories. At the server side, users should specify the repository folder at the time of starting the Axis2
Server (e.g. HTTP or TCP). In Tomcat, `webapps/axis2/WEB-INF`
folder acts as the repository. At the client side, binary distribution can
itself be a repository. You can copy the conf directory which includes the
axis2.xml file from the exploded axis2.war and edit it to change the global
configurations repository.

### Global Configurations

The Global configuration can be changed by editing the axis2.xml file, refer to the [Axis2
Configuration Guide](#docs-axis2config--global_configuration) for more information.

### Add New Services

New services can be written either using WSDL based code generation as we
did, or from scratch as explained in [Writing
Web Services Using Axis2's Primary APIs](#docs-xmlbased-server). Read [Creating a Service from Scratch](#docs-xmlbased-server) for more
information. Also refer to [Axis2 Configuration Guide](#docs-axis2config--service_configuration)
for a reference on **services.xml** file.

### Engaging Modules

Each module(.mar file) provides extensions to Axis2. A module can be
deployed by copying it to the modules directory in the repository. Then it
becomes available and can be engaged at a global, service or operation scope.
Once engaged, it becomes active (adds handlers to the execution flow) at the
respective scope. Please refer to [Axis2
architecture guide](#docs-axis2architectureguide) for detailed explanation. The following table explains
the semantics of scope, and how to engage modules in those scopes.

| Scope | Semantics | How to Engage |
| --- | --- | --- |
| Global | Add handlers in the module to all the services. Addressing Handler can be only engaged as global | By adding a <module ref="addressing"/> to the Axis2 xml file or calling `stub._getServiceClient().engageModule(moduleName)` at client side |
| Service | Add handlers in the module to a specific service | By adding a <module ref="addressing"/> to a service.xml file in a service archive |
| Operation | Add handlers in the module to a specific operation | By adding a <module ref="addressing"/> inside an operation tag of a service.xml file in a service archive |

\* If a handler is added to a service or an operation, it will be invoked
for every request received by that service or operation

Axis2 provides a number of built in Modules (such as addressing,Security, WS-Reliable
Messaging), and they can be engaged as shown above. Please refer to each
module on how to use and configure them. You can also [create your own modules with Axis2](#docs-modules). Also refer to [Axis2 Configuration Guide](#docs-axis2config--global_configuration)
for a reference on the module.xml file.

### WS-Addressing Support

WS-Addressing support for Axis2 is implemented by the addressing module.
To enable addressing, you need to engage the addressing module in both server
and client sides.

1. To **enable** addressing at the server side, you need to
   copy the addressing.mar file to the modules directory of the server's
   axis2 repository. To engage the module, add a <module
   ref="addressing"/> to axis2.xml. The **Addressing module can be
   engaged only at global level.**
2. To **enable** addressing at the client side, you should
   add it to the repository and provide the repository as an argument to the
   [ServiceClient](#docs-dii) or [generated
   stub](#docs-adv-userguide--client) or have it in your classpath.
3. To **engage** the addressing module, you should either add
   <module ref="addressing"/> to the axis2.xml file at the client side
   or call
   `stub._getServiceClient().engageModule(moduleName)`

## Advanced Topics

### Transports

By default, Axis2 is configured to use HTTP as the transport. However, Axis2 supports HTTP, SMTP, TCP and JMS transports. You can also write your
own transports, and deploy them by adding new transportReceiver or
transportSender tags to axis2.xml. To learn how to configure and use
different transports, please refer to the following documents.

1. [HTTP Transports](#docs-http-transport)
2. [WS-Commons Transport project](http://ws.apache.org/commons/transport/)

### Attachments

Axis2 provides attachment support using [MTOM](http://www.w3.org/TR/soap12-mtom/). Please refer to [MTOM with Axis2](#docs-mtom-guide) for more
information.

### Security

WS-Security support for Axis2 is provided by [Apache Rampart](http://axis.apache.org/axis2/java/rampart/).

### REST Web Service

Please refer to [RESTful Web
Services](#docs-rest-ws) for more information.

### Pluggable Data Binding

Axis2 ships with Axis Data Binding(ADB) as the default data binding
framework. However, data binding frameworks are pluggable to Axis2, and
therefore you can use other data binding frameworks with Axis2. Please refer
to the following documents for more information.

#### Axis2 Data Binding(ADB)

1. [Axis2 Databinding
   Framework](#docs-adb-adb-howto)
2. [ADB
   Integration With Axis2](#docs-adb-adb-codegen-integration)
3. [Advanced Axis2 Databinding Framework
   Features](#docs-adb-adb-advanced)
4. [ADB Tweaking Guide](#docs-adb-adb-tweaking)

#### JiBX

[JiBX Integration With Axis2](#docs-jibx-jibx-codegen-integration)

### Other Topics

1. [Axis2 Integration With The Spring
   Framework](#docs-spring)
2. [Web Services Policy Support In
   Axis2](#docs-ws_policy)
3. [Axis2 Configuration
   Guide](#docs-axis2config--global_configuration)
4. [Axis2 RPC Support](#docs-axis2-rpc-support)
5. [Migrating from Apache Axis 1.x to Axis
   2](#docs-migration)
6. [Writing your Own Axis2 Module](#docs-modules)
7. [Using the SOAP Monitor](#docs-soapmonitor-module)
8. [Writing Web Services Using Axis2's
   Primary APIs](#docs-xmlbased-server)
9. [Writing Web Service Clients Using Axis2's Primary
   APIs](#docs-dii)
10. [Application Server Specific Configuration
    Guide](#docs-app_server)

---

<a id="docs-axis2config"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/axis2config.html -->

<!-- page_index: 8 -->

# Axis2 Configuration Guide

In Axis2, there are three kinds of configuration files to configure the
system. The first one is to configure the whole system (global
configuration), the second one is to configure a service (service
configuration), and the third one is to configure a module (module
configuration). This document explains the above configurations in detail.

## Content

- [Global Configuration
  (axis2.xml)](#docs-axis2config--global_configuration)
- [Service Configuration
  (services.xml)](#docs-axis2config--service_configuration)
- [Module Configuration
  (module.xml)](#docs-axis2config--module_configuration)

## Global Configuration (axis2.xml)

All the configurations that require starting Axis2 are obtained from
axis2.xml. The way to specify them is extremely simple and easy. The document
is all about the proper way of specifying the configurations in axis2.xml, which
is located at AXIS2\_HOME/conf. There are six top level elements that
can be seen in the configuration file inside the root element,
<axisconfig name="AxisJava2.0"> and can be listed as follows:

- [Parameter](#docs-axis2config--parameter)
- [Transport Receiver](#docs-axis2config--receiver)
- [Transport Sender](#docs-axis2config--sender)
- [Phase Order](#docs-axis2config--phase_order)
- [Module References](#docs-axis2config--references)
- [Listeners (Observers)](#docs-axis2config--listeners)

### Parameter

In Axis2, a parameter is nothing but a name-value pair. Each and every top
level parameter available in the axis2.xml (direct sub elements of the root
element) will be transformed into properties in AxisConfiguration. Therefore, the top level parameters in the configuration document can be accessed via
AxisConfiguration in the running system. The correct way of defining a
parameter is shown below:

```
<parameter name="name of the parameter" >parameter value </parameter>
```

### Transport Receiver

Depending on the underlying transport on which Axis2 is going to run, you
need to have different transport receivers. The way you add them to the
system is as follows:

```
<transportReceiver name="http" class="org.apache.axis2.transport.http.SimpleHTTPServer">
    <parameter name="port" >6060</parameter>
</transportReceiver>
```

The above elements show how to define transport receivers in
axis2.xml. Here the "name" attribute of the <transportReceiver/> element identifies the
type of the transport receiver. It can be HTTP, TCP, SMTP, etc.
When the system starts up or when you set the transport at the client side, you can use these transport names to load the appropriate transport. The "class"
attribute is for specifying the actual java class that will implement the required
interfaces for the transport. Any transport can have zero or more parameters, and any parameters given can be accessed via the corresponding
transport receiver.

### Transport Sender

Just like the transport receivers, you can register transport senders in the
system, and later at run time, the senders can be used to send the messages.
For example, consider Axis2 running under Apache Tomcat. Then Axis2 can use
TCP transport senders to send messages rather than HTTP. The method of
specifying transport senders is as follows:

```
 
<transportSender name="http" class="org.apache.axis2.transport.http.impl.httpclient5.HTTPClient5TransportSender">
        <parameter name="PROTOCOL" locked="xsd:false">HTTP/1.0</parameter>
 </transportSender> 
 
```

**name:** Name of the transport (you can have HTTP and HTTP1 as
the transport name)

**class:** Implementation class of the corresponding
transport.

Just like the transport receivers, transport senders can have zero
or more parameters, and if there are any, they can be accessed via the
corresponding transport sender.

### Phase Order

Specifying the order of phases in the execution chain has to be done using
the phase order element. It will look as follows:

```
<phaseOrder type="InFlow">
         <phase name="TransportIn"/>
         .
         .
</phaseOrder>   
```

The most interesting thing is that you can add handlers here as well. If
you want to add a handler that should go into that phase, you can directly do
that by adding a handler element into it. In addition to that, there is no
hard coding work for the handler chain anywhere in Axis2 (at any Axis\*). So
all those configurations are also done in the phase order element. The
complete configurations will look as follows:

```
<phaseOrder type="InFlow">
        <!--   Global phases    -->
         <phase name="Transport">
            <handler name="RequestURIBasedDispatcher"
                     class="org.apache.axis2.dispatchers.RequestURIBasedDispatcher">
                <order phase="Transport"/>
            </handler>

            <handler name="SOAPActionBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPActionBasedDispatcher">
                <order phase="Transport"/>
            </handler>
        </phase>
        <phase name="Security"/>
        <phase name="PreDispatch"/>
        <phase name="Dispatch" class="org.apache.axis2.engine.DispatchPhase">
            <handler name="AddressingBasedDispatcher"
                     class="org.apache.axis2.dispatchers.AddressingBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPMessageBodyBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPMessageBodyBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="InstanceDispatcher"
                     class="org.apache.axis2.engine.InstanceDispatcher">
                <order phase="Dispatch"/>
            </handler>
        </phase>
        <!--   Global phases   -->
        <!--   After the Dispatch phase module author or service author can add any phase he wants    -->
        <phase name="OperationInPhase"/>
    </phaseOrder>
    <phaseOrder type="OutFlow">
        <!--   user can add his own phases to this area  -->
        <phase name="OperationOutPhase"/>
        <!--  Global phases  -->
        <!--  these phases will run irrespective of the service  -->
        <phase name="MessageOut"/>
        <phase name="PolicyDetermination"/>
    </phaseOrder>
    <phaseOrder type="InFaultFlow">
        <phase name="PreDispatch"/>
        <phase name="Dispatch" class="org.apache.axis2.engine.DispatchPhase">
            <handler name="RequestURIBasedDispatcher"
                     class="org.apache.axis2.dispatchers.RequestURIBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPActionBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPActionBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="AddressingBasedDispatcher"
                     class="org.apache.axis2.dispatchers.AddressingBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPMessageBodyBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPMessageBodyBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="InstanceDispatcher"
                     class="org.apache.axis2.engine.InstanceDispatcher">
                <order phase="Dispatch"/>
            </handler>
        </phase>
        <!--      user can add his own phases to this area  -->
        <phase name="OperationInFaultPhase"/>
    </phaseOrder>
    <phaseOrder type="OutFaultFlow">
        <!--      user can add his own phases to this area  -->
        <phase name="OperationOutFaultPhase"/>
        <phase name="PolicyDetermination"/>
        <phase name="MessageOut"/>
    </phaseOrder>
```

**type:** the attribute represents the type of the flow. It
can only be one of the following:

- InFlow
- OutFlow
- InFaultFlow
- OutFaultFlow

In addition to that, the only child element that is allowed inside
"phaseOrder" is the "phase" element which represents the available phases in
the execution chain. The method of specifying phases inside "phaseOrder" is
as follows:

```
<phase name="Transport"/>
```

**name:** Name of the phase.

There are a number of things that one has to keep in mind when changing a
phaseOrder:

For the phaseOrder types **"InFlow"** and
**"InFaultFlow"**

- All the phases that are above the "Dispatch" phase, including the
  "Dispatch" phase, are known as "Global phases" . You can add any number
  of new phases here and they will be considered global.
- In these two phaseOrder types, the phases added after the "Dispatch"
  phase are known as "Operation phases".

For the phaseOrder types **"OutFlow"** and
**"OutFaultFlow"**

- All the phases that are below the "MessageOut" phase, including the
  "MessageOut" phase, are known as "Global phases". You can add new phases
  according to your requirement.
- The phases added before the "MessageOut" phase are known as "Operation
  phases".

**Note :** If you look closely at the default axis2.xml, you will be able to clearly identify it.

### Module References

If you want to engage a module, system wide, you can do it by adding a top
level module element in axis2.xml. It should look as follows:

```
<module ref="addressing"/>
```

**ref:** the module name which is going to be engaged, system
wide.

### **Listeners (Observers)**

In Axis2, AxisConfiguration is observable so that you can register
observers into that. They will be automatically informed whenever a change
occurs in AxisConfiguration. In the current implementation, the observers are
informed of the following events:

- Deploying a Service
- Removing a service
- Activate/Inactivate Service
- Module deploy
- Module remove

Registering Observers is very useful for additional features such as RSS
feed generation, which will provide service information to subscribers. The
correct way of registering observers should as follows:

```
<listener class="org.apache.axis2.ObserverIMPL">
    <parameter name="RSS_URL" >http://127.0.0.1/rss</parameter>
</listener>
```

**class:** Represents an Implementation class of observer, and it should be noted that the Implementation class should implement
AxisObserver interface, and the class has to be available in the classpath.

## Service Configuration (services.xml)

The description of services are specified using services.xml. Each
service archive file needs to have a services.xml in order to be a valid
service and it should be available in the META-INF directory of the archive
file(aar) which should be located in AXIS2\_HOME/repository/services in
standalone use. In war distribution this will be axis2/WEB-INF/services
inside the servlet container. A very simple services.xml is shown below:

```

<service name="name of the service" scope="name of the scope" 
    class="fully qualified name the service lifecycle class"   
    targetNamespace="target namespace for the service">
    
    <description> The description of the service  </description>  

    <transports> 
        <transport>HTTP</transport>
    </transports>
    
    <schema schemaNamespace="schema namespace"/> 
     
    <messageReceivers>
            <messageReceiver mep="http://www.w3.org/ns/wsdl/in-out"
                             class="org.apache.axis2.rpc.receivers.RPCMessageReceiver"/>
    </messageReceivers>
     
    <parameter name="ServiceClass" locked="xsd:false">org.apache.axis2.sample.echo.EchoImpl</parameter>
    
    <operation name="echoString" mep="operation MEP"> 
        <actionMapping>Mapping to action</actionMapping>
        <module ref=" a module name "/>
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
</service>
```

**name**: The service name will be the name of the archive
file if the .aar file contains only one service, or else the name of the
service will be the name given by the name attribute.

**scope**: (Optional Attribute) The time period during which
runtime information of the deployed services will be available. Scope is of
several types- "application", "soapsession", "transportsession", "request".
The default value (if you don't enter any value) will be "request"

**class**: (Optional attribute) The full qualified name of
the service lifecycle implementation class. ServiceLifeCycle class is useful
when you want to do some tasks when the system starts and when it
shuts down.

**targetNamespace**: (Optional Attribute) Target name space
of the service. This value will be used when generating the WSDL. If you do
not specify this value, the value will be calculated from the package name of
the service impl class.

**Description**: (Optional) If you want to display any
description about the service via Axis2 web-admin module, then the
description can be specified here.

**transports** : (Optional) The transports to which the
service is going to be exposed. If the transport element is not present, then
the service will be exposed in all the transports available in the system.
The transport child element specifies the transport prefix (the name of the
transport specified in axis2.xml).

**parameters:** A services.xml can have any number of top level
parameters and all the specified parameters will be transformed into service
properties in the corresponding AxisService. There is a compulsory parameter
in services.xml called ServiceClass that specifies the Java class, which
performs the above transformation. This class is loaded by the
MessageReceiver.

**operations :** If the service impl class is Java, then all the public
methods in that service will be exposed. If the user wants to override it, he
has to add the "operation" tag and override it. In a non-Java scenario or if
you do not have a service class, then all the operations the user wants to
expose by the service has to be indicated in the services.xml. It is
specified as follows:

```
    
<operation name="echoString">
   <module ref=" a module name "/>
   <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
</operation>
```

The only compulsory attribute here is "name", which represents the
operation name that is going to be exposed. Any operation can contain module
references as well as any number of parameters. The most interesting thing is
that you can register custom message receivers per operation. Then the
registered message receiver will be the message receiver for the
corresponding operation. If you do not specify the message receiver, then the
default message receiver will perform the operation.

## Module Configuration (module.xml)

The description of the module is specified using the module.xml. Each
module archive file needs to have a module.xml in order to be a valid module, and it should be available in the META-INF directory of the archive file(mar)
which should be located in AXIS2\_HOME/repository/modules in standalone use.
In war distribution this will be axis2/WEB-INF/modules inside the servlet container.

A very simple module.xml is shown below:

```

<module class="org.apache.module.Module1Impl">
    <InFlow>
        .
        .
    </InFlow>
    <OutFlow>
        .
        .
    </OutFlow>

    <OutFaultFlow>
        .   
        .
    </OutFaultFlow>

    <InFaultFlow>
        .         
        .
    </InFaultFlow>

    <operation name="creatSeq" mep="MEP_URI_IN_OUT">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
        <parameter name="para1" locked="xsd:true">10</parameter>
    </operation>
</module>
```

**class:** (Optional attribute) Indicates the module
implementation class. A module may or may not contain a module implementation
class since the module can also be a collection of handlers. If a module
contains an implementation class that implements the
org.apache.axis2.modules.Module interface at deployment, its
`init();` method will be called.

**parameter:** A module can contain any number of parameters and all
the listed parameters in the module.xml will be transformed into the
corresponding AxisModule of the module.

**flow:** Defining of handlers in a module has to be done inside flows.
There are four types of flows as listed below.

You can add any number of handlers into a flow, and those handlers will be
available in the corresponding chains at runtime, when they are engaged.

- InFlow
- OutFlow
- InFaultFlow
- OutFaultFlow

**operations:**  If a module wants to add an operation when it is
engaged into a service, it can be done by adding an operation tag in
module.xml. The method of specifying the operation is the same as operation
in services.xml.

**handler:** The Handler element consists of compulsory and optional
attributes. The method of defining a handler will look as follows:

```
<handler name="handler1" class="handlerClass ">
            <order phase="userphase1" />
</handler>
```

***Compulsory Attributes***
**name:** Name of the handler.
**class:** Handler implementation class.
**phase:** Name of the phase that the handler should remain, in the
execution chain.
***Optional Attributes :***
**phaseLast:** Indicates that the handler is the last handler of the
phase.
**phaseFirst:** Indicate that the handler is the first handler of the
phase.
**before :** Indicates that the current handler should be invoked before
the handler specified by the before handler
**after:** Indicates that the current handler should be invoked after the
handler specified by the after handler

---

<a id="docs-webadminguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/webadminguide.html -->

<!-- page_index: 9 -->

# Apache Axis2 Web Administrator's Guide

This document gives you detailed information on the
administration console of the Apache Axis2 Web application. Apache
Axis2 Administration is all about configuring Apache Axis2 at run
time, where the configuration is transient.

*Send your feedback to: [java-dev@axis.apache.org](mailto:java-dev@axis.apache.org?subject=[Axis2])*.
(Subscription details are available on the [Axis2 site](#mail-lists).)
Kindly prefix every email subject with [Axis2].

## Contents

- [Introduction](#docs-webadminguide--intro)
  - [Login into Administration Site](#docs-webadminguide--login)
- [Administration Options](#docs-webadminguide--adminoptions)
  - [Tools](#docs-webadminguide--tools)

    - [Upload Service](#docs-webadminguide--upservice)
  - [System components](#docs-webadminguide--syscomponents)

    - [Available services](#docs-webadminguide--heading1)
    - [Available service groups](#docs-webadminguide--servgroups)
    - [Available modules](#docs-webadminguide--avmodules)
    - [Globally engaged modules](#docs-webadminguide--globalmodules)
    - [Available phases](#docs-webadminguide--phases)
  - [Execution chains](#docs-webadminguide--executionchains)

    - [Global chains](#docs-webadminguide--globalchains)
    - [Operation specific chains](#docs-webadminguide--operationchains)
  - [Engage module](#docs-webadminguide--engaginmodule)
  - [Services](#docs-webadminguide--services)
    - [Deactivate Service](#docs-webadminguide--turnoffservice)
    - [Activate Service](#docs-webadminguide--turnonservice)
    - [Edit service parameters](#docs-webadminguide--editservicepara)
  - [Contexts](#docs-webadminguide--context)

    - [View Hierarchy](#docs-webadminguide--viewhierarchy)

### Introduction

The Apache Axis2 Web application has three main sections:
'Services' lists all the available services deployed in this
server, 'Validate' checks the system to see whether all the
required libraries are in place and views the system information, and 'Administration' is the Axis2 Web Administration module which
is the console for administering the Apache Axis2 installation.

The Axis2 Web Administration module provides a way to configure
Axis2 dynamically. It's important to note that this dynamic
configuration will NOT be persistent, i.e., if the servlet
container is restarted, then all the dynamic configuration changes
will be lost.

#### Log on to the Administration Site (DISABLED BY DEFAULT)

Once Apache Axis2 is successfully installed, the Web application
can be accessed (see [Installation
Guide](#docs-installationguide) for instructions). From the [Axis2 Web
Application Home page](#docs-webadminguide--homepage) you can go to the Administration page by
clicking the 'Administration' link. The Login page shown below will
appear requesting the user name and password. The default user name
and password are undefined by default as the values are blank
in the axis2.xml file. You must edit the axis2.xml to enable a login
by defining a username and password. Below is an arbitrary example.
The username is 'admin' (without quotes) and the password is 'axis2'
(without quotes).

![](assets/images/adminlogin_b3c6c2e2a41e18d8.jpg)

You can change the user name and password values by changing the
following two parameters in the axis2.xml as required.

![](assets/images/parameters_da908336455a03b9.jpg)

If the log on is successful, you will see the screen below. This
is where you can view the configuration and the status of the
running system and dynamically configure it.

![](assets/images/admin_004957568f051413.jpg)

### Administration Options

**Tools**

- [Upload Service](#docs-webadminguide--upservice)

**System
components**

- [Available services](#docs-webadminguide--heading1)
- [Available service groups](#docs-webadminguide--servgroups)
- [Available modules](#docs-webadminguide--avmodules)
- [Globally engaged modules](#docs-webadminguide--globalmodules)
- [Available phases](#docs-webadminguide--phases)

**Execution
chains**

- [Global chains](#docs-webadminguide--globalchains)
- [Operation specific chains](#docs-webadminguide--operationchains)

**[Engage module](#docs-webadminguide--engaginmodule)**

- For all Services
- For a Service Group
- For a Service
- For an Operation

**Services**

- [Deactivate service](#docs-webadminguide--turnoffservice)
- [Activate service](#docs-webadminguide--turnonservice)
- [Edit service parameters](#docs-webadminguide--editservicepara)

**Contexts**

- [View Hierarchy](#docs-webadminguide--viewhierarchy)

### Apache Axis2 Web Application Home Page

**![](assets/images/clip-image006_c10a6267117859bb.jpg)**

### Upload Services

You can upload packaged Apache Axis2 service archive files using
this page. This can be done in two simple steps:

- Browse to the location and select the axisService archive file
  you wish to upload
- Then click Upload

![](assets/images/clip-image010_33e6bbf8fc6f0a24.jpg)

### Available Services

The functionality of the 'Available Services' option is almost
the same as the functionality of the 'Services' option on the Axis2
Web Application Home page, where it displays a list of deployed
services and their operations. As an additional feature, the
'Available Services' page lists details of modules that are engaged
to the deployed services and their operations on a global, service
or on an operation level.

Using the 'Disengage' link, you can disengage the corresponding
module as long as the module is not globally engaged (i.e., engaged
to all the services and operations).

Click on a specific service and it will give you the WSDL file
of that particular service.

**Faulty services** of this system will also be
listed on this page. Click on a faulty service to view a page that
lists the exception stack trace of the exception, which caused the
service to be faulty.

![](assets/images/adminmain_2bc0c5757498c011.jpg)

### Available Service Groups

Service group is a logical collection of related services, and
the 'Available Service Groups' link will list all the available
service groups in the system.

![](assets/images/servicegroups_273beb3e726548d6.jpg)

### Available Modules

To view the available modules in the 'modules' directory of the
repository, click 'Available Modules'. This will show you all the
available modules in the system. Those modules can be engaged
dynamically.

![](assets/images/modules_5e2426156b4b63c6.jpg)

### Globally Engaged Modules

Click the 'Globally Engaged Modules' to view the globally
engaged modules, if any. If a module is engaged globally, then the
handlers that belong to that module will be executed irrespective
of the service.

### Available Phases

The 'Available Phases' link will display all the available
phases. In Axis2, there are two levels of phases:

- System predefined phases (not allowed to be changed)
- User defined phases

The main difference between these two levels is that system
predefined phases will be invoked irrespective of the services, while the user defined phases will be invoked when the dispatcher
finds the operation. Note that it is essential for module
developers and service writers to have a good understanding of
phases and phase ordering.

![](assets/images/viewphases_74cdb0a75182b059.jpg)

### Global Chains

The 'Global Chains' link will display all the Global Execution
Chains. The most interesting feature of the Axis2 Web
Administration Module is that it provides a very basic method of
viewing the global phase list and handlers inside the phases
depending on both the phase and handler orders. This kind of
information is extremely useful in debugging the system, as there
is no other way to list out handlers in the global chains. If you
engage a new module, the new handlers will be added to the global
chains and will be displayed on this page.

![](assets/images/globalchain_a407535875dfed8e.jpg)

### Operation Specific Chains

The 'Operation Specific Chains' link can be used to view the
handlers corresponding to a given service in the same order as it
is in the real execution chain.

![](assets/images/select-service-for-handler_d9a2782ebc654d17.jpg)

Select the service of whose service handlers you wish to view
from the list, and click 'View' to view the handlers. The page
below shows the service handlers of the service
*version*

![](assets/images/servicehandlers_60900117ef754bef.jpg)

### Engaging Modules

The 'Engaging Modules' link allows you to engage modules either
globally (to all services), to a service group, to a service, or to
an operation depending on the module implementation. If the module
was designed to engage the handlers globally, then the handlers in
the module can be included in any phase in the system. It can be
either a system predefined phase or a user defined phase.

On the other hand, if the module was implemented in such a way
that it is going to be deployed to a service or to an operation, then the module cannot be included in any of the [System Predefined Phases](#docs-webadminguide--phases). Thus it can only be
included in [User Defined Phases](#docs-webadminguide--phases).

Immediately after engaging the module, you can see the status of
the engagement indicating whether it is engaged properly or
not.

![](assets/images/moduleengage_3d89799496b2a4c8.jpg)

### Deactivate Service

The 'Deactivate Service' link under the 'Services' list will
lead to the page below. The Deactivate service functionality
provides a way to remove unnecessary services from the running
system, but the removal is transient--which means that if you
restart the system, the service will be active.

To deactivate a service, select a service from the list, select
the 'Deactivate service' check box, and then click 'Deactivate'..
The 'Clear' button will clear the 'Deactivate service' check
box.

![](assets/images/inactivate_aa12520eb55b7636.jpg)

### Activate Service

The 'Activate Service' link under the 'Services' list will lead
to the page below. The Activate service functionality provides a
way to activate services while the system is running, but the
activation is transient-- which means that if you restart the
system, the service will be inactive.

To activate a service, select a service from the list, select
the 'Activate Service' check box, then click 'Activate'. The
'Clear' button will clear the 'Activate service' check box.

![](assets/images/activate_3f6f5a499019afd1.jpg)

### Edit Service Parameters

This functionality provides a way to change the parameters in a
service or its operations. These changes will be transient too, which means if you restart the system, the changes will not be
reflected.

The 'Edit Parameters' link under the 'Services' list (on the
navigation bar) will link to the page where you can select the
services of which you want to edit the parameters. Once the service
is selected, click 'Edit Parameters'.. This will open the page
shown below.

![](assets/images/editserviecpara_b68f9b0ac979a72b.jpg)

### View Hierarchy

By listing the current context hierarchy, the 'View Hierarchy'
link provides a means to look at the system state at run time. This
will list out all the available service group contexts, service
contexts, operation contexts, etc.

---

<a id="docs-axis2architectureguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/Axis2ArchitectureGuide.html -->

<!-- page_index: 10 -->

# Apache Axis2 Architecture Guide

This document gives an introduction to Axis2's modular
architecture with explanations on every module.

## Contents

- [The Big Picture](#docs-axis2architectureguide--bmbp)
- [Requirement of Axis2](#docs-axis2architectureguide--requirements)
- [Axis2 Architecture](#docs-axis2architectureguide--thearchi)
  - [Core Modules](#docs-axis2architectureguide--bmcore)
  - [Other Modules](#docs-axis2architectureguide--bmother)
  - [Information Model](#docs-axis2architectureguide--bminfomod)
  - [XML Processing Model](#docs-axis2architectureguide--bmxml)
  - [SOAP Processing Model](#docs-axis2architectureguide--bmsoappm)

    - [Axis2 Default Processing Model](#docs-axis2architectureguide--default)
    - [Processing an Incoming SOAP
      Message](#docs-axis2architectureguide--incomingsoap)
    - [Processing of the Outgoing Message](#docs-axis2architectureguide--outgoing)
    - [Extending the SOAP Processing Model](#docs-axis2architectureguide--extending)

      - [Extending the SOAP Processing
        Model with Handlers](#docs-axis2architectureguide--extendingwithhandlers)
      - [Extending the SOAP Processing
        Model with Modules](#docs-axis2architectureguide--extendingwithmodules)
  - [Deployment](#docs-axis2architectureguide--bmdeployment)
    - [The *axis2.xml* file](#docs-axis2architectureguide--xmlfile)
    - [Service Archive](#docs-axis2architectureguide--servicearchive)
    - [Module Archive](#docs-axis2architectureguide--modulearchive)
  - [Client API](#docs-axis2architectureguide--bmclientapi)

    - [One Way Messaging Support](#docs-axis2architectureguide--oneway)
    - [Request Response Messaging
      Support](#docs-axis2architectureguide--requestresponse)
  - [Transports](#docs-axis2architectureguide--bmtransports)
  - [Code Generation](#docs-axis2architectureguide--bmwsdl)
  - [Data Binding](#docs-axis2architectureguide--bmdb)
    - [Integration with Code Generation
      Engine](#docs-axis2architectureguide--integration)
    - [Serialization and De-Serialization](#docs-axis2architectureguide--serial)

## The Big Picture

A new architecture for Axis was introduced during the August
2004 Summit in Colombo, Sri Lanka. This new architecture on which
Axis2 is based is more flexible, efficient, and configurable in
comparison to [Axis1.x
architecture](http://ws.apache.org/axis/java/architecture-guide.html). Some well established concepts from Axis 1.x, like handlers etc., have been preserved in this new
architecture.

Any architecture is a result of what that architecture should
yield. The success of an architecture should be evaluated based on
the requirements expected to be met by that architecture. Let us
start our journey into Axis2 by looking at the requirements.

## Requirement of Axis2

In SOAP terminology, a participant who is taking part in a Web
service interaction is known as a SOAP Node. Delivery of a single
SOAP Message is defined based on two participants, SOAP Sender and
SOAP Receiver. Each SOAP message is sent by a SOAP Sender and
received by a SOAP Receiver. A single SOAP delivery is the most
basic unit that builds the Web service interaction.

Each SOAP Node may be written in specific programming language, may it be Java, C++, .NET or Perl, but the Web services allow them
to interoperate. This is possible because on the wire each Web
service interaction is done via SOAP, which is common to every SOAP
Node.

![](assets/images/soap_9f4e5a5d0ee26039.gif)

Web service middleware handles the complexity in SOAP messaging
and lets the users work with the programming language they are
accustomed to. Axis2 allows Java users to invoke Web services using
Java representations, and handles the SOAP messaging behind the
curtain.

Axis2 handles SOAP processing along with numerous other tasks.
This makes life of a Web service developer a whole lot easier.
Following are the identified requirements:

1. Provide a framework to process the SOAP messages. The framework
   should be extensible and the users should be able to extend the
   SOAP processing per service or per operation basis. Furthermore, it
   should be able to model different Message Exchange Patterns (MEPs)
   using the processing framework.
2. Ability to deploy a Web service (with or without WSDL)
3. Provide a Client API that can be used to invoke Web services.
   This API should support both the Synchronous and Asynchronous
   programming models.
4. Ability to configure Axis2 and its components through
   deployment.
5. Ability to send and receive SOAP messages with different
   transports.

Apart from the above functionalities, performance in terms of
memory and speed is a major consideration for Axis2. Axis2 Core
Architecture is built on three specifications- [WSDL](http://www.w3.org/TR/wsdl), [SOAP](http://www.w3.org/TR/soap/) and [WS-Addressing](http://www.w3.org/Submission/ws-addressing/).
Other specifications like JAX-RPC, [SAAJ](http://java.sun.com/webservices/saaj/index.jsp) and
[WS-Policy](http://www.w3.org/Submission/WS-Policy/) are
layered on top of the Core Architecture.

## Axis2 Architecture

Axis2 architecture lays out some principals to preserve the
uniformity. They are as follows:

- Axis2 architecture separates the logic and the states. Code that
  does the processing does not have a state inside Axis2. This allows
  code to be executed freely by parallel threads.
- All the information is kept in one information model, allowing
  the system to be suspended and resumed.

Axis2 architecture is modular. Therefore, Axis2 Framework is
built up of core modules that collectively make up the core
architecture of Axis2. Non-core/other modules are layered on top of
these core modules.

### Core Modules:

- [Information Model](#docs-axis2architectureguide--bminfomod) - Axis2 defines a
  model to handle information and all states are kept in this model.
  The model consists of a hierarchy of information. The system
  manages the life cycle of the objects in this hierarchy.
- [XML processing Model](#docs-axis2architectureguide--bmxml) - Handling the SOAP
  Message is the most important and most complex task. The efficiency
  of this is the single most important factor that decides the
  performance. It makes sense to delegate this task to a separate
  sub-project under the Web services project, allowing that
  sub-project ([AXIOM](http://ws.apache.org/axiom/) or AXis
  Object Model) to provide a simple API for SOAP and XML info-set. It
  hides the complexities of efficient XML processing within its
  implementation.
- [SOAP Processing Model](#docs-axis2architectureguide--bmsoappm) - This controls
  the execution of the processing. The model defines different phases
  the execution would walk through, and the user can extend the
  Processing Model at specific places.
- [Deployment Model](#docs-axis2architectureguide--bmdeployment) - The Axis2
  deployment model allows the user to deploy services, configure the
  transports, and extend the SOAP Processing model per system,
  service, or operation basis.
- [Client API](#docs-axis2architectureguide--bmclientapi) - This provides a
  convenient API for users to communicate with Web services using
  Axis2. There are a set of classes to interact with IN-OUT and
  IN-Only style [Message Exchange
  Patterns (MEPs)](http://www.w3.org/2002/ws/cg/2/07/meps.html), where they can be used to construct any other
  MEP. (Please note that even if the client API has in-built support
  for the above named MEPs, it does not by any means limit Axis2's
  flexibility to support custom MEPs.)
- [Transports](#docs-axis2architectureguide--bmtransports) - Axis2 defines a
  transport framework that enables the user to use multiple different
  transports. The transports fit into specific places in the SOAP
  processing model. The implementation provides a few common
  transports and the user can write or plug-in new ones if and when
  it is needed.

### Other Modules:

- [Code Generation](#docs-axis2architectureguide--bmwsdl) - Axis2 provides a code
  generation tool that generates server side and client side code
  along with descriptors and a test case. The generated code
  simplifies the service deployment and the service invocation,
  increasing the usability of Axis2.
- [Data Binding](#docs-axis2architectureguide--bmdb) - The basic client API of Axis2
  lets the users process SOAP at the infoset level, whereas data
  binding extends it to make it more convenient to users by
  encapsulating the infoset layer and providing a programming
  language specific interface.

![](assets/images/all_08be1dd728f44524.png)

## Information Model

The Information Model has two main hierarchies--Contexts and
Descriptions. This model is described in UML notations below.

![](assets/images/contexts_7081a6c05f229bc5.png)

( A ----<> B says, B has 1 or more objects of A.
A------>B says, the given relationship holds between A and
B.)

The two hierarchies are connected as shown in the above figure.
The Description hierarchy represents the static data. This data may
be loaded from a configuration file that exists throughout the
lifetime of Axis2. For example, deployed Web services, operations, etc. On the other hand, the context hierarchy holds more dynamic
information about objects that can have more than one instance
(e.g., Message Contexts).

These two hierarchies create a model that provides the ability
to search for key-value pairs. When the values are searched at a
given level, they are searched while moving up the hierarchy until
a match is found. In the resulting model, the lower levels override
the values in the upper levels. For example, when a value is looked
up in the Message Context and is not found, it would be looked up
in the Operation Context, etc, up the hierarchy. The Search is
first done up the hierarchy, and if the starting point is a Context
then it searches in the Description hierarchy as well.

This allows the user to declare and override values, with the
result being a very flexible configuration model. This flexibility
could be the *Achilles heel* for the system, however, as
searches are expensive, especially for parameters that turn out not
to exist. Yet in the final analysis, the Axis Team believes that
this flexibility serves developers better overall.

|  |  |  |  |
| --- | --- | --- | --- |
| **Context** | **Description** | **Configuration** | **Description** |
| Configuration Context | Holds the Axis2's run time status. A deep copy of this would essentially make a copy of Axis2. | Axis Configuration | Holds all global configurations: transports, global modules, parameters, services, etc. |
| Service Group Context | Holds information about a particular usage of the respective service group. The life of a Service Group Context starts when a user starts interacting with a service that belongs to this service group. This can be used to share information between services (within the same service group) in a single interaction. | AxisServiceGroup | Holds deployment time information about a particular service group. |
| Service Context | This context is available throughout the usage of the respective service. This can be used to share information between several MEPs of the same service, within a single interaction. The life cycle depends on the scope of the service. | AxisService | Holds the Operations and the service level configurations |
| Operation Context | Holds the information about the current MEP instance, maintains the messages in the current MEP etc. | AxisOperation | Holds the operation level configurations |
| Message Context | Holds all the information about the message currently being executed. | AxisMessage | Holds message level static information like the schema of the particular message. |

## XML Processing Model

As mentioned above, the XML processing model of Axis2 has become
a separate sub-project, called [Apache Axiom](http://ws.apache.org/axiom/), in the Apache Web services project. Please refer to the [OM Tutorial](https://axis.apache.org/axis2/java/core/docs/OMTutorial.html) for more information.

## SOAP Processing Model

![](assets/images/soap-processing_120f99395bc1c51d.gif)

The architecture identified two basic actions a SOAP processor
should perform, sending and receiving SOAP messages. The
architecture provides two pipes (or flows) to perform these two
basic actions. The Axis Engine or the driver of Axis2 defines two
methods, send() and receive(), to implement these two pipes. The
two pipes are named ***In** Pipe* and ***Out**
Pipe*, and complex Message Exchange Patterns (MEPs) are
constructed by combining these two pipes.

Extensibility of the SOAP processing model is provided through
handlers. When a SOAP message is being processed, the handlers that
are registered will be executed. The handlers can be registered in
global, service, or operation scope and the final handler chain is
calculated combining the handlers from all the scopes.

The handlers act as interceptors and they process parts of the
SOAP message and provide add-on services. Usually handlers work on
the SOAP headers, yet they may access or change the SOAP body as
well.

When a SOAP message is being sent through the Client API, an
*Out Pipe* activates. The *Out Pipe* will invoke the
handlers and end with a Transport Sender that sends the SOAP
message to the target endpoint. The SOAP message is received by a
Transport Receiver at the target endpoint, which reads the SOAP
message and starts the *In Pipe*. The *In Pipe*
consists of handlers and ends with the [Message
Receiver](#docs-axis2architectureguide--mr), which consumes the SOAP message.

The processing explained above happens for each and every SOAP
message that is exchanged. After processing one message, Axis2 may
decide to create other SOAP messages, in which case more complex
message patterns emerge. However, Axis2 always views the SOAP
message in terms of processing a single message. The combination of
the messages are layered on top of that basic framework.

The two pipes do not differentiate between the Server and the
Client. The SOAP Processing Model handles the complexity and
provides two abstract pipes to the user. The different areas or the
stages of the pipes are called 'phases' within Axis2. A Handler
always runs inside a specific phase, and the phase provides a
mechanism to specify the ordering of handlers. Both Pipes have
built-in phases, and both define the areas for 'User Phases' which
can be defined by the user.

### Axis2 Default Processing Model

Axis2 has some inbuilt handlers that run in inbuilt phases and
they create the default configuration for Axis2. We will be looking
more in to how to extend the default processing Model in the next
section.

There are three special handlers defined in Axis2.

1. Dispatchers - Finds the service and the operation the SOAP
   message is directed to. Dispatchers always run on the
   *In-Pipe* and inside the Dispatch phase. The in-built
   dispatchers dispatch to a particular operation depending on various
   conditions like WS-Addressing information, URI information, SOAP
   action information, etc. ( See more information on [Dispatching](http://wso2.org/library/176))

- Message Receiver - Consumes the SOAP
  message and hands it over to the application. The message receiver
  is the last handler of the in-pipe
- Transport Sender - Sends the SOAP message to the SOAP endpoint
  the message is destined to. Always runs as the last handler in the
  out-pipe

### Processing an Incoming SOAP Message

An incoming SOAP message is always received by a Transport
Receiver waiting for the SOAP messages. Once the SOAP message
arrives, the transport Headers are parsed and a [Message Context](#docs-axis2architectureguide--messagecontext) is created from the incoming
SOAP message. This message context encapsulates all the
information, including the SOAP message itself, transport headers, etc., inside it. Then the *In Pipe* is executed with the
Message Context.

Let us see what happens at each phase of the execution. This
process can happen in the server or in the client.

1. **Transport Phase** - The handlers are in the
   phase that processes transport specific information such as
   validating incoming messages by looking at various transport
   headers, adding data into message contexts, etc.
2. **Pre-Dispatch Phase**- The main functionality of
   the handlers in this phase is to populate message context to do the
   dispatching. For example, processing of addressing headers of the
   SOAP message, if any, happens in this phase. Addressing handlers
   extract information and put them in to the message context.
3. **Dispatch Phase** - The Dispatchers run in this
   phase and try to find the correct service and operation this
   particular message is destined for.
   The post condition of the dispatch phase (any phase can contain a
   post condition) checks whether a service and an operation were
   found by the dispatchers. If not, the execution will halt and
   return a "service not found' error.
4. **User Defined Phases** - Users can engage their
   custom handlers here.
5. **Message Validation Phase** - Once the user level
   execution has taken place, this phase validates whether SOAP
   Message Processing has taken place correctly.
6. **Message Processing Phase** - The Business logic
   of the SOAP message is executed here. A [Message
   Receiver](#docs-axis2architectureguide--mr) is registered with each Operation. This message
   receiver (associated to the particular operation) will be executed
   as the last handler of this phase.

There may be other handlers in any of these phases. Users may
use custom handlers to override the processing logic in each of
these phases.

### Processing of the Outgoing Message

The *Out Pipe* is simpler because the service and the
operation to dispatch are known by the time the pipe is executed.
The *Out Pipe* may be initiated by the

[Message Receiver](#docs-axis2architectureguide--mr) or the Client API
implementation. Phases of the *Out Pipe* are described
below:

1. **Message Initialize Phase** - First phase of the
   *Out Pipe*. Serves as the placeholder for the custom
   handlers.
2. **User Phases** - Executes handlers in
   user-defined phases.
3. **Transports Phase** - Executes any transport
   handlers taken from the associated transport configuration. The
   last handler would be a transport sender which will send the SOAP
   message to the target endpoint.

### Extending the SOAP Processing Model

Above, we discussed the default processing model of Axis2. Now
let us discuss the extension mechanism for the SOAP processing
model. After all, the whole effort of making this SOAP
engine/processing model was focused on making it extendable.

The idea behind introducing step-wise processing of the SOAP
message in terms of handlers and phases is to allow easier
modification of the processing order. The notion of phases makes it
easier to place handlers in between other handlers. This enables
modification of the default processing behavior. The SOAP
Processing Model can be extended with [handlers](#docs-axis2architectureguide--extendingwithhandlers) or [modules](#docs-axis2architectureguide--extendingwithmodules).

#### Extending the SOAP Processing Model with Handlers

The handlers in a module can specify the phase they need to be
placed in. Furthermore, they can specify their location inside a
phase by providing phase rules. Phase rules will place a
handler,

1. as the first handler in a phase, 2. as the last handler in a phase, 3. before a given handler, 4. or after a given handler.

#### Extending the SOAP Processing Model with Modules

Axis2 defines an entity called a 'module' that can introduce
handlers and Web service operations. A Module in terms of Axis2
usually acts as a convenient packaging that includes:

- A set of handlers and
- An associated descriptor which includes the phase rules

Modules have the concept of being 'available' and 'engaged'.
'Availability' means the module is present in the system, but has
not been activated, i.e., the handlers included inside the module
have not been used in the processing mechanism. When a module is
'engaged' it becomes active and the handlers get placed in the
proper phases. The handlers will act in the same way as explained
in the previous section. Usually a module will be used to implement
a WS-\* functionality such as WS-Addressing.

Apart from the extension mechanism based on the handlers, the
WS-\* specifications may suggest a requirement for adding new
operations. For example, once a user adds Reliable Messaging
capability to a service, the "Create Sequence" operation needs to
be available to the service endpoint. This can be implemented by
letting the modules define the operations. Once the module is
engaged to a service, the necessary operations will be added to
that service.

A service, operation, or the system may engage a module. Once
the module is engaged, the handlers and the operations defined in
the module are added to the entity that engaged them.

Modules cannot be added (no hot deployment) while the Axis2
engine is running, but they will be available once the system is
restarted.

## Deployment

The Deployment Model provides a concrete mechanism to configure
Axis2. This model has three entities that provide the
configuration.

### The axis2.xml file

This file holds the global configuration for the client and
server, and provides the following information:

1. The global parameters
2. Registered transport-in and transport-outs
3. User-defined phase names
4. Modules that are engaged globally (to all services)
5. Globally defined [Message Receivers](#docs-axis2architectureguide--mr)

### Service Archive

The Service archive must have a *META-INF/services.xml* file and may
contain the dependent classes. Please see modules/kernel/resources/services.xsd in
the source distribution for the schema for services.xml. The *services.xml* file has
the following information.

1. Service level parameters
2. Modules that are engaged at service level
3. Service Specific [Message Receivers](#docs-axis2architectureguide--mr)
4. Operations inside the service

### Module Archive

Module archive must have a META-INF/[module.xml](https://axis.apache.org/axis2/java/core/schemas/module.xsd) file and dependent
classes. The *module.xml* file has Module parameters and the
Operations defined in the module.

When the system starts up, Axis2 prompts the deployment model to
create an Axis Configuration. The deployment model first finds the
axis2.xml file and builds the global configuration. Then it checks
for the module archives and then for the service archives. After
that, the corresponding services and modules are added to the Axis
Configuration. The system will build contexts on top of the Axis
Configuration. After this, Axis2 is ready to send or receive SOAP
messages. Hot deployment is only allowed for services.

## Client API

There are three parameters that decide the nature of the Web
service interaction.

1. Message Exchange Pattern (MEP)
2. The behavior of the transport, whether it's One-Way or
   Two-Way
3. Synchronous/Asynchronous behavior of the Client API

Variations of the three parameters can result in an indefinite
number of scenarios. Even though Axis2 is built on a core that
supports any messaging interaction, the developers were compelled
to provide built-in support for only the two most widely used
Message Exchange Patterns (MEPs).

The two supported MEPs are One-Way and the In-Out
(Request-Response) scenarios in the Client API. The implementation
is based on a class called `ServiceClient` and there are
extensions for each MEP that Axis2 Client API supports.

### One Way Messaging Support

The One-Way support is provided by the
`fireAndForget` method of `ServiceClient`.
For one way invocations, one can use HTTP, SMTP and TCP transports.
In the case of the HTTP transport, the return channel is not used, and the HTTP 202 OK is returned in the return channel.

### In-Out (Request Response) Messaging Support

The In-Out support is provided by the `sendReceive()`
method in ServiceClient. This provides a simpler interface for the
user. The Client API has four ways to configure a given message
exchange

1. Blocking or Non-Blocking nature - this can be decided by using
   `sendReceive()` or `sendReceiveNonBlocking()`
   methods
2. Sender transport - transport that sends the SOAP message
3. Listener transport - transport that receives the response
4. Use Separate Channel - determines whether the response is sent
   over a separate transport connection or not. This can be false only
   when the sender and listener transport is same and is a Two-Way
   transport.

Depending on the values of the above four parameters, Axis2
behaves differently.

## Transports

Axis2 has two basic constructs for transports, namely: Transport
Senders and Transport Receivers. These are accessed via the
AxisConfiguration.

The incoming transport is the transport via which the AxisEngine
receives the message. The outgoing transport is decided based on
the addressing information (wsa:ReplyTo and wsa:FaultTo). If
addressing information is not available and if the server is trying
to respond, then the out going transport will be the output stream
of the incoming transport (if it is two-way transport).

At the client side, the user is free to specify the transport to
be used.

Transport Senders and Transport Receivers contain the following
information.

1. Transport Sender for Out Configuration
2. Transport Listener for In Configuration
3. Parameters of the transport

Each and every transport out configuration defines a transport
sender. The transport sender sends the SOAP message depending on
its configuration.

The transport receiver waits for the SOAP messages, and for each
SOAP message that arrives, it uses the *In Pipe* to process
the SOAP message.

Axis2 presently supports the following transports:

1. HTTP - In HTTP transport, the transport listener is a servlet
   or org.apache.axis2.transport.http.SimpleHTTPServer provided by
   Axis2. The transport sender uses apache httpcomponents to connect and
   send the SOAP message.
2. Local - This transport can be used for in-VM communication.
3. Transports for TCP, SMTP, JMS and other protocols are available
   from the [WS-Commons Transport](http://ws.apache.org/commons/transport/)
   project.

## Code Generation

Although the basic objective of the code generation tools has
not changed, the code generation module of Axis2 has taken a
different approach to generate code. Primarily, the change is in
the use of templates, namely XSL templates, which gives the code
generator the flexibility to generate code in multiple
languages.

The basic approach is to set the code generator to generate an
XML, and parse it with a template to generate the code file. The
following figure describes how this shows up in the architecture of
the tool.

![](assets/images/codegenarchitecture-new_4f64d9a3c65d0c85.gif)

The fact here is that it is the same information that is
extracted from the WSDL no matter what output code is generated.
First, an AxisService is populated from a WSDL. Then the code
generator extracts information from the AxisService and creates an
XML, which is language independent. This emitted XML is then parsed
with the relevant XSL to generate code in the desired output
language. No matter what the output language is, the process is the
same except for the XSL template that is used.

## Data Binding

### Integration with the Code Generation Engine

Databinding for Axis2 is implemented in an interesting manner.
Databinding has not been included in the core deliberately, and
hence the code generation allows different data binding frameworks
to be plugged in. This is done through an extension mechanism where
the codegen engine first calls the extensions and then executes the
core emitter. The extensions populate a map of QNames vs. class
names that is passed to the code generator on which the emitter
operates on.

**The following diagram shows the structure:**

![](assets/images/codegen_d7c56987a61dd74c.gif)

**The following databinding extensions are
available:**

1. **ADB** - ADB (Axis Data Binding ) is a simple
   framework that allows simple schemas to be compiled. It is
   lightweight and simple, works off StAX and fairly performant.
   However, it does not support the complete set of schema constructs
   and is likely to complain for certain schemas!
2. **XMLBeans** - XMLbeans claims that it supports
   the complete schema specification, and it is preferred if full
   schema support is needed!
3. **JAXB-RI** - JAXB2 support has been added in a
   similar manner to XMLbeans and serves as another option for the
   user
4. **JibX** - This is the most recent addition to the
   family of databinding extensions, and it is also another option
   users have for data binding.

### Serialization and De-Serialization of Data bound classes

AXIOM is based on the StAX API (Streaming API for XML).
Xml-beans also supports this API. Data binding in Axis2 is achieved
through interfacing the AXIOM with the Xml-beans using the StAX
API. At the time of code generation, there will be utility methods
generated inside the stub (or the message receiver) that can
de-serialize from AXIOM to a data bound object and serialize from a
data bound object to AXIOM. For example, if the WSDL has an
operation called "echoString", once the code is generated, the
following methods will be generated inside the relevant
classes.

```

public static
org.apache.axiom.om.OMElement toOM(org.soapinterop.xsd.EchoStringParamDocument
param)// This method will handle the serialization.

public static org.apache.xmlbeans.XmlObject
fromOM(org.apache.axis2.om.OMElement param, java.lang.Class type) //This
method will handle the de-serialization.
```

---

<a id="docs-jaxws-guide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/jaxws-guide.html -->

<!-- page_index: 11 -->

# JAX-WS Guide

## Table of Contents

1. [Introduction to JAX-WS](#docs-jaxws-guide--jaxwsintro)
2. [Introduction to JAXB](#docs-jaxws-guide--jaxbintro)
3. [Developing JAX-WS Web services](#docs-jaxws-guide--developservice)
   1. [From a JavaBean
      (bottom-up)](#docs-jaxws-guide--bottomupservice)
   2. [From a WSDL document
      (top-down)](#docs-jaxws-guide--topdownservice)
4. [Packaging and deploying a JAX-WS
   service](#docs-jaxws-guide--deployservice)
   1. [Developing a JAX-WS client from
      a WSDL document](#docs-jaxws-guide--proxyclient)
   2. [Developing a dynamic client
      using JAX-WS APIs](#docs-jaxws-guide--dispatchclient)
5. [Developing JAX-WS clients](#docs-jaxws-guide--developclient)
6. [Running a JAX-WS client](#docs-jaxws-guide--runclient)
7. [Invoking JAX-WS Web services
   asynchronously](#docs-jaxws-guide--async)
8. [Using handlers in JAX-WS Web
   services](#docs-jaxws-guide--handlers)
9. [Enabling HTTP session management
   support for JAX-WS applications](#docs-jaxws-guide--httpsession)
10. [Enabling MTOM](#docs-jaxws-guide--mtom)

## Introduction to JAX-WS

JAX-WS 2.0 is a new programming model that
simplifies application development through support of a standard, annotation-based model to develop Web Service applications and
clients. The JAX-WS 2.0 specification strategically aligns itself
with the current industry trend towards a more document-centric
messaging model and replaces the remote procedure call
programming model as defined by JAX-RPC. JAX-WS is the strategic
programming model for developing Web services and is a required
part of the Java Platform, Enterprise Edition 5 (Java EE 5). The
implementation of the JAX-WS programming standard provides the
following enhancements for developing Web services and clients:

- Better platform independence for Java applications.
- Using JAX-WS APIs, development of Web services and clients is
  simplified with better platform independence for Java
  applications. JAX-WS takes advantage of the dynamic proxy
  mechanism to provide a formal delegation model with a pluggable
  provider. This is an enhancement over JAX-RPC, which relies on
  the generation of vendor-specific stubs for invocation.
- Annotations
- JAX-WS introduces support for annotating Java classes with
  metadata to indicate that the Java class is a Web service.
  JAX-WS supports the use of annotations based on the Metadata
  Facility for the Java Programming Language (JSR 175)
  specification, the Web Services Metadata for the Java
  Platform (JSR 181) specification and annotations defined by
  the JAX-WS 2.0 specification. Using annotations within the
  Java source and within the Java class simplifies development
  of Web services by defining some of the additional
  information that is typically obtained from deployment
  descriptor files, WSDL files, or mapping metadata from XML
  and WSDL files into the source artifacts.
  For example, you can embed a simple @WebService tag in the
  Java source to expose the bean as a Web service.

```

      @WebService 

      public class QuoteBean implements StockQuote {

             public float getQuote(String sym) { ... }

      }
```

  The `@WebService` annotation tells the server
  runtime to expose all public methods on that bean as a Web service.
  Additional levels of granularity can be controlled by adding
  additional annotations on individual methods or parameters. Using
  annotations makes it much easier to expose Java artifacts as Web
  services. In addition, as artifacts are created from using some of
  the top-down mapping tools starting from a WSDL file, annotations
  are included within the source and Java classes as a way of
  capturing the metadata along with the source files.
  Using annotations also improves the development of Web
  services within a team structure because you do not need to
  define every Web service in a single or common deployment
  descriptor as required with JAX-RPC Web services. Taking
  advantage of annotations with JAX-WS Web services allows
  parallel development of the service and the required
  metadata.
- Invoking Web services asynchronously
- With JAX-WS, Web services are called both synchronously and
  asynchronously. JAX-WS adds support for both a polling and
  callback mechanism when calling Web services asynchronously.
  Using a polling model, a client can issue a request, get a
  response object back, which is polled to determine if the
  server has responded. When the server responds, the actual
  response is retrieved. Using the callback model, the client
  provides a callback handler to accept and process the inbound
  response object. Both the polling and callback models enable
  the client to focus on continuing to process work without
  waiting for a response to return, while providing for a more
  dynamic and efficient model to invoke Web services.
  For example, a Web service interface might have methods for
  both synchronous and asynchronous requests. Asynchronous
  requests are identified in bold below:

```

      @WebService
      public interface CreditRatingService {
            // sync operation
            Score      getCreditScore(Customer customer);
            // async operation with polling
            Response<Score> getCreditScoreAsync(Customer customer);
            // async operation with callback
            Future<?> getCreditScoreAsync(Customer customer, 
               AsyncHandler<Score> handler);
      }
```

  The asynchronous invocation that uses the callback mechanism
  requires an additional input by the client programmer. The callback
  is an object that contains the application code that will be
  executed when an asynchronous response is received. The following
  is a code example for an asynchronous callback handler:

```

      CreditRatingService svc = ...;

      Future<?> invocation = svc.getCreditScoreAsync(customerFred,
        new AsyncHandler<Score>() {
           public void handleResponse (
               Response<Score> response)
             {
               Score score = response.get();
               // do work here...
             }
         }
      );
```

  The following is a code example for an asynchronous polling
  client:

```

      CreditRatingService svc = ...;
      Response<Score> response = svc.getCreditScoreAsync(customerFred);

      while (!response.isDone()) {
                // do something while we wait
      }

      // no cast needed, thanks to generics
      Score score = response.get();
```

- Using resource injection
- JAX-WS supports resource injection
  to further simplify development of Web services. JAX-WS uses
  this key feature of Java EE 5 to shift the burden of creating
  and initializing common resources in a Java runtime environment
  from your Web service application to the application container
  environment itself. JAX-WS provides support for a subset of
  annotations that are defined in JSR-250 for resource injection
  and application lifecycle in its runtime.
  Axis2 supports the JAX-WS usage of the `@Resource`
  annotation for resource injection. The `@Resource`
  annotation is defined by the JSR-250, Common Annotations
  specification that is included in Java Platform, Enterprise
  Edition 5 (Java EE 5). By placing the `@Resource`
  annotation on a service endpoint implementation, you can
  request a resource injection and collect the
  `jakarta.xml.ws.WebServiceContext` interface related
  to that particular endpoint invocation. When the endpoint
  sees the `@Resource` annotation, the endpoint adds
  the annotated variable with an appropriate value before the
  servlet is placed into service. From the
  `WebServiceContext` interface, you can collect the
  `MessageContext` for the request associated with
  the particular method call using the
  `getMessageContext()` method.
  The following example illustrates using the
  `@Resource` annotation for resource injection:

```
@WebService
public class MyService {
    
    @Resource
    private WebServiceContext ctx;

    public String echo (String input) {
        …
    }
     
}
```

  Refer to sections 5.2.1 and 5.3 of the JAX-WS 2.0
  specification for more information on resource injection.
- Data binding with Java Architecture for XML Binding (JAXB)
  2.0
- JAX-WS leverages the JAXB 2.0 API and tools as the binding
  technology for mappings between Java objects and XML documents.
  JAX-WS tooling relies on JAXB tooling for default data binding
  for two-way mappings between Java objects and XML
  documents.
- Dynamic and static clients
- The dynamic client API for JAX-WS is called the dispatch client
  (`jakarta.xml.ws.Dispatch`). The dispatch client is an
  XML messaging oriented client. The data is sent in either
  `PAYLOAD` or `MESSAGE` mode. When using
  the `PAYLOAD` mode, the dispatch client is only
  responsible for providing the contents of the <soap:Body>
  and JAX-WS adds the <soap:Envelope> and
  <soap:Header> elements. When using the
  `MESSAGE` mode, the dispatch client is responsible
  for providing the entire SOAP envelope including the
  <soap:Envelope>, <soap:Header>, and
  <soap:Body> elements and JAX-WS does not add anything
  additional to the message. The dispatch client supports
  asynchronous invocations using a callback or polling
  mechanism.
  The static client programming model for JAX-WS is the called
  the proxy client. The proxy client invokes a Web service based
  on a Service Endpoint interface (SEI) which must be
  provided.
- Support for Message Transmission Optimized Mechanism
  (MTOM)
- Using JAX-WS, you can send binary attachments such as images or
  files along with Web services requests. JAX-WS adds support for
  optimized transmission of binary data as specified by Message
  Transmission Optimization Mechanism (MTOM).
- Multiple data binding technologies
- JAX-WS exposes the following binding technologies to the end
  user: XML Source, SOAP Attachments API for Java (SAAJ) 1.3, and
  Java Architecture for XML Binding (JAXB) 2.0. XML Source
  enables a user to pass a javax.xml.transform.Source into the
  runtime which represents the data in a Source object to be
  processed. SAAJ 1.3 now has the ability to pass an entire SOAP
  document across the interface rather than just the payload
  itself. This is done by the client passing the SAAJ
  `SOAPMessage` object across the interface. JAX-WS
  leverages the JAXB 2.0 support as the data binding technology
  of choice between Java and XML.
- Support for SOAP 1.2
- Support for SOAP 1.2 has been added to JAX-WS 2.0. JAX-WS
  supports both SOAP 1.1 and SOAP 1.2 so that you can send binary
  attachments such as images or files along with Web services
  requests. JAX-WS adds support for optimized transmission of
  binary data as specified by MTOM.
- New development tools
- JAX-WS provides the **wsgen** and **wsimport**
  command-line tools for generating portable artifacts for
  JAX-WS Web services. When creating JAX-WS Web services, you
  can start with either a WSDL file or an implementation bean
  class. If you start with an implementation bean class, use
  the wsgen command-line tool to generate all the Web services
  server artifacts, including a WSDL file if requested. If you
  start with a WSDL file, use the wsimport command-line tool to
  generate all the Web services artifacts for either the server
  or the client. The wsimport command line tool processes the
  WSDL file with schema definitions to generate the portable
  artifacts, which include the service class, the service
  endpoint interface class, and the JAXB 2.0 classes for the
  corresponding XML schema.

## Introduction to JAXB

Java Architecture for XML Binding (JAXB) is a
Java technology that provides an easy and convenient way to
map Java classes and XML schema for simplified development of
Web services. JAXB leverages the flexibility of
platform-neutral XML data in Java applications to bind XML
schema to Java applications without requiring extensive
knowledge of XML programming.
Axis2 provides JAXB 2.0 standards.
JAXB is an XML to Java binding technology that supports
transformation between schema and Java objects and between
XML instance documents and Java object instances. JAXB
consists of a runtime application programming interface (API)
and accompanying tools that simplify access to XML documents.
JAXB also helps to build XML documents that both conform and
validate to the XML schema.
JAXB provides the **xjc** schema compiler tool, the
**schemagen** schema generator tool, and a runtime
framework. You can use the **xjc** schema compiler tool to
start with an XML schema definition (XSD) to create a set of
JavaBeans that map to the elements and types defined in the
XSD schema. You can also start with a set of JavaBeans and
use the **schemagen** schema generator tool to create the
XML schema. Once the mapping between XML schema and Java
classes exists, XML instance documents can be converted to
and from Java objects through the use of the JAXB binding
runtime API. Data stored in XML documents can be accessed
without the need to understand the data structure. You can
then use the resulting Java classes to assemble a Web
services application.
JAXB annotated classes and artifacts contain all the
information needed by the JAXB runtime API to process XML
instance documents. The JAXB runtime API supports marshaling
of JAXB objects to XML and unmarshaling the XML document back
to JAXB class instances. Optionally, you can use JAXB to
provide XML validation to enforce both incoming and outgoing
XML documents to conform to the XML constraints defined
within the XML schema.
JAXB is the default data binding technology used by the Java
API for XML Web Services (JAX-WS) 2.0 tooling and
implementation within this product. You can develop JAXB
objects for use within JAX-WS applications.
You can also use JAXB independently of JAX-WS when you want
to leverage the XML data binding technology to manipulate XML
within your Java applications.
The following diagram illustrates the JAXB
architecture.
![](assets/images/jaxb-architecture_f2591faa685a45ae.gif)

## Developing JAX-WS Web services

### Developing a JAX-WS Web service from a JavaBean (bottom-up development)

When developing a JAX-WS Web service
starting from JavaBeans, you can use a bean that already
exists and then enable the implementation for JAX-WS Web
services. The use of annotations simplifies the enabling of a
bean for Web services. Adding the `@WebService`
annotation to the bean defines the application as a Web
service and how a client can access the Web service.
JavaBeans can have a service endpoint interface, but it is
not required. Enabling JavaBeans for Web services includes
annotating the bean and the optional service endpoint
interface, assembling all artifacts required for the Web
service, and deploying the application into Axis2. You are
not required to develop a WSDL file because the use of
annotations can provide all of the WSDL information necessary
to configure the service endpoint or the client. It is, however, a best practice to develop a WSDL file.

1. Develop a service endpoint interface.
2. Java API for XML-Based Web Services (JAX-WS) supports two
   different service endpoint implementations types, the
   standard JavaBeans service endpoint interface and a new
   `Provider` interface to enable services to
   work at the XML message level. By using annotations on
   the service endpoint or client, you can define the
   service endpoint as a Web service.
   JavaBeans endpoints in JAX-WS are similar to the endpoint
   implementations in the Java API for XML-based RPC
   (JAX-RPC) specification. Unlike JAX-RPC, the requirement
   for a service endpoint interface (SEI) is optional for
   JavaBeans-based services. JAX-WS services that do not
   have an associated SEI are regarded as having an implicit
   SEI, whereas services that have an associated SEI are
   regarded as having an explicit SEI. The service endpoint
   interfaces required by JAX-WS are also more generic than
   the service endpoint interfaces required by JAX-RPC. With
   JAX-WS, the SEI is not required to extend the
   java.rmi.Remote interface as required by the JAX-RPC
   specification.
   The JAX-WS programming model also leverages support for
   annotating Java classes with metadata to define a service
   endpoint application as a Web service and define how a
   client can access the Web service. JAX-WS supports
   annotations based on the Metadata Facility for the Java
   Programming Language (JSR 175) specification, the Web
   Services Metadata for the Java Platform (JSR 181)
   specification and annotations defined by the JAX-WS 2.0
   (JSR 224) specification, which includes Java Architecture
   for XML Binding (JAXB) annotations. Using annotations,
   the service endpoint implementation can independently
   describe the Web service without requiring a WSDL file.
   Annotations can provide all of the WSDL information
   necessary to configure your service endpoint
   implementation or Web services client. You can specify
   annotations on the service endpoint interface used by the
   client and the server, or on the server-side service
   implementation class.
   To develop a JAX-WS Web service, you must annotate your
   Java class with the `jakarta.jws.WebService`
   annotation for JavaBeans endpoints or the
   `jakarta.jws.WebServiceProvider` annotation for
   a Provider endpoint. These annotations define the Java
   class as a Web service endpoint. For a JavaBeans
   endpoint, the service endpoint interface or service
   endpoint implementation is a Java interface or class,
   respectively, that declares the business methods provided
   by a particular Web service. The only methods on a
   JavaBeans endpoint that can be invoked by a Web services
   client are the business methods that are defined in the
   explicit or implicit service endpoint interface.
   All JavaBeans endpoints are required to have the
   `@WebService (jakarta.jws.WebService)`
   annotation included on the bean class. If the service
   implementation bean also uses an SEI, then that endpoint
   interface must be referenced by the endpointInterface
   attribute on that annotation. If the service
   implementation bean does not use an SEI, then the service
   is described by the implicit SEI defined in the
   bean.
   The JAX-WS programming model introduces the new Provider
   API, `jakarta.xml.ws.Provider`, as an
   alternative to service endpoint interfaces. The
   `Provider` interface supports a more messaging
   oriented approach to Web services. With the
   `Provider` interface, you can create a Java
   class that implements a simple interface to produce a
   generic service implementation class. The
   `Provider` interface has one method, the
   invoke method, which uses generics to control both the
   input and output types when working with various messages
   or message payloads. All Provider endpoints must be
   annotated with the `@WebServiceProvider
   (jakarta.xml.ws.WebServiceProvider)` annotation. A
   service implementation cannot specify the
   `@WebService` annotation if it implements the
   `jakarta.xml.ws.Provider` interface.
   So the steps involved are:
   1. Identify your service endpoint requirements for
      your Web services application.
   2. First determine if the service implementation is a
      JavaBeans endpoint or a Provider endpoint. If you
      choose to use a JavaBeans endpoint, then determine if
      you want to use an explicit SEI or if the bean itself
      will have an implicit SEI.
      A Java class that implements a Web service must
      specify either the `jakarta.jws.WebService`
      or `jakarta.xml.ws.WebServiceProvider`
      annotation. Both annotations must not be present on a
      Java class. The
      `jakarta.xml.ws.WebServiceProvider`
      annotation is only supported on classes that
      implement the `jakarta.xml.ws.Provider`
      interface.
      - If you have an explicit service endpoint
        interface with the Java class, then use the
        endpointInterface parameter to specify the service
        endpoint interface class name to the
        `jakarta.jws.WebService` annotation. You
        can add the `@WebMethod` annotation to
        methods of a service endpoint interface to
        customize the Java-to-WSDL mappings. All public
        methods are considered as exposed methods
        regardless of whether the `@WebMethod`
        annotation is specified or not. It is incorrect to
        have an `@WebMethod` annotation on an
        service endpoint interface that contains the
        `exclude` attribute.
      - If you have an implicit service endpoint
        interface with the Java class, then the
        `jakarta.jws.WebService` annotation will
        use the default values for the
        `serviceName`, `portName`,
        and `targetNamespace` parameters. To
        override these default values, specify values for
        these parameters in the `@WebService`
        annotation. If the `@WebMethod`
        annotation is not specified, all public methods are
        exposed including the inherited methods with the
        exception of methods inherited from
        `java.lang.Object`. The
        `exclude` parameter of the
        `@WebMethod` annotation can be used to
        control which methods are exposed.
      - If you are using the `Provider`
        interface, use the
        `jakarta.xml.ws.WebServiceProvider`
        annotation on the Provider endpoint.
   3. Annotate the service endpoints.
   4. Implement your service.When using a bottom-up approach to develop JAX-WS Web
   services, use the wsgen command-line tool when starting
   from a service endpoint implementation. The wsgen tool
   processes a compiled service endpoint implementation
   class as input and generates the following portable
   artifacts:
   - any additional Java Architecture for XML Binding
     (JAXB) classes that are required to marshal and
     unmarshal the message contents. The additional classes
     include classes that are represented by the
     @RequestWrapper annotation and the
     `@ResponseWrapper` annotation for a wrapped
     method.
   - a WSDL file if the optional `-wsdl`
     argument is specified. The wsgen command does not
     automatically generate the WSDL file. The WSDL file is
     automatically generated when you deploy the service
     endpoint.You are not required to develop a WSDL file when
   developing JAX-WS Web services using the bottom-up
   approach of starting with JavaBeans. The use of
   annotations provides all of the WSDL information
   necessary to configure the service endpoint or the
   client. Axis2 supports WSDL 1.1 documents that comply
   with Web Services-Interoperability (WS-I) Basic Profile
   1.1 specifications and are either Document/Literal style
   documents or RPC/Literal style documents. Additionally,
   WSDL documents with bindings that declare a USE attribute
   of value `LITERAL` are supported while the
   value, `ENCODED`, is not supported. For WSDL
   documents that implement a Document/Literal wrapped
   pattern, a root element is declared in the XML schema and
   is used as an operation wrapper for a message flow.
   Separate wrapper element definitions exist for both the
   request and the response.
   To ensure the wsgen command does not miss inherited
   methods on a service endpoint implementation bean, you
   must either add the `@WebService` annotation
   to the desired superclass or you can override the
   inherited method in the implementation class with a call
   to the superclass method. Implementation classes only
   expose methods from superclasses that are annotated with
   the `@WebService` annotation.
   Note: The **wsgen** command does not differentiate the
   XML namespace between multiple `XMLType`
   annotations that have the same `@XMLType` name
   defined within different Java packages. When this
   scenario occurs, the following error is produced:

```

   Error: Two classes have the same XML type name ....
   Use @XmlType.name and @XmlType.namespace to assign different names to them...
```

   This error indicates you have class names or
   `@XMLType.name` values that have the same name, but
   exist within different Java packages. To prevent this error, add
   the `@XML.Type.namespace` class to the existing `@XMLType` annotation to differentiate between the
   XML types.
3. Develop the Java artifacts.
4. Package and deploy your service.

### Developing a JAX-WS Web service from a WSDL document (top-down development)

You can use a top-down development
approach to create a JAX-WS Web service with an existing WSDL
file using JavaBeans.
You can use the JAX-WS tool, **wsimport**, to process a
WSDL file and generate portable Java artifacts that are used
to create a Web service. The portable Java artifacts created
using the **wsimport** tool are:

- Service endpoint interface (SEI)
- Service class
- Exception class that is mapped from the
  `wsdl:fault` class (if any)
- Java Architecture for XML Binding (JAXB) generated type
  values which are Java classes mapped from XML schema
  types

Run the

```

wsimport -keep -verbose wsdl_URL
```

command to generate the portable artifacts. The
`-keep` option tells the tool not to delete the
generated files, and the `-verbose` option tells it to
list the files that were created. The ObjectFactory.java file that
is created contains factory methods for each Java content interface
and Java element interface generated in the associated package. The
package-info.java file takes the `targetNamespace` value
and creates the directory structure.
You must now provide an implementation for the SEI created by
the tool.

## Packaging and deploying a JAX-WS service

Axis2 provides two
mechanisms for deploying JAX-WS services:

1. The service may be packaged and deployed as an AAR,
   just like any other service within Axis2. Like with all
   AARs, a services.xml file containing the relevant metadata
   is required for the service to deploy correctly.
2. The service may be packaged in a jar file and placed
   into the `servicejars` directory. The
   `JAXWSDeployer` will examine all jars within
   that directory and deploy those classes that have JAX-WS
   annotations which identify them as Web services.

## Developing JAX-WS clients

The Java API for XML-Based Web
Services (JAX-WS) Web service client programming model
supports both the Dispatch client API and the Dynamic Proxy
client API. The Dispatch client API is a dynamic client
programming model, whereas the static client programming
model for JAX-WS is the Dynamic Proxy client. The Dispatch
and Dynamic Proxy clients enable both synchronous and
asynchronous invocation of JAX-WS Web services.

- Dispatch client: Use this client when you want to work
  at the XML message level or when you want to work without
  any generated artifacts at the JAX-WS level.
- Dynamic Proxy client: Use this client when you want to
  invoke a Web service based on a service endpoint
  interface.

#### Dispatch client

XML-based Web services use XML
messages for communications between Web services and Web
services clients. The JAX-WS APIs provide high-level methods
to simplify and hide the details of converting between Java
method invocations and their associated XML messages.
However, in some cases, you might desire to work at the XML
message level. Support for invoking services at the XML
message level is provided by the Dispatch client API. The
Dispatch client API, `jakarta.xml.ws.Dispatch`, is a
dynamic JAX-WS client programming interface. To write a
Dispatch client, you must have expertise with the Dispatch
client APIs, the supported object types, and knowledge of the
message representations for the associated WSDL file. The
Dispatch client can send data in either `MESSAGE`
or `PAYLOAD` mode. When using the
`jakarta.xml.ws.Service.Mode.MESSAGE` mode, the
Dispatch client is responsible for providing the entire SOAP
envelope including the `<soap:Envelope>`, `<soap:Header>`, and
`<soap:Body>` elements. When using the
`jakarta.xml.ws.Service.Mode.PAYLOAD` mode, the
Dispatch client is only responsible for providing the
contents of the `<soap:Body>` and JAX-WS
includes the payload in a `<soap:Envelope>`
element.
The Dispatch client API requires application clients to
construct messages or payloads as XML which requires a
detailed knowledge of the message or message payload. The
Dispatch client supports the following types of objects:

- `jakarta.xml.transform.Source`: Use
  `Source` objects to enable clients to use XML
  APIs directly. You can use `Source` objects with
  SOAP or HTTP bindings.
- JAXB objects: Use JAXB objects so that clients can use
  JAXB objects that are generated from an XML schema to
  create and manipulate XML with JAX-WS applications. JAXB
  objects can only be used with SOAP or HTTP bindings.
- `jakarta.xml.soap.SOAPMessage`: Use
  `SOAPMessage` objects so that clients can work
  with SOAP messages. You can only use
  `SOAPMessage` objects with SOAP bindings.
- `jakarta.activation.DataSource`: Use
  `DataSource` objects so that clients can work
  with Multipurpose Internet Mail Extension (MIME) messages.
  Use `DataSource` only with HTTP bindings.

For example, if the input parameter type is
javax.xml.transform.Source, the call to the Dispatch client
API is similar to the following code example:

```
Dispatch<Source> dispatch = … create a Dispatch<Source>
Source request = … create a Source object
Source response = dispatch.invoke(request);
```

The Dispatch parameter value determines the return type of
the `invoke()` method.
The Dispatch client is invoked in one of three ways:

- Synchronous invocation for requests and responses using
  the `invoke` method
- Asynchronous invocation for requests and responses
  using the `invokeAsync` method with a callback
  or polling object
- One-way invocation using the `invokeOneWay`
  methods

Refer to Chapter 4, section 3 of the JAX-WS 2.0 specification
for more information on using a Dispatch client.

#### Dynamic Proxy client

The static client programming
model for JAX-WS is the called the Dynamic Proxy client. The
Dynamic Proxy client invokes a Web service based on a Service
Endpoint Interface (SEI) which must be provided. The Dynamic
Proxy client is similar to the stub client in the Java API
for XML-based RPC (JAX-RPC) programming model. Although the
JAX-WS Dynamic Proxy client and the JAX-RPC stub client are
both based on the Service Endpoint Interface (SEI) that is
generated from a WSDL file , there is a major difference. The
Dynamic Proxy client is dynamically generated at run time
using the Java 5 Dynamic Proxy functionality, while the
JAX-RPC-based stub client is a non-portable Java file that is
generated by tooling. Unlike the JAX-RPC stub clients, the
Dynamic Proxy client does not require you to regenerate a
stub prior to running the client on an application server for
a different vendor because the generated interface does not
require the specific vendor information.
The Dynamic Proxy instances extend the
`java.lang.reflect.Proxy` class and leverage the
Dynamic Proxy function in the base Java Runtime Environment
Version 5. The client application can then provide an
interface that is used to create the proxy instance while the
runtime is responsible for dynamically creating a Java object
that represents the SEI.
The Dynamic Proxy client is invoked in one of three
ways:

- Synchronous invocation for requests and responses using
  the `invoke` method
- Asynchronous invocation for requests and responses
  using the `invokeAsync` method with a callback
  or polling object
- One-way invocation using the `invokeOneWay`
  methods

Refer to Chapter 4 of the JAX-WS 2.0 specification for more
information on using Dynamic Proxy clients.

### Developing a JAX-WS client from a WSDL document

Java API for
XML-Based Web Services (JAX-WS) tooling supports generating
Java artifacts you need to develop static JAX-WS Web services
clients when starting with a Web Services Description
Language (WSDL) file.
The static client programming model for JAX-WS is the called
the dynamic proxy client. The dynamic proxy client invokes a
Web service based on a service endpoint interface that is
provided. After you create the proxy, the client application
can invoke methods on the proxy just like a standard
implementation of those interfaces. For JAX-WS Web service
clients using the dynamic proxy programming model, use the
JAX-WS tool, **wsimport**, to process a WSDL file and
generate portable Java artifacts that are used to create a
Web service client.
Create the following portable Java artifacts using the
wsimport tool:

- Service endpoint interface (SEI)
- Service class
- Exception class that is mapped from the wsdl:fault
  class (if any)
- Java Architecture for XML Binding (JAXB) generated type
  values which are Java classes mapped from XML schema
  types

The steps to creating a dynamic proxy client are:

1. (Optional) If you are using WSDL or schema
   customizations, use the **-b** option with the
   **wsimport** command to specify an external binding
   files that contain your customizations.
   For example: **wsimport -b *binding.xml
   wsdlfile.wsdl***.
   You can customize the bindings in your WSDL file to enable
   asynchronous mappings or attachments. To generate
   asynchronous interfaces, add the client-side only
   customization `enableAsyncMapping` binding
   declaration to the `wsdl:definitions` element or
   in an external binding file that is defined in the WSDL
   file. Use the `enableMIMEContent` binding
   declaration in your custom client or server binding file to
   enable or disable the default `mime:content`
   mapping rules. For additional information on custom binding
   declarations, see chapter 8 the JAX-WS specification.
3. Run the **wsimport -keep *wsdl\_UR*L** command
   to generate the portable client artifacts. Use the
   **-verbose** option to see a list of generated files
   when you run the command.
   Best practice: When you run the **wsimport** tool, the
   location of your WSDL file must either be omitted or point
   to a valid WSDL document. A best practice for ensuring that
   you produce a JAX-WS Web services client that is portable
   to other systems is to package the WSDL document within the
   application module such as a Web services client Java
   archive (JAR) file or a Web archive (WAR) file. You can
   specify a relative URI for the location of your WSDL file
   by using the`-wsdllocation` annotation
   attribute. For example, if your MyService.wsdl file is
   located in the META-INF/wsdl/ directory, then run the
   wsimport tool and use the `-wsdllocation` option
   to specify the value to be used for the location of the
   WSDL file.
   `wsimport -keep
   -wsdllocation=META-INF/wsdl/MyService.wsdl`

### Developing a dynamic client using JAX-WS APIs

JAX-WS provides a
new dynamic Dispatch client API that is more generic and
offers more flexibility than the existing Java API for
XML-based RPC (JAX-RPC)-based Dynamic Invocation Interface
(DII). The Dispatch client interface, `jakarta.xml.ws.Dispatch`, is an XML messaging
oriented client that is intended for advanced XML developers
who prefer to work at the XML level using XML constructs. To
write a Dispatch client, you must have expertise with the
Dispatch client APIs, the supported object types, and
knowledge of the message representations for the associated
WSDL file.
The Dispatch API can send data in either `PAYLOAD`
or `MESSAGE` mode. When using the
`PAYLOAD` mode, the Dispatch client is only
responsible for providing the contents of the
`<soap:Body>` and JAX-WS includes the input
payload in a `<soap:Envelope>` element. When
using the `MESSAGE` mode, the Dispatch client is
responsible for providing the entire SOAP envelope.
The Dispatch client API requires application clients to
construct messages or payloads as XML and requires a detailed
knowledge of the message or message payload. The Dispatch
client can use HTTP bindings when using `Source`
objects, Java Architecture for XML Binding (JAXB) objects, or
data source objects. The Dispatch client supports the
following types of objects:

- `javax.xml.transform.Source`: Use
  `Source` objects to enable clients to use XML
  APIs directly. You can use `Source` objects with
  SOAP and HTTP bindings.
- JAXB objects: Use JAXB objects so that clients can use
  JAXB objects that are generated from an XML schema to
  create and manipulate XML with JAX-WS applications. JAXB
  objects can only be used with SOAP and HTTP bindings.
- `jakarta.xml.soap.SOAPMessage`: Use
  `SOAPMessage` objects so that clients can work
  with SOAP messages. You can only use
  `SOAPMessage` objects with SOAP version 1.1 or
  SOAP version 1.2 bindings.
- `jakarta.activation.DataSource`: Use
  `DataSource` objects so that clients can work
  with Multipurpose Internet Mail Extension (MIME) messages.
  Use `DataSource` only with HTTP bindings.

The Dispatch API uses the concept of generics that are
introduced in Java Runtime Environment Version 5. For each of
the invoke() methods on the Dispatch interface, generics are
used to determine the return type.
The steps to creating a dynamic client are:

1. Determine if you want your dynamic client to send data
   in `PAYLOAD` or `MESSAGE` mode.
2. Create a service instance and add at least one port to
   it. The port carries the protocol binding and service
   endpoint address information.
3. Create a `Dispatch<T>` object using
   either the `Service.Mode.PAYLOAD` method or the
   `Service.Mode.MESSAGE` method.
4. Configure the request context properties on the
   `jakarta.xml.ws.BindingProvider` interface. Use
   the request context to specify additional properties such
   as enabling HTTP authentication or specifying the endpoint
   address.
5. Compose the client request message for the dynamic
   client.
6. Invoke the service endpoint with the Dispatch client
   either synchronously or asynchronously.
7. Process the response message from the service.

The following example illustrates the steps to create a
Dispatch client and invoke a sample EchoService service
endpoint.

```

   String endpointUrl = ...;
                
   QName serviceName = new QName("http://org/apache/ws/axis2/sample/echo/",
    "EchoService");
   QName portName = new QName("http://org/apache/ws/axis2/sample/echo/",
    "EchoServicePort");
                
   /** Create a service and add at least one port to it. **/ 
   Service service = Service.create(serviceName);
   service.addPort(portName, SOAPBinding.SOAP11HTTP_BINDING, endpointUrl);
                
   /** Create a Dispatch instance from a service.**/ 
   Dispatch<SOAPMessage> dispatch = service.createDispatch(portName, 
   SOAPMessage.class, Service.Mode.MESSAGE);
        
   /** Create SOAPMessage request. **/
   // compose a request message
   MessageFactory mf = MessageFactory.newInstance(SOAPConstants.SOAP_1_1_PROTOCOL);

   // Create a message.  This example works with the SOAPPART.
   SOAPMessage request = mf.createMessage();
   SOAPPart part = request.getSOAPPart();

   // Obtain the SOAPEnvelope and header and body elements.
   SOAPEnvelope env = part.getEnvelope();
   SOAPHeader header = env.getHeader();
   SOAPBody body = env.getBody();

   // Construct the message payload.
   SOAPElement operation = body.addChildElement("invoke", "ns1",
    "http://org/apache/ws/axis2/sample/echo/");
   SOAPElement value = operation.addChildElement("arg0");
   value.addTextNode("ping");
   request.saveChanges();

   /** Invoke the service endpoint. **/
   SOAPMessage response = dispatch.invoke(request);

   /** Process the response. **/
```

## Running a JAX-WS client

A JAX-WS client may be started from the
command line like any other Axis2-based client, including
through the use of the `axis2` shell scripts in
the `bin` directory of the installed runtime.

## Invoking JAX-WS Web services asynchronously

Java API for XML-Based Web Services
(JAX-WS) provides support for invoking Web services using an
asynchronous client invocation. JAX-WS provides support for
both a callback and polling model when calling Web services
asynchronously. Both the callback model and the polling model
are available on the Dispatch client and the Dynamic Proxy
client.
An asynchronous invocation of a Web service sends a request
to the service endpoint and then immediately returns control
to the client program without waiting for the response to
return from the service. JAX-WS asynchronous Web service
clients consume Web services using either the callback
approach or the polling approach. Using a polling model, a
client can issue a request and receive a response object that
is polled to determine if the server has responded. When the
server responds, the actual response is retrieved. Using the
callback model, the client provides a callback handler to
accept and process the inbound response object. The
`handleResponse()` method of the handler is called
when the result is available. Both the polling and callback
models enable the client to focus on continuing to process
work without waiting for a response to return, while
providing for a more dynamic and efficient model to invoke
Web services.

### Using the callback asynchronous invocation model

To
implement an asynchronous invocation that uses the callback
model, the client provides an `AsynchHandler`
callback handler to accept and process the inbound response
object. The client callback handler implements the
`jakarta.xml.ws.AsynchHandler` interface, which
contains the application code that is executed when an
asynchronous response is received from the server. The
`jakarta.xml.ws.AsynchHandler` interface contains
the `handleResponse(java.xml.ws.Response)` method
that is called after the run time has received and processed
the asynchronous response from the server. The response is
delivered to the callback handler in the form of a
`jakarta.xml.ws.Response` object. The response
object returns the response content when the
`get()` method is called. Additionally, if an
error was received, then an exception is returned to the
client during that call. The response method is then invoked
according to the threading model used by the executor method, `java.util.concurrent.Executor` on the client's
`java.xml.ws.Service` instance that was used to
create the Dynamic Proxy or Dispatch client instance. The
executor is used to invoke any asynchronous callbacks
registered by the application. Use the
`setExecutor` and `getExecutor` methods
to modify and retrieve the executor configured for your
service.

### Using the polling asynchronous invocation model

Using
the polling model, a client can issue a request and receive a
response object that can subsequently be polled to determine
if the server has responded. When the server responds, the
actual response can then be retrieved. The response object
returns the response content when the `get()`
method is called. The client receives an object of type
`jakarta.xml.ws.Response` from the
`invokeAsync` method. That `Response`
object is used to monitor the status of the request to the
server, determine when the operation has completed, and to
retrieve the response results.

### Using an asynchronous message exchange

By default, asynchronous client invocations do not have asynchronous
behavior of the message exchange pattern on the wire. The
programming model is asynchronous; however, the exchange of
request or response messages with the server is not
asynchronous. To use an asynchronous message exchange, the
org.apache.axis2.jaxws.use.async.mep property must be set on
the client request context with a boolean value of true. When
this property is enabled, the messages exchanged between the
client and server are different from messages exchanged
synchronously. With an asynchronous exchange, the request and
response messages have WS-Addressing headers added that
provide additional routing information for the messages.
Another major difference between asynchronous and synchronous
message exchange is that the response is delivered to an
asynchronous listener that then delivers that response back
to the client. For asynchronous exchanges, there is no
timeout that is sent to notify the client to stop listening
for a response. To force the client to stop waiting for a
response, issue a `Response.cancel()` method on
the object returned from a polling invocation or a
`Future.cancel()` method on the object returned
from a callback invocation. The cancel response does not
affect the server when processing a request.
The steps necessary to invoke a Web service asynchronously
are:

1. Determine if you want to implement the callback method
   or the polling method for the client to asynchronously
   invoke the Web service.
2. (Optional) Configure the client request context. Add
   the
   `org.apache.axis2.jaxws.use.async.mep`
   property to the request context to enable asynchronous
   messaging for the Web services client. Using this
   property requires that the service endpoint supports
   WS-Addressing which is supported by default for the
   application server. The following example demonstrates
   how to set this property:

```

           Map<String, Object> rc = ((BindingProvider) port).getRequestContext();
           rc.put("org.apache.axis2.jaxws.use.async.mep", Boolean.TRUE);
```

3. To implement the asynchronous callback method, perform
   the following steps.
   1. Find the asynchronous callback method on the SEI or
      `jakarta.xml.ws.Dispatch` interface. For an
      SEI, the method name ends in `Async` and has
      one more parameter than the synchronous method of type
      `jakarta.xml.ws.AsyncHandler`. The
      `invokeAsync(Object, AsyncHandler)` method
      is the one that is used on the Dispatch interface.
   2. (Optional) Add the `service.setExecutor`
      methods to the client application. Adding the executor
      methods gives the client control of the scheduling
      methods for processing the response. You can also
      choose to use the `java.current.Executors`
      class factory to obtain packaged executors or implement
      your own executor class. See the JAX-WS specification
      for more information on using executor class methods
      with your client.
   3. Implement the
      `jakarta.xml.ws.AsynchHandler` interface. The
      `jakarta.xml.ws.AsynchHandler` interface only
      has the
      `handleResponse(jakarta.xml.ws.Response)`
      method. The method must contain the logic for
      processing the response or possibly an exception. The
      method is called after the client run time has received
      and processed the asynchronous response from the
      server.
   4. Invoke the asynchronous callback method with the
      parameter data and the callback handler.
   5. The `handleResponse(Response)` method is
      invoked on the callback object when the response is
      available. The `Response.get()` method is
      called within this method to deliver the response.
4. To implement the polling method,
   1. Find the asynchronous polling method on the SEI or
      `jakarta.xml.ws.Dispatch` interface. For an
      SEI, the method name ends in `Async` and has
      a return type of `jakarta.xml.ws.Response`.
      The `invokeAsync(Object)` method is used on
      the Dispatch interface.
   2. Invoke the asynchronous polling method with the
      parameter data.
   3. The client receives the object type,
      `jakarta.xml.ws.Response`, that is used to
      monitor the status of the request to the server. The
      `isDone()` method indicates whether the
      invocation has completed. When the
      `isDone()` method returns a value of true,
      call the `get()` method to retrieve the
      response object.
5. Use the `cancel()` method for the callback
   or polling method if the client needs to stop waiting for a
   response from the service. If the `cancel()`
   method is invoked by the client, the endpoint continues to
   process the request. However, the wait and response
   processing for the client is stopped.

When developing Dynamic Proxy clients, after you generate the
portable client artifacts from a WSDL file using the
**wsimport** command, the generated service endpoint
interface (SEI) does not have asynchronous methods included
in the interface. Use JAX-WS bindings to add the asynchronous
callback or polling methods on the interface for the Dynamic
Proxy client. To enable asynchronous mappings, you can add
the `jaxws:enableAsyncMapping` binding declaration
to the WSDL file. For more information on adding binding
customizations to generate an asynchronous interface, see
chapter 8 of the JAX-WS specification.
Note: When you run the **wsimport** tool and enable
asynchronous invocation through the use of the JAX-WS
`enableAsyncMapping` binding declaration, ensure
that the corresponding response message your WSDL file does
not contain parts. When a response message does not contain
parts, the request acts as a two-way request, but the actual
response that is sent back is empty. The **wsimport** tool
does not correctly handle a void response. To avoid this
scenario, you can remove the output message from the
operation which makes your operation a one-way operation or
you can add a <wsdl:part> to your message. For more
information on the usage, syntax and parameters for the
**wsimport** tool, see the **wsimport** command for
JAX-WS applications documentation.
The following example illustrates a Web service interface
with methods for asynchronous requests from the client.

```

   @WebService

   public interface CreditRatingService {
          // Synchronous operation.
          Score getCreditScore(Customer     customer);
          // Asynchronous operation with polling.
          Response<Score> getCreditScoreAsync(Customer customer);
          // Asynchronous operation with callback.
          Future<?> getQuoteAsync(Customer customer, 
                 AsyncHandler<Score> handler);
   }
```

Using the callback method The callback method requires a
callback handler that is shown in the following example. When using
the callback procedure, after a request is made, the callback
handler is responsible for handling the response. The response
value is a response or possibly an exception. The
`Future<?>` method represents the result of an
asynchronous computation and is checked to see if the computation
is complete. When you want the application to find out if the
request is completed, invoke the `Future.isDone()`
method. Note that the `Future.get()` method does not
provide a meaningful response and is not similar to the `Response.get()` method.

```

   CreditRatingService svc = ...;
 
   Future<?> invocation = svc.getCreditScoreAsync(customerTom,
          new AsyncHandler<Score>() {
                 public void handleResponse (
                        Response<Score> response)
                     {
                        score = response.get();
                        // process the request...
                     }
       }
  );
```

Using the polling method The following example illustrates an
asynchronous polling client:

```

   CreditRatingService svc = ...;
   Response<Score> response = svc.getCreditScoreAsync(customerTom);
 
   while (!response.isDone()) {
          // Do something while we wait.
   }
 

   score = response.get();
```

## Using handlers in JAX-WS Web services

As in the Java API for XML-based RPC
(JAX-RPC) programming model, the JAX-WS programming model
provides an application handler facility that enables you to
manipulate a message on either an inbound or an outbound
flow. You can add handlers into the JAX-WS runtime
environment to perform additional processing of request and
response messages. You can use handlers for a variety of
purposes such as capturing and logging information and adding
security or other information to a message. Because of the
support for additional protocols beyond SOAP, JAX-WS provides
two different classifications for handlers. One type of
handler is a logical handler that is protocol independent and
can obtain the message in the flow as an extensible markup
language (XML) message. The logical handlers operate on
message context properties and message payload. These
handlers must implement the
`jakarta.xml.ws.handler.LogicalHandler` interface. A
logical handler receives a `LogicalMessageContext`
object from which the handler can get the message
information. Logical handlers can exist on both SOAP and
XML/HTTP-based configurations.
The second type of handler is a protocol handler. The
protocol handlers operate on message context properties and
protocol-specific messages. Protocol handlers are limited to
SOAP-based configurations and must implement the
`jakarta.xml.ws.handler.soap.SOAPHandler` interface.
Protocol handlers receive the message as a
`jakarta.xml.soap.SOAPMessage` to read the message
data.
The JAX-WS runtime makes no distinction between server-side
and client-side handler classes. The runtime does not
distinguish between inbound or outbound flow when a
`handleMessage(MessageContext)` method or
`handleFault(MessageContext)` method for a
specific handler is invoked. You must configure the handlers
for the server or client, and implement sufficient logic
within these methods to detect the inbound or outbound
direction of the current message.
To use handlers with Web services client applications, you
must add the `@HandlerChain` annotation to the
service endpoint interface or the generated service class and
provide the handler chain configuration file. The
`@HandlerChain` annotation contains a file
attribute that points to a handler chain configuration file
that you create. For Web services client applications, you
can also configure the handler chain programmatically using
the Binding API. To modify the `handlerchain`
class programmatically, use either the default implementation
or a custom implementation of the
`HandlerResolver` method.
To use handlers with your server application, you must set
the `@HandlerChain` annotation on either the
service endpoint interface or the endpoint implementation
class, and provide the associated handler chain configuration
file. Handlers for the server are only configured by setting
the `@HandlerChain` annotation on the service
endpoint implementation or the implementation class. The
handler classes must be included in the deployed
artifact.
For both server and client implementations of handlers using
the `@HandlerChain` annotation, you must specify
the location of the handler configuration as either a
relative path from the annotated file or as an absolute URL.
For example:

```

   @HandlerChain(file="../../common/handlers/myhandlers.xml")
```

or

```

   @HandlerChain(file="http://foo.com/myhandlers.xml")
```

For more information on the schema of the handler
configuration file, see the JSR 181 specification.
For more information regarding JAX-WS handlers, see chapter 9
of the JAX-WS specification.
To create a JAX-WS handler:

1. Determine if you want to implement JAX-WS handlers on
   the service or the client.
   1. Use the default implementation of a handler
      resolver. The runtime now uses the
      `@HandlerChain` annotation and the default
      implementation of `HandlerResolver` class to
      build the handler chain. You can obtain the existing
      handler chain from the `Binding`, add or
      remove handlers, and then return the modified handler
      chain to the `Binding` object.
   2. To use a custom implementation of a handler
      resolver, set the custom `HandlerResolver`
      class on the `Service` instance. The runtime
      uses your custom implementation of the
      `HandlerResolver` class to build the handler
      chain, and the default runtime implementation is not
      used. In this scenario, the `@HandlerChain`
      annotation is not read when retrieving the handler
      chain from the binding after the custom
      `HandlerResolver` instance is registered on
      the `Service` instance. You can obtain the
      existing handler chain from the `Binding`,
      add or remove handlers, and then return the modified
      handler chain to the `Binding` object.
2. Configure the client handlers by setting the
   `@HandlerChain` annotation on the service
   instance or service endpoint interface, or you can modify
   the handler chain programmatically to control how the
   handler chain is built in the runtime. If you choose to
   modify the handler chain programmatically, then you must
   determine if you will use the default handler resolver or
   use a custom implementation of a handler resolver that is
   registered on the service instance. A service instance uses
   a handler resolver when creating binding providers. When
   the binding providers are created, the handler resolver
   that is registered with a service is used to create a
   handler chain and the handler chain is subsequently used to
   configure the binding provider.
3. Configure the server handlers by setting the
   `@HandlerChain` annotation on the service
   endpoint interface or implementation class. When the
   `@HandlerChain` annotation is configured on both
   the service endpoint interface and the implementation
   class, the implementation class takes priority.
4. Create the handler chain configuration XML file. You
   must create a handler chain configuration XML file for the
   `@HandlerChain` to reference.
5. Add the handler chain configuration XML file in the
   class path for the service endpoint interface when
   configuring the server or client handlers using the
   `@HandlerChain` annotation. You must also
   include the handler classes contained in the configuration
   XML file in your class path.
6. Write your handler implementation.

The following example illustrates the steps necessary to
configure JAX-WS handlers on a service endpoint interface
using the `@HandlerChain` annotation.
The `@HandlerChain` annotation has a file
attribute that points to a handler chain configuration XML
file that you create. The following file illustrates a
typical handler configuration file. The
`protocol-bindings`, `port-name-pattern`, and
`service-name-pattern` elements are all filters
that are used to restrict which services can apply the
handlers.

```

   <?xml version="1.0" encoding="UTF-8"?>

   <jws:handler-chains xmlns:jws="http://java.sun.com/xml/ns/javaee">
   <!-- Note:  The '*" denotes a wildcard. -->

        <jws:handler-chain name="MyHandlerChain">
                <jws:protocol-bindings>##SOAP11_HTTP ##ANOTHER_BINDING</jws:protocol-bindings>
                <jws:port-name-pattern 
                 xmlns:ns1="http://handlersample.samples.apache.org/">ns1:MySampl*</jws:port-name-pattern>
           <jws:service-name-pattern 
                 xmlns:ns1="http://handlersample.samples.apache.org/">ns1:*</jws:service-name-pattern>
                <jws:handler>
                        <jws:handler-class>org.apache.samples.handlersample.SampleLogicalHandler</jws:handler-class>
                </jws:handler>
                <jws:handler>
                        <jws:handler-class>org.apache.samples.handlersample.SampleProtocolHandler2</jws:handler-class>
                </jws:handler>
                <jws:handler>
                        <jws:handler-class>org.apache.samples.handlersample.SampleLogicalHandler</jws:handler-class>
                </jws:handler>
                <jws:handler>
                        <jws:handler-class>org.apache.samples.handlersample.SampleProtocolHandler2</jws:handler-class>
                </jws:handler>
        </jws:handler-chain>
        
   </jws:handler-chains>
```

Make sure that you add the handler.xml file and the handler
classes contained in the handler.xml file in your class path.
The following example demonstrates a handler implementation:

```

   package org.apache.samples.handlersample;

   import java.util.Set;

   import javax.xml.namespace.QName;
   import jakarta.xml.ws.handler.MessageContext;
   import jakarta.xml.ws.handler.soap.SOAPMessageContext;

   public class SampleProtocolHandler implements
           jakarta.xml.ws.handler.soap.SOAPHandler<SOAPMessageContext> {

       public void close(MessageContext messagecontext) {
       }

       public Set<QName> getHeaders() {
           return null;
       }

       public boolean handleFault(SOAPMessageContext messagecontext) {
           return true;
       }

       public boolean handleMessage(SOAPMessageContext messagecontext) {
           Boolean outbound = (Boolean) messagecontext.get(MessageContext.MESSAGE_OUTBOUND_PROPERTY);
           if (outbound) {
               // Include your steps for the outbound flow.
           }
           return true;
       }

   }
```

## Enabling HTTP session management support for JAX-WS applications

You can use HTTP session management to
maintain user state information on the server, while passing
minimal information back to the user to track the session.
You can implement HTTP session management on the application
server using either session cookies or URL rewriting.
The interaction between the browser, application server, and
application is transparent to the user and the application
program. The application and the user are typically not aware
of the session identifier provided by the server.

### Session cookies

The HTTP maintain session feature
uses a single cookie, `JSESSIONID`, and this
cookie contains the session identifier. This cookie is used
to associate the request with information stored on the
server for that session. On subsequent requests from the
JAX-WS application, the session ID is transmitted as part of
the request header, which enables the application to
associate each request for a given session ID with prior
requests from that user. The JAX-WS client applications
retrieve the session ID from the HTTP response headers and
then use those IDs in subsequent requests by setting the
session ID in the HTTP request headers.

### URL rewriting

URL rewriting works like a redirected
URL as it stores the session identifier in the URL. The
session identifier is encoded as a parameter on any link or
form that is submitted from a Web page. This encoded URL is
used for subsequent requests to the same server.
To enable HTTP session management:

1. Configure the server to enable session tracking.
2. Enable session management on the client by setting the
   JAX-WS property,
   `jakarta.xml.ws.session.maintain`, to true on the
   `BindingProvider`.

```

      Map<String, Object> rc = ((BindingProvider) port).getRequestContext();
      ...
      ...
      rc.put(BindingProvider.SESSION_MAINTAIN_PROPERTY, Boolean.TRUE);
      ...
      ...
   
```

## Enabling MTOM

JAX-WS
supports the use of SOAP Message Transmission Optimized
Mechanism (MTOM) for sending binary attachment data. By
enabling MTOM, you can send and receive binary data optimally
without incurring the cost of data encoding to ensure the
data is included in the XML document.
JAX-WS applications can send binary data as base64 or
hexBinary encoded data contained within the XML document.
However, to take advantage of the optimizations provided by
MTOM, enable MTOM to send binary base64 data as attachments
contained outside the XML document. MTOM optimization is only
available for the xs:base64Binary data type. The MTOM option
is not enabled by default. JAX-WS applications require
separate configuration of both the client and the server
artifacts to enable MTOM support. For the server, MTOM can be
enabled on a JAX-WS JavaBeans endpoint only and not on a
provider-based endpoint.
To enable MTOM on an endpoint, use the @BindingType
(jakarta.xml.ws.BindingType) annotation on a server endpoint
implementation class to specify that the endpoint supports
one of the MTOM binding types so that the response messages
are MTOM-enabled. The jakarta.xml.ws.SOAPBinding class defines
two different constants, SOAP11HTTP\_MTOM\_BINDING and
SOAP12HTTP\_MTOM\_BINDING that you can use for the value of the
@BindingType annotation. For example:

```

   // for SOAP version 1.1
   @BindingType(value = SOAPBinding.SOAP11HTTP_MTOM_BINDING)
   // for SOAP version 1.2
   @BindingType(value = SOAPBinding.SOAP12HTTP_MTOM_BINDING)
```

Enable MTOM on the client by using the
jakarta.xml.ws.soap.SOAPBinding client-side API. Enabling MTOM
on the client optimizes the binary messages that are sent to
the server.

- Enable MTOM on a Dispatch client.
- The following example uses
  SOAP version 1.1:
  - First method: Using
    SOAPBinding.setMTOMEnabled()
  -
```

             SOAPBinding binding = (SOAPBinding)dispatch.getBinding();
             binding.setMTOMEnabled(true);
         
```

  - Second method: Using Service.addPort()
  -
```

 
             Service svc = Service.create(serviceName);
             svc.addPort(portName,SOAPBinding.SOAP11HTTP_MTOM_BINDING,endpointUrl);
         
```

- Enable MTOM on a Dynamic Proxy client.
-
```

          // Create a BindingProvider bp from a proxy port.
          Service svc = Service.create(serviceName);
          MtomSample proxy = svc.getPort(portName, MtomSample.class);
          BindingProvider bp = (BindingProvider) proxy;

          //Enable MTOM
          SOAPBinding binding = (SOAPBinding) bp.getBinding();
          binding.setMTOMEnabled(true);
      
```

---

<a id="docs-pojoguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/pojoguide.html -->

<!-- page_index: 12 -->

# POJO Web Services using Apache Axis2

Want a quick way to get a Web service up and running in no time?
Then you should consider creating a Plain Old Java Object (POJO)
that you can deploy using Apache Axis2 on Apache Tomcat. POJOs are
fast to build and easy to maintain, which means you'll save a lot
of time building and debugging your code. This document shows you
how to take a simple POJO, and deploy it on Apache Tomcat as a Web
service in the exploded directory format. You'll also learn how to
take a POJO based on the Spring Framework, and deploy that as an
AAR packaged Web service on Tomcat.

## Content

- [Introduction](#docs-pojoguide--introduction)
- [The POJO](#docs-pojoguide--pojo)
- [POJO Web service using Apache Axis2 and
  Tomcat](#docs-pojoguide--pojows)
  - [Defining the Service:
    services.xml](#docs-pojoguide--definingservice)
- [Building the POJO Web Service Using
  Ant](#docs-pojoguide--buildpojows)
- [Testing the POJO Web Service Using
  RPCServiceClient](#docs-pojoguide--testingpojows)
  - [Limitations and Strengths of
    POJO](#docs-pojoguide--limitationspojo)
- [Spring-based POJO Web Service](#docs-pojoguide--springpojows)
  - [Quick Introduction](#docs-pojoguide--quickintro)
  - [The Service Definition:
    services.xml](#docs-pojoguide--servicedef)
  - [Initializing the Spring
    application context: SpringInit](#docs-pojoguide--initializingspring)
  - [Testing Using an
    RPCServiceClient](#docs-pojoguide--testingrpc)
- [JSR 181 Annotation support with POJO Web services](#docs-pojoguide--jsr181pojows)
  - [Sample JSR 181 POJO Web Service](#docs-pojoguide--jsr181definingservice)
- [Summary](#docs-pojoguide--summary)
- [For Further Study](#docs-pojoguide--furtherstudy)

## Introduction

The task of building a Web service can sometimes be
overwhelming, but not with POJOs! The old-school Plain Old Java
Object is a simple and quick way to get most, if not all, of your
currently existing Java classes up on the Web as readily accessible
Web services. This document describes how to build a POJO-style Web
service with Apache Axis2 and Tomcat. It is organized as
follows:

- The POJO: This is the Java class that you'll use throughout
  this document
- POJO deployment
- Test the POJO Web service using an RPC based client
- Limitations of straight POJO
- Spring-based POJO Web service and deployment

The code for the document can be found at
Axis2\_HOME/samples/pojoguide and Axis2\_HOME/samples/pojoguidespring
once you extract the [Axis2
Standard Distribution](https://axis.apache.org/axis2/java/core/download.cgi). (It is better to get it now as it will
help you to follow along.) Let's get started.

## The POJO

The POJO you'll be using throughout this document is a Weather
service POJO that consists of two classes: WeatherService and
Weather. Weather contains the Weather data: Temperature, forecast, rain (will it rain?), and howMuchRain (See Code Listing 1).

**Code Listing 1: The Weather POJO**

```

package sample.pojo.data;

public class Weather{
    float temperature;
    String forecast;
    boolean rain;
    float howMuchRain;
    
    public void setTemperature(float temp){
        temperature = temp;
    }

    public float getTemperature(){
        return temperature;
    }
    
    public void setForecast(String fore){
        forecast = fore;
    }

    public String getForecast(){
        return forecast;
    }
    
    public void setRain(boolean r){
        rain = r;
    }

    public boolean getRain(){
        return rain;
    }
    
    public void setHowMuchRain(float howMuch){
        howMuchRain = howMuch;
    }

    public float getHowMuchRain(){
        return howMuchRain;
    }
}
```

And here's the WeatherService class, shown in Code Listing
2.

**Code Listing 2: The WeatherService class**

```

package sample.pojo.service;

import sample.pojo.data.Weather;

public class WeatherService{
    Weather weather;
    
    public void setWeather(Weather weather){
        this.weather = weather;
    }

    public Weather getWeather(){
        return this.weather;
    }
}
```

Note that it's all just straight POJOs with field items and
`getter` and `setter` methods for each field.
Next, you'll take a look at what you need to do to make it ready
for deployment on Apache Axis2 and Tomcat.

## POJO Web Service Using Apache Axis2 and Tomcat

Got the POJOs? Great. This section will show you how to package
them in the exploded directory format for easy deployment. First
you'll look at the services.xml file that defines the Web service, and then you'll build the files using [Apache Ant](http://ant.apache.org/), and deploy the Web service
on Tomcat.

### Defining the Service: services.xml

Before Axis2 can understand what is going on, you have to tell
it to use the services.xml file. Let's get right into it (see Code
Listing 3).

**Code Listing 3: The service definition file:
services.xml**

```

<service name="WeatherService" scope="application">
    <description>
        Weather POJO Service
    </description>
    <messageReceivers>
        <messageReceiver 
            mep="http://www.w3.org/ns/wsdl/in-only"
    class="org.apache.axis2.rpc.receivers.RPCInOnlyMessageReceiver"/>
        <messageReceiver
            mep="http://www.w3.org/ns/wsdl/in-out"
    class="org.apache.axis2.rpc.receivers.RPCMessageReceiver"/>
    </messageReceivers>
    <parameter name="ServiceClass">
        sample.pojo.service.WeatherService
    </parameter>
</service>
```

The name of the service is specified as WeatherService and the
scope of the service is application. As you can see in the
WeatherService POJO, there are two methods: IN-ONLY method and
IN-OUT method. Hence the messageReceiver elements are ordered
within the messageReceivers tag. Lastly, the ServiceClass parameter
specifies the class of the Web service, which is
sample.pojo.service.WeatherService. When operations of your Web
service get called, the methods of the WeatherService class will be
called. Next let usl take a look at an easy method of building your
application using Ant.

## Building the POJO Web Service Using Apache Ant

[Ant](http://ant.apache.org/) is a slick build tool.
It helps reduce the time to build the applications, and several of
the Axis2 command-line tools create the build.xml files for you.
(We will not be going into too much detail on the build.xml file
that you'll be using.)

Here are the main Ant tasks you'll be using:

- generate.service -- This Ant task builds the service relevant
  source, and copies the files to build/WeatherService
- rpc.client -- This task builds the client relevant files,
  builds a JAR at *build/lib/rpc-client.jar*, and then runs
  the client

Before you can build the source, you'll need to download the
Axis2 2.0.0-bin and 2.0.0-war distributions
from [here](https://axis.apache.org/axis2/java/core/download.cgi). Then
modify the following line inside the build.xml file (in the
Axis2\_HOME/samples/pojoguide directory in the extracted Axis2
2.0.0 Standard Binary (bin) Distribution) :

```

<property name="axis2.home" value="c:\apps\axis2" />
```

This modification contains the path to the root of the unzipped
Axis2 2.0.0-bin [download](https://axis.apache.org/axis2/java/core/download.cgi).
With that explanation, you'll now build the source by typing the
following: ant

The following directory format should now exist at
build/WeatherService:

```

 - WeatherService
   - META-INF
     - services.xml
   - sample
     - pojo
       - data
         - Weather.class
       - service
         - WeatherService.class
```

Simple isn't it? An excellent way to dive into Web services
development.

Now get a [Tomcat](http://tomcat.apache.org/)
distribution (I used v5.5), and start it up by running
*bin/startup.bat* or *bin/startup.sh*. Once it's
running, deploy the Axis2 2.0.0-war by copying the
axis2.war file to Tomcat's webapps directory. Tomcat will proceed
by deploying axis2 and un-archiving it into the webapps directory.
Now copy the WeatherService directory that was created at the time
of building our project to:
*<tomcat-home>/webapps/axis2/WEB-INF/services*.

The service should deploy quickly. You willl test the Web
service using the RPCServiceClient in the next section.

## Testing the POJO Web Service Using RPCServiceClient

OK, so the Web service should be running on Tomcat. Now you'll
build a simple RPCServiceClient and test the POJO Web service.
You'll first start out with the class constructs, creating the
RPCServiceClient and initializing the values of the Weather class
within the Web service (See Code Listing 4).

**Code Listing 4: Setting the weather**

```

package sample.pojo.rpcclient;

import javax.xml.namespace.QName;

import org.apache.axis2.AxisFault;
import org.apache.axis2.addressing.EndpointReference;
import org.apache.axis2.client.Options;
import org.apache.axis2.rpc.client.RPCServiceClient;

import sample.pojo.data.Weather;


public class WeatherRPCClient {

    public static void main(String[] args1) throws AxisFault {

        RPCServiceClient serviceClient = new RPCServiceClient();

        Options options = serviceClient.getOptions();

        EndpointReference targetEPR = new EndpointReference(
                "http://localhost:8080/axis2/services/WeatherService");
        options.setTo(targetEPR);

        // Setting the weather
        QName opSetWeather =
            new QName("http://service.pojo.sample/xsd", "setWeather");

        Weather w = new Weather();

        w.setTemperature((float)39.3);
        w.setForecast("Cloudy with showers");
        w.setRain(true);
        w.setHowMuchRain((float)4.5);

        Object[] opSetWeatherArgs = new Object[] { w };

        serviceClient.invokeRobust(opSetWeather, opSetWeatherArgs);
...
```

The most interesting code to note is in bold font. Notice the
targetEPR variable you create, setting the endpoint reference to
http://localhost:8080/axis2/services/WeatherService. This is where
you deployed it on Axis2. You can also verify this by asking Axis2
to list its services by going to the following URL:
http://localhost:8080/axis2/services/listServices.

Next the opSetWeather variable gets setup, pointing to the
setWeather operation. Then the Weather data is created and
initialized. Lastly, you invoke the Web service, which initializes
the weather data (you'll verify this soon). Next you get back the
weather data (see Code Listing 5).

**Code Listing 5: Getting the weather data**

```

...
        serviceClient.invokeRobust(opSetWeather, opSetWeatherArgs);

        // Getting the weather
        QName opGetWeather =
            new QName("http://service.pojo.sample/xsd", "getWeather");

        Object[] opGetWeatherArgs = new Object[] { };
        Class[] returnTypes = new Class[] { Weather.class };
        
        Object[] response = serviceClient.invokeBlocking(opGetWeather,
                opGetWeatherArgs, returnTypes);
        
        Weather result = (Weather) response[0];
        
        if (result == null) {
            System.out.println("Weather didn't initialize!");
            return;
        }
...
```

First you set the operation in opGetWeather to getWeather. Then
you create an empty argument list. Note that this time you expect
something back from the Web service, and so you create a list of
return types. Then you invoke the Web service using a blocking call
and wait for the weather data to be returned to you, and you place
it in the result variable. Lastly, you make sure it isn't null and
that it was successfully initialized by the previous call to
setWeather. Now display the data to verify it. (see Code Listing
6).

**Code Listing 6: Displaying the data**

```

...
            return;
        }

        // Displaying the result
        System.out.println("Temperature               : " +
                           result.getTemperature());
        System.out.println("Forecast                  : " +
                           result.getForecast());
        System.out.println("Rain                      : " +
                           result.getRain());
        System.out.println("How much rain (in inches) : " +
                           result.getHowMuchRain());
        
    }
}
```

You should receive the data shown in Code Listing 7.

**Code Listing 7: Output from running the client**

```

rpc.client.run:
     [java] Temperature               : 39.3
     [java] Forecast                  : Cloudy with showers
     [java] Rain                      : true
     [java] How much rain (in inches) : 4.5
```

Excellent! You have a working POJO Web service! Next you'll
quickly morph this one into a Spring based POJO.

### Limitations and Strengths of POJO

We've covered the strengths of using POJO based Web services, but what about any limitations? One main limitation of POJO based
Web services is the lack of initialization support (meaning that
you have to go into your Web service and initialize the values
before the Web service is completely useful). However, you'll soon
see how to overcome that limitation with a Spring based POJO, which
is covered next.

## Spring-based POJO Web Service

Spring is a hot framework for J2EE and makes bean usage a
breeze. You'll use it in this section to create a Spring based POJO
Web service. For this section, you'll need the spring.jar from the
latest 1.x Spring download.

### Quick Introduction

If you take a look at the source code of this document in
Axis2\_HOME/samples/pojoguidespring (to see how the Spring based
POJO Web service is coded), you can see that the Weather class
didn't change at all and the WeatherService class only got its name
changed to WeatherSpringService.

You'll also notice an applicationContext.xml file, which we'll
cover later. It is used to setup the beans used in our Web
service.

Now you might wonder what the SpringInit.java class is for. This
service is necessary to initialize the Spring Framework's
application context.

The client is pretty much the same, except you won't use it to
initialize the Weather data in the Web service, since Spring does
that for you using Inversion of Control (IoC), which is covered
next.

### The Service Definition: services.xml

Since the core POJOs didn't change, you move straight to the
services.xml file. It's a bit longer this time because it
instantiates two services in one file (see Code Listing 7).

**Code Listing 7: Defining the services: services.xml**

```

<serviceGroup>
  <service name="SpringInit" 
class="sample.spring.service.SpringInit">
    <description>
      This web service initializes Spring.
    </description>
    <parameter name="ServiceClass">
        sample.spring.service.SpringInit
    </parameter>
    <parameter name="ServiceTCCL">composite</parameter>
    <parameter name="load-on-startup">true</parameter>
    <operation name="springInit">
      <messageReceiver 
      class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
  </service>
  <service name="WeatherSpringService">
    <description>
      Weather Spring POJO Axis2 AAR deployment
    </description>
    <parameter name="ServiceClass">
        sample.spring.service.WeatherSpringService
    </parameter>
    <parameter name="ServiceObjectSupplier">
org.apache.axis2.extensions.spring.receivers.SpringAppContextAwareObjectSupplier
    </parameter>
    <parameter name="SpringBeanName">
        weatherSpringService
    </parameter>
    <messageReceivers>
      <messageReceiver mep="http://www.w3.org/ns/wsdl/in-only"
      class="org.apache.axis2.rpc.receivers.RPCInOnlyMessageReceiver"/>
      <messageReceiver mep="http://www.w3.org/ns/wsdl/in-out"
      class="org.apache.axis2.rpc.receivers.RPCMessageReceiver"/>
    </messageReceivers>
  </service>
</serviceGroup>
```

You'll see a few familiar items in the above listing, and
several changes. Once again, the items in bold are most important.
The ServiceTCCL property under the SpringInit service makes sure
that the Spring class loader is used for the Web service, allowing
it to properly instantiate the Spring application context. The
load-on-startup variable is a must-have so that the service loads
up immediately on startup, creating the Spring application context.
The WeatherSpringService stays similar to the WeatherService
previously with a couple of additions: The ServiceObjectSupplier
provides the service with the Spring application context, making it
"Spring Aware."

Lastly, the SpringBeanName points to the name of the bean
associated with this Web service, which is defined in the
applicationContext.xml file (essentially the WeatherSpringService).
We'll cover the applicationContext.xml file next. The application
context, applicationContext.xml file tells the Spring Framework
what beans are defined. For this example, you'll define three of
them (see Code Listing 8).

**Code Listing 8: Defining the application context:
applicationContext.xml**

```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" 
"http://www.springframework.org/dtd/spring-beans.dtd">

<beans>
  <bean id="applicationContext" class=
"org.apache.axis2.extensions.spring.receivers.ApplicationContextHolder" />

  <bean id="weatherSpringService" 
        class="sample.spring.service.WeatherSpringService">
    <property name="weather" ref="weatherBean"/>
  </bean>

  <bean id="weatherBean" class="sample.spring.bean.Weather">
    <property name="temperature" value="89.9"/>
    <property name="forecast" value="Sunny"/>
    <property name="rain" value="false"/>
    <property name="howMuchRain" value="0.2"/>
  </bean>
</beans>
```

The first one is Axis2's hook into Spring's application context
(needed since AAR deployment is quite different from regular WAR
deployment). Next, you define the bean to which the services.xml
file points, which is the weatherSpringService bean that points to
the WeatherSpringService class. It has one field property that gets
initialized by the Spring Framework - weather. This will be set to
the weatherBean. The weatherBean is an instantiation of the Weather
class that holds information on the weather. Spring will initialize
it to the values shown above, and set the Weather object in the
WeatherSpringService class to the weatherBean instantiation. Thus, when you deploy the Web service, you won't have to instantiate the
values because they'll already be set.

Next up is the SpringInit class.

### Initializing the Spring Application Context: SpringInit

Without the Spring application context being initialized
quickly, you'll run into problems. The SpringInit class initializes
the Spring application context on startup because it is a
ServiceLifeCycle class whose startUp method gets called upon
loading the class (and because its load-on-startup property is set
in the services.xml file). The only code worth mentioning in this
class is shown in Code Listing 9.

**Code Listing 9: SpringInit's startUp method**

```

    public void startUp(ConfigurationContext ignore,
                        AxisService service) {
        ClassLoader classLoader = service.getClassLoader();
        ClassPathXmlApplicationContext appCtx = new
            ClassPathXmlApplicationContext(new String[]
                                           {"applicationContext.xml"}, 
                                           false);
        appCtx.setClassLoader(classLoader);
        appCtx.refresh();
        if (logger.isDebugEnabled()) {
            logger.debug("\n\nstartUp() set spring classloader " +
                         "via axisService.getClassLoader() ... ");
        }
    }
```

Note that this method retrieves the Spring class loader, and
creates an application context with applicationContext.xml as the
parameters. This new application context then gets the Spring class
loader as its class loader. The Spring Framework is now up and
ready for our WeatherSpringService.

### Build and Deploy Using Apache Axis2 and Tomcat

Your POJO is now ready for primetime within the Spring
Framework. Before you build, you'll first need to make sure the
axis2-spring-2.0.0.jar and spring.jar files are in the
project's *Axis2\_HOME/lib* directory.

**Note:** The service will not deploy if you add
the above .jar files to the service archive due to class loding
issues.

Now build the source and create an AAR file by typing: ant

It'll be created at *target/WeatherSpringService.aar*.
Copy it to
*<tomcat-home>/webapps/axis2/WEB-INF/services*, and
Axis2 should deploy it quickly.

Next, test the Web service to see whether Spring will really
initialize the weather data for you.

### Testing Using an RPCServiceClient

It's as simple as it was for the other Web service, except this
time type: ant rpc.client

Feel free to browse the code for this client in
src/client/WeatherSpringRPCClient.java. Essentially, this client
does the same thing as the client testing the WeatherService.
Except that this one skips the "Setting the weather" task since the
weather data should have already been set by the Spring framework
at startup.

Thus, you should get the following as output from the
client:

```

run.client:
    [javac] Compiling 1 source file to C:\axis2-2.0.0\samples\pojoguidespring\build\cl
asses
     [java] Temperature               : 89.9
     [java] Forecast                  : Sunny
     [java] Rain                      : false
     [java] How much rain (in inches) : 0.2
```

Which are exactly the values you set in the
applicationContext.xml file!

## SR 181 Annotation support with POJO Web services

Got the JSR 181 annotated POJOs? Great. This section will show you how to package
them in to a jar format for easy pojo deployment with the help of Axis2 POJO deployer.
First create the JSR 181 Annotated class.

### Sample JSR 181 POJO Web Service

For example lets assume that our JSR 181 Annotated class is.

```

@WebService(name="JSR181TestService" targetNamespace="http://www.test.org/jsr181/Example")
@SOAPBinding(style=SOAPBinding.Style.RPC)
public class TestService {
    @WebMethod(operationName = "echoMethod")
    public String echoString(@WebParam(name="stringIn")String s){
        return s;
    }
}
```

Compile this with the help of the Axis2 libs in to a jar file.
Add one additional like to the axis2.xml to deploy jar files on the pojo directory

```

        Ex: <deployer extension=".jar" directory="pojo" class="org.apache.axis2.deployment.POJODeployer"/>
    
```

Create a pojo directory if its not already there under the Axis2 repository and put the JSR 181 Annotated
jar inside that and start Axis2. You will see the service up and running !!

## Summary

Apache Axis2 is an excellent way to expose your POJOs as Web
services. Spring adds greater flexibility to your POJOs by adding
beans support and initialization abilities, along with all the
other goodies provided by the Spring framework.

## For Further Study

[Axis2 Architecture](#docs-axis2architectureguide)

Introduction to Apache Axis2-<http://www.redhat.com/magazine/021jul06/features/apache_axis2/>

[Working With Apache Axis2](http://wso2.org/library/259)

Apache Tomcat-[http://tomcat.apache.org](http://tomcat.apache.org/)

Spring Framework-<http://www.springframework.org/>

---

<a id="docs-spring"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/spring.html -->

<!-- page_index: 13 -->

# Axis2 Integration with the Spring Framework

This document is a guide on how to use Axis2 with the Spring Framework

For users of JSON and [Spring Boot](https://spring.io/projects/spring-boot)
- or anyone interesed in a complete Spring Boot example that includes Spring Security -
see the sample application in the [JSON and Spring Boot User's Guide.](#docs-json-springboot-userguide)

Update: Spring inside the AAR is no longer supported. See this commit:

```

commit 9e392c0ae1f0abab3d4956fbf4c0818c9570021e
Author: Andreas Veithen <veithen@apache.org>
Date:   Sat May 6 22:21:10 2017 +0000

    AXIS2-3919: Remove the alternate class loading mechanism:
    - It degrades performance.
    - There is no test coverage for it.
    - With r1794157 in place, in most cases, no temporary files will be created and there is no need for a fallback mechanism.
```

## Content

- [Introduction](#docs-spring--a1)
- [Configuring Axis2 to be Spring Aware](#docs-spring--a2)
  - [Programming Model](#docs-spring--a21)
  - [Simple Spring Config Example](#docs-spring--a22)
  - [With a ServletContext](#docs-spring--a23)
  - [Without a ServletContext](#docs-spring--a24)
  - [Putting it All Together](#docs-spring--a25)

## Introduction

Axis2 and Spring integration takes place when Spring supplies one of its
pre-loaded beans to the Axis2 Message Receiver defined in the AAR
services.xml. Axis2 typically uses reflection to instantiate the ServiceClass
defined in the services.xml used by the Message Receiver. Alternatively, you
can define a ServiceObjectSupplier that will supply the Object.

This guide describes how to use two separate ServiceObjectSupplier classes
that are a part of the Axis2 standard distribution - one for use with a
ServletContext, and one without. Configuring Axis2 with a ServletContext is
simpler than without, and is recommended for most use cases. Without a
ServletContext, ie, Spring inside the AAR, requires an extra Spring bean
and is considered an advanced use case. Once configured, the Web service itself
acts like any other Spring wired bean. These Spring beans can be loaded any way
desired as Axis2 has no configuration file dependencies from Spring. Spring
versions 1.2.6, 1.2.8 and 2.0 have been tested, but probably any version
would work as only the core functionality is required.

This guide assumes some basic knowledge of Axis2. See the [User's Guide](#docs-userguide) for more information.

### Programming Model

From an Axis2 standpoint, two hooks are needed to be placed into the AAR
services.xml - the ServiceObjectSupplier that hooks Axis2 and Spring
together, and the name of the Spring bean that Axis2 will use as the service.
All Message Receivers are currently supported, as would be any Message
Receiver that extends org.apache.axis2.receivers.AbstractMessageReceiver .

### Simple Spring Config Example

For the purpose of this example, we'll configure Spring via a WAR file's
web.xml. Let's add a context-param and a listener:

```
<listener>
        <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
<context-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>/WEB-INF/applicationContext.xml</param-value>
</context-param>
```

Next we will show two examples of Spring's /WEB-INF/applicationContext.xml
referenced in the web.xml listener - one using a ServletContext, and one
without.

### With a ServletContext

This example (with a ServletContext) applicationContext.xml should be
familiar to any Spring user:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">

<beans>
  <!-- Axis2 Web Service, but to Spring, its just another bean that has dependencies -->
  <bean id="springAwareService" class="spring.SpringAwareService">
    <property name="myBean" ref="myBean"/>
  </bean>

  <!-- just another bean / interface with a wired implementation, that's injected by Spring
          into the Web Service -->
   <bean id="myBean" class="spring.MyBeanImpl">
     <property name="val" value="Spring, emerge thyself" />
  </bean>
</beans>
```

If the service is running in a Servlet Container, i.e., Axis2 will be able
to get a hold of the ServletContext, the services.xml for the example would
be using SpringServletContextObjectSupplier such as:

```
 <service name="SpringAwareService">
    <description>
        simple spring example
    </description>
    <parameter name="ServiceObjectSupplier">org.apache.axis2.extensions.spring.receivers.SpringServletContextObjectSupplier</parameter>
    <parameter name="SpringBeanName">springAwareService</parameter>
    <operation name="getValue">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
</service> 
```

While the above example uses RawXMLINOutMessageReceiver as its
messageReceiver class, all Message Receivers are currently supported, as
would be any Message Receiver that extends
org.apache.axis2.receivers.AbstractMessageReceiver .

### Without a ServletContext

In case Axis2 can't get a ServletContext, (i.e., uses a different
transport or is running Axis2 inside the AAR etc,) you have the option of
defining a bean that takes advantage of Spring's internal abilities
(ApplicationContextAware interface, specifically) to provide an Application
Context to Axis2, with a bean ref 'applicationContext' :

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">

<beans>
  <!-- Configure spring to give a hook to axis2 without a ServletContext -->
  <bean id="applicationContext" 
    class="org.apache.axis2.extensions.spring.receivers.ApplicationContextHolder" />

  <!-- Axis2 Web Service, but to Spring, its just another bean that has dependencies -->
  <bean id="springAwareService"
        class="spring.SpringAwareService">
    <property name="myBean" ref="myBean" />
  </bean>

  <!-- just another bean with a wired implementation, that's injected by Spring 
          into the Web Service -->
   <bean id="myBean"
        class="spring.MyBeanImpl">
     <property name="val" value="Spring, emerge thyself" />
  </bean>
</beans>
```

If the service is **not** running in a Servlet Container, i.e., Axis2 will not be able to get a hold of ServletContext or you prefer
not to, the services.xml for the example will be using
SpringAppContextAwareObjectSupplier such as:

```
 <service name="SpringAwareService">
    <description>
        simple spring example
    </description>
    <parameter name="ServiceObjectSupplier">org.apache.axis2.extensions.spring.receivers.SpringAppContextAwareObjectSupplier</parameter>
    <parameter name="SpringBeanName">springAwareService</parameter>
    <operation name="getValue">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
</service> 
```

While the above example uses RawXMLINOutMessageReceiver as its
messageReceiver class, all Message Receivers are currently supported, as
would be any Message Receiver that extends
org.apache.axis2.receivers.AbstractMessageReceiver .

In an environment **without a ServletContext**, one way you
could load the applicationContext.xml file is in a place that will be run
once. Upon start-up, execute the following:

```
import org.springframework.context.support.ClassPathXmlApplicationContext;

 public void createSpringAppCtx(ClassLoader cl)
            throws Exception {

    ClassPathXmlApplicationContext ctx = new
      ClassPathXmlApplicationContext(new String[] {Constants.MY_PATH +
      "spring/applicationContext.xml"}, false);
           ctx.setClassLoader(cl);
           ctx.refresh();
```

}

### Putting It All Together

From here, it's just standard Axis2 coding. Only now the service has
Spring wiring capabilities. The implementation is the same whether using
either SpringServletContextObjectSupplier or
SpringAppContextAwareObjectSupplier. The service is as follows:

```
package spring;

import org.apache.axiom.om.OMAbstractFactory;
import org.apache.axiom.om.OMElement;
import org.apache.axiom.om.OMFactory;
import org.apache.axiom.om.OMNamespace;
import org.apache.axiom.om.OMText;

public class SpringAwareService {

    private MyBean myBean = null;

    //spring 'injects' this implementation
    public void setMyBean(MyBean myBean) {
            this.myBean = myBean;
    }

    // The web service
    public OMElement getValue(OMElement ignore) {
            OMFactory factory=
                OMAbstractFactory.getOMFactory();
            OMNamespace payloadNs= factory.createOMNamespace(
                "http://springExample.org/example1", "example1");
            OMElement payload =
                factory.createOMElement("string", payloadNs);
            OMText response = factory.createOMText(this.myBean.emerge());
            payload.addChild(response);
            return payload;
    }
} 
```

For those who are new to Spring, one of the ideas is that you program an
Interface, as the implementation is pluggable. This idea is referenced in the
Spring config file above. Below is the interface:

```
package spring;

/** Interface for Spring aware Bean */
public interface MyBean {
         String emerge();
}
```

Here's the implementation:

```
/** Spring wired implementation */
public class MyBeanImpl implements MyBean {

    String str = null;
    // spring 'injects' this value
    public void setVal(String s) {
        str = s;
    }
    // web service gets this value
    public String emerge() {
        return str;
    }
}
```

Lastly here's the client - not really necessary for the example, other
than for completeness:

```
package client;

import java.io.StringWriter;

import javax.xml.stream.XMLOutputFactory;

import org.apache.axiom.om.OMAbstractFactory;
import org.apache.axiom.om.OMElement;
import org.apache.axiom.om.OMFactory;
import org.apache.axiom.om.OMNamespace;
import org.apache.axis2.addressing.EndpointReference;
import org.apache.axis2.client.Options;
import org.apache.axis2.client.ServiceClient;

public class TestClient {
    private static EndpointReference targetEPR =
        new EndpointReference(
               "http://localhost:8080/axis2/services/SpringAwareService");

    /**
     * Simple axis2 client.
     *
     * @param args Main
     */
    public static void main(String[] args) {
        try {
            OMFactory factory = OMAbstractFactory.getOMFactory();
            OMNamespace omNs = factory.createOMNamespace(
                        "http://springExample.org/example1", "example1");

            OMElement method = factory.createOMElement("getValue", omNs);
            OMElement value = factory.createOMElement("Text", omNs);
            value.addChild(factory.createOMText(value, "Some String "));
            method.addChild(value);

            ServiceClient serviceClient = new ServiceClient();

            Options options = new Options();
            serviceClient.setOptions(options);
            options.setTo(targetEPR);

            //Blocking invocation
            OMElement result = serviceClient.sendReceive(method);

            StringWriter writer = new StringWriter();
            result.serialize(XMLOutputFactory.newInstance()
                    .createXMLStreamWriter(writer));
            writer.flush();

            System.out.println("Response: " + writer.toString());
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
} 
```

The examples above assume that both the spring framework .jar and the
axis2-spring-\*.jar are under WEB-INF/lib. In such a case, the classes shown
in this tutorial need to be placed in a JAR under WEB-INF/lib. In this
example the JAR layout is:

```
./mySpring.jar
./META-INF
./META-INF/MANIFEST.MF
./spring
./spring/MyBean.class
./spring/MyBeanImpl.class
./spring/SpringAwareService.class
```

Since all the user classes are in mySpring.jar in this example, the AAR
merely contains the services.xml file:

```
./springExample.aar
./META-INF
./META-INF/MANIFEST.MF
./META-INF/services.xml
```

To run this example, make sure you have the axis2-spring\*.jar that comes
from the axis2-std-\*-bin distro in the server side WEB-INF/lib, as well as
the appropriate Spring jar - most will use the full spring.jar, but the
minimum requirements are spring-core, spring-beans, spring-context, and
spring-web. When running the client, you should see this output:

```
Response: <example1:string xmlns:example1="http://springExample.org/example1" 
  xmlns:tns="http://ws.apache.org/axis2">Spring, emerge thyself</example1:string>
```

---

<a id="docs-modules"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/modules.html -->

<!-- page_index: 14 -->

# Writing Your Own Axis2 Module

Axis2 provides extended support for modules (See the [Architecture
Guide](#docs-axis2architectureguide) for more details about modules in Axis2). Let's create a
custom module and deploy it to MyService, which we created
earlier.

Send your feedback or questions to: [java-dev@axis.apache.org](mailto:java-dev@axis.apache.org?subject=[Axis2]).
( Subscription details are available on the [Axis2 site](#mail-lists).)
Kindly prefix subject with [Axis2].

## Content List

- [MyService with a
  Logging Module](#docs-modules--myservice_with_a_logging_module)
  - [Step1 : LoggingModule
    Class](#docs-modules--step1_.3a_loggingmodule_class)
  - [Step2 : LogHandler](#docs-modules--step2_.3a_loghandler)
  - [Step3 : module.xml](#docs-modules--step3_.3a_module_xml)
  - [Step4:
    Modify the "axis2.xml"](#docs-modules--step_4.3a_modify_the_.22axis2_xml.22)
  - [Step5 :
    Modify the "services.xml](#docs-modules--step5_.3a_modify_the_.22services_xml.22)
  - [Step6 : Packaging](#docs-modules--step6_.3a_packaging)
  - [Step7 : Deploy
    the Module in Axis2](#docs-modules--step7_.3a_deploy_the_module_in_axis2)

The following steps show the actions that need to be performed
to deploy a custom module for a given Web service:

1. Create the Module Implementation
2. Create the Handlers
3. Create the module.xml
4. Modify the "axis2.xml" (if you need
   custom phases)
5. Modify the "services.xml" to engage
   modules at the deployment time.
6. Package in a ".mar" (Module
   Archive)
7. Deploy the module in Axis2

### MyService with a Logging Module

Let's write a simple logging module for our sample located at
the **"samples\userguide\src"** directory of the binary
distribution. This module contains one handler that just logs the
message that is passed through it. Axis2 uses ".mar" (Module
Archive) to deploy modules in Axis2. The following diagram shows
the file structure inside which needs to be there in the ".mar"
archive. Let's create all these and see how it works.

![](assets/images/moduleview_23f968bb8aea1309.jpg)

#### Step1 : LoggingModule Class

LoggingModule is the implementation class of the Axis2 module.
Axis2 modules should implement the "[org.apache.axis2.modules.Module](https://github.com/apache/axis-axis2-java-core/blob/master/modules/kernel/src/org/apache/axis2/modules/Module.java)"
interface with the following methods.

```

public void init(ConfigurationContext configContext, AxisModule module) throws AxisFault;//Initialize the module
public void shutdown(ConfigurationContext configurationContext) throws AxisFault;//End of module processing
public void engageNotify(AxisDescription axisDescription) throws AxisFault;
public void applyPolicy(Policy policy, AxisDescription axisDescription) throws AxisFault ;
public boolean canSupportAssertion(Assertion assertion) ;
```

The first three methods can be used to control the module
initialization and the termination, and the next three methods are
used to perform policy related operations. With the input parameter
AxisConfiguration, the user is provided with the complete
configuration hierarchy. This can be used to fine-tune the module
behavior by the module writers. For a simple logging service, we
can keep these methods blank in our implementation class.

#### Step2 : LogHandler

A module in Axis2 can contain, one or more handlers that perform
various SOAP header processing at different phases. (See the
[Architecture Guide](#docs-axis2architectureguide--incomingsoap) for more information on phases). To
write a handler one should implement [org.apache.axis2.engine.Handler](https://github.com/apache/axis-axis2-java-core/blob/master/modules/kernel/src/org/apache/axis2/engine/Handler.java). But for convenience, [org.apache.axis2.handlers.AbstractHandler](https://github.com/apache/axis-axis2-java-core/blob/master/modules/kernel/src/org/apache/axis2/handlers/AbstractHandler.java) provides an abstract
implementation of the Handler interface.

For the logging module, we will write a handler with the
following methods. "public void invoke(MessageContext ctx);" is the
method that is called by the Axis2 engine when the control is
passed to the handler. "public void revoke(MessageContext ctx);" is
called when the handlers are revoked by the Axis2 engine.

```

public class LogHandler extends AbstractHandler implements Handler {
    private static final Log log = LogFactory.getLog(LogHandler.class);
    private String name;

    public String getName() {
        return name;
    }

    public InvocationResponse invoke(MessageContext msgContext) throws AxisFault {
        log.info(msgContext.getEnvelope().toString());
        return InvocationResponse.CONTINUE;        
    }

    public void revoke(MessageContext msgContext) {
        log.info(msgContext.getEnvelope().toString());
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

#### Step3 : module.xml

"module.xml" contains the deployment configurations for a
particular module. It contains details such as the Implementation
class of the module (in this example it is the "LoggingModule"
class and various handlers that will run in different phases). The
"module.xml" for the logging module will be as follows:

```

<module name="sample-logging" class="userguide.loggingmodule.LoggingModule">
   <InFlow>
        <handler name="InFlowLogHandler" class="userguide.loggingmodule.LogHandler">
        <order phase="loggingPhase" />
        </handler>
   </InFlow>

   <OutFlow>
        <handler name="OutFlowLogHandler" class="userguide.loggingmodule.LogHandler">
        <order phase="loggingPhase"/>
        </handler>
   </OutFlow>

   <OutFaultFlow>
        <handler name="FaultOutFlowLogHandler" class="userguide.loggingmodule.LogHandler">
        <order phase="loggingPhase"/>
        </handler>
   </OutFaultFlow>

   <InFaultFlow>
        <handler name="FaultInFlowLogHandler" class="userguide.loggingmodule.LogHandler">
        <order phase="loggingPhase"/>
        </handler>
   </InFaultFlow>
</module>
```

As you can see, there are four flows defined in the
"module.xml"

1. InFlow Represents the handler chain that will run when a
   message is coming in.
2. OutFlow Represents the handler chain
   that will run when the message is going out.
3. OutFaultFlow - Represents the handler
   chain that will run when there is a fault, and the fault is going
   out.
4. InFaultFlow - Represents the handler chain that will run when
   there is a fault, and the fault is coming in.

The following set of tags describe the name of the handler, handler class, and the phase in which this handler is going to run.
"InFlowLogHandler" is the name given for the particular instance of
this handler class. The value of the class attribute is the actual
implementation class for this handler. Since we are writing a
logging handler, we can reuse the same handler in all these phases.
However, this may not be the same for all the modules. "<order
phase="loggingPhase" />" describes the phase in which this
handler runs.

```

<handler name="InFlowLogHandler" class="userguide.loggingmodule.LogHandler">
<order phase="loggingPhase" />
</handler>
```

To learn more about Phase rules, check out the article [Axis2 Execution Framework](http://www.developer.com/java/web/article.php/3529321)

#### Step 4: Modify the "axis2.xml"

In this handler, the "loggingPhase", is defined by the module
writer. It is not a pre-defined handler phase, hence the module
writer should introduce it to the "axis2.xml" (NOT the
services.xml) so that the Axis2 engine knows where to place the
handler in different "flows" (inFlow, outFlow, etc.). The following
XML lines show the respective changes made to the "axis2.xml" in
order to deploy the logging module in the Axis2 engine. This is an
extract of the phase section of "axis2.xml".

```

<!-- ================================================= -->
<!-- Phases -->
<!-- ================================================= -->

<phaseOrder type="inflow">
        <!--  System pre defined phases       -->
        <phase name="TransportIn"/>
        <phase name="PreDispatch"/>
        <phase name="Dispatch" class="org.apache.axis2.engine.DispatchPhase">
            <handler name="AddressingBasedDispatcher"
                     class="org.apache.axis2.dispatchers.AddressingBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="RequestURIBasedDispatcher"
                     class="org.apache.axis2.dispatchers.RequestURIBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPActionBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPActionBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPMessageBodyBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPMessageBodyBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="InstanceDispatcher"
                     class="org.apache.axis2.engine.InstanceDispatcher">
                <order phase="PostDispatch"/>
            </handler>
        </phase>
        <!--  System pre defined phases       -->
        <!--   After Postdispatch phase module author or service author can add any phase he wants      -->
        <phase name="OperationInPhase"/>
                <phase name="loggingPhase"/>
    </phaseOrder>
    <phaseOrder type="outflow">
        <!--      user can add his own phases to this area  -->
        <phase name="OperationOutPhase"/>
        <phase name="loggingPhase"/>
        <!--system predefined phases-->
        <!--these phases will run irrespective of the service-->
        <phase name="PolicyDetermination"/>
        <phase name="MessageOut"/>
    </phaseOrder/>
    <phaseOrder type="INfaultflow">
        <!--      user can add his own phases to this area  -->
        <phase name="OperationInFaultPhase"/>
        <phase name="loggingPhase"/>
    </phaseOrder>
    <phaseOrder type="Outfaultflow">
        <!--      user can add his own phases to this area  -->
        <phase name="OperationOutFaultPhase"/>
        <phase name="loggingPhase"/>
        <phase name="PolicyDetermination"/>
        <phase name="MessageOut"/>
    </phaseOrder>
    
```

The text in green, the custom phase "loggingPhase" is placed in
all the flows, hence that phase will be called in all the message
flows in the engine. Since our module is associated with this
phase, the LogHandler inside the module will now be executed in
this phase.

#### Step5 : Modify the "services.xml"

Up to this point, we have created the required classes and
configuration descriptions for the logging module, and by changing
the "axis2.xml" we created the required phases for the logging
module.

Next step is to "**engage**" (use) this module in one of our
services. (Hint: it is often easier to edit the axis2.xml for global logging). For this, let's use the same Web service that we have
used throughout the user's guide- MyService. However, since we need
to modify the "services.xml" of MyService in order to engage this
module, we use a separate Web service, but with similar
operations.

The code for this service can be found in the
"**Axis2\_HOME/samples/userguide/src/userguide/example2**"
directory. The simple changes that we have done to "services.xml'
are shown in green in the following lines of xml.

```

<service name="MyServiceWithModule">
    <description>
    This is a sample Web service with a logging module engaged.
    </description>
    <module ref="logging"/>
    <parameter name="ServiceClass" locked="xsd:false">userguide.example2.MyService</parameter>
    <operation name="echo">
    <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
    <operation name="ping">
    <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
</service>
```

In this example, we have changed the service name (the
implementation class is very similar to what we have used earlier, although it is in a different package). In addition we have added
the line **"<module ref="logging"/>"** to "services.xml".
This informs the Axis2 engine that the module "logging" should be
engaged for this service. The handler inside the module will be
executed in their respective phases as described by the
"module.xml".

#### Step6 : Packaging

Before deploying the module, we need to create the ".mar" file
for this module. This can be done, using the "jar" command and then
renaming the created .jar file. Else, you can find the
"logging.mar" that has already been created in the
"**Axis2\_HOME/samples/userguide**" directory.

#### Step7 : Deploy the Module in Axis2

Deploying a module in Axis2 requires the user to create a
directory with the name "modules" in the "webapps/axis2/WEB-INF"
directory of their servlet container, and then copying the ".mar"
file to that directory. So let's first create the "modules"
directory and drop the "logging.mar" into this directory.

Although the required changes to the "services.xml" is very
little, we have created a separate service archive
(MyServiceWithModule.aar) for users to deploy the service..

Deploy this service using the same steps used in the ['Step 4: Deploy Web
Service'](#docs-adv-userguide--step5_deploy_web_service) sub section in '[Writing a New Service using
Codegeneration](#docs-userguide--ws_codegen)', and copy the "logging.mar" file to the
"modules" directory.

Then run 'ant run.client.servicewithmodule' from
**axis2home/samples/userguide directory**

**Note (on samples):** All the samples
mentioned in the user's guide are located at the
**"samples\userguide\src"** directory of the binary
distribution.

---

<a id="docs-clustering-guide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/clustering-guide.html -->

<!-- page_index: 15 -->

# Axis2 Clustering Support

Are you interested in improving Scalability and High Availability of your Web Services?

Axis2 1.4 provides experimental clustering support to add ***Scalability, Failover and High Availability*** to your Web Services.
This guide will explain the extent of clustering support and it's the current limitations.
It also highlights the recommended approaches using examples.

Axis2 clustering support can be used in several scenarios.
However it is important to understand the current limitations and the risks/impacts associated with each scenario.

## Content

- [Introduction](#docs-clustering-guide--introduction)
- [Scalability](#docs-clustering-guide--scalability)
- [Failover](#docs-clustering-guide--failover)
- [High Availability](#docs-clustering-guide--ha)
- [Clustering for Stateless Web Services](#docs-clustering-guide--stateless_webservices)
- [Clustering for Stateful Web Services](#docs-clustering-guide--stateful_web_services)
- [Configuring Axis2 to add Clustering Support](#docs-clustering-guide--config)
- [Example 1: Scalability and HA with Stateless Web Services](#docs-clustering-guide--scalability_stateless_example)
- [Example 2: Failover for Stateful Web Services](#docs-clustering-guide--failover_stateful_example)
- [Example 3: Scalability and HA with Stateful Web Services](#docs-clustering-guide--scalability_stateful_example)
- [Summary](#docs-clustering-guide--summary)
- [For Further Study](#docs-clustering-guide--furtherstudy)

## Introduction

In the context of Axis2 clustering, a node is defined as a separate process with a unique port number where it listens for requests on a given transport . A physical machine can contain more than one node.

## Scalability

In order to maintain the same level of serviceability (QoS) during an increase in load you need the ability to scale.
Axis2 provides replication support to scale horizontally. That is, you can deploy the same service in more than one node to share the work load, thereby increasing or maintaining the same level of serviceability (throughput etc).

## Failover

Axis2 provides excellent support for Failover by replicating to backup node(s).
If you deploy your Stateful Web Services in this mode, you can designate 1-2 backups and replicate state.
In the event the primary node fails, the clients can switch to one of the backups.
If you use Synapse with the Failover mediator you can provide transparent Failover.

## High Availability

You can improve the availability of your Web Service by using the following Axis2 functionality.

- **Failover** support will ensure that a client will continued be served, without any interruption due to a node failure.
- **Scalability** support will ensure that your services can maintain the same level of serviceability/availability (QoS) in increased load conditions.
- **Hot Deploy** feature ensures that you could deploy new services without shutting down your existing services.

## Clustering for Stateless Web Services

This is the simplest use case.
If your Web Service does not store any state in the context hierarchy then you could deploy your service in "n" number of nodes. To ensure identical configuration for your services, you can load from a central repository using the URLBasedAxisConfigurator. This is not a must, but it makes management of the cluster easy and less error prone.

Since it is stateless no explicit replication is needed. If a node fails any other node in the cluster can take over. You can use a load balancer to direct requests based on a particular algorithm (Ex: Round Robin, Weight based, Affinity based). You can increase the no of nodes to handle scalability (to scale vertically) without worrying about the overhead of replication as the services are stateless

## Clustering for Stateful Web Services

This is a more complicated use case where your Web Service needs to store state in the context hierarchy. Each Web Service instance (deployed in separate nodes) will need to share state among themselves. Axis2 provides replication to support sharing of state among services.

However, if more than one node tries to update the same state in the context hierarchy, conflicts will arise and the integrity of your data will be compromised. Now your cluster will have inconsistent state. This can be avoided using a locking mechanism. However Axis2 currently does not support it yet.

If this shared state is read more frequently and updated rarely the probability of conflicts decrease. You may use Axis2 in the above use case for Stateful Web Services based on your discretion. However it's important to remember that there can be conflicts.***If you have frequent writes it is not advisable to use Axis2 until we introduce locking support***

Please note this warning is only applicable to the following use cases.

- Your Service is deployed in Application Scope
- You store information in the ServiceGroupContext (irrespective of your scope)

You may safely use services in "soapsession" scope provided you ***don't modify (or modify at all) state in ServiceGroupContext frequently***. In soap-session the service context is exclusive to the client who owns the session. Therefore only that client can modify state. A conflict might arise if the same client tries to access the same service in two different nodes simultaneously which happens to modify the same state. However this is rare, but might arise due to an error in the load balancer or the client. If you use Sticky sessions, it will ensure that state will be changed in one node only by directing all requests by the same client to the same node. This is the safest way to use Axis2 clustering support for Stateful Web Services to acheive scalability.

## Configuring Axis2 to add Clustering Support

You need to add the following snippet to your axis2.xml

```

   <cluster class="org.apache.axis2.clustering.tribes.TribesClusterManager">
     <contextManager class="org.apache.axis2.clustering.context.DefaultContextManager">
        <listener class="org.apache.axis2.clustering.context.DefaultContextManagerListener"/>
        <replication>
            <defaults>
                <exclude name="local_*"/>
                <exclude name="LOCAL_*"/>
            </defaults>
            <context class="org.apache.axis2.context.ConfigurationContext">
                <exclude name="SequencePropertyBeanMap"/>
                <exclude name="NextMsgBeanMap"/>
                <exclude name="RetransmitterBeanMap"/>
                <exclude name="StorageMapBeanMap"/>
                <exclude name="CreateSequenceBeanMap"/>
                <exclude name="ConfigContextTimeoutInterval"/>
                <exclude name="ContainerManaged"/>
            </context>
            <context class="org.apache.axis2.context.ServiceGroupContext">
                <exclude name="my.sandesha.*"/>
            </context>
            <context class="org.apache.axis2.context.ServiceContext">
                <exclude name="my.sandesha.*"/>
            </context>
        </replication>
     </contextManager>
   </cluster>
```

The exclude tag tells the system to avoid replicating that particular property. This is a useful
feature as you would need to have properties that is node specific only.
The default config in axis2 will have all properties the axis2 system doesn't want to replicate. Web Service developers can also use this to filter out properties that should be local only.

## Example 1: Scalability and HA with Stateless Web Services

The following is a good example for deploying a Stateless Web Service for Scalability and High Availability.
The following service can be deployed in "application" scope in "n" nodes using a central repository.
Once state is loaded by a particular node it will be shared by other nodes as the config context will replicate the data.
Even if two nodes load the data at the same time, there want be any conflicts as it is the same set of data.
(All nodes should synchronize their clocks using a time server to avoid loading different sets of data)

For the sake of this example we assume replication is cheaper than querying the database.
So once queried it will be replicated to the cluster

```

/**
 * This Service is responsible for providing the top 5
 * stocks for the day, week or quarter
 */
public class Top5StockService
{
	public String[] getTop5StocksForToday()
	{
		// If cache is null or invalid fetch it from data base
		ConfigurationContext configContext =
            MessageContext.getCurrentMessageContext().getConfigurationContext();
		
		String[]  symbols = (String[])configContext.getProperty(TOP5_TODAY);
		if (!checkValidity(configContext.getProperty(TOP5_TODAY_LOAD_TIME)))
                {
		    symbols = loadFromDatabase(TOP5_TODAY);
                    configContext.setProperty(TOP5_TODAY,symbols);
		    configContext.setProperty(TOP5_TODAY_LOAD_TIME,new java.util.Date()); 	 
                } 
		
		return symbols;
	}
	
	public String[] getTop5StocksForTheWeek()
	{
		 // If cache is null or invalid fetch it from data base
		.............
	}
	
	public String[] getTop5StocksForTheQuarter()
	{
		// If cache is null or invalid fetch it from data base
                ............
	}
}
```

## Example 2: Failover for Stateful Web Services

The following example demonstrates Failover support by replicating state in a service deployed in "soapsession" scope.
You can deploy the service in 2 nodes. Then point a client to the first node and add a few items to the shopping cart.
Assuming the primary node has crashed, point the client to the backup node. You should be able to checkout the cart with the items you added in the first node.

```

public class ShoppingCart
{	
	public final static String SHOPPING_CART = "SHOPPING_CART";
	public final static String DISCOUNT = "DISCOUNT";
	
	public void createSession()
	{
		List<Item> cart = new ArrayList<Item>();
		ServiceContext serviceContext =
            MessageContext.getCurrentMessageContext().getServiceContext();
		serviceContext.setProperty(SHOPPING_CART, cart);
	}
	
	public void addItem(Item item)
	{
		ServiceContext serviceContext =
            MessageContext.getCurrentMessageContext().getServiceContext();
		List<Item> cart = (List<Item>)serviceContext.getProperty(SHOPPING_CART);
		cart.add(item);
	}
	
	public void removeItem(Item item)
	{
		ServiceContext serviceContext =
            MessageContext.getCurrentMessageContext().getServiceContext();
		List<Item> cart = (List<Item>)serviceContext.getProperty(SHOPPING_CART);
		cart.remove(item);
	}
	
	public double checkout()
	{
		ServiceContext serviceContext =
            MessageContext.getCurrentMessageContext().getServiceContext();
		List<Item> cart = (List<Item>)serviceContext.getProperty(SHOPPING_CART);
		
		double discount = (Double)serviceContext.getServiceGroupContext().getProperty(DISCOUNT);
		
		double total = 0;
		for (Item i : cart)
		{
			total = total + i.getPrice();
		}
		
		total = total - total * (discount/100);
		
		return total;
	}	
}
```

## Example3: Scalability and HA with Stateful Web Services

You can deploy the the above Shopping Cart service in several active nodes (with a backup(s) for each node).
You only replicate to your backup nodes for Failover. The load balancer should ensure sticky sessions.
The strategy is to partition your load between the active nodes to achieve scalability and replication to the backups to achieve Failover. These in turn will increase the high availability of your services. Since the above example doesn't use Service Group Context to write any state there want be any conflicts.

For the sake of this example we assume that all read only properties for the Service Group Context is loaded at initialization
***Please note this is the recommended approach for Stateful Web Services due to the current limitations***

## Summary

Apache Axis2 provides experimental support for clustering to improve the following properties of your Web Services.

- Scalability
- Failover
- High Availability

It is important to understand the current limitations when leveraging clustering support.

## For Further Study

[Apache Axis2](#index)

[Axis2 Architecture](#docs-axis2architectureguide)

Introduction to Apache Axis2-<http://www.redhat.com/magazine/021jul06/features/apache_axis2/>

---

<a id="docs-adb-adb-howto"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/adb/adb-howto.html -->

<!-- page_index: 16 -->

# Axis2 Databinding Framework

This document aims to provide an architectural overview of the
Axis2 Databinding Framework (referred to as ADB from here onwards)
and be a guide to anyone who wants to use and modify ADB. The
information is presented under the following topics.

## Content

- [Introduction](#docs-adb-adb-howto--intro)
- [Architectural Overview](#docs-adb-adb-howto--archi)
- [Code and Dependencies](#docs-adb-adb-howto--code_depend)
- [Invoking the ADB Code Generator](#docs-adb-adb-howto--code_gen)
  - [As a Stand-alone Schema
    Compiler](#docs-adb-adb-howto--schema_compiler)
  - [Through the API](#docs-adb-adb-howto--api)
- [Generation Modes](#docs-adb-adb-howto--gen_modes)
- [Deep into Generated Code](#docs-adb-adb-howto--deep)
  - [An Example!](#docs-adb-adb-howto--example)
- [Known Limitations](#docs-adb-adb-howto--limitation)
- [Want to Learn More?](#docs-adb-adb-howto--more)

## Introduction

The objective of the Axis2 Databinding framework is to provide a
lightweight and simple schema compiler/Java bean generator for
Axis2. By no means is it intended to be a fully functional schema
compiler like XMLBeans. Note that ADB is written in a fashion that
allows it to be used as a stand-alone schema compiler and also to
be extended to generate code for other languages.

## Architectural Overview

ADB is built on a modular architecture that allows it to utilize
a pre-configured writer depending on the configuration. The 'big
block diagram' for the code generator architecture is depicted
below.

![ADB architecture](assets/images/adb_adc6e709003546b5.jpg)

ADB utilizes the WS-Commons [XmlSchema
library](http://ws.apache.org/commons/XmlSchema/index.html) for reading the Schema. The object model for the schema
comes in the form of an XmlSchema object. The schema compiler keeps
an instance of the writer (in the default case it's the
JavaBeanWriter) which actually writes the classes. The writers may
use whatever technique they prefer, in the case of the
JavaBeanWriter, it uses an XSLT template. The SchemaCompiler also
uses a typemapper object that tells it what classnames to use for
the QNames that it encounters. This type mapper is also part of the
configuration and the users can override the default type mapper by
overriding the property setting.

## Code and Dependencies

As explained in the previous section, the schema compiler
depends on the WS-Commons XmlSchema library. The XSLT
transformations are dependent on the JVM's DOM implementation
(either Crimson or Xerces) which means that the underlying JVM
should be 1.4 or higher. Apart from that ADB has no dependencies on
any other special jar files. The code for the schema compiler is
completely in the **org.apache.axis2.schema.\***
package. This package resides in the codegen module of the Axis2
source tree.

The following are the important classes and files of ADB:

1. **SchemaCompiler** - The work horse that really
   compiles the schema into classes.
2. **BeanWriter** - BeanWriters handle the the actual
   rendering of the classes. BeanWriter is the interface that writers
   need to implement in order to be used by the SchemaCompiler.
3. **JavaBeanWriter** - The default implementation of
   the BeanWriter interface.
4. **TypeMap** - represents the interface that the
   schema compiler uses to find class names for a given QName.
5. **JavaTypeMap** - the default implementation of
   the TypeMap
6. **ADBBeanTemplate.xsl** - the XSLtemplate the
   JavaBeanWriter uses.
7. **Schema-compile.properties** - The property file
   for the schema compiler

The easiest way to obtain the ADB binaries is to run the maven
build for the Axis2 adb-codegen module. This will generate the
**axis2-adb-codegen-{$version}.jar** inside the target
folder which is directly usable when the ADB schema compiler is
required.

The runtime dependencies for the ADB generated classes is in the
Axis2 adb module and the kernal module. Hence to compile and work
with the generated classes the
**axis2-adb-{$version}.jar** and
**axis2-kernal-{$version}.jar** needs to be in the
classpath in addition to other dependencies such as StAX, Axiom, Commons-logging and javax.activation.

## Invoking the ADB Code Generator

### As a Standalone Schema Compiler

ADB comes with a XSD2Java code generator that allows the schemas
to be compiled just by giving the schema file reference. This main
class is presently rather primitive and does not provide much
control over the code generation process. This is bound to improve
in the near future.

XSD2Java accepts the following parameters:

1. The Schema file name - This should be a complete file name
   pointing to the local file system
2. The output folder name - This should be the name of a folder
   within the local file system

Since the code generator presently has no validations built into
it, the compiler is likely to show various error messages if these
parameters are not supplied properly.

### Through the API

This is the only way to harness the full potential of the schema
compiler. The current Axis2 integration of ADB happens through this
API. The most important classes and methods of the Schema compiler
are as follows.

- **SchemaCompiler - Constructor**

  The constructor of the schema compiler expects a CompilerOptions
  object. This compilerOptions object is more of a holder for the
  parameters that are passed to the SchemaCompiler. The only
  mandatory parameter in the CompilerOptions is the output
  directory.
- **SchemaCompiler - Compile(XMLSchema schema)**

  The compile method to call for a single schema. The expected
  object is a XMLSchema which is part of the XmlSchema library.
- **SchemaCompiler - Compile(List schemaList)**

  Similar to the previous method but accepts a list of schemas
  instead of one.

For a comprehensive code sample in invoking the schema compiler
through the API, the following classes would be helpful. One would
also need an understanding of the generation modes of the ADB
schema compiler when using it through the API. Hence the following
section includes a brief description of the generation modes.

- **org.apache.axis2.schema.XSD2Java**
- **org.apache.axis2.schema.ExtensionUtility**

## Generation Modes

ADB extension provides several generation modes for the data
bound classes.

1. **Integrated Mode**

   In this mode the classes are generated as inner classes of the
   stub, message receiver or the interface. The ADB framework does not
   actually write the classes but instead provides a map of DOM
   document objects that contains the model for the databinding
   classes. The Axis2 codegen engine in turn parses these documents
   within its own XSLT parser to create the necessary classes.
   Implementers are free to use these models differently for their own
   particular needs.

   Integrated mode is intended to be used by tool builders.
2. **Wrapped Mode**

   In the wrapped mode, the ADB databinder generates one class that
   contains all the databound classes. This is convenient when the
   number of classes need to be limited.
3. **Expanded Mode**

   This is the usual mode where the code generator generates a
   class for each of the outer elements and the named complex types.
   The command line tool (XSD2Java) always generates code in the
   expanded mode.

The rules for generating code (described in the next section)
applies regardless of the mode. Switching these modes can be done
by passing the correct options via the CompilerOptions object. The
following table lists the options and the effects of using
them.

|  |  |
| --- | --- |
| **Field Name in Options** | **Description** |
| writeOutput | This determines whether to write the output or not. If the flag is on then the classes will be written by ADB. The default is off. |
| wrapClasses | This determines whether to wrap the generated classes. If the flag is on then a single class (with adb added to the end of the specified package) will be generated. The default is off. |
| mapperClassPackage | The package name for the mapper class. Please see the advanced section for details of the mapper class. |
| helperMode | The switch that determines whether to switch to helper mode or not. Please see the advanced section for details of helper mode. |
| ns2PackageMap | A map that stores the namespace name against the package name These details are used to override the default packages |

## Deep into Generated Code

When the schema compiler is invoked (one-way or another) it
generates code depending on the following rules:

1. All named complex types become bean classes. Any attribute or
   element encapsulated in this complex type will become a field in
   the generated class. Note that the support for constructs other
   than xsd:sequence and xsd:all is not yet implemented.
2. All top level elements become classes. This is a rather obvious
   feature since unless classes are generated for the top level
   elements the handling of elements becomes difficult and messy!
3. SimpleType restrictions are handled by replacing the relevant
   type with the basetype

Once the code is generated according to the rules it looks like
the following. Consider the following schema:

```

<schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tns="http://soapinterop.org/types" targetNamespace="http://soapinterop.org/types" 
elementFormDefault="qualified" >
<import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>
 <complexType name="SOAPStruct">
  <sequence>
   <element name="varString" type="xsd:string"/>
   <element name="varInt" type="xsd:int"/>
   <element name="varFloat" type="xsd:float"/>
  </sequence>
 </complexType>
<element name="myElement" type="tns:SOAPStruct"/>
</schema>
```

For comprehension let us consider the expanded mode for the code
generator. Unless specifically mentioned, the rest of this document
assumes that the expanded mode of the code generation is used. This
particular schema will generate the following two classes in the
designated package, which in this case would be
**org.soapinterop.types**. The package name is derived
from the target namespace of the schema.

1. MyElement.java
2. SOAPStruct.java

As explained earlier, SOAPStruct refers to the complexType.
MyElement is the class that refers to the element. Just as
expected, the SOAPStruct bean has getters and setters for
varString, varInt and varFloat which are String, int and float
respectively. MyElement on the other hand has a single field
representing the SOAPStruct object that it encapsulates.

The most important aspect of the generated code is that it
encapsulates two methods for creating and serializing the beans.
Note that to make this work, the generated beans implement the
**org.apache.axis2.databinding.ADBBean** interface

The creator and serializer methods look like the following:

-
```

public javax.xml.stream.XMLStreamReader
    getPullParser(javax.xml.namespace.QName qName)
```

  This method returns a pull parser that throws the right events
  for this particular object. However there is a subtle difference
  between element based classes and complexType based classes

  1. An element based bean class (like MyElement.java in the
     example) will ***ignore the passed in QName***.
     Instead of using the passed in QName it'll utilize its own QName
     which is embedded in the class under the constant MY\_QNAME, during
     the code generation. Hence it is usual to call getPullparser() with
     a null parameter for elements.
  2. A ComplexType based bean class (like SOAPStruct.java in the
     example) will use the passed-in QName to return an instance of the
     ADBpullparser. This will effectively wrap the elements inside with
     an element having the passed QName
-
```

 public org.apache.axiom.om.OMElement getOMElement(
            final javax.xml.namespace.QName parentQName,
            final org.apache.axiom.om.OMFactory factory){
```

  This method returns an OMElement representing the ADB bean
  object.

  1. Inside the getOMElement method an anonymous ADBDataSource class
     is created. This anonymous class implements a serialize() method
     where the serialization logic for that particular bean class is
     handled. Finally an OMSourcedElementImpl object with the above
     anonymous class type object as the data source is returned.
-
```

 public static [Object].Factory. 
             parse(javax.xml.stream.XMLStreamReader reader) 
             throws java.lang.Exception 
```

  This method returns a populated instance of the class in
  question. Note that


```

[Object]
```

  will be replaced by the actual class that contains this method. Say
  for SOAPStruct the method looks like

```

public static SOAPStruct.Factory. 
                parse(javax.xml.stream.XMLStreamReader reader) 
                throws java.lang.Exception
```

  Also note that the above parse method is available in the
  **Factory** nested class within the relevant top level
  class. Hence one will have to get the static Factory instance
  before calling the parse method.

### An Example!

Consider the following XML fragment

```

<myElement xmlns="http://soapinterop.org/types">
  <varInt>5</varInt>
  <varString>Hello</varString>
  <varFloat>3.3</varFloat>
</myElement>
```

Enthusiastic readers might already have figured out that this
XML fragment complies with the Schema mentioned above. The
following code snippet shows how to build a populated instance of
MyElement with the XML above:

```

XMLStreamReader reader = XMLInputFactory.newInstance().
                                createXMLStreamReader(
                                        new ByteArrayInputStream(xmlString.getBytes()));
MyElement elt = MyElement.Factory.parse(reader);
```

Optionally, the above xml fragment can be reproduced with the
following code fragment:

```

OMElement omElement = myElement.getOMElement
                (MyElement.MY_QNAME, OMAbstractFactory.getSOAP12Factory());
String xmlString = omElement.toStringWithConsume();
```

Although this example takes on the tedious effort of creating a
reader out of a String, inside the Axis2 environment an
XMLStreamReader can be directly obtained from the OMElement! Hence, the parse method becomes a huge advantage for hassle free object
creation.

Similarly the reader obtained from the object can also be
utilized as needed. The following code fragment shows how to
utilize the getPullParser method to create an OMElement :

```

XMLStreamReader reader = elt.getPullParser(null);
OMElement omElt =  new StAXOMBuilder(reader).getDocumentElement();
```

That's all to it! If you are interested in learning more on ADB
the following documents may also be helpful. However, be sure to
check the limitations section that follows if you are planning to
use ADB for something serious.

## Known Limitations

ADB is meant to be a 'Simple' databinding framework and was not
meant to compile all types of schemas. The following limitations
are the most highlighted.

1. Complex Type Extensions and Restrictions.

## Want to Learn More?

- [Advanced features of the ADB code
  generator](#docs-adb-adb-advanced) - explains xsi:type based deserialization and helper
  mode
- [Tweaking the ADB Code Generator](#docs-adb-adb-tweaking)
  - explains available mechanisms to extend ADB and possibly adopt it
  to compile schemas to support other languages.
- [ADB and Axis2
  Integration](#docs-adb-adb-codegen-integration) - explains how the ADB schema compiler was attached
  to the Axis2 framework

---

<a id="docs-adb-adb-advanced"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/adb/adb-advanced.html -->

<!-- page_index: 17 -->

# Advanced Axis2 Databinding Framework Features

The aim of this section is provide an insight into the newly
added advanced features of the Axis2 Databinding (ADB)
Framework.

## Content

- [xsi:type Support](#docs-adb-adb-advanced--typesupport)
- [Helper Mode](#docs-adb-adb-advanced--helper)
- [Additional ADB Topics](#docs-adb-adb-advanced--more)

## xsi:type Support

This is implemented by adding a extension mapping class. The
code that calls the extension mapper is generated inside the
Factory.parse method of the beans and gets activated when the
xsi:type attribute is present. The following code fragment shows
what the generated type mapper looks like :

```

            public static java.lang.Object getTypeObject(java.lang.String namespaceURI,
                                java.lang.String typeName,
                                javax.xml.stream.XMLStreamReader reader) throws java.lang.Exception{
              
                  if (
                  "http://soapinterop.org/types".equals(namespaceURI) &&
                  "SOAPStruct".equals(typeName)){
                            return  com.test.SOAPStruct.Factory.parse(reader);
                  }
              throw new java.lang.RuntimeException("Unsupported type " + namespaceURI + " " + typeName);
            }
```

Inside every Factory.parse method, the extension mapper gets
called when a xsi:type attribute is encountered
**and** that type is not the type that is currently
being parsed.

The following code fragment shows how the ADB deserialize method
calls the mapper class:

```

             if (reader.getAttributeValue("http://www.w3.org/2001/XMLSchema-instance","type")!=null){
                  java.lang.String fullTypeName = reader.getAttributeValue("http://www.w3.org/2001/XMLSchema-instance",
                        "type");
                  if (fullTypeName!=null){
                    java.lang.String nsPrefix = fullTypeName.substring(0,fullTypeName.indexOf(":"));
                    nsPrefix = nsPrefix==null?"":nsPrefix;

                    java.lang.String type = fullTypeName.substring(fullTypeName.indexOf(":")+1);
                    if (!"SOAPStruct".equals(type)){
                        //find namespace for the prefix
                        java.lang.String nsUri = reader.getNamespaceContext().getNamespaceURI(nsPrefix);
                        return (SOAPStruct)org.soapinterop.types.ExtensionMapper.getTypeObject(
                             nsUri,type,reader);
                      }

                  }
              }
```

This makes xsi:type based parsing possible and results in proper
xsi:type based serializations at runtime.

By default, the mapping package is derived from the
targetnamespace of the first schema that is encountered. The
package name can also be explicitly set by a CompilerOption:

```

   
        CompilerOptions compilerOptions = new CompilerOptions();
        compilerOptions.setWriteOutput(true);
        compilerOptions.setMapperClassPackage("com.test");
        compilerOptions.setOutputLocation(new File("src"));
        try {
            SchemaCompiler schemaCompiler = new SchemaCompiler(compilerOptions);
            XmlSchemaCollection xmlSchemaCollection = new XmlSchemaCollection();
            XmlSchema xmlSchema =xmlSchemaCollection.read(new FileReader("schema/sample.xsd"),null);
            schemaCompiler.compile(xmlSchema);
        } catch (Exception e) {
            e.printStackTrace();
        }
```

## Helper mode

Helper mode is a fairly new feature. In the helper mode, the
beans are plain Java beans and all the
deserialization/serialization code is moved to a helper class. For
example, the simple schema mentioned in the ADB-howto document will
yield four classes instead of the two previously generated:

1. MyElement.java
2. MyElementHelper.java
3. SOAPStruct.java
4. SOAPStructHelper.java

The helpers basically contain all the serialization code that
otherwise would go into the ADBBeans. Hence the beans in the helper
mode are much more simplified. Also note that the helper mode is
available only if you are in unpacked mode. The code generator by
default does not expand the classes.

Helper mode can be switched on by using the setHelperMode method
in CompilerOptions:

```

compilerOptions.setHelperMode(true);
```

## Additional ADB Topics

- [Tweaking the ADB Code
  Generator](#docs-adb-adb-tweaking)- explains available mechanisms to extend ADB and
  possibly adopt it to compile schemas to support other
  languages.
- [ADB and Axis2
  Integration](#docs-adb-adb-codegen-integration) - explains how the ADB schema compiler was attached
  to the Axis2 framework

---

---

<a id="docs-adb-adb-codegen-integration"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/adb/adb-codegen-integration.html -->

<!-- page_index: 18 -->

# ADB Integration With Axis2

This document will assist you in writing an extension using the
integrator in order to integrate ADB with Axis2.

## Content

- [Introduction](#docs-adb-adb-codegen-integration--intro)
- [Selection of Generation Modes for
  ADB](#docs-adb-adb-codegen-integration--select_modes)
- [Things to Remember](#docs-adb-adb-codegen-integration--remember)

## Introduction

ADB Integration with Axis2 is simple and straightforward. Given
the extension mechanism of the Axis2 code generator, the obvious
choice for the integrator is to write an extension. The extension
that is added to support ADB is the SimpleDBExtension
(**org.apache.axis2.wsdl.codegen.extension.SimpleDBExtension**)
and can be found in the extensions list of the
codegen-config.properties file.

## Selection of Generation Modes for ADB

The extension sets the options for the code generator via the
CompilerOptions, depending on the user's settings. The following
table summarizes the use of options. Please refer to the [ADB-How to document](#docs-adb-adb-howto) for the
different generation modes and their descriptions.

|  |  |
| --- | --- |
| **User parameters** | **Selected code generation parameters** |
| None (no parameter other than mandatory ones) | wrapClasses=false,writeClasses=false |
| -ss (server side) | wrapClasses=false,writeClasses=true |
| -u (unwrap classes) | wrapClasses=false,writeClasses=true |

The following parameters (prefixed with -E) can be used to
override these settings manually:

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Allowed values** | **Description** |
| r | true, false | Sets the write flag. If set to true the classes will be written by ADB |
| w | true, false | Sets the wrapping flag. if true the classes will be wrapped. |

Note that these parameters have no corresponding long names and
MUST be prefixed with a -E to be processed by the code generator.
For example:

```

WSDL2Java .... -Er true
```

## Things to Remember

1. SimpleDBExtension is for the ADB databinding framework only and
   will process requests only when this framework is specified during
   code generation (using the switch -d adb). In the most recent
   release, the default has been set as ADB and hence if the -d option
   is missing then the databinding framework will be ADB.

---

---

<a id="docs-adb-adb-tweaking"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/adb/adb-tweaking.html -->

<!-- page_index: 19 -->

# ADB Tweaking Guide

This document explains the mechanisms available to extend ADB
and possibly adopt it to compile schemas to support other
languages.

## Content

- [Introduction](#docs-adb-adb-tweaking--intro)
- [Know the Configuration](#docs-adb-adb-tweaking--config)
- [The First Tweak - Generate Plain Java
  Beans](#docs-adb-adb-tweaking--first_tweak)
- [A More Advanced Tweak - Generate Code
  for Another Language](#docs-adb-adb-tweaking--advanced_tweak)

## Introduction

ADB was written with future extensibility in mind, with a clear
and flexible way to extend or modify its functionality. Available
mechanisms to extend ADB and possibly adopt it to compile schemas
to support other languages are described below.

## Know the Configuration

The configuration for the ADB framework is in the
**schema-compile.properties** file found in the
**org.apache.axis2.schema** package. This properties
file has the following important properties

- schema.bean.writer.class

  This is the writer class. This is used by the schema compiler to
  write the beans and should implement the
  **org.apache.axis2.schema.writer.BeanWriter**
  interface. The schema compiler delegates the bean writing task to
  the specified instance of the BeanWriter.
- schema.bean.writer.template

  This specifies the template to be used in the BeanWriter. The
  BeanWriter author is free to use any mechanism to write the classes
  but the default mechanism is to use a xsl template. This property
  may be left blank if the BeanWriter implementation does not use a
  template.
- schema.bean.typemap

  This is the type map to be used by the schema compiler. It
  should be an implementation of the
  **org.apache.axis2.schema.typemap.TypeMap** interface.
  The default typemap implementation encapsulates a hashmap with type
  QName to Class name string mapping.

## The First Tweak - Generate Plain Java Beans

The first, most simple tweak for the code generator could be to
switch to plain bean generation. The default behavior of the ADB
framework is to generate ADBBeans, but most users, if they want to
use ADB as a standalone compiler, would prefer to have plain java
beans. This can in fact be done by simply changing the template
used.

The template for plain java beans is already available in the
**org.apache.axis2.schema.template** package. To make
this work replace the
**/org/apache/axis2/databinding/schema/template/ADBBeanTemplate.xsl**
with the
**/org/apache/axis2/databinding/schema/template/PlainBeanTemplate.xsl**
in the schema-compile.properties**.**

Congratulations! You just tweaked ADB to generate plain java
beans.

To generate custom formats, the templates need to be modified.
The schema for the xml generated by the JavaBeanWriter is available
in the source tree under the Other directory in the codegen module.
Advanced users with knowledge of XSLT can easily modify the
templates to generate code in their own formats.

## A More Advanced Tweak - Generate Code for Another Language

To generate code for another language, there are two main
components that need to be written.

- The BeanWriter

  Implement the BeanWriter interface for this class. A nice
  example is the
  **org.apache.axis2.schema.writer.JavaBeanWriter**
  which has a lot of reusable code. In fact if the target language is
  object-oriented (such as C# or even C++), one would even be able to
  extend the JavaBeanWriter itself.
- The TypeMap

  Implement the TypeMap interface for this class. The
  **org.apache.axis2.schema.typemap.JavaTypeMap** class
  is a simple implementation for the typemap where the QName to class
  name strings are kept inside a hashmap instance. This technique is
  fairly sufficient and only the type names would need to change to
  support another language.

Surprisingly, this is all that needs to be done to have other
language support for ADB. Change the configuration and you are
ready to generate code for other languages!

This tweaking guide is supposed to be a simple guideline for
anyone who wishes to dig deep into the mechanics of the ADB code
generator. Users are free to experiment with it and modify the
schema compiler accordingly to their needs. Also note that the
intention of this section is *not* to be a step by step
guide to custom code generation. Anyone who wish to do so would
need to dig into the code and get their hands dirty!

---

<a id="docs-jibx-jibx-codegen-integration"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/jibx/jibx-codegen-integration.html -->

<!-- page_index: 20 -->

# JiBX Integration With Axis2

This document describes using JiBX data binding with Axis2. JiBX
differs from the other data binding techniques supported by Axis2
in that it allows you to use your own Java data objects (as opposed
to Java data objects generated from a schema definition). JiBX also
provides a nicer form of unwrapped Web services interface than is
supported by the other data binding techniques. On the downside, JiBX requires more setup than the other data binding techniques -
in particular, you need to come up with a set of data classes and a
binding definition in order to work with JiBX in Axis2.

## Content

- [Introduction](#docs-jibx-jibx-codegen-integration--intro)
- [Wrapped vs. unwrapped](#docs-jibx-jibx-codegen-integration--wrapped)
- [Starting from Java](#docs-jibx-jibx-codegen-integration--java)
- [Starting from WSDL](#docs-jibx-jibx-codegen-integration--wsdl)
- [Axis2 JiBX Code Generation](#docs-jibx-jibx-codegen-integration--codegen)
- [Coming Attractions](#docs-jibx-jibx-codegen-integration--coming)

## Introduction

[JiBX data binding](http://www.jibx.org) supports
fast and flexible conversions between plain old Java objects
(POJOs) and XML. JiBX uses a mapped binding approach that's based
on binding definition documents you provide. This approach let's
you customize the way your Java objects are converted to and from
XML. You can even define multiple bindings to use the same Java
objects with different XML representations. These features make
JiBX especially useful if you're developing a Web service based on
existing Java code, or when you need to support multiple XML
representations for a Web service (as when you're using versioned
schema definitions).

Axis2 supports using JiBX with your Web services, including
generating the necessary linkage code for both client and server
sides. However, the Axis2 support for JiBX does not currently
include code generation from the schema for a Web service - you
need to provide your own data classes and JiBX binding definition, and you also need to make sure that the binding definition matches
the XML structures defined for your Web service. The JiBX project
provides some basic tools to help with code generation from schema, binding generation from Java classes, and schema generation from
the combination of Java classes and a binding definition. In the
future, improved versions of these tools will be integrated
directly into the Axis2 framework support, but for now you're on
your own with this part of the setup.

You can use JiBX data binding both to expose existing Java code
as a service, and to build a client for an existing service. This
document runs through the sequence of steps involved for each of
these cases, just to help users understand the basic approach to
working with JiBX in Axis2. You can find full instructions on the
standard JiBX parts of this sequence on the [JiBX Web site](http://www.jibx.org).

## Wrapped vs. unwrapped

Axis2 support for JiBX currently only works with the
document-literal (doc/lit) form of Web services definitions.
Doc/lit Web services generally use particular schema elements as
input and output from each operation, and the Axis2 support for
JiBX assumes this structure (which is also the structure required
for compatibility with the [WS-I Basic
Profile](http://www.ws-i.org/Profiles/BasicProfile-1.1.html)).

A popular subset of doc/lit Web services use a form called
"wrapped". Wrapped doc/lit Web services define service operations
that correspond to method calls, using input and output element
names based on the method name and embedding the actual parameter
values for the method call within the input element.

When used with Axis2, JiBX supports both general doc/lit and
wrapped service definitions. Wrapped service definitions can be
"unwrapped" during code generation to provide a greatly simplified
interface. JiBX unwrapping of service definitions is not compatible
with the unwrapping support for other data binding frameworks used
with Axis2, but most users will find the JiBX approach easy and
convenient. See the [JiBX
Unwrapped Example](#docs-jibx-jibx-unwrapped-example) and the [JiBX Document/Literal Example](#docs-jibx-jibx-doclit-example)
pages for a detailed comparison of the two forms of service
interface.

## Starting from Java

Here's the sequence of steps for using JiBX with Axis2 to expose
existing Java code as a Web service:

1. Create a JiBX binding definition for the data being transferred
   by the Web service (you may be able to use the JiBX binding
   generator to help with this step).
2. Create a schema that matches the XML defined by your binding
   (you may be able to use the JiBX schema generator to help with
   this). If you're using a wrapped form of interface to your service
   you'll also need to create schema definitions for the wrapper input
   and output elements used by each operation.
3. Create a WSDL document for your service, with the schema
   embedded or imported.
4. Generate Axis2 server-side linkage code using WSDL2Java with
   the WSDL and your binding definition.
5. Run the JiBX binding compiler on your Java classes to add the
   actual binding code.
6. Include the *axis2-jibx.jar* in your runtime classpath,
   along with the *jibx-runtime.jar*.

If you use a wrapped interface for your Web service you can
expose method calls in your existing code directly as operations in
the service. In this case you normally just use your existing data
objects with JiBX data binding, and add schema definitions for the
wrapper elements. See the [JiBX Unwrapped Example](#docs-jibx-jibx-unwrapped-example) page for
more details on how this works.

If you use a non-wrapped interface for your Web service you need
to define classes to hold the data input and output from each
operation. In this case these holder classes need to be included in
the JiBX binding definition. See the [JiBX Document/Literal Example](#docs-jibx-jibx-doclit-example) page
for more details on this case.

## Starting from WSDL

Here's the sequence of steps for using JiBX with Axis2 to
implement a client for an existing Web service (or the actual
service, when you've been supplied with the WSDL your service is to
implement):

1. Create Java classes for the data being transferred by the Web
   service, and a JiBX binding definition that maps these classes to
   the schema defined by the Web service (you may be able to use the
   JiBX xsd2jibx tool to help with this).
2. Generate Axis2 client linkage code using WSDL2Java with the
   WSDL and your binding definition.
3. Run the JiBX binding compiler on your Java classes to add the
   actual binding code.
4. Include the *axis2-jibx.jar* in your runtime classpath,
   along with the *jibx-runtime.jar*

As with the starting from Java case, there are some differences
in the handling depending on whether your service definition fits
the wrapped form. See the [JiBX Unwrapped Example](#docs-jibx-jibx-unwrapped-example) and
[JiBX Document/Literal
Example](#docs-jibx-jibx-doclit-example) pages for more details.

## WSDL2Java usage

To run the WSDL2Java tool for JiBX data binding you need:

1. To specify *-d jibx* to select JiBX binding.
2. You also generally need an additional parameter,
   *-Ebindingfile {file}* (where *{file}* is the file path
   to your JiBX binding definition).
3. Finally, you need to have the *axis2-jibx-XXXX.jar*, the
   *jibx-bind-XXXX.jar*, and the *jibx-run-XXXX.jar* files
   from your Axis2 distribution included in the WSDL2Java
   classpath.

If you want to use the unwrapped form of interface you also need
to specify the *-uw* option to WSDL2Java. In this case your
JiBX binding definition must include abstact mappings for all the
complex objects which correspond to method parameters, and each
abstract mapping must specify a *type-name* attribute that
matches the schema *complexType* used in the WSDL. You can
also use formats in the binding definition to define the handling
of schema *simpleType*s. Schema types corresponding to Java
primitives and simple objects with built-in JiBX conversions are
handled automatically, and if all the parameter and return values
in your wrapped WSDL are of these types you don't even need a JiBX
binding definition. This is the one case where the *-Ebindingfile
{file}* parameter is not needed.

If you're not unwrapping the interface, you must use a JiBX
binding definition and it must include a concrete mapping for each
element used as input or output by any operation.

## Coming Attractions

Work is in-progress on better tools to support generating Java
classes and corresponding JiBX binding definitions from an input
schema, and also for generating binding+schema generation from
existing code. These features will be integrated into the Axis2
JiBX support when they are available. Check the [JiBX project site](http://www.jibx.org) for updates on JiBX.

## References

[JiBX:
Bindings Tutorial](http://jibx.sourceforge.net/tutorial/binding-tutorial.html)

---

<a id="docs-jibx-jibx-doclit-example"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/jibx/jibx-doclit-example.html -->

<!-- page_index: 21 -->

# JiBX general document/literal

Code generation for JiBX data binding converts operations
defined by a Web service to method calls. With general
document/literal (doc/lit) Web services the generated methods each
take a single parameter object and return a single result object.
Here's a sample doc/lit WSDL (partial) by way of an example:

```

<wsdl:definitions targetNamespace="http://ws.sosnoski.com/library/wsdl"
    xmlns:tns="http://ws.sosnoski.com/library/types"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/">
    
  <wsdl:types>
  
    <schema elementFormDefault="qualified"
        targetNamespace="http://ws.sosnoski.com/library/types"
        xmlns="http://www.w3.org/2001/XMLSchema">
        
      <element name="getBook">
        <complexType>
          <sequence>
            <element name="isbn" type="string"/>
          </sequence>
        </complexType>
      </element>
      
      <element name="getBookResponse">
        <complexType>
          <sequence>
            <element name="book" minOccurs="0" type="tns:BookInformation"/>
          </sequence>
        </complexType>
      </element>
      
      <element name="addBook">
        <complexType>
          <sequence>
            <element name="type" type="string"/>
            <element name="isbn" type="string"/>
            <element name="author" minOccurs="0" maxOccurs="unbounded" type="string"/>
            <element name="title" type="string"/>
          </sequence>
        </complexType>
      </element>
      
      <element name="addBookResponse">
        <complexType>
          <sequence>
            <element name="success" type="boolean"/>
          </sequence>
        </complexType>
      </element>
      
      <complexType name="BookInformation">
        <sequence>
          <element name="author" minOccurs="0" maxOccurs="unbounded" type="string"/>
          <element name="title" type="string"/>
        </sequence>
        <attribute name="type" use="required" type="string"/>
        <attribute name="isbn" use="required" type="string"/>
      </complexType>
      
    </schema>

  </wsdl:types>

  <wsdl:message name="getBookRequest">
    <wsdl:part element="wns:getBook" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getBookResponse">
    <wsdl:part element="wns:getBookResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="addBookRequest">
    <wsdl:part element="wns:addBook" name="parameters"/>
  </wsdl:message>
  
  <wsdl:message name="addBookResponse">
    <wsdl:part element="wns:addBookResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:portType name="Library">

    <wsdl:operation name="getBook">
      <wsdl:input message="wns:getBookRequest" name="getBookRequest"/>
      <wsdl:output message="wns:getBookResponse" name="getBookResponse"/>
    </wsdl:operation>

    <wsdl:operation name="addBook">
      <wsdl:input message="wns:addBookRequest" name="addBookRequest"/>
      <wsdl:output message="wns:addBookResponse" name="addBookResponse"/>
    </wsdl:operation>

  </wsdl:portType>
  ...
</wsdl:definitions>
```

This WSDL defines a service with just two operations:
**getBook** and **addBook**. The **getBook** operation
takes a *getBook* element as input, and returns a
*getBookResponse* element as output, while **addBook**
takes an *addBook* element as input and returns an
*addBookResponse* as output. Here's the body of the client
interface generated by the standard JiBX code generation:

```

    public interface LibraryJibxUnwrapped {
          
             
        /**
         * Auto generated method signatures
         * @param addBook
         */
         public com.sosnoski.ws.library.jibx.wrappers.AddBookResponse addBook(
         com.sosnoski.ws.library.jibx.wrappers.AddBookRequest addBook) throws java.rmi.RemoteException
          
                       
             ;
             
             
        /**
         * Auto generated method signatures
         * @param getBook
         */
         public com.sosnoski.ws.library.jibx.wrappers.GetBookResponse getBook(
         com.sosnoski.ws.library.jibx.wrappers.GetBookRequest getBook) throws java.rmi.RemoteException
          
                       
             ;
             

        
       //
       }
```

You can see that the JiBX code generation converted the
operations into simple method call interfaces using objects
corresponding to the input and output elements of the operation
(see [JiBX Unwrapped
Example](#docs-jibx-jibx-unwrapped-example) for the interface generated when unwrapping is instead
used). The server-side interface is the same.

You need to supply an appropriate JiBX binding definition for
use in code generation (using the *-Ebindingfile {file}*
parameter for WSDL2Java - see [JiBX Codegen Integration
- WSDL2Java usage](#docs-jibx-jibx-codegen-integration--codegen) for more details). This must define concrete
*mappings* for each element used as the input or output of an
operation. The JiBX code generation extension matches the element
names to the binding in order to determine the corresponding class
to use in generated code.

For example, here's a binding definition that matches the above
WSDL:

```

<binding add-constructors="true">

  <namespace uri="http://ws.sosnoski.com/library/types" default="elements"/>
  
  <mapping name="getBook"
      class="com.sosnoski.ws.library.jibx.wrappers.GetBookRequest">
    <value name="isbn" field="m_isbn"/>
  </mapping>
  
  <mapping name="getBookResponse"
      class="com.sosnoski.ws.library.jibx.wrappers.GetBookResponse">
    <structure name="book" field="m_book"/>
  </mapping>
  
  <mapping name="addBook"
      class="com.sosnoski.ws.library.jibx.wrappers.AddBookRequest">
    <structure field="m_book">
      <value name="type" field="m_type"/>
      <value name="isbn" field="m_isbn"/>
      <collection field="m_authors">
        <value name="author" type="java.lang.String"/>
      </collection>
      <value name="title" field="m_title"/>
    </structure>
  </mapping>
  
  <mapping name="addBookResponse"
      class="com.sosnoski.ws.library.jibx.wrappers.AddBookResponse"/>
  
  <mapping abstract="true" class="com.sosnoski.ws.library.jibx.beans.Book">
    <value name="type" style="attribute" field="m_type"/>
    <value name="isbn" style="attribute" field="m_isbn"/>
    <collection field="m_authors">
      <value name="author" type="java.lang.String"/>
    </collection>
    <value name="title" field="m_title"/>
  </mapping>

</binding>
```

And here are the actual data object classes:

```

package com.sosnoski.ws.library.jibx.wrappers;

import com.sosnoski.ws.library.jibx.beans.Book;

public class AddBookRequest
{
    private Book m_book;
    
    public AddBookRequest(Book book) {
        m_book = book;
    }
    
    public Book getBook() {
        return m_book;
    }
}

public class AddBookResponse
{
}

public class GetBookRequest
{
    private String m_isbn;
    
    public GetBookRequest(String isbn) {
        m_isbn = isbn;
    }

    public String getIsbn() {
        return m_isbn;
    }
}

public class GetBookResponse
{
    private Book m_book;
    
    public GetBookResponse(Book book) {
        m_book = book;
    }
    
    public Book getBook() {
        return m_book;
    }
}

package com.sosnoski.ws.library.jibx.beans;

public class Book
{
    private String m_type;
    private String m_isbn;
    private String m_title;
    private String[] m_authors;
    
    public Book() {}

    public String getType() {
        return m_type;
    }
    
    public String getIsbn() {
        return m_isbn;
    }
    
    public String getTitle() {
        return m_title;
    }
    
    public String[] getAuthors() {
        return m_authors;
    }
}
```

---

<a id="docs-jibx-jibx-unwrapped-example"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/jibx/jibx-unwrapped-example.html -->

<!-- page_index: 22 -->

# JiBX Unwrapped document/literal

Code generation for JiBX data binding converts operations
defined by a Web service to method calls. In the most general case
of document/literal (doc/lit) Web services the generated methods
each take a single parameter object and return a single result
object. This type of interface can be painful for developers
because it adds both a layer of indirection and potentially a large
number of extra classes (one input and one output class for each
generated method).

Fortunately, there's an alternative way of generating methods
that gives a much more usable API for many Web services. This
alternative is called *unwrapping*, and the service
definitions that it applies to are called *wrapped*
definitions. The key difference that qualifies a service definition
as wrapped is the structure of the input and output elements used
for operations.

Here's a sample wrapped WSDL (partial) by way of an example:

```

<wsdl:definitions targetNamespace="http://ws.sosnoski.com/library/wsdl"
    xmlns:tns="http://ws.sosnoski.com/library/types"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/">
    
  <wsdl:types>
  
    <schema elementFormDefault="qualified"
        targetNamespace="http://ws.sosnoski.com/library/types"
        xmlns="http://www.w3.org/2001/XMLSchema">
        
      <element name="getBook">
        <complexType>
          <sequence>
            <element name="isbn" type="string"/>
          </sequence>
        </complexType>
      </element>
      
      <element name="getBookResponse">
        <complexType>
          <sequence>
            <element name="book" minOccurs="0" type="tns:BookInformation"/>
          </sequence>
        </complexType>
      </element>
      
      <element name="addBook">
        <complexType>
          <sequence>
            <element name="type" type="string"/>
            <element name="isbn" type="string"/>
            <element name="author" minOccurs="0" maxOccurs="unbounded" type="string"/>
            <element name="title" type="string"/>
          </sequence>
        </complexType>
      </element>
      
      <element name="addBookResponse">
        <complexType>
          <sequence>
            <element name="success" type="boolean"/>
          </sequence>
        </complexType>
      </element>
      
      <complexType name="BookInformation">
        <sequence>
          <element name="author" minOccurs="0" maxOccurs="unbounded" type="string"/>
          <element name="title" type="string"/>
        </sequence>
        <attribute name="type" use="required" type="string"/>
        <attribute name="isbn" use="required" type="string"/>
      </complexType>
      
    </schema>

  </wsdl:types>

  <wsdl:message name="getBookRequest">
    <wsdl:part element="wns:getBook" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getBookResponse">
    <wsdl:part element="wns:getBookResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="addBookRequest">
    <wsdl:part element="wns:addBook" name="parameters"/>
  </wsdl:message>
  
  <wsdl:message name="addBookResponse">
    <wsdl:part element="wns:addBookResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:portType name="Library">

    <wsdl:operation name="getBook">
      <wsdl:input message="wns:getBookRequest" name="getBookRequest"/>
      <wsdl:output message="wns:getBookResponse" name="getBookResponse"/>
    </wsdl:operation>

    <wsdl:operation name="addBook">
      <wsdl:input message="wns:addBookRequest" name="addBookRequest"/>
      <wsdl:output message="wns:addBookResponse" name="addBookResponse"/>
    </wsdl:operation>

  </wsdl:portType>
  ...
</wsdl:definitions>
```

This WSDL defines a service with just two operations:
**getBook** and **addBook**. The **getBook** operation
takes a *getBook* element as input, and returns a
*getBookResponse* element as output, while **addBook**
takes an *addBook* element as input and returns an
*addBookResponse* as output. Each of these input and output
elements in turn consists of a sequence of child elements, with
some of the child elements defined directly using standard schema
types and others referencing user-defined schema types.

As I said up front, this WSDL qualifies for unwrapped handling
using JiBX. Here's the body of the client interface generated when
using unwrapping (the *-uw* option for WSDL2Java):

```

    public interface LibraryJibxUnwrapped {
          
             
        /**
         * Auto generated method signatures
         * @param type* @param isbn* @param author* @param title
         */
         public boolean addBook(
         java.lang.String type,java.lang.String isbn,java.lang.String[] author,java.lang.String title) throws java.rmi.RemoteException
          
                       
             ;
             
             
        /**
         * Auto generated method signatures
         * @param isbn
         */
         public com.sosnoski.ws.library.jibx.beans.Book getBook(
         java.lang.String isbn) throws java.rmi.RemoteException
          
                       
             ;
             

        
       //
       }
```

You can see that the JiBX code generation converted the
operations into simple method call interfaces without introducing
any extraneous objects (see [JiBX Document/Literal Example](#docs-jibx-jibx-doclit-example) for
the interface generated when unwrapping is not used). The
server-side interface is the same.

The key points that allow unwrapped handling with JiBX are:

1. Each operation either accepts no input, or the input consists
   of a single element.
2. Each input element is defined as a schema *complexType*
   consisting of a *sequence* of any number of child
   elements.
3. Each operation either generates no output, or the output
   consists of a single element.
4. Each output element is defined as a schema *complexType*
   consisting of a *sequence* that's either empty or contains a
   single child element.
5. The child elements of both inputs and outputs are defined using
   *type* references, rather than an embedded type
   definitions.

You also need to supply an appropriate JiBX binding definition
(using the *-Ebindingfile {file}* parameter for WSDL2Java -
see [JiBX Codegen
Integration - WSDL2Java usage](#docs-jibx-jibx-codegen-integration--codegen) for more details). This must
define abstract *mapping*s for the *complexType*s
referenced by child elements of the inputs and outputs, with a
*type-name* attribute matching the schema *complexType*
name. If the child elements reference schema *simpleType*
definitions the binding must also define a *format*s for each
*simpleType*, with a *label* attribute matching the
schema *simpleType* name. The binding definition must also
specify the *force-classes='true'* attribute on the
*binding* element.

For example, here's a binding definition that matches the above
WSDL:

```

<binding force-classes="true" xmlns:tns="http://ws.sosnoski.com/library/types">

  <namespace uri="http://ws.sosnoski.com/library/types" default="elements"/>
  
  <mapping abstract="true" class="com.sosnoski.ws.library.jibx.beans.Book"
      type-name="tns:BookInformation">
    <value name="type" style="attribute" field="m_type"/>
    <value name="isbn" style="attribute" field="m_isbn"/>
    <collection field="m_authors">
      <value name="author"/>
    </collection>
    <value name="title" field="m_title"/>
  </mapping>
  
</binding>
```

And here's the actual
`com.sosnoski.ws.library.jibx.beans.Book` class:

```

package com.sosnoski.ws.library.jibx.beans;

public class Book
{
    private String m_type;
    private String m_isbn;
    private String m_title;
    private String[] m_authors;
    
    public Book() {}

    public String getType() {
        return m_type;
    }
    
    public String getIsbn() {
        return m_isbn;
    }
    
    public String getTitle() {
        return m_title;
    }
    
    public String[] getAuthors() {
        return m_authors;
    }
}
```

The JiBX code generation for Axis2 currently requires that
classes coresponding to unwrapped child elements (such as
`com.sosnoski.ws.library.jibx.beans.Book`, in this case)
provide public default (no-argument) constructors.

JiBX handling allows the child elements of both inputs and
outputs to be optional (with *nillable='true'*,
*minOccurs='0'*, or both), providing the binding converts
these child elements to object types rather than primitive types.
It also allows repeated child elements (with
*minOccurs='unbounded'*, or any value of *minOccurs*
greater than one), representing the repeated elements as arrays of
the corresponding object or primitive types.

---

<a id="docs-xmlbased-server"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/xmlbased-server.html -->

<!-- page_index: 23 -->

# Writing Web Services Using Apache Axis2's Primary APIs

Apache Axis2 dispatches a component called
**MessageReceiver** when Receiving a Message to the
server. Apache Axis2 provides different implementations of this
class and it can be configured by adding a messageReceiver tag to
services.xml. Apache Axis2 provides an implementation for a class
of Message receivers called RawXml Message receivers. They work at
the XML level and can only handle OMElements as parameters. This
section explains how to write a service using them.

In our example, the Web service will have two operations.

```

public void ping(OMElement element){} //IN-ONLY operation, just accepts the OMElement and does some processing.
public OMElement echo(OMElement element){}//IN-OUT operation, accepts an OMElement and  
                                          // sends back the same again 
```

#### How to Write a Web Service?

Writing a new Web service with Apache Axis2 involves four steps:

1. Write the Implementation Class.
2. Write a services.xml file to explain the Web service.
3. Create a \*.aar archive (Axis Archive) for the Web service.
4. Deploy the Web service.

#### Step1: Write the Implementation Class

An implementation class has the business logic for the Web
service and implements the operations provided by the Web service.
Unless you have data binding, the signature of the methods can have
only one parameter of the type OMElement. *OM stands for Object
Model (also known as AXIOM - AXis Object Model) and refers to the
XML infoset model that is initially developed for Apache Axis2. DOM
and JDOM are two such XML models conceptually similar to OM as an
XML model by its external behavior, but considering the deep down
implementation OM is very much different to others. OMElement is
the basic representation of the XML infoset element in OM.For more
details on OMElement see the [Axiom
User Guide](http://ws.apache.org/axiom/userguide/userguide.html).*

```

public class MyService{
    public void ping(OMElement element){
        // Business Logic     
        ......
    }
    public OMElement echo(OMElement element){
     ......
    }
}
```

#### Step2: Write the services.xml file

"services.xml" has the configuration for a Web service. Each Web
service, deployed in Apache Axis2 , must have its configuration in
"services.xml". The configuration for MyService is as follows:

```

<service >
    <description>
        This is a sample Web service with two operations, echo and ping.
    </description>
    <parameter name="ServiceClass">userguide.example1.MyService</parameter>
    <operation name="echo">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
        <actionMapping>urn:echo</actionMapping>
    </operation>
     <operation name="ping">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOnlyMessageReceiver"/>
        <actionMapping>urn:ping</actionMapping>
    </operation>
 </service>
```

The above XML tags can be explained as follows:

1. The description of the service class is provided in the
description tag.

```

<service >
    <description>
        This is a sample Web service with two operations, echo and ping.
    </description>
```

2. The name of the service class is provided as a parameter.

```

<parameter name="serviceClass">userguide.example1.MyService</parameter>
```

3. The "operation" XML tag describes the operations that are
available in this service with respective message receivers.

```

   <operation name="echo">
            <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
            <actionMapping>urn:echo</actionMapping>
   </operation>
   <operation name="ping">
       <messageReceiver class="org.apache.axis2.receivers.RawXMLINOnlyMessageReceiver"/>
       <actionMapping>urn:ping</actionMapping>
   </operation>
```

4. Every operation must map to a corresponding MessageReceiver
class. After a message is processed by the handlers, the Axis2
engine hands it over to a MessageReceiver.

5. For the "echo" operation, we have used a
**RawXMLINOutMessageReceiver** since it is an IN-OUT
operation. For the IN-ONLY operation "ping", we have used
**RawXMLINOnlyMessageReceiver** as the message
receiver.

6. The actionMapping is required only if you want to enable
WS-Addressing. This will be used later in this user guide.

7. You can write a services.xml file to include a group of
services instead of a single service. This makes the management and
deployment of a set of related services very easy. At runtime, you
can share information between these services within a single
interaction using the ServiceGroupContext. If you hope to use this
functionality, the services.xml file should have the following
format.

```

<ServiceGroup>
  <service name="Service1">
    <!-- details for Service1 -->
  </service>
  <service name="Service2">
    <!-- details for Service2 -->
  </service>
  <module ref="ModuleName" />
  <parameter name="serviceGroupParam1">value 1</parameter>
</serviceGroup>
```

Note : The name of the service is a compulsory attribute.

#### Step3: Create the Web Service Archive

Apache Axis2 uses the ".aar" (Axis Archive) file as the
deployment package for Web services. Therefore, for MyService we
will use "MyService.aar" with the "services.xml" packaged in the
META-INF in the directory structure shown below. Please note that
the name of the archive file will be the same as that of the
service only if the services.xml contains only one service
element.

![](assets/images/serviceitems_0367e2140e53c3ae.jpg)

To create the archive file, you can create a .jar file
containing all the necessary files and then rename it to a .aar
file. This archive file can be found in the
"Axis2\_HOME/samples/userguide" directory. This file has to be
deployed now.

#### Step4: Deploy the Web Service

The service can be deployed by dropping the ".aar" file into the
"services" directory in "/webapps/axis2/WEB-INF" of your servlet
container. Start the servlet container (if you have not already
started), click the link "Services" on the [Home Page of Axis2
Web Application](http://localhost:8080/axis2/) (http://localhost:8080/axis2) and see whether
MyService is deployed properly. If you can see the following
output, then you have successfully deployed MyService on Apache
Axis2. Congratulations !!

![](assets/images/myservicedeployed_59bd53bdda2f0d79.jpg)

Note: Apache Axis2 provides an easy way to deploy Web services
using the "Upload Service" tool on the Axis2 Web Application's
Administration module. Please refer to the [Web Administration Guide](#docs-webadminguide)
for more information.

---

<a id="docs-dii"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/dii.html -->

<!-- page_index: 24 -->

# Writing Web Service Clients Using Axis2's Primary APIs

This section presents a complex yet powerful **XML based client
API**, which is intended for advanced users. However, if you are a new
user, we recommend using code generation given in the [Advanced User's Guide](#docs-adv-userguide).

Web services can be used to provide a wide-range of functionality to the
user from simple, quick operations such as "getStockQuote" to time consuming
business services. When we utilize (invoke using client applications) these
Web services, we cannot always use simple generic invocation paradigms that suite
all the timing complexities involved in the service operations. For example, if we use a single transport channel (such as HTTP) to invoke a Web service
with an IN-OUT operation that takes a long time to complete, then most often
we may end up with "connection time outs". Further, if there are
simultaneous service invocations that we need to perform from a single client
application, then the use of a "blocking" client API will degrade the
performance of the client application. Similarly, there are various other
consequences such as One-Way transports that come into play when we need
them. Let's try to analyze some common service invocation paradigms.

Many Web service engines provide users with Blocking and Non-Blocking
client APIs.

- **Blocking API** - Once the service
  invocation is called, the client application hangs, regaining control
  only when the operation completes, after which the client receives a
  response or a fault. This is the simplest way of invoking Web services,
  and it also suites many business situations.
- **Non-Blocking API** - This is a callback or polling based API.
  Here, once a service invocation is called, the client application
  immediately regains control and the response is retrieved using the
  callback object provided. This approach allows the
  client application to invoke several Web services simultaneously without
  needing to wait for the response of previous operations.

Both these mechanisms work at the API level. Let's name the asynchronous
behavior that we can get using the Non-Blocking API as **API Level
Asynchrony.**

Both mechanisms use single transport connections to send the request and
to receive the response. They severely lag the capability of using two
transport connections for the request and the response (either One-Way or
Two-Way). So both these mechanisms fail to address the problem of long
running transactions, as the transport connection may still time-out before the
operation completes. A possible solution would be to use two separate
transport connections for request and response. The asynchronous behavior
that we gain using this solution can be called **Transport Level
Asynchrony**.

By **combining API Level Asynchrony and Transport Level
Asynchrony**, we can obtain four different invocation patterns for Web
services as shown in the following table.

|  |  |  |
| --- | --- | --- |
| **API (Blocking/Non-Blocking)** | **Dual Transports (Yes/No)** | **Description** |
| Blocking | No | The simplest and most familiar invocation pattern |
| Non-Blocking | No | Using callbacks or polling |
| Blocking | Yes | This is useful when the service operation is Request-Response in nature but the transport used is One-Way (e.g. SMTP) |
| Non-Blocking | Yes | This is can be used to gain the maximum asynchronous behavior. Non blocking at the API level and also at the transport level. |

Axis2 provides the user with all these possibilities to invoke Web
services.

The following section presents clients that use some of the different
possibilities presented above to invoke a Web Service using
`ServiceClient`s. All the samples mentioned in this guide are
located at the **"samples\userguide\src"**
directory of the binary distribution.

This section presents four types of clients.

1. Request-Response, Blocking Client
2. One Way Client, Non-Blocking
3. Request-Response, Non-Blocking that uses one transport connection
4. Request-Response, Non-Blocking that uses two transport connections

#### Request-Response, Blocking Client

The client code below will invoke the "echo" operation of
"MyService" using a pure blocking single-channel invocation.

```
   try {
                  
      OMElement payload = ClientUtil.getEchoOMElement();
      Options options = new Options();
      options.setTo(targetEPR); // this sets the location of MyService service
            
      ServiceClient serviceClient = new ServiceClient();
      serviceClient.setOptions(options);

      OMElement result = serviceClient.sendReceive(payload);
      
      System.out.println(result);
   } catch (AxisFault axisFault) {
      axisFault.printStackTrace();
   } 
}
```

The lines highlighted in green show the set of operations that you need
to perform in order to invoke the Web service in this manner.

To test this client, use the provided Ant build file that can be found in
the "**Axis2\_HOME/samples/userguide**" directory. Run the
"run.client.blocking" target. If you can see the response OMElement printed
in your command line, then you have successfully tested the client.

#### One Way Client, Non-Blocking

In the Web service "MyService", we had an IN-ONLY operation with the name
"ping" (see [Creating a
New Web Service](#docs-adv-userguide--web_services_using_axis2)). Let's write a client to invoke this operation. The
client code is as follows:

```
 
   try {
      OMElement payload = ClientUtil.getPingOMElement();
      Options options = new Options();
      options.setTo(targetEPR);
      ServiceClient serviceClient = new ServiceClient();
      serviceClient.setOptions(options);
      serviceClient.fireAndForget(payload);
      /**
       * We need to wait some time for the message to be sent.  Otherwise,
       * if we immediately exit this function using the main thread, 
       * the request won't be sent.
       */
      Thread.sleep(500);
   } catch (AxisFault axisFault) {
      axisFault.printStackTrace();
   }
```

Since we are calling an IN-ONLY web service, we can directly use the
`fireAndForget()` in the ServiceClient to invoke this operation.
This will not block the invocation and will return the control immediately
back to the client. You can test this client by running the target
"run.client.ping" of the Ant build file at
"**Axis2Home/samples/userguide**".

#### Request-Response, Non-Blocking that uses one transport connection

In the "EchoBlockingClient" once the
`serviceClient.sendReceive(payload);` is called, the client is
blocked till the operation is complete. This behavior is not desirable when
there are many Web service invocations to be done in a single client
application or within a GUI. A solution would be to use a Non-Blocking API to
invoke Web services. Axis2 provides a callback based non-blocking API for
users.

A sample client for this can be found under
"**Axis2\_HOME/samples/userguide/src/userguide/clients**" with
the name "EchoNonBlockingClient". If we consider the changes that the developer may
have to do with respect to the "EchoBlockingClient" that we have already
seen, it will be as follows:

```
serviceClient.sendReceiveNonblocking(payload, callback);
```

The invocation accepts a Callback object as a parameter. Axis2 client API
provides an abstract Callback with the following methods:

```
public abstract void onComplete(AsyncResult result);
public abstract void onError(Exception e);
public boolean isComplete() {}
```

The developer is expected to override the onComplete() and onError() methods
of their Callback subclass. The Axis2 engine calls the onComplete()
method once the Web service response is received by the Axis2 Client API
(ServiceClient). This eliminates the blocking nature of the web service
request-response invocation.

To run the sample client ("EchoNonBlockingClient") you can simply use the
`run.client.nonblocking` target of the Ant file found in the
"**Axis2\_HOME/samples/userguide**" directory.

#### Request-Response, Non-Blocking that uses two transport connections

The solution provided above by the Non-Blocking API has one limitation when it
comes to Web service invocations that take a long time to complete. The
limitation is due to the use of single transport connections to invoke the
Web service and retrieve the response. In other words, the client API provides a
non-blocking invocation mechanism for developers, but the request and the response
still come in a single transport (Two-Way transport) connection like HTTP. Long
running Web service invocations or Web service invocations using One-Way
transports such as SMTP cannot be utilized by simply using a non-blocking
API invocation.

The simplest solution is to use separate transport connections (either
One-Way or Two-Way) for the request and response. The next problem that needs
to be solved, however, is subsequently correlating each request with its response.
[WS-Addressing](http://www.w3.org/2002/ws/addr/)
provides a neat solution to this using <wsa:MessageID> and
<wsa:RelatesTo> headers. Axis2 provides support for an addressing based
correlation mechanism and a complying Client API to invoke Web services with
two transport connections. (The core of Axis2 does not depend on
WS-Addressing, but contains a set of parameters, like in addressing, that can
be populated by any method. WS-Addressing is one of the uses that may
populate them. Even the transports can populate them. Hence, Axis2 has the
flexibility to use different addressing standards.)

Users can select between Blocking and Non-Blocking APIs for the Web
service clients with two transport connections. By simply using a boolean
flag, the same API can be used to invoke Web services (IN-OUT operations)
using two separate transport connections. Let's see how it's done using an
example. The following code fragment shows how to invoke the same "echo"
operation using Non-Blocking API with two transport connections**. The
ultimate asynchrony!!**

```

   try {
      OMElement payload = ClientUtil.getEchoOMElement();

      Options options = new Options();
      options.setTo(targetEPR);
      options.setTransportInProtocol(Constants.TRANSPORT_HTTP);
      options.setUseSeparateListener(true);
      options.setAction("urn:echo");  // this is the action mapping we put within the service.xml

      //Callback to handle the response
      Callback callback = new Callback() {
         public void onComplete(AsyncResult result) {
            System.out.println(result.getResponseEnvelope());
         }

         public void onError(Exception e) {
            e.printStackTrace();
         }
      };

      //Non-Blocking Invocation            
      sender = new ServiceClient();            
      sender.engageModule(new QName(Constants.MODULE_ADDRESSING));
      sender.setOptions(options);            
      sender.sendReceiveNonBlocking(payload, callback);            
   
      //Wait till the callback receives the response.            
      while (!callback.isComplete()) {                
         Thread.sleep(1000);            
      }               
   } catch (AxisFault axisFault) {            
     axisFault.printStackTrace();
   } catch (Exception ex) {
     ex.printStackTrace();
   } finally {
      try {
         //Close the Client Side Listener.
         sender.cleanup();
      } catch (AxisFault axisFault) {
        //have to ignore this
      }
   }
```

The boolean flag (value True) in the
**`options.setUseSeparateListener(...)`** method informs the
Axis2 engine to use separate transport connections for the request and
response. Finally **`sender.cleanup()`** informs the Axis2
engine to stop the client side listener, which started to retrieve the
response.

To run the sample client ("EchoNonBlockingDualClient") you can simply use
the "run.client.nonblockingdual" target of the Ant file found in the
"**Axis2\_HOME/samples/userguide/**" directory.

---

<a id="docs-mtom-guide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/mtom-guide.html -->

<!-- page_index: 25 -->

# Handling Binary Data with Axis2 (MTOM/SwA)

This document describes how to use the Axis2 functionality to send/receive
binary data with SOAP.

## Content

- [Introduction](#docs-mtom-guide--a1)
  - [Where Does MTOM Come In?](#docs-mtom-guide--a11)
- [MTOM with Axis2](#docs-mtom-guide--a2)
  - [Programming Model](#docs-mtom-guide--a21)
  - [Enabling MTOM Optimization at Client Side](#docs-mtom-guide--a22)
  - [Enabling MTOM Optimization at Server Side](#docs-mtom-guide--a23)
  - [Accessing Received Binary Data (Sample Code)](#docs-mtom-guide--a24)
    - [Service](#docs-mtom-guide--a241)
    - [Client](#docs-mtom-guide--a242)
  - [MTOM Databinding](#docs-mtom-guide--a25)
    - [Using ADB](#docs-mtom-guide--a251)
- [SOAP with Attachments with Axis2](#docs-mtom-guide--a3)
  - [Sending SwA Type Attachments](#docs-mtom-guide--a31)
  - [Receiving SwA Type Attachments](#docs-mtom-guide--a32)
  - [MTOM Backward Compatibility with SwA](#docs-mtom-guide--a33)
- [Advanced Topics](#docs-mtom-guide--a4)
  - [File Caching for Attachments](#docs-mtom-guide--a41)

## Introduction

Despite the flexibility, interoperability, and global acceptance of XML, there are times when serializing data into XML does not make sense. Web
services users may want to transmit binary attachments of various sorts like
images, drawings, XML docs, etc., together with a SOAP message. Such data is
often in a particular binary format.

Traditionally, two techniques have been used in dealing with opaque data
in XML;

1. **"By value"**
> Sending binary data by value is achieved by embedding opaque data (of
> course after some form of encoding) as an element or attribute content of
> the XML component of data. The main advantage of this technique is that
> it gives applications the ability to process and describe data, based
> only on the XML component of the data.
>
> XML supports opaque data as content through the use of either base64
> or hexadecimal text encoding. Both techniques bloat the size of the data.
> For UTF-8 underlying text encoding, base64 encoding increases the size of
> the binary data by a factor of 1.33x of the original size, while
> hexadecimal encoding expands data by a factor of 2x. The above factors
> will be doubled if UTF-16 text encoding is used. Also of concern is the
> overhead in processing costs (both real and perceived) for these formats,
> especially when decoding back into raw binary.

2. **"By reference"**
   > Sending binary data by reference is achieved by attaching pure
   > binary data as external unparsed general entities outside the XML
   > document and then embedding reference URIs to those entities as
   > elements or attribute values. This prevents the unnecessary bloating of
   > data and wasting of processing power. The primary obstacle for using
   > these unparsed entities is their heavy reliance on DTDs, which impedes
   > modularity as well as the use of XML namespaces.
   >
   > There were several specifications introduced in the Web services
   > world to deal with this binary attachment problem using the "by
   > reference" technique. [SOAP with Attachments](http://www.w3.org/TR/SOAP-attachments)
   > is one such example. Since SOAP prohibits document type declarations
   > (DTD) in messages, this leads to the problem of not representing data
   > as part of the message infoset, therefore creating two data models.
   > This scenario is like sending attachments with an e-mail message. Even
   > though those attachments are related to the message content they are
   > not inside the message. This causes the technologies that process and
   > describe the data based on the XML component of the data to
   > malfunction. One example is WS-Security.

### Where Does MTOM Come In?

[MTOM (SOAP
Message Transmission Optimization Mechanism)](http://www.w3.org/TR/2004/PR-soap12-mtom-20041116/) is another specification
that focuses on solving the "Attachments" problem. MTOM tries to leverage the
advantages of the above two techniques by trying to merge the two techniques.
MTOM is actually a "by reference" method. The wire format of a MTOM optimized
message is the same as the SOAP with Attachments message, which also makes it
backward compatible with SwA endpoints. The most notable feature of MTOM is
the use of the XOP:Include element, which is defined in the [XML Binary Optimized
Packaging (XOP)](http://www.w3.org/TR/2004/PR-xop10-20041116/) specification to reference the binary attachments
(external unparsed general entities) of the message. With the use of this
exclusive element, the attached binary content logically becomes inline (by
value) with the SOAP document even though it is actually attached separately.
This merges the two realms by making it possible to work only with one data
model. This allows the applications to process and describe by only looking
at the XML part, making the reliance on DTDs obsolete. On a lighter note, MTOM has standardized the referencing mechanism of SwA. The following is an
extract from the [XOP](http://www.w3.org/TR/2004/PR-xop10-20041116/) specification.

*At the conceptual level, this binary data can be thought of as being
base64-encoded in the XML Document. As this conceptual form might be needed
during some processing of the XML document (e.g., for signing the XML
document), it is necessary to have a one-to-one correspondence between XML
Infosets and XOP Packages. Therefore, the conceptual representation of such
binary data is as if it were base64-encoded, using the canonical lexical form
of the XML Schema base64Binary datatype (see [[XML
Schema Part 2: Datatypes Second Edition]](#docs-mtom-guide--xmlschemap2)  [3.2.16
base64Binary](http://www.w3.org/TR/2004/REC-xmlschema-2-20041028/#base64Binary)). In the reverse direction, XOP is capable of optimizing
only base64-encoded Infoset data that is in the canonical lexical
form.*

Apache Axis2 supports **Base64 encoding**, **SOAP with
Attachments** and **MTOM (SOAP Message Transmission Optimization
Mechanism).**

## MTOM with Axis2

### Programming Model

AXIOM is (and may be the first) Object Model that has the ability to hold
binary data. It has this ability as OMText can hold raw binary content in the
form of jakarta.activation.DataHandler. OMText has been chosen for this purpose
with two reasons. One is that XOP (MTOM) is capable of optimizing only
base64-encoded Infoset data that is in the canonical lexical form of XML
Schema base64Binary datatype. Other one is to preserve the infoset in both
the sender and receiver. (To store the binary content in the same kind of
object regardless of whether it is optimized or not).

MTOM allows to selectively encode portions of the message, which allows us
to send base64encoded data as well as externally attached raw binary data
referenced by the "XOP" element (optimized content) to be sent in a SOAP
message. You can specify whether an OMText node that contains raw binary data
or base64encoded binary data is qualified to be optimized at the time of
construction of that node or later. For optimum efficiency of MTOM, a user is
advised to send smaller binary attachments using base64encoding
(non-optimized) and larger attachments as optimized content.

```
        OMElement imageElement = fac.createOMElement("image", omNs);

        // Creating the Data Handler for the file.  Any implementation of
        // jakarta.activation.DataSource interface can fit here.
        jakarta.activation.DataHandler dataHandler = new jakarta.activation.DataHandler(new FileDataSource("SomeFile"));
      
        //create an OMText node with the above DataHandler and set optimized to true
        OMText textData = fac.createOMText(dataHandler, true);

        imageElement.addChild(textData);

        //User can set optimized to false by using the following
        //textData.doOptimize(false);
```

Also, a user can create an optimizable binary content node using a base64
encoded string, which contains encoded binary content, given with the MIME
type of the actual binary representation.

```
        String base64String = "some_base64_encoded_string";
        OMText binaryNode =fac.createOMText(base64String,"image/jpg",true);
```

Axis2 uses jakarta.activation.DataHandler to handle the binary data. All the
optimized binary content nodes will be serialized as Base64 Strings if "MTOM
is not enabled". You can also create binary content nodes, which will not be
optimized at any case. They will be serialized and sent as Base64 Strings.

```
        //create an OMText node with the above DataHandler and set "optimized" to false
        //This data will be send as Base64 encoded string regardless of MTOM is enabled or not
        jakarta.activation.DataHandler dataHandler = new jakarta.activation.DataHandler(new FileDataSource("SomeFile"));
        OMText textData = fac.createOMText(dataHandler, false); 
        image.addChild(textData);
```

### Enabling MTOM Optimization on the Client Side

In Options, set the "enableMTOM" property to True when sending
messages.

```
        ServiceClient serviceClient = new ServiceClient ();
        Options options = new Options();
        options.setTo(targetEPR);
        options.setProperty(Constants.Configuration.ENABLE_MTOM, Constants.VALUE_TRUE);
        serviceClient .setOptions(options);
```

When this property is set to True, any SOAP envelope, regardless of
whether it contains optimizable content or not, will be serialized as an MTOM
optimized MIME message.

Axis2 serializes all binary content nodes as Base64 encoded strings
regardless of whether they are qualified to be optimized or not

- if the "enableMTOM" property is set to False.
- if the envelope contains any element information items of the name
  xop:Include (see [[XML-binary Optimized Packaging]](#docs-mtom-guide--xop) [3. XOP
  Infosets Constructs](http://www.w3.org/TR/2005/REC-xop10-20050125/#xop_infosets) ).

The user does **not** have to specify anything in order for
Axis2 to receive MTOM optimised messages. Axis2 will automatically identify
and de-serialize accordingly, as and when an MTOM message arrives.

### Enabling MTOM Optimization on the Server Side

The Axis 2 server automatically identifies incoming MTOM optimized
messages based on the content-type and de-serializes them accordingly. The
user can enableMTOM on the server side for outgoing messages,

> To enableMTOM globally for all services, users can set the "enableMTOM"
> parameter to True in the Axis2.xml. When it is set, all outgoing messages
> will be serialized and sent as MTOM optimized MIME messages. If it is not
> set, all the binary data in the binary content nodes will be serialized as
> Base64 encoded strings. This configuration can be overriden in services.xml
> on the basis of per service and per operation.

```
<parameter name="enableMTOM">true</parameter>
```

You must restart the server after setting this parameter.

### Accessing Received Binary Data (Sample Code)

- **Service**

```
public class MTOMService {
    public void uploadFileUsingMTOM(OMElement element) throws Exception {

       OMText binaryNode = (OMText) (element.getFirstElement()).getFirstOMChild();
       DataHandler actualDH;
       actualDH = (DataHandler) binaryNode.getDataHandler();
            
       ... Do whatever you need with the DataHandler ...
    }
  }
```

- **Client**

```
        ServiceClient sender = new ServiceClient();        
        Options options = new Options();
        options.setTo(targetEPR); 
        // enabling MTOM
        options.set(Constants.Configuration.ENABLE_MTOM, Constants.VALUE_TRUE);
        ............

        OMElement result = sender.sendReceive(payload);
        OMElement ele = result.getFirstElement();
        OMText binaryNode = (OMText) ele.getFirstOMChild();
        
        // Retrieving the DataHandler & then do whatever the processing to the data
        DataHandler actualDH;
        actualDH = binaryNode.getDataHandler();
        .............
```

### MTOM Databinding

You can define a binary element in the schema using the schema
type="xsd:base64Binary". Having an element with the type "xsd:base64Binary"
is enough for the Axis2 code generators to identify possible MTOM
attachments, and to generate code accordingly.

Going a little further, you can use the xmime schema
(http://www.w3.org/2005/05/xmlmime) to describe the binary content more
precisely. With the xmime schema, you can indicate the type of content in the
element at runtime using an MTOM attribute extension xmime:contentType.
Furthermore, you can identify what type of data might be expected in the
element using the xmime:expectedContentType. Putting it all together, our
example element becomes:

```
      <element name="MyBinaryData" xmime:expectedContentTypes='image/jpeg' >
        <complexType>
          <simpleContent>
            <extension base="base64Binary" >

              <attribute ref="xmime:contentType" use="required"/>
            </extension>
          </simpleContent>
        </complexType>
      </element>
```

You can also use the xmime:base64Binary type to express the above
mentioned data much clearly.

```
      <element name="MyBinaryData" xmime:expectedContentTypes='image/jpeg' type="xmime:base64Binary"/>
```

### MTOM Databinding Using ADB

Let's define a full, validated doc/lit style WSDL that uses the xmime
schema, has a service that receives a file, and saves it in the server using
the given path.

```
<wsdl:definitions xmlns:tns="http://ws.apache.org/axis2/mtomsample/"
        xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/"
        xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
        xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/"
        xmlns:xmime="http://www.w3.org/2005/05/xmlmime"
        xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
        xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
        xmlns="http://schemas.xmlsoap.org/wsdl/"
        targetNamespace="http://ws.apache.org/axis2/mtomsample/">

        <wsdl:types>
                <xsd:schema xmlns="http://schemas.xmlsoap.org/wsdl/"
                        attributeFormDefault="qualified" elementFormDefault="qualified"
                        targetNamespace="http://ws.apache.org/axis2/mtomsample/">

                        <xsd:import namespace="http://www.w3.org/2005/05/xmlmime"
                                schemaLocation="http://www.w3.org/2005/05/xmlmime" />
                        <xsd:complexType name="AttachmentType">
                                <xsd:sequence>
                                        <xsd:element minOccurs="0" name="fileName"
                                                type="xsd:string" />
                                        <xsd:element minOccurs="0" name="binaryData"
                                                type="xmime:base64Binary" />
                                </xsd:sequence>
                        </xsd:complexType>
                        <xsd:element name="AttachmentRequest" type="tns:AttachmentType" />
                        <xsd:element name="AttachmentResponse" type="xsd:string" />
                </xsd:schema>
        </wsdl:types>
        <wsdl:message name="AttachmentRequest">
                <wsdl:part name="part1" element="tns:AttachmentRequest" />
        </wsdl:message>
        <wsdl:message name="AttachmentResponse">
                <wsdl:part name="part1" element="tns:AttachmentResponse" />
        </wsdl:message>
        <wsdl:portType name="MTOMServicePortType">
                <wsdl:operation name="attachment">
                        <wsdl:input message="tns:AttachmentRequest"
                                wsaw:Action="attachment" />
                        <wsdl:output message="tns:AttachmentResponse"
                                wsaw:Action="http://schemas.xmlsoap.org/wsdl/MTOMServicePortType/AttachmentResponse" />
                </wsdl:operation>
        </wsdl:portType>
        <wsdl:binding name="MTOMServiceSOAP11Binding"
                type="tns:MTOMServicePortType">
                <soap:binding transport="http://schemas.xmlsoap.org/soap/http"
                        style="document" />
                <wsdl:operation name="attachment">
                        <soap:operation soapAction="attachment" style="document" />
                        <wsdl:input>
                                <soap:body use="literal" />
                        </wsdl:input>
                        <wsdl:output>
                                <soap:body use="literal" />
                        </wsdl:output>
                </wsdl:operation>
        </wsdl:binding>
        <wsdl:binding name="MTOMServiceSOAP12Binding"
                type="tns:MTOMServicePortType">
                <soap12:binding transport="http://schemas.xmlsoap.org/soap/http"
                        style="document" />
                <wsdl:operation name="attachment">
                        <soap12:operation soapAction="attachment" style="document" />
                        <wsdl:input>
                                <soap12:body use="literal" />
                        </wsdl:input>
                        <wsdl:output>
                                <soap12:body use="literal" />
                        </wsdl:output>
                </wsdl:operation>
        </wsdl:binding>
        <wsdl:service name="MTOMSample">
                <wsdl:port name="MTOMSampleSOAP11port_http"
                        binding="tns:MTOMServiceSOAP11Binding">
                        <soap:address
                                location="http://localhost:8080/axis2/services/MTOMSample" />
                </wsdl:port>
                <wsdl:port name="MTOMSampleSOAP12port_http"
                        binding="tns:MTOMServiceSOAP12Binding">
                        <soap12:address
                                location="http://localhost:8080/axis2/services/MTOMSample" />
                </wsdl:port>
        </wsdl:service>
</wsdl:definitions>
```

The important point here is we import http://www.w3.org/2005/05/xmlmime
and define the element 'binaryData' that utilizes MTOM.

The next step is using the Axis2 tool 'WSDL2Java' to generate Java source
files from this WSDL. See the 'Code Generator Tool' guide for more
information. Here, we define an Ant task that chooses ADB (Axis2 Data
Binding) as the databinding implementation. The name we list for the WSDL
above is MTOMSample.wsdl, and we define our package name for our generated
source files to 'sample.mtom.service' . Our Ant task for this example is:

```
        
<target name="generate.service">
                 <java classname="org.apache.axis2.wsdl.WSDL2Java">
                        <arg value="-uri" />
                        <arg value="${basedir}/resources/MTOMSample.wsdl" />
                        <arg value="-ss" />
                        <arg value="-sd" />
                          <arg value="-g"/>
                        <arg value="-p" />
                        <arg value="sample.mtom.service" />
                        <arg value="-o" />
                        <arg value="${service.dir}" />
                        <classpath refid="class.path" />
                </java>
          </target>
```

Now we are ready to code. Let's edit
output/src/sample/mtom/service/MTOMSampleSkeleton.java and fill in the
business logic. Here is an example:

```
        public org.apache.ws.axis2.mtomsample.AttachmentResponse attachment(
                        org.apache.ws.axis2.mtomsample.AttachmentRequest param0) throws Exception
        {
                AttachmentType attachmentRequest = param0.getAttachmentRequest();
                Base64Binary binaryData = attachmentRequest.getBinaryData();
                DataHandler dataHandler = binaryData.getBase64Binary();
                File file = new File(
                                attachmentRequest.getFileName());
                FileOutputStream fileOutputStream = new FileOutputStream(file);
                dataHandler.writeTo(fileOutputStream);
                fileOutputStream.flush();
                fileOutputStream.close();
                
                AttachmentResponse response = new AttachmentResponse();
                response.setAttachmentResponse("File saved succesfully.");
                return response;
        }
```

The code above receives a file and writes it to the disk using the given
file name. It returns a message once it is successful. Now let's define the
client:

```
        public static void transferFile(File file, String destination)
                        throws RemoteException {
                MTOMSampleStub serviceStub = new MTOMSampleStub();

                // Enable MTOM in the client side
                serviceStub._getServiceClient().getOptions().setProperty(
                                Constants.Configuration.ENABLE_MTOM, Constants.VALUE_TRUE);
                //Increase the time out when sending large attachments
                serviceStub._getServiceClient().getOptions().setTimeOutInMilliSeconds(10000);

                // Populating the code generated beans
                AttachmentRequest attachmentRequest = new AttachmentRequest();
                AttachmentType attachmentType = new AttachmentType();
                Base64Binary base64Binary = new Base64Binary();

                // Creating a jakarta.activation.FileDataSource from the input file.
                FileDataSource fileDataSource = new FileDataSource(file);

                // Create a dataHandler using the fileDataSource. Any implementation of
                // jakarta.activation.DataSource interface can fit here.
                DataHandler dataHandler = new DataHandler(fileDataSource);
                base64Binary.setBase64Binary(dataHandler);
                base64Binary.setContentType(dataHandler.getContentType());
                attachmentType.setBinaryData(base64Binary);
                attachmentType.setFileName(destination);
                attachmentRequest.setAttachmentRequest(attachmentType);

                AttachmentResponse response = serviceStub.attachment(attachmentRequest);
                System.out.println(response.getAttachmentResponse());
        }
```

The last step is to create an AAR with our Skeleton and the services.xml
and then deploy the service. You can find the completed sample in the Axis2
standard binary distribution under the samples/mtom directory

## SOAP with Attachments (SwA) with Axis2

### Receiving SwA Type Attachments

Axis2 automatically identifies SwA messages based on the content type.
Axis2 stores the references on the received attachment parts (MIME parts) in
the Message Context. Axis2 preserves the order of the received attachments
when storing them in the MessageContext. Users can access binary attachments
using the attachement API given in the Message Context using the content-id
of the mime part as the key. Care needs be taken to rip off the "cid" prefix
when content-id is taken from the "Href" attributes. Users can access the
message context from whithin a service implementation class using the
"setOperationContext()" method as shown in the following example.

Note: Axis2 supports content-id based referencing only. Axis2 does not
support Content Location based referencing of MIME parts.

- **Sample service which accesses a received SwA type
  attachment**

```
public class SwA {
    public SwA() {
    }
    
    public void uploadAttachment(OMElement omEle) throws AxisFault {
        OMElement child = (OMElement) omEle.getFirstOMChild();
        OMAttribute attr = child.getAttribute(new QName("href"));
        
        //Content ID processing
        String contentID = attr.getAttributeValue();
        contentID = contentID.trim();
        if (contentID.substring(0, 3).equalsIgnoreCase("cid")) {
            contentID = contentID.substring(4);
        }
        
        MessageContext msgCtx = MessageContext.getCurrentMessageContext();
        Attachments attachment = msgCtx.getAttachmentMap();
        DataHandler dataHandler = attachment.getDataHandler(contentID);
        ...........
    }
}
```

### Sending SwA Type Attachments

The user needs to set the "enableSwA" property to True in order to be able
to send SwA messages. The Axis2 user is **not** expected to
enable MTOM and SwA together. In such a situation, MTOM will get priority
over SwA.

This can be set using the axis2.xml as follows.

```
  
        <parameter name="enableSwA">true</parameter>
```

"enableSwA" can also be set using the client side Options as follows

```
  
        options.setProperty(Constants.Configuration.ENABLE_SwA, Constants.VALUE_TRUE);
```

Users are expected to use the attachment API provided in the
MessageContext to specify the binary attachments needed to be attached to the
outgoing message as SwA type attachments. Client side SwA capability can be
used only with the OperationClient api, since the user needs the ability to
access the MessageContext.

- **Sample client which sends a message with SwA type
  attachments**

```
   public void uploadFileUsingSwA(String fileName) throws Exception {

        Options options = new Options();
        options.setTo(targetEPR);
        options.setProperty(Constants.Configuration.ENABLE_SWA, Constants.VALUE_TRUE);
        options.setTransportInProtocol(Constants.TRANSPORT_HTTP);
        options.setSoapVersionURI(SOAP11Constants.SOAP_ENVELOPE_NAMESPACE_URI);
        options.setTo(targetEPR);
  
        ServiceClient sender = new ServiceClient(null,null);
        sender.setOptions(options);
        OperationClient mepClient = sender.createClient(ServiceClient.ANON_OUT_IN_OP);
        
        MessageContext mc = new MessageContext();   
        mc.setEnvelope(createEnvelope());
        FileDataSource fileDataSource = new FileDataSource("test-resources/mtom/test.jpg");
        DataHandler dataHandler = new DataHandler(fileDataSource);
        mc.addAttachment("FirstAttachment",dataHandler);
       
        mepClient.addMessageContext(mc);
        mepClient.execute(true);
    }
```

### MTOM Backward Compatibility with SwA

MTOM specification is designed to be backward compatible with the SOAP
with Attachments specification. Even though the representation is different, both technologies have the same wire format. We can safely assume that any
SOAP with Attachments endpoint can accept MTOM optimized messages and treat
them as SOAP with Attachment messages - any MTOM optimized message is a valid
SwA message.

Note : Above backword compatibility was succesfully tested against Axis
1.x

- **A sample SwA message from Axis 1.x**

```
Content-Type: multipart/related; type="text/xml"; 
          start="<9D645C8EBB837CE54ABD027A3659535D>";
                boundary="----=_Part_0_1977511.1123163571138"

------=_Part_0_1977511.1123163571138
Content-Type: text/xml; charset=UTF-8
Content-Transfer-Encoding: binary
Content-Id: <9D645C8EBB837CE54ABD027A3659535D>

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="...."....>
    ........
                <source href="cid:3936AE19FBED55AE4620B81C73BDD76E" xmlns="/>

    ........
</soapenv:Envelope>
------=_Part_0_1977511.1123163571138
Content-Type: text/plain
Content-Transfer-Encoding: binary
Content-Id: <3936AE19FBED55AE4620B81C73BDD76E>

Binary Data.....
------=_Part_0_1977511.1123163571138--
```

- **Corresponding MTOM message from Axis2**

```
Content-Type: multipart/related; boundary=MIMEBoundary4A7AE55984E7438034;
                         type="application/xop+xml"; start="<0.09BC7F4BE2E4D3EF1B@apache.org>";
                         start-info="text/xml; charset=utf-8"

--MIMEBoundary4A7AE55984E7438034
content-type: application/xop+xml; charset=utf-8; type="application/soap+xml;"
content-transfer-encoding: binary
content-id: <0.09BC7F4BE2E4D3EF1B@apache.org>

<?xml version='1.0' encoding='utf-8'?>
<soapenv:Envelope xmlns:soapenv="...."....>
  ........
         <xop:Include href="cid:1.A91D6D2E3D7AC4D580@apache.org" 
                        xmlns:xop="http://www.w3.org/2004/08/xop/include">
         </xop:Include>
  ........

</soapenv:Envelope>
--MIMEBoundary4A7AE55984E7438034
content-type: application/octet-stream
content-transfer-encoding: binary
content-id: <1.A91D6D2E3D7AC4D580@apache.org>

Binary Data.....
--MIMEBoundary4A7AE55984E7438034--
```

## Advanced Topics

### File Caching for Attachments

Axis2 comes handy with a file caching mechanism for incoming attachments, which gives Axis2 the ability to handle very large attachments without
buffering them in the memory at any time. Axis2 file caching streams the
incoming MIME parts directly into the files, after reading the MIME part
headers.

Also, a user can specify a size threshold for the File caching (in bytes).
When this threshold value is specified, only the attachments whose size is
bigger than the threshold value will get cached in the files. Smaller
attachments will remain in the memory.

Note : It is a must to specify a directory to temporarily store the
attachments. Also care should be taken to **clean that
directory** from time to time.

The following parameters need to be set in Axis2.xml in order to enable
file caching.

```
<axisconfig name="AxisJava2.0">

    <!-- ================================================= -->
    <!-- Parameters -->
    <!-- ================================================= -->
    <parameter name="cacheAttachments">true</parameter>
    <parameter name="attachmentDIR">temp directory</parameter>

    <parameter name="sizeThreshold">4000</parameter>
    .........
    .........
</axisconfig>
```

Enabling file caching for client side receiving can be done for the by
setting the Options as follows.

```
options.setProperty(Constants.Configuration.CACHE_ATTACHMENTS,Constants.VALUE_TRUE);
options.setProperty(Constants.Configuration.ATTACHMENT_TEMP_DIR,TempDir);
options.setProperty(Constants.Configuration.FILE_SIZE_THRESHOLD, "4000");
```

---

<a id="docs-http-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/http-transport.html -->

<!-- page_index: 26 -->

# HTTP Transport

This document covers the sending and receiving of SOAP messages with Axis2 using HTTP
as the transport mechanism.

## Contents

- [HTTPClient5TransportSender](#docs-http-transport--httpclient5transportsender)
  - [HTTPS support](#docs-http-transport--httpsupport)
  - [Further customization](#docs-http-transport--further)
- [Timeout Configuration](#docs-http-transport--timeout_config)
- [HTTP Version Configuration](#docs-http-transport--version_config)
- [Proxy Authentication](#docs-http-transport--auth)
- [Basic, Digest and NTLM Authentication](#docs-http-transport--preemptive_auth)
- [Reusing the httpclient object](#docs-http-transport--reusing_httpclient_object)
- [Setting the cached httpclient object](#docs-http-transport--setting_cached_httpclient_object)

## HTTPClient5TransportSender

HTTPClient5TransportSender is the transport sender that is used by default in both
the Server and Client APIs. As its name implies, it is based on [Apache HttpComponents](http://hc.apache.org/).
For maximum flexibility, this sender supports both the HTTP GET and POST interfaces.
(REST in Axis2 also supports both interfaces.)

Axis2 uses a single HTTPClient instance per ConfigurationContext (which usually means per instance
of ServiceClient). This pattern allows for HTTP 1.1 to automatically reuse TCP connections - in earlier versions of Axis2 the REUSE\_HTTP\_CLIENT configuration property was necessary to enable this functionality, but as of 1.5 this is no longer necessary.

Apache HttpComponents also provides HTTP 1.1, Chunking and KeepAlive support for Axis2.

The <transportSender/> element defines transport senders in
the axis2.xml configuration file as follows:

```

<transportSender name="http" class="org.apache.axis2.transport.http.impl.httpclient5.HTTPClient5TransportSender">
   <parameter name="PROTOCOL">HTTP/1.1</parameter>
   <parameter name="Transfer-Encoding">chunked</parameter>
</transportSender>
```

The above code snippet shows the simplest configuration of a transport
sender for common use. The <parameter/> element is used to specify additional
constraints that the sender should comply with. The HTTP PROTOCOL parameter
should be set as HTTP/1.0 or HTTP/1.1. The default version is HTTP/1.1. Note that
chunking support is available only for HTTP/1.1. Thus, even if "chunked" is specified
as a parameter, if the HTTP version is 1.0, this setting will be
ignored by the transport framework. Also, KeepAlive is enabled by default in
HTTP/1.1.

If you use HTTP1.1 for its Keep-Alive ability, but you need to disable
chunking at runtime (some servers don't allow chunked requests to
prevent denial of service), you can do so in the Stub:

```

options.setProperty(HTTPConstants.CHUNKED, "false");
```

Some absolute properties are provided at runtime instead. For example, character
encoding style (UTF-8, UTF-16, etc.) is provided via MessageContext.

### HTTPS support

HTTPClient5TransportSender can be also used to communicate over https.

```

   <transportSender name="https" class="org.apache.axis2.transport.http.impl.httpclient5.HTTPClient5TransportSender">
      <parameter name="PROTOCOL">HTTP/1.1</parameter>
      <parameter name="Transfer-Encoding">chunked</parameter>
   </transportSender>
```

Please note that by default HTTPS works only when the server does not
expect to authenticate the clients (1-way SSL only) and where the
server has the clients' public keys in its trust store.

If you want to perform SSL client authentication (2-way SSL), you may
configure your own HttpClient class and customize it as desired - see the
example below.

To control the max connections per host attempted in parallel by a
reused httpclient, or any other advanced parameters, you need to
set the cached httpclient object when your application starts up
(before any actual axis request). You can set the relevant property
as shown below by using HTTPConstants.CACHED\_HTTP\_CLIENT.

The following code was tested with Axis2 on Wildfly 32, the cert was obtained by
'openssl s\_client -connect myserver:8443 -showcerts'

```

        String wildflyserver_cert_path = "src/wildflyserver.crt";
        Certificate certificate = CertificateFactory.getInstance("X.509").generateCertificate(new FileInputStream(new File(wildflyserver_cert_path)));
        KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
        keyStore.load(null, null);
        keyStore.setCertificateEntry("server", certificate);

        TrustManagerFactory trustManagerFactory = null;
        trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        trustManagerFactory.init(keyStore);
        TrustManager[] trustManagers = trustManagerFactory.getTrustManagers();
        if (trustManagers.length != 1 || !(trustManagers[0] instanceof X509TrustManager)) {
            throw new Exception("Unexpected default trust managers:" + Arrays.toString(trustManagers));
        }

        SSLContext sslContext = SSLContext.getInstance("TLSv1.3");
        sslContext.init(null, trustManagers, new SecureRandom());

	// NoopHostnameVerifier to trust self-singed cert
        SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sslContext, NoopHostnameVerifier.INSTANCE);

	HttpClientConnectionManager connManager = PoolingHttpClientConnectionManagerBuilder.create().setSSLSocketFactory(sslsf).setMaxConnTotal(100).setMaxConnPerRoute(100).build();

        HttpClient httpclient = HttpClients.custom().setConnectionManager(connManager.setConnectionManagerShared(true).build();
	Options options = new Options();
        options.setTo("myurl");
        options.setTransportInProtocol(Constants.TRANSPORT_HTTP);
        options.setTimeOutInMilliSeconds(120000);
        options.setProperty(HTTPConstants.CACHED_HTTP_CLIENT, httpClient);
        ServiceClient sender = new ServiceClient();
        sender.setOptions(options);
```

## Further customization

References to the core HTTP classes used by Axis2 Stub classes can be obtained below.

```

TransportOutDescription transportOut = new TransportOutDescription("https");
HTTPClient5TransportSender sender = new HTTPClient5TransportSender();
sender.init(stub._getServiceClient().getServiceContext().getConfigurationContext(), transportOut);
transportOut.setSender(sender);
options.setTransportOut(transportOut);
```

## Async Thread Pool

For Async requests, the axis2 thread pool core size is set to 5. That can
be changed as shown below.

```

configurationContext.setThreadPool(new ThreadPool(200, Integer.MAX_VALUE));
```

## Timeout Configuration

Two timeout instances exist in the transport level, Socket timeout
and Connection timeout. These can be configured either at deployment
or run time. If configuring at deployment time, the user has to add the
following lines in axis2.xml.

For Socket timeout:

```
<parameter name="SO_TIMEOUT">some_integer_value</parameter>
```

For Connection timeout:

```
 <parameter name="CONNECTION_TIMEOUT">some_integer_value</parameter>
```

For runtime configuration, it can be set as follows within the client stub:

```

...
Options options = new Options();
options.setProperty(HTTPConstants.SO_TIMEOUT, new Integer(timeOutInMilliSeconds));
options.setProperty(HTTPConstants.CONNECTION_TIMEOUT, new Integer(timeOutInMilliSeconds));

// or
options.setTimeOutInMilliSeconds(timeOutInMilliSeconds);
...
```

## HTTP Version Configuration

The default HTTP version is 1.1. There are two methods in which the user
can change the HTTP version to 1.0

- By defining the version in axis2.xml as shown below.

```
 <parameter name="PROTOCOL">HTTP/1.0</parameter>
```

- By changing the version at runtime by using code similar to the following:

```

...
options.setProperty(org.apache.axis2.context.MessageContextConstants.HTTP_PROTOCOL_VERSION,
   org.apache.axis2.transport.http.HTTPConstants.HEADER_PROTOCOL_10);
...
```

## Proxy Authentication

The Apache Httpcomponents client has built-in support for proxy
authentication. Axis2 uses deployment time and runtime mechanisms to
authenticate proxies. At deployment time, the user has to change the
axis2.xml as follows. This authentication is available for both HTTP and
HTTPS.

```

<transportSender name="http" class="org.apache.axis2.transport.http.impl.httpclient5.HTTPClient5TransportSender">
   <parameter name="PROTOCOL">HTTP/1.1</parameter>
   <parameter name="PROXY" proxy_host="proxy_host_name" proxy_port="proxy_host_port">userName:domain:passWord</parameter>
</transportSender>
```

For a particular proxy, if authentication is not available, enter the
"userName:domain:passWord" as "anonymous:anonymous:anonymous".

Prior shown configuration has been deprecated after Axis2 1.2 release and we strongly recommend using the new
proxy configuration as below.

New proxy configuration would require the user to add a TOP level parameter in the axis2.xml named "Proxy".

```

<parameter name="Proxy">
    <Configuration>
        <ProxyHost>example.org</ProxyHost>
        <ProxyPort>5678</ProxyPort>
        <ProxyUser>EXAMPLE\saminda</ProxyUser>
        <ProxyPassword>ppp</ProxyPassword>
    </Configuration>
</parameter>
    
```

Thus, if its a open proxy, user can ignore ProxyUser and ProxyPassword elements.

In addition to this, if you don't want to go through writing the above parameter you could
use Java Networking Properties for open proxies,
-Dhttp.proxyHost=10.150.112.254 -Dhttp.proxyPort=8080

At runtime, the user can override the PROXY settings using the
HttpTransportProperties.ProxyProperties object. Within your client stub, create an instance of this object, configure proxy values for it, and then set it to the MessageContext's property bag via options.setProperty().
For example:

```

...
Options options = new Options();
...

HttpTransportProperties.ProxyProperties proxyProperties = new HttpTransportProperties.new ProxyProperties();
proxyProperties.setProxyHostName(....);
proxyProperties.setProxyPort(...);
...
options.setProperty(HttpConstants.PROXY, proxyProperties);
...
```

The above code will override the deployment proxy configuration settings.

## Basic, Digest and NTLM Authentication

Note: Basic preemptive authentication requires a work around described in
https://issues.apache.org/jira/browse/AXIS2-6055 until a proper fix is contributed by
the community as we lack committers who use it.

HttpClient supports three different types of HTTP authentication schemes:
Basic, Digest and NTLM. Based on the challenge provided by the server, HttpClient automatically selects the authentication scheme with which the
request should be authenticated. The most secure method is NTLM and the Basic
is the least secure.

NTLM is the most complex of the authentication protocols supported by
HttpClient. It requires an instance of NTCredentials to be available for the
domain name of the server or the default credentials. Note that since NTLM
does not use the notion of realms, HttpClient uses the domain name of the
server as the name of the realm. Also note that the username provided to the
NTCredentials should not be prefixed with the domain - ie: "axis2" is correct
whereas "DOMAIN\axis2" is not correct.

There are some significant differences in the way that NTLM works compared
with basic and digest authentication. These differences are generally handled
by HttpClient, however having an understanding of these differences can help
avoid problems when using NTLM authentication.

1. NTLM authentication works almost exactly the same way as any other form
   of authentication in terms of the HttpClient API. The only difference is
   that you need to supply 'NTCredentials' instead of
   'UsernamePasswordCredentials' (NTCredentials actually extends
   UsernamePasswordCredentials so you can use NTCredentials right throughout
   your application if need be).
2. The realm for NTLM authentication is the domain name of the computer to
   which you are being connected. This can become troublesome as servers often
   have multiple domain names that refer to them. Only the domain name that
   the HttpClient connects to (as specified by the HostConfiguration) is
   used to look up the credentials. It is generally advised that while
   initially testing NTLM authentication, you pass the realm as null, which
   is its default value.
3. NTLM authenticates a connection and not a request. So you need to
   authenticate every time a new connection is made, and keeping the
   connection open during authentication is vital. Because of this, NTLM cannot
   be used to authenticate with both a proxy and the server, nor can NTLM be
   used with HTTP 1.0 connections or servers that do not support HTTP
   keep-alives.

Axis2 also allows adding a custom Authentication Scheme to HttpClient.

The static inner bean Authenticator of HttpTransportProperties will hold
the state of the server to be authenticated with. Once filled, it has to be
set to the Options's property bag with the key as HTTPConstants.AUTHENTICATE.
The following code snippet shows how to configure the transport
framework to use Basic Authentication:

```

...
Options options = new Options();
 
HttpTransportProperties.Authenticator
   auth = new HttpTransportProperties.Authenticator();
auth.setUsername("username");
auth.setPassword("password");
// set if realm or domain is known

options.setProperty(org.apache.axis2.transport.http.HTTPConstants.AUTHENTICATE, auth);
...
```

## Reusing the httpclient object

By default, a new httpclient object is created for each send. It may
be worthwhile to reuse the same httpclient object to take advantage of
HTTP1.1 Keep-Alive, especially in HTTPS environment, where the SSL
handshake may not be of negligible cost. To reuse the same httpclient
object, you can set the relevant property in the Stub:

```
options.setProperty(HTTPConstants.REUSE_HTTP_CLIENT, "true");
```

## Setting the cached httpclient object

See the SSL example for a definition of the HTTPClient Object.

```

configurationContext.setProperty(HTTPConstants.CACHED_HTTP_CLIENT, client);
```

## Setting the cached httpstate object

HttpState object can be set as property to the options of a given Axis2 client.
HttpState keeps HTTP attributes that may persist from request to request, such
as cookies and authentication credentials. So, it is possible to re-use one and
the same HttpState object if appropriate.
The idea is to provide the capability to specify/associate a separate HttpState
with every client and still reuse one and the same HttpClient. So, this make
sense only when CACHED\_HTTP\_CLIENT is re-used between different clients
from different threads which may invoke different hosts with different credentials
and cookies. This is really complicated scenario, but is absolutely possible one.
If you re-use a common HttpClient between different clients then the clients will
re-use, the internal for the HttpClient, HttpState object. Doing so authentication
credentials are exposed to all clients sharing one and the same HttpClient.
This is definitely not a good idea. The problem with Cookies is different. The
problem here is that if two distinct clients invoke one and the same service
at a specific host then the session established with a given cookie by one of
the clients can wrongly be shared among them, too, if it has not expired. This
will cause problems since the two client may need different sessions, which is
the more probable scenario.
Sample configuration:

```

HttpState myHttpState = new HttpState();
options.setProperty(WSClientConstants.CACHED_HTTP_STATE, myHttpState);
```

Doing so the HttpState is attached to the client. Respectively this is automatically propagated to all MessageContext objects used by the client.
Underneath this just instructs Axis2 that the CACHED\_HTTP\_STATE set should be passed as a parameter when HttpClient#executeMethod is invoked.

---

<a id="docs-servlet-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/servlet-transport.html -->

<!-- page_index: 27 -->

# HTTP servlet transport

# Introduction

The servlet transport processes HTTP requests received through the servlet
container in which Axis2 is deployed. It is different from the other transports
because its lifecycle is not managed by Axis2, but by the servlet container.
Two things are necessary to enable and configure the servlet transport:

- `org.apache.axis2.transport.http.AxisServlet` must be registered
  and mapped as a servlet in `web.xml`.
- One or more `org.apache.axis2.transport.http.AxisServletListener`
  instances must be declared as transport receivers in `axis2.xml`.

It should be noted that the role of `AxisServlet` is not limited to that
of an Axis2 transport, but that it provides two additional features:

- It starts the Axis2 runtime and sets it up to load the `axis2.xml`
  configuration as well as the repository from the Web application.
- It exposes the WSDL documents of deployed services. The WSDL of a service can be
  accessed by appending `?wsdl` to the EPR of the service.

# Adding AxisServlet to web.xml

`AxisServlet` is typically configured as follows in `web.xml`:

```

    <servlet>
        <servlet-name>AxisServlet</servlet-name>
        <display-name>Apache-Axis Servlet</display-name>
        <servlet-class>org.apache.axis2.transport.http.AxisServlet</servlet-class>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>AxisServlet</servlet-name>
        <url-pattern>/services/*</url-pattern>
    </servlet-mapping>
```

Note that the prefix used in `url-pattern` must match the
`servicePath` parameter in `axis2.xml`. The default
value of this parameter is `services`, which is compatible
with the above configuration.

# Configuring axis2.xml

For each protocol (HTTP and/or HTTPS), an `AxisServletListener`
instance must be declared in `axis2.xml`. If only a single
protocol is used, no further configuration is required. For example, if only HTTP is used, the following declaration must be present in
`axis2.xml`:

```

<transportReceiver name="http" class="org.apache.axis2.transport.http.AxisServletListener"/>
```

If both HTTP and HTTPS are used, then things become a bit more complicated.
The reason is that in order to expose WSDLs with correct endpoint URIs, `AxisServlet` must know the ports used by HTTP and HTTPS.
Unfortunately the servlet API doesn't allow a Web application to discover
all configured protocols. It only provides information about the protocol, host name and port for the current request. If only a single
`AxisServletListener` is configured, then this information is enough
to let `AxisServlet` auto-detect the port number. If both HTTP
and HTTPS are used (or if WSDLs are retrieved through transports other than
`AxisServlet`), then `AxisServlet` has no way of knowing the
port numbers until it has processed at least one request
for each protocol. To make WSDL generation predictable in this scenario, it
is necessary to explicitly configure the port numbers in `axis2.xml`, such as in the following example:

```

<transportReceiver name="http" class="org.apache.axis2.transport.http.AxisServletListener">
    <parameter name="port">8080</parameter>
</transportReceiver>

<transportReceiver name="https" class="org.apache.axis2.transport.http.AxisServletListener">
    <parameter name="port">8443</parameter>
</transportReceiver>
```

---

<a id="docs-jms-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/jms-transport.html -->

<!-- page_index: 28 -->

# JMS Transport

## Content

- [JMS Transport](#docs-jms-transport--jms_transport)
  - [Content](#docs-jms-transport--content)
  - [Transport configuration](#docs-jms-transport--transport_configuration)
  - [Transport listener](#docs-jms-transport--transport_listener)
    - [JMS connections and message dispatching](#docs-jms-transport--jms_connections_and_message_dispatching)
    - [Service configuration](#docs-jms-transport--service_configuration)
    - [Message context properties for incoming messages](#docs-jms-transport--message_context_properties_for_incoming_messages)
  - [Transport sender](#docs-jms-transport--transport_sender)
    - [Endpoint references](#docs-jms-transport--endpoint_references)
    - [Message context properties for outcoming messages](#docs-jms-transport--message_context_properties_for_outcoming_messages)
  - [Content type detection](#docs-jms-transport--content_type_detection)

## Transport configuration

Connection factories are configured using parameters in the transport description in `axis2.xml`. The syntax is the same for the transport listener and sender. For example, the following configuration sets up the JMS listener with three connection factories:

```
<transportReceiver name="jms" class="org.apache.axis2.transport.jms.JMSListener">
    <parameter name="myTopicConnectionFactory" locked="false">                      
        <parameter name="java.naming.factory.initial" locked="false">org.apache.activemq.jndi.ActiveMQInitialContextFactory</parameter>
        <parameter name="java.naming.provider.url" locked="false">tcp://localhost:61616</parameter>         
        <parameter name="transport.jms.ConnectionFactoryJNDIName" locked="false">TopicConnectionFactory</parameter>
    </parameter>
    <parameter name="myQueueConnectionFactory" locked="false">
        <parameter name="java.naming.factory.initial" locked="false">org.apache.activemq.jndi.ActiveMQInitialContextFactory</parameter>
        <parameter name="java.naming.provider.url" locked="false">tcp://localhost:61616</parameter>         
        <parameter name="transport.jms.ConnectionFactoryJNDIName" locked="false">QueueConnectionFactory</parameter>
    </parameter>
    <parameter name="default" locked="false">                       
        <parameter name="java.naming.factory.initial" locked="false">org.apache.activemq.jndi.ActiveMQInitialContextFactory</parameter>
        <parameter name="java.naming.provider.url" locked="false">tcp://localhost:61616</parameter>         
        <parameter name="transport.jms.ConnectionFactoryJNDIName" locked="false">QueueConnectionFactory</parameter>
    </parameter>
</transportReceiver>
```

If a connection factory named `default` (as shown above) is defined, this would be used for services which does not explicitly specify the connection factory that should be used. The `services.xml` of a service should indicate the connection factory and the destination name to be associated with. If a destination is not specified, the implementation would create a JMS Queue with the service name. The JMS destination should ideally be created and administered through the JMS provider utilities.

For the JMS sender, only the outer element is different:

```
<transportSender name="jms" class="org.apache.axis2.transport.jms.JMSSender">
    ...
</transportSender>
```

As explained below, for the JMS sender configuration it is not mandatory (but recommended) to specify connection factories.

The parameters that may appear in a connection factory configuration are defined as follows:

`java.naming.factory.initial`
:   REQUIRED - JNDI initial context factory class. The class must implement the java.naming.spi.InitialContextFactory interface.

`java.naming.provider.url`
:   REQUIRED - URL of the JNDI provider

`transport.jms.ConnectionFactoryJNDIName`
:   REQUIRED - The JNDI name of the connection factory

`java.naming.security.principal`
:   JNDI Username

`java.naming.security.credentials`
:   JNDI password

`transport.Transactionality`
:   Desired mode of transactionality. possible values are 'none', 'local' or 'jta', while it defaults to 'none'

`transport.UserTxnJNDIName`
:   JNDI name to be used to require user transaction

`transport.CacheUserTxn`
:   Whether caching for user transactions should be enabled or not. Possible values are 'true' or 'false', while the value defaults to 'true'

`transport.jms.SessionTransacted`
:   Whether the JMS session be transacted or not. Possible values are 'true' or 'false', while the value defaults to 'true' if the transactionality is 'local'

`transport.jms.SessionAcknowledgement`
:   JMS session acknowledgement mode. Possible values are AUTO\_ACKNOWLEDGE, CLIENT\_ACKNOWLEDGE, DUPS\_OK\_ACKNOWLEDGE, SESSION\_TRANSACTED. Default value is AUTO\_ACKNOWLEDGE

`transport.jms.ConnectionFactoryType`
:   Type of the connection factory. Possible values are 'queue' or 'topic' while the default value of 'queue'

`transport.jms.JMSSpecVersion`
:   JMS API version. Possible values are 1.1 or 1.0.2b, and the default API version is 1.1

`transport.jms.UserName`
:   The JMS connection username

`transport.jms.Password`
:   The JMS connection password

`transport.jms.DefaultReplyDestination`
:   JNDI name of the default reply destination

`transport.jms.DefaultReplyDestinationType`
:   Default type of the reply destination, if not provided the destination type will be taken as the reply destination type as well

`transport.jms.MessageSelector`
:   Message selector implementation

`transport.jms.SubscriptionDurable`
:   Whether the connection factory is subscription durable or not. Possible values are 'true' or 'false', while the value defaults to 'false'

`transport.jms.DurableSubscriberName`
:   Name of the durable subscriber. This is required if the above parameter is set to 'true'

`transport.jms.PubSubNoLocal`
:   Whether the messages should be published by the same connection they were received. Possible values are 'true' or 'false', while the value defaults to 'false'

`transport.jms.CacheLevel`
:   JMS resource cache level. Possible values are 'none', 'connection', 'session', 'consumer', 'producer', 'auto' and defaults to 'auto'

`transport.jms.ReceiveTimeout`
:   Time to wait for a JMS message during polling. Set this parameter value to a negative integer to wait indefinitely. Set to zero to prevent waiting and the default value is 1000ms

`transport.jms.ConcurrentConsumers`
:   Number of concurrent threads to be started to consume messages when polling. Defaults to 1, and the value should be a positive integer. For topics it has to be always 1

`transport.jms.MaxConcurrentConsumers`
:   Maximum number of concurrent threads to use during polling. Defaults to 1, and the value should be a positive integer. For topics it has to be always 1

`transport.jms.IdleTaskLimit`
:   The number of idle runs per thread before it dies out, which defaults to 10

`transport.jms.MaxMessagesPerTask`
:   The maximum number of successful message receipts per thread. Defaults to -1 meaning the infinity

`transport.jms.InitialReconnectDuration`
:   Initial reconnection attempts duration in milliseconds, which defaults to 1000ms

`transport.jms.ReconnectProgressFactor`
:   Factor by which the reconnection duration will be increased, which defaults to 2.

`transport.jms.MaxReconnectDuration`
:   Maximum reconnection duration in milliseconds, which defaults to 3600000ms (1 hr)

## Transport listener

### JMS connections and message dispatching

Every deployed service for which the JMS transport is enabled will be associated with a destination (queue or topic) according to the following rules:

- If the service has a `transport.jms.Destination` parameter, its value is interpreted as the JNDI name of the destination.
- Otherwise the service name is used as the JNDI name of the destination.

At the same time, the connection factory is determined by looking at the service parameter `transport.jms.ConnectionFactory`. If this parameter is not set, the default value `default` is assumed. The value of this parameter is interpreted as a logical identifier for the connection factory configuration defined in the transport configuration (see above).

It follows that JMS destinations are statically bound to services. Therefore the transport always predispatches incoming messages to the service the destination is bound to.

The message is dispatched to an operation according to the following rules:

- The transport looks for a service parameter `Operation`. If this parameter is not present, the default value `urn:mediate` is assumed.
- If the service has an operation with the corresponding name, the transport predispatches the message to that operation.
- If no such operation exists, the message will be dispatched by the Axis2 engine using the configured dispatchers.

In addition, if the JMS message has a property named `SOAPAction`, the value of this property is interpreted as the SOAP action.

### Service configuration

Apart from the following list most of the parameters defined in the global connection factory can be overriden at the service level as well

`transport.jms.ConnectionFactory` (Optional)
:   The JMS connection factory definition (from `axis2.xml`) to be used to listen for messages for this service.

`transport.jms.Destination` (Optional)
:   The JMS destination name (Defaults to a Queue with the service name).

`transport.jms.DestinationType` (Optional)
:   The JMS destination type. Accept values 'queue' or 'topic' (default: queue).

`transport.jms.ReplyDestination` (Optional)
:   The destination where a reply will be posted.

`transport.jms.ContentType` (Optional)
:   Specifies how the transport listener should determine the content type of received messages. This can either be a simple string value, in which case the transport listener assumes that the received messages always have the specified content type, or a set of rules as in the following example:

```
<parameter name="transport.jms.ContentType">
    <rules>
        <jmsProperty>contentType</jmsProperty>
        <jmsProperty>ctype</jmsProperty>
        <default>text/xml</default>
    </rules>
</parameter>
```

    The rules are evaluated in turn until the first matches. The following rule types are defined:

    `jmsProperty`
    :   Extract the content type from the specified message property.

    `bytesMessage` `textMessage`
    :   Match the corresponding message type. The content type is specified as the value of the rule, e.g. `<bytesMessage>binary/octet-stream</bytesMessage>`

    `default`
    :   Defines the default content type. This rule always matches and should therefore be the last rule in the rule set.

    If none of the rules matches, an error is triggered and the message is not processed. The default value for this property corresponds to the following set of rules:


```
<parameter name="transport.jms.ContentType">
    <rules>
        <jmsProperty>Content-Type</jmsProperty>
        <bytesMessage>application/octet-stream</bytesMessage>
        <textMessage>text/plain</textMessage>
    </rules>
</parameter>
```

    This choice preserves compatibility with previous versions of the JMS transport. Note however that `Content-Type` is not a valid JMS property name and will not work with some JMS providers.

`Wrapper` (Optional)
:   The wrapper element for pure text or binary messages. Note that this parameter is actually not JMS specific but recognized by the message builders for `text/plain` and `application/octet-stream` (which are the respective default content types for JMS text and binary messages).

Sample `services.xml`:

```
<service name="echo">
        <transports>
                ....
            <transport>jms</transport>
        </transports>
    ...
    <parameter name="transport.jms.ConnectionFactory" locked="true">myTopicConnectionFactory</parameter>
    <parameter name="transport.jms.Destination" locked="true">dynamicTopics/something.TestTopic</parameter>
</service>
```

### Message context properties for incoming messages

For incoming messages, the transport listener will make the following properties available in the message context:

`TRANSPORT_HEADERS`
:   This property will contain a map with the JMS message properties.

## Transport sender

### Endpoint references

Endpoint references for the JMS transport must have the following form:

```
jms-epr = "jms:/" jms-dest [ "?" param  *( [ "&" param ] ) ]
param = param-name "=" param-value
```

`jms-dest` is the JNDI name of the destination to send the message to. The parameters are defined as follows:

`transport.jms.ConnectionFactory` (Optional)
:   The JMS connection factory definition (from `axis2.xml`) to be used to send messages to the endpoint.

`transport.jms.ContentTypeProperty`
:   The name of the message property to store the content type of messages sent to the endpoint.

All the above listed parameters under the connection factory configuration are applied to the JMS EPR as well, apart from these.

If no connection factory definition is explicitly specified using the `transport.jms.ConnectionFactory` parameter, the JMS sender will check if the transport configuration contains a connection factory compatible with the other settings specified in the endpoint URL (`transport.jms.ConnectionFactoryJNDIName`, `java.naming.factory.initial`, `java.naming.provider.url`, `java.naming.security.principal` and `java.naming.security.credentials`). If a matching configuration is found, the sender will reuse the cached JMS objects related to that configuration. Otherwise it will execute the JNDI lookup and open a new connection. In that case the connection will be closed immediately after sending the message.

### Message context properties for outcoming messages

For outgoing messages, the transport sender will recognize the following message context properties:

`TRANSPORT_HEADERS`
:   The transport expects a map as value for this property. The entries of this map will be set as properties on the outgoing JMS message.

Note that all the properties are optional.

## Content type detection

Incoming requests
:   The content type of the message is determined according to the settings specified in the `transport.jms.ContentType` service parameter.

Outgoing responses
:   If the content type of the request was determined using the value of a message property, the content type of the response will stored in the same message property.

Outgoing requests
:   The content type will be stored in the message property specified by the `transport.jms.ContentTypeProperty` message context property or the `transport.jms.ContentTypeProperty` parameter of the endpoint reference.

Incoming responses
:   The content type will be extracted from the message property that was used to store the content type of the outgoing request.

---

<a id="docs-tcp-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/tcp-transport.html -->

<!-- page_index: 29 -->

# TCP Transport

## Content

- [TCP Transport](#docs-tcp-transport--tcp_transport)
  - [Content](#docs-tcp-transport--content)
  - [Transport listener](#docs-tcp-transport--transport_listener)
    - [Listener configuration](#docs-tcp-transport--listener_configuration)
    - [Endpoint configuration](#docs-tcp-transport--endpoint_configuration)
  - [Transport sender](#docs-tcp-transport--transport_sender)
  - [Examples](#docs-tcp-transport--examples)
    - [Enabling TCP listener at the transport level](#docs-tcp-transport--enabling_tcp_listener_at_the_transport_level)

## Transport listener

### Listener configuration

The TCP transport listener is configured in `axis2.xml` using the following declaration:

```
<transportReceiver name="tcp" class="org.apache.axis2.transport.tcp.TCPTransportListener"/>
```

Depending on how the TCP transport is set up, additional parameters may be required inside the `transportReceiver` element (see next section).

### Endpoint configuration

Endpoints can be configured both at the transport level and at the service level. Each endpoint opens a TCP server socket for listening. TCP requests received on a port that is configured on a service will be pre-dispatched to that service. Packets received by a port that is configured at the transport level need to be dispatched using one of the following mechanisms:

1. Using the namespace URI of the first child element of SOAPBody (SOAPMessageBodyBasedDispatcher).
2. Using WS-Addressing headers (SOAPActionBasedDispatcher).

   Endpoints are configured by adding `parameter` elements to the `transportReceiver` element in `axis2.xml` or to a `service` element in an `services.xml` file. The set of parameters is the same for both scenarios:

   `transport.tcp.port` (required)
   :   The port number over which the TCP server socket should be opened.

   `transport.tcp.hostname` (optional)
   :   The hostname to which the TCP server socket should be bound.

   `transport.tcp.contentType` (optional, defaults to text/xml)
   :   Specifies the content type of the messages received on the endpoint.

   `transport.tcp.backlog` (optional, defaults to 50)
   :   The length of the backlog (queue) supported by the TCP server socket.

## Transport sender

The TCP transport sender can be enabled in `axis2.xml` using the following declaration:

```
<transportSender name="tcp" class="org.apache.axis2.transport.tcp.TCPTransportSender"/>
```

## Examples

### Enabling TCP listener at the transport level

The following declaration in `axis2.xml` initializes a TCP server socket on port 6060 and allows all services (for which TCP is in the list of exposed transports) to receive messages over that port:

```
<transportReceiver name="tcp" class="org.apache.axis2.transport.tcp.TCPTransportListener">
  <parameter name="transport.tcp.port">6060</parameter>
</transportReceiver>
```

For this to work, WS-Addressing must be enabled, and messages sent to port 6060 must have the relevant WS-Addressing headers.

```
<module ref="addressing"/>
```

With the configuration shown above, the TCP transport would generate bindings with the following EPR:

```
tcp://localhost:6060/services/Version?contentType=text/xml
```

Similar EPRs will be generated for services when the transport is configured at service level.

The following example shows a message that can be sent to the Version service over TCP:

```
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:wsa="http://www.w3.org/2005/08/addressing">
    <SOAP-ENV:Header>
        <wsa:MessageID>1234</wsa:MessageID>
        <wsa:To>tcp://localhost:6060/services/Version?contentType=text/xml</wsa:To>
        <wsa:Action>urn:getVersion</wsa:Action>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

Axis2 client API can be used to easily send TCP requests to a remote service. The following code snippet shows how to do that. The TCP transport sender must be enabled in the **axis2.xml** in order for this to work.

```

String url = "tcp://localhost:6060/services/Version?contentType=text/xml";
OMElement payload = ...

ServiceClient serviceClient = new ServiceClient();
Options options = new Options();
EndpointReference targetEPR = new EndpointReference(url);
options.setTo(targetEPR);
serviceClient.setOptions(options);
OMElement response = serviceClient.sendReceive(payload);
```

The transport sender that should be invoked is inferred from the targetEPR (tcp://...). In this case it is TCP and the listener is also TCP. The SOAP message has to be self contained in order to use Addressing. The parameter is of the type OMElement, the XML representation of Axis2.

A TCP URL may contain an optional timeout value, as a query parameter, to indicate how long (in milliseconds) the client should wait for a response. Once this period has expired, the client TCP socket will timeout:

```
tcp://localhost:6060/services/Version?contentType=text/xml&timeout=10000
```

If the Axis2 client API is used to send a request to the above URL, the client socket will timeout after waiting for 10 seconds, for the response.

---

<a id="docs-mail-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/mail-transport.html -->

<!-- page_index: 30 -->

# Introduction

The mail transport allows to send and receive messages using MIME compliant mail messages. The transport sender
transmits outgoing messages using SMTP, while the transport listener connects to one or more mail accounts
and periodically polls these accounts for new incoming messages. The implementation is based on
[JavaMail](http://java.sun.com/products/javamail/) and therefore supports any mail store protocol
for which a JavaMail provider is available.

# Transport listener

## Configuration

```
    <transportReceiver name="mailto" class="org.apache.axis2.transport.mail.MailTransportListener"/>
```

## Endpoint configuration

Endpoints can be configured both at the transport level and at the service level. In order to receive messages using
the mail transport, the listener or the service must be configured with a set of parameters
to access the corresponding mailbox account. If messages from the mail account should be
directly dispatched to a given service, than the parameters must be specified on that service.
If on the other hand messages from that account can't be pre-dispatched to a specific service
(e.g. because the account is used to receive responses to outgoing messages), then the parameters
must be added to the `transportReceiver` element in `axis2.xml`.

All parameters starting with `mail.` are
interpreted as JavaMail environment properties. The most relevant are `mail.<protocol>.host`
and `mail.<protocol>.user`, where `<protocol>` is typically `pop3`
or `imap`. Assuming that Sun's JavaMail implementation is used, the complete list of supported properties for these
two protocols can be found [here](http://java.sun.com/products/javamail/javadocs/com/sun/mail/pop3/package-summary.html)
and [here](http://java.sun.com/products/javamail/javadocs/com/sun/mail/imap/package-summary.html).

In additional to the JavaMail environment properties, the following transport specific service parameters are
used:

| Parameter | Required | Description |
| --- | --- | --- |
| transport.PollInterval | No | The poll interval in seconds. |
| transport.mail.Address | Yes | The address used to calculate the endpoint reference for the service. It is assumed that mails sent to this address will be delivered to the mailbox account configured for the service. Note that the transport has no means to validate this value and an incorrect address will not be detected. |
| mail.*<protocol>*.password | Yes | The password for the mailbox account. |
| transport.mail.Protocol | Yes | The mail store protocol to be used. The value must be protocol identifier recognized by JavaMail. Usual values are `pop3` and `imap`. Note that the SSL variants of these two protocols are not considered as distinct protocols. Rather, SSL is configured using the appropriate JavaMail environment properties. |
| transport.mail.ContentType | No | This parameter allows to override the content type of incoming messages. This parameter is useful if the service can only receive messages of a single content type and the client is known to send incorrect content type information. If this parameter is set, the `Content-Type` MIME header in incoming messages is ignored. |
| transport.mail.ReplyAddress | No | The reply-to address to be used when no From or Reply-To header is present in the request message. |
| transport.mail.Folder | No | The folder to read messages from. Defaults to `INBOX`. |
| transport.mail.PreserveHeaders, transport.mail.RemoveHeaders | No | These two properties control which MIME headers of the received message will be stored in the `TRANSPORT_HEADERS` property of the message context. Both parameters expect a comma separated list of header names as value. `transport.mail.PreserveHeaders` specifies a whitelist of headers to retain, while `transport.mail.RemoveHeaders` specifies a blacklist of headers to remove. Note that the two parameters should not be used simultaneously. |
| transport.mail.ActionAfterProcess | No | Determines what the transport should do with the message after successful processing. Possible values are `MOVE` and `DELETE`. The default value is `DELETE`. |
| transport.mail.ActionAfterFailure | No | Determines what the transport should do with the message if processing fails. Possible values are `MOVE` and `DELETE`. The default value is `DELETE`. [FIXME: we should reconsider this; it is dangerous!] |
| transport.mail.MoveAfterProcess | Conditional | Specifies the destination folder if `transport.mail.ActionAfterProcess` is `MOVE`. |
| transport.mail.MoveAfterFailure | Conditional | Specifies the destination folder if `transport.mail.ActionAfterFailure` is `MOVE`. |
| transport.mail.MaxRetryCount | No | The number of connection attempts. When the maximum number of retries is exceeded, a new poll is scheduled after the normal poll interval. The default value is 0, i.e. connection failures are simply ignored. |
| transport.mail.ReconnectTimeout | No | The interval between two connection attempts if the first failed. The default value is 0, i.e. a new connection is attempted immediately. [FIXME: either it is not implemented as intended or the name of the property is misleading; it is not a timeout, but an interval] |

## Content extraction

Content is extracted from incoming mails using the following rules:

1. If the content type of the message is not `multipart/mixed`, the message is extracted
   from the body of the message.
2. If the content type of the message is `multipart/mixed`, the listener will attempt to
   find a MIME part with a content type different from `text/plain` and for which a
   message builder is registered. If a matching part is found, the message will be extracted
   from that part. Otherwise, the listener will extract the message from
   the last `text/plain` part if a message builder is registered for that content type.
   Finally, if no message builder is registered for any of the content types appearing in the multipart
   message, an error is triggered.

Note that these rules only apply if the content type has not been overridden using the
`transport.mail.ContentType` property. If this property is set, the message will always be
extracted from the body of the message and support for `multipart/mixed` is disabled.

In all cases the transport listener will use the corresponding message builder registered in the
Axis configuration to build the SOAP infoset from the message.

The special rules for `multipart/mixed` are designed to enable the following use cases:

- Allow humans to send messages to a Web service using a standard mail client. The user
  can do so by adding the message as attachment to the mail. Note that this only works
  if the mail client correctly sets the `Content-Type` header on the attachment.
  This works best for SOAP 1.1 messages: when attaching a file with suffix `.xml`,
  most mail clients will set the content type to `text/xml`, exactly as required
  for SOAP 1.1.
- Allow clients to send a human readable message together with the actual message.
  This is useful if the message may be read by a human before being processed.

Note that these rules don't interfere with the support for SOAP with Attachments, because
SwA uses `multipart/related`.

# Transport sender

## Configuration

```
    <transportSender name="mailto" class="org.apache.synapse.transport.mail.MailTransportSender">
        <parameter name="mail.smtp.host">smtp.gmail.com</parameter>
        <parameter name="mail.smtp.port">587</parameter>
        <parameter name="mail.smtp.starttls.enable">true</parameter>
        <parameter name="mail.smtp.auth">true</parameter>
        <parameter name="mail.smtp.user">synapse.demo.0</parameter>
        <parameter name="mail.smtp.password">mailpassword</parameter>
        <parameter name="mail.smtp.from">synapse.demo.0@gmail.com</parameter>
    </transportSender>
```

---

<a id="docs-udp-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/udp-transport.html -->

<!-- page_index: 31 -->

# UDP Transport

## Content

- [UDP Transport](#docs-udp-transport--udp_transport)
  - [Content](#docs-udp-transport--content)
  - [Transport listener](#docs-udp-transport--transport_listener)
    - [Listener configuration](#docs-udp-transport--listener_configuration)
    - [Endpoint configuration](#docs-udp-transport--endpoint_configuration)
  - [Transport sender](#docs-udp-transport--transport_sender)
  - [Examples](#docs-udp-transport--examples)
    - [Enabling SOAP over UDP at the transport level](#docs-udp-transport--enabling_soap_over_udp_at_the_transport_level)

## Transport listener

### Listener configuration

The UDP transport listener is configured in `axis2.xml` using the following declaration:

```
<transportReceiver name="udp" class="org.apache.axis2.transport.udp.UDPListener"/>
```

Depending on how the UDP transport is set up, additional parameters may be required inside the `transportReceiver` element (see next section).

### Endpoint configuration

Endpoints can be configured both at the transport level and at the service level. Each endpoint opens a local UDP port for listening. UDP packets received on a port that is configured on a service will be pre-dispatched to that service. Packets received by a port that is configured at the transport level need to be dispatched using WS-Addressing or some other mechanism implemented by a dispatcher configured in Axis2.

Endpoints are configured by adding `parameter` elements to the `transportReceiver` element in `axis2.xml` or to a `service` element in an `services.xml` file. The set of parameters is the same for both scenarios:

`transport.udp.port` (required)
:   Specifies the UDP port to bind to.

`transport.udp.contentType` (required)
:   Specifies the content type of the messages received on the endpoint. This parameter is necessary because in contrast to HTTP, the content type information is not part of the information exchanged on the wire.

`transport.udp.maxPacketSize` (optional, defaults to 1024)
:   The maximum UDP packet size.

## Transport sender

The UDP transport sender can be enabled in `axis2.xml` using the following declaration:

```
<transportSender name="udp" class="org.apache.axis2.transport.udp.UDPSender"/>
```

## Examples

### Enabling SOAP over UDP at the transport level

The following declaration in `axis2.xml` enables SOAP over UDP on port 3333 and allows all services (for which UDP is in the list of exposed transports) to receive messages over that port:

```
<transportReceiver name="udp" class="org.apache.axis2.transport.udp.UDPListener">
  <parameter name="transport.udp.port">3333</parameter>
  <parameter name="transport.udp.contentType">text/xml</parameter>
  <parameter name="transport.udp.maxPacketSize">4096</parameter>
</transportReceiver>
```

For this to work, WS-Addressing must be enabled, and messages sent to port 3333 must have the relevant WS-Addressing headers.

```
<module ref="addressing"/>
```

With the configuration shown above, the UDP transport would generate bindings with the following EPR:

```
udp://localhost:3333/axis2/services/Version?contentType=text/xml
```

The following example shows a message that can be sent to the Version service over UDP:

```
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:wsa="http://www.w3.org/2005/08/addressing">
    <SOAP-ENV:Header>
        <wsa:MessageID>1234</wsa:MessageID>
        <wsa:To>udp://localhost:3333/axis2/services/Version?contentType=text/xml</wsa:To>
        <wsa:Action>urn:getVersion</wsa:Action>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

On most Linux/Unix systems (including Mac OS X), the `nc` utility is available to send UDP messages and can be used to test the transport. To do this, save the message into `test-message.xml` and execute the following command:

```
nc -u 127.0.0.1 3333 < test-message.xml
```

---

<a id="docs-xmpp-transport"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/xmpp-transport.html -->

<!-- page_index: 32 -->

# Introduction

The XMPP transport allows to send and receive chat messages.

# Transport listener

## Configuration

```
<transportReceiver name="xmpp" class="org.apache.axis2.transport.xmpp.XMPPListener">
   <!-- Account details for google talk -->
   <parameter name="GoogleServer">
      <parameter name="transport.xmpp.ServerUrl">talk.google.com</parameter>
      <parameter name="transport.xmpp.ServerAccountUserName">axis2.xmpp.account1</parameter>
      <parameter name="transport.xmpp.ServerAccountPassword">apacheaxis2</parameter>
      <parameter name="transport.xmpp.ServerType">transport.xmpp.ServerType.GoogleTalk</parameter>
   </parameter>
</transportReceiver>
```

## Transport Specific Parameters

Following transport specific service parameters are used:

| Parameter | Required | Description |
| --- | --- | --- |
| transport.xmpp.ServerUrl | Yes | The server url of the XMPP server |
| transport.xmpp.ServerAccountUserName | Yes | The user name of the XMPP account |
| transport.xmpp.ServerAccountPassword | Yes | The password for the XMPP account. |
| transport.xmpp.ServerType | Yes | The type of XMPP server |

# Transport sender

## Configuration

```
<transportSender name="xmpp" class="org.apache.axis2.transport.xmpp.XMPPSender">
</transportSender>
```

---

<a id="docs-transport_howto"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/transport_howto.html -->

<!-- page_index: 33 -->

# How to Write Your Own Axis2 Transport

## Prologue

To stop you from re-inventing the wheel, before we get started, I will
quickly list the transports that are already supported in Axis2 with a small
description.

- **HTTP** - In the HTTP transport, the transport Listener is either a
  Servlet or a Simple HTTP server provided by Axis2. The transport Sender
  uses sockets to connect and send the SOAP message. Currently we have the
  Apache Httpcomponents based HTTP Transport sender as the default
  transport.
- **TCP** - This is the most simple transport, but needs Addressing
  support to be functional.

To understand the rest of this document you will need some understanding
of the architecture of Axis2. If you are not familiar with the Axis2
architecture, please go through the [Axis2 Architecture Guide](#docs-axis2architectureguide) before you
read any further.

## Introduction

Broadly speaking, a transport inside Axis2 can be classified as a way of
getting messages that arrive though some channel into the Axis2 engine. The
core of Axis2 is transport independent. All data that is transport specific
is stripped out of the incoming message and inserted into the MessageContext.
In the outgoing message, all transport specific information, like headers, are added and sent.

To write your own transport, you will primarily need to write two classes:
one is the TransportSender and the other is the TransportReceiver. To
register a transport with Axis2 you will need to put entries corresponding
to these two classes in the axis2.xml file. I will take you through the
process of adding the entries in the relevant sections.

## Transport Receiver

Any message that is coming into Axis2 needs to go through a transport
receiver. All information about how the message is received at the Axis2
server from the wire (or via an e-mail) is isolated inside the transport
receiver. It extracts the data that is coming on the wire and transforms it
into a state that the Axis2 server understands.

So now that we have some background information about how transports work
inside Axis2, without further delay, lets dive into some coding and start
building our own transport.

To get things stared, you will first need to extend from the
org.apache.Axis2.transport.TransportListener class and write your own
transport listener. To create an engine to process the MessageContext, we
need a configuration context. The following code fragment will do this. This
should ideally be only done once for the lifetime of the Transport
receiver.

```
try {
        //Create a factory 
        ConfigurationContextFactory factory = new ConfigurationContextFactory();
        //Use the factory and an Axis2 repository to create a new Configuration Context
        configurationContext = ConfigurationContextFactory.createConfigurationContextFromFileSystem(repository_directory, 
axis2xmllocation);
} catch (Exception e) {
        log.info(e.getMessage());
}
```

Now we need some kind of a Listener to listen to the requests that come
in. You need to implement this according to the transport that you are trying
to build. After a message is received at the Receiver, you can use the
following code to process the request and then forward the message context to
the engine using the engine.receive(msgContext) method. (The following code
is extracted from the MailListener as an example)

```
AxisEngine engine = new AxisEngine(configurationContext);
MessageContext msgContext = null;

// create and initialize a message context
try {
        TransportInDescription transportIn =
                reg.getAxisConfiguration().getTransportIn(new QName(Constants.TRANSPORT_NAME));
        TransportOutDescription transportOut =
                reg.getAxisConfiguration().getTransportOut(new QName(Constants.TRANSPORT_NAME));
        if (transportIn != null && transportOut != null) {
                //create Message Context
                
                msgContext = new MessageContext(configurationContext, transportIn, transportOut);
                msgContext.setServerSide(true);
                msgContext.setProperty(MailSrvConstants.CONTENT_TYPE, message.getContentType());
                msgContext.setProperty(MessageContext.CHARACTER_SET_ENCODING, message.getEncoding());

                String soapAction = message.getSOAPActionHeader();
                msgContext.setWSAAction(soapAction);
                msgContext.setSoapAction(soapAction);

                // Here we are trying to set the reply to if it is present in the transport information.
                msgContext.setReplyTo(new EndpointReference(message.getReplyTo());

                //Create the SOAP Message -- This code in from the mail transport and will change depending
                //on how the data is handled in each transport.
                ByteArrayInputStream bais = new ByteArrayInputStream(message.getContent().toString().getBytes());
                XMLStreamReader reader = XMLInputFactory.newInstance().createXMLStreamReader(bais);

                String soapNamespaceURI = "";
                if(message.getContentType().indexOf(SOAP12Constants.SOAP_12_CONTENT_TYPE) > -1){
                        soapNamespaceURI = SOAP12Constants.SOAP_ENVELOPE_NAMESPACE_URI;
                }else if(message.getContentType().indexOf(SOAP11Constants.SOAP_11_CONTENT_TYPE) > -1){
                        soapNamespaceURI = SOAP11Constants.SOAP_ENVELOPE_NAMESPACE_URI;
                }

                StAXBuilder builder = new StAXSOAPModelBuilder(reader, soapNamespaceURI);

                SOAPEnvelope envelope = (SOAPEnvelope) builder.getDocumentElement();
                msgContext.setEnvelope(envelope);
                engine.receive(msgContext);
        } else {
                throw new AxisFault(Messages.getMessage("unknownTransport",Constants.TRANSPORT_NAME));
        }

} catch (Exception e) {
        try {
                if (msgContext != null) {
                        MessageContext faultContext = engine.createFaultMessageContext(msgContext, e);
                        engine.sendFault(faultContext);
                } else {
                        log.error(e);
                }
        } catch (AxisFault e1) {
                log.error(e);
        }
}
```

Now that we have the coding in place, we need to let Axis2 know about our
new transport receiver. We do this by adding an entry into the axis2.xml
file. If you need to pass any properties for the transport to operate, it can
also be done through the axis2.xml file.

```
   <transportReceiver name="TRANSPORT_NAME" class="org.apache.Axis2.transport.TRANSPORT_NAME.TRANSPORT_LISTNER_CLASS">
        <parameter name="PROPERTY_NAME">PROPERTY_VALUE</parameter>
        <parameter name="PROPERTY_NAME_2">PROPERTY_VALUE_2</parameter>
  </transportReceiver>
  
```

By using a code fragment like
`Utils.getParameterValue(transportOut.getParameter(MailSrvConstants.SMTP_USER))`
we can extract the parameters that we inserted into the axis2.xml file.

As you can see, getting a new transport receiver up and running is a task
that requires very little effort.

## Transport Sender

Any message that is to be sent out of Axis2, is sent through the Transport
Sender. The Transport Sender needs to be extended from the
org.apache.Axis2.transport.AbstractTransportSender class.

The following bit of code from the abstract transport sender will call the
Transport Sender that you wrote.

```
// If an EPR is present then the message is going on a different channel.
if (epr != null) {
        out = openTheConnection(epr, msgContext);
        OutputStream newOut = startSendWithToAddress(msgContext, out);
        if (newOut != null) {
                out = newOut;
        }
        writeMessage(msgContext, out);
        finalizeSendWithToAddress(msgContext, out);
        } else {
        out = (OutputStream) msgContext.getProperty(MessageContext.TRANSPORT_OUT);
        if (out != null) {
                startSendWithOutputStreamFromIncomingConnection(msgContext, out);
                writeMessage(msgContext, out);
                finalizeSendWithOutputStreamFromIncomingConnection(msgContext, out);
        } else {
                throw new AxisFault(
                        "Both the TO and Property MessageContext.TRANSPORT_WRITER is Null, No way to send response.");
        }
}
```

Therefore, depending on whether your transport is using the same channel
to send the response or using a different channel, you will need to implement
a sub-set of the methods from the abstract class.

After implementing the necessary methods, you can let Axis2 know about
your new transport sender by adding an entry to the axis2.xml file, like you
did for the TransportReceiver.

```
  <transportSender name="TRANSPORT_NAME" class="org.apache.Axis2.transport.TRANSPORT_NAME.TRANSPORT_SENDER_CLASS">
        <parameter name="PROPERTY_NAME">PROPERTY_VALUE</parameter>
        <parameter name="PROPERTY_NAME_2">PROPERTY_VALUE_2</parameter>
  </transportSender>
  
```

Have a look at
org.apache.axis2.transport.http.impl.httpclient5.HTTPClient5TransportSender which is used to
send HTTP responses.

Once we have written our transport receiver and our transport sender, and
inserted the required entries into the axis2.xml file, we are done. It is as
simple as that!

---

<a id="docs-ws_policy"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/WS_policy.html -->

<!-- page_index: 34 -->

# Web Services Policy Support In Apache Axis2

This document gives you an introduction to the role of Web
services policy in Apache Axis2.

Send your feedback to: [java-dev@axis.apache.org](mailto:java-dev@axis.apache.org?subject=[Axis2]).
(Subscription details are available on the [Axis2 site](#mail-lists).)
Kindly prefix every email subject with [Axis2].

## Content

- [What is Web Services (WS) Policy?](#docs-ws_policy--what)
- [Client Side WS-Policy Support](#docs-ws_policy--client)
- [Server Side WS-Policy Support](#docs-ws_policy--server)
- [Resources](#docs-ws_policy--resources)

## What is Web Services (WS) Policy?

To consume non trivial web services you must fully understand
its XML contract (WSDL) along with any other additional
requirements, capabilities, or preferences that translate to the
configuration of the service and essentially becomes the policies
of the service.

WS Policy framework provides a way to express the policies of a
service in a machine-readable way. A Web services infrastructure
can be enhanced to understand and enforce policies at runtime. For
instance, a service author might write a policy requiring a digital
signature and encryption, while service consumers can use the
policy information to reason out whether they can adhere to this
policy information to use the service.

Furthermore, Web service infrastructure can be enhanced to
enforce those requirements without requiring the service author to
write even a single line of code.

## Client Side WS-Policy Support

This release **fully supports WS Policy at
client-side**. It means that when you codegen a stub against
a WSLD which contains policies, the stub will contain the
capability to engage the required modules with the appropriate
configurations, plus it will generate additional methods in the
stub where the user can set certain properties. For instance, if
there is a security policy attached to a binding, the generated
stub will engage the security module for that service with the
appropriate security configurations with some addtional methods
that the user can use to set properties in the generated stub.

### How it works:

#### Phase 1: At PolicyEvaluator

The Codegen engine runs a few of its registered extensions
before it generates the stub. When the PolicyEvalutor (which is a
registered Codegen extension) is initialized, it populates a
registry of QNames of supported policy assertions to
PolicyExtensions.

For instance, module Foo might have a mapping of assertion
{http://test.com/foo, foo} which means any assertion that has this
name will be processed by this module. The Foo module might
implement the ModulePolicyExtension interface through which the
PolicyExtension object can be obtained.

A **PolicyExtension** is the access point for a
module to add any additional methods to the stub. For instance a
Reliable Messaging module can add startSequence() and endSequence()
methods to the stub, that the user must call to start and end an RM
sequence.

Then at the engagement of the PolicyEvaluator, the effective
policy of each message of every operation is calculated based on
policy information declared in the WSDL document. Here we assume
that the effective policy of an operation contains a single
alternative (**Multiple policy alternatives are not
supported**). Then we split that policy as follows into few
other policies such that, each policy will contain assertions that
can be processed by a single module.

```

  <wsp:Policy>         <wsp:Policy>       <wsp:Policy>        
    <a:Foo/>             <a:Foo/>           <b:Foo/>               
    <b:Bar/>      =>                               </wsp:Policy>       
                                   </wsp:Policy>
  </wsp:Policy>
```

Then each policy is given the appropriate PolicyExtension with
an org.w3c.Element type object to which the module can append any
other elements/attributes it wishes. Those attributes/elements
should resolve to meaningful stub functions through the Custom
PolicyExtensionTemplate.xsl at a latter point of time.

For instance, depending on the policy, the Security module can
append <username>, <passwd> elements to the given
element as children, which are later resolved into setUsername(..), setPasswd(..), functions of the stub. This way a module can include
additional methods to the stub that can be used to get specific
propreties from the user. These methods store any user input in the
ServiceClient properties
(ServiceClient.getOptions().putProperty(...)) which can later be
accessed by the module.

#### Phase 2: At AxisServiceBasedMultiLanguageClientEmitter

Further, policies (based on the WSDL) at appropriate levels
(service level, operation level) are stored as policy strings in
the stub. If there are a few policies at a given level, they are
merged together and represented as a single policy in the stub. Few
more generic methods are also added to the stub which are used to
evaluate and process the policies at runtime.

#### Phase 3: Runtime

When a new stub object is created, the policy strings in the
stub are converted into policy objects and are set in the
AxisDescription hierarchy that is used in the stub. In other words, any policy information available in the WSDL will be preserved in
the AxisService object that is used in the stub.

Then based on its policy, each AxisDescription is engaged to a
set of modules. Modules can do a prior calculation of
configurations if needed at the engagement.

When the stub method is invoked, those modules which are engaged
to that AxisDescription, access the policy for that operation via
the AxisDescription object. It can get the other required
information from the MessageContext, which is stored by stub
methods that the module has added to the stub earlier, through the
ModulePolicyExtension implementation. The modules are required to
load their configurations according to the effective policy, which
is set at AxisDescription, and the properties they get via
MessageContext.

## Server Side WS-Policy Support

In this current release, the Apache Axis2 framework uses the
WS-Commons/Neethi framework to manipulate policy documents. All its
description builders store the policy information included in
description documents (services.xml, axis2.xml, .. etc) in the
appropriate description classes. This information is available at
both deployment and run time via these description classes.

When generating WSDL dynamically for each service, policy
information in the description classes is included. For instance, if you declare a policy in axis2.xml, then that policy is reflected
in the service elements of the WSDL of every service. If a policy
is declared in a services.xml, it is shown in the service element
of WSDL for that particular service.

Further, when a service is deployed, an arbitary policy
alternative is selected and set for each AxisOperation and
AxisMessages of the AxisService. If the selected Policy alternative
cannot be supported by any modules that are capable of processing
the selective alternative, then the service is considered as a
faulty service. Else, the set of modules is engaged at appropriate
levels to support the requirments and capabilities that are defined
in the Policies associated with the AxisDescription.

It is evident that there is some work left to make Apache Axis2
a fully fledged ws-policy supported Web service infrastructure.
However, it is encouraging to note that we've taken the first steps
towards this goal. We appreciate any suggestions, patches, etc., you send us in this regard. Keep on contributing!

## Resources

- Apache Neethi (WS Policy Implementation) official site-
  [Home Page](http://ws.apache.org/commons/neethi/index.html)
- Sanka Samaranayake, March 2006. [Web services Policy - Why, What & How](http://wso2.org/library/23)
- [WS-commons/policy GitHub](https://github.com/apache/ws-neethi)
- [Web Services Policy Framework (WS-Policy)](http://specs.xmlsoap.org/ws/2004/09/policy/ws-policy.pdf)

---

<a id="docs-rest-ws"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/rest-ws.html -->

<!-- page_index: 35 -->

# RESTful Web Services Support

This document presents an introduction on REST and REST with HTTP POST and
GET.

## Content

- [Introduction](#docs-rest-ws--intro)
- [Doing REST Web Services with HTTP POST](#docs-rest-ws--rest_with_post)
  - [Sample REST - HTTP POST Client](#docs-rest-ws--sample)
- [Access a REST Web Service via HTTP GET](#docs-rest-ws--rest_with_get)

## Introduction

WSDL 2.0 HTTP Binding defines a way to implement REST (Representational
State Transfer) with Web services. Axis2 implements the most defined HTTP
binding specification. REST Web services are a reduced subset of the usual
Web service stack.

The Axis2 REST implementation assumes the following properties:

1. REST Web services are Synchronous and Request Response in nature.
2. When REST Web services are accessed via GET, the service and the
   operations are identified based on the URL. The parameters are assumed as
   parameters of the Web service. In this case, the GET based REST Web
   services support only simple types as arguments and it should adhere to
   the [IRI
   style](http://www.w3.org/TR/2006/CR-wsdl20-adjuncts-20060327/#_operation_iri_style).
3. POST based Web services do not need a SOAP Envelope or a SOAP Body.
   REST Web Services do not have Headers and the payload is sent
   directly.

Axis2 can be configured as a REST Container and can be used to send and
receive RESTful Web service requests and responses. REST Web services can be
accessed using HTTP GET and POST.

## REST Web Services with HTTP POST

If REST is enabled, the Axis2 server will act as both a REST endpoint and
a SOAP endpoint. When a message is received, if the content type is text/xml
and if the SOAPAction Header is missing, then the message is treated as a
RESTful Message, if not it is treated as a usual SOAP Message.

On sending a message, whether the message is RESTful or not, can be
decided from the client API.
Set a property in the client API.

```
...
Options options = new Options();
options.setProperty(Constants.Configuration.ENABLE_REST, Constants.VALUE_TRUE);
...
```

### Sample REST - HTTP POST Client

There is an example named, userguide.clients.RESTClient.java found in
AXIS2\_HOME/samples/userguide/src/userguide/clients which demonstrates the
usage of the above. It uses the "echo" operation of the
`userguide.example1.MyService` of the
AXIS2\_HOME/samples/userguide/src/userguide/example1.

The class source will be as follows:

```
public class RESTClient {

    private static String toEpr = "http://localhost:8080/axis2/services/MyService";
    
    public static void main(String[] args) throws AxisFault {

        Options options = new Options();
        options.setTo(new EndpointReference(toEpr));
        options.setTransportInProtocol(Constants.TRANSPORT_HTTP);
        
        options.setProperty(Constants.Configuration.ENABLE_REST, Constants.VALUE_TRUE);

        ServiceClient sender = new ServiceClient();
        sender.engageModule(Constants.MODULE_ADDRESSING);
        sender.setOptions(options);
        OMElement result = sender.sendReceive(getPayload());

        try {
            XMLStreamWriter writer = XMLOutputFactory.newInstance()
                    .createXMLStreamWriter(System.out);
            result.serialize(writer);
            writer.flush();
        } catch (XMLStreamException e) {
            e.printStackTrace();
        } catch (FactoryConfigurationError e) {
            e.printStackTrace();
        }
    }

    private static OMElement getPayload() {
        OMFactory fac = OMAbstractFactory.getOMFactory();
        OMNamespace omNs = fac.createOMNamespace(
                "http://example1.org/example1", "example1");
        OMElement method = fac.createOMElement("echo", omNs);
        OMElement value = fac.createOMElement("Text", omNs);
        value.addChild(fac.createOMText(value, "Axis2 Echo String "));
        method.addChild(value);

        return method;
    }
}
```

## Access a REST Web Service via HTTP GET

Axis2 allows users to access Web services that have simple type parameters
via HTTP GET. For example, the following URL requests the Version Service via
HTTP GET. However, the Web service arriving via GET assumes REST. Other
parameters are converted into XML and put into the SOAP body.

```
http://127.0.0.1:8080/axis2/services/Version/getVersion
```

The result can be shown in the browser as follows:

![](assets/images/http-get-ws_421b308a1067d433.jpg)

For example, the following request,

```
http://127.0.0.1:8080/axis2/services/Version/getVersion
```

will be converted into the following SOAP message for processing by
Axis2.

```
 
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Body>   
          <axis2:getVersion xmlns:axis2="http://ws.apache.org/goGetWithREST" />
      </soapenv:Body>
   </soapenv:Envelope>
    
```

## Resources

How I Explained REST to My Wife, By Ryan Tomayko- <http://naeblis.cx/articles/2004/12/12/rest-to-my-wife>

Building Web Services the REST Way, By Roger L. Costello- <http://www.xfront.com/REST-Web-Services.html>

Resource-oriented vs. activity-oriented Web services, By James Snell- <http://www-128.ibm.com/developerworks/webservices/library/ws-restvsoap/>

---

<a id="docs-json_support"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/json_support.html -->

<!-- page_index: 36 -->

# JSON Support in Axis2

# Introduction

Update: This documentation represents early forms of JSON
conventions, Badgerfish and Mapped. GSON support was added a few
years later. Moshi support is now included as an alternative to
GSON. For users of JSON seeking modern features, see the [JSON Support Guide.](#docs-json_support_gson). For users of
JSON and Spring Boot 3, see the sample application in the [JSON and Spring Boot 3 User's Guide.](#docs-json-springboot-userguide)

This document explains the JSON support implementation in Axis2.
It includes an introduction to JSON, an outline as to why JSON
support is useful to Axis2 and how it should be used. This document
also provides details on test cases and samples.

# What is JSON?

[JSON](http://www.json.org/) (Java Script Object
Notation) is another data exchangeable format like XML, but more
lightweight and easily readable. It is based on a subset of the
JavaScript language. Therefore, JavaScript can understand JSON, and
it can make JavaScript objects by using JSON strings. JSON is based
on key-value pairs and it uses colons to separate keys and values.
JSON doesn't use end tags, and it uses braces (curly brackets) to
enclose JSON Objects.

e.g. <root><test>json
object</test></root> ==
{{json object}}

When it comes to converting XML to JSON and vice versa, there
are two major conventions, one named "[Badgerfish](http://www.sklar.com/badgerfish/)" and the other, Mapped. The main difference
between these two conventions exists in the way they map XML
namespaces into JSON.

e.g. <xsl:root
xmlns:xsl="http://foo.com"><data>my json
string</data></xsl:root>

This XML string can be converted into JSON as follows.

**Using Badgerfish**

{"xsl:root":{"@xmlns":{"xsl":"http://foo.com"},"data":{"$":"my
json string"}}}

**Using Mapped**

If we use the namespace mapping as http://foo.com -> foo

{"foo.root":{"data":"my json string"}}

# Why JSON Support for Axis2?

[Apache Axis2](#index) is a Web
services stack that delivers incoming messages into target
applications. In most cases, these messages are SOAP messages. In
addition, it is also possible to send REST messages through Axis2.
Both types of messages use XML as their data exchangeable format.
So if we can use XML as a format, why use JSON as another
format?

There are many advantages of implementing JSON support in Axis2.
Mainly, it helps the JavaScript users (services and clients written
in JavaScript) to deal with Axis2. When the service or the client
is in JavaScript, it can use the JSON string and directly build
JavaScript objects to retrieve information, without having to build
the object model (OMElement in Axis2). Also, JavaScript services
can return the response through Axis2, just as a JSON string can be
shipped in a JSONDataSource.

Other than for that, there are some extra advantages of using
JSON in comparison to XML. Although the conversation
XML or JSON? is still a hot topic, many people accept the fact that JSON can be passed and built more
easily by machines than XML.

# How to use JSON in Axis2

At the moment JSON doesn't have a standard and unique content
type. `application/json` (this is
the content type which is approved in the [JSON RFC](http://www.ietf.org/rfc/rfc4627.txt)), `text/javascript` and
`text/json` are some of the commonly
used content types for JSON. Fortunately, in Axis2, the user
has the freedom of specifying the content type to use.

## Configuring axis2.xml

First of all, you need to map the appropriate message formatters and builders to the
content type you are using in the `axis2.xml` file. This applies both the to
client side and the server side.

E.g., if you are using the
Mapped convention with the content
type `application/json`, add the following declaration:

```

    <messageFormatters>        
        <messageFormatter contentType="application/json"
                          class="org.apache.axis2.json.JSONMessageFormatter"/>
        <!-- more message formatters -->
    </messageFormatters>   

    <messageBuilders>
        <messageBuilder contentType="application/json"
                        class="org.apache.axis2.json.JSONOMBuilder"/>
        <!-- more message builders -->
    </messageBuilders>
```

If you are using the
Badgerfish convention with the
content type `text/javascript`, add:

```

    <messageFormatters>        
        <messageFormatter contentType="text/javascript"
                          class="org.apache.axis2.json.JSONBadgerfishMessageFormatter">
        <!-- more message formatters -->
    </messageFormatters> 

    <messageBuilders>
        <messageBuilder contentType="text/javascript"
                        class="org.apache.axis2.json.JSONBadgerfishOMBuilder"/>
        <!-- more message builders -->
    </messageBuilders>
```

## Client-side configuration

On the client side, make the ConfigurationContext by reading the
axis2.xml in which the correct mappings are given.

e.g.

```

        File configFile = new File("test-resources/axis2.xml");
        configurationContext = ConfigurationContextFactory
                        .createConfigurationContextFromFileSystem(null, configFile.getAbsolutePath());
        ..........        
        ServiceClient sender = new ServiceClient(configurationContext, null);
```

Set the *MESSAGE\_TYPE* option with exactly the same content
type you used in the axis2.xml.

e.g. If you use the content type
application/json,

```

        Options options = new Options();        
        options.setProperty(Constants.Configuration.MESSAGE_TYPE, "application/json");
        //more options
        //...................        

        ServiceClient sender = new ServiceClient(configurationContext, null);        
        sender.setOptions(options);
```

If you are sending a request to a remote service, you have to
know the exact JSON content type that is used by that service, and
you have to use that content type in your client as well.

HTTP POST is used as the default method to send JSON messages
through Axis2, if the HTTP method is not explicitly set by the
user. But if you want to send JSON in HTTP GET method as a
parameter, you can do that by just setting an option on the client
side.

e.g.

`options.setProperty(Constants.Configuration.HTTP_METHOD, Constants.Configuration.HTTP_METHOD_GET);`

Here, the Axis2 receiving side (JSONOMBuilder) builds the
OMElement by reading the JSON string which is sent as a parameter.
The request can be made even through the browser.

e.g. Sample JSON request through HTTP GET. The JSON message is
encoded and sent.

`GET
/axis2/services/EchoXMLService/echoOM?query=%7B%22echoOM%22:%7B%22data%22:%5B%22my%20json%20string%22,%22my%20second%20json%20string%22%5D%7D%7D
HTTP/1.1`

## Server-side configuration

Since Badgerfish defines a 1-to-1 transformation between JSON and XML, no additional configuration
is required on the server side if that convention is used. Any service deployed into Axis2 will work
out of the box.

On the other hand, if the Mapped JSON convention is used, then Axis2 needs to know the mappings
between XML namespaces and JSON "namespaces" in order to translate messages from JSON
into XML representations and vice-versa. To use the Mapped convention with a service deployed into Axis2, add a `xmlToJsonNamespaceMap` property with these mappings to the `services.xml` file for that service, as
shown in the following example:

```

<service name="...">
    ...
    <parameter name="xmlToJsonNamespaceMap">
        <mappings>
            <mapping xmlNamespace="http://example.org/foo" jsonNamespace=""/>
            <mapping xmlNamespace="http://example.org/bar" jsonNamespace="bar"/>
        </mappings>
    </parameter>
    ...
</service>
```

# How the JSON implementation works - Architecture

## Introduction

The Axis2 architecture is based on the assumption that any message flowing through
the Axis2 runtime is representable as a SOAP infoset, i.e. as XML wrapped in a SOAP
envelope. Conceptually, the two message builders `JSONOMBuilder` and
`JSONBadgerfishOMBuilder` convert incoming messages from JSON to XML and
the two message formatters `JSONMessageFormatter` and `JSONBadgerfishMessageFormatter`
convert outgoing messages from XML to JSON. Axis2 doesn't implement its own JSON parser and serializer, and
instead relies on [Jettison](http://jettison.codehaus.org/) to do the JSON<->XML conversions.

On the server side the XML for an incoming
message is typically converted to Java objects by a databinding (such as ADB or JAX-WS)
before the invocation of the service implementation. In the same way, the Java object returned by the
service implementation is converted to XML. In the case we are interested in, that XML is then converted
by the message formatters to JSON. The usage of an intermediate XML representation is the reason why
JSON can be enabled on any service deployed in Axis2.

It is important to note that the explanation given in the previous two paragraphs is only valid from
a conceptual point of view. The actual processing model is more complicated. In the next two sections
we will explain in detail how Axis2 processes incoming and outgoind JSON messages.

## Processing of incoming JSON messages

Axis2 relies on [Apache Axiom](http://ws.apache.org/axiom/) as its XML object model. Although
Axiom has a DOM like API, it also has several advanced features that enable Axis2 to avoid
building a complete object model representation of the XML message. This is important for performance
reasons and distinguishes Axis2 from previous generation SOAP stacks. To leverage these features, the
JSON message builders create a SOAP envelope the body of which contains a single `OMSourcedElement`.

An `OMSourcedElement` is a special kind of `OMElement` that wraps an arbitrary
Java object that can be converted to XML in a well defined way. More precisely, the Java object as well as the logic
to convert the object to XML are encapsulated in an `OMDataSource` instance and it is that
`OMDataSource` instance that is used to create the `OMSourcedElement`.
For JSON, the `OMDataSource` implementation is `JSONDataSource` or `JSONBadgerfishDataSource`, depending on the convention being used. The base class (`AbstractJSONDataSource`) of these two classes
actually contains the code that invokes Jettison to perform the JSON to XML conversion.

An `OMSourcedElement` still behaves like a normal `OMElement`. In particular, if the
element is accessed using DOM like methods, then Axiom will convert the data encapsulated by
the `OMDataSource` on the fly to an object model representation. This process is called *expansion* of the
`OMSourcedElement`. However, the `OMDataSource` API is designed such that the conversion to
XML is always done using a streaming API: either the `OMDataSource` produces an `XMLStreamReader`
instance from which the XML representation can be read (this is the case for JSON and the `XMLStreamReader` implementation
is actually provided by Jettison) or it serializes the XML representation to an `XMLStreamWriter`.
Because of this, expansion of the `OMSourcedElement` is often not necessary, so that the overhead of
creating an object model representation can usually be avoided. E.g. a databinding will typically consume the message by requesting an
`XMLStreamReader` for the element in the SOAP body, and this doesn't require expansion of the
`OMSourcedElement`. In this case, the databinding pulls the XML data almost directly from the
underlying Jettison `XMLStreamReader` and no additional Axiom objects are created.

Actually here again, things are slightly more complicated because in order to dispatch to the right
operation, Axis2 needs to determine the name of the element in the body. Since the name is not known
in advance, that operation requires expansion of the `OMSourcedElement`. However, at this point
none of the children of the `OMSourcedElement` will be built. Fortunately the databindings
generally request the `XMLStreamReader` with caching turned off, so that the child nodes will never be
built. Therefore the conclusion of the previous paragraph remains valid: processing the message with a databinding
will not create a complete object model representation of the XML.

Usage of an `OMSourcedElement` also solves another architectural challenge posed by
the Mapped JSON convention: the JSON payload can only be converted to XML if the namespace mappings
are known. Since they are defined per service, they are only known after the incoming message has been
dispatched and the target service has been identified. This typically occurs
in `RequestURIBasedDispatcher`, which is executed after
the message builder. This means that `JSONOMBuilder` cannot actually perform the conversion.
Usage of an `OMSourcedElement` avoids this issue because the conversion is done lazily when
the `OMSourcedElement` is first accessed, and this occurs after `RequestURIBasedDispatcher`
has been executed.

Another advantage of using `OMSourcedElement` is that a JSON aware service could directly process
the JSON payload without going through the JSON to XML conversion. That is possible because the `OMDataSource`
simply keeps a reference to the JSON payload and this reference is accessible to JSON aware code.

## Processing of outgoing messages

For outgoing messages, the two JSON message formatters `JSONMessageFormatter` and
`JSONBadgerfishMessageFormatter` use Jettision to create an appropriate `XMLStreamWriter`
and then request Axiom to serialize the body element to that `XMLStreamWriter`. If a databinding
is used, then the body element will typically be an `OMSourcedElement` with an `OMDataSource`
implementation specific to that databinding. `OMSourcedElement` will delegate the serialization
request to the appropriate method defined by `OMDataSource`. This means that the databinding code
directly writes to the `XMLStreamWriter` instance provided by Jettision, without building an
intermediate XML object model.

Before doing this, the JSON message formatters actually check if the element is an `OMSourcedElement`
backed by a corresponding JSON `OMDataSource` implementation. If that is the case, then they will
extract the JSON payload and directly write it to the output stream. This allows JSON aware services to
bypass the XML to JSON conversion entirely.

# Tests and Samples

## Integration Test

The JSON integration test is available under
test in the
json module of Axis2. It uses the
SimpleHTTPServer to deploy the service. A simple echo service is
used to return the incoming OMSourcedElement object, which
contains the JSONDataSource. There are two test cases for two
different conventions and another one test case to send the request
in GET.

## Yahoo-JSON Sample

This sample is available in the
samples module of Axis2. It is a
client which calls the Yahoo search API using the GET method, with
the parameter output=json. The
Yahoo search service sends the response as a
formatted JSON string with
the content type text/javascript.
This content type is mapped with the JSONOMBuilder in the
axis2.xml. All the results are shown in a GUI. To run the sample, execute the ant script.

These two applications provide good examples of using JSON
within Axis2. By reviewing these samples, you will be able to
better understand Axis2's JSON support implementation.

## Enabling mapped JSON on the ADB quickstart sample

To illustrate how JSON can be enabled on an existing service deployed in Axis2, we will use the ADB stock quote service sample from the
[Quick Start Guide](#docs-quickstartguide--adb). The code for this sample
can be found in the `samples/quickstartadb` folder in the binary distribution.

Only a few steps are necessary to enable JSON (using the Mapped convention) on
that service:

1. Configure the JSON message builders and formatters in `conf/axis2.xml`.
   Add the following element to the `messageFormatters`:


```

<messageFormatter contentType="application/json"
                  class="org.apache.axis2.json.JSONMessageFormatter"/>
```

   Also add the following element to the `messageBuilders:`


```

<messageBuilder contentType="application/json"
                class="org.apache.axis2.json.JSONOMBuilder"/>
```

2. Edit the `services.xml` for the stock quote service and add the following
   configuration:


```

<parameter name="xmlToJsonNamespaceMap">
    <mappings>
        <mapping xmlNamespace="http://quickstart.samples/xsd" jsonNamespace=""/>
    </mappings>
</parameter>
```

   The `services.xml` file can be found under
   `samples/quickstartadb/resources/META-INF`.
3. Build and deploy the service by executing the ant script in
   `samples/quickstartadb` and then start the Axis2 server using
   `bin/axis2server.sh` or `bin/axis2server.bat`.

That's it; the stock quote service can now be invoked using JSON. This can be tested
using the well known [curl](http://curl.haxx.se/) tool:

```
curl -H 'Content-Type: application/json' -d '{"getPrice":{"symbol":"IBM"}}' http://localhost:8080/axis2/services/StockQuoteService
```

This will give the following result:

```
{"getPriceResponse":{"return":42}}
```

---

<a id="docs-json_support_gson"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/json_support_gson.html -->

<!-- page_index: 37 -->

# New JSON support in Apache Axis2

Update: Moshi support is now included as an alternative to GSON, though both are supported and will continue to be. Both libs are very
similar in features though Moshi is widely considered to have better
performance. GSON development has largely ceased. Switching between
Moshi and GSON is a matter of editing the axis2.xml file.

For users of JSON and Spring Boot, the Native approach discussed below can be seen as a complete sample application in
the [JSON and Spring Boot 3 User's Guide.](#docs-json-springboot-userguide)

This documentation explains how the existing JSON support in Apache Axis2 have been improved with two new
methods named, Native approach and XML stream API based approach. Here it initially explains about the
drawbacks of the old JSON support, how to overcome those drawbacks with the new approaches and, how to use
those approaches to send pure JSON objects without converting it to any XML representations. XML Stream API
based approach addresses the namespace problem with pure JSON support, and provides a good solution for
that.

# Introduction

Apache Axis2 is an efficient third generation SOAP processing web services engine. JSON (JavaScript
Object Notation) is a lightweight data-interchange format and, an alternative for XML which is easily
human readable and writable as well as it can be parsed and generated easily for machines.

The existing JSON implementation in Apache Axis2/Java supports badgerfish format of the JSON object, which is an XML representation of JSON object. With this approach, it first completely converts the
badgerfish JSON string to the relevant XML format in the server side and, treats it as a normal SOAP
message. The current JSON implementation also supports Mapped JSON, which is another XML representation
of the JSON object, if we set xmlToJsonNamespaceMap parameter in the services.xml file of the service.
The main problem with Mapped JSON format is, at the client side it is not aware of the namespaces which
is used in server side to validate the request. Therefore with current implementation, it is required
to do modifications to the existing services to use this mapped format support. The current JSON
implementations of Axis2 are slower than the existing SOAP support too. Therefore the existing JSON
support doesn't expose its advantages at all.

However this JSON support can be improved to support pure JSON objects without using any format to
convert it into a XML, as JSON is a light weighted alternative to XML. Thre are two new approaches
have been used with google-gson library, a rich library to convert a JSON string to a Java object
and vice-versa, in order to improve the existing JSON support in Apache Axis2/java.

Gson[1] is a Java library that can be used to convert Java Objects into their JSON representation.
It can be also used to convert a JSON string to an equivalent Java object. Gson can work with arbitrary
Java objects including pre-existing objects for which you do not have the source code.

There are a few open source projects, capable of converting Java objects into JSON. However, most of
them require to place Java annotations in all classes; something that cannot be done if we do not have
access to the source code. Most of them also do not fully support the use of Java Generics. Gson has
considered both of these facts as very important design goals and, the following are some of the
advantages of using Gson to convert JSON into Java objects and vice-versa.

- It provides simple toJSON() and fromJSON() methods to convert Java objects into JSON objects and
  vice-versa.
- It allows pre-existing unmodifiable objects to be converted into/from JSON objects.
- It has the extensive support of Java Generics.
- It allows custom representations for objects.
- It supports arbitrarily complex objects (with deep inheritance hierarchies and extensive use of
  generic types).

As mentioned above, these two new approaches have been introduced to overcome the above explained
problems in the existing JSON implementation (Badgerfish and Mapped) of Axis2. The first one, the
Native approach, has been implemented with completely pure JSON support throughout the axis2 message
processing process while with the second approach which is XML stream API based approach, an
XMLStreamReader/XMLStreamWriter implementation using google-gson with the help of XMLSchema is being
implemented. The detailed description on the two approaches is given out in the next sections of the
documentation.

# Native Approach

The Native approach is for JSON use cases without a WSDL nor any XML dependency, and you just want some simple Java Objects that map to and from GSON or Moshi.

With this approach you can expose your POJO service to accept pure JSON request other than converting to
any representation or format. You just need to send a valid JSON string request to the service url and, in the url you should have addressed the operation as well as the service. Because in this scenario Axis2
uses URI based operation dispatcher to dispatch the correct operation. in
[here](#docs-json_gson_user_guide--native_approach) you can
find the complete user guide for this native approach.

The Native approach is being implemented to use pure JSON throughout the axis2 message processing
process. In Axis2 as the content-type header is used to specify the type of data in the message body, and depending on the content type, the wire format varies. Therefore, we need to have a mechanism to
format the message depending on content type. We know that any kind of message is represented in Axis2
using AXIOM, and when we serialize the message, it needs to be formatted based on content type.
MessageFormatters exist to do that job for us. We can specify MessageFormatters along with the content
type in axis2.xml. On the other hand, a message coming into Axis2 may or may not be XML, but for it to
go through Axis2, an AXIOM element needs to be created. As a result, MessageBuilders are employed to
construct the message depending on the content type.

After building the message it gets pass through AXIS2 execution chain to execute the message. If the
message has gone through the execution chain without having any problem, then the engine will hand over
the message to the message receiver in order to do the business logic invocation. After this, it is up
to the message receiver to invoke the service and send the response. So according to the Axis2
architecture to accomplish this approach it is required to implement three main components, a
MessageBuilder, a MessageReceiver and a MessageFormatter, where in this Native implementation those are
JSONBuilder, JSONRPCMessageReceiver and JSONFomatter, to handle the pure JSON request and invoke the
service and return a completely pure JSON string as a response. In the builder, it creates and returns
a dummy SOAP envelop to process over execution chain, while storing input json stream and a boolean
flag IS\_JSON\_STREAM as a property of input MessageContext. The next one is JSONRPCMessageReceiver which
is an extended subclass of RPCMessageReceiver. In here it checks IS\_JSON\_STREAM property value, if it is
'true' then it processes InputStream stored in input MessageContext, using JsonReader in google-gson API.
Then it invokes request service operation by Gson in google-gson API which uses Java reflection to invoke
the service. To write the response to wire, it stores the returned object and return java bean type, as
properties of output MessageContext. If IS\_JSON\_STREAM is 'false' or null then it is handed over to its
super class RPCMessageReceiver, in order to handle the request. This means, using JSONRPCMessageReceiver
as the message receiver of your service you can send pure JSON messages as well as SOAP requests too.
There is a JSONRPCInOnly-MessageReceiver which extends RPCInOnlyMessageReceiver class, to handle In-Only
JSON requests too. In JSONformatter it gets return object and the java bean type, and writes response as
a pure JSON string to the wire using JsonWriter in google-gson API. The native approach doesn’t support
namespaces. If you need namespace support with JSON then go through XML Stream API based approach.

# XML Stream API Base Approach

XML Stream API Base Approach is for use cases with a WSDL, and in addition to SOAP you also want to support JSON. This support is currently limited to XML Elements and not XML Attributes - though if you are interested in that support please see AXIS2-6081.

As you can see the native approach can only be used with POJO services but if you need to expose your
services which is generated by using ADB or xmlbeans databinding then you need to use this XML Stream
API based approach. With this approach you can send pure JSON requests to the relevant services.
Similar to the native approach you need to add operation name after the service name to use uri based
operation dispatch to dispatch the request operation.
[Here](#docs-json_gson_user_guide--xml_stream_api_base_approach) you can see the user guide
for this XML Stream API based approach.

As mentioned in Native approach, Apache Axis2 uses AXIOM to process XML. If it can be implement a way to
represent JSON stream as an AXIOM object which provides relevant XML infoset while processing JSON
stream on fly, that would be make JSON, in line with Axis2 architecture and will support the services
which have written on top of xmlstream API too.

There are a few libraries like jettison , Json-lib etc. which already provide this
XMLStreaReader/XMLStreamWriter interfaces for JSON. There is no issue in converting JSON to XML, as we
can use jettison for that, but when it comes to XML to JSON there is a problem. How could we identify
the XML element which represent JSON array type? Yes we can identify it if there is two or more
consecutive XML elements as jettison does, but what happen if the expected JSON array type has only one
value? Then there is only one XML element. If we use Json-lib then xml element should have an attribute
name called "class" value to identify the type of JSON. As you can see this is not a standard way and
we cannot use this with Axis2 as well. Hence we can't use above libraries to convert XML to JSON
accurately without distort expected JSON string even it has one value JSON array type.

Therefore with this new improvement Axis2 have it's own way to handle incoming JSON requests and
outgoing JSON responses. It uses GsonXMLStreamReader and GsonXMLStreamWriter which are implementations
of XMLStreamReader/XMLStreamWriter, to handle this requests and responses. To identify expected request
OMElement structure and namespace uri, it uses XmlSchema of the request and response operations. With
the XmlSchema it can provide accurate XML infoset of the JSON message. To get the relevant XMLSchema
for the operation, it uses element qname of the message. At the MessageBuilder level Axis2 doesn't know
the element qname hence it can't get the XmlSchema of the operation. To solve this issue Axis2 uses a
new handler call JSONMessageHandler, which executes after the RequestURIOperationDispatcher handler or optionally the JSONBasedDefaultDispatcher that can be used in the native approach though it is not mandatory (See the JSON based Spring Boot User Guide).
In the MessageBuilder it creates GsonXMLStreamReader parsing JsonReader instance which is created using
inputStream and stores it in input MessageContext as a message property and returns a default SOAP
envelop. Inside the JSONMessageHandler it checks for this GsonXMLStreamReader property, if it is not
null and messageReceiver of the operation is not an instance of JSONRPCMessageReceiver, it gets the
element qname and relevant XMLSchema list from the input MessageContext and pass it to
GsonXMLStreamReader. After that it creates StAXOMBuilder passing this GsonXMLStreamReader as the
XMLStreamReader and get the document element. Finally set this document element as child of default
SOAP body. If Axis2 going to process XMLSchema for every request this would be a performance issue.
To solve this, Axis2 uses an intermediate representation(XmlNode) of operation XmlSchema list and store
it inside the ConfigurationContext with element qname as a property to use it for a next request
which will come to the same operation. Hence it only processes XmlSchema only once for each operation.

Same thing happens in the JsonFormatter, as it uses GsonXMLStreamWriter to write response to wire and
uses intermediate representation to identify the structure of outgoing OMElement. As we know the
structure here we can clearly identify expected JSON response. Even expected JSON string have a JSON
Array type which has only one value.

In addition, XML Stream API based approach supports namespace uri where it get namespaces from the
operation XMLSchema and provides it when it is asked.

---

<a id="docs-json_gson_user_guide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/json_gson_user_guide.html -->

<!-- page_index: 38 -->

# How to configure Native approach and XML Stream API base approach

# How to use Native JSON support

If you need to expose your POJO services to support pure JSON requests as well as SOAP requests, then you
need to go through the following process to do that with this new feature introduced into Axis2 JSON
support.

Step 1 : Set in-out message receiver and in-only message receiver

You need to set `org.apache.axis2.json.gson.rpc.JsonRpcMessageReceiver` with
`http://www.w3.org/ns/wsdl/in-out` message exchange pattern. Also with `http://www.w3.org/ns/wsdl/in-only`
message exchange pattern, set `org.apache.axis2.json.gson.rpc.JsonInOnlyRPCMessageReceiver`.

eg.

```

            <messageReceivers>
                <messageReceiver mep="http://www.w3.org/ns/wsdl/in-out"
                                 class="org.apache.axis2.json.gson.rpc.JsonRpcMessageReceiver"/>
                <messageReceiver mep="http://www.w3.org/ns/wsdl/in-only"
                                 class="org.apache.axis2.json.gson.rpc.JsonInOnlyRPCMessageReceiver"/>
            </messageReceivers>
            
```

Step 2: Set message builder and message formatter

you need to edit axis2.xml in `[AXIS2_HOME]/conf/` directory, to set `org.apache.axis2.json.gson.JsonBuilder`
as message builder with application/json contentType to handle JSON requests and
`org.apache.axis2.json.gson.JsonFormatter` as message formatter with application/json
contentType to write response to wire as JSON format.

eg.

```

                  <messageBuilder contentType="application/json"
                                  class="org.apache.axis2.json.gson.JsonBuilder" />

                  <messageFormatter contentType="application/json"
                                    class="org.apache.axis2.json.gson.JsonFormatter" />
           
```

# How to use XML stream API based approach

You can use this XML Stream API based approach with databinding services like ADB and xmlbeans as well
as with normal POJO services. Follow the steps mentioned below to use this new feature introduced into
Axis2 JSON support.

Step 1 : Set message builder and message formatter

You need to edit axis2.xml in `[AXIS2_HOME]/conf/` directory, to set `org.apache.axis2.json.gson.JsonBuilder`
as message builder with `application/json` contentType to handle JSON requests and, `org.apache.axis2.json.gson.JsonFormatter` as message formatter with `application/json` contentType to
write response to wire as JSON format.

eg.

```

                <messageBuilder contentType="application/json"
                                class="org.apache.axis2.json.gson.JsonBuilder" />

                <messageFormatter contentType="application/json"
                                  class="org.apache.axis2.json.gson.JsonFormatter" />
                        
            
```

Step 2: Set inflow handlers

Remove RequestURIOperationDispatcher handler from dispatch phase and place it as the last handler in
transport phase. Now add new JSONMessageHandler after the RequestURIOperationDispatcher. Finally
transport phase would be like following,

```

            <phaseOrder type="InFlow">
                <!--  System predefined phases  -->
                <phase name="Transport">
                    -------------
                    <handler name="RequestURIOperationDispatcher"
                             class="org.apache.axis2.dispatchers.RequestURIOperationDispatcher"/>
                    <handler name="JSONMessageHandler"
                             class="org.apache.axis2.json.gson.JSONMessageHandler" />
                </phase>
                ------------
            </phaseOrder>
                    
            
```

---

<a id="docs-json-springboot-userguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/json-springboot-userguide.html -->

<!-- page_index: 39 -->

# Apache Axis2 JSON and REST with Spring Boot 3 User's Guide

This guide will help you get started with Axis2 and JSON via REST, using
[Spring Security](https://spring.io/projects/spring-security) with
[Spring Boot 3!](https://spring.io/projects/spring-boot)
It gives a detailed description on how to write JSON based REST Web services and also
Web service clients via JSON and Curl, how to write a custom login, and how to use them
in a token based Web service that also helps prevent cross site scripting (XSS).

More docs concerning Axis2 and JSON can be found in the [Pure JSON Support documentation](#docs-json_support_gson) and [JSON User Guide](#docs-json_gson_user_guide)

## Introduction

This user guide is written based on the Axis2 Standard Binary
Distribution. The Standard Binary Distribution can be directly [downloaded](https://axis.apache.org/axis2/java/core/download.cgi) or built using
the Source Distribution. If
you choose the latter, then the [Installation
Guide](#docs-installationguide) will instruct you on how to build Axis2 Standard Binary
Distribution using the source.

The source code for this guide provides a pom.xml for an entire demo WAR application built by maven.

Please note that Axis2 is an open-source effort. If you feel the code
could use some new features or fixes, please get involved and lend us a hand!
The Axis developer community welcomes your participation.

Let us know what you think! Send your feedback to "[java-user@axis.apache.org](mailto:java-user@axis.apache.org?subject=[Axis2])".
(Subscription details are available on the [Axis2 site](#mail-lists).) Kindly
prefix the subject of the mail with [Axis2].

## Getting Started

This user guide explains how to write and deploy a
new JSON and REST based Web Service using Axis2, and how to write a Web Service client
using JSON with Curl.

All the sample code mentioned in this guide is located in
the **"samples/userguide/src/springbootdemo"** directory of [Axis2 standard binary
distribution](https://axis.apache.org/axis2/java/core/download.cgi).

This quide supplies a pom.xml for building an exploded WAR with Spring Boot 3 -
however this WAR does not have an embedded web server such as Tomcat.

The testing was carried out on Wildfly 32 with Jakarta, by installing the WAR in its app server.

Please deploy the result of the maven build via 'mvn clean install', axis2-json-api.war, into your servlet container and ensure that it installs without any errors.

## Creating secure Web Services

Areas out of scope for this guide are JWT and JWE for token generation and validation, since they require elliptic curve cryptography. A sample token that is not meant for
production is generated in this demo - with the intent that the following standards
should be used in its place. This demo merely shows a place to implement these
standards.

https://datatracker.ietf.org/doc/html/rfc7519

https://datatracker.ietf.org/doc/html/rfc7516

Tip: com.nimbusds is recommended as an open-source Java implementation of these
standards, for both token generation and validation.

DB operations are also out of scope. There is a minimal DAO layer for authentication.
Very limited credential validation is done.

The NoOpPasswordEncoder Spring class included in this guide is meant for demos
and testing only. Do not use this code as is in production.

This guide provides two JSON based web services, LoginService and TestwsService.

The login, if successful, will return a simple token not meant for anything beyond demos.
The intent of this guide is to show a place that the JWT and JWE standards can be
implemented.

Axis2 JSON support is via POJO Objects. LoginRequest and LoginResponse are coded in the LoginService as the names would indicate. A flag in the suupplied axis2.xml file, enableJSONOnly, disables Axis2 functionality not required for JSON and sets up the server to expect JSON.

Also provided is a test service, TestwsService. It includes two POJO Objects as would
be expected, TestwsRequest and TestwsResponse. This service attempts to return
a String with some Javascript, that is HTML encoded by Axis2 and thereby
eliminating the possibility of a Javascript engine executing the response i.e. a
reflected XSS attack.

Concerning Spring Security and Spring Boot 3, the Axis2Application class that
extends [SpringBootServletInitializer](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/web/servlet/support/SpringBootServletInitializer.html) as typically
done utilizes a List of [SecurityFilterChain](https://docs.spring.io/spring-security/site/docs/current/api/org/springframework/security/web/SecurityFilterChain.html) as a
binary choice; A login url will match, otherwise invoke JWTAuthenticationFilter. All URL's
to other services besides the login, will proceed after JWTAuthenticationFilter verifies the
token.

The JWTAuthenticationFilter class expects a token from the web services JSON client in
the form of "Authorization: Bearer mytoken".

The Axis2WebAppInitializer class supplied in this guide, is the config class
that registers AxisServlet with Spring Boot 3.

Axis2 web services are installed via a WEB-INF/services directory that contains
files with an .aar extention for each service. These aar files are similar to
jar files, and contain a services.xml that defines the web service behavior.
The pom.xml supplied in this guide generates these files.

Tip: don't expose methods in your web services that are not meant to be exposed, such as getters and setters. Axis2 determines the available methods by reflection.
For JSON, the message name at the start of the JSON received by the Axis2 server
defines the Axis2 operation to invoke. It is recommended that only one method per
class be exposed as a starting point. The place to add method exclusion is the
services.xml file:

```

    <excludeOperations>
        <operation>setMyVar</operation>
    </excludeOperations>
```

The axis2.xml file can define [GSON](https://github.com/google/gson) or [Moshi](https://github.com/square/moshi) as the JSON engine. GSON was the original
however development has largely ceased. Moshi is very similar and is widely considered
to be the superior implementation in terms of performance. GSON will likely continue to
be supported in Axis2 because it is helpful to have two JSON implementations to compare
with for debugging.

JSON based web services in the binary distribution of axis2.xml are not enabled by
default. See the supplied axis2.xml of this guide, and note the places were it has
"moshi". Just replace "moshi" with "gson" as a global search and replace to switch to
GSON.

Axis2 web services that are JSON based must be invoked from a client that sets an
HTTP header as "Content-Type: application/json". In order for axis2 to properly
handle JSON requests, this header behavior needs to be defined in the file
WEB-INF/conf/axis2.xml.

```

    <message name="requestMessage">
        <messageFormatter contentType="application/json"
                          class="org.apache.axis2.json.moshi.JsonFormatter"/>
```

Other required classes for JSON in the axis2.xml file include JsonRpcMessageReceiver, JsonInOnlyRPCMessageReceiver, JsonBuilder, JSONBasedDefaultDispatcher and JSONMessageHandler.

Invoking the client for a login that returns a token can be done as follows:

```

curl -v -H "Content-Type: application/json" -X POST --data @/home/myuser/login.dat http://localhost:8080/axis2-json-api/services/loginService
```

Where the contents of /home/myuser/login.dat are:

```

{"doLogin":[{"arg0":{"email":java-dev@axis.apache.org,"credentials":userguide}}]}
```

Response:

```

{"response":{"status":"OK","token":"95104Rn2I2oEATfuI90N","uuid":"99b92d7a-2799-4b20-b029-9fbd6108798a"}}
```

Invoking the client for a Test Service that validates a sample token can be done as
follows:

```

curl -v -H "Authorization: Bearer 95104Rn2I2oEATfuI90N" -H "Content-Type: application/json" -X POST --data @/home/myuser/test.dat http://localhost:8080/axis2-json-api/services/testws'
```

Where the contents of /home/myuser/test.dat are below. arg0 is a var name
and is used by Axis2 as part of its reflection based code:

```

{"doTestws":[{"arg0":{"messagein":hello}}]}
```

Response, HTML encoded to prevent XSS. For the results with encoding see src/site/xdoc/docs/json-springboot-userguide.xml.

```

{"response":{"messageout":"<script xmlns=\"http://www.w3.org/1999/xhtml\">alert('Hello');</script> \">","status":"OK"}}
```

---

<a id="docs-corba-deployer"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/corba-deployer.html -->

<!-- page_index: 40 -->

# Exposing CORBA Services as Web Services

## Overview

### What is CORBA?

CORBA stands for Common Object Request Broker Architecture. It allows clients to invoke methods of remote objects running on remote machines through a binary protocol such as IIOP.

### What Axis2 CORBA module does?

The Axis2 CORBA module acts as a bridge between SOAP and IIOP protocols by converting SOAP messages originated from a web services client to IIOP messages and vise versa. In other words, Axis2 CORBA module allows web service client to invoke methods on a remote CORBA server.

#### Features

- Supports all the primitive and composite IDL data types including Value types (objects by value), Structures, Union, Sequences and Arrays (including multidimensional arrays), Enumerations and Exceptions.
- Dynamic conversion of complex data types
- IDL driven WSDL generation
- Supports CORBA pre-processor directives

### Why it is Useful?

- Convert legacy CORBA services into web services
- Facilitate interoperability between heterogeneous systems
- Integrate CORBA services with Enterprise Service Buses (ESBs)

## Tutorial

This tutorial explains how to write a simple CORBA service and how to make it available as a web service using the Axis2 CORBA module. Let's start the tutorial by creating an IDL file.

### Prerequisites

- Sun JDK version 5.0 or higher
- Latest version of Axis2 with Axis2 CORBA module

### Creating the IDL file

The Interface Definition Language (IDL) is used to describe the interface to a CORBA object. An IDL file can then be used to generate the source code for the CORBA server.
Copy the following listing and save as a text file named `calculator.idl`.

```

// Address book system module
module example
{
    // A data structure which contains two integer values
    struct numbers
    {
        long first;
        long second;
    };
 
    // Specify interface to our address book
    interface calculator
    {
        // returns n.first + n.second
        long add(in numbers n);

        // returns n.first + n.second
        long subtract(in numbers n);
    };
};
```

### Creating the CORBA server

Open a console window and type the following command. (Make sure JAVA\_HOME/bin is included to the PATH environment variable)

```
idlj -fall calculator.idl
```

idlj generates several classes needed for CORBA servers and client. Typically, idlj command will generate the following file structure.

```

|
|   calculator.idl
|
\---example
        numbersHelper.java
        numbersHolder.java
        numbers.java
        calculatorPOA.java
        _calculatorStub.java
        calculatorHolder.java
        calculatorHelper.java
        calculator.java
        calculatorOperations.java
```

Goto the example subdirectory and create `calculatorImpl.java` file as follows.

```

package example;

import example.calculatorPackage.numbers;

public class calculatorImpl extends calculatorPOA {

	public int add(numbers n) {
		return n.first + n.second;
	}

	public int subtract(numbers n) {
		return n.first - n.second;
	}
}
```

Go back to the root directory (the directory where calculator.idl is located) and create `Server.java` as follows.

```

import java.io.*;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;
import example.calculatorImpl;

public class Server {
    public static void main(String[] args) {
        org.omg.CORBA_2_3.ORB orb = 
        	(org.omg.CORBA_2_3.ORB) org.omg.CORBA.ORB.init(args, null);
        try {
            org.omg.PortableServer.POA poa = 
            	org.omg.PortableServer.POAHelper.narrow(
            			orb.resolve_initial_references("RootPOA"));
            poa.the_POAManager().activate();
            org.omg.CORBA.Object o = 
            	poa.servant_to_reference(new calculatorImpl());
            if(args.length == 1) {
                PrintWriter ps = new PrintWriter(new FileOutputStream(args[0]));
                ps.println(orb.object_to_string(o));
                ps.close();
            } else {
                NamingContextExt nc = 
                	NamingContextExtHelper.narrow(
                			orb.resolve_initial_references("NameService"));
                nc.bind(nc.to_name("calculator"), o);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        orb.run();
    }
}
```

Compile all the Java classes by using the following command.

```
javac *.java
```

### Creating the CORBA web service

Now we are ready to create a CORBA web service using the Axis2 CORBA module. First of all we have to prepare Axis2 to work with CORBA module.
1. Make sure axis2-corba-{version}.jar is available in AXIS2\_HOME/lib directory.
2. Download latest Apache Yoko binary distribution form http://cwiki.apache.org/YOKO/download.html. Extract the downloaded archive to a temporary directory and copy yoko-core-{version}.jar and yoko-spec-corba{version}.jar to AXIS2\_HOME/lib directory. (Axis2 CORBA module can also work with other CORBA implementations. Refer 'Additional Configuration Details' section for more information.)
3. Add the following line to the <axisconfig> section of the axis2.xml file which is located in AXIS2\_HOME/conf directory.

```
<deployer extension=".xml" directory="corba" class="org.apache.axis2.corba.deployer.CorbaDeployer"/>
```

4.Create a new directory named corba inside AXIS2\_HOME/repository directory.
Now, your Axis2 server is ready to deploy CORBA web services. Copy calculator.idl file to the newly created corba directory and create a new file named `calculator.xml` as follows inside the same directory.

```

<service name="Calculator">
    <description>Calculator Service</description>
    <parameter name="idlFile">calculator.idl</parameter>
    <parameter name="interfaceName">example::calculator</parameter>
    <parameter name="namingServiceUrl">corbaloc::localhost:900/NameService</parameter>
    <parameter name="objectName">calculator</parameter>
</service>
```

Running the Example
Start a console window and execute the following command to start the CORBA name service.

```
tnameserv -ORBInitialPort 900
```

Start an other console window and goto the directory where Server.java is located. Execute the following command to start the CORBA server.

```
java Server
```

Start the Axis2 server. The EPR of the new Calculator web service will be `http://localhost:8080/axis2/services/Calculator`. The WSDL is located at `http://localhost:8080/axis2/services/Calculator?wsdl`. Now you can create a web service client and use it to invoke methods on the CORBA server.

### Additional Configuration details

The service definition file (eg. calculator.xml) supports the following parameters.

| Parameter Name | Description | Required |
| --- | --- | --- |
| idlFil | Relative path to the IDL file | Yes |
| orbClass | Overrides the default orb class name. | No |
| orbSingletonClass | Overrides the default orb singleton class name. (Default: org.apache.yoko.orb.CORBA.ORB) | No |
| namingServiceUrl | URL of the CORBA naming service (Default: org.apache.yoko.orb.CORBA.ORBSingleton) | No |
| iorFilePath | Path to IOR file | No |
| iorString | IOR as a string | No |
| objectName | Name of the CORBA service which used in the naming service Required if namingServiceUrl is present interfaceName Full name of the IDL interface used for the web service. (use :: as the separator between module and interface names) | Yes |

### Notes:

1. Axis2 CORBA module uses Apache Yoko as the default CORBA implementation. If you want to use a CORBA implementation other than Apache Yoko, override orbClass and orbSingletonClass properties.
2. To run the above tutorial without a naming service:
Use `java Server /path/to/a/new/file` to start the server. Remove `namingServiceUrl` and `objectName` properties from the `calculator.xml` file and add the following line to the same file.

```
<parameter name="iorFilePath">/path/to/a/new/file</parameter>
```

---

<a id="docs-ejb-provider"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/ejb-provider.html -->

<!-- page_index: 41 -->

# Guide to using EJB Provider for Axis2

The EJB message receiver allows one to access stateless session
EJBs (Enterprise JavaBeans) through Web services. The example used
in this guide illustrates how to use the EJB provider that ships
with Axis2 to access EJBs deployed on a J2EE server such as
Geronimo or JBoss.

This example explains how to use Geronimo 1.1 and JBoss 4.0.4.GA
as application server.

The following steps will take you through the example through
which we will explain how to use an EJB provider in Axis2

## 1. Creating a Simple Stateless Session EJB

First we need to create a stateless session EJB. Use the
following files to make an EJB for testing:

```

Remote interface (Hello.java)
package my.ejb;
import javax.ejb.EJBObject;

public interface Hello extends EJBObject, HelloBusiness {
}
```

The following interface defines the business methods available
in

`1.`HelloBusiness.java

```

package my.ejb;
import java.rmi.RemoteException;

public interface HelloBusiness {
   public String sayHello(String name) throws RemoteException;
}
```

2, Remote home interface - HelloHome.java

```

package my.ejb;
import javax.ejb.EJBHome;
import javax.ejb.CreateException;
import java.rmi.RemoteException;

public interface HelloHome extends EJBHome {
   public Hello create() throws CreateException, RemoteException;
}
```

3. Bean class - HelloBean.java

```

package my.ejb;
import javax.ejb.SessionBean;
import javax.ejb.SessionContext;
import javax.ejb.EJBException;
import javax.ejb.CreateException;

public class HelloBean implements SessionBean {
   public void setSessionContext(SessionContext sessionContext) throws
      EJBException {}

   public void ejbRemove() throws EJBException {}
   public void ejbActivate() throws EJBException {}
   public void ejbPassivate() throws EJBException {}
   public void ejbCreate() throws CreateException {}

   public String sayHello(String name) {
      return "Hello " + name + ", Have a nice day!";
   }

}
```

4. Deployment descriptor - ejb-jar.xml

```

<?xml version="1.0" encoding="UTF-8"?>
<ejb-jar xmlns="http://java.sun.com/xml/ns/j2ee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee
        http://java.sun.com/xml/ns/j2ee/ejb-jar_2_1.xsd"
        version="2.1">

  <enterprise-beans>
     <session>
       <ejb-name>Hello</ejb-name>
       <home>my.ejb.HelloHome</home>
       <remote>my.ejb.Hello</remote>
       <ejb-class>my.ejb.HelloBean</ejb-class>
       <session-type>Stateless</session-type>
       <transaction-type>Bean</transaction-type>
     </session>
  </enterprise-beans>
  <assembly-descriptor>
     <container-transaction>
       <method>
          <ejb-name>Hello</ejb-name>
          <method-name>*</method-name>
       </method>
       <trans-attribute>Required</trans-attribute>
     </container-transaction>
  </assembly-descriptor>
</ejb-jar>
```

Now we have to write application server specific deployment
descriptor(s) for the Hello EJB. The following listing shows an
example Geronimo/OpenEJB deployment descriptor
(openejb-jar.xml)

```

<?xml version="1.0" encoding="UTF-8"?>
<openejb-jar 
    xmlns="http://www.openejb.org/xml/ns/openejb-jar-2.1"
    xmlns:naming="http://geronimo.apache.org/xml/ns/naming-1.1"
    xmlns:security="http://geronimo.apache.org/xml/ns/security-1.1"
    xmlns:sys="http://geronimo.apache.org/xml/ns/deployment-1.1"
    xmlns:pkgen="http://www.openejb.org/xml/ns/pkgen-2.0">
    <enterprise-beans>
        <session>
            <ejb-name>Hello</ejb-name>
            <jndi-name>my/ejb/HelloBean</jndi-name>
        </session>
    </enterprise-beans>
</openejb-jar>
```

If you want to test on JBoss, use the following JBoss deployment
descriptor (jboss.xml)

```

<?xml version="1.0"?>
<!DOCTYPE jboss PUBLIC "-//JBoss//DTD JBOSS 4.0//EN"
      "http://www.jboss.org/j2ee/dtd/jboss_4_0.dtd">
<jboss>
    <enterprise-beans>
      <session>
         <ejb-name>Hello</ejb-name>
         <jndi-name>my/ejb/HelloBean</jndi-name>
      </session>
    </enterprise-beans>
</jboss>
```

Compile the above java classes and bundle the compiled classes
and the XML files into a jar file (HelloEJB.jar) as shown
below.

```

 
HelloEJB.jar
  |
  +--META-INF
  |    +--ejb-jar.xml
  |    +--jboss.xml [If you want to deploy on Jboss]
  |    +--openejb-jar.xml  [If you want to deploy on Geronimo/Openejb]
  |
  +--my
       +--ejb
             |
             +--Hello.class
             +--HelloBean.class
             +--HelloBusiness.class
             +--HelloHome.class
 
```

Next, deploy the HelloEJB.jar file onto the appropriate J2EE
application server.

## Creating the Axis2 Service Archive

Now we need to make the services.xml file.

```

<serviceGroup>
    <service name="HelloBeanService">
        <description>Hello! web service</description>
        <messageReceivers>
            <messageReceiver mep="http://www.w3.org/ns/wsdl/in-only"
                class="org.apache.axis2.rpc.receivers.ejb.EJBInOnlyMessageReceiver"/>
        <messageReceiver mep="http://www.w3.org/ns/wsdl/in-out"
                class="org.apache.axis2.rpc.receivers.ejb.EJBMessageReceiver"/>
        </messageReceivers>
        <parameter name="ServiceClass">my.ejb.HelloBusiness</parameter>
        <parameter name="remoteInterfaceName">my.ejb.Hello</parameter>
        <parameter name="homeInterfaceName">my.ejb.HelloHome</parameter>
        <parameter name="beanJndiName">my/ejb/HelloBean</parameter>
        <parameter name="providerUrl">[URL]</parameter>
        <parameter name="jndiContextClass">[Context Factory Class
             Name]</parameter>
     </service>
</serviceGroup>
```

In the above services.xml file, replace the [URL] and [Context
Factory Class Name] with valid values as follows:

**i.e. If the EJB is deployed on Geronimo:**

Replace [URL] by 127.0.0.1:4201

Replace [Context Factory Class Name] by
org.openejb.client.JNDIContext

**For Jboss:**

Replace [URL] by jnp://localhost:1099

Replace [Context Factory Class Name] by
org.jnp.interfaces.NamingContextFactory

Bundle the HelloBeanService.wsdl, services.xml, remote interface
class and home interface class as illustrated below:

```

 
HelloBeanService.aar
  |
  +--META-INF
  |    +--services.xml
  |
  +--lib
  |    +--[jars used by the ejb client eg.initial context factory classes]
  |
  +--my
       +--ejb
             +--Hello.class
             +--HelloBusiness.class
             +--HelloHome.class
 
```

The lib directory of HelloBeanService.aar must contain all the
libraries needed to access the EJB. If the EJB is deployed on
**Geronimo**, add the following jar files to the lib
directory.

- cglib-nodep-2.1\_3.jar
- geronimo-ejb\_2.1\_spec-1.0.1.jar
- geronimo-j2ee-jacc\_1.0\_spec-1.0.1.jar
- geronimo-kernel-1.1.jar
- geronimo-security-1.1.jar
- openejb-core-2.1.jar

For **JBoss** add the following jar files.

- jnp-client.jar
- jboss-client.jar
- jboss-common-client.jar
- jboss-remoting.jar
- jboss-serialization.jar
- jboss-transaction-client.jar
- concurrent.jar
- jbosssx-client.jar
- jboss-j2ee.jar

Deploy HelloBeanService.aar on an Axis2 server.

Now you can access the Hello EJB through Web services. Since our
EJB message receivers extend RPC message receivers, org.apache.axis2.rpc.client.RPCServiceClient can be used to invoke
the service as illustrated in the following code fragment.

```

...

RPCServiceClient serviceClient = new RPCServiceClient();
Options options = serviceClient.getOptions();

EndpointReference targetEPR = new
   EndpointReference("http://localhost:8080/axis2/services/HelloBeanService");

options.setTo(targetEPR);
QName hello = new QName("http://ejb.my/xsd", "sayHello");
Object[] helloArgs = new Object[] {"John"};

System.out.println(serviceClient.invokeBlocking(hello,
   helloArgs).getFirstElement().getText());

...
```

---

<a id="docs-soapmonitor-module"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/soapmonitor-module.html -->

<!-- page_index: 42 -->

# Using the SOAP Monitor

**Warning: the SOAP Monitor uses a protocol based on Java serialization
and is therefore vulnerable to attacks. It should be used exclusively as a
development and debugging tool, but never be permanently enabled on production
systems.**

Web service developers often want to see the SOAP messages that are being
used to invoke the Web services, along with the results of those messages.
The goal of the SOAP Monitor utility is to provide a way for the developers
to monitor these SOAP messages without requiring any special configuration or
restarting the server.

In this utility, a handler has been written and added to the global
handler chain. As SOAP requests and responses are received, the SOAP message
information is forwarded to a SOAP monitor service where it can be displayed
using a Web browser interface. The SOAP message information is accessed by a
Web browser by going to http://localhost:8080/axis2/SOAPMonitor (where 8080
is the port number where the application server is running). The SOAP message
information is displayed through a Web browser by using an applet that opens
a socket connection to the SOAP monitor service. This applet requires a Java
plug-in 1.3 or higher to be installed in your browser. If you do not have a
correct plug-in, the browser will prompt you to install one. The port used by
the SOAP monitor service to communicate with applets is configurable. Edit
the web.xml file to change the port used by the Axis2 Web application.

The SOAP Monitor module (soapmonitor.mar) is available in the axis2.war
but it is not engaged by default. The SOAP Monitor is NOT enabled by default
for security reasons.

The SOAP Monitor can be engaged by inserting the following in the
axis2.xml file.

```
   <module ref="soapmonitor"/>
```

In the axis2.xml file, define your phase orders for the 'soapmonitorPhase'
referenced in the module.xml of soapmonitor.mars. Below is an example which
should NOT be copied exactly, since the default phases change occasionally.
The important point here is that 'soapmonitorPhase' should be placed under
the 'user can add his own phases to this area' comment in the 'inflow',
'outflow', 'INfaultflow', and 'Outfaultflow' sections.

```
    <phaseOrder type="inflow">
        <!--System pre defined phases-->
        <phase name="TransportIn"/>
        <phase name="PreDispatch"/>
        <phase name="Dispatch" class="org.apache.axis2.engine.DispatchPhase">
            <handler name="AddressingBasedDispatcher"
                     class="org.apache.axis2.dispatchers.AddressingBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="RequestURIBasedDispatcher"
                     class="org.apache.axis2.dispatchers.RequestURIBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="SOAPActionBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPActionBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="SOAPMessageBodyBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPMessageBodyBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="InstanceDispatcher"
                     class="org.apache.axis2.engine.InstanceDispatcher">
                <order phase="PostDispatch"/>
            </handler>
        </phase>
        <!--System pre defined phases-->
        <!--After Postdispatch phase module author or or service author can add any phase he want-->
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
    </phaseOrder>
    <phaseOrder type="outflow">
        <!--user can add his own phases to this area-->
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
        <!--system predefined phase-->
        <!--these phase will run irrespective of the service-->
        <phase name="PolicyDetermination"/>
        <phase name="MessageOut"/>
    </phaseOrder>
    <phaseOrder type="INfaultflow">
        <!--user can add his own phases to this area-->
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
    </phaseOrder>
    <phaseOrder type="Outfaultflow">
        <!--user can add his own phases to this area-->
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
        <phase name="PolicyDetermination"/>
        <phase name="MessageOut"/>
    </phaseOrder>
```

To configure the servlet to communicate with the applet, add the following
code to the web.xml (The SOAPMonitorPort is configurable.):

```
    <servlet>
       <servlet-name>SOAPMonitorService</servlet-name>
       <display-name>SOAPMonitorService</display-name>
       <servlet-class>
         org.apache.axis2.soapmonitor.servlet.SOAPMonitorService
       </servlet-class>
       <init-param>
          <param-name>SOAPMonitorPort</param-name>
          <param-value>5001</param-value>
       </init-param>
       <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>SOAPMonitorService</servlet-name>
        <url-pattern>/SOAPMonitor</url-pattern>
    </servlet-mapping>
```

Finally, the applet classes must be placed into the Web application so that
they can be loaded by the Web browser. You can get the compiled applet
classes from the WEB-INF/lib/axis2-soapmonitor-servlet-2.0.0.jar which is inside
the extracted axis2.war. To extract the content of the file, simply
execute the command, `jar -xf axis2-soapmonitor-servlet-2.0.0.jar`.
The applet code is in the org.apache.axis2.soapmonitor.applet package and therefore
the 'org' directory created by the unpacking of JAR file should be placed
in <CATALINA\_HOME>/webapps/axis2/.

Using a Web browser, go to http[s]://host[:port][/webapp]/SOAPMonitor
(e.g.http://localhost:8080/axis2/SOAPMonitor) substituting the correct values
for your Web application. This will show the SOAP Monitor applet used to view
the service requests and responses. Any requests to services that have been
configured and deployed correctly should show up in the applet.

The SOAPMonitor with attachments currently serializes themselves as base64
characters. It is therefore recommended to use the TCPMon tool to correctly
capture MTOM and SWA messages as an multipart mime where the binary data is
an attachment.

---

<a id="docs-reference"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/reference.html -->

<!-- page_index: 43 -->

# Axis2 Reference Guide

## WSDL2Java Reference

```
NAME
       wsdl2java.sh or wsdl2java.bat - Generates java code according to a given WSDL file to handle Web service invocation.
       These scripts can be found under the bin directory of the Axis2 distribution.

SYNOPSIS
       wsdl2java.sh [OPTION]... -uri <Location of WSDL>

DESCRIPTION
       Given a WSDL file, this generates java code to handle Web service invocations.

      -o <path>                Specify a directory path for the generated code.
      -a                       Generate async style code only (Default: off).
      -s                       Generate sync style code only (Default: off). Takes precedence over -a.
      -p <pkg1>                Specify a custom package name for the generated code.
      -l <language>            Valid languages are java and c (Default: java).
      -t                       Generate a test case for the generated code.
      -ss                      Generate server side code (i.e. skeletons) (Default: off).
      -sd                      Generate service descriptor (i.e. services.xml). (Default: off). Valid with -ss.
      -d <databinding>         Valid databinding(s) are adb, xmlbeans, jibx and jaxbri (Default: adb).
      -g                       Generates all the classes. Valid only with -ss.
      -pn <port_name>          Choose a specific port when there are multiple ports in the wsdl.
      -sn <service_name>       Choose a specific service when there are multiple services in the wsdl.
      -u                       Unpacks the databinding classes
      -r <path>                Specify a repository against which code is generated.
      -ns2p ns1=pkg1,ns2=pkg2  Specify a custom package name for each namespace specified in the wsdls schema.
      -ssi                     Generate an interface for the service implementation (Default: off).
      -wv <version>            WSDL Version. Valid Options : 2, 2.0, 1.1
      -S                       Specify a directory path for generated source
      -R                       Specify a directory path for generated resources
      -em                      Specify an external mapping file
      -f                       Flattens the generated files
      -uw                      Switch on un-wrapping.
      -xsdconfig <file path>   Use XMLBeans .xsdconfig file. Valid only with -d xmlbeans.
      -ap                      Generate code for all ports
      -or                      Overwrite the existing classes
      -b                       Generate Axis 1.x backword compatible code.
      -sp                      Suppress namespace prefixes (Optimzation that reduces size of soap request/response)
      -E<key> <value>          Extra configuration options specific to certain databindings. Examples:
                               -Ebindingfile <path>                   (for jibx) - specify the file path for the binding file
                               -Etypesystemname <my_type_system_name> (for xmlbeans) - override the randomly generated type system name
                               -Ejavaversion 1.5                      (for xmlbeans) - generates Java 1.5 code (typed lists instead of arrays)
                               -Emp <package name> (for ADB) - extension mapper package name
                               -Eosv (for ADB) - turn off strict validation.
                               -Eiu (for ADB) - Ignore Unexpected elements instead of throwing ADBException
                               -Ewdc (for xmlbeans) - Generate code with a dummy schema. if someone use this option
                                  they have to generate the xmlbeans code seperately with the scomp command comes with the
                                  xmlbeans distribution and replace the Axis2 generated classes with correct classes
      --noBuildXML             Dont generate the build.xml in the output directory
      --noWSDL                 Dont generate WSDLs in the resources directory
      --noMessageReceiver      Dont generate a MessageReceiver in the generated sources
      --http-proxy-host        Proxy host address if you are behind a firewall
      --http-proxy-port        Proxy prot address if you are behind a firewall
      -ep                      Exclude packages - these packages are deleted after codegeneration
    
EXAMPLES
       wsdl2java.sh -uri ../samples/wsdl/Axis2SampleDocLit.wsdl
       wsdl2java.sh -uri ../samples/wsdl/Axis2SampleDocLit.wsdl -ss -sd 
       wsdl2java.sh -uri ../samples/wsdl/Axis2SampleDocLit.wsdl -ss -sd -d xmlbeans -o ../samples -p org.apache.axis2.userguide
```

## Java2WSDL Reference

```
NAME
       Java2WSDL.sh or Java2WSDL.bat - Generates the appropriate WSDL file for a given java class.
       These scripts can be found under the bin directory of the Axis2 distribution.

SYNOPSIS
       Java2WSDL.sh [OPTION]... -cn <fully qualified class name>

DESCRIPTION
       Given a java class generates a WSDL file for the given java class. 

      -o <output location>                    output directory
      -of <output file name>                  output file name for the WSDL
      -sn <service name>                      service name
      -l <one or more soap addresses>         location URIs, comma-delimited
      -cp <class path uri>                    list of classpath entries - (urls)
      -tn <target namespace>                  target namespace for service
      -tp <target namespace prefix>           target namespace prefix for service
      -stn <schema target namespace>          target namespace for schema
      -stp <schema target namespace prefix>   target namespace prefix for schema
      -st <binding style>                     style for the WSDL
      -u <binding use>                        use for the WSDL
      -nsg <class name>                       fully qualified name of a class that implements NamespaceGenerator
      -sg <class name>                        fully qualified name of a class that implements SchemaGenerator
      -p2n [<java package>,<namespace>] [<java package>,<namespace>]
                                              java package to namespace mapping for argument and return types
      -p2n [all, <namespace>]                 to assign all types to a single namespace
      -efd <qualified/unqualified>            setting for elementFormDefault (defaults to qualified)
      -afd <qualified/unqualified>            setting for attributeFormDefault (defaults to qualified)
      -xc class1 -xc class2...                extra class(es) for which schematype must be generated.
      -wv <1.1/2.0>                           wsdl version - defaults to 1.1 if not specified
      -dlb                                    generate schemas conforming to doc/lit/bare style
      -dne                                    disallow nillable elements in the generated schema
      -doe                                    disallow optional elements in the generated schema
      -disableSOAP11                          disable binding generation for SOAP 1.1
      -disableSOAP12                          disable binding generation for SOAP 1.2
      -disableREST                            disable binding generation for REST
    
EXAMPLES
       Java2WSDL.sh -cn ../samples/test/searchTool.Search
       Java2WSDL.sh -cn ../samples/test/searchTool.Search -sn search
       Java2WSDL.sh -cn ../samples/test/searchTool.Search -u -sn search
       Java2WSDL.sh -cn ../samples/test/searchTool.Search -sn search -o ../samples/test/wsdl  
```

---

<a id="tools"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/index.html -->

<!-- page_index: 44 -->

# Apache Axis2 Tools

Axis2 is bundled with a set of tools in order to make users'
life easier. This page is maintained to keep track of the tools
supported by Axis2.

| Name | Description |
| --- | --- |
| [Code Generator Tool- Command Line & Ant Task](#tools-codegentoolreference) | Tool consists of a command line version and an Ant Task. It is implemented by the WSDL2Code class and WSDL2Java class. One can choose to run the main classes directly or use one of the scripts to run the WSDL2Code and WSDL2Java appropriately. |
| [Service Archive Wizard - Eclipse Plug-in](#tools-eclipse-servicearchiver-plugin) | As part of the Axis2 tool set, the service archive generator is an important tool that allows the generation of service archives ("aar" file or a "jar" files) that can be deployed as a Web services to the Axis2. |
| [Code Generator Wizard - Eclipse Plug-in](#tools-eclipse-wsdl2java-plugin) | Axis2 code generator comes built-in with an [eclipse](http://www.eclipse.org/) plug-in. This can be used to generate a WSDL file from a java class (Java2WSDL) and/or a java class file from a WSDL (WSDL2Java) |
| [Code Generator Wizard - IntelliJ IDEA Plug-in](#tools-idea-idea_plug-in_userguide) | Using this tool one can create service archives that can be deployed as a Web services to the Axis2, and also generate a java class file from a WSDL file (WSDL2Java). |
| [axis2-aar-maven-plugin](#tools-maven-plugins-maven-aar-plugin) | This plugin generates an Axis2 service file (AAR file). |
| axis2-mar-maven-plugin | This plugin generates an Axis2 module archive file (MAR file). |
| [axis2-java2wsdl-maven-plugin](#tools-maven-plugins-maven-java2wsdl-plugin) | This plugin takes as input a Java class and generates a WSDL, which describes a Web service for invoking the classes methods. |
| [axis2-wsdl2code-maven-plugin](#tools-maven-plugins-axis2-wsdl2code-maven-plugin) | This plugin takes as input a WSDL and generates client and server stubs for calling or implementing a Web service matching the WSDL. |
| [axis2-repo-maven-plugin](https://axis.apache.org/axis2/java/core/tools/maven-plugins/axis2-repo-maven-plugin/index.html) | This plugin creates Axis2 repositories from project dependencies. |
| [axis2-xsd2java-maven-plugin](https://axis.apache.org/axis2/java/core/tools/maven-plugins/axis2-xsd2java-maven-plugin/index.html) | This plugin generates ADB beans from a set of XSD files. |

The command line tools and Ant tasks are bundled with the Axis2 binary distribution.
The Eclipse and IntelliJ IDEA plugins are shipped as separate archives. These files can
be downloaded [here](#download).
All Maven plugins are available from the Maven central repository and need not be downloaded separately.

---

<a id="tools-codegentoolreference"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/CodegenToolReference.html -->

<!-- page_index: 45 -->

# Code Generator Tool Guide for Command Line and Ant Task

The Code Generator tool consists of a command line version and
an Ant Task. This document will list the command line references
and Ant task references. Also in detail, this document shows how to
build file using custom Ant task and invoking the Code Generator
from Ant.

This tool is bundled with the [Axis2 Binary
Distribution](https://axis.apache.org/axis2/java/core/download.cgi#std-bin).

## Content

- [Introduction](#tools-codegentoolreference--intro)
- [Command Line Version](#tools-codegentoolreference--cmdline)
  - [Option Reference](#tools-codegentoolreference--cmdref)
- [Ant Task](#tools-codegentoolreference--ant)
  - [Ant Task Reference](#tools-codegentoolreference--antref)
  - [Example Build File Using the Custom Ant
    Task](#tools-codegentoolreference--example)
  - [Invoking the Code Generator From
    Ant](#tools-codegentoolreference--invoking)
- [Appendix](#tools-codegentoolreference--appendix)

## Introduction

This basic tool is implemented by the WSDL2Code class and just
for the convenience in the case of Java (which would be the
majority) there is another WSDL2Java class. One can choose to run
the main classes directly or use one of the scripts to run the
WSDL2Code and WSDL2Java appropriately. (the scripts are found in
the bin directory of the [Standard Binary
Distribution](https://axis.apache.org/axis2/java/core/download.cgi#std-bin))

## Command Line Version

For those users who wish to use the command line version of the
tool, this section will be of value.

### Option Reference

Usage WSDL2Code <option\_reference>

**E.g. :- WSDL2Code -uri <Location of WSDL>**

|  |  |  |  |
| --- | --- | --- | --- |
| **Short Option** | **Long Option** | **Description** |  |
| -uri <Location of WSDL> | None | WSDL file location. This should point to a WSDL file in the local file system. |  |
| -o <output Location> | --output <output Location> | Output file location. This is where the files would be copied once the code generation is done. If this option is omitted the generated files would be copied to the working directory. |  |
| -l <language> | --language <language> | Output language. Currently the code generator can generate code in Java but it has the ability to be extended to support other languages. |  |
| -p <package name> | --package <package name> | The target package name. If omitted, a default package (formed using the target namespace of the WSDL) will be used. |  |
| -a | --async | Generate code only for async style. When this option is used the generated stubs will have only the asynchronous invocation methods. Switched off by default. |  |
| -s | --sync | Generate code only for sync style . When this option is used the generated stubs will have only the synchronous invocation methods. Switched off by default. When used with the -a option, this takes precedence. |  |
| -t | --test-case | Generates a test case. In the case of Java it would be a JUnit test case. |  |
| -ss | --server-side | Generates server side code (i.e. skeletons). Default is off. |  |
| -sd | --service-description | Generates the service descriptor (i.e. server.xml). Default is off. Only valid with -ss, the server side code generation option. |  |
| -d <databinding> | --databinding-method <databinding> | Specifies the Databinding framework. Valid values are xmlbeans, adb, jibx, and none. Default is adb. |  |
| -g | --generate-all | Generates all the classes. This option is valid only with the -ss (server side code generation) option. When on, the client code (stubs) will also be generated along with the skeleton. |  |
| -u | --unpack-classes | Unpack classes. This option specifies whether to unpack the classes and generate separate classes for the databinders. |  |
| -sn <service name> | --service-name <service name> | Specifies the service name to be code generated. If the service name is not specified, then the first service will be picked. |  |
| -pn <port name> | --port-name <port name> | Specifies the port name to be code generated. If the port name is not specified, then the first port (of the selected service) will be picked. |  |
| -ns2p | --namespace2package | Specifies a comma separated list of namespaces and packages where the given package will be used in the place of the auto generated package for the relevant namespace. The list will be the format of ns1=pkg1,ns2=pkg2. |  |
| -ssi | --serverside-interface | Generate an interface for the service skeleton. |  |
| -wv | --wsdl-version | WSDL Version. Valid Options : 2, 2.0, 1.1 |  |
| -S | --source-folder | Specify a directory path for generated source |  |
| -R | --resource-folder | Specify a directory path for generated resources |  |
| -em | --external-mapping | Specify an external mapping file |  |
| -f | --flatten-files | Flattens the generated files |  |
| -uw | --unwrap-params | Switch on un-wrapping |  |
| -xsdconfig |  | Use XMLBeans .xsdconfig file. Valid only with -d xmlbeans |  |
| -ap | --all-ports | Generate code for all ports |  |
| -or | --over-ride | Overwrite the existing classes |  |
| -b | --backword-compatible | Generate Axis 1.x backword compatible code |  |
| -sp | --suppress-prefixes | Suppress namespace prefixes (Optimzation that reduces size of soap request/response) |  |
|  | --noBuildXML | Don't generate the build.xml in the output directory |  |
|  | --noWSDL | Don't generate WSDL's in the resources directory |  |
|  | --noMessageReceiver | Don't generate a MessageReceiver in the generated sources |  |

Apart from these mentioned options one can pass extra options by
prefixing them with -E (uppercase). These extra options will be
processed by the extensions. The extra options that can be passed
are documented separately with the extensions documentation (For
example with ADB).

## Ant Task

The code generator also comes bundled with an Ant task. The ant
task is implemented by the org.apache.axis2.tool.ant.AntCodegenTask
class. Following are the ant task attributes.

### Ant Task Reference

|  |  |
| --- | --- |
| wsdlfilename | WSDL file location. Maps to the -uri option of the command line tool. |
| output | Output file location. This is where the files would be copied once the code generation is done. If this option is omitted the generated files would be copied to the working directory. Maps to the -o option of the command line tool. |
| language | Output language. Currently the code generator can generate code in Java. Maps to the -l option of the command line tool. |
| packageName | The target package name. If omitted, a default package (formed using the target namespace of the WSDL) will be used. Maps to the -p option of the command line tool. |
| databindingName | Data binding framework name. Maps to the -d option of the command line tool. Possible values include "adb", "xmlbeans", "jibx","jaxbri". |
| serviceName | The name of the service in the case of multiple services. Maps to -sn options of the command line tool. |
| portName | The name of the port in the presence of multiple ports. Maps to -pn options of the command line tool. |
| asyncOnly | Generate code only for async style. When this option is used the generated stubs will have only the asynchronous invocation methods. Defaults to false if omitted. Only true and false are applicable as values. Maps to the -a option of the command line tool. |
| syncOnly | Generate code only for sync style. When this option is used the generated stubs will have only the synchronous invocation methods. Defaults to false if omitted. Only true and false are applicable as values. Maps to the -s option of the command line tool. |
| serverSide | Generates server side code (i.e. skeletons). Only true and false are applicable as values. Default is false. Maps to the -ss option of the command line tool. |
| testcase | Generates a test case. Possible values are true and false. Maps to the -t options of the command line tool. |
| generateServiceXml | Generates server side code (i.e. skeletons). Only true and false are applicable as values. Default is false. Maps to the -sd option of the command line tool. |
| unpackClasses | Unpacks the generated classes. This forces the databinding classes to be generated separately, which otherwise would have been generated as inner classes. |
| generateAllClasses | Generates all the classes including client and server side code. Maps to the -g option of the command line tool. |
| namespaceToPackages | A list of namespace to package mappings. |
| serverSideInterface | Flag stating whether to generate an interface for the server side skeleton. |
| repositoryPath | Sets the repository path to be used. Maps to the -r option of the command line tool. |
| wsdlVersion | Sets the version of the wsdl that is being used during codegeneration. This deafults to 1.1 and one can set this to 2, when trying to work with a WSDL 2.0 document. Maps to the -wv option of the command line tool. |
| externalMapping | Location of the external mapping file to be used. Maps to the -em option of the command line tool. |
| targetSourceFolderLocation | Rather than dumping all the code in the same location, one has the option to make the sources to be generated in a different location, given using this option. Maps to the -S option of the command line tool. |
| targetResourcesFolderLocation | Rather than dumping all the code in the same location, one has the option to make the resources to be generated in a different location, given using this option. Maps to the -R option of the command line tool. |
| unwrap | This will select between wrapped and unwrapped during code generation. Default is set to false. Maps to the -uw option of the command line tool. |

### Example Build File Using the Custom Ant Task

Following is an example ant build file that uses the custom Ant
task. You can use any wsdl file to test the example. Replace the
"CombinedService.wsdl" with the name of your wsdl file in the
following script.

```

1 <?xml version="1.0"?>
    2 <project name="CodegenExample" default="main" basedir=".">
    3
    4 <path id="example.classpath">
    5 <fileset dir="classes">
    6 <include name="**/*.jar" />
    7 </fileset>
    8 </path>
    9
    10 <target name="declare" >
    11 <taskdef name="codegen"
    12 classname="org.apache.axis2.tool.ant.AntCodegenTask"
    13 classpathref="example.classpath"/>
    15 </target>
    16
    17 <target name="main" depends="declare">
    18 <codegen
    19 wsdlfilename="C:\test\wsdl\CombinedService.wsdl"
    20 output="C:\output"
    21 serverside="true"
    22 generateservicexml="true"/>
    23 </target>
    24
    25 </project>
```

In the above build script, from line 4 to 8 it sets the
classpath and includes all the .jar files (which are listed below)
into the classpath. From line 10 to 15 it creates a target to
declare a task called "codegen" and sets the appropriate class
(org.apache.axis2.tool.ant.AntCodegenTask) within the classpath in
line 12. From line 17 to 23 it creates the "main" target to
generate the code from the given wsdl. There are some arguments set
form line 19 to 22. Here in line 19 it sets the location of the
wsdl. In line 20 it sets the output directory in which the code is
generated. Line 21 indicates that this build generates the server
side code(skeleton) and line 22 indicates that the services.xml is
also generated.

Notice the main target that uses the "codegen" task which will
use the org.apache.axis2.tool.ant.AntCodegenTask class and run the
code generation tool internally while passing the relevant
arguments and do the proper generation. If a user types

`>ant` or `>ant main`

it will generate the server side code and services.xml for the
given WSDL file (C:\test\wsdl\CombinedService.wsdl -in the above
instance) and the generated code will be written to the specified
output path (C:\output - in the above instance).

For this Ant task to work the following jars need to be in the
class path.

- axis2-\*.jar (from the Axis2 distribution)
- wsdl4j-1.6.2.jar or higher (The WSDL4J implementation jar.
  Bundled with the Axis2 distribution)
- stax-api-1.0.1.jar (The StAX API's that contain the
  javax.xml.namespace.QName class. This jar may be replaced by any
  other jar that contains the javax.xml.namespace.QName
  implementation. However Axis2 uses this class from the
  stax-api-1.0.1.jar which comes bundled with the Axis2
  distribution)
- commons-logging-1.1.jar, neethi-2.0.jar and XmlSchema-1.2.jar
  (from the Axis2 distribution)
- axiom-api-1.2.1.jar and axiom-impl-1.2.1.jar (from the Axis2
  distribution)
- activation-1.1.jar (from the Axis2 distribution)
- wstx-asl-3.1.0.jar (from the Axis2 distribution)

### Invoking the Code Generator From Ant

Since the users may find altering their ant class path a bit
daunting they can also follow an easier technique. The code
generator main class can be invoked directly through the build
file.

Below is an example of a full build.xml needed to run WSDL2Java
and generate the Java source files, compile the sources, and build
an AAR file ready for deployment (These are done one by one, by
calling the targets in the build file separately):

```

<!DOCTYPE project>

<project name="wsdl2java-example" default="usage" basedir=".">

<property name="project-name" value="wsdl2java-example"/>
<property file="build.properties"/>

<property name="build" value="build"/>
<property name="src" value="src"/>
<property name="build.classes" value="build/classes" />

<path id="axis.classpath">
<pathelement location="build/classes" />
<fileset dir="${axis.home}/lib">
<include name="**/*.jar" />
</fileset>
<pathelement location="${build.classes}" />
</path>

<path id="axis_client.classpath">
<pathelement location="build/classes" />
<fileset dir="${axis.home}">
<include name="**/*.jar" />
</fileset>
<fileset dir="lib">
<include name="*.jar" />
</fileset>
<pathelement location="${build.classes}" />
</path>

<target name="usage" description="Build file usage info (default task)">
<echo message=" " />
<echo message="${project-name} " />
<echo message="-------------------------------------------------------" />
<echo message=" " />
<echo message="Available Targets:" />
<echo message=" " />
<echo message=" Compiling:" />
<echo message=" compile - Compiles the WSDL2Java source code" />
<echo message=" " />
<echo message=" Compiling client:" />
<echo message=" compile_client - Compiles the client source code" />
<echo message=" " />
<echo message=" Cleaning up:" />
<echo message=" clean - Delete class files" />
<echo message=" " />
<echo message=" WSDL:" />
<echo message=" wsdl2java - Generate source from WSDL" />
<echo message=" " />
<echo message=" AAR:" />
<echo message=" aar - Generate an .aar for deployment into WEB-INF/services" />
<echo message=" " />
<echo message=" Executing:" />
<echo message=" runLogin - Execute the runLogin client" />
</target>

<target name="prepare" >
<mkdir dir="${build.classes}" />
</target>

<target name="clean" >
<delete dir="${build}" />
<delete dir="${dist}" />
</target>

<target name="compile">
<echo message="Compiling wsdl2 files"/>

<javac
srcdir="output"
destdir="${build.classes}"
deprecation="true"
failonerror="true" debug="true">

<classpath refid="axis.classpath"/>
</javac>

</target>

<target name="wsdl2java" depends="clean,prepare">
<delete dir="output" />
<java classname="org.apache.axis2.wsdl.WSDL2Java" fork="true">
<classpath refid="axis.classpath"/>
<arg value="-d"/>
<arg value="xmlbeans"/>
<arg value="-uri"/>
<arg file="wsdl/LoginEndpoint.wsdl"/>
<arg value="-ss"/>
<arg value="-g"/>
<arg value="-sd"/>
<arg value="-o"/>
<arg file="output"/>
<arg value="-p"/>
<arg value="org.example.types"/>
</java>

<!-- Move the schema folder to classpath-->
<move todir="${build.classes}">
<fileset dir="output/resources">
<include name="**/*schema*/**/*.class"/>
<include name="**/*schema*/**/*.xsb"/>
</fileset>
</move>

</target>

<target name="jar_wsdl" depends="compile">
<jar jarfile="lib/axis2_example_wsdl.jar" >
<fileset dir="${build.classes}" />
</jar>
</target>

<!-- build an .aar file for axis2 web services -->
<target name="aar" depends="compile">
<delete dir="${build.classes}/META-INF" />
<mkdir dir="${build.classes}/META-INF" />
<copy todir="${build.classes}/META-INF" >
<fileset dir="output/resources" >
<!-- axis2 web services definitions file -->
<include name="services.xml"/>
</fileset>
<fileset dir="wsdl" >
<include name="LoginEndpoint.wsdl"/>
</fileset>
</copy>
<jar jarfile="dist/LoginEndpoint.aar" >
<fileset dir="${build.classes}" />
</jar>
</target>

<target name="compile_client">
<echo message="Compiling client files"/>

<javac
srcdir="src"
destdir="${build.classes}"
deprecation="true"
failonerror="true" debug="true">

<classpath refid="axis.classpath"/>
</javac>

</target>

<target name="runLogin" depends="prepare,compile_client" description="run simple Login client">
<java classname="org.client.LoginClient" >
<classpath refid="axis_client.classpath"/>
</java>
</target>

</project>
```

Place the above build.xml file in the 'bin' directory of the
axis2 binary distribution. Then create a build.properties file in
the same directory and specify the axis.home path pointing to the
axis2 binary distribution

E.g. :- axis.home=C://Axis2//axis2-1.1-bin

The above build.xml example also assumes three empty directories
exist, 'dist', 'lib', and 'src'.

Below is a validated WSDL Document following the
Document/Literal Style. The name of this file matches the name used
in the WSDL2Java ant task above, LoginEndpoint.wsdl.

```

<?xml version="1.0" encoding="UTF-8"?>

    <definitions name="LoginService" targetNamespace="http://login" xmlns:tns="http://login"
    xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:ns2="http://login/types">

    <types>
    <schema targetNamespace="http://login/types" xmlns:tns="http://login/types"
    xmlns:soap11-enc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns="http://www.w3.org/2001/XMLSchema">
    <import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>
    <element name="returnWebLoginElement">
    <complexType>
    <sequence>

    <element ref="tns:soap_session_idElement"/>
    <element ref="tns:web_user_nameElement"/>
    </sequence>
    </complexType>
    </element>
    <element name="webLoginElement">

    <complexType>
    <sequence>
    <element ref="tns:user_nameElement"/>
    <element ref="tns:user_passwordElement"/>
    </sequence>
    </complexType>

    </element>
    <element name="user_nameElement" type="xsd:string"/>
    <element name="user_passwordElement" type="xsd:string"/>
    <element name="soap_session_idElement" type="xsd:string"/>
    <element name="web_user_nameElement" type="xsd:string"/>
    </schema></types>

    <message name="LoginEndpoint_webLogin">
    <part name="parameters" element="ns2:webLoginElement"/>
    </message>
    <message name="LoginEndpoint_webLoginResponse">
    <part name="result" element="ns2:returnWebLoginElement"/>
    </message>

    <portType name="LoginEndpoint">
    <operation name="webLogin">
    <input message="tns:LoginEndpoint_webLogin" name="LoginEndpoint_webLogin"/>
    <output message="tns:LoginEndpoint_webLoginResponse" name="LoginEndpoint_webLoginResponse"/>
    </operation>
    </portType>

    <binding name="LoginEndpointBinding" type="tns:LoginEndpoint">
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" style="document"/>
    <operation name="webLogin">
    <soap:operation soapAction="webLogin"/>
    <input name="LoginEndpoint_webLogin">
    <soap:body use="literal"/>

    </input>
    <output name="LoginEndpoint_webLoginResponse">
    <soap:body use="literal"/>
    </output>
    </operation>
    </binding>

    <service name="LoginService">
    <port name="LoginEndpointPort" binding="tns:LoginEndpointBinding">
    <soap:address location="http://localhost:8080/axis2/services/LoginService"/></port>
    </service></definitions>
```

Place the above file, named LoginEndpoint.wsdl, in the directory
'wsdl' which is also inside the 'bin' directory. Run the wsdl2java
command via the ant task defined above (>ant wsdl2java), and
there will be a directory called 'output' created. This directory
contains the WSDL2Java generated source.

An important detail is that an XMLBean class file is also
generated by WSDL2Java, TypeSystemHolder.class. That file is placed
into build/classes by the above ant task and will be needed to
compile the generated sources. A frequent problem is users get an
error such as:

***ClassNotFoundException : Cannot load SchemaTypeSystem.
Unable to load class with name
schemaorg\_apache\_xmlbeans.system.s68C41DB812F52C975439BA10FE4FEE54.TypeSystemHolder.
Make sure the generated binary files are on the
classpath.***

The TypeSystemHolder.class generated by WSDL2Java must be placed
in your classpath in order to avoid this error.

The next step is to modify the generated Skeleton Java Source
file - the Web service. This file as generated returns null and
needs to be updated to contain the business logic.

After the WSDL2Java command runs the file LoginEndpoint.wsdl, edit the following file:

output/src/org/example/types/LoginServiceSkeleton.java. You
should see the following code:

```

/**
    * LoginServiceSkeleton.java
    *
    * This file was auto-generated from WSDL
    * by the Apache Axis2 version: 1.0-RC4 Apr 28, 2006 (05:23:23 IST)
    */
    package org.example.types;
    /**
    * LoginServiceSkeleton java skeleton for the axisService
    */
    public class LoginServiceSkeleton {


    /**
    * Auto generated method signature

    * @param param0

    */
    public login.types.ReturnWebLoginElementDocument webLogin
    (login.types.WebLoginElementDocument param0 )

    {
    //Todo fill this with the necessary business logic
    throw new java.lang.UnsupportedOperationException();
    }

    }
```

Replace the contents of this file with the following, which uses
the complex types generated by WSDL2Java and the example wsdl
file:

```

/**
    * LoginServiceSkeleton.java
    *
    * This file was auto-generated from WSDL
    * by the Apache Axis2 version: 1.0-RC4 Apr 28, 2006 (05:23:23 IST)
    */
    package org.example.types;
    import login.types.ReturnWebLoginElementDocument;
    import login.types.ReturnWebLoginElementDocument.*;
    import login.types.WebLoginElementDocument;
    import login.types.WebLoginElementDocument.*;

    /**
    * Auto generated java skeleton for the service by the Axis code generator
    */
    public class LoginServiceSkeleton {

    /**
    * Auto generated method signature

    * @param webLoginElementDocument changed from param0

    */
    public ReturnWebLoginElementDocument webLogin
    (WebLoginElementDocument webLoginElementDocument ){

    //Todo fill this with the necessary business logic
    System.out.println("LoginServiceSkeleton.webLogin reached successfully!");

    // Get parameters passed in
    WebLoginElement webLoginElement = webLoginElementDocument.getWebLoginElement();
    String userName = webLoginElement.getUserNameElement();
    String password = webLoginElement.getUserPasswordElement();
    System.out.println("LoginServiceSkeleton.webLogin userName: " + userName);
    System.out.println("LoginServiceSkeleton.webLogin password: " + password);

    // input paramaters would be used here

    // prepare output
    ReturnWebLoginElementDocument retDoc =
    ReturnWebLoginElementDocument.Factory.newInstance();

    ReturnWebLoginElement retElement = ReturnWebLoginElement.Factory.newInstance();

    retElement.setWebUserNameElement("joe sixpack");
    retElement.setSoapSessionIdElement("some_random_string");
    System.out.println("validate retElement: " + retElement.validate());

    retDoc.setReturnWebLoginElement(retElement);
    System.out.println("validate retDoc: " + retDoc.validate());

    System.out.println("LoginServiceSkeleton.webLogin returning...");

    return retDoc;

    }
    }
```

The next steps assume the axis2.war has been deployed and has
expanded in a servlet container.

Run the 'jar\_wsdl' ant task from the example build.xml (>ant
jar\_wsdl), which generates a jar file axis2\_example\_wsdl.jar in the
'bin/lib' directory. This jar will be used to compile the client, and also will be placed in the servlet container.

Next, run the 'aar' ant task from the example build.xml (>ant
aar), which generates the deployable axis2 Web service. Place
dist/LoginEndpoint.aar into axis2/WEB-INF/services . Place
lib/axis2\_example\_wsdl.jar into axis2/WEB-INF/lib . Verify the
happy axis page loaded the services correctly - there should be the
service 'LoginEndpoint' with the available operation 'webLogin'
displayed.

The last step is to create and run the client. In the src
directory create the file org.client.LoginClient.java, with the
contents below:

```

package org.client;

    import org.apache.axis2.AxisFault;

    import login.types.ReturnWebLoginElementDocument;
    import login.types.ReturnWebLoginElementDocument.*;
    import login.types.WebLoginElementDocument;
    import login.types.WebLoginElementDocument.*;
    import org.example.types.LoginServiceStub;

    /**
    * Login.
    *
    */
    public class LoginClient {

    public static void main(String[] args) {
    try {

    System.out.println("webLogin, firing...");
    LoginServiceStub stub = new LoginServiceStub();

    WebLoginElementDocument webLoginElementDocument
    = WebLoginElementDocument.Factory.newInstance();
    WebLoginElement webLoginElement =
    WebLoginElement.Factory.newInstance();
    webLoginElement.setUserNameElement("joe");
    webLoginElement.setUserPasswordElement("sixpack");

    webLoginElementDocument.setWebLoginElement(webLoginElement);

    System.out.println("validate: " + webLoginElement.validate());
    stub.webLogin(webLoginElementDocument);

    ReturnWebLoginElementDocument returnWebLoginElementDocument =
    stub.webLogin(webLoginElementDocument);

    System.out.println("Client returned");

    ReturnWebLoginElementDocument.ReturnWebLoginElement
    retElement = returnWebLoginElementDocument.getReturnWebLoginElement();

    System.out.println("WebUserName: " + retElement.getWebUserNameElement());
    System.out.println("SOAPSessionId: " + retElement.getSoapSessionIdElement());
    System.out.println("webLogin, completed!!!");

    } catch (AxisFault axisFault) {
    axisFault.printStackTrace();
    } catch (Exception ex) {
    ex.printStackTrace();
    }
    }
    }
```

Now run the ant task 'runLogin' (>ant runLogin). The
following output should appear:

```

runLogin:
    [echo] running the webLogin client
    [java] webLogin, firing...
    [java] validate: true
    [java] Client returned
    [java] WebUserName: joe sixpack
    [java] SOAPSessionId: some_random_string
    [java] webLogin, completed!!!
```

## Appendix

- Eclipse reference - <http://www.eclipse.org/>
- Custom Ant Tasks - <http://ant.apache.org/manual/develop.html>

---

<a id="tools-idea-idea_plug-in_userguide"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/idea/Idea_plug-in_userguide.html -->

<!-- page_index: 46 -->

# Axis2 Plug-in Guide for IntelliJ IDEA

This document explains the installation and usage of Axis2
plug-in for IntelliJ IDEA.

[[Download
Plug-in]](#download)

## Content

- [Introduction](#tools-idea-idea_plug-in_userguide--intro)
- [Installation](#tools-idea-idea_plug-in_userguide--installation)
- [WSDL2Java Code
  Generation](#tools-idea-idea_plug-in_userguide--wsdl2java_code_generation)
- [Create a Service Archive](#tools-idea-idea_plug-in_userguide--create_service_archive)
  - [Sub Wizard 1 & Sub Wizard 2](#tools-idea-idea_plug-in_userguide--sub12)
  - [Sub Wizard 3](#tools-idea-idea_plug-in_userguide--sub3)

## Introduction

The Axis2 plug-in for IntelliJ IDEA helps users to create
service archives which can be deployed in Axis2, and generate java
classes files from WSDL files. The following section describes the
installation procedure followed by the usage of the plug-in.

**Note:** This plug-in is made up with IDEA Open API which will be
compatible with idea version since build 4121. The plugin also be
compatible with all the builds after build number 4121 and also the
java version should be 1.4 or higher. The provided screen shots may
slightly differ with what the user would actually see but the
functionality has not been changed.

## Installation

First [download](#download) the
plug-in which is a zipped file, and extract it into plugins
directory which is located in the directory where IDEA is
installed. If a previous version of the plug-in resides in this
directory you will have to delete it prior to extracting the new
zip file. If you have extracted the file correctly you would see a
directory called axis2-idea-plugin.

Next step is to restart IDEA so that the changes can take place.
If the plug-in has been installed correctly, you will see following
icons in IDEA when it is restarted.

![Figure 1](assets/images/idea-icons_96be673172e9ef3b.jpg)

Also if you right-click on the IDEA editor you would see a link
to the same plug-in.

![Figure2](assets/images/idea-popup_5421be1645a4e9db.jpg)

When you click on either one of them, a window (Page 1) will
appear asking you to select one of the following two options.

1. [Create a service
   archive](#tools-idea-idea_plug-in_userguide--create_service_archive)
2. [WSDL2Java code
   generation](#tools-idea-idea_plug-in_userguide--wsdl2java_code_generation)

**Page 1:**

![Figure3](assets/images/fig1_281e3700dd8c7e46.jpg)

If you want to create a service archive obviously you must
select "Create a service archive" option. Like wise, if u want to
generate java class file from a WSDL file you must select the radio
button option "WSDL2Java code generation".

## WSDL2Java Code Generation

Select "WSDL2Java code generation" and click on the button "OK"
to generate code from a WSDL file. Then the following window will
appear.

**WSDL2Java Page 2:**

![Figure4](assets/images/fig2_0cdea6da2b8ba2f0.jpg)

Once the WSDL file is selected you will be able to move onto the
next page. The "Browse" button can be used to easily browse for a
file rather than having to type the whole path.

Once the WSDL file is selected, click on the "Next" button which
will take you to the page below.

**WSDL2Java Page 3:**

This page gives the user the option of selecting default or
custom code generation options. There are three default code
generation options in all. The first enables the user to generate
both client and server code under default configurations while the
second generates just the client side under default configurations.
The third option generates server side code under default
configurations.

**Note:**

- When client side code is generated under default configurations
  it generates the stub, compiles it, packages it as a jar (the name
  of the jar will be <service name >-jar) places it in a lib
  folder (If there is no lib folder, it is created) under the IDEA
  project that is opened. This jar that's generated will also be
  added as a project library to the current active IDEA project.
- When server code is generated under default configurations it
  generates the server side code and also generates a default
  service.xml. The user will then be taken to page 5.
- When both server and client side is generated under default
  configurations the client stub is added are a jar to the current
  IDEA project and the user is taken to page 5.

![Figure5](assets/images/fig19_b99fa761fbd7932f.jpg)

**WSDL2Java Page 4:**

**Codegen options** are to be selected here. By far
this is the most important page in this wizard, which determines
the characteristics of the code being generated.

![Figure5](assets/images/fig18_ad331316cb766009.jpg)

**Here's some information on the options for
selection:**

- Output language can be Java, C#. But we have not fully tested
  C# codegeneration, therefore, it is better to select Java as output
  language.
- If the WSDL comprises of several services, the user can select
  the service for which the code should be generated for.
- If the WSDL comprises of several ports for a particullar
  service, the user can select the port which the code should be
  generated for.
- The default data binding type is adb (Axis2 Data Binding).
  Although the tool is capable of providing XML beans, due to class
  loading issues in XML beans, current implementation only generate
  code with OM and ADB.
- As for the package name of the generated code, you can set the
  name as you wish.
- Users can select the one out of the three options- "Generate
  Client Side", "Generate Server Side" and "Generate All". The user
  will be able to select further options based on his options
  selected here. These sub options are explained below.
- - If user selects "Generate Client Side", he can further select
    the service invocation style. Since Axis2 supports both synchronous
    and asynchronous client programming model, the tool has provided a
    way to selecting the invocation style.
  - If user selects "Generate Server Side", he can also generate a
    default service XML file. If the user selects "Generate an
    interface for skeleton" option then it only generates an interface
    for the server side. If so the user has to implement this
    interface. If this option is not selected, the skeleton class is
    generated, which the user can fill in later on.
  - If user selects "Generate All" option, then all the classes
    will be generated in the referenced schemas by the WSDL
    irrespective of elements referred by the WSDL, along with the
    client side code.
- The dafault behaviour of the code generator is to map
  namespaces to package names logically, but if the user wishes to
  change the package names of the generated classes, he can do so by
  changing the values in the Namespace to Packagename mapping
  table.

With these enhanced options novices need not worry about the
options that can be set as the default options cover the most
common cases. Advanced users will find it very easy to turn the
knobs using the custom generation option.

**WSDL2Java Page 5:**

![Figure6](assets/images/fig3_9c9a679b67971bd7.jpg)

Here uses have the option of adding the generated code directly
to their working IDEA project or choose a custom location. If the
user decides to add it to the current IDEA project he/she will have
to choose the module and the source directory that the code should
be generated to.

Alternatively the user can browse and select the output
location/path (the location at which the code is to be generated)
using the "Browse" button. Because of the "Browse" button you do
not need to type in the output file path.

![Fig4](assets/images/fig4_68ccf5081e880511.jpg)

Once an output location is selected you can click on "Finish"
button which will generate the java class file. If code generation
is successful then a message box will appear acknowledging this
fact a shown above.

## Create a Service Archive

Select the "Create a service archive" radio button on Page 1 of
Axis2 IDEA plug-in wizard.

**Page 1:**

![Fig5](assets/images/fig1_281e3700dd8c7e46.jpg)

**Service Archive Page 2:**

The page below will appear asking the user to select the archive
type

![fig6](assets/images/fig6_7f38254d2951264f.jpg)

In Axis2, the user can deploy a single service or a service
group. Therefore, you can select either "Single service archive" or
"Service group archive" for the archive type you want to
create.

If you already have a services.xml you can skip some of the
steps in the wizard by selecting the radio button option "I already
have services.xml" and clicking on "Next" button. If you do not
have the services.xml, select the radio button option "Generate
services.xml" and click on the "Next" button, in which case the
tool will create the services.xml for you.

Depending on the options you selected on this page there can be
three sub wizards:

1. [Sub wizard 1](#tools-idea-idea_plug-in_userguide--sub12) (Generate single service and
   its services.xml)
2. [Sub wizard 2](#tools-idea-idea_plug-in_userguide--sub12) (Generate service group and
   its services.xml)
3. [Sub wizard 3](#tools-idea-idea_plug-in_userguide--sub3) (Generate service/service
   group using already existing services.xml)

1 & 2 follow the same set of steps except for some looping
mechanism in the middle of the wizard.

### Sub Wizard 1 and Sub Wizard 2

**Service Archive (sub wizards 1 & 2) Page
3:**

From this page you have to select the location of the service
classes directory (the location of the compiled classes). You do
not need to type path, simply browse and select.

![fig7](assets/images/fig7_a7936cc8b05b277a.jpg)

When you click on "Next" button, wizard will move to the page
below

**Service Archive (sub wizards 1 & 2) Page
4:**

Here you select service specific external libraries (third party
libraries) and service WSDL files. If you want to add multiple WSDL
files to a single service type you can do that as well.

![fig8](assets/images/fig8_e6760c25b997a2e8.jpg)

To add libraries first click on the browse button to browse for
library files and then click on the "Add" button. Once added the
selected file will appear in the list box.

To add WSDLs, first click on the browse button to browse for
WSDL file and then click the "Add" button to add the file to the
list.

After adding external libraries and service WSDL files click on
the "Next" button to move to next page.

**Service Archive (sub wizards 1 & 2) Page
5:**

This page allows you to select service implementation class. In
the case of service group, same page will be looped to select
multiple service implementation classes. This process is explained
in detail below.

Select a service implementation class by browsing and clicking
on the "Load" button to load all the public methods in that class, after which you can select the methods that you want to publish
using the check boxes.

**Note :** If you do not select the correct class
path from the "Class location selection" window, the public methods
which are available in the selected class file will not be
loaded.

![fig10](assets/images/fig10_89a3645fd80fd27d.jpg)

In "Service Name" text box you can type the name of the service
you want, but remember that the service name should be unique
throughout the system.

When you have completed this particular service click on the
button "Next". In the case of a service group when you click on the
"Next" button for that particular service the following dialog box
will appear with option to add more service(s) to a service
group.

![fig11](assets/images/fig11_eab10f6181eba796.jpg)

If you click on "Yes", you have to follow the same procedure to
add some other service(s) to service group.

If you click on "No", the button "Next" will be enabled and you
can go to next page.

***Note: From this point
onwards the steps are similar to all the sub
wizards.***

**Service Archive (sub wizards 1 & 2) Page
6:**

This page displays the services.xml file, either the one given
by you (in the case of I already have services.xml)
or the one generated by the system (in the case of "generate
services.xml")

![fig12](assets/images/fig12_439b6e99a182ac49.jpg)

This page is editable and provide a way to add parameters and
module references to any level.

**Note :** When you click on either the
"+Parameter" or the "+ModuleRef" buttons remember that
corresponding text will be added to the current mouse position.
Therefore, click on the location you want to add the parameter or
module references and then click relevant button (+Parameter or
+ModuleRef).

**+Parameter button:**

If you click on the "+Parameter" button a window will appear
asking to give parameter name and parameter value.

![fig13](assets/images/fig13_88babe55cd8286aa.jpg)

Note that you can also manually add parameters (without clicking
on the "+Parameter" button ) to any where in the document as you
wish.

**+ModuleRef button:**

Likewise, adding module references can be done by clicking on
the "+ModuleRef" button in the page. You have to type the name of
the module to be engaged as shown in the following figure.

![fig14](assets/images/fig14_0df39498d410eba9.jpg)

When you complete this page press the "Next" button to go to
final page.

**Service Archive (sub wizards 1 & 2) Page
7:**

![fig15](assets/images/fig15_fa7398827c45cd9b.jpg)

Next step is to select output file location, the location in
which archive file should be created.

In the "Archive Name" text box, type the name of the archive
file you want to place. This name will finally become the service
group name.

**Note :** Do not include file extension when you
type archive name. System will generate that for you.

When you are done, click the "Finish" button. If everything has
been done successfully you will see following message.

![fig16](assets/images/fig16_9ea0263c54544edc.jpg)

***Note: Pages 6 & 7 of sub wizards 1 & 2 are
common to sub wizard 3 from its page 3 onwards.***

### Sub Wizard 3

In the case where services.xml is already available, the steps
are as follows:

**Service Archive (sub wizard 3) Page 3:**

![fig17](assets/images/fig17_636c2de8762c89b3.jpg)

This page allows you to select both location of services.xml and
the location of service classes directory. Click on the "Select"
buttons and browse the file system to find required document and
location.

Click on the "Next" button which will take you to a page which
allows you to add third party libraries and WSDL's in the same
manner as "Sub Wizard 1 & Sub Wizard 2" section's [Page 6 - Edit service descriptors](#tools-idea-idea_plug-in_userguide--note). Note that Sub Wizard
3 from this point takes the same pages as 6 to 7 of Sub Wizards 1
& 2.

---

<a id="tools-eclipse-servicearchiver-plugin"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/eclipse/servicearchiver-plugin.html -->

<!-- page_index: 47 -->

# Service Archive Generator Wizard Guide for Eclipse Plug-in

This document will guide you through the installation and usage
of the archive generator Eclipse plug-in.

[[Download Plugin Tool]](#download)

- [Service Archive Generator Wizard Guide for Eclipse Plug-in](#tools-eclipse-servicearchiver-plugin--service_archive_generator_wizard_guide_for_eclipse_plug-in)
  - [Introduction](#tools-eclipse-servicearchiver-plugin--introduction)
  - [Installation](#tools-eclipse-servicearchiver-plugin--installation)
  - [Operation](#tools-eclipse-servicearchiver-plugin--operation)
  - [Appendix](#tools-eclipse-servicearchiver-plugin--appendix)

# Introduction

As part of the Axis2 tool set, the service archive generator is
an important tool that allows the generation of service archives
("aar" file or a "jar" files) that can be deployed as a web
services to the Axis2.

# Installation

Installation instructions for the plugin can be found
[here](https://axis.apache.org/axis2/java/core/tools/eclipse/plugin-installation.html).

# Operation

If the plug-in is properly installed you should see a new wizard
under the "New" section. (Use the File -> New -> Other or
Ctrl + N )

![ServiceWizardSelection](assets/images/servicewizardselection_54233189a186b68a.jpg)

Selecting the wizard and pressing the "Next" button will start
the service generator wizard. Following is the first page of the
wizard.

**Page 1:**

![ServicePage1](assets/images/servicepage1_61f9debaabbfb4e5.jpg)

Once the class file folder(which should be a folder in the
file system) is browsed and selected, the "Next" button will be
enabled and you can move to the next page. Note that you have the
option of either including all the files or the class files only of
the folder on page 1.

**Page 2:**

Page 2 of the wizard as seen below requires you to locate/browse
the WSDL file. If you do not wish to add a WSDL file to the service
archive, select skip WSDL, else you can select the location of the
WSDL file by selecting the select WSDL option.

![service_page2](assets/images/service-page2_76073de2f89ce822.jpg)

**Page 3:**

Select the services.xml file on this wizard page by browsing or
select the option of generating service xml automatically, after
which you can click "Next" button to go to the next page. Notice
how the browsing option disables when the "Generate service xml
automatically" check box is ticked.

![service_page3](assets/images/service-page3_44d8f95246c8721b.jpg)

**Page 4:**

The next step is to add the libraries. The library addition page
looks like this :

![service_page5](assets/images/service-page5_92f4585b2da5f677.jpg)

The library name (with full path) can be either typed on the
text box or browsed for using the "Browse" button.

![service_page5_browsed](assets/images/service-page5-browsed_46d7d9fb10fff6d4.jpg)

Once there is a library name with full path on the text box, hit
the "Add" button to add the library to the list. Added libraries
should be displayed in the "Added libraries" list box. This way you
can add as many external libraries as you wish. See the screen
shots below.

![service_page5_hl](assets/images/service-page5-hl_62a2d13561cce76b.jpg)

![service_page5_added](assets/images/service-page5-added_522bc1103df2ed4f.jpg)

If any added library needs to be removed, highlight it or in
other words, select it from the "Added libraries" list and hit on
the "Remove" button as shown below. Click on the "Next" button to
proceed to the last page of the wizard if the user did not select
to auto generate the services.xml file. If user select to auto
generate the services.xml file then the services.xml option page
will be displayed.

![service_page5_remove](assets/images/service-page5-remove_703dea75bc2a1f19.jpg)

**Page 5:**

This page only appears if the user select to generate the
services.xml at page 3 of the wizard. If the user have selected a
services.xml then the user will be directed to the last page of the
wizard.

After entering the correct service name and valid fully
qualified class name, try to load the existing methods of that
class by clicking the load button.

![service_page4_load](assets/images/service-page4-load_e9f3ee8864069d7d.jpg)

If successfully loaded the user will be presented with a table
at the bottom of the page with the details of the loaded class. By
checking and unchecking the user can select the necessary methods
to include in the services.xml

![service_page4_table](assets/images/service-page4-table_c458e92d7880f551.jpg)

By clicking on the search declared method only check box, the
user can remove the inherited methods from the class. Click on the
"Next" button to proceed to the last page of the wizard

![service_page4_search_declared](assets/images/service-page4-search-declared_9866751b03aa84fb.jpg)

**Page 6:**

The last page of the wizard asks for the output file location
and the output archive file name. To be able to finish the wizard, user must enter valid output file location and output file
name.

![service_page6](assets/images/service-page6_e3b19a3c40231eb1.jpg)

Once all the parameters are filled, hit the "Finish" button to
complete the wizard and generate the service archive.

![success_msg](assets/images/success-msg_244ae7415ca2850c.jpg)

If you see the above message, then you've successfully generated
the service archive! This service archive can be hot deployed
(deployed at run time) to the axis2

# Appendix

- Eclipse reference - <http://www.eclipse.org/>
- Custom Ant Tasks - <http://ant.apache.org/manual/develop.html>

---

<a id="tools-eclipse-wsdl2java-plugin"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/eclipse/wsdl2java-plugin.html -->

<!-- page_index: 48 -->

# Update: The Code generator plugin for Eclipse is broken. The docs as well as the code are outdated. If interested in contributing a fix, see Jira issue AXIS2-5955.

This document explains the usage of this code generator plug-in
for Eclipse. In other words, this document will guide you through
the operations of generating a WSDL file from a Java class and/or
generating a Java class file from a WSDL file.

[[Download Plugin Tool]](#download)

- [Update: The Code generator plugin for Eclipse is broken. The docs as well as the code are outdated. If interested in contributing a fix, see Jira issue AXIS2-5955.](#tools-eclipse-wsdl2java-plugin--update.3a_the_code_generator_plugin_for_eclipse_is_broken._the_docs_as_well_as_the_code_are_outdated._if_interested_in_contributing_a_fix.2c_see_jira_issue_axis2-5955.)
  - [Introduction](#tools-eclipse-wsdl2java-plugin--introduction)
  - [Installation](#tools-eclipse-wsdl2java-plugin--installation)
  - [Operation](#tools-eclipse-wsdl2java-plugin--operation)
    - [WSDL2Java](#tools-eclipse-wsdl2java-plugin--wsdl2java)
    - [Java2WSDL](#tools-eclipse-wsdl2java-plugin--java2wsdl)
  - [Appendix](#tools-eclipse-wsdl2java-plugin--appendix)

# Introduction

The Axis2 code generator comes built-in with an [Eclipse](http://www.eclipse.org) plug-in. This plug-in can be
used to generate a WSDL file from a java class (Java2WSDL) and/or a
java class file from a WSDL (WSDL2Java). First you need to install
the plug-in. The instructions for the installation process are
given below.

# Installation

Installation instructions for the plugin can be found
[here](https://axis.apache.org/axis2/java/core/tools/eclipse/plugin-installation.html).

# Operation

## WSDL2Java

If the plug-in is properly installed you should see a new wizard
under the "New" section.(use the File -> New -> Other or Ctrl
+ N )

![wsdl2java-screen0](assets/images/wsdl2java-screen0_4c9d38a0150d70a4.png)

Selecting the wizard and pressing the "Next" button will start
the code generator wizard. Following is the first wizard page.

**Page 1:**

![wsdl2java-screen1](assets/images/wsdl2java-screen1_7fc78dfd27a52a0a.png)

Selecting the "Generate Java source code from WSDL file" option
and clicking "Next" leads to the following page.

**WSDL2Java Page 2 :**

![wsdl2java-screen2](assets/images/wsdl2java-screen2_a154f0719deb95d9.png)

To move on to the next page the WSDL file location must be
given. The "Browse" button can be used to easily browse for a file
rather than typing the whole path.

**WSDL2Java Page 3 :**

Once the WSDL file is selected, the next page will take you to
the page from where **codegen options** are to be
selected. By far this is the most important page in this wizard.
This page determines the characteristics of the code being
generated.

Novices need not worry about these options since the most common
options are defaulted, but advanced users will find it very easy to
turn the knobs using these options.

![wsdl2java-screen3](assets/images/wsdl2java-screen3_8db5a39b14724c75.png)

What advanced users can do is select custom from the select
codegen options drop down list and then change/edit the fields that
you need.

![wsdl2java-screen31](assets/images/wsdl2java-screen31_d87ad183a28fd79e.png)

Once the options are selected, only the final step of the code
generation is left which is the selection of the output file
location.

**WSDL2Java Page 4 :**

Here you can select the output file path by typing or browsing
using the "Browse" button. You have the option of browsing only
eclipse workspace projects by selecting the "Add the source to a
project on current eclipse workspace" radio button. Or else you
have the option to save the codegen resutls to file system

![wsdl2java-screen4](assets/images/wsdl2java-screen4_697e0e701e00e444.png)

Here also you have the option to add some value to the codegen
results. If you have enabled the check box "Add Axis2 libraries to
the codegen result project" then all other controls below will get
enabled. What you can do is point the downloaded Axis2\_HOME
location via the "Browse" button. Then you can verify the
availability of the Axis2 libs by clicking on the "Check Libs"
button. If all goes well then you can add the axis 2 libs to the
codegen results location. Another option is available to generate a
jar file if the user needs to add the codegen results to a project
as a compiled jar file to the selected locations lib directory.

![wsdl2java-screen41](assets/images/wsdl2java-screen41_0a944dacd76a6ab3.png)

When the output file location is selected, the "Finish" button
will be enabled. Clicking the "Finish" button will generate the
code and a message box will pop up acknowledging the success. Well
Done! You've successfully completed Axis2 code generation.

## Java2WSDL

**Page 1:**

For this operation you need to select the option which says
"Generate a WSDL from a Java source file"

![java2wsdl-screen0](assets/images/java2wsdl-screen0_7bba0e5f76c4a369.png)

Then click the "Next" button which will lead to the next page
below.

**Java2WSDL Page 2:**

![java2wsdl-screen1](assets/images/java2wsdl-screen1_a90afdc81ade993a.png)

In this page one needs to select the class to be exposed and the
relevant jar files /classes to be loaded as the classpath. After
the libraries have been set, the "Test Class Loading" button must
be clicked in order to test whether the class is loadable. Unless
the class loading is successful proceeding to the "Next" button
will not be enabled.

Once the classloading is successful and "Next" button is clicked
the page below will appear.

**Java2WSDL Page 3:**

This page allows the parameters to be modified by setting the
options for the generator.

![java2wsdl-screen2](assets/images/java2wsdl-screen2_730f9f3bff1522fc.png)

**Java2WSDL Page 4:**

Here you can select the output file path by typing or browsing
using the "Browse" button. You have the option of browsing only
Eclipse workspace projects by selecting the "Add the source to a
project on current eclipse workspace" radio button . Or else you
have the option to save the codegen resutls to file system. Once
the output file location and the output WSDL file name is added you
can click the "Finish" button to complete generation.

![java2wsdl-screen3](assets/images/java2wsdl-screen3_3940958e76e0a9b6.png)

If a message box pops up acknowledging the success, then you've
successfully completed the Java2WSDL code generation.

# Appendix

- Eclipse reference - <http://www.eclipse.org/>
- Custom Ant Tasks - <http://ant.apache.org/manual/develop.html>

---

<a id="tools-maven-plugins-maven-aar-plugin"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/maven-plugins/maven-aar-plugin.html -->

<!-- page_index: 49 -->

# Maven2 AAR Plug-in Guide

## Introduction

This plugin generates an Axis 2 service file (AAR file).

[[Download Plugin Tool]](#tools)

## Goals

The AAR plugin allows the packaging of an Axis 2 service aar in
3 different modes:

1. **axis2-aar:aar**: generates the aar artifact
2. **axis2-aar:inplace** : package the aar in the source tree
3. **axis2-aar:exploded** : package an exploded aar application

Each mode is materialized by a goal. For instance, to generate
an exploded aar from the current project, one would type

```

mvn axis2-aar:exploded
```

## Configuration

All AAR plugin goals takes the following configuration
parameters as input:

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Default Value** | **Description** |
| aarDirectory | ${project.build.directory}/aar | Directory where the aar file is built |
| classesDirectory | ${project.build.outputDirectory} | Directory with compiled classes and resources |
| fileSets |  | Additional file sets, which are being added to the archive. See "[File Sets](#tools-maven-plugins-maven-aar-plugin--file_sets)" below for an example |
| servicesXmlFile |  | Location of the services.xml file. By default, it is assumed that the file is already present in classesDirectory/META-INF and no special processing is required |
| wsdlFile |  | Location of the WSDL file. By default, it is assumed that the file is already present in classesDirectory/META-INF and no special processing is required |
| wsdlFileName | service.wsdl | Name, to which the WSDL file should be mapped |

### The aar Goal

The aar goal allows the following additional parameters:

|  |  |  |
| --- | --- | --- |
| **Parameter Name** | **Default Value** | **Description** |
| outputDirectory | ${project.build.directory} | Directory where to generate the AAR file |
| aarName | ${project.build.finalName} | The generated AAR files name |
| archive |  | A Maven archive configuration. This allows, for example, to configure the MANIFEST.MF file |
| classifier |  | A classifier, which should be added to the generated AAR files name. Setting this parameter has the side effect, that the artifact is treated as an attachment and not as the projects primary artifact |
| primaryArtifact | true | Setting this property to false disables installation or deployment of the artifact as the projects primary artifact |

### File Sets

Additional file sets may be configured for inclusion into the
AAR file. A file set looks as follows:

```

  
  <fileSets>
    <fileSet>
      <directory>src/aar/files</directory>
      <outputDirectory>META-INF/docs</outputDirectory>
      <includes>
        <include>**/*.html</include>

      </includes>
    </fileSet>
    <fileSet>
      <directory>src/aar/files</directory>
      <outputDirectory>META-INF/etc</outputDirectory>

      <excludes>
        <exclude>**/*.html</exclude>
      </excludes>
    </fileSet>
  </fileSets>
  
```

The example specifies, that the contents of the directory
src/aar/files shall be added to the AAR file. HTML files will go
into META-INF/docs, all other files to META-INF/etc.

A file set is configured through the following configuration
parameters:

|  |  |
| --- | --- |
| **Parameter Name** | **Description** |
| directory | The directory, from which to read the file set. This parameter is required |
| outputDirectory | The target directory within the AAR file. Defaults to the AAR files root directory |
| includes | Configures the set of files, which shall be included into the AAR file. Defaults to \*\*/\* |
| excludes | Configures a set of files, which shall be excluded from the file set. Defaults to the Maven default excludes (\*\*/\*~, \*\*/cvs/\*\*/\*, \*\*/.svn/\*\*/\*, etc.) |
| skipDefaultExcludes | If this parameter is set to true, then no default excludes are being used |

---

<a id="tools-maven-plugins-maven-java2wsdl-plugin"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/maven-plugins/maven-java2wsdl-plugin.html -->

<!-- page_index: 50 -->

# Maven2 Java2WSDL Plug-in Guide

## Introduction

This plugin takes as input a Java class and generates a WSDL, which describes a Web service for invoking the classes methods.

[[Download Plugin Tool]](#tools)

## Goals

The Java2WSDL plugin offers a single goal:

- java2wsdl (default): Reads a java class and generates a WSDL
  for invoking the classes methods as a Web service.

To run the plugin, add the following section to your [POM](http://maven.apache.org/guides/introduction/introduction-to-the-pom.html) (Project Object Model):

```

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.axis2</groupId>
        <artifactId>axis2-java2wsdl-maven-plugin</artifactId>
        <configuration>
          <className>com.foo.myservice.MyHandler</className>
        </configuration>
        <executions>
          <execution>
            <goals>
              <goal>java2wsdl</goal>
            </goals>
          </execution>
         </executions>
      </plugin>
    </plugins>
  </build>
  
```

The plugin will be invoked automatically in the
generate-resources phase. You can also invoke it directly from the
command line by running the command:

```

mvn axis2-java2wsdl:java2wsdl
```

### The Java2WSDL Goal

By default, the plugin reads the given Java class and creates a
file
**target/generated-resources/java2wsdl/service.wsdl**.
The Java class is given by the configuration element
**className** above.

## Configuration

The Java2WSDL goal takes the following parameters as input. All
parameters can be set from the command line by using properties.
For example, the parameter "className" may be set using the
property "axis2.java2wsdl.className". If the parameter isn't set
via property or in the POM, then a default value applies.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter name** | **Command line property** | **Description** | **Default value** |
| className | ${axis2.java2wsdl.className} | Fully qualified name of the class, which is being read and transformed into a WSDL |  |
| outputFileName | ${axis2.java2wsdl.outputFileName} | Path of the generated service file. |  |
| schemaTargetNamespace | ${axis2.java2wsdl.schemaTargetNamespace} | Target namespace of the generated schema. |  |
| schemaTargetNamespacePrefix | ${axis2.java2wsdl.schemaTargetNamespacePrefix} | Prefix, which is being associated with the schemas target namespace. |  |
| serviceName | ${axis2.java2wsdl.serviceName} | Name of the generated Web service. | Unqualified name of the input class. |
| targetNamespace | ${axis2.java2wsdl.targetNamespace} | Target namespace of the generated WSDL | Default namespace |
| targetNamespacePrefix | ${axis2.java2wsdl.targetNamespacePrefix} | Prefix, which is being associated with the target namespace |  |

---

<a id="tools-maven-plugins-axis2-wsdl2code-maven-plugin"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/maven-plugins/axis2-wsdl2code-maven-plugin/index.html -->

<!-- page_index: 51 -->

## About

This plugin takes as input a WSDL and generates client and server stubs for calling or implementing a web service matching the WSDL.

The full description of goals is available [here](#tools-maven-plugins-axis2-wsdl2code-maven-plugin-plugin-info).

---

<a id="docs-migration"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/migration.html -->

<!-- page_index: 52 -->

# Migrating from Apache Axis 1.x to Axis2

This document is intended for helping Axis 1.x users migrate to
the Axis2 series. We'll begin by listing the improvements in Axis2
in comparison with Axis1. This will be followed by guidelines for
migration to the new version.

*Send your feedback or questions to: [java-user@axis.apache.org](mailto:java-user@axis.apache.org?subject=[Axis2])*.
(Subscription details are available on the [Axis2 site](#mail-lists).)
Kindly prefix subject with [Axis2].

## Content

- [Compatibility](#docs-migration--comp)
- [Getting Started](#docs-migration--start)
- [Custom Deployment of Services,
  Handlers and Modules](#docs-migration--custom_deployment)
- [Transports for HTTP Connection](#docs-migration--transports)
- [Data Binding Support](#docs-migration--data_binding)
- [Best Usage](#docs-migration--best)

## Compatibility

Axis1.x and Axis2 have evolved from different architectures.

**Speed** - Axis2 is based on the StAX API, which
gives greater speed than the SAX event based parsing used in
Axis1.x.

**Stability** - Axis2 has fixed phases as well as
user-defined phases for extensions. This allows far more stability
as well as flexibility than Axis1.x.

**Transport framework** - Transports (i.e., senders
and listeners for SOAP over various protocols such as HTTP, SMTP, etc.), have been abstracted away from the Axis2 engine. Having a
transport-independent Axis engine allows far more flexibility in
transport options.

**WSDL 2.0 support** - Axis2 supports both WSDL
versions 1.1 and 2.0, which are used by Axis2's code generation
tools to create web service skeletons and client stubs.

**Component-oriented architecture** - Axis2
components consist of handlers and modules in .mar and .aar
archives. These easily reusable components allow extended
functionality such as pattern processing for your applications or
distribution to partners. Axis2 emphasizes the "Module" concept
over the "Handler" concept of Axis 1.x. Modules contain handlers
that are ordered by phase rules. These are attached to specific
service(s).

## Getting Started

Let's look at a simple example of echoing at client API.

**Axis 1.x**

```

import org.apache.axis.client.Call;
import org.apache.axis.client.Service;
import javax.xml.namespace.QName;
   
public class TestClient {
  public static void main(String [] args) {
    try {
      String endpoint ="http://ws.apache.org:5049/axis/services/echo";
      Service  service = new Service();
      Call     call    = (Call) service.createCall();
      call.setTargetEndpointAddress( new java.net.URL(endpoint) );
      call.setOperationName(new QName("http://soapinterop.org/", "echoString"));
      String ret = (String) call.invoke( new Object[] { "Hello!" } );
      System.out.println("Sent 'Hello!', got '" + ret + "'");
    } catch (Exception e) {
       System.err.println(e.toString());
    }
  }
}
```

**Axis 2**

```

import org.apache.axiom.om.OMAbstractFactory;
import org.apache.axiom.om.OMElement;
import org.apache.axiom.om.OMFactory;
import org.apache.axiom.om.OMNamespace;
import org.apache.axis2.AxisFault;
import org.apache.axis2.addressing.EndpointReference;
import org.apache.axis2.client.Options;
import org.apache.axis2.client.ServiceClient;


public class EchoBlockingClient {
        private static EndpointReference targetEPR = new EndpointReference(
                        "http://127.0.0.1:8080/axis2/services/MyService");
        public static void main(String[] args) {
                try {
                        OMFactory fac = OMAbstractFactory.getOMFactory();
                        OMNamespace ns = fac.createOMNamespace("http://soapinterop.org/", "ns1");
                        OMElement payload = fac.createOMElement("echoString", ns);
                        payload.setText("Hello!");
                        Options options = new Options();
                        ServiceClient client = new ServiceClient();
                        options.setTo(targetEPR);
                        client.setOptions(options); 
                        //Blocking invocation
                        OMElement result = client.sendReceive(payload);
                        System.out.println("Sent Hello, got : " + result.toString());

                } catch (AxisFault axisFault) {
                        axisFault.printStackTrace();
                }

        }
}
```

The above code demonstrates that Axis2 service invocations deal
with the SOAP body element itself. The simple shows a synchronous
invocation, but Axis2 can handle asynchronous invocations as well.
The "payload" variable above contains the SOAP body element which
will go in the SOAP envelope.

Once the service is called by the client stub in Axis2, the
"payload" will be bound according to the data binding framework in
use. So the extra work of parsing the "payload" will vanish.

Axis2 supports asynchronous invocation through
sendReceiveNonblocking(). Synchronous/Asynchronous invocations can
handle both single and double HTTP connections.

With this advanced architecture, Axis2 is capable of handling
megabytes of requests and responses, well above the capabilities of
Axis1.x.

## Custom Deployment of Services, Handlers, and Modules

In Axis 1.x, the deployment of services was via the rather
cumbersome WSDD. Service deployment in Axis2 is straightforward and
dynamic using the web-based Axis2 Admin application. Deployment is
just a matter of creating the service archive (.aar) file and
deploying it. More details regarding this is given in the Axis2
user guide.

Axis2 has moved away from the "Handler concept" and is more into
the "Module concept". Abstractly speaking, the module concept is a
collection of handlers with rules that govern which modules are
created as .mar files. It uses a module.xml file to specify handler
configuration and activation.

When a service is called through a handler, it is just a matter
of giving a reference to the module that includes the handler in
the services.xml (using <module ref="foo/>").

Services are hot deployable in Axis2, but modules are not. This
is one feature which is unique to Axis2.

Let's take a detailed look at what it takes to migrate the Axis
1.x handlers to the Axis 2 modules via the "SOAP Monitor". The SOAP
monitor is really a combination of three components: An applet
which displays responses/requests, a servlet which binds to a
default port of 5001 and connects to the applet, and a handler
chain used to intercept the SOAP messages. Here we'll focus on the
handler.

**Axis 1.x required two WSDD's to use the SOAP Monitor. First, the SOAP Monitor Handler itself:**

```

<deployment xmlns="http://xml.apache.org/axis/wsdd/"
    xmlns:java="http://xml.apache.org/axis/wsdd/providers/java">
    
  <handler name="soapmonitor" 
      type="java:org.apache.axis.handlers.SOAPMonitorHandler">
    <parameter name="wsdlURL" 
      value="/wzs/SOAPMonitorService-impl.wsdl"/>
    <parameter name="namespace" 
      value="http://tempuri.org/wsdl/2001/12/SOAPMonitorService-impl.wsdl"/>
    <parameter name="serviceName" value="SOAPMonitorService"/>
    <parameter name="portName" value="Demo"/>
  </handler>

  <service name="SOAPMonitorService" provider="java:RPC">
    <parameter name="allowedMethods" value="publishMessage"/>
    <parameter name="className" 
      value="org.apache.axis.monitor.SOAPMonitorService"/>
    <parameter name="scope" value="Application"/>
  </service>
</deployment>
```

**Axis 1.x requires a reference to the handler in the user's
WSDD that defines their Web Service:**

```

<deployment name="example" xmlns="http://xml.apache.org/axis/wsdd/" 
    xmlns:java="http://xml.apache.org/axis/wsdd/providers/java">
  
  <service name="urn:myService" provider="java:RPC">
    <parameter name="className" value="org.MyService"/>
    <parameter name="allowedMethods" value="*"/>

    <requestFlow>
      <handler type="soapmonitor"/>
    </requestFlow>
    <responseFlow>
      <handler type="soapmonitor"/>
    </responseFlow>

  </service>
</deployment>
```

**Axis 2 requires a module.xml, placed inside a jar with a .mar
extension under WEB-INF/modules, to define a Handler:**

```

<module name="soapmonitor" class="org.apache.axis2.handlers.soapmonitor.SOAPMonitorModule">
    <inflow>
        <handler name="InFlowSOAPMonitorHandler" class="org.apache.axis2.handlers.soapmonitor.SOAPMonitorHandler">
            <order phase="soapmonitorPhase"/>
        </handler>
    </inflow>

    <outflow>
        <handler name="OutFlowSOAPMonitorHandler" class="org.apache.axis2.handlers.soapmonitor.SOAPMonitorHandler">
            <order phase="soapmonitorPhase"/>
        </handler>
    </outflow>

    <Outfaultflow>
        <handler name="FaultOutFlowSOAPMonitorHandler" class="org.apache.axis2.handlers.soapmonitor.SOAPMonitorHandler">
            <order phase="soapmonitorPhase"/>
        </handler>
    </Outfaultflow>

    <INfaultflow>
        <handler name="FaultInFlowSOAPMonitorHandler" class="org.apache.axis2.handlers.soapmonitor.SOAPMonitorHandler">
            <order phase="soapmonitorPhase"/>
        </handler>
    </INfaultflow>
</module>
```

The SOAPMonitorModule referenced above simply implements the
org.apache.axis2.modules.Module, and is used for any additional
tasks needed to initialize the module and shutdown the module. In
this situation, nothing is needed and the implemented interface
methods have blank bodies. Furthermore, the 'soapmonitorPhase' will
be used later (below) in the axis2.xml .

**Axis 1.x the SOAPMonitorHandler has the class signature
as:**

```

public class SOAPMonitorHandler extends BasicHandler
```

**Axis 2 the SOAPMonitorHandler has the class signature
as:**

```

public class SOAPMonitorHandler extends AbstractHandler 
```

**In Axis2, you need to reference the module that contains the
handler chain that you want to use inside your
services.xml:**

```

<service name="ExampleService">
    <module ref="soapmonitor"/>
    <description>
       This service has the SOAP Monitor wired in 
    </description>
    <parameter name="ServiceClass">org.ExampleService</parameter>
    <operation name="myExecute">
        <messageReceiver class="org.apache.axis2.receivers.RawXMLINOutMessageReceiver"/>
    </operation>
</service>
```

**Finally, Axis2 requires you to make some changes to
axis2.xml. Start by adding a global module:**

```

    <module ref="soapmonitor"/>
```

**Then define your phase orders for the 'soapmonitorPhase'
referenced in the module.xml :**

```

    <phaseOrder type="inflow">
        <!--  Global Phases       -->
        <phase name="TransportIn"/>
        <phase name="PreDispatch"/>
        <phase name="Dispatch" class="org.apache.axis2.engine.DispatchPhase">
            <handler name="AddressingBasedDispatcher"
                     class="org.apache.axis2.dispatchers.AddressingBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="RequestURIBasedDispatcher"
                     class="org.apache.axis2.dispatchers.RequestURIBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPActionBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPActionBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>

            <handler name="SOAPMessageBodyBasedDispatcher"
                     class="org.apache.axis2.dispatchers.SOAPMessageBodyBasedDispatcher">
                <order phase="Dispatch"/>
            </handler>
            <handler name="InstanceDispatcher"
                     class="org.apache.axis2.engine.InstanceDispatcher">
                <order phase="Dispatch"/>
            </handler>
        </phase>
        <!--    Global Phases     -->
        <!--   After Dispatch phase module author or service author can add any phase he wants      -->
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
    </phaseOrder>
    <phaseOrder type="outflow">
        <!--   user can add his own phases to this area  -->
        <!--   Global phases   -->
        <!--   these phases will run irrespective of the service   -->
        <phase name="MessageOut"/>
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
        <phase name="PolicyDetermination"/>
        <!--   Global phases   -->
    </phaseOrder>
    <phaseOrder type="INfaultflow">
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
        <!--   user can add his own phases to this area  -->
    </phaseOrder>
    <phaseOrder type="Outfaultflow">
        <!--   user can add his own phases to this area  -->
        <!--   Global phases   -->
        <phase name="MessageOut"/>
        <phase name="userphase1"/>
        <phase name="soapmonitorPhase"/>
        <phase name="PolicyDetermination"/>
        <!--   Global phases   -->
    </phaseOrder>
```

See the user guide for more information on Axis2 modules.

## Transports for HTTP Connection

Axis2 comes with the HTTPClient5TransportSender which is based
on Apache Httpcomponents.

It should be noted that axis2.xml should be configured to call
the commons transports in this manner:

```

...
<transportSender name="http" class="org.apache.axis2.transport.http.impl.httpclient5.HTTPClient5TransportSender"> 
   <parameter name="PROTOCOL">HTTP/1.1</parameter>
   <parameter name="Transfer-Encoding">chunked</parameter>
</transportSender>
...
```

## Data Binding Support

ADB is used to provide data binding support. In Axis2, XML is
manipulated via AXIOM, which is based on the StAX API. AXIOM
provides full XML schema support. Thus, serialization and
de-serialization of XML is handled in Axis2 via the xml-data
binding framework.

Below is an example of migrating a WSDL based Axis 1.x Web
Service to Axis2.

First, let's take a look at a simple document/literal style WSDL
used in an Axis 1.x Web Service. This example assumes the name
simple.wsdl for the WSDL below:

```

<?xml version="1.0" encoding="UTF-8"?>

<definitions name="SimpleService" targetNamespace="http://simpleNS" xmlns:tns="http://simpleNS" 
xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:ns2="http://simpleNS/types">
  <types>
    <schema targetNamespace="http://simpleNS/types" xmlns:tns="http://simpleNS/types" 
xmlns:soap11-enc="http://schemas.xmlsoap.org/soap/encoding/" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
xmlns="http://www.w3.org/2001/XMLSchema">
      <import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>
      <element name="simpleLogin">
        <complexType>
          <sequence>
            <element name="user_name" type="xsd:string"/>
            <element name="user_password" type="xsd:string"/>
          </sequence>
        </complexType>
      </element>
      <element name="simpleLoginResponse">
        <complexType>
          <sequence>
            <element name="soap_session_id" type="xsd:string"/>
            <element name="web_user_name" type="xsd:string"/>
          </sequence>
        </complexType>
      </element>
</schema></types>
  <message name="SimpleEndpoint_simpleLogin">
     <part name="parameters" element="ns2:simpleLogin"/>
  </message>
  <message name="SimpleEndpoint_simpleLoginResponse">
    <part name="result" element="ns2:simpleLoginResponse"/>
  </message>
  <portType name="SimpleEndpoint">
    <operation name="simpleLogin">
      <input message="tns:SimpleEndpoint_simpleLogin" name="SimpleEndpoint_simpleLogin"/>
      <output message="tns:SimpleEndpoint_simpleLoginResponse" name="SimpleEndpoint_simpleLoginResponse"/>
    </operation>
  </portType>
  <binding name="SimpleEndpointBinding" type="tns:SimpleEndpoint">
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" style="document"/>
    <operation name="simpleLogin">
      <soap:operation soapAction="simpleLogin"/>
      <input name="SimpleEndpoint_simpleLogin">
        <soap:body use="literal"/>
      </input>
      <output name="SimpleEndpoint_simpleLoginResponse">
        <soap:body use="literal"/>
      </output>
    </operation>
  </binding>
  <service name="SimpleService">
    <port name="SimpleEndpointPort" binding="tns:SimpleEndpointBinding">
      <soap:address location="http://localhost:8080/axis/services/SimpleEndpointPort"/></port></service></definitions>
```

The next step is to run WSDL2Java on the wsdl. For axis 1.x, this example uses the following Ant task:

```

<target name="wsdl2java" description="axis 1.x">
       <delete dir="output" />
       <mkdir dir="output" />
       <axis-wsdl2java
         output="output"
         verbose="true"
         url="wsdl/simple.wsdl"
         serverside="true"
         skeletondeploy="true"
         nowrapped="true">
       </axis-wsdl2java>
   </target>
```

The Axis 1.x Ant task above takes the simple.wsdl under the
directory 'wsdl' , and from that creates files under the directory
'output'. The files created are shown below:

```

output/
output/simpleNS
output/simpleNS/types
output/simpleNS/types/SimpleLoginResponse.java
output/simpleNS/types/SimpleLogin.java
output/simpleNS/SimpleEndpoint.java
output/simpleNS/SimpleEndpointBindingStub.java
output/simpleNS/SimpleEndpointBindingSkeleton.java
output/simpleNS/SimpleEndpointBindingImpl.java
output/simpleNS/SimpleService.java
output/simpleNS/SimpleServiceLocator.java
output/simpleNS/deploy.wsdd
output/simpleNS/undeploy.wsdd
```

Now let's run WSDL2Java with Axis2. In this example, the only
change to simple.wsdl required for Axis2 is that 'soap:address
location' be changed to:

```

<soap:address location="http://localhost:8080/axis2/services/SimpleEndpoint"/></port></service></definitions>
```

In Axis2, the default databinding uses ADB. However, XMLBeans, JiBX and JAXB-RI are also supported. This example uses XMLBeans. For
Axis2, our example uses the following Ant task:

```

<target name="wsdl2java">
      <delete dir="output" />
      <java classname="org.apache.axis2.wsdl.WSDL2Java" fork="true">
          <classpath refid="axis.classpath"/> 
          <arg value="-d"/>
          <arg value="xmlbeans"/>
          <arg value="-uri"/>
          <arg file="wsdl/simple.wsdl"/>
          <arg value="-ss"/>
          <arg value="-g"/>
          <arg value="-sd"/>
          <arg value="-o"/>
          <arg file="output"/>
          <arg value="-p"/>
          <arg value="org.simple.endpoint"/>
      </java>

      <!-- Move the schema folder to classpath-->
      <move todir="${build.classes}">
          <fileset dir="output/resources">
              <include name="*schema*/**/*.class"/>
              <include name="*schema*/**/*.xsb"/>
          </fileset>
      </move>

  </target>
```

For an explanation of the Axis2 WSDL2Java Ant task and its
options, see the [CodegenToolReference
Guide.](#tools-codegentoolreference)

A feature of XMLBeans is that there is one class file created
with WSDL2java, and a series of .xsb files. They must be referenced
when compiling, and as the example shows, these files are moved to
a build directory.

The Axis2 WSDL2Java example also takes the simple.wsdl, which is
under the directory 'wsdl', and creates files under the directory
'output'. The relevant non-xmlbean files created are shown
below:

```

output/resources/services.xml
output/src/org/simple
output/src/org/simple/endpoint
output/src/org/simple/endpoint/SimpleEndpointSkeleton.java
output/src/org/simple/endpoint/SimpleEndpointMessageReceiverInOut.java
output/src/org/simple/endpoint/SimpleEndpointCallbackHandler.java
output/src/org/simple/endpoint/SimpleEndpointStub.java
output/src/simplens
output/src/simplens/types
output/src/simplens/types/SimpleLoginDocument.java
output/src/simplens/types/impl
output/src/simplens/types/impl/SimpleLoginDocumentImpl.java
output/src/simplens/types/impl/SimpleLoginResponseDocumentImpl.java
output/src/simplens/types/SimpleLoginResponseDocument.java
```

The first important distinction is that while the Axis 1.x
example generated deploy.wsdd and undeploy.wsdd, the Axis2 example
created a services.xml. The files deploy.wsdd and services.xml are
a breed apart, coming from different architectures. There is no
direct parallel between them. See the Axis2 user guide for an
explanation about services.xml

Now we're ready to code. We'll start with Axis 1.x on the
service side. To implement the business logic, we'll change
simpleNS/SimpleEndpointBindingImpl.java from:

```

package simpleNS;

public class SimpleEndpointBindingImpl implements simpleNS.SimpleEndpoint{
    public simpleNS.types.SimpleLoginResponse simpleLogin(simpleNS.types.SimpleLogin parameters) 
        throws java.rmi.RemoteException {
        return null;
    }

}
```

To:

```

package simpleNS;

public class SimpleEndpointBindingImpl implements simpleNS.SimpleEndpoint{
    public simpleNS.types.SimpleLoginResponse simpleLogin(simpleNS.types.SimpleLogin parameters) 
        throws java.rmi.RemoteException {

        String userName = parameters.getUser_name();
        String password = parameters.getUser_password();
        // do something with those vars...
        return new simpleNS.types.SimpleLoginResponse("mySessionID", "username");
    }

}
```

In Axis 1.x, the next step is to compile the classes and put
them in the Axis.war, and then run the admin client with the
generated deploy.wsdd. You then look at the happy axis page to
verify that the service has been installed correctly.

Now let's code Axis2. In Axis 1.x, while the Ant task shown in
the example created a skeleton, a peek inside shows that the
skeleton calls the binding implementation class. In Axis2, we work
with the skeleton directly. To implement the business logic in the
generated Axis2 classes, we'll change
org/simple/endpoint/SimpleEndpointSkeleton.java from:

```

package org.simple.endpoint;
    /**
     *  SimpleEndpointSkeleton java skeleton for the axisService
     */
    public class SimpleEndpointSkeleton {

        /**
         * Auto generated method signature
          * @param param0
         */
        public  simplens.types.SimpleLoginResponseDocument simpleLogin
                  (simplens.types.SimpleLoginDocument param0 ) throws Exception {
                //Todo fill this with the necessary business logic
                throw new  java.lang.UnsupportedOperationException();
        }
}
```

To:

```

package org.simple.endpoint;
    
    import simplens.types.*;
    import simplens.types.SimpleLoginResponseDocument.*;
    import simplens.types.SimpleLoginDocument.*;
    /**
     *  SimpleEndpointSkeleton java skeleton for the axisService
     */
    public class SimpleEndpointSkeleton {
     
        /**
         * Modified 
          * @param simpleLoginDocument
         */
        public SimpleLoginResponseDocument simpleLogin
                  (simplens.types.SimpleLoginDocument simpleLoginDocument){
  
                SimpleLoginResponseDocument retDoc =
                    SimpleLoginResponseDocument.Factory.newInstance();
                 
                SimpleLoginResponse retElement =
                    SimpleLoginResponse.Factory.newInstance();
  
                // Get parameters passed in 
                SimpleLogin simpleLogin = simpleLoginDocument.getSimpleLogin();
                String userName = simpleLogin.getUserName();
                String password = simpleLogin.getUserPassword();

                // do something with those variables...

                retElement.setWebUserName(userName);
                retElement.setSoapSessionId("my random string");
                retDoc.setSimpleLoginResponse(retElement);
                return retDoc; 
        }
}
```

In Axis2, the next step is to compile the classes, put them
along with the generated services.xml in an AAR, and then hot
deploy the AAR by placing it in the Axis2.war under
WEB-INF/services. Point a browser to
http://localhost:8080/axis2/listServices, and you should see the
service 'SimpleService' ready for action. See the Axis2 user guide
for more info.

The last step is constructing the client. Our Axis 1.x client
for this example is:

```

package org;

import simpleNS.*;
import simpleNS.types.*;

public class Tester {
  public static void main(String [] args) throws Exception {
    // Make a service
    SimpleService service = new SimpleServiceLocator();

    // Now use the service to get a stub which implements the SDI.
    SimpleEndpoint port =  service.getSimpleEndpointPort();

    // set the params
    SimpleLogin parameters = new SimpleLogin("username","password");
    // Make the actual call
    SimpleLoginResponse simpleLoginResponse = port.simpleLogin(parameters);
    String session = simpleLoginResponse.getSoap_session_id();
    String user = simpleLoginResponse.getWeb_user_name();
    System.out.println("simpleLoginResponse, session: " + session + ", user: " + user);
  }
}
```

Finally, our Axis2 client for this example is:

```

package org;
import simplens.types.*;
import simplens.types.SimpleLoginDocument.*;
import simplens.types.SimpleLoginResponseDocument.*;
import simplens.types.impl.*;
import org.simple.endpoint.*;

public class Tester {
  public static void main(String [] args) throws Exception {

    // you may not need to pass in the url to the constructor - try the default no arg one
    SimpleEndpointStub stub =
         new SimpleEndpointStub(null, "http://localhost:8080/axis2/services/SimpleService");

    SimpleLogin simpleLogin = SimpleLogin.Factory.newInstance();
    simpleLogin.setUserName("userName");
    simpleLogin.setUserPassword("password");

    SimpleLoginDocument simpleLoginDocument =
        SimpleLoginDocument.Factory.newInstance();

    simpleLoginDocument.setSimpleLogin(simpleLogin);

    SimpleLoginResponseDocument simpleLoginResponseDocument
        = stub.simpleLogin(simpleLoginDocument);

    SimpleLoginResponse simpleLoginResponse =
        simpleLoginResponseDocument.getSimpleLoginResponse();

    String session = simpleLoginResponse.getSoapSessionId();
    String user = simpleLoginResponse.getWebUserName();
    System.out.println("simpleLoginResponse, session: " + session + ", user: " + user);

  }
}
```

Axis2 clients also have asynchronous options via a Callback and
alternatively a 'Fire and forget'. See the user guide for more
details.

## Best Usage

Axis1.x and Axis2 have different ways of seeing the SOAP stack.
So the best way to migrate is to follow the [User's Guide](#docs-userguide) and the [Architecture Guide](#docs-axis2architectureguide) of Axis2
properly. We are confident you will find Axis2 very straightforward
and more friendly to use than its predecessor.

---

<a id="docs-axis2-rpc-support"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/Axis2-rpc-support.html -->

<!-- page_index: 53 -->

# Axis2 RPC Support

This document describes Axis2's Remote Procedure Call support in
a set of easy to understand implementation steps.

## Introduction

Axis2 Remote Procedure Call (RPC) support may seem somewhat
tricky and confusing at first glance. However, Axis2 RPC strategy
is based on a set of well defined rules. This document aims to
drill down to the details of the strategy and resolve most of the
unknown bits and pieces. Note that Axis2 currently does not support
the rpc/encoded style. But it fully supports the rpc/literal
style.

We will discuss the Axis2 RPC strategy in the following
steps

## Step 1 - Converting RPC Style WSDL's into Doc/Lit Style WSDL

This is probably the most confusing part of the RPC strategy.
Since the Axis2 code generator is based on pure doc/lit style, the
first step of the code generation process is to generate a wrapper
schema. This wrapper generation can be easily explained by using an
example.

Take the following piece of WSDL

```

 .....
    <message name="requestMessage">
                <part name="part1" type="xs:string"/>
                <part name="part2" type="xs:int"/>
        </message>
        <message name="responseMessage">
                <part name="part1" type="xs:string"/>
        </message>
        <portType name="echoPortType">
                <operation name="echo">
                        <input message="y:requestMessage"/>
                        <output message="y:responseMessage"/>
                </operation>
        </portType>
        <binding name="echoBinding" type="y:echoPortType">
                <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
                <operation name="echo">
                        <soap:operation soapAction="echo"/>
                        <input>
                                <soap:body use="literal"/>
                        </input>
                        <output>
                                <soap:body use="literal"/>
                        </output>
                </operation>
        </binding>
.....
```

The binding says rpc/lit is required and in this case the
message parts will need wrapping in the following order:

1. The first element needs to have the operation name as the local
   name and the operation namespace. (This happens to be the namespace
   of the porttype - in this case the targetnamespace of the
   WSDL.)
2. The children of this element are non namespace qualified
   elements with the part names as local names (referred to as
   **part element**)
3. In case the part refers to a standard type like the example
   WSDL, the content of the part element would be of that type. If the
   part refers to a complex type defined in the schema, the content of
   the part element becomes of that type. Having an element reference
   in the part when the binding is rpc is invalid.

For example, the input wire message for the echo operation
mentioned in the above WSDL fragment would look like this:

```

 <op:echo xmlns:op="porttype namespace">
  <part1>Hello World</part1>
  <part2>123</part2>
 </op:echo>
```

Note that the element name is in bold. The first one is the
operation name, the second and third are part names. It can be seen
that it is possible to generate a schema representing this
structure, and then treat the whole service as a pure doc/lit
service. In this case, the following piece of schema is generated
to make the rpc to doc conversion. Note that in this case the wire
message stays unchanged. It is only a different WSDL authoring
style

```

 <xs:element name="echo">
    <xs:complexType>
      <xs:sequence>
                <xs:element name="part1" type="xs:string" /> 
                <xs:element name="part2" type="xs:int" /> 
           </xs:sequence>    
    </xs:complexType>
 </xs:element>
```

What the Axis2 code generator does is exactly this. By looking
at the binding style, it generates a wrapper schema in places
required before handing over the Axis\* hierarchy to the code
generator engine. In every case (even when the schema needs to be
unwrapped) this wrapping part will take place!

## Step 2 - Unwrapping the Schema

If the schema needs to be unwrapped, it brings up a few issues.
This is mainly because the only thing that the emitters rely on
when generating code is a mapping table.

1. When the schema is unwrapped, where will the unwrapping
   information remain?

   There has to be a store to keep the information seperated. The
   Axis \* hierarchy can be used for this. It has nicely separated
   information holders and a parameter store that can hold an
   information bean.
2. How do we maintain uniqueness among message part names?

   Part names are only unique across a message and not globally.
   However, due to the fact that we have a global mapping table, we
   need a way to differentiate between parts of different messages.
   The technique used here is to generate a QName that has the
   operation name as a namespace and a suffix (like \_input) appended
   to the local name.

Given these solutions, the first step in unwrapping is to walk
the schema and figure out the unwrappable items. The key player of
the unwrapping process is the unwrapping extension. It walks a
given schema and figure out the unwrappable parts if there are
any.

The current unwrapper looks for the following patterns and fails
if it is not found!

```

< element >
      < complexType >
           < sequence >
               < element />
           < /sequence >
       < /complexType >
  < /element >
 
```

Once this pattern is detected, the unwrapper details will be
added to the relevant AxisMessage component.

## Step 3 - Populate Type Information

The next step is to populate the Type information for the parts.
This has to be explicitly done by the data binding extensions, and
currently the ADB and XMLbeans extensions populate the relevant
AxisMessage by looking up their generated type systems. This type
information goes into the AxisMessage inside a
MessagePartInformationHolder instance.

The following code fragment from the ADB extension shows how the
AxisMessages get populated with the relevant type information. The
code is almost the same for the XMLBeans extension. Note the items
in bold.

```

 if (message.getParameter(Constants.UNWRAPPED_KEY) != null) {
            XmlSchemaType schemaType = message.getSchemaElement().getSchemaType();
            if (schemaType instanceof XmlSchemaComplexType) {
                XmlSchemaComplexType cmplxType = (XmlSchemaComplexType) schemaType;
                XmlSchemaParticle particle = cmplxType.getParticle();
                if (particle instanceof XmlSchemaSequence) {
                    XmlSchemaObjectCollection items =
                            ((XmlSchemaSequence) particle).getItems();
                    for (Iterator i = items.getIterator(); i.hasNext();) {
                        Object item = i.next();
                        if (item instanceof XmlSchemaElement) {
                           XmlSchemaElement xmlSchemaElement = (XmlSchemaElement) item;
                            XmlSchemaType eltSchemaType = xmlSchemaElement.getSchemaType();
                            if (eltSchemaType != null) {
                                populateClassName(eltSchemaType,mapper,opName,xmlSchemaElement.getName());
                            } else if (xmlSchemaElement.getSchemaTypeName() != null) {
                              eltSchemaType = findSchemaType(schemaMap,
                                       xmlSchemaElement.getSchemaTypeName());
                              if (eltSchemaType!=null){
                                 populateClassName(eltSchemaType,mapper,opName,xmlSchemaElement.getName());
                            }
                          }
                      }
                  }
              }
         }
   }
```

The populateClassName looks like this

```

 private static void populateClassName(XmlSchemaType eltSchemaType,
                                          TypeMapper typeMap,
                                          String opName,
                                          String partName) {
        Map metaInfoMap = eltSchemaType.getMetaInfoMap();
        if (metaInfoMap != null) {
            String className = (String) metaInfoMap.
                    get(SchemaConstants.SchemaCompilerInfoHolder.CLASSNAME_KEY);
            QName partQName = WSDLUtil.getPartQName(opName,
                    WSDLConstants.INPUT_PART_QNAME_SUFFIX,
                    partName);
            typeMap.addTypeMappingName(partQName,className);
            if (Boolean.TRUE.equals(
                    metaInfoMap.get(SchemaConstants.
                            SchemaCompilerInfoHolder.CLASSNAME_PRIMITVE_KEY))){
                //this type is primitive - add that to the type mapper status
                //for now lets add a boolean
                typeMap.addTypeMappingStatus(partQName,Boolean.TRUE);
            }

        }
    }
```

## Step 4 - Generate Code with Unwrapped Parameters

The next step is generating the actual code. The
AxisServiceBasedMultiLanguageEmitter has a method that generates
the XML model for the input parameters, and that method includes
the relevant part parameters inside the relavant top level input
parameter element.

The relevant part of the XML model looks like this. Note that
this intermediate XML model is the one that is parsed against the
Stylesheets to generate the code.

```

<input>
 <param name="param4" type="com.example.www.ServiceNameStub.Echo" shorttype="Echo" value="null" location="body" opname="echo">
        <param name="param5" type="java.lang.String" shorttype="String" value="null" location="body" opname="echo" partname="Part1" 
                                                                                                primitive="yes"/>
        <param name="param6" type="int" shorttype="int" value="0" location="body" opname="echo" partname="Part2" primitive="yes"/>
  </param>
</input>
```

The next part is handled by the template. Basically, the
template looks after the generation of multiple parameters into the
method signatures, and then the generating of the relevant
serialization and deserialization code for the parameters.

## Bringing the Parameters Together and Exploding Them

This is a somewhat controversial area. The current Axis2 code
generator does the wrapping and unwrapping at the object level and
not the XML level. In short, the exploded parameters are only a
convenience and the explosion does not run down to the XML level.
The following example of generated source code makes this
clear:

```

 private org.apache.axiom.soap.SOAPEnvelope toEnvelope(
        org.apache.axiom.soap.SOAPFactory factory, java.lang.String param1,
        int param2, boolean optimizeContent) {
        com.example.www.ServiceNameStub.Echo wrappedType = new com.example.www.ServiceNameStub.Echo();
        wrappedType.setPart1(param1);
        wrappedType.setPart2(param2);
        rg.apache.axiom.soap.SOAPEnvelope emptyEnvelope = factory.getDefaultEnvelope();
        emptyEnvelope.getBody().addChild(wrappedType.getOMElement(
                        com.example.www.ServiceNameStub.Echo.MY_QNAME, factory));
        
        return emptyEnvelope;
}
```

Note the lines in bold. The wrapped class will anyway be
instantiated and used at the end, but what the user sees is
different. Exploding the parameters happens in a similar way!

## Conclusion

Axis2 RPC support is sort of a misty area, but it is based on a
well defined set of rules which makes it not *that* misty
after all!

---

---

<a id="index"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/index.html -->

<!-- page_index: 54 -->

# Welcome to Apache Axis2/Java

Apache Axis2™ is a Web Services JSON / SOAP / WSDL engine, the successor to the
widely used [Apache Axis](http://ws.apache.org/axis/) SOAP stack.
There are two implementations
of the Apache Axis2 Web services engine - Apache Axis2/Java and
Apache Axis2/C

While you will find all the information on Apache Axis2/Java
here, you can visit the [**Apache Axis2/C**](http://axis.apache.org/axis2/c/)
Web site for Axis2/C implementation information.

Apache Axis2, Axis2, Apache, the Apache feather logo, and the Apache Axis2 project logo are trademarks of The Apache Software Foundation.

### *Why Apache Axis2:*

A new architecture for Axis2 was introduced during the August
2004 Summit in Colombo, Sri Lanka. The new architecture on which
Axis2 is based on is more flexible, efficient and configurable in
comparison to [Axis1.x
architecture](http://ws.apache.org/axis/java/architecture-guide.html). Some well established concepts from Axis 1.x, like handlers etc., have been preserved in the new
architecture.

Apache Axis2 not only supports SOAP 1.1 and SOAP 1.2, but it
also has integrated support for the widely popular [REST style of Web
services](http://www.xfront.com/REST-Web-Services.html). The same business logic implementation can offer both
a WS-\* style interface as well as a REST/POX style interface
simultaneously.

Apache Axis2 over time has expanded to contemporary JSON
(JavaScript Object Notation) web services, and that area
is where new development is occuring. In addition to GSON
for the Java serialization/deserialization of JSON, Moshi
is now supported since GSON development has largely ceased.

Apache Axis2 is more efficient, more modular and more
XML-oriented / JSON-orientated than the older version. It is
carefully designed to support the easy addition of plug-in "modules"
that extend their functionality for features such as security and
reliability. The [Modules](#modules)
currently available or under development include:

- [WS-Security](http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=wss) - Supported by [Apache Rampart](http://axis.apache.org/axis2/java/rampart/)
- [WS-Addressing](http://www.w3.org/Submission/ws-addressing/) -Module included as part of Axis2
  core

Apache Axis2 is built on [Apache AXIOM](http://ws.apache.org/axiom/), a
new high performant, pull-based XML object model - however for JSON
based web services, Moshi (or GSON) takes its place and largely follows
the same pull-based concepts.

Axis2 comes with many new features, enhancements and industry
specification implementations. The key features offered are as
follows:

- **Speed** - Axis2 uses
  its own object model and StAX (Streaming API for XML) parsing to
  achieve significantly greater speed than earlier versions of Apache
  Axis.
- **Low memory foot
  print**- Axis2 was designed ground-up keeping low memory
  foot print in mind.
- **AXIOM** - Axis2 comes
  with its own light-weight object model, AXIOM, for message
  processing which is extensible, highly performant and is developer
  convenient.
- **Hot Deployment** - Axis2 is equipped
  with the capability of deploying Web services and handlers while
  the system is up and running. In other words, new services can be
  added to the system without having to shut down the server. Simply
  drop the required Web service archive into the services directory
  in the repository, and the deployment model will automatically
  deploy the service and make it available for use.
- **Asynchronous Web
  services** - Axis2 now supports asynchronous Web services
  and asynchronous Web services invocation using non-blocking clients
  and transports.
- **MEP Support** - Axis2
  now comes handy with the flexibility to support Message Exchange
  Patterns (MEPs) with in-built support for basic MEPs defined in
  WSDL 2.0.
- **Flexibility** - The
  Axis2 architecture gives the developer complete freedom to insert
  extensions into the engine for custom header processing, system
  management, and *anything else you can imagine*.
- **Stability** - Axis2
  defines a set of published interfaces which change relatively
  slowly compared to the rest of Axis.
- **Component-oriented
  Deployment** - You can easily define reusable networks of
  Handlers to implement common patterns of processing for your
  applications, or to distribute to partners.
- **Transport Framework**
  - We have a clean and simple abstraction for integrating and using
  Transports (i.e., senders and listeners for SOAP over various
  protocols such as SMTP, FTP, message-oriented middleware, etc), and
  the core of the engine is completely transport-independent.
- **WSDL support** - Axis2
  supports the Web Service Description Language, version [1.1](http://www.w3.org/TR/wsdl) and [2.0](http://www.w3.org/TR/wsdl20/), which allows you to easily
  build stubs to access remote services, and also to automatically
  export machine-readable descriptions of your deployed services from
  Axis2.
- **JSON support** - Axis2
  supports the creation of Web Services using JavaScript Object Notation, with [GSON](https://github.com/google/gson) and [Moshi](https://github.com/square/moshi), which allows you to easily
  build POJO based services that receive and return JSON.
- **Composition and
  Extensibility** - Modules and phases improve support for
  composability and extensibility. Modules support composability and
  can also support new WS-\* specifications in a simple and clean
  manner. They are however not [hot
  deployable](#index--hot_deployment) as they change the overall behavior of the
  system.

We hope you enjoy using Axis2. Please note that this is an
open-source effort. If you feel the code could use new features or
fixes, or the documentation can be improved, please get involved
and lend us a hand! The Axis developer community welcomes your
participation.

Let us know what you think! Send your feedback on Axis2 to
"[java-user@axis.apache.org](mailto:java-user@axis.apache.org)". Make
sure to prefix the subject of the mail with [Axis2].

---

<a id="download"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/download.html -->

<!-- page_index: 55 -->

## Releases

The current release is 2.0.0 and was published on March 04, 2025. The release note for this
release can be found [here](https://axis.apache.org/axis2/java/core/release-notes/2.0.0.html).

The following distributions are available for download:

|  | Link | Checksums and signatures |
| --- | --- | --- |
| Binary distribution | [axis2-2.0.0-bin.zip](http://www.apache.org/dyn/closer.lua/axis/axis2/java/core/2.0.0/axis2-2.0.0-bin.zip) | [SHA512](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-2.0.0-bin.zip.sha512) [PGP](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-2.0.0-bin.zip.asc) |
| Source distribution | [axis2-2.0.0-src.zip](http://www.apache.org/dyn/closer.lua/axis/axis2/java/core/2.0.0/axis2-2.0.0-src.zip) | [SHA512](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-2.0.0-src.zip.sha512) [PGP](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-2.0.0-src.zip.asc) |
| WAR distribution | [axis2-2.0.0-war.zip](http://www.apache.org/dyn/closer.lua/axis/axis2/java/core/2.0.0/axis2-2.0.0-war.zip) | [SHA512](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-2.0.0-war.zip.sha512) [PGP](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-2.0.0-war.zip.asc) |
| Axis2 plugin for IntelliJ IDEA | [axis2-idea-plugin-2.0.0.zip](http://www.apache.org/dyn/closer.lua/axis/axis2/java/core/2.0.0/axis2-idea-plugin-2.0.0.zip) | [SHA512](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-idea-plugin-2.0.0.zip.sha512) [PGP](https://downloads.apache.org/axis/axis2/java/core/2.0.0/axis2-idea-plugin-2.0.0.zip.asc) |

The binary distribution contains all the Axis2 libraries and modules, except for [Apache Rampart](https://axis.apache.org/axis2/java/rampart/)
(WS-Security implementation) which must be downloaded separately. It also contains command line tools, samples and scripts to start a standalone Axis2 server.

The WAR (Web Archive) distribution is designed for deployment on a servlet container.

The signatures of the distributions can be [verified](http://www.apache.org/dev/release-signing#verifying-signature) against the public keys in the [KEYS](https://downloads.apache.org/axis/axis2/java/core/KEYS) file.

Maintenance releases from branches other than the main branch can be found [here](http://www.apache.org/dyn/closer.lua/axis/axis2/java/core/).
Distributions for older releases can be found in the [archive](http://archive.apache.org/dist/axis/axis2/java/core/).

All releases are also available as Maven artifacts in the [central repository](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.apache.axis2%22).

---

<a id="docs-toc"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/docs/toc.html -->

<!-- page_index: 56 -->

# Table of Contents

1. [Introduction](#docs-contents)
2. [Installation Guide](#docs-installationguide)
3. [Add-on
   Modules](#modules)
4. [Application Server
   Specific Configuration Guide](#docs-app_server)
5. [Quick Start
   Guide](#docs-quickstartguide)
6. [User's
   Guide](#docs-userguide)
7. [Advanced User's
   Guide](#docs-adv-userguide)
8. [Configuration
   Guide](#docs-axis2config)
9. [Web
   Administrator's Guide](#docs-webadminguide)
10. [Architecture Guide](#docs-axis2architectureguide)
11. [JAXWS Guide](#docs-jaxws-guide)
12. [POJO Guide](#docs-pojoguide)
13. [Spring Guide](#docs-spring)
14. [ModulesGuide](#docs-modules)
15. [Clustering Guide](#docs-clustering-guide)
16. ADB Data Binding
    - 14.1 [Architecture](#docs-adb-adb-howto)
    - 14.2 [Advanced Features](#docs-adb-adb-advanced)
    - 14.3 [Code Generation Integration](#docs-adb-adb-codegen-integration)
    - 14.4 [Tweaking](#docs-adb-adb-tweaking)
17. JiBX Data Binding
    - 15.1 [Code Generation Integration](#docs-jibx-jibx-codegen-integration)
    - 15.2 [doc/lit Example](#docs-jibx-jibx-doclit-example)
    - 15.3 [unwrapped Example](#docs-jibx-jibx-unwrapped-example)
18. Advanced
    - 16.1 [AXIOM
      Based Service](#docs-xmlbased-server)
    - 16.2 [AXIOM Based
      Client](#docs-dii)
19. [Attachments/MTOM
    Guide](#docs-mtom-guide)
20. Transports
    - 18.1 [HTTP
      Transport sender](#docs-http-transport)
    - 18.2 [HTTP
      servlet transport](#docs-servlet-transport)
    - 18.3 [JMS Transport](#docs-jms-transport)
    - 18.4 [TCP Transport](#docs-tcp-transport)
    - 18.5 [Mail Transport](#docs-mail-transport)
    - 18.6 [UDP Transport](#docs-udp-transport)
    - 18.7 [XMPP Transport](#docs-xmpp-transport)
    - 18.8 [Custom
      Transport](#docs-transport_howto)
21. [WS-Policy
    Support](#docs-ws_policy)
22. [REST Support](#docs-rest-ws)
23. JSON support
    - 23.1[JSON support with Mapped/Badgerfish formats](#docs-json_support)
    - 23.2[Pure JSON Support](#docs-json_support_gson)
      - [Native Approach](#docs-json_support_gson--native_approach)
      - [XML Stream API Base Approach](#docs-json_support_gson--xml_stream_api_base_approach)
      - [User Guide](#docs-json_gson_user_guide)
      - [JSON and REST with Spring Boot User's Guide](#docs-json-springboot-userguide)
24. [Exposing CORBA Services as Web Services](#docs-corba-deployer)
25. [Guide to using
    EJB Provider in Axis2](#docs-ejb-provider)
26. [SOAP
    Monitor](#docs-soapmonitor-module)
27. [Command Line
    Tools](#docs-reference)
28. [Tools/Plug-ins](#tools)
    - 25.1 [Code Generator Tool - Command Line and Ant
      Task](#tools-codegentoolreference)
    - 25.2 [Axis2 Plug-in for IntelliJ IDEA](#tools-idea-idea_plug-in_userguide)
    - 25.3 [Service Archive Generator Wizard - Eclipse
      Plug-in](#tools-eclipse-servicearchiver-plugin)
    - 25.4 [Code Generator Wizard - Eclipse Plug-in](#tools-eclipse-wsdl2java-plugin)
    - 25.5 [AAR Maven2 Plug-in](#tools-maven-plugins-maven-aar-plugin)
    - 25.6 [Java2WSDL Maven2 Plug-in](#tools-maven-plugins-maven-java2wsdl-plugin)
    - 25.7 [WSDL2Code Maven2 Plug-in](#tools-maven-plugins-axis2-wsdl2code-maven-plugin)
29. [Migration Guide
    (from Axis1)](#docs-migration)
30. Design Notes
    - 27.1 [RPC
      Support](#docs-axis2-rpc-support)

---

<a id="faq"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/faq.html -->

<!-- page_index: 57 -->

# Frequently Asked Questions on Apache Axis2

**General**

1. [I'm having a problem using Axis2. What should I do?](#faq--a1)
2. [How to ask a question on the mailing list?](#faq--mailinglists)

**Class Loading Issues**

1. [How do I access resources that I put into my service or module archive file?](#faq--b1)

**Client API**

1. [I want to do Request-Response Messaging, Where should I look?](#faq--c1)
2. [I want to do One Way Messaging, Where should I look?](#faq--c2)
3. [When I try to do a non blocking call with useSeparateListener=true I get the error *to do two Transport Channels the Addressing
   Modules must be engaged*, Why is this?](#faq--c3)
4. [I have engaged addressing, and
   when I try to invoke a service I get an exception](#faq--c4)
5. [What is Axis2 Repository?](#faq--c5)

**Services**

1. [How do I have multiple services in one service archive?](#faq--e1)
2. [I see an internal server error page when I try to view the WSDL file.](#faq--f1)

**Databindings**

1. [When using ADB, I get an "Unexpected subelement" exception. Is this a bug?](#faq--unexpected_subelement)

# General

I'm having a problem using Axis2. What should I do?
:   First make sure you go through the user guide and this FAQ. If
    you are using a released version of Axis2, then there is a
    possibility that your problem has already being fixed in the latest
    code. Download Axis2 nightly builds and test again. You can download
    the complete snapshot distributions from our
    [Hudson
    continuous integration server](https://hudson.apache.org/hudson/job/Axis2/lastStableBuild/org.apache.axis2$distribution) and individual JARs from our
    [snapshot repository](http://repository.apache.org/snapshots/org/apache/axis2/). The
    snapshot repository is also the best choice if you are using Maven to build your project.

    If the problem still persists, then try to search for your
    question in our [developer](http://marc.theaimsgroup.com/?l=axis-dev&r=1&w=2)
    or [user](http://marc.theaimsgroup.com/?l=axis-user&r=1&w=2)
    mailing archives as it might have already being answered.

    If your problem is not answered in the mailing list, now is the
    best time to post your question to the axis-user mailing list (see next question). If
    you think it is a bug, please fill a bug report in [JIRA](http://issues.apache.org/jira/browse/AXIS2). Please
    attach all the supportive information, like your wsdl, schema,
    clients, services, stacktraces, etc., to the JIRA issue you
    created, as it will help one of our contributors to re-create the
    problem. **PLEASE DO NOT ASK QUESTIONS USING JIRA; USE IT ONLY AS
    AN ISSUE TRACKER.**

    If you are asking for an explanation of a feature in Axis2,
    there is a possibility that there is an article or FAQ written on
    it. Please search the web as there are lots of articles written and
    hosted by various sources on the web.

    ---

How to ask a question on the mailing list?
:   If you have a question that has not been answered elsewhere (see previous question),
    you may ask it on one of the mailing lists:

    - Users : [java-user@axis.apache.org](mailto:java-user@axis.apache.org)
    - Developers : [java-dev@axis.apache.org](mailto:java-dev@axis.apache.org)

    Before posting to a list, you need to [subscribe](#mail-lists) first.
    Since the mailing lists are shared with other subprojects (such as Rampart), please
    prefix the subject with [Axis2].

    **Note** : When you ask questions in the mailing list, please
    remember that everyone working in our project are volunteers.
    No-one can be forced to fix your bugs (See [What is Apache not about?](http://www.apache.org/foundation/faq.html#what-is-apache-NOT-about) ).

    Make sure you add enough information about your problem with
    stacktraces and any other supportive information. It will improve
    the chances of your question being answered. Prefixing your mail
    subject with prefixes like "URGENT" will not help you in any means.
    Yes we also accept all the blames about Axis2 in these mailing
    lists, as those will definitely help us to improve Axis2 :) .

# Class Loading Issues

How do I access resources that I put into my service or module archive file?
:   Axis2 has the notion of service isolation where each service or
    module gets its own class loader. Using this class loader you can
    access any resource that you put into your service archive file.
    You may want to access your resources from different locations. For
    example,

    1. A third party module wants to access your resources. Then the
       scenario is as follows:


```

AxisService myService =
messageContext.getAxisConfiguration().getAxisService("serviceName"); 
```

       or


```

AxisService myService = msgCtx.getAxisService();
```

       Then you can use the service class loader through which you can
       access its resources


```

ClassLoader clsLoader = myService.getServiceClassLoader();
clsLoader.getResourceAsStream("myResource");
```

    2. To initialize the service implementation class at the
       MessageReceiver level, the following steps need to be taken


```

AxisService service = msgCtx.getAxisService();
ClassLoader clsLoader = service.getServiceClassLoader();
Class.forName("serviceName",clsLoader,true);
```

       NOTE : Axis2 default MessageReciver uses the same technique to
       initialize service implementations
    3. If you want to load your resources at the service
       implementation class, then the scenario is as follows


```

getClass().getClassLoader().getResourceAsStream("myResource");
```

# Client API

I want to do Request-Response Messaging, Where should I look?
:   Look at the [ServiceClient](https://svn.apache.org/repos/asf/axis/axis2/java/core/trunk/modules/kernel/src/org/apache/axis2/client/ServiceClient.java) class, for more information
    please read the [User's Guide](#docs-adv-userguide)

    ---

I want to do One Way Messaging, Where should I look?
:   From Axis2 0.94 onwards, both request-response and one way
    messaging will be handled by [ServiceClient](https://svn.apache.org/repos/asf/axis/axis2/java/core/trunk/modules/kernel/src/org/apache/axis2/client/ServiceClient.java).

    ---

When I try to do a non blocking call with useSeparateListener=true I get the error *to do two Transport Channels the Addressing Modules must be engaged*, Why is this?
:   To do the two transport channel invocation, you need to engage
    the addressing module. You can enable it by un-commenting the entry
    in the axis2.xml file or `Call.engageModule(QName)`. However,
    addressing is enabled by default.

    ---

I have engaged addressing, and when I try to invoke a service I get an exception
:   If you have engaged addressing, then you must have wsa:action,
    the required WS-Addressing header. You have to call
    `option.setAction("urn:myaction");`. Note that the
    action should be a URI.

    ---

What is Axis2 Repository?
:   The Repository stores the configuration of Axis2. The users
    should specify the repository folder of the Axis Server (HTTP or
    TCP). In the case of Tomcat, it is the webapps/axis2/WEB-INF
    folder. The following picture shows a sample repository.

    ![Sample repository](assets/images/1_d8faade5ec987092.jpg)

    Modules and services have an archive format defined and they are
    automatically picked up by Axis2 when they are copied to
    corresponding folders.

# Services

How do I have multiple services in one service archive?
:   It's just a matter of writing a services.xml file to configure
    the service or services in an archive file. The corresponding
    services.xml **must** look as follows,


```

<serviceGroup>
  <service name="myService1">
  ...........................
  </service>

  <service name="myService2">
  ...........................
  </service>
<serviceGroup>
```

    NOTE : The name attribute is a compulsory attribute that will
    become the name of the services. If you want to have one service in
    the archive file, then there are two options. You can either have
    one service inside the serviceGroup tag or have only one service
    tag, as shown below, in your services.xml, in which case, the name
    of the service will be the name of the archive file, which you
    cannot override.


```

<service>
...............
<service>
```

    ---

I see an internal server error page when I try to view the WSDL file.
:   This happens specifically with Tomcat 4.x and 5.0 in a JDK 1.5
    environment. The reason is that the system picks up a wrong
    transformer factory class. This can be solved simply by putting the
    [xalan-2.7.0.jar](http://www.apache.org/dist/java-repository/xalan/jars/)
    into the axis2/WEB-INF/lib directory

# Databindings

When using ADB, I get an "Unexpected subelement" exception. Is this a bug?
:   In general, "Unexpected subelement" means that the message being processed
    doesn't conform to the WSDL that was used to generate the ADB code. If you are getting
    this exception on the client side, it means that the response from the server
    is invalid. If you are seeing the error on the server side, it means that the
    request received by the service is invalid.

    If you are sure that the message conforms to the WSDL and believe that there
    is an issue with the code generated by Axis2, you should do the following before
    opening a JIRA issue:

    1. Test the scenario with the latest Axis2 snapshot version. This includes
       regenerating the code with the latest codegen version.
    2. Provide the WSDL that causes the issue, or if for legal reasons you are not
       allowed to provide the original WSDL, provide a minimal WSDL that reproduces
       the problem.
    3. Provide some hard evidence that this is indeed an issue in Axis2. This means
       at least a transcript of the SOAP message that proves that it conforms to the WSDL.

---

<a id="articles"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/articles.html -->

<!-- page_index: 58 -->

# Apache Axis2 References

This page contains articles, tutorials, presentations and
question and answers published on various Web sites on the Apache
Axis2 engine. These references will prove to be a great help in
boosting your knowledge on Axis2.

## Books:

- [Apache Axis2 Web Services](https://www.packtpub.com/apache-axis2-web-services/book)
  - By Deepal Jayasinghe and Afkham Azeez
![Apache Axis2 Web Services](https://www.packtpub.com/sites/default/files/imagecache/productview/1568_Apache%20Axis2cov.jpg)- [Quicktstart Apache Axis2](http://www.packtpub.com/article/create-quality-web-services-with-quicktstart-apache-axis2)
  - By Deepal Jayasinghe
![Quicktstart Apache Axis2](http://images.packtpub.com/images/100x123/1847192866.png)

## Articles:

- [Axis2 - The Future of Web Services](http://www.jaxmag.com/itr/online_artikel/psecom,id,747,nodeid,147.html)- By Srinath Perera, Ajith
  Ranabahu
- [Introducing
  Axis2, the Next Generation of the Apache Web Service Stack](http://www.developer.com/services/article.php/3525481)- By
  Srinath Perera
- [Web
  Services Messaging with Apache Axis2: Concepts and Techniques](http://www.onjava.com/pub/a/onjava/2005/07/27/axis2.html)-
  By Srinath Perera, Ajith Ranabahu (27 July 2005)
- [Axis2 Execution
  Framework](http://developer.com/java/web/article.php/3529321)- By Deepal Jayasinghe
- [Axis2 Deployment Model](http://jaxmag.com/itr/online_artikel/psecom,id,757,nodeid,147.html)- By Deepal Jayasinghe
- [Understanding
  Axis2 Deployment Architecture](http://www.developer.com/open/article.php/3557741)- By Deepal Jayasinghe
- [Inside the Axis2 Code Generator](http://wso2.org/library/35)- By Ajith Ranabahu (06 Feb
  2006)
- [Utilizing
  a Non-Java Web Service with Axis2](http://www.developer.com/java/other/article.php/3570031)- By Deepal Jayasinghe
- [Avoiding
  Mistakes Made Using Axis2](http://www.developer.com/open/article.php/3589126)- By Deepal Jayasinghe
- [Migrating Apache Axis apps to Axis2 using Apache Geronimo](http://www-128.ibm.com/developerworks/java/library/os-ag-axis2mig/index.html)- By
  Tyler Anderson (07 Mar 2006)
- [The Axis2
  Transport Framework](http://www.developer.com/java/ent/article.php/3606466)- By Deepal Jayasinghe
- [Reference Guide to Apache Axis2 Client API Parameters](http://wso2.org/library/230)- By Eran
  Chinthaka (01 Aug 2006)
- [Axis2 - Performance Testing Round #1](http://wso2.org/library/91)- By
  Devanum Sirinivas (17 May 2006)
- [Working With Apache Axis2](http://wso2.org/library/259)- Deepal Jayasinghe (13 Sep 2006)
- [Writing an
  Apache Axis2 Service from Scratch](http://www.developer.com/java/ent/article.php/3613896)- By Deepal Jayasinghe (20
  June 2006)
- [Apache
  Axis2 Session Management](http://www.developer.com/java/web/article.php/3620661)- By Deepal Jayasinghe
- [Apache Axis2
  with POJO's and Spring](http://www.devx.com/Java/Article/33839)- By Ramanujam A. Rao
- [Six ways the Axis2 deployment model is more user friendly](http://www-128.ibm.com/developerworks/webservices/library/ws-axis2soap/)- By Deepal Jayasinghe
- [Invoking Web Services using Apache Axis2](http://today.java.net/pub/a/today/2006/12/13/invoking-web-services-using-apache-axis2.html)- By Deepal Jayasinghe
- [Writing Your Own services.xml for Axis2 Web Services](http://wso2.org/library/2060)- By Deepal Jayasinghe
- [ADB Generated Code in Apache Axis2](http://wso2.org/library/2068)- By Amila Suriarachchi
- [Working with RPCServiceClient](http://wso2.org/library/articles/working-rpcserviceclient)- By Deepal Jayasinghe
- [Embedding Apache Axis2 into Existing Applications](http://www.developer.com/open/article.php/10930_3777111_2/Embedding-Apache-Axis2-into-Existing-Applications.htm)- By Deepal Jayasinghe
- [Using Axis2 and Java for Asynchronous Web Service Invocation on the Client Side](http://www.developer.com/java/web/article.php/10935_3863416_2/Using-Axis2-and-Java-for-Asynchronous-Web-Service-Invocation-on-the-Client-Side.htm)- By Deepal Jayasinghe
- [Java
  Web services, Part 2: Digging into Axis2: AXIOM](http://www.ibm.com/developerworks/webservices/library/ws-java2/) - By Dennis Sosnoski (30 Nov
  2006)
- [Java
  Web services, Part 3: Axis2 Data Binding](http://www.ibm.com/developerworks/webservices/library/ws-java3/) - By Dennis Sosnoski (26 Jul
  2007)

## Tutorials

- [Introducing Axis2](http://wso2.org/library/140)- By
  Eran Chinthaka, Chathura Herath (05 June 2006)
- [Accelerating Web Services
  Development with Axis2](http://wso2.org/library/141)- By Deepal Jayasinghe, Ajith Ranabahu
  (05 June 2006)
- [Hello World with Apache
  Axis2](http://wso2.org/library/95)- By Ruchith Fernando (29 May 2006)
- [How Apache Axis2 Finds
  the Operation and Service a Message is Destined To](http://wso2.org/library/176)- By Eran
  Chinthaka(18 June 2006)
- [How to Debug a Web
  Service?](http://wso2.org/library/225)- By Ajith Ranabahu (28 July 2006)

## Presentations

- [Why Axis2: The Future of
  Web Services](http://wso2.org/library/136)- By Eran Chinthaka (05 June 2006)
- [Building Enterprise
  Applications with Axis2-Tutorial from ApacheCon Asia 2006](http://wso2.org/library/247)- By
  Deepal Jayasinghe, Ruchith Fernando (30 Aug 2006)
- [Introducing Axis2](http://wso2.org/library/137)- By
  Ajith Ranabahu (05 June 2006)

## Questions and Answers

- [Setting up Apache Axis2 in
  eclipse IDE](http://wso2.org/library/67)- By Ruchith Fernando (04 April 2006)
- [How do I Embed
  SimpleHTTPServer in My Application and Deploy a POJO?](http://wso2.org/library/83)- By
  Davanum Sirinivas (09 May 2006)
- [How to Configure Axis2's
  HTTP Transport Sender at Client Side?](http://wso2.org/library/209)- By Saminda Abeysinghe
  (11July 2006)
- [How to do REST invocation
  with Axis2/Java ServiceClient?](http://wso2.org/library/175)- By Eran Chinthaka (17 June
  2006)
- [How to Embed an Axis2
  based Web Service in your Webapp?](http://wso2.org/library/90)- By Davanum Sirinivas(17 May
  2006)

---

<a id="reflib"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/refLib.html -->

<!-- page_index: 59 -->

## Reference Library

The Axis Project lives or fails based on its human resources.
Users and contributors alike help the project with ideas and
brainpower. A common foundation of knowledge is required to
effectively participate in this virtual community. The following is
a list of documents that we have found helpful to us and they maybe
helpful to you:

These resources are required reading for anybody contributing
source code to the project.

**SOAP Specific Resources**

**SOAP W3C Specification** [1.1](http://www.w3.org/TR/2000/NOTE-SOAP-20000508/) and
[1.2](http://www.w3.org/TR/soap/)
Required reading.

**[SOAP
Messaging with Attachments W3C Specification](http://www.w3.org/TR/SOAP-attachments)**
SOAP combined with MIME.

**[SOAP Security
Extensions: Digital Signature Specification](http://www.w3.org/TR/SOAP-dsig/)**
Adding security to SOAP.

**Other Specifications**

Web Services Description Language (WSDL) [1.1](http://www.w3c.org/TR/wsdl.html) [2.0](http://www.w3.org/TR/wsdl20/)

WS - Addressing [submission](http://www.w3.org/Submission/ws-addressing/)
[1.0
(31st March,2005)](http://www.w3.org/TR/2005/WD-ws-addr-core-20050331/)

[Web Services Policy Framework (WSPolicy)](http://www.w3.org/TR/ws-policy/)

[WS-I Basic
Profile Version 1.0](http://www.ws-i.org/Profiles/BasicProfile-1.0.html)

[Java API for XML-based RPC (JAX-RPC)](http://jcp.org/aboutJava/communityprocess/first/jsr101/index.html)

[SOAP Message
Transmission Optimization Mechanism](http://www.w3.org/TR/2005/REC-soap12-mtom-20050125/)

**Other Resources**

**[The
Java Language Specification](http://java.sun.com/docs/books/jls/index.html)**
Written by the creators of the Java Programming Language, this
online book is considered by many to be the bible for programming
in Java. A must read.

**[Javadoc](http://java.sun.com/products/jdk/javadoc/index.html)**
Javadoc is the automatic software documentation generator used by
Java, since it was first released. All code written for this
project must be documented using Javadoc conventions.

**[The
Java Code Conventions](http://java.sun.com/docs/codeconv/html/CodeConvTOC.doc.html)**
This Sun document specifies the de-facto standard way of formatting
Java code. All code written for this project must follow these
conventions.

[**Version
Control with SubVersion**](http://svnbook.red-bean.com/en/1.1/svn-book.html)
Written by Ben Collins-Sussman, Brian W. Fitzpatrick, C. Michael
Pilato. It provides details on SVN features.

---

<a id="overview"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/overview.html -->

<!-- page_index: 60 -->

## Overview

Every volunteer project obtains its strength from the people
involved in it. We invite you to participate as much or as little
as you choose. The roles and responsibilities that people can
assume in the project are based on merit. Everybody's input
matters!

There are a variety of ways to participate. Regardless of how
you choose to participate, we suggest you join some or all of our
[mailing lists](#mail-lists).

## **Use the Products and Give Us Feedback**

Using the products, reporting bugs, making feature requests, etc. is by far the most important role. It's your feedback that
allows the technology to evolve.

- [Join Mailing Lists](#mail-lists)
- [Download Binary Builds](https://axis.apache.org/axis2/java/core/download.cgi)
- [Report
  bugs/Request additional features](https://issues.apache.org/jira/projects/AXIS2)

## **Contribute Code or Documentation Patches**

In this role, you participate in the actual development of the
code. If this is the type of role you'd like to play, here are some
steps (in addition to the ones above) to get you started:

- Read our [developer guidelines](#guidelines) and [release process](#release-process)
- Review the [reference library](#reflib)
- [View the Source Code](https://github.com/apache/axis-axis2-java-core)
- [Access GIT Repository](#git)

---

<a id="git"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/git.html -->

<!-- page_index: 61 -->

# Introduction

This document provides information on how to use Git to get a
GitHub checkout/update, make commits to the repository, etc., in the
process of contributing to Apache projects (specifically Axis2).
Instructions on configuring IDEs for development and using Maven to
build the project is also included here.

# Working with GitHub (Git)

The Axis2 development team uses GitHub (Git) for source
control.

# Checkout Axis2 from Git

To check out the latest version of Axis2 from the Foundation's
GitHub repository, you must use the following URL:

- **If you are a committer or not a committer, the link is the same:** <https://github.com/apache/axis-axis2-java-core>

Once you have successfully installed Git, you can check
out Axis2 trunk by following these steps:

1. Run **git clone <repository URL>** where
   the repository URL from the previous list.
2. This step will check out the latest version of the Axis2 Java
   codebase to a directory named "axis-axis2-java-core".

# Installing Maven 3

Axis2's build is based on Maven 3. Maven is a build system that
allows for the reuse of common build projects across multiple
projects. For information about obtaining, installing, and
configuring Maven 3, please see the [Maven project page](http://maven.apache.org).
To use Maven to build the Axis2 project, Please install
[Maven2](http://maven.apache.org/download.html) and
follow instructions here - [Quick Guide to Maven for Axis 2.0](https://axis.apache.org/axis2/java/core/maven-help.html).

# Configuring your IDE

The Axis2 development team uses a variety of development tools
from vi to emacs to Eclipse to Intellij/IDEA. The following section
is not an endorsement of a specific set of tools, it is simply
meant as a pointer to ease the process of getting started with
Axis2 development.

## Intellij IDEA

Type **mvn idea:idea**. Generates the necessary IDEA .ipr, .iml
and .iws project files.

## Eclipse

We recommend using [maven-eclipse-plugin](http://maven.apache.org/plugins/maven-eclipse-plugin/)
to import the Axis2 sources into Eclipse. This works best with the following
combinations of versions and settings:

- Early versions of Maven 2 have issues with non standard packagings
  (`bundle`, `aar` and `mar` in the case of Axis2)
  in multi-module builds. While this has no impact on the normal Maven
  build, it prevents the Maven Eclipse plugin from identifying modules
  with these packagings as Java projects. Therefore it is recommended
  to use Maven 2.2.x or 3.0.x to execute the Maven Eclipse plugin.
- By default, the Maven Eclipse plugin only imports generated sources
  and resources created during the `generate-sources` and
  `generate-resources` phases, but fails to locate them if they
  are generated during the `generate-test-sources` and
  `generate-test-resources` phases. This is due to a limitation in Maven 2 (see
  [MECLIPSE-37](http://jira.codehaus.org/browse/MECLIPSE-37)
  for more information). Executing the `eclipse:eclipse` goal after
  the `process-test-resources` phase is also not enough because of
  [MDEP-259](http://jira.codehaus.org/browse/MDEP-259). The
  best is to execute it after the `install` phase. The `skipTests`
  property can be used to skip the execution of the unit tests (`maven.test.skip`
  is not appropriate here because it also skips some of the goals configured
  in the `generate-test-sources` and `generate-test-resources` phases).

To summarize, use the following command to prepare the Axis2 sources for
import into Eclipse:

```
mvn -DskipTests=true install eclipse:eclipse
```

As usual, before importing the projects into Eclipse, check that a Classpath Variable
for `M2_REPO` is configured in Eclipse. Then select File > Import > Existing Projects
into Workspace > Select root directory. Selecting the root of
the Axis source discovers all the modules and allows them to be
imported as individual projects at once.

---

<a id="mail-lists"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/mail-lists.html -->

<!-- page_index: 62 -->

## Project Mailing Lists

These are the mailing lists that have been established for this project. For each list, there is a subscribe, unsubscribe, and an archive link.

| Name | Subscribe | Unsubscribe | Post | Archive | Other Archives |
| --- | --- | --- | --- | --- | --- |
| Axis2 Developer List | [Subscribe](mailto:java-dev-subscribe@axis.apache.org) | [Unsubscribe](mailto:java-dev-unsubscribe@axis.apache.org) | [Post](mailto:java-dev@axis.apache.org) | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/axis-java-dev/) | [markmail.org](http://markmail.org/search/list:org.apache.ws.axis-dev) |
| Axis2 User List | [Subscribe](mailto:java-user-subscribe@axis.apache.org) | [Unsubscribe](mailto:java-user-unsubscribe@axis.apache.org) | [Post](mailto:java-user@axis.apache.org) | [mail-archives.apache.org](http://mail-archives.apache.org/mod_mbox/axis-java-user/) | [markmail.org](http://markmail.org/search/list:org.apache.ws.axis-user) |

---

<a id="release-process"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/release-process.html -->

<!-- page_index: 63 -->

# Release Process

## Release process overview

### Update: Since the 1.8.x series we have released from git master without branches. Skip to Performing a Release. We may or may not use branches again in the future.

### Cutting a branch

- When a release is ready to go, release manager (RM) puts
  forward a release plan as per standard Apache process, including
  dates. This gets VOTEd on by the committers. During this period the
  trunk is still the only relevant source base.
- As soon as a release is approved (or even before), RM should
  add the new version into JIRA as a target.
- At the point where we would normally do the “code freeze” for a
  release, the RM cuts a branch named for the release. This branch is
  where the release candidates and releases will happen.
- Ideally a release branch is only around for a week or maybe two
  before the release happens.
- The only things that should EVER get checked into the release
  branch are - 1) bug fixes targeted at the release, 2)
  release-specific updates (documentation, SNAPSHOT removal, etc). In
  particular new functionality does not go here unless it is a
  solution to a JIRA report targeted at the release.
- Normal development continues on the trunk.

### Dependencies and branches

- The trunk should always be “cutting edge” and as such should
  usually be pointing at SNAPSHOT versions of all dependencies. This
  allows for continuous integration with our partner projects.
- Soon after a release branch is cut, the RM is responsible for
  removing ALL dependencies on SNAPSHOT versions and replacing them
  with officially released versions. This change happens only on the
  release branch.

### Managing change and issue resolution with a release branch

- The RM goes through JIRA issues and sets “fix for” to point to
  both “NIGHTLY” and the new branched release number for the fixes
  that are targeted for the release after the branch is cut.
- In general, the assignee/coder fixes JIRA issues or makes other
  changes *on the trunk*. If the JIRA issue is targeted at the
  release, or upon coder's discretion, they then merge the fix over
  to the release branch.
- This way the trunk is ALWAYS up-to-date, and we don't have to
  worry about losing fixes that have only been made on the release
  branch.
- When the assignee resolves an issue, they confirm it's been
  fixed in both branches, if appropriate.

### Checking changes into the branch

- If bug fixes are needed later for a release which has long
  since happened (to fix user issues, etc), those fixes generally
  should also happen on the trunk first assuming the problem still
  exists on the trunk.
- There are only two cases where we would ever check anything
  into the branch without first checking it into the trunk. 1)
  Release specific items (release number references, release notes,
  removal of SNAPSHOTs), and 2) if the trunk has moved on in some
  incompatible way.

## Performing a release

### Preparation

Verify that the code meets the basic requirements for being releasable:

1. Check that the set of legal (`legal/*.LICENSE`) files corresponds to the set of third party
   JARs included in the binary distribution.
2. Check that the `apache-release` profile works correctly and produces the required distributions.
   The profile can be executed as follows:


```
mvn clean install -Papache-release
```

You may also execute a dry run of the release process: mvn release:prepare -DdryRun=true. In a dry run, the generated zip files will still be labled as SNAPSHOT. After this, you need to clean up using the following command: mvn release:clean

1. Check that the Maven site can be generated and deployed successfully, and that it has the expected content.

To generate the entire documentation in one place, complete with working inter-module links, execute the site-deploy phase (and check the files under target/staging). A quick and reliable way of doing that is to use the following command: mvn -Dmaven.test.skip=true clean package site-deploy

1. Check that the source distribution is buildable.
2. Check that the source tree is buildable with an empty local Maven repository.

If any problems are detected, they should be fixed on the trunk (except for issues specific to the
release branch) and then merged to the release branch.

Next update the release note found under `src/site/markdown/release-notes`. To avoid extra work for
the RM doing the next major release, these changes should be done on the trunk first and then merged
to the release branch.

### Pre-requisites

The following things are required to perform the actual release:

- A PGP key that conforms to the [requirements for Apache release signing](http://www.apache.org/dev/release-signing.html).
  To make the release process easier, the passphrase for the code signing key should
  be configured in `${user.home}/.m2/settings.xml`:


```
<settings>
  ...
  <profiles>
    <profile>
      <id>apache-release</id>
      <properties>
        <gpg.passphrase><!-- key passphrase --></gpg.passphrase>
      </properties>
    </profile>
  </profiles>
  ...
</settings>
```

- The release process uses a Nexus staging repository. Every committer should have access to the corresponding
  staging profile in Nexus. To validate this, login to [repository.apache.org](https://repository.apache.org)
  and check that you can see the `org.apache.axis2` staging profile. The credentials used to deploy to Nexus
  should be added to `settings.xml`:


```
<servers>
  ...
  <server>
    <id>apache.releases.https</id>
    <username><!-- ASF username --></username>
    <password><!-- ASF LDAP password --></password>
  </server>
  ...
</servers>
```

### Release

In order to prepare the release artifacts for vote, execute the following steps:

If not yet done, export your public key and  [append it there.](https://dist.apache.org/repos/dist/release/axis/axis2/java/core/KEYS)

If not yet done, also export your public key to the dev area and  [append it there.](https://dist.apache.org/repos/dist/release/axis/axis2/java/core/KEYS)

The command to export a public key is as follows:

`gpg –armor –export key_id`

If you have multiple keys, you can define a ~/.gnupg/gpg.conf file for a default. Note that while ‘gpg –list-keys’ will show your public keys, using maven-release-plugin with the command ‘release:perform’ below requires ‘gpg –list-secret-keys’ to have a valid entry that matches your public key, in order to create ‘asc’ files that are used to verify the release artifcats. ‘release:prepare’ creates the sha512 checksum files.

The created artifacts i.e. zip files can be checked with, for example, sha512sum ‘axis2-2.0.0-bin.zip.asc’ which should match the generated sha512 files. In that example, use ‘gpg –verify axis2-2.0.0-bin.zip.asc axis2-2.0.0-bin.zip’ to verify the artifacts were signed correctly.

1. Start the release process using the following command - use ‘mvn release:rollback’ to undo and be aware that in the main pom.xml there is an apache parent that defines some plugin versions [documented here.](https://maven.apache.org/pom/asf/)


```
mvn release:prepare
```

   When asked for a tag name, accept the default value (in the following format: `vX.Y.Z`).
2. Perform the release using the following command:


```
mvn release:perform
```

3. Login to Nexus and close the staging repository. For more details about this step, see
   [here](https://maven.apache.org/developers/release/maven-project-release-procedure.html) and [here](https://infra.apache.org/publishing-maven-artifacts.html#promote).
4. Execute the `target/checkout/etc/dist.py` script to upload the source and binary distributions to the development area of the  [repository.](https://dist.apache.org/repos/dist/)
5. Create a staging area for the Maven site:


```
git clone https://gitbox.apache.org/repos/asf/axis-site.git
cd axis-site
cp -r axis2/java/core/ axis2/java/core-staging
git add  axis2/java/core-staging
git commit -am "core-staging"
git push
```

6. Change to the `target/checkout` directory and prepare the site using the following commands:


```
mvn site-deploy
mvn scm-publish:publish-scm -Dscmpublish.skipCheckin=true
```

   Now go to the `target/scmpublish-checkout` directory (relative to `target/checkout`) and check that there
   are no unexpected changes to the site. Then commit the changes.

   The root dir of axis-site has a .asf.yaml file, referenced here at target/scmpublish-checkout/.asf.yaml, that is  [documented here.](https://github.com/apache/infrastructure-asfyaml/blob/main/README.md)
7. Start the release vote by sending a mail to `java-dev@axis.apache.org`.
   The mail should mention the following things:

   - A link to the Nexus staging repository.
   - A link to the directory containing the distributions
     (<https://dist.apache.org/repos/dist/dev/axis/axis2/java/core/x.y.x/>).
   - A link to the preview of the Maven site (<http://axis.apache.org/axis2/java/core-staging/>).

If the vote passes, execute the following steps:

1. Promote the artifacts in the staging repository. See
   [here](https://central.sonatype.org/publish/release/#close-and-drop-or-release-your-staging-repository)
   for detailed instructions for this step.
2. Publish the distributions:


```
svn mv https://dist.apache.org/repos/dist/dev/axis/axis2/java/core/x.y.z \
       https://dist.apache.org/repos/dist/release/axis/axis2/java/core/
```

3. Publish the site:


```
git clone https://gitbox.apache.org/repos/asf/axis-site.git
git rm -r core
git mv core-staging core
git commit -am "Axis2 X.Y.Z site"
git push
```

It may take several hours before everything has been synchronized. Before proceeding, check that

- the Maven artifacts for the release are available from the Maven central repository;
- the Maven site has been synchronized;
- the distributions can be downloaded from the mirror sites.

Once everything is in place, send announcements to `java-user@axis.apache.org` (with copy to
`java-dev@axis.apache.org`) and `announce@apache.org`. Since the two lists have different conventions, audiences and moderation policies, it is recommended to send the announcement separately to the two lists.
Note that mail to `announce@apache.org` must be sent from an `apache.org` address and will
always be moderated. The announcement sent to `announce@apache.org` also should include a general description
of Axis2, because not everybody subscribed to that list knows about the project.

### Post-release actions

1. Update the DOAP file (`etc/doap_Axis2.rdf`) and add a new entry for the release.
2. Update the status of the release version in JIRA.
3. Remove old (archived) releases from <https://dist.apache.org/repos/dist/release/axis/axis2/java/core/>.
4. Create an empty release note for the next release under `src/site/markdown/release-notes`.

---

<a id="guidelines"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/guidelines.html -->

<!-- page_index: 64 -->

## Release Process

Click to read our [Release Process
Guidelines](#release-process).

## Mail Guidelines

Every volunteer project obtains its strength from the people
involved in it. Mailing lists provide a simple and effective
communication mechanism.

You are welcome to join any of our mailing lists (or all of them
if you wish). You can choose to lurk, or actively participate. It's
up to you.

**Before you join these lists, you should make sure that you
read and follow the information below.**

We ask that you do your best to respect the charter of the
appropriate mailing list. There are generally two types of lists
that you can join.

- The "User" list is where you should send questions and comments
  about configuration, setup, usage and other "user" type of
  questions.
- The "Developer" list is where you should send questions and
  comments about the actual software source code and general
  "development" type of questions.

**Summary : Prefix each message subject with
"[Axis2]"**
You may already know that Axis 1.x is still going parallel with
Axis 2.0. So for everyone's convenience, prefix the subject of
**every mail** about Axis 2.0 with [Axis2].

**Summary: Join the lists that are appropriate for your
discussion.**
Please make sure that you are joining the list that is appropriate
for the topic or product that you would like to discuss.

**Summary: Do not abuse resources in order to get
help.**
Asking your configuration or user type of question on the
developers list because you think that you will get help more
quickly by going directly to the developers instead of to the user
base is not very nice. Chances are that doing this will actually
prevent people from answering your question because it is clear
that you are trying to abuse resources.

**Summary: Do your best to ensure that you are not sending HTML
or "Stylelized" email to the list.**
If you are using Outlook or Outlook Express or Eudora, chances are
that you are sending HTML email by default. There is usually a
setting that will allow you to send "Plain Text" email. If you are
using Microsoft products to send email, there are several bugs in
the software that prevent you from turning off the sending of HTML
email. Please read this page as well.

**Summary: Watch where you are sending email.**
The majority of our mailing lists have set the Reply-To to go back
to the list. That means that when you Reply to a message, it will
go to the list and not to the original author directly. The reason
is because it helps facilitate discussion on the list for everyone
to benefit from. Be careful of this as sometimes you may intend to
reply to a message directly to someone instead of the entire
list.

**Summary: Do not crosspost messages.**
In other words, pick a mailing list and send your messages to that
mailing list only. Do not send your messages to multiple mailing
lists. The reason is that people may be subscribed to one list and
not to the other. Therefore, some people may only see half of the
conversation.

---

<a id="sitehowto"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/siteHowTo.html -->

<!-- page_index: 65 -->

# How to Build the Axis2 Project's Website

## Installing Maven2

The Axis 2.0 website build system solely depends on [Maven2](http://maven.apache.org/). The build has been
specifically tested to work with Maven version 2.0.7. To install
Maven, download the distributions and follow the instructions in
the documentation. Make sure you don't forget to add MAVEN\_HOME/bin
directory in the path.

## Checking out Axis 2.0

Checkout the [latest
source](http://svn.apache.org/repos/asf/axis/axis2/java/core/trunk) using your favorite SVN client. If you are a committer, get a [commiter
check out.](https://svn.apache.org/repos/asf/axis/axis2/java/core/trunk)

## Building the Site

During maven releases site should have been generated on target/site directory and no special action required. Further [release process guide](#release-process)  describes necessary steps to update Axis2 site with your new modifications.

In case if you want to generate site only you could run *mvn site* on root project of your local copy.

## FAQ

1. How can I update a document in the site ?
   Get a commiter check out. All the documents are in XHTML format
   under the modules/documentation/xdocs folder, and you can change only the documents found
   under this folder. Change the relevant file and run *mvn
   install*. New documentation will be available under
   the target folder.
2. How can I add a new document?
   Add the new document in the xdocs folder. Change the navigation.xml
   found under the xdocs folder by adding a link to the newly added
   document. Re-generate the site.
   Please make sure you have not included any of the illegal
   characters and your document should be well formed.

---

<a id="team-list"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/team-list.html -->

<!-- page_index: 66 -->

## The Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization |
| --- | --- | --- | --- | --- | --- |
|  | saminda | Saminda Abeyruwan | saminda AT wso2.com | - | WSO2 |
|  | azeez | Afkham Azeez | azeez AT wso2.com | <http://www.apache.org/~azeez> | WSO2 |
|  | - | Jeff Barrett | - | - | IBM |
|  | chinthaka | Eran Chinthaka | chinthaka AT wso2.com | <http://www.apache.org/~chinthaka> | WSO2 |
|  | gdaniels | Glen Daniels | gdaniels AT apache.org | - | Sonic Software |
|  | pradine | Brian DePradine | pradine AT uk.ibm.com | - | IBM |
|  | jaliya | Jaliya Ekanayake | jaliya AT opensource.lk | <http://www.apache.org/~jaliya> | Indiana University, USA |
|  | ruchithf | Ruchith Fernando | ruchith AT wso2.com | - | WSO2 |
|  | - | Nicholas Gallardo | - | - | IBM |
|  | thilina | Thilina Gunarathne | thilina AT opensource.lk | - | Lanka Software Foundation |
|  | chathura | Chathura Herath | chathura AT opensource.lk | <http://www.apache.org/~chathura> | Indiana University, USA |
|  | davidillsley | David Illsley | - | <http://www.illsley.org> | IBM |
|  | deepal | Deepal Jayasinghe | deepal AT gatech.org | <http://www.apache.org/~deepal> | Georgia Institute of Technology, USA |
|  | robertlazarski | Robert Lazarski | robertlazarski AT gmail.com | - | Brazil Outsource |
|  | senaka | Senaka Fernando | senaka AT wso2.com | - | WSO2 |
|  | stevel | Steve Loughran | stevel AT apache.org | - | HP labs |
|  | - | Bill Nagy | - | - | IBM |
|  | chatra | Chatra Nakkawita | chatra AT WSO2.com | - | WSO2 |
|  | sumedha | Sumedha Rubasinghe | sumedha AT WSO2.com | - | WSO2 |
|  | charitha | Charitha Kamkanamge | charitha AT WSO2.com | - | WSO2 |
|  | hemapani | Srinath Perera | hemapani AT apache.org | <http://www.apache.org/~hemapani> | Indiana University, USA |
|  | ajith | Ajith Ranabahu | ajith AT wso2.com | <http://www.apache.org/~ajith> | WSO2 |
|  | venkat | Venkat Reddy | vreddyp AT gmail.com | - | Computer Associates |
|  | - | Michael Rheinheimer | - | - | IBM |
|  | - | Ann Robinson | - | - | IBM |
|  | sanka | Sanka Samaranayake | sanka AT wso2.com | - | WSO2 |
|  | scheu | Rich Scheuerle | scheu AT us.ibm.com | - | IBM |
|  | ashu | Ashutosh Shahi | Ashutosh.Shahi AT ca.com | - | Computer Associates |
|  | alek | Aleksander Slominski | aslom AT cs.indiana.edu | - | Indiana University Extreme! Computing Lab |
|  | dsosnoski | Dennis Sosnoski | dms AT sosnoski.com | - | Sosnoski Software |
|  | dims | Davanum Srinivas | davanum AT gmail.com | - | - |
|  | jaya | Jayachandra Sekhara Rao Sunkara | jayachandra AT gmail.com | - | Computer Associates |
|  | nandana | Nandana Mihindukulasooriya | nandana AT wso2.com | - | WSO2 |
|  | - | Nikhil Thaker | - | - | IBM |
|  | chamil | Chamil Thanthrimudalige | chamil AT wso2.com | - | WSO2 |
|  | dasarath | Dasarath Weerathunga | dasarath AT opensource.lk | - | Purdue University, USA |
|  | eranga | Eranga Jayasundera | eranga AT apache.org | - | - |
|  | sanjiva | Sanjiva Weerawarana | sanjiva AT wso2.com | - | WSO2 |
|  | keithc | Keith Chapman | keith AT wso2.com | - | WSO2 |
|  | veithen | Andreas Veithen | veithen AT apache.org | <http://www.linkedin.com/in/aveithen> | - |
|  | ruwan | Ruwan Linton | ruwan AT apache.org | <http://www.linkedin.com/in/ruwanlinton> | - |
|  | sagara | Sagara Gunathunga | sagara AT apache.org | - | WSO2 |
|  | shameera | Shameera Rathnayaka | shameera AT apache.org | <http://lk.linkedin.com/pub/shameera-rathnayaka/1a/661/561> | WSO2 |
|  | isurues | Isuru Suriarachchi | isurues AT apache.org | <https://www.linkedin.com/pub/isuru-suriarachchi/a/58b/b69> | Indiana University |
|  | hiranya | Hiranya Jayathilaka | hiranya AT apache.org | - | UC Santa Barbara |

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization |
| --- | --- | --- | --- |
|  | Gayan Asanka | gayan AT opensource.lk | Lanka Software Foundation |
|  | Dharshana Dias | - | Lanka Software Foundation / University of Moratuwa |
|  | Nadana Gunarathna | nadana AT opensource.lk | Lanka Software Foundation |
|  | Thilini Gunawardhana | thilini AT WSO2.com | WSO2 |
|  | Anushka Kumara | anushkakumar AT gmail.com | Lanka Software Foundation / University of Moratuwa |
|  | Farhaan Mohideen | fmohideen AT valista.com | Lanka Software Foundation |
|  | Chinthaka Thilakarathne | - | Lanka Software Foundation / University of Moratuwa |
|  | Shivantha Huruggamuwa | shivanthah AT gmail.com | University Of Peradeniya , Sri Lanka |
|  | Dobri Kitipov | kdobrik AT gmail.com | Software AG |

---

<a id="issue-tracking"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/issue-tracking.html -->

<!-- page_index: 67 -->

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira).

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/AXIS2
```

---

<a id="thanks"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/thanks.html -->

<!-- page_index: 68 -->

# Special Thanks to ...

| Company | Donation Type |
| --- | --- |
|  | Licenses for IDEA |
|  | Licenses for YourKit |
|  | Licenses for JProfiler |
|  | Licenses for Altova XMLSpy |

---

<a id="tools-maven-plugins-axis2-wsdl2code-maven-plugin-usage"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/maven-plugins/axis2-wsdl2code-maven-plugin/usage.html -->

<!-- page_index: 69 -->

## Usage

axis2-wsdl2code-maven-plugin offers a single goal:

- wsdl2code: Reads the WSDL and generates code.

To run the plugin, add the following section to your POM:

```
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.axis2</groupId>
      <artifactId>axis2-wsdl2code-maven-plugin</artifactId>
      <executions>
        <execution>
          <goals>
            <goal>wsdl2code</goal>
          </goals>
          <configuration>
            <packageName>com.foo.myservice</packageName>
            <wsdlFile>src/main/wsdl/myservice.wsdl</wsdlFile>
            <databindingName>xmlbeans</databindingName>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

The plugin will be invoked automatically in the generate-sources phase.

See the detailed documentation on [properties](#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo) for how to configure the goal.

---

<a id="tools-maven-plugins-axis2-wsdl2code-maven-plugin-plugin-info"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/maven-plugins/axis2-wsdl2code-maven-plugin/plugin-info.html -->

<!-- page_index: 70 -->

## Plugin Documentation

Goals available for this plugin:

| Goal | Description |
| --- | --- |
| [axis2-wsdl2code:wsdl2code](#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo) | A Mojo for generating Java sources from a WSDL. |

### System Requirements

The following specifies the minimum requirements to run this Maven plugin:

|  |  |
| --- | --- |
| Maven | 2.0 |
| JDK | 1.5 |
| Memory | No minimum requirement. |
| Disk Space | No minimum requirement. |

### Usage

You should specify the version in your project's plugin configuration:

```
<project>
  ...
  <build>
    <!-- To define the plugin version in your parent POM -->
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.apache.axis2</groupId>
          <artifactId>axis2-wsdl2code-maven-plugin</artifactId>
          <version>1.7.9</version>
        </plugin>
        ...
      </plugins>
    </pluginManagement>
    <!-- To use the plugin goals in your POM or parent POM -->
    <plugins>
      <plugin>
        <groupId>org.apache.axis2</groupId>
        <artifactId>axis2-wsdl2code-maven-plugin</artifactId>
        <version>1.7.9</version>
      </plugin>
      ...
    </plugins>
  </build>
  ...
</project>
```

For more information, see ["Guide to Configuring Plug-ins"](http://maven.apache.org/guides/mini/guide-configuring-plugins.html)

---

<a id="tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo"></a>

<!-- source_url: https://axis.apache.org/axis2/java/core/tools/maven-plugins/axis2-wsdl2code-maven-plugin/wsdl2code-mojo.html -->

<!-- page_index: 71 -->

## axis2-wsdl2code:wsdl2code

**Full name**:

org.apache.axis2:axis2-wsdl2code-maven-plugin:1.7.9:wsdl2code

**Description**:

A Mojo for generating Java sources from a WSDL.

**Attributes**:

- Requires a Maven 2.0 project to be executed.
- Requires dependency resolution of artifacts in scope: test.
- The goal is thread-safe and supports parallel builds.
- Binds by default to the lifecycle phase: generate-sources.

### Optional Parameters

<table align="left" border="0" class="table table-striped">
<tr>
<th>Name</th>
<th>Type</th>
<th>Since</th>
<th>Description</th>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--allports">allPorts</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Set this to true to generate code for all ports. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--backwardcompatible">backwardCompatible</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--databindingname">databindingName</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>The databinding framework, which is being used by the generated
sources. <b>Default value is</b>: <tt>adb</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--externalmapping">externalMapping</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--flattenfiles">flattenFiles</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--generateallclasses">generateAllClasses</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Whether to generate simply all classes. This is only valid in
conjunction with "generateServerSide". <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--generateserverside">generateServerSide</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Whether server side sources are being generated. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--generateserversideinterface">generateServerSideInterface</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Whether to generate the server side interface. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--generateservicesxml">generateServicesXml</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Whether a "services.xml" file is being generated. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--generatetestcase">generateTestcase</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Whether a test case is being generated. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--httpproxyhost">httpProxyHost</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--httpproxypassword">httpProxyPassword</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--httpproxyport">httpProxyPort</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--httpproxyuser">httpProxyUser</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--jibxbindingfile">jibxBindingFile</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>The binding file for JiBX databinding. </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--language">language</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>The programming language of the generated sources. <b>Default value is</b>: <tt>java</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--namespacetopackages">namespaceToPackages</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>Map of namespace URI to packages in the format
<tt>uri1=package1,uri2=package2,...</tt>. Using this parameter
is discouraged. In general, you should use the
<tt>namespaceUris</tt> parameter. However, the latter cannot be
set on the command line. </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--namespaceuris">namespaceURIs</a></b></td>
<td><tt>NamespaceURIMapping[]</tt></td>
<td><tt>-</tt></td>
<td>Map of namespace URI to packages. Example:

<div>
<pre>
&lt;namespaceURIs&gt;
  &lt;namespaceURI&gt;
    &lt;uri&gt;uri1&lt;/uri&gt;
    &lt;packageName&gt;package1&lt;/packageName&gt;
  &lt;/namespaceURI&gt;
  ...
&lt;/namespaceURI&gt;
</pre></div>
</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--options">options</a></b></td>
<td><tt>Properties</tt></td>
<td><tt>-</tt></td>
<td>Specify databinding specific extra options </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--outputdirectory">outputDirectory</a></b></td>
<td><tt>File</tt></td>
<td><tt>-</tt></td>
<td>The output directory, where the generated sources are being
created. <b>Default value is</b>: <tt>${project.build.directory}/generated-sources/axis2/wsdl2code</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--overwrite">overWrite</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--packagename">packageName</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>Package name of the generated sources; will be used to create a
package structure below the output directory. </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--portname">portName</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>Port name, for which to generate sources. By default, sources will
be generated for a randomly picked port. </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--repositorypath">repositoryPath</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--servicename">serviceName</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>Service name, for which to generate sources. By default, sources
will be generated for all services. </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--skipbuildxml">skipBuildXML</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--skipmessagereceiver">skipMessageReceiver</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--skipwsdl">skipWSDL</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--suppressprefixes">suppressPrefixes</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--syncmode">syncMode</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>Mode, for which sources are being generated; either of "sync",
"async" or "both". <b>Default value is</b>: <tt>both</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--targetresourcesfolderlocation">targetResourcesFolderLocation</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--targetsourcefolderlocation">targetSourceFolderLocation</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) <b>Default value is</b>: <tt>src</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--unpackclasses">unpackClasses</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>Whether to unpack classes. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--unwrap">unwrap</a></b></td>
<td><tt>boolean</tt></td>
<td><tt>-</tt></td>
<td>This will select between wrapped and unwrapped during code
generation. Maps to the -uw option of the command line tool. <b>Default value is</b>: <tt>false</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--wsdlfile">wsdlFile</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>The WSDL file, which is being read. <b>Default value is</b>: <tt>src/main/resources/service.wsdl</tt>.</td>
</tr>
<tr>
<td><b><a href="#tools-maven-plugins-axis2-wsdl2code-maven-plugin-wsdl2code-mojo--wsdlversion">wsdlVersion</a></b></td>
<td><tt>String</tt></td>
<td><tt>-</tt></td>
<td>(no description) </td>
</tr>
</table>

### Parameter Details

**allPorts:**

Set this to true to generate code for all ports.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.allPorts}
- **Default**: false

---

**backwardCompatible:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.backwardCompatible}
- **Default**: false

---

**databindingName:**

The databinding framework, which is being used by the generated
sources.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.databindingName}
- **Default**: adb

---

**externalMapping:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.externalMapping}

---

**flattenFiles:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.flattenFiles}
- **Default**: false

---

**generateAllClasses:**

Whether to generate simply all classes. This is only valid in
conjunction with "generateServerSide".

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.generateAllClasses}
- **Default**: false

---

**generateServerSide:**

Whether server side sources are being generated.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.generateServerSide}
- **Default**: false

---

**generateServerSideInterface:**

Whether to generate the server side interface.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.generateServerSideInterface}
- **Default**: false

---

**generateServicesXml:**

Whether a "services.xml" file is being generated.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.generateServicesXml}
- **Default**: false

---

**generateTestcase:**

Whether a test case is being generated.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.generateTestCase}
- **Default**: false

---

**httpProxyHost:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.http-proxy-host}

---

**httpProxyPassword:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.http-proxy-password}

---

**httpProxyPort:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.http-proxy-port}

---

**httpProxyUser:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.http-proxy-user}

---

**jibxBindingFile:**

The binding file for JiBX databinding.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.jibxBindingFile}

---

**language:**

The programming language of the generated sources.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.language}
- **Default**: java

---

**namespaceToPackages:**

Map of namespace URI to packages in the format
uri1=package1,uri2=package2,.... Using this parameter
is discouraged. In general, you should use the
namespaceUris parameter. However, the latter cannot be
set on the command line.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.namespaceToPackages}

---

**namespaceURIs:**

Map of namespace URI to packages. Example:

```

<namespaceURIs>
  <namespaceURI>
    <uri>uri1</uri>
    <packageName>package1</packageName>
  </namespaceURI>
  ...
</namespaceURI>
```

- **Type**: org.apache.axis2.maven2.wsdl2code.NamespaceURIMapping[]
- **Required**: No

---

**options:**

Specify databinding specific extra options

- **Type**: java.util.Properties
- **Required**: No
- **Expression**: ${axis2.java2wsdl.options}

---

**outputDirectory:**

The output directory, where the generated sources are being
created.

- **Type**: java.io.File
- **Required**: No
- **Expression**: ${axis2.wsdl2code.target}
- **Default**: ${project.build.directory}/generated-sources/axis2/wsdl2code

---

**overWrite:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.overWrite}
- **Default**: false

---

**packageName:**

Package name of the generated sources; will be used to create a
package structure below the output directory.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.package}

---

**portName:**

Port name, for which to generate sources. By default, sources will
be generated for a randomly picked port.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.portName}

---

**repositoryPath:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.repositoryPath}

---

**serviceName:**

Service name, for which to generate sources. By default, sources
will be generated for all services.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.serviceName}

---

**skipBuildXML:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.skipBuildXML}
- **Default**: false

---

**skipMessageReceiver:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.skipMessageReceiver}
- **Default**: false

---

**skipWSDL:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.skipWSDL}
- **Default**: false

---

**suppressPrefixes:**

(no description)

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.suppressPrefixes}
- **Default**: false

---

**syncMode:**

Mode, for which sources are being generated; either of "sync",
"async" or "both".

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.syncMode}
- **Default**: both

---

**targetResourcesFolderLocation:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.targetResourcesFolderLocation}

---

**targetSourceFolderLocation:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.targetSourceFolderLocation}
- **Default**: src

---

**unpackClasses:**

Whether to unpack classes.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.unpackClasses}
- **Default**: false

---

**unwrap:**

This will select between wrapped and unwrapped during code
generation. Maps to the -uw option of the command line tool.

- **Type**: boolean
- **Required**: No
- **Expression**: ${axis2.wsdl2code.unwrap}
- **Default**: false

---

**wsdlFile:**

The WSDL file, which is being read.

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.wsdlFile}
- **Default**: src/main/resources/service.wsdl

---

**wsdlVersion:**

(no description)

- **Type**: java.lang.String
- **Required**: No
- **Expression**: ${axis2.wsdl2code.wsdlVersion}

---
