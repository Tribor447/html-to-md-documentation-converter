# Project Information

## Navigation

- [Commons Lang](#index)
  - [About](#index)
  - [Sources](#scm)
  - [Users guide](#userguide)
  - [Building](#building)
  - [Proposal](#proposal)
  - [Developer guide](#developerguide)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-lang"></a>

# Commons Lang

The standard Java libraries fail to provide enough methods for
manipulation of its core classes. Apache Commons Lang provides
these extra methods.

Apache Commons Lang provides a host of helper utilities for the java.lang API, notably
String manipulation methods, basic numerical methods, object reflection, concurrency, creation and serialization
and System properties. Additionally it contains basic enhancements to java.util.Date and a series of utilities dedicated to help with
building methods, such as hashCode, toString and equals.

Note that Commons Lang 3.0 (and subsequent versions) use a different package (*org.apache.commons.lang3*) than the previous versions (*org.apache.commons.lang*), allowing Commons Lang 3 to be used at the same time as Commons Lang 2.

<a id="index--documentation"></a>

# Documentation

The package descriptions in the [Javadoc](https://commons.apache.org/proper/commons-lang/apidocs/index.html) give an overview of the available features
and various [project reports](https://commons.apache.org/proper/commons-lang/project-reports.html) are provided.

The Javadoc API documents are available online:

- The [current release](https://commons.apache.org/proper/commons-lang/apidocs/index.html) [Java 8 and up]
- The [legacy releases for 3.x](https://javadoc.io/doc/org.apache.commons/commons-lang3)
- The [legacy releases for 2.x](https://javadoc.io/doc/commons-lang/commons-lang) [Java 1.2 and up]
- Older releases - see the [Release History](https://commons.apache.org/proper/commons-lang/changes.html) page

The [git repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-lang.git), or you can browse/contribute via [GitHub](https://github.com/apache/commons-lang).

<a id="index--release-information"></a>

# Release Information

Read about the latest release:

- Pull it using a build tool like Maven using a [dependency management reference](https://commons.apache.org/proper/commons-lang/dependency-info.html).
- Download the latest release from a [mirror](https://commons.apache.org/lang/download_lang.cgi).
- Read the [change report](https://commons.apache.org/proper/commons-lang/changes.html).
- Examine the [2.x to 3.0 upgrade notes](https://commons.apache.org/proper/commons-lang/article3_0.html).
- Compare major versions via the [Lang2 to Lang3 Clirr report](https://commons.apache.org/proper/commons-lang/lang2-lang3-clirr-report.html).

For information on previous releases see the [Release History](https://commons.apache.org/proper/commons-lang/changes.html), and to download previous releases see the [Commons Lang Archive](https://archive.apache.org/dist/commons/lang/).

<a id="index--getting-involved"></a>

# Getting Involved

The [commons developer mailing list](https://commons.apache.org/proper/commons-lang/mail-lists.html) is the main channel of communication for contributors. Please remember that the lists are shared between all commons components, so prefix your email by [lang].

You can also peruse [JIRA](https://commons.apache.org/proper/commons-lang/issue-tracking.html). Specific links of interest for JIRA are:

- Ideas looking for code: [Patch Needed](https://issues.apache.org/jira/issues/?jql=project%20%3D%20LANG%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20%22Patch%20Needed%22%20ORDER%20BY%20priority%20DESC)
- Issues with patches, looking for reviews: [Review Patch](https://issues.apache.org/jira/issues/?jql=fixVersion%20%3D%20%22Review%20Patch%22%20AND%20project%20%3D%20LANG%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC)

Alternatively you can go through the *Needs Work* tags in the [TagList report](https://commons.apache.org/proper/commons-lang/taglist.html).

If you'd like to offer up pull requests via GitHub rather than applying patches to JIRA, we have a [GitHub mirror](https://github.com/apache/commons-lang/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-lang/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [lang].

Bug reports and enhancements are also welcomed via the [JIRA](https://commons.apache.org/proper/commons-lang/issue-tracking.html) issue tracker.
Please read the instructions carefully.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-lang.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch rel/commons-lang-3.18.0 https://gitbox.apache.org/repos/asf/commons-lang.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/commons-lang-3.18.0 https://gitbox.apache.org/repos/asf/commons-lang.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="userguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/userguide.html -->

<!-- page_index: 3 -->

<a id="userguide--user-guide-for-commons-lang"></a>

# User guide for Commons "Lang"

The User Guide has moved to the package [Javadoc](https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/package-summary.html).

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/building.html -->

<!-- page_index: 4 -->

<a id="building--overview"></a>

# Overview

Commons Lang uses [Maven](https://maven.apache.org).

You may also be interested in the upgrade notes:

- Upgrade from 2.6 to 3.0 - [Lang 3.0 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto3_0.html)
- Upgrade from 2.5 to 2.6 - [Lang 2.6 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_6.html)
- Upgrade from 2.4 to 2.5 - [Lang 2.5 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_5.html)
- Upgrade from 2.3 to 2.4 - [Lang 2.4 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_4.html)
- Upgrade from 2.2 to 2.3 - [Lang 2.3 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_3.html)
- Upgrade from 2.1 to 2.2 - [Lang 2.2 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_2.html)
- Upgrade from 2.0 to 2.1 - [Lang 2.1 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_1.html)
- Upgrade from 1.0 to 2.0 - [Lang 2.0 Release Notes](https://commons.apache.org/proper/commons-lang/upgradeto2_0.html)

<a id="building--maven-goals"></a>

# Maven Goals

To build a jar file, change into the root directory of Lang and run "mvn package".
The result will be in the "target" subdirectory.

To build the full website, run "mvn site".
The result will be in "target/site".
You must be online to successfully complete this target.

Further details can be found in the
[commons build instructions](https://commons.apache.org/building.html).

<a id="building--ant-goals"></a>

# Ant Goals

To build a jar file, change into the root directory of Lang and run "ant jar".
The result will be in the "target" subdirectory.

To build the Javadocs, run "ant javadoc".
The result will be in "target/docs/api".

---

<a id="proposal"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/proposal.html -->

<!-- page_index: 5 -->

<a id="proposal--proposal-for-lang-package"></a>

# Proposal for Lang Package

<a id="proposal--0-rationale"></a>

## (0) Rationale

The standard Java libraries fail to provide enough methods for
manipulation of its main components. The *Lang* Package provides
these extra methods. There are other classes which might justifiably
be included in java.lang someday, this package also provides for them.

<a id="proposal--1-scope-of-the-package"></a>

## (1) Scope of the Package

This proposal is to create a package of Java utility classes for the
classes that are in java.lang's hierarchy, or are considered to be so
standard as to justify existence in java.lang. The *Lang* Package
also applies to primitives and arrays.

<a id="proposal--1.5-interaction-with-other-packages"></a>

## (1.5) Interaction With Other Packages

*Lang* relies only on standard JDK 1.2 (or later) APIs for
production deployment. It utilizes the JUnit unit testing framework for
developing and executing unit tests, but this is of interest only to
developers of the component. Lang will be a dependency for
several existing components in the open source world.

No external configuration files are utilized.

<a id="proposal--2-initial-source-of-the-package"></a>

## (2) Initial Source of the Package

The initial classes came from the Commons.Util subproject.

The proposed package name for the new component is
`org.apache.commons.lang`.

<a id="proposal--3-required-jakarta-commons-resources"></a>

## (3) Required Jakarta-Commons Resources

- CVS Repository - New directory `lang` in the
  `jakarta-commons` CVS repository.
- Mailing List - Discussions will take place on the general
  *dev@commons.apache.org* mailing list. To help
  list subscribers identify messages of interest, it is suggested that
  the message subject of messages about this component be prefixed with
  [lang].
- Bugzilla - New component "Lang" under the "Commons" product
  category, with appropriate version identifiers as needed.
- Jyve FAQ - New category "commons-lang" (when available).

<a id="proposal--4-initial-committers"></a>

## (4) Initial Committers

The initial committers on the Lang component shall be as follows:

- Henri Yandell (bayard)
- Daniel Rall (dlr)
- Stephen Colebourne (scolebourne)

---

<a id="developerguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/developerguide.html -->

<!-- page_index: 6 -->

<a id="developerguide--developer-guide-for-commons-lang"></a>

# Developer guide for Commons "Lang"

<a id="developerguide--the-commons-lang-package"></a>

# The Commons *Lang* Package

<a id="developerguide--developers-guide"></a>

## Developers Guide

[[Introduction]](#developerguide--introduction)
[[Package Structure]](#developerguide--packagestructure)
[[Utility Classes]](#developerguide--utilityclasses)
[[Javadoc]](#developerguide--javadoc)
[[Building]](#developerguide--building)

<a id="developerguide--1.-introduction"></a>

### 1. INTRODUCTION

The *Lang* package contains a set of Java classes that extend
the basic JDK classes. This developer guide seeks to set
out rules for the naming of classes and methods within the package. The purpose
of this, as with all naming standards, is to improve the coherency and
consistency of the whole API.

The philosophy of the naming standards is to follow those of the JDK
if possible.

<a id="developerguide--2.-package-structure"></a>

### 2. PACKAGE STRUCTURE

The main package for Lang is `org.apache.commons.lang3`. Subpackages should
be created for each group of related items.

Each package should have a `package.html` file for javadoc. This should
describe the use of the package and its scope.

<a id="developerguide--3.-utility-classes"></a>

### 3. UTILITY CLASSES

Utility classes provide additional functionality around a class or interface.
Examples include StringUtils and SerializationUtils.

Each class shall follow the naming pattern XxxUtils where Xxx relates to the
class or interface that the utility services. Variations on a theme (`Integer`
as opposed to `Number`) should be dealt with in one Utils class where possible.
Each Utils class shall:

- be a single, static method based, class
- have a name consisting of the interface name plus 'Utils'
- deal with one class or interface and its variations (subclasses)
- provide methods that perform useful utility functions
- the class will not be final
- for null parameters, rather than throwing an Exception, consider performing a Null patterned concept, such as returning 0 or ""

A utility class can act as a factory for specific implementations of a class or
interface. In such cases the implementations should be non-public, static, inner classes
of the utility class. However, if warranted due to maintenance or other reasons, these
decorator classes may be moved to top-level classes in a subpackage. The
naming of such a subpackage should be discussed and agreed upon on the
developers mailing list.

If different overloaded variants of a method are desired, with the same method signature, it should not be indicated via a boolean argument, but via a more focused method name. Rather than replace(boolean repeat), replace and replaceAll, or replaceOnce and replace.

<a id="developerguide--4.-javadoc"></a>

### 4. JAVADOC

The Sun javadoc guidelines are the starting point for Lang. These points are
an extension to make it easier for users reading the generated
docs and developers with javadoc-popup capabilities from within their IDE.

<a id="developerguide--general"></a>

#### General

References to other objects, interfaces or methods use the @link-tag the
first time it is referenced in a class or interface. On the following
references always enclose it inside <code></code>.

References to `null`, `this`, `long`, `int`, `short`, `char`, `byte`, `double`, `float` and `boolean` should be enclosed
in <code></code>.

<a id="developerguide--classes-interfaces-methods"></a>

#### Classes/Interfaces/Methods

Use a short description of what the class/interface/method is used for, enclose with <p></p>.

A longer description about what the class/interface/method is used for
and if it is needed how it is done. If it is necessary include
description of the parameters, what they are used for and how. Enclose
with <p></p> where it is needed, try to divide into smaller parts (not
to small!) to enhance readability of the generated Javadoc.

If an example is needed enclose it with <pre></pre>.
It should be supported with an explanation within a normal paragraph.

<a id="developerguide--exception-throwing"></a>

#### Exception throwing

When throwing an exception to indicate a bad argument, always try to throw
IllegalArgumentException, even if the argument was null. Do not throw
NullPointerException. (Obviously, you should document what the code actually does!)

<a id="developerguide--deprecations"></a>

#### Deprecations

When deprecating a method or class include a clear reference to when the method will be deleted.
This should be of the form 'Method will be removed in Commons Lang 3.0.'.

<a id="developerguide--language-used-in-code-comments"></a>

#### Language used in code/comments

It has been decided to casually standardize on US-English.
To avoid misplaced jeers of 'americanisation', the people making this decision largely write in non-US-English.
However, it's not something to get worked up about. Lots of spelling differences will creep in all over.

<a id="developerguide--5.building"></a>

### 5.BUILDING

<a id="developerguide--building-a-release"></a>

#### Building a Release

The currently targeted version of Java is 1.6.

To build Lang:

|  | Tested JAR | Distribution | Site |
| --- | --- | --- | --- |
| Maven 2.x | `mvn package` | mvn assembly:assembly | mvn site |

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/project-info.html -->

<!-- page_index: 7 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Lang is a package of Java utility classes for the Java lang packages, classes that could be considered standard to justify their existence in java.lang. The code is tested using the latest revision of the JDK for supported LTS releases: 8, 11, 17, 21, and 25. See https://github.com/apache/commons-lang/blob/master/.github/workflows/maven.yml Please ensure your build environment is up-to-date and kindly report any build issues. Starting with Commons Lang 3.9, we target Java 8 and use those features. For advice on upgrading from 2.x to 3.x, see https://commons.apache.org/lang/article3\_0.html |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-lang/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-lang/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-lang/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-lang/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-lang/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-lang/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-lang/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/summary.html -->

<!-- page_index: 8 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Lang |
| Description | Apache Commons Lang is a package of Java utility classes for the Java lang packages, classes that could be considered standard to justify their existence in java.lang. The code is tested using the latest revision of the JDK for supported LTS releases: 8, 11, 17, 21, and 25. See https://github.com/apache/commons-lang/blob/master/.github/workflows/maven.yml Please ensure your build environment is up-to-date and kindly report any build issues. Starting with Commons Lang 3.9, we target Java 8 and use those features. For advice on upgrading from 2.x to 3.x, see https://commons.apache.org/lang/article3\_0.html |
| Homepage | [https://commons.apache.org/proper/commons-lang/](#index) |

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
| ArtifactId | commons-lang3 |
| Version | 3.21.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/team.html -->

<!-- page_index: 9 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | Java Developer | - |
| ![](assets/images/0c9a662be575728ba1c4921d3ba2f8ba_e830d37e6bc628cc.jpg) | scolebourne | Stephen Colebourne | [scolebourne@joda.org](mailto:scolebourne@joda.org) | - | SITA ATS Ltd | - | Java Developer | 0 |
| ![](assets/images/4156866f23b66d5ca7df5cdc86cb9a0e_9f809cc2576f8b8c.jpg) | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | scaswell | Steven Caswell | [stevencaswell@apache.org](mailto:stevencaswell@apache.org) | - | - | - | Java Developer | -5 |
| ![](assets/images/30f9094d5dbe2ce93f1a41afc9615b83_80d1f176546aba34.jpg) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | Java Developer | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | fredrik | Fredrik Westermarck | [-](mailto:) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | jcarman | James Carman | [jcarman@apache.org](mailto:jcarman@apache.org) | - | Carman Consulting, Inc. | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | niallp | Niall Pemberton | - | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | mbenson | Matt Benson | - | - | - | - | Java Developer | - |
| ![](assets/images/b57f757efea9e04ad3a5cb489499ec01_3ba133839b413215.jpg) | joehni | Joerg Schaible | [joerg.schaible@gmx.de](mailto:joerg.schaible@gmx.de) | - | - | - | Java Developer | +1 |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | oheger | Oliver Heger | [oheger@apache.org](mailto:oheger@apache.org) | - | - | - | Java Developer | +1 |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | pbenedict | Paul Benedict | [pbenedict@apache.org](mailto:pbenedict@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/cbfb61ee7f8641b2b6eaf22fed163b1e_2f06214da027cdde.jpg) | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/d26c6e21bb0ae329d807cc378ee0020b_acd90b0aaad9dbdc.jpg) | djones | Duncan Jones | [djones@apache.org](mailto:djones@apache.org) | - | - | - | Java Developer | 0 |
| ![](assets/images/00000000000000000000000000000000_1faf7a7d598c48b4.jpg) | lguibert | Loic Guibert | [lguibert@apache.org](mailto:lguibert@apache.org) | - | - | - | Java Developer | +4 |
| ![](assets/images/a010ac0916b6b9b10883e9359cfcd7f9_f360f6bbefa439cd.jpg) | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | - | - | Java Developer | -5 |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

C. Scott Ananian

Chris Audley

Stephane Bailliez

Michael Becke

Benjamin Bentmann

Ola Berg

Nathan Beyer

Stefan Bodewig

Janek Bogucki

Mike Bowler

Sean Brown

Alexander Day Chaffee

Al Chou

Greg Coladonato

Maarten Coene

Justin Couch

Michael Davey

Norm Deane

Morgan Delagrange

Ringo De Smet

Russel Dittmar

Steve Downey

Matthias Eichel

Christopher Elkins

Chris Feldhacker

Roland Foerther

Pete Gieser

Jason Gritman

Matthew Hawthorne

Michael Heuer

Chas Honton

Chris Hyzer

Paul Jack

Marc Johnson

Shaun Kalley

Tetsuya Kaneuchi

Nissim Karpenstein

Ed Korthof

Holger Krauth

Rafal Krupinski

Rafal Krzewski

David Leppik

Eli Lindsey

Sven Ludwig

Craig R. McClanahan

Rand McNeely

Hendrik Maryns

Dave Meikle

Nikolay Metchev

Kasper Nielsen

Tim O'Brien

Brian S O'Neill

Andrew C. Oliver

Alban Peignier

Moritz Petersen

Dmitri Plotnikov

Neeme Praks

Eric Pugh

Stephen Putman

Travis Reeder

Antony Riley

Valentin Rocher

Scott Sanders

James Sawle

Ralph Schaer

Henning P. Schmiedehausen

Sean Schofield

Robert Scholte

Reuben Sivan

Ville Skytta

David M. Sledge

Michael A. Smith

Jan Sorensen

Glen Stampoultzis

Scott Stanchfield

Jon S. Stevens

Sean C. Sullivan

Ashwin Suresh

Helge Tesgaard

Arun Mammen Thomas

Masato Tezuka

Daniel Trebbien

Jeff Varszegi

Chris Webb

Mario Winterer

Stepan Koltsov

Holger Hoffstatte

Derek C. Ashmore

Sebastien Riou

Allon Mureinik

Adam Hooper

Chris Karcher

Michael Osipov

Thiago Andrade

Jonathan Baker

Mikhail Mazursky

Fabian Lange

Michał Kordas

Felipe Adorno

Adrian Ber

Mark Dacek

Peter Verhas

Jin Xu

Arturo Bernal

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-lang/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-lang/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
