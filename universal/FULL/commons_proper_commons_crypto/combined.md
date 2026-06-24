# Apache Commons Crypto – Project Information

## Navigation

- Documentation
  - [Overview](#index)
  - [User Guide](#userguide)
  - [FAQ](#faq)
  - [Security](#security)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Source Repository](#scm)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes-report)
    - [JIRA Report](#jira-report)
    - [Surefire Report](#surefire-report)
    - [Rat Report](#rat-report)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [SpotBugs](#spotbugs)
    - [CPD](#cpd)
    - [PMD](#pmd)
    - [Tag List](#taglist)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-crypto"></a>

## Apache Commons Crypto

Apache Commons Crypto is a cryptographic library optimized with AES-NI (Advanced Encryption
Standard New Instructions). Commons Crypto provides Java APIs at the cipher level and Java stream
level. Developers can implement high performance AES encryption/decryption with
minimum coding and effort. Please note that Commons Crypto doesn't implement the
cryptographic algorithm such as AES directly, it wraps OpenSSL and JCE.

<a id="index--features"></a>

## Features

- Cipher API for low level cryptographic operations.
- Secure true random number generator.
- Java stream API for high level stream
  encryption/decryption.
- High performance AES encryption/decryption optimized with Intel AES-NI.
- Portable across various operating systems (currently only Linux/Mac OS/Windows); Apache
  Commons Crypto loads the library according to your machine environment (using system
  properties, os.name and os.arch).
- Simple usage. Add the commons-crypto-(version).jar file to your classpath.

<a id="index--documentation"></a>

## Documentation

An overview of the functionality is provided in the
[user guide](#userguide).
Various
[project reports](#project-reports)
are also available.

The Javadoc API documents are available online:

- [Javadoc](https://commons.apache.org/proper/commons-crypto/apidocs/index.html)

The [git repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-crypto.git).

<a id="index--releases"></a>

## Releases

- [Crypto 1.2.0 (mirrors)](https://commons.apache.org/proper/commons-crypto/download_crypto.cgi)
  requires Java 1.8 and OpenSSL 1.1.x (should also work with 1.0.x)
- [Crypto 1.1.0 (archives)](https://archive.apache.org/dist/commons/crypto/)
  requires Java 1.8, built and tested with:

- darwin64-x86\_64-cc; OpenSSL 1.1.1g
- debian-amd64; OpenSSL 1.0.1f
- debian-amd64; OpenSSL 1.1.1g
- debian-arm64; OpenSSL 1.1.1f
- linux-aarch64; OpenSSL 1.0.2k-fips
- Linux x86\_64; OpenSSL 1.1.1
- Windows 64 (mingw64); OpenSSL 1.1.1d

- [Crypto 1.0.0 (archives)](https://archive.apache.org/dist/commons/crypto/)
  requires Java 1.7.

See the
[Download Page](https://commons.apache.org/proper/commons-crypto/download_crypto.cgi)
for the latest releases.

[Change reports](#changes-report) are also available.

For previous releases, see the [Apache
Archive](https://archive.apache.org/dist/commons/crypto/)

<a id="index--support"></a>

## Support

The [commons mailing lists](https://commons.apache.org/proper/commons-crypto/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [crypto].

Issues may be reported via [ASF JIRA](#issue-tracking).

---

<a id="userguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/userguide.html -->

<!-- page_index: 2 -->

<a id="userguide--user-guide"></a>

## User guide

Apache Commons Crypto is a cryptographic library optimized with AES-NI
(Advanced Encryption
Standard New Instructions). It provides Java API for both cipher level and Java stream
level. Developers can use it to implement high performance AES encryption/decryption with
the minimum code and effort.

Please note that Apache Commons Crypto doesn't implement the cryptographic
algorithm such as AES directly. It wraps OpenSSL or JCE which implement the algorithms.
OpenSSL 1.1.1 is required for building and running.

<a id="userguide--interfaces-overview"></a>

### Interfaces Overview

Interfaces and classes used by the various implementation in the sub-packages.

|  |  |
| --- | --- |
| [random](https://commons.apache.org/proper/commons-crypto/apidocs/index.html) | The interface for CryptoRandom. |
| [cipher](https://commons.apache.org/proper/commons-crypto/apidocs/index.html) | The interface of cryptographic cipher for encryption and decryption. |
| [stream](https://commons.apache.org/proper/commons-crypto/apidocs/index.html) | The interface wraps the underlying stream and it automatically encrypts the stream when data is written and decrypts the stream when data is read. |

<a id="userguide--usage"></a>

### Usage

<a id="userguide--prerequisites"></a>

#### Prerequisites

Commons Crypto relies on standard JDK 1.8 (or above) and OpenSSL 1.1.1 for production
deployment.
If it is installed, the command `openssl version` can be used to show the version.

OpenSSL may already be installed on your system; if not, please visit
[OpenSSL.org](https://www.openssl.org/) for information on installation.

<a id="userguide--using-commons-crypto-in-your-apache-maven-build"></a>

#### Using Commons Crypto in your Apache Maven build

To build with Apache Maven, add the dependencies listed below to your pom.xml file.

```

<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-crypto</artifactId>
    <version>1.1.0</version>
</dependency>
```

<a id="userguide--usage-of-random-api"></a>

#### Usage of Random API

CryptoRandom provides a cryptographically strong random number generators.
The default implementation will use Intel® Digital Random Number Generator (DRNG)
for accelerating the random generation.

[RandomExample.java](https://commons.apache.org/proper/commons-crypto/xref-test/org/apache/commons/crypto/examples/RandomExample.html)

<a id="userguide--usage-of-cipher-api"></a>

#### Usage of Cipher API

Cipher provides an cryptographic interface for encryption and decryption.
We provide two kind of implementations: JCE Cipher and OpenSSL Cipher. The
JCE implementation uses JCE provider and the OpenSSL implementation uses
Intel® AES New Instructions (Intel® AES NI).

<a id="userguide--usage-of-byte-array-encryption-decryption"></a>

##### Usage of Byte Array Encryption/Decryption

[CipherByteArrayExample.java](https://commons.apache.org/proper/commons-crypto/xref-test/org/apache/commons/crypto/examples/CipherByteArrayExample.html)

<a id="userguide--usage-of-bytebuffer-encryption-decryption"></a>

##### Usage of ByteBuffer Encryption/Decryption

[CipherByteBufferExample.java](https://commons.apache.org/proper/commons-crypto/xref-test/org/apache/commons/crypto/examples/CipherByteBufferExample.html)

<a id="userguide--usage-of-stream-api"></a>

#### Usage of Stream API

Stream provides the data encryption and decryption in stream manner. We provide CryptoInputStream, CTRCryptoInputStream, PositionedCryptoInputStream implementations for InputStream and CryptoOutputStream, CTRCryptoOutputStream implementations for OutputStream.

<a id="userguide--usage-of-stream-encryption-decryption"></a>

##### Usage of stream encryption/decryption

[StreamExample.java](https://commons.apache.org/proper/commons-crypto/xref-test/org/apache/commons/crypto/examples/StreamExample.html)

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/faq.html -->

<!-- page_index: 3 -->

<a id="faq--frequently-asked-questions"></a>

# Frequently asked questions

<a id="faq--how-to-use-a-custom-secret-generator"></a>

## How to use a custom secret generator?

Commons Crypto provides the `CryptoRandom` interface for defining secret generators.
The `RandomProvider` enum in the `CryptoRandomFactory` defines some sensible default
implementations:

OPENSSL
:   OpenSSL based JNI implementation shipped with Commons Crypto.

JAVA
:   The SecureRandom implementation from the JVM.

OS
:   The OS random device implementation. May not be available on some operation systems.

When calling `CryptoRandomFactory.getCryptoRandom()`, Commons Crypto tries to use the OpenSSL
CryptoRandom implementation first. If this fails, the Java implementation is used.
In order use a different `CryptoRandom` implementation (e.g. OS), the
`CryptoRandomFactory.getCryptoRandom(Properties)` method can be used, passing in the desired
implementation class names:

```

Properties props = new Properties();
props.setProperty(CryptoRandomFactory.CLASSES_KEY, CryptoRandomFactory.RandomProvider.OS.getClassName());
CryptoRandom random = CryptoRandomFactory.getCryptoRandom(props);
```

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/security.html -->

<!-- page_index: 4 -->

<a id="security--security-vulnerabilities"></a>

## Security Vulnerabilities

For information about reporting or asking questions about
security, please see the
[security page](https://commons.apache.org/security.html)
of the Apache Commons project.

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the
building instructions for the component version that you are using.

If you need help on building this component or other help on following the instructions to
mitigate the known vulnerabilities listed here, please send your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-crypto/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security
impact, or if the descriptions here are incomplete, please report them privately to the Apache Security
Team. Thank you.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/issue-tracking.html -->

<!-- page_index: 5 -->

<a id="issue-tracking--apache-commons-crypto-issue-tracking"></a>

## Apache Commons Crypto Issue tracking

Apache Commons Crypto uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Crypto JIRA project page](https://issues.apache.org/jira/browse/CRYPTO).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Crypto please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320024&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-crypto/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12320024&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12320024&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Crypto are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Crypto bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320024&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Crypto bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320024&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Crypto bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320024&sorter/field=issuekey&sorter/order=DESC)

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/scm.html -->

<!-- page_index: 6 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-crypto.git
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-crypto.git
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-crypto.git
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/project-info.html -->

<!-- page_index: 7 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Crypto is a cryptographic library optimized with AES-NI (Advanced Encryption Standard New Instructions). It provides Java API for both cipher level and Java stream level. Developers can use it to implement high performance AES encryption/decryption with the minimum code and effort. Please note that Crypto doesn't implement the cryptographic algorithm such as AES directly. It wraps to OpenSSL or JCE which implement the algorithms. Features -------- 1. Cipher API for low level cryptographic operations. 2. Java stream API (CryptoInputStream/CryptoOutputStream) for high level stream encryption/decryption. 3. Both optimized with high performance AES encryption/decryption. (1400 MB/s - 1700 MB/s throughput in modern Xeon processors). 4. JNI-based implementation to achieve comparable performance to the native C/C++ version based on OpenSsl. 5. Portable across various operating systems (currently only Linux/MacOSX/Windows); Apache Commons Crypto loads the library according to your machine environment (it checks system properties, `os.name` and `os.arch`). 6. Simple usage. Add the commons-crypto-(version).jar file to your classpath. Export restrictions ------------------- This distribution includes cryptographic software. The country in which you currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software. BEFORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted. See <http://www.wassenaar.org/> for more information. The U.S. Government Department of Commerce, Bureau of Industry and Security (BIS), has classified this software as Export Commodity Control Number (ECCN) 5D002.C.1, which includes information security software using or performing cryptographic functions with asymmetric algorithms. The form and manner of this Apache Software Foundation distribution makes it eligible for export under the License Exception ENC Technology Software Unrestricted (TSU) exception (see the BIS Export Administration Regulations, Section 740.13) for both object code and source code. The following provides more details on the included cryptographic software: \* Commons Crypto use [Java Cryptography Extension](http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html) provided by Java \* Commons Crypto link to and use [OpenSSL](https://www.openssl.org/) ciphers |
| [Summary](https://commons.apache.org/proper/commons-crypto/summary.html) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-crypto/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-crypto/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependency Information](https://commons.apache.org/proper/commons-crypto/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-crypto/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-crypto/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-crypto/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-crypto/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/team.html -->

<!-- page_index: 8 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | atm | Aaron T Myers | [atm@apache.org](mailto:atm@apache.org) | - | - | - | - | - |
|  | wang | Andrew Wang | [wang@apache.org](mailto:wang@apache.org) | - | - | - | - | - |
|  | cnauroth | Chris Nauroth | [cnauroth@apache.org](mailto:cnauroth@apache.org) | - | - | - | - | - |
|  | cmccabe | Colin P. McCabe | [cmccabe@apache.org](mailto:cmccabe@apache.org) | - | - | - | - | - |
|  | sdp | Dapeng Sun | [sdp@apache.org](mailto:sdp@apache.org) | - | - | - | - | - |
|  | dianfu | Dian Fu | [dianfu@apache.org](mailto:dianfu@apache.org) | - | - | - | - | - |
|  | dongc | Dong Chen | [dongc@apache.org](mailto:dongc@apache.org) | - | - | - | - | - |
|  | xuf | Ferdinand Xu | [xuf@apache.org](mailto:xuf@apache.org) | - | - | - | - | - |
|  | haifengchen | Haifeng Chen | [haifengchen@apache.org](mailto:haifengchen@apache.org) | - | - | - | - | - |
|  | vanzin | Marcelo Vanzin | [vanzin@apache.org](mailto:vanzin@apache.org) | - | - | - | - | - |
|  | umamahesh | Uma Maheswara Rao G | [umamahesh@apache.org](mailto:umamahesh@apache.org) | - | - | - | - | - |
|  | yliu | Yi Liu | [yliu@apache.org](mailto:yliu@apache.org) | - | - | - | - | - |
|  | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization |
| --- | --- | --- | --- |
|  | Colin Ma | [junjie.ma@intel.com](mailto:junjie.ma@intel.com) | - |
|  | Xianda Ke | [xianda.ke@intel.com](mailto:xianda.ke@intel.com) | - |
|  | Ke Jia | [ke.a.jia@intel.com](mailto:ke.a.jia@intel.com) | - |
|  | George Kankava | [george.kankava@devfactory.com](mailto:george.kankava@devfactory.com) | - |
|  | Tian Jianguo | [jianguo.tian@intel.com](mailto:jianguo.tian@intel.com) | - |
|  | Adam Retter | - | Evolved Binary |
|  | Arturo Bernal | - | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/ci-management.html -->

<!-- page_index: 9 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [Jenkins](https://www.jenkins.io/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://builds.apache.org/search/?q=Commons-CRYPTO
```

<a id="ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/project-reports.html -->

<!-- page_index: 10 -->

<a id="project-reports--generated-reports"></a>

## Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](http://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [Changes](#changes-report) | Changes report on releases of this project. |
| [JIRA Report](#jira-report) | Report on Issues from the JIRA Issue Tracking System. |
| [Javadoc](https://commons.apache.org/proper/commons-crypto/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-crypto/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-crypto/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire Report](#surefire-report) | Report on the test results of the project. |
| [Rat Report](#rat-report) | Report on compliance to license related source code policies |
| [JaCoCo](https://commons.apache.org/proper/commons-crypto/jacoco/index.html) | JaCoCo Coverage Report. |
| [japicmp](#japicmp) | Comparing source compatibility of commons-crypto-1.2.0.jar against commons-crypto-1.1.0.jar |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [SpotBugs](#spotbugs) | Generates a source code report with the SpotBugs Library. |
| [CPD](#cpd) | Duplicate code detection. |
| [PMD](#pmd) | Verification of coding rules. |
| [Tag List](#taglist) | Report on various tags found in the code. |

---

<a id="changes-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/changes-report.html -->

<!-- page_index: 11 -->

# Apache Commons Crypto – Apache Commons Crypto Release Notes

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
DOC2MDPLACEHOLDERTOKEN0END<h2><a name="Apache_Commons_Crypto_Release_Notes"></a>Apache Commons Crypto Release Notes</h2><section>
DOC2MDPLACEHOLDERTOKEN1END<h3><a name="Release_History"></a>Release History</h3>
<table>
<tr>
<th>Version</th>
<th>Date</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes-report--a1.2.0">1.2.0</a></td>
<td>2023-01-14</td>
<td>Minor release  (Java 8, OpenSSL 1.1.1)</td></tr>
<tr>
<td><a href="#changes-report--a1.1.0">1.1.0</a></td>
<td>2020-08-28</td>
<td>Minor release (Java 8, OpenSSL 1.1.1)</td></tr>
<tr>
<td><a href="#changes-report--a1.0.0">1.0.0</a></td>
<td>2016-07-22</td>
<td>Initial release (Java 7).  The initial release is known to build on Linux, MacOS/X and Windows (using MinGW).  It may build on other systems.  Please note that the JNA interface to OpenSSL is a preliminary release.  It is relatively slow, but may be of use on systems which aren't yet supported by the JNI code.</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN2END<h3 id="a1.2.0">Release 1.2.0 – 2023-01-14</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Enhance the quality of JavaCryptoRandom. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-160">CRYPTO-160</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#jochen">jochen</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Package-private implementations of CryptoRandom extends java.util.Random but should not. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-160">CRYPTO-160</a>. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Makefile does not recompile objects if local include files are changed. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-163">CRYPTO-163</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>License header should be a plain comment #113. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-154">CRYPTO-154</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Fix PMD warning and don't init to defaults #128. Thanks to Arturo Bernal.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Minor changes #135. Thanks to Arturo Bernal.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Port from pre-Java 8 javah tool to Java 8 and up javac with the -h option. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Fix build on Java 11. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Fix build on Java 17. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Minor improvement #115, #125. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-155">CRYPTO-155</a>. Thanks to Arturo Bernal.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>PositionedCryptoInputStream does not close its CryptoCipher instances. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Validate return value from OpenSslNativeJna.EVP_CIPHER_CTX_set_padding(). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Validate return value from OpenSslNativeJna.ENGINE_finish(). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Validate return value from OpenSslNativeJna.ENGINE_free(). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Add github/codeql-action 2 #159. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Add AES utility class. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump actions/cache from 2.1.7 to 3.0.9 #150, #184. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump actions/checkout from 2 to 3.1.0 #149, #187. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump actions/setup-java from 2 to 3.6.0 #190. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump actions/upload-artifact from 3.1.0 to 3.1.1 #192. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Migrate to Junit 5.9.1 #114, #171, #183. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-151">CRYPTO-151</a>. Thanks to Arturo Bernal, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump jna from 5.5.0 to 5.13.0 #123, #139, #153, #167, #209. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump commons.japicmp.version from 0.14.3 to 0.17.1. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.1.1 to 3.2.0 #130, #176. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump jmh.version from 1.12 to 1.36 #119, #157, #194. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump exec-maven-plugin from 1.6.0 to 3.1.0 #121, #170. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump maven-antrun-plugin from 1.8 to 3.1.0 #120, #158. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump commons.japicmp.version from 0.15.2 to 0.15.7 #138. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump jacoco-maven-plugin from 0.6.6 to 0.8.8 #138, #154. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.2.0 to 3.4.1 #138. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.14.0 to 3.19.0 #140, #177, #178. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump pmd from 6.44.0 to 6.52.0. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump taglist-maven-plugin from 2.4 to 3.0.0 #147. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.5.3.0 to 4.7.3.0 #152, #160, #168, #174, #179, #189, #193. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump commons-parent from 52 to 56 #182, #196, #204. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump commons.surefire.version from 3.0.0-M5 to 3.0.0-M7. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump maven-resources-plugin from 3.2.0 to 3.3.0 #172. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump jaxb-impl from 2.3.6 to 2.3.7. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN3END<h3 id="a1.1.0">Release 1.1.0 – 2020-08-28</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Support Galois/Counter Mode (GCM). Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-59">CRYPTO-59</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>CryptoOutputStream does not call write in a loop when underlying channel works in non-block mode. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-125">CRYPTO-125</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Provide FAQ page. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-131">CRYPTO-131</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>CipherByteBufferExample should not truncate the string. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-134">CRYPTO-134</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Error compiling on Win64 with Mingw. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-137">CRYPTO-137</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>CipherByteArrayExample fails on OpenSSL 1.1.0g with java.lang.UnsatisfiedLinkError: EVP_CIPHER_CTX_cleanup. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-138">CRYPTO-138</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Add support for AARCH64. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-139">CRYPTO-139</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Errors in native code can leave Java wrappers in bad state. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-141">CRYPTO-141</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Intermittent Failure in GCMCipherTest#testGcmTamperedData() #105. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-141">CRYPTO-141</a>. Thanks to Alex Remily.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Make org.apache.commons.crypto.stream.input.Input extend Closeable. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-139">CRYPTO-139</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Make org.apache.commons.crypto.stream.output.Output extend Closeable. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-139">CRYPTO-139</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Add support for ARM.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Add support for ARM-HF.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Reset JAVA_HOME for aarch64 and ppc builds. Turn off maven-enforcer for Xenial builds #104. Thanks to Geoffrey Blake.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Update maven-checkstyle-plugin 3.0.0 -&gt; 3.1.1.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Update commons-parent 51 -&gt; 52.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Update maven-resources-plugin 3.1.0 -&gt; 3.2.0.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Update Apache CLIRR to JApiCmp.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Update FindBugs to SpotBugs.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Bump coveralls-maven-plugin from 3.1.0 to 4.3.0 #112. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-153">CRYPTO-153</a>. Thanks to Arturo Bernal.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#ggregory">ggregory</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN4END<h3 id="a1.0.0">Release 1.0.0 – 2016-07-22</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Enable common code quality reports. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-68">CRYPTO-68</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Warnings compiling on MacOSX - JNIEXPORT redefined. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-65">CRYPTO-65</a>. Thanks to sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>User guide documentation . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-11">CRYPTO-11</a>. Thanks to Ke Jia, Jerry Chen.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Ke Jia">Ke Jia</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Rename CryptoInputStream to CipherInputStream and CryptoOutputStream to CipherOutputStream . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-12">CRYPTO-12</a>. Thanks to Xianda Ke.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Xianda Ke">Xianda Ke</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>The API differences between apache.commons.crypto and JCE . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-13">CRYPTO-13</a>. Thanks to Xianda Ke.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Xianda Ke">Xianda Ke</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Utility classes should not have public constructors . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-26">CRYPTO-26</a>. Thanks to Dapeng Sun.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dapeng Sun">Dapeng Sun</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Update the README.md of Apache Commons Crypto . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-28">CRYPTO-28</a>. Thanks to Ferdinand Xu, Ke Jia.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Ferdinand Xu">Ferdinand Xu</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Make sure Cipher.ENCRYPT_MODE is consistent with JDK . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-29">CRYPTO-29</a>. Thanks to Dian Fu, Sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dian Fu">Dian Fu</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Change default cipher as OpenSslCipher . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-3">CRYPTO-3</a>. Thanks to ferdinand xu.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Ferdinand Xu">Ferdinand Xu</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Mutable fields should be private . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-30">CRYPTO-30</a>. Thanks to Ferdinand Xu, Sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Ferdinand Xu">Ferdinand Xu</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Make fields final wherever possible . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-31">CRYPTO-31</a>. Thanks to Ferdinand Xu, Sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Ferdinand Xu">Ferdinand Xu</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>SecureRandom shadows JVM class . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-33">CRYPTO-33</a>. Thanks to Xianda Ke, Sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Xianda Ke">Xianda Ke</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>JavaSecureRandom should throw Exception if it cannot create the instance . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-34">CRYPTO-34</a>. Thanks to Dapeng Sun, Sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dapeng Sun">Dapeng Sun</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Always use blocks . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-38">CRYPTO-38</a>. Thanks to Dapeng Sun, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dapeng Sun">Dapeng Sun</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Remove the full qualified package name for shadowed classes . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-40">CRYPTO-40</a>. Thanks to Xianda Ke, Jerry Chen.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Xianda Ke">Xianda Ke</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Remove the header files required for cross platform compilation . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-42">CRYPTO-42</a>. Thanks to Dian Fu, Jerry Chen.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dian Fu">Dian Fu</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Document how to build Commons Crypto . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-45">CRYPTO-45</a>. Thanks to Dian Fu, Benedikt Ritter.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dian Fu">Dian Fu</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Fix build of MAC_OS . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-47">CRYPTO-47</a>. Thanks to Dapeng Sun.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dapeng Sun">Dapeng Sun</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_bf184d3d45464026.gif" title="Add"/></td>
<td>Setup site build as defined in commons-parent pom . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-48">CRYPTO-48</a>. Thanks to Benedikt Ritter, Dapeng Sun.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Benedikt Ritter">Benedikt Ritter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>CRYPTO-1 Fix build of X86 . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-49">CRYPTO-49</a>. Thanks to Dapeng Sun.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dapeng Sun">Dapeng Sun</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Rename source code in Chimera to Apache name space . Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-7">CRYPTO-7</a>. Thanks to ferdinand xu.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Ferdinand Xu">Ferdinand Xu</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Fix build on Mac OS. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-57">CRYPTO-57</a>. Thanks to Benedikt Ritter.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Benedikt Ritter">Benedikt Ritter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>Fix possible NPE in OpenSslCryptoRandom. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-61">CRYPTO-61</a>. Thanks to Hendrik Saly.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Hendrik Saly">Hendrik Saly</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_9c044af4f0ab5136.gif" title="Fix"/></td>
<td>US Export classification and ECCN registration for encryption. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-54">CRYPTO-54</a>. Thanks to Stian Soiland-Reyes, Jerry Chen, Benedikt Ritter, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Dapeng Sun">Dapeng Sun</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a87bd7f4c692918e.gif" title="Update"/></td>
<td>Add multithreaded related tests. Fixes <a href="https://issues.apache.org/jira/browse/CRYPTO-62">CRYPTO-62</a>. Thanks to Hendrik Saly.</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/team-list.html#Hendrik Saly">Hendrik Saly</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2016-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Crypto, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jira-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/jira-report.html -->

<!-- page_index: 12 -->

# Apache Commons Crypto – JIRA Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
DOC2MDPLACEHOLDERTOKEN0END<h2><a name="JIRA_Report"></a>JIRA Report</h2>
<table>
<tr>
<th>Fix Version</th>
<th>Key</th>
<th>Component</th>
<th>Summary</th>
<th>Type</th>
<th>Resolution</th>
<th>Status</th></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-129">CRYPTO-129</a></td>
<td></td>
<td>Change access of instance variables from package private to private (or protected if appropriate)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-127">CRYPTO-127</a></td>
<td></td>
<td>CryptoInputStream#read should handle non-block case</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-124">CRYPTO-124</a></td>
<td></td>
<td>Fix JavaCryptoRandom extend java.util.Random</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-123">CRYPTO-123</a></td>
<td></td>
<td>Clean CRYPTO build script</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-122">CRYPTO-122</a></td>
<td>Document</td>
<td>Fix CRYPTO website after 1.0.0</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-119">CRYPTO-119</a></td>
<td></td>
<td>Fix checkstyle issues</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-118">CRYPTO-118</a></td>
<td></td>
<td>Fix pmd and findbugs issues</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-117">CRYPTO-117</a></td>
<td></td>
<td>Define WINDOWS when _WIN64 and CYGWIN defined </td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-116">CRYPTO-116</a></td>
<td></td>
<td>Fix compile error at 64 bits Windows</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-99">CRYPTO-99</a></td>
<td></td>
<td>Makefile clean removes too much</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-96">CRYPTO-96</a></td>
<td></td>
<td>OpenSSL Random implementation silently falls back to Java</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-89">CRYPTO-89</a></td>
<td></td>
<td>more robust native code to eliminate memory leak</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-86">CRYPTO-86</a></td>
<td></td>
<td>What purpose does the Properties instance serve?</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-85">CRYPTO-85</a></td>
<td></td>
<td>CryptoCipher ENCRYPT_MODE and DECRYPT_MODE are unnecessary and confusing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-84">CRYPTO-84</a></td>
<td></td>
<td>Utils.getJCEProvider belongs in JceCipher class</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-83">CRYPTO-83</a></td>
<td></td>
<td>Utils.getRandomDevPath should be private method in OsCryptoRandom</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-82">CRYPTO-82</a></td>
<td></td>
<td>CipherTransformation is an enum which limits the possible transformations</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-81">CRYPTO-81</a></td>
<td></td>
<td>improve factory api for constructing Random &amp; Cipher</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-80">CRYPTO-80</a></td>
<td></td>
<td>Fix the PMD error.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-79">CRYPTO-79</a></td>
<td></td>
<td>Fix the javadoc based on the checkstyle.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-77">CRYPTO-77</a></td>
<td></td>
<td>Hide Stream's Ctor with cipher parameter</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-76">CRYPTO-76</a></td>
<td></td>
<td>Remove log dependence</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-75">CRYPTO-75</a></td>
<td></td>
<td>ConfigurationKeys#COMMONS_CRYPTO_CIPHER_CLASSES_DEFAULT is not guaranteed constant</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-72">CRYPTO-72</a></td>
<td></td>
<td>CryptoCipherFactory.getInstance does unnecessary class instantiation</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-66">CRYPTO-66</a></td>
<td></td>
<td>Warnings compiling - bootstrap class path not set</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-64">CRYPTO-64</a></td>
<td></td>
<td>Code uses sun classes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-152">CRYPTO-152</a></td>
<td></td>
<td>Bump maven-antrun-plugin from 1.8 to 3.0.0</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-91">CRYPTO-91</a></td>
<td></td>
<td>Drop the fallback property and implementation</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-88">CRYPTO-88</a></td>
<td></td>
<td>ConfigurationKeys constants could have much shorter names</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-87">CRYPTO-87</a></td>
<td></td>
<td>Reduce util package API footprint </td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-78">CRYPTO-78</a></td>
<td></td>
<td>Upgrade JDK from 1.6 to 1.7</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-74">CRYPTO-74</a></td>
<td></td>
<td>Full class names make code more difficult to update</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-71">CRYPTO-71</a></td>
<td></td>
<td> Hide the implementation of OpensslCipher</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-69">CRYPTO-69</a></td>
<td>Build</td>
<td>Activate Travis CI</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-67">CRYPTO-67</a></td>
<td></td>
<td>Makefile should use variable for the source and target Java version</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-56">CRYPTO-56</a></td>
<td></td>
<td>add informative error message, keep consistent with JDK</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-52">CRYPTO-52</a></td>
<td></td>
<td>Improve assertion message when test fails due to lack of JCE Unlimited Strength Jurisdiction Policy Files.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-146">CRYPTO-146</a></td>
<td></td>
<td>Create new release to major repositories</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-163">CRYPTO-163</a></td>
<td></td>
<td>Makefile does not recompile objects if local include files are changed</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-160">CRYPTO-160</a></td>
<td></td>
<td>Package-private class JavaCryptoRandom extends Random but should not</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-155">CRYPTO-155</a></td>
<td></td>
<td>Minor improvement</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-154">CRYPTO-154</a></td>
<td></td>
<td>License header should be a plain comment</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-153">CRYPTO-153</a></td>
<td></td>
<td>Bump coveralls-maven-plugin from 3.1.0 to 4.3.0</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-151">CRYPTO-151</a></td>
<td></td>
<td>Migrate to Junit 5</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-149">CRYPTO-149</a></td>
<td>Cipher</td>
<td>Intermittent Failure in GCMCipherTest#testGcmTamperedData()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-141">CRYPTO-141</a></td>
<td>Native</td>
<td>Errors in native code can leave Java wrappers in bad state</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-138">CRYPTO-138</a></td>
<td>Cipher</td>
<td>CipherByteArrayExample fails on openssl 1.1.0g with java.lang.UnsatisfiedLinkError: EVP_CIPHER_CTX_cleanup</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-137">CRYPTO-137</a></td>
<td>Build, Native</td>
<td>Error compiling on Win64 with Mingw</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-134">CRYPTO-134</a></td>
<td>Document</td>
<td>CipherByteBufferExample should not truncate the string</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-128">CRYPTO-128</a></td>
<td>Stream</td>
<td>Make constructors of CryptoOutputStream and CryptoInputStream are public</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-125">CRYPTO-125</a></td>
<td>Stream</td>
<td>CryptoOutputStream does not call write in a loop when underlying channel works in non-block mode.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-131">CRYPTO-131</a></td>
<td>Document</td>
<td>Provide FAQ page</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-59">CRYPTO-59</a></td>
<td></td>
<td>Support Galois/Counter Mode (GCM)</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-139">CRYPTO-139</a></td>
<td></td>
<td>Add support for AARCH64</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-148">CRYPTO-148</a></td>
<td>Build</td>
<td>Releasing Commons Crypto with AArch64 support</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-114">CRYPTO-114</a></td>
<td></td>
<td>exception.c/exception.h are not used</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-113">CRYPTO-113</a></td>
<td></td>
<td>Improve error reporting by factories</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-108">CRYPTO-108</a></td>
<td></td>
<td>OpenSSL does not handle Native code loading failure</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-107">CRYPTO-107</a></td>
<td></td>
<td>NativeCodeLoader fails to handle UnsatisfiedLinkError</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-106">CRYPTO-106</a></td>
<td></td>
<td>CryptoRandomFactory only handles ClassCast and ClassNotFound</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-103">CRYPTO-103</a></td>
<td></td>
<td>NativeCodeLoader.getVersion() is not needed</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-102">CRYPTO-102</a></td>
<td></td>
<td>Makefile.common defines JAVA/JAVAH/JAVAC incorrectly for Windows</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-101">CRYPTO-101</a></td>
<td></td>
<td>Makefile does not use correct PATH separator for Windows</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-98">CRYPTO-98</a></td>
<td></td>
<td>Makefile does not use MVN or TAR variables</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-97">CRYPTO-97</a></td>
<td></td>
<td>Code uses System.err/System.out</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-95">CRYPTO-95</a></td>
<td></td>
<td>Code should never catch Throwable</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-94">CRYPTO-94</a></td>
<td></td>
<td>Consistently camel-case type names</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-93">CRYPTO-93</a></td>
<td></td>
<td>add a factory method to provide simpler API</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-90">CRYPTO-90</a></td>
<td></td>
<td>Utils loads system properties during class loading</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-65">CRYPTO-65</a></td>
<td></td>
<td>Warnings compiling on MacOSX - JNIEXPORT redefined</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-61">CRYPTO-61</a></td>
<td></td>
<td>possible NPE in OpensslCryptoRandom if OpensslCryptoRandomNative.nextRandBytes fails</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-45">CRYPTO-45</a></td>
<td>Document</td>
<td>Document how to build Commons Crypto</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-39">CRYPTO-39</a></td>
<td></td>
<td>Fix code style violation</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-36">CRYPTO-36</a></td>
<td>Document</td>
<td>Fix crypto web link</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-34">CRYPTO-34</a></td>
<td>SecureRandom</td>
<td>JavaSecureRandom should throw Exception if it cannot create the instance</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-33">CRYPTO-33</a></td>
<td>SecureRandom</td>
<td>SecureRandom shadows JVM class</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-32">CRYPTO-32</a></td>
<td>Build</td>
<td>Add missing @Overrides</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-30">CRYPTO-30</a></td>
<td>Stream</td>
<td>Mutable fields should be private</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-29">CRYPTO-29</a></td>
<td>Cipher</td>
<td>Make sure Cipher.ENCRYPT_MODE is consistent with JDK</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-27">CRYPTO-27</a></td>
<td>Document</td>
<td>Sync Javadoc of stream in stream package</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-26">CRYPTO-26</a></td>
<td>Document</td>
<td>Utility classes should not have public constructors</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-25">CRYPTO-25</a></td>
<td>Document</td>
<td>Add download_crypto.cgi to exclude list of rat check</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-8">CRYPTO-8</a></td>
<td>Document, Stream</td>
<td>Add the package-info for input, output and stream</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-3">CRYPTO-3</a></td>
<td>Cipher</td>
<td>Change default cipher as OpensslCipher</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-1">CRYPTO-1</a></td>
<td></td>
<td>Prepare Apache Commons Crypto for Apache release</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-112">CRYPTO-112</a></td>
<td></td>
<td>OpenSslCipher.loadingFailureReason should be a Throwable</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-105">CRYPTO-105</a></td>
<td></td>
<td>Eliminate Configuration class</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-100">CRYPTO-100</a></td>
<td></td>
<td>Makefile does not need to include VERSION file</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-92">CRYPTO-92</a></td>
<td></td>
<td>Handling default properties; allow SystemProperties to be ignored</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-68">CRYPTO-68</a></td>
<td>Build, Document</td>
<td>Enable common code quality reports</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-63">CRYPTO-63</a></td>
<td></td>
<td>Add JNA binding</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-62">CRYPTO-62</a></td>
<td></td>
<td>Add multithreaded related tests and javadoc comments</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-58">CRYPTO-58</a></td>
<td>Build</td>
<td>Generate VERSION file using maven build</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-57">CRYPTO-57</a></td>
<td>Build</td>
<td>Fix build on Mac OS</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-42">CRYPTO-42</a></td>
<td>Native</td>
<td>Remove the header files required for cross platform compilation</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-40">CRYPTO-40</a></td>
<td>Cipher, SecureRandom, Stream</td>
<td>Remove the full qualified package name for shadowed classes</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-35">CRYPTO-35</a></td>
<td>Document</td>
<td>Update the issue-tracking.xml file</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-31">CRYPTO-31</a></td>
<td>Stream</td>
<td>Make fields final wherever possible</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-13">CRYPTO-13</a></td>
<td>Cipher</td>
<td>The API differences between apache.commons.crypto and JCE</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.0</td>
<td><a href="https://issues.apache.org/jira/browse/CRYPTO-12">CRYPTO-12</a></td>
<td>Stream</td>
<td>Rename CryptoInputStream to CipherInputStream and CryptoOutputStream to CipherOutputStream</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2016-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Crypto, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="surefire-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/surefire-report.html -->

<!-- page_index: 13 -->

# Apache Commons Crypto – Surefire Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
DOC2MDPLACEHOLDERTOKEN0END<h2><a name="Surefire_Report"></a>Surefire Report</h2></section><section>
DOC2MDPLACEHOLDERTOKEN1END<h2><a name="Summary"></a>Summary</h2><a name="Summary"></a>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p>
<table>
<tr>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left">140</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">97.857%</td>
<td align="left">2.043</td></tr></table>
<p>Note: failures are anticipated and checked for with assertions while errors are unanticipated.</p>
</section><section>
DOC2MDPLACEHOLDERTOKEN2END<h2><a name="Package_List"></a>Package List</h2><a name="Package_List"></a>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p>
<table>
<tr>
<th>Package</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.output">org.apache.commons.crypto.stream.output</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto">org.apache.commons.crypto</a></td>
<td align="left">10</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">70%</td>
<td align="left">0.287</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream">org.apache.commons.crypto.stream</a></td>
<td align="left">27</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.48</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random">org.apache.commons.crypto.random</a></td>
<td align="left">19</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.508</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna">org.apache.commons.crypto.jna</a></td>
<td align="left">34</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.606</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher">org.apache.commons.crypto.cipher</a></td>
<td align="left">43</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.149</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.utils">org.apache.commons.crypto.utils</a></td>
<td align="left">5</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.009</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.input">org.apache.commons.crypto.stream.input</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.002</td></tr></table>
<p>Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.</p><section>
DOC2MDPLACEHOLDERTOKEN3END<h3><a name="org.apache.commons.crypto.stream.output"></a>org.apache.commons.crypto.stream.output</h3><a name="org.apache.commons.crypto.stream.output"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.output.streamoutputtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.output.streamoutputtest">StreamOutputTest</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.002</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN4END<h3><a name="org.apache.commons.crypto"></a>org.apache.commons.crypto</h3><a name="org.apache.commons.crypto"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cryptotest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cryptotest">CryptoTest</a></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.256</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest">NativeCodeLoaderTest</a></td>
<td align="left">5</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">3</td>
<td align="left">40%</td>
<td align="left">0.03</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.osinfotest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.osinfotest">OsInfoTest</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN5END<h3><a name="org.apache.commons.crypto.stream"></a>org.apache.commons.crypto.stream</h3><a name="org.apache.commons.crypto.stream"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.cbcnopaddingcipherstreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.cbcnopaddingcipherstreamtest">CbcNoPaddingCipherStreamTest</a></td>
<td align="left">6</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.045</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.ctrcryptostreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.ctrcryptostreamtest">CtrCryptoStreamTest</a></td>
<td align="left">7</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.061</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.positionedcryptoinputstreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.positionedcryptoinputstreamtest">PositionedCryptoInputStreamTest</a></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.038</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.ctrnopaddingcipherstreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.ctrnopaddingcipherstreamtest">CtrNoPaddingCipherStreamTest</a></td>
<td align="left">6</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.227</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.cbcpkcs5paddingcipherstreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.cbcpkcs5paddingcipherstreamtest">CbcPkcs5PaddingCipherStreamTest</a></td>
<td align="left">6</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.109</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN6END<h3><a name="org.apache.commons.crypto.random"></a>org.apache.commons.crypto.random</h3><a name="org.apache.commons.crypto.random"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.javacryptorandomtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.javacryptorandomtest">JavaCryptoRandomTest</a></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.395</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.opensslcryptorandomtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.opensslcryptorandomtest">OpenSslCryptoRandomTest</a></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.034</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.cryptorandomfactorytest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.cryptorandomfactorytest">CryptoRandomFactoryTest</a></td>
<td align="left">12</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.014</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.oscryptorandomtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.random.oscryptorandomtest">OsCryptoRandomTest</a></td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.065</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN7END<h3><a name="org.apache.commons.crypto.jna"></a>org.apache.commons.crypto.jna</h3><a name="org.apache.commons.crypto.jna"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.ctrnopaddingcipherjnastreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.ctrnopaddingcipherjnastreamtest">CtrNoPaddingCipherJnaStreamTest</a></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.034</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.openssljnaciphertest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.openssljnaciphertest">OpenSslJnaCipherTest</a></td>
<td align="left">11</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.036</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.cbcnopaddingcipherjnastreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.cbcnopaddingcipherjnastreamtest">CbcNoPaddingCipherJnaStreamTest</a></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.05</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.opensslnativejnatest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.opensslnativejnatest">OpenSslNativeJnaTest</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.051</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.ctrcryptojnastreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.ctrcryptojnastreamtest">CtrCryptoJnaStreamTest</a></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.228</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.openssljnatest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.openssljnatest">OpenSslJnaTest</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.openssljnacryptorandomtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.openssljnacryptorandomtest">OpenSslJnaCryptoRandomTest</a></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.137</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.positionedcryptoinputstreamjnatest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.positionedcryptoinputstreamjnatest">PositionedCryptoInputStreamJnaTest</a></td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.047</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.cbcpkcs5paddingcipherjnastreamtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.jna.cbcpkcs5paddingcipherjnastreamtest">CbcPkcs5PaddingCipherJnaStreamTest</a></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.022</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN8END<h3><a name="org.apache.commons.crypto.cipher"></a>org.apache.commons.crypto.cipher</h3><a name="org.apache.commons.crypto.cipher"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.cryptociphertest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.cryptociphertest">CryptoCipherTest</a></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.004</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.jceciphertest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.jceciphertest">JceCipherTest</a></td>
<td align="left">11</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.036</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.opensslciphertest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.opensslciphertest">OpenSslCipherTest</a></td>
<td align="left">16</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.053</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.gcmciphertest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.gcmciphertest">GcmCipherTest</a></td>
<td align="left">8</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.034</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.cryptocipherfactorytest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.cryptocipherfactorytest">CryptoCipherFactoryTest</a></td>
<td align="left">5</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.02</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.opensslcommonmodetest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.cipher.opensslcommonmodetest">OpenSslCommonModeTest</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.002</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN9END<h3><a name="org.apache.commons.crypto.utils"></a>org.apache.commons.crypto.utils</h3><a name="org.apache.commons.crypto.utils"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.utils.enumtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.utils.enumtest">EnumTest</a></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.006</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.utils.utilstest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.utils.utilstest">UtilsTest</a></td>
<td align="left">3</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.003</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN10END<h3><a name="org.apache.commons.crypto.stream.input"></a>org.apache.commons.crypto.stream.input</h3><a name="org.apache.commons.crypto.stream.input"></a>
<table>
<tr>
<th></th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.input.channelinputtest"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></a></td>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.stream.input.channelinputtest">ChannelInputTest</a></td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">0</td>
<td align="left">100%</td>
<td align="left">0.002</td></tr></table></section>
</section><section>
DOC2MDPLACEHOLDERTOKEN11END<h2><a name="Test_Cases"></a>Test Cases</h2><a name="Test_Cases"></a>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p><section>
DOC2MDPLACEHOLDERTOKEN12END<h3><a name="JavaCryptoRandomTest"></a>JavaCryptoRandomTest</h3><a name="org.apache.commons.crypto.random.JavaCryptoRandomTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.JavaCryptoRandomTest.testRandomBytes"></a>testRandomBytes</td>
<td align="left">0.041</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.JavaCryptoRandomTest.testRandomBytesMultiThreaded"></a>testRandomBytesMultiThreaded</td>
<td align="left">0.351</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN13END<h3><a name="OpenSslCryptoRandomTest"></a>OpenSslCryptoRandomTest</h3><a name="org.apache.commons.crypto.random.OpenSslCryptoRandomTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.OpenSslCryptoRandomTest.testRandomBytes"></a>testRandomBytes</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.OpenSslCryptoRandomTest.testRandomBytesMultiThreaded"></a>testRandomBytesMultiThreaded</td>
<td align="left">0.032</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN14END<h3><a name="CtrNoPaddingCipherJnaStreamTest"></a>CtrNoPaddingCipherJnaStreamTest</h3><a name="org.apache.commons.crypto.jna.CtrNoPaddingCipherJnaStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrNoPaddingCipherJnaStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrNoPaddingCipherJnaStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.005</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrNoPaddingCipherJnaStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrNoPaddingCipherJnaStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.021</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN15END<h3><a name="OpenSslJnaCipherTest"></a>OpenSslJnaCipherTest</h3><a name="org.apache.commons.crypto.jna.OpenSslJnaCipherTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.closeTestRepeat"></a>closeTestRepeat</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.cryptoTest"></a>cryptoTest</td>
<td align="left">0.015</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.testInvalidIV"></a>testInvalidIV</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.testInvalidTransform"></a>testInvalidTransform</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.closeTestAfterInit"></a>closeTestAfterInit</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.testInvalidIVClass"></a>testInvalidIVClass</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.testNullTransform"></a>testNullTransform</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.reInitAfterClose"></a>reInitAfterClose</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.reInitTest"></a>reInitTest</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.testInvalidKey"></a>testInvalidKey</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCipherTest.closeTestNoInit"></a>closeTestNoInit</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN16END<h3><a name="CbcNoPaddingCipherJnaStreamTest"></a>CbcNoPaddingCipherJnaStreamTest</h3><a name="org.apache.commons.crypto.jna.CbcNoPaddingCipherJnaStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcNoPaddingCipherJnaStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.02</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcNoPaddingCipherJnaStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcNoPaddingCipherJnaStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcNoPaddingCipherJnaStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.02</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN17END<h3><a name="OpenSslNativeJnaTest"></a>OpenSslNativeJnaTest</h3><a name="org.apache.commons.crypto.jna.OpenSslNativeJnaTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslNativeJnaTest.testTestReporter"></a>test(TestReporter)</td>
<td align="left">0.048</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN18END<h3><a name="CryptoCipherTest"></a>CryptoCipherTest</h3><a name="org.apache.commons.crypto.cipher.CryptoCipherTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherTest.testUpdateAADByteBuffer"></a>testUpdateAADByteBuffer</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherTest.testUpdateAADByteArray"></a>testUpdateAADByteArray</td>
<td align="left">0</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN19END<h3><a name="EnumTest"></a>EnumTest</h3><a name="org.apache.commons.crypto.utils.EnumTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.utils.EnumTest.testCipher"></a>testCipher</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.utils.EnumTest.testRandom"></a>testRandom</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN20END<h3><a name="CbcNoPaddingCipherStreamTest"></a>CbcNoPaddingCipherStreamTest</h3><a name="org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.004</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.022</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest.testByteBufferRead"></a>testByteBufferRead</td>
<td align="left">0.007</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcNoPaddingCipherStreamTest.testByteBufferWrite"></a>testByteBufferWrite</td>
<td align="left">0.003</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN21END<h3><a name="CtrCryptoStreamTest"></a>CtrCryptoStreamTest</h3><a name="org.apache.commons.crypto.stream.CtrCryptoStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.004</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.023</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testByteBufferRead"></a>testByteBufferRead</td>
<td align="left">0.013</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.004</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testByteBufferWrite"></a>testByteBufferWrite</td>
<td align="left">0.004</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrCryptoStreamTest.testDecrypt"></a>testDecrypt</td>
<td align="left">0.003</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN22END<h3><a name="CtrCryptoJnaStreamTest"></a>CtrCryptoJnaStreamTest</h3><a name="org.apache.commons.crypto.jna.CtrCryptoJnaStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrCryptoJnaStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.203</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrCryptoJnaStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrCryptoJnaStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CtrCryptoJnaStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.013</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN23END<h3><a name="OpenSslJnaTest"></a>OpenSslJnaTest</h3><a name="org.apache.commons.crypto.jna.OpenSslJnaTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaTest.testMain"></a>testMain</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN24END<h3><a name="StreamOutputTest"></a>StreamOutputTest</h3><a name="org.apache.commons.crypto.stream.output.StreamOutputTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.output.StreamOutputTest.testGetOut"></a>testGetOut</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN25END<h3><a name="OpenSslJnaCryptoRandomTest"></a>OpenSslJnaCryptoRandomTest</h3><a name="org.apache.commons.crypto.jna.OpenSslJnaCryptoRandomTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCryptoRandomTest.testRandomBytes"></a>testRandomBytes</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.OpenSslJnaCryptoRandomTest.testRandomBytesMultiThreaded"></a>testRandomBytesMultiThreaded</td>
<td align="left">0.133</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN26END<h3><a name="CryptoTest"></a>CryptoTest</h3><a name="org.apache.commons.crypto.CryptoTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.CryptoTest.testLoadingError"></a>testLoadingError</td>
<td align="left">0.175</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.CryptoTest.testMain"></a>testMain</td>
<td align="left">0.054</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.CryptoTest.testGetComponentName"></a>testGetComponentName</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.CryptoTest.testGetComponentVersion"></a>testGetComponentVersion</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN27END<h3><a name="CryptoRandomFactoryTest"></a>CryptoRandomFactoryTest</h3><a name="org.apache.commons.crypto.random.CryptoRandomFactoryTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testDefaultRandom"></a>testDefaultRandom</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testDefaultRandomClass"></a>testDefaultRandomClass</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testEmpty"></a>testEmpty</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testNull"></a>testNull</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testFailingRandom"></a>testFailingRandom</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testGetOSRandom"></a>testGetOSRandom</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testInvalidRandom"></a>testInvalidRandom</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testAbstractRandom"></a>testAbstractRandom</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testDummmyRandom"></a>testDummmyRandom</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testInvalidRandomClass"></a>testInvalidRandomClass</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testFullClassName"></a>testFullClassName</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.CryptoRandomFactoryTest.testNoClasses"></a>testNoClasses</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN28END<h3><a name="ChannelInputTest"></a>ChannelInputTest</h3><a name="org.apache.commons.crypto.stream.input.ChannelInputTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.input.ChannelInputTest.testSkipWithSkipBuffer"></a>testSkipWithSkipBuffer</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN29END<h3><a name="NativeCodeLoaderTest"></a>NativeCodeLoaderTest</h3><a name="org.apache.commons.crypto.NativeCodeLoaderTest"></a>
<table>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest.testunsuccessfulload"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></a></td>
<td align="left"><a name="TC_org.apache.commons.crypto.NativeCodeLoaderTest.testUnSuccessfulLoad"></a><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest.testunsuccessfulload">testUnSuccessfulLoad</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.crypto.NativeCodeLoaderTest.testUnSuccessfulLoad');"><span id="org.apache.commons.crypto.NativeCodeLoaderTest.testUnSuccessfulLoad-off"> + </span><span id="org.apache.commons.crypto.NativeCodeLoaderTest.testUnSuccessfulLoad-on"> - </span>[ Detail ]</a></div></td>
<td align="left">0</td></tr>
<tr>
<td align="left"></td>
<td align="left">Seems to cause issues with other tests on Linux; disable for now</td>
<td align="left"></td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.NativeCodeLoaderTest.test"></a>test</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest.testcanloadifpresent"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></a></td>
<td align="left"><a name="TC_org.apache.commons.crypto.NativeCodeLoaderTest.testCanLoadIfPresent"></a><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest.testcanloadifpresent">testCanLoadIfPresent</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.crypto.NativeCodeLoaderTest.testCanLoadIfPresent');"><span id="org.apache.commons.crypto.NativeCodeLoaderTest.testCanLoadIfPresent-off"> + </span><span id="org.apache.commons.crypto.NativeCodeLoaderTest.testCanLoadIfPresent-on"> - </span>[ Detail ]</a></div></td>
<td align="left">0</td></tr>
<tr>
<td align="left"></td>
<td align="left">Causes crash on Ubuntu when compiled with Java 17</td>
<td align="left"></td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.NativeCodeLoaderTest.testNativePresent"></a>testNativePresent</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest.testnativenotpresent"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></a></td>
<td align="left"><a name="TC_org.apache.commons.crypto.NativeCodeLoaderTest.testNativeNotPresent"></a><a href="#surefire-report--org.apache.commons.crypto.nativecodeloadertest.testnativenotpresent">testNativeNotPresent</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.crypto.NativeCodeLoaderTest.testNativeNotPresent');"><span id="org.apache.commons.crypto.NativeCodeLoaderTest.testNativeNotPresent-off"> + </span><span id="org.apache.commons.crypto.NativeCodeLoaderTest.testNativeNotPresent-on"> - </span>[ Detail ]</a></div></td>
<td align="left">0</td></tr>
<tr>
<td align="left"></td>
<td align="left">skipped</td>
<td align="left"></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN30END<h3><a name="JceCipherTest"></a>JceCipherTest</h3><a name="org.apache.commons.crypto.cipher.JceCipherTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.closeTestRepeat"></a>closeTestRepeat</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.cryptoTest"></a>cryptoTest</td>
<td align="left">0.016</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.testInvalidIV"></a>testInvalidIV</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.testInvalidTransform"></a>testInvalidTransform</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.closeTestAfterInit"></a>closeTestAfterInit</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.testInvalidIVClass"></a>testInvalidIVClass</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.testNullTransform"></a>testNullTransform</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.reInitAfterClose"></a>reInitAfterClose</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.reInitTest"></a>reInitTest</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.testInvalidKey"></a>testInvalidKey</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.JceCipherTest.closeTestNoInit"></a>closeTestNoInit</td>
<td align="left">0</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN31END<h3><a name="UtilsTest"></a>UtilsTest</h3><a name="org.apache.commons.crypto.utils.UtilsTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.utils.UtilsTest.testGetProperties"></a>testGetProperties</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.utils.UtilsTest.testSplitNull"></a>testSplitNull</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.utils.UtilsTest.testSplitOmitEmptyLine"></a>testSplitOmitEmptyLine</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN32END<h3><a name="PositionedCryptoInputStreamTest"></a>PositionedCryptoInputStreamTest</h3><a name="org.apache.commons.crypto.stream.PositionedCryptoInputStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.PositionedCryptoInputStreamTest.doTestJCE"></a>doTestJCE</td>
<td align="left">0.026</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.PositionedCryptoInputStreamTest.doTestJNI"></a>doTestJNI</td>
<td align="left">0.01</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN33END<h3><a name="OpenSslCipherTest"></a>OpenSslCipherTest</h3><a name="org.apache.commons.crypto.cipher.OpenSslCipherTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.closeTestRepeat"></a>closeTestRepeat</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.cryptoTest"></a>cryptoTest</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testInvalidTransform"></a>testInvalidTransform</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.closeTestAfterInit"></a>closeTestAfterInit</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testNullTransform"></a>testNullTransform</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.reInitAfterClose"></a>reInitAfterClose</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.reInitTest"></a>reInitTest</td>
<td align="left">0</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.closeTestNoInit"></a>closeTestNoInit</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testInvalidMode"></a>testInvalidMode</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testInvalidIV"></a>testInvalidIV</td>
<td align="left">0.004</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testCipherLifecycle"></a>testCipherLifecycle</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testUpdateArguments"></a>testUpdateArguments</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testInvalidIVClass"></a>testInvalidIVClass</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testDoFinalArguments"></a>testDoFinalArguments</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testInvalidKey"></a>testInvalidKey</td>
<td align="left">0.005</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCipherTest.testInvalidPadding"></a>testInvalidPadding</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN34END<h3><a name="GcmCipherTest"></a>GcmCipherTest</h3><a name="org.apache.commons.crypto.cipher.GcmCipherTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGMac"></a>testGMac</td>
<td align="left">0.005</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGcmTamperedData"></a>testGcmTamperedData</td>
<td align="left">0.008</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGcmNistCase2"></a>testGcmNistCase2</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGcmNistCase4"></a>testGcmNistCase4</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGcmNistCase5"></a>testGcmNistCase5</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGcmNistCase6"></a>testGcmNistCase6</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGcmNistCases"></a>testGcmNistCases</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.GcmCipherTest.testGMacTamperedData"></a>testGMacTamperedData</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN35END<h3><a name="CryptoCipherFactoryTest"></a>CryptoCipherFactoryTest</h3><a name="org.apache.commons.crypto.cipher.CryptoCipherFactoryTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherFactoryTest.testDefaultCipher"></a>testDefaultCipher</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherFactoryTest.testEmptyCipher"></a>testEmptyCipher</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherFactoryTest.testInvalidTransformation"></a>testInvalidTransformation</td>
<td align="left">0.01</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherFactoryTest.testInvalidCipher"></a>testInvalidCipher</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.CryptoCipherFactoryTest.testNoCipher"></a>testNoCipher</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN36END<h3><a name="OsCryptoRandomTest"></a>OsCryptoRandomTest</h3><a name="org.apache.commons.crypto.random.OsCryptoRandomTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.OsCryptoRandomTest.testRandomBytes"></a>testRandomBytes</td>
<td align="left">0.001</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.OsCryptoRandomTest.testRandomBytesMultiThreaded"></a>testRandomBytesMultiThreaded</td>
<td align="left">0.063</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.random.OsCryptoRandomTest.testInvalidRandom"></a>testInvalidRandom</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN37END<h3><a name="CtrNoPaddingCipherStreamTest"></a>CtrNoPaddingCipherStreamTest</h3><a name="org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.121</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.015</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.055</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest.testByteBufferRead"></a>testByteBufferRead</td>
<td align="left">0.022</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CtrNoPaddingCipherStreamTest.testByteBufferWrite"></a>testByteBufferWrite</td>
<td align="left">0.006</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN38END<h3><a name="CbcPkcs5PaddingCipherStreamTest"></a>CbcPkcs5PaddingCipherStreamTest</h3><a name="org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.005</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.012</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.06</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest.testByteBufferRead"></a>testByteBufferRead</td>
<td align="left">0.02</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.stream.CbcPkcs5PaddingCipherStreamTest.testByteBufferWrite"></a>testByteBufferWrite</td>
<td align="left">0.004</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN39END<h3><a name="OsInfoTest"></a>OsInfoTest</h3><a name="org.apache.commons.crypto.OsInfoTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.OsInfoTest.testMain"></a>testMain</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN40END<h3><a name="PositionedCryptoInputStreamJnaTest"></a>PositionedCryptoInputStreamJnaTest</h3><a name="org.apache.commons.crypto.jna.PositionedCryptoInputStreamJnaTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.PositionedCryptoInputStreamJnaTest.doTestJCE"></a>doTestJCE</td>
<td align="left">0.007</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.PositionedCryptoInputStreamJnaTest.doTestJNI"></a>doTestJNI</td>
<td align="left">0.01</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.PositionedCryptoInputStreamJnaTest.doTest"></a>doTest</td>
<td align="left">0.026</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN41END<h3><a name="OpenSslCommonModeTest"></a>OpenSslCommonModeTest</h3><a name="org.apache.commons.crypto.cipher.OpenSslCommonModeTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.cipher.OpenSslCommonModeTest.testUpdateAAD"></a>testUpdateAAD</td>
<td align="left">0.001</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN42END<h3><a name="CbcPkcs5PaddingCipherJnaStreamTest"></a>CbcPkcs5PaddingCipherJnaStreamTest</h3><a name="org.apache.commons.crypto.jna.CbcPkcs5PaddingCipherJnaStreamTest"></a>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcPkcs5PaddingCipherJnaStreamTest.testExceptions"></a>testExceptions</td>
<td align="left">0.003</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcPkcs5PaddingCipherJnaStreamTest.testFieldGetters"></a>testFieldGetters</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcPkcs5PaddingCipherJnaStreamTest.testSkip"></a>testSkip</td>
<td align="left">0.002</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-success-sml_eac60f51adab3cf7.gif"/></figure></td>
<td align="left"><a name="TC_org.apache.commons.crypto.jna.CbcPkcs5PaddingCipherJnaStreamTest.testReadWrite"></a>testReadWrite</td>
<td align="left">0.013</td></tr></table></section>
</section><section>
DOC2MDPLACEHOLDERTOKEN43END<h2><a name="Failure_Details"></a>Failure Details</h2><a name="Failure_Details"></a>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p>
<table>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></td>
<td align="left"><a name="org.apache.commons.crypto.NativeCodeLoaderTest.testUnSuccessfulLoad"></a>testUnSuccessfulLoad</td></tr>
<tr>
<td align="left"></td>
<td align="left">skipped: Seems to cause issues with other tests on Linux; disable for now</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></td>
<td align="left"><a name="org.apache.commons.crypto.NativeCodeLoaderTest.testCanLoadIfPresent"></a>testCanLoadIfPresent</td></tr>
<tr>
<td align="left"></td>
<td align="left">skipped: Causes crash on Ubuntu when compiled with Java 17</td></tr>
<tr>
<td align="left"><figure><img alt="" src="assets/images/icon-warning-sml_fe3c4601c86c9f28.gif"/></figure></td>
<td align="left"><a name="org.apache.commons.crypto.NativeCodeLoaderTest.testNativeNotPresent"></a>testNativeNotPresent</td></tr>
<tr>
<td align="left"></td>
<td align="left">skipped: skipped</td></tr></table>
</section>
</td>
</tr>
</table>

Copyright © 2016-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Crypto, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/rat-report.html -->

<!-- page_index: 14 -->

# Apache Commons Crypto – Rat (Release Audit Tool) results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
DOC2MDPLACEHOLDERTOKEN0END<h2><a name="Rat_.28Release_Audit_Tool.29_results"></a>Rat (Release Audit Tool) results</h2>
<p>The following document contains the results of <a href="https://creadur.apache.org/rat/apache-rat-plugin/">Rat (Release Audit Tool)</a>.</p>
<p></p>
<div>
<pre>
*****************************************************
Summary
-------
Generated at: 2023-01-23T09:17:51-05:00

Notes: 4
Binaries: 1
Archives: 0
Standards: 147

Apache Licensed: 147
Generated Documents: 0

JavaDocs are generated, thus a license header is optional.
Generated files do not require license headers.

0 Unknown Licenses

*****************************************************
  Files with Apache License headers will be marked AL
  Binary files (which do not require any license headers) will be marked B
  Compressed archives will be marked A
  Notices, licenses etc. will be marked N
  AL    CODE_OF_CONDUCT.md
  AL    PROPOSAL.html
  AL    Makefile
  N     RELEASE-NOTES.txt
  AL    pom.xml
  AL    Makefile.common
  AL    README.md
  N     NOTICE.txt
  AL    CONTRIBUTING.md
  AL    .github/GH-ROBOTS.txt
  AL    .github/workflows/coverage.yml
  AL    .github/workflows/maven.yml
  AL    .github/workflows/codeql-analysis.yml
  AL    .github/workflows/scorecards-analysis.yml
  AL    .github/workflows/adhoctest.yml
  AL    .github/dependabot.yml
  AL    checkstyle.xml
  AL    lib/include/config.h
  N     BUILDING.txt
  N     LICENSE.txt
  AL    SECURITY.md
  AL    src/docker/docker-compose.yaml
  AL    src/docker/tests.sh
  AL    src/docker/Dockerfile
  AL    src/docker/README.md
  AL    src/docker/build_linux32.sh
  AL    src/docker/build.sh
  AL    src/test/java/org/apache/commons/crypto/AbstractBenchmark.java
  AL    src/test/java/org/apache/commons/crypto/OsInfoTest.java
  AL    src/test/java/org/apache/commons/crypto/NativeCodeLoaderTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/CtrNoPaddingCipherStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/input/ChannelInputTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/output/StreamOutputTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/AbstractCipherStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/CtrCryptoStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/CbcNoPaddingCipherStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/PositionedCryptoInputStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/stream/CbcPkcs5PaddingCipherStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/OpenSslCommonModeTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/DefaultCryptoCipher.java
  AL    src/test/java/org/apache/commons/crypto/cipher/AbstractCipherTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/GcmCipherTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/OpenSslCipherTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/TestData.java
  AL    src/test/java/org/apache/commons/crypto/cipher/CryptoCipherTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/JceCipherTest.java
  AL    src/test/java/org/apache/commons/crypto/cipher/CryptoCipherFactoryTest.java
  AL    src/test/java/org/apache/commons/crypto/utils/EnumTest.java
  AL    src/test/java/org/apache/commons/crypto/utils/UtilsTest.java
  AL    src/test/java/org/apache/commons/crypto/CryptoBenchmark.java
  AL    src/test/java/org/apache/commons/crypto/examples/RandomExample.java
  AL    src/test/java/org/apache/commons/crypto/examples/CipherByteArrayExample.java
  AL    src/test/java/org/apache/commons/crypto/examples/CipherByteBufferExample.java
  AL    src/test/java/org/apache/commons/crypto/examples/StreamExample.java
  AL    src/test/java/org/apache/commons/crypto/examples/package-info.java
  AL    src/test/java/org/apache/commons/crypto/CryptoTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/OpenSslNativeJnaTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/OpenSslJnaCryptoRandomTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/CbcPkcs5PaddingCipherJnaStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/CryptoJnaBenchmark.java
  AL    src/test/java/org/apache/commons/crypto/jna/CbcNoPaddingCipherJnaStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/AbstractCipherJnaStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/CtrNoPaddingCipherJnaStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/OpenSslJnaTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/PositionedCryptoInputStreamJnaTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/CtrCryptoJnaStreamTest.java
  AL    src/test/java/org/apache/commons/crypto/jna/OpenSslJnaCipherTest.java
  AL    src/test/java/org/apache/commons/crypto/random/OsCryptoRandomTest.java
  AL    src/test/java/org/apache/commons/crypto/random/FailingRandom.java
  AL    src/test/java/org/apache/commons/crypto/random/JavaCryptoRandomTest.java
  AL    src/test/java/org/apache/commons/crypto/random/CryptoRandomFactoryTest.java
  AL    src/test/java/org/apache/commons/crypto/random/OpenSslCryptoRandomTest.java
  AL    src/test/java/org/apache/commons/crypto/random/NoopRandom.java
  AL    src/test/java/org/apache/commons/crypto/random/AbstractRandomTest.java
  AL    src/test/java/org/apache/commons/crypto/random/AbstractRandom.java
  AL    src/changes/release-notes.vm
  AL    src/changes/changes.xml
  AL    src/assembly/src.xml
  AL    src/assembly/bin.xml
  AL    src/site/resources/checkstyle/checkstyle-suppressions.xml
  AL    src/site/resources/spotbugs/spotbugs-exclude-filter.xml
  B     src/site/resources/images/logo.png
  AL    src/site/resources/pmd/pmd-ruleset.xml
  AL    src/site/xdoc/index.xml
  AL    src/site/xdoc/mail-lists.xml
  AL    src/site/xdoc/proposal.xml
  AL    src/site/xdoc/userguide.xml
  AL    src/site/xdoc/download_crypto.xml
  AL    src/site/xdoc/issue-tracking.xml
  AL    src/site/xdoc/faq.xml
  AL    src/site/xdoc/security.xml
  AL    src/site/site.xml
  AL    src/main/native/org/apache/commons/crypto/DynamicLoader.c
  AL    src/main/native/org/apache/commons/crypto/org_apache_commons_crypto.h
  AL    src/main/native/org/apache/commons/crypto/cipher/OpenSslNative.c
  AL    src/main/native/org/apache/commons/crypto/OpenSslInfoNative.c
  AL    src/main/native/org/apache/commons/crypto/random/OpenSslCryptoRandomNative.c
  AL    src/main/native/org/apache/commons/crypto/random/org_apache_commons_crypto_random.h
  AL    src/main/resources/org/apache/commons/crypto/component.properties
  AL    src/main/java/org/apache/commons/crypto/NativeCodeLoader.java
  AL    src/main/java/org/apache/commons/crypto/OpenSslInfoNative.java
  AL    src/main/java/org/apache/commons/crypto/stream/CryptoOutputStream.java
  AL    src/main/java/org/apache/commons/crypto/stream/CtrCryptoInputStream.java
  AL    src/main/java/org/apache/commons/crypto/stream/input/ChannelInput.java
  AL    src/main/java/org/apache/commons/crypto/stream/input/Input.java
  AL    src/main/java/org/apache/commons/crypto/stream/input/StreamInput.java
  AL    src/main/java/org/apache/commons/crypto/stream/input/package-info.java
  AL    src/main/java/org/apache/commons/crypto/stream/CryptoInputStream.java
  AL    src/main/java/org/apache/commons/crypto/stream/CtrCryptoOutputStream.java
  AL    src/main/java/org/apache/commons/crypto/stream/output/StreamOutput.java
  AL    src/main/java/org/apache/commons/crypto/stream/output/ChannelOutput.java
  AL    src/main/java/org/apache/commons/crypto/stream/output/Output.java
  AL    src/main/java/org/apache/commons/crypto/stream/output/package-info.java
  AL    src/main/java/org/apache/commons/crypto/stream/PositionedCryptoInputStream.java
  AL    src/main/java/org/apache/commons/crypto/stream/package-info.java
  AL    src/main/java/org/apache/commons/crypto/cipher/OpenSslEvpCtrlValues.java
  AL    src/main/java/org/apache/commons/crypto/cipher/OpenSslNative.java
  AL    src/main/java/org/apache/commons/crypto/cipher/CryptoCipherFactory.java
  AL    src/main/java/org/apache/commons/crypto/cipher/OpenSslCommonMode.java
  AL    src/main/java/org/apache/commons/crypto/cipher/OpenSslGaloisCounterMode.java
  AL    src/main/java/org/apache/commons/crypto/cipher/OpenSsl.java
  AL    src/main/java/org/apache/commons/crypto/cipher/AbstractOpenSslFeedbackCipher.java
  AL    src/main/java/org/apache/commons/crypto/cipher/JceCipher.java
  AL    src/main/java/org/apache/commons/crypto/cipher/OpenSslCipher.java
  AL    src/main/java/org/apache/commons/crypto/cipher/package-info.java
  AL    src/main/java/org/apache/commons/crypto/cipher/CryptoCipher.java
  AL    src/main/java/org/apache/commons/crypto/utils/IoUtils.java
  AL    src/main/java/org/apache/commons/crypto/utils/Transformation.java
  AL    src/main/java/org/apache/commons/crypto/utils/Utils.java
  AL    src/main/java/org/apache/commons/crypto/utils/Padding.java
  AL    src/main/java/org/apache/commons/crypto/utils/AES.java
  AL    src/main/java/org/apache/commons/crypto/utils/ReflectionUtils.java
  AL    src/main/java/org/apache/commons/crypto/utils/package-info.java
  AL    src/main/java/org/apache/commons/crypto/OsInfo.java
  AL    src/main/java/org/apache/commons/crypto/Crypto.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSslInterfaceNativeJna.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSslJnaCryptoRandom.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSslJna.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSslNativeJna.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSsl11XNativeJna.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.java
  AL    src/main/java/org/apache/commons/crypto/jna/OpenSslJnaCipher.java
  AL    src/main/java/org/apache/commons/crypto/jna/package-info.java
  AL    src/main/java/org/apache/commons/crypto/random/CryptoRandom.java
  AL    src/main/java/org/apache/commons/crypto/random/CryptoRandomFactory.java
  AL    src/main/java/org/apache/commons/crypto/random/OsCryptoRandom.java
  AL    src/main/java/org/apache/commons/crypto/random/JavaCryptoRandom.java
  AL    src/main/java/org/apache/commons/crypto/random/OpenSslCryptoRandom.java
  AL    src/main/java/org/apache/commons/crypto/random/OpenSslCryptoRandomNative.java
  AL    src/main/java/org/apache/commons/crypto/random/package-info.java
  AL    src/main/java/org/apache/commons/crypto/package-info.java

*****************************************************
</pre></div></section>
</td>
</tr>
</table>

Copyright © 2016-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Crypto, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/japicmp.html -->

<!-- page_index: 15 -->

# Apache Commons Crypto –

MODIFIED final public class org.apache.commons.crypto.jna.OpenSslJna[top](#japicmp--toc)

Methods:

<table>
<thead>
<tr>
<td>Status</td><td>Modifier</td><td>Generic Templates</td><td>Type</td><td>Method</td><td>Exceptions</td><td>Compatibility Changes:</td><td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>MODIFIED</span></td><td><span></span><span>static </span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>void</span></td><td>main(<span>java.lang.String[]</span>)</td><td>
<table>
<thead>
<tr>
<td>Status:</td><td>Name:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td>java.lang.Throwable</td>
</tr>
</tbody>
</table>
</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>82</td><td>86</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED public class org.apache.commons.crypto.stream.CryptoInputStream[top](#japicmp--toc)

Fields:

| Status | Modifier | Type | Field | Compatibility Changes: |
| --- | --- | --- | --- | --- |
| NEW | public static final | int | EOS | n.a. |

NEW public class org.apache.commons.crypto.utils.AES[top](#japicmp--toc)

Fields:

| Status | Modifier | Type | Field | Compatibility Changes: |
| --- | --- | --- | --- | --- |
| NEW | public static final | java.lang.String | ALGORITHM | n.a. |
| NEW | public static final | java.lang.String | CBC\_NO\_PADDING | n.a. |
| NEW | public static final | java.lang.String | CBC\_PKCS5\_PADDING | n.a. |
| NEW | public static final | java.lang.String | CTR\_NO\_PADDING | n.a. |

Constructors:

<table>
<thead>
<tr>
<td>Status</td><td>Modifier</td><td>Generic Templates</td><td>Constructor</td><td>Exceptions</td><td>Compatibility Changes:</td><td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td><span></span><span></span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td>AES()</td><td>n.a.</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>27</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

Methods:

<table>
<thead>
<tr>
<td>Status</td><td>Modifier</td><td>Generic Templates</td><td>Type</td><td>Method</td><td>Exceptions</td><td>Compatibility Changes:</td><td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td><span></span><span>static </span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>javax.crypto.spec.SecretKeySpec</span></td><td>newSecretKeySpec(<span>byte[]</span>)</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>54</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

NEW (Serializable compatible) final public enum org.apache.commons.crypto.utils.Padding[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| INTERFACE\_ADDED |

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| NEW | java.lang.Enum | n.a. |

Interfaces:

| Status | Interface | Compatibility Changes |
| --- | --- | --- |
| NEW | java.io.Serializable | n.a. |
| NEW | java.lang.Comparable | n.a. |

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | false | n.a. | n.a. |
| New | true | 3877649537256580291 | n.a. |

Fields:

| Status | Modifier | Type | Field | Compatibility Changes: |
| --- | --- | --- | --- | --- |
| NEW | public static final | org.apache.commons.crypto.utils.Padding | NoPadding | n.a. |
| NEW | public static final | org.apache.commons.crypto.utils.Padding | PKCS5Padding | n.a. |

Methods:

<table>
<thead>
<tr>
<td>Status</td><td>Modifier</td><td>Generic Templates</td><td>Type</td><td>Method</td><td>Exceptions</td><td>Compatibility Changes:</td><td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td><span></span><span>static </span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>org.apache.commons.crypto.utils.Padding</span></td><td>get(<span>java.lang.String</span>)</td><td>
<table>
<thead>
<tr>
<td>Status:</td><td>Name:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td>javax.crypto.NoSuchPaddingException</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>43</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td><td><span></span><span>static </span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>org.apache.commons.crypto.utils.Padding</span></td><td>valueOf(<span>java.lang.String</span>)</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>26</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td><td><span></span><span>static </span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>org.apache.commons.crypto.utils.Padding[]</span></td><td>values()</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>26</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

NEW public class org.apache.commons.crypto.utils.Transformation[top](#japicmp--toc)

Methods:

<table>
<thead>
<tr>
<td>Status</td><td>Modifier</td><td>Generic Templates</td><td>Type</td><td>Method</td><td>Exceptions</td><td>Compatibility Changes:</td><td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td><span></span><span></span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>java.lang.String</span></td><td>getAlgorithm()</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>95</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td><td><span></span><span></span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>java.lang.String</span></td><td>getMode()</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>104</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td><td><span></span><span></span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>org.apache.commons.crypto.utils.Padding</span></td><td>getPadding()</td><td>n.a.</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>113</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td><td><span></span><span>static </span><span>public </span><span></span><span></span><span></span></td><td>
			n.a.
		</td><td><span>org.apache.commons.crypto.utils.Transformation</span></td><td>parse(<span>java.lang.String</span>)</td><td>
<table>
<thead>
<tr>
<td>Status:</td><td>Name:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td><td>java.security.NoSuchAlgorithmException</td>
</tr>
<tr>
<td><span>NEW</span></td><td>javax.crypto.NoSuchPaddingException</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr>
<td>METHOD_ADDED_TO_PUBLIC_CLASS</td>
</tr>
</tbody>
</table>
</td><td>
<table>
<thead>
<tr>
<td>Old file</td><td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>n.a.</td><td>44</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/checkstyle.html -->

<!-- page_index: 16 -->

<a id="checkstyle--checkstyle-results"></a>

## Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 9.3 with /Users/garydgregory/git/commons-crypto/checkstyle.xml ruleset.

<a id="checkstyle--summary"></a>

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 54 | 0 | 0 | 0 |

<a id="checkstyle--files"></a>

## Files

| File | I | W | E |
| --- | --- | --- | --- |

<a id="checkstyle--details"></a>

## Details

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/spotbugs.html -->

<!-- page_index: 17 -->

<a id="spotbugs--spotbugs-bug-detector-report"></a>

## SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.7.3*

Threshold is *medium*

Effort is *default*

<a id="spotbugs--summary"></a>

## Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 53 | 0 | 0 | 0 |

<a id="spotbugs--files"></a>

## Files

| Class | Bugs |
| --- | --- |

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/cpd.html -->

<!-- page_index: 18 -->

<a id="cpd--cpd-results"></a>

## CPD Results

The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 6.52.0.

<a id="cpd--duplications"></a>

## Duplications

<table border="0" class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl10XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L343">343</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl20XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L334">334</a></td></tr>
<tr><td colspan="2">
<div>
<pre>}

    @Override
    public int _ENGINE_set_default(final PointerByReference rdrandEngine, final int flags) {
        return ENGINE_set_default(rdrandEngine, flags);
    }

    @Override
    public String _ERR_error_string(final NativeLong err, final char[] buff) {
        return ERR_error_string(err, buff);
    }

    @Override
    public NativeLong _ERR_peek_error() {
        return ERR_peek_error();
    }

    @Override
    public PointerByReference _EVP_aes_128_cbc() {
        return EVP_aes_128_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_128_ctr() {
        return EVP_aes_128_ctr();
    }

    @Override
    public PointerByReference _EVP_aes_192_cbc() {
        return EVP_aes_192_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_192_ctr() {
        return EVP_aes_192_ctr();
    }

    @Override
    public PointerByReference _EVP_aes_256_cbc() {
        return EVP_aes_256_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_256_ctr() {
        return EVP_aes_256_ctr();
    }

    @Override
    public void _EVP_CIPHER_CTX_cleanup(final PointerByReference context) {
        EVP_CIPHER_CTX_cleanup(context);
    }

    @Override
    public void _EVP_CIPHER_CTX_free(final PointerByReference context) {
        EVP_CIPHER_CTX_free(context);
    }

    @Override
    public PointerByReference _EVP_CIPHER_CTX_new() {
        return EVP_CIPHER_CTX_new();
    }

    @Override
    public int _EVP_CIPHER_CTX_set_padding(final PointerByReference context, final int padding) {
        return EVP_CIPHER_CTX_set_padding(context, padding);
    }

    @Override
    public int _EVP_CipherFinal_ex(final PointerByReference context, final ByteBuffer outBuffer, final int[] outlen) {
        return EVP_CipherFinal_ex(context, outBuffer, outlen);
    }

    @Override
    public int _EVP_CipherInit_ex(final PointerByReference context, final PointerByReference algo, final PointerByReference impl, final byte[] encoded,
            final byte[] iv, final int cipherMode) {
        return EVP_CipherInit_ex(context, algo, impl, encoded, iv, cipherMode);
    }

    @Override
    public int _EVP_CipherUpdate(final PointerByReference context, final ByteBuffer outBuffer, final int[] outlen, final ByteBuffer inBuffer,
            final int remaining) {
        return EVP_CipherUpdate(context, outBuffer, outlen, inBuffer, remaining);
    }

    @Override
    public Throwable _INIT_ERROR() {
        return INIT_ERROR;
    }

    @Override
    public boolean _INIT_OK() {
        return INIT_OK;
    }

    @Override
    public String _OpenSSL_version(final int i) {
        return SSLeay_version(i);
    }

    @Override
    public int _RAND_bytes(final ByteBuffer buf, final int length) {
        return RAND_bytes(buf, length) ;
    }

    @Override
    public PointerByReference _RAND_get_rand_method() {
        return RAND_get_rand_method();
    }

    @Override
    public PointerByReference _RAND_SSLeay() {
        return RAND_SSLeay();
    }
}</pre></div></td></tr></table>

<table border="0" class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl10XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L100">100</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl20XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L95">95</a></td></tr>
<tr><td colspan="2">
<div>
<pre>public static native void ENGINE_load_rdrand();

    /**
     * Sets the engine as the default for random number generation.
     *
     * @param e
     *            engine reference
     * @param flags
     *            ENGINE_METHOD_RAND
     * @return zero if failed.
     */
    public static native int ENGINE_set_default(PointerByReference e, int flags);

    /**
     * Generates a human-readable string representing the error code e.
     *
     * @see &lt;a href="https://www.openssl.org/docs/man1.0.2/man3/ERR_error_string.html"&gt;ERR_error_string&lt;/a&gt;
     *
     * @param err
     *            the error code
     * @param null_
     *            buf is NULL, the error string is placed in a static buffer
     * @return the human-readable error messages.
     */
    public static native String ERR_error_string(NativeLong err, char[] null_);

    // TODO: NOT USED?
    /**
     * Registers the error strings for all libcrypto functions.
     */
    public static native void ERR_load_crypto_strings();

    /**
     * @return the earliest error code from the thread's error queue without modifying it.
     */
    public static native NativeLong ERR_peek_error();

    /**
     * @return an OpenSSL AES EVP cipher instance with a 128-bit key CBC mode
     */
    public static native PointerByReference EVP_aes_128_cbc();

    /**
     * @return an OpenSSL AES EVP cipher instance with a 128-bit key CTR mode
     */
    public static native PointerByReference EVP_aes_128_ctr();

    /**
     * @return an OpenSSL AES EVP cipher instance with a 192-bit key CBC mode
     */
    public static native PointerByReference EVP_aes_192_cbc();

    /**
     * @return an OpenSSL AES EVP cipher instance with a 192-bit key CTR mode
     */
    public static native PointerByReference EVP_aes_192_ctr();

    /**
     * @return an OpenSSL AES EVP cipher instance with a 256-bit key CBC mode
     */
    public static native PointerByReference EVP_aes_256_cbc();

    /**
     * @return an OpenSSL AES EVP cipher instance with a 256-bit key CTR mode
     */
    public static native PointerByReference EVP_aes_256_ctr();

    /**
     * Clears all information from a cipher context and free up any allocated * memory associate
     * with it.
     *
     * @param c
     *            openssl evp cipher
     */
    public static native void EVP_CIPHER_CTX_cleanup(PointerByReference c);

    /**
     * Clears all information from a cipher context and free up any allocated memory associate with
     * it, including ctx itself.
     *
     * @param c
     *            openssl evp cipher
     */
    public static native void EVP_CIPHER_CTX_free(PointerByReference c);

    // TODO: NOT USED?
    /**
     * EVP_CIPHER_CTX_init() remains as an alias for EVP_CIPHER_CTX_reset
     *
     * @param p
     *            cipher context
     */
    public static native void EVP_CIPHER_CTX_init(PointerByReference p);

    /**
     * Creates a cipher context.
     *
     * @return a pointer to a newly created EVP_CIPHER_CTX for success and NULL for failure.
     */
    public static native PointerByReference EVP_CIPHER_CTX_new();

    /**
     * Enables or disables padding
     *
     * @param c
     *            cipher context
     * @param pad
     *            If the pad parameter is zero then no padding is performed
     * @return always returns 1
     */
    public static native int EVP_CIPHER_CTX_set_padding(PointerByReference c, int pad);

    /**
     * Finishes a multiple-part operation.
     *
     * @param ctx
     *            cipher context
     * @param bout
     *            output byte buffer
     * @param outl
     *            output length
     * @return 1 for success and 0 for failure.
     */
    public static native int EVP_CipherFinal_ex(PointerByReference ctx, ByteBuffer bout,
            int[] outl);

    // ENGINE API: https://www.openssl.org/docs/man1.0.2/man3/engine.html

    /**
     * Init a cipher.
     *
     * @param ctx
     *            cipher context
     * @param cipher
     *            evp cipher instance
     * @param impl
     *            engine
     * @param key
     *            key
     * @param iv
     *            iv
     * @param enc
     *            1 for encryption, 0 for decryption
     * @return 1 for success and 0 for failure.
     */
    public static native int EVP_CipherInit_ex(PointerByReference ctx, PointerByReference cipher,
            PointerByReference impl, byte[] key, byte[] iv, int enc);

    /**
     * Continues a multiple-part encryption/decryption operation.
     *
     * @param ctx
     *            cipher context
     * @param bout
     *            output byte buffer
     * @param outl
     *            output length
     * @param in
     *            input byte buffer
     * @param inl
     *            input length
     * @return 1 for success and 0 for failure.
     */
    public static native int EVP_CipherUpdate(PointerByReference ctx, ByteBuffer bout, int[] outl,
            ByteBuffer in, int inl);

    /**
     * Generates random data
     *
     * @param buf
     *            the bytes for generated random.
     * @param num
     *            buffer length
     * @return 1 on success, 0 otherwise.
     */
    public static native int RAND_bytes(ByteBuffer buf, int num);

    // Random generator
    /**
     * OpenSSL uses for random number generation
     *
     * @return pointers to the respective methods
     */
    public static native PointerByReference RAND_get_rand_method();

    /**
     * OpenSSL uses for random number generation.
     *
     * @return pointers to the respective methods
     */
    public static native PointerByReference RAND_SSLeay();

    /**
     * @see &lt;a href="https://www.openssl.org/docs/man1.0.2/man3/SSLeay.html"&gt;Version Number&lt;/a&gt;
     * TODO (does not appear to be used yet)
     * @return OPENSSL_VERSION_NUMBER which is a numeric release version identifier
     */
    public static native NativeLong SSLeay();

    /**
     * Retrieves version/build information about OpenSSL library.
     * This is returned by {@link OpenSslNativeJna#OpenSSLVersion(int)}
     *
     * @see &lt;a href="https://www.openssl.org/docs/man1.0.2/man3/SSLeay_version.html"&gt;Version Info&lt;/a&gt;
     *
     * @param type
     *            type can be SSLEAY_VERSION, SSLEAY_CFLAGS, SSLEAY_BUILT_ON...
     * @return A pointer to a constant string describing the version of the OpenSSL library or
     *         giving information about the library build.
     */
    public static native String SSLeay_version(int type);

    // ================== instance interface methods ==================

    @Override
    public PointerByReference _ENGINE_by_id(final String string) {
        return ENGINE_by_id(string);
    }

    @Override
    public int _ENGINE_cleanup() {
        return ENGINE_cleanup();
    }

    @Override
    public int _ENGINE_finish(final PointerByReference rdrandEngine) {
        return ENGINE_finish(rdrandEngine);
    }

    @Override
    public int _ENGINE_free(final PointerByReference rdrandEngine) {
        return ENGINE_free(rdrandEngine);
    }

    @Override
    public int _ENGINE_init(final PointerByReference rdrandEngine) {
        return ENGINE_init(rdrandEngine);
    }

    @Override
    public void _ENGINE_load_rdrand() {</pre></div></td></tr></table>

<table border="0" class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl10XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L393">393</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl11XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl11XNativeJna.html#L349">349</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl20XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L384">384</a></td></tr>
<tr><td colspan="2">
<div>
<pre>}

    @Override
    public void _EVP_CIPHER_CTX_free(final PointerByReference context) {
        EVP_CIPHER_CTX_free(context);
    }

    @Override
    public PointerByReference _EVP_CIPHER_CTX_new() {
        return EVP_CIPHER_CTX_new();
    }

    @Override
    public int _EVP_CIPHER_CTX_set_padding(final PointerByReference context, final int padding) {
        return EVP_CIPHER_CTX_set_padding(context, padding);
    }

    @Override
    public int _EVP_CipherFinal_ex(final PointerByReference context, final ByteBuffer outBuffer, final int[] outlen) {
        return EVP_CipherFinal_ex(context, outBuffer, outlen);
    }

    @Override
    public int _EVP_CipherInit_ex(final PointerByReference context, final PointerByReference algo, final PointerByReference impl, final byte[] encoded,
            final byte[] iv, final int cipherMode) {
        return EVP_CipherInit_ex(context, algo, impl, encoded, iv, cipherMode);
    }

    @Override
    public int _EVP_CipherUpdate(final PointerByReference context, final ByteBuffer outBuffer, final int[] outlen, final ByteBuffer inBuffer,
            final int remaining) {
        return EVP_CipherUpdate(context, outBuffer, outlen, inBuffer, remaining);
    }

    @Override
    public Throwable _INIT_ERROR() {
        return INIT_ERROR;
    }

    @Override
    public boolean _INIT_OK() {
        return INIT_OK;
    }

    @Override
    public String _OpenSSL_version(final int i) {
        return SSLeay_version(i);</pre></div></td></tr></table>

<table border="0" class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl11XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl11XNativeJna.html#L279">279</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl20XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L314">314</a></td></tr>
<tr><td colspan="2">
<div>
<pre>}

    @Override
    public int _ENGINE_finish(final PointerByReference rdrandEngine) {
        return ENGINE_finish(rdrandEngine);
    }

    @Override
    public int _ENGINE_free(final PointerByReference rdrandEngine) {
        return ENGINE_free(rdrandEngine);
    }

    @Override
    public int _ENGINE_init(final PointerByReference rdrandEngine) {
        return ENGINE_init(rdrandEngine);
    }

    @Override
    public void _ENGINE_load_rdrand() {
        // Not available
    }

    @Override
    public int _ENGINE_set_default(final PointerByReference rdrandEngine, final int flags) {
        return ENGINE_set_default(rdrandEngine, flags);
    }

    @Override
    public String _ERR_error_string(final NativeLong err, final char[] buff) {
        return ERR_error_string(err, buff);
    }

    @Override
    public NativeLong _ERR_peek_error() {
        return ERR_peek_error();
    }

    @Override
    public PointerByReference _EVP_aes_128_cbc() {
        return EVP_aes_128_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_128_ctr() {
        return EVP_aes_128_ctr();
    }

    @Override
    public PointerByReference _EVP_aes_192_cbc() {
        return EVP_aes_192_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_192_ctr() {
        return EVP_aes_192_ctr();
    }

    @Override
    public PointerByReference _EVP_aes_256_cbc() {
        return EVP_aes_256_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_256_ctr() {
        return EVP_aes_256_ctr();
    }

    @Override
    public void _EVP_CIPHER_CTX_cleanup(final PointerByReference context) {</pre></div></td></tr></table>

<table border="0" class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl10XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L343">343</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl11XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl11XNativeJna.html#L299">299</a></td></tr>
<tr><td colspan="2">
<div>
<pre>}

    @Override
    public int _ENGINE_set_default(final PointerByReference rdrandEngine, final int flags) {
        return ENGINE_set_default(rdrandEngine, flags);
    }

    @Override
    public String _ERR_error_string(final NativeLong err, final char[] buff) {
        return ERR_error_string(err, buff);
    }

    @Override
    public NativeLong _ERR_peek_error() {
        return ERR_peek_error();
    }

    @Override
    public PointerByReference _EVP_aes_128_cbc() {
        return EVP_aes_128_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_128_ctr() {
        return EVP_aes_128_ctr();
    }

    @Override
    public PointerByReference _EVP_aes_192_cbc() {
        return EVP_aes_192_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_192_ctr() {
        return EVP_aes_192_ctr();
    }

    @Override
    public PointerByReference _EVP_aes_256_cbc() {
        return EVP_aes_256_cbc();
    }

    @Override
    public PointerByReference _EVP_aes_256_ctr() {
        return EVP_aes_256_ctr();
    }

    @Override
    public void _EVP_CIPHER_CTX_cleanup(final PointerByReference context) {</pre></div></td></tr></table>

<table border="0" class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl10XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L29">29</a></td></tr>
<tr>
<td>org/apache/commons/crypto/jna/OpenSsl20XNativeJna.java</td>
<td><a href="https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L29">29</a></td></tr>
<tr><td colspan="2">
<div>
<pre>final class OpenSsl10XNativeJna implements OpenSslInterfaceNativeJna {

    static final boolean INIT_OK;

    static final Throwable INIT_ERROR;

    static {
        boolean ok = false;
        Throwable thrown = null;
        try {
            final String libName = System.getProperty(Crypto.CONF_PREFIX + OpenSslNativeJna.class.getSimpleName(), "crypto");
            OpenSslJna.debug("Native.register('%s')", libName);
            Native.register(libName);
            ok = true;
        } catch (final Exception | UnsatisfiedLinkError e) {
            thrown = e;
        } finally {
            INIT_OK = ok;
            INIT_ERROR = thrown;
        }
    }

    // Try to keep methods aligned across versions

    /**
     * Gets engine by id
     *
     * @param id
     *            engine id
     * @return engine instance
     */
    public static native PointerByReference ENGINE_by_id(String id);

    /**
     * Cleanups before program exit, it will avoid memory leaks.
     *
     * @return 0 on success, 1 otherwise.
     */
    public static native int ENGINE_cleanup();

    /**
     * Releases all functional references.
     *
     * @param e
     *            engine reference.
     * @return 0 on success, 1 otherwise.
     */
    public static native int ENGINE_finish(PointerByReference e);

    /**
     * Frees the structural reference
     *
     * @param e
     *            engine reference.
     * @return 0 on success, 1 otherwise.
     */
    public static native int ENGINE_free(PointerByReference e);

    /**
     * Obtains a functional reference from an existing structural reference.
     *
     * @param e
     *            engine reference
     * @return zero if the ENGINE was not already operational and couldn't be successfully
     *         initialized
     */
    public static native int ENGINE_init(PointerByReference e);

    /**
     * Initializes the engine.
     */
    public static native void ENGINE_load_rdrand();</pre></div></td></tr></table>

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/pmd.html -->

<!-- page_index: 19 -->

<a id="pmd--pmd-results"></a>

## PMD Results

The following document contains the results of [PMD](https://pmd.github.io) 6.52.0.

PMD found no problems in your source code.

<a id="pmd--suppressed-violations"></a>

## Suppressed Violations

| Filename | Rule message | Suppression type | Reason |
| --- | --- | --- | --- |
| org/apache/commons/crypto/cipher/OpenSslCipher.java | Avoid unused constructor parameters such as 'props'. | nopmd |  |
| org/apache/commons/crypto/jna/OpenSslJnaCipher.java | Avoid unused constructor parameters such as 'props'. | nopmd |  |
| org/apache/commons/crypto/jna/OpenSslJnaCryptoRandom.java | Avoid unused constructor parameters such as 'props'. | nopmd |  |
| org/apache/commons/crypto/random/OpenSslCryptoRandom.java | Avoid unused constructor parameters such as 'props'. | nopmd |  |
| org/apache/commons/crypto/stream/CryptoInputStream.java | Avoid empty while statements | nopmd |  |

---

<a id="taglist"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/taglist.html -->

<!-- page_index: 20 -->

<a id="taglist--tag-list-report"></a>

## Tag List Report

The following document contains the listing of user tags found in the code. Below is the summary of the occurrences per tag.

| Tag Class | Total number of occurrences | Tag strings used by tag class |
| --- | --- | --- |
| [Needs Work](#taglist--tag_class_1) | 18 | TODO, FIXME, XXX |
| [Noteable Markers](#taglist--tag_class_2) | 10 | NOTE, NOPMD, NOSONAR |

Each tag is detailed below:

<a id="taglist--needs-work"></a>

### Needs Work

**Number of occurrences found in the code: 18**

| org.apache.commons.crypto.NativeCodeLoader | Line |
| --- | --- |
| Find a better way to do this later. | [124](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/NativeCodeLoader.html#L124) |
| org.apache.commons.crypto.cipher.CryptoCipherFactory | Line |
| does it make sense to treat the empty string as the default? | [144](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/cipher/CryptoCipherFactory.html#L144) |
| org.apache.commons.crypto.cipher.CryptoCipherFactoryTest | Line |
| should this really mean use the default? | [47](https://commons.apache.org/proper/commons-crypto/xref-test/org/apache/commons/crypto/cipher/CryptoCipherFactoryTest.html#L47) |
| org.apache.commons.crypto.jna.OpenSsl10XNativeJna | Line |
| NOT USED? | [126](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L126) |
| NOT USED? | [185](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L185) |
| (does not appear to be used yet) | [294](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl10XNativeJna.html#L294) |
| org.apache.commons.crypto.jna.OpenSsl20XNativeJna | Line |
| NOT USED? | [121](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L121) |
| NOT USED? | [180](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L180) |
| (does not appear to be used yet) | [288](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSsl20XNativeJna.html#L288) |
| org.apache.commons.crypto.jna.OpenSslInterfaceNativeJna | Line |
| Appears to be deprecated as of OpenSSL 1.1.0. | [34](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslInterfaceNativeJna.html#L34) |
| org.apache.commons.crypto.jna.OpenSslJna | Line |
| Find a better way to do this later. | [40](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJna.html#L40) |
| Find a better way to do this later. | [67](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJna.html#L67) |
| org.apache.commons.crypto.jna.OpenSslJnaCipher | Line |
| is that sufficient? OpenSslNativeJna.EVP\_CIPHER\_CTX\_free(context); | [112](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJnaCipher.html#L112) |
| implement GCM mode using Jna | [343](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJnaCipher.html#L343) |
| implement GCM mode using Jna | [373](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJnaCipher.html#L373) |
| org.apache.commons.crypto.jna.OpenSslNativeJna | Line |
| Throw error? | [86](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslNativeJna.html#L86) |
| org.apache.commons.crypto.random.CryptoRandomFactory | Line |
| does it make sense to treat the empty string as the default? | [219](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/random/CryptoRandomFactory.html#L219) |
| org.apache.commons.crypto.utils.EnumTest | Line |
| check if any implementations of CryptoRandom or CryptoCipher are missing from the values | [64](https://commons.apache.org/proper/commons-crypto/xref-test/org/apache/commons/crypto/utils/EnumTest.html#L64) |

<a id="taglist--noteable-markers"></a>

### Noteable Markers

**Number of occurrences found in the code: 10**

| org.apache.commons.crypto.Crypto | Line |
| --- | --- |
| --No comment-- | [52](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/Crypto.html#L52) |
| org.apache.commons.crypto.OsInfo | Line |
| --No comment-- | [125](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/OsInfo.html#L125) |
| org.apache.commons.crypto.cipher.OpenSslCipher | Line |
| --No comment-- | [55](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/cipher/OpenSslCipher.html#L55) |
| org.apache.commons.crypto.jna.OpenSslJnaCipher | Line |
| --No comment-- | [85](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJnaCipher.html#L85) |
| org.apache.commons.crypto.jna.OpenSslJnaCryptoRandom | Line |
| --No comment-- | [60](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/jna/OpenSslJnaCryptoRandom.html#L60) |
| org.apache.commons.crypto.random.OpenSslCryptoRandom | Line |
| --No comment-- | [98](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/random/OpenSslCryptoRandom.html#L98) |
| org.apache.commons.crypto.stream.CryptoInputStream | Line |
| --No comment-- | [126](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/stream/CryptoInputStream.html#L126) |
| --No comment-- | [516](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/stream/CryptoInputStream.html#L516) |
| org.apache.commons.crypto.stream.CtrCryptoInputStream | Line |
| --No comment-- | [86](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/stream/CtrCryptoInputStream.html#L86) |
| org.apache.commons.crypto.utils.IoUtils | Line |
| --No comment-- | [55](https://commons.apache.org/proper/commons-crypto/xref/org/apache/commons/crypto/utils/IoUtils.html#L55) |

---
