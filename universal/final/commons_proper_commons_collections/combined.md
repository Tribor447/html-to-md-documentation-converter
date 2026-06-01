# Project Information

## Navigation

- [Commons Collections](#index)
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Users guide](#userguide)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- [General Information](#security)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-collections"></a>

# Commons Collections

The [Java Collections Framework](https://docs.oracle.com/javase/tutorial/collections/)
was a major addition in Java 1.2.
It added many powerful data structures that accelerate development of most significant Java applications.
Since that time it has become the recognised standard for collection handling in Java.

Commons-Collections seek to build upon the JDK classes by providing new interfaces, implementations and utilities.
There are many features, including:

- Bag interface for collections that have a number of copies of each object
- BidiMap interface for maps that can be looked up from value to key as well and key to value
- [Bloom filter](https://commons.apache.org/proper/commons-collections/bloomFilters.html) classes and interfaces
- MapIterator interface to provide simple and quick iteration over maps
- Transforming decorators that alter each object as it is added to the collection
- Composite collections that make multiple collections look like one
- Ordered maps and sets that retain the order elements are added in, including an LRU based map
- Reference map that allows keys and/or values to be garbage collected under close control
- Many comparator implementations
- Many iterator implementations
- Adapter classes from array and enumerations to collections
- Utilities to test or create typical set-theory properties of collections such as union, intersection, and closure

<a id="index--documentation"></a>

# Documentation

A getting started [User's Guide](#userguide) is available
as are various [project reports](https://commons.apache.org/proper/commons-collections/project-reports.html).

The Javadoc API documents are available online:

- The [current release](https://commons.apache.org/proper/commons-collections/apidocs/index.html)
- The latest 3.x release - [version 3.2.2](https://commons.apache.org/proper/commons-collections/javadocs/api-3.2.2/index.html)
- The latest 2.x release - [version 2.1.1](https://commons.apache.org/proper/commons-collections/javadocs/api-2.1.1/index.html)

The [source repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-collections.git), and we have a mirror
on [GitHub](https://github.com/apache/commons-collections).

<a id="index--releases"></a>

# Releases

The latest version is available:
[Download now!](https://commons.apache.org/collections/download_collections.cgi)

This requires Java 8 or later, see also the [release notes](https://commons.apache.org/changes.html).

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/collections/)

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-collections/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [collections].

Issues may be reported via [ASF JIRA](https://commons.apache.org/proper/commons-collections/issue-tracking.html).
Please read the instructions carefully to submit a useful bug report or enhancement request.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-collections.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-collections.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-collections.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/security.html -->

<!-- page_index: 3 -->

<a id="security--general-information"></a>

# General Information

For information about reporting or asking questions about
security problems, please see the [security page
of the Commons project](https://commons.apache.org/security.html).

<a id="security--apache-commons-collections-security-vulnerabilities"></a>

# Apache Commons Collections Security Vulnerabilities

This page lists all security vulnerabilities fixed in
released versions of Apache Commons Collections. Each
vulnerability is given a security impact rating by the
development team - please note that this rating may vary from
platform to platform. We also list the versions of Commons
Collections the flaw is known to affect, and where a flaw has not
been verified list the version with a question mark.

Please note that binary patches are never provided. If you
need to apply a source code patch, use the building
instructions for the Commons Collections version that you are
using.

If you need help on building Commons Collections or other help
on following the instructions to mitigate the known
vulnerabilities listed here, please send your questions to the
public [Collections Users mailing
list](https://commons.apache.org/proper/commons-collections/mail-lists.html).

If you have encountered an unlisted security vulnerability
or other unexpected behavior that has security impact, or if
the descriptions here are incomplete, please report them
privately to the Apache Security Team. Thank you.

<a id="security--fixed-in-apache-commons-collections-3.2.2-and-4.1"></a>

## Fixed in Apache Commons Collections 3.2.2 and 4.1

**High: Remote Code Execution during object de-serialization**

The Apache Commons Collections library contains various classes
in the "functor" package which are serializable and use reflection.
This can be exploited for remote code execution attacks by injecting
specially crafted objects to applications that de-serialize
java objects from untrusted sources and have the Apache Commons Collections
library in their classpath and do not perform any kind of input
validation.

The implemented fix can be tracked via its related issue
[COLLECTIONS-580](https://issues.apache.org/jira/browse/COLLECTIONS-580):

- **3.2.2**: de-serialization of unsafe classes in the functor package
  will trigger an "UnsupportedOperationException" by default. In order to re-enable
  the previous behavior, the system property
  "org.apache.commons.collections.enableUnsafeSerialization" has to be set to "true".
- **4.1**: de-serialization support for unsafe classes in the functor package
  has been completely removed (unsafe classes do not implement Serializable anymore).

The potential exploit was first presented at AppSecCali2015 [3] on 28 January 2015 by
Gabriel Lawrence and Chris Frohoff. Based on these exploits, Stephen Breen published
on 06 November 2015 attack scenarios [4] for various products like WebSphere, JBoss, Jenkins, WebLogic, and OpenNMS. The Security team was **not** informed about these security
problems prior to their publication. No CVE id was assigned for the Apache Commons
Collections library, please refer to [1] or [2] for more information about the general
problem with Java serialization.

Affects: 3.0 - 4.0

Related links:

1. Vulnerability Report for Oracle Weblogic Server:
   [CVE-2015-4852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4852)
2. Vulnerability Report for Red Hat JBoss products:
   [CVE-2015-7501](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7501)
   ([Red Hat Portal](https://access.redhat.com/security/cve/cve-2015-7501))
3. Apache Commons
   [statement](https://blogs.apache.org/foundation/entry/apache_commons_statement_to_widespread)
   to widespread Java object de-serialization vulnerability
4. [Presentation](https://www.slideshare.net/frohoff1/appseccali-2015-marshalling-pickles) @ AppSecCali2015 by Lawrence and Frohoff
5. [Attack scenarios](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/)
   for various products by Stephen Breen

<a id="security--errors-and-omissions"></a>

# Errors and Omissions

Please report any errors or omissions to [the dev mailing list](https://commons.apache.org/proper/commons-collections/mail-lists.html).

---

<a id="userguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/userguide.html -->

<!-- page_index: 4 -->

<a id="userguide--user-guide"></a>

# User guide

Commons-Collections provides a large number of classes to aid day to day programming.
This document highlights some key features to get you started.

- [Utilities](#userguide--utilities) for the standard collections.
- [Maps](#userguide--maps)
  - [Map Iteration](#userguide--map.2520iteration)
  - [Ordered Maps](#userguide--ordered.2520maps)
  - [Bidirectional Maps](#userguide--bidirectional.2520maps)
- [Bags](#userguide--bags)
- [Bloom filters (starting in 4.5.0)](https://commons.apache.org/proper/commons-collections/bloomFilters.html)

<a id="userguide--note-on-synchronization"></a>

## Note On Synchronization

Commons-collections uses a design approach to synchronization similar
to the standard Java collections. The majority of the various implementations
of collections, maps and bags are not thread safe without additional
synchronization. The appropriate `synchronizeXXX` method on `Collections` is one way that these implementations can be synchronized for use in a
multithreaded application.

The class level javadocs should indicate whether a particular
implementation is safe for multithreaded access without additional
synchronization. Where there is no explicit indication that the implementation
is thread safe then it should be assumed that synchronization is required.
Please report the missing documentation to the commons development team.

<a id="userguide--utilities"></a>

# Utilities

A Utility class is provided for each major collection interface.
Thus, the `Set` and `SortedSet` interfaces are provided for by `SetUtils.`
These classes provide useful methods for working with that collection type.

The most methods are found on the two 'root' collection utility classes -
`CollectionUtils` and `MapUtils.`
As all other collection interfaces extend `Collection` or `Map` these utilities can be used widely.
They include intersection, counting, iteration, functor and typecasting operations amongst others.
The utility classes also provide access to collection decorator classes in a way similar to the JDK `Collections` class.

<a id="userguide--maps"></a>

# Maps

<a id="userguide--map-iteration"></a>

## Map Iteration

The JDK `Map` interface always suffered from being difficult to iterate over.
API users are forced to either iterate over an EntrySet or over the KeySet.
Commons-Collections now provides a new interface - `MapIterator` that allows simple iteration over maps.

```

IterableMap map = new HashedMap();
MapIterator it = map.mapIterator();
while (it.hasNext()) {
  Object key = it.next();
  Object value = it.getValue();

  it.setValue(newValue);
}
```

<a id="userguide--ordered-maps"></a>

## Ordered Maps

A new interface is provided for maps that have an order but are not sorted - `OrderedMap.`
Two implementations are provided - `LinkedMap` and `ListOrderedMap` (a decorator).
This interface supports the map iterator, and also allows iteration both forwards and backwards through the map.

```

OrderedMap map = new LinkedMap();
map.put("FIVE", "5");
map.put("SIX", "6");
map.put("SEVEN", "7");
map.firstKey();  // returns "FIVE"
map.nextKey("FIVE");  // returns "SIX"
map.nextKey("SIX");  // returns "SEVEN"
```

<a id="userguide--bidirectional-maps"></a>

## Bidirectional Maps

A new interface hierarchy has been added to support bidirectional maps - `BidiMap.`
These represent maps where the key can lookup the value and the value can look up the key with equal ease.

```

BidiMap bidi = new TreeBidiMap();
bidi.put("SIX", "6");
bidi.get("SIX");  // returns "6"
bidi.getKey("6");  // returns "SIX"
bidi.removeValue("6");  // removes the mapping
BidiMap inverse = bidi.inverseBidiMap();  // returns a map with keys and values swapped
```

Additional interfaces are provided for ordered and sorted bidirectional maps.
Implementations are provided for each bidirectional map type.

<a id="userguide--bags"></a>

# Bags

A new interface hierarchy has been added to support bags - `Bag.`
These represent collections where a certain number of copies of each element is held.

```

Bag bag = new HashBag();
bag.add("ONE", 6);  // add 6 copies of "ONE"
bag.remove("ONE", 2);  // removes 2 copies of "ONE"
bag.getCount("ONE");  // returns 4, the number of copies in the bag (6 - 2)
```

Implementations are provided for both unsorted and sorted Bags.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons Collections package contains types that extend and augment the Java Collections Framework. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-collections/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-collections/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-collections/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-collections/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-collections/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-collections/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-collections/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/summary.html -->

<!-- page_index: 6 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Collections |
| Description | The Apache Commons Collections package contains types that extend and augment the Java Collections Framework. |
| Homepage | [https://commons.apache.org/proper/commons-collections/](#index) |

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
| ArtifactId | commons-collections4 |
| Version | 4.5.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/team.html -->

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
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | mbenson | Matt Benson | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | jcarman | James Carman | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | rdonkin | Robert Burrell Donkin | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | morgand | Morgan Delagrange | - | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | matth | Matthew Hawthorne | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | dlaha | Dipanjan Laha | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | geirm | Geir Magnusson | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | luc | Luc Maisonobe | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | craigmcc | Craig McClanahan | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | tn | Thomas Neidhart | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | adriannistor | Adrian Nistor | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | amamment | Arun M. Thomas | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | rwaldhoff | Rodney Waldhoff | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | bayard | Henri Yandell | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | chtompki | Rob Tompkins | - | - | - | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Rafael U. C. Afonso

Max Rydahl Andersen

Avalon

Federico Barbieri

Jeffrey Barnes

Nicola Ken Barozzi

Arron Bates

Sebastian Bazley

Benjamin Bentmann

Ola Berg

Sam Berlin

Christopher Berry

Nathan Beyer

Rune Peter Bjørnstad

Janek Bogucki

Maarten Brak

Dave Bryson

Chuck Burdick

Julien Buret

Josh Cain

Jonathan Carlson

Ram Chidambaram

Steve Clark

Benoit Corne

Eric Crampton

Dimiter Dimitrov

Peter Donald

Steve Downey

Rich Dougherty

Tom Dunham

Stefano Fornari

Andrew Freeman

Gerhard Froehlich

Goran Hacek

David Hay

Mario Ivankovits

Paul Jack

Eric Johnson

Kent Johnson

Marc Johnson

Roger Kapsi

Nissim Karpenstein

Shinobu Kawai

Stephen Kestle

Mohan Kishore

Simon Kitching

Thomas Knych

Serge Knystautas

Peter KoBek

Jordan Krey

Olaf Krische

Guilhem Lavaux

Paul Legato

David Leppik

Berin Loritsch

Hendrik Maryns

Stefano Mazzocchi

Brian McCallister

David Meikle

Steven Melzer

Leon Messerschmidt

Mauricio S. Moura

Kasper Nielsen

Stanislaw Osinski

Alban Peignier

Mike Pettypiece

Steve Phelps

Ilkka Priha

Jonas Van Poucke

Will Pugh

Herve Quiroz

Daniel Rall

Robert Ribnitz

Huw Roberts

Henning P. Schmiedehausen

Joerg Schmuecker

Howard Lewis Ship

Joe Raysa

Jeff Rodriguez

Ashwin S

Jordane Sarda

Thomas Schapitz

Jon Schewe

Andreas Schlosser

Christian Siefkes

Michael Smith

Stephen Smith

Jan Sorensen

Jon S. Stevens

James Strachan

Leo Sutic

Radford Tam

Chris Tilden

Neil O'Toole

Jeff Turner

Kazuya Ujihara

Thomas Vahrst

Jeff Varszegi

Ralph Wagner

Hollis Waite

David Weinrich

Dieter Wimberger

Serhiy Yevtushenko

Sai Zhang

Jason van Zyl

Geoff Schoeman

Goncalo Marques

Vamsi Kavuri

Claude Warren

Chen Guoping

Stefano Cordio

Arturo Bernal

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-collections/ci-management.html -->

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
