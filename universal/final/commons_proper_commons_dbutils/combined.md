# DbUtils – Project Information

## Navigation

- DbUtils
  - [Overview](#index)
  - [Examples](#examples)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Source Repository](#scm)
  - [Building](#building)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/index.html -->

<!-- page_index: 1 -->

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

<!-- page_index: 2 -->

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

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/issue-tracking.html -->

<!-- page_index: 3 -->

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

<!-- page_index: 4 -->

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

<!-- page_index: 5 -->

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

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons DbUtils package is a set of Java utility classes for easing JDBC development. |
| [Summary](#summary) | This document lists other related information of this project |
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

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/summary.html -->

<!-- page_index: 7 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons DbUtils |
| Description | The Apache Commons DbUtils package is a set of Java utility classes for easing JDBC development. |
| Homepage | [https://commons.apache.org/proper/commons-dbutils/](#index) |

<a id="summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | commons-dbutils |
| ArtifactId | commons-dbutils |
| Version | 1.8.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/team.html -->

<!-- page_index: 8 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/2bcb82403b87c2c4cba0fe6a5edb4c20?d=mm&s=60) | baliuka | Juozas Baliuka | [baliuka@apache.org](mailto:baliuka@apache.org) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/e5fb9b8bba7ccd5fc0c8b86ac83ce4b5?d=mm&s=60) | scaswell | Steven Caswell | [steven@caswell.name](mailto:steven@caswell.name) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/0ded147122e1c318a63340568904762b?d=mm&s=60) | dfabulich | Dan Fabulich | [dan@fabulich.com](mailto:dan@fabulich.com) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/3797c8c3332e7ccd80273f7eac7c2949?d=mm&s=60) | dgraham | David Graham | [dgraham@apache.org](mailto:dgraham@apache.org) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/248341e80da66f10c0d6af27f40c8d63?d=mm&s=60) | yoavs | Yoav Shapira | [yoavs@apache.org](mailto:yoavs@apache.org) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/910b15b19b44768cbeefc884cd2d6460?d=mm&s=60) | wspeirs | William Speirs | [wspeirs@apache.org](mailto:wspeirs@apache.org) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/a23637cb700caf1c78d93cd5212418c9?d=mm&s=60) | simonetripodi | Simone Tripodi | [simonetripodi at apache dot org](mailto:simonetripodi at apache dot org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/4156866f23b66d5ca7df5cdc86cb9a0e?d=mm&s=60) | bayard | Henri Yandell | [bayard@apache.org](mailto:bayard@apache.org) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/cbfb61ee7f8641b2b6eaf22fed163b1e?d=mm&s=60) | britter | Benedikt Ritter | [britter@apache.org](mailto:britter@apache.org) | - | - | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/487c829cb2071c62b09770a987986ce2?d=mm&s=60) | thecarlhall | Carl Hall | [thecarlhall@apache.org](mailto:thecarlhall@apache.org) | - | - | - | Java Developer | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Roles |
| --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Péter Bagyinszki | - | Java Developer |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Alan Canon | - | Java Developer |
| ![](https://www.gravatar.com/avatar/ccad3c663dffd81a6a3e54b246966629?d=mm&s=60) | Stefan Fleiter | [stefan.fleiter@web.de](mailto:stefan.fleiter@web.de) | Java Developer |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Adkins Kendall | - | Java Developer |
| ![](https://www.gravatar.com/avatar/428b2f330c1eb3274deeff27864da9bb?d=mm&s=60) | Markus Khouri | [mkhouri.list@gmail.com](mailto:mkhouri.list@gmail.com) | Documentation |
| ![](https://www.gravatar.com/avatar/5e48bb1bdf7dd9b5bd909ce270a21206?d=mm&s=60) | Uli Kleeberger | [ukleeberger@web.de](mailto:ukleeberger@web.de) | Java Developer |
| ![](https://www.gravatar.com/avatar/c2771fe987234ec0a6c5bc18809adb75?d=mm&s=60) | Piotr Lakomy | [piotrl@cft-inc.net](mailto:piotrl@cft-inc.net) | Java Developer |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Corby Page | - | Java Developer |
| ![](https://www.gravatar.com/avatar/bce1d1b7c3ec7b577dcb42e254899e6b?d=mm&s=60) | Michael Schuerig | [michael@schuerig.de](mailto:michael@schuerig.de) | Java Developer |
| ![](https://www.gravatar.com/avatar/e9b6b3a115dcb64e45711f40de87116c?d=mm&s=60) | Norris Shelton | [norrisshelton@yahoo.com](mailto:norrisshelton@yahoo.com) | Java Developer |
| ![](https://www.gravatar.com/avatar/d3c1de0c1f733d6aa98d77f508be3ac5?d=mm&s=60) | Stevo Slavic | [sslavic at gmail dot com](mailto:sslavic at gmail dot com) | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-dbutils/ci-management.html -->

<!-- page_index: 9 -->

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
