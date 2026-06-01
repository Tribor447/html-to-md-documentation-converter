# Commons Proxy - Project Information

## Navigation

- [Commons Proxy](#index)
  - [Overview](#index)
  - [Issue Tracking](#issue-tracking)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Project Summary](#project-summary)
    - [Project Modules](#modules)
    - [Issue Tracking](#issue-tracking)
    - [Continuous Integration](#integration)
- Other pages
  - [Commons Proxy ASM Proxies Module -](#commons-proxy2-asm)
  - [Commons Proxy ASM Proxies Module - Continuous Integration](#commons-proxy2-asm-integration)
  - [Commons Proxy ASM Proxies Module - Issue Tracking](#commons-proxy2-asm-issue-tracking)
  - [Commons Proxy ASM Proxies Module - Project Summary](#commons-proxy2-asm-project-summary)
  - [Commons Proxy Build Tools - About](#commons-proxy2-build-tools)
  - [Commons Proxy Build Tools - Continuous Integration](#commons-proxy2-build-tools-integration)
  - [Commons Proxy Build Tools - Issue Tracking](#commons-proxy2-build-tools-issue-tracking)
  - [Commons Proxy Build Tools - Project Summary](#commons-proxy2-build-tools-project-summary)
  - [Commons Proxy CGLIB Proxies Module -](#commons-proxy2-cglib)
  - [Commons Proxy CGLIB Proxies Module - Continuous Integration](#commons-proxy2-cglib-integration)
  - [Commons Proxy CGLIB Proxies Module - Issue Tracking](#commons-proxy2-cglib-issue-tracking)
  - [Commons Proxy CGLIB Proxies Module - Project Summary](#commons-proxy2-cglib-project-summary)
  - [Commons Proxy Core - About](#commons-proxy2-core)
  - [Commons Proxy Core - Continuous Integration](#commons-proxy2-core-integration)
  - [Commons Proxy Core - Issue Tracking](#commons-proxy2-core-issue-tracking)
  - [Commons Proxy Core - Project Summary](#commons-proxy2-core-project-summary)
  - [Commons Proxy Javassist Proxies Module -](#commons-proxy2-javassist)
  - [Commons Proxy Javassist Proxies Module - Continuous Integration](#commons-proxy2-javassist-integration)
  - [Commons Proxy Javassist Proxies Module - Issue Tracking](#commons-proxy2-javassist-issue-tracking)
  - [Commons Proxy Javassist Proxies Module - Project Summary](#commons-proxy2-javassist-project-summary)
  - [Commons Proxy JDK Proxies Module -](#commons-proxy2-jdk)
  - [Commons Proxy JDK Proxies Module - Continuous Integration](#commons-proxy2-jdk-integration)
  - [Commons Proxy JDK Proxies Module - Issue Tracking](#commons-proxy2-jdk-issue-tracking)
  - [Commons Proxy JDK Proxies Module - Project Summary](#commons-proxy2-jdk-project-summary)
  - [Commons Proxy Test - About](#commons-proxy2-test)
  - [Commons Proxy Test - Continuous Integration](#commons-proxy2-test-integration)
  - [Commons Proxy Test - Issue Tracking](#commons-proxy2-test-issue-tracking)
  - [Commons Proxy Test - Project Summary](#commons-proxy2-test-project-summary)
  - [Apache Commons Proxy Distribution - About](#commons-proxy2)
  - [Apache Commons Proxy Distribution - Continuous Integration](#commons-proxy2-integration)
  - [Apache Commons Proxy Distribution - Issue Tracking](#commons-proxy2-issue-tracking)
  - [Apache Commons Proxy Distribution - Project Summary](#commons-proxy2-project-summary)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-proxy:-dynamic-proxies-made-easy"></a>

## Commons Proxy: Dynamic Proxies Made Easy

The *Proxy* design pattern ([GoF](http://www.amazon.com/exec/obidos/tg/detail/-/0201633612/qid=1125413337/sr=1-1/ref=sr_1_1/104-0714405-6441551?v=glance&amp;s=books)) allows you to provide “a surrogate or placeholder for another object to control access to it”. Proxies can be used in many ways, some of which are:

- **Deferred Initialization** - the proxy acts as a “stand-in” for the actual implementation allowing it to be instantiated only when absolutely necessary.
- **Security** - the proxy object can verify that the user actually has the permission to execute the method (a la EJB).
- **Logging** - the proxy can log evey method invocation, providing valuable debugging information.
- **Performance Monitoring** - the proxy can log each method invocation to a performance monitor allowing system administrators to see what parts of the system are potentially bogged down.

*Commons Proxy* supports dynamic proxy generation using proxy factories, object providers, invokers, and interceptors.

<a id="index--proxy-factories"></a>

## Proxy Factories

A [ProxyFactory](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/ProxyFactory.html) encapsulates all necessary proxying logic away from your code. Switching proxying techniques/technologies is as simple as using a different proxy factory implementation class. *Commons Proxy* provides several proxy factory implementation modules:

- [commons-proxy2-jdk](#commons-proxy2-jdk)
- [commons-proxy2-cglib](#commons-proxy2-cglib)
- [commons-proxy2-javassist](#commons-proxy2-javassist)
- [commons-proxy2-asm4](https://commons.apache.org/dormant/commons-proxy/commons-proxy2-asm4/index.html)

Additionally, the core library provides a proxy factory [implementation](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/ProxyUtils.html#proxyFactory) that delegates to instances discoverable using the Java [ServiceLoader](http://docs.oracle.com/javase/6/docs/api/java/util/ServiceLoader.html) mechanism (including those provided by the listed modules).

Proxy factories allow you to create three different types of proxy objects:

- **Delegator Proxy** - delegates each method invocation to an object provided by an [ObjectProvider](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/ObjectProvider.html).
- **Interceptor Proxy** - allows an [Interceptor](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/Interceptor.html) to intercept each method invocation as it makes its way to the target of the invocation.
- **Invoker Proxy** - uses an [Invoker](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/Invoker.html) to handle all method invocations.

<a id="index--object-providers"></a>

## Object Providers

[Object providers](https://commons.apache.org/dormant/commons-proxy/apidocs/index.html?org%2Fapache%2Fcommons%2Fproxy2%2Fprovider%2Fpackage-summary.html=) provide the objects which will be the “target” of a proxy. There are two types of object providers:

<a id="index--core-object-providers"></a>

### Core Object Providers

A core object provider provides a core implementation object. *Commons Proxy* supports many different implementations including:

- **Constant** - Always returns a specific object
- **Bean** - Instantiates an object of a specified class each time
- **Cloning** - Reflectively calls the public clone() method on a Cloneable object

<a id="index--decorating-object-providers"></a>

### Decorating Object Providers

A decorating object provider decorates the object returned by another provider. *Commons Proxy* provides a few implementations including:

- **Singleton** - Calls a nested provider at most once, returning that original value on all subsequent invocations

<a id="index--invokers"></a>

## Invokers

An [Invoker](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/Invoker.html) handles all method invocations using a single method. *Commons Proxy* provides a few invoker implementations:

- **Null** - Always returns a null (useful for the “Null Object” pattern)
- **Duck Typing** - Supports so-called “duck typing” by adapting a class to an interface it does not implement.
- **Invocation Handler Adapter** - Adapts an implementation of the JDK [InvocationHandler](http://docs.oracle.com/javase/6/docs/api/java/lang/reflect/InvocationHandler.html) interface as a *Commons Proxy* [Invoker](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/Invoker.html).

<a id="index--interceptors"></a>

## Interceptors

*Commons Proxy* allows you to “intercept” a method invocation using an [Interceptor](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/Interceptor.html). Interceptors provide *rudimentary* aspect-oriented programming (AOP) support, allowing you to alter the parameters/results of a method invocation without actually changing the implementation of the method itself. *Commons Proxy* provides a few interceptor implementations including:

- **ObjectProvider** - returns the value from an [ObjectProvider](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/ObjectProvider.html)
- **Throwing** - throws an exception
- **Switch** - provides a fluent API to configure the handling of invoked methods

<a id="index--serialization"></a>

## Serialization

The proxies created by the provided proxy factories are Serializable in most cases. For more complex cases *Commons Proxy* provides basic support for the “serialization proxy” pattern. See [org.apache.commons.proxy.serialization](https://commons.apache.org/dormant/commons-proxy/apidocs/index.html?org%2Fapache%2Fcommons%2Fproxy2%2Fserialization%2Fpackage-summary.html=) for details.

<a id="index--stubbing"></a>

## Stubbing

The [StubBuilder](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/stub/StubBuilder.html) class allows you to create a proxy with customized behavior specified by a typesafe DSL. The [AnnotationBuilder](https://commons.apache.org/dormant/commons-proxy/apidocs/org/apache/commons/proxy2/stub/AnnotationBuilder.html) variant provides a simple way to create Java annotation instances at runtime.

<a id="index--releases"></a>

## Releases

The latest version is v1.0 *(requires Java 1.4 or later)*. - [Download now!](http://commons.apache.org/downloads/download_proxy.cgi)

For previous releases, see the [Apache archive](http://archive.apache.org/dist/commons/proxy/).

<a id="index--support"></a>

## Support

The [Commons mailing lists](https://commons.apache.org/dormant/commons-proxy/mail-lists.html) act as the main support forum. The user list is suitable for most library usage queries. The dev list is intended for the development discussion. Please remember that the lists are shared between all Commons components, so prefix your email subject with [proxy].

Issues may be reported via [ASF JIRA](#issue-tracking). Please read the instructions carefully to submit a useful bug report or enhancement request.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/issue-tracking.html -->

<!-- page_index: 2 -->

<a id="issue-tracking--commons-proxy-issue-tracking"></a>

## Commons Proxy Issue tracking

Commons Proxy uses [ASF JIRA](http://issues.apache.org/jira/) for tracking issues.
See the [Commons Proxy JIRA project page](http://issues.apache.org/jira/browse/PROXY).

To use JIRA you may need to [create an account](http://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](http://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Commons Proxy please do the following:

1. [Search existing open bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310731&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/dormant/commons-proxy/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310731&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310731&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Commons Proxy are all unpaid volunteers

For more information on subversion and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Commons Proxy bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310731&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Commons Proxy bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310731&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Commons Proxy bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310731&sorter/field=issuekey&sorter/order=DESC)

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/project-info.html -->

<!-- page_index: 3 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | Java library for dynamic proxying |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Project Team](https://commons.apache.org/dormant/commons-proxy/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Repository](https://commons.apache.org/dormant/commons-proxy/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Mailing Lists](https://commons.apache.org/dormant/commons-proxy/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependency Management](https://commons.apache.org/dormant/commons-proxy/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/dormant/commons-proxy/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/dormant/commons-proxy/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/dormant/commons-proxy/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/project-summary.html -->

<!-- page_index: 4 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Proxy |
| Description | Java library for dynamic proxying |
| Homepage | <http://commons.apache.org/proxy/> |

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
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-parent |
| Version | 2.0-SNAPSHOT |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/modules.html -->

<!-- page_index: 5 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Commons Proxy Build Tools](#commons-proxy2-build-tools) | Provide common setup, from http://maven.apache.org/plugins/maven-checkstyle-plugin/examples/multi-module-config.html |
| [Commons Proxy Core](#commons-proxy2-core) | Java library for dynamic proxying |
| [Commons Proxy JDK Proxies Module](#commons-proxy2-jdk) | Interface-based proxies using the core JDK Proxy mechanism |
| [Commons Proxy ASM Proxies Module](#commons-proxy2-asm) | Proxies based on classes dynamically generated using ASM v4+ |
| [Commons Proxy Javassist Proxies Module](#commons-proxy2-javassist) | Proxies based on classes dynamically generated using Javassist |
| [Commons Proxy CGLIB Proxies Module](#commons-proxy2-cglib) | Proxies based on classes dynamically generated using cglib |
| [Commons Proxy Test](#commons-proxy2-test) | Tests things that depend on multiple modules |
| [Apache Commons Proxy Distribution](#commons-proxy2) | Creates the Apache Commons Proxy multimodule distribution. |

---

<a id="integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/integration.html -->

<!-- page_index: 6 -->

<a id="integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-asm"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-asm/index.html -->

<!-- page_index: 7 -->

<a id="commons-proxy2-asm--commons-proxy-asm4"></a>

## Commons Proxy ASM4

Provides the [ASM4ProxyFactory](https://commons.apache.org/dormant/commons-proxy/commons-proxy2-asm/apidocs/org/apache/commons/proxy2/asm4/ASM4ProxyFactory.html) which uses the [ASM](http://asm.ow2.org/) library (v4.x) to create proxy classes. This proxy factory is capable of proxying concrete non-final types and can thus be considered a *subclassing* proxy factory.

---

<a id="commons-proxy2-asm-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-asm/integration.html -->

<!-- page_index: 8 -->

<a id="commons-proxy2-asm-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-asm-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-asm-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-asm-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-asm/issue-tracking.html -->

<!-- page_index: 9 -->

<a id="commons-proxy2-asm-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-asm-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-asm-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-asm/project-summary.html -->

<!-- page_index: 10 -->

<a id="commons-proxy2-asm-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-asm-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy ASM Proxies Module |
| Description | Proxies based on classes dynamically generated using ASM v4+ |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-asm/> |

<a id="commons-proxy2-asm-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-asm-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-asm |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2-build-tools"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-build-tools/index.html -->

<!-- page_index: 11 -->

<a id="commons-proxy2-build-tools--about-commons-proxy-build-tools"></a>

## About Commons Proxy Build Tools

Provide common setup, from http://maven.apache.org/plugins/maven-checkstyle-plugin/examples/multi-module-config.html

---

<a id="commons-proxy2-build-tools-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-build-tools/integration.html -->

<!-- page_index: 12 -->

<a id="commons-proxy2-build-tools-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-build-tools-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-build-tools-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-build-tools-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-build-tools/issue-tracking.html -->

<!-- page_index: 13 -->

<a id="commons-proxy2-build-tools-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-build-tools-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-build-tools-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-build-tools/project-summary.html -->

<!-- page_index: 14 -->

<a id="commons-proxy2-build-tools-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-build-tools-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy Build Tools |
| Description | Provide common setup, from http://maven.apache.org/plugins/maven-checkstyle-plugin/examples/multi-module-config.html |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-build-tools/> |

<a id="commons-proxy2-build-tools-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-build-tools-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-build-tools |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2-cglib"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-cglib/index.html -->

<!-- page_index: 15 -->

<a id="commons-proxy2-cglib--commons-proxy-cglib"></a>

## Commons Proxy Cglib

Provides the [CglibProxyFactory](https://commons.apache.org/dormant/commons-proxy/commons-proxy2-cglib/apidocs/org/apache/commons/proxy2/cglib/CglibProxyFactory.html) which uses the [cglib](http://cglib.sourceforge.net/) library to create proxy classes. This proxy factory is capable of proxying concrete non-final types and can thus be considered a *subclassing* proxy factory.

---

<a id="commons-proxy2-cglib-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-cglib/integration.html -->

<!-- page_index: 16 -->

<a id="commons-proxy2-cglib-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-cglib-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-cglib-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-cglib-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-cglib/issue-tracking.html -->

<!-- page_index: 17 -->

<a id="commons-proxy2-cglib-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-cglib-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-cglib-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-cglib/project-summary.html -->

<!-- page_index: 18 -->

<a id="commons-proxy2-cglib-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-cglib-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy CGLIB Proxies Module |
| Description | Proxies based on classes dynamically generated using cglib |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-cglib/> |

<a id="commons-proxy2-cglib-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-cglib-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-cglib |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2-core"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-core/index.html -->

<!-- page_index: 19 -->

<a id="commons-proxy2-core--about-commons-proxy-core"></a>

## About Commons Proxy Core

Java library for dynamic proxying

---

<a id="commons-proxy2-core-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-core/integration.html -->

<!-- page_index: 20 -->

<a id="commons-proxy2-core-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-core-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-core-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-core-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-core/issue-tracking.html -->

<!-- page_index: 21 -->

<a id="commons-proxy2-core-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-core-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-core-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-core/project-summary.html -->

<!-- page_index: 22 -->

<a id="commons-proxy2-core-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-core-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy Core |
| Description | Java library for dynamic proxying |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-core/> |

<a id="commons-proxy2-core-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-core-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-core |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2-javassist"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-javassist/index.html -->

<!-- page_index: 23 -->

<a id="commons-proxy2-javassist--commons-proxy-javassist"></a>

## Commons Proxy Javassist

Provides the [JavassistProxyFactory](https://commons.apache.org/dormant/commons-proxy/commons-proxy2-javassist/apidocs/org/apache/commons/proxy2/javassist/JavassistProxyFactory.html) which uses the [Javassist](http://www.javassist.org) library to create proxy classes. This proxy factory is capable of proxying concrete non-final types and can thus be considered a *subclassing* proxy factory.

---

<a id="commons-proxy2-javassist-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-javassist/integration.html -->

<!-- page_index: 24 -->

<a id="commons-proxy2-javassist-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-javassist-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-javassist-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-javassist-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-javassist/issue-tracking.html -->

<!-- page_index: 25 -->

<a id="commons-proxy2-javassist-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-javassist-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-javassist-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-javassist/project-summary.html -->

<!-- page_index: 26 -->

<a id="commons-proxy2-javassist-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-javassist-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy Javassist Proxies Module |
| Description | Proxies based on classes dynamically generated using Javassist |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-javassist/> |

<a id="commons-proxy2-javassist-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-javassist-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-javassist |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2-jdk"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-jdk/index.html -->

<!-- page_index: 27 -->

<a id="commons-proxy2-jdk--commons-proxy-jdk"></a>

## Commons Proxy JDK

Uses the [Proxy](http://docs.oracle.com/javase/6/docs/api/java/lang/reflect/Proxy.html) mechanism provided by the core JDK to create dynamic proxy instances. This proxy factory exposes interfaces only.

---

<a id="commons-proxy2-jdk-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-jdk/integration.html -->

<!-- page_index: 28 -->

<a id="commons-proxy2-jdk-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-jdk-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-jdk-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-jdk-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-jdk/issue-tracking.html -->

<!-- page_index: 29 -->

<a id="commons-proxy2-jdk-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-jdk-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-jdk-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-jdk/project-summary.html -->

<!-- page_index: 30 -->

<a id="commons-proxy2-jdk-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-jdk-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy JDK Proxies Module |
| Description | Interface-based proxies using the core JDK Proxy mechanism |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-jdk/> |

<a id="commons-proxy2-jdk-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-jdk-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-jdk |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2-test"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-test/index.html -->

<!-- page_index: 31 -->

<a id="commons-proxy2-test--about-commons-proxy-test"></a>

## About Commons Proxy Test

Tests things that depend on multiple modules

---

<a id="commons-proxy2-test-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-test/integration.html -->

<!-- page_index: 32 -->

<a id="commons-proxy2-test-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-test-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-test-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-test-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-test/issue-tracking.html -->

<!-- page_index: 33 -->

<a id="commons-proxy2-test-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-test-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-test-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2-test/project-summary.html -->

<!-- page_index: 34 -->

<a id="commons-proxy2-test-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-test-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Proxy Test |
| Description | Tests things that depend on multiple modules |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2-test/> |

<a id="commons-proxy2-test-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-test-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2-test |
| Version | 2.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.6 |

---

<a id="commons-proxy2"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2/index.html -->

<!-- page_index: 35 -->

<a id="commons-proxy2--about-apache-commons-proxy-distribution"></a>

## About Apache Commons Proxy Distribution

Creates the Apache Commons Proxy multimodule distribution.

---

<a id="commons-proxy2-integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2/integration.html -->

<!-- page_index: 36 -->

<a id="commons-proxy2-integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="commons-proxy2-integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="commons-proxy2-integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-proxy2-issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2/issue-tracking.html -->

<!-- page_index: 37 -->

<a id="commons-proxy2-issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="commons-proxy2-issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/PROXY
```

---

<a id="commons-proxy2-project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-proxy/commons-proxy2/project-summary.html -->

<!-- page_index: 38 -->

<a id="commons-proxy2-project-summary--project-summary"></a>

## Project Summary

<a id="commons-proxy2-project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Proxy Distribution |
| Description | Creates the Apache Commons Proxy multimodule distribution. |
| Homepage | <http://commons.apache.org/proxy/commons-proxy2/> |

<a id="commons-proxy2-project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="commons-proxy2-project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-proxy2 |
| Version | 2.0-SNAPSHOT |
| Type | pom |

---
