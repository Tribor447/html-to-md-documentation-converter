# Project Information

## Navigation

- [Commons BeanUtils](#index)
  - [About](#index)
  - [Release History](#changes)
  - [Sources](#scm)
  - [Security](#security)
- Documentation
  - [Building](#building)
  - [2.0.0-M2](#index)
  - [2.0.0-M1](#index)
  - [1.11.0](#index)
  - [1.10.1](#index)
  - [1.9.3](#index)
  - [1.9.2](#index)
  - [1.8.3](#index)
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
    - [PMD](#pmd)
    - [SpotBugs](#spotbugs)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/index.html -->

<!-- page_index: 1 -->

# Commons BeanUtils

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Commons_BeanUtils"></a>
DOC2MDPLACEHOLDERTOKEN0END<h1>Commons BeanUtils</h1>
<p>
Most Java developers are used to creating Java classes that conform to the
JavaBeans naming patterns for property getters and setters.  It is natural to
then access these methods directly, using calls to the corresponding
<code>getXxx</code> and <code>setXxx</code> methods.  However, there are some
occasions where dynamic access to Java object properties (without compiled-in
knowledge of the property getter and setter methods to be called) is needed.
Example use cases include:</p>
<ul>
<li>Building scripting languages that interact with the Java object model
    (such as the Bean Scripting Framework).</li>
<li>Building template language processors for web presentation and similar
    uses (such as JSP or Velocity).</li>
<li>Building custom tag libraries for JSP and XSP environments (such as Jakarta
    Taglibs, Struts, Cocoon).</li>
<li>Consuming XML-based configuration resources (such as Ant build scripts, web
    application deployment descriptors, Tomcat's <code>server.xml</code>
    file).</li>
</ul>
<p>
The Java language provides <em>Reflection</em> and <em>Introspection</em>
APIs (see the <code>java.lang.reflect</code> and <code>java.beans</code>
packages in the JDK Javadocs).  However, these APIs can be quite complex to
understand and utilize.  The  <em>BeanUtils</em> component provides
easy-to-use wrappers around these capabilities.
</p>
<section><a id="BeanUtils_Core_And_Modules"></a>
DOC2MDPLACEHOLDERTOKEN1END<h2>BeanUtils Core And Modules</h2>
<p>
The 1.7.x and 1.8.x releases of BeanUtils distributed three jars:
</p>
<ul>
<li><code>commons-beanutils.jar</code> - contains everything</li>
<li><code>commons-beanutils-core.jar</code> - excludes <i>Bean Collections</i> classes</li>
<li><code>commons-beanutils-bean-collections.jar</code> - only <i>Bean Collections</i> classes</li>
</ul>
<p>
The main <code>commons-beanutils.jar</code> has an <b><i>optional</i></b> dependency on
<a href="https://commons.apache.org/collections">Commons Collections</a>
</p>
<p>
Version 1.9.0 reverts this split for reasons outlined at
<a href="https://issues.apache.org/jira/browse/BEANUTILS-379">BEANUTILS-379</a>.
There is now only one jar for the BeanUtils library.
</p>
<p>
Version 2.0.0 updates the dependencies for Apache Commons Collection from version 3 to 4.
Apache Commons Collection 4 changes packages from <code>org.apache.commons.collections</code>
to <code>org.apache.commons.collections4</code>.
Since some Commons BeanUtils APIs surface Commons Collection types, Commons BeanUtils 2 changes packages from <code>org.apache.commons.beanutils</code>
to <code>org.apache.commons.beanutils2</code>.
</p>
</section>
<section><a id="Bean_Collections"></a>
DOC2MDPLACEHOLDERTOKEN2END<h2>Bean Collections</h2>
<p>
Bean collections is a library combining BeanUtils with
<a href="https://commons.apache.org/collections">Commons Collections</a>
to provide services for collections of beans. One class (<code>BeanComparator</code>)
was previously released, the rest are new. This new distribution strategy should allow
this sub-component to evolve naturally without the concerns about size and scope
that might otherwise happen.
</p>
<p>
Bean Collections has an additional dependency on
<a href="https://commons.apache.org/collections">Commons Collections</a>.
</p>
</section>
</section>
<section><a id="Releases"></a>
DOC2MDPLACEHOLDERTOKEN3END<h1>Releases</h1>
<section><a id="a2.0.x_releases"></a>
DOC2MDPLACEHOLDERTOKEN4END<h2>2.0.x releases</h2>
<p>
    BeanUtils <strong>2.0.x</strong> releases are not binary compatible (but easy to port) with version 1.x.x and require a minimum of
    Java 8.
  </p>
<p>
    The latest BeanUtils release is available to download
    <a href="https://commons.apache.org/beanutils/download_beanutils.cgi">here</a>.
  </p>
<ul>
<li>2.0.0

<ul>
<li><a href="https://commons.apache.org/beanutils/changes.html">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
</ul>
</section>
<section><a id="a1.9.x_releases"></a>
DOC2MDPLACEHOLDERTOKEN5END<h2>1.9.x releases</h2>
<p>
    The latest BeanUtils release is available to download
    <a href="https://commons.apache.org/beanutils/download_beanutils.cgi">here</a>.
<em><strong>1.9.4</strong></em>
</p>
<ul>
<li><a href="https://commons.apache.org/beanutils/changes.html#a1.9.4">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.9.4/apidocs/index.html">JavaDoc</a></li>
</ul>
<p>
<strong>CVE-2019-10086.</strong> Apache Commons Beanutils does not suppresses
    the class property in bean introspection by default.
<strong>Severity.</strong> Medium
<strong>Vendor.</strong> The Apache Software Foundation
<strong>Versions Affected.</strong> All versions commons-beanutils-1.9.3 and before.
<strong>Description.</strong> In version 1.9.2, a special BeanIntrospector class was added which allows suppressing the ability for
    an attacker to access the classloader via the class property available on all Java objects. We, however were not
    using this by default characteristic of the PropertyUtilsBean.
<strong>Mitigation.</strong> Upgrade to commons-beanutils-1.9.4
<strong>Credit.</strong> This was discovered by Melloware (https://melloware.com/).
<strong>Example.</strong>
</p>
<pre><code>/**
* Example usage after 1.9.4
*/
public void testSuppressClassPropertyByDefault() throws Exception {
  final BeanUtilsBean bub = new BeanUtilsBean();
  final AlphaBean bean = new AlphaBean();
  try {
    bub.getProperty(bean, "class");
    fail("Could access class property!");
  } catch (final NoSuchMethodException ex) {
    // ok
  }
}

/**
* Example usage to restore 1.9.3 behavior
*/
public void testAllowAccessToClassProperty() throws Exception {
  final BeanUtilsBean bub = new BeanUtilsBean();
  bub.getPropertyUtils().removeBeanIntrospector(SuppressPropertiesBeanIntrospector.SUPPRESS_CLASS);
  final AlphaBean bean = new AlphaBean();
  String result = bub.getProperty(bean, "class");
  assertEquals("Class property should have been accessed", "class org.apache.commons.beanutils2.AlphaBean", result);
}</code></pre>
<p>
    BeanUtils <strong>1.9.x</strong> releases are binary compatible (with a minor exception
    described in the release notes) with version 1.8.3 and require a minimum of
    JDK 1.5.
  </p>
<p>
    The latest BeanUtils release is available to download
    <a href="https://commons.apache.org/beanutils/download_beanutils.cgi">here</a>.
  </p>
<ul>
<li>1.9.3

<ul>
<li><a href="assets/files/release-notes_e6bc7328f4da5bd9.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.9.3/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
<li>1.9.2

<ul>
<li><a href="assets/files/release-notes_920f61732c363750.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.9.2/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
<li>1.9.1

<ul>
<li><a href="assets/files/release-notes_396bd27e40ca7095.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.9.1/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
<li>1.9.0

<ul>
<li><a href="assets/files/release-notes_9f197c7f083b8d9e.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.9.0/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
</ul>
</section>
<section><a id="a1.8.x_releases"></a>
DOC2MDPLACEHOLDERTOKEN6END<h2>1.8.x releases</h2>
<p>
    BeanUtils <strong>1.8.x</strong> releases are binary compatible with version 1.7.0 and
    require a minimum of JDK 1.3.
  </p>
<ul>
<li>1.8.3

<ul>
<li><a href="assets/files/release-notes_0e990c6fa6343638.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.8.3/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
<li>1.8.2

<ul>
<li><a href="assets/files/release-notes_c6b4e5f5a237332a.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.8.2/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
<li>1.8.1

<ul>
<li><a href="assets/files/release-notes_f171dbf0529e9bb0.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.8.1/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
<li>1.8.0

<ul>
<li><a href="assets/files/release-notes_13c4dd284ef7ae54.txt">Release Notes</a></li>
<li><a href="https://commons.apache.org/beanutils/javadocs/v1.8.0/apidocs/index.html">Javadoc</a></li>
</ul>
</li>
</ul>
</section>
<section><a id="a1.7.0"></a>
DOC2MDPLACEHOLDERTOKEN7END<h2>1.7.0</h2>
<p>
<strong>BeanUtils 1.7.0</strong> is a service release which removes the dependency
upon a specific commons-collection library version. It may be safely used together
with either the 2.x or 3.x series of commons-collections releases.
It also introduces a number of important enhancements. It is backward compatible
with the 1.6 release.
    </p>
<p>
This important service release is intended to help downstream applications solve
dependency issues. The dependency on commons collections (which has become problematic
now that there are two incompatible series of commons collections releases)
has been factored into a separate optional sub-component plus a small number of
stable and mature <code>org.apache.commons.collections</code> packaged classes
(which are distributed with the BeanUtils core). This arrangement means that the
BeanUtils core sub-component (which is the primary dependency for most downsteam
applications) can now be safely included on the same classpath as commons collections
2.x, 3.x or indeed neither.
</p>
<p>
The distribution now contains alternative jar sets. The all-in-one
jar contains all classes. The modular jar set consists of a core jar dependent only
on commons logging and an optional bean collections jar (containing classes that
provide easy and efficient ways to manage collections of beans) which depends on
commons collections 3.
</p>
</section>
<section><a id="Older_Releases_.28Not_Mirrored.29"></a>
DOC2MDPLACEHOLDERTOKEN8END<h2>Older Releases (Not Mirrored)</h2>
<ul>
<li>Version 1.6.1 - 18 Feb 2003
        <a href="https://archive.apache.org/dist/commons/beanutils/binaries/">binary</a> and
        <a href="https://archive.apache.org/dist/commons/beanutils/source/">source</a></li>
<li>Version 1.6 - 21 Jan 2003
        <a href="https://archive.apache.org/dist/commons/beanutils/binaries/">binary</a> and
        <a href="https://archive.apache.org/dist/commons/beanutils/source/">source</a></li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.5/">Version 1.5 </a> - 23 Oct 2002</li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.4.1/">Version 1.4.1</a> - 28 Aug 2002</li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.4/">Version 1.4</a> - 13 Aug 2002</li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.3/">Version 1.3</a> - 29 Apr 2002</li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.2/">Version 1.2</a> - 24 Dec 2001</li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.1/">Version 1.1</a> - 22 Sep 2001</li>
<li><a href="https://archive.apache.org/dist/commons/beanutils/old/v1.0/">Version 1.0</a> - 14 July 2001</li>
</ul>
</section>
</section>
<section><a id="Support"></a>
DOC2MDPLACEHOLDERTOKEN9END<h1>Support</h1>
<p>
    The <a href="https://commons.apache.org/proper/commons-beanutils/mail-lists.html">commons mailing lists</a> act as the main support forum.
    The user list is suitable for most library usage queries.
    The dev list is intended for the development discussion.
    Please remember that the lists are shared between all commons components,
    so prefix your email by [beanutils].
    </p>
<p>
    Issues may be reported via <a href="https://commons.apache.org/proper/commons-beanutils/issue-tracking.html">ASF JIRA</a>.
    </p>
</section>
</td>
</tr>
</table>

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/changes.html -->

<!-- page_index: 2 -->

<a id="changes--apache-commons-beanutils-release-notes"></a>

# Apache Commons BeanUtils Release Notes

<a id="changes--release-history"></a>

## Release History

| Version | Date | Description |
| --- | --- | --- |
| [2.0.0-M2](#changes--a2.0.0-m2) | 2025-05-25 | This is a major release and requires Java 8. |
| [2.0.0-M1](#changes--a2.0.0-m1) | 2024-12-27 | This is a major release and requires Java 8 |
| [1.11.0](#changes--a1.11.0) | 2025-05-25 | This is a maintenance release and requires Java 8. |
| [1.10.1](#changes--a1.10.1) | 2025-01-31 | This is a maintenance release and requires Java 8. |
| [1.10.0](#changes--a1.10.0) | 2024-12-26 | This is a maintenance release and requires Java 8. |
| [1.9.4](#changes--a1.9.4) | 2019-08-13 | The primary reason for this release is a bugfix for CVE-2014-0114. More specifically, our goal with BEANUTILS-520 is to set the default behavior of the BeanUtilsBean to not allow class level access. The goal in doing this now is to bring 1.9.X into alignment with the same behavior of the 2.X version line in regards to security. If one would like to opt out of the default behavior, one could follow the example set out in the test class available in src/test/java/org/apache/commons/beanutils/bugs/Jira520TestCase.java. |
| [1.9.3](#changes--a1.9.3) | 2016-09-21 | Bug fix release, now builds with Java 8 |
| [1.9.2](#changes--a1.9.2) | 2014-05-29 | Added a new BeanIntrospector for addressing a potential class loader vulnerability |
| [1.9.1](#changes--a1.9.1) | 2014-01-11 | Bug fix for 1.9.0 |
| [1.9.0](#changes--a1.9.0) | 2013-12-11 | Upgrade to Java 5 including generics where possible |
| [1.8.3](#changes--a1.8.3) | 2010-03-28 | Bug fix for 1.8.2 |
| [1.8.2](#changes--a1.8.2) | 2009-11-13 | Bug fix for 1.8.1 |
| [1.8.1](#changes--a1.8.1) | 2009-10-20 | Bug fixes for 1.8.0 |
| [1.8.0](#changes--a1.8.0) | 2008-09-01 | Converter improvements, Plugable expression Resolver and bug fixes for 1.7.0 |
| [1.8.0-BETA](#changes--a1.8.0-beta) | 2007-08-04 | Trial Beta release |
| [1.7.0](#changes--a1.7.0) | 2004-08-02 |  |
| [1.6.1](#changes--a1.6.1) | 2003-02-18 |  |
| [1.6](#changes--a1.6) | 2003-01-21 |  |
| [1.5](#changes--a1.5) | 2002-10-23 |  |
| [1.4.1](#changes--a1.4.1) | 2002-08-28 |  |
| [1.4](#changes--a1.4) | 2002-08-13 |  |
| [1.3](#changes--a1.3) | 2002-04-29 |  |
| [1.2](#changes--a1.2) | 2001-12-24 |  |
| [1.1](#changes--a1.1) | 2001-09-22 |  |
| [1.0](#changes--a1.0) | 2001-07-14 | Initial Release |

<a id="changes--release-2.0.0-m2-2025-05-25"></a>

## Release 2.0.0-M2 – 2025-05-25

| Type | Changes | By |
| --- | --- | --- |
| Fix | Javadoc is missing its Overview page. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.PropertyUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.PropertyUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.locale.LocaleConvertUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.locale.LocaleConvertUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.locale.LocaleBeanUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.locale.LocaleBeanUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.MethodUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.MethodUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.ConvertUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.ConvertUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.ConstructorUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.ConstructorUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class LocaleBeanUtils no longer extends BeanUtils (both classes only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The class org.apache.commons.beanutils2.BeanUtils is now final (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | The constructor org.apache.commons.beanutils2.BeanUtils is now private (the class only contains static methods). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | BeanComparator.compare(T, T) now throws IllegalArgumentException instead of RuntimeException to wrap all cases of ReflectiveOperationException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | MappedMethodReference.get() now throws IllegalStateException instead of RuntimeException to wrap cases of NoSuchMethodException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.get(String) now throws IllegalArgumentException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.hasNext() now throws IllegalStateException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.next() now throws IllegalStateException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.set(String, Object) now throws IllegalArgumentException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.set(String, String, Object) now throws IllegalArgumentException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add org.apache.commons.beanutils.SuppressPropertiesBeanIntrospector.SUPPRESS\_DECLARING\_CLASS. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 78 to 84 #348. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.3.4 to 1.3.5. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-collections4 from 4.5.0-M3 to 4.5.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-2.0.0-m1-2024-12-27"></a>

## Release 2.0.0-M1 – 2024-12-27

| Type | Changes | By |
| --- | --- | --- |
| Update | Change packaging from org.apache.commons.beanutils to org.apache.commons.beanutils2. Fixes [BEANUTILS-503](https://issues.apache.org/jira/browse/BEANUTILS-503). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Double-Checked Locking anti pattern in WeakFastHashMap. Fixes [BEANUTILS-402](https://issues.apache.org/jira/browse/BEANUTILS-402). Thanks to Melloware. | [melloware](#team--melloware) |
| Update | Add missing serialVersionUID to Serializable classes. Fixes [BEANUTILS-505](https://issues.apache.org/jira/browse/BEANUTILS-505). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Add Automatic-Module-Name entry to MANIFEST.MF. Fixes [BEANUTILS-512](https://issues.apache.org/jira/browse/BEANUTILS-512). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Remove deprecated code for 2.0.0. Fixes [BEANUTILS-514](https://issues.apache.org/jira/browse/BEANUTILS-514). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | WeakHashmap enters into infinite loop in WrapDynaClass.java. Fixes [BEANUTILS-509](https://issues.apache.org/jira/browse/BEANUTILS-509). Thanks to sunil, Akshay Gehi. | [ggregory](#team--ggregory) |
| Update | BeanUtils2 mitigate CVE-2014-0114. Fixes [BEANUTILS-520](https://issues.apache.org/jira/browse/BEANUTILS-520). Thanks to Melloware. | [ggregory](#team--ggregory) |
| Update | Convert Collections4 to java.util.function. #8. Fixes [BEANUTILS-527](https://issues.apache.org/jira/browse/BEANUTILS-527). Thanks to Melloware, Matt Sicker, Gary Gregory. | [ggregory](#team--ggregory) |
| Remove | Removed Commons Collections dependency. #8. Fixes [BEANUTILS-527](https://issues.apache.org/jira/browse/BEANUTILS-527). Thanks to Melloware, Matt Sicker, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | New converters for UUID, URI, and Path #10. Fixes [BEANUTILS-528](https://issues.apache.org/jira/browse/BEANUTILS-528). Thanks to Melloware, Matt Sicker, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | New converters for Java 8 Time classes #13. Fixes [BEANUTILS-530](https://issues.apache.org/jira/browse/BEANUTILS-530). Thanks to Melloware, Matt Sicker, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Log at the debug level instead of info. Fixes [BEANUTILS-529](https://issues.apache.org/jira/browse/BEANUTILS-529). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Fix typos; fix error in Javadoc; performance fix; fix code smells #25. Fixes [BEANUTILS-537](https://issues.apache.org/jira/browse/BEANUTILS-537). Thanks to XenoAmess, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Refactor logger usage #72. Thanks to Andrei Korzhevskii, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Migrate to JUnit 5 #93, #283, #284, #285, #287. Thanks to SethFalco, Steve Bosman, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: org.apache.commons.beanutils2.BasicDynaClass.constructorTypes should be both final and package protected [org.apache.commons.beanutils2.BasicDynaClass] At BasicDynaClass.java:[line 95] MS\_FINAL\_PKGPROTECT. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: Load of known null value in org.apache.commons.beanutils2.converters.AbstractConverter.convert(Class, Object) [org.apache.commons.beanutils2.converters.AbstractConverter] At AbstractConverter.java:[line 163] NP\_LOAD\_OF\_KNOWN\_NULL\_VALUE. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: Unused public or protected field: org.apache.commons.beanutils2.WrapDynaClass.descriptors [org.apache.commons.beanutils2.WrapDynaClass] In WrapDynaClass.java UUF\_UNUSED\_PUBLIC\_OR\_PROTECTED\_FIELD. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: org.apache.commons.beanutils2.converters.ArrayConverter.setAllowedChars(char[]) may expose internal representation by storing an externally mutable object into ArrayConverter.allowedChars [org.apache.commons.beanutils2.converters.ArrayConverter] At ArrayConverter.java:[line 202] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: org.apache.commons.beanutils2.converters.DateTimeConverter.setPatterns(String[]) may expose internal representation by storing an externally mutable object into DateTimeConverter.patterns [org.apache.commons.beanutils2.converters.DateTimeConverter] At DateTimeConverter.java:[line 204] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: org.apache.commons.beanutils2.ConversionException.getCause() may expose internal representation by returning ConversionException.cause [org.apache.commons.beanutils2.ConversionException] At ConversionException.java:[line 83] EI\_EXPOSE\_REP. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: new org.apache.commons.beanutils2.ConversionException(String, Throwable) may expose internal representation by storing an externally mutable object into ConversionException.cause [org.apache.commons.beanutils2.ConversionException] At ConversionException.java:[line 53] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: new org.apache.commons.beanutils2.ConversionException(Throwable) may expose internal representation by storing an externally mutable object into ConversionException.cause [org.apache.commons.beanutils2.ConversionException] At ConversionException.java:[line 65] EI\_EXPOSE\_REP2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: org.apache.commons.beanutils2.converters.DateTimeConverter.getPatterns() may expose internal representation by returning DateTimeConverter.patterns [org.apache.commons.beanutils2.converters.DateTimeConverter] At DateTimeConverter.java:[line 189] EI\_EXPOSE\_REP. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix SpotBugs [ERROR] Medium: org.apache.commons.beanutils2.WrapDynaClass.getDynaProperties() may expose internal representation by returning WrapDynaClass.properties [org.apache.commons.beanutils2.WrapDynaClass] At WrapDynaClass.java:[line 172] EI\_EXPOSE\_REP. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Replace Commons Collections Test Framework 3.2.2 with 4.5.0-M3 #40. Thanks to Melloware, sebbASF, Gary Gregory, Michal Landsman. | [ggregory](#team--ggregory) |
| Fix | Provide error index in ConversionException message in DateTimeConverter.parse(Class, Class, String, DateFormat). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Avoid possible NPE in DateTimeConverter.parse(Class, Class, String). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Annotate Converter with @FunctionalInterface. Thanks to Claude Warren, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix JDK 21 CI failure due to locale changes #201. Fixes [BEANUTILS-564](https://issues.apache.org/jira/browse/BEANUTILS-564). Thanks to SingingBush. | [ggregory](#team--ggregory) |
| Fix | Fix warnings and To-Dos #92. Thanks to Seth Falco. | [ggregory](#team--ggregory) |
| Fix | Replace internal use of Locale.ENGLISH with Locale.ROOT. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | FluentPropertyBeanIntrospector caches corrupted writeMethod (2.x) #68. Fixes [BEANUTILS-541](https://issues.apache.org/jira/browse/BEANUTILS-541). Thanks to Sergey Chernov. | [ggregory](#team--ggregory) |
| Add | New converter for Enum. Fixes [BEANUTILS-346](https://issues.apache.org/jira/browse/BEANUTILS-346). Thanks to Melloware. | [melloware](#team--melloware) |
| Add | Add github/codeql-action #118. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add and use ConversionException.format(String, Object...). Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add Converters for additional types: Color, Dimension, InetAddress, Locale, Pattern, Point #47. Thanks to Seth Falco, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Make PropertyUtilsBean.getReadMethod(Class, PropertyDescriptor) public #232. Thanks to Sergey Chernov, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from 2 to 3.0.11 #77, #89, #103, #111. #137, #141. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update actions/checkout from 2.3.1 to 3.0.2 #33, #108. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update actions/setup-java from 1.4.0 to 3.6.0 #35, #114, #144. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/upload-artifact from 3.1.0 to 3.1.1 #143. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Collections from 4.3 to 4.4. Fixes [BEANUTILS-522](https://issues.apache.org/jira/browse/BEANUTILS-522). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Java from 6 to 7. Fixes [BEANUTILS-504](https://issues.apache.org/jira/browse/BEANUTILS-504). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Java from 7 to 8. Fixes [BEANUTILS-515](https://issues.apache.org/jira/browse/BEANUTILS-515). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump junit-jupiter from 5.7.2 to 5.9.1 #113, #126, #134. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump JUnit from 4 to 5.9.1 vintage, #78, #112, #127, #136. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump Jacoco from 0.8.4 to 0.8.8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump JApiCmp from 0.12.0 to 0.17.1, #46, #110, #130, #146. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-surefire-plugin from 2.22.1 to 3.0.0-M7, #116, #122. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.0.0 to 3.2.0, #76, #129. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump maven-pmd-plugin from 3.12.0 to 3.19.0, #120, #128, #131. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump BC version from 1.9.3 to 1.9.4. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 50 to 74 #229, #245, #254, #264, #274, #279. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump biz.aQute.bndlib from 5.1.0 to 6.4.1 #29, #45, #79, #109, #119, #121, #147, #175. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Jacoco 0.8.6 for JDK15 support #55. Thanks to melloware. | [ggregory](#team--ggregory) |
| Update | Updated URLConverterTestCase to run without Internet access #50. Thanks to SethFalco. | [ggregory](#team--ggregory) |
| Update | Don't initialize variables to defaults #71. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.5.3.0 to 4.6.0.0. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs from 4.5.3 to 4.6.0. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-lang3 from 3.12.0 to 3.17.0 #263, #269, #280. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.2 to 1.3.4 #226, #246, #259, #275. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 74 to 78 #291, #295, #299, #306. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Remove | Removed BeanUtilsBean2, use BeanUtilsBean. BeanUtilsBean2 functionality is now in BeanUtilsBean. Previous BeanUtilsBean functionality for those methods is no longer supported. Thanks to Gary Gregory, Niall Pemberton. | [ggregory](#team--ggregory) |
| Remove | Removed ConvertUtilsBean2, use ConvertUtilsBean. ConvertUtilsBean2 functionality is now in ConvertUtilsBean. Previous ConvertUtilsBean functionality for those methods is no longer supported. Thanks to Gary Gregory, Niall Pemberton. | [ggregory](#team--ggregory) |
| Remove | Do not implement Serializable. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.11.0-2025-05-25"></a>

## Release 1.11.0 – 2025-05-25

| Type | Changes | By |
| --- | --- | --- |
| Fix | BeanComparator.compare(T, T) now throws IllegalArgumentException instead of RuntimeException to wrap all cases of ReflectiveOperationException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | MappedMethodReference.get() now throws IllegalStateException instead of RuntimeException to wrap cases of NoSuchMethodException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.get(String) now throws IllegalArgumentException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.hasNext() now throws IllegalStateException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.next() now throws IllegalStateException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.set(String, Object) now throws IllegalArgumentException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ResultSetIterator.set(String, String, Object) now throws IllegalArgumentException instead of RuntimeException to wrap cases of SQLException. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add org.apache.commons.beanutils.SuppressPropertiesBeanIntrospector.SUPPRESS\_DECLARING\_CLASS. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 81 to 84. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.3.4 to 1.3.5. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.10.1-2025-01-31"></a>

## Release 1.10.1 – 2025-01-31

| Type | Changes | By |
| --- | --- | --- |
| Fix | FluentPropertyBeanIntrospector concurrency issue (backport to 1.X) #325. Fixes [BEANUTILS-541](https://issues.apache.org/jira/browse/BEANUTILS-541). Thanks to Sergey Chernov. | [ggregory](#team--ggregory) |
| Fix | Javadoc is missing its Overview page. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate BeanUtils.BeanUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate ConstructorUtils.ConstructorUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate LocaleBeanUtils.LocaleBeanUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate LocaleConvertUtils.LocaleConvertUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate ConvertUtils.ConvertUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate MethodUtils.MethodUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate PropertyUtils.PropertyUtils(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 78 to 81. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.10.0-2024-12-26"></a>

## Release 1.10.0 – 2024-12-26

| Type | Changes | By |
| --- | --- | --- |
| Fix | FluentPropertyBeanIntrospector caches corrupted writeMethod (backport to 1.x) #69. Fixes [BEANUTILS-541](https://issues.apache.org/jira/browse/BEANUTILS-541). Thanks to Sergey Chernov. | [ggregory](#team--ggregory) |
| Fix | Replace internal use of Locale.ENGLISH with Locale.ROOT. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Replace Maven CLIRR plugin with JApiCmp. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Port to Java 1.4 Throwable APIs (!). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix Javadoc generation on Java 8, 17, and 21. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | AbstractArrayConverter.parseElements(String) now returns a List<String> instead of a raw List. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 47 to 78. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Java requirement from Java 6 to 8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump junit:junit from 4.12 to 4.13.2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump JUnit from 4.x to 5.x "vintage". Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.2 to 1.3.4. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Deprecate BeanUtilsBean.initCause(Throwable, Throwable) for removal, use Throwable.initCause(Throwable). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Deprecate BeanUtils.initCause(Throwable, Throwable) for removal, use Throwable.initCause(Throwable). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.9.4-2019-08-13"></a>

## Release 1.9.4 – 2019-08-13

| Type | Changes | By |
| --- | --- | --- |
| Fix | BeanUtils mitigation of CVE-2014-0114. (CVE-2019-10086 for commons-beanutils). Fixes [BEANUTILS-520](https://issues.apache.org/jira/browse/BEANUTILS-520). Thanks to Melloware. | [chtompki](#team--chtompki) |

<a id="changes--release-1.9.3-2016-09-21"></a>

## Release 1.9.3 – 2016-09-21

| Type | Changes | By |
| --- | --- | --- |
| Update | Update dependency from JUnit 3.8.1 to 4.12. Fixes [BEANUTILS-433](https://issues.apache.org/jira/browse/BEANUTILS-433). Thanks to Benedikt Ritter, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Indexed List Setters no longer work. Fixes [BEANUTILS-465](https://issues.apache.org/jira/browse/BEANUTILS-465). Thanks to Daniel Atallah. | [oheger](#team--oheger) |
| Update | Update commons-logging from 1.1.1 to 1.2. Fixes [BEANUTILS-469](https://issues.apache.org/jira/browse/BEANUTILS-469). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Precision lost when converting BigDecimal. Fixes [BEANUTILS-470](https://issues.apache.org/jira/browse/BEANUTILS-470). Thanks to Tommy Tynjä. | [oheger](#team--oheger) |
| Update | FluentPropertyBeanIntrospector does not use the same naming algorithm as DefaultBeanIntrospector. Fixes [BEANUTILS-474](https://issues.apache.org/jira/browse/BEANUTILS-474). Thanks to Michael Grove. | [ggregory](#team--ggregory) |
| Fix | Changed log level of warnings from FluentPropertyBeanIntrospector; exceptions are no longer logged with level WARN. Fixes [BEANUTILS-477](https://issues.apache.org/jira/browse/BEANUTILS-477). | [oheger](#team--oheger) |
| Update | Update commons-collections from 3.2.1 to 3.2.2. (CVE-2015-4852). Fixes [BEANUTILS-482](https://issues.apache.org/jira/browse/BEANUTILS-482). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update Java requirement from Java 5 to 6. Fixes [BEANUTILS-490](https://issues.apache.org/jira/browse/BEANUTILS-490). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | IndexedPropertyDescriptor not supported for List in Java 8. Fixes [BEANUTILS-492](https://issues.apache.org/jira/browse/BEANUTILS-492). Thanks to Stian Soiland-Reyes. | [stain](#team--stain) |
| Fix | Exception when setting indexed properties: "Default conversion to ArrayList failed". Fixes [BEANUTILS-493](https://issues.apache.org/jira/browse/BEANUTILS-493). Thanks to Bernhard Seebass. | [stain](#team--stain) |
| Update | DateConverterTestBase fails on M/d/yy in Java 9. Fixes [BEANUTILS-495](https://issues.apache.org/jira/browse/BEANUTILS-495). Thanks to Stian Soiland-Reyes. | [stain](#team--stain) |
| Update | testGetDescriptorInvalidBoolean fails on Java 9. Fixes [BEANUTILS-496](https://issues.apache.org/jira/browse/BEANUTILS-496). Thanks to Stian Soiland-Reyes. | [stain](#team--stain) |

<a id="changes--release-1.9.2-2014-05-29"></a>

## Release 1.9.2 – 2014-05-29

| Type | Changes | By |
| --- | --- | --- |
| Add | Class loader vulnerability in DefaultResolver (). Fixes [BEANUTILS-463](https://issues.apache.org/jira/browse/BEANUTILS-463). | [oheger](#team--oheger) |
| Fix | BaseLocaleConverter.checkConversionResult() fails with ConversionException when result is null when it should not. Fixes [BEANUTILS-458](https://issues.apache.org/jira/browse/BEANUTILS-458). Thanks to Manuel Dominguez Sarmiento. | [oheger](#team--oheger) |

<a id="changes--release-1.9.1-2014-01-11"></a>

## Release 1.9.1 – 2014-01-11

| Type | Changes | By |
| --- | --- | --- |
| Fix | Write methods for PropertyDescriptors created during custom introspection are lost. Fixes [BEANUTILS-456](https://issues.apache.org/jira/browse/BEANUTILS-456). | [oheger](#team--oheger) |

<a id="changes--release-1.9.0-2013-12-11"></a>

## Release 1.9.0 – 2013-12-11

| Type | Changes | By |
| --- | --- | --- |
| Add | WrapDynaBeans always use the default PropertyUtilsBean instance. Fixes [BEANUTILS-455](https://issues.apache.org/jira/browse/BEANUTILS-455). | [oheger](#team--oheger) |
| Update | BeanUtilsBean.copyProperties() throws conversion exception for null Date. Fixes [BEANUTILS-454](https://issues.apache.org/jira/browse/BEANUTILS-454). | [oheger](#team--oheger) |
| Update | Add generics. Fixes [BEANUTILS-452](https://issues.apache.org/jira/browse/BEANUTILS-452). | [oheger](#team--oheger) |
| Update | LocaleConverters do not take the target type into account. Fixes [BEANUTILS-449](https://issues.apache.org/jira/browse/BEANUTILS-449). | [oheger](#team--oheger) |
| Update | LocaleConverters do not check their default value. Fixes [BEANUTILS-448](https://issues.apache.org/jira/browse/BEANUTILS-448). | [oheger](#team--oheger) |
| Update | LazyDynaList.toArray() is not conform to the contract defined by the Collection interface. Fixes [BEANUTILS-447](https://issues.apache.org/jira/browse/BEANUTILS-447). | [oheger](#team--oheger) |
| Update | Some of the converters ignore the passed in target type. Fixes [BEANUTILS-446](https://issues.apache.org/jira/browse/BEANUTILS-446). | [oheger](#team--oheger) |
| Update | Converters can return an invalid result object if a default value is set. Fixes [BEANUTILS-445](https://issues.apache.org/jira/browse/BEANUTILS-445). | [oheger](#team--oheger) |
| Update | Replace UnmodifiableSet.decorate with Collections.unModifiableSet. Fixes [BEANUTILS-441](https://issues.apache.org/jira/browse/BEANUTILS-441). Thanks to Samir Kerroumi. | [oheger](#team--oheger) |
| Update | Replace package.html with package-info.java. Fixes [BEANUTILS-436](https://issues.apache.org/jira/browse/BEANUTILS-436). | [britter](#team--britter) |
| Update | Add @Deprecated and @Override Annotations. Fixes [BEANUTILS-438](https://issues.apache.org/jira/browse/BEANUTILS-438). | [britter](#team--britter) |
| Update | Replace Date and Revision SVN keywords with Id. Fixes [BEANUTILS-437](https://issues.apache.org/jira/browse/BEANUTILS-437). | [britter](#team--britter) |
| Update | Remove @author tags and move missing authors to pom.xml. Fixes [BEANUTILS-431](https://issues.apache.org/jira/browse/BEANUTILS-431). | [britter](#team--britter) |
| Update | Switch to Java 1.5. Fixes [BEANUTILS-432](https://issues.apache.org/jira/browse/BEANUTILS-432). | [britter](#team--britter) |
| Add | Provide a BeanIntrospector implementation which supports properties in a fluent API. Fixes [BEANUTILS-428](https://issues.apache.org/jira/browse/BEANUTILS-428). | [oheger](#team--oheger) |
| Add | Support customization of introspection mechanism. Fixes [BEANUTILS-425](https://issues.apache.org/jira/browse/BEANUTILS-425). | [oheger](#team--oheger) |
| Fix | BeanUtilsBean.setProperty throws IllegalArgumentException if getter of nested property returns null. Fixes [BEANUTILS-411](https://issues.apache.org/jira/browse/BEANUTILS-411). Thanks to Marcus Zander. | [britter](#team--britter) |
| Update | Delete trailing white spaces and white spaces on empty lines from all files. Fixes [BEANUTILS-429](https://issues.apache.org/jira/browse/BEANUTILS-429). | [britter](#team--britter) |
| Update | Configure Checkstyle to check for trailing white spaces and white spaces on empty lines. Fixes [BEANUTILS-427](https://issues.apache.org/jira/browse/BEANUTILS-427). | [britter](#team--britter) |
| Fix | MethodUtils.invokeMethod() throws NullPointerException when args==null. Fixes [BEANUTILS-408](https://issues.apache.org/jira/browse/BEANUTILS-408). | [britter](#team--britter) |
| Fix | ConstructorUtils.invokeConstructor(Class klass, Object arg) throws NullPointerException when arg==null. Fixes [BEANUTILS-426](https://issues.apache.org/jira/browse/BEANUTILS-426). | [britter](#team--britter) |
| Fix | BeanMap methods should initialize the root cause of exceptions that are thrown when running on JDK 1.4+. Fixes [BEANUTILS-380](https://issues.apache.org/jira/browse/BEANUTILS-380). Thanks to Brendan Nolan. | [niallp](#team--niallp) |
| Fix | Remove copied Collection classes. Fixes [BEANUTILS-379](https://issues.apache.org/jira/browse/BEANUTILS-379). | [niallp](#team--niallp) |
| Fix | BeanMap does not work in osgi (fixed by BEANUTILS-379). Fixes [BEANUTILS-378](https://issues.apache.org/jira/browse/BEANUTILS-378). Thanks to Christian Schneider. | [niallp](#team--niallp) |
| Fix | MethodUtils getMatchingAccessibleMethod() does not correctly handle inheritance and method overloading. Fixes [BEANUTILS-381](https://issues.apache.org/jira/browse/BEANUTILS-381). Thanks to Todd Nine. | [niallp](#team--niallp) |

<a id="changes--release-1.8.3-2010-03-28"></a>

## Release 1.8.3 – 2010-03-28

| Type | Changes | By |
| --- | --- | --- |
| Fix | MethodUtils is not thread safe because WeakFastHashMap which uses WeakHashMap is not thread-safe (duplicate of BEANUTILS-318 which was not fixed properly in BeanUtils 1.8.0). Fixes [BEANUTILS-373](https://issues.apache.org/jira/browse/BEANUTILS-373). Thanks to Andrew Sunde. | [niallp](#team--niallp) |
| Fix | Add constructors which have useColumnLabel parameter to ResultSetDynaClass and RowSetDynaClass. Fixes [BEANUTILS-371](https://issues.apache.org/jira/browse/BEANUTILS-371). Thanks to David Tonhofer. | [niallp](#team--niallp) |

<a id="changes--release-1.8.2-2009-11-13"></a>

## Release 1.8.2 – 2009-11-13

| Type | Changes | By |
| --- | --- | --- |
| Fix | NullPointerException in BeanUtilsBean .setProperty(). Fixes [BEANUTILS-368](https://issues.apache.org/jira/browse/BEANUTILS-368). Thanks to Peter Fassev. | [niallp](#team--niallp) |

<a id="changes--release-1.8.1-2009-10-20"></a>

## Release 1.8.1 – 2009-10-20

| Type | Changes | By |
| --- | --- | --- |
| Fix | NPE in LazyDynaList. Fixes [BEANUTILS-300](https://issues.apache.org/jira/browse/BEANUTILS-300). Thanks to Henri and Sebb. | [niallp](#team--niallp) |
| Fix | JDBCDynaClass throws class not found exception under java6. Fixes [BEANUTILS-327](https://issues.apache.org/jira/browse/BEANUTILS-327). Thanks to Sascha Riemann. | [niallp](#team--niallp) |
| Fix | MappedPropertyDescriptor#reLoadClass() possible NPE / odd code; also swallows Throwable. Fixes [BEANUTILS-336](https://issues.apache.org/jira/browse/BEANUTILS-336). Thanks to Sebb. | [niallp](#team--niallp) |
| Fix | BeanUtilsBean.setProperty throws IllegalArgumentException if value is null. Fixes [BEANUTILS-339](https://issues.apache.org/jira/browse/BEANUTILS-339). Thanks to Alan Escreet. | [niallp](#team--niallp) |
| Fix | BeanUtilsBean.setProperty does not handle some kind of nested properties. Fixes [BEANUTILS-345](https://issues.apache.org/jira/browse/BEANUTILS-345). Thanks to Simone Riccucci. | [niallp](#team--niallp) |
| Fix | MappedPropertyDescriptor throws an exception after method reference has been garbage collected. Fixes [BEANUTILS-347](https://issues.apache.org/jira/browse/BEANUTILS-347). Thanks to Eickvonder. | [niallp](#team--niallp) |
| Fix | copyProperties throws NullPointerException if an IllegalArgumentException is thrown due to a null value parameter for a primitive. Fixes [BEANUTILS-349](https://issues.apache.org/jira/browse/BEANUTILS-349). Thanks to Eivind Tagseth. | [niallp](#team--niallp) |
| Fix | FloatLocaleConverter cannot parse 0. Fixes [BEANUTILS-351](https://issues.apache.org/jira/browse/BEANUTILS-351). Thanks to Lucian Chirita. | [niallp](#team--niallp) |
| Fix | Type in BooleanConverter: "Cna't convert value". Fixes [BEANUTILS-354](https://issues.apache.org/jira/browse/BEANUTILS-354). Thanks to Anders Wallgren. | [niallp](#team--niallp) |
| Update | Avoid calling setAccessible() if not needed. Fixes [BEANUTILS-333](https://issues.apache.org/jira/browse/BEANUTILS-333). Thanks to Lukasz Lenart. | [niallp](#team--niallp) |
| Update | Method createDynaProperty of JDBCDynaClass should first look for column label instead of column name in ResultSetMetadata object.. Fixes [BEANUTILS-344](https://issues.apache.org/jira/browse/BEANUTILS-344). Thanks to Viral. | [niallp](#team--niallp) |
| Update | change visibility of method "evaluateValue" belongs to the class BeanPropertyValueEqualsPredicate to "protected". Fixes [BEANUTILS-350](https://issues.apache.org/jira/browse/BEANUTILS-350). Thanks to rodrigo hernandez. | [niallp](#team--niallp) |

<a id="changes--release-1.8.0-2008-09-01"></a>

## Release 1.8.0 – 2008-09-01

| Type | Changes | By |
| --- | --- | --- |
| Fix | Allow access to non public class's public methods from a public sub-classes. Fixes [BEANUTILS-265](https://issues.apache.org/jira/browse/BEANUTILS-265). Thanks to Tom Schindl and Romain Muller. | [niallp](#team--niallp) |
| Fix | Circular Reference on WeakHashMap. Fixes [BEANUTILS-291](https://issues.apache.org/jira/browse/BEANUTILS-291). Thanks to Clebert Suconic. | [niallp](#team--niallp) |
| Fix | BeanUtilsBean.setProperty() does not support nested map. Fixes [BEANUTILS-294](https://issues.apache.org/jira/browse/BEANUTILS-294). Thanks to Stephen Leung. | [niallp](#team--niallp) |
| Fix | Unnecessary Garbage Objects in Class PropertyUtilsBean. Fixes [BEANUTILS-295](https://issues.apache.org/jira/browse/BEANUTILS-295). Thanks to Stefan Wohlgemuth. | [bayard](#team--bayard) |
| Fix | ConvertingWrapDynaBean hides cause exceptions. Fixes [BEANUTILS-297](https://issues.apache.org/jira/browse/BEANUTILS-297). Thanks to Alex Tkachev. | [niallp](#team--niallp) |
| Fix | MethodUtils.getAccessibleMethod(Method method) could not find right public method. Fixes [BEANUTILS-298](https://issues.apache.org/jira/browse/BEANUTILS-298). Thanks to Roman Mukhin. | [niallp](#team--niallp) |
| Fix | NPE in ArrayConverter when converting a non-quoted string with underscores to a string array. Fixes [BEANUTILS-302](https://issues.apache.org/jira/browse/BEANUTILS-302). Thanks to Martin Bartlett. | [niallp](#team--niallp) |
| Fix | LocaleConvertUtilsBean.convert throws NPE on null Locale when debug logging is enabled. Fixes [BEANUTILS-306](https://issues.apache.org/jira/browse/BEANUTILS-306). Thanks to Lucian Chirita. | [niallp](#team--niallp) |
| Fix | Fix WeakHashMap is not thread safe in MethodUtils using new FastWeakHashMap. Fixes [BEANUTILS-318](https://issues.apache.org/jira/browse/BEANUTILS-318). Thanks to Sylvain Legault. | [niallp](#team--niallp) |
| Fix | PropertyUtils.getPropertyType fails for DynaBeans contained within a normal bean. Fixes [BEANUTILS-319](https://issues.apache.org/jira/browse/BEANUTILS-319). Thanks to Erik Erskine. | [niallp](#team--niallp) |
| Fix | Iterating by a Map' key/value pairs in BeanUtilsBean and PropertyUtilsBean. Fixes [BEANUTILS-326](https://issues.apache.org/jira/browse/BEANUTILS-326). Thanks to Vladimir Orlov. | [niallp](#team--niallp) |

<a id="changes--release-1.8.0-beta-2007-08-04"></a>

## Release 1.8.0-BETA – 2007-08-04

| Type | Changes | By |
| --- | --- | --- |
| Add | Add plugable property name expression Resolver. Fixes [BEANUTILS-259](https://issues.apache.org/jira/browse/BEANUTILS-259). | [niallp](#team--niallp) |
| Update | General Converter implementation improvements: New AbstractConverter which provides a basic structure for Converter implementations and new NumberConverter implementation. Fixes [BEANUTILS-258](https://issues.apache.org/jira/browse/BEANUTILS-258). | [niallp](#team--niallp) |
| Add | Add new generic ArrayConverter implementation. Fixes [BEANUTILS-242](https://issues.apache.org/jira/browse/BEANUTILS-242). | [niallp](#team--niallp) |
| Add | Add new generic DateTimeConverter implementation. Fixes [BEANUTILS-255](https://issues.apache.org/jira/browse/BEANUTILS-255). | [niallp](#team--niallp) |
| Update | Better implementation of SqlDateConverter. Modified SqlDateConverter, SqlTimeConverter and SqlTimestampConverter to accept java.util.Date and Calendar object instances. Added tests. Fixes [BEANUTILS-239](https://issues.apache.org/jira/browse/BEANUTILS-239). Thanks to Rafael Afonso. | [vgritsenko](#team--vgritsenko) |
| Add | New Facade converter implementation - hide non-Converter public APIs. Fixes [BEANUTILS-286](https://issues.apache.org/jira/browse/BEANUTILS-286). | [niallp](#team--niallp) |
| Update | Add "t/f" to BooleanConverter. Fixes [BEANUTILS-229](https://issues.apache.org/jira/browse/BEANUTILS-229). | [skitching](#team--skitching) |
| Update | Support Mapped property inside a mapped property. Fixes [BEANUTILS-43](https://issues.apache.org/jira/browse/BEANUTILS-43). Thanks to Firepica and Thomas Jacob. | [niallp](#team--niallp) |
| Update | Support Indexed property inside a mapped property. Fixes [BEANUTILS-113](https://issues.apache.org/jira/browse/BEANUTILS-113). Thanks to Firepica and Ludwig Wensauer. | [niallp](#team--niallp) |
| Update | Support Arrays with multiple dimension. Fixes [BEANUTILS-247](https://issues.apache.org/jira/browse/BEANUTILS-247). Thanks to Christian Poitras, Thomas Jacob and scott sadlo. | [niallp](#team--niallp) |
| Update | Include bean class in the message of PropertyUtilsBean exceptions. Fixes [BEANUTILS-207](https://issues.apache.org/jira/browse/BEANUTILS-207). Thanks to Erik Meade. | [bayard](#team--bayard) |
| Update | Provide better error message for "argument type mismatch". Fixes [BEANUTILS-224](https://issues.apache.org/jira/browse/BEANUTILS-224). Thanks to Ralf Hauser. | [bayard](#team--bayard) |
| Update | Improved messages for unknown properties. Fixes [BEANUTILS-30](https://issues.apache.org/jira/browse/BEANUTILS-30). Thanks to Barry Kaplan. | [bayard](#team--bayard) |
| Update | MethodUtils.invoke for static methods. Fixes [BEANUTILS-193](https://issues.apache.org/jira/browse/BEANUTILS-193). Thanks to Nestor Boscan. | [bayard](#team--bayard) |
| Update | Log or throw exception in PropertyUtilsBean. Added mechanism to initialize the "cause" on an Exception using reflection for JDK 1.4+ (copied from Commons HttpClient). Fixes [BEANUTILS-266](https://issues.apache.org/jira/browse/BEANUTILS-266). Thanks to Brian Ewins and Commons HttpClient. | [niallp](#team--niallp) |
| Add | Add lazyDynaList. Thanks to Vic Cekvenich. | [niallp](#team--niallp) |
| Add | Provide a Map decorator for a DynaBean (enables DynaBean to be used with other teechnologies such as JSTL). Fixes [BEANUTILS-185](https://issues.apache.org/jira/browse/BEANUTILS-185). Thanks to Gabriel Belingueres. | [niallp](#team--niallp) |
| Update | Implement equals() and hashCode() methods for DynaProperty. Fixes [BEANUTILS-233](https://issues.apache.org/jira/browse/BEANUTILS-233). Thanks to Russell. | [niallp](#team--niallp) |
| Fix | BeanUtils's tests fail to compile under JDK 1.6. Fixes [BEANUTILS-243](https://issues.apache.org/jira/browse/BEANUTILS-243). Thanks to Henri Yandell. | [niallp](#team--niallp) |
| Fix | Lock in BeanUtilsBean.getInstance(. Fixes [BEANUTILS-49](https://issues.apache.org/jira/browse/BEANUTILS-49). Thanks to Jesper Richter-Reichhelm. | [niallp](#team--niallp) |
| Fix | Beanutils's describe() method cannot determine reader methods for anonymous class. Fixes [BEANUTILS-157](https://issues.apache.org/jira/browse/BEANUTILS-157). Thanks to Thorbjorn Ravn Andersen. | [niallp](#team--niallp) |
| Fix | Added warning about describe behavior to the javadocs. Fixes [BEANUTILS-158](https://issues.apache.org/jira/browse/BEANUTILS-158). | [rdonkin](#team--rdonkin) |
| Fix | BeanUtilsBean's setProperty() does not convert objects using custom converters properly. Fixes [BEANUTILS-249](https://issues.apache.org/jira/browse/BEANUTILS-249). Thanks to Brad. | [niallp](#team--niallp) |
| Fix | Fix javadoc - IllegalArgumentException in BeanUtils.copyProperties when property types don't match. Fixes [BEANUTILS-17](https://issues.apache.org/jira/browse/BEANUTILS-17). Thanks to Matthew Sgarlata and Corey Scott. | [niallp](#team--niallp) |
| Fix | Writing to a mapped property requires a setter for a map, but never uses it. Fixes [BEANUTILS-68](https://issues.apache.org/jira/browse/BEANUTILS-68). Thanks to Dmitry Platonoff. | [niallp](#team--niallp) |
| Fix | BeanUtilsBean.getArrayProperty() does not use ConvertUtils. Fixes [BEANUTILS-110](https://issues.apache.org/jira/browse/BEANUTILS-110). Thanks to Etienne Bernard. | [niallp](#team--niallp) |
| Fix | MappedPropertyDescriptor - replace copied code. Fixes [BEANUTILS-6](https://issues.apache.org/jira/browse/BEANUTILS-6). Thanks to Sam Ruby. | [niallp](#team--niallp) |
| Fix | MappedPropertyDescriptor: Add comments re: \* use of static variable safe in shared classloader \* memory leak possible on webapp undeploy. | [skitching](#team--skitching) |
| Fix | MappedPropertyDescriptor doesn't recognize boolean property accessor. Fixes [BEANUTILS-69](https://issues.apache.org/jira/browse/BEANUTILS-69). Thanks to Chris Audley. | [niallp](#team--niallp) |
| Fix | Add test for MappedPropertyDescriptor with different types on get/set methods. Fixes [BEANUTILS-163](https://issues.apache.org/jira/browse/BEANUTILS-163). | [niallp](#team--niallp) |
| Fix | LocaleBeanUtils setProperty does not work on nested property. Fixes [BEANUTILS-140](https://issues.apache.org/jira/browse/BEANUTILS-140). Thanks to Marco La Porta. | [niallp](#team--niallp) |
| Fix | Package scope implementation of a public interface for mapped property fails (fixed by changes to MappedPropertyDescriptor associated with BEANUTILS-6). Fixes [BEANUTILS-87](https://issues.apache.org/jira/browse/BEANUTILS-87). Thanks to YOKOTA Takehiko. | [niallp](#team--niallp) |
| Fix | PropertyUtils incosistency - can't use "dot" in mapped properties for setProperty or getPropertyDescriptor (fixed by the changes for BEANUTILS-259 Plugable Property Name Expression Resolver). Fixes [BEANUTILS-33](https://issues.apache.org/jira/browse/BEANUTILS-33). Thanks to Eoin Curran. | [niallp](#team--niallp) |
| Fix | Public methods overridden in anonymous or private subclasses are not recognized by PropertyUtils. Fixes [BEANUTILS-273](https://issues.apache.org/jira/browse/BEANUTILS-273). Thanks to Marcelo Liberato. | [niallp](#team--niallp) |
| Fix | PropertyUtilsBean's isReadable() / isWriteable() always return false for mapped properties. Fixes [BEANUTILS-88](https://issues.apache.org/jira/browse/BEANUTILS-88). Thanks to Chuck Daniels. | [niallp](#team--niallp) |
| Fix | PropertyUtilsBean isReadable() and isWriteable() methods do not work correctly for WrapDynaBean. Fixes [BEANUTILS-61](https://issues.apache.org/jira/browse/BEANUTILS-61). Thanks to Brian Ewins. | [niallp](#team--niallp) |
| Fix | PropertyUtils.isReadable() and PropertyUtils.getProperty() not consistent. Fixes [BEANUTILS-18](https://issues.apache.org/jira/browse/BEANUTILS-18). Thanks to Maarten Coene. | [niallp](#team--niallp) |
| Fix | PropertyUtilsBean.copyProperties does not catch NoSuchMethodException. Fixes [BEANUTILS-92](https://issues.apache.org/jira/browse/BEANUTILS-92). Thanks to Will Pugh. | [bayard](#team--bayard) |
| Fix | PropertyUtilsBean.getIndexedProperty()'s javadoc should indicate IndexOutOufBoundsException can be thrown rather than just ArrayIndexOutOufBoundsException. Fixes [BEANUTILS-256](https://issues.apache.org/jira/browse/BEANUTILS-256). Thanks to Torsten Feig. | [niallp](#team--niallp) |
| Fix | Create new methods getPropertyOfMapBean and setPropertyOfMapBean that the existing setNestedProperty and getNestedProperty methods now call when they discover the bean they are accessing implements Map. This makes it much easier for users to subclass and customize this behavior of PropertyUtilsBean, eg in order to restore pre-1.5 behavior. This patch also causes an exception to be thrown when the propertyName passed to getPropertyOfMapBean or setPropertyOfMapBean has MAPPED\_DELIM or INDEXED\_DELIM chars in it. This never worked as expected before (the whole string was treated literally as the propertyName), so throwing an exception here should not break any existing code. It should be of help to future developers who make this mistake though... Fixes [BEANUTILS-162](https://issues.apache.org/jira/browse/BEANUTILS-162). | [skitching](#team--skitching) |
| Fix | Ignore simple properties on java.util.Map objects - Map methods are always used on a Map object. Reverts BEANUTILS-144. See BEANUTILS-162 for discussion. | [skitching](#team--skitching) |
| Fix | Correct getPropertyDescriptor() and setNestedProperty() methods to throw a NestedNullException rather than just IllegalArgumentException (consistent with the getNestedProperty() method). Fixes [BEANUTILS-262](https://issues.apache.org/jira/browse/BEANUTILS-262). | [niallp](#team--niallp) |
| Fix | Problems on indexed property with JDK 1.4. Fixes [BEANUTILS-97](https://issues.apache.org/jira/browse/BEANUTILS-97). | [niallp](#team--niallp) |
| Update | BooleanArrayConverter: Use new AbstractArrayConverter constructors and Convert strings to booleans by invoking a BooleanConverter rather than hard-wiring the conversion. | [skitching](#team--skitching) |
| Update | BooleanConverter: Add facility for user to override the default set of true and false string definitions and provide ability to pass special NO\_DEFAULT object as the "defaultValue" constructor parameter. Thanks to Eric Rizzo. | [skitching](#team--skitching) |
| Update | AbstractArrayConverter: provide ability to pass special NO\_DEFAULT object as the "defaultValue" constructor parameter. | [skitching](#team--skitching) |
| Fix | DecimalLocaleConverter and subClasses never throw a ConversionException. Fixes [BEANUTILS-78](https://issues.apache.org/jira/browse/BEANUTILS-78). Thanks to Stefan Lotscher. | [niallp](#team--niallp) |
| Fix | FloatLocaleConverter cannot parse negative values. Fixes [BEANUTILS-44](https://issues.apache.org/jira/browse/BEANUTILS-44). Thanks to Paul Jenkins. | [niallp](#team--niallp) |
| Fix | Improve ClassConverter robustness. Fixes [BEANUTILS-263](https://issues.apache.org/jira/browse/BEANUTILS-263). Thanks to Alex Albu. | [niallp](#team--niallp) |
| Fix | DateLocaleConverter does not always throw an Exception for invalid dates. Fixes [BEANUTILS-271](https://issues.apache.org/jira/browse/BEANUTILS-271). Thanks to Nico Hoogervorst. | [niallp](#team--niallp) |
| Fix | Don't try parsing values that are already Dates/Numbers in Date/Number locale Converters. Fixes [BEANUTILS-288](https://issues.apache.org/jira/browse/BEANUTILS-288). | [niallp](#team--niallp) |
| Fix | WrapDynaClass: Added comment re potential memory leak, and safety when using shared classloader | [skitching](#team--skitching) |
| Fix | Make WrapDynaBean Serializable. | [niallp](#team--niallp) |
| Fix | WrapDynaBeanTestCase failing with jikes/kaffe because of static List in TestBean. Fixes [BEANUTILS-36](https://issues.apache.org/jira/browse/BEANUTILS-36). Thanks to Jack. | [niallp](#team--niallp) |
| Fix | Misleading error message in ConvertingWrapDynaBean. Fixes [BEANUTILS-23](https://issues.apache.org/jira/browse/BEANUTILS-23). Thanks to Aslak Hellesoy. | [niallp](#team--niallp) |
| Fix | LazyDynaBean: don't try and instantiate properties of type Object.class. Fixes [BEANUTILS-24](https://issues.apache.org/jira/browse/BEANUTILS-24). Thanks to Roi Ares. | [niallp](#team--niallp) |
| Fix | LazyDynabean Javadoc corrections. Fixes [BEANUTILS-133](https://issues.apache.org/jira/browse/BEANUTILS-133). Thanks to Masoud Omidvar. | [niallp](#team--niallp) |
| Fix | LazyDynaClass can create a DynaProperty with a "null" type. Fixes [BEANUTILS-250](https://issues.apache.org/jira/browse/BEANUTILS-250). | [niallp](#team--niallp) |
| Fix | JDBCDynaClass "lowerCase" option causes problems in RowSetDynaClass and ResultSetIterator. Fixes [BEANUTILS-289](https://issues.apache.org/jira/browse/BEANUTILS-289). | [niallp](#team--niallp) |
| Fix | RowSetDynaClass fails to copy ResultSet to DynaBean with Oracle 10g JDBC driver. Fixes [BEANUTILS-142](https://issues.apache.org/jira/browse/BEANUTILS-142). Thanks to Li Zhang. | [niallp](#team--niallp) |
| Fix | Fix BeanComparator throws wrong exception and hides cause. Fixes [BEANUTILS-241](https://issues.apache.org/jira/browse/BEANUTILS-241). Thanks to Chris Hyzer. | [bayard](#team--bayard) |
| Fix | Deprecate the public static defaultTransformers HashMap and make it unmodifiable. Fixes [BEANUTILS-112](https://issues.apache.org/jira/browse/BEANUTILS-112). Thanks to Simon Kitching. | [niallp](#team--niallp) |
| Update | Merge Bean-Collections back into core BeanUtils and remove Bean-Collections sub-project. Fixes [BEANUTILS-290](https://issues.apache.org/jira/browse/BEANUTILS-290). | [niallp](#team--niallp) |
| Fix | Fixi the build to include all the tests and change the build.properties.sample so it's easier to use for the default maven user (ie: it looks by default in the .maven repository). Fixes [BEANUTILS-287](https://issues.apache.org/jira/browse/BEANUTILS-287). | [bayard](#team--bayard) |
| Fix | Improvements to maven build. Fixes [BEANUTILS-217](https://issues.apache.org/jira/browse/BEANUTILS-217). Thanks to Carlos Sanchez. | [niallp](#team--niallp) |
| Fix | Add Implementation-Vendor-Id entry to jar's manifest. Fixes [BEANUTILS-54](https://issues.apache.org/jira/browse/BEANUTILS-54). Thanks to Pascal Grange. | [niallp](#team--niallp) |
| Fix | Resolve compiler warnings: Unused imports, un-read local variables, field hiding, empty block, improperly used statics, uncessary semi colons, unnecessary casts. Fixes [BEANUTILS-121](https://issues.apache.org/jira/browse/BEANUTILS-121). Thanks to Chris Tilden. | [bayard](#team--bayard) |
| Fix | Replace use of static Log objects with instance or local variables. It isn't safe to use static Log objects in code that might be deployed via a shared classloader as they will bind to the Log object from the context classloader in use when the first use happens. | [skitching](#team--skitching) |
| Fix | BeanMap: Fix internal variable to not include non-existant write methods. - ported from Commons Collections. Fixes [COLLECTIONS-22](https://issues.apache.org/jira/browse/COLLECTIONS-22). Thanks to Dimiter Dimitrov. | [scolebourne](#team--scolebourne) |
| Update | Change MethodUtils to make getMatchingAccessibleMethod() method selection more rational. Thanks to Steve Cohen. | [rdonkin](#team--rdonkin) |

<a id="changes--release-1.7.0-2004-08-02"></a>

## Release 1.7.0 – 2004-08-02

| Type | Changes | By |
| --- | --- | --- |
| Update | See href="https://commons.apache.org/beanutils/commons-beanutils-1.7.0/RELEASE-NOTES.txt | - |

<a id="changes--release-1.6.1-2003-02-18"></a>

## Release 1.6.1 – 2003-02-18

| Type | Changes | By |
| --- | --- | --- |
| Update | See https://commons.apache.org/beanutils/commons-beanutils-1.6.1/RELEASE-NOTES.txt | - |

<a id="changes--release-1.6-2003-01-21"></a>

## Release 1.6 – 2003-01-21

| Type | Changes | By |
| --- | --- | --- |
| Update | See https://commons.apache.org/beanutils/commons-beanutils-1.6/RELEASE-NOTES.txt | - |

<a id="changes--release-1.5-2002-10-23"></a>

## Release 1.5 – 2002-10-23

| Type | Changes | By |
| --- | --- | --- |
| Update | See https://commons.apache.org/beanutils/commons-beanutils-1.5/RELEASE-NOTES.txt | - |

<a id="changes--release-1.4.1-2002-08-28"></a>

## Release 1.4.1 – 2002-08-28

| Type | Changes | By |
| --- | --- | --- |
| Fix | See https://commons.apache.org/beanutils/commons-beanutils-1.4.1/RELEASE-NOTES.txt | - |

<a id="changes--release-1.4-2002-08-13"></a>

## Release 1.4 – 2002-08-13

| Type | Changes | By |
| --- | --- | --- |
| Update | See https://commons.apache.org/beanutils/commons-beanutils-1.4/RELEASE-NOTES.txt | - |

<a id="changes--release-1.3-2002-04-29"></a>

## Release 1.3 – 2002-04-29

| Type | Changes | By |
| --- | --- | --- |
| Update | See https://commons.apache.org/beanutils/commons-beanutils-1.3/RELEASE-NOTES.txt | - |

<a id="changes--release-1.2-2001-12-24"></a>

## Release 1.2 – 2001-12-24

| Type | Changes | By |
| --- | --- | --- |
| Update | See https://commons.apache.org/beanutils/commons-beanutils-1.2/RELEASE-NOTES.txt | - |

<a id="changes--release-1.1-2001-09-22"></a>

## Release 1.1 – 2001-09-22

| Type | Changes | By |
| --- | --- | --- |
| Update | Version 1.1 | - |

<a id="changes--release-1.0-2001-07-14"></a>

## Release 1.0 – 2001-07-14

| Type | Changes | By |
| --- | --- | --- |
| Add | Initial Release | - |

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/scm.html -->

<!-- page_index: 3 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-beanutils.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-beanutils.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-beanutils.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/security.html -->

<!-- page_index: 4 -->

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
[user mailing list](https://commons.apache.org/proper/commons-beanutils/mail-lists.html)
.

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report
them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

<a id="security--cve-2019-10086"></a>

## CVE-2019-10086

- CVE-2019-10086: Apache Commons Beanutils does not suppresses the class property in PropertyUtilsBean by default.
- Severity: Medium
- Vendor: The Apache Software Foundation
- Versions Affected: commons-beanutils-1.9.3 and earlier
- Description: A special BeanIntrospector class was added in version 1.9.2.
  This can be used to stop attackers from using the class property of
  Java objects to get access to the classloader.
  However this protection was not enabled by default.
  PropertyUtilsBean (and consequently BeanUtilsBean) now disallows class
  level property access by default, thus protecting against
  CVE-2014-0114.
- Mitigation: 1.X users should migrate to 1.9.4.
- Credit: This was discovered by Melloware (https://melloware.com/).

Example:

```

/**
 * Example displaying the new default behavior such that
 * it is not possible to access class level properties utilizing the
 * BeanUtilsBean, which in turn utilizes the PropertyUtilsBean.
 */
public void testSuppressClassPropertyByDefault() throws Exception {
    final BeanUtilsBean bub = new BeanUtilsBean();
    final AlphaBean bean = new AlphaBean();
    try {
        bub.getProperty(bean, "class");
        fail("Could access class property!");
    } catch (final NoSuchMethodException ex) {
        // ok
    }
}

/**
 * Example showing how by which one would use to revert to the 
 * behaviour prior to the 1.9.4 release where class level properties were accessible by
 * the BeanUtilsBean and the PropertyUtilsBean.
 */
public void testAllowAccessToClassProperty() throws Exception {
    final BeanUtilsBean bub = new BeanUtilsBean();
    bub.getPropertyUtils().removeBeanIntrospector(SuppressPropertiesBeanIntrospector.SUPPRESS_CLASS);
    final AlphaBean bean = new AlphaBean();
    String result = bub.getProperty(bean, "class");
    assertEquals("Class property should have been accessed", "class org.apache.commons.beanutils2.AlphaBean", result);
}
```

References:

1. https://issues.apache.org/jira/browse/BEANUTILS-520
2. http://commons.apache.org/proper/commons-beanutils/

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/building.html -->

<!-- page_index: 5 -->

<a id="building--overview"></a>

# Overview

Commons BeanUtils can be built using
[Maven 3](http://maven.apache.org)
(Recommended: Maven 3.3)
and JDK 6 / OpenJDK 6 or later (recommended: JDK 8).

Further details can be found in the
[commons build instructions](https://commons.apache.org/building.html).

<a id="building--maven-3-goals"></a>

# Maven 3 Goals

Build using
[Maven 3](http://maven.apache.org)
is the preferred build method.
The compiled BeanUtils JAR should work with Java 6 or later.

To build
`target/commons-beanutils-*.jar`

```

        mvn clean package
      
```

or to install into your
`~/.m2/repository`

```

        mvn clean install
      
```

You can skip the unit tests by adding the parameter
`-DskipTests=true`

To regenerate the web site
(corresponding to
https://commons.apache.org/proper/commons-beanutils/)

```

        mvn clean site
      
```

Note: the Apache Commons BeanUtils site should include a
[japicmp report](#japicmp)
for the
purpose of checking API version compatibility; to enable this, use Java 7
or later and run instead:

```

        mvn clean package site -Pjapicmp
      
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/project-info.html -->

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons BeanUtils provides an easy-to-use but flexible wrapper around reflection and introspection. |
| [Summary](https://commons.apache.org/proper/commons-beanutils/summary.html) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-beanutils/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-beanutils/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-beanutils/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-beanutils/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-beanutils/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-beanutils/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-beanutils/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/team.html -->

<!-- page_index: 7 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | dion | Dion Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | craigmcc | Craig McClanahan | [craigmcc@apache.org](mailto:craigmcc@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | geirm | Geir Magnusson Jr. | [geirm@apache.org](mailto:geirm@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | sanders | Scott Sanders | [sanders@apache.org](mailto:sanders@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | jstrachan | James Strachan | [jstrachan@apache.org](mailto:jstrachan@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | rwaldhoff | Rodney Waldhoff | [rwaldhoff@apache.org](mailto:rwaldhoff@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | mvdb | Martin van den Bemt | [mvdb@apache.org](mailto:mvdb@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | yoavs | Yoav Shapira | [yoavs@apache.org](mailto:yoavs@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | niallp | Niall Pemberton | [niallp@apache.org](mailto:niallp@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | skitching | Simon Kitching | [skitching@apache.org](mailto:skitching@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | jcarman | James Carman | [jcarman@apache.org](mailto:jcarman@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | tobrien | Tim O'Brien | [tobrien@apache.org](mailto:tobrien@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | epugh | David Eric Pugh | [epugh@apache.org](mailto:epugh@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | rwaldhoff | Rodney Waldhoff | [rwaldhoff@apache.org](mailto:rwaldhoff@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | morgand | Morgan James Delagrange | [morgand@apache.org](mailto:morgand@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | jconlon | John E. Conlon | [jconlon@apache.org](mailto:jconlon@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | scolebourne | Stephen Colebourne | [scolebourne@apache.org](mailto:scolebourne@apache.org) | - | The Apache Software Foundation | - | - | - |
|  | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
|  | stain | Stian Soiland-Reyes | [stain@apache.org](mailto:stain@apache.org) | <http://orcid.org/0000-0001-9842-9718> | The Apache Software Foundation | - | - | +0 |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Name |
| --- |
| Paul Jack |
| Stephen Colebourne |
| Berin Loritsch |
| Alex Crown |
| Marcus Zander |
| Paul Hamamnt |
| Rune Johannesen |
| Clebert Suconic |
| Norm Deane |
| Ralph Schaer |
| Chris Audley |
| Rey François |
| Gregor Raýman |
| Jan Sorensen |
| Eric Pabst |
| Paulo Gaspar |
| Michael Smith |
| George Franciscus |
| Erik Meade |
| Tomas Viberg |
| Yauheny Mikulski |
| Michael Szlapa |
| Juozas Baliuka |
| Tommy Tynjä |
| Bernhard Seebass |
| Raviteja Lokineni |
| Sergey Chernov |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/ci-management.html -->

<!-- page_index: 8 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/project-reports.html -->

<!-- page_index: 9 -->

<a id="project-reports--generated-reports"></a>

# Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](https://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [Changes](#changes) | Changes report on releases of this project. |
| [JIRA Report](#jira-changes) | Report on Issues from the JIRA Issue Tracking System. |
| [Javadoc](https://commons.apache.org/proper/commons-beanutils/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-beanutils/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-beanutils/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire](#surefire) | Report on the test results of the project. |
| [Rat Report](#rat-report) | Report on compliance to license related source code policies |
| [JaCoCo](https://commons.apache.org/proper/commons-beanutils/jacoco/index.html) | JaCoCo Coverage Report. |
| [japicmp](#japicmp) | Comparing source compatibility of commons-beanutils2-2.0.0-M2.jar against commons-beanutils2-2.0.0-M1.jar |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [PMD](#pmd) | Verification of coding rules. |
| [SpotBugs](#spotbugs) | Generates a source code report with the SpotBugs Library. |

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/jira-changes.html -->

<!-- page_index: 10 -->

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
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-506">BEANUTILS-506</a></td>
<td>-</td>
<td>Building with Oracle Java 9.0.1 causes unit tests to fail.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-491">BEANUTILS-491</a></td>
<td>-</td>
<td>Tests fail on Oracle and IBM Java 8</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-442">BEANUTILS-442</a></td>
<td>Bean / Property Utils</td>
<td>Broken Link</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-165">BEANUTILS-165</a></td>
<td>-</td>
<td>Cache Bug in the PropertyUtils.java line 889</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-164">BEANUTILS-164</a></td>
<td>-</td>
<td>populate method doesn't work for an indexed setter for arrays</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-161">BEANUTILS-161</a></td>
<td>-</td>
<td>StringArrayConvertor does not convert int[] to String[]</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-151">BEANUTILS-151</a></td>
<td>-</td>
<td>Combined property access ( b.mapped(bar/foo) ) throws excception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-150">BEANUTILS-150</a></td>
<td>-</td>
<td>RowSetDynaClass hardcodes BasicDynaBean</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-148">BEANUTILS-148</a></td>
<td>-</td>
<td>minor typo in overview doc</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-147">BEANUTILS-147</a></td>
<td>-</td>
<td>[beanutils][PATCH] LICENSE.txt: acknowledgement(s) typo</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-146">BEANUTILS-146</a></td>
<td>-</td>
<td>[bean] DateLocaleConverter is not thread-safe</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-145">BEANUTILS-145</a></td>
<td>-</td>
<td>Can't use . (dot) in mapped properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-144">BEANUTILS-144</a></td>
<td>-</td>
<td>PropertyUtils.setProperty Ignores Property Setter</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-143">BEANUTILS-143</a></td>
<td>-</td>
<td>BasicDynaBean, BasicDynaClass not serializable</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-141">BEANUTILS-141</a></td>
<td>-</td>
<td>Mapped properties should work against a collection object as well as method definition only.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-139">BEANUTILS-139</a></td>
<td>-</td>
<td>[PATCH] Beanutils package documentation fixes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-132">BEANUTILS-132</a></td>
<td>-</td>
<td>ClassConverter @since 1.3 when it should be @since 1.4</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-131">BEANUTILS-131</a></td>
<td>-</td>
<td>[beanutils]BigDecimalLocaleConverter seems not working as designed</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-128">BEANUTILS-128</a></td>
<td>-</td>
<td>MethodUtils getMatchingAccessibleMethod has non-deterministic behavior</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-120">BEANUTILS-120</a></td>
<td>-</td>
<td>ResultSetDynaClass lowerCase broken</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-114">BEANUTILS-114</a></td>
<td>-</td>
<td>[beanutils]DateLocaleConverter does NOT return a default value if a conversion error occurs</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-107">BEANUTILS-107</a></td>
<td>-</td>
<td>ConvertUtils changes long standing default conversions from null to zero</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-105">BEANUTILS-105</a></td>
<td>-</td>
<td>NullPointerException in BeanUtils.java when submission of form with &lt;select&gt; results in ...&amp;bla=&amp;...</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-99">BEANUTILS-99</a></td>
<td>-</td>
<td>ResultSetDynaClass misspelled ResutSetDynaClass</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-89">BEANUTILS-89</a></td>
<td>-</td>
<td>Fix for ConvertUtils.deregister(Class clazz)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-85">BEANUTILS-85</a></td>
<td>-</td>
<td>ConvertUtils.convert does not support zero-length arrays</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-84">BEANUTILS-84</a></td>
<td>-</td>
<td>BeanUtils.populate() throws IllegalArgumentException when setting indexed property as array.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-83">BEANUTILS-83</a></td>
<td>-</td>
<td>BeanUtils.copyProperties goes through wasted processing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-79">BEANUTILS-79</a></td>
<td>-</td>
<td>BeanUtils.populate fails with DoubleLocaleConverter on integer values</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-75">BEANUTILS-75</a></td>
<td>-</td>
<td>Abstract common functionality found in RowSetDynaClass and ResultSetDynaClass</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-74">BEANUTILS-74</a></td>
<td>-</td>
<td>BeanUtils.cloneBean fails to clone DynaBeans</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-71">BEANUTILS-71</a></td>
<td>-</td>
<td>BeanUtils.setProperty does not work with indexed properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-67">BEANUTILS-67</a></td>
<td>-</td>
<td>[beanutils] Broken link report (three 404s)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-63">BEANUTILS-63</a></td>
<td>-</td>
<td>PropertyUtil.getPropertyType() should support MappedPropertyDecriptors</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-62">BEANUTILS-62</a></td>
<td>-</td>
<td>[beanutils] Converters should really be final?</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-60">BEANUTILS-60</a></td>
<td>-</td>
<td>[beanutils] PropertyUtils.copyProperties does not copy to DynaBean</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-58">BEANUTILS-58</a></td>
<td>-</td>
<td>setProperty throws exception on null value</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-57">BEANUTILS-57</a></td>
<td>-</td>
<td>Wrong method BeanUtils.populate(), so that in struts indexed multiselects not work.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-56">BEANUTILS-56</a></td>
<td>-</td>
<td>populate method has mistaken the judgment which uses indexed poperty.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-53">BEANUTILS-53</a></td>
<td>-</td>
<td>BeanComparator should handle null property values (?)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-52">BEANUTILS-52</a></td>
<td>-</td>
<td>[beanutils] WrapDynaBean misleading error message: Property has no read method</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-51">BEANUTILS-51</a></td>
<td>-</td>
<td>MappedPropertyDescriptor requires more permissions than necessary</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-50">BEANUTILS-50</a></td>
<td>-</td>
<td>PropertyUtils.copyProperties don't work if JavaBean orig and DynaBean dest</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-46">BEANUTILS-46</a></td>
<td>-</td>
<td>Default convertion patterns in LocaleConverUtils do not work</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-45">BEANUTILS-45</a></td>
<td>-</td>
<td>Bean Utilities: add BeanComparator.equals()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-32">BEANUTILS-32</a></td>
<td>-</td>
<td>[bean] DecimalLocaleConverter is not thread-safe</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-29">BEANUTILS-29</a></td>
<td>-</td>
<td>debug logging turns on exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-28">BEANUTILS-28</a></td>
<td>-</td>
<td>BeanUtils.populate() does not handle nested properties of dynabean</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-27">BEANUTILS-27</a></td>
<td>-</td>
<td>[beanutils] Excessive exceptions log under security manager</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-26">BEANUTILS-26</a></td>
<td>-</td>
<td>Missing dependency on FastHashMap is masked</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-15">BEANUTILS-15</a></td>
<td>-</td>
<td>ConvertUtils.convert(Object) doesn't use registered convertor</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-14">BEANUTILS-14</a></td>
<td>-</td>
<td>BeanUtils.setProperty doesn't convert primitive wrappers</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-12">BEANUTILS-12</a></td>
<td>-</td>
<td>ResultSetDynaClass.createDynaProperty uses getColumnName(i).toLowerCase()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-8">BEANUTILS-8</a></td>
<td>-</td>
<td>BeanComparator compare method throws ClassCastException regardless of underlying exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-5">BEANUTILS-5</a></td>
<td>-</td>
<td>Missing Test case</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-3">BEANUTILS-3</a></td>
<td>-</td>
<td>commons-beanutils.jar, debug info line numbers off by factor of 2</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-2">BEANUTILS-2</a></td>
<td>-</td>
<td>MethodUtils method compare bug</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-522">BEANUTILS-522</a></td>
<td>-</td>
<td>Update Apache Commons Collections from 4.3 to 4.4.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-428">BEANUTILS-428</a></td>
<td>Bean / Property Utils</td>
<td>Provide a BeanIntrospector implementation which supports properties in a fluent API</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-240">BEANUTILS-240</a></td>
<td>-</td>
<td>[beanutils] Wrapped DynaBean Enhancement</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-236">BEANUTILS-236</a></td>
<td>-</td>
<td>Add "y/n" to BooleanConverter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-234">BEANUTILS-234</a></td>
<td>-</td>
<td>limit the number of rows returned by RowSetDynaClass</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-232">BEANUTILS-232</a></td>
<td>-</td>
<td>MethodUtils.getMatchingAccessibleMethod throws NullPointerException when parameterTypes is null</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-231">BEANUTILS-231</a></td>
<td>-</td>
<td>Add "1/0" to BooleanConverter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-225">BEANUTILS-225</a></td>
<td>-</td>
<td>Can add a method cache in MethodUtils</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-222">BEANUTILS-222</a></td>
<td>-</td>
<td>Add ClassConverter to standard converters</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-216">BEANUTILS-216</a></td>
<td>-</td>
<td>[beanutils] javadoc of BeanUtilsBean.describe(Object) incomplete</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-203">BEANUTILS-203</a></td>
<td>-</td>
<td>[beanutils] LazyDynaBean and LazyDynaClass</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-195">BEANUTILS-195</a></td>
<td>-</td>
<td>ConvertUtils is not (thread)safe</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-190">BEANUTILS-190</a></td>
<td>-</td>
<td>'lenient' method is loose in 'DateLocaleConverter'</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-180">BEANUTILS-180</a></td>
<td>-</td>
<td>java.util.List to be permitted for indexed properties.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-174">BEANUTILS-174</a></td>
<td>-</td>
<td>Mapped properties require getter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-170">BEANUTILS-170</a></td>
<td>-</td>
<td>java.util.List support for getIndexedProperty()</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-169">BEANUTILS-169</a></td>
<td>-</td>
<td>Add methods to find and invoke constructor methods</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-166">BEANUTILS-166</a></td>
<td>-</td>
<td>speedup for beanutils / array getter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-559">BEANUTILS-559</a></td>
<td>-</td>
<td>Is there a plan to release a new version because the time before the previous version is too long?</td>
<td>Wish</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-404">BEANUTILS-404</a></td>
<td>-</td>
<td>BeanUtils on Git</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-564">BEANUTILS-564</a></td>
<td>-</td>
<td>Some tests fail on Java 21 and 22-ea</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-563">BEANUTILS-563</a></td>
<td>Bean / Property Utils</td>
<td>Building from source release fails with a Maven error</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-560">BEANUTILS-560</a></td>
<td>-</td>
<td>Add support for JPMS</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-532">BEANUTILS-532</a></td>
<td>Bean-Collections</td>
<td>Require commons-beanutils library which supports commons-collections-4.x version </td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-529">BEANUTILS-529</a></td>
<td>-</td>
<td>Log at the debug level instead of info</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-505">BEANUTILS-505</a></td>
<td>-</td>
<td>Add missing serialVersionUID to Serializable classes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-475">BEANUTILS-475</a></td>
<td>-</td>
<td>beanutils could use commons-collections4 instead of commons-collections 3</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-402">BEANUTILS-402</a></td>
<td>Bean / Property Utils, ConvertUtils &amp; Converters, Locale BeanUtils / Converters</td>
<td>Double-Checked Locking anti pattern in WeakFastHashMap</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-361">BEANUTILS-361</a></td>
<td>-</td>
<td>BeanMap.defaultTransformers should be final</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-549">BEANUTILS-549</a></td>
<td>Bean / Property Utils</td>
<td>Update commons-lang dependency to commons-lang3</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-537">BEANUTILS-537</a></td>
<td>-</td>
<td>Fix typos; fix error in Javadoc; performance fix; fix code smells #25</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-517">BEANUTILS-517</a></td>
<td>-</td>
<td>Update Apache Commons Collections from 4.2 to 4.3</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-515">BEANUTILS-515</a></td>
<td>-</td>
<td>Update from Java 7 to 8.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-504">BEANUTILS-504</a></td>
<td>-</td>
<td>Update from Java 6 to 7</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-500">BEANUTILS-500</a></td>
<td>Bean / Property Utils</td>
<td>Upgrade from Apache Commons Collections 3 to 4</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-530">BEANUTILS-530</a></td>
<td>-</td>
<td>Add converts for java.time JRE classes</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-528">BEANUTILS-528</a></td>
<td>ConvertUtils &amp; Converters</td>
<td>Converters for URI, UUID, and Path</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-527">BEANUTILS-527</a></td>
<td>-</td>
<td>Convert from Collections4 to java.util.function #8</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-514">BEANUTILS-514</a></td>
<td>-</td>
<td>Remove deprecated code for 2.0.0</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-512">BEANUTILS-512</a></td>
<td>-</td>
<td>Add Automatic-Module-Name entry to MANIFEST.MF</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-565">BEANUTILS-565</a></td>
<td>-</td>
<td>Types postfixed with "2" need to be merged into their supertypes</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0.0-M1</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-503">BEANUTILS-503</a></td>
<td>-</td>
<td>Change Java package from org.apache.commons.beanutils to org.apache.commons.beanutils2</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.10.0</td>
<td><a href="https://issues.apache.org/jira/browse/BEANUTILS-574">BEANUTILS-574</a></td>
<td>-</td>
<td>The version number under tag rel/commons-beanutils-1.10.0 in GitHub is incorrect.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr></table></section>
</td>
</tr>
</table>

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/surefire.html -->

<!-- page_index: 11 -->

<a id="surefire--surefire-report"></a>

# Surefire Report

<a id="surefire--summary"></a>

## Summary

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 1264 | 0 | 0 | 12 | 99.1% | 17.38 s |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

<a id="surefire--package-list"></a>

## Package List

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Package | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.beanutils2.expression](#surefire--org.apache.commons.beanutils2.expression) | 7 | 0 | 0 | 0 | 100% | 0.025 s |
| [org.apache.commons.beanutils2.converters](#surefire--org.apache.commons.beanutils2.converters) | 410 | 0 | 0 | 0 | 100% | 1.953 s |
| [org.apache.commons.beanutils2.memoryleaktests](#surefire--org.apache.commons.beanutils2.memoryleaktests) | 8 | 0 | 0 | 0 | 100% | 10.35 s |
| [org.apache.commons.beanutils2.sql](#surefire--org.apache.commons.beanutils2.sql) | 16 | 0 | 0 | 0 | 100% | 0.088 s |
| [org.apache.commons.beanutils2.bugs](#surefire--org.apache.commons.beanutils2.bugs) | 93 | 0 | 0 | 1 | 98.9% | 2.697 s |
| [org.apache.commons.beanutils2](#surefire--org.apache.commons.beanutils2) | 673 | 0 | 0 | 5 | 99.3% | 1.865 s |
| [org.apache.commons.beanutils2.locale](#surefire--org.apache.commons.beanutils2.locale) | 23 | 0 | 0 | 6 | 73.9% | 0.257 s |
| [org.apache.commons.beanutils2.sql.converters](#surefire--org.apache.commons.beanutils2.sql.converters) | 34 | 0 | 0 | 0 | 100% | 0.147 s |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

<a id="surefire--org.apache.commons.beanutils2.expression"></a>

### org.apache.commons.beanutils2.expression

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [DefaultResolverTest](#surefire--org.apache.commons.beanutils2.expression.defaultresolvertest) | 7 | 0 | 0 | 0 | 100% | 0.025 s |

<a id="surefire--org.apache.commons.beanutils2.converters"></a>

### org.apache.commons.beanutils2.converters

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [FloatLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.floatlocaleconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.068 s |
|  | [FileConverterTest](#surefire--org.apache.commons.beanutils2.converters.fileconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |
|  | [StringConverterTest](#surefire--org.apache.commons.beanutils2.converters.stringconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [EnumConverterTest](#surefire--org.apache.commons.beanutils2.converters.enumconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.027 s |
|  | [IntegerLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.integerlocaleconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.044 s |
|  | [DateConverterTest](#surefire--org.apache.commons.beanutils2.converters.dateconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.048 s |
|  | [BigDecimalConverterTest](#surefire--org.apache.commons.beanutils2.converters.bigdecimalconvertertest) | 20 | 0 | 0 | 0 | 100% | 0.055 s |
|  | [YearMonthConverterTest](#surefire--org.apache.commons.beanutils2.converters.yearmonthconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.029 s |
|  | [CalendarConverterTest](#surefire--org.apache.commons.beanutils2.converters.calendarconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [ByteLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.bytelocaleconvertertest) | 9 | 0 | 0 | 0 | 100% | 0.045 s |
|  | [PatternConverterTest](#surefire--org.apache.commons.beanutils2.converters.patternconvertertest) | 1 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [PointConverterTest](#surefire--org.apache.commons.beanutils2.converters.pointconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [UUIDConverterTest](#surefire--org.apache.commons.beanutils2.converters.uuidconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.027 s |
|  | [BooleanConverterTest](#surefire--org.apache.commons.beanutils2.converters.booleanconvertertest) | 7 | 0 | 0 | 0 | 100% | 0.029 s |
|  | [DurationConverterTest](#surefire--org.apache.commons.beanutils2.converters.durationconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.029 s |
|  | [FloatConverterTest](#surefire--org.apache.commons.beanutils2.converters.floatconvertertest) | 21 | 0 | 0 | 0 | 100% | 0.055 s |
|  | [BigDecimalLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.bigdecimallocaleconvertertest) | 9 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [PeriodConverterTest](#surefire--org.apache.commons.beanutils2.converters.periodconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [LongLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.longlocaleconvertertest) | 9 | 0 | 0 | 0 | 100% | 0.045 s |
|  | [ClassConverterTest](#surefire--org.apache.commons.beanutils2.converters.classconvertertest) | 7 | 0 | 0 | 0 | 100% | 0.030 s |
|  | [ColorConverterTest](#surefire--org.apache.commons.beanutils2.converters.colorconvertertest) | 16 | 0 | 0 | 0 | 100% | 0.042 s |
|  | [CharacterConverterTest](#surefire--org.apache.commons.beanutils2.converters.characterconvertertest) | 6 | 0 | 0 | 0 | 100% | 0.030 s |
|  | [DoubleLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.doublelocaleconvertertest) | 9 | 0 | 0 | 0 | 100% | 0.042 s |
|  | [ZonedDateTimeConverterTest](#surefire--org.apache.commons.beanutils2.converters.zoneddatetimeconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.047 s |
|  | [ShortLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.shortlocaleconvertertest) | 9 | 0 | 0 | 0 | 100% | 0.044 s |
|  | [URLConverterTest](#surefire--org.apache.commons.beanutils2.converters.urlconvertertest) | 1 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [InetAddressConverterTest](#surefire--org.apache.commons.beanutils2.converters.inetaddressconvertertest) | 5 | 0 | 0 | 0 | 100% | 0.037 s |
|  | [YearConverterTest](#surefire--org.apache.commons.beanutils2.converters.yearconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |
|  | [MonthDayConverterTest](#surefire--org.apache.commons.beanutils2.converters.monthdayconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.029 s |
|  | [IntegerConverterTest](#surefire--org.apache.commons.beanutils2.converters.integerconvertertest) | 22 | 0 | 0 | 0 | 100% | 0.056 s |
|  | [ZoneIdConverterTest](#surefire--org.apache.commons.beanutils2.converters.zoneidconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.030 s |
|  | [OffsetTimeConverterTest](#surefire--org.apache.commons.beanutils2.converters.offsettimeconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |
|  | [ArrayConverterTest](#surefire--org.apache.commons.beanutils2.converters.arrayconvertertest) | 7 | 0 | 0 | 0 | 100% | 0.043 s |
|  | [PathConverterTest](#surefire--org.apache.commons.beanutils2.converters.pathconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |
|  | [DimensionConverterTest](#surefire--org.apache.commons.beanutils2.converters.dimensionconvertertest) | 5 | 0 | 0 | 0 | 100% | 0.037 s |
|  | [LocalDateTimeConverterTest](#surefire--org.apache.commons.beanutils2.converters.localdatetimeconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.047 s |
|  | [ShortConverterTest](#surefire--org.apache.commons.beanutils2.converters.shortconvertertest) | 21 | 0 | 0 | 0 | 100% | 0.056 s |
|  | [LocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.localeconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |
|  | [OffsetDateTimeConverterTest](#surefire--org.apache.commons.beanutils2.converters.offsetdatetimeconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.046 s |
|  | [ByteConverterTest](#surefire--org.apache.commons.beanutils2.converters.byteconvertertest) | 21 | 0 | 0 | 0 | 100% | 0.057 s |
|  | [BigIntegerConverterTest](#surefire--org.apache.commons.beanutils2.converters.bigintegerconvertertest) | 20 | 0 | 0 | 0 | 100% | 0.055 s |
|  | [DoubleConverterTest](#surefire--org.apache.commons.beanutils2.converters.doubleconvertertest) | 20 | 0 | 0 | 0 | 100% | 0.054 s |
|  | [DateLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.datelocaleconvertertest) | 13 | 0 | 0 | 0 | 100% | 0.058 s |
|  | [LongConverterTest](#surefire--org.apache.commons.beanutils2.converters.longconvertertest) | 20 | 0 | 0 | 0 | 100% | 0.056 s |
|  | [BigIntegerLocaleConverterTest](#surefire--org.apache.commons.beanutils2.converters.bigintegerlocaleconvertertest) | 9 | 0 | 0 | 0 | 100% | 0.044 s |
|  | [LocalDateConverterTest](#surefire--org.apache.commons.beanutils2.converters.localdateconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [ClassReloaderTest](#surefire--org.apache.commons.beanutils2.converters.classreloadertest) | 1 | 0 | 0 | 0 | 100% | 0.018 s |
|  | [LocalTimeConverterTest](#surefire--org.apache.commons.beanutils2.converters.localtimeconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |
|  | [ZoneOffsetConverterTest](#surefire--org.apache.commons.beanutils2.converters.zoneoffsetconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.026 s |
|  | [URIConverterTest](#surefire--org.apache.commons.beanutils2.converters.uriconvertertest) | 2 | 0 | 0 | 0 | 100% | 0.028 s |

<a id="surefire--org.apache.commons.beanutils2.memoryleaktests"></a>

### org.apache.commons.beanutils2.memoryleaktests

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [MemoryLeakTest](#surefire--org.apache.commons.beanutils2.memoryleaktests.memoryleaktest) | 8 | 0 | 0 | 0 | 100% | 10.35 s |

<a id="surefire--org.apache.commons.beanutils2.sql"></a>

### org.apache.commons.beanutils2.sql

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [DynaRowSetTest](#surefire--org.apache.commons.beanutils2.sql.dynarowsettest) | 9 | 0 | 0 | 0 | 100% | 0.046 s |
|  | [DynaResultSetTest](#surefire--org.apache.commons.beanutils2.sql.dynaresultsettest) | 7 | 0 | 0 | 0 | 100% | 0.042 s |

<a id="surefire--org.apache.commons.beanutils2.bugs"></a>

### org.apache.commons.beanutils2.bugs

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [Jira493Test](#surefire--org.apache.commons.beanutils2.bugs.jira493test) | 1 | 0 | 0 | 0 | 100% | 0.044 s |
|  | [Jira520Test](#surefire--org.apache.commons.beanutils2.bugs.jira520test) | 2 | 0 | 0 | 0 | 100% | 0.047 s |
|  | [Jira458Test](#surefire--org.apache.commons.beanutils2.bugs.jira458test) | 2 | 0 | 0 | 0 | 100% | 0.036 s |
|  | [Jira422bTest](#surefire--org.apache.commons.beanutils2.bugs.jira422btest) | 2 | 0 | 0 | 0 | 100% | 0.047 s |
|  | [Jira18Test](#surefire--org.apache.commons.beanutils2.bugs.jira18test) | 12 | 0 | 0 | 0 | 100% | 0.056 s |
|  | [Jira381Test](#surefire--org.apache.commons.beanutils2.bugs.jira381test) | 1 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [Jira87Test](#surefire--org.apache.commons.beanutils2.bugs.jira87test) | 1 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [Jira422Test](#surefire--org.apache.commons.beanutils2.bugs.jira422test) | 0 | 0 | 0 | 0 | 0% | 0.017 s |
|  | [Jira492Test](#surefire--org.apache.commons.beanutils2.bugs.jira492test) | 8 | 0 | 0 | 0 | 100% | 0.052 s |
|  | [Jira339Test](#surefire--org.apache.commons.beanutils2.bugs.jira339test) | 2 | 0 | 0 | 0 | 100% | 0.050 s |
|  | [Jira541Test](#surefire--org.apache.commons.beanutils2.bugs.jira541test) | 2 | 0 | 0 | 0 | 100% | 0.132 s |
|  | [Jira359Test](#surefire--org.apache.commons.beanutils2.bugs.jira359test) | 4 | 0 | 0 | 0 | 100% | 0.050 s |
|  | [Jira349Test](#surefire--org.apache.commons.beanutils2.bugs.jira349test) | 1 | 0 | 0 | 0 | 100% | 0.051 s |
|  | [Jira157Test](#surefire--org.apache.commons.beanutils2.bugs.jira157test) | 3 | 0 | 0 | 0 | 100% | 0.053 s |
|  | [Jira298Test](#surefire--org.apache.commons.beanutils2.bugs.jira298test) | 3 | 0 | 0 | 0 | 100% | 0.051 s |
|  | [Jira358Test](#surefire--org.apache.commons.beanutils2.bugs.jira358test) | 2 | 0 | 0 | 0 | 100% | 0.050 s |
|  | [Jira465Test](#surefire--org.apache.commons.beanutils2.bugs.jira465test) | 4 | 0 | 0 | 0 | 100% | 0.056 s |
|  | [Jira61Test](#surefire--org.apache.commons.beanutils2.bugs.jira61test) | 16 | 0 | 0 | 0 | 100% | 0.069 s |
|  | [Jira456Test](#surefire--org.apache.commons.beanutils2.bugs.jira456test) | 2 | 0 | 0 | 0 | 100% | 0.035 s |
|  | [Jira509Test](#surefire--org.apache.commons.beanutils2.bugs.jira509test) | 1 | 0 | 0 | 1 | 0% | 0.001 s |
|  | [EnumDeclaringClassTest](#surefire--org.apache.commons.beanutils2.bugs.enumdeclaringclasstest) | 4 | 0 | 0 | 0 | 100% | 0.051 s |
|  | [Jira345Test](#surefire--org.apache.commons.beanutils2.bugs.jira345test) | 2 | 0 | 0 | 0 | 100% | 0.046 s |
|  | [Jira411Test](#surefire--org.apache.commons.beanutils2.bugs.jira411test) | 1 | 0 | 0 | 0 | 100% | 0.042 s |
|  | [Jira463Test](#surefire--org.apache.commons.beanutils2.bugs.jira463test) | 1 | 0 | 0 | 0 | 100% | 0.047 s |
|  | [Jira347Test](#surefire--org.apache.commons.beanutils2.bugs.jira347test) | 1 | 0 | 0 | 0 | 100% | 1.249 s |
|  | [Jira357Test](#surefire--org.apache.commons.beanutils2.bugs.jira357test) | 3 | 0 | 0 | 0 | 100% | 0.050 s |
|  | [Jira368Test](#surefire--org.apache.commons.beanutils2.bugs.jira368test) | 1 | 0 | 0 | 0 | 100% | 0.042 s |
|  | [Jira454Test](#surefire--org.apache.commons.beanutils2.bugs.jira454test) | 1 | 0 | 0 | 0 | 100% | 0.048 s |
|  | [Jira369Test](#surefire--org.apache.commons.beanutils2.bugs.jira369test) | 3 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [Jira273Test](#surefire--org.apache.commons.beanutils2.bugs.jira273test) | 6 | 0 | 0 | 0 | 100% | 0.053 s |
|  | [Jira92Test](#surefire--org.apache.commons.beanutils2.bugs.jira92test) | 1 | 0 | 0 | 0 | 100% | 0.049 s |

<a id="surefire--org.apache.commons.beanutils2"></a>

### org.apache.commons.beanutils2

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [BeanMapTest](#surefire--org.apache.commons.beanutils2.beanmaptest) | 54 | 0 | 0 | 3 | 94.4% | 0.082 s |
|  | [BeanComparatorTest](#surefire--org.apache.commons.beanutils2.beancomparatortest) | 8 | 0 | 0 | 0 | 100% | 0.055 s |
|  | [LazyDynaBeanTest](#surefire--org.apache.commons.beanutils2.lazydynabeantest) | 16 | 0 | 0 | 0 | 100% | 0.055 s |
|  | [DynaBeanUtilsTest](#surefire--org.apache.commons.beanutils2.dynabeanutilstest) | 29 | 0 | 0 | 0 | 100% | 0.078 s |
|  | [PropertyUtilsTest](#surefire--org.apache.commons.beanutils2.propertyutilstest) | 116 | 0 | 0 | 0 | 100% | 0.188 s |
|  | [BeanPredicateTest](#surefire--org.apache.commons.beanutils2.beanpredicatetest) | 4 | 0 | 0 | 0 | 100% | 0.055 s |
|  | [MappedPropertyTest](#surefire--org.apache.commons.beanutils2.mappedpropertytest) | 17 | 0 | 0 | 0 | 100% | 0.061 s |
|  | [DefaultIntrospectionContextTest](#surefire--org.apache.commons.beanutils2.defaultintrospectioncontexttest) | 9 | 0 | 0 | 0 | 100% | 0.027 s |
|  | [BeanToPropertyValueTransformerTest](#surefire--org.apache.commons.beanutils2.beantopropertyvaluetransformertest) | 17 | 0 | 0 | 0 | 100% | 0.062 s |
|  | [LazyDynaMapTest](#surefire--org.apache.commons.beanutils2.lazydynamaptest) | 17 | 0 | 0 | 0 | 100% | 0.053 s |
|  | [WrapDynaBeanTest](#surefire--org.apache.commons.beanutils2.wrapdynabeantest) | 43 | 0 | 0 | 0 | 100% | 0.101 s |
|  | [BeanPropertyValueChangeConsumerTest](#surefire--org.apache.commons.beanutils2.beanpropertyvaluechangeconsumertest) | 26 | 0 | 0 | 0 | 100% | 0.074 s |
|  | [LazyDynaClassTest](#surefire--org.apache.commons.beanutils2.lazydynaclasstest) | 15 | 0 | 0 | 0 | 100% | 0.033 s |
|  | [BeanPropertyValueEqualsPredicateTest](#surefire--org.apache.commons.beanutils2.beanpropertyvalueequalspredicatetest) | 17 | 0 | 0 | 0 | 100% | 0.062 s |
|  | [DynaPropertyUtilsTest](#surefire--org.apache.commons.beanutils2.dynapropertyutilstest) | 55 | 0 | 0 | 0 | 100% | 0.090 s |
|  | [LazyDynaListTest](#surefire--org.apache.commons.beanutils2.lazydynalisttest) | 15 | 0 | 0 | 0 | 100% | 0.084 s |
|  | [MethodUtilsTest](#surefire--org.apache.commons.beanutils2.methodutilstest) | 32 | 0 | 0 | 0 | 100% | 0.053 s |
|  | [ConstructorUtilsTest](#surefire--org.apache.commons.beanutils2.constructorutilstest) | 11 | 0 | 0 | 0 | 100% | 0.038 s |
|  | [FluentPropertyBeanIntrospectorTest](#surefire--org.apache.commons.beanutils2.fluentpropertybeanintrospectortest) | 3 | 0 | 0 | 0 | 100% | 0.037 s |
|  | [BeanUtilsBeanTest](#surefire--org.apache.commons.beanutils2.beanutilsbeantest) | 57 | 0 | 0 | 0 | 100% | 0.122 s |
|  | [BeanIntrospectionDataTest](#surefire--org.apache.commons.beanutils2.beanintrospectiondatatest) | 4 | 0 | 0 | 0 | 100% | 0.036 s |
|  | [BeanificationTest](#surefire--org.apache.commons.beanutils2.beanificationtest) | 8 | 0 | 0 | 0 | 100% | 0.103 s |
|  | [BasicDynaBeanTest](#surefire--org.apache.commons.beanutils2.basicdynabeantest) | 35 | 0 | 0 | 0 | 100% | 0.060 s |
|  | [ConvertUtilsTest](#surefire--org.apache.commons.beanutils2.convertutilstest) | 13 | 0 | 0 | 0 | 100% | 0.076 s |
|  | [DynaBeanMapDecoratorTest](#surefire--org.apache.commons.beanutils2.dynabeanmapdecoratortest) | 13 | 0 | 0 | 0 | 100% | 0.030 s |
|  | [IndexedPropertyTest](#surefire--org.apache.commons.beanutils2.indexedpropertytest) | 29 | 0 | 0 | 2 | 93.1% | 0.077 s |
|  | [PropertyUtilsBeanTest](#surefire--org.apache.commons.beanutils2.propertyutilsbeantest) | 4 | 0 | 0 | 0 | 100% | 0.033 s |
|  | [DynaPropertyTest](#surefire--org.apache.commons.beanutils2.dynapropertytest) | 2 | 0 | 0 | 0 | 100% | 0.018 s |
|  | [SuppressPropertiesBeanIntrospectorTest](#surefire--org.apache.commons.beanutils2.suppresspropertiesbeanintrospectortest) | 4 | 0 | 0 | 0 | 100% | 0.022 s |

<a id="surefire--org.apache.commons.beanutils2.locale"></a>

### org.apache.commons.beanutils2.locale

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [LocaleConvertUtilsTest](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest) | 12 | 0 | 0 | 6 | 50.0% | 0.066 s |
|  | [LocaleBeanificationTest](#surefire--org.apache.commons.beanutils2.locale.localebeanificationtest) | 9 | 0 | 0 | 0 | 100% | 0.125 s |
|  | [LocaleBeanUtilsTest](#surefire--org.apache.commons.beanutils2.locale.localebeanutilstest) | 2 | 0 | 0 | 0 | 100% | 0.066 s |

<a id="surefire--org.apache.commons.beanutils2.sql.converters"></a>

### org.apache.commons.beanutils2.sql.converters

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [SqlTimeConverterTest](#surefire--org.apache.commons.beanutils2.sql.converters.sqltimeconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.048 s |
|  | [SqlDateConverterTest](#surefire--org.apache.commons.beanutils2.sql.converters.sqldateconvertertest) | 12 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [SqlTimestampConverterTest](#surefire--org.apache.commons.beanutils2.sql.converters.sqltimestampconvertertest) | 11 | 0 | 0 | 0 | 100% | 0.050 s |

<a id="surefire--test-cases"></a>

## Test Cases

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

<a id="surefire--jira493test"></a>

### Jira493Test

|  |  |  |
| --- | --- | --- |
|  | testIndexedProperties | 0.033 s |

<a id="surefire--floatlocaleconvertertest"></a>

### FloatLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.028 s |
|  | testParseZero | 0.021 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0.001 s |
|  | testConstructor\_6 | 0.001 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0.001 s |
|  | testFloatLimits | 0.002 s |

<a id="surefire--sqltimeconvertertest"></a>

### SqlTimeConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.026 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.002 s |
|  | testDefaultType | 0 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.001 s |
|  | testStringConversion | 0.002 s |
|  | testMultiplePatterns | 0.001 s |
|  | testDefaultStringToTypeConvert | 0.001 s |
|  | testLocale | 0.003 s |

<a id="surefire--memoryleaktest"></a>

### MemoryLeakTest

|  |  |  |
| --- | --- | --- |
|  | testPropertyUtilsBean\_descriptorsCache\_memoryLeak | 1.337 s |
|  | testPropertyUtilsBean\_mappedDescriptorsCache\_memoryLeak | 1.315 s |
|  | testMappedPropertyDescriptor\_MappedMethodReference1 | 1.301 s |
|  | testMappedPropertyDescriptor\_MappedMethodReference2 | 1.295 s |
|  | testLocaleConvertUtilsBean\_converters\_memoryLeak | 1.292 s |
|  | testWrapDynaClass\_dynaClasses\_memoryLeak | 1.158 s |
|  | testMethodUtils\_cache\_memoryLeak | 1.309 s |
|  | testConvertUtilsBean\_converters\_memoryLeak | 1.317 s |

<a id="surefire--beanmaptest"></a>

### BeanMapTest

|  |  |  |
| --- | --- | --- |
|  | testObjectEqualsSelf | 0.010 s |
|  | testCanonicalFullCollectionExists | 0 s |
|  | testEqualsNull | 0.001 s |
|  | testCanonicalEmptyCollectionExists | 0.001 s |
|  | testSimpleSerialization | 0 s |
|  | testObjectHashCodeEqualsContract | 0.001 s |
|  | testObjectHashCodeEqualsSelfHashCode | 0.001 s |
|  | testSerializeDeserializeThenCompare | 0 s |
|  | [testReplaceKeyValueValue](#surefire--org.apache.commons.beanutils2.beanmaptest.testreplacekeyvaluevalue) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.BeanMapTest.testReplaceKeyValueValue');) | 0 s |
| - | skipped | - |
|  | testEntrySetContains1 | 0.004 s |
|  | testEntrySetContains2 | 0 s |
|  | testEntrySetContains3 | 0.002 s |
|  | testSampleMappings | 0 s |
|  | testValuesIteratorRemoveChangesMap | 0.002 s |
|  | testEntrySetRemoveChangesMap | 0.001 s |
|  | testValuesRetainAll | 0.001 s |
|  | testMapHashCode | 0 s |
|  | testForEach | 0 s |
|  | testEntrySetRemove1 | 0 s |
|  | testEntrySetRemove2 | 0 s |
|  | testEntrySetRemove3 | 0 s |
|  | testKeySetClearChangesMap | 0.001 s |
|  | testMapComputeIfPresent | 0 s |
|  | testValuesRemoveChangesMap | 0.001 s |
|  | testEntrySetRemoveAll | 0 s |
|  | testEntrySetIteratorRemoveChangesMap | 0.001 s |
|  | testEntrySetClearChangesMap | 0 s |
|  | testMapPutNullValue | 0 s |
|  | testKeySetRemoveChangesMap | 0 s |
|  | testMapContainsKey | 0.001 s |
|  | testKeySetRemoveAll | 0.001 s |
|  | testMapComputeIfPresentOnEmpty | 0.001 s |
|  | testMakeMap | 0.001 s |
|  | testMapSize | 0 s |
|  | testMapPutIfAbsent | 0.016 s |
|  | testMapPutNullKey | 0 s |
|  | testEmptyMapCompatibility | 0.001 s |
|  | [testReplaceKeyValue](#surefire--org.apache.commons.beanutils2.beanmaptest.testreplacekeyvalue) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.BeanMapTest.testReplaceKeyValue');) | 0 s |
| - | skipped | - |
|  | testFullMapCompatibility | 0 s |
|  | testMapToString | 0.001 s |
|  | testMapEquals | 0.001 s |
|  | testEntrySetRetainAll | 0.001 s |
|  | testMapComputeIfAbsent | 0.003 s |
|  | testMapIsEmpty | 0 s |
|  | testValuesRemoveAll | 0.001 s |
|  | testMapPutAll | 0 s |
|  | testKeySetIteratorRemoveChangesMap | 0 s |
|  | testMapGet | 0.001 s |
|  | testMapRemove | 0.001 s |
|  | testMapContainsValue | 0 s |
|  | testKeySetRetainAll | 0 s |
|  | [testRemoveKeyValue](#surefire--org.apache.commons.beanutils2.beanmaptest.testremovekeyvalue) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.BeanMapTest.testRemoveKeyValue');) | 0 s |
| - | skipped | - |
|  | testValuesClearChangesMap | 0 s |
|  | testMapGetOrDefault | 0 s |

<a id="surefire--jira520test"></a>

### Jira520Test

|  |  |  |
| --- | --- | --- |
|  | testSuppressClassPropertyByDefault | 0.036 s |
|  | testAllowAccessToClassProperty | 0.002 s |

<a id="surefire--jira458test"></a>

### Jira458Test

|  |  |  |
| --- | --- | --- |
|  | testConversionWithNullDefaultEmptyString | 0.025 s |
|  | testConversionWithNullDefaultNullInput | 0.001 s |

<a id="surefire--fileconvertertest"></a>

### FileConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedTargetType | 0.015 s |
|  | testSimpleConversion | 0.002 s |

<a id="surefire--jira422btest"></a>

### Jira422bTest

|  |  |  |
| --- | --- | --- |
|  | testSecondChildBean | 0.036 s |
|  | testRootBean | 0.001 s |

<a id="surefire--jira18test"></a>

### Jira18Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_isWriteable | 0.034 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_getProperty\_Indexed | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_getProperty\_Mapped | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_setProperty | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_getProperty | 0 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_setProperty\_Mapped | 0 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_isReadable\_Mapped | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_isWriteable\_Mapped | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_isWriteable\_Indexed | 0 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_isReadable | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_setProperty\_Indexed | 0.001 s |
|  | testIssue\_BEANUTILS\_18\_PropertyUtils\_isReadable\_Indexed | 0 s |

<a id="surefire--beancomparatortest"></a>

### BeanComparatorTest

|  |  |  |
| --- | --- | --- |
|  | testCompareIdentical | 0.037 s |
|  | testCompareOnBooleanProperty | 0.003 s |
|  | testCompareWithNulls | 0.001 s |
|  | testCompareOnMissingProperty | 0.001 s |
|  | testCompareBeanAgainstSelf | 0 s |
|  | testSimpleCompareInverse | 0 s |
|  | testSetProperty | 0.002 s |
|  | testSimpleCompare | 0 s |

<a id="surefire--jira381test"></a>

### Jira381Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_381\_getMatchingAccessibleMethod | 0.015 s |

<a id="surefire--defaultresolvertest"></a>

### DefaultResolverTest

|  |  |  |
| --- | --- | --- |
|  | testGetIndex | 0.009 s |
|  | testNext | 0 s |
|  | testGetName | 0 s |
|  | testIsMapped | 0.001 s |
|  | testGetMapKey | 0.001 s |
|  | testRemove | 0.001 s |
|  | testIsIndexed | 0 s |

<a id="surefire--lazydynabeantest"></a>

### LazyDynaBeanTest

|  |  |  |
| --- | --- | --- |
|  | testIndexedObjectArray | 0.016 s |
|  | testIndexedDynaBeanArray | 0.002 s |
|  | testIndexedInvalidType | 0.001 s |
|  | testMappedInvalidType | 0.001 s |
|  | testSimpleProperty | 0.001 s |
|  | testIndexedPropertyRestricted | 0.001 s |
|  | testIndexedPrimitiveArray | 0 s |
|  | testNullProperty | 0 s |
|  | testIndexedPropertyUtils | 0.017 s |
|  | testSimplePropertyRestricted | 0.001 s |
|  | testMappedPropertyDefault | 0 s |
|  | testMappedPropertyUtils | 0 s |
|  | testMappedPropertyRestricted | 0.001 s |
|  | testIndexedPropertyDefault | 0.001 s |
|  | testIndexedLinkedList | 0 s |
|  | testMappedPropertyTreeMap | 0 s |

<a id="surefire--stringconvertertest"></a>

### StringConverterTest

|  |  |  |
| --- | --- | --- |
|  | testDefaultType | 0.009 s |
|  | testConvertToTypeString | 0.005 s |

<a id="surefire--dynabeanutilstest"></a>

### DynaBeanUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testGetNestedProperty | 0.041 s |
|  | testCopyPropertiesStandard | 0.003 s |
|  | testCopyPropertiesDynaBean | 0.001 s |
|  | testGetIndexedProperty1 | 0 s |
|  | testGetIndexedProperty2 | 0 s |
|  | testSetPropertyNullValues | 0.002 s |
|  | testSetPropertyOnPrimitiveWrappers | 0.001 s |
|  | testCopyPropertyNestedIndexedArray | 0.001 s |
|  | testCopyPropertyDouble | 0.001 s |
|  | testGetArrayProperty | 0.001 s |
|  | testCopyPropertyNestedMappedMap | 0 s |
|  | testPopulateArrayElements | 0 s |
|  | testPopulateMapped | 0.001 s |
|  | testPopulateNested | 0.003 s |
|  | testPopulateArrayProperties | 0 s |
|  | testPopulateScalar | 0 s |
|  | testCopyPropertyNestedSimple | 0 s |
|  | testCloneDynaBean | 0.001 s |
|  | testCopyPropertyByte | 0.001 s |
|  | testCopyPropertyLong | 0.001 s |
|  | testCopyPropertyNull | 0 s |
|  | testSetPropertyNull | 0 s |
|  | testCopyPropertyInteger | 0.001 s |
|  | testCopyPropertiesMap | 0 s |
|  | testDescribe | 0 s |
|  | testGetSimpleProperty | 0.001 s |
|  | testGetGeneralProperty | 0 s |
|  | testCopyPropertyFloat | 0 s |
|  | testCopyPropertyShort | 0.001 s |

<a id="surefire--propertyutilstest"></a>

### PropertyUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testMapExtensionCustom | 0.048 s |
|  | testGetDescriptorArguments | 0.001 s |
|  | testGetNestedString | 0.003 s |
|  | testGetDescriptorLong | 0.002 s |
|  | testGetIndexedMap | 0.001 s |
|  | testGetSetParentBean | 0.002 s |
|  | testSetNestedUnknown | 0.002 s |
|  | testAddBeanIntrospectorNull | 0.001 s |
|  | testGetSetInnerBean | 0.002 s |
|  | testSetIndexedList | 0.002 s |
|  | testSetSimpleBoolean | 0.002 s |
|  | testSetPublicSubBean\_of\_PackageBean | 0.001 s |
|  | testGetNestedReadOnly | 0.001 s |
|  | testGetWriteMethodPackageSubclass | 0.002 s |
|  | testGetPublicSubBean\_of\_PackageBean | 0.002 s |
|  | testGetSimpleArguments | 0 s |
|  | testGetDescriptorInt | 0.001 s |
|  | testGetIndexedArray | 0.002 s |
|  | testGetMappedMap | 0.001 s |
|  | testSetNestedBoolean | 0.001 s |
|  | testSetNestedDouble | 0.002 s |
|  | testGetDescriptorWriteOnly | 0.002 s |
|  | testGetWriteMethodPublicSubclass | 0.001 s |
|  | testSetIndexedMap | 0.001 s |
|  | testSetNestedFloat | 0.002 s |
|  | testSetNestedShort | 0.001 s |
|  | testGetSimpleInt | 0.001 s |
|  | testSetNestedString | 0.001 s |
|  | testGetSimpleWriteOnly | 0.001 s |
|  | testExceptionFromInvoke | 0.002 s |
|  | testIsWriteable | 0.001 s |
|  | testGetDescriptorReadOnly | 0 s |
|  | testGetReadMethodPublicSubclass | 0.002 s |
|  | testGetReadMethodPackageSubclass | 0.001 s |
|  | testSetSimpleFloat | 0.001 s |
|  | testSetSimpleShort | 0 s |
|  | testSetSimpleArguments | 0 s |
|  | testCustomIntrospectionEx | 0.003 s |
|  | testSetNestedInt | 0.001 s |
|  | testSetIndexedArray | 0.001 s |
|  | testGetMappedList | 0.001 s |
|  | testGetDescriptorMappedPeriods | 0.001 s |
|  | testSetMappedPeriods | 0.001 s |
|  | testGetIndexedValues | 0.003 s |
|  | testCustomIntrospection | 0.001 s |
|  | testGetSimpleDouble | 0.001 s |
|  | testGetSimpleUnknown | 0.001 s |
|  | testGetReadMethodPublicInterface | 0.001 s |
|  | testGetMappedSlashes | 0.001 s |
|  | testSetSimpleWriteOnly | 0.001 s |
|  | testSetMappedArray | 0.001 s |
|  | testGetDescriptorFloat | 0.001 s |
|  | testGetDescriptorShort | 0.001 s |
|  | testMappedPropertyType | 0 s |
|  | testGetSimpleNested | 0.001 s |
|  | testGetIndexedList | 0.001 s |
|  | testGetNestedUnknown | 0.001 s |
|  | testSetMappedMap | 0.001 s |
|  | testGetNestedArguments | 0 s |
|  | testGetSimpleBoolean | 0 s |
|  | testSetSimpleIndexed | 0.001 s |
|  | testGetMappedValues | 0.001 s |
|  | testGetSimpleString | 0.001 s |
|  | testSetMappedList | 0.001 s |
|  | testGetDescriptorInvalidBoolean | 0.001 s |
|  | testGetSimpleLong | 0.001 s |
|  | testGetWriteMethodBasic | 0.001 s |
|  | testGetNestedBoolean | 0.001 s |
|  | testSetSimpleInt | 0.001 s |
|  | testSetIndexedArguments | 0.001 s |
|  | testSetSimpleDouble | 0.001 s |
|  | testGetPropertyType | 0.001 s |
|  | testGetNestedFloat | 0 s |
|  | testGetNestedShort | 0 s |
|  | testGetNestedWriteOnly | 0.001 s |
|  | testGetDescriptorDouble | 0 s |
|  | testNestedWithIndex | 0 s |
|  | testGetDescriptors | 0.001 s |
|  | testGetReadMethodBasic | 0 s |
|  | testGetNestedLong | 0.001 s |
|  | testSetSimpleNested | 0 s |
|  | testGetMappedArguments | 0.001 s |
|  | testSetNestedArguments | 0.001 s |
|  | testSetSimpleLong | 0.001 s |
|  | testGetSimpleFloat | 0.001 s |
|  | testGetSimpleShort | 0.001 s |
|  | testSetMappedValues | 0.001 s |
|  | testSetSimpleString | 0.001 s |
|  | testRemoveBeanIntrospector | 0 s |
|  | testGetDescriptorSecond | 0.001 s |
|  | testGetDescriptorString | 0 s |
|  | testGetDescriptorUnknown | 0.001 s |
|  | testSetSimpleReadOnly | 0.001 s |
|  | testGetMappedPeriods | 0.001 s |
|  | testNestedPropertyKeyOrIndexOnBeanImplementingMap | 0.005 s |
|  | testGetDescriptorBoolean | 0 s |
|  | testSetNestedLong | 0 s |
|  | testMapExtensionDefault | 0.001 s |
|  | testGetDescriptorsArguments | 0.001 s |
|  | testSetNestedWriteOnly | 0 s |
|  | testSetNestedReadOnly | 0.001 s |
|  | testSetNoGetter | 0.001 s |
|  | testGetMappedArray | 0.001 s |
|  | testCopyPropertiesMap | 0 s |
|  | testResetBeanIntrospectors | 0 s |
|  | testDescribe | 0.001 s |
|  | testSetMappedArguments | 0.001 s |
|  | testGetNestedDouble | 0.001 s |
|  | testGetSimpleIndexed | 0 s |
|  | testIsReadable | 0.001 s |
|  | testThrowNestedNull | 0.001 s |
|  | testGetSimpleReadOnly | 0.001 s |
|  | testGetIndexedArguments | 0.001 s |
|  | testSetIndexedValues | 0.002 s |
|  | testGetNestedInt | 0.001 s |
|  | testSetSimpleUnknown | 0.001 s |

<a id="surefire--beanpredicatetest"></a>

### BeanPredicateTest

|  |  |  |
| --- | --- | --- |
|  | testNotEqual | 0.042 s |
|  | testEqual | 0.001 s |
|  | testNull | 0.001 s |
|  | testInstanceOf | 0.001 s |

<a id="surefire--sqldateconvertertest"></a>

### SqlDateConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.027 s |
|  | testConvertNull | 0 s |
|  | testInvalidType | 0 s |
|  | testPatternDefault | 0.002 s |
|  | testDefaultType | 0.001 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.001 s |
|  | testLocale | 0.002 s |
|  | testStringConversion | 0.001 s |
|  | testMultiplePatterns | 0.002 s |
|  | testDefaultStringToTypeConvert | 0 s |
|  | testDefaultTypeToStringConvert | 0 s |

<a id="surefire--jira87test"></a>

### Jira87Test

|  |  |  |
| --- | --- | --- |
|  | testJira87 | 0.034 s |

<a id="surefire--enumconvertertest"></a>

### EnumConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--dynarowsettest"></a>

### DynaRowSetTest

|  |  |  |
| --- | --- | --- |
|  | testGetDynaProperty | 0.026 s |
|  | testListCount | 0.001 s |
|  | testGetName | 0 s |
|  | testInconsistentOracleDriver | 0.002 s |
|  | testListResults | 0.002 s |
|  | testLimitedRows | 0.001 s |
|  | testNewInstance | 0.002 s |
|  | testGetDynaProperties | 0.001 s |
|  | testListResultsNormalCase | 0.001 s |

<a id="surefire--mappedpropertytest"></a>

### MappedPropertyTest

|  |  |  |
| --- | --- | --- |
|  | testNotFound | 0.015 s |
|  | testMappedSetterOnly | 0.002 s |
|  | testFound | 0.001 s |
|  | testChildInterfaceMapped | 0.001 s |
|  | testAnyArgsProperty | 0.001 s |
|  | testBooleanMapped | 0 s |
|  | testPublicParentMethod | 0 s |
|  | testProtected | 0 s |
|  | testPrimitiveArgsProperty | 0.001 s |
|  | testDifferentTypes | 0.001 s |
|  | testInvalidGetter | 0 s |
|  | testInvalidSetter | 0 s |
|  | testMappedGetterOnly | 0.001 s |
|  | testProtectedParentMethod | 0.001 s |
|  | testMapGetter | 0.023 s |
|  | testInterfaceNotFound | 0.001 s |
|  | testInterfaceMapped | 0 s |

<a id="surefire--integerlocaleconvertertest"></a>

### IntegerLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.027 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0.001 s |
|  | testConstructor\_6 | 0.001 s |
|  | testConstructor\_7 | 0 s |
|  | testConstructor\_8 | 0 s |
|  | testConstructor\_9 | 0.001 s |
|  | testToPrimitiveType | 0.001 s |
|  | testNumber | 0 s |

<a id="surefire--dateconvertertest"></a>

### DateConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.026 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.003 s |
|  | testDefaultStringToTypeConvert | 0 s |
|  | testDefaultType | 0 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.002 s |
|  | testLocale | 0.001 s |
|  | testStringConversion | 0.001 s |
|  | testMultiplePatterns | 0.001 s |

<a id="surefire--bigdecimalconvertertest"></a>

### BigDecimalConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.014 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0.001 s |
|  | testStringToNumberPattern | 0.013 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0.001 s |
|  | testInvalidTypeWithDefault | 0.001 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0.001 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0.001 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0 s |
|  | testStringToNumberDefault | 0 s |
|  | testStringToNumberLocale | 0.001 s |
|  | testNumberToStringDefault | 0.001 s |
|  | testOtherToStringDefault | 0.001 s |
|  | testDateToNumber | 0.001 s |
|  | testSimpleConversion | 0 s |

<a id="surefire--yearmonthconvertertest"></a>

### YearMonthConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.003 s |

<a id="surefire--calendarconvertertest"></a>

### CalendarConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.026 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.003 s |
|  | testDefaultStringToTypeConvert | 0 s |
|  | testDefaultType | 0 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.001 s |
|  | testLocale | 0.001 s |
|  | testStringConversion | 0.002 s |
|  | testMultiplePatterns | 0.001 s |

<a id="surefire--bytelocaleconvertertest"></a>

### ByteLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.027 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0.001 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0 s |
|  | testConstructor\_6 | 0 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0.001 s |

<a id="surefire--defaultintrospectioncontexttest"></a>

### DefaultIntrospectionContextTest

|  |  |  |
| --- | --- | --- |
|  | testAddPropertyDescriptor | 0.009 s |
|  | testAddPropertyDescriptors | 0.001 s |
|  | testInit | 0.001 s |
|  | testHasPropertyFalse | 0 s |
|  | testPropertyNamesModify | 0.001 s |
|  | testRemovePropertyDescriptor | 0 s |
|  | testGetPropertyDescriptorUnknown | 0 s |
|  | testAddPropertyDescriptorsNull | 0.001 s |
|  | testAddPropertyDescriptorNull | 0.001 s |

<a id="surefire--beantopropertyvaluetransformertest"></a>

### BeanToPropertyValueTransformerTest

|  |  |  |
| --- | --- | --- |
|  | testTransformWithNullInPath | 0.038 s |
|  | testTransformWithReadOnlyProperty | 0.001 s |
|  | testTransformWithSimpleBooleanProperty | 0.001 s |
|  | testTransformWithSimpleStringProperty | 0 s |
|  | testTransformWithSimpleIntProperty | 0 s |
|  | testTransformWithSimpleDoubleProperty | 0.001 s |
|  | testTransformWithNestedIndexedProperty | 0.001 s |
|  | testTransformWithIndexedProperty | 0 s |
|  | testTransformWithSimpleFloatProperty | 0.001 s |
|  | testTransformWithNullInPathAndIgnoreTrue | 0.002 s |
|  | testTransformWithMappedProperty | 0.001 s |
|  | testTransformWithNestedProperty | 0 s |
|  | testTransformWithSimpleLongProperty | 0.001 s |
|  | testTransformWithSimpleByteProperty | 0.001 s |
|  | testTransformWithSimpleStringPropertyAndNullValue | 0 s |
|  | testTransformWithInvalidProperty | 0 s |
|  | testTransformWithWriteOnlyProperty | 0.001 s |

<a id="surefire--patternconvertertest"></a>

### PatternConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertingPattern | 0.014 s |

<a id="surefire--pointconvertertest"></a>

### PointConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertingNoSpace | 0.014 s |
|  | testConvertingPoint | 0.001 s |

<a id="surefire--jira492test"></a>

### Jira492Test

|  |  |  |
| --- | --- | --- |
|  | getPropertyUnconverted | 0.013 s |
|  | getPropertyDescriptor | 0.001 s |
|  | getPropertySubScript | 0.001 s |
|  | getIndexedProperty | 0.001 s |
|  | setIndexedProperty | 0.001 s |
|  | getPropertyType | 0 s |
|  | describe | 0 s |
|  | getProperty | 0.001 s |

<a id="surefire--uuidconvertertest"></a>

### UUIDConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.017 s |
|  | testSimpleConversion | 0.002 s |

<a id="surefire--lazydynamaptest"></a>

### LazyDynaMapTest

|  |  |  |
| --- | --- | --- |
|  | testIndexedObjectArray | 0.016 s |
|  | testIndexedDynaBeanArray | 0 s |
|  | testIndexedInvalidType | 0.001 s |
|  | testMappedInvalidType | 0 s |
|  | testSimpleProperty | 0 s |
|  | testIndexedPropertyRestricted | 0.001 s |
|  | testGeneral | 0.001 s |
|  | testIndexedPrimitiveArray | 0.001 s |
|  | testIndexedPropertyUtils | 0.017 s |
|  | testSimplePropertyRestricted | 0 s |
|  | testMappedPropertyDefault | 0 s |
|  | testMappedPropertyUtils | 0.001 s |
|  | testNewInstance | 0 s |
|  | testMappedPropertyRestricted | 0 s |
|  | testIndexedPropertyDefault | 0 s |
|  | testIndexedLinkedList | 0.001 s |
|  | testMappedPropertyTreeMap | 0 s |

<a id="surefire--booleanconvertertest"></a>

### BooleanConverterTest

|  |  |  |
| --- | --- | --- |
|  | testAdditionalStrings | 0.014 s |
|  | testCaseInsensitivity | 0 s |
|  | testDefaultValue | 0 s |
|  | testConversionToOtherType | 0 s |
|  | testInvalidString | 0 s |
|  | testStandardValues | 0 s |
|  | testPrimitiveTargetClass | 0.001 s |

<a id="surefire--jira339test"></a>

### Jira339Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_339\_BeanUtilsBean\_setProperty | 0.033 s |
|  | testIssue\_BEANUTILS\_331\_BeanUtilsBean\_populate | 0.001 s |

<a id="surefire--wrapdynabeantest"></a>

### WrapDynaBeanTest

|  |  |  |
| --- | --- | --- |
|  | testGetDescriptorArguments | 0.040 s |
|  | testGetDescriptorLong | 0.001 s |
|  | testSetSimpleBoolean | 0.002 s |
|  | testGetSimpleArguments | 0.001 s |
|  | testGetDescriptorInt | 0.001 s |
|  | testGetSimpleInt | 0 s |
|  | testSetSimpleFloat | 0.001 s |
|  | testSetSimpleShort | 0 s |
|  | testGetIndexedValues | 0.002 s |
|  | testGetSimpleDouble | 0.001 s |
|  | testGetDescriptorFloat | 0 s |
|  | testGetDescriptorShort | 0.001 s |
|  | testGetSimpleBoolean | 0.001 s |
|  | testGetMappedValues | 0.001 s |
|  | testGetSimpleString | 0 s |
|  | testGetSimpleLong | 0 s |
|  | testSetSimpleInt | 0 s |
|  | testSetIndexedArguments | 0.001 s |
|  | testSetSimpleDouble | 0.001 s |
|  | testGetDescriptorDouble | 0.001 s |
|  | testGetDescriptors | 0.001 s |
|  | testGetMappedArguments | 0 s |
|  | testSetSimpleLong | 0.001 s |
|  | testGetSimpleFloat | 0 s |
|  | testGetSimpleShort | 0 s |
|  | testSetMappedValues | 0.001 s |
|  | testSetSimpleString | 0.001 s |
|  | testGetDescriptorSecond | 0 s |
|  | testGetDescriptorString | 0.001 s |
|  | testGetDescriptorBoolean | 0 s |
|  | testGetIndexedArguments | 0 s |
|  | testSetIndexedValues | 0.001 s |
|  | testIntrospectionWithCustomPropUtils | 0.002 s |
|  | testNotSerializableException | 0.017 s |
|  | testGetWrapDynaClassFromCacheWithPropUtils | 0.001 s |
|  | testSimpleProperties | 0.001 s |
|  | testMappedRemove | 0.001 s |
|  | testMappedContains | 0 s |
|  | testIndexedProperties | 0.001 s |
|  | testGetWrapDynaClassFromCache | 0.001 s |
|  | testNewInstance | 0 s |
|  | testGetInstance | 0.001 s |
|  | testInitWithDynaClass | 0 s |

<a id="surefire--durationconvertertest"></a>

### DurationConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.016 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--dynaresultsettest"></a>

### DynaResultSetTest

|  |  |  |
| --- | --- | --- |
|  | testGetDynaProperty | 0.024 s |
|  | testGetName | 0.001 s |
|  | testIteratorResults | 0.002 s |
|  | testIteratorCount | 0.001 s |
|  | testNewInstance | 0.001 s |
|  | testGetDynaProperties | 0.001 s |
|  | testIteratorResultsNormalCase | 0 s |

<a id="surefire--beanpropertyvaluechangeconsumertest"></a>

### BeanPropertyValueChangeConsumerTest

|  |  |  |
| --- | --- | --- |
|  | testExecuteWithSimpleFloatPropertyAndDoubleValue | 0.041 s |
|  | testExecuteWithSimpleFloatPropertyAndStringValue | 0 s |
|  | testExecuteWithNullInPropertyPath | 0 s |
|  | testExecuteWithSimpleBytePropertyAndStringValue | 0.001 s |
|  | testExecuteWithSimpleBooleanPropertyAndBooleanValue | 0.001 s |
|  | testExecuteWithSimpleIntPropertyAndDoubleValue | 0.001 s |
|  | testExecuteWithMappedProperty | 0.002 s |
|  | testExecuteWithSimpleIntPropertyAndStringValue | 0.001 s |
|  | testExecuteWithNestedProperty | 0 s |
|  | testExecuteWithReadOnlyProperty | 0 s |
|  | testExecuteWithSimpleStringProperty | 0.001 s |
|  | testExecuteWithSimplePrimitivePropertyAndNullValue | 0 s |
|  | testExecuteWithSimpleFloatPropertyAndFloatValue | 0 s |
|  | testExecuteWithSimpleDoublePropertyAndIntegerValue | 0.001 s |
|  | testExecuteWithSimpleDoublePropertyAndFloatValue | 0 s |
|  | testExecuteWithSimpleFloatPropertyAndIntegerValue | 0.001 s |
|  | testExecuteWithSimpleIntPropertyAndIntegerValue | 0 s |
|  | testExecuteWithWriteOnlyProperty | 0.001 s |
|  | testExecuteWithNullInPropertyPathAngIgnoreTrue | 0.001 s |
|  | testExecuteWithSimpleBooleanPropertyAndStringValue | 0 s |
|  | testExecuteWithIndexedProperty | 0.001 s |
|  | testExecuteWithInvalidPropertyName | 0 s |
|  | testExecuteWithSimpleBytePropertyAndByteValue | 0 s |
|  | testExecuteWithSimpleDoublePropertyAndDoubleValue | 0 s |
|  | testExecuteWithSimpleIntPropertyAndFloatValue | 0 s |
|  | testExecuteWithSimpleDoublePropertyAndStringValue | 0.001 s |

<a id="surefire--lazydynaclasstest"></a>

### LazyDynaClassTest

|  |  |  |
| --- | --- | --- |
|  | testRemovePropertyDoesntExist | 0.010 s |
|  | testRemovePropertyNullName | 0.001 s |
|  | testAddPropertyRestricted1 | 0.001 s |
|  | testAddPropertyRestricted2 | 0.001 s |
|  | testAddPropertyRestricted3 | 0.001 s |
|  | testGetPropertyDoesntExist1 | 0.001 s |
|  | testGetPropertyDoesntExist2 | 0 s |
|  | testRemovePropertyRestricted | 0 s |
|  | testAddProperty1 | 0.001 s |
|  | testAddProperty2 | 0 s |
|  | testAddProperty3 | 0 s |
|  | testRemoveProperty | 0.001 s |
|  | testAddPropertyNullName1 | 0 s |
|  | testAddPropertyNullName2 | 0 s |
|  | testAddPropertyNullName3 | 0 s |

<a id="surefire--beanpropertyvalueequalspredicatetest"></a>

### BeanPropertyValueEqualsPredicateTest

|  |  |  |
| --- | --- | --- |
|  | testEvaluateWithIndexedProperty | 0.040 s |
|  | testEvaluateWithIntProperty | 0.001 s |
|  | testEvaluateWithReadOnlyProperty | 0 s |
|  | testEvaluateWithByteProperty | 0.001 s |
|  | testEvaluateWithMappedProperty | 0.001 s |
|  | testEvaluateWithNestedProperty | 0.001 s |
|  | testEvaluateWithNullInPath | 0.001 s |
|  | testEvaluateWithInvalidPropertyName | 0.001 s |
|  | testEvaluateWithPrimitiveAndNull | 0.001 s |
|  | testEvaluateWithSimpleStringProperty | 0 s |
|  | testEvaluateWithNullInPathAndIgnoreTrue | 0.001 s |
|  | testEvaluateWithDoubleProperty | 0.001 s |
|  | testEvaluateWithFloatProperty | 0 s |
|  | testEvaluateWithNestedMappedProperty | 0 s |
|  | testEvaluateWithBooleanProperty | 0 s |
|  | testEvaluateWithWriteOnlyProperty | 0 s |
|  | testEvaluateWithSimpleStringPropertyWithNullValues | 0 s |

<a id="surefire--dynapropertyutilstest"></a>

### DynaPropertyUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testGetNestedString | 0.040 s |
|  | testSetNestedUnknown | 0.001 s |
|  | testSetSimpleBoolean | 0 s |
|  | testGetNestedReadOnly | 0 s |
|  | testGetSimpleArguments | 0 s |
|  | testSetNestedBoolean | 0.002 s |
|  | testSetNestedDouble | 0.002 s |
|  | testSetNestedFloat | 0.001 s |
|  | testSetNestedShort | 0.001 s |
|  | testGetSimpleInt | 0.001 s |
|  | testSetNestedString | 0 s |
|  | testSetSimpleFloat | 0 s |
|  | testSetSimpleShort | 0.001 s |
|  | testSetSimpleArguments | 0 s |
|  | testSetNestedInt | 0 s |
|  | testGetIndexedValues | 0.001 s |
|  | testGetSimpleDouble | 0.001 s |
|  | testGetSimpleUnknown | 0 s |
|  | testGetMappedSlashes | 0.001 s |
|  | testGetSimpleNested | 0.001 s |
|  | testGetNestedUnknown | 0.001 s |
|  | testGetNestedArguments | 0.001 s |
|  | testGetSimpleBoolean | 0.001 s |
|  | testSetSimpleIndexed | 0 s |
|  | testGetMappedValues | 0.001 s |
|  | testGetSimpleString | 0 s |
|  | testGetSimpleLong | 0 s |
|  | testGetNestedBoolean | 0.001 s |
|  | testSetSimpleInt | 0 s |
|  | testSetIndexedArguments | 0.001 s |
|  | testSetSimpleDouble | 0 s |
|  | testGetNestedFloat | 0.001 s |
|  | testGetNestedShort | 0.001 s |
|  | testGetNestedLong | 0 s |
|  | testSetSimpleNested | 0.001 s |
|  | testGetMappedArguments | 0.001 s |
|  | testSetNestedArguments | 0 s |
|  | testSetSimpleLong | 0.001 s |
|  | testGetSimpleFloat | 0 s |
|  | testGetSimpleShort | 0 s |
|  | testSetMappedValues | 0 s |
|  | testSetSimpleString | 0 s |
|  | testGetMappedPeriods | 0 s |
|  | testSetNestedLong | 0.001 s |
|  | testSetNestedWriteOnly | 0.001 s |
|  | testSetNestedReadOnly | 0 s |
|  | testCopyPropertiesMap | 0.001 s |
|  | testDescribe | 0.001 s |
|  | testSetMappedArguments | 0.001 s |
|  | testGetNestedDouble | 0.001 s |
|  | testGetSimpleIndexed | 0 s |
|  | testGetIndexedArguments | 0.001 s |
|  | testSetIndexedValues | 0 s |
|  | testGetNestedInt | 0.001 s |
|  | testSetSimpleUnknown | 0 s |

<a id="surefire--lazydynalisttest"></a>

### LazyDynaListTest

|  |  |  |
| --- | --- | --- |
|  | testPojoDynaClass | 0.012 s |
|  | testDynaBeanDynaClass | 0.001 s |
|  | testSerializationMap | 0.018 s |
|  | testToArrayUnsufficientSize | 0.001 s |
|  | testToArrayDynaBeans | 0.001 s |
|  | testMapDynaClass | 0 s |
|  | testNullType | 0 s |
|  | testToArrayOtherType | 0.001 s |
|  | testSerializationLazyDynaBean | 0.002 s |
|  | testDynaBeanType | 0 s |
|  | testMapType | 0 s |
|  | testSerializationPojo | 0.001 s |
|  | testPojoType | 0 s |
|  | testToArrayMapType | 0.001 s |
|  | testSerializationDynaBean | 0.001 s |

<a id="surefire--jira541test"></a>

### Jira541Test

|  |  |  |
| --- | --- | --- |
|  | testFluentBeanIntrospectorOnOverriddenSetter | 0.024 s |
|  | testFluentBeanIntrospectorOnOverriddenSetterConcurrent | 0.096 s |

<a id="surefire--jira359test"></a>

### Jira359Test

|  |  |  |
| --- | --- | --- |
|  | testBeanUtilsSetProperty\_CustomConvertStringToArray\_WithColonValue | 0.036 s |
|  | testBeanUtilsSetProperty\_DefaultConvertStringToArray\_WithColonValue | 0.001 s |
|  | testBeanUtilsSetProperty\_DefaultConvertStringToArray\_WithoutColonValue | 0.001 s |
|  | testBeanUtilsSetProperty\_DefaultConvertStringToArray\_WithoutColonValueAndNocoma | 0.001 s |

<a id="surefire--jira349test"></a>

### Jira349Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_349\_PropertyUtils\_copyProperties | 0.035 s |

<a id="surefire--jira157test"></a>

### Jira157Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_157\_BeanUtils\_Describe\_Bean | 0.034 s |
|  | testIssue\_BEANUTILS\_157\_BeanUtils\_Describe\_Interface | 0.002 s |
|  | testIssue\_BEANUTILS\_157\_BeanUtils\_Describe\_Serializable | 0.001 s |

<a id="surefire--jira298test"></a>

### Jira298Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_298\_PropertyUtils\_setProperty | 0.034 s |
|  | testIssue\_BEANUTILS\_298\_PropertyUtils\_getProperty | 0 s |
|  | testIssue\_BEANUTILS\_298\_MethodUtils\_getAccessibleMethod | 0 s |

<a id="surefire--floatconvertertest"></a>

### FloatConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.014 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0.001 s |
|  | testStringToNumberPattern | 0.013 s |
|  | testNumberToStringPattern | 0.002 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0.001 s |
|  | testInvalidTypeWithDefault | 0 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0.001 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0 s |
|  | testStringToNumberLocale | 0 s |
|  | testNumberToStringDefault | 0 s |
|  | testOtherToStringDefault | 0.001 s |
|  | testDateToNumber | 0.002 s |
|  | testInvalidAmount | 0.001 s |
|  | testSimpleConversion | 0 s |

<a id="surefire--bigdecimallocaleconvertertest"></a>

### BigDecimalLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.030 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0.001 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0 s |
|  | testConstructor\_6 | 0.001 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0 s |

<a id="surefire--localeconvertutilstest"></a>

### LocaleConvertUtilsTest

|  |  |  |
| --- | --- | --- |
|  | [fixmetestPositiveArray](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest.fixmetestpositivearray) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.locale.LocaleConvertUtilsTest.fixmetestPositiveArray');) | 0 s |
| - | Array conversions not implemented yet. | - |
|  | testObjectToStringScalar | 0.044 s |
|  | [fixmetestPositiveIntegerArray](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest.fixmetestpositiveintegerarray) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.locale.LocaleConvertUtilsTest.fixmetestPositiveIntegerArray');) | 0 s |
| - | Array conversions not implemented yet. | - |
|  | testConvertStringLocaleNull | 0.001 s |
|  | [fixmetestNegativeStringArray](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest.fixmetestnegativestringarray) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.locale.LocaleConvertUtilsTest.fixmetestNegativeStringArray');) | 0 s |
| - | Array conversions not implemented yet. | - |
|  | [fixmetestPositiveStringArray](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest.fixmetestpositivestringarray) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.locale.LocaleConvertUtilsTest.fixmetestPositiveStringArray');) | 0 s |
| - | Array conversions not implemented yet. | - |
|  | [fixmetestNegativeIntegerArray](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest.fixmetestnegativeintegerarray) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.locale.LocaleConvertUtilsTest.fixmetestNegativeIntegerArray');) | 0 s |
| - | Array conversions not implemented yet. | - |
|  | [fixmetestObjectToStringArray](#surefire--org.apache.commons.beanutils2.locale.localeconvertutilstest.fixmetestobjecttostringarray) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.locale.LocaleConvertUtilsTest.fixmetestObjectToStringArray');) | 0 s |
| - | Array conversions not implemented yet. | - |
|  | testNegativeScalar | 0.001 s |
|  | testDefaultToStringConversionUnsupportedType | 0 s |
|  | testPositiveScalar | 0.004 s |
|  | testConvertStringArrayLocaleNull | 0 s |

<a id="surefire--methodutilstest"></a>

### MethodUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testInvokeMethodObject | 0.015 s |
|  | testInvokeMethodPrimitiveFloat | 0.002 s |
|  | testClearCache | 0.001 s |
|  | testInvokeMethodNull | 0.001 s |
|  | testInvokeExactMethodNull | 0 s |
|  | testInvokeMethodPrimitiveLong | 0.002 s |
|  | testInvokeMethodPrimitiveDouble | 0.001 s |
|  | testInvokeMethodArray | 0.001 s |
|  | testInvokeMethodPrimitiveInt | 0.001 s |
|  | testInvokeMethodUnknown | 0.001 s |
|  | testInvokeExactMethodFromInterface | 0.001 s |
|  | testInvokeExactStaticMethodNull | 0.002 s |
|  | testGetAccessibleMethodIndirectInterface | 0.001 s |
|  | testInvokeMethodPrimitiveBoolean | 0 s |
|  | testInvokeMethodNullArrayNullArray | 0 s |
|  | testInvokeStaticMethodNull | 0 s |
|  | testInvokeExactMethod | 0 s |
|  | testInvokeMethod | 0 s |
|  | testSetCacheMethods | 0.001 s |
|  | testInvokeExactMethodNullArrayNullArray | 0 s |
|  | testInvokeExactMethodIndirectInterface | 0.001 s |
|  | testInvokeExactMethodNullArray | 0.001 s |
|  | testGetAccessibleMethodFromInterface | 0 s |
|  | testStaticInvokeMethod | 0.001 s |
|  | testNoCaching | 0 s |
|  | testParentMethod | 0.001 s |
|  | testGetAccessibleMethod | 0 s |
|  | testPublicSub | 0 s |
|  | testSimpleStatic1 | 0.001 s |
|  | testSimpleStatic2 | 0 s |
|  | testSimpleStatic3 | 0.001 s |
|  | testInvokeMethodNullArray | 0 s |

<a id="surefire--periodconvertertest"></a>

### PeriodConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.002 s |

<a id="surefire--longlocaleconvertertest"></a>

### LongLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.028 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0 s |
|  | testConstructor\_6 | 0.001 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0.001 s |

<a id="surefire--jira358test"></a>

### Jira358Test

|  |  |  |
| --- | --- | --- |
|  | testPropertyUtils\_getIndexedProperty\_List | 0.039 s |
|  | testPropertyUtils\_getIndexedProperty\_Array | 0.001 s |

<a id="surefire--jira465test"></a>

### Jira465Test

|  |  |  |
| --- | --- | --- |
|  | testArrayProperty | 0.039 s |
|  | testListIndexedProperty | 0.002 s |
|  | testListProperty | 0.001 s |
|  | testArrayIndexedProperty | 0.001 s |

<a id="surefire--classconvertertest"></a>

### ClassConverterTest

|  |  |  |
| --- | --- | --- |
|  | testArray | 0.015 s |
|  | testUnsupportedTargetType | 0.001 s |
|  | testConvertToString | 0 s |
|  | testConvertToClass | 0.001 s |
|  | testConvertToClassDefault | 0.001 s |
|  | testConvertToClassDefaultNull | 0.001 s |
|  | testInvalid | 0 s |

<a id="surefire--colorconvertertest"></a>

### ColorConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertingJavaExtendsColorString | 0.022 s |
|  | testConvertingJavaColorStringWithoutBrackets | 0 s |
|  | testConvertingJavaColorStringWithoutColorPrefixes | 0 s |
|  | testConvertingPattern3Digit | 0 s |
|  | testConvertingPattern4Digit | 0.001 s |
|  | testConvertingPatternWithAlpha | 0 s |
|  | testConvertingPattern | 0.001 s |
|  | testConvertingJavaColorStringWithoutPackage | 0 s |
|  | testColorBlank | 0 s |
|  | testColorInvalidLength | 0 s |
|  | testInvalidNumber3 | 0.001 s |
|  | testInvalidNumber4 | 0 s |
|  | testConvertingJavaColorStringFull | 0.001 s |
|  | testConvertingColorNameCaps | 0 s |
|  | testConvertingColorName | 0 s |
|  | testConvertingLiteralHex | 0.001 s |

<a id="surefire--characterconvertertest"></a>

### CharacterConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertToChar | 0.015 s |
|  | testConvertToString | 0 s |
|  | testDefault | 0 s |
|  | testConvertToUnsupportedType | 0.001 s |
|  | testConvertToCharacterNullNoDefault | 0 s |
|  | testConvertToCharacter | 0 s |

<a id="surefire--doublelocaleconvertertest"></a>

### DoubleLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.027 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0.001 s |
|  | testConstructor\_6 | 0.001 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0 s |

<a id="surefire--jira61test"></a>

### Jira61Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_isWriteable\_Mapped | 0.007 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_copyProperties\_from\_WrapDynaBean | 0.002 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_isWriteable\_Indexed | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_BeanUtils\_copyProperties\_to\_WrapDynaBean | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_isWriteable | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_setProperty\_Indexed | 0.002 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_isReadable\_Indexed | 0 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_copyProperties\_to\_WrapDynaBean | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_isReadable\_Mapped | 0 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_setProperty | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_getProperty | 0 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_getProperty\_Indexed | 0 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_getProperty\_Mapped | 0 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_isReadable | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_BeanUtils\_copyProperties\_from\_WrapDynaBean | 0.001 s |
|  | testIssue\_BEANUTILS\_61\_PropertyUtils\_setProperty\_Mapped | 0.001 s |

<a id="surefire--zoneddatetimeconvertertest"></a>

### ZonedDateTimeConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.025 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.003 s |
|  | testDefaultStringToTypeConvert | 0.001 s |
|  | testDefaultType | 0 s |
|  | testPatternNullDefault | 0 s |
|  | testPatternNoDefault | 0.001 s |
|  | testLocale | 0.001 s |
|  | testStringConversion | 0.002 s |
|  | testMultiplePatterns | 0.001 s |

<a id="surefire--constructorutilstest"></a>

### ConstructorUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testInvokeExactConstructorWithArgArray | 0.011 s |
|  | testInvokeConstructor | 0.007 s |
|  | testInvokeConstructorWithArgArray | 0.001 s |
|  | testInvokeExactConstructor | 0 s |
|  | testInvokeExactConstructorWithNull | 0 s |
|  | testInvokeConstructorNull | 0 s |
|  | testGetAccessibleConstructor | 0.001 s |
|  | testInvokeConstructorWithTypeArray | 0.001 s |
|  | testGetAccessibleConstructorWithConstructorArg | 0 s |
|  | testInvokeExactConstructorWithTypeArray | 0.001 s |
|  | testGetAccessibleConstructorWithTypeArray | 0.001 s |

<a id="surefire--shortlocaleconvertertest"></a>

### ShortLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.027 s |
|  | testConstructor\_2 | 0.002 s |
|  | testConstructor\_3 | 0.001 s |
|  | testConstructor\_4 | 0.001 s |
|  | testConstructor\_5 | 0 s |
|  | testConstructor\_6 | 0 s |
|  | testConstructor\_7 | 0 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0.001 s |

<a id="surefire--urlconvertertest"></a>

### URLConverterTest

|  |  |  |
| --- | --- | --- |
|  | testSimpleConversion | 0.015 s |

<a id="surefire--jira456test"></a>

### Jira456Test

|  |  |  |
| --- | --- | --- |
|  | testPropertyIsWritable | 0.024 s |
|  | testWriteMethodRecover | 0.002 s |

<a id="surefire--inetaddressconvertertest"></a>

### InetAddressConverterTest

|  |  |  |
| --- | --- | --- |
|  | testInvalidIp | 0.016 s |
|  | testConvertingLocalhost | 0.001 s |
|  | testText | 0.008 s |
|  | testConvertingIpv4 | 0.001 s |
|  | testConvertingIpv6 | 0.001 s |

<a id="surefire--yearconvertertest"></a>

### YearConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.016 s |
|  | testSimpleConversion | 0.003 s |

<a id="surefire--monthdayconvertertest"></a>

### MonthDayConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.003 s |

<a id="surefire--fluentpropertybeanintrospectortest"></a>

### FluentPropertyBeanIntrospectorTest

|  |  |  |
| --- | --- | --- |
|  | testIntrospection | 0.025 s |
|  | testInitNoPrefix | 0.001 s |
|  | testIntrospectionCaps | 0.001 s |

<a id="surefire--beanutilsbeantest"></a>

### BeanUtilsBeanTest

|  |  |  |
| --- | --- | --- |
|  | testGetNestedProperty | 0.049 s |
|  | testSetPropertyDouble | 0.003 s |
|  | testCopyPropertiesStandard | 0.007 s |
|  | testCopyPropertyConvertToString | 0.002 s |
|  | testCopyPropertiesDynaBean | 0.004 s |
|  | testGetIndexedProperty1 | 0.002 s |
|  | testGetIndexedProperty2 | 0.001 s |
|  | testSetPropertyConvert | 0.001 s |
|  | testSetPropertyFloat | 0.001 s |
|  | testSetPropertyShort | 0.001 s |
|  | testMappedProperty | 0.002 s |
|  | testSetPropertyNullValues | 0.002 s |
|  | testSetPropertyConvertFromString | 0.001 s |
|  | testGetIndexedPropertyDate | 0.001 s |
|  | testSetPropertyOnPrimitiveWrappers | 0.001 s |
|  | testSetPropertyConvertToStringArray | 0.001 s |
|  | testCopyPropertyNestedIndexedArray | 0.001 s |
|  | testSetPropertyWriteOnly | 0.001 s |
|  | testCopyPropertyDouble | 0.002 s |
|  | testGetMappedProperty2Args | 0.001 s |
|  | testGetMappedProperty3Args | 0.001 s |
|  | testSetMappedMap | 0.001 s |
|  | testCopyPropertyConvertFromString | 0.001 s |
|  | testGetArrayProperty | 0.001 s |
|  | testSetPropertyInteger | 0 s |
|  | testSeparateInstances | 0.001 s |
|  | testCopyPropertyNestedMappedMap | 0.001 s |
|  | testPopulateArrayElements | 0.002 s |
|  | testPopulateMapped | 0.001 s |
|  | testGetSimplePropertyDate | 0 s |
|  | testPopulateNested | 0 s |
|  | testPopulateArrayProperties | 0 s |
|  | testPopulateScalar | 0 s |
|  | testCopyPropertyConvert | 0.001 s |
|  | testGetArrayPropertyDate | 0.001 s |
|  | testArrayPropertyConversion | 0 s |
|  | testCopyPropertyNestedSimple | 0 s |
|  | testSetPropertyConvertToString | 0.001 s |
|  | testCopyPropertyWriteOnly | 0.001 s |
|  | testPopulate | 0 s |
|  | testSetPropertyStringToArray | 0.001 s |
|  | testCopyPropertyByte | 0.001 s |
|  | testCopyPropertyLong | 0.001 s |
|  | testCopyPropertyNull | 0 s |
|  | testSetPropertyByte | 0.001 s |
|  | testSetPropertyLong | 0.001 s |
|  | testSetPropertyNull | 0 s |
|  | testCopyPropertyInteger | 0.001 s |
|  | testCopyPropertiesMap | 0.001 s |
|  | testSetPropertyConvertToStringIndexed | 0 s |
|  | testDescribe | 0.001 s |
|  | testCopyPropertyConvertToStringIndexed | 0.001 s |
|  | testGetSimpleProperty | 0.001 s |
|  | testCopyPropertyConvertToStringArray | 0 s |
|  | testGetGeneralProperty | 0.001 s |
|  | testCopyPropertyFloat | 0 s |
|  | testCopyPropertyShort | 0.001 s |

<a id="surefire--integerconvertertest"></a>

### IntegerConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.015 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0.001 s |
|  | testStringToNumberPattern | 0.013 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0 s |
|  | testInvalidTypeWithDefault | 0 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0.001 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0 s |
|  | testStringToNumberLocale | 0 s |
|  | testNumberToStringDefault | 0.001 s |
|  | testOtherToStringDefault | 0.001 s |
|  | testDateToNumber | 0.001 s |
|  | testInvalidDefaultObject | 0 s |
|  | testInvalidAmount | 0 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--jira509test"></a>

### Jira509Test

|  |  |  |
| --- | --- | --- |
|  | [testConcurrent](#surefire--org.apache.commons.beanutils2.bugs.jira509test.testconcurrent) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.bugs.Jira509Test.testConcurrent');) | 0 s |
| - | https://issues.apache.org/jira/browse/BEANUTILS-509. | - |

<a id="surefire--beanintrospectiondatatest"></a>

### BeanIntrospectionDataTest

|  |  |  |
| --- | --- | --- |
|  | testGetWriteMethodUndefined | 0.024 s |
|  | testGetWriteMethodNonExisting | 0.001 s |
|  | testGetWriteMethodDefined | 0.001 s |
|  | testGetWriteMethodUnknown | 0 s |

<a id="surefire--enumdeclaringclasstest"></a>

### EnumDeclaringClassTest

|  |  |  |
| --- | --- | --- |
|  | testAllowAccessToClassPropertyFromPropertyUtilsBean | 0.027 s |
|  | testSuppressClassPropertyByDefaultFromPropertyUtilsBean | 0.001 s |
|  | testAllowAccessToClassPropertyFromBeanUtilsBean | 0.012 s |
|  | testSuppressClassPropertyByDefaultFromBeanUtilsBean | 0.001 s |

<a id="surefire--zoneidconvertertest"></a>

### ZoneIdConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.014 s |
|  | testSimpleConversion | 0.005 s |

<a id="surefire--offsettimeconvertertest"></a>

### OffsetTimeConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.014 s |
|  | testSimpleConversion | 0.003 s |

<a id="surefire--jira345test"></a>

### Jira345Test

|  |  |  |
| --- | --- | --- |
|  | testBeanUtilsSetProperty\_2DArray | 0.036 s |
|  | testBeanUtilsSetProperty\_3DArray | 0.001 s |

<a id="surefire--arrayconvertertest"></a>

### ArrayConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnderscore\_BEANUTILS\_302 | 0.016 s |
|  | testTheMatrix | 0.002 s |
|  | testInvalidWithDefault | 0.001 s |
|  | testEmptyString | 0.001 s |
|  | testComponentIntegerConverter | 0.012 s |
|  | testErrors | 0.002 s |
|  | testStringArrayToNumber | 0 s |

<a id="surefire--pathconvertertest"></a>

### PathConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--beanificationtest"></a>

### BeanificationTest

|  |  |  |
| --- | --- | --- |
|  | testMemoryTestMethodology | 0.036 s |
|  | testContextClassloaderIndependence | 0.010 s |
|  | testContextClassLoaderLocal | 0.001 s |
|  | testContextClassLoaderUnset | 0.001 s |
|  | testBeanUtilsBeanSetInstance | 0.002 s |
|  | testMemoryLeak2 | 0.019 s |
|  | testGetByContextClassLoader | 0.002 s |
|  | testMemoryLeak | 0.019 s |

<a id="surefire--dimensionconvertertest"></a>

### DimensionConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertingDimension | 0.023 s |
|  | testInvalidDimensions | 0 s |
|  | testInvalidNumberFormatException | 0.001 s |
|  | testConvertingSquare | 0 s |
|  | testNegativeDimension | 0 s |

<a id="surefire--basicdynabeantest"></a>

### BasicDynaBeanTest

|  |  |  |
| --- | --- | --- |
|  | testGetDescriptorArguments | 0.010 s |
|  | testGetDescriptorLong | 0.001 s |
|  | testSetSimpleBoolean | 0 s |
|  | testNotSerializableException | 0.019 s |
|  | testGetSimpleArguments | 0 s |
|  | testGetDescriptorInt | 0.001 s |
|  | testGetSimpleInt | 0.001 s |
|  | testSetSimpleFloat | 0.001 s |
|  | testSetSimpleShort | 0 s |
|  | testMappedRemove | 0.001 s |
|  | testGetIndexedValues | 0.001 s |
|  | testGetSimpleDouble | 0.001 s |
|  | testMappedContains | 0.001 s |
|  | testGetDescriptorFloat | 0 s |
|  | testGetDescriptorShort | 0.001 s |
|  | testGetSimpleBoolean | 0.001 s |
|  | testGetMappedValues | 0.001 s |
|  | testGetSimpleString | 0 s |
|  | testGetSimpleLong | 0.001 s |
|  | testSetSimpleInt | 0 s |
|  | testSetIndexedArguments | 0 s |
|  | testSetSimpleDouble | 0.001 s |
|  | testGetDescriptorDouble | 0 s |
|  | testGetDescriptors | 0.001 s |
|  | testGetMappedArguments | 0 s |
|  | testSetSimpleLong | 0.001 s |
|  | testGetSimpleFloat | 0 s |
|  | testGetSimpleShort | 0.001 s |
|  | testSetMappedValues | 0 s |
|  | testSetSimpleString | 0 s |
|  | testGetDescriptorSecond | 0.001 s |
|  | testGetDescriptorString | 0 s |
|  | testGetDescriptorBoolean | 0.001 s |
|  | testGetIndexedArguments | 0 s |
|  | testSetIndexedValues | 0.001 s |

<a id="surefire--localdatetimeconvertertest"></a>

### LocalDateTimeConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.026 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.003 s |
|  | testDefaultStringToTypeConvert | 0.001 s |
|  | testDefaultType | 0.001 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.001 s |
|  | testLocale | 0.001 s |
|  | testStringConversion | 0.001 s |
|  | testMultiplePatterns | 0.001 s |

<a id="surefire--shortconvertertest"></a>

### ShortConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.014 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0.001 s |
|  | testStringToNumberPattern | 0.013 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0 s |
|  | testInvalidTypeWithDefault | 0 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0.001 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0 s |
|  | testStringToNumberLocale | 0 s |
|  | testNumberToStringDefault | 0 s |
|  | testOtherToStringDefault | 0.001 s |
|  | testDateToNumber | 0.001 s |
|  | testInvalidAmount | 0 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--jira411test"></a>

### Jira411Test

|  |  |  |
| --- | --- | --- |
|  | testSetProperty | 0.033 s |

<a id="surefire--jira463test"></a>

### Jira463Test

|  |  |  |
| --- | --- | --- |
|  | testSuppressClassProperty | 0.036 s |

<a id="surefire--localeconvertertest"></a>

### LocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertStandardLocale | 0.016 s |
|  | testConvertCustomLocale | 0.001 s |

<a id="surefire--convertutilstest"></a>

### ConvertUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testSeparateConvertInstances | 0.034 s |
|  | testObjectToStringScalar | 0.001 s |
|  | testPositiveIntegerArray | 0.001 s |
|  | testNegativeStringArray | 0 s |
|  | testPositiveStringArray | 0.001 s |
|  | testConvertToString | 0.015 s |
|  | testNegativeIntegerArray | 0.001 s |
|  | testPositiveArray | 0.005 s |
|  | testObjectToStringArray | 0.001 s |
|  | testNegativeScalar | 0.001 s |
|  | testPositiveScalar | 0.001 s |
|  | testConvertUnsupportedTargetType | 0.001 s |
|  | testDeregisteringSingleConverter | 0 s |

<a id="surefire--offsetdatetimeconvertertest"></a>

### OffsetDateTimeConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.026 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.002 s |
|  | testDefaultStringToTypeConvert | 0 s |
|  | testDefaultType | 0.001 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.001 s |
|  | testLocale | 0.001 s |
|  | testStringConversion | 0.001 s |
|  | testMultiplePatterns | 0.002 s |

<a id="surefire--byteconvertertest"></a>

### ByteConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.014 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0 s |
|  | testStringToNumberPattern | 0.013 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0.001 s |
|  | testInvalidTypeWithDefault | 0.001 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0.001 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0.001 s |
|  | testBooleanToNumberDefault | 0.001 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0.001 s |
|  | testStringToNumberLocale | 0.001 s |
|  | testNumberToStringDefault | 0.001 s |
|  | testOtherToStringDefault | 0 s |
|  | testDateToNumber | 0.001 s |
|  | testInvalidAmount | 0 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--bigintegerconvertertest"></a>

### BigIntegerConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.015 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0 s |
|  | testStringToNumberPattern | 0.012 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0 s |
|  | testInvalidTypeWithDefault | 0 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0.001 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0 s |
|  | testStringToNumberLocale | 0.001 s |
|  | testNumberToStringDefault | 0.001 s |
|  | testOtherToStringDefault | 0 s |
|  | testDateToNumber | 0.001 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--dynabeanmapdecoratortest"></a>

### DynaBeanMapDecoratorTest

|  |  |  |
| --- | --- | --- |
|  | testGet | 0.010 s |
|  | testPut | 0 s |
|  | testEntrySet | 0.001 s |
|  | testClear | 0.001 s |
|  | testSize | 0 s |
|  | testContainsKey | 0 s |
|  | testContainsValue | 0 s |
|  | testKeySet | 0.001 s |
|  | testPutAll | 0.001 s |
|  | testIsEmpty | 0.001 s |
|  | testRemove | 0.001 s |
|  | testValues | 0 s |
|  | testIsReadOnly | 0 s |

<a id="surefire--jira347test"></a>

### Jira347Test

|  |  |  |
| --- | --- | --- |
|  | testMappedPropertyDescriptor\_AnyArgsProperty | 1.239 s |

<a id="surefire--jira357test"></a>

### Jira357Test

|  |  |  |
| --- | --- | --- |
|  | testPropertyUtils\_getPropertyDescriptors\_InnerClassProperty | 0.038 s |
|  | testPropertyUtils\_getPropertyDescriptors\_Bar | 0 s |
|  | testPropertyUtils\_getPropertyDescriptors\_Foo | 0 s |

<a id="surefire--sqltimestampconvertertest"></a>

### SqlTimestampConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.027 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.002 s |
|  | testDefaultType | 0 s |
|  | testPatternNullDefault | 0 s |
|  | testPatternNoDefault | 0.001 s |
|  | testStringConversion | 0.001 s |
|  | testMultiplePatterns | 0.001 s |
|  | testDefaultStringToTypeConvert | 0 s |
|  | testLocale | 0.001 s |

<a id="surefire--indexedpropertytest"></a>

### IndexedPropertyTest

|  |  |  |
| --- | --- | --- |
|  | testArrayWriteMethod | 0.034 s |
|  | testArrayIndexedWriteMethod | 0.001 s |
|  | testGetArray | 0.003 s |
|  | testListIndexedPropertyDescriptor | 0.002 s |
|  | testListWriteMethod | 0.001 s |
|  | testGetList | 0.001 s |
|  | testGetArrayList | 0.001 s |
|  | testGetListItemA | 0.001 s |
|  | testGetListItemB | 0.001 s |
|  | testGetArrayAsString | 0.001 s |
|  | testArrayIndexedPropertyDescriptor | 0 s |
|  | testArrayIndexedReadMethod | 0 s |
|  | testArrayListReadMethod | 0.001 s |
|  | testListReadMethod | 0.001 s |
|  | testGetArrayItemA | 0.002 s |
|  | testGetArrayItemB | 0.001 s |
|  | [testListIndexedWriteMethod](#surefire--org.apache.commons.beanutils2.indexedpropertytest.testlistindexedwritemethod) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.IndexedPropertyTest.testListIndexedWriteMethod');) | 0 s |
| - | skipped | - |
|  | [testListIndexedReadMethod](#surefire--org.apache.commons.beanutils2.indexedpropertytest.testlistindexedreadmethod) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.beanutils2.IndexedPropertyTest.testListIndexedReadMethod');) | 0 s |
| - | skipped | - |
|  | testSetArrayItemA | 0.001 s |
|  | testSetArrayItemB | 0.001 s |
|  | testSetArrayList | 0.001 s |
|  | testGetListAsString | 0.001 s |
|  | testSetListItemA | 0.001 s |
|  | testSetListItemB | 0 s |
|  | testArrayListWriteMethod | 0 s |
|  | testArrayListIndexedPropertyDescriptor | 0.001 s |
|  | testSetList | 0.001 s |
|  | testArrayReadMethod | 0.001 s |
|  | testSetArray | 0 s |

<a id="surefire--doubleconvertertest"></a>

### DoubleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.013 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0 s |
|  | testStringToNumberPattern | 0.012 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0.001 s |
|  | testInvalidTypeWithDefault | 0.001 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0 s |
|  | testCalendarToNumber | 0.003 s |
|  | testStringToNumberDefaultType | 0 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0 s |
|  | testStringToNumberLocale | 0.001 s |
|  | testNumberToStringDefault | 0 s |
|  | testOtherToStringDefault | 0.001 s |
|  | testDateToNumber | 0.002 s |
|  | testSimpleConversion | 0 s |

<a id="surefire--datelocaleconvertertest"></a>

### DateLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.031 s |
|  | testSetLenient | 0.002 s |
|  | testInvalidDate | 0 s |
|  | testCalendarObject | 0 s |
|  | testDateObject | 0 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0 s |
|  | testConstructor\_6 | 0 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0 s |
|  | testConstructor\_9 | 0 s |

<a id="surefire--propertyutilsbeantest"></a>

### PropertyUtilsBeanTest

|  |  |  |
| --- | --- | --- |
|  | testGetPropertyDescriptor | 0.019 s |
|  | testSetResolver | 0.001 s |
|  | testGetPropertyEditorClass | 0.001 s |
|  | testGetMappedPropertyDescriptors | 0.001 s |

<a id="surefire--jira368test"></a>

### Jira368Test

|  |  |  |
| --- | --- | --- |
|  | testBeanUtilsSetProperty\_NullBean | 0.033 s |

<a id="surefire--longconvertertest"></a>

### LongConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertNull | 0.015 s |
|  | testInvalidType | 0.001 s |
|  | testToString | 0 s |
|  | testStringToNumberPattern | 0.013 s |
|  | testNumberToStringPattern | 0.001 s |
|  | testConvertNumber | 0.001 s |
|  | testInvalidException | 0.001 s |
|  | testInvalidTypeWithDefault | 0.001 s |
|  | testStringArrayToInteger | 0.001 s |
|  | testInvalidDefault | 0.001 s |
|  | testCalendarToNumber | 0.002 s |
|  | testStringToNumberDefaultType | 0 s |
|  | testBooleanToNumberDefault | 0 s |
|  | testNumberToStringLocale | 0.001 s |
|  | testStringToNumberDefault | 0.001 s |
|  | testStringToNumberLocale | 0.001 s |
|  | testNumberToStringDefault | 0.001 s |
|  | testOtherToStringDefault | 0.001 s |
|  | testDateToNumber | 0.002 s |
|  | testSimpleConversion | 0 s |

<a id="surefire--bigintegerlocaleconvertertest"></a>

### BigIntegerLocaleConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConstructorMain | 0.027 s |
|  | testConstructor\_2 | 0.001 s |
|  | testConstructor\_3 | 0.001 s |
|  | testConstructor\_4 | 0 s |
|  | testConstructor\_5 | 0.001 s |
|  | testConstructor\_6 | 0.001 s |
|  | testConstructor\_7 | 0.001 s |
|  | testConstructor\_8 | 0.001 s |
|  | testConstructor\_9 | 0 s |

<a id="surefire--localdateconvertertest"></a>

### LocalDateConverterTest

|  |  |  |
| --- | --- | --- |
|  | testConvertDate | 0.027 s |
|  | testConvertNull | 0.001 s |
|  | testInvalidType | 0.001 s |
|  | testPatternDefault | 0.002 s |
|  | testDefaultStringToTypeConvert | 0 s |
|  | testDefaultType | 0.001 s |
|  | testPatternNullDefault | 0.001 s |
|  | testPatternNoDefault | 0.001 s |
|  | testLocale | 0.001 s |
|  | testStringConversion | 0.001 s |
|  | testMultiplePatterns | 0.001 s |

<a id="surefire--jira454test"></a>

### Jira454Test

|  |  |  |
| --- | --- | --- |
|  | testCopyProperties | 0.037 s |

<a id="surefire--jira369test"></a>

### Jira369Test

|  |  |  |
| --- | --- | --- |
|  | testBeanUtilsGetProperty\_aRatedCd | 0.037 s |
|  | testBeanUtilsGetProperty\_ARatedCd | 0.001 s |
|  | testBeanUtilsGetProperty\_bRatedCd | 0.001 s |

<a id="surefire--jira273test"></a>

### Jira273Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_273\_PrivatePublicOverridden | 0.032 s |
|  | testIssue\_BEANUTILS\_273\_PrivatePrivatePublicOverridden | 0.001 s |
|  | testIssue\_BEANUTILS\_273\_PrivatePrivatePublicNotOverridden | 0.001 s |
|  | testIssue\_BEANUTILS\_273\_AnonymousNotOverridden | 0.001 s |
|  | testIssue\_BEANUTILS\_273\_PrivatePublicNotOverridden | 0.001 s |
|  | testIssue\_BEANUTILS\_273\_AnonymousOverridden | 0.001 s |

<a id="surefire--jira92test"></a>

### Jira92Test

|  |  |  |
| --- | --- | --- |
|  | testIssue\_BEANUTILS\_92\_copyProperties\_indexed\_only\_setter | 0.039 s |

<a id="surefire--classreloadertest"></a>

### ClassReloaderTest

|  |  |  |
| --- | --- | --- |
|  | testBasicOperation | 0.008 s |

<a id="surefire--localtimeconvertertest"></a>

### LocalTimeConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.003 s |

<a id="surefire--dynapropertytest"></a>

### DynaPropertyTest

|  |  |  |
| --- | --- | --- |
|  | testEqualsObject | 0.010 s |
|  | testHashCode | 0.001 s |

<a id="surefire--localebeanificationtest"></a>

### LocaleBeanificationTest

|  |  |  |
| --- | --- | --- |
|  | testMemoryTestMethodology | 0.051 s |
|  | testLocaleAwareConverterInConvertUtils | 0.002 s |
|  | testContextClassloaderIndependence | 0.010 s |
|  | testContextClassLoaderLocal | 0.001 s |
|  | testContextClassLoaderUnset | 0.001 s |
|  | testBeanUtilsBeanSetInstance | 0.001 s |
|  | testMemoryLeak2 | 0.025 s |
|  | testGetByContextClassLoader | 0.002 s |
|  | testMemoryLeak | 0.019 s |

<a id="surefire--suppresspropertiesbeanintrospectortest"></a>

### SuppressPropertiesBeanIntrospectorTest

|  |  |  |
| --- | --- | --- |
|  | testGetSuppressedPropertiesModify | 0.008 s |
|  | testInitNoPropertyNames | 0.001 s |
|  | testPropertyNamesDefensiveCopy | 0.001 s |
|  | testRemovePropertiesDuringIntrospection | 0 s |

<a id="surefire--zoneoffsetconvertertest"></a>

### ZoneOffsetConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.014 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--localebeanutilstest"></a>

### LocaleBeanUtilsTest

|  |  |  |
| --- | --- | --- |
|  | testSetNestedPropertySimple | 0.050 s |
|  | testSetNestedPropertyIndexed | 0.001 s |

<a id="surefire--uriconvertertest"></a>

### URIConverterTest

|  |  |  |
| --- | --- | --- |
|  | testUnsupportedType | 0.015 s |
|  | testSimpleConversion | 0.001 s |

<a id="surefire--failure-details"></a>

## Failure Details

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

|  |  |
| --- | --- |
|  | testReplaceKeyValueValue |
| - | skipped: skipped |
|  | testReplaceKeyValue |
| - | skipped: skipped |
|  | testRemoveKeyValue |
| - | skipped: skipped |
|  | fixmetestPositiveArray |
| - | skipped: Array conversions not implemented yet. |
|  | fixmetestPositiveIntegerArray |
| - | skipped: Array conversions not implemented yet. |
|  | fixmetestNegativeStringArray |
| - | skipped: Array conversions not implemented yet. |
|  | fixmetestPositiveStringArray |
| - | skipped: Array conversions not implemented yet. |
|  | fixmetestNegativeIntegerArray |
| - | skipped: Array conversions not implemented yet. |
|  | fixmetestObjectToStringArray |
| - | skipped: Array conversions not implemented yet. |
|  | testConcurrent |
| - | skipped: https://issues.apache.org/jira/browse/BEANUTILS-509. |
|  | testListIndexedWriteMethod |
| - | skipped: skipped |
|  | testListIndexedReadMethod |
| - | skipped: skipped |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/rat-report.html -->

<!-- page_index: 12 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

# Rat (Release Audit Tool) results

The following document contains the results of [Rat (Release Audit Tool)](https://creadur.apache.org/rat/apache-rat-plugin/).

```

*****************************************************
Summary
-------
Generated at: 2025-05-27T23:37:11Z

Notes: 4
Binaries: 2
Archives: 0
Standards: 323

Apache Licensed: 323
Generated Documents: 0

JavaDocs are generated, thus a license header is optional.
Generated files do not require license headers.

0 Unknown Licenses

*****************************************************
  Files with Apache License headers will be marked AL
  Binary files (which do not require any license headers) will be marked B
  Compressed archives will be marked A
  Notices, licenses etc. will be marked N
  AL    CODE_OF_CONDUCT.md
  N     RELEASE-NOTES.txt
  AL    pom.xml
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
  N     BUILDING.txt
  N     LICENSE.txt
  AL    SECURITY.md
  AL    src/test/java/org/apache/commons/beanutils2/BetaBean.java
  AL    src/test/java/org/apache/commons/beanutils2/MappedPropertyTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanPropertyValueChangeConsumerTest.java
  AL    src/test/java/org/apache/commons/beanutils2/LazyDynaMapTest.java
  AL    src/test/java/org/apache/commons/beanutils2/MappedPropertyTestInterface.java
  AL    src/test/java/org/apache/commons/beanutils2/LazyDynaClassTest.java
  AL    src/test/java/org/apache/commons/beanutils2/ExtendMapBean.java
  AL    src/test/java/org/apache/commons/beanutils2/locale/LocaleConvertUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/locale/LocaleBeanUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/locale/LocaleBeanificationTest.java
  AL    src/test/java/org/apache/commons/beanutils2/Child.java
  AL    src/test/java/org/apache/commons/beanutils2/TestBeanPublicSubclass.java
  AL    src/test/java/org/apache/commons/beanutils2/BenchBean.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanComparatorTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanUtilsBenchCase.java
  AL    src/test/java/org/apache/commons/beanutils2/NestedTestBean.java
  AL    src/test/java/org/apache/commons/beanutils2/LazyDynaListTest.java
  AL    src/test/java/org/apache/commons/beanutils2/PassTestException.java
  AL    src/test/java/org/apache/commons/beanutils2/PropertyUtilsBeanTest.java
  AL    src/test/java/org/apache/commons/beanutils2/MappedPropertyChildBean.java
  AL    src/test/java/org/apache/commons/beanutils2/MethodUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/TestBean.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira463Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira381Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira456Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira87Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira347Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/EnumDeclaringClassTest.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira157Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira298Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira18Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/other/Jira61BeanFactory.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/other/Jira87BeanFactory.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/other/Jira273BeanFactory.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/other/Jira492IndexedListsSupport.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/other/Jira18BeanFactory.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/other/Jira298BeanFactory.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira465Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira357Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira368Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira369Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira339Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira345Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira492Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira493Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira509Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira541Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira61Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira273Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira422Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira358Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira359Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira454Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira520Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira92Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira458Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira411Test.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira422bTest.java
  AL    src/test/java/org/apache/commons/beanutils2/bugs/Jira349Test.java
  AL    src/test/java/org/apache/commons/beanutils2/AlphaBean.java
  AL    src/test/java/org/apache/commons/beanutils2/ConstructorUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ColorConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ArrayConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/YearConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/DoubleLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/BigIntegerLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/PathConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/AbstractDateConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/DurationConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/DateLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/DimensionConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/DoubleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/IntegerConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/PeriodConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/BooleanConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/URIConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/AbstractLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/LongConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/LongLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/URLConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ZonedDateTimeConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/PatternConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ByteConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ZoneOffsetConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ClassReloaderTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/FloatConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/FloatLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/BigIntegerConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/UUIDConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/IntegerLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/LocalDateConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/YearMonthConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/MemoryTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/LocalTimeConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/PointConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ClassReloader.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/CalendarConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/BigDecimalLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/AbstractNumberConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/CharacterConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/BigDecimalConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/EnumConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ShortConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/DateConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ShortLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ClassConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/InetAddressConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ByteLocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/LocaleConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/FileConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/ZoneIdConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/MonthDayConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/StringConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/OffsetDateTimeConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/LocalDateTimeConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/converters/OffsetTimeConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanMapTest.java
  AL    src/test/java/org/apache/commons/beanutils2/PropsFirstPropertyUtilsBean.java
  AL    src/test/java/org/apache/commons/beanutils2/TestBeanPackageSubclass.java
  AL    src/test/java/org/apache/commons/beanutils2/IndexedPropertyTest.java
  AL    src/test/java/org/apache/commons/beanutils2/MappedPropertyTestBean.java
  AL    src/test/java/org/apache/commons/beanutils2/DefaultIntrospectionContextTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanUtilsBeanTest.java
  AL    src/test/java/org/apache/commons/beanutils2/SuppressPropertiesBeanIntrospectorTest.java
  AL    src/test/java/org/apache/commons/beanutils2/DynaBeanMapDecoratorTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanIntrospectionDataTest.java
  AL    src/test/java/org/apache/commons/beanutils2/PropertyUtilsBenchCase.java
  AL    src/test/java/org/apache/commons/beanutils2/MappedPropertyChildInterface.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PrivateBeanSubclass.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PrivateBean.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PublicSubBean.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PrivateDirect.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PrivateBeanFactory.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PrivateIndirect.java
  AL    src/test/java/org/apache/commons/beanutils2/priv/PackageBean.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanToPropertyValueTransformerTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanPredicateTest.java
  AL    src/test/java/org/apache/commons/beanutils2/LazyDynaBeanTest.java
  AL    src/test/java/org/apache/commons/beanutils2/SonOfAlphaBean.java
  AL    src/test/java/org/apache/commons/beanutils2/ConvertUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/FluentPropertyBeanIntrospectorTest.java
  AL    src/test/java/org/apache/commons/beanutils2/PrimitiveBean.java
  AL    src/test/java/org/apache/commons/beanutils2/AbstractParent.java
  AL    src/test/java/org/apache/commons/beanutils2/memoryleaktests/pojotests/SomeMappedPojo.java
  AL    src/test/java/org/apache/commons/beanutils2/memoryleaktests/pojotests/SomePojo.java
  AL    src/test/java/org/apache/commons/beanutils2/memoryleaktests/pojotests/CustomInteger.java
  AL    src/test/java/org/apache/commons/beanutils2/memoryleaktests/MemoryLeakTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BasicDynaBeanTest.java
  AL    src/test/java/org/apache/commons/beanutils2/AbstractChild.java
  AL    src/test/java/org/apache/commons/beanutils2/expression/DefaultResolverTest.java
  AL    src/test/java/org/apache/commons/beanutils2/ThrowExceptionConverter.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanPropertyValueEqualsPredicateTest.java
  AL    src/test/java/org/apache/commons/beanutils2/DynaBeanUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/FluentIntrospectionTestBean.java
  AL    src/test/java/org/apache/commons/beanutils2/IndexedTestBean.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanWithInnerBean.java
  AL    src/test/java/org/apache/commons/beanutils2/WrapDynaBeanTest.java
  AL    src/test/java/org/apache/commons/beanutils2/DynaPropertyUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/BeanificationTest.java
  AL    src/test/java/org/apache/commons/beanutils2/DynaPropertyTest.java
  AL    src/test/java/org/apache/commons/beanutils2/PropertyUtilsTest.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/DynaResultSetTest.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/TestResultSet.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/converters/SqlTimestampConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/converters/SqlDateConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/converters/SqlTimeConverterTest.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/TestResultSetMetaData.java
  AL    src/test/java/org/apache/commons/beanutils2/sql/DynaRowSetTest.java
  AL    src/changes/release-notes.vm
  AL    src/changes/changes.xml
  AL    src/site/resources/profile.jacoco
  B     src/site/resources/images/logo.png
  AL    src/site/resources/.htaccess
  AL    src/site/xdoc/download_beanutils.xml
  AL    src/site/xdoc/index.xml
  AL    src/site/xdoc/mail-lists.xml
  AL    src/site/xdoc/proposal.xml
  AL    src/site/xdoc/building.xml
  AL    src/site/xdoc/issue-tracking.xml
  AL    src/site/xdoc/bean-collections.xml
  AL    src/site/xdoc/security.xml
  AL    src/site/site.xml
  AL    src/main/assembly/src.xml
  AL    src/main/assembly/bin.xml
  AL    src/main/java/org/apache/commons/beanutils2/DynaBeanPropertyMapDecorator.java
  AL    src/main/java/org/apache/commons/beanutils2/DefaultBeanIntrospector.java
  AL    src/main/java/org/apache/commons/beanutils2/ConvertingWrapDynaBean.java
  AL    src/main/java/org/apache/commons/beanutils2/DynaProperty.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanMap.java
  AL    src/main/java/org/apache/commons/beanutils2/DynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/DecimalLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/DateLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/IntegerLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/LongLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/FloatLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/StringLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/BigDecimalLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/DoubleLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/BigIntegerLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/ByteLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/converters/ShortLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/LocaleConvertUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/LocaleConvertUtilsBean.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/LocaleBeanUtilsBean.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/BaseLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/LocaleBeanUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/LocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/locale/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/ConvertUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/PropertyDescriptors.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanIntrospectionData.java
  AL    src/main/java/org/apache/commons/beanutils2/LazyDynaList.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanUtilsBean.java
  AL    src/main/java/org/apache/commons/beanutils2/TestEnum.java
  AL    src/main/java/org/apache/commons/beanutils2/IntrospectionContext.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanPropertyValueChangeConsumer.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/OffsetTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ZoneOffsetConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/PointConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/AbstractConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/DurationConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/LongConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ArrayConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ShortConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/NumberConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/LocalDateConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/StringConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/BigIntegerConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/EnumConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/PatternConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/FloatConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/URLConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ZonedDateTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/BooleanConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/BigDecimalConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/DateConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/IntegerConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/OffsetDateTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/YearConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/DoubleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/FileConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/DateTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/DimensionConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ZoneIdConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/UUIDConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/MonthDayConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/URIConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/PathConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/LocalTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ColorConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/InetAddressConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ClassConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/YearMonthConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/CharacterConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/LocalDateTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ConverterFacade.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/LocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/CalendarConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/ByteConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/converters/PeriodConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/WrapDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/MappedPropertyDescriptor.java
  AL    src/main/java/org/apache/commons/beanutils2/MethodUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/SuppressPropertiesBeanIntrospector.java
  AL    src/main/java/org/apache/commons/beanutils2/ContextClassLoaderLocal.java
  AL    src/main/java/org/apache/commons/beanutils2/ConvertUtilsBean.java
  AL    src/main/java/org/apache/commons/beanutils2/WrapDynaBean.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanIntrospector.java
  AL    src/main/java/org/apache/commons/beanutils2/BasicDynaBean.java
  AL    src/main/java/org/apache/commons/beanutils2/Converter.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/DynaBean.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanToPropertyValueTransformer.java
  AL    src/main/java/org/apache/commons/beanutils2/BaseDynaBeanMapDecorator.java
  AL    src/main/java/org/apache/commons/beanutils2/ConversionException.java
  AL    src/main/java/org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanAccessLanguageException.java
  AL    src/main/java/org/apache/commons/beanutils2/DefaultIntrospectionContext.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanComparator.java
  AL    src/main/java/org/apache/commons/beanutils2/LazyDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/PropertyUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/LazyDynaBean.java
  AL    src/main/java/org/apache/commons/beanutils2/expression/Resolver.java
  AL    src/main/java/org/apache/commons/beanutils2/expression/DefaultResolver.java
  AL    src/main/java/org/apache/commons/beanutils2/expression/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/ConstructorUtils.java
  AL    src/main/java/org/apache/commons/beanutils2/BasicDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/PropertyUtilsBean.java
  AL    src/main/java/org/apache/commons/beanutils2/NestedNullException.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanPropertyValueEqualsPredicate.java
  AL    src/main/java/org/apache/commons/beanutils2/MutableDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/LazyDynaMap.java
  AL    src/main/java/org/apache/commons/beanutils2/BeanPredicate.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/locale/SqlTimestampLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/locale/SqlDateLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/locale/SqlTimeLocaleConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/locale/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/SqlTimestampConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/SqlTimeConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/SqlDateConverter.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/converters/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/ResultSetDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/RowSetDynaClass.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/package-info.java
  AL    src/main/java/org/apache/commons/beanutils2/sql/ResultSetIterator.java
  AL    src/main/javadoc/overview.html
  AL    src/conf/checkstyle-suppressions.xml
  AL    src/conf/checkstyle.xml
  B     src/media/logo.xcf
 
*****************************************************
```

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/japicmp.html -->

<!-- page_index: 13 -->

# Apache Commons BeanUtils

Comparing source compatibility of commons-beanutils2-2.0.0-M2.jar against commons-beanutils2-2.0.0-M1.jar

|  |  |
| --- | --- |
| Old: | commons-beanutils2-2.0.0-M1.jar |
| New: | commons-beanutils2-2.0.0-M2.jar |
| Created: | 2025-05-27T23:37:12.130+0000 |
| Access modifier filter: | PROTECTED |
| Only modifications: | true |
| Only binary incompatible modifications: | false |
| Ignore missing classes: | false |
| Includes: | all |
| Excludes: | n.a. |
| Semantic Versioning: | 1.0.0 |

- [Classes](#japicmp--toc)

Classes:

| Status | Fully Qualified Name |
| --- | --- |
| MODIFIED (!) | [org.apache.commons.beanutils2.BeanUtils](#japicmp--org.apache.commons.beanutils2.beanutils) |
| MODIFIED (!) | [org.apache.commons.beanutils2.ConstructorUtils](#japicmp--org.apache.commons.beanutils2.constructorutils) |
| MODIFIED (!) | [org.apache.commons.beanutils2.ConvertUtils](#japicmp--org.apache.commons.beanutils2.convertutils) |
| MODIFIED (!) | [org.apache.commons.beanutils2.locale.LocaleBeanUtils](#japicmp--org.apache.commons.beanutils2.locale.localebeanutils) |
| MODIFIED (!) | [org.apache.commons.beanutils2.locale.LocaleConvertUtils](#japicmp--org.apache.commons.beanutils2.locale.localeconvertutils) |
| MODIFIED (!) | [org.apache.commons.beanutils2.MethodUtils](#japicmp--org.apache.commons.beanutils2.methodutils) |
| MODIFIED (!) | [org.apache.commons.beanutils2.PropertyUtils](#japicmp--org.apache.commons.beanutils2.propertyutils) |
| MODIFIED | [org.apache.commons.beanutils2.SuppressPropertiesBeanIntrospector](#japicmp--org.apache.commons.beanutils2.suppresspropertiesbeanintrospector) |
| NEW | [org.apache.commons.beanutils2.TestEnum](#japicmp--org.apache.commons.beanutils2.testenum) |

Binary incompatible changes are marked with (!) while source incompatible changes are marked with (\*).

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.BeanUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>BeanUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			37
		</td>
<td>
			363
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.ConstructorUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>ConstructorUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			43
		</td>
<td>
			413
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.ConvertUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>ConvertUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			31
		</td>
<td>
			224
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.locale.LocaleBeanUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Superclass:

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
<td><span>MODIFIED (!)</span></td>
<td>java.lang.Object(&lt;- org.apache.commons.beanutils2.BeanUtils)</td>
<td><div>
<span>Compatibility Changes:</span>
<table>
<thead>
<tr>
<td>Change</td>
</tr>
</thead>
<tbody>
<tr><td>SUPERCLASS_REMOVED</td></tr>
</tbody>
</table>
</div>
</td>
</tr>
</tbody>
</table>

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>LocaleBeanUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			34
		</td>
<td>
			548
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.locale.LocaleConvertUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>LocaleConvertUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			33
		</td>
<td>
			356
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.MethodUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>MethodUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			53
		</td>
<td>
			1174
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

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
<span>static</span>
<span>public</span>
</td>
<td>n.a.</td>
<td><span>boolean</span></td>
<td>isAssignmentCompatible(<span>java.lang.Class<div><span>&lt;..&gt;</span><div><table><tr><td>New:</td><td>?</td></tr><tr><td>Old:</td><td>?</td></tr></table></div></div></span>, <span>java.lang.Class<div><span>&lt;..&gt;</span><div><table><tr><td>New:</td><td>?</td></tr><tr><td>Old:</td><td>?</td></tr></table></div></div></span>)</td>
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
			1069
		</td>
<td>
			1069
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED (!)
FINAL (<- NON\_FINAL)
public
class
org.apache.commons.beanutils2.PropertyUtils
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| CLASS\_NOW\_FINAL |

Constructors:

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
<td><span>MODIFIED (!)</span></td>
<td><span>PRIVATE (&lt;- PUBLIC) </span>
</td>
<td>n.a.</td>
<td>PropertyUtils()</td>
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
<tr><td>CONSTRUCTOR_LESS_ACCESSIBLE</td></tr>
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
			38
		</td>
<td>
			656
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
class
org.apache.commons.beanutils2.SuppressPropertiesBeanIntrospector
[top](#japicmp--toc)

Fields:

| Status | Modifier | Type | Field | Compatibility Changes: |
| --- | --- | --- | --- | --- |
| NEW | public static final | org.apache.commons.beanutils2.SuppressPropertiesBeanIntrospector | SUPPRESS\_DECLARING\_CLASS | n.a. |

NEW
 (Serializable compatible)
final
public
enum
org.apache.commons.beanutils2.TestEnum
[top](#japicmp--toc)

Compatibility Changes:

| Change |
| --- |
| INTERFACE\_ADDED |

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| NEW | java.lang.Enum | n.a. |

Interfaces:

| Status | Interface | Compatibility Changes |
| --- | --- | --- |
| NEW | java.lang.constant.Constable | n.a. |
| NEW | java.lang.Comparable | n.a. |
| NEW | java.io.Serializable | n.a. |

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | false | n.a. | n.a. |
| New | true | -2238496090173180950 | n.a. |

Fields:

| Status | Modifier | Type | Field | Compatibility Changes: |
| --- | --- | --- | --- | --- |
| NEW | public static final | org.apache.commons.beanutils2.TestEnum | A | n.a. |
| NEW | public static final | org.apache.commons.beanutils2.TestEnum | B | n.a. |
| NEW | public static final | org.apache.commons.beanutils2.TestEnum | C | n.a. |

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
<td><span>static</span>
<span>public</span>
</td>
<td>n.a.</td>
<td><span>org.apache.commons.beanutils2.TestEnum</span></td>
<td>valueOf(<span>java.lang.String</span>)</td>
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
			23
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td>
<td><span>static</span>
<span>public</span>
</td>
<td>n.a.</td>
<td><span>org.apache.commons.beanutils2.TestEnum[]</span></td>
<td>values()</td>
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
			23
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/checkstyle.html -->

<!-- page_index: 14 -->

<a id="checkstyle--checkstyle-results"></a>

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 10.23.1 with /Users/garygregory/git/commons-beanutils/src/conf/checkstyle.xml ruleset.

<a id="checkstyle--summary"></a>

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 293 | 0 | 0 | 0 |

<a id="checkstyle--files"></a>

## Files

| File | I | W | E |
| --- | --- | --- | --- |

<a id="checkstyle--details"></a>

## Details

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/pmd.html -->

<!-- page_index: 15 -->

# PMD Results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="PMD_Results"></a>
DOC2MDPLACEHOLDERTOKEN0END<h1>PMD Results</h1>
<p>The following document contains the results of <a href="https://pmd.github.io">PMD</a> 7.13.0.</p><section><a id="Violations_By_Priority"></a>
DOC2MDPLACEHOLDERTOKEN1END<h2>Violations By Priority</h2><section><a id="Priority_3"></a>
DOC2MDPLACEHOLDERTOKEN2END<h3>Priority 3</h3><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FBeanIntrospectionData.java"></a>
DOC2MDPLACEHOLDERTOKEN3END<h4>org/apache/commons/beanutils2/BeanIntrospectionData.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanIntrospectionData.html#L130">130</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanIntrospectionData.html#L132">132</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FBeanUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN4END<h4>org/apache/commons/beanutils2/BeanUtilsBean.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedformalparameter">UnusedFormalParameter</a></td>
<td>Avoid unused constructor parameters such as 'todoRemove'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L153">153</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L303">303</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L305">305</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FConstructorUtils.java"></a>
DOC2MDPLACEHOLDERTOKEN5END<h4>org/apache/commons/beanutils2/ConstructorUtils.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L149">149</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L151">151</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L154">154</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L155">155</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L179">179</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L183">183</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FContextClassLoaderLocal.java"></a>
DOC2MDPLACEHOLDERTOKEN6END<h4>org/apache/commons/beanutils2/ContextClassLoaderLocal.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L134">134</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L135">135</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L176">176</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L177">177</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L193">193</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L194">194</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FConvertUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN7END<h4>org/apache/commons/beanutils2/ConvertUtilsBean.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatemethod">UnusedPrivateMethod</a></td>
<td>Avoid unused private methods such as 'convert(String[], Class&lt;T&gt;, Converter&lt;T&gt;)'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConvertUtilsBean.html#L315">315</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_performance.html#bigintegerinstantiation">BigIntegerInstantiation</a></td>
<td>Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConvertUtilsBean.html#L658">658</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FDynaProperty.java"></a>
DOC2MDPLACEHOLDERTOKEN8END<h4>org/apache/commons/beanutils2/DynaProperty.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'BOOLEAN_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L42">42</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'BYTE_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L43">43</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'CHAR_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L44">44</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'DOUBLE_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L45">45</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'FLOAT_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L46">46</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'INT_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L47">47</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'LONG_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L48">48</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'SHORT_TYPE'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L49">49</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FFluentPropertyBeanIntrospector.java"></a>
DOC2MDPLACEHOLDERTOKEN9END<h4>org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedformalparameter">UnusedFormalParameter</a></td>
<td>Avoid unused method parameters such as 'propertyName'.</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.html#L109">109</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FLazyDynaBean.java"></a>
DOC2MDPLACEHOLDERTOKEN10END<h4>org/apache/commons/beanutils2/LazyDynaBean.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_performance.html#bigintegerinstantiation">BigIntegerInstantiation</a></td>
<td>Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L135">135</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_performance.html#bigintegerinstantiation">BigIntegerInstantiation</a></td>
<td>Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L137">137</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FMappedPropertyDescriptor.java"></a>
DOC2MDPLACEHOLDERTOKEN11END<h4>org/apache/commons/beanutils2/MappedPropertyDescriptor.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L140">140</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L142">142</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L293">293</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L297">297</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FMethodUtils.java"></a>
DOC2MDPLACEHOLDERTOKEN12END<h4>org/apache/commons/beanutils2/MethodUtils.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L316">316</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L320">320</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L429">429</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L430">430</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FPropertyUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN13END<h4>org/apache/commons/beanutils2/PropertyUtilsBean.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L684">684</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L688">688</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Fconverters.2FClassConverter.java"></a>
DOC2MDPLACEHOLDERTOKEN14END<h4>org/apache/commons/beanutils2/converters/ClassConverter.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/ClassConverter.html#L79">79</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/ClassConverter.html#L82">82</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Fsql.2FAbstractJdbcDynaClass.java"></a>
DOC2MDPLACEHOLDERTOKEN15END<h4>org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L114">114</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L117">117</a></td></tr></table></section></section><section><a id="Priority_4"></a>
DOC2MDPLACEHOLDERTOKEN16END<h3>Priority 4</h3><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FBeanUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN17END<h4>org/apache/commons/beanutils2/BeanUtilsBean.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.util': 'HashMap' is already in scope because it is imported in this file</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L483">483</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FLazyDynaClass.java"></a>
DOC2MDPLACEHOLDERTOKEN18END<h4>org/apache/commons/beanutils2/LazyDynaClass.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.lang': 'UnsupportedOperationException' is already in scope because it is declared in java.lang</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaClass.html#L190">190</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FLazyDynaMap.java"></a>
DOC2MDPLACEHOLDERTOKEN19END<h4>org/apache/commons/beanutils2/LazyDynaMap.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.lang': 'UnsupportedOperationException' is already in scope because it is declared in java.lang</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L204">204</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FMethodUtils.java"></a>
DOC2MDPLACEHOLDERTOKEN20END<h4>org/apache/commons/beanutils2/MethodUtils.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'MethodUtils': 'getPrimitiveWrapper' is already in scope</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L1165">1165</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Flocale.2Fconverters.2FDateLocaleConverter.java"></a>
DOC2MDPLACEHOLDERTOKEN21END<h4>org/apache/commons/beanutils2/locale/converters/DateLocaleConverter.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'DateLocaleConverter': 'initDefaultChars' is already in scope</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/locale/converters/DateLocaleConverter.html#L102">102</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Fsql.2FAbstractJdbcDynaClass.java"></a>
DOC2MDPLACEHOLDERTOKEN22END<h4>org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.java</h4>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.sql': 'Date' is already in scope because it is imported in this file</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L106">106</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.sql': 'Timestamp' is already in scope because it is imported in this file</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L108">108</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.sql': 'Time' is already in scope because it is imported in this file</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L110">110</a></td></tr></table></section></section></section><section><a id="Files"></a>
DOC2MDPLACEHOLDERTOKEN23END<h2>Files</h2><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FBeanIntrospectionData.java"></a>
DOC2MDPLACEHOLDERTOKEN24END<h3>org/apache/commons/beanutils2/BeanIntrospectionData.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanIntrospectionData.html#L130">130</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanIntrospectionData.html#L132">132</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FBeanUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN25END<h3>org/apache/commons/beanutils2/BeanUtilsBean.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedformalparameter">UnusedFormalParameter</a></td>
<td>Avoid unused constructor parameters such as 'todoRemove'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L153">153</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L303">303</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L305">305</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.util': 'HashMap' is already in scope because it is imported in this file</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L483">483</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FConstructorUtils.java"></a>
DOC2MDPLACEHOLDERTOKEN26END<h3>org/apache/commons/beanutils2/ConstructorUtils.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L149">149</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L151">151</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L154">154</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L155">155</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L179">179</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConstructorUtils.html#L183">183</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FContextClassLoaderLocal.java"></a>
DOC2MDPLACEHOLDERTOKEN27END<h3>org/apache/commons/beanutils2/ContextClassLoaderLocal.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L134">134</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L135">135</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L176">176</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L177">177</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L193">193</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L194">194</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FConvertUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN28END<h3>org/apache/commons/beanutils2/ConvertUtilsBean.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatemethod">UnusedPrivateMethod</a></td>
<td>Avoid unused private methods such as 'convert(String[], Class&lt;T&gt;, Converter&lt;T&gt;)'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConvertUtilsBean.html#L315">315</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_performance.html#bigintegerinstantiation">BigIntegerInstantiation</a></td>
<td>Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConvertUtilsBean.html#L658">658</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FDynaProperty.java"></a>
DOC2MDPLACEHOLDERTOKEN29END<h3>org/apache/commons/beanutils2/DynaProperty.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'BOOLEAN_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L42">42</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'BYTE_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L43">43</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'CHAR_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L44">44</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'DOUBLE_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L45">45</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'FLOAT_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L46">46</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'INT_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L47">47</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'LONG_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L48">48</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedprivatefield">UnusedPrivateField</a></td>
<td>Avoid unused private fields such as 'SHORT_TYPE'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DynaProperty.html#L49">49</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FFluentPropertyBeanIntrospector.java"></a>
DOC2MDPLACEHOLDERTOKEN30END<h3>org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_bestpractices.html#unusedformalparameter">UnusedFormalParameter</a></td>
<td>Avoid unused method parameters such as 'propertyName'.</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.html#L109">109</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FLazyDynaBean.java"></a>
DOC2MDPLACEHOLDERTOKEN31END<h3>org/apache/commons/beanutils2/LazyDynaBean.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_performance.html#bigintegerinstantiation">BigIntegerInstantiation</a></td>
<td>Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L135">135</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_performance.html#bigintegerinstantiation">BigIntegerInstantiation</a></td>
<td>Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L137">137</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FLazyDynaClass.java"></a>
DOC2MDPLACEHOLDERTOKEN32END<h3>org/apache/commons/beanutils2/LazyDynaClass.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.lang': 'UnsupportedOperationException' is already in scope because it is declared in java.lang</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaClass.html#L190">190</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FLazyDynaMap.java"></a>
DOC2MDPLACEHOLDERTOKEN33END<h3>org/apache/commons/beanutils2/LazyDynaMap.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.lang': 'UnsupportedOperationException' is already in scope because it is declared in java.lang</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L204">204</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FMappedPropertyDescriptor.java"></a>
DOC2MDPLACEHOLDERTOKEN34END<h3>org/apache/commons/beanutils2/MappedPropertyDescriptor.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L140">140</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L142">142</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L293">293</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L297">297</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FMethodUtils.java"></a>
DOC2MDPLACEHOLDERTOKEN35END<h3>org/apache/commons/beanutils2/MethodUtils.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L316">316</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L320">320</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L429">429</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L430">430</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'MethodUtils': 'getPrimitiveWrapper' is already in scope</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MethodUtils.html#L1165">1165</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2FPropertyUtilsBean.java"></a>
DOC2MDPLACEHOLDERTOKEN36END<h3>org/apache/commons/beanutils2/PropertyUtilsBean.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L684">684</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L688">688</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Fconverters.2FClassConverter.java"></a>
DOC2MDPLACEHOLDERTOKEN37END<h3>org/apache/commons/beanutils2/converters/ClassConverter.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/ClassConverter.html#L79">79</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/ClassConverter.html#L82">82</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Flocale.2Fconverters.2FDateLocaleConverter.java"></a>
DOC2MDPLACEHOLDERTOKEN38END<h3>org/apache/commons/beanutils2/locale/converters/DateLocaleConverter.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'DateLocaleConverter': 'initDefaultChars' is already in scope</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/locale/converters/DateLocaleConverter.html#L102">102</a></td></tr></table></section><section><a id="org.2Fapache.2Fcommons.2Fbeanutils2.2Fsql.2FAbstractJdbcDynaClass.java"></a>
DOC2MDPLACEHOLDERTOKEN39END<h3>org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.java</h3>
<table>
<tr>
<th>Rule</th>
<th>Violation</th>
<th>Priority</th>
<th>Line</th></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.sql': 'Date' is already in scope because it is imported in this file</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L106">106</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.sql': 'Timestamp' is already in scope because it is imported in this file</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L108">108</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_codestyle.html#unnecessaryfullyqualifiedname">UnnecessaryFullyQualifiedName</a></td>
<td>Unnecessary qualifier 'java.sql': 'Time' is already in scope because it is imported in this file</td>
<td>4</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L110">110</a></td></tr>
<tr>
<td><a href="https://docs.pmd-code.org/pmd-doc-7.13.0/pmd_rules_java_errorprone.html#emptycatchblock">EmptyCatchBlock</a></td>
<td>Avoid empty catch blocks</td>
<td>3</td>
<td><a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L114">114</a>–<a href="https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/AbstractJdbcDynaClass.html#L117">117</a></td></tr></table></section></section></section>
</td>
</tr>
</table>

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-beanutils/spotbugs.html -->

<!-- page_index: 16 -->

<a id="spotbugs--spotbugs-bug-detector-report"></a>

# SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.9.3*

Threshold is

Effort is *default*

<a id="spotbugs--summary"></a>

# Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 164 | 61 | 0 | 0 |

<a id="spotbugs--files"></a>

# Files

| Class | Bugs |
| --- | --- |
| [org.apache.commons.beanutils2.BaseDynaBeanMapDecorator](#spotbugs--org.apache.commons.beanutils2.basedynabeanmapdecorator) | 1 |
| [org.apache.commons.beanutils2.BasicDynaBean](#spotbugs--org.apache.commons.beanutils2.basicdynabean) | 1 |
| [org.apache.commons.beanutils2.BasicDynaClass](#spotbugs--org.apache.commons.beanutils2.basicdynaclass) | 3 |
| [org.apache.commons.beanutils2.BeanMap](#spotbugs--org.apache.commons.beanutils2.beanmap) | 1 |
| [org.apache.commons.beanutils2.BeanMap$Entry](#spotbugs--org.apache.commons.beanutils2.beanmap-entry) | 2 |
| [org.apache.commons.beanutils2.BeanPredicate](#spotbugs--org.apache.commons.beanutils2.beanpredicate) | 1 |
| [org.apache.commons.beanutils2.BeanPropertyValueChangeConsumer](#spotbugs--org.apache.commons.beanutils2.beanpropertyvaluechangeconsumer) | 2 |
| [org.apache.commons.beanutils2.BeanPropertyValueEqualsPredicate](#spotbugs--org.apache.commons.beanutils2.beanpropertyvalueequalspredicate) | 2 |
| [org.apache.commons.beanutils2.BeanToPropertyValueTransformer](#spotbugs--org.apache.commons.beanutils2.beantopropertyvaluetransformer) | 2 |
| [org.apache.commons.beanutils2.BeanUtilsBean](#spotbugs--org.apache.commons.beanutils2.beanutilsbean) | 2 |
| [org.apache.commons.beanutils2.ContextClassLoaderLocal](#spotbugs--org.apache.commons.beanutils2.contextclassloaderlocal) | 2 |
| [org.apache.commons.beanutils2.ConvertUtilsBean](#spotbugs--org.apache.commons.beanutils2.convertutilsbean) | 2 |
| [org.apache.commons.beanutils2.DefaultBeanIntrospector](#spotbugs--org.apache.commons.beanutils2.defaultbeanintrospector) | 1 |
| [org.apache.commons.beanutils2.FluentPropertyBeanIntrospector](#spotbugs--org.apache.commons.beanutils2.fluentpropertybeanintrospector) | 2 |
| [org.apache.commons.beanutils2.LazyDynaBean](#spotbugs--org.apache.commons.beanutils2.lazydynabean) | 3 |
| [org.apache.commons.beanutils2.LazyDynaList](#spotbugs--org.apache.commons.beanutils2.lazydynalist) | 5 |
| [org.apache.commons.beanutils2.LazyDynaMap](#spotbugs--org.apache.commons.beanutils2.lazydynamap) | 6 |
| [org.apache.commons.beanutils2.MappedPropertyDescriptor](#spotbugs--org.apache.commons.beanutils2.mappedpropertydescriptor) | 4 |
| [org.apache.commons.beanutils2.PropertyUtilsBean](#spotbugs--org.apache.commons.beanutils2.propertyutilsbean) | 3 |
| [org.apache.commons.beanutils2.WrapDynaBean](#spotbugs--org.apache.commons.beanutils2.wrapdynabean) | 1 |
| [org.apache.commons.beanutils2.converters.AbstractConverter](#spotbugs--org.apache.commons.beanutils2.converters.abstractconverter) | 1 |
| [org.apache.commons.beanutils2.converters.ArrayConverter](#spotbugs--org.apache.commons.beanutils2.converters.arrayconverter) | 2 |
| [org.apache.commons.beanutils2.converters.DateTimeConverter](#spotbugs--org.apache.commons.beanutils2.converters.datetimeconverter) | 2 |
| [org.apache.commons.beanutils2.locale.LocaleBeanUtilsBean](#spotbugs--org.apache.commons.beanutils2.locale.localebeanutilsbean) | 3 |
| [org.apache.commons.beanutils2.sql.ResultSetDynaClass](#spotbugs--org.apache.commons.beanutils2.sql.resultsetdynaclass) | 2 |
| [org.apache.commons.beanutils2.sql.ResultSetIterator](#spotbugs--org.apache.commons.beanutils2.sql.resultsetiterator) | 1 |
| [org.apache.commons.beanutils2.sql.RowSetDynaClass](#spotbugs--org.apache.commons.beanutils2.sql.rowsetdynaclass) | 4 |

<a id="spotbugs--org.apache.commons.beanutils2.basedynabeanmapdecorator"></a>

## org.apache.commons.beanutils2.BaseDynaBeanMapDecorator

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.BaseDynaBeanMapDecorator.getDynaBean() may expose internal representation by returning BaseDynaBeanMapDecorator.dynaBean | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [219](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BaseDynaBeanMapDecorator.html#L219) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.basicdynabean"></a>

## org.apache.commons.beanutils2.BasicDynaBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.BasicDynaBean.getMap() may expose internal representation by returning BasicDynaBean.mapDecorator | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [232](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BasicDynaBean.html#L232) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.basicdynaclass"></a>

## org.apache.commons.beanutils2.BasicDynaClass

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.BasicDynaClass at new org.apache.commons.beanutils2.BasicDynaClass() will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [78](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BasicDynaClass.html#L78) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.BasicDynaClass at new org.apache.commons.beanutils2.BasicDynaClass(String, Class) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [88](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BasicDynaClass.html#L88) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.BasicDynaClass at new org.apache.commons.beanutils2.BasicDynaClass(String, Class, DynaProperty[]) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [105](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BasicDynaClass.html#L105) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beanmap"></a>

## org.apache.commons.beanutils2.BeanMap

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Do not catch NullPointerException like in org.apache.commons.beanutils2.BeanMap.get(Object) | STYLE | [DCN\_NULLPOINTER\_EXCEPTION](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#DCN_NULLPOINTER_EXCEPTION) | [387](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanMap.html#L387) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beanmap-entry"></a>

## org.apache.commons.beanutils2.BeanMap$Entry

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.BeanMap$Entry doesn't override java.util.AbstractMap$SimpleEntry.equals(Object) | STYLE | [EQ\_DOESNT\_OVERRIDE\_EQUALS](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EQ_DOESNT_OVERRIDE_EQUALS) | [1](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanMap.html#L1) | Medium |
| Class org.apache.commons.beanutils2.BeanMap$Entry defines non-transient non-serializable instance field owner | BAD\_PRACTICE | [SE\_BAD\_FIELD](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#SE_BAD_FIELD) | Not available | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beanpredicate"></a>

## org.apache.commons.beanutils2.BeanPredicate

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.BeanPredicate at new org.apache.commons.beanutils2.BeanPredicate(String, Predicate) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [35](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanPredicate.html#L35) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beanpropertyvaluechangeconsumer"></a>

## org.apache.commons.beanutils2.BeanPropertyValueChangeConsumer

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.BeanPropertyValueChangeConsumer at new org.apache.commons.beanutils2.BeanPropertyValueChangeConsumer(String, Object) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [105](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanPropertyValueChangeConsumer.html#L105) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.BeanPropertyValueChangeConsumer at new org.apache.commons.beanutils2.BeanPropertyValueChangeConsumer(String, Object, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [73](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanPropertyValueChangeConsumer.html#L73) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beanpropertyvalueequalspredicate"></a>

## org.apache.commons.beanutils2.BeanPropertyValueEqualsPredicate

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.BeanPropertyValueEqualsPredicate at new org.apache.commons.beanutils2.BeanPropertyValueEqualsPredicate(String, Object) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [139](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanPropertyValueEqualsPredicate.html#L139) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.BeanPropertyValueEqualsPredicate at new org.apache.commons.beanutils2.BeanPropertyValueEqualsPredicate(String, Object, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [103](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanPropertyValueEqualsPredicate.html#L103) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beantopropertyvaluetransformer"></a>

## org.apache.commons.beanutils2.BeanToPropertyValueTransformer

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.BeanToPropertyValueTransformer at new org.apache.commons.beanutils2.BeanToPropertyValueTransformer(String) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [96](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanToPropertyValueTransformer.html#L96) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.BeanToPropertyValueTransformer at new org.apache.commons.beanutils2.BeanToPropertyValueTransformer(String, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [67](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanToPropertyValueTransformer.html#L67) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.beanutilsbean"></a>

## org.apache.commons.beanutils2.BeanUtilsBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.BeanUtilsBean.getPropertyUtils() may expose internal representation by returning BeanUtilsBean.propertyUtilsBean | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [660](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L660) | Medium |
| new org.apache.commons.beanutils2.BeanUtilsBean(ConvertUtilsBean, PropertyUtilsBean) may expose internal representation by storing an externally mutable object into BeanUtilsBean.propertyUtilsBean | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [167](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/BeanUtilsBean.html#L167) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.contextclassloaderlocal"></a>

## org.apache.commons.beanutils2.ContextClassLoaderLocal

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Return value of java.util.Map.isEmpty() ignored, but method has no side effect | STYLE | [RV\_RETURN\_VALUE\_IGNORED\_NO\_SIDE\_EFFECT](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#RV_RETURN_VALUE_IGNORED_NO_SIDE_EFFECT) | [119](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L119) | Medium |
| Return value of java.util.Map.isEmpty() ignored, but method has no side effect | STYLE | [RV\_RETURN\_VALUE\_IGNORED\_NO\_SIDE\_EFFECT](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#RV_RETURN_VALUE_IGNORED_NO_SIDE_EFFECT) | [167](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ContextClassLoaderLocal.html#L167) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.convertutilsbean"></a>

## org.apache.commons.beanutils2.ConvertUtilsBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.ConvertUtilsBean at new org.apache.commons.beanutils2.ConvertUtilsBean() will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [223](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConvertUtilsBean.html#L223) | Medium |
| Private method org.apache.commons.beanutils2.ConvertUtilsBean.convert(String[], Class, Converter) is never called | PERFORMANCE | [UPM\_UNCALLED\_PRIVATE\_METHOD](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#UPM_UNCALLED_PRIVATE_METHOD) | [316-323](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/ConvertUtilsBean.html#L316) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.defaultbeanintrospector"></a>

## org.apache.commons.beanutils2.DefaultBeanIntrospector

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.DefaultBeanIntrospector at new org.apache.commons.beanutils2.DefaultBeanIntrospector() will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [54](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/DefaultBeanIntrospector.html#L54) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.fluentpropertybeanintrospector"></a>

## org.apache.commons.beanutils2.FluentPropertyBeanIntrospector

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.FluentPropertyBeanIntrospector at new org.apache.commons.beanutils2.FluentPropertyBeanIntrospector() will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [86](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.html#L86) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.FluentPropertyBeanIntrospector at new org.apache.commons.beanutils2.FluentPropertyBeanIntrospector(String) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [76](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/FluentPropertyBeanIntrospector.html#L76) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.lazydynabean"></a>

## org.apache.commons.beanutils2.LazyDynaBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.LazyDynaBean.getDynaClass() may expose internal representation by returning LazyDynaBean.dynaClass | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [568](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L568) | Medium |
| org.apache.commons.beanutils2.LazyDynaBean.getMap() may expose internal representation by returning LazyDynaBean.mapDecorator | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [587](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L587) | Medium |
| new org.apache.commons.beanutils2.LazyDynaBean(DynaClass) may expose internal representation by storing an externally mutable object into LazyDynaBean.dynaClass | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [185](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaBean.html#L185) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.lazydynalist"></a>

## org.apache.commons.beanutils2.LazyDynaList

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.LazyDynaList at new org.apache.commons.beanutils2.LazyDynaList(Class) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [198](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaList.html#L198) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.LazyDynaList at new org.apache.commons.beanutils2.LazyDynaList(DynaClass) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [217](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaList.html#L217) | Medium |
| org.apache.commons.beanutils2.LazyDynaList doesn't override java.util.ArrayList.equals(Object) | STYLE | [EQ\_DOESNT\_OVERRIDE\_EQUALS](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EQ_DOESNT_OVERRIDE_EQUALS) | [1](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaList.html#L1) | Medium |
| Public method org.apache.commons.beanutils2.LazyDynaList.setElementType(Class) uses reflection to create a class it gets in its parameter which could increase the accessibility of any class | MALICIOUS\_CODE | [REFLC\_REFLECTION\_MAY\_INCREASE\_ACCESSIBILITY\_OF\_CLASS](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#REFLC_REFLECTION_MAY_INCREASE_ACCESSIBILITY_OF_CLASS) | [471](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaList.html#L471) | Medium |
| Class org.apache.commons.beanutils2.LazyDynaList defines non-transient non-serializable instance field elementDynaClass | BAD\_PRACTICE | [SE\_BAD\_FIELD](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#SE_BAD_FIELD) | Not available | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.lazydynamap"></a>

## org.apache.commons.beanutils2.LazyDynaMap

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.LazyDynaMap at new org.apache.commons.beanutils2.LazyDynaMap(String, DynaProperty[]) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [125](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L125) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.LazyDynaMap at new org.apache.commons.beanutils2.LazyDynaMap(DynaClass) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [85](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L85) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.LazyDynaMap at new org.apache.commons.beanutils2.LazyDynaMap(DynaProperty[]) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [94](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L94) | Medium |
| org.apache.commons.beanutils2.LazyDynaMap.getMap() may expose internal representation by returning LazyDynaBean.values | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [279](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L279) | Medium |
| new org.apache.commons.beanutils2.LazyDynaMap(String, Map) may expose internal representation by storing an externally mutable object into LazyDynaMap.dynaClass | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [139](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L139) | Medium |
| org.apache.commons.beanutils2.LazyDynaMap.setMap(Map) may expose internal representation by storing an externally mutable object into LazyDynaMap.values | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [402](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/LazyDynaMap.html#L402) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.mappedpropertydescriptor"></a>

## org.apache.commons.beanutils2.MappedPropertyDescriptor

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.MappedPropertyDescriptor at new org.apache.commons.beanutils2.MappedPropertyDescriptor(String, Class) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [276](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L276) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.MappedPropertyDescriptor at new org.apache.commons.beanutils2.MappedPropertyDescriptor(String, Class, String, String) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [327](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L327) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.MappedPropertyDescriptor at new org.apache.commons.beanutils2.MappedPropertyDescriptor(String, Method, Method) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [360](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L360) | Medium |
| org.apache.commons.beanutils2.MappedPropertyDescriptor doesn't override java.beans.PropertyDescriptor.equals(Object) | STYLE | [EQ\_DOESNT\_OVERRIDE\_EQUALS](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EQ_DOESNT_OVERRIDE_EQUALS) | [1](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/MappedPropertyDescriptor.html#L1) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.propertyutilsbean"></a>

## org.apache.commons.beanutils2.PropertyUtilsBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Do not catch NullPointerException like in org.apache.commons.beanutils2.PropertyUtilsBean.invokeMethod(Method, Object, Object[]) | STYLE | [DCN\_NULLPOINTER\_EXCEPTION](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#DCN_NULLPOINTER_EXCEPTION) | [1024](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L1024) | Medium |
| org.apache.commons.beanutils2.PropertyUtilsBean.getResolver() may expose internal representation by returning PropertyUtilsBean.resolver | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [918](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L918) | Medium |
| org.apache.commons.beanutils2.PropertyUtilsBean.setResolver(Resolver) may expose internal representation by storing an externally mutable object into PropertyUtilsBean.resolver | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [1561](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/PropertyUtilsBean.html#L1561) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.wrapdynabean"></a>

## org.apache.commons.beanutils2.WrapDynaBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Do not catch NullPointerException like in org.apache.commons.beanutils2.WrapDynaBean.get(String) | STYLE | [DCN\_NULLPOINTER\_EXCEPTION](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#DCN_NULLPOINTER_EXCEPTION) | [110](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/WrapDynaBean.html#L110) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.converters.abstractconverter"></a>

## org.apache.commons.beanutils2.converters.AbstractConverter

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.converters.AbstractConverter at new org.apache.commons.beanutils2.converters.AbstractConverter(Object) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [119](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/AbstractConverter.html#L119) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.converters.arrayconverter"></a>

## org.apache.commons.beanutils2.converters.ArrayConverter

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.converters.ArrayConverter at new org.apache.commons.beanutils2.converters.ArrayConverter(Class, Converter) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [125](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/ArrayConverter.html#L125) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.converters.ArrayConverter at new org.apache.commons.beanutils2.converters.ArrayConverter(Class, Converter, int) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [140](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/ArrayConverter.html#L140) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.converters.datetimeconverter"></a>

## org.apache.commons.beanutils2.converters.DateTimeConverter

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.converters.DateTimeConverter.getTimeZone() may expose internal representation by returning DateTimeConverter.timeZone | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [334](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/DateTimeConverter.html#L334) | Medium |
| org.apache.commons.beanutils2.converters.DateTimeConverter.setTimeZone(TimeZone) may expose internal representation by storing an externally mutable object into DateTimeConverter.timeZone | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [480](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/converters/DateTimeConverter.html#L480) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.locale.localebeanutilsbean"></a>

## org.apache.commons.beanutils2.locale.LocaleBeanUtilsBean

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.locale.LocaleBeanUtilsBean.getLocaleConvertUtils() may expose internal representation by returning LocaleBeanUtilsBean.localeConvertUtils | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [331](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/locale/LocaleBeanUtilsBean.html#L331) | Medium |
| new org.apache.commons.beanutils2.locale.LocaleBeanUtilsBean(LocaleConvertUtilsBean) may expose internal representation by storing an externally mutable object into LocaleBeanUtilsBean.localeConvertUtils | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [94](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/locale/LocaleBeanUtilsBean.html#L94) | Medium |
| new org.apache.commons.beanutils2.locale.LocaleBeanUtilsBean(LocaleConvertUtilsBean, ConvertUtilsBean, PropertyUtilsBean) may expose internal representation by storing an externally mutable object into LocaleBeanUtilsBean.localeConvertUtils | MALICIOUS\_CODE | [EI\_EXPOSE\_REP2](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP2) | [107](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/locale/LocaleBeanUtilsBean.html#L107) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.sql.resultsetdynaclass"></a>

## org.apache.commons.beanutils2.sql.ResultSetDynaClass

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.sql.ResultSetDynaClass at new org.apache.commons.beanutils2.sql.ResultSetDynaClass(ResultSet, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [123](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/ResultSetDynaClass.html#L123) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.sql.ResultSetDynaClass at new org.apache.commons.beanutils2.sql.ResultSetDynaClass(ResultSet, boolean, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [149](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/ResultSetDynaClass.html#L149) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.sql.resultsetiterator"></a>

## org.apache.commons.beanutils2.sql.ResultSetIterator

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| org.apache.commons.beanutils2.sql.ResultSetIterator.getDynaClass() may expose internal representation by returning ResultSetIterator.dynaClass | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [157](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/ResultSetIterator.html#L157) | Medium |

<a id="spotbugs--org.apache.commons.beanutils2.sql.rowsetdynaclass"></a>

## org.apache.commons.beanutils2.sql.RowSetDynaClass

| Bug | Category | Details | Line | Priority |
| --- | --- | --- | --- | --- |
| Exception thrown in class org.apache.commons.beanutils2.sql.RowSetDynaClass at new org.apache.commons.beanutils2.sql.RowSetDynaClass(ResultSet, boolean, int) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [156](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/RowSetDynaClass.html#L156) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.sql.RowSetDynaClass at new org.apache.commons.beanutils2.sql.RowSetDynaClass(ResultSet, boolean, int, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [185](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/RowSetDynaClass.html#L185) | Medium |
| Exception thrown in class org.apache.commons.beanutils2.sql.RowSetDynaClass at new org.apache.commons.beanutils2.sql.RowSetDynaClass(ResultSet, boolean, boolean) will leave the constructor. The object under construction remains partially initialized and may be vulnerable to Finalizer attacks. | BAD\_PRACTICE | [CT\_CONSTRUCTOR\_THROW](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#CT_CONSTRUCTOR_THROW) | [134](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/RowSetDynaClass.html#L134) | Medium |
| org.apache.commons.beanutils2.sql.RowSetDynaClass.getRows() may expose internal representation by returning RowSetDynaClass.rows | MALICIOUS\_CODE | [EI\_EXPOSE\_REP](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html#EI_EXPOSE_REP) | [250](https://commons.apache.org/proper/commons-beanutils/xref/org/apache/commons/beanutils2/sql/RowSetDynaClass.html#L250) | Medium |

---
