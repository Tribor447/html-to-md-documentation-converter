# Project Information

## Navigation

- Commons JXPath
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Building](#building)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/index.html -->

<!-- page_index: 1 -->

<a id="index--the-jxpath-component"></a>

# The JXPath Component

The `org.apache.commons.jxpath` package defines a simple
interpreter of an expression language called XPath. JXPath applies *XPath*
expressions to graphs of objects of all kinds: JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

Consider this example:

>
```

Address address = (Address)JXPathContext.newContext(vendor).
         getValue("locations[address/zipCode='90210']/address");
```

This XPath expression is equivalent to the following Java code:

>
```

Address address = null;
Collection locations = vendor.getLocations();
Iterator it = locations.iterator();
while (it.hasNext()){
    Location location = (Location)it.next();
    String zipCode = location.getAddress().getZipCode();
    if (zipCode.equals("90210")){
      address = location.getAddress();
      break;
    }
}
```

XPath was standardized by W3C and is used in both XSLT and XPointer.

If you want to find out more about XPath, a good place to start
is an excellent XPath Tutorial by [W3Schools](http://www.w3schools.com/xpath)

The official definition of XPath by W3C can be found at
[XML Path Language (XPath) Version 1.0](http://www.w3.org/TR/xpath)

Primary applications of JXPath are in scripting: JSP and similar template/script based technologies.
However, programmers who prefer XML-flavored APIs, should consider JXPath as
an alternative to other expression languages as well. JXPath is a must-have tool
for those who work with mixtures of Java objects and XML and need to frequently
traverse through graphs of those.

Some XPath expressions may cause Java code execution, so you should not allow arbitrary expressions from untrusted input, which could in turn lead to security issues in your environment. Future enhancements may include the addition of an allow
list to let developers provide a stricter execution environment for expressions.

JXPath documentation currently contains:

- [User's Guide](https://commons.apache.org/proper/commons-jxpath/apidocs/index.html)
- [Javadoc API Documentation](https://commons.apache.org/proper/commons-jxpath/apidocs/index.html)

<a id="index--releases"></a>

# Releases

See the [JXPath Downloads](http://commons.apache.org/jxpath/download_jxpath.cgi)
page for current/previous releases.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-jxpath
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-jxpath
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-jxpath
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/security.html -->

<!-- page_index: 3 -->

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

For information about reporting or asking questions about security, please see the
[security page](https://commons.apache.org/security.html)
of the Apache Commons project.

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-jxpath/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the
[Apache Security Team](https://commons.apache.org/security.html).

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/building.html -->

<!-- page_index: 4 -->

<a id="building--overview"></a>

# Overview

Commons JXPath uses [Maven 1](http://maven.apache.org/maven-1.x/), [Maven 2](http://maven.apache.org) (preferred), or
[Ant](http://ant.apache.org) as a build system.

<a id="building--maven-2-goals"></a>

# Maven 2 Goals

The following ***Maven 2*** commands can be used to build Commons JXPath:

- `mvn clean` - clean up
- `mvn test` - compile and run the unit tests
- `mvn site` - create Commons JXPath documentation
- `mvn package` - build the jar
- `mvn install` - build the jar and install in local maven repository
- `mvn site assembly:assembly` - Create the source and binary distributions

<a id="building--maven-1-goals"></a>

# Maven 1 Goals

The following ***Maven 1*** commands can be used to build Commons JXPath:

- `maven clean` - clean up
- `maven test` - compile and run the unit tests
- `maven site` - create Commons JXPath documentation
- `maven jar` - build the jar
- `maven dist` - Create the source and binary distributions

<a id="building--ant-goals"></a>

# Ant Goals

**Note:**

- Dependencies are automatically downloaded if not specified explicitly in
  a `build.properties` file.

The following ***Ant*** commands can be used to build Commons JXPath:

- `ant clean` - clean up
- `ant test` - compile and run the unit tests
- `ant javadoc` - create javadocs
- `ant jar` - build the jar
- `ant dist` - Create the source and binary distributions

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | A Java-based implementation of XPath 1.0 that, in addition to XML processing, can inspect/modify Java object graphs (the library's explicit purpose) and even mixed Java/XML structures. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-jxpath/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-jxpath/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-jxpath/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-jxpath/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-jxpath/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-jxpath/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-jxpath/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/summary.html -->

<!-- page_index: 6 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JXPath |
| Description | A Java-based implementation of XPath 1.0 that, in addition to XML processing, can inspect/modify Java object graphs (the library's explicit purpose) and even mixed Java/XML structures. |
| Homepage | [https://commons.apache.org/proper/commons-jxpath/](#index) |

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
| GroupId | commons-jxpath |
| ArtifactId | commons-jxpath |
| Version | 1.4.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/team.html -->

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
| ![](https://www.gravatar.com/avatar/920b1560077708fade17fb18b5793913?d=mm&s=60) | dmitri | Dmitri Plotnikov | [dmitri@apache.org](mailto:dmitri@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/76e4509e1cd56389a2d776a9cfc8185d?d=mm&s=60) | craigmcc | Craig McClanahan | [Craig.McClanahan@eng.sun.com](mailto:Craig.McClanahan@eng.sun.com) | - | Sun Microsystems | - | - | - |
| ![](https://www.gravatar.com/avatar/f69e8a47116e742a2564d68f533f5357?d=mm&s=60) | mbenson | Matt Benson | [mbenson@apache.org](mailto:mbenson@apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Michele Vivoda

Uwe Barthel

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jxpath/ci-management.html -->

<!-- page_index: 8 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-jaxpth/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
