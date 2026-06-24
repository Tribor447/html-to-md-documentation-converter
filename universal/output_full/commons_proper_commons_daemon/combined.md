# Project Information

## Navigation

- Commons Daemon
  - [About](#index)
  - [Asking Questions](https://commons.apache.org/proper/commons-daemon/mail-lists.html)
  - [Release History](#changes)
  - [Issue Tracking](#issue-management)
  - [Dependency Management](#dependency-info)
  - [Javadoc](https://commons.apache.org/proper/commons-daemon/apidocs/index.html)
  - [Javadoc Archive](https://javadoc.io/doc/commons-daemon/commons-daemon/)
  - [Sources](#scm)
  - [Security](#security)
  - [License](https://www.apache.org/licenses/LICENSE-2.0)
  - [Code of Conduct](https://www.apache.org/foundation/policies/conduct.html)
  - [Download](https://commons.apache.org/proper/commons-daemon/download_daemon.cgi)
  - [Procrun](#procrun)
  - [Jsvc](#jsvc)
  - [Native binaries](#binaries)
  - [FAQ](#faq)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [Issue Management](#issue-management)
    - [Mailing Lists](https://commons.apache.org/proper/commons-daemon/mailing-lists.html)
    - [Maven Coordinates](#dependency-info)
    - [Dependency Management](#dependency-management)
    - [Dependencies](#dependencies)
    - [Dependency Convergence](#dependency-convergence)
    - [CI Management](#ci-management)
    - [Distribution Management](#distribution-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes)
    - [JIRA Report](#jira-changes)
    - [Javadoc](https://commons.apache.org/proper/commons-daemon/apidocs/index.html)
    - [Source Xref](https://commons.apache.org/proper/commons-daemon/xref/index.html)
    - [Test Source Xref](https://commons.apache.org/proper/commons-daemon/xref-test/index.html)
    - [Surefire](#surefire)
    - [RAT Report](#rat-report)
    - [JaCoCo](https://commons.apache.org/proper/commons-daemon/jacoco/index.html)
    - [japicmp](https://commons.apache.org/proper/commons-daemon/japicmp.html)
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

<!-- source_url: https://commons.apache.org/proper/commons-daemon/index.html -->

<!-- page_index: 1 -->

# Introduction

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Introduction"></a>
<h1>Introduction</h1>
<p>
      Since 1994, the Java programming language evolved and became a
      valid tool to develop reliable and performant server applications as
      opposed to just applets and client applications. The major disadvantage of
      the Java platform is that still today the only portable way to
      start a Java application relies on a single point of entry: the
      <code><em>public static void</em>
      main(<em>String</em>[])</code> method.
</p>
<p>
      Having a single-point of entry is a valid solution for client
      applications, where interactively a user can command to the application
      to quit (which can terminate the Virtual Machine process at calling the
      <code><em>System</em>.exit(<em>int</em>)</code>
      method), but in those cases where the application is not interactive
      (server applications) there is currently no portable way to notify
      the Virtual Machine of its imminent shutdown.
</p>
<p>
      A server application written in Java might have to perform several tasks
      before being able to shut down the Virtual Machine process. For example
      in the case of a Servlet container, before the VM process is shut down,
      sessions might need to be serialized to disk, and web applications need
      to be destroyed.
</p>
<p>
      One common solution to this problem is to create (for example) a
      <code><em>ServerSocket</em></code> and wait for a particular
      message to be issued. When the message is received, all operations
      required to shut down the server applications are performed and at the
      end the <code><em>System</em>.exit</code> method is called
      to terminate the Virtual Machine process. This method however, has
      several disadvantages and risks:
</p>
<ul>
<li>
      In case of a system-wide shutdown, the Virtual Machine process may be
      shut down directly by the operating system without notifying the running
      server application.
      </li>
<li>
      If an attacker finds out the shutdown message to send to the server
      and discovers a way to send this message, he can easily interrupt
      the server's operation, bypassing all the security restrictions
      implemented in the operating system.
      </li>
</ul>
<p>
      Most multi-user operating systems already have a way in which server
      applications are started and stopped. Under Unix based operating systems
      non-interactive server applications are called <em>daemons</em> and are
      controlled by the operating system with a set of specified
      <em>signals</em>. Under Windows such programs are called <em>services</em>
      and are controlled by appropriate calls to specific functions defined in
      the application binary, but although the ways of dealing with the problem
      are different, in both cases the operating system can notify a server
      application of its imminent shutdown, and the application has the
      ability to perform certain tasks before its process of execution is
      destroyed.
</p>
</section>
<section><a id="Structure"></a>
<h1>Structure</h1>
<p>
      Daemon is made of 2 parts. One written in C that makes the interface to
      the operating system and the other in Java that provides the
      Daemon API.
</p>
</section>
<section><a id="Platforms"></a>
<h1>Platforms</h1>
<p>
      Both Win32 and UNIX like platforms are supported.
      For Win32 platforms use <a href="#procrun">procrun</a>.
      For UNIX like platforms use <a href="#jsvc">jsvc</a>.
</p>
</section>
<section><a id="Initial_Source_of_the_Package"></a>
<h1>Initial Source of the Package</h1>
<p>The original Java classes came from the Jakarta Tomcat 4.0 project.</p>
<p>The package name for the Daemon component is
<code>org.apache.commons.daemon</code>.
</p>
</section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/changes.html -->

<!-- page_index: 2 -->

# Apache Commons Daemon Release Notes

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Apache_Commons_Daemon_Release_Notes"></a>
<h1>Apache Commons Daemon Release Notes</h1><section><a id="Release_History"></a>
<h2>Release History</h2>
<table>
<tr>
<th>Version</th>
<th>Date</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes--a1.5.1">1.5.1</a></td>
<td>2025-12-16</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.5.0">1.5.0</a></td>
<td>2025-11-26</td>
<td>This is a maintenance release. Java 8 or later is required.</td></tr>
<tr>
<td><a href="#changes--a1.4.1">1.4.1</a></td>
<td>2025-01-13</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.4.0">1.4.0</a></td>
<td>2024-05-24</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.3.4">1.3.4</a></td>
<td>2023-05-12</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.3.3">1.3.3</a></td>
<td>2022-11-29</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.3.2">1.3.2</a></td>
<td>2022-10-10</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.3.1">1.3.1</a></td>
<td>2022-05-09</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.3.0">1.3.0</a></td>
<td>2022-03-18</td>
<td>Feature and bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.2.4">1.2.4</a></td>
<td>2021-01-21</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.2.3">1.2.3</a></td>
<td>2020-09-01</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.2.2">1.2.2</a></td>
<td>2019-10-04</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.2.1">1.2.1</a></td>
<td>2019-09-09</td>
<td>Bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.2.0">1.2.0</a></td>
<td>2019-07-02</td>
<td>Feature and bug fix release</td></tr>
<tr>
<td><a href="#changes--a1.1.0">1.1.0</a></td>
<td>2017-11-15</td>
<td>Feature and bug fix release</td></tr></table></section><section><a id="a1.5.1"></a>
<h2>Release 1.5.1 – 2025-12-16</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Fix compilation warnings.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procun. Build binaries for Windows using the static hybrid CRT strategy by default.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.5.0"></a>
<h2>Release 1.5.0 – 2025-11-26</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Document --enable-preview</td>
<td><a href="#team--michaelo">michaelo</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Fix first appearance of --enable-native-access</td>
<td><a href="#team--michaelo">michaelo</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix redirection issues on some OS versions by using recommended method to redirect stdout and stderr. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-398">DAEMON-398</a>.</td>
<td><a href="#team--jfclere">jfclere</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix updating of startup mode to 'Automatic (delayed)' being incorrectly processed as an update to 'Manual'. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-439">DAEMON-439</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix timeout handling #238. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-468">DAEMON-468</a>. Thanks to Jean-Frederic Clere, Mark Thomas, Sebb, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Replace RTF version of license header with plain text version of full license in about box for monitor application. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-472">DAEMON-472</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Service should be marked as stopped if the service worker crashes. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-475">DAEMON-475</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add support for --enable-native-access Java startup option in jsvc. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-471">DAEMON-471</a>.</td>
<td><a href="#team--michaelo">michaelo</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add tests for prunsrv on Windows #260. Thanks to Jean-Frederic Clere, Gary Gregory, Mark Thomas.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add Java API compatibility report to the site (JApiCmp). Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 78 to 91 #253, #255, #287. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Update to use new ASF logo</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.4.1"></a>
<h2>Release 1.4.1 – 2025-01-13</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Fix several issues around Java OS and header files location detection.</td>
<td><a href="#team--michaelo">michaelo</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Correct several log messages where an incorrect placeholder led to
        truncation of the inserted values.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add protection to avoid high CPU usage for applications running in JVM
        mode that do not wait for the stop method to be called before the start
        method returns. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-460">DAEMON-460</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump org.apache.commons:commons-parent from 71 to 78 #189, #196, #198, #204, #207, #210, #216. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Remove autogenerated files and rely on autoreconf only.</td>
<td><a href="#team--michaelo">michaelo</a></td></tr></table></section><section><a id="a1.4.0"></a>
<h2>Release 1.4.0 – 2024-05-24</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>[StepSecurity] ci: Harden GitHub Actions #95. Thanks to step-security-bot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Enable Control Flow Guard for Windows binaries. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-429">DAEMON-429</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Better label for command used to start service shown in
        Prunmgr.exe. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-461">DAEMON-461</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Fix warnings when running support/buildconf.sh</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Fix compilation issue with newer compilers. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-463">DAEMON-463</a>. Thanks to michaelo.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Refactor UAC support so that elevation is only requested for
        actions that require administrator privileges.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add support for hybrid CRT builds.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>jsvc. Add support for LoongArch64 support #92. Thanks to huajingyun.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons-parent from 57 to 69 #155. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>The minimum support Java version has been upgraded from Java 7 to Java
        8.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Procrun. The minimum Windows versions supported are now Windows 10 and
        Windows Server 2016.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons-parent from 69 to 70.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.3.4"></a>
<h2>Release 1.3.4 – 2023-05-12</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Configured stack size now applies to the main thread when
        running in JVM mode. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-451">DAEMON-451</a>. Thanks to kkolinko.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. If the specified log directory does not exist, attempt to
        create any missing parent directories, as well as the specified
        directory, when the service starts. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-452">DAEMON-452</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Allow Windows service dependencies to be managed by Procrun or
        by 'sc config ...'. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-458">DAEMON-458</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Fix DaemonController.reload() only working the first time it is
        called. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-459">DAEMON-459</a>. Thanks to Klaus Malorny.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Remove incorrent definition 'supported_os' which defined in
        psupport.m4 file to fix jsvc build error on riscv64. Thanks to Eastdong.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons-parent from 54 to 57 #71, #91. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.3.3"></a>
<h2>Release 1.3.3 – 2022-11-29</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix creation of duplicate ACL entries on some Windows platforms. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-450">DAEMON-450</a>. Thanks to Norimasa Yamamoto.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Follow-up to ensure all child processes are cleaned up if the
        service does not stop cleanly. #64 Thanks to jfclere.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/cache from 3.0.8 to 3.0.11 #60. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/checkout from 3.0.2 to 3.1.0 #59. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/setup-java from 3.5.1 to 3.6.0 #63. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.7.2.0 to 4.7.3.0 #61, #66. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons-parent from 55 to 56 #76 Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.3.2"></a>
<h2>Release 1.3.2 – 2022-10-10</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Remove noisy INFO log message that triggered logging once per
        minute while the service was running.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Fix typos in Javadoc and comments #50, #51. Thanks to Marc Wrobel.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. The DependsOn parameter is no longer ignored when updating the
        service configuration. Fixes <a href="https://issues.apache.org/jira/browse/DAEMOM-446">DAEMOM-446</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix crash and provide an error level log message when the user
        attempts to start the service without configuring a JVM and none is
        available via the registry. Fixes <a href="https://issues.apache.org/jira/browse/DAEMOM-448">DAEMOM-448</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/cache from 3.0.3 to 3.0.8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/checkout from 3 to 3.0.2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons-parent from 53 to 54 #55. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.6.0.0 to 4.7.2.0 #48, #52, #53. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump jacoco-maven-plugin from 0.8.7 to 0.8.8. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump japicmp-maven-plugin from 0.15.4 to 0.16.0. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump JUnit 4 to 5 vintage. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.3.1"></a>
<h2>Release 1.3.1 – 2022-05-09</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Take account of LogLevel setting when logging to standard error
        so the user can opt to see messages at Info level and below. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Clear expected errors when checking for environment variables
        to prevent the expected errors from polluting subsequent log messages. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Only configure the logging to be written to a file when
        running as a service. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Clear logged error on service installation failure to prevent
        the error polluting subsequent log messages. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. When configuring permissions for the logging path, use the
        default path if no explicit logging path is specified. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. When logging issues configuring permissions for the logging
        path, explicitly state when default values are being used rather than
        logging blank values. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Increase the size limit on the message component of log entries
        to 4096 characters. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-442">DAEMON-442</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure child processes are cleaned up if the service does not
        stop cleanly. #39 Thanks to jfclere.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Refactor multiple if statements to use switch. #45 Thanks to Arturo Bernal.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/cache from 2.1.7 to 3.0.3 #41. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/setup-java from 2 to 3.5.1 #43. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.5.3.0 to 4.6.0.0 #42. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons-parent from 52 to 53 #44. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.3.0"></a>
<h2>Release 1.3.0 – 2022-03-18</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. --StopTimeout can be used to define the time that procrun waits for service to exit,
        but INFINITE timeout was using instead. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-430">DAEMON-430</a>.</td>
<td><a href="#team--jfclere">jfclere</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Minor improvements to Java code #22, #31. Thanks to Arturo Bernal.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Minor improvement that allows to have WINVER nmake variable
        directly defined at compile time as ABI version in hexadecimal format.</td>
<td><a href="#team--mturk">mturk</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Log at Trace instead of Debug when a service reports its state from the prunsrv app.
        This avoids the Debug log filling up as it adds two events per minute.
        You can then stay in Debug logging to capture register, start, stop, and unregister Debug events. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Miscellaneous logging improvements. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Log the prunsrv function names at the Trace level. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Only redirect stderr and stdout to files for the running
        service. Output from commands executed on the command line will not be
        redirected. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-437">DAEMON-437</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure that the user configured to run the service is also
        granted access to the log file directory. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-437">DAEMON-437</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure Trace is included in the logging levels exposed in the
        GUI.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Support --Startup=delayed for service installation as well as
        service update. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-439">DAEMON-439</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Enable Dependabot #20. Thanks to John Patrick.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. reportServiceStatusE() shows scale of dwWaitHint as millisecond in logging. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. reportServiceStatusE() shows a short description for dwCurrentState in logging. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add support for a new log level called Trace, lower-level than Debug. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add logging when failing to obtain a service's description from the registry. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add logging when failing to set the options of a service. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/cache from v2 to v2.1.7 #24, #30, #36. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump build actions/setup-java from v1.4.3 to v2. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons.jacoco.version from 0.8.5 to 0.8.7. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons.japicmp.version from 0.14.3 to 0.15.4. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump junit from 4.13.1 to 4.13.2 #25. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump commons.daemon.javaversion 1.6 -&gt; 1.7. Thanks to Gary Gregory.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 4.4.2.2 to 4.5.2.0 #37. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Update the release build instructions to use CMSC 15.0.44.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Bump actions/checkout from 2 to 3 #40. Thanks to Dependabot.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.2.4"></a>
<h2>Release 1.2.4 – 2021-01-21</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure that log messages written to stdout and stderr are not
        lost during start-up. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-424">DAEMON-424</a>. Thanks to Bernhard Scholz.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct a regression introduced in 1.2.3. Enable the service to
        start if the Options value is not present in the registry. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-425">DAEMON-425</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Don't fail if the CAP_DAC_READ_SEARCH capability is not available.
        Fall back to using argv[0] rather than /proc/self/exe to determine the
        path for the current binary. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-426">DAEMON-426</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Remove some unnecessary code. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-428">DAEMON-428</a>.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.2.3"></a>
<h2>Release 1.2.3 – 2020-09-01</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct multiple issues related to enabling a service to
        interact with the desktop. Provide a better error message if this option
        is used with an invalid user, install the service with the option
        enabled if requested and correctly save the setting if it is enabled in
        the GUI. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-411">DAEMON-411</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Update the list of paths searched for libjvm.so to include the
        path used by OpenJDK 11. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-410">DAEMON-410</a>. Thanks to Richard Morrell.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add additional debug logging for Java start mode.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Remove incorrect definition 'supported_os' which defined in
        psupport.m4 file to fix jsvc build error on s390, arm, aarch64,
        mipsel and mips. Thanks to Ray Wang.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. More debug logging in prunsrv.c and javajni.c.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>jsvc. Update arguments.c to support Java 11 --enable-preview #18. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-419">DAEMON-419</a>. Thanks to mads1980.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>jsvc and Procrun. Add support for Java native memory tracking. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-412">DAEMON-412</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add a new command, print, that outputs the command to
        (re-)configure the service with the current settings. This is intended
        to be used to save settings such as before an upgrade. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-422">DAEMON-422</a>.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.2.2"></a>
<h2>Release 1.2.2 – 2019-10-04</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct a regression in the fix for DAEMON-401 that prevented
        the service from starting unless support for the universal C runtime had
        been installed. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-408">DAEMON-408</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Update Commons-Parent to version 49.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix compiler warnings for unreferenced formal parameters.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Switch code to use more secure versions of Windows API calls to
        resolve warnings reported by newer versions of Visual Studio.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Correct the source assembly definitions to add README.md,
        CONTRIBUTING.md and HOWTO-RELEASE.txt, remove references to the deleted
        Ant build files and exclude the working directories of Windows binary
        builds.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>More startup on Windows logging in javajni.c. #14.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr></table></section><section><a id="a1.2.1"></a>
<h2>Release 1.2.1 – 2019-09-09</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Correct debug log message that reports change in umask. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-403">DAEMON-403</a>. Thanks to Charles.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct a regression in the previous fix for this issue that
        caused 32-bit services to crash on start-up. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-401">DAEMON-401</a>. Thanks to Norimasa Yamamoto.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct a regression in the fix for DAEMON-391 that caused the
        GUI to mix up the WARN and INFO logging levels. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-407">DAEMON-407</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Expand the search for a valid Java runtime library to include
        the current JDK home defined in the Windows registry. Fully document the
        search algorithm used to find the Java runtime library. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-404">DAEMON-404</a>.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.2.0"></a>
<h2>Release 1.2.0 – 2019-07-02</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Add to OPT_LFLAGS rather than overwrite OPT_LFLAGS when setting
        /OPT:REF in the make file for Windows. Thanks to mturk.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Only set the global shutdown event if the event is created. Thanks to mturk.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Unable to build with Java 9 using ant; dropped Ant build files. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-379">DAEMON-379</a>.</td>
<td><a href="#team--sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. prunsrv stopping with error due to hard-coded timeout. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-384">DAEMON-384</a>. Thanks to blassmegod.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Update config.guess and config.sub. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-385">DAEMON-385</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Jsvc. Set the sun.java.command system property when starting via jsvc so
        that tools like jconsole show something meaningful for the process name. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-388">DAEMON-388</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct the level name used in the GUI for WARN so that changes
        made via the GUI are recognised. Order the log levels in the drop-down
        from ERROR to DEBUG. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-391">DAEMON-391</a>. Thanks to Thorsten Schöning.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Correct reversed code comments for JRE and JDK locations in the
        registry. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-393">DAEMON-393</a>. Thanks to Daniel Hofmann.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Undefined behavior in registry.c dwRegKey = dwRegKey++. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-392">DAEMON-392</a>. Thanks to Daniel Hofmann.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Fix a bug that meant a value provided for LibraryPath replaced
        the value of the PATH environment variable rather than prepended to it. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-396">DAEMON-396</a>. Thanks to Gerwin.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure that JAVA_HOME/bin is on the path when running in jvm
        mode so that additional DLLs, such as awt.dll, can be found if required. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-396">DAEMON-396</a>. Thanks to Gerwin.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure that the java.library.path environment variable is
        correctly configured when running on a JRE that depends on the Universal
        CRT. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-396">DAEMON-396</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Log the error code returned if JVM creation fails to aid
        debugging.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Harden the Windows binaries against DLL hijacking in the directory where
        the binaries are located.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure that environment variables set via prunsrv are visible
        to native libraries that depend on the Universal CRT. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-401">DAEMON-401</a>. Thanks to Jonathan Gallimore.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add 'NT Authority\LocalService' and
        'NT Authority\NetworkService' as options to the Log On user interface.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Procrun. Change the default service user from LocalSystem to
        'NT Authority\LocalService'.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Avoid a crash on shutdown if multiple WM_CLOSE messages are
        received. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-402">DAEMON-402</a>. Thanks to Iode Leroy.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ignore blank lines inserted into the Java Options and/or Java 9
        Options text areas. This prevents settings after the first blank line
        from being lost when saved to the registry. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-394">DAEMON-394</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Remove the code that removed quotes from configured Java and
        Java 9 Options. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-399">DAEMON-399</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Ensure that vfprintf is the first parameter passed when using
        JNI to create the JVM as a workaround for startup error messages not
        being visible on stdout or stderr. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-398">DAEMON-398</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. Add an option to configure the service to use the 'Automatic
        (Delayed Start)' startup mode. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-303">DAEMON-303</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Procrun. When running in jre mode, if the standard Java registry entries
        for JavaHome and RuntimeLib are not present, attempt to use the Procrun
        JavaHome key to find the runtime library. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-329">DAEMON-329</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>jsvc. Include the full path to the jsvc executable in the debug log. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-297">DAEMON-297</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>jsvc. Improve search for libjli.dylib on macOS when using custom-built
        OpenJDK binaries. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-397">DAEMON-397</a>. Thanks to Petr Hadraba.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Procrun. Improve log messages for interactions with the Windows service. Thanks to ggregory.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>jsvc. Improve mips detection. Thanks to YunQiang Su.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section><section><a id="a1.1.0"></a>
<h2>Release 1.1.0 – 2017-11-15</h2>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add DEBUG and ERROR logging to help diagnose problems when starting a Windows Service. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-368">DAEMON-368</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Update the minimum Java requirement from version 5 to 6. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-371">DAEMON-371</a>.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Increase minimum Java version to Java 5.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Add AArch64 support to src/native/unix/support/apsupport.m4. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-347">DAEMON-347</a>. Thanks to Ganesh Raju.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Compile the Windows binaries with the /DYNAMICBASE and /NXCOMPAT
        switches. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-346">DAEMON-346</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Remove calls to explicit garbage collection during daemon start and
        stop. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-333">DAEMON-333</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Update config.guess and config.sub to add support, amongst others, for
        the 64-bit PowerPC Little-Endian architecture. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-343">DAEMON-343</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Ensure that the PID file on Windows, if used, is readable by other
        processes. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-332">DAEMON-332</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Update Commons-Parent to version 41.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Update apsupport.m4 add support for 64-bit PowerPC architectures. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-358">DAEMON-358</a>. Thanks to Gustavo Romero.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Suppress spurious "The data area passed to a system call is too
        small" error message in the log when Procrun fails to stop the
        service. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-282">DAEMON-282</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Move attributions from @author in Javadocs to POM. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-370">DAEMON-370</a>. Thanks to Amey Jadiye.</td>
<td><a href="#team--ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Enable jsvc to start when running on Java 9. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-373">DAEMON-373</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Fix a resource leak opening the JVM configuration file. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-324">DAEMON-324</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Improve the jsvc code that restarts the process if the JVM crashes so
        that if the JVM crashes after a signal has been received to shut down
        jsvc does not attempt to restart the JVM. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-339">DAEMON-339</a>. Thanks to John Wehle.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Ensure that the child process is started with the correct umask. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-318">DAEMON-318</a>. Thanks to Markus Schneider.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Correct conflicting information for the behavior of Procrun when using
        jvm mode. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-309">DAEMON-309</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Ensure that, when using Procrun in java or exe mode, the service process
        waits for the stop process to complete before starting clean-up to avoid
        a crash in the stop process. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-372">DAEMON-372</a>. Thanks to Sérgio Ozaki.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Enable jsvc to find the jvm when running on AIX. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-310">DAEMON-310</a>. Thanks to John Wehle.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Ensure that Procrun treats JVM crashes as service failures so the
        recovery options will apply. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-302">DAEMON-302</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Ensure that the //MQ command closes the prunmgr process even if the
        configuration dialog is open when the //MQ command is used. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-312">DAEMON-312</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>When looking in the Windows registry for JRE and JDK installation
        locations, additionally check the registry keys used by IBM provided
        JREs and JDKs. Do this after checking the keys used by Oracle provided
        JREs and JDKs. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-311">DAEMON-311</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>When looking in the Windows registry for JRE and JDK installation
        locations, additionally check the registry keys used by Oracle provided
        Java 9 and later JREs and JDKs. Do this after checking the keys used by
        Oracle provided Java 8 and earlier JREs and JDKs. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-376">DAEMON-376</a>.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Add support for Java 9 command line arguments to jsvc. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-374">DAEMON-374</a>. Thanks to Rashmi Ranjan Mohanty.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add a restarts options to jsvc to control the number of permitted
        restarts after a system crash. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-334">DAEMON-334</a>. Thanks to Brett Delle Grazie.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_0709549ef19b3cfd.gif" title="Remove"/></td>
<td>Remove support for building Procrun for the Itanium platform.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_c74c1340248cb28d.gif" title="Update"/></td>
<td>Make Windows XP the minimum support target platform.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_3a944079c48e53e0.gif" title="Add"/></td>
<td>Add support to Procrun for separate JVM options for use when running on
        Java 9 and above.</td>
<td><a href="#team--markt">markt</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ea60102868380a49.gif" title="Fix"/></td>
<td>Fix race conditions in PID file handling in jsvc. Fixes <a href="https://issues.apache.org/jira/browse/DAEMON-377">DAEMON-377</a>. Thanks to Rustam Abdullaev.</td>
<td><a href="#team--markt">markt</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="issue-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/issue-management.html -->

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
<pre><a href="https://issues.apache.org/jira/browse/DAEMON">https://issues.apache.org/jira/browse/DAEMON</a></pre></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/dependency-info.html -->

<!-- page_index: 4 -->

# Maven Coordinates

## Apache Maven

```
<dependency>
  <groupId>commons-daemon</groupId>
  <artifactId>commons-daemon</artifactId>
  <version>1.5.1</version>
</dependency>
```

## Apache Ivy

```
<dependency org="commons-daemon" name="commons-daemon" rev="1.5.1">
  <artifact name="commons-daemon" type="jar" />
</dependency>
```

## Groovy Grape

```
@Grapes(
@Grab(group='commons-daemon', module='commons-daemon', version='1.5.1')
)
```

## Gradle/Grails

```
implementation 'commons-daemon:commons-daemon:1.5.1'
```

## Scala SBT

```
libraryDependencies += "commons-daemon" % "commons-daemon" % "1.5.1"
```

## Leiningen

```
[commons-daemon "1.5.1"]
```

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/scm.html -->

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
<pre><a href="https://gitbox.apache.org/repos/asf?p=commons-daemon.git">https://gitbox.apache.org/repos/asf?p=commons-daemon.git</a></pre></section><section><a id="Anonymous_Access"></a>
<h1>Anonymous Access</h1>
<p>The source can be checked out anonymously from Git with this command (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>):</p>
<pre>$ git clone https://gitbox.apache.org/repos/asf/commons-daemon.git</pre></section><section><a id="Developer_Access"></a>
<h1>Developer Access</h1>
<p>Only project developers can access the Git tree via this method (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>).</p>
<pre>$ git clone https://gitbox.apache.org/repos/asf/commons-daemon.git</pre></section><section><a id="Access_from_Behind_a_Firewall"></a>
<h1>Access from Behind a Firewall</h1>
<p>Refer to the documentation of the SCM used for more information about access behind a firewall.</p></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/security.html -->

<!-- page_index: 6 -->

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-daemon/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

# Security Vulnerabilities

None.

---

<a id="procrun"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/procrun.html -->

<!-- page_index: 7 -->

# Introduction

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Introduction"></a>
<h1>Introduction</h1>
<p>
    Procrun is a set of applications that allow Windows users to wrap
    (mostly) Java applications (e.g. Tomcat) as a Windows service.

    The service can be set to automatically start when the machine boots
    and will continue to run with no user logged onto the machine.
</p>
</section>
<section><a id="Procrun_monitor_application"></a>
<h1>Procrun monitor application</h1>
<p>
<b>Prunmgr</b> is a GUI application for monitoring and configuring procrun
    services.
</p>
<p>
    Each command line directive is in the form of <b>//XX[//ServiceName]</b>
</p>
<p>
    If the <code>//ServiceName</code> parameter is omitted, then the service name is
    assumed to be the name of the file.


    The Prunsrv application behaves in the same way,
    so to allow both applications to reside in the same directory, the Prunmgr application
    will remove a trailing <b>w</b> (lower-case w) from the name.


    For example if the Prunmgr application is renamed as <code>TestService.exe</code>
    - or as <code>TestServicew.exe</code> -
    then the default service name is <code>TestService</code>.
</p>
<p>The available command line options are:</p>
<table>
<tr>
<th>//ES</th>
<td>Edit service configuration</td>
<td>This is the default operation. It is called if the no option is
            provided.
            Starts the GUI application which allows the service configuration
            to be modified, started and stopped.
        </td>
</tr>
<tr>
<th>//MS</th>
<td>Monitor service</td>
<td>Starts the GUI application and minimizes it to the system tray.
        </td>
</tr>
<tr>
<th>//MR</th>
<td>Monitor &amp; run service</td>
<td>Starts the GUI application and minimizes it to the system tray.
            Start the service if it is not currently running.
        </td>
</tr>
<tr>
<th>//MQ</th>
<td>Monitor Quit</td>
<td>Stop any running monitor for the service.
        </td>
</tr>
</table>
</section>
<section><a id="Procrun_service_application"></a>
<h1>Procrun service application</h1>
<p>
<b>Prunsrv</b> is a service application for running applications as services.
    It can convert any application (not just Java applications) to run as a service.
</p>
<section><a id="Command_line_arguments"></a>
<h2>Command line arguments</h2>
<p>
    Each command line directive is in the form of <b>//XX[//ServiceName]</b>.
</p>
<p>
    If the <code>//ServiceName</code> parameter is omitted, then the service name is
    assumed to be the name of the file.


    For example if the application is renamed as <code>TestService.exe</code>,
    then the default service name is <code>TestService</code>.
</p>
<p>The available command line options are:</p>
<table>
<tr>
<th>//TS</th>
<td>Run the service as a console application</td>
<td>This is the default operation. It is called if the no option is provided.
        </td>
</tr>
<tr>
<th>//RS</th>
<td>Run the service</td>
<td>Called only from ServiceManager</td>
</tr>
<tr>
<th>//ES</th>
<td>Start (execute) the service</td>
<td></td>
</tr>
<tr>
<th>//SS</th>
<td>Stop the service</td>
<td></td>
</tr>
<tr>
<th>//US</th>
<td>Update service parameters</td>
<td></td>
</tr>
<tr>
<th>//IS</th>
<td>Install service</td>
<td></td>
</tr>
<tr>
<th>//DS</th>
<td>Delete service</td>
<td>Stops the service first if it is currently running</td>
</tr>
<tr>
<th>//PS</th>
<td>Print service</td>
<td>Prints the command to (re-)create the current configuration</td>
</tr>
<tr>
<th>//PP[//seconds]</th>
<td>Pause</td>
<td>Default is 60 seconds</td>
</tr>
<tr>
<th>//VS</th>
<td>Version</td>
<td>Print version and exit (since version 1.0.3)</td>
</tr>
<tr>
<th>//?</th>
<td>Help</td>
<td>Print usage and exit (since version 1.0.3)</td>
</tr>
</table>
<p>Starting with version <b>1.0.8</b> a more traditional command line can
    be used in the form: <b>command [ServiceName]</b>.
</p>
<table>
<tr>
<th>run</th>
<td>Run the service as a console application</td>
<td>This is the default operation. It is called if the no option is provided
        and has the same effect as calling <b>//TS</b>.
        </td>
</tr>
<tr>
<th>service</th>
<td>Run the service</td>
<td>Called only from ServiceManager</td>
</tr>
<tr>
<th>start</th>
<td>Start the service</td>
<td>Synonym for <b>//ES</b></td>
</tr>
<tr>
<th>stop</th>
<td>Stop the service</td>
<td>Synonym for <b>//SS</b></td>
</tr>
<tr>
<th>update</th>
<td>Update service parameters</td>
<td>Synonym for <b>//US</b></td>
</tr>
<tr>
<th>install</th>
<td>Install service</td>
<td>Synonym for <b>//IS</b></td>
</tr>
<tr>
<th>delete</th>
<td>Delete service</td>
<td>Stops the service first if it is currently running</td>
</tr>
<tr>
<th>print</th>
<td>Print service</td>
<td>Prints the command to (re-)create the current configuration</td>
</tr>
<tr>
<th>pause [seconds]</th>
<td>Pause</td>
<td>Default is 60 seconds</td>
</tr>
<tr>
<th>version</th>
<td>Version</td>
<td>Print version and exit</td>
</tr>
<tr>
<th>help</th>
<td>Help</td>
<td>Print usage and exit</td>
</tr>
</table>
</section>
<section><a id="Command_line_parameters"></a>
<h2>Command line parameters</h2>
<p>
    Each command parameter is prefixed with <b>--</b> (or <b>++</b>, see below).


    If an environment variable exists with the same name as a command line parameter but
    prefixed with <code>PR_</code> it will <b>override</b> the equivalent command line parameter.


    For example:
</p>
<pre><code>set PR_CLASSPATH=xx.jar</code></pre>
<p>is equivalent to providing
</p>
<pre><code>--Classpath=xx.jar</code></pre>
<p> as a command line parameter.</p>
<p>
If a parameter is repeated, then normally the last value takes precedence.
However some parameters can take multiple values - for example StartParams and JvmOptions.
If these parameters are prefixed with <b>++</b>, then the value will be appended to the existing value.
For example:
</p>
<pre><code>
--Startup=manual --Startup=auto --JvmOptions=-Done=1 ++JvmOptions=-Dtwo=2
</code></pre>
will result in the following values being used:

<pre><code>
Startup:
auto

JvmOptions:
-Done=1
-Dtwo=2
</code></pre>

Only multivalued parameters support this; they are indicated in the table below by <b><code>++</code></b>.

If <b><code>++</code></b> is used for a parameter that does not support multiple values, then it is treated the same as <b><code>--</code></b>. No error is reported.

Configuration is overwritten in case <b><code>--</code></b> is used.
For example:

<pre><code>
--JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=4
</code></pre>
will always overwrite the JvmOptions. The resulting configuration will be:

<pre><code>
Startup:
auto

JvmOptions:
-Dthree=3
-Dfour=4
</code></pre>
However if on  <b><code>++</code></b> is used the values will be appended. For example calling the
following after the first example

<pre><code>
++JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=2
</code></pre>
will result in the following values being used:

<pre><code>
Startup:
auto

JvmOptions:
-Done=1
-Dtwo=2
-Dthree=3
-Dfour=4
</code></pre>

In case you intermix the <b><code>++</code></b> and <b><code>--</code></b> options, the
last <b><code>--</code></b> parameter will cause option reset. For example:

<pre><code>
--Startup=manual --Startup=auto --JvmOptions=-Done=1 ++JvmOptions=-Dtwo=2 --JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=2
</code></pre>
will result in the following values being used:

<pre><code>
Startup:
auto

JvmOptions:
-Dthree=3
-Dfour=4
</code></pre>
<p>
When updating a service (//US or update command), using <b><code>--</code></b>
will replace any existing parameter with the new setting.

For multivalued parameters, using the <b><code>++</code></b> option qualifier
will add the new value(s) to any existing value(s).
</p>
<table>
<tr>
<th>Parameter Name  </th>
<th>Default</th>
<th>Description</th>
</tr>
<tr>
<td>--Description</td>
<td></td>
<td>Service name description (maximum 1024 characters)</td>
</tr>
<tr>
<td>--DisplayName</td>
<td>ServiceName</td>
<td>Service display name</td>
</tr>
<tr>
<td>--Install</td>
<td>procrun.exe //RS//ServiceName</td>
<td>Install image</td>
</tr>
<tr>
<td>--Startup</td>
<td>manual</td>
<td>Service startup mode can be either <b>delayed</b>, <b>auto</b> or <b>manual</b></td>
</tr>
<tr>
<td>--Type</td>
<td></td>
<td>Service type can be <b>interactive</b> to allow the service to interact with the desktop.
    This option can only be used with the <i>LocalSystem</i> account.</td>
</tr>
<tr>
<td>++DependsOn</td>
<td></td>
<td>List of services that this service depends on. Services are separated
        using either <b>#</b> or <b>;</b> characters.

<p>
<b>Note:</b> At installation, additional dependencies will be created
        on the services <i>Tcpip</i> and <i>Afd</i> if not explicitly
        specified. These additional dependencies will not be created
        automatically when updating the service configuration with
        <i>--DependsOn</i> and must be explicitly defined if required in that
        case.
        </p>
</td>
</tr>
<tr>
<td>++Environment</td>
<td></td>
<td>List of environment variables that will be provided to the service
        in the form <b>key=value</b>. They are separated using either
        <b>#</b> or <b>;</b> characters.
        If you need to embed either # or ; character within a value put them inside single quotes.
    </td>
</tr>
<tr>
<td>--User</td>
<td></td>
<td>User account used for running executable. It is used only for
        StartMode <b>Java</b> or <b>exe</b> and enables running applications
        as a service under an account without the LogonAsService privilege.</td>
</tr>
<tr>
<td>--Password</td>
<td></td>
<td>Password for user account set by --User parameter</td>
</tr>
<tr>
<td>--ServiceUser</td>
<td></td>
<td>Specifies the name of the account under which the service should run.
        Use an account name in the form <i>DomainName\UserName</i>.
        The service process will be logged on as this user.
        if the account belongs to the built-in domain, you can specify <i>.\UserName</i>
        Note that the Service Control Manager does not accept localised forms of
        the standard names so to use them you need to specify
        <i>NT Authority\LocalService</i>, <i>NT Authority\NetworkService</i> or
        <i>LocalSystem</i> as appropriate.
    </td>
</tr>
<tr>
<td>--ServicePassword</td>
<td></td>
<td>Password for user account set by --ServiceUser parameter</td>
</tr>
<tr>
<td>--LibraryPath</td>
<td></td>
<td>Directory added to the search path used to locate the DLLs for the JVM.
        This directory is added both in front of the <b>PATH</b> environment variable
        and as a parameter to the <b>SetDLLDirectory</b> function.
    </td>
</tr>
<tr>
<td>--JavaHome</td>
<td>JAVA_HOME</td>
<td>Set a different <strong>JAVA_HOME</strong> than defined by the <strong>JAVA_HOME</strong> environment
        variable.</td>
</tr>
<tr>
<td>--Jvm</td>
<td>auto</td>
<td>Use either <b>auto</b> (i.e. find the JVM from the Windows registry) or specify the full path to the <b>jvm.dll</b>.
        You can use environment variable expansion here. When auto is specified the following search order is used:

<ol>
<li>The current Java runtime library as defined in the registry</li>
<li>The current JRE as defined in the registry</li>
<li>The explicitly configured JavaHome for the service</li>
<li>The current JDK as defined in the registry</li>
</ol></td>
</tr>
<tr>
<td>++JvmOptions</td>
<td>-Xrs</td>
<td>List of options in the form of <b>-D</b> or <b>-X</b> that will be
        passed to the JVM. The options are separated using either
        <b>#</b> or <b>;</b> characters. If you need to embed either # or ;
        character put them inside single quotes. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>++JvmOptions9</td>
<td></td>
<td>List of options in the form of <b>-D</b> or <b>-X</b> that will be
        passed to the JVM when running on Java 9 or later. The options are
        separated using either <b>#</b> or <b>;</b> characters. If you need to
        embed either # or ; character put them inside single quotes.
        (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--Classpath</td>
<td></td>
<td>Set the Java classpath. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--JvmMs</td>
<td></td>
<td>Initial memory pool size in MB. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--JvmMx</td>
<td></td>
<td>Maximum memory pool size in MB. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--JvmSs</td>
<td></td>
<td>Thread stack size in KB. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--StartMode</td>
<td></td>
<td>One of <b>jvm</b>, <b>Java</b> or <b>exe</b>.
    The modes are:

<ul>
<li>jvm - start Java in-process. Depends on jvm.dll, see <b>--Jvm</b>.</li>
<li>Java - same as exe, but automatically uses the default Java executable, i.e. %JAVA_HOME%\bin\java.exe.
    Make sure JAVA_HOME is set correctly, or use --JavaHome to provide the correct location.
    If neither is set, procrun will try to find the default JDK (not JRE) from the Windows registry.</li>
<li>exe - run the image as a separate process</li>
</ul>
</td>
</tr>
<tr>
<td>--StartImage</td>
<td></td>
<td>Executable that will be run. Only applies to <b>exe</b> mode.</td>
</tr>
<tr>
<td>--StartPath</td>
<td></td>
<td>Working path for the start image executable.</td>
</tr>
<tr>
<td>--StartClass</td>
<td>Main</td>
<td>Class that contains the startup method.
    Applies to the <b>jvm</b> and <b>Java</b> modes.  (Not used in <b>exe</b> mode.)
    </td>
</tr>
<tr>
<td>--StartMethod</td>
<td>main</td>
<td>Name of method to be called when service is started.
    It must be <code>static void</code> and have argument <code>(String args[])</code>.
    Only applies to <b>jvm</b> mode - in <b>Java</b> mode, the <b>main</b> method is always used.


<b>Note:</b> in <code>jvm</code> mode, the start method should not return until the stop method
    has been called.
    </td>
</tr>
<tr>
<td>++StartParams</td>
<td></td>
<td>List of parameters that will be passed to either StartImage or
        StartClass. Parameters are separated using either <b>#</b> or
        <b>;</b> character.</td>
</tr>
<tr>
<td>--StopMode</td>
<td></td>
<td>One of <b>jvm</b>, <b>Java</b> or <b>exe</b>.
    See <b>--StartMode</b> for further details.
    </td>
</tr>
<tr>
<td>--StopImage</td>
<td></td>
<td>Executable that will be run on Stop service signal. Only applies to <b>exe</b> mode.</td>
</tr>
<tr>
<td>--StopPath</td>
<td></td>
<td>Working path for the stop image executable. Does not apply to <b>jvm</b> mode.</td>
</tr>
<tr>
<td>--StopClass</td>
<td>Main</td>
<td>Class that will be used on Stop service signal.
    Applies to the <b>jvm</b> and <b>Java</b> modes.
    </td>
</tr>
<tr>
<td>--StopMethod</td>
<td>main</td>
<td>Name of method to be called when service is stopped.
    It must be <code>static void</code> and have argument <code>(String args[])</code>.
    Only applies to <b>jvm</b> mode.
    In <b>Java</b> mode, the <b>main</b> method is always used.
    </td>
</tr>
<tr>
<td>++StopParams</td>
<td></td>
<td>List of parameters that will be passed to either StopImage or
        StopClass. Parameters are separated using either <b>#</b> or
        <b>;</b> character.</td>
</tr>
<tr>
<td>--StopTimeout</td>
<td>60 seconds</td>
<td>Defines the timeout in seconds that procrun waits for service
        to stop.
        <b>The timeout applies to the stop command and to the time service needs to stop</b>
        Negative values are not allowed.
        Note: Make sure you use a value big enough to give time for
        procrun to stop the service. Once the time out is elapsed,
        procrun will try to kill the whole process tree the service
        has created.</td>
</tr>
<tr>
<td>--LogPath</td>
<td>%SystemRoot%\System32\LogFiles\Apache</td>
<td>Defines the path for logging. Creates the directory if necessary.</td>
</tr>
<tr>
<td>--LogPrefix</td>
<td>commons-daemon</td>
<td>Defines the service log filename prefix. The log file is created in the LogPath directory with
    <code>.YEAR-MONTH-DAY.log</code> suffix</td>
</tr>
<tr>
<td>--LogLevel</td>
<td>Info</td>
<td>Defines the logging level and can be either <b>Error</b>, <b>Warn</b>
<b>Info</b>, <b>Debug</b>, or <b>Trace</b>. (Case insensitive). Note
        that for all log entries, the maximum length of the message component of
        the log entry is 4096 characters.
    </td>
</tr>
<tr>
<td>--LogJniMessages</td>
<td>0</td>
<td>Set this non-zero (e.g. 1) to capture JVM jni debug messages in the procrun log file.
    Is not needed if stdout/stderr redirection is being used.

    Only applies to <b>jvm</b> mode.
    </td>
</tr>
<tr>
<td>--StdOutput</td>
<td></td>
<td>Redirected stdout filename. If named <b>auto</b> file is created
    inside <b>LogPath</b> with the name <b>service-stdout.YEAR-MONTH-DAY.log</b>.</td>
</tr>
<tr>
<td>--StdError</td>
<td></td>
<td>Redirected stderr filename. If named <b>auto</b> file is created
    in the <b>LogPath</b> directory with the name <b>service-stderr.YEAR-MONTH-DAY.log</b>.</td>
</tr>
<tr>
<td>--PidFile</td>
<td></td>
<td>Defines the file name for storing the running process id.
    Actual file is created in the <b>LogPath</b> directory</td>
</tr>
</table>
</section>
<section><a id="Installing_services"></a>
<h2>Installing services</h2>
<p>
To install the service, you need to use the <b>//IS</b> parameter.
</p>
<section><section><a id="Install_the_service_named_.27TestService.27"></a>
<h4>Install the service named 'TestService'</h4>
<pre><code>
prunsrv //IS//TestService --DisplayName="Test Service" \
        --Install=prunsrv.exe --Jvm=auto --StartMode=jvm --StopMode=jvm \
        --StartClass=org.apache.SomeStartClass --StartParams=arg1;arg2;arg3 \
        --StopClass=org.apache.SomeStopClass --StopParams=arg1#arg2
</code></pre>
</section></section></section>
<section><a id="Updating_services"></a>
<h2>Updating services</h2>
<p>
To update the service parameters, you need to use the <b>//US</b> parameter.
</p>
<section><section><a id="Update_the_service_named_.27TestService.27"></a>
<h4>Update the service named 'TestService'</h4>
<pre><code>
prunsrv //US//TestService --Description="Some Dummy Test Service" \
        --Startup=auto --Classpath=%CLASSPATH%;test.jar
</code></pre>
</section></section></section>
<section><a id="Removing_services"></a>
<h2>Removing services</h2>
<p>
To remove the service, you need to use the <b>//DS</b> parameter.
If the service is running it will be stopped and then deleted.
</p>
<section><section><a id="Remove_the_service_named_.27TestService.27"></a>
<h4>Remove the service named 'TestService'</h4>
<pre><code>prunsrv //DS//TestService</code></pre>
</section></section></section>
<section><a id="Debugging_services"></a>
<h2>Debugging services</h2>
<p>
To run the service in console mode, you need to use the <b>//TS</b> parameter.
The service shutdown can be initiated by pressing <b>CTRL+C</b> or
<b>CTRL+BREAK</b>.
If you rename the prunsrv.exe to testservice.exe then you can just execute the
testservice.exe and this command mode will be executed by default.
</p>
<section><section><a id="Run_the_service_named_.27TestService.27_in_console_mode"></a>
<h4>Run the service named 'TestService' in console mode</h4>
<pre><code>prunsrv //TS//TestService [additional arguments]</code></pre>
</section></section></section>
</section>
<section><a id="Using_Procrun_in_jvm_mode"></a>
<h1>Using Procrun in jvm mode</h1>
<p>
To interface with the Procrun service application (prunsrv) using the <b>jvm</b> mode, you need to create a class with the appropriate method(s).
For example:
</p>
<pre><code>
class MyClass;
// Error handling not shown
static void main(String [] args){
    String mode = args[0];
    if ("start".equals(mode){
        // process service start function
    }
    etc.
}
</code></pre>
This should be configured as follows:

<pre><code>
--Classpath MyClass.jar
--StartMode jvm --StartClass MyClass --StartParams start
--StopMode  jvm --StopClass  MyClass --StopParams  stop
</code></pre>
The above example uses a single 'main' method, and uses a string parameter to specify whether the service function
is start or stop.

Alternatively, you can use different method names for the service start and stop functions:

<pre><code>
class MyClass;
// Error handling not shown
static void start(String [] args){
        // process service start function
    }
static void stop(String [] args){
        // process service stop function
    }
}
</code></pre>
This should be configured as follows:

<pre><code>
--Classpath MyClass.jar
--StartMode jvm --StartClass MyClass --StartMethod start
--StopMode  jvm --StopClass  MyClass --StopMethod  stop
</code></pre>
Note: in jvm mode, the start method should not return until the stop method has
been called. The start and stop methods are called from different threads.

</section>
<section><a id="Using_Procrun_in_Java_or_exe_mode"></a>
<h1>Using Procrun in Java or exe mode</h1>
<p>
When using the <b>Java</b> or <b>exe</b> modes, the Procrun service application (prunsrv)
launches the target application in a separate process.
The "stop" application needs to communicate somehow with the "start" application to tell it to stop.
For example, using RPC.
</p>
</section>
<section><a id="Windows_Registry_Usage"></a>
<h1>Windows Registry Usage</h1>
<p>
The basic Service definitions are maintained under the registry key:
</p>
<pre><code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\&lt;ServiceName&gt;</code></pre>
Additional parameters are stored in the registry at:

<pre><code>HKEY_LOCAL_MACHINE\SOFTWARE\Apache Software Foundation\ProcRun 2.0\&lt;ServiceName&gt;\Parameters</code></pre>
<p>
On 64-bit Windows procrun always uses 32-bit registry view for storing the configuration.
This means that parameters will be stored inside:
</p>
<pre><code>HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\ProcRun 2.0\&lt;ServiceName&gt;</code></pre>
</section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jsvc"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/jsvc.html -->

<!-- page_index: 8 -->

# Introduction

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Introduction"></a>
<h1>Introduction</h1>
<p>
      Jsvc is a set of libraries and applications for making Java
      applications run on UNIX more easily.

      Jsvc allows the application (e.g. Tomcat) to perform some privileged operations as root
      (e.g. bind to a port &lt; 1024), and then switch identity to a non-privileged user.

      It can run on Win32 via the Cygwin emulation layer (see
      <a href="https://www.cygwin.com/"> Cygwin</a> for more information),
      however Win32 users may prefer to use <a href="#procrun"> procrun</a>
      instead, which allows the application to run as a Windows Service.
</p>
<p>
      The sources are located in the src/native/unix subdirectory.
</p>
<p>
      In the future <a href="https://apr.apache.org/"> APR </a> may be used
      to provide more portable platform support.
</p>
</section>
<section><a id="Building_from_source"></a>
<h1>Building from source</h1>
<p>
To build under a UNIX operating system you will need:
</p>
<ul>
<li>GNU AutoConf (at least version 2.53)</li>
<li>An ANSI-C compliant compiler (GCC is good)</li>
<li>GNU Make</li>
<li>A Java Platform 2 compliant SDK</li>
</ul>
<p>
You need to build the "configure" program with:
</p>
<pre><code>
sh support/buildconf.sh
</code></pre>
<p>
(Note it is possible to replace sh by any compatible shell like bash, ksh).

The result should be something like:
</p>
<pre><code>
support/buildconf.sh
support/buildconf.sh: configure script generated successfully
</code></pre>
Once the configure script is generated, follow the next section.

</section>
<section><a id="Building_from_a_release_tarball"></a>
<h1>Building from a release tarball</h1>
<p>
To build the binary under a UNIX operating system you will need:
</p>
<ul>
<li>An ANSI-C compliant compiler (GCC is good)</li>
<li>GNU Make</li>
<li>A Java Platform 2 compliant SDK</li>
</ul>
<p>
You have to specify the <code>JAVA_HOME</code> of the SDK
either with the <code>--with-java=&lt;dir&gt;</code> parameter or set the <code>JAVA_HOME</code> environment
to point to your SDK installation. For example:
</p>
<pre><code>
./configure --with-java=/usr/java
</code></pre>
or

<pre><code>
export JAVA_HOME
./configure
</code></pre>

If your operating system is supported, configure will go through cleanly, otherwise it will report an error (please send us the details of your
OS/JDK, or a patch against the sources). To build the binaries and
libraries simply do:

<pre><code>
make
</code></pre>
This will generate the executable file <code>jsvc</code>.

</section>
<section><a id="Starting_jsvc"></a>
<h1>Starting jsvc</h1>
<p>
To check the allowed parameters for the jsvc binary simply do:
</p>
<pre><code>
./jsvc -help
Usage: jsvc [-options] class [args...]

Where options include:

    -help | --help | -?
        show this help page (implies -nodetach)
    -jvm &lt;JVM name&gt;
        use a specific Java Virtual Machine. Available JVMs:
            'client' 'server'
    -client
        use a client Java Virtual Machine.
    -server
        use a server Java Virtual Machine.
    -cp / -classpath &lt;directories and zip/jar files&gt;
        set search path for service classes and resouces
    -home &lt;directory&gt;
        set the path of your JDK or JRE installation (or set
        the JAVA_HOME environment variable)
    -version
        show the current Java environment version (to check
        correctness of -home and -jvm. Implies -nodetach)
    -showversion
        show the current Java environment version (to check
        correctness of -home and -jvm) and continue execution.
    -nodetach
        don't detach from parent process and become a daemon
    -debug
        verbosely print debugging information
    -check
        only check service (implies -nodetach)
    -user &lt;user&gt;
        user used to run the daemon (defaults to current user)
    -verbose[:class|gc|jni]
        enable verbose output
    -cwd &lt;/full/path&gt;
        set working directory to given location (defaults to /)
    -outfile &lt;/full/path/to/file&gt;
        Location for output from stdout (defaults to /dev/null)
        Use the value '&amp;2' to simulate '1&gt;&amp;2'
    -errfile &lt;/full/path/to/file&gt;
        Location for output from stderr (defaults to /dev/null)
        Use the value '&amp;1' to simulate '2&gt;&amp;1'
    -pidfile &lt;/full/path/to/file&gt;
        Location for output from the file containing the pid of jsvc
        (defaults to /var/run/jsvc.pid)
    -D&lt;name&gt;=&lt;value&gt;
        set a Java system property
    -X&lt;option&gt;
        set Virtual Machine specific option
    -ea[:&lt;packagename&gt;...|:&lt;classname&gt;]
    -enableassertions[:&lt;packagename&gt;...|:&lt;classname&gt;]
        enable assertions
    -da[:&lt;packagename&gt;...|:&lt;classname&gt;]
    -disableassertions[:&lt;packagename&gt;...|:&lt;classname&gt;]
        disable assertions
    -esa | -enablesystemassertions
        enable system assertions
    -dsa | -disablesystemassertions
        disable system assertions
    -agentlib:&lt;libname&gt;[=&lt;options&gt;]
        load native agent library &lt;libname&gt;, e.g. -agentlib:hprof
    -agentpath:&lt;pathname&gt;[=&lt;options&gt;]
        load native agent library by full pathname
    -javaagent:&lt;jarpath&gt;[=&lt;options&gt;]
        load Java programming language agent, see java.lang.instrument
    -procname &lt;procname&gt;
        use the specified process name (works only for Linux)
    -wait &lt;waittime&gt;
        wait waittime seconds for the service to start
        waittime should multiple of 10 (min=10)
    -restarts &lt;maxrestarts&gt;
        maximum automatic restarts (integer)
        -1=infinite (default), 0=none, 1..(INT_MAX-1)=fixed restart count
    -stop
        stop the service using the file given in the -pidfile option
    -keepstdin
        does not redirect stdin to /dev/null
    --add-modules=&lt;module name&gt;
        Java 9 --add-modules option. Passed as it is to JVM
    --module-path=&lt;module path&gt;
        Java 9 --module-path option. Passed as it is to JVM
    --upgrade-module-path=&lt;module path&gt;
        Java 9 --upgrade-module-path option. Passed as it is to JVM
    --add-reads=&lt;module name&gt;
        Java 9 --add-reads option. Passed as it is to JVM
    --add-exports=&lt;module name&gt;
        Java 9 --add-exports option. Passed as it is to JVM
    --add-opens=&lt;module name&gt;
        Java 9 --add-opens option. Passed as it is to JVM
    --limit-modules=&lt;module name&gt;
        Java 9 --limit-modules option. Passed as it is to JVM
    --patch-module=&lt;module name&gt;
        Java 9 --patch-module option. Passed as it is to JVM
    --illegal-access=&lt;value&gt;
        Java 9 --illegal-access option. Passed as it is to JVM. Refer java help for possible values.
    --enable-preview
        Java 11 --enable-preview option. Passed as it is to JVM
    --enable-native-access=&lt;module name&gt;
        Java 21 --enable-native-access option. Passed as it is to JVM
</code></pre>
<section><a id="Mac_OS_X_universal_binaries"></a>
<h2>Mac OS X universal binaries</h2>
<p>
If jsvc was build with universal binary support the proper way of
starting <code>jsvc</code> is by using Mac OS X <code>arch</code> command:
</p>
<pre><code>
    arch -arch i386 ./jsvc -jvm server &lt;original jsvc parameters&gt;

    for running 64-bit JVM use the:
    arch -arch x86_64 ./jsvc -jvm server &lt;original jsvc parameters&gt;

</code></pre>
<p>
Use <code>-jvm server</code> because default <code>client</code> JVM is
not present for all architectures.
</p>
</section>
</section>
<section><a id="Using_jsvc"></a>
<h1>Using jsvc</h1>
<p>
There two ways to use jsvc: via a Class that implements the Daemon interface or
via calling a Class that has the required methods.
For example Tomcat-4.1.x uses the Daemon interface
whereas Tomcat-5.0.x provides a Class whose methods are called by jsvc directly.
</p>
<section><a id="Via_Daemon_interface"></a>
<h2>Via Daemon interface</h2>
<p>
Do the following:
</p>
<ul>
<li>Write a Class that implements the Daemon interface (MyClass).</li>
<li>Put it in a jarfile (my.jar).</li>
<li>Call jsvc like:

<pre><code>
./jsvc -cp commons-daemon.jar:my.jar MyClass
  </code></pre>
</li>
</ul>
</section>
<section><a id="Directly"></a>
<h2>Directly</h2>
<p>
Write a Class (MyClass) that implements the following methods:
</p>
<ul>
<li>void init(String[] arguments): Here open configuration files, create a trace file, create
      ServerSockets, Threads</li>
<li>void start(): Start the Thread, accept incoming connections</li>
<li>void stop(): Inform the Thread to terminate the run(), close the ServerSockets</li>
<li><code>void destroy()</code>: Destroy any object created in init()</li>
</ul>
<p>
Store it in a jarfile and use as above:
</p>
<pre><code>
./jsvc -cp my.jar MyClass
</code></pre>
</section>
</section>
<section><a id="How_jsvc_works"></a>
<h1>How jsvc works</h1>
<p>
Jsvc uses 3 processes: a launcher process, a controller process and a controlled process.
The controlled process is also the main java thread, if the JVM crashes
the controller will restart it in the next minute.
Jsvc is a daemon process so it should be started as root and the <code>-user</code> parameter
allows to downgrade to an unprivilegded user.
When the <code>-wait</code> parameter is used, the launcher process waits until the controller says
"I am ready", otherwise it returns after creating the controller process.
</p>
<section><a id="Forks_in_commons-daemon"></a>
<h2>Forks in commons-daemon</h2>
<p>
Launcher process:
</p>
<pre><code>
main()
{
  fork()
  parent: wait_child(), wait until JAVA service started when the child says "I am ready".
  child: controller process.
}
</code></pre>

Controller process:

<pre><code>
  while (fork()) {
    parent: wait_for_child.
      if exited and restart needed continue
      else exit.
    child: exit(child()). controlled process.
  }
</code></pre>

Controlled process:

<pre><code>
In child(): controlled process.
  init_JVM().
  load_service().
  start_service().
  say "I am ready"
  wait for signal or poll for stop
  stop_service().
  destroy_service().
  destroy_JVM().
  exit (with different codes so that parent knows if it has to restart us).
</code></pre>
Note: The controller process uses signals to stop the controlled process.

</section>
<section><a id="Downgrading_user"></a>
<h2>Downgrading user</h2>
<p>
On Linux <code>setuid()</code>/<code>setgid()</code> + capabilities are used. On other Unix <code>setgid</code>/<code>initgroups</code> are used.

We have something like:
</p>
<pre><code>
/* as root */
init_JVM().
load_service. /*  java_load() calls the load method */
downgrade user (set_caps() or set_user_group())
/* as the user $USER (from -user $USER parameter) */
umask()
start_service. /* java_start() calls the start method */
</code></pre>
</section>
</section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="binaries"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/binaries.html -->

<!-- page_index: 9 -->

# What to download?

In the directory
[binaries](https://downloads.apache.org/commons/daemon/binaries/)
you will find subdirectories containing archives
corresponding to your operating system. Only the Windows builds are provided as a zip file.

# How do I get the executable?

## procrun

The Windows archive (e.g. commons-daemon-x.y.z-bin-windows.zip) contains 2 different executables:

- prunsrv.exe - service application for running applications as services.
- prunmgr.exe - the GUI manager application used to monitor and configure installed services.

There is only one `prunmgr.exe` application for all architectures.
The `prunsrv.exe` executable is available in 2 different versions for different architectures.
The version in the top-level directory is for 32-bit (x86) architectures.
The lower level directories are for AMD/EMT 64-bit systems. Itanium is no longer supported.

The Windows application `prunsrv.exe` is used to install an application as a service.
Once installed, `prunmgr.exe` can be used to monitor and reconfigure the service.
(see [procrun](#procrun) for more information).
The Windows binary zip archive should be unpacked into the location from which you wish to run it, for example:
`%ProgramFiles%\Apache Commons Daemon`

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/faq.html -->

<!-- page_index: 10 -->

# Buildconf problems

```

$ sh support/buildconf.sh autoconf: Undefined macros:***BUG in Autoconf--please report*** AC_PATH ***BUG in Autoconf--please report*** AC_PATH ***BUG in Autoconf--please report*** AC_PATH
```

Your version of autoconf is too old, upgrade your autoconf and retry.
Or run support/buildconf.sh in another machine and copy the daemon tree in
the machine where you want to compile jsvc.

# Configure problems

```

configure: creating ./config.status
config.status: creating Makefile
mv: Makefile: set owner/group (was: 1670/0): Operation not permitted
config.status: creating Makedefs
mv: Makedefs: set owner/group (was: 1670/0): Operation not permitted
config.status: creating native/Makefile
mv: native/Makefile: set owner/group (was: 1670/0): Operation not permitted
*** All done ***
Now you can issue "make"
```

You should ignore those error messages they are normal in FreeBSD.
config.status creates files in /tmp and move them in the current directory.
When FreeBSD creates files it sets the group of the files to
the group of the directory where the files are created.
So if /tmp is group "wheel" the files are "wheel". When moving the files in
the current directory (if you are not member of group "wheel")
the group "wheel" cannot be set on the moved files.

# Runtime problems

On Linux 2.6.x jsvc does not start and write the following error:

```

jsvc.exec error: syscall failed in set_caps
jsvc.exec error: Service exit with a return value of 4
```

CONFIG\_SECURITY\_CAPABILITIES in missing in your kernel try the following in the kernel sources:

- Configure the kernel with "Default Linux Capabilities" and reboot
  (by make gconfig or make xconfig under "security options" and "Enable different security models")
- Insert the module "capability":

```

modprobe capability
```

# Cygwin configuration problems

The configure of jsvc does not like spaces in directory name.
To configure with java installed in directory whose name contains a space, use the 8 characters name of the directory.
For example for java in installed in `c:\Archivos de programa\java\jdk1.5.0_06`:

```

./configure --with-java=/cygdrive/c/Archiv~1/java/jdk1.5.0_06
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/project-info.html -->

<!-- page_index: 11 -->

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
<td>Apache Commons Daemon software is a set of utilities and Java support
    classes for running Java applications as server processes. These are
    commonly known as 'daemon' processes in Unix terminology (hence the
    name). On Windows they are called 'services'.</td></tr>
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
<td><a href="https://commons.apache.org/proper/commons-daemon/mailing-lists.html">Mailing Lists</a></td>
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

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/summary.html -->

<!-- page_index: 12 -->

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
<td>Apache Commons Daemon</td></tr>
<tr>
<td>Description</td>
<td>Apache Commons Daemon software is a set of utilities and Java support
    classes for running Java applications as server processes. These are
    commonly known as 'daemon' processes in Unix terminology (hence the
    name). On Windows they are called 'services'.</td></tr>
<tr>
<td>Homepage</td>
<td><a href="https://commons.apache.org/proper/commons-daemon/">https://commons.apache.org/proper/commons-daemon/</a></td></tr></table></section><section><a id="Project_Organization"></a>
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
<td>commons-daemon</td></tr>
<tr>
<td>ArtifactId</td>
<td>commons-daemon</td></tr>
<tr>
<td>Version</td>
<td>1.5.1</td></tr>
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

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/team.html -->

<!-- page_index: 13 -->

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
<td><figure><img src="assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg"/></figure></td>
<td><a id="jfclere"></a>jfclere</td>
<td>Jean-Frederic Clere</td>
<td><a href="mailto:jfclere at apache.org">jfclere at apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg"/></figure></td>
<td><a id="remm"></a>remm</td>
<td>Remy Maucherat</td>
<td><a href="mailto:remm at apache.org">remm at apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg"/></figure></td>
<td><a id="yoavs"></a>yoavs</td>
<td>Yoav Shapira</td>
<td><a href="mailto:yoavs at apache.org">yoavs at apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg"/></figure></td>
<td><a id="billbarker"></a>billbarker</td>
<td>Bill Barker</td>
<td><a href="mailto:billbarker at apache.org">billbarker at apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg"/></figure></td>
<td><a id="mturk"></a>mturk</td>
<td>Mladen Turk</td>
<td><a href="mailto:mturk at apache.org">mturk at apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg"/></figure></td>
<td><a id="pier"></a>pier</td>
<td>Pier Fumagalli</td>
<td><a href="mailto:pier at apache.org">pier at apache.org</a></td>
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
<th>Email</th></tr>
<tr>
<td><figure><img src="assets/images/b7540f73db192bd34c6880a272d78612_1e0c169e26914241.jpg"/></figure></td>
<td>Nick Griffiths</td>
<td><a href="mailto:nicobrevin@gmail.com">nicobrevin@gmail.com</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/dependency-management.html -->

<!-- page_index: 14 -->

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

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependencies"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/dependencies.html -->

<!-- page_index: 15 -->

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
<td>org.junit.jupiter</td>
<td><a href="https://junit.org/">junit-jupiter</a></td>
<td>5.14.1</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr></table></section></section><section><a id="Project_Transitive_Dependencies"></a>
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
<td>org.apiguardian</td>
<td><a href="https://github.com/apiguardian-team/apiguardian">apiguardian-api</a></td>
<td>1.1.2</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr>
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
<td>org.opentest4j</td>
<td><a href="https://github.com/ota4j-team/opentest4j">opentest4j</a></td>
<td>1.3.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr></table></section></section><section><a id="Project_Dependency_Graph"></a>
<h1>Project Dependency Graph</h1>
<section><a id="Dependency_Tree"></a>
<h2>Dependency Tree</h2>
</section></section><section><a id="Licenses"></a>
<h1>Licenses</h1>
<p><b>The Apache License, Version 2.0: </b>org.apiguardian:apiguardian-api, org.opentest4j:opentest4j</p>
<p><b>Apache-2.0: </b>Apache Commons Daemon</p>
<p><b>Eclipse Public License v2.0: </b>JUnit Jupiter (Aggregator), JUnit Jupiter API, JUnit Jupiter Engine, JUnit Jupiter Params, JUnit Platform Commons, JUnit Platform Engine API</p></section><section><a id="Dependency_File_Details"></a>
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
<td>apiguardian-api-1.1.2.jar</td>
<td>6.8 kB</td>
<td>9</td>
<td>3</td>
<td>2</td>
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
<td>8</td>
<td>1.7 MB</td>
<td>1154</td>
<td>1026</td>
<td>64</td>
<td>9</td>
<td>7</td></tr>
<tr>
<td>test: 8</td>
<td>test: 1.7 MB</td>
<td>test: 1154</td>
<td>test: 1026</td>
<td>test: 64</td>
<td>9</td>
<td>test: 7</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-convergence"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/dependency-convergence.html -->

<!-- page_index: 16 -->

# Dependency Convergence

**Statistics:**

| Number of dependencies (NOD): | 8 |
| Number of unique artifacts (NOA): | 8 |
| Number of version-conflicting artifacts (NOC): | 0 |
| Number of SNAPSHOT artifacts (NOS): | 0 |
| Convergence (NOD/NOA): | [Success] **100 %** |
| Ready for release (100% convergence and no SNAPSHOTS): | [Success] **Success** |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/ci-management.html -->

<!-- page_index: 17 -->

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
<pre><a href="https://github.com/apache/commons-daemon/actions">https://github.com/apache/commons-daemon/actions</a></pre></section><section><a id="Notifiers"></a>
<h1>Notifiers</h1>
<p>No notifiers are defined. Please check back at a later date.</p></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="distribution-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/distribution-management.html -->

<!-- page_index: 18 -->

# Overview

The following is the distribution management information used by this project.

## Repository - apache.releases.https

<https://repository.apache.org/service/local/staging/deploy/maven2>

## Snapshot Repository - apache.snapshots.https

<https://repository.apache.org/content/repositories/snapshots>

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/project-reports.html -->

<!-- page_index: 19 -->

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
<td><a href="https://commons.apache.org/proper/commons-daemon/apidocs/index.html">Javadoc</a></td>
<td>Javadoc API documentation.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-daemon/xref/index.html">Source Xref</a></td>
<td>HTML based, cross-reference version of Java source code.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-daemon/xref-test/index.html">Test Source Xref</a></td>
<td>HTML based, cross-reference version of Java test source code.</td></tr>
<tr>
<td><a href="#surefire">Surefire</a></td>
<td>Report on the test results of the project.</td></tr>
<tr>
<td><a href="#rat-report">RAT Report</a></td>
<td>Report on compliance to license related source code policies</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-daemon/jacoco/index.html">JaCoCo</a></td>
<td>JaCoCo Coverage Report.</td></tr>
<tr>
<td><a href="https://commons.apache.org/proper/commons-daemon/japicmp.html">japicmp</a></td>
<td>Comparing source compatibility of commons-daemon-1.5.1.jar against commons-daemon-1.5.0.jar</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/jira-changes.html -->

<!-- page_index: 20 -->

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
<td><a href="https://issues.apache.org/jira/browse/DAEMON-416">DAEMON-416</a></td>
<td>-</td>
<td>prunsrv.exe adding special character while executing in windows 2019</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-475">DAEMON-475</a></td>
<td>Procrun</td>
<td>EXE MODE - Apache Commons Daemon Child process exit code 1 - Service Still Running</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-474">DAEMON-474</a></td>
<td>prunsrv</td>
<td>Logging doesn't work on 1.40./1.4.1 - Regression of 1.3.4 (worked perfectly)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-439">DAEMON-439</a></td>
<td>prunsrv</td>
<td>prunsrv '--Startup=delayed' sets manual mode instead</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-398">DAEMON-398</a></td>
<td>Procrun, prunsrv</td>
<td>Java 11 jvm.dll startup messages not available on stdout/stderr using Windows 10/2016</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-472">DAEMON-472</a></td>
<td>-</td>
<td>replace license.rtf with plain text</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-471">DAEMON-471</a></td>
<td>Jsvc</td>
<td>Add support for --enable-native-access Java startup option in jsvc</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-468">DAEMON-468</a></td>
<td>prunsrv</td>
<td>Fix timeout handling in procrun</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-466">DAEMON-466</a></td>
<td>prunsrv</td>
<td>Service crashes with 1067 when stopping</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-460">DAEMON-460</a></td>
<td>prunsrv</td>
<td>High CPU usage in prunsrv.exe since Daemon 1.3.3</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-463">DAEMON-463</a></td>
<td>Jsvc</td>
<td>Daemon fails to build on macOS with XCode 15.3</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-429">DAEMON-429</a></td>
<td>Procrun, prunsrv</td>
<td>prunsrv.exe, and prunmgr.exe improper binary protection</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-461">DAEMON-461</a></td>
<td>Procrun</td>
<td>Improve "Path to executable:" label on service manager General tab</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-459">DAEMON-459</a></td>
<td>Jsvc</td>
<td>Restart only works once (regression)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-458">DAEMON-458</a></td>
<td>Procrun</td>
<td>The changes in DAEMON-446 cause existing DependsOn values to be removed</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-451">DAEMON-451</a></td>
<td>Procrun</td>
<td>Prunsrv does not use configured stack size for the main thread in jvm mode</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-452">DAEMON-452</a></td>
<td>prunsrv</td>
<td>Should we create the target folder before apxSecurityGrantFileAccessToUser?</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-450">DAEMON-450</a></td>
<td>prunsrv</td>
<td>Invoked "bin\tomcat9 //US/Tomcat9", logs directory will be inserted unwanted two ACLs</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.2</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-448">DAEMON-448</a></td>
<td>prunsrv</td>
<td>Service start fails with default Eclipse Temurin install</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.2</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-446">DAEMON-446</a></td>
<td>Procrun</td>
<td>Update service (//US) does not change DependsOn</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-443">DAEMON-443</a></td>
<td>-</td>
<td>prunsrv writes gigabytes of null bytes to stderr</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-442">DAEMON-442</a></td>
<td>Procrun</td>
<td>ProcRun classpath limitation of 1010 characters truncates the classpath string for many libraries on the classpath</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a></td>
<td>-</td>
<td>When installing a Windows service using Commons Daemon 1.3.0 the errorlevel is -1073741819</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-437">DAEMON-437</a></td>
<td>prunsrv</td>
<td>prunsrv: Better not to redirect stdout/stderr during service installation?</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-430">DAEMON-430</a></td>
<td>Procrun</td>
<td>prunsrv stop timeout not honored</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-428">DAEMON-428</a></td>
<td>prunsrv</td>
<td> apxMultiSzToArrayW has incorrect use of IS_INVALID_HANDLE</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-426">DAEMON-426</a></td>
<td>Jsvc</td>
<td>CAP_DAC_READ_SEARCH not allowed in containers by default</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-425">DAEMON-425</a></td>
<td>Procrun</td>
<td>Crash if Java Options parameter is missing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-424">DAEMON-424</a></td>
<td>prunsrv</td>
<td>stderr logfile is corrupted when running Tomcat 8.5 as Windows service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-412">DAEMON-412</a></td>
<td>Procrun</td>
<td>Tomcat started as windows service does not support Java Native Memory Tracking feature probably because of improper JVM initialization by Procrun</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-410">DAEMON-410</a></td>
<td>Jsvc</td>
<td>jsvc fails to find OpenJDK11 libjvm.so on a raspberry 4 (buster)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-422">DAEMON-422</a></td>
<td>Procrun</td>
<td>Add "dump configuration" mode of operation which generates a .BAT file capabile of re-creating the dumped service</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-419">DAEMON-419</a></td>
<td>Jsvc</td>
<td>jsvc support for Java 12+ preview features with --enable-preview</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-414">DAEMON-414</a></td>
<td>prunsrv</td>
<td>prunsrv uses its log is before it is initialized.</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-314">DAEMON-314</a></td>
<td>Jsvc</td>
<td>[daemon] feature request: jsvc stop with force option</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.2</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-408">DAEMON-408</a></td>
<td>Procrun</td>
<td>PROCRUN 1.2.x x64 crash on Windows Server 2008 R2</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-407">DAEMON-407</a></td>
<td>Procrun</td>
<td>Prunmgr displays incorrect logging level.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-404">DAEMON-404</a></td>
<td>Procrun</td>
<td>Crash: Openjdk not detected from registry</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-403">DAEMON-403</a></td>
<td>Jsvc</td>
<td>umask log is wrong</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-399">DAEMON-399</a></td>
<td>Procrun</td>
<td>apxStrUnQuoteInplaceA removes needed quotes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-394">DAEMON-394</a></td>
<td>Procrun</td>
<td>Monitor application will update multi-string values in Windows registry with blank lines</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-402">DAEMON-402</a></td>
<td>Procrun</td>
<td>frequent crash in prunsrv when stopping service in 'java' mode</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1, 1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-401">DAEMON-401</a></td>
<td>-</td>
<td>Environment variables set on service not available in JNI dll</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-396">DAEMON-396</a></td>
<td>Procrun</td>
<td>LibraryPath is broken for Java 11 using Windows 10/2016</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-393">DAEMON-393</a></td>
<td>-</td>
<td>Revered code comments for JRE and JDK locations in the registry</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-392">DAEMON-392</a></td>
<td>-</td>
<td>Undefined behaviour in registry.c dwRegKey = dwRegKey++</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-391">DAEMON-391</a></td>
<td>Procrun</td>
<td>Log level set by Tomcat-GUI under Windows not recognized.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-388">DAEMON-388</a></td>
<td>Jsvc</td>
<td>jsvc does not play nice with JMX</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-385">DAEMON-385</a></td>
<td>Jsvc</td>
<td>commons-daemon-1.1.0 not supported with AIX 7</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-384">DAEMON-384</a></td>
<td>Procrun</td>
<td>prunsrv stopping with error due to hardcoded timeout</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-379">DAEMON-379</a></td>
<td>-</td>
<td>Unable to build with Java 9 using Ant</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-329">DAEMON-329</a></td>
<td>Procrun</td>
<td>Can procrun detect the JVM without consulting the registry</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-297">DAEMON-297</a></td>
<td>-</td>
<td>Show jsvc path in debug output</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-151">DAEMON-151</a></td>
<td>Procrun</td>
<td>Enable/Disable fields on the Start/Stop panels according to which Mode is selected</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-303">DAEMON-303</a></td>
<td>Procrun</td>
<td>prunsrv --Startup should offer "Automatic (Delayed Start)" option for service startup</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-397">DAEMON-397</a></td>
<td>Jsvc</td>
<td>jsvc on macOS cannot find libjli.dylib when home is OpenJDK 10 or 11</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-377">DAEMON-377</a></td>
<td>-</td>
<td>Race in PID file handing in jsvc resulting in Tomcat running without a pidfile</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-376">DAEMON-376</a></td>
<td>-</td>
<td>Update Daemon to also search registry for JRE with Java 9 JRE location</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-374">DAEMON-374</a></td>
<td>Jsvc</td>
<td>Add support for Java 9 command-line arguments</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-373">DAEMON-373</a></td>
<td>Jsvc</td>
<td>Daemon does not start with JDK9</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-372">DAEMON-372</a></td>
<td>Procrun</td>
<td>create shutdown event for shutdown process</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-358">DAEMON-358</a></td>
<td>Jsvc</td>
<td>PPC64: jsvc fails to find JVM jvm.cfg file and shared objects due to wrong path</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-347">DAEMON-347</a></td>
<td>Jsvc</td>
<td>Add AArch64 support to src/native/unix/support/apsupport.m4</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-339">DAEMON-339</a></td>
<td>Jsvc</td>
<td>Patch for commons-daemon 1.0.15 to avoid shutdown failures</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-333">DAEMON-333</a></td>
<td>Jsvc</td>
<td>Stop abusing System.gc() on Commons Daemon jsvc shutdown</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-332">DAEMON-332</a></td>
<td>Procrun</td>
<td>pid file not readable on Windows 7/8/2008</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-324">DAEMON-324</a></td>
<td>-</td>
<td>[home.c:130]: (error) Resource leak: cfgf</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-319">DAEMON-319</a></td>
<td>-</td>
<td>Add mips ABI n32, n64 support </td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-318">DAEMON-318</a></td>
<td>Jsvc</td>
<td>children (controller) process doesnt use correct umask value</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-312">DAEMON-312</a></td>
<td>Procrun</td>
<td>prunmgr: //MQ fails to kill multiple instances</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-311">DAEMON-311</a></td>
<td>Procrun</td>
<td>Commons Daemon procrun failed with exit value: 5 (Failed to start service)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-310">DAEMON-310</a></td>
<td>Jsvc</td>
<td>jsvc fails on AIX 5.3</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-309">DAEMON-309</a></td>
<td>Procrun</td>
<td>Documentation for start method in JVM mode is conflicting</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-302">DAEMON-302</a></td>
<td>Procrun</td>
<td>Service recovery options do not work when a JNI crash brings down the JVM</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-282">DAEMON-282</a></td>
<td>Procrun</td>
<td>Failed to stop 'xx' service: The data area passed to a system call is too small</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-395">DAEMON-395</a></td>
<td>Jsvc</td>
<td>Fix hash links on download page</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-368">DAEMON-368</a></td>
<td>Procrun</td>
<td>Add DEBUG and ERROR logging to help diagnose problems when starting a Windows Service</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-343">DAEMON-343</a></td>
<td>-</td>
<td>Add 64-bit POWERPC-LE (ppc64le) support</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-334">DAEMON-334</a></td>
<td>Jsvc</td>
<td>Specify a maximum limit for automatic restarts</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-308">DAEMON-308</a></td>
<td>-</td>
<td>Add 64-bit ARM (aarch64) support</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-289">DAEMON-289</a></td>
<td>-</td>
<td>Integrate Debian patches</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-243">DAEMON-243</a></td>
<td>Procrun</td>
<td>Support for Failure Recovery</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-371">DAEMON-371</a></td>
<td>-</td>
<td>Update Java requirement from version 5 to 6.</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-370">DAEMON-370</a></td>
<td>-</td>
<td>Move attributions from @author in Javadocs to POM</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-346">DAEMON-346</a></td>
<td>Procrun</td>
<td>Compile PROCRUN with Data Execution Prevention (DEP) flag</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.15</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-292">DAEMON-292</a></td>
<td>Procrun</td>
<td>Thread dump does not work</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.15</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-291">DAEMON-291</a></td>
<td>Jsvc</td>
<td>jsvc cores on Linux</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.15</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-288">DAEMON-288</a></td>
<td>Procrun</td>
<td>Hang while stopping procrun service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-287">DAEMON-287</a></td>
<td>Procrun</td>
<td>procrun's CloseHandle(_service_status_handle) not needed and causes exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-286">DAEMON-286</a></td>
<td>Procrun</td>
<td>Race condition during stopping service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-284">DAEMON-284</a></td>
<td>-</td>
<td>Service configuration corruption on install</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-283">DAEMON-283</a></td>
<td>Jsvc</td>
<td>DaemonWrapper cannot start launch methods with private constructors</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14, 1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-281">DAEMON-281</a></td>
<td>Jsvc</td>
<td>Jsvc not loading correct shared lib for Java 7 on MacOS</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-280">DAEMON-280</a></td>
<td>Jsvc</td>
<td>jsvc umask comparison wrong - fix attached</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-278">DAEMON-278</a></td>
<td>Procrun</td>
<td>procrunsrv windows ++Environment doesn't work for java type</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.13</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-276">DAEMON-276</a></td>
<td>-</td>
<td>commons-daemon.log blows up when stopping Windows service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.13</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-275">DAEMON-275</a></td>
<td>-</td>
<td>Website says that non-Windows binaries may be provided</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.12</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-274">DAEMON-274</a></td>
<td>Procrun</td>
<td>procrun ignores shutdown</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.0.12</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-272">DAEMON-272</a></td>
<td>Jsvc</td>
<td>jsvc ignores -home option</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.12</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-268">DAEMON-268</a></td>
<td>Jsvc</td>
<td>jsvc fails to find java home on centos</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/surefire.html -->

<!-- page_index: 21 -->

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
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.064 s</td></tr></table>
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
<td><a href="#surefire--org.apache.commons.daemon">org.apache.commons.daemon</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.064 s</td></tr></table>
<p>Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.</p><section><a id="org.apache.commons.daemon"></a>
<h3>org.apache.commons.daemon</h3>
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
<td><a href="#surefire--org.apache.commons.daemon.daemoninitexceptiontest"><img src="assets/images/icon-success-sml_2a836ab2a11e9e07.gif"/></a></td>
<td><a href="#surefire--org.apache.commons.daemon.daemoninitexceptiontest">DaemonInitExceptionTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.064 s</td></tr></table></section>
</section><section><a id="Test_Cases"></a>
<h2>Test Cases</h2>
<p>[<a href="#surefire--summary">Summary</a>] [<a href="#surefire--package_list">Package List</a>] [<a href="#surefire--test_cases">Test Cases</a>]</p><section><a id="org.apache.commons.daemon.DaemonInitExceptionTest"></a>
<h3>DaemonInitExceptionTest</h3>
<table>
<tr>
<td><img src="assets/images/icon-success-sml_2a836ab2a11e9e07.gif"/></td>
<td><a id="TC_org.apache.commons.daemon.DaemonInitExceptionTest.test"></a>test</td>
<td>0.033 s</td></tr></table></section>
</section></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/rat-report.html -->

<!-- page_index: 22 -->

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
Generated at: 2025-12-16T13:35:58Z
    by Apache Creadur RAT::Core 0.17 (Apache Software Foundation)

-----------------------------------------------------
Counters
-----------------------------------------------------
    (Entries starting with '!' exceed the minimum or maximum values)
  Approved:           117    A count of approved licenses.
  Archives:           0    A count of archive files.
  Binaries:           27    A count of binary files.
  Document types:     4    A count of distinct document types.
  Ignored:            11    A count of ignored files.
  License categories: 1    A count of distinct license categories.
  License names:      1    A count of distinct license names.
  Notices:            7    A count of notice files.
  Standards:          117    A count of standard files.
  Unapproved:         0    A count of unapproved licenses.
  Unknown:            0    A count of unknown file types.

-----------------------------------------------------
Licenses detected
-----------------------------------------------------

Apache License 2.0: 117

-----------------------------------------------------
License Categories detected
-----------------------------------------------------

AL   : 117

-----------------------------------------------------
Document Types detected
-----------------------------------------------------

BINARY: 27
IGNORED: 11
NOTICE: 7
STANDARD: 117

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

  /.git
  I         application/octet-stream     (directory)

  /.gitattributes
  I         application/octet-stream

  /.github
  I         application/octet-stream     (directory)

  /.gitignore
  I         application/octet-stream

  /CODE_OF_CONDUCT.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /CONTRIBUTING.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /HOWTO-RELEASE.txt
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /LICENSE.txt
  N         text/plain    ISO-8859-1

  /NOTICE.txt
  N         text/plain    ISO-8859-1

  /PROPOSAL.html
  S         text/html    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /README.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /RELEASE-NOTES.txt
  N         text/plain    ISO-8859-1

  /SECURITY.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /pom.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/bin.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/native-src.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/src.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/win.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/changes/changes.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/docs/daemon.css
  S         text/css    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/docs/daemon.html
  S         text/html    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/Daemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonContext.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonController.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonInitException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonPermission.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonUserSignal.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/support/DaemonConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/support/DaemonLoader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/support/DaemonWrapper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/media/commons-logo-component-100.xcf
  B         image/x-xcf

  /src/media/commons-logo-component.xcf
  B         image/x-xcf

  /src/media/logo.png
  B         image/png

  /src/native/unix/INSTALL.txt
  N         text/plain    ISO-8859-1

  /src/native/unix/Makedefs.in
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/Makefile.in
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/autom4te.cache
  I         application/octet-stream     (directory)

  /src/native/unix/configure
  I         application/octet-stream

  /src/native/unix/configure.ac
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/man/README.txt
  N         text/plain    ISO-8859-1

  /src/native/unix/man/fetch.sh
  B         application/x-sh

  /src/native/unix/man/jsvc.1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/.indent.pro
  S         text/x-prolog    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/Makefile.in
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/arguments.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/arguments.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/debug.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/debug.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/dso-dlfcn.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/dso-dyld.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/dso.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/help.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/help.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/home.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/home.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/java.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/java.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/jsvc-unix.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/jsvc.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/location.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/location.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/locks.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/locks.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/replace.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/replace.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/signals.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/signals.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/version.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/apfunctions.m4
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/apjava.m4
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/apsupport.m4
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/buildconf.sh
  B         application/x-sh

  /src/native/unix/support/config.guess
  I         application/octet-stream

  /src/native/unix/support/config.sub
  I         application/octet-stream

  /src/native/windows/README.txt
  N         text/plain    ISO-8859-1

  /src/native/windows/apps/prunmgr/Makefile
  S         text/x-makefile    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.manifest
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.rc
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/Makefile
  S         text/x-makefile    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.manifest
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.rc
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/test/scripts/cleanstd.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/deleteservice.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/isemptystd.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/mybanner.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/startservice.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/stopservice.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/test.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/testservice.bat
  B         application/x-bat

  /src/native/windows/apps/prunsrv/test/scripts/waituntilstop.bat
  B         application/x-bat

  /src/native/windows/include/Makefile.inc
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/apxwin.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/cmdline.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/console.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/gui.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/handles.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/javajni.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/log.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/registry.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/rprocess.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/security.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/service.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/resources/commons.bmp
  B         image/bmp

  /src/native/windows/resources/procrunr.ico
  B         image/vnd.microsoft.icon

  /src/native/windows/resources/procruns.ico
  B         image/vnd.microsoft.icon

  /src/native/windows/resources/procrunw.ico
  B         image/vnd.microsoft.icon

  /src/native/windows/resources/susers.bmp
  B         image/bmp

  /src/native/windows/src/cmdline.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/console.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/gui.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/handles.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/javajni.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/log.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/mclib.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/mclib.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/private.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/registry.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/rprocess.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/security.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/service.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/utils.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/xdocs/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/AloneDaemon.sh
  B         application/x-sh

  /src/samples/AloneService.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/Native.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/Native.sh
  B         application/x-sh

  /src/samples/ProcrunService.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/ProcrunServiceInstall.cmd
  B         application/x-bat

  /src/samples/ProcrunServiceRemove.cmd
  B         application/x-bat

  /src/samples/README.txt
  N         text/plain    ISO-8859-1

  /src/samples/ServiceDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/ServiceDaemon.sh
  B         application/x-sh

  /src/samples/ServiceDaemonReadThread.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/SimpleApplication.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/SimpleApplication.sh
  B         application/x-sh

  /src/samples/SimpleDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/SimpleDaemon.sh
  B         application/x-sh

  /src/samples/build.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/download_daemon.cgi
  I         text/x-cgi

  /src/site/resources/images/logo.png
  B         image/png

  /src/site/resources/profile.jacoco
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/profile.japicmp
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/site.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/binaries.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/download_daemon.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/faq.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/issue-tracking.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/jsvc.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/mail-lists.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/procrun.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/security.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/daemon/DaemonInitExceptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/daemon/ProcrunDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/daemon/SimpleDaemon.java
  S         text/x-java-source    ISO-8859-1
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

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---
