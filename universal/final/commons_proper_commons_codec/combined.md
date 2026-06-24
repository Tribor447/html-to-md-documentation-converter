# Project Information

## Navigation

- Commons Codec
  - [About](#index)
  - [Sources](#scm)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-codec/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-codec"></a>

# Apache Commons Codec

Apache Commons Codec (TM) software provides implementations of common encoders and decoders
such as Base64, Hex, Phonetic and URLs.

<a id="index--impetus"></a>

# Impetus

Codec was formed as an attempt to focus development effort on one
definitive implementation of the Base64 encoder. At the time of
Codec's proposal, there were approximately 34 different Java
classes that dealt with Base64 encoding spread over the
Foundation's CVS repository. Developers in the Jakarta Tomcat
project had implemented an original version of the Base64 codec
which had been copied by the Commons HttpClient and Apache XML
project's XML-RPC subproject. After almost one year, the two
forked versions of Base64 had significantly diverged from one
another. XML-RPC had applied numerous fixes and patches which
were not applied to the Commons HttpClient Base64. Different
subprojects had differing implementations at various levels
of compliance with the [RFC 2045](https://www.ietf.org/rfc/rfc2045).

Out of that confusing duplication of effort sprang this simple
attempt to encourage code reuse among various projects. While
this package contains an abstract framework for the creation of
encoders and decoders, Codec itself is primarily focused on
providing functional utilities for working with common encodings.

<a id="index--documentation"></a>

# Documentation

An overview of the functionality is provided in the
[user guide](https://commons.apache.org/proper/commons-codec/userguide.html).
Various [project reports](https://commons.apache.org/proper/commons-codec/project-reports.html) are also available.

The Javadoc API documents are available online:

- [Javadoc latest version](https://commons.apache.org/proper/commons-codec/apidocs/index.html)
- [Javadoc archive](https://javadoc.io/doc/commons-codec/commons-codec)

The [Git repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-codec.git).

<a id="index--releases"></a>

# Releases

- [Download latest version (mirrors)](https://commons.apache.org/codec/download_codec.cgi); requires Java 8 or above
- [Download archive](https://archive.apache.org/dist/commons/codec/)

See the
[Download Page](https://commons.apache.org/codec/download_codec.cgi)
for the latest releases.

[Change reports](https://commons.apache.org/proper/commons-codec/changes.html) are also available.

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/codec/)

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-codec/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [codec].

Issues may be reported via [ASF JIRA](https://commons.apache.org/proper/commons-codec/issue-tracking.html).

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-codec/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://github.com/apache/commons-codec
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch rel/commons-io-2.20.0 https://gitbox.apache.org/repos/asf/commons-codec
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/commons-io-2.20.0 https://gitbox.apache.org/repos/asf/commons-codec
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-codec/project-info.html -->

<!-- page_index: 3 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons Codec component contains encoders and decoders for formats such as Base16, Base32, Base64, digest, and Hexadecimal. In addition to these widely used encoders and decoders, the codec package also maintains a collection of phonetic encoding utilities. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-codec/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-codec/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-codec/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-codec/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-codec/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-codec/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-codec/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-codec/summary.html -->

<!-- page_index: 4 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Codec |
| Description | The Apache Commons Codec component contains encoders and decoders for formats such as Base16, Base32, Base64, digest, and Hexadecimal. In addition to these widely used encoders and decoders, the codec package also maintains a collection of phonetic encoding utilities. |
| Homepage | [https://commons.apache.org/proper/commons-codec/](#index) |

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
| GroupId | commons-codec |
| ArtifactId | commons-codec |
| Version | 1.22.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-codec/team.html -->

<!-- page_index: 5 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/4156866f23b66d5ca7df5cdc86cb9a0e_2712f661aebc2bc3.jpg) | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | - | - | - | - |
| ![](assets/images/0b185e68b9933eccb52d90eda3097986_df4535b2cba45185.jpg) | tobrien | Tim OBrien | [tobrien@apache.org](mailto:tobrien@apache.org) | - | - | - | - | -6 |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | sanders | Scott Sanders | [sanders@totalsync.com](mailto:sanders@totalsync.com) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | rwaldhoff | Rodney Waldhoff | [rwaldhoff@apache.org](mailto:rwaldhoff@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | jon | Jon S. Stevens | [jon@collab.net](mailto:jon@collab.net) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | dgraham | David Graham | [dgraham@apache.org](mailto:dgraham@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | julius | Julius Davies | [julius@apache.org](mailto:julius@apache.org) | - | - | <https://juliusdavies.ca/> | - | -8 |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | - | - | - | - |
| ![](assets/images/a010ac0916b6b9b10883e9359cfcd7f9_eb738dc6e924f5b3.jpg) | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | - | - | - | - |
| ![](assets/images/702e018a90dc063767ecaa04a8336eb1_26ac772eafc3b281.jpg) | mattsicker | Matt Sicker | [mattsicker@apache.org](mailto:mattsicker@apache.org) | <https://musigma.blog/> | - | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization | Roles |
| --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Christopher O'Brien | [siege@preoccupied.net](mailto:siege@preoccupied.net) | - | hex, md5, architecture |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Martin Redington | - | - | Representing xml-rpc |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Jeffery Dever | - | - | Representing http-client |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Steve Zimmermann | [steve.zimmermann@heii.com](mailto:steve.zimmermann@heii.com) | - | Documentation |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Benjamin Walstrum | [ben@walstrum.com](mailto:ben@walstrum.com) | - | - |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Oleg Kalnichevski | [oleg@ural.ru](mailto:oleg@ural.ru) | - | Representing http-client |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Dave Dribin | [apache@dave.dribin.org](mailto:apache@dave.dribin.org) | - | DigestUtil |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Alex Karasulu | [aok123 at bellsouth.net](mailto:aok123 at bellsouth.net) | - | Submitted Binary class and test |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Matthew Inger | [mattinger at yahoo.com](mailto:mattinger at yahoo.com) | - | Submitted DIFFERENCE algorithm for Soundex and RefinedSoundex |
| ![](assets/images/468ff229320651ab6f58f746ea6642c1_9ebb15cf4ddc2fa2.jpg) | Jochen Wiedmann | [jochen@apache.org](mailto:jochen@apache.org) | - | Base64 code [CODEC-69] |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Sebastian Bazley | [sebb@apache.org](mailto:sebb@apache.org) | - | Streaming Base64 |
| ![](assets/images/334c26bcec0c77d7280b1b6bbaca952c_0f715477a5241aae.jpg) | Matthew Pocock | [turingatemyhamster@gmail.com](mailto:turingatemyhamster@gmail.com) | - | Beider-Morse phonetic matching |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Colm Rice | [colm\_rice at hotmail dot com](mailto:colm_rice at hotmail dot com) | - | Submitted Match Rating Approach (MRA) phonetic encoder and tests [CODEC-161] |
| ![](assets/images/00000000000000000000000000000000_6d24364568d35fd9.jpg) | Adam Retter | - | Evolved Binary | Base16 Input and Output Streams |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-codec/ci-management.html -->

<!-- page_index: 6 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-codec/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
