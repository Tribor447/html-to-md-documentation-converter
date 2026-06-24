# Apache Synapse – Apache Synapse - Installation Guide

## Navigation

- Documentation
  - [Installation Guide](#installation)
  - [Quick Start Guide](#quick_start)
  - [Samples Setup Guide](#samples-setup)
  - [Samples Catalog](#samples)
  - [Configuration Language](#config)
  - [Mediators Catalog](#mediators)
  - [Transports Catalog](#transports)
  - [Properties Catalog](#properties)
  - [XPath functions and Variables](#xpath)
  - [Extending Synapse](#extending)
  - [Synapse Template Libraries](#template_library)
  - [Upgrading](#upgrading)
  - [Deployment](#deployment)
  - [FAQ](#faq)

## Content

<a id="installation"></a>

<!-- source_url: https://synapse.apache.org/userguide/installation.html -->

<!-- page_index: 1 -->

<a id="installation--apache-synapse-installation-guide"></a>

## Apache Synapse Installation Guide

Welcome to Apache Synapse Installation Guide. This guide provides information on,

- [Prerequisites for Installing Apache Synapse](#installation--prerequisites)
- [Distribution Packages](#installation--distribution)
- [Installing Synapse](#installation--installing)
  - [Installing on \*nix (Linux/macOS/Solaris)](#installation--installinglinux)
  - [Installing on MS Windows](#installation--installingwin)
- [Building Synapse Using the Source Distribution](#installation--building)

<a id="installation--prerequisites-for-installing-apache-synapse"></a>

## Prerequisites for Installing Apache Synapse

You should have following pre-requisites installed on your system to run Apache
Synapse.

[Java SE
Development Kit](http://java.sun.com/javase/downloads/index.jsp)

1.8.0\_141 or higher (For instructions on setting up the JDK on different
operating systems, visit[Java homepage.](http://www.oracle.com/technetwork/java/index.html))

[Apache Ant](http://ant.apache.org/) - To run Synapse samples

To compile and run the sample clients, an Ant installation is
required.
Ant 1.7.0 version or higher is recommended.

[Apache Maven](http://maven.apache.org/) - To
build Synapse from the source

To build Apache Synapse from its source distribution, you will need
Maven 3.2.x or later.

Memory

No minimum requirement - A heap size of 1GB is generally
sufficient to process typical SOAP messages. Requirements may vary
with larger message size and on the number of messages processed
concurrently.

Disk

No minimum requirement. The installation will require ~75 MB
excluding space allocated for log files and databases.

Operating System

Linux, Solaris, macOS, MS Windows - XP/2003/2008 (Not fully tested on Windows
Vista/7/8/10). Since Apache Synapse is a Java application, it will
generally be possible to run it on other operating systems with a
JDK 1.6.x or higher runtime. Linux is recommended for production
deployments.

<a id="installation--distribution-packages"></a>

## Distribution Packages

The following distribution packages are available for [download](http://synapse.apache.org/download.html).

1. Binary Distribution: Includes binary files for Linux, macOS and
   MS Windows operating systems, compressed into a single zip file. Recommended
   for normal users.
2. Source Distribution: Includes the source code for Linux, macOS and MS Windows
   operating systems, compressed into a single zip file which can be used to build
   the binaries. Recommended for advanced users.

<a id="installation--installing-synapse"></a>

## Installing Synapse

The following guide will take you through the binary distribution installation
on different platforms.

<a id="installation--installing-on-nix-linux-macos-solaris"></a>

### Installing on \*nix (Linux/macOS/Solaris)

1. [Download](http://synapse.apache.org/download.html) Apache
   Synapse binary distribution.
2. Extract the downloaded zip archive to where you want Synapse installed
   (e.g. into /opt).
3. Set the JAVA\_HOME environment variable to your Java home using the export
   command or by editing /etc/profile, and add the JAVA\_HOME/bin
   directory to your PATH.
4. Execute the Synapse start script or the daemon script from the bin
   directory of your Synapse installation.
   i.e., ./synapse.sh OR ./synapse-daemon.sh start
5. Synapse is now ready to accept messages for mediation.

<a id="installation--installing-on-ms-windows"></a>

### Installing on MS Windows

1. [Download](http://synapse.apache.org/download.html) Apache
   Synapse binary distribution.
2. Extract the downloaded zip archive to where you want Synapse installed
   (e.g. into C:\Synapse).
3. Set the JAVA\_HOME environment variable to your Java home using the set
   command or Windows System Properties dialog, and add the JAVA\_HOME\bin
   directory to your PATH.
4. Execute the Synapse start script or the service installation script from
   the bin directory of your Synapse installation.
   i.e., synapse.bat OR install-synapse-service.bat
5. Synapse is now ready to accept messages for mediation.

<a id="installation--building-synapse-using-the-source-distribution"></a>

## Building Synapse Using the Source Distribution

Apache Synapse build is based on  [Apache
Maven 3](http://maven.apache.org/). Hence, it is a prerequisite to have Maven (version 3.2.0 or later)
installed in order to build Synapse from the source distribution. Instructions on
installing Maven 3 are available on the  [Maven
website](http://maven.apache.org/). Follow these steps to build Synapse after setting up Maven 3.

1. [Download](http://synapse.apache.org/download.html)
   the source
   distribution, which is available as a zip archive. All the necessary
   build scripts are included with this distribution.
   Alternatively Synapse can be cloned from the Github [repository](https://github.com/apache/synapse).
2. Extract the source archive to a directory of your choice. If cloned from Github repository,
   change directories into downloaded project root.
3. Run **mvn clean install** command inside that directory to build
   Synapse. Note that you will require a connection to the Internet for the Maven
   build to download dependencies required for the build.

This will create the complete set of release artifacts including the binary
distribution in the modules/distribution/target/ directory which can be installed
using the above instructions.

---

<a id="quick_start"></a>

<!-- source_url: https://synapse.apache.org/userguide/quick_start.html -->

<!-- page_index: 2 -->

<a id="quick_start--quick-start-guide"></a>

## Quick Start Guide

Welcome to Apache Synapse quick start guide. This tutorial demonstrates two
sample applications covering the fundamental usage scenarios of Synapse, namely
message mediation and service mediation. It starts from the absolute beginning and
walks you through a series of steps while giving a firm grasp on the Synapse
messaging model.

<a id="quick_start--pre-requisites"></a>

## Pre-requisites

You should have following pre-requisites installed on your system to
follow this tutorial.

- A Java runtime - JDK or JRE of version 1.6.0\_23 or higher
- Apache Ant <http://ant.apache.org>

<a id="quick_start--installing-synapse"></a>

## Installing Synapse

Let's start by downloading Apache Synapse. Launch a web browser and navigate to
the [Synapse Downloads](https://synapse.apache.org/download.html) page. Download the binary distribution
of the latest release. Binary distributions are available in standard zip
format and Unix tar ball format.

Once downloaded you can install Synapse by simply extracting the archive to
a suitable location on your local disk. When extracted, a directory named
synapse with the corresponding version number will be created. This directory
houses all the libraries, configuration files, scripts and other artifacts
used by the Synapse runtime. From now on we will refer to this directory as
{SYNAPSE\_HOME}. So for an example {SYNAPSE\_HOME}/bin refers to the subdirectory
named 'bin' which is generally available in the Synapse installation.

<a id="quick_start--running-the-axis2-server"></a>

## Running the Axis2 Server

Samples described in this tutorial involve routing messages to a Web Service
through the Synapse ESB. In real world applications, these Web Services could be
hosted in a web server in your organization, or practically anywhere in the
Internet. In this tutorial we will be using a sample Web Service that ships with
Synapse and we will deploy it in the sample Axis2 server that comes bundled with
Synapse.

To deploy the sample service in the Axis2 server, go to
{SYNAPSE\_HOME}/samples/axis2Server/src/SimpleStockQuoteService directory and run
'ant'. You will see an output similar to the following as the service is built
and deployed to the sample Axis2 server.

user@domain:/opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService$ ant
Buildfile: build.xml
clean:
init:
[mkdir] Created dir: /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp
[mkdir] Created dir: /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp/classes
[mkdir] Created dir: /opt/synapse-3.0.1/samples/axis2Server/repository/services
compile-all:
[javac] Compiling 9 source files to /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp/classes
build-service:
[mkdir] Created dir: /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp/SimpleStockQuote
[mkdir] Created dir: /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp/SimpleStockQuote/META-INF
[copy] Copying 1 file to /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp/SimpleStockQuote/META-INF
[copy] Copying 9 files to /opt/synapse-3.0.1/samples/axis2Server/src/SimpleStockQuoteService/temp/SimpleStockQuote
[jar] Building jar: /opt/synapse-3.0.1/samples/axis2Server/repository/services/SimpleStockQuoteService.aar
BUILD SUCCESSFUL
Total time: 1 second

Now go to {SYNAPSE\_HOME}/samples/axis2Server directory and start the sample server
by executing the following command.

Linux / Unix: . axis2server.sh
Windows: axis2server.bat

This will start the Axis2 server on HTTP port 9000. You can see the WSDL of the
sample service by launching your web browser and navigating to the URL
http://localhost:9000/services/SimpleStockQuoteService?wsdl.

<a id="quick_start--message-mediation"></a>

## Message Mediation

Now we are all set to try our first scenario with Synapse. We will be starting
Synapse using the sample configuration found in synapse\_sample\_0.xml file which
resides in {SYNAPSE\_HOME}/repository/conf/sample directory. This configuration
enables Synapse to log all the messages passing through the service bus:

<definitions xmlns="http://ws.apache.org/ns/synapse">
<sequence name="main">
<log level="full"/>
<send/>
</sequence>
</definitions>

To start the ESB with the above configuration go the {SYNAPSE\_HOME}/bin directory
and execute the following command.

Linux / Unix: . synapse.sh -sample 0
Windows: synapse.bat -sample 0

Following messages will be displayed on the console as Synapse boots up with the
above configuration.

Starting Synapse/Java ...
Using SYNAPSE\_HOME: /opt/synapse-3.0.1
Using JAVA\_HOME: /opt/jdk1.7.0\_79
Using SYNAPSE\_XML: /opt/synapse-3.0.1/repository/conf/sample/synapse\_sample\_0.xml
2016-12-28 10:38:00,456 [-] [main] INFO SynapseServer Starting Apache Synapse...
2016-12-28 10:38:00,476 [-] [main] INFO SynapseControllerFactory Using Synapse home : /opt/synapse-3.0.1
2016-12-28 10:38:00,476 [-] [main] INFO SynapseControllerFactory Using Axis2 repository : /opt/synapse-3.0.1/repository
2016-12-28 10:38:00,476 [-] [main] INFO SynapseControllerFactory Using axis2.xml location : /opt/synapse-3.0.1/repository/conf/axis2.xml
2016-12-28 10:38:00,476 [-] [main] INFO SynapseControllerFactory Using synapse.xml location : /opt/synapse-3.0.1/repository/conf/sample/synapse\_sample\_0.xml
2016-12-28 10:38:00,476 [-] [main] INFO SynapseControllerFactory Using server name : localhost
2016-12-28 10:38:00,493 [-] [main] INFO SynapseControllerFactory The timeout handler will run every : 15s
2016-12-28 10:38:00,566 [-] [main] INFO Axis2SynapseController Initializing Synapse at : Wed Dec 28 10:38:00 IST 2016
2016-12-28 10:38:01,140 [-] [main] INFO PassThroughHttpSSLSender Loading Identity Keystore from : lib/identity.jks
2016-12-28 10:38:01,174 [-] [main] INFO PassThroughHttpSSLSender Loading Trust Keystore from : lib/trust.jks
2016-12-28 10:38:01,242 [-] [main] INFO PassThroughHttpSSLSender Pass-through HTTPS sender started...
2016-12-28 10:38:01,243 [-] [main] INFO PassThroughHttpSender Pass-through HTTP sender started...
2016-12-28 10:38:01,249 [-] [main] INFO JMSSender JMS Sender started
2016-12-28 10:38:01,250 [-] [main] INFO JMSSender JMS Transport Sender initialized...
2016-12-28 10:38:01,251 [-] [main] INFO VFSTransportSender VFS Sender started
2016-12-28 10:38:01,428 [-] [main] INFO PassThroughHttpSSLListener Loading Identity Keystore from : lib/identity.jks
2016-12-28 10:38:01,429 [-] [main] INFO PassThroughHttpSSLListener Loading Trust Keystore from : lib/trust.jks
2016-12-28 10:38:01,443 [-] [main] INFO Axis2SynapseController Loading mediator extensions...
2016-12-28 10:38:01,451 [-] [main] INFO XMLConfigurationBuilder Generating the Synapse configuration model by parsing the XML configuration
2016-12-28 10:38:01,506 [-] [main] INFO SynapseConfigurationBuilder Loaded Synapse configuration from : /opt/synapse-3.0.1/repository/conf/sample/synapse\_sample\_0.xml
2016-12-28 10:38:01,542 [-] [main] INFO Axis2SynapseController Deploying the Synapse service...
2016-12-28 10:38:01,563 [-] [main] INFO Axis2SynapseController Deploying Proxy services...
2016-12-28 10:38:01,563 [-] [main] INFO Axis2SynapseController Deploying EventSources...
2016-12-28 10:38:01,584 [-] [main] INFO PassThroughHttpSSLListener Starting pass-through HTTPS listener...
2016-12-28 10:38:01,601 [-] [main] INFO PassThroughHttpSSLListener Pass-through HTTPS listener started on port: 8243
2016-12-28 10:38:01,601 [-] [main] INFO PassThroughHttpListener Starting pass-through HTTP listener...
2016-12-28 10:38:01,603 [-] [main] INFO PassThroughHttpListener Pass-through HTTP listener started on port: 8280
2016-12-28 10:38:01,603 [-] [main] INFO Axis2SynapseController Management using JMX available via: service:jmx:rmi:///jndi/rmi://localhost:1099/synapse
2016-12-28 10:38:01,606 [-] [main] INFO TimeoutHandler This engine will expire all callbacks after : 180 seconds, irrespective of the timeout action, after the specified or optional timeout
2016-12-28 10:38:01,607 [-] [main] INFO ServerManager Server ready for processing...
2016-12-28 10:38:01,608 [-] [main] INFO SynapseServer Apache Synapse started successfully

Note that by default Synapse listens for HTTP requests on port 8280.

<a id="quick_start--executing-the-sample-client"></a>

### Executing the Sample Client

Now we have a Web Service hosted in Axis2 and a Synapse ESB instance which
is configured to log and route messages. All that is left is to send some requests
to Synapse and see the magic happen. Synapse comes bundled with a sample
Web Service client that can be used to send different kinds of requests. Go to
{SYNAPSE\_HOME}/samples/axis2Client directory and execute the following command
to send a request to Synapse.

ant stockquote -Daddurl=http://localhost:9000/services/SimpleStockQuoteService -Dtrpurl=http://localhost:8280 -Dmode=quote -Dsymbol=IBM

You should get the following output on the conosle.

Buildfile: build.xml
init:
[mkdir] Created dir: /opt/synapse-3.0.1/samples/axis2Client/target/classes
compile:
[javac] Compiling 22 source files to /opt/synapse-3.0.1/samples/axis2Client/target/classes
[javac] Note: /opt/synapse-3.0.1/samples/axis2Client/src/samples/userguide/PWCallback.java uses or overrides a deprecated API.
[javac] Note: Recompile with -Xlint:deprecation for details.
[javac] Note: /opt/synapse-3.0.1/samples/axis2Client/src/samples/userguide/LoadbalanceFailoverClient.java uses unchecked or unsafe operations.
[javac] Note: Recompile with -Xlint:unchecked for details.
stockquote:
[java] 2010-11-26 01:35:16,485 [-] [main] INFO MailTransportSender MAILTO Sender started
[java] 2010-11-26 01:35:16,496 [-] [main] INFO JMSSender JMS Sender started
[java] 2010-11-26 01:35:16,497 [-] [main] INFO JMSSender JMS Transport Sender initialized...
[java] Standard :: Stock price = $99.14593325984416
BUILD SUCCESSFUL
Total time: 5 seconds

This sends a stock quote request for the symbol 'IBM' with the transport URL set
to http://localhost:8280 (Synapse) and the WS-Addressing EPR set to
http://localhost:9000/services/SimpleStockQuoteService (Axis2). Synapse first
logs the message and then forwards it to the URL given in the WS-Addressing
headers. The actual message sent by the client is as follows.

POST / HTTP/1.1
Content-Type: text/xml; charset=UTF-8
SOAPAction: "urn:getQuote"
User-Agent: Axis2
Host: 127.0.0.1
Transfer-Encoding: chunked
218
<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Header>
<wsa:To>http://localhost:9000/services/SimpleStockQuoteService</wsa:To>
<wsa:MessageID>urn:uuid:D538B21E30B32BB8291177589283717</wsa:MessageID>
<wsa:Action>urn:getQuote</wsa:Action>
</soapenv:Header>
<soapenv:Body>
<m0:getQuote xmlns:m0="http://services.samples">
<m0:request>
<m0:symbol>IBM</m0:symbol>
</m0:request>
</m0:getQuote>
</soapenv:Body>
</soapenv:Envelope>0

Now take a look at the console running Synapse. You will see that all the
details of the mediation are logged along with all the SOAP messages
passed through Synapse. If you execute Synapse in debug mode by editing
the lib/log4j.properties file and setting "log4j.category.org.apache.synapse"
as "DEBUG" instead of INFO, you will see even more information as follows after
a restart and on replay of the above scenario.

2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG SynapseMessageReceiver Synapse received a new message for message mediation...
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG SynapseMessageReceiver Received To: http://localhost:9000/services/SimpleStockQuoteService
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG SynapseMessageReceiver SOAPAction: urn:getQuote
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG SynapseMessageReceiver WSA-Action: urn:getQuote
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG Axis2SynapseEnvironment Injecting MessageContext
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG Axis2SynapseEnvironment Using Main Sequence for injected message
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG SequenceMediator Start : Sequence <main>
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG SequenceMediator Sequence <SequenceMediator> :: mediate()
2012-09-18 09:46:57,909 [-] [HttpServerWorker-2] DEBUG LogMediator Start : Log mediator
2012-09-18 09:46:57,910 [-] [HttpServerWorker-2] INFO LogMediator To: http://localhost:9000/services/SimpleStockQuoteService, WSAction: urn:getQuote, SOAPAction: urn:getQuote, ReplyTo: http://www.w3.org/2005/08/addressing/anonymous, MessageID: urn:uuid:754cc296-ff58-4875-a999-3a33ec94c8a1, Direction: request, Envelope: <?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Header xmlns:wsa="http://www.w3.org/2005/08/addressing"><wsa:To>http://localhost:9000/services/SimpleStockQuoteService</wsa:To><wsa:MessageID>urn:uuid:754cc296-ff58-4875-a999-3a33ec94c8a1</wsa:MessageID><wsa:Action>urn:getQuote</wsa:Action></soapenv:Header><soapenv:Body><m0:getQuote xmlns:m0="http://services.samples"><m0:request><m0:symbol>IBM</m0:symbol></m0:request></m0:getQuote></soapenv:Body></soapenv:Envelope>
2012-09-18 09:46:57,910 [-] [HttpServerWorker-2] DEBUG LogMediator End : Log mediator
2012-09-18 09:46:57,910 [-] [HttpServerWorker-2] DEBUG SendMediator Start : Send mediator
2012-09-18 09:46:57,910 [-] [HttpServerWorker-2] DEBUG SendMediator Sending request message using implicit message properties..
Sending To: http://localhost:9000/services/SimpleStockQuoteService
SOAPAction: urn:getQuote
2012-09-18 09:46:57,910 [-] [HttpServerWorker-2] DEBUG Axis2FlexibleMEPClient Sending [add = false] [sec = false] [rm = false] [to=Address: http://localhost:9000/services/SimpleStockQuoteService]
2012-09-18 09:46:57,910 [-] [HttpServerWorker-2] DEBUG Axis2FlexibleMEPClient Message [Original Request Message ID : urn:uuid:754cc296-ff58-4875-a999-3a33ec94c8a1] [New Cloned Request Message ID : urn:uuid:835c68a7-0645-496d-9acc-1d84a03ccb09]
2012-09-18 09:46:57,911 [-] [HttpServerWorker-2] DEBUG SynapseCallbackReceiver Callback added. Total callbacks waiting for : 1
2012-09-18 09:46:57,912 [-] [HttpServerWorker-2] DEBUG SendMediator End : Send mediator
2012-09-18 09:46:57,912 [-] [HttpServerWorker-2] DEBUG SequenceMediator End : Sequence <main>
2012-09-18 09:46:58,035 [-] [HttpClientWorker-2] DEBUG SynapseCallbackReceiver Callback removed for request message id : urn:uuid:835c68a7-0645-496d-9acc-1d84a03ccb09. Pending callbacks count : 0
2012-09-18 09:46:58,035 [-] [HttpClientWorker-2] DEBUG SynapseCallbackReceiver Synapse received an asynchronous response message
2012-09-18 09:46:58,035 [-] [HttpClientWorker-2] DEBUG SynapseCallbackReceiver Received To: null
2012-09-18 09:46:58,035 [-] [HttpClientWorker-2] DEBUG SynapseCallbackReceiver SOAPAction:
2012-09-18 09:46:58,035 [-] [HttpClientWorker-2] DEBUG SynapseCallbackReceiver WSA-Action:
2012-09-18 09:46:58,036 [-] [HttpClientWorker-2] DEBUG SynapseCallbackReceiver Body :
<?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns:getQuoteResponse xmlns:ns="http://services.samples"><ns:return xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns:GetQuoteResponse"><ns:change>4.158253518011668</ns:change><ns:earnings>13.000214652478554</ns:earnings><ns:high>176.07121446241788</ns:high><ns:last>171.44223855674258</ns:last><ns:lastTradeTimestamp>Tue Sep 18 09:46:57 CEST 2012</ns:lastTradeTimestamp><ns:low>-169.3791832231285</ns:low><ns:marketCap>3.844340450887613E7</ns:marketCap><ns:name>IBM Company</ns:name><ns:open>-167.9098655007073</ns:open><ns:peRatio>-17.815829214870217</ns:peRatio><ns:percentageChange>-2.4400099237243</ns:percentageChange><ns:prevClose>-170.41953303471544</ns:prevClose><ns:symbol>IBM</ns:symbol><ns:volume>16090</ns:volume></ns:return></ns:getQuoteResponse></soapenv:Body></soapenv:Envelope>
2012-09-18 09:46:58,036 [-] [HttpClientWorker-2] DEBUG Axis2SynapseEnvironment Injecting MessageContext
2012-09-18 09:46:58,036 [-] [HttpClientWorker-2] DEBUG Axis2SynapseEnvironment Using Main Sequence for injected message
2012-09-18 09:46:58,036 [-] [HttpClientWorker-2] DEBUG SequenceMediator Start : Sequence <main>
2012-09-18 09:46:58,036 [-] [HttpClientWorker-2] DEBUG SequenceMediator Sequence <SequenceMediator> :: mediate()
2012-09-18 09:46:58,036 [-] [HttpClientWorker-2] DEBUG LogMediator Start : Log mediator
2012-09-18 09:46:58,037 [-] [HttpClientWorker-2] INFO LogMediator To: http://www.w3.org/2005/08/addressing/anonymous, WSAction: , SOAPAction: , ReplyTo: http://www.w3.org/2005/08/addressing/anonymous, MessageID: urn:uuid:835c68a7-0645-496d-9acc-1d84a03ccb09, Direction: response, Envelope: <?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><ns:getQuoteResponse xmlns:ns="http://services.samples"><ns:return xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns:GetQuoteResponse"><ns:change>4.158253518011668</ns:change><ns:earnings>13.000214652478554</ns:earnings><ns:high>176.07121446241788</ns:high><ns:last>171.44223855674258</ns:last><ns:lastTradeTimestamp>Tue Sep 18 09:46:57 CEST 2012</ns:lastTradeTimestamp><ns:low>-169.3791832231285</ns:low><ns:marketCap>3.844340450887613E7</ns:marketCap><ns:name>IBM Company</ns:name><ns:open>-167.9098655007073</ns:open><ns:peRatio>-17.815829214870217</ns:peRatio><ns:percentageChange>-2.4400099237243</ns:percentageChange><ns:prevClose>-170.41953303471544</ns:prevClose><ns:symbol>IBM</ns:symbol><ns:volume>16090</ns:volume></ns:return></ns:getQuoteResponse></soapenv:Body></soapenv:Envelope>
2012-09-18 09:46:58,037 [-] [HttpClientWorker-2] DEBUG LogMediator End : Log mediator
2012-09-18 09:46:58,037 [-] [HttpClientWorker-2] DEBUG SendMediator Start : Send mediator
2012-09-18 09:46:58,037 [-] [HttpClientWorker-2] DEBUG SendMediator Sending response message using implicit message properties..
Sending To: http://www.w3.org/2005/08/addressing/anonymous
SOAPAction:
2012-09-18 09:46:58,038 [-] [HttpClientWorker-2] DEBUG SendMediator End : Send mediator
2012-09-18 09:46:58,038 [-] [HttpClientWorker-2] DEBUG SequenceMediator End : Sequence <main>

And with that you have successfully completed the first part of this guide. Now let's
look at the next scenario, service mediation with proxy services.

<a id="quick_start--service-mediation-proxy-services"></a>

## Service Mediation (Proxy Services)

As the name implies, a proxy service acts as an intermediary service hosted in
Synapse, and typically fronts an existing service endpoint. A proxy service can be
created and exposed on a different transport, schema, WSDL, or QoS setup (such
as WS-Security, WS-Reliable Messaging) than the real service. Proxy services
are capable of mediating requests before they are delivered to the actual
endpoint. Similarly responses from the actual service can be mediated before
they are sent back to the client.

Clients can send proxy service requests directly to Synapse. From the client's
perspective, proxy services are simply Web Services hosted on Synapse. They can
append the '?wsdl' suffix to the proxy service endpoints to get the WSDLs of these
virtual services. But in the Synapse configuration, service requests can be handled
in anyway you like. Most obvious thing would be to do some processing on the
message and send it to the actual service, which could be running on a different host.
But it is not necessary to always send the messages to an actual service. You may
list any combination of tasks to be performed on the messages received by
the proxy service and terminate the flow or send some response back to the
client even without sending it to any service.

Let's explore a simple proxy services scenario step-by-step to get a better feeling.
As you have downloaded and installed Synapse in the previous section, now you
just run the scenario straightaway. This scenario also requires the same stock
quote service we used in the previous example. So have it deployed in Axis2 and make
sure Axis2 server is up and running.

We are going to start Synapse with a configuration which contains a proxy service.
The configuration in synapse\_sample\_150.xml file in repository/conf/sample directory
matches well with the scope of this tutorial.

<definitions xmlns="http://synapse.apache.org/ns/2010/04/configuraiton">
<proxy name="StockQuoteProxy">
<target>
<endpoint>
<address uri="http://localhost:9000/services/SimpleStockQuoteService"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
<publishWSDL uri="file:repository/conf/sample/resources/proxy/sample\_proxy\_1.wsdl"/>
</proxy>
</definitions>

The above configuration exposes a proxy service named StockQuoteProxy
and specifies an endpoint
(http://localhost:9000/services/SimpleStockQuoteService) as the target for the
proxy service. Therefore, messages coming to the proxy service will be
directed to the address http://localhost:9000/services/SimpleStockQuoteService
specified in the endpoint. There is also an out sequence for the proxy
service, which will be executed for response messages. In the out sequence, we just send the messages back to the client. The publishWSDL tag
specifies an WSDL to be published for this proxy service. Let's start
Synapse with this sample configuration by running the below command from
the {SYNAPSE\_HOME}/bin directory.

Linux / Unix: . synapse.sh -sample 150
Windows: synapse.bat -sample 150

Synapse will display a set of messages as it boots up just like in the previous
section describing the start-up procedure. Before running the client, it
is time to observe another feature of proxy services. That is displaying
the published WSDL. Just open a web browser and point it to the URL
http://localhost:8280/services/StockQuoteProxy?wsdl. You will see the
sample\_proxy\_1.wsdl specified in the configuration but containing the
correct EPRs for the service over HTTP/S.

<a id="quick_start--executing-the-sample-client-2"></a>

### Executing the Sample Client

Now we can invoke the proxy service by sending a request from our sample Axis2
client. Go to the {SYNAPSE\_HOME}/samples/axis2Client directory and run the
following command.

ant stockquote -Dtrpurl=http://localhost:8280/services/StockQuoteProxy -Dmode=quote -Dsymbol=IBM

The above command sends a stock quote request directly to the provided
transport endpoint at http://localhost:8280/services/StockQuoteProxy. The
proxy service will forward the message to the Axis2 server and route the
response from Axis2 back to the client. You will see the response from the
server displayed on the console as follows:

Standard :: Stock price = $165.32687331383468

<a id="quick_start--more-on-proxy-services"></a>

### More on Proxy Services

Proxy services are among the most powerful functional components of Apache
Synapse. They can be used to perform transport switching, message format
switching and lot more. This quick start tutorial only covers the simple
usecases of proxy services. Please refer samples #150 and above in the
Synapse samples catalog, for in depth coverage on more advanced use cases.

<a id="quick_start--conclusion"></a>

## Conclusion

This brings the Synapse quick start guide to an end. Now it is time to go
deeper and discover the advanced features of Synapse. You can browse through
the array of samples for your interested areas. If you have any issue regarding
Synapse as a user, feel free write to the Synapse user mailing list
(<http://synapse.apache.org/mail-lists.html>).

---

<a id="samples-setup"></a>

<!-- source_url: https://synapse.apache.org/userguide/samples/setup/index.html -->

<!-- page_index: 3 -->

<a id="samples-setup--introduction"></a>

## Introduction

Apache Synapse comes with a collection of working examples that demonstrates the
basic features of the Synapse ESB. In addition to the sample configurations, a set
of sample client applications and services are provided which can be used to try out
each of the examples. Most examples are self contained and can be run without any third
party applications or libraries. A set of Ant build files and scripts are provided
to make setting up the examples easier. A few examples however require deploying
certain external libraries and using third party client applications.

The main objectives of this article are:

- Introduce the concept of Synapse samples
- Describe how to setup the environment for running samples
- Describe how to run the sample client applications and services
- Describe how to deploy third party libraries when required

<a id="samples-setup--prerequisites"></a>

## Prerequisites

Following applications are required to run any sample that comes with Synapse.
Please make sure you have them properly installed and configured in your system.

- A Java runtime - JDK or JRE of version 1.6.0\_23 or higher
- [Apache Ant](http://ant.apache.org) version 1.6.5 or higher
- A command line interface such as 'Command Prompt' on Windows and the Bash shell
  on Unix/Linux systems

When installing Java, make sure you setup the 'JAVA\_HOME' environment variable
properly. Also adding the JAVA\_HOME/bin directory to the system path will make
running the samples much easier.

In addition to the applications listed above, some samples require setting up few
other external resources such as JMS brokers and database engines. You can find the
relevant documentation under the '[Setting Up Additional Features](#samples-setup--setting_up_additional_resources)'
section.

It is also advisable to run Synapse in the debug mode when trying out the example
configurations. This will give you important runtime status information that can be
used to better understand the functionality of Synapse. To enable the debug mode, open up the lib/log4j.properties file and specify 'DEBUG' logging mode for the
'org.apache.synapse' package.

log4j.category.org.apache.synapse=DEBUG

<a id="samples-setup--understanding-the-samples"></a>

## Understanding the Samples

A Synapse sample scenario is generally comprised of three elements.

- Sample Synapse configuration (an XML configuration file given as the input
  of Synapse)
- Sample service (an Axis2 based Web Service to which Synapse will send messages)
- Sample client (an Axis2 based service client which is used to send requests to
  Synapse)

<a id="samples-setup--sample-synapse-configurations"></a>

### Sample Synapse Configurations

All the sample Synapse configurations are housed under the repository/conf/sample
directory. These configuration files are named in the following format.

synapse\_sample\_n.xml

Here 'n' is a number which uniquely identifies the sample. This number can be passed
as an argument to the Synapse startup script in order to start Synapse with a particular
sample configuration. For an example to start Synapse with the configuration numbered
100 (ie synapse\_sample\_100.xml) run one of the following commands in the command line
interface.

Unix/Linux: sh synapse.sh -sample 100
Windows: synapse.bat -sample 100

<a id="samples-setup--sample-services"></a>

### Sample Services

All the source of example services can be found in the samples/axis2Server/src directory.
You will find the source code for following services in this directory.

| Service | Description |
| --- | --- |
| SimpleStockQuoteService | This service has four operations; getQuote (in-out), getFullQuote(in-out), getMarketActivity(in-out) and placeOrder (in-only). The getQuote operation will generate a sample stock quote for a given symbol. The getFullQuote operation will generate a history of stock quotes for the symbol for a number of days, and the getMarketActivity operation returns stock quotes for a list of given symbols. The placeOrder operation will accept a one way message for an order. |
| SecureStockQuoteService | This service is a clone of the SimpleStockQuoteService, but has WS-Security enabled and an attached security policy for signing and encryption of messages. |
| ReliableStockQuoteService | This service is a clone of the SimpleStockQuoteService, but has WS-ReliableMessaging enabled. |
| MTOMSwASampleService | This service has three operations uploadFileUsingMTOM(in-out), uploadFileUsingSwA(in-out) and oneWayUploadUsingMTOM(in-only) and demonstrates the use of MTOM and SwA. The uploadFileUsingMTOM and uploadFileUsingSwA operations accept a binary image from the SOAP request as MTOM and SwA, and returns this image back again as the response, while the oneWayUploadUsingMTOM saves the request message to disk. |
| LoadbalanceFailoverService | A simple web service that can be used to test state less as well as session aware load balancing scenarios. |

You can compile and deploy any of these services into the provided sample Axis2
server by switching to the corresponding directory and invoking 'ant'. For an
example to setup the SimpleStockQuoteService, switch to the
samples/axis2Server/src/SimpleStockQuoteService directory and run the 'ant'
command. You will get an output similar to the following.

user@host:/tmp/synapse-1.1/samples/axis2Server/src/SimpleStockQuoteService$ ant
Buildfile: build.xml
...
build-service:
....
[jar] Building jar: /tmp/synapse-1.1/samples/axis2Server/repository/services/SimpleStockQuoteService.aar
BUILD SUCCESSFUL
Total time: 3 seconds

To start the Axis2 server, go to the samples/axis2Server directory and execute
the axis2server.sh or axis2server.bat script. This starts the Axis2 server with
the HTTP transport listener on port 9000 and HTTPS on port 9002 respectively.
For some samples it is required to enable additional transport listeners for the
sample Axis2 server. The resources listed under '[Setting Up Additional Features'](#samples-setup--setting_up_additional_resources)
section provides more information on this.

<a id="samples-setup--sample-client-applications"></a>

### Sample Client Applications

The client applications that come with Synapse are able to send SOAP, REST or
POX messages over transports like HTTP/S and JMS. They also support WS-Addressing, WS-Security and WS-ReliableMessaging. Some sample clients can be used to send
pure binary or plain text messages. They are also capable of sending optimized
binary content using MTOM or SwA. Most sample scenarios involve invoking one
of these clients to send messages to Synapse. Synapse will then mediate those
requests and forward them to the sample services deployed on Axis2.

The sample clients can be executed from the samples/axis2Client directory
using the provided ant script. Simply executing 'ant' displays the available
clients and some of the options used to configure them. The sample clients
available are further described in the next section.

<a id="samples-setup--sample-axis2-clients"></a>

## Sample Axis2 Clients

<a id="samples-setup--stock-quote-client"></a>

### Stock Quote Client

This is a simple SOAP client that can send stock quote requests, receive
generated quotes and display the last sale price for a stock symbol.

ant stockquote [-Dsymbol=IBM|MSFT|SUN|..]
[-Dmode=quote | customquote | fullquote | placeorder | marketactivity]
[-Dsoapver=soap11 | soap12]
[-Daddurl=http://localhost:9000/services/SimpleStockQuoteService]
[-Dtrpurl=http://localhost:8280] [-Dprxurl=http://localhost:8280]
[-Dpolicy=../../repository/conf/sample/resources/policy/policy\_1.xml]

The client is able to operate in the following modes, and send the payloads
listed below as SOAP messages.

| Mode | Payload | Description |
| --- | --- | --- |
| quote | <m:getQuote xmlns:m="http://services.samples"> <m:request> <m:symbol>IBM</m:symbol> </m:request> </m:getQuote> | Sends a quote request for a single stock symbol. The response contains the last sales price for the stock which will be displayed on console. |
| customquote | <m0:checkPriceRequest xmlns:m0="http://www.apache-synapse.org/test"> <m0:Code>symbol</m0:Code> </m0:checkPriceRequest> | Sends a quote request in a custom format. Synapse will transform this custom request to the standard stock quote request format and send it to the Axis2 service. Upon receipt of the response, it will be transformed again to a custom response format and returned to the client, which will then display the last sales price. |
| fullquote | <m:getFullQuote xmlns:m="http://services.samples"> <m:request> <m:symbol>IBM</m:symbol> </m:request> </m:getFullQuote> | Gets quote reports for a stock symbol over a number of days (i.e. last 100 days of the year). |
| placeorder | <m:placeOrder xmlns:m="http://services.samples"> <m:order> <m:price>3.141593E0</m:price> <m:quantity>4</m:quantity> <m:symbol>IBM</m:symbol> </m:order> </m:placeOrder> | Places an order for stocks using a one way request. |
| marketactivity | <m:getMarketActivity xmlns:m="http://services.samples"> <m:request> <m:symbol>IBM</m:symbol> ... <m:symbol>MSFT</m:symbol> </m:request> </m:getMarketActivity> | Gets a market activity report for the day (i.e. quotes for multiple symbols) |

To run the stock quote client in a particular mode, pass the name of the mode
as a system property as follows.

ant stockquote -Dmode=placeorder

Behavior of the sample Axis2 client can be further customized by using the 'addurl',
'trpurl' and 'prxurl' parameters. These parameters enable the following modes of
operation.

<a id="samples-setup--smart-client-mode"></a>

##### Smart Client Mode

The 'addurl' property sets the WS-Addressing EPR, and the 'trpurl' sets a
transport URL for a message. Thus by specifying both of these properties, the client can operate in the 'smart client' mode, where the addressing EPR can
specify the ultimate receiver, while the transport URL set to Synapse will ensure
that any necessary mediation takes place before the message is delivered to the
ultimate receiver.

ant stockquote -Daddurl=<addressingEPR> -Dtrpurl=<synapse>

<a id="samples-setup--gateway-dumb-client-mode"></a>

##### Gateway/Dumb Client Mode

By specifying only a transport URL, the client operates in the 'dumb client'
mode, where it sends the message to Synapse and depends on the rules configured
in Synapse for proper mediation and routing of the message to the ultimate
destination.

ant stockquote -Dtrpurl=<synapse>

<a id="samples-setup--proxy-client-mode"></a>

##### Proxy Client Mode

In this mode, the client uses the 'prxurl' as a HTTP proxy to send the request.
Thus by setting the 'prxurl' to Synapse, the client can ensure that the message
will reach Synapse for mediation. The client can optionally set a WS-Addressing
EPR if required.

ant stockquote -Dprxurl=<synapse> [-Daddurl=<addressingEPR>]

<a id="samples-setup--generic-jms-client"></a>

### Generic JMS Client

The JMS client is able to send plain text, plain binary content or POX content
by directly publishing a JMS message to the specified destination. The JMS
destination name should be specified with the 'jms\_dest' property. The 'jms\_type'
property can specify 'text', 'binary' or 'pox' to specify the type of message
payload.

The plain text payload for a 'text' message can be specified through the 'payload'
property. For binary messages, the 'payload' property will contain the path to
the binary file. For POX messages, the 'payload' property will hold a stock
symbol name to be used within the POX request for stock order placement requests.

ant jmsclient -Djms\_type=text -Djms\_dest=dynamicQueues/JMSTextProxy -Djms\_payload="24.34 100 IBM"
ant jmsclient -Djms\_type=pox -Djms\_dest=dynamicQueues/JMSPoxProxy -Djms\_payload=MSFT
ant jmsclient -Djms\_type=binary -Djms\_dest=dynamicQueues/JMSFileUploadProxy
-Djms\_payload=./../../repository/conf/sample/resources/mtom/asf-logo.gif

The JMS client assumes the existence of a default ActiveMQ (v4.1.0 or above)
installation on the local machine. Refer JMS setup guide for more details.

<a id="samples-setup--mtom-swa-client"></a>

### MTOM/SwA Client

The MTOM / SwA client is able to send a binary image file as a MTOM or SwA
optimized message, and receive the same file again through the response and save
it as a temporary file. The 'opt\_mode' can specify 'mtom' or 'swa' respectively
for the above mentioned optimizations. Optionally the path to a custom file can
be specified through the 'opt\_file' property, and the destination address can be
changed through the 'opt\_url' property if required.

ant optimizeclient -Dopt\_mode=[mtom | swa]

<a id="samples-setup--setting-up-additional-features"></a>

## Setting Up Additional Features

- [JMS Setup Guide](https://synapse.apache.org/userguide/samples/setup/jms.html)
- [FIX Setup Guide](https://synapse.apache.org/userguide/samples/setup/fix.html)
- [TCP/UDP Setup Guide](https://synapse.apache.org/userguide/samples/setup/tcp_udp.html)
- [Database Setup Guide](https://synapse.apache.org/userguide/samples/setup/db.html)
- [Script Setup Guide](https://synapse.apache.org/userguide/samples/setup/script.html)
- [JSON Setup Guide](https://synapse.apache.org/userguide/samples/setup/script.html#json-syn3)
- [E-Mail Setup Guide](https://synapse.apache.org/userguide/samples/setup/mail.html)

---

<a id="samples"></a>

<!-- source_url: https://synapse.apache.org/userguide/samples.html -->

<!-- page_index: 4 -->

<a id="samples--apache-synapse-samples-catalog"></a>

## Apache Synapse Samples Catalog

Apache Synapse comes preloaded with a horde of sample configurations that
demonstrate various features of the service bus. This catalog lists out all
these sample configurations and provides detailed information on how to run
them. These samples require an Apache ANT installation for you to be able to
try them out. If you are new to Synapse and have no experience running Synapse, the Quick Start Guide may be a better starting point. If you are comfortable
with running Synapse samples, please go ahead and pick the samples you are
interested in.

<a id="samples--message-mediation"></a>

### Message Mediation

- [Sample 0: Introduction to Synapse](https://synapse.apache.org/userguide/samples/sample0.html)
- [Sample 1: Simple content based routing (CBR) of messages](https://synapse.apache.org/userguide/samples/sample1.html)
- [Sample 2: CBR with the Switch-case mediator, using message properties](https://synapse.apache.org/userguide/samples/sample2.html)
- [Sample 3: Local Registry entry definitions, reusable endpoints and sequences](https://synapse.apache.org/userguide/samples/sample3.html)
- [Sample 4: Introduction to error handling](https://synapse.apache.org/userguide/samples/sample4.html)
- [Sample 5: Creating SOAP fault messages and changing the direction of a message](https://synapse.apache.org/userguide/samples/sample5.html)
- [Sample 6: Manipulating SOAP headers, and filtering incoming and outgoing messages](https://synapse.apache.org/userguide/samples/sample6.html)
- [Sample 7: Introduction to local registry entries and using schema validation](https://synapse.apache.org/userguide/samples/sample7.html)
- [Sample 8: Introduction to static and dynamic registry resources, and using XSLT transformations](https://synapse.apache.org/userguide/samples/sample8.html)
- [Sample 9: Introduction to dynamic sequences with registry](https://synapse.apache.org/userguide/samples/sample9.html)
- [Sample 10: Introduction to dynamic endpoints with registry](https://synapse.apache.org/userguide/samples/sample10.html)
- [Sample 11: A full registry based configuration, and sharing a configuration between multiple instances](https://synapse.apache.org/userguide/samples/sample11.html)
- [Sample 12: One-way messaging / fire-and-forget through Synapse](https://synapse.apache.org/userguide/samples/sample12.html)
- [Sample 14: Sequences and Endpoints as local registry items](https://synapse.apache.org/userguide/samples/sample14.html)
- [Sample 15: Message Copying and Content Enriching with Enrich Mediator](https://synapse.apache.org/userguide/samples/sample15.html)
- [Sample 16: Introduction to dynamic and static keys](https://synapse.apache.org/userguide/samples/sample16.html)
- [Sample 17: Introduction to the payloadFactory mediator](https://synapse.apache.org/userguide/samples/sample17.html)

<a id="samples--endpoints"></a>

### Endpoints

- [Sample 50: POX to SOAP conversion](https://synapse.apache.org/userguide/samples/sample50.html)
- [Sample 51: MTOM and SwA optimizations and request/response correlation](https://synapse.apache.org/userguide/samples/sample51.html)
- [Sample 52: Session less load balancing between 3 endpoints](https://synapse.apache.org/userguide/samples/sample52.html)
- [Sample 53: Fail-over routing among 3 endpoints](https://synapse.apache.org/userguide/samples/sample53.html)
- [Sample 54: Session affinity load balancing between 3 endpoints](https://synapse.apache.org/userguide/samples/sample54.html)
- [Sample 55: Session affinity load balancing between fail-over endpoints](https://synapse.apache.org/userguide/samples/sample55.html)
- [Sample 56: WSDL endpoint](https://synapse.apache.org/userguide/samples/sample56.html)
- [Sample 57: Dynamic load balancing between 3 nodes](https://synapse.apache.org/userguide/samples/sample57.html)
- [Sample 58: Static load balancing between 3 nodes](https://synapse.apache.org/userguide/samples/sample58.html)
- [Sample 59: Weighted Round-Robin loadbalancing between 3 endpoints](https://synapse.apache.org/userguide/samples/sample59.html)
- [Sample 61: Routing message to 3 static recipients](https://synapse.apache.org/userguide/samples/sample61.html)
- [Sample 62: Routing message to dynamic recipients](https://synapse.apache.org/userguide/samples/sample62.html)

<a id="samples--qos-addition-removal-with-message-mediation"></a>

### QoS Addition/Removal with Message Mediation

- [Sample 100: Using WS-Security for outgoing messages](https://synapse.apache.org/userguide/samples/sample100.html)

<a id="samples--proxy-services"></a>

### Proxy Services

- [Sample 150: Introduction to proxy services](https://synapse.apache.org/userguide/samples/sample150.html)
- [Sample 151: Custom sequences and endpoints with proxy services](https://synapse.apache.org/userguide/samples/sample151.html)
- [Sample 152: Switching transports and message format from SOAP to REST/POX](https://synapse.apache.org/userguide/samples/sample152.html)
- [Sample 153: Routing the messages without processing the security headers](https://synapse.apache.org/userguide/samples/sample153.html)
- [Sample 154: Load Balancing with proxy services](https://synapse.apache.org/userguide/samples/sample154.html)
- [Sample 155: Dual channel invocation on client side and server side](https://synapse.apache.org/userguide/samples/sample155.html)
- [Sample 156: Service integration with specifying the receiving sequence](https://synapse.apache.org/userguide/samples/sample156.html)
- [Sample 157: Conditional router mediator for implementing complex routing scenarios](https://synapse.apache.org/userguide/samples/sample157.html)
- [Sample 158: Exposing a SOAP service over JSON](https://synapse.apache.org/userguide/samples/sample158.html)

<a id="samples--qos-addition-removal-with-proxy-services"></a>

### QoS Addition/Removal with Proxy Services

- [Sample 200: Engaging WS-Security on proxy services](https://synapse.apache.org/userguide/samples/sample200.html)

<a id="samples--transports"></a>

### Transports

- [Sample 250: Introduction to transport switching - JMS to HTTP/S](https://synapse.apache.org/userguide/samples/sample250.html)
- [Sample 251: Switching from http/s to JMS](https://synapse.apache.org/userguide/samples/sample251.html)
- [Sample 252: Pure text, binary and POX message support with JMS](https://synapse.apache.org/userguide/samples/sample252.html)
- [Sample 253: One way bridging from JMS to http and replying with a 202 Accepted response](https://synapse.apache.org/userguide/samples/sample253.html)
- [Sample 254: Using file system as the transport medium (reading/writing files)](https://synapse.apache.org/userguide/samples/sample254.html)
- [Sample 255: Switching from file transport (ftp) to the mail transport](https://synapse.apache.org/userguide/samples/sample255.html)
- [Sample 256: Proxy services with the mail transport](https://synapse.apache.org/userguide/samples/sample256.html)
- [Sample 257: Proxy services with the FIX transport](https://synapse.apache.org/userguide/samples/sample257.html)
- [Sample 258: Switching from HTTP to FIX](https://synapse.apache.org/userguide/samples/sample258.html)
- [Sample 259: Switching from FIX to HTTP](https://synapse.apache.org/userguide/samples/sample259.html)
- [Sample 260: Switching from FIX to AMQP](https://synapse.apache.org/userguide/samples/sample260.html)
- [Sample 261: Switch between different FIX versions](https://synapse.apache.org/userguide/samples/sample261.html)
- [Sample 262: Content Based Routing of FIX messages](https://synapse.apache.org/userguide/samples/sample262.html)
- [Sample 263: Transport switching - JMS to http/s using JBoss Messaging (JBM)](https://synapse.apache.org/userguide/samples/sample263.html)
- [Sample 264: Request-response invocations with the JMS transport](https://synapse.apache.org/userguide/samples/sample264.html)
- [Sample 265: Switching from TCP to HTTP/S](https://synapse.apache.org/userguide/samples/sample265.html)
- [Sample 266: Switching from UDP to HTTP/S](https://synapse.apache.org/userguide/samples/sample266.html)
- [Sample 269: AMQP transport-consumer proxy](https://synapse.apache.org/userguide/samples/sample269.html)

<a id="samples--scheduled-tasks"></a>

### Scheduled Tasks

- [Sample 300: Introduction to tasks with simple trigger](https://synapse.apache.org/userguide/samples/sample300.html)
- [Sample 301: Message Injector Task to invoke a named sequence](https://synapse.apache.org/userguide/samples/sample301.html)
- [Sample 302: Message Injector Task to invoke a Proxy service](https://synapse.apache.org/userguide/samples/sample302.html)

<a id="samples--advanced-mediators"></a>

### Advanced Mediators

<a id="samples--script-mediator-writing-mediation-logic-in-scripting-languages"></a>

#### Script Mediator (Writing Mediation Logic in Scripting Languages)

- [Sample 350: Introduction to the script mediator using js scripts](https://synapse.apache.org/userguide/samples/sample350.html)
- [Sample 351: Inline scripts with the script mediator](https://synapse.apache.org/userguide/samples/sample351.html)
- [Sample 352: Accessing Synapse MessageContext API through scripts](https://synapse.apache.org/userguide/samples/sample352.html)
- [Sample 353: Using Ruby scripts for mediation](https://synapse.apache.org/userguide/samples/sample353.html)
- [Sample 354: Using In-lined Ruby scripts for mediation](https://synapse.apache.org/userguide/samples/sample354.html)
- [Sample 355: Using Python scripts for mediation](https://synapse.apache.org/userguide/samples/sample355.html)

<a id="samples--database-mediators-interacting-with-databases"></a>

#### Database Mediators (Interacting with Databases)

- [Sample 360: Introduction to dblookup mediator](https://synapse.apache.org/userguide/samples/sample360.html)
- [Sample 361: Introduction to dbreport mediator](https://synapse.apache.org/userguide/samples/sample361.html)
- [Sample 362: Perform database lookups and updates in the same mediation sequence](https://synapse.apache.org/userguide/samples/sample362.html)
- [Sample 363: Reusable database connection pools](https://synapse.apache.org/userguide/samples/sample363.html)
- [Sample 364: Executing database Stored Procedures](https://synapse.apache.org/userguide/samples/sample364.html)

<a id="samples--throttle-mediator"></a>

#### Throttle Mediator

- [Sample 370: Introduction to throttle mediator and concurrency throttling](https://synapse.apache.org/userguide/samples/sample370.html)
- [Sample 371: Restricting requests based on policies](https://synapse.apache.org/userguide/samples/sample371.html)
- [Sample 372: Use of both concurrency throttling and request rate based throttling](https://synapse.apache.org/userguide/samples/sample372.html)

<a id="samples--class-mediator-writing-mediation-logic-in-java"></a>

#### Class Mediator (Writing Mediation Logic in Java)

- [Sample 380: Writing custom mediation logic in Java](https://synapse.apache.org/userguide/samples/sample380.html)
- [Sample 381: Class mediator for CBR of binary messages](https://synapse.apache.org/userguide/samples/sample381.html)

<a id="samples--xquery-mediator"></a>

#### XQuery Mediator

- [Sample 390: Introduction to the XQuery mediator](https://synapse.apache.org/userguide/samples/sample390.html)
- [Sample 391: Using external XML documents in the XQuery mediator](https://synapse.apache.org/userguide/samples/sample391.html)

<a id="samples--iterate-mediator-and-aggregate-mediator"></a>

#### Iterate Mediator and Aggregate Mediator

- [Sample 400: Message splitting and aggregation](https://synapse.apache.org/userguide/samples/sample400.html)

<a id="samples--transaction-mediator"></a>

#### Transaction Mediator

- [Sample 410: Distributed transactions management with the transaction mediator](https://synapse.apache.org/userguide/samples/sample410.html)

<a id="samples--cache-mediator"></a>

#### Cache Mediator

- [Sample 420: Simple response caching scenario](https://synapse.apache.org/userguide/samples/sample420.html)

<a id="samples--callout-mediator"></a>

#### Callout Mediator

- [Sample 430: Callout mediator for synchronous web service invocations](https://synapse.apache.org/userguide/samples/sample430.html)
- [Sample 431: Callout Mediator with WS-Security for Outgoing Messages](https://synapse.apache.org/userguide/samples/sample431.html)
- [Sample 432: Callout Mediator - Invoke a secured service which has different policies for inbound and outbound flows](https://synapse.apache.org/userguide/samples/sample432.html)
- [Sample 433: Callout Mediator - Invoke a service using a defined Endpoint](https://synapse.apache.org/userguide/samples/sample433.html)
- [Sample 434: Callout Mediator - Invoke a service using an inline Endpoint](https://synapse.apache.org/userguide/samples/sample434.html)

<a id="samples--respond-mediator"></a>

#### Respond Mediator

- [Sample 440: Respond Mediator - Echo Service with a Proxy service](https://synapse.apache.org/userguide/samples/sample440.html)
- [Sample 441: Respond Mediator - Mock Service with a Proxy service](https://synapse.apache.org/userguide/samples/sample441.html)

<a id="samples--url-rewrite-mediator"></a>

#### URL Rewrite Mediator

- [Sample 450: Introduction to the URL Rewrite mediator](https://synapse.apache.org/userguide/samples/sample450.html)
- [Sample 451: Conditional URL rewriting](https://synapse.apache.org/userguide/samples/sample451.html)
- [Sample 452: Conditional URL rewriting with multiple rules](https://synapse.apache.org/userguide/samples/sample452.html)

<a id="samples--spring-mediator"></a>

#### Spring Mediator

- [Sample 460: Introduction to the Spring mediator](https://synapse.apache.org/userguide/samples/sample460.html)

<a id="samples--ejb-mediator"></a>

#### EJB Mediator

- [Sample 470: Introduction to the EJB mediator I: Invoking Stateless Session Beans](https://synapse.apache.org/userguide/samples/sample470.html)
- [Sample 471: Introduction to the EJB mediator II: Invoking Stateful Session Beans](https://synapse.apache.org/userguide/samples/sample471.html)

<a id="samples--eventing"></a>

### Eventing

- [Sample 500: Introduction to Eventing](https://synapse.apache.org/userguide/samples/sample500.html)
- [Sample 501: Event source with static subscriptions](https://synapse.apache.org/userguide/samples/sample501.html)
- [Sample 502: Transforming events before publish](https://synapse.apache.org/userguide/samples/sample502.html)

<a id="samples--synapse-configuration-model"></a>

### Synapse Configuration Model

- [Sample 600: File hierarchy based configuration builder](https://synapse.apache.org/userguide/samples/sample600.html)
- [Sample 601: Using Synapse Observers](https://synapse.apache.org/userguide/samples/sample601.html)

<a id="samples--priority-based-mediation"></a>

### Priority Based Mediation

- [Sample 650: Introduction to priority based mediation](https://synapse.apache.org/userguide/samples/sample650.html)
- [Sample 651: Priority based dispatching at transport level](https://synapse.apache.org/userguide/samples/sample651.html)

<a id="samples--message-stores-and-message-processors"></a>

### Message Stores and Message Processors

- [Sample 700: Introduction to Synapse Message Stores](https://synapse.apache.org/userguide/samples/sample700.html)
- [Sample 701: Introduction to Message Sampling Processor](https://synapse.apache.org/userguide/samples/sample701.html)
- [Sample 702: Introduction to Message Forwarding Processor](https://synapse.apache.org/userguide/samples/sample702.html)
- [Sample 703: Introduction to Message Resequencing Processor](https://synapse.apache.org/userguide/samples/sample703.html)
- [Sample 704: Invoke Secured Services with Scheduled Message Forwarding Processor](https://synapse.apache.org/userguide/samples/sample704.html)
- [Sample 705: Introduction to Message Forwarding Processor With Advance Parameters](https://synapse.apache.org/userguide/samples/sample705.html)

<a id="samples--templates"></a>

### Templates

- [Sample 750: Introduction to Synapse Templates](https://synapse.apache.org/userguide/samples/sample750.html)

<a id="samples--rest-api"></a>

### REST API

- [Sample 800: Introduction to REST APIs](https://synapse.apache.org/userguide/samples/sample800.html)

<a id="samples--synapse-eip-library"></a>

### Synapse EIP Library

- [Sample 850: Introduction to Synapse Callout Block function template](https://synapse.apache.org/userguide/samples/sample850.html)
- [Sample 851: Introduction to Synapse Splitter and Aggregator eip function templates](https://synapse.apache.org/userguide/samples/sample851.html)
- [Sample 852: Introduction to Synapse Splitter-Agrregator combined function template](https://synapse.apache.org/userguide/samples/sample852.html)
- [Sample 853: Introduction to Synapse Scatter-Gather eip function template](https://synapse.apache.org/userguide/samples/sample853.html)
- [Sample 854: Introduction to Synapse Wire Tap eip function template](https://synapse.apache.org/userguide/samples/sample854.html)
- [Sample 855: Introduction to Synapse Content Based Router eip function template](https://synapse.apache.org/userguide/samples/sample855.html)
- [Sample 856: Introduction to Synapse Dynamic Router eip function template](https://synapse.apache.org/userguide/samples/sample856.html)
- [Sample 857: Introduction to Synapse Recipient List eip function template](https://synapse.apache.org/userguide/samples/sample857.html)

---

<a id="config"></a>

<!-- source_url: https://synapse.apache.org/userguide/config.html -->

<!-- page_index: 5 -->

<a id="config--introduction"></a>

## Introduction

Apache Synapse loads its configuration from a set of XML files. This enables the
user to easily hand edit the configuration, maintain backups and even include the
entire configuration in a version control system for easier management and control.
For an example one may check-in all Synapse configuration files into a version
control system such as Subversion and easily move the configuration files from
development, through QA, staging and into production.

All the configuration files related to Synapse are housed in the repository/conf/synapse-config
directory of the Synapse installation. Synapse is also capable of loading certain
configuration elements (eg: sequences, endpoints) from an external SOA registry.
When using a registry to store fragments of the configuration, some configuration
elements such as endpoints can be updated dynamically while Synapse is executing.

This article describes the hierarchy of XML files from which Synapse reads its
configuration. It describes the high level structure of the file set and the XML
syntax used to configure various elements in Synapse.

<a id="config--contents"></a>

## Contents

- [Synapse Configuration](#config--synapseconfig)
  - [Service Mediation (Proxy Services)](#config--servicemediation)
  - [Message Mediation](#config--messagemediation)
  - [Task Scheduling](#config--taskscheduling)
  - [Eventing](#config--eventing)
- [Functional Components Overview](#config--overview)
  - [Mediators and Sequences](#config--mediatorsandsequences)
  - [Endpoints](#config--endpoints)
  - [Proxy Services](#config--proxyservices)
  - [Scheduled Tasks](#config--scheduledtasks)
  - [Templates](#config--templates)
  - [Remote Registry and Local Registry](#config--registry)
  - [APIs](#config--api)
  - [Priority Executors](#config--priorityexecutors)
  - [Message Stores and Processors](#config--stores)
- [Synapse Configuration Files](#config--configfiles)
- [Configuration Syntax](#config--syntax)
- [Registry Configuration](#config--registryconfig)
- [Local Entry (Local Registry) Configuration](#config--localentryconfig)
- [Sequence Configuration](#config--sequenceconfig)
- [Endpoint Configuration](#config--endpointconfig)
  - [Address Endpoint](#config--addressendpointconfig)
  - [Default Endpoint](#config--defaultendpointconfig)
  - [WSDL Endpoint](#config--wsdlendpointconfig)
  - [Load Balance Endpoint](#config--lbendpointconfig)
  - [Dynamic Load Balance Endpoint](#config--dlbendpointconfig)
  - [Fail-Over Endpoint](#config--foendpointconfig)
  - [Recipient List Endpoint"](#config--recipientlistendpointconfig)
- [Proxy Service Configuration](#config--proxyserviceconfig)
- [Scheduled Task Configuration](#config--taskconfig)
- [Template Configuration](#config--templateconfig)
- [Event Source Configuration](#config--eventsourceconfig)
- [API Configuration](#config--apiconfig)
- [Priority Executor Configuration](#config--executorconfig)
- [Message Stores and Processors Configuration](#config--storesconfig)

<a id="config--the-synapse-configuration"></a>

## The Synapse Configuration

A typical Synapse configuration is comprised of sequences, endpoints, proxy services
and local entries. In certain advanced scenarios, Synapse configuration may also
contain scheduled tasks, event sources, messages stores and priority executors.
Synapse configuration may also include a registry adapter through which the mediation
engine can import various resources to the mediation engine at runtime. Following
diagram illustrates different functional components of Synapse and how they interact
with each other.

![](assets/images/synapse-flow_85d8f06fc1caf91f.png)

All the functional components of the Synapse configuration are configured through
XML files. The Synapse configuration language governs the XML syntax used to define
and configure different types of components. This configuration language is now
available as a [XML schema](http://synapse.apache.org/ns/2010/04/configuration/synapse_config.xsd).

Typically the Synapse ESB is used to mediate the message flow between a client
and a back-end service implementation. Therefore Synapse can accept a message on
behalf of the actual service and perform a variety of mediation tasks on it such
as authentication, validation, transformation, logging and routing. Synapse can also
detect timeouts and other communication errors when connecting to back-end services.
In addition to that users can configure Synapse to perform load balancing, access
throttling and response caching. In case of a fault scenario, such as an authentication
failure or a schema validation failure, the Synapse ESB can be configured to return
a custom message or a SOAP fault to the requesting client without forwarding the
message to the back-end service. All these scenarios and use cases can be put into
action by selecting the right set of functional components of Synapse and combining
them appropriately through the Synapse configuration.

Depending on how functional components are used in the Synapse configuration, Synapse
can execute in one or more of the following operational modes.

<a id="config--service-mediation-proxy-services"></a>

### Service Mediation (Proxy Services)

In service mediation, the Synapse ESB exposes a service endpoint on the ESB, which
accepts messages from clients. Typically these services acts as proxies for existing
(external) services, and the role of Synapse would be to 'mediate' these messages
before they are delivered to the actual service. In this mode, Synapse could expose
a service already available in one transport, over a different transport; or expose
a service that uses one schema or WSDL as a service that uses a different schema or
WSDL. A Proxy service could define the transports over which the service is exposed, and point to the mediation sequences that should be used to process request and
response messages. A proxy service maybe a SOAP or a REST/POX service over HTTP/S or
SOAP, POX, plain text or binary/legacy service for other transports such as JMS
and VFS file systems.

<a id="config--message-mediation"></a>

### Message Mediation

In message mediation, Synapse acts as a transparent proxy for clients. This way, Synapse could be configured to filter all the messages on a network for logging, access control etc, and could 'mediate' messages without the explicit knowledge
of the original client. If Synapse receives a message that is not accepted by any
proxy service, that message is handled through message mediation. Message mediation
always processes messages according to the mediation sequence defined with
the name 'main'.

<a id="config--task-scheduling"></a>

### Task Scheduling

In task scheduling, Synapse can execute a predefined task (job) based on a user
specified schedule. This way a task can be configured to run exactly once or
multiple times with fixed intervals. The schedule can be defined by specifying
the number of times the task should be executed and the interval between
executions. Alternatively one may use the Unix Cron syntax to define task
schedules. This mode of operation can be used to periodically invoke a given
service, poll databases and execute other periodic maintenance activities.

<a id="config--eventing"></a>

### Eventing

In eventing mode, Synapse can be used as an event source and users or systems can
subscribe to receive events from Synapse. Synapse can also act as an event broker
which receives events from other systems and delivers them to the appropriate
subscribers with or without mediation. The set of subscribers will be selected
by applying a predefined filter criteria. This mode enables Synapse to integrate
applications and systems based on the Event Driven Architecture (EDA).

<a id="config--functional-components-overview"></a>

## Functional Components Overview

As described in the previous section, Synapse engine is comprised of a range of
functional components. Synapse configuration language is used to define, configure
and combine these components so various messaging scenarios and integration
patterns can be realized. Before diving into the specifics of the configuration
language, it is useful to have a thorough understanding of all the functional
components available, their capabilities and features. A good knowledge on Synapse
functional components will help you determine which components should be used to
implement any given scenario or use case. In turns it will allow you to develop
powerful and efficient Synapse configurations thus putting the ESB to maximum use.

As of now Synapse mediation engine consists of following functional elements:

- Mediators and sequences
- Endpoints
- Proxy services
- Scheduled tasks
- Event sources
- Sequence templates
- Endpoint templates
- Registry adapter
- APIs
- Priority executors
- Message stores and processors

<a id="config--mediators-and-sequences"></a>

### Mediators and Sequences

The Synapse ESB defines a 'mediator' as a component which performs a predefined
action on a message during a message flow. It is the most fundamental message
processing unit in Synapse. A mediator can be thought of as a filter that resides
in a message flow, which processes all the messages passing through it.

A mediator gets full access to the messages at the point where it is defined.
Thus they can inspect, validate and modify messages. Further, mediators can take
external action such as looking up a database or invoking a remote service, depending on some attributes or values in the current message. Synapse ships
with a variety of built-in mediators which are capable of handling an array of
heterogeneous tasks. There are built-in mediators that can log the requests, perform content transformations, filter out traffic and a plethora of other
messaging and integration activities.

Synapse also provides an API using which custom mediators can be implemented
easily in Java. The 'Class' and 'POJO (command)' mediators allow one to plugin a
Java class into Synapse with minimal effort. In addition, the 'Script' mediator
allows one to provide an Apache BSF script (eg: JavaScript, Ruby, Groovy etc)
for mediation.

A mediation sequence, commonly called a 'sequence' is a list of mediators. A
sequence may be named for re-use, or defined in-line or anonymously within a
configuration. Sequences may be defined within the Synapse configuration or in
the Registry. From an ESB point of view, a sequence equates to a message flow.
It can be thought of as a pipe consisting of many filters, where individual
mediators play the role of the filters.

A Synapse configuration contains two special sequences named 'main' and 'fault'.
These too may be defined in the Synapse configuration, or externally in the
Registry. If either is not found, a suitable default configuration is generated at
runtime by the ESB. The default 'main' sequence will simply send a message without
any mediation, while the default 'fault' sequence would log the message and error
details and stop further processing. The 'fault' sequence executes whenever Synapse
itself encounters an error while processing a message, or when a fault handler has
not been defined to handle exceptions. A sequence can assign another named sequence
as its 'fault' handler sequence, and handover control to the fault handler if an
error is encountered during the execution of the initial sequence.

<a id="config--endpoints"></a>

### Endpoints

An Endpoint definition within Synapse defines an external service endpoint and
any attributes or semantics that should be followed when communicating with that
endpoint. An endpoint definition can be named for re-use, or defined in-line or
anonymously within a configuration. Typically an endpoint would be based on a
service address or a WSDL. Additionally the Synapse ESB supports Failover and
Load-balance endpoints - which are defined over a group of endpoints. Endpoints
may be defined within the local Synapse configuration or within the Registry.

From a more practical stand point, an endpoint can be used to represent any
entity to which Synapse can make a connection. An endpoint may represent a
URL, a mail box, a JMS queue or a TCP socket. The 'send' mediator of Synapse
which is used to forward messages can take an endpoint as an argument. In that
case the 'send' mediator would forward the message to the specified endpoint.

<a id="config--proxy-services"></a>

### Proxy Services

A proxy service is a virtual service exposed on Synapse. For the external
clients, a proxy service looks like a full fledged web service which has a
set of endpoint references (EPRs), a WSDL and a set of developer specified
policies. But in reality, a proxy service sits in front of a real web service
implementation, acting as a proxy, mediating messages back and forth. The
actual business logic of the service resides in the real back-end web service.
Proxy service simply hides the real service from the consumer and provides
an interface through which the actual service can be reached but with some
added mediation/routing logic.

Proxy services have many use cases. A proxy can be used to expose an existing
service over a different protocol or a schema. The mediation logic in the proxy
can take care of performing the necessary content transformations and protocol
switching. A proxy service can act as a load balancer or a lightweight process
manager thereby hiding multiple back-end services from the client. Proxy services
also provide a convenient way of extending existing web services without changing
the back-end service implementations. For an example a proxy service can add logging
and validation capabilities to an existing service without the developer having
to implement such functionality at service level. Another very common usage of
proxy services is to secure an existing service or a legacy system.

A proxy service is a composite functional component. It is made of several
sequences and endpoints. Typically a proxy service consists of an 'in sequence', an 'out sequence' and an endpoint. The 'in sequence' handles all the incoming
requests sent by the client. Mediated messages are then forwarded to the target
endpoint which generally points to the real back-end service. Responses coming
back from the back-end service are processed by the 'out sequence'. In addition
to these a 'fault sequence' can also be associated with a proxy service which
is invoked in case of an error.

In addition to the above basic configuration elements, a proxy service can
also define a WSDL file to be published, a set of policies and various other
parameters.

<a id="config--scheduled-tasks"></a>

### Scheduled Tasks

A scheduled task is a job deployed in the Synapse runtime for periodic execution.
Users can program the jobs using the task API (Java) provided by Synapse. Once
deployed, tasks can be configured to run periodically. The execution schedule
can be configured by specifying the delay between successive executions or using
the Unix Cron syntax.

<a id="config--templates"></a>

### Templates

A Template is an abstract concept in synapse. One way to view a template, is as
a prototype or a function. Templates try to minimize redundancy in synapse
artifacts (ie sequences and endpoints) by creating prototypes that users can
re-use and utilize as and when needed. This is very much analogous to classes
and instances of classes whereas, a template is a class that can be used to
wield instance objects such as sequences and endpoints.

Templates is an ideal way to improve re-usability and readability of
ESB configurations (XML). Addition to that users can utilize predefined templates
that reflect commonly used EIP patterns for rapid development of ESB
message/mediation flows.There are two flavours of templates which are Endpoint
and Sequence Templates.

An endpoint template is an abstract definition of a synapse endpoint. Users have
to invoke this kind of a template using a special template endpoint. Endpoint
templates can specify various commons parameters of an endpoint that can be reused
across many endpoint definitions (eg: address uri, timeouts, error codes etc).

A sequence template defines a functional form of an ESB sequence. Sequence
templates have the ability to parametrize a sequence flow. Generally
parametrization is in the form of static values as well as xpath expressions.
Users can invoke a template of this kind with a mediator named 'call-template'
by passing in the required parameter values.

<a id="config--remote-registry-and-local-registry-local-entries"></a>

### Remote Registry and Local Registry (Local Entries)

Synapse configuration can refer to an external registry/repository for resources
such as WSDLs, schemas, scripts, XSLT and XQuery transformations etc. One or
more remote registries may be hidden or merged behind a local registry interface
defined in the Synapse configuration. Resources from an external registry are
looked up using 'keys' - which are known to the external registry. The Synapse
ESB ships with a simple URL based registry implementation that uses the file system
for storage of resources, and URLs or fragments as 'keys'.

A registry may define a duration for which a resource served may be cached by the
Synapse runtime. If such a duration is specified, the Synapse ESB is capable of
refreshing the resource after cache expiry to support dynamic re-loading of resources
at runtime. Optionally, a configuration could define certain 'keys' to map to locally
defined entities. These entities may refer to a source URL or file, or may be defined
as in-line XML or text within the configuration itself. If a registry contains a
resource whose 'key' matches the key of a locally defined entry, the local entry
shadows the resource available in the registry. Thus it is possible to override
registry resources locally from within the configuration. To integrate Synapse with
a custom/new registry, one needs to implement the org.apache.synapse.registry.Registry
interface to suit the actual registry being used.

<a id="config--apis"></a>

### APIs

An API is similar to a web application deployed in Synapse. It provides a
convenient approach for filtering and processing HTTP traffic (specially RESTful
invocations) through the service bus. Each API is anchored at a user defined
URL context (eg: /ws) and can handle all the HTTP requests that
fall within that context. Each API is also comprised of one or more resources.
Resources contain the mediation logic for processing requests and responses.
Resources can also be associated with a set of HTTP methods and header values.
For an example one may define an API with two resources, where one resources is
used to handle GET requests and the other is used to handle POST requests.
Similarly an API can be defined with separate resources for handling XML and JSON
content (by looking at the Content-type HTTP header).

Resources bare a strong resemblance to proxy services. Similar to proxy services, a resource can also define an 'in sequence', an 'out sequence' and a 'fault
sequence'. Just like in the case of proxy services, the 'in sequence' is used
to process incoming requests and the 'out sequence' is used to mediate responses.

APIs provide a powerful framework using which comprehensive REST APIs can be
constructed on existing systems. For an example a set of SOAP services can be
hidden behind an API defined in Synapse. Clients can access the API in Synapse
by making pure RESTful invocations over HTTP. Synapse takes care of transforming
the requests and routing them to appropriate back-end services which may or may
not be based on REST.

<a id="config--priority-executors"></a>

### Priority Executors

Priority executors can be used to execute sequences with a given priority.
Priority executors are used in high load scenarios where user wants to execute
different sequences at different priority levels. This allows user to control
the resources allocated to executing sequences and prevent high priority messages
from getting delayed and dropped. A priority has a specific meaning compared to
other priorities specified. For example if we have two priorities with value 10
and 1, messages with priority 10 will get 10 times more resources than messages
with priority 1.

<a id="config--message-stores-and-processors"></a>

### Message Stores and Processors

Message store acts as a unit of storage for messages/data exchanged during synapse
runtime. By default synapse ships with a in-memory message store and the storage
can be plugged in depending on the requirement. There is a specific mediator called
store mediator which is able to direct message traffic to a particular message
store at runtime.

On the other hand a Message processor has the ability to connect to a message
store and perform message mediation or required data manipulations. Essentially
a particular message processor will be coupled with a message store and as a
result respective message processor will be inherited with the traits of that
particular message storage.

For example in the eye of a message processor, data/messages coming from in-memory
message store will be seen as more volatile compared to a persistent message store.
Nevertheless it will find it can perform operations much faster on the former.
This is in fact a very powerful concept and hence depending on the processor and
store combination users can define limitless number of EI patterns in synapse
that could meet different runtime requirements and SLA's. Synapse by default
support two processors which are scheduled message processor and sampling
processor.

<a id="config--synapse-configuration-files"></a>

## Synapse Configuration Files

All the XML files pertaining to the Synapse configuration are available in the
repository/conf/synapse-config directory of the Synapse installation. This file
hierarchy consists of two files named synapse.xml and registry.xml. In addition to
that, following sub-directories can be found in the synapse-config directory.

- api
- endpoints
- events
- local-entries
- message-processors
- message-stores
- priority-executors
- proxy-services
- sequences
- tasks
- templates

Each of these sub-directories can contain zero or more configuration items. For
an example the 'endpoints' directory may contain zero or more endpoint definitions
and the 'sequences' directory may contain zero or more sequence definitions. The
registry adapter is defined in the top level registry.xml file. The synapse.xml file
is there mainly for backward compatibility reasons. It can be used to define any
type of configuration items. One may define few endpoints in the 'endpoints' directory
and a few endpoints in the synapse.xml file. However it is recommended to stick to
a single, consistent way of defining configuration elements. So you should either
define everything in synapse.xml file, or not use it at all.

The following tree diagram shows the high-level view of the resulting file
hierarchy.

synapse-config
|-- api
|-- endpoints
| `-- foo.xml
|-- events
| `-- event1.xml
|-- local-entries
| `-- bar.xml
|-- message-processors
|-- message-stores
|-- priority-executors
|-- proxy-services
| |-- proxy1.xml
| |-- proxy2.xml
| `-- proxy3.xml
|-- registry.xml
|-- sequences
| |-- custom-logger.xml
| |-- fault.xml
| `-- main.xml
|-- synapse.xml
|-- tasks
| `-- task1.xml
`-- templates

<a id="config--configuration-syntax"></a>

## Configuration Syntax

Synapse ESB is configured using an XML based configuration language. This is a
Domain Specific Language (DSL) created and maintained by the Synapse community.
The language is designed to be simple, intuitive and easy to learn. All XML
elements (tags) in this language must be namespace qualified with the namespace
URL **http://ws.apache.org/ns/synapse**.

As stated earlier, the synapse.xml file can be used to define all kinds of artifacts.
All these different configuration items should be wrapped in a top level 'definitions'
element. A configuration defined in the synapse.xml file looks like this at the
high level.

<definitions>
<[registry](#config--registryconfig) provider="string">...</registry>?
<[localEntry](#config--localentryconfig) key="string">...</localEntry>?
<[sequence](#config--sequenceconfig) name="string">...</sequence>?
<[endpoint](#config--endpointconfig) name="string">...</endpoint>?
<[proxy](#config--proxyserviceconfig) name="string" ...>...</proxy>?
<[task](#config--taskconfig) name="string" ...>...</task>?
<[eventSource](#config--eventsourceconfig) name="string" ...>...</eventSource>?
<[executor](#config--executorconfig) name="string" ...>...</executor>?
<[api](#config--apiconfig) name="string" ...>...</api>?
<[template](#config--templateconfig) name="string" ...>...</template>?
<[messageStore](#config--storesconfig) name="string" ...>...</messageStore>?
</definitions>

The registry adapter definition is defined under the <registry> element. Similarly
<endpoint>, <sequence>, <proxy>, <localEntry>, <eventSource
and <executor> elements are used to define other functional components.

As pointed out earlier, the synapse.xml file is there in the synapse-config directory
for backwards compatibility reasons. Any artifact defined in this file can be
defined separately in its own XML file. The registry can be defined in the registry.xml
and other artifacts can be defined in the corresponding sub-directories of the synapse-config
directory. However the XML syntax used to configure these artifacts are always the same.
Next few sections of this document explains the XML syntax for defining various
types of components in the Synapse configuration.

<a id="config--registry-configuration"></a>

## Registry Configuration

The <registry> element is used to define the registry adapter used by the
Synapse runtime. The registry provider specifies an implementation class for the
registry being used, and optionally a number of configuration parameters as may be
required by the particular registry implementation. An outline configuration is given
below.

<registry provider="string"/>
<parameter name="string">text | xml</parameter>\*
</registry>

Registry entries loaded from a remote registry may be cached as governed by the
registry, and reloaded after the cache periods expires if a newer version is found.
Hence it is possible to define configuration elements such as (dynamic) sequences and
endpoints, as well as resources such as XSLT's, scripts or XSDs in the registry, and
update the configuration as these are allowed to dynamically change over time.

Synapse ships with a built-in URL based registry implementation called the
'SimpleURLRegistry' and this can be configured as follows:

<registry provider="org.apache.synapse.registry.url.SimpleURLRegistry">
<parameter name="root">file:./repository/conf/sample/resources/</parameter>
<parameter name="cachableDuration">15000</parameter>
</registry>

The 'root' parameter specifies the root URL of the registry for loaded resources. The
SimpleURLRegistry keys are path fragments, that when combined with the root prefix
would form the full URL for the referenced resource. The 'cachableDuration' parameter
specifies the number of milliseconds for which resources loaded from the registry
should be cached. More advanced registry implementations allows different cachable
durations to be specified for different resources, or mark some resources as never
expires. (e.g. Check the WSO2 ESB implementation based on Apache Synapse)

<a id="config--local-entry-local-registry-configuration"></a>

## Local Entry (Local Registry) Configuration

Local entries provide a convenient way to import various external configuration
artifacts into the Synapse runtime. This includes WSDLs, policies, XSLT files, and scripts. Local entry definitions are parsed at server startup and the referenced
configurations are loaded to the memory where they will remain until the server is
shut down. Other functional components such as sequences, endpoints and proxy services
can refer these locally defined in-memory configuration elements by using the local
entry keys.

The <localEntry> element is used to declare registry entries that are local
to the Synapse instance. Following syntax is used to define a local entry in the
Synapse configuration.

<localEntry key="string" [src="url"]>text | xml</localEntry>

A local entry may contain static text or static XML specified as inline content.
Following examples show how such static content can be included in local entry
definitions.

<localEntry key="version">0.1</localEntry>
<localEntry key="validate\_schema">
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
...
</xs:schema>
</localEntry>

Note the validate\_schema local entry which wraps some static XML schema content. A
mediator such as the validate mediator can refer this local entry to load its XML
schema definition.

A local entry may also point to a remote URL (specified using the 'src'
attribute) from which the contents can be loaded. This way the user does not have
to specify all external configurations in the Synapse configuration itself. The
required artifacts can be kept on the file system or hosted on a web server from where
Synapse can fetch them using a local entry definition. Following example shows
how a local entry is configured to load an XSLT file from the local file system.

<localEntry key="xslt-key-req" src="file:repository/conf/sample/resources/transform/transform.xslt"/>

It is important to note that Synapse loads the local entry contents only during
server start up (even when they are defined with a remote URL). Therefore any
changes done on the remote artifacts will not reflect on Synapse until the server
is restarted. This is in contrast to the behavior with remote registry where
Synapse reloads configuration artifacts as soon as the cache period expires.

<a id="config--sequence-configuration"></a>

## Sequence Configuration

As explained earlier a sequence resembles a message flow in Synapse and consists
of an array of mediators. The <sequence> element is used to define a sequence
in the Synapse configuration. Sequences can be defined with names so they can be
reused across the Synapse configuration. The sequences named 'main' and 'fault' have
special significance in a Synapse configuration. The 'main' sequence handles any message
that is accepted for '[Message Mediation](#config--messagemediation)'. The
'fault' sequence is invoked if Synapse encounters a fault, and a custom fault handler
is not specified for the sequence via its 'onError' attribute. If the 'main' or
'fault' sequences are not defined locally or not found in the Registry, Synapse
auto generates suitable defaults at initialization.

A Dynamic Sequence may be defined by specifying a key reference to a registry entry.
As the remote registry entry changes, the sequence will dynamically be updated
according to the specified cache duration and expiration. If tracing is enabled on a
sequence, all messages being processed through the sequence would write tracing
information through each mediation step to the 'trace.log' file configured via the
log4j.properties configuration.

The syntax outline of a sequence definition is given below.

<sequence name="string" [onError="string"] [key="string"] [trace="enable"] [statistics="enable"]>
mediator\*
</sequence>

The 'onError' attribute can be used to define a custom error handler sequence.
Statistics collection can be activated by setting the 'statistics' attribute to
'enable' on the sequence. In this mode the sequence will keep track of the number
of messages processed and their processing times. This statistical information can
then be retrieved through the Synapse statistics API.

All the immediate child elements of the sequence element must be valid mediators.
Following example shows a sequence configuration which consists of three child
mediators.

<sequence name="main" onError="errorHandler">
<log/>
<property name="test" value="test value"/>
<send/>
</sequence>

Sequences can also hand over messages to other sequences. In this sense a sequence
is analogous to a procedure in a larger program. In many programming languages
procedures can invoke other procedures. See the following example sequence
configuration.

<sequence name="foo">
<log/>
<property name="test" value="test value"/>
<sequence key="other\_sequence"/>
<send/>
</sequence>

Note how the message is handed to a sequence named 'other\_sequence' using the
'sequence' element. The 'key' attribute could point to another named sequence, a
local entry or a remote registry entry.

<a id="config--endpoint-configuration"></a>

## Endpoint Configuration

An <endpoint> element defines a destination for an outgoing message. There
are several types of endpoints that can be defined in a Synapse configuration.

- Address endpoint
- WSDL endpoint
- Load balance endpoint
- Fail-over endpoint
- Default endpoint
- Recipient list endpoint

Configuration syntax and runtime semantics of these endpoint types differ from
each other. However the high level configuration syntax of an endpoint definition
takes the following form.

<endpoint [name="string"] [key="string"]>
[address-endpoint](#config--addressendpointconfig) | [default-endpoint](#config--defaultendpointconfig) | [wsdl-endpoint](#config--wsdlendpointconfig) |
[load-balanced-endpoint](#config--lbendpointconfig) | [fail-over-endpoint](#config--foendpointconfig) | [recipient-list-endpoint](#config--recipientlistendpointconfig)
</endpoint>

Note how the endpoint definitions always start with an 'endpoint' element. The
immediate child element of this top level 'endpoint' element determines the type of
the endpoint. All above endpoint types can have a 'name' attribute, and such named
endpoints can be referred by other endpoints, through the key attribute. For example
if there is an endpoint named 'foo', the following endpoint can be used in any place, where 'foo' has to be used.

<endpoint key="foo"/>

This provides a simple mechanism for reusing endpoint definitions within a Synapse
configuration.

The 'trace' attribute turns on detailed trace information for messages being sent
to the endpoint. These will be available in the 'trace.log' file configured via the
log4j.properties file.

<a id="config--address-endpoint"></a>

### Address Endpoint

<address uri="*endpoint address*" [format="soap11|soap12|pox|get"] [optimize="mtom|swa"]
[encoding="*charset encoding*"]
[statistics="enable|disable"] [trace="enable|disable"]>
<enableSec [policy="*key*"]/>?
<enableAddressing [version="final|submission"] [separateListener="true|false"]/>?
<timeout>
<duration>*timeout duration in milliseconds*</duration>
<responseAction>discard|fault</responseAction>
</timeout>?
<markForSuspension>
[<errorCodes>xxx,yyy</errorCodes>]
<retriesBeforeSuspension>m</retriesBeforeSuspension>
<retryDelay>d</retryDelay>
</markForSuspension>
<suspendOnFailure>
[<errorCodes>xxx,yyy</errorCodes>]
<initialDuration>n</initialDuration>
<progressionFactor>r</progressionFactor>
<maximumDuration>l</maximumDuration>
</suspendOnFailure>
</address>

Address endpoint is an endpoint defined by specifying the EPR and other
attributes of the endpoint directly in the configuration. The 'uri' attribute
of the address element contains the EPR of the target endpoint. Message format
for the endpoint and the method to optimize attachments can be specified in the
'format' and 'optimize' attributes respectively. Security
policies for the endpoint can be specified in the policy attribute of the
'enableSec' element. WS-Addressing can be engaged
for the messages sent to the endpoint by using the 'enableAddressing' element.

The 'timeout' element of the endpoint configuration is used to set a specific
socket timeout for the endpoint. By default this is set to 1 minute (60 seconds).
When integrating with back-end services which take longer to respond the timeout
duration should be increased accordingly. The 'responseAction' element states
the action that should be taken in case a response is received after the timeout
period has elapsed. Synapse can either 'discard' the delayed response or inject it
into a 'fault' handler.

A Synapse endpoint is a state machine. At any given point in time it could be
in one of four states - Active, Timeout, Suspended and Switched Off. How and
when an endpoint changes its state is configurable through the Synapse configuration.
An endpoint in suspended or switched off states cannot be used to send messages.
Such an attempt would generate a runtime error.

By default an endpoint is in the 'Active' state. The endpoint will continue to
forward requests as long as its in this state. If an active endpoint encounters
an error while trying to send a message out (eg: a connection failure), the
endpoint may get pushed into the 'Timeout' state or the 'Suspended' state.
Generally most errors will put the endpoint straight into the 'Suspended' state.
Connection timeouts (error code 101504) and connection closed errors (101505)
are the only errors that will not directly suspend an endpoint. Using the
'errorCodes' element in the 'suspendOnFailure' configuration one can explicitly
define the errors for which the endpoint should be suspended. Similarly the
'errorCodes' element in the 'markForSuspension' configuration can be used to
define the errors for which the endpoint should be pushed into the 'Timeout'
state.

Endpoints in 'Timeout' state can be used to send messages. But any consecutive
errors while in this state can push the endpoint into the 'Suspended' state.
The number of consecutive errors that can suspend the endpoint can be configured
using the 'retriesBeforeSuspension' element in the 'markForSuspension' configuration.
The 'retryDelay' is used to specify a duration for which an endpoint will not be
available for immediate use after moving it to the 'Timeout' state. This duration
should be specified in milliseconds.

An endpoint in 'Suspended' state cannot be used to send messages. However the
suspension is only temporary. The suspend duration can be configured using the
'initialDuration' element. When this time period expires a suspended endpoint
becomes available for use again. However any recurring errors can put the
endpoint back in the 'Suspended' state. Such consecutive suspensions can also
progressively increase the suspend duration of the endpoint as configured by the
'progressionFactor' element. But the suspend duration will never exceed the
period configured in the 'maximumDuration' element. Note that both 'initialDuration'
and 'maximumDuration' should be specified in milliseconds.

Some example address endpoint configurations are given below. Note how the
communication protocol is used as a suffix to indicate the outgoing transport.

| Transport | Sample address |
| --- | --- |
| HTTP | http://localhost:9000/services/SimpleStockQuoteService |
| JMS | jms:/SimpleStockQuoteService? transport.jms.ConnectionFactoryJNDIName=QueueConnectionFactory& java.naming.factory.initial=org.apache.activemq.jndi.ActiveMQInitialContextFactory& java.naming.provider.url=tcp://localhost:61616& transport.jms.DestinationType=topic |
| Mail | mailto:guest@host |
| VFS | vfs:file:///home/user/directory |
|  | vfs:file:///home/user/file |
|  | vfs:ftp://guest:guest@localhost/directory?vfs.passive=true |

<a id="config--default-endpoint"></a>

### Default Endpoint

Default endpoint is an endpoint defined for adding QoS and other configurations
to the endpoint which is resolved from the 'To' address of the message context.
All the configurations such as message format for the endpoint, the method to
optimize attachments, and security policies for the endpoint
can be specified as in the case of Address Endpoint. This endpoint differs from
the address endpoint only in the 'uri' attribute which will not be present in
this endpoint. Following section describes the configuration of a default
endpoint.

<default [format="soap11|soap12|pox|get"] [optimize="mtom|swa"]
[encoding="*charset encoding*"]
[statistics="enable|disable"] [trace="enable|disable"]>
<enableSec [policy="*key*"]/>?
<enableAddressing [version="final|submission"] [separateListener="true|false"]/>?
<timeout>
<duration>*timeout duration in milliseconds*</duration>
<responseAction>discard|fault</responseAction>
</timeout>?
<markForSuspension>
[<errorCodes>xxx,yyy</errorCodes>]
<retriesBeforeSuspension>m</retriesBeforeSuspension>
<retryDelay>d</retryDelay>
</markForSuspension>
<suspendOnFailure>
[<errorCodes>xxx,yyy</errorCodes>]
<initialDuration>n</initialDuration>
<progressionFactor>r</progressionFactor>
<maximumDuration>l</maximumDuration>
</suspendOnFailure>
</default>

<a id="config--wsdl-endpoint"></a>

### WSDL Endpoint

WSDL endpoint is an endpoint definition based on a specified WSDL document. The
WSDL document can be specified either as a URI or as an inline definition within
the configuration. The service and port name containing the target EPR has to be
specified with the 'service' and 'port' (or 'endpoint') attributes respectively.
Elements like 'enableSec', 'enableAddressing', 'suspendOnFailure' and
'timeout' are same as for an Address endpoint.

<wsdl [uri="wsdl-uri"] service="qname" port/endpoint="qname">
<wsdl:definition>...</wsdl:definition>?
<wsdl20:description>...</wsdl20:description>?
<enableSec [policy="key"]/>?
<enableAddressing/>?
<timeout>
<duration>timeout duration in milliseconds</duration>
<responseAction>discard|fault</responseAction>
</timeout>?
<markForSuspension>
[<errorCodes>xxx,yyy</errorCodes>]
<retriesBeforeSuspension>m</retriesBeforeSuspension>
<retryDelay>d</retryDelay>
</markForSuspension>
<suspendOnFailure>
[<errorCodes>xxx,yyy</errorCodes>]
<initialDuration>n</initialDuration>
<progressionFactor>r</progressionFactor>
<maximumDuration>l</maximumDuration>
</suspendOnFailure>
</wsdl>

<a id="config--load-balance-endpoint"></a>

### Load Balance Endpoint

A Load balanced endpoint distributes the messages (load) among a set of listed
endpoints or static members by evaluating the load balancing policy and any other
relevant parameters. The policy attribute of the load balance element specifies the
load balance policy (algorithm) to be used for selecting the target endpoint or
static member. Currently only the roundRobin policy is supported. The 'failover'
attribute determines if the next endpoint or static member should be selected once
the currently selected endpoint or static member has failed, and defaults to true.
The set of endpoints or static members amongst which the load has to be distributed
can be listed under the 'loadBalance' element. These endpoints can belong to any
endpoint type mentioned in this document. For example, failover endpoints can be
listed inside the load balance endpoint to load balance between failover groups etc.
The 'loadbalance' element cannot have both 'endpoint' and 'member' child elements in
the same configuration. In the case of the 'member' child element, the 'hostName',
'httpPort' and/or 'httpsPort' attributes should be specified.

The optional 'session' element makes the endpoint a session affinity based load
balancing endpoint. If it is specified, sessions are bound to endpoints in the
first message and all successive messages for those sessions are directed to their
associated endpoints. Currently there are two types of sessions supported in session
aware load balancing. Namely HTTP transport based session which identifies the
sessions based on http cookies and the client session which identifies the session
by looking at a SOAP header sent by the client with the QName
'{http://ws.apache.org/ns/synapse}ClientID'. The 'failover' attribute mentioned
above is not applicable for session affinity based endpoints and it is always
considered as set to false. If it is required to have failover behavior in session
affinity based load balance endpoints, failover endpoints should be listed as the
target endpoints.

<loadBalance [policy="roundRobin"] [algorithm="impl of org.apache.synapse.endpoints.algorithms.LoadbalanceAlgorithm"]
[failover="true|false"]>
<endpoint .../>+
<member hostName="host" [httpPort="port"] [httpsPort="port2"]>+
</loadBalance>
<session type="http|simpleClientSession"/>?

<a id="config--dynamic-load-balance-endpoint"></a>

### Dynamic Load Balance Endpoint

This is a special variation of the load balance endpoint where instead of
having to specify the child endpoints explicitly, the endpoint automatically
discovers the child endpoints available for load balancing. These child
endpoints will be discovered using the 'membershipHandler' class. Generally, this
class will use a group communication mechanism to discover the application members.
The 'class' attribute of the 'membershipHandler' element should be an
implementation of org.apache.synapse.core.LoadBalanceMembershipHandler.
The 'membershipHandler' specific properties can be specified using the 'property'
elements. The 'policy' attribute of the 'dynamicLoadbalance' element specifies
the load balance policy (algorithm) to be used for selecting the next member to
which the message has to be forwarded. Currently only the 'roundRobin' policy is
supported. 'The failover' attribute determines if the next member should be
selected once the currently selected member has failed, and defaults to true.

<dynamicLoadBalance [policy="roundRobin"] [failover="true|false"]>
<membershipHandler class="impl of org.apache.synapse.core.LoadBalanceMembershipHandler">
<property name="name" value="value"/>+
</membershipHandler>
</dynamicLoadBalance>

Currently Synapse ships with one implementation of the LoadBalanceMembershipHandler
interface. This class is named 'Axis2LoadBalanceMembershipHandler' and its
usage is demonstrated in sample 57.

<a id="config--fail-over-endpoint"></a>

### Fail-Over Endpoint

Failover endpoints send messages to the listed endpoints with the following
failover behavior. At the start, the first listed endpoint is selected as the
primary and all other endpoints are treated as backups. Incoming messages are
always sent only to the primary endpoint. If the primary endpoint fails, next
active endpoint is selected as the primary and failed endpoint is marked as
inactive. Thus it sends messages successfully as long as there is at least one
active endpoint among the listed endpoints.

When a previously failed endpoint becomes available again, it will assume
its position as the primary endpoint and the traffic will be routed to that endpoint.
It is possible to disable this behavior by setting the 'dynamic' attribute to false.

<failover [dynamic="true|false"]>
<endpoint .../>+
</failover>

<a id="config--recipient-list-endpoint"></a>

### Recipient List Endpoint

A recipient list endpoint can be used to send a single message to a list of
recipients (child endpoints). This is used to implement the well-known
integration pattern named 'recipient list'. The same functionality can
be achieved using the 'clone' mediator, but the recipient list provides
a more natural and intuitive way of implementing such a scenario. Configuration
of the recipient list endpoint takes the following general form.

<recipientList name="string">
<endpoint>+
<member hostName="host" [httpPort="port"] [httpsPort="port2"]>+
</recipientList>

A recipient list can be named by setting the 'name' attribute on the 'recipientList'
element. Similar to a load balance endpoint, the recipient list endpoint also
wraps a set of endpoint definitions or a set of member definitions. At runtime
messages will be sent to all the child endpoints or members.

<a id="config--proxy-service-configuration"></a>

## Proxy Service Configuration

A <proxy> element is used to define a Synapse Proxy service.

<proxy name="string" [transports="(http |https |jms |.. )+|all"] [pinnedServers="(serverName )+"] [serviceGroup="string"]>
<description>...</description>?
<target [inSequence="name"] [outSequence="name"] [faultSequence="name"] [endpoint="name"]>
<inSequence>...</inSequence>?
<outSequence>...</outSequence>?
<faultSequence>...</faultSequence>?
<endpoint>...</endpoint>?
</target>?
<publishWSDL key="string" uri="string">
( <wsdl:definition>...</wsdl:definition> | <wsdl20:description>...</wsdl20:description> )?
<resource location="..." key="..."/>\*
</publishWSDL>?
<enableAddressing/>?
<enableSec/>?
<policy key="string" [type="(in | out)"]/>? // optional service or message level policies such as (e.g. WS-Security and/or WS-RM policies)
<parameter name="string"> // optional service parameters such as (e.g. transport.jms.ConnectionFactory)
string | xml
</parameter>
</proxy>

A proxy service is created and exposed on the specified transports through the
underlying Axis2 engine, exposing service EPRs as per the standard Axis2
conventions (ie based on the service name). Note that currently Axis2 does not allow
custom URI's to be set for services on some transports such as http/s. A proxy
service could be exposed over all enabled Axis2 transports such as http, https, JMS, Mail and File etc. or on a subset of these as specified by the optional
'transports' attribute. By default, if this attribute is not specified, Synapse
will attempt to expose the proxy service on all enabled transports.

In a clustered setup it might be required to deploy a particular proxy service
on a subset of the available nodes. This can be achieved using the 'pinnedServers'
attribute. This attribute takes a list of server names. At server startup Synapse
will check whether the name of the current host matches any of the names given
in this attribute and only deploy the proxy service if a match is found. The
server host name is picked from the system property 'SynapseServerName', failing
which the hostname of the machine would be used or default to 'localhost'. User can
specify a more meaningful name to a Synapse server instance by starting the server
using the following command.

./synapse.sh -serverName=<ServerName>

If Synapse is started as a daemon or a service, the above setting should be specified
in the wrapper.conf file.

By default when a proxy service is created it is added to an Axis service group
which has the same name as the proxy service. With the 'serviceGroup' attribute
this behavior can be further configured. A custom Axis service group can be specified
for a proxy service using the 'serviceGroup' attribute. This way multiple proxy
services can be grouped together at Axis2 level thus greatly simplifying service
management tasks.

Each service could define the target for received messages as a named sequence or a
direct endpoint. Either target inSequence or endpoint is required for the proxy
configuration, and a target outSequence defines how responses should be handled. Any
WS-Policies provided would apply as service level policies, and any service parameters
could be passed into the proxy service's AxisService instance using the 'parameter'
elements (e.g. the JMS destination etc). If the proxy service should enable
WS-Reliable Messaging or Security, the appropriate modules should be engaged, and
specified service level policies will apply. To engage the required modules, one may
use the 'enableSec', and 'enableAddressing' elements.

A dynamic proxy may be defined by specifying the properties of the proxy as dynamic
entries by referring them with the key. For example one could specify the
inSequence or endpoint with a remote key, without defining it in the local
configuration. As the remote registry entry changes, the properties of the proxy
will dynamically be updated accordingly. (Note: proxy service definition itself
cannot be specified to be dynamic; i.e <proxy key="string"/> is wrong)

A WSDL for the proxy service can be published using the 'publishWSDL' element.
The WSDL document can be loaded from the registry by specifying the 'key' attribute
or from any other location by specifying the 'uri' attribute. Alternatively the WSDL
can be provided inline as a child element of the 'publishWSDL' element. Artifacts
(schemas or other WSDL documents) imported by the WSDL can be resolved from the
registry by specifying appropriate 'resource' elements.

<publishWSDL key="my.wsdl">
<resource location="http://www.standards.org/standard.wsdl" key="standard.wsdl"/>
</publishWSDL>

In this example the WSDL is retrieved from the registry using the key 'my.wsdl'. It
imports another WSDL from location 'http://www.standards.org/standard.wsdl'. Instead
of loading it from this location, Synapse will retrieve the imported WSDL from the
registry entry 'standard.wsdl'.

Some well-known parameters that are useful when writing complex proxy services
are listed below. These can be included in a proxy configuration using 'parameter'
tags.

| Parameter | Value | Default | Description |
| --- | --- | --- | --- |
| useOriginalwsdl | true\|false | false | Use the given WSDL instead of generating the WSDL. |
| modifyUserWSDLPortAddress | true\|false | true | (Effective only with useOriginalwsdl=true) If true (default) modify the port addresses to current host. |
| showAbsoluteSchemaURL | true\|false | false | Show the absolute path of the referred schemas of the WSDL without showing the relative paths. |

Following table lists some transport specific parameters that can be passed into
proxy service configurations.

| Transport | Require | Parameter | Description |
| --- | --- | --- | --- |
| JMS | Optional | transport.jms.ConnectionFactory | The JMS connection factory definition (from axis2.xml) to be used to listen for messages for this service |
|  | Optional | transport.jms.Destination | The JMS destination name (Defaults to a Queue with the service name) |
|  | Optional | transport.jms.DestinationType | The JMS destination type. Accept values 'queue' or 'topic' (default: queue) |
|  | Optional | transport.jms.ReplyDestination | The destination where a reply will be posted |
|  | Optional | transport.jms.Wrapper | The wrapper element for the JMS message |

<a id="config--scheduled-task-configuration"></a>

## Scheduled Task Configuration

A <task> element is used to define a Synapse task (aka startup).

<task class="mypackage.MyTask" name="string" [pinnedServers="(serverName)+"]>
<property name="stringProp" value="String"/>
<property name="xmlProp">
<somexml>config</somexml>
</property>
<trigger ([[count="10"]? interval="1000"] | [cron="0 \* 1 \* \* ?"] | [once=(true | false)])/>
</task>

A task is created and scheduled to run at specified time intervals or as specified
by the cron expression. The 'class' attribute specifies the actual task
implementation class (which must implement org.apache.synapse.task.Task interface)
to be executed at the specified interval/s, and name specifies an identifier for
the scheduled task.

Fields in the task class can be set using properties provided as string literals or
XML fragments. For example, if the task implementation class has a field named
'version' with a corresponding setter method, the configuration value which will be
assigned to this field before running the task can be specified using a property with
the name 'version'.

There are three different trigger mechanisms to schedule tasks. A simple trigger is
specified with a 'count' and an 'interval', implying that the task will run a
'count' number of times at specified intervals. A trigger may also be specified as
a cron trigger using a cron expression. A one-time trigger is specified using the
'once' attribute in the definition and could be specified as true in which case the
task will be executed only once just after the initialization of Synapse.

In clustered deployments sometimes it would be necessary to deploy a particular task
in a selected set of nodes. This can be achieved using the optional 'pinnedServers'
attribute. A list of server names or host names can be specified in this attribute.
At server startup, Synapse will match the current server name or the host name with
the values specified in this attribute to see whether the task should be initialized
or not.

<a id="config--template-configuration"></a>

## Template Configuration

As explained earlier templates in synapse are defined in two flavors; sequence and
endpoint templates. The configuration, syntax forms and semantics of these are explained
in the following section.

A sequence template consist of two parts. As in any kind of a function, it has a
parameter set definition (argument list) and a function body definition. An important
difference is sequence template parameters are not typed (typically these are
string parameters, but can be of any type which is determined at runtime). Also
function body is a typical esb flow or a sequence.

The syntax outline of a sequence template definition is given below.

<template name="string">
<!-- parameters this sequence template will be supporting -->
(
<parameter name="string"/>
) \*
<!--this is the in-line sequence of the template -->
<sequence>
mediator+
</sequence>
</template>

A sequence template is a top level element defined with the 'name' attribute in Synapse
configuration. Both endpoint and sequence templates start with a 'template' element.
Parameters (defined by <parameter> elements) are the inputs supported by a
sequence template. These sequence template parameters can be referred by any xpath
expression defined within the in-lined sequence. For example parameter named 'foo' can
be referred by a property mediator (defined inside the in-line sequence of the template)
in following ways.

<property name="PropertyValue" expression="$func:foo"/>
<property name="PropertyValue" expression="get-property('foo', 'func')"/>

Note the scope variable used in the XPath expression. We use 'function' scope or '$func'
to refer to template parameters.

Invoking a sequence template can be done with a mediator named 'call-template' by
passing parameter values. The syntax outline of a call template mediator definition
is given below.

<call-template target="string">
<!-- parameter values will be passed on to a sequence template -->
(
<!--passing plain static values -->
<with-param name="string" value="string" /> |
<!--passing xpath expressions -->
<with-param name="string" value="{string}" /> |
<!--passing dynamic xpath expressions where values will be compiled dynamically-->
<with-param name="string" value="{{string}}" /> |
) \*
</call-template>

The 'call-template' mediator should define a target template it should be
invoking, with 'target' attribute.

The 'with-param' element is used to parse parameter values to a target
sequence template. Note that parameter names has to be exact matches to the names
specified in the target template. Parameter elements can contain three types of
parameterized values. xpath values are passed in within curly braces ({}) for value
attribute.

Endpoint templates are similar to the sequence templates in definition. Unlike
sequence templates, endpoint templates are always parameterized using '$' prefixed
values (NOT xpath expressions). Users can parameterize endpoint configuration elements
with these '$' prefixed values. An example is shown below.

<template name="ep\_template">
<parameter name="codes"/>
<parameter name="factor"/>
<parameter name="retries"/>
<endpoint name="$name">
<default>
<suspendOnFailure>
<errorCodes>$codes</errorCodes>
<progressionFactor>$factor</progressionFactor>
</suspendOnFailure>
<markForSuspension>
<retriesBeforeSuspension>$retries</retriesBeforeSuspension>
<retryDelay>0</retryDelay>
</markForSuspension>
</default>
</endpoint>
</template>

The syntax outline of a endpoint template definition is given below.

<template name="string">
<!-- parameters this endpoint template will be supporting -->
(
<parameter name="string"/>
) \*
<!--this is the in-line endpoint of the template -->
<endpoint [name="string"] >
address-endpoint | default-endpoint | wsdl-endpoint |
load-balanced-endpoint | fail-over-endpoint | recipient-list-endpoint
</endpoint>
</template>

As described earlier template endpoint is the artifact that makes a template of an
endpoint type into a concrete endpoint. In other words an endpoint template would
be useless without a template endpoint referring to it. This is semantically similar
to the relationship between a sequence template and a 'call-template' mediator.

The syntax outline of a template endpoint definition is as following..

<endpoint [name="string"] [key="string"] template="string">
<!-- parameter values will be passed on to a endpoint template -->
(
<parameter name="string" value="string" />
) \*
</endpoint>

Template endpoint defines parameter values that can parameterize an endpoint.
The 'template' attribute points to a target endpoint template.

As in the case of sequence template, note that parameter names has to be exact match
to the names specified in target endpoint template.

<a id="config--event-source-configuration"></a>

## Event Source Configuration

Event sources enable the user to run Synapse in the eventing mode of operation.
Synapse can act as an event source as well as an event broker. An event source
is defined using the <eventSource> configuration element.

<eventSource name="string">
<subscriptionManager class="mypackage.MyClass">
<parameter name="string"/>
</subscriptionManager>
</eventSource>

Once an event source is deployed in Synapse, it will provide a service URL (EPR) to
which clients can send WS-Eventing subscription requests. Clients can subscribe, unsubscribe and renew subscriptions by sending messages to this EPR. The subscription
manager configured inside the event source will be responsible for storing
and managing the subscriptions. The 'class' attribute of the 'subscriptionManager'
element should point to the Java class which provides this subscription management
functionality. Synapse ships with an in-memory subscription manager which
keeps and manages all subscriptions in memory.

Any additional parameters required to configure the subscription manager implementation
can be specified using the 'parameter' elements.

<a id="config--api-configuration"></a>

## API Configuration

APIs provide a flexible and powerful approach for defining full fledged REST APIs
in Synapse. An API definition starts with the <api> element.

<api name="string" context="string" [transport="http|https"][hostname="string"][port="int"]>
<resource [methods="http-method-list"][inSequence="string"][outSequence="string"]
[faultSequence="string"][url-mapping="string"][uri-template="string"]
[content-type="string"][user-agent="str"]>
<inSequence>...</inSequence>?
<outSequence>...</outSequence>?
<faultSequence>...</faultSequence>?
</resource>+
<handlers>
<handler class="name"/>+
</handlers>?
</api>

Each API definition must be uniquely named using the 'name' attribute. The 'context'
attribute is used to define the URL context at which the REST API will be anchored
(eg: /ws, /foo/bar, /soap). The API will only receive requests that fall in the
specified URL context. In addition to that an API could be bound to a particular
host and a port using the 'hostname' and 'port' attributes. The 'transport' attribute
can be used to restrict the API to process either HTTP messages or HTTPS messages only.

An API must also contain one or more resources. Resources define how messages
are processed and mediated by the API. A resource can be associated with a set of HTTP
methods using the 'methods' attribute. This attribute can support a single method name
(eg: GET) or a space separated list of methods (eg: GET PUT DELETE). The 'url-mapping'
and 'uri-template' attributes can be used to specify the type of URL requests that should
be handled by any particular resource. The 'url-mapping' attribute accepts any Java
servlet style URL mapping (eg: /test/\*, \*.jsp). The 'uri-template' attribute accepts
valid RFC6570 style expressions (eg: /orders/{orderId}). A resource can also refer
other sequences using the 'inSequence', 'outSequence' and 'faultSequence' attributes.
Alternatively these mediation sequences can be defined inline with the resource using
'inSequence', 'outSequence' and 'faultSequence' tags.

An API can also optionally define a set of handlers. These handlers are invoked
for each incoming API request, before they are dispatched to the appropriate
resources. The 'class' attribute on the 'handler' elements should contain the
ful qualified names of the handler implementation classes.

<a id="config--priority-executor-configuration"></a>

## Priority Executor Configuration

The priority executor configuration syntax takes the following general form.

<priority-executor name="string">
<queues isFixed="true|false" nextQueue="class implementing NextQueueAlgorithm">
<queue [size="size of the queue"] priority="priority of the messages put in to this queue"/>\*
</queues>
<threads core="core number of threads" max="max number of threads' keep-alive="keep alive time"/>
</priority-executor>

A priority executor consists of a thread pool and a set of queues for different
priority levels. Queues can be either bounded on unbounded in terms of capacity.
Each executor must define at least two queues. By default queues are unbounded.
By specifying the attribute 'size' they can be configured to have a limited capacity.
The 'priority' attribute specifies the priority level associated with a particular
queue. As explained earlier, higher the level, higher the priority the messages will
get.

The next queue algorithm is used to determine the next message processed. By default
Synapse uses a built-in priority queueing algorithm for this purpose. If required a
custom algorithm can be used by specifying the 'nextQueue' algorithm on the 'queues'
element.

The 'threads' element is used to configure the underlying thread pool. The 'core'
and 'max' attributes are used to specify the initial size and the maximum size of the
thread pool. A keep-alive time duration can be specified for idling threads using
the 'keep-alive' attribute where the duration is configured in seconds. If not
specified a default keep-alive duration of 5 seconds will be used.

In order to process messages through a priority executor one must use the 'enqueue'
mediator. This mediator can be used in a sequence or a proxy service to get all
requests processed through a pre-configured priority executor.

<enqueue priority="10" executor="MyExecutor"/>

For best results it's recommended to dispatch messages into priority executors
straight from the transport level. This can be achieved by adding an additional
parameter to the NHTTP transport configuration in the axis2.xml file of Synapse.

<parameter name="priorityConfigFile">file path</parameter>

The parameter should point to a separate XML configuration which defines the
priority configuration.

<Priority-Configuration>
<priority-executor name="priority-executor">
<queues isFixed="true|false">
<queue [size=""] priority=""/>\*
</queues>
<threads core="core number of threads" max="max number of threads' keep-alive="keep alive time"/>
</priority-executor>
<!-- conditions for calculating the priorities based on HTTP message -->
<conditions defaultPriority="default priority as an integer">
<condition priority="priority value as an integer">
one evaluator, this evaluator can contain other evaluators
</condition>
</conditions>
</Priority-Configuration>

<a id="config--message-stores-and-processors-configuration"></a>

## Message Stores and Processors Configuration

Both Message Stores and processors are top level configuration of synapse. Following
section tries to describe some of the syntax of the message store/processors
configurations.

The syntax outline of a message store definition is given below.

<messageStore name="string" class="classname" >
<parameter name="string" > "string" </parameter>\*
</messageStore>

The 'class' attribute value is the fully qualified class name of the underlying message
store implementation. There can be many message store implementations.Users can write
their own message store implementation and use it. Parameters section is used to
configure the parameters that is needed by underlying message store implementation.

The syntax outline of a message processor definition is given below.

<messageProcessor name="string" class="class name" messageStore="classname" >
<parameter name="string" > "string" </parameter>\*
</messageProcessor>

The 'class' attribute value is the fully qualified class name of the underlying message
processor implementation. There are two message processor implementations shipped by
default. There can be many message processor implementations.Users can write their
own message processor implementation and use it. Similar to message stores ,parameters
section here as well is used to configure the parameters that is needed by underlying
message processor implementation

Message Forwarding Processor : org.apache.synapse.message.processors.forward.ScheduledMessageForwardingProcessor

Sampling Processor : org.apache.synapse.message.processors.sampler.SamplingProcessor

As mentioned earlier, there are several message store/processor implementations
shipped by default. However if users wants to extend these following interfaces are
available.

Interface: org.apache.synapse.message.store.MessageStore
Abstract Class: org.apache.synapse.message.store.AbstractMessageStore
Interface: org.apache.synapse.message.processors.MessageProcessor
Abstract Class: org.apache.synapse.message.processors.AbstractMessageProcessor

---

<a id="mediators"></a>

<!-- source_url: https://synapse.apache.org/userguide/mediators.html -->

<!-- page_index: 6 -->

<a id="mediators--mediators-catalog"></a>

## Mediators Catalog

This document lists all the built-in mediators of Synapse and describes their
usage, functionality and configuration syntax.

<a id="mediators--contents"></a>

## Contents

- [Introduction](#mediators--intro)
- [Mediator Categories](#mediators--categories)
- [Core Mediators](#mediators--coremediators)
  - [Drop Mediator](#mediators--drop)
  - [Log Mediator](#mediators--log)
  - [Property Mediator](#mediators--property)
  - [Send Mediator](#mediators--send)
  - [Respond Mediator](#mediators--respond)
  - [Loopback Mediator](#mediators--loopback)
- [Filter Mediators](#mediators--filtermediators)
  - [Filter Mediator](#mediators--filter)
  - [In/Out Mediator](#mediators--inout)
  - [Switch Mediator](#mediators--switch)
  - [Validate Mediator](#mediators--validate)
- [Transformation Mediators](#mediators--transformationmediators)
  - [Header Mediator](#mediators--header)
  - [MakeFault Mediator](#mediators--makefault)
  - [Payload Factory Mediator](#mediators--payloadfactory)
  - [URL Rewrite Mediator](#mediators--urlrewrite)
  - [XSLT Mediator](#mediators--xslt)
  - [XQuery Mediator](#mediators--xquery)
- [Extension Mediators](#mediators--extensionmediators)
  - [Class Mediator](#mediators--clazz)
  - [POJO Command Mediator](#mediators--pojocommand)
  - [Script Mediator](#mediators--script)
  - [Spring Mediator](#mediators--spring)
- [Advanced Mediators](#mediators--advancedmediators)
  - [Aggregate Mediator](#mediators--aggregate)
  - [Cache Mediator](#mediators--cache)
  - [Callout Mediator](#mediators--callout)
  - [Clone Mediator](#mediators--clone)
  - [DBLookup Mediator](#mediators--dblookup)
  - [DBReport Mediator](#mediators--dbreport)
  - [Iterate Mediator](#mediators--iterate)
  - [RMSequence Mediator](#mediators--rmsequence)
  - [Store Mediator](#mediators--store)
  - [Throttle Mediator](#mediators--throttle)
  - [Transaction Mediator](#mediators--transaction)

<a id="mediators--introduction"></a>

## Introduction

Mediator is the basic message processing unit in Synapse. A mediator takes an
input message, carries out some processing on it, and provides an output message.
Mediators can be linked up and arranged into chains to implement complex message
flows (sequences). Mediators can manipulate message content (payload), properties, headers and if needed can also execute additional tasks such as database lookup, service invocation and script execution.

Apache Synapse ships with an array of useful mediators that can be used out of the
box to implement message flows, services and integration patterns. Rest of this
article describes these mediators in detail, along with their use cases and
configuration syntax.

<a id="mediators--mediator-categories"></a>

## Mediator Categories

Built-in mediators of Synapse can be classified into several groups depending
on the nature of their functionality and use cases.

- Core mediators - Utility mediators that are useful in a variety of scenarios
- Filter mediators - Mediators used to filter out messages
- Transform mediators - Mediators used to transform message content, headers and
  attributes
- Extension mediators - Mediators used to extend the Synapse mediation engine by
  plugging in custom developed code
- Advanced mediators - Mediators used to implement advanced integration scenarios
  and patterns

Rest of this article is structured according to the above classification. Mediators
in each section are arranged in the alphabetical order.

<a id="mediators--core-mediators"></a>

## Core Mediators

<a id="mediators--drop-mediator"></a>

### Drop Mediator

Drop mediator can be used to drop the current message being processed and
terminate a message flow. This mediator is configured as follows and it
does not take any additional parameters or arguments.

<drop/>

<a id="mediators--log-mediator"></a>

### Log Mediator

Log mediator can be used in any sequence or proxy service to log the messages
being mediated. Log entries generated by the log mediator will go into the
standard Synapse log files. This can be further configured using the
log4j.properties file.

By default, the log mediator only logs a minimalistic set of details to avoid
the message content being parsed. But if needed it can be configured to log the
full message payload, headers and even custom user defined properties. The log
mediator configuration takes the following general form.

<log [level="simple|full|headers|custom"] [separator="string"]
[category="INFO|DEBUG|WARN|ERROR|TRACE|FATAL"]>
<property name="string" (value="literal" | expression="xpath")/>\*
</log>

The 'level' attribute is used to specify how much information should be logged
by the log mediator. This attribute can take one of following four values.

- simple - Logs a set of standard headers (To, From, WSAction, SOAPAction,
  ReplyTo and MessageID). If no log level is specified, this level will be
  used by default.
- full - Logs all standard headers logged in the log level 'simple' and also
  the full payload of the message. This log level causes the message content
  to be parsed and hence incurs a performance overhead.
- headers - Logs all SOAP header blocks
- custom - Only logs the user defined properties (see the next section)

Users can define custom attributes and properties to be logged by the log mediator
by specifying some 'property' elements. Each property must be named, and can
have a constant value or an XPath expression. If a constant value is specified, that value will be logged with each and every entry logged by the mediator. If
an XPath is specified instead, that XPath will be evaluated on the message being
mediated and the outcome will be included in the generated log entry.

By default, all properties and attributes logged by the log mediator are separated
by commas (,). This can be configured using the 'separator' attribute. Further
all logs generated by the mediator are logged at log4j log level 'INFO' by default.
This behavior can also be configured using the 'category' attribute.
In addition to this behaviour, when 'category' is set to debug, logs can be printed
at log4j log level 'INFO' by starting the server with the following flag. This is
especially helpful during the development time to quickly debug the mediation flow.

Linux / Unix: ./synapse.sh -synapseDebug
Windows: synapse.bat -synapseDebug

<a id="mediators--property-mediator"></a>

### Property Mediator

Every message mediated through Synapse can have a set of associated properties.
Synapse engine and the underlying transports set a number of properties on
each message processed which can be manipulated by the user to modify the
runtime behavior of the message flows. In addition, user can set his/her own
properties on the message which is very helpful when it comes to managing
message flow state and storing scenario specific variables. For an example in
some situations a user might want to access a particular value in the request
payload while processing a response. This can be easily achieved by setting the
required value to a property in the request (in) sequence and then later accessing
that property in the response (out) sequence.

Property mediator is used to manipulate the properties of a message. This
mediator can be used to set and remove property values. When it comes to setting
property values, the input could be a constant or a variable value generated
by an XPath expression. The syntax for configuring the property mediator is as
follows.

<property name="string" [action=set|remove] [type="string"] (value="literal" | expression="xpath") [scope=default|transport|axis2|axis2-client] [pattern="regex" [group="integer"]]>
<xml-element/>?
</property>

The 'name' attribute specifies the name of the property which needs to be either
set or removed while the 'action' attribute specifies the exact action that needs
to be carried out by the mediator. If not specified action will default to 'set'.

When setting a property value, either the 'value' or the 'expression' attribute
must be specified. The 'value' attribute can be used to set a constant as
the property value whereas the 'expression' attribute can be used to specify an
XPath expression. If an XPath expression is specified, Synapse will evaluate that
on the message to determine the value that needs to be assigned to the property.

Synapse properties are scoped. Therefore, when using this mediator the user should
specify the scope at which the property will be set or removed from. If not
specified, property mediator will work at the 'default' scope. Properties set in
this scope last as long as the transaction (request-response) exists. Properties
set on scope 'axis2' has a shorter life span and it's mainly used for passing
parameters to the underlying Axis2 engine. Properties set in the 'transport'
scope will be treated as transport headers. For an example if it is required to
send an HTTP header named 'CustomHeader' with an outgoing request, one may use
the property mediator configuration.

<property name="CustomHeader" value="some value" scope="transport" type="type name"/>

This will force Synapse to send a transport header named 'CustomHeader' along
with the outgoing message. Property mediator also supports a scope named
'axis2-client'. Properties set in this scope will be treated as Axis2 client
options.

When using properties to store user or scenario specific information it is
recommended to always use the 'default' scope. Other scopes should not be used
for custom development or mediation work since they have the potential to
alter the behavior of the underlying Axis2 engine and transports framework.

By default, property mediator sets all property values as strings. It is possible
to set properties in other types by specifying the 'type' attribute. This attribute
can accept one of following values.

- STRING
- BOOLEAN
- DOUBLE
- FLOAT
- INTEGER
- LONG
- SHORT
- OM

The type names are case sensitive. Type 'OM' can be used to set XML property
values on the message context. This becomes useful when the expression associated
with the property mediator evaluates to an XML node during mediation. With the
type attribute set to 'OM' the resulting XML will be converted to an AXIOM
OMElement before assigning it to a property.

It is also possible to use the property mediator to set some static XML content
as a property value. To do this specify the static XML content as a child node
of the 'property' element instead of using the 'value' attribute.

<a id="mediators--send-mediator"></a>

### Send Mediator

Send mediator is used to send requests to endpoints. The same can be used
to send response messages back to clients. The send mediator is configured using
the following XML syntax.

<send [receive="string"]>
(endpointref | endpoint)?
</send>

Messages are sent to the endpoint specified as the child of the
'send' element. An optional receiving sequence can be configured using the
'receive' attribute. When specified, response messages from the endpoint will
be dispatched to the referred sequence. This makes it easier to implement
complex service chaining scenarios, where the response from one service needs
to be processed and directed to another service.

The send mediator can be configured without any child endpoints. For an example
following is a perfectly valid send mediator configuration.

<send/>

In this case the messages will be sent to an implicit endpoint. If the message
is a request from a client, Synapse will lookup the 'To' header of the request and
simply forward it to the service addressed by that header. If it is a response
from a back-end service, Synapse will simply send it back to the original
client who initiated the original message flow.

The service invocations done by the send mediator may or may not be
synchronous based on the underlying transport used. If the default non-blocking
HTTP transport is used, the send mediator will make an asynchronous invocation
and release the calling thread as soon as possible. Synapse will asynchronously
handle the response from the endpoint while the giving the illusion that Synapse
is making blocking service calls.

<a id="mediators--respond-mediator"></a>

### Respond Mediator

The Respond Mediator stops the processing on the current message flow and sends
the message back to the client as a response.

<respond/>

<a id="mediators--loopback-mediator"></a>

### Loopback Mediator

The Loopback Mediator moves the message from the In flow to the Out flow.
All the configuration in the In flow that appears after the Loopback mediator is skipped.

<loopback/>

<a id="mediators--filter-mediators"></a>

## Filter Mediators

<a id="mediators--filter-mediator"></a>

### Filter Mediator

Filter mediator adds 'if-else' like semantics to the Synapse configuration language.
It can be used to evaluate a condition on a message and take some action
based on the outcome. The configuration of the filter mediator takes the
following form.

<filter (source="xpath" regex="string") | xpath="xpath">
mediator+
</filter>

The filter mediator either tests the given XPath expression as a boolean
expression, or matches the result of the source XPath expression as a string
against the given regular expression. If the condition evaluates to true, the
filter mediator will execute the enclosed child mediators.

Alternatively, one can use the following syntax to configure the filter mediator.

<filter (source="xpath" regex="string") | xpath="xpath">
<then [sequence="string"]>
mediator+
</then>
<else [sequence="string"]>
mediator+
</else>
</filter>

In this case also the filter condition is evaluated in the same manner as
described above. Messages for which the condition evaluates to true will be
mediated through the mediators enclosed by the 'then' element. Failed messages
will be mediated through the mediators enclosed by the 'else' element.

<a id="mediators--in-out-mediators"></a>

### In/Out Mediators

In mediator and Out mediator are used to filter out traffic based on the
direction of the messages. As their names imply, In mediator processes only
the requests (in messages) while ignoring the responses (out messages). The
out mediator does the exact opposite by processing only the responses while
ignoring the requests. In many occasions these two mediators are deployed
together to create separate flows for requests and responses. The syntax
outline for the two mediators is given below.

<in>
mediator+
</in>
<out>
mediator+
</out>

In mediator will process requests through the child mediators and the Out
mediator will process responses through the child mediators.

<a id="mediators--switch-mediator"></a>

### Switch Mediator

Switch mediator provides switch-case semantics in the Synapse configuration
language.

<switch source="xpath">
<case regex="string">
mediator+
</case>+
<default>
mediator+
</default>?
</switch>

The source XPath is executed on the messages. The resulting value is then
tested against the regular expressions defined in each 'case' element. When
a matching case is found, the message will be mediated through its child
mediators. If none of the cases match, the message will be handed to the 'default'
case (if available).

<a id="mediators--validate-mediator"></a>

### Validate Mediator

The validate mediator validates the XML node selected by
the source xpath expression, against the specified XML schema. If the source
attribute is not specified, the validation is performed against the first
child of the SOAP body of the current message. If the validation fails, the on-fail sequence of mediators is executed. Feature elements could be used to
turn on/off some of the underlying features of the schema validator (See <http://xerces.apache.org/xerces2-j/features.html>).
The schema can be specified as a static or dynamic key. When
needed, imports can be specified using additional resources.

<validate [source="xpath"]>
<schema key="string" />+
<resource location="<external-schema>" key="string">\*
<feature name="<validation-feature-name>" value="true|false"/>\*
<on-fail>
mediator+
</on-fail>
</validate>

<a id="mediators--transformation-mediators"></a>

## Transformation Mediators

<a id="mediators--header-mediator"></a>

### Header Mediator

Header mediator sets or removes a specified header from the message.
The optional 'scope' attribute specifies the scope of the header.
Scope can be either 'soap' or 'transport'.
If the scope is set to 'soap', header is treated as a soap header and if it is 'transport', header is treated as a transport header.
If the scope is omitted, header is treated as a soap header or one of the below mentioned known headers.
The optional 'action' attribute specifies whether the mediator should
set or remove the header. If omitted, it defaults to 'set' action.

<header [name="qname"] (value="literal" | expression="xpath") [action="set"] [scope="soap | transport"]>
[<embeddedxml/>]
</header>

<header name="qname" action="remove" [scope="soap | transport"]/>

The value of the 'name' attribute must be one of the following aliases or
a valid QName with a namespace prefix. In the latter case the namespace prefix
must be mapped to a valid namespace URI using the standard 'xmlns' attribute.
When setting an embedded xml element as a soap header, 'name' attribute is not required.

- To
- From
- Action
- FaultTo
- ReplyTo
- RelatesTo

<a id="mediators--makefault-mediator"></a>

### MakeFault Mediator

MakeFault mediator transforms the current message into a fault message.
It should be noted that makeFault mediator does NOT send the message after
transforming it. A send mediator needs to be invoked separately to send
a fault message created by this mediator.

<makefault [version="soap11|soap12|pox"] [response="true|false"]>
<code (value="literal" | expression="xpath")/>
<reason (value="literal" | expression="xpath")/>
<node>...</node>?
<role>...</role>?
(<detail expression="xpath"/> | <detail>...</detail>)?
</makefault>

The To header of the fault message is set to the 'Fault-To' of the original message
if such a header exists on the original message. Depending on the 'version'
attribute, the fault message is created as a SOAP 1.1, SOAP 1.2
or POX fault. If the optional response attribute value is set as 'true', makefault mediator marks the message as a response. Optional 'node',
'role' and 'detail' sub-elements in the mediator configuration can
be used to set the corresponding elements in the resulting SOAP fault.

<a id="mediators--payload-factory-mediator"></a>

### Payload Factory Mediator

Payload-factory mediator creates a new SOAP payload for the message, replacing
the existing one. printf() style formatting is used to configure the
transformation performed by this mediator.

<payloadFactory>
<format>"xmlstring"</format>
<args>
<arg (value="literal" | expression="xpath")/>\*
</args>
</payloadFactory>

'format' sub-element of the mediator configuration specifies the format of the
new payload. All $n occurrences in the format will be replaced by the value of
the n th argument at runtime. Each argument in the mediator configuration could
be a static value or an XPath expression. When an expression is used, value is
fetched at runtime by evaluating the provided XPath expression against the
existing SOAP message/message context.

<a id="mediators--url-rewrite-mediator"></a>

### URL Rewrite Mediator

URL Rewrite mediator can be used to modify and transform the URL values
available in the message. By default, this mediator takes the 'To' header of the
message and apples the provided rewrite rules on it. Alternatively, one can
specify a property name in the 'inProperty' attribute, in which case the
mediator takes the value of the specified property as the input URL.

Similarly, the mediator by default sets the transformed URL as the 'To' header of
the message and alternatively you can use the 'outProperty' attribute to
instruct the mediator to set the resulting URL as a property.

<rewrite [inProperty="string"] [outProperty="string"]>
<rewriterule>
<condition>
...
</condition>?
<action [type="append|prepend|replace|remove|set"] [value="string"]
[xpath="xpath"] [fragment="protocol|host|port|path|query|ref|user|full"] [regex="regex"]>+
</rewriterule>+
</rewrite>

The mediator applies URL transformations by evaluating a set of rules on
the message. Rules are specified using the 'rewriterule' element. Rules are
evaluated in the order in which they are specified. A rule can consist of an
optional condition and one or more rewrite actions. If the condition is provided, it is evaluated first and specified rewrite actions are executed only if the
condition evaluates to true. If no condition is specified, the provided rewrite
actions will be always executed. The condition should be wrapped in a 'condition'
element within the 'rewriterule' element. Rewrite actions are specified using
'action' elements.

<a id="mediators--xquery-mediator"></a>

### XQuery Mediator

The XQuery mediator can be used to perform an XQuery transformation. 'key'
attribute specifies the XQuery transformation, and the optional 'target'
attribute specifies the node of the message that should be transformed.
This defaults to the first child of the SOAP body of the payload. 'variable'
element defines a variable that could be bound to the dynamic context of the
XQuery engine in order to access those variables through the XQuery script.

<xquery key="string" [target="xpath"]>
<variable name="string" type="string" [key="string"] [expression="xpath"] [value="string"]/>?
</xquery>

It is possible to specify just a literal 'value', or an XPath expression
over the payload, or even specify a registry key or a registry key
combined with an XPath expression that selects the variable. The name of
the variable corresponds to the name of variable declaration in the XQuery
script. The 'type' of the variable must be a valid type defined by the
JSR-000225 (XQJ API).

The supported types are:

- XQItemType.XQBASETYPE\_INT -> INT
- XQItemType.XQBASETYPE\_INTEGER -> INTEGER
- XQItemType.XQBASETYPE\_BOOLEAN -> BOOLEAN
- XQItemType.XQBASETYPE\_BYTE - > BYTE
- XQItemType.XQBASETYPE\_DOUBLE -> DOUBLE
- XQItemType.XQBASETYPE\_SHORT -> SHORT
- XQItemType.XQBASETYPE\_LONG -> LONG
- XQItemType.XQBASETYPE\_FLOAT -> FLOAT
- XQItemType.XQBASETYPE\_STRING -> STRING
- XQItemType.XQITEMKIND\_DOCUMENT -> DOCUMENT
- XQItemType.XQITEMKIND\_DOCUMENT\_ELEMENT -> DOCUMENT\_ELEMENT
- XQItemType.XQITEMKIND\_ELEMENT -> ELEMENT

<a id="mediators--xslt-mediator"></a>

### XSLT Mediator

XSLT mediator applies the specified XSLT transformation to the selected
element of the current message payload. 'source' attribute selects the source
element to apply the transformation on. Where not specified, it defaults to the
first child of the SOAP body. Output of the transformation replaces the source
element when 'target' attribute is not specified. Otherwise, the output is
stored in the property specified by the 'target' attribute.

<xslt key="string" [source="xpath"] [target="string"]>
<property name="string" (value="literal" | expression="xpath")/>\*
<feature name="string" value="true | false" />\*
<attribute name="string" value="string" />\*
<resource location="..." key="..."/>\*
</xslt>

If the output method specified by the stylesheet is text (i.e. the stylesheet
has the <xsl:output method="text"/> directive), then the output of the transformation is wrapped in an element with name
{http://ws.apache.org/commons/ns/payload}text. Note that when an
element with this name is present as the first child of the SOAP body of an
outgoing message, JMS and VFS transports automatically unwrap the
content and send it out as plain text. XSLT mediator can therefore be used for
integration with systems relying on plain text messages.

Usage of sub-elements of XSLT mediator configuration is as follows:

- property - Stylesheet parameters can be passed into the transformations
  using 'property' elements.
- feature - Defines any features which should be explicitly set to the
  TransformerFactory. For example,
  'http://ws.apache.org/ns/synapse/transform/feature/dom' feature
  enables DOM based transformations instead of serializing elements into byte
  streams and/or temporary files. Although enabling this feature could improve
  performance of the transformation, it might not work for all transformations.
- attribute - Defines attributes which should be explicitly set on the
  TransformerFactory.
- resource - Can be used to resolve XSLT imports and includes from the
  repository. It works in exactly the same way as the corresponding element in
  a <proxy> definition.

<a id="mediators--extension-mediators"></a>

## Extension Mediators

<a id="mediators--class-mediator"></a>

### Class Mediator

The class mediator makes it possible to use a custom class as a mediator. The
class must implement the org.apache.synapse.api.Mediator interface. If any properties are
specified, the corresponding setter methods are invoked on the class, once, during initialization.

<class name="class-name">
<property name="string" value="literal">
(either literal or XML child)
</property>
</class>

This mediator creates an instance of a specified class and sets it as a
mediator. If any properties are specified, the corresponding setter methods are
invoked on the class with the given values, once, during initialization.

<a id="mediators--pojo-command-mediator"></a>

### POJO Command Mediator

POJO Command mediator implements the popular Command design pattern and can be
used to invoke an object which encapsulates a method call.

<pojoCommand name="class-name">
(
<property name="string" value="string"/> |
<property name="string" context-name="literal" [action=(ReadContext | UpdateContext | ReadAndUpdateContext)]>
(either literal or XML child)
</property> |
<property name="string" expression="xpath" [action=(ReadMessage | UpdateMessage | ReadAndUpdateMessage)]/>
)\*
</pojoCommand>

POJO Command mediator creates an instance of the specified command class, which may implement the org.apache.synapse.Command interface or should have a
method with "public void execute()" signature. If any properties are specified, the corresponding setter methods are invoked on the class before each message is
executed. It should be noted that a new instance of the POJO Command class is
created to process each message processed. After execution of the POJO Command
mediator, depending on the 'action' attribute of the property, the new value
returned by a call to the corresponding getter method is stored back to the
message or to the context. The 'action' attribute may specify whether this
behaviour is expected or not via the Read, Update and ReadAndUpdate values.

<a id="mediators--script-mediator"></a>

### Script Mediator

Synapse supports mediators implemented in a variety of scripting languages such
as JavaScript, Python and Ruby. There are two ways of defining a script mediator, either with the script program statements stored in a separate file which is
referenced via the local or remote registry entry, or with the script program
statements embedded in-line within the Synapse configuration. A script mediator
using a script off the registry (local or remote) is defined as follows:

<script key="string" language="string" [function="script-function-name"]/>

The property key is the registry key to load the script. The language
attribute specifies the scripting language of the script code (e.g. "js"
for Javascript, "rb" for ruby, "groovy" for Groovy, "py" for Python..).
The function is an optional attribute defining the name of the script
function to invoke, if not specified it defaults to a function named
'mediate'. The function is passed a single parameter - which is the
Synapse MessageContext. The function may return a boolean, if it does not, then true is assumed, and the script mediator returns this value. An
inline script mediator has the script source embedded in the configuration
as follows:

<script language="string">...script source code...<script/>

If the specified script calls a function defined in another script, then the
latter script should also be included in the script mediator configuration.
It's done using the 'include' sub-element of the mediator configuration. The key
attribute of the 'include' element should point to the script which has to be
included. The included script could be stored as a local entry or in the remote
registry. Script includes are defined as follows:

<script key="string" language="string" [function="script-function-name"]>
<include key="string"/>
</script>

The execution context environment of the script has access to the Synapse
MessageContext predefined in a script variable named 'mc'. An example of
an inline mediator using JavaScript/E4X which returns false if the SOAP
message body contains an element named 'symbol' which has a value of 'IBM'
would be:

<script language="js">mc.getPayloadXML()..symbol != "IBM";<script/>

Synapse uses the Apache
[Bean Scripting Framework](http://jakarta.apache.org/bsf/)
for the scripting language support, any script language supported by BSF may be
used to implement a Synapse mediator.

Implementing a mediator with a script language can have advantages over
using the built in Synapse mediator types or implementing a custom Java
class mediator. Script mediators have all the flexibility of a class
mediator with access to the Synapse MessageContext and SynapseEnvironment
APIs, and the ease of use and dynamic nature of scripting languages allows
rapid development and prototyping of custom mediators. An additional
benefit of some scripting languages is that they have very simple and
elegant XML manipulation capabilities, for example JavaScript E4X or Ruby
REXML, so this makes them well suited for use in the Synapse mediation
environment. For both types of script mediator definition, the
MessageContext passed into the script has additional methods over the
standard Synapse MessageContext to enable working with the XML in a way
natural to the scripting language. For example when using JavaScript
getPayloadXML and setPayloadXML, E4X XML objects, and when using Ruby, REXML documents.

The complete list of available methods can be found in the
[ScriptMessageContext Javadoc](https://synapse.apache.org/apidocs/org/apache/synapse/mediators/bsf/ScriptMessageContext.html).

<a id="mediators--spring-mediator"></a>

### Spring Mediator

The Spring mediator exposes a spring bean as a mediator. In other terms, it
creates an instance of a mediator, which is managed by Spring. This Spring bean
must implement org.apache.synapse.api.Mediator interface.

<spring:spring bean="string" key="string" xmlns:spring="http://ws.apache.org/ns/synapse/spring"/>

'key' attribute refers to the Spring ApplicationContext/Configuration
(i.e. spring configuration XML) used for the bean. This key can be a registry
key or local entry key. The bean attribute is used for looking up a Spring bean
from the spring Application Context. Therefore, a bean with same name must be in
the given spring configuration. In addition to that, that bean must implement
the Mediator interface.

<a id="mediators--advanced-mediators"></a>

## Advanced Mediators

<a id="mediators--aggregate-mediator"></a>

### Aggregate Mediator

Aggregate mediator implements the Message Aggregator EIP by aggregating the
messages or responses for split messages generated using either the clone or
iterate mediator.

<aggregate [id="string"]>
<correlateOn expression="xpath"/>?
<completeCondition [timeout="time-in-seconds"]>
<messageCount min="int-min" max="int-max"/>?
</completeCondition>?
<onComplete expression="xpath" [sequence="sequence-ref"]>
(mediator +)?
</onComplete>
</aggregate>

This mediator can also aggregate messages on the presence of matching elements
specified by the correlateOn XPath expression. Aggregate will collect the
messages coming into it until the messages collected on the aggregation
satisfies the complete condition. The completion condition can specify a minimum
or maximum number of messages to be collected, or a timeout value in seconds, after which the aggregation terminates. On completion of the aggregation it will
merge all of the collected messages and invoke the onComplete sequence on it.
The merged message would be created using the XPath expression specified by the
attribute 'expression' on the 'onComplete' element.

<a id="mediators--cache-mediator"></a>

### Cache Mediator

Cache mediator is used for simple response message caching in Synapse. When a
message reaches the cache mediator, it checks weather an equivalent message is
already cached using a hash value.

When the cache mediator detects that the message is a cached message, it fetches
the cached response and prepares Synapse for sending the response. If a sequence
is specified for a cache hit, user can send back the response message within
this sequence using a send mediator. If a sequence is not specified, then cached
response is sent back to the client.

<cache [id="string"] [hashGenerator="class"] [timeout="seconds"] [scope=(per-host | per-mediator)]
collector=(true | false) [maxMessageSize="in-bytes"]>
<onCacheHit [sequence="key"]>
(mediator)+
</onCacheHit>?
<implementation type=(memory | disk) maxSize="int"/>
</cache>

This mediator will evaluate the hash value of an incoming message as described
in the optional hash generator implementation (which should be a class
implementing the org.wso2.caching.digest.DigestGenerator interface). The default
hash generator is 'org.wso2.caching.digest.DOMHashGenerator'. If the generated
hash value has been found in the cache then the cache mediator will execute the
onCacheHit sequence which can be specified inline or referenced. The cache
mediator must be specified with an 'id' and two instances with this same 'id'
that correlates the response message into the cache for the request message
hash. The optional 'timeout' specifies the valid duration for cached elements, and the scope defines if mediator instances share a common cache per every host
instance, or per every cache mediator pair (i.e. 'id') instance. 'collector'
attribute value 'true' specifies that the mediator instance is a response
collection instance, and 'false' specifies that its a cache serving instance.
The maximum size of a message to be cached could be specified with the optional
'maxMessageSize' attributes in bytes and defaults to unlimited. Finally,
'implementation' element may define if the cache is disk or memory based, and
'maxSize' attribute defines the maximum number of elements to be cached.

> [!NOTE]
> <a id="mediators--callout-mediator"></a>

>
> ### Callout Mediator
>
> Callout mediator performs a blocking external service invocation during mediation.
> The target external service can be configured either using a child endpoint element
> or using the 'serviceURL' attribute. When serviceURL is specified, it is used as
> the EPR of the external service. We can specify the endpoint element if we want to
> leverage endpoint functionality like format conversions, security, etc.
> The target endpoint can be defined inline or we can refer to an existing named
> endpoint in the configuration.
> Only Leaf endpoint types (Address/WSDL/Default) are supported.
> When both serviceURL and endpoint is not present, 'To' header on the request is
> used as the target endpoint.
>
> <callout [serviceURL="string"] [action="string"][passHeaders="true|false"] [initAxis2ClientOptions="true|false"] >
> <configuration [axis2xml="string"] [repository="string"]/>?
> <endpoint/>?
> <source xpath="expression" | key="string">?
> <target xpath="expression" | key="string"/>?
> <enableSec policy="string" | outboundPolicy="String" | inboundPolicy="String" />?
> </callout>
>
> 'action' attribute can be used to specify the SOAP Action of the external service
> call. When 'initAxis2ClientOptions' is set to false, axis2 client options available
> in the incoming message context is reused for the service invocation.
> When 'passHeaders' is set to true, SOAP Headers of the received message is parsed
> to the external service.
>
> The source element specifies the payload for the request message using an XPath
> expression or a registry key.
> When source element is not defined, entire SOAP Envelope arrived at the Callout
> mediator is treated as the source.
> The target element specifies a node, at which the response payload will be
> attached into the current message, or the name of a key/property using which the
> response would be attached to the current message context as a property.
> When target element is not specified, entire SOAP Envelope arrived to the
> Callout mediator is replaced from the response received from the external service
> invocation.
>
> Since the callout mediator performs a blocking call, it cannot use the default
> non-blocking http/s transports based on Java NIO, and thus defaults to
> using the repository/conf/axis2\_blocking\_client.xml as the
> Axis2 configuration, and repository/ as the client repository
> unless these are specified inside the 'configuration' sub-element.
>
> To invoke secured services, Callout mediator can be configured to enable WS-Security
> using the 'enableSec' element. Security policy should be specified using the 'policy'
> attribute which may point to a registry key or a local entry. You can also specify
> two different policies for inbound and outbound messages (flows). This is done by
> using the 'inboundPolicy' and 'outboundPolicy' attributes. These security
> configurations will not get activated if we configure the external service using
> the endpoint element. When endpoint is defined, security settings can be
> configured at the endpoint.

<a id="mediators--clone-mediator"></a>

### Clone Mediator

Clone mediator can be used to create several clones or copies of a message. This
mediator implements the Message Splitter EIP by splitting the message into
number of identical messages which will be processed in parallel. They can also
be set to process sequentially by setting the value of the optional 'sequential'
attribute to 'true'.

<clone [id="string"] [sequential=(true | false)] [continueParent=(true | false)]>
<target [to="uri"] [soapAction="qname"] [sequence="sequence\_ref"] [endpoint="endpoint\_ref"]>
<sequence>
(mediator)+
</sequence>?
<endpoint>
endpoint
</endpoint>?
</target>+
</clone>

The original message can be continued or dropped depending on the boolean value
of the optional 'continueParent' attribute. Optionally a custom 'To' address
and/or a 'Action' may be specified for cloned messages. The optional 'id'
attribute can be used to identify the clone mediator which created a particular
split message when nested clone mediators are used. This is particularly useful
when aggregating responses of messages that were created using nested clone
mediators.

<a id="mediators--dblookup"></a>

### DBLookup

DB Lookup mediator is capable of executing an arbitrary SQL SELECT statement, and then set some resulting values as local message properties on the message
context. The DB connection used maybe looked up from an external DataSource or
specified in-line, in which case an Apache DBCP connection pool is established
and used.

<dblookup>
<connection>
<pool>
(
<driver/>
<url/>
<user/>
<password/>
<property name="name" value="value"/>\*
|
<dsName/>
<inClass/>
<url/>
<user/>
<password/>
)
</pool>
</connection>
<statement>
<sql>SELECT something FROM table WHERE something\_else = ?</sql>
<parameter [value="" | expression=""] type="CHAR|VARCHAR|LONGVARCHAR|NUMERIC|DECIMAL|BIT|TINYINT|SMALLINT|INTEGER|BIGINT|REAL|FLOAT|DOUBLE|DATE|TIME|TIMESTAMP"/>\*
<result name="string" column="int|string"/>\*
</statement>+
</dblookup>

For in-lined data sources the following parameters have to be specified.

- driver: Fully qualified class name of the database driver.
- url: Database URL.
- user: Username for database access.
- password: Password for database access.

This new data source is based on Apache DBCP connection pools. This connection
pool support the following configuration properties:

- autocommit = true | false
- isolation = Connection.TRANSACTION\_NONE | Connection.TRANSACTION\_READ\_COMMITTED | Connection.TRANSACTION\_READ\_UNCOMMITTED |
  Connection.TRANSACTION\_REPEATABLE\_READ | Connection.TRANSACTION\_SERIALIZABLE
- initialsize = int
- maxactive = int
- maxidle = int
- maxopenstatements = int
- maxwait = long
- minidle = int
- poolstatements = true | false
- testonborrow = true | false
- testonreturn = true | false
- testwhileidle = true | false
- validationquery = String

When an external data source is used the following parameters have to be
specified.

- dsName: The name of the data source to be looked up.
- icClass: Initial context factory class. The corresponding Java environment property is java.naming.factory.initial
- url: The naming service provider URL. The corresponding Java environment property is java.naming.provider.url
- user: Username corresponding to the Java environment property java.naming.security.principal
- password: Password corresponding to the Java environment property java.naming.security.credentials

More than one statement can be included in the mediator configuration. SQL
statement may specify parameters which could be specified as values or XPath
expressions. The type of a parameter could be any valid SQL type. 'result'
sub-element contains 'name' and 'column' attributes which define the name
under which the result is stored in the Synapse message context, and a column
number or name respectively.

<a id="mediators--dbreport"></a>

### DBReport

DB Report mediator is quite similar to the
[DB Lookup](#mediators--dbreport)
mediator, but writes data into a database instead of reading data from a
database.

<dbreport useTransaction=(true|false)>
<connection>
<pool>
(
<driver/>
<url/>
<user/>
<password/>
<property name="name" value="value"/>\*
|
<dsName/>
<icClass/>
<url/>
<user/>
<password/>
)
</pool>
</connection>
<statement>
<sql>INSERT INTO table VALUES (?, ?, ?, ?)</sql>
<parameter [value="" | expression=""] type="CHAR|VARCHAR|LONGVARCHAR|NUMERIC|DECIMAL|BIT|TINYINT|SMALLINT|INTEGER|BIGINT|REAL|FLOAT|DOUBLE|DATE|TIME|TIMESTAMP"/>\*
</statement>+
</dblreport>

This mediator executes the specified SQL INSERT on the database specified
in-line or as an external data source. For information on configuring database
related mediators, refer[DB Lookup mediator guide](#mediators--dbreport).

<a id="mediators--iterate-mediator"></a>

### Iterate Mediator

Iterate mediator splits the message into number of different messages
derived from the parent message by finding matching elements for the XPath
expression specified. New messages will be created for each matching element and
processed in parallel (default behavior) using either the specified sequence or
endpoint.

<iterate [id="string"] [continueParent=(true | false)] [preservePayload=(true | false)] [sequential=(true | false)]
(attachPath="xpath")? expression="xpath">
<target [to="uri"] [soapAction="qname"] [sequence="sequence\_ref"] [endpoint="endpoint\_ref"]>
<sequence>
(mediator)+
</sequence>?
<endpoint>
endpoint
</endpoint>?
</target>+
</iterate>

Created messages can also be set to process sequentially by setting the optional
'sequential' attribute to 'true'. Parent message can be continued or dropped in
the same way as in the clone mediator. The 'preservePayload' attribute specifies
if the original message should be used as a template when creating the split
messages, and defaults to 'false', in which case the split messages would
contain the split elements as the SOAP body. The optional 'id' attribute can be
used to identify the iterator which created a particular split message when
nested iterate mediators are used. This is particularly useful when aggregating
responses of messages that are created using nested iterate mediators.

<a id="mediators--rmsequence"></a>

### RMSequence

RM Sequence mediator can be used to create a sequence of messages to communicate
via WS-Reliable Messaging with a WS-RM enabled endpoint.

<RMSequence (correlation="xpath" [last-message="xpath"]) | single="true" [version="1.0|1.1"]/>

The simplest use case of this mediator sets 'single' attribute to "true", which means that only one message is involved in the same sequence. However, if
multiple messages should be sent in the same sequence, 'correlation' attribute
should be used with an XPath expression that selects a unique element value from
the incoming message. With the result of the XPath expression, Synapse can group
messages together that belong to the same sequence. To close the sequence
neatly, an XPath expression should be specified for the last message of the
sequence as well. The optional 'version' attribute, which specifies the WS-RM
specification version as 1.0 or 1.1, defaults to 1.0.

<a id="mediators--store"></a>

### Store

Store mediator can be used to store the current message in a specific message
store.

<store messageStore="string" [sequence="sequence-ref"]>

In the mediator configuration 'messageStore' attribute is used to specify the
message store to store the message in. The optional 'sequence' attribute
specifies a sequence through which the message is sent before storing it.

<a id="mediators--throttle-mediator"></a>

### Throttle Mediator

Throttle mediator can be used for rate limiting as well as concurrency based
limiting. A WS-Policy dictates the throttling configuration and can be
specified inline or loaded from the registry. Please refer to the samples
document for sample throttling policies.

<throttle [onReject="string"] [onAccept="string"] id="string">
(<policy key="string"/> | <policy>..</policy>)
<onReject>..</onReject>?
<onAccept>..</onAccept>?
</throttle>

The throttle mediator could be used in the request path for rate limiting and
concurrent access limiting. When it's used for concurrent access limitation, the same throttle mediator 'id' must be triggered on the response flow so that
completed responses are deducted from the available limit. (i.e. two instances
of the throttle mediator with the same 'id' attribute in the request and
response flows). 'onReject' and 'onAccept' sequence references or inline
sequences define how accepted and rejected messages are handled.

<a id="mediators--transaction-mediator"></a>

### Transaction Mediator

Transaction mediator can provide transaction facility for a set of mediators
defined as its child mediators. A transaction mediator with the action "new"
indicates the entry point for the transaction. A transaction is marked completed
by a transaction mediator with the action "commit". The suspend and resume
actions are used to pause a transaction at some point and start it again later.
Additionally, the transaction mediator supports three other actions, i.e.
use-existing-or-new, fault-if-no-tx, rollback.

<transaction action="new|use-existing-or-new|fault-if-no-tx|commit|rollback|suspend|resume"/>

- new: Initiate a new transaction.
- use-existing-or-new: If a transaction already exists
  continue it, otherwise create a new transaction.
- fault-if-no-tx: Go to the error handler if no transaction exists.
- commit: End the transaction.
- rollback: Rollback a transaction.
- suspend: Pause a transaction.
- resume: Resume a paused transaction.

---

<a id="transports"></a>

<!-- source_url: https://synapse.apache.org/userguide/transports.html -->

<!-- page_index: 7 -->

<a id="transports--transports-catalog"></a>

## Transports Catalog

The Synapse project has developed a set of transport implementations that provide
protocol support and/or features that go beyond what is provided out of the box by
Axis2:

- A non-blocking HTTP transport that gives better performance in a highly
  asynchronous environment like Synapse.
- A VFS transport that can read messages from files and write outgoing messages to
  a file system. The file system can be local or remote, and several remote
  protocols are supported, such as FTP, SSH, WebDAV, etc.
- A transport supporting the
  [Financial Information eXchange](http://www.fixprotocol.org)
  protocol. FIX is a public-domain messaging standard developed specifically for
  the real-time electronic exchange of securities transactions. It has a large user
  base and is developed by the collaborative effort of banks, broker-dealers,
  exchanges, industry utilities and associations, institutional investors, and IT
  providers around the world.
- A AMQP transport which support the AMQP protocol.
  [AMQP](http://www.amqp.org/) is a messaging
  protocol.

Note that while these transports are developed as part of the Synapse project, they can be used with any Axis2 based application.

The Synapse distribution also comes bundled with the following transports from
the [Axis2 Transport](http://axis.apache.org/axis2/java/transports/index.html)
project:

- A
  [JMS transport](http://axis.apache.org/axis2/java/transports/jms.html)
  supporting any JMS 1.0 or 1.1 provider.
- A
  [Mail transport](http://axis.apache.org/axis2/java/transports/mail.html)
  able to send messages using SMTP and poll messages from a POP3 or IMAP account.

  Apache Synapse is also compatible with the following transport implementations
  from the Apache Axis2 Transports project:
- [TCP transport](http://axis.apache.org/axis2/java/transports/tcp-transport.html)
- [SMS transport](http://axis.apache.org/axis2/java/transports/sms.html)
- UDP transport
- XMPP transport

  These transports are not shipped with Apache Synapse by default and hence they
  should be
  [downloaded separately](http://axis.apache.org/axis2/java/transports/download.cgi)
  from the Axis2 transport website and installed in the Synapse runtime.

<a id="transports--content"></a>

## Content

- [Introduction](#transports--introduction)
- [Contents](#transports--contents)
- [Passthrough HTTP transport](#transports--passthrough_http_transport)
  - [Example configurations](#transports--example_configurations)
  - [Transport listener parameters](#transports--transport_listener_parameters)
  - [Transport sender parameters](#transports--transport_sender_parameters)
- [Non-blocking HTTP(NHTTP) transport](#transports--non-blocking_httpnhttp_transport)
  - [Example configurations](#transports--example_configurations)
  - [Transport listener parameters](#transports--transport_listener_parameters)
  - [Transport sender parameters](#transports--transport_sender_parameters)
- [VFS transport](#transports--vfs_transport)
  - [Transport listener](#transports--transport_listener)
  - [Transport sender](#transports--transport_sender)
  - [Using SFTP](#transports--using_sftp)
  - [Known issues](#transports--known_issues)
- [FIX transport](#transports--fix_transport)
  - [Setting up the FIX Transport](#transports--setting_up_the_fix_transport)
  - [FIX Transport Parameters](#transports--fix_transport_parameters)
- [AMQP transport](#transports--amqp_transport)
  - [Setting up the AMQP Transport](#transports--setting_up_the_amqp_transport)
  - [AMQP Transport Parameters](#transports--amqp_transport_parameters)
  - [Sample Configurations](#transports--amqp_transport_ex)

<a id="transports--passthrough-http-transport"></a>

## Passthrough HTTP transport

<a id="transports--example-configuration"></a>

### Example configuration

<transportReceiver name="http" class="org.apache.synapse.transport.passthru.PassThroughHttpListener">
<parameter name="port">8280</parameter>
<parameter name="httpGetProcessor"locked="org.apache.synapse.transport.passthru.api.PassThroughNHttpGetProcessor">true</parameter>
</transportReceiver>
<transportReceiver name="https" class="org.apache.synapse.transport.passthru.PassThroughHttpSSLListener">
<parameter name="port" locked="false">8243</parameter>
<parameter name="httpGetProcessor"locked="org.apache.synapse.transport.passthru.api.PassThroughNHttpGetProcessor">true</parameter>
<parameter name="keystore" locked="false">
<KeyStore>
<Location>lib/identity.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
<KeyPassword>password</KeyPassword>
</KeyStore>
</parameter>
<parameter name="truststore" locked="false">
<TrustStore>
<Location>lib/trust.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
</TrustStore>
</parameter>
</transportReceiver>
<transportSender name="http" class="org.apache.synapse.transport.passthru.PassThroughHttpSender">
</transportSender>
<transportSender name="https" class="org.apache.synapse.transport.passthru.PassThroughHttpSSLSender">
<parameter name="keystore" locked="false">
<KeyStore>
<Location>lib/identity.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
<KeyPassword>password</KeyPassword>
</KeyStore>
</parameter>
<parameter name="truststore" locked="false">
<TrustStore>
<Location>lib/trust.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
</TrustStore>
</parameter>
<parameter name="CertificateRevocationVerifier">
<CacheSize>50</CacheSize>
<CacheDurationMins>5</CacheDurationMins>
</parameter>
</transportSender>

<a id="transports--transport-listener-parameters"></a>

### Transport listener parameters

The following parameters are supported by both the HTTP and the HTTPS listener:

port
:   The TCP port to bind the listener to.

bind-address
:   The IP address to bind the listener to. This can be used on hosts that have
    more than one network interface or IP address to run multiple Synapse instances
    listening to the same port. If this parameter is not specified, the
    listener will accept connections on any IP address.

hostname
:   The host name to use when computing endpoint references in generated WSDL files.
    The default value is the host name as provided by the operation system or
    localhost if the host name can't be determined. The value of this
    parameter is ignored if WSDLEPRPrefix is specified.

WSDLEPRPrefix
:   The URL prefix to use when computing endpoint references in generated WSDL files.
    The value must be a valid URL with at least a protocol and host. If this value
    is unspecified, endpoint references will be computed based on the listener type
    (HTTP or HTTPS) and hostname and port parameters.

    This parameter should be used if clients connect to Synapse through a frontend
    server, e.g. a (load balancing) Apache, and these clients rely on the address
    information in the WSDL documents exposed through ...?wsdl URLs.

The following parameters are specific to the HTTPS listener:

keystore
:   The keystore configuration. The value of this parameter must be a
    <KeyStore>
    element as shown in the example configurations above.

truststore
:   The truststore configuration. The value of this parameter must be a
    <TrustStore>
    element as shown in the example configurations above.

SSLVerifyClient
:   This parameter has the same meaning as the corresponding
    [mod\_ssl directive](http://httpd.apache.org/docs/2.2/mod/mod_ssl.html#sslverifyclient)
    and sets the desired certificate verification level for client authentication:

    - none (default): no client certificate is required at all
    - optional: the client may present a valid certificate, but is
      not required to do so
    - require: the client has to present a valid certificate,
      otherwise the connection request will be terminated during SSL handshake

<a id="transports--transport-sender-parameters"></a>

### Transport sender parameters

The following property can be used to control based on content-types whether the
HTTP/HTTPS sender shall output a warning for responses with HTTP status code 500.

warnOnHTTP500
:   A list of content-types for which Synapse shall output a warning when receiving
    an HTTP 500 response (each value each separated by a |). By default, Synapse
    outputs a warning for any HTTP 500 response, irrespective of the content-type.
    Consequently, also for each SOAP fault a warning will be logged. If only for
    specific content-types a warning shall be logged, please provide a |-separated
    list. To output the warning for messages which do not have a content-type set,
    please use the value 'none'.

    Example value: x-application/hessian|none

The following properties can be used to configure the HTTP sender to use a proxy.
They can be specified either as transport parameters in declared in
<transportSender> or as system properties.

http.proxyHost
:   The host name or address of the proxy server.

http.proxyPort
:   The TCP port of the proxy server.

http.nonProxyHosts
:   The hosts to which the HTTP sender should connect directly and not through
    the proxy server. The value can be a list of hosts, each separated by a |, and
    in addition a wildcard character (\*) can be used for matching.

    Example value:
    \*.foo.com|localhost

Note that the HTTPS sender has no proxy support yet.

The following parameters are specific to the HTTPS sender:

keystore
:   The keystore configuration. The value of this parameter must be a
    <KeyStore> element as shown in the example configurations
    above.

truststore
:   The truststore configuration. The value of this parameter must be a
    <TrustStore>
    element as shown in the example configurations above.

novalidatecert
:   When set to true, this parameter disables server certificate
    validation (trust). The default value is false. This parameter will
    be ignored if truststore is set.

    Setting his parameter to true
    is useful in development and test environments, but should not be used in
    production environments. If validation is disabled, a warning message will
    be logged at startup.

HostnameVerifier
:   This optional parameter specifies the policy to apply when checking that the
    hostname of the server matches the names stored inside the X.509 certificate
    presented by the server. Possible values are Strict, AllowAll
    and DefaultAndLocalhost. See the
    [HostnameVerifier Javadoc](https://synapse.apache.org/apidocs/org/apache/synapse/transport/nhttp/HostnameVerifier.html)
    for more details.

CertificateRevocationVerifier
:   This is an optional parameter to validate the revocation status of the host
    certificates using [OCSP](http://www.ietf.org/rfc/rfc2560.txt) and
    [CRL](http://www.ietf.org/rfc/rfc5280.txt) when making HTTPS connections.
    Simply uncomment this parameter in the axis2.xml file to enable the feature.
    Two LRU caches are used to cache CRLs and OCSP responses until they are expired. "CacheSize"
    property defines the maximum size of a cache. When this limit is reached, the
    old values will be automatically removed and updated with new values. "CacheDurationMins"
    is used to configure the time duration (in minutes) between two consecutive
    runs of the CacheManager task which periodically performs housekeeping work
    in each cache. Refer the example configuration above to see how to configure
    these properties. The scheduled CacheManager tasks for OCSP and CRL caches can
    be manually controlled using the JMX MBeans registered under the "CacheController"
    category.

<a id="transports--non-blocking-http-nhttp-transport"></a>

## Non-blocking HTTP (NHTTP) transport

<a id="transports--example-configuration-2"></a>

### Example configuration

<transportReceiver name="http" class="org.apache.synapse.transport.nhttp.HttpCoreNIOListener">
<parameter name="port">8280</parameter>
<parameter name="non-blocking">true</parameter>
</transportReceiver>
<transportReceiver name="https" class="org.apache.synapse.transport.nhttp.HttpCoreNIOSSLListener">
<parameter name="port" locked="false">8243</parameter>
<parameter name="non-blocking" locked="false">true</parameter>
<parameter name="keystore" locked="false">
<KeyStore>
<Location>lib/identity.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
<KeyPassword>password</KeyPassword>
</KeyStore>
</parameter>
<parameter name="truststore" locked="false">
<TrustStore>
<Location>lib/trust.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
</TrustStore>
</parameter>
</transportReceiver>
<transportSender name="http" class="org.apache.synapse.transport.nhttp.HttpCoreNIOSender">
<parameter name="non-blocking" locked="false">true</parameter>
<parameter name="warnOnHTTP500" locked="false">\*</parameter>
</transportSender>
<transportSender name="https" class="org.apache.synapse.transport.nhttp.HttpCoreNIOSSLSender">
<parameter name="non-blocking" locked="false">true</parameter>
<parameter name="warnOnHTTP500" locked="false">\*</parameter>
<parameter name="keystore" locked="false">
<KeyStore>
<Location>lib/identity.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
<KeyPassword>password</KeyPassword>
</KeyStore>
</parameter>
<parameter name="truststore" locked="false">
<TrustStore>
<Location>lib/trust.jks</Location>
<Type>JKS</Type>
<Password>password</Password>
</TrustStore>
</parameter>
<parameter name="CertificateRevocationVerifier">
<CacheSize>50</CacheSize>
<CacheDurationMins>5</CacheDurationMins>
</parameter>
</transportSender>

<a id="transports--transport-listener-parameters-2"></a>

### Transport listener parameters

The following parameters are supported by both the HTTP and the HTTPS listener:

port
:   The TCP port to bind the listener to.

bind-address
:   The IP address to bind the listener to. This can be used on hosts that have
    more than one network interface or IP address to run multiple Synapse instances
    listening to the same port. If this parameter is not specified, the
    listener will accept connections on any IP address.

hostname
:   The host name to use when computing endpoint references in generated WSDL files.
    The default value is the host name as provided by the operation system or
    localhost if the host name can't be determined. The value of this
    parameter is ignored if WSDLEPRPrefix is specified.

WSDLEPRPrefix
:   The URL prefix to use when computing endpoint references in generated WSDL files.
    The value must be a valid URL with at least a protocol and host. If this value
    is unspecified, endpoint references will be computed based on the listener type
    (HTTP or HTTPS) and hostname and port parameters.

    This parameter should be used if clients connect to Synapse through a frontend
    server, e.g. a (load balancing) Apache, and these clients rely on the address
    information in the WSDL documents exposed through ...?wsdl URLs.

The following parameters are specific to the HTTPS listener:

keystore
:   The keystore configuration. The value of this parameter must be a
    <KeyStore>
    element as shown in the example configurations above.

truststore
:   The truststore configuration. The value of this parameter must be a
    <TrustStore>
    element as shown in the example configurations above.

SSLVerifyClient
:   This parameter has the same meaning as the corresponding
    [mod\_ssl directive](http://httpd.apache.org/docs/2.2/mod/mod_ssl.html#sslverifyclient)
    and sets the desired certificate verification level for client authentication:

    - none (default): no client certificate is required at all
    - optional: the client may present a valid certificate, but is
      not required to do so
    - require: the client has to present a valid certificate,
      otherwise the connection request will be terminated during SSL handshake

<a id="transports--transport-sender-parameters-2"></a>

### Transport sender parameters

The following property can be used to control based on content-types whether the
HTTP/HTTPS sender shall output a warning for responses with HTTP status code 500.

warnOnHTTP500
:   A list of content-types for which Synapse shall output a warning when receiving
    an HTTP 500 response (each value each separated by a |). By default, Synapse
    outputs a warning for any HTTP 500 response, irrespective of the content-type.
    Consequently, also for each SOAP fault a warning will be logged. If only for
    specific content-types a warning shall be logged, please provide a |-separated
    list. To output the warning for messages which do not have a content-type set,
    please use the value 'none'.

    Example value: x-application/hessian|none

The following properties can be used to configure the HTTP sender to use a proxy.
They can be specified either as transport parameters in declared in
<transportSender> or as system properties.

http.proxyHost
:   The host name or address of the proxy server.

http.proxyPort
:   The TCP port of the proxy server.

http.nonProxyHosts
:   The hosts to which the HTTP sender should connect directly and not through
    the proxy server. The value can be a list of hosts, each separated by a |, and
    in addition a wildcard character (\*) can be used for matching.

    Example value:
    \*.foo.com|localhost

Note that the HTTPS sender has no proxy support yet.

The following parameters are specific to the HTTPS sender:

keystore
:   The keystore configuration. The value of this parameter must be a
    <KeyStore> element as shown in the example configurations
    above.

truststore
:   The truststore configuration. The value of this parameter must be a
    <TrustStore>
    element as shown in the example configurations above.

novalidatecert
:   When set to true, this parameter disables server certificate
    validation (trust). The default value is false. This parameter will
    be ignored if truststore is set.

    Setting his parameter to true
    is useful in development and test environments, but should not be used in
    production environments. If validation is disabled, a warning message will
    be logged at startup.

HostnameVerifier
:   This optional parameter specifies the policy to apply when checking that the
    hostname of the server matches the names stored inside the X.509 certificate
    presented by the server. Possible values are Strict, AllowAll
    and DefaultAndLocalhost. See the
    [HostnameVerifier Javadoc](https://synapse.apache.org/apidocs/org/apache/synapse/transport/nhttp/HostnameVerifier.html)
    for more details.

CertificateRevocationVerifier
:   This is an optional parameter to validate the revocation status of the host
    certificates using [OCSP](http://www.ietf.org/rfc/rfc2560.txt) and
    [CRL](http://www.ietf.org/rfc/rfc5280.txt) when making HTTPS connections.
    Simply uncomment this parameter in the axis2.xml file to enable the feature.
    Two LRU caches are used to cache CRLs and OCSP responses until they are expired. "CacheSize"
    property defines the maximum size of a cache. When this limit is reached, the
    old values will be automatically removed and updated with new values. "CacheDurationMins"
    is used to configure the time duration (in minutes) between two consecutive
    runs of the CacheManager task which periodically performs housekeeping work
    in each cache. Refer the example configuration above to see how to configure
    these properties. The scheduled CacheManager tasks for OCSP and CRL caches can
    be manually controlled using the JMX MBeans registered under the "CacheController"
    category.

<a id="transports--vfs-transport"></a>

## VFS transport

<a id="transports--transport-listener"></a>

### Transport listener

The VFS transport listener receives messages dropped in a given local or remote file
system location. The location is specified by a URL that either identifies a single
file or a directory. The transport listener will periodically poll the specified
location and process any file(s) found. After a file has been processed it will be
deleted or moved to another location. Note that this is absolutely mandatory to
prevent the listener from processing files multiple times. Therefore, the VFS transport
listener can only be used in situations where it has write access to the file system
location and where deleting or moving the dropped files is acceptable.

The transport is based on
[Apache Commons VFS](http://commons.apache.org/vfs/)
and supports any protocol for which a VFS provider is available. The transport is
pre-configured with providers for local files (
file:
scheme), HTTP, HTTPS, FTP and SFTP (i.e. file transfer over SSH).

There is a fundamental difference between the VFS transport and transports such as
HTTP and it is important to understand this difference to be able to use the VFS
transport correctly. The HTTP transport binds to a single protocol endpoint, i.e.
a TCP port on which it accepts incoming HTTP requests. These requests are then
dispatched to the right service based on the request URI. On the other hand, the
VFS transport only receives the payload of a message, but no additional information
that could be used to dispatch the message to a service. This means that file system
locations must be explicitly mapped to services. This is done using a set of service
parameters.

For Synapse this means that the VFS transport listener can only be used in
conjunction with proxy services. The relevant service parameters are then specified
as follows:

<proxy name="MyVFSService" transports="vfs">
<parameter name="transport.vfs.FileURI">file:///var/spool/synapse/in</parameter>
<parameter name="transport.vfs.ContentType">application/xml</parameter>
...
<target>
...
</target>
</proxy>

In this example the file system location
file:///var/spool/synapse/in
is explicitly bound to
MyVFSService
, i.e. any message dropped in that location will be predispatched to that service, bypassing any other configured
dispatch mechanisms that would apply to messages received through HTTP.

The VFS transport recognizes the following service parameters:

transport.vfs.FileURI(Required)
:   The primary File (or Directory) URI in the vfs\* transport format, for this
    service

transport.vfs.ContentType (Required)
:   The expected content type for files retrieved for this service. The VFS
    transport uses this information to select the appropriate message builder.

    Examples:

    - text/xml for plain XML or SOAP
    - text/plain; charset=ISO-8859-1 for text files
    - application/octet-stream for binary data

transport.vfs.FileNamePattern (Optional)
:   A file name regex pattern to match files against a directory specified by
    the FileURI

transport.PollInterval (Optional)
:   The poll interval (in seconds)

transport.vfs.ActionAfterProcess (Optional)
:   DELETE or MOVE

transport.vfs.MoveAfterProcess (Optional)
:   The directory to move files after processing (i.e. all files process
    successfully)

transport.vfs.ActionAfterErrors (Optional)
:   DELETE or MOVE

transport.vfs.MoveAfterErrors (Optional)
:   The directory to move files after errors (i.e. some of the files succeed
    but some fail)

transport.vfs.ActionAfterFailure (Optional)
:   DELETE or MOVE

transport.vfs.MoveAfterFailure (Optional)
:   The directory to move after failure (i.e. all files fail)

transport.vfs.ReplyFileURI (Optional)
:   Reply file URI

transport.vfs.ReplyFileName (Optional)
:   Reply file name (defaults to response.xml)

transport.vfs.MoveTimestampFormat (Optional)
:   Timestamp prefix format for processed file name. java.text.SimpleDateFormat
    compatible string. e.g. yyMMddHHmmss'-'

transport.vfs.Locking (Optional)
:   By-default file locking is turned on in the VFS transport, and this parameter
    lets you configure the locking behaviour on a per service basis. Possible values are
    enable or disable, and both these values are important because
    the locking can be disabled at the global level by specifying that at the
    receiver level and selectively enable locking only for a set of services.

transport.vfs.Streaming (Optional)
:   If this parameter is set to true, the transport will attempt to use a
    javax.activation.DataSource (instead of a java.io.InputStream
    ) object to pass the content of the file to the message builder. Note that this
    is only supported by some message builders, e.g. for plain text and binary.

    This allows processing of the message without storing the entire content
    in memory. It also has two other side effects:

    - The incoming file (or connection in case of a remote file) will only
      be opened on demand.
    - Since the data is not cached, the file might be read several times.

    This option can be used to achieve streaming of large payloads. Note that
    this feature is still somewhat experimental and might be superseded by a
    more flexible mechanism in a future release.

Note that since the VFS endpoints are configured at the level of the service, the
only parameter that is available at the listener is the file locking configuration
parameter which is optional and the transport listener is enabled in
axis2.xml
simply as follows:

<transportReceiver name="vfs" class="org.apache.synapse.transport.vfs.VFSTransportListener">
<parameter name="transport.vfs.Locking">enable | disable</parameter> ?
</transportReceiver>

<a id="transports--transport-sender"></a>

### Transport sender

The VFS transport sender allows to write outgoing messages to local or remote files.
As with the listener, the transport sender supports any protocol for which there
is a VFS provider.

The sender is enabled be the following directive in
axis2.xml file locking which is by-default enabled can be configured
using the transport.vfs.Locking parameter:

<transportSender name="vfs" class="org.apache.synapse.transport.vfs.VFSTransportSender">
<parameter name="transport.vfs.Locking">enable | disable</parameter> ?
</transportSender>

To send a message using the VFS transport, the destination URI must start with
vfs: followed by a valid VFS URL. For example, in a Synapse mediation, one would use:

<endpoint>
<address uri="vfs:file:///var/spool/synapse/out"/>
</endpoint>

Other examples of valid VFS URLs are (see
<http://commons.apache.org/vfs/filesystems.html>
for more samples):

- file:///directory/filename.ext
- file:////somehost/someshare/afile.txt
- jar:../lib/classes.jar!/META-INF/manifest.mf
- jar:zip:outer.zip!/nested.jar!/somedir
- ftp://myusername:mypassword@somehost/pub/downloads/somefile.tgz[?vfs.passive=true]

The global configuration of the file locking can be overriden by providing the
transport.vfs.Locking as a URL parameter with the appropriate value (
enable, or disable) on a given endpoint.

It should be noted that by its nature, the VFS transport sender doesn't support
synchronous responses and should only be invoked using the out-only message
exchange pattern. In a Synapse mediation, this can be forced using the
following mediator:

<property action="set" name="OUT\_ONLY" value="true"/>

<a id="transports--using-sftp"></a>

### Using SFTP

To avoid man-in-the-middle attacks, SSH clients will only connect to hosts with
a known host key. When connecting for the first time to an SSH server, a typical
command line SSH client would request confirmation from the user to add the
server and its fingerprint to the list of known hosts.

The VFS transports supports SFTP through the
[JSch](http://www.jcraft.com/jsch/)
library and this library also requires a list of known hosts. Since Synapse is
not an interactive process, it can't request confirmation from the user and is
therefore unable to automatically add a host to the list. This implies that the
list of known hosts must be set up manually before the transport can connect.

Jsch loads the list of known hosts from a file called known\_hosts in
the .ssh sub-directory of the user's home directory, i.e. $HOME/.ssh
in Unix and %HOMEPATH%\.ssh in Windows. The location and format of this
file are compatible with the [OpenSSH](http://www.openssh.com/)
client.

Since the file not only contains a list of host names but also the fingerprints
of their host keys, the easiest way to add a new host to that file is to simply
use the OpenSSH client to open an SSH session on the target host. The client will
then ask to add the credentials to the known\_hosts file. Note that if
the SSH server is configured to only allow SFTP sessions, but no interactive
sessions, the connection will actually fail. Since this doesn't rollback the
change to the known\_hosts file, this error can be ignored.

<a id="transports--known-issues"></a>

### Known issues

The VFS listener will start reading a file as soon as it appears in the configured
location. To avoid processing half written files, the creation of these files should
be made atomic. On most platforms, this can be achieved by writing the data to a
temporary file and then moving the file to the target location. Note however that
a move operation is only atomic if the source and destination are on the same
physical file system. The location for the temporary file should be chosen with
that constraint in mind.

It should also be noted that the VFS transport sender doesn't create files atomically.

<a id="transports--fix-transport"></a>

## FIX transport

A general overview about the FIX transport can be found in the following articles:

- [Apache Synapse FIX'ed](http://wso2.org/library/3449)
- [Using the WSO2 ESB and FIX](http://wso2.org/library/3837)
  (also applies to Synapse)

<a id="transports--setting-up-the-fix-transport"></a>

### Setting up the FIX Transport

To use the FIX transport, you need a local
[Quickfix/J](http://www.quickfixj.org)
installation. Download Quickfix/J from
<http://www.quickfixj.org/downloads>
.

To enable the FIX transport, you need to uncomment the FIX transport sender and
FIX transport receiver configurations in the SYNAPSE\_HOME/repository/conf/axis2.xml.
Simply locate and uncomment the FIXTransportSender and FIXTransportListener sample
configurations. Also, add the following jars to the Synapse class path
(SYNAPSE\_HOME/lib directory).

- quickfixj-core.jar
- quickfixj-msg-fix40.jar
- quickfixj-msg-fix41.jar
- quickfixj-msg-fix42.jar
- quickfixj-msg-fix43.jar
- quickfixj-msg-fix44.jar
- mina-core.jar
- slf4j-api.jar
- slf4j-jdk14.jar

All these jars are shipped with the Quickfix/J binary distribution.

<a id="transports--fix-transport-parameters"></a>

### FIX Transport Parameters

This is the list of all parameters accepted by the FIX transport. Refer the
sample 257 and 258 to see how some of them are used in practice.

transport.fix.AcceptorConfigURL
:   If a service needs to listen to incoming FIX messages from a remote initiator,
    then Synapse needs to create an acceptor. This parameter should contain the
    URL of the file which contains the FIX configuration for the acceptor.
    (See sample 257)

transport.fix.InitiatorConfigURL
:   If a service needs to send FIX messages to a remote acceptor Synapse should
    create an initiator. This parameter should contain the URL of the file which
    contains the FIX configuration for the initiator. (See sample 257)

transport.fix.AcceptorMessageStore
:   The type of message store to be used with the acceptor. Allowed values for
    this parameter are 'file', 'jdbc', 'memory' and 'sleepycat'. If not specified
    memory based message store will be used by default. Additional parameters
    required to configure each of the message stores should be specified in the
    acceptor configuration file.

transport.fix.InitiatorMessageStore
:   Same as the above but applies only for the initiators. Additional parameters
    required to configure each of the message stores should be specified in the
    initiator configuration file.

transport.fix.AcceptorLogFactory
:   Specifies the transport level log factory to be used to log messages going
    through the acceptor. FIX messages are logged without putting them in SOAP
    envelopes at this level. Accepted values are 'console', 'file' and 'jdbc'.
    If not specified no logging will be done at the transport level. Additional
    parameters required to configure each of the lof factories should be specified
    in the acceptor configuration file.

transport.fix.InitiatorLogFactory
:   Specifies the transport level log factory to be used to log messages going
    through the initiator. Functionality is similar to the above. Additional
    parameters required to configure each of the lof factories should be specified
    in the initiator configuration file.

transport.fix.ResponseDeliverToCompID
:   If a response FIX message sent from Synapse to a remote FIX engine should be
    forwarded from the remote engine to another party, this parameter can be used
    to set the DeliverToCompID field of the messages at Synapse.

transport.fix.ResponseDeliverToSubID
:   If a response FIX message sent from Synapse to a remote FIX engine should be
    forwarded from the remote engine to another party, this parameter can be used
    to set the DeliverToSubID field of the messages at Synapse.

transport.fix.ResponseDeliverToLocationID
:   If a response FIX message sent from Synapse to a remote FIX engine should be
    forwarded from the remote engine to another party, this parameter can be used
    to set the DeliverToLocationID field of the messages at Synapse.

transport.fix.ServiceName
:   Used when messages coming over a different protocol has to be forwarded over
    FIX. The value must be equal to the name of the service and the scope must be
    'axis2-client' (See sample 258)

transport.fix.SendAllToInSequence
:   When there are multiple responses to a FIX request and when we need only one
    of them to be sent to the original requester this parameter has to be set to
    'false'. This mostly comes handy when the original requester is communicating
    over a different protocol (like HTTP). If this parameter is not set to 'false'
    at such scenarios messages might get into a loop. (See sample 258)

transport.fix.BeginStringValidation
:   When the FIX messages sent to Synapse should not be forwarded to a FIX session
    with a different BeginString value this parameter can be set to 'true'. Setting
    this parameter to 'true' will enforce this restriction.

<a id="transports--amqp-transport"></a>

## AMQP transport

<a id="transports--setting-up-the-transport"></a>

### Setting Up the Transport

AMQP transport is based on the widely used
[Java AMQP client](http://www.rabbitmq.com/java-client.html) library from
[RabbitMQ](http://www.rabbitmq.com/).
The client library is not distributed with Apache Synapse, and hence in order to use
the AMQP transport, download the RabbitMQ Java client and copy the client library
(rabbitmq-client.jar) into Synapse classpath (SYNAPSE\_HOME/lib directory).

To enable the AMQP transport, uncomment the AMQP transport sender and AMQP transport
receiver configurations in the SYNAPSE\_HOME/repository/conf/axis2.xml.

<a id="transports--amqp-transport-parameters"></a>

### AMQP Transport Parameters

Following parameters can be configured as part of AMQP transport receiver, sender, a proxy service or an AMQP endpoint declaration.

transport.amqp.Uri
:   The connection URL for the broker of the form
    amqp://userName:password@hostName:portNumber/virtualHost

transport.amqp.BrokerList
:   The list of broker of the form, host1:port1,host2:port2... which will be used
    as the address array in AMQP connection to the broker

transport.amqp.ExchangeName
:   The name of the exchange to connect

transport.amqp.IsExchangeDurable
:   Should the exchange be declared as durable?

transport.amqp.IsExchangeAutoDelete
:   Should the exchange be auto delete? Possible values are true or false

transport.amqp.ChannelPreFetchSize
:   The channel pre fetch size for fair dispatch

transport.amqp.ChannelPreFetchCountSize
:   The channel prefetch count for fair dispatch

transport.amqp.ExchangeType
:   Type of the exchange to use. Possible values are, fanout, direct, header or topic

transport.amqp.ExchangeInternal
:   Should the exchange be declared as internal? Possible values are true or false

transport.amqp.BindExchange
:   The name of the exchange that the publisher/consumer should publish/consume message to.

transport.amqp.BindingKeys
:   The comma separated binding keys this queue should be bound into exchange

transport.amqp.RoutingKey
:   The routing key to be used by the publisher.

transport.amqp.ConsumerTx
:   Use transactions at consumer side if set to true. By default, this will be
    considered false and explicit acknowledgement will be done

transport.amqp.QueueName
:   The name of the queue

transport.amqp.IsQueueDurable
:   Should the queue declare as durable? Possible values are true or false.

transport.amqp.IsQueueRestricted
:   Should the queue declare as restricted? Possible values are true or false.

transport.amqp.IsQueueAutoDelete
:   Should the queue declare as auto delete when it's no longer in use?.
    Possible values are true or false.

transport.amqp.OperateOnBlockingMode
:   True if the polling task should wait until it process the accepted
    messages. This can be used in conjunction with a single thread polling
    task (in the whole transport, i.e. only a single AMQP proxy per flow)
    to achieve in order delivery

transport.amqp.ConnectionFactoryName
:   The connection factory to be used either with consumer or producer.

transport.amqp.ResponseConnectionFactoryName
:   In a two-way scenario, which connection factory of the senders' should be used
    to send the response

transport.amqp.ScheduledTaskInitialDelay
:   The initial delay (in milliseconds) that the polling task should delay before initial attempt

transport.amqp.ScheduledTaskDelay
:   The delay (in milliseconds) that the polling task should delay before next attempt.

transport.amqp.ScheduledTaskTimeUnit
:   The time unit which should use to calculate,
    transport.amqp.ScheduledTaskInitialDelay and transport.amqp.ScheduledTaskDelay.

transport.amqp.NoOfConcurrentConsumers
:   Number of concurrent consumers per polling task.

transport.amqp.NoOfDispatchingTask
:   Number of dispatching task to use any request messages to actual processing task.

transport.amqp.ContentType
:   Configure the content type as a service parameter.

AMQP\_CONTENT\_TYPE
:   Message context property to set the AMQP message content type.

AMQP\_CONTENT\_ENCODING
:   Message context property to set the AMQP message encoding

AMQP\_HEADER\_\*
:   Specify any AMQP headers as message context properties using AMQP\_HEADER\_\*

AMQP\_DELIVERY\_MODE
:   Message context property to set the AMQP message delivery mode

AMQP\_PRIORITY
:   Message context property to set the AMQP message priority.

AMQP\_CORRELATION\_ID
:   Message context property to set the AMQP message correlation id

AMQP\_REPLY\_TO
:   Message context property to set the AMQP message reply to header.

AMQP\_EXPIRATION
:   Message context property to set the AMQP expiration.

AMQP\_MESSAGE\_ID
:   Message context property to set the message id of the AMQP message

AMQP\_TIME\_STAMP
:   Message context property to set the timestamp of the AMQP message.

AMQP\_TYPE
:   Message context property to set the type of the AMQP message

AMQP\_PRODUCER\_TX
:   Use transactions at producer side. Possible values are tx(for blocking transactions),
    lwpc(for light weight producer connections).

connection-factory-pool-size
:   A system property to set the worker pool size of the connection factory executor service.

worker-pool-size
:   A system property to set the worker pool size used by deployed services for polling broker.

semaphore-time-out
:   A system property to set the timeout (in seconds) of semaphore which waits for
    a response.

initial-reconnect-duration
:   If a polling task encounter an exception due to some reason(most probably
    due to broker outage) it will be suspended until a successful re-connect.
    This system property defines the initial duration that the re-connection
    check task should be suspended (1000 ms by default) before next re-try.

reconnection-progression-factor
:   A system property to define the factor (2.0 by default) to multiply the initial
    suspended duration to calculate the next suspending duration for the
    re-connection check task.

maximum-reconnection-duration
:   The maximum duration that re-connection check task should be suspended(
    10 minutes by default). After this time is reached, the suspended duration
    will be fall back to its original initial configured duration.

<a id="transports--sample-configurations"></a>

### Sample Configurations

Producer example

<proxy name="ProducerProxy" transports="http">
<target>
<inSequence>
<property action="set" name="OUT\_ONLY" value="true"/>
<property name="PRESERVE\_WS\_ADDRESSING" value="true"/>"
<log level="custom">
<property name="status" value="At ProducerProxy"/>
</log>
</inSequence>
<endpoint>
<!--use the defined connection factory in AMQP transport sender-->
<address
uri="amqp://SimpleStockQuoteService?transport.amqp.ConnectionFactoryName=producer&transport.amqp.QueueName=ProducerProxy"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
</proxy>

Consumer example

<proxy name="ConsumerProxy" transports="amqp">
<target>
<inSequence>
<property action="set" name="OUT\_ONLY" value="true"/>
<log level="custom">
<property name="status" value="At ConsumerProxy"/>
</log>
</inSequence>
<endpoint>
<address uri="http://localhost:9000/services/SimpleStockQuoteService"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
<parameter name="transport.amqp.ConnectionFactoryName">consumer</parameter>
<parameter name="transport.amqp.QueueName">ProducerProxy</parameter>
</proxy>

Routing example

<proxy name="DirectPublisherProxy" transports="http">
<target>
<inSequence>
<property action="set" name="OUT\_ONLY" value="true"/>
<log level="custom">
<property name="status" value="At DirectPublisherProxy"/>
</log>
</inSequence>
<endpoint>
<!--use the defined connection factory in AMQP transport sender, note how we don't provide
any queue name because this is bind to the exchange-->
<address
uri="amqp://?transport.amqp.ConnectionFactoryName=publisher&transport.amqp.ExchangeName=direct\_logs&transport.amqp.ExchangeType=direct&transport.amqp.RoutingKey=error"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
</proxy>
<proxy name="DirectSubscriberProxy1" transports="amqp">
<target>
<inSequence>
<property action="set" name="OUT\_ONLY" value="true"/>
<log level="custom">
<property name="status" value="At DirectSubscriberProxy 1"/>
</log>
</inSequence>
<endpoint>
<address uri="http://localhost:9000/services/SimpleStockQuoteService"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
<parameter name="transport.amqp.ConnectionFactoryName">subscriber</parameter>
<parameter name="transport.amqp.ExchangeName">direct\_logs</parameter>
<parameter name="transport.amqp.ExchangeType">direct</parameter>
<parameter name="transport.amqp.BindingKeys">warning,error</parameter>
</proxy>
<proxy name="DirectSubscriberProxy2" transports="amqp">
<target>
<inSequence>
<property action="set" name="OUT\_ONLY" value="true"/>
<log level="custom">
<property name="status" value="At DirectSubscriberProxy 2"/>
</log>
</inSequence>
<endpoint>
<address uri="http://localhost:9000/services/SimpleStockQuoteService"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
<parameter name="transport.amqp.ConnectionFactoryName">subscriber</parameter>
<parameter name="transport.amqp.ExchangeName">direct\_logs</parameter>
<parameter name="transport.amqp.ExchangeType">direct</parameter>
<parameter name="transport.amqp.BindingKeys">error</parameter>
</proxy>

Producer transactions

<proxy name="ProducerTxProxy1" transports="http">
<target>
<inSequence>
<property action="set" name="OUT\_ONLY" value="true"/>
<property action="set" name="AMQP\_PRODUCER\_TX" scope="axis2" value="lwpc"/>
<log level="custom">
<property name="status" value="At ProducerTxProxy1, use light weight producer confirm..."/>
</log>
</inSequence>
<endpoint>
<!--use the defined connection factory in AMQP transport sender-->
<address
uri="amqp://SimpleStockQuoteService?transport.amqp.ConnectionFactoryName=producer&transport.amqp.QueueName=ProducerProxy"/>
</endpoint>
<outSequence>
<send/>
</outSequence>
</target>
</proxy>

---

<a id="properties"></a>

<!-- source_url: https://synapse.apache.org/userguide/properties.html -->

<!-- page_index: 8 -->

<a id="properties--properties-catalog"></a>

## Properties Catalog

Properties provide the means of accessing various types of information
regarding a message that passes through the ESB. Furthermore, it is also
possible to use properties to control the behavior of the ESB on a given message flow.

<a id="properties--content"></a>

## Content

- [Introduction](#properties--introduction)
- [Contents](#properties--contents)
- [Generic Properties](#properties--generic_properties)
  - [PRESERVE\_WS\_ADDRESSING](#properties--preserve_ws_addressing)
  - [RESPONSE](#properties--response)
  - [OUT\_ONLY](#properties--out_only)
  - [ERROR\_CODE](#properties--error_code)
  - [ERROR\_MESSAGE](#properties--error_message)
  - [ERROR\_DETAIL](#properties--error_detail)
  - [ERROR\_EXCEPTION](#properties--error_exception)
  - [TRANSPORT\_HEADERS](#properties--transport_headers)
  - [messageType](#properties--messagetype)
  - [ContentType](#properties--contenttype)
  - [preserveProcessedHeaders](#properties--preserveprocessedheaders)
  - [SERVER\_IP](#properties--server_ip)
- [HTTP Transport Properties](#properties--http_transport_properties)
  - [POST\_TO\_URI](#properties--post_to_uri)
  - [FORCE\_SC\_ACCEPTED](#properties--force_sc_accepted)
  - [DISABLE\_CHUNKING](#properties--disable_chunking)
  - [NO\_ENTITY\_BODY](#properties--no_entity_body)
  - [FORCE\_HTTP\_1.0](#properties--force_http_1.0)
  - [HTTP\_SC](#properties--http_sc.0)
  - [FAULTS\_AS\_HTTP\_200](#properties--faults_as_http_200)
  - [NO\_KEEPALIVE](#properties--no_keepalive)
  - [REST\_URL\_POSTFIX](#properties--rest_url_postfix)
  - [REQUEST\_HOST\_HEADER](#properties--request_host_header)
  - [FORCE\_POST\_PUT\_NOBODY](#properties--force_post_put_nobody)
  - [FORCE\_HTTP\_CONTENT\_LENGTH](#properties--force_http_content_length)
  - [COPY\_CONTENT\_LENGTH\_FROM\_INCOMING](#properties--copy_content_length_from_incoming)
  - [COPY\_CONTENT\_LENGTH\_FROM\_INCOMING](#properties--copy_content_length_from_incoming)
- [Synapse Message Context Properties](#properties--synapse_message_context_properties)
  - [SYSTEM\_DATE](#properties--system_date)
  - [SYSTEM\_TIME](#properties--system_time)
  - [MESSAGE\_FORMAT](#properties--message_format)
  - [OperationName](#properties--operationname)

<a id="properties--generic-properties"></a>

## Generic Properties

Generic properties allow to configure or change the behavior of the message flow as they are processed by the ESB.

<a id="properties--preserve_ws_addressing"></a>

### PRESERVE\_WS\_ADDRESSING

By default, the ESB adds a new set of WS-Addressing headers to the messages
forwarded from the ESB. If this property is set to "true" on a message, the ESB will forward it without altering its existing WS-Addressing headers.

Possible Values
:   "true", "false"

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="PRESERVE\_WS\_ADDRESSING" value="true"/>

<a id="properties--response"></a>

### RESPONSE

Once this property is set to 'true' on a message, the ESB will
start treating it as a response message. It is generally used to
route a request message back to its source as the response.
However, currently respond mediator perform the same functionality.

Possible Values
:   "true", "false"

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="RESPONSE" value="true"/>

<a id="properties--out_only"></a>

### OUT\_ONLY

Set this property to "true" on a message to indicate that no response
message is expected for it once it is forwarded from the ESB. In other
words, the ESB will do an out-only invocation with such messages.
It is very important to set this property on messages that are involved
in out-only invocations to prevent the ESB from registering unnecessary
callbacks for response handling and eventually running out of memory.

Possible Values
:   "true", "false"

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="OUT\_ONLY" value="true"/>

<a id="properties--error_code"></a>

### ERROR\_CODE

Use this property to set a custom error code on a message which can be later
processed by a Synapse fault handler. If the Synapse encounters an error during
mediation or routing, this property will be automatically populated.

Possible Values
:   String

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="error-code" expression="get-property('ERROR\_CODE')"/>

<a id="properties--error_message"></a>

### ERROR\_MESSAGE

Use this property to set a custom error message on a message which can be
later processed by a Synapse fault handler. If the Synapse encounters an error
during mediation or routing, this property will be automatically populated.

Possible Values
:   String

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="Cause" expression="get-property('ERROR\_MESSAGE')"/>

<a id="properties--error_detail"></a>

### ERROR\_DETAIL

Use this property to set the exception stacktrace in case of an error.
If the ESB encounters an error during mediation or routing, this property
will be automatically populated.

Possible Values
:   String

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="Trace" expression="get-property('ERROR\_DETAIL')"/>

<a id="properties--error_exception"></a>

### ERROR\_EXCEPTION

Contains the actual exception thrown in case of a runtime error.

Possible Values
:   String

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="error-exception" expression="get-property('ERROR\_EXCEPTION')"/>

<a id="properties--transport_headers"></a>

### TRANSPORT\_HEADERS

Contains the map of transport headers. Automatically populated.
Individual values of this map can be accessed using the property
mediator in the transport scope.

Possible Values
:   java.util.Map

Default Behavior
:   Populated with the transport headers of the incoming request.

Scope
:   axis2

Example
:   <property name="TRANSPORT\_HEADERS" action="remove" scope="axis2"/>

<a id="properties--messagetype"></a>

### messageType

Message formatter is selected based on this property.
This property should have the content type, such as text/xml, application/xml, or application/json.

Possible Values
:   string

Default Behavior
:   Content type of incoming request.

Scope
:   axis2

Example
:   <property name="messageType" value="text/xml" scope="axis2"/>

<a id="properties--contenttype"></a>

### ContentType

This property will be in effect only if the messageType property is set.
If the messageType is set, the value of Content-Type HTTP header of the
outgoing request will be chosen based on this property. Note that this property
is required to be set only if the message formatter seeks it in the
message formatter implementation.

Possible Values
:   string

Default Behavior
:   Value of the Content-type header of the incoming request.

Scope
:   axis2

Example
:   <property name="ContentType" value="text/xml" scope="axis2"/>

<a id="properties--preserveprocessedheaders"></a>

### preserveProcessedHeaders

By default, Synapse removes the SOAP headers of incoming requests that have been processed.
If we set this property to 'true', Synapse preserves the SOAP headers.

Possible Values
:   "true", "false"

Default Behavior
:   Preserving SOAP headers

Scope
:   synapse

Example
:   <property name="preserveProcessedHeaders" value="true" scope="default"/>

<a id="properties--server_ip"></a>

### SERVER\_IP

Server IP/Host name of hosted server

Possible Values
:   string

Default Behavior
:   Set automatically by the mediation engine upon startup with IP address or
    hostname of the ESB host

Scope
:   synapse

Example
:   <property name="StringServerIp" expression="get-property('SERVER\_IP')" scope="default" type="STRING"/>

<a id="properties--http-transport-properties"></a>

## HTTP Transport Properties

HTTP transport properties allow to control and configure how the HTTP transport processes the ongoing messages.

<a id="properties--post_to_uri"></a>

### POST\_TO\_URI

This property makes the outgoing URL of the ESB a complete URL.
This is important when we talk through a Proxy Server.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="POST\_TO\_URI" scope="axis2" value="true"/>

<a id="properties--force_sc_accepted"></a>

### FORCE\_SC\_ACCEPTED

When set to true, this property forces a 202 HTTP response to the client so that it stops waiting
for a response.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="FORCE\_SC\_ACCEPTED" scope="axis2" value="true"/>

<a id="properties--disable_chunking"></a>

### DISABLE\_CHUNKING

Disables the HTTP chunking for outgoing messaging.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="DISABLE\_CHUNKING" scope="axis2" value="true"/>

<a id="properties--no_entity_body"></a>

### NO\_ENTITY\_BODY

This property should be removed if a user want to generate a
response from the ESB to a request without an entity body, for example, GET request.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="NO\_ENTITY\_BODY" scope="axis2" value="true"/>

<a id="properties--force_http_1.0"></a>

### FORCE\_HTTP\_1.0

Force HTTP 1.0 for outgoing HTTP messages.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="FORCE\_HTTP\_1.0" scope="axis2" value="true"/>

<a id="properties--http_sc"></a>

### HTTP\_SC

Set the HTTP status code.

Possible Values
:   HTTP status code number

Default Behavior
:   none

Scope
:   axis2

Example
:   <property name="HTTP\_SC" value="500" scope="axis2"/>

<a id="properties--faults_as_http_200"></a>

### FAULTS\_AS\_HTTP\_200

Set the HTTP status code.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="FAULTS\_AS\_HTTP\_200" value="true" scope="axis2"/>

<a id="properties--no_keepalive"></a>

### NO\_KEEPALIVE

Disables HTTP keep alive for corresponded connection flow. This Can be use in both inflow and outflow.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="NO\_KEEPALIVE" value="true" scope="axis2"/>

<a id="properties--rest_url_postfix"></a>

### REST\_URL\_POSTFIX

The value of this property will be appended to the target URL when sending messages
out in a RESTful manner through an address endpoint. This is useful when you need to
append a context to the target URL in case of RESTful invocations. If you are using an
HTTP endpoint instead of an address endpoint, specify variables in the format of "uri.var.\*"
instead of using this property.

Possible Values
:   A URL fragment starting with "/"

Default Behavior
:   In the case of GET requests through an address endpoint, this contains the query string.

Scope
:   axis2

Example
:   <property name="REST\_URL\_POSTFIX" value="/context" scope="axis2"/>

<a id="properties--request_host_header"></a>

### REQUEST\_HOST\_HEADER

The value of this property will be set as the HTTP host header of outgoing request.

Possible Values
:   string

Default Behavior
:   ESB will set hostname of target endpoint and port as the HTTP host header

Scope
:   axis2

Example
:   <property name="REQUEST\_HOST\_HEADER" value="www.wso2.org" scope="axis2"/>

<a id="properties--force_http_content_length"></a>

### FORCE\_HTTP\_CONTENT\_LENGTH

This property allows the content length to be sent when the ESB sends a
request to a back end server. When HTTP 1.1 is used, this property disables
chunking and sends the content length. When HTTP 1.0 is used, the property
only sends the content length. This property should be set in scenarios where
the backend server is not able to accept chunked content.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="FORCE\_HTTP\_CONTENT\_LENGTH" scope="axis2" value="true"/>

<a id="properties--copy_content_length_from_incoming"></a>

### COPY\_CONTENT\_LENGTH\_FROM\_INCOMING

This property allows the HTTP content length to be copied from an incoming message.
It is only valid when the FORCE\_HTTP\_CONTENT\_LENGTH property is used.
The COPY\_CONTENT\_LENGTH\_FROM\_INCOMING avoids buffering the message in memory for calculating
the content length, thus reducing the risk of performance degradation.

Possible Values
:   "true", "false"

Default Behavior
:   false

Scope
:   axis2

Example
:   <property name="COPY\_CONTENT\_LENGTH\_FROM\_INCOMING" scope="axis2" value="true"/>

<a id="properties--synapse-message-context-properties"></a>

## Synapse Message Context Properties

Synapse Message Context Properties allow to retrieve the data related to synapse
mediation engine information for current message flow.

<a id="properties--system_date"></a>

### SYSTEM\_DATE

Returns the current date as a String. Optionally, a date format as per the standard
date format may be supplied. e.g. synapse:get-property("SYSTEM\_DATE", "yyyy.MM.dd G 'at' HH:mm:ss
z")
or get-property('SYSTEM\_DATE').

Possible Values
:   string

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="StringDateVal" expression="get-property('SYSTEM\_DATE')" scope="default" type="STRING"/>

<a id="properties--system_time"></a>

### SYSTEM\_TIME

Returns the current time in milliseconds.

Possible Values
:   string

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="StringTimeVal" expression="get-property('SYSTEM\_TIME')" scope="default" type="STRING"/>

<a id="properties--message_format"></a>

### MESSAGE\_FORMAT

Returns pox, soap11, soap12 depending on the message.
If a message type is unknown this returns soap12.

Possible Values
:   string

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="StringMessageFormat" expression="get-property('MESSAGE\_FORMAT')" scope="default" type="STRING"/>

<a id="properties--operationname"></a>

### OperationName

Returns the operation name corresponding to the message.

Possible Values
:   string

Default Behavior
:   none

Scope
:   synapse

Example
:   <property name="StringOperationName" expression="get-property('OperationName')" scope="default" type="STRING"/>

---

<a id="xpath"></a>

<!-- source_url: https://synapse.apache.org/userguide/xpath.html -->

<!-- page_index: 9 -->

<a id="xpath--introduction"></a>

## Introduction

Apache Synapse supports standard XPath functions and variables through its
underlying XPath
engine. Apart from standard XPath functions, there are several custom XPath
functions
and variables defined by Synapse to retrieve various message context properties.

<a id="xpath--contents"></a>

## Contents

- [Functions](#xpath--functions)
  - [get-property](#xpath--get_prop)
  - [base64Encode](#xpath--base64_encode)
  - [base64Decode](#xpath--base64_decode)
  - [url-encode](#xpath--url_encode)
- [Variables](#xpath--var)
  - [axis2](#xpath--axis2)
  - [trp](#xpath--trp)
  - [ctx](#xpath--ctx)
  - [url](#xpath--url)
  - [body](#xpath--body)
  - [header](#xpath--header)

<a id="xpath--custom-functions"></a>

## Custom Functions

<a id="xpath--get-property-function"></a>

### get-property function

Get property function retrieves a property from the message context at the given
scope.
If the scope is not specified, property is retrieved from the default synapse
scope.

Syntax:

get-property(String scope, String propertyName)
get-property(String propertyName)

<a id="xpath--supported-scopes"></a>

#### Supported Scopes

- default
- axis2
- transport
- registry
- system

<a id="xpath--default_scope"></a>
<a id="xpath--default-scope"></a>

#### Default scope

Message context properties residing in Synapse scope can be retrieved from the
default scope. These are the properties directly set on the Synapse MessageContext
instance.
Apart from user defined properties, following special properties can also be
retrieved from the default scope.

| Name | Return Value |
| --- | --- |
| To | Incoming URL as a String or empty string if a To address is not defined. |
| From | From address as a String or empty string if a From address is not defined |
| Action | SOAP Action header value as a String or empty string if a Action is not defined |
| FaultTo | SOAP FautTo header value as a String or empty string if a FaultTo address is not defined |
| ReplyTo | ReplyTo header value as a String or empty string if a ReplyTo address is not defined |
| MessageID | A unique identifier (UUID) for the message as a String . This id is guaranteed to be unique. |
| FAULT | TRUE if the message has a fault or empty string if message doesn't have a fault |
| MESSAGE\_FORMAT | Returns pox, get, soap11, soap12 depending on the message. If a message type is unknown this returns soap12 |
| OperationName | Operation name corresponding to the message. |

<a id="xpath--axis2_scope"></a>
<a id="xpath--axis2-scope"></a>

#### Axis2 scope

Message context properties residing in axis2 scope can be retrieved from the axis2
scope. These are the properties set on the underlying Axis2 MessageContext object.

<a id="xpath--transport_scope"></a>
<a id="xpath--transport-scope"></a>

#### Transport scope

Message context properties residing in transport scope can be retrieved from the
transport scope. These are the transport headers set on the MessageContext.

<a id="xpath--reg_scope"></a>
<a id="xpath--registry-scope"></a>

#### Registry scope

Properties residing in registry can be retrieved from the registry scope.

<a id="xpath--system_scope"></a>
<a id="xpath--system-scope"></a>

#### System scope

Java System properties can be retrieved from the system scope.

<a id="xpath--base64encode-function"></a>

### base64Encode function

Returns the base64 encoded value of the argument.

Syntax:

base64Encode(String value)

<a id="xpath--base64decode-function"></a>

### base64Decode function

Returns the base64 decoded value of the argument.

Syntax:

base64Decode(String value)

<a id="xpath--url-encode-function"></a>

### url-encode function

Returns the URL encoded value of the argument.

Syntax:

url-encode(String value)

<a id="xpath--variables"></a>

## Variables

There are several XPath variables supported by Synapse. These are used for
accessing
various
properties from the message context

- $axis2
- $trp
- $ctx
- $url
- $body
- $header

These XPath variables get the properties at various scopes.

<a id="xpath--ctx"></a>

#### $ctx

Variable prefix for accessing the MessageContext properties in default scope.

i.e To get the property named 'foo' at the default scope use the following XPath
expression

$ctx:foo

<a id="xpath--axis2"></a>

#### $axis2

Variable prefix for accessing the axis2 MessageContext properties

i.e. To get the property named 'messageType' use the following XPath expression

$axis2:messageType

<a id="xpath--trp"></a>

#### $trp

Variable prefix for accessing transport headers of the message

i.e. To get the transport header named Content-Type use the following XPath
expression

$trp:Content-Type

<a id="xpath--url"></a>

#### $url

Variable prefix for accessing URL parameters of the message

i.e. To get the URL parameter named 'bar' use the following XPth expression

$url:bar

<a id="xpath--body"></a>

#### $body

Get the message body

<a id="xpath--header"></a>

#### $header

Get the soap header

---

<a id="extending"></a>

<!-- source_url: https://synapse.apache.org/userguide/extending.html -->

<!-- page_index: 10 -->

<a id="extending--apache-synapse-esb-extending-synapse"></a>

## Apache Synapse ESB - Extending Synapse

Apache Synapse provides a number of extension points so that
users can plug-in custom developed code to extend the
functionality of the ESB. While the built-in mediators are sufficient to implement
most integration scenarios, sometimes it is very helpful to be able to deploy some custom code into the
service bus and make the solution simpler. Most Synapse APIs are in Java and
therefore the users looking to extend Synapse are expected to have a
decent knowledge and experience in Java programming.

<a id="extending--writing-custom-mediator-implementations"></a>

## Writing custom Mediator implementations

The primary interface of the Synapse API is the MessageContext
interface defined below. This essentially defines the per-message
context passed through the chain of mediators, for each and every
message received and processed by Synapse. Each message instance is
wrapped within a MessageContext instance, and the message context
is set with the references to the SynapseConfiguration and
SynapseEnvironment objects. The
[SynapseConfiguration](https://synapse.apache.org/apidocs/org/apache/synapse/config/SynapseConfiguration.html)
object holds the global configuration model that defines
mediation rules, local registry entries and other and configuration, while
the
[SynapseEnvironment](https://synapse.apache.org/apidocs/org/apache/synapse/core/SynapseEnvironment.html)
object gives access to the underlying SOAP implementation used -
Axis2. A typical mediator would need to manipulate the
MessageContext by referring to the SynapseConfiguration. However, it
is strongly recommended that the SynapseConfiguration is not
updated by mediator instances as it is shared by all messages, and
may be updated by Synapse administration or configuration modules.
Mediator instances may store local message properties into the
MessageContext for later retrieval by successive mediators.

<a id="extending--messagecontext-interface"></a>

#### [MessageContext Interface](http://svn.apache.org/viewvc/synapse/trunk/java/modules/core/src/main/java/org/apache/synapse/MessageContext.java?view=markup)

package org.apache.synapse;
import ...
public interface MessageContext {
/\*\*
\* Get a reference to the current SynapseConfiguration
\*
\* @return the current synapse configuration
\*/
public SynapseConfiguration getConfiguration();
/\*\*
\* Set or replace the Synapse Configuration instance to be used. May be used to
\* programmatically change the configuration at runtime etc.
\*
\* @param cfg The new synapse configuration instance
\*/
public void setConfiguration(SynapseConfiguration cfg);
/\*\*
\* Returns a reference to the host Synapse Environment
\* @return the Synapse Environment
\*/
public SynapseEnvironment getEnvironment();
/\*\*
\* Sets the SynapseEnvironment reference to this context
\* @param se the reference to the Synapse Environment
\*/
public void setEnvironment(SynapseEnvironment se);
/\*\*
\* Get the value of a custom (local) property set on the message instance
\* @param key key to look up property
\* @return value for the given key
\*/
public Object getProperty(String key);
/\*\*
\* Set a custom (local) property with the given name on the message instance
\* @param key key to be used
\* @param value value to be saved
\*/
public void setProperty(String key, Object value);
/\*\*
\* Returns the Set of keys over the properties on this message context
\* @return a Set of keys over message properties
\*/
public Set getPropertyKeySet();
/\*\*
\* Get the SOAP envelope of this message
\* @return the SOAP envelope of the message
\*/
public SOAPEnvelope getEnvelope();
/\*\*
\* Sets the given envelope as the current SOAPEnvelope for this message
\* @param envelope the envelope to be set
\* @throws org.apache.axis2.AxisFault on exception
\*/
public void setEnvelope(SOAPEnvelope envelope) throws AxisFault;
/\*\*
\* SOAP message related getters and setters
\*/
public ....get/set()...
}

The MessageContext interface is based on the Axis2
MessageContext interface, and uses the Axis2 EndpointReference and
SOAPEnvelope classes/interfaces. The purpose of this interface is
to capture a message as it flows through the system. As you will
see the message payload is represented using the SOAP infoset.
Binary messages can be embedded in the Envelope using MTOM or SwA
attachments using the AXIOM object model.

<a id="extending--mediator-interface"></a>

#### [Mediator interface](http://svn.apache.org/viewvc/synapse/trunk/java/modules/core/src/main/java/org/apache/synapse/Mediator.java?view=markup)

The second key interface for mediator writers is the Mediator
interface:

package org.apache.synapse;
import org.apache.synapse.MessageContext;
/\*\*
\* All Synapse mediators must implement this Mediator interface. As a message passes
\* through the synapse system, each mediator's mediate() method is invoked in the
\* sequence/order defined in the SynapseConfiguration.
\*/
public interface Mediator {
/\*\*
\* Invokes the mediator passing the current message for mediation. Each
\* mediator performs its mediation action, and returns true if mediation
\* should continue, or false if further mediation should be aborted.
\*
\* @param synCtx the current message for mediation
\* @return true if further mediation should continue
\*/
public boolean mediate(MessageContext synCtx);
/\*\*
\* This is used for debugging purposes and exposes the type of the current
\* mediator for logging and debugging purposes
\* @return a String representation of the mediator type
\*/
public String getType();
}

A mediator can read and/or modify the message encapsulated in
the MessageContext in any suitable manner - adjusting the routing
headers or changing the message body. If the mediate() method
returns false, it signals to the Synapse processing model to stop
further processing of the message. For example, if the mediator is
a security agent it may decide that this message is dangerous and
should not be processed further. This is generally the exception as
mediators are usually designed to co-operate to rocess the message
onwards.

<a id="extending--leaf-and-node-mediators-list-mediators-and-filter-mediators"></a>

### Leaf and Node Mediators, List mediators and Filter mediators

Mediators may be Node mediators (i.e. these that can contain
child mediators) or Leaf mediators (mediators that does not hold
any other child mediators). A Node mediator must implement the
org.apache.synapse.mediators.ListMediator interface listed below, or extend from the
org.apache.synapse.mediators.AbstractListMediator.

<a id="extending--the-listmediator-interface"></a>

#### [The ListMediator interface](http://svn.apache.org/viewvc/synapse/trunk/java/modules/core/src/main/java/org/apache/synapse/mediators/ListMediator.java?view=markup)

package org.apache.synapse.mediators;
import java.util.List;
/\*\*
\* The List mediator executes a given sequence/list of child mediators
\*/
public interface ListMediator extends Mediator {
/\*\*
\* Appends the specified mediator to the end of this mediator's (children) list
\* @param m the mediator to be added
\* @return true (as per the general contract of the Collection.add method)
\*/
public boolean addChild(Mediator m);
/\*\*
\* Appends all of the mediators in the specified collection to the end of this mediator's (children)
\* list, in the order that they are returned by the specified collection's iterator
\* @param c the list of mediators to be added
\* @return true if this list changed as a result of the call
\*/
public boolean addAll(List c);
/\*\*
\* Returns the mediator at the specified position
\* @param pos index of mediator to return
\* @return the mediator at the specified position in this list
\*/
public Mediator getChild(int pos);
/\*\*
\* Removes the first occurrence in this list of the specified mediator
\* @param m mediator to be removed from this list, if present
\* @return true if this list contained the specified mediator
\*/
public boolean removeChild(Mediator m);
/\*\*
\* Removes the mediator at the specified position in this list
\* @param pos the index of the mediator to remove
\* @return the mediator previously at the specified position
\*/
public Mediator removeChild(int pos);
/\*\*
\* Return the list of mediators of this List mediator instance
\* @return the child/sub mediator list
\*/
public List getList();
}

A ListMediator implementation should call super.mediate(synCtx)
to process its sub mediator sequence. A FilterMediator is a
ListMediator which executes its sequence of sub mediators on
successful outcome of a test condition. The Mediator instance which
performs filtering should implement the FilterMediator interface.

<a id="extending--filtermediator-interface"></a>

#### [FilterMediator interface](http://svn.apache.org/viewvc/synapse/trunk/java/modules/core/src/main/java/org/apache/synapse/mediators/FilterMediator.java?view=markup)

package org.apache.synapse.mediators;
import org.apache.synapse.MessageContext;
/\*\*
\* The filter mediator is a list mediator, which executes the given (sub) list of mediators
\* if the specified condition is satisfied
\*
\* @see FilterMediator#test(org.apache.synapse.MessageContext)
\*/
public interface FilterMediator extends ListMediator {
/\*\*
\* Should return true if the sub/child mediators should execute. i.e. if the filter
\* condition is satisfied
\* @param synCtx
\* @return true if the configured filter condition evaluates to true
\*/
public boolean test(MessageContext synCtx);
}

<a id="extending--writing-custom-configuration-implementations-for-mediators"></a>

## Writing custom Configuration implementations for mediators

You may write your own custom configurator for the Mediator
implementation you write without relying on the Class mediator or
Spring extension for its initialization. You could thus write a
MediatorFactory implementation which defines how to digest a custom
XML configuration element to be used to create and configure the
custom mediator instance. A MediatorSerializer implementation
defines how a configuration should be serialized back into
an XML configuration. The custom MediatorFactory &
MediatorSerializer implementations and the mediator class/es must be bundled in a JAR
file conforming to the J2SE Service Provider model (See the
description for Extensions below for more details and examples) and
placed into the SYNAPSE\_HOME/lib folder, so that the Synapse
runtime could find and load the definition. Essentially this means
that a custom JAR file must bundle your class implementing the
Mediator interface, and the MediatorFactory implementation class and
contain two text files named
"org.apache.synapse.config.xml.MediatorFactory" and
"org.apache.synapse.config.xml.MediatorSerializer" which
will contain the fully qualified name(s) of your MediatorFactory
and MediatorSerializer implementation classes. You should also
place any dependency JARs into the same lib folder so that the
correct classpath references could be made.
The MediatorFactory interface listing is given below, which you
should implement, and its getTagQName() method must define the fully qualified
element of interest for custom configuration. The Synapse
initialization will call back to this MediatorFactory instance through the
createMediator(OMElement elem) method passing in this XML element, so that an instance of the mediator could be created utilizing the
custom XML specification and returned. See the ValidateMediator and
the ValidateMediatorFactory classes under modules/extensions in the
Synapse source distribution for examples.

<a id="extending--the-mediatorfactory-interface"></a>

#### [The MediatorFactory interface](http://svn.apache.org/viewvc/synapse/trunk/java/modules/core/src/main/java/org/apache/synapse/config/xml/MediatorFactory.java?view=markup)

package org.apache.synapse.config.xml;
import ...
/\*\*
\* A mediator factory capable of creating an instance of a mediator through a given
\* XML should implement this interface
\*/
public interface MediatorFactory {
/\*\*
\* Creates an instance of the mediator using the OMElement
\* @param elem
\* @return the created mediator
\*/
public Mediator createMediator(OMElement elem);
/\*\*
\* The QName of this mediator element in the XML config
\* @return QName of the mediator element
\*/
public QName getTagQName();
}

<a id="extending--the-mediatorserializer-interface"></a>

#### [The MediatorSerializer interface](http://svn.apache.org/viewvc/synapse/trunk/java/modules/core/src/main/java/org/apache/synapse/config/xml/MediatorSerializer.java?view=markup)

package org.apache.synapse.config.xml;
import ...
/\*\*
\* Interface which should be implemented by mediator serializers. Does the
\* reverse of the MediatorFactory
\*/
public interface MediatorSerializer {
/\*\*
\* Return the XML representation of this mediator
\* @param m mediator to be serialized
\* @param parent the OMElement to which the serialization should be attached
\* @return the serialized mediator XML
\*/
public OMElement serializeMediator(OMElement parent, Mediator m);
/\*\*
\* Return the class name of the mediator which can be serialized
\* @return the class name
\*/
public String getMediatorClassName();
}

<a id="extending--configuring-mediators"></a>

## Configuring mediators

Mediators could access the Synapse registry to load resources
and configure the local behaviour. Refer to the Spring mediator and
Script mediator implementations for examples on how this could be
achieved.

<a id="extending--loading-of-extensions-by-the-synapse-runtime"></a>

#### Loading of Extensions by the Synapse runtime

Synapse loads available extensions from the runtime classpath
using the
[J2SE
Service Provider model](http://java.sun.com/j2se/1.3/docs/guide/jar/jar.html#Service%20Provider)
. This essentially iterates over the available JAR files, for a META-INF/services directory within each file, and looks for a text file with the name org.apache.synapse.config.xml.MediatorFactory
which contains a list of fully qualified classname that implement
the above interface, listing each class in a separate line. e.g. The
built-in synapse-extensions.jar contains the following structure

synapse-extensions.jar
/META-INF/services
org.apache.synapse.config.xml.MediatorFactory
org.apache.synapse.config.xml.MediatorSerializer
/... the implementation classes as usual...

<a id="extending--writing-synapse-observers"></a>

## Writing Synapse Observers

A Synapse observer is developed by either implementing the
org.apache.synapse.config.SynapseObserver interface or by
extending the org.apache.synapse.config.AbstractSynapseObserver
class. A Synapse observer is notified by the Synapse configuration
when new elements are added to the configuration and
when existing elements are removed from the configuration. The
following event handlers are available to the Synapse observer implementations.

public void sequenceAdded(Mediator sequence);
public void sequenceRemoved(Mediator sequence);
public void entryAdded(Entry entry);
public void entryRemoved(Entry entry);
public void endpointAdded(Endpoint endpoint);
public void endpointRemoved(Endpoint endpoint);
public void proxyServiceAdded(ProxyService proxy);
public void proxyServiceRemoved(ProxyService proxy);
public void startupAdded(Startup startup);
public void startupRemoved(Startup startup);
public void eventSourceAdded(SynapseEventSource eventSource);
public void eventSourceRemoved(SynapseEventSource eventSource);

The AbstractSynapseObserver provides default implementations to
all these event handlers. It simply logs any received events.

In situations where the custom code has access to the
SynapseConfiguration class observers can be directly registered
with the SynapseConfiguration by using
the registerObserver(SynapseObserver o) method. Otherwise
SynapseObserver implementations
can be defined in the synapse.properties file which resides in the
SYNAPSE\_HOME/lib directory. The following example shows how two observers are
registered with the Synapse configuration using the
synapse.properties file.

synapse.observers=test.LoggingObserverImpl, test.SimpleObserverImpl

<a id="extending--scheduled-tasks"></a>

## Scheduled Tasks

A scheduled task is a custom developed piece of Java code that
is scheduled in the ESB to execute periodically. A scheduled task
must implement the org.apache.synapse.task.Task
interface. This interface has a single 'execute' method. Once scheduled the
execute method is called by Synapse periodically.

Synapse also comes with a built-in task implementation known as
the MessageInjector. This task can be used to inject messages into
the service bus periodically. Refer sample 300 to see how to use the
MessageInjector task.

---

<a id="template_library"></a>

<!-- source_url: https://synapse.apache.org/userguide/template_library.html -->

<!-- page_index: 11 -->

<a id="template_library--synapse-template-libraries"></a>

## Synapse Template Libraries

Synapse template libraries are a mechanism to group synapse templates and automatically
expose it as a self contained set of function modules. It can be considered as a container
consisting a set of templates grouped in a particular order. Currently a synapse template
library is shipped as a ".zip" file and should be deployed inside
{$SYNAPSE\_HOME}/repository/conf/synapse-libs .
If a given template container is successfully deployed, all
templates within the library will be accessible to any Synapse user.

Following is a sample skeleton structure of a template library

|-- artifacts.xml
|-- com
| `-- synapse
| `-- sample
| `-- SynapseLibTestMediator.class
|-- lib
| `-- test-mediator-1.0.0.jar
|-- template\_dir-1
| |-- artifact.xml
| |-- templ1\_ns1.xml
| `-- templ2\_ns1.xml
`-- template\_dir-2
|-- artifact.xml
|-- templ1\_ns2.xml
`-- templ2\_ns2.xml

Following are these components at an overview.

- artifacts.xml
  This contains synapse library name , package name information and template groupings.

  <artifacts>
  <artifact name="synapse.lib.name" package="synapse.lib.package.name">
  <dependency artifact="template.group.name"/>\*
  <description>sample synapse library</description>?
  </artifact>
  </artifacts>
- artifact.xml
  This contains information about each individual template group.
  ie: - names of the templates in the group , corresponding configuration file ,etc.

  <artifact name="template.group.name" type="synapse/template">
  <subArtifacts>
  <artifact name="template.name">
  <file>template\_file.xml</file>
  <description>a sample synapse library function</description>?
  </artifact>\*
  </subArtifacts>
  </artifact>
- template\_file.xml
  This contains the implementation of each individual template configuration
- ./lib
  This is the directory to add any classes for class loading or can contain the .class files from
  the root
  level.

Also utilizing a synapse library is a three step process.

- Create and deploy the library
- Importing the library into synapse
  Users should deploy a import\_lib\_name.xml into
  {$SYNAPSE\_HOME}/repository/conf/synapse-config/imports

  <import xmlns="http://ws.apache.org/ns/synapse" name="SampleLibrary" package="synapse.lib"/>
- Execute functions of library using a template invoker. Target template is a
  combination of the package of synapse library and the target template name
  target == {synapse\_lib\_package}.{template name}

  <call-template target="synapse.lib.pkg.name.template\_name">
  <with-param name="..." value="..."/>\*
  </call-template>

<a id="template_library--synapse-enterprise-integration-patterns-library"></a>

## Synapse Enterprise Integration Patterns library

Synapse Enterprise Integration Patterns library is a container consisting a set of
templates grouped in a particular order by implementing commonly used
[Enterprise
Integration Patterns](http://www.eaipatterns.com)
from the set of patterns introduced by Gregor Hohpe and Bobby Woolf.
Users can design their solutions using these well-known patterns and then simply configure
and use these same patterns in Apache Synapse by calling up the function as required.
So this will greatly reduce the effort required when building integrations.

Following lists all the built-in patterns of Synapse EIP library currently supports and
describes their usage, functionality and configuration syntax.
This excludes all generic EIP patterns supported by synapse out of the box.

- [Callout Block](#template_library--calloutblock)
- [Splitter](#template_library--splitter)
- [Aggregator](#template_library--aggregator)
- [Splitter-Aggregator](#template_library--splitteraggregator)
- [Scatter-Gather](#template_library--scattergather)
- [Wire Tap](#template_library--wiretap)
- [Content-Based Router](#template_library--contentbasedrouter)
- [Dynamic Router](#template_library--dynamicrouter)
- [Recipient List](#template_library--recipientlist)

> [!NOTE]
> <a id="template_library--callout-block"></a>

>
> ### Callout Block
>
> This pattern is pretty much identical to the
> [Routing slip pattern](http://www.eaipatterns.com/RoutingTable.html)
> and this blocks
> external service invocation during mediation. And useful in scenarios such as service chaining.
> As default values are assigned to source and target xpaths, one can simply utilize this pattern by just defining serviceURL.
> Call template target -
> **synapse.lang.eip.callout\_block**
> Parameters
> **service\_URL**
> - URL of the service
> **[action]**
> - SOAP action(Optional)
> **[source\_xpath | source\_key]**
> - Payload of the message( either Xpath or key and Optional)
> **[target\_xpath | target\_key]**
> - A node to attach the response element ( either Xpath or key and optional)
> Related Sample - [Sample 850](https://synapse.apache.org/userguide/samples/sample850.html)

<a id="template_library--splitter"></a>

### Splitter

The
[Splitter pattern](http://www.eaipatterns.com/Sequencer.html)
breaks out the composite message into a series of individual messages by
finding matching elements for the XPath expression specified and then redirected to the given
endpoint.
Call template target -
**synapse.lang.eip.splitter**
Parameters
**iterate\_exp**
- Xpath expression from which element you want to split the message.
**[attach\_path]**
- Xpath expression to specify which elements needs to be attached to form new messages.( Optional)
**endpoint\_url**
- Endpoint which newly created messages are redirected to.
**[attach\_path\_enabled]**
- Boolean value to enable attach path. Optional and by default this is false.
Related Sample - [Sample 851](https://synapse.apache.org/userguide/samples/sample851.html)

<a id="template_library--aggregator"></a>

### Aggregator

The
[Aggregator pattern](http://www.eaipatterns.com/Aggregator.html)
builds a single message distilled from the individual messages.
And messages will be merged by using the XPath expression specified for aggregator\_exp.
Call template target -
**synapse.lang.eip.aggregator**
Parameters
**aggregator\_exp**
- An XPath expression specifying based on which elements to aggregate.
**[sequence\_ref]**
- target sequence which message should be mediated after aggregation. (Optional and if this is not
specified aggregator will send the aggregated message to the client).
**[oncomplete\_seq\_enabled]**
- Boolean value to enable target sequence. (Optional and by default this is false)
Related Sample - [Sample 851](https://synapse.apache.org/userguide/samples/sample851.html)

<a id="template_library--splitter-aggregator"></a>

### Splitter-Aggregator

This pattern provides the combined functionality of Splitter and Aggregator patterns.
Which is when you specified following parameters this pattern will split the message and
does a synchronized call for the given endpoint and aggregates replies then send back to
client or mediates to the defined target sequence.
Call template target -
**synapse.lang.eip.splitter\_aggregator**
Parameters
**iterate\_exp**
- An Xpath expression from which element you want to split the message.
**[attach\_path]**
- An Xpath expression to specify which elements needs to be attached to form new messages.(
Optional)
**endpoint\_url**
- Endpoint which newly created messages are redirected to.
**[attach\_path\_enabled]**
- Boolean value to enable attach path. Optional and by default this is false.
**aggregator\_exp**
- An XPath expression specifying based on which elements to aggregate.
**[sequence\_ref]**
- Target sequence which message should be mediated after aggregation. (Optional and if this is not
specified aggregator will send the aggregated message to the client).
**[oncomplete\_seq\_enabled]**
- Boolean value to enable target sequence. (Optional and by default this is false)
Related Sample - [Sample 852](https://synapse.apache.org/userguide/samples/sample852.html)

<a id="template_library--scatter-gather"></a>

### Scatter-Gather

The
[Scatter-Gather pattern](http://www.eaipatterns.com/BroadcastAggregate.html)
broadcasts a message to multiple recipients and re-aggregates the
responses back into a single message and send back to client or mediates to the defined
target sequence.
Call template target -
**synapse.lang.eip.scatter\_gather**
Parameters
**aggregator\_exp**
- An XPath expression specifying based on which elements to aggregate.
**[sequence\_ref]**
- Target sequence which message should be mediated after aggregation. (Optional and if this is not
specified aggregator will send the aggregated message to the client).
**[oncomplete\_seq\_enabled]**
- Boolean value to enable target sequence. (Optional and by default this is false)
**recipient\_list**
- Set of recipient endpoints , which should be specified as comma separated values
Related Sample - [Sample 853](https://synapse.apache.org/userguide/samples/sample853.html)

<a id="template_library--wire-tap"></a>

### Wire Tap

[Wire Tap pattern](http://www.eaipatterns.com/WireTap.html)
enables route messages to a secondary channel while they are being forwarded to the main channel.
Call template target -
**synapse.lang.eip.wire\_tap**
Parameters
**destination\_uri**
- Endpoint of main channel
**wiretap\_uri**
- Endpoint of secondary channel
Related Sample - [Sample 854](https://synapse.apache.org/userguide/samples/sample854.html)

<a id="template_library--content-based-router"></a>

### Content-Based Router

The
[Content Based Router pattern](http://www.eaipatterns.com/ContentBasedRouter.html)
route messages to the appropriate sequence, according to the message contents.
Routing decision is taken by matching given Xpath expression and Regular Expression.
User can define multiple matching elements as regular expressions and a target sequence where
if any of matching element evaluates to true then it mediates using the target sequence.
If none of the case statements are matching and default case is specified, it will be executed.
Call template target -
**synapse.lang.eip.content\_base\_router**
Parameters
**routing\_exp**
- Here you can specify the source xpath to be evaluated
**match\_content**
- This is a String which contains the matching conditions. Following is the syntax of it
**"IBM:cnd1\_seq,MSFT:cnd2\_seq;cnd3\_seq"**
User can define multiple matching conditions using "," splitter. regular expressions and
target sequence should be separated by inserting":". And finally default sequence needs to be
defined
after inserting ";". If there is no any target sequence
defined for a particular regular expression , default it will be mediated to the main sequence.
Related Sample - [Sample 855](https://synapse.apache.org/userguide/samples/sample855.html)

<a id="template_library--dynamic-router"></a>

### Dynamic Router

The
[Dynamic Router pattern](http://www.eaipatterns.com/DynamicRouter.html)
route a message consecutively through a series of condition steps, which is parsed by the â€œconditionsâ€ parameter. The list of sequences through which the message
should pass is decided dynamically at run time.
It checks whether the route condition evaluates to true and mediates using the given sequence and
user can define
routing decision based on the message contents such as HTTP url,HTTP headers or combination of both.
Call template target -
**synapse.lang.eip.dynamic\_router**
Parameters
**conditions**
- This is a String which contains the routing rules. Following is the syntax of it.
**"header=foo:bar.\*{AND}url=/services/;seq=seq1,header=header1:bar.\*{OR}header=header1:foo.\*;seq=seq2,header=header2:foo.\*;seq=seq3"**
User can define multiple routing rules by using "," splitter. Routing rule contains following
format, To match HTTP headers , use
**header=regEx:seqRef**
header source and regular expression should be separated by inserting ":"
To match HTTP url, use
**url=/url**
Then target sequence needs to be defined after inserting ";"
Also you can use**"{AND}"**as to specify logical AND ,
**"{OR}"**
as to specify logical OR to match
multiple headers and url in your expression.
Related Sample - [Sample 856](https://synapse.apache.org/userguide/samples/sample856.html)

<a id="template_library--recipient-list"></a>

### Recipient List

The
[Recipient List pattern](http://www.eaipatterns.com/RecipientList.html)
forward the message to all channels associated with the defined set of recipients.
Call template target -
**synapse.lang.eip.recipient\_list**
Parameters
**recipient\_list**
- set of recipient endpoints , which should be specified as comma separated values
Related Sample - [Sample 857](https://synapse.apache.org/userguide/samples/sample857.html)

---

<a id="upgrading"></a>

<!-- source_url: https://synapse.apache.org/userguide/upgrading.html -->

<!-- page_index: 12 -->

<a id="upgrading--upgrading-to-the-latest-version"></a>

## Upgrading to the Latest Version

If you are using an older version of Synapse (1.x/2.x) and now looking to migrate to
the latest versions (3.x) this document would be a good starting point. This
article provides information on steps that need to be carried out to smoothly
migrate from an older release of Synapse to the latest version. If you are migrating from 1.x version
to 3.x we recommend you follow the 1.x -> 2.x migration followed by the 2.x -> 3.x.

<a id="upgrading--contents"></a>

## Contents

- [General comments](#upgrading--general_comments)
- [Upgrading from 2.1 to 3.0](#upgrading--upgrading_from_2.1_to_3.0)
  - [Custom Extensions](#upgrading--custom_extensions_3.0)
  - [Respond and Loopback Mediators](#upgrading--new_mediators_3.0)
- [Upgrading from 1.2 to 2.1](#upgrading--upgrading_from_1.2_to_2.1)
  - [Configuration file vs multi XML configuration](#upgrading--configuration_file_vs_multi_xml_configuration)
  - [Endpoint URLs for proxy services](#upgrading--endpoint_urls_for_proxy_services)
  - [Mediator Deployer](#upgrading--mediator_deployer)
  - [Main Sequence](#upgrading--main_sequence)
  - [Filter Mediator](#upgrading--filter_mediator)
  - [Migration Tool](#upgrading--migration_tool)
  - [Custom Extensions and API changes](#upgrading--custom_extensions_and_api_changes)

<a id="upgrading--general-comments"></a>

## General comments

If you are using custom extensions (mediators, startups, etc.) implemented in Java and
depending on Synapse APIs, you should go through the following process before upgrading
to a new release:

1. Compile the extension with the libraries from the Synapse release you are
   currently using and check for any deprecation warnings. You should change your
   code to eliminate all those warnings. In general the Javadoc of the
   deprecated class or method gives you a hint on how to change your code. Test all
   your changes with your current Synapse release.
2. Recompile and test the extension with the libraries from the new Synapse release.
   We try to avoid introducing incompatible changes to Synapse's core APIs between
   releases (except if the related classes or methods were deprecated in the previous
   release). However, it is not always possible to maintain compatibility. In addition
   your code might depend on features that are not part of the core API. Therefore,
   even if you don't use deprecated methods and classes, there is no guarantee that
   your code will not break when upgrading to a new release and you always need to
   recompile and test them before deploying to the new release.
3. Upgrade your Synapse installation and deploy the new version of your extensions.

If you are skipping releases when upgrading your installation, you might nevertheless
want to go through the first step for all the intermediate releases. This will make
the migration easier.

<a id="upgrading--upgrading-from-2.1-to-3.0"></a>

## Upgrading from 2.1 to 3.0

<a id="upgrading--custom-extensions"></a>

### Custom Extensions

Synapse 3.0 introduces the PassThrough HTTP Transport which improves HTTP transport performance by removing
intermediary buffer use when there is no requirement to read an HTTP payload (i.e. message is merely passed
through). If you have custom extensions that depend on accessing or reading buffers directly, you
may require to change your code to trigger the PassThrough transport to build the payload. This can
be done using the [RelayUtils#buildMessage()](https://synapse.apache.org/apidocs/org/apache/synapse/transport/passthru/util/RelayUtils.html)
static methods.

<a id="upgrading--respond-and-loopback-mediators"></a>

### Respond and Loopback Mediators

[Respond](#mediators--respond) and [Loopback](#mediators--loopback)
are new mediators introduced in Apache Synapse 3.0. [Respond](#mediators--respond) provides
a mechanism to send a message back to the client as a response. In older versions of Apache Synapse
we would use the [Send](#mediators--send) mediator to respond back to a client either
after a message is received from a backend in an out sequence or force a response back to the client
using a series of mediators as follows:

<header name="To" action="remove"/>
<property name="RESPONSE" value="true" scope="default" type="STRING"/>
<property name="NO\_ENTITY\_BODY" scope="axis2" action="remove"/>
<send/>

We can replace above methods with the [Respond](#mediators--respond) mediator anywhere
in the mediation flow to respond back to the client with the current message. Any mediators residing
after the [Respond](#mediators--respond) mediator will be ignored.

Similarly the [Loopback](#mediators--loopback) mediator is used to jump the flow from
an in sequence to the out sequence ignoring any mediators residing after the
[Loopback](#mediators--loopback) mediator. [Loopback](#mediators--loopback)
mediator has no effect from inside an out sequence.

<a id="upgrading--upgrading-from-1.2-to-2.1"></a>

## Upgrading from 1.2 to 2.1

<a id="upgrading--configuration-file-vs-multi-xml-configuration"></a>

### Configuration file vs multi XML configuration

In 1.2 you have been using a single synapse.xml file which resides on the
repository/conf directory of the distribution, where as on 2.1 we have structured
this into a configuration repository with multiple directories to have different
artifact types and each and every artifact configuration to reside on a different
files inside the desired repository directory. This repository directory on the 2.1
release resides in the repository/conf directory too, and named as synapse-config.
The repository directory structure inside the synapse-config directory
looks like follows;

synapse-config
/api
/endpoints
/event-sources
/local-entries
/priority-executors
/proxy-services
/sequences
main.xml
fault.xml
/tasks
/templates
registry.xml
synapse.xml

As you can see in the above sketch of the repository though it is a repository based
configuration, it also supports the old style single flat synapse.xml file in which
case it has to reside inside the root of the repository.

So the easiest way to migrate the configuration is to move your already existing
synapse.xml file in repository/conf directory in 1.2 version into the
repository/conf/synapse-config directory of the 2.x version. *Note: When doing this
migration you should also delete the main.xml and fault.xml files which are there on the
sequences directory of the repository, otherwise there will be 2 main and fault
sequences one coming from the sequences directory and the other coming from your just
copied synapse.xml file.*

<a id="upgrading--endpoint-urls-for-proxy-services"></a>

### Endpoint URLs for proxy services

In release 2.1 the endpoint URLs for proxy services have changed from
/soap to /services. E.g. http://localhost:8280/services/StockQuote
should be used instead of http://localhost:8280/soap/StockQuote.

<a id="upgrading--mediatordeployer"></a>

### MediatorDeployer

Release 1.3 has enhanced capabilities for extension deployment. While in 1.2 extension
deployment was limited to mediators bundled as simple JAR files, 1.3 extended this
support to tasks and defined a new archive format (XAR) that allows to bundle
these extensions together with their dependency JARs (see
[SYNAPSE-377](http://issues.apache.org/jira/browse/SYNAPSE-377)
for more details). Enabling these features requires changes to the axis2.xml
configuration file. In 1.2 the deployer was configured as follows:

<deployer extension="jar" directory="mediators"
class="org.apache.synapse.core.axis2.MediatorDeployer"/>

In 2.1 the suggested configuration is:

<deployer extension="xar" directory="extensions"
class="org.apache.synapse.deployers.ExtensionDeployer"/>

It is possible to have multiple configuration entries for the extension deployer
with different settings. For example, if you used the deployer in 1.2 you might
want to have the following configuration:

<deployer extension="jar" directory="mediators"
class="org.apache.synapse.deployers.ExtensionDeployer"/>
<deployer extension="xar" directory="extensions"
class="org.apache.synapse.deployers.ExtensionDeployer"/>

<a id="upgrading--jms-transport"></a>

### JMS transport

The way the JMS transport determines the content type of incoming messages has
slightly changed between Synapse 1.2 and 2.x. The mechanism is also more flexible.
See SYNAPSE-304 and SYNAPSE-424 for the reasons of this change and refer to the
[WS-Commons Transport project](http://ws.apache.org/commons/transport/)
for documentation.

<a id="upgrading--main-sequence"></a>

### Main Sequence

On Synapse 1.2 you could have mediator configuration on the top level definitions
tag and they were treated as the **main** sequence if there is no
main sequence defined in the configuration. How ever removing the conflict of having
top level mediators and a main sequence leading the synapse to fail to start on
2.x Synapse configuration builder simply ignores the top level mediators. So you
need to wrap the top level mediators, if there are any, with the sequence named
**main** on the new 2.1 version.

To further explain this lets have a look at the following valid configuration bit
(this is the sample 0 configuration) on the 1.2;

<definitions xmlns="http://ws.apache.org/ns/synapse">
<!-- log all attributes of messages passing through -->
<log level="full"/>
<!-- Send the message to implicit destination -->
<send/>
</definitions>

which needs to be changed to the following configuration on 2.1

<definitions xmlns="http://ws.apache.org/ns/synapse">
<sequence name="main">
<!-- log all attributes of messages passing through -->
<log level="full"/>
<!-- Send the message to implicit destination -->
<send/>
<sequence/>
</definitions>

<a id="upgrading--filter-mediator"></a>

### Filter Mediator

From 2.1 onwards Synapse filter mediator supports the else close as well, and hence
the filter matching set of mediators has to be enclosed within a <then> element.

If we consider the following sample from the 1.2 version of synapse;

<filter source="get-property('To')" regex=".\*/StockQuote.\*">
<send>
<endpoint>
<address uri="http://localhost:9000/soap/SimpleStockQuoteService"/>
</endpoint>
</send>
<drop/>
</filter>

the equivalent configuration for the 2.1 release is going to be;

<filter source="get-property('To')" regex=".\*/StockQuote.\*">
<then>
<send>
<endpoint>
<address uri="http://localhost:9000/soap/SimpleStockQuoteService"/>
</endpoint>
</send>
<drop/>
<then/>
</filter>

You could also add an else close to this conditional statement as follows on 2.x
which is not possible on 1.2

<filter source="get-property('To')" regex=".\*/StockQuote.\*">
<then>
<send>
<endpoint>
<address uri="http://localhost:9000/soap/SimpleStockQuoteService"/>
</endpoint>
</send>
<drop/>
<then/>
<else/>
<log/>
<else/>
</filter>

<a id="upgrading--migration-tool"></a>

### Migration Tool

In general it is recommended to run the configuration through the migration tool
provided with the Synapse 2.x release, on your synapse 1.2 configuration before
using it with the 2.1.

To run the migration tool execute the synapse-config-migrator.sh by passing the
synapse.xml file location of the
1.2 configuration. Which will create the 2.1
compatible configuration with the .new suffix. For example;

```
sh bin/synapse-config-migrator.sh synapse-i1.2/repository/conf/synapse.xml
```

<a id="upgrading--custom-extensions-and-api-changes"></a>

### Custom Extensions and API changes

Even though there is a migration tool it just takes care of your configuration and not
custom extensions that you have done for example like CustomMediators or Tasks
and so forth. There are some API changes that affect your custom extensions
unfortunately. This section tries to list all the public API changes which affects
the backward compatibility of the custom extensions that you have been running
with the 1.2 version of Synapse.

| Class | Method | Change Description |
| --- | --- | --- |
| [AbstractMediatorFactory](https://synapse.apache.org/apidocs/org/apache/synapse/config/xml/AbstractMediatorFactory.html) | createMediator(OMElement) | This was the method that you have been overwriting on the 1.2 version to implement a new custom mediator factory to build the mediator by looking at the XML configuration. On the 2.1 version you should be extending the [createSpecificMediator(OMElement, Properties)](https://synapse.apache.org/userguide/apidocs/org/apache/synapse/config/xml/AbstractMediatorFactory.html#createSpecificMediatororg.apache.axiom.om.OMElement20java.util.Properties) . Note that in the process of changing the method to be extended, the method [createMediator](https://synapse.apache.org/userguide/apidocs/org/apache/synapse/config/xml/AbstractMediatorFactory.html#createMediatororg.apache.axiom.om.OMElement20java.util.Properties) method has been changed to be final. From a users point of view of this interface he/she should be using the createMediator method which is what Synapse does. |
| [AbstractMediatorSerializer](https://synapse.apache.org/apidocs/org/apache/synapse/config/xml/AbstractMediatorSerializer.html) | serializeMediator(Mediator) | This was the method that you have been overwriting on the 1.2 version to implement a new custom mediator serializer to serialize to the XML Configuration by walking through the mediator properties. On the 2.1 version you should be extending the [serializeSpecificMediator(Mediator)](https://synapse.apache.org/userguide/apidocs/org/apache/synapse/config/xml/AbstractMediatorSerializer.html#serializeSpecificMediatororg.apache.synapse.Mediator) . Note that in the process of changing the method to be extended, the method [serializeMediator](https://synapse.apache.org/userguide/apidocs/org/apache/synapse/config/xml/AbstractMediatorSerializer.html#serializeMediatororg.apache.axiom.om.OMElement20org.apache.synapse.Mediator) method has been changed to be final. From a users point of view of this interface he/she should be using the serializeMediator method which is what Synapse does. |

Further to that if you have been using
[ServerManager](https://synapse.apache.org/apidocs/org/apache/synapse/ServerManager.html)
class you may have noticed that the class is no more a singleton and doesn't have
the static getInstance method. Also note that the common utilities like data
sources JMX and RMI registration stuff have been moved to a new module with
org.apache.synapse.commons package name.

On the configuration building front all entities are given a properties map to
construct its instance and that has been used to pass in any additional information
required like RESOLVE\_ROOT, or SYNAPSE\_HOME startup parameters. For example if you
look at the
[MediatorFactoryFinder](https://synapse.apache.org/apidocs/org/apache/synapse/config/xml/MediatorFactoryFinder.html)
class the
[getMediator](https://synapse.apache.org/apidocs/org/apache/synapse/config/xml/MediatorFactoryFinder.html#getMediatororg.apache.axiom.om.OMElement20java.util.Properties)
method is expecting a properties map apart from the OMElement argument.
It is safe to pass in a empty properties map if you are using these methods for
any testing purposes or even in cases where you do not resolve dependencies.

---

<a id="deployment"></a>

<!-- source_url: https://synapse.apache.org/userguide/deployment.html -->

<!-- page_index: 13 -->

<a id="deployment--deployment-guide"></a>

## Deployment Guide

This article explains the various approaches that can be taken to deploy an
Apache Synapse server instance. It provides information on each deployment
option along with their software requirements and steps that need to be carried
out.

<a id="deployment--contents"></a>

## Contents

- [Platform requirements](#deployment--platform_requirements)
- [Overview of available deployment options](#deployment--overview_of_available_deployment_options)
- [Stand-alone deployment](#deployment--stand-alone_deployment)
  - [Using the standard binary distribution](#deployment--using_the_standard_binary_distribution)
  - [Using Maven to build a custom distribution](#deployment--using_maven_to_build_a_custom_distribution)
- [WAR deployment](#deployment--war_deployment)

<a id="deployment--platform-requirements"></a>

## Platform requirements

Synapse requires Java 1.6 or higher and has been tested on Java runtime environments
from Sun, IBM and Apple.Synapse is used on various operation systems, including Linux, Mac OS X, Solaris, Windows and AIX, as well as mainframe environments. The recommended operation system for production use
is Linux since it offers a wider range of options to tune the TCP/IP stack. This is
important to optimize the performance of the NIO HTTP transport.

When selecting the environment for deployment, the following known issues should be taken into account:

- The synapse.bat and synapse.sh scripts included in the binary
  distribution use the -server option which is not supported by IBM's JRE.
  This problem can be easily solved by manually editing these scripts to
  remove the unsupported -server option. See
  [SYNAPSE-454](https://issues.apache.org/jira/browse/SYNAPSE-454)
  .
- In the past several issues related to subtle concurrency problems have been reported
  with the non-blocking HTTP transport (which is the recommended HTTP implementation
  for Synapse) when used on more "exotic" platforms. While this has been
  improved it is recommended to thoroughly test the HTTP transport before deploying
  Synapse in a production environment based on these platforms. Please don't hesitate
  to report any issues using JIRA or by posting a message on the mailing list.

<a id="deployment--overview-of-available-deployment-options"></a>

## Overview of available deployment options

Synapse can be deployed in two different ways:

- Stand-alone, i.e. as an independently managed Java process.
- As a J2EE application (WAR) deployed into a simple servlet container (e.g. Tomcat)
  or a full-featured J2EE application server.

Since Synapse doesn't rely on any container API, the features offered are the same in
both deployment scenarios, with very few exceptions:

- There is a minor issue that prevents classpath resources from being used in a
  WAR deployment. See [SYNAPSE-207](https://issues.apache.org/jira/browse/SYNAPSE-207)
  .
- When deployed as a WAR file, Synapse can be configured with the standard Axis2
  servlet based HTTP transport: while the recommended HTTP implementation for Synapse
  is the NIO HTTP transport, there might be situations where it is preferable or
  mandatory to use the HTTP protocol implementation of the application server.

In some scenarios Synapse is used to proxy services that are deployed themselves on
an application server. In these cases it would be interesting to deploy Synapse on
the same application server and use an in-VM transport instead of HTTP to communicate
with these services. Note that for the moment no production-grade implementation of
this type of transport exists yet for Axis2, but this might change in the future.

Since the features offered are almost the same, the differences between the two
deployment options are mainly related to packaging and operational considerations:

- Many IT departments prefer deploying J2EE applications than managing stand-alone
  Java processes, because this allows them to leverage the management and monitoring
  facilities offered by the application server.
- If the use case relies on JNDI resources such as JMS connection factories,
  JDBC data source and transactions it might be easier to set up and configure these
  resources when Synapse is deployed directly on the application
  server that hosts these resources.

<a id="deployment--stand-alone-deployment"></a>

## Stand-alone deployment

<a id="deployment--using-the-standard-binary-distribution"></a>

### Using the standard binary distribution

The easiest way to get started with a stand-alone deployment is using the standard
binary distribution ZIP or tarball (see [download.html](https://synapse.apache.org/download.html)).
It already contains everything that is needed to run Synapse stand-alone and you
only need to customize it according to your requirements:

- Place your mediation configuration in repository/conf/synapse-config
  directory.
- Place any additional files such as WSDL files, endpoint definitions, etc.
  referenced by your configuration in the repository directory.
- Customize repository/conf/axis2.xml
  to enable and disable transports according to your needs.
- Add any additional libraries required by your mediation to the
  libdirectory. Alternatively modify repository/conf/wrapper.conf
  to add directories and JAR files to the classpath.
- Add any required modules to repository/modules.
- If necessary, modify lib/log4j.properties to configure logging.

Since the standard binary distribution also contains samples and documentation, you might want to remove the following folders:

- docs
- repository/conf/sample
- samples

The bin directory contains Unix and Windows scripts to run Synapse:

- synapse.sh and synapse.bat allow to run Synapse in non
  daemon mode.
- synapse-daemon.sh is a Sys V init script that can be used on Unix
  systems to start and stop Synapse in daemon mode.
- install-synapse-service.bat and uninstall-synapse-service.bat
  can be used on Windows to install Synapse as an NT service.

<a id="deployment--using-maven-to-build-a-custom-distribution"></a>

### Using Maven to build a custom distribution

Building a custom Synapse package based on the standard binary distribution is a
manual process and this has some drawbacks:

- The JAR files required to run Synapse must be selected manually and it is not easy to identify unused JARs
  that could be safely removed.
- The process is not suitable if there is a requirement for strict configuration management. In particular:
  - Because of the large number of JAR files, managing the artifacts using
    a source control repository is not practical.
  - The process is not repeatable and there is no way to go back to a
    previous version of the artifacts.
- When upgrading to a newer version of Synapse (or when working with snapshot
  versions), it is necessary either to manually replace the JARs in the current
  package or to start again from a new version of the standard binary
  distribution.
- If Synapse needs to be deployed with slightly different configurations in
  multiple environments (e.g. test and production), the corresponding packages
  need to be prepared manually.

Note that these problems not only arise in the development and maintenance phases
of a project, but also when doing proof of concepts that you want to keep in a safe
place for later reuse. One approach to overcome these difficulties is to use Maven
to assemble a custom package. When used correctly, this approach solves all of the
issues identified above. In particular Maven's dependency management together with
the excellent [assembly plugin](http://maven.apache.org/plugins/maven-assembly-plugin/)
can be used to automatically select the relevant JARs to include and pull them
from Maven repositories. The remaining artifacts required to assemble the package
can then be easily stored in a source control repository.

Synapse provides a Maven archetype that allows to set up this kind of project in
only a few simple steps. To begin with, change to the directory where you want to
create the project and issue the following command:

mvn archetype:generate -DarchetypeCatalog=http://synapse.apache.org

In case of problems, you can try to use the latest version of the archetype catalog:

mvn archetype:generate -DarchetypeCatalog=http://svn.apache.org/repos/asf/synapse/trunk/java/src/site/resources

Finally, if you have build Synapse from sources, you don't need to specify a
catalog at all: the archetype is added automatically to the local catalog during
the build.

In any case, when prompted by Maven, select synapse-package-archetype
for the Synapse version you want to use. In the next step enter the values for
groupId, artifactId and version for your project. You
will also be prompted for a package name. Since the archetype doesn't contain any source
code, this value is irrelevant and you can continue with the default value.

At this stage a Maven project has been created in a sub-directory with the same
name as the artifactId specified previously. You should now customize this
projects according to your needs:

- Add your mediation configuration to repository/conf/synapse-config
  directory.
- Customize the dependencies in pom.xml. In particular if additional
  transports such as JMS are needed, add the required dependencies here. Additional
  Axis2 modules should also be added here.
- Enable and configure additional transports in repository/conf/axis2.xml.
- Place any other files referenced by mediation configuration into the
  repository directory.

The project is built as usual with the following command:

mvn package

This will create a ZIP file (in the target directory) containing
everything that is needed to run your custom Synapse configuration. You only
need to extract it and use the appropriate script in the bin
directory to start Synapse.

<a id="deployment--war-deployment"></a>

## WAR deployment

Synapse provides a standard WAR file that can be used to deploy mediation on a servlet
container or on a J2EE application server. Note that this WAR file is not part of the
downloadable distributions. It can be retrieved from the following location:

- <http://repo1.maven.org/maven2/org/apache/synapse/synapse-war/>
  for released versions.
- <https://builds.apache.org/view/All/job/Synapse%20-%20Trunk/lastBuild/org.apache.synapse$synapse-war/>
  for snapshot versions.

Customization of the Web application is similar to the stand-alone option, but the
default directory structure is different:

- synapse.xml and axis2.xml are placed into the WEB-INF/conf
  directory. All other files referenced by your mediation should go to the
  WEB-INF/repository
  directory.
- Additional libraries must be placed into the standard WEB-INF/lib
  directory.
- Axis2 modules are located in repository/modules.
- log4j.properties is located in WEB-INF/classes.

---

<a id="faq"></a>

<!-- source_url: https://synapse.apache.org/userguide/faq.html -->

<!-- page_index: 14 -->

<a id="faq--apache-synapse-faqs"></a>

## Apache Synapse FAQs

Welcome to Apache Synapse FAQs.

<a id="faq--general-generalapache-synapse-questions-non-technical"></a>

## General(GeneralApache Synapse questions - Non technical)

1. What is Apache Synapse?
   - Apache Synapse is a lightweight and high-performance Enterprise Service
     Bus (ESB).
2. What makes Apache Synapse unique?
   - Apache Synapse is fast and able to handle thousands of concurrent
     connections
     with constant memory usage. It comes with a rich set of mediators to
     support almost any integration scenario out of the box. It is also
     easily
     extensible and highly customizable.
3. What is the license?
   - Apache Synapse comes with Apache 2.0 licence.

<a id="faq--mediation-questions-related-to-sequences-endpoints-proxies-etc"></a>

## Mediation(Questions related to sequences, endpoints, proxies etc)

1. What is a proxy service?
   - A proxy service is a virtual service hosted on the ESB. It can accept
     requests from service clients, just like a real Web Service. A proxy
     service can process requests and forward them to an actual Web Service
     (back end service) to be further processed. The responses coming back
     from
     the back end service can be routed back to the original client. Proxy
     services are mostly used to expose an existing service over a different
     transport, format or QoS configuration.
2. What is a mediator?
   - A mediator is the basic message processing unit in the ESB. A mediator
     can take a message, carry out some predefined actions on it and output
     the modified message. Apache Synapse ships with a range of mediators capable
     of carrying out various tasks on input messages.
3. What is a sequence?
   - A sequence is an ordered list of mediators (a mediator chain). When a
     sequence is given a message, it will go through all the mediators in the
     sequence. A sequence can also handover messages to other sequences.
4. What is an Endpoint?
   - A logical representation of an actual endpoint or a group of endpoints
     (i.e. Load Balancing and Fail Over).
5. What are Local Entries?
   - Local entries can be used to hold various configuration elements
     required by sequences and proxy services. Usually they are used to hold
     WSDLs, XSDs, XSLT files etc. A local entry can contain XML content as
     well
     as plain text content. A local entry can be configured to load content
     from a remote file too.
6. What is a Message Mediation?
   - Managing and transforming the messages flowing between the client and a
     service in an enterprise.
7. What is Message Mediation?
   - Mediating messages coming into a specific service by specifying the
     target URI as a Synapse mediation service.
8. What is Service Mediation?
   - Mediating messages coming into a specific service by specifying the
     target URI as a Synapse mediation service.
9. What is a Message Store?
   - Message Store is the storage for ESB messages. It can be an in-memory
     store
     or can be JMS store with an external Message Broker. You can always plug
     your
     own message store implementations as well.
10. What is a Message Processor?
    - Message processor can be used to implement different messaging and
      integration patters along with Message stores. Message processors will
      consume
      the messages in message stores and do the processing of them.
11. What is a Template?
    - ESB Templates try to minimize this redundancy by creating prototypes
      that
      users can re-use and utilize as and when needed. This is very much
      analogous
      to classes and instances of classes where-as, a template is a class that
      can be used to wield instance objects such as templates and endpoints.
12. What is the REST Api?
    - REST Api can be used to mediate HTTP POST, GET, PUT and DELETE request
      through Synapse and to integrate various RESTful services.
13. Can Endpoint perform error handling?
    - Yes. Endpoints can do error handling. User can configure the behavior
      of an endpoints when it faced to a erroneous situation.

<a id="faq--transports-transport-related-questions"></a>

## Transports(Transport related questions)

1. What are the transports supported by the Apache Synapse?
   - HTTP, HTTPS, VFS based file transport, FIX, Hessian, HL7,UDP, JMS, Mail,
     TCP, XMPP
2. Do I need an external JMS broker for the JMS transport?
   - Yes, Apache Synapse requires an external JMS broker like Apache ActiveMQ
3. Does Apache Synapse support two way JMS scenario (request/response) ?
   - Yes, you can refer sample 264 which demonstrates exactly the JMS
     request/response scenario.
4. What is the Passthrough transport?
   - This is the default HTTP transport used by Apache Synapse. HTTP PassThrough Transport
     is a non-blocking HTTP transport implementation based on HTTP Core NIO and specially
     designed for streaming messages. It is similar to the old message relay transport,
     but it does not care about the content type and simply streams all received messages
     through. It also has a simpler and cleaner model for forwarding messages back and forth.
     It can be used as an alternative to the NHTTP transport.
5. What is the NHTTP transport?
   - NHTTP stands for non-blocking HTTP. NHTTP transport uses the Java Non-blocking I/O API.
     This allows the NHTTP transport to scale into handling hundreds of connections
     without blocking the threads. The server worker threads used by the NHTTP
     transport do not get blocked on I/O until the Synapse receives responses
     for the already forwarded requests. Therefore Apache Synapse can accept
     more concurrent connections and requests than most HTTP server products.
6. What is the underlying HTTP library used by the NHTTP/Passthrough transport?
   - NHTTP transport uses the Apache Http Core NIO library underneath. This
     library provides low level I/O handling and HTTP level detail handling.

---
