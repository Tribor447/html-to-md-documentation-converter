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
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

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
[project reports](https://commons.apache.org/proper/commons-crypto/project-reports.html)
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

[Change reports](https://commons.apache.org/proper/commons-crypto/changes-report.html) are also available.

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

| [random](https://commons.apache.org/proper/commons-crypto/apidocs/index.html) | The interface for CryptoRandom. |
| --- | --- |
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
| [Summary](#summary) | This document lists other related information of this project |
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

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/summary.html -->

<!-- page_index: 8 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Crypto |
| Description | Apache Commons Crypto is a cryptographic library optimized with AES-NI (Advanced Encryption Standard New Instructions). It provides Java API for both cipher level and Java stream level. Developers can use it to implement high performance AES encryption/decryption with the minimum code and effort. Please note that Crypto doesn't implement the cryptographic algorithm such as AES directly. It wraps to OpenSSL or JCE which implement the algorithms. Features -------- 1. Cipher API for low level cryptographic operations. 2. Java stream API (CryptoInputStream/CryptoOutputStream) for high level stream encryption/decryption. 3. Both optimized with high performance AES encryption/decryption. (1400 MB/s - 1700 MB/s throughput in modern Xeon processors). 4. JNI-based implementation to achieve comparable performance to the native C/C++ version based on OpenSsl. 5. Portable across various operating systems (currently only Linux/MacOSX/Windows); Apache Commons Crypto loads the library according to your machine environment (it checks system properties, `os.name` and `os.arch`). 6. Simple usage. Add the commons-crypto-(version).jar file to your classpath. Export restrictions ------------------- This distribution includes cryptographic software. The country in which you currently reside may have restrictions on the import, possession, use, and/or re-export to another country, of encryption software. BEFORE using any encryption software, please check your country's laws, regulations and policies concerning the import, possession, or use, and re-export of encryption software, to see if this is permitted. See <http://www.wassenaar.org/> for more information. The U.S. Government Department of Commerce, Bureau of Industry and Security (BIS), has classified this software as Export Commodity Control Number (ECCN) 5D002.C.1, which includes information security software using or performing cryptographic functions with asymmetric algorithms. The form and manner of this Apache Software Foundation distribution makes it eligible for export under the License Exception ENC Technology Software Unrestricted (TSU) exception (see the BIS Export Administration Regulations, Section 740.13) for both object code and source code. The following provides more details on the included cryptographic software: \* Commons Crypto use [Java Cryptography Extension](http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html) provided by Java \* Commons Crypto link to and use [OpenSSL](https://www.openssl.org/) ciphers |
| Homepage | [https://commons.apache.org/proper/commons-crypto/](#index) |

<a id="summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-crypto |
| Version | 1.2.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/team.html -->

<!-- page_index: 9 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/f6d817a812d2d080c0f4ff9e0a73a7bd?d=mm&s=60) | atm | Aaron T Myers | [atm@apache.org](mailto:atm@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/d45756616ba46a12f4d16ca252d4941d?d=mm&s=60) | wang | Andrew Wang | [wang@apache.org](mailto:wang@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/e7c65ef2202a0c1f43255aff617cb4ec?d=mm&s=60) | cnauroth | Chris Nauroth | [cnauroth@apache.org](mailto:cnauroth@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/ad06a3c29ef7c463664af7b6ec298f4f?d=mm&s=60) | cmccabe | Colin P. McCabe | [cmccabe@apache.org](mailto:cmccabe@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/1f6b8ca791a94da93e963b1d77669000?d=mm&s=60) | sdp | Dapeng Sun | [sdp@apache.org](mailto:sdp@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/781e10f69b102b1340627ab1d7040bbc?d=mm&s=60) | dianfu | Dian Fu | [dianfu@apache.org](mailto:dianfu@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/fcbb395c7c47a4d51fb260869fda9d75?d=mm&s=60) | dongc | Dong Chen | [dongc@apache.org](mailto:dongc@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/f39a4c19c83fb3ee83a019904abd4e18?d=mm&s=60) | xuf | Ferdinand Xu | [xuf@apache.org](mailto:xuf@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/d957fdc3c9e83e1e0f23cf89a5b59547?d=mm&s=60) | haifengchen | Haifeng Chen | [haifengchen@apache.org](mailto:haifengchen@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/43c64a79c74756d632ce8a8a409795ca?d=mm&s=60) | vanzin | Marcelo Vanzin | [vanzin@apache.org](mailto:vanzin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/d59300095a035422227ef15a208e8485?d=mm&s=60) | umamahesh | Uma Maheswara Rao G | [umamahesh@apache.org](mailto:umamahesh@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/d7ef146420d1c0daa071e3ebd0fb2147?d=mm&s=60) | yliu | Yi Liu | [yliu@apache.org](mailto:yliu@apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization |
| --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/525b13534a36b69744dbd0813a649d27?d=mm&s=60) | Colin Ma | [junjie.ma@intel.com](mailto:junjie.ma@intel.com) | - |
| ![](https://www.gravatar.com/avatar/346d2b4823caad10b1f6673bd377da2b?d=mm&s=60) | Xianda Ke | [xianda.ke@intel.com](mailto:xianda.ke@intel.com) | - |
| ![](https://www.gravatar.com/avatar/cb75a25214ddf798c617bc6c1498ba00?d=mm&s=60) | Ke Jia | [ke.a.jia@intel.com](mailto:ke.a.jia@intel.com) | - |
| ![](https://www.gravatar.com/avatar/7e01fa73258b35326b5943ced6cd939a?d=mm&s=60) | George Kankava | [george.kankava@devfactory.com](mailto:george.kankava@devfactory.com) | - |
| ![](https://www.gravatar.com/avatar/d176a1c30d722b24c1df2d771ed43914?d=mm&s=60) | Tian Jianguo | [jianguo.tian@intel.com](mailto:jianguo.tian@intel.com) | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Adam Retter | - | Evolved Binary |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Arturo Bernal | - | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-crypto/ci-management.html -->

<!-- page_index: 10 -->

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
