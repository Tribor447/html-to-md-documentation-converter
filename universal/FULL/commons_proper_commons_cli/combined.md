# Project Information

## Navigation

- Commons CLI
  - [About](#index)
  - [Release History](#changes)
  - [Sources](#scm)
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
    - [RAT Report](#rat-report)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [SpotBugs](#spotbugs)
    - [CPD](#cpd)
    - [PMD](#pmd)

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
as are various [project reports](#project-reports).

The Javadoc API documents are available online:

- [Javadoc latest](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
- [Javadoc archives](https://javadoc.io/doc/commons-cli/commons-cli/latest/index.html)

The [source repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-cli.git).

<a id="index--releases"></a>

# Releases

[Download](https://commons.apache.org/cli/download_cli.cgi) the latest version.
The [release notes](#changes) are also available.

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/cli/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-cli/mail-lists.html) act as the main support forum. The user list
is suitable for most library usage queries. The dev list is intended for the development discussion. Please
remember that the lists are shared between all commons components, so prefix your email subject by
`[cli]`.

Issues may be reported via the [ASF JIRA](https://commons.apache.org/proper/commons-cli/issue-tracking.html).

<a id="index--cli-2"></a>

# CLI 2?

Commons CLI 1.0 was formed from the merger of ideas and code from three different libraries -
Werken, Avalon and Optz. In dealing with the bugs and the feature requests a freshly designed and not
backwards compatible CLI 2 was created in 2004, but never finished or released.

The current plan is to continue to maintain the 1.x line. The CLI2 work may be found in the Commons Sandbox.

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/changes.html -->

<!-- page_index: 2 -->

<a id="changes--apache-commons-cli-release-notes"></a>

# Apache Commons CLI Release Notes

<a id="changes--release-history"></a>

## Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.11.0](#changes--a1.11.0) | 2025-11-08 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.10.0](#changes--a1.10.0) | 2025-07-30 | This is a feature and maintenance release. Java 8 or later is required. |
| [1.9.0](#changes--a1.9.0) | 2024-08-10 | This release contains new features and bug fixes and requires Java 8 or above. |
| [1.8.0](#changes--a1.8.0) | 2024-05-18 | This release contains new features and bug fixes and requires Java 8 or above. |
| [1.7.0](#changes--a1.7.0) | 2024-04-13 | This release contains new features and bug fixes and requires Java 8 or above. |
| [1.6.0](#changes--a1.6.0) | 2023-10-23 | This release contains new features and bug fixes and requires Java 8 or above. |
| [1.5.0](#changes--a1.5.0) | 2021-10-23 | This release contains new features and bug fixes and requires Java 7 or above. |
| [1.4](#changes--a1.4) | 2017-03-09 | This release contains new features and bug fixes and requires Java 5 or above. |
| [1.3.1](#changes--a1.3.1) | 2015-06-17 | This release contains bug fixes and requires Java 5 or above. |
| [1.3](#changes--a1.3) | 2015-05-09 | This release contains new features and bug fixes and requires Java 5 or above.. |
| [1.2](#changes--a1.2) | 2009-03-19 | This release contains new features and bug fixes and requires Java 5 or above. |
| [1.1](#changes--a1.1) | 2007-07-08 | This is a maintenance release containing bug fixes. |
| [1.0](#changes--a1.0) | 2002-11-06 | Initial release |

<a id="changes--release-1.11.0-2025-11-08"></a>

## Release 1.11.0 – 2025-11-08

| Type | Changes | By |
| --- | --- | --- |
| Fix | Multiple trailing BREAK\_CHAR\_SET characters cause infinite loop in HelpFormatter. Fixes [CLI-351](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-351). Thanks to Damien Carbonne, Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix issue with groups not being reported in help output. #411. Fixes [CLI-351](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-351). Thanks to Damien Carbonne, Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CommandLine.getOptionCount() to measure option repetition #396. Thanks to David Larochette, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 85 to 91 #393. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.20.0 to 2.21.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.10.0-2025-07-30"></a>

## Release 1.10.0 – 2025-07-30

| Type | Changes | By |
| --- | --- | --- |
| Fix | Deprecate CommandLine.Builder() in favor of CommandLine.builder(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate DeprecatedAttributes.Builder() in favor of DeprecatedAttributes.builder(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Refactor default parser test #294. Thanks to Dávid Szigecsán. | [ggregory](#team--ggregory) |
| Fix | Port to JUnit 5. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Generics for Converter should use Exception not Throwable. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Pick up maven-antrun-plugin version from parent POM org.apache:apache. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Javadoc is missing its Overview page. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Get mockito version from parent pom (#351). Thanks to Arnout Engelen. | [ggregory](#team--ggregory) |
| Fix | Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate PatternOptionBuilder.PatternOptionBuilder(). Thanks to Arnout Engelen. | [ggregory](#team--ggregory) |
| Fix | HelpFormatter infinite loop with 0 width input. Fixes [CLI-341](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-341). Thanks to Ruiqi Dong, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail faster with a more precise NullPointerException: Option.processValue() throws NullPointerException when passed null value with value separator configured. Fixes [CLI-349](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-349). Thanks to Leo Fernandes, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail faster with a more precise NullPointerException: DefaultParser.parse() throws NullPointerException when options parameter is null. Fixes [CLI-344](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-344). Thanks to Ruiqi Dong, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Options.addOptionGroup(OptionGroup) does not remove required options from requiredOpts list. Fixes [CLI-347](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-347). Thanks to Ruiqi Dong, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | org.apache.commons.cli.Option.Builder.get() should throw IllegalStateException instead of IllegalArgumentException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | org.apache.commons.cli.Option.processValue(String) should throw IllegalStateException instead of IllegalArgumentException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | org.apache.commons.cli.OptionBuilder.create() should throw IllegalStateException instead of IllegalArgumentException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Help formatter extension in the new package #314. Fixes [CLI-339](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-339). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | CommandLine.Builder implements Supplier<CommandLine>. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | DefaultParser.Builder implements Supplier<DefaultParser>. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add CommandLine.getParsedOptionValues() #334. Fixes [CLI-340](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-340). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | org.apache.commons.cli.Option.Builder implements Supplier<Option>. Fixes [CLI-333](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-333). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add new options for parsing: ignore and skip. Thanks to Tamás Cservenák. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 72 to 85 #302, #304, #310, #315, #320, #327, #371. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | [test] Bump commons-io:commons-io from 2.16.1 to 2.20.0 #309, #337. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | [test] Bump org.apache.commons:commons-text from 1.12.0 to 1.14.0 #344. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Update site documentation to https://maven.apache.org/xsd/xdoc-2.0.xsd. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.9.0-2024-08-10"></a>

## Release 1.9.0 – 2024-08-10

| Type | Changes | By |
| --- | --- | --- |
| Add | Add OptionGroup.isSelected(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | You can now extend HelpFormatter.Builder. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add 'since' attribute to Option to track when an Option was introduced #292 Thanks to Claude Warren. | [ggregory](#team--ggregory) |
| Fix | Fix Javadoc pathing #280. Fixes [CLI-334](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-334). Thanks to Eric Pugh. | [ggregory](#team--ggregory) |
| Fix | Updated properties documentation #285. Fixes [CLI-335](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-335). Thanks to Claude Warren. | [ggregory](#team--ggregory) |
| Fix | Deprecation not always reported #284. Fixes [CLI-336](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-336). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Replace internal StringBuffer with StringBuilder. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 70 to 72 #283. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.8.0-2024-05-18"></a>

## Release 1.8.0 – 2024-05-18

| Type | Changes | By |
| --- | --- | --- |
| Add | Add optional HelpFormatter Function to document Deprecated options #271. Fixes [CLI-332](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-332). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add PMD check to default Maven goal. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Handle reporting of deprecated options when parameters are not String type. #270. Fixes [CLI-331](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-331). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Avoid throwing NullPointerException when calling CommandLineParser will null array elements. Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Cleanup deprecation issues #272. Thanks to Claude Warren. | [ggregory](#team--ggregory) |
| Fix | Fix PMD UnnecessaryFullyQualifiedName issues. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 69 to 70. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.7.0-2024-04-13"></a>

## Release 1.7.0 – 2024-04-13

| Type | Changes | By |
| --- | --- | --- |
| Fix | Inconsistent behavior in key/value pairs (Java property style). Fixes [CLI-312](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-312). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Avoid NullPointerException in Util.stripLeadingAndTrailingQuotes(String). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Awkward behavior of Option.builder() for multiple optional args. Fixes [CLI-320](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-320). Thanks to Paul King, Claude Warren. | [ggregory](#team--ggregory) |
| Fix | Properties from multiple arguments with value separator. #237. Fixes [CLI-325](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-325). Thanks to Claude Warren. | [ggregory](#team--ggregory) |
| Fix | Fix for expected textual date values. #244. Fixes [CLI-327](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-327). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Option.Builder.option("") should throw IllegalArgumentException instead of ArrayIndexOutOfBoundsException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Avoid NullPointerException in CommandLine.getOptionValues(Option|String). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add and use a Converter interface and implementations without using BeanUtils #216. Fixes [CLI-321](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-321). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add Maven property project.build.outputTimestamp for build reproducibility. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add '-' as an option char and implemented extensive tests #217. Fixes [CLI-322](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-322). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Make adding OptionGroups and Options to existing Options easier #230. Fixes [CLI-324](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-324). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Added Supplier<T> defaults for getParsedOptionValue #229. Fixes [CLI-323](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-323). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Make Option.getKey() public #239. Fixes [CLI-326](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-326). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add builder factory CommandLine#builder(). Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Support "Deprecated" CLI Options #252. Fixes [CLI-329](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-329). Thanks to Eric Pugh, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 64 to 69 #256. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update the tests to JUnit 5 #238. Thanks to Elric, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests commons-io:commons-io from 2.16.0 to 2.16.1 #258. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.6.0-2023-10-23"></a>

## Release 1.6.0 – 2023-10-23

| Type | Changes | By |
| --- | --- | --- |
| Update | Fix SpotBugs Error: Medium: Method intentionally throws RuntimeException. [org.apache.commons.cli.Option] At Option.java:[lines 417-423] THROWS\_METHOD\_THROWS\_RUNTIMEEXCEPTION Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Fix SpotBugs Error: Medium: Method intentionally throws RuntimeException. [org.apache.commons.cli.Option] At Option.java:[lines 446-450] THROWS\_METHOD\_THROWS\_RUNTIMEEXCEPTION Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Fix SpotBugs Error: Medium: Method intentionally throws RuntimeException. [org.apache.commons.cli.Option] At Option.java:[lines 474-478] THROWS\_METHOD\_THROWS\_RUNTIMEEXCEPTION Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Use EMPTY\_STRING\_ARRAY constant. #102. Thanks to Ken Dombeck. | [ggregory](#team--ggregory) |
| Update | Fix site links that are broken #155. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Update | Use Math.max() #111. Delete unused assignment #112. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | [StepSecurity] ci: Harden GitHub Actions #176. Thanks to step-security-bot, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Inconsistent date format in changes report. Fixes [CLI-318](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-318). Thanks to Alexander Veit, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix NPE in CommandLine.resolveOption(String). Fixes [CLI-283](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-283). Thanks to Dilraj Singh, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CommandLine.addOption(Option) should not allow a null Option. Fixes [CLI-283](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-283). Thanks to Dilraj Singh, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CommandLine.addArgs(String) should not allow a null String. Fixes [CLI-283](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-283). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Site docs: "Usage Scenarios" refers to deprecated methods. Fixes [CLI-303](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-303). Thanks to Julian Schilling, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | NullPointerException thrown by CommandLineParser.parse(). Fixes [CLI-317](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-317). Thanks to Philippe Bastiani, Sruteesh Kumar Paramata, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | StringIndexOutOfBoundsException thrown by CommandLineParser.parse(). Fixes [CLI-313](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-313). Thanks to Dominik Stadler, HUNG LU, Sruteesh Kumar Paramata. | [ggregory](#team--ggregory) |
| Update | Add github/codeql-action. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Java from 7 to 8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from 2.1.7 to 3.0.10 #97, #130, #132. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/checkout from 3 to 3.1.0 #133. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from 2 to 3.6.0 #136. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs from 4.5.3 to 4.7.3 #96, #107, #113, #125, #138. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.5.3.0 to 4.7.3.0 #98, #108, #115, #117, #126, #145. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 52 to 64 #100, #128, #151, #158. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-antrun-plugin from 3.0.0 to 3.1.0 #103. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-javadoc-plugin from 3.3.2 to 3.4.1 #105, #120. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-pmd-plugin from 3.16.0 to 3.19.0 #110, #124. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump jacoco-maven-plugin from 0.8.7 to 0.8.8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.1.2 to 3.2.0 #121. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump japicmp-maven-plugin from 0.15.4 to 0.16.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update JUnit 4 to 5 vintage. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.5.0-2021-10-23"></a>

## Release 1.5.0 – 2021-10-23

| Type | Changes | By |
| --- | --- | --- |
| Fix | Fix NPE in DefaultParser.isLongOption(String). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | @param or @return lines should end with a period in CommandLine.java. Fixes [CLI-279](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-279). Thanks to Krishna Mohan Rao Kandunoori. | [britter](#team--britter) |
| Fix | Replace deprecated FindBugs with SpotBugs. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Replace CLIRR with JApiCmp. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Option Javadocs grammar nits #55. Thanks to Elliotte Rusty Harold. | [ggregory](#team--ggregory) |
| Fix | Minor Improvements #57, #61. Thanks to Arturo Bernal, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Input "test" gets parsed as test, quotes die #58. Fixes [CLI-254](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-254). Thanks to stoty. | [ggregory](#team--ggregory) |
| Fix | Allow whitespace-only header and footer #26. Fixes [CLI-287](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-287). Thanks to MrQubo, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Accommodate toggling partial matching in DefaultParser. Fixes [CLI-217](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-217). Thanks to Rubin Simons. | [chtompki](#team--chtompki) |
| Add | Option parser type EXISTING\_FILE\_VALUE not check file existing. Fixes [CLI-274](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-274). Thanks to Béla Schaum. | [britter](#team--britter) |
| Add | CommandLine.getXXX and CommandLine.hasXXX should accept an Option as a parameter. Fixes [CLI-271](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-271). Thanks to Christoph Läubrich. | [britter](#team--britter) |
| Add | Adjust access-modifier of checkRequiredOptions() to protected. Fixes [CLI-276](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-276). Thanks to Jason Dillon. | [ggregory](#team--ggregory) |
| Add | TypeHandler should throw ParseException for an unsupported class. Fixes [CLI-282](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-282). Thanks to Alex Nordlund. | [ggregory](#team--ggregory) |
| Add | Added setter for Builder.option #33. Thanks to Waldemar Sojka, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add Option unit tests #76. Thanks to Waldemar Sojka, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update Java from version 5 to 7. Fixes [CLI-294](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-294). | [ggregory](#team--ggregory) |
| Update | Docs: Replace OptionBuilder in usage page #30. Thanks to Mincong Huang. | [ggregory](#team--ggregory) |
| Update | Remove deprecated sudo setting. #36. Thanks to dengliming. | [ggregory](#team--ggregory) |
| Update | Bump junit:junit from 4.12 to 4.13.2, #53, #60. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 48 to 52. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-pmd-plugin from 3.12.0 to 3.16.0, #44, #54, #67, #92. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/checkout from 2.3.1 to 3 #46, #72, #78, #93. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from v1.4.2 to v2 #50. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-antrun-plugin from 1.7 to 3.0.0 #43. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 2.15 to 3.1.2 #41. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump checkstyle to 9.3 #68, #86, #90. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from 2 to 2.1.7 #64, #65, #81. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons.animal-sniffer.version 1.19 -> 1.20. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-bundle-plugin 5.1.1 -> 5.1.2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump biz.aQute.bndlib.version 5.1.2 -> 6.0.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs from 4.4.1 to 4.5.3 #70, #88. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.4.1 to 4.5.3.0 #71, #85, #87. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-javadoc-plugin from 3.3.1 to 3.3.2, #91. Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.4-2017-03-09"></a>

## Release 1.4 – 2017-03-09

| Type | Changes | By |
| --- | --- | --- |
| Add | Introduce CommandLine.Builder. Fixes [CLI-269](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-269). | [rfscholte](#team--rfscholte) |
| Fix | Optional argument picking up next regular option as its argument. Fixes [CLI-265](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-265). Thanks to Martin Sandiford. | [britter](#team--britter) |
| Add | Add an addRequiredOption method to Options. Fixes [CLI-267](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-267). Thanks to Ricardo Ribeiro. | [britter](#team--britter) |
| Fix | HelpFormatter.setOptionComparator(null) doesn't display the values in inserted order. Fixes [CLI-266](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-266). Thanks to Ravi Teja. | [britter](#team--britter) |

<a id="changes--release-1.3.1-2015-06-17"></a>

## Release 1.3.1 – 2015-06-17

| Type | Changes | By |
| --- | --- | --- |
| Fix | LongOpt falsely detected as ambiguous. Fixes [CLI-252](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-252). Thanks to Simon Harrer. | [britter](#team--britter) |

<a id="changes--release-1.3-2015-05-09"></a>

## Release 1.3 – 2015-05-09

| Type | Changes | By |
| --- | --- | --- |
| Fix | Fixed broken Javadoc links on Introduction page. Fixes [CLI-248](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-248). | [djones](#team--djones) |
| Fix | Fixed code example in javadoc of "Option#Builder#valueSeparator(char)". Fixes [CLI-234](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-234). Thanks to Greg Thomas. | [tn](#team--tn) |
| Fix | Clarified behavior of "OptionValidator#validateOption(String)" in case of null input. Fixes [CLI-241](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-241). Thanks to Beluga Behr. | [tn](#team--tn) |
| Update | Small cleanup of Option class. Fixes [CLI-240](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-240). Thanks to Beluga Behr. | [tn](#team--tn) |
| Update | Removed DoubleCheckedLocking test from checkstyle configuration. Fixes [CLI-231](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-231). Thanks to Duncan Jones. | [tn](#team--tn) |
| Update | Options.getRequiredOptions() now returns an unmodifiable list. Fixes [CLI-230](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-230). | [tn](#team--tn) |
| Add | Added new fluent API to create Option instances via builder class Option.Builder. This replaces the now deprecated OptionBuilder. Fixes [CLI-224](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-224). Thanks to Duncan Jones, Brian Blount. | [tn](#team--tn) |
| Update | Clarify javadoc for CommandLine.getOptionValue() that the first specified argument will be returned. Fixes [CLI-218](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-218). Thanks to Sven. | [tn](#team--tn) |
| Add | Added new method Options.addOption(String, String). Fixes [CLI-214](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-214). Thanks to Alexandru Mocanu. | [tn](#team--tn) |
| Update | Changed unit tests to junit 4 annotation style. Fixes [CLI-227](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-227). Thanks to Duncan Jones. | [tn](#team--tn) |
| Fix | Default options will now work correctly with required options that are missing. Fixes [CLI-202](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-202). | [ebourg](#team--ebourg) |
| Fix | Default options will now work correctly together with option groups. Fixes [CLI-203](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-203). | [ebourg](#team--ebourg) |
| Update | The javadoc of OptionBuilder now states that the class is not thread-safe. Fixes [CLI-209](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-209). Thanks to Thomas Herre. | [ebourg](#team--ebourg) |
| Add | HelpFormatter now supports setting the displayed separator of long options. Fixes [CLI-169](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-169). Thanks to J. Lewis Muir. | [ebourg](#team--ebourg) |
| Update | Improve description of parameter "stopAtNonOption" in method CommandLine.parse(Options, String[], boolean). Fixes [CLI-197](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-197). Thanks to Anders Larsson. | [ebourg](#team--ebourg) |
| Fix | Passing default values for not defined options to a parser will now trigger a ParseException instead of a NullPointerException. Fixes [CLI-204](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-204). | [ebourg](#team--ebourg) |
| Fix | HelpFormatter.setArgName(String) now correctly sets the argument name. Fixes [CLI-205](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-205). | [ebourg](#team--ebourg) |
| Fix | Default properties provided as input to the Parser.parse() methods are now correctly processed. Fixes [CLI-201](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-201). | [ebourg](#team--ebourg) |
| Fix | CommandLine.getParsedOptionValue() now returns a String object if no option type has been explicitly set. Fixes [CLI-215](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-215). Thanks to Manuel Müller. | [ebourg](#team--ebourg) |
| Update | Fixed typo in javadoc of class CommandLine. Fixes [CLI-200](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-200). Thanks to Gerard Weatherby. | [ggregory](#team--ggregory) |
| Update | Source code now uses generic types instead of raw types where possible. Fixes [CLI-223](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-223). Thanks to Gerard Weatherby. | [ebourg](#team--ebourg) |
| Update | Corrected javadoc for return type of MissingOptionException.getMissingOptions(). Fixes [CLI-220](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-220). Thanks to Joe Casadonte. | [ebourg](#team--ebourg) |
| Fix | HelpFormatter now prints command-line options in the same order as they have been added. Fixes [CLI-212](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-212). Thanks to Per Cederberg. | [ebourg](#team--ebourg) |
| Fix | Standard help text now shows mandatory arguments also for the first option. Fixes [CLI-186](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-186). Thanks to Kristoff Kiefer. | [ebourg](#team--ebourg) |
| Fix | HelpFormatter does not strip anymore leading whitespace in the footer text. Fixes [CLI-207](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-207). Thanks to Uri Moszkowicz. | [ebourg](#team--ebourg) |
| Fix | Strip quotes contained in argument values only if there is exactly one at the beginning and one at the end. Fixes [CLI-185](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-185). Thanks to Einar M R Rosenvinge. | [ebourg](#team--ebourg) |
| Fix | Negative numerical arguments take precedence over numerical options (only supported by the new DefaultParser). Fixes [CLI-184](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-184). | [ebourg](#team--ebourg) |
| Fix | Fix possible StringIndexOutOfBoundsException in HelpFormatter. Fixes [CLI-193](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-193). Thanks to Travis McLeskey. | [ebourg](#team--ebourg) |
| Add | A new parser is available: DefaultParser. It combines the features of the GnuParser and the PosixParser. It also provides additional features like partial matching for the long options, and long options without separator (i.e like the JVM memory settings: -Xmx512m). This new parser deprecates the previous ones. Fixes [CLI-161,CLI-167,CLI-181](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-161,CLI-167,CLI-181). | [ebourg](#team--ebourg) |
| Fix | OptionGroups no longer throw an AlreadySelectedException when reused for several parsings. Fixes [CLI-183](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-183). | [ebourg](#team--ebourg) |
| Fix | OptionGroup now selects properly an option with no short name. Fixes [CLI-182](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-182). | [ebourg](#team--ebourg) |
| Add | PosixParser now supports partial long options (--ver instead of --version). Fixes [CLI-160](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-160). | [ebourg](#team--ebourg) |

<a id="changes--release-1.2-2009-03-19"></a>

## Release 1.2 – 2009-03-19

| Type | Changes | By |
| --- | --- | --- |
| Fix | OptionBuilder is now reseted if an IllegalArgumentException occurs in create(). Fixes [CLI-177](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-177). | [joehni](#team--joehni) |
| Remove | Ant build system removed. | [bayard](#team--bayard) |
| Fix | Incomplete usage documentation about Java property option. Fixes [CLI-154](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-154). | [ebourg](#team--ebourg) |
| Fix | TypeHandler prints messages to stderr. Fixes [CLI-170](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-170). | [bayard](#team--bayard) |
| Fix | Infinite loop in the wrapping code of HelpFormatter. Fixes [CLI-162](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-162). | [bayard](#team--bayard) |
| Fix | Fixing some minor javadoc issues. | [sgoeschl](#team--sgoeschl) |
| Fix | The number of arguments defined for an option specifies the arguments per occurrence of the option and not for all occurrences. This was a major regression in CLI 1.1 which prevented the use of repeated options. Fixes [CLI-137](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-137). | [ebourg](#team--ebourg) |
| Add | Added a getOptionProperties() method in the CommandLine class to retrieve easily the key/value pairs specified with options like -Dkey1=value1 -Dkey2=value2. | [ebourg](#team--ebourg) |
| Update | GnuParser now supports long options with an '=' sign (ie. --foo=bar and -foo=bar). Fixes [CLI-157](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-157). | [ebourg](#team--ebourg) |
| Fix | PosixParser no longer ignores unrecognized short options. Fixes [CLI-164](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-164). | [ebourg](#team--ebourg) |
| Fix | PosixParser no longer stops the bursting process of a token if stopAtNonOption is enabled and a non option character is encountered. Fixes [CLI-163](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-163). | [ebourg](#team--ebourg) |
| Fix | PosixParser no longer keeps processing the tokens after an unrecognized long option when stopAtNonOption is enabled. Fixes [CLI-165](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-165). | [ebourg](#team--ebourg) |
| Fix | Required options are properly checked if an Options instance is used twice to parse a command line. Fixes [CLI-156](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-156). | [ebourg](#team--ebourg) |
| Update | The ordering of options can be defined in help messages. Fixes [CLI-155](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-155). | [bayard](#team--bayard) |
| Fix | The line wrapping in HelpFormatter now works properly. This caused CLI-162, and thus there was a feature change for the HelpFormatter in that it is strict on width now rather than what seemed to be lenience before. Text without whitespace will be cut off to fit in the spacing, and an IllegalStateException will be thrown if it is impossible to output the information due to spacing constraints. Fixes [CLI-151](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-151). Thanks to Dan Armbrust. | [bayard](#team--bayard) |
| Fix | The message of MissingOptionException has been improved. Fixes [CLI-149](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-149). | [bayard](#team--bayard) |
| Update | The exceptions have been enhanced with methods to retrieve easily the related options. Fixes [CLI-86](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-86). | [ebourg](#team--ebourg) |
| Fix | Option.toString() now reports arguments properly. Fixes [CLI-141](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-141). Thanks to Henning Schmiedehausen, Bjorn Townsend. | [bayard](#team--bayard) |
| Update | The Parser class has been changed to be more easily extendable. Fixes [CLI-142](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-142). Thanks to Henning Schmiedehausen. | [bayard](#team--bayard) |
| Update | The following classes are now serializable: Option, OptionGroup, CommandLine and Options. Fixes [CLI-140](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-140). | [bayard](#team--bayard) |
| Remove | OptionValidator is no longer public, its methods were all private. | [ebourg](#team--ebourg) |

<a id="changes--release-1.1-2007-07-08"></a>

## Release 1.1 – 2007-07-08

| Type | Changes | By |
| --- | --- | --- |
| Fix | Wrong usage summary. Fixes [CLI-2](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-2). | - |
| Fix | Dependecy on commons-lang-2.0 but commons-lang-1.0 is obtained. Fixes [CLI-5](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-5). | - |
| Fix | Line separator as first char for helpformatter (footer) throws exception. Fixes [CLI-8](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-8). | - |
| Fix | CommandLine.getOptionValue() behaves contrary to docs. Fixes [CLI-13](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-13). | - |
| Fix | clone method in Option should use super.clone(). Fixes [CLI-21](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-21). | - |
| Fix | Passing properties in Parser does not work for options with a single argument. Fixes [CLI-23](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-23). | - |
| Fix | Only long options without short option seems to be noticed. Fixes [CLI-26](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-26). | - |
| Fix | Infinite Loop in Command-Line processing. Fixes [CLI-28](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-28). | - |
| Fix | Options should not be able to be added more than once. Fixes [CLI-29](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-29). | - |
| Fix | HelpFormatter doesn't sort options properly. Fixes [CLI-35](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-35). | - |
| Fix | HelpFormatter doesn't function correctly for options with only LongOpt. Fixes [CLI-38](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-38). | - |
| Fix | Document enhancement. Fixes [CLI-44](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-44). | - |
| Fix | Documentation errors. Fixes [CLI-45](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-45). | - |
| Fix | Parameter value "-something" misinterpreted as a parameter. Fixes [CLI-51](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-51). | - |
| Fix | clone() method doesn't fully clone contents. Fixes [CLI-56](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-56). | - |
| Fix | No Javadoc for HelpFormatter!. Fixes [CLI-59](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-59). | - |
| Fix | Parser breaks up command line parms into single characters. Fixes [CLI-65](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-65). | - |
| Fix | Missing arguments in HelpFormatter.renderOptions(..). Fixes [CLI-67](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-67). | - |
| Fix | Error parsing option arguments. Fixes [CLI-69](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-69). | - |
| Fix | A weakness of parser. Fixes [CLI-71](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-71). | - |
| Add | Setting description of a Option. Fixes [CLI-78](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-78). | - |
| Fix | CLI\_1\_BRANCH build.xml doesn't work. Fixes [CLI-129](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-129). | - |
| Fix | Remove the Commons Lang dependency. Fixes [CLI-130](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-130). | - |
| Fix | Options class returns options in random order. Fixes [CLI-131](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-131). | - |
| Fix | MissingOptionException should contain a useful error message. Fixes [CLI-132](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-132). | - |
| Fix | NullPointerException in Util.stripLeadingHyphens when passed a null argument. Fixes [CLI-133](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-133). | - |
| Fix | 1.1 is not backwards compatible because it adds methods to the CommandLineParser interface. Fixes [CLI-134](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-134). | - |
| Fix | Backwards compatibility between 1.1 and 1.0 broken due to Option.addValue removal. Fixes [CLI-135](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-135). | - |

<a id="changes--release-1.0-2002-11-06"></a>

## Release 1.0 – 2002-11-06

No changes in this release.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/scm.html -->

<!-- page_index: 3 -->

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

<!-- page_index: 4 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons CLI provides a simple API for presenting, processing, and validating a Command Line Interface. |
| [Summary](https://commons.apache.org/proper/commons-cli/summary.html) | This document lists other related information of this project |
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
|  | jstrachan | James Strachan | [jstrachan@apache.org](mailto:jstrachan@apache.org) | - | SpiritSoft, Inc. | - | - | - |
|  | bob | Bob McWhirter | [bob@werken.com](mailto:bob@werken.com) | - | Werken | - | contributed ideas and code from werken.opt | - |
|  | jkeyes | John Keyes | [jbjk@mac.com](mailto:jbjk@mac.com) | - | integral Source | - | contributed ideas and code from Optz | - |
|  | roxspring | Rob Oxspring | [roxspring@imapmail.org](mailto:roxspring@imapmail.org) | - | Indigo Stone | - | designed CLI2 | - |
|  | ebourg | Emmanuel Bourg | [ebourg@apache.org](mailto:ebourg@apache.org) | - | Ariane Software | - | - | - |
|  | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | - | - | - | - |
|  | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | - | - | - | - |
|  | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization | Roles |
| --- | --- | --- | --- | --- |
|  | Beluga Behr | - | - | - |
|  | Peter Donald | - | - | contributed ideas and code from Avalon Excalibur's cli package |
|  | Brian Egge | - | - | made the 1.1 release happen |
|  | Duncan Jones | - | - | supplied patches |
|  | Berin Loritsch | [bloritsch@apache.org](mailto:bloritsch@apache.org) | - | helped in the Avalon CLI merge |
|  | Peter Maddocks | [peter\_maddocks@hp.com](mailto:peter_maddocks@hp.com) | Hewlett-Packard | supplied patch |
|  | Alexandru Mocanu | - | - | supplied patch |
|  | Andrew Shirley | - | - | lots of fixes for 1.1 |
|  | Greg Thomas | - | - | - |
|  | Slawek Zachcial | - | - | unit tests |
|  | Rubin Simons | [rubin@raaftech.com](mailto:rubin@raaftech.com) | - | supplied patch |

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

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/project-reports.html -->

<!-- page_index: 7 -->

<a id="project-reports--generated-reports"></a>

# Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](https://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [Changes](#changes) | Changes report on releases of this project. |
| [JIRA Report](#jira-changes) | Report on Issues from the JIRA Issue Tracking System. |
| [Javadoc](https://commons.apache.org/proper/commons-cli/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-cli/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-cli/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire](#surefire) | Report on the test results of the project. |
| [RAT Report](#rat-report) | Report on compliance to license related source code policies |
| [JaCoCo](https://commons.apache.org/proper/commons-cli/jacoco/index.html) | JaCoCo Coverage Report. |
| [japicmp](#japicmp) | Comparing source compatibility of commons-cli-1.11.0.jar against commons-cli-1.10.0.jar |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [SpotBugs](#spotbugs) | Generates a source code report with the SpotBugs Library. |
| [CPD](#cpd) | Duplicate code detection. |
| [PMD](#pmd) | Verification of coding rules. |

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/jira-changes.html -->

<!-- page_index: 8 -->

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
<td><a href="https://issues.apache.org/jira/browse/CLI-327">CLI-327</a></td>
<td>CLI-1.x</td>
<td>Date processing tests fail on some systems</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-326">CLI-326</a></td>
<td>Options definition</td>
<td>Make options.getKey() public</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-254">CLI-254</a></td>
<td>-</td>
<td>"test" gets parsed as test, quotes die :-(</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-232">CLI-232</a></td>
<td>CLI-1.x</td>
<td>Download link gives HTTP/1.1 403 Forbidden</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-198">CLI-198</a></td>
<td>Documentation</td>
<td>Download links for CLI 1.2 binaries are broken</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-146">CLI-146</a></td>
<td>-</td>
<td>SVN repository link incorrect / related to TLP change</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-139">CLI-139</a></td>
<td>CLI-1.x, CLI-2.x</td>
<td>Broken Links on the Web-Site</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-128">CLI-128</a></td>
<td>-</td>
<td>Remove Commons-logging from CLI's pom.xml</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-337">CLI-337</a></td>
<td>Parser</td>
<td>Parse arguments in a single string</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-242">CLI-242</a></td>
<td>-</td>
<td>PATCH: Util Class Cleaning</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.11.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-351">CLI-351</a></td>
<td>Help formatter</td>
<td>Multiple traililng BREAK_CHAR_SET characters cause infinite loop in HelpFormatter</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-349">CLI-349</a></td>
<td>Options definition, Parser</td>
<td>DefaultParser.parse() throws NullPointerException when options parameter is null</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-347">CLI-347</a></td>
<td>-</td>
<td>Options.addOptionGroup() does not remove required options from requiredOpts list</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-344">CLI-344</a></td>
<td>Options definition</td>
<td>Option.processValue() throws NullPointerException when passed null value with value separator configured</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-341">CLI-341</a></td>
<td>Help formatter</td>
<td>HelpFormatter infinite loop with 0 width input </td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-340">CLI-340</a></td>
<td>CLI-1.x</td>
<td>Add CommandLine.getParsedOptionValues() </td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-339">CLI-339</a></td>
<td>Help formatter</td>
<td>Help formatter framework is hard to extend.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-335">CLI-335</a></td>
<td>Documentation</td>
<td>Defining Default Properties documentation has errors.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-336">CLI-336</a></td>
<td>CLI-1.x</td>
<td>Deprecation use not always reported.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.9.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-334">CLI-334</a></td>
<td>Documentation</td>
<td>Fix Javadoc pathing</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-331">CLI-331</a></td>
<td>CLI-1.x</td>
<td>Deprecated option usage is not detected if non string keys are used for resolution.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-332">CLI-332</a></td>
<td>Help formatter</td>
<td>Add optional HelpFormatter Function to document Deprecated options</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-322">CLI-322</a></td>
<td>Parser</td>
<td>Allow minus for kebab-case options</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-325">CLI-325</a></td>
<td>Parser</td>
<td>When properties are retrieve for an Option that has both multiple arguments and a value separator only the first is retrieved.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-320">CLI-320</a></td>
<td>-</td>
<td>Awkward behavior of Option.builder() for multiple optional args</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-312">CLI-312</a></td>
<td>Parser</td>
<td>Inconsistent behaviour in key/value pairs (Java property style)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-324">CLI-324</a></td>
<td>CLI-1.x</td>
<td>Make adding OptionGroups and Options to existing Options easier</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-323">CLI-323</a></td>
<td>CLI-1.x</td>
<td>Add methods to accept Supplier&lt;T&gt; for getParsedOptionValue</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-321">CLI-321</a></td>
<td>Parser</td>
<td>Add and use a Converter interface and implementations without using BeanUtils </td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-329">CLI-329</a></td>
<td>-</td>
<td>Support "Deprecated" CLI Options</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-318">CLI-318</a></td>
<td>Documentation</td>
<td>Inconsistent date format in changes report</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-317">CLI-317</a></td>
<td>Parser</td>
<td>NullPointerException thrown by CommandLineParser.parse()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-314">CLI-314</a></td>
<td>-</td>
<td>Release notes are missing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-313">CLI-313</a></td>
<td>Parser</td>
<td>StringIndexOutOfBoundsException thrown by CommandLineParser.parse() on invalid input</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-303">CLI-303</a></td>
<td>Documentation</td>
<td>Doc: "Usage Scenarios" refers to deprecated methods</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-283">CLI-283</a></td>
<td>CLI-2.x</td>
<td>Missing Null pointer checks in CommandLine.java</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-299">CLI-299</a></td>
<td>-</td>
<td>Add Automatic-Module-Name to MANIFEST.MF</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>avalon-1.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-104">CLI-104</a></td>
<td>-</td>
<td>[CLI] Avalon Excalibur CLI package with bugfixes</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-171">CLI-171</a></td>
<td>CLI-2.x, Documentation</td>
<td>Typo in ant documentation, more logical example code</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-159">CLI-159</a></td>
<td>CLI-2.x</td>
<td>The required property for the child groups of a group should be more consistent</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-158">CLI-158</a></td>
<td>CLI-2.x</td>
<td>deafult arguments only works if no arguments are submitted</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-150">CLI-150</a></td>
<td>CLI-2.x, Parser</td>
<td>Negative numbers mistaken for options</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-145">CLI-145</a></td>
<td>CLI-2.x</td>
<td>ArgumentBuilder.withMaximum causes parse errors: Unexpeced &lt;value&gt; while processing options</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-144">CLI-144</a></td>
<td>CLI-2.x</td>
<td>adding a FileValidator results in ClassCastException in parser.parseAndHelp(args)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-143">CLI-143</a></td>
<td>CLI-2.x</td>
<td>Put CLI 2.x into Maven repository</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-127">CLI-127</a></td>
<td>CLI-2.x</td>
<td>Date validation tests are locale dependent</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-123">CLI-123</a></td>
<td>CLI-2.x</td>
<td>the minimum and maximum constraints on a group do not take other groups into account</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-121">CLI-121</a></td>
<td>CLI-2.x</td>
<td>Tests fail under 1.6 + error at end that may or may not be related</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-74">CLI-74</a></td>
<td>CLI-2.x</td>
<td>Prefix ignored with DefaultOption</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-72">CLI-72</a></td>
<td>CLI-2.x</td>
<td>support anonymous arguments explicity</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-64">CLI-64</a></td>
<td>CLI-2.x</td>
<td>[cli][PATCH] cli2.commandline.Parser.parseAndHelp need not throw IOException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-63">CLI-63</a></td>
<td>CLI-2.x</td>
<td>[cli] parser confuses values with similar options</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-62">CLI-62</a></td>
<td>CLI-2.x</td>
<td>Error parsing options a-la Java property option</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-61">CLI-61</a></td>
<td>CLI-2.x</td>
<td>[cli] argument defaults prevent commandline usage.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-55">CLI-55</a></td>
<td>CLI-2.x</td>
<td>[cli] PatternOptionBuilder does not support required Options</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-52">CLI-52</a></td>
<td>CLI-2.x</td>
<td>Add support for stuff like [target [target2 [target3] ...]]</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-50">CLI-50</a></td>
<td>CLI-2.x</td>
<td>[cli] TestHelpFormatter.testAutomaticUsage unit test failure</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-46">CLI-46</a></td>
<td>CLI-2.x</td>
<td>java.lang.StringIndexOutOfBoundsException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-42">CLI-42</a></td>
<td>CLI-2.x</td>
<td>[PATCH][CLI] Remove dependency on commons-logging</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-41">CLI-41</a></td>
<td>CLI-2.x, Help formatter</td>
<td>HelpFormatter shouldn't throw IOException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-40">CLI-40</a></td>
<td>CLI-2.x, Validation</td>
<td>DateValidatorTest &amp; FileValidatorTest problems</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-32">CLI-32</a></td>
<td>CLI-2.x</td>
<td>[cli] ant test needs resources copied.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-31">CLI-31</a></td>
<td>CLI-2.x</td>
<td>readme lists deprecate maven goal and old maven URL</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-30">CLI-30</a></td>
<td>CLI-2.x</td>
<td>[cli] Really strange parsing behaviour</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-25">CLI-25</a></td>
<td>CLI-2.x</td>
<td>[PATCH] [CLI] Default Values for Arguments at definition stage</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-20">CLI-20</a></td>
<td>CLI-2.x</td>
<td>MissingArgumentException: no argument for &lt;option&gt; is thrown when the option's parameter equals to an existing option.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-19">CLI-19</a></td>
<td>CLI-2.x</td>
<td>[cli] Broken link report (13 404s)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-17">CLI-17</a></td>
<td>CLI-2.x</td>
<td>Interrogation using switch statement</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-12">CLI-12</a></td>
<td>CLI-2.x</td>
<td>[cli] Not handling property=value followed by 'remaining' args</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-10">CLI-10</a></td>
<td>CLI-2.x</td>
<td>[cli] testNewMessage1Param fails</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-7">CLI-7</a></td>
<td>CLI-2.x</td>
<td>[cli][PATCH] Javadoc warning</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-4">CLI-4</a></td>
<td>CLI-2.x, Validation</td>
<td>Mispelled functions in DateValidator</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-3">CLI-3</a></td>
<td>CLI-2.x</td>
<td>[cli] CLI2 Group Parser skips arguments</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-126">CLI-126</a></td>
<td>CLI-2.x</td>
<td>CLI2 should support multiple property args on command line</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-124">CLI-124</a></td>
<td>CLI-2.x, Help formatter</td>
<td>HelpFormatter should be more cunning when deciding if a Group is Optional and therefore square-bracketing it</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-114">CLI-114</a></td>
<td>CLI-2.x</td>
<td>Multiple Option Occurrences</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-112">CLI-112</a></td>
<td>CLI-2.x</td>
<td>Defaults supplied at interrogation stage</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-108">CLI-108</a></td>
<td>CLI-2.x</td>
<td>the ability to add validate to options that spanned multiple options</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-106">CLI-106</a></td>
<td>CLI-2.x</td>
<td>CommandLine.hasOption type method that takes argument name</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-105">CLI-105</a></td>
<td>CLI-2.x</td>
<td>[cli] Options.getOptions() should return options in the order they were insterted</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-101">CLI-101</a></td>
<td>CLI-2.x</td>
<td>the ability to have long options that only use one hyphen</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-100">CLI-100</a></td>
<td>CLI-2.x</td>
<td>Default Values at Definition Stage</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-99">CLI-99</a></td>
<td>CLI-2.x</td>
<td>[cli] separate definition and values</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-98">CLI-98</a></td>
<td>CLI-2.x</td>
<td>Javadoc crosslinking</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-97">CLI-97</a></td>
<td>CLI-2.x</td>
<td>[patch] small error text patch</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-96">CLI-96</a></td>
<td>CLI-2.x</td>
<td>[cli][PATCH] HelpWriter.printWrapped() should have public access</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-91">CLI-91</a></td>
<td>CLI-2.x</td>
<td>[cli] distinction between required arguments in help formatter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-89">CLI-89</a></td>
<td>CLI-2.x</td>
<td>All arguments should have ConsumeRemaining behaviour</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-83">CLI-83</a></td>
<td>CLI-2.x</td>
<td>OptionBuilder only has static methods, yet many return an OptionBuilder instance</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-80">CLI-80</a></td>
<td>CLI-2.x</td>
<td>[cli] support validation for one/many values</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-76">CLI-76</a></td>
<td>CLI-2.x</td>
<td>auto usage/help issues</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-153">CLI-153</a></td>
<td>CLI-2.x</td>
<td>Add svn:eol-style=native</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-308">CLI-308</a></td>
<td>Documentation</td>
<td>Website has very out of date usage (site generation issue)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-282">CLI-282</a></td>
<td>-</td>
<td>TypeHandler should throw ParseException for an unsupported class</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-274">CLI-274</a></td>
<td>Parser</td>
<td>Option parser type EXISTING_FILE_VALUE not check file existing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-294">CLI-294</a></td>
<td>-</td>
<td>Update Java from version 5 to 7</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-279">CLI-279</a></td>
<td>-</td>
<td>@param or @return lines should end with a period in CommandLine.java</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-277">CLI-277</a></td>
<td>-</td>
<td>Add generics to TypeHandler</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-276">CLI-276</a></td>
<td>CLI-1.x</td>
<td>Adjust access-modifier of checkRequiredOptions() to protected</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/CLI-271">CLI-271</a></td>
<td>CLI-1.x</td>
<td>CommandLine.getXXX and CommandLine.hasXXX should accept an Option as a parameter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/surefire.html -->

<!-- page_index: 9 -->

<a id="surefire--surefire-report"></a>

# Surefire Report

<a id="surefire--summary"></a>

## Summary

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 977 | 0 | 0 | 61 | 93.8% | 0.754 s |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

<a id="surefire--package-list"></a>

## Package List

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Package | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.cli.example](#surefire--org.apache.commons.cli.example) | 13 | 0 | 0 | 0 | 100% | 0.022 s |
| [org.apache.commons.cli](#surefire--org.apache.commons.cli) | 809 | 0 | 0 | 61 | 92.5% | 0.698 s |
| [org.apache.commons.cli.help](#surefire--org.apache.commons.cli.help) | 118 | 0 | 0 | 0 | 100% | 0.025 s |
| [org.apache.commons.cli.bug](#surefire--org.apache.commons.cli.bug) | 37 | 0 | 0 | 0 | 100% | 0.009 s |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

<a id="surefire--org.apache.commons.cli.example"></a>

### org.apache.commons.cli.example

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [AptHelpAppendableTest](#surefire--org.apache.commons.cli.example.apthelpappendabletest) | 7 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [XhtmlHelpAppendableTest](#surefire--org.apache.commons.cli.example.xhtmlhelpappendabletest) | 6 | 0 | 0 | 0 | 100% | 0.020 s |

<a id="surefire--org.apache.commons.cli"></a>

### org.apache.commons.cli

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [ApplicationTest](#surefire--org.apache.commons.cli.applicationtest) | 5 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [OptionCountTest](#surefire--org.apache.commons.cli.optioncounttest) | 5 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [UnrecognizedOptionExceptionTest](#surefire--org.apache.commons.cli.unrecognizedoptionexceptiontest) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [CommandLineTest](#surefire--org.apache.commons.cli.commandlinetest) | 138 | 0 | 0 | 0 | 100% | 0.116 s |
|  | [AlreadySelectedExceptionTest](#surefire--org.apache.commons.cli.alreadyselectedexceptiontest) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [ParseExceptionTest](#surefire--org.apache.commons.cli.parseexceptiontest) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TypeHandlerTest](#surefire--org.apache.commons.cli.typehandlertest) | 63 | 0 | 0 | 0 | 100% | 0.027 s |
|  | [SolrCliTest](#surefire--org.apache.commons.cli.solrclitest) | 1 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [PosixParserTest](#surefire--org.apache.commons.cli.posixparsertest) | 67 | 0 | 0 | 10 | 85.1% | 0.008 s |
|  | [ValueTest](#surefire--org.apache.commons.cli.valuetest) | 40 | 0 | 0 | 0 | 100% | 0.010 s |
|  | [OptionValidatorTest](#surefire--org.apache.commons.cli.optionvalidatortest) | 115 | 0 | 0 | 0 | 100% | 0.024 s |
|  | [OptionTest](#surefire--org.apache.commons.cli.optiontest) | 23 | 0 | 0 | 0 | 100% | 0.008 s |
|  | [PatternOptionBuilderTest](#surefire--org.apache.commons.cli.patternoptionbuildertest) | 10 | 0 | 0 | 0 | 100% | 0.067 s |
|  | [HelpFormatterTest](#surefire--org.apache.commons.cli.helpformattertest) | 44 | 0 | 0 | 0 | 100% | 0.278 s |
|  | [UtilTest](#surefire--org.apache.commons.cli.utiltest) | 2 | 0 | 0 | 0 | 100% | 0.020 s |
|  | [DefaultParserTest](#surefire--org.apache.commons.cli.defaultparsertest) | 87 | 0 | 0 | 2 | 97.7% | 0.035 s |
|  | [OptionsTest](#surefire--org.apache.commons.cli.optionstest) | 16 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [ArgumentIsOptionTest](#surefire--org.apache.commons.cli.argumentisoptiontest) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [BasicParserTest](#surefire--org.apache.commons.cli.basicparsertest) | 67 | 0 | 0 | 27 | 59.7% | 0.006 s |
|  | [OptionBuilderTest](#surefire--org.apache.commons.cli.optionbuildertest) | 9 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [DisablePartialMatchingTest](#surefire--org.apache.commons.cli.disablepartialmatchingtest) | 2 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [GnuParserTest](#surefire--org.apache.commons.cli.gnuparsertest) | 67 | 0 | 0 | 22 | 67.2% | 0.006 s |
|  | [DeprecatedAttributesTest](#surefire--org.apache.commons.cli.deprecatedattributestest) | 4 | 0 | 0 | 0 | 100% | 0 s |
|  | [MissingOptionExceptionTest](#surefire--org.apache.commons.cli.missingoptionexceptiontest) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [OptionGroupTest](#surefire--org.apache.commons.cli.optiongrouptest) | 13 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [SolrCreateToolTest](#surefire--org.apache.commons.cli.solrcreatetooltest) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [ValuesTest](#surefire--org.apache.commons.cli.valuestest) | 7 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [ConverterTests](#surefire--org.apache.commons.cli.convertertests) | 14 | 0 | 0 | 0 | 100% | 0.065 s |

<a id="surefire--org.apache.commons.cli.help"></a>

### org.apache.commons.cli.help

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [OptionFormatterTest](#surefire--org.apache.commons.cli.help.optionformattertest) | 22 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [HelpFormatterTest](#surefire--org.apache.commons.cli.help.helpformattertest) | 16 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TextHelpAppendableTest](#surefire--org.apache.commons.cli.help.texthelpappendabletest) | 33 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [UtilTest](#surefire--org.apache.commons.cli.help.utiltest) | 34 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TextStyleTests](#surefire--org.apache.commons.cli.help.textstyletests) | 13 | 0 | 0 | 0 | 100% | 0.002 s |

<a id="surefire--org.apache.commons.cli.bug"></a>

### org.apache.commons.cli.bug

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [BugCLI252Test](#surefire--org.apache.commons.cli.bug.bugcli252test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [BugCLI71Test](#surefire--org.apache.commons.cli.bug.bugcli71test) | 4 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [BugCLI13Test](#surefire--org.apache.commons.cli.bug.bugcli13test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [BugCLI265Test](#surefire--org.apache.commons.cli.bug.bugcli265test) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [BugCLI18Test](#surefire--org.apache.commons.cli.bug.bugcli18test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [BugCLI162Test](#surefire--org.apache.commons.cli.bug.bugcli162test) | 4 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [BugCLI266Test](#surefire--org.apache.commons.cli.bug.bugcli266test) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [BugCLI148Test](#surefire--org.apache.commons.cli.bug.bugcli148test) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [BugCLI312Test](#surefire--org.apache.commons.cli.bug.bugcli312test) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [BugCLI133Test](#surefire--org.apache.commons.cli.bug.bugcli133test) | 1 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [BugCLI325Test](#surefire--org.apache.commons.cli.bug.bugcli325test) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [BugsTest](#surefire--org.apache.commons.cli.bug.bugstest) | 13 | 0 | 0 | 0 | 100% | 0.002 s |

<a id="surefire--test-cases"></a>

## Test Cases

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

<a id="surefire--applicationtest"></a>

### ApplicationTest

|  |  |  |
| --- | --- | --- |
|  | testAnt | 0 s |
|  | testMan | 0.001 s |
|  | testNLT | 0 s |
|  | testLs | 0.001 s |
|  | testGroovy | 0 s |

<a id="surefire--optioncounttest"></a>

### OptionCountTest

|  |  |  |
| --- | --- | --- |
|  | testFiveSwitchesMixed | 0.002 s |
|  | testOneSwitch | 0 s |
|  | testThreeSwitchesCompact | 0 s |
|  | testThreeSwitches | 0.001 s |
|  | testNoSwitch | 0 s |

<a id="surefire--optionformattertest"></a>

### OptionFormatterTest

|  |  |  |
| --- | --- | --- |
|  | testSetOptSeparator | 0.001 s |
|  | testCopyConstructor | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[1] | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[2] | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[3] | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[4] | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[5] | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[6] | 0.001 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[7] | 0 s |
|  | testComplexDeprecationFormat(DeprecatedAttributes, String)[8] | 0 s |
|  | testAsOptional | 0 s |
|  | testSetLongOptPrefix | 0 s |
|  | testSetOptArgumentSeparator | 0 s |
|  | testGetBothOpt | 0 s |
|  | testCli343Part1 | 0 s |
|  | testCli343Part2 | 0 s |
|  | testSetSyntaxFormatFunction | 0 s |
|  | testGetDescription | 0 s |
|  | testAsSyntaxOption | 0 s |
|  | testDefaultSyntaxFormat | 0 s |
|  | testSetArgumentNameDelimiters | 0 s |
|  | testSetDefaultArgName | 0 s |

<a id="surefire--bugcli252test"></a>

### BugCLI252Test

|  |  |  |
| --- | --- | --- |
|  | testAmbiquousOptionName | 0 s |
|  | testExactOptionNameMatch | 0 s |

<a id="surefire--unrecognizedoptionexceptiontest"></a>

### UnrecognizedOptionExceptionTest

|  |  |  |
| --- | --- | --- |
|  | testConstructor | 0 s |

<a id="surefire--commandlinetest"></a>

### CommandLineTest

|  |  |  |
| --- | --- | --- |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[1] | 0.007 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[2] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[3] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[4] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[5] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[6] | 0 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[7] | 0 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[8] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[9] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[10] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[11] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[12] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[13] | 0 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[14] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[15] | 0.001 s |
|  | testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[16] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[1] | 0.003 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[2] | 0.002 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[3] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[4] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[5] | 0.001 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[6] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[7] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[8] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[9] | 0.001 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[10] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[11] | 0.001 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[12] | 0.001 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[13] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[14] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[15] | 0 s |
|  | testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[16] | 0.001 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[1] | 0.002 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[2] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[3] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[4] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[5] | 0.001 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[6] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[7] | 0.001 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[8] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[9] | 0.001 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[10] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[11] | 0.001 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[12] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[13] | 0.001 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[14] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[15] | 0 s |
|  | testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[16] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[1] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[2] | 0.001 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[3] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[4] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[5] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[6] | 0.001 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[7] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[8] | 0.001 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[9] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[10] | 0.001 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[11] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[12] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[13] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[14] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[15] | 0 s |
|  | testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[16] | 0.001 s |
|  | testBuilderGet | 0 s |
|  | testBuilderNullArgs | 0 s |
|  | testGetOptionsBuilder | 0.001 s |
|  | testBuilderNullOption | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[1] | 0.001 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[2] | 0.001 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[3] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[4] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[5] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[6] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[7] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[8] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[9] | 0.001 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[10] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[11] | 0.001 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[12] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[13] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[14] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[15] | 0 s |
|  | testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[16] | 0.001 s |
|  | testGetOptionProperties | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[1] | 0.001 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[2] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[3] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[4] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[5] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[6] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[7] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[8] | 0.001 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[9] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[10] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[11] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[12] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[13] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[14] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[15] | 0 s |
|  | testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[16] | 0.001 s |
|  | testGetOptionPropertiesWithOption | 0 s |
|  | testBuilderBuild | 0.001 s |
|  | testNullOption | 0 s |
|  | testBadGetParsedOptionValue | 0.001 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[1] | 0.001 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[2] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[3] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[4] | 0.001 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[5] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[6] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[7] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[8] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[9] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[10] | 0.001 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[11] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[12] | 0.001 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[13] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[14] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[15] | 0 s |
|  | testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[16] | 0.001 s |
|  | testGetOptionsCtor | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[1] | 0.001 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[2] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[3] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[4] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[5] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[6] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[7] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[8] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[9] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[10] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[11] | 0.001 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[12] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[13] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[14] | 0.001 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[15] | 0 s |
|  | testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[16] | 0.001 s |

<a id="surefire--alreadyselectedexceptiontest"></a>

### AlreadySelectedExceptionTest

|  |  |  |
| --- | --- | --- |
|  | testConstructor | 0 s |

<a id="surefire--bugcli71test"></a>

### BugCLI71Test

|  |  |  |
| --- | --- | --- |
|  | testBasic | 0 s |
|  | testLackOfError | 0.001 s |
|  | testMistakenArgument | 0 s |
|  | testGetsDefaultIfOptional | 0 s |

<a id="surefire--bugcli13test"></a>

### BugCLI13Test

|  |  |  |
| --- | --- | --- |
|  | testCLI13 | 0 s |

<a id="surefire--bugcli265test"></a>

### BugCLI265Test

|  |  |  |
| --- | --- | --- |
|  | testShouldParseShortOptionWithoutValue | 0.001 s |
|  | testShouldParseShortOptionWithValue | 0 s |
|  | testShouldParseConcatenatedShortOptions | 0 s |

<a id="surefire--parseexceptiontest"></a>

### ParseExceptionTest

|  |  |  |
| --- | --- | --- |
|  | testConstructor | 0 s |

<a id="surefire--typehandlertest"></a>

### TypeHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testCreateNumber | 0 s |
|  | testCreateObject | 0 s |
|  | testCreateClass | 0 s |
|  | testCreateFiles | 0.001 s |
|  | testCreateValue(String, Class, Object)[1] | 0.001 s |
|  | testCreateValue(String, Class, Object)[2] | 0 s |
|  | testCreateValue(String, Class, Object)[3] | 0 s |
|  | testCreateValue(String, Class, Object)[4] | 0 s |
|  | testCreateValue(String, Class, Object)[5] | 0.001 s |
|  | testCreateValue(String, Class, Object)[6] | 0 s |
|  | testCreateValue(String, Class, Object)[7] | 0 s |
|  | testCreateValue(String, Class, Object)[8] | 0 s |
|  | testCreateValue(String, Class, Object)[9] | 0 s |
|  | testCreateValue(String, Class, Object)[10] | 0.001 s |
|  | testCreateValue(String, Class, Object)[11] | 0 s |
|  | testCreateValue(String, Class, Object)[12] | 0 s |
|  | testCreateValue(String, Class, Object)[13] | 0 s |
|  | testCreateValue(String, Class, Object)[14] | 0 s |
|  | testCreateValue(String, Class, Object)[15] | 0 s |
|  | testCreateValue(String, Class, Object)[16] | 0.001 s |
|  | testCreateValue(String, Class, Object)[17] | 0 s |
|  | testCreateValue(String, Class, Object)[18] | 0 s |
|  | testCreateValue(String, Class, Object)[19] | 0 s |
|  | testCreateValue(String, Class, Object)[20] | 0 s |
|  | testCreateValue(String, Class, Object)[21] | 0 s |
|  | testCreateValue(String, Class, Object)[22] | 0.001 s |
|  | testCreateValue(String, Class, Object)[23] | 0 s |
|  | testCreateValue(String, Class, Object)[24] | 0 s |
|  | testCreateValue(String, Class, Object)[25] | 0 s |
|  | testCreateValue(String, Class, Object)[26] | 0 s |
|  | testCreateValue(String, Class, Object)[27] | 0 s |
|  | testCreateValue(String, Class, Object)[28] | 0.001 s |
|  | testCreateValue(String, Class, Object)[29] | 0 s |
|  | testCreateValue(String, Class, Object)[30] | 0 s |
|  | testCreateValue(String, Class, Object)[31] | 0 s |
|  | testCreateValue(String, Class, Object)[32] | 0 s |
|  | testCreateValue(String, Class, Object)[33] | 0 s |
|  | testCreateValue(String, Class, Object)[34] | 0.001 s |
|  | testCreateValue(String, Class, Object)[35] | 0 s |
|  | testCreateValue(String, Class, Object)[36] | 0 s |
|  | testCreateValue(String, Class, Object)[37] | 0 s |
|  | testCreateValue(String, Class, Object)[38] | 0 s |
|  | testCreateValue(String, Class, Object)[39] | 0 s |
|  | testCreateValue(String, Class, Object)[40] | 0.001 s |
|  | testCreateValue(String, Class, Object)[41] | 0 s |
|  | testCreateValue(String, Class, Object)[42] | 0 s |
|  | testCreateValue(String, Class, Object)[43] | 0 s |
|  | testCreateValue(String, Class, Object)[44] | 0 s |
|  | testCreateValue(String, Class, Object)[45] | 0 s |
|  | testCreateValue(String, Class, Object)[46] | 0.001 s |
|  | testCreateValue(String, Class, Object)[47] | 0 s |
|  | testCreateValue(String, Class, Object)[48] | 0 s |
|  | testCreateValue(String, Class, Object)[49] | 0 s |
|  | testCreateValue(String, Class, Object)[50] | 0 s |
|  | testRegister | 0.001 s |
|  | testOpenFile | 0 s |
|  | testCreateValueExistingFile | 0 s |
|  | testCreateDate(Date)[1] | 0.001 s |
|  | testCreateDate(Date)[2] | 0 s |
|  | testCreateDate(Date)[3] | 0.001 s |
|  | testCreateFile | 0.004 s |
|  | testCreateURL | 0 s |
|  | testnstantiableEquals | 0 s |

<a id="surefire--solrclitest"></a>

### SolrCliTest

|  |  |  |
| --- | --- | --- |
|  | testOptions | 0.001 s |

<a id="surefire--posixparsertest"></a>

### PosixParserTest

|  |  |  |
| --- | --- | --- |
|  | testSimpleLong | 0 s |
|  | testSimpleShort | 0.001 s |
|  | testLongOptionQuoteHandling | 0 s |
|  | testOptionalArgsOptionBuilder | 0 s |
|  | testStopBursting2 | 0 s |
|  | testMissingRequiredOption | 0 s |
|  | testShortWithoutEqual | 0 s |
|  | testReuseOptionsTwice | 0 s |
|  | testMissingRequiredGroup | 0.001 s |
|  | testOptionGroupLong | 0 s |
|  | testLongOptionWithEqualsQuoteHandling | 0 s |
|  | testMissingArgWithBursting | 0 s |
|  | testMissingRequiredOptions | 0 s |
|  | testShortWithUnexpectedArgument | 0 s |
|  | testPropertyOverrideValues | 0 s |
|  | testStopAtNonOptionLong | 0 s |
|  | testNegativeArgument | 0 s |
|  | testOptionalArgsOptionDotBuilder | 0 s |
|  | testStopBursting | 0 s |
|  | testStopAtUnexpectedArg | 0 s |
|  | testPartialLongOptionSingleDash | 0 s |
|  | testOptionGroup | 0.001 s |
|  | testLongWithoutEqualDoubleDash | 0 s |
|  | testPropertyOptionSingularValue | 0 s |
|  | testPropertyOptionMultipleValues | 0 s |
|  | testMissingArg | 0 s |
|  | testPropertyOptionFlags | 0 s |
|  | testPropertyOptionGroup | 0 s |
|  | testUnrecognizedOptionWithBursting | 0 s |
|  | testAmbiguousArgParsing | 0 s |
|  | testMultipleWithLong | 0 s |
|  | testMultipleWithNull | 0 s |
|  | testUnrecognizedOption | 0 s |
|  | testBursting | 0 s |
|  | testAmbiguousPartialLongOption1 | 0 s |
|  | testAmbiguousPartialLongOption2 | 0 s |
|  | testAmbiguousPartialLongOption3 | 0 s |
|  | testPropertyOptionUnexpected | 0 s |
|  | testSingleDash | 0 s |
|  | testWithRequiredOption | 0 s |
|  | testUnlimitedArgs | 0 s |
|  | testPropertyOptionRequired | 0 s |
|  | testOptionAndRequiredOption | 0 s |
|  | testLongWithEqualDoubleDash | 0 s |
|  | testLongWithUnexpectedArgument2 | 0 s |
|  | testStopAtNonOptionShort | 0 s |
|  | testUnambiguousPartialLongOption1 | 0 s |
|  | testUnambiguousPartialLongOption2 | 0 s |
|  | testUnambiguousPartialLongOption3 | 0 s |
|  | testShortOptionConcatenatedQuoteHandling | 0.001 s |
|  | testMultiple | 0 s |
|  | testArgumentStartingWithHyphen | 0 s |
|  | testPropertiesOption1 | 0 s |
|  | testPropertiesOption2 | 0 s |
|  | testDoubleDash1 | 0 s |
|  | testStopAtExpectedArg | 0 s |
|  | testShortOptionQuoteHandling | 0 s |
|  | [testAmbiguousLongWithoutEqualSingleDash](#surefire--org.apache.commons.cli.posixparsertest.testambiguouslongwithoutequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testLongWithoutEqualSingleDash](#surefire--org.apache.commons.cli.posixparsertest.testlongwithoutequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testLongWithoutEqualSingleDash');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testAmbiguousPartialLongOption4](#surefire--org.apache.commons.cli.posixparsertest.testambiguouspartiallongoption4) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption4');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testShortWithEqual](#surefire--org.apache.commons.cli.posixparsertest.testshortwithequal) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testShortWithEqual');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testNegativeOption](#surefire--org.apache.commons.cli.posixparsertest.testnegativeoption) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testNegativeOption');) | 0 s |
| - | not supported by the PosixParser (CLI-184) | - |
|  | [testLongWithUnexpectedArgument1](#surefire--org.apache.commons.cli.posixparsertest.testlongwithunexpectedargument1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument1');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testLongWithEqualSingleDash](#surefire--org.apache.commons.cli.posixparsertest.testlongwithequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testLongWithEqualSingleDash');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testUnambiguousPartialLongOption4](#surefire--org.apache.commons.cli.posixparsertest.testunambiguouspartiallongoption4) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption4');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testDoubleDash2](#surefire--org.apache.commons.cli.posixparsertest.testdoubledash2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testDoubleDash2');) | 0 s |
| - | not supported by the PosixParser | - |
|  | [testAmbiguousLongWithoutEqualSingleDash2](#surefire--org.apache.commons.cli.posixparsertest.testambiguouslongwithoutequalsingledash2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash2');) | 0 s |
| - | not supported by the PosixParser | - |

<a id="surefire--apthelpappendabletest"></a>

### AptHelpAppendableTest

|  |  |  |
| --- | --- | --- |
|  | testAppendTitleTest | 0 s |
|  | testAppendTableTest | 0.001 s |
|  | testAppendParagraphTest | 0 s |
|  | testAppendHeaderTest | 0.001 s |
|  | testAppendListTest | 0 s |
|  | testAppendParagraphFormatTest | 0 s |
|  | testAppendFormatTest | 0 s |

<a id="surefire--valuetest"></a>

### ValueTest

|  |  |  |
| --- | --- | --- |
|  | testLongOptionalArgValuesWithOption(CommandLineParser)[1] | 0.001 s |
|  | testLongOptionalArgValuesWithOption(CommandLineParser)[2] | 0 s |
|  | testShortOptionalNArgValuesWithOption | 0 s |
|  | testShortOptionalArgValues(CommandLineParser)[1] | 0 s |
|  | testShortOptionalArgValues(CommandLineParser)[2] | 0 s |
|  | testShortOptionalArgValuesWithOption(CommandLineParser)[1] | 0 s |
|  | testShortOptionalArgValuesWithOption(CommandLineParser)[2] | 0 s |
|  | testShortOptionalArgValueWithOption(CommandLineParser)[1] | 0 s |
|  | testShortOptionalArgValueWithOption(CommandLineParser)[2] | 0 s |
|  | testLongOptionalArgValue(CommandLineParser)[1] | 0 s |
|  | testLongOptionalArgValue(CommandLineParser)[2] | 0.001 s |
|  | testShortOptionalArgNoValue(CommandLineParser)[1] | 0 s |
|  | testShortOptionalArgNoValue(CommandLineParser)[2] | 0 s |
|  | testShortNoArgWithOption | 0 s |
|  | testLongWithArg | 0 s |
|  | testLongOptionalNArgValuesWithOption(CommandLineParser)[1] | 0.001 s |
|  | testLongOptionalNArgValuesWithOption(CommandLineParser)[2] | 0 s |
|  | testLongOptionalNArgValues(CommandLineParser)[1] | 0 s |
|  | testLongOptionalNArgValues(CommandLineParser)[2] | 0 s |
|  | testShortWithArgWithOption | 0 s |
|  | testShortWithArg | 0 s |
|  | testShortOptionalNArgValuesSeparated | 0 s |
|  | testLongOptionalArgValueWithOption(CommandLineParser)[1] | 0 s |
|  | testLongOptionalArgValueWithOption(CommandLineParser)[2] | 0 s |
|  | testLongOptionalArgValues(CommandLineParser)[1] | 0 s |
|  | testLongOptionalArgValues(CommandLineParser)[2] | 0.001 s |
|  | testShortOptionalNArgValues(CommandLineParser)[1] | 0 s |
|  | testShortOptionalNArgValues(CommandLineParser)[2] | 0 s |
|  | testLongNoArgWithOption | 0 s |
|  | testLongOptionalNoValueWithOption(CommandLineParser)[1] | 0.001 s |
|  | testLongOptionalNoValueWithOption(CommandLineParser)[2] | 0 s |
|  | testLongNoArg | 0 s |
|  | testShortNoArg | 0 s |
|  | testLongOptionalNoValue(CommandLineParser)[1] | 0 s |
|  | testLongOptionalNoValue(CommandLineParser)[2] | 0.001 s |
|  | testShortOptionalArgValue(CommandLineParser)[1] | 0 s |
|  | testShortOptionalArgValue(CommandLineParser)[2] | 0 s |
|  | testShortOptionalArgNoValueWithOption(CommandLineParser)[1] | 0 s |
|  | testShortOptionalArgNoValueWithOption(CommandLineParser)[2] | 0 s |
|  | testLongWithArgWithOption | 0 s |

<a id="surefire--optionvalidatortest"></a>

### OptionValidatorTest

|  |  |  |
| --- | --- | --- |
|  | testValidate(String, boolean, String)[1] | 0.001 s |
|  | testValidate(String, boolean, String)[2] | 0 s |
|  | testValidate(String, boolean, String)[3] | 0 s |
|  | testValidate(String, boolean, String)[4] | 0 s |
|  | testValidate(String, boolean, String)[5] | 0 s |
|  | testValidate(String, boolean, String)[6] | 0 s |
|  | testValidate(String, boolean, String)[7] | 0 s |
|  | testValidate(String, boolean, String)[8] | 0 s |
|  | testValidate(String, boolean, String)[9] | 0 s |
|  | testValidate(String, boolean, String)[10] | 0.001 s |
|  | testValidate(String, boolean, String)[11] | 0 s |
|  | testValidate(String, boolean, String)[12] | 0 s |
|  | testValidate(String, boolean, String)[13] | 0 s |
|  | testValidate(String, boolean, String)[14] | 0 s |
|  | testValidate(String, boolean, String)[15] | 0 s |
|  | testValidate(String, boolean, String)[16] | 0 s |
|  | testValidate(String, boolean, String)[17] | 0 s |
|  | testValidate(String, boolean, String)[18] | 0 s |
|  | testValidate(String, boolean, String)[19] | 0 s |
|  | testValidate(String, boolean, String)[20] | 0 s |
|  | testValidate(String, boolean, String)[21] | 0 s |
|  | testValidate(String, boolean, String)[22] | 0 s |
|  | testValidate(String, boolean, String)[23] | 0 s |
|  | testValidate(String, boolean, String)[24] | 0 s |
|  | testValidate(String, boolean, String)[25] | 0 s |
|  | testValidate(String, boolean, String)[26] | 0 s |
|  | testValidate(String, boolean, String)[27] | 0 s |
|  | testValidate(String, boolean, String)[28] | 0 s |
|  | testValidate(String, boolean, String)[29] | 0 s |
|  | testValidate(String, boolean, String)[30] | 0 s |
|  | testValidate(String, boolean, String)[31] | 0 s |
|  | testValidate(String, boolean, String)[32] | 0.001 s |
|  | testValidate(String, boolean, String)[33] | 0 s |
|  | testValidate(String, boolean, String)[34] | 0 s |
|  | testValidate(String, boolean, String)[35] | 0 s |
|  | testValidate(String, boolean, String)[36] | 0 s |
|  | testValidate(String, boolean, String)[37] | 0 s |
|  | testValidate(String, boolean, String)[38] | 0 s |
|  | testValidate(String, boolean, String)[39] | 0 s |
|  | testValidate(String, boolean, String)[40] | 0.001 s |
|  | testValidate(String, boolean, String)[41] | 0 s |
|  | testValidate(String, boolean, String)[42] | 0 s |
|  | testValidate(String, boolean, String)[43] | 0 s |
|  | testValidate(String, boolean, String)[44] | 0 s |
|  | testValidate(String, boolean, String)[45] | 0 s |
|  | testValidate(String, boolean, String)[46] | 0 s |
|  | testValidate(String, boolean, String)[47] | 0 s |
|  | testValidate(String, boolean, String)[48] | 0 s |
|  | testValidate(String, boolean, String)[49] | 0.001 s |
|  | testValidate(String, boolean, String)[50] | 0 s |
|  | testValidate(String, boolean, String)[51] | 0 s |
|  | testValidate(String, boolean, String)[52] | 0 s |
|  | testValidate(String, boolean, String)[53] | 0 s |
|  | testValidate(String, boolean, String)[54] | 0 s |
|  | testValidate(String, boolean, String)[55] | 0 s |
|  | testValidate(String, boolean, String)[56] | 0 s |
|  | testValidate(String, boolean, String)[57] | 0 s |
|  | testValidate(String, boolean, String)[58] | 0 s |
|  | testValidate(String, boolean, String)[59] | 0.001 s |
|  | testValidate(String, boolean, String)[60] | 0 s |
|  | testValidate(String, boolean, String)[61] | 0 s |
|  | testValidate(String, boolean, String)[62] | 0 s |
|  | testValidate(String, boolean, String)[63] | 0 s |
|  | testValidate(String, boolean, String)[64] | 0 s |
|  | testValidate(String, boolean, String)[65] | 0 s |
|  | testValidate(String, boolean, String)[66] | 0 s |
|  | testValidate(String, boolean, String)[67] | 0 s |
|  | testValidate(String, boolean, String)[68] | 0 s |
|  | testValidate(String, boolean, String)[69] | 0 s |
|  | testValidate(String, boolean, String)[70] | 0 s |
|  | testValidate(String, boolean, String)[71] | 0 s |
|  | testValidate(String, boolean, String)[72] | 0 s |
|  | testValidate(String, boolean, String)[73] | 0 s |
|  | testValidate(String, boolean, String)[74] | 0 s |
|  | testValidate(String, boolean, String)[75] | 0.001 s |
|  | testValidate(String, boolean, String)[76] | 0 s |
|  | testValidate(String, boolean, String)[77] | 0 s |
|  | testValidate(String, boolean, String)[78] | 0 s |
|  | testValidate(String, boolean, String)[79] | 0 s |
|  | testValidate(String, boolean, String)[80] | 0 s |
|  | testValidate(String, boolean, String)[81] | 0 s |
|  | testValidate(String, boolean, String)[82] | 0 s |
|  | testValidate(String, boolean, String)[83] | 0 s |
|  | testValidate(String, boolean, String)[84] | 0 s |
|  | testValidate(String, boolean, String)[85] | 0 s |
|  | testValidate(String, boolean, String)[86] | 0 s |
|  | testValidate(String, boolean, String)[87] | 0 s |
|  | testValidate(String, boolean, String)[88] | 0 s |
|  | testValidate(String, boolean, String)[89] | 0 s |
|  | testValidate(String, boolean, String)[90] | 0 s |
|  | testValidate(String, boolean, String)[91] | 0 s |
|  | testValidate(String, boolean, String)[92] | 0.001 s |
|  | testValidate(String, boolean, String)[93] | 0 s |
|  | testValidate(String, boolean, String)[94] | 0 s |
|  | testValidate(String, boolean, String)[95] | 0 s |
|  | testValidate(String, boolean, String)[96] | 0 s |
|  | testValidate(String, boolean, String)[97] | 0 s |
|  | testValidate(String, boolean, String)[98] | 0 s |
|  | testValidate(String, boolean, String)[99] | 0 s |
|  | testValidate(String, boolean, String)[100] | 0 s |
|  | testValidate(String, boolean, String)[101] | 0.001 s |
|  | testValidate(String, boolean, String)[102] | 0 s |
|  | testValidate(String, boolean, String)[103] | 0 s |
|  | testValidate(String, boolean, String)[104] | 0 s |
|  | testValidate(String, boolean, String)[105] | 0 s |
|  | testValidate(String, boolean, String)[106] | 0 s |
|  | testValidate(String, boolean, String)[107] | 0 s |
|  | testValidate(String, boolean, String)[108] | 0 s |
|  | testValidate(String, boolean, String)[109] | 0 s |
|  | testValidate(String, boolean, String)[110] | 0.001 s |
|  | testValidate(String, boolean, String)[111] | 0 s |
|  | testValidate(String, boolean, String)[112] | 0 s |
|  | testValidate(String, boolean, String)[113] | 0 s |
|  | testValidate(String, boolean, String)[114] | 0 s |
|  | testExclusivity | 0 s |

<a id="surefire--bugcli18test"></a>

### BugCLI18Test

|  |  |  |
| --- | --- | --- |
|  | testCLI18 | 0 s |

<a id="surefire--optiontest"></a>

### OptionTest

|  |  |  |
| --- | --- | --- |
|  | testGetValue | 0 s |
|  | testSerialization | 0.004 s |
|  | testSubclass | 0 s |
|  | testProcessValue | 0 s |
|  | testClear | 0.001 s |
|  | testClone | 0 s |
|  | testBuilderDeprecatedBuildEmpty | 0 s |
|  | testBuilderInvalidOptionName0 | 0 s |
|  | testBuilderInvalidOptionName1 | 0 s |
|  | testBuilderInvalidOptionName2 | 0 s |
|  | testBuilderInvalidOptionName3 | 0 s |
|  | testBuilderInvalidOptionName4 | 0 s |
|  | testAddValue | 0 s |
|  | testBuilderMethods | 0 s |
|  | testHasArgs | 0 s |
|  | testHasArgName | 0.001 s |
|  | testHashCode | 0 s |
|  | testBuilderEmpty | 0 s |
|  | testTypeClass | 0 s |
|  | testEquals | 0 s |
|  | testBuilderInsufficientParams1 | 0 s |
|  | testBuilderInsufficientParams2 | 0.001 s |
|  | testTypeObject | 0 s |

<a id="surefire--patternoptionbuildertest"></a>

### PatternOptionBuilderTest

|  |  |  |
| --- | --- | --- |
|  | testSimplePattern | 0.056 s |
|  | testExistingFilePattern | 0.002 s |
|  | testURLPattern | 0 s |
|  | testEmptyPattern | 0 s |
|  | testClassPattern | 0.001 s |
|  | testRequiredOption | 0.001 s |
|  | testExistingFilePatternFileNotExist | 0.001 s |
|  | testNumberPattern | 0.004 s |
|  | testUntypedPattern | 0 s |
|  | testObjectPattern | 0.001 s |

<a id="surefire--bugcli162test"></a>

### BugCLI162Test

|  |  |  |
| --- | --- | --- |
|  | testInfiniteLoop | 0.001 s |
|  | testLongLineChunkingIndentIgnored | 0 s |
|  | testLongLineChunking | 0 s |
|  | testPrintHelpLongLines | 0.001 s |

<a id="surefire--bugcli266test"></a>

### BugCLI266Test

|  |  |  |
| --- | --- | --- |
|  | testOptionComparatorInsertedOrder | 0 s |
|  | testOptionComparatorDefaultOrder | 0 s |

<a id="surefire--helpformattertest"></a>

### HelpFormatterTest

|  |  |  |
| --- | --- | --- |
|  | testDeprecatedPrintOptionsZeroWidth(int)[1] | 0.001 s |
|  | testDeprecatedPrintOptionsZeroWidth(int)[2] | 0.001 s |
|  | testDeprecatedPrintOptionsZeroWidth(int)[3] | 0 s |
|  | testUsageWithLongOptSeparator | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[1] | 0.001 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[2] | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[3] | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[4] | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[5] | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[6] | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[7] | 0 s |
|  | testPrintDeprecatedOptions(HelpFormatter, Option, String)[8] | 0.001 s |
|  | testRenderWrappedTextSingleLine | 0.261 s |
|  | testIndentedHeaderAndFooter | 0.001 s |
|  | testPrintSortedUsageWithNullComparator | 0 s |
|  | testAccessors | 0 s |
|  | testDeprecatedFindWrapPosZeroWidth(int)[1] | 0.001 s |
|  | testDeprecatedFindWrapPosZeroWidth(int)[2] | 0 s |
|  | testDeprecatedFindWrapPosZeroWidth(int)[3] | 0 s |
|  | testRtrim | 0 s |
|  | testPrintRequiredOptionGroupUsage | 0.001 s |
|  | testHelpWithLongOptSeparator | 0 s |
|  | testRenderWrappedTextSingleLinePadded | 0 s |
|  | testRenderWrappedTextMultiLine | 0 s |
|  | testPrintUsage | 0 s |
|  | testPrintSortedUsage | 0.001 s |
|  | testPrintHelpWithEmptySyntax | 0 s |
|  | testPrintOptions | 0 s |
|  | testAutomaticUsage | 0 s |
|  | testDefaultArgName | 0 s |
|  | testPrintHelpNewlineFooter | 0 s |
|  | testPrintHelpNewlineHeader | 0.001 s |
|  | testRenderWrappedTextWordCut | 0 s |
|  | testHeaderStartingWithLineSeparator0 | 0 s |
|  | testHeaderStartingWithLineSeparator1 | 0 s |
|  | testOptionWithoutShortFormat | 0.001 s |
|  | testRenderWrappedTextMultiLinePadded | 0 s |
|  | testPrintOptionGroupUsage | 0 s |
|  | testPrintOptionWithEmptyArgNameUsage | 0 s |
|  | testRenderWrappedTextSingleLinePadded2 | 0 s |
|  | testOptionWithoutShortFormat2 | 0.001 s |
|  | testFindWrapPos | 0 s |
|  | testRenderSince | 0.002 s |
|  | testPrintHelpWithSince | 0 s |

<a id="surefire--utiltest"></a>

### UtilTest

|  |  |  |
| --- | --- | --- |
|  | testStripLeadingAndTrailingQuotes | 0.010 s |
|  | testStripLeadingHyphens | 0.001 s |

<a id="surefire--bugcli148test"></a>

### BugCLI148Test

|  |  |  |
| --- | --- | --- |
|  | testWorkaround1 | 0.001 s |
|  | testWorkaround2 | 0 s |

<a id="surefire--bugcli312test"></a>

### BugCLI312Test

|  |  |  |
| --- | --- | --- |
|  | testNoOptionValues | 0 s |
|  | testPropertyStyleOption\_withGetOptionProperties | 0 s |
|  | testPropertyStyleOption\_withGetOptions | 0.001 s |

<a id="surefire--bugcli133test"></a>

### BugCLI133Test

|  |  |  |
| --- | --- | --- |
|  | testOrder | 0.001 s |

<a id="surefire--defaultparsertest"></a>

### DefaultParserTest

|  |  |  |
| --- | --- | --- |
|  | testSimpleLong | 0 s |
|  | testSimpleShort | 0.001 s |
|  | testLongOptionQuoteHandling | 0.001 s |
|  | testOptionalArgsOptionBuilder | 0.001 s |
|  | testStopBursting2 | 0 s |
|  | testMissingRequiredOption | 0.001 s |
|  | testShortWithoutEqual | 0 s |
|  | testReuseOptionsTwice | 0.001 s |
|  | testMissingRequiredGroup | 0 s |
|  | testOptionGroupLong | 0.001 s |
|  | testAmbiguousLongWithoutEqualSingleDash | 0 s |
|  | testMissingArgWithBursting | 0 s |
|  | testMissingRequiredOptions | 0 s |
|  | testShortWithUnexpectedArgument | 0 s |
|  | testPropertyOverrideValues | 0 s |
|  | testStopAtNonOptionLong | 0 s |
|  | testNegativeArgument | 0 s |
|  | testOptionalArgsOptionDotBuilder | 0 s |
|  | testStopBursting | 0 s |
|  | testStopAtUnexpectedArg | 0 s |
|  | testPartialLongOptionSingleDash | 0 s |
|  | testOptionGroup | 0.001 s |
|  | testLongWithoutEqualDoubleDash | 0 s |
|  | testLongWithoutEqualSingleDash | 0 s |
|  | testPropertyOptionSingularValue | 0 s |
|  | testPropertyOptionMultipleValues | 0 s |
|  | testMissingArg | 0.001 s |
|  | testPropertyOptionFlags | 0 s |
|  | testPropertyOptionGroup | 0 s |
|  | testUnrecognizedOptionWithBursting | 0.001 s |
|  | testAmbiguousArgParsing | 0 s |
|  | testMultipleWithLong | 0 s |
|  | testMultipleWithNull | 0 s |
|  | testUnrecognizedOption | 0 s |
|  | testBursting | 0 s |
|  | testAmbiguousPartialLongOption1 | 0.001 s |
|  | testAmbiguousPartialLongOption2 | 0 s |
|  | testAmbiguousPartialLongOption3 | 0 s |
|  | testAmbiguousPartialLongOption4 | 0 s |
|  | testPropertyOptionUnexpected | 0 s |
|  | testSingleDash | 0.001 s |
|  | testShortWithEqual | 0 s |
|  | testWithRequiredOption | 0 s |
|  | testUnlimitedArgs | 0 s |
|  | testNegativeOption | 0 s |
|  | testPropertyOptionRequired | 0 s |
|  | testOptionAndRequiredOption | 0 s |
|  | testLongWithEqualDoubleDash | 0 s |
|  | testLongWithUnexpectedArgument1 | 0.001 s |
|  | testLongWithUnexpectedArgument2 | 0 s |
|  | testStopAtNonOptionShort | 0 s |
|  | testLongWithEqualSingleDash | 0 s |
|  | testUnambiguousPartialLongOption1 | 0 s |
|  | testUnambiguousPartialLongOption2 | 0.001 s |
|  | testUnambiguousPartialLongOption3 | 0 s |
|  | testUnambiguousPartialLongOption4 | 0 s |
|  | testMultiple | 0 s |
|  | testArgumentStartingWithHyphen | 0 s |
|  | testPropertiesOption1 | 0 s |
|  | testPropertiesOption2 | 0 s |
|  | testDoubleDash1 | 0 s |
|  | testDoubleDash2 | 0.001 s |
|  | testStopAtExpectedArg | 0.001 s |
|  | testAmbiguousLongWithoutEqualSingleDash2 | 0 s |
|  | testShortOptionQuoteHandling | 0 s |
|  | testParseSkipNonHappyPath | 0 s |
|  | testParseSkipHappyPath | 0 s |
|  | [testLongOptionWithEqualsQuoteHandling](#surefire--org.apache.commons.cli.defaultparsertest.testlongoptionwithequalsquotehandling) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.DefaultParserTest.testLongOptionWithEqualsQuoteHandling');) | 0 s |
| - | Test case handled in the parameterized tests as "DEFAULT behavior" | - |
|  | testParseIgnoreHappyPath | 0 s |
|  | testBuilder | 0 s |
|  | testLegacyStopAtNonOption | 0 s |
|  | testParseNullOption | 0.001 s |
|  | testParseIgnoreNonHappyPath | 0 s |
|  | [testShortOptionConcatenatedQuoteHandling](#surefire--org.apache.commons.cli.defaultparsertest.testshortoptionconcatenatedquotehandling) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.DefaultParserTest.testShortOptionConcatenatedQuoteHandling');) | 0 s |
| - | Test case handled in the parameterized tests as "DEFAULT behavior" | - |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[1] | 0.002 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[2] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[3] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[4] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[5] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[6] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[7] | 0.001 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[8] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[9] | 0.001 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[10] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[11] | 0 s |
|  | testParameterized(String, CommandLineParser, String[], String, String, String)[12] | 0 s |
|  | testDeprecated | 0.001 s |

<a id="surefire--helpformattertest-2"></a>

### HelpFormatterTest

|  |  |  |
| --- | --- | --- |
|  | testToArgNameTest | 0.001 s |
|  | verifyOptionGroupingOutput | 0 s |
|  | testToSyntaxOptionGroupTest | 0 s |
|  | testPrintHelp | 0.001 s |
|  | testSetOptionFormatBuilderTest | 0 s |
|  | testPrintHelpWithIterableOptions | 0.001 s |
|  | testSyntaxPrefix | 0 s |
|  | testPrintOptions | 0 s |
|  | testToSyntaxOptionIterableTest | 0 s |
|  | testToSyntaxOptionOptionsTest | 0 s |
|  | testSetOptionGroupSeparatorTest | 0 s |
|  | testPrintHelpHeader | 0.001 s |
|  | testSortOptionGroupsTest | 0 s |
|  | testSortOptionsTest | 0 s |
|  | testDefault | 0 s |
|  | testPrintHelpXML | 0 s |

<a id="surefire--optionstest"></a>

### OptionsTest

|  |  |  |
| --- | --- | --- |
|  | testAddOptions2X | 0 s |
|  | testMissingOptionsException | 0 s |
|  | testGetMatchingOpts | 0 s |
|  | testLong | 0.001 s |
|  | testToString | 0 s |
|  | testHelpOptions | 0 s |
|  | testAddOptions | 0 s |
|  | testMissingOptionException | 0 s |
|  | testDuplicateSimple | 0 s |
|  | testAddNonConflictingOptions | 0 s |
|  | testAddConflictingOptions | 0 s |
|  | testGetOptionsGroups | 0.001 s |
|  | testDuplicateLong | 0 s |
|  | testSimple | 0 s |
|  | testDeprecated | 0 s |
|  | testRequiredOptionInGroupShouldNotBeInRequiredList | 0 s |

<a id="surefire--argumentisoptiontest"></a>

### ArgumentIsOptionTest

|  |  |  |
| --- | --- | --- |
|  | testOptionWithArgument | 0.001 s |
|  | testOptionAndOptionWithArgument | 0 s |
|  | testOption | 0 s |

<a id="surefire--basicparsertest"></a>

### BasicParserTest

|  |  |  |
| --- | --- | --- |
|  | testSimpleLong | 0 s |
|  | testSimpleShort | 0.001 s |
|  | testLongOptionQuoteHandling | 0 s |
|  | testOptionalArgsOptionBuilder | 0 s |
|  | testMissingRequiredOption | 0 s |
|  | testReuseOptionsTwice | 0 s |
|  | testMissingRequiredGroup | 0 s |
|  | testOptionGroupLong | 0 s |
|  | testMissingRequiredOptions | 0 s |
|  | testShortWithUnexpectedArgument | 0 s |
|  | testPropertyOverrideValues | 0 s |
|  | testStopAtNonOptionLong | 0 s |
|  | testNegativeArgument | 0.001 s |
|  | testOptionalArgsOptionDotBuilder | 0 s |
|  | testStopAtUnexpectedArg | 0 s |
|  | testOptionGroup | 0 s |
|  | testLongWithoutEqualDoubleDash | 0 s |
|  | testPropertyOptionSingularValue | 0 s |
|  | testPropertyOptionMultipleValues | 0 s |
|  | testMissingArg | 0 s |
|  | testPropertyOptionFlags | 0 s |
|  | testPropertyOptionGroup | 0 s |
|  | testAmbiguousArgParsing | 0 s |
|  | testMultipleWithLong | 0 s |
|  | testMultipleWithNull | 0 s |
|  | testUnrecognizedOption | 0 s |
|  | testPropertyOptionUnexpected | 0 s |
|  | testSingleDash | 0 s |
|  | testWithRequiredOption | 0 s |
|  | testUnlimitedArgs | 0 s |
|  | testPropertyOptionRequired | 0 s |
|  | testOptionAndRequiredOption | 0 s |
|  | testLongWithUnexpectedArgument1 | 0 s |
|  | testLongWithUnexpectedArgument2 | 0 s |
|  | testStopAtNonOptionShort | 0 s |
|  | testMultiple | 0 s |
|  | testArgumentStartingWithHyphen | 0 s |
|  | testDoubleDash1 | 0.001 s |
|  | testStopAtExpectedArg | 0 s |
|  | testShortOptionQuoteHandling | 0 s |
|  | [testStopBursting2](#surefire--org.apache.commons.cli.basicparsertest.teststopbursting2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testStopBursting2');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testShortWithoutEqual](#surefire--org.apache.commons.cli.basicparsertest.testshortwithoutequal) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testShortWithoutEqual');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testLongOptionWithEqualsQuoteHandling](#surefire--org.apache.commons.cli.basicparsertest.testlongoptionwithequalsquotehandling) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongOptionWithEqualsQuoteHandling');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testAmbiguousLongWithoutEqualSingleDash](#surefire--org.apache.commons.cli.basicparsertest.testambiguouslongwithoutequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testMissingArgWithBursting](#surefire--org.apache.commons.cli.basicparsertest.testmissingargwithbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testMissingArgWithBursting');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testStopBursting](#surefire--org.apache.commons.cli.basicparsertest.teststopbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testStopBursting');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testPartialLongOptionSingleDash](#surefire--org.apache.commons.cli.basicparsertest.testpartiallongoptionsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testPartialLongOptionSingleDash');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testLongWithoutEqualSingleDash](#surefire--org.apache.commons.cli.basicparsertest.testlongwithoutequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongWithoutEqualSingleDash');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testUnrecognizedOptionWithBursting](#surefire--org.apache.commons.cli.basicparsertest.testunrecognizedoptionwithbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnrecognizedOptionWithBursting');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testBursting](#surefire--org.apache.commons.cli.basicparsertest.testbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testBursting');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testAmbiguousPartialLongOption1](#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption1');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testAmbiguousPartialLongOption2](#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption2');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testAmbiguousPartialLongOption3](#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption3) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption3');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testAmbiguousPartialLongOption4](#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption4) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption4');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testShortWithEqual](#surefire--org.apache.commons.cli.basicparsertest.testshortwithequal) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testShortWithEqual');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testNegativeOption](#surefire--org.apache.commons.cli.basicparsertest.testnegativeoption) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testNegativeOption');) | 0 s |
| - | not supported by the BasicParser (CLI-184) | - |
|  | [testLongWithEqualDoubleDash](#surefire--org.apache.commons.cli.basicparsertest.testlongwithequaldoubledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongWithEqualDoubleDash');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testLongWithEqualSingleDash](#surefire--org.apache.commons.cli.basicparsertest.testlongwithequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongWithEqualSingleDash');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testUnambiguousPartialLongOption1](#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption1');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testUnambiguousPartialLongOption2](#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption2');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testUnambiguousPartialLongOption3](#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption3) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption3');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testUnambiguousPartialLongOption4](#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption4) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption4');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testShortOptionConcatenatedQuoteHandling](#surefire--org.apache.commons.cli.basicparsertest.testshortoptionconcatenatedquotehandling) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testShortOptionConcatenatedQuoteHandling');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testPropertiesOption1](#surefire--org.apache.commons.cli.basicparsertest.testpropertiesoption1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testPropertiesOption1');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testPropertiesOption2](#surefire--org.apache.commons.cli.basicparsertest.testpropertiesoption2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testPropertiesOption2');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testDoubleDash2](#surefire--org.apache.commons.cli.basicparsertest.testdoubledash2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testDoubleDash2');) | 0 s |
| - | not supported by the BasicParser | - |
|  | [testAmbiguousLongWithoutEqualSingleDash2](#surefire--org.apache.commons.cli.basicparsertest.testambiguouslongwithoutequalsingledash2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash2');) | 0 s |
| - | not supported by the BasicParser | - |

<a id="surefire--optionbuildertest"></a>

### OptionBuilderTest

|  |  |  |
| --- | --- | --- |
|  | testBaseOptionStringOpt | 0 s |
|  | testTwoCompleteOptions | 0 s |
|  | testBuilderIsResettedAlways | 0.001 s |
|  | testCompleteOption | 0 s |
|  | testCreateIncompleteOption | 0 s |
|  | testOptionArgNumbers | 0 s |
|  | testIllegalOptions | 0 s |
|  | testSpecialOptChars | 0 s |
|  | testBaseOptionCharOpt | 0 s |

<a id="surefire--texthelpappendabletest"></a>

### TextHelpAppendableTest

|  |  |  |
| --- | --- | --- |
|  | testAppendParagraph | 0.001 s |
|  | testAppendParagraphFormat | 0 s |
|  | testAdjustTableFormat | 0 s |
|  | testWriteColumnQueues | 0.001 s |
|  | testPrintWrapped | 0 s |
|  | testGetStyleBuilder | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[1] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[2] | 0.001 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[3] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[4] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[5] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[6] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[7] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[8] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[9] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[10] | 0.001 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[11] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[12] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[13] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[14] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[15] | 0 s |
|  | testindexOfWrapPosWithWhitespace(Character, boolean)[16] | 0 s |
|  | testMakeColumnQueueWithMultipleTrailingLineBreaks | 0 s |
|  | testMakeColumnQueue | 0.001 s |
|  | testSetIndent | 0 s |
|  | testindexOfWrapPos | 0 s |
|  | testAppend | 0 s |
|  | testAppendList | 0 s |
|  | testResize | 0 s |
|  | testAppendTable | 0.001 s |
|  | testAppendTitle | 0 s |
|  | testResizeTableFormat | 0 s |
|  | testAppendHeader | 0 s |

<a id="surefire--xhtmlhelpappendabletest"></a>

### XhtmlHelpAppendableTest

|  |  |  |
| --- | --- | --- |
|  | testAppendTitleTest | 0.010 s |
|  | testAppendTableTest | 0.005 s |
|  | testAppendParagraphTest | 0 s |
|  | testAppendHeaderTest | 0 s |
|  | testAppendListTest | 0.001 s |
|  | testAppendParagraphFormatTest | 0.003 s |

<a id="surefire--disablepartialmatchingtest"></a>

### DisablePartialMatchingTest

|  |  |  |
| --- | --- | --- |
|  | testDisablePartialMatching | 0 s |
|  | testRegularPartialMatching | 0 s |

<a id="surefire--bugcli325test"></a>

### BugCLI325Test

|  |  |  |
| --- | --- | --- |
|  | testCli325 | 0 s |

<a id="surefire--gnuparsertest"></a>

### GnuParserTest

|  |  |  |
| --- | --- | --- |
|  | testSimpleLong | 0 s |
|  | testSimpleShort | 0 s |
|  | testLongOptionQuoteHandling | 0 s |
|  | testOptionalArgsOptionBuilder | 0 s |
|  | testMissingRequiredOption | 0 s |
|  | testShortWithoutEqual | 0 s |
|  | testReuseOptionsTwice | 0 s |
|  | testMissingRequiredGroup | 0 s |
|  | testOptionGroupLong | 0 s |
|  | testLongOptionWithEqualsQuoteHandling | 0 s |
|  | testMissingRequiredOptions | 0 s |
|  | testPropertyOverrideValues | 0.001 s |
|  | testStopAtNonOptionLong | 0 s |
|  | testNegativeArgument | 0 s |
|  | testOptionalArgsOptionDotBuilder | 0 s |
|  | testStopAtUnexpectedArg | 0 s |
|  | testOptionGroup | 0 s |
|  | testLongWithoutEqualDoubleDash | 0 s |
|  | testPropertyOptionSingularValue | 0 s |
|  | testPropertyOptionMultipleValues | 0 s |
|  | testMissingArg | 0.001 s |
|  | testPropertyOptionFlags | 0 s |
|  | testPropertyOptionGroup | 0 s |
|  | testAmbiguousArgParsing | 0 s |
|  | testMultipleWithLong | 0 s |
|  | testMultipleWithNull | 0 s |
|  | testUnrecognizedOption | 0 s |
|  | testPropertyOptionUnexpected | 0 s |
|  | testSingleDash | 0 s |
|  | testShortWithEqual | 0 s |
|  | testWithRequiredOption | 0 s |
|  | testUnlimitedArgs | 0 s |
|  | testPropertyOptionRequired | 0 s |
|  | testOptionAndRequiredOption | 0 s |
|  | testLongWithEqualDoubleDash | 0 s |
|  | testStopAtNonOptionShort | 0 s |
|  | testLongWithEqualSingleDash | 0 s |
|  | testShortOptionConcatenatedQuoteHandling | 0 s |
|  | testMultiple | 0 s |
|  | testArgumentStartingWithHyphen | 0.001 s |
|  | testPropertiesOption1 | 0 s |
|  | testPropertiesOption2 | 0 s |
|  | testDoubleDash1 | 0 s |
|  | testStopAtExpectedArg | 0 s |
|  | testShortOptionQuoteHandling | 0 s |
|  | [testStopBursting2](#surefire--org.apache.commons.cli.gnuparsertest.teststopbursting2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testStopBursting2');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testAmbiguousLongWithoutEqualSingleDash](#surefire--org.apache.commons.cli.gnuparsertest.testambiguouslongwithoutequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testMissingArgWithBursting](#surefire--org.apache.commons.cli.gnuparsertest.testmissingargwithbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testMissingArgWithBursting');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testShortWithUnexpectedArgument](#surefire--org.apache.commons.cli.gnuparsertest.testshortwithunexpectedargument) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testShortWithUnexpectedArgument');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testStopBursting](#surefire--org.apache.commons.cli.gnuparsertest.teststopbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testStopBursting');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testPartialLongOptionSingleDash](#surefire--org.apache.commons.cli.gnuparsertest.testpartiallongoptionsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testPartialLongOptionSingleDash');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testLongWithoutEqualSingleDash](#surefire--org.apache.commons.cli.gnuparsertest.testlongwithoutequalsingledash) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testLongWithoutEqualSingleDash');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testUnrecognizedOptionWithBursting](#surefire--org.apache.commons.cli.gnuparsertest.testunrecognizedoptionwithbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnrecognizedOptionWithBursting');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testBursting](#surefire--org.apache.commons.cli.gnuparsertest.testbursting) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testBursting');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testAmbiguousPartialLongOption1](#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption1');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testAmbiguousPartialLongOption2](#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption2');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testAmbiguousPartialLongOption3](#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption3) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption3');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testAmbiguousPartialLongOption4](#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption4) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption4');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testNegativeOption](#surefire--org.apache.commons.cli.gnuparsertest.testnegativeoption) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testNegativeOption');) | 0 s |
| - | not supported by the GnuParser (CLI-184) | - |
|  | [testLongWithUnexpectedArgument1](#surefire--org.apache.commons.cli.gnuparsertest.testlongwithunexpectedargument1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument1');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testLongWithUnexpectedArgument2](#surefire--org.apache.commons.cli.gnuparsertest.testlongwithunexpectedargument2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument2');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testUnambiguousPartialLongOption1](#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption1) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption1');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testUnambiguousPartialLongOption2](#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption2');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testUnambiguousPartialLongOption3](#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption3) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption3');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testUnambiguousPartialLongOption4](#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption4) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption4');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testDoubleDash2](#surefire--org.apache.commons.cli.gnuparsertest.testdoubledash2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testDoubleDash2');) | 0 s |
| - | not supported by the GnuParser | - |
|  | [testAmbiguousLongWithoutEqualSingleDash2](#surefire--org.apache.commons.cli.gnuparsertest.testambiguouslongwithoutequalsingledash2) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash2');) | 0 s |
| - | not supported by the GnuParser | - |

<a id="surefire--deprecatedattributestest"></a>

### DeprecatedAttributesTest

|  |  |  |
| --- | --- | --- |
|  | testDefaultToString | 0 s |
|  | testBuilderNonDefaults | 0 s |
|  | testDefaultBuilder | 0 s |
|  | testBuilderNonDefaultsToString | 0 s |

<a id="surefire--bugstest"></a>

### BugsTest

|  |  |  |
| --- | --- | --- |
|  | test13666\_Builder | 0 s |
|  | test11456 | 0 s |
|  | test11457 | 0 s |
|  | test11458 | 0 s |
|  | test11680 | 0.001 s |
|  | test12210 | 0 s |
|  | test13425 | 0 s |
|  | test13666 | 0 s |
|  | test13935 | 0 s |
|  | test14786 | 0.001 s |
|  | test15046 | 0 s |
|  | test15648 | 0 s |
|  | test31148 | 0 s |

<a id="surefire--missingoptionexceptiontest"></a>

### MissingOptionExceptionTest

|  |  |  |
| --- | --- | --- |
|  | testGetMissingOptions | 0 s |
|  | testGetMessage | 0 s |

<a id="surefire--optiongrouptest"></a>

### OptionGroupTest

|  |  |  |
| --- | --- | --- |
|  | testTwoOptionsFromDifferentGroup | 0 s |
|  | testNoOptionsExtraArgs | 0.001 s |
|  | testGetNames | 0 s |
|  | testTwoValidOptions | 0 s |
|  | testSingleOption | 0 s |
|  | testToString | 0 s |
|  | testTwoOptionsFromGroup | 0.001 s |
|  | testTwoValidLongOptions | 0 s |
|  | testSingleOptionFromGroup | 0 s |
|  | testTwoOptionsFromGroupWithProperties | 0 s |
|  | testTwoLongOptionsFromGroup | 0 s |
|  | testSingleLongOption | 0 s |
|  | testValidLongOnlyOptions | 0 s |

<a id="surefire--solrcreatetooltest"></a>

### SolrCreateToolTest

|  |  |  |
| --- | --- | --- |
|  | testHelpFormatter | 0.001 s |
|  | testHelpFormatterDeprecated | 0 s |

<a id="surefire--valuestest"></a>

### ValuesTest

|  |  |  |
| --- | --- | --- |
|  | testTwoArgValues | 0 s |
|  | testShortArgs | 0 s |
|  | testCharSeparator | 0 s |
|  | testExtraArgs | 0.001 s |
|  | testShortArgsWithValue | 0 s |
|  | testComplexValues | 0 s |
|  | testMultipleArgValues | 0 s |

<a id="surefire--convertertests"></a>

### ConverterTests

|  |  |  |
| --- | --- | --- |
|  | testUrl | 0.060 s |
|  | testClass | 0 s |
|  | testDate | 0.001 s |
|  | testFile | 0 s |
|  | testNumber(String, Number)[1] | 0 s |
|  | testNumber(String, Number)[2] | 0 s |
|  | testNumber(String, Number)[3] | 0 s |
|  | testNumber(String, Number)[4] | 0 s |
|  | testNumber(String, Number)[5] | 0 s |
|  | testNumber(String, Number)[6] | 0 s |
|  | testNumber(String, Number)[7] | 0.001 s |
|  | testNumber(String, Number)[8] | 0 s |
|  | testNumber(String, Number)[9] | 0 s |
|  | testObject | 0 s |

<a id="surefire--utiltest-2"></a>

### UtilTest

|  |  |  |
| --- | --- | --- |
|  | testRtrim(Character, boolean)[1] | 0.001 s |
|  | testRtrim(Character, boolean)[2] | 0 s |
|  | testRtrim(Character, boolean)[3] | 0 s |
|  | testRtrim(Character, boolean)[4] | 0 s |
|  | testRtrim(Character, boolean)[5] | 0 s |
|  | testRtrim(Character, boolean)[6] | 0 s |
|  | testRtrim(Character, boolean)[7] | 0 s |
|  | testRtrim(Character, boolean)[8] | 0 s |
|  | testRtrim(Character, boolean)[9] | 0 s |
|  | testRtrim(Character, boolean)[10] | 0 s |
|  | testRtrim(Character, boolean)[11] | 0 s |
|  | testRtrim(Character, boolean)[12] | 0 s |
|  | testRtrim(Character, boolean)[13] | 0 s |
|  | testRtrim(Character, boolean)[14] | 0 s |
|  | testRtrim(Character, boolean)[15] | 0 s |
|  | testRtrim(Character, boolean)[16] | 0.001 s |
|  | testFindNonWhitespacePos | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[1] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[2] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[3] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[4] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[5] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[6] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[7] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[8] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[9] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[10] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[11] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[12] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[13] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[14] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[15] | 0 s |
|  | testFindNonWhitespacePos(Character, boolean)[16] | 0 s |
|  | testIsEmpty | 0 s |

<a id="surefire--textstyletests"></a>

### TextStyleTests

|  |  |  |
| --- | --- | --- |
|  | testPad(TextStyle, String, String)[1] | 0.001 s |
|  | testPad(TextStyle, String, String)[2] | 0 s |
|  | testPad(TextStyle, String, String)[3] | 0 s |
|  | testPad(TextStyle, String, String)[4] | 0 s |
|  | testPad(TextStyle, String, String)[5] | 0 s |
|  | testPad(TextStyle, String, String)[6] | 0 s |
|  | testPad(TextStyle, String, String)[7] | 0.001 s |
|  | testPad(TextStyle, String, String)[8] | 0 s |
|  | testPad(TextStyle, String, String)[9] | 0 s |
|  | testPad(TextStyle, String, String)[10] | 0 s |
|  | testPad(TextStyle, String, String)[11] | 0 s |
|  | testPad(TextStyle, String, String)[12] | 0 s |
|  | testDefaultStyle | 0 s |

<a id="surefire--failure-details"></a>

## Failure Details

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

|  |  |
| --- | --- |
|  | testAmbiguousLongWithoutEqualSingleDash |
| - | skipped: not supported by the PosixParser |
|  | testLongWithoutEqualSingleDash |
| - | skipped: not supported by the PosixParser |
|  | testAmbiguousPartialLongOption4 |
| - | skipped: not supported by the PosixParser |
|  | testShortWithEqual |
| - | skipped: not supported by the PosixParser |
|  | testNegativeOption |
| - | skipped: not supported by the PosixParser (CLI-184) |
|  | testLongWithUnexpectedArgument1 |
| - | skipped: not supported by the PosixParser |
|  | testLongWithEqualSingleDash |
| - | skipped: not supported by the PosixParser |
|  | testUnambiguousPartialLongOption4 |
| - | skipped: not supported by the PosixParser |
|  | testDoubleDash2 |
| - | skipped: not supported by the PosixParser |
|  | testAmbiguousLongWithoutEqualSingleDash2 |
| - | skipped: not supported by the PosixParser |
|  | testLongOptionWithEqualsQuoteHandling |
| - | skipped: Test case handled in the parameterized tests as "DEFAULT behavior" |
|  | testShortOptionConcatenatedQuoteHandling |
| - | skipped: Test case handled in the parameterized tests as "DEFAULT behavior" |
|  | testStopBursting2 |
| - | skipped: not supported by the BasicParser |
|  | testShortWithoutEqual |
| - | skipped: not supported by the BasicParser |
|  | testLongOptionWithEqualsQuoteHandling |
| - | skipped: not supported by the BasicParser |
|  | testAmbiguousLongWithoutEqualSingleDash |
| - | skipped: not supported by the BasicParser |
|  | testMissingArgWithBursting |
| - | skipped: not supported by the BasicParser |
|  | testStopBursting |
| - | skipped: not supported by the BasicParser |
|  | testPartialLongOptionSingleDash |
| - | skipped: not supported by the BasicParser |
|  | testLongWithoutEqualSingleDash |
| - | skipped: not supported by the BasicParser |
|  | testUnrecognizedOptionWithBursting |
| - | skipped: not supported by the BasicParser |
|  | testBursting |
| - | skipped: not supported by the BasicParser |
|  | testAmbiguousPartialLongOption1 |
| - | skipped: not supported by the BasicParser |
|  | testAmbiguousPartialLongOption2 |
| - | skipped: not supported by the BasicParser |
|  | testAmbiguousPartialLongOption3 |
| - | skipped: not supported by the BasicParser |
|  | testAmbiguousPartialLongOption4 |
| - | skipped: not supported by the BasicParser |
|  | testShortWithEqual |
| - | skipped: not supported by the BasicParser |
|  | testNegativeOption |
| - | skipped: not supported by the BasicParser (CLI-184) |
|  | testLongWithEqualDoubleDash |
| - | skipped: not supported by the BasicParser |
|  | testLongWithEqualSingleDash |
| - | skipped: not supported by the BasicParser |
|  | testUnambiguousPartialLongOption1 |
| - | skipped: not supported by the BasicParser |
|  | testUnambiguousPartialLongOption2 |
| - | skipped: not supported by the BasicParser |
|  | testUnambiguousPartialLongOption3 |
| - | skipped: not supported by the BasicParser |
|  | testUnambiguousPartialLongOption4 |
| - | skipped: not supported by the BasicParser |
|  | testShortOptionConcatenatedQuoteHandling |
| - | skipped: not supported by the BasicParser |
|  | testPropertiesOption1 |
| - | skipped: not supported by the BasicParser |
|  | testPropertiesOption2 |
| - | skipped: not supported by the BasicParser |
|  | testDoubleDash2 |
| - | skipped: not supported by the BasicParser |
|  | testAmbiguousLongWithoutEqualSingleDash2 |
| - | skipped: not supported by the BasicParser |
|  | testStopBursting2 |
| - | skipped: not supported by the GnuParser |
|  | testAmbiguousLongWithoutEqualSingleDash |
| - | skipped: not supported by the GnuParser |
|  | testMissingArgWithBursting |
| - | skipped: not supported by the GnuParser |
|  | testShortWithUnexpectedArgument |
| - | skipped: not supported by the GnuParser |
|  | testStopBursting |
| - | skipped: not supported by the GnuParser |
|  | testPartialLongOptionSingleDash |
| - | skipped: not supported by the GnuParser |
|  | testLongWithoutEqualSingleDash |
| - | skipped: not supported by the GnuParser |
|  | testUnrecognizedOptionWithBursting |
| - | skipped: not supported by the GnuParser |
|  | testBursting |
| - | skipped: not supported by the GnuParser |
|  | testAmbiguousPartialLongOption1 |
| - | skipped: not supported by the GnuParser |
|  | testAmbiguousPartialLongOption2 |
| - | skipped: not supported by the GnuParser |
|  | testAmbiguousPartialLongOption3 |
| - | skipped: not supported by the GnuParser |
|  | testAmbiguousPartialLongOption4 |
| - | skipped: not supported by the GnuParser |
|  | testNegativeOption |
| - | skipped: not supported by the GnuParser (CLI-184) |
|  | testLongWithUnexpectedArgument1 |
| - | skipped: not supported by the GnuParser |
|  | testLongWithUnexpectedArgument2 |
| - | skipped: not supported by the GnuParser |
|  | testUnambiguousPartialLongOption1 |
| - | skipped: not supported by the GnuParser |
|  | testUnambiguousPartialLongOption2 |
| - | skipped: not supported by the GnuParser |
|  | testUnambiguousPartialLongOption3 |
| - | skipped: not supported by the GnuParser |
|  | testUnambiguousPartialLongOption4 |
| - | skipped: not supported by the GnuParser |
|  | testDoubleDash2 |
| - | skipped: not supported by the GnuParser |
|  | testAmbiguousLongWithoutEqualSingleDash2 |
| - | skipped: not supported by the GnuParser |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/rat-report.html -->

<!-- page_index: 10 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

# RAT (Release Audit Tool) results

The following document contains the results of [RAT (Release Audit Tool)](https://creadur.apache.org/rat/apache-rat-plugin/) Apache Creadur RAT::Plugin4Maven 0.17 (Apache Software Foundation).

```
*****************************************************
Summary
*****************************************************
Generated at: 2025-11-20T08:56:24-05:00
    by Apache Creadur RAT::Core 0.17 (Apache Software Foundation)

-----------------------------------------------------
Counters
-----------------------------------------------------
    (Entries starting with '!' exceed the minimum or maximum values)
  Approved:           120    A count of approved licenses.
  Archives:           0    A count of archive files.
  Binaries:           9    A count of binary files.
  Document types:     4    A count of distinct document types.
  Ignored:            11    A count of ignored files.
  License categories: 1    A count of distinct license categories.
  License names:      1    A count of distinct license names.
  Notices:            3    A count of notice files.
  Standards:          120    A count of standard files.
  Unapproved:         0    A count of unapproved licenses.
  Unknown:            0    A count of unknown file types.


-----------------------------------------------------
Licenses detected
-----------------------------------------------------

Apache License 2.0: 120 

-----------------------------------------------------
License Categories detected
-----------------------------------------------------

AL   : 120 

-----------------------------------------------------
Document Types detected
-----------------------------------------------------

BINARY: 9 
IGNORED: 11 
NOTICE: 3 
STANDARD: 120 

*****************************************************
Detail
*****************************************************

  Documents with unapproved licenses will start with a '!'
  The first character on the next line identifies the document type.
   
   char         type
    A       Archive file
    B       Binary file
    I       Ignored file
    N       Notice file
    S       Standard file
    U       Unknown file.
  
  /.asf.yaml
  I         text/x-yaml    

  /.classpath
  I         text/plain    

  /.git
  I         application/octet-stream     (directory)

  /.gitattributes
  I         application/octet-stream    

  /.github
  I         application/octet-stream     (directory)

  /.gitignore
  I         application/octet-stream    

  /.project
  I         text/plain    

  /.settings
  I         application/octet-stream     (directory)

  /CODE_OF_CONDUCT.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /CONTRIBUTING.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /LICENSE.txt
  N         text/plain    ISO-8859-1

  /NOTICE.txt
  N         text/plain    ISO-8859-1

  /README.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /RELEASE-NOTES.txt
  N         text/plain    UTF-8

  /SECURITY.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /pom.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /site-content
  I         application/octet-stream     (directory)

  /src/assembly/bin.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/src.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/changes/changes.xml
  S         application/xml    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/changes/release-notes.vm
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/checkstyle-suppressions.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/checkstyle.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/spotbugs-exclude-filter.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/AlreadySelectedException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/AmbiguousOptionException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/BasicParser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/Char.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/CommandLine.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/CommandLineParser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/Converter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/DefaultParser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/DeprecatedAttributes.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/GnuParser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/HelpFormatter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/MissingArgumentException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/MissingOptionException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/Option.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/OptionBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/OptionGroup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/OptionValidator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/Options.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/ParseException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/Parser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/PatternOptionBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/PosixParser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/TypeHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/UnrecognizedOptionException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/Util.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/doc-files/leaf.svg
  S         image/svg+xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/doc-files/logo.png
  B         image/png    

  /src/main/java/org/apache/commons/cli/help/AbstractHelpFormatter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/FilterHelpAppendable.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/HelpAppendable.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/HelpFormatter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/OptionFormatter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/TableDefinition.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/TextHelpAppendable.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/TextStyle.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/Util.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/help/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/cli/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/javadoc/overview.html
  S         text/html    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/media/commons-logo-component-100.xcf
  B         image/x-xcf    

  /src/media/commons-logo-component.xcf
  B         image/x-xcf    

  /src/media/logo.png
  B         image/png    

  /src/site/resources/.htaccess
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/download_cli.cgi
  I         text/x-cgi    

  /src/site/resources/images/1x1.gif
  B         image/gif    

  /src/site/resources/images/logo.png
  B         image/png    

  /src/site/resources/images/options.png
  B         image/png    

  /src/site/resources/images/svg/commandlines.svg
  S         image/svg+xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/images/svg/diagrams-cli2.js
  B         application/javascript    

  /src/site/resources/images/svg/diagrams.css
  S         text/css    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/images/svg/diagrams.js
  B         application/javascript    

  /src/site/resources/images/svg/options.svg
  S         image/svg+xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/images/svg/util.svg
  S         image/svg+xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/profile.jacoco
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/site.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/download_cli.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/issue-tracking.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/mail-lists.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release_1_0.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release_1_2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release_1_3.xml
  S         application/xml    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release_1_3_1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release_1_4.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/security.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/upgrading-1.0-to-1.1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/AbstractParserTestCase.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/AlreadySelectedExceptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/ApplicationTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/ArgumentIsOptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/BasicParserTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/CommandLineTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/ConverterTests.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/DefaultParserTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/DeprecatedAttributesTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/DisablePartialMatchingTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/GnuParserTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/HelpFormatterTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/MissingOptionExceptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/OptionBuilderTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/OptionCountTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/OptionGroupTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/OptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/OptionValidatorTest.java
  S         text/x-java-source    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/OptionsTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/ParseExceptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/PatternOptionBuilderTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/PosixParserTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/SolrCliTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/SolrCreateToolTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/TypeHandlerTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/UnrecognizedOptionExceptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/UtilTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/ValueTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/ValuesTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI133Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI13Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI148Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI162Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI18Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI252Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI265Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI266Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI312Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI325Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugCLI71Test.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/bug/BugsTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/example/AptHelpAppendable.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/example/AptHelpAppendableTest.java
  S         text/x-java-source    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/example/WeirdOptionFormat.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/example/XhtmlHelpAppendable.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/example/XhtmlHelpAppendableTest.java
  S         text/x-java-source    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/help/HelpFormatterTest.java
  S         text/x-java-source    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/help/OptionFormatterTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/help/TextHelpAppendableTest.java
  S         text/x-java-source    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/help/TextStyleTests.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/cli/help/UtilTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/org/apache/commons/cli/existing-readable.file
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /target
  I         application/octet-stream     (directory)
```

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/japicmp.html -->

<!-- page_index: 11 -->

# Apache Commons CLI

Comparing source compatibility of commons-cli-1.11.0.jar against commons-cli-1.10.0.jar

|  |  |
| --- | --- |
| Old: | commons-cli-1.10.0.jar |
| New: | commons-cli-1.11.0.jar |
| Created: | 2025-11-20T08:56:24.912-0500 |
| Access modifier filter: | PROTECTED |
| Only modifications: | true |
| Only binary incompatible modifications: | false |
| Ignore missing classes: | false |
| Includes: | all |
| Excludes: | n.a. |
| Semantic Versioning: | 0.0.1 |

- [Classes](#japicmp--toc)

Classes:

| Status | Fully Qualified Name |
| --- | --- |
| MODIFIED | [org.apache.commons.cli.CommandLine](#japicmp--org.apache.commons.cli.commandline) |
| MODIFIED | [org.apache.commons.cli.help.AbstractHelpFormatter](#japicmp--org.apache.commons.cli.help.abstracthelpformatter) |
| MODIFIED | [org.apache.commons.cli.Option](#japicmp--org.apache.commons.cli.option) |
| MODIFIED | [org.apache.commons.cli.PosixParser](#japicmp--org.apache.commons.cli.posixparser) |

Binary incompatible changes are marked with (!) while source incompatible changes are marked with (\*).

MODIFIED
 (Serializable compatible)
public
class
org.apache.commons.cli.CommandLine
[top](#japicmp--toc)

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | true | 7076145126846789520 | 1 |
| New | true | 8065023836524799982 | 1 |

Methods:

<table>
<thead>
<tr>
<td>Status</td>
<td>Modifier</td>
<td>Generic Templates</td>
<td>Type</td>
<td>Method</td>
<td>Exceptions</td>
<td>Compatibility Changes:</td>
<td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td><span>int</span></td>
<td>getOptionCount(<span>char</span>)</td>
<td></td>
<td><div>
<span>Compatibility Changes:</span>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr><td>METHOD_ADDED_TO_PUBLIC_CLASS</td></tr>
</tbody>
</table>
</div>
</td>
<td><table>
<thead>
<tr>
<td>Old file</td>
<td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>
			n.a.
		</td>
<td>
			242
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td><span>int</span></td>
<td>getOptionCount(<span>org.apache.commons.cli.Option</span>)</td>
<td></td>
<td><div>
<span>Compatibility Changes:</span>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr><td>METHOD_ADDED_TO_PUBLIC_CLASS</td></tr>
</tbody>
</table>
</div>
</td>
<td><table>
<thead>
<tr>
<td>Old file</td>
<td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>
			n.a.
		</td>
<td>
			253
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td><span>int</span></td>
<td>getOptionCount(<span>java.lang.String</span>)</td>
<td></td>
<td><div>
<span>Compatibility Changes:</span>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr><td>METHOD_ADDED_TO_PUBLIC_CLASS</td></tr>
</tbody>
</table>
</div>
</td>
<td><table>
<thead>
<tr>
<td>Old file</td>
<td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>
			n.a.
		</td>
<td>
			264
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED
public
abstract
class
org.apache.commons.cli.help.AbstractHelpFormatter
[top](#japicmp--toc)

Methods:

<table>
<thead>
<tr>
<td>Status</td>
<td>Modifier</td>
<td>Generic Templates</td>
<td>Type</td>
<td>Method</td>
<td>Exceptions</td>
<td>Compatibility Changes:</td>
<td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>MODIFIED</span></td>
<td><span>NON_FINAL (&lt;- FINAL) </span>
<span>public</span>
</td>
<td>n.a.</td>
<td><span>void</span></td>
<td>printHelp(<span>java.lang.String</span>, <span>java.lang.String</span>, <span>org.apache.commons.cli.Options</span>, <span>java.lang.String</span>, <span>boolean</span>)</td>
<td><table>
<thead>
<tr>
<td>Status:</td>
<td>Name:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>UNCHANGED</span></td>
<td>java.io.IOException</td>
</tr>
</tbody>
</table>
</td>
<td>n.a.</td>
<td><table>
<thead>
<tr>
<td>Old file</td>
<td>New file</td>
</tr>
</thead>
<tbody>
<tr>
<td>
			327
		</td>
<td>
			315
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED
 (Serializable compatible)
public
class
org.apache.commons.cli.Option
[top](#japicmp--toc)

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | true | 15783033580600091 | 1 |
| New | true | 3006244500561563562 | 1 |

MODIFIED
public
class
org.apache.commons.cli.PosixParser
[top](#japicmp--toc)

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| UNCHANGED | org.apache.commons.cli.Parser | n.a. |

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/checkstyle.html -->

<!-- page_index: 12 -->

<a id="checkstyle--checkstyle-results"></a>

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 12.1.0 with /Users/garygregory/git/commons/commons-cli/src/conf/checkstyle.xml ruleset.

<a id="checkstyle--summary"></a>

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 90 | 0 | 0 | 0 |

<a id="checkstyle--files"></a>

## Files

| File | I | W | E |
| --- | --- | --- | --- |

<a id="checkstyle--details"></a>

## Details

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/spotbugs.html -->

<!-- page_index: 13 -->

<a id="spotbugs--spotbugs-bug-detector-report"></a>

# SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.9.8*

Threshold is *medium*

Effort is *default*

<a id="spotbugs--summary"></a>

# Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 56 | 0 | 0 | 0 |

<a id="spotbugs--files"></a>

# Files

| Class | Bugs |
| --- | --- |

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/cpd.html -->

<!-- page_index: 14 -->

<a id="cpd--cpd-results"></a>

# CPD Results

The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 7.17.0.

<a id="cpd--duplications"></a>

## Duplications

<table class="bodyTable">
<tr>
<th>File</th>
<th>Line</th></tr>
<tr>
<td>org/apache/commons/cli/DefaultParser.java</td>
<td><a href="https://commons.apache.org/proper/commons-cli/xref/org/apache/commons/cli/DefaultParser.html#L501">501</a></td></tr>
<tr>
<td>org/apache/commons/cli/Parser.java</td>
<td><a href="https://commons.apache.org/proper/commons-cli/xref/org/apache/commons/cli/Parser.html#L271">271</a></td></tr>
<tr>
<td colspan="2">
<pre>private void handleProperties(final Properties properties) throws ParseException {
        if (properties == null) {
            return;
        }
        for (final Enumeration&lt;?&gt; e = properties.propertyNames(); e.hasMoreElements();) {
            final String option = e.nextElement().toString();
            final Option opt = options.getOption(option);
            if (opt == null) {
                throw new UnrecognizedOptionException("Default option wasn't defined", option);
            }
            // if the option is part of a group, check if another option of the group has been selected
            final OptionGroup optionGroup = options.getOptionGroup(opt);
            final boolean selected = optionGroup != null &amp;&amp; optionGroup.isSelected();
            if (!cmd.hasOption(option) &amp;&amp; !selected) {
                // get the value from the properties
                final String value = properties.getProperty(option);

                if (opt.hasArg()) {
                    if (opt.isValuesEmpty()) {</pre></td></tr></table>

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/pmd.html -->

<!-- page_index: 15 -->

<a id="pmd--pmd-results"></a>

# PMD Results

The following document contains the results of [PMD](https://pmd.github.io) 7.17.0.

PMD found no problems in your source code.

<a id="pmd--suppressed-violations"></a>

## Suppressed Violations

| Filename | Rule message | Suppression type | Reason |
| --- | --- | --- | --- |
| org/apache/commons/cli/HelpFormatter.java | Avoid empty catch blocks | //nopmd |  |
| org/apache/commons/cli/Parser.java | Avoid empty catch blocks | //nopmd |  |

---
