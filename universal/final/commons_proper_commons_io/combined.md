# Project Information

## Navigation

- Commons IO
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Users guide](#description)
  - [Best practices](#bestpractices)
  - [Building](#building)
  - [Proposal](#proposal)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-io"></a>

# Apache Commons IO

Apache Commons IO is a library of utilities to assist with developing IO functionality.

The Commons IO packages include:

- [io](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/package-summary.html)
  - This package defines utility classes for working with streams, readers, writers and files.
- [build](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/build/package-summary.html)
  - This package provides classes to implement IO builders.
- [charset](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/charset/package-summary.html)
  - This package provides classes to work with code from `java.nio.charset`.
- [comparator](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/comparator/package-summary.html)
  - This package provides various Comparator implementations for Files and Paths.
- [file](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/file/package-summary.html)
  - This package provides extensions in the realm of java.nio.file.
- [file.attribute](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/file/attribute/package-summary.html)
  - This package provides help using `java.nio.file.attribute` types.
- [file SPI](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/file/spi/package-summary.html)
  - This package provides extensions in the realm of `java.nio.file.spi`.
- [filefilter](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/filefilter/package-summary.html)
  - This package defines an interface (IOFileFilter) that combines both FileFilter and FilenameFilter.
- [function](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/function/package-summary.html)
  - This package defines IO-only related functional interfaces for lambda expressions and method references.
- [input](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/input/package-summary.html)
  - This package provides implementations of input classes, such as InputStream and Reader.
- [input.buffer](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/input/buffer/package-summary.html)
  - This package provides implementations of buffered input classes, such as CircularBufferInputStream and PeekableInputStream.
- [monitor](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/monitor/package-summary.html)
  - This package provides a component for monitoring file system events (directory and file create, update and delete events).
- [output](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/output/package-summary.html)
  - This package provides implementations of output classes, such as OutputStream and Writer.
- [serialization](https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/serialization/package-summary.html)
  - This package provides a framework for controlling the deserialization of classes.

<a id="index--releases"></a>

# Releases

<a id="index--latest-release-java-8-and-up"></a>

## Latest Release (Java 8 and up)

Commons IO requires a minimum of Java 8 -
[Download now](https://commons.apache.org/io/download_io.cgi)
.

View the
[Release Notes](https://commons.apache.org/proper/commons-io/changes.html)
and
[Javadoc API documents](https://commons.apache.org/proper/commons-io/apidocs/index.html)
.

<a id="index--previous-releases"></a>

## Previous Releases

See the
[download archive](https://archive.apache.org/dist/commons/io/)
and
[Javadoc archive](https://javadoc.io/doc/commons-io/commons-io/)
.

The Java platform requirements are:

- Version 2.7 and up requires Java 8 or above.
- Version 2.6 requires Java 7 or above.
- Version 2.3 through 2.5 requires Java 6 or above.
- Version 2.2 requires Java 5 or above.

<a id="index--support"></a>

# Support

The
[commons mailing lists](https://commons.apache.org/proper/commons-io/mail-lists.html)
act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [io].

Issues may be reported via
[ASF JIRA](https://commons.apache.org/proper/commons-io/issue-tracking.html)
.
Please read the instructions carefully to submit a useful bug report or enhancement request.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-io.git/commons-io
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch rel/commons-io-2.22.0 https://gitbox.apache.org/repos/asf/commons-io.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/commons-io-2.22.0 https://gitbox.apache.org/repos/asf/commons-io.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/security.html -->

<!-- page_index: 3 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html)
.

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the
public
[user mailing list](https://commons.apache.org/proper/commons-io/mail-lists.html)
.

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report
them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

<a id="security--cve-2024-47554"></a>

## CVE-2024-47554

- CVE-2024-47554: Uncontrolled Resource Consumption vulnerability in Apache Commons IO.
- Severity: Low
- Vendor: The Apache Software Foundation
- Versions Affected: Apache Commons IO 2.0 before 2.14.0.
- Description: The org.apache.commons.io.input.XmlStreamReader class may excessively consume CPU resources when processing maliciously crafted input.
- Mitigation: Users are recommended to upgrade to version 2.14.0 or later, which fixes the issue.
- Credit: CodeQL (tool).

<a id="security--safe-deserialization"></a>

# Safe Deserialization

For information about safe deserialization, please see [Safe Deserialization](https://commons.apache.org/io/description.html#Safe_Deserialization).

---

<a id="description"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/description.html -->

<!-- page_index: 4 -->

<a id="description--user-guide"></a>

# User guide

Commons-IO contains
[utility classes](#description--utility_classes), [endian classes](#description--endian_classes), [line iterator](#description--line_iterator), [file filters](#description--file_filters), [file comparators](#description--file_comparators) and
[stream implementations](#description--streams).

For a more detailed descriptions, take a look at the
[Javadocs](https://commons.apache.org/proper/commons-io/apidocs/index.html).

<a id="description--utility-classes"></a>

# Utility classes

<a id="description--ioutils"></a>

## IOUtils

[IOUtils](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2FIOUtils.html=)
contains utility methods dealing with reading, writing and copying.
The methods work on InputStream, OutputStream, Reader and Writer.

As an example, consider the task of reading bytes
from a URL, and printing them. This would typically be done like this:

```

 InputStream in = new URL("https://commons.apache.org").openStream();
 try {
   InputStreamReader inR = new InputStreamReader(in);
   BufferedReader buf = new BufferedReader(inR);
   String line;
   while ((line = buf.readLine()) != null) {
     System.out.println(line);
   }
 } finally {
   in.close();
 }
```

With the IOUtils class, that could be done with:

```

 InputStream in = new URL("https://commons.apache.org").openStream();
 try {
   System.out.println(IOUtils.toString(in));
 } finally {
   IOUtils.closeQuietly(in);
 }
```

In certain application domains, such IO operations are
common, and this class can save a great deal of time. And you can
rely on well-tested code.

For utility code such as this, flexibility and speed are of primary importance.
However you should also understand the limitations of this approach.
Using the above technique to read a 1GB file would result in an
attempt to create a 1GB String object!

<a id="description--fileutils"></a>

## FileUtils

The [FileUtils](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2FFileUtils.html=)
class contains utility methods for working with File objects.
These include reading, writing, copying and comparing files.

For example to read an entire file line by line you could use:

```

 File file = new File("/commons/io/project.properties");
 List lines = FileUtils.readLines(file, "UTF-8");
```

<a id="description--filenameutils"></a>

## FilenameUtils

The [FilenameUtils](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2FFilenameUtils.html=)
class contains utility methods for working with filenames *without*
using File objects. The class aims to be consistent
between Unix and Windows, to aid transitions between these
environments (such as moving from development to production).

For example to normalize a filename removing double dot segments:

```

 String filename = "C:/commons/io/../lang/project.xml";
 String normalized = FilenameUtils.normalize(filename);
 // result is "C:/commons/lang/project.xml"
```

<a id="description--filesystemutils"></a>

## FileSystemUtils

The [FileSystemUtils](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2FFileSystemUtils.html=)
class contains
utility methods for working with the file system
to access functionality not supported by the JDK.
Currently, the only method is to get the free space on a drive.
Note that this uses the command line, not native code.

For example to find the free space on a drive:

```

 long freeSpace = FileSystemUtils.freeSpace("C:/");
```

<a id="description--endian-classes"></a>

# Endian classes

Different computer architectures adopt different
conventions for byte ordering. In so-called
"Little Endian" architectures (eg Intel), the low-order
byte is stored in memory at the lowest address, and
subsequent bytes at higher addresses. For "Big Endian"
architectures (eg Motorola), the situation is reversed.

There are two classes in this package of relevance:

- The [EndianUtils](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2FEndianUtils.html=)
  class contains static methods for swapping the Endian-ness
  of Java primitives and streams.
- The [SwappedDataInputStream](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Finput%2FSwappedDataInputStream.html=)
  class is an implementation of the `DataInput` interface. With
  this, one can read data from files of non-native Endian-ness.

For more information, see
<https://www.cs.umass.edu/~verts/cs32/endian.html>

<a id="description--line-iterator"></a>

# Line iterator

The `org.apache.commons.io.LineIterator` class
provides a flexible way for working with a line-based file.
An instance can be created directly, or via factory methods on
`FileUtils` or `IOUtils`.
The recommended usage pattern is:

```
LineIterator it = FileUtils.lineIterator(file, "UTF-8"); try {while (it.hasNext()) {String line = it.nextLine(); /// do something with line} } finally {LineIterator.closeQuietly(iterator);}
```

<a id="description--file-filters"></a>

# File filters

The `org.apache.commons.io.filefilter`
package defines an interface
([IOFileFilter](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Ffilefilter%2FIOFileFilter.html=))
that combines both `java.io.FileFilter` and
`java.io.FilenameFilter`. Besides
that the package offers a series of ready-to-use
implementations of the `IOFileFilter`
interface including
implementation that allow you to combine other such filters.
These filters can be used to list files or in FileDialog, for example.

See the
[filefilter](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Ffilefilter%2Fpackage-summary.html=)
package Javadoc for more details.

<a id="description--file-comparators"></a>

# File comparators

The `org.apache.commons.io.comparator`
package provides a number of `java.util.Comparator`
implementations for `java.io.File`.
These comparators can be used to sort lists and arrays of files, for example.

See the
[comparator](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Fcomparator%2Fpackage-summary.html=)
package Javadoc for more details.

<a id="description--safe-deserialization"></a>

# Safe Deserialization

You can safely deserialize any input using a [ValidatingObjectInputStream](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Fserialization%2FValidatingObjectInputStream.html=).

Here is the only way to safely read a `HashMap` of `String` keys and `Integer` values:

```

        ValidatingObjectInputStream vois = ValidatingObjectInputStream.builder()
          .setPath(Paths.get("MyFile.ser"))
          .get();
        vois.accept(HashMap.class, Number.class, Integer.class);
        HashMap<String, Integer> map2 = (HashMap<String, Integer>) vois.readObject();
      
```

Here is an example that performs a roundtrip:

```

        // Data
        final HashMap<String, Integer> map1 = new HashMap<>();
        map1.put("1", 1);
        // Write
        final byte[] byteArray;
        try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
                final ObjectOutputStream oos = new ObjectOutputStream(baos)) {
            oos.writeObject(map1);
            oos.flush();
            byteArray = baos.toByteArray();
        }
        // Read
        try (ByteArrayInputStream bais = new ByteArrayInputStream(byteArray);
                ValidatingObjectInputStream vois = ValidatingObjectInputStream.builder().setInputStream(bais).get()) {
            // String.class is automatically accepted
            vois.accept(HashMap.class, Number.class, Integer.class);
            final HashMap<String, Integer> map2 = (HashMap<String, Integer>) vois.readObject();
            assertEquals(map1, map2);
        }
        // Reusing a configuration
        final ObjectStreamClassPredicate predicate = new ObjectStreamClassPredicate()
                .accept(HashMap.class, Number.class, Integer.class);
        try (ByteArrayInputStream bais = new ByteArrayInputStream(byteArray);
                ValidatingObjectInputStream vois = ValidatingObjectInputStream.builder()
                        .setPredicate(predicate)
                        .setInputStream(bais)
                        .get()) {
            // String.class is automatically accepted
            final HashMap<String, Integer> map2 = (HashMap<String, Integer>) vois.readObject();
            assertEquals(map1, map2);
        }
      
```

<a id="description--streams"></a>

# Streams

The `org.apache.commons.io.input` and
`org.apache.commons.io.output` packages
contain various useful implementations of streams.
These include:

- Null output stream - that silently absorbs all data sent to it
- Tee output stream - that sends output data to two streams instead of one
- Byte array output stream - that is a faster version of the JDK class
- Counting streams - that count the number of bytes passed
- Proxy streams - that delegate to the correct method in the proxy
- Lockable writer - that provides synchronization of writes using a lock file

See the
[input](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Finput%2Fpackage-summary.html=) or
[output](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2Foutput%2Fpackage-summary.html=)
package Javadoc for more details.

---

<a id="bestpractices"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/bestpractices.html -->

<!-- page_index: 5 -->

<a id="bestpractices--best-practices"></a>

# Best practices

This document presents a number of 'best practices' in the IO area.

<a id="bestpractices--java.io.file"></a>

# java.io.File

Often, you have to deal with files and filenames. There are many
things that can go wrong:

- A class works in Unix but doesn't on Windows (or vice versa)
- Invalid filenames due to double or missing path separators
- UNC filenames (on Windows) don't work with my home-grown filename utility function
- etc. etc.

These are good reasons not to work with filenames as Strings.
Using java.io.File instead handles many of the above cases nicely.
Thus, our best practice recommendation is to use java.io.File
instead of String for filenames to avoid platform dependencies.

*Version 1.1 of commons-io now includes a dedicated filename
handling class - [FilenameUtils](https://commons.apache.org/proper/commons-io/apidocs/index.html?org%2Fapache%2Fcommons%2Fio%2FFilenameUtils.html=).
This does handle many of these filename issues, however we still
recommend, wherever possible, that you use java.io.File objects.*

Let's look at an example.

```
public static String getExtension(String filename) {int index = filename.lastIndexOf('.'); if (index == -1) {return ""; } else {return filename.substring(index + 1);}}
```

Easy enough? Right, but what happens if someone passes in a full path
instead of only a filename? Consider the following, perfectly legal path:
"C:\Temp\documentation.new\README".
The method as defined above would return "new\README" - definitely
not what you wanted.

Please use java.io.File for filenames instead of Strings.
The functionality that the class provides is well tested.
In FileUtils you will find other useful utility functions
around java.io.File.

Instead of:

```

 String tmpdir = "/var/tmp";
 String tmpfile = tmpdir + System.getProperty("file.separator") + "test.tmp";
 InputStream in = new java.io.FileInputStream(tmpfile);
```

...write:

```

 File tmpdir = new File("/var/tmp");
 File tmpfile = new File(tmpdir, "test.tmp");
 InputStream in = new java.io.FileInputStream(tmpfile);
```

<a id="bestpractices--buffering-streams"></a>

# Buffering streams

IO performance depends a lot on the buffering strategy. Usually, it's
quite fast to read packets with the size of 512 or 1024 bytes because
these sizes match well with the packet sizes used on hard disks in
file systems or file system caches. But as soon as you have to read only
a few bytes and that many times performance drops significantly.

Make sure you're properly buffering streams when reading or writing
streams, especially when working with files. Just decorate your
FileInputStream with a BufferedInputStream:

```

 InputStream in = new java.io.FileInputStream(myfile);
 try {
   in = new java.io.BufferedInputStream(in);
   
   in.read(.....
 } finally {
   IOUtils.closeQuietly(in);
 }
```

Pay attention that you're not buffering an already buffered stream. Some
components like XML parsers may do their own buffering so decorating
the InputStream you pass to the XML parser does nothing but slowing down
your code. If you use our CopyUtils or IOUtils you don't need to
additionally buffer the streams you use as the code in there already
buffers the copy process. Always check the Javadocs for information.
Another case where buffering is unnecessary is when you write to a
ByteArrayOutputStream since you're writing to memory only.

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/building.html -->

<!-- page_index: 6 -->

<a id="building--overview"></a>

# Overview

Commons IO uses [Maven](https://maven.apache.org) its build system.

Commons IO requires a minimum of JDK 8 to build.

You may also be interested in the upgrade notes:

- Upgrade [from 2.0 to 2.0.1](https://commons.apache.org/proper/commons-io/upgradeto2_0_1.html)
- Upgrade [from 1.4 to 2.0](https://commons.apache.org/proper/commons-io/upgradeto2_0.html)
- Upgrade [from 1.3.2 to 1.4](https://commons.apache.org/proper/commons-io/upgradeto1_4.html)
- Upgrade [from 1.3, or 1.3.1 to 1.3.2](https://commons.apache.org/proper/commons-io/upgradeto1_3_2.html)
- Upgrade [from 1.3 to 1.3.1](https://commons.apache.org/proper/commons-io/upgradeto1_3_1.html)
- Upgrade [from 1.2 to 1.3](https://commons.apache.org/proper/commons-io/upgradeto1_3.html)
- Upgrade [from 1.1 to 1.2](https://commons.apache.org/proper/commons-io/upgradeto1_2.html)
- Upgrade [from 1.0 to 1.1](https://commons.apache.org/proper/commons-io/upgradeto1_1.html)

<a id="building--maven-goals"></a>

# Maven Goals

The following [Maven](https://maven.apache.org) commands can be used to build io:

- `mvn` - runs the default Maven goal which performs all build checks
- `mvn clean` - cleans up
- `mvn test` - compiles and runs the unit tests
- `mvn site` - creates the site and documentation
- `mvn package` - creates the jar

---

<a id="proposal"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/proposal.html -->

<!-- page_index: 7 -->

<a id="proposal--proposal-for-io-package"></a>

# Proposal for IO Package

<a id="proposal--0-rationale"></a>

## (0) Rationale

Many software projects have a need to perform I/O in various ways, and
the JDK class libraries provide a lot of functionality, but sometimes you
need just a little bit more. The io package seeks to encapsulate some of
the most popular i/o base classes into one easy to use package.

<a id="proposal--1-scope-of-the-package"></a>

## (1) Scope of the Package

This proposal is to create a package of Java utility classes for various
types of i/o related activity.

<a id="proposal--1.5-interaction-with-other-packages"></a>

## (1.5) Interaction With Other Packages

*IO* relies only on standard JDK 1.2 (or later) APIs for production
deployment. It utilizes the JUnit unit testing framework for developing
and executing unit tests, but this is of interest only to developers of the
component. IO will be a dependency for several existing components in the
open source world.

No external configuration files are utilized.

<a id="proposal--2-initial-source-of-the-package"></a>

## (2) Initial Source of the Package

The original Java classes are splashed around various Apache subprojects.
We intend to seek them out and integrate them.

The proposed package name for the new component is `org.apache.commons.io`.

<a id="proposal--3-required-jakarta-commons-resources"></a>

## (3) Required Jakarta-Commons Resources

- CVS Repository - New directory `io` in the `jakarta-commons`
  CVS repository.
- Mailing List - Discussions will take place on the general *dev@commons.apache.org*
  mailing list. To help list subscribers identify messages of interest,
  it is suggested that the message subject of messages about this component
  be prefixed with [IO].
- Bugzilla - New component "IO" under the "Commons" product category,
  with appropriate version identifiers as needed.
- Jyve FAQ - New category "commons-io" (when available).

<a id="proposal--4-initial-committers"></a>

## (4) Initial Committers

The initial committers on the IO component shall be Scott Sanders and
Nicola Ken Barozzi and Henri Yandell

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/project-info.html -->

<!-- page_index: 8 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons IO library contains utility classes, stream implementations, file filters, file comparators, endian transformation classes, and much more. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-io/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-io/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-io/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-io/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-io/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-io/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-io/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/summary.html -->

<!-- page_index: 9 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons IO |
| Description | The Apache Commons IO library contains utility classes, stream implementations, file filters, file comparators, endian transformation classes, and much more. |
| Homepage | [https://commons.apache.org/proper/commons-io/](#index) |

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
| GroupId | commons-io |
| ArtifactId | commons-io |
| Version | 2.22.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/team.html -->

<!-- page_index: 10 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | sanders | Scott Sanders | [sanders@apache.org](mailto:sanders@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | nicolaken | Nicola Ken Barozzi | [nicolaken@apache.org](mailto:nicolaken@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/4156866f23b66d5ca7df5cdc86cb9a0e_b7912c1388d06861.jpg) | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | scolebourne | Stephen Colebourne | - | - | - | - | Java Developer | 0 |
| ![](assets/images/7e0393eaef26065d612909513ec19196_2a3b37f68888937d.jpg) | jeremias | Jeremias Maerki | [jeremias@apache.org](mailto:jeremias@apache.org) | - | - | - | Java Developer | +1 |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | matth | Matthew Hawthorne | [matth@apache.org](mailto:matth@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | martinc | Martin Cooper | [martinc@apache.org](mailto:martinc@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | roxspring | Rob Oxspring | [roxspring@apache.org](mailto:roxspring@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/336bc7e3330df0d682d46abf0193d420_fc2a3f620894f8aa.jpg) | jochen | Jochen Wiedmann | [jochen.wiedmann@gmail.com](mailto:jochen.wiedmann@gmail.com) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | niallp | Niall Pemberton | - | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | jukka | Jukka Zitting | - | - | - | - | Java Developer | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/3c2ad6b6efb1c84d9ff60259f8c8ef95_4de85bc1b06dccb0.jpg) | krosenvold | Kristian Rosenvold | [krosenvold@apache.org](mailto:krosenvold@apache.org) | - | - | - | - | +1 |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Rahul Akolkar | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Jason Anderson | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Nathan Beyer | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Emmanuel Bourg | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Chris Eldredge | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Magnus Grimsell | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Jim Harrington | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Thomas Ledoux | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Andy Lehane | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Marcelo Liberato | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Alban Peignier | [alban.peignier at free.fr](mailto:alban.peignier at free.fr) | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Adam Retter | - | Evolved Binary |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Ian Springer | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Dominik Stadler | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Masato Tezuka | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | James Urie | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Frank W. Zammetti | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Martin Grigorov | [mgrigorov@apache.org](mailto:mgrigorov@apache.org) | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Arturo Bernal | - | - |
| ![](assets/images/00000000000000000000000000000000_f04ca47cd0c7834c.jpg) | Miguel Muñoz | - | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-io/ci-management.html -->

<!-- page_index: 11 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-io/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
