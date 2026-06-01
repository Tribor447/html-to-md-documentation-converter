# Project Information

## Navigation

- Commons Compress
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [User Guide](#examples)
  - [Known Limitations](#limitations)
  - [Conventions](#conventions)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- [General Information](#security)
- Other pages
  - [The Pack200 package](#pack200)
  - [The TAR package](#tar)
  - [The ZIP package](#zip)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-compress"></a>

# Apache Commons Compress™

The Apache Commons Compress library defines an API for
working with ar, cpio, Unix dump, tar, zip, gzip, XZ, Pack200, bzip2, 7z, arj, LZMA, snappy, DEFLATE, lz4, Brotli, Zstandard, DEFLATE64 and Z files.

The code in this component has many origins:

- The bzip2, tar and zip support came from Avalon's
  Excalibur, but originally from Ant, as far as life in
  Apache goes. The tar package is originally Tim Endres'
  public domain package. The bzip2 package is based on
  the work done by Keiron Liddle as well as Julian Seward's
  [libbzip2](http://www.bzip.org/index.html).
  It has migrated
  via: Ant -> Avalon-Excalibur -> Commons-IO
  -> Commons-Compress.
- The cpio package has been contributed by Michael Kuss
  and
  the [jRPM](http://jrpm.sourceforge.net/)
  project.
- The pack200 code has originally been part of the now
  retired [Apache
  Harmony™](https://harmony.apache.org/) project.

<a id="index--status"></a>

# Status

The current release requires Java 8 or above.

For a list of changes see the [Changes Report](https://commons.apache.org/proper/commons-compress/changes.html).

<a id="index--documentation"></a>

# Documentation

The compress component is split into *compressors* and
*archivers*. While *compressors*
(un)compress streams that usually store a single
entry, *archivers* deal with archives that contain
structured content represented
by `ArchiveEntry` instances which in turn
usually correspond to single files or directories.

Currently the bzip2, Pack200, XZ, gzip, LZMA, brotli, Zstandard and Z formats are
supported as compressors where gzip support is mostly provided by
the `java.util.zip` package of the Java
class library. XZ and LZMA support is provided by the public
domain [XZ for
Java](https://tukaani.org/xz/java.html) library. Brotli support is provided by the MIT
licensed [Google
Brotli decoder](https://github.com/google/brotli). Zstandard support is provided by the BSD
licensed [Zstd-jni](https://github.com/luben/zstd-jni).
As of Commons Compress 1.21 support for the DEFLATE64, Z and Brotli
formats is read-only.

The ar, arj, cpio, dump, tar, 7z and zip formats are supported as
archivers where the [zip](#zip)
implementation provides capabilities that go beyond the
features found in java.util.zip. As of Commons Compress
1.21 support for the dump and arj formats is
read-only - 7z can read most compressed and encrypted
archives but only write unencrypted ones. LZMA(2) support
in 7z requires [XZ for
Java](https://tukaani.org/xz/java.html) as well.

The compress component provides abstract base classes for
compressors and archivers together with factories that can
be used to choose implementations by algorithm name. In
the case of input streams the factories can also be used
to guess the format and provide the matching
implementation.

- The [user guide](#examples) contains
  more detailed information and some examples.
- The [known limitations and
  problems](#limitations) page lists the currently known problems
  grouped by the format they apply to.
- The [Javadoc](https://commons.apache.org/proper/commons-compress/apidocs/index.html) of the latest GIT
- The [GIT
  repository](https://gitbox.apache.org/repos/asf?p=commons-compress.git) can be browsed.

<a id="index--releases"></a>

# Releases

[Download now!](https://commons.apache.org/compress/download_compress.cgi)

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-compress.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-compress.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-compress.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/security.html -->

<!-- page_index: 3 -->

<a id="security--general-information"></a>

# General Information

For information about reporting or asking questions about
security problems, please see the [security page
of the Commons project](https://commons.apache.org/security.html).

<a id="security--apache-commons-compress-security-vulnerabilities"></a>

# Apache Commons Compress Security Vulnerabilities

This page lists all security vulnerabilities fixed in
released versions of Apache Commons Compress. Each
vulnerability is given a security impact rating by the
development team - please note that this rating may vary from
platform to platform. We also list the versions of Commons
Compress the flaw is known to affect, and where a flaw has not
been verified list the version with a question mark.

Please note that binary patches are never provided. If you
need to apply a source code patch, use the building
instructions for the Commons Compress version that you are
using.

If you need help on building Commons Compress or other help
on following the instructions to mitigate the known
vulnerabilities listed here, please send your questions to the
public [Compress Users mailing
list](https://commons.apache.org/proper/commons-compress/mail-lists.html).

If you have encountered an unlisted security vulnerability
or other unexpected behavior that has security impact, or if
the descriptions here are incomplete, please report them
privately to the Apache Security Team. Thank you.

<a id="security--fixed-in-apache-commons-compress-1.26.0"></a>

## Fixed in Apache Commons Compress 1.26.0

**Important: Denial of Service** [CVE-2024-25710](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25710)

This affects version 1.3 through 1.25.0.

This denial of service is caused by an infinite loop reading a corrupted DUMP file.

Users are recommended to upgrade to version 1.26.0 which fixes the issue.

Credit to Yakov Shafranovich, Amazon Web Services (reporter).

**Moderate: Denial of Service** [CVE-2024-26308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26308)

You can get an OutOfMemoryError unpacking a broken Pack200 file.

This issue affects Commons Compress 1.21 before 1.26.0.

Users are recommended to upgrade to version 1.26.0 which fixes the issue.

Credit to Yakov Shafranovich, Amazon Web Services (reporter).

<a id="security--fixed-in-apache-commons-compress-1.24.0"></a>

## Fixed in Apache Commons Compress 1.24.0

**Moderate: Denial of Service** [CVE-2023-42503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42503)

Improper Input Validation, Uncontrolled Resource Consumption vulnerability in Apache Commons Compress in TAR parsing.

This issue affects Apache Commons Compress: from 1.22 before 1.24.0.

Users are recommended to upgrade to version 1.24.0, which fixes the issue.

A third party can create a malformed TAR file by manipulating file modification times headers, which when parsed with Apache Commons Compress, will cause a denial of service issue via CPU consumption.

In version 1.22 of Apache Commons Compress, support was added for file modification times with higher precision
(issue # COMPRESS-612[[1]](#security--ref-1-24-1)).
The format for the PAX extended headers carrying this data consists of two numbers separated by a period[[2]](#security--ref-1-24-2), indicating seconds and subsecond precision (for example “1647221103.5998539”). The impacted fields are “atime”, “ctime”, “mtime” and
“LIBARCHIVE.creationtime”. No input validation is performed prior to the parsing of header values.

Parsing of these numbers uses the BigDecimal[[3]](#security--ref-1-24-3) class from the JDK which has a publicly known algorithmic complexity issue when doing
operations on large numbers, causing denial of service (see issue # JDK-6560193[[4]](#security--ref-1-24-4)). A third party can manipulate file time headers
in a TAR file by placing a number with a very long fraction (300,000 digits) or a number with exponent notation (such as “9e9999999”)
within a file modification time header, and the parsing of files with these headers will take hours instead of seconds, leading to a
denial of service via exhaustion of CPU resources. This issue is similar to CVE-2012-2098[[5]](#security--ref-1-24-5).

- [1]: [COMPRESS-612](https://issues.apache.org/jira/browse/COMPRESS-612)
- [2]: [PAX extended headers](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/pax.html#tag_20_92_13_05)
- [3]: [BigDecimal](https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html)
- [4]: [JDK-6560193](https://bugs.openjdk.org/browse/JDK-6560193)
- [5]: [CVE-2012-2098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2098)

Only applications using CompressorStreamFactory class (with auto-detection of file types), TarArchiveInputStream and TarFile
classes to parse TAR files are impacted. Since this code was introduced in v1.22, only that version and later versions are impacted.

<a id="security--fixed-in-apache-commons-compress-1.21"></a>

## Fixed in Apache Commons Compress 1.21

**Low: Denial of Service** [CVE-2021-35515](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35515)

When reading a specially crafted 7Z archive, the construction of the
list of codecs that decompress an entry can result in an infinite
loop. This could be used to mount a denial of service attack against
services that use Compress' sevenz package.

This was fixed in revision [3fe6b42](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=3fe6b42110dc56d0d6fe0aaf80cfecb8feea5321).

This issue was discovered by OSS Fuzz.

Affects: 1.6 - 1.20

**Low: Denial of Service** [CVE-2021-35516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35516)

When reading a specially crafted 7Z archive, Compress can be made to
allocate large amounts of memory that finally leads to an out of memory
error even for very small inputs. This could be used to mount a denial
of service attack against services that use Compress' sevenz package.

This was fixed in revisions
[26924e9](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=26924e96c7730db014c310757e11c9359db07f3e), [c51de6c](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=c51de6cfaec75b21566374158f25e1734c3a94cb), [0aba8b8](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=0aba8b8fd8053ae323f15d736d1762b2161c76a6), [60d551a](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=60d551a748236d7f4651a4ae88d5a351f7c5754b), [bf5a534](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=bf5a5346ae04b9d2a5b0356ca75f11dcc8d94789), [5761493](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=5761493cbaf7a7d608a3b68f4d61aaa822dbeb4f), and [ae2b27c](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=ae2b27cc011f47f0289cb24a11f2d4f1db711f8a)
.

This issue was first reported to the project's issue tracker as
[COMPRESS-542](https://issues.apache.org/jira/browse/COMPRESS-542)
by Robin Schimpf.
Later OSS Fuzz detected ways to exploit this issue which managed to
escape the initial attempt to fix it.

Affects: 1.6 - 1.20

**Low: Denial of Service** [CVE-2021-35517](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35517)

When reading a specially crafted TAR archive, Compress
can be made to allocate large amounts of memory that finally
leads to an out of memory error even for very small
inputs. This could be used to mount a denial of service
attack against services that use Compress' tar package.

This was fixed in revisions
[d0af873](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=d0af873e77d16f41edfef7b69da5c8c35c96a650), [7ce1b07](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=7ce1b0796d6cbe1f41b969583bd49f33ae0efef0)
and [80124dd](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=80124dd9fe4b0a0b2e203ca19aacac8cd0afc96f).

This issue was discovered by OSS Fuzz.

Affects: 1.1 - 1.20

**Low: Denial of Service** [CVE-2021-36090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36090)

When reading a specially crafted ZIP archive, Compress
can be made to allocate large amounts of memory that finally
leads to an out of memory error even for very small
inputs. This could be used to mount a denial of service
attack against services that use Compress' zip package.

This was fixed in revisions
[ef5d70b](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=ef5d70b625000e38404194aaab311b771c44efda)
and [80124dd](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commit;h=80124dd9fe4b0a0b2e203ca19aacac8cd0afc96f).

This issue was discovered by OSS Fuzz.

Affects: 1.0 - 1.20

<a id="security--fixed-in-apache-commons-compress-1.19"></a>

## Fixed in Apache Commons Compress 1.19

**Low: Denial of Service** [CVE-2019-12402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-12402)

The file name encoding algorithm used internally in Apache Commons
Compress can get into an infinite loop when faced with specially
crafted inputs. This can lead to a denial of service attack if an
attacker can choose the file names inside of an archive created by
Compress.

This was fixed in revision [4ad5d80a](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=commitdiff;h=4ad5d80a6272e007f64a6ac66829ca189a8093b9;hp=16a0c84e84b93cc8c107b7ff3080bd11317ab581).

This was first reported to the Commons Security Team on 22 August
2019 and made public on 27 August 2019.

Affects: 1.15 - 1.18

<a id="security--fixed-in-apache-commons-compress-1.18"></a>

## Fixed in Apache Commons Compress 1.18

**Low: Denial of Service** [CVE-2018-11771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11771)

When reading a specially crafted ZIP archive, the read
method of `ZipArchiveInputStream` can fail to
return the correct EOF indication after the end of the
stream has been reached. When combined with a
`java.io.InputStreamReader` this can lead to an
infinite stream, which can be used to mount a denial of
service attack against services that use Compress' zip
package

This was fixed in revision [a41ce68](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=blobdiff;f=src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveInputStream.java;h=e1995d7aa51dfac6ae933987fb0b7760c607582b;hp=0a2c1aa0063c620c867715119eae2013c87b5e70;hb=a41ce6892cb0590b2e658704434ac0dbcb6834c8;hpb=64ed6dde03afbef6715fdfdeab5fc04be6192899).

This was first reported to the Security Team on 14 June
2018 and made public on 16 August 2018.

Affects: 1.7 - 1.17

<a id="security--fixed-in-apache-commons-compress-1.16"></a>

## Fixed in Apache Commons Compress 1.16

**Low: Denial of Service** [CVE-2018-1324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1324)

A specially crafted ZIP archive can be used to cause an
infinite loop inside of Compress' extra field parser used by
the `ZipFile` and
`ZipArchiveInputStream` classes. This can be
used to mount a denial of service attack against services
that use Compress' zip package.

This was fixed in revision [2a2f1dc4](https://gitbox.apache.org/repos/asf?p=commons-compress.git;a=blobdiff;f=src/main/java/org/apache/commons/compress/archivers/zip/X0017_StrongEncryptionHeader.java;h=acc3b22346b49845e85b5ef27a5814b69e834139;hp=0feb9c98cc622cde1defa3bbd268ef82b4ae5c18;hb=2a2f1dc48e22a34ddb72321a4db211da91aa933b;hpb=dcb0486fb4cb2b6592c04d6ec2edbd3f690df5f2).

This was first reported to the project's JIRA on [19
December 2017](https://issues.apache.org/jira/browse/COMPRESS-432).

Affects: 1.11 - 1.15

<a id="security--fixed-in-apache-commons-compress-1.4.1"></a>

## Fixed in Apache Commons Compress 1.4.1

**Low: Denial of Service** [CVE-2012-2098](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2098)

The bzip2 compressing streams in Apache Commons Compress
internally use sorting algorithms with unacceptable
worst-case performance on very repetitive inputs. A
specially crafted input to Compress'
`BZip2CompressorOutputStream` can be used to make
the process spend a very long time while using up all
available processing time effectively leading to a denial of
service.

This was fixed in revisions
[1332540](https://svn.apache.org/viewvc?view=revision&revision=1332540), [1332552](https://svn.apache.org/viewvc?view=revision&revision=1332552), [1333522](https://svn.apache.org/viewvc?view=revision&revision=1333522), [1337444](https://svn.apache.org/viewvc?view=revision&revision=1337444), [1340715](https://svn.apache.org/viewvc?view=revision&revision=1340715), [1340723](https://svn.apache.org/viewvc?view=revision&revision=1340723), [1340757](https://svn.apache.org/viewvc?view=revision&revision=1340757), [1340786](https://svn.apache.org/viewvc?view=revision&revision=1340786), [1340787](https://svn.apache.org/viewvc?view=revision&revision=1340787), [1340790](https://svn.apache.org/viewvc?view=revision&revision=1340790), [1340795](https://svn.apache.org/viewvc?view=revision&revision=1340795) and
[1340799](https://svn.apache.org/viewvc?view=revision&revision=1340799).

This was first reported to the Security Team on 12 April
2012 and made public on 23 May 2012.

Affects: 1.0 - 1.4

<a id="security--errors-and-omissions"></a>

# Errors and Omissions

Please report any errors or omissions to [the dev mailing list](https://commons.apache.org/proper/commons-compress/mail-lists.html).

---

<a id="examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/examples.html -->

<!-- page_index: 4 -->

<a id="examples--general-notes"></a>

# General Notes

<a id="examples--archivers-and-compressors"></a>

## Archivers and Compressors

Commons Compress calls all formats that compress a single
stream of data compressor formats while all formats that
collect multiple entries inside a single (potentially
compressed) archive are archiver formats.

The compressor formats supported are gzip, bzip2, XZ, LZMA, Pack200, DEFLATE, Brotli, DEFLATE64, ZStandard and Z, the archiver formats are 7z, ar, arj, cpio, dump, tar and zip. Pack200 is a special case as it can
only compress JAR files.

We currently only provide read support for arj, dump, Brotli, DEFLATE64 and Z. arj can only read uncompressed archives, 7z can read
archives with many compression and encryption algorithms
supported by 7z but doesn't support encryption when writing
archives.

<a id="examples--buffering"></a>

## Buffering

The stream classes all wrap around streams provided by the
calling code and they work on them directly without any
additional buffering. On the other hand most of them will
benefit from buffering so it is highly recommended that
users wrap their stream
in `Buffered(In|Out)putStream`s before
using the Commons Compress API.

<a id="examples--factories"></a>

## Factories

Compress provides factory methods to create input/output
streams based on the names of the compressor or archiver
format as well as factory methods that try to guess the
format of an input stream.

To create a compressor writing to a given output by using
the algorithm name:

```

CompressorOutputStream gzippedOut = new CompressorStreamFactory()
    .createCompressorOutputStream(CompressorStreamFactory.GZIP, myOutputStream);
```

Make the factory guess the input format for a given
archiver stream:

```

ArchiveInputStream input = new ArchiveStreamFactory()
    .createArchiveInputStream(originalInput);
```

Make the factory guess the input format for a given
compressor stream:

```

CompressorInputStream input = new CompressorStreamFactory()
    .createCompressorInputStream(originalInput);
```

Note that there is no way to detect the LZMA or Brotli formats so only
the two-arg version of
`createCompressorInputStream` can be used. Prior
to Compress 1.9 the .Z format hasn't been auto-detected
either.

<a id="examples--restricting-memory-usage"></a>

## Restricting Memory Usage

Starting with Compress 1.14
`CompressorStreamFactory` has an optional
constructor argument that can be used to set an upper limit of
memory that may be used while decompressing or compressing a
stream. As of 1.14 this setting only affects decompressing Z, XZ and LZMA compressed streams.

Since Compress 1.19 `SevenZFile` also has an
optional constructor to pass an upper memory limit which is supported
in LZMA compressed streams. Since Compress 1.21 this setting
also is taken into account when reading the metadata of an archive.

For the Snappy and LZ4 formats the amount of memory used
during compression is directly proportional to the window
size.

<a id="examples--statistics"></a>

## Statistics

Starting with Compress 1.17 most of the
`CompressorInputStream` implementations as well as
`ZipArchiveInputStream` and all streams returned by
`ZipFile.getInputStream` implement the
`InputStreamStatistics`
interface. `SevenZFile` provides statistics for the
current entry via the
`getStatisticsForCurrentEntry` method. This
interface can be used to track progress while extracting a
stream or to detect potential [zip bombs](https://en.wikipedia.org/wiki/Zip_bomb)
when the compression ratio becomes suspiciously large.

<a id="examples--archivers"></a>

# Archivers

<a id="examples--unsupported-features"></a>

## Unsupported Features

Many of the supported formats have developed different
dialects and extensions and some formats allow for features
(not yet) supported by Commons Compress.

The `ArchiveInputStream` class provides a method
`canReadEntryData` that will return false if
Commons Compress can detect that an archive uses a feature
that is not supported by the current implementation. If it
returns false you should not try to read the entry but skip
over it.

<a id="examples--entry-names"></a>

## Entry Names

All archive formats provide meta data about the individual
archive entries via instances of `ArchiveEntry` (or
rather subclasses of it). When reading from an archive the
information provided the `getName` method is the
raw name as stored inside of the archive. There is no
guarantee the name represents a relative file name or even a
valid file name on your target operating system at all. You
should double check the outcome when you try to create file
names from entry names.

<a id="examples--common-extraction-logic"></a>

## Common Extraction Logic

Apart from 7z all formats provide a subclass of
`ArchiveInputStream` that can be used to create an
archive. For 7z `SevenZFile` provides a similar API
that does not represent a stream as our implementation
requires random access to the input and cannot be used for
general streams. The ZIP implementation can benefit a lot from
random access as well, see the [zip
page](#zip--ziparchiveinputstream_vs_zipfile) for details.

Assuming you want to extract an archive to a target
directory you'd call `getNextEntry`, verify the
entry can be read, construct a sane file name from the entry's
name, create a `File` and write all contents to
it - here `IOUtils.copy` may come handy. You do so
for every entry until `getNextEntry` returns
`null`.

A skeleton might look like:

```
File targetDir = ...try (ArchiveInputStream i = ... create the stream for your format, use buffering...) {ArchiveEntry entry = null; while ((entry = i.getNextEntry()) != null) {if (!i.canReadEntryData(entry)) {// log something? continue;} String name = fileName(targetDir, entry); File f = new File(name); if (entry.isDirectory()) {if (!f.isDirectory() && !f.mkdirs()) {throw new IOException("failed to create directory " + f);} } else {File parent = f.getParentFile(); if (!parent.isDirectory() && !parent.mkdirs()) {throw new IOException("failed to create directory " + parent);} try (OutputStream o = Files.newOutputStream(f.toPath())) {IOUtils.copy(i, o);}}}}
```

where the hypothetical `fileName` method is
written by you and provides the absolute name for the file
that is going to be written on disk. Here you should perform
checks that ensure the resulting file name actually is a valid
file name on your operating system or belongs to a file inside
of `targetDir` when using the entry's name as
input.

If you want to combine an archive format with a compression
format - like when reading a "tar.gz" file - you wrap the
`ArchiveInputStream` around
`CompressorInputStream` for example:

```

try (InputStream fi = Files.newInputStream(Paths.get("my.tar.gz"));
     InputStream bi = new BufferedInputStream(fi);
     InputStream gzi = new GzipCompressorInputStream(bi);
     ArchiveInputStream o = new TarArchiveInputStream(gzi)) {
}
```

<a id="examples--common-archival-logic"></a>

## Common Archival Logic

Apart from 7z all formats that support writing provide a
subclass of `ArchiveOutputStream` that can be used
to create an archive. For 7z `SevenZOutputFile`
provides a similar API that does not represent a stream as our
implementation requires random access to the output and cannot
be used for general streams. The
`ZipArchiveOutputStream` class will benefit from
random access as well but can be used for non-seekable streams
- but not all features will be available and the archive size
might be slightly bigger, see [the zip page](#zip--ziparchiveoutputstream) for
details.

Assuming you want to add a collection of files to an
archive, you can first use `createArchiveEntry` for
each file. In general this will set a few flags (usually the
last modified time, the size and the information whether this
is a file or directory) based on the `File` or `Path`
instance. Alternatively you can create the
`ArchiveEntry` subclass corresponding to your
format directly. Often you may want to set additional flags
like file permissions or owner information before adding the
entry to the archive.

Next you use `putArchiveEntry` in order to add
the entry and then start using `write` to add the
content of the entry - here `IOUtils.copy` may
come handy. Finally you invoke
`closeArchiveEntry` once you've written all content
and before you add the next entry.

Once all entries have been added you'd invoke
`finish` and finally `close` the
stream.

A skeleton might look like:

```
Collection<File> filesToArchive = ...try (ArchiveOutputStream o = ... create the stream for your format ...) {for (File f : filesToArchive) {// maybe skip directories for formats like AR that don't store directories ArchiveEntry entry = o.createArchiveEntry(f, entryName(f)); // potentially add more flags to entry o.putArchiveEntry(entry); if (f.isFile()) {try (InputStream i = Files.newInputStream(f.toPath())) {IOUtils.copy(i, o);}} o.closeArchiveEntry();} o.finish();}
```

where the hypothetical `entryName` method is
written by you and provides the name for the entry as it is
going to be written to the archive.

If you want to combine an archive format with a compression
format - like when creating a "tar.gz" file - you wrap the
`ArchiveOutputStream` around a
`CompressorOutputStream` for example:

```

try (OutputStream fo = Files.newOutputStream(Paths.get("my.tar.gz"));
     OutputStream gzo = new GzipCompressorOutputStream(fo);
     ArchiveOutputStream o = new TarArchiveOutputStream(gzo)) {
}
```

<a id="examples--7z"></a>

## 7z

Note that Commons Compress currently only supports a subset
of compression and encryption algorithms used for 7z archives.
For writing only uncompressed entries, LZMA, LZMA2, BZIP2 and
Deflate are supported - in addition to those reading supports
AES-256/SHA-256 and DEFLATE64.

Writing multipart archives is not supported at
all. Multipart archives can be read by concatenating the parts
for example by using
`MultiReadOnlySeekableByteChannel`.

7z archives can use multiple compression and encryption
methods as well as filters combined as a pipeline of methods
for its entries. Prior to Compress 1.8 you could only specify
a single method when creating archives - reading archives
using more than one method has been possible before. Starting
with Compress 1.8 it is possible to configure the full
pipeline using the `setContentMethods` method of
`SevenZOutputFile`. Methods are specified in the
order they appear inside the pipeline when creating the
archive, you can also specify certain parameters for some of
the methods - see the Javadocs of
`SevenZMethodConfiguration` for details.

When reading entries from an archive the
`getContentMethods` method of
`SevenZArchiveEntry` will properly represent the
compression/encryption/filter methods but may fail to
determine the configuration options used. As of Compress 1.8
only the dictionary size used for LZMA2 can be read.

Currently solid compression - compressing multiple files
as a single block to benefit from patterns repeating across
files - is only supported when reading archives. This also
means compression ratio will likely be worse when using
Commons Compress compared to the native 7z executable.

Reading or writing requires a
`SeekableByteChannel` that will be obtained
transparently when reading from or writing to a file. The
class
`org.apache.commons.compress.utils.SeekableInMemoryByteChannel`
allows you to read from or write to an in-memory archive.

Some 7z archives don't contain any names for the archive
entries. The native 7zip tools derive a default name from the
name of the archive itself for such entries. Starting with
Compress 1.19 `SevenZFile` has an option to mimic
this behavior, but by default unnamed archive entries will
return `null` from
`SevenZArchiveEntry#getName`.

Adding an entry to a 7z archive:

```

SevenZOutputFile sevenZOutput = new SevenZOutputFile(file);
SevenZArchiveEntry entry = sevenZOutput.createArchiveEntry(fileToArchive, name);
sevenZOutput.putArchiveEntry(entry);
sevenZOutput.write(contentOfEntry);
sevenZOutput.closeArchiveEntry();
```

Uncompressing a given 7z archive (you would
certainly add exception handling and make sure all streams
get closed properly):

```

SevenZFile sevenZFile = new SevenZFile(new File("archive.7z"));
SevenZArchiveEntry entry = sevenZFile.getNextEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    sevenZFile.read(content, offset, content.length - offset);
}
```

Uncompressing a given in-memory 7z archive:

```

byte[] inputData; // 7z archive contents
SeekableInMemoryByteChannel inMemoryByteChannel = new SeekableInMemoryByteChannel(inputData);
SevenZFile sevenZFile = new SevenZFile(inMemoryByteChannel);
SevenZArchiveEntry entry = sevenZFile.getNextEntry();
sevenZFile.read();  // read current entry's data
```

<a id="examples--encrypted-7z-archives"></a>

#### Encrypted 7z Archives

Currently Compress supports reading but not writing of
encrypted archives. When reading an encrypted archive a
password has to be provided to one of
`SevenZFile`'s constructors. If you try to read
an encrypted archive without specifying a password a
`PasswordRequiredException` (a subclass of
`IOException`) will be thrown.

When specifying the password as a `byte[]` one
common mistake is to use the wrong encoding when creating
the `byte[]` from a `String`. The
`SevenZFile` class expects the bytes to
correspond to the UTF16-LE encoding of the password. An
example of reading an encrypted archive is

```

SevenZFile sevenZFile = new SevenZFile(new File("archive.7z"), "secret".getBytes(StandardCharsets.UTF_16LE));
SevenZArchiveEntry entry = sevenZFile.getNextEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    sevenZFile.read(content, offset, content.length - offset);
}
```

Starting with Compress 1.17 new constructors have been
added that accept the password as `char[]` rather
than a `byte[]`. We recommend you use these in
order to avoid the problem above.

```

SevenZFile sevenZFile = new SevenZFile(new File("archive.7z"), "secret".toCharArray());
SevenZArchiveEntry entry = sevenZFile.getNextEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    sevenZFile.read(content, offset, content.length - offset);
}
```

<a id="examples--random-access-to-7z-archives"></a>

#### Random-Access to 7z Archives

Prior to Compress 1.20 7z archives could only be read
sequentially. The
`getInputStream(SevenZArchiveEntry)` method
introduced with Compress 1.20 now provides random access but
at least when the archive uses solid compression random access
will likely be significantly slower than sequential
access.

<a id="examples--recovering-from-certain-broken-7z-archives"></a>

#### Recovering from Certain Broken 7z Archives

`SevenZFile` tries
to recover archives that look as if they were part of a
multi-volume archive where the first volume has been removed
too early.

This option has to be enabled
explicitly in `SevenZFile.Builder`. The way recovery
works is by Compress scanning an archive from the end for
something that might look like valid 7z metadata and use that, if it can successfully parse the block of data. When doing so
Compress may encounter blocks of metadata that look like the
metadata of very large archives which in turn may make
Compress allocate a lot of memory. Therefore we strongly
recommend you also set a memory limit inside the
`SevenZFile.Builder` if you enable recovery.

<a id="examples--ar"></a>

## ar

In addition to the information stored
in `ArchiveEntry` a `ArArchiveEntry`
stores information about the owner user and group as well as
Unix permissions.

Adding an entry to an ar archive:

```

ArArchiveEntry entry = new ArArchiveEntry(name, size);
arOutput.putArchiveEntry(entry);
arOutput.write(contentOfEntry);
arOutput.closeArchiveEntry();
```

Reading entries from an ar archive:

```

ArArchiveEntry entry = (ArArchiveEntry) arInput.getNextEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    arInput.read(content, offset, content.length - offset);
}
```

Traditionally the AR format doesn't allow file names longer
than 16 characters. There are two variants that circumvent
this limitation in different ways, the GNU/SRV4 and the BSD
variant. Commons Compress 1.0 to 1.2 can only read archives
using the GNU/SRV4 variant, support for the BSD variant has
been added in Commons Compress 1.3. Commons Compress 1.3
also optionally supports writing archives with file names
longer than 16 characters using the BSD dialect, writing
the SVR4/GNU dialect is not supported.

| Version of Apache Commons Compress | Support for Traditional AR Format | Support for GNU/SRV4 Dialect | Support for BSD Dialect |
| --- | --- | --- | --- |
| 1.0 to 1.2 | read/write | read | - |
| 1.3 and later | read/write | read | read/write |

It is not possible to detect the end of an AR archive in a
reliable way so `ArArchiveInputStream` will read
until it reaches the end of the stream or fails to parse the
stream's content as AR entries.

<a id="examples--arj"></a>

## arj

Note that Commons Compress doesn't support compressed, encrypted or multi-volume ARJ archives, yet.

Uncompressing a given arj archive (you would
certainly add exception handling and make sure all streams
get closed properly):

```

ArjArchiveEntry entry = arjInput.getNextEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    arjInput.read(content, offset, content.length - offset);
}
```

<a id="examples--cpio"></a>

## cpio

In addition to the information stored
in `ArchiveEntry` a `CpioArchiveEntry`
stores various attributes including information about the
original owner and permissions.

The cpio package supports the "new portable" as well as the
"old" format of CPIO archives in their binary, ASCII and
"with CRC" variants.

Adding an entry to a cpio archive:

```

CpioArchiveEntry entry = new CpioArchiveEntry(name, size);
cpioOutput.putArchiveEntry(entry);
cpioOutput.write(contentOfEntry);
cpioOutput.closeArchiveEntry();
```

Reading entries from an cpio archive:

```

CpioArchiveEntry entry = cpioInput.getNextCPIOEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    cpioInput.read(content, offset, content.length - offset);
}
```

Traditionally CPIO archives are written in blocks of 512
bytes - the block size is a configuration parameter of the
`Cpio*Stream`'s constructors. Starting with version
1.5 `CpioArchiveInputStream` will consume the
padding written to fill the current block when the end of the
archive is reached. Unfortunately many CPIO implementations
use larger block sizes so there may be more zero-byte padding
left inside the original input stream after the archive has
been consumed completely.

<a id="examples--jar"></a>

## jar

In general, JAR archives are ZIP files, so the JAR package
supports all options provided by the [ZIP](#examples--zip) package.

To be interoperable JAR archives should always be created
using the UTF-8 encoding for file names (which is the
default).

Archives created using `JarArchiveOutputStream`
will implicitly add a `JarMarker` extra field to
the very first archive entry of the archive which will make
Solaris recognize them as Java archives and allows them to
be used as executables.

Note that `ArchiveStreamFactory` doesn't
distinguish ZIP archives from JAR archives, so if you use
the one-argument `createArchiveInputStream`
method on a JAR archive, it will still return the more
generic `ZipArchiveInputStream`.

The `JarArchiveEntry` class contains fields for
certificates and attributes that are planned to be supported
in the future but are not supported as of Compress 1.0.

Adding an entry to a jar archive:

```

JarArchiveEntry entry = new JarArchiveEntry(name, size);
entry.setSize(size);
jarOutput.putArchiveEntry(entry);
jarOutput.write(contentOfEntry);
jarOutput.closeArchiveEntry();
```

Reading entries from an jar archive:

```

JarArchiveEntry entry = jarInput.getNextJarEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    jarInput.read(content, offset, content.length - offset);
}
```

<a id="examples--dump"></a>

## dump

In addition to the information stored
in `ArchiveEntry` a `DumpArchiveEntry`
stores various attributes including information about the
original owner and permissions.

As of Commons Compress 1.3 only dump archives using the
new-fs format - this is the most common variant - are
supported. Right now this library supports uncompressed and
ZLIB compressed archives and can not write archives at
all.

Reading entries from an dump archive:

```

DumpArchiveEntry entry = dumpInput.getNextDumpEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    dumpInput.read(content, offset, content.length - offset);
}
```

Prior to version 1.5 `DumpArchiveInputStream`
would close the original input once it had read the last
record. Starting with version 1.5 it will not close the
stream implicitly.

<a id="examples--tar"></a>

## tar

The TAR package has a [dedicated
documentation page](#tar).

Adding an entry to a tar archive:

```

TarArchiveEntry entry = new TarArchiveEntry(name);
entry.setSize(size);
tarOutput.putArchiveEntry(entry);
tarOutput.write(contentOfEntry);
tarOutput.closeArchiveEntry();
```

Reading entries from an tar archive:

```

TarArchiveEntry entry = tarInput.getNextTarEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    tarInput.read(content, offset, content.length - offset);
}
```

<a id="examples--zip"></a>

## zip

The ZIP package has a [dedicated
documentation page](#zip).

Adding an entry to a zip archive:

```

ZipArchiveEntry entry = new ZipArchiveEntry(name);
entry.setSize(size);
zipOutput.putArchiveEntry(entry);
zipOutput.write(contentOfEntry);
zipOutput.closeArchiveEntry();
```

`ZipArchiveOutputStream` can use some internal
optimizations exploiting `SeekableByteChannel` if it
knows it is writing to a seekable output rather than a non-seekable
stream. If you are writing to a file, you should use the
constructor that accepts a `File` or
`SeekableByteChannel` argument rather
than the one using an `OutputStream` or the
factory method in `ArchiveStreamFactory`.

Reading entries from an zip archive:

```

ZipArchiveEntry entry = zipInput.getNextZipEntry();
byte[] content = new byte[entry.getSize()];
LOOP UNTIL entry.getSize() HAS BEEN READ {
    zipInput.read(content, offset, content.length - offset);
}
```

Reading entries from an zip archive using the
recommended `ZipFile` class:

```

ZipArchiveEntry entry = zipFile.getEntry(name);
InputStream content = zipFile.getInputStream(entry);
try {
    READ UNTIL content IS EXHAUSTED
} finally {
    content.close();
}
```

Reading entries from an in-memory zip archive using
`SeekableInMemoryByteChannel` and `ZipFile` class:

```

byte[] inputData; // zip archive contents
SeekableInMemoryByteChannel inMemoryByteChannel = new SeekableInMemoryByteChannel(inputData);
ZipFile zipFile = new ZipFile(inMemoryByteChannel);
ZipArchiveEntry archiveEntry = zipFile.getEntry("entryName");
InputStream inputStream = zipFile.getInputStream(archiveEntry);
inputStream.read() // read data from the input stream
```

Creating a zip file with multiple threads:

A simple implementation to create a zip file might look like this:

```
public class ScatterSample {
ParallelScatterZipCreator scatterZipCreator = new ParallelScatterZipCreator(); ScatterZipOutputStream dirs = ScatterZipOutputStream.fileBased(File.createTempFile("scatter-dirs", "tmp"));
public ScatterSample() throws IOException {}
public void addEntry(ZipArchiveEntry zipArchiveEntry, InputStreamSupplier streamSupplier) throws IOException {if (zipArchiveEntry.isDirectory() && !zipArchiveEntry.isUnixSymlink()) dirs.addArchiveEntry(ZipArchiveEntryRequest.createZipArchiveEntryRequest(zipArchiveEntry, streamSupplier)); else scatterZipCreator.addArchiveEntry( zipArchiveEntry, streamSupplier);}
public void writeTo(ZipArchiveOutputStream zipArchiveOutputStream) throws IOException, ExecutionException, InterruptedException {dirs.writeTo(zipArchiveOutputStream); dirs.close(); scatterZipCreator.writeTo(zipArchiveOutputStream);}}
```

<a id="examples--compressors"></a>

# Compressors

<a id="examples--concatenated-streams"></a>

## Concatenated Streams

For the bzip2, gzip and XZ formats as well as the framed
lz4 format a single compressed file
may actually consist of several streams that will be
concatenated by the command line utilities when decompressing
them. Starting with Commons Compress 1.4 the
`*CompressorInputStream`s for these formats support
concatenating streams as well, but they won't do so by
default. You must use the two-arg constructor and explicitly
enable the support.

<a id="examples--brotli"></a>

## Brotli

The implementation of this package is provided by the
[Google Brotli dec](https://github.com/google/brotli) library.

Uncompressing a given Brotli compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.br"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
BrotliCompressorInputStream brIn = new BrotliCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = brIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
brIn.close();
```

<a id="examples--bzip2"></a>

## bzip2

Note that `BZipCompressorOutputStream` keeps
hold of some big data structures in memory. While it is
recommended for *any* stream that you close it as soon as
you no longer need it, this is even more important
for `BZipCompressorOutputStream`.

Uncompressing a given bzip2 compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.bz2"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
BZip2CompressorInputStream bzIn = new BZip2CompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = bzIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
bzIn.close();
```

Compressing a given file using bzip2 (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.bz2"));
BufferedOutputStream out = new BufferedOutputStream(fout);
BZip2CompressorOutputStream bzOut = new BZip2CompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    bzOut.write(buffer, 0, n);
}
bzOut.close();
in.close();
```

<a id="examples--deflate"></a>

## DEFLATE

The implementation of the DEFLATE/INFLATE code used by this
package is provided by the `java.util.zip` package
of the Java class library.

Uncompressing a given DEFLATE compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("some-file"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
DeflateCompressorInputStream defIn = new DeflateCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = defIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
defIn.close();
```

Compressing a given file using DEFLATE (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("some-file"));
BufferedOutputStream out = new BufferedOutputStream(fout);
DeflateCompressorOutputStream defOut = new DeflateCompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    defOut.write(buffer, 0, n);
}
defOut.close();
in.close();
```

<a id="examples--deflate64"></a>

## DEFLATE64

Uncompressing a given DEFLATE64 compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("some-file"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
Deflate64CompressorInputStream defIn = new Deflate64CompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = defIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
defIn.close();
```

<a id="examples--gzip"></a>

## gzip

The implementation of the DEFLATE/INFLATE code used by this
package is provided by the `java.util.zip` package
of the Java class library.

Uncompressing a given gzip compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.gz"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
GzipCompressorInputStream gzIn = new GzipCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = gzIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
gzIn.close();
```

Compressing a given file using gzip (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.gz"));
BufferedOutputStream out = new BufferedOutputStream(fout);
GzipCompressorOutputStream gzOut = new GzipCompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    gzOut.write(buffer, 0, n);
}
gzOut.close();
in.close();
```

<a id="examples--lz4"></a>

## LZ4

There are two different "formats" used for [lz4](http://lz4.github.io/lz4/). The format called
"block format" only contains the raw compressed data while the
other provides a higher level "frame format" - Commons
Compress offers two different stream classes for reading or
writing either format.

Uncompressing a given framed LZ4 file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.lz4"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
FramedLZ4CompressorInputStream zIn = new FramedLZ4CompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = zIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
zIn.close();
```

Compressing a given file using the LZ4 frame format (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.lz4"));
BufferedOutputStream out = new BufferedOutputStream(fout);
FramedLZ4CompressorOutputStream lzOut = new FramedLZ4CompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    lzOut.write(buffer, 0, n);
}
lzOut.close();
in.close();
```

<a id="examples--lzma"></a>

## lzma

The implementation of this package is provided by the
public domain [XZ
for Java](https://tukaani.org/xz/java.html) library.

Uncompressing a given LZMA compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.lzma"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
LZMACompressorInputStream lzmaIn = new LZMACompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = xzIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
lzmaIn.close();
```

Compressing a given file using LZMA (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.lzma"));
BufferedOutputStream out = new BufferedOutputStream(fout);
LZMACompressorOutputStream lzOut = new LZMACompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    lzOut.write(buffer, 0, n);
}
lzOut.close();
in.close();
```

<a id="examples--pack200"></a>

## Pack200

The Pack200 package has a [dedicated
documentation page](#pack200).

The implementation of this package used to be provided by
the `java.util.zip` package of the Java class
library. Starting with Compress 1.21 the implementation uses
a copy of the pack200 code of the now retired Apache
Harmony™ project that ships with Compress itself.

Uncompressing a given pack200 compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.pack"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.jar"));
Pack200CompressorInputStream pIn = new Pack200CompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = pIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
pIn.close();
```

Compressing a given jar using pack200 (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.jar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.pack"));
BufferedOutputStream out = new BufferedInputStream(fout);
Pack200CompressorOutputStream pOut = new Pack200CompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    pOut.write(buffer, 0, n);
}
pOut.close();
in.close();
```

<a id="examples--snappy"></a>

## Snappy

There are two different "formats" used for [Snappy](https://github.com/google/snappy/), one only
contains the raw compressed data while the other provides a
higher level "framing format" - Commons Compress offers two
different stream classes for reading either format.

Starting with 1.12 we've added support for different
dialects of the framing format that can be specified when
constructing the stream. The `STANDARD` dialect
follows the "framing format" specification while the
`IWORK_ARCHIVE` dialect can be used to parse IWA
files that are part of Apple's iWork 13 format. If no dialect
has been specified, `STANDARD` is used. Only the
`STANDARD` format can be detected by
`CompressorStreamFactory`.

Uncompressing a given framed Snappy file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.sz"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
FramedSnappyCompressorInputStream zIn = new FramedSnappyCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = zIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
zIn.close();
```

Compressing a given file using framed Snappy (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.sz"));
BufferedOutputStream out = new BufferedOutputStream(fout);
FramedSnappyCompressorOutputStream snOut = new FramedSnappyCompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    snOut.write(buffer, 0, n);
}
snOut.close();
in.close();
```

<a id="examples--xz"></a>

## XZ

The implementation of this package is provided by the
public domain [XZ
for Java](https://tukaani.org/xz/java.html) library.

When you try to open an XZ stream for reading using
`CompressorStreamFactory`, Commons Compress will
check whether the XZ for Java library is available. Starting
with Compress 1.9 the result of this check will be cached
unless Compress finds OSGi classes in its classpath. You can
use `XZUtils#setCacheXZAvailability` to override
this default behavior.

Uncompressing a given XZ compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.xz"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
XZCompressorInputStream xzIn = new XZCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = xzIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
xzIn.close();
```

Compressing a given file using XZ (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.xz"));
BufferedOutputStream out = new BufferedInputStream(fout);
XZCompressorOutputStream xzOut = new XZCompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    xzOut.write(buffer, 0, n);
}
xzOut.close();
in.close();
```

<a id="examples--z"></a>

## Z

Uncompressing a given Z compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.Z"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
ZCompressorInputStream zIn = new ZCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = zIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
zIn.close();
```

<a id="examples--zstandard"></a>

## Zstandard

The implementation of this package is provided by the
[Zstandard JNI](https://github.com/luben/zstd-jni) library.

Uncompressing a given Zstandard compressed file (you would
certainly add exception handling and make sure all streams
get closed properly):

```

InputStream fin = Files.newInputStream(Paths.get("archive.tar.zstd"));
BufferedInputStream in = new BufferedInputStream(fin);
OutputStream out = Files.newOutputStream(Paths.get("archive.tar"));
ZstdCompressorInputStream zsIn = new ZstdCompressorInputStream(in);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = zsIn.read(buffer))) {
    out.write(buffer, 0, n);
}
out.close();
zsIn.close();
```

Compressing a given file using the Zstandard format (you
would certainly add exception handling and make sure all
streams get closed properly):

```

InputStream in = Files.newInputStream(Paths.get("archive.tar"));
OutputStream fout = Files.newOutputStream(Paths.get("archive.tar.zstd"));
BufferedOutputStream out = new BufferedOutputStream(fout);
ZstdCompressorOutputStream zOut = new ZstdCompressorOutputStream(out);
final byte[] buffer = new byte[buffersize];
int n = 0;
while (-1 != (n = in.read(buffer))) {
    zOut.write(buffer, 0, n);
}
zOut.close();
in.close();
```

<a id="examples--extending-commons-compress"></a>

# Extending Commons Compress

Starting in release 1.13, it is now possible to add Compressor- and ArchiverStream implementations using the
Java's [ServiceLoader](https://docs.oracle.com/javase/7/docs/api/java/util/ServiceLoader.html)
mechanism.

<a id="examples--extending-commons-compress-compressors"></a>

## Extending Commons Compress Compressors

To provide your own compressor, you must make available on the classpath a file called
`META-INF/services/org.apache.commons.compress.compressors.CompressorStreamProvider`.

This file MUST contain one fully-qualified class name per line.

For example:

```
org.apache.commons.compress.compressors.TestCompressorStreamProvider
```

This class MUST implement the Commons Compress interface
[org.apache.commons.compress.compressors.CompressorStreamProvider](https://commons.apache.org/proper/commons-compress/apidocs/org/apache/commons/compress/compressors/CompressorStreamProvider.html).

<a id="examples--extending-commons-compress-archivers"></a>

## Extending Commons Compress Archivers

To provide your own compressor, you must make available on the classpath a file called
`META-INF/services/org.apache.commons.compress.archivers.ArchiveStreamProvider`.

This file MUST contain one fully-qualified class name per line.

For example:

```
org.apache.commons.compress.archivers.TestArchiveStreamProvider
```

This class MUST implement the Commons Compress interface
[org.apache.commons.compress.archivers.ArchiveStreamProvider](https://commons.apache.org/proper/commons-compress/apidocs/org/apache/commons/compress/archivers/ArchiveStreamProvider.html).

---

<a id="limitations"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/limitations.html -->

<!-- page_index: 5 -->

<a id="limitations--general"></a>

# General

This page lists the known limitations and problems of Apache
Commons Compress™ grouped by the archiving/compression
format they apply to.

- Several implementations of decompressors and unarchivers will
  invoke [`skip`](https://docs.oracle.com/javase/10/docs/api/java/io/InputStream.html#skip(long))
  on the underlying `InputStream` which may throw an
  `IOException` in some stream implementations. One
  known case where this happens is when using
  `System.in` as input. If you encounter an
  exception with a message like "Illegal seek" we recommend you
  wrap your stream in a `SkipShieldingInputStream`
  from our utils package before passing it to Compress.
- Commons Compress prior to 1.21 cannot be built on JDK 14 or newer.

<a id="limitations--7z"></a>

# 7Z

- the format requires the otherwise optional [XZ for Java](https://tukaani.org/xz/java.html)
  library.
- only `File`s are supported as input/output,
  not streams. Starting with Compress 1.13
  `SeekableByteChannel` is supported as well.
- In Compress 1.7
  `ArchiveStreamFactory` will not auto-detect 7z
  archives, starting with 1.8 it will throw a
  `StreamingNotSupportedException` when reading from
  a 7z archive.
- Encryption, solid compression and header compression
  are only supported when reading archives
- Commons Compress 1.12 and earlier didn't support writing
  LZMA.
- Several of the "methods" supported by 7z are not
  implemented in Compress.
- No support for writing multi-volume archives. Such
  archives can be read by simply concatenating the parts, for
  example by using
  `MultiReadOnlySeekableByteChannel`.
- Support for some BCJ filters and the DELTA filter has
  been added with Compress 1.8. Because of a known bug in
  version 1.4 of the [XZ for Java](https://tukaani.org/xz/java.html)
  library, archives using BCJ filters will cause an
  `AssertionError` when read. If you need support
  for BCJ filters you must use XZ for Java 1.5 or later.

<a id="limitations--ar"></a>

# AR

- AR archives can not contain directories - this is a
  limitation of the format rather than one of Compress'
  implementation.
- file names longer than 16 characters are only fully
  supported using the BSD dialect, the GNU/SRV4 dialect is only
  supported when reading archives.

<a id="limitations--arj"></a>

# ARJ

- read-only support
- no support for compression, encryption or multi-volume
  archives

<a id="limitations--brotli"></a>

# Brotli

- the format requires the otherwise optional [Google Brotli dec](https://github.com/google/brotli)
  library.
- read-only support
- `CompressorStreamFactory` is not able to auto-detect
  streams using Brotli compression.

<a id="limitations--bzip2"></a>

# BZIP2

Versions of Compress prior to 1.4.1 are vulnerable to a
possible denial of service attack, see the [Security Reports](#security) page for details.

<a id="limitations--cpio"></a>

# CPIO

We are not aware of any problems.

<a id="limitations--deflate"></a>

# DEFLATE

- `CompressorStreamFactory` is not able to auto-detect
  streams using DEFLATE compression.

<a id="limitations--deflate64"></a>

# DEFLATE64

- `CompressorStreamFactory` is not able to auto-detect
  streams using DEFLATE64 compression.
- read-only support

<a id="limitations--dump"></a>

# DUMP

- read-only support
- only the new-fs format is supported
- the only compression algorithm supported is zlib

<a id="limitations--gzip"></a>

# GZIP

We are not aware of any problems.

<a id="limitations--jar"></a>

# JAR

JAR archives are special ZIP archives, all limitations of [ZIP](#limitations--zip) apply to JAR as well.

- `ArchiveStreamFactory` cannot tell JAR
  archives from ZIP archives and will not auto-detect
  JARs.
- Compress doesn't provide special access to the archive's
  MANIFEST

<a id="limitations--lz4"></a>

# LZ4

- In theory LZ4 compressed streams can contain literals and
  copies of arbitrary length while Commons Compress only
  supports sizes up to 263 - 1 (i.e. ≈ 9.2
  EB).

<a id="limitations--lzma"></a>

# LZMA

- the format requires the otherwise optional [XZ for Java](https://tukaani.org/xz/java.html)
  library.
- Commons Compress 1.12 and earlier only support reading
  the format

<a id="limitations--pack200"></a>

# PACK200

- Pack200 support in Commons Compress prior to 1.21 relies on the
  `Pack200` class of the Java classlib. Java 14
  removed support and thus Pack200 will not work at all when
  running on Java 14 or later.

  Starting with Commons Compress 1.21 the classlib
  implementation is no longer used at all, instead Commons
  Compress contains the pack200 code of the retired Apache
  Harmony™ project.

<a id="limitations--snappy"></a>

# SNAPPY

- Commons Compress 1.13 and earlier only support reading
  the format

<a id="limitations--tar"></a>

# TAR

- sparse files could not be read in version prior to
  Compress 1.20
- sparse files can not be written
- only a subset of the GNU and POSIX extensions are
  supported
- In Compress 1.6 `TarArchiveInputStream` could
  fail to read the full contents of an entry unless the stream
  was wrapped in a buffering stream.

<a id="limitations--xz"></a>

# XZ

- the format requires the otherwise optional [XZ for Java](https://tukaani.org/xz/java.html)
  library.

<a id="limitations--z"></a>

# Z

- Prior to Compress 1.8.1
  `CompressorStreamFactory` was not able to
  auto-detect streams using .Z compression.
- read-only support

<a id="limitations--zip"></a>

# ZIP

- `ZipArchiveInputStream` is limited and may
  even return false contents in some cases, use
  `ZipFile` whenever possible. See [the ZIP
  documentation page](#zip--ziparchiveinputstream_vs_zipfile) for details. This limitation is a
  result of streaming data vs using random access and not a
  limitation of Compress' specific implementation.
- only a subset of compression methods are supported,
  including the most common STORED and DEFLATEd. IMPLODE,
  SHRINK, DEFLATE64 and BZIP2 support is read-only.
- no support for encryption
- no support for multi-volume archives prior to Compress 1.20
- It is currently not possible to write split archives with
  more than 64k segments. When creating split archives with more
  than 100 segments you will need to adjust the file names as
  `ZipArchiveOutputStream` assumes extensions will be
  three characters long.
- In versions prior to Compress 1.6
  `ZipArchiveEntries` read from an archive will
  contain non-zero millisecond values when using Java 8 or later rather
  than the expected two-second granularity.
- Compress 1.7 has a known bug where the very first entry
  of an archive will not be read correctly by
  `ZipArchiveInputStream` if it used the STORED
  method.
- `ZipArchiveEntry#getLastModifiedDate` uses
  `ZipEntry#getTime` under the covers which may
  return different times for the same archive when using
  different versions of Java.
- In versions of Compress prior to 1.16 a specially crafted
  ZIP archive can be used to cause an infinite loop inside of
  Compress' extra field parser used by the `ZipFile`
  and `ZipArchiveInputStream` classes. This can be
  used to mount a denial of service attack against services
  that use Compress' zip package. See the [Security Reports](#security) page for
  details.

<a id="limitations--zstandard"></a>

# Zstandard

- the format requires the otherwise optional [Zstandard JNI](https://github.com/luben/zstd-jni)
  library.

---

<a id="conventions"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/conventions.html -->

<!-- page_index: 6 -->

<a id="conventions--code-style"></a>

# Code Style

The developers of this component decided to follow the recommended standards
but not to include Checkstyle (or similar tools) into Commons Compress.

<a id="conventions--multithreading"></a>

# Multithreading

Commons Compress does not aim to be threadsafe at the moment. But the developers
agreed to document multithreading behavior in the javadocs.

We use some of the annotations from
[JCIP](http://jcip.net/annotations/doc/net/jcip/annotations/package-summary.html)
as Javadoc tags. The used tags are:

- @GuardedBy (field or method)
- @Immutable (class)
- @NotThreadSafe (class)
- @ThreadSafe (class)

For example:

```
/** * Utility class that represents a four byte integer with conversion * rules for the big endian byte order of ZIP files.* * @Immutable */ public final class ZipLong implements Cloneable {
```

and:

```
 
private final char [] highChars;
//@GuardedBy("this")
private Simple8BitZipEncoding encoding;
            
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/project-info.html -->

<!-- page_index: 7 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Compress defines an API for working with compression and archive formats. These include bzip2, gzip, pack200, LZMA, XZ, Snappy, traditional Unix Compress, DEFLATE, DEFLATE64, LZ4, Brotli, Zstandard and ar, cpio, jar, tar, zip, dump, 7z, arj. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-compress/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-compress/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-compress/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-compress/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-compress/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-compress/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-compress/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/summary.html -->

<!-- page_index: 8 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Compress |
| Description | Apache Commons Compress defines an API for working with compression and archive formats. These include bzip2, gzip, pack200, LZMA, XZ, Snappy, traditional Unix Compress, DEFLATE, DEFLATE64, LZ4, Brotli, Zstandard and ar, cpio, jar, tar, zip, dump, 7z, arj. |
| Homepage | [https://commons.apache.org/proper/commons-compress/](#index) |

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
| ArtifactId | commons-compress |
| Version | 1.28.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/team.html -->

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
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | tcurdt | Torsten Curdt | [tcurdt at apache.org](mailto:tcurdt at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | bodewig | Stefan Bodewig | [bodewig at apache.org](mailto:bodewig at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | sebb | Sebastian Bazley | [sebb at apache.org](mailto:sebb at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | grobmeier | Christian Grobmeier | [grobmeier at apache.org](mailto:grobmeier at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | julius | Julius Davies | [julius at apache.org](mailto:julius at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | damjan | Damjan Jovanovic | [damjan at apache.org](mailto:damjan at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | ebourg | Emmanuel Bourg | [ebourg at apache.org](mailto:ebourg at apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | chtompki | Rob Tompkins | [chtompki at apache.org](mailto:chtompki at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | peterlee | Peter Alfred Lee | [peterlee at apache.org](mailto:peterlee at apache.org) | - | - | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | Wolfgang Glas | [wolfgang.glas at ev-i.at](mailto:wolfgang.glas at ev-i.at) |
| ![](assets/images/e4b53ad57fb412b9a77cd4d661d63fff_ac2e83ad576ec5c5.jpg) | Christian Kohlschütte | [ck@newsclub.de](mailto:ck@newsclub.de) |
| ![](assets/images/2166ab2d8442a987e597d08120d6d3f7_76f87e435d62beaa.jpg) | Bear Giles | [bgiles@coyotesong.com](mailto:bgiles@coyotesong.com) |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | Michael Kuss | [mail at michael minus kuss.de](mailto:mail at michael minus kuss.de) |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | Lasse Collin | [lasse.collin@tukaani.org](mailto:lasse.collin@tukaani.org) |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | John Kodis | - |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | BELUGA BEHR | - |
| ![](assets/images/7526ce341af0093827dfe8c9cc709c4e_c457f0a8d754e9c8.jpg) | Simon Spero | [sesuncedu@gmail.com](mailto:sesuncedu@gmail.com) |
| ![](assets/images/12caa3bfb415c505d9e5fd704c2f0362_585b3c262acb74bc.jpg) | Michael Hausegger | [hausegger.michael@googlemail.com](mailto:hausegger.michael@googlemail.com) |
| ![](assets/images/00000000000000000000000000000000_5b117bb3ce65cb58.jpg) | Arturo Bernal | [arturobernalg@yahoo.com](mailto:arturobernalg@yahoo.com) |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-compress/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="pack200"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/pack200.html -->

<!-- page_index: 11 -->

<a id="pack200--the-pack200-package"></a>

# The Pack200 package

The Pack200 algorithm is not a general purpose compression
algorithm but one specialized for compressing JAR archives. JAR
archives compressed with Pack200 will in general be different
from the original archive when decompressed again. More
information can be found in the Javadocs of the [Pack200.Packer
class](https://docs.oracle.com/javase/7/docs/api/java/util/jar/Pack200.Packer.html).

While the `pack200` command line utility of the
JDK creates GZip compressed archives (`.pack.gz`) by
default, the streams provided by the Pack200 package only
perform the actual Pack200 operation. Wrap them in an
additional `GzipCompressor(In|Out)putStream` in order to deal
with deflated streams.

<a id="pack200--pack200strategy"></a>

## Pack200Strategy

The Pack200-API provided by the java class library is not
streaming friendly as it wants to consume its input completely
in a single operation. Because of this
`Pack200CompressorInputStream`'s constructor will immediately
unpack the stream, cache the results and provide an input
stream to the cache.

`Pack200CompressorOutputStream` will cache all data that
is written to it and then pack it once the `finish`
or `close` method is called.

Two different caching modes are available - "in memory", which is the default, and "temporary file". By default data
is cached in memory but you should switch to the temporary
file option if your archives are really big.

Given there always is an intermediate result
the `getBytesRead` and `getCount`
methods of `Pack200CompressorInputStream` are
meaningless (read from the real stream or from the
intermediate result?) and always return 0.

<a id="pack200--normalization"></a>

## Normalization

As a pack/unpack cycle may create a JAR archive that is
different from the original, digital signatures created for
the initial JAR will be broken by the process. There is a way
to "normalize" JAR archives prior to packing them that ensures
signatures applied to the "normalized" JAR will still be valid
aftre a pack/unpack cycle - see [Pack200.Packer](https://download.oracle.com/javase/7/docs/api/java/util/jar/Pack200.Packer.html)'s
javadocs.

The `Pack200Utils` class in the
`pack200` package provides several overloads of a
`normalize` method that can be used to prepare a
JAR archive in place or to a separate file.

---

<a id="tar"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/tar.html -->

<!-- page_index: 12 -->

<a id="tar--the-tar-package"></a>

# The TAR package

In addition to the information stored
in `ArchiveEntry` a `TarArchiveEntry`
stores various attributes including information about the
original owner and permissions.

There are several different dialects of the TAR format, maybe
even different TAR formats. The tar package contains special
cases in order to read many of the existing dialects and will by
default try to create archives in the original format (often
called "ustar"). This original format didn't support file names
longer than 100 characters or bigger than 8 GiB and the tar
package will by default fail if you try to write an entry that
goes beyond those limits. "ustar" is the common denominator of
all the existing tar dialects and is understood by most of the
existing tools.

The tar package does not support the full POSIX tar standard
nor more modern GNU extension of said standard.

<a id="tar--long-file-names"></a>

## Long File Names

The `longFileMode` option of
`TarArchiveOutputStream` controls how files with
names longer than 100 characters are handled. The possible
choices are:

- `LONGFILE_ERROR`: throw an exception if such a
  file is added. This is the default.
- `LONGFILE_TRUNCATE`: truncate such names.
- `LONGFILE_GNU`: use a GNU tar variant now
  referred to as "oldgnu" of storing such names. If you choose
  the GNU tar option, the archive can not be extracted using
  many other tar implementations like the ones of OpenBSD,
  Solaris or MacOS X.
- `LONGFILE_POSIX`: use a PAX [extended
  header](http://pubs.opengroup.org/onlinepubs/009695399/utilities/pax.html#tag_04_100_13_03) as defined by POSIX 1003.1. Most modern tar
  implementations are able to extract such archives. *since
  Commons Compress 1.4*

`TarArchiveInputStream` will recognize the GNU
tar as well as the POSIX extensions (starting with Commons
Compress 1.2) for long file names and reads the longer names
transparently.

<a id="tar--big-numeric-values"></a>

## Big Numeric Values

The `bigNumberMode` option of
`TarArchiveOutputStream` controls how files larger
than 8GiB or with other big numeric values that can't be
encoded in traditional header fields are handled. The
possible choices are:

- `BIGNUMBER_ERROR`: throw an exception if such an
  entry is added. This is the default.
- `BIGNUMBER_STAR`: use a variant first
  introduced by Jörg Schilling's [star](http://developer.berlios.de/projects/star)
  and later adopted by GNU and BSD tar. This method is not
  supported by all implementations.
- `BIGNUMBER_POSIX`: use a PAX [extended
  header](http://pubs.opengroup.org/onlinepubs/009695399/utilities/pax.html#tag_04_100_13_03) as defined by POSIX 1003.1. Most modern tar
  implementations are able to extract such archives.

Starting with Commons Compress 1.4
`TarArchiveInputStream` will recognize the star as
well as the POSIX extensions for big numeric values and reads them
transparently.

<a id="tar--file-name-encoding"></a>

## File Name Encoding

The original ustar format only supports 7-Bit ASCII file
names, later implementations use the platform's default
encoding to encode file names. The POSIX standard recommends
using PAX extension headers for non-ASCII file names
instead.

Commons Compress 1.1 to 1.3 assumed file names would be
encoded using ISO-8859-1. Starting with Commons Compress 1.4
you can specify the encoding to expect (to use when writing)
as a parameter to `TarArchiveInputStream`
(`TarArchiveOutputStream`), it now defaults to the
platform's default encoding.

Since Commons Compress 1.4 another optional parameter -
`addPaxHeadersForNonAsciiNames` - of
`TarArchiveOutputStream` controls whether PAX
extension headers will be written for non-ASCII file names.
By default they will not be written to preserve space.
`TarArchiveInputStream` will read them
transparently if present.

<a id="tar--sparse-files"></a>

## Sparse files

Prior to Commons Compress 1.20 `TarArchiveInputStream` would recognize sparse
file entries stored using the "oldgnu" format
(`--sparse-version=0.0` in GNU tar) but not
able to extract them correctly. Starting with Commons Compress 1.20
all GNU and POSIX variants of sparse files are recognized and
can be read.

<a id="tar--consuming-archives-completely"></a>

## Consuming Archives Completely

The end of a tar archive is signaled by two consecutive
records of all zeros. Unfortunately not all tar
implementations adhere to this and some only write one record
to end the archive. Commons Compress will always write two
records but stop reading an archive as soon as finds one
record of all zeros.

Prior to version 1.5 this could leave the second EOF record
inside the stream when `getNextEntry` or
`getNextTarEntry` returned `null`
Starting with version 1.5 `TarArchiveInputStream`
will try to read a second record as well if present, effectively consuming the archive completely.

<a id="tar--pax-extended-header"></a>

## PAX Extended Header

The tar package has supported reading PAX extended headers
since 1.3 for local headers and 1.11 for global headers. The
following entries of PAX headers are applied when reading:

path
:   set the entry's name

linkpath
:   set the entry's link name

gid
:   set the entry's group id

gname
:   set the entry's group name

uid
:   set the entry's user id

uname
:   set the entry's user name

size
:   set the entry's size

mtime
:   set the entry's modification time

SCHILY.devminor
:   set the entry's minor device number

SCHILY.devmajor
:   set the entry's major device number

in addition some fields used by GNU tar and star used to
signal sparse entries are supported and are used for the
`is*GNUSparse` and `isStarSparse`
methods.

Some PAX extra headers may be set when writing archives, for example for non-ASCII names or big numeric values. This
depends on various setting of the output stream - see the
previous sections.

Since 1.15 you can directly access all PAX extension
headers that have been found when reading an entry or specify
extra headers to be written to a (local) PAX extended header
entry.

Some hints if you try to set extended headers:

- pax header keywords should be ascii. star/gnutar
  (SCHILY.xattr.\* ) do not check for this. libarchive/bsdtar
  (LIBARCHIVE.xattr.\*) uses URL-Encoding.
- pax header values should be encoded as UTF-8 characters
  (including trailing `\0`). star/gnutar
  (SCHILY.xattr.\*) do not check for this. libarchive/bsdtar
  (LIBARCHIVE.xattr.\*) encode values using Base64.
- libarchive/bsdtar will read SCHILY.xattr headers, but
  will not generate them.
- gnutar will complain about LIBARCHIVE.xattr (and any
  other unknown) headers and will neither encode nor decode
  them.

<a id="tar--random-access"></a>

## Random Access

Starting with Commons Compress 1.21 the tar package
contains a `TarFile` class that provides random
access to archives. Except for the ability to access entries
out of order `TarFile` is not superior to
`TarArchiveInputStream`.

---

<a id="zip"></a>

<!-- source_url: https://commons.apache.org/proper/commons-compress/zip.html -->

<!-- page_index: 13 -->

<a id="zip--the-zip-package"></a>

# The ZIP package

The ZIP package provides features not found
in `java.util.zip`:

- Support for encodings other than UTF-8 for filenames and
  comments. Starting with Java7 this is supported
  by `java.util.zip` as well.
- Access to internal and external attributes (which are used
  to store Unix permission by some zip implementations).
- Structured support for extra fields.

In addition to the information stored
in `ArchiveEntry` a `ZipArchiveEntry`
stores internal and external attributes as well as extra
fields which may contain information like Unix permissions, information about the platform they've been created on, their
last modification time and an optional comment.

<a id="zip--ziparchiveinputstream-vs-zipfile"></a>

## ZipArchiveInputStream vs ZipFile

ZIP archives store archive entries in sequence and
contain a registry of all entries at the very end of the
archive. It is acceptable for an archive to contain several
entries of the same name and have the registry (called the
central directory) decide which entry is actually to be used
(if any).

In addition the ZIP format stores certain information only
inside the central directory but not together with the entry
itself, this is:

- internal and external attributes
- different or additional extra fields

This means the ZIP format cannot really be parsed
correctly while reading a non-seekable stream, which is what
`ZipArchiveInputStream` is forced to do. As a
result `ZipArchiveInputStream`

- may return entries that are not part of the central
  directory at all and shouldn't be considered part of the
  archive.
- may return several entries with the same name.
- will not return internal or external attributes.
- may return incomplete extra field data.
- may return unknown sizes and CRC values for entries
  until the next entry has been reached if the archive uses
  the data descriptor feature (see below).
- can not skip over bytes that occur before the real zip
  stream. This means self-extracting zips as they are created
  by some tools can not be read using
  `ZipArchiveInputStream` at all. This also applies
  to Chrome extension archives, for example.

`ZipArchiveInputStream` shares these limitations
with `java.util.zip.ZipInputStream`.

`ZipFile` is able to read the central directory
first and provide correct and complete information on any
ZIP archive.

ZIP archives know a feature called the data descriptor
which is a way to store an entry's length after the entry's
data. This can only work reliably if the size information
can be taken from the central directory or the data itself
can signal it is complete, which is true for data that is
compressed using the DEFLATED compression algorithm.

`ZipFile` has access to the central directory
and can extract entries using the data descriptor reliably.
The same is true for `ZipArchiveInputStream` as
long as the entry is DEFLATED. For STORED
entries `ZipArchiveInputStream` can try to read
ahead until it finds the next entry, but this approach is
not safe and has to be enabled by a constructor argument
explicitly. For example it will completely fail if the
stored entry is a ZIP archive itself. Starting with Compress 1.19
`ZipArchiveInputStream` will perform a few sanity
checks for STORED entries with data descriptors and throw an
exception if they fail.

If possible, you should **always** prefer `ZipFile`
over `ZipArchiveInputStream`.

`ZipFile` requires a
`SeekableByteChannel` that will be obtained
transparently when reading from a file. The class
`org.apache.commons.compress.utils.SeekableInMemoryByteChannel`
allows you to read from an in-memory archive.

<a id="zip--ziparchiveoutputstream"></a>

## ZipArchiveOutputStream

`ZipArchiveOutputStream` has four constructors, two of them uses a `File` argument, one a
`SeekableByteChannel` and the last uses an
`OutputStream`.

The constructor accepting a `File` and a size is
used exclusively for creating a split ZIP archive and is
described in the next section. For the remainder of this
section this constructor is equivalent to the one using the
`OutputStream` argument and thus it is not possible
to add uncompressed entries of unknown size.

Of the remaining three constructors the `File` version will
try to use `SeekableByteChannel` and fall back to
using a `FileOutputStream` internally if that
fails.

If `ZipArchiveOutputStream` can
use `SeekableByteChannel` it can employ some
optimizations that lead to smaller archives. It also makes
it possible to add uncompressed (`setMethod` used
with `STORED`) entries of unknown size when
calling `putArchiveEntry` - this is not allowed
if `ZipArchiveOutputStream` has to use
an `OutputStream`.

If you know you are writing to a file, you should always
prefer the `File`- or
`SeekableByteChannel`-arg constructors. The class
`org.apache.commons.compress.utils.SeekableInMemoryByteChannel`
allows you to write to an in-memory archive.

<a id="zip--multi-volume-archives"></a>

## Multi Volume Archives

The ZIP format knows so called split and spanned
archives. Spanned archives cross several removable media and
are not supported by Commons Compress.

Split archives consist of multiple files that reside in the
same directory with the same base name (the file name without
the file extension). The last file of the archive has the
extension `zip` the remaining files conventionally
use extensions `z01`, `z02` and so
on. Support for splitted archives has been added with Compress
1.20.

If you want to create a split ZIP archive you use the
constructor of `ZipArchiveOutputStream` that
accepts a `File` argument and a size. The size
determines the maximum size of a split segment - the size must
be between 64kB and 4GB. While creating the archive, this will
create several files following the naming convention described
above. The name of the `File` argument used inside
of the constructor must use the extension
`zip`.

It is currently not possible to write split archives with
more than 64k segments. When creating split archives with more
than 100 segments you will need to adjust the file names as
`ZipArchiveOutputStream` assumes extensions will be
three characters long.

If you want to read a split archive you must create a
`ZipSplitReadOnlySeekableByteChannel` from the
parts. Both `ZipFile` and
`ZipArchiveInputStream` support reading streams of
this type, in the case of `ZipArchiveInputStream`
you need to use a constructor where you can set
`skipSplitSig` to true.

<a id="zip--extra-fields"></a>

## Extra Fields

Inside a ZIP archive, additional data can be attached to
each entry. The `java.util.zip.ZipEntry` class
provides access to this via the `get/setExtra`
methods as arrays of `byte`s.

Actually the extra data is supposed to be more structured
than that and Compress' ZIP package provides access to the
structured data as `ZipExtraField` instances. Only
a subset of all defined extra field formats is supported by
the package, any other extra field will be stored
as `UnrecognizedExtraField`.

Prior to version 1.1 of this library trying to read an
archive with extra fields that didn't follow the recommended
structure for those fields would cause Compress to throw an
exception. Starting with version 1.1 these extra fields
will now be read
as `UnparseableExtraFieldData`.

Prior to version 1.19 of this library trying to read an
archive with extra fields that Compress expects to
understand but that used a different content than expected
would cause Compress to throw an exception. Starting with
version 1.19 these extra fields will now be read as
`UnrecognizedExtraField`. Using
`ZipArchiveEntry.getExtraFields(ExtraFieldParsingBehavior)`
you have a more fine grained control over the parser.

<a id="zip--encoding"></a>

## Encoding

Traditionally the ZIP archive format uses CodePage 437 as
encoding for file name, which is not sufficient for many
international character sets.

Over time different archivers have chosen different ways to
work around the limitation - the `java.util.zip`
packages simply uses UTF-8 as its encoding for example.

Ant has been offering the encoding attribute of the zip and
unzip task as a way to explicitly specify the encoding to
use (or expect) since Ant 1.4. It defaults to the
platform's default encoding for zip and UTF-8 for jar and
other jar-like tasks (war, ear, ...) as well as the unzip
family of tasks.

More recent versions of the ZIP specification introduce
something called the "language encoding flag"
which can be used to signal that a file name has been
encoded using UTF-8. All ZIP-archives written by Compress
will set this flag, if the encoding has been set to UTF-8.
Our interoperability tests with existing archivers didn't
show any ill effects (in fact, most archivers ignore the
flag to date), but you can turn off the "language encoding
flag" by setting the attribute
`useLanguageEncodingFlag` to `false` on the
`ZipArchiveOutputStream` if you should encounter
problems.

The `ZipFile`
and `ZipArchiveInputStream` classes will
recognize the language encoding flag and ignore the encoding
set in the constructor if it has been found.

The InfoZIP developers have introduced new ZIP extra fields
that can be used to add an additional UTF-8 encoded file
name to the entry's metadata. Most archivers ignore these
extra fields. `ZipArchiveOutputStream` supports
an option `createUnicodeExtraFields` which makes
it write these extra fields either for all entries
("always") or only those whose name cannot be encoded using
the specified encoding (not-encodable), it defaults to
"never" since the extra fields create bigger archives.

The fallbackToUTF8 attribute
of `ZipArchiveOutputStream` can be used to create
archives that use the specified encoding in the majority of
cases but UTF-8 and the language encoding flag for filenames
that cannot be encoded using the specified encoding.

The `ZipFile`
and `ZipArchiveInputStream` classes recognize the
Unicode extra fields by default and read the file name
information from them, unless you set the constructor parameter
`scanForUnicodeExtraFields` to false.

<a id="zip--recommendations-for-interoperability"></a>

#### Recommendations for Interoperability

The optimal setting of flags depends on the archivers you
expect as consumers/producers of the ZIP archives. Below
are some test results which may be superseded with later
versions of each tool.

- The java.util.zip package used by the jar executable or
  to read jars from your CLASSPATH reads and writes UTF-8
  names, it doesn't set or recognize any flags or Unicode
  extra fields.
- Starting with Java7 `java.util.zip` writes
  UTF-8 by default and uses the language encoding flag. It
  is possible to specify a different encoding when
  reading/writing ZIPs via new constructors. The package
  now recognizes the language encoding flag when reading and
  ignores the Unicode extra fields.
- 7Zip writes CodePage 437 by default but uses UTF-8 and
  the language encoding flag when writing entries that
  cannot be encoded as CodePage 437 (similar to the zip task
  with fallbacktoUTF8 set to true). It recognizes the
  language encoding flag when reading and ignores the
  Unicode extra fields.
- WinZIP writes CodePage 437 and uses Unicode extra fields
  by default. It recognizes the Unicode extra field and the
  language encoding flag when reading.
- Windows' "compressed folder" feature doesn't recognize
  any flag or extra field and creates archives using the
  platforms default encoding - and expects archives to be in
  that encoding when reading them.
- InfoZIP based tools can recognize and write both, it is
  a compile time option and depends on the platform so your
  mileage may vary.
- PKWARE zip tools recognize both and prefer the language
  encoding flag. They create archives using CodePage 437 if
  possible and UTF-8 plus the language encoding flag for
  file names that cannot be encoded as CodePage 437.

So, what to do?

If you are creating jars, then java.util.zip is your main
consumer. We recommend you set the encoding to UTF-8 and
keep the language encoding flag enabled. The flag won't
help or hurt java.util.zip prior to Java7 but archivers that
support it will show the correct file names.

For maximum interop it is probably best to set the encoding
to UTF-8, enable the language encoding flag and create
Unicode extra fields when writing ZIPs. Such archives
should be extracted correctly by java.util.zip, 7Zip, WinZIP, PKWARE tools and most likely InfoZIP tools. They
will be unusable with Windows' "compressed folders" feature
and bigger than archives without the Unicode extra fields, though.

If Windows' "compressed folders" is your primary consumer, then your best option is to explicitly set the encoding to
the target platform. You may want to enable creation of
Unicode extra fields so the tools that support them will
extract the file names correctly.

<a id="zip--encryption-and-alternative-compression-algorithms"></a>

## Encryption and Alternative Compression Algorithms

In most cases entries of an archive are not encrypted and
are either not compressed at all or use the DEFLATE
algorithm, Commons Compress' ZIP archiver will handle them
just fine. As of version 1.7, Commons Compress can also
decompress entries compressed with the legacy SHRINK and
IMPLODE algorithms of PKZIP 1.x. Version 1.11 of Commons
Compress adds read-only support for BZIP2. Version 1.16 adds
read-only support for DEFLATE64 - also known as "enhanced DEFLATE".

The ZIP specification allows for various other compression
algorithms and also supports several different ways of
encrypting archive contents. Neither of those methods is
currently supported by Commons Compress and any such entry can
not be extracted by the archiving code.

`ZipFile`'s and
`ZipArchiveInputStream`'s
`canReadEntryData` methods will return false for
encrypted entries or entries using an unsupported encryption
mechanism. Using this method it is possible to at least
detect and skip the entries that can not be extracted.

| Version of Apache Commons Compress | Supported Compression Methods | Supported Encryption Methods |
| --- | --- | --- |
| 1.0 to 1.6 | STORED, DEFLATE | - |
| 1.7 to 1.10 | STORED, DEFLATE, SHRINK, IMPLODE | - |
| 1.11 to 1.15 | STORED, DEFLATE, SHRINK, IMPLODE, BZIP2 | - |
| 1.16 and later | STORED, DEFLATE, SHRINK, IMPLODE, BZIP2, DEFLATE64 (enhanced deflate) | - |

<a id="zip--zip64-support"></a>

## Zip64 Support

The traditional ZIP format is limited to archive sizes of
four gibibyte (actually 232 - 1 bytes ≈
4.3 GB) and 65635 entries, where each individual entry is
limited to four gibibyte as well. These limits seemed
excessive in the 1980s.

Version 4.5 of the ZIP specification introduced the so
called "Zip64 extensions" to push those limitations for
compressed or uncompressed sizes of up to 16 exbibyte
(actually 264 - 1 bytes ≈ 18.5 EB, i.e
18.5 x 1018 bytes) in archives that themselves
can take up to 16 exbibyte containing more than
18 x 1018 entries.

Apache Commons Compress 1.2 and earlier do not support
Zip64 extensions at all.

Starting with Apache Commons Compress
1.3 `ZipArchiveInputStream`
and `ZipFile` transparently support Zip64
extensions. By default `ZipArchiveOutputStream`
supports them transparently as well (i.e. it adds Zip64
extensions if needed and doesn't use them for
entries/archives that don't need them) if the compressed and
uncompressed sizes of the entry are known
when `putArchiveEntry` is called
or `ZipArchiveOutputStream`
uses `SeekableByteChannel`
(see [above](#zip--ziparchiveoutputstream)). If only
the uncompressed size is
known `ZipArchiveOutputStream` will assume the
compressed size will not be bigger than the uncompressed
size.

`ZipArchiveOutputStream`'s
`setUseZip64` can be used to control the behavior.
`Zip64Mode.AsNeeded` is the default behavior
described in the previous paragraph.

If `ZipArchiveOutputStream` is writing to a
non-seekable stream it has to decide whether to use Zip64
extensions or not before it starts writing the entry data.
This means that if the size of the entry is unknown
when `putArchiveEntry` is called it doesn't have
anything to base the decision on. By default it will not
use Zip64 extensions in order to create archives that can be
extracted by older archivers (it will later throw an
exception in `closeEntry` if it detects Zip64
extensions had been needed). It is possible to
instruct `ZipArchiveOutputStream` to always
create Zip64 extensions by using
the `setUseZip64` with an argument
of `Zip64Mode.Always`; use this if you are
writing entries of unknown size to a stream and expect some
of them to be too big to fit into the traditional
limits.

`Zip64Mode.Always` creates archives that use
Zip64 extensions for all entries, even those that don't
require them. Such archives will be slightly bigger than
archives created with one of the other modes and not be
readable by unarchivers that don't support Zip64
extensions.

`Zip64Mode.Never` will not use any Zip64
extensions at all and may lead to
a `Zip64RequiredException` to be thrown
if `ZipArchiveOutputStream` detects that one of
the format's limits is exceeded. Archives created in this
mode will be readable by all unarchivers; they may be
slightly smaller than archives created
with `SeekableByteChannel`
in `Zip64Mode.AsNeeded` mode if some of the
entries had unknown sizes.

The `java.util.zip` package and the
`jar` command of Java5 and earlier can not read
Zip64 extensions and will fail if the archive contains any.
So if you intend to create archives that Java5 can consume
you must set the mode to `Zip64Mode.Never`

<a id="zip--known-limitations"></a>

#### Known Limitations

Some of the theoretical limits of the format are not
reached because Apache Commons Compress' own API
(`ArchiveEntry`'s size information uses
a `long`) or its usage of Java collections
or `SeekableByteChannel` internally. The table
below shows the theoretical limits supported by Apache
Commons Compress. In practice it is very likely that you'd
run out of memory or your file system won't allow files that
big long before you reach either limit.

|  | Max. Size of Archive | Max. Compressed/Uncompressed Size of Entry | Max. Number of Entries |
| --- | --- | --- | --- |
| ZIP Format Without Zip 64 Extensions | 232 - 1 bytes ≈ 4.3 GB | 232 - 1 bytes ≈ 4.3 GB | 65535 |
| ZIP Format using Zip 64 Extensions | 264 - 1 bytes ≈ 18.5 EB | 264 - 1 bytes ≈ 18.5 EB | 264 - 1 ≈ 18.5 x 1018 |
| Commons Compress 1.2 and earlier | unlimited in `ZipArchiveInputStream` and `ZipArchiveOutputStream` and 232 - 1 bytes ≈ 4.3 GB in `ZipFile`. | 232 - 1 bytes ≈ 4.3 GB | unlimited in `ZipArchiveInputStream`, 65535 in `ZipArchiveOutputStream` and `ZipFile`. |
| Commons Compress 1.3 and later | unlimited in `ZipArchiveInputStream` and `ZipArchiveOutputStream` and 263 - 1 bytes ≈ 9.2 EB in `ZipFile`. | 263 - 1 bytes ≈ 9.2 EB | unlimited in `ZipArchiveInputStream`, 231 - 1 ≈ 2.1 billion in `ZipArchiveOutputStream` and `ZipFile`. |

<a id="zip--known-interoperability-problems"></a>

#### Known Interoperability Problems

The `java.util.zip` package of OpenJDK7 supports
Zip 64 extensions but its `ZipInputStream` and
`ZipFile` classes will be unable to extract
archives created with Commons Compress 1.3's
`ZipArchiveOutputStream` if the archive contains
entries that use the data descriptor, are smaller than 4 GiB
and have Zip 64 extensions enabled. I.e. the classes in
OpenJDK currently only support archives that use Zip 64
extensions only when they are actually needed. These classes
are used to load JAR files and are the base for the
`jar` command line utility as well.

<a id="zip--consuming-archives-completely"></a>

## Consuming Archives Completely

Prior to version 1.5 `ZipArchiveInputStream`
would return null from `getNextEntry` or
`getNextZipEntry` as soon as the first central
directory header of the archive was found, leaving the whole
central directory itself unread inside the stream. Starting
with version 1.5 `ZipArchiveInputStream` will try
to read the archive up to and including the "end of central
directory" record effectively consuming the archive
completely.

<a id="zip--symbolic-links"></a>

## Symbolic Links

Starting with Compress 1.5 `ZipArchiveEntry`
recognizes Unix Symbolic Link entries written by InfoZIP's
zip.

The `ZipFile` class contains a convenience
method to read the link name of an entry. Basically all it
does is read the contents of the entry and convert it to
a string using the given file name encoding of the
archive.

<a id="zip--parallel-zip-creation"></a>

## Parallel zip creation

Starting with Compress 1.10 there is now built-in support for
parallel creation of zip archives

Multiple threads can write
to their own `ScatterZipOutputStream`
instance that is backed to file or to some user-implemented form of
storage (implementing `ScatterGatherBackingStore`).

When the threads finish, they can join these streams together
to a complete zip file using the `writeTo` method
that will write a single `ScatterOutputStream` to a target
`ZipArchiveOutputStream`.

To assist this process, clients can use
`ParallelScatterZipCreator` that will handle threads
pools and correct memory model consistency so the client
can avoid these issues.

Until version 1.18, there was no guarantee of order of the entries when writing a Zip
file with `ParallelScatterZipCreator`. In consequence, when writing well-formed
Zip files this way, it was usually necessary to keep a
separate `ScatterZipOutputStream` that received all directories
and wrote this to the target `ZipArchiveOutputStream` before
the ones created through `ParallelScatterZipCreator`. This was the responsibility of the client.

Starting with version 1.19, entries order is kept, then this specific handling of directories is not
necessary any more.

See the examples section for a code sample demonstrating how to make a zip file.

<a id="zip--zstandard-support"></a>

## Zstandard Support

Starting with Compress 1.28.0, `org.apache.commons.compress.archivers.zip` supports reading and writing using the Zstandard method.
Zstandard method `93` and the deprecated `20` are supported.

---
