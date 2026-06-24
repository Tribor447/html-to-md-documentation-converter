# Project Information

## Navigation

- [Commons BeanUtils](#index)
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
- Documentation
  - [Building](#building)
  - [2.0.0-M2](#index)
  - [2.0.0-M1](#index)
  - [1.11.0](#index)
  - [1.10.1](#index)
  - [1.9.3](#index)
  - [1.9.2](#index)
  - [1.8.3](#index)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-beanutils"></a>

# Commons BeanUtils

Most Java developers are used to creating Java classes that conform to the
JavaBeans naming patterns for property getters and setters. It is natural to
then access these methods directly, using calls to the corresponding
`getXxx` and `setXxx` methods. However, there are some
occasions where dynamic access to Java object properties (without compiled-in
knowledge of the property getter and setter methods to be called) is needed.
Example use cases include:

- Building scripting languages that interact with the Java object model
  (such as the Bean Scripting Framework).
- Building template language processors for web presentation and similar
  uses (such as JSP or Velocity).
- Building custom tag libraries for JSP and XSP environments (such as Jakarta
  Taglibs, Struts, Cocoon).
- Consuming XML-based configuration resources (such as Ant build scripts, web
  application deployment descriptors, Tomcat's `server.xml`
  file).

The Java language provides *Reflection* and *Introspection*
APIs (see the `java.lang.reflect` and `java.beans`
packages in the JDK Javadocs). However, these APIs can be quite complex to
understand and utilize. The *BeanUtils* component provides
easy-to-use wrappers around these capabilities.

<a id="index--beanutils-core-and-modules"></a>

## BeanUtils Core And Modules

The 1.7.x and 1.8.x releases of BeanUtils distributed three jars:

- `commons-beanutils.jar` - contains everything
- `commons-beanutils-core.jar` - excludes *Bean Collections* classes
- `commons-beanutils-bean-collections.jar` - only *Bean Collections* classes

The main `commons-beanutils.jar` has an ***optional*** dependency on
[Commons Collections](https://commons.apache.org/collections)

Version 1.9.0 reverts this split for reasons outlined at
[BEANUTILS-379](https://issues.apache.org/jira/browse/BEANUTILS-379).
There is now only one jar for the BeanUtils library.

Version 2.0.0 updates the dependencies for Apache Commons Collection from version 3 to 4.
Apache Commons Collection 4 changes packages from `org.apache.commons.collections`
to `org.apache.commons.collections4`.
Since some Commons BeanUtils APIs surface Commons Collection types, Commons BeanUtils 2 changes packages from `org.apache.commons.beanutils`
to `org.apache.commons.beanutils2`.

<a id="index--bean-collections"></a>

## Bean Collections

Bean collections is a library combining BeanUtils with
[Commons Collections](https://commons.apache.org/collections)
to provide services for collections of beans. One class (`BeanComparator`)
was previously released, the rest are new. This new distribution strategy should allow
this sub-component to evolve naturally without the concerns about size and scope
that might otherwise happen.

Bean Collections has an additional dependency on
[Commons Collections](https://commons.apache.org/collections).

<a id="index--releases"></a>

# Releases

<a id="index--2.0.x-releases"></a>

## 2.0.x releases

BeanUtils **2.0.x** releases are not binary compatible (but easy to port) with version 1.x.x and require a minimum of
Java 8.

The latest BeanUtils release is available to download
[here](https://commons.apache.org/beanutils/download_beanutils.cgi).

- 2.0.0
  - [Release Notes](https://commons.apache.org/beanutils/changes.html)
  - [Javadoc](https://commons.apache.org/beanutils/apidocs/index.html)

<a id="index--1.9.x-releases"></a>

## 1.9.x releases

The latest BeanUtils release is available to download
[here](https://commons.apache.org/beanutils/download_beanutils.cgi).
***1.9.4***

- [Release Notes](https://commons.apache.org/beanutils/changes.html#a1.9.4)
- [JavaDoc](https://commons.apache.org/beanutils/javadocs/v1.9.4/apidocs/index.html)

**CVE-2019-10086.** Apache Commons Beanutils does not suppresses
the class property in bean introspection by default.
**Severity.** Medium
**Vendor.** The Apache Software Foundation
**Versions Affected.** All versions commons-beanutils-1.9.3 and before.
**Description.** In version 1.9.2, a special BeanIntrospector class was added which allows suppressing the ability for
an attacker to access the classloader via the class property available on all Java objects. We, however were not
using this by default characteristic of the PropertyUtilsBean.
**Mitigation.** Upgrade to commons-beanutils-1.9.4
**Credit.** This was discovered by Melloware (https://melloware.com/).
**Example.**

```
/** * Example usage after 1.9.4 */ public void testSuppressClassPropertyByDefault() throws Exception {final BeanUtilsBean bub = new BeanUtilsBean(); final AlphaBean bean = new AlphaBean(); try {bub.getProperty(bean, "class"); fail("Could access class property!"); } catch (final NoSuchMethodException ex) {// ok}}
/** * Example usage to restore 1.9.3 behavior */ public void testAllowAccessToClassProperty() throws Exception {final BeanUtilsBean bub = new BeanUtilsBean(); bub.getPropertyUtils().removeBeanIntrospector(SuppressPropertiesBeanIntrospector.SUPPRESS_CLASS); final AlphaBean bean = new AlphaBean(); String result = bub.getProperty(bean, "class"); assertEquals("Class property should have been accessed", "class org.apache.commons.beanutils2.AlphaBean", result);}
```

BeanUtils **1.9.x** releases are binary compatible (with a minor exception
described in the release notes) with version 1.8.3 and require a minimum of
JDK 1.5.

The latest BeanUtils release is available to download
[here](https://commons.apache.org/beanutils/download_beanutils.cgi).

- 1.9.3
  - [Release Notes](assets/files/release-notes_e6bc7328f4da5bd9.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.9.3/apidocs/index.html)
- 1.9.2
  - [Release Notes](assets/files/release-notes_920f61732c363750.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.9.2/apidocs/index.html)
- 1.9.1
  - [Release Notes](assets/files/release-notes_396bd27e40ca7095.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.9.1/apidocs/index.html)
- 1.9.0
  - [Release Notes](assets/files/release-notes_9f197c7f083b8d9e.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.9.0/apidocs/index.html)

<a id="index--1.8.x-releases"></a>

## 1.8.x releases

BeanUtils **1.8.x** releases are binary compatible with version 1.7.0 and
require a minimum of JDK 1.3.

- 1.8.3
  - [Release Notes](assets/files/release-notes_0e990c6fa6343638.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.8.3/apidocs/index.html)
- 1.8.2
  - [Release Notes](assets/files/release-notes_c6b4e5f5a237332a.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.8.2/apidocs/index.html)
- 1.8.1
  - [Release Notes](assets/files/release-notes_f171dbf0529e9bb0.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.8.1/apidocs/index.html)
- 1.8.0
  - [Release Notes](assets/files/release-notes_13c4dd284ef7ae54.txt)
  - [Javadoc](https://commons.apache.org/beanutils/javadocs/v1.8.0/apidocs/index.html)

<a id="index--1.7.0"></a>

## 1.7.0

**BeanUtils 1.7.0** is a service release which removes the dependency
upon a specific commons-collection library version. It may be safely used together
with either the 2.x or 3.x series of commons-collections releases.
It also introduces a number of important enhancements. It is backward compatible
with the 1.6 release.

This important service release is intended to help downstream applications solve
dependency issues. The dependency on commons collections (which has become problematic
now that there are two incompatible series of commons collections releases)
has been factored into a separate optional sub-component plus a small number of
stable and mature `org.apache.commons.collections` packaged classes
(which are distributed with the BeanUtils core). This arrangement means that the
BeanUtils core sub-component (which is the primary dependency for most downsteam
applications) can now be safely included on the same classpath as commons collections
2.x, 3.x or indeed neither.

The distribution now contains alternative jar sets. The all-in-one
jar contains all classes. The modular jar set consists of a core jar dependent only
on commons logging and an optional bean collections jar (containing classes that
provide easy and efficient ways to manage collections of beans) which depends on
commons collections 3.

<a id="index--older-releases-not-mirrored"></a>

## Older Releases (Not Mirrored)

- Version 1.6.1 - 18 Feb 2003
  [binary](https://archive.apache.org/dist/commons/beanutils/binaries/) and
  [source](https://archive.apache.org/dist/commons/beanutils/source/)
- Version 1.6 - 21 Jan 2003
  [binary](https://archive.apache.org/dist/commons/beanutils/binaries/) and
  [source](https://archive.apache.org/dist/commons/beanutils/source/)
- [Version 1.5](https://archive.apache.org/dist/commons/beanutils/old/v1.5/)  - 23 Oct 2002
- [Version 1.4.1](https://archive.apache.org/dist/commons/beanutils/old/v1.4.1/) - 28 Aug 2002
- [Version 1.4](https://archive.apache.org/dist/commons/beanutils/old/v1.4/) - 13 Aug 2002
- [Version 1.3](https://archive.apache.org/dist/commons/beanutils/old/v1.3/) - 29 Apr 2002
- [Version 1.2](https://archive.apache.org/dist/commons/beanutils/old/v1.2/) - 24 Dec 2001
- [Version 1.1](https://archive.apache.org/dist/commons/beanutils/old/v1.1/) - 22 Sep 2001
- [Version 1.0](https://archive.apache.org/dist/commons/beanutils/old/v1.0/) - 14 July 2001

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-beanutils/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [beanutils].

Issues may be reported via [ASF JIRA](https://commons.apache.org/proper/commons-beanutils/issue-tracking.html).

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-beanutils.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-beanutils.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-beanutils.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/security.html -->

<!-- page_index: 3 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html)
.

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the
public
[user mailing list](https://commons.apache.org/proper/commons-beanutils/mail-lists.html)
.

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report
them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

<a id="security--cve-2019-10086"></a>

## CVE-2019-10086

- CVE-2019-10086: Apache Commons Beanutils does not suppresses the class property in PropertyUtilsBean by default.
- Severity: Medium
- Vendor: The Apache Software Foundation
- Versions Affected: commons-beanutils-1.9.3 and earlier
- Description: A special BeanIntrospector class was added in version 1.9.2.
  This can be used to stop attackers from using the class property of
  Java objects to get access to the classloader.
  However this protection was not enabled by default.
  PropertyUtilsBean (and consequently BeanUtilsBean) now disallows class
  level property access by default, thus protecting against
  CVE-2014-0114.
- Mitigation: 1.X users should migrate to 1.9.4.
- Credit: This was discovered by Melloware (https://melloware.com/).

Example:

```
/** * Example displaying the new default behavior such that * it is not possible to access class level properties utilizing the * BeanUtilsBean, which in turn utilizes the PropertyUtilsBean.*/ public void testSuppressClassPropertyByDefault() throws Exception {final BeanUtilsBean bub = new BeanUtilsBean(); final AlphaBean bean = new AlphaBean(); try {bub.getProperty(bean, "class"); fail("Could access class property!"); } catch (final NoSuchMethodException ex) {// ok}}
/** * Example showing how by which one would use to revert to the * behaviour prior to the 1.9.4 release where class level properties were accessible by * the BeanUtilsBean and the PropertyUtilsBean.*/ public void testAllowAccessToClassProperty() throws Exception {final BeanUtilsBean bub = new BeanUtilsBean(); bub.getPropertyUtils().removeBeanIntrospector(SuppressPropertiesBeanIntrospector.SUPPRESS_CLASS); final AlphaBean bean = new AlphaBean(); String result = bub.getProperty(bean, "class"); assertEquals("Class property should have been accessed", "class org.apache.commons.beanutils2.AlphaBean", result);}
```

References:

1. https://issues.apache.org/jira/browse/BEANUTILS-520
2. http://commons.apache.org/proper/commons-beanutils/

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/building.html -->

<!-- page_index: 4 -->

<a id="building--overview"></a>

# Overview

Commons BeanUtils can be built using
[Maven 3](http://maven.apache.org)
(Recommended: Maven 3.3)
and JDK 6 / OpenJDK 6 or later (recommended: JDK 8).

Further details can be found in the
[commons build instructions](https://commons.apache.org/building.html).

<a id="building--maven-3-goals"></a>

# Maven 3 Goals

Build using
[Maven 3](http://maven.apache.org)
is the preferred build method.
The compiled BeanUtils JAR should work with Java 6 or later.

To build
`target/commons-beanutils-*.jar`

```

        mvn clean package
      
```

or to install into your
`~/.m2/repository`

```

        mvn clean install
      
```

You can skip the unit tests by adding the parameter
`-DskipTests=true`

To regenerate the web site
(corresponding to
https://commons.apache.org/proper/commons-beanutils/)

```

        mvn clean site
      
```

Note: the Apache Commons BeanUtils site should include a
[japicmp report](https://commons.apache.org/proper/commons-beanutils/japicmp.html)
for the
purpose of checking API version compatibility; to enable this, use Java 7
or later and run instead:

```

        mvn clean package site -Pjapicmp
      
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons BeanUtils provides an easy-to-use but flexible wrapper around reflection and introspection. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-beanutils/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-beanutils/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-beanutils/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-beanutils/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-beanutils/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-beanutils/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-beanutils/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/summary.html -->

<!-- page_index: 6 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons BeanUtils |
| Description | Apache Commons BeanUtils provides an easy-to-use but flexible wrapper around reflection and introspection. |
| Homepage | [https://commons.apache.org/proper/commons-beanutils/](#index) |

<a id="summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-beanutils2 |
| Version | 2.0.0-M2 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/team.html -->

<!-- page_index: 7 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/30f9094d5dbe2ce93f1a41afc9615b83_b8c2a9282cccd18e.jpg) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | dion | Dion Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | craigmcc | Craig McClanahan | [craigmcc@apache.org](mailto:craigmcc@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | geirm | Geir Magnusson Jr. | [geirm@apache.org](mailto:geirm@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | sanders | Scott Sanders | [sanders@apache.org](mailto:sanders@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | jstrachan | James Strachan | [jstrachan@apache.org](mailto:jstrachan@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | rwaldhoff | Rodney Waldhoff | [rwaldhoff@apache.org](mailto:rwaldhoff@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | mvdb | Martin van den Bemt | [mvdb@apache.org](mailto:mvdb@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/248341e80da66f10c0d6af27f40c8d63_ad554cac634c21d1.jpg) | yoavs | Yoav Shapira | [yoavs@apache.org](mailto:yoavs@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | niallp | Niall Pemberton | [niallp@apache.org](mailto:niallp@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | skitching | Simon Kitching | [skitching@apache.org](mailto:skitching@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | jcarman | James Carman | [jcarman@apache.org](mailto:jcarman@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/cbfb61ee7f8641b2b6eaf22fed163b1e_4309e5829f39bf45.jpg) | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/0b185e68b9933eccb52d90eda3097986_37a1600aab7d35d3.jpg) | tobrien | Tim O'Brien | [tobrien@apache.org](mailto:tobrien@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | epugh | David Eric Pugh | [epugh@apache.org](mailto:epugh@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | rwaldhoff | Rodney Waldhoff | [rwaldhoff@apache.org](mailto:rwaldhoff@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | morgand | Morgan James Delagrange | [morgand@apache.org](mailto:morgand@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | jconlon | John E. Conlon | [jconlon@apache.org](mailto:jconlon@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1f23908d89f927ad.jpg) | scolebourne | Stephen Colebourne | [scolebourne@apache.org](mailto:scolebourne@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/9338945503e6ce8778c35b7f8218f397_331a06b62e9c42e6.jpg) | stain | Stian Soiland-Reyes | [stain@apache.org](mailto:stain@apache.org) | <http://orcid.org/0000-0001-9842-9718> | The Apache Software Foundation | - | - | +0 |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Paul Jack

Stephen Colebourne

Berin Loritsch

Alex Crown

Marcus Zander

Paul Hamamnt

Rune Johannesen

Clebert Suconic

Norm Deane

Ralph Schaer

Chris Audley

Rey François

Gregor Raýman

Jan Sorensen

Eric Pabst

Paulo Gaspar

Michael Smith

George Franciscus

Erik Meade

Tomas Viberg

Yauheny Mikulski

Michael Szlapa

Juozas Baliuka

Tommy Tynjä

Bernhard Seebass

Raviteja Lokineni

Sergey Chernov

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/ci-management.html -->

<!-- page_index: 8 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
