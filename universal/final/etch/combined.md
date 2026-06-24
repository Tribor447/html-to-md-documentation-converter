# 2016/12/13 - Apache Etch has been retired.

## Navigation

- General
  - [Home](#index)
  - [Downloads](#downloads)
- Community
  - [Get Involved](#get-involved)
  - [Who we are](#contributors)
  - [Mailing Lists](#mailinglists)
  - [Bug Tracker](#issue-tracking)
- Development
  - [Source Code](#sources)
  - [Getting Started](#getting-started)
  - [Project Roadmap](#roadmap)
  - [Buildserver](#buildserver)
  - [Tools](#tools)
  - [Release How To](#howto-make-a-release)
- Documentation
  - [Overview](#documentation)
  - [Presentations](#presentations)
- Other pages
  - [Etch The Architecture](#documentation-architecture)
  - [Using the C Binding](#documentation-c-binding-tips-tricks)
  - [Etch Compiler Users Guide](#documentation-compiler-users-guide)
  - [Introduction](#documentation-csharp-binding-users-guide)
  - [Documentation](#documentation-documentation)
  - [Etch Binary Protocol](#documentation-etch-binary-protocol)
  - [Example - Hello World](#documentation-example-hello-world)
  - [Examples](#documentation-examples)
  - [Generated Code Users Guide](#documentation-generated-code-users-guide)
  - [KeepAlive Filter](#documentation-howto-keepalive-filter)
  - [Logger Filter](#documentation-howto-logger-filter)
  - [PwAuth Filter](#documentation-howto-pwauth-filter)
  - [TLS in Etch](#documentation-howto-tls)
  - [Javascript Language Binding](#documentation-javascript-language-binding)
  - [Introduction](#documentation-language-reference)
  - [Overview](#documentation-overview)
  - [Getting Started documentation for upcoming Release 1.1](#documentation-setup-guide-for-users)
  - [2016/12/13 - Apache Etch has been retired.](#roadmap-architecture-message-size)
  - [2016/12/13 - Apache Etch has been retired.](#roadmap-architecture-transport)
  - [Nameservice Client Details ¶](#roadmap-concepts-nameservice-client)
  - [Nameservice Listener Details ¶](#roadmap-concepts-nameservice-listener)
  - [2016/12/13 - Apache Etch has been retired.](#roadmap-concepts-nameservice)
  - [2016/12/13 - Apache Etch has been retired.](#roadmap-concepts-router)
  - [2016/12/13 - Apache Etch has been retired.](#roadmap-service-configuration)

## Content

<a id="index"></a>

<!-- source_url: https://etch.apache.org/index.html -->

<!-- page_index: 1 -->

<a id="index--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="index--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="index--apache-etch"></a>

# Apache Etch

<a id="index--welcome-to-apache-etch"></a>

# Welcome to Apache Etch

Etch is a cross-platform, language- and transport-independent framework for building
and consuming network services. The Etch toolset includes a network service description
language, a compiler, and binding libraries for a variety of programming languages.
Etch is also transport-independent, allowing for a variety of different transports
to be used based on need and circumstance. The goal of Etch is to make it simple to
define small, focused services that can be easily accessed, combined, and deployed
in a similar manner. With Etch, service development and consumption becomes no more
difficult than library development and consumption.

Etch was started because we wanted to have a way to write a concise, formal description of the message exchange between a client and a server, with that message exchange supporting a hefty set of requirements:

- support one-way and two-way, real-time communication
- high performance and scalability
- support clients and servers written in different languages
- support clients/servers running in a wide range of contexts (such as thin web client, embedded device, PC application, or server)
- support anyone adding new language bindings and new transports
- be fast and small, while still being flexible enough to satisfy requirements
- finally, it must be easy to use for developers both implementing and/or consuming the service.

<a id="index--news"></a>

## News

- *Apache Etch 1.4.0*
  This release contains a lot of improvements mainly for the C++-binding. Download the newest version from [downloads](#downloads).
  (2014-08-06)
- *Apache Etch 1.3.0*
  The Apache Etch development team is pleased to announce the first stable release since Etch has become a TLP. You can download the newest version for our [download section](#downloads).
  The release contains a couple of bug fixes for different bindings and the feature complete C++-binding, which is now in beta state.
  (2013-09-26)
- *Etch is an Apache TLP!*
  We are happy and proud to announce that the Apache Board has decided in its board meeting in January to graduate the Apache Etch project.
  The "After-Graduation" process is ongoing. Follow us on [twitter (@apacheetch)](https://twitter.com/apacheetch) to stay up to date.
- *Etch C++ Binding alpha version*
  The Apache Etch team has been working on the C++ Binding for the last few months. Now we are happy to announce that a first working alpha version is now available in the [SVN repository](#sources). Check it out!
  For bug reports or feature request please refer to our [BugTracker](#issue-tracking).
- *Apache Incubator Etch 1.2.0*
  The Apache Etch development team is really pleased to announce the new stable build [Apache Etch 1.2.0-incubating](#downloads).
  (2012-01-03)
- *Apache Incubator Etch at FOSDEM 2011*
  The Apache Etch project was present at FOSDEM 2011. Here you can finde the [slides](http://www.slideshare.net/grandyho/apache-etch-introduction-fosdem-2011) and a [video stream](http://www.youtube.com/watch?v=1h76ch2-G-M).
  (2011-02-07)

<a id="index--project-status"></a>

## Project Status

The Apache Etch project is permanently in progress. The latest stable version can be downloaded [here](#downloads). The language bindings are currently in different states:

- Java - stable
- C# - stable
- C - stable
- C++ - beta
- Google Go - alpha
- Javascript - alpha
- Python - alpha

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="downloads"></a>

<!-- source_url: https://etch.apache.org/downloads.html -->

<!-- page_index: 2 -->

<a id="downloads--apache-etch-downloads"></a>

# Apache Etch Downloads

Welcome to the Apache Etch download page.

<a id="downloads--apache-etch-140-aug-2014"></a>
<a id="downloads--apache-etch-1.4.0-aug-2014"></a>

## Apache Etch 1.4.0 (Aug 2014)

Release Notes can be found [here](http://svn.apache.org/repos/asf/etch/releases/release-1.4.0/RELEASE_NOTES.txt). A list of known bugs for the 1.4.0 release is available [here](https://etch.apache.org/release-140-known-bugs).

| Description |  | Download Link | Signature |
| --- | --- | --- | --- |
| Etch 1.4.0 setup | (Windows) | [apache-etch-1.4.0-windows-x86-setup.exe](http://www.apache.org/dyn/closer.cgi/etch/1.4.0/apache-etch-1.4.0-windows-x86-setup.exe) | [MD5](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-windows-x86-setup.exe.md5) [SHA-512](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-windows-x86-setup.exe.sha) [ASC](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-windows-x86-setup.exe.asc) |
| Etch 1.4.0 binary | (Windows) | [apache-etch-1.4.0-windows-x86-bin.zip](http://www.apache.org/dyn/closer.cgi/etch/1.4.0/apache-etch-1.4.0-windows-x86-bin.zip) | [MD5](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-windows-x86-bin.zip.md5) [SHA-512](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-windows-x86-bin.zip.sha) [ASC](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-windows-x86-bin.zip.asc) |
| Etch 1.4.0 source | (Windows) | [apache-etch-1.4.0-src.zip](http://www.apache.org/dyn/closer.cgi/etch/1.4.0/apache-etch-1.4.0-src.zip) | [MD5](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-src.zip.md5) [SHA-512](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-src.zip.sha) [ASC](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-src.zip.asc) |
| Etch 1.4.0 binary | (Linux) | [apache-etch-1.4.0-linux-x86-bin.tar.gz](http://www.apache.org/dyn/closer.cgi/etch/1.4.0/apache-etch-1.4.0-linux-x86-bin.tar.gz) | [MD5](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-linux-x86-bin.tar.gz.md5) [SHA-512](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-linux-x86-bin.tar.gz.sha) [ASC](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-linux-x86-bin.tar.gz.asc) |
| Etch 1.4.0 source | (Linux) | [apache-etch-1.4.0-src.tar.gz](http://www.apache.org/dyn/closer.cgi/etch/1.4.0/apache-etch-1.4.0-src.tar.gz) | [MD5](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-src.tar.gz.md5) [SHA-512](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-src.tar.gz.sha) [ASC](https://www.apache.org/dist/etch/1.4.0/apache-etch-1.4.0-src.tar.gz.asc) |

<a id="downloads--verifying-the-downloads"></a>

## Verifying the downloads

To ensure the integrity of the release artifacts they are digitally signed. You can find more information about
the way that we sign releases here. To verify the integrity of the downloaded files you must use signatures
downloaded from our main distribution directory not from the distribution mirrors.

MD5 checksums can be verified simply by regenerating the checksum and comparing it against the checksum
(the md5 file) supplied with the release. There are various utilities that can be used to generate the checksum, for example

```
openssl md5 apache-etch-1.4.0-windows-x86-setup.exe
```

or

```
md5sum apache-etch-1.4.0-windows-x86-setup.exe
```

PGP signatures can be verified using PGP or GPG. First download the [KEYS](http://www.apache.org/dist/etch/KEYS) as well as the asc signature file for the relevant distribution. Make sure you get these files from our [main distribution directory](http://www.apache.org/dist/etch/), rather than from a mirror. Then verify the signatures using, for example

```
pgpk -a KEYS
pgpv apache-etch-1.4.0-windows-x86-setup.exe.asc
```

or

```
pgp -ka KEYS
pgp apache-etch-1.4.0-windows-x86-setup.exe.asc
```

or

```
gpg --import KEYS
gpg --verify apache-etch-1.4.0-windows-x86-setup.exe.asc
```

<a id="downloads--apache-etch-release-archives"></a>

## Apache Etch release archives

All previous releases of Etch can be found in the [archives](https://etch.apache.org/archive.html).

---

<a id="get-involved"></a>

<!-- source_url: https://etch.apache.org/get-involved.html -->

<!-- page_index: 3 -->

<a id="get-involved--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="get-involved--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="get-involved--apache-etch"></a>

# Apache Etch

<a id="get-involved--get-involved"></a>

# Get Involved

If you are new to Apache and open source and would like to learn more about how to work in open source, check this [page](http://apache.org/foundation/getinvolved.html).

The Apache Etch project is pleased about any contributions like documentation, source code, bug fixes or feedback. The following infos give you some suggestions on how you can get involved into Apache Etch.

- Subscribe to the [mailing lists](#mailinglists). If you are interested in getting involved at the user level, subscribe to the user mailing list. If you are interested in the development of Etch, then subscribe to the developer list.
- Follow us on Twitter at <http://twitter.com/apacheetch>
- Help answer questions posted to the user mailing list for areas that you are familiar with. Your user experience can be very valuable to other users as well as developers on the project.
- Contribute to feature development. Just let the community know what you would like to work on. It is as easy as that.
- Identify [JIRAs](http://issues.apache.org/jira/browse/ETCH) in the area that you are interested and provide patches.
- The source is maintained in Apache's subversion. Information to the project source code is available [here](#sources).
- Contribute to the user or developer documentation or website. Contribute updates to the Apche CMS content [here](http://svn.apache.org/repos/asf/etch/site/trunk/), create a patch and attach it to a JIRA issue. More infos about the Apache CMS can be found [here](http://svn.apache.org/repos/asf/etch/site/trunk/README).
- If in doubt about where to start, send a note to the mailing list and mention your area of interest. Any questions are welcome. We would like you to be involved.
- Provide Feedback: What is working well? What is not? Any help is good. Be part of the community.

<a id="get-involved--reporting-an-issue-or-asking-for-new-features"></a>

## Reporting an Issue or Asking for New Features

Please use Apache's [JIRA](http://issues.apache.org/jira/browse/ETCH) system to report bugs or request new features. First time users will need to create a login.

Search the existing JIRAs to see if what you want to create is already there. If not, create a new one. Make sure JIRAs are categorized correctly using JIRA categories and are created under the correct component area. Please include as much information as possible in your JIRA to help resolve the issue quicker. This can include version of the software used, platforms running on, steps to reproduce, test case, details of your requirement or even a patch if you have one.

You can always propose a release and drive the release with the content that you want. Another way to get a JIRA into a release is by providing a patch or working with other community members (volunteers) to help you get the problem fixed. You can also help by providing test cases.

In general, the best attempt is made to include as many JIRAs as possible depending on the level of community help. The voting mechanism in the JIRA system can be used to raise the importance of a JIRA to the attention of the committers. Adding comments in the JIRA would help the committers to understand why a JIRA is important to include in a given release.

<a id="get-involved--how-to-submitting-a-patch"></a>

## How to Submitting a Patch

Please follow the steps below to create a patch. It will be reviewed and committed by a committer in the project.

- Perform a full build with all tests enabled for the module the fix is for. Specific build procedures vary by sub-project.
- Confirm that the problem is fixed and include a test case where possible to help the person who is applying the patch to verify the fix.
- Generate the patch using svn diff command as follows:


```

    svn diff file.java > file.patch
```

- Try to give your patch files meaningful names, including the JIRA number
- Add your patch file as an attachment to the associated JIRA issue. You can do this by clicking on the 'Patch Available' box in the screen where the patch is being submitted.

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="contributors"></a>

<!-- source_url: https://etch.apache.org/contributors.html -->

<!-- page_index: 4 -->

<a id="contributors--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="contributors--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="contributors--apache-etch"></a>

# Apache Etch

<a id="contributors--who-we-are"></a>

# Who we are

**Apache Etch Developers**

Who: All of the volunteers who contribute to the Apache Etch project in the form of time, code, documentation. They are active on the developer mailing list, take part in discussions, supply patches, documentation, give constructive suggestions or comments.

Currently all developers are also committers.

**Apache Etch Committers**

Who: All of the volunteers who are developers to Apache Etch project and have write access to the subversion repository. All Committers have signed a Contributor License Agreement (CLA) on record. They are responsible for progress and technical aspects of the Apache Etch project.

Active:

- Scott Comer
- Youngjin Park
- Michael Fitzner
- Martin Veith

Inactive:

- Thomas Marsh
- Holger Grandy
- James Dixson
- Gaurav Sandhir
- J.D. Liau
- Rene Barrazza
- Seth Call
- James DeCocq

Further information about the project organisation with a list of all commiters and project mentors can be found [here](http://people.apache.org/committers-by-project.html#etch).

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="mailinglists"></a>

<!-- source_url: https://etch.apache.org/mailinglists.html -->

<!-- page_index: 5 -->

<a id="mailinglists--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="mailinglists--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="mailinglists--apache-etch"></a>

# Apache Etch

<a id="mailinglists--mailing-lists"></a>

# Mailing Lists

The Apache Etch project maintains three mailing lists. Some of these are available in public.

<a id="mailinglists--user-mailing-list"></a>

### User Mailing List

The user list is for general discussion or questions on using Etch. Etch developers monitor this list and provide assistance when needed.

- [Send](mailto:user@etch.apache.org)(user@etch.apache.org)
- [Subscribe](mailto:user-subscribe@etch.apache.org)(user-subscribe@etch.apache.org)
- [Unsubscribe](mailto:user-unsubscribe@etch.apache.org)(user-unsubscribe@etch.apache.org)
- [Archive](http://mail-archives.apache.org/mod_mbox/etch-user/)(http://mail-archives.apache.org/mod\_mbox/etch-user/)
- [Incubator Archive](http://mail-archives.apache.org/mod_mbox/incubator-etch-user/)(http://mail-archives.apache.org/mod\_mbox/incubator-etch-user/)

<a id="mailinglists--developer-mailing-list"></a>

### Developer Mailing List

The developer list is for Etch developers to discuss ongoing work, make decisions, and vote on technical issues.

- [Send](mailto:dev@etch.apache.org)(dev@etch.apache.org)
- [Subscribe](mailto:dev-subscribe@etch.apache.org)(dev-subscribe@etch.apache.org)
- [Unsubscribe](mailto:dev-unsubscribe@etch.apache.org)(dev-unsubscribe@etch.apache.org)
- [Archive](http://mail-archives.apache.org/mod_mbox/etch-dev/)(http://mail-archives.apache.org/mod\_mbox/etch-dev/)
- [Incubator Archive](http://mail-archives.apache.org/mod_mbox/incubator-etch-dev/)(http://mail-archives.apache.org/mod\_mbox/incubator-etch-dev/)

<a id="mailinglists--commits-mailing-list"></a>

### Commits Mailing List

The commits list receives notifications with diffs when changes are committed to the Etch source tree.

- [Subscribe](mailto:commits-subscribe@etch.apache.org)(commits-subscribe@etch.apache.org)
- [Unsubscribe](mailto:commits-unsubscribe@etch.apache.org)(commits-unsubscribe@etch.apache.org)
- [Archive](http://mail-archives.apache.org/mod_mbox/etch-commits/)(http://mail-archives.apache.org/mod\_mbox/etch-commits/)
- [Incubator Archive](http://mail-archives.apache.org/mod_mbox/incubator-etch-commits/)(http://mail-archives.apache.org/mod\_mbox/incubator-etch-commits/)

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="issue-tracking"></a>

<!-- source_url: https://etch.apache.org/issue-tracking.html -->

<!-- page_index: 6 -->

<a id="issue-tracking--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="issue-tracking--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="issue-tracking--apache-etch"></a>

# Apache Etch

<a id="issue-tracking--bug-tracker"></a>

# Bug Tracker

Please use [Apache\'s JIRA](http://issues.apache.org/jira/browse/ETCH) system to report bugs or request new features. The first time
you have to create a login name to get access to the system.

Search the existing JIRAs to see if what you want to create is already there. If not, create a new one. Make sure JIRAs are categorized correctly using JIRA categories and are created under the correct component area. Please include as much information as possible in your JIRA to help resolve the issue quicker. This can include version of the software used, platforms running on, steps to reproduce, test case, details of your requirement or even a patch if you have one.

Further information about how reporting an Issue or Asking for New Features can be found at [Get Involved](#get-involved).

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="sources"></a>

<!-- source_url: https://etch.apache.org/sources.html -->

<!-- page_index: 7 -->

<a id="sources--source-code"></a>

# Source Code

Each stable release provides also a tar and zip archive of the source code. The latest release can be found [here](#downloads). If you would like to get the latest source code from a version control system you can do it with Subversion or Git.

The offical source is maintained in Apache's subversion repository at svn.apache.org. If you are a committer for the project, you should use the https url, otherwise (if you are just interested in a copy) then http is fine.

<a id="sources--subversion"></a>

## Subversion

If you only want browse the project sources, you can do this via a default webbrowser and this [link](http://svn.apache.org/repos/asf/etch/trunk/).

**Check out from Subversion**

Everbody is invited to check out the project sources out of our SVN repository. For committing source code changes, you need a username and password and only committers are allowed to do that. For all those of you, who are not familiar with Subversion, can get some basic information in the [online book](http://svnbook.red-bean.com/). If you do not have a Subversion client for your platform, you can get one at <http://subversion.tigris.org>.

Use the following command to check out:

```
svn co http://svn.apache.org/repos/asf/etch/trunk/
```

**Commit Changes to Subversion**

Use the following command to check out:

```
svn co https://svn.apache.org/repos/asf/etch/trunk/
```

and

```
svn commit
```

to commit changes. Each commit message should include a reference to a JIRA issue and a small note about the change.
Make sure that your *svn:eol-style* is set to *native* in order to use the proper line endings on your machine. These settings are normally located in your subversion config file within the auto-props section.

<a id="sources--git"></a>

## Git

Some of our developers use Git for source management. If you also interested in Git to manage your source code, check out Git documentation and proper client software at <http://git-scm.com/>.

Apache Etch has its own Git Repository at git://git.apache.org/etch.git. There is also a public read-only mirror of all of Apache's SVN at github site http://github.com/apache/etch.

Use the following command to clone the repository:

```
git clone git://git.apache.org/etch.git
```

Apache does not provide a Git Repository with write access. If you would like to work with Git in combination to the Apache SVN repository, please use Git SVN. The following command can be used to clone the SVN repository with Git. Man pages for git-svn can be found [here](http://www.kernel.org/pub/software/scm/git/docs/git-svn.html).

```
git svn clone https://svn.apache.org/repos/asf/etch/trunk/ -r HEAD
```

---

<a id="getting-started"></a>

<!-- source_url: https://etch.apache.org/getting-started.html -->

<!-- page_index: 8 -->

<a id="getting-started--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="getting-started--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="getting-started--apache-etch"></a>

# Apache Etch

<a id="getting-started--getting-started"></a>

# Getting Started

The following steps give you an introduction how to configure, build and work with the Apache Etch sources. At the the moment we support Windows and Linux builds.

1. [Preconditions](#getting-started--preconditions)
2. [Get the source code](#getting-started--getsourcecode)
3. [Build sources](#getting-started--buildsources)

After your build of Apache Etch was successful, you will be able to run the examples in the example directory.

<a id="getting-started--preconditions"></a>

### Preconditions

The tools and libraries mentioned in the following listing must be available on your development machine in order to be able to work with Etch.
It is a good practice to set up a folder containing the external dependencies of all the bindings you would like to build. This folder will be called **ETCH\_EXTERNAL\_DEPENDS** later on.

You can use the workspace contents of our continous integration server as a reference
for your machine:

- Win32: <https://builds.apache.org/job/etch-trunk-windows-x86/ws/externals/>
- Linux: <https://builds.apache.org/job/etch-trunk-linux-x86/ws/externals/>

<table style="width:99%;">
<thead>
<tr>
<th>Component</th>
<th>Prerequisites and dependencies</th>
</tr>
</thead>
<tbody>
<tr>
<td>Etch compiler/code generator  [mandatory for each binding]</td>
<td>
<ul>
<li>Java JDK version 1.5_011 or higher</li>
<li>Apache Ant 1.8.2 or higher</li>
<li>JavaCC 5.0</li>
<li>JUnit 4.3.1</li>
<li> Velocity 1.7</li>
</ul>
</td>
</tr>
<tr>
<td>
    Binding Java
      </td>
<td>
        no additional dependencies
      </td>
</tr>
<tr>
<td>Binding C#</td>
<td>
<ul>
<li>Apache Ant DotNet 1.1</li>
<li>.NET Framework 4.0 (Visual Studio 2008 or higher)</li>
<li>(Mono 1.9 support is experimental)</li>
<li>NUnit 2.5.10.11092</li>
</ul>
</td>
</tr>
<tr>
<td>Binding C</td>
<td>
<ul>
<li>Apache APR 1.4.5</li>
<li>Apache APR Util 1.3.12</li>
<li>Apache APR iconv 1.2.1</li>
<li>Cunit 2.1</li>
<li>Apache Ant CMake 1.0 (cmakeant.jar)</li>
</ul>
</td>
</tr>
</tbody>
</table>

After the download of all the dependencies mentioned above you should now have the following structure (if you want to compile and build for all language bindings):

```
ETCH_EXTERNAL_DEPENDS/
  javacc/
    5.0/
      javacc.jar
  junit /
    4.3.1/
      junit-4.3.1.jar
  nunit/
    2.5.10.11092/
      [contents of nunit 2.5.10.11092 release tgz/zip]      
  velocity/
    1.7/
      velocity-dep-1.7.jar
  apache-ant/
    1.8.2/
      [contents of apache ant 1.8.2 release tgz/zip]
  apache-ant-cmake/
    1.0/
      cmakeant.jar
  apache-ant-dotnet/
    1.1/
      [contents of apache ant dotnet 1.1 release tgz/zip]
  apr/
    1.4.5/
      [apr binary installation, see above]
  cmake/
    2.8.6/
      [contents of cmake standalone 2.8.6 release tgz/zip]    
  cunit/
    2.1/
      [built cunit version, 
       on linux: you can skip this and use system libraries on your machine, e.g. apt-get install      libcunit1 libcunit1-dev
       on win32: see binding-c/runtime/c/README.txt for instructions on building cunit on Win32]
  nsis/ (WINDOWS ONLY)
    2.46/
      [skip if you want no installer built, else: contents of nsis 2.46 standalone zip/tgz]
```

<a id="getting-started--getsourcecode"></a>
<a id="getting-started--get-the-source-code"></a>

### Get the source code

You can checkout the source tree by using the following SVN command:

```
svn co http://svn.apache.org/repos/asf/etch/trunk/
```

If you prefer to use Git you can use git-svn:

```
git svn clone http://svn.apache.org/repos/asf/etch/trunk/
```

<a id="getting-started--buildsources"></a>
<a id="getting-started--build-sources"></a>

### Build sources

As soon as all the required dependencies and the source is available on your machine, you are able to build Etch.

*Note for Linux 64-bit users:*
In order to perform the 32-bit build of the C and C++ bindings make sure that you have installed the 32-bit support libraries. On Ubuntu you need the following packages:

```
ia32-libs
libc6.dev.i386
g++-multilib
gcc-multilib
```

<a id="getting-started--ant-build"></a>

##### Ant Build

1. Open the `scripts/antSetup.bat` (Windows) or `scripts/antSetup.sh` (Linux) with your favourite text editor
2. Check if every environment variable set by the script points to the right location
3. Run the antSetup script to prepare your build environment

   Win32:


```
`scripts/antSetup.bat`
```

   Linux:


```
`source scripts/antSetup.sh`
```

4. Check the correctness of the paths to the jar archives Etch depends on in the `build.dependencies` file inside the root folder.
5. Start build by executeing `ant debug` at the shell prompt

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="roadmap"></a>

<!-- source_url: https://etch.apache.org/roadmap.html -->

<!-- page_index: 9 -->

<a id="roadmap--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="roadmap--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="roadmap--apache-etch"></a>

# Apache Etch

<a id="roadmap--project-roadmap"></a>

# Project Roadmap

The Apache Etch system currently includes the compiler, bindings for java, csharp and c, some documentation, and an ant based build system. Development for Etch cuts across the following categories:

- IDL, Toolchain, and Language Bindings
- Etch Services, of which there are two types
  - Standard IDL implementations that support service and application development
  - Services that support the Etch Cloud
- Validation and Testing
- Documentation

Some of the projects necessarily cut across the above categories, e.g adding a new transport requires some programming in each binding implementation and documentation, etc.

<a id="roadmap--idl"></a>

### IDL

The Etch language could be extended to include more descriptive information about the service being modeled. We have a few RFE's for extensions, some of which are well-thought out and some of which are sketchy.

- Annotations on message, struct, or exception fields which describe acceptable values. For example, a certain field might be required (not null) and the value within a specified range (e.g., percent: 0-100).
- @AsyncReceiver annotation, while solving a certain problem, forces an implementation which may or may not be necessary. And the lack of the annotation where necessary, causes a headache as the implementor is forced to edit the service description to fix it. Look for a better mechanism.
- @Deprecated and @Delete annotations on service elements to warn of retirement or retire elements but retain their information for historical reasons.
- Option to mixin statement to change the direction of the mixed in interface. This allows some flexibility in certain deployment styles.
- Certain service models, such as REST, include a few standard messages but are heavy on object modeling. Etch data modeling could be strengthened to allow modeling of RESTful api.

<a id="roadmap--compiler"></a>

### Compiler

- The internal structure of the compiler could certainly use some love, particularly in the areas of error handling.
- We desperately need some unit testing around the compiler, particularly negative tests (error conditions).
- The build is currently Ant. We're thinking it should be Maven. Maven support for non-java languages is, eh, not all that good. We have an Etch plugin for Ant and sort of Maven. The maven plugin needs to be way better. And having an Etch project archtype for Maven would be nice.
- Better support for Eclipse, Intelli-J, and Visual Studio would be nice.

<a id="roadmap--language-bindings"></a>

### Language Bindings

Improve the current language bindings. Add new bindings.

<a id="roadmap--java"></a>

#### Java

- Xml tagged data format.
- TlsConnection could use server certificate authentication handshake, client authentication via certificate.
- Message filters (i.e., KeepAlive and PwAuth) need to be robustified.
- Always more unit tests and code coverage.
- Java reference documentation e.g. as javadoc

<a id="roadmap--csharp"></a>

#### CSharp

- More or less the same as the Java binding

<a id="roadmap--c"></a>

#### C

- More or less the same as the Java binding

<a id="roadmap--other"></a>

#### Other

- We have started on Cpp, Ruby, Python, Javascript, and Google Go bindings. Some are more complete than others. I have heard of an Objective C binding. The sources for these are not yet part of standard Etch. We're not sure when or how that will happen.

<a id="roadmap--architecture"></a>

### Architecture

General aspects how the architecture could be extended and improved.

- More transport layers e.g. for SOAP, JMS, UDP, Jabber, Protocol Buffers.
- Efficient connection handling and support of many simultaneous connections.
- Transfer of big message e.g. streams [more](#roadmap-architecture-message-size)
- Connection lifecycle management [more](#roadmap-architecture-transport)

<a id="roadmap--concepts-of-application-services"></a>

### Concepts of Application Services

These are proposed services that could be used by any application or service. They abstract common activities through an Etch interface.

<a id="roadmap--cloud"></a>

#### Cloud

Etch Cloud services are services that facilitate the communication between multiple Etch consumers and producers. The following mantra is true for all Etch Cloud:

Neither a service (producer) nor application (consumer) should have to be overtly aware of any Etch cloud service. It should be possible to deploy a service or application with or without any supporting Etch cloud services, with no conditional code or changes to code. Etch cloud services are purely deployment time considerations and are not required for operation.

Etch Name Service - Etch URIs can be very long and cumbersome to maintain, the Etch Name Service allows an Etch Service to look-up the necessary connection URI using an abstract reference. [more](#roadmap-concepts-nameservice)

Etch Router Service - Failover, redundancy, policy enforcement, geographic preference... the Etch Router helps Etch clients find just the right Etch service and stay connected. [more](#roadmap-concepts-router)

<a id="roadmap--logging"></a>

#### Logging

General purpose network-hosted log catcher

<a id="roadmap--configuration"></a>

#### Configuration

Who needs YAML files, pull your configuration over the network [more](#roadmap-service-configuration)

<a id="roadmap--authentication"></a>

#### Authentication

Many services in the web world have single sign on, Etch can too!

<a id="roadmap--documentation"></a>

### Documentation

General project infos are documented via this web page. The documentation about the Etch framework and different language binding will be done with Docbook and as HTML and PDF provided.

<a id="roadmap--testing"></a>

### Testing

While the unit tests assure some level of wire format compliance, nothing beats a validation test suite. We need to be able to plug in different (but compatible) transport options and then run a standard set of tests to verify that things still work (while mixing and matching bindings as well). There are two parts to this:

- Validate Suite Framework and Service definition
- Per binding implementation of the validation suite service

[Here](https://etch.apache.org/roadmap-testing-interoperabillity.html) you can find a discussion on Interoperability Testing Framework.

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="buildserver"></a>

<!-- source_url: https://etch.apache.org/buildserver.html -->

<!-- page_index: 10 -->

<a id="buildserver--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="buildserver--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="buildserver--apache-etch"></a>

# Apache Etch

<a id="buildserver--buildserver"></a>

# Buildserver

The Apache Etch project use the Jenkins build server for doing Nightly Builds. At the moment the build is configured to run on a Windows as well on a Linux machine. You can reach the build server at [link](https://hudson.apache.org/hudson/view/A-F/view/Etch/).

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="tools"></a>

<!-- source_url: https://etch.apache.org/tools.html -->

<!-- page_index: 11 -->

<a id="tools--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="tools--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="tools--apache-etch"></a>

# Apache Etch

<a id="tools--tools"></a>

# Tools

The Apache Etch project developed also some tools to work with the Etch framework. Following you can find more about these.

<a id="tools--wireshark-etch-tracing"></a>

### Wireshark Etch Tracing

The Wireshark plugin for Etch uses compiler-generated files to disassemble the wire protocol (.ewh files). In the Wireshark Etch plugin preferences (Edit -> Preferences -> Protocols -> Etch), you can specify a path to your generated .ewh files and you will get your specific analyzed and displayed directly in Wireshark. The plugin is available in Wireshark since version 1.5.0.

![Wireshark preference window for the Etch protocol](assets/images/etch-wireshark-preferences-window_a534862d028fc074.png)

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="howto-make-a-release"></a>

<!-- source_url: https://etch.apache.org/howto-make-a-release.html -->

<!-- page_index: 12 -->

<a id="howto-make-a-release--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="howto-make-a-release--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="howto-make-a-release--apache-etch"></a>

# Apache Etch

<a id="howto-make-a-release--how-to-make-a-release"></a>

# How to make a release

<a id="howto-make-a-release--introduction"></a>

## Introduction

Apache Etch releases are made according to the release policy of the Apache Software Foundation.
More information about this can be found here:
<http://www.apache.org/dev/release.html>

<a id="howto-make-a-release--prerequisites"></a>

## Prerequisites

This describes the necessary steps to be taken BEFORE drafting a release:

1. Update release depended files in trunk

   - Changelog: /Changelog.txt

     Update the file with the svn log output between the last release and the current trunk:


```
svn log -r \:HEAD
```

     In order to get the revision of the last release you can e.g. use the command


```
svn info https://svn.apache.org/repos/asf/etch/releases/release-\
```

   - Update the version numbers in all files. (e.g. grep the trunk for the last release version). You should get at least to following files:

     - /README.txt
     - /dist-README.txt
     - /compiler/src/main/java/org/apache/etch/compiler/Version.java
     - /doc/libs/global.ent
     - /etch.properties
   - Release notes: /RELEASE\_NOTES.txt

     The release notes do contain important information about the release. Please read through the existing content carefully, add new notes or remove obsolete remarks.
     At the end of the file the release notes exported from JIRA are attached. Those release notes can be copied from the [Roadmap](https://issues.apache.org/jira/browse/ETCH/?selectedTab=com.atlassian.jira.jira-projects-plugin:roadmap-panel) section of JIRA for the respective release.

<a id="howto-make-a-release--create-the-release-artifacts"></a>

## Create the release artifacts

Apache Etch is currently shipped both as a source package (mandatory according to ASF Policy!) and as a binary package for different platforms.
Therefore you need the toolchains for Linux as well as Windows at hand in order to create all the release artifacts.

**Make sure all the stable bindings are building, the unit tests do succeed and all the examples are working.**

1. Source packages

   Create a zip-compressed archive and a tarball.


```

svn export trunk/ apache-etch-\-src
zip -r apache-etch-\-src.zip apache-etch-\-src
tar cfzv apache-etch-\-src.tar.gz apache-etch-\-src/
```

2. Binary packages:

   The binaries are build with ant by calling the release target.


```

On Linux:
ant release -DEtch.property.platformVersion=x86 -DEtch.property.osVersion=linux


On Windows:
ant release -DEtch.property.platformVersion=x86 -DEtch.property.osVersion=windows
```

   After a successful build the binary packages are located at trunk/target/Installers/packages
3. Create checksums and signatures for all the created packages


```

MD5
gpg --print-md MD5 ${artifact} > ${artifact}.md5


SHA512
gpg --print-md SHA512 ${artifact} > ${artifact}.sha


Signature
gpg -u \ --armor --output ${artifact}.asc --detach-sig ${artifact}
```

4. Upload release candidate

   All the generated artifacts are committed to the [/dev](https://dist.apache.org/repos/dist/dev/etch/) tree of the dist repository in order to make them testable for other members of the PMC before they need to cast their vote.
5. Start [VOTE] thread on the dev@etch.a.o mailing list
6. Wait at least 72h for votes.

<a id="howto-make-a-release--publish-the-release"></a>

## Publish the release

As soon as a release got accepted, it can be published officially on the Apache servers.

1. Move the approved release candidate from the [/dev](https://dist.apache.org/repos/dist/dev/etch/) tree of the dist repository to the [/release](https://dist.apache.org/repos/dist/release/etch/) directory.
2. Update news and download section on the website.
3. Create known bugs webpage with link to the bug tracker.
4. Send out the good news on all known communication channels (mailing lists, [Etch's Twitter account](https://twitter.com/apacheetch)).

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="documentation"></a>

<!-- source_url: https://etch.apache.org/documentation.html -->

<!-- page_index: 13 -->

<a id="documentation--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="documentation--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="documentation--apache-etch"></a>

# Apache Etch

<a id="documentation--documentation"></a>

# Documentation

*We are currently working on a restructuring and expansion of the Etch documentation. In the meanwhile you can use the existing documentation embedded below.*

<iframe frameborder="0" id="docFrame" name="docFrame" onload="resizeIframe()" src="documentation/documentation.html" width="99%"></iframe>

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="presentations"></a>

<!-- source_url: https://etch.apache.org/presentations.html -->

<!-- page_index: 14 -->

<a id="presentations--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="presentations--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="presentations--apache-etch"></a>

# Apache Etch

<a id="presentations--presentations"></a>

# Presentations

The Etch middleware has been introduced on several events. Please find the slides and corresponding videos below:

- FOSDEM 2011
  - Slides at [Slideshare](http://www.slideshare.net/grandyho/apache-etch-introduction-fosdem-2011)
  - Video at [Youtube](http://www.youtube.com/watch?v=1h76ch2-G-M)
- Cisco Unified Application Environment Developer Conference
  - Slides can be found [here](http://developer.cisco.com/c/document_library/get_file?groupId=13403&folderId=63902&name=DLFE-8208.pdf)
  - Video is available [here](http://developer.cisco.com/web/cuae/devconf2008_session_3)

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="documentation-architecture"></a>

<!-- source_url: https://etch.apache.org/documentation/architecture.html -->

<!-- page_index: 15 -->

# Etch The Architecture

- 1 [Etch The Architecture](#documentation-architecture--architecture-etchthearchitecture)

- 1.1 [Etch Client Architecture](#documentation-architecture--architecture-etchclientarchitecture)
- 1.2 [Etch Service Architecture](#documentation-architecture--architecture-etchservicearchitecture)
- 1.3 [Datagram Based Transport](#documentation-architecture--architecture-datagrambasedtransport)
- 1.4 [Core Modules](#documentation-architecture--architecture-coremodules)

<a id="documentation-architecture--etch-the-architecture"></a>

# Etch The Architecture

<a id="documentation-architecture--etch-client-architecture"></a>

## Etch Client Architecture

![](assets/images/etchclient3_0d43ff78cfbea759.png)

<a id="documentation-architecture--etch-service-architecture"></a>

## Etch Service Architecture

![](assets/images/etchservice1_1d9a9f4c4eb477f5.png)

<a id="documentation-architecture--datagram-based-transport"></a>

## Datagram Based Transport

For datagram based protocol like **UDP**.

![](assets/images/datagram_02c07c54c47d9453.png)

<a id="documentation-architecture--core-modules"></a>

## Core Modules

<a id="documentation-architecture--listener"></a>

### Listener

The listener for a transport accepts a connection and constructs a new server session to process messages on that connection for that session. In the case of TCP, the listener would normally be a TCP listening socket. For UDP, it might be an unconnected datagram socket

<a id="documentation-architecture--value-factory"></a>

### Value Factory

The value factory is the repository of the compiler generated service meta-data and methods for serializing and de-serializing custom data objects.

<a id="documentation-architecture--out-of-band-message-handler"></a>

### Out-Of-Band Message Handler

Normally the client or server implementation, the out-of-band message handler is the last handler in a chain which originates at the lowest level of the transport stack. Transport messages flow up the stack until someone handles them or they get to the top of the stack where the client or server implementation handles them. Transport messages are not the same as service messages, in that they communicate information about the transport stack itself.

<a id="documentation-architecture--stub-client"></a>

### Stub Client

The stub client accepts service messages not otherwise distributed to mailboxes by the mailbox manager, turning them into calls on the client implementation where they are handled.

<a id="documentation-architecture--stub-server"></a>

### Stub Server

The stub server accepts service messages not otherwise handled by the mailbox manager, turning them into calls on the server implementation where they are handled.

<a id="documentation-architecture--remote-client"></a>

### Remote Client

The remote client implements the client interface turning method calls into messages which are passed across the network to the stub client.

<a id="documentation-architecture--remote-server"></a>

### Remote Server

The remote server implements the server interface turning method calls into messages which are passed across the network to the stub server.

<a id="documentation-architecture--mailbox-manager"></a>

### Mailbox Manager

When a call is made, the mailbox manager allocates a mailbox and ties it to the message id of the resulting message before it is sent. The mailbox manager then watches incoming messages, grabbing those that are responses and delivering them to their associated mailboxes.

<a id="documentation-architecture--filter-chain"></a>

### Filter Chain

The filters get to watch, edit, or intercept service messages as they flow up and down the transport stack. Filters might also originate their own messages, originate or intercept out-of-band transport messages, and carry on a dialog with filters on the remote end of a session.

- Auth - the auth filter might add authentication data to outgoing messages and process authentication data on incoming messages when using a session based on a packet protocol; it might also dialog with an auth filter on the remote side to authenticate session based on a stream protocol.

- Log - records the incoming and outgoing messages.

- Session - when using a shared packet protocol, segregates the packets by session much like mailbox manager does.

- Throttle - limits the amount of traffic on a particular session.

- Reliable - adds reliability to an unreliable connection.

- Security - helper filter for Packet Layer Security. Assists with key changes.

- KeepAlive - periodic message to keep the connection open / detect connection failure.

- RemoteMonitor - records the incoming and outgoing messages to a remote service.

- QueuedOutput - used to queue outgoing packets for later delivery when it is important to not delay the sender.

<a id="documentation-architecture--messagizer"></a>

### Messagizer

The Messagizer intercepts messages flowing down the transport stack (say, from a filter or Mailbox Manager), reformats them into packets, and delivers them to a packet source for transport to the remote end of a session. Packets flowing up the transport stack are also reformatted into messages and delivered to a message handler (say, to a filter or Mailbox Manager). The message formatter is pluggable.

<a id="documentation-architecture--packetizer"></a>

### Packetizer

The Packetizer intercepts packets flowing down the transport stack (say, from Messagizer), reformats them into data, and delivers them to a data source for transport to the remote end of a session. Data flowing up the transport stack are also reformatted into packets and delivered to a packet handler (say, to Messagizer).

<a id="documentation-architecture--transport-layer-security"></a>

### Transport Layer Security

Security encryption and message authentication which prevents snooping or tampering with the data stream.

<a id="documentation-architecture--stream-protocol"></a>

### Stream Protocol

A stream protocol such as TCP.

<a id="documentation-architecture--optional-packet-oriented-protocol"></a>

### Optional Packet Oriented Protocol

If a packet oriented protocol is needed, the bottom three modules (Packetizer, Transport Layer Security, and Stream Protocol) are replaced with Packet Layer Security and Packet Protocol. These two modules serve an equivalent purpose. Care needs to be taken to manage the session, in particular session life cycle.

---

<a id="documentation-c-binding-tips-tricks"></a>

<!-- source_url: https://etch.apache.org/documentation/c-binding-tips-tricks.html -->

<!-- page_index: 16 -->

<a id="documentation-c-binding-tips-tricks--using-the-c-binding"></a>

# Using the C Binding

This guide uses "xxx" as the service name. Substitute with the service name from your etch file.

<a id="documentation-c-binding-tips-tricks--generated-code"></a>

## Generated code

The C Binding compiler is called using

```

etch -b c -d . -w INTF,MAIN,IMPL,CLIENT,SERVER xxxNSDL.etch
```

It generates code for both sides (client and server). The main files you need to change manually to add your implementation are:

| File | Function |
| --- | --- |
| xxx\_client\_main.c | main method of client, starts runtime, connects to server, calls of server methods, disconnect, destroy runtime |
| xxx\_listener\_main.c | main method of server, starts runtime, waits for calls |
| xxx\_server\_impl.c/.h | implementations of server directed methods |
| xxx\_client\_impl.c/.h | implementations of client directed methods |

<a id="documentation-c-binding-tips-tricks--how-to-implement-a-method-on-the-server-on-the-client"></a>

## How to implement a method on the server / on the client

The following steps describe implementation of server-directed methods. Since Etch is symmetric, the client directed functions are implemented exactly the
same way in the client-related generated files.

Assume you have an IDL containing

```

	@Direction(server)
	int simpleFunction(int x)
```

- open xxx\_server\_impl.c
- declare an implementation of simpleFunction,e.g.:


```

etch_int32* simpleFunctionImpl(void* thisx, etch_int32* x);
```



![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

You can get the desired function signatures from xxx\_interface.h. This file contains typedefs for all functions from the NSDL.

- implement simpleFunction, e.g:


```

etch_int32* simpleFunctionImpl(void* thisx, etch_int32* x){
    etch_int32* result;
    result = new_int32(x->value + 1);
    etch_object_destroy(x);
    return result;
}
```



![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

The first parameter is an instance of the server\_impl object. It also contains a reference to the calling client. You can use this for callbacks (if the call is @AsyncReceiver or @Oneway, otherwise you will end up in a deadlock). To do a callback, do the following:

```

    ((tester_server_impl*)thisx)->client->callbackFunctionName(((tester_server_impl*)thisx)->client, ...);
```



![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

Parameters of functions have to be destroyed by the function implementation using etch\_object\_destroy.

- find function new\_xxx\_server\_impl, this function is called when a client connects (the client is given as parameter)
- add the function pointer of simpleFunctionImpl to the pserver object in this function. This "registers" the function as the implementation of the call.


```

xxx_server_impl* new_xxx_server_impl(xxx_remote_client* client) {
    .... // some other code
    pserver->simpleFunction = pserver_base->simpleFunction = simpleFunctionImpl;
}
```

- Thats it!

![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

If you want to return a user defined exception (which was defined in the NSDL), then simply return it in your function implementation instead of the usual return value.

<a id="documentation-c-binding-tips-tricks--how-to-call-a-method-on-the-server-on-the-client"></a>

## How to call a method on the server / on the client

As above, the instructions below are symmetrical for client and server. Server directed calls are called like this:

- open xxx\_client\_main.c
- find main method
- add your call after the starting of the runtime, e.g.

```

        ...//some code
	etch_int32* result;
        ...//some code

        //start the runtime and connect
        etch_status = tester_helper_remote_server_start_wait(remote, waitupms);
        ...//some code
 
        //call the remote function
	result = remote->simpleFunction(remote,new_int32(42));
	if(is_etch_exception(result)){
                wchar_t* extext = NULL;
	 	ex = (etch_exception*)result;
                if(etch_exception_get_message(ex)){
                      extext = etch_exception_get_message(ex)->v.valw;
                }
                ..//do something with exception message...
        }else{
                ..//do something with result
        }
  
        ..//do something with result
        etch_object_destroy(result);
}
```

![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

Result Objects have to be freed by the caller using etch\_object\_destroy. Parameters of calls will be freed by the runtime automatically.

![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

You can get an built-in exception from any remote Etch call (e.g. in case of timeouts). This is why the code above contains is\_etch\_exception(result).
Please note that there are special is\_blabla\_exception test methods generated for used defined exception, which you can use to further refine the type of exception "thrown".

<a id="documentation-c-binding-tips-tricks--memory-management"></a>

## Memory Management

The C Binding for Etch has the following memory management rules:

- Implementation side: Parameters of functions have to be destroyed by the function implementation using etch\_object\_destroy.
- Caller side: Result Objects have to be freed by the caller using etch\_object\_destroy. Parameters of calls will be freed by the runtime automatically.

All Etch Objects (including the primitive type wrappers) are freed using

```

etch_object_destroy(void* val)
```

<a id="documentation-c-binding-tips-tricks--etch-primitive-data-types"></a>

## Etch primitive data types

All primitive types have constructurs of the form

```

new_int32(42)
```

<a id="documentation-c-binding-tips-tricks--user-defined-struct-types"></a>

## User defined struct types

Etch generates structs and constructors for user defined types.
Assume you have the following in your IDL:

```

	struct simpleStruct (
		int x,
		int y
	)
```

The compiler will generate (in xxx\_interface.c/.h)

```

typedef struct tester_simpleStruct
{
    etch_object object;
    int x;
    int y; 
 } tester_simpleStruct;


tester_simpleStruct* new_tester_simpleStruct();
```

You can pass those structs to Etch function calls just like primitive type wrappers. You can also use etch\_object\_destroy on them to free the memory.

<a id="documentation-c-binding-tips-tricks--array-types"></a>

## Array types

Arrays in the IDL are implemented using the struct

```

etch_nativearray
```

You have to supply the correct CLASSID for the content for the C Binding to work properly. Here are samples for primitive and complex arrays:

<a id="documentation-c-binding-tips-tricks--primitive-arrays"></a>

### Primitive Arrays

```

	int values[4] = {0,1,2,3};
	const int numdims = 1, itemsize = sizeof(int), itemcount = sizeof(values)/itemsize;
	param = new_etch_nativearray_from (values, CLASSID_ARRAY_INT32,
            itemsize, numdims, itemcount, 0, 0);
```

"numdims" is the number of dimensions of the array (e.g. int[] vs. int[][]). The last three parameters of new\_etch\_nativearray are the sizes of the (up to) three dimensions of the array. More dimensions are not supported.

<a id="documentation-c-binding-tips-tricks--complex-typed-arrays"></a>

### Complex typed Arrays

Assume the NSDL with "simpleStruct" from above. Create an array of simplestruct using:

```

    int arraysize = 5;
    tester_simpleStruct** values = etch_malloc(arraysize * sizeof(tester_simpleStruct*),0);
    ... //fill values
    etch_nativearray* natarray = new_etch_nativearray_from(
values, CLASSID_ARRAY_STRUCT, sizeof(tester_simpleStruct*), 1, arraysize, 0, 0);
    natarray->content_class_id = CLASSID_XXX_SIMPLESTRUCT;
    natarray->content_obj_type = ETCHTYPEB_USER;
    natarray->is_content_owned = TRUE;
    ... // do something with natarray
```

![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

For complex typed arrays you have to supply the CLASSID of the content of the object. Those CLASSIDs are generated by the compiler for your user defined types.

![](https://cwiki.apache.org/confluence/images/icons/emoticons/warning.gif)

The field is\_content\_owned tells Etch whether it should destroy the array content on array destruction, too. This will take effect when calling etch\_object\_destroy on the natarray or if it is destroyed by the runtime itself (e.g. when it is used as a remote call parameter, see above).

---

<a id="documentation-compiler-users-guide"></a>

<!-- source_url: https://etch.apache.org/documentation/compiler-users-guide.html -->

<!-- page_index: 17 -->

# Etch Compiler Users Guide

- 1 [Etch Compiler Users Guide](#documentation-compiler-users-guide--compilerusersguide-etchcompilerusersguide)

- 1.1 [Name](#documentation-compiler-users-guide--compilerusersguide-name)
- 1.2 [Synopsis](#documentation-compiler-users-guide--compilerusersguide-synopsis)
- 1.3 [Description](#documentation-compiler-users-guide--compilerusersguide-description)
- 1.4 [Options](#documentation-compiler-users-guide--compilerusersguide-options)
- 1.5 [Detailed Examples](#documentation-compiler-users-guide--compilerusersguide-detailedexamples)

<a id="documentation-compiler-users-guide--etch-compiler-users-guide"></a>

# Etch Compiler Users Guide

<a id="documentation-compiler-users-guide--name"></a>

## Name

etch - compiler for binding code into the Etch runtime environment.

<a id="documentation-compiler-users-guide--synopsis"></a>

## Synopsis

```
etch  --help|-h
etch  --version|-v
etch [ --output-dir|-d <outputDir> ]
     [  --who|--what|-w <what>  ]
     [ --ignore-global|-g ] [ --ignore-local|-l ]
     [ --word-list|-W  <wordList> ]
     [ --include-Path|-I <includePath> ]
     [ --ignore-Include-Path|-i ]
     [ --dir-mixin|-m <mixinOutputDir> ]
     [ --no-mixin-artifacts|-n] [ --no-flatten|-f ] [ --quiet|-q ]
     --binding|-b <binding> <file>
```

<a id="documentation-compiler-users-guide--description"></a>

## Description

The Etch compiler processes input etch files and generates target server and/or client code for the selected binding that is integrated with the Etch runtime environment.

Source and target filename suffixes identify language bindings and the kind of processing performed:

.c C target

.cs C# target

.etch Etch source

.java Java target

.kwd Reserved words lists

.rb Ruby target

.xml XML target

.py Python Target

<a id="documentation-compiler-users-guide--options"></a>

## Options

This section describes the compiler options in details

<a id="documentation-compiler-users-guide--help-option"></a>

### Help Option

--help

-help

-h

?

Print a description of the command options and parameters and then exit.

<a id="documentation-compiler-users-guide--usage"></a>

#### Usage

```
etch -h
```

<a id="documentation-compiler-users-guide--output-directory-option"></a>

### Output Directory Option

-d outputDir

--outputDir outputDir

Specifies the output directory where etch files will be generated

<a id="documentation-compiler-users-guide--usage-2"></a>

#### Usage

```
etch -d c:\temp Foo.etch
```

<a id="documentation-compiler-users-guide--binding-option"></a>

### Binding Option

-b binding

--binding binding

Specifies the target language binding to generate. For example "etch -b java" will generate the java binding. Bindings currently supported are java, csharp and xml. In future the plan is to support c, ruby, python and javascript.

<a id="documentation-compiler-users-guide--usage-3"></a>

#### Usage

```
etch -b java Foo.etch
```

<a id="documentation-compiler-users-guide--what-option"></a>

### What option

-w what

--who what

--what what

Selects what to generate. What can include: server, client, or both; impl, helper, main, or all; and force.

It is also possible to specify more than one option. For example, a user can specify "etch -w both,helper,main" or "etch -w all". If more than one option is specified, please make sure to separate it by a comma.

Force forces potentially modified files such as impl, main to be overwritten if they already exist in the output directory.

<a id="documentation-compiler-users-guide--usage-4"></a>

#### Usage

```

etch -b java -w client Foo.etch

// Generates Client Code

etch -b java -w server Foo.etch

// Generates Server Code

etch -b java -w both Foo.etch

// Generates both client and server code

etch -b java -w both,impl,main Foo.etch

// Generates Impl and Main code for both server and client

etch -b java -w all Foo.etch

// Generates all code Foo.etch (all is a superset of all -w options)

etch -b java -w all,force Foo.etch

// Generates all code, as well as overwrite impl and main for both server and client
```

<a id="documentation-compiler-users-guide--ignore-global-reserved-word-list-option"></a>

### Ignore Global Reserved Word List Option

-g

--ignore-global

Ignore the global reserved words list for Etch.

<a id="documentation-compiler-users-guide--ignore-local-reserved-word-list-option"></a>

### Ignore Local Reserved Word List Option

-l

--ignore-local

Ignore the local reserved words list for the binding.

<a id="documentation-compiler-users-guide--load-reserved-word-list-option"></a>

### Load Reserved Word List Option

-W wordList

--word-list wordList

Specifies the file name of a reserved words list to load, either augmenting or replacing the global and local word lists.

<a id="documentation-compiler-users-guide--include-option"></a>

### Include Option

-I path

--include-path path

Append the specified path to the path of directories searched for include files as defined in the environment variable ETCH\_INCLUDE\_PATH.

<a id="documentation-compiler-users-guide--usage-5"></a>

#### Usage

```
etch -b java -I c:\temp Foo.etch

Please see Detailed Example section for an elaborate example
```

<a id="documentation-compiler-users-guide--ignore-include-path-option"></a>

### Ignore Include Path Option

-i

--ignore-include-path

Ignore the path of directories searched for include files as defined in the environment variable ETCH\_INCLUDE\_PATH.

<a id="documentation-compiler-users-guide--suppress-mixin-artifact-option"></a>

### Suppress Mixin Artifact Option

-n

--no-mixin-artifacts

Mixin artifacts are not generated when this option is specified. By default, mixin artifacts will be generated.

<a id="documentation-compiler-users-guide--mixin-directory-option"></a>

### Mixin Directory Option

-m outputMixinDir

--dir-Mixin

Directory where mixins will be generated. If -m option is not specified, then mixin will be generated in directory specified by -d option. If etch file contains mixin and neither -m -d and -n are specified, then compiler will throw an error

<a id="documentation-compiler-users-guide--usage-6"></a>

#### Usage

```
etch -b java -m c:\temp\mixin -d c:\temp -w all Foo.etch
Please see Detailed Example section for an elaborate example
```

<a id="documentation-compiler-users-guide--no-flatten-option-c-specific"></a>

### No Flatten Option (C# specific)

-f
--no-flatten

Don't flatten the package directories, but rather nest them like java requires. This option is only for C# binding

<a id="documentation-compiler-users-guide--regulate-compiler-logs-option"></a>

### Regulate Compiler Logs Option

-q

--quiet

This option suppresses info messages in the compiler. It only report problems.

<a id="documentation-compiler-users-guide--etch-version"></a>

### Etch Version

-v

--version

Shows the version and exits.

<a id="documentation-compiler-users-guide--detailed-examples"></a>

## Detailed Examples

<a id="documentation-compiler-users-guide--include-example"></a>

### Include Example

To use include files in an etch file, use the .txt extention, not .etch for includes.
You can also include other include files in the etch include files.

```
module etch.bindings.java.compiler.test

@Direction(Both)
@Timeout(4000)
service TestInclude
{
	const int INT1 = 98765431;

	const boolean BOOL3 = false
	const boolean BOOL4 = true
	
	include "testincl.txt";
	
	const boolean BOOL1 = false
	const boolean BOOL2 = true
	
}
```

<a id="documentation-compiler-users-guide--testincl.txt"></a>

#### testincl.txt

```
 
const int INT2 = -2147483648;
include "testincl1.txt";
```

<a id="documentation-compiler-users-guide--mixin-example"></a>

### Mixin Example

---

<a id="documentation-csharp-binding-users-guide"></a>

<!-- source_url: https://etch.apache.org/documentation/csharp-binding-users-guide.html -->

<!-- page_index: 18 -->

<a id="documentation-csharp-binding-users-guide--introduction"></a>

# Introduction

This document will provide details on how to build an etch application using csharp.

<a id="documentation-csharp-binding-users-guide--sample-etch-file"></a>

# Sample Etch File

The following is the etch file we will refer to in this document. Lets call this File Example.etch and store it in directory c:\EtchExamples\Example

```
module etch.examples.example
/** * Service version of hello world.*/ service Example {
/** the number of times to perform the action */ const int COUNT = 4
/* Exception thrown if ping doesn't work.* @param msg the explanation.*/ exception PongException ( string msg )
/** * Says hello to the server.* @param msg a greeting for the server.* @param d the current date.* @return the id of our hello */ @Timeout( 1234 ) @Direction( Server ) int helloServer( string msg, Datetime d )
/** * Says hello to the client.* @param msg a greeting for the client.* @return the id of our hello */ @Timeout( 2345 ) @Direction( Client ) int helloClient( string msg )
/** * Says hello to the client or server.* @param msg a greeting for the client or server.* @return the id of our hello */ @Timeout( 3456 ) @Direction( Both ) int hello( string msg )
/** * Says howdy to the server. Oneway.* @param msg a greeting for the server.*/ @Oneway @Direction( Server ) void howdyServer( string msg )
/** * Says howdy to the client. Oneway.* @param msg a greeting for the client.*/ @Oneway @Direction( Client ) void howdyClient( string msg )
/** * Says howdy to the client or server. Oneway.* @param msg a greeting for the client or server.*/ @Oneway @Direction( Both ) void howdy( string msg )
/** * Pings the other side.* @throws PongException */ @Timeout( 4567 ) @Direction( Both ) @AsyncReceiver( Queued ) void ping() throws PongException}
```

<a id="documentation-csharp-binding-users-guide--using-etch-compiler"></a>

# Using Etch Compiler

Before compiling etch file, please make sure Etch is installed and is present in the path

<a id="documentation-csharp-binding-users-guide--command-line"></a>

## Command Line

- Before we generate the server code, lets create a directory for server (c:\EtchExamples\Example\server).

- From the command line, use the following command to generate the server side code

```
etch -b csharp -d .\server -w server,impl,main Example.etch
```

- This command will generate the server side code under

c:\EtchExamples\Example\server\etch.examples.example

- The directory name "etch.examples.example" is generated by the compiler. This name corresponds to the module name of the etch file.

- Like we did for server, lets create a directory for client (c:\EtchExamples\Example\client)

- Similarly using the following command to generate the client side code


```
etch -b csharp -d .\client -w client,impl,main Example.etch
```

- This command will generate the client code under

c:\EtchExamples\Example\client\etch.examples.example

Please refer to the Etch Compiler Guide for more details on the various compiler options

<a id="documentation-csharp-binding-users-guide--visual-studio-plugin"></a>

## Visual Studio Plugin

- If you are using Visual Studio as your IDE, then you can install the Visual Studio Etch Plugin. TODO Make sure the setup.exe for the plugin is a part of etch install...

- Once the plugin has been installed, open Visual Studio and goto Tools->Add-in Manager. Make sure Etch is checked

- Create a new Empty solution add two projects client and server to the solution.

- Copy Example.etch to both client and server project

- Right click on the etch file in the solution explorer and chose server compiler option for server project. Add the generated files to the project by right clicking on the project and choosing Add->Existing Item. Do the exact same thing for client project

<a id="documentation-csharp-binding-users-guide--generated-files"></a>

# Generated Files

Once the etch file has been compiled successfully, either from command line or Visual Studio Plugin, a bunch of files are generated.

This section briefly explains the purpose of each generated file.

<a id="documentation-csharp-binding-users-guide--interface-files"></a>

### Interface Files

Example.cs
ExampleClient.cs
ExampleServer.cs

These three files are the generated interface classes. Service defined constants and types are in Example.cs, as well as direction "both" messages, which are messages which are shared between client and server. ExampleClient.cs and ExampleServer.cs are respectively the messages for just the direction client or server. These Files should not be edited by the user

<a id="documentation-csharp-binding-users-guide--remote-files"></a>

### Remote Files

RemoteExample.cs
RemoteExampleClient.cs
RemoteExampleServer.cs

RemoteExample\*.cs are the generated classes which implement the interfaces, with message implementations which encode the message type and arguments for transport to the connection peer and then receive and decode any response. These files should not be edited by the user either

<a id="documentation-csharp-binding-users-guide--stub-files"></a>

### Stub Files

StubExample.cs
StubExampleServer.cs
StubExampleClient.cs

StubExample\*.cs are the generated classes which receive messages encoded by RemoteExample\*.cs and decode them, calling the appropriate message implementation and then encoding and sending any result. These Files are also not edited by the user

<a id="documentation-csharp-binding-users-guide--value-factory-file"></a>

### Value Factory File

ValueFactoryExample.cs

ValueFactoryExample.cs is a generated class which contains helper code to serialize service defined types and also the meta data which describes the messages and fields, field types, timeouts, etc. This file is also not edited by the user

<a id="documentation-csharp-binding-users-guide--base-files"></a>

### Base Files

BaseExample.cs
BaseExampleClient.cs
BaseExampleServer.cs

BaseExample\*.cs are generated classes which implement the interfaces, with message implementations which call the delegate. If no delegate is defined i.e. if delegate is null, an UnsupportedOperationException is thrown. These files are also not edited by the user

<a id="documentation-csharp-binding-users-guide--impl-files"></a>

### Impl Files

ImplExampleClient.cs
ImplExampleServer.cs

ImplExample\*.cs are the generated sample client and server implementation classes. They extend the generated base classes. These are used by the sample main programs to provide implementations of the client or server messages. Edit these files as you wish to implement your service (overriding the default implementations from the generated base classes or uisng delegates).

<a id="documentation-csharp-binding-users-guide--helper-file"></a>

### Helper File

ExampleHelper.cs

ExampleHelper.cs is a generated class which includes static methods to help construct transports for client and listener. This file should not be edited by the user

<a id="documentation-csharp-binding-users-guide--main-files"></a>

### Main Files

MainExampleClient.cs
MainExampleListener.cs

MainExample\*.cs are the generated sample client and server main programs. They show how to setup a transport and start it and how to create a session. Edit these files as you wish to implement your service, or just copy the code into your own application.

<a id="documentation-csharp-binding-users-guide--changes-required-to-make-the-application-work"></a>

# Changes Required to Make the Application Work

Only a few files need to be edited to make the etch application run.

<a id="documentation-csharp-binding-users-guide--mainexamplelistener"></a>

## MainExampleListener

As mentioned in the previous section, MainExampleListener is the class where the listener (server) is started. The user needs to edit the URI to point to the location where listener must listen for connection from the client

```
string uri = "tcp://localhost:4002";
```

In the above code snippet, the listener will run at port 4002 on localhost.

When the listener accepts a connection from the client, an server object (ImplExampleServer) is created to service the client request. The code to create the Impl object is auto generated by the compiler.

```
public ExampleServer NewExampleServer( RemoteExampleClient client )
{
     return new ImplExampleServer( client );
}
```

If a user wishes to, he can pass more parameters to the Impl Object. In the context of our example, we do not need to pass any other arguments, thus we will keep the generated code as is.

In summary, editing the uri is the only change required for our example.

<a id="documentation-csharp-binding-users-guide--implexampleserver"></a>

## ImplExampleServer

In this class, we will provide implementation of any "both" or "server" directed messages. To get a better understanding of what is meant by "both" and "server" directed message, lets look at snippet of Example.etch

```
        @Timeout( 3456 )
	@Direction( Both )
	int hello( string msg )

	@Oneway
	@Direction( Server )
	void howdyServer( string msg )

        @Oneway
	@Direction( Client )
	void howdyClient( string msg )
```

The keyword @Direction(....) is used to specify the direction of the message. @Direction(server) implies that the message is headed towards the server. Both implies that the message can be directed towards the server or client. For more details please refer to the Etch Language Reference Manual.

For our purpose, in ImplExampleServer we will only implement the messages that are directed towards server "@Direction(Server)" or both "@Direction(Both)"

ImplExampleServer extends from BaseExampleServer which provides a default implementation of all messages with direction server or both. Below is a snippet of BaseExampleServer

```
........./// <summary> /// Delegate Definition; Please do not modify /// </summary>
public delegate int? _delegate_type_helloServer	(string msg, System.DateTime? d);
/// <summary> /// Add your implementation method to this variable /// </summary>
public _delegate_type_helloServer  _delegate_helloServer;
public virtual int? helloServer (string msg, System.DateTime? d) {
if (_delegate_helloServer != null) return _delegate_helloServer(msg,d); else throw new NotSupportedException( "helloServer" );} .........
```

In ImplExampleServer we can either override method helloServer or use the power of delegate (see example below for how to use delegate)

```
public ImplExampleServer(RemoteExampleClient client) {this.client = client; _delegate_helloServer = SayHello;}
/// <summary>A connection to the client session. Use this to /// send a message to the client.</summary> private readonly RemoteExampleClient client;
public int? SayHello(string msg, DateTime? d) {Console.WriteLine("Msg is {0} and date is {1}", msg,d); return 0;}
```

Notice that method SayHello is assigned to delegate \_delegate\_helloServer in the constructor.

In summary, ImplExampleServer is where the actual server implementation resides. The user can choose to either override the methods in BaseExampleServer or assign methods to delegates.

<a id="documentation-csharp-binding-users-guide--mainexampleclient"></a>

## MainExampleClient

The uri in MainExampleClient needs to be modified such that it points to location where listener was started. In the context of our example the uri will point to the following

```
string uri = "tcp://localhost:4002";
```

The compiler generates code to setup up the transport layer. It also gets an instance of RemoteExampleServer. The client uses RemoteExampleServer to send messages to server.
In the context of our example, we will call method helloServer on RemoteExampleServer. Following is a code snippet

```
public static void Main(String[] args)
{

    string uri = "tcp://localhost:4002";

    RemoteExampleServer server = ExampleHelper.NewServer( uri, null, new MainExampleClient());

   // Connect to the service
   server._StartAndWaitUp( 4000 );

   server.helloServer("Hi !!!", DateTime.Now);

   // Disconnect from the service
   server._StopAndWaitDown( 4000 );

}
```

Thus a user only needs to change the uri and use the RemoteExampleServer instance to invoke messages on the server

<a id="documentation-csharp-binding-users-guide--implexampleclient"></a>

## ImplExampleClient

MainExampleClient also contains method NewExampleClient, which creates an ImplExampleClient object. This class provides implementation of "both" directed and "client" directed messages. This class is analogous to the ImplExampleServer. The only difference being that ImplExampleServer implemented "server" and "both" directed messages, while ImplExampleClient implements "client" and "both" directed messages.

To see ImplExampleClient at work, we will have to modify ImlExampleServer as well. In ImplExampleServer section, we provided implementation of helloServer method using delegates, lets tweak this a little such that the server replies back client with a howdyClient message.

```
public ImplExampleServer(RemoteExampleClient client) {this.client = client; _delegate_helloServer = SayHello;}
/// <summary>A connection to the client session. Use this to /// send a message to the client.</summary> private readonly RemoteExampleClient client;
public override int? helloServer(string msg, DateTime? d) {Console.WriteLine("Msg is {0} and date is {1} ", msg, d); client.howdyClient("Hi Client"); return 0;}
```

It is very important to remember that howdyClient is defined as a @oneway message in the Example etch file. Such messages don't wait for a response. They are often referred to as event or "fire and forget" message. If howdyClient was not defined as @oneway, it would have resulted in a deadlock or a timeout exception. This is because client would expect to hear back from helloServer message, while server would be waiting to hear back from howdyClient. Since neither can respond until they hear from the other, they will eventually timeout if a timeout has been defined or just wait indefinitely. However since howdyClient message has been defined as @oneway the server does not have to wait for a response from the client.

In summary, ImplExampleClient is the place where the client implementation resides. The user can chose to override the base implementation provided in BaseExampleClient or assign methods to delegates.

<a id="documentation-csharp-binding-users-guide--compile-and-run-the-application"></a>

# Compile and Run the Application

<a id="documentation-csharp-binding-users-guide--using-csc"></a>

## Using CSC

Please make sure that .NET 2.0 or greater is installed on your system

Building on our example, lets first compile the server files.

- The first step would be to change directory to the server location
  (c:\EtchExamples\Example\server\etch.examples.example).

- The next step would be to copy Etch.dll from Etch Home Directory to the server directory.

- Once the file is copied, use csc to compile the \*.cs file.

```

copy "%ETCH_HOME%\lib\Etch.dll" .

csc "/reference:%ETCH_HOME%\lib\Etch.dll" /main:etch.examples.example.MainExampleListener *.cs
```

If there are no compile errors MainExampleListener.exe is created. Use the exe file to run the listener.

For the client files, cd to the client directory and follow the same instructions as mentioned above. In csc command replace etch.examples.example.MainExampleListener with
etch.examples.example.MainExampleClient

use MainExampleClient.exe to run the client.

<a id="documentation-csharp-binding-users-guide--using-visual-studio"></a>

## Using Visual Studio

- Please make sure you have followed the steps mentioned in section "Visual Studio Plugin".

- Add %ETCH\_HOME%\lib\Etch.dll as a reference to both client and server project

- Build solution by either right clicking on solution and choosing Rebuild Solution or by using keyborad shortcut (CTRL+SHIFT+B).

To Run the Application

- Right click on the server project and chose "Set as Startup Project".

- Press CTRL+F5 to run the listener or server.

- Follow the above two steps to run client as well.

---

<a id="documentation-documentation"></a>

<!-- source_url: https://etch.apache.org/documentation/documentation.html -->

<!-- page_index: 19 -->

<a id="documentation-documentation--getting-started"></a>

#### Getting Started

[Overview](#documentation-overview "Overview") - What is Etch and why should I care
[Architecture](#documentation-architecture "Architecture") - Architecture summary
[User Setup Guide](#documentation-setup-guide-for-users "Setup Guide for Users") - installing Etch and using it
[Examples](#documentation-examples "Examples") - example applications and services using Etch

<a id="documentation-documentation--reference"></a>

#### Reference

[Language Reference](#documentation-language-reference "Language Reference") - Etch IDL reference
[Etch Binary Protocol](#documentation-etch-binary-protocol "Etch Binary Protocol") - Etch serialization format
[Compiler Users Guide](#documentation-compiler-users-guide "Compiler Users Guide") - Etch compiler command-line options
[Generated Code Users Guide](#documentation-generated-code-users-guide "Generated Code Users Guide") - Navigating generated code

<a id="documentation-documentation--advanced-topics"></a>

#### Advanced Topics

[TLS](#documentation-howto-tls "Howto - TLS") - Using TLS with Etch
[KeepAlive Filter](#documentation-howto-keepalive-filter "Howto - KeepAlive Filter") - Setting up keep-alive's for connections
[Pwauth Filter](#documentation-howto-pwauth-filter "Howto - Pwauth Filter") - Setting up connection authorizations
[Logger Filter](#documentation-howto-logger-filter "Howto - Logger Filter") - Setting up logging

---

<a id="documentation-etch-binary-protocol"></a>

<!-- source_url: https://etch.apache.org/documentation/etch-binary-protocol.html -->

<!-- page_index: 20 -->

<a id="documentation-etch-binary-protocol--example-nsdl"></a>

## Example NSDL

The Etch binary protocol is illustrated using the following example NSDL:

```

module org.apache.etch.example.binary
 
service binaryExample {
    struct A ( int c )
    int f(A[] as)
}
```

<a id="documentation-etch-binary-protocol--hashed-values"></a>

## Hashed Values

Etch uses hashed values to identify names (such as names of parameters or functions). The values are computed by hashing the full qualified names of the elements. As an example, the computed hash values for the example above are:

```

org.apache.etch.example.binary.binaryExample.f = 0x28e34aa1
org.apache.etch.example.binary.binaryExample._result_f = 0x0972201e
org.apache.etch.example.binary.binaryExample.A = 0x28e34a7c
c = 0x150a2c9e
as = 0x5a1cfad7
_messageId = 0x6306b468
_inReplyTo = 0xeda8c9a6
```

<a id="documentation-etch-binary-protocol--example-code"></a>

## Example Code

Consider the following Java program for the NSDL Idl:

```

binaryExample.A a1 = new binaryExample.A(1);
binaryExample.A a2 = new binaryExample.A(2);
binaryExample.A[] as = {a1, a2};
Integer res = server.f(as);
```

<a id="documentation-etch-binary-protocol--request-message:"></a>

## Request Message:

The request message for the call server.f(as) in the program above will be:

```

0xde,0xad,0xbe,0xef,0x0,0x0,0x0,0x41,0x3,0x86,0x28,0xe3,0x4a,0xa1,0x2,0x86,0x63,0x6,0xb4,0x68,0x87,0x0,0x0,0x1,0x2b,0x1f,0x33,0x1c,0x6b,0x86,0x5a,0x1c,0xfa,0xd7,0x91,0x95,0x86,0x28,0xe3,0x4a,0x7c,0x1,0x2,0x95,0x86,0x28,0xe3,0x4a,0x7c,0x1,0x86,0x15,0xa,0x2c,0x9e,0x1,0x81,0x95,0x86,0x28,0xe3,0x4a,0x7c,0x1,0x86,0x15,0xa,0x2c,0x9e,0x2,0x81,0x81,0x81
```

Lets explain this in detail:

```

 HEADER_______________________________________________________________________________________________ 
 0xde 0xad 0xbe 0xef                    etch identifier
 0x00 0x00 0x00 0x41                    etch message length (0x41 bytes)
 0x03                                   etch protocol version
 CALL of f____________________________________________________________________________________________ 
 0x86                                   type flag: INT
 0x28 0xe3 0x4a 0xa1                    INT value: hash for name of message: Call of F
 0x02                                   size of parameters (1 param for f + message ID)
 Message ID___________________________________________________________________________________________ 
 0x86                                   type flag: INT
 0x63 0x06 0xb4 0x68                    INT value: hash for "_messageId"
 0x87                                   type flag LONG
 0x0 0x0 0x1 0x2b 0x1f 0x33 0x1c 0x6b   LONG value: MessageID (unique for this call)
 param of call (array as)_____________________________________________________________________________
        0x86                                    type flag: INT
        0x5a 0x1c 0xfa 0xd7                     INT value: hash for "as"
        0x91                                    type flag: ARRAY
        type of array_________________________________________________________________________________
        0x95                                    type flag: (type of array elems) CUSTOM 
        0x86                                    type flag: INT
        0x28 0xe3 0x4a 0x7c                     INT value: hash for "A" (super type of all array elems)
        0x01                                    INT value: dimension of array
        0x02                                    INT value: number of array elements
        first array element___________________________________________________________________________
        0x95                                    type flag: CUSTOM
        0x86                                    type flag: INT
        0x28 0xe3 0x4a 0x7c                     INT value: hash for "A" (type of elem)
        0x1                                     INT value: number of fields of A (only one: c)
               field values of first array element____________________________________________________
                0x86                                    type flag: INT
                0x15 0x0a 0x2c 0x9e                     INT value: hash for "c" (name of A's field)
                0x01                                    INT value: value of A.c
        0x81                                    NONE value: end delimiter for struct A
        second array element__________________________________________________________________________
        0x95                                    type flag: CUSTOM
        0x86                                    type flag: INT
        0x28 0xe3 0x4a 0x7c                     INT value: hash for "A" (type of elem)
        0x1                                     INT value: number of fields of A (only one: c)
               field values of second array element____________________________________________________
               0x86                                     type flag: INT
               0x15 0xa 0x2c 0x9e                       INT value: hash for "c" (name of A's field)
                0x2                                     INT value: value of A.c
        0x81                                    NONE value: end delimiter for struct A
        0x81                                    NONE value: end delimiter for param array
        0x81                                    NONE value: end delimiter for call of f
```

<a id="documentation-etch-binary-protocol--return-message:"></a>

## Return Message:

The return message will be serialized just like that, but additionally contains a "\_inReplyTo" ID. This ID is the \_messageID value of the request message. This enables Etch to find the right caller for this response. Of course the message is much simpler, since it only contains a single integer return value, \_inReplyTo and \_messageID

<a id="documentation-etch-binary-protocol--implementation"></a>

## Implementation

The [BinaryTaggedDataOutput](https://svn.apache.org/repos/asf/etch/trunk/binding-java/runtime/src/main/java/org/apache/etch/bindings/java/transport/fmt/binary/BinaryTaggedDataOutput.java) class implements the serialization in Etch. It's code is pretty good to understand and is - at the moment - the availble specification for the whole protocol. Start with the writeMessage function.

<a id="documentation-etch-binary-protocol--type-codes:"></a>

## Type Codes:

Here are all current type codes, which Etch uses:

```

	ANY = 0x96
	CUSTOM = 0x95
	STRING = 0x93
	EMPTY_STRING = 0x92
	ARRAY = 0x91
	DOUBLES = 0x90
	BYTES = 0x8b
	DOUBLE = 0x89
	FLOAT = 0x88
	LONG = 0x87
	INT = 0x86
	SHORT = 0x85
	BYTE = 0x84
	NULL = 0x80
	NONE = 0x81
	BOOLEAN_FALSE = 0x82
	BOOLEAN_TRUE = 0x83
```

Optimization:
Any Integer value between

```

	MAX_TINY_INT = 0x7f = 127
	MIN_TINY_INT = 0xc0 = -64
```

will be serialized directly without specifying an own type flag. Bigger or smaller Integer Values will have their own type flag before the value.

---

<a id="documentation-example-hello-world"></a>

<!-- source_url: https://etch.apache.org/documentation/example-hello-world.html -->

<!-- page_index: 21 -->

<a id="documentation-example-hello-world--hello-etch"></a>

## Hello Etch

The classic helloworld example in Etch is provided in examples/helloworld (both svn and releases, starting with 1.1).

You will find the following directory structure:

- build.xml
- README.txt
- src
  - main
    - csharp (csharp implementation)
    - java (java implementation)
    - c (c implementation)
    - etch
      - HelloWorld.etch (NSDL service description)
  - target (created on build, contains generated parts)

You can build the HelloWorld example (generate source from HelloWorld.etch, compile and test) for Java and CSharp on the command line using

```

cd examples/helloworld
ant Debug
```

Note that you must setup your command line environment correctly. If you have checked out the trunk from svn, use scripts/antSetup.bat and the information in [Building Trunk](https://etch.apache.org/documentation/building-trunk.html "Building Trunk").

<a id="documentation-example-hello-world--helloworld-nsdl"></a>

## HelloWorld NSDL

```
module org.apache.etch.examples.helloworld
service HelloWorld {struct user (int id,string name)
exception UserUnknownException (string mes)
@Direction(Server) string say_hello(user to_whom) throws UserUnknownException
}
```

The service provides the say\_hello method, which should greet a user, which is supplied as a parameter.

<a id="documentation-example-hello-world--java-helloworld-in-more-detail"></a>

## Java HelloWorld in more detail

The implementation of the example server and client is located in:

trunk\examples\helloworld\src\main\java\org\apache\etch\examples\helloworld\

The classes MainHelloWorldListener and MainHelloWorldClient spawn the server and client parts of the helloworld example.

The Client code is:

```

String uri = "tcp://127.0.0.1:4001";
RemoteHelloWorldServer server = HelloWorldHelper.newServer( uri, null,new MainHelloWorldClient() );
server._startAndWaitUp( 4000 );
user u = new user(5, "Testuser");
System.out.println(server.say_hello(u));
server._stopAndWaitDown( 4000 );
```

It connects to an Etch server running on localhost by constructing a new RemoteHelloWorldServer object (the proxy in the rpc sense) using the HelloWorldHelper class, which is generated from the NSDL. Afterwards the connection is started and the say\_hello method is called.

Starting a server is also quite simple:

```

String uri = "tcp://127.0.0.1:4001";
ServerFactory listener = HelloWorldHelper.newListener( uri, null, new MainHelloWorldListener() );
listener.transportControl( Transport.START_AND_WAIT_UP, 4000 );
```

The last parameter of newListener must implement the HelloWorldServerFactory interface, which defines the newHelloWorldServer factory method. This method is called by the etch runtime once for every client connect and must return an instance of ImplHelloWorldServer, which is the implementation class for the services that are invoked for that specific connected client. In the code for the client above you can see the same principle for the client. This already shows Etch's basic principle of two-way communication: The Client has an Impl... object, too. It contains all @Direction(client) methods from the IDL (in this small example, there are none. see the chat example for client-side methods.)

---

<a id="documentation-examples"></a>

<!-- source_url: https://etch.apache.org/documentation/examples.html -->

<!-- page_index: 22 -->

<a id="documentation-examples--application-examples"></a>

## Application Examples

- [Hello World](#documentation-example-hello-world "Example - Hello World")
- [2008 Developer Conference Video](http://developer.cisco.com/web/cuae/devconf2008_session_3) - video from the 2008 Cisco Unified Application Environment Developer's conference where Etch was introduced.

---

<a id="documentation-generated-code-users-guide"></a>

<!-- source_url: https://etch.apache.org/documentation/generated-code-users-guide.html -->

<!-- page_index: 23 -->

<a id="documentation-generated-code-users-guide--c-sharp-binding-user-guide"></a>

## C Sharp Binding User Guide

Best documentation for generated code is available for the C# Binding:

- [Csharp Binding Users Guide](#documentation-csharp-binding-users-guide "Csharp Binding Users Guide")

<a id="documentation-generated-code-users-guide--java-user-guide"></a>

## Java User Guide

The generated Java Binding code follows the same structure as the C# binding. We will provide more detailed documentation on those bindings in the future. Reading the Csharp Compiler User Guide should also help with understanding the generated java code.

<a id="documentation-generated-code-users-guide--c-binding-user-guide"></a>

## C Binding User Guide

- [C Binding Tips & Tricks](#documentation-c-binding-tips-tricks "C Binding Tips & Tricks")

<a id="documentation-generated-code-users-guide--javascript-binding-in-development"></a>

## JavaScript Binding (in development)

- [Javascript Language Binding](#documentation-javascript-language-binding "Javascript Language Binding")

---

<a id="documentation-howto-keepalive-filter"></a>

<!-- source_url: https://etch.apache.org/documentation/howto-keepalive-filter.html -->

<!-- page_index: 24 -->

# KeepAlive Filter

- 1 [KeepAlive Filter](#documentation-howto-keepalive-filter--howto-keepalivefilter-keepalivefilter)

- 1.1 [KeepAlive Operation](#documentation-howto-keepalive-filter--howto-keepalivefilter-keepaliveoperation)
- 1.2 [KeepAlive Parameters](#documentation-howto-keepalive-filter--howto-keepalivefilter-keepaliveparameters)
- 1.3 [KeepAlive SessionNotify](#documentation-howto-keepalive-filter--howto-keepalivefilter-keepalivesessionnotify)
- 1.4 [KeepAlive Examples](#documentation-howto-keepalive-filter--howto-keepalivefilter-keepaliveexamples)
- 1.5 [KeepAlive Issues](#documentation-howto-keepalive-filter--howto-keepalivefilter-keepaliveissues)

<a id="documentation-howto-keepalive-filter--keepalive-filter"></a>

# KeepAlive Filter

The etch KeepAlive filter is a message filter which periodically checks the health of a connection and resets it if it not responsive. The filter must be added to both sides of the connection to be effective.

<a id="documentation-howto-keepalive-filter--keepalive-operation"></a>

## KeepAlive Operation

The client periodically sends a request message to the server. The server responds by sending a response message to the client.

Both client and server periodically check to see how long it has been since the last KeepAlive message was received from the other side. If the time since the last KeepAlive message was received is too great, the connection is reset.

<a id="documentation-howto-keepalive-filter--keepalive-parameters"></a>

## KeepAlive Parameters

There are two parameters which control KeepAlive:

- KeepAlive.delay - the number of seconds between sends (client) and checks (client and server). Value is number of seconds. The default value is 15 seconds.
- KeepAlive.count - the number of delay intervals without a message before the connection is reset. Value is number of delay intervals. The default value is 4.

The server adopts the settings (per connection) of the client.

<a id="documentation-howto-keepalive-filter--keepalive-sessionnotify"></a>

## KeepAlive SessionNotify

When KeepAlive decides to reset a connection, it also notifies the session with an event:

```
"KeepAlive resetting dead connection"
```

<a id="documentation-howto-keepalive-filter--keepalive-examples"></a>

## KeepAlive Examples

Start KeepAlive with default parameters.

```
tcp://localhost:4001?filter=KeepAlive
```

Start KeepAlive with a delay of 60 seconds and a count of 5.

```
tcp://localhost:4001?filter=KeepAlive&KeepAlive.delay=60&KeepAlive.count=5
```

<a id="documentation-howto-keepalive-filter--keepalive-issues"></a>

## KeepAlive Issues

A few issues with KeepAlive come to mind:

- Client specified parameters override server. Seemed like a good idea at the time. On reflection I think the server settings ought to rule. Centralized management, etc.
- If a really long running operation is holding up the message receiver thread then the connection will be declared dead and reset. Not necessarily a bad thing, just something to note.
- Server is passive and only sends a message to client when it receives a message from client. Again, not exactly an issue, just something to note.

---

<a id="documentation-howto-logger-filter"></a>

<!-- source_url: https://etch.apache.org/documentation/howto-logger-filter.html -->

<!-- page_index: 25 -->

<a id="documentation-howto-logger-filter--logger-filter"></a>

# Logger Filter

The purpose of this document is to provide an overview on how to setup Logger Filter in Etch. As the name suggests, Logger filter logs etch messages and events into a file.
Logger Filter can be enabled for Client, Listener or both.

<a id="documentation-howto-logger-filter--logger-filter-parameters"></a>

## Logger Filter Parameters

Logger.filePath - This parameter is used to define the location and name of the logFile. For example Logger.filePath=C:\test\log\server.txt, in this case etch messages and
events will be logged to file C:\test\log\server.txt. If a user then does define this parameter, then etch will use a default file for logging (Log.txt)

<a id="documentation-howto-logger-filter--how-to-enable-logger-filter"></a>

## How to enable Logger Filter

Change uri to one of the following

- string uri ="tcp://localhost:4006?filter=Logger&Logger.filePath=C:\test\log\server.txt";

Logs will be written to C:\test\log\server.txt

- string uri = "tcp://localhost:4006?filter=Logger

In this case, logs will be written to default file Log.txt

<a id="documentation-howto-logger-filter--snippet-of-log-file"></a>

## Snippet of Log File

```
16:11:49.593: Incoming: Messagizer : Packetizer / TcpConnection(up, 127.0.0.1:4006, 127.0.0.1:3161)
16:11:49.609: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 0, _messageId(1661383784)=633512167095000000}
16:11:49.609: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000000, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 1, _messageId(1661383784)=633512167095000037}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000037, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 2, _messageId(1661383784)=633512167095000074}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000074, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 3, _messageId(1661383784)=633512167095000111}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000111, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 4, _messageId(1661383784)=633512167095000148}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000148, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 5, _messageId(1661383784)=633512167095000185}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000185, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 6, _messageId(1661383784)=633512167095000222}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000222, result(-2130379326)=0}
16:11:49.625: Incoming: etch.examples.example.Example.hello(-1567573670): {msg(769750364)=I am printing message 7, _messageId(1661383784)=633512167095000259}
16:11:49.625: Outgoing: etch.examples.example.Example._result_hello(92919767): {_inReplyTo(-307705434)=633512167095000259, result(-2130379326)=0}
```

<a id="documentation-howto-logger-filter--issues"></a>

## Issues

- **How to prevent overwriting of log file ?**

The current solution is to rename the older log file. The name of the file will be based on the current time. Image below depicts the name format of the older log files

![](assets/images/filerename_37ce0d47730912af.JPG)

- **When to flush the contents of the buffer to file ?**

Option 1 is to flush the contents immediately (may lead to a performance hit)
Option 2 is to do it periodically (user will be given the flexibility to chose the time interval for e.g. user can specify flush buffer every 2 minutes)
Option 3 is not to flush the buffer at all

Currently only Option 1 has been implemented.

- **Should we set a limit on the file size ? In other words, how large should we allow a log file to get before we create a new log file ?**

- **At some point, should very old log files be deleted ?**

---

<a id="documentation-howto-pwauth-filter"></a>

<!-- source_url: https://etch.apache.org/documentation/howto-pwauth-filter.html -->

<!-- page_index: 26 -->

# PwAuth Filter

- 1 [PwAuth Filter](#documentation-howto-pwauth-filter--howto-pwauthfilter-pwauthfilter)

- 1.1 [PwAuth Parameters](#documentation-howto-pwauth-filter--howto-pwauthfilter-pwauthparameters)
- 1.2 [How to enable PwAuth Filter](#documentation-howto-pwauth-filter--howto-pwauthfilter-howtoenablepwauthfilter)
- 1.3 [How it works](#documentation-howto-pwauth-filter--howto-pwauthfilter-howitworks)

<a id="documentation-howto-pwauth-filter--pwauth-filter"></a>

# PwAuth Filter

The purpose of this document is to provide an overview of the PwAuth Filter. PwAuth is a message filter which watches for Session.UP and attempts to
authenticate the user by sending a message to the server with the name and password in it. If the server responds, the session is notified with the
user name. If the server responds negatively, the session is notified of the failure (using a PwAuthFail event). A transport control may also be sent to
force a login or logout or to set the name or password. The name and password are initialized from the uri, or prompted for if not specified.

<a id="documentation-howto-pwauth-filter--pwauth-parameters"></a>

## PwAuth Parameters

PwAuth.user - Specify the user name on the uri
PwAuth.password - Specify the password on the uri

<a id="documentation-howto-pwauth-filter--how-to-enable-pwauth-filter"></a>

## How to enable PwAuth Filter

In Listener, change the uri to enable PWAuth Filter

```
String uri = "tcp://0.0.0.0:4008?filter=PwAuth"
```

In client, change the uri to

```
String uri = "tcp://fred:1234@localhost:4008?filter=PwAuth";

where fred is the username
and 1234 is the password
```

<a id="documentation-howto-pwauth-filter--how-it-works"></a>

## How it works

When the session is UP, the client send a PwAuth request to the server. If username/password has not been set on the uri, the PWAuth
will send a session query to the client, asking for username/password.

On the server side, PWAuth filter intercepts the request, gets the username/password from the request, package them in a UserPassword Object and sends a
session query to the server. In the Server Impl, the logic to authenticate the user can be placed. The return object is OkStatus

```
public Object _sessionQuery( Object query ) throws Exception {if (query instanceof UserPassword) {OkStatus status = null; UserPassword up = (UserPassword) query; if (up.user.equals( "fred" ) && up.password.equals( "1234" )) {status = new OkStatus( true, "" ); System.out.println( " Authentication Passed" );} else {status = new OkStatus( false, "Authentication failed" ); System.out.println( " Authentication Failed" );} return status;}
throw new UnsupportedOperationException( "unknown query: " + query );}
```

---

<a id="documentation-howto-tls"></a>

<!-- source_url: https://etch.apache.org/documentation/howto-tls.html -->

<!-- page_index: 27 -->

# TLS in Etch

- 1 [TLS in Etch](#documentation-howto-tls--howto-tls-tlsinetch)

- 1.1 [Certificate Management](#documentation-howto-tls--howto-tls-certificatemanagement)
- 1.2 [Changes to the Listener](#documentation-howto-tls--howto-tls-changestothelistener)
- 1.3 [Changes to Client](#documentation-howto-tls--howto-tls-changestoclient)

<a id="documentation-howto-tls--tls-in-etch"></a>

# TLS in Etch

The purpose of this document is to provide a step by step description on how to enable SSL in etch

<a id="documentation-howto-tls--certificate-management"></a>

## Certificate Management

Certificates are required to enable encryption of data, maintaining its integrity and optionally providing authentication.

<a id="documentation-howto-tls--certificate-management-for-java-server-and-java-client"></a>

### Certificate Management for Java Server and Java Client

<a id="documentation-howto-tls--creating-server-certificate-using-keytool-java"></a>

#### Creating Server Certificate using KeyTool (Java)

(Before running keytool make sure java is installed on your machine and is defined in PATH enviorment variable)

This certificate will be used on the machine where the listener is running.

**keytool -genkey -alias myalias -validity 365 -keystore keys/my.keystore**

Enter keystore password: abc123
What is your first and last name?
Unknown: Etch
What is the name of your organizational unit?
Unknown: CUAE
What is the name of your organization?
Unknown: Cisco
What is the name of your City or Locality?
Unknown: Austin
What is the name of your State or Province?
Unknown: TX
What is the two-letter country code for this unit?
Unknown: US
Is CN=Etch, OU=CUAE, O=Cisco, L=Austin, ST=TX, C=US correct?
y

Enter key password for <myalias>
(RETURN if same as keystore password):

It is preferable that you type in the same password for myalias as you did for keystore.
-keystore option allows you to specify the keystore you want to use. In the above example my.keystore is created in the (current directory)/keys

<a id="documentation-howto-tls--importing-the-certificate-into-a-client-machine-java"></a>

#### Importing the Certificate into a Client Machine (Java)

This section is only required if you want to authenticate the server. If authenticate is not required, please skip this section

In the last section we created a certificate for the machine running the listener. Now the certificate has to be imported into the client machine

First export the certificate created in previous section to a file

**keytool -export -keystore keys/my.keystore -alias myalias -file server.cer**

Now copy this certificate to your client machine and import it to a truststore

**keytool -import -keystore jssecacerts -alias myalias -file server.cer**

-keystore in this context is the truststore

<a id="documentation-howto-tls--certificate-management-for-c-server-and-c-client"></a>

### Certificate Management for C# Server and C# Client

<a id="documentation-howto-tls--creating-a-server-certificate-using-makecert-c"></a>

#### Creating a server certificate using makecert (C#)

This certificate will be used on the machine where the listener is running.

\*makecert -pe -n "CN=Test And Dev Root Authority" -ss my -sr LocalMachine -a sha1 -sky signature -r "Test And Dev Root Authority.cer"\*

![](https://cwiki.apache.org/confluence/images/icons/emoticons/check.gif)

**Handy Hint** You are not required to install Visual Studio on to the CUAE server to get the makecert executable. You should be able to copy the file from a client that has Visual Studio installed and place it on the CUAE server to run the command above. The file can be found in the folloowing directory for a Visual Studio install:
C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\Bin\makecert

The above command creates a Root certificate. All your personal certificates will extend from this root certificate. So lets create a personal certificate now.
**makecert -pe -n "CN=gsandhir-wxp02" -ss my -sr LocalMachine -a sha1 -sky exchange -in "Test And Dev Root Authority" -is my -ir LocalMachine -sp "Microsoft RSA SChannel Cryptographic Provider" -sy 12 gsandhir-wxp02.cer**

If you run up a Certificates MMC at this point, you will be able to see this. However, by default, the Certificates snap-in isn't available as a short cut. Hence, use the following steps:

- start/run/mmc
- File/Add-Remove Snap-In
- Click Add
- Select Certificates and click Add
- Select Computer Account and hit Next
- Select Local Computer
- Click Finish
- Click Close
- Click OK

If you expand the console out to Personal/Certificates, you will see your newly created certificates.

In the certificates snap-in, right-click the "Test and Dev Root Authority" certificate and copy it to the "Trusted Root Certification Authorities" node. Once done, if you expand this node, and then select certificates your newly created root cert should be present.

<a id="documentation-howto-tls--importing-the-certificate-created-using-makecert-into-a-client-machine-c"></a>

#### Importing the Certificate created using makecert into a Client Machine (C#)

This section is only required if you want to authenticate the server. If authentication is not required, please skip this section

First thing we need to do is export the certificate made in the previous step into a file

Run MMC

- Add the Certificate snap-in as described in the previous section
- Expand Trusted Root Certification Authorities\Certificates and select the Test And Dev Root Authority we created in the last section
- Right click on the certificate and select All Tasks->Export
- Certificate Export wizard will be launched. Click next
- Make sure you select "No, do not export the private key".
- Keep the default for the Export File Format (DER encoded binary X509)
- Type in any file name and click finish

Now we will copy this file into the client machine and then import it into that machine's certificate store

- Run MMC
- Add the Certificate snap-in as described in the previous section
- Select Certificates under Trusted Root Certification Authorities and right click on it and chose All Tasks->Import
- Specify the file name as the certificate we copied from server.
- Chose all the default options and click finish

<a id="documentation-howto-tls--certificate-management-for-c-server-and-java-client"></a>

### Certificate Management for C# Server and Java Client

<a id="documentation-howto-tls--creating-a-server-certificate-using-makecert-c-2"></a>

#### Creating a server certificate using makecert (C#)

This certificate will be used on the machine where the listener is running.

\*makecert -pe -n "CN=TestRoot" -ss my -sr LocalMachine -a sha1 -sky signature -r "TestRoot.cer"\*

![](https://cwiki.apache.org/confluence/images/icons/emoticons/check.gif)

**Handy Hint** You are not required to install Visual Studio on to the CUAE server to get the makecert executable. You should be able to copy the file from a client that has Visual Studio installed and place it on the CUAE server to run the command above. The file can be found in the folloowing directory for a Visual Studio install:
C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\Bin\makecert

The above command creates a Root certificate. All your personal certificates will extend from this root certificate. So lets create a personal certificate now.
**makecert -pe -n "CN=Test" -ss my -sr LocalMachine -a sha1 -sky exchange -in "TestRoot" -is my -ir LocalMachine -sp "Microsoft RSA SChannel Cryptographic Provider" -sy 12 Test.cer**

If you run up a Certificates MMC at this point, you will be able to see this. However, by default, the Certificates snap-in isn't available as a short cut. Hence, use the following steps:

- start/run/mmc
- File/Add-Remove Snap-In
- Click Add
- Select Certificates and click Add
- Select Computer Account and hit Next
- Select Local Computer
- Click Finish
- Click Close
- Click OK

If you expand the console out to Personal/Certificates, you will see your newly created certificates.

In the certificates snap-in, right-click the "TestRoot" certificate and copy it to the "Trusted Root Certification Authorities" node. Once done, if you expand this node, and then select certificates your newly created root cert should be present.

<a id="documentation-howto-tls--importing-the-certificate-to-java-client"></a>

#### Importing the certificate to Java Client

This section is only required if you want to authenticate the server. If authentication is not required, please skip this section

First thing we need to do is export the certificate made in the previous step into a file

Run MMC

- Add the Certificate snap-in as described in the previous section
- Expand Trusted Root Certification Authorities\Certificates and select the TestRoot certificate we created in the last section
- Right click on the certificate and select All Tasks->Export
- Certificate Export wizard will be launched. Click next
- Make sure you select "No, do not export the private key".
- Keep the default for the Export File Format (DER encoded binary X509)
- Type in any file name and click finish (for example server.cer)

Now copy this certificate to your client machine and import it to a truststore

**keytool -import -keystore jssecacerts -alias myalias -file server.cer**

-keystore in this context is the truststore

<a id="documentation-howto-tls--changes-to-the-listener"></a>

## Changes to the Listener

<a id="documentation-howto-tls--java-listener"></a>

### Java Listener

<a id="documentation-howto-tls--vm-arguments"></a>

#### VM Arguments

Before we run the listener we need to specify the keystore, keystore password through the VM arguments

For example

-Djavax.net.ssl.keyStore=C:\MyKeyTools\keys\my.keystore
-Djavax.net.ssl.keyStorePassword=abc123
-Djavax.net.ssl.keyPairPassword=xyz123 ( optional )

-Djavax.net.ssl.keyStore corresponds to the keystore created while using "keytools -genkey" command (see Creating Server Certificate using KeyTool section)
-Djavax.net.ssl.keyStorePassword=abc123 corresponds to the keystore password used
-Djavax.net.ssl.keyPairPassword=xyz123 is only REQUIRED if the keypair password is different than the keystore password

<a id="documentation-howto-tls--changes-to-code"></a>

#### Changes to Code

The only change is to use tls as the protocol instead of tcp.

Hence instead on specifying uri as

String uri = "tcp://0.0.0.0:4001";

we will now specify it as

String uri = "tls://0.0.0.0:4001";

<a id="documentation-howto-tls--c-listener"></a>

### C# Listener

The only change is in the URI

Before

string uri = "tcp://0.0.0.0:4001";

After TLS

string uri = "tls://localhost:4001?TlsConnection.certName=gsandhir-wxp02";

Please remember in order to run in secure mode the certificate name has to be specified on the uri. The name of the certificate corresponds to the CN argument we specified in makecert (see section "Creating a server certificate using makecert (C#)". The example in that section created a certificate with -n "CN=gsandhir-wxp02", hence in the uri we pass in the certName as gsandhir-wxp02.

<a id="documentation-howto-tls--changes-to-client"></a>

## Changes to Client

<a id="documentation-howto-tls--java-client"></a>

### Java Client

The client can chose whether it wants to authenticate the server or not

<a id="documentation-howto-tls--changes-when-authentication-is-required"></a>

#### Changes when authentication is required

Before we run the client we need to pass in the location of the truststore as a VM argument

-Djavax.net.ssl.trustStore=C:\MyKeyTools\deftruststore

-Djavax.net.ssl.trustStore - Corresponds to the keystore location where server certificate was imported (see section "Importing the Certificate into a Client Machine (Java)")

Change the uri in the code to String uri = "tls://localhost:4001";

<a id="documentation-howto-tls--changes-when-authentication-is-not-required"></a>

#### Changes when authentication is not required

In this case we do not need to specify the truststore location.

However in the uri we must specify explicitly that authentication should be switched off

String uri = "tls://localhost:4001?TlsConnection.authReqd=false";

<a id="documentation-howto-tls--c-client"></a>

### C# Client

Similar to Java, client can chose whether it wants to authenticate the server or not

<a id="documentation-howto-tls--changes-when-authentication-is-required-2"></a>

#### Changes when authentication is required

The uri in the client code will appear as following

string uri = "tls://localhost:4001?TlsConnection.certName=gsandhir-wxp02";

As mentioned in the listener C# section, the certificate name must correspond to the CN name specified when creating a certificate.

<a id="documentation-howto-tls--changes-when-authentication-is-not-required-2"></a>

#### Changes when authentication is not required

The uri in the client code will appear as following

String uri = "tls://localhost:4001?TlsConnection.authReqd=false";

---

<a id="documentation-javascript-language-binding"></a>

<!-- source_url: https://etch.apache.org/documentation/javascript-language-binding.html -->

<!-- page_index: 28 -->

# Javascript Language Binding

- 1 [Overview](#documentation-javascript-language-binding--javascriptlanguagebinding-overview)
- 2 [Ideals](#documentation-javascript-language-binding--javascriptlanguagebinding-ideals)
- 3 [Mapping Etch IDL to Javascript](#documentation-javascript-language-binding--javascriptlanguagebinding-mappingetchidltojavascript)

- 3.1 [Server-directed method](#documentation-javascript-language-binding--javascriptlanguagebinding-serverdirectedmethod)
- 3.2 [Server-directed method that uses structs](#documentation-javascript-language-binding--javascriptlanguagebinding-serverdirectedmethodthatusesstructs)
- 3.3 [Server-directed method with exception](#documentation-javascript-language-binding--javascriptlanguagebinding-serverdirectedmethodwithexception)
- 3.4 [Client-directed method](#documentation-javascript-language-binding--javascriptlanguagebinding-clientdirectedmethod)
- 3.5 [Client-directed method with a return](#documentation-javascript-language-binding--javascriptlanguagebinding-clientdirectedmethodwithareturn)
- 3.6 [Client-directed method that defines an exception](#documentation-javascript-language-binding--javascriptlanguagebinding-clientdirectedmethodthatdefinesanexception)

- 4 [Current State](#documentation-javascript-language-binding--javascriptlanguagebinding-currentstate)
- 5 [Roadmap](#documentation-javascript-language-binding--javascriptlanguagebinding-roadmap)

<a id="documentation-javascript-language-binding--overview"></a>

## Overview

The Javascript binding, like other Etch language bindings, aims to allow developers a way to access Etch-based services in a manner which is as natural to the developer as possible. Ideally, this means that by simply looking at an Etch IDL, one should be able intuit how one would invoke the methods of such a service with understanding just a few simple conventions.

Since most developers speak code, let's look at some examples of what this really means for Javascript.

Consider a simple, server-directed **add** method defined in an Etch IDL file:

```
@Direction(server)
int add(int arg1, int arg2)
```

Then we consider how one would invoke that method in a Javascript script:

```
svc.add({arg1: 1,arg2: 2,onSuccess: function(returnValue) {alert ("Got a result: " + returnValue); },onError: function(error) {alert("failure");} });
```

Using the above example, let's take a second to talk about how a method in an Etch IDL translates into a Javascript method.

The **svc** variable in the above snippet is the object which represents the client-side reference to the service. There are just a few lines of boilerplate service initialization not shown here, but all one needs to know is that every method associated with the Etch service is represented as a function on this **svc** object, such as the **add** method defined in the Etch IDL above.

The next convention in use here is that each argument is passed into the method as a named parameter. In this example, that's the **arg1:** and **arg2:**. If we had omitted **arg1**, **arg2**, or both, nulls would have been passed to the server for those omitted values.

Finally, every server-directed method support a **onSuccess** and **onError** argument, which expect you to pass a function. These functions serve as callbacks that are fired once the method has completed. The **onSuccess** callback is invoked if the operation completed successfully. Passed back as the only argument to this **onSuccess** callback is the return value of the method (if void is the return then no argument is passed). The **onError** callback is invoked if the operation did not complete successfully; for instance, if the method threw an exception, or if communication was interrupted between client and server on that method call. Note that we use callbacks instead of the return value of the **svc.add** method because Javascript is implemented as a single-threaded language in every browser. This thread is shared between the browser UI and the Javascript script code, so we must not block the browser waiting on a response from the server.

<a id="documentation-javascript-language-binding--ideals"></a>

## Ideals

There are a number of considerations one must make when dealing with browsers, Javascript, and the web in general. The ideals below represent the general mindset and direction of the binding. At this point in time, these ideals are not necessarily fully implemented.

- **No dependency on browser plugins** – such as applets or Flash
- **Cross-browser support**
- **Small Javascript script size** – we don't want to ruin your user download experience
- **No Javascript type pollution** – we don't add fields to native Javascript types, such as Object
- **Hide the transport** – Etch is transport agnostic, so you should not see any HTTP requests/responses in your code. This is important; what if someday there is an alternate Etch Javascript implementation which uses Flash sockets? In such a case, ideally your code could use either transport with just a simple switch during initialization
- **Hide the encoding** – Etch is encoding agnostic. There may be valid reasons to encode messages in XML, JSON, or something else over the transport, but your code should not be exposed to these technology choices
- **Client-directed messages must be supported** – we have first implemented a COMET (alternatively known as hang-polling or long-polling) mechanism within the underlying transport to achieve low-latency, but it only makes sense to allow a web page to use polling instead, if great latency is not demanded
- **Support all popular browser-abstraction libraries** – jQuery, prototype, and other libraries do a great job of abstracting away the complexities of browser-specific differences for a number of AJAX operations. These libraries are becoming indispensable in any rich web application, and ideally, this binding can detect which library is in use and use it, rather than this binding force you to include an entire library to your page when the one already in your page would work just as well
- **Small server-side footprint** – to achieve this, we need to support leveraging **your** already-deployed web server technology, whatever that may be
- **Support any Etch service** – This guided the use of XMLHttpRequest instead of <script> tag or iFrame requests, since an XMLHttpRequest can POST huge amounts of data, whereas <script>/iFrame requests can not send much data since they only support GET. This means that a server-side proxy is very likely required since XMLHttpRequest has cross-domain request restrictions, but, the overall solution has less restrictions on what types of services can be consumed by this binding without heartache
- **Namespacing must be supported** – Etch is inherently namespaced, and maximum compatibility with all services require this binding be namespaced. When using the binding, it should be noted that namespaces are hidden from the developer as much as possible without sacrificing flexibility

<a id="documentation-javascript-language-binding--mapping-etch-idl-to-javascript"></a>

## Mapping Etch IDL to Javascript

Every Etch IDL construct should have a intuitive analogy in Javascript. This section details those mappings.

<a id="documentation-javascript-language-binding--server-directed-method"></a>

### Server-directed method

Etch IDL

```
@Direction(server)
int add(int arg1, int arg2)
```

Javascript

```
svc.add({arg1: 1,arg2: 2,onSuccess: function(returnValue) {alert ("Got a result: " + returnValue); },onError: function(error) {alert("failure");} });
```

<a id="documentation-javascript-language-binding--server-directed-method-that-uses-structs"></a>

### Server-directed method that uses structs

Etch IDL

```
module etch.examples
service Calculator {struct Values {int arg1,int arg2}
struct AddResult {int addResult}
@Direction(server) AddResult add(Values toBeAdded)}
```

Javascript

```
var values = new etch.examples.Calculator.Values(); values.arg1 = 1; values.arg2 = 2;
svc.add({toBeAdded: values,onSuccess: function(returnValue) {// returnValue instanceof etch.examples.Calculator.AddResult == true alert ("Got a result: " + returnValue.addResult); },onError: function(error) {alert("failure");} });
```

<a id="documentation-javascript-language-binding--server-directed-method-with-exception"></a>

### Server-directed method with exception

Etch IDL

```
module etch.examples
service Calculator {exception OverflowException {string message}
@Direction(server) int add(int arg1, int arg2) throws OverflowException}
```

Javascript

```
svc.add({arg1: 1,arg2: 2,onSuccess: function(returnValue) {alert ("Got a result: " + returnValue); },onError: function(error) {if(error instanceof etch.examples.Calculator.OverflowException) {alert("Overflow exception.  Message: " + error.message);}} });
```

<a id="documentation-javascript-language-binding--client-directed-method"></a>

### Client-directed method

Etch IDL

```
/** Example method  server tells client about some state change */
@Direction(client)
void stateChange(string username, boolean online)
```

Javascript

```
svc.callbacks.stateChange = function (username, online)
{
    // define your custom logic in this method, to indicate
    // what happens when the server invokes 'stateChange'
}
```

<a id="documentation-javascript-language-binding--client-directed-method-with-a-return"></a>

### Client-directed method with a return

Etch IDL

```
/** Example method  server tells client about some state change, client acks it */
@Direction(client)
boolean stateChange(string username, boolean online)
```

Javascript

```
svc.callbacks.stateChange = function (username, online)
{
    // because stateChange defines a boolean return, we should return a value
    return true;
}
```

<a id="documentation-javascript-language-binding--client-directed-method-that-defines-an-exception"></a>

### Client-directed method that defines an exception

Etch IDL

```
/** Example method  server tells client about some state change, client can throw exception */ module etch.examples
service Chat {struct NotSupportedException {string reason}
@Direction(client) boolean stateChange(string username, boolean online) throws NotSupportedException}
```

Javascript

```
svc.callbacks.stateChange = function (username, online) {// say we want to let the server know that this client does not support // the stateChange callback
var notSupported = etch.examples.Chat.NotSupportedException(); notSupported.reason = "Not currently supported.";
throw notSupported;}
```

<a id="documentation-javascript-language-binding--current-state"></a>

## Current State

- Only one server-side implementation currently, built for C#/.NET using System.Net.HttpListener. SVN location: <https://svn.apache.org/repos/asf/etch/branches/etch-javascript>
- Support for the following types: **boolean**, **int**, **byte**, **short**, **long**, **string**, **List**, **struct**, **datetime**
- Exceptions are supported.
- Notification is given on session "DOWN" and session "UP"
- jQuery is supported.
- Etch compiler successfully generates Javascript stub code (etch -b javascript)

<a id="documentation-javascript-language-binding--roadmap"></a>

## Roadmap

- Build up unit tests while also refactoring/cleaning up existing code
- Work on scale for C# implementation (need to vet System.Net.HttpListener sooner rather than later)
- Implement the following types: Map and Set
- Implement onUnload handler logic to keep browser resource usage low
- Implement cookie session handling (currently the session dies when window is closed)
- Add support for another browser-abstraction library, such as prototype.
- Implement Authorize on client.
- Assuming C# implementation is stable and mostly complete, implement Java implementation (presumably using Jetty).

---

<a id="documentation-language-reference"></a>

<!-- source_url: https://etch.apache.org/documentation/language-reference.html -->

<!-- page_index: 29 -->

# Introduction

- 1 [Introduction](#documentation-language-reference--languagereference-introduction)
- 2 [Syntax Elements](#documentation-language-reference--languagereference-syntaxelements)
- 3 [Native Data Types](#documentation-language-reference--languagereference-nativedatatypes)
- 4 [Extended Types](#documentation-language-reference--languagereference-extendedtypes)

- 4.1 [Datetime](#documentation-language-reference--languagereference-datetime)
- 4.2 [List](#documentation-language-reference--languagereference-list)
- 4.3 [Set](#documentation-language-reference--languagereference-set)
- 4.4 [Map](#documentation-language-reference--languagereference-map)

- 5 [Object Data Type](#documentation-language-reference--languagereference-objectdatatype)

- 5.1 [Constants](#documentation-language-reference--languagereference-constants)
- 5.2 [Enumerations](#documentation-language-reference--languagereference-enumerations)
- 5.3 [Structured Type](#documentation-language-reference--languagereference-structuredtype)
- 5.4 [Arrays](#documentation-language-reference--languagereference-arrays)
- 5.5 [External Type](#documentation-language-reference--languagereference-externaltype)
- 5.6 [Exceptions](#documentation-language-reference--languagereference-exceptions)
- 5.7 [Messages](#documentation-language-reference--languagereference-messages)
- 5.8 [Includes](#documentation-language-reference--languagereference-includes)
- 5.9 [Mixin](#documentation-language-reference--languagereference-mixin)
- 5.10 [Service](#documentation-language-reference--languagereference-service)
- 5.11 [Annotations](#documentation-language-reference--languagereference-annotations)
- 5.12 [Module](#documentation-language-reference--languagereference-module)

- 6 [Supported Annotations](#documentation-language-reference--languagereference-supportedannotations)

- 6.1 [@AsyncReceiver](#documentation-language-reference--languagereference-asyncreceiver)
- 6.2 [@Authorize](#documentation-language-reference--languagereference-authorize)
- 6.3 [@Direction](#documentation-language-reference--languagereference-direction)
- 6.4 [@Extern](#documentation-language-reference--languagereference-extern)
- 6.5 [@Oneway](#documentation-language-reference--languagereference-oneway)
- 6.6 [@Timeout](#documentation-language-reference--languagereference-timeout)
- 6.7 [@ToString](#documentation-language-reference--languagereference-tostring)
- 6.8 [@Unchecked](#documentation-language-reference--languagereference-unchecked)

- 7 [Formal Comments](#documentation-language-reference--languagereference-formalcomments)

<a id="documentation-language-reference--introduction"></a>

# Introduction

The Network Service Definition Language is used to specify the message exchange between client / server applications. The language specifies the messages, their parameters, message direction, timeout, authorization, delivery style, custom types, constants, and documentation for the service and each message, parameter, type, and constant. A compiler can then be used to process the NSDL into meta-data and code to support implementing clients and servers in a variety of different programming languages and environments with the help of a small runtime library.

<a id="documentation-language-reference--syntax-elements"></a>

# Syntax Elements

The NSDL uses syntax elements common to other programming languages:

- Keywords are used to identify grammar elements such as service, constants, enumerations, structured types, external types, exceptions, and native types. The keywords are: boolean, byte, const, double, enum, exception, extends, extern, false, float, int, long, mixin, include, module, null, object, service, short, string, struct, throws, true, and void. Keywords may not be used as an identifier for any service defined element.
- Boolean, numeric, and string literals are used to specify the values of constants, and as arguments to annotations. Examples include true, 49, 3.14159, and "boo". The usual hexadecimal, octal, and binary integral formats (e.g., 0x23, 023, and 0b011 respectively) are also supported. The usual string escapes as well as the Unicode escape are supported:


```
\t, \n, \r, \\, \", and \u03a9
```

- Identifiers are used to specify the name of the service, each message, parameter, custom type, and constant. An identifier is composed of ASCII characters, may start with an upper or lowercase alphabetic, and may contain upper and lower case alphabetic, numeric, or underscore characters. While not enforced (yet), the recommended style is that service, enum, struct, exception, and externnames should start with uppercase and use camel case conventions (e.g., FastCar, BlackCatWalking, etc.). Message and parameter names should start with lowercase and use camel case conventions (e.g., makeCall, sendName, etc.). Constants and enum elements should be all uppercase with underscores (e.g., FISH\_SOUP, STALE\_BREAD, etc.).
- Definitions may be terminated by a semi-colon ( ";" ) but that is totally optional.
- Comments may be the standard Java types:
  - // causes the rest of the line to be ignored.
  - /\* blah \*/ causes blah to be ignored; may extend over multiple lines; may not be nested.
  - /\*\* blah \*/ is a formal comment. Adds a description to the following definition (if allowed). Follows Javadoc style. Descriptions are copied into the generated interfaces.

<a id="documentation-language-reference--native-data-types"></a>

# Native Data Types

The native types include:

- boolean - true or false
- byte - signed 8-bit quantity (-2^7 to 2^7-1)
- short - signed 16-bit quantity (-2^15 to 2^15-1)
- int - signed 32-bit quantity (-2^31 to 2^31-1)
- long - signed 64-bit quantity (-2^63 to 2^63-1)
- float - single precision IEEE floating point (max 3.4028235e38)
- double - double precision IEEE floating point (max 1.7976931348623157e308)
- string - sequence of characters (generally, Unicode), arbitrary length

These types correspond to the architectural types found on almost all computer systems.

<a id="documentation-language-reference--extended-types"></a>

# Extended Types

Common extended types are also included.

<a id="documentation-language-reference--datetime"></a>

## Datetime

Datetime represents a specific moment in time.

<a id="documentation-language-reference--examples"></a>

### Examples

```
Datetime timeSaved;
boolean isSunday ( Datetime time )
```

<a id="documentation-language-reference--list"></a>

## List

A List represents an ordered collection of values.

<a id="documentation-language-reference--examples-2"></a>

### Examples

```
List values;
object getLastValue ( List list )
```

<a id="documentation-language-reference--set"></a>

## Set

A Set represents an unordered collection of unique values.

<a id="documentation-language-reference--examples-3"></a>

### Examples

```
Set values;
boolean addValueToSet ( Set set, object value )
```

<a id="documentation-language-reference--map"></a>

## Map

A Map represents a set of keys, each of which points to a value.

<a id="documentation-language-reference--example"></a>

### Example

```
boolean addPair ( Map map, object key, object value )
```

<a id="documentation-language-reference--object-data-type"></a>

# Object Data Type

An **object** is used to model a parameter or result where the actual type is determined at runtime. An object type specification may be used anywhere a native data type is allowed except when declaring constants.

<a id="documentation-language-reference--examples-4"></a>

### Examples

```
struct ValueList ( string name, object[] values )
exception BadValue ( int id, string msg, object value )
object getValue ( string name )
object[] setValue ( string name, object value )
```

<a id="documentation-language-reference--constants"></a>

## Constants

A constant declaration is used to include named values into the generated interfaces. There is no messaging component associated with them, just a handy way to define a named value which is available to each implementation in appropriate target syntax.

The value of the constant must be appropriate for the type.

Constant names are by convention all uppercase, with underscore used to separate words.

<a id="documentation-language-reference--syntax"></a>

### Syntax

```
<const_stmt> ::= "const" <ctype> <id> "=" <cvalue> (";")?
<ctype> ::= "boolean" | "byte" | "short" | "int" | "long" | "float" | "double" | "string"
<cvalue> ::= "true" | "false" | <integer> | <octal> | <hex> | <binary> | <decimal> | <string>
```

<a id="documentation-language-reference--examples-5"></a>

### Examples

```
const int MAX_NAME_LENGTH = 31
const string USER_NAME = "Fred"
const float PI = 3.14159
```

<a id="documentation-language-reference--enumerations"></a>

## Enumerations

An enumeration is used to declare a type which has a named set of values. These are most often used where the set of values is small. Some languages use integers to model enumerations while others use tokens (identifiers) and yet others use object instances.

Enumeration names are by convention capitalized. Enumeration item names are all uppercase.

<a id="documentation-language-reference--syntax-2"></a>

### Syntax

```
<enum_stmt> ::= "enum" <id> "(" <id> ("," <id>)* ")" (";")?
```

<a id="documentation-language-reference--examples-6"></a>

### Examples

```
enum State ( OPEN, CLOSED )
enum RGBColor ( RED, GREEN, BLUE )
```

<a id="documentation-language-reference--structured-type"></a>

## Structured Type

A structure is used to model a small set of named parameters of heterogeneous type. When a structure contains another structure as a parameter it is by reference. Thus, in Etch, a structure may contain itself (directly or indirectly) as a parameter (if the containment was by value, a structure could not contain itself because that would introduce a storage recursion).

Structure names are by convention capitalized. Parameter names are by convention lowercase.

Strangely enough, a structure might not have any parameters. This might seem silly, but the mere presence of the structure might be used like a boolean to assert a condition (that is, indicate the condition is true, whereas null indicates the condition is false), while allowing for future expansion by adding parameters to the structure.

Note that <ptype> includes the native types as well as <id>, <qid>, and <object>. The <id> or <qid> is used to indicate a custom type name. An <object> is used to model a parameter or result where the actual type is determined at runtime.

A structure may extend another structure. In this way the structure inherits the parameters and identity of the extended structure. This is functionally equivalent to class inheritance in java, csharp, ruby, etc.

There are some rules:

1. a structure may not extend another such that an inheritance loop is created.
2. a structure may not declare a parameter whose name is the same as any already in its inheritance.

<a id="documentation-language-reference--syntax-3"></a>

### Syntax

```
<struct_stmt> ::= "struct" <id> <params> ( "extends> <id> )? ( ";" )?
<params> ::= "(" ( <param> ( "," <param> )* )? ")"
<param> ::= <ptype> <dim> <id>
<ptype> ::= <ctype> | "object" | <ref>
<dim> ::= ( "[]" )*
<ref> ::= <xid>
<xid> :: = <qid> | <id>
<qid> :: = <ID> ("." <ID>)+>
```

<a id="documentation-language-reference--examples-7"></a>

### Examples

```
struct Point ( int x, int y )
struct Path ( Point[] points )
struct AsyncAction () extends Action
```

<a id="documentation-language-reference--arrays"></a>

## Arrays

As you can see in <param>, above, a parameter in a structure may be dimensioned. The number of square bracket pairs indicates the dimensionality. None indicates a scalar parameter. There is no particular limit on the number of dimensions you may have or the size of any particular dimension. Let your common sense guide you, keeping in mind all the possible language bindings there might be.

<a id="documentation-language-reference--examples-8"></a>

### Examples

```
int[] x // single dimensional array of int.
Point[][] grid // two-dimensional array of Point.
```

<a id="documentation-language-reference--external-type"></a>

## External Type

Sometimes you really need to be able to reference a target language specific type in the NSDL. When you do, you must think carefully about the applicability to other language bindings that may want or need to use your service. Many useful types have analogs in the other languages anyway, such as Java's HashMap, ArrayList, and Date types. Note that Etch cannot model abstract or generic types, and so where abstracts or generics are involved they must be made concrete. In Java, StrIntMap instead of HashMap<String, Integer>, HashMap, or even Map:

```
package project.util;
import java.util.HashMap;
public class StrIntMap extends HashMap<String, Integer> {// nothing else needed}
```

When you specify the external type, you import it into Etch by giving it a name that you will use inside Etch to reference it. Then for each language binding, you supply information about what the concrete type is and how to serialize / de-serialize it.

Note: the @Extern annotation, along with all the other annotations, is described later. It is only shown here because otherwise the example of extern would be too vague. See the appendix for an extern example.

<a id="documentation-language-reference--syntax-4"></a>

### Syntax

```
<extern_stmt> ::= "extern" <id> (";")?
```

<a id="documentation-language-reference--examples-9"></a>

### Examples

```
@Extern("java", "project.util.StrIntMap", "", "project.util.StrIntMapSerializer", "")
extern StrIntMap
```

<a id="documentation-language-reference--exceptions"></a>

## Exceptions

Exceptions are a special kind of struct which are an alternative response to a message execution. An exception cannot be a parameter or result of a message, nor a parameter in a structure.

When a program wants to return an exception in Java, it creates an instance of the exception and throws it (compare this with creating an instance of a normal type and returning it). The throw operation, unlike return, can be performed deep in the call chain and terminates each call up the chain until caught by a handler. Return, on the other hand, can only terminate one call up the call chain and makes its value available to the next level up.

In some programming languages (e.g., Java) exceptions are checked: a method cannot throw a checked exception unless it has declared that it might. Unchecked exceptions can always be thrown, and usually correspond to low-level conditions such as an attempt to use a null pointer, index an array element which doesn't exist, etc. In other programming languages (e.g., C#, Ruby, Python), all exceptions are unchecked. Some programming languages (e.g., C) do not have a concept of exception whatsoever.

Etch reflects this by requiring methods to declare thrown exceptions. In this way the declarations may be passed through to programming languages which require the declarations. Of course, it is good for the users of a service to know which exceptions a particular message might throw.

Note: exceptions should include at least some detail as to the cause, enough to suggest a solution of the problem. In messaging systems this is especially important, as a client often does not have enough access to the server to debug a problem from the server side. As you might expect, an exception with a simple message "parameter x (value 23) is not in the expected range (1-10)" is way more helpful than "value out of range". Furthermore, localization considerations might dictate that you declare an exception like this:

```
Exception IntOutOfRange( string name, int value, int min, int max )
```

and let the receiver format it as they wish. (But, that can get messy really fast!)

Like structures, exception may extend other exceptions. See the discussion under structures,above.

<a id="documentation-language-reference--syntax-5"></a>

### Syntax

```
<except_stmt> ::= "exception" <id> <params> ( "extends> <ref> )? ( ";" )?
<ref> ::= <xid>
<xid> :: = <qid> | <id>
<qid> :: = <ID> ("." <ID>)+>
```

<a id="documentation-language-reference--examples-10"></a>

### Examples

```
exception BadArgument( string name, string reason )
exception NoAuthorization( string name, string reason )
```

<a id="documentation-language-reference--messages"></a>

## Messages

Messages describe the actual network traffic between the clients and servers. We use function definition syntax but the elements are the same: a message type and parameters (names and types).

Message declarations actually describe two messages (if the message is two-way). The first is the request message which includes the message type and parameters with argument values. The second is the response message which includes the response message type and the result parameter and value.

Messages can terminate normally by returning a value or they can terminate abnormally by throwing an exception. Either type of termination will return a response message from the remote process (again, unless the message is declared one-way).

**NOTE:** The vast majority of modern programming languages support exceptions; those that do not will need to accommodate the dual nature of the response message.

**NOTE:** One-way messages must have a void result type and not throw any exceptions.

Message names and parameter names by convention start with a lowercase alphabetic, then use camel case.

<a id="documentation-language-reference--syntax-6"></a>

### Syntax

```
<message_stmt> ::= <rtype> <id> <params> (<throws>)? (";")?
<rtype> ::= ( <ptype> <dim> ) | "void"
<throws> ::= "throws" <ref> ( "," <ref> )*
<ref> ::= <xid>
<xid> :: = <qid> | <id>
<qid> :: = <ID> ("." <ID>)+>
```

<a id="documentation-language-reference--examples-11"></a>

### Examples

```
int add( int x, int y )
Date getBirthday( string name ) throws NameNotFound
Location[] getBestPath( Location[] locations ) throws NoSuchPath
void report( Date when, EventType type, string detail )
```

<a id="documentation-language-reference--includes"></a>

## Includes

You many add an include to to an etch servicde function.

<a id="documentation-language-reference--syntax-7"></a>

### Syntax

```
<inlcude> ::= "inlcude" <filename> (";")?
```

<a id="documentation-language-reference--example-2"></a>

### Example

To use include files in an etch file, use the .txt extention, not .etch for includes.
You can also include other include files in the etch include files.

```
module etch.bindings.java.compiler.test

@Direction(Both)
@Timeout(4000)
service TestInclude
{
	const int INT1 = 98765431;

	const boolean BOOL3 = false
	const boolean BOOL4 = true
	
	include "testincl.txt";
	
	const boolean BOOL1 = false
	const boolean BOOL2 = true
	
}
```

<a id="documentation-language-reference--testincl.txt"></a>

##### testincl.txt

```
 
const int INT2 = -2147483648;
include "testincl1.txt";
```

<a id="documentation-language-reference--mixin"></a>

## Mixin

A mixin is the mechanism used to incorporate the messages and types defined within another service into the current service. To the extent possible the original service retains its identity, such that with an object oriented language such as Java, C#, or Ruby, an instance of the current service could be passed where an instance of the mixed in service is expected. This facilitates the creation of reusable service libraries. You can have as many mixins as you like (up to the limit imposed by the various language bindings).

Two examples of a mixin are an authentication service and an event service. These could be standard components for a deployment of a suite of other services. You only have to define them once, then you can add them to each of your other services as you like.

<a id="documentation-language-reference--syntax-8"></a>

### Syntax

```
<mixin_stmt> ::= "mixin" <ref> (";")?
<ref> ::= <xid>
<xid> :: = <qid> | <id>
<qid> :: = <ID> ("." <ID>)+>
```

<a id="documentation-language-reference--examples-12"></a>

### Examples

```
module etch.bindings.csharp.compiler.test

@Direction(Both)
service MixinTest
{
	mixin NestedMixin
	@Authorize(isLoggedIn)
	int add( int x, int y )
	
	@Authorize(isLoggedIn)
	int sub( int x, int y )
	
	void testRef(test t) throws Excp2
	
		
}
```

<a id="documentation-language-reference--nestedmixin"></a>

##### NestedMixin

```
module etch.bindings.csharp.compiler.test
@Direction(Both) service NestedMixin {
struct test (string name,string value)
@Unchecked exception Excp2()
void login( string name, string pw )
void logout()
boolean isLoggedIn()
}
```

<a id="documentation-language-reference--important-notes"></a>

#### Important Notes

- The mixin etch file must be present in the Include Path. In the above example, NestedMixin must be present in the Include Path. If the include path is not specified, then the Mixin etch file will only be searched in the current directory. Thus in the above example, if -I option (include option) is not specified, then NestedMixin will only be searched in the directory in which MixinTest is present.
- When a user compiles the etch file which contains the mixin (TestMixin.etch in the above example), he can chose whether he wants the mixin artifacts to be generated or not. If he chooses not to generate the artifacts, then he must specify -n command line option If he chooses to generate the mixin artifacts then he must specify either -m or -d option (Please refer to the Etch Compiler Guide for more details on these options). Failure to specify either one of these option will lead to compilation problem.

<a id="documentation-language-reference--service"></a>

## Service

All the definitions above are packaged into a service, which provides a naming scope. The compiler uses the features available in each language binding to create the naming scope. For example, in Java, the compiler creates a number of interfaces and classes with names derived from the service name.

<a id="documentation-language-reference--syntax-9"></a>

### Syntax

```
<service> ::= opts "service" <id> "{" ( <stmt> )* "}"
opts ::= (opt)*
opt ::= @ id (args)?
args 	::= 	arg (, arg )*
arg 	::= 	( cvalue | xid | <NULL> )
cvalue 	::= 	( <TRUE> | <FALSE> | <INTEGER> | <OCTAL> | <HEX> | <BINARY> | <DECIMAL> | <STR> )
xid 	::= 	( qid | id )
<qid> :: = <ID> ("." <ID>)+>
<stmt> ::= <const_stmt> | <enum_stmt> | <struct_stmt> | <extern_stmt> | <except_stmt> | <message_stmt> | <mixin_stmt>
```

<a id="documentation-language-reference--example-3"></a>

### Example

```
service DigestAuth {exception LoginFailure( string msg ) string getSeed() void login( string name, string seed, string digest ) throws LoginFailure void logout() boolean isLoggedIn()}
```

<a id="documentation-language-reference--annotations"></a>

## Annotations

Annotations may be applied to a <stmt> to alter its behavior. Where it makes sense, you can even apply an annotation to the <service> to set the global behavior or defaults. See below for descriptions of supported annotations.

<a id="documentation-language-reference--syntax-10"></a>

### Syntax

```
opts ::= (opt)*
opt ::= @ id (args)?
args 	::= 	arg (, arg )*
arg 	::= 	( cvalue | xid | <NULL> )
cvalue 	::= 	( <TRUE> | <FALSE> | <INTEGER> | <OCTAL> | <HEX> | <BINARY> | <DECIMAL> | <STR> )
xid 	::= 	( qid | id )
<qid> :: = <ID> ("." <ID>)+>
```

<a id="documentation-language-reference--examples-13"></a>

### Examples

```
@Timeout( 4000 )
@Direction( Server )
Date getBirthday( string name )
```

<a id="documentation-language-reference--module"></a>

## Module

The last bit of syntax is the module. This appears in the NSDL file before the service and defines the global namespace of the service. This has a very strong correlation to the Java package or the C# namespace, and a looser correlation to the Ruby module. It also contributes to the fully qualified name of the service itself, which is used to distinguish the service from other like-named services.

<a id="documentation-language-reference--syntax-11"></a>

### Syntax

```
<module> ::= "module" (<qid> | <id>) (";")? <service>
```

<a id="documentation-language-reference--examples-14"></a>

### Examples

```
module project.auth
service DigestAuth
{
...
}
```

<a id="documentation-language-reference--supported-annotations"></a>

# Supported Annotations

<a id="documentation-language-reference--asyncreceiver"></a>

## @AsyncReceiver

```
@AsyncReceiver( NONE | QUEUED | FREE )
```

Specifies that the processing mode used by the server for this message or the default processing mode for all the messages of the service. A specification on a message overrides the service default.

- NONErequests the message be delivered on the message receiver thread. While this message is being processed, no other message may be read and delivered. Messages are processed in the order received.
- QUEUEDrequests the message be queued to a thread pool for delivery. This is generally used by operations which complete relatively quickly but might want to dialog with the caller using callbacks, or perform some other operation which might briefly block.
- FREErequests the message be delivered by a newly created free thread. This is generally used by long running operations.

<a id="documentation-language-reference--default"></a>

### Default

The service default is NONE.

<a id="documentation-language-reference--may-be-applied-to"></a>

### May Be Applied To

<message\_stmt>, <service>

<a id="documentation-language-reference--example-4"></a>

### Example

```
// run add asynchronously on a queued pool thread.
@AsyncReceiver( QUEUED )

int add( int x, int y )
```

<a id="documentation-language-reference--authorize"></a>

## @Authorize

```
 @Authorize[( method [, arg ...] )] 
```

Specifies that the message receiver should use the specified method to determine whether the message is allowed to be processed, or set the service default authorization method for all messages in the service. Method should be a service message declared the same direction as this message and returning a boolean result. An exception will be thrown by the receiver if the message is not allowed. A specification on a message overrides the service default.

The args are a sequence of named or unnamed constants, enumeration values, or message parameters or parameters of parameters, etc., corresponding in number, order, and type to the signature of method.

Method true always allows the message, while falsenever allows the message. Neither of these are allowed any args.

<a id="documentation-language-reference--default-2"></a>

### Default

The service default is true. If specified without an argument, true is assumed.

<a id="documentation-language-reference--may-be-applied-to-2"></a>

### May Be Applied To

<message\_stmt>, <service>

<a id="documentation-language-reference--example-5"></a>

### Example

```
// only allow logged in users to delete files.
@Authorize( isLoggedIn )

void deleteFile( string name )

// returns true if a user is logged in.
boolean isLoggedIn()

// only allow the admin of the specified user to grant rights.
@Authorize( isAdminOf, userName)
void grantRight( string userName, string right )

// returns true if the current user is the admin of the
// specified user. isAdminOf should test isLoggedIn first.
boolean isAdminOf( string userName )

// don't let anyone send this message for now.
@Authorize( false )

void rmDashRFSlash()
```

<a id="documentation-language-reference--direction"></a>

## @Direction

```
 @Direction( SERVER | CLIENT | BOTH ) 
```

Specifies the direction of the message, or sets the service default direction for all messages in the service:

- SERVER means from the client to the server.
- CLIENT means from the server to the client (a callback).
- BOTH means either client or server may send the message to the other.

A specification on a message overrides the service default.

<a id="documentation-language-reference--default-3"></a>

### Default

The service default is SERVER.

<a id="documentation-language-reference--may-be-applied-to-3"></a>

### May Be Applied To

<message\_stmt>, <service>

<a id="documentation-language-reference--example-6"></a>

### Example

```
// notify the client that a user's status has changed.
@Direction( CLIENT )

void statusUpdate( string userName, boolean online )
```

<a id="documentation-language-reference--extern"></a>

## @Extern

```
 @Extern( language, name, nImport, serializer, sImport ) 
```

Declares language binding and serializer for an external type. Language is a compiler supported name for a binding (e.g., java, csharp, ruby); name is the language specific name of the type to use; nImport is a string that must be used in something like an import or requires statement to make name available; serializer is the language specific name of the type to use to import and export (this type must declare certain specific methods); sImport is a string that must be used in something like an import, using, include, or require statement to make serializer available.

<a id="documentation-language-reference--default-4"></a>

### Default

There is no default. If NSDL is compiled for a language which has no binding for an external type, the compilation will fail.

<a id="documentation-language-reference--may-be-applied-to-4"></a>

### May Be Applied To

<extern\_stmt>

<a id="documentation-language-reference--example-7"></a>

### Example

```
// for java, map Date to java.util.Date and use
// project.util.DateSerializer to serialize and
// deserialize the object.

@Extern( java, "java.util.Date", "",

"project.util.DateSerializer", "" )

// for csharp, map Date to System.DateTime, and
// use project.util.DateTimeSerializer to serialize
// and deserialize the object.

@Extern( csharp, "System.DateTime", "", "project.util.DateTimeSerializer", "" )

// for ruby, map Date to Time, and use TimeSerializer
// from project/util/time_serializer.rb to serialize
// and deserialize the object.

@Extern( ruby, "Time", "", "TimeSerializer", "project/util/time_serializer" )

extern Date
```

<a id="documentation-language-reference--oneway"></a>

## @Oneway

```
 @Oneway[( true | false )] 
```

Specifies that the sender of this message does not wait for any response, or specifies the service default for all messages. This is sometimes called a fire-and-forget message, and some other times called an event message. Such a message must be declared to have a void result, and may not be declared to throw any exceptions. A specification on a message overrides the service default.

<a id="documentation-language-reference--default-5"></a>

### Default

The service default is false. If specified without an argument, true is assumed.

<a id="documentation-language-reference--may-be-applied-to-5"></a>

### May Be Applied To

<message\_stmt>, <service>

<a id="documentation-language-reference--example-8"></a>

### Example

```
// notify the client that a user's status has changed.
// don't wait for any response.
@Direction( CLIENT ) @Oneway

void statusUpdate( string userName, boolean online )
```

<a id="documentation-language-reference--timeout"></a>

## @Timeout

```
 @Timeout( ms ) 
```

Specifies the time in milliseconds for the sender of a message to wait for a response, or specifies the service default timeout for all messages. Timeout of '0' means wait forever. A specification on a message overrides the service default.

<a id="documentation-language-reference--default-6"></a>

### Default

The service default is .

<a id="documentation-language-reference--may-be-applied-to-6"></a>

### May Be Applied To

<message\_stmt>, <service>

<a id="documentation-language-reference--example-9"></a>

### Example

```
// wait 30 seconds for mom to respond, then if
// she doesn't, decide whether to go anyway...
@Timeout( 30000 )

boolean getPermission( "Mom, can I go to the movie with Fred?" )
```

<a id="documentation-language-reference--tostring"></a>

## @ToString

```
 @ToString( fmt ) 
```

Specifies a format specifier for language specific "to string" methods. The "to string" methods are written in the appropriate way for the target languages. Why "to string" methods? They are needed for debugging and logging.

<a id="documentation-language-reference--default-7"></a>

### Default

The default is "param1={param1}, ..." for each parameter of the struct or exception.

<a id="documentation-language-reference--may-be-applied-to-7"></a>

### May Be Applied To

<struct\_stmt>, <except\_stmt>

<a id="documentation-language-reference--example-10"></a>

### Example

```
@ToString( "Point({x}, {y})" )

struct Point( int x, int y )
```

<a id="documentation-language-reference--unchecked"></a>

## @Unchecked

```
 @Unchecked[( true | false)] 
```

In languages with checked exceptions, specifies than an exception should be unchecked, or specifies that the service default for exceptions should be unchecked.

<a id="documentation-language-reference--default-8"></a>

### Default

The service default is false. If specified without an argument, true is assumed.

<a id="documentation-language-reference--may-be-applied-to-8"></a>

### May Be Applied To

<except\_stmt>, <service>

<a id="documentation-language-reference--example-11"></a>

### Example

```
@Unchecked
exception AuthException( string name, string reason )
```

<a id="documentation-language-reference--formal-comments"></a>

# Formal Comments

Formal comments are used to describe each Etch service description element. The descriptions are copied over into the generated files so that they are available to the programmers in their natural environments. Here is a simple example:

```
/** * The HydroMath service uses an atomic-powered highly-advanced * hydrostatic processor to perform astounding binary * manipulations.*/
service HydroMath {
/** * Exception thrown if the hydrostatic processor * encounters a problem.* @param code the problem description code.*/ exception OverflowException( int code )
/** * Returns the sum of x and y.* @param x input value.* @param y input value.* @return the sum of x and y.* @throws OverflowException if the hydrostatic * processor encounters a problem.*/ void add( int x, int y ) throws OverflowException}
```

This produces (for the java target) the following output:

```
/** * Exception thrown if the hydrostatic processor * encounters a problem.*/ public class OverflowException extends Exception {/** * Constructs the OverflowException.* @param code the problem description code.*/ public OverflowException( Integer code ) {this.code = code;}
/** * the problem description code. RTFM.*/ public Integer code;}
/** * The HydroMath service uses an atomic-powered highly-advanced * hydrostatic processor to perform astounding binary * manipulations.*/ public interface HydroMathServer extends HydroMath {/** * Returns the sum of x and y.* @param x input value.* @param y input value.* @return the sum of x and y.* @throws OverflowException if the hydrostatic * processor encounters a problem.*/ public Integer add( Integer x, Integer y ) throws OverflowException;}
```

A formal comment may be attached to:

- Service
- Constant
- Enumeration
- Enumeration element
- Structure
- Exception
- Message
- Parameter of a structure, exception, or message
- Exception thrown by a message

The formal comment is started by the /**\* sequence, and terminated by the \*/ sequence. The contents, minus internal sequences that look like <eol><whitespace>**<whitespace> are attached to the element in question.

A parameter of a structure, exception, or message may be commented two ways. The Javadoc style was shown in the HydroMath example above. The second style is shown here:

```
/** @return the sum of x and y. */
int add(

   /** input value. */
   int x,

   /** input value. */
   int y

) throws

   /** if the hydrostatic processor encounters a problem. */
   OverflowException
```

The body of the formal comment is taken whole for elements except for a structure, exception, or message. For those the body is scanned looking for @param tags, and for a message, @return or @throws tags. If / when one of those tags is found, the main description is terminated and text is spooled to the description of the sub-element. In all cases the descriptions may span multiple lines.

<a id="documentation-language-reference--param-name-descr"></a>

### @param <name> <descr>

The name must specify the name of a structure, exception, or message.

<a id="documentation-language-reference--return-descr"></a>

### @return <descr>

The message must be defined to return a value.

<a id="documentation-language-reference--throws-name-descr"></a>

### @throws <name> <descr>

The name must specify the name of an exception that the message throws.

---

<a id="documentation-overview"></a>

<!-- source_url: https://etch.apache.org/documentation/overview.html -->

<!-- page_index: 30 -->

# Overview

- 1 [Abstract](#documentation-overview--overview-abstract)
- 2 [Problem Solved](#documentation-overview--overview-problemsolved)
- 3 [Network Service Description Language](#documentation-overview--overview-networkservicedescriptionlanguage)
- 4 [Language Independent Messaging](#documentation-overview--overview-languageindependentmessaging)
- 5 [Transport Independence](#documentation-overview--overview-transportindependence)
- 6 [Message Definition](#documentation-overview--overview-messagedefinition)
- 7 [Service Extension and Versioning](#documentation-overview--overview-serviceextensionandversioning)
- 8 [Fundamental Data Types](#documentation-overview--overview-fundamentaldatatypes)
- 9 [Extended Data Types](#documentation-overview--overview-extendeddatatypes)
- 10 [External Data Types](#documentation-overview--overview-externaldatatypes)
- 11 [Named Constants](#documentation-overview--overview-namedconstants)
- 12 [Implementation Details](#documentation-overview--overview-implementationdetails)
- 13 [Binary Transport](#documentation-overview--overview-binarytransport)
- 14 [Footprint](#documentation-overview--overview-footprint)
- 15 [Performance](#documentation-overview--overview-performance)
- 16 [Roadmap](#documentation-overview--overview-roadmap)

<a id="documentation-overview--abstract"></a>

## Abstract

Etch is a cross-platform, network messaging system which includes a service description language, a compiler, and runtime for a variety of programming languages. Etch is transport independent, which allows for a variety of transports to be used depending upon need and circumstance.

<a id="documentation-overview--problem-solved"></a>

## Problem Solved

The Etch project was started because we wanted to have a way to write a concise, formal description of the message exchange between a client and a server, with a hefty set of requirements, including: the messaging technology should support two-way, real-time communication, have high performance and scalability, support clients and servers written in differing languages, support client / server running in wide range of contexts (such as thin web client, PC application, or server), and must support anyone (Cisco or not) adding new language bindings and new transports if the set provided by the Cisco Unified Application Environment team is not sufficient.

Existing competing systems were either too slow, hard to use, bloated, and / or proprietary. In any case, none fit this matrix of requirements perfectly. So, Etch is designed to be easy to use, fast, and small; while still being flexible enough to satisfy the above requirements.

SOAP / REST Web Services offer an interesting comparison by contrast. While Web Services are generally accepted as the de facto standard for cross-platform communication due to strong adoption across many tools and languages, the unfortunate reality is that Web Services have serious deficiencies which make them completely unusable for real-time communications. Specifically, Web Services have no effective way to communicate asynchronously from server to client due to a reliance on HTTP and have very high parsing overhead due to XML and SOAP message bodies. In some deployments server to client communication would be blocked by a firewall. Finally, any particular language usually does not support every aspect of Web Services, so it is completely possible to create a Web Service that is not, in fact, cross-platform.

<a id="documentation-overview--network-service-description-language"></a>

## Network Service Description Language

The Etch service description language allows the messages of the service to be described using a concise, high-level programming language syntax. The NSDL describes messages; direction of the messages, message inputs and outputs, response timeouts, sender and receiver thread models, and authentication. The NSDL also allows for the specification of structured data, enumerated values, named constants, and exceptions. Comments written into the NSDL are copied into the generated native language files so that they are available to the programmers.

<a id="documentation-overview--language-independent-messaging"></a>

## Language Independent Messaging

Etch supports language independence by compiling language appropriate interfaces supported by libraries to send and receive the messages. External data types are defined and mapped to appropriate language specific runtime objects, supported by native serialization code.

<a id="documentation-overview--transport-independence"></a>

## Transport Independence

Etch service message descriptions and data are compiled into data structures which are used by the transport layer to format the messages for transport. All the information of the message is available to the transport layer. Transport is subdivided into message formatting, security, and protocol. Message formats include a compressed binary tagged format as well as XML. Security includes stream ciphers such as SSL / TLS and block ciphers such as DES or AES. Protocols include TCP, UDP (unicast, multicast, broadcast), and various SOAP formats. Other formats, security, and protocols are easily added.

<a id="documentation-overview--message-definition"></a>

## Message Definition

A message is defined as a standard function call:

```

int add( int x, int y )
```

It has a name and a list of typed fields. It may return a value and it may throw an exception. However, as Etch is a client / server network messaging technology – not purely in-memory code – network considerations must be made. So in addition there are attributes, or tags, that can further qualify messages for optimal performance and encourage correct programming paradigms. For instance, a message that has no need of a response (fire-and-forget) may be decorated as 'one-way':

```

@Oneway
void endSession()
```

With a client & server, the direction of the message is of course important. By default, a message is assumed client-initiated; server-initiated messages (callbacks) must be decorated appropriately:

```

@Direction(client)
void notify(MyStruct data)
```

Another important message attribute is authorization. For example, if a message should not be allowed unless a certain requirement is met, then the message is tagged with that requirement. In this way the requirement is made plain, and the programmers implementing the service cannot forget:

```

@Authorize(isLoggedIn)
void deleteFile(string filename)
```

There are more attributes that can be used to further qualify the service messages.

<a id="documentation-overview--service-extension-and-versioning"></a>

## Service Extension and Versioning

The Etch system is designed so that service descriptions may be extended or revised in ways that don't invalidate existing clients or servers. The rule is that changes following reasonable design disciplines do not invalidate the existing clients and servers.

Etch does not formally define service versioning because versioning is too often idiomatic to a service or organization. At the same time, versioning is too blunt a tool and artificially increases the difficulty of deploying compatible system upgrades. The best practice is to be disciplined about changes to the service description and to provide interfaces to query feature availability (a la ODBC / JDBC, SMTP, POP, etc.)

<a id="documentation-overview--fundamental-data-types"></a>

## Fundamental Data Types

Etch includes support for the fundamental data types which appear in many processor architectures and databases: boolean, byte, short, int, long, float, double, and string. The integral values are all signed, with size from 1 to 8 bytes. The floating point values are all typically IEEE compatible, with size from 4 to 8 bytes. The string value is Unicode, with no specified length limit.

Etch also supports arrays of any supported data type. The arrays may have one or more dimensions. The arrays conform to the Java style or jagged arrays.

In addition, Etch supports the **object** data type which is used to model a parameter or result where the actual type is determined at runtime. An object type specification my be used anywhere a native data type is allowed except when declaring constants.

<a id="documentation-overview--extended-data-types"></a>

## Extended Data Types

Etch supports the definition of enumerated types. The enumerations are mapped by name, not by any particular value or order.

Etch also supports the definition of structs and exceptions, which are very similar to message definitions (name, list of typed fields), although of course structs and exceptions do not have return values and cannot themselves throw exceptions.

<a id="documentation-overview--external-data-types"></a>

## External Data Types

Etch allows native language data types to be imported and used within the service definition. All that is needed is to give the type a name in the service description, then for each desired target language to nominate a type which carries the same semantics (java.util.Date in Java, System.DateTime in C#, Time in Ruby). A specific class which will perform the work of serializing and de-serializing the object must also be implemented per target language.

<a id="documentation-overview--named-constants"></a>

## Named Constants

Etch allows the definition of named constants of the fundamental data types. These do not appear in the protocol per se, but are copied into the generated files and are available to all target programming languages.

<a id="documentation-overview--implementation-details"></a>

## Implementation Details

The Etch compiler generates for each target language meta-data defining the types and fields of your service, interface files which define the messages, structs, enums, exceptions, external data, constants, and other NSDL elements, and then code to support turning method (or, function) calls into message sends (the remote implementation) and code to support turning messages received back into method calls (the stub implementation).

The compiler is implemented in Java and uses Velocity templates to generate the code. Thus the compiler is available to use on any Java enabled platform, although of course Java is not needed once the NSDL is compiled unless your application is written in Java. Once compiled, all your application need do is to link with the small Etch runtime written (more than likely) in the target programming language.

<a id="documentation-overview--binary-transport"></a>

## Binary Transport

The current Etch system includes a production-ready, compressed binary tagged message format with TCP and UDP transports, and a non-production ready XML transport in Java as an example. The binary transport includes a tag for every data element which describes the size and type (i.e., 4 byte integer stored as 1 byte). Struct types and fields are encoded as a 32-bit hash of the name. This saves space in the wire format over sending the complete names. The maximum size of the add message defined above is 49 bytes, including an 8 byte packet header and 8 byte message ID (but not IP / TCP header).

<a id="documentation-overview--footprint"></a>

## Footprint

The Java implementation of the Etch runtime needed to support a service using the compressed binary tagged message format over TCP without encryption is 288k (compressed jar file).

<a id="documentation-overview--performance"></a>

## Performance

Performance numbers are always tricky and subjective because so much depends upon the context of the test. That said, we have gone through the exercise of contrasting various messaging technologies against one another. In this test, we implemented the add function shown above in Etch (Java language binding), Apache Axis2 SOAP web service, JAX SOAP web services, Thrift (Java), and CORBA (Java):

| **System** | **Calls/Second** |
| --- | --- |
| Etch Java | 13.3k |
| Thrift Java | 13.5k |
| Java RMI | 7.4k |
| CORBA Java | 2.4k |
| JAX-WS | 943 |
| Apache Axis2 | 206 |

<a id="documentation-overview--roadmap"></a>

## Roadmap

A Python binding and some form of browser-Javascript binding have been implemented in first versions, but are not yet ready.

We plan to build a language binding for web services such than an Etch NSDL may be accessed and / or deployed as a web service. This would allow easy migration of clients and / or servers to use Etch natively while maintaining backwards compatibility with existing systems.

---

<a id="documentation-setup-guide-for-users"></a>

<!-- source_url: https://etch.apache.org/documentation/setup-guide-for-users.html -->

<!-- page_index: 31 -->

<a id="documentation-setup-guide-for-users--getting-started-documentation-for-upcoming-release-1.1"></a>

# Getting Started documentation for upcoming Release 1.1

<a id="documentation-setup-guide-for-users--binary-distribution"></a>

## Binary Distribution

The top-level structure of the install image is:

```

  ChangeLog.txt
  DISCLAIMER.txt
  LICENSE.txt
  LICENSE_THIRD_PARTY.txt
  NOTICE.txt
  NOTICE_THIRD_PARTY.txt
  README.txt
  RELEASE_NOTES.txt
  bin/
  examples/
  lib/
  binding-c/
  binding-csharp/
  binding-java/
  uninst.exe (for windows use only)
```

Please take a moment to review the RELEASE\_NOTES.txt, ChangeLog.txt and
LICENSE.txt files.

The Windows installer (apache-etch-1.1.0-incubating-setup.exe) has created a
user environment variable (ETCH\_HOME) which points to the Etch installation
directory. If you installed Etch using either

apache-etch-1.1.0-incubating-windows-x86-bin.zip

or

apache-etch-1.1.0-incubating-linux-x86-bin.tgz

you will want to create this environment variable yourself:

windows:

```

  set ETCH_HOME=C:\Program Files\Apache Software Foundation\apache-etch-1.1.0
```

\*nix:

```

  export ETCH_HOME=/path/to/apache-etch-1.1.0
```

The bin directory has also been put on your path by the Windows installer. If
you are using the archives, you will need to do this yourself:

windows:

```

  PATH %PATH%;%ETCH_HOME%\bin
```

\*nix:

```

  export PATH="$PATH:$ETCH_HOME/bin"
```

The bin/ directory contains a Windows bat script and a unix shell script.

You will also need to have a java runtime installed (later versions of sun jre
or jdk 1.5 or any version of 1.6 or later). A JAVA\_HOME environment variable
should point to the installation directory of the java runtime. If you are going
to compile java source you will need the jdk.

After the installer has been run and the environment setup, at a windows
command line or shell prompt, you should be able to run the etch compiler and
see some basic output:

windows:

```

  C:\>etch -v
  Etch version is Apache Etch 1.1.0-incubating (some build info)
```

unix:

```

  bash-3.2$ etch -v
  Etch version is Apache Etch 1.1.0-incubating (some build info)
```

The lib directory contains the various jar files for the compiler and the Apache Velocity dependency jar:

```

  apache-etch-java-compiler-1.1.0-incubating.jar
  apache-etch-java-compiler-1.1.0-incubating-src.jar
  ...
```

The top level folders binding-c, binding-java and binding-csharp contain the language specific
runtime libraries:

<a id="documentation-setup-guide-for-users--binding-for-java"></a>

## Binding for Java

binding-java is organized as follows:

```

  apache-etch-java-runtime-1.1.0-incubating-src.zip
  lib/
    apache-etch-java-runtime-1.1.0-incubating.jar
```

The generated java source from the etch compiler needs apache-etch-java-runtime-1.1.0-incubating.jar.
There is source code to go with it in apache-etch-java-runtime-1.1.0-incubating-src.zip.

<a id="documentation-setup-guide-for-users--binding-for-c"></a>

## Binding for C#

binding-csharp is organized as follows:

```

  apache-etch-csharp-runtime-1.1.0-incubating-src.zip  
  lib/
    ApacheEtchCsharpIncubating.dll
    ApacheEtchCsharpIncubating.pdb
```

The generated c# source from the etch compiler needs ApacheEtchCsharpIncubating.dll
The C# (.NET 2.0 and later) ApacheEtchCsharpIncubating.dll should be added to any C# projects.
There is source code to go with it in apache-etch-csharp-runtime-1.1.0-incubating-src.zip.

<a id="documentation-setup-guide-for-users--binding-for-c-2"></a>

## Binding for C

binding-c is organized as follows:

```

  bin/
    apr-1-config		(on linux)
    apriconv			(on linux)
  include/
    [etch-*].h			(on win32)
    apr-1			(on linux)
  lib/
    etch.lib			(on win32)
    etch.pdb			(on win32)
    libetch.a			(on linux)
  extern/
    apr/
      bin/
        libapr-1.dll		(on win32)
        libapr-1.pdb		(on win32)
        libapriconv-1.dll	(on win32)
        libapriconv-1.pdb	(on win32)
      iconv/
        [iconv*]-stuff
      include/
        [apr-*].h
      lib/
        libapr-1.lib		(on win32)
	libapriconv-1.lib	(on win32)
	libapr-1.so		(on linux)
	libapriconv-1.so	(on linux)
  apache-etch-c-runtime-1.1.0-incubating-src.zip
```

Generated C source depends on the dlls/so/a/h files mentioned above. The best choice to
build generated code using the c binding is cmake. You can use the examples/helloworld
example as a reference. The C binding has external dependencies to the Apache Portable
Runtime (APR). We ship dll/so/h for the apr in the extern folder. There is source code
to go with it in apache-etch-c-runtime-1.1.0-incubating-src.zip

<a id="documentation-setup-guide-for-users--ant-plugin"></a>

## Ant Plugin

There is an ant plugin which you can use with ant 1.7.0 or later to invoke the
compiler as a task. It is documented on the wiki referenced above. You can also see examples
of its usage in the build.xml files in the examples folder

<a id="documentation-setup-guide-for-users--maven"></a>

## Maven

If you are using maven, then you might want to install the Etch artifacts into
your local maven repository. There is a Windows bat script to do this in the
maven directory:

etch-maven-install.bat

You need to have maven on your path when you run this script. The file
etch-java-runtime-1.1.0.jar will be installed into your local repository with
group "etch.etch", artifact id "etch-java-runtime", and version "1.1.0". You
may then reference Etch from your maven projects.

<a id="documentation-setup-guide-for-users--python-and-xml-bindings"></a>

## Python and XML Bindings

The source distribution includes code to support XML and python bindings, but
these bindings are not yet complete, and there is no build products associated
with those. They are mainly there to 1) capture the code contribution from
cisco systems, and 2) inspire any fence sitters, ah, helpers to jump in and
contribute.

<a id="documentation-setup-guide-for-users--examples"></a>

## Examples

Examples have been provided in the examples/ subdirectory. Start with the HelloWorld
example, it contains code for all three language bindings. There is a readme
file in each example's directory which explains how to build and run it.

<a id="documentation-setup-guide-for-users--tests"></a>

## Tests

Unit tests can be had by checking out the source code from the subversion
repository and performing a complete build:

<http://svn.apache.org/repos/asf/etch/releases/release-1.1.0-incubating>

<a id="documentation-setup-guide-for-users--help"></a>

## Help

For help, see the wiki or send email to user@etch.apache.org. See
RELEASE\_NOTES.txt for specific information for this release.

---

<a id="roadmap-architecture-message-size"></a>

<!-- source_url: https://etch.apache.org/roadmap-architecture-message-size.html -->

<!-- page_index: 32 -->

<a id="roadmap-architecture-message-size--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="roadmap-architecture-message-size--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="roadmap-architecture-message-size--apache-etch"></a>

# Apache Etch

<a id="roadmap-architecture-message-size--transfer-of-big-messages"></a>

# Transfer of Big Messages

During the development of etch, it was thought to be useful that the generated interfaces should be able to support more than one request outstanding at a time. Some requests might be very quick, some might take a long time. Normally requests are processed sequentially by the message reader thread. Etch offers options to manage long running requests while maintaining reactivity for quick requests made from another thread. This involves marking some requests to be dispatched to a thread pool, allowing the message reader thread to go back and process another request.

Both requests and responses are messages with identical structure. So, the transport layers are not about requests and responses, they are about messages. The name of the game is moving messages from here to there. Each direction (towards client, and towards server) are more or less independent. Messages sent are generally transmitted using the thread which originated the message. While a message is being transmitted, another thread also wanting to transmit a message must wait. On the receiving end there is a dedicated message receiver thread which reads one message at a time and dispatches it to a handler. So you can see, the wire, the medium of message transmission, can only be used by one thread at a time.

Now suppose there is a request which returns a big response. Other messages will be blocked waiting for the big message to pass over the wire. So big messages reduce our reactivity.

For example, a 10 kb message over 100 megabit link takes 1 ms to transit the link (assuming no hops). So another message behind that one will experience up to a 1 ms delay just for transit. But if the first message is 10 mb then the second message will experience a 1 s delay for transit. These numbers can be much worse when you consider multiple hops, congestion, etc.

Another issue with big messages is that they consume big memory while being processed. This is because the entire message must be buffered up before it can be parsed and delivered. This causes issues within the heap and also within a server which has perhaps thousands of clients. A common denial of service attack is to open a connection to the server, send all the data of a request except the last byte. Open another connection, repeat. Soon the server will be out of memory and all processing will stop.

If a server allows up to 1 mb messages, then if I open 1,000 connections and send 999,999 bytes of a 1,000,000 byte message to each one, I've soaked up 1 gb of memory on the server.

<a id="roadmap-architecture-message-size--possible-solutions"></a>

## Possible Solutions

- Don't allow big messages
- Don't send big messages
- Break up big messages
- Incrementally parse messages
- Timeout partial messages

<a id="roadmap-architecture-message-size--dont-allow-big-messages"></a>
<a id="roadmap-architecture-message-size--don-t-allow-big-messages"></a>

### Don't allow big messages

Etch currently enforces a limit on the size of messages. The default value is around 16k. This limit can be adjusted. By keeping this number as small as is reasonable, you limit the impact of a denial of service attack.

<a id="roadmap-architecture-message-size--dont-send-big-messages"></a>
<a id="roadmap-architecture-message-size--don-t-send-big-messages"></a>

### Don't send big messages

This might seem easy, and it is a good idea to try, but it isn't always possible. The idea is to not request large blobs, rather to incrementally request smaller pieces. I'll give a couple of examples.

<a id="roadmap-architecture-message-size--reading-a-file"></a>

#### Reading a file

You're trying to read a file over the network. Read 8k bytes at a time instead of the whole file. Because etch allows multiple requests to be outstanding at once, you can even use a double buffering scheme to make it nearly as fast as one single request. Here is an example of single buffering:

```
String id = server.openFileForRead( "blah.jpg" ); beginRead(); try {byte[] buf; while ((buf = server.readFile( id, 8192 )).length > 0) processData( buf );} finally {endRead(); server.closeFileForRead( id );}
```

<a id="roadmap-architecture-message-size--database-query"></a>

#### Database query

Instead of reading hundreds or thousands of rows from a table, read a few rows at a time. Most databases support the notion of indexed result sets, so this can be pretty efficient. The server also has the option of caching the query result vs. rerunning the query. There might be issues with concurrent updates, beware.

```
int index = 0;
List rows;
while ((rows = server.query( "select * from foo", index, 20 )).size() > 0)
{
    processRows( rows );
    index += rows.size();
}
```

The second and third parameters to query are the offset into the result set and the count of items to return.

<a id="roadmap-architecture-message-size--break-up-big-messages"></a>

### Break up big messages

Sometimes it isn't possible for us at the api level to break up a big message. It might have deep structure which would be difficult to handle incrementally.

We could automatically break a big message up into smaller chunks, then send each chunk as a separate sub-message, then reassemble them on the other end. Other messages could slip in between and reactivity would be preserved.

We still have the denial of service problem whereby n-1 of our chunks have arrived. It is compounded because now we could also have many partial messages being buffered. How long do we hold a partial message before give up?

<a id="roadmap-architecture-message-size--incrementally-parse-messages"></a>

### Incrementally parse messages

Etch currently buffers up all the bytes of a message in a single large buffer before de-serializing it. The resulting single large buffer can constipate the heap. It also requires twice the storage, or more, to de-serialize a message, as we must de-serialize the entire message before we can free the buffer. If messages were buffered in chunks and parsed incrementally, buffers which have already been parsed may be discarded back to the heap sooner. Less constipation, and nearly half the storage requirement.

<a id="roadmap-architecture-message-size--timeout-partial-messages"></a>

### Timeout partial messages

A timeout mechanism on a connection should always be used. Etch's KeepAlive filter works for this. If the connection fails to make progress and the pipes become jammed, the connection should be closed and any partial buffers discarded. Where partial messages are allowed to exist, some perhaps similar mechanism needs to test for their presence and shutdown the connection if they get to be too old (because it is a denial of service attack).

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="roadmap-architecture-transport"></a>

<!-- source_url: https://etch.apache.org/roadmap-architecture-transport.html -->

<!-- page_index: 33 -->

<a id="roadmap-architecture-transport--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="roadmap-architecture-transport--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="roadmap-architecture-transport--apache-etch"></a>

# Apache Etch

<a id="roadmap-architecture-transport--connection-lifecycle-at-the-transport-stack"></a>

# Connection Lifecycle at the Transport Stack

The Transport Stack is the framework which ties together the various pieces of the etch architecture within a binding. It also is the key to binding implementation consistency and to deploying cross platform services with the features we want.

Before going any further, please study the Transport Stack [Architecture](https://cwiki.apache.org/ETCH/architecture.html). Here are some proposals which affect the model of the transport stack.

<a id="roadmap-architecture-transport--auto-start-reconnect-and-idle"></a>

## Auto Start, Reconnect, and Idle

When a client connects to a service it may use one of two models. The first is the temporary (acute) need model, the second is the continuous (chronic) need model.

<a id="roadmap-architecture-transport--temporary-need-model"></a>

### Temporary Need Model

The temporary need model is based on the idea of occasionally needing one service or another to satisfy an immediate concern, such as a database query. Processing cannot continue until the need is satisfied:

```
... oops, need a service ...
server = BlahHelper.newServer( ... );
server._startAndWaitUp( 4000 );
answer = server.doSomethingForMe( ... );
server._stopAndWaitDown( 4000 );
server = null;
... further work.
```

When the service is not in active use it is stopped and does not consume any resources. There is no particular dependence upon the state of a continuously existing connection.

While straightforward, this model has a few warts. Once the service is started it must be stopped to correctly release the resources. Any exception thrown which might prevent \_stopAndWaitDown from being called must be neutralized, else a dangling server object is left connected. Let's fix the code to account for this:

```
... need some service ...server = BlahHelper.newServer( ... ); try {server._startAndWaitUp( 4000 ); answer = server.doSomethingForMe( ... );} finally {server._stopAndWaitDown( 4000 ); server = null;} ... further work.
```

Another wart occurs when there are closely spaced back to back needs for the service. The service is started and stopped only to be started again shortly. This is wasteful of resources on both ends of the connection, both in the creation of the object to manage the session and also in the network resources required to establish the connection

There are a few things we can do. Instead of creating and destroying the service stack on demand we could create one instance, only starting and stopping it as needed. This removes the need to have any of the parameters to newServer handy, one only needs to pass around server (or put it in a global):

```
... need some service ...try {server._startAndWaitUp( 4000 ); answer = server.doSomethingForMe( ... );} finally {server._stopAndWaitDown( 4000 );} ... further work.
```

This introduces a problem, though, which is one of shared access. If any other thread might also desire access via server, we have to block it until we are done:

```
... need some service ...synchronized (server) {try {server._startAndWaitUp( 4000 ); answer = server.doSomethingForMe( ... );} finally {server._stopAndWaitDown( 4000 );}} ... further work.
```

This is better, but we're still starting and stopping a connection, perhaps to start and stop it again soon. Also we are blocking other uses of service when we might not need to. Wouldn't it be cool if the connection would start automatically if it was down and we made a request, and if after a period of inactivity it would stop automatically. Then we could just write this:

```
... need some service ...
answer = server.doSomethingForMe( ... );
...further work.
```

Now there is no need for the synchronize unless I'm going to make two back to back calls which must not be interrupted by any intermediate state changes (and all such calls must be similarly protected). Because the connection may go down between calls, there cannot be any dependence upon long term server statefulness. This applies even while we might have what we think of as a transaction going on:

```
... need some service ...
answer = server.doSomethingForMe( ... );
... dialog with the user ...
server.doSomethingElseForMe( ... );
... further work.
```

During the dialog with the user, the connection may automatically shut down because it is idle too long. The api doSomethingElseForMe cannot depend upon any state established by the api doSomethingForMe unless we somehow force the connection to stay up and block other simultaneous state changing requests.

```
... need some service ...synchronized (server) {try {server.transportControl( INCREMENT_IDLE_BLOCK ); answer = server.doSomethingForMe( ... ); ... dialog with the user ...server.doSomethingElseForMe( ... );} finally {server.transportControl( DECREMENT_IDLE_BLOCK );}} ... further work.
```

The idle block, while non-zero, blocks any automatic idle connection shut down. As you can see, we're almost back where we started. Better to use a stateless api here.

In summary, there were two concepts mentioned here which may be interesting: AutoStart and IdleStop. These are primarily interesting when used in combination with stateless apis.

<a id="roadmap-architecture-transport--initialization-of-otherwise-stateless-apis"></a>

#### Initialization of Otherwise Stateless APIs

A small note which might be helpful. While some apis are often easily rendered as stateless, some depend upon some initialization nonethess. An example is opening a connection to the Configuration service and then loading our assigned config resource. After that, we'd be good as the rest of the api is stateless.

We can achieve nirvana here if we realize that the session UP and DOWN messages can get us past this issue. When our session comes UP, we can immediately setup our initial state before any other requests are processed. This may require some changes to implement to a useful level of refinement, but that is easy.

<a id="roadmap-architecture-transport--continuous-need-mode"></a>

### Continuous Need Mode

This is the regular connection mode that keep up the service connection for a long time.

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="roadmap-concepts-nameservice-client"></a>

<!-- source_url: https://etch.apache.org/roadmap-concepts-nameservice-client.html -->

<!-- page_index: 34 -->

<a id="roadmap-concepts-nameservice-client--nameservice-client-details"></a>

# Nameservice Client Details

A typical etch client, which prefers a tcp transport starts itself up with the following set of operations:

```
String uri = "tcp://localhost:4004";
RemoteBlahClient server = BlahHelper.newServer( uri, null, factory );
server._startAndWaitUp( 4000 );
```

Here is the flow related to creating and starting a new server on the client end:

![Plain Connect](assets/images/etch-concepts-nameservice-plain-connect_7a147837b0a8d280.png)

<a id="roadmap-concepts-nameservice-client--naming-service-enhancement-what-changes"></a>
<a id="roadmap-concepts-nameservice-client--naming-service-enhancement:-what-changes"></a>

## Naming Service enhancement: What changes?

With the naming service under the hood, the only thing that changes would be the uri string itself. Rest of the operations remain the same. Of course, the old uri would work perfectly fine as before ensuring that the addition of Name Service capabilities are backward compatible.

```
String uri = "etch:etch.examples.perf.Perf/foo"
RemoteBlahClient server = BlahHelper.newServer( uri, null, factory );
server._startAndWaitUp( 4000 );
```

The following figure explains the flow:

![Nameservice Connect](assets/images/etch-concepts-nameservice-connect_440a50ed5fd97ddb.png)

The "target transport stack/factory" in the figure could be any target transport like TCP, TLS, etc. This distinction would be clear from the uri returned by the name service or through the uri specified by the user itself (for further details, please visit the main page).

<a id="roadmap-concepts-nameservice-client--dealing-with-disconnection"></a>

### Dealing with disconnection

There are three scenarios possible during a connection breakdown:

1. The application explicitly requests an end to the connection between itself and the target service. This will be of the form:


```
server._stopAndWaitDown( 4000 );
```

2. There is an unexpected disconnect between the application and the target service. In order to maintain the most up to date name translation, every time a disconnect occurs, the old target transport stack would be discarded and a new one be created (using the latest translation) which would be then used to reconnect. The flow associated with this process is shown below:

![Nameservice Disconnect](assets/images/etch-concepts-nameservice-disconnect_183614e2a258e3bc.png)

---

<a id="roadmap-concepts-nameservice-listener"></a>

<!-- source_url: https://etch.apache.org/roadmap-concepts-nameservice-listener.html -->

<!-- page_index: 35 -->

<a id="roadmap-concepts-nameservice-listener--nameservice-listener-details"></a>

# Nameservice Listener Details

An etch service has at its core some sort of listener for new sessions, possibly more than one. While the examples are tcp, any sort of transport will work. Here is a typical sequence of operations:

```
String suri = "tcp://0.0.0.0:4004";
Transport<ServerFactory> listener = PerfHelper.newListener( suri, null, factory );
listener.transportControl( Transport.START_AND_WAIT_UP, 4000 );
System.out.println( "listener ready" );
```

Listener is a short name for a listener transport stack. When the listener is issued the control "start", a tcp server socket is created, then a listen command is issued to the socket, then a thread is created to repeatedly call accept on the server socket and delivers any result to higher-levels of the listener transport stack. The higher levels take an accepted socket, wrap it in a session transport stack, and start the session. Thus a new connection is born. Once the listener thread is running, the listener's session is notified that the listener is "up" (the session is the top of the listener transport stack while the tcp server socket is the bottom).

Here is a diagram of the flow related to creating and starting a listener:

![Nameservice Listen](assets/images/etch-concepts-nameservice-plain-listen_7639f43589d7c03d.png)

<a id="roadmap-concepts-nameservice-listener--how-to-register-a-service"></a>

## How to Register a Service

One of our tenets is that we don't want to have to modify a service to cause it to be registered with a name service. First let's look at what sort of code we're trying to get rid of:

```
String nsuri = "tcp://ns:4002";
String name = "Perf/foo";
String curi = "tcp://foo:4004";

RemoteNameServiceServer server = NameServiceHelper.newServer( nsuri, null, factory );
server._startAndWaitUp( 4000 );
server.register( name, curi );
server._stopAndWaitDown( 4000 );
server = null;
```

This code would normally be inserted just after the message "listener ready" is printed. The result is that once the listener was up and ready, it would register itself with the name service, giving its assigned api and instance name (Perf/foo) and the uri that clients should use to attempt to connect. Omitted from this code is how the server authenticates with the name service. Also omitted is the loop wrapping the sequence from start to finish with a sleep inserted to periodically re-register the name in case the name service forgets.

<a id="roadmap-concepts-nameservice-listener--how-to-do-it-right"></a>

## How to Do It Right

In order to eliminate the code above we need to listen using a different transport (use etch: instead of tcp:) and supply enough information on the uri to allow the etch transport to register for us. Here is a listener uri which does this:

```
String suri = "etch:Perf/foo?ns=tcp://ns:4002&curi=tcp://foo:4004&suri=tcp://0.0.0.0:4004";
```

Use this with the code from the introduction to complete the task.

Here is a diagram of the flow related to creating and starting a listener with name service registration included:

![Nameservice Listen](assets/images/etch-concepts-nameservice-listen_9f7695d1c670c14b.png)

---

<a id="roadmap-concepts-nameservice"></a>

<!-- source_url: https://etch.apache.org/roadmap-concepts-nameservice.html -->

<!-- page_index: 36 -->

<a id="roadmap-concepts-nameservice--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="roadmap-concepts-nameservice--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="roadmap-concepts-nameservice--apache-etch"></a>

# Apache Etch

<a id="roadmap-concepts-nameservice--etch-nameservice"></a>

# Etch Nameservice

When an client is connecting to an etch service, a uri is used to specify the details of the connection. Likewise, a listener uses a uri to specify the details of the listening point. Typically this code looks something like thi

```
RemoteNameServiceServer server = NameServiceHelper.newServer(
    "tcp://host:4001?filter=KeepAlive&TcpTransport.reconnectDelay=4000", null, factory );
```

The uri specifies all the details of the etch connection in a convenient form. Yet the uri is still hard to manage. With it embedded in code we must recompile the client to change the connection details. We can load the uri from some other place, say a configuration file, environment variable, or the command line, but all we've done is move the problem to yet another hard to manage place. (Here 'manage' specifically refers to the process of obtaining the uri or updating it after a change.)

What can we do to make the uri easier to manage? The main issue is that the service implementation and deployment specifies what the uri should be. Any change to the service implementation or deployment could trigger a need to update the uri that clients use to connect to it. So, one fact (connection uri), one source (service implementation and deployment), but a delivery path which is not automatic and often includes a human. Can you imagine trying to update 30,000 clients with a new connection uri?

The classic solution applies here and represents the start of the next phase in etch development. Etch needs a Name Service.

<a id="roadmap-concepts-nameservice--the-basics"></a>

### The Basics

At its heart a name service is easy. We use them every day without really thinking about them. Given a simple but abstract identifier a more complicated but concrete identifier is produced by some sort of lookup. In exchange for the abstraction, we obtain some independence from the complicated details of the concrete identifier, allowing the concrete identifier to change as needed by the environment. For example, apache.org is translated into the internet protocol v4 address 140.211.11.131 for us by dns. My name, sccomer, is translated into a uid (1079) by my nearby Linux box and used for all sorts of evil purposes. In both cases I can use the simple name as a substitute for the more complicated name seamlessly in the environments I work in. Let's call the abstract identifier the source. Let's call the concrete identifier the target.

In order for the name service to be useful to me, I have to be able to depend upon and trust it. That is, the translation process needs to be available when I need it, and the translations need to be accurate and, most importantly, secure. By secure I mean that if I'm going to connect to a service and supply some credentials and use it to do my work, I have an expectation that the service itself is reliable and trustworthy. That it is not being spoofed. This translates into access controls limiting who can make changes to the underlying data used to implement the name service translation, safeguards to prevent the translation being modified in transit, and some assurance that I'm using the right name service instance.

<a id="roadmap-concepts-nameservice--the-requirements"></a>

### The Requirements

The following design principles are important to adhere to:

- A service or application should not have be overtly aware of the name service. It should be possible to deploy a service or application with or without the name service, with no conditional code or changes to code. Thus use of a name service is purely a deployment consideration and is not required.
- The name service should be supportable in a variety of styles or modes without changing the fundamental functional interface. Indeed, the basic contract should be very simple.

The name service should be defined using etch. Perhaps this is obvious but I'll say it here for completeness.

The source should be specified in a uri. This allows us to exchange the target uri for a source uri + name service api to achieve our goal.

The existing client framework would already be Naming Service ready, in the sense that, even with the old uri format, everything would work as it used to work before. This transparency allows the current clients to be completely forward compatible with the new Naming Service functionality underneath. Obviously, if the client decides to update the uri to the new uri (according to the Naming Service specifications), that would be supported too.

To implement the functionality of the name service we need to have these elements:

- An api to access the name translations, update them, etc.
- A mechanism to protect the name service api from unauthorized access.
- An etch connection scheme which uses the name service api to automate the translation process for the client, and the publishing mechanism for the listener.

<a id="roadmap-concepts-nameservice--source-format"></a>

### Source Format

Within a given name service database may be many entries offering the same (or, essentially the same) api, that is, etch service name (e.g., etch.examples.perf.Perf). This is just as it is for any other service available over the network (nfs file servers, smtp mail servers, jabber im servers, etc.). This suggests that the api might be useful as an organizational concept for the name service database.

Suppose we partition the name space into domains based on the api being offered. Within a given api domain, there may be a number of named instances. The instance name is used to uniquely identify a running instance of the service offering the api. There may be several ways to access an instance (called schemes in etch). The instance might offer tls and soap schemes, for example.

This suggests a three part name: api, instance, and scheme. We can combine the three parts into a single name by using the slash character as a separator. This gives the name a path-like quality and also allows it to be easily embedded in a uri:

```
api/instance/scheme
```

One obvious way to express api is to use the fully qualified service name of the etch idl. These names are composed of standard identifiers separated by periods (e.g., org.apache.etch.examples.perf.Perf).

The instance name and scheme should not contain the slash character for obvious reasons. Since we want to embed these in a uri, the instance name and scheme should not contain any other uri significant characters either. If we stick to the same format as the api, we still have a large and interesting name space to work with.

Since the scheme corresponds to a uri scheme name, then the same uri scheme syntax is required. This is pretty much a standard identifier.

This partitioning of the source name is not required, just a suggestion.

So, here is a fully specified source for the Perf service named foo with tcp scheme:

```
org.apache.etch.examples.perf.Perf/foo/tcp
```

<a id="roadmap-concepts-nameservice--name-service-api-details"></a>

### Name Service Api Details

Please see the accompanying [ns.etch](https://etch.apache.org/roadmap-service-configuration-idl.etch) file for specific api details and documentation.

<a id="roadmap-concepts-nameservice--etch-scheme"></a>

### Etch Scheme

An etch scheme is introduced to gain automatic access to the name service. This removes from most clients and listeners any burden relating to name service, and makes using a name service essentially transparent (i.e., no program changes are required).

Here's an example etch scheme:

```
etch:org.apache.etch.examples.perf.Perf/foo/tcp
```

This would connect to a name service, lookup the source, and then connect to the returned target. We did have some words here about alternative specifications, perhaps searching based on location, etc. This was felt to complicate the api and could be handled in a better way by a more sophisticated service implementation.

<a id="roadmap-concepts-nameservice--nameservice-client-and-listener-details"></a>

### Nameservice Client and Listener details

- Nameservice client details [more](#roadmap-concepts-nameservice-client)
- Nameservice listener details [more](#roadmap-concepts-nameservice-listener)

<a id="roadmap-concepts-nameservice--faq"></a>

### FAQ

<a id="roadmap-concepts-nameservice--which-name-service-is-used"></a>

#### Which name service is used?

The name service instance to be used might be configured in a number of ways:

- Via the source uri,
- Environment variable,
- Via web container, application resources, configuration file,
- Dhcp option (configures all clients within a subnet).

<a id="roadmap-concepts-nameservice--how-does-one-configure-the-name-service-instance-via-the-source-uri"></a>

#### How does one configure the name service instance via the source uri?

The name service instance uri can be directly embedded into the source uri as follows:

```
etch://<name_service_ip:port>/org.apache.etch.examples.perf.Perf/foo/tcp
```

The host portion of the uri would be taken to be the location of the name service instance. The problem with this approach is that it isn't a well-formed uri. An alternative that works better is this:

```
etch:org.apache.etch.examples.perf.Perf/foo/tcp?ns=<uri for the name service instance>
```

This technique gives more flexibility at the cost of having to escape all the special characters in the ns uri.

<a id="roadmap-concepts-nameservice--how-does-one-configure-the-name-service-instance-via-environment-variable"></a>

#### How does one configure the name service instance via environment variable?

Before the program is run, an environment variable would be defined which specified the uri of the name service. The name service code would know to look for that environment variable.

<a id="roadmap-concepts-nameservice--how-does-one-configure-the-name-service-instance-via-web-container-etc"></a>
<a id="roadmap-concepts-nameservice--how-does-one-configure-the-name-service-instance-via-web-container-etc."></a>

#### How does one configure the name service instance via web container, etc.

Many web containers have a mechanism for passing settings to a configured .war file. Alternatively, a specially named file in the path or a property in a configuration file would serve the purpose. It would be up to the installation / deployment process to set the appropriate value.

<a id="roadmap-concepts-nameservice--how-does-one-configure-the-name-service-instance-via-dhcp"></a>

#### How does one configure the name service instance via dhcp?

Many enterprise class dhcp servers support a lightweight option system associated with the network, scope, or host. One can query these options by broadcasting the request onto the local network and receiving a response. Common option requests are for subnet mask, router, dns servers, domain name, lease time, etc. An option number would have to be assigned, and then the name service instance uri value configured as appropriate for each dhcp server in the network. Option space may be limited, so this may not be practical. See RFC 2132.

<a id="roadmap-concepts-nameservice--can-name-service-be-partitioned-or-federated"></a>

#### Can name service be partitioned or federated?

Yes. The name space could have structure which suggests a hierarchy of name service instances serving various domains. A request to lookup or register a name not in the local domain could be routed to another name service instance for processing.

<a id="roadmap-concepts-nameservice--can-name-service-be-replicated"></a>

#### Can name service be replicated?

Yes. Using the subscribe feature, one name service could replicate the contents of another (in a publisher/subscriber fashion). Lookup could be satisfied locally, while register could flow through to the publisher or the relationship could be more symmetric.

<a id="roadmap-concepts-nameservice--if-i-connect-to-a-service-using-the-uri-etchfoobartcp-and-the-connection-goes-down-how-do-i-reconnect"></a>
<a id="roadmap-concepts-nameservice--if-i-connect-to-a-service-using-the-uri-etch:foo-bar-tcp-and-the-connection-goes-down-how-do-i-reconnect"></a>

#### If I connect to a service using the uri etch:Foo/bar/tcp and the connection goes down, how do I reconnect?

When a connection is brought up, the source is looked up to discover the target to connect to. If the connection goes down and is then brought up again, that lookup process must be repeated to ensure you are connection to the most current value of target for the given source.

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="roadmap-concepts-router"></a>

<!-- source_url: https://etch.apache.org/roadmap-concepts-router.html -->

<!-- page_index: 37 -->

<a id="roadmap-concepts-router--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="roadmap-concepts-router--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="roadmap-concepts-router--apache-etch"></a>

# Apache Etch

<a id="roadmap-concepts-router--etch-router"></a>

# Etch Router

An Etch client may connect to an Etch service to consume APIs that the service provides. The client may have to
maintain connections to multiple Etch services for the following purposes:

- The client wants to consume multiple set of unique API's, and each set is provided by a different Etch service
- There are multiple Etch services that are providing the same set of API, and the Etch client wants to connect
  to only one of them at a time, and use the others as a backup for high availability purpose.

To simplify the client side maintenance of multiple service connections, we'll implement a generic Etch service
component to sit as a middle man between Etch clients and the API providers ( the Etch servers ). Let's call this
an "Etch Router".

<a id="roadmap-concepts-router--basics"></a>

## Basics

Basically, an Etch Router itself is an Etch server - it has its own Etch IDL which defines APIs and data types that
it implements. Any an Etch client who wants to consume API services may connect to the Etch Router - as the router's
"client" - and then be registered as an "application" in the router. Any an Etch server who wants to expose its API
to the Etch router's "applications" may also connect to the Etch router - as the router's "client" too - and then be
registered as the Etch Router's "service plugin".

At the plugin's registration time, the Etch Router should be able to identify the set of the APIs that the plugin can
provide for service. A plugin may be registered either as a "singleton" plugin - i.e. the API set that this plugin
provides is unique within the router, and no other plugin is providing any duplicate API service - or, as a member
plugin of a plugin group - a plugin group may contain mutiple plugin members which all provide the same set of API
service and has a fixed strategy in terms of choosing a member for connection, such as failover or round-robin.

When registering an application, the Etch Router should also be able to identify the set of APIs that the application
wants to consume - so that it knows whether the currently registered plugins may satisfy the API requirements. The Etch
Router may map these identified APIs to one or multiple "singleton plugin" or "plugin group"'s that provide the service.
Then the Etch Router will establish a dedicated client connection to each of the plugin or plugin members for this
registered application. The Etch router will maintain these connections for the application: when the application shuts down
its connection to the router, the router will shut down the dedicated connections to the plugins for that application as well.
When a plugin shuts down its connection to the router, all its associated connections that the router creates for the registered
applications will be cleaned up and another connection to a plugin member in the same plugin group (if available) will be
established for each of the applications, and the affected applications will be notified of this change as well.

On the application side, the Etch Router may be the only Etch server that the application connects to during its life time.
As long as the initial registration is successful, it may call the Etch router to consume any API that it claims during Etch
router registration, and doesn't have to know whether those APIs are provided by the same or different plugins, or whether the
connections to the plugins has been re-mapped down the road.

<a id="roadmap-concepts-router--implementation-details"></a>

## Implementation Details

A prototype implementation of this Etch-Router has been checked in at [here](http://svn.apache.org/repos/asf/etch/branches/router/services/router/)

<a id="roadmap-concepts-router--the-plugins-folder-in-etch-routers-home-directory"></a>
<a id="roadmap-concepts-router--the-plugins-folder-in-etch-router-s-home-directory"></a>

### The "plugins" folder in Etch-Router's Home Directory

When the Etch-Router (a Java Etch service) is starting up, it tries loading sub-directories under "plugin" folder in its home - the full path name of the "plugins" directory is configurable in the EtchRouter.properties file, by the property named "plugins.root.dir". Each sub-directory under this "plugins" folder is treated as a profile directory of a named "plugin group" - it usually contains two files:

- One XML binding file compiled from a typical service plugin's Etch IDL - this identifies the set of types and API's that the plugin implements.
- A properties file named metadata.txt - the content of this file may look like:


```
plugin.group.type=roundrobina
plugin.member.url.no1=tcp://127.0.0.1:4001
plugin.member.metadata.no1=location\=LA
plugin.member.url.no2=tcp://127.0.0.1:4002
plugin.member.metadata.no2=location\=LA&language\=French
```

  This file defines the type of plugin group (currently "roundrobin" and "failover" are supported), and the URLs of the plugin members, or the Etch services that are providing API services defined by the XML binding. Additionally, each plugin member's service may also be marked with one or multiple properties via the "plugin.member.metadata." property.

The Etch-router will create one "plugin-group" object for each sub-directory under "plugins" and map all the methods defined in the directory's XML binding file to this named plugin-group.

<a id="roadmap-concepts-router--plugin-group-monitor"></a>

### Plugin-group Monitor

While the Etch-router is running, for each plugin-group that it has loaded, the router will monitor the "up and down" status of each plugin member by establishing a client connection to each member service URL defined in the group's metadata.txt file.

<a id="roadmap-concepts-router--client-connections-and-api-method-mapping"></a>

### Client Connections and API Method Mapping

Any an etch application may connect to the Etch-router service as an ordinary Etch service - it then may consume any an API method defined in any one of the router's plugin-group XML binding file. On the etch-router side, in the transport stack for each application client connection, a special "EtchRouterFilter" is added to intercept each message sent between the client and the service: if the message is a API method call sent from application client, by looking at the message ID, the router will know which plugin-group has the implementation of the method - then it will find out whether a dedicated client connection has been established to a live member service of the mapped plugin-group for the application client connection. If yes, then it will forward this message to that service connection channel, otherwise, it will ask the mapped plugin-group to create a new service connection to one of its live members (here roundrobin or failover strategy may be adopted to decide which member to choose) and book keep that mapping information for later reference.

So for each application client connected to the etch-router, the router may book keep several client connections to the plugin member services. When the application client disconnects, the router will clean up the corresponding plugin member connections associated to the application client; when any one of the plugin member connection is down, the router will ask the plugin group to re-establish another connection and maintain it for the same application client.

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---

<a id="roadmap-service-configuration"></a>

<!-- source_url: https://etch.apache.org/roadmap-service-configuration.html -->

<!-- page_index: 38 -->

<a id="roadmap-service-configuration--2016-12-13-apache-etch-has-been-retired."></a>

# 2016/12/13 - Apache Etch has been retired.

<a id="roadmap-service-configuration--for-more-information-please-explore-the-attic-."></a>

## For more information, please explore the [Attic](http://attic.apache.org/).

[![Apache Etch](assets/images/etch-logo_e7ea9915e2ba2c29.png)](#index)
<a id="roadmap-service-configuration--apache-etch"></a>

# Apache Etch

<a id="roadmap-service-configuration--configuration-service"></a>

# Configuration Service

The configuration service (and corresponding local components) allow for remote administration of a service or client. This remote administration is essential for enterprise deployments. The template main programs that etch creates for you have configuration information (service and listener uris) built into the code. If you go too far down this path then your programs will be hard to deploy as they will need to be recompiled to change settings. There is a natural evolutionary path often taken:

- Embedded code
- Command line (or plugin properties)
- Local configuration file
- Remote configuration file or database

At each level above we are trading off convenience for manageability. The last level is the most manageable for the operators, while the first level is the most convenient for the programmers.

The best practical systems often use a combination of the above techniques to achieve the goals of the project.

Another direction taken on configuration is whether the configuration information is static or dynamic. Static information is fixed once the program starts, dynamic configuration can change while the program is running. Consider a running service listener with some configured information for the listener uri and also the names, passwords, and other information for the users. Suppose it is statically configured. Some user information needs to be updated. The service must be stopped, the configuration updated, and the service started again. During that time the service is unavailable, and sometimes work in progress when the service went down is lost. Dynamic configuration would have allowed that service to remain available while the information was being updated.

<a id="roadmap-service-configuration--requirements"></a>

## Requirements

One of the goals of a configuration service should be to not make things so inconvenient for the programmers that the technique is abandoned. There are several ways that configuration interferes with programmers:

- The act of adding a new configuration item is burdensome.
- Development is hindered by requirement of using an external service.
- Different interfaces for local vs. remote configuration.
- Different interfaces for various languages.
- Parsing and checking configuration values.

From these we can come up with some requirements:

- Same api for local and remote configuration.
- Same api for various languages.
- Minimal information needed to get started during development.
- Self-contained / standalone development experience.
- Api delivers required data type.

Some other requirements come from extant ideas for configuration. XML brought us structured documents and this is perfect for configuration information as well. XML makes a lousy configuration medium because it is syntactically complex. Yaml has the advantage of being much simpler and just as powerful. Property files and command lines are initially easy but have no structure and run out of gas fast. Databases are good for structured data but are very complex to setup and use. File systems are nice and have a structured model but are perceived as heavyweight and difficult to manage. Let's go with yaml for a bit and see what we can use. Here's an example yaml file:

```
listenerUri: tcp://realty.net:4001
users:
    mary: { birthday: 1959-10-01, zip: 94001, pw: zowie1, active: true, interest: [ home, condo, apartment ] }
    jake: { birthday: 1967-01-19, zip: 78759, pw: flak33, active: false, interest: [ commercial ] }
```

Ok, we can see (or guess) the following:

- Structured organization (scalars, maps, lists)
- Easy syntax
- Simple scalar data types (boolean, integer, real, strings, dates)
- Easily supported in a variety of languages.

(I'm taking a subset of the possible yaml capabilities, ignoring references and complex language dependent data types.)

(Note that, while I'm talking about yaml, that I'm using it as a programmer friendly model.)

The data types supported by yaml match etch capabilities as well. So, let's call these a requirement.

- Data types supported include boolean, integers, reals, strings, dates, maps, sets, and lists.

In the example above, we see that users is a map with two elements, mary and jake. Mary (and jake) is a map with 5 elements. We can think of maps (and lists and scalars) as nodes in a directed acyclic graph, with maps and lists containing more nodes within and scalars only having values. If I have my finger on the node users, I can reference mary's birthday by using the path "mary/birthday". I could also globally reference jake's password as the path "/users/jake/pw". The second of mary's interests could be referenced as the path "interest/1" with value condo. This naming scheme looks like a file system or network db, and so it is.

- Configuration data is organized into a directed, acyclic graph of nodes. Each node has a unique id and is either a map, a list, or a scalar value. Each node has a single parent. Each node has a unique name relative to its parent, and a unique path of names relative to the root node.

This allows us to treat subtrees of the configuration data generically, such as the subtrees "users/mary" and "users/jake" which are each "a user". By this abstraction we can write code which maps configuration data onto objects.

Some generic operations are suggested for nodes:

- getParent, getName, getIndex, getPath, isRoot, isList, isMap, size

These operations work for all nodes. Given a node id, they return the appropriate property.

For nodes which are maps or lists, we need to be able to list the children:

- listConfigIds

Given a node id, lists the children of this node. A node id list is returned.

For nodes which are maps or lists, we need to be able to get a specific named (or indexed) child:

- getConfigPath, getConfigIndex

Given a node id and a path or index, gets the node id of the specified child node.

For nodes which are scalars, we need to be able to get the value:

- hasValue, getBoolean, getInteger, getDouble, getString, getDate, getMap, getList, getSet

The operation hasValue tests to see if the value is present, the get operations return the value as the requested data type if it is or can be converted to that type.

For convenience, the value getting operations include three extra methods: getMap, getList, and getSet. These take structural nodes and return them as best effort mappings into local equivalents of the raw underlying data. You lose the data conversion capabilities of the scalar access methods (getBoolean, etc.).

<a id="roadmap-service-configuration--example"></a>

## Example

Here is a code snippet to access a mary's birthday:

```
java.util.Date bd = service.getDate( service.getConfigPath( service.getRoot(), "users/mary/birthday" ) ) );
```

That's a bit of typing, eh? Generally you'd cache the value of root in a variable, and let's add a convenient operation to get a value given a node and a relative path without having to handle the node id ourselves:

```
Object root = service.getRoot();
...
java.util.Date bd = service.getDatePath( root, "users/mary/birthday" );
```

<a id="roadmap-service-configuration--complete-configuration-idl"></a>

## Complete Configuration IDL

Now, this interface I've defined, it includes only operations to access the configuration values, not change them. I've done it this way on purpose, so that we can quickly get started with a variety of sources and ignore the actual implementation. This interface could, in fact, be implemented in a variety of ways, including file system, network or relational db, property file, yaml file, xml file, command line, or environment variables. Where a particular service supports modification, it would perhaps require a specialized api for that. So, you'd define that api, mixin this basic access api, and that's your service. Clients (of the service) that only need to access the data would use just this basic access api.

I've not discussed operations relating to noticing updates (however accomplished). I'll catch up to that later. But they are in the access api. Here is a complete etch service [idl](https://etch.apache.org/roadmap-service-configuration-idl.etch).

Copyright © 2013 The Apache Software Foundation, Licensed under
the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
Apache and the Apache feather logo are trademarks of The Apache Software Foundation.

---
