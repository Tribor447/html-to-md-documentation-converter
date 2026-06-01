# Project Information

## Navigation

- [Commons Validator](#index)
  - [About](#index)
  - [Sources](#scm)
- Documentation
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

<!-- source_url: https://commons.apache.org/proper/commons-validator/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-validator"></a>

# Commons Validator

Apache Commons Validator helps you with common issues when receiving data either electronically or from
user input and verifying the integrity of that data. This work is
repetitive and becomes even more complicated when different sets
of validation rules need to be applied to the same set of data based
on locale. Error messages may also vary by locale.
This package addresses some of these issues to
speed development and maintenance of validation rules.

<a id="index--releases"></a>

# Releases

See the [Downloads](https://commons.apache.org/validator/download_validator.cgi)
page for current/previous releases.
For details of whats new in each version see the [Release Notes](https://commons.apache.org/proper/commons-validator/changes.html).
[Community Notes](https://wiki.apache.org/commons/ValidatorReleaseNotes) on
release are maintained on the [Apache Commons Wiki](https://wiki.apache.org/commons/).

<a id="index--overview"></a>

# Overview

<a id="index--features"></a>

## Features

Validator provides two distinct sets of functionality:

1. A configurable (typically XML) validation engine
2. Reusable "primitive" validation methods

Your validation methods are plugged into the engine and
executed against your data. Often, these methods use
resources specific to one application or framework so Commons
Validator doesn't directly provide pluggable validator actions.
However, it does have a set of common validation methods
(email addresses, dates, URLs, etc.) that help in creating
pluggable actions.

<a id="index--usage"></a>

## Usage

In order to use the Validator, the following basic steps are required:

- Create a new instance of the
  `org.apache.commons.validator.Validator` class. Currently
  Validator instances may be safely reused if the current
  ValidatorResources are the same, as long as you have completed any
  previous validation, and you do not try to utilize a particular
  Validator instance from more than one thread at a time.
- Add any resources needed to perform the validations, such as the
  JavaBean to validate.
- Call the validate method on
  `org.apache.commons.validator.Validator`.

<a id="index--documentation"></a>

## Documentation

The package Javadoc has useful information:

- [Validator Framework](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/package-summary.html#package_description)
- [Routines package](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/package-summary.html#package_description)

See the [Git repository](#scm) for the latest source code.

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-validator/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [validator].

Issues may be reported via [ASF JIRA](https://commons.apache.org/proper/commons-validator/issue-tracking.html).

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-validator/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-validator.git/commons-validator
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch rel/commons-validator-1.10.2 https://gitbox.apache.org/repos/asf/commons-validator.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/commons-validator-1.10.2 https://gitbox.apache.org/repos/asf/commons-validator.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-validator/building.html -->

<!-- page_index: 3 -->

<a id="building--overview"></a>

# Overview

Commons Validator uses [Maven](https://maven.apache.org) or
[Ant](https://ant.apache.org) as a build system.

<a id="building--maven-goals"></a>

# Maven Goals

To build a jar file, change into Validator's root directory and run
**`maven jar`**.
The result will be in the "target" subdirectory.

To build the Javadocs, run **`maven javadoc`**.
The result will be in "target/docs/apidocs".

To build the full website, run **`maven site`**.
The result will be in "target/docs".

Further details can be found in the
[commons build instructions](https://commons.apache.org/building.html).

<a id="building--nightly-builds"></a>

# Nightly Builds

[Nightly Builds](https://people.apache.org/builds/commons/nightly/commons-validator/)
are built once a day from the current SVN HEAD. These are provided purely for test purposes and are **NOT
official releases** of the Apache Software Foundation - Released versions of Commons Validator are
available [here](https://commons.apache.org/validator/download_validator.cgi).

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-validator/project-info.html -->

<!-- page_index: 4 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Validator provides the building blocks for both client-side and server-side data validation. It may be used standalone or with a framework like Struts. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-validator/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-validator/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-validator/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-validator/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-validator/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-validator/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-validator/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-validator/summary.html -->

<!-- page_index: 5 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Validator |
| Description | Apache Commons Validator provides the building blocks for both client-side and server-side data validation. It may be used standalone or with a framework like Struts. |
| Homepage | [https://commons.apache.org/proper/commons-validator/](#index) |

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
| GroupId | commons-validator |
| ArtifactId | commons-validator |
| Version | 1.10.2-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-validator/team.html -->

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
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | mrdon | Don Brown | [mrdon@apache.org](mailto:mrdon@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | martinc | Martin Cooper | [martinc@apache.org](mailto:martinc@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | dgraham | David Graham | [dgraham@apache.org](mailto:dgraham@apache.org) | - | - | - | - | - |
| ![](assets/images/87a93952bc3587bbed2ab94ae88342af_fa9e38d6695cd4fb.jpg) | husted | Ted Husted | [husted@apache.org](mailto:husted@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | rleland | Rob Leland | [rleland at apache.org](mailto:rleland at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | craigmcc | Craig McClanahan | [craigmcc@apache.org](mailto:craigmcc@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | jmitchell | James Mitchell | [jmitchell NOSPAM apache.org](mailto:jmitchell NOSPAM apache.org) | - | EdgeTech, Inc | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | niallp | Niall Pemberton | - | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | turner | James Turner | [turner@apache.org](mailto:turner@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | dwinterfeldt | David Winterfeldt | [dwinterfeldt@apache.org](mailto:dwinterfeldt@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | bayard | Henri Yandell | - | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | bspeakmon | Ben Speakmon | - | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | nick | Nick Burch | - | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | simonetripodi | SimoneTripodi | - | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_589f9ef9d6f91ff6.jpg) | britter | Benedikt Ritter | - | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Makoto Uchino

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-validator/ci-management.html -->

<!-- page_index: 7 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-validator/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
