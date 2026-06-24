# Project Information

## Navigation

- Commons CSV
  - [About](#index)
  - [Asking Questions](https://commons.apache.org/proper/commons-csv/mail-lists.html)
  - [Release History](#changes)
  - [Issue Tracking](#issue-management)
  - [Dependency Management](#dependency-info)
  - [Javadoc](https://commons.apache.org/proper/commons-csv/apidocs/index.html)
  - [Javadoc Archive](https://javadoc.io/doc/org.apache.commons/commons-csv/)
  - [Sources](#scm)
  - [Security](#security)
  - [License](https://www.apache.org/licenses/LICENSE-2.0)
  - [Code of Conduct](https://www.apache.org/foundation/policies/conduct.html)
  - [Download](https://commons.apache.org/proper/commons-csv/download_bcel.cgi)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [Issue Management](#issue-management)
    - [Mailing Lists](https://commons.apache.org/proper/commons-csv/mailing-lists.html)
    - [Maven Coordinates](#dependency-info)
    - [Dependency Management](#dependency-management)
    - [Dependencies](#dependencies)
    - [Dependency Convergence](#dependency-convergence)
    - [CI Management](#ci-management)
    - [Distribution Management](#distribution-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes)
    - [JIRA Report](#jira-changes)
    - [Javadoc](https://commons.apache.org/proper/commons-csv/apidocs/index.html)
    - [Source Xref](https://commons.apache.org/proper/commons-csv/xref/index.html)
    - [Test Source Xref](https://commons.apache.org/proper/commons-csv/xref-test/index.html)
    - [Surefire](#surefire)
    - [Rat Report](#rat-report)
    - [JaCoCo](https://commons.apache.org/proper/commons-csv/jacoco/index.html)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [CPD](#cpd)
    - [PMD](#pmd)
    - [Tag List](#taglist)
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

<!-- source_url: https://commons.apache.org/proper/commons-csv/index.html -->

<!-- page_index: 1 -->

# Using Apache Commons CSV

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Using_Apache_Commons_CSV"></a>
<h1>Using Apache Commons CSV</h1>
<p>Commons CSV reads and writes files in variations of the Comma Separated Value (CSV) format.</p>
<p>Read the documentation starting with the <a href="https://commons.apache.org/proper/commons-csv/apidocs/index.html">Javadoc Overview</a>.</p>
</section>
<section><a id="Documentation"></a>
<h1>Documentation</h1>
<p>
An overview of the functionality is provided in the
<a href="https://commons.apache.org/proper/commons-csv/apidocs/index.html">user guide</a>.
Various <a href="#project-reports">project reports</a> are also available.
</p>
<p>
The Javadoc API documents are available online:
</p>
<p>
The <a href="#scm">git repository</a> can be
<a href="https://gitbox.apache.org/repos/asf?p=commons-csv.git">browsed</a>.
</p>
</section>
<section><a id="Releases"></a>
<h1>Releases</h1>
<ul>
<li><a href="https://commons.apache.org/csv/download_csv.cgi">Download Apache Commons CSV current (mirrors)</a>, requires Java 8 or above</li>
<li><a href="https://archive.apache.org/dist/commons/csv/">Download Apache Commons CSV archived releases</a></li>
</ul>
<p>
See the
<a href="https://commons.apache.org/csv/download_csv.cgi">Download Page</a>
for the latest releases.
</p>
<p>
<a href="#changes">Release History</a> are also available.
</p>
<p>
For previous releases, see the <a href="https://archive.apache.org/dist/commons/csv/">Apache Archive</a>
</p>
<p>
  For dependency access methods, see <a href="#dependency-info">Dependency Information</a>
</p>
</section>
<section><a id="Building_from_sources"></a>
<h1>Building from sources</h1>
<p>The latest code can be checked out from our git repository at <a href="https://gitbox.apache.org/repos/asf/commons-csv.git">https://gitbox.apache.org/repos/asf/commons-csv.git</a>.
    You can build the component using Apache Maven using <code>mvn clean package</code>.
  </p>
</section>
<section><a id="Getting_Involved"></a>
<h1>Getting Involved</h1>
<p>
    The <a href="https://commons.apache.org/proper/commons-csv/mail-lists.html">commons developer mailing list</a> is the main channel of communication for contributors. Please remember that the lists are shared between all commons components, so prefix your email by [csv]. </p>
<p>You can also peruse <a href="https://commons.apache.org/proper/commons-csv/issue-tracking.html">JIRA</a>. Specific links of interest for JIRA are:</p>
<ul>
<li>Ideas looking for code: <a href="https://issues.apache.org/jira/issues/?jql=project%20%3D%20CSV%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20%22Patch%20Needed%22">Patch Needed</a></li>
<li>Issues with patches, looking for reviews: <a href="https://issues.apache.org/jira/issues/?jql=project%20%3D%20CSV%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20Review">Review Patch</a></li>
</ul>
<p>Alternatively you can go through the <em>Needs Work</em> tags in the <a href="#taglist">TagList report</a>.</p>
<p>If you'd like to offer up pull requests via GitHub rather than applying patches to JIRA, we have a <a href="https://github.com/apache/commons-csv/">GitHub mirror</a>. </p>
</section>
<section><a id="Support"></a>
<h1>Support</h1>
<p>
    The <a href="https://commons.apache.org/proper/commons-csv/mail-lists.html">commons mailing lists</a> act as the main support forum.
    The user list is suitable for most library usage queries.
    The dev list is intended for the development discussion.
    Please remember that the lists are shared between all commons components,
    so prefix your email by [csv].
  </p>
<p>
    Bug reports and enhancements are also welcomed via the <a href="https://commons.apache.org/proper/commons-csv/issue-tracking.html">JIRA</a> issue tracker.
    Please read the instructions carefully.
  </p>
</section>
<section><a id="About_Commons_CSV"></a>
<h1>About Commons CSV</h1>
<p>Commons CSV was started to unify a common and simple interface for reading and writing CSV files under an ASL license. It has been bootstrapped by a code donation from Netcetera in Switzerland. There are three pre-existing BSD compatible CSV parsers which this component will hopefully make redundant (authors willing): </p>
<ul>
<li><a href="http://kasparov.skife.org/csv/">Skife CSV</a></li>
<li><a href="https://opencsv.sourceforge.net/">Open CSV</a></li>
<li>Genjava CSV</li>
</ul>
<p>In addition to the code from Netcetera (org.apache.commons.csv), Martin van den Bemt has added an additional writer API. </p>
<p>Other CSV implementations: </p>
<ul>
<li><a href="https://super-csv.github.io/super-csv/index.html">Super CSV</a></li>
</ul>
</section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/changes.html -->

<!-- page_index: 2 -->

# Apache Commons CSV Release Notes

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Apache_Commons_CSV_Release_Notes"></a>
<h1>Apache Commons CSV Release Notes</h1><section><a id="Release_History"></a>
<h2>Release History</h2>
<table>
<tr>
<th>Version</th>
<th>Date</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes--a1.14.2">1.14.2</a></td>
<td>YYYY-MM-DD</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.14.1">1.14.1</a></td>
<td>2025-07-27</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.14.0">1.14.0</a></td>
<td>2025-03-15</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.13.0">1.13.0</a></td>
<td>2025-01-08</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.12.0">1.12.0</a></td>
<td>2024-09-21</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.11.0">1.11.0</a></td>
<td>2024-04-28</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.10.0">1.10.0</a></td>
<td>2023-01-28</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.9.0">1.9.0</a></td>
<td>2021-07-24</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.8">1.8</a></td>
<td>2020-02-01</td>
<td>This is a feature and maintenance release. Java 8 or later is required.  This release fixes serialization compatibility of CSVRecord with versions 1.0 to 1.6. New fields added since 1.7 are not serialized. Support for Serializable is scheduled to be removed in version 2.0.</td></tr>
<tr>
<td><a href="#changes--a1.7">1.7</a></td>
<td>2019-06-01</td>
<td>This is a feature and maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.6">1.6</a></td>
<td>2018-09-22</td>
<td>Feature and bug fix release (Java 7 or above)</td></tr>
<tr>
<td><a href="#changes--a1.5">1.5</a></td>
<td>2017-09-03</td>
<td>Feature and bug fix release (Java 7 or above)</td></tr>
<tr>
<td><a href="#changes--a1.4">1.4</a></td>
<td>2016-05-28</td>
<td>Feature and bug fix release (Java 6 or above)</td></tr>
<tr>
<td><a href="#changes--a1.3">1.3</a></td>
<td>2016-05-09</td>
<td>Feature and bug fix release (Java 6 or above)</td></tr>
<tr>
<td><a href="#changes--a1.2">1.2</a></td>
<td>2015-08-24</td>
<td>Feature and bug fix release (Java 6 or above)</td></tr>
<tr>
<td><a href="#changes--a1.1">1.1</a></td>
<td>2014-11-16</td>
<td>Feature and bug fix release (Java 6 or above)</td></tr>
<tr>
<td><a href="#changes--a1.0">1.0</a></td>
<td>2014-08-14</td>
<td>First release (Java 6 or above)</td></tr></table></section><section><a id="a1.14.2"></a>
<h2>Release 1.14.2 – YYYY-MM-DD</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Remove Spotbugs dependency and use exclude-filter instead #564. Fixes <a href="https://issues.apache.org/jira/browse/CSV-320">CSV-320</a>. Thanks to Jan Burkhardt.</td>
<td><a href="#team--aherbert">aherbert</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Remove broken website link #577. Fixes <a href="https://issues.apache.org/jira/browse/CSV-320">CSV-320</a>. Thanks to Cassio Santos.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 85 to 88 #573. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>[test] Bump com.opencsv:opencsv from 5.11.2 to 5.12.0 #558. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-lang3 from 3.18.0 to 3.19.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.14.1"></a>
<h2>Release 1.14.1 – 2025-07-27</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVPrinter.printRecord(Stream) hangs if given a parallel stream. Fixes <a href="https://issues.apache.org/jira/browse/CSV-318">CSV-318</a>. Thanks to Joseph Shraibman, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVPrinter now uses an internal lock instead of synchronized methods. Fixes <a href="https://issues.apache.org/jira/browse/CSV-318">CSV-318</a>. Thanks to Joseph Shraibman, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>org.apache.commons.csv.CSVPrinter.printRecords(ResultSet) now writes one record at a time using a lock. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 81 to 85 #542. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-io:commons-io from 2.18.0 to 2.20.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump com.opencsv:opencsv from 5.10 to 5.11.2 #545, #551, #553. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-lang3 from 3.17.0 to 3.18.0 #556. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-codec:commons-codec from 1.18.0 to 1.19.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.14.0"></a>
<h2>Release 1.14.0 – 2025-03-15</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Release history link changed from changes-report.html to changes.html #516. Fixes <a href="https://issues.apache.org/jira/browse/CSV-317">CSV-317</a>. Thanks to Filipe Roque.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.parse(URL, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.parse(String, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.parse(File, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.parse(Path, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.parse(InputStream, Charset, CSVFormat) with a null CSVFormat maps to CSVFormat.DEFAULT (like CSVParser.parse(Reader, CSVFormat)). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.parse(*) methods with a null Charset maps to Charset.defaultCharset(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix possible NullPointerException in Token.toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Define and use Maven property commons.jmh.version. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVFormat.Builder.setMaxRows(long). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVFormat.getMaxRows(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVPrinter.printRecords(ResultSet) knows how to use CSVFormat's maxRows. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVPrinter.printRecords(Iterable) knows how to use CSVFormat's maxRows. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVPrinter.printRecords(Stream) knows how to use CSVFormat's maxRows. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVParser.stream() knows how to use CSVFormat's maxRows. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVParser.getRecords() knows how to use CSVFormat's maxRows. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVParser.iterator() knows how to use CSVFormat's maxRows. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump com.opencsv:opencsv from 5.9 to 5.10. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-codec:commons-codec from 1.17.2 to 1.18.0 #522. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 79 to 81. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.13.0"></a>
<h2>Release 1.13.0 – 2025-01-08</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Required OSGi Import-Package version numbers in MANIFEST.MF #504. Fixes <a href="https://issues.apache.org/jira/browse/CSV-314">CSV-314</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.nextRecord() should throw CSVException (an IOException subclass) instead of IOException and IllegalStateException, no method signature changes needed. Fixes <a href="https://issues.apache.org/jira/browse/CSV-314">CSV-314</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVPrinter.getRecordCount(). Fixes <a href="https://issues.apache.org/jira/browse/CSV-313">CSV-313</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add and use CSVParser.Builder and builder() and deprecate CSVParser constructors. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVFormat.Builder implements Supplier&lt;CSVFormat&gt;. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Deprecate CSVFormat.Builder.build() for get(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Track byte position #502. Fixes <a href="https://issues.apache.org/jira/browse/CSV-196">CSV-196</a>. Thanks to Yuzhan Jiang, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 76 to 78 #486, #495. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.codehaus.mojo:taglist-maven-plugin from 3.1.0 to 3.2.1 #493. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-io:commons-io from 2.17.0 to 2.18.0 #505. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-codec:commons-codec from 1.17.1 to 1.17.2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 78 to 79. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.12.0"></a>
<h2>Release 1.12.0 – 2024-09-21</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVException that extends IOException thrown on invalid input instead of IOException. Fixes <a href="https://issues.apache.org/jira/browse/CSV-270">CSV-270</a>. Thanks to Thomas Kamps, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix PMD issues for port to PMD 7.1.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix some Javadoc links #442. Thanks to Dávid Szigecsán, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Extract duplicated code into a method #444. Thanks to Dávid Szigecsán.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Migrate CSVFormat#print(File, Charset) to NIO #445. Thanks to Dávid Szigecsán.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix documentation for CSVFormat private constructor #466. Thanks to Dávid Szigecsán.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat does not support explicit " as escape char. Fixes <a href="https://issues.apache.org/jira/browse/CSV-294">CSV-294</a>. Thanks to Joern Huxhorn, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Escaping is not disableable. Fixes <a href="https://issues.apache.org/jira/browse/CSV-150">CSV-150</a>. Thanks to dota17, Gary Gregory, Jörn Huxhorn.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix Javadoc warnings on Java 23. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Improve parser performance by up to 20%, YMMV. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-codec:commons-codec from 1.16.1 to 1.17.1 #422, #449. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 69 to 76 #435, #452, #465, #468, #475, #482. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.codehaus.mojo:taglist-maven-plugin from 3.0.0 to 3.1.0 #441. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-lang3 from 3.14.0 to 3.17.0 #450, #459, #470. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump org.hamcrest:hamcrest from 2.2 to 3.0 #455. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-io:commons-io from 2.16.1 to 2.17.0 #476. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.11.0"></a>
<h2>Release 1.11.0 – 2024-04-28</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>[Javadoc] Add example to CSVFormat#setHeaderComments() #344. Fixes <a href="https://issues.apache.org/jira/browse/CSV-308">CSV-308</a>. Thanks to Buddhi De Silva, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add and use CSVFormat#setTrailingData(boolean) in CSVFormat.EXCEL for Excel compatibility #303. Thanks to DamjanJovanovic, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add and use CSVFormat#setLenientEof(boolean) in CSVFormat.EXCEL for Excel compatibility #303. Thanks to DamjanJovanovic, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Replace deprecated method in user guide, update external link #324, #325. Fixes <a href="https://issues.apache.org/jira/browse/CSV-306">CSV-306</a>. Thanks to Sam Ng, Bruno P. Kinoshita.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Document duplicate header behavior #309. Thanks to Seth Falco, Bruno P. Kinoshita.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Add missing docs #328. Thanks to jkbkupczyk.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>[StepSecurity] CI: Harden GitHub Actions #329, #330. Thanks to step-security-bot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Better error message during faulty CSV record read #347. Fixes <a href="https://issues.apache.org/jira/browse/CSV-147">CSV-147</a>. Thanks to Steven Peterson, Benedikt Ritter, Gary Gregory, Joerg Schaible, Buddhi De Silva, Elliotte Rusty Harold.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Misleading error message when QuoteMode set to None #352. Fixes <a href="https://issues.apache.org/jira/browse/CSV-310">CSV-310</a>. Thanks to Buddhi De Silva.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>OutOfMemory for very long rows despite using column value of type Reader. Fixes <a href="https://issues.apache.org/jira/browse/CSV-311">CSV-311</a>. Thanks to Christian Feuersaenger, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Use try-with-resources to manage JDBC CLOB in CSVPrinter.printRecords(ResultSet). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>JDBC Blob columns are now output as Base64 instead of Object#toString(), which usually is InputStream#toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Support unusual Excel use cases: Add support for trailing data after the closing quote, and EOF without a final closing quote #303. Thanks to DamjanJovanovic, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>MongoDB CSV empty first column parsing fix #412. Thanks to Igor Kamyshnikov, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-io:commons-io: from 2.11.0 to 2.16.1 #408, #413. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-parent from 57 to 69 #410. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump h2 from 2.1.214 to 2.2.224 #333, #349, #359. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-lang3 from 3.12.0 to 3.14.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update exception message in CSVRecord#getNextRecord() #348. Thanks to Buddhi De Silva, Michael Osipov, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump tests using com.opencsv:opencsv from 5.8 to 5.9 #373. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.10.0"></a>
<h2>Release 1.10.0 – 2023-01-28</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Minor changes #172. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>No Automatic-Module-Name prevents usage in JPMS projects without repacking the JAR. Fixes <a href="https://issues.apache.org/jira/browse/CSV-292">CSV-292</a>. Thanks to Rob Vesse.</td>
<td><a href="#team--kinow">kinow</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix for multi-char delimiter not working as expected #218. Fixes <a href="https://issues.apache.org/jira/browse/CSV-288">CSV-288</a>. Thanks to Santhsoh, Angus.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVRecord.get(Enum) should use Enum.name() instead of Enum.toString(). Fixes <a href="https://issues.apache.org/jira/browse/CSV-269">CSV-269</a>. Thanks to Auke te Winkel, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Allow org.apache.commons.csv.IOUtils.copy(Reader, Appendable, CharBuffer) to compile on Java 11 and run on Java 8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVRecord.toList() does not give write access to the new List. Fixes <a href="https://issues.apache.org/jira/browse/CSV-300">CSV-300</a>. Thanks to Markus Spann, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser.getRecords() now throws UncheckedIOException instead of IOException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Add comments to iterator() and stream() #270. Fixes <a href="https://issues.apache.org/jira/browse/CSV-274">CSV-274</a>. Thanks to Peter Hull, Bruno P. Kinoshita, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix wrong assumptions in PostgreSQL formats #265. Fixes <a href="https://issues.apache.org/jira/browse/CSV-290">CSV-290</a>. Thanks to angusdev, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Validate input to setDelimiter(String) for empty string #266. Thanks to Mykola Faryma.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Bump CSVFormat#serialVersionUID from 1 to 2. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser: Identify duplicates in null, empty and blank header names #279. Thanks to Alex Herbert.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_2a6cfb0a632c665d.gif" title="Remove"/></td>
<td>Serialization in CSVFormat is not supported from one version to the next.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Make CSVRecord#values() public. Fixes <a href="https://issues.apache.org/jira/browse/CSV-291">CSV-291</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add DuplicateHeaderMode for flexibility with header strictness. #114. Fixes <a href="https://issues.apache.org/jira/browse/CSV-264">CSV-264</a>. Thanks to Sagar Tiwari, Seth Falco, Alex Herbert, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Support for parallelism in CSVPrinter. Fixes <a href="https://issues.apache.org/jira/browse/CSV-295">CSV-295</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVPrinter.printRecord[s](Stream). Fixes <a href="https://issues.apache.org/jira/browse/CSV-295">CSV-295</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add accessors for header/trailer comments #257. Fixes <a href="https://issues.apache.org/jira/browse/CSV-304">CSV-304</a>. Thanks to Peter Hull, Bruno P. Kinoshita, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add github/codeql-action.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump actions/cache from 2.1.6 to 3.0.10 #196, #233, #243, #267, #271. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--kinow">kinow</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump actions/checkout from 2.3.4 to 3.1.0 #188, #195, #220, #272. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump actions/setup-java from 2 to 3.5.1. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump actions/upload-artifact from 3.1.0 to 3.1.1 #280. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-parent from 52 to 57 #264, #288, #298, #323. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump checkstyle from 8.44 to 9.2.1 #180, #190, #194, #202, #207. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump junit-jupiter from 5.8.0-M1 to 5.9.1 #179, #186, #201, #244, #263. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump jmh-core from 1.32 to 1.36 #176, #208, #229, #285. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump jmh-generator-annprocess from 1.32 to 1.36 #175, #206, #226, #283. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump mockito-core from 3.11.2 to 4.11.0 #187, #197, #204, #212, #230, #237, #251, #259, #284, #292, #297. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.14.0 to 3.19.0 #184, #219, #238, #254, #258. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump pmd from 6.36.0 to 6.52.0 #173, #189, #193, #199, #227, #233, #214, #236, #240, #247, #255, #273. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump opencsv from 5.5.1 to 5.7.1 #182, #221, #260, #281. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.3.0 to 4.7.3.0 #192, #198, #203, #211, #225, #234, #242, #245, #261, #275, #282. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump com.github.spotbugs:spotbugs from 4.5.3 to 4.7.2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump h2 from 1.4.200 to 2.1.214 #200, #205, #213, #239. Thanks to Dependabot.</td>
<td><a href="#team--kinow">kinow</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.3.0 to 3.4.1. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump biz.aQute.bnd:biz.aQute.bndlib from 5.3.0 to 6.3.1. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump jacoco-maven-plugin from 0.8.7 to 0.8.8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump japicmp-maven-plugin from 0.15.3 to 0.16.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.1.2 to 3.2.0 #253. Thanks to Dependabot.</td>
<td><a href="#team--kinow">kinow</a></td></tr></table></section><section><a id="a1.9.0"></a>
<h2>Release 1.9.0 – 2021-07-24</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Replace FindBugs with SpotBugs #56. Thanks to Amey Jadiye.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Javadoc typo in CSVFormat let's -&gt; lets #57. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.printWithEscapes throws StringIndexOutOfBoundsException when value is Reader #61. Fixes <a href="https://issues.apache.org/jira/browse/CSV-259">CSV-259</a>. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Improve CSVFormat test coverage #63. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix CSVFileParserTest.java to allow for a null return value from record.getComment() #62. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Improve test coverage in CSVFormatTest #65. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Removed invalid Javadoc markup for CSVFormat EXCEL #64. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Improve CSVRecord and CSVPrinter code coverage #66. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Improve lexer and token coverage #67. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.format trims last delimiter if the delimiter is a white space #71. Fixes <a href="https://issues.apache.org/jira/browse/CSV-211">CSV-211</a>. Thanks to Alpesh Kulkarni, Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Replace org.apache.commons.csv.Assertions.notNull() with Objects.requireNonNull(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Line number is not proper at EOF. Fixes <a href="https://issues.apache.org/jira/browse/CSV-149">CSV-149</a>. Thanks to Kranthi, Gary Gregory, Brent Worden, dota17.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Parser iterates over the last CSV Record twice. Fixes <a href="https://issues.apache.org/jira/browse/CSV-195">CSV-195</a>. Thanks to Rodolfo Duldulao, Rodolfo Duldulao, Michael Vitz, dota17.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Minor improvements #126, #127, #130. Fixes <a href="https://issues.apache.org/jira/browse/CSV-267">CSV-267</a>. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Add possibility to use ResultSet header meta data as CSV header #11. Fixes <a href="https://issues.apache.org/jira/browse/CSV-123">CSV-123</a>. Thanks to Emmanuel Bourg, Benedikt Ritter, shivakrishnaah, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Add test cases for withIgnoreSurroundingSpaces() and withTrim() #70. Fixes <a href="https://issues.apache.org/jira/browse/CSV-148">CSV-148</a>. Thanks to dota17.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Update CSVParser.parse(File, Charset, CSVFormat) from IO to NIO. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Missing separator with print(object) followed by printRecord(Object[]) #157. Fixes <a href="https://issues.apache.org/jira/browse/CSV-271">CSV-271</a>. Thanks to Amar Prakash Pandey.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix EOL checking for read array in ExtendedBufferedReader #5. Fixes <a href="https://issues.apache.org/jira/browse/CSV-158">CSV-158</a>. Thanks to Alexander Bondarev, Benedikt Ritter, Gary Gregory, Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Print from Reader with embedded quotes generates incorrect output #78. Fixes <a href="https://issues.apache.org/jira/browse/CSV-263">CSV-263</a>. Thanks to Jason A. Guild, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Replace JUnit assert by simpler but equivalent calls. #159. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Update gitignore to ignore idea and vscode #160. Thanks to Seth Falco.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Update CSVBenchmark #165. Fixes <a href="https://issues.apache.org/jira/browse/CSV-281">CSV-281</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Remove Whitespace Check Determines Delimiter Twice #167. Fixes <a href="https://issues.apache.org/jira/browse/CSV-283">CSV-283</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Document and Automate CSV Benchmark Harness #166. Fixes <a href="https://issues.apache.org/jira/browse/CSV-283">CSV-283</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Optimize Lexer Delimiter Check for One Character Delimiter #163. Fixes <a href="https://issues.apache.org/jira/browse/CSV-279">CSV-279</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>SpotBugs Error: Medium: org.apache.commons.csv.CSVParser.getHeaderNames() may expose internal representation by returning CSVParser.headerNames [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 599] EI_EXPOSE_REP. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>SpotBugs Error: Medium: new org.apache.commons.csv.CSVParser(Reader, CSVFormat, long, long) may expose internal representation by storing an externally mutable object into CSVParser.format [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 433] EI_EXPOSE_REP2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>SpotBugs Error: Medium: new org.apache.commons.csv.CSVParser(Reader, CSVFormat, long, long) may expose internal representation by storing an externally mutable object into CSVParser.headerMap [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 437] EI_EXPOSE_REP2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>SpotBugs Error: Medium: new org.apache.commons.csv.CSVParser(Reader, CSVFormat, long, long) may expose internal representation by storing an externally mutable object into CSVParser.headerNames [org.apache.commons.csv.CSVParser] At CSVParser.java:[line 438] EI_EXPOSE_REP2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>SpotBugs Error: Medium: new org.apache.commons.csv.CSVPrinter(Appendable, CSVFormat) may expose internal representation by storing an externally mutable object into CSVPrinter.format [org.apache.commons.csv.CSVPrinter] At CSVPrinter.java:[line 100] EI_EXPOSE_REP2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Formalize PerformanceTest #168. Fixes <a href="https://issues.apache.org/jira/browse/CSV-284">CSV-284</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Reuse Buffers in Lexer for Delimiter Detection #162. Fixes <a href="https://issues.apache.org/jira/browse/CSV-278">CSV-278</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Cleanup and Document Performance Test Harness #170. Fixes <a href="https://issues.apache.org/jira/browse/CSV-286">CSV-286</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Update buffer position when reading line comment #120. Fixes <a href="https://issues.apache.org/jira/browse/CSV-265">CSV-265</a>. Thanks to belugabehr.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Make CSVRecord#toList() public. Fixes <a href="https://issues.apache.org/jira/browse/CSV-275">CSV-275</a>. Thanks to Michael Wyraz, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVRecord#stream(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVParser#stream(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Make the method CSVRecord.putIn(Map) public. Fixes <a href="https://issues.apache.org/jira/browse/CSV-184">CSV-184</a>. Thanks to Gaurav Agarwal, M. Steiger, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add test cases for CSVRecord with get(Enum) and toString. #54. Thanks to dota17.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add and use CSVFormat.Builder, deprecated CSVFormat#with methods, based on #73. Thanks to Gary Gregory, dota17.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add support for String delimiters #76. Fixes <a href="https://issues.apache.org/jira/browse/CSV-206">CSV-206</a>. Thanks to Gary Gregory, dota17.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update org.junit.jupiter:junit-jupiter from 5.6.0 to 5.7.0, #84 #109 Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from Apache Commons Lang 3.9 to 3.12.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from commons-io:commons-io 2.6 to 2.11.0, #108. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump actions/checkout from v1 to v2.3.4, #79, #92, #121. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons-parent from 50 to 51 #80. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump tests from opencsv from 3.1 to 5.5.1 #81, #137, #158. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from super-csv from 2.2.1 to 2.4.0 #86. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump build actions/setup-java from v1.4.0 to v2, #101, #113. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.13.0 to 3.14.0 #122. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump tests from org.mockito:mockito-core 3.2.4 -&gt; 3.11.2; #88, #107, #110, #123, #128, #129, #156. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump actions/cache from v2 to v2.1.6 #132, #153. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.0.0 to 3.1.2 #131. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump checkstyle from 8.29 to 8.44. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump junit-jupiter from 5.7.0 to 5.8.0-M1 #133, #149. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons.jacoco.version from 0.8.5 to 0.8.7 (Java 16). Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump commons.spotbugs.version from 4.0.4 to 4.3.0 (Java 16). Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.2.0 to 3.3.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump jmh-generator-annprocess from 1.5.2 to 1.32 #151. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump PMD core from 6.29.0 to 6.36.0. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Bump biz.aQute.bnd:biz.aQute.bndlib from 5.1.2 to 5.3.0. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.8"></a>
<h2>Release 1.8 – 2020-02-01</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVRecord.isSet(int) method #52. Fixes <a href="https://issues.apache.org/jira/browse/CSV-255">CSV-255</a>. Thanks to 0x100.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Char escape doesn't work properly with quoting. Fixes <a href="https://issues.apache.org/jira/browse/CSV-135">CSV-135</a>. Thanks to Mateusz Zakarczemny.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Test case failures following CSVFormat#equals() update. Fixes <a href="https://issues.apache.org/jira/browse/CSV-244">CSV-244</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat withTrim() and withIgnoreSurroundingSpaces() need better docs. Fixes <a href="https://issues.apache.org/jira/browse/CSV-243">CSV-243</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat equals() and hashCode() don't use all fields. Fixes <a href="https://issues.apache.org/jira/browse/CSV-242">CSV-242</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat#validate() does not account for allowDuplicateHeaderNames #43. Fixes <a href="https://issues.apache.org/jira/browse/CSV-241">CSV-241</a>. Thanks to LuckyIlam, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Post 1.7 release fixes. Fixes <a href="https://issues.apache.org/jira/browse/CSV-245">CSV-245</a>. Thanks to Alex Herbert.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Upgrade test framework to JUnit 5 Jupiter #49, #50. Fixes <a href="https://issues.apache.org/jira/browse/CSV-252">CSV-252</a>. Thanks to Alex Herbert.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>A single empty header is allowed when not allowing empty column headers. #47. Fixes <a href="https://issues.apache.org/jira/browse/CSV-247">CSV-247</a>. Thanks to Alex Herbert, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVRecord is not Serializable. Fixes <a href="https://issues.apache.org/jira/browse/CSV-248">CSV-248</a>. Thanks to Alex Herbert.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Use test scope for supercsv #48. Thanks to Alex Herbert.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from H2 1.4.199 to 1.4.200. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from Hamcrest 2.1 to 2.2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from Mockito 3.1.0 to 3.2.4. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Fix typos in site and test #53. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Fix typo performance test #55. Thanks to Chen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.7"></a>
<h2>Release 1.7 – 2019-06-01</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add predefined CSVFormats for printing MongoDB CSV and TSV. Fixes <a href="https://issues.apache.org/jira/browse/CSV-233">CSV-233</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix escape character for POSTGRESQL_TEXT and POSTGRESQL_CSV formats. Fixes <a href="https://issues.apache.org/jira/browse/CSV-208">CSV-208</a>. Thanks to Jurrie Overgoor.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Site link "Source Repository" does not work. Fixes <a href="https://issues.apache.org/jira/browse/CSV-232">CSV-232</a>. Thanks to Jurrie Overgoor, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add support for java.sql.Clob. Fixes <a href="https://issues.apache.org/jira/browse/CSV-234">CSV-234</a>. Thanks to Roberto Benedetti, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update to Java 8. Fixes <a href="https://issues.apache.org/jira/browse/CSV-237">CSV-237</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Escape quotes in CLOBs #39. Fixes <a href="https://issues.apache.org/jira/browse/CSV-238">CSV-238</a>. Thanks to Stephen Olander-Waters.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Cannot get headers in column order from CSVRecord. Fixes <a href="https://issues.apache.org/jira/browse/CSV-239">CSV-239</a>. Thanks to Gary Gregory, Dave Moten.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update tests from H2 1.4.198 to 1.4.199. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.6"></a>
<h2>Release 1.6 – 2018-09-22</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Add more documentation to CSVPrinter. Fixes <a href="https://issues.apache.org/jira/browse/CSV-231">CSV-231</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add autoFlush option for CsvPrinter. PR #24. Fixes <a href="https://issues.apache.org/jira/browse/CSV-217">CSV-217</a>. Thanks to Korolyov Alexei.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>The behavior of quote char using is not similar as Excel does when the first string contains CJK char(s). Fixes <a href="https://issues.apache.org/jira/browse/CSV-219">CSV-219</a>. Thanks to Zhang Hongda.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Don't quote cells just because they have UTF-8 encoded characters. Fixes <a href="https://issues.apache.org/jira/browse/CSV-172">CSV-172</a>. Thanks to Andrew Pennebaker.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add API org.apache.commons.csv.CSVFormat.withSystemRecordSeparator(). Fixes <a href="https://issues.apache.org/jira/browse/CSV-220">CSV-220</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Inconsistency between Javadoc of CSVFormat DEFAULT EXCEL. Fixes <a href="https://issues.apache.org/jira/browse/CSV-223">CSV-223</a>. Thanks to Samuel Martin.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Create CSVFormat.ORACLE preset. Fixes <a href="https://issues.apache.org/jira/browse/CSV-209">CSV-209</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Some multi-iterator parsing peek sequences incorrectly consume elements. Fixes <a href="https://issues.apache.org/jira/browse/CSV-224">CSV-224</a>. Thanks to David Warshaw.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Parse method should avoid creating a redundant BufferedReader. Fixes <a href="https://issues.apache.org/jira/browse/CSV-225">CSV-225</a>. Thanks to Anson Schwabecher.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Add predefined CSVFormats for printing MongoDB CSV and TSV. Fixes <a href="https://issues.apache.org/jira/browse/CSV-233">CSV-233</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.5"></a>
<h2>Release 1.5 – 2017-09-03</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>withNullString value is printed without quotes when QuoteMode.ALL is specified; add QuoteMode.ALL_NON_NULL. PR #17. Fixes <a href="https://issues.apache.org/jira/browse/CSV-203">CSV-203</a>. Thanks to Richard Wheeldon, Kai Paroth.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix outdated comments about FileReader in CSVParser #13. Fixes <a href="https://issues.apache.org/jira/browse/CSV-194">CSV-194</a>. Thanks to Marc Prud'hommeaux.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix incorrect method name 'withFirstRowAsHeader' in user guide. Fixes <a href="https://issues.apache.org/jira/browse/CSV-193">CSV-193</a>. Thanks to Matthias Wiehl.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Negative numeric values in the first column are always quoted in minimal mode. Fixes <a href="https://issues.apache.org/jira/browse/CSV-171">CSV-171</a>. Thanks to Gary Gregory, Michael Graessle, Adrian Bridgett.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Update platform requirement from Java 6 to 7. Fixes <a href="https://issues.apache.org/jira/browse/CSV-187">CSV-187</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Do not use RuntimeException in CSVParser.iterator().new Iterator() {...}.getNextRecord(). Fixes <a href="https://issues.apache.org/jira/browse/CSV-201">CSV-201</a>. Thanks to Benedikt Ritter, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVParser: Add factory method accepting InputStream. Fixes <a href="https://issues.apache.org/jira/browse/CSV-189">CSV-189</a>. Thanks to Peter Holzwarth, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add convenience API CSVFormat.print(File, Charset). Fixes <a href="https://issues.apache.org/jira/browse/CSV-190">CSV-190</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add convenience API CSVFormat.print(Path, Charset). Fixes <a href="https://issues.apache.org/jira/browse/CSV-191">CSV-191</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add convenience API CSVParser.parse(Path, Charset, CSVFormat). Fixes <a href="https://issues.apache.org/jira/browse/CSV-192">CSV-192</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add convenience API CSVFormat#printer() to print to System.out. Fixes <a href="https://issues.apache.org/jira/browse/CSV-205">CSV-205</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Provide a CSV Format for printing PostgreSQL CSV and Text formats. Fixes <a href="https://issues.apache.org/jira/browse/CSV-207">CSV-207</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Adding a placeholder in the Lexer and CSV parser to store the end-of-line string. Fixes <a href="https://issues.apache.org/jira/browse/CSV-214">CSV-214</a>. Thanks to Nitin Mahendru, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.4"></a>
<h2>Release 1.4 – 2016-05-28</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Make CSVPrinter.print(Object) GC-free. Fixes <a href="https://issues.apache.org/jira/browse/CSV-181">CSV-181</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Allow some printing operations directly from CSVFormat. Fixes <a href="https://issues.apache.org/jira/browse/CSV-182">CSV-182</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Drop ferc.gov tests. Fixes <a href="https://issues.apache.org/jira/browse/CSV-183">CSV-183</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.3"></a>
<h2>Release 1.3 – 2016-05-09</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add shortcut method for using first record as header to CSVFormat. Fixes <a href="https://issues.apache.org/jira/browse/CSV-179">CSV-179</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add withHeader(Class&lt;? extends Enum&gt;) to CSVFormat. Fixes <a href="https://issues.apache.org/jira/browse/CSV-180">CSV-180</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Comment line hides next record; update Javadoc to make behavior clear. Fixes <a href="https://issues.apache.org/jira/browse/CSV-167">CSV-167</a>. Thanks to Rene.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>CSVPrinter doesn't skip creation of header record if skipHeaderRecord is set to true. Fixes <a href="https://issues.apache.org/jira/browse/CSV-153">CSV-153</a>. Thanks to Wren.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add IgnoreCase option for accessing header names. Fixes <a href="https://issues.apache.org/jira/browse/CSV-159">CSV-159</a>. Thanks to Yamil Medina.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>The null string should be case-sensitive when reading records. Fixes <a href="https://issues.apache.org/jira/browse/CSV-169">CSV-169</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.nullString should not be escaped. Fixes <a href="https://issues.apache.org/jira/browse/CSV-168">CSV-168</a>. Thanks to Gary Gregory, cornel creanga.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.MYSQL nullString should be "\N". Fixes <a href="https://issues.apache.org/jira/browse/CSV-170">CSV-170</a>. Thanks to Gary Gregory, cornel creanga.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Fix Javadoc to say CSVFormat with() methods return a new CSVFormat. Fixes <a href="https://issues.apache.org/jira/browse/CSV-161">CSV-161</a>. Thanks to Gary Gregory, Kristof Meixner, Emmanuel Bourg.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Support for ignoring trailing delimiter. Fixes <a href="https://issues.apache.org/jira/browse/CSV-175">CSV-175</a>. Thanks to Gary Gregory, Chris Jones.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Support trimming leading and trailing blanks. Fixes <a href="https://issues.apache.org/jira/browse/CSV-177">CSV-177</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Create default formats for Informix UNLOAD and UNLOAD CSV. Fixes <a href="https://issues.apache.org/jira/browse/CSV-178">CSV-178</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.2"></a>
<h2>Release 1.2 – 2015-08-24</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.with* methods clear the header comments. Fixes <a href="https://issues.apache.org/jira/browse/CSV-145">CSV-145</a>. Thanks to Frank Ulbricht.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Incorrect Javadoc on QuoteMode.NONE. Fixes <a href="https://issues.apache.org/jira/browse/CSV-156">CSV-156</a>. Thanks to Jason Steenstra-Pickens.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add enum CSVFormat.Predefined that contains the default CSVFormat values. Fixes <a href="https://issues.apache.org/jira/browse/CSV-157">CSV-157</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.1"></a>
<h2>Release 1.1 – 2014-11-16</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>QuoteMode.NON_NUMERIC doesn't work with CSVPrinter.printRecords(ResultSet). Fixes <a href="https://issues.apache.org/jira/browse/CSV-140">CSV-140</a>. Thanks to Damjan Jovanovic.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat#withHeader doesn't work well with #printComment, add withHeaderComments(String...). Fixes <a href="https://issues.apache.org/jira/browse/CSV-130">CSV-130</a>. Thanks to Sergei Lebedev.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.EXCEL should ignore empty header names. Fixes <a href="https://issues.apache.org/jira/browse/CSV-128">CSV-128</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Incorrect Javadoc referencing org.apache.commons.csv.CSVFormat withQuote(). Fixes <a href="https://issues.apache.org/jira/browse/CSV-132">CSV-132</a>. Thanks to Sascha Szott.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Improve toString() implementation of CSVRecord. Fixes <a href="https://issues.apache.org/jira/browse/CSV-124">CSV-124</a>. Thanks to Kalyan.</td>
<td><a href="#team--brentworden">brentworden</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Unified parameter validation. Fixes <a href="https://issues.apache.org/jira/browse/CSV-134">CSV-134</a>. Thanks to wu wen.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add CSVFormat#with 0-arg methods matching boolean arg methods. Fixes <a href="https://issues.apache.org/jira/browse/CSV-129">CSV-129</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Save positions of records to enable random access. Fixes <a href="https://issues.apache.org/jira/browse/CSV-131">CSV-131</a>. Thanks to Holger Stratmann.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVPrinter.printRecord(ResultSet) with metadata. Fixes <a href="https://issues.apache.org/jira/browse/CSV-139">CSV-139</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.0"></a>
<h2>Release 1.0 – 2014-08-14</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>No longer works with Java 6. Fixes <a href="https://issues.apache.org/jira/browse/CSV-125">CSV-125</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>NullPointerException when empty header string and null string of "". Fixes <a href="https://issues.apache.org/jira/browse/CSV-122">CSV-122</a>. Thanks to Mike Lewis.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Validate format parameters in constructor. Fixes <a href="https://issues.apache.org/jira/browse/CSV-117">CSV-117</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>IllegalArgumentException thrown when the header contains duplicate names when the column names are empty. Fixes <a href="https://issues.apache.org/jira/browse/CSV-121">CSV-121</a>. Thanks to Sebastian Hardt.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVFormat#withHeader doesn't work with CSVPrinter. Fixes <a href="https://issues.apache.org/jira/browse/CSV-120">CSV-120</a>. Thanks to Sergei Lebedev.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>CSVFormat is missing a print(...) method. Fixes <a href="https://issues.apache.org/jira/browse/CSV-119">CSV-119</a>. Thanks to Sergei Lebedev.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVRecord.toMap() throws NPE on formats with no
        headers. Fixes <a href="https://issues.apache.org/jira/browse/CSV-118">CSV-118</a>. Thanks to Enrique Lara.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Check whether ISE/IAE are being used appropriately. Fixes <a href="https://issues.apache.org/jira/browse/CSV-113">CSV-113</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat constructor should reject a header array with duplicate
        entries. Fixes <a href="https://issues.apache.org/jira/browse/CSV-114">CSV-114</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>HeaderMap is inconsistent when it is parsed from an input with
        duplicate columns names. Fixes <a href="https://issues.apache.org/jira/browse/CSV-112">CSV-112</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVRecord.toMap() fails if row length shorter than header length. Fixes <a href="https://issues.apache.org/jira/browse/CSV-111">CSV-111</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat.format allways append null. Fixes <a href="https://issues.apache.org/jira/browse/CSV-106">CSV-106</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Add Map conversion API to CSVRecord. Fixes <a href="https://issues.apache.org/jira/browse/CSV-105">CSV-105</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVParser: getHeaderMap throws NPE. Fixes <a href="https://issues.apache.org/jira/browse/CSV-100">CSV-100</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Lots of possible changes. Fixes <a href="https://issues.apache.org/jira/browse/CSV-42">CSV-42</a>. Thanks to Bob Smith.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Use Character instead of char for char fields except delimiter. Fixes <a href="https://issues.apache.org/jira/browse/CSV-78">CSV-78</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Revert Builder implementation in CSVFormat. Fixes <a href="https://issues.apache.org/jira/browse/CSV-99">CSV-99</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVRecord does not verify that the length of the header mapping
        matches the number of values. Fixes <a href="https://issues.apache.org/jira/browse/CSV-53">CSV-53</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Allow the handling of NULL values. Fixes <a href="https://issues.apache.org/jira/browse/CSV-93">CSV-93</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Use the Builder pattern for CSVFormat. Fixes <a href="https://issues.apache.org/jira/browse/CSV-68">CSV-68</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Clarify comment handling. Fixes <a href="https://issues.apache.org/jira/browse/CSV-84">CSV-84</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>CSVParser.nextValue() seems pointless. Fixes <a href="https://issues.apache.org/jira/browse/CSV-25">CSV-25</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Allow the String value for null to be customized for the CSV
        printer. Fixes <a href="https://issues.apache.org/jira/browse/CSV-97">CSV-97</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Not possible to create a CSVFormat from scratch. Fixes <a href="https://issues.apache.org/jira/browse/CSV-88">CSV-88</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Keep track of record number. Fixes <a href="https://issues.apache.org/jira/browse/CSV-52">CSV-52</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Lexer should only use char fields. Fixes <a href="https://issues.apache.org/jira/browse/CSV-94">CSV-94</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Need a way to extract parsed headers, e.g. for use in formatting
        output. Fixes <a href="https://issues.apache.org/jira/browse/CSV-92">CSV-92</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Header support. Fixes <a href="https://issues.apache.org/jira/browse/CSV-65">CSV-65</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Confusing semantic of the ignore leading/trailing spaces parameters. Fixes <a href="https://issues.apache.org/jira/browse/CSV-54">CSV-54</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Add convenience methods to CSVLexer. Fixes <a href="https://issues.apache.org/jira/browse/CSV-71">CSV-71</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Is CharBuffer really needed, now that StringBuilder is available?. Fixes <a href="https://issues.apache.org/jira/browse/CSV-59">CSV-59</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Replace while(true)-loop in CSVParser.getRecord with do-while-loop. Fixes <a href="https://issues.apache.org/jira/browse/CSV-55">CSV-55</a>.</td>
<td><a href="#team--britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>CSVFormat describes itself as immutable, but it is not - in
        particular it is not thread-safe. Fixes <a href="https://issues.apache.org/jira/browse/CSV-34">CSV-34</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Endless loops in CSV parser. Fixes <a href="https://issues.apache.org/jira/browse/CSV-36">CSV-36</a>.</td>
<td><a href="#team--yonik">yonik</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>NullPointerException in CSVPrinter.print()/println(). Fixes <a href="https://issues.apache.org/jira/browse/CSV-13">CSV-13</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>CSVPrinter overhaul. Fixes <a href="https://issues.apache.org/jira/browse/CSV-45">CSV-45</a>.</td>
<td><a href="#team--yonik">yonik</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_c6259c3bf8ed6742.gif" title="Fix"/></td>
<td>Excel strategy uses wrong separator. Fixes <a href="https://issues.apache.org/jira/browse/CSV-23">CSV-23</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>CSVStrategy has modifiable public static variables. Fixes <a href="https://issues.apache.org/jira/browse/CSV-49">CSV-49</a>. Thanks to Bob Smith.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_91e12b5452aab3eb.gif" title="Add"/></td>
<td>Predefined format for MYSQL. Fixes <a href="https://issues.apache.org/jira/browse/CSV-48">CSV-48</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Reduce visibility of methods in internal classes. Fixes <a href="https://issues.apache.org/jira/browse/CSV-46">CSV-46</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>ExtendedBufferedReader does too much. Fixes <a href="https://issues.apache.org/jira/browse/CSV-26">CSV-26</a>.</td>
<td><a href="#team--jacopoc">jacopoc</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_fce609b9920046d0.gif" title="Update"/></td>
<td>Decide whether to keep the csv.writer subpackage. Fixes <a href="https://issues.apache.org/jira/browse/CSV-27">CSV-27</a>.</td>
<td><a href="#team--ebourg">ebourg</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="issue-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/issue-management.html -->

<!-- page_index: 3 -->

# Overview

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Overview"></a>
<h1>Overview</h1>
<p>This project uses <a href="http://www.atlassian.com/software/jira">JIRA</a>.</p></section><section><a id="Issue_Management"></a>
<h1>Issue Management</h1>
<p>Issues, bugs, and feature requests should be submitted to the following issue management system for this project.</p>
<pre><a href="https://issues.apache.org/jira/browse/CSV">https://issues.apache.org/jira/browse/CSV</a></pre></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/dependency-info.html -->

<!-- page_index: 4 -->

# Maven Coordinates

## Apache Maven

```
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-csv</artifactId>
  <version>1.14.2-SNAPSHOT</version>
</dependency>
```

## Apache Ivy

```
<dependency org="org.apache.commons" name="commons-csv" rev="1.14.2-SNAPSHOT">
  <artifact name="commons-csv" type="jar" />
</dependency>
```

## Groovy Grape

```
@Grapes(
@Grab(group='org.apache.commons', module='commons-csv', version='1.14.2-SNAPSHOT')
)
```

## Gradle/Grails

```
implementation 'org.apache.commons:commons-csv:1.14.2-SNAPSHOT'
```

## Scala SBT

```
libraryDependencies += "org.apache.commons" % "commons-csv" % "1.14.2-SNAPSHOT"
```

## Leiningen

```
[org.apache.commons/commons-csv "1.14.2-SNAPSHOT"]
```

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/scm.html -->

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
<pre><a href="https://gitbox.apache.org/repos/asf?p=commons-csv.git">https://gitbox.apache.org/repos/asf?p=commons-csv.git</a></pre></section><section><a id="Anonymous_Access"></a>
<h1>Anonymous Access</h1>
<p>The source can be checked out anonymously from Git with this command (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>):</p>
<pre>$ git clone https://gitbox.apache.org/repos/asf/commons-csv.git</pre></section><section><a id="Developer_Access"></a>
<h1>Developer Access</h1>
<p>Only project developers can access the Git tree via this method (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>).</p>
<pre>$ git clone https://gitbox.apache.org/repos/asf/commons-csv.git</pre></section><section><a id="Access_from_Behind_a_Firewall"></a>
<h1>Access from Behind a Firewall</h1>
<p>Refer to the documentation of the SCM used for more information about access behind a firewall.</p></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/security.html -->

<!-- page_index: 6 -->

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

# Security Vulnerabilities

None.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/project-info.html -->

<!-- page_index: 7 -->

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
<td>The Apache Commons CSV library provides a simple interface for reading and writing CSV files of various types.</td></tr>
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
<td><a href="https://commons.apache.org/proper/commons-csv/mailing-lists.html">Mailing Lists</a></td>
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

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/summary.html -->

<!-- page_index: 8 -->

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
<td>Apache Commons CSV</td></tr>
<tr>
<td>Description</td>
<td>The Apache Commons CSV library provides a simple interface for reading and writing CSV files of various types.</td></tr>
<tr>
<td>Homepage</td>
<td><a href="https://commons.apache.org/proper/commons-csv/">https://commons.apache.org/proper/commons-csv/</a></td></tr></table></section><section><a id="Project_Organization"></a>
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
<td>org.apache.commons</td></tr>
<tr>
<td>ArtifactId</td>
<td>commons-csv</td></tr>
<tr>
<td>Version</td>
<td>1.14.2-SNAPSHOT</td></tr>
<tr>
<td>Type</td>
<td>jar</td></tr>
<tr>
<td>Java Version</td>
<td>1.8</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/team.html -->

<!-- page_index: 9 -->

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
<td><figure><img src="assets/images/4156866f23b66d5ca7df5cdc86cb9a0e_c37d873d8a2e11f2.jpg"/></figure></td>
<td><a id="bayard"></a>bayard</td>
<td>Henri Yandell</td>
<td><a href="mailto:bayard@apache.org">bayard@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_1add3111cf5acc1c.jpg"/></figure></td>
<td><a id="mvdb"></a>mvdb</td>
<td>Martin van den Bemt</td>
<td><a href="mailto:mvdb@apache.org">mvdb@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_1add3111cf5acc1c.jpg"/></figure></td>
<td><a id="yonik"></a>yonik</td>
<td>Yonik Seeley</td>
<td><a href="mailto:yonik@apache.org">yonik@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/8304c64641badd4218a89a5f97d2ae86_060b1cb028ffb53c.jpg"/></figure></td>
<td><a id="ebourg"></a>ebourg</td>
<td>Emmanuel Bourg</td>
<td><a href="mailto:ebourg@apache.org">ebourg@apache.org</a></td>
<td>-</td>
<td>Apache</td>
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
<td>America/New_York</td></tr>
<tr>
<td><figure><img src="assets/images/cbfb61ee7f8641b2b6eaf22fed163b1e_0fe7d74e5d147642.jpg"/></figure></td>
<td><a id="britter"></a>britter</td>
<td>Benedikt Ritter</td>
<td><a href="mailto:britter@apache.org">britter@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/a010ac0916b6b9b10883e9359cfcd7f9_a8dfd1169a0c1e32.jpg"/></figure></td>
<td><a id="chtompki"></a>chtompki</td>
<td>Rob Tompkins</td>
<td><a href="mailto:chtompki@apache.org">chtompki@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
<td>-</td>
<td>-</td>
<td>-</td></tr></table></section><section><a id="Contributors"></a>
<h2>Contributors</h2>
<p>The following additional people have contributed to this project through the way of suggestions, patches or documentation.</p>
<table>
<tr>
<th>Name</th></tr>
<tr>
<td>Bob Smith</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/dependency-management.html -->

<!-- page_index: 10 -->

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

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependencies"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/dependencies.html -->

<!-- page_index: 11 -->

# Project Dependencies

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Project_Dependencies"></a>
<h1>Project Dependencies</h1><section><a id="Project_Dependencies_compile"></a>
<h2>compile</h2>
<p>The following is a list of compile dependencies for this project. These dependencies are required to compile and run the application:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>Licenses</th></tr>
<tr>
<td>commons-codec</td>
<td><a href="https://commons.apache.org/proper/commons-codec/">commons-codec</a></td>
<td>1.19.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>commons-io</td>
<td><a href="https://commons.apache.org/proper/commons-io/">commons-io</a></td>
<td>2.20.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr></table></section><section><a id="Project_Dependencies_test"></a>
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
<td>com.h2database</td>
<td><a href="https://h2database.com">h2</a></td>
<td>2.2.224</td>
<td>jar</td>
<td><a href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a><a href="https://opensource.org/licenses/eclipse-1.0.php">EPL 1.0</a></td></tr>
<tr>
<td>org.apache.commons</td>
<td><a href="https://commons.apache.org/proper/commons-lang/">commons-lang3</a></td>
<td>3.19.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter</a></td>
<td>5.13.4</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.mockito</td>
<td><a href="https://github.com/mockito/mockito">mockito-core</a></td>
<td>4.11.0</td>
<td>jar</td>
<td><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></td></tr>
<tr>
<td>org.openjdk.jmh</td>
<td><a href="http://openjdk.java.net/projects/code-tools/jmh/jmh-core/">jmh-core</a></td>
<td>1.37</td>
<td>jar</td>
<td><a href="http://openjdk.java.net/legal/gplv2+ce.html">GNU General Public License (GPL), version 2, with the Classpath exception</a></td></tr></table></section></section><section><a id="Project_Transitive_Dependencies"></a>
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
<td>net.sf.jopt-simple</td>
<td><a href="http://jopt-simple.github.io/jopt-simple">jopt-simple</a></td>
<td>5.0.4</td>
<td>jar</td>
<td><a href="http://www.opensource.org/licenses/mit-license.php">The MIT License</a></td></tr>
<tr>
<td>org.apache.commons</td>
<td><a href="http://commons.apache.org/proper/commons-math/">commons-math3</a></td>
<td>3.6.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td>org.apiguardian</td>
<td><a href="https://github.com/apiguardian-team/apiguardian">apiguardian-api</a></td>
<td>1.1.2</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr>
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
<li>org.apache.commons:commons-csv:jar:1.14.2-SNAPSHOT <img alt="[Information]" id="_img1" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep0">
<table>
<tr>
<th>Apache Commons CSV</th></tr>
<tr>
<td>
<p><b>Description: </b>The Apache Commons CSV library provides a simple interface for reading and writing CSV files of various types.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-csv/">https://commons.apache.org/proper/commons-csv/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.jupiter:junit-jupiter:jar:5.13.4 (test) <img alt="[Information]" id="_img3" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep2">
<table>
<tr>
<th>JUnit Jupiter (Aggregator)</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.jupiter:junit-jupiter-api:jar:5.13.4 (test) <img alt="[Information]" id="_img5" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep4">
<table>
<tr>
<th>JUnit Jupiter API</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-api" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.opentest4j:opentest4j:jar:1.3.0 (test) <img alt="[Information]" id="_img7" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep6">
<table>
<tr>
<th>org.opentest4j:opentest4j</th></tr>
<tr>
<td>
<p><b>Description: </b>Open Test Alliance for the JVM</p>
<p><b>URL: </b><a href="https://github.com/ota4j-team/opentest4j">https://github.com/ota4j-team/opentest4j</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.junit.platform:junit-platform-commons:jar:1.13.4 (test) <img alt="[Information]" id="_img9" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep8">
<table>
<tr>
<th>JUnit Platform Commons</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-commons" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li>
<li>org.apiguardian:apiguardian-api:jar:1.1.2 (test) <img alt="[Information]" id="_img11" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep10">
<table>
<tr>
<th>org.apiguardian:apiguardian-api</th></tr>
<tr>
<td>
<p><b>Description: </b>@API Guardian</p>
<p><b>URL: </b><a href="https://github.com/apiguardian-team/apiguardian">https://github.com/apiguardian-team/apiguardian</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.junit.jupiter:junit-jupiter-params:jar:5.13.4 (test) <img alt="[Information]" id="_img13" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep12">
<table>
<tr>
<th>JUnit Jupiter Params</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-params" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li>
<li>org.junit.jupiter:junit-jupiter-engine:jar:5.13.4 (test) <img alt="[Information]" id="_img15" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep14">
<table>
<tr>
<th>JUnit Jupiter Engine</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-engine" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.platform:junit-platform-engine:jar:1.13.4 (test) <img alt="[Information]" id="_img17" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep16">
<table>
<tr>
<th>JUnit Platform Engine API</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-engine" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li></ul></li></ul></li>
<li>org.mockito:mockito-core:jar:4.11.0 (test) <img alt="[Information]" id="_img19" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep18">
<table>
<tr>
<th>mockito-core</th></tr>
<tr>
<td>
<p><b>Description: </b>Mockito mock objects library core API and implementation</p>
<p><b>URL: </b><a href="https://github.com/mockito/mockito">https://github.com/mockito/mockito</a></p>
<p><b>Project Licenses: </b><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></p></td></tr></table></div>
<ul>
<li>net.bytebuddy:byte-buddy:jar:1.12.19 (test) <img alt="[Information]" id="_img21" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep20">
<table>
<tr>
<th>Byte Buddy (without dependencies)</th></tr>
<tr>
<td>
<p><b>Description: </b>Byte Buddy is a Java library for creating Java classes at run time.
        This artifact is a build of Byte Buddy with all ASM dependencies repackaged into its own name space.</p>
<p><b>URL: </b><a href="https://bytebuddy.net/byte-buddy">https://bytebuddy.net/byte-buddy</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>net.bytebuddy:byte-buddy-agent:jar:1.12.19 (test) <img alt="[Information]" id="_img23" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep22">
<table>
<tr>
<th>Byte Buddy agent</th></tr>
<tr>
<td>
<p><b>Description: </b>The Byte Buddy agent offers convenience for attaching an agent to the local or a remote VM.</p>
<p><b>URL: </b><a href="https://bytebuddy.net/byte-buddy-agent">https://bytebuddy.net/byte-buddy-agent</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.objenesis:objenesis:jar:3.3 (test) <img alt="[Information]" id="_img25" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep24">
<table>
<tr>
<th>Objenesis</th></tr>
<tr>
<td>
<p><b>Description: </b>A library for instantiating Java objects</p>
<p><b>URL: </b><a href="http://objenesis.org/objenesis">http://objenesis.org/objenesis</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>commons-io:commons-io:jar:2.20.0 (compile) <img alt="[Information]" id="_img27" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep26">
<table>
<tr>
<th>Apache Commons IO</th></tr>
<tr>
<td>
<p><b>Description: </b>The Apache Commons IO library contains utility classes, stream implementations, file filters, file comparators, endian transformation classes, and much more.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-io/">https://commons.apache.org/proper/commons-io/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>commons-codec:commons-codec:jar:1.19.0 (compile) <img alt="[Information]" id="_img29" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep28">
<table>
<tr>
<th>Apache Commons Codec</th></tr>
<tr>
<td>
<p><b>Description: </b>The Apache Commons Codec component contains encoders and decoders for
     formats such as Base16, Base32, Base64, digest, and Hexadecimal. In addition to these
     widely used encoders and decoders, the codec package also maintains a
     collection of phonetic encoding utilities.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-codec/">https://commons.apache.org/proper/commons-codec/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>org.apache.commons:commons-lang3:jar:3.19.0 (test) <img alt="[Information]" id="_img31" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep30">
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
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>com.h2database:h2:jar:2.2.224 (test) <img alt="[Information]" id="_img33" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep32">
<table>
<tr>
<th>H2 Database Engine</th></tr>
<tr>
<td>
<p><b>Description: </b>H2 Database Engine</p>
<p><b>URL: </b><a href="https://h2database.com">https://h2database.com</a></p>
<p><b>Project Licenses: </b><a href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>, <a href="https://opensource.org/licenses/eclipse-1.0.php">EPL 1.0</a></p></td></tr></table></div></li>
<li>org.openjdk.jmh:jmh-core:jar:1.37 (test) <img alt="[Information]" id="_img35" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep34">
<table>
<tr>
<th>JMH Core</th></tr>
<tr>
<td>
<p><b>Description: </b>The jmh is a Java harness for building, running, and analysing
        nano/micro/macro benchmarks written in Java and other languages
        targeting the JVM.</p>
<p><b>URL: </b><a href="http://openjdk.java.net/projects/code-tools/jmh/jmh-core/">http://openjdk.java.net/projects/code-tools/jmh/jmh-core/</a></p>
<p><b>Project Licenses: </b><a href="http://openjdk.java.net/legal/gplv2+ce.html">GNU General Public License (GPL), version 2, with the Classpath exception</a></p></td></tr></table></div>
<ul>
<li>net.sf.jopt-simple:jopt-simple:jar:5.0.4 (test) <img alt="[Information]" id="_img37" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep36">
<table>
<tr>
<th>JOpt Simple</th></tr>
<tr>
<td>
<p><b>Description: </b>A Java library for parsing command line options</p>
<p><b>URL: </b><a href="http://jopt-simple.github.io/jopt-simple">http://jopt-simple.github.io/jopt-simple</a></p>
<p><b>Project Licenses: </b><a href="http://www.opensource.org/licenses/mit-license.php">The MIT License</a></p></td></tr></table></div></li>
<li>org.apache.commons:commons-math3:jar:3.6.1 (test) <img alt="[Information]" id="_img39" src="assets/images/icon-info-sml_fc89a6b111e55098.gif"/><div id="_dep38">
<table>
<tr>
<th>Apache Commons Math</th></tr>
<tr>
<td>
<p><b>Description: </b>The Apache Commons Math project is a library of lightweight, self-contained mathematics and statistics components addressing the most common practical problems not immediately available in the Java programming language or commons-lang.</p>
<p><b>URL: </b><a href="http://commons.apache.org/proper/commons-math/">http://commons.apache.org/proper/commons-math/</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li></ul></li></ul></section></section><section><a id="Licenses"></a>
<h1>Licenses</h1>
<p><b>The Apache License, Version 2.0: </b>org.apiguardian:apiguardian-api, org.opentest4j:opentest4j</p>
<p><b>The MIT License: </b>JOpt Simple, mockito-core</p>
<p><b>Apache-2.0: </b>Apache Commons CSV, Apache Commons Codec, Apache Commons IO, Apache Commons Lang</p>
<p><b>Eclipse Public License v2.0: </b>JUnit Jupiter (Aggregator), JUnit Jupiter API, JUnit Jupiter Engine, JUnit Jupiter Params, JUnit Platform Commons, JUnit Platform Engine API</p>
<p><b>Apache License, Version 2.0: </b>Apache Commons Math, Byte Buddy (without dependencies), Byte Buddy agent, Objenesis</p>
<p><b>EPL 1.0: </b>H2 Database Engine</p>
<p><b>MPL 2.0: </b>H2 Database Engine</p>
<p><b>GNU General Public License (GPL), version 2, with the Classpath exception: </b>JMH Core</p></section><section><a id="Dependency_File_Details"></a>
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
<td>h2-2.2.224.jar</td>
<td>2.6 MB</td>
<td>1057</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>1054</td>
<td>1049</td>
<td>58</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>10</td>
<td>Yes</td></tr>
<tr>
<td>   • Versioned</td>
<td>-</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>21</td>
<td>Yes</td></tr>
<tr>
<td>commons-codec-1.19.0.jar</td>
<td>374.7 kB</td>
<td>263</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>262</td>
<td>115</td>
<td>7</td>
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
<td>commons-io-2.20.0.jar</td>
<td>564 kB</td>
<td>415</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>414</td>
<td>387</td>
<td>15</td>
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
<td>jopt-simple-5.0.4.jar</td>
<td>78.1 kB</td>
<td>71</td>
<td>59</td>
<td>3</td>
<td>1.7</td>
<td>Yes</td></tr>
<tr>
<td>commons-lang3-3.19.0.jar</td>
<td>709.1 kB</td>
<td>451</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>449</td>
<td>418</td>
<td>18</td>
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
<td>commons-math3-3.6.1.jar</td>
<td>2.2 MB</td>
<td>1402</td>
<td>1301</td>
<td>75</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>apiguardian-api-1.1.2.jar</td>
<td>6.8 kB</td>
<td>9</td>
<td>3</td>
<td>2</td>
<td>1.6</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-5.13.4.jar</td>
<td>6.4 kB</td>
<td>5</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
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
<td>jmh-core-1.37.jar</td>
<td>553 kB</td>
<td>363</td>
<td>332</td>
<td>13</td>
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
<td>19</td>
<td>13.8 MB</td>
<td>8707</td>
<td>8055</td>
<td>366</td>
<td>9</td>
<td>18</td></tr>
<tr>
<td>compile: 2</td>
<td>compile: 938.7 kB</td>
<td>compile: 678</td>
<td>compile: 502</td>
<td>compile: 22</td>
<td>1.8</td>
<td>compile: 2</td></tr>
<tr>
<td>test: 17</td>
<td>test: 12.8 MB</td>
<td>test: 8029</td>
<td>test: 7553</td>
<td>test: 344</td>
<td>9</td>
<td>test: 16</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-convergence"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/dependency-convergence.html -->

<!-- page_index: 12 -->

# Dependency Convergence

**Statistics:**

| Number of dependencies (NOD): | 19 |
| Number of unique artifacts (NOA): | 19 |
| Number of version-conflicting artifacts (NOC): | 0 |
| Number of SNAPSHOT artifacts (NOS): | 0 |
| Convergence (NOD/NOA): | [Success] **100 %** |
| Ready for release (100% convergence and no SNAPSHOTS): | [Success] **Success** |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/ci-management.html -->

<!-- page_index: 13 -->

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
<pre><a href="https://github.com/apache/commons-csv/actions">https://github.com/apache/commons-csv/actions</a></pre></section><section><a id="Notifiers"></a>
<h1>Notifiers</h1>
<p>No notifiers are defined. Please check back at a later date.</p></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="distribution-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/distribution-management.html -->

<!-- page_index: 14 -->

# Overview

|  |  |
| --- | --- |
|  | Overview The following is the distribution management information used by this project.  Repository - apache.releases.https<https://repository.apache.org/service/local/staging/deploy/maven2>  Snapshot Repository - apache.snapshots.https<https://repository.apache.org/content/repositories/snapshots>  Site - apache.website scm:svn:https://svn.apache.org/repos/infra/websites/production/commons/content/proper/commons-csv/ |

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/project-reports.html -->

<!-- page_index: 15 -->

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
<td><a href="https://commons.apache.org/proper/commons-csv/apidocs/index.html">Javadoc</a></td>
<td>Javadoc API documentation.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-csv/xref/index.html">Source Xref</a></td>
<td>HTML based, cross-reference version of Java source code.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-csv/xref-test/index.html">Test Source Xref</a></td>
<td>HTML based, cross-reference version of Java test source code.</td></tr>
<tr>
<td><a href="#surefire">Surefire</a></td>
<td>Report on the test results of the project.</td></tr>
<tr>
<td><a href="#rat-report">Rat Report</a></td>
<td>Report on compliance to license related source code policies</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-csv/jacoco/index.html">JaCoCo</a></td>
<td>JaCoCo Coverage Report.</td></tr>
<tr>
<td><a href="#japicmp">japicmp</a></td>
<td>Comparing source compatibility of commons-csv-1.14.2-SNAPSHOT.jar against commons-csv-1.14.1.jar</td></tr>
<tr>
<td><a href="#checkstyle">Checkstyle</a></td>
<td>Report on coding style conventions.</td></tr>
<tr>
<td><a href="#cpd">CPD</a></td>
<td>Duplicate code detection.</td></tr>
<tr>
<td><a href="#pmd">PMD</a></td>
<td>Verification of coding rules.</td></tr>
<tr>
<td><a href="#taglist">Tag List</a></td>
<td>Report on various tags found in the code.</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/jira-changes.html -->

<!-- page_index: 16 -->

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

<!-- page_index: 17 -->

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
<td>923</td>
<td>0</td>
<td>0</td>
<td>11</td>
<td>98.8%</td>
<td>2.306 s</td></tr></table>
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
<td><a href="#surefire--org.apache.commons.csv.issues">org.apache.commons.csv.issues</a></td>
<td>60</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.144 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv">org.apache.commons.csv</a></td>
<td>863</td>
<td>0</td>
<td>0</td>
<td>11</td>
<td>98.7%</td>
<td>2.162 s</td></tr></table>
<p>Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.</p><section><a id="org.apache.commons.csv.issues"></a>
<h3>org.apache.commons.csv.issues</h3>
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
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv213test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv213test">JiraCsv213Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv203test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv203test">JiraCsv203Test</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv271test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv271test">JiraCsv271Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv198test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv198test">JiraCsv198Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.132 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv257test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv257test">JiraCsv257Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv247test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv247test">JiraCsv247Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv294test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv294test">JiraCsv294Test</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv150test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv150test">JiraCsv150Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv254test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv254test">JiraCsv254Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv149test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv149test">JiraCsv149Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv148test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv148test">JiraCsv148Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv263test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv263test">JiraCsv263Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv211test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv211test">JiraCsv211Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv167test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv167test">JiraCsv167Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv154test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv154test">JiraCsv154Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv249test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv249test">JiraCsv249Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv248test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv248test">JiraCsv248Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv265test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv265test">JiraCsv265Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv93test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv93test">JiraCsv93Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv253test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv253test">JiraCsv253Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv288test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv288test">JiraCsv288Test</a></td>
<td>12</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv206test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv206test">JiraCsv206Test</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv264test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv264test">JiraCsv264Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv290test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.issues.jiracsv290test">JiraCsv290Test</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv"></a>
<h3>org.apache.commons.csv</h3>
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
<td><a href="#surefire--org.apache.commons.csv.jiracsv318test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.jiracsv318test">JiraCsv318Test</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.007 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvduplicateheadertest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvduplicateheadertest">CSVDuplicateHeaderTest</a></td>
<td>348</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.099 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvformatpredefinedtest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvformatpredefinedtest">CSVFormatPredefinedTest</a></td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.extendedbufferedreadertest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.extendedbufferedreadertest">ExtendedBufferedReaderTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.tokentest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.tokentest">TokenTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvformattest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvformattest">CSVFormatTest</a></td>
<td>109</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.017 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.jiracsv196test"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.jiracsv196test">JiraCsv196Test</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvparsertest"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvparsertest">CSVParserTest</a></td>
<td>154</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>97.4%</td>
<td>0.034 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest">CSVPrinterTest</a></td>
<td>144</td>
<td>0</td>
<td>0</td>
<td>7</td>
<td>95.1%</td>
<td>1.920 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.userguidetest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.userguidetest">UserGuideTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.009 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvrecordtest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvrecordtest">CSVRecordTest</a></td>
<td>31</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.012 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.lexertest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.lexertest">LexerTest</a></td>
<td>33</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.050 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvfileparsertest"><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.csv.csvfileparsertest">CSVFileParserTest</a></td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.008 s</td></tr></table></section>
</section><section><a id="Test_Cases"></a>
<h2>Test Cases</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p><section><a id="org.apache.commons.csv.issues.JiraCsv213Test"></a>
<h3>JiraCsv213Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv213Test.test"></a>test</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv203Test"></a>
<h3>JiraCsv203Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testQuoteModeMinimal"></a>testQuoteModeMinimal</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testWithoutQuoteMode"></a>testWithoutQuoteMode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testQuoteModeNonNumeric"></a>testQuoteModeNonNumeric</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testQuoteModeAllNonNull"></a>testQuoteModeAllNonNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testWithEmptyValues"></a>testWithEmptyValues</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testWithoutNullString"></a>testWithoutNullString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv203Test.testQuoteModeAll"></a>testQuoteModeAll</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv271Test"></a>
<h3>JiraCsv271Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv271Test.testJiraCsv271_withList"></a>testJiraCsv271_withList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv271Test.testJiraCsv271_withArray"></a>testJiraCsv271_withArray</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv198Test"></a>
<h3>JiraCsv198Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv198Test.test"></a>test</td>
<td>0.131 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv257Test"></a>
<h3>JiraCsv257Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv257Test.testNoHeaderBuilder"></a>testNoHeaderBuilder</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv257Test.testHeaderDepreacted"></a>testHeaderDepreacted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv257Test.testHeaderBuilder"></a>testHeaderBuilder</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv247Test"></a>
<h3>JiraCsv247Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv247Test.testHeadersMissingThrowsWhenNotAllowingMissingColumnNames"></a>testHeadersMissingThrowsWhenNotAllowingMissingColumnNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv247Test.testHeadersMissingOneColumnWhenAllowingMissingColumnNames"></a>testHeadersMissingOneColumnWhenAllowingMissingColumnNames</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.JiraCsv318Test"></a>
<h3>JiraCsv318Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv318Test.testDefaultStream"></a>testDefaultStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv318Test.testParallelIOStream"></a>testParallelIOStream</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv318Test.testSequentialStream"></a>testSequentialStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv318Test.testParallelStream"></a>testParallelStream</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv318Test.testParallelIOStreamSynchronizedPrinterNotUsed"></a>testParallelIOStreamSynchronizedPrinterNotUsed</td>
<td>0.004 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVDuplicateHeaderTest"></a>
<h3>CSVDuplicateHeaderTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B1.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B2.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B3.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B4.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B5.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B6.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B7.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B8.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B9.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B10.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B11.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B12.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[12]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B13.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B14.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[14]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B15.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B16.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B17.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[17]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B18.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[18]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B19.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[19]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B20.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[20]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B21.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[21]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B22.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[22]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B23.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[23]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B24.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[24]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B25.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[25]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B26.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[26]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B27.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[27]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B28.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[28]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B29.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[29]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B30.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[30]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B31.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[31]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B32.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[32]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B33.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[33]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B34.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[34]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B35.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[35]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B36.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[36]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B37.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[37]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B38.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[38]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B39.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[39]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B40.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[40]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B41.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[41]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B42.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[42]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B43.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[43]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B44.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[44]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B45.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[45]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B46.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[46]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B47.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[47]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B48.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[48]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B49.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[49]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B50.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[50]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B51.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[51]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B52.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[52]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B53.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[53]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B54.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[54]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B55.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[55]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B56.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[56]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B57.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[57]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B58.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[58]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B59.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[59]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B60.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[60]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B61.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[61]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B62.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[62]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B63.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[63]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B64.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[64]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B65.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[65]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B66.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[66]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B67.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[67]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B68.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[68]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B69.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[69]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B70.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[70]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B71.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[71]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B72.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[72]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B73.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[73]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B74.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[74]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B75.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[75]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B76.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[76]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B77.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[77]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B78.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[78]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B79.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[79]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B80.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[80]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B81.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[81]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B82.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[82]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B83.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[83]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B84.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[84]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B85.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[85]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B86.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[86]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B87.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[87]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B88.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[88]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B89.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[89]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B90.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[90]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B91.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[91]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B92.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[92]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B93.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[93]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B94.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[94]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B95.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[95]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B96.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[96]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B97.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[97]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B98.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[98]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B99.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[99]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B100.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[100]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B101.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[101]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B102.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[102]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B103.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[103]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B104.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[104]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B105.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[105]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B106.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[106]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B107.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[107]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B108.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[108]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B109.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[109]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B110.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[110]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B111.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[111]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B112.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[112]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B113.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[113]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B114.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[114]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B115.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[115]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B116.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[116]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B117.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[117]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B118.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[118]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B119.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[119]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B120.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[120]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B121.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[121]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B122.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[122]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B123.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[123]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B124.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[124]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B125.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[125]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B126.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[126]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B127.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[127]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B128.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[128]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B129.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[129]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B130.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[130]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B131.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[131]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B132.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[132]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B133.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[133]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B134.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[134]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B135.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[135]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B136.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[136]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B137.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[137]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B138.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[138]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B139.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[139]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B140.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[140]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B141.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[141]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B142.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[142]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B143.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[143]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B144.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[144]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B145.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[145]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B146.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[146]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B147.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[147]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B148.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[148]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B149.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[149]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B150.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[150]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B151.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[151]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B152.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[152]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B153.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[153]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B154.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[154]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B155.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[155]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B156.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[156]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B157.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[157]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B158.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[158]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B159.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[159]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B160.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[160]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B161.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[161]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B162.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[162]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B163.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[163]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B164.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[164]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B165.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[165]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B166.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[166]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B167.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[167]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B168.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[168]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B169.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[169]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B170.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[170]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B171.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[171]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B172.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[172]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B173.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[173]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B174.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[174]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B175.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[175]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B176.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[176]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B177.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[177]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B178.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[178]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B179.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[179]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B180.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[180]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B181.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[181]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B182.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[182]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B183.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[183]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B184.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[184]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B185.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[185]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B186.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[186]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B187.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[187]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B188.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[188]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B189.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[189]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B190.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[190]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B191.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[191]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B192.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[192]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B193.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[193]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B194.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[194]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B195.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[195]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B196.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[196]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B197.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[197]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B198.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[198]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B199.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[199]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B200.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[200]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B201.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[201]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B202.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[202]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B203.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[203]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B204.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[204]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B205.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[205]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B206.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[206]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B207.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[207]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B208.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[208]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B209.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[209]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B210.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[210]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B211.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[211]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B212.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[212]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B213.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[213]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B214.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[214]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B215.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[215]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVFormat.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B216.5D"></a>testCSVFormat(DuplicateHeaderMode, boolean, boolean, String[], boolean)[216]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B1.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B2.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B3.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B4.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B5.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B6.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B7.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B8.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B9.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B10.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B11.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B12.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B13.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B14.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B15.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[15]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B16.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[16]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B17.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[17]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B18.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[18]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B19.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[19]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B20.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[20]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B21.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[21]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B22.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[22]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B23.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[23]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B24.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[24]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B25.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[25]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B26.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[26]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B27.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[27]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B28.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[28]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B29.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[29]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B30.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[30]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B31.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[31]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B32.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[32]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B33.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[33]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B34.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[34]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B35.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[35]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B36.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[36]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B37.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[37]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B38.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[38]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B39.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[39]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B40.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[40]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B41.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[41]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B42.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[42]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B43.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[43]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B44.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[44]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B45.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[45]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B46.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[46]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B47.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[47]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B48.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[48]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B49.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[49]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B50.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[50]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B51.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[51]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B52.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[52]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B53.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[53]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B54.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[54]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B55.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[55]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B56.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[56]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B57.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[57]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B58.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[58]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B59.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[59]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B60.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[60]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B61.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[61]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B62.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[62]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B63.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[63]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B64.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[64]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B65.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[65]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B66.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[66]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B67.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[67]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B68.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[68]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B69.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[69]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B70.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[70]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B71.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[71]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B72.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[72]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B73.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[73]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B74.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[74]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B75.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[75]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B76.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[76]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B77.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[77]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B78.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[78]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B79.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[79]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B80.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[80]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B81.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[81]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B82.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[82]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B83.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[83]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B84.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[84]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B85.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[85]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B86.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[86]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B87.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[87]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B88.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[88]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B89.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[89]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B90.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[90]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B91.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[91]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B92.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[92]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B93.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[93]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B94.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[94]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B95.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[95]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B96.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[96]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B97.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[97]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B98.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[98]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B99.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[99]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B100.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[100]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B101.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[101]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B102.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[102]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B103.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[103]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B104.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[104]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B105.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[105]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B106.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[106]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B107.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[107]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B108.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[108]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B109.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[109]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B110.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[110]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B111.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[111]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B112.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[112]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B113.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[113]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B114.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[114]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B115.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[115]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B116.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[116]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B117.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[117]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B118.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[118]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B119.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[119]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B120.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[120]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B121.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[121]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B122.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[122]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B123.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[123]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B124.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[124]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B125.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[125]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B126.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[126]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B127.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[127]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B128.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[128]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B129.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[129]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B130.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[130]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B131.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[131]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVDuplicateHeaderTest.testCSVParser.28DuplicateHeaderMode.2C_boolean.2C_boolean.2C_String.5B.5D.2C_boolean.29.5B132.5D"></a>testCSVParser(DuplicateHeaderMode, boolean, boolean, String[], boolean)[132]</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVFormatPredefinedTest"></a>
<h3>CSVFormatPredefinedTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testTDF"></a>testTDF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testExcel"></a>testExcel</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testMySQL"></a>testMySQL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testMongoDbCsv"></a>testMongoDbCsv</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testMongoDbTsv"></a>testMongoDbTsv</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testRFC4180"></a>testRFC4180</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testPostgreSqlCsv"></a>testPostgreSqlCsv</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testPostgreSqlText"></a>testPostgreSqlText</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testDefault"></a>testDefault</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatPredefinedTest.testOracle"></a>testOracle</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv294Test"></a>
<h3>JiraCsv294Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv294Test.testDefaultCsvFormatWithQuoteEscapeWorks"></a>testDefaultCsvFormatWithQuoteEscapeWorks</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv294Test.testDefaultCsvFormatWithBackslashEscapeWorks"></a>testDefaultCsvFormatWithBackslashEscapeWorks</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv294Test.testDefaultCsvFormatWorks"></a>testDefaultCsvFormatWorks</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv294Test.testDefaultCsvFormatWithNullEscapeWorks"></a>testDefaultCsvFormatWithNullEscapeWorks</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv.ExtendedBufferedReaderTest"></a>
<h3>ExtendedBufferedReaderTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.ExtendedBufferedReaderTest.testEmptyInput"></a>testEmptyInput</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.ExtendedBufferedReaderTest.testReadChar"></a>testReadChar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.ExtendedBufferedReaderTest.testReadLine"></a>testReadLine</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.ExtendedBufferedReaderTest.testReadLookahead1"></a>testReadLookahead1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.ExtendedBufferedReaderTest.testReadLookahead2"></a>testReadLookahead2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.ExtendedBufferedReaderTest.testReadingInDifferentBuffer"></a>testReadingInDifferentBuffer</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv150Test"></a>
<h3>JiraCsv150Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv150Test.testDisableEscaping"></a>testDisableEscaping</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv150Test.testDisableEncapsulation"></a>testDisableEncapsulation</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv150Test.testDisableComment"></a>testDisableComment</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv254Test"></a>
<h3>JiraCsv254Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv254Test.test"></a>test</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.TokenTest"></a>
<h3>TokenTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.TokenTest.testToString.28Type.29.5B1.5D"></a>testToString(Type)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.TokenTest.testToString.28Type.29.5B2.5D"></a>testToString(Type)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.TokenTest.testToString.28Type.29.5B3.5D"></a>testToString(Type)[3]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.TokenTest.testToString.28Type.29.5B4.5D"></a>testToString(Type)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.TokenTest.testToString.28Type.29.5B5.5D"></a>testToString(Type)[5]</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv149Test"></a>
<h3>JiraCsv149Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv149Test.testJiraCsv149EndWithEOL"></a>testJiraCsv149EndWithEOL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv149Test.testJiraCsv149EndWithoutEOL"></a>testJiraCsv149EndWithoutEOL</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv148Test"></a>
<h3>JiraCsv148Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv148Test.testWithTrimEmpty"></a>testWithTrimEmpty</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv148Test.testWithIgnoreSurroundingSpacesEmpty"></a>testWithIgnoreSurroundingSpacesEmpty</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv263Test"></a>
<h3>JiraCsv263Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv263Test.testPrintFromReaderWithQuotes"></a>testPrintFromReaderWithQuotes</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv211Test"></a>
<h3>JiraCsv211Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv211Test.testJiraCsv211Format"></a>testJiraCsv211Format</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv167Test"></a>
<h3>JiraCsv167Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv167Test.testParse"></a>testParse</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv154Test"></a>
<h3>JiraCsv154Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv154Test.testJiraCsv154_withCommentMarker"></a>testJiraCsv154_withCommentMarker</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv154Test.testJiraCsv154_withHeaderComments"></a>testJiraCsv154_withHeaderComments</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv249Test"></a>
<h3>JiraCsv249Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv249Test.testJiraCsv249"></a>testJiraCsv249</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv248Test"></a>
<h3>JiraCsv248Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv248Test.testJiraCsv248"></a>testJiraCsv248</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVFormatTest"></a>
<h3>CSVFormatTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsIgnoreSurroundingSpaces"></a>testEqualsIgnoreSurroundingSpaces</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterSameAsEscapeThrowsException_Deprecated"></a>testDelimiterSameAsEscapeThrowsException_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintWithQuoteModeIsNONE"></a>testPrintWithQuoteModeIsNONE</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsCommentStart"></a>testEqualsCommentStart</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteCharSameAsDelimiterThrowsException_Deprecated"></a>testQuoteCharSameAsDelimiterThrowsException_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testJiraCsv236"></a>testJiraCsv236</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated"></a>testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithDelimiter"></a>testWithDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEscapeSameAsCommentStartThrowsException_Deprecated"></a>testEscapeSameAsCommentStartThrowsException_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testToStringAndWithCommentMarkerTakingCharacter"></a>testToStringAndWithCommentMarkerTakingCharacter</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuotePolicyNoneWithoutEscapeThrowsException"></a>testQuotePolicyNoneWithoutEscapeThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithQuoteLFThrowsException"></a>testWithQuoteLFThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithFirstRecordAsHeader"></a>testWithFirstRecordAsHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsNullString_Deprecated"></a>testEqualsNullString_Deprecated</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testJiraCsv236__Deprecated"></a>testJiraCsv236__Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testSerialization"></a>testSerialization</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testNullRecordSeparatorCsv106"></a>testNullRecordSeparatorCsv106</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testGetDuplicateHeaderMode"></a>testGetDuplicateHeaderMode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsQuoteChar"></a>testEqualsQuoteChar</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testBuildVsGet"></a>testBuildVsGet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testTrim"></a>testTrim</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testNullRecordSeparatorCsv106__Deprecated"></a>testNullRecordSeparatorCsv106__Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithEmptyDuplicates"></a>testWithEmptyDuplicates</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithHeaderComments"></a>testWithHeaderComments</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintRecord"></a>testPrintRecord</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testGetAllowDuplicateHeaderNames"></a>testGetAllowDuplicateHeaderNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintRecordEmpty"></a>testPrintRecordEmpty</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsQuoteChar_Deprecated"></a>testEqualsQuoteChar_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteCharSameAsCommentStartThrowsException"></a>testQuoteCharSameAsCommentStartThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithRecordSeparatorCR"></a>testWithRecordSeparatorCR</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithRecordSeparatorLF"></a>testWithRecordSeparatorLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterSameAsCommentStartThrowsException_Deprecated"></a>testDelimiterSameAsCommentStartThrowsException_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintWithEscapesEndWithoutCRLF"></a>testPrintWithEscapesEndWithoutCRLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithEscapeCRThrowsExceptions"></a>testWithEscapeCRThrowsExceptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithSystemRecordSeparator"></a>testWithSystemRecordSeparator</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithIgnoreEmptyLines"></a>testWithIgnoreEmptyLines</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsNoQuotes"></a>testEqualsNoQuotes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testHashCodeAndWithIgnoreHeaderCase"></a>testHashCodeAndWithIgnoreHeaderCase</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterEmptyStringThrowsException1"></a>testDelimiterEmptyStringThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsTrue"></a>testDuplicateHeaderElementsTrue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsSkipHeaderRecord_Deprecated"></a>testEqualsSkipHeaderRecord_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsIgnoreSurroundingSpaces_Deprecated"></a>testEqualsIgnoreSurroundingSpaces_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsEscape"></a>testEqualsEscape</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsHeader"></a>testEqualsHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsIgnoreEmptyLines"></a>testEqualsIgnoreEmptyLines</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsTrueContainsEmpty1"></a>testDuplicateHeaderElementsTrueContainsEmpty1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsTrueContainsEmpty2"></a>testDuplicateHeaderElementsTrueContainsEmpty2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsTrueContainsEmpty3"></a>testDuplicateHeaderElementsTrueContainsEmpty3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterCharLineBreakCrThrowsException1"></a>testDelimiterCharLineBreakCrThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsHash"></a>testEqualsHash</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsTrue_Deprecated"></a>testDuplicateHeaderElementsTrue_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithCommentStart"></a>testWithCommentStart</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testNewFormat"></a>testNewFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithIgnoreSurround"></a>testWithIgnoreSurround</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testRFC4180"></a>testRFC4180</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterSameAsRecordSeparatorThrowsException"></a>testDelimiterSameAsRecordSeparatorThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEscapeSameAsCommentStartThrowsException"></a>testEscapeSameAsCommentStartThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testFormatThrowsNullPointerException"></a>testFormatThrowsNullPointerException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsDelimiter"></a>testEqualsDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsRecordSeparator_Deprecated"></a>testEqualsRecordSeparator_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterSameAsCommentStartThrowsException1"></a>testDelimiterSameAsCommentStartThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithHeaderResultSetNull"></a>testWithHeaderResultSetNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElements_Deprecated"></a>testDuplicateHeaderElements_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType"></a>testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterSameAsEscapeThrowsException1"></a>testDelimiterSameAsEscapeThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsQuotePolicy_Deprecated"></a>testEqualsQuotePolicy_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteCharSameAsCommentStartThrowsException_Deprecated"></a>testQuoteCharSameAsCommentStartThrowsException_Deprecated</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterCharLineBreakLfThrowsException1"></a>testDelimiterCharLineBreakLfThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsNullString"></a>testEqualsNullString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsHeader_Deprecated"></a>testEqualsHeader_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterStringLineBreakCrThrowsException1"></a>testDelimiterStringLineBreakCrThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsCommentStart_Deprecated"></a>testEqualsCommentStart_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithQuotePolicy"></a>testWithQuotePolicy</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsFalse"></a>testDuplicateHeaderElementsFalse</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsQuotePolicy"></a>testEqualsQuotePolicy</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEscapeSameAsCommentStartThrowsExceptionForWrapperType"></a>testEscapeSameAsCommentStartThrowsExceptionForWrapperType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsNoQuotes_Deprecated"></a>testEqualsNoQuotes_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsRecordSeparator"></a>testEqualsRecordSeparator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithCommentStartCRThrowsException"></a>testWithCommentStartCRThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteModeNoneShouldReturnMeaningfulExceptionMessage"></a>testQuoteModeNoneShouldReturnMeaningfulExceptionMessage</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDelimiterStringLineBreakLfThrowsException1"></a>testDelimiterStringLineBreakLfThrowsException1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteCharSameAsDelimiterThrowsException"></a>testQuoteCharSameAsDelimiterThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintWithoutQuotes"></a>testPrintWithoutQuotes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithDelimiterLFThrowsException"></a>testWithDelimiterLFThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsLeftNoQuoteRightQuote_Deprecated"></a>testEqualsLeftNoQuoteRightQuote_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithEscape"></a>testWithEscape</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithHeader"></a>testWithHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testGetHeader"></a>testGetHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsLeftNoQuoteRightQuote"></a>testEqualsLeftNoQuoteRightQuote</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testFormatToString"></a>testFormatToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithQuoteChar"></a>testWithQuoteChar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEquals"></a>testEquals</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithEmptyEnum"></a>testWithEmptyEnum</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testFormat"></a>testFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithRecordSeparatorCRLF"></a>testWithRecordSeparatorCRLF</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintWithEscapesEndWithCRLF"></a>testPrintWithEscapesEndWithCRLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsIgnoreEmptyLines_Deprecated"></a>testEqualsIgnoreEmptyLines_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsOne"></a>testEqualsOne</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsEscape_Deprecated"></a>testEqualsEscape_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElementsFalse_Deprecated"></a>testDuplicateHeaderElementsFalse_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testDuplicateHeaderElements"></a>testDuplicateHeaderElements</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testPrintWithQuotes"></a>testPrintWithQuotes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithHeaderEnumNull"></a>testWithHeaderEnumNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithNullString"></a>testWithNullString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testWithHeaderEnum"></a>testWithHeaderEnum</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated"></a>testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated"></a>testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFormatTest.testEqualsWithNull"></a>testEqualsWithNull</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.JiraCsv196Test"></a>
<h3>JiraCsv196Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv196Test.testParseFourBytes"></a>testParseFourBytes</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.JiraCsv196Test.testParseThreeBytes"></a>testParseThreeBytes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVParserTest"></a>
<h3>CSVParserTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_HeaderComment1"></a>testGetHeaderComment_HeaderComment1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_HeaderComment2"></a>testGetHeaderComment_HeaderComment2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_HeaderComment3"></a>testGetHeaderComment_HeaderComment3</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvparsertest.testbackslashescapingold"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld"></a><a href="#surefire--org.apache.commons.csv.csvparsertest.testbackslashescapingold">testBackslashEscapingOld</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld');"><span id="org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld-off"> + </span><span id="org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld() throws java.io.IOException is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseWithDelimiterWithQuote"></a>testParseWithDelimiterWithQuote</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141CSVFormat_DEFAULT"></a>testCSV141CSVFormat_DEFAULT</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvparsertest.teststartwithemptylinesthenheaders"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders"></a><a href="#surefire--org.apache.commons.csv.csvparsertest.teststartwithemptylinesthenheaders">testStartWithEmptyLinesThenHeaders</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders');"><span id="org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders-off"> + </span><span id="org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testExcelHeaderCountLessThanData"></a>testExcelHeaderCountLessThanData</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeadersWithNullColumnName"></a>testHeadersWithNullColumnName</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testMultipleIterators"></a>testMultipleIterators</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B1.5D"></a>testGetRecordsMaxRows(long)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B2.5D"></a>testGetRecordsMaxRows(long)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B3.5D"></a>testGetRecordsMaxRows(long)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B4.5D"></a>testGetRecordsMaxRows(long)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B5.5D"></a>testGetRecordsMaxRows(long)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B6.5D"></a>testGetRecordsMaxRows(long)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsMaxRows.28long.29.5B7.5D"></a>testGetRecordsMaxRows(long)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeaderComment"></a>testHeaderComment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_HeaderTrailerComment"></a>testGetHeaderComment_HeaderTrailerComment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testDefaultFormat"></a>testDefaultFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141CSVFormat_INFORMIX_UNLOAD_CSV"></a>testCSV141CSVFormat_INFORMIX_UNLOAD_CSV</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEndOfFileBehaviorExcel"></a>testEndOfFileBehaviorExcel</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordPositionWithCRLF"></a>testGetRecordPositionWithCRLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeaderMissing"></a>testHeaderMissing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_NoComment1"></a>testGetHeaderComment_NoComment1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_NoComment2"></a>testGetHeaderComment_NoComment2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderComment_NoComment3"></a>testGetHeaderComment_NoComment3</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testTrailingDelimiter"></a>testTrailingDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testNotValueCSV"></a>testNotValueCSV</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_MultilineComment"></a>testGetTrailerComment_MultilineComment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseWithDelimiterStringWithQuote"></a>testParseWithDelimiterStringWithQuote</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsePathCharsetNullFormat"></a>testParsePathCharsetNullFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseFileCharsetNullFormat"></a>testParseFileCharsetNullFormat</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvparsertest.testbom"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBOM"></a><a href="#surefire--org.apache.commons.csv.csvparsertest.testbom">testBOM</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testBOM');"><span id="org.apache.commons.csv.CSVParserTest.testBOM-off"> + </span><span id="org.apache.commons.csv.CSVParserTest.testBOM-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>CSV-107</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testFirstEndOfLineCrLf"></a>testFirstEndOfLineCrLf</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testProvidedHeaderAuto"></a>testProvidedHeaderAuto</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordWithMultiLineValues"></a>testGetRecordWithMultiLineValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseWithDelimiterStringWithEscape"></a>testParseWithDelimiterStringWithEscape</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseNullStringFormat"></a>testParseNullStringFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseInputStreamCharsetNullFormat"></a>testParseInputStreamCharsetNullFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseWithDelimiterWithEscape"></a>testParseWithDelimiterWithEscape</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testSkipSetAltHeaders"></a>testSkipSetAltHeaders</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordNumberWithCR"></a>testGetRecordNumberWithCR</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordNumberWithLF"></a>testGetRecordNumberWithLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV57"></a>testCSV57</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParse"></a>testParse</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testTrim"></a>testTrim</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetLineNumberWithCR"></a>testGetLineNumberWithCR</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetLineNumberWithLF"></a>testGetLineNumberWithLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParserUrlNullCharsetFormat"></a>testParserUrlNullCharsetFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B1.5D"></a>testStreamMaxRows(long)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B2.5D"></a>testStreamMaxRows(long)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B3.5D"></a>testStreamMaxRows(long)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B4.5D"></a>testStreamMaxRows(long)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B5.5D"></a>testStreamMaxRows(long)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B6.5D"></a>testStreamMaxRows(long)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStreamMaxRows.28long.29.5B7.5D"></a>testStreamMaxRows(long)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testForEach"></a>testForEach</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetOneLine"></a>testGetOneLine</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetLineNumberWithCRLF"></a>testGetLineNumberWithCRLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCarriageReturnLineFeedEndings"></a>testCarriageReturnLineFeedEndings</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvparsertest.testmongodbcsv"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testMongoDbCsv"></a><a href="#surefire--org.apache.commons.csv.csvparsertest.testmongodbcsv">testMongoDbCsv</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVParserTest.testMongoDbCsv');"><span id="org.apache.commons.csv.CSVParserTest.testMongoDbCsv-off"> + </span><span id="org.apache.commons.csv.CSVParserTest.testMongoDbCsv-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVParserTest.testMongoDbCsv() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordNumberWithCRLF"></a>testGetRecordNumberWithCRLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseUrlCharsetNullFormat"></a>testParseUrlCharsetNullFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEmptyFile"></a>testEmptyFile</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderNames"></a>testGetHeaderNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCarriageReturnEndings"></a>testCarriageReturnEndings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseWithQuoteThrowsException"></a>testParseWithQuoteThrowsException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetLine"></a>testGetLine</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIgnoreCaseHeaderMapping"></a>testIgnoreCaseHeaderMapping</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordPositionWithLF"></a>testGetRecordPositionWithLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetOneLineOneParser"></a>testGetOneLineOneParser</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeadersMissingException"></a>testHeadersMissingException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBOMInputStreamParseWithReader"></a>testBOMInputStreamParseWithReader</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B1.5D"></a>testIteratorMaxRows(long)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B2.5D"></a>testIteratorMaxRows(long)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B3.5D"></a>testIteratorMaxRows(long)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B4.5D"></a>testIteratorMaxRows(long)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B5.5D"></a>testIteratorMaxRows(long)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B6.5D"></a>testIteratorMaxRows(long)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B7.5D"></a>testIteratorMaxRows(long)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorMaxRows.28long.29.5B8.5D"></a>testIteratorMaxRows(long)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderNamesReadOnly"></a>testGetHeaderNamesReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141CSVFormat_INFORMIX_UNLOAD"></a>testCSV141CSVFormat_INFORMIX_UNLOAD</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testDuplicateHeadersAllowedByDefault"></a>testDuplicateHeadersAllowedByDefault</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordsFromBrokenInputStream"></a>testGetRecordsFromBrokenInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testProvidedHeader"></a>testProvidedHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBOMInputStreamParserWithInputStream"></a>testBOMInputStreamParserWithInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141CSVFormat_ORACLE"></a>testCSV141CSVFormat_ORACLE</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIteratorSequenceBreaking"></a>testIteratorSequenceBreaking</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testSkipHeaderOverrideDuplicateHeaders"></a>testSkipHeaderOverrideDuplicateHeaders</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testRepeatedHeadersAreReturnedInCSVRecordHeaderNames"></a>testRepeatedHeadersAreReturnedInCSVRecordHeaderNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordThreeBytesRead"></a>testGetRecordThreeBytesRead</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEmptyLineBehaviorCSV"></a>testEmptyLineBehaviorCSV</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseNullUrlCharsetFormat"></a>testParseNullUrlCharsetFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testInvalidFormat"></a>testInvalidFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141CSVFormat_POSTGRESQL_CSV"></a>testCSV141CSVFormat_POSTGRESQL_CSV</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBackslashEscaping2"></a>testBackslashEscaping2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testExcelFormat1"></a>testExcelFormat1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testExcelFormat2"></a>testExcelFormat2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecordFourBytesRead"></a>testGetRecordFourBytesRead</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testDuplicateHeadersNotAllowed"></a>testDuplicateHeadersNotAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEmptyString"></a>testEmptyString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBOMInputStreamParserWithReader"></a>testBOMInputStreamParserWithReader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testRoundtrip"></a>testRoundtrip</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testNoHeaderMap"></a>testNoHeaderMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseWithQuoteWithEscape"></a>testParseWithQuoteWithEscape</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_HeaderComment1"></a>testGetTrailerComment_HeaderComment1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_HeaderComment2"></a>testGetTrailerComment_HeaderComment2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_HeaderComment3"></a>testGetTrailerComment_HeaderComment3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetHeaderMap"></a>testGetHeaderMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testBackslashEscaping"></a>testBackslashEscaping</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testThrowExceptionWithLineAndPosition"></a>testThrowExceptionWithLineAndPosition</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testLineFeedEndings"></a>testLineFeedEndings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_HeaderTrailerComment1"></a>testGetTrailerComment_HeaderTrailerComment1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_HeaderTrailerComment2"></a>testGetTrailerComment_HeaderTrailerComment2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetTrailerComment_HeaderTrailerComment3"></a>testGetTrailerComment_HeaderTrailerComment3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseNullPathFormat"></a>testParseNullPathFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testMappedButNotSetAsOutlook2007ContactExport"></a>testMappedButNotSetAsOutlook2007ContactExport</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testSkipSetHeader"></a>testSkipSetHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeaderMissingWithNull"></a>testHeaderMissingWithNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIgnoreEmptyLines"></a>testIgnoreEmptyLines</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV235"></a>testCSV235</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEndOfFileBehaviorCSV"></a>testEndOfFileBehaviorCSV</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testNewCSVParserNullReaderFormat"></a>testNewCSVParserNullReaderFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEmptyLineBehaviorExcel"></a>testEmptyLineBehaviorExcel</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseStringNullFormat"></a>testParseStringNullFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeader"></a>testHeader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testGetRecords"></a>testGetRecords</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeadersMissing"></a>testHeadersMissing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141RFC4180"></a>testCSV141RFC4180</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testFirstEndOfLineCr"></a>testFirstEndOfLineCr</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testFirstEndOfLineLf"></a>testFirstEndOfLineLf</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testEmptyFileHeaderParsing"></a>testEmptyFileHeaderParsing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testStream"></a>testStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testCSV141Excel"></a>testCSV141Excel</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testIterator"></a>testIterator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testHeadersMissingOneColumnException"></a>testHeadersMissingOneColumnException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParseNullFileFormat"></a>testParseNullFileFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testSkipAutoHeader"></a>testSkipAutoHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B1.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B2.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B3.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[3]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B4.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B5.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B6.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B7.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B8.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B9.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B10.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[10]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B11.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[11]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testParsingPrintedEmptyFirstColumn.28Predefined.29.5B12.5D"></a>testParsingPrintedEmptyFirstColumn(Predefined)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVParserTest.testNewCSVParserReaderNullFormat"></a>testNewCSVParserReaderNullFormat</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv265Test"></a>
<h3>JiraCsv265Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv265Test.testCharacterPositionWithCommentsSpanningMultipleLines"></a>testCharacterPositionWithCommentsSpanningMultipleLines</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv265Test.testCharacterPositionWithComments"></a>testCharacterPositionWithComments</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv93Test"></a>
<h3>JiraCsv93Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv93Test.testWithSetNullStringNULL"></a>testWithSetNullStringNULL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv93Test.testWithNotSetNullString"></a>testWithNotSetNullString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv93Test.testWithSetNullStringEmptyString"></a>testWithSetNullStringEmptyString</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv253Test"></a>
<h3>JiraCsv253Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv253Test.testHandleAbsentValues"></a>testHandleAbsentValues</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv288Test"></a>
<h3>JiraCsv288Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithTwoCharDelimiter1"></a>testParseWithTwoCharDelimiter1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithTwoCharDelimiter2"></a>testParseWithTwoCharDelimiter2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithTwoCharDelimiter3"></a>testParseWithTwoCharDelimiter3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithTwoCharDelimiter4"></a>testParseWithTwoCharDelimiter4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithABADelimiter"></a>testParseWithABADelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithDoublePipeDelimiterQuoted"></a>testParseWithDoublePipeDelimiterQuoted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithTwoCharDelimiterEndsWithDelimiter"></a>testParseWithTwoCharDelimiterEndsWithDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithDoublePipeDelimiterDoubleCharValue"></a>testParseWithDoublePipeDelimiterDoubleCharValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithDoublePipeDelimiterEndsWithDelimiter"></a>testParseWithDoublePipeDelimiterEndsWithDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithTriplePipeDelimiter"></a>testParseWithTriplePipeDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithSinglePipeDelimiterEndsWithDelimiter"></a>testParseWithSinglePipeDelimiterEndsWithDelimiter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv288Test.testParseWithDoublePipeDelimiter"></a>testParseWithDoublePipeDelimiter</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVPrinterTest"></a>
<h3>CSVPrinterTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintRecordsWithEmptyVector"></a>testPrintRecordsWithEmptyVector</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllIterableOfArraysWithFirstEmptyValue2"></a>testExcelPrintAllIterableOfArraysWithFirstEmptyValue2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintReaderWithoutQuoteToWriter"></a>testPrintReaderWithoutQuoteToWriter</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEolQuoted"></a>testEolQuoted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbTsvBasic"></a>testMongoDbTsvBasic</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testHeaderCommentTdf"></a>testHeaderCommentTdf</td>
<td>0.006 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllArrayOfArraysWithFirstEmptyValue2"></a>testExcelPrintAllArrayOfArraysWithFirstEmptyValue2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimeterQuoteNone"></a>testDelimeterQuoteNone</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testrandommongodbcsv"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testrandommongodbcsv">testRandomMongoDbCsv</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv');"><span id="org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintRecordStream"></a>testPrintRecordStream</td>
<td>0.006 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testHeaderNotSet"></a>testHeaderNotSet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPostgreSqlNullStringDefaultCsv"></a>testPostgreSqlNullStringDefaultCsv</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomExcel"></a>testRandomExcel</td>
<td>0.276 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomMySql"></a>testRandomMySql</td>
<td>0.228 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllArrayOfLists"></a>testExcelPrintAllArrayOfLists</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbCsvBasic"></a>testMongoDbCsvBasic</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintOnePositiveInteger"></a>testPrintOnePositiveInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrint"></a>testPrint</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetHeader.28long.29.5B1.5D"></a>testJdbcPrinterWithResultSetHeader(long)[1]</td>
<td>0.171 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetHeader.28long.29.5B2.5D"></a>testJdbcPrinterWithResultSetHeader(long)[2]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetHeader.28long.29.5B3.5D"></a>testJdbcPrinterWithResultSetHeader(long)[3]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetHeader.28long.29.5B4.5D"></a>testJdbcPrinterWithResultSetHeader(long)[4]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetHeader.28long.29.5B5.5D"></a>testJdbcPrinterWithResultSetHeader(long)[5]</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testNewCsvPrinterNullAppendableFormat"></a>testNewCsvPrinterNullAppendableFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testQuoteNonNumeric"></a>testQuoteNonNumeric</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintRecordsWithResultSetOneRow"></a>testPrintRecordsWithResultSetOneRow</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbTsvTabInValue"></a>testMongoDbTsvTabInValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCloseWithCsvFormatAutoFlushOff"></a>testCloseWithCsvFormatAutoFlushOff</td>
<td>0.193 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetMetaData.28long.29.5B1.5D"></a>testJdbcPrinterWithResultSetMetaData(long)[1]</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetMetaData.28long.29.5B2.5D"></a>testJdbcPrinterWithResultSetMetaData(long)[2]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetMetaData.28long.29.5B3.5D"></a>testJdbcPrinterWithResultSetMetaData(long)[3]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetMetaData.28long.29.5B4.5D"></a>testJdbcPrinterWithResultSetMetaData(long)[4]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSetMetaData.28long.29.5B5.5D"></a>testJdbcPrinterWithResultSetMetaData(long)[5]</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEolPlain"></a>testEolPlain</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbTsvCommaInValue"></a>testMongoDbTsvCommaInValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbCsvCommaInValue"></a>testMongoDbCsvCommaInValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeNull1"></a>testEscapeNull1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeNull2"></a>testEscapeNull2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeNull3"></a>testEscapeNull3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeNull4"></a>testEscapeNull4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeNull5"></a>testEscapeNull5</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintRecordsWithCSVRecord"></a>testPrintRecordsWithCSVRecord</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter1"></a>testPrinter1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter2"></a>testPrinter2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter3"></a>testPrinter3</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter4"></a>testPrinter4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter5"></a>testPrinter5</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter6"></a>testPrinter6</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrinter7"></a>testPrinter7</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimiterPlain"></a>testDelimiterPlain</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJira135_part1"></a>testJira135_part1</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testjira135_part2"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJira135_part2"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testjira135_part2">testJira135_part2</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testJira135_part2');"><span id="org.apache.commons.csv.CSVPrinterTest.testJira135_part2-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testJira135_part2-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testJira135_part2() throws java.io.IOException is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJira135_part3"></a>testJira135_part3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlText"></a>testRandomPostgreSqlText</td>
<td>0.247 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllArrayOfArraysWithFirstSpaceValue1"></a>testExcelPrintAllArrayOfArraysWithFirstSpaceValue1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testSingleQuoteQuoted"></a>testSingleQuoteQuoted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintRecordsWithObjectArray"></a>testPrintRecordsWithObjectArray</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimeterStringQuoteNone"></a>testDelimeterStringQuoteNone</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testTrimOffOneColumn"></a>testTrimOffOneColumn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbCsvTabInValue"></a>testMongoDbCsvTabInValue</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDontQuoteEuroFirstChar"></a>testDontQuoteEuroFirstChar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testTrailingDelimiterOnTwoColumns"></a>testTrailingDelimiterOnTwoColumns</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testQuoteAll"></a>testQuoteAll</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomTdf"></a>testRandomTdf</td>
<td>0.208 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintToFileWithCharsetUtf16Be"></a>testPrintToFileWithCharsetUtf16Be</td>
<td>0.007 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testpostgresqlcsvtextoutput"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testpostgresqlcsvtextoutput">testPostgreSqlCsvTextOutput</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput');"><span id="org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput() throws java.io.IOException is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllStreamOfArrays.28long.29.5B1.5D"></a>testExcelPrintAllStreamOfArrays(long)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllStreamOfArrays.28long.29.5B2.5D"></a>testExcelPrintAllStreamOfArrays(long)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllStreamOfArrays.28long.29.5B3.5D"></a>testExcelPrintAllStreamOfArrays(long)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllStreamOfArrays.28long.29.5B4.5D"></a>testExcelPrintAllStreamOfArrays(long)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllStreamOfArrays.28long.29.5B5.5D"></a>testExcelPrintAllStreamOfArrays(long)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPostgreSqlNullStringDefaultText"></a>testPostgreSqlNullStringDefaultText</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintToPathWithDefaultCharset"></a>testPrintToPathWithDefaultCharset</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testpostgresqlcsvnulloutput"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testpostgresqlcsvnulloutput">testPostgreSqlCsvNullOutput</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput');"><span id="org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput() throws java.io.IOException is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVRecords.28long.29.5B1.5D"></a>testPrintCSVRecords(long)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVRecords.28long.29.5B2.5D"></a>testPrintCSVRecords(long)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVRecords.28long.29.5B3.5D"></a>testPrintCSVRecords(long)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVRecords.28long.29.5B4.5D"></a>testPrintCSVRecords(long)[4]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVRecords.28long.29.5B5.5D"></a>testPrintCSVRecords(long)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllIterableOfLists"></a>testExcelPrintAllIterableOfLists</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testTrimOnOneColumn"></a>testTrimOnOneColumn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimeterQuoted"></a>testDelimeterQuoted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testSkipHeaderRecordFalse"></a>testSkipHeaderRecordFalse</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllArrayOfArraysWithFirstTabValue1"></a>testExcelPrintAllArrayOfArraysWithFirstTabValue1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPlainPlain"></a>testPlainPlain</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testSingleLineComment"></a>testSingleLineComment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllIterableOfArrays"></a>testExcelPrintAllIterableOfArrays</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testNewCsvPrinterAppendableNullFormat"></a>testNewCsvPrinterAppendableNullFormat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testInvalidFormat"></a>testInvalidFormat</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testrandomoracle"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomOracle"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testrandomoracle">testRandomOracle</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testRandomOracle');"><span id="org.apache.commons.csv.CSVPrinterTest.testRandomOracle-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testRandomOracle-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testRandomOracle() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMultiLineComment"></a>testMultiLineComment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithFirstEmptyValue2"></a>testJdbcPrinterWithFirstEmptyValue2</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllArrayOfListsWithFirstEmptyValue2"></a>testExcelPrintAllArrayOfListsWithFirstEmptyValue2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B1.5D"></a>testJdbcPrinterWithResultSet(long)[1]</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B2.5D"></a>testJdbcPrinterWithResultSet(long)[2]</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B3.5D"></a>testJdbcPrinterWithResultSet(long)[3]</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B4.5D"></a>testJdbcPrinterWithResultSet(long)[4]</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B5.5D"></a>testJdbcPrinterWithResultSet(long)[5]</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B6.5D"></a>testJdbcPrinterWithResultSet(long)[6]</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinterWithResultSet.28long.29.5B7.5D"></a>testJdbcPrinterWithResultSet(long)[7]</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testQuoteCommaFirstChar"></a>testQuoteCommaFirstChar</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPlainQuoted"></a>testPlainQuoted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testNotFlushable"></a>testNotFlushable</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomRfc4180"></a>testRandomRfc4180</td>
<td>0.241 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrintAllArrayOfArrays"></a>testExcelPrintAllArrayOfArrays</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimeterStringQuoted"></a>testDelimeterStringQuoted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJdbcPrinter"></a>testJdbcPrinter</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeBackslash1"></a>testEscapeBackslash1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeBackslash2"></a>testEscapeBackslash2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeBackslash3"></a>testEscapeBackslash3</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeBackslash4"></a>testEscapeBackslash4</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEscapeBackslash5"></a>testEscapeBackslash5</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testSkipHeaderRecordTrue"></a>testSkipHeaderRecordTrue</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomDefault"></a>testRandomDefault</td>
<td>0.202 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCloseBackwardCompatibility"></a>testCloseBackwardCompatibility</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCloseWithCsvFormatAutoFlushOn"></a>testCloseWithCsvFormatAutoFlushOn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testTrimOnTwoColumns"></a>testTrimOnTwoColumns</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimiterEscaped"></a>testDelimiterEscaped</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCSV135"></a>testCSV135</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCSV259"></a>testCSV259</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEquals"></a>testEquals</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testHeader"></a>testHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testParseCustomNullValues"></a>testParseCustomNullValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMongoDbCsvDoubleQuoteInValue"></a>testMongoDbCsvDoubleQuoteInValue</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCustomNullValues"></a>testPrintCustomNullValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testEolEscaped"></a>testEolEscaped</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVParser"></a>testPrintCSVParser</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCRComment"></a>testCRComment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintNullValues"></a>testPrintNullValues</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testrandompostgresqlcsv"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testrandompostgresqlcsv">testRandomPostgreSqlCsv</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv');"><span id="org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintCSVRecord"></a>testPrintCSVRecord</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testHeaderCommentExcel"></a>testHeaderCommentExcel</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrinter1"></a>testExcelPrinter1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testExcelPrinter2"></a>testExcelPrinter2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCloseWithFlushOn"></a>testCloseWithFlushOn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMySqlNullOutput"></a>testMySqlNullOutput</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintReaderWithoutQuoteToAppendable"></a>testPrintReaderWithoutQuoteToAppendable</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.csv.csvprintertest.testjira135all"><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></a></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testJira135All"></a><a href="#surefire--org.apache.commons.csv.csvprintertest.testjira135all">testJira135All</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.csv.CSVPrinterTest.testJira135All');"><span id="org.apache.commons.csv.CSVPrinterTest.testJira135All-off"> + </span><span id="org.apache.commons.csv.CSVPrinterTest.testJira135All-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.csv.CSVPrinterTest.testJira135All() throws java.io.IOException is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testMySqlNullStringDefault"></a>testMySqlNullStringDefault</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPlainEscaped"></a>testPlainEscaped</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testPrintToFileWithDefaultCharset"></a>testPrintToFileWithDefaultCharset</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDelimiterStringEscaped"></a>testDelimiterStringEscaped</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testCloseWithFlushOff"></a>testCloseWithFlushOff</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVPrinterTest.testDisabledComment"></a>testDisabledComment</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.UserGuideTest"></a>
<h3>UserGuideTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.UserGuideTest.testBomFull"></a>testBomFull</td>
<td>0.008 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.UserGuideTest.testBomUtil"></a>testBomUtil</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv206Test"></a>
<h3>JiraCsv206Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv206Test.testJiraCsv206MultipleCharacterDelimiter"></a>testJiraCsv206MultipleCharacterDelimiter</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVRecordTest"></a>
<h3>CSVRecordTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testIsInconsistent"></a>testIsInconsistent</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testRemoveAndAddColumns"></a>testRemoveAndAddColumns</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testPutInMap"></a>testPutInMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testIsConsistent"></a>testIsConsistent</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testSerialization"></a>testSerialization</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToMap"></a>testToMap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testDuplicateHeaderToMap"></a>testDuplicateHeaderToMap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToListAdd"></a>testToListAdd</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToListFor"></a>testToListFor</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToListSet"></a>testToListSet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testCSVRecordNULLValues"></a>testCSVRecordNULLValues</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetNullEnum"></a>testGetNullEnum</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testDuplicateHeaderGet"></a>testDuplicateHeaderGet</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testIsMapped"></a>testIsMapped</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetWithEnum"></a>testGetWithEnum</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testIsSetInt"></a>testIsSetInt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetStringInconsistentRecord"></a>testGetStringInconsistentRecord</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToMapWithShortRecord"></a>testToMapWithShortRecord</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetStringNoHeader"></a>testGetStringNoHeader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToListForEach"></a>testToListForEach</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetUnmappedPositiveInt"></a>testGetUnmappedPositiveInt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testIsSetString"></a>testIsSetString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetUnmappedNegativeInt"></a>testGetUnmappedNegativeInt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetUnmappedEnum"></a>testGetUnmappedEnum</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetUnmappedName"></a>testGetUnmappedName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetInt"></a>testGetInt</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testGetString"></a>testGetString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testStream"></a>testStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testIterator"></a>testIterator</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVRecordTest.testToMapWithNoHeader"></a>testToMapWithNoHeader</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.LexerTest"></a>
<h3>LexerTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testNextToken4"></a>testNextToken4</td>
<td>0.013 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testNextToken5"></a>testNextToken5</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testNextToken6"></a>testNextToken6</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testReadEscapeBackspace"></a>testReadEscapeBackspace</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEOFWithoutClosingQuote"></a>testEOFWithoutClosingQuote</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testTab"></a>testTab</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testTrimTrailingSpacesZeroLength"></a>testTrimTrailingSpacesZeroLength</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testSurroundingSpacesAreDeleted"></a>testSurroundingSpacesAreDeleted</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedControlCharacter2"></a>testEscapedControlCharacter2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testCommentsAndEmptyLines"></a>testCommentsAndEmptyLines</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testCR"></a>testCR</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testFF"></a>testFF</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testLF"></a>testLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedTab"></a>testEscapedTab</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testIsMetaCharCommentStart"></a>testIsMetaCharCommentStart</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testTrailingTextAfterQuote"></a>testTrailingTextAfterQuote</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testComments"></a>testComments</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testSurroundingTabsAreDeleted"></a>testSurroundingTabsAreDeleted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapingAtEOF"></a>testEscapingAtEOF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedMySqlNullValue"></a>testEscapedMySqlNullValue</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedBackspace"></a>testEscapedBackspace</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testBackslashWithEscaping"></a>testBackslashWithEscaping</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedCharacter"></a>testEscapedCharacter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testBackslashWithoutEscaping"></a>testBackslashWithoutEscaping</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testDelimiterIsWhitespace"></a>testDelimiterIsWhitespace</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testIgnoreEmptyLines"></a>testIgnoreEmptyLines</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testReadEscapeTab"></a>testReadEscapeTab</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testReadEscapeFF"></a>testReadEscapeFF</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedControlCharacter"></a>testEscapedControlCharacter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedCR"></a>testEscapedCR</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedFF"></a>testEscapedFF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testEscapedLF"></a>testEscapedLF</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.LexerTest.testBackspace"></a>testBackspace</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv264Test"></a>
<h3>JiraCsv264Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv264Test.testJiraCsv264"></a>testJiraCsv264</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv264Test.testJiraCsv264WithGapAllowEmpty"></a>testJiraCsv264WithGapAllowEmpty</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv264Test.testJiraCsv264WithGapDisallow"></a>testJiraCsv264WithGapDisallow</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.CSVFileParserTest"></a>
<h3>CSVFileParserTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B1.5D"></a>testCSVFile(File)[1]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B2.5D"></a>testCSVFile(File)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B3.5D"></a>testCSVFile(File)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B4.5D"></a>testCSVFile(File)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B5.5D"></a>testCSVFile(File)[5]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B6.5D"></a>testCSVFile(File)[6]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVFile.28File.29.5B7.5D"></a>testCSVFile(File)[7]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B1.5D"></a>testCSVUrl(File)[1]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B2.5D"></a>testCSVUrl(File)[2]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B3.5D"></a>testCSVUrl(File)[3]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B4.5D"></a>testCSVUrl(File)[4]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B5.5D"></a>testCSVUrl(File)[5]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B6.5D"></a>testCSVUrl(File)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.CSVFileParserTest.testCSVUrl.28File.29.5B7.5D"></a>testCSVUrl(File)[7]</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.csv.issues.JiraCsv290Test"></a>
<h3>JiraCsv290Test</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv290Test.testPostgresqlText"></a>testPostgresqlText</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv290Test.testWriteThenRead"></a>testWriteThenRead</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_44d131d789b1def9.gif"/></td>
<td><a id="TC_org.apache.commons.csv.issues.JiraCsv290Test.testPostgresqlCsv"></a>testPostgresqlCsv</td>
<td>0.001 s</td></tr></table></section>
</section><section><a id="Failure_Details"></a>
<h2>Failure Details</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p>
<table>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld"></a>testBackslashEscapingOld</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVParserTest.testBackslashEscapingOld() throws java.io.IOException is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders"></a>testStartWithEmptyLinesThenHeaders</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVParserTest.testStartWithEmptyLinesThenHeaders() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVParserTest.testBOM"></a>testBOM</td></tr>
<tr>
<td>-</td>
<td>skipped: CSV-107</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVParserTest.testMongoDbCsv"></a>testMongoDbCsv</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVParserTest.testMongoDbCsv() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv"></a>testRandomMongoDbCsv</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testRandomMongoDbCsv() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testJira135_part2"></a>testJira135_part2</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testJira135_part2() throws java.io.IOException is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput"></a>testPostgreSqlCsvTextOutput</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvTextOutput() throws java.io.IOException is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput"></a>testPostgreSqlCsvNullOutput</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testPostgreSqlCsvNullOutput() throws java.io.IOException is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testRandomOracle"></a>testRandomOracle</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testRandomOracle() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv"></a>testRandomPostgreSqlCsv</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testRandomPostgreSqlCsv() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_058e8ca2ac7b6856.gif"/></td>
<td><a id="org.apache.commons.csv.CSVPrinterTest.testJira135All"></a>testJira135All</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.csv.CSVPrinterTest.testJira135All() throws java.io.IOException is @Disabled</td></tr></table>
</section></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/rat-report.html -->

<!-- page_index: 18 -->

# Rat (Release Audit Tool) results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h1>Rat (Release Audit Tool) results</h1>
<p>The following document contains the results of <a href="https://creadur.apache.org/rat/apache-rat-plugin/">Rat (Release Audit Tool)</a>.</p>
<p></p>
<pre>
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
</pre></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/japicmp.html -->

<!-- page_index: 19 -->

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

<!-- page_index: 20 -->

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 11.0.1 with /Users/garygregory/git/commons-csv/src/conf/checkstyle/checkstyle.xml ruleset.

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 54 | 0 | 0 | 0 |

## Files

| File | I | W | E |
| --- | --- | --- | --- |

## Details

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/cpd.html -->

<!-- page_index: 21 -->

# CPD Results

|  |  |
| --- | --- |
|  | CPD Results The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 7.17.0.  CPD found no problems in your source code. |

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/pmd.html -->

<!-- page_index: 22 -->

# PMD Results

|  |  |
| --- | --- |
|  | PMD Results The following document contains the results of [PMD](https://pmd.github.io) 7.17.0.  PMD found no problems in your source code. |

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="taglist"></a>

<!-- source_url: https://commons.apache.org/proper/commons-csv/taglist.html -->

<!-- page_index: 23 -->

# Tag List Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Tag_List_Report"></a>
<h1>Tag List Report</h1>
<p>The following document contains the listing of user tags found in the code. Below is the summary of the occurrences per tag.</p>
<table>
<tr>
<th>Tag Class</th>
<th>Total number of occurrences</th>
<th>Tag strings used by tag class</th></tr>
<tr>
<td><a href="#taglist--tag_class_1">Needs Work</a></td>
<td>9</td>
<td>TODO, FIXME, XXX</td></tr>
<tr>
<td>Notable Markers</td>
<td>0</td>
<td>NOTE, NOPMD, NOSONAR</td></tr></table>
<p>Each tag is detailed below:</p><section><a id="tag_class_1"></a>
<h2>Needs Work</h2>
<p>Number of occurrences found in the code: 9</p>
<table>
<tr>
<th>org.apache.commons.csv.CSVParserTest</th>
<th>Line</th></tr>
<tr>
<td>this may lead to strange behavior, throw an exception if iterator() has already been called?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/CSVParserTest.html#L1328">1328</a></td></tr>
<tr>
<th>org.apache.commons.csv.CSVPrinter</th>
<th>Line</th></tr>
<tr>
<td>Is it a good idea to do this here instead of on the first call to a print method? It seems a pain to have to track whether the header has already been printed or not.</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/CSVPrinter.html#L112">112</a></td></tr>
<tr>
<th>org.apache.commons.csv.Lexer</th>
<th>Line</th></tr>
<tr>
<td>escape handling needs more work</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L470">470</a></td></tr>
<tr>
<td>is this correct?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L495">495</a></td></tr>
<tr>
<td>is this correct? Do tabs need to be escaped?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L496">496</a></td></tr>
<tr>
<td>is this correct?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref/org/apache/commons/csv/Lexer.html#L497">497</a></td></tr>
<tr>
<th>org.apache.commons.csv.LexerTest</th>
<th>Line</th></tr>
<tr>
<td>is this correct? Do we expect &lt;esc&gt;BACKSPACE to be unescaped?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/LexerTest.html#L232">232</a></td></tr>
<tr>
<td>is this correct? Do we expect &lt;esc&gt;FF to be unescaped?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/LexerTest.html#L268">268</a></td></tr>
<tr>
<td>is this correct? Do we expect &lt;esc&gt;TAB to be unescaped?</td>
<td><a href="https://commons.apache.org/proper/commons-csv/xref-test/org/apache/commons/csv/LexerTest.html#L290">290</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2005-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons CSV, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---
