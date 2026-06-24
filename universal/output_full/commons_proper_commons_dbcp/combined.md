# Project Information

## Navigation

- Commons DBCP
  - [About](#index_2)
  - [Asking Questions](https://commons.apache.org/proper/commons-dbcp/mail-lists.html)
  - [Release History](#changes)
  - [Issue Tracking](#issue-management)
  - [Dependency Management](#dependency-info)
  - [Sources](#scm)
  - [Security](#security)
  - [License](https://www.apache.org/licenses/LICENSE-2.0)
  - [Code of Conduct](https://www.apache.org/foundation/policies/conduct.html)
  - [Download](https://commons.apache.org/proper/commons-dbcp/download_dbcp.cgi)
  - [Javadoc](#index)
    - [Javadoc Current](https://commons.apache.org/proper/commons-dbcp/apidocs/index.html)
    - [Javadoc 2.x Archive](https://javadoc.io/doc/org.apache.commons/commons-dbcp2/latest/index.html)
    - [Javadoc 1.x Archive](https://javadoc.io/doc/commons-dbcp/commons-dbcp/1.4/index.html)
  - [Configuration](#configuration)
  - [Developers Guide](#guide)
    - [JNDI Howto](#guide-jndi-howto)
    - [Class Diagrams](#guide-classdiagrams)
    - [Sequence Diagrams](#guide-sequencediagrams)
    - [Building](#building)
  - [Examples](https://gitbox.apache.org/repos/asf?p=commons-dbcp.git%3Ba%3Dtree%3Bf%3Ddoc%3Bhb%3DHEAD)
  - [Downloads](https://commons.apache.org/proper/commons-dbcp/download_dbcp.cgi)
  - [Wiki](https://wiki.apache.org/commons/DBCP)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index_2)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [Issue Management](#issue-management)
    - [Mailing Lists](https://commons.apache.org/proper/commons-dbcp/mailing-lists.html)
    - [Maven Coordinates](#dependency-info)
    - [Dependency Management](#dependency-management)
    - [Dependencies](#dependencies)
    - [Dependency Convergence](#dependency-convergence)
    - [CI Management](#ci-management)
    - [Distribution Management](#distribution-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes)
    - [JIRA Report](#jira-changes)
    - [Javadoc](https://commons.apache.org/proper/commons-dbcp/apidocs/index.html)
    - [Source Xref](https://commons.apache.org/proper/commons-dbcp/xref/index.html)
    - [Test Source Xref](https://commons.apache.org/proper/commons-dbcp/xref-test/index.html)
    - [Surefire](#surefire)
    - [RAT Report](#rat-report)
    - [japicmp](#japicmp)
    - [SpotBugs](#spotbugs)
    - [Checkstyle](#checkstyle)
    - [PMD](#pmd)
    - [CPD](#cpd)
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

<a id="index_2"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/index.html -->

<!-- page_index: 1 -->

# The DBCP Component

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="The_DBCP_Component"></a>
<h1>The DBCP Component</h1>
<p>Many Apache projects support interaction with a relational database.
Creating a new connection for each user can be time consuming (often
requiring multiple seconds of clock time), in order to perform a database
transaction that might take milliseconds.  Opening a connection per user
can be unfeasible in a publicly-hosted Internet application where the
number of simultaneous users can be very large.  Accordingly, developers
often wish to share a "pool" of open connections between all of the
application's current users.  The number of users actually performing
a request at any given time is usually a very small percentage of the
total number of active users, and during request processing is the only
time that a database connection is required.  The application itself logs
into the DBMS, and handles any user account issues internally.</p>
<p>There are several Database Connection Pools already available, both
within Apache products and elsewhere.  This Commons package provides an
opportunity to coordinate the efforts required to create and maintain an
efficient, feature-rich package under the ASF license.</p>
<p>The <code>commons-dbcp2</code> artifact relies on code in the
<code>commons-pool2</code> artifact to provide the underlying object pool
mechanisms.</p>
<p>DBCP now comes in four different versions to support different versions of
JDBC. Here is how it works:</p>
<p>Developing</p>
<ul>
<li>DBCP 2.5.0 and up compiles and runs under Java 8
(<a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/jdbc_42.html">JDBC 4.2</a>) and up.</li>
<li>DBCP 2.4.0 compiles and runs under Java 7
(<a href="https://docs.oracle.com/javase/7/docs/technotes/guides/jdbc/jdbc_41.html">JDBC 4.1</a>) and above.</li>
</ul>
<p>Running</p>
<ul>
<li>DBCP 2.5.0 and up binaries should be used by applications running on Java 8 and up.</li>
<li>DBCP 2.4.0 binaries should be used by applications running under Java 7.</li>
</ul>
<p>DBCP 2 is based on
<a href="https://commons.apache.org/proper/commons-pool/">Apache Commons Pool</a>
and provides increased performance, JMX
support as well as numerous other new features compared to DBCP 1.x. Users
upgrading to 2.x should be aware that the Java package name has changed, as well
as the Maven co-ordinates, since DBCP 2.x is not binary compatible with DBCP
1.x. Users should also be aware that some configuration options (e.g. maxActive
to maxTotal) have been renamed to align them with the new names used by Commons
Pool.</p>
</section>
<section><a id="Releases"></a>
<h1>Releases</h1>
<p>
       See the <a href="https://commons.apache.org/proper/commons-dbcp/download_dbcp.cgi">downloads</a> page for information on
       obtaining releases.
    </p>
</section>
<section><a id="Documentation"></a>
<h1>Documentation</h1>
<p>The
<a href="https://commons.apache.org/proper/commons-dbcp/apidocs/index.html">Javadoc API documents</a>
are available online.  In particular, you should
read the package overview of the
<code><a href="https://commons.apache.org/proper/commons-dbcp/apidocs/org/apache/commons/dbcp2/package-summary.html#package_description">org.apache.commons.dbcp2</a></code>
package for an overview of how to use DBCP.</p>
<p>There are
<a href="https://gitbox.apache.org/repos/asf?p=commons-dbcp.git;a=tree;f=doc;hb=refs/heads/master">several examples</a>
of using DBCP available.</p>
</section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/changes.html -->

<!-- page_index: 2 -->

# Apache Commons DBCP Release Notes

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Apache_Commons_DBCP_Release_Notes"></a>
<h1>Apache Commons DBCP Release Notes</h1><section><a id="Release_History"></a>
<h2>Release History</h2>
<table>
<tr>
<th>Version</th>
<th>Date</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes--a2.14.0">2.14.0</a></td>
<td>2025-12-11</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.13.0">2.13.0</a></td>
<td>2024-11-23</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.12.0">2.12.0</a></td>
<td>2024-02-29</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.11.0">2.11.0</a></td>
<td>2023-10-23</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.10.0">2.10.0</a></td>
<td>2023-08-28</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.9.0">2.9.0</a></td>
<td>2021-07-30</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.8.0">2.8.0</a></td>
<td>2020-09-21</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.7.0">2.7.0</a></td>
<td>2019-07-31</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.6.0">2.6.0</a></td>
<td>2019-02-14</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.5.0">2.5.0</a></td>
<td>2018-07-15</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.4.0">2.4.0</a></td>
<td>2018-06-12</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.3.0">2.3.0</a></td>
<td>2018-05-12</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.2.0">2.2.0</a></td>
<td>2017-12-27</td>
<td>This is a minor release, including bug fixes and enhancements.</td></tr>
<tr>
<td><a href="#changes--a2.1.1">2.1.1</a></td>
<td>6 Aug 2015</td>
<td>This is a patch release, including bug fixes only.</td></tr>
<tr>
<td><a href="#changes--a2.1">2.1</a></td>
<td>23 Feb 2015</td>
<td>This is minor release, including bug fixes and enhancements. Note that   one of the enhancements (DBCP-423) is to implement AutoCloseable in   BasicDataSource, PoolingDataSource and the InstanceKeyDataSource   implementations.</td></tr>
<tr>
<td><a href="#changes--a2.0.1">2.0.1</a></td>
<td>24 May 2014</td>
<td>This is a bug fix release.</td></tr>
<tr>
<td><a href="#changes--a2.0">2.0</a></td>
<td>3 March 2014</td>
<td>This release includes new features as well as bug fixes and enhancements.  Version 2.0.x supports JDBC 4.1, so requires Java 7.   The Java package name has been changed from 'org.apache.commons.dbcp' to 'org.apache.commons.dbcp2'.  Also the Maven groupId is now 'org.apache.commons' and the artifactId is 'commons-dbcp2'  These changes are necessary because the API is not strictly binary compatible with the 1.x releases.  To convert from the earlier releases, update the package name in imports, update the dependencies and recompile.  There may be a few other changes to be made.   Applications running under Java 7 should use DBCP 2.0.x.  Java 6 users should use DBCP 1.4.x which supports JDBC 4.  Java 1.4 and Java 5 users should use DBCP 1.3.x which supports JDBC 3.</td></tr>
<tr>
<td><a href="#changes--a1.5.1">1.5.1</a></td>
<td>not yet released</td>
<td>TBD</td></tr>
<tr>
<td><a href="#changes--a1.4.1">1.4.1</a></td>
<td>not yet released</td>
<td>TBD</td></tr>
<tr>
<td><a href="#changes--a1.4">1.4</a></td>
<td>2010-02-14</td>
<td>This release includes      new features as well as bug fixes and enhancements.  Some bug fixes      change semantics (e.g. connection close is now idempotent).  The 1.3      and 1.4 releases of DBCP are built from the same sources.  Version 1.4      supports JDBC 4, so requires JDK 1.6. Applications running under      JDK 1.4-1.5 must use DBCP 1.3. Applications running under JDK 1.6      should use DBCP 1.4. Other than support for the added methods in JDBC 4,      there is nothing new or different in DBCP 1.4 vs. DBCP 1.3.   The list of      changes below since 1.2.2 applies to both the 1.3 and 1.4 release.  Other than      the one issue related to adding JDBC 4 support (DBCP-191), all bug fixes      or new features are included in both DBCP 1.3 and 1.4</td></tr>
<tr>
<td><a href="#changes--a1.3">1.3</a></td>
<td>2010-02-14</td>
<td>Compatability release for JDBC 3.       See version 1.4 description and change log.</td></tr>
<tr>
<td><a href="#changes--a1.2.2">1.2.2</a></td>
<td>2007-04-04</td>
<td>This is a maintenance release containing bug fixes       and enhancements. All API changes are binary compatible with version 1.2.1.</td></tr>
<tr>
<td><a href="#changes--a1.2.1">1.2.1</a></td>
<td>2004-06-12</td>
<td>Maintenance Release to restore JDK 1.3 compatibility</td></tr>
<tr>
<td><a href="#changes--a1.2">1.2</a></td>
<td>2004-06-07</td>
<td> </td></tr>
<tr>
<td><a href="#changes--a1.1">1.1</a></td>
<td>2003-10-20</td>
<td> </td></tr>
<tr>
<td><a href="#changes--a1.0">1.0</a></td>
<td>2002-08-12</td>
<td>Initial Release</td></tr></table></section><section><a id="a2.14.0"></a>
<h2>Release 2.14.0 – 2025-12-11</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Validation query not timing out on connections managed by SharedPoolDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-597">DBCP-597</a>. Thanks to Xiaotian Bai, Raju Gupta, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Validation query not timing out on connections managed by PerUserPoolDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-597">DBCP-597</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>KeyedCPDSConnectionFactory.validateObject(UserPassKey, PooledObject) ignores timeouts less than 1 second when there is no validation query. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-597">DBCP-597</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modernize tests to use JUnit 5 features. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Javadoc is missing its Overview page. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Deprecate org.apache.commons.dbcp2.Jdbc41Bridge.Jdbc41Bridge(), constructor will be private in the next major release. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Deprecate org.apache.commons.dbcp2.Constants.Constants(), constructor will be private in the next major release. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix Javadoc warnings on Java 17. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix Javadoc warnings on Java 21. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>XAException thrown by LocalXAResource now all include a message. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "isSharedConnection" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.managed.ManagedConnection] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "closed" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.cpdsadapter.PooledConnectionImpl] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "closed" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.DelegatingStatement] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "cacheState" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.DelegatingConnection] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Operation on the "fatalSqlExceptionThrown" shared variable in "PoolableConnection" class is not atomic [org.apache.commons.dbcp2.PoolableConnection] AT_NONATOMIC_OPERATIONS_ON_SHARED_VARIABLE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "clearStatementPoolOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolingConnection] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "maxTotal" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.SharedPoolDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultBlockWhenExhausted" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultLifo" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultMaxIdle" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultMaxTotal" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultMinIdle" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultNumTestsPerEvictionRun" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultTestOnBorrow" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultTestOnCreate" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultTestOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultTestWhileIdle" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultTransactionIsolation" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "rollbackAfterValidation" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.datasources.InstanceKeyDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "loginTimeout" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS] At DriverAdapterCPDS.java:[line 644] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "maxIdle" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS] At DriverAdapterCPDS.java:[line 664] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "maxPreparedStatements" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS] At DriverAdapterCPDS.java:[line 673] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "numTestsPerEvictionRun" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS] At DriverAdapterCPDS.java:[line 722] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "poolPreparedStatements" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS] At DriverAdapterCPDS.java:[line 757] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "autoCommitOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory-] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "cacheState" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "clearStatementPoolOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "defaultTransactionIsolation" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "autoCommitOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "fastFailValidation" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "maxOpenPreparedStatements" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "poolStatements" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "rollbackOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.PoolableConnectionFactory] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "autoCommitOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbc-p2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "cacheState" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "clearStatementPoolOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "autoCommitOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "fastFailValidation" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "logExpiredConnections" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "registerConnectionMBean" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs [ERROR] Medium: Shared primitive variable "rollbackOnReturn" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.dbcp2.BasicDataSource] AT_STALE_THREAD_WRITE_OF_PRIMITIVE. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix a potential resource leak if an SQLException occurs during an attempt to obtain an XAConnection. Thanks to Coverity Scan.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Minor optimisations to the processing of the "connectionProperties" string. Thanks to Coverity Scan.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add org.apache.commons.dbcp2.datasources.PooledConnectionManager.setPassword(char[]). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests and CPDSConnectionFactory#invalidate to accomodate changed behavior in the fix for POOL-424.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 78 to 93 #521, #537, #538. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-pool2 from 2.12.0 to 2.13.0 #474. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Port site from Doxia 1 to 2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-logging:commons-logging from 1.3.4 to 1.3.5. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.slf4j:slf4j-simple from 2.0.16 to 2.0.17 #481. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-lang3 from 3.17.0 to 3.20.0 #506. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_8c59dffb9af6280a.gif" title="Remove"/></td>
<td>Removed internal constructors and methods from the package-private class CPDSConnectionFactory; this is binary compatible. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_8c59dffb9af6280a.gif" title="Remove"/></td>
<td>Removed an internal constructor and methods from the package-private class KeyedCPDSConnectionFactory; this is binary compatible. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.13.0"></a>
<h2>Release 2.13.0 – 2024-11-23</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid object creation when invoking isDisconnectionSqlException #422. Thanks to Johno Crawford.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PoolableConnectionFactory.destroyObject() method behaves incorrectly on ABANDONED connection, issue with unhandled AbstractMethodError. DelegatingConnection.abort(Executor) should delegate to Jdbc41Bridge. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-599">DBCP-599</a>. Thanks to denixx baykin, Phil Steitz, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DelegatingConnection.setSchema(String) should delegate to Jdbc41Bridge. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix possible NullPointerException in PoolingConnection.close(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PerUserPoolDataSource.registerPool() incorrectly replacing a CPDSConnectionFactory into managers map before throwing an IllegalStateException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix PMD UnnecessaryFullyQualifiedName in AbandonedTrace. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix PMD UnnecessaryFullyQualifiedName in PoolableCallableStatement. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix PMD UnnecessaryFullyQualifiedName in PoolablePreparedStatement. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix PMD UnnecessaryFullyQualifiedName in Utils. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix PMD UnnecessaryFullyQualifiedName in LocalXAConnectionFactory. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs MC_OVERRIDABLE_METHOD_CALL_IN_READ_OBJECT in PerUserPoolDataSource. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix SpotBugs MC_OVERRIDABLE_METHOD_CALL_IN_READ_OBJECT in SharedPoolDataSource. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add support for ignoring non-fatal SQL state codes #421. Thanks to Johno Crawford, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add @FunctionalInterface to SwallowedExceptionListener. Thanks to Johno Crawford, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add missing Javadoc comments and descriptions. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add tests, raise the bar for JaCoCo checks. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 66 to 78 #360, #371, #395, #420, #426, #436, #441, #449. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-logging:commons-logging from 1.3.0 to 1.3.4 #368, #399, #423. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-lang3 from 3.14.0 to 3.17.0 #404, #412, #427. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.hamcrest:hamcrest from 2.2 to 3.0 #410. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.slf4j:slf4j-simple from 2.0.13 to 2.0.16 #413, #418. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.12.0"></a>
<h2>Release 2.12.0 – 2024-02-29</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicDataSource#setAbandonedUsageTracking has no effect. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-590">DBCP-590</a>. Thanks to Réda Housni Alaoui.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PoolingConnection.toString() causes StackOverflowError. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-596">DBCP-596</a>. Thanks to Aapo Haapanen, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PooledConnectionImpl.destroyObject(PStmtKey, PooledObject) can throw NullPointerException #312. Thanks to Gary Gregory, Rémy Maucherat.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PoolingConnection.destroyObject(PStmtKey, PooledObject) can throw NullPointerException #312. Thanks to Gary Gregory, Rémy Maucherat.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix examples in src/main/java/org/apache/commons/dbcp2/package-info.java. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-477">DBCP-477</a>. Thanks to Mubasher Usman, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add property project.build.outputTimestamp for build reproducibility. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add null guards in DelegatingDatabaseMetaData constructor #352. Thanks to Heewon Lee.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Data source bean creation failed due to mismatched return type of setter and getter for connectionInitSqls in BasicDataSource: Add BasicDataSource.setConnectionInitSqls(List). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-473">DBCP-473</a>. Thanks to Steve Cohen, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Use ReentrantLock in PoolableConnection.close, #591 Thanks to cortlepp-intershop.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-lang3 from 3.13.0 to 3.14.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-parent from 64 to 66. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.slf4j:slf4j-simple from 2.0.9 to 2.0.12 #349. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.11.0"></a>
<h2>Release 2.11.0 – 2023-10-23</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update call sites of deprecated APIs from Apache Commons Pool. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Add DataSourceMXBean.getUserName() and deprecate getUsername(). Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump h2 from 2.2.220 to 2.2.224, #308. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-parent from 60 to 64. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.slf4j:slf4j-simple from 2.0.7 to 2.0.9 #301. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-pool2 from 2.11.1 to 2.12.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump jakarta.transaction:jakarta.transaction-api from 1.3.1 to 1.3.3. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-logging:commons-logging from 1.2 to 1.3.0. Thanks to Piotr P. Karwasz.</td>
<td><a href="#team--pkarwasz">pkarwasz</a></td></tr></table></section><section><a id="a2.10.0"></a>
<h2>Release 2.10.0 – 2023-08-28</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix StackOverflowError in PoolableConnection.isDisconnectionSqlException #123. Thanks to newnewcoder, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PerUserPoolDataSourceFactory.getNewInstance(Reference) parsed defaultMaxWaitMillis as an int instead of a long. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Reimplement time tracking in AbandonedTrace with an Instant instead of a long. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Migrate away from deprecated APIs in Apache Commons Pool. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix possible NullPointerException in BasicDataSourceFactory.validatePropertyNames(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix possible NullPointerException in BasicDataSourceFactory.getObjectInstance(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Connection level JMX queries result in concurrent access to connection objects, causing errors #179. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-585">DBCP-585</a>. Thanks to Kurtcebe Eroglu, Gary Gregory, Phil Steitz.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>UserPassKey should be Serializable. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>LifetimeExceededException should extend SQLException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Replace Exception with SQLException in some method signatures (preserves binary compatibility, not source). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Don't leak Connections when PoolableConnectionFactory.makeObject() fails to create a JMX ObjectName. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Performance: No need for map lookups if we traverse map entries instead of keys. Thanks to SpotBugs, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Performance: Refactor to use a static inner class in DataSourceXAConnectionFactory. Thanks to SpotBugs, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Reuse pattern of throwing XAException instead of NullPointerException in LocalXAConnectionFactory.LocalXAResource. Thanks to SpotBugs, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>SpotBugs: An overridable method is called from constructors in PoolableCallableStatement. Thanks to SpotBugs, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>SpotBugs: An overridable method is called from constructors in PoolablePreparedStatement. Thanks to SpotBugs, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Wrong property name logged in ConnectionFactoryFactory.createConnectionFactory(BasicDataSource, Driver). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Throw SQLException instead of NullPointerException when the connection is already closed. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>CPDSConnectionFactory.makeObject() does not need to wrap and rethrow SQLException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PoolingDataSource.close() now always throws SQLException. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>[StepSecurity] ci: Harden GitHub Actions #282. Thanks to step-security-bot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixes typos, missing or misplaced characters, and grammar issues #299. Thanks to Martin Wiesner.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and use AbandonedTrace#setLastUsed(Instant). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and use Duration versions of now deprecated APIs that use ints and longs.
        Internally track durations with Duration objects instead of ints and longs.
        See the JApiCmp report for the complete list. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add PMD check to default Maven goal. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add Utils.getDisconnectionSqlCodes() and Utils.DISCONNECTION_SQL_CODES. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Make BasicDataSource.getConnectionPool() public. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add github/codeql-action. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/cache from 2.1.6 to 3.0.8 #147, #176. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/checkout from 2.3.4 to 3.0.2 #139, #143, #173. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/setup-java from 2 to 3.6.0 #229. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/upload-artifact from 3.1.0 to 3.1.1 #231. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump checkstyle from 8.44 to 9.3 #121, #130, #149, #158, #190. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.1.2 to 3.2.0 #210. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-pool2 2.10.0 to 2.11.1. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump junit-jupiter from 5.8.0-M1 to 5.9.1 #125, #136, #157, #203, #218. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.3.0 to 4.7.3.0 #140, #154, #161, #178, #192, #200, #204, #213, #234. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump spotbugs from 4.3.0 to 4.7.3 #124, #133, #151, #164, #177, #189, #214, #230. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.mockito:mockito-core from 3.11.2 to 4.11.0, #128, #138, #152, #175, #188. #193, #208, #215, #232, #235, #246, #252. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.3.0 to 3.4.1 #131, #184. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.14.0 to 3.19.0 #132, #172, #195. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump pmd from 6.44.0 to 6.52.0. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump narayana-jta from 5.12.0.Final to 5.12.7.Final #134, #156, #163, #185, #197. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump japicmp-maven-plugin from 0.15.3 to 0.17.1 #137, #166, #174, #211, #238. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump h2 from 1.4.200 to 2.2.220 #153, #183, #196, #287.
        Update SQL for migration from H2 1.4.200 to 2.0.204 where "KEY" and "VALUE" are now reserved keywords. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump jboss-logging from 3.4.2.Final to 3.4.3.Final #162. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump slf4j-simple from 1.7.30 to 1.7.36 #169. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-parent from 52 to 60 #180, #219, #254, #278. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump JaCoCo from 0.8.7 to 0.8.8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-surefire-plugin 2.22.2 to 3.0.0-M7. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump apache-rat-plugin 0.13 to 0.14. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-lang3 from 3.12 to 3.13.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.9.0"></a>
<h2>Release 2.9.0 – 2021-07-30</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse Constants.KEY_USER and Constants.KEY_PASSWORD. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse DataSourceMXBean. Thanks to Frank Gasdorf, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse DriverAdapterCPDS.{get|set}DurationBetweenEvictionRuns(), deprecate {get|set}TimeBetweenEvictionRunsMillis(long). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse DriverAdapterCPDS.{get|set}MinEvictableIdleDuration(), deprecate {get|set}MinEvictableIdleTimeMillis(int). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse CPDSConnectionFactory.setMaxConnLifetime(Duration), deprecate setMaxConnLifetimeMillis(long). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse KeyedCPDSConnectionFactory.setMaxConnLifetime(Duration), deprecate setMaxConnLifetimeMillis(long). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse KeyedCPDSConnectionFactory.setMaxConnLifetime(Duration), deprecate setMaxConnLifetimeMillis(long). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add and reuse InstanceKeyDataSource.{get|set}DefaultMaxWait(Duration), deprecate {get|set}DefaultMaxWaitMillis(long). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix test random failure on TestSynchronizationOrder.testInterposedSynchronization, #84. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-569">DBCP-569</a>. Thanks to Florent Guillaume.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>ManagedConnection must clear its cached state after transaction completes, #75. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-568">DBCP-568</a>. Thanks to Florent Guillaume.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Minor Improvements #78. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Use abort rather than close to clean up abandoned connections. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-567">DBCP-567</a>. Thanks to Phil Steitz, Gary Gregory, Phil Steitz, Romain Manni-Bucau.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Performance Enhancement: Call toArray with Zero Array Size #20. Thanks to Gary Gregory, DaGeRe.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid exposing password via JMX #38. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-562">DBCP-562</a>. Thanks to Frank Gasdorf, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Remove redundant initializers #98. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-575">DBCP-575</a>. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Simplify test assertions #100, #113. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-577">DBCP-577</a>. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DataSource implementations do not implement Wrapper interface correctly #93. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-573">DBCP-573</a>. Thanks to Réda Housni Alaoui, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Replace FindBugs with SpotBugs.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DataSourceConnectionFactory.getUserPassword() may expose internal representation by returning DataSourceConnectionFactory.userPassword.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DataSourceXAConnectionFactory.getUserPassword() may expose internal representation by returning DataSourceXAConnectionFactory.userPassword.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DriverAdapterCPDS.getPasswordCharArray() may expose internal representation by returning DriverAdapterCPDS.userPassword.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>new org.apache.commons.dbcp2.managed.DataSourceXAConnectionFactory(TransactionManager, XADataSource, String, char[], TransactionSynchronizationRegistry) may expose internal representation by storing an externally mutable object into DataSourceXAConnectionFactory.userPassword.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>org.apache.commons.dbcp2.managed.DataSourceXAConnectionFactory.setPassword(char[]) may expose internal representation by storing an externally mutable object into DataSourceXAConnectionFactory.userPassword.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>org.apache.commons.dbcp2.PStmtKey.getColumnIndexes() may expose internal representation by returning PStmtKey.columnIndexes.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>org.apache.commons.dbcp2.PStmtKey.getColumnNames() may expose internal representation by returning PStmtKey.columnNames.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Use Collections.synchronizedList() Instead Of Vector #101. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-578">DBCP-578</a>. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Simplify and inline variables #99. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-576">DBCP-576</a>. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Update PoolKey#toString() to avoid revealing a user name is here. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Internal package private UserPassKey class stores its user name as a char[] as it already does the password. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Performance of DelegatingConnection.prepareStatement(String) regressed enormously in 2.8.0 compared to 1.4.
        DelegatingConnection should also cache connection schema string to avoid calling the Connection#getSchema() for each key creation.
        DelegatingConnection should also cache connection catalog string to avoid calling the Connection#getCatalog() for each key creation. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-579">DBCP-579</a>. Thanks to Shaktisinh Jhala, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicDataSource should test for the presence of a security manager dynamically, not once on initialization. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump mockito-core from 3.5.11 to 3.11.2 #66, #72, #77, #85, #91, #105, #110, #116. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/checkout from v2.3.2 to v2.3.4 #65, #74. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/cache from v2 to v2.1.6 #90, #108. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-pool2 from 2.8.1 to 2.9.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump actions/setup-java from v1.4.2 to v2 #69. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump japicmp-maven-plugin from 0.14.3 to 0.15.2 #71, #82. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-pmd-plugin from 3.13.0 to 3.14.0 #76. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump japicmp-maven-plugin from 0.14.4 to 0.15.3, #83. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump Hamcrest 1.3 -&gt; 2.2 #70. Thanks to John Patrick.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.1.1 to 3.1.2 #88. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump junit-jupiter from 5.7.0 to 5.8.0-M1, #89, #106. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump narayana-jta from 5.10.6.Final to 5.12.0.Final #103, #111. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump maven-javadoc-plugin from 3.2.0 to 3.3.0 #107. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons.jacoco.version 0.8.6 -&gt; 0.8.7. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump jboss-logging from 3.4.1.Final to 3.4.2.Final #109. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump org.jboss:jboss-transaction-spi from 7.6.0.Final to 7.6.1.Final. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump commons-pool2 from 2.9.0 to 2.10.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump checkstyle to 8.44. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump spotbugs from 4.2.3 to 4.3.0 #117. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.2.3 to 4.3.0 #118. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.8.0"></a>
<h2>Release 2.8.0 – 2020-09-21</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Fix BasicManagedDataSource leak of connections opened after transaction is rollback-only #39. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-564">DBCP-564</a>. Thanks to Florent Guillaume.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add clearStatementPoolOnReturn #42. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-566">DBCP-566</a>. Thanks to Robert Paschek, Gary Gregory, Phil Steitz.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add start, restart methods to BasicDataSource. #50. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-559">DBCP-559</a>. Thanks to Phil Steitz.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>NPE when creating a SQLExceptionList with a null list. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-555">DBCP-555</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix DelegatingConnection readOnly and autoCommit caching mechanism #35. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-558">DBCP-558</a>. Thanks to louislatreille.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix regression introduced by unreleased code clean-up #63. Thanks to Sebastian Haas.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update to PR#36 - PrepareStatement and prepareCall methods are extracted #37. Thanks to DoiMasayuki, Alexander Norz, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not display credentials in DriverAdapterCPDS.toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not display credentials in DelegatingConnection.toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not display credentials in DriverConnectionFactory.toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not display credentials in PoolKey.toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not display credentials in UserPassKey.toString(). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Apache Commons Pool from 2.7.0 to 2.8.1, #48. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-650">DBCP-650</a>. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from H2 1.4.199 to 1.4.200. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from Mockito 3.0.0 to 3.5.11 #47, #60, #64. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from jboss-logging 3.4.0.Final to 3.4.1.Final. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from narayana-jta 5.9.5.Final to 5.10.6.Final, #61. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from junit-jupiter 5.5.1 to 5.7.0 #62. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from org.slf4j:slf4j-simple 1.7.26 to 1.7.30. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update build from com.github.siom79.japicmp:japicmp-maven-plugin 0.13.1 to 0.14.3. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update build from maven-javadoc-plugin 3.1.1 to 3.2.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update build from maven-pmd-plugin 3.12.0 to 3.13.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update org.apache.commons:commons-parent from 48 to 51. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update jacoco-maven-plugin from 0.8.4 to 0.8.6. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update maven-checkstyle-plugin from 3.0.0 to 3.1.1. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update actions/checkout from v1 to v2.3.2, #44, #51. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update actions/setup-java from v1.4.0 to v1.4.2 #58. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.7.0"></a>
<h2>Release 2.7.0 – 2019-07-31</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>ManagedDataSource#close() should declare used exceptions. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-539">DBCP-539</a>. Thanks to Jacques Le Roux.</td>
<td><a href="#team--jleroux">jleroux</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add a ConnectionFactory class name setting for BasicDataSource.createConnectionFactory() #33. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-547">DBCP-547</a>. Thanks to leechoongyon, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add missing Javadocs. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Wrong JMX base name derived in BasicDataSource#updateJmxName. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-538">DBCP-538</a>. Thanks to Ragnar Haugan, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid NPE when calling DriverAdapterCPDS.toString(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-546">DBCP-546</a>. Thanks to Sergey Chupov.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>java.util.IllegalFormatException while building a message for a SQLFeatureNotSupportedException in Jdbc41Bridge.getObject(ResultSet,String,Class). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-550">DBCP-550</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix Javadoc link in README.md #21. Thanks to LichKing-lee.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Close ObjectOutputStream before calling toByteArray() on underlying ByteArrayOutputStream #28. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-540">DBCP-540</a>. Thanks to emopers.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Upgrade to JUnit Jupiter #19. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-541">DBCP-541</a>. Thanks to Allon Murienik.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Fix tests on Java 11. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-542">DBCP-542</a>. Thanks to Zheng Feng, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Apache Commons Pool from 2.6.1 to 2.6.2. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-543">DBCP-543</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Add 'jmxName' property to web configuration parameters listing. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-529">DBCP-529</a>. Thanks to Yuri.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Apache Commons Pool from 2.6.2 to 2.7.0. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-548">DBCP-548</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Make org.apache.commons.dbcp2.AbandonedTrace.removeTrace(AbandonedTrace) null-safe. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-549">DBCP-549</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.DelegatingStatement.close() should try to close ALL of its result sets even when an exception occurs. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-551">DBCP-551</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.DelegatingConnection.passivate() should close ALL of its resources even when an exception occurs. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-552">DBCP-552</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.PoolablePreparedStatement.passivate() should close ALL of its resources even when an exception occurs. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-553">DBCP-553</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.PoolableCallableStatement.passivate() should close ALL of its resources even when an exception occurs. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-554">DBCP-554</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from org.mockito:mockito-core 2.28.2 to 3.0.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from H2 1.4.198 to 1.4.199. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from com.h2database:h2 1.4.197 to 1.4.199. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from org.jboss.narayana.jta:narayana-jta 5.9.2.Final to 5.9.5.Final. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from org.jboss.logging:jboss-logging 3.3.2.Final to 3.4.0.Final. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from org.mockito:mockito-core 2.24.0 to 2.28.2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update tests from org.mockito:mockito-core 2.28.2 to 3.0.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.6.0"></a>
<h2>Release 2.6.0 – 2019-02-14</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Allow for manual connection eviction. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-534">DBCP-534</a>. Thanks to Peter Wicks.</td>
<td><a href="#team--chtompki">chtompki</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Allow DBCP to register with a TransactionSynchronizationRegistry for XA cases. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-514">DBCP-514</a>. Thanks to Tom Jenkinson, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Make defensive copies of char[] passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-517">DBCP-517</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not try to register synchronization when the transaction is no longer active. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-515">DBCP-515</a>. Thanks to Tom Jenkinson, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Do not double returnObject back to the pool if there is a transaction context with a shared connection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-516">DBCP-516</a>. Thanks to Tom Jenkinson, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Allow DBCP to work with old Java 6/JDBC drivers without throwing AbstractMethodError. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-518">DBCP-518</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add some toString() methods for debugging (never printing passwords.). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-519">DBCP-519</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>BasicManagedDataSource needs to pass the TSR with creating DataSourceXAConnectionFactory. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-520">DBCP-520</a>. Thanks to Zheng Feng.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add getters to some classes. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-527">DBCP-527</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>org.apache.commons.dbcp2.DriverManagerConnectionFactory should use a char[] instead of a String to store passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-528">DBCP-528</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Apache Commons Pool from 2.6.0 to 2.6.1. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-537">DBCP-537</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.5.0"></a>
<h2>Release 2.5.0 – 2018-07-15</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Java requirement from version 7 to 8. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-505">DBCP-505</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Support JDBC 4.2. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-506">DBCP-506</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Support default schema in configuration. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-479">DBCP-479</a>. Thanks to Guillaume Husta, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Examines 'SQLException's thrown by underlying connections or statements for fatal (disconnection) errors. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-427">DBCP-427</a>. Thanks to Vladimir Konkov, Phil Steitz, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Change default for fail-fast connections from false to true. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-507">DBCP-507</a>. Thanks to Vladimir Konkov, Phil Steitz, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Prepared statement keys should take a Connection's schema into account. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-508">DBCP-508</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Increase test coverage. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-504">DBCP-504</a>. Thanks to Bruno P. Kinoshita.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Apache Commons Pool from 2.5.0 to 2.6.0. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-510">DBCP-510</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid exceptions when closing a connection in mutli-threaded use case. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-512">DBCP-512</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.4.0"></a>
<h2>Release 2.4.0 – 2018-06-12</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Connection leak during XATransaction in high load. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-484">DBCP-484</a>. Thanks to Emanuel Freitas.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Drop Ant build. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-492">DBCP-492</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Ensure DBCP ConnectionListener can deal with transaction managers which invoke rollback in a separate thread. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-491">DBCP-491</a>. Thanks to Zheng Feng, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.PStmtKey should make copies of given arrays in constructors. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-494">DBCP-494</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Remove duplicate code in org.apache.commons.dbcp2.cpdsadapter.PStmtKeyCPDS. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-495">DBCP-495</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Add support for pooling CallableStatements to the org.apache.commons.dbcp2.cpdsadapter package. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-496">DBCP-496</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Deprecate use of PStmtKeyCPDS in favor of PStmtKey. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-497">DBCP-497</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.DataSourceConnectionFactory should use a char[] instead of a String to store passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-498">DBCP-498</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.managed.DataSourceXAConnectionFactory should use a char[] instead of a String to store passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-499">DBCP-499</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS should use a char[] instead of a String to store passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-500">DBCP-500</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.datasources.CPDSConnectionFactory should use a char[] instead of a String to store passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-501">DBCP-501</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.datasources internals should use a char[] instead of a String to store passwords. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-502">DBCP-502</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>org.apache.commons.dbcp2.datasources.InstanceKeyDataSourceFactory.closeAll() does not close all. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-503">DBCP-503</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.3.0"></a>
<h2>Release 2.3.0 – 2018-05-12</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>AbandonedTrace.getTrace() contains race condition. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-476">DBCP-476</a>. Thanks to Gary Evesson, Richard Cordova.</td>
<td><a href="#team--pschumacher">pschumacher</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid javax.management.InstanceNotFoundException on shutdown when a bean is not registered. Closes #9. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-482">DBCP-482</a>. Thanks to Dennis Lloyd, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Make constant public: org.apache.commons.dbcp2.PoolingDriver.URL_PREFIX. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-483">DBCP-483</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>DriverAdapterCPDS.setUser(), setPassword(), and getPooledConnection() with null arguments throw NullPointerExceptions when connection properties are set. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-486">DBCP-486</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Add API org.apache.commons.dbcp2.datasources.PerUserPoolDataSource.clear(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-487">DBCP-487</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>NPE for org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS.setConnectionProperties(null). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-488">DBCP-488</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>The method org.apache.commons.dbcp2.PoolingDriver.getConnectionPool(String) does not tell you which pool name is not registered when it throws an exception. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-490">DBCP-490</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a2.2.0"></a>
<h2>Release 2.2.0 – 2017-12-27</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Update Apache Commons Pool from 2.4.2 to 2.5.0. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-481">DBCP-481</a>. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>OSGi declarations contain multiple import headers for javax.transaction. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-454">DBCP-454</a>. Thanks to Philipp Marx, Matt Sicker.</td>
<td><a href="#team--mattsicker">mattsicker</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Wrong parameter name in site documentation for BasicDataSource Configuration Parameters. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-478">DBCP-478</a>. Thanks to nicola mele.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Add jmxName to properties set by BasicDataSourceFactory.  This
        enables container-managed pools created from JNDI Resource
        definitions to enable JMX by supplying a valid root JMX name. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-452">DBCP-452</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>NullPointerException thrown when calling ManagedConnection.isClosed(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-446">DBCP-446</a>. Thanks to Gary Gregory, feng yang, Euclides M, Phil Steitz.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>InvalidateConnection can result in closed connection returned by getConnection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-444">DBCP-444</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Complete the fix for DBCP-418, enabling PoolableConnection class to load in environments
        (such as GAE) where the JMX ManagementFactory is not available. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-449">DBCP-449</a>. Thanks to Grzegorz D..</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add constructor DriverManagerConnectionFactory(String). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-451">DBCP-451</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Ensure that the cacheState setting is used when statement pooling is
        disabled. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-455">DBCP-455</a>. Thanks to Kyohei Nakamura.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Ensure that setSoftMinEvictableIdleTimeMillis is used when working with
        BasicDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-453">DBCP-453</a>. Thanks to Philipp Marx.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct the name of the configuration attribute
        softMinEvictableIdleTimeMillis. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-456">DBCP-456</a>. Thanks to Kyohei Nakamura.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid potential infinite loops when checking if an SQLException is fatal
        for a connection or not. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-472">DBCP-472</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Expand the fail-fast for fatal connection errors feature to include
        managed connections. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-468">DBCP-468</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct a typo in the method name
        PoolableConnectionFactory#setMaxOpenPreparedStatements. The old method
        remains but is deprecated so not to break clients currently using the
        incorrect name. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-463">DBCP-463</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Refactoring to prepare for a future patch to enable pooling of all
         prepared and callable statements in PoolingConnection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-462">DBCP-462</a>. Thanks to Keiichi Fujino.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Ensure that a thread's interrupt status is visible to the caller if the
         thread is interrupted during a call to
         PoolingDataSource.getConnection(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-459">DBCP-459</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Make it simpler to extend BasicDataSource to allow sub-classes to
         provide custom GenericObjectPool implementations. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-458">DBCP-458</a>. Thanks to Adrian Tarau.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>When using a BasicDataSource, pass changes related to the handling of
         abandoned connections to the underlying pool so that the pool
         configuration may be updated dynamically. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-457">DBCP-457</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Enable pooling of all prepared and callable statements
         inPoolingConnection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-474">DBCP-474</a>. Thanks to Keiichi Fujino.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a2.1.1"></a>
<h2>Release 2.1.1 – 6 Aug 2015</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Updated pool version to 2.4.2.  The fix for POOL-300 may cause DBCP
        users to see more reports of abandoned connections (if removal and logging
        are configured).  Prior to the fix for POOL-300, the PrintWriter used to log
        abandoned connection stack traces was not being flushed on each log event.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Added BasicDataSource abandonedUsageTracking property missing from BasicDataSourceFactory. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-441">DBCP-441</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>SharedPoolDataSource getConnection fails when testOnBorrow is set with
        a null validation query. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-442">DBCP-442</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Nested connections in a transaction (local) throws null pointer. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-438">DBCP-438</a>. Thanks to Raihan Kibria.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicDataSource does not set disconnectionSql properties on its PoolableConnectionFactory. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-437">DBCP-437</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr></table></section><section><a id="a2.1"></a>
<h2>Release 2.1 – 23 Feb 2015</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>InstanceKeyDataSource discards native SQLException when given password does not match
        password used to create the connection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-420">DBCP-420</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update Apache Commons Logging to 1.2 from 1.1.3. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-422">DBCP-422</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct some Javadoc references to Apache Commons Pool 2 classes that
        have changed names since Pool 1.x.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Do not ignore the configured custom eviction policy when creating a
        BasicDataSource.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Added invalidateConnection method to BasicDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-426">DBCP-426</a>. Thanks to Kasper Sørensen.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Unsuccessful Connection enlistment in XA Transaction ignored by TransactionContext. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-428">DBCP-428</a>. Thanks to Vladimir Konkov.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Made expired connection logging configurable in BasicDataSource.  Setting
        logExpiredConnections to false suppresses expired connection log messages. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-424">DBCP-424</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Made Datasources implement AutoCloseable. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-423">DBCP-423</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Added fastFailValidation property to PoolableConnection, configurable in
        BasicDataSource.  When set to true, connections that have previously thrown
        fatal disconnection errors will fail validation immediately (no driver calls). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-427">DBCP-427</a>. Thanks to Vladimir Konkov.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Changed BasicDataSource createDataSource method to ensure that initialization
        completes before clients get reference to newly created instances. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-432">DBCP-432</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed connection leak when SQLException is thrown while enlisting an XA
        transaction. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-433">DBCP-433</a>. Thanks to Vladimir Konkov.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Setting jmxName to null should suppress JMX registration of connection
        and statement pools. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-434">DBCP-434</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Eliminated synchronization in BasicDataSource getNumActive, getNumIdle methods.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added property name verification to BasicDataSourceFactory. References including
        obsolete or unrecognized properties now generate log messages. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-435">DBCP-435</a>. Thanks to Denixx Baykin.</td>
<td>-</td></tr></table></section><section><a id="a2.0.1"></a>
<h2>Release 2.0.1 – 24 May 2014</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Small performance improvements when returning connections to the pool.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed DelegatingStatement close to ensure closed statements do not retain references
        to pooled prepared statements. Due to finalization code added in 2.0, this was causing
        pooled prepared statements to be closed by GC while in use by clients. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-414">DBCP-414</a>. Thanks to Pasi Eronen.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added check in PoolingDataSource constructor to ensure that the connection factory
        and pool are properly linked. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-412">DBCP-412</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed connection leak when managed connections are closed during transactions. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-417">DBCP-417</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Enable PoolableConnection class to load without JMX. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-418">DBCP-418</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr></table></section><section><a id="a2.0"></a>
<h2>Release 2.0 – 3 March 2014</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicManagedDataSource - unregister from JMX on close(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-411">DBCP-411</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Log validation failures of poolable connections. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-154">DBCP-154</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DelegatingStatement.close() fails with NPE if statement is null. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-403">DBCP-403</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>CPDSConnectionFactory.validateObject(Object) ignores Throwable. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-322">DBCP-322</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Provide a new option (cacheState) to cache current values of autoCommit
        and readOnly so database queries are not required for every call to the
        associated getters. This option is enabled by default.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Removed unnecessary synchronisation in BasicDataSource#createDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-300">DBCP-300</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>The Java package name has been changed from org.apache.commons.dbcp to
        org.apache.commons.dbcp2.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Update to Commons Pool 2 (based on java.util.concurrent) to provide
        pooling functionality.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Updated source code for Java 1.6 (added @Override &amp; @Deprecated
        annotations).</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Removed JOCL support.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Remove deprecated SQLNestedException. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-143">DBCP-143</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix threading issues with accessToUnderlyingConnectionAllowed attribute
        of PoolingDriver which is used to support unit testing. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-384">DBCP-384</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>BasicDataSource instances are now exposed via JMX. All the configuration
        properties are available as is the connection pool and the statement
        pools (if statement pooling is enabled). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-292">DBCP-292</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix thread safety issues in the SharedPoolDataSource and the
        PerUserPoolDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-376">DBCP-376</a>. Thanks to Dave Oxley.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Allow accessToUnderlyingConnectionAllowed to be configured when
        configuration takes place via JNDI in a JavaEE container. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-382">DBCP-382</a>. Thanks to Stefan Rempfer.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix threading issue when using multiple instances of the
        SharedPoolDataSource concurrently. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-369">DBCP-369</a>. Thanks to Michael Pradel.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Ensure that the close state of a pooled connection and the underlying
        connection is consistent when the underlying connection is closed as a
        result of an error condition. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-391">DBCP-391</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Make all mutable fields private. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-404">DBCP-404</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Return BasicDataSource rather than DataSource from
        BasicDataSourceFactory so a cast is not required to use BasicDataSource
        specific methods. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-364">DBCP-364</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>The equals() implementations of the DelegatingXxx classes are now
        symmetric. There are some important API changes underlying this fix.
        Firstly, two DelegatingXxx instances are no longer considered equal if
        they have the same innermost delegate. Secondly, a DelegatingXxx
        instance is not considered equal to its innermost delegate. The
        getInnermostDelegateInternal() method has been made public (but remains
        part of the internal API) to allow classes extending this implementation
        to access the innermost delegate when required. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-358">DBCP-358</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Expose the new Pool 2 property evictionPolicyClassName to enable more
        sophisticated eviction strategies to be used. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-368">DBCP-368</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add support for pooling PreparedStatements that use auto-generated keys. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-406">DBCP-406</a>. Thanks to Steeve Beroard.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Enable JDBC resources that are no longer referenced by client code to be
        eligible for garbage collection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-180">DBCP-180</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Enable DBCP to work with a SecurityManager such that only DBCP needs to
        be granted the necessary permissions to communicate with the database. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-177">DBCP-177</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct path to Javadoc overview in build.xml. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-410">DBCP-410</a>. Thanks to Andreas Sturmlechner.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>The default values for readOnly, autoCommit and transactionIsolation are
        now taken from the JDBC driver. No calls to setReadOnly(),
        setAutoCommit() or setTransactionIsolation() will be made for a newly
        borrowed connection unless a default is explicitly configured and the
        connection is currently using a different setting. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-234">DBCP-234</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Register pooled connections with JMX so that they may be forcibly closed
        via JMX if required. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-219">DBCP-219</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Modify SharedPoolDataSource and PerUserPoolDataSource to expose all of
        the configuration properties of the underlying connection pool(s). This
        represents a significant refactoring of these classes and a number of
        property names have changed as a result. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-373">DBCP-373</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Provide an option to control if autoCommit is always set to true when a
        connection is returned to the connection pool. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-351">DBCP-351</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Provide an option to control if rollback is called when a connection is
        returned to the poll with autoCommit disabled. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-399">DBCP-399</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Provide an option to set the default query timeout. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-340">DBCP-340</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Connection.isValid() should not throw an SQLException if the connection
        is closed.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Use Connection.isValid() to validate connections unless a validation
        query is explicitly configured. Note that this means it is no longer
        necessary for a validation query to be specified in order for validation
        to take place. When testing with Oracle, this resulted in database
        validation being approximately 7 times faster. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-357">DBCP-357</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add support for validation testing database connections on creation. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-249">DBCP-249</a>.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.5.1"></a>
<h2>Release 1.5.1 – not yet released</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct the documentation for the maxOpenPreparedStatements parameter
        and review the use of the phrase non-positive throughout the
        documentation and javadoc, replacing it with negative where that is the
        correct definition to use. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-400">DBCP-400</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid multiple calls to Connection.getAutoCommit() in
        PoolableConnectionFactory.passivateObject() as it could be an expensive
        call. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-405">DBCP-405</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Use one line per statement for methods with multiple statements rather
        than using a single line. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-392">DBCP-392</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Expose all of the AbandonedConfig properties through a BasicDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-396">DBCP-396</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct implementation of DelegatingConnection.isWrapperFor() so it
        works correctly with older JDBC drivers. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-380">DBCP-380</a>. Thanks to Balazs Zsoldos.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correct implementation of DelegatingStatement.isWrapperFor(). Also fix
        DelegatingDatabaseMetaData.isWrapperFor() and
        DelegatingResultSet.isWrapperFor() that had the same problem. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-347">DBCP-347</a>. Thanks to Robert Poskrobek.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>LocalXAConnectionFactory does not properly check if Xid is equal to
        currentXid when resuming which may result in an XAException. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-341">DBCP-341</a>. Thanks to Ioannis Canellos.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Ensure that the XAConnection is closed when the associated Connection is
        closed. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-355">DBCP-355</a>. Thanks to Florent Guillaume.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Clarify Jaavdoc for isClosed() method of PoolableConnection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-398">DBCP-398</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Avoid NullPointerException and throw an XAException if an attempt is
        made to commit the current transaction for a connection when no
        transaction has been started. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-383">DBCP-383</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Using batchUpdate() should not invalidate the PreparedStatement when it
        is returned to the pool. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-372">DBCP-372</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Improve documentation for JNDI example using BasicDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-309">DBCP-309</a>.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.4.1"></a>
<h2>Release 1.4.1 – not yet released</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Exposed GenericObjectPool's softMinEvictableIdleTimeMillis property for
        configuration and use by BasicDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-334">DBCP-334</a>. Thanks to Alberto Mozzone.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Made equals reflexive in DelegatingStatement (and subclasses), DelegatingMetaData,
        DelegatingResultSet and PoolingDriver#PoolGuardConnectionWrapper. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-337">DBCP-337</a>. Thanks to Rob Gansevles.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified createDataSource method in BasicDataSource to ensure that GenericObjectPool
        Evictor tasks are not started and orphaned when BasicDataSource encounters errors on
        initialization.  Prior to this fix, when minIdle and timeBetweenEvictionRunsMillis
        are both positive, Evictors orphaned by failed initialization can continue to
        generate database connection requests.  This issue is duplicated by DBCP-339
        and DBCP-93. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-342">DBCP-342</a>. Thanks to Byungchol Kim.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Changed DelegatingDatabaseMetaData to no longer add itself to the AbandonedTrace
        of its parent connection.  This was causing excessive memory consumption and was
        not necessary, as resultsets created by DelegatingDatabaseMetaData instances are
        attached to the parent connection's trace on creation.  Also fixes DBCP-352. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-330">DBCP-330</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified execute methods of Statement objects to ensure that whenever
        a statement is used, the lastUsed property of its parent connection is
        updated. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-343">DBCP-343</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Correctly implemented the option to configure the class loader used to load
        the JDBC driver. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-333">DBCP-333</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>LIFO configuration option has been added to BasicDataSource.  When set
        to true (the default), the pool acts as a LIFO queue; setting to false
        causes connections to enter and exit to pool in FIFO order. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-346">DBCP-346</a>. Thanks to Ken Tatsushita.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Test transitive dependencies brought in by geronimo-transaction created
        version conflicts (commons logging and junit).  These have been explicitly
        excluded in the POM. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-344">DBCP-344</a>. Thanks to Jeremy Whiting.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicDataSourceFactory incorrectly used "initConnectSqls" in versions
        1.3 and 1.4 of DBCP as the property name for connectionInitSqls.
        Online docs for 1.3/1/4 have been updated to reflect this inconsistency.
        The BasicDataSourceFactory property name has been changed to "connectInitSqls"
        to match the online docs and the BasicDataSource property name. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-348">DBCP-348</a>. Thanks to Eiji Takahashi.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr></table></section><section><a id="a1.4"></a>
<h2>Release 1.4 – 2010-02-14</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Eliminated poolKeys cache from PerUserPoolDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-320">DBCP-320</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Eliminated userKeys LRUMap cache from SharedPoolDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-321">DBCP-321</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Made private fields final where possible. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-319">DBCP-319</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PerUserPoolDataSource.getPooledConnectionAndInfo multi-threading bug. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-318">DBCP-318</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Remove throws clause from method that does not throw an exception. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-315">DBCP-315</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Remove code that catches and ignores Exceptions when calling
        PooledConnection.removeConnectionEventListener(ConnectionEventListener)
        as the method does not throw any Exceptions. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-313">DBCP-313</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Remove impossible null check. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-316">DBCP-316</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Renamed variables with duplicate names in different scopes. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-314">DBCP-314</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Clarified javadoc for BasicDataSource close() method. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-312">DBCP-312</a>. Thanks to Glen Mazza.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Made PoolingConnection pool CallableStatements. When BasicDataSource's
        poolPreparedStatements property is true, CallableStatements are now
        pooled along with PreparedStatements. The maxOpenPreparedStatements
        property limits the combined number of Callable and Prepared statements
        that can be in use at a given time. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-204">DBCP-204</a>. Thanks to Wei Chen.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Use an API specific exception for logging abandoned objects to make
        scanning the logs for these exceptions simpler and to provide a better
        message that includes the creation time of the abandoned object. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-305">DBCP-305</a>. Thanks to Christopher Schultz.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Ensure Statement.getGeneratedKeys() works correctly with the CPDS
        adapter. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-303">DBCP-303</a>. Thanks to Dave Oxley.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Removed incorrectly advertised ClassNotFoundException from
        JOCLContentHandler.ConstructorDetails.createObject(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-302">DBCP-302</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Make the class loader used to load the JDBC driver configurable for the
        BasicDatasource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-203">DBCP-203</a>. Thanks to Mark Grand.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Handle user password changes for InstanceKeyDataSources. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-8">DBCP-8</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Made XADataSource configurable in BasicManagedDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-289">DBCP-289</a>. Thanks to Marc Kannegießer.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Added PoolableManagedConnection and PoolableManagedConnectionFactory so that
        pooled managed connections can unregister themselves from transaction registries,
        avoiding resource leaks. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-294">DBCP-294</a>. Thanks to Philippe Mouawad.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added connectionProperties property to DriverAdapterCPDS. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-276">DBCP-276</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Added a validationQueryTimeout configuration parameter to BasicDataSource
        allowing the user to specify a timeout value (in seconds) for connection
        validation queries. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-226">DBCP-226</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Added a connectionInitSqls configuration parameter to BasicDataSource
        allowing the user to specify a collection of SQL statements to execute
        one time when a physical database connection is first opened. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-175">DBCP-175</a>. Thanks to Jiri Melichna and Jerome Lacoste.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>PoolableConnectionFactory.makeObject() is no longer synchronized. This
        provides improved response times when load spikes at the cost of a
        faster rise in database server load. This change was made as a partial
        fix for DBCP-212.  The synchronization changes in Commons Pool 1.5 complete
        the fix for this issue. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-212">DBCP-212</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Reverted DelegatingConnection close to 1.2.2 version to ensure
        open statements are closed before the underlying connection is closed. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-242">DBCP-242</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Refactor DelegatingConnection and ManagedConnection enable overridden
        equals() and hashcode() to work correctly. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-235">DBCP-235</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Add a DelegatingDatabaseMetaData to track ResultSets returned from
        DatabaseMetaData objects. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-265">DBCP-265</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified BasicDataSourceFactory to complete initialization of the pool
        by creating initialSize connections rather than leaving this to lazy
        initialization when the pool is used. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-215">DBCP-215</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Eliminated masked _stmt field in descendents of DelegatingStatement. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-253">DBCP-253</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified DBCP sources to support compilation under JDK 1.4-1.6
        using Ant flags to do conditional compilation. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-191">DBCP-191</a>. Thanks to Michael Heuer and J. David Beutel.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Added a static initializer to BasicDatasource that calls
        DriverManager.getDrivers() to force initialization before we ever do
        anything that might use Class.forName() to load (and register) a JDBC
        driver. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-272">DBCP-272</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Eliminated direct System.out calls in AbandonedTrace. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-4">DBCP-4</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified DelegatingStatement close to clear open batches. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-264">DBCP-264</a>.</td>
<td><a href="#team--niallp">niallp</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Eliminated unused private "parent" field in AbandonedTrace. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-255">DBCP-255</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed errors handling boolean-valued Reference properties in
        InstanceKeyObjectFactory, DriverAdapterCPDS that were causing
        testOnBorrow and poolPreparedStatements properties to be incorrectly
        set when creating objects from javax.naming.Reference instances. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-273">DBCP-273</a>. Thanks to Mark Lin.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Made private instance fields of AbandonedTrace volatile (parent,
        createdBy, lastUsed, createdTime) or final (trace). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-271">DBCP-271</a>. Thanks to Sebastian Bazley.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Narrowed synchronization in AbandonedTrace to resolve an Evictor deadlock. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-270">DBCP-270</a>. Thanks to Filip Hanik.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Corrected Javadoc to state that getLoginTimeout and setLoginTimeout are
        NOT supported by BasicDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-218">DBCP-218</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added Maven 2 pom.xml. Removed a block of code from TestJOCLed that set
        the Xerces parser manually. This was to support early JDKs. The 1.3
        version of DBCP requires JDK 1.4+. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-211">DBCP-211</a>.</td>
<td><a href="#team--bayard">bayard</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Added support for pooling managed connections. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-228">DBCP-228</a>. Thanks to Dain Sundstrom.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Added BasicManagedDataSource, extending BasicDataSource.
        Also improved extensibility of BasicDataSource by encapsulating
        methods to create object pool, connection factory and datasource
        instance previously embedded in createDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-230">DBCP-230</a>. Thanks to Dain Sundstrom.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Changed behavior to allow Connection, Statement, PreparedStatement,
        CallableStatement and ResultSet to be closed multiple times. The first
        time close is called the resource is closed and any subsequent calls
        have no effect. This behavior is required as per the Javadocs for these
        classes. Also added tests for closing all types multiple times and
        updated any tests that incorrectly assert that a resource can not be
        closed more then once.  Fixes DBCP-3, DBCP-5, DBCP-23 and DBCP-134. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-233">DBCP-233</a>. Thanks to Dain Sundstrom.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Modified PoolingDataSource, PoolingDriver and DelegatingStatement to
        assure that all returned Statements, PreparedStatements,
        CallableStatements and ResultSets are wrapped with a delegating object,
        which already properly handle the back pointers for Connection and
        Statement.  Also added tests to assure that the *same* object used
        to create the statement or result set is returned  from either
        getConnection() or getStatement(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-11">DBCP-11</a>. Thanks to Dain Sundstrom.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>SQLNestedException has been deprecated and will be replaced in DBCP 2.0 with
        SQLException and standard Java exception chaining. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-143">DBCP-143</a>.</td>
<td><a href="#team--dain">dain</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicDataSource.close() now permanently marks the data source as closed,
        and no new connections can be obtained from the data source. At close all
        idle connections are destroyed and the method returns.  As the remaining
        active connections are closed, they are destroyed. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-221">DBCP-221</a>.</td>
<td><a href="#team--dain">dain</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Eliminated potential sources of NullPointerExceptions in
        PoolingConnection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-241">DBCP-241</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Improved error recovery and listener cleanup in
        KeyedCPDSConnectionFactory. Substituted calls to destroyObject with
         _pool.invalidateObject on error to ensure pool active count is
        decremented on error events. Ensured that events from closed or invalid
        connections are ignored and listeners are cleaned up. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-216">DBCP-216</a>. Thanks to Marcos Sanz.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed error in SharedPoolDataSource causing incorrect passwords to be
        stored under certain conditions. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-245">DBCP-245</a>. Thanks to Michael Drechsel.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Added exception handler to ensure that PooledConnections are not
        orphaned when an exception occurs in setUpDefaults or clearWarnings in
        InstanceKeyDataSource.getConnection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-237">DBCP-237</a>. Thanks to Oliver Matz.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Made getPool synchronized in PoolableConnectionFactory.
        Fixes inconsistent synchronization accessing _pool. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-252">DBCP-252</a>. Thanks to FindBugs.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed inconsistent synchronization on _rollbackAfterValidation,
        _validationQuery and _pool in CPDSConnectionFactory and
        KeyedCPDSConnectionFactory by making the first two volatile and making
        both getter and setter for _pool synchronized. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-252">DBCP-252</a>. Thanks to FindBugs.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr></table></section><section><a id="a1.3"></a>
<h2>Release 1.3 – 2010-02-14</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>See &lt;a href="changes.html#a1.4"&gt;DBCP 1.4 Changes &lt;/a&gt; for details. Version
        1.3 is identical to 1.4, other than JDBC 4 methods being filtered out of the DBCP 1.3 sources. Changes
        Since 1.2.2 are the same for 1.3 and 1.4.</td>
<td>-</td></tr></table></section><section><a id="a1.2.2"></a>
<h2>Release 1.2.2 – 2007-04-04</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Add a &lt;i&gt;JNDI How To&lt;/i&gt; to the User Guide.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>DriverManagerConnectionFactory: blank user name and password handling. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-108">DBCP-108</a>. Thanks to Maxwell Grender-Jones.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Broken behaviour for BasicDataSource.setMaxActive(0). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-113">DBCP-113</a>. Thanks to Rohan Lenard.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>BasicDataSource does not work with getConnection(String, String). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-36">DBCP-36</a>. Thanks to Jonathan Whitall.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Enhancements to prepared statement in DriverAdapterCPDS. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-164">DBCP-164</a>. Thanks to Todd Carmichael.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Better messages and docs for LoginTimeout UnsupportedOperationException. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-186">DBCP-186</a>. Thanks to Ralf Hauser.</td>
<td><a href="#team--yoavs">yoavs</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Error in JOCL snippet in org.apache.commons.dbcp package javadoc. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-50">DBCP-50</a>. Thanks to Nicky Nicolson.</td>
<td><a href="#team--yoavs">yoavs</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added toString() methods to DelegatingPreparedStatement and DelegatingStatement. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-165">DBCP-165</a>. Thanks to QM.</td>
<td><a href="#team--yoavs">yoavs</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Changes to make DBCP compile on JDK 1.5 by adding source="1.4" to compiler
        arguments (there are compiler errors in JDK 5.0 without this source switch
        that cannot be fixed without JDK 5.0-specific syntax).</td>
<td><a href="#team--yoavs">yoavs</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Per-user pooling with Oracle driver and default isolation settings. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-20">DBCP-20</a>. Thanks to Chris Nappin.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Error in JOCL document in javadoc. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-9">DBCP-9</a>. Thanks to Adrian Baker.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added toString() method to DelegatingConnection.</td>
<td><a href="#team--sullis">sullis</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Add DriverManager.invalidateConnection(). Fixes <a href="https://issues.apache.org/jira/browse/DBCP-181">DBCP-181</a>. Thanks to Meikel Bisping.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Improved Exception nesting in ConnectionPool. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-184">DBCP-184</a>. Thanks to Meikel Bisping.</td>
<td><a href="#team--dirkv">dirkv</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fix broken website links for examples. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-144">DBCP-144</a>. Thanks to Sebb.</td>
<td><a href="#team--dennisl">dennisl</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified PoolableConnection close method to invalidate instance
        when invoked on an already closed connection. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-28">DBCP-28</a>. Thanks to Huw Lewis, James Ring.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Inserted null checks to avoid NPE in close operations. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-81">DBCP-81</a>.</td>
<td><a href="#team--joehni">joehni</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Changed getReference method in InstanceKeyDataSource to return a
        concrete factory and added implementations of getReference in concrete
        subclasses. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-105">DBCP-105</a>. Thanks to Sandy McArthur, Thomas Fischer.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Inserted null check in close method of SharedPoolDataSource to avoid
        NPE when invoked on non-initialized pool. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-39">DBCP-39</a>. Thanks to Jindrich Vimr.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Document fact that true values for testOnBorrow, testOnReturn, testWhileIdle
        only have effect when validationQuery is set to a non-null string. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-71">DBCP-71</a>. Thanks to Douglas Squirrel.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Modified activateObject in PoolableConnection to test connection
        properties before resetting to defaults. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-102">DBCP-102</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Corrected maxActive documentation in configuration.html. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-188">DBCP-188</a>.</td>
<td><a href="#team--sandymac">sandymac</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Upgraded dependency to Pool 1.3.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added connection info to SQLException messages when closed connections
        (resp stmts) are accessed in DelegatingConnection, DelegatingStatement. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-187">DBCP-187</a>. Thanks to Ralf Hauser.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Fixed errors in pool parameter documentation and made
        0 value for _maxPreparedStatements in DriverAdapterCPDS behave
        like a negative value, to be consistent with documentation
        and pool behavior. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-41">DBCP-41</a>. Thanks to Anton Tagunov.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Made userKeys an instance variable (i.e., not static)
        in SharedPoolDataSource. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-100">DBCP-100</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Changed implementation of equals in
        PoolingDataSource.PoolGuardConnectionWrapper
        to ensure it is reflexive, even when wrapped connections are not
        DelegatingConnections. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-198">DBCP-198</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Added rollbackAfterValidation property and code to issue a rollback on a
        connection after validation when this property is set to true to eliminate
        Oracle driver exceptions. Default property value is false. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-116">DBCP-116</a>. Thanks to Thomas Fischer.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>Removed dependency on Commons Collections by adding collections
        2.1 sources for LRUMap and SequencedHashMap with package scope to
        datasources package. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-68">DBCP-68</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>Removed synchronization from prepareStatement methods in
        PoolingConnection. Synchronization in these methods was causing
        deadlocks. No resources other than the prepared statement pool are
        accessed by these methods, and the pool methods are synchronized.
        Also fixes DBCP-202. Fixes <a href="https://issues.apache.org/jira/browse/DBCP-65">DBCP-65</a>.</td>
<td><a href="#team--psteitz">psteitz</a></td></tr></table></section><section><a id="a1.2.1"></a>
<h2>Release 1.2.1 – 2004-06-12</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea91edf4c22537a3.gif" title="Fix"/></td>
<td>See &lt;a href="release-notes-1.2.1.html"&gt;DBCP 1.2.1 Release Notes&lt;/a&gt; for details.</td>
<td>-</td></tr></table></section><section><a id="a1.2"></a>
<h2>Release 1.2 – 2004-06-07</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>See &lt;a href="release-notes-1.2.html"&gt;DBCP 1.2 Release Notes&lt;/a&gt; for details.</td>
<td>-</td></tr></table></section><section><a id="a1.1"></a>
<h2>Release 1.1 – 2003-10-20</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_a431d677f589f898.gif" title="Update"/></td>
<td>See &lt;a href="release-notes-1.1.html"&gt;DBCP 1.1 Release Notes&lt;/a&gt; for details.</td>
<td>-</td></tr></table></section><section><a id="a1.0"></a>
<h2>Release 1.0 – 2002-08-12</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_1fd29044ed1ad4e3.gif" title="Add"/></td>
<td>Initial Release</td>
<td>-</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="issue-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/issue-management.html -->

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
<pre><a href="https://issues.apache.org/jira/browse/DBCP">https://issues.apache.org/jira/browse/DBCP</a></pre></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/dependency-info.html -->

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
  &lt;groupId&gt;org.apache.commons&lt;/groupId&gt;
  &lt;artifactId&gt;commons-dbcp2&lt;/artifactId&gt;
  &lt;version&gt;2.14.0&lt;/version&gt;
&lt;/dependency&gt;</pre></section><section><a id="Apache_Ivy"></a>
<h2>Apache Ivy</h2>
<pre>&lt;dependency org="org.apache.commons" name="commons-dbcp2" rev="2.14.0"&gt;
  &lt;artifact name="commons-dbcp2" type="jar" /&gt;
&lt;/dependency&gt;</pre></section><section><a id="Groovy_Grape"></a>
<h2>Groovy Grape</h2>
<pre>@Grapes(
@Grab(group='org.apache.commons', module='commons-dbcp2', version='2.14.0')
)</pre></section><section><a id="Gradle.2FGrails"></a>
<h2>Gradle/Grails</h2>
<pre>implementation 'org.apache.commons:commons-dbcp2:2.14.0'</pre></section><section><a id="Scala_SBT"></a>
<h2>Scala SBT</h2>
<pre>libraryDependencies += "org.apache.commons" % "commons-dbcp2" % "2.14.0"</pre></section><section><a id="Leiningen"></a>
<h2>Leiningen</h2>
<pre>[org.apache.commons/commons-dbcp2 "2.14.0"]</pre></section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/scm.html -->

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
<pre><a href="https://gitbox.apache.org/repos/asf?p=commons-dbcp.git">https://gitbox.apache.org/repos/asf?p=commons-dbcp.git</a></pre></section><section><a id="Anonymous_Access"></a>
<h1>Anonymous Access</h1>
<p>The source can be checked out anonymously from Git with this command (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>):</p>
<pre>$ git clone --branch rel/commons-dbcp-2.14.0 https://gitbox.apache.org/repos/asf/commons-dbcp.git</pre></section><section><a id="Developer_Access"></a>
<h1>Developer Access</h1>
<p>Only project developers can access the Git tree via this method (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>).</p>
<pre>$ git clone --branch rel/commons-dbcp-2.14.0 https://gitbox.apache.org/repos/asf/commons-dbcp.git</pre></section><section><a id="Access_from_Behind_a_Firewall"></a>
<h1>Access from Behind a Firewall</h1>
<p>Refer to the documentation of the SCM used for more information about access behind a firewall.</p></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/security.html -->

<!-- page_index: 6 -->

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-dbcp/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

# Security Vulnerabilities

None.

---

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/ -->

<!-- page_index: 7 -->

# The DBCP Component

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="The_DBCP_Component"></a>
<h1>The DBCP Component</h1>
<p>Many Apache projects support interaction with a relational database.
Creating a new connection for each user can be time consuming (often
requiring multiple seconds of clock time), in order to perform a database
transaction that might take milliseconds.  Opening a connection per user
can be unfeasible in a publicly-hosted Internet application where the
number of simultaneous users can be very large.  Accordingly, developers
often wish to share a "pool" of open connections between all of the
application's current users.  The number of users actually performing
a request at any given time is usually a very small percentage of the
total number of active users, and during request processing is the only
time that a database connection is required.  The application itself logs
into the DBMS, and handles any user account issues internally.</p>
<p>There are several Database Connection Pools already available, both
within Apache products and elsewhere.  This Commons package provides an
opportunity to coordinate the efforts required to create and maintain an
efficient, feature-rich package under the ASF license.</p>
<p>The <code>commons-dbcp2</code> artifact relies on code in the
<code>commons-pool2</code> artifact to provide the underlying object pool
mechanisms.</p>
<p>DBCP now comes in four different versions to support different versions of
JDBC. Here is how it works:</p>
<p>Developing</p>
<ul>
<li>DBCP 2.5.0 and up compiles and runs under Java 8
(<a href="https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/jdbc_42.html">JDBC 4.2</a>) and up.</li>
<li>DBCP 2.4.0 compiles and runs under Java 7
(<a href="https://docs.oracle.com/javase/7/docs/technotes/guides/jdbc/jdbc_41.html">JDBC 4.1</a>) and above.</li>
</ul>
<p>Running</p>
<ul>
<li>DBCP 2.5.0 and up binaries should be used by applications running on Java 8 and up.</li>
<li>DBCP 2.4.0 binaries should be used by applications running under Java 7.</li>
</ul>
<p>DBCP 2 is based on
<a href="https://commons.apache.org/proper/commons-pool/">Apache Commons Pool</a>
and provides increased performance, JMX
support as well as numerous other new features compared to DBCP 1.x. Users
upgrading to 2.x should be aware that the Java package name has changed, as well
as the Maven co-ordinates, since DBCP 2.x is not binary compatible with DBCP
1.x. Users should also be aware that some configuration options (e.g. maxActive
to maxTotal) have been renamed to align them with the new names used by Commons
Pool.</p>
</section>
<section><a id="Releases"></a>
<h1>Releases</h1>
<p>
       See the <a href="https://commons.apache.org/proper/commons-dbcp/download_dbcp.cgi">downloads</a> page for information on
       obtaining releases.
    </p>
</section>
<section><a id="Documentation"></a>
<h1>Documentation</h1>
<p>The
<a href="https://commons.apache.org/proper/commons-dbcp/apidocs/index.html">Javadoc API documents</a>
are available online.  In particular, you should
read the package overview of the
<code><a href="https://commons.apache.org/proper/commons-dbcp/apidocs/org/apache/commons/dbcp2/package-summary.html#package_description">org.apache.commons.dbcp2</a></code>
package for an overview of how to use DBCP.</p>
<p>There are
<a href="https://gitbox.apache.org/repos/asf?p=commons-dbcp.git;a=tree;f=doc;hb=refs/heads/master">several examples</a>
of using DBCP available.</p>
</section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="configuration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/configuration.html -->

<!-- page_index: 8 -->

# BasicDataSource Configuration Parameters

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="BasicDataSource_Configuration_Parameters"></a>
<h1>BasicDataSource Configuration Parameters</h1>
<table>
<tr>
<th>Parameter</th>
<th>Description</th></tr>
<tr>
<td>username</td>
<td>The connection user name to be passed to our JDBC driver to establish a connection.</td>
</tr>
<tr>
<td>password</td>
<td>The connection password to be passed to our JDBC driver to establish a connection.</td>
</tr>
<tr>
<td>url</td>
<td>The connection URL to be passed to our JDBC driver to establish a connection.</td>
</tr>
<tr>
<td>driverClassName</td>
<td>The fully qualified Java class name of the JDBC driver to be used.</td>
</tr>
<tr>
<td>connectionProperties</td>
<td>The connection properties that will be sent to our JDBC driver when establishing new connections.
        Format of the string must be [propertyName=property;]*
        <strong>NOTE</strong> - The "user" and "password" properties will be passed explicitly,
       so they do not need to be included here.
   </td>
</tr>
</table>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>defaultAutoCommit</td>
<td>driver default</td>
<td>The default auto-commit state of connections created by this pool.
       If not set then the setAutoCommit method will not be called.
   </td>
</tr>
<tr>
<td>defaultReadOnly</td>
<td>driver default</td>
<td>The default read-only state of connections created by this pool.
       If not set then the setReadOnly method will not be called.
       (Some drivers don't support read only mode, ex: Informix)
   </td>
</tr>
<tr>
<td>defaultTransactionIsolation</td>
<td>driver default</td>
<td>The default TransactionIsolation state of connections created by this pool.
       One of the following: (see
       <a href="https://java.sun.com/j2se/1.4.2/docs/api/java/sql/Connection.html#field_summary">javadoc</a>)

<ul>
<li>NONE</li>
<li>READ_COMMITTED</li>
<li>READ_UNCOMMITTED</li>
<li>REPEATABLE_READ</li>
<li>SERIALIZABLE</li>
</ul>
</td>
</tr>
<tr>
<td>defaultCatalog</td>
<td></td>
<td>The default catalog of connections created by this pool.</td>
</tr>
<tr>
<td>cacheState</td>
<td>true</td>
<td>If true, the pooled connection will cache the current readOnly and
      autoCommit settings when first read or written and on all subsequent
      writes. This removes the need for additional database queries for any
      further calls to the getter. If the underlying connection is accessed
      directly and the readOnly and/or autoCommit settings changed the cached
      values will not reflect the current state. In this case, caching should be
      disabled by setting this attribute to false.</td>
</tr>
<tr>
<td>defaultQueryTimeout</td>
<td>null</td>
<td>If non-null, the value of this <code>Integer</code> property determines
      the query timeout that will be used for Statements created from
      connections managed by the pool. <code>null</code> means that the driver
      default will be used.</td>
</tr>
<tr>
<td>enableAutoCommitOnReturn</td>
<td>true</td>
<td>If true, connections being returned to the pool will be checked and configured with
      <code>Connection.setAutoCommit(true)</code> if the auto commit setting is
      <code>false</code> when the connection is returned.</td>
</tr>
<tr>
<td>rollbackOnReturn</td>
<td>true</td>
<td>True means a connection will be rolled back when returned to the pool if
      auto commit is not enabled and the connection is not read-only.</td>
</tr>
</table>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>initialSize</td>
<td>0</td>
<td>
      The initial number of connections that are created when the pool
      is started.
       Since: 1.2
   </td>
</tr>
<tr>
<td>maxTotal</td>
<td>8</td>
<td>
      The maximum number of active connections that can be allocated from
      this pool at the same time, or negative for no limit.
   </td>
</tr>
<tr>
<td>maxIdle</td>
<td>8</td>
<td>
      The maximum number of connections that can remain idle in the
      pool, without extra ones being released, or negative for no limit.
   </td>
</tr>
<tr>
<td>minIdle</td>
<td>0</td>
<td>
      The minimum number of connections that can remain idle in the
      pool, without extra ones being created, or zero to create none.
   </td>
</tr>
<tr>
<td>maxWaitMillis</td>
<td>indefinitely</td>
<td>
      The maximum number of milliseconds that the pool will wait (when there
      are no available connections) for a connection to be returned before
      throwing an exception, or -1 to wait indefinitely.
   </td>
</tr>
</table>
<p>
<img alt="Warning" src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/>
<strong>NOTE</strong>: If maxIdle is set too low on heavily loaded systems it is
possible you will see connections being closed and almost immediately new
connections being opened. This is a result of the active threads momentarily
closing connections faster than they are opening them, causing the number of
idle connections to rise above maxIdle. The best value for maxIdle for heavily
loaded system will vary but the default is a good starting point.
</p>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>validationQuery</td>
<td></td>
<td>
The SQL query that will be used to validate connections from this pool
before returning them to the caller.  If specified, this query
<strong>MUST</strong> be an SQL SELECT statement that returns at least
one row. If not specified, connections will be validation by calling the
isValid() method.
   </td>
</tr>
<tr>
<td>validationQueryTimeout</td>
<td>no timeout</td>
<td>The timeout in seconds before connection validation queries fail. If set
      to a positive value, this value is passed to the driver via the
      <code>setQueryTimeout</code> method of the <code>Statement</code>
      used to execute the validation query.</td>
</tr>
<tr>
<td>testOnCreate</td>
<td>false</td>
<td>
      The indication of whether objects will be validated after creation. If the
      object fails to validate, the borrow attempt that triggered the object
      creation will fail.
   </td>
</tr>
<tr>
<td>testOnBorrow</td>
<td>true</td>
<td>
      The indication of whether objects will be validated before being
      borrowed from the pool.  If the object fails to validate, it will be
      dropped from the pool, and we will attempt to borrow another.
   </td>
</tr>
<tr>
<td>testOnReturn</td>
<td>false</td>
<td>
      The indication of whether objects will be validated before being
      returned to the pool.
   </td>
</tr>
<tr>
<td>testWhileIdle</td>
<td>false</td>
<td>
      The indication of whether objects will be validated by the idle object
      evictor (if any).  If an object fails to validate, it will be dropped
      from the pool.
   </td>
</tr>
<tr>
<td>timeBetweenEvictionRunsMillis</td>
<td>-1</td>
<td>
      The number of milliseconds to sleep between runs of the idle object
      evictor thread.  When non-positive, no idle object evictor thread will
      be run.
   </td>
</tr>
<tr>
<td>numTestsPerEvictionRun</td>
<td>3</td>
<td>
      The number of objects to examine during each run of the idle object
      evictor thread (if any).
   </td>
</tr>
<tr>
<td>minEvictableIdleTimeMillis</td>
<td>1000 * 60 * 30</td>
<td>
      The minimum amount of time an object may sit idle in the pool before it
      is eligible for eviction by the idle object evictor (if any).
   </td>
</tr>
<tr>
<td>softMinEvictableIdleTimeMillis</td>
<td>-1</td>
<td>
      The minimum amount of time a connection may sit idle in the pool before
      it is eligible for eviction by the idle connection evictor, with
      the extra condition that at least "minIdle" connections remain in the
      pool. When minEvictableIdleTimeMillis is set to a positive value,
      minEvictableIdleTimeMillis is examined first by the idle
      connection evictor - i.e. when idle connections are visited by the
      evictor, idle time is first compared against minEvictableIdleTimeMillis
      (without considering the number of idle connections in the pool) and then
      against softMinEvictableIdleTimeMillis, including the minIdle constraint.
   </td>
</tr>
<tr>
<td>maxConnLifetimeMillis</td>
<td>-1</td>
<td>
      The maximum lifetime in milliseconds of a connection. After this time is
      exceeded the connection will fail the next activation, passivation or
      validation test. A value of zero or less means the connection has an
      infinite lifetime.
   </td>
</tr>
<tr>
<td>logExpiredConnections</td>
<td>true</td>
<td>
      Flag to log a message indicating that a connection is being closed by the
      pool due to maxConnLifetimeMillis exceeded. Set this property to false
      to suppress expired connection logging that is turned on by default.
   </td>
</tr>
<tr>
<td>connectionInitSqls</td>
<td>null</td>
<td>
      A Collection of SQL statements that will be used to initialize physical
      connections when they are first created.  These statements are executed
      only once - when the configured connection factory creates the connection.
   </td>
</tr>
<tr>
<td>lifo</td>
<td>true</td>
<td>
      True means that borrowObject returns the most recently used ("last in")
      connection in the pool (if there are idle connections available).  False
      means that the pool behaves as a FIFO queue - connections are taken from
      the idle instance pool in the order that they are returned to the pool.
   </td>
</tr>
</table>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>poolPreparedStatements</td>
<td>false</td>
<td>Enable prepared statement pooling for this pool.</td>
</tr>
<tr>
<td>maxOpenPreparedStatements</td>
<td>unlimited</td>
<td>
      The maximum number of open statements that can be allocated from
      the statement pool at the same time, or negative for no limit.
   </td>
</tr>
</table>
<p>
<img alt="Info" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/>
This component has also the ability to pool PreparedStatements.
When enabled a statement pool will be created for each Connection
and PreparedStatements created by one of the following methods will be pooled:
</p>
<ul>
<li>public PreparedStatement prepareStatement(String sql)</li>
<li>public PreparedStatement prepareStatement(String sql, int resultSetType, int resultSetConcurrency)</li>
</ul>
<p>
<img alt="Warning" src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/>
<strong>NOTE</strong> - Make sure your connection has some resources left for the other statements.
Pooling PreparedStatements may keep their cursors open in the database, causing a connection to run out of cursors, especially if maxOpenPreparedStatements is left at the default (unlimited) and an application opens a large number
of different PreparedStatements per connection. To avoid this problem, maxOpenPreparedStatements should be set to a
value less than the maximum number of cursors that can be open on a Connection.
</p>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>accessToUnderlyingConnectionAllowed</td>
<td>false</td>
<td>Controls if the PoolGuard allows access to the underlying connection.</td>
</tr>
</table>
<p>When allowed you can access the underlying connection using the following construct:</p>
<pre><code>
    Connection conn = ds.getConnection();
    Connection dconn = ((DelegatingConnection) conn).getInnermostDelegate();
    ...
    conn.close()
</code></pre>
<p>
<img alt="Info" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/>
Default is false, it is a potential dangerous operation and misbehaving programs can do harmful things. (closing the underlying or continue using it when the guarded connection is already closed)
Be careful and only use when you need direct access to driver specific extensions.
</p>
<p>
<img alt="Warning" src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/>
<b>NOTE:</b> Do not close the underlying connection, only the original one.
</p>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>removeAbandonedOnMaintenance
       removeAbandonedOnBorrow
   </td>
<td>false</td>
<td>
      Flags to remove abandoned connections if they exceed the
      removeAbandonedTimout.

      A connection is considered abandoned and eligible
      for removal if it has not been used for longer than removeAbandonedTimeout.

      Creating a Statement, PreparedStatement or CallableStatement or using
      one of these to execute a query (using one of the execute methods)
      resets the lastUsed property of the parent connection.

      Setting one or both of these to true can recover db connections from poorly written
      applications which fail to close connections.

      Setting removeAbandonedOnMaintenance to true removes abandoned connections on the
      maintenance cycle (when eviction ends). This property has no effect unless maintenance
      is enabled by setting timeBetweenEvictionRunsMillis to a positive value.

      If removeAbandonedOnBorrow is true, abandoned connections are removed each time
      a connection is borrowed from the pool, with the additional requirements that

<ul>
<li>getNumActive() &gt; getMaxTotal() - 3; and</li>
<li>getNumIdle() &lt; 2 </li></ul>
</td>
</tr>
<tr>
<td>removeAbandonedTimeout</td>
<td>300</td>
<td>Timeout in <b>seconds</b> before an abandoned connection can be removed.</td>
</tr>
<tr>
<td>logAbandoned</td>
<td>false</td>
<td>
      Flag to log stack traces for application code which abandoned
      a Statement or Connection.
      Logging of abandoned Statements and Connections adds overhead
      for every Connection open or new Statement because a stack
      trace has to be generated.
   </td>
</tr>
<tr>
<td>abandonedUsageTracking</td>
<td>false</td>
<td>
      If true, the connection pool records a stack trace every time a method is called on a
      pooled connection and retains the most recent stack trace to aid debugging
      of abandoned connections. There is significant overhead added by setting this
      to true.
   </td>
</tr>
</table>
<p>
<img alt="Info" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/>
If you have enabled removeAbandonedOnMaintenance or removeAbandonedOnBorrow then it is possible that
a connection is reclaimed by the pool because it is considered to be abandoned. This mechanism is triggered
when (getNumIdle() &lt; 2) and (getNumActive() &gt; getMaxTotal() - 3) and removeAbandonedOnBorrow is true;
or after eviction finishes and removeAbandonedOnMaintenance is true. For example, maxTotal=20 and 18 active
connections and 1 idle connection would trigger removeAbandonedOnBorrow, but only the active connections
that aren't used for more then "removeAbandonedTimeout" seconds are removed (default 300 sec). Traversing
a resultset doesn't count as being used. Creating a Statement, PreparedStatement or CallableStatement or
using one of these to execute a query (using one of the execute methods) resets the lastUsed property of
the parent connection.
</p>
<table>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Description</th></tr>
<tr>
<td>fastFailValidation</td>
<td>false</td>
<td>
      When this property is true, validation fails fast for connections that have
      thrown "fatal" SQLExceptions. Requests to validate disconnected connections
      fail immediately, with no call to the driver's isValid method or attempt to
      execute a validation query.

      The SQL_STATE codes considered to signal fatal errors are by default the following:

<ul>
<li>57P01 (ADMIN SHUTDOWN)</li>
<li>57P02 (CRASH SHUTDOWN)</li>
<li>57P03 (CANNOT CONNECT NOW)</li>
<li>01002 (SQL92 disconnect error)</li>
<li>JZ0C0 (Sybase disconnect error)</li>
<li>JZ0C1 (Sybase disconnect error)</li>
<li>Any SQL_STATE code that starts with "08"</li>
</ul>
      To override this default set of disconnection codes, set the
      <code>disconnectionSqlCodes</code> property.
   </td>
</tr>
<tr>
<td>disconnectionSqlCodes</td>
<td>null</td>
<td>Comma-delimited list of SQL_STATE codes considered to signal fatal disconnection
       errors. Setting this property has no effect unless
      <code>fastFailValidation</code> is set to <code>true.</code>
</td>
</tr>
<tr>
<td>disconnectionIgnoreSqlCodes</td>
<td>null</td>
<td>Comma-delimited list of SQL State codes that should be ignored when determining fatal disconnection errors.
       These codes will not trigger a fatal disconnection status, even if they match the usual criteria.
       Setting this property has no effect unless <code>fastFailValidation</code> is set to <code>true.</code>
</td>
</tr>
<tr>
<td>jmxName</td>
<td></td>
<td>
       Registers the DataSource as JMX MBean under specified name. The name has to conform to the JMX Object Name Syntax (see
       <a href="https://docs.oracle.com/javase/1.5.0/docs/api/javax/management/ObjectName.html">javadoc</a>).
    </td>
</tr>
<tr>
<td>registerConnectionMBean</td>
<td>true</td>
<td>
        Registers Connection JMX MBeans. See <a href="https://issues.apache.org/jira/browse/DBCP-585">DBCP-585</a>).
    </td>
</tr>
</table>
</section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="guide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/guide/index.html -->

<!-- page_index: 9 -->

# BasicDataSource

![Basic data source](assets/images/basicdatasource_2ae3e3e75bef8c7d.gif)

# ConnectionFactory

![Connection factory](assets/images/connectionfactory_b52c4653fae546d3.gif)

---

<a id="guide-jndi-howto"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/guide/jndi-howto.html -->

<!-- page_index: 10 -->

# JNDI Howto

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="JNDI_Howto"></a>
<h1>JNDI Howto</h1>
<p>
  The <a href="https://java.sun.com/products/jndi/">Java Naming and Directory Interface</a>
  (JNDI) is part of the Java platform,
  providing applications based on Java technology with a unified interface to
  multiple naming and directory services. You can build powerful and portable
  directory-enabled applications using this industry standard.
</p>
<p>
  When you deploy your application inside an application server, the container will setup
  the JNDI tree for you. But if you are writing a framework or just a standalone application,
  then the following examples will show you how to construct and bind references to DBCP
  datasources.
</p>
<p>
  The following examples are using the sun filesystem JNDI service provider.
  You can download it from the
  <a href="https://java.sun.com/products/jndi/downloads/index.html">JNDI software download</a> page.
</p>
</section>
<section><a id="BasicDataSource"></a>
<h1>BasicDataSource</h1>
<pre><code>
  System.setProperty(Context.INITIAL_CONTEXT_FACTORY,
    "com.sun.jndi.fscontext.RefFSContextFactory");
  System.setProperty(Context.PROVIDER_URL, "file:///tmp");
  InitialContext ic = new InitialContext();

  // Construct BasicDataSource
  BasicDataSource bds = new BasicDataSource();
  bds.setDriverClassName("org.apache.commons.dbcp2.TesterDriver");
  bds.setUrl("jdbc:apache:commons:testdriver");
  bds.setUsername("userName");
  bds.setPassword("password");

  ic.rebind("jdbc/basic", bds);

  // Use
  InitialContext ic2 = new InitialContext();
  DataSource ds = (DataSource) ic2.lookup("jdbc/basic");
  assertNotNull(ds);
  Connection conn = ds.getConnection();
  assertNotNull(conn);
  conn.close();
</code></pre>
</section>
<section><a id="PerUserPoolDataSource"></a>
<h1>PerUserPoolDataSource</h1>
<pre><code>
  System.setProperty(Context.INITIAL_CONTEXT_FACTORY,
    "com.sun.jndi.fscontext.RefFSContextFactory");
  System.setProperty(Context.PROVIDER_URL, "file:///tmp");
  InitialContext ic = new InitialContext();

  // Construct DriverAdapterCPDS reference
  Reference cpdsRef = new Reference("org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS",
    "org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS", null);
  cpdsRef.add(new StringRefAddr("driver", "org.apache.commons.dbcp2.TesterDriver"));
  cpdsRef.add(new StringRefAddr("url", "jdbc:apache:commons:testdriver"));
  cpdsRef.add(new StringRefAddr("user", "foo"));
  cpdsRef.add(new StringRefAddr("password", "bar"));
  ic.rebind("jdbc/cpds", cpdsRef);

  // Construct PerUserPoolDataSource reference
  Reference ref = new Reference("org.apache.commons.dbcp2.datasources.PerUserPoolDataSource",
    "org.apache.commons.dbcp2.datasources.PerUserPoolDataSourceFactory", null);
  ref.add(new StringRefAddr("dataSourceName", "jdbc/cpds"));
  ref.add(new StringRefAddr("defaultMaxTotal", "100"));
  ref.add(new StringRefAddr("defaultMaxIdle", "30"));
  ref.add(new StringRefAddr("defaultMaxWaitMillis", "10000"));
  ic.rebind("jdbc/peruser", ref);

  // Use
  InitialContext ic2 = new InitialContext();
  DataSource ds = (DataSource) ic2.lookup("jdbc/peruser");
  assertNotNull(ds);
  Connection conn = ds.getConnection("foo","bar");
  assertNotNull(conn);
  conn.close();
</code></pre>
</section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="guide-classdiagrams"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/guide/classdiagrams.html -->

<!-- page_index: 11 -->

# PoolingDataSource

![Poolinf data source](assets/images/poolingdatasource_7ebc35280cff40b5.gif)

# PoolingConnection

![Pooling connection](assets/images/poolingconnection_010c477f89f3a09d.gif)

# Delegating

![Delegating](assets/images/delegating_d9c657c47cca14ef.gif)

# AbandonedObjectPool

![Abandoned object pool](assets/images/abandonedobjectpool_9ab8d6e9cd9527b1.gif)

---

<a id="guide-sequencediagrams"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/guide/sequencediagrams.html -->

<!-- page_index: 12 -->

# createDataSource

![Create data source](assets/images/createdatasource_a417da001b46e2ed.gif)

# getConnection

![Get connection](assets/images/getconnection_49b9221e6b89f463.gif)

# prepareStatement

![Pprepare statement](assets/images/preparestatement_9491ef6f08aa3484.gif)

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/building.html -->

<!-- page_index: 13 -->

# Overview

Commons DBCP uses
[Maven](https://maven.apache.org)
or
[Ant](https://ant.apache.org)
as a build system.
The maven build requires maven 3 and JDK 8.

# Maven Goals

To build a jar file, change into DBCP's root directory and run
**`mvn clean package`**
.
The result will be in the "target" subdirectory.

To build the Javadocs, run
**`mvn clean javadoc:javadoc`**
.
The result will be in "target/site/apidocs/".

To build the full website, run
**`mvn clean verify site`**
.
The result will be in "target/site".

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/project-info.html -->

<!-- page_index: 14 -->

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
<td><a href="#index_2">About</a></td>
<td>Apache Commons DBCP software implements Database Connection Pooling</td></tr>
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
<td><a href="https://commons.apache.org/proper/commons-dbcp/mailing-lists.html">Mailing Lists</a></td>
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

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/summary.html -->

<!-- page_index: 15 -->

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
<td>Apache Commons DBCP</td></tr>
<tr>
<td>Description</td>
<td>Apache Commons DBCP software implements Database Connection Pooling</td></tr>
<tr>
<td>Homepage</td>
<td><a href="#index">https://commons.apache.org/proper/commons-dbcp/</a></td></tr></table></section><section><a id="Project_Organization"></a>
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
<td>commons-dbcp2</td></tr>
<tr>
<td>Version</td>
<td>2.14.0</td></tr>
<tr>
<td>Type</td>
<td>jar</td></tr>
<tr>
<td>Java Version</td>
<td>1.8</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/team.html -->

<!-- page_index: 16 -->

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
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="morgand"></a>morgand</td>
<td>Morgan Delagrange</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="geirm"></a>geirm</td>
<td>Geir Magnusson</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="craigmcc"></a>craigmcc</td>
<td>Craig McClanahan</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="jmcnally"></a>jmcnally</td>
<td>John McNally</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="mpoeschl"></a>mpoeschl</td>
<td>Martin Poeschl</td>
<td><a href="mailto:mpoeschl@marmot.at">mpoeschl@marmot.at</a></td>
<td>-</td>
<td>tucana.at</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="rwaldhoff"></a>rwaldhoff</td>
<td>Rodney Waldhoff</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="dweinr1"></a>dweinr1</td>
<td>David Weinrich</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="dirkv"></a>dirkv</td>
<td>Dirk Verbeeck</td>
<td><a href="mailto:">-</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/248341e80da66f10c0d6af27f40c8d63_1ecb7a7f9148be4d.jpg"/></figure></td>
<td><a id="yoavs"></a>yoavs</td>
<td>Yoav Shapira</td>
<td><a href="mailto:yoavs@apache.org">yoavs@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/b57f757efea9e04ad3a5cb489499ec01_f932ae32c8cc9790.jpg"/></figure></td>
<td><a id="joehni"></a>joehni</td>
<td>Jörg Schaible</td>
<td><a href="mailto:joerg.schaible@gmx.de">joerg.schaible@gmx.de</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>+1</td></tr>
<tr>
<td><figure><img src="assets/images/2ecfd40ef69301d18d9f6067ce5d23b9_2208d29b8bd7b076.jpg"/></figure></td>
<td><a id="markt"></a>markt</td>
<td>Mark Thomas</td>
<td><a href="mailto:markt@apache.org">markt@apache.org</a></td>
<td>-</td>
<td>The Apache Software Foundation</td>
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
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="nacho"></a>nacho</td>
<td>Ignacio J. Ortega</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td><a id="sullis"></a>sullis</td>
<td>Sean C. Sullivan</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr></table></section><section><a id="Contributors"></a>
<h2>Contributors</h2>
<p>The following additional people have contributed to this project through the way of suggestions, patches or documentation.</p>
<table>
<tr>
<th>Image</th>
<th>Name</th>
<th>Email</th></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>Todd Carmichael</td>
<td><a href="mailto:toddc@concur.com">toddc@concur.com</a></td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>Wayne Woodfield</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>Dain Sundstrom</td>
<td><a href="mailto:dain@apache.org">dain@apache.org</a></td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>Philippe Mouawad</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>Glenn L. Nielsen</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>James House</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>James Ring</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_3a42d0c72c7c3a54.jpg"/></figure></td>
<td>Peter Wicks</td>
<td><a href="mailto:pwicks@apache.org">pwicks@apache.org</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/dependency-management.html -->

<!-- page_index: 17 -->

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
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-api</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-engine</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-migrationsupport</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-params</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-commons</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-console</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-engine</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-jfr</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-launcher</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-reporting</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-runner</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite-api</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite-commons</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-suite-engine</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-testkit</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.vintage</td>
<td><a href="https://junit.org/">junit-vintage-engine</a></td>
<td>5.14.1</td>
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

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependencies"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/dependencies.html -->

<!-- page_index: 18 -->

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
<td>commons-logging</td>
<td><a href="https://commons.apache.org/proper/commons-logging/">commons-logging</a></td>
<td>1.3.5</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>jakarta.transaction</td>
<td><a href="https://projects.eclipse.org/projects/ee4j.jta">jakarta.transaction-api</a></td>
<td>1.3.3</td>
<td>jar</td>
<td><a href="http://www.eclipse.org/legal/epl-2.0">EPL 2.0</a><a href="https://www.gnu.org/software/classpath/license.html">GPL2 w/ CPE</a></td></tr>
<tr>
<td>org.apache.commons</td>
<td><a href="https://commons.apache.org/proper/commons-pool/">commons-pool2</a></td>
<td>2.13.0</td>
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
<td>3.20.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.modules</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/plugins/connector/geronimo-transaction">geronimo-transaction</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.jboss</td>
<td><a href="http://www.jboss.org">jboss-transaction-spi</a></td>
<td>8.0.0.Final</td>
<td>jar</td>
<td><a href="http://repository.jboss.org/licenses/cc0-1.0.txt">Public Domain</a></td></tr>
<tr>
<td>org.jboss.logging</td>
<td><a href="http://www.jboss.org">jboss-logging</a></td>
<td>3.4.3.Final</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, version 2.0</a></td></tr>
<tr>
<td>org.jboss.narayana.jta</td>
<td><a href="http://www.jboss.org/jbosstm/narayana-jta-all/narayana-jta/">narayana-jta</a></td>
<td>5.12.7.Final</td>
<td>jar</td>
<td><a href="http://www.gnu.org/licenses/lgpl-2.1.html">LGPL 2.1</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.mockito</td>
<td><a href="https://github.com/mockito/mockito">mockito-core</a></td>
<td>4.11.0</td>
<td>jar</td>
<td><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></td></tr>
<tr>
<td>org.slf4j</td>
<td><a href="http://www.slf4j.org">slf4j-simple</a></td>
<td>2.0.17</td>
<td>jar</td>
<td><a href="https://opensource.org/license/mit">MIT</a></td></tr>
<tr>
<td>tomcat</td>
<td>naming-common</td>
<td>5.0.28</td>
<td>jar</td>
<td>-</td></tr>
<tr>
<td>tomcat</td>
<td>naming-java</td>
<td>5.0.28</td>
<td>jar</td>
<td>-</td></tr></table></section></section><section><a id="Project_Transitive_Dependencies"></a>
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
<td>asm</td>
<td><a href="http://asm.objectweb.org/asm/">asm</a></td>
<td>3.1</td>
<td>jar</td>
<td>-</td></tr>
<tr>
<td>asm</td>
<td><a href="http://asm.objectweb.org/asm-commons/">asm-commons</a></td>
<td>3.1</td>
<td>jar</td>
<td>-</td></tr>
<tr>
<td>cglib</td>
<td><a href="http://cglib.sourceforge.net/">cglib-nodep</a></td>
<td>2.1_3</td>
<td>jar</td>
<td>-</td></tr>
<tr>
<td>com.thoughtworks.xstream</td>
<td>xstream</td>
<td>1.3</td>
<td>jar</td>
<td><a href="http://xstream.codehaus.com/license.html">BSD style</a></td></tr>
<tr>
<td>commons-cli</td>
<td>commons-cli</td>
<td>1.0</td>
<td>jar</td>
<td>-</td></tr>
<tr>
<td>commons-jexl</td>
<td><a href="http://jakarta.apache.org/commons/jexl/">commons-jexl</a></td>
<td>1.1</td>
<td>jar</td>
<td><a href="https://commons.apache.org/LICENSE.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>jakarta.annotation</td>
<td><a href="https://projects.eclipse.org/projects/ee4j.ca">jakarta.annotation-api</a></td>
<td>2.0.0</td>
<td>jar</td>
<td><a href="http://www.eclipse.org/legal/epl-2.0">EPL 2.0</a><a href="https://www.gnu.org/software/classpath/license.html">GPL2 w/ CPE</a></td></tr>
<tr>
<td>jakarta.resource</td>
<td><a href="https://github.com/eclipse-ee4j/jca-api">jakarta.resource-api</a></td>
<td>2.0.0</td>
<td>jar</td>
<td><a href="http://www.eclipse.org/legal/epl-2.0">EPL 2.0</a><a href="https://www.gnu.org/software/classpath/license.html">GPL2 w/ CPE</a></td></tr>
<tr>
<td>log4j</td>
<td><a href="http://logging.apache.org:80/log4j/1.2/">log4j</a></td>
<td>1.2.15</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
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
<td>org.apache.geronimo.components</td>
<td><a href="http://geronimo.apache.org/maven/txmanager/2.2.1/geronimo-transaction">geronimo-transaction</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-cli">geronimo-cli</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-common">geronimo-common</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-core">geronimo-core</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-crypto">geronimo-crypto</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-kernel">geronimo-kernel</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-management">geronimo-management</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.framework</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-system">geronimo-system</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.modules</td>
<td><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/plugins/j2ee/geronimo-j2ee">geronimo-j2ee</a></td>
<td>2.2.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.specs</td>
<td><a href="http://geronimo.apache.org/specs/geronimo-j2ee-connector_1.5_spec">geronimo-j2ee-connector_1.5_spec</a></td>
<td>2.0.0</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.specs</td>
<td><a href="http://geronimo.apache.org/specs/geronimo-j2ee-management_1.1_spec">geronimo-j2ee-management_1.1_spec</a></td>
<td>1.0.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.specs</td>
<td><a href="http://geronimo.apache.org/maven/specs/geronimo-jaxb_2.1_spec/1.0">geronimo-jaxb_2.1_spec</a></td>
<td>1.0</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.specs</td>
<td><a href="http://geronimo.apache.org/specs/geronimo-jta_1.1_spec">geronimo-jta_1.1_spec</a></td>
<td>1.1.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.geronimo.specs</td>
<td><a href="http://geronimo.apache.org/specs/geronimo-stax-api_1.0_spec">geronimo-stax-api_1.0_spec</a></td>
<td>1.0.1</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apache.xbean</td>
<td><a href="http://geronimo.apache.org/maven/xbean/3.7/xbean-reflect">xbean-reflect</a></td>
<td>3.7</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></td></tr>
<tr>
<td>org.apiguardian</td>
<td><a href="https://github.com/apiguardian-team/apiguardian">apiguardian-api</a></td>
<td>1.1.2</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr>
<tr>
<td>org.jboss.spec.javax.resource</td>
<td><a href="http://www.jboss.org/jboss-connector-api_1.7_spec">jboss-connector-api_1.7_spec</a></td>
<td>1.0.0.Final</td>
<td>jar</td>
<td><a href="http://repository.jboss.org/licenses/cddl.txt">Common Development and Distribution License</a><a href="http://repository.jboss.org/licenses/gpl-2.0-ce.txt">GNU General Public License, Version 2 with the Classpath Exception</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-api</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-engine</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter-params</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-commons</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.junit.platform</td>
<td><a href="https://junit.org/">junit-platform-engine</a></td>
<td>1.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td>org.objectweb.howl</td>
<td><a href="http://forge.objectweb.org/projects/howl/">howl</a></td>
<td>1.0.1-1</td>
<td>jar</td>
<td>BSD</td></tr>
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
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr>
<tr>
<td>org.slf4j</td>
<td><a href="http://www.slf4j.org">slf4j-api</a></td>
<td>2.0.17</td>
<td>jar</td>
<td><a href="https://opensource.org/license/mit">MIT</a></td></tr>
<tr>
<td>xpp3</td>
<td><a href="http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/">xpp3_min</a></td>
<td>1.1.4c</td>
<td>jar</td>
<td><a href="http://www.extreme.indiana.edu/viewcvs/~checkout~/XPP3/java/LICENSE.txt">Indiana University Extreme! Lab Software License, vesion 1.1.1</a><a href="http://creativecommons.org/licenses/publicdomain">Public Domain</a></td></tr></table></section></section><section><a id="Project_Dependency_Graph"></a>
<h1>Project Dependency Graph</h1>
<section><a id="Dependency_Tree"></a>
<h2>Dependency Tree</h2>
<ul>
<li>org.apache.commons:commons-dbcp2:jar:2.14.0 <img alt="[Information]" id="_img1" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep0">
<table>
<tr>
<th>Apache Commons DBCP</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Commons DBCP software implements Database Connection Pooling</p>
<p><b>URL: </b><a href="#index">https://commons.apache.org/proper/commons-dbcp/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.commons:commons-pool2:jar:2.13.0 (compile) <img alt="[Information]" id="_img3" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep2">
<table>
<tr>
<th>Apache Commons Pool</th></tr>
<tr>
<td>
<p><b>Description: </b>The Apache Commons Object Pooling Library.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-pool/">https://commons.apache.org/proper/commons-pool/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>commons-logging:commons-logging:jar:1.3.5 (compile) <img alt="[Information]" id="_img5" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep4">
<table>
<tr>
<th>Apache Commons Logging</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Commons Logging is a thin adapter allowing configurable bridging to other,
    well-known logging systems.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-logging/">https://commons.apache.org/proper/commons-logging/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>org.junit.jupiter:junit-jupiter:jar:5.14.1 (test) <img alt="[Information]" id="_img7" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep6">
<table>
<tr>
<th>JUnit Jupiter (Aggregator)</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.jupiter:junit-jupiter-api:jar:5.14.1 (test) <img alt="[Information]" id="_img9" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep8">
<table>
<tr>
<th>JUnit Jupiter API</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-api" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.opentest4j:opentest4j:jar:1.3.0 (test) <img alt="[Information]" id="_img11" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep10">
<table>
<tr>
<th>org.opentest4j:opentest4j</th></tr>
<tr>
<td>
<p><b>Description: </b>Open Test Alliance for the JVM</p>
<p><b>URL: </b><a href="https://github.com/ota4j-team/opentest4j">https://github.com/ota4j-team/opentest4j</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.junit.platform:junit-platform-commons:jar:1.14.1 (test) <img alt="[Information]" id="_img13" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep12">
<table>
<tr>
<th>JUnit Platform Commons</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-commons" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li>
<li>org.apiguardian:apiguardian-api:jar:1.1.2 (test) <img alt="[Information]" id="_img15" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep14">
<table>
<tr>
<th>org.apiguardian:apiguardian-api</th></tr>
<tr>
<td>
<p><b>Description: </b>@API Guardian</p>
<p><b>URL: </b><a href="https://github.com/apiguardian-team/apiguardian">https://github.com/apiguardian-team/apiguardian</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.junit.jupiter:junit-jupiter-params:jar:5.14.1 (test) <img alt="[Information]" id="_img17" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep16">
<table>
<tr>
<th>JUnit Jupiter Params</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-params" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li>
<li>org.junit.jupiter:junit-jupiter-engine:jar:5.14.1 (test) <img alt="[Information]" id="_img19" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep18">
<table>
<tr>
<th>JUnit Jupiter Engine</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-jupiter-engine" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div>
<ul>
<li>org.junit.platform:junit-platform-engine:jar:1.14.1 (test) <img alt="[Information]" id="_img21" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep20">
<table>
<tr>
<th>JUnit Platform Engine API</th></tr>
<tr>
<td>
<p><b>Description: </b>Module "junit-platform-engine" of JUnit 5.</p>
<p><b>URL: </b><a href="https://junit.org/">https://junit.org/</a></p>
<p><b>Project Licenses: </b><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></p></td></tr></table></div></li></ul></li></ul></li>
<li>org.mockito:mockito-core:jar:4.11.0 (test) <img alt="[Information]" id="_img23" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep22">
<table>
<tr>
<th>mockito-core</th></tr>
<tr>
<td>
<p><b>Description: </b>Mockito mock objects library core API and implementation</p>
<p><b>URL: </b><a href="https://github.com/mockito/mockito">https://github.com/mockito/mockito</a></p>
<p><b>Project Licenses: </b><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></p></td></tr></table></div>
<ul>
<li>net.bytebuddy:byte-buddy:jar:1.12.19 (test) <img alt="[Information]" id="_img25" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep24">
<table>
<tr>
<th>Byte Buddy (without dependencies)</th></tr>
<tr>
<td>
<p><b>Description: </b>Byte Buddy is a Java library for creating Java classes at run time.
        This artifact is a build of Byte Buddy with all ASM dependencies repackaged into its own name space.</p>
<p><b>URL: </b><a href="https://bytebuddy.net/byte-buddy">https://bytebuddy.net/byte-buddy</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>net.bytebuddy:byte-buddy-agent:jar:1.12.19 (test) <img alt="[Information]" id="_img27" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep26">
<table>
<tr>
<th>Byte Buddy agent</th></tr>
<tr>
<td>
<p><b>Description: </b>The Byte Buddy agent offers convenience for attaching an agent to the local or a remote VM.</p>
<p><b>URL: </b><a href="https://bytebuddy.net/byte-buddy-agent">https://bytebuddy.net/byte-buddy-agent</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.objenesis:objenesis:jar:3.3 (test) <img alt="[Information]" id="_img29" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep28">
<table>
<tr>
<th>Objenesis</th></tr>
<tr>
<td>
<p><b>Description: </b>A library for instantiating Java objects</p>
<p><b>URL: </b><a href="http://objenesis.org/objenesis">http://objenesis.org/objenesis</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.apache.commons:commons-lang3:jar:3.20.0 (test) <img alt="[Information]" id="_img31" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep30">
<table>
<tr>
<th>Apache Commons Lang</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Commons Lang, a package of Java utility classes for the
  classes that are in java.lang's hierarchy, or are considered to be so
  standard as to justify existence in java.lang.

  The code is tested using the latest revision of the JDK for supported
  LTS releases: 8, 11, 17, 21 and 25 currently.
  See https://github.com/apache/commons-lang/blob/master/.github/workflows/maven.yml

  Please ensure your build environment is up-to-date and kindly report any build issues.</p>
<p><b>URL: </b><a href="https://commons.apache.org/proper/commons-lang/">https://commons.apache.org/proper/commons-lang/</a></p>
<p><b>Project Licenses: </b><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></p></td></tr></table></div></li>
<li>jakarta.transaction:jakarta.transaction-api:jar:1.3.3 (compile) <img alt="[Information]" id="_img33" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep32">
<table>
<tr>
<th>javax.transaction API</th></tr>
<tr>
<td>
<p><b>Description: </b>Jakarta Transactions</p>
<p><b>URL: </b><a href="https://projects.eclipse.org/projects/ee4j.jta">https://projects.eclipse.org/projects/ee4j.jta</a></p>
<p><b>Project Licenses: </b><a href="http://www.eclipse.org/legal/epl-2.0">EPL 2.0</a>, <a href="https://www.gnu.org/software/classpath/license.html">GPL2 w/ CPE</a></p></td></tr></table></div></li>
<li>tomcat:naming-common:jar:5.0.28 (test) <img alt="[Information]" id="_img35" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep34">
<table>
<tr>
<th>naming-common</th></tr>
<tr>
<td>
<p><b>Description: </b>There is currently no description associated with this project.</p>
<p><b>Project Licenses: </b>No licenses are defined for this project.</p></td></tr></table></div></li>
<li>tomcat:naming-java:jar:5.0.28 (test) <img alt="[Information]" id="_img37" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep36">
<table>
<tr>
<th>naming-java</th></tr>
<tr>
<td>
<p><b>Description: </b>There is currently no description associated with this project.</p>
<p><b>Project Licenses: </b>No licenses are defined for this project.</p></td></tr></table></div></li>
<li>org.apache.geronimo.modules:geronimo-transaction:jar:2.2.1 (test) <img alt="[Information]" id="_img39" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep38">
<table>
<tr>
<th>Geronimo Plugins, Connector :: Transaction</th></tr>
<tr>
<td>
<p><b>Description: </b>Connector plugin</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/plugins/connector/geronimo-transaction">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/plugins/connector/geronimo-transaction</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.geronimo.components:geronimo-transaction:jar:2.2.1 (test) <img alt="[Information]" id="_img41" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep40">
<table>
<tr>
<th>Geronimo TxManager :: Transaction</th></tr>
<tr>
<td>
<p><b>Description: </b>Geronimo Transaction Manager</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/maven/txmanager/2.2.1/geronimo-transaction">http://geronimo.apache.org/maven/txmanager/2.2.1/geronimo-transaction</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.geronimo.specs:geronimo-jta_1.1_spec:jar:1.1.1 (test) <img alt="[Information]" id="_img43" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep42">
<table>
<tr>
<th>JTA 1.1</th></tr>
<tr>
<td>
<p><b>Description: </b>Provides open-source implementations of Sun specifications.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/specs/geronimo-jta_1.1_spec">http://geronimo.apache.org/specs/geronimo-jta_1.1_spec</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.apache.geronimo.specs:geronimo-j2ee-connector_1.5_spec:jar:2.0.0 (test) <img alt="[Information]" id="_img45" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep44">
<table>
<tr>
<th>J2EE Connector 1.5</th></tr>
<tr>
<td>
<p><b>Description: </b>Provides open-source implementations of Sun specifications.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/specs/geronimo-j2ee-connector_1.5_spec">http://geronimo.apache.org/specs/geronimo-j2ee-connector_1.5_spec</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.apache.geronimo.framework:geronimo-core:jar:2.2.1 (test) <img alt="[Information]" id="_img47" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep46">
<table>
<tr>
<th>Geronimo Framework, Modules :: Core</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Geronimo, the JavaEE server project of the Apache Software Foundation.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-core">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-core</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.geronimo.framework:geronimo-system:jar:2.2.1 (test) <img alt="[Information]" id="_img49" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep48">
<table>
<tr>
<th>Geronimo Framework, Modules :: System</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Geronimo, the JavaEE server project of the Apache Software Foundation.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-system">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-system</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.geronimo.framework:geronimo-cli:jar:2.2.1 (test) <img alt="[Information]" id="_img51" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep50">
<table>
<tr>
<th>Geronimo Framework, Modules :: CLI</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Geronimo, the JavaEE server project of the Apache Software Foundation.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-cli">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-cli</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>commons-cli:commons-cli:jar:1.0 (test) <img alt="[Information]" id="_img53" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep52">
<table>
<tr>
<th>CLI</th></tr>
<tr>
<td>
<p><b>Description: </b>Commons CLI provides a simple API for working with the command line arguments and options.</p>
<p><b>Project Licenses: </b>No licenses are defined for this project.</p></td></tr></table></div></li></ul></li>
<li>org.apache.geronimo.framework:geronimo-common:jar:2.2.1 (test) <img alt="[Information]" id="_img55" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep54">
<table>
<tr>
<th>Geronimo Framework, Modules :: Common</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Geronimo, the JavaEE server project of the Apache Software Foundation.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-common">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-common</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.apache.geronimo.framework:geronimo-crypto:jar:2.2.1 (test) <img alt="[Information]" id="_img57" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep56">
<table>
<tr>
<th>Geronimo Framework, Modules :: Crypto</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Geronimo, the JavaEE server project of the Apache Software Foundation.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-crypto">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-crypto</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.apache.geronimo.framework:geronimo-kernel:jar:2.2.1 (test) <img alt="[Information]" id="_img59" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep58">
<table>
<tr>
<th>Geronimo Framework, Modules :: Kernel</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Geronimo, the JavaEE server project of the Apache Software Foundation.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-kernel">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-kernel</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>asm:asm:jar:3.1 (test) <img alt="[Information]" id="_img61" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep60">
<table>
<tr>
<th>ASM Core</th></tr>
<tr>
<td>
<p><b>Description: </b>A very small and fast Java bytecode manipulation framework</p>
<p><b>URL: </b><a href="http://asm.objectweb.org/asm/">http://asm.objectweb.org/asm/</a></p>
<p><b>Project Licenses: </b>No licenses are defined for this project.</p></td></tr></table></div></li>
<li>asm:asm-commons:jar:3.1 (test) <img alt="[Information]" id="_img63" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep62">
<table>
<tr>
<th>ASM Commons</th></tr>
<tr>
<td>
<p><b>Description: </b>A very small and fast Java bytecode manipulation framework</p>
<p><b>URL: </b><a href="http://asm.objectweb.org/asm-commons/">http://asm.objectweb.org/asm-commons/</a></p>
<p><b>Project Licenses: </b>No licenses are defined for this project.</p></td></tr></table></div></li>
<li>cglib:cglib-nodep:jar:2.1_3 (test) <img alt="[Information]" id="_img65" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep64">
<table>
<tr>
<th>cglib</th></tr>
<tr>
<td>
<p><b>Description: </b>There is currently no description associated with this project.</p>
<p><b>URL: </b><a href="http://cglib.sourceforge.net/">http://cglib.sourceforge.net/</a></p>
<p><b>Project Licenses: </b>No licenses are defined for this project.</p></td></tr></table></div></li>
<li>org.apache.xbean:xbean-reflect:jar:3.7 (test) <img alt="[Information]" id="_img67" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep66">
<table>
<tr>
<th>Apache XBean :: Reflect</th></tr>
<tr>
<td>
<p><b>Description: </b>xbean-reflect provides very flexible ways to creat objects and graphs of objects for DI frameworks</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/maven/xbean/3.7/xbean-reflect">http://geronimo.apache.org/maven/xbean/3.7/xbean-reflect</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>com.thoughtworks.xstream:xstream:jar:1.3 (test) <img alt="[Information]" id="_img69" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep68">
<table>
<tr>
<th>XStream Core</th></tr>
<tr>
<td>
<p><b>Description: </b>There is currently no description associated with this project.</p>
<p><b>Project Licenses: </b><a href="http://xstream.codehaus.com/license.html">BSD style</a></p></td></tr></table></div>
<ul>
<li>xpp3:xpp3_min:jar:1.1.4c (test) <img alt="[Information]" id="_img71" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep70">
<table>
<tr>
<th>MXP1: Xml Pull Parser 3rd Edition (XPP3)</th></tr>
<tr>
<td>
<p><b>Description: </b>MXP1 is a stable XmlPull parsing engine that is based on ideas from XPP and in particular XPP2 but completely revised and rewritten to take the best advantage of latest JIT JVMs such as Hotspot in JDK 1.4+.</p>
<p><b>URL: </b><a href="http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/">http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/</a></p>
<p><b>Project Licenses: </b><a href="http://www.extreme.indiana.edu/viewcvs/~checkout~/XPP3/java/LICENSE.txt">Indiana University Extreme! Lab Software License, vesion 1.1.1</a>, <a href="http://creativecommons.org/licenses/publicdomain">Public Domain</a></p></td></tr></table></div></li></ul></li></ul></li>
<li>commons-jexl:commons-jexl:jar:1.1 (test) <img alt="[Information]" id="_img73" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep72">
<table>
<tr>
<th>Commons JEXL</th></tr>
<tr>
<td>
<p><b>Description: </b>Jexl is an implementation of the JSTL Expression Language with extensions.</p>
<p><b>URL: </b><a href="http://jakarta.apache.org/commons/jexl/">http://jakarta.apache.org/commons/jexl/</a></p>
<p><b>Project Licenses: </b><a href="https://commons.apache.org/LICENSE.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>log4j:log4j:jar:1.2.15 (test) <img alt="[Information]" id="_img75" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep74">
<table>
<tr>
<th>Apache Log4j</th></tr>
<tr>
<td>
<p><b>Description: </b>Apache Log4j 1.2</p>
<p><b>URL: </b><a href="http://logging.apache.org:80/log4j/1.2/">http://logging.apache.org:80/log4j/1.2/</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.apache.geronimo.specs:geronimo-jaxb_2.1_spec:jar:1.0 (test) <img alt="[Information]" id="_img77" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep76">
<table>
<tr>
<th>Apache JAXB 2.1 Spec</th></tr>
<tr>
<td>
<p><b>Description: </b>Java API for XML binding 2.1 API</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/maven/specs/geronimo-jaxb_2.1_spec/1.0">http://geronimo.apache.org/maven/specs/geronimo-jaxb_2.1_spec/1.0</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.apache.geronimo.specs:geronimo-stax-api_1.0_spec:jar:1.0.1 (test) <img alt="[Information]" id="_img79" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep78">
<table>
<tr>
<th>Streaming API for XML (STAX API 1.0)</th></tr>
<tr>
<td>
<p><b>Description: </b>Provides open-source implementations of Sun specifications.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/specs/geronimo-stax-api_1.0_spec">http://geronimo.apache.org/specs/geronimo-stax-api_1.0_spec</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li></ul></li>
<li>org.apache.geronimo.framework:geronimo-management:jar:2.2.1 (test) <img alt="[Information]" id="_img81" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep80">
<table>
<tr>
<th>Geronimo Framework, Modules :: Management API</th></tr>
<tr>
<td>
<p><b>Description: </b>Contains interfaces that define the management API for Geronimo.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-management">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/framework/modules/geronimo-management</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div>
<ul>
<li>org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec:jar:1.0.1 (test) <img alt="[Information]" id="_img83" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep82">
<table>
<tr>
<th>J2EE Management 1.1</th></tr>
<tr>
<td>
<p><b>Description: </b>Provides open-source implementations of Sun specifications.</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/specs/geronimo-j2ee-management_1.1_spec">http://geronimo.apache.org/specs/geronimo-j2ee-management_1.1_spec</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li></ul></li></ul></li>
<li>org.apache.geronimo.modules:geronimo-j2ee:jar:2.2.1 (test) <img alt="[Information]" id="_img85" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep84">
<table>
<tr>
<th>Geronimo Framework, Modules :: J2EE</th></tr>
<tr>
<td>
<p><b>Description: </b>J2EE plugin</p>
<p><b>URL: </b><a href="http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/plugins/j2ee/geronimo-j2ee">http://geronimo.apache.org/genesis-default-flava/genesis-java5-flava/geronimo/plugins/j2ee/geronimo-j2ee</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache Software License, Version 2.0</a></p></td></tr></table></div></li>
<li>org.objectweb.howl:howl:jar:1.0.1-1 (test) <img alt="[Information]" id="_img87" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep86">
<table>
<tr>
<th>HOWL logger</th></tr>
<tr>
<td>
<p><b>Description: </b>HOWL is a logger implementation providing features required by the JOTM project. HOWL uses unformatted
        binary logs to maximize performance and specifies a journalization API with methods necessary to support JOTM
        recovery operations.</p>
<p><b>URL: </b><a href="http://forge.objectweb.org/projects/howl/">http://forge.objectweb.org/projects/howl/</a></p>
<p><b>Project Licenses: </b>BSD</p></td></tr></table></div></li></ul></li>
<li>org.slf4j:slf4j-simple:jar:2.0.17 (test) <img alt="[Information]" id="_img89" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep88">
<table>
<tr>
<th>SLF4J Simple Provider</th></tr>
<tr>
<td>
<p><b>Description: </b>SLF4J Simple Provider</p>
<p><b>URL: </b><a href="http://www.slf4j.org">http://www.slf4j.org</a></p>
<p><b>Project Licenses: </b><a href="https://opensource.org/license/mit">MIT</a></p></td></tr></table></div>
<ul>
<li>org.slf4j:slf4j-api:jar:2.0.17 (test) <img alt="[Information]" id="_img91" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep90">
<table>
<tr>
<th>SLF4J API Module</th></tr>
<tr>
<td>
<p><b>Description: </b>The slf4j API</p>
<p><b>URL: </b><a href="http://www.slf4j.org">http://www.slf4j.org</a></p>
<p><b>Project Licenses: </b><a href="https://opensource.org/license/mit">MIT</a></p></td></tr></table></div></li></ul></li>
<li>com.h2database:h2:jar:2.2.224 (test) <img alt="[Information]" id="_img93" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep92">
<table>
<tr>
<th>H2 Database Engine</th></tr>
<tr>
<td>
<p><b>Description: </b>H2 Database Engine</p>
<p><b>URL: </b><a href="https://h2database.com">https://h2database.com</a></p>
<p><b>Project Licenses: </b><a href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>, <a href="https://opensource.org/licenses/eclipse-1.0.php">EPL 1.0</a></p></td></tr></table></div></li>
<li>org.jboss.narayana.jta:narayana-jta:jar:5.12.7.Final (test) <img alt="[Information]" id="_img95" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep94">
<table>
<tr>
<th>Narayana: ArjunaJTA narayana-jta</th></tr>
<tr>
<td>
<p><b>Description: </b>Narayana: ArjunaJTA narayana-jta (jta uber jar)</p>
<p><b>URL: </b><a href="http://www.jboss.org/jbosstm/narayana-jta-all/narayana-jta/">http://www.jboss.org/jbosstm/narayana-jta-all/narayana-jta/</a></p>
<p><b>Project Licenses: </b><a href="http://www.gnu.org/licenses/lgpl-2.1.html">LGPL 2.1</a></p></td></tr></table></div>
<ul>
<li>org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec:jar:1.0.0.Final (test) <img alt="[Information]" id="_img97" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep96">
<table>
<tr>
<th>Java(TM) EE Connector Architecture 1.7 API</th></tr>
<tr>
<td>
<p><b>Description: </b>JSR 322: Java(TM) EE Connector Architecture 1.7 API</p>
<p><b>URL: </b><a href="http://www.jboss.org/jboss-connector-api_1.7_spec">http://www.jboss.org/jboss-connector-api_1.7_spec</a></p>
<p><b>Project Licenses: </b><a href="http://repository.jboss.org/licenses/cddl.txt">Common Development and Distribution License</a>, <a href="http://repository.jboss.org/licenses/gpl-2.0-ce.txt">GNU General Public License, Version 2 with the Classpath Exception</a></p></td></tr></table></div></li></ul></li>
<li>org.jboss:jboss-transaction-spi:jar:8.0.0.Final (test) <img alt="[Information]" id="_img99" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep98">
<table>
<tr>
<th>JBoss Transaction SPI</th></tr>
<tr>
<td>
<p><b>Description: </b>The Java Transaction SPI classes</p>
<p><b>URL: </b><a href="http://www.jboss.org">http://www.jboss.org</a></p>
<p><b>Project Licenses: </b><a href="http://repository.jboss.org/licenses/cc0-1.0.txt">Public Domain</a></p></td></tr></table></div>
<ul>
<li>jakarta.resource:jakarta.resource-api:jar:2.0.0 (test) <img alt="[Information]" id="_img101" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep100">
<table>
<tr>
<th>jakarta.resource API</th></tr>
<tr>
<td>
<p><b>Description: </b>Jakarta Connectors 2.0</p>
<p><b>URL: </b><a href="https://github.com/eclipse-ee4j/jca-api">https://github.com/eclipse-ee4j/jca-api</a></p>
<p><b>Project Licenses: </b><a href="http://www.eclipse.org/legal/epl-2.0">EPL 2.0</a>, <a href="https://www.gnu.org/software/classpath/license.html">GPL2 w/ CPE</a></p></td></tr></table></div>
<ul>
<li>jakarta.annotation:jakarta.annotation-api:jar:2.0.0 (test) <img alt="[Information]" id="_img103" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep102">
<table>
<tr>
<th>Jakarta Annotations API</th></tr>
<tr>
<td>
<p><b>Description: </b>Jakarta Annotations API</p>
<p><b>URL: </b><a href="https://projects.eclipse.org/projects/ee4j.ca">https://projects.eclipse.org/projects/ee4j.ca</a></p>
<p><b>Project Licenses: </b><a href="http://www.eclipse.org/legal/epl-2.0">EPL 2.0</a>, <a href="https://www.gnu.org/software/classpath/license.html">GPL2 w/ CPE</a></p></td></tr></table></div></li></ul></li></ul></li>
<li>org.jboss.logging:jboss-logging:jar:3.4.3.Final (test) <img alt="[Information]" id="_img105" src="assets/images/icon-info-sml_4b59af4a660ca248.gif"/><div id="_dep104">
<table>
<tr>
<th>JBoss Logging 3</th></tr>
<tr>
<td>
<p><b>Description: </b>The JBoss Logging Framework</p>
<p><b>URL: </b><a href="http://www.jboss.org">http://www.jboss.org</a></p>
<p><b>Project Licenses: </b><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, version 2.0</a></p></td></tr></table></div></li></ul></li></ul></section></section><section><a id="Licenses"></a>
<h1>Licenses</h1>
<p><b>Apache License, version 2.0: </b>JBoss Logging 3</p>
<p><b>Common Development and Distribution License: </b>Java(TM) EE Connector Architecture 1.7 API</p>
<p><b>The Apache License, Version 2.0: </b>org.apiguardian:apiguardian-api, org.opentest4j:opentest4j</p>
<p><b>Eclipse Public License v2.0: </b>JUnit Jupiter (Aggregator), JUnit Jupiter API, JUnit Jupiter Engine, JUnit Jupiter Params, JUnit Platform Commons, JUnit Platform Engine API</p>
<p><b>Indiana University Extreme! Lab Software License, vesion 1.1.1: </b>MXP1: Xml Pull Parser 3rd Edition (XPP3)</p>
<p><b>GPL2 w/ CPE: </b>Jakarta Annotations API, jakarta.resource API, javax.transaction API</p>
<p><b>Public Domain: </b>JBoss Transaction SPI, MXP1: Xml Pull Parser 3rd Edition (XPP3)</p>
<p><b>BSD style: </b>XStream Core</p>
<p><b>BSD: </b>HOWL logger</p>
<p><b>Unknown: </b>ASM Commons, ASM Core, CLI, cglib, naming-common, naming-java</p>
<p><b>The MIT License: </b>mockito-core</p>
<p><b>Apache-2.0: </b>Apache Commons DBCP, Apache Commons Lang, Apache Commons Logging, Apache Commons Pool</p>
<p><b>Apache License, Version 2.0: </b>Byte Buddy (without dependencies), Byte Buddy agent, Objenesis</p>
<p><b>MIT: </b>SLF4J API Module, SLF4J Simple Provider</p>
<p><b>LGPL 2.1: </b>Narayana: ArjunaJTA narayana-jta</p>
<p><b>EPL 2.0: </b>Jakarta Annotations API, jakarta.resource API, javax.transaction API</p>
<p><b>EPL 1.0: </b>H2 Database Engine</p>
<p><b>GNU General Public License, Version 2 with the Classpath Exception: </b>Java(TM) EE Connector Architecture 1.7 API</p>
<p><b>MPL 2.0: </b>H2 Database Engine</p>
<p><b>The Apache Software License, Version 2.0: </b>Apache JAXB 2.1 Spec, Apache Log4j, Apache XBean :: Reflect, Commons JEXL, Geronimo Framework, Modules :: CLI, Geronimo Framework, Modules :: Common, Geronimo Framework, Modules :: Core, Geronimo Framework, Modules :: Crypto, Geronimo Framework, Modules :: J2EE, Geronimo Framework, Modules :: Kernel, Geronimo Framework, Modules :: Management API, Geronimo Framework, Modules :: System, Geronimo Plugins, Connector :: Transaction, Geronimo TxManager :: Transaction, J2EE Connector 1.5, J2EE Management 1.1, JTA 1.1, Streaming API for XML (STAX API 1.0)</p></section><section><a id="Dependency_File_Details"></a>
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
<td>asm-3.1.jar</td>
<td>43 kB</td>
<td>24</td>
<td>23</td>
<td>2</td>
<td>1.2</td>
<td>No</td></tr>
<tr>
<td>asm-commons-3.1.jar</td>
<td>32.7 kB</td>
<td>23</td>
<td>22</td>
<td>1</td>
<td>1.2</td>
<td>No</td></tr>
<tr>
<td>cglib-nodep-2.1_3.jar</td>
<td>324.2 kB</td>
<td>262</td>
<td>258</td>
<td>10</td>
<td>1.1</td>
<td>Yes</td></tr>
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
<td>xstream-1.3.jar</td>
<td>411.1 kB</td>
<td>360</td>
<td>330</td>
<td>21</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>commons-cli-1.0.jar</td>
<td>30.1 kB</td>
<td>27</td>
<td>20</td>
<td>1</td>
<td>1.1</td>
<td>Yes</td></tr>
<tr>
<td>commons-jexl-1.1.jar</td>
<td>132.2 kB</td>
<td>107</td>
<td>93</td>
<td>7</td>
<td>1.2</td>
<td>Yes</td></tr>
<tr>
<td>commons-logging-1.3.5.jar</td>
<td>73.7 kB</td>
<td>42</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>41</td>
<td>27</td>
<td>2</td>
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
<td>jakarta.annotation-api-2.0.0.jar</td>
<td>25.4 kB</td>
<td>29</td>
<td>16</td>
<td>4</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>jakarta.resource-api-2.0.0.jar</td>
<td>68.5 kB</td>
<td>113</td>
<td>89</td>
<td>6</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>jakarta.transaction-api-1.3.3.jar</td>
<td>15.4 kB</td>
<td>29</td>
<td>19</td>
<td>1</td>
<td>1.7</td>
<td>Yes</td></tr>
<tr>
<td>log4j-1.2.15.jar</td>
<td>391.8 kB</td>
<td>296</td>
<td>259</td>
<td>19</td>
<td>1.1</td>
<td>Yes</td></tr>
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
<td>commons-lang3-3.20.0.jar</td>
<td>713.9 kB</td>
<td>454</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>452</td>
<td>421</td>
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
<td>commons-pool2-2.13.0.jar</td>
<td>156.7 kB</td>
<td>103</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>101</td>
<td>85</td>
<td>3</td>
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
<td>geronimo-transaction-2.2.1.jar</td>
<td>71.7 kB</td>
<td>58</td>
<td>42</td>
<td>3</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-cli-2.2.1.jar</td>
<td>56.7 kB</td>
<td>60</td>
<td>42</td>
<td>4</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-common-2.2.1.jar</td>
<td>43.6 kB</td>
<td>61</td>
<td>46</td>
<td>2</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-core-2.2.1.jar</td>
<td>24.6 kB</td>
<td>30</td>
<td>15</td>
<td>2</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-crypto-2.2.1.jar</td>
<td>280.3 kB</td>
<td>226</td>
<td>195</td>
<td>18</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-kernel-2.2.1.jar</td>
<td>416.2 kB</td>
<td>288</td>
<td>266</td>
<td>14</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-management-2.2.1.jar</td>
<td>79.8 kB</td>
<td>138</td>
<td>121</td>
<td>4</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-system-2.2.1.jar</td>
<td>235 kB</td>
<td>163</td>
<td>128</td>
<td>16</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-j2ee-2.2.1.jar</td>
<td>34.8 kB</td>
<td>33</td>
<td>15</td>
<td>4</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-transaction-2.2.1.jar</td>
<td>13.5 kB</td>
<td>20</td>
<td>4</td>
<td>2</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-j2ee-connector_1.5_spec-2.0.0.jar</td>
<td>37.5 kB</td>
<td>78</td>
<td>62</td>
<td>6</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-j2ee-management_1.1_spec-1.0.1.jar</td>
<td>20.2 kB</td>
<td>46</td>
<td>33</td>
<td>2</td>
<td>1.5</td>
<td>No</td></tr>
<tr>
<td>geronimo-jaxb_2.1_spec-1.0.jar</td>
<td>78.5 kB</td>
<td>109</td>
<td>91</td>
<td>6</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-jta_1.1_spec-1.1.1.jar</td>
<td>16 kB</td>
<td>30</td>
<td>18</td>
<td>2</td>
<td>1.5</td>
<td>Yes</td></tr>
<tr>
<td>geronimo-stax-api_1.0_spec-1.0.1.jar</td>
<td>28.8 kB</td>
<td>48</td>
<td>34</td>
<td>3</td>
<td>1.4</td>
<td>Yes</td></tr>
<tr>
<td>xbean-reflect-3.7.jar</td>
<td>148.1 kB</td>
<td>133</td>
<td>118</td>
<td>2</td>
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
<td>jboss-transaction-spi-8.0.0.Final.jar</td>
<td>32.4 kB</td>
<td>51</td>
<td>37</td>
<td>4</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>jboss-logging-3.4.3.Final.jar</td>
<td>60.8 kB</td>
<td>47</td>
<td>35</td>
<td>1</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>narayana-jta-5.12.7.Final.jar</td>
<td>955.2 kB</td>
<td>641</td>
<td>496</td>
<td>83</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>jboss-connector-api_1.7_spec-1.0.0.Final.jar</td>
<td>73.7 kB</td>
<td>120</td>
<td>103</td>
<td>6</td>
<td>1.6</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-5.14.1.jar</td>
<td>6.4 kB</td>
<td>5</td>
<td>1</td>
<td>1</td>
<td>9</td>
<td>No</td></tr>
<tr>
<td>junit-jupiter-api-5.14.1.jar</td>
<td>242.5 kB</td>
<td>217</td>
<td>202</td>
<td>8</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-engine-5.14.1.jar</td>
<td>343.2 kB</td>
<td>179</td>
<td>162</td>
<td>9</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-jupiter-params-5.14.1.jar</td>
<td>663.1 kB</td>
<td>433</td>
<td>399</td>
<td>22</td>
<td>1.8</td>
<td>Yes</td></tr>
<tr>
<td>junit-platform-commons-1.14.1.jar</td>
<td>164.4 kB</td>
<td>105</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>94</td>
<td>78</td>
<td>10</td>
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
<td>junit-platform-engine-1.14.1.jar</td>
<td>271.7 kB</td>
<td>191</td>
<td>172</td>
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
<td>howl-1.0.1-1.jar</td>
<td>80 kB</td>
<td>60</td>
<td>42</td>
<td>3</td>
<td>1.4</td>
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
<td>slf4j-api-2.0.17.jar</td>
<td>69.9 kB</td>
<td>71</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>69</td>
<td>55</td>
<td>4</td>
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
<td>slf4j-simple-2.0.17.jar</td>
<td>15.7 kB</td>
<td>22</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td>   • Root</td>
<td>-</td>
<td>20</td>
<td>6</td>
<td>1</td>
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
<td>naming-common-5.0.28.jar</td>
<td>28 kB</td>
<td>34</td>
<td>20</td>
<td>2</td>
<td>1.2</td>
<td>Yes</td></tr>
<tr>
<td>naming-java-5.0.28.jar</td>
<td>2.1 kB</td>
<td>9</td>
<td>1</td>
<td>1</td>
<td>1.2</td>
<td>Yes</td></tr>
<tr>
<td>xpp3_min-1.1.4c.jar</td>
<td>25 kB</td>
<td>12</td>
<td>3</td>
<td>2</td>
<td>1.1</td>
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
<td>52</td>
<td>14.6 MB</td>
<td>10210</td>
<td>9143</td>
<td>528</td>
<td>9</td>
<td>48</td></tr>
<tr>
<td>compile: 3</td>
<td>compile: 245.8 kB</td>
<td>compile: 174</td>
<td>compile: 131</td>
<td>compile: 6</td>
<td>1.8</td>
<td>compile: 3</td></tr>
<tr>
<td>test: 49</td>
<td>test: 14.4 MB</td>
<td>test: 10036</td>
<td>test: 9012</td>
<td>test: 522</td>
<td>9</td>
<td>test: 45</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-convergence"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/dependency-convergence.html -->

<!-- page_index: 19 -->

# Dependency Convergence

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h1>Dependency Convergence</h1>
<table><caption>
<b>Legend:</b>
</caption>
<tr>
<td><img alt="[Error]" src="assets/images/icon-error-sml_27bfe13c725c312f.gif"/></td>
<td>At least one dependency has a differing version of the dependency or has SNAPSHOT dependencies.</td></tr></table>
<table><caption>
<b>Statistics:</b>
</caption>
<tr>
<th>Number of dependencies (NOD):</th>
<td>52</td></tr>
<tr>
<th>Number of unique artifacts (NOA):</th>
<td>57</td></tr>
<tr>
<th>Number of version-conflicting artifacts (NOC):</th>
<td>2</td></tr>
<tr>
<th>Number of SNAPSHOT artifacts (NOS):</th>
<td>0</td></tr>
<tr>
<th>Convergence (NOD/NOA):</th>
<td><img alt="[Error]" src="assets/images/icon-error-sml_27bfe13c725c312f.gif"/> <b>91 %</b></td></tr>
<tr>
<th>Ready for release (100% convergence and no SNAPSHOTS):</th>
<td><img alt="[Error]" src="assets/images/icon-error-sml_27bfe13c725c312f.gif"/> <b>Error</b> You do not have 100% convergence.</td></tr></table></section><section>
<h2>Dependencies used in this project</h2><section>
<h3>org.jboss:jboss-transaction-spi</h3>
<table>
<tr>
<td><img alt="[Error]" src="assets/images/icon-error-sml_27bfe13c725c312f.gif"/></td>
<td>
<table>
<tr>
<td>7.6.1.Final</td>
<td>
<ol>org.apache.commons:commons-dbcp2:jar:2.14.0
\- org.jboss.narayana.jta:narayana-jta:jar:5.12.7.Final:test
   \- org.jboss:jboss-transaction-spi:jar:7.6.1.Final:test

</ol></td></tr>
<tr>
<td>8.0.0.Final</td>
<td>
<ol>org.apache.commons:commons-dbcp2:jar:2.14.0
\- org.jboss:jboss-transaction-spi:jar:8.0.0.Final:test

</ol></td></tr></table></td></tr></table></section><section>
<h3>org.slf4j:slf4j-api</h3>
<table>
<tr>
<td><img alt="[Error]" src="assets/images/icon-error-sml_27bfe13c725c312f.gif"/></td>
<td>
<table>
<tr>
<td>1.4.3</td>
<td>
<ol>org.apache.commons:commons-dbcp2:jar:2.14.0
\- org.apache.geronimo.modules:geronimo-transaction:jar:2.2.1:test
   \- org.apache.geronimo.components:geronimo-transaction:jar:2.2.1:test
      \- org.slf4j:slf4j-api:jar:1.4.3:test

</ol></td></tr>
<tr>
<td>1.5.5</td>
<td>
<ol>org.apache.commons:commons-dbcp2:jar:2.14.0
\- org.apache.geronimo.modules:geronimo-transaction:jar:2.2.1:test
   \- org.apache.geronimo.framework:geronimo-core:jar:2.2.1:test
      +- org.apache.geronimo.framework:geronimo-system:jar:2.2.1:test
      |  +- org.apache.geronimo.framework:geronimo-cli:jar:2.2.1:test
      |  |  \- org.slf4j:slf4j-api:jar:1.5.5:test
      |  +- org.apache.geronimo.framework:geronimo-common:jar:2.2.1:test
      |  |  \- org.slf4j:slf4j-api:jar:1.5.5:test
      |  +- org.apache.geronimo.framework:geronimo-crypto:jar:2.2.1:test
      |  |  \- org.slf4j:slf4j-api:jar:1.5.5:test
      |  +- org.apache.geronimo.framework:geronimo-kernel:jar:2.2.1:test
      |  |  \- org.slf4j:slf4j-api:jar:1.5.5:test
      |  \- org.slf4j:slf4j-api:jar:1.5.5:test
      +- org.apache.geronimo.framework:geronimo-management:jar:2.2.1:test
      |  \- org.slf4j:slf4j-api:jar:1.5.5:test
      \- org.slf4j:slf4j-api:jar:1.5.5:test

</ol></td></tr>
<tr>
<td>2.0.17</td>
<td>
<ol>org.apache.commons:commons-dbcp2:jar:2.14.0
\- org.slf4j:slf4j-simple:jar:2.0.17:test
   \- org.slf4j:slf4j-api:jar:2.0.17:test

</ol></td></tr></table></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/ci-management.html -->

<!-- page_index: 20 -->

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
<pre><a href="https://github.com/apache/commons-dbcp/actions">https://github.com/apache/commons-dbcp/actions</a></pre></section><section><a id="Notifiers"></a>
<h1>Notifiers</h1>
<p>No notifiers are defined. Please check back at a later date.</p></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="distribution-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/distribution-management.html -->

<!-- page_index: 21 -->

# Overview

|  |  |
| --- | --- |
|  | Overview The following is the distribution management information used by this project.  Repository - apache.releases.https<https://repository.apache.org/service/local/staging/deploy/maven2>  Snapshot Repository - apache.snapshots.https<https://repository.apache.org/content/repositories/snapshots>  Site - apache.website scm:svn:https://svn.apache.org/repos/infra/websites/production/commons/content/proper/commons-dbcp/ |

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/project-reports.html -->

<!-- page_index: 22 -->

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
<td><a href="https://commons.apache.org/proper/commons-dbcp/apidocs/index.html">Javadoc</a></td>
<td>Javadoc API documentation.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-dbcp/xref/index.html">Source Xref</a></td>
<td>HTML based, cross-reference version of Java source code.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-dbcp/xref-test/index.html">Test Source Xref</a></td>
<td>HTML based, cross-reference version of Java test source code.</td></tr>
<tr>
<td><a href="#surefire">Surefire</a></td>
<td>Report on the test results of the project.</td></tr>
<tr>
<td><a href="#rat-report">RAT Report</a></td>
<td>Report on compliance to license related source code policies</td></tr>
<tr>
<td><a href="#japicmp">japicmp</a></td>
<td>Comparing source compatibility of commons-dbcp2-2.14.0.jar against commons-dbcp2-2.13.0.jar</td></tr>
<tr>
<td><a href="#spotbugs">SpotBugs</a></td>
<td>Generates a source code report with the SpotBugs Library.</td></tr>
<tr>
<td><a href="#checkstyle">Checkstyle</a></td>
<td>Report on coding style conventions.</td></tr>
<tr>
<td><a href="#pmd">PMD</a></td>
<td>Verification of coding rules.</td></tr>
<tr>
<td><a href="#cpd">CPD</a></td>
<td>Duplicate code detection.</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/jira-changes.html -->

<!-- page_index: 23 -->

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
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-434">DBCP-434</a></td>
<td>-</td>
<td>Disable JMX for Statement Pool</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-433">DBCP-433</a></td>
<td>-</td>
<td>Connection leak when SQLException is thrown while enlisting in XA transaction</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-432">DBCP-432</a></td>
<td>-</td>
<td>BasicDataSource createDataSource can return partially initialized DataSource</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-428">DBCP-428</a></td>
<td>-</td>
<td>Unsuccessful Connection enlistment in XA Transaction ignored by TransactionContext</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-426">DBCP-426</a></td>
<td>-</td>
<td>DBCP should allow clients to mark connections as invalid</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-420">DBCP-420</a></td>
<td>-</td>
<td>InstanceKeyDataSource discards native SQLException when given password does not match password used to create the connection</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-412">DBCP-412</a></td>
<td>-</td>
<td>dbcp2.PoolableConnection.close raises NullPointerException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-435">DBCP-435</a></td>
<td>-</td>
<td>[PATCH] Friendly BasicDataSourceFactory</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-424">DBCP-424</a></td>
<td>-</td>
<td>validateLifetime causes needless warnings about swallowed exceptions to be logged</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-423">DBCP-423</a></td>
<td>-</td>
<td>PoolingDataSource should implement Closeable</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-422">DBCP-422</a></td>
<td>-</td>
<td>Update Apache Commons Logging to 1.2 from 1.1.3</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-418">DBCP-418</a></td>
<td>-</td>
<td>Cannot Disable JMX</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-417">DBCP-417</a></td>
<td>-</td>
<td>BasicManagedDataSource does not free connection after transaction is commited</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-414">DBCP-414</a></td>
<td>-</td>
<td>PoolablePreparedStatement can get closed while it's being used</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-425">DBCP-425</a></td>
<td>-</td>
<td>Example code for pooling driver should be fixed.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-411">DBCP-411</a></td>
<td>-</td>
<td>BasicManagedDataSource - unregister from JMX on close()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-410">DBCP-410</a></td>
<td>-</td>
<td>build.xml: wrong path for javadoc.overview</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-404">DBCP-404</a></td>
<td>-</td>
<td>Mutable fields should be private</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-403">DBCP-403</a></td>
<td>-</td>
<td>DelegatingStatement.close() fails with NPE if statement is null</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-385">DBCP-385</a></td>
<td>-</td>
<td>Please update to support Java 7 and JDBC 4.1</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-384">DBCP-384</a></td>
<td>-</td>
<td>PoolingDriver.accessToUnderlyingConnectionAllowed is thread-hostile</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-358">DBCP-358</a></td>
<td>-</td>
<td>Equals implementations in DelegatingXxx classes are not symmetric</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-351">DBCP-351</a></td>
<td>-</td>
<td>setAutoCommit called too many times</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-322">DBCP-322</a></td>
<td>-</td>
<td>CPDSConnectionFactory.validateObject(Object) ignores Throwable</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-317">DBCP-317</a></td>
<td>-</td>
<td>Findbugs: Class doesn't override equals in superclass</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-143">DBCP-143</a></td>
<td>-</td>
<td>[dbcp] SQLNestedException thrown by server causes client ClassNotFoundException.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-406">DBCP-406</a></td>
<td>-</td>
<td>Support for caching statements with autogenerated keys</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-402">DBCP-402</a></td>
<td>-</td>
<td>Add a way to set an instance of java.sql.Driver directly on org.apache.commons.dbcp2.BasicDataSource</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-373">DBCP-373</a></td>
<td>-</td>
<td>Ability to configure upper bound on total number of connections managed by pooled data sources across all keys (user/password).</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-364">DBCP-364</a></td>
<td>-</td>
<td>BasicDataSourceFactory#createDataSource return signature should be BasicDataSourceFactory so that caller can invoke methods not declared in DataSource (e.g., close())</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-357">DBCP-357</a></td>
<td>-</td>
<td>Connection validationQuery mechanism should be replaced by new method connection#isValid()</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-340">DBCP-340</a></td>
<td>-</td>
<td>setQueryTimeout(int)  should be set through property.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-319">DBCP-319</a></td>
<td>-</td>
<td>Make private fields final where possible</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-300">DBCP-300</a></td>
<td>-</td>
<td>remove synchronize access of createDataSource</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-260">DBCP-260</a></td>
<td>-</td>
<td>borrowObject from the AbandonedObjectPool hangs on a wait() method when the WHEN_EXHAUSTED_BLOCK is set</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-246">DBCP-246</a></td>
<td>-</td>
<td>Logging For DBCP</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-234">DBCP-234</a></td>
<td>-</td>
<td>Only set *configured* default values for Connection</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-210">DBCP-210</a></td>
<td>-</td>
<td>Have dbcp close pooled prepared statements after some settable time limit</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-180">DBCP-180</a></td>
<td>-</td>
<td>[dbcp] Dbcp doesn't meet JDBC specification</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-177">DBCP-177</a></td>
<td>-</td>
<td>[dbcp] redesign to use dbcp with security manager</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-156">DBCP-156</a></td>
<td>-</td>
<td>[dbcp] Specifying the maximum lifetime of a connection</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-154">DBCP-154</a></td>
<td>-</td>
<td>[dbcp] PoolableConnectionFactory.validateConnection() should log exception message</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-368">DBCP-368</a></td>
<td>-</td>
<td>determine which connections to hold in pool by relative value</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-292">DBCP-292</a></td>
<td>-</td>
<td>Adds an mbean for exposing metrics around a BasicDataSource via JMX</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-249">DBCP-249</a></td>
<td>-</td>
<td>Validate connection only on create.</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-229">DBCP-229</a></td>
<td>-</td>
<td>Track callers of active connections for debugging</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-223">DBCP-223</a></td>
<td>-</td>
<td>Auto-alert of connection pool critical events?</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-219">DBCP-219</a></td>
<td>-</td>
<td>how to kill a connection from the connection pool without shutting down the connection pool</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-400">DBCP-400</a></td>
<td>-</td>
<td>The documentation of maxOpenPreparedStatements parameter seems to be wrong</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-391">DBCP-391</a></td>
<td>-</td>
<td>Close on invalid connections throws unexpected exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-382">DBCP-382</a></td>
<td>-</td>
<td>Could not set flag "accessToUnderlyingConnectionAllowed" in "context.xml" for DriverAdapterCPDS/PerUserPoolDataSource</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-376">DBCP-376</a></td>
<td>-</td>
<td>Thread safety issue</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-372">DBCP-372</a></td>
<td>-</td>
<td>Statement Leak occurs when batch update is used.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-369">DBCP-369</a></td>
<td>-</td>
<td>Exception when using SharedPoolDataSource concurrently</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-355">DBCP-355</a></td>
<td>-</td>
<td>DataSourceXAConnectionFactory does not store the XAConnection</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-341">DBCP-341</a></td>
<td>-</td>
<td>LocalXAConnectionFactory does not properly check if Xid is equal to currentXid when resuming</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-309">DBCP-309</a></td>
<td>-</td>
<td>First example for FSContext is invalid</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1, 1.4.1, 1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-380">DBCP-380</a></td>
<td>-</td>
<td>DelegatingConnection isWrapperFor dies on older JDBC drivers</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1, 1.4.1, 1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-347">DBCP-347</a></td>
<td>-</td>
<td>DelegatingStatement class has incomplete isWrapperFor method</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1, 1.4.1, 1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-405">DBCP-405</a></td>
<td>-</td>
<td>getAutoCommit in PoolableConnectionFactory</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1, 1.4.1, 1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-396">DBCP-396</a></td>
<td>-</td>
<td>AbandonedConfig.setLogWriter() never used</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1, 1.4.1, 1.5.1, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBCP-392">DBCP-392</a></td>
<td>-</td>
<td>Remove Occurrences of Multiple Statements on One Line</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/surefire.html -->

<!-- page_index: 24 -->

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
<td>1605</td>
<td>0</td>
<td>0</td>
<td>9</td>
<td>99.4%</td>
<td>90.68 s</td></tr></table>
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
<td><a href="#surefire--org.apache.commons.dbcp2.datasources">org.apache.commons.dbcp2.datasources</a></td>
<td>268</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>10.73 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2">org.apache.commons.dbcp2</a></td>
<td>1039</td>
<td>0</td>
<td>0</td>
<td>7</td>
<td>99.3%</td>
<td>49.17 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed">org.apache.commons.dbcp2.managed</a></td>
<td>275</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>99.3%</td>
<td>29.90 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.cpdsadapter">org.apache.commons.dbcp2.cpdsadapter</a></td>
<td>23</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.877 s</td></tr></table>
<p>Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.</p><section><a id="org.apache.commons.dbcp2.datasources"></a>
<h3>org.apache.commons.dbcp2.datasources</h3>
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
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testsharedpooldatasource"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testsharedpooldatasource">TestSharedPoolDataSource</a></td>
<td>37</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>5.963 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testperuserpooldatasource"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testperuserpooldatasource">TestPerUserPoolDataSource</a></td>
<td>146</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>4.618 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.chararraytest"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.chararraytest">CharArrayTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.020 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testuserpasskey"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testuserpasskey">TestUserPassKey</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testkeyedcpdsconnectionfactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testkeyedcpdsconnectionfactory">TestKeyedCPDSConnectionFactory</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.004 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.userpasskeytest"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.userpasskeytest">UserPassKeyTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testcpdsconnectionfactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testcpdsconnectionfactory">TestCPDSConnectionFactory</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testinstancekeydatasource"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testinstancekeydatasource">TestInstanceKeyDataSource</a></td>
<td>34</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.064 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.pooledconnectionmanagertest"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.pooledconnectionmanagertest">PooledConnectionManagerTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testfactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testfactory">TestFactory</a></td>
<td>26</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.051 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testpoolkey"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.datasources.testpoolkey">TestPoolKey</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2"></a>
<h3>org.apache.commons.dbcp2</h3>
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
<td><a href="#surefire--org.apache.commons.dbcp2.testlifetimeexceededexception"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testlifetimeexceededexception">TestLifetimeExceededException</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdrivermanagerconnectionfactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdrivermanagerconnectionfactory">TestDriverManagerConnectionFactory</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.217 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testparallelcreationwithnoidle"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testparallelcreationwithnoidle">TestParallelCreationWithNoIdle</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>2.175 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testutils"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testutils">TestUtils</a></td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdatasourceconnectionfactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdatasourceconnectionfactory">TestDataSourceConnectionFactory</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testsqlexceptionlist"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testsqlexceptionlist">TestSQLExceptionList</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.004 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdriverconnectionfactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdriverconnectionfactory">TestDriverConnectionFactory</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolableconnection"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolableconnection">TestPoolableConnection</a></td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.241 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingstatement"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingstatement">TestDelegatingStatement</a></td>
<td>57</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.044 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testconstants"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testconstants">TestConstants</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolingdriver"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolingdriver">TestPoolingDriver</a></td>
<td>29</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>3.164 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolingdatasource"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolingdatasource">TestPoolingDataSource</a></td>
<td>32</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>3.107 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.jdbc41bridgetest"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.jdbc41bridgetest">Jdbc41BridgeTest</a></td>
<td>11</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.051 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasourcefactory"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasourcefactory">TestBasicDataSourceFactory</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testabandonedbasicdatasource"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testabandonedbasicdatasource">TestAbandonedBasicDataSource</a></td>
<td>84</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>98.8%</td>
<td>16.87 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingcallablestatement"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingcallablestatement">TestDelegatingCallableStatement</a></td>
<td>124</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.257 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testjndi"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testjndi">TestJndi</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.013 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtkey"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtkey">TestPStmtKey</a></td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasource"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasource">TestBasicDataSource</a></td>
<td>73</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>98.6%</td>
<td>6.266 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingdatabasemetadata"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingdatabasemetadata">TestDelegatingDatabaseMetaData</a></td>
<td>181</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.094 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasourcemxbean"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasourcemxbean">TestBasicDataSourceMXBean</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset">TestDelegatingResultSet</a></td>
<td>196</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>98.0%</td>
<td>0.043 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolingconnection"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpoolingconnection">TestPoolingConnection</a></td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testabandonedtrace"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testabandonedtrace">TestAbandonedTrace</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingconnection"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingconnection">TestDelegatingConnection</a></td>
<td>38</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.028 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtpooling"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtpooling">TestPStmtPooling</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testlistexception"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testlistexception">TestListException</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingpreparedstatement"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingpreparedstatement">TestDelegatingPreparedStatement</a></td>
<td>61</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.037 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtpoolingbasicdatasource"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtpoolingbasicdatasource">TestPStmtPoolingBasicDataSource</a></td>
<td>80</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>98.8%</td>
<td>16.54 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed"></a>
<h3>org.apache.commons.dbcp2.managed</h3>
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
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanagedconnectioncachedstate"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanagedconnectioncachedstate">TestManagedConnectionCachedState</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testdatasourcexaconnectionfactory"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testdatasourcexaconnectionfactory">TestDataSourceXAConnectionFactory</a></td>
<td>74</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>98.6%</td>
<td>6.102 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testtransactioncontext"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testtransactioncontext">TestTransactionContext</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanageddatasource"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanageddatasource">TestManagedDataSource</a></td>
<td>37</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>2.945 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testpoolablemanagedconnection"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testpoolablemanagedconnection">TestPoolableManagedConnection</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testlocalxaresource"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testlocalxaresource">TestLocalXaResource</a></td>
<td>25</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.004 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testbasicmanageddatasource"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testbasicmanageddatasource">TestBasicManagedDataSource</a></td>
<td>85</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>98.8%</td>
<td>6.186 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanagedconnection"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanagedconnection">TestManagedConnection</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.005 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanageddatasourceintx"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testmanageddatasourceintx">TestManagedDataSourceInTx</a></td>
<td>43</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>3.195 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testconnectionwithnarayana"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testconnectionwithnarayana">TestConnectionWithNarayana</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>11.45 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testsynchronizationorder"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testsynchronizationorder">TestSynchronizationOrder</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.cpdsadapter"></a>
<h3>org.apache.commons.dbcp2.cpdsadapter</h3>
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
<td><a href="#surefire--org.apache.commons.dbcp2.cpdsadapter.testdriveradaptercpds"><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.dbcp2.cpdsadapter.testdriveradaptercpds">TestDriverAdapterCPDS</a></td>
<td>23</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.877 s</td></tr></table></section>
</section><section><a id="Test_Cases"></a>
<h2>Test Cases</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p><section><a id="org.apache.commons.dbcp2.managed.TestManagedConnectionCachedState"></a>
<h3>TestManagedConnectionCachedState</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedConnectionCachedState.testConnectionCachedState"></a>testConnectionCachedState</td>
<td>0.005 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestLifetimeExceededException"></a>
<h3>TestLifetimeExceededException</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestLifetimeExceededException.testLifetimeExceededException"></a>testLifetimeExceededException</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestLifetimeExceededException.testLifetimeExceededExceptionNoMessage"></a>testLifetimeExceededExceptionNoMessage</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS"></a>
<h3>TestDriverAdapterCPDS</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetConnectionProperties"></a>testSetConnectionProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testGetParentLogger"></a>testGetParentLogger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testGettersAndSetters"></a>testGettersAndSetters</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetConnectionPropertiesNull"></a>testSetConnectionPropertiesNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetPasswordNullWithConnectionProperties"></a>testSetPasswordNullWithConnectionProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetPasswordNull"></a>testSetPasswordNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetPasswordThenModCharArray"></a>testSetPasswordThenModCharArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testClose"></a>testClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testNullValidationQuery"></a>testNullValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testCloseWithUserName"></a>testCloseWithUserName</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testGetReference"></a>testGetReference</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testDeprecatedAccessors"></a>testDeprecatedAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetConnectionPropertiesConnectionCalled"></a>testSetConnectionPropertiesConnectionCalled</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testToStringWithoutConnectionProperties"></a>testToStringWithoutConnectionProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetUserNull"></a>testSetUserNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testDbcp367"></a>testDbcp367</td>
<td>0.871 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSimpleWithUsername"></a>testSimpleWithUsername</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testGetObjectInstanceChangeDescription"></a>testGetObjectInstanceChangeDescription</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testGetObjectInstanceNull"></a>testGetObjectInstanceNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testGetObjectInstance"></a>testGetObjectInstance</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testSetUserNullWithConnectionProperties"></a>testSetUserNullWithConnectionProperties</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.cpdsadapter.TestDriverAdapterCPDS.testIncorrectPassword"></a>testIncorrectPassword</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource"></a>
<h3>TestSharedPoolDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testThreaded"></a>testThreaded</td>
<td>2.998 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testPoolPreparedStatements"></a>testPoolPreparedStatements</td>
<td>0.009 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testOpening"></a>testOpening</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testClosingWithUserName"></a>testClosingWithUserName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testChangePassword"></a>testChangePassword</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testPoolPrepareCall"></a>testPoolPrepareCall</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testPoolPrepareStatement"></a>testPoolPrepareStatement</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testMaxWaitMillis"></a>testMaxWaitMillis</td>
<td>1.009 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testClosePool"></a>testClosePool</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testClosing"></a>testClosing</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testDbcp369"></a>testDbcp369</td>
<td>0.474 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testDbcp597"></a>testDbcp597</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testSimpleWithUsername"></a>testSimpleWithUsername</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testPoolPreparedCalls"></a>testPoolPreparedCalls</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testSimple2"></a>testSimple2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testSimple"></a>testSimple</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testMultipleThreads1"></a>testMultipleThreads1</td>
<td>0.304 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testMultipleThreads2"></a>testMultipleThreads2</td>
<td>1.007 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestSharedPoolDataSource.testIncorrectPassword"></a>testIncorrectPassword</td>
<td>0.007 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDriverManagerConnectionFactory"></a>
<h3>TestDriverManagerConnectionFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerInitWithCredentials"></a>testDriverManagerInitWithCredentials</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerWithoutPassword"></a>testDriverManagerWithoutPassword</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerWithoutCredentials"></a>testDriverManagerWithoutCredentials</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerInitWithEmptyProperties"></a>testDriverManagerInitWithEmptyProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerInitWithProperties"></a>testDriverManagerInitWithProperties</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerWithoutUser"></a>testDriverManagerWithoutUser</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverManagerConnectionFactory.testDriverManagerCredentialsInUrl"></a>testDriverManagerCredentialsInUrl</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory"></a>
<h3>TestDataSourceXAConnectionFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testThreaded"></a>testThreaded</td>
<td>3.015 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testNoRsetClose"></a>testNoRsetClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testOpening"></a>testOpening</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testClosing"></a>testClosing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testBackPointers"></a>testBackPointers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testMaxTotal"></a>testMaxTotal</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testClearWarnings"></a>testClearWarnings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testSimple2"></a>testSimple2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEmptyValidationQuery"></a>testEmptyValidationQuery</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCreateConnectionFactoryWithConnectionFactoryClassName"></a>testCreateConnectionFactoryWithConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testValidationQueryTimoutFail"></a>testValidationQueryTimoutFail</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testConcurrentInvalidateBorrow"></a>testConcurrentInvalidateBorrow</td>
<td>0.023 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testSetValidationTestProperties"></a>testSetValidationTestProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCreateConnectionFactoryWithoutConnectionFactoryClassName"></a>testCreateConnectionFactoryWithoutConnectionFactoryClassName</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testRollbackReadOnly"></a>testRollbackReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testdatasourcexaconnectionfactory.testevict"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEvict"></a><a href="#surefire--org.apache.commons.dbcp2.managed.testdatasourcexaconnectionfactory.testevict">testEvict</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEvict');"><span id="org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEvict-off"> + </span><span id="org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEvict-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testStart"></a>testStart</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testPropertyTestOnReturn"></a>testPropertyTestOnReturn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testValidationQueryTimeoutSucceed"></a>testValidationQueryTimeoutSucceed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testStartInitializes"></a>testStartInitializes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testMaxTotalZero"></a>testMaxTotalZero</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testConnectionMBeansDisabled"></a>testConnectionMBeansDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testMaxConnLifetimeExceeded"></a>testMaxConnLifetimeExceeded</td>
<td>0.503 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testValidationQueryTimeoutNegative"></a>testValidationQueryTimeoutNegative</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testPoolCloseRTE"></a>testPoolCloseRTE</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testInstanceNotFoundExceptionLogSuppressed"></a>testInstanceNotFoundExceptionLogSuppressed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testSetAutoCommitTrueOnClose"></a>testSetAutoCommitTrueOnClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testConcurrentInitBorrow"></a>testConcurrentInitBorrow</td>
<td>0.489 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testDeprecatedAccessors"></a>testDeprecatedAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testManualConnectionEvict"></a>testManualConnectionEvict</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testValidationQueryTimeoutZero"></a>testValidationQueryTimeoutZero</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testMaxConnLifetimeExceededMutedLog"></a>testMaxConnLifetimeExceededMutedLog</td>
<td>0.505 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEmptyInitConnectionSql"></a>testEmptyInitConnectionSql</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testDriverClassLoader"></a>testDriverClassLoader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testJmxDisabled"></a>testJmxDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testInitialSize"></a>testInitialSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testInvalidValidationQuery"></a>testInvalidValidationQuery</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testRestart"></a>testRestart</td>
<td>0.206 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testNoAccessToUnderlyingConnectionAllowed"></a>testNoAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testPoolCloseCheckedException"></a>testPoolCloseCheckedException</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCreateDataSourceCleanupEvictor"></a>testCreateDataSourceCleanupEvictor</td>
<td>1.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testCreateDataSourceCleanupThreads"></a>testCreateDataSourceCleanupThreads</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testDefaultCatalog"></a>testDefaultCatalog</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testInvalidateConnection"></a>testInvalidateConnection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testSetProperties"></a>testSetProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testMutateAbandonedConfig"></a>testMutateAbandonedConfig</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testDisconnectionIgnoreSqlCodes"></a>testDisconnectionIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testUnwrap"></a>testUnwrap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testJmxDoesNotExposePassword"></a>testJmxDoesNotExposePassword</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testInvalidConnectionInitSqlCollection"></a>testInvalidConnectionInitSqlCollection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testDisconnectSqlCodes"></a>testDisconnectSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testInvalidConnectionInitSqlList"></a>testInvalidConnectionInitSqlList</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testIsClosedFailure"></a>testIsClosedFailure</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testPhysicalClose"></a>testPhysicalClose</td>
<td>0.006 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestParallelCreationWithNoIdle"></a>
<h3>TestParallelCreationWithNoIdle</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestParallelCreationWithNoIdle.testMassiveConcurrentInitBorrow"></a>testMassiveConcurrentInitBorrow</td>
<td>2.175 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestUtils"></a>
<h3>TestUtils</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsNoOverlap"></a>testCheckForConflictsNoOverlap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testClassLoads"></a>testClassLoads</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsWith2Overlap"></a>testCheckForConflictsWith2Overlap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsBothCollectionsNull"></a>testCheckForConflictsBothCollectionsNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsEmptyCollections"></a>testCheckForConflictsEmptyCollections</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsFirstCollectionNull"></a>testCheckForConflictsFirstCollectionNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testIsDisconnectionSqlCode"></a>testIsDisconnectionSqlCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsSecondCollectionNull"></a>testCheckForConflictsSecondCollectionNull</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestUtils.testCheckForConflictsWith1Overlap"></a>testCheckForConflictsWith1Overlap</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource"></a>
<h3>TestPerUserPoolDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testThreaded"></a>testThreaded</td>
<td>3.113 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testHashing"></a>testHashing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnCreateMapNotInitialized"></a>testPerUserTestOnCreateMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultTransactionIsolationWithUserMapInitialized"></a>testPerUserDefaultTransactionIsolationWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnCreateWithUserMapNotInitialized"></a>testPerUserTestOnCreateWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultReadOnlyWithUserMapNotInitializedMissingKey"></a>testPerUserDefaultReadOnlyWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnBorrowWithUserMapNotInitialized"></a>testPerUserTestOnBorrowWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnReturnMapInitialized"></a>testPerUserTestOnReturnMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserSoftMinEvictableIdleDurationMapInitialized"></a>testPerUserSoftMinEvictableIdleDurationMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinIdleWithUserMapNotInitializedMissingKey"></a>testPerUserMinIdleWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnCreateWithUserMapNotInitializedMissingKey"></a>testPerUserTestOnCreateWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxIdleWithUserMapNotInitializedMissingKey"></a>testPerUserMaxIdleWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultAutoCommitWithUserMapNotInitializedMissingKey"></a>testPerUserDefaultAutoCommitWithUserMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserNumTestsPerEvictionRunWithUserMapNotInitialized"></a>testPerUserNumTestsPerEvictionRunWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnReturnWithUserMapNotInitialized"></a>testPerUserTestOnReturnWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDurationBetweenEvictionRunsMapNotInitializedMissingKey"></a>testPerUserDurationBetweenEvictionRunsMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxIdleWithUserMapInitialized"></a>testPerUserMaxIdleWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMethods"></a>testPerUserMethods</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserEvictionPolicyClassNameWithUserMapInitialized"></a>testPerUserEvictionPolicyClassNameWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testOpening"></a>testOpening</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserLifoWithUserMapNotInitializedMissingKey"></a>testPerUserLifoWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnReturnWithUserMapInitialized"></a>testPerUserTestOnReturnWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinEvictableIdleTimeMillisWithUserMapInitialized"></a>testPerUserMinEvictableIdleTimeMillisWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserLifoWithUserMapNotInitialized"></a>testPerUserLifoWithUserMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserEvictionPolicyClassNameMapNotInitializedMissingKey"></a>testPerUserEvictionPolicyClassNameMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserNumTestsPerEvictionRunWithUserMapNotInitializedMissingKey"></a>testPerUserNumTestsPerEvictionRunWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxWaitMillisWithUserMapNotInitializedDeprecated"></a>testPerUserMaxWaitMillisWithUserMapNotInitializedDeprecated</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinIdleMapInitialized"></a>testPerUserMinIdleMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserNumTestsPerEvictionRunMapInitialized"></a>testPerUserNumTestsPerEvictionRunMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testSerialization"></a>testSerialization</td>
<td>0.017 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinEvictableIdleDurationMapInitialized"></a>testPerUserMinEvictableIdleDurationMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnReturnWithUserMapNotInitializedMissingKey"></a>testPerUserTestOnReturnWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestWhileIdleWithUserMapInitialized"></a>testPerUserTestWhileIdleWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinEvictableIdleDurationMapNotInitializedMissingKey"></a>testPerUserMinEvictableIdleDurationMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinEvictableIdleTimeMillisWithUserMapNotInitializedMissingKey"></a>testPerUserMinEvictableIdleTimeMillisWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestWhileIdleMapNotInitialized"></a>testPerUserTestWhileIdleMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserEvictionPolicyClassNameMapNotInitialized"></a>testPerUserEvictionPolicyClassNameMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxTotalWithUserMapNotInitializedMissingKey"></a>testPerUserMaxTotalWithUserMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultReadOnlyMapNotInitialized"></a>testPerUserDefaultReadOnlyMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultAutoCommitMapNotInitializedMissingKey"></a>testPerUserDefaultAutoCommitMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinIdleMapNotInitializedMissingKey"></a>testPerUserMinIdleMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserNumTestsPerEvictionRunMapNotInitializedMissingKey"></a>testPerUserNumTestsPerEvictionRunMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxWaitDurationMapInitialized"></a>testPerUserMaxWaitDurationMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTimeBetweenEvictionRunsMillisWithUserMapNotInitializedMissingKey"></a>testPerUserTimeBetweenEvictionRunsMillisWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDurationBetweenEvictionRunsMapNotInitialized"></a>testPerUserDurationBetweenEvictionRunsMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultTransactionIsolationMapNotInitializedMissingKey"></a>testPerUserDefaultTransactionIsolationMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testClosingWithUserName"></a>testClosingWithUserName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTimeBetweenEvictionRunsMillisWithUserMapNotInitialized"></a>testPerUserTimeBetweenEvictionRunsMillisWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserSoftMinEvictableIdleDurationMapNotInitialized"></a>testPerUserSoftMinEvictableIdleDurationMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultTransactionIsolationMapNotInitialized"></a>testPerUserDefaultTransactionIsolationMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinIdleWithUserMapNotInitialized"></a>testPerUserMinIdleWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultReadOnlyWithUserMapInitialized"></a>testPerUserDefaultReadOnlyWithUserMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinIdleWithUserMapInitialized"></a>testPerUserMinIdleWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxWaitDurationMapNotInitializedMissingKey"></a>testPerUserMaxWaitDurationMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserLifoMapNotInitializedMissingKey"></a>testPerUserLifoMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnBorrowWithUserMapInitialized"></a>testPerUserTestOnBorrowWithUserMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestWhileIdleMapNotInitializedMissingKey"></a>testPerUserTestWhileIdleMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserBlockWhenExhaustedWithUserMapNotInitialized"></a>testPerUserBlockWhenExhaustedWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxWaitMillisWithUserMapNotInitializedMissingKeyDeprecated"></a>testPerUserMaxWaitMillisWithUserMapNotInitializedMissingKeyDeprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testChangePassword"></a>testChangePassword</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserLifoWithUserMapInitialized"></a>testPerUserLifoWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultAutoCommitWithUserMapNotInitialized"></a>testPerUserDefaultAutoCommitWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserNumTestsPerEvictionRunWithUserMapInitialized"></a>testPerUserNumTestsPerEvictionRunWithUserMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinEvictableIdleTimeMillisWithUserMapNotInitialized"></a>testPerUserMinEvictableIdleTimeMillisWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinEvictableIdleDurationMapNotInitialized"></a>testPerUserMinEvictableIdleDurationMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserLifoMapInitialized"></a>testPerUserLifoMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultAutoCommitWithUserMapInitialized"></a>testPerUserDefaultAutoCommitWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultAutoCommitMapInitialized"></a>testPerUserDefaultAutoCommitMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultAutoCommitMapNotInitialized"></a>testPerUserDefaultAutoCommitMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxTotalMapNotInitialized"></a>testPerUserMaxTotalMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserBlockWhenExhaustedWithUserMapInitialized"></a>testPerUserBlockWhenExhaustedWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxTotalMapNotInitializedMissingKey"></a>testPerUserMaxTotalMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testDefaultUser1"></a>testDefaultUser1</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testDefaultUser2"></a>testDefaultUser2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testClosing"></a>testClosing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserBlockWhenExhaustedMapInitialized"></a>testPerUserBlockWhenExhaustedMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultTransactionIsolationWithUserMapNotInitializedMissingKey"></a>testPerUserDefaultTransactionIsolationWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testDepreactedAccessors"></a>testDepreactedAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnBorrowMapInitialized"></a>testPerUserTestOnBorrowMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxTotalWithUserMapNotInitialized"></a>testPerUserMaxTotalWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxIdleMapNotInitializedMissingKey"></a>testPerUserMaxIdleMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserBlockWhenExhaustedMapNotInitializedMissingKey"></a>testPerUserBlockWhenExhaustedMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxTotalMapInitialized"></a>testPerUserMaxTotalMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserEvictionPolicyClassNameMapInitialized"></a>testPerUserEvictionPolicyClassNameMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnReturnMapNotInitialized"></a>testPerUserTestOnReturnMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnReturnMapNotInitializedMissingKey"></a>testPerUserTestOnReturnMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserSoftMinEvictableIdleDurationMapNotInitializedMissingKey"></a>testPerUserSoftMinEvictableIdleDurationMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDurationBetweenEvictionRunsMapInitialized"></a>testPerUserDurationBetweenEvictionRunsMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnCreateMapInitialized"></a>testPerUserTestOnCreateMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultReadOnlyWithUserMapNotInitialized"></a>testPerUserDefaultReadOnlyWithUserMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testDefaultReadOnly"></a>testDefaultReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxIdleWithUserMapNotInitialized"></a>testPerUserMaxIdleWithUserMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestWhileIdleWithUserMapNotInitialized"></a>testPerUserTestWhileIdleWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testDbcp597"></a>testDbcp597</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxIdleMapNotInitialized"></a>testPerUserMaxIdleMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultReadOnlyMapNotInitializedMissingKey"></a>testPerUserDefaultReadOnlyMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserSoftMinEvictableIdleTimeMillisWithUserMapNotInitializedMissingKey"></a>testPerUserSoftMinEvictableIdleTimeMillisWithUserMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxWaitDurationMapNotInitialized"></a>testPerUserMaxWaitDurationMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testSimpleWithUsername"></a>testSimpleWithUsername</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnCreateMapNotInitializedMissingKey"></a>testPerUserTestOnCreateMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserLifoMapNotInitialized"></a>testPerUserLifoMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserEvictionPolicyClassNameWithUserMapNotInitialized"></a>testPerUserEvictionPolicyClassNameWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testMaxWaitMillisZero"></a>testMaxWaitMillisZero</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMinIdleMapNotInitialized"></a>testPerUserMinIdleMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserNumTestsPerEvictionRunMapNotInitialized"></a>testPerUserNumTestsPerEvictionRunMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxWaitMillisWithUserMapInitializedDeprecated"></a>testPerUserMaxWaitMillisWithUserMapInitializedDeprecated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnCreateWithUserMapInitialized"></a>testPerUserTestOnCreateWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserBlockWhenExhaustedWithUserMapNotInitializedMissingKey"></a>testPerUserBlockWhenExhaustedWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTimeBetweenEvictionRunsMillisWithUserMapInitialized"></a>testPerUserTimeBetweenEvictionRunsMillisWithUserMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultReadOnlyMapInitialized"></a>testPerUserDefaultReadOnlyMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestWhileIdleMapInitialized"></a>testPerUserTestWhileIdleMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultTransactionIsolationWithUserMapNotInitialized"></a>testPerUserDefaultTransactionIsolationWithUserMapNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testSimple2"></a>testSimple2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserBlockWhenExhaustedMapNotInitialized"></a>testPerUserBlockWhenExhaustedMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserEvictionPolicyClassNameWithUserMapNotInitializedMissingKey"></a>testPerUserEvictionPolicyClassNameWithUserMapNotInitializedMissingKey</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxIdleMapInitialized"></a>testPerUserMaxIdleMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testMultipleThreads1"></a>testMultipleThreads1</td>
<td>0.308 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testMultipleThreads2"></a>testMultipleThreads2</td>
<td>1.008 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnBorrowWithUserMapNotInitializedMissingKey"></a>testPerUserTestOnBorrowWithUserMapNotInitializedMissingKey</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserMaxTotalWithUserMapInitialized"></a>testPerUserMaxTotalWithUserMapInitialized</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserDefaultTransactionIsolationMapInitialized"></a>testPerUserDefaultTransactionIsolationMapInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnBorrowMapNotInitializedMissingKey"></a>testPerUserTestOnBorrowMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testUnregisteredUser"></a>testUnregisteredUser</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestOnBorrowMapNotInitialized"></a>testPerUserTestOnBorrowMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserSoftMinEvictableIdleTimeMillisWithUserMapNotInitialized"></a>testPerUserSoftMinEvictableIdleTimeMillisWithUserMapNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserSoftMinEvictableIdleTimeMillisWithUserMapInitialized"></a>testPerUserSoftMinEvictableIdleTimeMillisWithUserMapInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testPerUserTestWhileIdleWithUserMapNotInitializedMissingKey"></a>testPerUserTestWhileIdleWithUserMapNotInitializedMissingKey</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPerUserPoolDataSource.testIncorrectPassword"></a>testIncorrectPassword</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDataSourceConnectionFactory"></a>
<h3>TestDataSourceConnectionFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDataSourceConnectionFactory.testDefaultValues"></a>testDefaultValues</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDataSourceConnectionFactory.testEmptyUser"></a>testEmptyUser</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDataSourceConnectionFactory.testCredentials"></a>testCredentials</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDataSourceConnectionFactory.testEmptyPassword"></a>testEmptyPassword</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestSQLExceptionList"></a>
<h3>TestSQLExceptionList</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestSQLExceptionList.testCause"></a>testCause</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestSQLExceptionList.testNullCause"></a>testNullCause</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.CharArrayTest"></a>
<h3>CharArrayTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.CharArrayTest.testGet"></a>testGet</td>
<td>0.010 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.CharArrayTest.testClear"></a>testClear</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.CharArrayTest.testToString"></a>testToString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.CharArrayTest.testAsString"></a>testAsString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.CharArrayTest.testHashCode"></a>testHashCode</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.CharArrayTest.testEquals"></a>testEquals</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestUserPassKey"></a>
<h3>TestUserPassKey</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestUserPassKey.testGettersAndSetters"></a>testGettersAndSetters</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestUserPassKey.testSerialization"></a>testSerialization</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestUserPassKey.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestUserPassKey.testHashcode"></a>testHashcode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestUserPassKey.testEquals"></a>testEquals</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestTransactionContext"></a>
<h3>TestTransactionContext</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestTransactionContext.testSetSharedConnectionEnlistFailure"></a>testSetSharedConnectionEnlistFailure</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestKeyedCPDSConnectionFactory"></a>
<h3>TestKeyedCPDSConnectionFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestKeyedCPDSConnectionFactory.testNullValidationQuery"></a>testNullValidationQuery</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestKeyedCPDSConnectionFactory.testConnectionErrorCleanup"></a>testConnectionErrorCleanup</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestKeyedCPDSConnectionFactory.testSharedPoolDSDestroyOnReturn"></a>testSharedPoolDSDestroyOnReturn</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDriverConnectionFactory"></a>
<h3>TestDriverConnectionFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverConnectionFactory.testDriverConnectionFactoryToString"></a>testDriverConnectionFactoryToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDriverConnectionFactory.testCreateConnection"></a>testCreateConnection</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPoolableConnection"></a>
<h3>TestPoolableConnection</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testPoolableConnectionLeak"></a>testPoolableConnectionLeak</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testIsDisconnectionSqlExceptionStackOverflow"></a>testIsDisconnectionSqlExceptionStackOverflow</td>
<td>0.238 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testFastFailValidationCustomCodes"></a>testFastFailValidationCustomCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testConnectionPool"></a>testConnectionPool</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testClosingWrappedInDelegate"></a>testClosingWrappedInDelegate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testFastFailValidation"></a>testFastFailValidation</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testMXBeanCompliance"></a>testMXBeanCompliance</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolableConnection.testDisconnectionIgnoreSqlCodes"></a>testDisconnectionIgnoreSqlCodes</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.UserPassKeyTest"></a>
<h3>UserPassKeyTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.UserPassKeyTest.testClear"></a>testClear</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestManagedDataSource"></a>
<h3>TestManagedDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testThreaded"></a>testThreaded</td>
<td>2.788 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testOpening"></a>testOpening</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testClosing"></a>testClosing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testHashCode"></a>testHashCode</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testSimple2"></a>testSimple2</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testSimple"></a>testSimple</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testSetNullTransactionRegistry"></a>testSetNullTransactionRegistry</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualsSameDelegateNoUnderlyingAccess"></a>testManagedConnectionEqualsSameDelegateNoUnderlyingAccess</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testNestedConnections"></a>testNestedConnections</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testTransactionRegistryNotInitialized"></a>testTransactionRegistryNotInitialized</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testSharedConnection"></a>testSharedConnection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualsSameDelegate"></a>testManagedConnectionEqualsSameDelegate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testConnectionReturnOnCommit"></a>testConnectionReturnOnCommit</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testSetTransactionRegistry"></a>testSetTransactionRegistry</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualsFail"></a>testManagedConnectionEqualsFail</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualsNull"></a>testManagedConnectionEqualsNull</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualsType"></a>testManagedConnectionEqualsType</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualInnermost"></a>testManagedConnectionEqualInnermost</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testManagedConnectionEqualsReflexive"></a>testManagedConnectionEqualsReflexive</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSource.testSetTransactionRegistryAlreadySet"></a>testSetTransactionRegistryAlreadySet</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDelegatingStatement"></a>
<h3>TestDelegatingStatement</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetDelegate"></a>testGetDelegate</td>
<td>0.016 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetMoreResults"></a>testGetMoreResults</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetLargeMaxRowsLong"></a>testSetLargeMaxRowsLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetResultSetConcurrency"></a>testGetResultSetConcurrency</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteLargeUpdateStringInteger"></a>testExecuteLargeUpdateStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetQueryTimeoutInteger"></a>testSetQueryTimeoutInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteLargeUpdateStringIntegerArray"></a>testExecuteLargeUpdateStringIntegerArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteStringIntegerArray"></a>testExecuteStringIntegerArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteString"></a>testExecuteString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testClearBatch"></a>testClearBatch</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteUpdateStringInteger"></a>testExecuteUpdateStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testClose"></a>testClose</td>
<td>0.018 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testWrap"></a>testWrap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetMaxFieldSizeInteger"></a>testSetMaxFieldSizeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetResultSetType"></a>testGetResultSetType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testIsCloseOnCompletion"></a>testIsCloseOnCompletion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testCloseWithStatementCloseException"></a>testCloseWithStatementCloseException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteStringInteger"></a>testExecuteStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testCloseWithResultSetCloseException"></a>testCloseWithResultSetCloseException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testIsPoolable"></a>testIsPoolable</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetEscapeProcessingBoolean"></a>testSetEscapeProcessingBoolean</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetResultSet"></a>testGetResultSet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testAddBatchString"></a>testAddBatchString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetCursorNameString"></a>testSetCursorNameString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetFetchSizeInteger"></a>testSetFetchSizeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetGeneratedKeys"></a>testGetGeneratedKeys</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteBatch"></a>testExecuteBatch</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteLargeUpdateString"></a>testExecuteLargeUpdateString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetFetchSize"></a>testGetFetchSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteLargeBatch"></a>testExecuteLargeBatch</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetLargeMaxRows"></a>testGetLargeMaxRows</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteLargeUpdateStringStringArray"></a>testExecuteLargeUpdateStringStringArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testCloseOnCompletion"></a>testCloseOnCompletion</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetFetchDirection"></a>testGetFetchDirection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetFetchDirectionInteger"></a>testSetFetchDirectionInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteQueryString"></a>testExecuteQueryString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetConnection"></a>testGetConnection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteQueryReturnsNull"></a>testExecuteQueryReturnsNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testCheckOpen"></a>testCheckOpen</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetMaxRows"></a>testGetMaxRows</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteUpdateString"></a>testExecuteUpdateString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testCancel"></a>testCancel</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetLargeUpdateCount"></a>testGetLargeUpdateCount</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetMaxFieldSize"></a>testGetMaxFieldSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteStringStringArray"></a>testExecuteStringStringArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetQueryTimeout"></a>testGetQueryTimeout</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetMaxRowsInteger"></a>testSetMaxRowsInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetMoreResultsInteger"></a>testGetMoreResultsInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testClearWarnings"></a>testClearWarnings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetUpdateCount"></a>testGetUpdateCount</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteUpdateStringStringArray"></a>testExecuteUpdateStringStringArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetWarnings"></a>testGetWarnings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testGetResultSetHoldability"></a>testGetResultSetHoldability</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testExecuteUpdateStringIntegerArray"></a>testExecuteUpdateStringIntegerArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingStatement.testSetPoolableBoolean"></a>testSetPoolableBoolean</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestConstants"></a>
<h3>TestConstants</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestConstants.testConstants"></a>testConstants</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPoolingDriver"></a>
<h3>TestPoolingDriver</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testThreaded"></a>testThreaded</td>
<td>3.013 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testOpening"></a>testOpening</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testPooling"></a>testPooling</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testClosing"></a>testClosing</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testBackPointers"></a>testBackPointers</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testHashCode"></a>testHashCode</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testMaxTotal"></a>testMaxTotal</td>
<td>0.107 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testSimple2"></a>testSimple2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testLogWriter"></a>testLogWriter</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testReportedBug12400"></a>testReportedBug12400</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testReportedBug28912"></a>testReportedBug28912</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.test1"></a>test1</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.test2"></a>test2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testClosePool"></a>testClosePool</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDriver.testInvalidateConnection"></a>testInvalidateConnection</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestCPDSConnectionFactory"></a>
<h3>TestCPDSConnectionFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestCPDSConnectionFactory.testNullValidationQuery"></a>testNullValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestCPDSConnectionFactory.testConnectionErrorCleanup"></a>testConnectionErrorCleanup</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestCPDSConnectionFactory.testSetPasswordString"></a>testSetPasswordString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestCPDSConnectionFactory.testSetPasswordCharArray"></a>testSetPasswordCharArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestCPDSConnectionFactory.testSharedPoolDSDestroyOnReturn"></a>testSharedPoolDSDestroyOnReturn</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPoolingDataSource"></a>
<h3>TestPoolingDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testThreaded"></a>testThreaded</td>
<td>2.974 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testOpening"></a>testOpening</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testClosing"></a>testClosing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.104 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testSimple2"></a>testSimple2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testSimple"></a>testSimple</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testClose"></a>testClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testFixFactoryConfig"></a>testFixFactoryConfig</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPoolGuardConnectionWrapperEqualsSameDelegate"></a>testPoolGuardConnectionWrapperEqualsSameDelegate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPoolGuardConnectionWrapperEqualInnermost"></a>testPoolGuardConnectionWrapperEqualInnermost</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPoolGuardConnectionWrapperEqualsReflexive"></a>testPoolGuardConnectionWrapperEqualsReflexive</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testUnwrap"></a>testUnwrap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPoolGuardConnectionWrapperEqualsFail"></a>testPoolGuardConnectionWrapperEqualsFail</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPoolGuardConnectionWrapperEqualsNull"></a>testPoolGuardConnectionWrapperEqualsNull</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingDataSource.testPoolGuardConnectionWrapperEqualsType"></a>testPoolGuardConnectionWrapperEqualsType</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.Jdbc41BridgeTest"></a>
<h3>Jdbc41BridgeTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testGetParentLogger"></a>testGetParentLogger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testGeneratedKeyAlwaysReturned"></a>testGeneratedKeyAlwaysReturned</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testGetObjectName"></a>testGetObjectName</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testGetNetworkTimeout"></a>testGetNetworkTimeout</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testAbort"></a>testAbort</td>
<td>0.031 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testIsCloseOnCompletion"></a>testIsCloseOnCompletion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testCloseOnCompletion"></a>testCloseOnCompletion</td>
<td>0.014 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testGetObjectIndex"></a>testGetObjectIndex</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testSetSchema"></a>testSetSchema</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testGetSchema"></a>testGetSchema</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.Jdbc41BridgeTest.testSetNetworkTimeout"></a>testSetNetworkTimeout</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource"></a>
<h3>TestInstanceKeyDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testExceptionOnSetupDefaults"></a>testExceptionOnSetupDefaults</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDataSourceNameAlreadySet"></a>testDataSourceNameAlreadySet</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultTransactionIsolationInvalid"></a>testDefaultTransactionIsolationInvalid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testLogWriter"></a>testLogWriter</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testConnection"></a>testConnection</td>
<td>0.046 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testJndiPropertiesNotInitialized"></a>testJndiPropertiesNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultEvictionPolicyClassName"></a>testDefaultEvictionPolicyClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultTransactionIsolation"></a>testDefaultTransactionIsolation</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultLifo"></a>testDefaultLifo</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testJndiNullProperties"></a>testJndiNullProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testValidationQueryTimeout"></a>testValidationQueryTimeout</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testRollbackAfterValidation"></a>testRollbackAfterValidation</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testConnectionPoolDataSourceAlreadySetUsingJndi"></a>testConnectionPoolDataSourceAlreadySetUsingJndi</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testLogWriterAutoInitialized"></a>testLogWriterAutoInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testLoginTimeout"></a>testLoginTimeout</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testJndiEnvironment"></a>testJndiEnvironment</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testValidationQuery"></a>testValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultTestOnCreate"></a>testDefaultTestOnCreate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testJndiPropertiesCleared"></a>testJndiPropertiesCleared</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testValidationQueryWithConnectionCalled"></a>testValidationQueryWithConnectionCalled</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testValidationQueryTimeoutDuration"></a>testValidationQueryTimeoutDuration</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testConnectionPoolDataSource"></a>testConnectionPoolDataSource</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultReadOnly"></a>testDefaultReadOnly</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultSoftMinEvictableIdleTimeMillis"></a>testDefaultSoftMinEvictableIdleTimeMillis</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testMaxConnLifetimeMillis"></a>testMaxConnLifetimeMillis</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testUnwrap"></a>testUnwrap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testRollbackAfterValidationWithConnectionCalled"></a>testRollbackAfterValidationWithConnectionCalled</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDataSourceName"></a>testDataSourceName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultMinIdle"></a>testDefaultMinIdle</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDefaultBlockWhenExhausted"></a>testDefaultBlockWhenExhausted</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDescription"></a>testDescription</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testDataSourceNameAlreadySetUsingJndi"></a>testDataSourceNameAlreadySetUsingJndi</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestInstanceKeyDataSource.testConnectionPoolDataSourceAlreadySet"></a>testConnectionPoolDataSourceAlreadySet</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestBasicDataSourceFactory"></a>
<h3>TestBasicDataSourceFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSourceFactory.testProperties"></a>testProperties</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSourceFactory.testValidateProperties"></a>testValidateProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSourceFactory.testAllProperties"></a>testAllProperties</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSourceFactory.testNoProperties"></a>testNoProperties</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestPoolableManagedConnection"></a>
<h3>TestPoolableManagedConnection</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestPoolableManagedConnection.testReallyClose"></a>testReallyClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestPoolableManagedConnection.testManagedConnection"></a>testManagedConnection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestPoolableManagedConnection.testPoolableConnection"></a>testPoolableConnection</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestLocalXaResource"></a>
<h3>TestLocalXaResource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartReadOnlyConnectionPrepare"></a>testStartReadOnlyConnectionPrepare</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testRollbackMissingXid"></a>testRollbackMissingXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testCommitMissingXid"></a>testCommitMissingXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testCommitConnectionClosed"></a>testCommitConnectionClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartReadOnlyConnectionExceptionOnGetAutoCommit"></a>testStartReadOnlyConnectionExceptionOnGetAutoCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testCommitNoTransaction"></a>testCommitNoTransaction</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartExceptionOnGetAutoCommit"></a>testStartExceptionOnGetAutoCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartNoFlagResumeEnd"></a>testStartNoFlagResumeEnd</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartFailsWhenCannotSetAutoCommit"></a>testStartFailsWhenCannotSetAutoCommit</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testForgetMissingXid"></a>testForgetMissingXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartNoFlagResume"></a>testStartNoFlagResume</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testRollback"></a>testRollback</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testCommitConnectionNotReadOnly"></a>testCommitConnectionNotReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartInvalidFlag"></a>testStartInvalidFlag</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testRollbackInvalidXid"></a>testRollbackInvalidXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartNoFlagResumeEndDifferentXid"></a>testStartNoFlagResumeEndDifferentXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testCommit"></a>testCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartNoFlagResumeButDifferentXid"></a>testStartNoFlagResumeButDifferentXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testForget"></a>testForget</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testCommitInvalidXid"></a>testCommitInvalidXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testIsSame"></a>testIsSame</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartNoFlagResumeEndMissingXid"></a>testStartNoFlagResumeEndMissingXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testForgetDifferentXid"></a>testForgetDifferentXid</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testStartNoFlagButAlreadyEnlisted"></a>testStartNoFlagButAlreadyEnlisted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestLocalXaResource.testConstructor"></a>testConstructor</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestBasicManagedDataSource"></a>
<h3>TestBasicManagedDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testThreaded"></a>testThreaded</td>
<td>3.034 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testOpening"></a>testOpening</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testHashing"></a>testHashing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testClosing"></a>testClosing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testBackPointers"></a>testBackPointers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testHashCode"></a>testHashCode</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSimple2"></a>testSimple2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEmptyValidationQuery"></a>testEmptyValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCreateConnectionFactoryWithConnectionFactoryClassName"></a>testCreateConnectionFactoryWithConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testValidationQueryTimoutFail"></a>testValidationQueryTimoutFail</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testConcurrentInvalidateBorrow"></a>testConcurrentInvalidateBorrow</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetValidationTestProperties"></a>testSetValidationTestProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCreateConnectionFactoryWithoutConnectionFactoryClassName"></a>testCreateConnectionFactoryWithoutConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testRollbackReadOnly"></a>testRollbackReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.managed.testbasicmanageddatasource.testevict"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEvict"></a><a href="#surefire--org.apache.commons.dbcp2.managed.testbasicmanageddatasource.testevict">testEvict</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEvict');"><span id="org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEvict-off"> + </span><span id="org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEvict-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testStart"></a>testStart</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testPropertyTestOnReturn"></a>testPropertyTestOnReturn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testValidationQueryTimeoutSucceed"></a>testValidationQueryTimeoutSucceed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testStartInitializes"></a>testStartInitializes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testMaxTotalZero"></a>testMaxTotalZero</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testConnectionMBeansDisabled"></a>testConnectionMBeansDisabled</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testMaxConnLifetimeExceeded"></a>testMaxConnLifetimeExceeded</td>
<td>0.506 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testValidationQueryTimeoutNegative"></a>testValidationQueryTimeoutNegative</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testPoolCloseRTE"></a>testPoolCloseRTE</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testInstanceNotFoundExceptionLogSuppressed"></a>testInstanceNotFoundExceptionLogSuppressed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetAutoCommitTrueOnClose"></a>testSetAutoCommitTrueOnClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testConcurrentInitBorrow"></a>testConcurrentInitBorrow</td>
<td>0.492 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testDeprecatedAccessors"></a>testDeprecatedAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testManualConnectionEvict"></a>testManualConnectionEvict</td>
<td>0.102 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testValidationQueryTimeoutZero"></a>testValidationQueryTimeoutZero</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testMaxConnLifetimeExceededMutedLog"></a>testMaxConnLifetimeExceededMutedLog</td>
<td>0.504 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEmptyInitConnectionSql"></a>testEmptyInitConnectionSql</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testDriverClassLoader"></a>testDriverClassLoader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testJmxDisabled"></a>testJmxDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testInitialSize"></a>testInitialSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testInvalidValidationQuery"></a>testInvalidValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testRestart"></a>testRestart</td>
<td>0.202 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testNoAccessToUnderlyingConnectionAllowed"></a>testNoAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testPoolCloseCheckedException"></a>testPoolCloseCheckedException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCreateDataSourceCleanupEvictor"></a>testCreateDataSourceCleanupEvictor</td>
<td>1.006 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCreateDataSourceCleanupThreads"></a>testCreateDataSourceCleanupThreads</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testDefaultCatalog"></a>testDefaultCatalog</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testInvalidateConnection"></a>testInvalidateConnection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetProperties"></a>testSetProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testMutateAbandonedConfig"></a>testMutateAbandonedConfig</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testDisconnectionIgnoreSqlCodes"></a>testDisconnectionIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testUnwrap"></a>testUnwrap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testJmxDoesNotExposePassword"></a>testJmxDoesNotExposePassword</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testInvalidConnectionInitSqlCollection"></a>testInvalidConnectionInitSqlCollection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testDisconnectSqlCodes"></a>testDisconnectSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testInvalidConnectionInitSqlList"></a>testInvalidConnectionInitSqlList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testIsClosedFailure"></a>testIsClosedFailure</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetNullXaDataSourceInstance"></a>testSetNullXaDataSourceInstance</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testTransactionManagerNotSet"></a>testTransactionManagerNotSet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testReallyClose"></a>testReallyClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetDriverName"></a>testSetDriverName</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetRollbackOnlyBeforeGetConnectionDoesNotLeak"></a>testSetRollbackOnlyBeforeGetConnectionDoesNotLeak</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testXaDataSourceInstance"></a>testXaDataSourceInstance</td>
<td>0.006 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCreateXaDataSourceNoInstanceSetAndNoDataSource"></a>testCreateXaDataSourceNoInstanceSetAndNoDataSource</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testCreateXaDataSourceNewInstance"></a>testCreateXaDataSourceNewInstance</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testSetXaDataSourceInstance"></a>testSetXaDataSourceInstance</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testTransactionSynchronizationRegistry"></a>testTransactionSynchronizationRegistry</td>
<td>0.093 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testRuntimeExceptionsAreRethrown"></a>testRuntimeExceptionsAreRethrown</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testXADataSource"></a>testXADataSource</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestAbandonedBasicDataSource"></a>
<h3>TestAbandonedBasicDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testThreaded"></a>testThreaded</td>
<td>3.108 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testOpening"></a>testOpening</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testClosing"></a>testClosing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.107 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testSimple2"></a>testSimple2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testSimple"></a>testSimple</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEmptyValidationQuery"></a>testEmptyValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCreateConnectionFactoryWithConnectionFactoryClassName"></a>testCreateConnectionFactoryWithConnectionFactoryClassName</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testValidationQueryTimoutFail"></a>testValidationQueryTimoutFail</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testConcurrentInvalidateBorrow"></a>testConcurrentInvalidateBorrow</td>
<td>0.035 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testSetValidationTestProperties"></a>testSetValidationTestProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCreateConnectionFactoryWithoutConnectionFactoryClassName"></a>testCreateConnectionFactoryWithoutConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testRollbackReadOnly"></a>testRollbackReadOnly</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testabandonedbasicdatasource.testevict"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEvict"></a><a href="#surefire--org.apache.commons.dbcp2.testabandonedbasicdatasource.testevict">testEvict</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEvict');"><span id="org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEvict-off"> + </span><span id="org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEvict-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testStart"></a>testStart</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testPropertyTestOnReturn"></a>testPropertyTestOnReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testValidationQueryTimeoutSucceed"></a>testValidationQueryTimeoutSucceed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testStartInitializes"></a>testStartInitializes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testMaxTotalZero"></a>testMaxTotalZero</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testConnectionMBeansDisabled"></a>testConnectionMBeansDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testMaxConnLifetimeExceeded"></a>testMaxConnLifetimeExceeded</td>
<td>0.506 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testValidationQueryTimeoutNegative"></a>testValidationQueryTimeoutNegative</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testPoolCloseRTE"></a>testPoolCloseRTE</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testInstanceNotFoundExceptionLogSuppressed"></a>testInstanceNotFoundExceptionLogSuppressed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testSetAutoCommitTrueOnClose"></a>testSetAutoCommitTrueOnClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testConcurrentInitBorrow"></a>testConcurrentInitBorrow</td>
<td>0.494 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testDeprecatedAccessors"></a>testDeprecatedAccessors</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testManualConnectionEvict"></a>testManualConnectionEvict</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testValidationQueryTimeoutZero"></a>testValidationQueryTimeoutZero</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testMaxConnLifetimeExceededMutedLog"></a>testMaxConnLifetimeExceededMutedLog</td>
<td>0.506 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEmptyInitConnectionSql"></a>testEmptyInitConnectionSql</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testDriverClassLoader"></a>testDriverClassLoader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testJmxDisabled"></a>testJmxDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testInitialSize"></a>testInitialSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testInvalidValidationQuery"></a>testInvalidValidationQuery</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testRestart"></a>testRestart</td>
<td>0.207 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testNoAccessToUnderlyingConnectionAllowed"></a>testNoAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testPoolCloseCheckedException"></a>testPoolCloseCheckedException</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCreateDataSourceCleanupEvictor"></a>testCreateDataSourceCleanupEvictor</td>
<td>1.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testCreateDataSourceCleanupThreads"></a>testCreateDataSourceCleanupThreads</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testDefaultCatalog"></a>testDefaultCatalog</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testInvalidateConnection"></a>testInvalidateConnection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testSetProperties"></a>testSetProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testMutateAbandonedConfig"></a>testMutateAbandonedConfig</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testDisconnectionIgnoreSqlCodes"></a>testDisconnectionIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testUnwrap"></a>testUnwrap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testJmxDoesNotExposePassword"></a>testJmxDoesNotExposePassword</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testInvalidConnectionInitSqlCollection"></a>testInvalidConnectionInitSqlCollection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testDisconnectSqlCodes"></a>testDisconnectSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testInvalidConnectionInitSqlList"></a>testInvalidConnectionInitSqlList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testIsClosedFailure"></a>testIsClosedFailure</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testAbandonedStackTraces"></a>testAbandonedStackTraces</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testAbandonedCloseWithExceptions"></a>testAbandonedCloseWithExceptions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testLastUsedPrepareCall"></a>testLastUsedPrepareCall</td>
<td>2.619 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testLastUsed"></a>testLastUsed</td>
<td>2.613 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testAbandoned"></a>testAbandoned</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testLastUsedLargePreparedStatementUse"></a>testLastUsedLargePreparedStatementUse</td>
<td>2.617 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testGarbageCollectorCleanUp01"></a>testGarbageCollectorCleanUp01</td>
<td>0.041 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testGarbageCollectorCleanUp02"></a>testGarbageCollectorCleanUp02</td>
<td>0.134 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testLastUsedUpdate"></a>testLastUsedUpdate</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testAbandonedClose"></a>testAbandonedClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testLastUsedPreparedStatementUse"></a>testLastUsedPreparedStatementUse</td>
<td>2.618 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestManagedConnection"></a>
<h3>TestManagedConnection</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedConnection.testConnectionReturnOnErrorWhenEnlistingXAResource"></a>testConnectionReturnOnErrorWhenEnlistingXAResource</td>
<td>0.004 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDelegatingCallableStatement"></a>
<h3>TestDelegatingCallableStatement</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetFloatStringFloat"></a>testSetFloatStringFloat</td>
<td>0.230 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBlobInteger"></a>testGetBlobInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDateStringCalendar"></a>testGetDateStringCalendar</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDelegate"></a>testGetDelegate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBigDecimalInteger"></a>testGetBigDecimalInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetSQLXMLInteger"></a>testGetSQLXMLInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBytesString"></a>testGetBytesString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetClobStringReaderLong"></a>testSetClobStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetObjectIntegerMap"></a>testGetObjectIntegerMap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterIntegerIntegerString"></a>testRegisterOutParameterIntegerIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetDateStringSqlDateCalendar"></a>testSetDateStringSqlDateCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimeString"></a>testGetTimeString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetURLString"></a>testGetURLString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBinaryStreamStringInputStreamInteger"></a>testSetBinaryStreamStringInputStreamInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetObjectStringObjectSQLTypeInteger"></a>testSetObjectStringObjectSQLTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetNCharacterStreamInteger"></a>testGetNCharacterStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetNClobInteger"></a>testGetNClobInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetRowIdString"></a>testGetRowIdString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimeIntegerCalendar"></a>testGetTimeIntegerCalendar</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetObjectStringObjectIntegerInteger"></a>testSetObjectStringObjectIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetRowIdInteger"></a>testGetRowIdInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBooleanStringBoolean"></a>testSetBooleanStringBoolean</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDoubleString"></a>testGetDoubleString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetClobStringClob"></a>testSetClobStringClob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testExecuteQueryReturnsNotNull"></a>testExecuteQueryReturnsNotNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterStringIntegerString"></a>testRegisterOutParameterStringIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetLongInteger"></a>testGetLongInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimestampStringCalendar"></a>testGetTimestampStringCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetCharacterStreamStringReaderLong"></a>testSetCharacterStreamStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNClobStringReaderLong"></a>testSetNClobStringReaderLong</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNStringStringString"></a>testSetNStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBlobStringBlob"></a>testSetBlobStringBlob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBlobStringInputStream"></a>testSetBlobStringInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetURLStringUrl"></a>testSetURLStringUrl</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterIntegerSQLTypeString"></a>testRegisterOutParameterIntegerSQLTypeString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetByteStringByte"></a>testSetByteStringByte</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetAsciiStreamStringInputStreamInteger"></a>testSetAsciiStreamStringInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBinaryStreamStringInputStream"></a>testSetBinaryStreamStringInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNClobStringReader"></a>testSetNClobStringReader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetArrayString"></a>testGetArrayString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNCharacterStreamStringReaderLong"></a>testSetNCharacterStreamStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetObjectStringObjectSQLType"></a>testSetObjectStringObjectSQLType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDateIntegerCalendar"></a>testGetDateIntegerCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetShortString"></a>testGetShortString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterStringSQLTypeString"></a>testRegisterOutParameterStringSQLTypeString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterIntegerSQLTypeInteger"></a>testRegisterOutParameterIntegerSQLTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterIntegerIntegerInteger"></a>testRegisterOutParameterIntegerIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetCharacterStreamStringReader"></a>testSetCharacterStreamStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetRefInteger"></a>testGetRefInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBigDecimalString"></a>testGetBigDecimalString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetNClobString"></a>testGetNClobString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetRefString"></a>testGetRefString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetObjectStringObjectInteger"></a>testSetObjectStringObjectInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBooleanString"></a>testGetBooleanString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetSQLXMLString"></a>testGetSQLXMLString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetStringStringString"></a>testSetStringStringString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDoubleInteger"></a>testGetDoubleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetTimeStringTimeCalendar"></a>testSetTimeStringTimeCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetStringInteger"></a>testGetStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetCharacterStreamString"></a>testGetCharacterStreamString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNClobStringNClob"></a>testSetNClobStringNClob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetByteInteger"></a>testGetByteInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetIntStringInteger"></a>testSetIntStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetNStringString"></a>testGetNStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetObjectString"></a>testGetObjectString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetTimestampStringTimestampCalendar"></a>testSetTimestampStringTimestampCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBigDecimalIntegerInteger"></a>testGetBigDecimalIntegerInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBinaryStreamStringInputStreamLong"></a>testSetBinaryStreamStringInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterIntegerSQLType"></a>testRegisterOutParameterIntegerSQLType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetClobInteger"></a>testGetClobInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetObjectStringObject"></a>testSetObjectStringObject</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetNStringInteger"></a>testGetNStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimestampIntegerCalendar"></a>testGetTimestampIntegerCalendar</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetFloatString"></a>testGetFloatString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetObjectInteger"></a>testGetObjectInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetShortInteger"></a>testGetShortInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimestampString"></a>testGetTimestampString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimeStringCalendar"></a>testGetTimeStringCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testWasNull"></a>testWasNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetSQLXMLStringSQLXML"></a>testSetSQLXMLStringSQLXML</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimeInteger"></a>testGetTimeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetIntInteger"></a>testGetIntInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetURLInteger"></a>testGetURLInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetLongStringLong"></a>testSetLongStringLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testExecuteQueryReturnsNull"></a>testExecuteQueryReturnsNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetLongString"></a>testGetLongString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterIntegerInteger"></a>testRegisterOutParameterIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetFloatInteger"></a>testGetFloatInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetIntString"></a>testGetIntString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetCharacterStreamStringReaderInteger"></a>testSetCharacterStreamStringReaderInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetClobString"></a>testGetClobString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterStringSQLType"></a>testRegisterOutParameterStringSQLType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetObjectIntegerClass"></a>testGetObjectIntegerClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetDoubleStringDouble"></a>testSetDoubleStringDouble</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDateInteger"></a>testGetDateInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBlobString"></a>testGetBlobString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetClobStringReader"></a>testSetClobStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNCharacterStreamStringReader"></a>testSetNCharacterStreamStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetTimestampStringTimestamp"></a>testSetTimestampStringTimestamp</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetRowIdStringRowId"></a>testSetRowIdStringRowId</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBytesStringByteArray"></a>testSetBytesStringByteArray</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBytesInteger"></a>testGetBytesInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetStringString"></a>testGetStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetCharacterStreamInteger"></a>testGetCharacterStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetObjectStringClass"></a>testGetObjectStringClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetAsciiStreamStringInputStreamLong"></a>testSetAsciiStreamStringInputStreamLong</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetDateStringSqlDate"></a>testSetDateStringSqlDate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetShortStringShort"></a>testSetShortStringShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetObjectStringMap"></a>testGetObjectStringMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetNCharacterStreamString"></a>testGetNCharacterStreamString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterStringInteger"></a>testRegisterOutParameterStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNullStringIntegerString"></a>testSetNullStringIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBlobStringInputStreamLong"></a>testSetBlobStringInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetNullStringInteger"></a>testSetNullStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetAsciiStreamStringInputStream"></a>testSetAsciiStreamStringInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetBigDecimalStringBigDecimal"></a>testSetBigDecimalStringBigDecimal</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetArrayInteger"></a>testGetArrayInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetBooleanInteger"></a>testGetBooleanInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testSetTimeStringTime"></a>testSetTimeStringTime</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterStringSQLTypeInteger"></a>testRegisterOutParameterStringSQLTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetByteString"></a>testGetByteString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetDateString"></a>testGetDateString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testRegisterOutParameterStringIntegerInteger"></a>testRegisterOutParameterStringIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingCallableStatement.testGetTimestampInteger"></a>testGetTimestampInteger</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestJndi"></a>
<h3>TestJndi</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestJndi.testBasicDataSourceBind"></a>testBasicDataSourceBind</td>
<td>0.011 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestJndi.testPerUserPoolDataSourceBind"></a>testPerUserPoolDataSourceBind</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestJndi.testSharedPoolDataSourceBind"></a>testSharedPoolDataSourceBind</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPStmtKey"></a>
<h3>TestPStmtKey</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testGettersSetters"></a>testGettersSetters</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorEquals"></a>testCtorEquals</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorStringStringArrayOfStrings"></a>testCtorStringStringArrayOfStrings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorStringStringArrayOfInts"></a>testCtorStringStringArrayOfInts</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorStringStringArrayOfNullInts"></a>testCtorStringStringArrayOfNullInts</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testEquals"></a>testEquals</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorDifferentCatalog"></a>testCtorDifferentCatalog</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorDifferentSchema"></a>testCtorDifferentSchema</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtKey.testCtorStringStringArrayOfNullStrings"></a>testCtorStringStringArrayOfNullStrings</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestBasicDataSource"></a>
<h3>TestBasicDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testThreaded"></a>testThreaded</td>
<td>3.144 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testOpening"></a>testOpening</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testClosing"></a>testClosing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testHashCode"></a>testHashCode</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.104 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.009 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testSimple2"></a>testSimple2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testSimple"></a>testSimple</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testEmptyValidationQuery"></a>testEmptyValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCreateConnectionFactoryWithConnectionFactoryClassName"></a>testCreateConnectionFactoryWithConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testValidationQueryTimoutFail"></a>testValidationQueryTimoutFail</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testConcurrentInvalidateBorrow"></a>testConcurrentInvalidateBorrow</td>
<td>0.019 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testSetValidationTestProperties"></a>testSetValidationTestProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCreateConnectionFactoryWithoutConnectionFactoryClassName"></a>testCreateConnectionFactoryWithoutConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testRollbackReadOnly"></a>testRollbackReadOnly</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasource.testevict"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testEvict"></a><a href="#surefire--org.apache.commons.dbcp2.testbasicdatasource.testevict">testEvict</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestBasicDataSource.testEvict');"><span id="org.apache.commons.dbcp2.TestBasicDataSource.testEvict-off"> + </span><span id="org.apache.commons.dbcp2.TestBasicDataSource.testEvict-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testStart"></a>testStart</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testPropertyTestOnReturn"></a>testPropertyTestOnReturn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testValidationQueryTimeoutSucceed"></a>testValidationQueryTimeoutSucceed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testStartInitializes"></a>testStartInitializes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testMaxTotalZero"></a>testMaxTotalZero</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testConnectionMBeansDisabled"></a>testConnectionMBeansDisabled</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testMaxConnLifetimeExceeded"></a>testMaxConnLifetimeExceeded</td>
<td>0.506 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testValidationQueryTimeoutNegative"></a>testValidationQueryTimeoutNegative</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testPoolCloseRTE"></a>testPoolCloseRTE</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testInstanceNotFoundExceptionLogSuppressed"></a>testInstanceNotFoundExceptionLogSuppressed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testSetAutoCommitTrueOnClose"></a>testSetAutoCommitTrueOnClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testConcurrentInitBorrow"></a>testConcurrentInitBorrow</td>
<td>0.496 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testDeprecatedAccessors"></a>testDeprecatedAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testManualConnectionEvict"></a>testManualConnectionEvict</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testValidationQueryTimeoutZero"></a>testValidationQueryTimeoutZero</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testMaxConnLifetimeExceededMutedLog"></a>testMaxConnLifetimeExceededMutedLog</td>
<td>0.502 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testEmptyInitConnectionSql"></a>testEmptyInitConnectionSql</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testDriverClassLoader"></a>testDriverClassLoader</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testJmxDisabled"></a>testJmxDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testInitialSize"></a>testInitialSize</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testInvalidValidationQuery"></a>testInvalidValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testRestart"></a>testRestart</td>
<td>0.205 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testNoAccessToUnderlyingConnectionAllowed"></a>testNoAccessToUnderlyingConnectionAllowed</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testPoolCloseCheckedException"></a>testPoolCloseCheckedException</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCreateDataSourceCleanupEvictor"></a>testCreateDataSourceCleanupEvictor</td>
<td>1.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testCreateDataSourceCleanupThreads"></a>testCreateDataSourceCleanupThreads</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testDefaultCatalog"></a>testDefaultCatalog</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testInvalidateConnection"></a>testInvalidateConnection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testSetProperties"></a>testSetProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testMutateAbandonedConfig"></a>testMutateAbandonedConfig</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testDisconnectionIgnoreSqlCodes"></a>testDisconnectionIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testUnwrap"></a>testUnwrap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testJmxDoesNotExposePassword"></a>testJmxDoesNotExposePassword</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testInvalidConnectionInitSqlCollection"></a>testInvalidConnectionInitSqlCollection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testDisconnectSqlCodes"></a>testDisconnectSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testInvalidConnectionInitSqlList"></a>testInvalidConnectionInitSqlList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSource.testIsClosedFailure"></a>testIsClosedFailure</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData"></a>
<h3>TestDelegatingDatabaseMetaData</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSchemasInPrivilegeDefinitions"></a>testSupportsSchemasInPrivilegeDefinitions</td>
<td>0.064 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetVersionColumnsStringStringString"></a>testGetVersionColumnsStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxColumnsInOrderBy"></a>testGetMaxColumnsInOrderBy</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDriverName"></a>testGetDriverName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetIndexInfoStringStringStringBooleanBoolean"></a>testGetIndexInfoStringStringStringBooleanBoolean</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsStoredProcedures"></a>testSupportsStoredProcedures</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDelegate"></a>testGetDelegate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSchemas"></a>testGetSchemas</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsStoredFunctionsUsingCallSyntax"></a>testSupportsStoredFunctionsUsingCallSyntax</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsNamedParameters"></a>testSupportsNamedParameters</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetAttributesStringStringStringString"></a>testGetAttributesStringStringStringString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsANSI92FullSQL"></a>testSupportsANSI92FullSQL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetJDBCMinorVersion"></a>testGetJDBCMinorVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testDataDefinitionIgnoredInTransactions"></a>testDataDefinitionIgnoredInTransactions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSchemasStringString"></a>testGetSchemasStringString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetExportedKeysStringStringString"></a>testGetExportedKeysStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsDataManipulationTransactionsOnly"></a>testSupportsDataManipulationTransactionsOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDatabaseMajorVersion"></a>testGetDatabaseMajorVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxColumnsInSelect"></a>testGetMaxColumnsInSelect</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testNullsAreSortedAtStart"></a>testNullsAreSortedAtStart</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testOwnDeletesAreVisibleInteger"></a>testOwnDeletesAreVisibleInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testNullsAreSortedHigh"></a>testNullsAreSortedHigh</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGeneratedKeyAlwaysReturned"></a>testGeneratedKeyAlwaysReturned</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsOpenCursorsAcrossCommit"></a>testSupportsOpenCursorsAcrossCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCatalogsInIndexDefinitions"></a>testSupportsCatalogsInIndexDefinitions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsGroupByUnrelated"></a>testSupportsGroupByUnrelated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxUserNameLength"></a>testGetMaxUserNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetPseudoColumnsStringStringStringString"></a>testGetPseudoColumnsStringStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsMultipleOpenResults"></a>testSupportsMultipleOpenResults</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetExtraNameCharacters"></a>testGetExtraNameCharacters</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCatalogsInProcedureCalls"></a>testSupportsCatalogsInProcedureCalls</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsOpenStatementsAcrossRollback"></a>testSupportsOpenStatementsAcrossRollback</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testNullsAreSortedLow"></a>testNullsAreSortedLow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsMinimumSQLGrammar"></a>testSupportsMinimumSQLGrammar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsMultipleTransactions"></a>testSupportsMultipleTransactions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsIntegrityEnhancementFacility"></a>testSupportsIntegrityEnhancementFacility</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxTableNameLength"></a>testGetMaxTableNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCorrelatedSubqueries"></a>testSupportsCorrelatedSubqueries</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsResultSetConcurrencyIntegerInteger"></a>testSupportsResultSetConcurrencyIntegerInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsGetGeneratedKeys"></a>testSupportsGetGeneratedKeys</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCatalogsInPrivilegeDefinitions"></a>testSupportsCatalogsInPrivilegeDefinitions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testStoresLowerCaseQuotedIdentifiers"></a>testStoresLowerCaseQuotedIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testWrap"></a>testWrap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testNullPlusNonNullIsNull"></a>testNullPlusNonNullIsNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testAllTablesAreSelectable"></a>testAllTablesAreSelectable</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsMixedCaseQuotedIdentifiers"></a>testSupportsMixedCaseQuotedIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testInsertsAreDetectedInteger"></a>testInsertsAreDetectedInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testUsesLocalFiles"></a>testUsesLocalFiles</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsOpenStatementsAcrossCommit"></a>testSupportsOpenStatementsAcrossCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSchemasInProcedureCalls"></a>testSupportsSchemasInProcedureCalls</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsTransactions"></a>testSupportsTransactions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetPrimaryKeysStringStringString"></a>testGetPrimaryKeysStringStringString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxCharLiteralLength"></a>testGetMaxCharLiteralLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSchemasInIndexDefinitions"></a>testSupportsSchemasInIndexDefinitions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetImportedKeysStringStringString"></a>testGetImportedKeysStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testNullsAreSortedAtEnd"></a>testNullsAreSortedAtEnd</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testDeletesAreDetectedInteger"></a>testDeletesAreDetectedInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsPositionedDelete"></a>testSupportsPositionedDelete</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDatabaseProductVersion"></a>testGetDatabaseProductVersion</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxStatementLength"></a>testGetMaxStatementLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testUsesLocalFilePerTable"></a>testUsesLocalFilePerTable</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetProcedureColumnsStringStringStringString"></a>testGetProcedureColumnsStringStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxColumnsInGroupBy"></a>testGetMaxColumnsInGroupBy</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetIdentifierQuoteString"></a>testGetIdentifierQuoteString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testOthersInsertsAreVisibleInteger"></a>testOthersInsertsAreVisibleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testStoresLowerCaseIdentifiers"></a>testStoresLowerCaseIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetClientInfoProperties"></a>testGetClientInfoProperties</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetInnermostDelegate"></a>testGetInnermostDelegate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxSchemaNameLength"></a>testGetMaxSchemaNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSQLKeywords"></a>testGetSQLKeywords</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsMixedCaseIdentifiers"></a>testSupportsMixedCaseIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsDifferentTableCorrelationNames"></a>testSupportsDifferentTableCorrelationNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxCursorNameLength"></a>testGetMaxCursorNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsGroupBy"></a>testSupportsGroupBy</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDefaultTransactionIsolation"></a>testGetDefaultTransactionIsolation</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetNumericFunctions"></a>testGetNumericFunctions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsANSI92EntryLevelSQL"></a>testSupportsANSI92EntryLevelSQL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsAlterTableWithDropColumn"></a>testSupportsAlterTableWithDropColumn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSearchStringEscape"></a>testGetSearchStringEscape</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsFullOuterJoins"></a>testSupportsFullOuterJoins</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCatalogsInTableDefinitions"></a>testSupportsCatalogsInTableDefinitions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsOpenCursorsAcrossRollback"></a>testSupportsOpenCursorsAcrossRollback</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsPositionedUpdate"></a>testSupportsPositionedUpdate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testOthersUpdatesAreVisibleInteger"></a>testOthersUpdatesAreVisibleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxProcedureNameLength"></a>testGetMaxProcedureNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsMultipleResultSets"></a>testSupportsMultipleResultSets</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetUDTsStringStringStringIntegerArray"></a>testGetUDTsStringStringStringIntegerArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetColumnPrivilegesStringStringStringString"></a>testGetColumnPrivilegesStringStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxColumnsInIndex"></a>testGetMaxColumnsInIndex</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxColumnsInTable"></a>testGetMaxColumnsInTable</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetTimeDateFunctions"></a>testGetTimeDateFunctions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxRowSize"></a>testGetMaxRowSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDriverMajorVersion"></a>testGetDriverMajorVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsTransactionIsolationLevelInteger"></a>testSupportsTransactionIsolationLevelInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testAllProceduresAreCallable"></a>testAllProceduresAreCallable</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDriverVersion"></a>testGetDriverVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxColumnNameLength"></a>testGetMaxColumnNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testUpdatesAreDetectedInteger"></a>testUpdatesAreDetectedInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetTableTypes"></a>testGetTableTypes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSubqueriesInExists"></a>testSupportsSubqueriesInExists</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSubqueriesInIns"></a>testSupportsSubqueriesInIns</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsResultSetTypeInteger"></a>testSupportsResultSetTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsGroupByBeyondSelect"></a>testSupportsGroupByBeyondSelect</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsExtendedSQLGrammar"></a>testSupportsExtendedSQLGrammar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDatabaseMinorVersion"></a>testGetDatabaseMinorVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testOwnInsertsAreVisibleInteger"></a>testOwnInsertsAreVisibleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxTablesInSelect"></a>testGetMaxTablesInSelect</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsConvert"></a>testSupportsConvert</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsRefCursors"></a>testSupportsRefCursors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetRowIdLifetime"></a>testGetRowIdLifetime</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSuperTypesStringStringString"></a>testGetSuperTypesStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetJDBCMajorVersion"></a>testGetJDBCMajorVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsConvertIntegerInteger"></a>testSupportsConvertIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetTablePrivilegesStringStringString"></a>testGetTablePrivilegesStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsNonNullableColumns"></a>testSupportsNonNullableColumns</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsOrderByUnrelated"></a>testSupportsOrderByUnrelated</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSchemasInTableDefinitions"></a>testSupportsSchemasInTableDefinitions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testOwnUpdatesAreVisibleInteger"></a>testOwnUpdatesAreVisibleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetBestRowIdentifierStringStringStringIntegerBoolean"></a>testGetBestRowIdentifierStringStringStringIntegerBoolean</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsOuterJoins"></a>testSupportsOuterJoins</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetColumnsStringStringStringString"></a>testGetColumnsStringStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSelectForUpdate"></a>testSupportsSelectForUpdate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsStatementPooling"></a>testSupportsStatementPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testAutoCommitFailureClosesAllResultSets"></a>testAutoCommitFailureClosesAllResultSets</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetTypeInfo"></a>testGetTypeInfo</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxStatements"></a>testGetMaxStatements</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testDataDefinitionCausesTransactionCommit"></a>testDataDefinitionCausesTransactionCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSavepoints"></a>testSupportsSavepoints</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetConnection"></a>testGetConnection</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsColumnAliasing"></a>testSupportsColumnAliasing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsUnionAll"></a>testSupportsUnionAll</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxIndexLength"></a>testGetMaxIndexLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetFunctionsStringStringString"></a>testGetFunctionsStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetCatalogSeparator"></a>testGetCatalogSeparator</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSuperTablesStringStringString"></a>testGetSuperTablesStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCatalogsInDataManipulation"></a>testSupportsCatalogsInDataManipulation</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsAlterTableWithAddColumn"></a>testSupportsAlterTableWithAddColumn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testCheckOpen"></a>testCheckOpen</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testLocatorsUpdateCopy"></a>testLocatorsUpdateCopy</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsBatchUpdates"></a>testSupportsBatchUpdates</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsDataDefinitionAndDataManipulationTransactions"></a>testSupportsDataDefinitionAndDataManipulationTransactions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetTablesStringStringStringStringArray"></a>testGetTablesStringStringStringStringArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetFunctionColumnsStringStringStringString"></a>testGetFunctionColumnsStringStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetUserName"></a>testGetUserName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSchemaTerm"></a>testGetSchemaTerm</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testStoresMixedCaseQuotedIdentifiers"></a>testStoresMixedCaseQuotedIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetStringFunctions"></a>testGetStringFunctions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsLimitedOuterJoins"></a>testSupportsLimitedOuterJoins</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsExpressionsInOrderBy"></a>testSupportsExpressionsInOrderBy</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testNullArguments"></a>testNullArguments</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetURL"></a>testGetURL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetCatalogTerm"></a>testGetCatalogTerm</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetProcedureTerm"></a>testGetProcedureTerm</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsCoreSQLGrammar"></a>testSupportsCoreSQLGrammar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetCatalogs"></a>testGetCatalogs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxConnections"></a>testGetMaxConnections</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSubqueriesInQuantifieds"></a>testSupportsSubqueriesInQuantifieds</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxCatalogNameLength"></a>testGetMaxCatalogNameLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSubqueriesInComparisons"></a>testSupportsSubqueriesInComparisons</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetProceduresStringStringString"></a>testGetProceduresStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testStoresMixedCaseIdentifiers"></a>testStoresMixedCaseIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDatabaseProductName"></a>testGetDatabaseProductName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testIsCatalogAtStart"></a>testIsCatalogAtStart</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSQLStateType"></a>testGetSQLStateType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testOthersDeletesAreVisibleInteger"></a>testOthersDeletesAreVisibleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsUnion"></a>testSupportsUnion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testStoresUpperCaseQuotedIdentifiers"></a>testStoresUpperCaseQuotedIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxBinaryLiteralLength"></a>testGetMaxBinaryLiteralLength</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsSchemasInDataManipulation"></a>testSupportsSchemasInDataManipulation</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsResultSetHoldabilityInteger"></a>testSupportsResultSetHoldabilityInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetSystemFunctions"></a>testGetSystemFunctions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testStoresUpperCaseIdentifiers"></a>testStoresUpperCaseIdentifiers</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetDriverMinorVersion"></a>testGetDriverMinorVersion</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsTableCorrelationNames"></a>testSupportsTableCorrelationNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testIsReadOnly"></a>testIsReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsANSI92IntermediateSQL"></a>testSupportsANSI92IntermediateSQL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetCrossReferenceStringStringStringStringStringString"></a>testGetCrossReferenceStringStringStringStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetResultSetHoldability"></a>testGetResultSetHoldability</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testGetMaxLogicalLobSize"></a>testGetMaxLogicalLobSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testDoesMaxRowSizeIncludeBlobs"></a>testDoesMaxRowSizeIncludeBlobs</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingDatabaseMetaData.testSupportsLikeEscapeClause"></a>testSupportsLikeEscapeClause</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestBasicDataSourceMXBean"></a>
<h3>TestBasicDataSourceMXBean</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSourceMXBean.testDefaultSchema"></a>testDefaultSchema</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestBasicDataSourceMXBean.testMXBeanCompliance"></a>testMXBeanCompliance</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDelegatingResultSet"></a>
<h3>TestDelegatingResultSet</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetUnicodeStreamInteger"></a>testGetUnicodeStreamInteger</td>
<td>0.020 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBlobInteger"></a>testGetBlobInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetDateStringCalendar"></a>testGetDateStringCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalInteger"></a>testGetBigDecimalInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testRowUpdated"></a>testRowUpdated</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateClobStringReader"></a>testUpdateClobStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetSQLXMLInteger"></a>testGetSQLXMLInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBytesString"></a>testGetBytesString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNClobIntegerReader"></a>testUpdateNClobIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectSQLType"></a>testUpdateObjectStringObjectSQLType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetObjectIntegerMap"></a>testGetObjectIntegerMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBlobIntegerInputStream"></a>testUpdateBlobIntegerInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateDateIntegerSqlDate"></a>testUpdateDateIntegerSqlDate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateRowIdStringRowId"></a>testUpdateRowIdStringRowId</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateTimeStringTime"></a>testUpdateTimeStringTime</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimeString"></a>testGetTimeString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetURLString"></a>testGetURLString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectSQLTypeInteger"></a>testUpdateObjectIntegerObjectSQLTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetNCharacterStreamInteger"></a>testGetNCharacterStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBinaryStreamIntegerInputStreamLong"></a>testUpdateBinaryStreamIntegerInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetNClobInteger"></a>testGetNClobInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetRowIdString"></a>testGetRowIdString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimeIntegerCalendar"></a>testGetTimeIntegerCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetRowIdInteger"></a>testGetRowIdInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetDoubleString"></a>testGetDoubleString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testBeforeFirst"></a>testBeforeFirst</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateAsciiStreamStringInputStreamLong"></a>testUpdateAsciiStreamStringInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateShortStringShort"></a>testUpdateShortStringShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateAsciiStreamIntegerInputStreamInteger"></a>testUpdateAsciiStreamIntegerInputStreamInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObject"></a>testUpdateObjectIntegerObject</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testAbsolutes"></a>testAbsolutes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testFindColumnString"></a>testFindColumnString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetLongInteger"></a>testGetLongInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBinaryStreamStringInputStream"></a>testUpdateBinaryStreamStringInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimestampStringCalendar"></a>testGetTimestampStringCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateDateStringSqlDate"></a>testUpdateDateStringSqlDate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateClobStringClob"></a>testUpdateClobStringClob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateStringStringString"></a>testUpdateStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testupdateobjectstringobjectinteger"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger"></a><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testupdateobjectstringobjectinteger">testUpdateObjectStringObjectInteger</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger');"><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger-off"> + </span><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateTimestampIntegerTimestamp"></a>testUpdateTimestampIntegerTimestamp</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateCharacterStreamIntegerReader"></a>testUpdateCharacterStreamIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateRow"></a>testUpdateRow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateFloatStringFloat"></a>testUpdateFloatStringFloat</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testFirst"></a>testFirst</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetArrayString"></a>testGetArrayString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testLast"></a>testLast</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testNext"></a>testNext</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testWrap"></a>testWrap</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBinaryStreamIntegerInputStreamInteger"></a>testUpdateBinaryStreamIntegerInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetStatement"></a>testGetStatement</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testToString"></a>testToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNClobIntegerNClob"></a>testUpdateNClobIntegerNClob</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testRefreshRow"></a>testRefreshRow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBinaryStreamIntegerInputStream"></a>testUpdateBinaryStreamIntegerInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateCharacterStreamStringReaderLong"></a>testUpdateCharacterStreamStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBytesIntegerByteArray"></a>testUpdateBytesIntegerByteArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetDateIntegerCalendar"></a>testGetDateIntegerCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateTimeIntegerTime"></a>testUpdateTimeIntegerTime</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetShortString"></a>testGetShortString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBlobStringBlob"></a>testUpdateBlobStringBlob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectSQLTypeInteger"></a>testUpdateObjectStringObjectSQLTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetAsciiStreamString"></a>testGetAsciiStreamString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateTimestampStringTimestamp"></a>testUpdateTimestampStringTimestamp</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateByteStringByte"></a>testUpdateByteStringByte</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testgetbigdecimalstringinteger"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger"></a><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testgetbigdecimalstringinteger">testGetBigDecimalStringInteger</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger');"><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger-off"> + </span><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateAsciiStreamIntegerInputStream"></a>testUpdateAsciiStreamIntegerInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetHoldability"></a>testGetHoldability</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateClobIntegerReader"></a>testUpdateClobIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNStringStringString"></a>testUpdateNStringStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateFloatIntegerFloat"></a>testUpdateFloatIntegerFloat</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateIntIntegerInteger"></a>testUpdateIntIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testIsBeforeFirst"></a>testIsBeforeFirst</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObject"></a>testUpdateObjectStringObject</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testPrevious"></a>testPrevious</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNStringIntegerString"></a>testUpdateNStringIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateSQLXMLIntegerSQLXML"></a>testUpdateSQLXMLIntegerSQLXML</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBlobIntegerBlob"></a>testUpdateBlobIntegerBlob</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetRefInteger"></a>testGetRefInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testSetFetchSizeInteger"></a>testSetFetchSizeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetType"></a>testGetType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalString"></a>testGetBigDecimalString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetNClobString"></a>testGetNClobString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNCharacterStreamIntegerReader"></a>testUpdateNCharacterStreamIntegerReader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetRefString"></a>testGetRefString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetConcurrency"></a>testGetConcurrency</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNullString"></a>testUpdateNullString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateSQLXMLStringSQLXML"></a>testUpdateSQLXMLStringSQLXML</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBooleanString"></a>testGetBooleanString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetSQLXMLString"></a>testGetSQLXMLString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBytesStringByteArray"></a>testUpdateBytesStringByteArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBinaryStreamStringInputStreamLong"></a>testUpdateBinaryStreamStringInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testRowDeleted"></a>testRowDeleted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetDoubleInteger"></a>testGetDoubleInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetFetchSize"></a>testGetFetchSize</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateAsciiStreamStringInputStreamInteger"></a>testUpdateAsciiStreamStringInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetStringInteger"></a>testGetStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetCharacterStreamString"></a>testGetCharacterStreamString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateRowIdIntegerRowId"></a>testUpdateRowIdIntegerRowId</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNCharacterStreamStringReaderLong"></a>testUpdateNCharacterStreamStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNClobStringReader"></a>testUpdateNClobStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetByteInteger"></a>testGetByteInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetNStringString"></a>testGetNStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateClobIntegerReaderLong"></a>testUpdateClobIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateDoubleStringDouble"></a>testUpdateDoubleStringDouble</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetObjectString"></a>testGetObjectString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetFetchDirection"></a>testGetFetchDirection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNullInteger"></a>testUpdateNullInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testSetFetchDirectionInteger"></a>testSetFetchDirectionInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testInsertRow"></a>testInsertRow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testDeleteRow"></a>testDeleteRow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectSQLType"></a>testUpdateObjectIntegerObjectSQLType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBlobIntegerInputStreamLong"></a>testUpdateBlobIntegerInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testgetbigdecimalintegerinteger"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger"></a><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testgetbigdecimalintegerinteger">testGetBigDecimalIntegerInteger</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger');"><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger-off"> + </span><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetClobInteger"></a>testGetClobInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateCharacterStreamIntegerReaderInteger"></a>testUpdateCharacterStreamIntegerReaderInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateByteIntegerByte"></a>testUpdateByteIntegerByte</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateClobStringReaderLong"></a>testUpdateClobStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetUnicodeStreamString"></a>testGetUnicodeStreamString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNCharacterStreamIntegerReaderLong"></a>testUpdateNCharacterStreamIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetNStringInteger"></a>testGetNStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateStringIntegerString"></a>testUpdateStringIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testRowInserted"></a>testRowInserted</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimestampIntegerCalendar"></a>testGetTimestampIntegerCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetFloatString"></a>testGetFloatString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetObjectInteger"></a>testGetObjectInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetShortInteger"></a>testGetShortInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimestampString"></a>testGetTimestampString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBooleanStringBoolean"></a>testUpdateBooleanStringBoolean</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimeStringCalendar"></a>testGetTimeStringCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBinaryStreamStringInputStreamInteger"></a>testUpdateBinaryStreamStringInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testWasNull"></a>testWasNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateAsciiStreamIntegerInputStreamLong"></a>testUpdateAsciiStreamIntegerInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimeInteger"></a>testGetTimeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBigDecimalIntegerBigDecimal"></a>testUpdateBigDecimalIntegerBigDecimal</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateRefIntegerRef"></a>testUpdateRefIntegerRef</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetIntInteger"></a>testGetIntInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetURLInteger"></a>testGetURLInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateArrayStringArray"></a>testUpdateArrayStringArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBlobStringInputStreamLong"></a>testUpdateBlobStringInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testupdateobjectintegerobjectinteger"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger"></a><a href="#surefire--org.apache.commons.dbcp2.testdelegatingresultset.testupdateobjectintegerobjectinteger">testUpdateObjectIntegerObjectInteger</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger');"><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger-off"> + </span><span id="org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetLongString"></a>testGetLongString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNClobStringNClob"></a>testUpdateNClobStringNClob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetMetaData"></a>testGetMetaData</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetFloatInteger"></a>testGetFloatInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateClobIntegerClob"></a>testUpdateClobIntegerClob</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetIntString"></a>testGetIntString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateIntStringInteger"></a>testUpdateIntStringInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNClobIntegerReaderLong"></a>testUpdateNClobIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateCharacterStreamIntegerReaderLong"></a>testUpdateCharacterStreamIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateArrayIntegerArray"></a>testUpdateArrayIntegerArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateLongIntegerLong"></a>testUpdateLongIntegerLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetClobString"></a>testGetClobString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testMoveToCurrentRow"></a>testMoveToCurrentRow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateLongStringLong"></a>testUpdateLongStringLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testMoveToInsertRow"></a>testMoveToInsertRow</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetObjectIntegerClass"></a>testGetObjectIntegerClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetDateInteger"></a>testGetDateInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateRefStringRef"></a>testUpdateRefStringRef</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetAsciiStreamInteger"></a>testGetAsciiStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBlobString"></a>testGetBlobString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetRow"></a>testGetRow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateCharacterStreamStringReaderInteger"></a>testUpdateCharacterStreamStringReaderInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBooleanIntegerBoolean"></a>testUpdateBooleanIntegerBoolean</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testCancelRowUpdates"></a>testCancelRowUpdates</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testIsLast"></a>testIsLast</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNClobStringReaderLong"></a>testUpdateNClobStringReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBinaryStreamInteger"></a>testGetBinaryStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBytesInteger"></a>testGetBytesInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetStringString"></a>testGetStringString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testIsAfterLast"></a>testIsAfterLast</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetCharacterStreamInteger"></a>testGetCharacterStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateNCharacterStreamStringReader"></a>testUpdateNCharacterStreamStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetObjectStringClass"></a>testGetObjectStringClass</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBigDecimalStringBigDecimal"></a>testUpdateBigDecimalStringBigDecimal</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateBlobStringInputStream"></a>testUpdateBlobStringInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testIsFirst"></a>testIsFirst</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testAfterLast"></a>testAfterLast</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetCursorName"></a>testGetCursorName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateShortIntegerShort"></a>testUpdateShortIntegerShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetObjectStringMap"></a>testGetObjectStringMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetNCharacterStreamString"></a>testGetNCharacterStreamString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testAbsoluteInteger"></a>testAbsoluteInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateCharacterStreamStringReader"></a>testUpdateCharacterStreamStringReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBinaryStreamString"></a>testGetBinaryStreamString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateDoubleIntegerDouble"></a>testUpdateDoubleIntegerDouble</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetWarnings"></a>testGetWarnings</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testRelativeInteger"></a>testRelativeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetArrayInteger"></a>testGetArrayInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBooleanInteger"></a>testGetBooleanInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetByteString"></a>testGetByteString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateAsciiStreamStringInputStream"></a>testUpdateAsciiStreamStringInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetDateString"></a>testGetDateString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingResultSet.testGetTimestampInteger"></a>testGetTimestampInteger</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPoolingConnection"></a>
<h3>TestPoolingConnection</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareCall"></a>testPrepareCall</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testToStringStackOverflow"></a>testToStringStackOverflow</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareStatementWithColumnIndexes"></a>testPrepareStatementWithColumnIndexes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareStatementWithAutoGeneratedKeys"></a>testPrepareStatementWithAutoGeneratedKeys</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareStatementWithColumnNames"></a>testPrepareStatementWithColumnNames</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareCallWithResultSetHoldability"></a>testPrepareCallWithResultSetHoldability</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareStatementWithResultSetHoldability"></a>testPrepareStatementWithResultSetHoldability</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareCallWithResultSetConcurrency"></a>testPrepareCallWithResultSetConcurrency</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareStatementWithResultSetConcurrency"></a>testPrepareStatementWithResultSetConcurrency</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPoolingConnection.testPrepareStatement"></a>testPrepareStatement</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx"></a>
<h3>TestManagedDataSourceInTx</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testThreaded"></a>testThreaded</td>
<td>3.044 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testOpening"></a>testOpening</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testHashing"></a>testHashing</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testClosing"></a>testClosing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testBackPointers"></a>testBackPointers</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSimple2"></a>testSimple2</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSimple"></a>testSimple</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSetNullTransactionRegistry"></a>testSetNullTransactionRegistry</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualsSameDelegateNoUnderlyingAccess"></a>testManagedConnectionEqualsSameDelegateNoUnderlyingAccess</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testTransactionRegistryNotInitialized"></a>testTransactionRegistryNotInitialized</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualsSameDelegate"></a>testManagedConnectionEqualsSameDelegate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSetTransactionRegistry"></a>testSetTransactionRegistry</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualsNull"></a>testManagedConnectionEqualsNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualsType"></a>testManagedConnectionEqualsType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualInnermost"></a>testManagedConnectionEqualInnermost</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualsReflexive"></a>testManagedConnectionEqualsReflexive</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSetTransactionRegistryAlreadySet"></a>testSetTransactionRegistryAlreadySet</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testGetConnectionInAfterCompletion"></a>testGetConnectionInAfterCompletion</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testNestedConnections"></a>testNestedConnections</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSharedConnection"></a>testSharedConnection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testReadOnly"></a>testReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testConnectionReturnOnCommit"></a>testConnectionReturnOnCommit</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCloseInTransaction"></a>testCloseInTransaction</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testManagedConnectionEqualsFail"></a>testManagedConnectionEqualsFail</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testHashCode"></a>testHashCode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testMaxTotal"></a>testMaxTotal</td>
<td>0.107 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testCommit"></a>testCommit</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testClearWarnings"></a>testClearWarnings</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testSharedTransactionConversion"></a>testSharedTransactionConversion</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestManagedDataSourceInTx.testDoubleReturn"></a>testDoubleReturn</td>
<td>0.003 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestAbandonedTrace"></a>
<h3>TestAbandonedTrace</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestAbandonedTrace.testDeprecated"></a>testDeprecated</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.PooledConnectionManagerTest"></a>
<h3>PooledConnectionManagerTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.PooledConnectionManagerTest.testSetPasswordString"></a>testSetPasswordString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.PooledConnectionManagerTest.testSetPasswordCharArray"></a>testSetPasswordCharArray</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestFactory"></a>
<h3>TestFactory</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B1.5D"></a>testJNDI2Pools(String, String)[1]</td>
<td>0.010 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B2.5D"></a>testJNDI2Pools(String, String)[2]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B3.5D"></a>testJNDI2Pools(String, String)[3]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B4.5D"></a>testJNDI2Pools(String, String)[4]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B5.5D"></a>testJNDI2Pools(String, String)[5]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B6.5D"></a>testJNDI2Pools(String, String)[6]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B7.5D"></a>testJNDI2Pools(String, String)[7]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B8.5D"></a>testJNDI2Pools(String, String)[8]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B9.5D"></a>testJNDI2Pools(String, String)[9]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B10.5D"></a>testJNDI2Pools(String, String)[10]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B11.5D"></a>testJNDI2Pools(String, String)[11]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B12.5D"></a>testJNDI2Pools(String, String)[12]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B13.5D"></a>testJNDI2Pools(String, String)[13]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B14.5D"></a>testJNDI2Pools(String, String)[14]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B15.5D"></a>testJNDI2Pools(String, String)[15]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B16.5D"></a>testJNDI2Pools(String, String)[16]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B17.5D"></a>testJNDI2Pools(String, String)[17]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B18.5D"></a>testJNDI2Pools(String, String)[18]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B19.5D"></a>testJNDI2Pools(String, String)[19]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B20.5D"></a>testJNDI2Pools(String, String)[20]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B21.5D"></a>testJNDI2Pools(String, String)[21]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B22.5D"></a>testJNDI2Pools(String, String)[22]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B23.5D"></a>testJNDI2Pools(String, String)[23]</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B24.5D"></a>testJNDI2Pools(String, String)[24]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B25.5D"></a>testJNDI2Pools(String, String)[25]</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestFactory.testJNDI2Pools.28String.2C_String.29.5B26.5D"></a>testJNDI2Pools(String, String)[26]</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.datasources.TestPoolKey"></a>
<h3>TestPoolKey</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPoolKey.testToString"></a>testToString</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPoolKey.testHashcode"></a>testHashcode</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.datasources.TestPoolKey.testEquals"></a>testEquals</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDelegatingConnection"></a>
<h3>TestDelegatingConnection</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetDelegate"></a>testGetDelegate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testReadOnlyCaching"></a>testReadOnlyCaching</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCreateSQLXML"></a>testCreateSQLXML</td>
<td>0.006 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCreateStruct"></a>testCreateStruct</td>
<td>0.006 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testPassivateWithResultSetCloseExceptionAndStatementCloseException"></a>testPassivateWithResultSetCloseExceptionAndStatementCloseException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetClientInfo"></a>testGetClientInfo</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testSetSavepoint"></a>testSetSavepoint</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testSetDefaultQueryTimeout"></a>testSetDefaultQueryTimeout</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetNetworkTimeout"></a>testGetNetworkTimeout</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testAbort"></a>testAbort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCreateNClob"></a>testCreateNClob</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testReleaseSavepoint"></a>testReleaseSavepoint</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCreateArrayOf"></a>testCreateArrayOf</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testSetClientInfo"></a>testSetClientInfo</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testRollbackSavepoint"></a>testRollbackSavepoint</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetHoldability"></a>testGetHoldability</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testPassivateWithStatementCloseException"></a>testPassivateWithStatementCloseException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetTypeMap"></a>testGetTypeMap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCheckOpenNull"></a>testCheckOpenNull</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testPassivateWithResultSetCloseException"></a>testPassivateWithResultSetCloseException</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testNativeSQL"></a>testNativeSQL</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testIsClosed"></a>testIsClosed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testRollback"></a>testRollback</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetDefaultQueryTimeoutDuration"></a>testGetDefaultQueryTimeoutDuration</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCreateBlob"></a>testCreateBlob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCreateClob"></a>testCreateClob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testIsClosedNullDelegate"></a>testIsClosedNullDelegate</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetClientInfoString"></a>testGetClientInfoString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCheckOpen"></a>testCheckOpen</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testConnectionToString"></a>testConnectionToString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testCommit"></a>testCommit</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testAutoCommitCaching"></a>testAutoCommitCaching</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetDefaultQueryTimeout"></a>testGetDefaultQueryTimeout</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testGetCacheState"></a>testGetCacheState</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testSetHoldability"></a>testSetHoldability</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testUnwrap"></a>testUnwrap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingConnection.testSetNetworkTimeout"></a>testSetNetworkTimeout</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestConnectionWithNarayana"></a>
<h3>TestConnectionWithNarayana</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestConnectionWithNarayana.testConnectionInTimeout"></a>testConnectionInTimeout</td>
<td>5.419 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestConnectionWithNarayana.testConnectionCommitAfterTimeout"></a>testConnectionCommitAfterTimeout</td>
<td>3.009 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestConnectionWithNarayana.testRepeatedGetConnectionInTimeout"></a>testRepeatedGetConnectionInTimeout</td>
<td>3.018 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPStmtPooling"></a>
<h3>TestPStmtPooling</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPooling.testStmtPool"></a>testStmtPool</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPooling.testBatchUpdate"></a>testBatchUpdate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPooling.testClosePool"></a>testClosePool</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPooling.testCallableStatementPooling"></a>testCallableStatementPooling</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPooling.testMultipleClose"></a>testMultipleClose</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestListException"></a>
<h3>TestListException</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestListException.testExceptionList"></a>testExceptionList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestListException.testNulls"></a>testNulls</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestDelegatingPreparedStatement"></a>
<h3>TestDelegatingPreparedStatement</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testGetDelegate"></a>testGetDelegate</td>
<td>0.025 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetClobIntegerReader"></a>testSetClobIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetByteIntegerByte"></a>testSetByteIntegerByte</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetFloatIntegerFloat"></a>testSetFloatIntegerFloat</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetIntIntegerInteger"></a>testSetIntIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testExecuteQueryReturnsNotNull"></a>testExecuteQueryReturnsNotNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testExecute"></a>testExecute</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBigDecimalIntegerBigDecimal"></a>testSetBigDecimalIntegerBigDecimal</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBooleanIntegerBoolean"></a>testSetBooleanIntegerBoolean</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testExecuteUpdate"></a>testExecuteUpdate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetRefIntegerRef"></a>testSetRefIntegerRef</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetCharacterStreamIntegerReader"></a>testSetCharacterStreamIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetClobIntegerClob"></a>testSetClobIntegerClob</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testGetParameterMetaData"></a>testGetParameterMetaData</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetLongIntegerLong"></a>testSetLongIntegerLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetRowIdIntegerRowId"></a>testSetRowIdIntegerRowId</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetObjectIntegerObjectSQLTypeInteger"></a>testSetObjectIntegerObjectSQLTypeInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetObjectIntegerObjectIntegerInteger"></a>testSetObjectIntegerObjectIntegerInteger</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetSQLXMLIntegerSQLXML"></a>testSetSQLXMLIntegerSQLXML</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetURLIntegerUrl"></a>testSetURLIntegerUrl</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNClobIntegerReader"></a>testSetNClobIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetDateIntegerSqlDate"></a>testSetDateIntegerSqlDate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetCharacterStreamIntegerReaderInteger"></a>testSetCharacterStreamIntegerReaderInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testAddBatch"></a>testAddBatch</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetAsciiStreamIntegerInputStream"></a>testSetAsciiStreamIntegerInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testClearParameters"></a>testClearParameters</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBinaryStreamIntegerInputStream"></a>testSetBinaryStreamIntegerInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetTimestampIntegerTimestamp"></a>testSetTimestampIntegerTimestamp</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testExecuteQuery"></a>testExecuteQuery</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNCharacterStreamIntegerReader"></a>testSetNCharacterStreamIntegerReader</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetArrayIntegerArray"></a>testSetArrayIntegerArray</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetStringIntegerString"></a>testSetStringIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetAsciiStreamIntegerInputStreamInteger"></a>testSetAsciiStreamIntegerInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetCharacterStreamIntegerReaderLong"></a>testSetCharacterStreamIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBytesIntegerByteArray"></a>testSetBytesIntegerByteArray</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testExecuteLargeUpdate"></a>testExecuteLargeUpdate</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNullIntegerInteger"></a>testSetNullIntegerInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetShortIntegerShort"></a>testSetShortIntegerShort</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetObjectIntegerObjectSQLType"></a>testSetObjectIntegerObjectSQLType</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNClobIntegerReaderLong"></a>testSetNClobIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBlobIntegerInputStreamLong"></a>testSetBlobIntegerInputStreamLong</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetTimeIntegerTimeCalendar"></a>testSetTimeIntegerTimeCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetDateIntegerSqlDateCalendar"></a>testSetDateIntegerSqlDateCalendar</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testExecuteQueryReturnsNull"></a>testExecuteQueryReturnsNull</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetUnicodeStreamIntegerInputStreamInteger"></a>testSetUnicodeStreamIntegerInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testGetMetaData"></a>testGetMetaData</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetTimeIntegerTime"></a>testSetTimeIntegerTime</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBinaryStreamIntegerInputStreamInteger"></a>testSetBinaryStreamIntegerInputStreamInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNCharacterStreamIntegerReaderLong"></a>testSetNCharacterStreamIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetObjectIntegerObjectInteger"></a>testSetObjectIntegerObjectInteger</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetDoubleIntegerDouble"></a>testSetDoubleIntegerDouble</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNStringIntegerString"></a>testSetNStringIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBlobIntegerBlob"></a>testSetBlobIntegerBlob</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetAsciiStreamIntegerInputStreamLong"></a>testSetAsciiStreamIntegerInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetClobIntegerReaderLong"></a>testSetClobIntegerReaderLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNullIntegerIntegerString"></a>testSetNullIntegerIntegerString</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetObjectIntegerObject"></a>testSetObjectIntegerObject</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBlobIntegerInputStream"></a>testSetBlobIntegerInputStream</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetNClobIntegerNClob"></a>testSetNClobIntegerNClob</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetBinaryStreamIntegerInputStreamLong"></a>testSetBinaryStreamIntegerInputStreamLong</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestDelegatingPreparedStatement.testSetTimestampIntegerTimestampCalendar"></a>testSetTimestampIntegerTimestampCalendar</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.managed.TestSynchronizationOrder"></a>
<h3>TestSynchronizationOrder</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestSynchronizationOrder.testInterposedSynchronization"></a>testInterposedSynchronization</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.managed.TestSynchronizationOrder.testSessionSynchronization"></a>testSessionSynchronization</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource"></a>
<h3>TestPStmtPoolingBasicDataSource</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testThreaded"></a>testThreaded</td>
<td>2.903 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCanCloseStatementTwice"></a>testCanCloseStatementTwice</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testNoRsetClose"></a>testNoRsetClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testOpening"></a>testOpening</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCanCloseConnectionTwice"></a>testCanCloseConnectionTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testIsClosed"></a>testIsClosed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCanCloseCallableStatementTwice"></a>testCanCloseCallableStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testAutoCommitBehavior"></a>testAutoCommitBehavior</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testHashing"></a>testHashing</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCanClosePreparedStatementTwice"></a>testCanClosePreparedStatementTwice</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testClosing"></a>testClosing</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPrepareStatementOptions"></a>testPrepareStatementOptions</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testBackPointers"></a>testBackPointers</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testHashCode"></a>testHashCode</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testConnectionsAreDistinct"></a>testConnectionsAreDistinct</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testMaxTotal"></a>testMaxTotal</td>
<td>0.102 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testRepeatedBorrowAndReturn"></a>testRepeatedBorrowAndReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCanCloseResultSetTwice"></a>testCanCloseResultSetTwice</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testClearWarnings"></a>testClearWarnings</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testSimple2"></a>testSimple2</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testSimple"></a>testSimple</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEmptyValidationQuery"></a>testEmptyValidationQuery</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCreateConnectionFactoryWithConnectionFactoryClassName"></a>testCreateConnectionFactoryWithConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testValidationQueryTimoutFail"></a>testValidationQueryTimoutFail</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testIsWrapperFor"></a>testIsWrapperFor</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testConcurrentInvalidateBorrow"></a>testConcurrentInvalidateBorrow</td>
<td>0.046 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testSetValidationTestProperties"></a>testSetValidationTestProperties</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCreateConnectionFactoryWithoutConnectionFactoryClassName"></a>testCreateConnectionFactoryWithoutConnectionFactoryClassName</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testRollbackReadOnly"></a>testRollbackReadOnly</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testClose"></a>testClose</td>
<td>0 s</td></tr>
<tr>
<td><a href="#surefire--org.apache.commons.dbcp2.testpstmtpoolingbasicdatasource.testevict"><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></a></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEvict"></a><a href="#surefire--org.apache.commons.dbcp2.testpstmtpoolingbasicdatasource.testevict">testEvict</a>
<div><a href="javascript:toggleDisplay('org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEvict');"><span id="org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEvict-off"> + </span><span id="org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEvict-on"> - </span>[ Detail ]</a></div></td>
<td>0 s</td></tr>
<tr>
<td>-</td>
<td>void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td>
<td>-</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testStart"></a>testStart</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPropertyTestOnReturn"></a>testPropertyTestOnReturn</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testValidationQueryTimeoutSucceed"></a>testValidationQueryTimeoutSucceed</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testStartInitializes"></a>testStartInitializes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testMaxTotalZero"></a>testMaxTotalZero</td>
<td>0.105 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPooling"></a>testPooling</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testConnectionMBeansDisabled"></a>testConnectionMBeansDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testMaxConnLifetimeExceeded"></a>testMaxConnLifetimeExceeded</td>
<td>0.506 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testValidationQueryTimeoutNegative"></a>testValidationQueryTimeoutNegative</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPoolCloseRTE"></a>testPoolCloseRTE</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testInstanceNotFoundExceptionLogSuppressed"></a>testInstanceNotFoundExceptionLogSuppressed</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testSetAutoCommitTrueOnClose"></a>testSetAutoCommitTrueOnClose</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes"></a>testNoOverlapBetweenDisconnectionAndIgnoreSqlCodes</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testConcurrentInitBorrow"></a>testConcurrentInitBorrow</td>
<td>0.483 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testDeprecatedAccessors"></a>testDeprecatedAccessors</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testManualConnectionEvict"></a>testManualConnectionEvict</td>
<td>0.106 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testValidationQueryTimeoutZero"></a>testValidationQueryTimeoutZero</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testMaxConnLifetimeExceededMutedLog"></a>testMaxConnLifetimeExceededMutedLog</td>
<td>0.508 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEmptyInitConnectionSql"></a>testEmptyInitConnectionSql</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testDriverClassLoader"></a>testDriverClassLoader</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testJmxDisabled"></a>testJmxDisabled</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testInitialSize"></a>testInitialSize</td>
<td>0.004 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testInvalidValidationQuery"></a>testInvalidValidationQuery</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testRestart"></a>testRestart</td>
<td>0.208 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testNoAccessToUnderlyingConnectionAllowed"></a>testNoAccessToUnderlyingConnectionAllowed</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPoolCloseCheckedException"></a>testPoolCloseCheckedException</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCreateDataSourceCleanupEvictor"></a>testCreateDataSourceCleanupEvictor</td>
<td>1.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testTransactionIsolationBehavior"></a>testTransactionIsolationBehavior</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testCreateDataSourceCleanupThreads"></a>testCreateDataSourceCleanupThreads</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testDefaultCatalog"></a>testDefaultCatalog</td>
<td>0.005 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testAccessToUnderlyingConnectionAllowed"></a>testAccessToUnderlyingConnectionAllowed</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testInvalidateConnection"></a>testInvalidateConnection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testSetProperties"></a>testSetProperties</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testMutateAbandonedConfig"></a>testMutateAbandonedConfig</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testDisconnectionIgnoreSqlCodes"></a>testDisconnectionIgnoreSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testUnwrap"></a>testUnwrap</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testJmxDoesNotExposePassword"></a>testJmxDoesNotExposePassword</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testInvalidConnectionInitSqlCollection"></a>testInvalidConnectionInitSqlCollection</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testDisconnectSqlCodes"></a>testDisconnectSqlCodes</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testInvalidConnectionInitSqlList"></a>testInvalidConnectionInitSqlList</td>
<td>0 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testIsClosedFailure"></a>testIsClosedFailure</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testLRUBehavior"></a>testLRUBehavior</td>
<td>0.213 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPreparedStatementPooling"></a>testPreparedStatementPooling</td>
<td>0.003 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPStmtPoolingAcrossClose"></a>testPStmtPoolingAcrossClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPStmtPoolingWithNoClose"></a>testPStmtPoolingWithNoClose</td>
<td>0.002 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPStmtPoolingAcrossCloseWithClearOnReturn"></a>testPStmtPoolingAcrossCloseWithClearOnReturn</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testPStmtCatalog"></a>testPStmtCatalog</td>
<td>0.001 s</td></tr>
<tr>
<td><img src="assets/images/icon-success-sml_3637b2b6cc4c2674.gif"/></td>
<td><a id="TC_org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testMultipleThreads1"></a>testMultipleThreads1</td>
<td>10.27 s</td></tr></table></section>
</section><section><a id="Failure_Details"></a>
<h2>Failure Details</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p>
<table>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.managed.TestDataSourceXAConnectionFactory.testEvict"></a>testEvict</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.managed.TestBasicManagedDataSource.testEvict"></a>testEvict</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestAbandonedBasicDataSource.testEvict"></a>testEvict</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestBasicDataSource.testEvict"></a>testEvict</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger"></a>testUpdateObjectStringObjectInteger</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectStringObjectInteger() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger"></a>testGetBigDecimalStringInteger</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalStringInteger() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger"></a>testGetBigDecimalIntegerInteger</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestDelegatingResultSet.testGetBigDecimalIntegerInteger() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger"></a>testUpdateObjectIntegerObjectInteger</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestDelegatingResultSet.testUpdateObjectIntegerObjectInteger() throws java.lang.Exception is @Disabled</td></tr>
<tr>
<td><img src="assets/images/icon-warning-sml_eb6be213ebdf9132.gif"/></td>
<td><a id="org.apache.commons.dbcp2.TestPStmtPoolingBasicDataSource.testEvict"></a>testEvict</td></tr>
<tr>
<td>-</td>
<td>skipped: void org.apache.commons.dbcp2.TestBasicDataSource.testEvict() throws java.lang.Exception is @Disabled</td></tr></table>
</section></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/rat-report.html -->

<!-- page_index: 25 -->

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
Generated at: 2025-12-16T11:58:54Z
    by Apache Creadur RAT::Core 0.17 (Apache Software Foundation)

-----------------------------------------------------
Counters
-----------------------------------------------------
    (Entries starting with '!' exceed the minimum or maximum values)
  Approved:           180    A count of approved licenses.
  Archives:           0    A count of archive files.
  Binaries:           17    A count of binary files.
  Document types:     4    A count of distinct document types.
  Ignored:            11    A count of ignored files.
  License categories: 1    A count of distinct license categories.
  License names:      1    A count of distinct license names.
  Notices:            4    A count of notice files.
  Standards:          180    A count of standard files.
  Unapproved:         0    A count of unapproved licenses.
  Unknown:            0    A count of unknown file types.

-----------------------------------------------------
Licenses detected
-----------------------------------------------------

Apache License 2.0: 180

-----------------------------------------------------
License Categories detected
-----------------------------------------------------

AL   : 180

-----------------------------------------------------
Document Types detected
-----------------------------------------------------

BINARY: 17
IGNORED: 11
NOTICE: 4
STANDARD: 180

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

  /.DS_Store
  I         application/octet-stream

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
  N         text/plain    ISO-8859-1

  /SECURITY.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /dbcp-RC.sh
  B         application/x-sh

  /dbcp-pre-RC.sh
  B         application/x-sh

  /dbcp-release.sh
  B         application/x-sh

  /doc/BasicDataSourceExample.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /doc/PoolingDataSourceExample.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /doc/PoolingDriverExample.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /doc/README.txt
  N         text/plain    ISO-8859-1

  /doc/abandon.jsp
  S         text/html    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /doc/static_structure_dia.gif
  B         image/gif

  /pom.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/changes/changes.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/changes/release-notes.vm
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/checkstyle.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/eclipse/formatter.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/spotbugs-exclude-filter.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/assembly/bin.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/assembly/src-tar-gz.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/assembly/src-zip.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/AbandonedTrace.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/BasicDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/BasicDataSourceFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/BasicDataSourceMXBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/ConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/ConnectionFactoryFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/Constants.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DataSourceConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DataSourceMXBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DelegatingCallableStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DelegatingConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DelegatingDatabaseMetaData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DelegatingPreparedStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DelegatingResultSet.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DelegatingStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DriverConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DriverFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/DriverManagerConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/Jdbc41Bridge.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/LifetimeExceededException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/ListException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/ObjectNameWrapper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PStmtKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolableCallableStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolableConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolableConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolableConnectionMXBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolablePreparedStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolingConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolingDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/PoolingDriver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/SQLExceptionList.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/SwallowedExceptionLogger.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/Utils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/cpdsadapter/ConnectionImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/cpdsadapter/DriverAdapterCPDS.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/cpdsadapter/PStmtKeyCPDS.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/cpdsadapter/PooledConnectionImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/cpdsadapter/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/AbstractConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/CPDSConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/CharArray.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/InstanceKeyDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/InstanceKeyDataSourceFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/KeyedCPDSConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/PerUserPoolDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/PerUserPoolDataSourceFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/PoolKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/PooledConnectionAndInfo.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/PooledConnectionManager.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/SharedPoolDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/SharedPoolDataSourceFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/UserPassKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/datasources/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/BasicManagedDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/DataSourceXAConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/LocalXAConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/ManagedConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/ManagedDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/PoolableManagedConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/PoolableManagedConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/SynchronizationAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/TransactionContext.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/TransactionContextListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/TransactionRegistry.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/XAConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/managed/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/dbcp2/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/javadoc/overview.html
  S         text/html    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/resources/org/apache/commons/dbcp2/LocalStrings.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/media/commons-logo-component-100.xcf
  B         image/x-xcf

  /src/media/commons-logo-component.xcf
  B         image/x-xcf

  /src/media/logo.png
  B         image/png

  /src/site/resources/download_dbcp.cgi
  I         text/x-cgi

  /src/site/resources/images/logo.png
  B         image/png

  /src/site/resources/images/uml/AbandonedObjectPool.gif
  B         image/gif

  /src/site/resources/images/uml/BasicDataSource.gif
  B         image/gif

  /src/site/resources/images/uml/ConnectionFactory.gif
  B         image/gif

  /src/site/resources/images/uml/Delegating.gif
  B         image/gif

  /src/site/resources/images/uml/PoolingConnection.gif
  B         image/gif

  /src/site/resources/images/uml/PoolingDataSource.gif
  B         image/gif

  /src/site/resources/images/uml/createDataSource.gif
  B         image/gif

  /src/site/resources/images/uml/getConnection.gif
  B         image/gif

  /src/site/resources/images/uml/prepareStatement.gif
  B         image/gif

  /src/site/resources/profile.jacoco
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/site.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/building.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/configuration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/download_dbcp.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/guide/classdiagrams.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/guide/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/guide/jndi-howto.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/guide/sequencediagrams.xml
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

  /src/site/xdoc/release-notes-1.1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release-notes-1.2.1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/release-notes-1.2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/security.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/AbstractDriverTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/Jdbc41BridgeTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/StackMessageLog.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestAbandonedBasicDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestAbandonedTrace.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestBasicDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestBasicDataSourceFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestBasicDataSourceMXBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestConnectionPool.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestConstants.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDataSourceConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDelegatingCallableStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDelegatingConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDelegatingDatabaseMetaData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDelegatingPreparedStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDelegatingResultSet.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDelegatingStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDriverConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestDriverManagerConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestJndi.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestLifetimeExceededException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestListException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPStmtKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPStmtPooling.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPStmtPoolingBasicDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestParallelCreationWithNoIdle.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPoolableConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPoolingConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPoolingDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestPoolingDriver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestSQLExceptionList.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TestUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterCallableStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterClassLoader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterDatabaseMetaData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterDriver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterPreparedStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterResultSet.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterStatement.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/TesterUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/cpdsadapter/TestDriverAdapterCPDS.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/cpdsadapter/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/CharArrayTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/ConnectionPoolDataSourceProxy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/PooledConnectionManagerTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/PooledConnectionProxy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestCPDSConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestInstanceKeyDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestKeyedCPDSConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestPerUserPoolDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestPoolKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestSharedPoolDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/TestUserPassKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/UserPassKeyTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/datasources/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestBasicManagedDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestConnectionWithNarayana.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestDataSourceXAConnectionFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestLocalXaResource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestManagedConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestManagedConnectionCachedState.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestManagedDataSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestManagedDataSourceInTx.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestPoolableManagedConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestSynchronizationOrder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TestTransactionContext.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/TesterBasicXAConnection.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/managed/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/transaction/TransactionAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/transaction/TransactionManagerAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/transaction/TransactionSynchronizationRegistryAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/dbcp2/transaction/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/commons-logging.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /target
  I         application/octet-stream     (directory)

</pre></section>
</td>
</tr>
</table>

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/japicmp.html -->

<!-- page_index: 26 -->

# Apache Commons DBCP

<table class="layout-table">
<tr>
<td>
</td>
<td>
<span>Comparing source compatibility of commons-dbcp2-2.14.0.jar against commons-dbcp2-2.13.0.jar</span>
<div>
<table>
<tr>
<td>Old:</td>
<td>
				commons-dbcp2-2.13.0.jar
			</td>
</tr>
<tr>
<td>New:</td>
<td>
				commons-dbcp2-2.14.0.jar
			</td>
</tr>
<tr>
<td>Created:</td>
<td>
				2025-12-16T11:58:55.144+0000
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
				true
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
				0.1.0
			</td>
</tr>
</table>
</div>
<div>
<span id="warning-missingclasses">
WARNING: You are using the option '--ignore-missing-classes', i.e. superclasses and
interfaces that could not be found on the classpath are ignored. Hence changes
caused by these superclasses and interfaces are not reflected in the output.
</span>
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
<a href="#japicmp--org.apache.commons.dbcp2.basicdatasource">
			org.apache.commons.dbcp2.BasicDataSource
		</a>
</td>
</tr>
<tr>
<td>
<span>UNCHANGED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.constants">
			org.apache.commons.dbcp2.Constants
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.cpdsadapter.driveradaptercpds">
			org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.datasources.instancekeydatasource">
			org.apache.commons.dbcp2.datasources.InstanceKeyDataSource
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.datasources.sharedpooldatasource">
			org.apache.commons.dbcp2.datasources.SharedPoolDataSource
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.delegatingconnection">
			org.apache.commons.dbcp2.DelegatingConnection
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.delegatingstatement">
			org.apache.commons.dbcp2.DelegatingStatement
		</a>
</td>
</tr>
<tr>
<td>
<span>UNCHANGED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.jdbc41bridge">
			org.apache.commons.dbcp2.Jdbc41Bridge
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.managed.localxaconnectionfactory-localxaresource">
			org.apache.commons.dbcp2.managed.LocalXAConnectionFactory$LocalXAResource
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.managed.managedconnection-completionlistener">
			org.apache.commons.dbcp2.managed.ManagedConnection$CompletionListener
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.poolableconnection">
			org.apache.commons.dbcp2.PoolableConnection
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.poolableconnectionfactory">
			org.apache.commons.dbcp2.PoolableConnectionFactory
		</a>
</td>
</tr>
<tr>
<td>
<span>MODIFIED</span>
</td>
<td>
<a href="#japicmp--org.apache.commons.dbcp2.poolingconnection">
			org.apache.commons.dbcp2.PoolingConnection
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
<div id="org.apache.commons.dbcp2.BasicDataSource">
<div>
<span>
<a name="org.apache.commons.dbcp2.BasicDataSource"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.BasicDataSource
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
</div>
</div>
</div>
<div>
<div id="org.apache.commons.dbcp2.Constants">
<div>
<span>
<a name="org.apache.commons.dbcp2.Constants"></a>
<span>UNCHANGED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.Constants
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
<span>Constructors:</span>
<table>
<thead>
<tr>
<td>Status</td>
<td>Modifier</td>
<td>Generic Templates</td>
<td>Constructor</td>
<td>Exceptions</td>
<td>Compatibility Changes:</td>
<td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>UNCHANGED</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>Constants()<div>
<span>Annotations:</span>
<table>
<thead>
<tr>
<td>Status:</td>
<td>Fully Qualified Name:</td>
<td>Elements:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td>
<td>java.lang.Deprecated</td>
<td>n.a.</td>
</tr>
</tbody>
</table>
</div>
</td>
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
<tr><td>ANNOTATION_DEPRECATED_ADDED</td></tr>
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
			24
		</td>
<td>
			71
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div>
<div>
</div>
</div>
</div>
<div>
<div id="org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS">
<div>
<span>
<a name="org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS"></a>
<span>MODIFIED</span>
<span> (Serializable compatible) </span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS
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
<td>3462286550346526200</td>
<td>-4820523787212147844</td>
</tr>
<tr>
<td>New</td><td>true</td>
<td>-6491507213728593230</td>
<td>-4820523787212147844</td>
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
<div id="org.apache.commons.dbcp2.datasources.InstanceKeyDataSource">
<div>
<span>
<a name="org.apache.commons.dbcp2.datasources.InstanceKeyDataSource"></a>
<span>MODIFIED</span>
<span> (Serializable compatible) </span>
<span>public</span>
<span>abstract</span>
<span>class</span>
 org.apache.commons.dbcp2.datasources.InstanceKeyDataSource
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
<td>-8936616570915298427</td>
<td>-6819270431752240878</td>
</tr>
<tr>
<td>New</td><td>true</td>
<td>-1868436432841728928</td>
<td>-6819270431752240878</td>
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
<div id="org.apache.commons.dbcp2.datasources.SharedPoolDataSource">
<div>
<span>
<a name="org.apache.commons.dbcp2.datasources.SharedPoolDataSource"></a>
<span>MODIFIED</span>
<span> (Serializable compatible) </span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.datasources.SharedPoolDataSource
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
<td>org.apache.commons.dbcp2.datasources.InstanceKeyDataSource</td>
<td>n.a.</td>
</tr>
</tbody>
</table>
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
<td>-5422492039978237089</td>
<td>-1458539734480586454</td>
</tr>
<tr>
<td>New</td><td>true</td>
<td>-6252325996008993822</td>
<td>-1458539734480586454</td>
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
<div id="org.apache.commons.dbcp2.DelegatingConnection">
<div>
<span>
<a name="org.apache.commons.dbcp2.DelegatingConnection"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.DelegatingConnection
			</span>
<a href="#japicmp--toc">top</a>
</div>
<div>
<span>Generic Templates:</span>
<table>
<thead>
<tr>
<td>Change Status</td>
<td>Name</td>
<td>Old Type</td>
<td>New Type</td>
<td>Generics</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>UNCHANGED</span></td>
<td>C</td>
<td>java.sql.Connection</td>
<td>java.sql.Connection</td>
<td></td>
</tr>
</tbody>
</table>
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
<td>org.apache.commons.dbcp2.AbandonedTrace</td>
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
<div>
<div id="org.apache.commons.dbcp2.DelegatingStatement">
<div>
<span>
<a name="org.apache.commons.dbcp2.DelegatingStatement"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.DelegatingStatement
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
<td>org.apache.commons.dbcp2.AbandonedTrace</td>
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
<div>
<div id="org.apache.commons.dbcp2.Jdbc41Bridge">
<div>
<span>
<a name="org.apache.commons.dbcp2.Jdbc41Bridge"></a>
<span>UNCHANGED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.Jdbc41Bridge
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
<span>Constructors:</span>
<table>
<thead>
<tr>
<td>Status</td>
<td>Modifier</td>
<td>Generic Templates</td>
<td>Constructor</td>
<td>Exceptions</td>
<td>Compatibility Changes:</td>
<td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>UNCHANGED</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>Jdbc41Bridge()<div>
<span>Annotations:</span>
<table>
<thead>
<tr>
<td>Status:</td>
<td>Fully Qualified Name:</td>
<td>Elements:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td>
<td>java.lang.Deprecated</td>
<td>n.a.</td>
</tr>
</tbody>
</table>
</div>
</td>
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
<tr><td>ANNOTATION_DEPRECATED_ADDED</td></tr>
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
			55
		</td>
<td>
			494
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div>
<div>
</div>
</div>
</div>
<div>
<div id="org.apache.commons.dbcp2.managed.LocalXAConnectionFactory$LocalXAResource">
<div>
<span>
<a name="org.apache.commons.dbcp2.managed.LocalXAConnectionFactory$LocalXAResource"></a>
<span>MODIFIED</span>
<span>static</span>
<span>protected</span>
<span>class</span>
 org.apache.commons.dbcp2.managed.LocalXAConnectionFactory$LocalXAResource
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
</div>
</div>
</div>
<div>
<div id="org.apache.commons.dbcp2.managed.ManagedConnection$CompletionListener">
<div>
<span>
<a name="org.apache.commons.dbcp2.managed.ManagedConnection$CompletionListener"></a>
<span>MODIFIED</span>
<span>protected</span>
<span>class</span>
 org.apache.commons.dbcp2.managed.ManagedConnection$CompletionListener
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
<span>Constructors:</span>
<table>
<thead>
<tr>
<td>Status</td>
<td>Modifier</td>
<td>Generic Templates</td>
<td>Constructor</td>
<td>Exceptions</td>
<td>Compatibility Changes:</td>
<td>Line Number</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>MODIFIED</span></td>
<td><span>PUBLIC (&lt;- PROTECTED) </span>
</td>
<td>n.a.</td>
<td>ManagedConnection$CompletionListener(<span>org.apache.commons.dbcp2.managed.ManagedConnection</span>)</td>
<td></td>
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
			53
		</td>
<td>
			58
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div>
<div>
</div>
</div>
</div>
<div>
<div id="org.apache.commons.dbcp2.PoolableConnection">
<div>
<span>
<a name="org.apache.commons.dbcp2.PoolableConnection"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.PoolableConnection
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
<td>org.apache.commons.dbcp2.DelegatingConnection</td>
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
<div>
<div id="org.apache.commons.dbcp2.PoolableConnectionFactory">
<div>
<span>
<a name="org.apache.commons.dbcp2.PoolableConnectionFactory"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.PoolableConnectionFactory
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
</div>
</div>
</div>
<div>
<div id="org.apache.commons.dbcp2.PoolingConnection">
<div>
<span>
<a name="org.apache.commons.dbcp2.PoolingConnection"></a>
<span>MODIFIED</span>
<span>public</span>
<span>class</span>
 org.apache.commons.dbcp2.PoolingConnection
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
<td>org.apache.commons.dbcp2.DelegatingConnection</td>
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

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/spotbugs.html -->

<!-- page_index: 27 -->

# SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.9.8*

Threshold is *medium*

Effort is *default*

# Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 78 | 0 | 0 | 0 |

# Files

| Class | Bugs |
| --- | --- |

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/checkstyle.html -->

<!-- page_index: 28 -->

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 12.1.2 with /Users/garygregory/git/commons/commons-dbcp/src/conf/checkstyle.xml ruleset.

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 147 | 0 | 0 | 0 |

## Files

| File | I | W | E |
| --- | --- | --- | --- |

## Details

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/pmd.html -->

<!-- page_index: 29 -->

# PMD Results

The following document contains the results of [PMD](https://pmd.github.io) 7.18.0.

PMD found no problems in your source code.

## Suppressed Violations

| Filename | Rule message | Suppression type | Reason |
| --- | --- | --- | --- |
| org/apache/commons/dbcp2/BasicDataSource.java | Do not call pure method getDrivers if the result is not used. | //nopmd |  |
| org/apache/commons/dbcp2/DriverManagerConnectionFactory.java | Do not call pure method getDrivers if the result is not used. | //nopmd |  |
| org/apache/commons/dbcp2/cpdsadapter/DriverAdapterCPDS.java | Do not call pure method getDrivers if the result is not used. | //nopmd |  |

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbcp/cpd.html -->

<!-- page_index: 30 -->

# CPD Results

|  |  |
| --- | --- |
|  | CPD Results The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 7.18.0.  CPD found no problems in your source code. |

Copyright © 2001-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DBCP, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---
