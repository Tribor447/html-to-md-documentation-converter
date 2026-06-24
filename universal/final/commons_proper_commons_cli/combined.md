# Project Information

## Navigation

- Commons CLI
  - [About](#index)
  - [Sources](#scm)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Other pages
  - [Apache Commons CLI Issue tracking](#issue-tracking)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-cli"></a>

# Apache Commons CLI

The Apache Commons CLI library provides an API for parsing command-line options passed to an application.
It can also print help detailing the options available for that application.

Commons CLI supports different types of options:

- POSIX like options, for example `tar -zxvf foo.tar.gz`
- GNU like long options, for example `du --human-readable --max-depth=1`
- Java like properties, for example `java -Djava.awt.headless=true -Djava.net.useSystemProxies=true Foo`
- Short options with value attached, for example `gcc -O2 foo.c`
- long options with single hyphen, for example `ant -projecthelp`

A typical help message displayed by Commons CLI looks like this:

```

usage: ls
 -A,--almost-all          do not list implied . and ..
 -a,--all                 do not hide entries starting with .
 -B,--ignore-backups      do not list implied entried ending with ~
 -b,--escape              print octal escapes for nongraphic characters
    --block-size <SIZE>   use SIZE-byte blocks
 -c                       with -lt: sort by, and show, ctime (time of last
                          modification of file status information) with
                          -l:show ctime and sort by name otherwise: sort
                          by ctime
 -C                       list entries by columns
      
```

Check out the [introduction](https://commons.apache.org/proper/commons-cli/introduction.html) page for a detailed presentation.

<a id="index--documentation"></a>

# Documentation

A full [User's Guide](https://commons.apache.org/proper/commons-cli/introduction.html) is available
as are various [project reports](https://commons.apache.org/proper/commons-cli/project-reports.html).

The Javadoc API documents are available online:

- [Javadoc latest](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
- [Javadoc archives](https://javadoc.io/doc/commons-cli/commons-cli/latest/index.html)

The [source repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-cli.git).

<a id="index--releases"></a>

# Releases

[Download](https://commons.apache.org/cli/download_cli.cgi) the latest version.
The [release notes](https://commons.apache.org/proper/commons-cli/changes.html) are also available.

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/cli/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-cli/mail-lists.html) act as the main support forum. The user list
is suitable for most library usage queries. The dev list is intended for the development discussion. Please
remember that the lists are shared between all commons components, so prefix your email subject by
`[cli]`.

Issues may be reported via the [ASF JIRA](#issue-tracking).

<a id="index--cli-2"></a>

# CLI 2?

Commons CLI 1.0 was formed from the merger of ideas and code from three different libraries -
Werken, Avalon and Optz. In dealing with the bugs and the feature requests a freshly designed and not
backwards compatible CLI 2 was created in 2004, but never finished or released.

The current plan is to continue to maintain the 1.x line. The CLI2 work may be found in the Commons Sandbox.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-cli.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch rel/common-cli-1.11.0 https://gitbox.apache.org/repos/asf/commons-cli.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/common-cli-1.11.0 https://gitbox.apache.org/repos/asf/commons-cli.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/project-info.html -->

<!-- page_index: 3 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons CLI provides a simple API for presenting, processing, and validating a Command Line Interface. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-cli/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-cli/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-cli/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-cli/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-cli/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-cli/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-cli/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/summary.html -->

<!-- page_index: 4 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons CLI |
| Description | Apache Commons CLI provides a simple API for presenting, processing, and validating a Command Line Interface. |
| Homepage | [https://commons.apache.org/proper/commons-cli/](#index) |

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
| GroupId | commons-cli |
| ArtifactId | commons-cli |
| Version | 1.11.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/team.html -->

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
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | jstrachan | James Strachan | [jstrachan@apache.org](mailto:jstrachan@apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | bob | Bob McWhirter | [bob@werken.com](mailto:bob@werken.com) | - | Werken | - | contributed ideas and code from werken.opt | - |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | jkeyes | John Keyes | [jbjk@mac.com](mailto:jbjk@mac.com) | - | integral Source | - | contributed ideas and code from Optz | - |
| ![](assets/images/b0ceb95e9c57f1881d6a2b3d1bc77073_cb6613f0f68c26a0.jpg) | roxspring | Rob Oxspring | [roxspring@imapmail.org](mailto:roxspring@imapmail.org) | - | Indigo Stone | - | designed CLI2 | - |
| ![](assets/images/8304c64641badd4218a89a5f97d2ae86_fcb6742561c76d11.jpg) | ebourg | Emmanuel Bourg | [ebourg@apache.org](mailto:ebourg@apache.org) | - | Ariane Software | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | - | - | - | - |
| ![](assets/images/a010ac0916b6b9b10883e9359cfcd7f9_2b1b31f5610f06c0.jpg) | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization | Roles |
| --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Beluga Behr | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Peter Donald | - | - | contributed ideas and code from Avalon Excalibur's cli package |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Brian Egge | - | - | made the 1.1 release happen |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Duncan Jones | - | - | supplied patches |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Berin Loritsch | [bloritsch@apache.org](mailto:bloritsch@apache.org) | - | helped in the Avalon CLI merge |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Peter Maddocks | [peter\_maddocks@hp.com](mailto:peter_maddocks@hp.com) | Hewlett-Packard | supplied patch |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Alexandru Mocanu | - | - | supplied patch |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Andrew Shirley | - | - | lots of fixes for 1.1 |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Greg Thomas | - | - | - |
| ![](assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg) | Slawek Zachcial | - | - | unit tests |
| ![](assets/images/ca45422f802b5af7cfaa7f9ed73e62aa_ac70a6009d755e93.jpg) | Rubin Simons | [rubin@raaftech.com](mailto:rubin@raaftech.com) | - | supplied patch |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/ci-management.html -->

<!-- page_index: 6 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-cli/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/issue-tracking.html -->

<!-- page_index: 7 -->

<a id="issue-tracking--apache-commons-cli-issue-tracking"></a>

# Apache Commons CLI Issue tracking

Apache Commons CLI uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons CLI JIRA project page](https://issues.apache.org/jira/browse/CLI).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons CLI please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310463&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-cli/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310463&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310463&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons CLI are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons CLI bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310463&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons CLI bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310463&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons CLI bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310463&sorter/field=issuekey&sorter/order=DESC)

---
