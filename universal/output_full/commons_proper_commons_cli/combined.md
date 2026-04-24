# Project Information

## Navigation

- Commons CLI
  - [About](#index)
  - [Asking Questions](https://commons.apache.org/proper/commons-cli/mail-lists.html)
  - [Release History](#changes)
  - [Issue Tracking](#issue-management)
  - [Dependency Management](#dependency-info)
  - [Sources](#scm)
  - [Security](https://commons.apache.org/proper/commons-cli/security.html)
  - [License](https://www.apache.org/licenses/LICENSE-2.0)
  - [Code of Conduct](https://www.apache.org/foundation/policies/conduct.html)
  - [Download](https://commons.apache.org/proper/commons-bcel/download_bcel.cgi)
  - Javadoc
    - [Javadoc Current](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
    - [Javadoc Archive](https://javadoc.io/doc/commons-cli/commons-cli/)
- User Guide
  - [Getting started](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
  - [Using CLI](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
  - [Option properties](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
  - [Javadoc](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
  - [Javadoc Archive](https://javadoc.io/doc/commons-cli/commons-cli/latest/index.html)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [Issue Management](#issue-management)
    - [Mailing Lists](https://commons.apache.org/proper/commons-cli/mailing-lists.html)
    - [Maven Coordinates](#dependency-info)
    - [Dependency Management](#dependency-management)
    - [Dependencies](#dependencies)
    - [Dependency Convergence](#dependency-convergence)
    - [CI Management](#ci-management)
    - [Distribution Management](#distribution-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes)
    - [JIRA Report](#jira-changes)
    - [Javadoc](https://commons.apache.org/proper/commons-cli/apidocs/index.html)
    - [Source Xref](https://commons.apache.org/proper/commons-cli/xref/index.html)
    - [Test Source Xref](https://commons.apache.org/proper/commons-cli/xref-test/index.html)
    - [Surefire](#surefire)
    - [RAT Report](#rat-report)
    - [JaCoCo](https://commons.apache.org/proper/commons-cli/jacoco/index.html)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [SpotBugs](#spotbugs)
    - [CPD](#cpd)
    - [PMD](#pmd)
- Commons
  - [Home](https://commons.apache.org/)
  - [License](https://www.apache.org/licenses/)
  - [Components](https://commons.apache.org/components.html)
  - [Sandbox](https://commons.apache.org/sandbox/index.html)
  - [Dormant](https://commons.apache.org/dormant/index.html)
- General Information
  - [Security](https://commons.apache.org/security.html)
  - [Volunteering](https://commons.apache.org/volunteering.html)
  - [Contributing Patches](https://commons.apache.org/patches.html)
  - [Building Components](https://commons.apache.org/building.html)
  - [Commons Parent POM](https://commons.apache.org/commons-parent-pom.html)
  - [Commons Build Plugin](https://commons.apache.org/build-plugin/index.html)
  - [Commons Release Plugin](https://commons.apache.org/release-plugin/index.html)
  - [Site Publication](https://commons.apache.org/site-publish.html)
  - [Releasing Components](https://commons.apache.org/releases/index.html)
  - [Wiki](https://cwiki.apache.org/confluence/display/commons/FrontPage)
- ASF
  - [How the ASF works](https://www.apache.org/foundation/how-it-works.html)
  - [Get Involved](https://www.apache.org/foundation/getinvolved.html)
  - [Developer Resources](https://www.apache.org/dev/)
  - [Code of Conduct](https://www.apache.org/foundation/policies/conduct.html)
  - [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
  - [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
  - [Thanks](https://www.apache.org/foundation/thanks.html)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/index.html -->

<!-- page_index: 1 -->

# Apache Commons CLI

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Apache_Commons_CLI"></a>
<h1>Apache Commons CLI</h1>
<p>
        The Apache Commons CLI library provides an API for parsing command-line options passed to an application.
        It can also print help detailing the options available for that application.
      </p>
<p>
        Commons CLI supports different types of options:
      </p>
<ul>
<li>POSIX like options, for example <code>tar -zxvf foo.tar.gz</code></li>
<li>GNU like long options, for example <code>du --human-readable --max-depth=1</code></li>
<li>Java like properties, for example <code>java -Djava.awt.headless=true -Djava.net.useSystemProxies=true Foo</code></li>
<li>Short options with value attached, for example <code>gcc -O2 foo.c</code></li>
<li>long options with single hyphen, for example <code>ant -projecthelp</code></li>
</ul>
<p>
        A typical help message displayed by Commons CLI looks like this:
      </p>
<pre><code>
usage: ls
 -A,--almost-all          do not list implied . and ..
 -a,--all                 do not hide entries starting with .
 -B,--ignore-backups      do not list implied entried ending with ~
 -b,--escape              print octal escapes for nongraphic characters
    --block-size &lt;SIZE&gt;   use SIZE-byte blocks
 -c                       with -lt: sort by, and show, ctime (time of last
                          modification of file status information) with
                          -l:show ctime and sort by name otherwise: sort
                          by ctime
 -C                       list entries by columns
      </code></pre>
<p>
        Check out the <a href="https://commons.apache.org/proper/commons-cli/introduction.html">introduction</a> page for a detailed presentation.
      </p>
</section>
<section><a id="Documentation"></a>
<h1>Documentation</h1>
<p>
        A full <a href="https://commons.apache.org/proper/commons-cli/introduction.html">User's Guide</a> is available
        as are various <a href="#project-reports">project reports</a>.
      </p>
<p>
        The Javadoc API documents are available online:
      </p>
<p>
        The <a href="#scm">source repository</a> can be
        <a href="https://gitbox.apache.org/repos/asf?p=commons-cli.git">browsed</a>.
      </p>
</section>
<section><a id="Releases"></a>
<h1>Releases</h1>
<p>
<a href="https://commons.apache.org/cli/download_cli.cgi">Download</a> the latest version.

        The <a href="#changes">release notes</a> are also available.
      </p>
<p>
        For previous releases, see the <a href="https://archive.apache.org/dist/commons/cli/">Apache Archive</a>.
      </p>
</section>
<section><a id="Support"></a>
<h1>Support</h1>
<p>
        The <a href="https://commons.apache.org/proper/commons-cli/mail-lists.html">commons mailing lists</a> act as the main support forum. The user list
        is suitable for most library usage queries. The dev list is intended for the development discussion. Please
        remember that the lists are shared between all commons components, so prefix your email subject by
        <code>[cli]</code>.
      </p>
<p>
        Issues may be reported via the <a href="https://commons.apache.org/proper/commons-cli/issue-tracking.html">ASF JIRA</a>.
      </p>
</section>
<section><a id="CLI_2.3F"></a>
<h1>CLI 2?</h1>
<p>
        Commons CLI 1.0 was formed from the merger of ideas and code from three different libraries -
        Werken, Avalon and Optz. In dealing with the bugs and the feature requests a freshly designed and not
        backwards compatible CLI 2 was created in 2004, but never finished or released.
      </p>
<p>The current plan is to continue to maintain the 1.x line. The CLI2 work may be found in the Commons Sandbox. </p>
</section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/changes.html -->

<!-- page_index: 2 -->

# Apache Commons CLI Release Notes

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Apache_Commons_CLI_Release_Notes"></a>
<h1>Apache Commons CLI Release Notes</h1><section><a id="Release_History"></a>
<h2>Release History</h2>
<table>
<tr>
<th>Version</th>
<th>Date</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes--a1.11.0">1.11.0</a></td>
<td>2025-11-08</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.10.0">1.10.0</a></td>
<td>2025-07-30</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.9.0">1.9.0</a></td>
<td>2024-08-10</td>
<td>This release contains new features and bug fixes and requires Java 8 or above.</td></tr>
<tr>
<td><a href="#changes--a1.8.0">1.8.0</a></td>
<td>2024-05-18</td>
<td>This release contains new features and bug fixes and requires Java 8 or above.</td></tr>
<tr>
<td><a href="#changes--a1.7.0">1.7.0</a></td>
<td>2024-04-13</td>
<td>This release contains new features and bug fixes and requires Java 8 or above.</td></tr>
<tr>
<td><a href="#changes--a1.6.0">1.6.0</a></td>
<td>2023-10-23</td>
<td>This release contains new features and bug fixes and requires Java 8 or above.</td></tr>
<tr>
<td><a href="#changes--a1.5.0">1.5.0</a></td>
<td>2021-10-23</td>
<td>This release contains new features and bug fixes and requires Java 7 or above.</td></tr>
<tr>
<td><a href="#changes--a1.4">1.4</a></td>
<td>2017-03-09</td>
<td>This release contains new features and bug fixes and requires Java 5 or above.</td></tr>
<tr>
<td><a href="#changes--a1.3.1">1.3.1</a></td>
<td>2015-06-17</td>
<td>This release contains bug fixes and requires Java 5 or above.</td></tr>
<tr>
<td><a href="#changes--a1.3">1.3</a></td>
<td>2015-05-09</td>
<td>This release contains new features and bug fixes and requires Java 5 or above..</td></tr>
<tr>
<td><a href="#changes--a1.2">1.2</a></td>
<td>2009-03-19</td>
<td>This release contains new features and bug fixes and requires Java 5 or above.</td></tr>
<tr>
<td><a href="#changes--a1.1">1.1</a></td>
<td>2007-07-08</td>
<td>This is a maintenance release containing bug fixes.</td></tr>
<tr>
<td><a href="#changes--a1.0">1.0</a></td>
<td>2002-11-06</td>
<td>Initial release</td></tr></table></section><section><a id="a1.11.0"></a>
<h2>Release 1.11.0 – 2025-11-08</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Multiple trailing BREAK_CHAR_SET characters cause infinite loop in HelpFormatter. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-351">CLI-351</a>. Thanks to Damien Carbonne, Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix issue with groups not being reported in help output. #411. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-351">CLI-351</a>. Thanks to Damien Carbonne, Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add CommandLine.getOptionCount() to measure option repetition #396. Thanks to David Larochette, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 85 to 91 #393. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump commons-io:commons-io from 2.20.0 to 2.21.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.10.0"></a>
<h2>Release 1.10.0 – 2025-07-30</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Deprecate CommandLine.Builder() in favor of CommandLine.builder(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Deprecate DeprecatedAttributes.Builder() in favor of DeprecatedAttributes.builder(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Refactor default parser test #294. Thanks to Dávid Szigecsán.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Port to JUnit 5. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Generics for Converter should use Exception not Throwable. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Pick up maven-antrun-plugin version from parent POM org.apache:apache. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Javadoc is missing its Overview page. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Get mockito version from parent pom (#351). Thanks to Arnout Engelen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Deprecate PatternOptionBuilder.PatternOptionBuilder(). Thanks to Arnout Engelen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter infinite loop with 0 width input. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-341">CLI-341</a>. Thanks to Ruiqi Dong, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fail faster with a more precise NullPointerException: Option.processValue() throws NullPointerException when passed null value with value separator configured. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-349">CLI-349</a>. Thanks to Leo Fernandes, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fail faster with a more precise NullPointerException: DefaultParser.parse() throws NullPointerException when options parameter is null. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-344">CLI-344</a>. Thanks to Ruiqi Dong, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Options.addOptionGroup(OptionGroup) does not remove required options from requiredOpts list. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-347">CLI-347</a>. Thanks to Ruiqi Dong, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>org.apache.commons.cli.Option.Builder.get() should throw IllegalStateException instead of IllegalArgumentException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>org.apache.commons.cli.Option.processValue(String) should throw IllegalStateException instead of IllegalArgumentException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>org.apache.commons.cli.OptionBuilder.create() should throw IllegalStateException instead of IllegalArgumentException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Help formatter extension in the new package #314. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-339">CLI-339</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>CommandLine.Builder implements Supplier&lt;CommandLine&gt;. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>DefaultParser.Builder implements Supplier&lt;DefaultParser&gt;. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add CommandLine.getParsedOptionValues() #334. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-340">CLI-340</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>org.apache.commons.cli.Option.Builder implements Supplier&lt;Option&gt;. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-333">CLI-333</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add new options for parsing: ignore and skip. Thanks to Tamás Cservenák.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 72 to 85 #302, #304, #310, #315, #320, #327, #371. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>[test] Bump commons-io:commons-io from 2.16.1 to 2.20.0 #309, #337. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>[test] Bump org.apache.commons:commons-text from 1.12.0 to 1.14.0 #344. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Update site documentation to https://maven.apache.org/xsd/xdoc-2.0.xsd. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.9.0"></a>
<h2>Release 1.9.0 – 2024-08-10</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add OptionGroup.isSelected(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>You can now extend HelpFormatter.Builder. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add 'since' attribute to Option to track when an Option was introduced #292 Thanks to Claude Warren.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix Javadoc pathing #280. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-334">CLI-334</a>. Thanks to Eric Pugh.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Updated properties documentation #285. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-335">CLI-335</a>. Thanks to Claude Warren.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Deprecation not always reported #284. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-336">CLI-336</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Replace internal StringBuffer with StringBuilder. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 70 to 72 #283. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.8.0"></a>
<h2>Release 1.8.0 – 2024-05-18</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add optional HelpFormatter Function to document Deprecated options #271. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-332">CLI-332</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add PMD check to default Maven goal. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Handle reporting of deprecated options when parameters are not String type. #270. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-331">CLI-331</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Avoid throwing NullPointerException when calling CommandLineParser will null array elements. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Cleanup deprecation issues #272. Thanks to Claude Warren.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix PMD UnnecessaryFullyQualifiedName issues. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump commons-parent from 69 to 70. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.7.0"></a>
<h2>Release 1.7.0 – 2024-04-13</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Inconsistent behavior in key/value pairs (Java property style). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-312">CLI-312</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Avoid NullPointerException in Util.stripLeadingAndTrailingQuotes(String). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Awkward behavior of Option.builder() for multiple optional args. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-320">CLI-320</a>. Thanks to Paul King, Claude Warren.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Properties from multiple arguments with value separator. #237. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-325">CLI-325</a>. Thanks to Claude Warren.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix for expected textual date values. #244. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-327">CLI-327</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Option.Builder.option("") should throw IllegalArgumentException instead of ArrayIndexOutOfBoundsException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Avoid NullPointerException in CommandLine.getOptionValues(Option|String). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add and use a Converter interface and implementations without using BeanUtils #216. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-321">CLI-321</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add Maven property project.build.outputTimestamp for build reproducibility. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add '-' as an option char and implemented extensive tests #217. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-322">CLI-322</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Make adding OptionGroups and Options to existing Options easier #230. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-324">CLI-324</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Added Supplier&lt;T&gt; defaults for getParsedOptionValue #229. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-323">CLI-323</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Make Option.getKey() public #239. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-326">CLI-326</a>. Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add builder factory CommandLine#builder(). Thanks to Claude Warren, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Support "Deprecated" CLI Options #252. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-329">CLI-329</a>. Thanks to Eric Pugh, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump commons-parent from 64 to 69 #256. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Update the tests to JUnit 5 #238. Thanks to Elric, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump tests commons-io:commons-io from 2.16.0 to 2.16.1 #258. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.6.0"></a>
<h2>Release 1.6.0 – 2023-10-23</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Fix SpotBugs Error: Medium: Method intentionally throws RuntimeException. [org.apache.commons.cli.Option] At Option.java:[lines 417-423] THROWS_METHOD_THROWS_RUNTIMEEXCEPTION Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Fix SpotBugs Error: Medium: Method intentionally throws RuntimeException. [org.apache.commons.cli.Option] At Option.java:[lines 446-450] THROWS_METHOD_THROWS_RUNTIMEEXCEPTION Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Fix SpotBugs Error: Medium: Method intentionally throws RuntimeException. [org.apache.commons.cli.Option] At Option.java:[lines 474-478] THROWS_METHOD_THROWS_RUNTIMEEXCEPTION Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Use EMPTY_STRING_ARRAY constant. #102. Thanks to Ken Dombeck.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Fix site links that are broken #155. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Use Math.max() #111. Delete unused assignment #112. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>[StepSecurity] ci: Harden GitHub Actions #176. Thanks to step-security-bot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Inconsistent date format in changes report. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-318">CLI-318</a>. Thanks to Alexander Veit, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix NPE in CommandLine.resolveOption(String). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-283">CLI-283</a>. Thanks to Dilraj Singh, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>CommandLine.addOption(Option) should not allow a null Option. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-283">CLI-283</a>. Thanks to Dilraj Singh, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>CommandLine.addArgs(String) should not allow a null String. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-283">CLI-283</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Site docs: "Usage Scenarios" refers to deprecated methods. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-303">CLI-303</a>. Thanks to Julian Schilling, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>NullPointerException thrown by CommandLineParser.parse(). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-317">CLI-317</a>. Thanks to Philippe Bastiani, Sruteesh Kumar Paramata, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>StringIndexOutOfBoundsException thrown by CommandLineParser.parse(). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-313">CLI-313</a>. Thanks to Dominik Stadler, HUNG LU, Sruteesh Kumar Paramata.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Add github/codeql-action. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump Java from 7 to 8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump actions/cache from 2.1.7 to 3.0.10 #97, #130, #132. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump actions/checkout from 3 to 3.1.0 #133. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump actions/setup-java from 2 to 3.6.0 #136. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump spotbugs from 4.5.3 to 4.7.3 #96, #107, #113, #125, #138. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.5.3.0 to 4.7.3.0 #98, #108, #115, #117, #126, #145. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump commons-parent from 52 to 64 #100, #128, #151, #158. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-antrun-plugin from 3.0.0 to 3.1.0 #103. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.3.2 to 3.4.1 #105, #120. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.16.0 to 3.19.0 #110, #124. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump jacoco-maven-plugin from 0.8.7 to 0.8.8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.1.2 to 3.2.0 #121. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump japicmp-maven-plugin from 0.15.4 to 0.16.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Update JUnit 4 to 5 vintage. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.5.0"></a>
<h2>Release 1.5.0 – 2021-10-23</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix NPE in DefaultParser.isLongOption(String). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>@param or @return lines should end with a period in CommandLine.java. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-279">CLI-279</a>. Thanks to Krishna Mohan Rao Kandunoori.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Replace deprecated FindBugs with SpotBugs. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Replace CLIRR with JApiCmp. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Option Javadocs grammar nits #55. Thanks to Elliotte Rusty Harold.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Minor Improvements #57, #61. Thanks to Arturo Bernal, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Input "test" gets parsed as test, quotes die #58. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-254">CLI-254</a>. Thanks to stoty.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Allow whitespace-only header and footer #26. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-287">CLI-287</a>. Thanks to MrQubo, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Accommodate toggling partial matching in DefaultParser. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-217">CLI-217</a>. Thanks to Rubin Simons.</td>
<td><a href="#team--chtompki">chtompki</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Option parser type EXISTING_FILE_VALUE not check file existing. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-274">CLI-274</a>. Thanks to Béla Schaum.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>CommandLine.getXXX and CommandLine.hasXXX should accept an Option as a parameter. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-271">CLI-271</a>. Thanks to Christoph Läubrich.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Adjust access-modifier of checkRequiredOptions() to protected. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-276">CLI-276</a>. Thanks to Jason Dillon.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>TypeHandler should throw ParseException for an unsupported class. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-282">CLI-282</a>. Thanks to Alex Nordlund.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Added setter for Builder.option #33. Thanks to Waldemar Sojka, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add Option unit tests #76. Thanks to Waldemar Sojka, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Update Java from version 5 to 7. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-294">CLI-294</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Docs: Replace OptionBuilder in usage page #30. Thanks to Mincong Huang.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Remove deprecated sudo setting. #36. Thanks to dengliming.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump junit:junit from 4.12 to 4.13.2, #53, #60. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump commons-parent from 48 to 52. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.12.0 to 3.16.0, #44, #54, #67, #92. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump actions/checkout from 2.3.1 to 3 #46, #72, #78, #93. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump actions/setup-java from v1.4.2 to v2 #50. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-antrun-plugin from 1.7 to 3.0.0 #43. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 2.15 to 3.1.2 #41. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump checkstyle to 9.3 #68, #86, #90. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump actions/cache from 2 to 2.1.7 #64, #65, #81. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump commons.animal-sniffer.version 1.19 -&gt; 1.20. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-bundle-plugin 5.1.1 -&gt; 5.1.2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump biz.aQute.bndlib.version 5.1.2 -&gt; 6.0.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump spotbugs from 4.4.1 to 4.5.3 #70, #88. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.4.1 to 4.5.3.0 #71, #85, #87. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.3.1 to 3.3.2, #91. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.4"></a>
<h2>Release 1.4 – 2017-03-09</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Introduce CommandLine.Builder. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-269">CLI-269</a>.</td>
<td><a href="#team--rfscholte">rfscholte</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Optional argument picking up next regular option as its argument. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-265">CLI-265</a>. Thanks to Martin Sandiford.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Add an addRequiredOption method to Options. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-267">CLI-267</a>. Thanks to Ricardo Ribeiro.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter.setOptionComparator(null) doesn't display the values in inserted order. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-266">CLI-266</a>. Thanks to Ravi Teja.</td>
<td><a href="#team--britter">britter</a></td></tr></table></section><section><a id="a1.3.1"></a>
<h2>Release 1.3.1 – 2015-06-17</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>LongOpt falsely detected as ambiguous. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-252">CLI-252</a>. Thanks to Simon Harrer.</td>
<td><a href="#team--britter">britter</a></td></tr></table></section><section><a id="a1.3"></a>
<h2>Release 1.3 – 2015-05-09</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fixed broken Javadoc links on Introduction page. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-248">CLI-248</a>.</td>
<td><a href="#team--djones">djones</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fixed code example in javadoc of "Option#Builder#valueSeparator(char)". Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-234">CLI-234</a>. Thanks to Greg Thomas.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Clarified behavior of "OptionValidator#validateOption(String)" in case of null input. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-241">CLI-241</a>. Thanks to Beluga Behr.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Small cleanup of Option class. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-240">CLI-240</a>. Thanks to Beluga Behr.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Removed DoubleCheckedLocking test from checkstyle configuration. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-231">CLI-231</a>. Thanks to Duncan Jones.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Options.getRequiredOptions() now returns an unmodifiable list. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-230">CLI-230</a>.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Added new fluent API to create Option instances via builder class Option.Builder.
        This replaces the now deprecated OptionBuilder. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-224">CLI-224</a>. Thanks to Duncan Jones, Brian Blount.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Clarify javadoc for CommandLine.getOptionValue() that the first specified
        argument will be returned. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-218">CLI-218</a>. Thanks to Sven.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Added new method Options.addOption(String, String). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-214">CLI-214</a>. Thanks to Alexandru Mocanu.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Changed unit tests to junit 4 annotation style. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-227">CLI-227</a>. Thanks to Duncan Jones.</td>
<td><a href="#team--tn">tn</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Default options will now work correctly with required options that are missing. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-202">CLI-202</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Default options will now work correctly together with option groups. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-203">CLI-203</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>The javadoc of OptionBuilder now states that the class is not thread-safe. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-209">CLI-209</a>. Thanks to Thomas Herre.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>HelpFormatter now supports setting the displayed separator of long options. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-169">CLI-169</a>. Thanks to J. Lewis Muir.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Improve description of parameter "stopAtNonOption" in method
        CommandLine.parse(Options, String[], boolean). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-197">CLI-197</a>. Thanks to Anders Larsson.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Passing default values for not defined options to a parser will now trigger
        a ParseException instead of a NullPointerException. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-204">CLI-204</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter.setArgName(String) now correctly sets the argument name. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-205">CLI-205</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Default properties provided as input to the Parser.parse() methods are now
        correctly processed. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-201">CLI-201</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>CommandLine.getParsedOptionValue() now returns a String object if no
        option type has been explicitly set. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-215">CLI-215</a>. Thanks to Manuel Müller.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Fixed typo in javadoc of class CommandLine. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-200">CLI-200</a>. Thanks to Gerard Weatherby.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Source code now uses generic types instead of raw types where possible. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-223">CLI-223</a>. Thanks to Gerard Weatherby.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>Corrected javadoc for return type of MissingOptionException.getMissingOptions(). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-220">CLI-220</a>. Thanks to Joe Casadonte.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter now prints command-line options in the same order as they
        have been added. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-212">CLI-212</a>. Thanks to Per Cederberg.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Standard help text now shows mandatory arguments also for the first option. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-186">CLI-186</a>. Thanks to Kristoff Kiefer.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter does not strip anymore leading whitespace in the footer text. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-207">CLI-207</a>. Thanks to Uri Moszkowicz.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Strip quotes contained in argument values only if there is exactly one at the
        beginning and one at the end. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-185">CLI-185</a>. Thanks to Einar M R Rosenvinge.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Negative numerical arguments take precedence over numerical options (only supported
        by the new DefaultParser). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-184">CLI-184</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fix possible StringIndexOutOfBoundsException in HelpFormatter. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-193">CLI-193</a>. Thanks to Travis McLeskey.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>A new parser is available: DefaultParser. It combines the features of the GnuParser and the PosixParser.
        It also provides additional features like partial matching for the long options, and long options without
        separator (i.e like the JVM memory settings: -Xmx512m). This new parser deprecates the previous ones. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-161,CLI-167,CLI-181">CLI-161,CLI-167,CLI-181</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>OptionGroups no longer throw an AlreadySelectedException when reused for several parsings. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-183">CLI-183</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>OptionGroup now selects properly an option with no short name. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-182">CLI-182</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>PosixParser now supports partial long options (--ver instead of --version). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-160">CLI-160</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr></table></section><section><a id="a1.2"></a>
<h2>Release 1.2 – 2009-03-19</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>OptionBuilder is now reseted if an IllegalArgumentException occurs in create(). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-177">CLI-177</a>.</td>
<td><a href="#team--joehni">joehni</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_ddf2cdc445aebd21.gif" title="Remove"/></td>
<td>Ant build system removed.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Incomplete usage documentation about Java property option. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-154">CLI-154</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>TypeHandler prints messages to stderr. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-170">CLI-170</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Infinite loop in the wrapping code of HelpFormatter. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-162">CLI-162</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Fixing some minor javadoc issues.</td>
<td><a href="#team--sgoeschl">sgoeschl</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>The number of arguments defined for an option specifies the arguments per occurrence of the option
        and not for all occurrences. This was a major regression in CLI 1.1 which prevented the use of repeated options. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-137">CLI-137</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Added a getOptionProperties() method in the CommandLine class to retrieve easily the key/value pairs
        specified with options like -Dkey1=value1 -Dkey2=value2.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>GnuParser now supports long options with an '=' sign (ie. --foo=bar and -foo=bar). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-157">CLI-157</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>PosixParser no longer ignores unrecognized short options. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-164">CLI-164</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>PosixParser no longer stops the bursting process of a token if stopAtNonOption is enabled and a non option
        character is encountered. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-163">CLI-163</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>PosixParser no longer keeps processing the tokens after an unrecognized long option
        when stopAtNonOption is enabled. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-165">CLI-165</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Required options are properly checked if an Options instance is used twice to parse a command line. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-156">CLI-156</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>The ordering of options can be defined in help messages. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-155">CLI-155</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>The line wrapping in HelpFormatter now works properly. This caused CLI-162, and thus there was a feature change
        for the HelpFormatter in that it is strict on width now rather than what seemed to be lenience before. Text without
        whitespace will be cut off to fit in the spacing, and an IllegalStateException will be thrown if it is impossible
        to output the information due to spacing constraints. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-151">CLI-151</a>. Thanks to Dan Armbrust.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>The message of MissingOptionException has been improved. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-149">CLI-149</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>The exceptions have been enhanced with methods to retrieve easily the related options. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-86">CLI-86</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Option.toString() now reports arguments properly. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-141">CLI-141</a>. Thanks to Henning Schmiedehausen, Bjorn Townsend.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>The Parser class has been changed to be more easily extendable. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-142">CLI-142</a>. Thanks to Henning Schmiedehausen.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_165f4fcea4ed9d14.gif" title="Update"/></td>
<td>The following classes are now serializable: Option, OptionGroup, CommandLine and Options. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-140">CLI-140</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_ddf2cdc445aebd21.gif" title="Remove"/></td>
<td>OptionValidator is no longer public, its methods were all private.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr></table></section><section><a id="a1.1"></a>
<h2>Release 1.1 – 2007-07-08</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Wrong usage summary. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-2">CLI-2</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Dependecy on commons-lang-2.0 but commons-lang-1.0 is obtained. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-5">CLI-5</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Line separator as first char for helpformatter (footer) throws exception. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-8">CLI-8</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>CommandLine.getOptionValue() behaves contrary to docs. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-13">CLI-13</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>clone method in Option should use super.clone(). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-21">CLI-21</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Passing properties in Parser does not work for options with a single argument. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-23">CLI-23</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Only long options without short option seems to be noticed. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-26">CLI-26</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Infinite Loop in Command-Line processing. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-28">CLI-28</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Options should not be able to be added more than once. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-29">CLI-29</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter doesn't sort options properly. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-35">CLI-35</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>HelpFormatter doesn't function correctly for options with only LongOpt. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-38">CLI-38</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Document enhancement. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-44">CLI-44</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Documentation errors. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-45">CLI-45</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Parameter value "-something" misinterpreted as a parameter. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-51">CLI-51</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>clone() method doesn't fully clone contents. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-56">CLI-56</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>No Javadoc for HelpFormatter!. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-59">CLI-59</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Parser breaks up command line parms into single characters. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-65">CLI-65</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Missing arguments in HelpFormatter.renderOptions(..). Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-67">CLI-67</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Error parsing option arguments. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-69">CLI-69</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>A weakness of parser. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-71">CLI-71</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_2af47992abe22469.gif" title="Add"/></td>
<td>Setting description of a Option. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-78">CLI-78</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>CLI_1_BRANCH build.xml doesn't work. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-129">CLI-129</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Remove the Commons Lang dependency. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-130">CLI-130</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Options class returns options in random order. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-131">CLI-131</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>MissingOptionException should contain a useful error message. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-132">CLI-132</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>NullPointerException in Util.stripLeadingHyphens when passed a null argument. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-133">CLI-133</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>1.1 is not backwards compatible because it adds methods to the CommandLineParser interface. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-134">CLI-134</a>.</td>
<td>-</td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_19c04b9192b44454.gif" title="Fix"/></td>
<td>Backwards compatibility between 1.1 and 1.0 broken due to Option.addValue removal. Fixes <a href="https://issues.apache.org/jira/browse/ViewIssue.jspa?key=CLI-135">CLI-135</a>.</td>
<td>-</td></tr></table></section><section><a id="a1.0"></a>
<h2>Release 1.0 – 2002-11-06</h2>
<p>No changes in this release.</p></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="issue-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/issue-management.html -->

<!-- page_index: 3 -->

# Overview

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Overview"></a>
<h1>Overview</h1>
<p>This project uses an issue management system to manage its issues.</p></section><section><a id="Issue_Management"></a>
<h1>Issue Management</h1>
<p>Issues, bugs, and feature requests should be submitted to the following issue management system for this project.</p>
<pre><a href="https://issues.apache.org/jira/browse/CLI">https://issues.apache.org/jira/browse/CLI</a></pre></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/dependency-info.html -->

<!-- page_index: 4 -->

# Maven Coordinates

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Maven_Coordinates"></a>
<h1>Maven Coordinates</h1><section><a id="Apache_Maven"></a>
<h2>Apache Maven</h2>
<pre>&lt;dependency&gt;
  &lt;groupId&gt;commons-cli&lt;/groupId&gt;
  &lt;artifactId&gt;commons-cli&lt;/artifactId&gt;
  &lt;version&gt;1.11.0&lt;/version&gt;
&lt;/dependency&gt;</pre></section><section><a id="Apache_Ivy"></a>
<h2>Apache Ivy</h2>
<pre>&lt;dependency org="commons-cli" name="commons-cli" rev="1.11.0"&gt;
  &lt;artifact name="commons-cli" type="jar" /&gt;
&lt;/dependency&gt;</pre></section><section><a id="Groovy_Grape"></a>
<h2>Groovy Grape</h2>
<pre>@Grapes(
@Grab(group='commons-cli', module='commons-cli', version='1.11.0')
)</pre></section><section><a id="Gradle.2FGrails"></a>
<h2>Gradle/Grails</h2>
<pre>implementation 'commons-cli:commons-cli:1.11.0'</pre></section><section><a id="Scala_SBT"></a>
<h2>Scala SBT</h2>
<pre>libraryDependencies += "commons-cli" % "commons-cli" % "1.11.0"</pre></section><section><a id="Leiningen"></a>
<h2>Leiningen</h2>
<pre>[commons-cli "1.11.0"]</pre></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/scm.html -->

<!-- page_index: 5 -->

# Overview

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Overview"></a>
<h1>Overview</h1>
<p>This project uses <a href="https://git-scm.com/">Git</a> to manage its source code. Instructions on Git use can be found at <a href="https://git-scm.com/doc">https://git-scm.com/doc</a>.</p></section><section><a id="Web_Browser_Access"></a>
<h1>Web Browser Access</h1>
<p>The following is a link to a browsable version of the source repository:</p>
<pre><a href="https://gitbox.apache.org/repos/asf?p=commons-cli.git">https://gitbox.apache.org/repos/asf?p=commons-cli.git</a></pre></section><section><a id="Anonymous_Access"></a>
<h1>Anonymous Access</h1>
<p>The source can be checked out anonymously from Git with this command (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>):</p>
<pre>$ git clone --branch rel/common-cli-1.11.0 https://gitbox.apache.org/repos/asf/commons-cli.git</pre></section><section><a id="Developer_Access"></a>
<h1>Developer Access</h1>
<p>Only project developers can access the Git tree via this method (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>).</p>
<pre>$ git clone --branch rel/common-cli-1.11.0 https://gitbox.apache.org/repos/asf/commons-cli.git</pre></section><section><a id="Access_from_Behind_a_Firewall"></a>
<h1>Access from Behind a Firewall</h1>
<p>Refer to the documentation of the SCM used for more information about access behind a firewall.</p></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/project-info.html -->

<!-- page_index: 6 -->

# Project Information

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h1>Project Information</h1>
<p>This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by <a href="https://maven.apache.org">Maven</a> on behalf of the project.</p><section>
<h2>Overview</h2>
<table>
<tr>
<th>Document</th>
<th>Description</th></tr>
<tr>
<td><a href="#index">About</a></td>
<td>Apache Commons CLI provides a simple API for presenting, processing, and validating a Command Line Interface.</td></tr>
<tr>
<td><a href="#summary">Summary</a></td>
<td>This document lists other related information of this project</td></tr>
<tr>
<td><a href="#team">Team</a></td>
<td>This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another.</td></tr>
<tr>
<td><a href="#scm">Source Code Management</a></td>
<td>This document lists ways to access the online source repository.</td></tr>
<tr>
<td><a href="#issue-management">Issue Management</a></td>
<td>This document provides information on the issue management system used in this project.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-cli/mailing-lists.html">Mailing Lists</a></td>
<td>This document provides subscription and archive information for this project's mailing lists.</td></tr>
<tr>
<td><a href="#dependency-info">Maven Coordinates</a></td>
<td>This document describes how to include this project as a dependency using various dependency management tools.</td></tr>
<tr>
<td><a href="#dependency-management">Dependency Management</a></td>
<td>This document lists the dependencies that are defined through dependencyManagement.</td></tr>
<tr>
<td><a href="#dependencies">Dependencies</a></td>
<td>This document lists the project's dependencies and provides information on each dependency.</td></tr>
<tr>
<td><a href="#dependency-convergence">Dependency Convergence</a></td>
<td>This document presents the convergence of dependency versions across the entire project, and its sub modules.</td></tr>
<tr>
<td><a href="#ci-management">CI Management</a></td>
<td>This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis.</td></tr>
<tr>
<td><a href="#distribution-management">Distribution Management</a></td>
<td>This document provides informations on the distribution management of this project.</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/summary.html -->

<!-- page_index: 7 -->

# Project Summary

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Project_Summary"></a>
<h1>Project Summary</h1><section><a id="Project_Information"></a>
<h2>Project Information</h2>
<table>
<tr>
<th>Field</th>
<th>Value</th></tr>
<tr>
<td>Name</td>
<td>Apache Commons CLI</td></tr>
<tr>
<td>Description</td>
<td>Apache Commons CLI provides a simple API for presenting, processing, and validating a Command Line Interface.</td></tr>
<tr>
<td>Homepage</td>
<td><a href="https://commons.apache.org/proper/commons-cli/">https://commons.apache.org/proper/commons-cli/</a></td></tr></table></section><section><a id="Project_Organization"></a>
<h2>Project Organization</h2>
<table>
<tr>
<th>Field</th>
<th>Value</th></tr>
<tr>
<td>Name</td>
<td>The Apache Software Foundation</td></tr>
<tr>
<td>URL</td>
<td><a href="https://www.apache.org/">https://www.apache.org/</a></td></tr></table></section><section><a id="Build_Information"></a>
<h2>Build Information</h2>
<table>
<tr>
<th>Field</th>
<th>Value</th></tr>
<tr>
<td>GroupId</td>
<td>commons-cli</td></tr>
<tr>
<td>ArtifactId</td>
<td>commons-cli</td></tr>
<tr>
<td>Version</td>
<td>1.11.0</td></tr>
<tr>
<td>Type</td>
<td>jar</td></tr>
<tr>
<td>Java Version</td>
<td>1.8</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/team.html -->

<!-- page_index: 8 -->

# Project Team

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Project_Team"></a>
<h1>Project Team</h1>
<p>A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.</p>
<p>The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.</p><section><a id="Members"></a>
<h2>Members</h2>
<p>The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.</p>
<table>
<tr>
<th>Image</th>
<th>Id</th>
<th>Name</th>
<th>Email</th>
<th>URL</th>
<th>Organization</th>
<th>Organization URL</th>
<th>Roles</th>
<th>Time Zone</th></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td><a id="jstrachan"></a>jstrachan</td>
<td>James Strachan</td>
<td><a href="mailto:jstrachan@apache.org">jstrachan@apache.org</a></td>
<td>-</td>
<td>SpiritSoft, Inc.</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td><a id="bob"></a>bob</td>
<td>Bob McWhirter</td>
<td><a href="mailto:bob@werken.com">bob@werken.com</a></td>
<td>-</td>
<td>Werken</td>
<td>-</td>
<td>contributed ideas and code from werken.opt</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td><a id="jkeyes"></a>jkeyes</td>
<td>John Keyes</td>
<td><a href="mailto:jbjk@mac.com">jbjk@mac.com</a></td>
<td>-</td>
<td>integral Source</td>
<td>-</td>
<td>contributed ideas and code from Optz</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/b0ceb95e9c57f1881d6a2b3d1bc77073_cb6613f0f68c26a0.jpg"/></figure></td>
<td><a id="roxspring"></a>roxspring</td>
<td>Rob Oxspring</td>
<td><a href="mailto:roxspring@imapmail.org">roxspring@imapmail.org</a></td>
<td>-</td>
<td>Indigo Stone</td>
<td>-</td>
<td>designed CLI2</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/8304c64641badd4218a89a5f97d2ae86_fcb6742561c76d11.jpg"/></figure></td>
<td><a id="ebourg"></a>ebourg</td>
<td>Emmanuel Bourg</td>
<td><a href="mailto:ebourg@apache.org">ebourg@apache.org</a></td>
<td>-</td>
<td>Ariane Software</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td><a id="tn"></a>tn</td>
<td>Thomas Neidhart</td>
<td><a href="mailto:tn@apache.org">tn@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/a010ac0916b6b9b10883e9359cfcd7f9_2b1b31f5610f06c0.jpg"/></figure></td>
<td><a id="chtompki"></a>chtompki</td>
<td>Rob Tompkins</td>
<td><a href="mailto:chtompki@apache.org">chtompki@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="https://people.apache.org/~ggregory/img/garydgregory80.png"/></figure></td>
<td><a id="ggregory"></a>ggregory</td>
<td>Gary Gregory</td>
<td><a href="mailto:ggregory at apache.org">ggregory at apache.org</a></td>
<td><a href="https://www.garygregory.com">https://www.garygregory.com</a></td>
<td>The Apache Software Foundation</td>
<td><a href="https://www.apache.org/">https://www.apache.org/</a></td>
<td>PMC Member</td>
<td>America/New_York</td></tr></table></section><section><a id="Contributors"></a>
<h2>Contributors</h2>
<p>The following additional people have contributed to this project through the way of suggestions, patches or documentation.</p>
<table>
<tr>
<th>Image</th>
<th>Name</th>
<th>Email</th>
<th>Organization</th>
<th>Roles</th></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Beluga Behr</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Peter Donald</td>
<td>-</td>
<td>-</td>
<td>contributed ideas and code from Avalon Excalibur's cli package</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Brian Egge</td>
<td>-</td>
<td>-</td>
<td>made the 1.1 release happen</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Duncan Jones</td>
<td>-</td>
<td>-</td>
<td>supplied patches</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Berin Loritsch</td>
<td><a href="mailto:bloritsch@apache.org">bloritsch@apache.org</a></td>
<td>-</td>
<td>helped in the Avalon CLI merge</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Peter Maddocks</td>
<td><a href="mailto:peter_maddocks@hp.com">peter_maddocks@hp.com</a></td>
<td>Hewlett-Packard</td>
<td>supplied patch</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Alexandru Mocanu</td>
<td>-</td>
<td>-</td>
<td>supplied patch</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Andrew Shirley</td>
<td>-</td>
<td>-</td>
<td>lots of fixes for 1.1</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Greg Thomas</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_6d2f0dc51f21de3b.jpg"/></figure></td>
<td>Slawek Zachcial</td>
<td>-</td>
<td>-</td>
<td>unit tests</td></tr>
<tr>
<td><figure><img src="assets/images/ca45422f802b5af7cfaa7f9ed73e62aa_ac70a6009d755e93.jpg"/></figure></td>
<td>Rubin Simons</td>
<td><a href="mailto:rubin@raaftech.com">rubin@raaftech.com</a></td>
<td>-</td>
<td>supplied patch</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/dependency-management.html -->

<!-- page_index: 9 -->

# Project Dependency Management

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Project_Dependency_Management"></a>
<h1>Project Dependency Management</h1><section><a id="compile"></a>
<h2>compile</h2>
<p>The following is a list of compile dependencies in the DependencyManagement of this project. These dependencies can be included in the submodules to compile and run the submodule:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>License</th></tr>
<tr>
<td>org.junit-pioneer</td>
<td><a href="https://junit-pioneer.org/">junit-pioneer</a></td>
<td>1.9.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-api</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-engine</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-migrationsupport</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-params</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-commons</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-console</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-engine</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-jfr</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-launcher</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-reporting</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-runner</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite-api</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite-commons</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite-engine</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-testkit</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.vintage</td>
<td><a href="https://junit.org/">junit-vintage-engine</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr></table></section><section><a id="test"></a>
<h2>test</h2>
<p>The following is a list of test dependencies in the DependencyManagement of this project. These dependencies can be included in the submodules to compile and run unit tests for the submodule:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>License</th></tr>
<tr>
<td>org.mockito</td>
<td><a href="https://github.com/mockito/mockito">mockito-bom</a></td>
<td>4.11.0</td>
<td>jar</td>
<td><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependencies"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/dependencies.html -->

<!-- page_index: 10 -->

# Project Dependencies

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Project_Dependencies"></a>
<h1>Project Dependencies</h1><section><a id="Project_Dependencies_test"></a>
<h2>test</h2>
<p>The following is a list of test dependencies for this project. These dependencies are only required to compile and run unit tests for the application:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>Licenses</th></tr>
<tr>
<td>commons-io</td>
<td><a href="https://commons.apache.org/proper/commons-io/">commons-io</a></td>
<td>2.21.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>org.apache.commons</td>
<td><a href="https://commons.apache.org/proper/commons-text">commons-text</a></td>
<td>1.14.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>org.junit-pioneer</td>
<td><a href="https://junit-pioneer.org/">junit-pioneer</a></td>
<td>1.9.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-api</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-engine</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-params</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.mockito</td>
<td><a href="https://github.com/mockito/mockito">mockito-core</a></td>
<td>4.11.0</td>
<td>jar</td>
<td><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></td></tr></table></section></section><section><a id="Project_Transitive_Dependencies"></a>
<h1>Project Transitive Dependencies</h1>
<p>The following is a list of transitive dependencies for this project. Transitive dependencies are the dependencies of the project dependencies.</p><section><a id="Project_Transitive_Dependencies_test"></a>
<h2>test</h2>
<p>The following is a list of test dependencies for this project. These dependencies are only required to compile and run unit tests for the application:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>Licenses</th></tr>
<tr>
<td>net.bytebuddy</td>
<td><a href="https://bytebuddy.net/byte-buddy">byte-buddy</a></td>
<td>1.12.19</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td>net.bytebuddy</td>
<td><a href="https://bytebuddy.net/byte-buddy-agent">byte-buddy-agent</a></td>
<td>1.12.19</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.commons</td>
<td><a href="https://commons.apache.org/proper/commons-lang/">commons-lang3</a></td>
<td>3.18.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>org.apiguardian</td>
<td><a href="https://github.com/apiguardian-team/apiguardian">apiguardian-api</a></td>
<td>1.1.2</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-commons</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-engine</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-launcher</a></td>
<td>1.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.objenesis</td>
<td><a href="http://objenesis.org/objenesis">objenesis</a></td>
<td>3.3</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td>org.opentest4j</td>
<td><a href="https://github.com/ota4j-team/opentest4j">opentest4j</a></td>
<td>1.3.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr></table></section></section><section><a id="Project_Dependency_Graph"></a>
<h1>Project Dependency Graph</h1>
<section><a id="Dependency_Tree"></a>
<h2>Dependency Tree</h2>
<ul>
<li>commons-cli:commons-cli:jar:1.11.0 <img alt="[Information]" id="_img1" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep0">
<table>
<tr>
<th>Apache Commons CLI</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Commons CLI provides a simple API for presenting, processing, and validating a Command Line Interface.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-cli/">https://commons.apache.org/proper/commons-cli/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.jupiter:junit-jupiter-api:jar:5.13.4 (test) <img alt="[Information]" id="_img3" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep2">
<table>
<tr>
<th>JUnit Jupiter API</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-api" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.opentest4j:opentest4j:jar:1.3.0 (test) <img alt="[Information]" id="_img5" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep4">
<table>
<tr>
<th>org.opentest4j:opentest4j</th></tr>
<tr>
<td>
<p><b>Description: </b>Open Test Alliance for the JVM</p>
<p><b>URL: </b><a href="https://github.com/ota4j-team/opentest4j">https://github.com/ota4j-team/opentest4j</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.junit.platform:junit-platform-commons:jar:1.13.4 (test) <img alt="[Information]" id="_img7" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep6">
<table>
<tr>
<th>JUnit Platform Commons</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-commons" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li>
<li>org.apiguardian:apiguardian-api:jar:1.1.2 (test) <img alt="[Information]" id="_img9" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep8">
<table>
<tr>
<th>org.apiguardian:apiguardian-api</th></tr>
<tr>
<td>
<p><b>Description: </b>@API Guardian</p>
<p><b>URL: </b><a href="https://github.com/apiguardian-team/apiguardian">https://github.com/apiguardian-team/apiguardian</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.junit.jupiter:junit-jupiter-engine:jar:5.13.4 (test) <img alt="[Information]" id="_img11" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep10">
<table>
<tr>
<th>JUnit Jupiter Engine</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-engine" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.platform:junit-platform-engine:jar:1.13.4 (test) <img alt="[Information]" id="_img13" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep12">
<table>
<tr>
<th>JUnit Platform Engine API</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-engine" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.junit.jupiter:junit-jupiter-params:jar:5.13.4 (test) <img alt="[Information]" id="_img15" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep14">
<table>
<tr>
<th>JUnit Jupiter Params</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-params" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li>
<li>org.junit-pioneer:junit-pioneer:jar:1.9.1 (test) <img alt="[Information]" id="_img17" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep16">
<table>
<tr>
<th>junit-pioneer</th></tr>
<tr>
<td>
<p><b>Description: </b>JUnit 5 Extension Pack</p>
<p><b>URL: </b><a href="https://junit-pioneer.org/">https://junit-pioneer.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.platform:junit-platform-launcher:jar:1.13.4 (test) <img alt="[Information]" id="_img19" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep18">
<table>
<tr>
<th>JUnit Platform Launcher</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-launcher" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li></ul></li>
<li>commons-io:commons-io:jar:2.21.0 (test) <img alt="[Information]" id="_img21" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep20">
<table>
<tr>
<th>Apache Commons IO</th></tr>
<tr>
<td>
<p><b>Description: </b>The Apache Commons IO library contains utility classes, stream implementations, file filters, file comparators, endian transformation classes, and much more.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-io/">https://commons.apache.org/proper/commons-io/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>org.apache.commons:commons-text:jar:1.14.0 (test) <img alt="[Information]" id="_img23" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep22">
<table>
<tr>
<th>Apache Commons Text</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Commons Text is a set of utility functions and reusable components for processing
    and manipulating text in a Java environment.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-text">https://commons.apache.org/proper/commons-text</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.commons:commons-lang3:jar:3.18.0 (test) <img alt="[Information]" id="_img25" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep24">
<table>
<tr>
<th>Apache Commons Lang</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Commons Lang, a package of Java utility classes for the
  classes that are in java.lang's hierarchy, or are considered to be so
  standard as to justify existence in java.lang.

  The code is tested using the latest revision of the JDK for supported
  LTS releases: 8, 11, 17 and 21 currently.
  See https://github.com/apache/commons-lang/blob/master/.github/workflows/maven.yml

  Please ensure your build environment is up-to-date and kindly report any build issues.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-lang/">https://commons.apache.org/proper/commons-lang/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.mockito:mockito-core:jar:4.11.0 (test) <img alt="[Information]" id="_img27" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep26">
<table>
<tr>
<th>mockito-core</th></tr>
<tr>
<td>
<p><b>Description: </b>Mockito mock objects library core API and implementation</p>
<p><b>URL: </b><a href="https://github.com/mockito/mockito">https://github.com/mockito/mockito</a></p>
<p><b>Project Licenses: </b><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></p></td></tr></table></div>
<ul>
<li>net.bytebuddy:byte-buddy:jar:1.12.19 (test) <img alt="[Information]" id="_img29" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep28">
<table>
<tr>
<th>Byte Buddy (without dependencies)</th></tr>
<tr>
<td>
<p><b>Description: </b>Byte Buddy is a Java library for creating Java classes at run time.
        This artifact is a build of Byte Buddy with all ASM dependencies repackaged into its own name space.</p>
<p><b>URL: </b><a href="https://bytebuddy.net/byte-buddy">https://bytebuddy.net/byte-buddy</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>net.bytebuddy:byte-buddy-agent:jar:1.12.19 (test) <img alt="[Information]" id="_img31" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep30">
<table>
<tr>
<th>Byte Buddy agent</th></tr>
<tr>
<td>
<p><b>Description: </b>The Byte Buddy agent offers convenience for attaching an agent to the local or a remote VM.</p>
<p><b>URL: </b><a href="https://bytebuddy.net/byte-buddy-agent">https://bytebuddy.net/byte-buddy-agent</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.objenesis:objenesis:jar:3.3 (test) <img alt="[Information]" id="_img33" src="assets/images/icon-info-sml_f08d25e9297e50ab.gif"/><div id="_dep32">
<table>
<tr>
<th>Objenesis</th></tr>
<tr>
<td>
<p><b>Description: </b>A library for instantiating Java objects</p>
<p><b>URL: </b><a href="http://objenesis.org/objenesis">http://objenesis.org/objenesis</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li></ul></li></ul></section></section><section><a id="Licenses"></a>
<h1>Licenses</h1>
<p><b>The Apache License, Version 2.0: </b>org.apiguardian:apiguardian-api, org.opentest4j:opentest4j</p>
<p><b>The MIT License: </b>mockito-core</p>
<p><b>Apache-2.0: </b>Apache Commons CLI, Apache Commons IO, Apache Commons Lang, Apache Commons Text</p>
<p><b>Eclipse Public License v2.0: </b>JUnit Jupiter API, JUnit Jupiter Engine, JUnit Jupiter Params, JUnit Platform Commons, JUnit Platform Engine API, JUnit Platform Launcher, junit-pioneer</p>
<p><b>Apache License, Version 2.0: </b>Byte Buddy (without dependencies), Byte Buddy agent, Objenesis</p></section><section><a id="Dependency_File_Details"></a>
<h1>Dependency File Details</h1>
<table>
<tr>
<th>Filename</th>
<th>Size</th>
<th>Entries</th>
<th>Classes</th>
<th>Packages</th>
<th>Java Version</th>
<th title="Indicates whether these dependencies have been compiled with debug information.">Debug Information</th></tr>
<tr>
<td>commons-io-2.21.0.jar</td>
<td>585.3 kB</td>
<td>428</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>426</td>
<td>398</td>
<td>15</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
<tr>
<td>byte-buddy-1.12.19.jar</td>
<td>4 MB</td>
<td>2742</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>2740</td>
<td>2687</td>
<td>38</td>
<td>1.6</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
<tr>
<td>byte-buddy-agent-1.12.19.jar</td>
<td>256.4 kB</td>
<td>90</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>88</td>
<td>69</td>
<td>2</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
<tr>
<td>commons-lang3-3.18.0.jar</td>
<td>703 kB</td>
<td>444</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>443</td>
<td>413</td>
<td>18</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
<tr>
<td>commons-text-1.14.0.jar</td>
<td>259.9 kB</td>
<td>185</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>184</td>
<td>164</td>
<td>8</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
<tr>
<td>apiguardian-api-1.1.2.jar</td>
<td>6.8 kB</td>
<td>9</td>
<td>3</td>
<td>2</td>
<td>1.6</td>
<td>Yes</td></tr>
<tr>
<td>junit-pioneer-1.9.1.jar</td>
<td>200 kB</td>
<td>171</td>
<td>156</td>
<td>9</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-api-5.13.4.jar</td>
<td>240.2 kB</td>
<td>216</td>
<td>201</td>
<td>8</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-engine-5.13.4.jar</td>
<td>341.1 kB</td>
<td>178</td>
<td>161</td>
<td>9</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-params-5.13.4.jar</td>
<td>660.8 kB</td>
<td>431</td>
<td>397</td>
<td>22</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-platform-commons-1.13.4.jar</td>
<td>158.5 kB</td>
<td>100</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>89</td>
<td>74</td>
<td>9</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>11</td>
<td>5</td>
<td>1</td>
<td>9</td>
<td>Yes</td></tr>
<tr>
<td>junit-platform-engine-1.13.4.jar</td>
<td>268.6 kB</td>
<td>189</td>
<td>170</td>
<td>10</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-platform-launcher-1.13.4.jar</td>
<td>223.1 kB</td>
<td>144</td>
<td>129</td>
<td>7</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>mockito-core-4.11.0.jar</td>
<td>684.9 kB</td>
<td>651</td>
<td>579</td>
<td>64</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>objenesis-3.3.jar</td>
<td>49.4 kB</td>
<td>59</td>
<td>43</td>
<td>10</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>opentest4j-1.3.0.jar</td>
<td>14.3 kB</td>
<td>15</td>
<td>9</td>
<td>2</td>
<td>1.6</td>
<td>Yes</td></tr>
<tr>
<th>Total</th>
<th>Size</th>
<th>Entries</th>
<th>Classes</th>
<th>Packages</th>
<th>Java Version</th>
<th>Debug Information</th></tr>
<tr>
<td>16</td>
<td>8.6 MB</td>
<td>6052</td>
<td>5653</td>
<td>233</td>
<td>1.8</td>
<td>16</td></tr>
<tr>
<td>test: 16</td>
<td>test: 8.6 MB</td>
<td>test: 6052</td>
<td>test: 5653</td>
<td>test: 233</td>
<td>1.8</td>
<td>test: 16</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-convergence"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/dependency-convergence.html -->

<!-- page_index: 11 -->

# Dependency Convergence

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h1>Dependency Convergence</h1>
<table><caption>
<b>Statistics:</b>
</caption>
<tr>
<th>Number of dependencies (NOD):</th>
<td>16</td></tr>
<tr>
<th>Number of unique artifacts (NOA):</th>
<td>16</td></tr>
<tr>
<th>Number of version-conflicting artifacts (NOC):</th>
<td>0</td></tr>
<tr>
<th>Number of SNAPSHOT artifacts (NOS):</th>
<td>0</td></tr>
<tr>
<th>Convergence (NOD/NOA):</th>
<td><img alt="[Success]" src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/> <b>100 %</b></td></tr>
<tr>
<th>Ready for release (100% convergence and no SNAPSHOTS):</th>
<td><img alt="[Success]" src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/> <b>Success</b></td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/ci-management.html -->

<!-- page_index: 12 -->

# Overview

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Overview"></a>
<h1>Overview</h1>
<p>This project uses <a href="https://github.com/features/actions/">GitHub Actions</a>.</p></section><section><a id="Access"></a>
<h1>Access</h1>
<p>The following is a link to the continuous integration system used by the project:</p>
<pre><a href="https://github.com/apache/commons-cli/actions">https://github.com/apache/commons-cli/actions</a></pre></section><section><a id="Notifiers"></a>
<h1>Notifiers</h1>
<p>No notifiers are defined. Please check back at a later date.</p></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="distribution-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/distribution-management.html -->

<!-- page_index: 13 -->

# Overview

|  |  |
| --- | --- |
|  | Overview The following is the distribution management information used by this project.  Repository - apache.releases.https<https://repository.apache.org/service/local/staging/deploy/maven2>  Snapshot Repository - apache.snapshots.https<https://repository.apache.org/content/repositories/snapshots>  Site - apache.website scm:svn:https://svn.apache.org/repos/infra/websites/production/commons/content/proper/commons-cli |

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/project-reports.html -->

<!-- page_index: 14 -->

# Generated Reports

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h1>Generated Reports</h1>
<p>This document provides an overview of the various reports that are automatically generated by <a href="https://maven.apache.org">Maven</a> . Each report is briefly described below.</p><section>
<h2>Overview</h2>
<table>
<tr>
<th>Document</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes">Changes</a></td>
<td>Changes report on releases of this project.</td></tr>
<tr>
<td><a href="#jira-changes">JIRA Report</a></td>
<td>Report on Issues from the JIRA Issue Tracking System.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-cli/apidocs/index.html">Javadoc</a></td>
<td>Javadoc API documentation.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-cli/xref/index.html">Source Xref</a></td>
<td>HTML based, cross-reference version of Java source code.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-cli/xref-test/index.html">Test Source Xref</a></td>
<td>HTML based, cross-reference version of Java test source code.</td></tr>
<tr>
<td><a href="#surefire">Surefire</a></td>
<td>Report on the test results of the project.</td></tr>
<tr>
<td><a href="#rat-report">RAT Report</a></td>
<td>Report on compliance to license related source code policies</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-cli/jacoco/index.html">JaCoCo</a></td>
<td>JaCoCo Coverage Report.</td></tr>
<tr>
<td><a href="#japicmp">japicmp</a></td>
<td>Comparing source compatibility of commons-cli-1.11.0.jar against commons-cli-1.10.0.jar</td></tr>
<tr>
<td><a href="#checkstyle">Checkstyle</a></td>
<td>Report on coding style conventions.</td></tr>
<tr>
<td><a href="#spotbugs">SpotBugs</a></td>
<td>Generates a source code report with the SpotBugs Library.</td></tr>
<tr>
<td><a href="#cpd">CPD</a></td>
<td>Duplicate code detection.</td></tr>
<tr>
<td><a href="#pmd">PMD</a></td>
<td>Verification of coding rules.</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/jira-changes.html -->

<!-- page_index: 15 -->

# JIRA Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="JIRA_Report"></a>
<h1>JIRA Report</h1>
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

<!-- page_index: 16 -->

# Surefire Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Surefire_Report"></a>
<h1>Surefire Report</h1><section><a id="Summary"></a>
<h2>Summary</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p>
<table>
<tr>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td>977</td>
<td>0</td>
<td>0</td>
<td>61</td>
<td>93.8%</td>
<td>0.754 s</td></tr></table>
<p>Note: failures are anticipated and checked for with assertions while errors are unanticipated.</p>
</section><section><a id="Package_List"></a>
<h2>Package List</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p>
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
<td><a href="#surefire--org.apache.commons.cli.example">org.apache.commons.cli.example</a></td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.022 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli">org.apache.commons.cli</a></td>
<td>809</td>
<td>0</td>
<td>0</td>
<td>61</td>
<td>92.5%</td>
<td>0.698 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.help">org.apache.commons.cli.help</a></td>
<td>118</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.025 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug">org.apache.commons.cli.bug</a></td>
<td>37</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.009 s</td></tr></table>
<p>Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.</p><section><a id="org.apache.commons.cli.example"></a>
<h3>org.apache.commons.cli.example</h3>
<table>
<tr>
<th>-</th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.example.apthelpappendabletest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.example.apthelpappendabletest">AptHelpAppendableTest</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.example.xhtmlhelpappendabletest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.example.xhtmlhelpappendabletest">XhtmlHelpAppendableTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.020 s</td></tr></table></section><section><a id="org.apache.commons.cli"></a>
<h3>org.apache.commons.cli</h3>
<table>
<tr>
<th>-</th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.applicationtest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.applicationtest">ApplicationTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.optioncounttest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.optioncounttest">OptionCountTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.007 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.unrecognizedoptionexceptiontest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.unrecognizedoptionexceptiontest">UnrecognizedOptionExceptionTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.commandlinetest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.commandlinetest">CommandLineTest</a></td>
<td>138</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.116 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.alreadyselectedexceptiontest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.alreadyselectedexceptiontest">AlreadySelectedExceptionTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.parseexceptiontest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.parseexceptiontest">ParseExceptionTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.typehandlertest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.typehandlertest">TypeHandlerTest</a></td>
<td>63</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.027 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.solrclitest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.solrclitest">SolrCliTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest">PosixParserTest</a></td>
<td>67</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>85.1%</td>
<td>0.008 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.valuetest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.valuetest">ValueTest</a></td>
<td>40</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.010 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.optionvalidatortest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.optionvalidatortest">OptionValidatorTest</a></td>
<td>115</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.024 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.optiontest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.optiontest">OptionTest</a></td>
<td>23</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.008 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.patternoptionbuildertest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.patternoptionbuildertest">PatternOptionBuilderTest</a></td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.067 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.helpformattertest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.helpformattertest">HelpFormatterTest</a></td>
<td>44</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.278 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.utiltest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.utiltest">UtilTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.020 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.defaultparsertest"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.defaultparsertest">DefaultParserTest</a></td>
<td>87</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>97.7%</td>
<td>0.035 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.optionstest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.optionstest">OptionsTest</a></td>
<td>16</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.argumentisoptiontest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.argumentisoptiontest">ArgumentIsOptionTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest">BasicParserTest</a></td>
<td>67</td>
<td>0</td>
<td>0</td>
<td>27</td>
<td>59.7%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.optionbuildertest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.optionbuildertest">OptionBuilderTest</a></td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.disablepartialmatchingtest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.disablepartialmatchingtest">DisablePartialMatchingTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest">GnuParserTest</a></td>
<td>67</td>
<td>0</td>
<td>0</td>
<td>22</td>
<td>67.2%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.deprecatedattributestest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.deprecatedattributestest">DeprecatedAttributesTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.missingoptionexceptiontest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.missingoptionexceptiontest">MissingOptionExceptionTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.optiongrouptest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.optiongrouptest">OptionGroupTest</a></td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.solrcreatetooltest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.solrcreatetooltest">SolrCreateToolTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.valuestest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.valuestest">ValuesTest</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.convertertests"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.convertertests">ConverterTests</a></td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.065 s</td></tr></table></section><section><a id="org.apache.commons.cli.help"></a>
<h3>org.apache.commons.cli.help</h3>
<table>
<tr>
<th>-</th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.help.optionformattertest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.help.optionformattertest">OptionFormatterTest</a></td>
<td>22</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.005 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.help.helpformattertest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.help.helpformattertest">HelpFormatterTest</a></td>
<td>16</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.help.texthelpappendabletest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.help.texthelpappendabletest">TextHelpAppendableTest</a></td>
<td>33</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.help.utiltest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.help.utiltest">UtilTest</a></td>
<td>34</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.help.textstyletests"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.help.textstyletests">TextStyleTests</a></td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug"></a>
<h3>org.apache.commons.cli.bug</h3>
<table>
<tr>
<th>-</th>
<th>Class</th>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli252test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli252test">BugCLI252Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli71test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli71test">BugCLI71Test</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli13test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli13test">BugCLI13Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli265test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli265test">BugCLI265Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli18test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli18test">BugCLI18Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli162test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli162test">BugCLI162Test</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli266test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli266test">BugCLI266Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli148test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli148test">BugCLI148Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli312test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli312test">BugCLI312Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli133test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli133test">BugCLI133Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli325test"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugcli325test">BugCLI325Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.bug.bugstest"><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.cli.bug.bugstest">BugsTest</a></td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr></table></section>
</section><section><a id="Test_Cases"></a>
<h2>Test Cases</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p><section><a id="org.apache.commons.cli.ApplicationTest"></a>
<h3>ApplicationTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ApplicationTest.testAnt"></a>testAnt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ApplicationTest.testMan"></a>testMan</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ApplicationTest.testNLT"></a>testNLT</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ApplicationTest.testLs"></a>testLs</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ApplicationTest.testGroovy"></a>testGroovy</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.OptionCountTest"></a>
<h3>OptionCountTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionCountTest.testFiveSwitchesMixed"></a>testFiveSwitchesMixed</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionCountTest.testOneSwitch"></a>testOneSwitch</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionCountTest.testThreeSwitchesCompact"></a>testThreeSwitchesCompact</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionCountTest.testThreeSwitches"></a>testThreeSwitches</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionCountTest.testNoSwitch"></a>testNoSwitch</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.help.OptionFormatterTest"></a>
<h3>OptionFormatterTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testSetOptSeparator"></a>testSetOptSeparator</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testCopyConstructor"></a>testCopyConstructor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B1.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B2.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B3.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B4.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B5.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B6.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[6]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B7.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testComplexDeprecationFormat.28DeprecatedAttributes.2C_String.29.5B8.5D"></a>testComplexDeprecationFormat(DeprecatedAttributes, String)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testAsOptional"></a>testAsOptional</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testSetLongOptPrefix"></a>testSetLongOptPrefix</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testSetOptArgumentSeparator"></a>testSetOptArgumentSeparator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testGetBothOpt"></a>testGetBothOpt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testCli343Part1"></a>testCli343Part1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testCli343Part2"></a>testCli343Part2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testSetSyntaxFormatFunction"></a>testSetSyntaxFormatFunction</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testGetDescription"></a>testGetDescription</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testAsSyntaxOption"></a>testAsSyntaxOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testDefaultSyntaxFormat"></a>testDefaultSyntaxFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testSetArgumentNameDelimiters"></a>testSetArgumentNameDelimiters</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.OptionFormatterTest.testSetDefaultArgName"></a>testSetDefaultArgName</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI252Test"></a>
<h3>BugCLI252Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI252Test.testAmbiquousOptionName"></a>testAmbiquousOptionName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI252Test.testExactOptionNameMatch"></a>testExactOptionNameMatch</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.UnrecognizedOptionExceptionTest"></a>
<h3>UnrecognizedOptionExceptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.UnrecognizedOptionExceptionTest.testConstructor"></a>testConstructor</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.CommandLineTest"></a>
<h3>CommandLineTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B1.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[1]</td>
<td>0.007 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B2.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B3.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[3]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B4.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[4]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B5.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[5]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B6.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B7.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B8.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[8]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B9.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[9]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B10.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B11.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B12.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[12]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B13.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B14.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[14]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B15.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[15]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNullDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B16.5D"></a>testHasOptionNullDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B1.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[1]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B2.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[2]</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B3.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B4.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B5.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[5]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B6.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B7.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B8.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B9.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[9]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B10.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B11.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B12.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[12]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B13.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B14.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B15.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.2C_boolean.2C_Integer.2C_Option.29.5B16.5D"></a>testGetParsedOptionValue(String[], Option, OptionGroup, boolean, Integer, boolean, Integer, Option)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B1.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[1]</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B2.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B3.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B4.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B5.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[5]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B6.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B7.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[7]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B8.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B9.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[9]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B10.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B11.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B12.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B13.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[13]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B14.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B15.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.5B.5D.2C_boolean.2C_String.5B.5D.2C_Option.29.5B16.5D"></a>testGetOptionValues(String[], Option, OptionGroup, boolean, String[], boolean, String[], Option)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B1.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B2.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B3.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B4.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B5.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B6.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[6]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B7.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B8.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[8]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B9.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B10.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B11.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B12.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B13.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B14.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B15.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOptionNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B16.5D"></a>testHasOptionNoDeprecationHandler(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testBuilderGet"></a>testBuilderGet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testBuilderNullArgs"></a>testBuilderNullArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionsBuilder"></a>testGetOptionsBuilder</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testBuilderNullOption"></a>testBuilderNullOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B1.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B2.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B3.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B4.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B5.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B6.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B7.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B8.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B9.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[9]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B10.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B11.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B12.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B13.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B14.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B15.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testHasOption.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_boolean.2C_boolean.2C_boolean.2C_Option.29.5B16.5D"></a>testHasOption(String[], Option, OptionGroup, boolean, boolean, boolean, boolean, Option)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionProperties"></a>testGetOptionProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B1.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B2.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B3.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B4.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B5.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B6.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B7.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B8.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[8]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B9.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B10.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B11.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B12.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B13.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B14.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B15.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetParsedOptionValues.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_Integer.5B.5D.2C_boolean.2C_Integer.5B.5D.2C_Option.29.5B16.5D"></a>testGetParsedOptionValues(String[], Option, OptionGroup, boolean, Integer[], boolean, Integer[], Option)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionPropertiesWithOption"></a>testGetOptionPropertiesWithOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testBuilderBuild"></a>testBuilderBuild</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNullOption"></a>testNullOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testBadGetParsedOptionValue"></a>testBadGetParsedOptionValue</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B1.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B2.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B3.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B4.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[4]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B5.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B6.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B7.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B8.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B9.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B10.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B11.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B12.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[12]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B13.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B14.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B15.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionValue.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B16.5D"></a>testGetOptionValue(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testGetOptionsCtor"></a>testGetOptionsCtor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B1.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B2.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B3.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B4.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B5.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B6.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B7.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B8.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B9.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B10.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B11.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B12.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B13.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B14.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[14]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B15.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.CommandLineTest.testNoDeprecationHandler.28String.5B.5D.2C_Option.2C_OptionGroup.2C_boolean.2C_String.2C_boolean.2C_String.2C_Option.29.5B16.5D"></a>testNoDeprecationHandler(String[], Option, OptionGroup, boolean, String, boolean, String, Option)[16]</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.AlreadySelectedExceptionTest"></a>
<h3>AlreadySelectedExceptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.AlreadySelectedExceptionTest.testConstructor"></a>testConstructor</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI71Test"></a>
<h3>BugCLI71Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI71Test.testBasic"></a>testBasic</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI71Test.testLackOfError"></a>testLackOfError</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI71Test.testMistakenArgument"></a>testMistakenArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI71Test.testGetsDefaultIfOptional"></a>testGetsDefaultIfOptional</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI13Test"></a>
<h3>BugCLI13Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI13Test.testCLI13"></a>testCLI13</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI265Test"></a>
<h3>BugCLI265Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI265Test.testShouldParseShortOptionWithoutValue"></a>testShouldParseShortOptionWithoutValue</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI265Test.testShouldParseShortOptionWithValue"></a>testShouldParseShortOptionWithValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI265Test.testShouldParseConcatenatedShortOptions"></a>testShouldParseConcatenatedShortOptions</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.ParseExceptionTest"></a>
<h3>ParseExceptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ParseExceptionTest.testConstructor"></a>testConstructor</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.TypeHandlerTest"></a>
<h3>TypeHandlerTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateNumber"></a>testCreateNumber</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateObject"></a>testCreateObject</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateClass"></a>testCreateClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateFiles"></a>testCreateFiles</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B1.5D"></a>testCreateValue(String, Class, Object)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B2.5D"></a>testCreateValue(String, Class, Object)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B3.5D"></a>testCreateValue(String, Class, Object)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B4.5D"></a>testCreateValue(String, Class, Object)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B5.5D"></a>testCreateValue(String, Class, Object)[5]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B6.5D"></a>testCreateValue(String, Class, Object)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B7.5D"></a>testCreateValue(String, Class, Object)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B8.5D"></a>testCreateValue(String, Class, Object)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B9.5D"></a>testCreateValue(String, Class, Object)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B10.5D"></a>testCreateValue(String, Class, Object)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B11.5D"></a>testCreateValue(String, Class, Object)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B12.5D"></a>testCreateValue(String, Class, Object)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B13.5D"></a>testCreateValue(String, Class, Object)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B14.5D"></a>testCreateValue(String, Class, Object)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B15.5D"></a>testCreateValue(String, Class, Object)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B16.5D"></a>testCreateValue(String, Class, Object)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B17.5D"></a>testCreateValue(String, Class, Object)[17]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B18.5D"></a>testCreateValue(String, Class, Object)[18]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B19.5D"></a>testCreateValue(String, Class, Object)[19]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B20.5D"></a>testCreateValue(String, Class, Object)[20]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B21.5D"></a>testCreateValue(String, Class, Object)[21]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B22.5D"></a>testCreateValue(String, Class, Object)[22]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B23.5D"></a>testCreateValue(String, Class, Object)[23]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B24.5D"></a>testCreateValue(String, Class, Object)[24]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B25.5D"></a>testCreateValue(String, Class, Object)[25]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B26.5D"></a>testCreateValue(String, Class, Object)[26]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B27.5D"></a>testCreateValue(String, Class, Object)[27]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B28.5D"></a>testCreateValue(String, Class, Object)[28]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B29.5D"></a>testCreateValue(String, Class, Object)[29]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B30.5D"></a>testCreateValue(String, Class, Object)[30]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B31.5D"></a>testCreateValue(String, Class, Object)[31]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B32.5D"></a>testCreateValue(String, Class, Object)[32]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B33.5D"></a>testCreateValue(String, Class, Object)[33]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B34.5D"></a>testCreateValue(String, Class, Object)[34]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B35.5D"></a>testCreateValue(String, Class, Object)[35]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B36.5D"></a>testCreateValue(String, Class, Object)[36]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B37.5D"></a>testCreateValue(String, Class, Object)[37]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B38.5D"></a>testCreateValue(String, Class, Object)[38]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B39.5D"></a>testCreateValue(String, Class, Object)[39]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B40.5D"></a>testCreateValue(String, Class, Object)[40]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B41.5D"></a>testCreateValue(String, Class, Object)[41]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B42.5D"></a>testCreateValue(String, Class, Object)[42]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B43.5D"></a>testCreateValue(String, Class, Object)[43]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B44.5D"></a>testCreateValue(String, Class, Object)[44]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B45.5D"></a>testCreateValue(String, Class, Object)[45]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B46.5D"></a>testCreateValue(String, Class, Object)[46]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B47.5D"></a>testCreateValue(String, Class, Object)[47]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B48.5D"></a>testCreateValue(String, Class, Object)[48]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B49.5D"></a>testCreateValue(String, Class, Object)[49]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValue.28String.2C_Class.2C_Object.29.5B50.5D"></a>testCreateValue(String, Class, Object)[50]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testRegister"></a>testRegister</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testOpenFile"></a>testOpenFile</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateValueExistingFile"></a>testCreateValueExistingFile</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateDate.28Date.29.5B1.5D"></a>testCreateDate(Date)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateDate.28Date.29.5B2.5D"></a>testCreateDate(Date)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateDate.28Date.29.5B3.5D"></a>testCreateDate(Date)[3]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateFile"></a>testCreateFile</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testCreateURL"></a>testCreateURL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.TypeHandlerTest.testnstantiableEquals"></a>testnstantiableEquals</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.SolrCliTest"></a>
<h3>SolrCliTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.SolrCliTest.testOptions"></a>testOptions</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.PosixParserTest"></a>
<h3>PosixParserTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testSimpleLong"></a>testSimpleLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testSimpleShort"></a>testSimpleShort</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongOptionQuoteHandling"></a>testLongOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testOptionalArgsOptionBuilder"></a>testOptionalArgsOptionBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testStopBursting2"></a>testStopBursting2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMissingRequiredOption"></a>testMissingRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testShortWithoutEqual"></a>testShortWithoutEqual</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testReuseOptionsTwice"></a>testReuseOptionsTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMissingRequiredGroup"></a>testMissingRequiredGroup</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testOptionGroupLong"></a>testOptionGroupLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongOptionWithEqualsQuoteHandling"></a>testLongOptionWithEqualsQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMissingArgWithBursting"></a>testMissingArgWithBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMissingRequiredOptions"></a>testMissingRequiredOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testShortWithUnexpectedArgument"></a>testShortWithUnexpectedArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOverrideValues"></a>testPropertyOverrideValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testStopAtNonOptionLong"></a>testStopAtNonOptionLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testNegativeArgument"></a>testNegativeArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testOptionalArgsOptionDotBuilder"></a>testOptionalArgsOptionDotBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testStopBursting"></a>testStopBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testStopAtUnexpectedArg"></a>testStopAtUnexpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPartialLongOptionSingleDash"></a>testPartialLongOptionSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testOptionGroup"></a>testOptionGroup</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongWithoutEqualDoubleDash"></a>testLongWithoutEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOptionSingularValue"></a>testPropertyOptionSingularValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOptionMultipleValues"></a>testPropertyOptionMultipleValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMissingArg"></a>testMissingArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOptionFlags"></a>testPropertyOptionFlags</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOptionGroup"></a>testPropertyOptionGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnrecognizedOptionWithBursting"></a>testUnrecognizedOptionWithBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousArgParsing"></a>testAmbiguousArgParsing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMultipleWithLong"></a>testMultipleWithLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMultipleWithNull"></a>testMultipleWithNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnrecognizedOption"></a>testUnrecognizedOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testBursting"></a>testBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption1"></a>testAmbiguousPartialLongOption1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption2"></a>testAmbiguousPartialLongOption2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption3"></a>testAmbiguousPartialLongOption3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOptionUnexpected"></a>testPropertyOptionUnexpected</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testSingleDash"></a>testSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testWithRequiredOption"></a>testWithRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnlimitedArgs"></a>testUnlimitedArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertyOptionRequired"></a>testPropertyOptionRequired</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testOptionAndRequiredOption"></a>testOptionAndRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongWithEqualDoubleDash"></a>testLongWithEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument2"></a>testLongWithUnexpectedArgument2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testStopAtNonOptionShort"></a>testStopAtNonOptionShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption1"></a>testUnambiguousPartialLongOption1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption2"></a>testUnambiguousPartialLongOption2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption3"></a>testUnambiguousPartialLongOption3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testShortOptionConcatenatedQuoteHandling"></a>testShortOptionConcatenatedQuoteHandling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testMultiple"></a>testMultiple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testArgumentStartingWithHyphen"></a>testArgumentStartingWithHyphen</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertiesOption1"></a>testPropertiesOption1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testPropertiesOption2"></a>testPropertiesOption2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testDoubleDash1"></a>testDoubleDash1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testStopAtExpectedArg"></a>testStopAtExpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testShortOptionQuoteHandling"></a>testShortOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testambiguouslongwithoutequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testambiguouslongwithoutequalsingledash">testAmbiguousLongWithoutEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash');"><span id="org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testlongwithoutequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongWithoutEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testlongwithoutequalsingledash">testLongWithoutEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testLongWithoutEqualSingleDash');"><span id="org.apache.commons.cli.PosixParserTest.testLongWithoutEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testLongWithoutEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testambiguouspartiallongoption4"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption4"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testambiguouspartiallongoption4">testAmbiguousPartialLongOption4</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption4');"><span id="org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption4-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption4-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testshortwithequal"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testShortWithEqual"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testshortwithequal">testShortWithEqual</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testShortWithEqual');"><span id="org.apache.commons.cli.PosixParserTest.testShortWithEqual-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testShortWithEqual-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testnegativeoption"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testNegativeOption"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testnegativeoption">testNegativeOption</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testNegativeOption');"><span id="org.apache.commons.cli.PosixParserTest.testNegativeOption-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testNegativeOption-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser (CLI-184)</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testlongwithunexpectedargument1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument1"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testlongwithunexpectedargument1">testLongWithUnexpectedArgument1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument1');"><span id="org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument1-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testlongwithequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testLongWithEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testlongwithequalsingledash">testLongWithEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testLongWithEqualSingleDash');"><span id="org.apache.commons.cli.PosixParserTest.testLongWithEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testLongWithEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testunambiguouspartiallongoption4"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption4"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testunambiguouspartiallongoption4">testUnambiguousPartialLongOption4</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption4');"><span id="org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption4-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption4-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testdoubledash2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testDoubleDash2"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testdoubledash2">testDoubleDash2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testDoubleDash2');"><span id="org.apache.commons.cli.PosixParserTest.testDoubleDash2-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testDoubleDash2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.posixparsertest.testambiguouslongwithoutequalsingledash2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a><a href="#surefire--org.apache.commons.cli.posixparsertest.testambiguouslongwithoutequalsingledash2">testAmbiguousLongWithoutEqualSingleDash2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash2');"><span id="org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash2-off"> + </span><span id="org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the PosixParser</td>
<td>-</td></tr></table></section><section><a id="org.apache.commons.cli.example.AptHelpAppendableTest"></a>
<h3>AptHelpAppendableTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendTitleTest"></a>testAppendTitleTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendTableTest"></a>testAppendTableTest</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendParagraphTest"></a>testAppendParagraphTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendHeaderTest"></a>testAppendHeaderTest</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendListTest"></a>testAppendListTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendParagraphFormatTest"></a>testAppendParagraphFormatTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.AptHelpAppendableTest.testAppendFormatTest"></a>testAppendFormatTest</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.ValueTest"></a>
<h3>ValueTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValuesWithOption.28CommandLineParser.29.5B1.5D"></a>testLongOptionalArgValuesWithOption(CommandLineParser)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValuesWithOption.28CommandLineParser.29.5B2.5D"></a>testLongOptionalArgValuesWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalNArgValuesWithOption"></a>testShortOptionalNArgValuesWithOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValues.28CommandLineParser.29.5B1.5D"></a>testShortOptionalArgValues(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValues.28CommandLineParser.29.5B2.5D"></a>testShortOptionalArgValues(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValuesWithOption.28CommandLineParser.29.5B1.5D"></a>testShortOptionalArgValuesWithOption(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValuesWithOption.28CommandLineParser.29.5B2.5D"></a>testShortOptionalArgValuesWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValueWithOption.28CommandLineParser.29.5B1.5D"></a>testShortOptionalArgValueWithOption(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValueWithOption.28CommandLineParser.29.5B2.5D"></a>testShortOptionalArgValueWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValue.28CommandLineParser.29.5B1.5D"></a>testLongOptionalArgValue(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValue.28CommandLineParser.29.5B2.5D"></a>testLongOptionalArgValue(CommandLineParser)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgNoValue.28CommandLineParser.29.5B1.5D"></a>testShortOptionalArgNoValue(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgNoValue.28CommandLineParser.29.5B2.5D"></a>testShortOptionalArgNoValue(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortNoArgWithOption"></a>testShortNoArgWithOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongWithArg"></a>testLongWithArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNArgValuesWithOption.28CommandLineParser.29.5B1.5D"></a>testLongOptionalNArgValuesWithOption(CommandLineParser)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNArgValuesWithOption.28CommandLineParser.29.5B2.5D"></a>testLongOptionalNArgValuesWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNArgValues.28CommandLineParser.29.5B1.5D"></a>testLongOptionalNArgValues(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNArgValues.28CommandLineParser.29.5B2.5D"></a>testLongOptionalNArgValues(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortWithArgWithOption"></a>testShortWithArgWithOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortWithArg"></a>testShortWithArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalNArgValuesSeparated"></a>testShortOptionalNArgValuesSeparated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValueWithOption.28CommandLineParser.29.5B1.5D"></a>testLongOptionalArgValueWithOption(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValueWithOption.28CommandLineParser.29.5B2.5D"></a>testLongOptionalArgValueWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValues.28CommandLineParser.29.5B1.5D"></a>testLongOptionalArgValues(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalArgValues.28CommandLineParser.29.5B2.5D"></a>testLongOptionalArgValues(CommandLineParser)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalNArgValues.28CommandLineParser.29.5B1.5D"></a>testShortOptionalNArgValues(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalNArgValues.28CommandLineParser.29.5B2.5D"></a>testShortOptionalNArgValues(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongNoArgWithOption"></a>testLongNoArgWithOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNoValueWithOption.28CommandLineParser.29.5B1.5D"></a>testLongOptionalNoValueWithOption(CommandLineParser)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNoValueWithOption.28CommandLineParser.29.5B2.5D"></a>testLongOptionalNoValueWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongNoArg"></a>testLongNoArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortNoArg"></a>testShortNoArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNoValue.28CommandLineParser.29.5B1.5D"></a>testLongOptionalNoValue(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongOptionalNoValue.28CommandLineParser.29.5B2.5D"></a>testLongOptionalNoValue(CommandLineParser)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValue.28CommandLineParser.29.5B1.5D"></a>testShortOptionalArgValue(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgValue.28CommandLineParser.29.5B2.5D"></a>testShortOptionalArgValue(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgNoValueWithOption.28CommandLineParser.29.5B1.5D"></a>testShortOptionalArgNoValueWithOption(CommandLineParser)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testShortOptionalArgNoValueWithOption.28CommandLineParser.29.5B2.5D"></a>testShortOptionalArgNoValueWithOption(CommandLineParser)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValueTest.testLongWithArgWithOption"></a>testLongWithArgWithOption</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.OptionValidatorTest"></a>
<h3>OptionValidatorTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B1.5D"></a>testValidate(String, boolean, String)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B2.5D"></a>testValidate(String, boolean, String)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B3.5D"></a>testValidate(String, boolean, String)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B4.5D"></a>testValidate(String, boolean, String)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B5.5D"></a>testValidate(String, boolean, String)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B6.5D"></a>testValidate(String, boolean, String)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B7.5D"></a>testValidate(String, boolean, String)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B8.5D"></a>testValidate(String, boolean, String)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B9.5D"></a>testValidate(String, boolean, String)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B10.5D"></a>testValidate(String, boolean, String)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B11.5D"></a>testValidate(String, boolean, String)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B12.5D"></a>testValidate(String, boolean, String)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B13.5D"></a>testValidate(String, boolean, String)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B14.5D"></a>testValidate(String, boolean, String)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B15.5D"></a>testValidate(String, boolean, String)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B16.5D"></a>testValidate(String, boolean, String)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B17.5D"></a>testValidate(String, boolean, String)[17]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B18.5D"></a>testValidate(String, boolean, String)[18]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B19.5D"></a>testValidate(String, boolean, String)[19]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B20.5D"></a>testValidate(String, boolean, String)[20]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B21.5D"></a>testValidate(String, boolean, String)[21]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B22.5D"></a>testValidate(String, boolean, String)[22]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B23.5D"></a>testValidate(String, boolean, String)[23]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B24.5D"></a>testValidate(String, boolean, String)[24]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B25.5D"></a>testValidate(String, boolean, String)[25]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B26.5D"></a>testValidate(String, boolean, String)[26]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B27.5D"></a>testValidate(String, boolean, String)[27]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B28.5D"></a>testValidate(String, boolean, String)[28]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B29.5D"></a>testValidate(String, boolean, String)[29]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B30.5D"></a>testValidate(String, boolean, String)[30]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B31.5D"></a>testValidate(String, boolean, String)[31]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B32.5D"></a>testValidate(String, boolean, String)[32]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B33.5D"></a>testValidate(String, boolean, String)[33]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B34.5D"></a>testValidate(String, boolean, String)[34]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B35.5D"></a>testValidate(String, boolean, String)[35]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B36.5D"></a>testValidate(String, boolean, String)[36]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B37.5D"></a>testValidate(String, boolean, String)[37]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B38.5D"></a>testValidate(String, boolean, String)[38]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B39.5D"></a>testValidate(String, boolean, String)[39]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B40.5D"></a>testValidate(String, boolean, String)[40]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B41.5D"></a>testValidate(String, boolean, String)[41]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B42.5D"></a>testValidate(String, boolean, String)[42]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B43.5D"></a>testValidate(String, boolean, String)[43]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B44.5D"></a>testValidate(String, boolean, String)[44]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B45.5D"></a>testValidate(String, boolean, String)[45]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B46.5D"></a>testValidate(String, boolean, String)[46]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B47.5D"></a>testValidate(String, boolean, String)[47]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B48.5D"></a>testValidate(String, boolean, String)[48]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B49.5D"></a>testValidate(String, boolean, String)[49]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B50.5D"></a>testValidate(String, boolean, String)[50]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B51.5D"></a>testValidate(String, boolean, String)[51]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B52.5D"></a>testValidate(String, boolean, String)[52]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B53.5D"></a>testValidate(String, boolean, String)[53]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B54.5D"></a>testValidate(String, boolean, String)[54]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B55.5D"></a>testValidate(String, boolean, String)[55]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B56.5D"></a>testValidate(String, boolean, String)[56]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B57.5D"></a>testValidate(String, boolean, String)[57]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B58.5D"></a>testValidate(String, boolean, String)[58]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B59.5D"></a>testValidate(String, boolean, String)[59]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B60.5D"></a>testValidate(String, boolean, String)[60]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B61.5D"></a>testValidate(String, boolean, String)[61]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B62.5D"></a>testValidate(String, boolean, String)[62]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B63.5D"></a>testValidate(String, boolean, String)[63]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B64.5D"></a>testValidate(String, boolean, String)[64]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B65.5D"></a>testValidate(String, boolean, String)[65]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B66.5D"></a>testValidate(String, boolean, String)[66]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B67.5D"></a>testValidate(String, boolean, String)[67]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B68.5D"></a>testValidate(String, boolean, String)[68]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B69.5D"></a>testValidate(String, boolean, String)[69]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B70.5D"></a>testValidate(String, boolean, String)[70]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B71.5D"></a>testValidate(String, boolean, String)[71]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B72.5D"></a>testValidate(String, boolean, String)[72]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B73.5D"></a>testValidate(String, boolean, String)[73]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B74.5D"></a>testValidate(String, boolean, String)[74]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B75.5D"></a>testValidate(String, boolean, String)[75]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B76.5D"></a>testValidate(String, boolean, String)[76]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B77.5D"></a>testValidate(String, boolean, String)[77]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B78.5D"></a>testValidate(String, boolean, String)[78]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B79.5D"></a>testValidate(String, boolean, String)[79]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B80.5D"></a>testValidate(String, boolean, String)[80]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B81.5D"></a>testValidate(String, boolean, String)[81]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B82.5D"></a>testValidate(String, boolean, String)[82]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B83.5D"></a>testValidate(String, boolean, String)[83]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B84.5D"></a>testValidate(String, boolean, String)[84]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B85.5D"></a>testValidate(String, boolean, String)[85]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B86.5D"></a>testValidate(String, boolean, String)[86]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B87.5D"></a>testValidate(String, boolean, String)[87]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B88.5D"></a>testValidate(String, boolean, String)[88]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B89.5D"></a>testValidate(String, boolean, String)[89]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B90.5D"></a>testValidate(String, boolean, String)[90]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B91.5D"></a>testValidate(String, boolean, String)[91]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B92.5D"></a>testValidate(String, boolean, String)[92]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B93.5D"></a>testValidate(String, boolean, String)[93]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B94.5D"></a>testValidate(String, boolean, String)[94]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B95.5D"></a>testValidate(String, boolean, String)[95]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B96.5D"></a>testValidate(String, boolean, String)[96]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B97.5D"></a>testValidate(String, boolean, String)[97]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B98.5D"></a>testValidate(String, boolean, String)[98]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B99.5D"></a>testValidate(String, boolean, String)[99]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B100.5D"></a>testValidate(String, boolean, String)[100]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B101.5D"></a>testValidate(String, boolean, String)[101]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B102.5D"></a>testValidate(String, boolean, String)[102]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B103.5D"></a>testValidate(String, boolean, String)[103]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B104.5D"></a>testValidate(String, boolean, String)[104]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B105.5D"></a>testValidate(String, boolean, String)[105]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B106.5D"></a>testValidate(String, boolean, String)[106]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B107.5D"></a>testValidate(String, boolean, String)[107]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B108.5D"></a>testValidate(String, boolean, String)[108]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B109.5D"></a>testValidate(String, boolean, String)[109]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B110.5D"></a>testValidate(String, boolean, String)[110]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B111.5D"></a>testValidate(String, boolean, String)[111]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B112.5D"></a>testValidate(String, boolean, String)[112]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B113.5D"></a>testValidate(String, boolean, String)[113]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testValidate.28String.2C_boolean.2C_String.29.5B114.5D"></a>testValidate(String, boolean, String)[114]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionValidatorTest.testExclusivity"></a>testExclusivity</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI18Test"></a>
<h3>BugCLI18Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI18Test.testCLI18"></a>testCLI18</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.OptionTest"></a>
<h3>OptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testGetValue"></a>testGetValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testSerialization"></a>testSerialization</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testSubclass"></a>testSubclass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testProcessValue"></a>testProcessValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testClear"></a>testClear</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testClone"></a>testClone</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderDeprecatedBuildEmpty"></a>testBuilderDeprecatedBuildEmpty</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInvalidOptionName0"></a>testBuilderInvalidOptionName0</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInvalidOptionName1"></a>testBuilderInvalidOptionName1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInvalidOptionName2"></a>testBuilderInvalidOptionName2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInvalidOptionName3"></a>testBuilderInvalidOptionName3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInvalidOptionName4"></a>testBuilderInvalidOptionName4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testAddValue"></a>testAddValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderMethods"></a>testBuilderMethods</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testHasArgs"></a>testHasArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testHasArgName"></a>testHasArgName</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderEmpty"></a>testBuilderEmpty</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testTypeClass"></a>testTypeClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testEquals"></a>testEquals</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInsufficientParams1"></a>testBuilderInsufficientParams1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testBuilderInsufficientParams2"></a>testBuilderInsufficientParams2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionTest.testTypeObject"></a>testTypeObject</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.PatternOptionBuilderTest"></a>
<h3>PatternOptionBuilderTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testSimplePattern"></a>testSimplePattern</td>
<td>0.056 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testExistingFilePattern"></a>testExistingFilePattern</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testURLPattern"></a>testURLPattern</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testEmptyPattern"></a>testEmptyPattern</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testClassPattern"></a>testClassPattern</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testRequiredOption"></a>testRequiredOption</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testExistingFilePatternFileNotExist"></a>testExistingFilePatternFileNotExist</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testNumberPattern"></a>testNumberPattern</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testUntypedPattern"></a>testUntypedPattern</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.PatternOptionBuilderTest.testObjectPattern"></a>testObjectPattern</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI162Test"></a>
<h3>BugCLI162Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI162Test.testInfiniteLoop"></a>testInfiniteLoop</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI162Test.testLongLineChunkingIndentIgnored"></a>testLongLineChunkingIndentIgnored</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI162Test.testLongLineChunking"></a>testLongLineChunking</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI162Test.testPrintHelpLongLines"></a>testPrintHelpLongLines</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI266Test"></a>
<h3>BugCLI266Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI266Test.testOptionComparatorInsertedOrder"></a>testOptionComparatorInsertedOrder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI266Test.testOptionComparatorDefaultOrder"></a>testOptionComparatorDefaultOrder</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.HelpFormatterTest"></a>
<h3>HelpFormatterTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDeprecatedPrintOptionsZeroWidth.28int.29.5B1.5D"></a>testDeprecatedPrintOptionsZeroWidth(int)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDeprecatedPrintOptionsZeroWidth.28int.29.5B2.5D"></a>testDeprecatedPrintOptionsZeroWidth(int)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDeprecatedPrintOptionsZeroWidth.28int.29.5B3.5D"></a>testDeprecatedPrintOptionsZeroWidth(int)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testUsageWithLongOptSeparator"></a>testUsageWithLongOptSeparator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B1.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B2.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B3.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B4.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B5.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B6.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B7.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintDeprecatedOptions.28HelpFormatter.2C_Option.2C_String.29.5B8.5D"></a>testPrintDeprecatedOptions(HelpFormatter, Option, String)[8]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderWrappedTextSingleLine"></a>testRenderWrappedTextSingleLine</td>
<td>0.261 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testIndentedHeaderAndFooter"></a>testIndentedHeaderAndFooter</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintSortedUsageWithNullComparator"></a>testPrintSortedUsageWithNullComparator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testAccessors"></a>testAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDeprecatedFindWrapPosZeroWidth.28int.29.5B1.5D"></a>testDeprecatedFindWrapPosZeroWidth(int)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDeprecatedFindWrapPosZeroWidth.28int.29.5B2.5D"></a>testDeprecatedFindWrapPosZeroWidth(int)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDeprecatedFindWrapPosZeroWidth.28int.29.5B3.5D"></a>testDeprecatedFindWrapPosZeroWidth(int)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRtrim"></a>testRtrim</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintRequiredOptionGroupUsage"></a>testPrintRequiredOptionGroupUsage</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testHelpWithLongOptSeparator"></a>testHelpWithLongOptSeparator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderWrappedTextSingleLinePadded"></a>testRenderWrappedTextSingleLinePadded</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderWrappedTextMultiLine"></a>testRenderWrappedTextMultiLine</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintUsage"></a>testPrintUsage</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintSortedUsage"></a>testPrintSortedUsage</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintHelpWithEmptySyntax"></a>testPrintHelpWithEmptySyntax</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintOptions"></a>testPrintOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testAutomaticUsage"></a>testAutomaticUsage</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testDefaultArgName"></a>testDefaultArgName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintHelpNewlineFooter"></a>testPrintHelpNewlineFooter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintHelpNewlineHeader"></a>testPrintHelpNewlineHeader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderWrappedTextWordCut"></a>testRenderWrappedTextWordCut</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testHeaderStartingWithLineSeparator0"></a>testHeaderStartingWithLineSeparator0</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testHeaderStartingWithLineSeparator1"></a>testHeaderStartingWithLineSeparator1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testOptionWithoutShortFormat"></a>testOptionWithoutShortFormat</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderWrappedTextMultiLinePadded"></a>testRenderWrappedTextMultiLinePadded</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintOptionGroupUsage"></a>testPrintOptionGroupUsage</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintOptionWithEmptyArgNameUsage"></a>testPrintOptionWithEmptyArgNameUsage</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderWrappedTextSingleLinePadded2"></a>testRenderWrappedTextSingleLinePadded2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testOptionWithoutShortFormat2"></a>testOptionWithoutShortFormat2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testFindWrapPos"></a>testFindWrapPos</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testRenderSince"></a>testRenderSince</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.HelpFormatterTest.testPrintHelpWithSince"></a>testPrintHelpWithSince</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.UtilTest"></a>
<h3>UtilTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.UtilTest.testStripLeadingAndTrailingQuotes"></a>testStripLeadingAndTrailingQuotes</td>
<td>0.010 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.UtilTest.testStripLeadingHyphens"></a>testStripLeadingHyphens</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI148Test"></a>
<h3>BugCLI148Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI148Test.testWorkaround1"></a>testWorkaround1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI148Test.testWorkaround2"></a>testWorkaround2</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI312Test"></a>
<h3>BugCLI312Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI312Test.testNoOptionValues"></a>testNoOptionValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI312Test.testPropertyStyleOption_withGetOptionProperties"></a>testPropertyStyleOption_withGetOptionProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI312Test.testPropertyStyleOption_withGetOptions"></a>testPropertyStyleOption_withGetOptions</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI133Test"></a>
<h3>BugCLI133Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI133Test.testOrder"></a>testOrder</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.DefaultParserTest"></a>
<h3>DefaultParserTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testSimpleLong"></a>testSimpleLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testSimpleShort"></a>testSimpleShort</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongOptionQuoteHandling"></a>testLongOptionQuoteHandling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testOptionalArgsOptionBuilder"></a>testOptionalArgsOptionBuilder</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testStopBursting2"></a>testStopBursting2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMissingRequiredOption"></a>testMissingRequiredOption</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testShortWithoutEqual"></a>testShortWithoutEqual</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testReuseOptionsTwice"></a>testReuseOptionsTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMissingRequiredGroup"></a>testMissingRequiredGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testOptionGroupLong"></a>testOptionGroupLong</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousLongWithoutEqualSingleDash"></a>testAmbiguousLongWithoutEqualSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMissingArgWithBursting"></a>testMissingArgWithBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMissingRequiredOptions"></a>testMissingRequiredOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testShortWithUnexpectedArgument"></a>testShortWithUnexpectedArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOverrideValues"></a>testPropertyOverrideValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testStopAtNonOptionLong"></a>testStopAtNonOptionLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testNegativeArgument"></a>testNegativeArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testOptionalArgsOptionDotBuilder"></a>testOptionalArgsOptionDotBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testStopBursting"></a>testStopBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testStopAtUnexpectedArg"></a>testStopAtUnexpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPartialLongOptionSingleDash"></a>testPartialLongOptionSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testOptionGroup"></a>testOptionGroup</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongWithoutEqualDoubleDash"></a>testLongWithoutEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongWithoutEqualSingleDash"></a>testLongWithoutEqualSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOptionSingularValue"></a>testPropertyOptionSingularValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOptionMultipleValues"></a>testPropertyOptionMultipleValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMissingArg"></a>testMissingArg</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOptionFlags"></a>testPropertyOptionFlags</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOptionGroup"></a>testPropertyOptionGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnrecognizedOptionWithBursting"></a>testUnrecognizedOptionWithBursting</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousArgParsing"></a>testAmbiguousArgParsing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMultipleWithLong"></a>testMultipleWithLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMultipleWithNull"></a>testMultipleWithNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnrecognizedOption"></a>testUnrecognizedOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testBursting"></a>testBursting</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousPartialLongOption1"></a>testAmbiguousPartialLongOption1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousPartialLongOption2"></a>testAmbiguousPartialLongOption2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousPartialLongOption3"></a>testAmbiguousPartialLongOption3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousPartialLongOption4"></a>testAmbiguousPartialLongOption4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOptionUnexpected"></a>testPropertyOptionUnexpected</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testSingleDash"></a>testSingleDash</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testShortWithEqual"></a>testShortWithEqual</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testWithRequiredOption"></a>testWithRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnlimitedArgs"></a>testUnlimitedArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testNegativeOption"></a>testNegativeOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertyOptionRequired"></a>testPropertyOptionRequired</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testOptionAndRequiredOption"></a>testOptionAndRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongWithEqualDoubleDash"></a>testLongWithEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongWithUnexpectedArgument1"></a>testLongWithUnexpectedArgument1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongWithUnexpectedArgument2"></a>testLongWithUnexpectedArgument2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testStopAtNonOptionShort"></a>testStopAtNonOptionShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongWithEqualSingleDash"></a>testLongWithEqualSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnambiguousPartialLongOption1"></a>testUnambiguousPartialLongOption1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnambiguousPartialLongOption2"></a>testUnambiguousPartialLongOption2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnambiguousPartialLongOption3"></a>testUnambiguousPartialLongOption3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testUnambiguousPartialLongOption4"></a>testUnambiguousPartialLongOption4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testMultiple"></a>testMultiple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testArgumentStartingWithHyphen"></a>testArgumentStartingWithHyphen</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertiesOption1"></a>testPropertiesOption1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testPropertiesOption2"></a>testPropertiesOption2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testDoubleDash1"></a>testDoubleDash1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testDoubleDash2"></a>testDoubleDash2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testStopAtExpectedArg"></a>testStopAtExpectedArg</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a>testAmbiguousLongWithoutEqualSingleDash2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testShortOptionQuoteHandling"></a>testShortOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParseSkipNonHappyPath"></a>testParseSkipNonHappyPath</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParseSkipHappyPath"></a>testParseSkipHappyPath</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.defaultparsertest.testlongoptionwithequalsquotehandling"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLongOptionWithEqualsQuoteHandling"></a><a href="#surefire--org.apache.commons.cli.defaultparsertest.testlongoptionwithequalsquotehandling">testLongOptionWithEqualsQuoteHandling</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.DefaultParserTest.testLongOptionWithEqualsQuoteHandling');"><span id="org.apache.commons.cli.DefaultParserTest.testLongOptionWithEqualsQuoteHandling-off"> + </span><span id="org.apache.commons.cli.DefaultParserTest.testLongOptionWithEqualsQuoteHandling-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>Test case handled in the parameterized tests as "DEFAULT behavior"</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParseIgnoreHappyPath"></a>testParseIgnoreHappyPath</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testBuilder"></a>testBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testLegacyStopAtNonOption"></a>testLegacyStopAtNonOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParseNullOption"></a>testParseNullOption</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParseIgnoreNonHappyPath"></a>testParseIgnoreNonHappyPath</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.defaultparsertest.testshortoptionconcatenatedquotehandling"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testShortOptionConcatenatedQuoteHandling"></a><a href="#surefire--org.apache.commons.cli.defaultparsertest.testshortoptionconcatenatedquotehandling">testShortOptionConcatenatedQuoteHandling</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.DefaultParserTest.testShortOptionConcatenatedQuoteHandling');"><span id="org.apache.commons.cli.DefaultParserTest.testShortOptionConcatenatedQuoteHandling-off"> + </span><span id="org.apache.commons.cli.DefaultParserTest.testShortOptionConcatenatedQuoteHandling-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>Test case handled in the parameterized tests as "DEFAULT behavior"</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B1.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[1]</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B2.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B3.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B4.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B5.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B6.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B7.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[7]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B8.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B9.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[9]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B10.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B11.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testParameterized.28String.2C_CommandLineParser.2C_String.5B.5D.2C_String.2C_String.2C_String.29.5B12.5D"></a>testParameterized(String, CommandLineParser, String[], String, String, String)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DefaultParserTest.testDeprecated"></a>testDeprecated</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.cli.help.HelpFormatterTest"></a>
<h3>HelpFormatterTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testToArgNameTest"></a>testToArgNameTest</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.verifyOptionGroupingOutput"></a>verifyOptionGroupingOutput</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testToSyntaxOptionGroupTest"></a>testToSyntaxOptionGroupTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testPrintHelp"></a>testPrintHelp</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testSetOptionFormatBuilderTest"></a>testSetOptionFormatBuilderTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testPrintHelpWithIterableOptions"></a>testPrintHelpWithIterableOptions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testSyntaxPrefix"></a>testSyntaxPrefix</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testPrintOptions"></a>testPrintOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testToSyntaxOptionIterableTest"></a>testToSyntaxOptionIterableTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testToSyntaxOptionOptionsTest"></a>testToSyntaxOptionOptionsTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testSetOptionGroupSeparatorTest"></a>testSetOptionGroupSeparatorTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testPrintHelpHeader"></a>testPrintHelpHeader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testSortOptionGroupsTest"></a>testSortOptionGroupsTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testSortOptionsTest"></a>testSortOptionsTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testDefault"></a>testDefault</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.HelpFormatterTest.testPrintHelpXML"></a>testPrintHelpXML</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.OptionsTest"></a>
<h3>OptionsTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testAddOptions2X"></a>testAddOptions2X</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testMissingOptionsException"></a>testMissingOptionsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testGetMatchingOpts"></a>testGetMatchingOpts</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testLong"></a>testLong</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testHelpOptions"></a>testHelpOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testAddOptions"></a>testAddOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testMissingOptionException"></a>testMissingOptionException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testDuplicateSimple"></a>testDuplicateSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testAddNonConflictingOptions"></a>testAddNonConflictingOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testAddConflictingOptions"></a>testAddConflictingOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testGetOptionsGroups"></a>testGetOptionsGroups</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testDuplicateLong"></a>testDuplicateLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testDeprecated"></a>testDeprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionsTest.testRequiredOptionInGroupShouldNotBeInRequiredList"></a>testRequiredOptionInGroupShouldNotBeInRequiredList</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.ArgumentIsOptionTest"></a>
<h3>ArgumentIsOptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ArgumentIsOptionTest.testOptionWithArgument"></a>testOptionWithArgument</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ArgumentIsOptionTest.testOptionAndOptionWithArgument"></a>testOptionAndOptionWithArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ArgumentIsOptionTest.testOption"></a>testOption</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.BasicParserTest"></a>
<h3>BasicParserTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testSimpleLong"></a>testSimpleLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testSimpleShort"></a>testSimpleShort</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongOptionQuoteHandling"></a>testLongOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testOptionalArgsOptionBuilder"></a>testOptionalArgsOptionBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMissingRequiredOption"></a>testMissingRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testReuseOptionsTwice"></a>testReuseOptionsTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMissingRequiredGroup"></a>testMissingRequiredGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testOptionGroupLong"></a>testOptionGroupLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMissingRequiredOptions"></a>testMissingRequiredOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testShortWithUnexpectedArgument"></a>testShortWithUnexpectedArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOverrideValues"></a>testPropertyOverrideValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testStopAtNonOptionLong"></a>testStopAtNonOptionLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testNegativeArgument"></a>testNegativeArgument</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testOptionalArgsOptionDotBuilder"></a>testOptionalArgsOptionDotBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testStopAtUnexpectedArg"></a>testStopAtUnexpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testOptionGroup"></a>testOptionGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongWithoutEqualDoubleDash"></a>testLongWithoutEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOptionSingularValue"></a>testPropertyOptionSingularValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOptionMultipleValues"></a>testPropertyOptionMultipleValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMissingArg"></a>testMissingArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOptionFlags"></a>testPropertyOptionFlags</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOptionGroup"></a>testPropertyOptionGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousArgParsing"></a>testAmbiguousArgParsing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMultipleWithLong"></a>testMultipleWithLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMultipleWithNull"></a>testMultipleWithNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnrecognizedOption"></a>testUnrecognizedOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOptionUnexpected"></a>testPropertyOptionUnexpected</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testSingleDash"></a>testSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testWithRequiredOption"></a>testWithRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnlimitedArgs"></a>testUnlimitedArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertyOptionRequired"></a>testPropertyOptionRequired</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testOptionAndRequiredOption"></a>testOptionAndRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongWithUnexpectedArgument1"></a>testLongWithUnexpectedArgument1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongWithUnexpectedArgument2"></a>testLongWithUnexpectedArgument2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testStopAtNonOptionShort"></a>testStopAtNonOptionShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMultiple"></a>testMultiple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testArgumentStartingWithHyphen"></a>testArgumentStartingWithHyphen</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testDoubleDash1"></a>testDoubleDash1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testStopAtExpectedArg"></a>testStopAtExpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testShortOptionQuoteHandling"></a>testShortOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.teststopbursting2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testStopBursting2"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.teststopbursting2">testStopBursting2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testStopBursting2');"><span id="org.apache.commons.cli.BasicParserTest.testStopBursting2-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testStopBursting2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testshortwithoutequal"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testShortWithoutEqual"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testshortwithoutequal">testShortWithoutEqual</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testShortWithoutEqual');"><span id="org.apache.commons.cli.BasicParserTest.testShortWithoutEqual-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testShortWithoutEqual-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongoptionwithequalsquotehandling"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongOptionWithEqualsQuoteHandling"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongoptionwithequalsquotehandling">testLongOptionWithEqualsQuoteHandling</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongOptionWithEqualsQuoteHandling');"><span id="org.apache.commons.cli.BasicParserTest.testLongOptionWithEqualsQuoteHandling-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testLongOptionWithEqualsQuoteHandling-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouslongwithoutequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouslongwithoutequalsingledash">testAmbiguousLongWithoutEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash');"><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testmissingargwithbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testMissingArgWithBursting"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testmissingargwithbursting">testMissingArgWithBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testMissingArgWithBursting');"><span id="org.apache.commons.cli.BasicParserTest.testMissingArgWithBursting-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testMissingArgWithBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.teststopbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testStopBursting"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.teststopbursting">testStopBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testStopBursting');"><span id="org.apache.commons.cli.BasicParserTest.testStopBursting-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testStopBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testpartiallongoptionsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPartialLongOptionSingleDash"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testpartiallongoptionsingledash">testPartialLongOptionSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testPartialLongOptionSingleDash');"><span id="org.apache.commons.cli.BasicParserTest.testPartialLongOptionSingleDash-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testPartialLongOptionSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongwithoutequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongWithoutEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongwithoutequalsingledash">testLongWithoutEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongWithoutEqualSingleDash');"><span id="org.apache.commons.cli.BasicParserTest.testLongWithoutEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testLongWithoutEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testunrecognizedoptionwithbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnrecognizedOptionWithBursting"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testunrecognizedoptionwithbursting">testUnrecognizedOptionWithBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnrecognizedOptionWithBursting');"><span id="org.apache.commons.cli.BasicParserTest.testUnrecognizedOptionWithBursting-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testUnrecognizedOptionWithBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testBursting"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testbursting">testBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testBursting');"><span id="org.apache.commons.cli.BasicParserTest.testBursting-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption1"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption1">testAmbiguousPartialLongOption1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption1');"><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption1-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption2"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption2">testAmbiguousPartialLongOption2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption2');"><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption2-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption3"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption3"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption3">testAmbiguousPartialLongOption3</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption3');"><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption3-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption3-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption4"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption4"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouspartiallongoption4">testAmbiguousPartialLongOption4</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption4');"><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption4-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption4-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testshortwithequal"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testShortWithEqual"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testshortwithequal">testShortWithEqual</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testShortWithEqual');"><span id="org.apache.commons.cli.BasicParserTest.testShortWithEqual-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testShortWithEqual-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testnegativeoption"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testNegativeOption"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testnegativeoption">testNegativeOption</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testNegativeOption');"><span id="org.apache.commons.cli.BasicParserTest.testNegativeOption-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testNegativeOption-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser (CLI-184)</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongwithequaldoubledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongWithEqualDoubleDash"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongwithequaldoubledash">testLongWithEqualDoubleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongWithEqualDoubleDash');"><span id="org.apache.commons.cli.BasicParserTest.testLongWithEqualDoubleDash-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testLongWithEqualDoubleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongwithequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testLongWithEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testlongwithequalsingledash">testLongWithEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testLongWithEqualSingleDash');"><span id="org.apache.commons.cli.BasicParserTest.testLongWithEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testLongWithEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption1"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption1">testUnambiguousPartialLongOption1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption1');"><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption1-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption2"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption2">testUnambiguousPartialLongOption2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption2');"><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption2-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption3"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption3"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption3">testUnambiguousPartialLongOption3</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption3');"><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption3-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption3-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption4"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption4"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testunambiguouspartiallongoption4">testUnambiguousPartialLongOption4</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption4');"><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption4-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption4-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testshortoptionconcatenatedquotehandling"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testShortOptionConcatenatedQuoteHandling"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testshortoptionconcatenatedquotehandling">testShortOptionConcatenatedQuoteHandling</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testShortOptionConcatenatedQuoteHandling');"><span id="org.apache.commons.cli.BasicParserTest.testShortOptionConcatenatedQuoteHandling-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testShortOptionConcatenatedQuoteHandling-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testpropertiesoption1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertiesOption1"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testpropertiesoption1">testPropertiesOption1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testPropertiesOption1');"><span id="org.apache.commons.cli.BasicParserTest.testPropertiesOption1-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testPropertiesOption1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testpropertiesoption2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testPropertiesOption2"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testpropertiesoption2">testPropertiesOption2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testPropertiesOption2');"><span id="org.apache.commons.cli.BasicParserTest.testPropertiesOption2-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testPropertiesOption2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testdoubledash2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testDoubleDash2"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testdoubledash2">testDoubleDash2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testDoubleDash2');"><span id="org.apache.commons.cli.BasicParserTest.testDoubleDash2-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testDoubleDash2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouslongwithoutequalsingledash2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a><a href="#surefire--org.apache.commons.cli.basicparsertest.testambiguouslongwithoutequalsingledash2">testAmbiguousLongWithoutEqualSingleDash2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash2');"><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash2-off"> + </span><span id="org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the BasicParser</td>
<td>-</td></tr></table></section><section><a id="org.apache.commons.cli.OptionBuilderTest"></a>
<h3>OptionBuilderTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testBaseOptionStringOpt"></a>testBaseOptionStringOpt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testTwoCompleteOptions"></a>testTwoCompleteOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testBuilderIsResettedAlways"></a>testBuilderIsResettedAlways</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testCompleteOption"></a>testCompleteOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testCreateIncompleteOption"></a>testCreateIncompleteOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testOptionArgNumbers"></a>testOptionArgNumbers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testIllegalOptions"></a>testIllegalOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testSpecialOptChars"></a>testSpecialOptChars</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionBuilderTest.testBaseOptionCharOpt"></a>testBaseOptionCharOpt</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.help.TextHelpAppendableTest"></a>
<h3>TextHelpAppendableTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppendParagraph"></a>testAppendParagraph</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppendParagraphFormat"></a>testAppendParagraphFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAdjustTableFormat"></a>testAdjustTableFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testWriteColumnQueues"></a>testWriteColumnQueues</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testPrintWrapped"></a>testPrintWrapped</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testGetStyleBuilder"></a>testGetStyleBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B1.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B2.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B3.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B4.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B5.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B6.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B7.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B8.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B9.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B10.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B11.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B12.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B13.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B14.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B15.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPosWithWhitespace.28Character.2C_boolean.29.5B16.5D"></a>testindexOfWrapPosWithWhitespace(Character, boolean)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testMakeColumnQueueWithMultipleTrailingLineBreaks"></a>testMakeColumnQueueWithMultipleTrailingLineBreaks</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testMakeColumnQueue"></a>testMakeColumnQueue</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testSetIndent"></a>testSetIndent</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testindexOfWrapPos"></a>testindexOfWrapPos</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppend"></a>testAppend</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppendList"></a>testAppendList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testResize"></a>testResize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppendTable"></a>testAppendTable</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppendTitle"></a>testAppendTitle</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testResizeTableFormat"></a>testResizeTableFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextHelpAppendableTest.testAppendHeader"></a>testAppendHeader</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.example.XhtmlHelpAppendableTest"></a>
<h3>XhtmlHelpAppendableTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.XhtmlHelpAppendableTest.testAppendTitleTest"></a>testAppendTitleTest</td>
<td>0.010 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.XhtmlHelpAppendableTest.testAppendTableTest"></a>testAppendTableTest</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.XhtmlHelpAppendableTest.testAppendParagraphTest"></a>testAppendParagraphTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.XhtmlHelpAppendableTest.testAppendHeaderTest"></a>testAppendHeaderTest</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.XhtmlHelpAppendableTest.testAppendListTest"></a>testAppendListTest</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.example.XhtmlHelpAppendableTest.testAppendParagraphFormatTest"></a>testAppendParagraphFormatTest</td>
<td>0.003 s</td></tr></table></section><section><a id="org.apache.commons.cli.DisablePartialMatchingTest"></a>
<h3>DisablePartialMatchingTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DisablePartialMatchingTest.testDisablePartialMatching"></a>testDisablePartialMatching</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DisablePartialMatchingTest.testRegularPartialMatching"></a>testRegularPartialMatching</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugCLI325Test"></a>
<h3>BugCLI325Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugCLI325Test.testCli325"></a>testCli325</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.GnuParserTest"></a>
<h3>GnuParserTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testSimpleLong"></a>testSimpleLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testSimpleShort"></a>testSimpleShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongOptionQuoteHandling"></a>testLongOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testOptionalArgsOptionBuilder"></a>testOptionalArgsOptionBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMissingRequiredOption"></a>testMissingRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testShortWithoutEqual"></a>testShortWithoutEqual</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testReuseOptionsTwice"></a>testReuseOptionsTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMissingRequiredGroup"></a>testMissingRequiredGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testOptionGroupLong"></a>testOptionGroupLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongOptionWithEqualsQuoteHandling"></a>testLongOptionWithEqualsQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMissingRequiredOptions"></a>testMissingRequiredOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOverrideValues"></a>testPropertyOverrideValues</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testStopAtNonOptionLong"></a>testStopAtNonOptionLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testNegativeArgument"></a>testNegativeArgument</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testOptionalArgsOptionDotBuilder"></a>testOptionalArgsOptionDotBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testStopAtUnexpectedArg"></a>testStopAtUnexpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testOptionGroup"></a>testOptionGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongWithoutEqualDoubleDash"></a>testLongWithoutEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOptionSingularValue"></a>testPropertyOptionSingularValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOptionMultipleValues"></a>testPropertyOptionMultipleValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMissingArg"></a>testMissingArg</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOptionFlags"></a>testPropertyOptionFlags</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOptionGroup"></a>testPropertyOptionGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousArgParsing"></a>testAmbiguousArgParsing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMultipleWithLong"></a>testMultipleWithLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMultipleWithNull"></a>testMultipleWithNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnrecognizedOption"></a>testUnrecognizedOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOptionUnexpected"></a>testPropertyOptionUnexpected</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testSingleDash"></a>testSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testShortWithEqual"></a>testShortWithEqual</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testWithRequiredOption"></a>testWithRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnlimitedArgs"></a>testUnlimitedArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertyOptionRequired"></a>testPropertyOptionRequired</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testOptionAndRequiredOption"></a>testOptionAndRequiredOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongWithEqualDoubleDash"></a>testLongWithEqualDoubleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testStopAtNonOptionShort"></a>testStopAtNonOptionShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongWithEqualSingleDash"></a>testLongWithEqualSingleDash</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testShortOptionConcatenatedQuoteHandling"></a>testShortOptionConcatenatedQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMultiple"></a>testMultiple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testArgumentStartingWithHyphen"></a>testArgumentStartingWithHyphen</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertiesOption1"></a>testPropertiesOption1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPropertiesOption2"></a>testPropertiesOption2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testDoubleDash1"></a>testDoubleDash1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testStopAtExpectedArg"></a>testStopAtExpectedArg</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testShortOptionQuoteHandling"></a>testShortOptionQuoteHandling</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.teststopbursting2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testStopBursting2"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.teststopbursting2">testStopBursting2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testStopBursting2');"><span id="org.apache.commons.cli.GnuParserTest.testStopBursting2-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testStopBursting2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouslongwithoutequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouslongwithoutequalsingledash">testAmbiguousLongWithoutEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash');"><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testmissingargwithbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testMissingArgWithBursting"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testmissingargwithbursting">testMissingArgWithBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testMissingArgWithBursting');"><span id="org.apache.commons.cli.GnuParserTest.testMissingArgWithBursting-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testMissingArgWithBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testshortwithunexpectedargument"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testShortWithUnexpectedArgument"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testshortwithunexpectedargument">testShortWithUnexpectedArgument</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testShortWithUnexpectedArgument');"><span id="org.apache.commons.cli.GnuParserTest.testShortWithUnexpectedArgument-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testShortWithUnexpectedArgument-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.teststopbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testStopBursting"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.teststopbursting">testStopBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testStopBursting');"><span id="org.apache.commons.cli.GnuParserTest.testStopBursting-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testStopBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testpartiallongoptionsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testPartialLongOptionSingleDash"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testpartiallongoptionsingledash">testPartialLongOptionSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testPartialLongOptionSingleDash');"><span id="org.apache.commons.cli.GnuParserTest.testPartialLongOptionSingleDash-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testPartialLongOptionSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testlongwithoutequalsingledash"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongWithoutEqualSingleDash"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testlongwithoutequalsingledash">testLongWithoutEqualSingleDash</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testLongWithoutEqualSingleDash');"><span id="org.apache.commons.cli.GnuParserTest.testLongWithoutEqualSingleDash-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testLongWithoutEqualSingleDash-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunrecognizedoptionwithbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnrecognizedOptionWithBursting"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunrecognizedoptionwithbursting">testUnrecognizedOptionWithBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnrecognizedOptionWithBursting');"><span id="org.apache.commons.cli.GnuParserTest.testUnrecognizedOptionWithBursting-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testUnrecognizedOptionWithBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testbursting"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testBursting"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testbursting">testBursting</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testBursting');"><span id="org.apache.commons.cli.GnuParserTest.testBursting-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testBursting-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption1"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption1">testAmbiguousPartialLongOption1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption1');"><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption1-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption2"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption2">testAmbiguousPartialLongOption2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption2');"><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption2-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption3"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption3"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption3">testAmbiguousPartialLongOption3</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption3');"><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption3-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption3-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption4"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption4"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouspartiallongoption4">testAmbiguousPartialLongOption4</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption4');"><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption4-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption4-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testnegativeoption"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testNegativeOption"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testnegativeoption">testNegativeOption</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testNegativeOption');"><span id="org.apache.commons.cli.GnuParserTest.testNegativeOption-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testNegativeOption-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser (CLI-184)</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testlongwithunexpectedargument1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument1"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testlongwithunexpectedargument1">testLongWithUnexpectedArgument1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument1');"><span id="org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument1-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testlongwithunexpectedargument2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument2"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testlongwithunexpectedargument2">testLongWithUnexpectedArgument2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument2');"><span id="org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument2-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption1"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption1"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption1">testUnambiguousPartialLongOption1</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption1');"><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption1-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption1-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption2"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption2">testUnambiguousPartialLongOption2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption2');"><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption2-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption3"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption3"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption3">testUnambiguousPartialLongOption3</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption3');"><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption3-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption3-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption4"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption4"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testunambiguouspartiallongoption4">testUnambiguousPartialLongOption4</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption4');"><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption4-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption4-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testdoubledash2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testDoubleDash2"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testdoubledash2">testDoubleDash2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testDoubleDash2');"><span id="org.apache.commons.cli.GnuParserTest.testDoubleDash2-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testDoubleDash2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouslongwithoutequalsingledash2"><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></a></td>
<td><a id="TC_org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a><a href="#surefire--org.apache.commons.cli.gnuparsertest.testambiguouslongwithoutequalsingledash2">testAmbiguousLongWithoutEqualSingleDash2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash2');"><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash2-off"> + </span><span id="org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>not supported by the GnuParser</td>
<td>-</td></tr></table></section><section><a id="org.apache.commons.cli.DeprecatedAttributesTest"></a>
<h3>DeprecatedAttributesTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DeprecatedAttributesTest.testDefaultToString"></a>testDefaultToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DeprecatedAttributesTest.testBuilderNonDefaults"></a>testBuilderNonDefaults</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DeprecatedAttributesTest.testDefaultBuilder"></a>testDefaultBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.DeprecatedAttributesTest.testBuilderNonDefaultsToString"></a>testBuilderNonDefaultsToString</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.bug.BugsTest"></a>
<h3>BugsTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test13666_Builder"></a>test13666_Builder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test11456"></a>test11456</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test11457"></a>test11457</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test11458"></a>test11458</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test11680"></a>test11680</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test12210"></a>test12210</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test13425"></a>test13425</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test13666"></a>test13666</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test13935"></a>test13935</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test14786"></a>test14786</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test15046"></a>test15046</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test15648"></a>test15648</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.bug.BugsTest.test31148"></a>test31148</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.MissingOptionExceptionTest"></a>
<h3>MissingOptionExceptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.MissingOptionExceptionTest.testGetMissingOptions"></a>testGetMissingOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.MissingOptionExceptionTest.testGetMessage"></a>testGetMessage</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.OptionGroupTest"></a>
<h3>OptionGroupTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testTwoOptionsFromDifferentGroup"></a>testTwoOptionsFromDifferentGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testNoOptionsExtraArgs"></a>testNoOptionsExtraArgs</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testGetNames"></a>testGetNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testTwoValidOptions"></a>testTwoValidOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testSingleOption"></a>testSingleOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testTwoOptionsFromGroup"></a>testTwoOptionsFromGroup</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testTwoValidLongOptions"></a>testTwoValidLongOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testSingleOptionFromGroup"></a>testSingleOptionFromGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testTwoOptionsFromGroupWithProperties"></a>testTwoOptionsFromGroupWithProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testTwoLongOptionsFromGroup"></a>testTwoLongOptionsFromGroup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testSingleLongOption"></a>testSingleLongOption</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.OptionGroupTest.testValidLongOnlyOptions"></a>testValidLongOnlyOptions</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.SolrCreateToolTest"></a>
<h3>SolrCreateToolTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.SolrCreateToolTest.testHelpFormatter"></a>testHelpFormatter</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.SolrCreateToolTest.testHelpFormatterDeprecated"></a>testHelpFormatterDeprecated</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.ValuesTest"></a>
<h3>ValuesTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testTwoArgValues"></a>testTwoArgValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testShortArgs"></a>testShortArgs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testCharSeparator"></a>testCharSeparator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testExtraArgs"></a>testExtraArgs</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testShortArgsWithValue"></a>testShortArgsWithValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testComplexValues"></a>testComplexValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ValuesTest.testMultipleArgValues"></a>testMultipleArgValues</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.ConverterTests"></a>
<h3>ConverterTests</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testUrl"></a>testUrl</td>
<td>0.060 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testClass"></a>testClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testDate"></a>testDate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testFile"></a>testFile</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B1.5D"></a>testNumber(String, Number)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B2.5D"></a>testNumber(String, Number)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B3.5D"></a>testNumber(String, Number)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B4.5D"></a>testNumber(String, Number)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B5.5D"></a>testNumber(String, Number)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B6.5D"></a>testNumber(String, Number)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B7.5D"></a>testNumber(String, Number)[7]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B8.5D"></a>testNumber(String, Number)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testNumber.28String.2C_Number.29.5B9.5D"></a>testNumber(String, Number)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.ConverterTests.testObject"></a>testObject</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.help.UtilTest"></a>
<h3>UtilTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B1.5D"></a>testRtrim(Character, boolean)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B2.5D"></a>testRtrim(Character, boolean)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B3.5D"></a>testRtrim(Character, boolean)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B4.5D"></a>testRtrim(Character, boolean)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B5.5D"></a>testRtrim(Character, boolean)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B6.5D"></a>testRtrim(Character, boolean)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B7.5D"></a>testRtrim(Character, boolean)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B8.5D"></a>testRtrim(Character, boolean)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B9.5D"></a>testRtrim(Character, boolean)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B10.5D"></a>testRtrim(Character, boolean)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B11.5D"></a>testRtrim(Character, boolean)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B12.5D"></a>testRtrim(Character, boolean)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B13.5D"></a>testRtrim(Character, boolean)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B14.5D"></a>testRtrim(Character, boolean)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B15.5D"></a>testRtrim(Character, boolean)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testRtrim.28Character.2C_boolean.29.5B16.5D"></a>testRtrim(Character, boolean)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos"></a>testFindNonWhitespacePos</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B1.5D"></a>testFindNonWhitespacePos(Character, boolean)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B2.5D"></a>testFindNonWhitespacePos(Character, boolean)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B3.5D"></a>testFindNonWhitespacePos(Character, boolean)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B4.5D"></a>testFindNonWhitespacePos(Character, boolean)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B5.5D"></a>testFindNonWhitespacePos(Character, boolean)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B6.5D"></a>testFindNonWhitespacePos(Character, boolean)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B7.5D"></a>testFindNonWhitespacePos(Character, boolean)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B8.5D"></a>testFindNonWhitespacePos(Character, boolean)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B9.5D"></a>testFindNonWhitespacePos(Character, boolean)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B10.5D"></a>testFindNonWhitespacePos(Character, boolean)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B11.5D"></a>testFindNonWhitespacePos(Character, boolean)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B12.5D"></a>testFindNonWhitespacePos(Character, boolean)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B13.5D"></a>testFindNonWhitespacePos(Character, boolean)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B14.5D"></a>testFindNonWhitespacePos(Character, boolean)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B15.5D"></a>testFindNonWhitespacePos(Character, boolean)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testFindNonWhitespacePos.28Character.2C_boolean.29.5B16.5D"></a>testFindNonWhitespacePos(Character, boolean)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.UtilTest.testIsEmpty"></a>testIsEmpty</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.cli.help.TextStyleTests"></a>
<h3>TextStyleTests</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B1.5D"></a>testPad(TextStyle, String, String)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B2.5D"></a>testPad(TextStyle, String, String)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B3.5D"></a>testPad(TextStyle, String, String)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B4.5D"></a>testPad(TextStyle, String, String)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B5.5D"></a>testPad(TextStyle, String, String)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B6.5D"></a>testPad(TextStyle, String, String)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B7.5D"></a>testPad(TextStyle, String, String)[7]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B8.5D"></a>testPad(TextStyle, String, String)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B9.5D"></a>testPad(TextStyle, String, String)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B10.5D"></a>testPad(TextStyle, String, String)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B11.5D"></a>testPad(TextStyle, String, String)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testPad.28TextStyle.2C_String.2C_String.29.5B12.5D"></a>testPad(TextStyle, String, String)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_0a4b985a6ef05347.gif"/></td>
<td><a id="TC_org.apache.commons.cli.help.TextStyleTests.testDefaultStyle"></a>testDefaultStyle</td>
<td>0 s</td></tr></table></section>
</section><section><a id="Failure_Details"></a>
<h2>Failure Details</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p>
<table>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash"></a>testAmbiguousLongWithoutEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testLongWithoutEqualSingleDash"></a>testLongWithoutEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testAmbiguousPartialLongOption4"></a>testAmbiguousPartialLongOption4</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testShortWithEqual"></a>testShortWithEqual</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testNegativeOption"></a>testNegativeOption</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser (CLI-184)</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testLongWithUnexpectedArgument1"></a>testLongWithUnexpectedArgument1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testLongWithEqualSingleDash"></a>testLongWithEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testUnambiguousPartialLongOption4"></a>testUnambiguousPartialLongOption4</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testDoubleDash2"></a>testDoubleDash2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.PosixParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a>testAmbiguousLongWithoutEqualSingleDash2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the PosixParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.DefaultParserTest.testLongOptionWithEqualsQuoteHandling"></a>testLongOptionWithEqualsQuoteHandling</td></tr>
<tr>
<td>-</td>
<td>skipped: Test case handled in the parameterized tests as "DEFAULT behavior"</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.DefaultParserTest.testShortOptionConcatenatedQuoteHandling"></a>testShortOptionConcatenatedQuoteHandling</td></tr>
<tr>
<td>-</td>
<td>skipped: Test case handled in the parameterized tests as "DEFAULT behavior"</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testStopBursting2"></a>testStopBursting2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testShortWithoutEqual"></a>testShortWithoutEqual</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testLongOptionWithEqualsQuoteHandling"></a>testLongOptionWithEqualsQuoteHandling</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash"></a>testAmbiguousLongWithoutEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testMissingArgWithBursting"></a>testMissingArgWithBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testStopBursting"></a>testStopBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testPartialLongOptionSingleDash"></a>testPartialLongOptionSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testLongWithoutEqualSingleDash"></a>testLongWithoutEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testUnrecognizedOptionWithBursting"></a>testUnrecognizedOptionWithBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testBursting"></a>testBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption1"></a>testAmbiguousPartialLongOption1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption2"></a>testAmbiguousPartialLongOption2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption3"></a>testAmbiguousPartialLongOption3</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testAmbiguousPartialLongOption4"></a>testAmbiguousPartialLongOption4</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testShortWithEqual"></a>testShortWithEqual</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testNegativeOption"></a>testNegativeOption</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser (CLI-184)</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testLongWithEqualDoubleDash"></a>testLongWithEqualDoubleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testLongWithEqualSingleDash"></a>testLongWithEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption1"></a>testUnambiguousPartialLongOption1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption2"></a>testUnambiguousPartialLongOption2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption3"></a>testUnambiguousPartialLongOption3</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testUnambiguousPartialLongOption4"></a>testUnambiguousPartialLongOption4</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testShortOptionConcatenatedQuoteHandling"></a>testShortOptionConcatenatedQuoteHandling</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testPropertiesOption1"></a>testPropertiesOption1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testPropertiesOption2"></a>testPropertiesOption2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testDoubleDash2"></a>testDoubleDash2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.BasicParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a>testAmbiguousLongWithoutEqualSingleDash2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the BasicParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testStopBursting2"></a>testStopBursting2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash"></a>testAmbiguousLongWithoutEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testMissingArgWithBursting"></a>testMissingArgWithBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testShortWithUnexpectedArgument"></a>testShortWithUnexpectedArgument</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testStopBursting"></a>testStopBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testPartialLongOptionSingleDash"></a>testPartialLongOptionSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testLongWithoutEqualSingleDash"></a>testLongWithoutEqualSingleDash</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testUnrecognizedOptionWithBursting"></a>testUnrecognizedOptionWithBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testBursting"></a>testBursting</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption1"></a>testAmbiguousPartialLongOption1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption2"></a>testAmbiguousPartialLongOption2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption3"></a>testAmbiguousPartialLongOption3</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testAmbiguousPartialLongOption4"></a>testAmbiguousPartialLongOption4</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testNegativeOption"></a>testNegativeOption</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser (CLI-184)</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument1"></a>testLongWithUnexpectedArgument1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testLongWithUnexpectedArgument2"></a>testLongWithUnexpectedArgument2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption1"></a>testUnambiguousPartialLongOption1</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption2"></a>testUnambiguousPartialLongOption2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption3"></a>testUnambiguousPartialLongOption3</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testUnambiguousPartialLongOption4"></a>testUnambiguousPartialLongOption4</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testDoubleDash2"></a>testDoubleDash2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_3ab6f44ece279d3e.gif"/></td>
<td><a id="org.apache.commons.cli.GnuParserTest.testAmbiguousLongWithoutEqualSingleDash2"></a>testAmbiguousLongWithoutEqualSingleDash2</td></tr>
<tr>
<td>-</td>
<td>skipped: not supported by the GnuParser</td></tr></table>
</section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/rat-report.html -->

<!-- page_index: 17 -->

# RAT (Release Audit Tool) results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h1>RAT (Release Audit Tool) results</h1>
<p>The following document contains the results of <a href="https://creadur.apache.org/rat/apache-rat-plugin/">RAT (Release Audit Tool)</a> Apache Creadur RAT::Plugin4Maven 0.17 (Apache Software Foundation).</p>
<p></p>
<pre>*****************************************************
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

</pre></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/japicmp.html -->

<!-- page_index: 18 -->

# Apache Commons CLI

<table class="layout-table">
<tr>
<td>
</td>
<td>
<span>Comparing source compatibility of commons-cli-1.11.0.jar against commons-cli-1.10.0.jar</span>
<div>
<table>
<tr>
<td>Old:</td>
<td>
				commons-cli-1.10.0.jar
			</td>
</tr>
<tr>
<td>New:</td>
<td>
				commons-cli-1.11.0.jar
			</td>
</tr>
<tr>
<td>Created:</td>
<td>
				2025-11-20T08:56:24.912-0500
			</td>
</tr>
<tr>
<td>Access modifier filter:</td>
<td id="meta-accessmodifier-value">
				PROTECTED
			</td>
</tr>
<tr>
<td>Only modifications:</td>
<td>
				true
			</td>
</tr>
<tr>
<td>Only binary incompatible modifications:</td>
<td>
				false
			</td>
</tr>
<tr>
<td>Ignore missing classes:</td>
<td>
				false
			</td>
</tr>
<tr>
<td>Includes:</td>
<td>
				all
			</td>
</tr>
<tr>
<td>Excludes:</td>
<td>
				n.a.
			</td>
</tr>
<tr>
<td id="semver-label">Semantic Versioning:</td>
<td id="semver-version">
				0.0.1
			</td>
</tr>
</table>
</div>
<div id="toc">
<span>Classes:</span>
<table>
<thead>
<tr>
<td>Status</td>
<td>Fully Qualified Name</td>
</tr>
</thead>
<tbody>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.cli.commandline">
			org.apache.commons.cli.CommandLine
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.cli.help.abstracthelpformatter">
			org.apache.commons.cli.help.AbstractHelpFormatter
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.cli.option">
			org.apache.commons.cli.Option
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.cli.posixparser">
			org.apache.commons.cli.PosixParser
		</a>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<span>Binary incompatible changes are marked with (!) while source incompatible changes are marked with (*).</span>
</div>
<div>
<div id="org.apache.commons.cli.CommandLine">
<div>
<span>
<a name="org.apache.commons.cli.CommandLine"></a>
<span>MODIFIED</span>
<span> (Serializable compatible) </span>
<span>public</span>
<span>class</span>
 org.apache.commons.cli.CommandLine
			</span>
<a href="#japicmp--toc">top</a>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
<div>
<table>
<thead>
<tr>
<td></td>
<td>Serializable</td>
<td>default serialVersionUID</td>
<td>serialVersionUID in class</td>
</tr>
</thead>
<tbody>
<tr>
<td>Old</td><td>true</td>
<td>7076145126846789520</td>
<td>1</td>
</tr>
<tr>
<td>New</td><td>true</td>
<td>8065023836524799982</td>
<td>1</td>
</tr>
</tbody>
</table>
</div>
<div>
</div>
<div>
</div>
<div>
<span>Methods:</span>
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
</div>
</div>
</div>
<div>
<div id="org.apache.commons.cli.help.AbstractHelpFormatter">
<div>
<span>
<a name="org.apache.commons.cli.help.AbstractHelpFormatter"></a>
<span>MODIFIED</span>
<span>public</span>
<span>abstract</span>
<span>class</span>
 org.apache.commons.cli.help.AbstractHelpFormatter
			</span>
<a href="#japicmp--toc">top</a>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
<div>
<span>Methods:</span>
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
</div>
</div>
</div>
<div>
<div id="org.apache.commons.cli.Option">
<div>
<span>
<a name="org.apache.commons.cli.Option"></a>
<span>MODIFIED</span>
<span> (Serializable compatible) </span>
<span>public</span>
<span>class</span>
 org.apache.commons.cli.Option
			</span>
<a href="#japicmp--toc">top</a>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
<div>
<table>
<thead>
<tr>
<td></td>
<td>Serializable</td>
<td>default serialVersionUID</td>
<td>serialVersionUID in class</td>
</tr>
</thead>
<tbody>
<tr>
<td>Old</td><td>true</td>
<td>15783033580600091</td>
<td>1</td>
</tr>
<tr>
<td>New</td><td>true</td>
<td>3006244500561563562</td>
<td>1</td>
</tr>
</tbody>
</table>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
</div>
</div>
<div>
<div id="org.apache.commons.cli.PosixParser">
<div>
<span>
<a name="org.apache.commons.cli.PosixParser"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.cli.PosixParser
			</span>
<a href="#japicmp--toc">top</a>
</div>
<div>
</div>
<div>
<span>Superclass:</span>
<table>
<thead>
<tr>
<td>Status</td>
<td>Superclass</td>
<td>Compatibility Changes</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>UNCHANGED</span></td>
<td>org.apache.commons.cli.Parser</td>
<td>n.a.</td>
</tr>
</tbody>
</table>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
<div>
</div>
</div>
</div>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/checkstyle.html -->

<!-- page_index: 19 -->

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 12.1.0 with /Users/garygregory/git/commons/commons-cli/src/conf/checkstyle.xml ruleset.

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 90 | 0 | 0 | 0 |

## Files

| File | I | W | E |
| --- | --- | --- | --- |

## Details

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/spotbugs.html -->

<!-- page_index: 20 -->

# SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.9.8*

Threshold is *medium*

Effort is *default*

# Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 56 | 0 | 0 | 0 |

# Files

| Class | Bugs |
| --- | --- |

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/cpd.html -->

<!-- page_index: 21 -->

# CPD Results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="CPD_Results"></a>
<h1>CPD Results</h1>
<p>The following document contains the results of PMD's  <a href="https://pmd.github.io/latest/pmd_userdocs_cpd.html">CPD</a> 7.17.0.</p><section><a id="Duplications"></a>
<h2>Duplications</h2>
<table>
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
                    if (opt.isValuesEmpty()) {</pre></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CLI, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-cli/pmd.html -->

<!-- page_index: 22 -->

# PMD Results

The following document contains the results of [PMD](https://pmd.github.io) 7.17.0.

PMD found no problems in your source code.

## Suppressed Violations

| Filename | Rule message | Suppression type | Reason |
| --- | --- | --- | --- |
| org/apache/commons/cli/HelpFormatter.java | Avoid empty catch blocks | //nopmd |  |
| org/apache/commons/cli/Parser.java | Avoid empty catch blocks | //nopmd |  |

---
