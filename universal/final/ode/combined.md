# Apache ODE – User Guide

## Navigation

- Installation
  - [WAR Deployment](#war-deployment)
  - [Upgrading ODE](#upgrading-ode)
- Using ODE
  - [Creating a Process](#creating-a-process)
  - [Process Versioning](#process-versioning)
  - [Management API](#management-api)
  - [Instance Replayer](#instance-replayer)
  - [ODE Execution Events](#ode-execution-events)
  - [Endpoint References](#endpoint-references)
  - [WSDL 1.1 HTTP Binding Support](#wsdl-11-http-binding-support)
  - [WSDL 1.1 Extensions for REST](#extensions-wsdl-11-extensions-for-rest)
  - [BPEL Extensions](#extensions)
  - [Instance Data Cleanup](#instance-data-cleanup)
  - [Direct Process-to-Process Communication](#direct-process-to-process-communication)
  - [Stateful Exchange Protocol](#developerguide-stateful-exchange-protocol)
  - [Activity Failure and Recovery](#extensions-activity-failure-and-recovery)
  - [XQuery Extensions](#extensions-xquery-extensions)
  - [Custom XPath functions](#custom-xpath-functions)
  - [Atomic Scopes Extension for BPEL](#developerguide-atomic-scopes-extension-for-bpel)
- How To
  - [ODE JBI and Axis2 properties overview](#ode-jbi-and-axis2-properties-overview)
  - [Controlling ODE's Memory Footprint](#controlling-odes-memory-footprint)
  - [Endpoint Configuration](#endpoint-configuration)
  - [HTTP Authentication](#http-authentication)
  - [Using a JNDI DataSource under ServiceMix JBI](#using-a-jndi-datasource-under-servicemix-jbi)
  - [Writing BPEL Test Cases](#writing-bpel-test-cases)
  - [WS-Security in ODE](#ws-security-in-ode)
  - [Use Assign to build messages](#use-assign-to-build-messages)
- End of Life
  - [JBI Deployment](#jbi-deployment)
  - [SMX4 OSGi Deployment](#smx4-osgi-deployment)
- [Getting ODE](#getting-ode)
- [Documentation](#userguide)
  - [User Guide](#userguide)
  - [Developer Guide](#developerguide)
  - [WS-BPEL Compliance](#ws-bpel-20-specification-compliance)
  - [WS-BPEL Extensions](#extensions)
  - [FAQ](#faq)
  - [Roadmap](#roadmap)
  - [Resources & Services](#resource-services)
- Contributing
  - [Mailing Lists](#mailing-lists)
  - [Building ODE](#developerguide-building-ode)
  - [Source Code](#developerguide-source-code)
  - [Contributors](#contributors)
- Configuring ODE in Tomcat with a MySQL database
  - [ODE schema](#ode-schema)
- Other pages
  - [assign](#assign)
  - [BPEL Management API Specification](#bpel-management-api-specification)
  - [Architectural Overview](#developerguide-architectural-overview)
  - [Apache ODE – Extension Activities & Extensible Assign Operations](#extensions-extension-activities-extensible-assign-operations)
  - [External Variables](#extensions-external-variables)
  - [Apache ODE – Flexible Assigns](#extensions-flexible-assigns)
  - [Apache ODE – Headers Handling](#extensions-headers-handling)
  - [Implicit Correlations](#extensions-implicit-correlations)
  - [Iterable ForEach](#extensions-iterable-foreach)
  - [Process Contexts](#extensions-process-contexts)
  - [Apache ODE – RESTful BPEL, Part I](#extensions-restful-bpel-part-i)
  - [RESTful BPEL, Part II](#extensions-restful-bpel-part-ii)
  - [XPath Extensions](#extensions-xpath-extensions)
  - [Required Third-Party Libraries](#required-third-party-libraries)
  - [Apache ODE – sendsoap Command](#sendsoap-command)
  - [Apache ODE – WS-BPEL 2.0](#ws-bpel-20)

## Content

<a id="war-deployment"></a>

<!-- source_url: https://ode.apache.org/war-deployment.html -->

<!-- page_index: 1 -->

# WAR Deployment

---

<a id="upgrading-ode"></a>

<!-- source_url: https://ode.apache.org/upgrading-ode.html -->

<!-- page_index: 2 -->

<a id="upgrading-ode--overview"></a>

## Overview

> [!NOTE]
> <a id="upgrading-ode--you-shall-backup"></a>

>
> > [!NOTE]
> > #### You shall backup

ODE upgrade procedures usually consist in:

- backing up your database
- checking your backup
- double-checking your backup
- running the required SQL upgrade script
- deploying your new ODE war.
- copying all the previous configuration and deployed processes (with the corresponding markers).

<a id="upgrading-ode--from-ode-136-137"></a>
<a id="upgrading-ode--from-ode-1.3.6-1.3.7"></a>

## From ODE 1.3.6 - 1.3.7

Migration is necessary from 1.3.6, read the migration script available [here](https://github.com/apache/ode/blob/APACHE_ODE_1.3.7/schema-updates/migrate-ode-1.3.6-to-1.3.7.sql).

<a id="upgrading-ode--from-ode-134-136"></a>
<a id="upgrading-ode--from-ode-1.3.4-1.3.6"></a>

## From ODE 1.3.4 - 1.3.6

ODE 1.3.4, 1.3.5 and 1.3.6 share the same schema definitions.

<a id="upgrading-ode--from-133-to-134"></a>
<a id="upgrading-ode--from-1.3.3-to-1.3.4"></a>

## From 1.3.3 to 1.3.4

First, apply SQLs to denormalize LARGE\_DATA table from [here](https://issues.apache.org/jira/browse/ODE-694)

Then, please apply following updates:

```
alter table BPEL_XML_DATA add SIMPLE_VALUE varchar2 (255 ); create table ODE_JOB_BAK as select * from ODE_JOB;
alter table ODE_JOB add instanceId number (37 ); alter table ODE_JOB add mexId varchar (255 ); alter table ODE_JOB add processId varchar (255 ); alter table ODE_JOB add type varchar (255 ); alter table ODE_JOB add channel varchar (255 ); alter table ODE_JOB add correlatorId varchar (255 ); alter table ODE_JOB add correlationKeySet varchar (255 ); alter table ODE_JOB add retryCount int;
alter table ODE_JOB add inMem int;
alter table ODE_JOB add priority int;
alter table ODE_JOB add detailsExt blob;
update ODE_JOB oj set detailsExt =(select details from ODE_JOB where jobid =oj.jobid ); alter table ODE_JOB drop column details;
```

<a id="upgrading-ode--from-132-to-133"></a>
<a id="upgrading-ode--from-1.3.2-to-1.3.3"></a>

## From 1.3.2 to 1.3.3

None

<a id="upgrading-ode--from-12-to-132"></a>
<a id="upgrading-ode--from-1.2-to-1.3.2"></a>

## From 1.2 to 1.3.2

If you're currently using ODE 1.2 and are upgrading to 1.3.2, please run the following queries.

<a id="upgrading-ode--for-openjpa-database-schema"></a>

### For OpenJPA database schema

```
create table ODE_SCHEMA_VERSION (VERSION integer ); insert into ODE_SCHEMA_VERSION values (5 ); alter table ODE_MESSAGE_EXCHANGE add column (SUBSCRIBER_COUNT integer ); alter table ODE_MESSAGE_ROUTE add column (ROUTE_POLICY character varying (255 ));
```

<a id="upgrading-ode--for-hibernate-database-schema"></a>

### For Hibernate database schema

(Mind the table names)

```
create table ODE_SCHEMA_VERSION (VERSION integer ); insert into ODE_SCHEMA_VERSION values (5 ); alter table BPEL_MESSAGE_EXCHANGE add column (SUBSCRIBER_COUNT integer ); alter table BPEL_SELECTORS add column (ROUTE_POLICY character varying (255 ));
```

<a id="upgrading-ode--from-11-to-12"></a>
<a id="upgrading-ode--from-1.1-to-1.2"></a>

## From 1.1 to 1.2

The upgrade path from 1.1 to 1.2 is relatively simple as there haven't any major change in the database or runtime models. Still, if you use the Hibernate database schema, one column has been added so you will need to execute the following upgrade script (make sure to *backup before* to prevent any data loss):

```
alter table BPEL_SELECTORS add column (PROC_TYPE varchar (255 )); update BPEL_PROCESS p,BPEL_CORRELATOR c,BPEL_SELECTORS s set s.PROC_TYPE =('{' + p.type_ns + '}' + p.type_name) where s.CORRELATOR =c.CID and c.PROCESS_ID =p.PROCID;
```

The update statement is only necessary if you have currently running instances. Note that if you're using the default OpenJPA database schema, no database modifications are necessary. Once this is done, it's fairly simple:

- Redeploy your new ODE 1.2 WAR.
- Copy all the previous configuration and deployed processes (with the corresponding markers).

That's it!

---

<a id="creating-a-process"></a>

<!-- source_url: https://ode.apache.org/creating-a-process.html -->

<!-- page_index: 3 -->

<a id="creating-a-process--overview"></a>

## Overview

<a id="creating-a-process--deploying-a-process-in-ode"></a>

## Deploying a Process in ODE

Each deployment is a directory with all relevant deployment artifacts. At the minimum it will contain the deployment descriptor, one or more process definitions (BPEL or .cbp), WSDL and XSDs (excluding those compiled into the .cbp). It may also contain other files, such as SVGs or XSLs. The deployment descriptor is a file named deploy.xml (see the next paragraoh for its description).

During deployment, the process engine loads all documents from the deployment descriptor. Loading documents allow it to reference processes, service and schema definitions using fully qualified names, and import based on namespaces instead of locations.

To deploy in ODE, just copy the whole directory containing your artifacts (the directory itself, not only its content) in the path `%DEPLOYMENT_ROOT%/WEB-INF/processes` (in Tomcat it would be `%TOMCAT_HOME%/webapps/ode/WEB-INF/processes`).

<a id="creating-a-process--deployment-descriptor"></a>

## Deployment Descriptor

To deploy your process in ODE you will need to create a simple deployment descriptor with basic information. The deploy.xml file configures one or several processes to use specific services. For each process, deploy.xml must supply binding information for partner links to concrete WSDL services. Every partner link used with a  activity must be matched with a  element, and every partnerLink used in an  activity must be matched with an  element in *deploy.xml* (unless that partnerLink has initializePartnerRole="false").

<a id="creating-a-process--formal-definition"></a>

## Formal definition

The XML schema describing ODE's deployment descriptor is available [here](http://svn.apache.org/viewvc/ode/trunk/bpel-schemas/src/main/xsd/dd.xsd?view=markup). The root element, deploy, contains a list of all deployed processes from the deployment directory:

```
<deploy>
    <process ...>*
        { other elements }
    </process>
</deploy>
```

Each process is identified by its qualified name and specifies bindings for provided and invoked services:

```
<process name = QName  fileName = String?  bpel11wsdlFileName = String? >
    (<provide> | <invoke>)*
    { other elements }
</process>
```

Each process element must provide a `name` attribute with the qualified name of the process. Optionally, a `fileName` attribute can be used to specify the location of the BPEL process definition (the .bpel file). The `fileName` attribute does not need to be provided unless non-standard compilation options are used or the `bpel11wsdlFileName` attribute is used to specify a WSDL document for a BPEL 1.1 process.

Each `<process>` element must enumerate the services provided by the process and bind each service to an endpoint. This is done through `<provide>` elements which associates `partnerLink`s with `endpoint`s:

```
<provide
partnerLink=
NCName
> <service name =QName port =NCName? > </provide>
```

Note, that only one partnerLink can be bound to any specified endpoint.

The port attribute can be used to select a particular endpoint from the service definition.

<a id="creating-a-process--examples"></a>

## Examples

A very simple process that would only be invoked would use a deploy.xml very similar to:

```
<deploy xmlns="http://www.apache.org/ode/schemas/dd/2007/03" 
    xmlns:pns="http://ode/bpel/unit-test" xmlns:wns="http://ode/bpel/unit-test.wsdl">
    <process name="pns:HelloWorld2">
        <active>true</active>
        <provide partnerLink="helloPartnerLink">
            <service name="wns:HelloService" port="HelloPort"/>
        </provide>
    </process>
</deploy>
```

See the complete example [here](https://github.com/apache/ode/tree/master/distro/src/examples-war/HelloWorld2).

A deployment including two processes invoking each other and whose execution would be triggered by a first message would look like:

```
<deploy xmlns="http://www.apache.org/ode/schemas/dd/2007/03" xmlns:main="http://ode/bpel/unit-test" 
        xmlns:mws="http://ode/bpel/unit-test.wsdl" xmlns:resp="http://ode/bpel/responder">

    <process name="main:MagicSessionMain">
        <provide partnerLink="executePartnerLink">
            <service name="mws:MSMainExecuteService" port="MSExecutePort"/>
        </provide>
        <provide partnerLink="responderPartnerLink">
            <service name="mws:MSMainService" port="MSMainPort"/>
        </provide>
        <invoke partnerLink="responderPartnerLink">
            <service name="mws:MSResponderService" port="MSResponderPort"/>
        </invoke>
    </process>
    <process name="resp:MagicSessionResponder">
        <type>resp:MagicSessionResponder</type>
        <provide partnerLink="mainPartnerLink">
            <service name="mws:MSResponderService" port="MSResponderPort"/>
        </provide>
        <invoke partnerLink="mainPartnerLink">
            <service name="mws:MSMainService" port="MSMainPort"/>
        </invoke>
    </process>
</deploy>
```

See the complete example [here](https://github.com/apache/ode/tree/master/distro/src/examples-war/MagicSession).

<a id="creating-a-process--additional-settings"></a>

## Additional settings

<a id="creating-a-process--in-memory-execution"></a>

### In memory execution

For performance purposes, you can define a process as being executed only in-memory. This greatly reduces the amount of generated queries and puts far less load on your database. Both persistent and non-persistent processes can cohabit in ODE.

To declare a process as in-memory just add an in-memory element in your deploy.xml:

```
<process name="pns:HelloWorld2">
    <in-memory>true</in-memory>
    <provide partnerLink="helloPartnerLink">
        <service name="wns:HelloService" port="HelloPort"/>
    </provide>
</process>
```

Be aware that in-memory executions introduces many restrictions on your process and what it can do. The instances of these processes can't be queried by using the [Management API](#management-api). The process definition can only include one single receive activity (the one that will trigger the instance creation).

<a id="creating-a-process--user-defined-process-properties"></a>

### User-defined process properties

User-defined process properties provide means to configure process models and their instances. They are either statically declared and set in the deployment descriptor `deploy.xml` or can be set using the process management API. All instances of a process model share the same set of process properties. If a process property changes, it changes for all instances.

A process property is identified by a QName and can carry a string as value. To set a process property statically in the deployment descriptor, add the following snippet to your `deploy.xml`:

```
<process name="pns:HelloWorld2">
    ...
    <property xmlns:loan="urn:example" name="loan:loanThreshold">4711</property>
    ...
</process>
```

It is also possible to set or change a property by calling the PM API function `setProcessProperty(final QName pid, final QName propertyName, final String value)`.

Once set, process properties can be used in two different ways:
\* Using XPath in process models
\* Using Java in ODE extensions

For instance, instead of hard coding the amount of money that triggers an in-depth check in a loan approval process, you could read a process property instead. That way you can reconfigure your process without having to redeploy the process again.

To read process properties in a BPEL process, you can use the non-standard XPath extension `bpws:process-property(propertyName)`, e.g. in a transition condition or in an assign activity:

```
...<assign> <copy> <from xmlns:loan="urn:example">bpws:process-property(loan:loanThreshold)</from> <to>$threshold</to> </copy> </assign> ...
```

---

<a id="process-versioning"></a>

<!-- source_url: https://ode.apache.org/process-versioning.html -->

<!-- page_index: 4 -->

<a id="process-versioning--introduction"></a>

## Introduction

Before starting on what process versioning exactly does, let's see what the world (or at least ODE) would be without versioning. It will be much more easier for you to understand the solution after fully seeing the problem.

So you're starting using ODE and you've just designed you first business process. It's all nice and dandy and works perfectly. It works so well that you let your users start using it. It's not really production but you know, release early, release often, so let's see what users think of it. After a couple of days you realize that a couple of steps are missing, you add them in your process and once again, it executes smoothly. So let's see what our users think of the improvement! Next thing you know, your phone starts ringing and the user on the other side is most likely pretty upset. What happened?

So when you start using a process, executions for it are created, running processes if you like (also called process instances). Depending on the type of your business these could take a variable amount of time to execute but they're usually not instantaneous. So you have all these running processes sometimes doing things, sometimes just waiting there and all of a sudden, a brand new process definition replaces the original one all these executions have been using so far. What is a process engine to do with all these executions? Well, the most logic thing on earth: just nuke them all.

At this time there's no simple automated way to migrate a running process that has been executing using one definition to another new one. Computing the differences between the 2 definitions can be very complex and chances are that they're not even compatible! When you think of all these little tasks that are arranged just so to guarantee a perfect execution using the right data types, even minor alterations can get really tricky to apply on instances without blowing them all.

So here is the crude and sad truth: without having some versioning goodness in it, a process engine will always delete all the running instances when a new process definition is deployed.

<a id="process-versioning--how-versioning-works"></a>

## How Versioning Works

So if existing executions can't be migrated, what are you going to do with them? Well, just let them be. Versioning is based on the fact that, instead of directly updating the original process definition (leaving its instances to their dreadful fate), another new version of this definition is created. The older one is declared retired so no new executions can be started on that one, the new process is the one to be used now on. But running instances can still finish their job peacefully as the process they've been using to execute so far is still available and unchanged.

However ODE also has the concept of deployment bundles and supports 2 modes of deployment (remotely or manually directly on the filsesystem). Let's see how we get versioning to work under those conditions.

<a id="process-versioning--process-versioning-in-ode"></a>

### Process Versioning in ODE

In ODE, processes are deployed in what we call a deployment bundle. When you come down to it, it's just a zip file or a directory containing ODE's deployment descriptor ([deploy.xml](#creating-a-process--deployment-descriptor.html)), the processes BPEL and all the other goodies necessary for your BPEL to run (WSDLs, schemas, xsl stylesheets, you name it). And what ODE is using to know you're redeploying the same thing is the deployment bundle name.

So when you're redeploying a deployment bundle in ODE, here is what happens:

1. A new version is attributed to the bundle by incrementing the version number of the last deployment.
2. ODE checks whether the same bundle has been deployed before, *all* processes in those older bundles are retired.
3. The processes in the bundle are deployed in the engine using the same version number as the bundle itself.
4. New executions of all newly deployed processes are ready to be started.

There are a couple of additional remarks to make. The first is that the version is a single, sequentially incremented (which is to say that 3 comes after 2 and 2 comes after 1) number. *All* deployed bundles share the same sequence. The second thing to be aware of is that all processes in a bundle share the same version number and it's the number of their bundle.

Let's use the notation Foo-x(Bar-x, Baz-x) to represent the deployment of the Foo bundle in version x with processes Bar and Baz (sharing the same version number as just explained). The following illustrates a valid deployment sequence:

1. Coconut-1(Pineapple-1, Mango-1)
2. Orange-2(Tangerine-2)
3. Orange-3(Tangerine-3) => retires Orange-2(Tangerine-2)
4. Coconut-4(Pineapple-4, Mango-4) => retires Coconut-1(Pineapple-1, Mango-1)
5. Banana-5(Kiwi-5)

That's both tasty and healthy!

There's still a last question left unsolved: what happens if you take your bundle and deploy it under a different name with the same content. If you know a bit about source version control (like CVS or Subversion), that's very close to branching, only you might be executing two branches at the same time. As ODE can't find another bundle with the same, the processes will simply be deployed *without* retiring anything. You will effectively have twice the same process deployed under different versions. In that scenario you're supposed to know what you're doing.

If two identical process definitions are deployed at the same time, the behavior of the engine is unspecified. Which one of the two process will pick up the message? Who knows!? But this can be a very useful feature in specific cases when you want to deploy the same process twice (by same understand same name and same namespace) but the 2 definitions are actually different and enable different endpoints. This allows the parallel deployment of two different version of the same process provided that they don't overlap in their endpoint implementation.

<a id="process-versioning--remote-deployment-vs-hand-made-deployment"></a>
<a id="process-versioning--remote-deployment-vs.-hand-made-deployment"></a>

### Remote Deployment vs. Hand-Made Deployment

ODE supports 2 different ways of deploying bundles:

- using the deployment web service or JBI deployment.
- dropping bundles as directories under WEB-INF/processes.

The first way works just as described previously. Under the hood, your process bundle is a zip and it gets unzipped in a directory named bundlename-version. The version number is automatically generated by the engine. So you only need to provide the zip itself and a consistent bundle name.

For the second way, it's a bit more tricky. Because you're directly interacting with the deployment directory, you're allowed to create a bundle directory with any name you like (even not numbered at all). In that case ODE will still create a version number, it just won't be shown on the filesystem. However as it won't be able to find the previous bundle to retire, it will just deploy the new bundle along with all other processes, even if you already had some conflicting deployments. Basically, if you don't number your directories properly, every new deployment will be a new branch. In short, you don't really want to do that.

Another thing you're allowed to do with the file system is simply to replace (or remove and copy) all the files in the deployment bundle directory and remove the .deployed marker file to trigger redeployment. In that case ODE will simply consider you've undeployed and deployed the whole thing. So we get back to the situation where we don't have any versioning. Which can be very useful when you're in development mode because you usually don't care much about the running instances and you usually don't want to pile up versions of process definitions.

---

<a id="management-api"></a>

<!-- source_url: https://ode.apache.org/management-api.html -->

<!-- page_index: 5 -->

<a id="management-api--overview"></a>

## Overview

ODE has a complete management API to check which processes are deployed, running and completed instances, variables values and more. To see which methods are available, have a look at the [ProcessManagement](http://ode.apache.org/javadoc/org/apache/ode/bpel/pmapi/ProcessManagement.html) and [InstanceManagement](http://ode.apache.org/javadoc/org/apache/ode/bpel/pmapi/InstanceManagement.html) interfaces, the javadoc is pretty comprehensive.

These two interfaces are available as web services on the Axis2-based distribution. The corresponding WSDL can be found [here](http://svn.apache.org/repos/asf/ode/trunk/axis2/src/main/wsdl/pmapi.wsdl).

To invoke these two services, any web service client should work (in a perfect interoperable world). To ease the invocation when using an Axis2 client, a helper class is bundled in ode-axis2.jar: [ServiceClientUtil](http://ode.apache.org/javadoc/axis2/org/apache/ode/axis2/service/ServiceClientUtil.html). Usage examples are also available in test classes [InstanceManagementTest](http://svn.apache.org/repos/asf/ode/trunk/axis2/src/test/java/org/apache/ode/axis2/management/InstanceManagementTest.java) and [ProcessManagementTest](http://svn.apache.org/repos/asf/ode/trunk/axis2/src/test/java/org/apache/ode/axis2/management/ProcessManagementTest.java). Here is a short example demonstrating the invocation of the *listAllProcesses* operation:

```
ServiceClientUtil client =new ServiceClientUtil (); OMElement root =client.buildMessage ("listAllProcesses",new String [] {},new String [] {}); OMElement result =client.send (msg,"http://localhost:8080/ode/processes/ProcessManagement" );
```

We're using [XMLBeans](http://xmlbeans.apache.org/) to serialize and deserialize the returned values from/to XML so in the previous example. So if you'd like to have objects instead of an [Axiom](http://ws.apache.org/commons/axiom/index.html) structure in the previous example, just add the following lines of code:

```
ScopeInfoDocument scopeIndoDoc =ScopeInfoDocument.Factory.parse (result.getXMLStreamReader ());
```

You will need to include ode-bpel-api.jar in your classpath.

<a id="management-api--specification"></a>

## Specification

More details are available in the [Process Management API specification](#bpel-management-api-specification)

---

<a id="instance-replayer"></a>

<!-- source_url: https://ode.apache.org/instance-replayer.html -->

<!-- page_index: 6 -->

<a id="instance-replayer--introduction"></a>

## Introduction

With instance replayer, you are able to upgrade long running process instance to the newest version.

There's an ongoing discussion on apache.org in a feature request:

<https://issues.apache.org/jira/browse/ODE-483>.

<a id="instance-replayer--example"></a>

## Example

Attached are example service assembly [replayer-example-sa.zip](assets/files/replayer-example-sa_78f064c5a750df79.zip) and SoapUI project [replayer-example-soapui-project.xml](assets/files/replayer-example-soapui-project_2fddfc436b8f8816.xml).

<a id="instance-replayer--usage"></a>

## Usage

The basic use cases for replayer are:

1. migrate existing log running instances to newest process version given their communication (incoming and outgoing requests)
2. reproduce error scenarios between two instances of ODE (eg. production and development)

Replayer extends management api by 2 operations: replay and getCommunication (see pmapi.wsdl from ODE distribution).

In order to do 1, you invoke:

```
<pmap:replay xmlns:ns="http://www.apache.org/ode/pmapi/types/2006/08/02/">
  <replay>
     <ns:upgradeInstance>1234</ns:upgradeInstance>
  </replay>
</pmap:replay>
```

To do 2, you need to retrieve exchanges from instance (or instances) by:

```
<pmap:getCommunication xmlns:ns="http://www.apache.org/ode/pmapi/types/2006/08/02/">
  <getCommunication>
     <ns:iid>1234</ns:iid>
  </getCommunication>
</pmap:getCommunication>


<ns:restoreInstance>
    <ns:processType xmlns:p="http://sample.bpel.org/bpel/sample">p:OnEventCorrelation</ns:processType>
    <exchange xmlns="http://www.apache.org/ode/pmapi/types/2006/08/02/">
        <type>M</type>
        <createTime>2009-04-01T16:41:29.873+02:00</createTime>
        <service xmlns:sam="http://sample.bpel.org/bpel/sample">sam:OnEventCorrelationInit</service>
        <operation>initiate</operation>
        <in>
            <initiate xmlns:sam="http://sample.bpel.org/bpel/sample" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="">
                <payload>abc7</payload>
                <payload2>abc8</payload2>
            </initiate>
        </in>
        <out>
            <message xmlns="">
                <payload>test1</payload>
                <payload2/>
            </message>
        </out>
    </exchange>

    <exchange xmlns:ns="http://www.apache.org/ode/pmapi/types/2006/08/02/" xmlns="http://www.apache.org/ode/pmapi/types/2006/08/02/">
        <type>P</type>
        <createTime>2009-04-01T16:41:32.998+02:00</createTime>
        <service xmlns:sam="http://sample.bpel.org/bpel/sample">sam:OnEventCorrelation</service>
        <operation>initiate</operation>
        <in>
            <initiate xmlns:sam="http://sample.bpel.org/bpel/sample" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="">
                <payload>abc7</payload>
                <payload2>abc8</payload2>
            </initiate>
        </in>
        <out>
            <message xmlns="">
                <payload>test5</payload>
                <payload2/>
            </message>
        </out>
    </exchange>
</ns:restoreInstance>
```

Then, you execute replay on the other ODE installation to replicate instance:

```
<pmap:replay xmlns:ns="http://www.apache.org/ode/pmapi/types/2006/08/02/">
    <replay>
        <ns:restoreInstance>
            <ns:processType xmlns:p="http://sample.bpel.org/bpel/sample">p:OnEventCorrelation</ns:processType>
            ... exchanges
        </ns:restoreInstance>
    </replay>
</pmap:replay>
```

<a id="instance-replayer--time-control-in-bpel"></a>

## Time control in BPEL

To have control over time in bpel process, there is a new variable introduced, $ode:currentEventDateTime.
It's equivalent to $fn:current-dateTime() during live session and it's set to corresponding time in past during replaying.

<a id="instance-replayer--implementation-notes"></a>

## Implementation notes

- Replaying works in one transaction.
  You can migrate a few instances at once and get an error, which will roll back all work if an error occurrs in some case.
- Replayer extends BpelRuntimeContextImpl by ReplayerBpelRuntimeContextImpl class, which overrides methods like invoke and registerTimer to mock up communication.
- It implements ReplayerScheduler, which executes actions from past in time sorted order (exchanges given to replayer have createTime field, which is used for sorting)
- jobs from past are processed in ReplayerScheduler and jobs in future are registered in engine's scheduler
- In order to make integrity constraints, replaying returns error if:
  - a first incoming request is routed to an existing instance instead of creating a new one
  - next incoming request is routed to other instance or creates a new instance
  - there is some unprocessed communication while finishing replaying (for example if there is some outgoing exchange for service, which did not have INVOKE from replayed instance)
- It extends bpel-compiler and xpath evaluation by $ode:currentEventDateTime variable
- It adds currentEventDateTime property to BpelRuntimeContext
- It adds replayer package to bpel engine in bpel-runtime module
- It changes visibility of some fields and methods in bpel engine from private to protected and from optional to public.

---

<a id="ode-execution-events"></a>

<!-- source_url: https://ode.apache.org/ode-execution-events.html -->

<!-- page_index: 7 -->

<a id="ode-execution-events--overview"></a>

## Overview

ODE generates events to let you track what is exactly happening in the engine and produces detailed information about process executions. These events are persisted in ODE's database and can be queried using the [Management API](#management-api). The default behavior for the engine is to always generate all events for every executed action. However from a performance standpoint it's a good idea to deactivate some of the events you're not interested in (or even all of them). Inserting all these events generates a non-negligeable overhead.

<a id="ode-execution-events--event-types"></a>

## Event types

The following table details each event possibly generated by ODE:

| Event Name | Process/Scope | Description | Type |
| --- | --- | --- | --- |
| ActivityEnabledEvent | Scope | An activity is enabled (just before it's started) | activityLifecycle |
| ActivityDisabledEvent | Scope | An activity is disabled (due to dead path elimination) | activityLifecycle |
| ActivityExecStartEvent | Scope | An activity starts its execution | activityLifecycle |
| ActivityExecEndEvent | Scope | An activity execution terminates | activityLifecycle |
| ActivityFailureEvent | Scope | An activity failed | activityLifecycle |
| CompensationHandlerRegistered | Scope | A compensation handler gets registered on a scope | scopeHandling |
| CorrelationMatchEvent | Process | A matching correlation has been found upon reception of a message | correlation |
| CorrelationNoMatchEvent | Process | No matching correlation has been found upon reception of a message | correlation |
| CorrelationSetWriteEvent | Scope | A correlation set value has been initialized | dataHandling |
| ExpressionEvaluationFailedEvent | Scope | The evaluation of an expression failed | dataHandling |
| ExpressionEvaluationSuccessEvent | Scope | The evaluation of an expression succeeded | dataHandling |
| NewProcessInstanceEvent | Process | A new process instance is created | instanceLifecycle |
| PartnerLinkModificationEvent | Scope | A partner link has been modified (a new value has been assigned to it) | dataHandling |
| ProcessCompletionEvent | Process | A process instance completes | instanceLifecycle |
| ProcessInstanceStartedEvent | Process | A process instance starts | instanceLifecycle |
| ProcessInstanceStateChangeEvent | Process | The state of a process instance has changed | instanceLifecycle |
| ProcessMessageExchangeEvent | Process | A process instance has received a message | instanceLifecycle |
| ProcessTerminationEvent | Process | A process instance terminates | instanceLifecycle |
| ScopeCompletionEvent | Scope | A scope completes | scopeHandling |
| ScopeFaultEvent | Scope | A fault has been produced in a scope | scopeHandling |
| ScopeStartEvent | Scope | A scope started | scopeHandling |
| VariableModificationEvent | Scope | The value of a variable has been modified | dataHandling |
| VariableReadEvent | Scope | The value of a variable has been read | dataHandling |

The second column specifies wether an event is associated with the process itself or with one of its scopes. The event type is used for filtering events.

<a id="ode-execution-events--filtering-events"></a>

## Filtering events

<a id="ode-execution-events--filtering-at-the-process-level"></a>

### Filtering at the process level

Using ODE's deployment descriptor, it's possible to tweak events generation to filtrate which ones get created. First, events can be filtered at the process level using one of the following stanza:

```
<dd:process-events generate="all"/> <!-- Default configuration -->

<dd:process-events generate="none"/>

<dd:process-events>
    <dd:enable-event>dataHandling</dd:enable-event>
    <dd:enable-event>activityLifecycle</dd:enable-event>
</dd:process-events>
```

The first form just duplicates the default behaviour, when nothing is specified in the deployment descriptor, all events are generated. The third form lets you define which type of event is generated, possible types are: `instanceLifecycle`, `activityLifecycle`, `dataHandling`, `scopeHandling`, `correlation`.

<a id="ode-execution-events--filtering-at-the-scope-level"></a>

### Filtering at the scope level

It's also possible to define filtering for each scope of your process. This overrides the settings defined on the process. In order to define event filtering on a scope, the scope activity MUST have a name in your process definition. Scopes are referenced by name in the deployment descriptor:

```
<dd:deploy xmlns:dd="http://www.apache.org/ode/schemas/dd/2007/03">
    ...
    <dd:process-events generate="none">
        <dd:scope-events name="aScope">
            <dd:enable-event>dataHandling</bpel:enable-event>
            <dd:enable-event>scopeHandling</bpel:enable-event>
        </dd:scope-events>
        <dd:scope-events name="anotherScope">
            <dd:enable-event>activityLifecycle</bpel:enable-event>
        </dd:scope-events>
    </dd:process-events>
    ...
</dd:deploy>
```

Note that it's useless to enable an event associated with the process itself when filtering events on scopes.

The filter defined on a scope is automatically inherited by its inner scopes. So if no filter is defined on a scope, it will use the settings of its closest parent scope having event filters (up to the process). Note that what gets inherited is the full list of selected events, not each event definition individually.

<a id="ode-execution-events--event-listeners"></a>

## Event listeners

ODE lets you register your own event listeners to analyze all produced events and do whatever you want to do with them. To create a listener you just need to implement the [org.apache.ode.bpel.iapi.BpelEventListener](https://svn.apache.org/repos/asf/ode/trunk/bpel-api/src/main/java/org/apache/ode/bpel/iapi/BpelEventListener.java) interface.

Then add your implementation in the server's classpath and add a property in ode-axis2.properties giving your fully qualified implementation class name. Something like:

```
ode-axis2.event.listeners
=
com.compamy.product.MyOdeEventListener
```

Note: These events are generated in the same thread running a JTA transaction which is being executed to process the bpel activities.
Subscribed consumers of these events should look for releasing the executing thread as soon as possible. Holding on to the executing thread
would delay the transactions and the jobs executions within ODE. May be look towards asynchronous way of consuming these events.

Start your server and you're done!

---

<a id="endpoint-references"></a>

<!-- source_url: https://ode.apache.org/endpoint-references.html -->

<!-- page_index: 8 -->

<a id="endpoint-references--introduction"></a>

## Introduction

An endpoint reference holds information to call a service. The simplest endpoint reference is usually an URL but it can also be much more complex such as holding a message id, a reply-to address or custom properties.

In BPEL, endpoint references (aka EPRs) are modeled as partner link roles. When defining a partner link, two roles maybe defined, `myRole` and `partnerRole`:

```
<partnerLink
name=
"responderPartnerLink"
partnerLinkType=
"test:ResponderPartnerLinkType"
myRole=
"main"
partnerRole=
"responder"
initializePartnerRole=
"yes"
/>
```

Both `partnerRole` and `myRole` represent EPRs. So when assigning partner link roles or invoking partners, you are using EPRs behind the scene.

<a id="endpoint-references--ode-and-endpoint-references"></a>

## ODE and Endpoint References

<a id="endpoint-references--types-of-eprs"></a>

### Types of EPRs

The ODE runtime supports 4 types of EPRs:

- A simple URL or a URL in the location attribute of the binding. See [soap:address](http://www.w3.org/TR/wsdl#_soap:address) and [http:address](http://www.w3.org/TR/wsdl#_http:address) WSDL 1.1 binding.
- A [WS-Addressing](http://www.w3.org/TR/ws-addr-core/) [EndpointReference](http://www.w3.org/TR/ws-addr-core/#eprinfomodel).
- A [WSDL 1.1](http://www.w3.org/TR/wsdl) [service element](http://www.w3.org/TR/wsdl#_services).
- A [WSDL 2.0](http://www.w3.org/TR/wsdl20/) [endpoint element](http://www.w3.org/TR/wsdl20/#Endpoint).

We recommend the two first solutions to interact with the engine. The first one is just the easiest and for the case where you need more robustness, WS-Addressing is the most popular second choice.

To show you how these EPRs look like and how they can be assigned to partner links roles here are some examples:

```
<assign>

  <!-- Simple URL, without the wrapper -->
  <copy>
    <from>
      <literal>http://localhost:8080/ode/dynresponder</literal>
    </from>
    <to partnerLink="responderPartnerLink"/>
  </copy>

  <!-- Simple URL, wrapped in an soap:address element -->
  <copy>
    <from>
      <literal>
        <service-ref>
          <soap:address location="http://localhost:8080/ode/dynresponder"/>
        </service-ref>
      </literal>
    </from>
    <to partnerLink="responderPartnerLink"/>
  </copy>

  <!-- WS-Addressing EPR, without the wrapper -->
  <copy>
    <from>
      <literal>
        <wsa:EndpointReference xmlns:wsa="http://www.w3.org/2005/08/addressing">
          <wsa:To>http://localhost:8080/ode/dynresponder</wsa:To>
        </wsa:EndpointReference>
      </literal>
    </from>
    <to partnerLink="responderPartnerLink"/>
  </copy>

  <!-- WS-Addressing EPR, with the wrapper -->
  <copy>
    <from>
      <literal>
        <service-ref>
           <wsa:EndpointReference xmlns:wsa="http://www.w3.org/2005/08/addressing">
             <wsa:To>http://localhost:8080/ode/dynresponder</wsa:To>
           </wsa:EndpointReference>
        <service-ref>
      </literal>
    </from>
    <to partnerLink="responderPartnerLink"/>
  </copy>

  <!-- WSDL1.1 EPR, without the wrapper -->
  <copy>
    <from>
      <literal>
         <wsdl:service xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" name="DynService" targetNamespace="http://org.apache.ode/examples/dynservice">
           <wsdl:port name="DynPort">
                   <soap:address location="http://localhost:8080/ode/dynresponder"/>
           </wsdl:port>
         </wsdl:service> 
     </literal>
    </from>
    <to partnerLink="responderPartnerLink"/>
  </copy>

  <!-- WSDL2.0 EPR, with the wrapper -->
  <copy>
    <from>
      <literal>
         <service-ref>
         <wsdl:service xmlns:wsdl="http://www.w3.org/2006/01/wsdl" name="DynService" targetNamespace="http://org.apache.ode/examples/dynservice">
           <wsdl:port name="DynPort">
                   <soap:address location="http://localhost:8080/ode/dynresponder"/>
           </wsdl:port>
         </wsdl:service> 
         </service-ref>
     </literal>
    </from>
    <to partnerLink="responderPartnerLink"/>
  </copy>

</assign>
```

Normally BPEL requires wrapping EPRs with inside a `service-ref` element, however ODE relaxes this requirement for ease of use and increased interoperability with existing services. If the `service-ref` element is absent, the EPR is automatically wrapped inside one on the fly. Moreover, ODE automatically detects the different EPR types when assigning to a partner link role. If you need to use WS-Addressing sessions (@see appropriate page), then you will have to use `wsa:EndpointReference` EPRs.

You can just as well assign EPRs to/from variables to pass them around and enable more dynamic communication patterns.

<a id="endpoint-references--passing-endpoint-references"></a>

## Passing Endpoint References

To pass endpoint references around and manipulate them, you usually need to assigne them to variables. The EPR can then be sent in a message and reassigned to another partner link. This lets you model complex scenarii where you don't know the address of your partner beforehand or where you select one partner among many others.

The type of the variable that will hold your EPR defines the type of the EPR that it will contain. For example if you define a message in your WSDL document that looks like this:

```
<wsdl:message
name=
"EndpointMessage"
> <wsdl:part name="payload" element="xsd:string"/> </wsdl:message>
```

ODE will automatically put a simple URL EPR when you assign this message part:

```
<variable name="myEndpoint" messageType="resp:EndpointMessage"/>
...
<assign>
  <copy>
    <from partnerLink="mainPartnerLink" endpointReference="myRole"/>
    <to variable="myEndpoint" part="payload"/>
  </copy>
</assign>
```

Now if you want to manipulate a WS-Addressing EPR, the only thing you have to change in the above examples is the message part type. So your message will then look like this:

Once your EPR has been assigned to a variable and set, say, to another process, you just need to reassign it to a partner link `partnerRole` to use it:

```
<assign>
<copy>
<from
variable=
"eprmessage"
part=
"payload"
/>
<to
partnerLink=
"mainPartnerLink"
/>
</copy>
</assign>
<invoke
name=
"eprcall"
partnerLink=
"mainPartnerLink"
portType=
"resp:MSMainPortType"
operation=
"call"
inputVariable=
"eprmessage"
/>
```

For a complete example check [DynPartner](http://svn.apache.org/repos/asf/ode/trunk/distro/src/examples-war/DynPartner/) in the engine examples.

---

<a id="wsdl-11-http-binding-support"></a>

<!-- source_url: https://ode.apache.org/wsdl-11-http-binding-support.html -->

<!-- page_index: 9 -->

<a id="wsdl-11-http-binding-support--http-binding"></a>

## HTTP Binding

Since version [1.2](#getting-ode), ODE supports [HTTP Binding](http://www.w3.org/TR/wsdl#_http). ODE is almost fully compliant with the WSDL 1.1 spec. The few limitations are related to MIME types.
Actually only the following [MIME types](http://www.iana.org/assignments/media-types/) are supported:
1. Media types that represent [XML MIME entities](http://www.rfc-editor.org/rfc/rfc3023.txt). Basically any types matching `"text/xml"`, `"application/xml"` and `"\*+xml"`.
1. Non-XML types will be processed as Text, thus Text Media Types comes de facto but they may have a very limited set of usages.

[mime:multipartRelated](http://www.w3.org/TR/wsdl#_mime:multipartRelated), [mime:soap:body](http://www.w3.org/TR/wsdl#_mime:soap:body) and [mime:mimeXml](http://www.w3.org/TR/wsdl#_mime:mimeXml) are not supported.

Considering how unsuitable WSDL 1.1 HTTP Binding is for a large majority of services -- especially RESTful services -- a set of extensions is available.
All the details you want to know are [here](#extensions-wsdl-11-extensions-for-rest).

---

<a id="extensions-wsdl-11-extensions-for-rest"></a>

<!-- source_url: https://ode.apache.org/extensions/wsdl-11-extensions-for-rest.html -->

<!-- page_index: 10 -->

<a id="extensions-wsdl-11-extensions-for-rest--overview"></a>

## Overview

The [Resource-Oriented Architecture](http://en.wikipedia.org/wiki/Representational_State_Transfer) defines four concepts:

1. Resources
2. Their names (URIs)
3. Their representations
4. The link bet ween them

and four properties:

1. Addressability
2. Statelesness
3. Connectedness
4. A uniform interface

HTTP binding as defined in WSDL 1.1 is not well suitable to describe services implementing these concepts and properties, mainly because a port type may access 4 different locations/resources but with only one HTTP method.

To better describe RESTful services, and turn a port type into a "resource type", ODE brings a set of 4 extensions:

1. one HTTP method per operation (instead of one per binding)
2. a unique URI Template for all operations
3. access to HTTP headers
4. fault support

Further details below.

In this page, we use an imaginary blog service as a use case to illustrate and make things more palpable. We will focus on the resources defined by the following URI template: `http://blog.org/post/{id}`

Let's assume that such a resource accept four operations:

- GET to retrieve a post
- DELETE to delete it
- PUT to update the post
- POST to add a comment to a post

> [!NOTE]
> <a id="extensions-wsdl-11-extensions-for-rest--check-out-unit-tests"></a>

>
> > [!NOTE]
> > #### Check out unit tests!

<a id="extensions-wsdl-11-extensions-for-rest--one-verb-per-operation"></a>

### One verb per operation

According to the WSDL 1.1 specification, the verb describing the HTTP method has to be at [the binding level](http://www.w3.org/TR/wsdl#A4.3). Which implies that the same HTTP method is used by all operations of a given port type. But RESTful web services leverage HTTP methods as a uniform interface to describe operation on resources. So for instance, if you want to use the following HTTP operations -- GET, POST, PUT, DELETE -- for a given resource, four different bindings would be required. And consequently four port types and four ports. Quite verbose and unusable, isn't it?

So, this extension is to push down the HTTP verb at the operation level. And if an operation does not have its own verb, then the verb defined at the binding level will be used.
This extension is declared in the namespace: `http://www.apache.org/ode/type/extension/http`

Please note that ODE supports GET, POST, PUT, DELETE only.

```
<definitions ...xmlns:odex="http://www.apache.org/ode/type/extension/http" /> <!-- many wsdl elements are ommited to highlight the interesting part --> <binding name="blogBinding" type="blogPortType"> <operation name="GET"> <odex:binding verb="GET" /> </operation> <operation name="DELETE"> <odex:binding verb="DELETE" /> </operation> </binding> </definitions>
```

<a id="extensions-wsdl-11-extensions-for-rest--uri-template"></a>

### URI Template

A RESTful service exposed a set of resources, each of them being accessible through a uniform interface: HTTP methods for a web service. So we need a way to define four operations (at most) for a single resource.

Moreover it's very likely that the resource URI actually describes a set of resources. For instance, the set of posts contained in our imaginary blog: `http://blog.org/post/{post_id}`.

HTTP binding offers the [http:operation](http://www.w3.org/TR/wsdl#_http:operation)  element to set the path of an operation. While the service address is set in the [http:address](http://www.w3.org/TR/wsdl#_http:address) of the [wsdl:port](http://www.w3.org/TR/wsdl#_ports) element.
So one could imagine splitting the URL this way:

```
<definitions
...
xmlns:odex=
"http://www.apache.org/ode/type/extension/http"
/>
<service
name=
"blogService"
> <port name="blogPort" binding="blogPortType" > <http:address location="http://blog.org"/> </port> </service> <binding name="blogBinding" type="blogPortType" > <operation name="PUT" > <odex:binding verb="PUT"/> <http:operation location="post/(post_id)"/> <input> <http:urlReplacement/> </input> <output/> </operation> </binding> </definitions>
```

However, here 3 issues show up:

- the location is not accessible from the End Point Reference. *=> ODE cannot process it before invoking the external service.*
- [http:urlReplacement](http://www.w3.org/TR/wsdl#_http:urlReplacement) is only accepted for GET *=> what about the uniform interface?!*
- http:urlReplacement requires all parts of the operation input message to be mentioned in the operation location. Meaning that:
- => the resource id (in the present example) must be a part of the message.
- => no parts may be stored in the HTTP body. this conflicts with a PUT operation for instance. With a PUT you would like to set the id in the url and the resource data in the HTTP request body.

To solve this, ODE allows [http:operation](http://www.w3.org/TR/wsdl#_http:operation) elements to be omitted or empty, and the full resource URI to be set in a single place, the http:address element.

> [!NOTE]
> Please note that curly brackets '{}' are the preferred argument delimiters in URI templates. So that URLs can be dynamically composed using [compose-url, combine-url and expand-template XPath Functions](#extensions-restful-bpel-part-i--xpath-functions).

In addition, the http:urlReplacement is relaxed: all parts are *not* required in the URI template anymore. One part could go in the URI, another in the request body.

```
<definitions
...
xmlns:odex=
"http://www.apache.org/ode/type/extension/http"
/>
<service
name=
"blogService"
> <port name="blogPort" binding="blogPortType" > <!-- here is the full URI template, using curly brackets --> <http:address location="http://blog.org/post/{post_id}"/> </port> </service> <binding name="blogBinding" type="blogPortType" > <operation name="PUT" > <odex:binding verb="PUT"/> <!-- location attribute intentionally blank --> <http:operation location=""/> <input> <http:urlReplacement/> <!-- an additional part can be mapped to the request body even if urlReplacement is used--> <mime:content type="text/xml" part="post_content"/> </input> <output/> </operation> </binding> </definitions>
```

<a id="extensions-wsdl-11-extensions-for-rest--http-headers-manipulation"></a>

### HTTP Headers manipulation

HTTP protocal convey a lot of information in Request/Response Headers. Caching information, Content description for instance. All this data is completely left out by WSDL 1.1 HTTP Binding. To fix this, ODE provides a header element. This element can be used to insert a part or a static value into a given HTTP request header (standard or custom). And the way around, a HTTP request header into a part. Also note that all HTTP response headers are inserted into the message headers, and thus are available from the BPEL process.

```
<definitions
...
xmlns:odex=
"http://www.apache.org/ode/type/extension/http"
/>
<binding
name=
"blogBinding"
type=
"blogPortType"
> <operation name="PUT" > <odex:binding verb="PUT"/> <http:operation location=""/> <input> <http:urlReplacement/> <mime:content type="text/xml" part="post_content"/> <!-- set a standard request header from a part --> <odex:header name="Authorization" part="credentials_part"/> <!-- set a custom request header with a static value --> <odex:header name="MyCustomHeader" value="ode@apache.org"/> </input> <output> <mime:content type="text/xml" part="post_content"/> <!-- set 1 response header to a part --> <odex:header name="Age" part="age_part"/> </output> </operation> </binding> </definitions>
```

For every HTTP response, in addition to HTTP response headers, the [Status-Line](http://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html#sec6.1) is passed as a message header. To save some painful XPath string manipulations, the Status-line is already parsed into the following structure:

```
<Status-Line>
   <HTTP-Version>HTTP/1.1</HTTP-Version>
   <Status-Code>200</Status-Code>
   <Reason-Phrase>OK</Reason-Phrase>
   <!-- the original unaltered Status-Line -->
   <original>HTTP/1.1 200 OK</original>
</Status-Line>
```

So that you can write the following BPEL lines:

```
<assign>
    <copy>
        <from variable="postMsg" header="Status-Line"/>
        <to>$statusLine</to>
    </copy>
</assign>
<if>
    <condition>number($statusLine/Status-Code) > 200 and number($statusLine/Status-Code) < 300</condition>
    <assign>
         <copy>
             <from>'Request successful!!!'</from>
             <to>$outputVar.TestPart</to>
         </copy>
     </assign>
</if>
```

<a id="extensions-wsdl-11-extensions-for-rest--fault-support"></a>

### Fault Support

Another domain completely neglected by WSDL 1.1 HTTP Binding is Fault management. The word is not even mentioned in the [HTTP Binding section](http://www.w3.org/TR/wsdl#_http).
ODE allows you to bind a fault with HTTP Binding. If a [4xx or a 5xx](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4) is returned, the following logic is applied:

A failure is thrown if the code is one of these:

Status-Codes triggering a Failure

3xx Redirections

401\_UNAUTHORIZED

408\_REQUEST\_TIMEOUT

503\_SERVICE\_UNAVAILABLE

504\_GATEWAY\_TIMEOUT

> [!NOTE]
> Note that 3xx errors should be pretty rare since by default the first hundred redirections are followed. You can tweak this value by setting the property `http.protocol.max-redirects` in the [enpoint-configuration.properties](#endpoint-configuration) of your process.

Here what ODE does, if the status code is one of those listed in the next table (500, 501, etc):

- check that the operation has at least one fault in its abstract part, and one fault binding
- check that the Content-type header describes an xml document ('application/xml', 'application/atom+xml' etc)
- check that the body is not empty

If so far everything is fine, the HTTP response body is parsed into an xml document. Then the fault to be thrown is inferred from the qname of the response root element, i.e the fault having a message part matching the root element. This matching process is exactly the same as for a SOAP service.
If one of these steps fails, a failure is thrown.

| Status-Codes that may trigger a Fault | if the body element matches a fault declaration |
| --- | --- |
| 500\_INTERNAL\_SERVER\_ERROR | 407\_PROXY\_AUTHENTICATION\_REQUIRED |
| 501\_NOT\_IMPLEMENTED | 409\_CONFLICT |
| 502\_BAD\_GATEWAY | 410\_GONE |
| 505\_HTTP\_VERSION\_NOT\_SUPPORTED | 412\_PRECONDITION\_FAILED |
| 400\_BAD\_REQUEST | 413\_REQUEST\_TOO\_LONG |
| 402\_PAYMENT\_REQUIRED | 414\_REQUEST\_URI\_TOO\_LONG |
| 403\_FORBIDDEN | 415\_UNSUPPORTED\_MEDIA\_TYPE |
| 404\_NOT\_FOUND | 411\_LENGTH\_REQUIRED |
| 405\_METHOD\_NOT\_ALLOWED | 416\_REQUESTED\_RANGE\_NOT\_SATISFIABLE |
| 406\_NOT\_ACCEPTABLE | 417\_EXPECTATION\_FAILED |

Note that you can't bind a given fault to a specific status code.

```
<definitions ...
                  xmlns:odex="http://www.apache.org/ode/type/extension/http"/>

   <portType name="BlogPortType">
        <operation name="PUT">
            <input message="..."/>
            <output message="..."/>
            <fault name="UpdateFault" message="tns:UpdateFault"/>
        </operation>
    </portType>

    <binding name="blogBinding" type="blogPortType">
        <operation name="PUT">
             <odex:binding verb="PUT" />
             <http:operation location=""/>
             <input> ... </input>
             <output> ...  </output>
             <!-- fault binding -->
             <fault name="UpdateException">
                 <!-- name attribute is optional if there is only one fault for this operation -->
                 <!-- <odex:fault name="UpdateFault"/> -->
                 <odex:fault/>
             </fault>
        </operation>
    </binding>
</definitions>
```

---

<a id="extensions"></a>

<!-- source_url: https://ode.apache.org/extensions/ -->

<!-- page_index: 11 -->

<a id="extensions--overview"></a>

# Overview

ODE extends the [WS-BPEL](#ws-bpel-20) in areas that aren't covered by the spec. This page details these extensions.

- [Implicit Correlations](#extensions--bpelextensions-implicitcorrelations)
- [Activity Failure and Recovery](#extensions--bpelextensions-activityfailureandrecovery)
- [Extension Activities & Extensible Assign Operations](#extensions--bpelextensions-extensionactivities-extensibleassignoperations)
- [XPath Extensions](#extensions--bpelextensions-xpathextensions)
- [XQuery Extensions](#extensions--bpelextensions-xqueryextensions)
- [External Variables](#extensions--bpelextensions-externalvariables)
- [Headers Handling](#extensions--bpelextensions-headershandling)
- [RESTful BPEL, Part I](#extensions--bpelextensions-restfulbpel-parti)
- [RESTful BPEL, Part II](#extensions--bpelextensions-restfulbpel-partii)
- [Iterable ForEach](#extensions--bpelextensions-iterableforeach)
- [Flexible Assigns](#extensions--bpelextensions-flexibleassigns)
- [Process Contexts](#extensions--bpelextensions-processcontexts)

<a id="extensions--implicit-correlations"></a>

## [Implicit Correlations](#extensions-implicit-correlations)

BPEL process instances are stateful — therefore, a client interacting with the BPEL engine must identify the particular instance with which it intends to interact in all of its communications. The BPEL specification defines a mechanism — *correlation* — which allows the process designer to specify which parts of an incoming message (i.e. a message going from a client to the BPEL server) should be used to identify the target process instance. Correlation is a powerful mechanism — however it is a bit complicated and relies on "in-band" message data to associate a messages with a process instance.

To keep simple cases simple, ODE provides an alternative correlation mechanism — *implicit correlation* — that automatically handles correlation through "out-of-band" session identifiers. The mechanism is simple: a unique session identifier is associated with every every partner link instance. When a message is sent on a partner link, the session identifier is sent along with the message. The recipient is then able to use the received session identifier in subsequent communications with the process instance. Messages received by the BPEL engine that have a session identifier are routed to the correct instance (and partner link) by that session identifier.

[Read more](#extensions-implicit-correlations)

<a id="extensions--activity-failure-and-recovery"></a>

## [Activity Failure and Recovery](#extensions-activity-failure-and-recovery)

There are several types of error conditions. In this document we introduce a class of error condition called *failures*, distinct from *faults*, and describe how failures are caught and handled by the process engine.

For example, when the process is unable to perform DNS resolution to determine the service endpoint, it generates a failure. An administrator can fix the DNS server and tell the process engine to retry the activity. Had the DNS error been reported as a fault, the process would either terminate or require complex fault handling and recovery logic to proceed past this point of failure.

In short, failures shields the process from common, non-terminal error conditions while retaining simple and straightforward process definitions that do not need to account for these error conditions.

[Read more](#extensions-activity-failure-and-recovery)

<a id="extensions--extension-activities-extensible-assign-operations"></a>

## [Extension Activities & Extensible Assign Operations](#extensions-extension-activities-extensible-assign-operations)

Apache ODE provides a plug-in architecture for custom activity implementations and custom variable assignment logic. Such plug-ins can be registered to ODE and can be used according to the WS-BPEL 2.0 extensibility mechnisms (`<extensionActivity>` & `<extensionAssignOperation>`).

[Read more](#extensions-extension-activities-extensible-assign-operations)

<a id="extensions--xpath-extensions"></a>

## [XPath Extensions](#extensions-xpath-extensions)

Apache ODE extends the default XPath coverage provided by the WS-BPEL specification mostly by adding support for [XPath 2.0](http://www.w3.org/TR/xpath20/) and by offering a few utility extension functions to make some assignments easier.

[Read more](#extensions-xpath-extensions)

<a id="extensions--xquery-extensions"></a>

## [XQuery Extensions](#extensions-xquery-extensions)

Apache ODE extends the default XPath coverage provided by the WS-BPEL specification mostly by adding support for [XQuery 1.0](http://www.w3.org/TR/xquery/) and by offering a few utility extension functions to make some assignments easier.

[Read more](#extensions-xquery-extensions)

<a id="extensions--external-variables"></a>

## [External Variables](#extensions-external-variables)

External variables are an easy way to share data between the process and external systems, by treating those independent entities as BPEL variables that can be used in expressions and assignments. External variables may be records stored in the database, REST resources, etc.

[Read more](#extensions-external-variables)

<a id="extensions--headers-handling"></a>

## [Headers Handling](#extensions-headers-handling)

There are several situations where one would want to access headers form the wire format in their BPEL process. It could be to assign them to another message and pass them around or to execute some business logic that's header-dependent (often a bad idea but sometimes there's no choice). ODE supports the manipulation of wire format headers in two different ways.

[Read more](#extensions-headers-handling)

<a id="extensions--restful-bpel-part-i"></a>

## [RESTful BPEL, Part I](#extensions-restful-bpel-part-i)

Extends the invoke activity to handle RESTful Web services. This extension uses BPEL variables of type xsd:uri and xsd:string instead of partner links, and does away with the WSDL indirection, making it straightforward to develop processes that use RESTful Web services.

[Read more](#extensions-restful-bpel-part-i)

<a id="extensions--restful-bpel-part-ii"></a>

## [RESTful BPEL, Part II](#extensions-restful-bpel-part-ii)

Extends receive and onEvent to expose RESTful resources that. This extension adds the ability to declare and instantiate resources, and specific handling for the HTTP methods GET, POST, PUT and DELETE.

[Read more](#extensions-restful-bpel-part-ii)

<a id="extensions--iterable-foreach"></a>

## [Iterable ForEach](#extensions-iterable-foreach)

Extends the  activity so that the counter variable iterates over the items contained in a given sequence. This extension provides an alternative and more dynamic way of generating M branches, where M is the size of the binding sequence. The semantics of the  stays the same, in that the loop is deemed to be complete if B out of the M branches complete (successfully), where B is its actual value.

[Read more](#extensions-iterable-foreach)

<a id="extensions--flexible-assigns"></a>

## [Flexible Assigns](#extensions-flexible-assigns)

Extends the  activity so that it can be made to either ignore or insert data that is missing in the to-spec of a copy operation. This shortcut allows users to handle what would normally be fault scenarios, in a more graceful and intuitive way.

[Read more](#extensions-flexible-assigns)

<a id="extensions--process-contexts"></a>

## [Process Contexts](#extensions-process-contexts)

Extends BPEL and ODE to allow the circulation of transport metadata (like security tokens, correlation keys, or tracing informations) from messages to processes and then from processes to messages.

[Read more](#extensions-process-contexts)

---

<a id="instance-data-cleanup"></a>

<!-- source_url: https://ode.apache.org/instance-data-cleanup.html -->

<!-- page_index: 12 -->

<a id="instance-data-cleanup--rational"></a>

## Rational

During its execution, a process instance can accumulate a significant amount of data. The running process itself isn't that much of an issue, when the instance is done there's nothing left to execute. But the process data can be rather big, mostly because of the messages it received and sent and its own variables. All of these are XML documents and in some cases, sizable ones.

<a id="instance-data-cleanup--levels-of-cleanup"></a>

## Levels of cleanup

<a id="instance-data-cleanup--cleanup-on-completion"></a>

### Cleanup on completion

> [!NOTE]
> <a id="instance-data-cleanup--ode-version"></a>

>
> > [!NOTE]
> > #### ODE Version
>
> This feature is only available in ODE 1.3 or later

The easiest approach to get started is simply to wait until the instance execution is finished and then cleanup everything that's related to it. That would include the instance state with its variables, scopes and correlation, but also all the messages it has received and sent. Execution events should also be disposed of. So this description defines 5 different categories: instance, messages and events. We should be able to turn on and off each level separately.

- instance: ODE\_PROCESS\_INSTANCE, EXECUTION\_STATE
- variables: ODE\_SCOPE, ODE\_XML\_DATA, ODE\_PARTNER\_LINK
- messages: ODE\_MESSAGE, ODE\_MESSAGE\_ROUTE, ODE\_MEX\_PROPS, ODE\_MESSAGE\_EXCHANGE
- correlations: ODE\_CORRELATION\_SET, ODE\_CORSET\_PROP
- events: ODE\_EVENTS

DTD

```
<xs:element
name=
"cleanup"
minOccurs=
"0"
maxOccurs=
"3"
type=
"dd:tCleanup"
/>
<xs:complexType
name=
"tCleanup"
> <xs:sequence> <xs:element name="category" default="all" minOccurs="0" maxOccurs="unbounded" > <xs:simpleType> <xs:restriction base="xs:string" > <xs:enumeration value="instance"/> <xs:enumeration value="variables"/> <xs:enumeration value="messages"/> <xs:enumeration value="correlations"/> <xs:enumeration value="events"/> <xs:enumeration value="all"/> </xs:restriction> </xs:simpleType> </xs:element> </xs:sequence> <xs:attribute name="on" use="required" > <xs:simpleType> <xs:restriction base="xs:string" > <xs:enumeration value="success"/> <xs:enumeration value="failure"/> <xs:enumeration value="always"/> </xs:restriction> </xs:simpleType> </xs:attribute> </xs:complexType>
```

<a id="instance-data-cleanup--examples"></a>

## Examples

1. no instance data cleanup


```
<process name="pns:HelloWorld2">
<active>true</active>
<provide partnerLink="helloPartnerLink">
    <service name="wns:HelloService" port="HelloPort"/>
</provide>
</process>
```

2. cleaning up all data on either successful or faulty completions of instances


```
<process name="pns:HelloWorld2">
<active>true</active>
<provide partnerLink="helloPartnerLink">
    <service name="wns:HelloService" port="HelloPort"/>
</provide>
<cleanup on="always" />
</process>
```

3. cleaning up all data on successful completions of instances and no data cleanup on faulty completions


```
<process name="pns:HelloWorld2">
<active>true</active>
<provide partnerLink="helloPartnerLink">
    <service name="wns:HelloService" port="HelloPort"/>
</provide>
<cleanup on="success" >
            <category>instance</category>
            <category>variables</category>
            <category>messages</category>
            <category>correlations</category>
            <category>events</category>
    </cleanup>
</process>
```

4. cleaning up all data on successful completions of instances and only messages and correlations on faulty completions


```
<process name="pns:HelloWorld2">
<active>true</active>
<provide partnerLink="helloPartnerLink">
    <service name="wns:HelloService" port="HelloPort"/>
</provide>

<cleanup on="success" >
            <category>all</category>
    </cleanup>
    <cleanup on="failure">
            <category>messages</category>
            <category>correlations</category>
    </cleanup>
</process>
```

5. an +invalid+ configuration; the instance category should accompany the variable and correlations categories


```
<process name="pns:HelloWorld2">
<active>true</active>
<provide partnerLink="helloPartnerLink">
    <service name="wns:HelloService" port="HelloPort"/>
</provide>
<cleanup on="success" >
            <category>all</category>
    </cleanup>
    <cleanup on="failure">
            <category>instance</category>
    </cleanup>
</process>
```

<a id="instance-data-cleanup--future-developments"></a>

## Future Developments

WS-BPEL makes heavy use of scopes, those could be another hook in the execution lifecycle for the cleanup to take place. So instead of waiting until the instance is finished and clean up the whole state, we could proceed by smaller increments and delete the state scope by scope. For short running processes (say less than a few days) the advantages of this approach are minimal but for long running processes (say months), there's potentially a lot of unused state that's just sitting there and will never be used anymore.

<a id="instance-data-cleanup--final-notes"></a>

## Final notes

When we continue along the lines of refining further when the cleanup should occur and what exactly should be cleaned up, we quickly start getting close to the transaction boundaries. Down the road, ideally, we shouldn't persist anything unnecessarily, so that no cleanup is needed when a given piece of data will never be reused. It's often the case for message variables for example, where a process will receive a message, assign some values from it and never use that message variable anymore. So this should never get written, minimizing the writes and deletes.

---

<a id="direct-process-to-process-communication"></a>

<!-- source_url: https://ode.apache.org/direct-process-to-process-communication.html -->

<!-- page_index: 13 -->

<a id="direct-process-to-process-communication--p2p-communication"></a>

## P2P Communication

ODE automatically optimizes all process-to-process (P2P) communication such that all message exchanges happen directly inside the engine and do not go through the integration layer (e.g. Axis2, JBI, ...).

---

<a id="developerguide-stateful-exchange-protocol"></a>

<!-- source_url: https://ode.apache.org/developerguide/stateful-exchange-protocol.html -->

<!-- page_index: 14 -->

<a id="developerguide-stateful-exchange-protocol--1-general"></a>
<a id="developerguide-stateful-exchange-protocol--1.-general"></a>

## 1. General

[TBD: Insert overview of the world before and after automagic correlation]

<a id="developerguide-stateful-exchange-protocol--2-state-identifiers"></a>
<a id="developerguide-stateful-exchange-protocol--2.-state-identifiers"></a>

## 2. State Identifiers

A common use case consists of a client that needs to invoke multiple operations against the same service. Each operation depends on the state resulting from the completion of the previous operation. The service needs to associate these invocations with states it maintains internally. That's the basis for the State Exchange protocol.

In the initial invocation, the client sends a request to the service. The service returns a response that includes a *state identifier*. The state identifier is opaque to the client, however, the client knows to use that state identifier in subsequent invocations that depend on the state of the pervious invocation.

In a subsequent invocation, the client sends a request to the service and includes the state identifier. The service is able to associate this request with thwe state reached by the previous request.

The exact mechanism for carrying the state identifier depends on the underlying transport protocol and the message wire format. This specification provides bindings for SOAP and HTTP.

The protocol requires an initial two-way operation, followed by any combination of two-way and one-way operations.

The service can decide how long to keep an association between the state identifier and any internal state, and how to deal with failure conditions that may result in loss of state. A service should express its ability to maintain state association through its policy.

The service responds with an error if it expects to receive a state identifier and does not find one in the message, or if it cannot associate the state identifier with any known state.

Unless specified otherwise, the client expects to receive the same state identifier in subsequent invocations of the service. The client may detect an error condition if it sends one state identifier and receives another. Unless specified otherwise, the client may conclude that the state identifier is no longer associated with any state if it receives a response that does not include a state identifier.

Although the state identifier is opaque to the client, the client can compare state identifiers for equivalence. Two state identifiers are equivalent if they contain the same set of characters.

Services are encouraged to create unique identifiers for each internal state using globally unique identifiers. In doing so, they prevent accidental association of two unrelated states.

<a id="developerguide-stateful-exchange-protocol--3-stateful-eprs"></a>
<a id="developerguide-stateful-exchange-protocol--3.-stateful-eprs"></a>

## 3. Stateful EPRs

Some interactions involve more than one client or more than one service. These interactions require the clients and services to communicate stateful EPRs.

A *stateful EPR* is an EPR that contains all the information necessary to invoke a service in association with a particular state. A stateful EPR is essentially an EPR that incorporates a state identifier. For example, when using WS-Addressing, the stateful EPR will include the state identifier as a reference property.

The client obtains the stateful EPR in one of three ways:
 *By composition.* From a header or the body of the message.
\* From the state callback header.

When using WS-Addressing, the client can compose the stateful EPR by combining the service EPR and the state identifier, using the state identifier as a reference property.

All addressing mechanisms support stateful EPRs. However, not all addressing mechanisms allow the client to compose stateful EPRs. For example, when using the HTTP protocol bindings, only the service can construct stateful EPRs.

The service may also send a stateful EPR in a header or the body of the message. The service may send its own stateful EPR, or the stateful EPR of a different service (see *Shared States*). The state callback header is a special case of that (see *State Callback*).

<a id="developerguide-stateful-exchange-protocol--4-shared-states"></a>
<a id="developerguide-stateful-exchange-protocol--4.-shared-states"></a>

## 4. Shared States

There are cases where two or more services share a common state. This non-normative part of the specification provides guidelines for implementing such scenarios.

For example, a process may implement two services that both affect the same process instance (internal state). The client invokes operations on the first service against the same process instance by using one state identifier. The client then needs to invoke operations on the second service against the same process instanace.

The two services use different EPRs, and the client may not be able to deduct one stateful EPR from the other. In fact, it is highly recommended that the two stateful EPRs use different state identifiers. Instead, the first service obtains the stateful EPR of the second service and sends it to the client.

In this case, the first service obtains the stateful EPR of the second service and sends it to the client.

For example, a BPEL process may receive a request on one partnerLink, assign the myRole EPR of another partnerLink to a message and reply with that message. After extracting the EPR from the message, the client is able to invoke the same process instance using the second partnerLink.

To support this pattern we recommend that a BPEL implementation construct a stateful EPR for a partnerLink myRole on or before first use. First use occurs when that partnerLink myRole is assigned to a variable, or communicated in the header of a message by a process instance. Once set, the stateful EPR remains the same until discarded by the process instance.

<a id="developerguide-stateful-exchange-protocol--5-state-callback"></a>
<a id="developerguide-stateful-exchange-protocol--5.-state-callback"></a>

## 5. State Callback

There are may ways in which services can be combined using stateful message exchanges. A common pattern consists of a two-way exchange between two services acting as peers invoke each other. This pattern is common enough that the State Exchange protocol introduces a specific header to cater for it.

The State Exchange protocol supports this pattern using *state callback headers*. State callback headers are sent in addition to state identifiers to provide a callback address. They are used to associate two states with each other.

In the initial invocation, the first service constructs a stateful EPR and sends it as a state callback header. The second service returns a response with a state identifier. In a subsequent invocation, the first service uses that state identifier to invoke the second service.

The second service may also follow up with an invocation of the first service using the stateful EPR provided in the state callback header. In this manner, both services can invoke each other within the same interaction.

Both services maintain their own internal states and use separate state identifiers. The state association results from invocations that, regardless of direction, refer to both internal states.

In order to support addressing schemes that do not allow the client to compose a stateful EPR, a service may return a callback state header in lieu of, or in addition to the state identifier. The client may then choose whether to use the state identifier or stateful EPR for subsequent invocations of that service.

<a id="developerguide-stateful-exchange-protocol--6-fail-fast-mechanism"></a>
<a id="developerguide-stateful-exchange-protocol--6.-fail-fast-mechanism"></a>

## 6. Fail-fast Mechanism

TBD: Cleanup

An important characteristic of the State Exchange protocol is that clients and servers must be aware whether the interaction is in fact stateful. Reaching that decision is not always possible, but for the benefit of protocols that allow it, we introduce a fail-fast mechanism.

When the client sends a message to the service that does not require the state identifier or state callback header, it may use the *state use* header instead. This header informs the service that the client supports state exchange. The client may also force the service to process the header (e.g. using the SOAP *mustUnderstand* attribute) to guarantee that the service supports state exchange.

<a id="developerguide-stateful-exchange-protocol--7-soap-bindings"></a>
<a id="developerguide-stateful-exchange-protocol--7.-soap-bindings"></a>

## 7. SOAP Bindings

When using SOAP, the state identifier is sent in the header `state:identifier` and the callback EPR is sent in the header `state:callback`. If the message does not contain either header, it may use the `state:use` header to indicate support for the State Exchange protocol.

The `state:identifier` header is an element of type xsd:string that contains an opaque identifier.

The `state:callback` header is an element of type `wsa:EndpointReference` that contains a WS-Addressing EPR. It must contain the reference property state:identifier.

The `state:use` header is an element of type `xsd:boolean` that must contain the value true.

The `state:identifier` header must be present in any response message, as long as the service can maintain an association for that state identifier. A response message that does not include the state:identifier header signals to the client that the service no longer accepts that state identifier.

A client can compose the stateful EPR of a service by combining the service EPR with the `state:identifier` header, using it as a reference property. When it sends a message to the service, it uses the service EPR and copies the state:identifier element to the header of the SOAP message. In doing so, it fulfills the requirements of both WS-Addressing and State Exchange protocol.

To fail fast is the protocol is not supported, clients are encouraged to use the mustUnderstand attribute to force the service to process state headers. Services are encourage to look for the existence of a state header to determine if the client supports the State Exchange protocol. Additional checking can be done on response messages.

The following table summarizes SOAP faults used by the State Exchange protocol:

`state:missingIdentifier`

The service expects to receive a state identifier and did not find one in the message.

`state:noSuchState`

The state identifier is not associated with any internal state maintained by the service.

`state:missingHeader`

The service expects a state exchange and the client did not provide any state header.

`state:invalidCallback`

The `state:callback` header cannot be used as an endpoint reference.

---

<a id="extensions-activity-failure-and-recovery"></a>

<!-- source_url: https://ode.apache.org/extensions/activity-failure-and-recovery.html -->

<!-- page_index: 15 -->

<a id="extensions-activity-failure-and-recovery--overview"></a>

## Overview

There are several types of error conditions. In this document we introduce a class of error condition called *failures*, distinct from *faults*, and describe how failures are caught and handled by the process engine.

A service returns a fault in response to a request it cannot process. A process may also raise a fault internally when it encounters a terminal error condition, e.g. a faulty expression or false join condition. In addition, processes may raise faults in order to terminate normal processing.

In contrast, failures are non-terminal error conditions that do not affect the normal flow of the process. We keep the process definition simple and straightforward by delegating failure handling to the process engine and administrator.

For example, when the process is unable to perform DNS resolution to determine the service endpoint, it generates a failure. An administrator can fix the DNS server and tell the process engine to retry the activity. Had the DNS error been reported as a fault, the process would either terminate or require complex fault handling and recovery logic to proceed past this point of failure.

In short, failures shields the process from common, non-terminal error conditions while retaining simple and straightforward process definitions that do not need to account for these error conditions.

<a id="extensions-activity-failure-and-recovery--from-failure-to-recovery"></a>

### From Failure to Recovery

Currently, the *Invoke* activity is the only activity that supports failure handling and recovery. The mechanism is identical for all other activities that may support failure handling and recovery in the future.

In case of the *Invoke* activity, a failure condition is triggered by the integration layer, in lieu of a response or fault message. The *Invoke* activity consults its failure handling policy (specified here) and decides how to respond.

Set *faultOnFailure* to *yes*, if you want the activity to throw a fault on failure. All other failure handling settings are ignored. The activity will throw the *activityFailure* fault.

The *activityFailure* fault is a standard fault, so you can use the *exitOnStandardFault* attribute to control whether the process exits immediately, or throws a fault in the enclosing scope.

Set *retryFor* to a positive integer if you want the activity to attempt self-recovery and retry up to that number of times. Set *retryDelay* to a reasonable time delay (specified in seconds) between retries. For example, if you set *retryFor=2, retryDelay=30*, the activity will retry after 30 and 60 seconds, for a total of three attempts, before entering activity recovery mode.

If the activity retries and succeeds, it will complete successfully as if no failure occurred. Of course, the activity may retry and fault, e.g. if the invoked service returns a fault. If the activity has exhausted all retry attempts, it enters activity recovery mode. By default *retryFor* is zero, and the activity enters recovery mode after the first failure.

When in recovery mode, you can recover the activity in one of three ways:
Retry *-- Retry the activity manually. You can repeat this any number of times until the activity completes or faults.* *Fault* -- Causes the activity to throw the *activityFailure* fault.
Cancel\* -- Cancels the activity. The activity completes unsuccessfully: without changing the state of variables, by setting the status of all its source links to false, and without installing a compensation handler.
Activity recovery is performed individually for each activity instance, and does not affect other activities executing in the same process. While the activity is in the *FAILURE* state, the process instance remains in the *ACTIVE* state and may execute other activities from parallel flows and event handlers.

<a id="extensions-activity-failure-and-recovery--specifying-failure-behavior"></a>

### Specifying Failure Behavior

Use the *failureHandling* extensibility element defined in the namespace `http://ode.apache.org/activityRecovery`. The structure of the *failureHandling* element is:

```
<ext:failureHandling xmlns:ext="http://ode.apache.org/activityRecovery">
    <ext:faultOnFailure> _boolean_ </ext:faultOnFailure>
    <ext:retryFor> _integer_ </ext:retryFor>
    <ext:retryDelay> _integer_ </ext:retryDelay>
</ext:failureHandling>
```

The *faultOnFailure*, *retryFor* and *retryDelay* elements are optional. The default values are false for *faultOnFailure*, and zero for *retryFor* and *retryDelay*.

An activity that does not specify failure handling using this extensibility element, inherits the failure handling policy of its parent activity, recursively up to the top-level activity of the process. You can useinheritence to specify the failure handling policy of a set of activities, or all activities in the process, using a single *failureHandling* extensibility element.

Note that due to this behavior, if activity *S* specifies failure handling with the values *retryFor=2, retryDelay=60*, and has a child activity *R* that specifies failure handling with the values *retryFor=3*, the *retryDelay* value for the child activity *R* is 0, and not 60. Using the *failureHandling* element without specifying one of its value elements will apply the default value for that element.

<a id="extensions-activity-failure-and-recovery--examples"></a>

### Examples

A simple invoke with the `ext:failureHandling` extension:

```
<bpel:invoke inputVariable="myRequest"
    operation="foo" outputVariable="aResponse"
    partnerLink="myPartner" portType="spt:SomePortType">

    <ext:failureHandling xmlns:ext="http://ode.apache.org/activityRecovery">
        <ext:faultOnFailure>false</ext:faultOnFailure>
        <ext:retryFor>2</ext:retryFor>
        <ext:retryDelay>60</ext:retryDelay>
    </ext:failureHandling>

</bpel:invoke>
```

And a sequence activity that converts failures into faults:

```
<bpel:sequence>

    <ext:failureHandling xmlns:ext="http://ode.apache.org/activityRecovery">
        <ext:faultOnFailure>true</ext:faultOnFailure>
    </ext:failureHandling>

    ...

    <bpel:invoke inputVariable="myRequest"
        operation="foo" outputVariable="aResponse"
        partnerLink="myPartner" portType="spt:SomePortType">

        <bpel:catchAll>
            ...
        </bpel:catchAll>

    </bpel:invoke>

</bpel:sequence>
```

<a id="extensions-activity-failure-and-recovery--process-instance-management"></a>

### Process Instance Management

The process instance management provides the following information:
 *Process instance summary includes a *failures* element with a count of the total number of process instances that have one or more activities in recovery mode, and the date/time of the last activity to enter recovery mode. The element exists if at least one activity is in recovery mode.* Process instance information includes a *failures* element with a count of the number of activities in recovery mode, and the date/time of the last activity to enter recovery mode. The element exists if at least one activity is in recovery mode.
\* Activity instance information includes a *failure* element that specifies the date/time of the failure, the reason for the failure, number of retries, and list of available recovery actions. The element exists if the activity is in the state *FAILURE*.

Use the *recoverActivity* operation to perform a recovery action on an activity in recovery mode. The operation requires the process instance ID, the activity instance ID and the recovery action to perform (one of retry, fault or cancel).

You can also determine when failure or recovery occurred for a given activity instance from the execution log.

---

<a id="extensions-xquery-extensions"></a>

<!-- source_url: https://ode.apache.org/extensions/xquery-extensions.html -->

<!-- page_index: 16 -->

<a id="extensions-xquery-extensions--overview"></a>

## Overview

> [!NOTE]
> XQuery is available only in ODE 1.3 or later

Apache ODE goes above and beyond the [WS-BPEL](#ws-bpel-20) specification by allowing the use of [XQuery 1.0](http://www.w3.org/TR/xquery/) in queries and expressions.

Unless specified otherwise, WS-BPEL considers XPath 1.0 to be the query/expression language, which is denoted by the default value of the "queryLanguage" and "expressionLanguage" attributes, viz. "urn:oasis:names:tc:wsbpel:2.0:sublang:xpath1.0". In addition, we have out-of-the-box support for XPath 2.0.

<a id="extensions-xquery-extensions--xquery-10"></a>
<a id="extensions-xquery-extensions--xquery-1.0"></a>

## XQuery 1.0

To use XQuery 1.0 in your processes just use the following *queryLanguage* and *expressionLanguage* attributes:

```
queryLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xquery1.0"
expressionLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xquery1.0"
```

If you want support at the process just add these attributes to your root *process* element. If you want to stick with XPath 1.0 but want XQuery 1.0 support for a specific assignment you can also define these attributes on an *assign* element.

For your convenience, all of the functions and variables, standard or otherwise, that are available in XPath 2.0 have been exposed in XQuery 1.0 as well.

<a id="extensions-xquery-extensions--examples"></a>

### Examples

The following snippet illustrates how to use XQuery 1.0 in *assign* activities. Needless to say, you may use XQuery 1.0 anywhere an expression is permitted, such as in a *while*, *if*, *repeatUntil* or *forEach* activity.

```
<process name="HelloXQueryWorld" 
    targetNamespace="http://ode/bpel/unit-test"
    xmlns:bpws="http://docs.oasis-open.org/wsbpel/2.0/process/executable"
    xmlns="http://docs.oasis-open.org/wsbpel/2.0/process/executable"
    xmlns:tns="http://ode/bpel/unit-test"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:types="http://ode/bpel/types"
    xmlns:test="http://ode/bpel/unit-test.wsdl"
    xmlns:ode="http://www.apache.org/ode/type/extension"
    queryLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xquery1.0"
    expressionLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xquery1.0">

        ...
        <assign name="assign1">
            <copy>
                <from variable="myVar" part="TestPart"/>
                <to variable="otherVar"/>
            </copy>
            <copy>
                <from><![CDATA[<test:content>Hello</test:content>]]></from>
                <to variable="tempVar"/>
            </copy>
            <copy>
                <from>
                    typeswitch ($myVar.TestPart) 
                      case $a as xs:string return "test"
                      default return "default"
                </from>
                <to variable="otherVar"/>
            </copy>
            <copy>
                <from><![CDATA[
                    typeswitch ($myVar.TestPart) 
                      case $a as text() return <test:content/>
                      default return <test:content/>
                    ]]>
                </from>
                <to variable="otherVar"/>
            </copy>
            <copy>
                <from>
                    for $loopOnce in (1) 
                    return 
                       concat(bpws:getVariableProperty("myVar", "test:content"), "XQuery World")
                </from>
                <to variable="myVar" part="TestPart"/>
            </copy>
        </assign>
        ...
    </sequence>
</process>
```

<a id="extensions-xquery-extensions--known-limitations"></a>

### Known Limitations

Currently, we do not support:
 *The use of modules in XQuery.* The use of update expressions in XQuery.

---

<a id="custom-xpath-functions"></a>

<!-- source_url: https://ode.apache.org/custom-xpath-functions.html -->

<!-- page_index: 17 -->

<a id="custom-xpath-functions--introduction"></a>

## Introduction

ODE uses the Saxon XPath processor to support custom XPath functions.

This text is a quick summary of Saxon's own extensibility documentation. I recommend you read it if you need more information. It goes into much more detail on Java invocation, supported data types, conversions, etc.

To use XPath extensions, you must use the XPath 2.0 expression language.

<a id="custom-xpath-functions--writing-extension-functions"></a>

## Writing extension functions

An extension function is invoked using a name such as `prefix:localname()`. The prefix must be the prefix associated with a namespace declaration that is in scope.

Extension functions must be implemented in Java. You bind external Java classes by encoding the class name part in the namespace URI. The URI for the namespace identifies the class where the external function will be found. The namespace URI must be `java:` followed by the fully-qualified class name; for example `xmlns:date="java:java.util.Date"`). The class must be on the classpath, or more specifically accessible from the current classloader.

> [!NOTE]
> Saxon 8.x and earlier supported namespace binding with a training "/" + the fully-qualified class name; for example `xmlns:date="http://www.jclark.com/xt/java/java.util.Date"`). This approach is no longer supported in Saxon 9.x and you should now use the `java:` prefix.

```
<assign> <copy xmlns:ext="java:com.example.xpath.Random"> <from expressionLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xpath2.0">ext:random()</from> <to>$myVariable</to> </copy> </assign>
:::java package com.example.xpath;
/** * Returns a random number */ public class Random {public static int random() {java.util.Random randomizer = new java.util.Random(); int number = randomizer.nextInt(); return Math.abs(number);}}
```

You can download source code or the ready-to-use jar for testing.

<a id="custom-xpath-functions--deploying-extension-functions"></a>

## Deploying extension functions

There are a few options:

- As a generic solution, you can add your XPath function jar in the application CLASSPATH
- If ODE is deployed as a webapp, you can copy your XPath function jar in the webapp /lib directory
- If ODE is deployed inside a JBI container, you can deploy your XPath function jar as a shared library

---

<a id="developerguide-atomic-scopes-extension-for-bpel"></a>

<!-- source_url: https://ode.apache.org/developerguide/atomic-scopes-extension-for-bpel.html -->

<!-- page_index: 18 -->

<a id="developerguide-atomic-scopes-extension-for-bpel--introduction"></a>

# Introduction

The goal of this specification is to provide a simple extension to WS-BPEL 2.0 that enables atomic scopes. Atomic scopes allow the process definition to demarcate atomic transactions against any number of invoked services, and participate in a distributed transaction.

The extension defines atomic scope as an extension of the already defined isolated scopes. It describes the atomic semantics for state changing operatings, such as assignments, for service invocations and for receiving and responding to service calls. It also covers the use of compensation handlers and event handlers.

<a id="developerguide-atomic-scopes-extension-for-bpel--atomic-scopes"></a>

# Atomic Scopes

An *atomic scope* is marked with the attribute `atomic` set to `yes`. This attribute applies to processes, *scope* activities and event handlers (their implicit scopes).

Atomic scopes provide isolation semantics, inheriting these semantics from isolated scopes. However, atomic scopes are not isolated scopes, specifically their compensation handler do not have isolated semantics. Atomic scopes cannot be nested inside atomic scopes or isolated scopes, and cannot enclose isolated scopes.

<a id="developerguide-atomic-scopes-extension-for-bpel--state-changes-and-assignments"></a>

# State Changes and Assignments

Atomic scopes provide '*all-or-nothing*'' behavior for all state changes made during the execution of activities inside the scope, and the status of all links crossing the scope boundary.

State changes include changes to variables, partner links and correlations sets declared in any scope enclosing the atomic scope. These state changes are not visible outside the atomic scope until the scope activity completes (successfully or unsuccessfully). These state changes are discarded if the atomic scope throws a fault in the enclosed scope.

The status of links that cross the boundary of an atomic scope and have a source activity inside the atomic scope is set only when the scope completes. If the scope completes without throwing a fault, the status of these links is set as per the result of their transition conditions. If the scope throws a fault, the status of all these links is set to false.

The status of message exchange is not affected by the atomic scope. Specifically all message exchanges made inside the atomic scope must complete before the scope is allowed to complete.

Since atomic scopes provide all-or-nothing semantics, *assign* activities inside the scope are not by themselves atomic. Rather, all *assign* activities occurring in the scope are collectively atomic, since the scope will discard all state changes if it throws a fault.

However, catching and handling the `bpws:selectionFailure` fault or any other fault throws by an *assign* activity could lead to partial assignments if the scope is allowed to complete. If fault handlers must be used inside the atomic scope, use them with discretion. This rule also applies to other unintended consequences of indiscriminately catching and handling faults inside an atomic scope.

<a id="developerguide-atomic-scopes-extension-for-bpel--activities-that-wait"></a>

# Activities That Wait

Since atomic scopes are intended to complete in a short duration of time, they are not allowed to wait for events occurring outside the scope, with the exception of events that trigger the scope.

Atomic scope are not allowed to use the *receive*, *wait* and *pick* activities, except for the case described below. Atomic scopes are not allowed to use event handlers, including not in any scope nested within the atomic scope.

An atomic scope may begin by receiving a message from a partner. In this case it can use the *receive* activity if that *receive* activity is the first basic activity to execute in the scope and no other basic activity is allowed to execute before it. Alternatively, it can use a *pick* activity with two or more *onMessage* handlers if no other basic or *pick* activity is allowed to execute before it.

Such a scope may begin with the block activity *sequence* or *flow* as long as it can guarantee that the first basic activity to execute is the *receive* or *pick* activity. These restrictions are similar to the start activity of a process.

An *onEvent* event handler can use the `atomic` attribute to specify atomic behavior for its implicit scope. In this case, the received message is treated as if the event handler started with a *receive* activity for that message. All other atomic scope restrictions are applied to the implicit scope created by the event handler.

If an atomic scope has a *receive* activity for a request-response operation, it must also include all *reply* activities that may send the corresponding response message. Specifically, it is an error for a *receive*/*reply* pair to cross the boundaries of an atomic scope.

An atomic scope is allowed to include an activity that is the target of a link, where the source activity resides outside the scope, only if the status of the link is determined before the atomic scope begins executing that activity.

If the process engine detects a violation of these restrictions if must throw an `atomic:scopeRollback` fault. If the process engine detects such a violation during static analysis, it should reject the process definition.

<a id="developerguide-atomic-scopes-extension-for-bpel--faults-and-termination"></a>

# Faults and Termination

Atomic scopes complete with one of three possible outcomes:

1. *Successful Completion* -- The *scope* activity, process or event handler completes without throwing a fault. For the *scope* activity this also includes evaluation of all transition conditions. All state changes made by the scope become visible to enclosing scopes and the compensation handler is installed.
2. *Unsuccessful Completion* -- A fault is thrown in the atomic scope and is handled by a fault handler. The behavior is similar to successful completion with the exception that the compensation handler is not installed.
3. *Scope Rollback* -- A fault is thrown by the *scope* activity or event handler, or the process terminates. All state changes made by the scope are discarded, no compensation handler is installed, and the status of all links originating from the scope is set to false.

The first two outcomes are similar to the successful and unsuccessful completion of non-atomic scopes. The last outcome is the case of a non-atomic scope throwing a fault, with the exception that all state changes are discarded.

An atomic scope that catches a fault and its fault handler rethrows that fault or throws a different fault, would result in the rollback outcome and discard all state changes.

It is recommended not to use fault handlers inside atomic scopes, since atomic scopes already provide a mechanism for dealing with failure, and indiscreminate use of fault handlers could lead to partial state changes and other unexpected results. However, there are some cases where fault handling is necessary, and the spec allows the use of fault handlers to deal with these situations.

Atomic scopes are intended to execute for a short duration of time, in particular since they may tie up global resources beyond the specific process. Like atomic activities, they cannot be interrupted by a fault thrown in an enclosing scope. However, implementations would terminate scopes that take too long to complete. It is up to the implementation to decide on the appropriate time duration.

In terminating the atomic scope, the implementation must force a rollback outcome, effectively throwing an `atomic:scopeRollback` fault in the enclosing scope. The behavior is similar to the way termination occurs in non-atomic scopes, with the exception that the scope has to terminate quickly and all state changes are discarded. As such, atomic scopes are not allowed to use termination handlers.

<a id="developerguide-atomic-scopes-extension-for-bpel--compensation"></a>

# Compensation

The compensation handler associated with an atomic scope is not by itself atomic. Some atomic scopes can use atomic compensation, however, other atomic scopes can only use non-atomic compensation. We cannot enforce an atomic scope to have an atomic compensation handler. To perform atomic compensation, the compensation handler may itself use an atomic scope.

The behavior of a compensation handler depends not on the scope in which it is defined, but the scope in which it is invoked. This could lead to situations where the compensation handler is potentially invoked in three different and incompatible scopes.

Consider a non-atomic outer scope *So*, enclosing an atomic scope *Sa*, itself enclosing an inner scope *Si* (perhaps an *invoke* activity). The scope *Si* installs a compensation handler *Ci*. The default fault handler associated with the scope *Si* will invoke the compensation handler *Ci* in that atomic scope, and then discard all state changes (by rethrowing the fault).

The atomic scope *Sa* can have a compensation handler *Ca* that invokes the compensation handler *Ci* from a non-atomic scope. However, the outer scope *So* may have a compensation handler that invokes *Ca* and through it *Ci* from within an atomic scope. Besides these three explicitly defined handlers, we also have to consider default and defined compensation, fault and termination handlers of each enclosing scope. This makes it hard to define compensation handlers that execute reliably.

Atomic scopes are generally simple in their logic and do not benefit much from the ability to compose compensation handlers though invocation of inner compensation handlers. In favor of simplicity the specification imposes the following constraints:

1. *Installing* -- Scopes nested inside an atomic scope (including the *invoke* activity shortcut) are not allowed to define a compensation handler.
2. *Invoking* -- Atomic scopes are not allowed to invoke any compensation handler through use of the *compensate* and *compensateScope* activities (or any other mechanism).

Since scopes nested inside an atomic scope are not allowed to install compensation handlers, the default fault handling behavior of an atomic scope is to rethrow the fault. The behavior is consistent with the outcome that discards all state changes (scope rollback).

Since atomic scopes are not allowed to invoke compensation handlers explicitly, and are not allowed to enclose compensation handler, a compensation handler is never invoked from within an atomic scope, explicitly of from a default compensation handler or fault handler.

<a id="developerguide-atomic-scopes-extension-for-bpel--web-service-invocation"></a>

# Web Service Invocation

Atomic scopes are primarily used to provide all-or-nothing behavior that includes Web service invocations. As such they must use appropriate protocols that guarantee operations complete only if the scope completes, and rollback if the scope outcome is a rollback.

<a id="developerguide-atomic-scopes-extension-for-bpel--request-response-operations"></a>

## Request-Response Operations

The atomic scope invokes a service using a distributed transaction protocol (e.g. *WS-AtomicTransaction*) to propagate a transaction context to the invoked service. The invoked service enrolls in the transaction and participates in determining the transaction outcome. An atomic scope must use the same transaction context with all services invoked in that scope.

An atomic scope that begins by receiving a message using a distributed transaction protocol must enroll in the transaction and participate in determining the outcome of that transaction. The atomic scope must then use that transaction context with all service invocations. If the scope begins without receiving a message, or receives a message without using a distributed transaction protocol, it creates its own transaction context.

The following rules govern the outcome of the atomic scope and associated distributed transaction:

1. *Commit* -- The atomic scope can complete, successfully or unsuccessfully, only if the transaction outcome has been determined to be *commit*.
2. *Rollback on fault* -- If the atomic scope throws a fault, it must vote for the outcome of *rollback*. Therefore, it must determine that it can complete before allowing the transaction outcome of *commit*.
3. *Fault on rollback* -- If the transaction outcome is *rollback* and the atomic scope has not thrown a fault, then it must throw the fault `atomic:scopeRollback`.
4. *Retry* -- In cases 2 and 3, when the atomic scope creates the transaction context, the implementation is allowed to rollback the transaction and execute the scope again using a different transaction context.

The *invoke* activity is not allowed to use the `atomic` attribute as a shortcut for a scope. However, it is allowed to use the `atomic` attribute with the value `no` to invoke a service without using a distributed transaction protocol. Such an invocation does not affect the rules above, but could break the isolation and atomicity semantics of the distributed transaction.

In either case, the service must be invoked using a synchronous protocol, such as sending the request and response messages over the same HTTP connection.

<a id="developerguide-atomic-scopes-extension-for-bpel--one-way-operations"></a>

## One-Way Operations

The atomic scope invokes a service using a one-way operation by sending the message only if the scope completes. If the scope throws a fault, the message is discarded. No transaction context is propagated to the invoked service, since the transaction must commit before the message is sent.

An atomic scope that receives a message from a one-way operation consumes the message only if the scope activity completes. If the scope throws a fault, the message is not consumed. As with one-way *invoke*, the one-way *receive* activity does not use a distributed transaction protocol.

A message that was *consumed* will not be available again to the process. A message that was not consumed may be available again to be received by a different *receive* activity, or by the same *receive* activity if the atomic scope is restarted. The availability of messages not consumed is left up to the implementation, this specification does not address the possibility of message loss.

<a id="developerguide-atomic-scopes-extension-for-bpel--concurrency"></a>

## Concurrency

Performing concurrent service invocations using the same transaction context can lead to a diamond scenario, whereby two services are operating on the same shared resource without any means to coordinate their work. Such scenarios are impossible to detect by looking at the process definition alone, and the risk from failure outweighs any benefits from allowing them.

In addition, *assign* activities are not atomic when enclosed in an atomic scope. As such, atomic scopes are not allowed to perform basic activities concurrently. Atomic scopes that use parallel composition such as the *flow* and *foreach* activity must serialize all basic activities with respect to each other. Basic activities can assume they are not executed concurrently, but cannot assume any order of execution unless they use links to establish dependencies.

<a id="developerguide-atomic-scopes-extension-for-bpel--appendix"></a>

# Appendix

Stuff that comes here:
 *Namespace URL.* Syntax for atomic attribute on scope/invoke.
 *Definition of atomic:rollback fault.* Reference to relevant specifications.

---

<a id="ode-jbi-and-axis2-properties-overview"></a>

<!-- source_url: https://ode.apache.org/ode-jbi-and-axis2-properties-overview.html -->

<!-- page_index: 19 -->

<a id="ode-jbi-and-axis2-properties-overview--introduction"></a>

## Introduction

ode-axis2.properties and ode-jbi.properties are used for engine configuration.

<a id="ode-jbi-and-axis2-properties-overview--common-properties"></a>

## Common properties

Here, ode-jbi prefix is used. However for axis2, you need to replace it into ode-axis2.

```
# Database Mode ("INTERNAL", "EXTERNAL", "EMBEDDED")
# What kind of database should ODE use?
#   * "EMBEDDED" - ODE will create its own embbeded database (Derby)
#              and connection pool (Minerva).
#   * "EXTERNAL" - ODE will use an app-server provided database and pool.
#                  The "ode-jbi.db.ext.dataSource" property will need to
#                  be set.
#   * "INTERNAL" - ODE will create its own connection pool for a user-
# specified JDBC URL and driver. ode-jbi.db.mode=EMBEDDED
# External Database [JNDI Name]
# JNDI Name of the DataSource for the ODE database. This is only
# used if the "ode-jbi.db.mode" property is set to "EXTERNAL" ode-jbi.db.ext.dataSource=java:comp/env/jdbc/ode
# Embedded Database Name [String]
# Name of the embedded Derby database. This is only used if the
# "ode-jbi.db.mode" property is set to "EMBEDDED". #ode-jbi.db.emb.name=hibdb #ode-jbi.db.emb.name=jpadb
# Internal Database Configuration using Tranql Vendor packages #For MySQL #ode-jbi.db.int.mcf=org.tranql.connector.mysql.XAMCF #ode-jbi.db.int.mcf.databaseName=ODE #ode-jbi.db.int.mcf.userName=root #ode-jbi.db.int.mcf.password=root #ode-jbi.db.int.mcf.serverName=localhost #For Postgres #ode-jbi.db.int.mcf=org.tranql.connector.postgresql.PGXAMCF #ode-jbi.db.int.mcf.databaseName=ODE #ode-jbi.db.int.mcf.userName=postgres #ode-jbi.db.int.mcf.password=postgres #ode-jbi.db.int.mcf.serverName=localhost #For SQLServer #ode-jbi.db.int.mcf=org.tranql.connector.sqlserver.XAMCF #ode-jbi.db.int.mcf.databaseName=ODE #ode-jbi.db.int.mcf.userName=sa #ode-jbi.db.int.mcf.password=sa #ode-jbi.db.int.mcf.portNumber=1433 #ode-jbi.db.int.mcf.serverName=localhost #For Oracle ode-jbi.db.int.mcf=org.tranql.connector.oracle.LocalMCF ode-jbi.db.int.mcf.databaseName=XE ode-jbi.db.int.mcf.userName=ODE ode-jbi.db.int.mcf.password=ode ode-jbi.db.int.mcf.portNumber=1521 ode-jbi.db.int.mcf.serverName=localhost ode-jbi.db.int.mcf.driverType=thin
# Internal Database Configuration using generic JDBCDriverMCF #ode-jbi.db.int.jdbcurl=jdbc:mysql://localhost/ode?user=sa #ode-jbi.db.int.driver=com.mysql.jdbc.Driver
# DAO Connection Factory class.
# uncomment the following for hibernate. #ode-jbi.dao.factory=org.apache.ode.daohib.bpel.BpelDAOConnectionFactoryImpl
# BPEL Event Listener
# Uncomment the following for a debug output of BPEL navigation events. #ode-jbi.event.listeners=org.apache.ode.bpel.common.evt.DebugBpelEventListener #debugeventlistener.dumpToStdOut=on/off #Executor pool size ode-jbi.threads.pool.size=100
```

<a id="ode-jbi-and-axis2-properties-overview--ode-axis2properties"></a>
<a id="ode-jbi-and-axis2-properties-overview--ode-axis2.properties"></a>

## ode-axis2.properties

To configure those properties, please put ode-axis2.properties file in webapps/ode/WEB-INF/conf directory.

```
# HTTP connection pool used to invoke external services ode-axis2.http.connection-manager.max-per-host =100 ode-axis2.http.connection-manager.max-total =100 # Process dehydration ode-axis2.process.dehydration =true # Transaction factory #ode-axis2.tx.factory.class=org.apache.ode.axis2.util.GeronimoFactory #ode-axis2.tx.factory.class=org.apache.ode.axis2.util.JBossFactory #ode-axis2.tx.factory.class=org.apache.ode.axis2.util.TomcatFactory # Used to redirect traffic to localhost instead of routing again via load balancer in clustered environment ode-axis2.cluster.localRoute.targets =http://myloadbalancer.com:8080/ode/processes/ ode-axis2.cluster.localRoute.base =http://localhost:8888/ode/processes/
```

<a id="ode-jbi-and-axis2-properties-overview--ode-jbiproperties"></a>
<a id="ode-jbi-and-axis2-properties-overview--ode-jbi.properties"></a>

## ode-jbi.properties

For JBI distribution, those properties are zipped into Service Assembly.
For SMX4 OSGi bundle distribution, those are in SMX4/etc/org.apache.ode.jbi.cfg file.

```
# Process Identifier Namespace [QNAME]
# Namespace for processes created using the JBI integration.
# This will be the namespace of the process identifiers (PIDs) ode-jbi.pidNamespace=urn:ode-jbi
# Allow Incomplete Deployment ("true","false")
# Should incomplete deployments be allowed? An incomplete deployment
# arises when a service unit contains multiple processes and not all
# of the processes can be deployed. If incomplete deployments are
# allowed (true), the service unit will report success if any of the
# processes can be deployed. If not allowed (false), a failure in
# one process will prevent all processes from being deployed. ode-jbi.allowIncompleteDeployment=false
# Class name of the message mapper that should be used to convert message
# between ODE / NMS.
# org.apache.ode.jbi.msgmap.JbiWsdl11WrapperMapper - use JBI WSDL 1.1 "wrapped"
# org.apache.ode.jbi.msgmap.ServiceMixMapper
# org.apache.ode.jbi.msgmap.DocLitMapper ode-jbi.messageMapper=org.apache.ode.jbi.msgmap.ServiceMixMapper
```

---

<a id="controlling-odes-memory-footprint"></a>

<!-- source_url: https://ode.apache.org/controlling-odes-memory-footprint.html -->

<!-- page_index: 20 -->

<a id="controlling-odes-memory-footprint--rational"></a>

## Rational

In most ODE deployments, processes are only used once in a while and the time between each solicitation can be pretty long with respect to the actual execution time. However the default behavior for the engine is to load all processes permanently in memory, including their definition. For environments where memory is scarce or where a large number of processes are deployed, this isn't suitable.

ODE implements two mechanisms in order to reduce the memory footprint of the engine to the strict minimum:

- Process definitions lazy-loading: processes are loaded in-memory bare, without their runtime definition (the compiled BPEL process). The definition will be loaded and associated to the in-memory process representation only when they are actually invoked. This mechanism is called hydration.
- Process definitions reaping: process definitions can be disassociated from their in-memory representation if they haven't been used for some time of if there are already too many definitions loaded in memory. This mechanism is called dehydration. A process will automatically rehydrate itself when necessary (when it receives a message for example).

<a id="controlling-odes-memory-footprint--activating-dehydration-policy"></a>

## Activating Dehydration Policy

In the Axis2 integration layer, activation of the policy can be done by setting the following property in the ode-axis2.properties file, which is located in the WEB-INF/conf directory of ODE's web application:

```
ode-axis2.process.dehydration
=
true
```

The default configuration is to dehydrate processes that haven't been used for 20mn or after the maximum of 1000 process definitions in memory is reached.

However, you may override the time that the process have to remain unused before they can be considered for dehydration by specifying a value, in milliseconds, for the following property in the ode-axis2.properties file:

```
# wait for 5 minutes instead of 20 minutes ode-axis2.process.dehydration.maximum.age=300000
```

Similarly, you may override the maximum number of process definitions that may remain hydrated at any given point in time by specifying a value for the following property in the ode-axis2.properties file:

```
# allow not more than 500 processes to be in memory at once ode-axis2.process.dehydration.maximum.count=500
```

<a id="controlling-odes-memory-footprint--dehydration-policy-at-il-level"></a>

## Dehydration Policy at IL Level

If you're using your own interface layer or want to do some customization at this level, the default hydration policy is implemented in [CountLRUDehydrationPolicy](http://svn.apache.org/repos/asf/ode/trunk/bpel-runtime/src/main/java/org/apache/ode/bpel/engine/CountLRUDehydrationPolicy.java). It should be set on [BpelServerImpl](http://svn.apache.org/repos/asf/ode/trunk/bpel-runtime/src/main/java/org/apache/ode/bpel/engine/BpelServerImpl.java) and can been configured by setting the process max age or max count (either one will not influence the dehydration if set to 0). For example:

```
CountLRUDehydrationPolicy dehy =new CountLRUDehydrationPolicy (); dehy.setProcessMaxAge (60000 ); // Setting process max age to one minute dehy.setProcessMaxCount (100 ); // Setting maximum hydrated processes to 100 _server.setDehydrationPolicy (dehy );
```

The dehydration policy is polled every 10s to see if some processes should be dehydrated so a process max age of less than 10 seconds will be effectively of 10 seconds. Alternatively a custom dehydration policy can be used by implementing the [DehydrationPolicy|http://svn.apache.org/repos/asf/ode/trunk/bpel-runtime/src/main/java/org/apache/ode/bpel/engine/DehydrationPolicy.java] interface.

<a id="controlling-odes-memory-footprint--in-memory-processes"></a>

## In-Memory Processes

The property `ode-axis2.mex.inmem.ttl` may be used to limit the time-to-live of in-memory instances. This setting can be useful to avoid memory leaks related to in-memory processes that may get 'stuck' during execution and never terminate.

```
# automatically discard any in-memory process instance after 5 minutes ode-axis2.mex.inmem.ttl=300000
```

---

<a id="endpoint-configuration"></a>

<!-- source_url: https://ode.apache.org/endpoint-configuration.html -->

<!-- page_index: 21 -->

<a id="endpoint-configuration--endpoint-configuration-property-files"></a>

## Endpoint configuration property files

SOAP and HTTP external endpoints can be tweaked using some property files. A common set of properties are available to configure external services. At run time, ODE will translate these properties and apply them to Axis2 or HttpClient depending if the targeted service uses SOAP binding or HTTP binding.

<a id="endpoint-configuration--conventions-and-locations"></a>

### Conventions and locations

The extension of these property files must be `*.endpoint`. These files can be dropped in 2 different locations:
 *the global configuration directory of ODE which is by default `ode/WEB-INF/conf`. This location might be customized with the system property `org.apache.ode.configDir`* the process deployment directory, `ode/WEB-INF/processes/$your_process`

Two rules of precedence apply:
1. Endpoint files in a same directory are loaded in alphabetical order. Meaning that if a property is set in two different files, the value from the "greatest" file name will have precedence.
1. Endpoint files located in the global conf directory have precedence over files in process deployment directories.

> [!NOTE]
> <a id="endpoint-configuration--version-information"></a>

>
> > [!NOTE]
> > #### Version Information
>
> This feature is available in ODE > 1.1. For version 1.1, a file named endpoint-configuration.properties may be dropped in process deployment unit directories. For backward compatibility, ODE > 1.1 supports this file too.
<a id="endpoint-configuration--dynamic-refresh"></a>

### Dynamic refresh

Properties are dynamically loaded and refreshed at run time.
The timing is the following:
On every request, if the file has not been polled during the last 30 seconds then check the file for updates. If any, reload it.

Consequently, if you have updated properties, you have to wait ~30 seconds and then trigger a request.

<a id="endpoint-configuration--hierarchical-properties"></a>

### Hierarchical properties

The property file is a regular property file except that service name and port name may be used to apply different default values to different services.
All properties follow this pattern:

```
[nsalias.servicename[.portname].ode.]property
```

If service name is mentioned but port name omitted, the value will apply to all ports of the service.
If service name and port name are omitted, the value will apply to all services.

<a id="endpoint-configuration--namespace-management"></a>

#### Namespace management

A service has to be qualified. To so do you may define namespace aliases. Aliases will then prefixed the service local name.

```
alias.ode_ns
=
http://ode.apache.org
ode_ns.dummyservice.ode.http.request.chunk
=
true
```

If your namespace does not collide with the [property syntax](http://java.sun.com/j2se/1.4.2/docs/api/java/util/properties.html#load(java.io.inputstream).html) , you dont have to define an alias. This property file is accepted:

```
# Next line is commented
# alias.ode_ns=http://ode.apache.org ode_ns.dummyservice.ode.http.request.chunk=true
```

<a id="endpoint-configuration--examples"></a>

#### Examples

For instance, considering 2 services:
 *the `foo-service`* and the `brel-service` which has 2 ports: `port-of-amsterdam` and `port-of-hiva-oa`

and this property file:

```
alias.test_ns =http://test.org http.protocol.max-redirects =5 test_ns.brel-service.ode.http.protocol.max-redirects =40 test_ns.brel-service.port-of-amsterdam.ode.http.protocol.max-redirects =100
```

The `http.protocol.max-redirect` property will have the following values:

- *5* for all ports of `foo-service`
- *40* for `brel-service.port-of-hiva-oa`
- *100* for `brel-service.port-of-amsterdam`

<a id="endpoint-configuration--supported-properties"></a>

### Supported properties

Here the list of supported properties, and their descriptions. If the file contains some properties not listed here, they will be available in the property map nevertheless. Values will be strings.
Such unmanaged properties will also be passed to Axis2 options and HttpClient params, see below.

| Context | Property name | Accepted values | Description/Notes |
| --- | --- | --- | --- |
| BPEL-runtime | mex.timeout | a long | the ODE Message Exchange timeout |
|  | mex.failure.verbose | true(default)/false | mute the details of a failure that might occur during a process invocation (to avoid information disclosure for instance) |
| Outbound Services | address | a URL | overrides the soap:address or http:address. The order of precedence is: process, property files, wsdl. |
|  | http.request.chunk | true/false | This will enable/disable chunking support. Will not apply to http-bound services TBD |
|  | http.protocol.version | HTTP/1.1 or HTTP/1.0 | the HTTP protocol version used |
|  | http.request.gzip | true/false | Will not apply to http-bound services TBD |
|  | http.accept.gzip | true/false | Append gzip to the Accept-Encoding header |
|  | http.protocol.content-charset | a string |  |
|  | http.default-headers.{your-header} |  | You must define one property per header, prefixed with 'http.default-headers'. These values will be appended to any previous value already set for a given header. |
|  | http.connection.timeout | an int | timeout in milliseconds until a connection is etablished |
|  | http.socket.timeout | an int | timeout in milliseconds for waiting for data |
|  | http.protocol.max-redirects | an int | the maximum number of redirects to be followed |
|  | http.proxy.host=myproxy.org |  | To disable proxy set the host to null |
|  | http.proxy.port |  |  |
|  | http.proxy.domain |  |  |
|  | http.proxy.user |  |  |
|  | http.proxy.password |  |  |
|  | jms.reply.destination | a string | the reply-to destination in an outbound message |
|  | jms.reply.timeout | an int | timeout in milliseconds for waiting for two-way reply |
|  | ws-adddressing.headers | true(default)/false | Enable/disable the WS-Addressing headers for outgoing soap requests |
<a id="endpoint-configuration--sample-file"></a>

### Sample file

[sample.endpoint.txt](assets/files/sample-endpoint_ad85f9b517bbf381.txt)

Download, remove the '.txt' prefix, customize then enjoy...

<a id="endpoint-configuration--implementation-details-for-outbound-services"></a>

### Implementation Details for Outbound services

The properties related to Outbound services have to be applied to Axis2 (for SOAP services) or HttpClient (for HTTP services).
Tables below sum up this information.

<a id="endpoint-configuration--soap-services-axis2"></a>

#### SOAP Services (Axis2)

For Axis2, all properties are converted to meet the [Options#setProperty()](http://ws.apache.org/axis2/1_3/api/org/apache/axis2/client/options.html#setproperty(java.lang.string,%20java.lang.object).html)  requirements.

| Property name | Axis2 | Description/Notes |
| --- | --- | --- |
| http.request.chunk | `Options.setProperty(HTTPConstants.CHUNKED, ?)` |  |
| http.protocol.version | `Options.setProperty(HTTPConstants.HTTP_PROTOCOL_VERSION, ?)` |  |
| http.request.gzip | `Options.setProperty(HTTPConstants.MC_GZIP_REQUEST, ?)` |  |
| http.accept.gzip | `Options.setProperty(HTTPConstants.MC_ACCEPT_GZIP, ?)` |  |
| http.protocol.content-charset | `Options.setProperty(Constants.Configuration.CHARACTER_SET_ENCODING,?)` |  |
| http.default-headers.\* | `Options.setProperty(HTTPConstants.HTTP_HEADERS, ?)` |  |
| http.connection.timeout | `Options.setProperty(HTTPConstants.CONNECTION_TIMEOUT, ?)` |  |
| http.socket.timeout | `Options.setProperty(HTTPConstants.SO_TIMEOUT, ?)` |  |
| http.protocol.max-redirects |  | not applied to Axis2 service |
| http.proxy.\* | `Options.setProperty(HTTPConstants.PROXY, ?)` |  |
| jms.reply.destination | `Options.setProperty(JMSConstants.REPLY_PARAM, ?)` |  |
| jms.reply.timeout | `Options.setProperty(JMSConstants.JMS_WAIT_REPLY, ?)` |  |
<a id="endpoint-configuration--http-services-httpclient"></a>

#### HTTP Services (HttpClient)

For HttpClient, all properties are defined by: [HttpMethodParams](http://hc.apache.org/httpclient-3.x/apidocs/org/apache/commons/httpclient/params/httpmethodparams.html.html) , HostParams, HttpClientParams, HttpConnectionParams and HttpConnectionManagerParams.
The idea is to convert properties into the expected type and push them in a [`DefaultHttpParams`](http://hc.apache.org/httpclient-3.x/apidocs/org/apache/commons/httpclient/params/defaulthttpparams.html.html) . This property holder is then set as the parent of all other `HttpParams` used.
If a given property is not listed below, you are still able to set it as long as the expected value is a string. For instance ["http.protocol.cookie-policy"](http://hc.apache.org/httpclient-3.x/apidocs/org/apache/commons/httpclient/params/HttpMethodParams.html#COOKIE_POLICY) can be set seamlessly.

| Property name | HttpClient | Description/Notes |
| --- | --- | --- |
| http.request.chunk | EntityEnclosingMethod.setContentChunked() |  |
| http.protocol.version | HttpParams.setParameter(HttpMethodParams.PROTOCOL\_VERSION, ?) |  |
| http.request.gzip |  | *not supported* |
| http.accept.gzip |  | *not supported* |
| http.protocol.content-charset | HttpParams.setParameter(HttpMethodParams.HTTP\_CONTENT\_CHARSET,?) |  |
| http.default-headers.\* | HttpParams.setParameter(HTTPConstants.HTTP\_HEADERS, ?) |  |
| http.connection.timeout | HttpParams.setParameter(HttpConnectionParams.CONNECTION\_TIMEOUT, ?) |  |
| http.socket.timeout | HttpParams.setParameter(HttpMethodParams.SO\_TIMEOUT, ?) |  |
| http.protocol.max-redirects | HttpParams.setParameter(HttpClientParams.MAX\_REDIRECTS, ?) |  |
| http.proxy.\* |  | Cannot be set with simple properties. Custom code added. |
<a id="endpoint-configuration--additional-configuration-for-soap-endpoints"></a>

## Additional Configuration for SOAP Endpoints

If you deploy ODE in an application server, the [Axis2 Integration Layer](#developerguide-architectural-overview--odeintegrationlayers.html) allows ODE to communicate via Web Service interactions. SOAP Web Services will be managed by Axis2. These web services may be configured dynamically.
For each service, you need to place a `[serviceLocalName].axis2` file at the root of the process bundle. Currently, this file can only be added on the server, under `ode/WEB-INF/processes/$your_process`.

For example, given this wsdl:

```
<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions ...>
  <wsdl:documentation xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">A sample Time service</wsdl:documentation>
 ...
  <wsdl:service name="TimeService">
    <wsdl:port name="TimeServiceSoap" binding="tns:TimeServiceSoap">
      <soap:address location="http://ws.intalio.com/TimeService/" />
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

You would place a `TimeService.axis2` file with:

```
<service
name=
"TimeService"
scope=
"application"
targetNamespace=
"http://ws.intalio.com/TimeService/"
> <module ref="sandesha2"/> <module ref="addressing"/> </service>
```

This will engage Engage sandesha2 and addressing modules.

On every request, if the config file has not been polled during the last 30 seconds then check the file for changes and (re)load it if any.

For further details about the type of parameters that can be set, see [Axis2 Service Config](http://ws.apache.org/axis2/1_0/axis2config.html#Service_Configuration).

This mechanism is available for external SOAP services -- i.e. services that processes invoke -- and for SOAP services exposed by ODE -- i.e. services exposed by BPEL processes.

The `service.xml` could be quite powerful. However all options are not accessible this way. Many settings are available programmatically only using the [Options class.](http://ws.apache.org/axis2/1_3/api/org/apache/axis2/client/options.html.html). ODE exposes these settings through an additional property file described in the previous section.

---

<a id="http-authentication"></a>

<!-- source_url: https://ode.apache.org/http-authentication.html -->

<!-- page_index: 22 -->

<a id="http-authentication--overview"></a>

## Overview

This section explains how to perform authentication against Web services requiring HTTP basic, digest or NTLM authentication mechanisms.

> [!NOTE]
> <a id="http-authentication--non-standard"></a>

>
> > [!NOTE]
> > #### Non-Standard
>
> This mode of authentication is non-standard in the Web service world because the authentication data is passed outside of the SOAP message. This feature is still experimental and requires ODE >1.1
<a id="http-authentication--authentication-element-and-message-part"></a>

## Authentication element and message part

To perform authentication, you must pass an additional message part containing the general `authentication` element which contains the credentials (as plain-text strings)

Authenticate Message Part Content

```
<auth:authenticate xmlns:auth="urn:ode.apache.org/authentication">
    <auth:username/>?
    <auth:password/>?
    <auth:domain/>?     <!-- NTLM specific -->
    <auth:realm/>?      <!-- NTLM specific -->
    <auth:token/>?
</auth:authenticate>
```

This additional message part may be declared in the WSDL definition to allow tools to validate the data structure:

MyService.wsdl

```
<?xml version='1.0' encoding='utf-8'?>
<wsdl:definitions
xmlns:tns=
"http://www.example.com"
xmlns:soap=
"http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:xs=
"http://www.w3.org/2001/XMLSchema"
xmlns:wsdl=
"http://schemas.xmlsoap.org/wsdl/"
xmlns:auth=
"urn:ode.apache.org/authentication"
targetNamespace=
"http://example.com"
> <wsdl:import namespace="urn:ode.apache.org/authentication" location="Authentication.xsd"/> <wsdl:message name="MyRequest" > <wsdl:part name="body" element="tns:HelloText"/> <wsdl:part name="authenticate" element="auth:authenticate"/> <!-- Additional part --> </wsdl:message> </wsdl:definitions>
```

Notes:
 *The message part does not have to be named `authenticate`, it is only suggested as descriptive name.* The message part should not be referenced as SOAP header or SOAP body in the binding.
\* If you are using Document-Literal style binding, make sure that your body binding references the body part, because you now have more than one part in the message definition.

<a id="http-authentication--the-authenticate-element-schema"></a>
<a id="http-authentication--the-authenticate-element-schema."></a>

### The "authenticate" element schema.

The schema of the `authenticate` element follows:

Authenticate.xsd

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema
xmlns:xs=
"http://www.w3.org/2001/XMLSchema"
targetNamespace=
"urn:ode.apache.org/authentication"
elementFormDefault=
"qualified"
> <xs:element name="authenticate" > <xs:complexType> <xs:sequence> <xs:element name="username" type="xs:string" minOccurs="0" maxOccurs="1"/> <xs:element name="password" type="xs:string" minOccurs="0" maxOccurs="1"/> <xs:element name="domain" type="xs:string" minOccurs="0" maxOccurs="1"/> <xs:element name="realm" type="xs:string" minOccurs="0" maxOccurs="1"/> <xs:element name="token" minOccurs="0" maxOccurs="1" > <xs:complexType> <xs:sequence> <xs:any minOccurs="1"/> </xs:sequence> </xs:complexType> </xs:element> </xs:sequence> </xs:complexType> </xs:element> </xs:schema>
```

You can add this schema to your project to allow tools to display/validate the correct element structure.

---

<a id="using-a-jndi-datasource-under-servicemix-jbi"></a>

<!-- source_url: https://ode.apache.org/using-a-jndi-datasource-under-servicemix-jbi.html -->

<!-- page_index: 23 -->

<a id="using-a-jndi-datasource-under-servicemix-jbi--overview"></a>

## Overview

These instructions will help you configure a JNDI DataSource for Apache ODE when running inside the ServiceMix JBI container.

<a id="using-a-jndi-datasource-under-servicemix-jbi--1-edit-servicemixconfjndixml"></a>
<a id="using-a-jndi-datasource-under-servicemix-jbi--1.-edit-servicemix-conf-jndi.xml"></a>

## 1. Edit $SERVICEMIX/conf/jndi.xml

Declare a managed connection factory pointing to your database:

```
<bean
id=
"odeManagedConnectionFactory"
class=
"org.jencks.tranql.DataSourceMCF"
> <property name="driverName" value="com.mysql.jdbc.Driver"/> <property name="url" value="jdbc:mysql://hostname/databaseName"/> <property name="user" value="username"/> <property name="password" value="myPassword"/> </bean>
```

And register the DataSource in the JNDI registry by adding an `<entry>` under the `<util:map>` element:

```
<util:map
id=
"jndiEntries"
> <!-- ODE DataSource --> <entry key="java:comp/env/jdbc/ode" > <bean id="odeDataSource" class="org.jencks.factory.ConnectionFactoryFactoryBean" > <property name="managedConnectionFactory" ref="odeManagedConnectionFactory"/> <property name="connectionManager" ref="connectionManager"/> </bean> </entry> <!-- ... other entries follow... --> </util:map>
```

<a id="using-a-jndi-datasource-under-servicemix-jbi--2-edit-ode-jbiproperties"></a>
<a id="using-a-jndi-datasource-under-servicemix-jbi--2.-edit-ode-jbi.properties"></a>

## 2. Edit ode-jbi.properties

In ode-jbi.properties, set the following properties:

```
ode-jbi.db.mode
=
EXTERNAL
ode-jbi.db.ext.dataSource
=
java:comp/env/jdbc/ode
```

(Be sure to match the JNDI lookup name to the one defined in $SERVICEMIX/conf/jndi.xml)

<a id="using-a-jndi-datasource-under-servicemix-jbi--3-add-jencks-20-all-library"></a>
<a id="using-a-jndi-datasource-under-servicemix-jbi--3.-add-jencks-2.0-all-library"></a>

## 3. Add jencks-2.0-all library

Copy [jencks-2.0-all.jar](http://repository.codehaus.org/org/jencks/jencks/2.0/jencks-2.0-all.jar) under $SERVICEMIX/lib

<a id="using-a-jndi-datasource-under-servicemix-jbi--4-restart-servicemix"></a>
<a id="using-a-jndi-datasource-under-servicemix-jbi--4.-restart-servicemix"></a>

## 4. Restart ServiceMix

And you're done! Don't forget to redeploy your service assemblies since they need to be re-synchronized with ODE.

<a id="using-a-jndi-datasource-under-servicemix-jbi--extras"></a>

## Extras

<a id="using-a-jndi-datasource-under-servicemix-jbi--connection-pool-parameters"></a>

### Connection Pool Parameters

If you want to manually configure the connection pool parameters, edit $SERVICEMIX/conf/tx.xml and update the "poolingSupport" object. For example,

```
<jencks:poolingSupport
id=
"poolingSupport"
connectionMaxIdleMinutes=
"5"
connectionMaxWaitMilliseconds=
"10000"
poolMaxSize=
"100"
poolMinSize=
"20"
/>
```

---

<a id="writing-bpel-test-cases"></a>

<!-- source_url: https://ode.apache.org/writing-bpel-test-cases.html -->

<!-- page_index: 24 -->

<a id="writing-bpel-test-cases--overview"></a>

## Overview

ODE has a test framework to automatically run BPEL processes. A big part of our test harness is therefore many different BPEL processes that test specific BPEL configurations or interactions. If you run into a problem with one of your processes that seems to be a bug, the best way to get it fixed is to contribute a test case to the project. We'll run it and keep it to prevent regressions. The more test cases we have, the more robust ODE will be.

This small guide will just explain you how to write and structure a test case to include it in ODE's test suite. For those who rather have examples than explanations, you can already check all [existing test cases](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/).

<a id="writing-bpel-test-cases--bpel-constraints"></a>

### BPEL Constraints

An automated test system has to make some assumptions about your test cases to reduce the complexity of running them. Therefore ODE's test framework can't run absolutely any process. There are a couple of limitations to be aware of:

- Your process must start with a receive and end with a matching reply. The result produced by the reply is what will be validated.
- Invoking external web services during the execution is not possible, test cases must be self-contained as BPEL processes. However we'll see later that a couple of predefined mocked services can be invoked.

Other than that your process can do anything and can use all the WSDL, schemas and XSL stylesheets you need.

<a id="writing-bpel-test-cases--test-descriptor"></a>

### Test Descriptor

So to begin with your test process must at least have a [BPEL file](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/HelloWorld2/HelloWorld2.bpel), a [WSDL file](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/HelloWorld2/HelloWorld2.wsdl) and the standard [deploy.xml](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/HelloWorld2/deploy.xml) deployment descriptor (links are provided for the HelloWorld test case). All of these should be included in a single directory.

Then for the test framework to know what it should do you will also need to write a simple test descriptor. It's a simple properties file saying which service is implemented by the process and which messages should be sent to start it and make it continue. It should me named test?.properties with the '?' being a increasing number. Here is the descriptor for the HelloWorld example, in test1.properties:

```
namespace =http://ode/bpel/unit-test.wsdl service =HelloService operation =hello request1 =<message><TestPart>Hello</TestPart></message> response1 =.*Hello World.*
```

The 3 first lines specify the namespace, the name and the operation to which messages will be sent. Then comes the request message. It should always be named request?, and should always be wrapped in a message element and another element named like the message part. Finally, and most importantly, comes the response test pattern. It's a regular expression that will be checked against the response produced by the process. If the expression can't be found, the test fails. In the HelloWorld example here we're just testing that our response includes 'Hello World'.

A test descriptor can contain more that one request/response couple, allowing several executions of a same process, testing different input/output combinations. You just need to increase the numbers in the request and response property names. For an example see the [descriptor of the flow test](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/TestFlowActivity1/test.properties).

Also if your process needs to receive several messages, you can have several test descriptors, each corresponding to a message. The files should just be named test1.properties, test2.properties, ... following the order of invocation. Here is an example with 2 descriptors used by the correlation test case:

test1.properties

```
namespace =http://ode/bpel/unit-test/testCorrelation.wsdl service =testCorrelationService operation =request request1 =<message><requestMessageData><testMessage><requestID>Start Test5.1</requestID><requestText>Event Start Test5.1</requestText><requestEnd>no</requestEnd></testMessage></requestMessageData></message> response1 =ASYNC
```

test2.properties

```
namespace =http://ode/bpel/unit-test/testCorrelation.wsdl service =testCorrelationService operation =continue request1 =<message><requestMessageData><testMessage><requestID>Start Test5.1</requestID><requestText>Event Start Test5.2.1</requestText><requestEnd>yes</requestEnd></testMessage></requestMessageData></message> response1 =.*Event Start Test5.1 -&gt; loop on receive until message includes requestEnd = yes -&gt; received message -&gt ; process complete.*
```

Finally a response can be marked as being ASYNC in the case no reply is expected for a given receive. This only applies to non instantiating receives:

```
response1
=
ASYNC
```

<a id="writing-bpel-test-cases--mocked-services-toolkit"></a>

### Mocked Services Toolkit

Writing isolated BPEL processes isn't something easy and for more advanced test cases you often need a bit more. The test framework therefore includes 2 mocked services to help you: the probe service and the fault service. Be aware however that the usage of these services require a bit more understanding on the BPEL that you're going to execute.

<a id="writing-bpel-test-cases--probe-service"></a>

#### Probe Service

The probe service makes it easy to track the path that has been taken by a process execution by appending strings that are specific to one execution case. It basically takes a string that you pass and appends it to a global process execution string that you can test in the end. Let's see with a pseudo-code example:

```
receive(foo)
probe("received message " + foo.name)
if (foo.value > 50)
  probe("big value")
else
  probe("small value")
end
reply(probeStr)
```

Once this has been executed you can check whether the probeStr produced as a reply contains both "received message" and "big value" or "received message" and "small value" using a response regular expression.

Practically the probe service takes 2 parts: probeName and probeData. The probeName part should contain what you wnat to append, the probeData part will contain the appended string after the call and shouldn't be modified once it's been initialized. The probeData part will effectively contain the successive appended strings and that's what you're going to test at the end of the execution.

Here is a usage example extracted from the [correlation test case](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/TestCorrelation/testCorrelation.bpel):

```
<receive
name=
"receive1"
partnerLink=
"request"
portType=
"wns:testCorrelationPT"
operation=
"request"
variable=
"request"
createInstance=
"yes"
> <correlations> <correlation set="testCorr1" initiate="yes"/> </correlations> </receive> <!-- Copy input variables to internal accumulators --> <assign name="assign1" > <copy> <from variable="request" property="wns:testProbeID"/> <to variable="probeInput" part="probeName"/> </copy> <copy> <from variable="request" property="wns:testProbeData"/> <to variable="probeInput" part="probeData"/> </copy> </assign> <assign> <copy> <from> <literal> <![CDATA[loop on receive until message includes requestEnd = yes]]> </literal> </from> <to variable="probeInput" part="probeName"/> </copy> </assign> <invoke name="probe" partnerLink="probe" portType="prb:probeMessagePT" operation="probe" inputVariable="probeInput" outputVariable="probeInput"/>
```

The first assign initializes the probe parts with the input message. The second one places in probeName the text that should be appended. After the call to the probe service, probeData will contain both information appended. Then to return the probeData at the end of the execution:

```
<assign
name=
"assign2"
> <copy> <from variable="probeInput" part="probeName"/> <to variable="reply" part="replyID"/> </copy> <copy> <from variable="probeInput" part="probeData"/> <to variable="reply" part="replyText"/> </copy> </assign> <reply name="reply" partnerLink="request" portType="wns:testCorrelationPT" operation="continue" variable="reply"/>
```

The returned data is finally tested by using a nice regular expression for the response:

```
response1
=
.*Event Start Test5.1 -&gt; loop on receive until message includes requestEnd = yes -&gt;
received
message
-&gt
; process complete.*
```

A complete usage example can be found with the [correlation test case](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/TestCorrelation/).

<a id="writing-bpel-test-cases--fault-service"></a>

#### Fault Service

When invoked, the fault service (as the name says) will return a fault. It's mostly used to test fault handlers and compensation. To invoke the fault service just use:

```
<invoke
name=
"throwTestFault"
partnerLink=
"fault"
portType=
"flt:faultMessagePT"
operation=
"throwFault"
inputVariable=
"fault"
outputVariable=
"faultResponse"
/>
```

The only types of fault that can be thrown for now are FaultMessage1, FaultMessage2 and UnknownFault in the http://ode/bpel/unit-test/FaultService.wsdl namespace. For more details see the example in the [implicit fault handler test](http://svn.apache.org/repos/asf/ode/trunk/bpel-test/src/test/resources/bpel/2.0/TestImplicitFaultHandler/).

---

<a id="ws-security-in-ode"></a>

<!-- source_url: https://ode.apache.org/ws-security-in-ode.html -->

<!-- page_index: 25 -->

<a id="ws-security-in-ode--how-to-use-ws-security-in-ode"></a>

## How to use WS-Security in ODE?

> [!NOTE]
> <a id="ws-security-in-ode--only-in-1.3.2"></a>

>
> > [!NOTE]
> > #### Only in 1.3.2+

ODE 1.3.2 introduces support for WS-Security: secure services can now be invoked from a process, and the process service itself might be secured. A first part will explain how to invoke a secured service, a second part how to secure the process service.

ODE has an [Integration Layer based on Axis2](#developerguide-architectural-overview--ode-integration-layers) so using Rampart, the Axis2 security modules, goes without saying. As a result this section will only focus on Rampart integration. Rampart and WS-Security specifications won't be detailed here. Please refer to their ad-hoc documentations for further details.

<a id="ws-security-in-ode--quick-rampart-introduction"></a>

### Quick Rampart introduction

As any other Axis2 module, Rampart is configurable with [Axis2 Service configuration files](http://ws.apache.org/axis2/1_0/axis2config.html#Service_Configuration). For instance a service.xml document, using the parameter based configuration model, might be:

```
<service>

    <module ref="rampart" />

    <parameter name="OutflowSecurity">
      <action>
        <items>Timestamp Signature</items>
        <user>client</user>
        <signaturePropFile>TestRampartBasic/secured-services/client.properties</signaturePropFile>
        <passwordCallbackClass>org.apache.rampart.samples.sample04.PWCBHandler</passwordCallbackClass>
        <signatureKeyIdentifier>DirectReference</signatureKeyIdentifier>
      </action>
    </parameter>

    <parameter name="InflowSecurity">
      <action>
        <items>Timestamp Signature</items>
        <signaturePropFile>TestRampartBasic/secured-services/client.properties</signaturePropFile>
      </action>
    </parameter>

 </service>
```

Another example using WS-Security Policy based configuration model is listed below. See the full document [here](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartPolicy/secured-services/process-sample04_policy_in_service.xml/sample04-policy.axis2?view=markup).

```
<service>

    <module ref="rampart"/>

    <wsp:Policy wsu:Id="SecConvPolicy2" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy">
        <wsp:ExactlyOne>
            <wsp:All>
                <sp:SymmetricBinding xmlns:sp="http://schemas.xmlsoap.org/ws/2005/07/securitypolicy">
                    <wsp:Policy>
                             <!-- truncated, see original document ny following the link above -->
                    </wsp:Policy>
                </sp:SymmetricBinding>
                <sp:Wss11 xmlns:sp="http://schemas.xmlsoap.org/ws/2005/07/securitypolicy">
                    <wsp:Policy>
                             <!-- truncated, see original document ny following the link above -->
                    </wsp:Policy>
                </sp:Wss11>
                <sp:Trust10 xmlns:sp="http://schemas.xmlsoap.org/ws/2005/07/securitypolicy">
                    <wsp:Policy>
                             <!-- truncated, see original document ny following the link above -->
                    </wsp:Policy>
                </sp:Trust10>
                <sp:EncryptedParts xmlns:sp="http://schemas.xmlsoap.org/ws/2005/07/securitypolicy">
                    <sp:Body/>
                </sp:EncryptedParts>
                <ramp:RampartConfig xmlns:ramp="http://ws.apache.org/rampart/policy">
                    <ramp:user>client</ramp:user>
                    <ramp:encryptionUser>service</ramp:encryptionUser>
                    <ramp:passwordCallbackClass>org.apache.rampart.samples.policy.sample04.PWCBHandler</ramp:passwordCallbackClass>

                    <ramp:signatureCrypto>
                        <ramp:crypto provider="org.apache.ws.security.components.crypto.Merlin">
                            <ramp:property name="org.apache.ws.security.crypto.merlin.keystore.type">JKS</ramp:property>
                            <ramp:property name="org.apache.ws.security.crypto.merlin.file">TestRampartPolicy/secured-services/client.jks</ramp:property>
                            <ramp:property name="org.apache.ws.security.crypto.merlin.keystore.password">apache</ramp:property>
                        </ramp:crypto>
                    </ramp:signatureCrypto>
                    <ramp:encryptionCypto>
                        <ramp:crypto provider="org.apache.ws.security.components.crypto.Merlin">
                            <ramp:property name="org.apache.ws.security.crypto.merlin.keystore.type">JKS</ramp:property>
                            <ramp:property name="org.apache.ws.security.crypto.merlin.file">TestRampartPolicy/secured-services/client.jks</ramp:property>
                            <ramp:property name="org.apache.ws.security.crypto.merlin.keystore.password">apache</ramp:property>
                        </ramp:crypto>
                    </ramp:encryptionCypto>

                </ramp:RampartConfig>
            </wsp:All>
        </wsp:ExactlyOne>
    </wsp:Policy>

</service>
```

The important thing to notice is that these documents are plain [Axis2 Service configuration files](http://ws.apache.org/axis2/1_0/axis2config.html#Service_Configuration). And as explained in the [ODE User Guide](#endpoint-configuration--additional-configuration-for-soap-endpoints), a mechanism to handle these files already exists. So all we have to do is reuse this mechanism, the rest is pure Rampart configuration.

Let's take an example and see the actual required steps.

<a id="ws-security-in-ode--how-to-invoke-a-secure-web-service"></a>

### How to invoke a secure web service?

<a id="ws-security-in-ode--prepare-your-service-document"></a>

#### Prepare your service document

Assuming your process needs to invoke the secure service {http://sample03.policy.samples.rampart.apache.org}Sample03, the *first step* is to prepare a service document named ${process\_bundle\_dir}/Sample03.axis2 and containing your desired Rampart configuration.

The *second step* is to to make sure the resources needed to invoke the services are available to Rampart through ODE webapp classpath. Typical resources are:

- password callback handler classes
- Java keystores
- property files containing keystore information

<a id="ws-security-in-ode--add-resources-to-ode-webapp-classpath"></a>

#### Add resources to ODE webapp classpath

How you add these resources to ODE classpath might vary depending on your application server, your global architecture or other criteria. So it's up to you to figure this out. However typical locations are:

- ode/WEB-INF/classes
- ode/WEB-INF/lib

<a id="ws-security-in-ode--an-alternative-for-ws-security-policies"></a>

#### An alternative for WS-Security Policies

If you're using the policy base configuration model, an alternative is available to you: use the [endpoint property mechanism](#endpoint-configuration) to attach the policy to the service. In that configuration, ODE will engage the Rampart module and load the policy when the service is invoked.

To do so:

- save the Policy document (not the service document) in the file of your choice. For instance mypolicy.xml
- create an endpoint file linking the service and the policy file. Basically with the two properties listed below. Note that if the path assigned to the "security.policy.file" property is relative it will be resolved against the process bundle directory. Of course if the path is absolute, it will be used as is.

```
alias.sample03-ns
=
http://sample03.policy.samples.rampart.apache.org
sample03-ns.sample03-policy.ode.security.policy.file
=
mypolicy.xml
```

<a id="ws-security-in-ode--how-to-secure-the-web-service-exposed-by-a-process"></a>

### How to secure the web service exposed by a process?

Applying security to a process service is no different from invoking a secured service. If the process service you're exposing is {http://mycompany.com}AbscenceRequest. All you have to do is prepare a service document named ${process\_bundle\_dir}/AbscenceRequest.axis2 and containing your Rampart configuration. Once again, it's up to you to add the required resources in ODE webapp classpath.

You can also use the property 'security.policy.file' to secure the process service.

<a id="ws-security-in-ode--do-i-need-to-install-rampart-myself"></a>

### Do I need to install Rampart myself?

No. ODE comes with the following Axis2 modules (and the jars they depend on): Rampart, Rahas and Addressing.

<a id="ws-security-in-ode--useful-resources"></a>

### Useful resources

<a id="ws-security-in-ode--rampart-material"></a>

#### Rampart material

- the [list](http://wso2.org/projects/rampart/java) of Web Services Security specifications supported by Rampart
- [Rampart articles](http://ws.apache.org/rampart/articles.html)
- [Rampart samples](http://ws.apache.org/rampart/samples.html)
- [a Rampart tutorial](https://wiki.internet2.edu/confluence/display/GrouperWG/The+Newcastle+University+Grouper+page)

<a id="ws-security-in-ode--ode-test-cases"></a>

### ODE test cases

<a id="ws-security-in-ode--how-to-run-them"></a>

#### How to run them

```
$ cd axis2-war
$ buildr test:Secure
```

<a id="ws-security-in-ode--where-are-the-processes-executed-by-the-unit-tests"></a>

#### Where are the processes executed by the unit tests?

The executed processes are generated by the build, so run the tests once, then look into the following directories. Process directories are prefixed with "process-".

- axis2-war/target/test-classes/TestRampartPolicy/secured-services/
- axis2-war/target/test-classes/TestRampartPolicy/secured-processes/
- axis2-war/target/test-classes/TestRampartBasic/secured-services/
- axis2-war/target/test-classes/TestRampartBasic/secured-processes/

<a id="ws-security-in-ode--the-nitty-gritty-details"></a>

#### the nitty-gritty details

The integration with Rampart described in this section is tested with a decent suite of unit tests. These unit tests are based on the [Rampart samples](http://ws.apache.org/rampart/samples.html). The [related resources](http://svn.apache.org/repos/asf/webservices/rampart/branches/java/1_3/modules/rampart-samples/) were imported into ODE repository.

These tests are divided into two parts: tests using the parameter base configuration model aka "basic tests" and tests using the policy base configuration model aka "policy tests".

ODE test cases reuse these test cases in two different scenarii:

- the security configuration is applied to an "external" web service, and a ODE process invokes it.
- the security configuration is applied to the web service exposed by a process.

These partitions lead to four resource directories:

- [TestRampartBasic/secured-services](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartBasic/secured-services/)
- [TestRampartBasic/secured-processes](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartBasic/secured-processes/)
- [TestRampartPolicy/secured-services](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartPolicy/secured-services/)
- [TestRampartPolicy/secured-processes](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartPolicy/secured-processes/)

Everything describes for TestRampartBasic applies to TestRampartPolicy. So for now on we will mention only TestRampartBasic.

For the "secured-services" scenario, the "external" web services are Axis [archives](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartBasic/secured-services/services/) deployed in an Axis2 webapp.

The corresponding unit test classes are [SecuredServicesTest.java and SecuredProcessTest.java](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/java/org/apache/ode/axis2/rampart/basic/). Each test class will start a list of processes that must succeed (as many processes as Rampart samples actually).

To avoid duplication these processes are generated by the build based on two process templates: [one](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartBasic/secured-services/process-template/) for the secured-services case, [another](http://svn.apache.org/viewvc/ode/branches/APACHE_ODE_1.X/axis2-war/src/test/resources/TestRampartBasic/secured-processes/process-template/) for the secured-processes case.

The build generates processes into:

- axis2-war/target/test-classes/TestRampartPolicy/secured-services/process-\*
- axis2-war/target/test-classes/TestRampartPolicy/secured-processes/process-\*
- axis2-war/target/test-classes/TestRampartBasic/secured-services/process-\*
- axis2-war/target/test-classes/TestRampartBasic/secured-processes/process-\*

---

<a id="use-assign-to-build-messages"></a>

<!-- source_url: https://ode.apache.org/use-assign-to-build-messages.html -->

<!-- page_index: 26 -->

<a id="use-assign-to-build-messages--use-assign-to-build-whole-message-at-once-all-parts"></a>

## Use Assign to build whole message at once (all parts)

Let's say you have WSDL parts defined as follow:

```
<wsdl:message
name=
"HelloMessage"
> <wsdl:part name="part1" type="xsd:string"/> <wsdl:part name="part2" type="xsd:string"/> </wsdl:message>
```

In order to build whole message at once, you need to use following statement:

```
<assign>
    <copy>
        <from><literal><message xmlns=""><part1>abc1</part1><part2>abc2</part2></message></literal></from>
        <to>$myVar</to>
    </copy>
</assign>
```

Complete BPEL example is provided here: [TestMultiPartMessage](https://svn.apache.org/repos/asf/ode/trunk/axis2-war/src/test/resources/TestMultiPartMessage)

---

<a id="jbi-deployment"></a>

<!-- source_url: https://ode.apache.org/jbi-deployment.html -->

<!-- page_index: 27 -->

# JBI Deployment

---

**This feature is no more supported from ODE Release 1.3.7**

---

<a id="jbi-deployment--overview"></a>

## Overview

Here's a quick overview to deploy ODE on a JBI container (e.g. [ServiceMix](http://servicemix.apache.org))

<a id="jbi-deployment--1-download-the-jbi-distribution"></a>

## 1) Download the JBI distribution

Check our [download page](#getting-ode) and get the latest JBI-based distribution. Unzip it in a directory of your choice. We'll now refer to this directory as ODE\_HOME.

<a id="jbi-deployment--2-install-on-jbi-container"></a>

## 2) Install on JBI container

For example, with ServiceMix you can use file-system deployment:

```
(from ode/jbi directory)
cp ODE_HOME/ode-jbi-1.1.zip SERVICEMIX_DIR/install
```

The above will result in ODE being installed with the default settings. You may wish to first modify the `ode-jbi.properties` file found in the root of the installer ZIP.

<a id="jbi-deployment--3-deploying-processes"></a>

### 3) Deploying Processes

We are assuming that the reader is familiar with JBI deployment concepts. Deploying a process consists of the following steps:

1. Create a temporary *service unit* directory for the BPEL processes
2. Place the relevant `.bpel`, `.wsdl` and `.xsd` files into the temporary directory
3. Create an ODE deployment descriptor (`[deploy.xml](deploy.xml.html)`) and place it in the temporary directory
4. (Optional) Compile the the BPEL processes using the `[bpelc](bpelc.html)` command.
5. Zip up the contents of the temporary directory into a service unit archive
6. Create a temporary *service assembly* directory
7. Place the service unit archive in a temporary *service assembly* directory
8. Update the service assembly's `jbi.xml` descriptor
9. Zip up the contents of the service assembly directory into a service assembly archive
10. Copy the service assembly archive into the appropriate *deploy* directory

<a id="jbi-deployment--examples"></a>

## Examples

Some JBI examples are available under the *examples* directory of the ODE distro:

- HelloWorld2
- PingPong
- Async2

Extract the distro-jbi-2.0-SNAPSHOT.zip created in the build instructions above.

To compile the examples, you may wish to define the ODE\_HOME environment variable. The build script does a good job of figuring this out without ODE\_HOME set, however.

```
# On Linux/Unix export ODE_HOME=/path/to/ode/distribution

# On Windows set ODE_HOME=C:\Path\To\ODE\Distribution
```

and run Ant in the example's directory:

```
cd %ODE_HOME%/examples/PingPong
ant
```

This will create a JBI service assembly in the "build" subdirectory. With ServiceMix you can simply copy it to the file-system hot deployment directory:

```
(from PingPong directory)
cp build/PingPing-sa.zip SERVICEMIX_DIR/deploy
```

Finally, you can test the example by typing:

```
(from PingPong directory)
ant test
```

<a id="jbi-deployment--jbi-endpoints"></a>

## JBI Endpoints

ODE now relies strictly on abstract web service definitions (i.e., without binding/service/port definitions), meaning that you only need abstract WSDLs when compiling processes. Since JBI uses normalized messages (in theory, at least), there is no need to define bindings for the BPEL service engine.

In deploy.xml, you simply define the JBI internal endpoints invoked or provided by your partnerLinks,

```
<?xml version="1.0" encoding="UTF-8"?>
<deploy xmlns="http://www.apache.org/ode/schemas/dd/2007/03"
        xmlns:process="urn:/Ping.bpel"
        xmlns:ping="urn:/Ping.wsdl"
        xmlns:pong="urn:/Pong.wsdl">

    <process name="process:Ping">
        <active>true</active>
        <provide partnerLink="PingPartnerLink">
            <service name="ping:PingService" port="PingPort"/>
        </provide>
        <invoke partnerLink="PongPartnerLink">
            <service name="pong:PongService" port="PongPort"/>
        </invoke>
    </process>

</deploy>
```

One may use JBI binding components to make services externally available and therefore providing concrete bindings to those binding components. An example of exposing process services via SOAP/HTTP can be found in the PingPong [ping-http service unit](http://svn.apache.org/repos/asf/ode/branches/APACHE_ODE_1.X/distro/src/examples-jbi/PingPong/ping-http/).

<a id="jbi-deployment--database"></a>

## Database

The generated installer will use an internally-managed embedded Derby database. No configuration is required. To use an external database one needs to modify `ode-jbi.properties` found in the component installer zip.

<a id="jbi-deployment--compatibility-caveat"></a>

## Compatibility Caveat

Many binding components are not very good about delivering messages in the correct format for WSDL11 services.

<a id="jbi-deployment--known-issues-with-servicemix"></a>

### Known Issues with ServiceMix

ServiceMix' so-called *lightweight components* make it difficult to properly expose process services since they do not fully implement the JBI contract and do not allow the process engine to enquire about its external endpoints.
\* SoapHelper needs to properly resolve the WSDL operation name (patch available)
<https://issues.apache.org/activemq/browse/SM-488>

- The servicemix-http binding component does not normalize messages

---

<a id="smx4-osgi-deployment"></a>

<!-- source_url: https://ode.apache.org/smx4-osgi-deployment.html -->

<!-- page_index: 28 -->

# Apache ODE – SMX4 OSGi Deployment

---

**This feature is no more supported from ODE Release 1.3.7**

---

<a id="smx4-osgi-deployment--deploy-apache-ode-osgi-bundle-and-example-process-ping-pong"></a>

## Deploy Apache ODE OSGi bundle and example process (Ping Pong)

Enter smx4 console and run following commands:

```
features:addUrl mvn:org.apache.ode/ode-jbi-karaf/1.3.6/xml/features
features:install ode
features:install examples-ode-ping-pong
```

This will install ODE with default settings (OpenJPA DAO, embedded Derby database)

<a id="smx4-osgi-deployment--configuring-database"></a>

## Configuring database

Create `SMX4/etc/org.apache.ode.jbi.cfg` file with following contents:

```
ode-jbi.pidNamespace
=
urn:ode-jbi
ode-jbi.allowIncompleteDeployment
=
false
ode-jbi.messageMapper
=
org.apache.ode.jbi.msgmap.ServiceMixMapper
ode-jbi.event.listeners
=
org.apache.ode.bpel.common.evt.DebugBpelEventListener
#For MySQL
#ode-jbi.db.int.mcf=org.tranql.connector.mysql.XAMCF
#ode-jbi.db.int.mcf.databaseName=ODE
#ode-jbi.db.int.mcf.userName=root
#ode-jbi.db.int.mcf.password=root
#ode-jbi.db.int.mcf.serverName=localhost
#For Postgres
#ode-jbi.db.int.mcf=org.tranql.connector.postgresql.PGXAMCF
#ode-jbi.db.int.mcf.databaseName=ODE
#ode-jbi.db.int.mcf.userName=postgres
#ode-jbi.db.int.mcf.password=postgres
#ode-jbi.db.int.mcf.serverName=localhost
#For SQLServer
#ode-jbi.db.int.mcf=org.tranql.connector.sqlserver.XAMCF
#ode-jbi.db.int.mcf.databaseName=ODE
#ode-jbi.db.int.mcf.userName=sa
#ode-jbi.db.int.mcf.password=sa
#ode-jbi.db.int.mcf.portNumber=1433
#ode-jbi.db.int.mcf.serverName=localhost
#For Oracle
ode-jbi.db.int.mcf
=
org.tranql.connector.oracle.LocalMCF
ode-jbi.db.int.mcf.databaseName
=
XE
ode-jbi.db.int.mcf.userName
=
ODE
ode-jbi.db.int.mcf.password
=
ode
ode-jbi.db.int.mcf.portNumber
=
1521
ode-jbi.db.int.mcf.serverName
=
localhost
ode-jbi.db.int.mcf.driverType
=
thin
# Uncomment the following to enable hibernate (this is recommended for production use):#ode-jbi.dao.factory=org.apache.ode.daohib.bpel.BpelDAOConnectionFactoryImpl
```

Please note that EXTERNAL database is currently not available in ServiceMix4, because it requires JNDI, which SMX4 doesn't support.

After choosing a particular database, we need to start ODE with required dependencies. There are 2 example features prepared in ode-jbi-karaf features (ode-hib-oracle and ode-hib-sqlserver).
So you need to run following command from Karaf console:

```
features:install ode-hib-oracle
```

Please note that `etc/org.apache.ode.jbi.cfg` must be set to the same database (in this case oracle) to load required dependencies properly.

<a id="smx4-osgi-deployment--tips"></a>

## Tips

<a id="smx4-osgi-deployment--how-to-make-pmapi-work"></a>

### How to make PMAPI work?

You can grab pmapi SA from here <http://markmail.org/message/ghigpzcpt2j3qnoo>.
Then edit SMX4 `etc/config.properties` and change from:

```
org.osgi.framework.bootdelegation
=
sun.*,com.sun*,javax.transaction,javax.transaction.*
```

to:

```
org.osgi.framework.bootdelegation
=
sun.*,com.sun*,javax.transaction,javax.transaction.*,javax.xml.stream,javax.xml.stream.*
```

---

<a id="getting-ode"></a>

<!-- source_url: https://ode.apache.org/getting-ode.html -->

<!-- page_index: 29 -->

<a id="getting-ode--releases"></a>

# Releases

*The latest stable release is Apache ODE 1.3.8*. All the built artifacts are also available in a [Maven2 repository](http://repo1.maven.org/maven2/org/apache/ode/).

*Note*: when downloading from a mirror please check the [md5sum](http://www.apache.org/dev/release-signing#md5) and verify the [OpenPGP](http://www.apache.org/dev/release-signing#openpgp) compatible signature from the main Apache site. Links are provided above (next to the release download link). This [KEYS](http://www.apache.org/dist/ode/KEYS) file contains the public keys used for signing releases. It is recommended that (when possible) a web of trust is used to confirm the identity of these keys. For more information, please see the [Apache Release FAQ](http://www.apache.org/dev/release.html).

<a id="getting-ode--138"></a>
<a id="getting-ode--1.3.8"></a>

# 1.3.8

Apache ODE 1.3.8 includes about 10 bug fixes and improvements. See the [changelog](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310270&version=12332764) for a complete list.

ODE 1.3.8 database schemas are now packaged within the distribution archives.

| Description | Files | PGP | SHA1 |
| --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.8.zip](http://www.apache.org/dyn/closer.cgi/ode/apache-ode-war-1.3.8.zip) | [pgp](https://www.apache.org/dist/ode/apache-ode-war-1.3.8.zip.asc) | [sha1](https://www.apache.org/dist/ode/apache-ode-war-1.3.8.zip.sha1) |
| Server Distribution | [apache-ode-server-1.3.8.zip](http://www.apache.org/dyn/closer.cgi/ode/apache-ode-server-1.3.8.zip) | [pgp](https://www.apache.org/dist/ode/apache-ode-server-1.3.8.zip.asc) | [sha1](https://www.apache.org/dist/ode/apache-ode-server-1.3.8.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.8.zip](http://www.apache.org/dyn/closer.cgi/ode/apache-ode-sources-1.3.8.zip) | [pgp](https://www.apache.org/dist/ode/apache-ode-sources-1.3.8.zip.asc) | [sha1](https://www.apache.org/dist/ode/apache-ode-sources-1.3.8.zip.sha1) |
<a id="getting-ode--archived-releases"></a>

# Archived Releases

<a id="getting-ode--137"></a>
<a id="getting-ode--1.3.7"></a>

## 1.3.7

Apache ODE 1.3.7 includes about 48 bug fixes and improvements. See the [changelog](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310270&version=12324967) for a complete list. Migration is necessary from 1.3.6, migration script available [here](https://github.com/apache/ode/blob/APACHE_ODE_1.3.7/schema-updates/migrate-ode-1.3.6-to-1.3.7.sql).

ODE 1.3.7 database schemas are now packaged within the distribution archives.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.7.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.3.7.zip) | [pgp](http://archive.apache.org/dist/ode/apache-ode-war-1.3.7.zip.asc) | [md5](http://archive.apache.org/dist/ode/apache-ode-war-1.3.7.zip.md5) | [sha1](http://archive.apache.org/dist/ode/apache-ode-war-1.3.7.zip.sha1) |
| Server Distribution | [apache-ode-server-1.3.7.zip](http://archive.apache.org/dist/ode/apache-ode-server-1.3.7.zip) | [pgp](http://archive.apache.org/dist/ode/apache-ode-server-1.3.7.zip.asc) | [md5](http://archive.apache.org/dist/ode/apache-ode-server-1.3.7.zip.md5) | [sha1](http://archive.apache.org/dist/ode/apache-ode-server-1.3.7.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.7.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.7.zip) | [pgp](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.7.zip.asc) | [md5](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.7.zip.md5) | [sha1](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.7.zip.sha1) |
<a id="getting-ode--136"></a>
<a id="getting-ode--1.3.6"></a>

## 1.3.6

Apache ODE 1.3.6 includes about 42 bug fixes and improvements. See the [changelog](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310270&version=12323509) for a complete list. No migration is necessary from 1.3.5.
The database schemas can be downloaded [here](#ode-schema).

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.6.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.3.6.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.3.6.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.3.6.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.3.6.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.3.6.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.3.6.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.6.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.6.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.6.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.6.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.6.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.6.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.6.zip.md5) | [sha1](https://www.apache.org/dist/ode/apache-ode-sources-1.3.6.zip.sha1) |
<a id="getting-ode--135"></a>
<a id="getting-ode--1.3.5"></a>

## 1.3.5

Apache ODE 1.3.5 includes about 30 bug fixes and performance improvements. The performance improvements affect XPath 2.0 processing in  activities or transition conditions and makes it up to 10 times faster than ODE 1.3.4. See the [changelog](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310270&styleName=Html&version=12314243) for a complete list. No migration is necessary from 1.3.4.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.5.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.3.5.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.3.5.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.3.5.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.3.5.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.3.5.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.3.5.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.5.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.5.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.5.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.5.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.5.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.5.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.5.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.5.zip.sha1) |
<a id="getting-ode--134"></a>
<a id="getting-ode--1.3.4"></a>

## 1.3.4

Apache ODE 1.3.4 includes about 100 bug fixes and improvements (among others: instance replaying, process deployments via OSGi bundles and spring configurable process properties. See the [changelog](https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12310270&styleName=Html&version=12314168) for a complete list. Migration is necessary from 1.3.2/1.3.3, please check the [upgrade](#upgrading-ode--from1.3.3to-1.3.4) page.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.4.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.3.4.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.3.4.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.3.4.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.3.4.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.3.4.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.3.4.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.4.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.4.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.4.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.4.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.4.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.4.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.4.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.4.zip.sha1) |
<a id="getting-ode--133"></a>
<a id="getting-ode--1.3.3"></a>

## 1.3.3

Apache ODE 1.3.3 is a security release for the process deployment web service, which was sensible to deployment messages with forged names. It also includes a few bug fixes and improvements. See the [changelog](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&&pid=12310270&status=5&status=6&fixfor=12313905&sorter/field=priority&sorter/order=DESC) for an exhaustive list. There are no migration necessary from 1.3.2, for other versions check the [upgrade](#upgrading-ode--from1.2to1.3.2) page if applicable.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.3.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.3.3.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.3.3.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.3.3.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.3.3.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.3.3.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.3.3.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.3.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.3.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.3.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.3.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.3.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.3.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.3.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.3.zip.sha1) |
<a id="getting-ode--20-beta2"></a>
<a id="getting-ode--2.0-beta2"></a>

## 2.0-beta2

The second beta of our experimental 2.0 branch. The next generation of the ODE engine adds reliability capabilities, improves on performance and open the way to better RESTful support. **However, we do not plan any further releases of this branch. Instead, we will focus on the main dev branch and will merge features from the experimental branch back to the 1.x release train**.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-2.0-beta2.zip](http://archive.apache.org/dist/ode/apache-ode-war-2.0-beta2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-2.0-beta2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-2.0-beta2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-2.0-beta2.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-2.0-beta2.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-2.0-beta2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-2.0-beta2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-2.0-beta2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-2.0-beta2.zip.sha1) |
| Source Distribution | [apache-ode-sources-2.0-beta2.zip](http://archive.apache.org/dist/ode/apache-ode-sources-2.0-beta2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-src-2.0-beta2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-src-2.0-beta2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-src-2.0-beta2.zip.sha1) |
<a id="getting-ode--132"></a>
<a id="getting-ode--1.3.2"></a>

## 1.3.2

Apache ODE 1.3.2 includes many features and improvements, among others: XQuery 1.0 in BPEL queries and expressions, Publish/Subscribe across process instances, WS-BPEL processes provided over JMS, WS-Security support, Process data clean up, better performance and memory management. As well as many bug fixes. See the [changelog](https://issues.apache.org/jira/browse/ODE/fixforversion/12313906) for an exhaustive list. Check the [upgrade](#upgrading-ode--from1.2to1.3.2) page if applicable.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.3.2.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.3.2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.3.2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.3.2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.3.2.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.3.2.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.3.2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.3.2.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.3.2.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.3.2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.3.2.zip.sha1) |
<a id="getting-ode--12"></a>
<a id="getting-ode--1.2"></a>

## 1.2

Apache ODE 1.2 packs new features as well as many small fixes and improvements. The features highlight is [external variables](#extensions-external-variables), support for the WSDL HTTP binding (allowing the invocation of REST style services) and advanced endpoint configurations. See the [changelog](https://issues.apache.org/jira/browse/ODE?report=com.atlassian.jira.plugin.system.project:changelog-panel) for the complete list of modifications and the [upgrade](#upgrading-ode--from1.1to1.2) page if applicable.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.2.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.2.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.2.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.2.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.2.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.2.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.2.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.2.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.2.zip.sha1) |
<a id="getting-ode--111"></a>
<a id="getting-ode--1.1.1"></a>

## 1.1.1

Apache ODE 1.1.1 is mostly an incremental release providing small improvements, bug fixes and more performance. See the [release notes](http://svn.apache.org/repos/asf/ode/tags/APACHE_ODE_1.1.1/RELEASE_NOTES) and the [JIRA changelog](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310270&fixfor=12312750).

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.1.1.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.1.1.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.1.1.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.1.1.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.1.1.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.1.1.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.1.1.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.1.1.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.1.1.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.1.1.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.1.1.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.1.1.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.1.1.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.1.1.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.1.1.zip.sha1) |
<a id="getting-ode--11"></a>
<a id="getting-ode--1.1"></a>

## 1.1

Apache ODE 1.1 is our first fully official release (outside of the Apache incubator). It adds a few more features, performance and usage improvements and many bug fixes. See the [release notes](http://svn.apache.org/repos/asf/ode/tags/APACHE_ODE_1.1RC2/RELEASE_NOTES) for more details about its content. The [JIRA changelog](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&mode=hide&sorter/order=DESC&sorter/field=priority&pid=12310270&fixfor=12312471) is also available.

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.1.zip](http://archive.apache.org/dist/ode/apache-ode-war-1.1.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-war-1.1.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-war-1.1.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-war-1.1.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.1.zip](http://archive.apache.org/dist/ode/apache-ode-jbi-1.1.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-jbi-1.1.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-jbi-1.1.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-jbi-1.1.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.1.zip](http://archive.apache.org/dist/ode/apache-ode-sources-1.1.zip) | [pgp](https://archive.apache.org/dist/ode/apache-ode-sources-1.1.zip.asc) | [md5](https://archive.apache.org/dist/ode/apache-ode-sources-1.1.zip.md5) | [sha1](https://archive.apache.org/dist/ode/apache-ode-sources-1.1.zip.sha1) |
<a id="getting-ode--10-incubating"></a>
<a id="getting-ode--1.0-incubating"></a>

## 1.0-incubating

This is the very first release of Apache ODE, done inside the incubator. For more information about its content, see the corresponding [release notes](http://svn.apache.org/repos/asf/ode/tags/APACHE_ODE_1.0-INCUBATING/RELEASE_NOTES).

| Description | Files | PGP | MD5 | SHA1 |
| --- | --- | --- | --- | --- |
| WAR Distribution | [apache-ode-war-1.0-incubating.zip](http://archive.apache.org/dist/incubator/ode/apache-ode-war-1.0-incubating.zip) | [pgp](https://archive.apache.org/dist/incubator/ode/apache-ode-war-1.0-incubating.zip.asc) | [md5](https://archive.apache.org/dist/incubator/ode/apache-ode-war-1.0-incubating.zip.md5) | [sha1](https://archive.apache.org/dist/incubator/ode/apache-ode-war-1.0-incubating.zip.sha1) |
| JBI Distribution | [apache-ode-jbi-1.0-incubating.zip](http://archive.apache.org/dist/incubator/ode/apache-ode-jbi-1.0-incubating.zip) | [pgp](https://archive.apache.org/dist/incubator/ode/apache-ode-jbi-1.0-incubating.zip.asc) | [md5](https://archive.apache.org/dist/incubator/ode/apache-ode-jbi-1.0-incubating.zip.md5) | [sha1](https://archive.apache.org/dist/incubator/ode/apache-ode-jbi-1.0-incubating.zip.sha1) |
| Source Distribution | [apache-ode-sources-1.0-incubating.zip](http://archive.apache.org/dist/incubator/ode/apache-ode-sources-1.0-incubating.zip) | [pgp](https://archive.apache.org/dist/incubator/ode/apache-ode-sources-1.0-incubating.zip.asc) | [md5](https://archive.apache.org/dist/incubator/ode/apache-ode-sources-1.0-incubating.zip.md5) | [sha1](https://archive.apache.org/dist/incubator/ode/apache-ode-sources-1.0-incubating.zip.sha1) |

All the built artifacts are available as a [Maven2 repository](http://people.apache.org/repo/m2-incubating-repository/org/apache/ode/).The project [PGP signatures](http://svn.apache.org/repos/asf/ode/trunk/KEYS) can also be checked.

<a id="getting-ode--building-from-sources"></a>

# Building from sources

To build from the sources please see our [Building ODE](#developerguide-building-ode) page.

---

<a id="userguide"></a>

<!-- source_url: https://ode.apache.org/userguide/ -->

<!-- page_index: 30 -->

<a id="userguide--getting-started"></a>

## Getting Started

First of all, getting familiar with the [WS-BPEL 2.0](#ws-bpel-20) standard is a very good idea. To use ODE, you will need to write processes using the BPEL language. There are several examples in our [distributions](#getting-ode) that you can use to get started, but a decent understanding of the spec is assumed.

Then, you can optionally check out [ODE Schema](#ode-schema) page in order to install schema for your database. Please note that schemas from distribution sometimes contain errors, because of poor quality of ORM schema generators.

ODE can be deployed in three different environments:

- As a simple Web Service in Axis 2, ODE is bundled in a WAR than can be deployed in any application server and is invoked using plain SOAP/HTTP.
- As a JBI service assembly, ODE is bundled in a ZIP that can be deployed in any JBI container and is invoked using the NMR.
- SMX4 OSGi bundle

<a id="userguide--installation"></a>

## Installation

1. [WAR Deployment](#war-deployment)
2. [Upgrading ODE](#upgrading-ode)

<a id="userguide--using-ode"></a>

## Using ODE

1. [Creating a Process](#creating-a-process)
2. [Process Versioning](#process-versioning)
3. [Management API](#management-api)
4. [Instance Replayer](#instance-replayer)
5. [ODE Execution Events](#ode-execution-events)
6. [Endpoint References](#endpoint-references)
7. [WSDL 1.1 HTTP Binding Support](#wsdl-11-http-binding-support)
8. [WSDL 1.1 Extensions for REST](#extensions-wsdl-11-extensions-for-rest)
9. [BPEL Extensions](#extensions)
10. [Instance Data Cleanup](#instance-data-cleanup)
11. [Direct Process-to-Process Communication](#direct-process-to-process-communication)
12. [Stateful Exchange Protocol](#developerguide-stateful-exchange-protocol)
13. [Activity Failure and Recovery](#extensions-activity-failure-and-recovery)
14. [XQuery Extensions](#extensions-xquery-extensions)
15. [Custom XPath functions](#custom-xpath-functions)
16. [Atomic Scopes Extension for BPEL](#developerguide-atomic-scopes-extension-for-bpel)

<a id="userguide--how-to"></a>

## How To

1. [ODE JBI and Axis2 properties overview](#ode-jbi-and-axis2-properties-overview)
2. [Controlling ODE's Memory Footprint](#controlling-odes-memory-footprint)
3. [Endpoint Configuration](#endpoint-configuration)
4. [HTTP Authentication](#http-authentication)
5. [Using a JNDI DataSource under ServiceMix JBI](#using-a-jndi-datasource-under-servicemix-jbi)
6. [Writing BPEL Test Cases](#writing-bpel-test-cases)
7. [WS-Security in ODE](#ws-security-in-ode)
8. [Use Assign to build messages](#use-assign-to-build-messages)

<a id="userguide--end-of-life"></a>

## End of Life

1. [JBI Deployment](#jbi-deployment) (EOL from ODE 1.3.7)
2. [SMX4 OSGi Deployment](#smx4-osgi-deployment) (EOL from ODE 1.3.7)

---

<a id="developerguide"></a>

<!-- source_url: https://ode.apache.org/developerguide/ -->

<!-- page_index: 31 -->

<a id="developerguide--general-documentation"></a>

## General Documentation

These documents are intended for those of you wanting an in-depth look into ODE. You'll learn a bit more about our Web Services interfaces, our internal interfaces and how the engine works.

- [Architectural Overview](#developerguide-architectural-overview)
- ODE's virtual machine: [JaCOb](https://ode.apache.org/developerguide/jacob.html)
- Notes about using [Eclipse IDE](https://ode.apache.org/developerguide/eclipse-ide.html) with Apache ODE
- [Release Guidelines](https://ode.apache.org/developerguide/release-guidelines.html)

<a id="developerguide--specifications"></a>

## Specifications

- [Stateful Exchange Protocol](#developerguide-stateful-exchange-protocol) Protocol for handling stateful interactions (aka automagic correlation).
- [Atomic Scopes Extension for BPEL](#developerguide-atomic-scopes-extension-for-bpel)

---

<a id="ws-bpel-20-specification-compliance"></a>

<!-- source_url: https://ode.apache.org/ws-bpel-20-specification-compliance.html -->

<!-- page_index: 32 -->

# WS-BPEL 2.0 Specification Compliance

This page provides information on ODE's compliance to the final [WS-BPEL 2.0](#ws-bpel-20) specification released by OASIS. ODE also implements [a few extensions](#extensions) we deemed necessary.

<a id="ws-bpel-20-specification-compliance--static-analysis"></a>

## Static Analysis

In this section the divergenced from the specification relating to static analysis requirements are described.

<a id="ws-bpel-20-specification-compliance--variables"></a>

## Variables

<a id="ws-bpel-20-specification-compliance--initialization"></a>

### Initialization

The inline `from-spec` used for variable initialization (BPEL 2.0 Section 8.1) is not supported, however a patch is available (see ODE-236).

<a id="ws-bpel-20-specification-compliance--external-variables"></a>

### External Variables

In addition to regular variables that are managed by the engine according to the BPEL specification, ODE adds support for variables whose content is stored externally yet transparently accessible from the engine. See [External Variables](#extensions-external-variables) for more information.

<a id="ws-bpel-20-specification-compliance--activities"></a>

## Activities

In this section the divergences from the specification for each standard BPEL activity are described.

<a id="ws-bpel-20-specification-compliance--receive"></a>

### <[receive](https://ode.apache.org/receive.html)>

There are several major issues with support for the `<receive>` activity.

ODE does not yet support the `<fromPart>` syntax. Therefore, the `variable` attribute must be used. Furthermore, only message variables can be referenced with the `variable` attribute, whereas the [specification](#ws-bpel-20) permits referencing of an element-typed variable if the WSDL for the request message contains a single element-typed part.

Multiple start activities as described in section 10.4, and 15.4 of the [specification](#ws-bpel-20)) are not officially supported. This precludes the use of `initiate="join"`.

ODE does not provide the ordering guarantees described in section 10.4 of the [specification](#ws-bpel-20). Also, it does not enforce the ordering requirements described in the same section. Hence, the BPEL code

```
<flow> <receive ...createInstance="yes" /> <assign .../> </flow>
```

is illegal according to the BPEL specification, but allowed by ODE.

The specification defines two standard faults --- `bpel:[conflictingRequest](conflictingrequest.html)` and `bpel:[conflictingReceive](conflictingreceive.html)` --- to deal with two similar error conditions relating to multiple outstanding requests on a single partner-link/operation/messageExchange tuple. ODE does not distinguish between these two conditions and `conflictingReceive` is thrown whenever either of the conditions occurs. That is to say, in certain cases a `conflictingReceive` indicates a `conflictingRequest`, and `conflictingRequest` is never thrown.

Finally, the `validate` attribute --- if present --- is ignored: ODE currently provides no variable validation.

<a id="ws-bpel-20-specification-compliance--_1"></a>

###

The conformance issues with the `<reply>` activity mirror those of the `<receive>` activity as described above: the `<toPart>` syntax is not supported, and `variable` attributes must reference message-typed variables.

<a id="ws-bpel-20-specification-compliance--invoke"></a>

### <[invoke](https://ode.apache.org/invoke.html)>

Again, as in the `<receive>>` and `<reply>` activities, the `<toPart>>` and `<fromPart>>` syntax are not supported. Similarly, the `inputVariable` and `outputVariable` attributes must reference message-typed variables. Here too, the `validate` attribute is ignored.

<a id="ws-bpel-20-specification-compliance--assign"></a>

### <[assign](#assign)>

The WS-BPEL 2.0 specification requires the <[assign](#assign)> activity to be atomic. Currently in ODE, each `<copy>` is atomic.

The specification also provides for validating variables at the end of an assignment using the `validate` attribute. ODE does not support this. This means that the `bpel:[invalidVariables](invalidvariables.html)` fault is never thrown by an <[assign](#assign)> activity.

Inline assignment as part of the variable declaration isn't currently supported.

ODE currently uses the `expressionLanguage` attribute to determine the language used in assignments instead of using the `queryLanguage` attribute.

There are no other known divergences from the specification relating to the `<assign>` activity that would prevent the execution of valid BPEL assignments. ODE provides certain (non-standard) extensions to the `<assign>` activity that do not conform to the specification's requirements for assignment extensions. Consult the [reference page](#assign) for the `<assign>` activity for further details regarding non-standard extensions.

<a id="ws-bpel-20-specification-compliance--_2"></a>

###

The `<throw>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_3"></a>

###

The `<exit>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_4"></a>

###

The `<wait>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_5"></a>

###

The `<empty>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_6"></a>

###

The `<sequence>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_7"></a>

###

The `<if>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_8"></a>

###

The `<while>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_9"></a>

###

The `<repeatUntil>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_10"></a>

###

The `<forEach>` activity is fully compliant with the specification. ODE supports both sequential and parallel for-each semantics.

<a id="ws-bpel-20-specification-compliance--pick"></a>

### <[pick](https://ode.apache.org/pick.html)>

The <[pick](https://ode.apache.org/pick.html)> activity has the same issues as the <[receive](https://ode.apache.org/receive.html)> activity.

<a id="ws-bpel-20-specification-compliance--_11"></a>

###

The `<flow>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_12"></a>

###

Isolated scopes are implemented in ODE's experimental branch (as of September 2007) and will be released in ODE 2.x.

ODE v1.0/1.1 do not support isolated scopes nor do they support "exit on standard fault" semantics. Hence, a BPEL 2.0 process will be interpreted as if any `isolated` and `exitOnStandardFault` attributes on `<scope>` elements did not exist.

<a id="ws-bpel-20-specification-compliance--compensate"></a>

### <[compensate](https://ode.apache.org/compensate.html)>

The `<compensate>` activity is not compliant with the specification. In ODE, this activity has the same effect and syntax as `<compensateScope>`. In addition, the `scope` attribute may be used in place of the `target` attribute with the same effect; and ODE expects one of these attributes must be specified.

<a id="ws-bpel-20-specification-compliance--_13"></a>

###

The `<compensateScope>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--_14"></a>

###

The `<rethrow>` activity is fully compliant with the specification.

<a id="ws-bpel-20-specification-compliance--validate"></a>

### <[validate](https://ode.apache.org/validate.html)>

The `<validate>` activity is *not* implemented by ODE. Processescontaining such activities will cause a compilation failure.

<a id="ws-bpel-20-specification-compliance--_15"></a>

###

Activity extension is not supported in ODE. There is an implementation in the ODE experimental branch.

---

<a id="faq"></a>

<!-- source_url: https://ode.apache.org/faq.html -->

<!-- page_index: 33 -->

<a id="faq--faq"></a>

## FAQ

This section collections frequently asked questions about ODE, BPEL, and related topics.

<a id="faq--general"></a>

## General

**Q.** *What is ODE?*
**A.** ODE is a system for executing reliable long-running process described using the WS-BPEL 2.0 standard and the BPEL4WS 1.1 vendor specification.

**Q.** *What is the architecture of ODE?*
**A.** The architecture of ODE is described in the ODE [Architectural Overview](#developerguide-architectural-overview)

**Q.** *In what language is ODE written?*
**A.** ODE is written in Java and relies on JDK v5.0 features.

**Q.** *How does ODE ensure reliable process execution?*
**A.** ODE relies on a relational database to provide persistent storage.

<a id="faq--language-related-bpel-questions"></a>

## Language-Related BPEL Questions

This section covers frequently-asked questions about ODE's support for the OASIS WS-BPEL language.

**Q.** *Which version or versions of BPEL does ODE currently support?*
**A.** ODE aims to provide full compliance to the OASIS [WS-BPEL 2.0](#ws-bpel-20) standard as well as backward compatibility for BPEL4WS 1.1 processes. At present, ODE (mostly) supports the syntax of the final [WS-BPEL 2.0](#ws-bpel-20) draft; limitations are described in the [WS-BPEL 2.0 Specification Compliance](#ws-bpel-20-specification-compliance) page.

**Q.** *Is the entire* *[WS-BPEL 2.0](#ws-bpel-20)* *specification supported?*
**A.** Most WS-BPEL 2.0 language features (and all important features) are supported. For specifics see the [WS-BPEL 2.0 Specification Compliance](#ws-bpel-20-specification-compliance) page.

**Q.** *Does ODE use native Java language constructs to execute BPEL, e.g., multiple threads for a* *`<bpel:flow>`* *or a* `while (...) {...}` *for a* `<bpel:while>`?
**A.** No. ODE's BPEL implementation does not map the BPEL process into Java. Instead, it relies on a transactional concurrency framework [JaCOb](https://ode.apache.org/developerguide/jacob.html) similar to the theoretical concurrency model known as Actors [Agha86](https://ode.apache.org/bibliography.html#agha86).

**Q.** *Does ODE support BPEL processes developed in third-party tools?*
**A.** Yes. Well-formed BPEL from any source should work.

**Q.** *Can ODE support extensions or alternatives to standard BPEL syntax and semantics?*
**A.** Yes. ODE's BPEL compiler can be customized to support non-standard BPEL syntax and semantics.

**Q.** *Does ODE support custom XPath extension functions in a BPEL process?* What are the limitations?
**A.** Yes. XPath extension functions are supported; however, to ensure correct process execution in the presence of system failures, extension functions must be side-effect free.

**Q.** *Does ODE support custom expression / query languages?*
**A.** Yes. The expression / query language is fully pluggable.

**Q.** *Does ODE support BPELJ or JSR-207?*
**A.** No.

**Q.** *Can multiple BPEL activities be grouped into a single transaction?*
**A.** No.

**Q.** *My process fails with a* `selectionFailure`; What can I do?\_
**A.** BPEL expects a *single* element to be selected when evaluating `<to>` and `<from>` expressions, and a `selectionFailure` fault is thrown if zero or more than one element are selected.

If you get zero element, double-check your namespace prefix and bindings. Also, remember that you must initialize your variables (most often with `<literal>`'s) before assigning into them, unless your are reassigning the whole variable (e.g. directly into `$variable`, or `$variable.part`). To debug assignments, you can set the "org.apache.ode" logging category to DEBUG in order to see the content of variables as the process executes.

<a id="faq--bpel-process-management"></a>

## BPEL Process Management

This section covers frequently-asked questions about the runtime management of the engine and process instances.

**Q.** *Does ODE support process versioning?*
**A.** Yes, our versioning approach is described [here](#process-versioning) in detail. The ability to modify the definition of an existing process instance may be available in future versions.

**Q.** *Does ODE provide debugging facilities?*
**A.** Yes, BPEL processes can be debugged "in-container" using the [Management API](#management-api).

**Q.** *What kind of eventing or audit information is available from ODE's BPEL engine?*
**A.** ODE includes a rich eventing API that exposes information about the start and completion time of activities and scopes, variable manipulations, and other information. Event listeners can extract as much or as little of this information as desired.

<a id="faq--runtime-environments-and-requirements"></a>

## Runtime Environments and Requirements

This section covers frequently-asked questions about the runtime requirements for ODE and supported thirdparty products.

**Q.** *Which Java virtual machines and runtime environments does ODE support?*
**A.** [Building ODE](#developerguide-building-ode) and executing ODE requires JDK 5.0.

**Q.** *Which operating systems does ODE support?*
**A.** ODE is written entirely in Java and can run on any operating system supporting the required Java environment. ODE has been tested and is known to run on Windows 2000, Windows XP, Linux, MacOS X, Solaris, and AIX.

**Q.** *Does ODE require a database? Which databases and versions does ODE support?*
**A.** ODE does not depend directly on any specific database or persistence mechanism. Instead, ODE relies on a set of data access object ("DAO") interfaces that encapsulate the behaviors of a persistence layer. The ODE distribution includes a DAO implementation for JDBC databases built using [OpenJPA](http://openjpa.apache.org). This DAO implementation can support most common relational databases. Schemas suitable for [MySQL](http://www.mysql.com) and [Derby](http://db.apache.org/derby/) are provided. Relational databases lacking transaction or binary large object ("BLOB") capabilities are not supported. The DAO interfaces can readily be implemented to support alternative persistence mechanisms (e.g. JDO), XML datastores, or direct filesystem-based persistence.

**Q.** *Does ODE require a J2EE application server?*
**A.** The core ODE components do not require a J2EE application server. ODE relies on a [Integration API](http://svn.apache.org/repos/asf/ode/trunk/bpel-api/src/main/java/org/apache/ode/bpel/iapi/) that allows ODE to be embedded in most any environment that can supply the required facilities. An [AXIS2 Integration](#developerguide-architectural-overview--odeintegrationlayers) is provided that permits ODE to be installed on a J2EE application server, or in a "dumb" Servlet container via a WAR file. A [JBI Integration](#developerguide-architectural-overview--odeintegrationlayers) integration is also provided that permits ODE to be installed in a JBI container.

**Q.** *Is there a stand-alone ODE integration?*
**A.** No, the standard ODE distributions require either an application server, Servlet container, or JBI container.

**Q.** *Can ODE be deployed within an application server or web container?*
**A.** Yes, ODE can be deployed into most common application servers. However, it is important to note that ODE is not an *enterprise application* in the J2EE sense: ODE manages its own transactions and threads.

**Q.** *Does ODE require JMS?*
**A.** No, however future versions of ODE will require a transactional transport to support clustering.

**Q.** *Is ODE internationalized? If so, which languages are supported?*
**A.** ODE messages intended for user consumption are internationalized using the Java resource bundle mechanism. American english messages are provided.

**Q.** *I'm getting data truncation errors, what does that mean?*
**A.** We try to use sensible sizes for the database columns that contain messages and variables in ODE. However if you're manipulating large quantities of data that may not e enough. The solution in that case is to alter the column that's too short to reserve enough database space for your needs.

<a id="faq--integration-with-third-party-products"></a>

## Integration with Third-Party Products

This section covers frequently asked questions related to integrating ODE into third-party products or integrating third-party products into ODE.

**Q.** *Can ODE interact directly (i.e., not over the network) with native Java services?*
**A.** This is currently supported in the [JBI Integration](#developerguide-architectural-overview--odeintegrationlayers) via standard JBI mechanisms. It is currently not supported in the [AXIS2 Integration](#developerguide-architectural-overview--odeintegrationlayers) but will be in the future.

**Q.** *Can ODE integrate with Middleware X? Can ODE integrate with Legacy system Y? Can ODE integrate with Enterprise Application Z? How is this accomplished?*
**A.** The generic answer is "Yes," although it requires some work on the part of the integrator. The primary extension point for integrating with external systems is the [Integration API](http://ode.apache.org/javadoc/org/apache/ode/bpel/pmapi/ProcessManagement.html), which can be used to embed ODE in most any environment.

**Q.** *Does ODE rely on any third-party or open source libraries?*
**A.** ODE uses a number of liberally-licensed (i.e., non-GPL) open source libraries, some integral and some not. These are enumerated in the [reference](#required-third-party-libraries).

<a id="faq--ode-and-web-services"></a>

## ODE and Web Services

This section covers frequently asked questions about how ODE related to various web services specifications and initiatives.

**Q.** *Does ODE supply a SOAP stack?*
**A.** Not directly. ODE relies on the [Integration Layer](#developerguide-architectural-overview--odeintegrationlayers) to supply the "physical" communication mechanisms. The [AXIS2 Integration Layer](#developerguide-architectural-overview--odeintegrationlayers) that is part of the ODE distribution uses the AXIS2 SOAP stack. The [JBI Integration Layer](#developerguide-architectural-overview--odeintegrationlayers) relies on external HTTP/SOAP components (e.g. ServiceMix's `servicemix-http` component).

**Q.** *Can ODE be integrated with third-party web services products such as Apache AXIS, Systinet WASP, or JAXRPC?*
**A.** Yes, ODE can be integrated into most any stack via the [Integration API](http://incubator.apache.org/ode/javadoc/bpel-api/index.html)

**Q.** *Does ODE support web services transaction specifications, e.g., WS-Transaction, WS-Coordination, WS-Business Activity, OASIS BTP, or Composite Application Framework (WS-CAF)?*
**A.** No, not at present.

**Q.** *Does ODE support WS-Addressing?*
**A.** ODE does not directly support WS-Addressing. However, the BPEL implementation and the core ODE infrastructure provides support for opaque end-point references. This allows ODE to be integrated with arbitrary addressing standards. The [AXIS2 Integration Layer](#developerguide-architectural-overview--odeintegrationlayers) for ODE employs this mechanism to support WS-Addressing.

<a id="faq--reliability"></a>

## Reliability

This section covers frequently asked questions about the reliability of ODE.

**Q.** *Can ODE recover in the event of system failure?*
**A.** Yes, ODE uses transaction management and relies on transactional data stores to ensure data consistency in the event of failure.

**Q.** *How does ODE's BPEL Engine recover in the event of system failure?*
**A.** todo: describe recovery mechanism

**Q.** *What happens to outbound invocations bound to transaction protocols (such as SOAP-over-JMS) in the event of system failure?*
**A.** todo: describe

**Q.** *What happens to outbound invocations bound to non-transactional protocols (such as HTTP) in the event of system failure?*
**A.** todo: describe

<a id="faq--clustering"></a>

## Clustering

This section covers frequently asked questions about ODE's clustering support.

**Q.** *Can ODE be deployed in clustered or other configurations intended to provide fault tolerance and increased performance?*
**A.** Clustering support is currently under development. Clustering support will require a transaction inter-node transport (such as JMS) as well as a transactional data store that can be accessed concurrently by all nodes in the cluster (i.e. a modern RDBMS).

---

<a id="roadmap"></a>

<!-- source_url: https://ode.apache.org/roadmap.html -->

<!-- page_index: 34 -->

<a id="roadmap--roadmap"></a>

## Roadmap

<a id="roadmap--development"></a>

#### Development

- BPEL 2.0 Compliance
   **Support  and** Invoking with variables that are not messages
  \*\* Isolated Scopes (done as of September 2007; will be ODE 1.2/2.0)
- Implement all management queries with OpenJPA
- Replace Quartz scheduler with something better performance-wise (done as of June 2007; released in ODE 1.1)
- Expose management APIs in a RESTful manner (I think Axis2 supports this?)
- Implement a Service Component Architecture (SCA) integration layer (in progress; basic integration released with Tuscany 1.0)
- Add more BPEL 2.0 test cases (this is work in progress; we add test cases as bugs are reported by the community)
- Provide a management console

<a id="roadmap--documentation"></a>

#### Documentation

- More examples!

---

<a id="resource-services"></a>

<!-- source_url: https://ode.apache.org/resource-services.html -->

<!-- page_index: 35 -->

<a id="resource-services--tutorials"></a>

## Tutorials

- [Developing, Deploying and Running a Hello World BPEL Process with the Eclipse BPEL Designer and Apache ODE](http://people.apache.org/~vanto/HelloWorld-BPELDesignerAndODE.pdf): A click-by-click Instruction
- [BPEL mit Apache ODE und dem Eclipse BPEL-Designer unter Eclipse 3.4 (Ganymede) entwickeln](http://www.se.uni-hannover.de/lehre/tutorials/BPEL-ODE-Eclipse-Getting-Started.php) (german)
- [Installation von Apache ODE in Eclipse 3.4 (Ganymede)](http://www.se.uni-hannover.de/lehre/tutorials/BPEL-ODE-Eclipse.php) (german)
- [Hello-World-BPEL-Prozess mit Apache ODE in Eclipse 3.4 (Ganymede)](http://www.se.uni-hannover.de/lehre/tutorials/BPEL-ODE-HelloBPEL.php) (german)
- [BPEL-Prozess mit einfachem Invoke auf Apache ODE in Eclipse 3.4 (Ganymede)](http://www.se.uni-hannover.de/lehre/tutorials/BPEL-ODE-SimpleInvoke.php) (german)
- [ODE/BPELUnit Tutorial: Unit Testing BPEL processes with Test Coverage - Part I](http://static.se.uni-hannover.de/lehre/tutorials/BPELUnit-Coverage1.php)
- [ODE/BPELUnit Tutorial: Unit Testing BPEL processes with Test Coverage - Part II](http://static.se.uni-hannover.de/lehre/tutorials/BPELUnit-Coverage2.php)
- [How to setup Apache ODE with Tomcat 7 and Bitronix](http://sathwikbp.blogspot.de/2013/09/apache-ode-on-tomcat-7-with-bitronix.html)

<a id="resource-services--projects-using-ode"></a>

## Projects using ODE

- [Apache ServiceMix](http://servicemix.apache.org/home.html): Agile open-source ESB (JBI Container)
- [Apache Tuscany](http://tuscany.apache.org): SCA based component aggregation framework.
- [Intalio BPMS](http://bpms.intalio.com/): a full open source BPMS solution including a [BPMN designer](http://www.intalio.com/products/designer/), runtime components and tooling.
- [SUPER](http://ip-super.org/): Integrated EU research project, aiming to raise BPM to the business level, where it belongs, from the IT level where it mostly resides now.
- [GASwerk](http://gaswerk.sourceforge.net/): pre-packaged SOA, JMS and Spring stacks based on the Geronimo application server.
- [JBoss RiftSaw](http://www.jboss.org/riftsaw): Apache ODE optimized for the JBoss Application Server container.
- [WSO2 Business Process Server](http://wso2.com/products/business-process-server/)

<a id="resource-services--useful-tools"></a>

## Useful Tools

- [Apache Axis2](http://ws.apache.org/axis2/): Web service stack
- [SoapUI](http://www.soapui.org): Free and open source desktop application for inspecting, invoking, developing, simulating/mocking and functional/load/compliance testing of web services.
- [Eclipse BPEL designer](http://www.eclipse.org/bpel/).
- [ObjectWeb Lomboz(TM)](http://lomboz.objectweb.org) is built on top of the Eclipse BPEL designer and offers additional options like an embedded server and easy deployment (see http://lomboz.objectweb.org/bpel\_demo.html for a demo)
- [Apache ODE Tomcat Bundle](https://github.com/vanto/apache-ode-tomcat-bundle): Build script that creates a fully configured bundle with Tomcat 7, Apache ODE, Hibernate and Bitronix.

<a id="resource-services--articles"></a>

## Articles

- [SOA auf die leichte Art (german)](http://javamagazin.de/itr/online_artikel/psecom,id,915,nodeid,11.html)
- [An Introduction to Apache ODE](http://www.infoq.com/articles/paul-brown-ode)
- [Develop and execute WS-BPEL V2.0 business processes using the Eclipse BPEL plug-in](http://www.ibm.com/developerworks/opensource/library/os-eclipse-bpel2.0/)
- [Execute business processes with Eclipse and Apache ODE](http://www.ibm.com/developerworks/edu/os-dw-os-eclipse-stpatlode.html)
- Open Source BPEL Orchestra (german) - [Part 1](http://taval.de/JM_1.2010_Moser_vanLessen_Luebke_BPEL1.pdf), [Part 2](http://taval.de/JM_2.2010_Luebke_Moser_van_Lessen_BPEL2.pdf), [Part 3](http://taval.de/JM_3.2010_van_Lessen_Luebke_Moser_BPEL3.pdf)

<a id="resource-services--important-specifications"></a>

## Important specifications

- [BPEL4WS 1.1](ftp://www6.software.ibm.com/software/developer/library/ws-bpel.pdf) (pdf) and [WS-BPEL 2.0](http://docs.oasis-open.org/wsbpel/2.0/wsbpel-v2.0.html)specifications.
- [WSDL 1.1](http://www.w3.org/TR/wsdl)
- [XPath 1.0](http://web5.w3.org/TR/xpath) and [XPath 2.0](http://www.w3.org/TR/xpath20/)
- [ECMAScript for XML (E4X) Specification](http://www.ecma-international.org/publications/standards/Ecma-357.htm) (can be used in BPEL extensions)

<a id="resource-services--professional-services"></a>

## Professional Services

Here is a list of companies providing professional services around Apache ODE. This includes consulting, support, training, products (sorted in alphabetical order):

- [TouK](http://touk.pl), Warsaw, Poland -- Consulting, Apache ServiceMix Integration

---

<a id="mailing-lists"></a>

<!-- source_url: https://ode.apache.org/mailing-lists.html -->

<!-- page_index: 36 -->

# Mailing Lists

The following mailing-lists are open to anybody:

| Mailing-List | Address | Subscribe |
| --- | --- | --- |
| User | user@ode.apache.org | user-subscribe@ode.apache.org |
| Development | dev@ode.apache.org | dev-subscribe@ode.apache.org |
| Commits | commits@ode.apache.org | commits-subscribe@ode.apache.org |

The archives are available below:

- <http://mail-archives.apache.org/mod_mbox/ode-user/>
- <http://mail-archives.apache.org/mod_mbox/ode-dev/>
- <http://mail-archives.apache.org/mod_mbox/ode-commits/>

For search and more advanced archives browsing, [MarkMail](http://ode.markmail.org) indexes our mailing-lists.

---

<a id="developerguide-building-ode"></a>

<!-- source_url: https://ode.apache.org/developerguide/building-ode.html -->

<!-- page_index: 37 -->

<a id="developerguide-building-ode--overview"></a>

# Overview

Building from the source is usually for the thick skinned, we try to keep our trunk stable but it's a development environment so we can never guarantee that everything will be smooth. If you rather work with something more stable or if you don't need the latest and greatest, using the [latest official distribution](#getting-ode) is probably a better option.

<a id="developerguide-building-ode--getting-the-source-code"></a>

## Getting the source code

<a id="developerguide-building-ode--with-git"></a>

### with Git

The Subversion repository is mirrored by a Git repository at <http://git.apache.org/ode.git> or [Github](http://github.com/apache/ode).
So if you're more comfortable with Git, you can clone this repo.

```
$> git clone http://git.apache.org/ode.git
$> cd ode
$> git checkout -b 1.X --track origin/trunk
```

<a id="developerguide-building-ode--building-with-buildr"></a>

## Building With Buildr

ODE uses [Apache Buildr](http://buildr.apache.org). Buildr has a very detailed [installation guide](http://buildr.apache.org/installing.html), so refer to it to get Buildr working on your machine.
The latest known working configuration for trunk (both for windows, linux, macos with JDK 1.5 and JDK 1.6) is buildr 1.4.4, jruby 1.5.1 (ruby 1.8.7 patchlevel 174).

Building is then pretty simple.

> [!NOTE]
> <a id="developerguide-building-ode--version-information"></a>

>
> > [!NOTE]
> > #### Version Information
>
> The trunk must be build with Buildr **1.4.4** or higher

Open a command in the source root directory and run:

```
$> buildr package test=no
```

To try the test cases bundled with ODE:

```
$> buildr test
```

You are very welcome to contribute by running test cases and posting spotted errors into [mailing list](http://ode.apache.org/mailing-lists.html).

To generate Eclipse project files:

```
$> buildr eclipse
```

> [!NOTE]
> You may use "buildr \_1.4.4\_ test" - like syntax to use specific buildr version.

It just works! For more information about Buildr see http://buildr.apache.org/.

<a id="developerguide-building-ode--troubleshooting"></a>

## Troubleshooting

- If you get a Zlib:BufError, that's because of your version of Rubygems, just upgrade RubyGems by typing:
  `gem update --system`

---

<a id="developerguide-source-code"></a>

<!-- source_url: https://ode.apache.org/developerguide/source-code.html -->

<!-- page_index: 38 -->

<a id="developerguide-source-code--overview"></a>

# Overview

ODE uses [Git](http://git-scm.com/) to manage its source code. Instructions on Git use can be found [here](http://git-scm.com/documentation).

<a id="developerguide-source-code--main-repository"></a>

## Main repository

<a id="developerguide-source-code--web-access-via-github"></a>

### Web Access (via Github)

1.3.x branch (Stable)
:   <https://github.com/apache/ode/tree/ode-1.3.6.x>

Trunk (Development)
:   <https://github.com/apache/ode/>

<a id="developerguide-source-code--anonymous-access"></a>

### Anonymous access

ODE source can be checked out anonymously with this command:

```
$> git clone git://git.apache.org/ode.git
```

Once you have ODE checked out you can update the source by executing the following command from within the *ode* directory.

```
$> git pull
```

Once you've got the code you'll probably want to build it; for instructions see [Building ODE](#developerguide-building-ode).

<a id="developerguide-source-code--submitting-a-patch"></a>

### Submitting a Patch

If you make changes to ODE, and would like to contribute the to the project, you should create a patch and post it to the [ODE JIRA issue tracker](http://issues.apache.org/jira/browse/ODE). To create a patch, simply execute one of the following commands:

```
$> git format-patch master --stdout > your-changes.patch

:::text
$> git diff > your-changes.patch
```

<a id="developerguide-source-code--developer-access"></a>

## Developer Access

Everyone can access the ODE Git repository via HTTP, but ODE Committers must checkout the repository via HTTPS.

```
$> git clone https://git-wip-us.apache.org/repos/asf/ode.git
```

For further instructions, please see [here](https://git-wip-us.apache.org/)

---

<a id="contributors"></a>

<!-- source_url: https://ode.apache.org/contributors.html -->

<!-- page_index: 39 -->

<a id="contributors--committers"></a>

## Committers

Here is the list of people who are actively working and committing on ODE.

| Name | ID | Organization | Role |
| --- | --- | --- | --- |
| Assaf Arkin | arkin | — | Developer & PMC |
| Alex Boisvert | boisvert | — | Developer & PMC |
| Alexis Midon | midon | — | Developer & PMC |
| [Tammo van Lessen](http://www.taval.de) | vanto | — | Developer & PMC |
| Guillaume Nodet | gnodet | [Iona](http://www.iona.com) | Developer & PMC |
| Milinda Pathirage | milinda | — | Developer & PMC |
| [Matthieu Riou](http://offthelip.org/) | mriou | — | Developer & PMC |
| [Rafał Rusin](http://rrusin.blogspot.com) | rr | [TouK](http://www.touk.pl) | Developer & PMC |
| Sathwik B P | sathwik | — | Developer & PMC Chair |
| Maciej Szefler | mszefler | — | Developer & PMC |
| Lance Waterman | lwaterman | [Sybase](http://www.sybase.com) | Developer & PMC |
| [Jeff Yu](http://jeff.familyyu.net) | jeffyu | [JBoss](http://www.jboss.com) | Developer & PMC |
| Hadrian Zbarcea | hadrian | — | Developer & PMC |
<a id="contributors--sponsors"></a>

## Sponsors

[YourKit](http://www.yourkit.com/) has graciously provided YourKit Java Profiler licenses to support our performance and quality efforts. We've had a wonderful experience using their tool – we were able to quickly and accurately find the cause of some issues in ODE -- and definitely recommend using it while building your own software.

---

<a id="ode-schema"></a>

<!-- source_url: https://ode.apache.org/ode-schema.html -->

<!-- page_index: 40 -->

# Apache ODE – ODE Schema

***Database scripts for fresh installation of ODE 1.3.7 is now packaged within the distribution archive.***

<a id="ode-schema--ode-136-137"></a>
<a id="ode-schema--ode-1.3.6-1.3.7"></a>

## ODE 1.3.6 - 1.3.7

Migration is necessary from 1.3.6, read the migration script available [here](https://github.com/apache/ode/blob/APACHE_ODE_1.3.7/schema-updates/migrate-ode-1.3.6-to-1.3.7.sql).

<a id="ode-schema--ode-134-136"></a>
<a id="ode-schema--ode-1.3.4-1.3.6"></a>

## ODE 1.3.4 - 1.3.6

ODE 1.3.4, 1.3.5 and 1.3.6 share the same schema definitions.

<a id="ode-schema--for-use-with-openjpa"></a>

### For use with OpenJPA

- [ode-1.3.4-jpa-mysql.sql](https://ode.apache.org/sql/ode-1.3.4-jpa-mysql.sql) (for MySQL < 5.5)
- [ode-1.3.4-jpa-mysql55.sql](https://ode.apache.org/sql/ode-1.3.4-jpa-mysql55.sql) (for MySQL >= 5.5)
- [ode-1.3.4-jpa-postgres.sql](https://ode.apache.org/sql/ode-1.3.4-jpa-postgres.sql)
- [ode-1.3.4-jpa-oracle.sql](https://ode.apache.org/sql/ode-1.3.4-jpa-oracle.sql)
- [ode-1.3.4-jpa-h2.sql](https://ode.apache.org/sql/ode-1.3.4-jpa-h2.sql)

<a id="ode-schema--for-use-with-hibernate"></a>

### For use with Hibernate

- [ode-1.3.4-hib-mysql.sql](https://ode.apache.org/sql/ode-1.3.4-hib-mysql.sql) (for MySQL < 5.5)
- [ode-1.3.4-hib-mysql55.sql](https://ode.apache.org/sql/ode-1.3.4-hib-mysql55.sql) (for MySQL >= 5.5)
- [ode-1.3.4-hib-pgsql.sql](https://ode.apache.org/sql/ode-1.3.4-hib-pgsql.sql)
- [ode-1.3.4-hib-oracle.sql](https://ode.apache.org/sql/ode-1.3.4-hib-oracle.sql)
- [ode-1.3.4-hib-h2.sql](https://ode.apache.org/sql/ode-1.3.4-hib-h2.sql)

<a id="ode-schema--configuring-hibernate"></a>

## Configuring Hibernate

In order to run ODE 1.3.6 under Hibernate, you need to grab external
dependencies (and accept Hibernate license). [This script](https://github.com/vanto/apache-ode-tomcat-bundle)
can be used to create a fully configured bundle with Apache Tomcat, Hibernate, and Bitronix.

<a id="ode-schema--configuring-h2-database"></a>

## Configuring H2 Database

Run this:

```
java -cp h2-1.1.117.jar org.h2.tools.RunScript -url 'jdbc:h2:file:ode-db;DB_CLOSE_ON_EXIT=false;user=sa' -showResults -script ode-1.3.4-hib-h2.sql
```

Then you will get ode-db\* files in directory.

Then edit ode-axis2.properties and set:

```
ode-axis2.dao.factory=org.apache.ode.daohib.bpel.BpelDAOConnectionFactoryImpl
ode-axis2.db.mode=INTERNAL
ode-axis2.db.int.jdbcurl=jdbc:h2:file:ode-db;DB_CLOSE_ON_EXIT=false;user=sa
ode-axis2.db.int.driver=org.h2.Driver
hibernate.dialect=org.hibernate.dialect.H2Dialect
```

<a id="ode-schema--upgrade-from-previous-versions"></a>

## Upgrade from previous versions

Please refer to this page: [Upgrading ODE](#upgrading-ode)

---

<a id="assign"></a>

<!-- source_url: https://ode.apache.org/assign.html -->

<!-- page_index: 41 -->

# assign

---

<a id="bpel-management-api-specification"></a>

<!-- source_url: https://ode.apache.org/bpel-management-api-specification.html -->

<!-- page_index: 42 -->

<a id="bpel-management-api-specification--bpel-management-api-specification"></a>

# BPEL Management API Specification

The BPEL Management API exposes management functions related to BPEL processes and their instances.

<a id="bpel-management-api-specification--general-design-principles"></a>

## General Design Principles

The Process Management API is defined as a Web service interface. In doing so we can offer SOAP access to the service, and also create Java interfaces for SOAP access and JMX, depending on needs. All messages are defined as XML elements, mapping to WSDL doc/literal.

Complex structures and other data fields are declared as XML elements. However, key fields are declared as XML attributes. This distinction maps to the concept of keys in several languages, e.g. constraints can be applied in XML Schema using key fields, or used as keys in a Java HashMap. Sequences of elements map to ordered collections, which may be accessed by position or key. For example, when returning a list of process instances, the collections is ordered as specified in the request, but in addition the process identifier can be used as a key into the collection.

When data does not easily yield to structuring, we use a textual presentation and BNF to define the syntax. For example, a query statement like "order\_id`123 and customer_id`456" is easier to process in textual form.

<a id="bpel-management-api-specification--the-process-definition-management-interface"></a>

## The Process Definition Management Interface

The process definition management interface defines six operations:
 **list* - Returns information about all, or some process definitions.* *details* - Returns detailed information about the specified process definition.
 **set-properties* - Changes properties associated with the process definition.* *activate* - Activates the process definition.
\* *retire* - Retires the process definition.

<a id="bpel-management-api-specification--list-process-definitions"></a>

### List Process Definitions

The *list* operation retrieves and returns information about all, or some process definitions.

The request identifies the process definitions using a filter that can select definitions with a given name, status, deployment date, etc. Without a filter, the operation returns all process definitions. The request also indicates what information to include in the response, and which key fields to use for ordering the results. The request schema has the following structure:

```
<list>
  <filter> filter <filter>?
  <include> includes </include>?
  <order> keys </order>?
</list>
```

The *filter* element can be used to narrow down the list of process definitions by applying selection criteria. There are four filters that can be applied:
 **name* - Only process definition with this local name.* *namespace* - Only process definition with this namespace URI.
 **status* - Only process definition with these status code(s).* *deployed* - Only process definitions deployed relative to this date/time.

The *name* and *namespace* filters can do full or partial name matching. Partial matching occurs if either filter ends with an asterisk (*). These filters are not case sensitive, for example\** *name`my_* will match _MyProcess_ and _my-process_. If unspecified, the default filter is _name`\* namespace=\**.

The *status* filter can be used to filter all process definitions based on two status codes, *activated* and *retired*.

The *deployed* filter can be used to filter all process definitions deployed on or after a particular date or date/time instant. The value of this filter is either an ISO-8601 date or ISO-8601 date/time. For example, to find all process definitions deployed on or after September 1, 2005, use *deployed>=20050901*.

The *include* element can be used to request the operation returns additional information in the response, by specifying a space-separated list of keywords. Currently two keywords are supported:
 **properties* - Returns process definition properties.* *instance* - Returns aggregate instance information.

By default the response returns process definitions in no particular order. The *order* element can be used to order the results by specifying a space-separated list of keys. Each key can be prefixed with a plus sign '+' to specify ascending order, or a '-' minus sign to specify descending order. Without a sign the default behavior is to return process definitions in ascending order. The currently supported odering keys are:
 **name* - Order based on the local name of the process definition.* *namespace* - Order based on the namespace URI of the process definition.
 **version* - Order based on the version number.* *status* - Order based on the status of the process definition (*activated* followed by *retired*).
\* *deployed* - Order based on the deployment date/time.

For exampe, the following request returns all process definitions that have a name starting with *order* and are currently in the activated status. The response is ordered by the definition name, definitions with the same name are ordered by descending version number. Aggergate instance information is returned for each process definition that matches the filter.

```
<list>
  <filter>name=order* status=activated</filter>
  <include>instance</include>
  <order>name -version</order>
</list>
```

The response to the *list* operation lists all process definitions that match the filters, empty if no process definition matches the filter. The response schema has the following structure:

```
<list.response>
  <definition name = ncname
              namespace = uri
              version = integer>
    <deployed>
    <activated> | <retired>
         <properties>?
         <instances>?
  </definition>*
</list.response>
```

Each process definition is identified by its fully qualified name (*name* and *namespace* attributes) and version number. If there are multiple versions of the same process definition, the operation will return information about all of the versions that match the filter.

The *deployed* element specifies when the process definition was deployed and by which user. It has the following structure:

```
<deployed>
  <on> date/time </on>
  <by> token </by>
</deployed>
```

If the process definition is activated, the *activated* element specifies when it was activated and by which user. If the process was activated upon deployment, then the information provided by the *deployed* and *activated* elements will be identical. If the process definition is retired, the *retired* element specifies which it was retired and by which user. All three elements use the same structure.

If the operation requested process properties, the *properties* element will appear in the response. It has the following structure:

```
<properties>
  <property name = ncname
                             namespace = uri>
  <value> mixed </value>
  </property>*
</properties>
```

Each property is identified by it's fully qualified name (the `name` and `namespace` attributes). The `value` element serves as a wrapper for the property value, which may include mixed content and use elements for different namespaces.

If the operation requested instance aggregates, the *instances* element will appear in the response. It has the following structure:

```
<instances>
  <instance status = token>
  <count> integer </count>
  </instance>*
</instances>
```

The *instance* element returns the number of process instances that have the status specified by the *status* attribute. The following status codes are used:
 **active* - All currently active process instances.* *completed* - All successfully completed process instances.
 **terminated* - All terminated process instances.* *failed* - All failed process instances.
 **suspended* - All process instances that are currently suspended.* *error* - All process instances currently reporting an error.

During it's execution, a process instance is in the *active* state. It may be suspended, in which case it is counted as *suspended* and not *active*. If an error occurs that does not cause the process to complete, but requires attention, the process is counted in *error* instead of *active*. If a process is terminated with the *exit* activity, or any other mechanism that applies the same semantics, it counts as *terminated*. If a fault occurs in the global scope, the process counts as *failed*. Otherwise, the process is counted as *completed*.

<a id="bpel-management-api-specification--get-process-definition-details"></a>

### Get Process Definition Details

The *details* operation retrieves and returns detailed information about the specified process definition.

The request identifies the process definition by its fully qualified name, and optionally by version number. If the version number is ommitted, information is returned about the last version of the process definition. The request schema has the following structure:

```
<details>
<definition
name =
ncname
namespace =
uri
version?
=
integer
> </definition> </details>
```

The response uses a structure similar to the *list* operation, with additional information not returned from *list*. The response includes the requested process definition, and will be empty if that process definition cannot be found in the system. The response schema has the following structure:

```
<details.response>
  <definition name = ncname
              namespace = uri
              version = integer>
    <deployed>
    <activated> | <retired>
         <properties>
  <instances>
   <documents>
   <extension elements>*
  </definition>?
</details.response>
```

The response always returns information about instances of the process definition. The response also returns a list of documents associated with the process definition, for example, the BPEL process definition, WSDL service definitions, deployment descriptor, etc. Applications may need to retrieve these documents for further processing, e.g. to monitor service endpoints defined in the process, or interpret data from the process instance.

The *documents* element has the following structure:

```
<documents>
  <document name = ncname?
            namespace = uri?
            type = uri
            src = uri>
  </document>*
</documents>
```

The *name* and *namespace* attributes reference the document name and namespace of definitions in that document, respectively. For example, if the document is a BPEL process definition, the *name* attribute specifies the process definition, and the *namespace* attribute specifies the target namespace of the process definition. These attributes are optional, as not all documents specify that information.

An implementation must return a *name* and *namespace* attribute for every BPEL, WSDL and XSD documents that specify a name and/or namespace for their target definitions.

The *type* attribute uses a URI to identify the document type. For BPEL, WSDL and XSD, this attribute uses the namespace URI of the relevant specification, e.g. (TODO: WSDL 1.1 namespace) for a WSDL 1.1 document.

The *src* attribute provides a URL that can be used to access the definition.

The *details* response may return additional information not covered here using extension elements. Extension elements must use a different namespace. Applications do not need to understand or process extension elements.

<a id="bpel-management-api-specification--set-process-definition-properties"></a>

### Set Process Definition Properties

The *set-properties* allows changes to properties associated with the process definition.

The request identifies the process definition by its fully qualified name and version number, and specifies the updates to perform on that process definition. The request schema has the following structure:

```
<set-properties>
  <definition name = ncname
              namespace = uri
             version = integer>
      <properties>
         <property name = ncname
                   namespace = uri>
             <value> mixed </value>?
         </property>*
   </properties>
  </definition>
</set-properties>
```

A property can be changed or added by specifying the property by name and providing a value. A property is removed if the property name is specified but the *value* element is absent.

The response uses a structure similar to the *details* operation, returning the state of the process definition after the state change. If the process could not be found, an empty response is returned. The response schema has the following structure:

```
<set-properties.response>
  <definition name = ncname
              namespace = uri
              version = integer>
    <deployed>
    <activated> | <retired>
    <properties>
    <instances>
    <documents>
    <extension elements>*
  </definition>?
</set-properties.response>
```

<a id="bpel-management-api-specification--activateretire-process-definition"></a>
<a id="bpel-management-api-specification--activate-retire-process-definition"></a>

### Activate/Retire Process Definition

The *activate* and *retire* operations are used to change the process definition status to activated and retired.

The request identifies the process definition by its fully qualified name and version number, and specifies the updates to perform on that process definition. The request schema has the following structure:

```
<activate>
<definition
name =
ncname
namespace =
uri
version =
integer
> </activate> <retire> <definition name =ncname namespace =uri version =integer > </retire>
```

The response uses a structure similar to the *details* operation, returning the state of the process definition after the state change. If the process could not be found, an empty response is returned.

<a id="bpel-management-api-specification--faults"></a>

### Faults

The operations in this interface may throw onw of two faults:
 **invalid-request* - The request message is missing mandatory information, contains invalid information, or contains elements/attributes that are not supported by the operation.* *processing-error* - The operation failed to process the request. The application may try the operation at a later time.

By design the operations return *invalid-request* only if the request message is invalid. If the request does not identify any deployed process definition, the operation returns a response that contains no process definition.

<a id="bpel-management-api-specification--the-process-instance-management-interface"></a>

## The Process Instance Management Interface

The process instance management interface defines four operations:
 **list* - Returns information about all, or some process instances.* *detail* - Returns detailed information about the specified process instance.
 **suspend* - Suspends the process instance.* *resume* - Resumes the process instance.
 **terminate* - Terminates the process instance.* *fault* - Faults the process instance.
\* *delete* - Deletes all or some completed process instances.

<a id="bpel-management-api-specification--list-process-instances"></a>

### List Process Instances

The *list* operation retrieves and returns information about all, or some process instances.

The request identifies the process instances using a filter that can select instances with a given name, status, property values, etc. Without a filter, the operation returns all process instances up to a specified limit. The request also indicates which key fields to use for ordering the results. The request schema has the following structure:

```
<list>
  <filter> filter <filter>?
  <order> keys </order>?
  <limit> integer </limit>
  <properties> names </properties>
</list>
```

The *filter* element can be used to narrow down the list of process definitions by applying selection criteria. There are six filters that can be applied:
 **name* - Only process instances with this local name.* *namespace* - Only process instances with this namespace URI.
 **status* - Only process instances with these status code(s).* *started* - Only process instances started relative to this date/time.
 **last-active* - Only process instances last active relative to this date/time.* *$property* - Only process instances with a correlation property equal to the specified value.

The *name* and *namespace* filters can do full or partial name matching. Partial matching occurs if either filter ends with an asterisk (*). These filters are not case sensitive, for example\** *name`my_* will match _MyProcess_ and _my-process_. If unspecified, the default filter is _name`\* namespace=\**.

The *status* filter can be used to filter all process definitions based on six status codes:
 **active* - All currently active process instances (excludes instances in any other state).* *suspended* - All process instances that have not completed, but are currently suspended.
 **error* - All process instances that have not completed, but are currently indicate an error condition.* *completed* - All successfully completed process instances (excludes instances in any other state).
 **terminated* - All process instances that were terminated.* *faulted* - All process instances that encountered a fault (in the global scope).

The *started* filter can be used to filter all process instances started on or after a particular date or date/time instant. The value of this filter is either an ISO-8601 date or ISO-8601 date/time. For example, to find all process instances started on or after September 1, 2005, use *started>=20050901*. Similarly, the *last-active* filter can be used to filter all process instances based on their last active time. The last active time records when the process last completed performing work, and either completed or is now waiting to receive a message, a timeout or some other event.

Each process instance has one or more properties that are set its instantiation, that can be used to distinguish it from other process instances. In this version of the specification, we only support properties instantiated as part of correlation sets defined in the global scope of the process. For example, if a process instantiates a correlation set that uses the property *order-id*, it is possible to filter that process instance based on the value of that property.

The property name is identified by the prefix *$*. If the property name is an *NCName*, the filter will match all properties with that local name. If the property name is
{namespace}\ *local*, the filter will match all properties with the specified namespace URI and local name. For example, to retrieve a list of all active process instances with a property *order-id* that has the value 456, use *status`active $order-id`456*.

By default the response returns process instances in no particular order. The *order* element can be used to order the results by specifying a space-separated list of keys. Each key can be prefixed with a plus sign '+' to specify ascending order, or a '-' minus sign to specify descending order. Without a sign the default behavior is to return process instances in ascending order. The currently supported odering keys are:
 **pid* - Order based on the process identifier.* *name* - Order based on the local name of the process instance.
 **namespace* - Order based on the namespace URI of the process instance.* *version* - Order based on the version number.
 **status* - Order based on the status of the process instance.* *started* - Order based on the process instance start date/time.
\* *last-active* - Order based on the process instance last active date/time.

The *properties* element is used to request the value of one or more properties, for each of the returned process instances. The value of this element is a list of names, each an *NCName*. Properties specified in this element do not have to overlap with properties specified in the filter.

*TBD:* describe limit.

The response to the *list* operation lists all process instances that match the filters, empty if no process instance matches the filter. The response schema has the following structure:

```
<list.response>
  <instance pid = string>
    <defintion name = ncname
               namespace = uri
               version = integer>
    </definition>
    <started> date/time </started>
    <last-active> date/time </last-active>
    <status>  status </status>
    <error-ts> date/time </error-ts>?
    <properties>
      <property name = ncname
                namespace = uri>
        value
      </property>*
    </properties>
    <fault>
      TBD
    </fault>?
  </instance>*
</list.response>
```

Each process is identified by the unique process instance identifier (*pid*). In addition, the process's definition is identified by its fully qualified name and version number.

The *started* element indicates when the process instance was started, while *last-active* indicates when the process instance was last active. If the process instance has completed (successfully or not), this element provides the actual completion date/time. The status code indicates whether the process is active, completed successfully, or any of the six states described for the filter.

The *properties* element lists one or more properties and their values. The name of the property is specified using the *name* and *namespace* attributes, the value is contained within the *property* element. Note that an instance may have multiple different values for the same property, in which case the *property* element will appear multiple times with the same name and different values.

*TBD:* error-ts and fault elements.

<a id="bpel-management-api-specification--get-process-instance-details"></a>

### Get Process Instance Details

The *details* operation retrieves and returns detailed information about the specified process instance.

The request identifies the process instance using the process identifier. The request schema has the following structure:

```
<details>
<instance
pid =
token
> </instance> </details>
```

The response uses a structure similar to the *list* operation, with additional information not returned from *list*. The response includes the requested process instance, and will be empty if that process instance cannot be found in the system. The response schema has the following structure:

```
<details.response>
  <instance pid = string>
     <defintion name = ncname
                namespace = uri
                version = integer>
     </definition>
      <started> date/time </started>
      <last-active> date/time </last-active>
      <status> status </status>
      <error-ts> date/time </error-ts>?
      <properties>
         <property name = ncname
                   namespace = uri>
           value
         </property>*
      </properties>
      <fault>
        TBD
      </fault>?
    <extension elements>*
  </instance>?
</details.response>
```

*TBD:* Structure for returning state information about the process instance.

The *details* response may return additional information not covered here using extension elements. Extension elements must use a different namespace. Applications do not need to understand or process extension elements.

<a id="bpel-management-api-specification--suspendresumseterminatefault-process-instance"></a>
<a id="bpel-management-api-specification--suspend-resumse-terminate-fault-process-instance"></a>

### Suspend/Resumse/Terminate/Fault Process Instance

These operations are used to suspend/resume the process instance, or to forcefully complete the process instance, with and without recovery.

The request identifies the process instance using the process identifier. The request schema has the following structure:

```
<suspend>
  <instance pid = token/>+
</suspend>

<resume>
  <instance pid = token/>+
</resume>

<terminate>
  <instance pid = token/>+
</terminate>

<fault>
  <instance pid = token>
  </instance>
    TBD: fault information
</fault>
```

The *suspend* operation changes the process state from active to suspended. It only affects process instances that are in the active or error states. Likewise, the *resume* operation changes the process state from suspended to active. It only affects process instances that are in the suspended state.

The *terminate* operation causes the process instance to terminate immediately, without a chance to perform any fault handling or compensation. The process transitions to the *terminated* state. It only affects process instances that are in the active, suspended or error states.

The *fault\_operation causes the process instance to complete unsuccessfully by throwing the specified fault in the global scope. The process is able to perform recovery using a fault handler in the global scope, through termination handlers in nested scopes and by invoking installed compensation handlers. The process will transition to the \_faulted* state.

The *suspend*, *resume* and *terminate* operations can be used with multiple process instances at the same time, by specifying a list of *instance* elements.

*TBD:* specifying which fault to throw and providing details.

The response uses a structure similar to the *detail* operation. The response includes the requested process instance, and will be empty if that process instance cannot be found in the system. The response reflects the process instance state available on return. Some state changes take significant time to process, e.g. when throwing a fault in the process, and may not be reflected in the response message.

<a id="bpel-management-api-specification--delete-process-instances"></a>

### Delete Process Instances

The *delete* operation delete all, or some completed process instances.

The request identifies the process instances using a filter that can select instances with a given name, status, property values, etc. Alternatively, the *instance* element can be used to specify a particular process instance to delete. The *instance* element can be repeated to delete multiple process instances in the same operation. At least one of these elements is required. The request schema has the following structure:

```
<delete>
  <filter> filter <filter> | <instance pid = token/>+
</delete>
```

This operation uses the same filters as the *list* operation, with the exception that the only meaningful status codes are *completed*, *terminated* and *faulted*. A process instance that is in the active, suspended or error state cannot be deleted. Similarly, specifying a process instance has no affect if that instance is not in the *completed*, *terminated* or *faulted* state.

The operation returns a message listing all the deleted process instances:

```
<delete.response>
  <instance pid = token/>*
</delete.response>
```

---

<a id="developerguide-architectural-overview"></a>

<!-- source_url: https://ode.apache.org/developerguide/architectural-overview.html -->

<!-- page_index: 43 -->

# Architectural Overview

---

<a id="extensions-extension-activities-extensible-assign-operations"></a>

<!-- source_url: https://ode.apache.org/extensions/extension-activities-extensible-assign-operations.html -->

<!-- page_index: 44 -->

<a id="extensions-extension-activities-extensible-assign-operations--bpel-extensibility"></a>

## BPEL Extensibility

Since BPEL 2.0 it is possible to extend the language by user-defined activities and custom variable assignment mechanisms.

Apache ODE (>= 2.0) supports these extensibility mechanisms and provides a plug-in architecture that allows for registering third-party extensions.

BPEL extensions must be declared for use in the process preamble to tell the engine which extensions must be available and which are optional. This can be done by adding an `<extension>` element to your BPEL process model:

```
<bpel:process...>
    <bpel:extensions>
        <bpel:extension namespace="#extension-namespace#" 
                        mustUnderstand="#yes|no#"/>
    </bpel:extensions>
...
</bpel:process>
```

This snippet declares the given extension namespace and tells the engine what to do if no extension bundle is registered for this namespace. If `mustUnderstand` is `yes` and no extension bundle is registered the engine complains during the deployment of the process model and refuses the execution of the process model. If `mustUnderstand` is `no` the engine logs a warning but continuous with deployment and execution. Unregistered extension activities are then executed like an `<empty>` activity.

<a id="extensions-extension-activities-extensible-assign-operations--extension-activities"></a>

### Extension Activities

```
<extensionActivity>
    <anyElementQName standard-attributes>
        standard-elements
    </anyElementQName>
</extensionActivity>
```

<a id="extensions-extension-activities-extensible-assign-operations--extensible-assign-operations"></a>

### Extensible Assign Operations

```
<assign validate="yes|no"? standard-attributes>
    standard-elements
    <extensionAssignOperation>
        assign-element-of-other-namespace
    </extensionAssignOperation>
</assign>
```

<a id="extensions-extension-activities-extensible-assign-operations--using-bpel-extensibility-in-apache-ode"></a>

## Using BPEL Extensibility in Apache ODE

> [!NOTE]
> <a id="extensions-extension-activities-extensible-assign-operations--ode-version"></a>

>
> > [!NOTE]
> > #### ODE version
>
> These extension points are only available on ODE experimental

In ODE extension activities and extension assign operations are grouped into so called Extension Bundles. Extension bundles are associated with an extension namespace and may provide several Extension Operations. Extension operations are the actual implementations of extension code and can be used for both, extension activities and extension assign operations.

<a id="extensions-extension-activities-extensible-assign-operations--installation-of-extensions-war-axis2-deployable"></a>

### Installation of extensions (WAR - Axis2 deployable)

- Copy the extension. The extension bundle and its dependencies must be part of the class path. The easiest way to achieve this is to copy the extension jar to /WEB-INF/lib.
- Register the extension. Open `/WEB-INF/conf/ode-axis2.properties` and add/uncomment the following lines:


```
ode-axis2.extension.bundles.runtime = fqcn.to.extension.bundle
ode-axis2.extension.bundles.validation = fqcn.to.extension.bundle
```

  The validation entry is only necessary if the extension bundle also provides compile-time validators
- Start/Restart Apache ODE

<a id="extensions-extension-activities-extensible-assign-operations--installation-of-extensions-jbi"></a>

### Installation of extensions (JBI)

- Embed the extension. The extension bundle and its dependencies must be part of the class path. The easiest way is to add the extension jar to the JBI deployable.
- Register the extension. Extract and open ode-jbi.properties from ODE SE and add/uncomment the following lines:


```
ode-jbi.extension.bundles.runtime = fqcn.to.extension.bundle
ode-jbi.extension.bundles.validation = fqcn.to.extension.bundle
```

  The validation entry is only necessary if your extension bundle also provides compile-time validators.
- Re-add the properties file to the service engine archive and deploy it to the JBI container of choice.

<a id="extensions-extension-activities-extensible-assign-operations--developing-extension-bundles"></a>

## Developing Extension Bundles

TBC...

---

<a id="extensions-external-variables"></a>

<!-- source_url: https://ode.apache.org/extensions/external-variables.html -->

<!-- page_index: 45 -->

<a id="extensions-external-variables--external-variables"></a>

## External Variables

- [Declaring External Variables in the Process Definition](#extensions-external-variables--externalvariables-declaringexternalvariablesintheprocessdefinition)
- [Incomplete Keys](#extensions-external-variables--externalvariables-incompletekeys)
- [JDBC Mapping](#extensions-external-variables--externalvariables-jdbcmapping)
- [REST Mapping](#extensions-external-variables--externalvariables-restmapping)

<a id="extensions-external-variables--declaring-external-variables-in-the-process-definition"></a>

### Declaring External Variables in the Process Definition

> [!NOTE]
> External variables are only available on ODE 1.2+

Syntax:

```
<scope>
   <variables xmlns:xvar=" http://ode.apache.org/externalVariables">
     <variable name="ext-var-name" element="ext-var-type" xvar:id="ext-var-id">
        <xvar:key-map key="key-id">*
            <expression>key-expression</expression>
        </xvar:key-map>
     </variable>
    </variables>
</scope>
```

External variables are declared in the `<variables>` section of the `<scope>` element, just like normal variables. However, unlike regular variables, external variables must specify the additional `xvar:id` attribute. This attribute identifies the variable as an external variable and links the external variable's declaration to the external variable's configuration in the deployment descriptor.

In addition to this attribute, an external variable may also define a set of key mappings by nesting `xvar:key-map` elements within the declaration. The key mappings are a collection of name-expression pairs that is used to create a composite key (identity) for the external variable. This composite key is used to retrieve the correct "instance" of the variable from the underlying storage. The key mappings are BPEL expressions ( i.e. XPath expressions) that are evaluated once, at the time that the scope is instantiated. Therefore, the "identity" of an external variable is determined during scope creation, and cannot be changed by the process (for qualifications see Incomplete Keys below).

Finally, any external variables must be of an "element" type, with a schema conforming to the requirements of the underlying storage mechanism.

Consider the following example:

process.bpel

```
...
<scope>
  <variables>
    <variable name="customer" element="myns:CustomerElement" xvar:id="customer1" >
       <xvar:key-map key="customer-id">
           <expression>$order/customerid</expression>
       </xvar:key-map>
    </variable>
  </variables>
</scope>
...
```

In the above, the "customer" variable is an external variable. The key for the external variable is derived from the value of the `customerid` element in the "order" variable. Note that the "order" variable must be declared in a scope above the scope declaring the "customer" external variable, otherwise it would not be possible to resolve the identify of the "customer" variable. In this scenario, the external variable can be "read" even if it was never assigned to in the process.

<a id="extensions-external-variables--incomplete-keys"></a>

### Incomplete Keys

It is not required that the full identity of the external variable be resolved at scope creation. For example, an external variable may correspond to a database row where the identity is generated by the database during an insert operation. In such a scenario the key mapping can be omitted, and the identity of the external variable will be unknown until the variable is assigned to. Any attempt to access the variable before the first assignment will result in an uninitialized variable fault. In general it is possible to specify external variables where some portions of the identity are determined using the key mappings and some using some other (implementation-specific) mechanism. In any case, if when the variable is read, the key is incomplete an uninitialized variable fault will result.

<a id="extensions-external-variables--jdbc-mapping"></a>

### JDBC Mapping

[External Variables - JDBC Mapping](https://ode.apache.org/extensions/external-variables-jdbc-mapping.html)

<a id="extensions-external-variables--rest-mapping"></a>

### REST Mapping

[External Variables - REST Mapping] TODO

---

<a id="extensions-flexible-assigns"></a>

<!-- source_url: https://ode.apache.org/extensions/flexible-assigns.html -->

<!-- page_index: 46 -->

<a id="extensions-flexible-assigns--auto-complete-copy-destination-l-value"></a>

## Auto Complete Copy Destination (L-Value)

A lot of times, users expect the  operation in a WS-BPEL assign activity to behave such that the path specified by the destination ("to-spec") is automatically created, if it doesn't already exist. By default, if the to-spec used within a  operation does not select exactly one XML information item during execution, then the standard fault bpel:selectionFailure is thrown (as mandated by the spec).

To override this default behavior, we introduce a insertMissingToData attribute in the  operation, which if it is set to "yes", will instruct the runtime to complete the (XPath) L-value specified by the to-spec, if no items were selected. For the sake of simplicity, we will complete the to-spec if and only if:
1. It's a path expression whose steps are separated by "/", and
1. Its steps have an axis, which is either "child" or "attribute", and
1. Its steps have no following predicates, and
1. Its steps test the name of a node, without the use of wildcards.

Formally, the grammar of the to-spec, for which auto-complete is enabled, may be defined in terms of these productions:

```
PathExpr ::= ("/" RelativePathExpr?) | RelativePathExpr 
RelativePathExpr ::= ForwardStep (("/" ) ForwardStep)* 
ForwardStep ::= (ForwardAxis QName) | AbbrevForwardStep 
AbbrevForwardStep ::= "@"? QName 
ForwardAxis ::= ("child" "::") | ("attribute" "::")
```

The example below illustrates the use of the insertMissingToData attribute. Let's say that the variable "response" is uninitialized. In that case, the first  operation will fail, whereas the second one will succeed.

```
<copy> 
    <from>$request.requestMessageData/typeIndicators/types:indicatorTwo</from> 
    <to>$response/typeIndicators/types:indicatorTwo</to> 
</copy>

<copy insertMissingToData="yes"> 
    <from>$request.requestMessageData/typeIndicators/types:indicatorTwo</from> 
    <to>$response/typeIndicators/child::types:indicatorTwo</to> 
 </copy>
```

<a id="extensions-flexible-assigns--add-support-for-the-ignoremissingfromdata-attribute-in-copy"></a>

## Add support for the ignoreMissingFromData attribute in `<copy>`

The attached patch adds support for the following attributes in the BPEL assign activity's copy operation:

1. The optional @ignoreMissingFromData attribute, which if it has the value of "yes", and the from-spec returns zero XML information items, then no bpel:selectionFailure is thrown, and the to-spec is not evaluated.
2. An extension @ignoreUninitializedFromVariable attribute, which if it has the value of "yes", and the from-spec contains an uninitialized variable, then no bpel:uninitializedVariable is thrown, and the to-spec is not evaluated.

The informal syntax of the above attributes is shown below:

```
<copy ignoreMissingFromData="yes|no"? ignoreUninitializedFromVariable="yes|no"?> 
      from-spec to-spec 
</copy>
```

---

<a id="extensions-headers-handling"></a>

<!-- source_url: https://ode.apache.org/extensions/headers-handling.html -->

<!-- page_index: 47 -->

<a id="extensions-headers-handling--overview"></a>

## Overview

There are several situations where one would want to access headers form the wire format in their BPEL process. It could be to assign them to another message and pass them around or to execute some business logic that's header-dependent (often a bad idea but sometimes there's no choice). ODE supports the manipulation of wire format headers in two different ways.

<a id="extensions-headers-handling--headers-as-abstract-message-parts"></a>

### Headers as Abstract Message Parts

In SOAP, message parts can be bound to a SOAP header. This requires to define all the parts that you want to extract in the abstract message definition and then create an appropriate binding to specify the parts that actually go in the header.

Once this is done, the header part is actually physically present in the abstract message definition and can be accessed like any other message part in your process. Headers can therefore be assigned using the classic from/part and to/part assignments, no specific extension is needed.

<a id="extensions-headers-handling--dynamic-headers"></a>

### Dynamic Headers

When headers aren't declared in the WSDL abstract message (or even in the binding), ODE still checks which headers are present in the exchanged SOAP messages and retrieve them. Those are dynamic headers, there's no validation as to which headers are present or absent, ODE just takes what's there.

Those headers can't be manipulated and assigned directly like a normal part as they don't have a part definition. So ODE supports a specific and additional type of  and  for assignments:

```
<from variable="BPELVariableName" header="NCName"?>
   <query queryLanguage="anyURI"?>?
      queryContent
   </query>
</from>

<to variable="BPELVariableName" header="NCName"?>
   <query queryLanguage="anyURI"?>?
      queryContent
   </query>
</to>
```

Using these  and  specifications, dynamic headers can be accessed and manipulated in your BPEL process. For example, passing a ConversationId SOAP header from an incoming to an outgoing message could look like:

```
<copy>
<from
variable=
"inputMsg"
header=
"ConversationId"
/>
<to
variable=
"outputMsg"
header=
"ConversationId"
/>
</copy>
```

Note that SOAP headers being *always* elements, a simple type (like a string) can't be used to assign to a header.

---

<a id="extensions-implicit-correlations"></a>

<!-- source_url: https://ode.apache.org/extensions/implicit-correlations.html -->

<!-- page_index: 48 -->

# Implicit Correlations

- [Introduction](#extensions-implicit-correlations--implicitcorrelations-introduction)
- [Process to Process Interaction Use Case](#extensions-implicit-correlations--implicitcorrelations-processtoprocessinteractionusecase)
- [Process to Service Interaction Use Case](#extensions-implicit-correlations--implicitcorrelations-processtoserviceinteractionusecase)

<a id="extensions-implicit-correlations--introduction"></a>

### Introduction

BPEL process instances are stateful --- therefore, a client interacting with the BPEL engine must identify the particular instance with which it intends to interact in all of its communications. The BPEL specification defines a mechanism --- *correlation* --- which allows the process designer to specify which parts of an incoming message (i.e. a message going from a client to the BPEL server) should be used to identify the target process instance. Correlation is a powerful mechanism --- however it is a bit complicated and relies on "in-band" message data to associate a messages with a process instance.

To keep simple cases simple, ODE provides an alternative correlation mechanism --- *implicit correlation* --- that automatically handles correlation through "out-of-band" session identifiers. The mechanism is simple: a unique session identifier is associated with every every partner link instance. When a message is sent on a partner link, the session identifier is sent along with the message. The recipient is then able to use the received session identifier in subsequent communications with the process instance. Messages received by the BPEL engine that have a session identifier are routed to the correct instance (and partner link) by that session identifer.

There are two major use cases for the implicit correlation mechanism requiring different levels of familiarity with the mechanism's details: process to process and process to service interactions. The former case deals with situations where the ODE BPEL process instance is communicating with another ODE process instance. The latter deals with situations where a ODE BPEL process instance is communicating with an external (non-ODE) service.

<a id="extensions-implicit-correlations--process-to-process-interaction-use-case"></a>

### Process to Process Interaction Use Case

When an ODE process needs to communicate with other ODE processes, using implicit correlations is quite simple. Simply omit the `<correlations>` element from the `<receive>`, `<pick>`, and `<invoke>` activities. The following is an example showing one process (processA) starting another (processB) and then being called back:

- ProcessA


```
...<invoke name="initiate" partnerLink="responderPartnerLink" portType="test:MSResponderPortType" operation="initiate" inputVariable="dummy"/> <receive name="callback" partnerLink="responderPartnerLink" portType="test:MSMainPortType" operation="callback" variable="dummy"/>...
```

- ProcessB


```
...<receive name="start" partnerLink="mainPartnerLink" variable="dummy" portType="resp:MSResponderPortType" operation="initiate" createInstance="yes"/> <invoke name="callback" partnerLink="mainPartnerLink" portType="resp:MSMainPortType" operation="callback" inputVariable="dummy"/>...
```

In the above example, ODE will use the implicit correlation mechanism because no explicit correlations are specified. Communication between the two processes will reach the correct instance as long as the same partner link is used.

For a complete example check [MagicSession](https://svn.apache.org/repos/asf/ode/trunk/distro/src/examples-war/MagicSession/).

<a id="extensions-implicit-correlations--process-to-service-interaction-use-case"></a>

### Process to Service Interaction Use Case

See the [Stateful Exchange Protocol](#developerguide-stateful-exchange-protocol).

---

<a id="extensions-iterable-foreach"></a>

<!-- source_url: https://ode.apache.org/extensions/iterable-foreach.html -->

<!-- page_index: 49 -->

<a id="extensions-iterable-foreach--overview"></a>

## Overview

This extension simplifies a common usage pattern in which forEach is used to iterate over a selected sequence of nodes.

The common use case involves selecting a sequence of nodes, storing it in a scope variable, and using forEach to iterate over that sequence, using the current counter value to extract and operate on the indexed value from the sequence. This extension captures the pattern in a form that's easier to author and debug, by replacing counter with iterator and eliminating the use of temporary variables.

<a id="extensions-iterable-foreach--processing-multiple-branches-foreach"></a>

## Processing Multiple Branches - ForEach

The `<forEach>` activity will execute its contained  activity exactly M times where M is the number of items in the .

```
<forEach rangeName="BPELVariableName" parallel="yes|no"
   standard-attributes>
   standard-elements
   <sequenceValue expressionLanguage="anyURI"? instanceOf="sequenceType">
      unsigned-integer-expression
   </sequenceValue>
   <completionCondition>?
      <branches expressionLanguage="anyURI"?
         successfulBranchesOnly="yes|no"?>?
         unsigned-integer-expression
      </branches>
   </completionCondition>
   <scope ...>...</scope>
</forEach>
```

When the  activity is started, the expression in  is evaluated. Once that value is returned it remains constant for the lifespan of the activity. [SA00074] That expressions MUST return a sequence of items (meaning it comprises nodes, texts or atomic values), where ach item can be validated to be the type specified by the instanceOf attribute. If that expression does not return a valid sequence value, a bpel:invalidExpressionValue fault will be thrown (see section 8.3. Expressions). If the  is empty, then the child  activity MUST NOT be performed and the  activity is complete.

The child activity of a  MUST be a  activity. The  construct introduces an implicit range variable, and also introduces dynamic parallelism (i.e. having parallel branches of which number is not known ahead of time). The  activity provides a well-defined scope snapshot semantic and a way to name the dynamic parallel work for compensation purposes (see scope snapshot description in section 12.4.2. Process State Usage in Compensation Handlers).

If the value of the parallel attribute is no then the activity is a serial . The enclosed  activity MUST be executed M times, each instance starting only after the previous repetition is complete. If premature termination occurs such as due to a fault, or the completion condition evaluates to true, then this M requirement does not apply. During each repetition, a variable of type specified by the instanceOf attribute is implicitly declared in the  activity's child . This implicit variable has the name specified in the rangeVariableName attribute. The first iteration of the scope will see the range variable initialized to the first item in . The next iteration will cause the range variable to be initialized to the second item in . Each subsequent iteration will move the range variable to the next item in the sequence until the final iteration where the range will be set to the last item in . The range variable is local to the enclosed  and although its value can be changed during an iteration, that value will be lost at the end of each iteration. Therefore, the range variable value will not affect the value of the next iteration's range.

If the value of the parallel attribute is yes then the activity is a parallel . The enclosed  activity MUST be concurrently executed M times. In essence an implicit  is dynamically created with M copies of the 's enclosed  activity as children. Each copy of the  activity will have the same range variable declared in the same manner as specified for serial . Each instance's range variable MUST be uniquely initialized in parallel to one of the teim values starting with first and up to and including the last item in , as a part of  instantiation.

[SA00076] If a variable of the same name as the value of the rangeName attribute is declared explicitly in the enclosed scope, it would be considered a case of duplicate variable declaration and MUST be reported as an error during static analysis.

The  activity without a  completes when all of its child 's have completed. The  element is optionally specified to prevent some of the children from executing (in the serial case), or to force early termination of some of the children (in the parallel case).

The  element represents an unsigned-integer expression (see section 8.3.4. Unsigned Integer Expressions) used to define a completion condition of the "at least N out of M" form. The actual value B of the expression is calculated once, at the beginning of the  activity. It will not change as the result of the  activity's execution. At the end of execution of each directly enclosed  activity, the number of completed children is compared to B, the value of the  expression. If at least B children have completed, the  is triggered: No further children will be started, and currently running children will be terminated (see section 12.6 Termination Handlers). Note that enforcing the semantic of "exactly N out of M" in parallel  would involve a race condition, and is therefore not specified.

When the completion condition B is calculated, if its value is larger than the number of directly enclosed activities M, then the standard bpel:invalidBranchCondition fault MUST be thrown. [SA00075] Both B and M may be constant expressions, and in such cases, static analysis SHOULD reject processes where it can be detected that B is greater than M.

The  element has an optional successfulBranchesOnly attribute with the default value of no. If the value of successfulBranchesOnly is no, all 's which have completed (successfully or unsuccessfully) MUST be counted. If successfulBranchesOnly is yes, only 's which have completed successfully MUST be counted.

The  is evaluated each time a directly enclosed  activity completes. If the  evaluates to true, the  activity completes:

- When the  is fulfilled for a parallel  activity, all still running directly enclosed  activities MUST be terminated (see section 12.6 Termination Handlers).
- When the  is fulfilled for a serial  activity, further child 's MUST NOT be instantiated, and the  activity completes.

If upon completion of a directly enclosed  activity, it can be determined that the  can never be true, the standard bpel:completionConditionFailure fault MUST be thrown.

When a  does not have any sub-elements or attributes understood by the WS-BPEL processor, it MUST be treated as if the  does not exist.

---

<a id="extensions-process-contexts"></a>

<!-- source_url: https://ode.apache.org/extensions/process-contexts.html -->

<!-- page_index: 50 -->

<a id="extensions-process-contexts--process-contexts"></a>

## Process Contexts

> [!NOTE]
> This feature is implemented in Apache ODE 2.0 only.
<a id="extensions-process-contexts--abstract"></a>

### Abstract

To allow the circulation of transport metadata from messages to processes and then from processes to messages, we want to add support for different levels of contextual data to our process engine. The main use cases are:

- Conversation ids, such as those of the Stateful Exchange Protocol and WS-Context
- Tracing ids, mostly with ServiceMix.
- Credentials (such as tokens) for authentication and authorization
- Eventually some WS-RM related context.

<a id="extensions-process-contexts--architecture"></a>

### Architecture

The aim of this proposal is to make transport metadata accessible within BPEL processes and allow modelers and deployers to define which metadata should be propagated between process and partners. Therefore, we model such metadata in terms of contexts. *Contexts* are modeled as a bag of metadata information represented as key-value pairs and are attached to partner links. A partner link may maintain multiple contexts; each of them is identifiable by a name attribute to distinguish context used for different purposes (e.g. security context vs. tracing context).
Whenever a message arrives through ODE's integration layer, the message is passed through a defined set of *context interceptors*. These interceptors are in charge to extract relevant transport metadata from messages, prepare the data and store it in terms of key-value pairs into a named context associated to the partner link from which the message came from. The context data is persistently stored in the runtime database.
For outgoing messages,  activities can be configured to take context data from a (different) partner link, pass it again through a *context interceptor* which translates the data back to transport-specific metadata. Such propagation configuration can be defined per invoke activity in the process model or on a global level in the deployment descriptor.
Context data can be assigned to variables. Therefore, the context data is translated into XML data, following a predefined schema. It is possible to define which contexts of a partner link are copied to a variable. Similarly, context data can be copied from a variable back into the context of a certain partner link.
Contexts can be used to classify or tag process instances and it is useful to make this information accessible for process management tools. Hence, this specification extends the process management API to make context data queryable and accessible.

<a id="extensions-process-contexts--contexts"></a>

### Contexts

Contexts are modeled as a bag of metadata information represented as key-value pairs *(string, string)* and are attached to partner links. Contexts have a name attribute. Contexts are persisted in ODE's runtime database. Long values are stored as a CLOB whereas shorter values (< 250 characters) are automatically stored in an indexed VARCHAR field.

Since contexts should also be accessible in BPEL, there is also an XML-based representation. It is defined as follows, the according XMLSchema can be found [here](http://svn.apache.org/viewvc/ode/trunk/bpel-schemas/src/main/xsd/contexts.xsd?view=markup)

Example: Context data in its XML representation

```
<?xml version="1.0" encoding="UTF-8"?>
<ctx:contexts xmlns:ctx="http://www.apache.org/ode/schemas/context/2009" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.apache.org/ode/schemas/context/2009 contexts.xsd ">
  <ctx:context name="foo">
    <ctx:value key="bar">baz</ctx:value>
  </ctx:context>
  <ctx:context name="tracing">
    <ctx:value key="id">0815</ctx:value>
  </ctx:context>
</ctx:contexts>
```

<a id="extensions-process-contexts--context-interceptors"></a>

### Context Interceptors

At the transport level, message headers can be translated to context data and contexts can be translated to message headers. Context interceptors define how the headers are set to/from contexts and which contexts are affected. Interceptors are Java classes that implement the following interface. They can be registered either globally in ode's property configuration file or per process in the `deploy.xml`.

```
/** * Context Interceptors can map message headers (or even payload) to * context information that is attached to process models.*/ public interface ContextInterceptor {/** * Configures the interceptor. This method will be called immediatedly after * instantiation of the implementing class. The passed element will contain the * configuration elements given in the deploy.xml. In case of a declaration in * ode-xxx.properties, the method won't be called.* * @param configuration */ void configure (Element configuration ); /** * Translates the data stored within the context object into SOAP headers or * vice versa.* * If direction is OUTBOUND, context data must be converted into message headers * if direction is INBOUND, context data must be extracted from the message.*/ void process (ContextData ctx,MessageExchangeDAO mexdao,IOContext.Direction dir) throws ContextException;
}
```

There is also a more high-level interface defined in terms of an abstract class:

```
public abstract class AbstractContextInterceptor implements ContextInterceptor {public abstract void configure (Element configuration ); /** * @see org.apache.ode.bpel.context.ContextInterceptor#process(org.apache.ode.bpel.rapi.ContextData, org.apache.ode.bpel.dao.MessageExchangeDAO, org.apache.ode.bpel.rapi.IOContext.Direction) */ public void process (ContextData ctx,MessageExchangeDAO mexdao,IOContext.Direction dir) throws ContextException {// dispatch} abstract void onPartnerInvoke (ContextData ctx,Message msg ); abstract void onPartnerReply (ContextData ctx,Message msg ); abstract void onProcessInvoke (ContextData ctx,Message msg ); abstract void onProcessReply (ContextData ctx,Message msg );}
```

<a id="extensions-process-contexts--working-with-contexts-in-bpel"></a>

### Working with Contexts in BPEL

<a id="extensions-process-contexts--declaring-context-interceptors"></a>

#### Declaring Context Interceptors

In order to use context interceptors, their implementation must be registered with ODE. There are two options to do this:
 *Engine-wide registration - the context interceptor will be available for all processes that are deployed to this ODE instance.* Per-process registration - the context interceptor will only be available for a particular process model.

Engine-wide context interceptors are registered in ODE's properties file (either `ode-axis2.properties` or `ode-jbi.properties`) using the properties key `context.interceptors`.

ode-axis2.properties

```
...
ode-axis2.context.interceptors = my.full.qualified.context.interceptor.class.name
...
```

ode-jbi.properties

```
...
ode-jbi.context.interceptors = my.full.qualified.context.interceptor.class.name
...
```

Per-process context interceptors are declared in ODE's deployment descriptor deploy.xml:

deploy.xml

```
<deploy xmlns="http://www.apache.org/ode/schemas/dd/2007/03"
    xmlns:pns="http://ode/bpel/unit-test"
    xmlns:wns="http://ode/bpel/unit-test.wsdl">

    <process name="pns:HelloWorld2">
        <active>true</active>
        <provide partnerLink="helloPartnerLink">
            <service name="wns:HelloService" port="HelloPort"/>
        </provide>
        <context>
            <propagate from="helloPartnerLink" to="helloPartnerLink2" context="*"/>
            <interceptor>
                <class-name>org.apache.ode.bpel.context.TestInterceptor</class-name>
                <config>
                    <myparam1>x</myparam1>
                    <myparam2>y</myparam2>
                </config>
            </interceptor>
        </context>
    </process>
</deploy>
```

The context-specific configuration takes place in the `<context>` element. The `<interceptor>` element is used to declare and register context interceptor implementations. The `<class-name>` element takes the full qualified class name of the context interceptor implementation (which must implement the `ContextInterceptor` interface). The content of the `<config>` element will be passed to configure method of the interceptor, immediately after instantiation.

Static propagation rules can be configured directly in the `deploy.xml`. Using the `<propagate>` element, ODE can be configured to propagate all contexts named in the `context` attribute (space-separated list) from a certain partner link to another partner link. To propagate all contexts the `context` attribute should be set to `\*`. These rules are automatically evaluated when an invoke activity is being executed. Before a BPEL process instance invokes an operation of a certain partner link, the propagation logic performs a look-up for propagation rules that have that partner link referenced by their `to` attribute. Subsequently the specified contexts are retrieved from the partner link specified by the `from` attribute of the rule, passed to the context interceptor that translates the context data into transport meta data, which is then added to the outgoing message.

<a id="extensions-process-contexts--customize-context-propagation-in-the-process-model"></a>

#### Customize Context Propagation in the Process Model

In addition to static propagation rules, context propagation can be explicitly configured for outbound interaction activities (i.e. `<invoke>` and `<reply>`. Therefore, we introduce a new BPEL extension element `<ctx:propagate>` in the `[http://ode.apache.org/contextPropagation](http://ode.apache.org/contextPropagation)` namespace (to which the `ctx`-prefix is bound to), following the syntax as described below:

```
<bpel:invoke ...> <ctx:propagate ctx:fromPartnerLink="testPartnerLink" ctx:context="*" /> </bpel:invoke> <bpel:reply ...> <ctx:propagate ctx:fromPartnerLink="testPartnerLink" ctx:context="*" /> </bpel:reply>
```

- `ctx:fromPartnerLink` identifies the partner link the context data should be retrieved from.
- `ctx:context` identifies which contexts should be propagates. This is a space-separated list of context names. `\*` serves as a wild card to copy all contexts.

The context data identified by this propagation rule will be passed to all registered context interceptors which enhance the outgoing message accordingly.

> [!NOTE]
> All partner link references are resolved by the interaction activity, i.e. only partner links can be referenced that are visible to the respective activity.
<a id="extensions-process-contexts--accessing-and-assigning-context-data"></a>

#### Accessing and Assigning Context Data

Context data should be accessible within BPEL processes and from the outside, e.g. for management purposes. For the former, the `<assign>` activity has been extended to support copying data from and to contexts of a partner link. The according `from`/`to` specs are defined as follows:

from/to specs for the work with context data

```
<assign>
    <!-- copy 'tracing' and 'security' contexts to a variable. -->
    <copy>
        <from partnerLink="pl1" context="tracing security"/>
        <to>$var</to>
    </copy>

    <!-- copy context data from $var to pl1. Only 'tracing' and 'security' contexts will be written, other contexts remain unchanged. -->
    <copy>
        <from>$var</from>
        <to partnerLink="pl1" context="tracing security"/>
    </copy>

    <!-- copy 'tracing' and 'security' contexts from pl1 to pl2. Pre-existing contexts in pl2 will be purged (*). -->
    <copy>
        <from partnerLink="pl1" context="tracing security"/>
        <to partnerLink="pl2" context="*"/>
    </copy>

    <!-- copy 'tracing' and 'security' contexts from pl1 to pl2. Pre-existing contexts in pl2 will be merged (+). -->
    <copy>
        <from partnerLink="pl1" context="tracing security"/>
        <to partnerLink="pl2" context="+"/>
    </copy>

    <!-- copy all contexts from pl1 to pl2. Pre-existing contexts in pl2 will be merged (+). -->
    <copy>
        <from partnerLink="pl1" context="*"/>
        <to partnerLink="pl2" context="+"/>
    </copy>

</assign>
```

> [!NOTE]
> - `context="*"` in `from`-specs selects all contexts.
> - `context="*"` in `to`-specs replaces existing contexts with context data selected by the `from`-spec.
> - `context="+"` in `to`-specs merges existing contexts with context data selected by the `from`-spec.

When assigning context data to variables, the variable should be declared to be an instance of the context XSD (see [Contexts section](#extensions-process-contexts--contexts.html)). It is also possible to copy only fragments of a context data set by applying an XPath query to the `from`-spec:

Applying XPath-query to context data

```
<assign>
    <!-- copy tracing id to a string variable. -->
    <copy>
        <from partnerLink="pl1" context="*">
            <query>/ctx:contexts/ctx:context[@name='tracing']/ctx:value[@key='id']</query>
        </from>
        <to>$tracingId</to>
    </copy>
</assign>
```

In order to make context data accessible for external management tools, the ProcessManagement-API has been extended. TODO: to be completed.

---

<a id="extensions-restful-bpel-part-i"></a>

<!-- source_url: https://ode.apache.org/extensions/restful-bpel-part-i.html -->

<!-- page_index: 51 -->

<a id="extensions-restful-bpel-part-i--restful-bpel-i"></a>

## RESTful BPEL (I)

> [!NOTE]
> This feature is not yet implemented in ODE. This is a proposal and is subject to change based on feedback, implementation experience, etc.
<a id="extensions-restful-bpel-part-i--invoke"></a>

### Invoke

The RESTfulvariant of the invoke activity replaces the attributes partnerLink/operation with resource and method. The method attribute identifies the HTTP method. All HTTP methods are supported, although this spec is only concerned with GET, POST, PUT and DELETE. The resource attribute identifies a BPELvariable of a simple type (xsd:uri, xsd:string, etc) used as the URL of the actual resource. The resource element can be used instead of the resource attribute to calculate the URL using an expression.

In addition to the above, the invoke activity adds a way to map values to/from HTTP headers, using a syntax similar to that for mapping message parts, but specifying the corresponding HTTP header instead. Headers mapped by the process override default values, and some headers have special handling.

The implementation shields the invoke activity from some of the details of the HTTP protocol, specifically:
 *Requests automatically follow redirects.* The Location and Content-Location headers are expanded to absolute URLs and will only use HTTP/HTTPS URLs.
 *Content negotiation and compression are handled automatically.* Proxies are handled automatically.
 *GET, PUT and DELETE requests retried automatically for certain error conditions.* GET requests may be cached by the engine, private caching is never shared across process instances.

This example uses the myPost variable to create a new blog post, store the response in the newPost variable, and the location of the new post in the variable newPostUrl:

```
invoke resource =createPostsUrl method =post input =myPost output =newPost from header =location to =newPostUrl
```

And to update the post:

```
invoke resource =newPostUrl method =put input =updatedPost
```

<a id="extensions-restful-bpel-part-i--xpath-functions"></a>

### XPath functions

The use or URLs requires the ability to combine URLs with two new XPath functions: `combine-url(base, relative)` and `compose-url(template, [name, value]*)` / `compose-url(template, pairs)`. See [xpath extensions](#extensions-xpath-extensions--combineurl-base-relative) for details.

---

<a id="extensions-restful-bpel-part-ii"></a>

<!-- source_url: https://ode.apache.org/extensions/restful-bpel-part-ii.html -->

<!-- page_index: 52 -->

<a id="extensions-restful-bpel-part-ii--restful-bpel-ii"></a>

## RESTful BPEL (II)

> [!NOTE]
> This feature is not yet implemented in ODE. This is a proposal subject to feedback, implementation experience, etc.

<a id="extensions-restful-bpel-part-ii--use-cases"></a>

### Use Cases

*Use case 1*: A client needs to process *foo*, which it does by creating a new resource which it can operate on. The client starts by making a POST request to /foos. This results in a new resource, a response with status code 201 (Created), relevant document and the Location header pointing to the URL of the new resource (/foos/123). The client can then operate on the new resource, e.g. reading its state at various points in time (GET), changing its state (PUT), or even discarding it (DELETE).

*Use case 2*: Continuing with use case 1, the client may need to process *bar* or *baz*, as part of the larger processing of *foo*. The client will attempt to create a new resource under /foos/123/bar or /foos/123/baz, but to do so the client must first determine the URL for either resource. This is done in a separate step, maybe in the response to the request that created /foos/123 or a subsequent operation against that resource (or in fact some other resource).

*Use case 3*: Continuing with use case 1, the client is able to operate on a collection of items that are part of the larger processing of *foo*. Those are exposed behind a URL like /foos/123/items/456, where 456 is the item number. The exact number of resources available depend on the number of items in that collection.

To achive these use cases we need the following features:

1. Ability to instantiate (create) resources that are unique to the processing unit (process, scope).
2. Ability to map resources (URL) into the content of a variable or message.
3. Ability to operate on nested resources, i.e. a resource defined relative to another resource.
4. Ability to recieve messages on a resource signifying a collection and map part of the request URL into member identification.

The above deal specifically with resources, but in addition we will also need a way to handle HTTP variables and query string parameters. We also expect the process engine to take care of common protocol details, such as status codes, redirection, cache control, content negotiation and encoding, HEAD and OPTIONs requests, etc.

<a id="extensions-restful-bpel-part-ii--resources"></a>

### Resources

Resources are declared in a scope, and a scope may declare any number of resources. A resource declaration consists of two properties, the resource **name**, which we use to reference the resource, and a relative **path** that denotes the relationship between this resource and other resources. Once instantiated, the value of the resource is an absolute URL.

The process can use resources in two ways. It can reference a resource for the purpose of receiving requests on that resource or a member of the collection denoted by the resource. It can also access the value of the resource (URL), for example, to send it as part of a message.

To access the value of the resource, we treat the resource as a read-only variable with the type xsd:uri. Expressions can access the resource as they would any other variable available in the scope, but cannot modify (assign to) its value. For that reason, all resources declared in a scope must have unique name and in addition no variable and resource declared in the same scope may have the same name.

A resource that specifies no path (or the empty path) will be instantiated using a URL unique to that process instance. A resource that specifies a static path will be instantiated by appending that path to the instance URL. A resource that specifies a path relative to another resource will be instantiated by appending that path to the URL of the other resource. We use the $ notation to reference another resource, so the path $foo/bar will append /bar to the URL denoted by the resource $foo.

<a id="extensions-restful-bpel-part-ii--recieving-requests"></a>

### Recieving requests

To expose themselves as resources, the receive activity and event handler introduce four new properties. The **method** property specifies the HTTP method to accept, and the semantics of each HTTP method are described below. The **resource** property references a resource declaration available in the scope.

The **instantiateResource** property is true if the resource is instantiated by the receive activity or event handler, and false if the resource must be instantiated before the activity executes. This property can only be set to true when using the POST method, and is always true for the instantiating activity of the process.

When instantiateResource is false, the resource is instantiated first and the activity receives requests on that URL. When instantiateResource is true, the resource value is calculated and the activity receives requests on that URL. Once received, the resource is instantiated by appending a unique identifier to that URL. For example, the receive activity listens on the URL /foos, and upon receipt instantiates the resource to the URL /foos/123. In addition, the corresponding reply activity will set the status code to 201 (Created) and set the Location header to the resource URL.

The **resourceIdentity** activity names a variable that will be set to the member identity when receiving requests on behalf of a collection resource. When used in event handlers, the variable is implicitly defined in the implicit scope of the event handler and has the type xsd:string.

For example, if the resource is /foos/123/bars and the resourceIdentity is set to bar, then the activity will receive requests on the URL /foos/123/bars/{bar}, and the last part of the request URL path (the member identity {bar}) is assigned to the value of the variable bar.

<a id="extensions-restful-bpel-part-ii--post"></a>

#### POST

The POST method has two uses, one involving the creation of a new resource, and the other involving processing of requests that do not map to any other HTTP method. The receive activity is coupled to a reply activity, and no other receive or wait is allowed to occur between the two.

When using the POST method to create a new resource, including in the instantiating activity of the process, the instantiateResource property is set to true, and the resource is instantiated by the activity. The reply activity uses the status code 201 (Created).

When using the POST method to process requests, the instantiate property is set to false. The reply activity sets the status code to 200 (OK), or if there is no document entity, to 204 (No Content).

<a id="extensions-restful-bpel-part-ii--gethead"></a>
<a id="extensions-restful-bpel-part-ii--get-head"></a>

#### GET/HEAD

The GET method has on side effects. To preserve this constraint only event handlers are allowed to use the GET method, and the event handler may only contain the reply activity. In addition, the event handler can only assign to variables declared in the implicit scope of the event handler, and faults occurring in the event handler are not propagated to the enclosing scope.

The process engine uses cache control to optimize the GET method by handling conditional GETs and setting the Last-Modified/ETag headers. These are set to detect any change in the state of the process instance (which excludes responding to a GET request).

The HEAD method is handled using receives for the GET method, without constructing a document entity in the response.

<a id="extensions-restful-bpel-part-ii--put"></a>

#### PUT

The PUT method is used to modify state. To be used successfully in combination with GET, the process engine supports conditional PUTs and returns 412 (Precondition Failed) if it detects a change in the process state since the corresponding GET.

The receive activity is coupled to a reply activity, and no other receive or wait is allowed to occur between the two. The reply activity sets the status code to 200 (OK), or if there is no document entity, to 204 (No Content).

<a id="extensions-restful-bpel-part-ii--delete"></a>

#### DELETE\*

The DELETE method does not have a corresponding reply activity and returns the status code 200 (OK).

<a id="extensions-restful-bpel-part-ii--options"></a>

#### OPTIONS

The OPTIONS method is handled by the process engine.

<a id="extensions-restful-bpel-part-ii--additional"></a>

### Additional

Since all incoming requests must disambiguate a receive activity, no two receive activities can be outstanding on the same URL using the same method. This behavior is defined in term of URLs not resources, since it is possible for two resources to denote the same URL. It is also possible for the same resource to be used, once with the resourceIdentity property and once without, since those map two distinct URLs (/foos/something vs /foos).

The reply activity is matched to the corresponding receive activity based on the resource name.

Both receive and reply activities have access to an implicit message part called bodythat contains the internal representation of the document entity. Receive activities have access to an implicit message part called params, instantiated from the query string parameters. The XML representation of this part consists of the element Parameters, which maps query string parameters as follows:

- foo -- Maps to the element foo.
- foo[bar] -- Maps to the element bar contained in the parent element foo.
- foo[] -- Each value is mapped to an element called foo in the parent element foos.

---

<a id="extensions-xpath-extensions"></a>

<!-- source_url: https://ode.apache.org/extensions/xpath-extensions.html -->

<!-- page_index: 53 -->

<a id="extensions-xpath-extensions--overview"></a>

## Overview

Apache ODE extends the default XPath coverage provided by the [WS-BPEL](#ws-bpel-20) specification mostly by adding support for [XPath 2.0](http://www.w3.org/TR/xpath20/) and by offering a few utility extension functions to make some assignments easier.

<a id="extensions-xpath-extensions--xpath-20"></a>
<a id="extensions-xpath-extensions--xpath-2.0"></a>

### XPath 2.0

To use XPath 2.0 in your processes just use the following *queryLanguage* and *expressionLanguage* attributes:

```
queryLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xpath2.0"
expressionLanguage="urn:oasis:names:tc:wsbpel:2.0:sublang:xpath2.0"
```

If you want support at the process just add these attributes to your root *process* element. If you want to stick with XPath 1.0 but want XPath 2.0 support for a specific assignment you can also define these attributes on an *assign* element.

<a id="extensions-xpath-extensions--extension-functions"></a>

### Extension Functions

All extension functions are defined in the ODE extension namespace: http://www.apache.org/ode/type/extension. This namespace will be associated with the *ode* prefix in the following examples.

<a id="extensions-xpath-extensions--insert-before"></a>

#### insert-before

This is a function that allows you to insert one or more siblings (specified by the $siblings argument in the signature below) before the first node of children (specified by the $children argument), all of whose nodes must have the same parent (specified by the $context argument).

Insert Before

```
ode:insert-before($context as node(), $children as node()*, $siblings as node()*) as node()
```

By design, this function is non-updating in that it preserves the identity and properties of its arguments (i.e., they don't try to change the XML in-place). Instead, a modified copy of the context node is created, essentially giving it a new identity. Further, it returns a single R-value item, as opposed to a sequence. The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:insert-before($parent, $parent/child::node[position()=last()], $siblings)</from>
    <to variable="parent"/>
  </copy>
</assign>
```

For those familiar with the [XQuery Update Facility](http://www.w3.org/TR/2008/CR-xquery-update-10-20080801/), the above example is semantically equivalent to the expression shown below:

XQuery Equivalent

```
insert nodes $siblings before $parent/child::node[position()=last()]
```

<a id="extensions-xpath-extensions--insert-after"></a>

#### insert-after

This is a function that allows you to insert one or more siblings (specified by the $siblings argument in the signature below) after the last node of children (specified by the $children argument), all of whose nodes must have the same parent (specified by the $context argument).

Insert After

```
ode:insert-after($context as node(), $children as node()*, $siblings as node()*) as node()
```

By design, this function is non-updating in that it preserves the identity and properties of its arguments (i.e., they don't try to change the XML in-place). Instead, a modified copy of the context node is created, essentially giving it a new identity. Further, it returns a single R-value item, as opposed to a sequence. The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:insert-after($parent, $parent/child::node(), $siblings)</from>
    <to variable="parent"/>
  </copy>
</assign>
```

For those familiar with the [XQuery Update Facility](http://www.w3.org/TR/2008/CR-xquery-update-10-20080801/), the above example is semantically equivalent to the expression shown below:

XQuery Equivalent

```
insert nodes $siblings after $parent/child::node()
```

<a id="extensions-xpath-extensions--insert-as-first-into"></a>

#### insert-as-first-into

This is a function that allows you to insert the node(s) (specified by the $children argument in the signature below) as the first child(ren) of a given context node (specified by the $context argument).

Insert As First Into

```
ode:insert-as-first-into($context as node(), $children as node()*) as node()
```

By design, this function is non-updating in that it preserves the identity and properties of its arguments (i.e., they don't try to change the XML in-place). Instead, a modified copy of the context node is created, essentially giving it a new identity. Further, it returns a single R-value item, as opposed to a sequence. The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:insert-as-first-into($parent, $children)</from>
    <to variable="parent"/>
  </copy>
</assign>
```

For those familiar with the [XQuery Update Facility](http://www.w3.org/TR/2008/CR-xquery-update-10-20080801/), the above example is semantically equivalent to the expression shown below:

XQuery Equivalent

```
insert nodes $children as first into $parent
```

<a id="extensions-xpath-extensions--insert-as-last-into"></a>

#### insert-as-last-into

This is a function that allows you to insert the node(s) (specified by the $children argument in the signature below) as the last child(ren) of a given context node (specified by the $context argument).

Insert As Last Into

```
ode:insert-as-last-into($context as node(), $children as node()*) as node()
```

By design, this function is non-updating in that it preserves the identity and properties of its arguments (i.e., they don't try to change the XML in-place). Instead, a modified copy of the context node is created, essentially giving it a new identity. Further, it returns a single R-value item, as opposed to a sequence. The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:insert-as-last-into($parent, $children)</from>
    <to variable="parent"/>
  </copy>
</assign>
```

For those familiar with the [XQuery Update Facility](http://www.w3.org/TR/2008/CR-xquery-update-10-20080801/), the above example is semantically equivalent to the expression shown below:

XQuery Equivalent

```
insert nodes $children as last into $parent
```

<a id="extensions-xpath-extensions--delete"></a>

#### delete

This is a function that allows you to delete one or more node(s) (specified by the $children argument in the signature below) from its parent (specified by the $context argument).

Delete

```
ode:delete($context as node(), $children as node()*) as node()
```

By design, this function is non-updating in that it preserves the identity and properties of its arguments (i.e., they don't try to change the XML in-place). Instead, a modified copy of the context node is created, essentially giving it a new identity. Further, it returns a single R-value item, as opposed to a sequence. The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:delete($parent, $children)</from>
    <to variable="parent"/>
  </copy>
</assign>
```

For those familiar with the [XQuery Update Facility](http://www.w3.org/TR/2008/CR-xquery-update-10-20080801/), the above example is semantically equivalent to the expression shown below:

XQuery Equivalent

```
delete nodes $children
```

<a id="extensions-xpath-extensions--rename"></a>

#### rename

This is a function that allows you to rename the context node (specified by the $context argument in the signature below) as per the given name (specified by $item, which is either a QName, Element or String).

Rename

```
ode:rename($context as node(), $name as item()) as node()
```

By design, this function is non-updating in that it preserves the identity and properties of its arguments (i.e., they don't try to change the XML in-place). Instead, a modified copy of the context node is created, essentially giving it a new identity. Further, it returns a single R-value item, as opposed to a sequence. The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:rename($person, fn:QName("http://www.example.com/example", "manager"))</from>
    <to variable="person"/>
  </copy>
</assign>
```

For those familiar with the [XQuery Update Facility](http://www.w3.org/TR/2008/CR-xquery-update-10-20080801/), the above example is semantically equivalent to the expression shown below:

XQuery Equivalent

```
rename $person as fn:QName("http://www.example.com/example", "manager")
```

> [!NOTE]
> <a id="extensions-xpath-extensions--assign-assumptions"></a>

>
> > [!NOTE]
> > #### Assign Assumptions
>
> The WS-BPEL requires that "for a copy operation to be valid, the data referred to by the from-spec and the to-spec MUST be of compatible types." Hence, make sure that when you rename an element, the new name refers to a type that is compatible with the target variable. In other words, it should be of a substitutable (essentially stronger) complex type.
<a id="extensions-xpath-extensions--split-to-elements"></a>

#### split-to-elements

It's impossible to split a given string into a sequence of elements using assignments. The only possible alternative is XSL which is a lot of complexity for a very simple usage pattern. The *ode:splitToElements* function splits a given string (that can be a variable reference) into several elements by using a specific separators. Here is an example:

```
<assign>
  <from>ode:split-to-elements($authorizeMessage.credential/userList, ',', 'user')</from>
  <to>$authorizedUsers</to>
</assign>
```

If the source element contains a list like "joe, paul, fred" the target variable will be assigned the sequence of elements:

```
<user>joe</user>
<user>paul</user>
<user>fred</user>
```

Alternatively this function can take a fourth parameter that would be the namespace of the elements used to wrap the split strings:

```
ode:split-to-elements(stringToSplit, separator, targetElement, targetNamespace)
```

> [!NOTE]
> <a id="extensions-xpath-extensions--deprecated-name"></a>

>
> > [!NOTE]
> > #### Deprecated Name
>
> This function was formerly known as splitToElements, which may still be used, but is deprecated.
<a id="extensions-xpath-extensions--combine-urlbase-relative"></a>
<a id="extensions-xpath-extensions--combine-url-base-relative"></a>

#### combine-url(base, relative)

Takes the relative URL and combines it with the base URL to return a new absolute URL. If the relative parameter is an absolute URL, returns it instead.
This function is similar to [func-resolve-uri](http://www.w3.org/TR/2004/WD-xpath-functions-20040723/#func-resolve-uri). However the latter is available in XPath 2.0 only.

<a id="extensions-xpath-extensions--compose-urltemplate-91name-value93"></a>
<a id="extensions-xpath-extensions--compose-url-template-name-value"></a>

#### compose-url(template, [name, value]\*)

<a id="extensions-xpath-extensions--compose-urltemplate-pairs"></a>
<a id="extensions-xpath-extensions--compose-url-template-pairs"></a>

#### compose-url(template, pairs)

Expands the template URL by substituting place holders in the template, for example, ('/order/{id}', 'id', 5) returns '/order/5'. Substitute values are either name/value pairs passed as separate parameters, or a node-set returning elements with name mapping to value. The functions applies proper encoding to the mapped values. Undefined variables are replaced with an empty string. This function returns an URL.
See also the [URI Template spec](http://bitworking.org/projects/URI-Templates/spec/draft-gregorio-uritemplate-03.html).

<a id="extensions-xpath-extensions--expand-templatetemplate-91name-value93"></a>
<a id="extensions-xpath-extensions--expand-template-template-name-value"></a>

#### expand-template(template, [name, value]\*)

<a id="extensions-xpath-extensions--expand-templatetemplate-pairs"></a>
<a id="extensions-xpath-extensions--expand-template-template-pairs"></a>

#### expand-template(template, pairs)

Similar to `composeURL` but undefined variables are **not** replaced with an empty string. They are ignored. As a result with incomplete mapping may return a new URL template.

<a id="extensions-xpath-extensions--dom-to-string"></a>

#### dom-to-string

This is a function that serializes a DOM node (specified by the $node argument in the signature below) into a string.

Dom To String

```
ode:dom-to-string($node as node()) as xs:string
```

<a id="extensions-xpath-extensions--process-property"></a>

#### process-property

This is a function that allows you to retrieve the value of a property, defined in deploy.xml for the current process, with the given name (specified by the $name argument in the signature below, which is either a QName, String, Element or Single-Valued List).

Process Property

```
ode:process-property($name as item()) as node()
```

Basically, this method gives you a way to reference properties, defined in deploy.xml for a given process, directly in the BPEL code for that process. The $name argument refers to any schema item that resolves to a QName. The return value is the child node of the property element with the given name.

The example below illustrates how it may be used in the context of an assign activity:

```
<assign>
  <copy>
    <from>ode:process-property("auctionEpr")</from>
    <to partnerLink="partnerLink"/>
  </copy>
</assign>
```

where, the property called "epr" is defined in the corresponding deploy.xml as follows:

```
<deploy xmlns="http://www.apache.org/ode/schemas/dd/2007/03"
                   xmlns:tns="http://ode/bpel/process">
   <process name="tns:negotiate">
       <property name="auctionEpr">
           <sref:service-ref
                xmlns:sref=" http://docs.oasis-open.org/wsbpel/2.0/serviceref"
                xmlns:addr="http://example.com/addressing"
                xmlns:as="http://example.com/auction/wsdl/auctionService/">
                <addr:EndpointReference>
                    <addr:Address>http://example.com/auction/RegistrationService&lt;/addr:Address>
                    <addr:ServiceName>as:RegistrationService</addr:ServiceName>
                </addr:EndpointReference>
            </sref:service-ref>
        </property>...
    </process>
</deploy>
```

> [!NOTE]
> <a id="extensions-xpath-extensions--release-information"></a>

>
> > [!NOTE]
> > #### Release Information
>
> This function will be available in the 1.3 or higher version of ODE.
<a id="extensions-xpath-extensions--predefined-process-properties"></a>

#### Predefined Process Properties

<a id="extensions-xpath-extensions--localhost-info-name-and-ip-address"></a>

##### Localhost info (name and IP address)

```
<bpws:assign>
  <bpws:copy>
    <bpws:from>ode:process-property('ode.localhost.name')</bpws:from>
    <bpws:to>$output.payload</bpws:to>
  </bpws:copy>
</bpws:assign>

<bpws:assign>
  <bpws:copy>
    <bpws:from>ode:process-property('ode.localhost.address')</bpws:from>
    <bpws:to>$output.payload</bpws:to>
  </bpws:copy>
</bpws:assign>
```

<a id="extensions-xpath-extensions--extension-variables"></a>

### Extension Variables

<a id="extensions-xpath-extensions--instance-id"></a>

#### Instance Id

```
$ode:pid
```

<a id="extensions-xpath-extensions--process-qname"></a>

#### Process QName

```
$ode:processQName
```

<a id="extensions-xpath-extensions--currenteventdatetime"></a>

#### CurrentEventDateTime

This is equivalent to current-dateTime() XPath function, which works with instance replayer.

```
$ode:currentEventDateTime
```

> [!NOTE]
> <a id="extensions-xpath-extensions--release-information-2"></a>

>
> > [!NOTE]
> > #### Release Information
>
> 1.3.4 or higher

---

<a id="required-third-party-libraries"></a>

<!-- source_url: https://ode.apache.org/required-third-party-libraries.html -->

<!-- page_index: 54 -->

# Required Third-Party Libraries

ODE builds on a number of third-party open source libraries, although the design goal of embeddability means that the dependencies have been purposefully limited. The source module contains all third-party open source dependencies, one per subdirectory, along with text files that describe the licensing terms of each library.

TODO: rework this page

---

<a id="sendsoap-command"></a>

<!-- source_url: https://ode.apache.org/sendsoap-command.html -->

<!-- page_index: 55 -->

<a id="sendsoap-command--overview"></a>

## Overview

The `sendsoap` command uses a lightweight HTTP client to send SOAP messages via POST.

<a id="sendsoap-command--synopsis"></a>

## Synopsis

```
sendsoap [-q|-v|-vv] [-o outfile] url -
sendsoap -h
```

<a id="sendsoap-command--description"></a>

## Description

The `sendsoap` command uses a lightweight HTTP client to send SOAP messages via POST using either a file or standard in as the source for the message. The command is useful for testing HTTP endpoints in ODE or external HTTP services that ODE will interact with, as `sendsoap` uses the same Axis2 client as the Axis2 Integration Layer.

<a id="sendsoap-command--options"></a>

## Options

| `url` | the HTTP URL to post the message to. |
| --- | --- |
| `file` | a file containing the message to post. |
| `-` | read the message data from standard in instead of a file. |
| `-o file` | sets a file to write the output to; otherwise, output is sent to the console. |
| `-q\|-v\|-vv` | adjust the verbosity of logging output. |
| `-h` | prints a synopsis to the console and exits. |

---

<a id="ws-bpel-20"></a>

<!-- source_url: https://ode.apache.org/ws-bpel-20.html -->

<!-- page_index: 56 -->

<a id="ws-bpel-20--overview"></a>

## Overview

**WS-BPEL 2.0** - the first official version of the BPEL specification released by the [OASIS](http://www.oasis-open.org) [technical committee](http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=wsbpel).

The specification has been finalized and can be found [here](http://docs.oasis-open.org/wsbpel/2.0/OS/wsbpel-v2.0-OS.html). To learn more about it check the webinars produced by the technical committee:

- http://www.oasis-open.org/events/webinars/

The presentation documents are also available:

- [Business value part 1](http://www.oasis-open.org/committees/download.php/23070/The%20Business%20Value%20of%20WS-BPEL%20for%20Business%20Analysts%20and%20Managers%20%28Frank%20Leymann%29%20-%20Part%201.pdf)
- [Business value part 2](http://www.oasis-open.org/committees/download.php/23069/The%20Business%20Value%20of%20WS-BPEL%20for%20Business%20Analysts%20and%20Managers%20-%20Part%202%20%28Chris%20Keller%29.pdf)
- [Technical overview part 1](http://www.oasis-open.org/committees/download.php/23068/WS-BPEL%20Technical%20Overview%20for%20Developers%20and%20Architects%20-%20Part%201%20%28Frank%20Ryan%29.pdf)
- [Technical overview part 2](http://www.oasis-open.org/committees/download.php/23067/WS-BPEL%20Technical%20Overview%20for%20Developers%20and%20Architects%20-%20Part%202%20%28Dieter%20Koenig%29.pdf)
- [Technical overview part 3](http://www.oasis-open.org/committees/download.php/23066/WS-BPEL%20Technical%20Overview%20for%20Developers%20and%20Architects%20-%20Part%203%20%28Charlton%20Barreto%29.pdf)

<a id="ws-bpel-20--odes-support-of-the-specification"></a>
<a id="ws-bpel-20--ode-s-support-of-the-specification"></a>

## ODE's support of the specification

ODE's support of the specification is outlined on the [WS-BPEL 2.0 Specification Compliance](#ws-bpel-20-specification-compliance) page.

<a id="ws-bpel-20--odes-bpel-extensions"></a>
<a id="ws-bpel-20--ode-s-bpel-extensions"></a>

## ODE's BPEL extensions

ODE also supports [a few extensions](#extensions) to WS-BPEL in the areas we thought necessary.

---
