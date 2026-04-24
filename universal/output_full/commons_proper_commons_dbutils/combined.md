# DbUtils – Project Information

## Navigation

- [DbUtils](#japicmp)
  - [Overview](#index)
  - [Download](https://commons.apache.org/dbutils/download_dbutils.cgi)
  - [Examples](#examples)
  - [Release Notes](#changes-report)
  - [Dependencies](#dependencies)
  - [Wiki](http://wiki.apache.org/commons/DbUtils)
- Development
  - [Mailing Lists](https://commons.apache.org/proper/commons-dbutils/mail-lists.html)
  - [Issue Tracking](#issue-tracking)
  - [Source Repository](#scm)
  - [Building](#building)
  - [Javadoc](https://commons.apache.org/proper/commons-dbutils/apidocs/index.html)
  - [Javadoc Archive](https://javadoc.io/doc/commons-dbutils/commons-dbutils/latest/index.html)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [Issue Management](#issue-management)
    - [Mailing Lists](https://commons.apache.org/proper/commons-dbutils/mailing-lists.html)
    - [Dependency Information](#dependency-info)
    - [Dependency Management](#dependency-management)
    - [Dependencies](#dependencies)
    - [Dependency Convergence](#dependency-convergence)
    - [CI Management](#ci-management)
    - [Distribution Management](#distribution-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes-report)
    - [JIRA Report](#jira-report)
    - [Javadoc](https://commons.apache.org/proper/commons-dbutils/apidocs/index.html)
    - [Source Xref](https://commons.apache.org/proper/commons-dbutils/xref/index.html)
    - [Test Source Xref](https://commons.apache.org/proper/commons-dbutils/xref-test/index.html)
    - [Surefire](#surefire-report)
    - [Rat Report](#rat-report)
    - [JaCoCo](https://commons.apache.org/proper/commons-dbutils/jacoco/index.html)
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

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/japicmp.html -->

<!-- page_index: 1 -->

# DbUtils –

Comparing source compatibility of commons-dbutils-1.8.1.jar against commons-dbutils-1.8.0.jar

|  |  |
| --- | --- |
| Old: | commons-dbutils-1.8.0.jar |
| New: | commons-dbutils-1.8.1.jar |
| Created: | 2023-09-15T07:54:41.640-0400 |
| Access modifier filter: | PROTECTED |
| Only modifications: | true |
| Only binary incompatible modifications: | false |
| Ignore missing classes: | false |
| Includes: | all |
| Excludes: | n.a. |
| Semantic Versioning: | 0.0.0 |

Classes:

| Status | Fully Qualified Name |
| --- | --- |

Binary incompatible changes are marked with (!) while source incompatible changes are marked with (\*).

---

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/index.html -->

<!-- page_index: 2 -->

# DbUtils – JDBC Utility Component

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Commons_DbUtils:_JDBC_Utility_Component"></a>Commons DbUtils: JDBC Utility Component</h2>
<p>
The Commons DbUtils library is a small set of classes designed to make working with
<a href="http://java.sun.com/products/jdbc/">JDBC</a> easier.  JDBC
resource cleanup code is mundane, error prone work so these classes
abstract out all of the cleanup tasks from your code leaving you with
what you really wanted to do with JDBC in the first place: query and
update data.
</p>
<p>Some of the advantages of using DbUtils are:</p>
<ul>
<li>
        No possibility for resource leaks.  Correct JDBC coding isn't
        difficult but it is time-consuming and tedious.  This often
        leads to connection leaks that may be difficult to track down.
    </li>
<li>
        Cleaner, clearer persistence code.  The amount of code needed
        to persist data in a database is drastically reduced. The remaining
        code clearly expresses your intention without being cluttered
        with resource cleanup.
    </li>
<li>
        Automatically populate JavaBean properties from ResultSets.  You
        don't need to manually copy column values into bean instances
        by calling setter methods.  Each row of the ResultSet can be
        represented by one fully populated bean instance.
    </li>
</ul>
</section>
<section>
<h2><a name="Scope_of_the_Package"></a>Scope of the Package</h2>
<p>
DbUtils is designed to be:
</p>
<ul>
<li>
<b>Small</b> - you should be able to understand the
        whole package in a short amount of time.
    </li>
<li>
<b>Transparent</b> - DbUtils doesn't do any magic
        behind the scenes.  You give it a query, it executes it and
        cleans up for you.
    </li>
<li>
<b>Fast</b> - You don't need to create a million
        temporary objects to work with DbUtils.
    </li>
</ul>
<p>
DbUtils is <b>not</b>:
</p>
<ul>
<li>
        An Object/Relational bridge - there are plenty of good O/R tools
        already.  DbUtils is for developers looking to use JDBC without all
        the mundane pieces.
    </li>
<li>
        A Data Access Object (DAO) framework - DbUtils can be used to build
        a DAO framework though.
    </li>
<li>
        An object oriented abstraction of general database
        objects like a Table, Column, or PrimaryKey.
    </li>
<li>
        A heavyweight framework of any kind - the goal here is to be a
        straightforward and easy to use JDBC helper library.
    </li>
</ul>
</section>
<section>
<h2><a name="Example_Usage"></a>Example Usage</h2>
<p>
Please see <a href="#examples">Examples Page</a>.
</p>
</section>
<section>
<h2><a name="Dependencies"></a>Dependencies</h2>
<p>
    DbUtils is intentionally a single jar distribution and relies only on
    a standard Java 8 or later JRE.
    </p>
</section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/examples.html -->

<!-- page_index: 3 -->

# DbUtils – JDBC Utility Component -- Examples

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="DbUtils:_JDBC_Utility_Component_Examples"></a>DbUtils: JDBC Utility Component Examples</h2>
<p>
This page provides examples that show how DbUtils may be used.
</p>
</section>
<section>
<h2><a name="Basic_Usage"></a>Basic Usage</h2>
<p>
DbUtils is a very small library of classes so it won't take long
to go through the <a href="https://commons.apache.org/proper/commons-dbutils/apidocs/">javadocs</a> for each class. The core classes/interfaces in DbUtils are
<code><a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/QueryRunner.html">QueryRunner</a></code>
and
<code><a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/ResultSetHandler.html">ResultSetHandler</a></code>.
You don't need to know about any other DbUtils classes to benefit from using the
library.  The following example demonstrates how these classes are used together.
</p>
<div>
<pre>

// Create a ResultSetHandler implementation to convert the
// first row into an Object[].
ResultSetHandler&lt;Object[]&gt; h = new ResultSetHandler&lt;Object[]&gt;() {
    public Object[] handle(ResultSet rs) throws SQLException {
        if (!rs.next()) {
            return null;
        }

        ResultSetMetaData meta = rs.getMetaData();
        int cols = meta.getColumnCount();
        Object[] result = new Object[cols];

        for (int i = 0; i &lt; cols; i++) {
            result[i] = rs.getObject(i + 1);
        }

        return result;
    }
};

// Create a QueryRunner that will use connections from
// the given DataSource
QueryRunner run = new QueryRunner(dataSource);

// Execute the query and get the results back from the handler
Object[] result = run.query(
    "SELECT * FROM Person WHERE name=?", h, "John Doe");

</pre></div>
<p>
You could also perform the previous query using a <code>java.sql.Connection</code> object
instead of a <code>DataSource</code>.  Notice that you are responsible for closing the
<code>Connection</code> in this example.
</p>
<div>
<pre>

ResultSetHandler&lt;Object[]&gt; h = ... // Define a handler the same as above example

// No DataSource so we must handle Connections manually
QueryRunner run = new QueryRunner();

Connection conn = ... // open a connection
try{
    Object[] result = run.query(
        conn, "SELECT * FROM Person WHERE name=?", h, "John Doe");
    // do something with the result
} finally {
    // Use this helper method so we don't have to check for null
    DbUtils.close(conn);
}

</pre></div>
<p>
  You can not only fetch data from the database - you can also insert or update
  data. The following example will first insert a person into the database and
  after that change the person's height.
</p>
<div>
<pre>

QueryRunner run = new QueryRunner( dataSource );
try
{
    // Execute the SQL update statement and return the number of
    // inserts that were made
    int inserts = run.update( "INSERT INTO Person (name,height) VALUES (?,?)",
                              "John Doe", 1.82 );
    // The line before uses varargs and autoboxing to simplify the code

    // Now it's time to rise to the occation...
    int updates = run.update( "UPDATE Person SET height=? WHERE name=?",
                              2.05, "John Doe" );
    // So does the line above
}
catch(SQLException sqle) {
    // Handle it
}

</pre></div>
<p>
  For long running calls you can use the <code>AsyncQueryRunner</code> to execute
  the calls asynchronously. The <code>AsyncQueryRunner</code> class has the same
  methods as the <code>QueryRunner</code> calls; however, the methods return a
  <code>Callable</code>.
</p>
<div>
<pre>

ExecutorCompletionService&lt;Integer&gt; executor =
    new ExecutorCompletionService&lt;Integer&gt;( Executors.newCachedThreadPool() );
AsyncQueryRunner asyncRun = new AsyncQueryRunner( dataSource );

try
{
    // Create a Callable for the update call
    Callable&lt;Integer&gt; callable = asyncRun.update( "UPDATE Person SET height=? WHERE name=?",
                                                  2.05, "John Doe" );
    // Submit the Callable to the executor
    executor.submit( callable );
} catch(SQLException sqle) {
    // Handle it
}

// Sometime later (or in another thread)
try
{
   // Get the result of the update
   Integer updates = executor.take().get();
} catch(InterruptedException ie) {
    // Handle it
}

</pre></div>
</section>
<section>
<h2><a name="ResultSetHandler_Implementations"></a>ResultSetHandler Implementations</h2>
<p>
In the examples above we implemented the <code>ResultSetHandler</code> interface
to turn the first row of the <code>ResultSet</code> into an Object[].  This is a
fairly generic implementation that can be reused across many projects.
In recognition of this DbUtils provides a set of <code>ResultSetHandler</code>
implementations in the
<a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/handlers/package-summary.html">org.apache.commons.dbutils.handlers</a>
package that perform common transformations into arrays, Maps, and JavaBeans.
There is a version of each implementation that converts just the first row and
another that converts all rows in the <code>ResultSet</code>.
</p>
<p>
  We'll start with an example using the <code>BeanHandler</code> to fetch one
  row from the <code>ResultSet</code> and turn it into a JavaBean.
</p>
<div>
<pre>

QueryRunner run = new QueryRunner(dataSource);

// Use the BeanHandler implementation to convert the first
// ResultSet row into a Person JavaBean.
ResultSetHandler&lt;Person&gt; h = new BeanHandler&lt;Person&gt;(Person.class);

// Execute the SQL statement with one replacement parameter and
// return the results in a new Person object generated by the BeanHandler.
Person p = run.query(
    "SELECT * FROM Person WHERE name=?", h, "John Doe");

</pre></div>
<p>
  This time we will use the BeanListHandler to fetch all rows from the
  <code>ResultSet</code> and turn them into a <code>List</code> of JavaBeans.
</p>
<div>
<pre>

QueryRunner run = new QueryRunner(dataSource);

// Use the BeanListHandler implementation to convert all
// ResultSet rows into a List of Person JavaBeans.
ResultSetHandler&lt;List&lt;Person&gt;&gt; h = new BeanListHandler&lt;Person&gt;(Person.class);

// Execute the SQL statement and return the results in a List of
// Person objects generated by the BeanListHandler.
List&lt;Person&gt; persons = run.query("SELECT * FROM Person", h);

</pre></div>
</section>
<section>
<h2><a name="Custom_RowProcessor"></a>Custom RowProcessor</h2>
<p>
Each of the provided <code>ResultSetHandler</code> implementations accept a
<a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/RowProcessor.html">RowProcessor</a>
to do the actual conversion of rows into objects.  By default the handlers
use the <a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BasicRowProcessor.html">BasicRowProcessor</a>
implementation but you can implement a custom version to plug in.
Probably the most common customization is to implement the <code>toBean()</code>
method to handle custom database datatype issues.
</p>
</section>
<section>
<h2><a name="Custom_BeanProcessor"></a>Custom BeanProcessor</h2>
<p>
<code>BasicRowProcessor</code> uses a <a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BeanProcessor.html">BeanProcessor</a>
to convert <code>ResultSet</code> columns into JavaBean properties.  You can
subclass and override processing steps to handle datatype mapping specific to
your application.  The provided implementation delegates datatype conversion to
the JDBC driver.
</p>
<p>
BeanProcessor maps columns to bean properties as documented in the
<a href="https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BeanProcessor.html#toBeanjava.sql.ResultSet20java.lang.Class">BeanProcessor.toBean()</a> javadoc. Column names must match the bean's property names case insensitively. For example, the <code>firstname</code> column would be stored in the bean
by calling its <code>setFirstName()</code> method.  However, many database
column names include characters that either can't be used or are not typically
used in Java method names.  You can do one of the following to map
these columns to bean properties:
</p>
</section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="changes-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/changes-report.html -->

<!-- page_index: 4 -->

# DbUtils – Apache Commons DBUtils Release Notes

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Apache_Commons_DBUtils_Release_Notes"></a>Apache Commons DBUtils Release Notes</h2><section>
<h3><a name="Release_History"></a>Release History</h3>
<table>
<tr>
<th>Version</th>
<th>Date</th>
<th>Description</th></tr>
<tr>
<td><a href="#changes-report--a1.8.1">1.8.1</a></td>
<td>2023-09-09</td>
<td>New features and bug fixes.</td></tr>
<tr>
<td><a href="#changes-report--a1.8.0">1.8.0</a></td>
<td>2023-08-01</td>
<td>New features and bug fixes.</td></tr>
<tr>
<td><a href="#changes-report--a1.7">1.7</a></td>
<td>2017-07-20</td>
<td>Bug fixes and separate column &amp; property handlers using SPI</td></tr>
<tr>
<td><a href="#changes-report--a1.6">1.6</a></td>
<td>2014-07-20</td>
<td>Bug fixes and addition of insert methods</td></tr>
<tr>
<td><a href="#changes-report--a1.5">1.5</a></td>
<td>2012-07-20</td>
<td>Bug fixes and addition of BeanMapHandler</td></tr>
<tr>
<td><a href="#changes-report--a1.4">1.4</a></td>
<td>2011-10-23</td>
<td>Bug fixes and addition of asynchronous QueryLoader</td></tr>
<tr>
<td><a href="#changes-report--a1.3">1.3</a></td>
<td>2009-11-04</td>
<td>Adds Java5 generics and varargs</td></tr>
<tr>
<td><a href="#changes-report--a1.2">1.2</a></td>
<td>2009-03-06</td>
<td>Another round of fixes; deprecates methods in preparation for varargs in java5</td></tr>
<tr>
<td><a href="#changes-report--a1.1">1.1</a></td>
<td>2006-12-01</td>
<td>Last couple of years of fixes</td></tr>
<tr>
<td><a href="#changes-report--a1.0">1.0</a></td>
<td>2003-11-10</td>
<td>First release of DbUtils</td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN0END<h3 id="a1.8.1">Release 1.8.1 – 2023-09-09</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Module org.apache.commons.dbutils does not declare `uses`. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-151">DBUTILS-151</a>. Thanks to mark, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump commons-parent from 61 to 62. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN1END<h3 id="a1.8.0">Release 1.8.0 – 2023-08-01</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Speedup query calls without parameters; Use PreparedStatement only when parameters are present. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-131">DBUTILS-131</a>. Thanks to yairlenga.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Always copy Date, Time, Timestamp on get and set in SqlNullCheckedResultSet.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>BeanProcessor is not thread safe since [DBUTILS-124]. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-135">DBUTILS-135</a>. Thanks to hdevalke.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Inefficient allocation of Maps in org.apache.commons.dbutils.BasicRowProcessor.toMap(ResultSet). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-137">DBUTILS-137</a>. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>org.apache.commons.dbutils.QueryRunner.query(Connection, boolean, String, ResultSetHandler, Object...) Exception in closing statement leave connections open. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-138">DBUTILS-138</a>. Thanks to Stefano Lissa, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Update Java requirement from version 6 to 8. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-139">DBUTILS-139</a>. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>clirr, checkstyle, and spotbugs configured as part of default build. Thanks to thecarlhall.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Correction of coverage badge #10. Thanks to Amey Jadiye.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Manage JDBC objects using try-with-resources. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>ResultSet not closed in QueryRunner.insert(Connection, String, ResultSetHandler, Object...). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>ResultSet not closed in QueryRunner.insertBatch(Connection, String, ResultSetHandler, Object[][]). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>AbstractQueryRunner.fillStatementWithBean(PreparedStatement, Object, String...) now throws IllegalStateException instead of RuntimeException. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add @Column annotation to hint the field name instead of dissecting the get method name. Fixes <a href="https://issues.apache.org/jira/browse/PR/9">PR/9</a>. Thanks to rewerma.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>CaseInsensitiveHashMap cannot be accessed by subclasses of BasicRowProcessor; add org.apache.commons.dbutils.BasicRowProcessor.createCaseInsensitiveHashMap(int). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-136">DBUTILS-136</a>. Thanks to Matthew Hall, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add github/codeql-action #115.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>[StepSecurity] ci: Harden GitHub Actions #191. Thanks to step-security-bot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add StatementConfiguration.StatementConfiguration(Integer, Integer, Integer, Integer, Duration). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add StatementConfiguration.getQueryTimeoutDuration(). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add StatementConfiguration.Builder.queryTimeout(Duration). Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump actions/cache from 2 to 3.0.11 #109, #141, #145. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump actions/checkout from 1 to 3.1.10, #44, #23, #48, #75, #93, #143. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump actions/setup-java from 1.4.0 to 3.5.1 #40. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump actions/upload-artifact from 3.1.0 to 3.1.1 #150. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump commons-parent from 50 to 61 #14, #113, #139, #168, #189. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump junit from 4.12 to 5.9.1 vintage #16, #42, #58. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump mockito-core from 3.2.4 to 4.8.1 #18, #21, #46, #53, #97, #103, #111, #116, #122, #131. #137, #151. Thanks to Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump spotbugs-maven-plugin from 3.1.12.2 to 4.4.2, #17, #45, #52. Thanks to Dependabot, Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump spotbugs from 3.1.12.2 to 4.2.3. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump maven-checkstyle-plugin from 3.1.0 to 3.2.0 #56, #132. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump checkstyle from 8.28 to 9.3 #20, #47. Thanks to Gary Gregory, Dependabot.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Bump commons.japicmp.version from 0.14.3 to 0.16.0. Thanks to Gary Gregory.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory">ggregory</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN2END<h3 id="a1.7">Release 1.7 – 2017-07-20</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Error handling possible getParameterMetaData() results
        - allow for null return
        - handle SQLFeatureNotSupportedException. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-117">DBUTILS-117</a>. Thanks to Vadim Smirnov.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb">sebb</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Correct errors in BeanMapHandler Javadoc. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-119">DBUTILS-119</a>. Thanks to Michael Akerman.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add getWriteMethod to BeanProcessor to allow subclasses to influence which write method is used. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-121">DBUTILS-121</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Change method contracts to allow extended class types when returning a bean populated from a query. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-82">DBUTILS-82</a>. Thanks to Kenshi Toriumi.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Add method in BeanProcessor to populate an existing bean. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-89">DBUTILS-89</a>. Thanks to Adam Dyga.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Add ability to configure statements used in QueryRunner. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-70">DBUTILS-70</a>. Thanks to Michael Akerman.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Support CallableStatement "out" parameters. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-50">DBUTILS-50</a>. Thanks to Dan Fabulich.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Implement column and property handlers using Java's service interfaces. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-124">DBUTILS-124</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Created some Unit Tests to increase code coverage. Fixes <a href="https://issues.apache.org/jira/browse/PR/1">PR/1</a>. Thanks to Michael Hausegger.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall">thecarlhall</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN3END<h3 id="a1.6">Release 1.6 – 2014-07-20</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>ArrayHandler should return an empty array when handle has no rows. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-110">DBUTILS-110</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Order of columns not retained in BasicRowProcessor with HashMap. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-114">DBUTILS-114</a>. Thanks to Michael Osipov.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>BeanProcessor not returning nanoseconds. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-118">DBUTILS-118</a>. Thanks to Feysal Rujbally, Daniele Cremonini.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add support for conversion of ResultSet strings to enums in the BeanProcessor. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-113">DBUTILS-113</a>. Thanks to Graylin Kim, Michael Osipov.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#britter">britter</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>In BeanProcessor#isCompatibleType, can Integer.class.isInstance(value) be replaced by value instanceof Integer (etc)?
        Simplified code by using instanceof. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-85">DBUTILS-85</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb">sebb</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>DBUtils can't build using JDK 1.7 - DriverProxy needs to implement getParentLogger()
        Add dynamic invocation. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-106">DBUTILS-106</a>. Thanks to Niall Pemberton.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb">sebb</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Create functionality to return auto-generated keys in batches of SQL inserts. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-108">DBUTILS-108</a>. Thanks to Micah Huff.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Patch QueryLoader to also load from XML properties files. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-107">DBUTILS-107</a>. Thanks to PB.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Updated the use of getColumnName to try getColumnLabel first. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-100">DBUTILS-100</a>. Thanks to xiaofei.xu.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add missing Javadoc to QueryRunner#insert. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-98">DBUTILS-98</a>. Thanks to Moandji Ezana.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi">simonetripodi</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add an Abstract ResultSetHandler implementation in order to reduce redundant 'resultSet' variable invocation. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-97">DBUTILS-97</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi">simonetripodi</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>DbUtils#loadDriver(ClassLoader,String) makes DriverManager throwing "No suitable driver found for jdbc"
        if ClassLoader is not the System's one. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-96">DBUTILS-96</a>. Thanks to yuyf.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi">simonetripodi</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added insert methods to QueryRunner and AsyncQueryRunner that return the generated key. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-87">DBUTILS-87</a>. Thanks to Moandji Ezana.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN4END<h3 id="a1.5">Release 1.5 – 2012-07-20</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Provide test coverage for org.apache.commons.dbutils.DbUtils. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-94">DBUTILS-94</a>. Thanks to Benedikt Ritter.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi">simonetripodi</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Source assembly artifact fails to build a site because of missing pmd-ruleset.xml. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-93">DBUTILS-93</a>. Thanks to Stevo Slavic.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi">simonetripodi</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Enhance BasicRowProcessor to have row mapping easier to configure. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-91">DBUTILS-91</a>. Thanks to Stevo Slavic.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi">simonetripodi</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Updated pom.xml: Java 1.6 now required, clirr and compiler plugin removed Thanks to wspeirs.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>BeanProcessor method processColumn should take SQLXML in consideration. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-84">DBUTILS-84</a>. Thanks to Tiago Cavaleiro.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Updated documentation to better reflect the use of pmdKnownBroken. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-77">DBUTILS-77</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Added a fixed Locale (Locale.ENGLISH) to all toLowerCase calls in BasicRowProcessor. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-73">DBUTILS-73</a>. Thanks to Sebb.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added BeanMapHandler. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-67">DBUTILS-67</a>. Thanks to Michael Osipov.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Added generics to ScalarHandler, ColumnHandler, and KeyedHandler. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-66">DBUTILS-66</a>. Thanks to Michael Osipov.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN5END<h3 id="a1.4">Release 1.4 – 2011-10-23</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>DbUtils.loadDriver() uses Class.forName(). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-81">DBUTILS-81</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>DbUtils.loadDriver catches Throwable. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-80">DBUTILS-80</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Duplicate code introduced during Java 1.5 branch merge. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-65">DBUTILS-65</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>fillStatement doesn't complain when there are too few parameters. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-79">DBUTILS-79</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>efficient usage from findbugs. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-75">DBUTILS-75</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Add asynchronous batch, query, and update calls. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-78">DBUTILS-78</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs">wspeirs</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN6END<h3 id="a1.3">Release 1.3 – 2009-11-04</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Java 1.5 generics and varargs. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-48">DBUTILS-48</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>BeanProcessor#mapColumnsToProperties now prefers to use column labels over column names (where aliases are not set, these should be identical). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-57">DBUTILS-57</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Setting pmdKnownBroken in QueryRunner constructor now completely ignores ParameterMetaData. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-58">DBUTILS-58</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Fixed error message in QueryRunner#rethrow. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-60">DBUTILS-60</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN7END<h3 id="a1.2">Release 1.2 – 2009-03-06</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Removed setDataSource method to guarantee thread safety. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-52">DBUTILS-52</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Made numerous private instance members final to guarantee thread safety; changed protected member of KeyedHandler to final. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-51">DBUTILS-51</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb">sebb</a></td></tr>
<tr>
<td><img alt="Remove" src="assets/images/remove_c1d2fa9bb9722223.gif" title="Remove"/></td>
<td>Remove old Maven1/Ant build scripts</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Support bean property to SQL IN parameter mapping. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-29">DBUTILS-29</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>fillStatement setNull bug with the Postgres/Derby JDBC driver (and others). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-31">DBUTILS-31</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Make GenericListHandler (now AbstractListHandler) public. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-33">DBUTILS-33</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>BasicRowProcessor loses any information on database field case. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-34">DBUTILS-34</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>BeanListHandler#handle(ResultSet) is not optimal. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-37">DBUTILS-37</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>NullPointerException occurred at rethrow method. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-40">DBUTILS-40</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Object with Long or Decimal got initial zero value while database field is null. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-42">DBUTILS-42</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich">dfabulich</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>example documentation page, update query. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-38">DBUTILS-38</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dennisl">dennisl</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Add serialVersionUID to BasicRowProcessor.CaseInsensitiveHashMap. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-36">DBUTILS-36</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN8END<h3 id="a1.1">Release 1.1 – 2006-12-01</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Tests fail to build under 1.6, and warning while compiling source. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-32">DBUTILS-32</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>BeanListHandler and BeanHandler fail to support java.sql.Date(). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-1">DBUTILS-1</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>ResultSetRowProcessor abstract handler and some classes rework. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-16">DBUTILS-16</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>Setting bean properties fails silently. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-3">DBUTILS-3</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>MockResultSet needs to handle equals and hashCode. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-9">DBUTILS-9</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Fix" src="assets/images/fix_ebcdbb03944a8118.gif" title="Fix"/></td>
<td>MockResultSet: Throw UnsupportedOperationException for not implemented methods. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-7">DBUTILS-7</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard">bayard</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Implement Pluggable Adaptors to Make BeanHandler Smarter. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-20">DBUTILS-20</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Patch for extending BasicRowProcessor. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-15">DBUTILS-15</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Protected QueryRunner.close() methods. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-12">DBUTILS-12</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Updated docs for example.html page (select AS). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-23">DBUTILS-23</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added protected ResultSetIterator.rethrow() method to wrap SQLExceptions in
        RuntimeExceptions. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-4">DBUTILS-4</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Added SQLState and error code to rethrown SQLExceptions. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-5">DBUTILS-5</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added KeyedHandler to create a Map of Maps from a ResultSet. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-25">DBUTILS-25</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Use current class' ClassLoader instead of QueryLoader's ClassLoader
        in loadQueries(). Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-2">DBUTILS-2</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Made QueryLoader.loadQueries() protected so subclasses can use query
        repositories other than properties files. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-22">DBUTILS-22</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>QueryRunner now calls getDataSource() internally any time it needs access
        to its DataSource object to allow subclasses to provide different behavior.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added DbUtils.rollbackAndClose() and DbUtils.rollbackAndCloseQuietly().</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Call ResultSet.getTimestamp() in BeanProcessor.processColumn() if
        the bean property is a java.sql.Timestamp.  Oracle's getObject()
        implementation returns its own incompatible Timestamp class. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-26">DBUTILS-26</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Update" src="assets/images/update_73f35d1297a2940f.gif" title="Update"/></td>
<td>Changed QueryRunner.fillStatement() null handling
        to use Types.VARCHAR instead of Types.OTHER.  This works for the
        following tested drivers: Firebird 1.5/firebirdsql 1.5RC3,
        Oracle 9/ Thin driver, MySQL 4.0/Msql Connecttor 3.0 and mm.mysql
        2.0.4 MaxDB 7.5, HSQLDB 1.7.1, and MS Access/ODBC Bridge. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-18">DBUTILS-18</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added a protected QueryRunner.prepareConnection() method to
        allow subclasses to customize the Connections retrieved from
        the DataSource before they're used. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-21">DBUTILS-21</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Refactored bean handling from BasicRowProcessor into new
        BeanProcessor class.  This also fixes the common problem with
        Oracle NUMERIC fields not being set into bean properties.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added QueryRunner.batch() methods for batch updates. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-13">DBUTILS-13</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Added new ResultSetHandler implementation, ColumnListHandler, that
        converts one ResultSet column into a List of Objects. Fixes <a href="https://issues.apache.org/jira/browse/DBUTILS-11">DBUTILS-11</a>.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham">dgraham</a></td></tr></table></section><section>
DOC2MDPLACEHOLDERTOKEN9END<h3 id="a1.0">Release 1.0 – 2003-11-10</h3>
<table>
<tr>
<th>Type</th>
<th>Changes</th>
<th>By</th></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>This is the first release of the Commons DbUtils package.  DbUtils
        is a small set of classes designed to make working with JDBC easier.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>QueryRunner class with ResultSetHandler interface allow you to easily query or
        update a database and handle the ResultSet.  Several useful implementations
        of the ResultSetHandler interface are located in the
        org.apache.commons.dbutils.handlers.* package.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>ResultSet wrappers that decorate ResultSets with specialized
        behavior.  See the classes in the org.apache.commons.dbutils.wrappers.*
        package for details.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr>
<tr>
<td><img alt="Add" src="assets/images/add_17562975ed428aad.gif" title="Add"/></td>
<td>Dynamic JDBC API interface implementations via the standard
        java.lang.reflect.Proxy class.  This allows you to implement JDBC
        interfaces such as ResultSet at runtime to avoid API version
        incompatibilities.  See org.apache.commons.dbutils.ProxyFactory
        for details.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/team-list.html#null"></a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependencies"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/dependencies.html -->

<!-- page_index: 5 -->

# DbUtils – Project Dependencies

<table class="layout-table">
<tr>
<td>
</td>
<td>
<a name="Project_Dependencies"></a><section>
<h2><a name="Project_Dependencies"></a>Project Dependencies</h2><a name="Project_Dependencies_test"></a><section>
<h3><a name="test"></a>test</h3>
<p>The following is a list of test dependencies for this project. These dependencies are only required to compile and run unit tests for the application:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>Licenses</th></tr>
<tr>
<td align="left">org.hamcrest</td>
<td><a href="https://github.com/hamcrest/JavaHamcrest/hamcrest-all">hamcrest-all</a></td>
<td>1.3</td>
<td>jar</td>
<td><a href="http://www.opensource.org/licenses/bsd-license.php">New BSD License</a></td></tr>
<tr>
<td align="left">org.junit.vintage</td>
<td><a href="https://junit.org/junit5/">junit-vintage-engine</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.mockito</td>
<td><a href="https://github.com/mockito/mockito">mockito-core</a></td>
<td>4.11.0</td>
<td>jar</td>
<td><a href="https://github.com/mockito/mockito/blob/main/LICENSE">The MIT License</a></td></tr></table></section></section><a name="Project_Transitive_Dependencies"></a><section>
<h2><a name="Project_Transitive_Dependencies"></a>Project Transitive Dependencies</h2>
<p>The following is a list of transitive dependencies for this project. Transitive dependencies are the dependencies of the project dependencies.</p><a name="Project_Transitive_Dependencies_test"></a><section>
<h3><a name="test"></a>test</h3>
<p>The following is a list of test dependencies for this project. These dependencies are only required to compile and run unit tests for the application:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>Licenses</th></tr>
<tr>
<td align="left">junit</td>
<td><a href="http://junit.org">junit</a></td>
<td>4.13.2</td>
<td>jar</td>
<td><a href="http://www.eclipse.org/legal/epl-v10.html">Eclipse Public License 1.0</a></td></tr>
<tr>
<td align="left">net.bytebuddy</td>
<td><a href="https://bytebuddy.net/byte-buddy">byte-buddy</a></td>
<td>1.12.19</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td align="left">net.bytebuddy</td>
<td><a href="https://bytebuddy.net/byte-buddy-agent">byte-buddy-agent</a></td>
<td>1.12.19</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td align="left">org.apiguardian</td>
<td><a href="https://github.com/apiguardian-team/apiguardian">apiguardian-api</a></td>
<td>1.1.2</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr>
<tr>
<td align="left">org.hamcrest</td>
<td><a href="https://github.com/hamcrest/JavaHamcrest/hamcrest-core">hamcrest-core</a></td>
<td>1.3</td>
<td>jar</td>
<td><a href="http://www.opensource.org/licenses/bsd-license.php">New BSD License</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-commons</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-engine</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.objenesis</td>
<td><a href="http://objenesis.org/objenesis">objenesis</a></td>
<td>3.3</td>
<td>jar</td>
<td><a href="http://www.apache.org/licenses/LICENSE-2.0.txt">Apache License, Version 2.0</a></td></tr>
<tr>
<td align="left">org.opentest4j</td>
<td><a href="https://github.com/ota4j-team/opentest4j">opentest4j</a></td>
<td>1.3.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">The Apache License, Version 2.0</a></td></tr></table></section></section><a name="Project_Dependency_Graph"></a><section>
<h2><a name="Project_Dependency_Graph"></a>Project Dependency Graph</h2><a name="Dependency_Tree"></a><section>
<h3><a name="Dependency_Tree"></a>Dependency Tree</h3>
</section></section><a name="Licenses"></a><section>
<h2><a name="Licenses"></a>Licenses</h2>
<p><b>The Apache License, Version 2.0: </b>org.apiguardian:apiguardian-api, org.opentest4j:opentest4j</p>
<p><b>Eclipse Public License 1.0: </b>JUnit</p>
<p><b>The MIT License: </b>mockito-core</p>
<p><b>Apache-2.0: </b>Apache Commons DbUtils</p>
<p><b>Eclipse Public License v2.0: </b>JUnit Platform Commons, JUnit Platform Engine API, JUnit Vintage Engine</p>
<p><b>Apache License, Version 2.0: </b>Byte Buddy (without dependencies), Byte Buddy agent, Objenesis</p>
<p><b>New BSD License: </b>Hamcrest All, Hamcrest Core</p></section><a name="Dependency_File_Details"></a><section>
<h2><a name="Dependency_File_Details"></a>Dependency File Details</h2>
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
<td align="left">junit-4.13.2.jar</td>
<td align="right">384.6 kB</td>
<td align="right">389</td>
<td align="right">350</td>
<td align="right">32</td>
<td align="center">1.5</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">byte-buddy-1.12.19.jar</td>
<td align="right">4 MB</td>
<td align="right">2742</td>
<td align="right">2688</td>
<td align="right">39</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">byte-buddy-agent-1.12.19.jar</td>
<td align="right">256.4 kB</td>
<td align="right">90</td>
<td align="right">70</td>
<td align="right">3</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">apiguardian-api-1.1.2.jar</td>
<td align="right">6.8 kB</td>
<td align="right">9</td>
<td align="right">3</td>
<td align="right">2</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">hamcrest-all-1.3.jar</td>
<td align="right">306.6 kB</td>
<td align="right">249</td>
<td align="right">204</td>
<td align="right">23</td>
<td align="center">1.5</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">hamcrest-core-1.3.jar</td>
<td align="right">45 kB</td>
<td align="right">52</td>
<td align="right">45</td>
<td align="right">3</td>
<td align="center">1.5</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">junit-platform-commons-1.10.0.jar</td>
<td align="right">106.2 kB</td>
<td align="right">64</td>
<td align="right">44</td>
<td align="right">7</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">junit-platform-engine-1.10.0.jar</td>
<td align="right">204.8 kB</td>
<td align="right">153</td>
<td align="right">136</td>
<td align="right">10</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">junit-vintage-engine-5.10.0.jar</td>
<td align="right">66.9 kB</td>
<td align="right">49</td>
<td align="right">35</td>
<td align="right">6</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">mockito-core-4.11.0.jar</td>
<td align="right">684.9 kB</td>
<td align="right">651</td>
<td align="right">579</td>
<td align="right">64</td>
<td align="center">1.8</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">objenesis-3.3.jar</td>
<td align="right">49.4 kB</td>
<td align="right">59</td>
<td align="right">43</td>
<td align="right">10</td>
<td align="center">1.8</td>
<td align="center">Yes</td></tr>
<tr>
<td align="left">opentest4j-1.3.0.jar</td>
<td align="right">14.3 kB</td>
<td align="right">15</td>
<td align="right">9</td>
<td align="right">2</td>
<td align="center">9</td>
<td align="center">Yes</td></tr>
<tr>
<th>Total</th>
<th>Size</th>
<th>Entries</th>
<th>Classes</th>
<th>Packages</th>
<th>Java Version</th>
<th>Debug Information</th></tr>
<tr>
<td align="right">12</td>
<td align="right">6.1 MB</td>
<td align="right">4522</td>
<td align="right">4206</td>
<td align="right">201</td>
<td align="center">9</td>
<td align="right">12</td></tr>
<tr>
<td align="right">test: 12</td>
<td align="right">test: 6.1 MB</td>
<td align="right">test: 4522</td>
<td align="right">test: 4206</td>
<td align="right">test: 201</td>
<td align="center">9</td>
<td align="right">test: 12</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/issue-tracking.html -->

<!-- page_index: 6 -->

# DbUtils – Apache Commons DbUtils Issue tracking

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Apache_Commons_DbUtils_Issue_tracking"></a>Apache Commons DbUtils Issue tracking</h2>
<p>
      Apache Commons DbUtils uses <a href="https://issues.apache.org/jira/">ASF JIRA</a> for tracking issues.
      See the <a href="https://issues.apache.org/jira/browse/DBUTILS">Apache Commons DbUtils JIRA project page</a>.
      </p>
<p>
      To use JIRA you may need to <a href="https://issues.apache.org/jira/secure/Signup!default.jspa">create an account</a>
      (if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
      created and you can use the <a href="https://issues.apache.org/jira/secure/ForgotPassword!default.jspa">Forgot Password</a>
      page to get a new password).
      </p>
<p>
      If you would like to report a bug, or raise an enhancement request with
      Apache Commons DbUtils please do the following:
      </p>
<p>
      Please also remember these points:
      </p>
<ul>
<li>the more information you provide, the better we can help you</li>
<li>test cases are vital, particularly for any proposed enhancements</li>
<li>the developers of Apache Commons DbUtils are all unpaid volunteers</li>
</ul>
<p>
      For more information on creating patches see the
      <a href="https://www.apache.org/dev/contributors.html">Apache Contributors Guide</a>.
      </p>
<p>
      You may also find these links useful:
      </p>
<ul>
<li><a href="https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&amp;pid=12310470&amp;sorter/field=issuekey&amp;sorter/order=DESC&amp;status=1&amp;status=3&amp;status=4">All Open Apache Commons DbUtils bugs</a></li>
<li><a href="https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&amp;pid=12310470&amp;sorter/field=issuekey&amp;sorter/order=DESC&amp;status=5&amp;status=6">All Resolved Apache Commons DbUtils bugs</a></li>
<li><a href="https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&amp;pid=12310470&amp;sorter/field=issuekey&amp;sorter/order=DESC">All Apache Commons DbUtils bugs</a></li>
</ul>
</section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/scm.html -->

<!-- page_index: 7 -->

# DbUtils – Source Code Management

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Overview"></a>Overview</h2><a name="Overview"></a>
<p>This project uses <a href="https://git-scm.com/">Git</a> to manage its source code. Instructions on Git use can be found at <a href="https://git-scm.com/documentation">https://git-scm.com/documentation</a>.</p></section><section>
<h2><a name="Web_Browser_Access"></a>Web Browser Access</h2><a name="Web_Browser_Access"></a>
<p>The following is a link to a browsable version of the source repository:</p>
<div>
<pre><a href="https://gitbox.apache.org/repos/asf?p=commons-dbutils.git">https://gitbox.apache.org/repos/asf?p=commons-dbutils.git</a></pre></div></section><section>
<h2><a name="Anonymous_Access"></a>Anonymous Access</h2><a name="Anonymous_Access"></a>
<p>The source can be checked out anonymously from Git with this command (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>):</p>
<div>
<pre>$ git clone git://git.apache.org/commons-dbutils.git</pre></div></section><section>
<h2><a name="Developer_Access"></a>Developer Access</h2><a name="Developer_Access"></a>
<p>Only project developers can access the Git tree via this method (See <a href="https://git-scm.com/docs/git-clone">https://git-scm.com/docs/git-clone</a>).</p>
<div>
<pre>$ git clone https://gitbox.apache.org/repos/asf/commons-dbutils.git</pre></div></section><section>
<h2><a name="Access_from_Behind_a_Firewall"></a>Access from Behind a Firewall</h2><a name="Access_from_Behind_a_Firewall"></a>
<p>Refer to the documentation of the SCM used for more information about access behind a firewall.</p></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/building.html -->

<!-- page_index: 8 -->

## Overview

Commons DBUtils uses [Maven](http://maven.apache.org) or
[Ant](http://ant.apache.org) as a build system.

## Maven Goals

To build a jar file, change into DBUtils's root directory and run
**`maven package`**.
The result will be in the "target" subdirectory.

To build the Javadocs, run **`maven javadoc:javadoc`**.
The result will be in "target/docs/apidocs".

To build the full website, run **`maven site`**.
The result will be in "target/docs".

Further details can be found in the
[commons build instructions](https://commons.apache.org/building.html).

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/project-info.html -->

<!-- page_index: 9 -->

# DbUtils – Project Information

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Project_Information"></a>Project Information</h2>
<p>This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by <a href="http://maven.apache.org">Maven</a> on behalf of the project.</p><section>
<h3><a name="Overview"></a>Overview</h3>
<table>
<tr>
<th>Document</th>
<th>Description</th></tr>
<tr>
<td align="left"><a href="#index">About</a></td>
<td align="left">The Apache Commons DbUtils package is a set of Java utility classes for easing JDBC development.</td></tr>
<tr>
<td align="left"><a href="#summary">Summary</a></td>
<td align="left">This document lists other related information of this project</td></tr>
<tr>
<td align="left"><a href="#team">Team</a></td>
<td align="left">This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another.</td></tr>
<tr>
<td align="left"><a href="#scm">Source Code Management</a></td>
<td align="left">This document lists ways to access the online source repository.</td></tr>
<tr>
<td align="left"><a href="#issue-management">Issue Management</a></td>
<td align="left">This document provides information on the issue management system used in this project.</td></tr>
<tr>
<td align="left"><a href="https://commons.apache.org/proper/commons-dbutils/mailing-lists.html">Mailing Lists</a></td>
<td align="left">This document provides subscription and archive information for this project's mailing lists.</td></tr>
<tr>
<td align="left"><a href="#dependency-info">Dependency Information</a></td>
<td align="left">This document describes how to include this project as a dependency using various dependency management tools.</td></tr>
<tr>
<td align="left"><a href="#dependency-management">Dependency Management</a></td>
<td align="left">This document lists the dependencies that are defined through dependencyManagement.</td></tr>
<tr>
<td align="left"><a href="#dependencies">Dependencies</a></td>
<td align="left">This document lists the project's dependencies and provides information on each dependency.</td></tr>
<tr>
<td align="left"><a href="#dependency-convergence">Dependency Convergence</a></td>
<td align="left">This document presents the convergence of dependency versions across the entire project, and its sub modules.</td></tr>
<tr>
<td align="left"><a href="#ci-management">CI Management</a></td>
<td align="left">This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis.</td></tr>
<tr>
<td align="left"><a href="#distribution-management">Distribution Management</a></td>
<td align="left">This document provides informations on the distribution management of this project.</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/summary.html -->

<!-- page_index: 10 -->

# DbUtils – Project Summary

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Project_Summary"></a>Project Summary</h2><a name="Project_Summary"></a><section>
<h3><a name="Project_Information"></a>Project Information</h3><a name="Project_Information"></a>
<table>
<tr>
<th>Field</th>
<th>Value</th></tr>
<tr>
<td align="left">Name</td>
<td>Apache Commons DbUtils</td></tr>
<tr>
<td align="left">Description</td>
<td>The Apache Commons DbUtils package is a set of Java utility classes for easing JDBC development.</td></tr>
<tr>
<td align="left">Homepage</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/">https://commons.apache.org/proper/commons-dbutils/</a></td></tr></table></section><section>
<h3><a name="Project_Organization"></a>Project Organization</h3><a name="Project_Organization"></a>
<table>
<tr>
<th>Field</th>
<th>Value</th></tr>
<tr>
<td align="left">Name</td>
<td>The Apache Software Foundation</td></tr>
<tr>
<td align="left">URL</td>
<td><a href="https://www.apache.org/">https://www.apache.org/</a></td></tr></table></section><section>
<h3><a name="Build_Information"></a>Build Information</h3><a name="Build_Information"></a>
<table>
<tr>
<th>Field</th>
<th>Value</th></tr>
<tr>
<td align="left">GroupId</td>
<td>commons-dbutils</td></tr>
<tr>
<td align="left">ArtifactId</td>
<td>commons-dbutils</td></tr>
<tr>
<td align="left">Version</td>
<td>1.8.1</td></tr>
<tr>
<td align="left">Type</td>
<td>jar</td></tr>
<tr>
<td align="left">Java Version</td>
<td>1.8</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/team.html -->

<!-- page_index: 11 -->

# DbUtils – Project Team

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Project_Team"></a>Project Team</h2><a name="Project_Team"></a>
<p>A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.</p>
<p>The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.</p><section>
<h3><a name="Members"></a>Members</h3><a name="Members"></a>
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
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/2bcb82403b87c2c4cba0fe6a5edb4c20?d=mm&amp;s=60"/></figure></td>
<td><a name="baliuka"></a>baliuka</td>
<td>Juozas Baliuka</td>
<td><a href="mailto:baliuka@apache.org">baliuka@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/e5fb9b8bba7ccd5fc0c8b86ac83ce4b5?d=mm&amp;s=60"/></figure></td>
<td><a name="scaswell"></a>scaswell</td>
<td>Steven Caswell</td>
<td><a href="mailto:steven@caswell.name">steven@caswell.name</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/0ded147122e1c318a63340568904762b?d=mm&amp;s=60"/></figure></td>
<td><a name="dfabulich"></a>dfabulich</td>
<td>Dan Fabulich</td>
<td><a href="mailto:dan@fabulich.com">dan@fabulich.com</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/3797c8c3332e7ccd80273f7eac7c2949?d=mm&amp;s=60"/></figure></td>
<td><a name="dgraham"></a>dgraham</td>
<td>David Graham</td>
<td><a href="mailto:dgraham@apache.org">dgraham@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/248341e80da66f10c0d6af27f40c8d63?d=mm&amp;s=60"/></figure></td>
<td><a name="yoavs"></a>yoavs</td>
<td>Yoav Shapira</td>
<td><a href="mailto:yoavs@apache.org">yoavs@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/910b15b19b44768cbeefc884cd2d6460?d=mm&amp;s=60"/></figure></td>
<td><a name="wspeirs"></a>wspeirs</td>
<td>William Speirs</td>
<td><a href="mailto:wspeirs@apache.org">wspeirs@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/a23637cb700caf1c78d93cd5212418c9?d=mm&amp;s=60"/></figure></td>
<td><a name="simonetripodi"></a>simonetripodi</td>
<td>Simone Tripodi</td>
<td><a href="mailto:simonetripodi at apache dot org">simonetripodi at apache dot org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/4156866f23b66d5ca7df5cdc86cb9a0e?d=mm&amp;s=60"/></figure></td>
<td><a name="bayard"></a>bayard</td>
<td>Henri Yandell</td>
<td><a href="mailto:bayard@apache.org">bayard@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/cbfb61ee7f8641b2b6eaf22fed163b1e?d=mm&amp;s=60"/></figure></td>
<td><a name="britter"></a>britter</td>
<td>Benedikt Ritter</td>
<td><a href="mailto:britter@apache.org">britter@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/487c829cb2071c62b09770a987986ce2?d=mm&amp;s=60"/></figure></td>
<td><a name="thecarlhall"></a>thecarlhall</td>
<td>Carl Hall</td>
<td><a href="mailto:thecarlhall@apache.org">thecarlhall@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://people.apache.org/~ggregory/img/garydgregory80.png"/></figure></td>
<td><a name="ggregory"></a>ggregory</td>
<td>Gary Gregory</td>
<td><a href="mailto:ggregory at apache.org">ggregory at apache.org</a></td>
<td><a href="https://www.garygregory.com">https://www.garygregory.com</a></td>
<td>The Apache Software Foundation</td>
<td><a href="https://www.apache.org/">https://www.apache.org/</a></td>
<td>PMC Member</td>
<td>America/New_York</td></tr></table></section><section>
<h3><a name="Contributors"></a>Contributors</h3><a name="Contributors"></a>
<p>The following additional people have contributed to this project through the way of suggestions, patches or documentation.</p>
<table>
<tr>
<th>Image</th>
<th>Name</th>
<th>Email</th>
<th>Roles</th></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&amp;f=y&amp;s=60"/></figure></td>
<td>Péter Bagyinszki</td>
<td>-</td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&amp;f=y&amp;s=60"/></figure></td>
<td>Alan Canon</td>
<td>-</td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/ccad3c663dffd81a6a3e54b246966629?d=mm&amp;s=60"/></figure></td>
<td>Stefan Fleiter</td>
<td><a href="mailto:stefan.fleiter@web.de">stefan.fleiter@web.de</a></td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&amp;f=y&amp;s=60"/></figure></td>
<td>Adkins Kendall</td>
<td>-</td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/428b2f330c1eb3274deeff27864da9bb?d=mm&amp;s=60"/></figure></td>
<td>Markus Khouri</td>
<td><a href="mailto:mkhouri.list@gmail.com">mkhouri.list@gmail.com</a></td>
<td>Documentation</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/5e48bb1bdf7dd9b5bd909ce270a21206?d=mm&amp;s=60"/></figure></td>
<td>Uli Kleeberger</td>
<td><a href="mailto:ukleeberger@web.de">ukleeberger@web.de</a></td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/c2771fe987234ec0a6c5bc18809adb75?d=mm&amp;s=60"/></figure></td>
<td>Piotr Lakomy</td>
<td><a href="mailto:piotrl@cft-inc.net">piotrl@cft-inc.net</a></td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&amp;f=y&amp;s=60"/></figure></td>
<td>Corby Page</td>
<td>-</td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/bce1d1b7c3ec7b577dcb42e254899e6b?d=mm&amp;s=60"/></figure></td>
<td>Michael Schuerig</td>
<td><a href="mailto:michael@schuerig.de">michael@schuerig.de</a></td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/e9b6b3a115dcb64e45711f40de87116c?d=mm&amp;s=60"/></figure></td>
<td>Norris Shelton</td>
<td><a href="mailto:norrisshelton@yahoo.com">norrisshelton@yahoo.com</a></td>
<td>Java Developer</td></tr>
<tr>
<td align="left"><figure><img alt="" src="https://www.gravatar.com/avatar/d3c1de0c1f733d6aa98d77f508be3ac5?d=mm&amp;s=60"/></figure></td>
<td>Stevo Slavic</td>
<td><a href="mailto:sslavic at gmail dot com">sslavic at gmail dot com</a></td>
<td>-</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="issue-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/issue-management.html -->

<!-- page_index: 12 -->

# DbUtils – Issue Management

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Overview"></a>Overview</h2><a name="Overview"></a>
<p>This project uses <a href="http://www.atlassian.com/software/jira">JIRA</a>.</p></section><section>
<h2><a name="Issue_Management"></a>Issue Management</h2><a name="Issue_Management"></a>
<p>Issues, bugs, and feature requests should be submitted to the following issue management system for this project.</p>
<div>
<pre><a href="https://issues.apache.org/jira/browse/DBUTILS">https://issues.apache.org/jira/browse/DBUTILS</a></pre></div></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/dependency-info.html -->

<!-- page_index: 13 -->

# DbUtils – Dependency Information

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Dependency_Information"></a>Dependency Information</h2><a name="Dependency_Information"></a><section>
<h3><a name="Apache_Maven"></a>Apache Maven</h3><a name="Apache_Maven"></a>
<div>
<pre>&lt;dependency&gt;
  &lt;groupId&gt;commons-dbutils&lt;/groupId&gt;
  &lt;artifactId&gt;commons-dbutils&lt;/artifactId&gt;
  &lt;version&gt;1.8.1&lt;/version&gt;
&lt;/dependency&gt;</pre></div></section><section>
<h3><a name="Apache_Ivy"></a>Apache Ivy</h3><a name="Apache_Ivy"></a>
<div>
<pre>&lt;dependency org="commons-dbutils" name="commons-dbutils" rev="1.8.1"&gt;
  &lt;artifact name="commons-dbutils" type="jar" /&gt;
&lt;/dependency&gt;</pre></div></section><section>
<h3><a name="Groovy_Grape"></a>Groovy Grape</h3><a name="Groovy_Grape"></a>
<div>
<pre>@Grapes(
@Grab(group='commons-dbutils', module='commons-dbutils', version='1.8.1')
)</pre></div></section><section>
<h3><a name="Gradle.2FGrails"></a>Gradle/Grails</h3><a name="Gradle.2FGrails"></a>
<div>
<pre>implementation 'commons-dbutils:commons-dbutils:1.8.1'</pre></div></section><section>
<h3><a name="Scala_SBT"></a>Scala SBT</h3><a name="Scala_SBT"></a>
<div>
<pre>libraryDependencies += "commons-dbutils" % "commons-dbutils" % "1.8.1"</pre></div></section><section>
<h3><a name="Leiningen"></a>Leiningen</h3><a name="Leiningen"></a>
<div>
<pre>[commons-dbutils "1.8.1"]</pre></div></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/dependency-management.html -->

<!-- page_index: 14 -->

# DbUtils – Project Dependency Management

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Project_Dependency_Management"></a>Project Dependency Management</h2><a name="Project_Dependency_Management"></a><section>
<h3><a name="compile"></a>compile</h3><a name="compile"></a>
<p>The following is a list of compile dependencies in the DependencyManagement of this project. These dependencies can be included in the submodules to compile and run the submodule:</p>
<table>
<tr>
<th>GroupId</th>
<th>ArtifactId</th>
<th>Version</th>
<th>Type</th>
<th>License</th></tr>
<tr>
<td align="left">org.apache.maven.plugin-tools</td>
<td><a href="https://maven.apache.org/plugin-tools/maven-plugin-annotations">maven-plugin-annotations</a></td>
<td>3.9.0</td>
<td>jar</td>
<td><a href="https://www.apache.org/licenses/LICENSE-2.0.txt">Apache-2.0</a></td></tr>
<tr>
<td align="left">org.junit.jupiter</td>
<td><a href="https://junit.org/junit5/">junit-jupiter</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.jupiter</td>
<td><a href="https://junit.org/junit5/">junit-jupiter-api</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.jupiter</td>
<td><a href="https://junit.org/junit5/">junit-jupiter-engine</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.jupiter</td>
<td><a href="https://junit.org/junit5/">junit-jupiter-migrationsupport</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.jupiter</td>
<td><a href="https://junit.org/junit5/">junit-jupiter-params</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-commons</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-console</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-engine</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-jfr</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-launcher</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-reporting</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-runner</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-suite</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-suite-api</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-suite-commons</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-suite-engine</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.platform</td>
<td><a href="https://junit.org/junit5/">junit-platform-testkit</a></td>
<td>1.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr>
<tr>
<td align="left">org.junit.vintage</td>
<td><a href="https://junit.org/junit5/">junit-vintage-engine</a></td>
<td>5.10.0</td>
<td>jar</td>
<td><a href="https://www.eclipse.org/legal/epl-v20.html">Eclipse Public License v2.0</a></td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="dependency-convergence"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/dependency-convergence.html -->

<!-- page_index: 15 -->

## Dependency Convergence

**Statistics:**

| Number of dependencies (NOD): | 12 |
| Number of unique artifacts (NOA): | 12 |
| Number of version-conflicting artifacts (NOC): | 0 |
| Number of SNAPSHOT artifacts (NOS): | 0 |
| Convergence (NOD/NOA): | [Success] **100 %** |
| Ready for release (100% convergence and no SNAPSHOTS): | [Success] **Success** |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/ci-management.html -->

<!-- page_index: 16 -->

# DbUtils – CI Management

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Overview"></a>Overview</h2><a name="Overview"></a>
<p>This project uses <a href="https://github.com/features/actions/">GitHub Actions</a>.</p></section><section>
<h2><a name="Access"></a>Access</h2><a name="Access"></a>
<p>The following is a link to the continuous integration system used by the project:</p>
<div>
<pre><a href="https://github.com/apache/commons-parent/actions">https://github.com/apache/commons-parent/actions</a></pre></div></section><section>
<h2><a name="Notifiers"></a>Notifiers</h2><a name="Notifiers"></a>
<p>No notifiers are defined. Please check back at a later date.</p></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="distribution-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/distribution-management.html -->

<!-- page_index: 17 -->

# DbUtils – Project Distribution Management

|  |  |
| --- | --- |
|  | Overview The following is the distribution management information used by this project.  Repository - apache.releases.https<https://repository.apache.org/service/local/staging/deploy/maven2>  Snapshot Repository - apache.snapshots.https<https://repository.apache.org/content/repositories/snapshots>  Site - apache.website scp://people.apache.org/www/commons.apache.org/dbutils |

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/project-reports.html -->

<!-- page_index: 18 -->

# DbUtils – Generated Reports

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Generated_Reports"></a>Generated Reports</h2>
<p>This document provides an overview of the various reports that are automatically generated by <a href="http://maven.apache.org">Maven</a> . Each report is briefly described below.</p><section>
<h3><a name="Overview"></a>Overview</h3>
<table>
<tr>
<th>Document</th>
<th>Description</th></tr>
<tr>
<td align="left"><a href="#changes-report">Changes</a></td>
<td align="left">Changes report on releases of this project.</td></tr>
<tr>
<td align="left"><a href="#jira-report">JIRA Report</a></td>
<td align="left">Report on Issues from the JIRA Issue Tracking System.</td></tr>
<tr>
<td align="left"><a href="https://commons.apache.org/proper/commons-dbutils/apidocs/index.html">Javadoc</a></td>
<td align="left">Javadoc API documentation.</td></tr>
<tr>
<td align="left"><a href="https://commons.apache.org/proper/commons-dbutils/xref/index.html">Source Xref</a></td>
<td align="left">HTML based, cross-reference version of Java source code.</td></tr>
<tr>
<td align="left"><a href="https://commons.apache.org/proper/commons-dbutils/xref-test/index.html">Test Source Xref</a></td>
<td align="left">HTML based, cross-reference version of Java test source code.</td></tr>
<tr>
<td align="left"><a href="#surefire-report">Surefire</a></td>
<td align="left">Report on the test results of the project.</td></tr>
<tr>
<td align="left"><a href="#rat-report">Rat Report</a></td>
<td align="left">Report on compliance to license related source code policies</td></tr>
<tr>
<td align="left"><a href="https://commons.apache.org/proper/commons-dbutils/jacoco/index.html">JaCoCo</a></td>
<td align="left">JaCoCo Coverage Report.</td></tr>
<tr>
<td align="left"><a href="#japicmp">japicmp</a></td>
<td align="left">Comparing source compatibility of commons-dbutils-1.8.1.jar against commons-dbutils-1.8.0.jar</td></tr>
<tr>
<td align="left"><a href="#checkstyle">Checkstyle</a></td>
<td align="left">Report on coding style conventions.</td></tr>
<tr>
<td align="left"><a href="#spotbugs">SpotBugs</a></td>
<td align="left">Generates a source code report with the SpotBugs Library.</td></tr>
<tr>
<td align="left"><a href="#cpd">CPD</a></td>
<td align="left">Duplicate code detection.</td></tr>
<tr>
<td align="left"><a href="#pmd">PMD</a></td>
<td align="left">Verification of coding rules.</td></tr></table></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jira-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/jira-report.html -->

<!-- page_index: 19 -->

# DbUtils – JIRA Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="JIRA_Report"></a>JIRA Report</h2>
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
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-122">DBUTILS-122</a></td>
<td></td>
<td>getParameterMetaData  Exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-81">DBUTILS-81</a></td>
<td></td>
<td>DbUtils.loadDriver() uses Class.forName()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-80">DBUTILS-80</a></td>
<td></td>
<td>DbUtils.loadDriver catches Throwable</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-71">DBUTILS-71</a></td>
<td></td>
<td>insert error</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-49">DBUTILS-49</a></td>
<td></td>
<td>QueryRunner - fillStatement method does not work for PostgreSQL database drivers</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-44">DBUTILS-44</a></td>
<td></td>
<td>QueryRunner#fillStatement setNull all database fix proposal</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-41">DBUTILS-41</a></td>
<td></td>
<td>Inserting/updating null in a timestamp field with PostgreSQL 8.x</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-39">DBUTILS-39</a></td>
<td></td>
<td>setNull with Postgres in QueryRunner</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-149">DBUTILS-149</a></td>
<td></td>
<td>Resolve bugs when upgrading to Spotbugs 4.7.3</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-14">DBUTILS-14</a></td>
<td></td>
<td>[dbutils] fillPreparedStatement</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-68">DBUTILS-68</a></td>
<td></td>
<td>Examples on main page are not generic and produce unchecked warning</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td></td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-35">DBUTILS-35</a></td>
<td></td>
<td>Can somebody upload commons-dbutils 1.1 sources jar to the apache repository</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.8.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-151">DBUTILS-151</a></td>
<td></td>
<td>Module org.apache.commons.dbutils does not declare `uses`</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-143">DBUTILS-143</a></td>
<td></td>
<td>Don't close connection if provided</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-138">DBUTILS-138</a></td>
<td></td>
<td>org.apache.commons.dbutils.QueryRunner.query(Connection, boolean, String, ResultSetHandler&lt;T&gt;, Object...) Exception in closing statement leave connections open</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-137">DBUTILS-137</a></td>
<td></td>
<td>Inefficient allocation of Maps in org.apache.commons.dbutils.BasicRowProcessor.toMap(ResultSet)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-136">DBUTILS-136</a></td>
<td></td>
<td>CaseInsensitiveHashMap cannot be accessed by subclasses of BasicRowProcessor; add org.apache.commons.dbutils.BasicRowProcessor.createCaseInsensitiveHashMap(int)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-135">DBUTILS-135</a></td>
<td></td>
<td>BeanProcessor is not thread safe since [DBUTILS-124]</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-139">DBUTILS-139</a></td>
<td></td>
<td>Update Java requirement from version 6 to 7.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.8.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-131">DBUTILS-131</a></td>
<td></td>
<td>Speedup query calls without parameters</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-144">DBUTILS-144</a></td>
<td></td>
<td>RowProcessor.asMap is invalid for multiple computed columns with no aliases</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-109">DBUTILS-109</a></td>
<td></td>
<td>AbstractExecutor.currentPosition should be an int</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-148">DBUTILS-148</a></td>
<td></td>
<td>Update deprecated Mockito.initMocks</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-95">DBUTILS-95</a></td>
<td></td>
<td>Remove all of the deprecated code</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-92">DBUTILS-92</a></td>
<td></td>
<td>Align maven groupId with rest of the apache commons projects</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-112">DBUTILS-112</a></td>
<td></td>
<td>Provide DbUtils.rollbackQuietly() method</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-119">DBUTILS-119</a></td>
<td></td>
<td>Correct errors in BeanMapHandler JavaDoc</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-121">DBUTILS-121</a></td>
<td></td>
<td>Allow influencing the setter method used</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-115">DBUTILS-115</a></td>
<td></td>
<td>Enhance BeanProcessor to support Joda DateTime</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-82">DBUTILS-82</a></td>
<td></td>
<td>Change BeanListHandler to be able to handle to list of the bean's super class or interface</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-70">DBUTILS-70</a></td>
<td></td>
<td>add setQueryTimeout support to QueryRunner</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-124">DBUTILS-124</a></td>
<td></td>
<td>Introduce SPI to add more column, property handlers</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-89">DBUTILS-89</a></td>
<td></td>
<td>Add method in BeanProcessor to populate an existing bean </td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.7</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-50">DBUTILS-50</a></td>
<td></td>
<td>Support CallableStatement "out" parameters</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-118">DBUTILS-118</a></td>
<td></td>
<td>BeanProcessor not returning nanoseconds</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-117">DBUTILS-117</a></td>
<td></td>
<td>Error handling possible getParameterMetaData() results</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-114">DBUTILS-114</a></td>
<td></td>
<td>Order of columns not retained in BasicRowProcessor with HashMap</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-96">DBUTILS-96</a></td>
<td></td>
<td>DbUtils#loadDriver(ClassLoader,String) makes DriverManager throwing "No suitable driver found for jdbc" if ClassLoader is not the System's one</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-113">DBUTILS-113</a></td>
<td></td>
<td>Add support for conversion of ResultSet strings to enums in the BeanProcessor</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-110">DBUTILS-110</a></td>
<td></td>
<td>ArrayHandler should return an empty array when handle has no rows</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-108">DBUTILS-108</a></td>
<td></td>
<td>Create functionality to return auto-generated keys in batches of SQL inserts</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-107">DBUTILS-107</a></td>
<td></td>
<td>Patch QueryLoader to also load from XML properties files</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-106">DBUTILS-106</a></td>
<td></td>
<td>DBUtils can't build using JDK 1.7 - DriverProxy needs to implement getParentLogger()</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-103">DBUTILS-103</a></td>
<td></td>
<td>fix Dependencies documentation to reference correct Java version</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-100">DBUTILS-100</a></td>
<td></td>
<td>columnLabel and  columnname</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6, 2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-85">DBUTILS-85</a></td>
<td></td>
<td>In BeanProcessor#isCompatibleType, can Integer.class.isInstance(value) be replaced by value instanceof Integer (etc)?</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-97">DBUTILS-97</a></td>
<td></td>
<td>Add an Abstract ResultSetHandler implementation in order to reduce redundant 'resultSet' variable invocation</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.6</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-98">DBUTILS-98</a></td>
<td></td>
<td>Add missing JavaDoc to QueryRunner#insert</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-93">DBUTILS-93</a></td>
<td></td>
<td>Source assembly artifact fails to build a site because of missing pmd-ruleset.xml</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-73">DBUTILS-73</a></td>
<td></td>
<td>.BasicRowProcessor.CaseInsensitiveHashMap uses default Locale for toLowerCase</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-91">DBUTILS-91</a></td>
<td></td>
<td>Enhance BasicRowProcessor to have row mapping easier to configure</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-84">DBUTILS-84</a></td>
<td></td>
<td>BeanProcessor method processColumn should take SQLXML in consideration</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-66">DBUTILS-66</a></td>
<td></td>
<td>ScalarHandler, ColumnHandler and KeyedHandler are missing generics</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-76">DBUTILS-76</a></td>
<td></td>
<td>New handler StringColumnListHandler</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-67">DBUTILS-67</a></td>
<td></td>
<td>Add a BeanMapHandler</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-88">DBUTILS-88</a></td>
<td></td>
<td>Make AsyncQueryRunner be a decorator around a QueryRunner</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-94">DBUTILS-94</a></td>
<td></td>
<td>Provide test coverage for org.apache.commons.dbutils.DbUtils</td>
<td>Test</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.4</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-79">DBUTILS-79</a></td>
<td></td>
<td>fillStatement doesn't complain when there are too few parameters</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.4</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-65">DBUTILS-65</a></td>
<td></td>
<td>Duplicate code introduced during Java 1.5 branch merge</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.4</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-75">DBUTILS-75</a></td>
<td></td>
<td>efficient usage from findbugs</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.4</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-78">DBUTILS-78</a></td>
<td></td>
<td>Add asynchronous batch, query, and update calls</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-63">DBUTILS-63</a></td>
<td></td>
<td>SqlNullCheckedResultSet exposes internal representation</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-61">DBUTILS-61</a></td>
<td></td>
<td>Backwards binary compatibility broken in KeyedHandler</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-57">DBUTILS-57</a></td>
<td></td>
<td>BeanProcessor not able to map an alias column from a HSQLDB query to the any bean properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-56">DBUTILS-56</a></td>
<td></td>
<td>QueryRunner exception using Oracle: Too many parameters: expected 0, was given 1 Query: ...</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-60">DBUTILS-60</a></td>
<td></td>
<td>Enhance message in QueryRunner#rethrow for Batch</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-58">DBUTILS-58</a></td>
<td></td>
<td>QueryRunner: Allow to completly disable use of PreparedStatement#getParameterMetaData</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-48">DBUTILS-48</a></td>
<td></td>
<td>Java 1.5 generics and varargs</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-62">DBUTILS-62</a></td>
<td></td>
<td>Fix example page according to Java 5 version</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-52">DBUTILS-52</a></td>
<td></td>
<td>QueryRunner is not thread-safe</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-40">DBUTILS-40</a></td>
<td></td>
<td>NullPointerException occured at rethrow method</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-36">DBUTILS-36</a></td>
<td></td>
<td>Add serialVersionUID to BasicRowProcessor.CaseInsensitiveHashMap</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-51">DBUTILS-51</a></td>
<td></td>
<td>Make classes immutable where possible to improve thread-safety</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-42">DBUTILS-42</a></td>
<td></td>
<td>Object with Long or Decimal got initial zero value while database field is null</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-38">DBUTILS-38</a></td>
<td></td>
<td>example documentation page, update query</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-37">DBUTILS-37</a></td>
<td></td>
<td>BeanListHandler#handle(ResultSet) is not optimal</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-34">DBUTILS-34</a></td>
<td></td>
<td>BasicRowProcessor loses any information on database field case</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-33">DBUTILS-33</a></td>
<td></td>
<td>Consdier making GenericListHandler public</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-31">DBUTILS-31</a></td>
<td></td>
<td>fillStatement setNull bug with the Derby JDBC driver</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.2</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-29">DBUTILS-29</a></td>
<td></td>
<td>[dbutils] Support bean property to SQL IN parameter mapping</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-32">DBUTILS-32</a></td>
<td></td>
<td>Tests fail to build under 1.6, and warning while compiling source</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-9">DBUTILS-9</a></td>
<td></td>
<td>[dbutils] MockResultSet needs to handle equals and hashCode</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-7">DBUTILS-7</a></td>
<td></td>
<td>[dbutils] MockResultSet: Throw UnsupportedOperationException for not implemented methods</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-5">DBUTILS-5</a></td>
<td></td>
<td>[dbutils] vendorCode and SQLState not included in SQLException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-4">DBUTILS-4</a></td>
<td></td>
<td>[dbutils] ResultSetIterator should rethrow SQLExceptions as RuntimException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-3">DBUTILS-3</a></td>
<td></td>
<td>[dbutils] Setting bean properties fails silently</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-2">DBUTILS-2</a></td>
<td></td>
<td>[dbutils] QueryLoader cannot locate properties file on weblogic</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-1">DBUTILS-1</a></td>
<td></td>
<td>[dbutils] BeanListHandler and BeanHandler fail to support java.sql.Date()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-26">DBUTILS-26</a></td>
<td></td>
<td>[dbutils] Oracle 9.2.0 JDBC Timestamp Problem</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-25">DBUTILS-25</a></td>
<td></td>
<td>[dbutils] Proposal for a set of new ResultSetHandlers</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-23">DBUTILS-23</a></td>
<td></td>
<td>[dbutils] Updated docs for example.html page (select AS)</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-22">DBUTILS-22</a></td>
<td></td>
<td>[dbutils] QueryLoader.loadQueries() should be protected</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-21">DBUTILS-21</a></td>
<td></td>
<td>[dbutils] Add protected QueryRunner.prepareConnection()</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-20">DBUTILS-20</a></td>
<td></td>
<td>[dbutils] Implement Pluggable Adaptors to Make BeanHandler Smarter</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-18">DBUTILS-18</a></td>
<td></td>
<td>[dbutils] Allow user to provide type information for input parameters</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-16">DBUTILS-16</a></td>
<td></td>
<td>[dbutils] ResultSetRowProcessor abstract handler and some classes rework</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-15">DBUTILS-15</a></td>
<td></td>
<td>[dbutils] Patch for extending BasicRowProcessor</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-13">DBUTILS-13</a></td>
<td></td>
<td>[dbutils] Add QueryRunner.batch()</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-12">DBUTILS-12</a></td>
<td></td>
<td>[dbutils] Protected QueryRunner.close() methods</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DBUTILS-11">DBUTILS-11</a></td>
<td></td>
<td>[dbutils] ColumnListHandler implementation</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="surefire-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/surefire-report.html -->

<!-- page_index: 20 -->

# DbUtils – Surefire Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Surefire_Report"></a>Surefire Report</h2></section><section><a id="Summary"></a>
<h2><a name="Summary"></a>Summary</h2>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p>
<table>
<tr>
<th>Tests</th>
<th>Errors</th>
<th>Failures</th>
<th>Skipped</th>
<th>Success Rate</th>
<th>Time</th></tr>
<tr>
<td align="left">320</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>2.717 s</td></tr></table>
<p>Note: failures are anticipated and checked for with assertions while errors are unanticipated.</p>
</section><section><a id="Package_List"></a>
<h2><a name="Package_List"></a>Package List</h2>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p>
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
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers">org.apache.commons.dbutils.handlers</a></td>
<td>52</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.207 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils">org.apache.commons.dbutils</a></td>
<td>179</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>1.308 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns">org.apache.commons.dbutils.handlers.columns</a></td>
<td>30</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.079 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties">org.apache.commons.dbutils.handlers.properties</a></td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.012 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.wrappers">org.apache.commons.dbutils.wrappers</a></td>
<td>49</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>1.111 s</td></tr></table>
<p>Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.</p><section><a id="org.apache.commons.dbutils.handlers"></a>
<h3><a name="org.apache.commons.dbutils.handlers"></a>org.apache.commons.dbutils.handlers</h3>
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
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columnlisthandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columnlisthandlertest">ColumnListHandlerTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.057 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.beanlisthandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.beanlisthandlertest">BeanListHandlerTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.011 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.maplisthandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.maplisthandlertest">MapListHandlerTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.011 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.beanmaphandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.beanmaphandlertest">BeanMapHandlerTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.043 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.beanhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.beanhandlertest">BeanHandlerTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.012 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.maphandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.maphandlertest">MapHandlerTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.021 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.arraylisthandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.arraylisthandlertest">ArrayListHandlerTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.009 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.keyedhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.keyedhandlertest">KeyedHandlerTest</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.021 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.scalarhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.scalarhandlertest">ScalarHandlerTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.arrayhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.arrayhandlertest">ArrayHandlerTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.016 s</td></tr></table></section><section><a id="org.apache.commons.dbutils"></a>
<h3><a name="org.apache.commons.dbutils"></a>org.apache.commons.dbutils</h3>
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
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.queryloadertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.queryloadertest">QueryLoaderTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.resultsetiteratortest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.resultsetiteratortest">ResultSetIteratorTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.010 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.outparametertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.outparametertest">OutParameterTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.255 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.queryrunnertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.queryrunnertest">QueryRunnerTest</a></td>
<td>57</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.271 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.asyncqueryrunnertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.asyncqueryrunnertest">AsyncQueryRunnerTest</a></td>
<td>32</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.526 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.dbutilstest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.dbutilstest">DbUtilsTest</a></td>
<td>36</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.072 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.statementconfigurationtest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.statementconfigurationtest">StatementConfigurationTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.037 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.dbutilstest-driverproxytest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.dbutilstest-driverproxytest">DbUtilsTest$DriverProxyTest</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.038 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.serviceloadertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.serviceloadertest">ServiceLoaderTest</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.007 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.basicrowprocessortest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.basicrowprocessortest">BasicRowProcessorTest</a></td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.013 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.baseresultsethandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.baseresultsethandlertest">BaseResultSetHandlerTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.beanprocessortest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.beanprocessortest">BeanProcessorTest</a></td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.032 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.proxyfactorytest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.proxyfactorytest">ProxyFactoryTest</a></td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.034 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.generousbeanprocessortest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.generousbeanprocessortest">GenerousBeanProcessorTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.009 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns"></a>
<h3><a name="org.apache.commons.dbutils.handlers.columns"></a>org.apache.commons.dbutils.handlers.columns</h3>
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
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.stringcolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.stringcolumnhandlertest">StringColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.sqlxmlcolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.sqlxmlcolumnhandlertest">SQLXMLColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.037 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.doublecolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.doublecolumnhandlertest">DoubleColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.shortcolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.shortcolumnhandlertest">ShortColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.longcolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.longcolumnhandlertest">LongColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.timestampcolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.timestampcolumnhandlertest">TimestampColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.booleancolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.booleancolumnhandlertest">BooleanColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.008 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.bytecolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.bytecolumnhandlertest">ByteColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.008 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.floatcolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.floatcolumnhandlertest">FloatColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.integercolumnhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.columns.integercolumnhandlertest">IntegerColumnHandlerTest</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.008 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.properties"></a>
<h3><a name="org.apache.commons.dbutils.handlers.properties"></a>org.apache.commons.dbutils.handlers.properties</h3>
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
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties.datepropertyhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties.datepropertyhandlertest">DatePropertyHandlerTest</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties.propertyhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties.propertyhandlertest">PropertyHandlerTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties.stringenumpropertyhandlertest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.handlers.properties.stringenumpropertyhandlertest">StringEnumPropertyHandlerTest</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.003 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.wrappers"></a>
<h3><a name="org.apache.commons.dbutils.wrappers"></a>org.apache.commons.dbutils.wrappers</h3>
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
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.wrappers.stringtrimmedresultsettest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.wrappers.stringtrimmedresultsettest">StringTrimmedResultSetTest</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>0.057 s</td></tr>
<tr>
<td align="left"><a href="#surefire-report--org.apache.commons.dbutils.wrappers.sqlnullcheckedresultsettest"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></a></td>
<td><a href="#surefire-report--org.apache.commons.dbutils.wrappers.sqlnullcheckedresultsettest">SqlNullCheckedResultSetTest</a></td>
<td>44</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>100%</td>
<td>1.054 s</td></tr></table></section>
</section><section><a id="Test_Cases"></a>
<h2><a name="Test_Cases"></a>Test Cases</h2>
<p>[<a href="#surefire-report--summary">Summary</a>] [<a href="#surefire-report--package_list">Package List</a>] [<a href="#surefire-report--test_cases">Test Cases</a>]</p><section><a id="org.apache.commons.dbutils.QueryLoaderTest"></a>
<h3><a name="QueryLoaderTest"></a>QueryLoaderTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryLoaderTest.testLoad"></a>testLoad</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryLoaderTest.testLoadThrowsIllegalArgumentException"></a>testLoadThrowsIllegalArgumentException</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryLoaderTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryLoaderTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest"></a>
<h3><a name="DatePropertyHandlerTest"></a>DatePropertyHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest.testNotMatch"></a>testNotMatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest.testMatch"></a>testMatch</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest.testApplyTypeOfDate"></a>testApplyTypeOfDate</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest.testApplyTypeOfTime"></a>testApplyTypeOfTime</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.DatePropertyHandlerTest.testApplyTypeOfTimestamp"></a>testApplyTypeOfTimestamp</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.ColumnListHandlerTest"></a>
<h3><a name="ColumnListHandlerTest"></a>ColumnListHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ColumnListHandlerTest.testColumnNameHandle"></a>testColumnNameHandle</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ColumnListHandlerTest.testColumnIndexHandle"></a>testColumnIndexHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ColumnListHandlerTest.testHandle"></a>testHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ColumnListHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ColumnListHandlerTest.testResultSets"></a>testResultSets</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ColumnListHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.BeanListHandlerTest"></a>
<h3><a name="BeanListHandlerTest"></a>BeanListHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanListHandlerTest.testHandleToInterface"></a>testHandleToInterface</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanListHandlerTest.testHandleToSuperClass"></a>testHandleToSuperClass</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanListHandlerTest.testHandle"></a>testHandle</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanListHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanListHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanListHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.wrappers.StringTrimmedResultSetTest"></a>
<h3><a name="StringTrimmedResultSetTest"></a>StringTrimmedResultSetTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.StringTrimmedResultSetTest.testMultipleWrappers"></a>testMultipleWrappers</td>
<td>0.035 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.StringTrimmedResultSetTest.testGetObject"></a>testGetObject</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.StringTrimmedResultSetTest.testGetString"></a>testGetString</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.StringTrimmedResultSetTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.StringTrimmedResultSetTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.ResultSetIteratorTest"></a>
<h3><a name="ResultSetIteratorTest"></a>ResultSetIteratorTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ResultSetIteratorTest.testNext"></a>testNext</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ResultSetIteratorTest.testCreatesResultSetIteratorTakingThreeArgumentsAndCallsRemove"></a>testCreatesResultSetIteratorTakingThreeArgumentsAndCallsRemove</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ResultSetIteratorTest.testRethrowThrowsRuntimeException"></a>testRethrowThrowsRuntimeException</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ResultSetIteratorTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ResultSetIteratorTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.OutParameterTest"></a>
<h3><a name="OutParameterTest"></a>OutParameterTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.OutParameterTest.testRegister"></a>testRegister</td>
<td>0.237 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.OutParameterTest.testRegisterAlternateConstructor"></a>testRegisterAlternateConstructor</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.OutParameterTest.testSetValue"></a>testSetValue</td>
<td>0.007 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.QueryRunnerTest"></a>
<h3><a name="QueryRunnerTest"></a>QueryRunnerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNoParamsUpdate"></a>testNoParamsUpdate</td>
<td>0.029 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testFillStatementWithBean"></a>testFillStatementWithBean</td>
<td>0.007 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testStatementConfiguration"></a>testStatementConfiguration</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullHandlerQuery"></a>testNullHandlerQuery</td>
<td>0.019 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNoParamsExecuteWithResultSet"></a>testNoParamsExecuteWithResultSet</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodExecute"></a>testGoodExecute</td>
<td>0.013 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodInsert"></a>testGoodInsert</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodExecuteWithResultSetPmdTrue"></a>testGoodExecuteWithResultSetPmdTrue</td>
<td>0.007 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodUpdatePmdTrue"></a>testGoodUpdatePmdTrue</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testExecuteUpdateException"></a>testExecuteUpdateException</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNoParamsExecute"></a>testNoParamsExecute</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodUpdate"></a>testGoodUpdate</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodBatchInsert"></a>testGoodBatchInsert</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testBadPrepareConnection"></a>testBadPrepareConnection</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testFillStatementWithBeanNullNames"></a>testFillStatementWithBeanNullNames</td>
<td>0.009 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodQueryPmdTrue"></a>testGoodQueryPmdTrue</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooManyParamsExecuteWithResultSet"></a>testTooManyParamsExecuteWithResultSet</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testAddBatchExceptionOnAdd"></a>testAddBatchExceptionOnAdd</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodUpdateDefaultConstructor"></a>testGoodUpdateDefaultConstructor</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullConnectionBatch"></a>testNullConnectionBatch</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullConnectionQuery"></a>testNullConnectionQuery</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodExecutePmdTrue"></a>testGoodExecutePmdTrue</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullConnectionExecuteWithResultSet"></a>testNullConnectionExecuteWithResultSet</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooManyParamsBatch"></a>testTooManyParamsBatch</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullSqlBatch"></a>testNullSqlBatch</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooManyParamsQuery"></a>testTooManyParamsQuery</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullSqlQuery"></a>testNullSqlQuery</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooFewParamsBatch"></a>testTooFewParamsBatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooFewParamsQuery"></a>testTooFewParamsQuery</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullSqlExecuteWithResultSet"></a>testNullSqlExecuteWithResultSet</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNoParamsQuery"></a>testNoParamsQuery</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooManyParamsUpdate"></a>testTooManyParamsUpdate</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullParamsArgBatch"></a>testNullParamsArgBatch</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testExecuteBatchExceptionOnExec"></a>testExecuteBatchExceptionOnExec</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodExecuteDefaultConstructor"></a>testGoodExecuteDefaultConstructor</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodBatchDefaultConstructor"></a>testGoodBatchDefaultConstructor</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooFewParamsExecuteWithResultSet"></a>testTooFewParamsExecuteWithResultSet</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullConnectionUpdate"></a>testNullConnectionUpdate</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullSqlUpdate"></a>testNullSqlUpdate</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullHandlerExecuteWithResultSet"></a>testNullHandlerExecuteWithResultSet</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodExecuteWithResultSet"></a>testGoodExecuteWithResultSet</td>
<td>0.008 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testExecuteWithMultipleResultSets"></a>testExecuteWithMultipleResultSets</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullHandlerExecute"></a>testNullHandlerExecute</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooManyParamsExecute"></a>testTooManyParamsExecute</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooFewParamsExecute"></a>testTooFewParamsExecute</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullConnectionExecute"></a>testNullConnectionExecute</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testExecuteQueryException"></a>testExecuteQueryException</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testExecuteWithResultSetException"></a>testExecuteWithResultSetException</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testTooFewParamsUpdate"></a>testTooFewParamsUpdate</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullSqlExecute"></a>testNullSqlExecute</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodExecuteWithResultSetDefaultConstructor"></a>testGoodExecuteWithResultSetDefaultConstructor</td>
<td>0.017 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testExecuteException"></a>testExecuteException</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testNullParamsBatch"></a>testNullParamsBatch</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodBatch"></a>testGoodBatch</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodQueryDefaultConstructor"></a>testGoodQueryDefaultConstructor</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodQuery"></a>testGoodQuery</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.QueryRunnerTest.testGoodBatchPmdTrue"></a>testGoodBatchPmdTrue</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.StringColumnHandlerTest"></a>
<h3><a name="StringColumnHandlerTest"></a>StringColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.StringColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.StringColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.StringColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.AsyncQueryRunnerTest"></a>
<h3><a name="AsyncQueryRunnerTest"></a>AsyncQueryRunnerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNoParamsUpdate"></a>testNoParamsUpdate</td>
<td>0.234 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullHandlerQuery"></a>testNullHandlerQuery</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodUpdatePmdTrue"></a>testGoodUpdatePmdTrue</td>
<td>0.008 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testExecuteUpdateException"></a>testExecuteUpdateException</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodUpdate"></a>testGoodUpdate</td>
<td>0.012 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testBadPrepareConnection"></a>testBadPrepareConnection</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodQueryPmdTrue"></a>testGoodQueryPmdTrue</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodUpdateDefaultConstructor"></a>testGoodUpdateDefaultConstructor</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullConnectionBatch"></a>testNullConnectionBatch</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullConnectionQuery"></a>testNullConnectionQuery</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testTooManyParamsBatch"></a>testTooManyParamsBatch</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullSqlBatch"></a>testNullSqlBatch</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testTooManyParamsQuery"></a>testTooManyParamsQuery</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullSqlQuery"></a>testNullSqlQuery</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testAddBatchException"></a>testAddBatchException</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testExecuteBatchException"></a>testExecuteBatchException</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testTooFewParamsBatch"></a>testTooFewParamsBatch</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testTooFewParamsQuery"></a>testTooFewParamsQuery</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNoParamsQuery"></a>testNoParamsQuery</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testTooManyParamsUpdate"></a>testTooManyParamsUpdate</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullParamsArgBatch"></a>testNullParamsArgBatch</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodBatchDefaultConstructor"></a>testGoodBatchDefaultConstructor</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullConnectionUpdate"></a>testNullConnectionUpdate</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullSqlUpdate"></a>testNullSqlUpdate</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testInsertUsesGivenQueryRunner"></a>testInsertUsesGivenQueryRunner</td>
<td>0.159 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testExecuteQueryException"></a>testExecuteQueryException</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testTooFewParamsUpdate"></a>testTooFewParamsUpdate</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testNullParamsBatch"></a>testNullParamsBatch</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodBatch"></a>testGoodBatch</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodQueryDefaultConstructor"></a>testGoodQueryDefaultConstructor</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodQuery"></a>testGoodQuery</td>
<td>0.007 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.AsyncQueryRunnerTest.testGoodBatchPmdTrue"></a>testGoodBatchPmdTrue</td>
<td>0.003 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.MapListHandlerTest"></a>
<h3><a name="MapListHandlerTest"></a>MapListHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapListHandlerTest.testHandle"></a>testHandle</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapListHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapListHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapListHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.DbUtilsTest"></a>
<h3><a name="DbUtilsTest"></a>DbUtilsTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeStatement"></a>closeStatement</td>
<td>0.008 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.commitAndClose"></a>commitAndClose</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeResultSet"></a>closeResultSet</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyNullStatement"></a>closeQuietlyNullStatement</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackQuietly"></a>rollbackQuietly</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackQuietlyNull"></a>rollbackQuietlyNull</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyNullResultSet"></a>closeQuietlyNullResultSet</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyResultSetThrowingException"></a>closeQuietlyResultSetThrowingException</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.commitAndCloseQuietly"></a>commitAndCloseQuietly</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyConnectionResultSetStatementThrowingException"></a>closeQuietlyConnectionResultSetStatementThrowingException</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyStatement"></a>closeQuietlyStatement</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackQuietlyWithException"></a>rollbackQuietlyWithException</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyResultSet"></a>closeQuietlyResultSet</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackAndClose"></a>rollbackAndClose</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeConnection"></a>closeConnection</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollback"></a>rollback</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyStatementThrowingException"></a>closeQuietlyStatementThrowingException</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackAndCloseQuietlyNull"></a>rollbackAndCloseQuietlyNull</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackAndCloseQuietly"></a>rollbackAndCloseQuietly</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackNull"></a>rollbackNull</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.testCommitAndCloseQuietlyWithNullDoesNotThrowAnSQLException"></a>testCommitAndCloseQuietlyWithNullDoesNotThrowAnSQLException</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackAndCloseQuietlyWithException"></a>rollbackAndCloseQuietlyWithException</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.testLoadDriverReturnsFalse"></a>testLoadDriverReturnsFalse</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyNullConnection"></a>closeQuietlyNullConnection</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyConnection"></a>closeQuietlyConnection</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyConnectionThrowingException"></a>closeQuietlyConnectionThrowingException</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackAndCloseWithException"></a>rollbackAndCloseWithException</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeNullStatement"></a>closeNullStatement</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeNullConnection"></a>closeNullConnection</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.commitAndCloseQuietlyWithException"></a>commitAndCloseQuietlyWithException</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.rollbackAndCloseNull"></a>rollbackAndCloseNull</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeNullResultSet"></a>closeNullResultSet</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyConnectionThrowingExceptionResultSetStatement"></a>closeQuietlyConnectionThrowingExceptionResultSetStatement</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyConnectionResultSetStatement"></a>closeQuietlyConnectionResultSetStatement</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.closeQuietlyConnectionResultSetThrowingExceptionStatement"></a>closeQuietlyConnectionResultSetThrowingExceptionStatement</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTest.commitAndCloseWithException"></a>commitAndCloseWithException</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.SQLXMLColumnHandlerTest"></a>
<h3><a name="SQLXMLColumnHandlerTest"></a>SQLXMLColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.SQLXMLColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.034 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.SQLXMLColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.SQLXMLColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.StatementConfigurationTest"></a>
<h3><a name="StatementConfigurationTest"></a>StatementConfigurationTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.StatementConfigurationTest.testBuilder"></a>testBuilder</td>
<td>0.029 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.StatementConfigurationTest.testEmptyBuilder"></a>testEmptyBuilder</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.StatementConfigurationTest.testConstructor"></a>testConstructor</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.DbUtilsTest$DriverProxyTest"></a>
<h3><a name="DbUtilsTest.24DriverProxyTest"></a>DbUtilsTest$DriverProxyTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.DbUtilsTestDriverProxyTest.testProxiedMethods"></a>testProxiedMethods</td>
<td>0.037 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.ServiceLoaderTest"></a>
<h3><a name="ServiceLoaderTest"></a>ServiceLoaderTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ServiceLoaderTest.testFindMoreThanLocalColumns"></a>testFindMoreThanLocalColumns</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ServiceLoaderTest.testFindMoreThanLocalProperties"></a>testFindMoreThanLocalProperties</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ServiceLoaderTest.testFindsLocalPropertyHandler"></a>testFindsLocalPropertyHandler</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ServiceLoaderTest.testFindsLocalColumnHandler"></a>testFindsLocalColumnHandler</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.BeanMapHandlerTest"></a>
<h3><a name="BeanMapHandlerTest"></a>BeanMapHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanMapHandlerTest.testEmptyResultSet"></a>testEmptyResultSet</td>
<td>0.033 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanMapHandlerTest.testBeanMapHandlerClassOfV"></a>testBeanMapHandlerClassOfV</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanMapHandlerTest.testBeanMapHandlerClassOfVRowProcessor"></a>testBeanMapHandlerClassOfVRowProcessor</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanMapHandlerTest.testBeanMapHandlerClassOfVInt"></a>testBeanMapHandlerClassOfVInt</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanMapHandlerTest.testBeanMapHandlerClassOfVString"></a>testBeanMapHandlerClassOfVString</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.BeanHandlerTest"></a>
<h3><a name="BeanHandlerTest"></a>BeanHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanHandlerTest.testHandleToInterface"></a>testHandleToInterface</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanHandlerTest.testHandleToSuperClass"></a>testHandleToSuperClass</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanHandlerTest.testHandle"></a>testHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.BeanHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.BasicRowProcessorTest"></a>
<h3><a name="BasicRowProcessorTest"></a>BasicRowProcessorTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testToArray"></a>testToArray</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testToMap"></a>testToMap</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testToBeanList"></a>testToBeanList</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testPutAllContainsKeyAndRemove"></a>testPutAllContainsKeyAndRemove</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testToMapOrdering"></a>testToMapOrdering</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testToBean"></a>testToBean</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testResultSets"></a>testResultSets</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BasicRowProcessorTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.MapHandlerTest"></a>
<h3><a name="MapHandlerTest"></a>MapHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapHandlerTest.testHandle"></a>testHandle</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapHandlerTest.testResultSets"></a>testResultSets</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.MapHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.DoubleColumnHandlerTest"></a>
<h3><a name="DoubleColumnHandlerTest"></a>DoubleColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.DoubleColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.DoubleColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.DoubleColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.ShortColumnHandlerTest"></a>
<h3><a name="ShortColumnHandlerTest"></a>ShortColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.ShortColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.ShortColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.ShortColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.LongColumnHandlerTest"></a>
<h3><a name="LongColumnHandlerTest"></a>LongColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.LongColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.LongColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.LongColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.TimestampColumnHandlerTest"></a>
<h3><a name="TimestampColumnHandlerTest"></a>TimestampColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.TimestampColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.TimestampColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.TimestampColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest"></a>
<h3><a name="SqlNullCheckedResultSetTest"></a>SqlNullCheckedResultSetTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullBoolean"></a>testSetNullBoolean</td>
<td>0.009 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetBytes"></a>testGetBytes</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetFloat"></a>testGetFloat</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetShort"></a>testGetShort</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullBigDecimal"></a>testSetNullBigDecimal</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testURL"></a>testURL</td>
<td>0.057 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullBytes"></a>testSetNullBytes</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullFloat"></a>testSetNullFloat</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullShort"></a>testSetNullShort</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullBinaryStream"></a>testSetNullBinaryStream</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullBlob"></a>testSetNullBlob</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullByte"></a>testSetNullByte</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullClob"></a>testSetNullClob</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullDate"></a>testSetNullDate</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullLong"></a>testSetNullLong</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullTime"></a>testSetNullTime</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetBlob"></a>testGetBlob</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetByte"></a>testGetByte</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetClob"></a>testGetClob</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetDate"></a>testGetDate</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetLong"></a>testGetLong</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetTime"></a>testGetTime</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullDouble"></a>testSetNullDouble</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetAsciiStream"></a>testGetAsciiStream</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullObject"></a>testSetNullObject</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetCharacterStream"></a>testGetCharacterStream</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullString"></a>testSetNullString</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullInt"></a>testSetNullInt</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullRef"></a>testSetNullRef</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testWrapResultSet"></a>testWrapResultSet</td>
<td>0.948 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetBoolean"></a>testGetBoolean</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullAsciiStream"></a>testSetNullAsciiStream</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetDouble"></a>testGetDouble</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetBigDecimal"></a>testGetBigDecimal</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetTimestamp"></a>testGetTimestamp</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetObject"></a>testGetObject</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullCharacterStream"></a>testSetNullCharacterStream</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetInt"></a>testGetInt</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetRef"></a>testGetRef</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetBinaryStream"></a>testGetBinaryStream</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testGetString"></a>testGetString</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testSetNullTimestamp"></a>testSetNullTimestamp</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.wrappers.SqlNullCheckedResultSetTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.properties.PropertyHandlerTest"></a>
<h3><a name="PropertyHandlerTest"></a>PropertyHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.PropertyHandlerTest.testServiceLoaderFindsMultipleRegistries"></a>testServiceLoaderFindsMultipleRegistries</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.PropertyHandlerTest.testFoundMoreThanLocal"></a>testFoundMoreThanLocal</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.BaseResultSetHandlerTest"></a>
<h3><a name="BaseResultSetHandlerTest"></a>BaseResultSetHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BaseResultSetHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BaseResultSetHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.BooleanColumnHandlerTest"></a>
<h3><a name="BooleanColumnHandlerTest"></a>BooleanColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.BooleanColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.BooleanColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.BooleanColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.ArrayListHandlerTest"></a>
<h3><a name="ArrayListHandlerTest"></a>ArrayListHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayListHandlerTest.testHandle"></a>testHandle</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayListHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayListHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayListHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.ByteColumnHandlerTest"></a>
<h3><a name="ByteColumnHandlerTest"></a>ByteColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.ByteColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.ByteColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.ByteColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.KeyedHandlerTest"></a>
<h3><a name="KeyedHandlerTest"></a>KeyedHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testColumnNameHandle"></a>testColumnNameHandle</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testColumnIndexHandle"></a>testColumnIndexHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testHandle"></a>testHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testInjectedRowProcess"></a>testInjectedRowProcess</td>
<td>0.013 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.KeyedHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.FloatColumnHandlerTest"></a>
<h3><a name="FloatColumnHandlerTest"></a>FloatColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.FloatColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.FloatColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.FloatColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0.003 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.BeanProcessorTest"></a>
<h3><a name="BeanProcessorTest"></a>BeanProcessorTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testMapColumnToProperties"></a>testMapColumnToProperties</td>
<td>0.011 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testIndexedPropertyDescriptor"></a>testIndexedPropertyDescriptor</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testProcessWithToBean"></a>testProcessWithToBean</td>
<td>0.005 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testWrongSetterParamCount"></a>testWrongSetterParamCount</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testMapColumnToAnnotationField"></a>testMapColumnToAnnotationField</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testProcessWithPopulateBean"></a>testProcessWithPopulateBean</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testMapColumnToPropertiesWithOverrides"></a>testMapColumnToPropertiesWithOverrides</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testCheckAnnotationOnMissingReadMethod"></a>testCheckAnnotationOnMissingReadMethod</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.BeanProcessorTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.ScalarHandlerTest"></a>
<h3><a name="ScalarHandlerTest"></a>ScalarHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ScalarHandlerTest.testColumnNameHandle"></a>testColumnNameHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ScalarHandlerTest.testColumnIndexHandle"></a>testColumnIndexHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ScalarHandlerTest.testHandle"></a>testHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ScalarHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ScalarHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ScalarHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.columns.IntegerColumnHandlerTest"></a>
<h3><a name="IntegerColumnHandlerTest"></a>IntegerColumnHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.IntegerColumnHandlerTest.testApplyType"></a>testApplyType</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.IntegerColumnHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.columns.IntegerColumnHandlerTest.testMatch"></a>testMatch</td>
<td>0.002 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.ProxyFactoryTest"></a>
<h3><a name="ProxyFactoryTest"></a>ProxyFactoryTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreatePreparedStatement"></a>testCreatePreparedStatement</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreateConnection"></a>testCreateConnection</td>
<td>0.006 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreateStatement"></a>testCreateStatement</td>
<td>0.004 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreateResultSet"></a>testCreateResultSet</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreateCallableStatement"></a>testCreateCallableStatement</td>
<td>0.012 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreateResultSetMetaData"></a>testCreateResultSetMetaData</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCreateDriver"></a>testCreateDriver</td>
<td>0.002 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.ProxyFactoryTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.GenerousBeanProcessorTest"></a>
<h3><a name="GenerousBeanProcessorTest"></a>GenerousBeanProcessorTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.GenerousBeanProcessorTest.testMapColumnsToPropertiesWithUnderscores"></a>testMapColumnsToPropertiesWithUnderscores</td>
<td>0.003 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.GenerousBeanProcessorTest.testMapColumnsToPropertiesMixedCase"></a>testMapColumnsToPropertiesMixedCase</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.GenerousBeanProcessorTest.testMapColumnsToPropertiesColumnLabelIsNull"></a>testMapColumnsToPropertiesColumnLabelIsNull</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.GenerousBeanProcessorTest.testMapColumnsToPropertiesWithSpaces"></a>testMapColumnsToPropertiesWithSpaces</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.GenerousBeanProcessorTest.testMapColumnsToPropertiesWithOutUnderscores"></a>testMapColumnsToPropertiesWithOutUnderscores</td>
<td>0.001 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.ArrayHandlerTest"></a>
<h3><a name="ArrayHandlerTest"></a>ArrayHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayHandlerTest.testHandle"></a>testHandle</td>
<td>0.001 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayHandlerTest.testEmptyResultSetHandle"></a>testEmptyResultSetHandle</td>
<td>0.014 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayHandlerTest.testResultSets"></a>testResultSets</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.ArrayHandlerTest.testCheckDataSizes"></a>testCheckDataSizes</td>
<td>0 s</td></tr></table></section><section><a id="org.apache.commons.dbutils.handlers.properties.StringEnumPropertyHandlerTest"></a>
<h3><a name="StringEnumPropertyHandlerTest"></a>StringEnumPropertyHandlerTest</h3>
<table>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.StringEnumPropertyHandlerTest.testMatch"></a>testMatch</td>
<td>0 s</td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-success-sml_767e06477cefe211.gif"/></td>
<td><a id="TC_org.apache.commons.dbutils.handlers.properties.StringEnumPropertyHandlerTest.testMatchNegative"></a>testMatchNegative</td>
<td>0 s</td></tr></table></section>
</section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/rat-report.html -->

<!-- page_index: 21 -->

# DbUtils – Rat (Release Audit Tool) results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Rat_.28Release_Audit_Tool.29_results"></a>Rat (Release Audit Tool) results</h2>
<p>The following document contains the results of <a href="https://creadur.apache.org/rat/apache-rat-plugin/">Rat (Release Audit Tool)</a>.</p>
<p></p>
<div>
<pre>
*****************************************************
Summary
-------
Generated at: 2023-09-15T07:54:40-04:00

Notes: 3
Binaries: 1
Archives: 0
Standards: 128

Apache Licensed: 128
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
  AL    .github/workflows/coverage.yml
  AL    .github/workflows/maven.yml
  AL    .github/workflows/codeql-analysis.yml
  AL    .github/workflows/scorecards-analysis.yml
  AL    .github/dependabot.yml
  N     LICENSE.txt
  AL    SECURITY.md
  AL    src/test/resources/org/apache/commons/dbutils/TestQueries.properties
  AL    src/test/resources/META-INF/services/org.apache.commons.dbutils.PropertyHandler
  AL    src/test/resources/META-INF/services/org.apache.commons.dbutils.ColumnHandler
  AL    src/test/java/org/apache/commons/dbutils/ServiceLoaderTest.java
  AL    src/test/java/org/apache/commons/dbutils/wrappers/SqlNullCheckedResultSetTest.java
  AL    src/test/java/org/apache/commons/dbutils/wrappers/StringTrimmedResultSetTest.java
  AL    src/test/java/org/apache/commons/dbutils/BeanProcessorTest.java
  AL    src/test/java/org/apache/commons/dbutils/BaseResultSetHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/DbUtilsTest.java
  AL    src/test/java/org/apache/commons/dbutils/StatementConfigurationTest.java
  AL    src/test/java/org/apache/commons/dbutils/BaseTestCase.java
  AL    src/test/java/org/apache/commons/dbutils/TestBean.java
  AL    src/test/java/org/apache/commons/dbutils/OutParameterTest.java
  AL    src/test/java/org/apache/commons/dbutils/AsyncQueryRunnerTest.java
  AL    src/test/java/org/apache/commons/dbutils/BasicRowProcessorTest.java
  AL    src/test/java/org/apache/commons/dbutils/ProxyFactoryTest.java
  AL    src/test/java/org/apache/commons/dbutils/GenerousBeanProcessorTest.java
  AL    src/test/java/org/apache/commons/dbutils/QueryRunnerTest.java
  AL    src/test/java/org/apache/commons/dbutils/MockResultSet.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/ColumnListHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/BeanMapHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/ArrayHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/MapListHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/ArrayListHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/BeanHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/MapHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/properties/DatePropertyHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/properties/TestEnum.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/properties/StringEnumPropertyHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/properties/TestPropertyHandler.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/properties/PropertyHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/ByteColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/TimestampColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/LongColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/ShortColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/FloatColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/DoubleColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/AbstractTestColumnHandler.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/IntegerColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/StringColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/SQLXMLColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/TestColumnHandler.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/columns/BooleanColumnHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/KeyedHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/BeanListHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/handlers/ScalarHandlerTest.java
  AL    src/test/java/org/apache/commons/dbutils/ResultSetIteratorTest.java
  AL    src/test/java/org/apache/commons/dbutils/QueryLoaderTest.java
  AL    src/test/java/org/apache/commons/dbutils/MockResultSetMetaData.java
  AL    src/changes/release-notes.vm
  AL    src/changes/changes.xml
  AL    src/site/resources/checkstyle/checkstyle-suppressions.xml
  AL    src/site/resources/checkstyle/checkstyle.xml
  AL    src/site/resources/checkstyle/checkstyle-header.txt
  AL    src/site/resources/spotbugs/sb-excludes.xml
  B     src/site/resources/images/logo.png
  AL    src/site/resources/pmd/pmd-ruleset.xml
  AL    src/site/xdoc/download_dbutils.xml
  AL    src/site/xdoc/index.xml
  AL    src/site/xdoc/mail-lists.xml
  AL    src/site/xdoc/examples.xml
  AL    src/site/xdoc/proposal.xml
  AL    src/site/xdoc/building.xml
  AL    src/site/xdoc/issue-tracking.xml
  AL    src/site/site.xml
  AL    src/main/assembly/src.xml
  AL    src/main/assembly/bin.xml
  AL    src/main/resources/META-INF/services/org.apache.commons.dbutils.PropertyHandler
  AL    src/main/resources/META-INF/services/org.apache.commons.dbutils.ColumnHandler
  AL    src/main/java/org/apache/commons/dbutils/DbUtils.java
  AL    src/main/java/org/apache/commons/dbutils/wrappers/StringTrimmedResultSet.java
  AL    src/main/java/org/apache/commons/dbutils/wrappers/SqlNullCheckedResultSet.java
  AL    src/main/java/org/apache/commons/dbutils/wrappers/package-info.java
  AL    src/main/java/org/apache/commons/dbutils/ProxyFactory.java
  AL    src/main/java/org/apache/commons/dbutils/ColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/AbstractQueryRunner.java
  AL    src/main/java/org/apache/commons/dbutils/StatementConfiguration.java
  AL    src/main/java/org/apache/commons/dbutils/BaseResultSetHandler.java
  AL    src/main/java/org/apache/commons/dbutils/ResultSetHandler.java
  AL    src/main/java/org/apache/commons/dbutils/Column.java
  AL    src/main/java/org/apache/commons/dbutils/OutParameter.java
  AL    src/main/java/org/apache/commons/dbutils/GenerousBeanProcessor.java
  AL    src/main/java/org/apache/commons/dbutils/RowProcessor.java
  AL    src/main/java/org/apache/commons/dbutils/AsyncQueryRunner.java
  AL    src/main/java/org/apache/commons/dbutils/QueryRunner.java
  AL    src/main/java/org/apache/commons/dbutils/BasicRowProcessor.java
  AL    src/main/java/org/apache/commons/dbutils/BeanProcessor.java
  AL    src/main/java/org/apache/commons/dbutils/PropertyHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/ColumnListHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/ScalarHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/ArrayListHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/ArrayHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/MapListHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/BeanListHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/KeyedHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/properties/StringEnumPropertyHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/properties/package-info.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/BeanHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/MapHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/IntegerColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/DoubleColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/ByteColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/FloatColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/LongColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/BooleanColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/SQLXMLColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/StringColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/TimestampColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/package-info.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/columns/ShortColumnHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/BeanMapHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/AbstractKeyedHandler.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/package-info.java
  AL    src/main/java/org/apache/commons/dbutils/handlers/AbstractListHandler.java
  AL    src/main/java/org/apache/commons/dbutils/QueryLoader.java
  AL    src/main/java/org/apache/commons/dbutils/package-info.java
  AL    src/main/java/org/apache/commons/dbutils/ResultSetIterator.java

*****************************************************
</pre></div></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/checkstyle.html -->

<!-- page_index: 22 -->

# DbUtils – Checkstyle Results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
<h2><a name="Checkstyle_Results"></a>Checkstyle Results</h2><a name="Checkstyle_Results"></a>
<p>The following document contains the results of <a href="https://checkstyle.org/">Checkstyle</a> 9.3 with /Users/garydgregory/git/commons-dbutils/src/site/resources/checkstyle/checkstyle.xml ruleset.</p><section>
<h3><a name="Summary"></a>Summary</h3><a name="Summary"></a>
<table>
<tr>
<th>Files</th>
<th><img alt="" src="assets/images/icon-info-sml_3175091237ea0852.gif"/> Info</th>
<th><img alt="" src="assets/images/icon-warning-sml_d180265c216cf638.gif"/> Warnings</th>
<th><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Errors</th></tr>
<tr>
<td align="left">55</td>
<td>0</td>
<td>0</td>
<td>14</td></tr></table></section><section>
<h3><a name="Files"></a>Files</h3><a name="Files"></a>
<table>
<tr>
<th>File</th>
<th><img alt="" src="assets/images/icon-info-sml_3175091237ea0852.gif"/> I</th>
<th><img alt="" src="assets/images/icon-warning-sml_d180265c216cf638.gif"/> W</th>
<th><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> E</th></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fabstractqueryrunner.java">org/apache/commons/dbutils/AbstractQueryRunner.java</a></td>
<td>0</td>
<td>0</td>
<td>1</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fbeanprocessor.java">org/apache/commons/dbutils/BeanProcessor.java</a></td>
<td>0</td>
<td>0</td>
<td>2</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fcolumnhandler.java">org/apache/commons/dbutils/ColumnHandler.java</a></td>
<td>0</td>
<td>0</td>
<td>3</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fpropertyhandler.java">org/apache/commons/dbutils/PropertyHandler.java</a></td>
<td>0</td>
<td>0</td>
<td>2</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fqueryrunner.java">org/apache/commons/dbutils/QueryRunner.java</a></td>
<td>0</td>
<td>0</td>
<td>1</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fstatementconfiguration.java">org/apache/commons/dbutils/StatementConfiguration.java</a></td>
<td>0</td>
<td>0</td>
<td>1</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fhandlers.2fkeyedhandler.java">org/apache/commons/dbutils/handlers/KeyedHandler.java</a></td>
<td>0</td>
<td>0</td>
<td>3</td></tr>
<tr>
<td align="left"><a href="#checkstyle--org.2fapache.2fcommons.2fdbutils.2fhandlers.2fproperties.2fdatepropertyhandler.java">org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.java</a></td>
<td>0</td>
<td>0</td>
<td>1</td></tr></table></section><section>
<h3><a name="Details"></a>Details</h3><a name="Details"></a><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FAbstractQueryRunner.java"></a>org/apache/commons/dbutils/AbstractQueryRunner.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FAbstractQueryRunner.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>design</td>
<td>VisibilityModifier</td>
<td>Variable 'ds' must be private and have accessor methods.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/AbstractQueryRunner.html#L54">54</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FBeanProcessor.java"></a>org/apache/commons/dbutils/BeanProcessor.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FBeanProcessor.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 159).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/BeanProcessor.html#L143">143</a></td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 140).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/BeanProcessor.html#L163">163</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FColumnHandler.java"></a>org/apache/commons/dbutils/ColumnHandler.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FColumnHandler.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 151).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/ColumnHandler.html#L23">23</a></td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 154).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/ColumnHandler.html#L30">30</a></td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 142).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/ColumnHandler.html#L36">36</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FPropertyHandler.java"></a>org/apache/commons/dbutils/PropertyHandler.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FPropertyHandler.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 140).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/PropertyHandler.html#L20">20</a></td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 154).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/PropertyHandler.html#L25">25</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FQueryRunner.java"></a>org/apache/commons/dbutils/QueryRunner.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FQueryRunner.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>whitespace</td>
<td>NoWhitespaceAfter</td>
<td>'{' is followed by whitespace.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/QueryRunner.html#L748">748</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FStatementConfiguration.java"></a>org/apache/commons/dbutils/StatementConfiguration.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2FStatementConfiguration.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 143).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/StatementConfiguration.html#L130">130</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2Fhandlers.2FKeyedHandler.java"></a>org/apache/commons/dbutils/handlers/KeyedHandler.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2Fhandlers.2FKeyedHandler.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>design</td>
<td>VisibilityModifier</td>
<td>Variable 'convert' must be private and have accessor methods.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/KeyedHandler.html#L58">58</a></td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>design</td>
<td>VisibilityModifier</td>
<td>Variable 'columnIndex' must be private and have accessor methods.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/KeyedHandler.html#L63">63</a></td></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>design</td>
<td>VisibilityModifier</td>
<td>Variable 'columnName' must be private and have accessor methods.</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/KeyedHandler.html#L69">69</a></td></tr></table></section><section>
<h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2Fhandlers.2Fproperties.2FDatePropertyHandler.java"></a>org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.java</h4><a name="org.2Fapache.2Fcommons.2Fdbutils.2Fhandlers.2Fproperties.2FDatePropertyHandler.java"></a>
<table>
<tr>
<th>Severity</th>
<th>Category</th>
<th>Rule</th>
<th>Message</th>
<th>Line</th></tr>
<tr>
<td align="left"><img alt="" src="assets/images/icon-error-sml_565875fcb5b379e6.gif"/> Error</td>
<td>sizes</td>
<td>LineLength</td>
<td>Line is longer than 132 characters (found 156).</td>
<td><a href="https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.html#L25">25</a></td></tr></table></section></section></section>
</td>
</tr>
</table>

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/spotbugs.html -->

<!-- page_index: 23 -->

## SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.7.3*

Threshold is

Effort is *default*

## Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 56 | 0 | 0 | 0 |

## Files

| Class | Bugs |
| --- | --- |

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/cpd.html -->

<!-- page_index: 24 -->

# DbUtils – CPD Results

|  |  |
| --- | --- |
|  | CPD Results The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 6.55.0.  CPD found no problems in your source code. |

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/pmd.html -->

<!-- page_index: 25 -->

# DbUtils – PMD Results

|  |  |
| --- | --- |
|  | PMD Results The following document contains the results of [PMD](https://pmd.github.io) 6.55.0.  PMD found no problems in your source code. |

Copyright © 2002-2023
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons DbUtils, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---
