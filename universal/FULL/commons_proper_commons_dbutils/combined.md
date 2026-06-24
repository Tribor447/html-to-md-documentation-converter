# DbUtils – Project Information

## Navigation

- [DbUtils](#japicmp)
  - [Overview](#index)
  - [Examples](#examples)
  - [Release Notes](#changes-report)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Source Repository](#scm)
  - [Building](#building)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes-report)
    - [JIRA Report](#jira-report)
    - [Surefire](#surefire-report)
    - [Rat Report](#rat-report)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [SpotBugs](#spotbugs)
    - [CPD](#cpd)
    - [PMD](#pmd)

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

<a id="index--commons-dbutils:-jdbc-utility-component"></a>

## Commons DbUtils: JDBC Utility Component

The Commons DbUtils library is a small set of classes designed to make working with
[JDBC](http://java.sun.com/products/jdbc/) easier. JDBC
resource cleanup code is mundane, error prone work so these classes
abstract out all of the cleanup tasks from your code leaving you with
what you really wanted to do with JDBC in the first place: query and
update data.

Some of the advantages of using DbUtils are:

- No possibility for resource leaks. Correct JDBC coding isn't
  difficult but it is time-consuming and tedious. This often
  leads to connection leaks that may be difficult to track down.
- Cleaner, clearer persistence code. The amount of code needed
  to persist data in a database is drastically reduced. The remaining
  code clearly expresses your intention without being cluttered
  with resource cleanup.
- Automatically populate JavaBean properties from ResultSets. You
  don't need to manually copy column values into bean instances
  by calling setter methods. Each row of the ResultSet can be
  represented by one fully populated bean instance.

<a id="index--scope-of-the-package"></a>

## Scope of the Package

DbUtils is designed to be:

- **Small** - you should be able to understand the
  whole package in a short amount of time.
- **Transparent** - DbUtils doesn't do any magic
  behind the scenes. You give it a query, it executes it and
  cleans up for you.
- **Fast** - You don't need to create a million
  temporary objects to work with DbUtils.

DbUtils is **not**:

- An Object/Relational bridge - there are plenty of good O/R tools
  already. DbUtils is for developers looking to use JDBC without all
  the mundane pieces.
- A Data Access Object (DAO) framework - DbUtils can be used to build
  a DAO framework though.
- An object oriented abstraction of general database
  objects like a Table, Column, or PrimaryKey.
- A heavyweight framework of any kind - the goal here is to be a
  straightforward and easy to use JDBC helper library.

<a id="index--example-usage"></a>

## Example Usage

Please see [Examples Page](#examples).

<a id="index--dependencies"></a>

## Dependencies

DbUtils is intentionally a single jar distribution and relies only on
a standard Java 8 or later JRE.

---

<a id="examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/examples.html -->

<!-- page_index: 3 -->

<a id="examples--dbutils:-jdbc-utility-component-examples"></a>

## DbUtils: JDBC Utility Component Examples

This page provides examples that show how DbUtils may be used.

<a id="examples--basic-usage"></a>

## Basic Usage

DbUtils is a very small library of classes so it won't take long
to go through the [javadocs](https://commons.apache.org/proper/commons-dbutils/apidocs/) for each class.
The core classes/interfaces in DbUtils are
`QueryRunner`
and
`ResultSetHandler`.
You don't need to know about any other DbUtils classes to benefit from using the
library. The following example demonstrates how these classes are used together.

```


// Create a ResultSetHandler implementation to convert the
// first row into an Object[].
ResultSetHandler<Object[]> h = new ResultSetHandler<Object[]>() {
    public Object[] handle(ResultSet rs) throws SQLException {
        if (!rs.next()) {
            return null;
        }
    
        ResultSetMetaData meta = rs.getMetaData();
        int cols = meta.getColumnCount();
        Object[] result = new Object[cols];

        for (int i = 0; i < cols; i++) {
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
```

You could also perform the previous query using a `java.sql.Connection` object
instead of a `DataSource`. Notice that you are responsible for closing the
`Connection` in this example.

```


ResultSetHandler<Object[]> h = ... // Define a handler the same as above example

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
```

You can not only fetch data from the database - you can also insert or update
data. The following example will first insert a person into the database and
after that change the person's height.

```


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
```

For long running calls you can use the `AsyncQueryRunner` to execute
the calls asynchronously. The `AsyncQueryRunner` class has the same
methods as the `QueryRunner` calls; however, the methods return a
`Callable`.

```


ExecutorCompletionService<Integer> executor =
    new ExecutorCompletionService<Integer>( Executors.newCachedThreadPool() );
AsyncQueryRunner asyncRun = new AsyncQueryRunner( dataSource );

try
{
    // Create a Callable for the update call
    Callable<Integer> callable = asyncRun.update( "UPDATE Person SET height=? WHERE name=?",
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
```

<a id="examples--resultsethandler-implementations"></a>

## ResultSetHandler Implementations

In the examples above we implemented the `ResultSetHandler` interface
to turn the first row of the `ResultSet` into an Object[]. This is a
fairly generic implementation that can be reused across many projects.
In recognition of this DbUtils provides a set of `ResultSetHandler`
implementations in the
[org.apache.commons.dbutils.handlers](https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/handlers/package-summary.html)
package that perform common transformations into arrays, Maps, and JavaBeans.
There is a version of each implementation that converts just the first row and
another that converts all rows in the `ResultSet`.

We'll start with an example using the `BeanHandler` to fetch one
row from the `ResultSet` and turn it into a JavaBean.

```


QueryRunner run = new QueryRunner(dataSource);

// Use the BeanHandler implementation to convert the first
// ResultSet row into a Person JavaBean.
ResultSetHandler<Person> h = new BeanHandler<Person>(Person.class);

// Execute the SQL statement with one replacement parameter and
// return the results in a new Person object generated by the BeanHandler.
Person p = run.query(
    "SELECT * FROM Person WHERE name=?", h, "John Doe"); 
```

This time we will use the BeanListHandler to fetch all rows from the
`ResultSet` and turn them into a `List` of JavaBeans.

```


QueryRunner run = new QueryRunner(dataSource);

// Use the BeanListHandler implementation to convert all
// ResultSet rows into a List of Person JavaBeans.
ResultSetHandler<List<Person>> h = new BeanListHandler<Person>(Person.class);

// Execute the SQL statement and return the results in a List of
// Person objects generated by the BeanListHandler.
List<Person> persons = run.query("SELECT * FROM Person", h);
```

<a id="examples--custom-rowprocessor"></a>

## Custom RowProcessor

Each of the provided `ResultSetHandler` implementations accept a
[RowProcessor](https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/RowProcessor.html)
to do the actual conversion of rows into objects. By default the handlers
use the [BasicRowProcessor](https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BasicRowProcessor.html)
implementation but you can implement a custom version to plug in.
Probably the most common customization is to implement the `toBean()`
method to handle custom database datatype issues.

<a id="examples--custom-beanprocessor"></a>

## Custom BeanProcessor

`BasicRowProcessor` uses a [BeanProcessor](https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BeanProcessor.html)
to convert `ResultSet` columns into JavaBean properties. You can
subclass and override processing steps to handle datatype mapping specific to
your application. The provided implementation delegates datatype conversion to
the JDBC driver.

BeanProcessor maps columns to bean properties as documented in the
[BeanProcessor.toBean()](https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BeanProcessor.html#toBeanjava.sql.ResultSet20java.lang.Class) javadoc.
Column names must match the bean's property names case insensitively.
For example, the `firstname` column would be stored in the bean
by calling its `setFirstName()` method. However, many database
column names include characters that either can't be used or are not typically
used in Java method names. You can do one of the following to map
these columns to bean properties:

1. Alias the column names in the SQL so they match the Java names:
   `select social_sec# as socialSecurityNumber from person`
2. Subclass BeanProcessor and override the [mapColumnsToProperties()](https://commons.apache.org/proper/commons-dbutils/apidocs/org/apache/commons/dbutils/BeanProcessor.html#mapColumnsToPropertiesjava.sql.ResultSetMetaData20java.beans.PropertyDescriptor)
   method to strip out the offending characters.

---

<a id="changes-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/changes-report.html -->

<!-- page_index: 4 -->

<a id="changes-report--apache-commons-dbutils-release-notes"></a>

## Apache Commons DBUtils Release Notes

<a id="changes-report--release-history"></a>

### Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.8.1](#changes-report--a1.8.1) | 2023-09-09 | New features and bug fixes. |
| [1.8.0](#changes-report--a1.8.0) | 2023-08-01 | New features and bug fixes. |
| [1.7](#changes-report--a1.7) | 2017-07-20 | Bug fixes and separate column & property handlers using SPI |
| [1.6](#changes-report--a1.6) | 2014-07-20 | Bug fixes and addition of insert methods |
| [1.5](#changes-report--a1.5) | 2012-07-20 | Bug fixes and addition of BeanMapHandler |
| [1.4](#changes-report--a1.4) | 2011-10-23 | Bug fixes and addition of asynchronous QueryLoader |
| [1.3](#changes-report--a1.3) | 2009-11-04 | Adds Java5 generics and varargs |
| [1.2](#changes-report--a1.2) | 2009-03-06 | Another round of fixes; deprecates methods in preparation for varargs in java5 |
| [1.1](#changes-report--a1.1) | 2006-12-01 | Last couple of years of fixes |
| [1.0](#changes-report--a1.0) | 2003-11-10 | First release of DbUtils |

<a id="changes-report--a1.8.1"></a>
<a id="changes-report--release-1.8.1-2023-09-09"></a>

### Release 1.8.1 – 2023-09-09

| Type | Changes | By |
| --- | --- | --- |
| Fix | Module org.apache.commons.dbutils does not declare `uses`. Fixes [DBUTILS-151](https://issues.apache.org/jira/browse/DBUTILS-151). Thanks to mark, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump commons-parent from 61 to 62. Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |

<a id="changes-report--a1.8.0"></a>
<a id="changes-report--release-1.8.0-2023-08-01"></a>

### Release 1.8.0 – 2023-08-01

| Type | Changes | By |
| --- | --- | --- |
| Fix | Speedup query calls without parameters; Use PreparedStatement only when parameters are present. Fixes [DBUTILS-131](https://issues.apache.org/jira/browse/DBUTILS-131). Thanks to yairlenga. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Fix | Always copy Date, Time, Timestamp on get and set in SqlNullCheckedResultSet. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Update | BeanProcessor is not thread safe since [DBUTILS-124]. Fixes [DBUTILS-135](https://issues.apache.org/jira/browse/DBUTILS-135). Thanks to hdevalke. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Inefficient allocation of Maps in org.apache.commons.dbutils.BasicRowProcessor.toMap(ResultSet). Fixes [DBUTILS-137](https://issues.apache.org/jira/browse/DBUTILS-137). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | org.apache.commons.dbutils.QueryRunner.query(Connection, boolean, String, ResultSetHandler, Object...) Exception in closing statement leave connections open. Fixes [DBUTILS-138](https://issues.apache.org/jira/browse/DBUTILS-138). Thanks to Stefano Lissa, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | Update Java requirement from version 6 to 8. Fixes [DBUTILS-139](https://issues.apache.org/jira/browse/DBUTILS-139). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | clirr, checkstyle, and spotbugs configured as part of default build. Thanks to thecarlhall. |  |
| Fix | Correction of coverage badge #10. Thanks to Amey Jadiye. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | Manage JDBC objects using try-with-resources. Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | ResultSet not closed in QueryRunner.insert(Connection, String, ResultSetHandler, Object...). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | ResultSet not closed in QueryRunner.insertBatch(Connection, String, ResultSetHandler, Object[][]). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | AbstractQueryRunner.fillStatementWithBean(PreparedStatement, Object, String...) now throws IllegalStateException instead of RuntimeException. Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Add | Add @Column annotation to hint the field name instead of dissecting the get method name. Fixes [PR/9](https://issues.apache.org/jira/browse/PR/9). Thanks to rewerma. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Add | CaseInsensitiveHashMap cannot be accessed by subclasses of BasicRowProcessor; add org.apache.commons.dbutils.BasicRowProcessor.createCaseInsensitiveHashMap(int). Fixes [DBUTILS-136](https://issues.apache.org/jira/browse/DBUTILS-136). Thanks to Matthew Hall, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Add | Add github/codeql-action #115. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Fix | [StepSecurity] ci: Harden GitHub Actions #191. Thanks to step-security-bot, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Add | Add StatementConfiguration.StatementConfiguration(Integer, Integer, Integer, Integer, Duration). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Add | Add StatementConfiguration.getQueryTimeoutDuration(). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Add | Add StatementConfiguration.Builder.queryTimeout(Duration). Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump actions/cache from 2 to 3.0.11 #109, #141, #145. Thanks to Dependabot, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump actions/checkout from 1 to 3.1.10, #44, #23, #48, #75, #93, #143. Thanks to Dependabot, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump actions/setup-java from 1.4.0 to 3.5.1 #40. Thanks to Dependabot, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump actions/upload-artifact from 3.1.0 to 3.1.1 #150. Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump commons-parent from 50 to 61 #14, #113, #139, #168, #189. Thanks to Dependabot. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump junit from 4.12 to 5.9.1 vintage #16, #42, #58. Thanks to Dependabot, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump mockito-core from 3.2.4 to 4.8.1 #18, #21, #46, #53, #97, #103, #111, #116, #122, #131. #137, #151. Thanks to Dependabot. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump spotbugs-maven-plugin from 3.1.12.2 to 4.4.2, #17, #45, #52. Thanks to Dependabot, Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump spotbugs from 3.1.12.2 to 4.2.3. Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.1.0 to 3.2.0 #56, #132. Thanks to Gary Gregory, Dependabot. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump checkstyle from 8.28 to 9.3 #20, #47. Thanks to Gary Gregory, Dependabot. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |
| Update | Bump commons.japicmp.version from 0.14.3 to 0.16.0. Thanks to Gary Gregory. | [ggregory](https://commons.apache.org/proper/commons-dbutils/team-list.html#ggregory) |

<a id="changes-report--a1.7"></a>
<a id="changes-report--release-1.7-2017-07-20"></a>

### Release 1.7 – 2017-07-20

| Type | Changes | By |
| --- | --- | --- |
| Update | Error handling possible getParameterMetaData() results - allow for null return - handle SQLFeatureNotSupportedException. Fixes [DBUTILS-117](https://issues.apache.org/jira/browse/DBUTILS-117). Thanks to Vadim Smirnov. | [sebb](https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb) |
| Update | Correct errors in BeanMapHandler Javadoc. Fixes [DBUTILS-119](https://issues.apache.org/jira/browse/DBUTILS-119). Thanks to Michael Akerman. | [britter](https://commons.apache.org/proper/commons-dbutils/team-list.html#britter) |
| Add | Add getWriteMethod to BeanProcessor to allow subclasses to influence which write method is used. Fixes [DBUTILS-121](https://issues.apache.org/jira/browse/DBUTILS-121). | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Fix | Change method contracts to allow extended class types when returning a bean populated from a query. Fixes [DBUTILS-82](https://issues.apache.org/jira/browse/DBUTILS-82). Thanks to Kenshi Toriumi. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Fix | Add method in BeanProcessor to populate an existing bean. Fixes [DBUTILS-89](https://issues.apache.org/jira/browse/DBUTILS-89). Thanks to Adam Dyga. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Fix | Add ability to configure statements used in QueryRunner. Fixes [DBUTILS-70](https://issues.apache.org/jira/browse/DBUTILS-70). Thanks to Michael Akerman. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Add | Support CallableStatement "out" parameters. Fixes [DBUTILS-50](https://issues.apache.org/jira/browse/DBUTILS-50). Thanks to Dan Fabulich. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Add | Implement column and property handlers using Java's service interfaces. Fixes [DBUTILS-124](https://issues.apache.org/jira/browse/DBUTILS-124). | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |
| Update | Created some Unit Tests to increase code coverage. Fixes [PR/1](https://issues.apache.org/jira/browse/PR/1). Thanks to Michael Hausegger. | [thecarlhall](https://commons.apache.org/proper/commons-dbutils/team-list.html#thecarlhall) |

<a id="changes-report--a1.6"></a>
<a id="changes-report--release-1.6-2014-07-20"></a>

### Release 1.6 – 2014-07-20

| Type | Changes | By |
| --- | --- | --- |
| Fix | ArrayHandler should return an empty array when handle has no rows. Fixes [DBUTILS-110](https://issues.apache.org/jira/browse/DBUTILS-110). | [britter](https://commons.apache.org/proper/commons-dbutils/team-list.html#britter) |
| Fix | Order of columns not retained in BasicRowProcessor with HashMap. Fixes [DBUTILS-114](https://issues.apache.org/jira/browse/DBUTILS-114). Thanks to Michael Osipov. | [britter](https://commons.apache.org/proper/commons-dbutils/team-list.html#britter) |
| Fix | BeanProcessor not returning nanoseconds. Fixes [DBUTILS-118](https://issues.apache.org/jira/browse/DBUTILS-118). Thanks to Feysal Rujbally, Daniele Cremonini. | [britter](https://commons.apache.org/proper/commons-dbutils/team-list.html#britter) |
| Add | Add support for conversion of ResultSet strings to enums in the BeanProcessor. Fixes [DBUTILS-113](https://issues.apache.org/jira/browse/DBUTILS-113). Thanks to Graylin Kim, Michael Osipov. | [britter](https://commons.apache.org/proper/commons-dbutils/team-list.html#britter) |
| Update | In BeanProcessor#isCompatibleType, can Integer.class.isInstance(value) be replaced by value instanceof Integer (etc)? Simplified code by using instanceof. Fixes [DBUTILS-85](https://issues.apache.org/jira/browse/DBUTILS-85). | [sebb](https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb) |
| Fix | DBUtils can't build using JDK 1.7 - DriverProxy needs to implement getParentLogger() Add dynamic invocation. Fixes [DBUTILS-106](https://issues.apache.org/jira/browse/DBUTILS-106). Thanks to Niall Pemberton. | [sebb](https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb) |
| Add | Create functionality to return auto-generated keys in batches of SQL inserts. Fixes [DBUTILS-108](https://issues.apache.org/jira/browse/DBUTILS-108). Thanks to Micah Huff. | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |
| Add | Patch QueryLoader to also load from XML properties files. Fixes [DBUTILS-107](https://issues.apache.org/jira/browse/DBUTILS-107). Thanks to PB. | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |
| Fix | Updated the use of getColumnName to try getColumnLabel first. Fixes [DBUTILS-100](https://issues.apache.org/jira/browse/DBUTILS-100). Thanks to xiaofei.xu. | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |
| Add | Add missing Javadoc to QueryRunner#insert. Fixes [DBUTILS-98](https://issues.apache.org/jira/browse/DBUTILS-98). Thanks to Moandji Ezana. | [simonetripodi](https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi) |
| Add | Add an Abstract ResultSetHandler implementation in order to reduce redundant 'resultSet' variable invocation. Fixes [DBUTILS-97](https://issues.apache.org/jira/browse/DBUTILS-97). | [simonetripodi](https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi) |
| Fix | DbUtils#loadDriver(ClassLoader,String) makes DriverManager throwing "No suitable driver found for jdbc" if ClassLoader is not the System's one. Fixes [DBUTILS-96](https://issues.apache.org/jira/browse/DBUTILS-96). Thanks to yuyf. | [simonetripodi](https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi) |
| Add | Added insert methods to QueryRunner and AsyncQueryRunner that return the generated key. Fixes [DBUTILS-87](https://issues.apache.org/jira/browse/DBUTILS-87). Thanks to Moandji Ezana. | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |

<a id="changes-report--a1.5"></a>
<a id="changes-report--release-1.5-2012-07-20"></a>

### Release 1.5 – 2012-07-20

| Type | Changes | By |
| --- | --- | --- |
| Update | Provide test coverage for org.apache.commons.dbutils.DbUtils. Fixes [DBUTILS-94](https://issues.apache.org/jira/browse/DBUTILS-94). Thanks to Benedikt Ritter. | [simonetripodi](https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi) |
| Fix | Source assembly artifact fails to build a site because of missing pmd-ruleset.xml. Fixes [DBUTILS-93](https://issues.apache.org/jira/browse/DBUTILS-93). Thanks to Stevo Slavic. | [simonetripodi](https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi) |
| Update | Enhance BasicRowProcessor to have row mapping easier to configure. Fixes [DBUTILS-91](https://issues.apache.org/jira/browse/DBUTILS-91). Thanks to Stevo Slavic. | [simonetripodi](https://commons.apache.org/proper/commons-dbutils/team-list.html#simonetripodi) |
| Update | Updated pom.xml: Java 1.6 now required, clirr and compiler plugin removed Thanks to wspeirs. |  |
| Fix | BeanProcessor method processColumn should take SQLXML in consideration. Fixes [DBUTILS-84](https://issues.apache.org/jira/browse/DBUTILS-84). Thanks to Tiago Cavaleiro. | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |
| Update | Updated documentation to better reflect the use of pmdKnownBroken. Fixes [DBUTILS-77](https://issues.apache.org/jira/browse/DBUTILS-77). | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |
| Fix | Added a fixed Locale (Locale.ENGLISH) to all toLowerCase calls in BasicRowProcessor. Fixes [DBUTILS-73](https://issues.apache.org/jira/browse/DBUTILS-73). Thanks to Sebb. |  |
| Add | Added BeanMapHandler. Fixes [DBUTILS-67](https://issues.apache.org/jira/browse/DBUTILS-67). Thanks to Michael Osipov. |  |
| Update | Added generics to ScalarHandler, ColumnHandler, and KeyedHandler. Fixes [DBUTILS-66](https://issues.apache.org/jira/browse/DBUTILS-66). Thanks to Michael Osipov. |  |

<a id="changes-report--a1.4"></a>
<a id="changes-report--release-1.4-2011-10-23"></a>

### Release 1.4 – 2011-10-23

| Type | Changes | By |
| --- | --- | --- |
| Fix | DbUtils.loadDriver() uses Class.forName(). Fixes [DBUTILS-81](https://issues.apache.org/jira/browse/DBUTILS-81). |  |
| Fix | DbUtils.loadDriver catches Throwable. Fixes [DBUTILS-80](https://issues.apache.org/jira/browse/DBUTILS-80). |  |
| Fix | Duplicate code introduced during Java 1.5 branch merge. Fixes [DBUTILS-65](https://issues.apache.org/jira/browse/DBUTILS-65). |  |
| Fix | fillStatement doesn't complain when there are too few parameters. Fixes [DBUTILS-79](https://issues.apache.org/jira/browse/DBUTILS-79). |  |
| Update | efficient usage from findbugs. Fixes [DBUTILS-75](https://issues.apache.org/jira/browse/DBUTILS-75). |  |
| Add | Add asynchronous batch, query, and update calls. Fixes [DBUTILS-78](https://issues.apache.org/jira/browse/DBUTILS-78). | [wspeirs](https://commons.apache.org/proper/commons-dbutils/team-list.html#wspeirs) |

<a id="changes-report--a1.3"></a>
<a id="changes-report--release-1.3-2009-11-04"></a>

### Release 1.3 – 2009-11-04

| Type | Changes | By |
| --- | --- | --- |
| Add | Java 1.5 generics and varargs. Fixes [DBUTILS-48](https://issues.apache.org/jira/browse/DBUTILS-48). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | BeanProcessor#mapColumnsToProperties now prefers to use column labels over column names (where aliases are not set, these should be identical). Fixes [DBUTILS-57](https://issues.apache.org/jira/browse/DBUTILS-57). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | Setting pmdKnownBroken in QueryRunner constructor now completely ignores ParameterMetaData. Fixes [DBUTILS-58](https://issues.apache.org/jira/browse/DBUTILS-58). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Fix | Fixed error message in QueryRunner#rethrow. Fixes [DBUTILS-60](https://issues.apache.org/jira/browse/DBUTILS-60). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |

<a id="changes-report--a1.2"></a>
<a id="changes-report--release-1.2-2009-03-06"></a>

### Release 1.2 – 2009-03-06

| Type | Changes | By |
| --- | --- | --- |
| Update | Removed setDataSource method to guarantee thread safety. Fixes [DBUTILS-52](https://issues.apache.org/jira/browse/DBUTILS-52). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | Made numerous private instance members final to guarantee thread safety; changed protected member of KeyedHandler to final. Fixes [DBUTILS-51](https://issues.apache.org/jira/browse/DBUTILS-51). | [sebb](https://commons.apache.org/proper/commons-dbutils/team-list.html#sebb) |
| Remove | Remove old Maven1/Ant build scripts | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |
| Update | Support bean property to SQL IN parameter mapping. Fixes [DBUTILS-29](https://issues.apache.org/jira/browse/DBUTILS-29). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Fix | fillStatement setNull bug with the Postgres/Derby JDBC driver (and others). Fixes [DBUTILS-31](https://issues.apache.org/jira/browse/DBUTILS-31). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | Make GenericListHandler (now AbstractListHandler) public. Fixes [DBUTILS-33](https://issues.apache.org/jira/browse/DBUTILS-33). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | BasicRowProcessor loses any information on database field case. Fixes [DBUTILS-34](https://issues.apache.org/jira/browse/DBUTILS-34). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | BeanListHandler#handle(ResultSet) is not optimal. Fixes [DBUTILS-37](https://issues.apache.org/jira/browse/DBUTILS-37). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Fix | NullPointerException occurred at rethrow method. Fixes [DBUTILS-40](https://issues.apache.org/jira/browse/DBUTILS-40). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | Object with Long or Decimal got initial zero value while database field is null. Fixes [DBUTILS-42](https://issues.apache.org/jira/browse/DBUTILS-42). | [dfabulich](https://commons.apache.org/proper/commons-dbutils/team-list.html#dfabulich) |
| Update | example documentation page, update query. Fixes [DBUTILS-38](https://issues.apache.org/jira/browse/DBUTILS-38). | [dennisl](https://commons.apache.org/proper/commons-dbutils/team-list.html#dennisl) |
| Fix | Add serialVersionUID to BasicRowProcessor.CaseInsensitiveHashMap. Fixes [DBUTILS-36](https://issues.apache.org/jira/browse/DBUTILS-36). | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |

<a id="changes-report--a1.1"></a>
<a id="changes-report--release-1.1-2006-12-01"></a>

### Release 1.1 – 2006-12-01

| Type | Changes | By |
| --- | --- | --- |
| Fix | Tests fail to build under 1.6, and warning while compiling source. Fixes [DBUTILS-32](https://issues.apache.org/jira/browse/DBUTILS-32). | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |
| Fix | BeanListHandler and BeanHandler fail to support java.sql.Date(). Fixes [DBUTILS-1](https://issues.apache.org/jira/browse/DBUTILS-1). | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |
| Update | ResultSetRowProcessor abstract handler and some classes rework. Fixes [DBUTILS-16](https://issues.apache.org/jira/browse/DBUTILS-16). | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |
| Fix | Setting bean properties fails silently. Fixes [DBUTILS-3](https://issues.apache.org/jira/browse/DBUTILS-3). | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |
| Fix | MockResultSet needs to handle equals and hashCode. Fixes [DBUTILS-9](https://issues.apache.org/jira/browse/DBUTILS-9). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Fix | MockResultSet: Throw UnsupportedOperationException for not implemented methods. Fixes [DBUTILS-7](https://issues.apache.org/jira/browse/DBUTILS-7). | [bayard](https://commons.apache.org/proper/commons-dbutils/team-list.html#bayard) |
| Add | Implement Pluggable Adaptors to Make BeanHandler Smarter. Fixes [DBUTILS-20](https://issues.apache.org/jira/browse/DBUTILS-20). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Patch for extending BasicRowProcessor. Fixes [DBUTILS-15](https://issues.apache.org/jira/browse/DBUTILS-15). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Protected QueryRunner.close() methods. Fixes [DBUTILS-12](https://issues.apache.org/jira/browse/DBUTILS-12). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Updated docs for example.html page (select AS). Fixes [DBUTILS-23](https://issues.apache.org/jira/browse/DBUTILS-23). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Added protected ResultSetIterator.rethrow() method to wrap SQLExceptions in RuntimeExceptions. Fixes [DBUTILS-4](https://issues.apache.org/jira/browse/DBUTILS-4). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Added SQLState and error code to rethrown SQLExceptions. Fixes [DBUTILS-5](https://issues.apache.org/jira/browse/DBUTILS-5). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Added KeyedHandler to create a Map of Maps from a ResultSet. Fixes [DBUTILS-25](https://issues.apache.org/jira/browse/DBUTILS-25). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Use current class' ClassLoader instead of QueryLoader's ClassLoader in loadQueries(). Fixes [DBUTILS-2](https://issues.apache.org/jira/browse/DBUTILS-2). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Made QueryLoader.loadQueries() protected so subclasses can use query repositories other than properties files. Fixes [DBUTILS-22](https://issues.apache.org/jira/browse/DBUTILS-22). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | QueryRunner now calls getDataSource() internally any time it needs access to its DataSource object to allow subclasses to provide different behavior. | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Added DbUtils.rollbackAndClose() and DbUtils.rollbackAndCloseQuietly(). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Call ResultSet.getTimestamp() in BeanProcessor.processColumn() if the bean property is a java.sql.Timestamp. Oracle's getObject() implementation returns its own incompatible Timestamp class. Fixes [DBUTILS-26](https://issues.apache.org/jira/browse/DBUTILS-26). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Update | Changed QueryRunner.fillStatement() null handling to use Types.VARCHAR instead of Types.OTHER. This works for the following tested drivers: Firebird 1.5/firebirdsql 1.5RC3, Oracle 9/ Thin driver, MySQL 4.0/Msql Connecttor 3.0 and mm.mysql 2.0.4 MaxDB 7.5, HSQLDB 1.7.1, and MS Access/ODBC Bridge. Fixes [DBUTILS-18](https://issues.apache.org/jira/browse/DBUTILS-18). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Added a protected QueryRunner.prepareConnection() method to allow subclasses to customize the Connections retrieved from the DataSource before they're used. Fixes [DBUTILS-21](https://issues.apache.org/jira/browse/DBUTILS-21). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Refactored bean handling from BasicRowProcessor into new BeanProcessor class. This also fixes the common problem with Oracle NUMERIC fields not being set into bean properties. | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Added QueryRunner.batch() methods for batch updates. Fixes [DBUTILS-13](https://issues.apache.org/jira/browse/DBUTILS-13). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |
| Add | Added new ResultSetHandler implementation, ColumnListHandler, that converts one ResultSet column into a List of Objects. Fixes [DBUTILS-11](https://issues.apache.org/jira/browse/DBUTILS-11). | [dgraham](https://commons.apache.org/proper/commons-dbutils/team-list.html#dgraham) |

<a id="changes-report--a1.0"></a>
<a id="changes-report--release-1.0-2003-11-10"></a>

### Release 1.0 – 2003-11-10

| Type | Changes | By |
| --- | --- | --- |
| Add | This is the first release of the Commons DbUtils package. DbUtils is a small set of classes designed to make working with JDBC easier. |  |
| Add | QueryRunner class with ResultSetHandler interface allow you to easily query or update a database and handle the ResultSet. Several useful implementations of the ResultSetHandler interface are located in the org.apache.commons.dbutils.handlers.\* package. |  |
| Add | ResultSet wrappers that decorate ResultSets with specialized behavior. See the classes in the org.apache.commons.dbutils.wrappers.\* package for details. |  |
| Add | Dynamic JDBC API interface implementations via the standard java.lang.reflect.Proxy class. This allows you to implement JDBC interfaces such as ResultSet at runtime to avoid API version incompatibilities. See org.apache.commons.dbutils.ProxyFactory for details. |  |

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/issue-tracking.html -->

<!-- page_index: 5 -->

<a id="issue-tracking--apache-commons-dbutils-issue-tracking"></a>

## Apache Commons DbUtils Issue tracking

Apache Commons DbUtils uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons DbUtils JIRA project page](https://issues.apache.org/jira/browse/DBUTILS).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons DbUtils please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310470&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-dbutils/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310470&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310470&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons DbUtils are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons DbUtils bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310470&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons DbUtils bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310470&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons DbUtils bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310470&sorter/field=issuekey&sorter/order=DESC)

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/scm.html -->

<!-- page_index: 6 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-dbutils.git
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone git://git.apache.org/commons-dbutils.git
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-dbutils.git
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/building.html -->

<!-- page_index: 7 -->

<a id="building--overview"></a>

## Overview

Commons DBUtils uses [Maven](http://maven.apache.org) or
[Ant](http://ant.apache.org) as a build system.

<a id="building--maven-goals"></a>

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

<!-- page_index: 8 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons DbUtils package is a set of Java utility classes for easing JDBC development. |
| [Summary](https://commons.apache.org/proper/commons-dbutils/summary.html) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-dbutils/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-dbutils/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependency Information](https://commons.apache.org/proper/commons-dbutils/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-dbutils/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-dbutils/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-dbutils/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-dbutils/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/team.html -->

<!-- page_index: 9 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | baliuka | Juozas Baliuka | [baliuka@apache.org](mailto:baliuka@apache.org) | - | - | - | Java Developer | - |
|  | scaswell | Steven Caswell | [steven@caswell.name](mailto:steven@caswell.name) | - | - | - | Java Developer | - |
|  | dfabulich | Dan Fabulich | [dan@fabulich.com](mailto:dan@fabulich.com) | - | - | - | Java Developer | - |
|  | dgraham | David Graham | [dgraham@apache.org](mailto:dgraham@apache.org) | - | - | - | Java Developer | - |
|  | yoavs | Yoav Shapira | [yoavs@apache.org](mailto:yoavs@apache.org) | - | - | - | Java Developer | - |
|  | wspeirs | William Speirs | [wspeirs@apache.org](mailto:wspeirs@apache.org) | - | - | - | Java Developer | - |
|  | simonetripodi | Simone Tripodi | [simonetripodi at apache dot org](mailto:simonetripodi at apache dot org) | - | - | - | - | - |
|  | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | - | - | Java Developer | - |
|  | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | - | - | Java Developer | - |
|  | thecarlhall | Carl Hall | [thecarlhall@apache.org](mailto:thecarlhall@apache.org) | - | - | - | Java Developer | - |
|  | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Roles |
| --- | --- | --- | --- |
|  | Péter Bagyinszki | - | Java Developer |
|  | Alan Canon | - | Java Developer |
|  | Stefan Fleiter | [stefan.fleiter@web.de](mailto:stefan.fleiter@web.de) | Java Developer |
|  | Adkins Kendall | - | Java Developer |
|  | Markus Khouri | [mkhouri.list@gmail.com](mailto:mkhouri.list@gmail.com) | Documentation |
|  | Uli Kleeberger | [ukleeberger@web.de](mailto:ukleeberger@web.de) | Java Developer |
|  | Piotr Lakomy | [piotrl@cft-inc.net](mailto:piotrl@cft-inc.net) | Java Developer |
|  | Corby Page | - | Java Developer |
|  | Michael Schuerig | [michael@schuerig.de](mailto:michael@schuerig.de) | Java Developer |
|  | Norris Shelton | [norrisshelton@yahoo.com](mailto:norrisshelton@yahoo.com) | Java Developer |
|  | Stevo Slavic | [sslavic at gmail dot com](mailto:sslavic at gmail dot com) | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/project-reports.html -->

<!-- page_index: 11 -->

<a id="project-reports--generated-reports"></a>

## Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](http://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [Changes](#changes-report) | Changes report on releases of this project. |
| [JIRA Report](#jira-report) | Report on Issues from the JIRA Issue Tracking System. |
| [Javadoc](https://commons.apache.org/proper/commons-dbutils/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-dbutils/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-dbutils/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire](#surefire-report) | Report on the test results of the project. |
| [Rat Report](#rat-report) | Report on compliance to license related source code policies |
| [JaCoCo](https://commons.apache.org/proper/commons-dbutils/jacoco/index.html) | JaCoCo Coverage Report. |
| [japicmp](#japicmp) | Comparing source compatibility of commons-dbutils-1.8.1.jar against commons-dbutils-1.8.0.jar |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [SpotBugs](#spotbugs) | Generates a source code report with the SpotBugs Library. |
| [CPD](#cpd) | Duplicate code detection. |
| [PMD](#pmd) | Verification of coding rules. |

---

<a id="jira-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/jira-report.html -->

<!-- page_index: 12 -->

# DbUtils – JIRA Report

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
DOC2MDPLACEHOLDERTOKEN0END<h2><a name="JIRA_Report"></a>JIRA Report</h2>
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

<!-- page_index: 13 -->

<a id="surefire-report--test-cases"></a>

## Test Cases

[[Summary](#surefire-report--summary)] [[Package List](#surefire-report--package_list)] [[Test Cases](#surefire-report--test_cases)]

<a id="surefire-report--queryloadertest"></a>

### QueryLoaderTest

|  |  |  |
| --- | --- | --- |
|  | testLoad | 0.002 s |
|  | testLoadThrowsIllegalArgumentException | 0 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--datepropertyhandlertest"></a>

### DatePropertyHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testNotMatch | 0.001 s |
|  | testMatch | 0 s |
|  | testApplyTypeOfDate | 0.001 s |
|  | testApplyTypeOfTime | 0 s |
|  | testMatchNegative | 0.001 s |
|  | testApplyTypeOfTimestamp | 0.001 s |

<a id="surefire-report--columnlisthandlertest"></a>

### ColumnListHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testColumnNameHandle | 0.002 s |
|  | testColumnIndexHandle | 0.001 s |
|  | testHandle | 0 s |
|  | testEmptyResultSetHandle | 0 s |
|  | testResultSets | 0.001 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--beanlisthandlertest"></a>

### BeanListHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testHandleToInterface | 0.004 s |
|  | testHandleToSuperClass | 0.001 s |
|  | testHandle | 0.003 s |
|  | testEmptyResultSetHandle | 0.001 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--stringtrimmedresultsettest"></a>

### StringTrimmedResultSetTest

|  |  |  |
| --- | --- | --- |
|  | testMultipleWrappers | 0.035 s |
|  | testGetObject | 0.001 s |
|  | testGetString | 0.001 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0.001 s |

<a id="surefire-report--resultsetiteratortest"></a>

### ResultSetIteratorTest

|  |  |  |
| --- | --- | --- |
|  | testNext | 0.006 s |
|  | testCreatesResultSetIteratorTakingThreeArgumentsAndCallsRemove | 0.001 s |
|  | testRethrowThrowsRuntimeException | 0 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--outparametertest"></a>

### OutParameterTest

|  |  |  |
| --- | --- | --- |
|  | testRegister | 0.237 s |
|  | testRegisterAlternateConstructor | 0.001 s |
|  | testSetValue | 0.007 s |

<a id="surefire-report--queryrunnertest"></a>

### QueryRunnerTest

|  |  |  |
| --- | --- | --- |
|  | testNoParamsUpdate | 0.029 s |
|  | testFillStatementWithBean | 0.007 s |
|  | testStatementConfiguration | 0.005 s |
|  | testNullHandlerQuery | 0.019 s |
|  | testNoParamsExecuteWithResultSet | 0.004 s |
|  | testGoodExecute | 0.013 s |
|  | testGoodInsert | 0.004 s |
|  | testGoodExecuteWithResultSetPmdTrue | 0.007 s |
|  | testGoodUpdatePmdTrue | 0.003 s |
|  | testExecuteUpdateException | 0.004 s |
|  | testNoParamsExecute | 0.005 s |
|  | testGoodUpdate | 0.003 s |
|  | testGoodBatchInsert | 0.005 s |
|  | testBadPrepareConnection | 0.002 s |
|  | testFillStatementWithBeanNullNames | 0.009 s |
|  | testGoodQueryPmdTrue | 0.003 s |
|  | testTooManyParamsExecuteWithResultSet | 0.002 s |
|  | testAddBatchExceptionOnAdd | 0.002 s |
|  | testGoodUpdateDefaultConstructor | 0.002 s |
|  | testNullConnectionBatch | 0.002 s |
|  | testNullConnectionQuery | 0.002 s |
|  | testGoodExecutePmdTrue | 0.004 s |
|  | testNullConnectionExecuteWithResultSet | 0.002 s |
|  | testTooManyParamsBatch | 0.002 s |
|  | testNullSqlBatch | 0.002 s |
|  | testTooManyParamsQuery | 0.001 s |
|  | testNullSqlQuery | 0.001 s |
|  | testTooFewParamsBatch | 0.001 s |
|  | testTooFewParamsQuery | 0.002 s |
|  | testNullSqlExecuteWithResultSet | 0.001 s |
|  | testNoParamsQuery | 0.005 s |
|  | testTooManyParamsUpdate | 0.002 s |
|  | testNullParamsArgBatch | 0.002 s |
|  | testExecuteBatchExceptionOnExec | 0.002 s |
|  | testGoodExecuteDefaultConstructor | 0.004 s |
|  | testGoodBatchDefaultConstructor | 0.002 s |
|  | testTooFewParamsExecuteWithResultSet | 0.005 s |
|  | testNullConnectionUpdate | 0.005 s |
|  | testNullSqlUpdate | 0.005 s |
|  | testNullHandlerExecuteWithResultSet | 0.003 s |
|  | testGoodExecuteWithResultSet | 0.008 s |
|  | testExecuteWithMultipleResultSets | 0.003 s |
|  | testNullHandlerExecute | 0.002 s |
|  | testTooManyParamsExecute | 0.001 s |
|  | testTooFewParamsExecute | 0.001 s |
|  | testNullConnectionExecute | 0.001 s |
|  | testExecuteQueryException | 0.002 s |
|  | testExecuteWithResultSetException | 0.002 s |
|  | testTooFewParamsUpdate | 0.001 s |
|  | testNullSqlExecute | 0.001 s |
|  | testGoodExecuteWithResultSetDefaultConstructor | 0.017 s |
|  | testExecuteException | 0.003 s |
|  | testNullParamsBatch | 0.003 s |
|  | testGoodBatch | 0.004 s |
|  | testGoodQueryDefaultConstructor | 0.003 s |
|  | testGoodQuery | 0.003 s |
|  | testGoodBatchPmdTrue | 0.002 s |

<a id="surefire-report--stringcolumnhandlertest"></a>

### StringColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.001 s |
|  | testMatch | 0.001 s |
|  | testMatchNegative | 0 s |

<a id="surefire-report--asyncqueryrunnertest"></a>

### AsyncQueryRunnerTest

|  |  |  |
| --- | --- | --- |
|  | testNoParamsUpdate | 0.234 s |
|  | testNullHandlerQuery | 0.003 s |
|  | testGoodUpdatePmdTrue | 0.008 s |
|  | testExecuteUpdateException | 0.004 s |
|  | testGoodUpdate | 0.012 s |
|  | testBadPrepareConnection | 0.002 s |
|  | testGoodQueryPmdTrue | 0.006 s |
|  | testGoodUpdateDefaultConstructor | 0.003 s |
|  | testNullConnectionBatch | 0.003 s |
|  | testNullConnectionQuery | 0.004 s |
|  | testTooManyParamsBatch | 0.003 s |
|  | testNullSqlBatch | 0.002 s |
|  | testTooManyParamsQuery | 0.004 s |
|  | testNullSqlQuery | 0.002 s |
|  | testAddBatchException | 0.002 s |
|  | testExecuteBatchException | 0.004 s |
|  | testTooFewParamsBatch | 0.003 s |
|  | testTooFewParamsQuery | 0.002 s |
|  | testNoParamsQuery | 0.005 s |
|  | testTooManyParamsUpdate | 0.002 s |
|  | testNullParamsArgBatch | 0.003 s |
|  | testGoodBatchDefaultConstructor | 0.003 s |
|  | testNullConnectionUpdate | 0.001 s |
|  | testNullSqlUpdate | 0.002 s |
|  | testInsertUsesGivenQueryRunner | 0.159 s |
|  | testExecuteQueryException | 0.003 s |
|  | testTooFewParamsUpdate | 0.006 s |
|  | testNullParamsBatch | 0.004 s |
|  | testGoodBatch | 0.004 s |
|  | testGoodQueryDefaultConstructor | 0.003 s |
|  | testGoodQuery | 0.007 s |
|  | testGoodBatchPmdTrue | 0.003 s |

<a id="surefire-report--maplisthandlertest"></a>

### MapListHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testHandle | 0.006 s |
|  | testEmptyResultSetHandle | 0 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0.001 s |

<a id="surefire-report--dbutilstest"></a>

### DbUtilsTest

|  |  |  |
| --- | --- | --- |
|  | closeStatement | 0.008 s |
|  | commitAndClose | 0.002 s |
|  | closeResultSet | 0.001 s |
|  | closeQuietlyNullStatement | 0.001 s |
|  | rollbackQuietly | 0.001 s |
|  | rollbackQuietlyNull | 0 s |
|  | closeQuietlyNullResultSet | 0 s |
|  | closeQuietlyResultSetThrowingException | 0.002 s |
|  | commitAndCloseQuietly | 0.001 s |
|  | closeQuietlyConnectionResultSetStatementThrowingException | 0.001 s |
|  | closeQuietlyStatement | 0.001 s |
|  | rollbackQuietlyWithException | 0.001 s |
|  | closeQuietlyResultSet | 0 s |
|  | rollbackAndClose | 0 s |
|  | closeConnection | 0.003 s |
|  | rollback | 0.002 s |
|  | closeQuietlyStatementThrowingException | 0.001 s |
|  | rollbackAndCloseQuietlyNull | 0 s |
|  | rollbackAndCloseQuietly | 0.001 s |
|  | rollbackNull | 0 s |
|  | testCommitAndCloseQuietlyWithNullDoesNotThrowAnSQLException | 0 s |
|  | rollbackAndCloseQuietlyWithException | 0 s |
|  | testLoadDriverReturnsFalse | 0 s |
|  | closeQuietlyNullConnection | 0.001 s |
|  | closeQuietlyConnection | 0.001 s |
|  | closeQuietlyConnectionThrowingException | 0.001 s |
|  | rollbackAndCloseWithException | 0 s |
|  | closeNullStatement | 0 s |
|  | closeNullConnection | 0.001 s |
|  | commitAndCloseQuietlyWithException | 0.001 s |
|  | rollbackAndCloseNull | 0 s |
|  | closeNullResultSet | 0 s |
|  | closeQuietlyConnectionThrowingExceptionResultSetStatement | 0.002 s |
|  | closeQuietlyConnectionResultSetStatement | 0.001 s |
|  | closeQuietlyConnectionResultSetThrowingExceptionStatement | 0.001 s |
|  | commitAndCloseWithException | 0.002 s |

<a id="surefire-report--sqlxmlcolumnhandlertest"></a>

### SQLXMLColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.034 s |
|  | testMatch | 0.001 s |
|  | testMatchNegative | 0 s |

<a id="surefire-report--statementconfigurationtest"></a>

### StatementConfigurationTest

|  |  |  |
| --- | --- | --- |
|  | testBuilder | 0.029 s |
|  | testEmptyBuilder | 0 s |
|  | testConstructor | 0.001 s |

<a id="surefire-report--dbutilstest-driverproxytest"></a>

### DbUtilsTest$DriverProxyTest

|  |  |  |
| --- | --- | --- |
|  | testProxiedMethods | 0.037 s |

<a id="surefire-report--serviceloadertest"></a>

### ServiceLoaderTest

|  |  |  |
| --- | --- | --- |
|  | testFindMoreThanLocalColumns | 0.001 s |
|  | testFindMoreThanLocalProperties | 0 s |
|  | testFindsLocalPropertyHandler | 0 s |
|  | testFindsLocalColumnHandler | 0.001 s |

<a id="surefire-report--beanmaphandlertest"></a>

### BeanMapHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testEmptyResultSet | 0.033 s |
|  | testBeanMapHandlerClassOfV | 0.002 s |
|  | testBeanMapHandlerClassOfVRowProcessor | 0.002 s |
|  | testBeanMapHandlerClassOfVInt | 0.001 s |
|  | testBeanMapHandlerClassOfVString | 0.002 s |

<a id="surefire-report--beanhandlertest"></a>

### BeanHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testHandleToInterface | 0.004 s |
|  | testHandleToSuperClass | 0 s |
|  | testHandle | 0.001 s |
|  | testEmptyResultSetHandle | 0.001 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0.001 s |

<a id="surefire-report--basicrowprocessortest"></a>

### BasicRowProcessorTest

|  |  |  |
| --- | --- | --- |
|  | testToArray | 0 s |
|  | testToMap | 0.002 s |
|  | testToBeanList | 0.004 s |
|  | testPutAllContainsKeyAndRemove | 0.001 s |
|  | testToMapOrdering | 0.001 s |
|  | testToBean | 0.002 s |
|  | testResultSets | 0.001 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--maphandlertest"></a>

### MapHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testHandle | 0.006 s |
|  | testEmptyResultSetHandle | 0.004 s |
|  | testResultSets | 0.003 s |
|  | testCheckDataSizes | 0.002 s |

<a id="surefire-report--doublecolumnhandlertest"></a>

### DoubleColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.001 s |
|  | testMatch | 0 s |
|  | testMatchNegative | 0 s |

<a id="surefire-report--shortcolumnhandlertest"></a>

### ShortColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.001 s |
|  | testMatch | 0.001 s |
|  | testMatchNegative | 0 s |

<a id="surefire-report--longcolumnhandlertest"></a>

### LongColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0 s |
|  | testMatch | 0.001 s |
|  | testMatchNegative | 0.001 s |

<a id="surefire-report--timestampcolumnhandlertest"></a>

### TimestampColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.001 s |
|  | testMatch | 0 s |
|  | testMatchNegative | 0 s |

<a id="surefire-report--sqlnullcheckedresultsettest"></a>

### SqlNullCheckedResultSetTest

|  |  |  |
| --- | --- | --- |
|  | testSetNullBoolean | 0.009 s |
|  | testGetBytes | 0.001 s |
|  | testGetFloat | 0.004 s |
|  | testGetShort | 0.001 s |
|  | testSetNullBigDecimal | 0 s |
|  | testURL | 0.057 s |
|  | testSetNullBytes | 0.001 s |
|  | testSetNullFloat | 0 s |
|  | testSetNullShort | 0 s |
|  | testSetNullBinaryStream | 0 s |
|  | testSetNullBlob | 0.001 s |
|  | testSetNullByte | 0 s |
|  | testSetNullClob | 0.001 s |
|  | testSetNullDate | 0.001 s |
|  | testSetNullLong | 0.001 s |
|  | testSetNullTime | 0 s |
|  | testGetBlob | 0 s |
|  | testGetByte | 0.001 s |
|  | testGetClob | 0 s |
|  | testGetDate | 0.001 s |
|  | testGetLong | 0.001 s |
|  | testGetTime | 0.001 s |
|  | testSetNullDouble | 0.001 s |
|  | testGetAsciiStream | 0.001 s |
|  | testSetNullObject | 0 s |
|  | testGetCharacterStream | 0.001 s |
|  | testSetNullString | 0.001 s |
|  | testSetNullInt | 0 s |
|  | testSetNullRef | 0 s |
|  | testWrapResultSet | 0.948 s |
|  | testGetBoolean | 0 s |
|  | testSetNullAsciiStream | 0 s |
|  | testGetDouble | 0.001 s |
|  | testGetBigDecimal | 0 s |
|  | testGetTimestamp | 0.001 s |
|  | testGetObject | 0 s |
|  | testSetNullCharacterStream | 0.001 s |
|  | testGetInt | 0 s |
|  | testGetRef | 0 s |
|  | testGetBinaryStream | 0 s |
|  | testGetString | 0 s |
|  | testSetNullTimestamp | 0.001 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--propertyhandlertest"></a>

### PropertyHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testServiceLoaderFindsMultipleRegistries | 0.001 s |
|  | testFoundMoreThanLocal | 0.001 s |

<a id="surefire-report--baseresultsethandlertest"></a>

### BaseResultSetHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--booleancolumnhandlertest"></a>

### BooleanColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.002 s |
|  | testMatch | 0 s |
|  | testMatchNegative | 0.001 s |

<a id="surefire-report--arraylisthandlertest"></a>

### ArrayListHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testHandle | 0.004 s |
|  | testEmptyResultSetHandle | 0 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0.002 s |

<a id="surefire-report--bytecolumnhandlertest"></a>

### ByteColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.003 s |
|  | testMatch | 0.003 s |
|  | testMatchNegative | 0.001 s |

<a id="surefire-report--keyedhandlertest"></a>

### KeyedHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testColumnNameHandle | 0.002 s |
|  | testColumnIndexHandle | 0.001 s |
|  | testHandle | 0.001 s |
|  | testEmptyResultSetHandle | 0 s |
|  | testInjectedRowProcess | 0.013 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0.001 s |

<a id="surefire-report--floatcolumnhandlertest"></a>

### FloatColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0 s |
|  | testMatch | 0.001 s |
|  | testMatchNegative | 0.003 s |

<a id="surefire-report--beanprocessortest"></a>

### BeanProcessorTest

|  |  |  |
| --- | --- | --- |
|  | testMapColumnToProperties | 0.011 s |
|  | testIndexedPropertyDescriptor | 0.004 s |
|  | testProcessWithToBean | 0.005 s |
|  | testWrongSetterParamCount | 0.002 s |
|  | testMapColumnToAnnotationField | 0.002 s |
|  | testProcessWithPopulateBean | 0.001 s |
|  | testMapColumnToPropertiesWithOverrides | 0 s |
|  | testCheckAnnotationOnMissingReadMethod | 0.001 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--scalarhandlertest"></a>

### ScalarHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testColumnNameHandle | 0.001 s |
|  | testColumnIndexHandle | 0.001 s |
|  | testHandle | 0 s |
|  | testEmptyResultSetHandle | 0 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--integercolumnhandlertest"></a>

### IntegerColumnHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testApplyType | 0.003 s |
|  | testMatchNegative | 0.002 s |
|  | testMatch | 0.002 s |

<a id="surefire-report--proxyfactorytest"></a>

### ProxyFactoryTest

|  |  |  |
| --- | --- | --- |
|  | testCreatePreparedStatement | 0.006 s |
|  | testCreateConnection | 0.006 s |
|  | testCreateStatement | 0.004 s |
|  | testCreateResultSet | 0 s |
|  | testCreateCallableStatement | 0.012 s |
|  | testCreateResultSetMetaData | 0 s |
|  | testCreateDriver | 0.002 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--generousbeanprocessortest"></a>

### GenerousBeanProcessorTest

|  |  |  |
| --- | --- | --- |
|  | testMapColumnsToPropertiesWithUnderscores | 0.003 s |
|  | testMapColumnsToPropertiesMixedCase | 0.001 s |
|  | testMapColumnsToPropertiesColumnLabelIsNull | 0.001 s |
|  | testMapColumnsToPropertiesWithSpaces | 0.001 s |
|  | testMapColumnsToPropertiesWithOutUnderscores | 0.001 s |

<a id="surefire-report--arrayhandlertest"></a>

### ArrayHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testHandle | 0.001 s |
|  | testEmptyResultSetHandle | 0.014 s |
|  | testResultSets | 0 s |
|  | testCheckDataSizes | 0 s |

<a id="surefire-report--stringenumpropertyhandlertest"></a>

### StringEnumPropertyHandlerTest

|  |  |  |
| --- | --- | --- |
|  | testMatch | 0 s |
|  | testMatchNegative | 0 s |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/rat-report.html -->

<!-- page_index: 14 -->

# DbUtils – Rat (Release Audit Tool) results

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section>
DOC2MDPLACEHOLDERTOKEN0END<h2><a name="Rat_.28Release_Audit_Tool.29_results"></a>Rat (Release Audit Tool) results</h2>
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

<!-- page_index: 15 -->

<a id="checkstyle--checkstyle-results"></a>

## Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 9.3 with /Users/garydgregory/git/commons-dbutils/src/site/resources/checkstyle/checkstyle.xml ruleset.

<a id="checkstyle--summary"></a>

### Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 55 | 0 | 0 | 14 |

<a id="checkstyle--files"></a>

### Files

| File | I | W | E |
| --- | --- | --- | --- |
| [org/apache/commons/dbutils/AbstractQueryRunner.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fabstractqueryrunner.java) | 0 | 0 | 1 |
| [org/apache/commons/dbutils/BeanProcessor.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fbeanprocessor.java) | 0 | 0 | 2 |
| [org/apache/commons/dbutils/ColumnHandler.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fcolumnhandler.java) | 0 | 0 | 3 |
| [org/apache/commons/dbutils/PropertyHandler.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fpropertyhandler.java) | 0 | 0 | 2 |
| [org/apache/commons/dbutils/QueryRunner.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fqueryrunner.java) | 0 | 0 | 1 |
| [org/apache/commons/dbutils/StatementConfiguration.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fstatementconfiguration.java) | 0 | 0 | 1 |
| [org/apache/commons/dbutils/handlers/KeyedHandler.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fhandlers.2fkeyedhandler.java) | 0 | 0 | 3 |
| [org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.java](#checkstyle--org.2fapache.2fcommons.2fdbutils.2fhandlers.2fproperties.2fdatepropertyhandler.java) | 0 | 0 | 1 |

<a id="checkstyle--details"></a>

### Details

<a id="checkstyle--org-apache-commons-dbutils-abstractqueryrunner.java"></a>

#### org/apache/commons/dbutils/AbstractQueryRunner.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | design | VisibilityModifier | Variable 'ds' must be private and have accessor methods. | [54](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/AbstractQueryRunner.html#L54) |

<a id="checkstyle--org-apache-commons-dbutils-beanprocessor.java"></a>

#### org/apache/commons/dbutils/BeanProcessor.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | sizes | LineLength | Line is longer than 132 characters (found 159). | [143](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/BeanProcessor.html#L143) |
| Error | sizes | LineLength | Line is longer than 132 characters (found 140). | [163](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/BeanProcessor.html#L163) |

<a id="checkstyle--org-apache-commons-dbutils-columnhandler.java"></a>

#### org/apache/commons/dbutils/ColumnHandler.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | sizes | LineLength | Line is longer than 132 characters (found 151). | [23](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/ColumnHandler.html#L23) |
| Error | sizes | LineLength | Line is longer than 132 characters (found 154). | [30](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/ColumnHandler.html#L30) |
| Error | sizes | LineLength | Line is longer than 132 characters (found 142). | [36](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/ColumnHandler.html#L36) |

<a id="checkstyle--org-apache-commons-dbutils-propertyhandler.java"></a>

#### org/apache/commons/dbutils/PropertyHandler.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | sizes | LineLength | Line is longer than 132 characters (found 140). | [20](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/PropertyHandler.html#L20) |
| Error | sizes | LineLength | Line is longer than 132 characters (found 154). | [25](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/PropertyHandler.html#L25) |

<a id="checkstyle--org-apache-commons-dbutils-queryrunner.java"></a>

#### org/apache/commons/dbutils/QueryRunner.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | whitespace | NoWhitespaceAfter | '{' is followed by whitespace. | [748](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/QueryRunner.html#L748) |

<a id="checkstyle--org-apache-commons-dbutils-statementconfiguration.java"></a>

#### org/apache/commons/dbutils/StatementConfiguration.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | sizes | LineLength | Line is longer than 132 characters (found 143). | [130](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/StatementConfiguration.html#L130) |

<a id="checkstyle--org-apache-commons-dbutils-handlers-keyedhandler.java"></a>

#### org/apache/commons/dbutils/handlers/KeyedHandler.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | design | VisibilityModifier | Variable 'convert' must be private and have accessor methods. | [58](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/KeyedHandler.html#L58) |
| Error | design | VisibilityModifier | Variable 'columnIndex' must be private and have accessor methods. | [63](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/KeyedHandler.html#L63) |
| Error | design | VisibilityModifier | Variable 'columnName' must be private and have accessor methods. | [69](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/KeyedHandler.html#L69) |

<a id="checkstyle--org-apache-commons-dbutils-handlers-properties-datepropertyhandler.java"></a>

#### org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.java

| Severity | Category | Rule | Message | Line |
| --- | --- | --- | --- | --- |
| Error | sizes | LineLength | Line is longer than 132 characters (found 156). | [25](https://commons.apache.org/proper/commons-dbutils/xref/org/apache/commons/dbutils/handlers/properties/DatePropertyHandler.html#L25) |

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/spotbugs.html -->

<!-- page_index: 16 -->

<a id="spotbugs--spotbugs-bug-detector-report"></a>

## SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.7.3*

Threshold is

Effort is *default*

<a id="spotbugs--summary"></a>

## Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 56 | 0 | 0 | 0 |

<a id="spotbugs--files"></a>

## Files

| Class | Bugs |
| --- | --- |

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/cpd.html -->

<!-- page_index: 17 -->

<a id="cpd--cpd-results"></a>

## CPD Results

The following document contains the results of PMD's [CPD](https://pmd.github.io/latest/pmd_userdocs_cpd.html) 6.55.0.

CPD found no problems in your source code.

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/pmd.html -->

<!-- page_index: 18 -->

<a id="pmd--pmd-results"></a>

## PMD Results

The following document contains the results of [PMD](https://pmd.github.io) 6.55.0.

PMD found no problems in your source code.

---
