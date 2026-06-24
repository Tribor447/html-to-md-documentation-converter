# Getting Started ¶

## Navigation

- [Home](#index)
- [Documentation](#documentation)
- [Source](#source)
- [Download](#download)
- [Community](#community)
- Misc
  - [Contact](#misc-contact)
  - [Legal](#misc-legal)
- Other pages
  - [OpenWebBeans FAQ ¶](#faq)
  - [OpenWebBeans Configuration ¶](#owbconfig)

## Content

<a id="index"></a>

<!-- source_url: https://openwebbeans.apache.org/index.html -->

<!-- page_index: 1 -->

# Apache OpenWebBeans

![owb_logo](assets/images/logo_7c4c9d6af179f7a3.png)

Apache OpenWebBeans delivers an implementation of the
[Contexts and Dependency injection for Jakarta EE](https://projects.eclipse.org/projects/ee4j.cdi/releases/4.1) (CDI) 4.1 Specification.
OpenWebBeans is TCK compliant and the latest version works on Java SE 17 or later.

Apache OpenWebBeans is

- Fast - we aggressively use caches internally and deliver great performance
- Modular - OpenWebBeans Core is purely JavaSE, additional EE functionality gets added via 'Modules'
- Industry Proven - Many projects use OpenWebBeans in production.
- Community Oriented - Please visit our mailing list and we will help you moving your project forward.

<a id="index--getting-started-with-cdi"></a>

## Getting Started with CDI

OpenWebBeans is packaged as modules which get activated by simply dropping them into the classpath.
The below link will take you to a step-by-step guide and get you started in no time!

[View details »](#documentation--module-overview)

<a id="index--meecrowave-server"></a>

## Meecrowave Server

Apache Meecrowave is a Microprofile Server based on Apache OpenWebBeans, Tomcat, CXF and Johnzon
In other words it contains all you need to run a JavaEE based Microservice from the command line - and all that in only 9 MB!

[View details »](https://openwebbeans.apache.org/meecrowave/index.html)

---

<a id="index--latest-news"></a>

## Latest News

<a id="index--apache-openwebbeans-4.1.0-has-been-released"></a>

#### [Apache OpenWebBeans-4.1.0 has been released](https://openwebbeans.apache.org/news.html)

The Apache OpenWebBeans Team is proud to announce the release of Apache OpenWebBeans-4.1.0.
This implements the CDI-4.1 specification

<a id="index--apache-openwebbeans-4.0.3-has-been-released"></a>

#### [Apache OpenWebBeans-4.0.3 has been released](https://openwebbeans.apache.org/news.html)

The Apache OpenWebBeans Team is proud to announce the release of Apache OpenWebBeans-4.0.3.

---

<a id="documentation"></a>

<!-- source_url: https://openwebbeans.apache.org/documentation.html -->

<!-- page_index: 2 -->

<a id="documentation--getting-started"></a>

# Getting Started

If you are completely new to CDI then you might want to take a look at the following introductory articles

- [How CDI works](https://openwebbeans.apache.org/cdi_explained.html)
- [Adding OpenWebBeans to your JavaSE project](https://openwebbeans.apache.org/owbsetup_se.html)
- [Adding OpenWebBeans to Apache Tomcat](https://openwebbeans.apache.org/owbsetup_tomcat.html)
- [Adding OpenWebBeans to your Servlet Container project](https://openwebbeans.apache.org/owbsetup_ee.html)
- [OpenWebBeans as part of JavaEE Containers](https://openwebbeans.apache.org/owb-eecontainers.html)
- [OpenWebBeans configuration](#owbconfig)
- [FAQ](#faq)

There are several Application Containers which come with Apache OpenWebBeans as their core CDI container

- [Apache Meecrowave](https://openwebbeans.apache.org/meecrowave/)
- [Apache TomEE](https://tomee.apache.org)

<a id="documentation--openwebbeans-plugin-structure"></a>

# OpenWebBeans Plugin Structure

OpenWebBeans consists of a core system which heavily uses SPIs (Service Provider Interfaces)
to extend it's functionality. The core system itself is purely JavaSE based
and does not need any further dependency. All special JavaEE features get added via
separate plugins.

<a id="documentation--system-core"></a>

### System Core

- [OpenWebBeans Core](https://openwebbeans.apache.org/openwebbeans-impl.html)
- [SPI definition](https://openwebbeans.apache.org/openwebbeans-spi.html)

<a id="documentation--commonly-used-plugins"></a>

### Commonly used Plugins

- [Web plugin](https://openwebbeans.apache.org/openwebbeans-web.html)
- [EL plugins 1.0 & 2.2](https://openwebbeans.apache.org/openwebbeans-el.html)
- [JSF plugins 1.2 & 2.x](https://openwebbeans.apache.org/openwebbeans-jsf.html)
- [Apache Tomcat plugins](https://openwebbeans.apache.org/openwebbeans-tomcat.html)

<a id="documentation--technical-integration-plugins"></a>

### Technical Integration Plugins

- [EE Common plugin](https://openwebbeans.apache.org/openwebbeans-ee-common.html)
- [Java EE plugin](https://openwebbeans.apache.org/openwebbeans-ee.html)
- [EJB plugin](https://openwebbeans.apache.org/openwebbeans-ejb.html)
- [EE Resource plugin](https://openwebbeans.apache.org/openwebbeans-resource.html)
- [JMS plugin](https://openwebbeans.apache.org/openwebbeans-jms.html)
- [OSGi plugin](https://openwebbeans.apache.org/openwebbeans-osgi.html)

<a id="documentation--testing-strategies-for-cdi-projects"></a>

# Testing Strategies for CDI Projects

- [JUnit5 integration](https://openwebbeans.apache.org/openwebbeans-junit5.html)
- [General guidelines for testing](https://openwebbeans.apache.org/testing_general.html)
- [Deltaspike Test-Control](https://openwebbeans.apache.org/testing_test-control.html)
- [Apache DeltaSpike CdiCtrl](https://openwebbeans.apache.org/testing_cdictrl.html)
- [JBoss Arquillian](https://openwebbeans.apache.org/testing_arquillian.html)
- [Writing unit tests for OWB itself](https://openwebbeans.apache.org/owbinternalunittests.html)

---

<a id="source"></a>

<!-- source_url: https://openwebbeans.apache.org/source.html -->

<!-- page_index: 3 -->

<a id="source--getting-involved"></a>

# Getting Involved

We are always looking for new contributors to the project.

Pleaes see our [Community Section](#community) for more information.

<a id="source--cannonical-source-repository"></a>

# Cannonical Source Repository

The sources of Apache OpenWebBeans are maintained in the Apache Software Foundation gitbox repository.
This is the repository where all committers work on.
It gets mirrored to GitHub in both directions.
That means you can either push to Apache GitBox or GitHub.

The master branch currently contains our implementation of the CDI-2.0 specification and is considered production ready.

The sources can be checked out read only with the following command:

```

$> git clone https://github.com/apache/openwebbeans
```

or

```

$> git clone https://gitbox.apache.org/repos/asf/openwebbeans.git
```

<a id="source--maintenance-releases-targetting-older-cdi-specifications"></a>

## Maintenance releases targetting older CDI specifications

<a id="source--cdi-12-openwebbeans-20x"></a>
<a id="source--cdi-1.2-openwebbeans-2.0.x"></a>

### CDI-1.2 - OpenWebBeans-2.0.x

For checking out sources of the stable CDI-2.0 version of OpenWebBeans, please use the owb\_2.0.x branch from here:

```

$> git clone https://github.com/apache/openwebbeans
$> git checkout owb_2.0.x
```

<a id="source--cdi-12-openwebbeans-17x"></a>
<a id="source--cdi-1.2-openwebbeans-1.7.x"></a>

### CDI-1.2 - OpenWebBeans-1.7.x

For checking out sources of the stable CDI-1.2 version of OpenWebBeans, please use the owb\_1.7.x branch from here:

```

$> git clone https://github.com/apache/openwebbeans
$> git checkout owb_1.7.x
```

<a id="source--cdi-10-openwebbeans-12x"></a>
<a id="source--cdi-1.0-openwebbeans-1.2.x"></a>

### CDI-1.0 - OpenWebBeans-1.2.x

For checking out sources of the stable CDI-1.0 version of OpenWebBeans, please use the owb\_1.2.x branch from here:

```

$> git clone https://github.com/apache/openwebbeans
$> git checkout owb_1.2.x
```

<a id="source--building-openwebbeans"></a>

# Building OpenWebBeans

Apache OpenWebBeans can be built by using Apache Maven. Just go into the source directory and execute

```

mvn clean install
```

The following maven profiles exist in our build to trigger additional build steps and configuration:

- tck - for executing the CDI (JSR-299, JSR-346 resp JSR-365) standalone TCK
- jsr330-tck - for executing the JSR-330 'atinject' TCK

In master they are all activated by default and run every time you build OpenWebBeans.

For older OpenWebBeans versions you might enable them manually.

```

mvn clean install -Ptck -Pjsr330-tck -Pdoc
```

---

<a id="download"></a>

<!-- source_url: https://openwebbeans.apache.org/download.html -->

<!-- page_index: 4 -->

<a id="download--apache-openwebbeans-releases"></a>

# Apache OpenWebBeans Releases

This page contains download links to the latest Apache OpenWebBeans releases.

All maven artifacts are available in the Maven.Central repository with the groupId `org.apache.openwebbeans`. The dependencies you can use are listed at the bottom of this page: [Maven Dependencies](#download--maven-dep).

<a id="download--keys-for-verifying-apache-releases"></a>

## KEYS for verifying Apache releases

The GPG keys in the [OpenWebBeans KEYS file](https://www.apache.org/dist/openwebbeans/KEYS) to validate our releases.
Read more about [How to verify downloaded files](https://www.apache.org/info/verification.html)

---

<a id="download--owb-40x"></a>
<a id="download--owb-4.0.x"></a>

## OWB-4.0.x

OWB-4.0.x implements the CDI-4.0 (Jakarta CDI) specification.
It requires Java11 or higher.

<a id="download--source"></a>

#### Source

The source distribution contains all OpenWebBeans source code.
Binaries are available via the Apache Maven Central repository.

- [openwebbeans-4.0.3-source-release.zip](https://www.apache.org/dyn/closer.lua/openwebbeans/4.0.3/openwebbeans-4.0.3-source-release.zip)
- [openwebbeans-4.0.3-source-release.zip.sha512](https://www.apache.org/dist/openwebbeans/4.0.3/openwebbeans-4.0.3-source-release.zip.sha512)
- [openwebbeans-4.0.3-source-release.zip.asc](https://www.apache.org/dist/openwebbeans/4.0.3/openwebbeans-4.0.3-source-release.zip.asc)

---

<a id="download--owb-20x"></a>
<a id="download--owb-2.0.x"></a>

## OWB-2.0.x

OWB-2.0.x implements the CDI-2.0 (JSR-365) specification.
It uses a shaded version of ASM-8 (Java11 support) for building our proxies and requires JavaSE 8 as minimum version.

<a id="download--source_1"></a>
<a id="download--source-2"></a>

#### Source

The source distribution contains all OpenWebBeans source code.
Binaries are available via the Apache Maven Central repository.

- [openwebbeans-2.0.27-source-release.zip](https://www.apache.org/dyn/closer.lua/openwebbeans/2.0.27/openwebbeans-2.0.27-source-release.zip)
- [openwebbeans-2.0.27-source-release.zip.sha512](https://www.apache.org/dist/openwebbeans/2.0.27/openwebbeans-2.0.27-source-release.zip.sha512)
- [openwebbeans-2.0.27-source-release.zip.asc](https://www.apache.org/dist/openwebbeans/2.0.27/openwebbeans-2.0.27-source-release.zip.asc)

---

<a id="download--owb-17x"></a>
<a id="download--owb-1.7.x"></a>

## OWB-1.7.x

OWB-1.7.x implements the full CDI-1.2 specification.
It uses a shaded version of ASM-5 for building our proxies and needs JavaSE 7 as minimum version.

<a id="download--source_2"></a>
<a id="download--source-3"></a>

#### Source

Should you want to build any of the above binaries, this source bundle is the right one and covers them all.

- [openwebbeans-1.7.6-source-release.zip](https://www.apache.org/dyn/closer.lua/openwebbeans/1.7.6/openwebbeans-1.7.6-source-release.zip)
- [openwebbeans-1.7.6-source-release.zip.sha1](https://www.apache.org/dist/openwebbeans/1.7.6/openwebbeans-1.7.6-source-release.zip.sha1)
- [openwebbeans-1.7.6-source-release.zip.asc](https://www.apache.org/dist/openwebbeans/1.7.6/openwebbeans-1.7.6-source-release.zip.asc)

---

<a id="download--owb-12x"></a>
<a id="download--owb-1.2.x"></a>

## OWB-1.2.x

OWB-1.2.x implements the CDI-1.0 specification and internally already CDI-1.1.
It uses a shaded version of ASM-5 for building our proxies and needs JavaSE 5 as minimum version.

<a id="download--binaries"></a>

#### Binaries

The binary distribution contains all OpenWebBeans modules.

- [openwebbeans-distribution-1.2.8-binary.zip](https://www.apache.org/dyn/closer.lua/openwebbeans/1.2.8/openwebbeans-distribution-1.2.8-binary.zip)
- [openwebbeans-distribution-1.2.8-binary.zip.sha1](https://www.apache.org/dist/openwebbeans/1.2.8/openwebbeans-distribution-1.2.8-binary.zip.sha1)
- [openwebbeans-distribution-1.2.8-binary.zip.asc](https://www.apache.org/dist/openwebbeans/1.2.8/openwebbeans-distribution-1.2.8-binary.zip.asc)
- [openwebbeans-distribution-1.2.8-binary.tar.gz](https://www.apache.org/dyn/closer.lua/openwebbeans/1.2.8/openwebbeans-distribution-1.2.8-binary.tar.gz)
- [openwebbeans-distribution-1.2.8-binary.tar.gz.sha1](https://www.apache.org/dist/openwebbeans/1.2.8/openwebbeans-distribution-1.2.8-binary.tar.gz.sha1)
- [openwebbeans-distribution-1.2.8-binary.tar.gz.asc](https://www.apache.org/dist/openwebbeans/1.2.8/openwebbeans-distribution-1.2.8-binary.tar.gz.asc)

**Hint:** OpenWeBeans has dependencies to several other jars and just adding our jars manually would lead to ClassNotFoundException if you choose not to use maven.
The jars you need depends on what modules you include.
They are all contained in the binary distribution.
We will try to add complete lists of this in the future, meanwhile please ask on the list or maybe look at the pom.xml for the modules you want to use.

<a id="download--source_3"></a>
<a id="download--source-4"></a>

#### Source

Should you want to build any of the above binaries, this source bundle is the right one covers them all.

- [openwebbeans-1.2.8-source-release.zip](https://www.apache.org/dyn/closer.lua/openwebbeans/1.2.8/openwebbeans-1.2.8-source-release.zip)
- [openwebbeans-1.2.8-source-release.zip.sha1](https://www.apache.org/dist/openwebbeans/1.2.8/openwebbeans-1.2.8-source-release.zip.sha1)
- [openwebbeans-1.2.8-source-release.zip.asc](https://www.apache.org/dist/openwebbeans/1.2.8/openwebbeans-1.2.8-source-release.zip.asc)

---

<a id="download--openwebbeans-archives"></a>

## OpenWebBeans Archives

Older versions of Apache OpenWebBeans can be found in our [archives](https://archive.apache.org/dist/openwebbeans/)

---

<a id="download--maven-dep"></a>
<a id="download--maven-dependencies"></a>

### Maven Dependencies

<a id="download--apis-version"></a>
<a id="download--apis-for-owb-2.0.x"></a>

#### APIs for OWB-2.0.x

```
<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-atinject_1.0_spec</artifactId>
    <version>1.2</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-jcdi_2.0_spec</artifactId>
    <version>1.2</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-interceptor_1.2_spec</artifactId>
    <version>1.2</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-annotation_1.3_spec</artifactId>
    <version>1.3</version>
</dependency>
```

Note that you should set the seope of those dependencies to either `provided` or `compile` depending on whether your environment already provide them or not.

<a id="download--apis-version12"></a>
<a id="download--apis-for-owb-1.7.x"></a>

#### APIs for OWB-1.7.x

```
<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-atinject_1.0_spec</artifactId>
    <version>1.0</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-jcdi_1.1_spec</artifactId>
    <version>1.0</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-interceptor_1.2_spec</artifactId>
    <version>1.0</version>
</dependency>

<dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-annotation_1.2_spec</artifactId>
    <version>1.0</version>
</dependency>
```

<a id="download--required-version"></a>
<a id="download--required"></a>

#### Required

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-spi</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>

<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-impl</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

<a id="download--plugins-version"></a>
<a id="download--plugins"></a>

#### Plugins

**Web Module** (Required for web-apps)

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-web</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

**JSF 2.X Module**

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-jsf</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

**EL 2.2 Module**

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-el22</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

**Tomcat 7 Module**

(also works for Tomcat-8, Tomcat-8.5 and Tomcat-9)

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-tomcat7</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

**JMS Module**

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-jms</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

**Arquillian Module**

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-arquillian</artifactId>
    <version>${owb.version}</version>
    <scope>compile</scope>
</dependency>
```

---

<a id="community"></a>

<!-- source_url: https://openwebbeans.apache.org/community.html -->

<!-- page_index: 5 -->

<a id="community--users"></a>

# Users

If you are a new user and you would like to start using Apache OpenWebBeans, you can have a look at the [Documentation](#documentation) and
[subscribe](mailto:user-subscribe@openwebbeans.apache.org)
our [mailing list for user](mailto:user@openwebbeans.apache.org).

Furthermore, you can check our [mail-archives](#community--mailing-lists).

Before you file a ticket in our [Issue Tracker](https://issues.apache.org/jira/browse/OWB), please ask on the mailing list
if it's a known issue in case of a bug or if there is an ongoing discussion in case of a feature.

You are very welcome to follow our twitter account [@Apache OpenWebBeansTeam](https://twitter.com/OwbTeam)
and spread the word of Apache OpenWebBeans with Tweets, Blog-Entries,...

<a id="community--cdi-40-jakartaee-10"></a>
<a id="community--cdi-4.0-jakartaee-10"></a>

# CDI-4.0 (JakartaEE 10)

The work on a implementing the [Jakarta CDI-4.0](https://projects.eclipse.org/projects/ee4j.cdi/releases/4.0)
specification is finished.
We are now doing minor enhancements and bug fixing in our main branch.

<a id="community--getting-involved"></a>

# Getting Involved

Everybody is welcome to get involved with our community. You can find general information at
<https://apache.org/foundation/getinvolved.html>
and <http://apache.org/foundation/how-it-works.html>.
The following sections provides some details about the different levels of getting involved.

<a id="community--contributors"></a>

## Contributors

Before you get a committer you have to contribute to our effort. E.g. you can help users, participate in
discussions on the dev list, submit patches,... . Therefore, it's essential to file a/n
[(I)CLA](https://www.apache.org/licenses/icla.txt) or [CLA](https://www.apache.org/licenses/cla-corporate.txt)
and send it to secretary at apache dot org (or fax it) as early as possible.

If you would like to submit a patch through Jira, just attach your patch to a created JIRA issue.

<a id="community--committers"></a>

## Committers

Before you read this section, please ensure that you have read the contributor section.
All of you are welcome to join our development effort. [Subscribe](mailto:dev-subscribe@openwebbeans.apache.org)
our [mailing list for developers](mailto:dev@openwebbeans.apache.org) and start contributing and help users.

Optionally [subscribe](mailto:commits-subscribe@openwebbeans.apache.org) our [mailing list for commits](mailto:commits@openwebbeans.apache.org).

Furthermore, you can check our [mail-archives](#community--mailing-lists).

Further details are available at <https://www.apache.org/dev/>.

If you are running an Apache OpenWebBeans release then please make sure to read our [Release Checklist](https://openwebbeans.apache.org/release-checklist.html)

<a id="community--mailing-lists"></a>

# Mailing lists

| List (Address) | Subscribe | Unsubscribe | Archive | Mirrors |  |
| --- | --- | --- | --- | --- | --- |
| [User List](mailto:user@openwebbeans.apache.org) | [Subscribe](mailto:user-subscribe@openwebbeans.apache.org) | [Unsubscribe](mailto:user-unsubscribe@openwebbeans.apache.org) | [Archive](https://mail-archives.apache.org/mod_mbox/openwebbeans-user/) | [MarkMail](https://markmail.org/search/?q=list%3Aorg.apache.openwebbeans.user+order%3Adate-backward) |  |
| [Developer List](mailto:dev@openwebbeans.apache.org) | [Subscribe](mailto:dev-subscribe@openwebbeans.apache.org) | [Unsubscribe](mailto:dev-unsubscribe@openwebbeans.apache.org) | [Archive](https://mail-archives.apache.org/mod_mbox/openwebbeans-dev/) | [MarkMail](https://markmail.org/search/?q=list%3Aorg.apache.openwebbeans.dev+order%3Adate-backward) |  |
| [Committer List](mailto:commits@openwebbeans.apache.org) | [Subscribe](mailto:commits-subscribe@openwebbeans.apache.org) | [Unsubscribe](mailto:commits-unsubscribe@openwebbeans.apache.org) | [Archive](https://mail-archives.apache.org/mod_mbox/openwebbeans-commits/) | [MarkMail](https://markmail.org/search/?q=list%3Aorg.apache.openwebbeans.commit+order%3Adate-backward) |  |

<a id="community--issue-tracking"></a>

# Issue Tracking

Bug reports and feature requests are handled via JIRA at

[OpenWebBeans JIRA](https://issues.apache.org/jira/browse/OWB).

<a id="community--spread-the-word"></a>

# Spread the word

You are very welcome e.g. to write blog entries, tweet (#OwbTeam) about the project
or just follow our twitter account ([@OwbTeam](https://twitter.com/OwbTeam)), ...

```
//with the irssi command-line client:
$ irssi

> /connect irc.freenode.net
> /join #openwebbeans
```

<a id="community--original-project-proposal"></a>

# Original Project Proposal

This is the original project proposal for the incubation of the Apache OpenWebBeans Project sent to the Apache Incubator by Gurkan Erdogdu. Although old (September 2009), it is still worth reading as the original vision of the project. It's a piece of history.

[OpenWebBeans Original Project Proposal](https://wiki.apache.org/incubator/OpenWebBeansProposal).

---

<a id="misc-contact"></a>

<!-- source_url: https://openwebbeans.apache.org/misc/contact.html -->

<!-- page_index: 6 -->

<a id="misc-contact--product-support"></a>

## Product Support

If you have questions or comments about the software or documentation on this site, please subscribe to the appropriate [mailing list](#community).

<a id="misc-contact--security-issues"></a>

## Security Issues

If you would like to report a security issues with Apache OpenWebBeans, please contact [security.AT.apache.DOT.org](mailto:security.AT.apache.DOT.org).
Only security issues should be sent to this address.

<a id="misc-contact--general-apache-issues"></a>

## General Apache Issues

The OpenWebBeans Project is an effort of the [Apache Software Foundation](https://www.apache.org).
The address for general ASF correspondence and licensing questions is:

[apache.AT.apache.DOT.org](mailto:apache.AT.apache.DOT.org)

You can find more contact information for the Apache Software Foundation on [the contact page of the main Apache site](https://www.apache.org/foundation/contact.html).

You may also use [Apache Site Search](https://search.apache.org/) to scan all the Apache sites at once.

---

<a id="misc-legal"></a>

<!-- source_url: https://openwebbeans.apache.org/misc/legal.html -->

<!-- page_index: 7 -->

<a id="misc-legal--legal-stuff-they-make-us-say"></a>

## Legal Stuff They Make Us Say

All material on this website is Copyright © 2016, The Apache Software Foundation

Sun, Sun Microsystems, Solaris, Java and JavaServer Pages are trademarks or registered trademarks of Oracle Corporation.
UNIX is a registered trademark in the United States and other countries, exclusively licensed through 'The Open Group'.
Microsoft, Windows, WindowsNT, and Win32 are registered trademarks of Microsoft Corporation.
Linux is a registered trademark of Linus Torvalds.
All other product names mentioned herein and throughout the entire web site are trademarks of their respective owners.

<a id="misc-legal--the-apache-license"></a>

## The Apache License

All software produced by The Apache Software Foundation or any of its projects or subjects is licensed according to the terms of
[Apache License, Version 2.0 (current)](https://www.apache.org/licenses/LICENSE-2.0).

<a id="misc-legal--trademarks"></a>

## Trademarks

"Apache OpenWebBeans" and "OpenWebBeans" are trademarks of the Apache Software Foundation.
Use of these trademarks is subject to the terms of section 6 of
[Apache License, Version 2.0 (current)](https://www.apache.org/licenses/LICENSE-2.0).

If you create a product that uses Apache OpenWebBeans software or provides additional functionality to that software then:

- When referring to Apache OpenWebBeans software, please use the full name of "Apache OpenWebBeans" for at least the first reference on any web page, help file or similar.
  Subsequent references may refer to "OpenWebBeans".
- You may not use the OpenWebBeans logo without the permission of the Apache OpenWebBeans PMC.
- If you use the words "OpenWebBeans" or "Apache" in your product name then you must call your product "... for Apache OpenWebBeans".
  No other form of product name that includes "OpenWebBeans" or "Apache" is permitted.

---

<a id="faq"></a>

<!-- source_url: https://openwebbeans.apache.org/faq.html -->

<!-- page_index: 8 -->

<a id="faq--openwebbeans-faq"></a>

# OpenWebBeans FAQ

- [Does OWB differ from the CDI-2.0 specification](#faq--does-owb-differ-from-the-cdi-20-specification)
- what is the default EL version used in OWB
- how can I provide own plugins if there is a new spec part (e.g EL-3.0) I like to support
- How can I contribute to OpenWebBeans
- I found what could be a bug, how do I proceed

<a id="faq--does-owb-differ-from-the-cdi-20-specification"></a>
<a id="faq--does-owb-differ-from-the-cdi-2.0-specification"></a>

### Does OWB differ from the CDI-2.0 specification

---

<a id="owbconfig"></a>

<!-- source_url: https://openwebbeans.apache.org/owbconfig.html -->

<!-- page_index: 9 -->

<a id="owbconfig--openwebbeans-configuration"></a>

# OpenWebBeans Configuration

Internal configuration of OpenWebBeans can be done via: src/main/resources/META-INF/openwebbeans/openwebbeans.properties

All those files contain at single property `configuration.ordinal` which defines their
'importance'. Any setting from a property file with a higher configuration.ordinal will
overwrite settings from one with a lower configuration.ordinal. The internally used
configuration.ordinal values range from 1 to 100. The default value is 100.

This trick allows us to split OpenWebBeans in different modules which automatically change the container
configuration if you put that jar on the classpath.

For overriding the default configuration with own settings simply put a `META-INF/openwebbeans/openwebbeans.properties`
file into your projects classpath (e.g. into a jar) and either use a `configuration.ordinal` higher than 100 or leave
it empty to get the default value of 100.

If you use OpenWebBeans as part of another project then you can assume that most of the values got tweaked
by the integration regarding to the specific needs.

<a id="owbconfig--configure-spi-implementations"></a>

## Configure SPI implementations

OpenWebBeans provide a set of Service Provider Interfaces and multiple different implementations a user can choose from.

You can choose the implementations you like to use for your situation by configuring them in
`META-INF/openwebbeans/openwebbeans.properties`.

Read more about our SPIs in [OpenWebBeans SPI](https://openwebbeans.apache.org/openwebbeans-spi.html)

<a id="owbconfig--other-configurable-values"></a>

## Other Configurable Values

The following configuration values can get tweaked to get tailor OWB to your specific needs.

Boolean values can either be `true`, or `TRUE`, or `false`, or `FALSE`.

- `org.apache.webbeans.forceNoCheckedExceptions`

  Lifycycle methods like `javax.annotation.PostConstruct` and
  `javax.annotation.PreDestroy` must not define a checked Exception
  regarding to the spec. But this is often unnecessary restrictive so we
  allow to disable this check application wide.

  Defaults to `true`.
- `org.apache.webbeans.spi.deployer.useEjbMetaDataDiscoveryService`

  Whether to perform EJB discovery or not.

  Defaults to `false`. In TomEE this gets automatically enabled.
- `org.apache.webbeans.application.jsp`

  If enabled, we automatically try to register the ELResolver in the JSP engine.
  Enable this setting if you like to access `@Named` CDI beans in JSP Expression Language.

  Default is `false`
- `org.apache.webbeans.application.supportsConversation`

  Enable support for the CDI `@ConversationScoped`.

  Disabled by default in JavaSE, but enabled by default when adding the webbeans-web module (Servlets)
- `org.apache.webbeans.application.supportsProducerInterception`

  Define if a CDI interceptor can be used on a producer method or field.
  In OpenWebBeans you can use a `@StereoType` with an Interceptor to enable
  an Interceptor on the instance returned from a Producer Method or Producer Field.

  Enabled by default.
- `org.apache.webbeans.scanExclusionPaths`

  A list of known JARs/paths which should not be scanned for beans.
  This is only used by the default ScannerService implementation.

  Please refer to the openwebbeans.properties file in ``webbeans-impl.jar``
- `org.apache.webbeans.scanBeansXmlOnly`

  Flag which indicates that only jars with an explicit META-INF/beans.xml marker file shall get parsed.
  This basically switches OWB back to the CDI-1.0 scanning behaviour and might speed up the boot process.

  Default is false
- `org.apache.webbeans.ignoredDecoratorInterfaces`

  A comma-separated list of fully qualified class names that should be ignored
  when determining if a decorator matches its delegate.

  Default is an empty list
- `org.apache.webbeans.web.eagerSessionInitialisation`

  By default we do \_not\_ force session creation in our WebBeansConfigurationListener. We only create the
  Session if we really need the SessionContext. E.g. when we create a Contextual Instance in it.
  Sometimes this creates a problem as the HttpSession can only be created BEFORE anything got written back
  to the client.
  With this configuration you can choose between 3 settings
  - "true" the Session will always eagerly be created at the begin of a request
  - "false" the Session will never eagerly be created but only lazily when the first @SessionScoped bean gets used
  - any other value will be interpreted as Java regular expression for request URIs which need eager Session initialization

  Defaults to false. A session will only get created if a `@SessionScoped` bean gets accessed for the first time.
- `org.apache.webbeans.generator.javaVersion`

  The Java Version to use for the generated proxy classes.
  If `auto` then we will pick the version of the current JVM.
  *Attention:* If you like to use Java8 Lambdas in CDI bean method signatures then you need to
  switch to either `auto` or `1.8`!

  The default is set to `1.6` as some tools in jetty/tomcat/etc still
  cannot properly handle Java8 (mostly due to older Eclipse JDT versions).
- `javax.enterprise.inject.allowProxying.classes`

  Environment property which comma separated list of classes which
  should NOT fail with an UnproxyableResolutionException.
  You only have to configure additional classes in your openwebbeans.properties file.
  All the configured values get added together into a big List.

  By default we allow the following classes: `java.util.HashMap` and `java.util.Calendar`

<a id="owbconfig--proxy-mapping"></a>

## Proxy Mapping

OpenWebBeans enables the user to define the NormalScope handlers for specific scopes.

NormalScope handlers are used by OpenWebBeans' proxies to resolve the 'Contextual Instance'.
E.g. for a `@SessionScoped User` injected into some other class, this is exactly the piece of code
which goes into the current Http Session and gets the User instance from there.
This class must extend `org.apache.webbeans.intercept.NormalScopedBeanInterceptorHandler` and overwrite the
`Object getContextualInstance()` method.

This allows for more aggressive caching than with the generic `NormalScopedBeanInterceptorHandler` which is the default.
The default NormalScope handler will look up the Contextual Instance in the respective Context for each and every
method invocation on the proxy.

But sometimes we can much more aggressively cache the instances.

E.g. for `@ApplicationScoped` beans we can keep the contextual instance inside the proxy, making it as fast as a pure Java instance - but still gaining all the benefits of CDI!

For `@RequestScoped` and `@SessionScoped` we can use a NormalScope handler which caches the Contextual Instance in a ThreadLocal.

By default the following NormalScope handlers get used:

```

org.apache.webbeans.proxy.mapping.javax.enterprise.context.ApplicationScoped
    =org.apache.webbeans.intercept.ApplicationScopedBeanInterceptorHandler
org.apache.webbeans.proxy.mapping.javax.enterprise.context.RequestScoped
    =org.apache.webbeans.intercept.RequestScopedBeanInterceptorHandler
org.apache.webbeans.proxy.mapping.javax.enterprise.context.SessionScoped
    =org.apache.webbeans.intercept.SessionScopedBeanInterceptorHandler
```

As you can see we use a prefix `org.apache.webbeans.proxy.mapping.` followed by the fully qualified scope name as key.
The value represents the fully qualified name of the handler class.

If you have a custom scope which spans a Request or longer then you can simply reuse the `RequestScopedBeanInterceptorHandler` as shown in the following example:

```

org.apache.webbeans.proxy.mapping.org.apache.deltaspike.core.api.scope.ViewAccessScoped
    =org.apache.webbeans.intercept.RequestScopedBeanInterceptorHandler
```

<a id="owbconfig--enable-failover-session-replication-support"></a>

## Enable FailOver / Session Replication support

<a id="owbconfig--since-openwebbeans-150"></a>
<a id="owbconfig--since-openwebbeans-1.5.0"></a>

#### Since OpenWebBeans-1.5.0

OWB-1.5.x and later does *not* need any special module or filter to enable clustering.
All that works out of the box as we now directly utilize the Servlet Session.

<a id="owbconfig--openwebbeans-12x"></a>
<a id="owbconfig--openwebbeans-1.2.x"></a>

#### OpenWebBeans-1.2.x

Add the clustering module to your project:

```
<dependency>
    <groupId>org.apache.openwebbeans</groupId>
    <artifactId>openwebbeans-clustering</artifactId>
</dependency>
```

Register the FailOverFilter in your web.xml:

```
<filter>
    <filter-name>OWB FailOverFilter</filter-name>
    <filter-class>org.apache.webbeans.web.failover.FailOverFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>OWB FailOverFilter</filter-name>
    <servlet-name>Faces Servlet</servlet-name>
</filter-mapping>
```

<a id="owbconfig--openwebbeans-10x-and-11x"></a>
<a id="owbconfig--openwebbeans-1.0.x-and-1.1.x"></a>

#### OpenWebBeans-1.0.x and 1.1.x

Add the following properties in your openwebbeans.properties:

```
configuration.ordinal=100 
org.apache.webbeans.web.failover.issupportfailover=true
org.apache.webbeans.web.failover.issupportpassivation=true
```

Register the FailOverFilter in your web.xml:

```
<filter>
    <filter-name>OWB FailOverFilter</filter-name>
    <filter-class>org.apache.webbeans.web.failover.FailOverFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>OWB FailOverFilter</filter-name>
    <servlet-name>Faces Servlet</servlet-name>
</filter-mapping>
```

---
