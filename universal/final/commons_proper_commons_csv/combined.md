# Project Information

## Navigation

- Commons CSV
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/index.html -->

<!-- page_index: 1 -->

<a id="index--using-apache-commons-csv"></a>

# Using Apache Commons CSV

Commons CSV reads and writes files in variations of the Comma Separated Value (CSV) format.

Read the documentation starting with the [Javadoc Overview](https://commons.apache.org/proper/commons-csv/apidocs/index.html).

<a id="index--documentation"></a>

# Documentation

An overview of the functionality is provided in the
[user guide](https://commons.apache.org/proper/commons-csv/apidocs/index.html).
Various [project reports](https://commons.apache.org/proper/commons-csv/project-reports.html) are also available.

The Javadoc API documents are available online:

- [Javadoc current](https://commons.apache.org/proper/commons-csv/apidocs/index.html)
- [Javadoc archives](https://javadoc.io/doc/org.apache.commons/commons-csv/)

The [git repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-csv.git).

<a id="index--releases"></a>

# Releases

- [Download Apache Commons CSV current (mirrors)](https://commons.apache.org/csv/download_csv.cgi), requires Java 8 or above
- [Download Apache Commons CSV archived releases](https://archive.apache.org/dist/commons/csv/)

See the
[Download Page](https://commons.apache.org/csv/download_csv.cgi)
for the latest releases.

[Release History](https://commons.apache.org/proper/commons-csv/changes.html) are also available.

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/csv/)

For dependency access methods, see [Dependency Information](https://commons.apache.org/proper/commons-csv/dependency-info.html)

<a id="index--building-from-sources"></a>

# Building from sources

The latest code can be checked out from our git repository at <https://gitbox.apache.org/repos/asf/commons-csv.git>.
You can build the component using Apache Maven using `mvn clean package`.

<a id="index--getting-involved"></a>

# Getting Involved

The [commons developer mailing list](https://commons.apache.org/proper/commons-csv/mail-lists.html) is the main channel of communication for contributors. Please remember that the lists are shared between all commons components, so prefix your email by [csv].

You can also peruse [JIRA](https://commons.apache.org/proper/commons-csv/issue-tracking.html). Specific links of interest for JIRA are:

- Ideas looking for code: [Patch Needed](https://issues.apache.org/jira/issues/?jql=project%20%3D%20CSV%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20%22Patch%20Needed%22)
- Issues with patches, looking for reviews: [Review Patch](https://issues.apache.org/jira/issues/?jql=project%20%3D%20CSV%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20Review)

Alternatively you can go through the *Needs Work* tags in the [TagList report](https://commons.apache.org/proper/commons-csv/taglist.html).

If you'd like to offer up pull requests via GitHub rather than applying patches to JIRA, we have a [GitHub mirror](https://github.com/apache/commons-csv/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-csv/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [csv].

Bug reports and enhancements are also welcomed via the [JIRA](https://commons.apache.org/proper/commons-csv/issue-tracking.html) issue tracker.
Please read the instructions carefully.

<a id="index--about-commons-csv"></a>

# About Commons CSV

Commons CSV was started to unify a common and simple interface for reading and writing CSV files under an ASL license. It has been bootstrapped by a code donation from Netcetera in Switzerland. There are three pre-existing BSD compatible CSV parsers which this component will hopefully make redundant (authors willing):

- [Skife CSV](http://kasparov.skife.org/csv/)
- [Open CSV](https://opencsv.sourceforge.net/)
- Genjava CSV

In addition to the code from Netcetera (org.apache.commons.csv), Martin van den Bemt has added an additional writer API.

Other CSV implementations:

- [Super CSV](https://super-csv.github.io/super-csv/index.html)

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-csv.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-csv.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-csv.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/security.html -->

<!-- page_index: 3 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-csv/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

None.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/project-info.html -->

<!-- page_index: 4 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons CSV library provides a simple interface for reading and writing CSV files of various types. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-csv/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-csv/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-csv/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-csv/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-csv/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-csv/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-csv/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/summary.html -->

<!-- page_index: 5 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons CSV |
| Description | The Apache Commons CSV library provides a simple interface for reading and writing CSV files of various types. |
| Homepage | [https://commons.apache.org/proper/commons-csv/](#index) |

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
| ArtifactId | commons-csv |
| Version | 1.14.2-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/team.html -->

<!-- page_index: 6 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/4156866f23b66d5ca7df5cdc86cb9a0e_c37d873d8a2e11f2.jpg) | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1add3111cf5acc1c.jpg) | mvdb | Martin van den Bemt | [mvdb@apache.org](mailto:mvdb@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_1add3111cf5acc1c.jpg) | yonik | Yonik Seeley | [yonik@apache.org](mailto:yonik@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/8304c64641badd4218a89a5f97d2ae86_060b1cb028ffb53c.jpg) | ebourg | Emmanuel Bourg | [ebourg@apache.org](mailto:ebourg@apache.org) | - | Apache | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/cbfb61ee7f8641b2b6eaf22fed163b1e_0fe7d74e5d147642.jpg) | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/a010ac0916b6b9b10883e9359cfcd7f9_a8dfd1169a0c1e32.jpg) | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | The Apache Software Foundation | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Bob Smith

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/ci-management.html -->

<!-- page_index: 7 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-csv/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
