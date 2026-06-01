# Documentation

## Navigation

- Overview
  - [Home](#index)
  - [Features](#features)
  - [FtpServer 1.1.4](#download_1_1)
  - [FtpServer 1.2.1](#download_1_2)
  - [Old Downloads](#old-downloads)
  - [Documentation](#documentation)
  - [Sources](#getting_source)
  - [FAQ](#faq)
  - [Related Project](#related_project)
- Community
  - [Mailing Lists](#mailing_list)
  - [Getting Involved](#getting_involved)
  - [Reporting a Bug](#reporting_bug)
  - [Contributors](#contributors)

## Content

<a id="index"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/index.html -->

<!-- page_index: 1 -->

<a id="index--welcome-to-apache-ftpserver"></a>

# Welcome to Apache FtpServer

<a id="index--overview"></a>

## Overview

The **Apache FtpServer** is a 100% pure **Java FTP** server. It’s designed to be a complete and portable **FTP** server engine solution based on currently available open protocols. **FtpServer** can be run standalone as a *Windows* service or *Unix/Linux* daemon, or embedded into a **Java** application. We also provide support for integration within [Spring](http://www.springsource.org/) applications and provide our releases as **OSGi** bundles.

The default network support is based on [Apache MINA](https://mina.apache.org/), a high performance asynchronous **IO** library. Using **MINA**, **FtpServer** can scale to a large number of concurrent users.

It is also an **FTP** application platform. We have developed a **Java API** to let you write **Java** code to process **FTP** event notifications that we call the **Ftplet API**. **Apache FtpServer** provides an implementation of an **FTP** server to support this **API**.

To get started, have a look at one of our tutorials:

- [Embedding FtpServer in 5 minutes](https://mina.apache.org/ftpserver-project/embedding_ftpserver.html)
- [Running FtpServer stand-alone in 5 minutes](https://mina.apache.org/ftpserver-project/running_ftpserver_standalone.html)

You can also have a look at the documentation for how to configure **FtpServer** to suite your needs.

<a id="index--history"></a>

## History

The inital code comes from the defunct **[Apache Avalon](https://avalon.apache.org/closed.html)** project. It was brought to incubator by *Paul Hammant*, the initial contributor, and graduated as a **MINA** subproject in December 2007.

---

<a id="features"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/features.html -->

<!-- page_index: 2 -->

<a id="features--features"></a>

# Features

- 100% pure Java, free, open source resumable FTP server
- Multi platform support and multithreaded design.
- User virtual directory, write permission, idle time-out and upload/download bandwidth limitation support.
- Anonymous login support.
- Both upload and download files are resumable.
- Handles both ASCII and binary data transfers.
- IP restriction support to ban IPs.
- Database and file can be used to store user data.
- All the FTP messages are customizable.
- Implicit/explicit SSL/TLS support.
- MDTM support - your users can change the date-time stamp of files.
- “MODE Z” support for faster data upload/download.
- Custom user manager, IP restrictor, logger can be added easily.
- User event notifications can be added (Ftplet).

---

<a id="download_1_1"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/download_1_1.html -->

<!-- page_index: 3 -->

<a id="download_1_1--apache-ftpserver-114-release"></a>
<a id="download_1_1--apache-ftpserver-1.1.4-release"></a>

# Apache FtpServer 1.1.4 Release

<a id="download_1_1--new-features-in-114"></a>
<a id="download_1_1--new-features-in-1.1.4"></a>

## New Features in 1.1.4

This release is rolling back an addedd feature (support for multiple TLS protocols), to be back compatible with 1.1.2. Would you want to benefit from this feature, you shiould switch to the 1.2.0 release.

<a id="download_1_1--getting-the-binary-distributions"></a>

## Getting the Binary Distributions

| Description | Download Link | SHA256 hashes | SHA512 hashes | PGP Signature file of download |
| --- | --- | --- | --- | --- |
| zip distribution | [apache-ftpserver-1.1.4-bin.zip](https://dlcdn.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.zip) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.zip.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.zip.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.zip.asc) |
| tar.gz distribution | [apache-ftpserver-1.1.4-bin.tar.gz](https://dlcdn.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.gz) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.gz.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.gz.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.gz.asc) |
| tar.bz2 distribution | [apache-ftpserver-1.1.4-bin.tar.bz2](https://dlcdn.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.bz2) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.bz2.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.bz2.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-bin.tar.bz2.asc) |

<a id="download_1_1--verify-the-integrity-of-downloads"></a>

## Verify the Integrity of Downloads

It is essential that you verify the integrity of the downloaded files using the PGP signatures. The PGP signatures can be verified using PGP or GPG. Begin by following these steps:

1. Download the [KEYS](https://downloads.apache.org/mina/KEYS)
2. Download the asc signature file for the relevant distribution
3. Verify the signatures using the following commands, depending on your use of PGP or GPG:


```
 $ pgpk -a KEYS
 $ pgpv apache-ftpserver-1.1.4-bin.tar.gz.asc
```

   or


```
 $ pgp -ka KEYS
 $ pgp apache-ftpserver-1.1.4-bin.tar.gz.asc apache-ftpserver-1.1.4-bin.tar.gz
```

   or


```
 $ gpg --import KEYS
 $ gpg --verify apache-ftpserver-1.1.4-bin.tar.gz.asc apache-ftpserver-1.1.4-bin.tar.gz
```

<a id="download_1_1--getting-the-binaries-using-maven-2"></a>

## Getting the Binaries using Maven 2

To use this release in your maven project, the proper dependency configuration that you should use in your [Maven POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) is:

```xml
<dependency>
    <groupId>org.apache.ftpserver</groupId>
    <artifactId>ftpserver-core</artifactId>
    <version>1.1.4</version>
</dependency>
```

<a id="download_1_1--getting-the-source-code"></a>

## Getting the Source Code

<a id="download_1_1--source-distributions"></a>

### Source Distributions

| Description | Download Link | SHA256 hashes | SHA512 hashes | PGP Signature file of download |
| --- | --- | --- | --- | --- |
| zip sources | [apache-ftpserver-1.1.4-src.zip](https://dlcdn.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.zip) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.zip.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.zip.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.zip.asc) |
| tar.gz sources | [apache-ftpserver-1.1.4-src.tar.gz](https://dlcdn.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.gz) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.gz.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.gz.asc) |
| tar.bz2 sources | [apache-ftpserver-1.1.4-src.tar.bz2](https://dlcdn.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.bz2) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.bz2.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.bz2.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.1.4/apache-ftpserver-1.1.4-src.tar.bz2.asc) |

<a id="download_1_1--git-tag-checkout"></a>

### Git Tag Checkout

```
$ git clone https://gitbox.apache.org/repos/asf/mina-ftpserver.git
$ git checkout ftpserver-parent-1.1.4
```

You are now on 1.1.4 branch.

---

<a id="download_1_2"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/download_1_2.html -->

<!-- page_index: 4 -->

<a id="download_1_2--apache-ftpserver-121-release"></a>
<a id="download_1_2--apache-ftpserver-1.2.1-release"></a>

# Apache FtpServer 1.2.1 Release

<a id="download_1_2--new-features-in-121"></a>
<a id="download_1_2--new-features-in-1.2.1"></a>

## New Features in 1.2.1

This release includes many fixes, and now depends on MINA core 2.2.4.

Here is the list of fixes and modifications:

o [FTPSERVER-515](https://issues.apache.org/jira/projects/FTPSERVER-515): Bump Apache Log4j from 2.17.2 to 2.19.0
o [FTPSERVER-510](https://issues.apache.org/jira/projects/FTPSERVER-510):Update Apache parent POM from 25 to 26
o [FTPSERVER-509](https://issues.apache.org/jira/projects/FTPSERVER/issues/FTPSERVER-509): Enable GitHub Action build
o [FTPSERVER-506](https://issues.apache.org/jira/projects/FTPSERVER-506): Fix binary compatibility issues.
o [FTPSERVER-499](https://issues.apache.org/jira/projects/FTPSERVER/issues/FTPSERVER-499): FtpResponseEncoder is not thread safe
o [FTPSERVER-446](https://issues.apache.org/jira/projects/FTPSERVER-446): Implementing User Manager not possible in OSGi environment

Otherwise, the following features have been added:
o Support for SHA256 and SHA512 encryption
o Use ThreadLocal for FtpResponseEncoder.ENCODER and SimpleDateFormat
o Make build reproductible

<a id="download_1_2--getting-the-binary-distributions"></a>

## Getting the Binary Distributions

| Description | Download Link | SHA256 hashes | SHA512 hashes | PGP Signature file of download |
| --- | --- | --- | --- | --- |
| zip distribution | [apache-ftpserver-1.2.1-bin.zip](https://dlcdn.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.zip) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.zip.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.zip.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.zip.asc) |
| tar.gz distribution | [apache-ftpserver-1.2.1-bin.tar.gz](https://dlcdn.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.gz) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.gz.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.gz.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.gz.asc) |
| tar.bz2 distribution | [apache-ftpserver-1.2.1-bin.tar.bz2](https://dlcdn.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.bz2) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.bz2.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.bz2.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-bin.tar.bz2.asc) |

<a id="download_1_2--verify-the-integrity-of-downloads"></a>

## Verify the Integrity of Downloads

It is essential that you verify the integrity of the downloaded files using the PGP signatures. The PGP signatures can be verified using PGP or GPG. Begin by following these steps:

1. Download the [KEYS](https://downloads.apache.org/mina/KEYS)
2. Download the asc signature file for the relevant distribution
3. Verify the signatures using the following commands, depending on your use of PGP or GPG:


```
 $ pgpk -a KEYS
 $ pgpv apache-ftpserver-1.2.1-bin.tar.gz.asc
```

   or


```
 $ pgp -ka KEYS
 $ pgp apache-ftpserver-1.2.1-bin.tar.gz.asc apache-ftpserver-1.2.1-bin.tar.gz
```

   or


```
 $ gpg --import KEYS
 $ gpg --verify apache-ftpserver-1.2.1-bin.tar.gz.asc apache-ftpserver-1.2.1-bin.tar.gz
```

<a id="download_1_2--getting-the-binaries-using-maven-2"></a>

## Getting the Binaries using Maven 2

To use this release in your maven project, the proper dependency configuration that you should use in your [Maven POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) is:

```xml
<dependency>
    <groupId>org.apache.ftpserver</groupId>
    <artifactId>ftpserver-core</artifactId>
    <version>1.2.1</version>
</dependency>
```

<a id="download_1_2--getting-the-source-code"></a>

## Getting the Source Code

<a id="download_1_2--source-distributions"></a>

### Source Distributions

| Description | Download Link | SHA256 hashes | SHA512 hashes | PGP Signature file of download |
| --- | --- | --- | --- | --- |
| zip sources | [apache-ftpserver-1.2.1-src.zip](https://dlcdn.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.zip) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.zip.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.zip.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.zip.asc) |
| tar.gz sources | [apache-ftpserver-1.2.1-src.tar.gz](https://dlcdn.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.gz) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.gz.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.gz.asc) |
| tar.bz2 sources | [apache-ftpserver-1.2.1-src.tar.bz2](https://dlcdn.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.bz2) | [SHA256](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.bz2.sha256) | [SHA512](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.bz2.sha512) | [ASC](https://downloads.apache.org/mina/ftpserver/1.2.1/apache-ftpserver-1.2.1-src.tar.bz2.asc) |

<a id="download_1_2--git-tag-checkout"></a>

### Git Tag Checkout

```
$ git clone https://gitbox.apache.org/repos/asf/mina-ftpserver.git
$ git checkout ftpserver-parent-1.2.1
```

You are now on 1.2.1 branch.

---

<a id="old-downloads"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/old-downloads.html -->

<!-- page_index: 5 -->

<a id="old-downloads--older-ftpserver-releases"></a>

# Older FtpServer Releases

<a id="old-downloads--ftpserver-12x"></a>
<a id="old-downloads--ftpserver-1.2.x"></a>

## FtpServer 1.2.x

| Version | Download Links | Date |
| --- | --- | --- |
| Apache FtpServer 1.2.0 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.2.0/) | 13/Mar/2022 |

<a id="old-downloads--ftpserver-11x"></a>
<a id="old-downloads--ftpserver-1.1.x"></a>

## FtpServer 1.1.x

| Version | Download Links | Date |
| --- | --- | --- |
| Apache FtpServer 1.1.3 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.1.3/) | 25/Feb/2022 |
| Apache FtpServer 1.1.2 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.1.2/) | 03/Jan/2022 |
| Apache FtpServer 1.1.1 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.1.1/) | 03/Jul/2020 |
| Apache FtpServer 1.1.0 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.1.0/) | 02/Jun/2019 |

<a id="old-downloads--ftpserver-10x"></a>
<a id="old-downloads--ftpserver-1.0.x"></a>

## FtpServer 1.0.x

Note that this version is not anymore maintained.

| Version | Download Links | Date |
| --- | --- | --- |
| Apache FtpServer 1.0.6 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.6/) | 04/May/2018 |
| Apache FtpServer 1.0.5 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.5/) | 02/Oct/2010 |
| Apache FtpServer 1.0.4 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.4/) | 13/Mar/2009 |
| Apache FtpServer 1.0.3 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.3/) | 17/Jun/2009 |
| Apache FtpServer 1.0.2 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.2/) | 17/Jun/2009 |
| Apache FtpServer 1.0.1 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.1/) | 18/May/2009 |
| Apache FtpServer 1.0.0 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.0/) | 28/Feb/2009 |
| Apache FtpServer 1.0.0-RC2 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.0-RC2/) | 31/Jan/2009 |
| Apache FtpServer 1.0.0-RC1 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.0-RC1/) | 13/Jan/2009 |
| Apache FtpServer 1.0.0-M4 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.0-M4/) | 10/Dec/2008 |
| Apache FtpServer 1.0.0-M3 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.0-M3/) | 08/Sep/2008 |
| Apache FtpServer 1.0.0-M2 | [Download](https://archive.apache.org/dist/mina/ftpserver/1.0.0-M2/) | 11/Aug/2008 |

<a id="old-downloads--verify-the-integrity-of-the-files"></a>

# Verify the integrity of the files

The PGP signatures can be verified using PGP or GPG. First download the [KEYS](https://downloads.apache.org/mina/KEYS) as well as the asc signature file for the relevant distribution. Then verify the signatures using:

```
$ pgpk -a KEYS
$ pgpv apache-ftpserver-1.1.3.tar.gz.asc
```

or

```
$ pgp -ka KEYS
$ pgp apache-ftpserver-1.1.3.tar.gz.asc
```

or

```
$ gpg --import KEYS
$ gpg --verify apache-apache-ftpserver-1.1.3.tar.gz.asc
```

<a id="old-downloads--previous-releases"></a>

# Previous Releases

The previous releases can be found [here](https://archive.apache.org/dist/mina/ftpserver).

<a id="old-downloads--version-numbering-scheme"></a>

# Version Numbering Scheme

The version number of FtpServer has the following form:

<major>.<minor>.<micro> \[-M<milestone number> or -RC<release candidate number>]

This scheme has three number components:

- The **major** number increases when there are incompatible changes in the API.
- The **minor** number increases when a new feature is introduced.
- The **micro** number increases when a bug or a trivial change is made.

and an optional label that indicates the maturity of a release:

- **M** (Milestone) means the feature set can change at any time in the next milestone releases. The last milestone release becomes the first release candidate after a vote.
- **RC** (Release Candidate) means the feature set is frozen and the next RC releases will focus on fixing problems unless there is a serious flaw in design. The last release candidate becomes the first GA release after a vote.
- No label implies **GA** (General Availability), which means the release is stable enough and therefore ready for production environment.

Here’s an example that illustrates how FtpServer version number increases:

1.0.0-M1 -> 1.0.0-M2 -> 1.0.0-M3 -> 1.0.0-M4 -> 1.0.0-RC1 -> 1.0.0-RC2 -> 1.0.0-RC3 -> **1.0.0** -> 1.0.1 -> 1.0.2 -> 1.1.0-M1 ...

Please note that we always specify the micro number, even if it’s zero.

---

<a id="documentation"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/documentation.html -->

<!-- page_index: 6 -->

<a id="documentation--documentation"></a>

# Documentation

<a id="documentation--tutorials"></a>

## Tutorials

- [Embedding FtpServer in 5 minutes](https://mina.apache.org/ftpserver-project/embedding_ftpserver.html)
- [Running FtpServer stand-alone in 5 minutes](https://mina.apache.org/ftpserver-project/running_ftpserver_standalone.html)

<a id="documentation--using-ftpserver"></a>

## Using FtpServer

- [Installation](https://mina.apache.org/ftpserver-project/installation.html)
  - [Installing FtpServer as a Windows service](https://mina.apache.org/ftpserver-project/ftpserver_as_windows_service.html)
- [Configuration](https://mina.apache.org/ftpserver-project/configuration.html)
  - [Server](https://mina.apache.org/ftpserver-project/configuration_server.html)
  - [Listeners](https://mina.apache.org/ftpserver-project/configuration_listeners.html)
  - [Configure passive ports](https://mina.apache.org/ftpserver-project/configuration_passive_ports.html)
  - [TLS/SSL Support](https://mina.apache.org/ftpserver-project/configuration_ssltls_support.html)
  - [User Manager](https://mina.apache.org/ftpserver-project/configuration_user_manager.html)
  - [Logging](https://mina.apache.org/ftpserver-project/configuration_logging.html)
- [Messages](https://mina.apache.org/ftpserver-project/messages.html)
- [Managing users](https://mina.apache.org/ftpserver-project/managing_users.html)
- [FtpServer and port 21 on Linux](https://mina.apache.org/ftpserver-project/ftpserver_port_21.html)

<a id="documentation--advanced"></a>

## Advanced

- [FTP Commands](https://mina.apache.org/ftpserver-project/ftpserver_commands.html)
- [SITE Commands](https://mina.apache.org/ftpserver-project/ftpserver_site_commands.html)
- [Ftplet](https://mina.apache.org/ftpserver-project/ftplet.html)

<a id="documentation--supported-rfcs"></a>

## Supported RFCs

- [RFC959](http://www.ietf.org/rfc/rfc959.txt)
- [RFC2228](http://www.ietf.org/rfc/rfc2228.txt)
- [RFC2389](http://www.ietf.org/rfc/rfc2389.txt)
- [RFC2428](http://www.ietf.org/rfc/rfc2428.txt)
- [RFC2640](http://www.ietf.org/rfc/rfc2640.txt)
- [draft-twine-ftpmd5-00](https://mina.apache.org/ftpserver-project/draft-twine-ftpmd5-00.html)
- [draft-somers-ftp-mfxx-00](http://www.omz13.com/downloads/draft-somers-ftp-mfxx-00.html#anchor8)

<a id="documentation--developing-ftpserver"></a>

## Developing FtpServer

- [Getting the source](#getting_source)
- [Building](https://mina.apache.org/ftpserver-project/building.html)
- [Releasing](https://mina.apache.org/ftpserver-project/releasing.html)

---

<a id="getting_source"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/getting_source.html -->

<!-- page_index: 7 -->

<a id="getting_source--overview"></a>

## Overview

Sources for the Apache MINA projects are currently managed through GIT. Instructions on GIT use can be found at <http://git-scm.com/book/>.

There is also a mirror on [GitHub](https://github.com/apache/mina-ftpserver)

<a id="getting_source--normal-git-access"></a>

## Normal Git Access

Anyone can check code out of Git. You only need to specify a username and password in order to update the Git repository, and only MINA committers have the permissions to do that. We run Git over standard HTTPS, so hopefully you won’t have problems with intervening firewalls.

<a id="getting_source--web-access"></a>

## Web Access

The following is a link to the [online source repository](https://gitbox.apache.org/repos/asf?p=mina-ftpserver.git;a=summary).

<a id="getting_source--cloning-from-the-git-repo"></a>

# Cloning from the Git repo

Again, anyone can do this. Use a command like to checkout the current development version (the trunk):

read only access :

git clone <http://gitbox.apache.org/repos/asf/mina-ftpserver.git> ftpserver

write access :

git clone <https://gitbox.apache.org/repos/asf/mina-ftpserver.git> ftpserver

You will not be able to commit into the project if you are not a committer.

There are currently two working branches:

- 1.2.X, the mot recent development branch
- 1.1.X, a maintainance branche

All the other branches are dead wood, including the ‘master’ branch

Be sure to checkout the **1.2.X** branch if you want to participate in the latest branch.

<a id="getting_source--documentation"></a>

# Documentation

The Website documentation is published via Apache SVN pubsub. The website source resides at

<https://svn.apache.org/repos/asf/mina/site/trunk/content/ftpserver-project/>

<a id="getting_source--coding-convention"></a>

# Coding Convention

We follow [Sun’s standard Java coding convention](https://www.oracle.com/technetwork/java/codeconventions-150003.pdf) except that we always use spaces instead of tabs. Please download [the Eclipse Java formatter settings file](assets/files/improvedjavaconventions_af8674a3ea2fe874.xml) before you make any changes to the code.

This file is also available in the `/resources` directory.

---

<a id="faq"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/faq.html -->

<!-- page_index: 8 -->

<a id="faq--faq"></a>

# FAQ

<a id="faq--general"></a>

## General

- [General](#faq--general)
  - [My server fails with java.net.SocketException: Too many files open](#faq--my-server-fails-with-javanetsocketexception-too-many-files-open)
  - [Change the timeout in Windows](#faq--change-the-timeout-in-windows)
  - [Change the timeout in Linux](#faq--change-the-timeout-in-linux)
  - [How can I add other language translations?](#faq--how-can-i-add-other-language-translations)
  - [How can I send binary data stored in a database when the FTP Server gets the RETR command?](#faq--how-can-i-send-binary-data-stored-in-a-database-when-the-ftp-server-gets-the-retr-command)
  - [Why I am getting ClassNotFoundException when I am trying to use database based user manager?](#faq--why-i-am-getting-classnotfoundexception-when-i-am-trying-to-use-database-based-user-manager)
  - [I am unable to run FtpServer on top of Glassfish although it is running correctly over tomcat.](#faq--i-am-unable-to-run-ftpserver-on-top-of-glassfish-although-it-is-running-correctly-over-tomcat)
<a id="faq--my-server-fails-with-javanetsocketexception-too-many-files-open"></a>
<a id="faq--my-server-fails-with-java.net.socketexception:-too-many-files-open"></a>

### My server fails with java.net.SocketException: Too many files open

Network sockets are treated like files and your operating system has a limit to the number of file handles it can manage. Running out of file handles is usually due to a large number of clients connecting and disconnecting frequently. As specified by TCP, after being closed sockets remain in the TIME\_WAIT state for some additional time. The reason is to ensure that delayed packets arrive on the correct socket. In Windows, the default TIME\_WAIT timeout is 4 minutes, in Linux it is 60 seconds.

<a id="faq--change-the-timeout-in-windows"></a>

### Change the timeout in Windows

1. Run regedit to start the Registry Editor
2. Locate the following key: HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\tcpip\Parameters
3. Add a new value named TcpTimedWaitDelay asa decimal and set the desired timeout in seconds (30-300)
4. Reboot

<a id="faq--change-the-timeout-in-linux"></a>

### Change the timeout in Linux

1. Update the configuration value by running (30 seconds used in the example)

   echo 30 > /proc/sys/net/ipv4/tcp\_fin\_timeout
2. Restart the networking component, for example by running

   /etc/init.d/networking restart
3. or

   service network restart

<a id="faq--how-can-i-add-other-language-translations"></a>

### How can I add other language translations?

First you need to specify your language name in config.message.languages configuration parameter. Then if you start the FTP server UI, you will see your language entry in the message panel. Translate messages and finally save your translated messages.

We are always interested in adding more translations to the official distribution of FtpServer. If you produce a translation and can contribute it back to the project, please create a new JIRA issue so that we can add it to the core product.

<a id="faq--how-can-i-send-binary-data-stored-in-a-database-when-the-ftp-server-gets-the-retr-command"></a>

### How can I send binary data stored in a database when the FTP Server gets the RETR command?

You can write your own ftplet to do this. The following code will clarify this.

```java
public FtpletEnum onDownloadStart(FtpSession session, FtpRequest request,
        FtpReplyOutput response) throws FtpException, IOException {

    String requestedFile = request.getArgument();

    // get input stream from database - BLOB data
    InputStream in = getInputStreamFromDatabase(requestedFile);
    if (in == null) {
        response.write(new DefaultFtpReply(550, "Cannot find data " + requestedFile));
        return FtpletEnum.RET_SKIP;
    }

    // open data connection
    DataConnection out = null;
    response.write(new DefaultFtpReply(150, "Getting data connection."));
    try {
        out = session.getDataConnection().openConnection();
    } catch (Exception ex) {
    }
    
    if (out == null) {
        response.write(new DefaultFtpReply(425, "Cannot open data connection."));
        return FtpletEnum.RET_SKIP;
    }

    // transfer data
    try {
        out.transferToClient(in);
        response.write(new DefaultFtpReply(226, "Data transfer okay."));
    } catch (Exception ex) {
        response.write(new DefaultFtpReply(551, "Data transfer failed."));
    } finally {
        session.getDataConnection().closeDataConnection();
        in.close();
    }
    return FtpletEnum.RET_SKIP;
}
```

<a id="faq--why-i-am-getting-classnotfoundexception-when-i-am-trying-to-use-database-based-user-manager"></a>

### Why I am getting ClassNotFoundException when I am trying to use database based user manager?

JDBC driver Jar file should be in CLASSPATH or it has to be copied in the INSTALL\_DIR/common/lib directory. Did you specify fully qualified JDBC driver class name in config.user-manager.jdbc-driver configuration parameter?

<a id="faq--i-am-unable-to-run-ftpserver-on-top-of-glassfish-although-it-is-running-correctly-over-tomcat"></a>
<a id="faq--i-am-unable-to-run-ftpserver-on-top-of-glassfish-although-it-is-running-correctly-over-tomcat."></a>

### I am unable to run FtpServer on top of Glassfish although it is running correctly over tomcat.

This can be caused by Glassfish’s QuickStartup mode which was the default one in some versions. In order to disable quick startup, add the following line to your domain.xml file:

```text
com.sun.enterprise.server.ss.ASQuickStartup=false
```

---

<a id="related_project"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/related_project.html -->

<!-- page_index: 9 -->

<a id="related_project--related-projects"></a>

# Related Projects

<a id="related_project--vfs-ftpserver-bridgehttpvfs-utilssourceforgenetftpserverindexhtml"></a>
<a id="related_project--vfs-ftpserver-bridge"></a>

## [VFS FTPServer Bridge](http://vfs-utils.sourceforge.net/ftpserver/index.html)

This project provides an Apache Commons VFS implementation for the Apache FTPServer project. Instead of working only on local files, with this VFS bridge you can connect to any VFS provider. You can still use a local file system, but you can also use a ZIP file, loop through to another FTP server, or use any other available VFS implementation such as DctmVFS.

<a id="related_project--hdfs-over-ftphttpssitesgooglecomaiponwebnethadoophomehdfs-over-ftp"></a>
<a id="related_project--hdfs-over-ftp"></a>

## [HDFS over FTP](https://sites.google.com/a/iponweb.net/hadoop/Home/hdfs-over-ftp)

FTP server which works on a top of HDFS. It aAllows to connect to HDFS using any FTP client. FTP server is configurable by hdfs-over-ftp.conf and users.conf. Also it allows to use secure connection over SSL and supports all HDFS permissions

---

<a id="mailing_list"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/mailing_list.html -->

<!-- page_index: 10 -->

<a id="mailing_list--mailing-list"></a>

# Mailing List

General information about the FtpServer mailing lists can be found here.

<a id="mailing_list--for-users"></a>

## For Users

Please use this list for any questions regarding how to use FtpServer in your application.

<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Subscribe</td>
<td><a href="mailto:ftpserver-users-subscribe@mina.apache.org">ftpserver-users-subscribe@mina.apache.org</a></td>
</tr>
<tr>
<td>Unsubscribe</td>
<td><a href="mailto:ftpserver-users-unsubscribe@mina.apache.org">ftpserver-users-unsubscribe@mina.apache.org</a></td>
</tr>
<tr>
<td>Post</td>
<td><a href="mailto:ftpserver-users@mina.apache.org">ftpserver-users@mina.apache.org</a></td>
</tr>
<tr>
<td>Archive</td>
<td><a href="http://www.mail-archive.com/ftpserver-users@mina.apache.org/">http://www.mail-archive.com/ftpserver-users@mina.apache.org/</a></td>
</tr>
</tbody>
</table>

<a id="mailing_list--for-developers"></a>

## For Developers

We use the MINA developers list for asking technical questions, discussing feature suggestions or general questions regarding the project.

| Subscribe | [dev-subscribe@mina.apache.org](mailto:dev-subscribe@mina.apache.org) |
| --- | --- |
| Unsubscribe | [dev-unsubscribe@mina.apache.org](mailto:dev-unsubscribe@mina.apache.org) |
| Post | [dev@mina.apache.org](mailto:dev@mina.apache.org) |
| Archive | <http://www.mail-archive.com/dev@mina.apache.org/> |

<a id="mailing_list--subversion-commits"></a>

## Subversion commits

| Subscribe | [commits-subscribe@mina.apache.org](mailto:commits-subscribe@mina.apache.org) |
| --- | --- |
| Unsubscribe | [commits-unsubscribe@mina.apache.org](mailto:commits-unsubscribe@mina.apache.org) |
| Post | [commits@mina.apache.org](mailto:commits@mina.apache.org) |
| Archive | <http://www.mail-archive.com/commits@mina.apache.org/> |

---

<a id="getting_involved"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/getting_involved.html -->

<!-- page_index: 11 -->

<a id="getting_involved--getting-involved"></a>

# Getting Involved

Apache FtpServer communicates using our [Mailing Lists](#mailing_list). If you have any questions, feedback or suggestions, you’re very welcome to join the list and send an email. We are also happy to receive [bug reports and feature requests in our JIRA](https://issues.apache.org/jira/browse/FTPSERVER).

<a id="getting_involved--patches"></a>

# Patches

The best chance of getting your bug or feature fixed is to provide a patch, if they fit our goals we will usually have them committed within a few days. The Apache Contributors page has excellent [information on how to produce patches](http://apache.org/dev/contributors.html#patches).

---

<a id="reporting_bug"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/reporting_bug.html -->

<!-- page_index: 12 -->

<a id="reporting_bug--reporting-a-bug"></a>

# Reporting a Bug

We are using JIRA to track all FtpServer issues including bugs. Please visit our [issue tracker page](http://issues.apache.org/jira/browse/FTPSERVER) to report a bug.

As an alternative you can also create some **[GitHub issues](https://github.com/apache/mina-ftpserver/issues)**

<a id="reporting_bug--how-to-report-a-bug"></a>

## How to report a bug

Writing a bug report with detailed information will help us to fix your problem sooner.

- Make sure if the bug you are going to report doesn’t exist yet.
- Attaching JUnit test case which reproduces the problem will put your report in our highest priority.
- Attach full thread stack dump if you suspect a dead lock.
- Attach full heap dump if you suspect a memory leak.
- Specify the environment in detail as much as possible.
  - Operating system version, distribution, architecture, …
  - JVM vendor, version, build number, command line arguments, …
  - Network settings

---

<a id="contributors"></a>

<!-- source_url: https://mina.apache.org/ftpserver-project/contributors.html -->

<!-- page_index: 13 -->

<a id="contributors--contributors"></a>

# Contributors

<a id="contributors--committers"></a>

## Committers

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another (in alphabetic order).

- Rana Battacharyya
- Sebastan Bazley
- Hervé Boutemy
- Gary Gregory
- [Niklas Gustavsson](http://protocol7.com/)
- Paul Hammant
- Nikola Ken Barozzi
- David Latorre
- Trustin Lee
- Emmanuel Lécharny
- Sai Pullabhotla
- Johnny Valiere
- Julien Vermillard
- Sergey M Vladimirov
- Mark Webb
- XenoAmess

---
