# Project Information

## Navigation

- Documentation
  - [Overview](#index)
  - [Migration How-to](#migration)
  - [FAQ](#faq)
  - [Security](#security)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Repository](#scm)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-net"></a>

# Apache Commons Net

Apache Commons Net™ library implements the client side of many basic
Internet protocols. The purpose of the library is to provide
fundamental protocol access, not higher-level
abstractions. Therefore, some of the design violates
object-oriented design principles. Our philosophy is to make the
global functionality of a protocol accessible (e.g., TFTP send
file and receive file) when possible, but also provide access to
the fundamental protocols where applicable so that the programmer
may construct his own custom implementations (e.g, the TFTP
packet classes and the TFTP packet send and receive methods are
exposed).

<a id="index--features"></a>

# Features

Supported protocols include:

- FTP/FTPS
- FTP over HTTP (experimental)
- NNTP
- SMTP(S)
- POP3(S)
- IMAP(S)
- Telnet
- TFTP
- Finger
- Whois
- rexec/rcmd/rlogin
- Time (rdate) and Daytime
- Echo
- Discard
- NTP/SNTP

<a id="index--background"></a>

# Background

Apache Jakarta Commons Net started as a commercial Java library called
NetComponents, originally developed by ORO, Inc. in the early
days of Java. After its 1.3.8 release in 1998, the source code was
donated to the Apache Software Foundation and made available under
the Apache License. Since then, many programmers have contributed
to the continued development of Jakarta Commons Net. The current
version numbering scheme bears no relation to the old. In other
words, Jakarta Commons Net 1.0 succeeded and supplanted
NetComponents 1.3.8.
Apache Jakarta Commons is now an independent project and is called Apache Commons.

<a id="index--examples"></a>

# Examples

Commons NET includes several working sample applications that you can use.
Source files are included in the source (and binary) archives, and a compiled jar is provided.

To use one of the sample applications, ensure that the example and main jars are both in the same directory.
Then run the class as per the following example:

```
java -jar [path/]commons-net-examples-3.8.0.jar FTPClientExample [parameters]
```

This uses the helper application which supports shorthand class names.

Alternatively, ensure that the example and main jars are on the classpath.
Then invoke the class directly, for example:

```
java -cp commons-net-examples-3.8.0.jar;commons-net-3.8.0.jar examples/ftp/FTPClientExample [parameters]
```

<a id="index--ftp-package:-examples-ftp"></a>

## FTP (package: examples/ftp)

- [FTPClientExample](https://commons.apache.org/proper/commons-net/examples/ftp/FTPClientExample.java)
  demonstrates file download and upload, LIST, MLST etc over FTP(S) and FTP over HTTP
- [ServerToServerFTP](https://commons.apache.org/proper/commons-net/examples/ftp/ServerToServerFTP.java)
  This program arranges a server to server file transfer that transfers a file from host1 to host2.
- [TFTPExample](https://commons.apache.org/proper/commons-net/examples/ftp/TFTPExample.java)
  This is an example of a simple Java tftp client

<a id="index--mail-package:-examples-mail"></a>

## MAIL (package: examples/mail)

- [IMAPMail](https://commons.apache.org/proper/commons-net/examples/mail/IMAPMail.java)
  This is an example program demonstrating how to use the IMAP[S]Client class.
- [POP3Mail](https://commons.apache.org/proper/commons-net/examples/mail/POP3Mail.java)
  This is an example program demonstrating how to use the POP3[S]Client class.
- [SMTPMail](https://commons.apache.org/proper/commons-net/examples/mail/SMTPMail.java)
  This is an example program demonstrating how to use the SMTP[S]Client class.

<a id="index--nntp-package:-examples-nntp"></a>

## NNTP (package: examples/nntp)

- [ArticleReader](https://commons.apache.org/proper/commons-net/examples/nntp/ArticleReader.java)
  Simple class showing one way to read an article header and body.
- [ExtendedNNTPOps](https://commons.apache.org/proper/commons-net/examples/nntp/ExtendedNNTPOps.java)
  Simple class showing some of the extended commands (AUTH, XOVER, LIST ACTIVE)
- [ListNewsgroups](https://commons.apache.org/proper/commons-net/examples/nntp/ListNewsgroups.java)
  This is a simple example using the NNTP package to approximate the
  Unix newsgroups command. It connects to the specified news
  server and issues fetches the list of newsgroups stored by the server.
  On servers that store a lot of newsgroups, this command can take a very
  long time (listing upwards of 30,000 groups).
- [MessageThreading](https://commons.apache.org/proper/commons-net/examples/nntp/MessageThreading.java)
  Sample program demonstrating the use of article iteration and threading.
- [PostMessage](https://commons.apache.org/proper/commons-net/examples/nntp/PostMessage.java)
  This is an example program using the NNTP package to post an article to the specified newsgroup(s).
  It prompts you for header information and a filename to post.

<a id="index--ntp-package:-examples-ntp"></a>

## NTP (package: examples/ntp)

- [NTPClient](https://commons.apache.org/proper/commons-net/examples/ntp/NTPClient.java)
  This is an example program demonstrating how to use the NTPUDPClient
  class. This program sends a Datagram client request packet to a
  Network time Protocol (NTP) service port on a specified server,
  retrieves the time, and prints it to standard output along with
  the fields from the NTP message header (e.g. stratum level, reference id,
  poll interval, root delay, mode, ...)
- [TimeClient](https://commons.apache.org/proper/commons-net/examples/ntp/TimeClient.java)
  This is an example program demonstrating how to use the TimeTCPClient
  and TimeUDPClient classes.
  This program connects to the default time service port of a
  specified server, retrieves the time, and prints it to standard output.

<a id="index--telnet-package:-examples-telnet"></a>

## TELNET (package: examples/telnet)

- [TelnetClientExample](https://commons.apache.org/proper/commons-net/examples/telnet/TelnetClientExample.java)
  This is a simple example of use of TelnetClient.
- [WeatherTelnet](https://commons.apache.org/proper/commons-net/examples/telnet/WeatherTelnet.java)
  This is an example of a trivial use of the TelnetClient class.
  It connects to the weather server at the University of Michigan,
  um-weather.sprl.umich.edu port 3000, and allows the user to interact
  with the server via standard input.

<a id="index--unix-utilities-package:-examples-unix"></a>

## Unix utilities (package: examples/unix)

- [chargen](https://commons.apache.org/proper/commons-net/examples/unix/chargen.java)
  This is a simple example of use of chargen.
- [daytime](https://commons.apache.org/proper/commons-net/examples/unix/daytime.java)
  This is a simple example of use of daytime.
- [echo](https://commons.apache.org/proper/commons-net/examples/unix/echo.java)
  This is a simple example of use of echo.
- [finger](https://commons.apache.org/proper/commons-net/examples/unix/finger.java)
  This is a simple example of use of finger.
- [fwhois](https://commons.apache.org/proper/commons-net/examples/unix/fwhois.java)
  This is a simple example of use of fwhois.
- [rdate](https://commons.apache.org/proper/commons-net/examples/unix/rdate.java)
  This is a simple example of use of rdate.
- [rexec](https://commons.apache.org/proper/commons-net/examples/unix/rexec.java)
  This is a simple example of use of rexec.
- [rlogin](https://commons.apache.org/proper/commons-net/examples/unix/rlogin.java)
  This is a simple example of use of rlogin.
- [rshell](https://commons.apache.org/proper/commons-net/examples/unix/rshell.java)
  This is a simple example of use of rshell.

---

<a id="migration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/migration.html -->

<!-- page_index: 2 -->

<a id="migration--migration-how-to"></a>

# Migration How-To

This how-to lists the migration steps for moving between versions of Apache Commons Net.

<a id="migration--apache-commons-net-3.9.0"></a>

# Apache Commons Net 3.9.0

This version requires Java 8 or above.

<a id="migration--apache-commons-net-3.7-to-3.8.0"></a>

# Apache Commons Net 3.7 to 3.8.0

This version requires Java 7 or above.

<a id="migration--apache-commons-net-3.5-to-3.6"></a>

# Apache Commons Net 3.5 to 3.6

This version requires Java 6 or above.

<a id="migration--apache-commons-net-3.x-to-commons-net-3.5"></a>

# Apache Commons Net 3.x to Commons Net 3.5

Version 3.5 is binary compatible with previous 3.x versions and 2.0.
There should be no changes required to existing binary code.

Version 3.5 is source compatible with 3.4.
However, version 3.4 is
**not source compatible**
with 3.3.

The interface NtpV3Packet has been updated to add 3 new methods.
Adding methods to an interface
[does not affect binary compatibility](https://docs.oracle.com/javase/specs/jls/se5.0/html/binaryComp.html#45348)
The
[clirr report](https://commons.apache.org/proper/commons-net/clirr-report.html)
shows which methods have been added.
(note that the report does not distinguish between source and binary incompatibility)
Code that uses the interface will need to be updated and recompiled.
However code that uses the implementation class NtpV3Impl will continue to work as before.

<a id="migration--apache-commons-net-2.x-to-commons-net-3.0"></a>

# Apache Commons Net 2.x to Commons Net 3.0

Version 3.0 is binary compatible with version 2.0. There should be no changes required to existing binary code.

However, version 3.0 is
**not source compatible**
with 2.0.

Several obsolete/unused constants have been removed.

(Such changes do not affect binary code, because compilers are required to localise constants).

The
[clirr report](https://commons.apache.org/proper/commons-net/clirr-report.html)
shows which constants have been removed.
If any source code happens to be using one of these constants, then the source will have to be updated.

Also, some throws clauses have been removed from methods which did not actually throw them.

Throws clauses are not part of method signatures, so do not affect binary compatibility.

The following public methods no longer throw IOException:

- TelnetClient#addOptionHandler(TelnetOptionHandler)
- TelnetClient#deleteOptionHandler(int)

Source code using these methods will need to be updated.

<a id="migration--apache-commons-net-1.4.x-to-commons-net-2.0"></a>

# Apache Commons Net 1.4.x to Commons Net 2.0

Version 2.0 requires a JDK 5.0+ runtime. It has also been tested on JDK 6.0. There should
be no changes required to existing client code.

<a id="migration--netcomponents-1.3.8-to-commons-net-1.x"></a>

# NetComponents 1.3.8 to Commons Net 1.x

This version is a drop in replacement for NetComponents. Only package names have changed.

1. Change all occurrences of
   `com.oroinc.net.*`
   to
   `org.apache.commons.net.*`
2. Change all occurrences of
   `com.oroinc.io.*`
   to
   `org.apache.commons.net.io.*`
3. Change all occurrences of
   `com.oroinc.util.*`
   to
   `org.apache.commons.net.util.*`

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/faq.html -->

<!-- page_index: 3 -->

<a id="faq--frequently-asked-questions"></a>

# Frequently Asked Questions

This document attempts to answer some of the more frequently asked
questions regarding various aspects of Commons/Net. These questions are
typically asked over and over again on the mailing lists, as a
courtesy to the developers, we ask that you read this document
before posting to the mailing lists.

The FAQ is hosted on the Commons Wiki; please see:
[CommonsNet/FrequentlyAskedQuestions](https://wiki.apache.org/commons/Net/FrequentlyAskedQuestions)

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/security.html -->

<!-- page_index: 4 -->

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
[user mailing list](https://commons.apache.org/proper/commons-net/mail-lists.html)
.

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security
impact, or if the descriptions here are incomplete, please report them privately to the Apache Security
Team. Thank you.

<a id="security--cve-2021-37533:-apache-commons-net-s-ftp-client-trusts-the-host-from-pasv-response-by-default"></a>

## CVE-2021-37533: Apache Commons Net's FTP client trusts the host from PASV response by default

On 2022-12-03, the Apache Commons Text team disclosed
[CVE-2021-37533](https://www.cve.org/CVERecord?id=CVE-2021-37533)

Severity: low

Prior to Apache Commons Net 3.9.0, Net's FTP client trusts the host from PASV response by default. A
malicious server can redirect the Commons Net code to use a different host, but the user has to
connect to the malicious server in the first place. This may lead to leakage of information about
services running on the private network of the client.
The default in version 3.9.0 is now false to ignore such hosts, as cURL does. See
[NET-711](https://issues.apache.org/jira/browse/NET-711).

Credit: Apache Commons would like to thank ZeddYu Lu for reporting this issue.

References:

- [Announcement on dev@commons.apache.org](https://lists.apache.org/thread/o6yn9r9x6s94v97264hmgol1sf48mvx7)
- [Announcement on oss-security](https://www.openwall.com/lists/oss-security/2022/12/03/1)
- [Advisory on cve.org](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-37533)

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/issue-tracking.html -->

<!-- page_index: 5 -->

<a id="issue-tracking--apache-commons-net-issue-tracking"></a>

# Apache Commons Net Issue tracking

Apache Commons Net uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Net JIRA project page](https://issues.apache.org/jira/browse/NET).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Net please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310487&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-net/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310487&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310487&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Net are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Net bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310487&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Net bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310487&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Net bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310487&sorter/field=issuekey&sorter/order=DESC)

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/scm.html -->

<!-- page_index: 6 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-net
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-net
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-net
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/project-info.html -->

<!-- page_index: 7 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Net library contains a collection of network utilities and protocol implementations. Supported protocols include Echo, Finger, FTP, NNTP, NTP, POP3(S), SMTP(S), Telnet, and Whois. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-net/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-net/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-net/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-net/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-net/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-net/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-net/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/summary.html -->

<!-- page_index: 8 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Net |
| Description | Apache Commons Net library contains a collection of network utilities and protocol implementations. Supported protocols include Echo, Finger, FTP, NNTP, NTP, POP3(S), SMTP(S), Telnet, and Whois. |
| Homepage | [https://commons.apache.org/proper/commons-net/](#index) |

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
| GroupId | commons-net |
| ArtifactId | commons-net |
| Version | 3.13.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/team.html -->

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
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | brekke | Jeffrey D. Brekke | [Jeff.Brekke@qg.com](mailto:Jeff.Brekke@qg.com) | - | Quad/Graphics, Inc. | - | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | scohen | Steve Cohen | [scohen@apache.org](mailto:scohen@apache.org) | - | javactivity.org | - | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | brudav | Bruno D'Avanzo | [bruno.davanzo@hp.com](mailto:bruno.davanzo@hp.com) | - | Hewlett-Packard | - | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | dfs | Daniel F. Savarese | [dfs@apache.org](mailto:dfs@apache.org) | - | <a href="https://www.savarese.com/">Savarese Software Research</a> | - | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | rwinston | Rory Winston | [rwinston@apache.org](mailto:rwinston@apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | - | Rory Winston | [rwinston@checkfree.com](mailto:rwinston@checkfree.com) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Henrik Sorensen | [henrik.sorensen@balcab.ch](mailto:henrik.sorensen@balcab.ch) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Jeff Nadler | [jnadler@srcginc.com](mailto:jnadler@srcginc.com) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | William Noto | [wnoto@openfinance.com](mailto:wnoto@openfinance.com) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Stephane ESTE-GRACIAS | [sestegra@free.fr](mailto:sestegra@free.fr) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Dan Armbrust | [daniel.armbrust.list@gmail.com](mailto:daniel.armbrust.list@gmail.com) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Yuval Kashtan | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Joseph Hindsley | - | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Rob Hasselbaum | [rhasselbaum@alumni.ithaca.edu](mailto:rhasselbaum@alumni.ithaca.edu) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Mario Ivankovits | [mario@ops.co.at](mailto:mario@ops.co.at) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Naz Irizarry | - | MITRE Corp |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Tapan Karecha | [tapan@india.hp.com](mailto:tapan@india.hp.com) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Jason Mathews | - | MITRE Corp |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Winston Ojeda | [Winston.Ojeda@qg.com](mailto:Winston.Ojeda@qg.com) | Quad/Graphics, Inc. |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Ted Wise | [ctwise@bellsouth.net](mailto:ctwise@bellsouth.net) | - |
| ![](assets/images/00000000000000000000000000000000_27bf3eb66a18eb1e.jpg) | Bogdan Drozdowski | [bogdandr # op dot pl](mailto:bogdandr # op dot pl) | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-net/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-net/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
