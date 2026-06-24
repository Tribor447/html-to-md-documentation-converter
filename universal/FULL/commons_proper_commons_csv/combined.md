# Project Information

## Navigation

- Commons CSV
  - [About](#index)
  - [Release History](#changes)
  - [Sources](#scm)
  - [Security](#security)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes)
    - [JIRA Report](#jira-changes)
    - [Surefire](#surefire)
    - [Rat Report](#rat-report)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [CPD](#cpd)
    - [PMD](#pmd)
    - [Tag List](#taglist)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/index.html -->

<!-- page_index: 1 -->

<a id="index--using-apache-commons-csv"></a>

# Using Apache Commons CSV

Commons CSV reads and writes files in variations of the Comma Separated Value (CSV) format.

Read the documentation starting with the [Javadoc Overview](https://commons.apache.org/proper/commons-csv/apidocs/index.html).

<a id="index--documentation"></a>

# Documentation

An overview of the functionality is provided in the
[user guide](https://commons.apache.org/proper/commons-csv/apidocs/index.html).
Various [project reports](#project-reports) are also available.

The Javadoc API documents are available online:

- [Javadoc current](https://commons.apache.org/proper/commons-csv/apidocs/index.html)
- [Javadoc archives](https://javadoc.io/doc/org.apache.commons/commons-csv/)

The [git repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-csv.git).

<a id="index--releases"></a>

# Releases

- [Download Apache Commons CSV current (mirrors)](https://commons.apache.org/csv/download_csv.cgi), requires Java 8 or above
- [Download Apache Commons CSV archived releases](https://archive.apache.org/dist/commons/csv/)

See the
[Download Page](https://commons.apache.org/csv/download_csv.cgi)
for the latest releases.

[Release History](#changes) are also available.

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/csv/)

For dependency access methods, see [Dependency Information](https://commons.apache.org/proper/commons-csv/dependency-info.html)

<a id="index--building-from-sources"></a>

# Building from sources

The latest code can be checked out from our git repository at <https://gitbox.apache.org/repos/asf/commons-csv.git>.
You can build the component using Apache Maven using `mvn clean package`.

<a id="index--getting-involved"></a>

# Getting Involved

The [commons developer mailing list](https://commons.apache.org/proper/commons-csv/mail-lists.html) is the main channel of communication for contributors. Please remember that the lists are shared between all commons components, so prefix your email by [csv].

You can also peruse [JIRA](https://commons.apache.org/proper/commons-csv/issue-tracking.html). Specific links of interest for JIRA are:

- Ideas looking for code: [Patch Needed](https://issues.apache.org/jira/issues/?jql=project%20%3D%20CSV%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20%22Patch%20Needed%22)
- Issues with patches, looking for reviews: [Review Patch](https://issues.apache.org/jira/issues/?jql=project%20%3D%20CSV%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20Review)

Alternatively you can go through the *Needs Work* tags in the [TagList report](#taglist).

If you'd like to offer up pull requests via GitHub rather than applying patches to JIRA, we have a [GitHub mirror](https://github.com/apache/commons-csv/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-csv/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [csv].

Bug reports and enhancements are also welcomed via the [JIRA](https://commons.apache.org/proper/commons-csv/issue-tracking.html) issue tracker.
Please read the instructions carefully.

<a id="index--about-commons-csv"></a>

# About Commons CSV

Commons CSV was started to unify a common and simple interface for reading and writing CSV files under an ASL license. It has been bootstrapped by a code donation from Netcetera in Switzerland. There are three pre-existing BSD compatible CSV parsers which this component will hopefully make redundant (authors willing):

- [Skife CSV](http://kasparov.skife.org/csv/)
- [Open CSV](https://opencsv.sourceforge.net/)
- Genjava CSV

In addition to the code from Netcetera (org.apache.commons.csv), Martin van den Bemt has added an additional writer API.

Other CSV implementations:

- [Super CSV](https://super-csv.github.io/super-csv/index.html)

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/changes.html -->

<!-- page_index: 2 -->

<a id="changes--apache-commons-csv-release-notes"></a>

# Apache Commons CSV Release Notes

<a id="changes--release-history"></a>

## Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.14.2](#changes--a1.14.2) | YYYY-MM-DD | This is a feature and maintenance release. Java 8 or later is required. |
| [1.14.1](#changes--a1.14.1) | 2025-07-27 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.14.0](#changes--a1.14.0) | 2025-03-15 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.13.0](#changes--a1.13.0) | 2025-01-08 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.12.0](#changes--a1.12.0) | 2024-09-21 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.11.0](#changes--a1.11.0) | 2024-04-28 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.10.0](#changes--a1.10.0) | 2023-01-28 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.9.0](#changes--a1.9.0) | 2021-07-24 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.8](#changes--a1.8) | 2020-02-01 | This is a feature and maintenance release. Java 8 or later is required. This release fixes serialization compatibility of CSVRecord with versions 1.0 to 1.6. New fields added since 1.7 are not serialized. Support for Serializable is scheduled to be removed in version 2.0. |
| [1.7](#changes--a1.7) | 2019-06-01 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.6](#changes--a1.6) | 2018-09-22 | Feature and bug fix release (Java 7 or above) |
| [1.5](#changes--a1.5) | 2017-09-03 | Feature and bug fix release (Java 7 or above) |
| [1.4](#changes--a1.4) | 2016-05-28 | Feature and bug fix release (Java 6 or above) |
| [1.3](#changes--a1.3) | 2016-05-09 | Feature and bug fix release (Java 6 or above) |
| [1.2](#changes--a1.2) | 2015-08-24 | Feature and bug fix release (Java 6 or above) |
| [1.1](#changes--a1.1) | 2014-11-16 | Feature and bug fix release (Java 6 or above) |
| [1.0](#changes--a1.0) | 2014-08-14 | First release (Java 6 or above) |

<a id="changes--release-1.14.2-yyyy-mm-dd"></a>

## Release 1.14.2 – YYYY-MM-DD

| Type | Changes | By |
| --- | --- | --- |
| Fix | Remove Spotbugs dependency and use exclude-filter instead #564. Fixes [CSV-320](https://issues.apache.org/jira/browse/CSV-320). Thanks to Jan Burkhardt. | [aherbert](#team--aherbert) |
| Fix | Remove broken website link #577. Fixes [CSV-320](https://issues.apache.org/jira/browse/CSV-320). Thanks to Cassio Santos. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 85 to 88 #573. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | [test] Bump com.opencsv:opencsv from 5.11.2 to 5.12.0 #558. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-lang3 from 3.18.0 to 3.19.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.14.1-2025-07-27"></a>

## Release 1.14.1 – 2025-07-27

| Type | Changes | By |
| --- | --- | --- |
| Fix | CSVPrinter.printRecord(Stream) hangs if given a parallel stream. Fixes [CSV-318](https://issues.apache.org/jira/browse/CSV-318). Thanks to Joseph Shraibman, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVPrinter now uses an internal lock instead of synchronized methods. Fixes [CSV-318](https://issues.apache.org/jira/browse/CSV-318). Thanks to Joseph Shraibman, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | org.apache.commons.csv.CSVPrinter.printRecords(ResultSet) now writes one record at a time using a lock. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 81 to 85 #542. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.18.0 to 2.20.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.opencsv:opencsv from 5.10 to 5.11.2 #545, #551, #553. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-lang3 from 3.17.0 to 3.18.0 #556. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.18.0 to 1.19.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.14.0-2025-03-15"></a>

## Release 1.14.0 – 2025-03-15

| Type | Changes | By |
| --- | --- | --- |
| Fix | Release history link changed from changes-report.html to changes.html #516. Fixes [CSV-317](https://issues.apache.org/jira/browse/CSV-317). Thanks to Filipe Roque. | [ggregory](#team--ggregory) |
| Fix | Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.parse(URL, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.parse(String, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.parse(File, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.parse(Path, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.parse(InputStream, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.parse(\*) methods with a null Charset maps to Charset.defaultCharset(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix possible NullPointerException in Token.toString(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Define and use Maven property commons.jmh.version. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CSVFormat.Builder.setMaxRows(long). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CSVFormat.getMaxRows(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVPrinter.printRecords(ResultSet) knows how to use CSVFormat's maxRows. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVPrinter.printRecords(Iterable) knows how to use CSVFormat's maxRows. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVPrinter.printRecords(Stream) knows how to use CSVFormat's maxRows. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVParser.stream() knows how to use CSVFormat's maxRows. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVParser.getRecords() knows how to use CSVFormat's maxRows. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVParser.iterator() knows how to use CSVFormat's maxRows. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.opencsv:opencsv from 5.9 to 5.10. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.17.2 to 1.18.0 #522. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 79 to 81. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.13.0-2025-01-08"></a>

## Release 1.13.0 – 2025-01-08

| Type | Changes | By |
| --- | --- | --- |
| Fix | Required OSGi Import-Package version numbers in MANIFEST.MF #504. Fixes [CSV-314](https://issues.apache.org/jira/browse/CSV-314). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.nextRecord() should throw CSVException (an IOException subclass) instead of IOException and IllegalStateException, no method signature changes needed. Fixes [CSV-314](https://issues.apache.org/jira/browse/CSV-314). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CSVPrinter.getRecordCount(). Fixes [CSV-313](https://issues.apache.org/jira/browse/CSV-313). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add and use CSVParser.Builder and builder() and deprecate CSVParser constructors. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVFormat.Builder implements Supplier<CSVFormat>. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Deprecate CSVFormat.Builder.build() for get(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Track byte position #502. Fixes [CSV-196](https://issues.apache.org/jira/browse/CSV-196). Thanks to Yuzhan Jiang, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 76 to 78 #486, #495. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.codehaus.mojo:taglist-maven-plugin from 3.1.0 to 3.2.1 #493. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.17.0 to 2.18.0 #505. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.17.1 to 1.17.2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 78 to 79. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.12.0-2024-09-21"></a>

## Release 1.12.0 – 2024-09-21

| Type | Changes | By |
| --- | --- | --- |
| Add | Add CSVException that extends IOException thrown on invalid input instead of IOException. Fixes [CSV-270](https://issues.apache.org/jira/browse/CSV-270). Thanks to Thomas Kamps, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix PMD issues for port to PMD 7.1.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix some Javadoc links #442. Thanks to Dávid Szigecsán, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Extract duplicated code into a method #444. Thanks to Dávid Szigecsán. | [ggregory](#team--ggregory) |
| Fix | Migrate CSVFormat#print(File, Charset) to NIO #445. Thanks to Dávid Szigecsán. | [ggregory](#team--ggregory) |
| Fix | Fix documentation for CSVFormat private constructor #466. Thanks to Dávid Szigecsán. | [ggregory](#team--ggregory) |
| Fix | CSVFormat does not support explicit " as escape char. Fixes [CSV-294](https://issues.apache.org/jira/browse/CSV-294). Thanks to Joern Huxhorn, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Escaping is not disableable. Fixes [CSV-150](https://issues.apache.org/jira/browse/CSV-150). Thanks to dota17, Gary Gregory, Jörn Huxhorn. | [ggregory](#team--ggregory) |
| Fix | Fix Javadoc warnings on Java 23. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Improve parser performance by up to 20%, YMMV. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.16.1 to 1.17.1 #422, #449. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 69 to 76 #435, #452, #465, #468, #475, #482. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.codehaus.mojo:taglist-maven-plugin from 3.0.0 to 3.1.0 #441. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-lang3 from 3.14.0 to 3.17.0 #450, #459, #470. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.hamcrest:hamcrest from 2.2 to 3.0 #455. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.16.1 to 2.17.0 #476. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.11.0-2024-04-28"></a>

## Release 1.11.0 – 2024-04-28

| Type | Changes | By |
| --- | --- | --- |
| Add | [Javadoc] Add example to CSVFormat#setHeaderComments() #344. Fixes [CSV-308](https://issues.apache.org/jira/browse/CSV-308). Thanks to Buddhi De Silva, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add and use CSVFormat#setTrailingData(boolean) in CSVFormat.EXCEL for Excel compatibility #303. Thanks to DamjanJovanovic, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add and use CSVFormat#setLenientEof(boolean) in CSVFormat.EXCEL for Excel compatibility #303. Thanks to DamjanJovanovic, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Replace deprecated method in user guide, update external link #324, #325. Fixes [CSV-306](https://issues.apache.org/jira/browse/CSV-306). Thanks to Sam Ng, Bruno P. Kinoshita. | [ggregory](#team--ggregory) |
| Fix | Document duplicate header behavior #309. Thanks to Seth Falco, Bruno P. Kinoshita. | [ggregory](#team--ggregory) |
| Fix | Add missing docs #328. Thanks to jkbkupczyk. | [ggregory](#team--ggregory) |
| Fix | [StepSecurity] CI: Harden GitHub Actions #329, #330. Thanks to step-security-bot. | [ggregory](#team--ggregory) |
| Fix | Better error message during faulty CSV record read #347. Fixes [CSV-147](https://issues.apache.org/jira/browse/CSV-147). Thanks to Steven Peterson, Benedikt Ritter, Gary Gregory, Joerg Schaible, Buddhi De Silva, Elliotte Rusty Harold. | [ggregory](#team--ggregory) |
| Fix | Misleading error message when QuoteMode set to None #352. Fixes [CSV-310](https://issues.apache.org/jira/browse/CSV-310). Thanks to Buddhi De Silva. | [ggregory](#team--ggregory) |
| Fix | OutOfMemory for very long rows despite using column value of type Reader. Fixes [CSV-311](https://issues.apache.org/jira/browse/CSV-311). Thanks to Christian Feuersaenger, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Use try-with-resources to manage JDBC CLOB in CSVPrinter.printRecords(ResultSet). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | JDBC Blob columns are now output as Base64 instead of Object#toString(), which usually is InputStream#toString(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Support unusual Excel use cases: Add support for trailing data after the closing quote, and EOF without a final closing quote #303. Thanks to DamjanJovanovic, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | MongoDB CSV empty first column parsing fix #412. Thanks to Igor Kamyshnikov, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io: from 2.11.0 to 2.16.1 #408, #413. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 57 to 69 #410. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump h2 from 2.1.214 to 2.2.224 #333, #349, #359. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-lang3 from 3.12.0 to 3.14.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update exception message in CSVRecord#getNextRecord() #348. Thanks to Buddhi De Silva, Michael Osipov, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests using com.opencsv:opencsv from 5.8 to 5.9 #373. Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.10.0-2023-01-28"></a>

## Release 1.10.0 – 2023-01-28

| Type | Changes | By |
| --- | --- | --- |
| Fix | Minor changes #172. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | No Automatic-Module-Name prevents usage in JPMS projects without repacking the JAR. Fixes [CSV-292](https://issues.apache.org/jira/browse/CSV-292). Thanks to Rob Vesse. | [kinow](#team--kinow) |
| Fix | Fix for multi-char delimiter not working as expected #218. Fixes [CSV-288](https://issues.apache.org/jira/browse/CSV-288). Thanks to Santhsoh, Angus. | [ggregory](#team--ggregory) |
| Fix | CSVRecord.get(Enum) should use Enum.name() instead of Enum.toString(). Fixes [CSV-269](https://issues.apache.org/jira/browse/CSV-269). Thanks to Auke te Winkel, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Allow org.apache.commons.csv.IOUtils.copy(Reader, Appendable, CharBuffer) to compile on Java 11 and run on Java 8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVRecord.toList() does not give write access to the new List. Fixes [CSV-300](https://issues.apache.org/jira/browse/CSV-300). Thanks to Markus Spann, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVParser.getRecords() now throws UncheckedIOException instead of IOException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Add comments to iterator() and stream() #270. Fixes [CSV-274](https://issues.apache.org/jira/browse/CSV-274). Thanks to Peter Hull, Bruno P. Kinoshita, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix wrong assumptions in PostgreSQL formats #265. Fixes [CSV-290](https://issues.apache.org/jira/browse/CSV-290). Thanks to angusdev, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Validate input to setDelimiter(String) for empty string #266. Thanks to Mykola Faryma. | [ggregory](#team--ggregory) |
| Fix | Bump CSVFormat#serialVersionUID from 1 to 2. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Fix | CSVParser: Identify duplicates in null, empty and blank header names #279. Thanks to Alex Herbert. | [ggregory](#team--ggregory) |
| Remove | Serialization in CSVFormat is not supported from one version to the next. | [ggregory](#team--ggregory) |
| Add | Make CSVRecord#values() public. Fixes [CSV-291](https://issues.apache.org/jira/browse/CSV-291). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add DuplicateHeaderMode for flexibility with header strictness. #114. Fixes [CSV-264](https://issues.apache.org/jira/browse/CSV-264). Thanks to Sagar Tiwari, Seth Falco, Alex Herbert, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Support for parallelism in CSVPrinter. Fixes [CSV-295](https://issues.apache.org/jira/browse/CSV-295). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CSVPrinter.printRecord[s](Stream). Fixes [CSV-295](https://issues.apache.org/jira/browse/CSV-295). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add accessors for header/trailer comments #257. Fixes [CSV-304](https://issues.apache.org/jira/browse/CSV-304). Thanks to Peter Hull, Bruno P. Kinoshita, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add github/codeql-action. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from 2.1.6 to 3.0.10 #196, #233, #243, #267, #271. Thanks to Dependabot, Gary Gregory. | [kinow](#team--kinow) |
| Update | Bump actions/checkout from 2.3.4 to 3.1.0 #188, #195, #220, #272. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from 2 to 3.5.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/upload-artifact from 3.1.0 to 3.1.1 #280. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 52 to 57 #264, #288, #298, #323. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump checkstyle from 8.44 to 9.2.1 #180, #190, #194, #202, #207. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump junit-jupiter from 5.8.0-M1 to 5.9.1 #179, #186, #201, #244, #263. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump jmh-core from 1.32 to 1.36 #176, #208, #229, #285. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump jmh-generator-annprocess from 1.32 to 1.36 #175, #206, #226, #283. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump mockito-core from 3.11.2 to 4.11.0 #187, #197, #204, #212, #230, #237, #251, #259, #284, #292, #297. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-pmd-plugin from 3.14.0 to 3.19.0 #184, #219, #238, #254, #258. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump pmd from 6.36.0 to 6.52.0 #173, #189, #193, #199, #227, #233, #214, #236, #240, #247, #255, #273. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump opencsv from 5.5.1 to 5.7.1 #182, #221, #260, #281. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.3.0 to 4.7.3.0 #192, #198, #203, #211, #225, #234, #242, #245, #261, #275, #282. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump com.github.spotbugs:spotbugs from 4.5.3 to 4.7.2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump h2 from 1.4.200 to 2.1.214 #200, #205, #213, #239. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump maven-javadoc-plugin from 3.3.0 to 3.4.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump biz.aQute.bnd:biz.aQute.bndlib from 5.3.0 to 6.3.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump jacoco-maven-plugin from 0.8.7 to 0.8.8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump japicmp-maven-plugin from 0.15.3 to 0.16.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.1.2 to 3.2.0 #253. Thanks to Dependabot. | [kinow](#team--kinow) |

<a id="changes--release-1.9.0-2021-07-24"></a>

## Release 1.9.0 – 2021-07-24

| Type | Changes | By |
| --- | --- | --- |
| Fix | Replace FindBugs with SpotBugs #56. Thanks to Amey Jadiye. | [ggregory](#team--ggregory) |
| Fix | Javadoc typo in CSVFormat let's -> lets #57. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | CSVFormat.printWithEscapes throws StringIndexOutOfBoundsException when value is Reader #61. Fixes [CSV-259](https://issues.apache.org/jira/browse/CSV-259). Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | Improve CSVFormat test coverage #63. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | Fix CSVFileParserTest.java to allow for a null return value from record.getComment() #62. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | Improve test coverage in CSVFormatTest #65. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | Removed invalid Javadoc markup for CSVFormat EXCEL #64. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | Improve CSVRecord and CSVPrinter code coverage #66. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | Improve lexer and token coverage #67. Thanks to Chen. | [ggregory](#team--ggregory) |
| Fix | CSVFormat.format trims last delimiter if the delimiter is a white space #71. Fixes [CSV-211](https://issues.apache.org/jira/browse/CSV-211). Thanks to Alpesh Kulkarni, Chen. | [ggregory](#team--ggregory) |
| Fix | Replace org.apache.commons.csv.Assertions.notNull() with Objects.requireNonNull(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Line number is not proper at EOF. Fixes [CSV-149](https://issues.apache.org/jira/browse/CSV-149). Thanks to Kranthi, Gary Gregory, Brent Worden, dota17. | [ggregory](#team--ggregory) |
| Fix | Parser iterates over the last CSV Record twice. Fixes [CSV-195](https://issues.apache.org/jira/browse/CSV-195). Thanks to Rodolfo Duldulao, Rodolfo Duldulao, Michael Vitz, dota17. | [ggregory](#team--ggregory) |
| Fix | Minor improvements #126, #127, #130. Fixes [CSV-267](https://issues.apache.org/jira/browse/CSV-267). Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Add possibility to use ResultSet header meta data as CSV header #11. Fixes [CSV-123](https://issues.apache.org/jira/browse/CSV-123). Thanks to Emmanuel Bourg, Benedikt Ritter, shivakrishnaah, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Add test cases for withIgnoreSurroundingSpaces() and withTrim() #70. Fixes [CSV-148](https://issues.apache.org/jira/browse/CSV-148). Thanks to dota17. | [ggregory](#team--ggregory) |
| Fix | Update CSVParser.parse(File, Charset, CSVFormat) from IO to NIO. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Missing separator with print(object) followed by printRecord(Object[]) #157. Fixes [CSV-271](https://issues.apache.org/jira/browse/CSV-271). Thanks to Amar Prakash Pandey. | [ggregory](#team--ggregory) |
| Fix | Fix EOL checking for read array in ExtendedBufferedReader #5. Fixes [CSV-158](https://issues.apache.org/jira/browse/CSV-158). Thanks to Alexander Bondarev, Benedikt Ritter, Gary Gregory, Chen. | [ggregory](#team--ggregory) |
| Fix | Print from Reader with embedded quotes generates incorrect output #78. Fixes [CSV-263](https://issues.apache.org/jira/browse/CSV-263). Thanks to Jason A. Guild, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Replace JUnit assert by simpler but equivalent calls. #159. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Update gitignore to ignore idea and vscode #160. Thanks to Seth Falco. | [ggregory](#team--ggregory) |
| Fix | Update CSVBenchmark #165. Fixes [CSV-281](https://issues.apache.org/jira/browse/CSV-281). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | Remove Whitespace Check Determines Delimiter Twice #167. Fixes [CSV-283](https://issues.apache.org/jira/browse/CSV-283). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | Document and Automate CSV Benchmark Harness #166. Fixes [CSV-283](https://issues.apache.org/jira/browse/CSV-283). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | Optimize Lexer Delimiter Check for One Character Delimiter #163. Fixes [CSV-279](https://issues.apache.org/jira/browse/CSV-279). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | SpotBugs Error: Medium: org.apache.commons.csv.CSVParser.getHeaderNames() may expose internal representation by returning CSVParser.headerNames [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 599] EI\_EXPOSE\_REP. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | SpotBugs Error: Medium: new org.apache.commons.csv.CSVParser(Reader, CSVFormat, long, long) may expose internal representation by storing an externally mutable object into CSVParser.format [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 433] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | SpotBugs Error: Medium: new org.apache.commons.csv.CSVParser(Reader, CSVFormat, long, long) may expose internal representation by storing an externally mutable object into CSVParser.headerMap [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 437] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | SpotBugs Error: Medium: new org.apache.commons.csv.CSVParser(Reader, CSVFormat, long, long) may expose internal representation by storing an externally mutable object into CSVParser.headerNames [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 438] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | SpotBugs Error: Medium: new org.apache.commons.csv.CSVPrinter(Appendable, CSVFormat) may expose internal representation by storing an externally mutable object into CSVPrinter.format [org.apache.commons.csv.CSVPrinter] At CSVPrinter.java:[line 100] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Formalize PerformanceTest #168. Fixes [CSV-284](https://issues.apache.org/jira/browse/CSV-284). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | Reuse Buffers in Lexer for Delimiter Detection #162. Fixes [CSV-278](https://issues.apache.org/jira/browse/CSV-278). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | Cleanup and Document Performance Test Harness #170. Fixes [CSV-286](https://issues.apache.org/jira/browse/CSV-286). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Fix | Update buffer position when reading line comment #120. Fixes [CSV-265](https://issues.apache.org/jira/browse/CSV-265). Thanks to belugabehr. | [ggregory](#team--ggregory) |
| Add | Make CSVRecord#toList() public. Fixes [CSV-275](https://issues.apache.org/jira/browse/CSV-275). Thanks to Michael Wyraz, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CSVRecord#stream(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CSVParser#stream(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Make the method CSVRecord.putIn(Map) public. Fixes [CSV-184](https://issues.apache.org/jira/browse/CSV-184). Thanks to Gaurav Agarwal, M. Steiger, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add test cases for CSVRecord with get(Enum) and toString. #54. Thanks to dota17. | [ggregory](#team--ggregory) |
| Add | Add and use CSVFormat.Builder, deprecated CSVFormat#with methods, based on #73. Thanks to Gary Gregory, dota17. | [ggregory](#team--ggregory) |
| Add | Add support for String delimiters #76. Fixes [CSV-206](https://issues.apache.org/jira/browse/CSV-206). Thanks to Gary Gregory, dota17. | [ggregory](#team--ggregory) |
| Update | Update org.junit.jupiter:junit-jupiter from 5.6.0 to 5.7.0, #84 #109 Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update tests from Apache Commons Lang 3.9 to 3.12.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update tests from commons-io:commons-io 2.6 to 2.11.0, #108. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/checkout from v1 to v2.3.4, #79, #92, #121. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 50 to 51 #80. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump tests from opencsv from 3.1 to 5.5.1 #81, #137, #158. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update tests from super-csv from 2.2.1 to 2.4.0 #86. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump build actions/setup-java from v1.4.0 to v2, #101, #113. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-pmd-plugin from 3.13.0 to 3.14.0 #122. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump tests from org.mockito:mockito-core 3.2.4 -> 3.11.2; #88, #107, #110, #123, #128, #129, #156. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from v2 to v2.1.6 #132, #153. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.0.0 to 3.1.2 #131. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump checkstyle from 8.29 to 8.44. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump junit-jupiter from 5.7.0 to 5.8.0-M1 #133, #149. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons.jacoco.version from 0.8.5 to 0.8.7 (Java 16). Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons.spotbugs.version from 4.0.4 to 4.3.0 (Java 16). Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-javadoc-plugin from 3.2.0 to 3.3.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump jmh-generator-annprocess from 1.5.2 to 1.32 #151. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump PMD core from 6.29.0 to 6.36.0. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump biz.aQute.bnd:biz.aQute.bndlib from 5.1.2 to 5.3.0. Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.8-2020-02-01"></a>

## Release 1.8 – 2020-02-01

| Type | Changes | By |
| --- | --- | --- |
| Add | Add CSVRecord.isSet(int) method #52. Fixes [CSV-255](https://issues.apache.org/jira/browse/CSV-255). Thanks to 0x100. | [ggregory](#team--ggregory) |
| Fix | Char escape doesn't work properly with quoting. Fixes [CSV-135](https://issues.apache.org/jira/browse/CSV-135). Thanks to Mateusz Zakarczemny. | [sebb](#team--sebb) |
| Fix | Test case failures following CSVFormat#equals() update. Fixes [CSV-244](https://issues.apache.org/jira/browse/CSV-244). | [sebb](#team--sebb) |
| Fix | CSVFormat withTrim() and withIgnoreSurroundingSpaces() need better docs. Fixes [CSV-243](https://issues.apache.org/jira/browse/CSV-243). | [sebb](#team--sebb) |
| Fix | CSVFormat equals() and hashCode() don't use all fields. Fixes [CSV-242](https://issues.apache.org/jira/browse/CSV-242). | [sebb](#team--sebb) |
| Fix | CSVFormat#validate() does not account for allowDuplicateHeaderNames #43. Fixes [CSV-241](https://issues.apache.org/jira/browse/CSV-241). Thanks to LuckyIlam, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Post 1.7 release fixes. Fixes [CSV-245](https://issues.apache.org/jira/browse/CSV-245). Thanks to Alex Herbert. | [ggregory](#team--ggregory) |
| Fix | Upgrade test framework to JUnit 5 Jupiter #49, #50. Fixes [CSV-252](https://issues.apache.org/jira/browse/CSV-252). Thanks to Alex Herbert. | [ggregory](#team--ggregory) |
| Fix | A single empty header is allowed when not allowing empty column headers. #47. Fixes [CSV-247](https://issues.apache.org/jira/browse/CSV-247). Thanks to Alex Herbert, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVRecord is not Serializable. Fixes [CSV-248](https://issues.apache.org/jira/browse/CSV-248). Thanks to Alex Herbert. | [ggregory](#team--ggregory) |
| Fix | Use test scope for supercsv #48. Thanks to Alex Herbert. | [ggregory](#team--ggregory) |
| Update | Update tests from H2 1.4.199 to 1.4.200. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update tests from Hamcrest 2.1 to 2.2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update tests from Mockito 3.1.0 to 3.2.4. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Fix typos in site and test #53. Thanks to Chen. | [ggregory](#team--ggregory) |
| Update | Fix typo performance test #55. Thanks to Chen. | [ggregory](#team--ggregory) |

<a id="changes--release-1.7-2019-06-01"></a>

## Release 1.7 – 2019-06-01

| Type | Changes | By |
| --- | --- | --- |
| Add | Add predefined CSVFormats for printing MongoDB CSV and TSV. Fixes [CSV-233](https://issues.apache.org/jira/browse/CSV-233). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix escape character for POSTGRESQL\_TEXT and POSTGRESQL\_CSV formats. Fixes [CSV-208](https://issues.apache.org/jira/browse/CSV-208). Thanks to Jurrie Overgoor. | [ggregory](#team--ggregory) |
| Fix | Site link "Source Repository" does not work. Fixes [CSV-232](https://issues.apache.org/jira/browse/CSV-232). Thanks to Jurrie Overgoor, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add support for java.sql.Clob. Fixes [CSV-234](https://issues.apache.org/jira/browse/CSV-234). Thanks to Roberto Benedetti, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update to Java 8. Fixes [CSV-237](https://issues.apache.org/jira/browse/CSV-237). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Escape quotes in CLOBs #39. Fixes [CSV-238](https://issues.apache.org/jira/browse/CSV-238). Thanks to Stephen Olander-Waters. | [ggregory](#team--ggregory) |
| Add | Cannot get headers in column order from CSVRecord. Fixes [CSV-239](https://issues.apache.org/jira/browse/CSV-239). Thanks to Gary Gregory, Dave Moten. | [ggregory](#team--ggregory) |
| Update | Update tests from H2 1.4.198 to 1.4.199. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.6-2018-09-22"></a>

## Release 1.6 – 2018-09-22

| Type | Changes | By |
| --- | --- | --- |
| Update | Add more documentation to CSVPrinter. Fixes [CSV-231](https://issues.apache.org/jira/browse/CSV-231). | [britter](#team--britter) |
| Add | Add autoFlush option for CsvPrinter. PR #24. Fixes [CSV-217](https://issues.apache.org/jira/browse/CSV-217). Thanks to Korolyov Alexei. | [ggregory](#team--ggregory) |
| Fix | The behavior of quote char using is not similar as Excel does when the first string contains CJK char(s). Fixes [CSV-219](https://issues.apache.org/jira/browse/CSV-219). Thanks to Zhang Hongda. | [ggregory](#team--ggregory) |
| Fix | Don't quote cells just because they have UTF-8 encoded characters. Fixes [CSV-172](https://issues.apache.org/jira/browse/CSV-172). Thanks to Andrew Pennebaker. | [ggregory](#team--ggregory) |
| Add | Add API org.apache.commons.csv.CSVFormat.withSystemRecordSeparator(). Fixes [CSV-220](https://issues.apache.org/jira/browse/CSV-220). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Inconsistency between Javadoc of CSVFormat DEFAULT EXCEL. Fixes [CSV-223](https://issues.apache.org/jira/browse/CSV-223). Thanks to Samuel Martin. | [ggregory](#team--ggregory) |
| Fix | Create CSVFormat.ORACLE preset. Fixes [CSV-209](https://issues.apache.org/jira/browse/CSV-209). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Some multi-iterator parsing peek sequences incorrectly consume elements. Fixes [CSV-224](https://issues.apache.org/jira/browse/CSV-224). Thanks to David Warshaw. | [ggregory](#team--ggregory) |
| Fix | Parse method should avoid creating a redundant BufferedReader. Fixes [CSV-225](https://issues.apache.org/jira/browse/CSV-225). Thanks to Anson Schwabecher. | [ggregory](#team--ggregory) |
| Fix | Add predefined CSVFormats for printing MongoDB CSV and TSV. Fixes [CSV-233](https://issues.apache.org/jira/browse/CSV-233). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.5-2017-09-03"></a>

## Release 1.5 – 2017-09-03

| Type | Changes | By |
| --- | --- | --- |
| Fix | withNullString value is printed without quotes when QuoteMode.ALL is specified; add QuoteMode.ALL\_NON\_NULL. PR #17. Fixes [CSV-203](https://issues.apache.org/jira/browse/CSV-203). Thanks to Richard Wheeldon, Kai Paroth. | [ggregory](#team--ggregory) |
| Fix | Fix outdated comments about FileReader in CSVParser #13. Fixes [CSV-194](https://issues.apache.org/jira/browse/CSV-194). Thanks to Marc Prud'hommeaux. | [ggregory](#team--ggregory) |
| Fix | Fix incorrect method name 'withFirstRowAsHeader' in user guide. Fixes [CSV-193](https://issues.apache.org/jira/browse/CSV-193). Thanks to Matthias Wiehl. | [ggregory](#team--ggregory) |
| Fix | Negative numeric values in the first column are always quoted in minimal mode. Fixes [CSV-171](https://issues.apache.org/jira/browse/CSV-171). Thanks to Gary Gregory, Michael Graessle, Adrian Bridgett. | [ggregory](#team--ggregory) |
| Update | Update platform requirement from Java 6 to 7. Fixes [CSV-187](https://issues.apache.org/jira/browse/CSV-187). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Do not use RuntimeException in CSVParser.iterator().new Iterator() {...}.getNextRecord(). Fixes [CSV-201](https://issues.apache.org/jira/browse/CSV-201). Thanks to Benedikt Ritter, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CSVParser: Add factory method accepting InputStream. Fixes [CSV-189](https://issues.apache.org/jira/browse/CSV-189). Thanks to Peter Holzwarth, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add convenience API CSVFormat.print(File, Charset). Fixes [CSV-190](https://issues.apache.org/jira/browse/CSV-190). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add convenience API CSVFormat.print(Path, Charset). Fixes [CSV-191](https://issues.apache.org/jira/browse/CSV-191). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add convenience API CSVParser.parse(Path, Charset, CSVFormat). Fixes [CSV-192](https://issues.apache.org/jira/browse/CSV-192). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add convenience API CSVFormat#printer() to print to System.out. Fixes [CSV-205](https://issues.apache.org/jira/browse/CSV-205). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Provide a CSV Format for printing PostgreSQL CSV and Text formats. Fixes [CSV-207](https://issues.apache.org/jira/browse/CSV-207). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Adding a placeholder in the Lexer and CSV parser to store the end-of-line string. Fixes [CSV-214](https://issues.apache.org/jira/browse/CSV-214). Thanks to Nitin Mahendru, Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.4-2016-05-28"></a>

## Release 1.4 – 2016-05-28

| Type | Changes | By |
| --- | --- | --- |
| Update | Make CSVPrinter.print(Object) GC-free. Fixes [CSV-181](https://issues.apache.org/jira/browse/CSV-181). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Allow some printing operations directly from CSVFormat. Fixes [CSV-182](https://issues.apache.org/jira/browse/CSV-182). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Drop ferc.gov tests. Fixes [CSV-183](https://issues.apache.org/jira/browse/CSV-183). | [ggregory](#team--ggregory) |

<a id="changes--release-1.3-2016-05-09"></a>

## Release 1.3 – 2016-05-09

| Type | Changes | By |
| --- | --- | --- |
| Add | Add shortcut method for using first record as header to CSVFormat. Fixes [CSV-179](https://issues.apache.org/jira/browse/CSV-179). | [britter](#team--britter) |
| Add | Add withHeader(Class<? extends Enum>) to CSVFormat. Fixes [CSV-180](https://issues.apache.org/jira/browse/CSV-180). | [britter](#team--britter) |
| Update | Comment line hides next record; update Javadoc to make behavior clear. Fixes [CSV-167](https://issues.apache.org/jira/browse/CSV-167). Thanks to Rene. | [sebb](#team--sebb) |
| Update | CSVPrinter doesn't skip creation of header record if skipHeaderRecord is set to true. Fixes [CSV-153](https://issues.apache.org/jira/browse/CSV-153). Thanks to Wren. | [britter](#team--britter) |
| Add | Add IgnoreCase option for accessing header names. Fixes [CSV-159](https://issues.apache.org/jira/browse/CSV-159). Thanks to Yamil Medina. | [ggregory](#team--ggregory) |
| Add | The null string should be case-sensitive when reading records. Fixes [CSV-169](https://issues.apache.org/jira/browse/CSV-169). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CSVFormat.nullString should not be escaped. Fixes [CSV-168](https://issues.apache.org/jira/browse/CSV-168). Thanks to Gary Gregory, cornel creanga. | [ggregory](#team--ggregory) |
| Fix | CSVFormat.MYSQL nullString should be "\N". Fixes [CSV-170](https://issues.apache.org/jira/browse/CSV-170). Thanks to Gary Gregory, cornel creanga. | [ggregory](#team--ggregory) |
| Fix | Fix Javadoc to say CSVFormat with() methods return a new CSVFormat. Fixes [CSV-161](https://issues.apache.org/jira/browse/CSV-161). Thanks to Gary Gregory, Kristof Meixner, Emmanuel Bourg. | [ggregory](#team--ggregory) |
| Add | Support for ignoring trailing delimiter. Fixes [CSV-175](https://issues.apache.org/jira/browse/CSV-175). Thanks to Gary Gregory, Chris Jones. | [ggregory](#team--ggregory) |
| Add | Support trimming leading and trailing blanks. Fixes [CSV-177](https://issues.apache.org/jira/browse/CSV-177). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Create default formats for Informix UNLOAD and UNLOAD CSV. Fixes [CSV-178](https://issues.apache.org/jira/browse/CSV-178). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.2-2015-08-24"></a>

## Release 1.2 – 2015-08-24

| Type | Changes | By |
| --- | --- | --- |
| Fix | CSVFormat.with\* methods clear the header comments. Fixes [CSV-145](https://issues.apache.org/jira/browse/CSV-145). Thanks to Frank Ulbricht. | [ggregory](#team--ggregory) |
| Fix | Incorrect Javadoc on QuoteMode.NONE. Fixes [CSV-156](https://issues.apache.org/jira/browse/CSV-156). Thanks to Jason Steenstra-Pickens. | [ggregory](#team--ggregory) |
| Add | Add enum CSVFormat.Predefined that contains the default CSVFormat values. Fixes [CSV-157](https://issues.apache.org/jira/browse/CSV-157). | [ggregory](#team--ggregory) |

<a id="changes--release-1.1-2014-11-16"></a>

## Release 1.1 – 2014-11-16

| Type | Changes | By |
| --- | --- | --- |
| Fix | QuoteMode.NON\_NUMERIC doesn't work with CSVPrinter.printRecords(ResultSet). Fixes [CSV-140](https://issues.apache.org/jira/browse/CSV-140). Thanks to Damjan Jovanovic. | [ggregory](#team--ggregory) |
| Fix | CSVFormat#withHeader doesn't work well with #printComment, add withHeaderComments(String...). Fixes [CSV-130](https://issues.apache.org/jira/browse/CSV-130). Thanks to Sergei Lebedev. | [ggregory](#team--ggregory) |
| Fix | CSVFormat.EXCEL should ignore empty header names. Fixes [CSV-128](https://issues.apache.org/jira/browse/CSV-128). | [ggregory](#team--ggregory) |
| Fix | Incorrect Javadoc referencing org.apache.commons.csv.CSVFormat withQuote(). Fixes [CSV-132](https://issues.apache.org/jira/browse/CSV-132). Thanks to Sascha Szott. | [ggregory](#team--ggregory) |
| Update | Improve toString() implementation of CSVRecord. Fixes [CSV-124](https://issues.apache.org/jira/browse/CSV-124). Thanks to Kalyan. | [brentworden](#team--brentworden) |
| Update | Unified parameter validation. Fixes [CSV-134](https://issues.apache.org/jira/browse/CSV-134). Thanks to wu wen. | [ggregory](#team--ggregory) |
| Add | Add CSVFormat#with 0-arg methods matching boolean arg methods. Fixes [CSV-129](https://issues.apache.org/jira/browse/CSV-129). | [ggregory](#team--ggregory) |
| Add | Save positions of records to enable random access. Fixes [CSV-131](https://issues.apache.org/jira/browse/CSV-131). Thanks to Holger Stratmann. | [ggregory](#team--ggregory) |
| Add | CSVPrinter.printRecord(ResultSet) with metadata. Fixes [CSV-139](https://issues.apache.org/jira/browse/CSV-139). | [ggregory](#team--ggregory) |

<a id="changes--release-1.0-2014-08-14"></a>

## Release 1.0 – 2014-08-14

| Type | Changes | By |
| --- | --- | --- |
| Fix | No longer works with Java 6. Fixes [CSV-125](https://issues.apache.org/jira/browse/CSV-125). | [britter](#team--britter) |
| Fix | NullPointerException when empty header string and null string of "". Fixes [CSV-122](https://issues.apache.org/jira/browse/CSV-122). Thanks to Mike Lewis. | [britter](#team--britter) |
| Update | Validate format parameters in constructor. Fixes [CSV-117](https://issues.apache.org/jira/browse/CSV-117). | [sebb](#team--sebb) |
| Add | IllegalArgumentException thrown when the header contains duplicate names when the column names are empty. Fixes [CSV-121](https://issues.apache.org/jira/browse/CSV-121). Thanks to Sebastian Hardt. | [ggregory](#team--ggregory) |
| Add | CSVFormat#withHeader doesn't work with CSVPrinter. Fixes [CSV-120](https://issues.apache.org/jira/browse/CSV-120). Thanks to Sergei Lebedev. | [ggregory](#team--ggregory) |
| Add | CSVFormat is missing a print(...) method. Fixes [CSV-119](https://issues.apache.org/jira/browse/CSV-119). Thanks to Sergei Lebedev. | [ggregory](#team--ggregory) |
| Fix | CSVRecord.toMap() throws NPE on formats with no headers. Fixes [CSV-118](https://issues.apache.org/jira/browse/CSV-118). Thanks to Enrique Lara. | [ggregory](#team--ggregory) |
| Fix | Check whether ISE/IAE are being used appropriately. Fixes [CSV-113](https://issues.apache.org/jira/browse/CSV-113). | [sebb](#team--sebb) |
| Fix | CSVFormat constructor should reject a header array with duplicate entries. Fixes [CSV-114](https://issues.apache.org/jira/browse/CSV-114). | [sebb](#team--sebb) |
| Fix | HeaderMap is inconsistent when it is parsed from an input with duplicate columns names. Fixes [CSV-112](https://issues.apache.org/jira/browse/CSV-112). | [britter](#team--britter) |
| Fix | CSVRecord.toMap() fails if row length shorter than header length. Fixes [CSV-111](https://issues.apache.org/jira/browse/CSV-111). | [ggregory](#team--ggregory) |
| Fix | CSVFormat.format allways append null. Fixes [CSV-106](https://issues.apache.org/jira/browse/CSV-106). | [ggregory](#team--ggregory) |
| Add | Add Map conversion API to CSVRecord. Fixes [CSV-105](https://issues.apache.org/jira/browse/CSV-105). | [ggregory](#team--ggregory) |
| Fix | CSVParser: getHeaderMap throws NPE. Fixes [CSV-100](https://issues.apache.org/jira/browse/CSV-100). | [ggregory](#team--ggregory) |
| Update | Lots of possible changes. Fixes [CSV-42](https://issues.apache.org/jira/browse/CSV-42). Thanks to Bob Smith. | [ebourg](#team--ebourg) |
| Update | Use Character instead of char for char fields except delimiter. Fixes [CSV-78](https://issues.apache.org/jira/browse/CSV-78). | [sebb](#team--sebb) |
| Update | Revert Builder implementation in CSVFormat. Fixes [CSV-99](https://issues.apache.org/jira/browse/CSV-99). | [britter](#team--britter) |
| Fix | CSVRecord does not verify that the length of the header mapping matches the number of values. Fixes [CSV-53](https://issues.apache.org/jira/browse/CSV-53). | [britter](#team--britter) |
| Update | Allow the handling of NULL values. Fixes [CSV-93](https://issues.apache.org/jira/browse/CSV-93). | [ggregory](#team--ggregory) |
| Update | Use the Builder pattern for CSVFormat. Fixes [CSV-68](https://issues.apache.org/jira/browse/CSV-68). | [ggregory](#team--ggregory) |
| Update | Clarify comment handling. Fixes [CSV-84](https://issues.apache.org/jira/browse/CSV-84). | [sebb](#team--sebb) |
| Update | CSVParser.nextValue() seems pointless. Fixes [CSV-25](https://issues.apache.org/jira/browse/CSV-25). | [ebourg](#team--ebourg) |
| Update | Allow the String value for null to be customized for the CSV printer. Fixes [CSV-97](https://issues.apache.org/jira/browse/CSV-97). | [ggregory](#team--ggregory) |
| Update | Not possible to create a CSVFormat from scratch. Fixes [CSV-88](https://issues.apache.org/jira/browse/CSV-88). | [ggregory](#team--ggregory) |
| Add | Keep track of record number. Fixes [CSV-52](https://issues.apache.org/jira/browse/CSV-52). | [ggregory](#team--ggregory) |
| Update | Lexer should only use char fields. Fixes [CSV-94](https://issues.apache.org/jira/browse/CSV-94). | [sebb](#team--sebb) |
| Add | Need a way to extract parsed headers, e.g. for use in formatting output. Fixes [CSV-92](https://issues.apache.org/jira/browse/CSV-92). | [ggregory](#team--ggregory) |
| Add | Header support. Fixes [CSV-65](https://issues.apache.org/jira/browse/CSV-65). | [ebourg](#team--ebourg) |
| Fix | Confusing semantic of the ignore leading/trailing spaces parameters. Fixes [CSV-54](https://issues.apache.org/jira/browse/CSV-54). | [sebb](#team--sebb) |
| Update | Add convenience methods to CSVLexer. Fixes [CSV-71](https://issues.apache.org/jira/browse/CSV-71). | [sebb](#team--sebb) |
| Update | Is CharBuffer really needed, now that StringBuilder is available?. Fixes [CSV-59](https://issues.apache.org/jira/browse/CSV-59). | [ebourg](#team--ebourg) |
| Update | Replace while(true)-loop in CSVParser.getRecord with do-while-loop. Fixes [CSV-55](https://issues.apache.org/jira/browse/CSV-55). | [britter](#team--britter) |
| Fix | CSVFormat describes itself as immutable, but it is not - in particular it is not thread-safe. Fixes [CSV-34](https://issues.apache.org/jira/browse/CSV-34). | [sebb](#team--sebb) |
| Fix | Endless loops in CSV parser. Fixes [CSV-36](https://issues.apache.org/jira/browse/CSV-36). | [yonik](#team--yonik) |
| Fix | NullPointerException in CSVPrinter.print()/println(). Fixes [CSV-13](https://issues.apache.org/jira/browse/CSV-13). | [ebourg](#team--ebourg) |
| Update | CSVPrinter overhaul. Fixes [CSV-45](https://issues.apache.org/jira/browse/CSV-45). | [yonik](#team--yonik) |
| Fix | Excel strategy uses wrong separator. Fixes [CSV-23](https://issues.apache.org/jira/browse/CSV-23). | [ebourg](#team--ebourg) |
| Update | CSVStrategy has modifiable public static variables. Fixes [CSV-49](https://issues.apache.org/jira/browse/CSV-49). Thanks to Bob Smith. | [ebourg](#team--ebourg) |
| Add | Predefined format for MYSQL. Fixes [CSV-48](https://issues.apache.org/jira/browse/CSV-48). | [ebourg](#team--ebourg) |
| Update | Reduce visibility of methods in internal classes. Fixes [CSV-46](https://issues.apache.org/jira/browse/CSV-46). | [ebourg](#team--ebourg) |
| Update | ExtendedBufferedReader does too much. Fixes [CSV-26](https://issues.apache.org/jira/browse/CSV-26). | [jacopoc](#team--jacopoc) |
| Update | Decide whether to keep the csv.writer subpackage. Fixes [CSV-27](https://issues.apache.org/jira/browse/CSV-27). | [ebourg](#team--ebourg) |

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/scm.html -->

<!-- page_index: 3 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-csv.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-csv.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-csv.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/security.html -->

<!-- page_index: 4 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-csv/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

None.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons CSV library provides a simple interface for reading and writing CSV files of various types. |
| [Summary](https://commons.apache.org/proper/commons-csv/summary.html) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-csv/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-csv/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-csv/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-csv/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-csv/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-csv/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-csv/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/team.html -->

<!-- page_index: 6 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | mvdb | Martin van den Bemt | [mvdb@apache.org](mailto:mvdb@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | yonik | Yonik Seeley | [yonik@apache.org](mailto:yonik@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | ebourg | Emmanuel Bourg | [ebourg@apache.org](mailto:ebourg@apache.org) | - | Apache | - | - | - |
|  | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
|  | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | The Apache Software Foundation | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Name |
| --- |
| Bob Smith |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/ci-management.html -->

<!-- page_index: 7 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-csv/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/project-reports.html -->

<!-- page_index: 8 -->

<a id="project-reports--generated-reports"></a>

# Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](https://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [Changes](#changes) | Changes report on releases of this project. |
| [JIRA Report](#jira-changes) | Report on Issues from the JIRA Issue Tracking System. |
| [Javadoc](https://commons.apache.org/proper/commons-csv/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-csv/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-csv/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire](#surefire) | Report on the test results of the project. |
| [Rat Report](#rat-report) | Report on compliance to license related source code policies |
| [JaCoCo](https://commons.apache.org/proper/commons-csv/jacoco/index.html) | JaCoCo Coverage Report. |
| [japicmp](#japicmp) | Comparing source compatibility of commons-csv-1.14.2-SNAPSHOT.jar against commons-csv-1.14.1.jar |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [CPD](#cpd) | Duplicate code detection. |
| [PMD](#pmd) | Verification of coding rules. |
| [Tag List](#taglist) | Report on various tags found in the code. |

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/jira-changes.html -->

<!-- page_index: 9 -->

# JIRA Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="JIRA_Report"></a>
DOC2MDPLACEHOLDERTOKEN0END<h1>JIRA Report</h1>
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
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-297">CSV-297</a></td>
<td>Parser</td>
<td>setHeader() does not consider the separator while parse header row</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-244">CSV-244</a></td>
<td>-</td>
<td>Test case failures following CSVFormat#equals() update</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-243">CSV-243</a></td>
<td>-</td>
<td>CSVFormat withTrim() and withIgnoreSurroundingSpaces() need better docs</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-242">CSV-242</a></td>
<td>-</td>
<td>CSVFormat equals() and hashCode() don't use all fields</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-235">CSV-235</a></td>
<td>Parser</td>
<td>WRONG Implementation for RFC4180  </td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-221">CSV-221</a></td>
<td>Documentation</td>
<td>Links to Javadoc for 1.5 give a 404</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-213">CSV-213</a></td>
<td>Parser</td>
<td>CSVParser#iterator()#hasNext() fails</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-186">CSV-186</a></td>
<td>-</td>
<td>SIte archives archive links don't work</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-144">CSV-144</a></td>
<td>Documentation</td>
<td>Broken link on project's nav panel, for item "Javadoc 1.1"</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-98">CSV-98</a></td>
<td>-</td>
<td>Line number counting is confusing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-90">CSV-90</a></td>
<td>-</td>
<td>CSVFormat isEscaping/isEncapsulating are not public</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-87">CSV-87</a></td>
<td>-</td>
<td>CSVParser.getRecords() returns null rather than empty List at EOF</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-82">CSV-82</a></td>
<td>-</td>
<td>CSVRecord inconsistent behaviour when header mapping is not found</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-80">CSV-80</a></td>
<td>-</td>
<td>CSVLexer.nextToken does not need wsBuf</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-79">CSV-79</a></td>
<td>-</td>
<td>CSVFormat.isCommentingDisabled() is confusing/confused</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-77">CSV-77</a></td>
<td>-</td>
<td>RFC 4180 (DEFAULT) format is wrong; should not ignore spaces or blank lines</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-75">CSV-75</a></td>
<td>-</td>
<td>ExtendedBufferReader does not handle EOL consistently</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-72">CSV-72</a></td>
<td>-</td>
<td>CSVFormat.DEFAULT should be renamed as RFC4180</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-67">CSV-67</a></td>
<td>-</td>
<td>UnicodeUnescapeReader should not be applied before parsing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-60">CSV-60</a></td>
<td>-</td>
<td>CSVParser.iterator().remove() should throw throw new UnsupportedOperationException()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-24">CSV-24</a></td>
<td>-</td>
<td>Remove stdout from tests</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-19">CSV-19</a></td>
<td>-</td>
<td>Nightly Maven repository deployment</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-18">CSV-18</a></td>
<td>-</td>
<td>CharBuffer is too slow.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-17">CSV-17</a></td>
<td>-</td>
<td>[PATCH] CSV can't handle missing entries in the Map - or non-String map values</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-14">CSV-14</a></td>
<td>-</td>
<td>backslash before quote character gives an error</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-10">CSV-10</a></td>
<td>-</td>
<td>CSVParser allow strategy in constructor</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-9">CSV-9</a></td>
<td>-</td>
<td>CSVStrategy.clone()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-8">CSV-8</a></td>
<td>-</td>
<td>Excel strategy separator error</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-7">CSV-7</a></td>
<td>Parser</td>
<td>CSVParser.getLine() blocks until char after eol is recieved.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-6">CSV-6</a></td>
<td>Build</td>
<td>ant javadoc fails</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-285">CSV-285</a></td>
<td>-</td>
<td>Replace BufferedReader with PushbackReader</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-260">CSV-260</a></td>
<td>Parser</td>
<td>Replace Assertions.notNull with Objects.requireNonNull</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-188">CSV-188</a></td>
<td>Parser</td>
<td>Returns headers as list</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-117">CSV-117</a></td>
<td>Parser</td>
<td>Validate format parameters in constructor</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-115">CSV-115</a></td>
<td>-</td>
<td>Simplify boolean expressions in CSVRecord</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-85">CSV-85</a></td>
<td>-</td>
<td>Allow comments to be returned in CSVRecord</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-81">CSV-81</a></td>
<td>-</td>
<td>Token.Type.isReady could perhaps be removed</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-74">CSV-74</a></td>
<td>-</td>
<td>CSVFormat definitions are difficult to read and maintain</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-57">CSV-57</a></td>
<td>Parser</td>
<td>CSVParser.getRecords() contract is confusing</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-175">CSV-175</a></td>
<td>Parser</td>
<td>Support for ignoring trailing delimiter</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-139">CSV-139</a></td>
<td>Printer</td>
<td>CSVPrinter.printRecord(ResultSet) with metadata</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-252">CSV-252</a></td>
<td>Build</td>
<td>Upgrade test framework to JUnit 5 Jupiter</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-69">CSV-69</a></td>
<td>-</td>
<td>Eliminate CSVPrinterTest.equals(String[][], String[][]) by using Assert.assertArrayEquals</td>
<td>Test</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-95">CSV-95</a></td>
<td>-</td>
<td>Create a git mirror for CSV</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.14.2</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-320">CSV-320</a></td>
<td>Build</td>
<td>Remove Spotbugs Dependency and use exclude-filter instead</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.14.1</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-318">CSV-318</a></td>
<td>Printer</td>
<td>CSVPrinter.printRecord(Stream) hangs if given a parallel stream</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.14.1</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-273">CSV-273</a></td>
<td>Build</td>
<td>Define automatic Java module name for jar file</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.14.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-317">CSV-317</a></td>
<td>-</td>
<td>Release history link changed from changes-report.html to changes.html</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.13.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-314">CSV-314</a></td>
<td>-</td>
<td>Missing OSGi Import-Package versions in Manifest can make commons-csv unusable in OSGi environments</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.13.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-196">CSV-196</a></td>
<td>Parser</td>
<td>Store the information of raw data read by lexer</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.13.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-313">CSV-313</a></td>
<td>Printer</td>
<td>Add CSVPrinter.getRecordCount()</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.12.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-294">CSV-294</a></td>
<td>-</td>
<td>CSVFormat does not support explicit " as escape char</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.12.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-150">CSV-150</a></td>
<td>Parser</td>
<td>Escaping is not disableable</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.12.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-270">CSV-270</a></td>
<td>Parser</td>
<td>Throw a different Expeciton type on malformed CSV input</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-311">CSV-311</a></td>
<td>Printer</td>
<td>OutOfMemory for very long rows despite using column value of type Reader</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-306">CSV-306</a></td>
<td>Documentation</td>
<td>The User Guide examples use deprecated methods</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-310">CSV-310</a></td>
<td>Parser</td>
<td>Misleading error message when QuoteMode set to None</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-309">CSV-309</a></td>
<td>Parser</td>
<td>Remove duplicate exception class name from message</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-308">CSV-308</a></td>
<td>Documentation, Printer</td>
<td>Javadoc example for method 'setHeaderComments'</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-147">CSV-147</a></td>
<td>Parser</td>
<td>Better error message during faulty CSV record read</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-300">CSV-300</a></td>
<td>-</td>
<td>CSVRecord.toList() does not give write access to the new List</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-299">CSV-299</a></td>
<td>Parser</td>
<td>get unexpected results when setting the delimiter to ‘||’</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-292">CSV-292</a></td>
<td>Build</td>
<td>No Automatic-Module-Name prevents usage in JPMS projects without repacking the JAR</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-291">CSV-291</a></td>
<td>-</td>
<td>CSVRecord.values() accessor is package-private instead of public</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-290">CSV-290</a></td>
<td>Parser</td>
<td>Produced CSV using PostgreSQL format cannot be read</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-288">CSV-288</a></td>
<td>-</td>
<td>String delimiter (||) is not working as expected.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-274">CSV-274</a></td>
<td>Parser</td>
<td>CSVParser.iterator() does not iterate over result set as expected.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-269">CSV-269</a></td>
<td>Parser</td>
<td>CSVRecord.get(Enum) should use Enum.name() instead of Enum.toString()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-264">CSV-264</a></td>
<td>Parser</td>
<td>Duplicate empty header names are allowed even with `.withAllowDuplicateHeaderNames(false)`</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-254">CSV-254</a></td>
<td>-</td>
<td>POSTGRESQL_CSV cannot parse correctly (null vs zero-length string)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-164">CSV-164</a></td>
<td>-</td>
<td>Support duplicate header names</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-304">CSV-304</a></td>
<td>Parser</td>
<td>Provide access methods for header and trailer comments</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-295">CSV-295</a></td>
<td>Printer</td>
<td>Support for parallelism in CSVPrinter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-236">CSV-236</a></td>
<td>Parser</td>
<td>Allow duplicate headers in CSV File</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-143">CSV-143</a></td>
<td>-</td>
<td>CSVPrinter ill-suited in multithreaded environment</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-216">CSV-216</a></td>
<td>Parser</td>
<td>Allow for mutable CSV records</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-296">CSV-296</a></td>
<td>Parser</td>
<td>Delimiter followed by Whitespace then by Quotes Failing with setTrim(true)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-271">CSV-271</a></td>
<td>Printer</td>
<td>Missing separator with "print(object)" followed by "printRecord(Object[])"</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-265">CSV-265</a></td>
<td>Parser</td>
<td>CSV comments break CSVRecord#getCharacterPosition</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-263">CSV-263</a></td>
<td>Printer</td>
<td>Print from Reader with embedded quotes generates incorrect output</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-259">CSV-259</a></td>
<td>Printer</td>
<td>CSVFormat.printWithEscapes throws StringIndexOutOfBoundsException when value is Reader</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-211">CSV-211</a></td>
<td>-</td>
<td>CSVFormat.format trims last delimiter if the delimiter is a white space</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-195">CSV-195</a></td>
<td>Parser</td>
<td>Parser iterates over the last CSV Record twice.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-158">CSV-158</a></td>
<td>Parser</td>
<td>Fix EOL checking for read array in ExtendedBufferedReader</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-149">CSV-149</a></td>
<td>Parser</td>
<td>Line number is not proper at EOF</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-148">CSV-148</a></td>
<td>Printer</td>
<td>Add test cases for withIgnoreSurroundingSpaces() and withTrim() #70</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-284">CSV-284</a></td>
<td>-</td>
<td>Formalize PerformanceTest</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-283">CSV-283</a></td>
<td>-</td>
<td>Remove Whitespace Check Determines Delimiter Twice</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-282">CSV-282</a></td>
<td>-</td>
<td>Document and Automate CSV Benchmark Harness</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-275">CSV-275</a></td>
<td>Parser</td>
<td>Make CSVRecord.toList() public</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-267">CSV-267</a></td>
<td>-</td>
<td>Minor improvements</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-253">CSV-253</a></td>
<td>Parser</td>
<td>Handle absent values in input (null)</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-206">CSV-206</a></td>
<td>-</td>
<td>Add support for String delimiters #76</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-184">CSV-184</a></td>
<td>Parser</td>
<td>Make the method CSVRecord#putIn(Map) public</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-93">CSV-93</a></td>
<td>Documentation, Parser, Printer</td>
<td>Allow the handling of NULL values</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-123">CSV-123</a></td>
<td>Printer</td>
<td>Add possibility to use ResultSet header meta data as CSV header</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-248">CSV-248</a></td>
<td>-</td>
<td>CSVRecord is not Serializable</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.8</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-247">CSV-247</a></td>
<td>-</td>
<td>A single empty header is allowed when not allowing empty column headers.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.8</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-245">CSV-245</a></td>
<td>-</td>
<td>Post 1.7 release fixes.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.8</td>
<td><a href="https://issues.apache.org/jira/browse/CSV-241">CSV-241</a></td>
<td>-</td>
<td>CSVFormat#valiadte() does not account for allowDuplicateHeaderNames #43</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/surefire.html -->

<!-- page_index: 10 -->

<a id="surefire--surefire-report"></a>

# Surefire Report

<a id="surefire--summary"></a>

## Summary

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 923 | 0 | 0 | 11 | 98.8% | 2.306 s |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

<a id="surefire--package-list"></a>

## Package List

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Package | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.csv.issues](#surefire--org.apache.commons.csv.issues) | 60 | 0 | 0 | 0 | 100% | 0.144 s |
| [org.apache.commons.csv](#surefire--org.apache.commons.csv) | 863 | 0 | 0 | 11 | 98.7% | 2.162 s |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

<a id="surefire--org.apache.commons.csv.issues"></a>

### org.apache.commons.csv.issues

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [JiraCsv213Test](#surefire--org.apache.commons.csv.issues.jiracsv213test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv203Test](#surefire--org.apache.commons.csv.issues.jiracsv203test) | 7 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv271Test](#surefire--org.apache.commons.csv.issues.jiracsv271test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv198Test](#surefire--org.apache.commons.csv.issues.jiracsv198test) | 1 | 0 | 0 | 0 | 100% | 0.132 s |
|  | [JiraCsv257Test](#surefire--org.apache.commons.csv.issues.jiracsv257test) | 3 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv247Test](#surefire--org.apache.commons.csv.issues.jiracsv247test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv294Test](#surefire--org.apache.commons.csv.issues.jiracsv294test) | 4 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv150Test](#surefire--org.apache.commons.csv.issues.jiracsv150test) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv254Test](#surefire--org.apache.commons.csv.issues.jiracsv254test) | 1 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv149Test](#surefire--org.apache.commons.csv.issues.jiracsv149test) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv148Test](#surefire--org.apache.commons.csv.issues.jiracsv148test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv263Test](#surefire--org.apache.commons.csv.issues.jiracsv263test) | 1 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv211Test](#surefire--org.apache.commons.csv.issues.jiracsv211test) | 1 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv167Test](#surefire--org.apache.commons.csv.issues.jiracsv167test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv154Test](#surefire--org.apache.commons.csv.issues.jiracsv154test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv249Test](#surefire--org.apache.commons.csv.issues.jiracsv249test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv248Test](#surefire--org.apache.commons.csv.issues.jiracsv248test) | 1 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [JiraCsv265Test](#surefire--org.apache.commons.csv.issues.jiracsv265test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv93Test](#surefire--org.apache.commons.csv.issues.jiracsv93test) | 3 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv253Test](#surefire--org.apache.commons.csv.issues.jiracsv253test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv288Test](#surefire--org.apache.commons.csv.issues.jiracsv288test) | 12 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv206Test](#surefire--org.apache.commons.csv.issues.jiracsv206test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [JiraCsv264Test](#surefire--org.apache.commons.csv.issues.jiracsv264test) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [JiraCsv290Test](#surefire--org.apache.commons.csv.issues.jiracsv290test) | 3 | 0 | 0 | 0 | 100% | 0.001 s |

<a id="surefire--org.apache.commons.csv"></a>

### org.apache.commons.csv

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [JiraCsv318Test](#surefire--org.apache.commons.csv.jiracsv318test) | 5 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [CSVDuplicateHeaderTest](#surefire--org.apache.commons.csv.csvduplicateheadertest) | 348 | 0 | 0 | 0 | 100% | 0.099 s |
|  | [CSVFormatPredefinedTest](#surefire--org.apache.commons.csv.csvformatpredefinedtest) | 10 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [ExtendedBufferedReaderTest](#surefire--org.apache.commons.csv.extendedbufferedreadertest) | 6 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TokenTest](#surefire--org.apache.commons.csv.tokentest) | 5 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [CSVFormatTest](#surefire--org.apache.commons.csv.csvformattest) | 109 | 0 | 0 | 0 | 100% | 0.017 s |
|  | [JiraCsv196Test](#surefire--org.apache.commons.csv.jiracsv196test) | 2 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [CSVParserTest](#surefire--org.apache.commons.csv.csvparsertest) | 154 | 0 | 0 | 4 | 97.4% | 0.034 s |
|  | [CSVPrinterTest](#surefire--org.apache.commons.csv.csvprintertest) | 144 | 0 | 0 | 7 | 95.1% | 1.920 s |
|  | [UserGuideTest](#surefire--org.apache.commons.csv.userguidetest) | 2 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [CSVRecordTest](#surefire--org.apache.commons.csv.csvrecordtest) | 31 | 0 | 0 | 0 | 100% | 0.012 s |
|  | [LexerTest](#surefire--org.apache.commons.csv.lexertest) | 33 | 0 | 0 | 0 | 100% | 0.050 s |
|  | [CSVFileParserTest](#surefire--org.apache.commons.csv.csvfileparsertest) | 14 | 0 | 0 | 0 | 100% | 0.008 s |

<a id="surefire--test-cases"></a>

## Test Cases

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

<a id="surefire--jiracsv213test"></a>

### JiraCsv213Test

|  |  |  |
| --- | --- | --- |
|  | test | 0 s |

<a id="surefire--jiracsv203test"></a>

### JiraCsv203Test

|  |  |  |
| --- | --- | --- |
|  | testQuoteModeMinimal | 0 s |
|  | testWithoutQuoteMode | 0 s |
|  | testQuoteModeNonNumeric | 0 s |
|  | testQuoteModeAllNonNull | 0 s |
|  | testWithEmptyValues | 0.001 s |
|  | testWithoutNullString | 0 s |
|  | testQuoteModeAll | 0 s |

<a id="surefire--jiracsv271test"></a>

### JiraCsv271Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv271\_withList | 0 s |
|  | testJiraCsv271\_withArray | 0 s |

<a id="surefire--jiracsv198test"></a>

### JiraCsv198Test

|  |  |  |
| --- | --- | --- |
|  | test | 0.131 s |

<a id="surefire--jiracsv257test"></a>

### JiraCsv257Test

|  |  |  |
| --- | --- | --- |
|  | testNoHeaderBuilder | 0 s |
|  | testHeaderDepreacted | 0 s |
|  | testHeaderBuilder | 0 s |

<a id="surefire--jiracsv247test"></a>

### JiraCsv247Test

|  |  |  |
| --- | --- | --- |
|  | testHeadersMissingThrowsWhenNotAllowingMissingColumnNames | 0 s |
|  | testHeadersMissingOneColumnWhenAllowingMissingColumnNames | 0 s |

<a id="surefire--jiracsv318test"></a>

### JiraCsv318Test

|  |  |  |
| --- | --- | --- |
|  | testDefaultStream | 0 s |
|  | testParallelIOStream | 0.002 s |
|  | testSequentialStream | 0 s |
|  | testParallelStream | 0.001 s |
|  | testParallelIOStreamSynchronizedPrinterNotUsed | 0.004 s |

<a id="surefire--csvduplicateheadertest"></a>

### CSVDuplicateHeaderTest

|  |  |  |
| --- | --- | --- |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[1] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[2] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[3] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[4] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[5] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[6] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[7] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[8] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[9] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[10] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[11] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[12] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[13] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[14] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[15] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[16] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[17] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[18] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[19] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[20] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[21] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[22] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[23] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[24] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[25] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[26] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[27] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[28] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[29] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[30] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[31] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[32] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[33] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[34] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[35] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[36] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[37] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[38] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[39] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[40] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[41] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[42] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[43] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[44] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[45] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[46] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[47] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[48] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[49] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[50] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[51] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[52] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[53] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[54] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[55] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[56] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[57] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[58] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[59] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[60] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[61] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[62] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[63] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[64] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[65] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[66] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[67] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[68] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[69] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[70] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[71] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[72] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[73] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[74] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[75] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[76] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[77] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[78] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[79] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[80] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[81] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[82] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[83] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[84] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[85] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[86] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[87] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[88] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[89] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[90] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[91] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[92] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[93] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[94] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[95] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[96] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[97] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[98] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[99] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[100] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[101] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[102] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[103] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[104] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[105] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[106] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[107] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[108] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[109] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[110] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[111] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[112] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[113] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[114] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[115] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[116] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[117] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[118] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[119] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[120] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[121] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[122] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[123] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[124] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[125] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[126] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[127] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[128] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[129] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[130] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[131] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[132] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[133] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[134] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[135] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[136] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[137] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[138] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[139] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[140] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[141] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[142] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[143] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[144] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[145] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[146] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[147] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[148] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[149] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[150] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[151] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[152] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[153] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[154] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[155] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[156] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[157] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[158] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[159] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[160] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[161] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[162] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[163] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[164] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[165] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[166] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[167] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[168] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[169] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[170] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[171] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[172] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[173] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[174] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[175] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[176] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[177] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[178] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[179] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[180] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[181] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[182] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[183] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[184] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[185] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[186] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[187] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[188] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[189] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[190] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[191] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[192] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[193] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[194] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[195] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[196] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[197] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[198] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[199] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[200] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[201] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[202] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[203] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[204] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[205] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[206] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[207] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[208] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[209] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[210] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[211] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[212] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[213] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[214] | 0 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[215] | 0.001 s |
|  | testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[216] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[1] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[2] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[3] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[4] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[5] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[6] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[7] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[8] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[9] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[10] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[11] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[12] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[13] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[14] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[15] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[16] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[17] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[18] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[19] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[20] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[21] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[22] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[23] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[24] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[25] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[26] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[27] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[28] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[29] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[30] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[31] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[32] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[33] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[34] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[35] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[36] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[37] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[38] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[39] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[40] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[41] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[42] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[43] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[44] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[45] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[46] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[47] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[48] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[49] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[50] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[51] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[52] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[53] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[54] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[55] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[56] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[57] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[58] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[59] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[60] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[61] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[62] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[63] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[64] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[65] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[66] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[67] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[68] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[69] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[70] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[71] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[72] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[73] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[74] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[75] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[76] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[77] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[78] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[79] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[80] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[81] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[82] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[83] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[84] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[85] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[86] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[87] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[88] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[89] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[90] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[91] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[92] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[93] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[94] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[95] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[96] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[97] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[98] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[99] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[100] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[101] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[102] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[103] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[104] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[105] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[106] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[107] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[108] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[109] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[110] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[111] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[112] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[113] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[114] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[115] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[116] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[117] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[118] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[119] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[120] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[121] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[122] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[123] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[124] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[125] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[126] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[127] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[128] | 0.001 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[129] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[130] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[131] | 0 s |
|  | testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[132] | 0 s |

<a id="surefire--csvformatpredefinedtest"></a>

### CSVFormatPredefinedTest

|  |  |  |
| --- | --- | --- |
|  | testTDF | 0 s |
|  | testExcel | 0 s |
|  | testMySQL | 0 s |
|  | testMongoDbCsv | 0 s |
|  | testMongoDbTsv | 0 s |
|  | testRFC4180 | 0 s |
|  | testPostgreSqlCsv | 0 s |
|  | testPostgreSqlText | 0 s |
|  | testDefault | 0 s |
|  | testOracle | 0 s |

<a id="surefire--jiracsv294test"></a>

### JiraCsv294Test

|  |  |  |
| --- | --- | --- |
|  | testDefaultCsvFormatWithQuoteEscapeWorks | 0 s |
|  | testDefaultCsvFormatWithBackslashEscapeWorks | 0 s |
|  | testDefaultCsvFormatWorks | 0 s |
|  | testDefaultCsvFormatWithNullEscapeWorks | 0.001 s |

<a id="surefire--extendedbufferedreadertest"></a>

### ExtendedBufferedReaderTest

|  |  |  |
| --- | --- | --- |
|  | testEmptyInput | 0 s |
|  | testReadChar | 0 s |
|  | testReadLine | 0.001 s |
|  | testReadLookahead1 | 0 s |
|  | testReadLookahead2 | 0 s |
|  | testReadingInDifferentBuffer | 0 s |

<a id="surefire--jiracsv150test"></a>

### JiraCsv150Test

|  |  |  |
| --- | --- | --- |
|  | testDisableEscaping | 0 s |
|  | testDisableEncapsulation | 0 s |
|  | testDisableComment | 0 s |

<a id="surefire--jiracsv254test"></a>

### JiraCsv254Test

|  |  |  |
| --- | --- | --- |
|  | test | 0 s |

<a id="surefire--tokentest"></a>

### TokenTest

|  |  |  |
| --- | --- | --- |
|  | testToString(Type)[1] | 0 s |
|  | testToString(Type)[2] | 0 s |
|  | testToString(Type)[3] | 0.001 s |
|  | testToString(Type)[4] | 0 s |
|  | testToString(Type)[5] | 0 s |

<a id="surefire--jiracsv149test"></a>

### JiraCsv149Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv149EndWithEOL | 0 s |
|  | testJiraCsv149EndWithoutEOL | 0.001 s |

<a id="surefire--jiracsv148test"></a>

### JiraCsv148Test

|  |  |  |
| --- | --- | --- |
|  | testWithTrimEmpty | 0 s |
|  | testWithIgnoreSurroundingSpacesEmpty | 0 s |

<a id="surefire--jiracsv263test"></a>

### JiraCsv263Test

|  |  |  |
| --- | --- | --- |
|  | testPrintFromReaderWithQuotes | 0.001 s |

<a id="surefire--jiracsv211test"></a>

### JiraCsv211Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv211Format | 0.001 s |

<a id="surefire--jiracsv167test"></a>

### JiraCsv167Test

|  |  |  |
| --- | --- | --- |
|  | testParse | 0 s |

<a id="surefire--jiracsv154test"></a>

### JiraCsv154Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv154\_withCommentMarker | 0 s |
|  | testJiraCsv154\_withHeaderComments | 0 s |

<a id="surefire--jiracsv249test"></a>

### JiraCsv249Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv249 | 0 s |

<a id="surefire--jiracsv248test"></a>

### JiraCsv248Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv248 | 0.002 s |

<a id="surefire--csvformattest"></a>

### CSVFormatTest

|  |  |  |
| --- | --- | --- |
|  | testEqualsIgnoreSurroundingSpaces | 0 s |
|  | testDelimiterSameAsEscapeThrowsException\_Deprecated | 0 s |
|  | testPrintWithQuoteModeIsNONE | 0 s |
|  | testEqualsCommentStart | 0.001 s |
|  | testQuoteCharSameAsDelimiterThrowsException\_Deprecated | 0 s |
|  | testJiraCsv236 | 0 s |
|  | testEscapeSameAsCommentStartThrowsExceptionForWrapperType\_Deprecated | 0 s |
|  | testWithDelimiter | 0 s |
|  | testEscapeSameAsCommentStartThrowsException\_Deprecated | 0 s |
|  | testToStringAndWithCommentMarkerTakingCharacter | 0.001 s |
|  | testQuotePolicyNoneWithoutEscapeThrowsException | 0 s |
|  | testWithQuoteLFThrowsException | 0 s |
|  | testWithFirstRecordAsHeader | 0 s |
|  | testEqualsNullString\_Deprecated | 0.001 s |
|  | testJiraCsv236\_\_Deprecated | 0 s |
|  | testSerialization | 0.001 s |
|  | testNullRecordSeparatorCsv106 | 0 s |
|  | testGetDuplicateHeaderMode | 0 s |
|  | testEqualsQuoteChar | 0.001 s |
|  | testBuildVsGet | 0 s |
|  | testTrim | 0 s |
|  | testNullRecordSeparatorCsv106\_\_Deprecated | 0 s |
|  | testToString | 0 s |
|  | testWithEmptyDuplicates | 0 s |
|  | testWithHeaderComments | 0 s |
|  | testPrintRecord | 0 s |
|  | testGetAllowDuplicateHeaderNames | 0 s |
|  | testPrintRecordEmpty | 0.001 s |
|  | testEqualsQuoteChar\_Deprecated | 0 s |
|  | testQuoteCharSameAsCommentStartThrowsException | 0 s |
|  | testWithRecordSeparatorCR | 0 s |
|  | testWithRecordSeparatorLF | 0 s |
|  | testDelimiterSameAsCommentStartThrowsException\_Deprecated | 0 s |
|  | testPrintWithEscapesEndWithoutCRLF | 0 s |
|  | testWithEscapeCRThrowsExceptions | 0 s |
|  | testWithSystemRecordSeparator | 0.001 s |
|  | testWithIgnoreEmptyLines | 0 s |
|  | testEqualsNoQuotes | 0 s |
|  | testHashCodeAndWithIgnoreHeaderCase | 0 s |
|  | testDelimiterEmptyStringThrowsException1 | 0 s |
|  | testDuplicateHeaderElementsTrue | 0 s |
|  | testEqualsSkipHeaderRecord\_Deprecated | 0 s |
|  | testEqualsIgnoreSurroundingSpaces\_Deprecated | 0 s |
|  | testEqualsEscape | 0 s |
|  | testEqualsHeader | 0 s |
|  | testEqualsIgnoreEmptyLines | 0 s |
|  | testDuplicateHeaderElementsTrueContainsEmpty1 | 0.001 s |
|  | testDuplicateHeaderElementsTrueContainsEmpty2 | 0 s |
|  | testDuplicateHeaderElementsTrueContainsEmpty3 | 0 s |
|  | testDelimiterCharLineBreakCrThrowsException1 | 0 s |
|  | testEqualsHash | 0.001 s |
|  | testDuplicateHeaderElementsTrue\_Deprecated | 0 s |
|  | testWithCommentStart | 0 s |
|  | testNewFormat | 0 s |
|  | testWithIgnoreSurround | 0 s |
|  | testRFC4180 | 0.001 s |
|  | testDelimiterSameAsRecordSeparatorThrowsException | 0 s |
|  | testEscapeSameAsCommentStartThrowsException | 0 s |
|  | testFormatThrowsNullPointerException | 0 s |
|  | testEqualsDelimiter | 0 s |
|  | testEqualsRecordSeparator\_Deprecated | 0 s |
|  | testDelimiterSameAsCommentStartThrowsException1 | 0 s |
|  | testWithHeaderResultSetNull | 0 s |
|  | testDuplicateHeaderElements\_Deprecated | 0 s |
|  | testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType | 0 s |
|  | testDelimiterSameAsEscapeThrowsException1 | 0 s |
|  | testEqualsQuotePolicy\_Deprecated | 0 s |
|  | testQuoteCharSameAsCommentStartThrowsException\_Deprecated | 0.001 s |
|  | testDelimiterCharLineBreakLfThrowsException1 | 0 s |
|  | testEqualsNullString | 0 s |
|  | testEqualsHeader\_Deprecated | 0 s |
|  | testDelimiterStringLineBreakCrThrowsException1 | 0 s |
|  | testEqualsCommentStart\_Deprecated | 0 s |
|  | testWithQuotePolicy | 0 s |
|  | testDuplicateHeaderElementsFalse | 0 s |
|  | testEqualsQuotePolicy | 0.001 s |
|  | testEscapeSameAsCommentStartThrowsExceptionForWrapperType | 0 s |
|  | testEqualsNoQuotes\_Deprecated | 0 s |
|  | testEqualsRecordSeparator | 0 s |
|  | testWithCommentStartCRThrowsException | 0 s |
|  | testQuoteModeNoneShouldReturnMeaningfulExceptionMessage | 0 s |
|  | testDelimiterStringLineBreakLfThrowsException1 | 0 s |
|  | testQuoteCharSameAsDelimiterThrowsException | 0 s |
|  | testPrintWithoutQuotes | 0 s |
|  | testWithDelimiterLFThrowsException | 0 s |
|  | testEqualsLeftNoQuoteRightQuote\_Deprecated | 0 s |
|  | testWithEscape | 0 s |
|  | testWithHeader | 0 s |
|  | testGetHeader | 0 s |
|  | testEqualsLeftNoQuoteRightQuote | 0 s |
|  | testFormatToString | 0 s |
|  | testWithQuoteChar | 0 s |
|  | testEquals | 0 s |
|  | testWithEmptyEnum | 0 s |
|  | testFormat | 0 s |
|  | testWithRecordSeparatorCRLF | 0.001 s |
|  | testPrintWithEscapesEndWithCRLF | 0 s |
|  | testEqualsIgnoreEmptyLines\_Deprecated | 0 s |
|  | testEqualsOne | 0 s |
|  | testEqualsEscape\_Deprecated | 0 s |
|  | testDuplicateHeaderElementsFalse\_Deprecated | 0 s |
|  | testDuplicateHeaderElements | 0 s |
|  | testPrintWithQuotes | 0 s |
|  | testWithHeaderEnumNull | 0 s |
|  | testWithNullString | 0 s |
|  | testWithHeaderEnum | 0 s |
|  | testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType\_Deprecated | 0 s |
|  | testQuotePolicyNoneWithoutEscapeThrowsException\_Deprecated | 0 s |
|  | testEqualsWithNull | 0 s |

<a id="surefire--jiracsv196test"></a>

### JiraCsv196Test

|  |  |  |
| --- | --- | --- |
|  | testParseFourBytes | 0.002 s |
|  | testParseThreeBytes | 0 s |

<a id="surefire--csvparsertest"></a>

### CSVParserTest

|  |  |  |
| --- | --- | --- |
|  | testGetHeaderComment\_HeaderComment1 | 0 s |
|  | testGetHeaderComment\_HeaderComment2 | 0 s |
|  | testGetHeaderComment\_HeaderComment3 | 0 s |
|  | [testBackslashEscapingOld](#surefire--org.apache.commons.csv.csvparsertest.testbackslashescapingold) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld');) | 0 s |
| - | void org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld() throws java.io.IOException is @Disabled | - |
|  | testParseWithDelimiterWithQuote | 0 s |
|  | testCSV141CSVFormat\_DEFAULT | 0.001 s |
|  | [testStartWithEmptyLinesThenHeaders](#surefire--org.apache.commons.csv.csvparsertest.teststartwithemptylinesthenheaders) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders');) | 0 s |
| - | void org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders() throws java.lang.Exception is @Disabled | - |
|  | testExcelHeaderCountLessThanData | 0 s |
|  | testHeadersWithNullColumnName | 0.001 s |
|  | testMultipleIterators | 0 s |
|  | testGetRecordsMaxRows(long)[1] | 0.001 s |
|  | testGetRecordsMaxRows(long)[2] | 0 s |
|  | testGetRecordsMaxRows(long)[3] | 0 s |
|  | testGetRecordsMaxRows(long)[4] | 0 s |
|  | testGetRecordsMaxRows(long)[5] | 0 s |
|  | testGetRecordsMaxRows(long)[6] | 0 s |
|  | testGetRecordsMaxRows(long)[7] | 0 s |
|  | testHeaderComment | 0 s |
|  | testGetHeaderComment\_HeaderTrailerComment | 0 s |
|  | testDefaultFormat | 0 s |
|  | testCSV141CSVFormat\_INFORMIX\_UNLOAD\_CSV | 0.001 s |
|  | testEndOfFileBehaviorExcel | 0 s |
|  | testGetRecordPositionWithCRLF | 0 s |
|  | testHeaderMissing | 0 s |
|  | testGetHeaderComment\_NoComment1 | 0 s |
|  | testGetHeaderComment\_NoComment2 | 0 s |
|  | testGetHeaderComment\_NoComment3 | 0.001 s |
|  | testTrailingDelimiter | 0 s |
|  | testNotValueCSV | 0 s |
|  | testGetTrailerComment\_MultilineComment | 0 s |
|  | testParseWithDelimiterStringWithQuote | 0 s |
|  | testParsePathCharsetNullFormat | 0 s |
|  | testParseFileCharsetNullFormat | 0.001 s |
|  | [testBOM](#surefire--org.apache.commons.csv.csvparsertest.testbom) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testBOM');) | 0 s |
| - | CSV-107 | - |
|  | testFirstEndOfLineCrLf | 0 s |
|  | testProvidedHeaderAuto | 0 s |
|  | testGetRecordWithMultiLineValues | 0 s |
|  | testParseWithDelimiterStringWithEscape | 0 s |
|  | testParseNullStringFormat | 0 s |
|  | testParseInputStreamCharsetNullFormat | 0 s |
|  | testParseWithDelimiterWithEscape | 0 s |
|  | testSkipSetAltHeaders | 0 s |
|  | testGetRecordNumberWithCR | 0 s |
|  | testGetRecordNumberWithLF | 0 s |
|  | testCSV57 | 0 s |
|  | testClose | 0 s |
|  | testParse | 0.003 s |
|  | testTrim | 0 s |
|  | testGetLineNumberWithCR | 0 s |
|  | testGetLineNumberWithLF | 0 s |
|  | testParserUrlNullCharsetFormat | 0 s |
|  | testStreamMaxRows(long)[1] | 0.001 s |
|  | testStreamMaxRows(long)[2] | 0 s |
|  | testStreamMaxRows(long)[3] | 0 s |
|  | testStreamMaxRows(long)[4] | 0 s |
|  | testStreamMaxRows(long)[5] | 0 s |
|  | testStreamMaxRows(long)[6] | 0 s |
|  | testStreamMaxRows(long)[7] | 0 s |
|  | testForEach | 0 s |
|  | testGetOneLine | 0 s |
|  | testGetLineNumberWithCRLF | 0 s |
|  | testCarriageReturnLineFeedEndings | 0 s |
|  | [testMongoDbCsv](#surefire--org.apache.commons.csv.csvparsertest.testmongodbcsv) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testMongoDbCsv');) | 0 s |
| - | void org.apache.commons.csv.CSVParserTest.testMongoDbCsv() throws java.lang.Exception is @Disabled | - |
|  | testGetRecordNumberWithCRLF | 0 s |
|  | testParseUrlCharsetNullFormat | 0 s |
|  | testEmptyFile | 0 s |
|  | testGetHeaderNames | 0 s |
|  | testCarriageReturnEndings | 0 s |
|  | testParseWithQuoteThrowsException | 0 s |
|  | testGetLine | 0 s |
|  | testIgnoreCaseHeaderMapping | 0 s |
|  | testGetRecordPositionWithLF | 0 s |
|  | testGetOneLineOneParser | 0 s |
|  | testHeadersMissingException | 0 s |
|  | testBOMInputStreamParseWithReader | 0.002 s |
|  | testIteratorMaxRows(long)[1] | 0 s |
|  | testIteratorMaxRows(long)[2] | 0.001 s |
|  | testIteratorMaxRows(long)[3] | 0 s |
|  | testIteratorMaxRows(long)[4] | 0 s |
|  | testIteratorMaxRows(long)[5] | 0 s |
|  | testIteratorMaxRows(long)[6] | 0 s |
|  | testIteratorMaxRows(long)[7] | 0 s |
|  | testIteratorMaxRows(long)[8] | 0 s |
|  | testGetHeaderNamesReadOnly | 0 s |
|  | testCSV141CSVFormat\_INFORMIX\_UNLOAD | 0 s |
|  | testDuplicateHeadersAllowedByDefault | 0 s |
|  | testGetRecordsFromBrokenInputStream | 0 s |
|  | testProvidedHeader | 0 s |
|  | testBOMInputStreamParserWithInputStream | 0 s |
|  | testCSV141CSVFormat\_ORACLE | 0 s |
|  | testIteratorSequenceBreaking | 0.001 s |
|  | testSkipHeaderOverrideDuplicateHeaders | 0 s |
|  | testRepeatedHeadersAreReturnedInCSVRecordHeaderNames | 0 s |
|  | testGetRecordThreeBytesRead | 0 s |
|  | testEmptyLineBehaviorCSV | 0.001 s |
|  | testParseNullUrlCharsetFormat | 0 s |
|  | testInvalidFormat | 0 s |
|  | testCSV141CSVFormat\_POSTGRESQL\_CSV | 0 s |
|  | testBackslashEscaping2 | 0 s |
|  | testExcelFormat1 | 0 s |
|  | testExcelFormat2 | 0 s |
|  | testGetRecordFourBytesRead | 0.001 s |
|  | testDuplicateHeadersNotAllowed | 0 s |
|  | testEmptyString | 0 s |
|  | testBOMInputStreamParserWithReader | 0.001 s |
|  | testRoundtrip | 0 s |
|  | testNoHeaderMap | 0 s |
|  | testParseWithQuoteWithEscape | 0 s |
|  | testGetTrailerComment\_HeaderComment1 | 0 s |
|  | testGetTrailerComment\_HeaderComment2 | 0 s |
|  | testGetTrailerComment\_HeaderComment3 | 0 s |
|  | testGetHeaderMap | 0 s |
|  | testBackslashEscaping | 0 s |
|  | testThrowExceptionWithLineAndPosition | 0.001 s |
|  | testLineFeedEndings | 0 s |
|  | testGetTrailerComment\_HeaderTrailerComment1 | 0 s |
|  | testGetTrailerComment\_HeaderTrailerComment2 | 0 s |
|  | testGetTrailerComment\_HeaderTrailerComment3 | 0 s |
|  | testParseNullPathFormat | 0 s |
|  | testMappedButNotSetAsOutlook2007ContactExport | 0 s |
|  | testSkipSetHeader | 0 s |
|  | testHeaderMissingWithNull | 0 s |
|  | testIgnoreEmptyLines | 0 s |
|  | testCSV235 | 0 s |
|  | testEndOfFileBehaviorCSV | 0 s |
|  | testNewCSVParserNullReaderFormat | 0 s |
|  | testEmptyLineBehaviorExcel | 0 s |
|  | testParseStringNullFormat | 0 s |
|  | testHeader | 0.001 s |
|  | testGetRecords | 0 s |
|  | testHeadersMissing | 0 s |
|  | testCSV141RFC4180 | 0 s |
|  | testFirstEndOfLineCr | 0 s |
|  | testFirstEndOfLineLf | 0 s |
|  | testEmptyFileHeaderParsing | 0 s |
|  | testStream | 0 s |
|  | testCSV141Excel | 0.001 s |
|  | testIterator | 0 s |
|  | testHeadersMissingOneColumnException | 0 s |
|  | testParseNullFileFormat | 0 s |
|  | testSkipAutoHeader | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[1] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[2] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[3] | 0.001 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[4] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[5] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[6] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[7] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[8] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[9] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[10] | 0.001 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[11] | 0 s |
|  | testParsingPrintedEmptyFirstColumn(Predefined)[12] | 0 s |
|  | testNewCSVParserReaderNullFormat | 0 s |

<a id="surefire--jiracsv265test"></a>

### JiraCsv265Test

|  |  |  |
| --- | --- | --- |
|  | testCharacterPositionWithCommentsSpanningMultipleLines | 0 s |
|  | testCharacterPositionWithComments | 0 s |

<a id="surefire--jiracsv93test"></a>

### JiraCsv93Test

|  |  |  |
| --- | --- | --- |
|  | testWithSetNullStringNULL | 0 s |
|  | testWithNotSetNullString | 0 s |
|  | testWithSetNullStringEmptyString | 0 s |

<a id="surefire--jiracsv253test"></a>

### JiraCsv253Test

|  |  |  |
| --- | --- | --- |
|  | testHandleAbsentValues | 0 s |

<a id="surefire--jiracsv288test"></a>

### JiraCsv288Test

|  |  |  |
| --- | --- | --- |
|  | testParseWithTwoCharDelimiter1 | 0 s |
|  | testParseWithTwoCharDelimiter2 | 0 s |
|  | testParseWithTwoCharDelimiter3 | 0 s |
|  | testParseWithTwoCharDelimiter4 | 0 s |
|  | testParseWithABADelimiter | 0 s |
|  | testParseWithDoublePipeDelimiterQuoted | 0 s |
|  | testParseWithTwoCharDelimiterEndsWithDelimiter | 0 s |
|  | testParseWithDoublePipeDelimiterDoubleCharValue | 0 s |
|  | testParseWithDoublePipeDelimiterEndsWithDelimiter | 0 s |
|  | testParseWithTriplePipeDelimiter | 0 s |
|  | testParseWithSinglePipeDelimiterEndsWithDelimiter | 0 s |
|  | testParseWithDoublePipeDelimiter | 0 s |

<a id="surefire--csvprintertest"></a>

### CSVPrinterTest

|  |  |  |
| --- | --- | --- |
|  | testPrintRecordsWithEmptyVector | 0.003 s |
|  | testExcelPrintAllIterableOfArraysWithFirstEmptyValue2 | 0.001 s |
|  | testPrintReaderWithoutQuoteToWriter | 0.005 s |
|  | testEolQuoted | 0 s |
|  | testMongoDbTsvBasic | 0 s |
|  | testHeaderCommentTdf | 0.006 s |
|  | testExcelPrintAllArrayOfArraysWithFirstEmptyValue2 | 0.001 s |
|  | testDelimeterQuoteNone | 0 s |
|  | [testRandomMongoDbCsv](#surefire--org.apache.commons.csv.csvprintertest.testrandommongodbcsv) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv() throws java.lang.Exception is @Disabled | - |
|  | testPrintRecordStream | 0.006 s |
|  | testHeaderNotSet | 0 s |
|  | testPostgreSqlNullStringDefaultCsv | 0 s |
|  | testRandomExcel | 0.276 s |
|  | testRandomMySql | 0.228 s |
|  | testExcelPrintAllArrayOfLists | 0 s |
|  | testMongoDbCsvBasic | 0.001 s |
|  | testPrintOnePositiveInteger | 0 s |
|  | testPrint | 0 s |
|  | testJdbcPrinterWithResultSetHeader(long)[1] | 0.171 s |
|  | testJdbcPrinterWithResultSetHeader(long)[2] | 0.003 s |
|  | testJdbcPrinterWithResultSetHeader(long)[3] | 0.003 s |
|  | testJdbcPrinterWithResultSetHeader(long)[4] | 0.003 s |
|  | testJdbcPrinterWithResultSetHeader(long)[5] | 0.002 s |
|  | testNewCsvPrinterNullAppendableFormat | 0 s |
|  | testQuoteNonNumeric | 0 s |
|  | testPrintRecordsWithResultSetOneRow | 0.002 s |
|  | testMongoDbTsvTabInValue | 0 s |
|  | testCloseWithCsvFormatAutoFlushOff | 0.193 s |
|  | testJdbcPrinterWithResultSetMetaData(long)[1] | 0.005 s |
|  | testJdbcPrinterWithResultSetMetaData(long)[2] | 0.003 s |
|  | testJdbcPrinterWithResultSetMetaData(long)[3] | 0.003 s |
|  | testJdbcPrinterWithResultSetMetaData(long)[4] | 0.003 s |
|  | testJdbcPrinterWithResultSetMetaData(long)[5] | 0.002 s |
|  | testEolPlain | 0.001 s |
|  | testMongoDbTsvCommaInValue | 0 s |
|  | testMongoDbCsvCommaInValue | 0 s |
|  | testEscapeNull1 | 0.001 s |
|  | testEscapeNull2 | 0 s |
|  | testEscapeNull3 | 0 s |
|  | testEscapeNull4 | 0 s |
|  | testEscapeNull5 | 0 s |
|  | testPrintRecordsWithCSVRecord | 0.002 s |
|  | testPrinter1 | 0 s |
|  | testPrinter2 | 0 s |
|  | testPrinter3 | 0.001 s |
|  | testPrinter4 | 0 s |
|  | testPrinter5 | 0 s |
|  | testPrinter6 | 0.001 s |
|  | testPrinter7 | 0 s |
|  | testDelimiterPlain | 0 s |
|  | testJira135\_part1 | 0 s |
|  | [testJira135\_part2](#surefire--org.apache.commons.csv.csvprintertest.testjira135_part2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testJira135_part2');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testJira135\_part2() throws java.io.IOException is @Disabled | - |
|  | testJira135\_part3 | 0 s |
|  | testRandomPostgreSqlText | 0.247 s |
|  | testExcelPrintAllArrayOfArraysWithFirstSpaceValue1 | 0 s |
|  | testSingleQuoteQuoted | 0 s |
|  | testPrintRecordsWithObjectArray | 0.001 s |
|  | testDelimeterStringQuoteNone | 0 s |
|  | testTrimOffOneColumn | 0 s |
|  | testMongoDbCsvTabInValue | 0.001 s |
|  | testDontQuoteEuroFirstChar | 0 s |
|  | testTrailingDelimiterOnTwoColumns | 0 s |
|  | testQuoteAll | 0 s |
|  | testRandomTdf | 0.208 s |
|  | testPrintToFileWithCharsetUtf16Be | 0.007 s |
|  | [testPostgreSqlCsvTextOutput](#surefire--org.apache.commons.csv.csvprintertest.testpostgresqlcsvtextoutput) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput() throws java.io.IOException is @Disabled | - |
|  | testExcelPrintAllStreamOfArrays(long)[1] | 0.001 s |
|  | testExcelPrintAllStreamOfArrays(long)[2] | 0 s |
|  | testExcelPrintAllStreamOfArrays(long)[3] | 0 s |
|  | testExcelPrintAllStreamOfArrays(long)[4] | 0 s |
|  | testExcelPrintAllStreamOfArrays(long)[5] | 0 s |
|  | testPostgreSqlNullStringDefaultText | 0 s |
|  | testPrintToPathWithDefaultCharset | 0 s |
|  | [testPostgreSqlCsvNullOutput](#surefire--org.apache.commons.csv.csvprintertest.testpostgresqlcsvnulloutput) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput() throws java.io.IOException is @Disabled | - |
|  | testPrintCSVRecords(long)[1] | 0 s |
|  | testPrintCSVRecords(long)[2] | 0 s |
|  | testPrintCSVRecords(long)[3] | 0 s |
|  | testPrintCSVRecords(long)[4] | 0.001 s |
|  | testPrintCSVRecords(long)[5] | 0 s |
|  | testExcelPrintAllIterableOfLists | 0 s |
|  | testTrimOnOneColumn | 0 s |
|  | testDelimeterQuoted | 0 s |
|  | testSkipHeaderRecordFalse | 0 s |
|  | testExcelPrintAllArrayOfArraysWithFirstTabValue1 | 0 s |
|  | testPlainPlain | 0 s |
|  | testSingleLineComment | 0 s |
|  | testExcelPrintAllIterableOfArrays | 0 s |
|  | testNewCsvPrinterAppendableNullFormat | 0 s |
|  | testInvalidFormat | 0 s |
|  | [testRandomOracle](#surefire--org.apache.commons.csv.csvprintertest.testrandomoracle) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testRandomOracle');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testRandomOracle() throws java.lang.Exception is @Disabled | - |
|  | testMultiLineComment | 0 s |
|  | testJdbcPrinterWithFirstEmptyValue2 | 0.002 s |
|  | testExcelPrintAllArrayOfListsWithFirstEmptyValue2 | 0 s |
|  | testJdbcPrinterWithResultSet(long)[1] | 0.004 s |
|  | testJdbcPrinterWithResultSet(long)[2] | 0.004 s |
|  | testJdbcPrinterWithResultSet(long)[3] | 0.002 s |
|  | testJdbcPrinterWithResultSet(long)[4] | 0.004 s |
|  | testJdbcPrinterWithResultSet(long)[5] | 0.004 s |
|  | testJdbcPrinterWithResultSet(long)[6] | 0.004 s |
|  | testJdbcPrinterWithResultSet(long)[7] | 0.003 s |
|  | testQuoteCommaFirstChar | 0.001 s |
|  | testPlainQuoted | 0 s |
|  | testNotFlushable | 0 s |
|  | testRandomRfc4180 | 0.241 s |
|  | testExcelPrintAllArrayOfArrays | 0 s |
|  | testDelimeterStringQuoted | 0 s |
|  | testJdbcPrinter | 0.005 s |
|  | testEscapeBackslash1 | 0.001 s |
|  | testEscapeBackslash2 | 0 s |
|  | testEscapeBackslash3 | 0 s |
|  | testEscapeBackslash4 | 0 s |
|  | testEscapeBackslash5 | 0 s |
|  | testSkipHeaderRecordTrue | 0.001 s |
|  | testRandomDefault | 0.202 s |
|  | testCloseBackwardCompatibility | 0.001 s |
|  | testCloseWithCsvFormatAutoFlushOn | 0.001 s |
|  | testTrimOnTwoColumns | 0 s |
|  | testDelimiterEscaped | 0.001 s |
|  | testCSV135 | 0 s |
|  | testCSV259 | 0 s |
|  | testEquals | 0 s |
|  | testHeader | 0 s |
|  | testParseCustomNullValues | 0 s |
|  | testMongoDbCsvDoubleQuoteInValue | 0 s |
|  | testPrintCustomNullValues | 0 s |
|  | testEolEscaped | 0 s |
|  | testPrintCSVParser | 0 s |
|  | testCRComment | 0 s |
|  | testPrintNullValues | 0.001 s |
|  | [testRandomPostgreSqlCsv](#surefire--org.apache.commons.csv.csvprintertest.testrandompostgresqlcsv) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv() throws java.lang.Exception is @Disabled | - |
|  | testPrintCSVRecord | 0 s |
|  | testHeaderCommentExcel | 0 s |
|  | testExcelPrinter1 | 0 s |
|  | testExcelPrinter2 | 0 s |
|  | testCloseWithFlushOn | 0 s |
|  | testMySqlNullOutput | 0 s |
|  | testPrintReaderWithoutQuoteToAppendable | 0 s |
|  | [testJira135All](#surefire--org.apache.commons.csv.csvprintertest.testjira135all) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testJira135All');) | 0 s |
| - | void org.apache.commons.csv.CSVPrinterTest.testJira135All() throws java.io.IOException is @Disabled | - |
|  | testMySqlNullStringDefault | 0 s |
|  | testPlainEscaped | 0.001 s |
|  | testPrintToFileWithDefaultCharset | 0 s |
|  | testDelimiterStringEscaped | 0.001 s |
|  | testCloseWithFlushOff | 0 s |
|  | testDisabledComment | 0 s |

<a id="surefire--userguidetest"></a>

### UserGuideTest

|  |  |  |
| --- | --- | --- |
|  | testBomFull | 0.008 s |
|  | testBomUtil | 0.001 s |

<a id="surefire--jiracsv206test"></a>

### JiraCsv206Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv206MultipleCharacterDelimiter | 0 s |

<a id="surefire--csvrecordtest"></a>

### CSVRecordTest

|  |  |  |
| --- | --- | --- |
|  | testIsInconsistent | 0.001 s |
|  | testRemoveAndAddColumns | 0 s |
|  | testPutInMap | 0 s |
|  | testIsConsistent | 0 s |
|  | testSerialization | 0.004 s |
|  | testToMap | 0.001 s |
|  | testToString | 0 s |
|  | testDuplicateHeaderToMap | 0.001 s |
|  | testToListAdd | 0 s |
|  | testToListFor | 0.001 s |
|  | testToListSet | 0 s |
|  | testCSVRecordNULLValues | 0 s |
|  | testGetNullEnum | 0 s |
|  | testDuplicateHeaderGet | 0.001 s |
|  | testIsMapped | 0 s |
|  | testGetWithEnum | 0 s |
|  | testIsSetInt | 0 s |
|  | testGetStringInconsistentRecord | 0.001 s |
|  | testToMapWithShortRecord | 0 s |
|  | testGetStringNoHeader | 0 s |
|  | testToListForEach | 0 s |
|  | testGetUnmappedPositiveInt | 0 s |
|  | testIsSetString | 0 s |
|  | testGetUnmappedNegativeInt | 0 s |
|  | testGetUnmappedEnum | 0.001 s |
|  | testGetUnmappedName | 0 s |
|  | testGetInt | 0 s |
|  | testGetString | 0 s |
|  | testStream | 0 s |
|  | testIterator | 0 s |
|  | testToMapWithNoHeader | 0 s |

<a id="surefire--lexertest"></a>

### LexerTest

|  |  |  |
| --- | --- | --- |
|  | testNextToken4 | 0.013 s |
|  | testNextToken5 | 0.001 s |
|  | testNextToken6 | 0 s |
|  | testReadEscapeBackspace | 0 s |
|  | testEOFWithoutClosingQuote | 0.005 s |
|  | testTab | 0.001 s |
|  | testTrimTrailingSpacesZeroLength | 0.001 s |
|  | testSurroundingSpacesAreDeleted | 0.001 s |
|  | testEscapedControlCharacter2 | 0.001 s |
|  | testCommentsAndEmptyLines | 0.001 s |
|  | testCR | 0.001 s |
|  | testFF | 0.001 s |
|  | testLF | 0 s |
|  | testEscapedTab | 0 s |
|  | testIsMetaCharCommentStart | 0.001 s |
|  | testTrailingTextAfterQuote | 0.001 s |
|  | testComments | 0.001 s |
|  | testSurroundingTabsAreDeleted | 0 s |
|  | testEscapingAtEOF | 0 s |
|  | testEscapedMySqlNullValue | 0.001 s |
|  | testEscapedBackspace | 0 s |
|  | testBackslashWithEscaping | 0.002 s |
|  | testEscapedCharacter | 0 s |
|  | testBackslashWithoutEscaping | 0 s |
|  | testDelimiterIsWhitespace | 0.001 s |
|  | testIgnoreEmptyLines | 0.001 s |
|  | testReadEscapeTab | 0 s |
|  | testReadEscapeFF | 0.001 s |
|  | testEscapedControlCharacter | 0 s |
|  | testEscapedCR | 0 s |
|  | testEscapedFF | 0 s |
|  | testEscapedLF | 0 s |
|  | testBackspace | 0.001 s |

<a id="surefire--jiracsv264test"></a>

### JiraCsv264Test

|  |  |  |
| --- | --- | --- |
|  | testJiraCsv264 | 0.001 s |
|  | testJiraCsv264WithGapAllowEmpty | 0 s |
|  | testJiraCsv264WithGapDisallow | 0 s |

<a id="surefire--csvfileparsertest"></a>

### CSVFileParserTest

|  |  |  |
| --- | --- | --- |
|  | testCSVFile(File)[1] | 0.001 s |
|  | testCSVFile(File)[2] | 0 s |
|  | testCSVFile(File)[3] | 0 s |
|  | testCSVFile(File)[4] | 0 s |
|  | testCSVFile(File)[5] | 0 s |
|  | testCSVFile(File)[6] | 0.001 s |
|  | testCSVFile(File)[7] | 0 s |
|  | testCSVUrl(File)[1] | 0 s |
|  | testCSVUrl(File)[2] | 0 s |
|  | testCSVUrl(File)[3] | 0 s |
|  | testCSVUrl(File)[4] | 0 s |
|  | testCSVUrl(File)[5] | 0.001 s |
|  | testCSVUrl(File)[6] | 0 s |
|  | testCSVUrl(File)[7] | 0 s |

<a id="surefire--jiracsv290test"></a>

### JiraCsv290Test

|  |  |  |
| --- | --- | --- |
|  | testPostgresqlText | 0 s |
|  | testWriteThenRead | 0 s |
|  | testPostgresqlCsv | 0.001 s |

<a id="surefire--failure-details"></a>

## Failure Details

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

|  |  |
| --- | --- |
|  | testBackslashEscapingOld |
| - | skipped: void org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld() throws java.io.IOException is @Disabled |
|  | testStartWithEmptyLinesThenHeaders |
| - | skipped: void org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders() throws java.lang.Exception is @Disabled |
|  | testBOM |
| - | skipped: CSV-107 |
|  | testMongoDbCsv |
| - | skipped: void org.apache.commons.csv.CSVParserTest.testMongoDbCsv() throws java.lang.Exception is @Disabled |
|  | testRandomMongoDbCsv |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv() throws java.lang.Exception is @Disabled |
|  | testJira135\_part2 |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testJira135\_part2() throws java.io.IOException is @Disabled |
|  | testPostgreSqlCsvTextOutput |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput() throws java.io.IOException is @Disabled |
|  | testPostgreSqlCsvNullOutput |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput() throws java.io.IOException is @Disabled |
|  | testRandomOracle |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testRandomOracle() throws java.lang.Exception is @Disabled |
|  | testRandomPostgreSqlCsv |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv() throws java.lang.Exception is @Disabled |
|  | testJira135All |
| - | skipped: void org.apache.commons.csv.CSVPrinterTest.testJira135All() throws java.io.IOException is @Disabled |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/rat-report.html -->

<!-- page_index: 11 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

# Rat (Release Audit Tool) results

The following document contains the results of [Rat (Release Audit Tool)](https://creadur.apache.org/rat/apache-rat-plugin/).

```

*****************************************************
Summary
-------
Generated at: 2025-09-29T06:59:14-04:00

Notes: 4
Binaries: 4
Archives: 1
Standards: 86

Apache Licensed: 86
Generated Documents: 0

JavaDocs are generated, thus a license header is optional.
Generated files do not require license headers.

0 Unknown Licenses

Archives:

 + src/test/resources/org/apache/commons/csv/perf/worldcitiespop.txt.gz
 
*****************************************************
  Files with Apache License headers will be marked AL
  Binary files (which do not require any license headers) will be marked B
  Compressed archives will be marked A
  Notices, licenses etc. will be marked N
  AL    CODE_OF_CONDUCT.md
  AL    benchmark-prereq.sh
  N     RELEASE-NOTES.txt
  AL    pom.xml
  AL    BENCHMARK.md
  AL    README.md
  N     NOTICE.txt
  AL    CONTRIBUTING.md
  AL    .github/GH-ROBOTS.txt
  AL    .github/workflows/maven.yml
  AL    .github/workflows/codeql-analysis.yml
  AL    .github/workflows/dependency-review.yml
  AL    .github/workflows/scorecards-analysis.yml
  AL    .github/pull_request_template.md
  AL    .github/dependabot.yml
  N     LICENSE.txt
  AL    SECURITY.md
  N     src/test/resources/org/apache/commons/csv/CSVFileParser/README.txt
  A     src/test/resources/org/apache/commons/csv/perf/worldcitiespop.txt.gz
  AL    src/test/java/org/apache/commons/csv/CSVFileParserTest.java
  AL    src/test/java/org/apache/commons/csv/ExtendedBufferedReaderTest.java
  AL    src/test/java/org/apache/commons/csv/PerformanceTest.java
  AL    src/test/java/org/apache/commons/csv/CSVRecordTest.java
  AL    src/test/java/org/apache/commons/csv/CSVBenchmark.java
  AL    src/test/java/org/apache/commons/csv/LexerTest.java
  AL    src/test/java/org/apache/commons/csv/Utils.java
  AL    src/test/java/org/apache/commons/csv/CSVFormatPredefinedTest.java
  AL    src/test/java/org/apache/commons/csv/JiraCsv196Test.java
  AL    src/test/java/org/apache/commons/csv/TokenTest.java
  AL    src/test/java/org/apache/commons/csv/CSVDuplicateHeaderTest.java
  AL    src/test/java/org/apache/commons/csv/CSVFormatTest.java
  AL    src/test/java/org/apache/commons/csv/CsvAssertions.java
  AL    src/test/java/org/apache/commons/csv/UserGuideTest.java
  AL    src/test/java/org/apache/commons/csv/JiraCsv318Test.java
  AL    src/test/java/org/apache/commons/csv/perf/PerformanceTest.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv263Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv257Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv290Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv203Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv167Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv154Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv247Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv198Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv265Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv264Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv213Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv148Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv149Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv93Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv150Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv248Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv249Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv254Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv288Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv253Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv211Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv271Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv206Test.java
  AL    src/test/java/org/apache/commons/csv/issues/JiraCsv294Test.java
  AL    src/test/java/org/apache/commons/csv/CSVParserTest.java
  AL    src/test/java/org/apache/commons/csv/CSVPrinterTest.java
  AL    src/changes/release-notes.vm
  AL    src/changes/changes.xml
  AL    src/assembly/src.xml
  AL    src/assembly/bin.xml
  AL    src/site/resources/spotbugs/spotbugs-exclude-filter.xml
  AL    src/site/resources/profile.jacoco
  B     src/site/resources/images/logo.png
  AL    src/site/resources/pmd/pmd-ruleset.xml
  AL    src/site/xdoc/index.xml
  AL    src/site/xdoc/mail-lists.xml
  AL    src/site/xdoc/download_csv.xml
  AL    src/site/xdoc/issue-tracking.xml
  AL    src/site/xdoc/user-guide.xml
  AL    src/site/xdoc/security.xml
  AL    src/site/site.xml
  AL    src/main/java/org/apache/commons/csv/CSVParser.java
  AL    src/main/java/org/apache/commons/csv/CSVPrinter.java
  AL    src/main/java/org/apache/commons/csv/CSVFormat.java
  AL    src/main/java/org/apache/commons/csv/ExtendedBufferedReader.java
  AL    src/main/java/org/apache/commons/csv/QuoteMode.java
  AL    src/main/java/org/apache/commons/csv/Lexer.java
  AL    src/main/java/org/apache/commons/csv/Token.java
  AL    src/main/java/org/apache/commons/csv/CSVException.java
  AL    src/main/java/org/apache/commons/csv/DuplicateHeaderMode.java
  AL    src/main/java/org/apache/commons/csv/package-info.java
  AL    src/main/java/org/apache/commons/csv/Constants.java
  AL    src/main/java/org/apache/commons/csv/CSVRecord.java
  AL    src/main/javadoc/overview.html
  AL    src/conf/checkstyle/checkstyle-suppressions.xml
  AL    src/conf/checkstyle/checkstyle.xml
  AL    src/conf/checkstyle/checkstyle-header.txt
  B     src/media/logo-large.xcf
  B     src/media/logo.xcf
  B     src/media/logo.png
 
*****************************************************
```

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/japicmp.html -->

<!-- page_index: 12 -->

# Apache Commons CSV

Comparing source compatibility of commons-csv-1.14.2-SNAPSHOT.jar against commons-csv-1.14.1.jar

|  |  |
| --- | --- |
| Old: | commons-csv-1.14.1.jar |
| New: | commons-csv-1.14.2-SNAPSHOT.jar |
| Created: | 2025-09-29T06:59:14.527-0400 |
| Access modifier filter: | PROTECTED |
| Only modifications: | true |
| Only binary incompatible modifications: | false |
| Ignore missing classes: | false |
| Includes: | all |
| Excludes: | n.a. |
| Semantic Versioning: | 0.0.1 |

Binary incompatible changes are marked with (!) while source incompatible changes are marked with (\*).

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/checkstyle.html -->

<!-- page_index: 13 -->

<a id="checkstyle--checkstyle-results"></a>

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 11.0.1 with /Users/garygregory/git/commons-csv/src/conf/checkstyle/checkstyle.xml ruleset.

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

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/cpd.html -->

<!-- page_index: 14 -->

<a id="cpd--cpd-results"></a>

# CPD Results

The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 7.17.0.

CPD found no problems in your source code.

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/pmd.html -->

<!-- page_index: 15 -->

<a id="pmd--pmd-results"></a>

# PMD Results

The following document contains the results of [PMD](https://pmd.github.io) 7.17.0.

PMD found no problems in your source code.

---

<a id="taglist"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/taglist.html -->

<!-- page_index: 16 -->

<a id="taglist--tag-list-report"></a>

# Tag List Report

The following document contains the listing of user tags found in the code. Below is the summary of the occurrences per tag.

| Tag Class | Total number of occurrences | Tag strings used by tag class |
| --- | --- | --- |
| [Needs Work](#taglist--tag_class_1) | 9 | TODO, FIXME, XXX |
| Notable Markers | 0 | NOTE, NOPMD, NOSONAR |

Each tag is detailed below:

<a id="taglist--needs-work"></a>

## Needs Work

Number of occurrences found in the code: 9

| org.apache.commons.csv.CSVParserTest | Line |
| --- | --- |
| this may lead to strange behavior, throw an exception if iterator() has already been called? | [1328](https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/CSVParserTest.html#L1328) |
| org.apache.commons.csv.CSVPrinter | Line |
| Is it a good idea to do this here instead of on the first call to a print method? It seems a pain to have to track whether the header has already been printed or not. | [112](https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/CSVPrinter.html#L112) |
| org.apache.commons.csv.Lexer | Line |
| escape handling needs more work | [470](https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L470) |
| is this correct? | [495](https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L495) |
| is this correct? Do tabs need to be escaped? | [496](https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L496) |
| is this correct? | [497](https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L497) |
| org.apache.commons.csv.LexerTest | Line |
| is this correct? Do we expect <esc>BACKSPACE to be unescaped? | [232](https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/LexerTest.html#L232) |
| is this correct? Do we expect <esc>FF to be unescaped? | [268](https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/LexerTest.html#L268) |
| is this correct? Do we expect <esc>TAB to be unescaped? | [290](https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/LexerTest.html#L290) |

---
