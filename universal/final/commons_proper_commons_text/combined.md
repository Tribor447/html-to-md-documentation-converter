# Project Information

## Navigation

- [Commons Text](#index)
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Proposal](#proposal)
  - [Developer Guide](#developerguide)
  - [Source Repository](#scm)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-text"></a>

# Commons Text

Apache Commons Text is a library focused on algorithms working on strings.

<a id="index--documentation"></a>

# Documentation

We provide documentation in the form of a [User Guide](https://commons.apache.org/apidocs/index.html), [Javadoc](https://commons.apache.org/proper/commons-text/javadocs/apidocs/index.html), and [Project Reports](https://commons.apache.org/proper/commons-text/project-reports.html).

The [Git repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-text.git), or you can browse/contribute via [GitHub](https://github.com/apache/commons-text).

<a id="index--release-information"></a>

# Release Information

Download the latest release from dependency-info.html

Alternatively, you can use a [build tool dependency](https://commons.apache.org/proper/commons-text/dependency-info.html).

For information on previous releases see the [Release History](https://commons.apache.org/proper/commons-text/changes.html), and to download previous releases see the [Commons Text Archive](https://archive.apache.org/dist/commons/text/).

<a id="index--getting-involved"></a>

# Getting Involved

The [commons developer mailing list](https://commons.apache.org/proper/commons-text/mail-lists.html) is the main channel of communication for contributors. Please remember that the lists are shared between all commons components, so prefix your email by [text].

You can also peruse [JIRA](#issue-tracking). Specific links of interest for JIRA are:

- Ideas looking for code: [Patch Needed](https://issues.apache.org/jira/issues/?jql=project%20%3D%20TEXT%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20%22Patch%20Needed%22%20ORDER%20BY%20priority%20DESC)
- Issues with patches, looking for reviews: [Review Patch](https://issues.apache.org/jira/issues/?jql=fixVersion%20%3D%20%22Review%20Patch%22%20AND%20project%20%3D%20TEXT%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC)

Alternatively you can go through the *Needs Work* tags in the [TagList report](https://commons.apache.org/proper/commons-text/taglist.html).

If you'd like to offer up pull requests via GitHub rather than applying patches to JIRA, we have a [GitHub mirror](https://github.com/apache/commons-text/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-text/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [text].

Bug reports and enhancements are also welcomed via the [JIRA](#issue-tracking) issue tracker.
Please read the instructions carefully.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-text.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-text
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-text
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/security.html -->

<!-- page_index: 3 -->

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

For information about reporting or asking questions about
security, please see the
[security page](https://commons.apache.org/security.html)
of the Apache Commons project.

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the
building instructions for the component version that you are using.

If you need help on building this component or other help on following the instructions to
mitigate the
known vulnerabilities listed here, please send your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-text/mail-lists.html)
.

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security
impact, or if the descriptions here are incomplete, please report them privately to the Apache Security
Team. Thank you.

<a id="security--cve-2022-42889-prior-to-1.10.0-rce-when-applied-to-untrusted-input"></a>

## CVE-2022-42889 prior to 1.10.0, RCE when applied to untrusted input

On 2022-10-13, the Apache Commons Text team disclosed
[CVE-2022-42889](https://www.cve.org/CVERecord?id=CVE-2022-42889)
. Key takeaways:

- If you rely on software that uses a version of commons-text prior to 1.10.0, you are likely
  still not vulnerable: only if this software uses the
  `StringSubstitutor`
  API without properly sanitizing any untrusted input.
- If your own software uses commons-text, double-check whether it uses the
  `StringSubstitutor`
  API without properly sanitizing any untrusted input. If so, an update to 1.10.0 could be a
  quick workaround, but the recommended solution is to also properly validate and sanitize any
  untrusted input.

Apache Commons Text is a low-level library for performing various text operations, such as escaping, calculating string
differences, and substituting placeholders in the text with values looked up through interpolators.
When using the string substitution feature, some of the available interpolators can trigger network
access or code execution. This is intended, but it also means an application that includes user
input in the string passed to the substitution without properly sanitizing it would allow an
attacker to trigger those interpolators.

For that reason the Apache Commons Text team have decided to update the configuration to be more
"secure by default", so that the impact of a failure to validate inputs is mitigated and will not
give an attacker access to these interpolators. However, it is still recommended that users treat
untrusted input with care.

We're not currently aware of any applications that pass untrusted input to the substitutor and thus would have been
impacted by this problem prior to Apache Commons Text 1.10.0.

This issue is different from
[Log4Shell (CVE-2021-44228)](https://logging.apache.org/log4j/2.x/security.html#log4j-2.15.0)
because in Log4Shell, string interpolation was possible from the log message body, which commonly
contains untrusted input. In the Apache Common Text issue, the relevant method is explicitly
intended and clearly documented to perform string interpolation, so it is much less likely that
applications would inadvertently pass in untrusted input without proper validation.

Credit: this issue was reported independently by Ruilin and by
[@pwntester (Alvaro Muñoz)](https://github.com/pwntester)
of the
[GitHub Security Lab team](https://securitylab.github.com)
. Thank you!

References:

- [Announcement on dev@commons.apache.org](https://lists.apache.org/thread/n2bd4vdsgkqh2tm14l1wyc3jyol7s1om)
- [Announcement on oss-security](https://www.openwall.com/lists/oss-security/2022/10/13/4)
- [Advisory on cve.org](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42889)
- [GHSL advisory](https://securitylab.github.com/advisories/GHSL-2022-018_Apache_Commons_Text/)

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/issue-tracking.html -->

<!-- page_index: 4 -->

<a id="issue-tracking--apache-commons-text-issue-tracking"></a>

# Apache Commons Text Issue tracking

Apache Commons Text uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Text JIRA project page](https://issues.apache.org/jira/browse/TEXT).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Text please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12318221&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-text/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12318221&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12318221&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Text are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Text bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12318221&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Text bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12318221&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Text bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12318221&sorter/field=issuekey&sorter/order=DESC)

---

<a id="proposal"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/proposal.html -->

<!-- page_index: 5 -->

<a id="proposal--proposal-for-apache-commons-text-package"></a>

# Proposal for Apache Commons Text Package

<a id="proposal--0-rationale"></a>

## (0) Rationale

Providing algorithms for processing texts like editing distance or
similarity is out of scope of the standard Java libraries. The
*Commons Text* Package provides these extra methods.

<a id="proposal--1-scope-of-the-package"></a>

## (1) Scope of the Package

This proposal is to create a package of Java utility classes implementing
well known string algorithms and metrics.

<a id="proposal--1.5-interaction-with-other-packages"></a>

## (1.5) Interaction With Other Packages

*Commons Text* relies only on standard JDK 7 (or later) APIs for
production deployment. It utilizes the JUnit unit testing framework and
the hamcrest matcher library for developing and executing unit tests, but
this is of interest only to developers of the component. Commons Text may be
a dependency for several existing components in the open source world that
implement higher order text processing.

No external configuration files are utilized.

<a id="proposal--2-initial-source-of-the-package"></a>

## (2) Initial Source of the Package

The initial classes came from the *Commons Lang* and *Commons Codec* subprojects.

The proposed package name for the new component is
`org.apache.commons.text`.

<a id="proposal--3-required-apache-commons-resources"></a>

## (3) Required Apache Commons Resources

- Git Repository - New repository `commons-text`.
- Mailing List - Discussions will take place on the general
  *dev@commons.apache.org* mailing list. To help
  list subscribers identify messages of interest, it is suggested that
  the message subject of messages about this component be prefixed with
  [text].
- Jira - New component "Common Text" under the "Commons Sandbox" product.
- Confluence FAQ - New category "commons-text" (when available).

<a id="proposal--4-initial-committers"></a>

## (4) Initial Committers

The initial committers on the *Commons Text* component shall be as follows:

- Benedikt Ritter (britter)
- Bruno P. Kinoshita (kinow)

---

<a id="developerguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/developerguide.html -->

<!-- page_index: 6 -->

<a id="developerguide--developer-guide-for-commons-text"></a>

# Developer guide for Commons "Text"

<a id="developerguide--the-commons-text-package"></a>

# The Commons *Text* Package

<a id="developerguide--developers-guide"></a>

## Developers Guide

[[Introduction]](#developerguide--introduction)
[[Package Structure]](#developerguide--packagestructure)
[[Utility Classes]](#developerguide--utilityclasses)
[[Javadoc]](#developerguide--javadoc)
[[Building]](#developerguide--building)

<a id="developerguide--1.-introduction"></a>

### 1. INTRODUCTION

The *Text* package contains a set of Java classes that contain algorithms for measuring
and manipulating string. This developer guide seeks to set
out rules for the naming of classes and methods within the package. The purpose
of this, as with all naming standards, is to improve the coherency and
consistency of the whole API.

The philosophy of the naming standards is to follow those of the JDK
if possible.

<a id="developerguide--2.-package-structure"></a>

### 2. PACKAGE STRUCTURE

The main package for Text is `org.apache.commons.text`. Subpackages should
be created for each group of related items.

Each package should have a `package.html` file for javadoc. This should
describe the use of the package and its scope.

<a id="developerguide--3.-utility-classes"></a>

### 3. UTILITY CLASSES

Utility classes provide additional functionality around a class or interface.
Examples include StringUtils and StringEscapeUtils.

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

The Sun javadoc guidelines are the starting point for Text. These points are
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
This should be of the form 'Method will be removed in Commons Text 2.0.'.

<a id="developerguide--language-used-in-code-comments"></a>

#### Language used in code/comments

It has been decided to casually standardize on US-English.
To avoid misplaced jeers of 'americanisation', the people making this decision largely write in non-US-English.
However, it's not something to get worked up about. Lots of spelling differences will creep in all over.

<a id="developerguide--5.building"></a>

### 5.BUILDING

<a id="developerguide--building-a-release"></a>

#### Building a Release

The currently targeted version of Java is 8.

To build Text:

|  | Tested JAR | Distribution | Site |
| --- | --- | --- | --- |
| Maven 3.x | `mvn package` | `mvn assembly:assembly` | `mvn site` |

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/project-info.html -->

<!-- page_index: 7 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Text is a set of utility functions and reusable components for processing and manipulating text in a Java environment. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-text/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-text/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-text/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-text/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-text/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-text/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-text/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/summary.html -->

<!-- page_index: 8 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Text |
| Description | Apache Commons Text is a set of utility functions and reusable components for processing and manipulating text in a Java environment. |
| Homepage | [https://commons.apache.org/proper/commons-text](#index) |

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
| ArtifactId | commons-text |
| Version | 1.15.1-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/team.html -->

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
| ![](assets/images/ce9a3f447614279422ca6a7c347dec0e_379c5afd79fb9900.jpg) | kinow | Bruno P. Kinoshita | [kinow@apache.org](mailto:kinow@apache.org) | - | - | - | - | - |
| ![](assets/images/cbfb61ee7f8641b2b6eaf22fed163b1e_8ad7fb1084392adc.jpg) | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | - | - | - | - |
| ![](assets/images/a010ac0916b6b9b10883e9359cfcd7f9_2578f1d66cac252f.jpg) | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/d26c6e21bb0ae329d807cc378ee0020b_488d9f687349256f.jpg) | djones | Duncan Jones | [djones@apache.org](mailto:djones@apache.org) | - | - | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | URL |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Don Jeba | [donjeba@yahoo.com](mailto:donjeba@yahoo.com) | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Sampanna Kahu | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Jarek Strzelecki | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Lee Adcock | - | - |
| ![](assets/images/1a58e05d1b2d68e8bab05dcd51317f48_d3bbb37aee540573.jpg) | Amey Jadiye | [ameyjadiye@gmail.com](mailto:ameyjadiye@gmail.com) | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Arun Vinud S S | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Ioannis Sermetziadis | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Jostein Tveit | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Luciano Medallia | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Jan Martin Keil | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Nandor Kollar | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Nick Wong | - | - |
| ![](assets/images/00000000000000000000000000000000_11bfe3944264938f.jpg) | Ali Ghanbari | - | <https://ali-ghanbari.github.io/> |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-text/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-text/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
