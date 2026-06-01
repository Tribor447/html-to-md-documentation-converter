# Project Information

## Navigation

- Statistics
  - [Overview](#index)
  - [Issue Tracking](#issue-tracking)
  - [Developers Guide](#developers)
  - [Release History](#release-history)
- User Guide
  - [Contents](#userguide--toc)
  - [Overview](#userguide--overview)
  - [Example Modules](#userguide--example-modules)
  - [Descriptive](#userguide--descriptive)
  - [Probability Distributions](#userguide--distributions)
  - [Inference](#userguide--inference)
  - [Ranking](#userguide--ranking)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Project Modules](#modules)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Statistics Documentation
  - [Overview](#commons-statistics-docs)
- Statistics Bill of Materials
  - [Overview](#commons-statistics-bom)
- Statistics Interval
  - [Overview](#commons-statistics-interval)
- Statistics Ranking
  - [Overview](#commons-statistics-ranking)
- Statistics Inference
  - [Overview](#commons-statistics-inference)
- Statistics Descriptive
  - [Overview](#commons-statistics-descriptive)
- Statistics Distribution
  - [Overview](#commons-statistics-distribution)
- Other pages
  - [Overview](#commons-statistics-bom-ci-management)
  - [Overview](#commons-statistics-bom-scm)
  - [Project Summary](#commons-statistics-bom-summary)
  - [Project Team](#commons-statistics-bom-team)
  - [Overview](#commons-statistics-descriptive-ci-management)
  - [Overview](#commons-statistics-descriptive-scm)
  - [Project Summary](#commons-statistics-descriptive-summary)
  - [Project Team](#commons-statistics-descriptive-team)
  - [Overview](#commons-statistics-distribution-ci-management)
  - [Overview](#commons-statistics-distribution-scm)
  - [Project Summary](#commons-statistics-distribution-summary)
  - [Project Team](#commons-statistics-distribution-team)
  - [Overview](#commons-statistics-docs-ci-management)
  - [Overview](#commons-statistics-docs-scm)
  - [Project Summary](#commons-statistics-docs-summary)
  - [Project Team](#commons-statistics-docs-team)
  - [Overview](#commons-statistics-examples-ci-management)
  - [About Apache Commons Statistics Examples](#commons-statistics-examples)
  - [Project Modules](#commons-statistics-examples-modules)
  - [Overview](#commons-statistics-examples-scm)
  - [Project Summary](#commons-statistics-examples-summary)
  - [Project Team](#commons-statistics-examples-team)
  - [Overview](#commons-statistics-inference-ci-management)
  - [Overview](#commons-statistics-inference-scm)
  - [Project Summary](#commons-statistics-inference-summary)
  - [Project Team](#commons-statistics-inference-team)
  - [Overview](#commons-statistics-interval-ci-management)
  - [Overview](#commons-statistics-interval-scm)
  - [Project Summary](#commons-statistics-interval-summary)
  - [Project Team](#commons-statistics-interval-team)
  - [Overview](#commons-statistics-ranking-ci-management)
  - [Overview](#commons-statistics-ranking-scm)
  - [Project Summary](#commons-statistics-ranking-summary)
  - [Project Team](#commons-statistics-ranking-team)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-statistics"></a>

# Apache Commons Statistics

Apache Commons Statistics provides utilities for statistical applications.

Descriptive statistics can be computed on array data or using the Java Stream API, for example:

```

int[] values = {1, 1, 2, 3, 5, 8, 13, 21};
double v = IntVariance.of(values).getAsDouble();   // 49.929

// A builder for specified statistics to allow
// parallel computation on a stream of values
IntStatistics.Builder builder = IntStatistics.builder(
    Statistic.MIN, Statistic.MAX, Statistic.MEAN);
IntStatistics stats =
    Stream.of("one", "two", "three", "four")
    .parallel()
    .mapToInt(String::length)
    .collect(builder::build, IntConsumer::accept, IntStatistics::combine);

stats.getAsInt(Statistic.MIN);       // 3
stats.getAsInt(Statistic.MAX);       // 5
stats.getAsDouble(Statistic.MEAN);   // 15.0 / 4
```

Support is provided for commonly used continuous and discrete distributions, for example:

```

TDistribution t = TDistribution.of(29);
double lowerTail = t.cumulativeProbability(-2.656);   // P(T(29) <= -2.656)
double upperTail = t.survivalProbability(2.75);       // P(T(29) > 2.75)

PoissonDistribution p = PoissonDistribution.of(4.56);
int x = p.inverseCumulativeProbability(0.99);
```

Hypothesis testing can be performed for various statistical tests, for example:

```

double[] math    = {53, 69, 65, 65, 67, 79, 86, 65, 62, 69};   // mean = 68.0
double[] science = {75, 65, 68, 63, 55, 65, 73, 45, 51, 52};   // mean = 61.2

SignificanceResult result = TTest.withDefaults()
                                 .with(AlternativeHypothesis.GREATER_THAN)
                                 .pairedTest(math, science);
result.getPValue();    // 0.05764
result.reject(0.05);   // false
```

For more examples and advanced usage, see the [user guide](#userguide).

<a id="index--download-apache-commons-statistics"></a>

# Download Apache Commons Statistics

<a id="index--releases"></a>

## Releases

Download the
[latest release](https://commons.apache.org/statistics/download_statistics.cgi) of Apache Commons Statistics.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/issue-tracking.html -->

<!-- page_index: 2 -->

<a id="issue-tracking--apache-commons-statistics-issue-tracking"></a>

# Apache Commons Statistics Issue tracking

Apache Commons Statistics uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Statistics JIRA project page](https://issues.apache.org/jira/browse/STATISTICS).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Statistics please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12321632&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-statistics/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12321632&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12321632&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Statistics are all unpaid volunteers

For more information on git and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Statistics bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12321632&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Statistics bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12321632&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Statistics bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12321632&sorter/field=issuekey&sorter/order=DESC)

---

<a id="developers"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/developers.html -->

<!-- page_index: 3 -->

<a id="developers--aims"></a>

# Aims

Maintenance of a library by decentralized team requires communication.
It is important that developers follow guidelines laid down by the community
to ensure that the code they create can be successfully maintained by others.

<a id="developers--guidelines"></a>

# Guidelines

Developers are asked to comply with the following development guidelines.
Code that does not comply with the guidelines including the word *must*
will not be committed. Our aim will be to fix all of the exceptions to the
"*should*" guidelines prior to a release.

<a id="developers--contributing"></a>

## Contributing

**Getting Started**

1. Download the Commons Statistics source code. Follow the instructions
   under the heading "Repository Checkout" on the
   [Git at the ASF page](https://gitbox.apache.org/).
   The git url for the current development sources of Commons Statistics
   is

```
http://gitbox.apache.org/repos/asf/commons-statistics.git
```

   for anonymous read-only access and

```
https://apacheid@gitbox.apache.org/repos/asf/commons-statistics.git
```

   (where apacheid should be replaced by each committer Apache ID) for committers
   read-write access.
2. Like most commons components, Commons Statistics uses Apache Maven as our
   build tool.
   To build Commons Statistics using Maven, you can follow the instructions for
   [Building a
   project with Maven](https://maven.apache.org/run-maven/index.html).
   Launch Maven from the top-level directory
   in the checkout of Commons Statistics trunk. No special setup is required,
   except that currently to build the site (i.e. to execute Maven's
   "site" goal), you may need to increase the default memory allocation
   (e.g. `export MAVEN_OPTS=-Xmx512m`) before launching
   Maven.
3. Be sure to join the commons-dev and commons-user
   [email lists](https://commons.apache.org/proper/commons-statistics/mail-lists.html) and use them appropriately (make sure the string
   "[Statistics]" starts the Subject line of all your postings).
   Make any proposals here where the group can comment on them.
4. [Setup an account on JIRA](https://issues.apache.org/jira/secure/Signup!default.jspa)
   and use it to submit patches and
   identify bugs. Read the
   [directions](https://issues.apache.org/bugwritinghelp.html)
   for submitting bugs and search the database to
   determine if an issue exists or has already been dealt with.
   See the [Commons Statistics Issue Tracking Page](https://commons.apache.org/statistics/issue-tracking.html)
   for more information on how to
   search for or submit bugs or enhancement requests.
5. Generating patches: The requested format for generating patches is
   the Unified Diff format, which can be easily generated using the git
   client or various IDEs.

```
git diff -p > patch 
```

   Run this command from the top-level project directory (where pom.xml
   resides).
6. Pull Requests: We accept pull requests (PRs) via the GitHub repository mirror.
   The Commons Statistics repository can be forked and changes merged via a PR.
   See [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) for more information on pull requests.

**Contributing ideas and code**

Follow the steps below when making suggestions for additions or
enhancements to Commons Statistics. This will make it easier for the community
to comment on your ideas and for the committers to keep track of them.
Thanks in advance!

1. Start with a post to the commons-dev mailing list, with [Statistics] at
   the beginning of the subject line, followed by a short title
   describing the new feature or enhancement; for example, "[Statistics]
   New univariate distribution".
   The body of the post should include each of the following items
   (but be **as brief as possible**):
   - A concise description of the new feature / enhancement
   - References to definitions and algorithms. Using standard
     definitions and algorithms makes communication much easier and will
     greatly increase the chances that we will accept the code / idea
   - Some indication of why the addition / enhancement is practically
     useful
2. Assuming a generally favorable response to the idea on commons-dev,
   the next step is to file a report on the issue-tracking system (JIRA).
   Create a JIRA ticket using the feature title as the short
   description. Incorporate feedback from the initial posting in the
   description. Add a reference to the discussion thread.
3. Submit code as:
   - Attachments to the JIRA ticket. Please use one
     ticket for each feature, adding multiple patches to the ticket
     as necessary. Use the git diff command to generate your patches as
     diffs. Please do not submit modified copies of existing java files.
   - A pull request (PR) via GitHub.
     To link the PR to a corresponding JIRA ticket prefix the PR title with
     `STATISTICS-xxx:` where `xxx` is the issue number.
     Please include quality commit messages with a single line title of about 50
     characters, followed by a blank line, followed by a more detailed explanation
     of the changeset. The title should be prefixed with the JIRA ticket number if
     applicable, e.g. `STATISTICS-xxx: New univariate distribution`.
     See [contributing to a project](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) in the git book for guidelines on commit messages.Be patient (but not **too** patient) with committers reviewing
   patches/PRs. Post a \*nudge\* message to commons-dev with a reference to the
   ticket if a submission goes more than a few days with no comment or commit.

<a id="developers--coding-style"></a>

## Coding Style

Commons Statistics follows [Code Conventions for the Java Programming Language (circa 1999)](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html). As part of the maven
build process, style checking is performed using the Checkstyle plugin, using the properties specified in `checkstyle.xml`. This is based on
the default [sun checks](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/sun_checks.xml) defined by the Checkstyle plugin using current Java best practices.
Committed code *should* generate no Checkstyle errors. One thing
that Checkstyle will complain about is tabs included in the source code.
Please make sure to set your IDE or editor to use spaces instead of tabs.

Committers should configure the `user.name` and `user.email`
git repository or global settings with `git config`.
These settings define the identity and mail of the committer. See [Customizing
Git - Git Configuration](https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration) in the git book for an explanation about how to
configure these settings and more.

<a id="developers--documentation"></a>

## Documentation

- Committed code *must* include full javadoc.
- All component contracts *must* be fully specified in the javadoc class,
  interface or method comments, including specification of acceptable ranges
  of values, exceptions or special return values.
- External references or full statements of definitions for all the
  terms used in component documentation *must* be provided.
- Commons Statistics javadoc generation supports embedded LaTeX formulas via the
  [MathJax](https://www.mathjax.org) javascript display engine.
  To embed mathematical expressions formatted in LaTeX in javadoc, simply surround
  the expression to be formatted with either `\(` and `\)`
  for inline formulas (or `\[` and `\]` to have the formula
  appear on a separate line).
  For example,
  `\(``a^2 + b^2 = c^2``\)`
  will render an in-line formula
  saying that (a, b, c) is a Pythagorean triplet: \( a^2 + b^2 = c^2 \).
  See the MathJax and LaTex documentation for details on how to represent formulas
  and escape special characters.
- Implementations *should* use standard algorithms and
  references or full descriptions of all algorithms *should* be
  provided.
- Additions and enhancements *should* include updates to the User
  Guide.

<a id="developers--exceptions"></a>

## Exceptions

- Exceptions generated by Commons Statistics are all unchecked.
- All public methods advertise all exceptions that they can generate.
  Exceptions *must* be documented in Javadoc and the documentation
  *must* include full description of the conditions under which
  exceptions are thrown.

<a id="developers--unit-tests"></a>

## Unit Tests

- Committed code *must* include unit tests.
- Unit tests *should* provide full path coverage.
- Unit tests *should* verify all boundary conditions specified in
  interface contracts, including verification that exceptions are thrown or
  special values (e.g. Double.NaN, Double.Infinity) are returned as
  expected.

<a id="developers--licensing-and-copyright"></a>

## Licensing and copyright

- All new source file submissions *must* include the Apache Software
  License in a comment that begins the file.
- All contributions must comply with the terms of the Apache
  [Contributor License Agreement (CLA)](https://www.apache.org/licenses/contributor-agreements.html#clas).
- Patches *must* be accompanied by a clear reference to a "source"
  - if code has been "ported" from another language, clearly state the
  source of the original implementation. If the "expression" of a given
  algorithm is derivative, please note the original source (textbook,
  paper, etc.).
- References to source materials covered by restrictive proprietary
  licenses should be avoided. In particular, contributions should not
  implement or include references to algorithms in
  [Numerical Recipes (NR)](http://numerical.recipes/).
  Any questions about copyright or patent issues should be raised on
  the commons-dev mailing list before contributing or committing code.

---

<a id="release-history"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/release-history.html -->

<!-- page_index: 4 -->

<a id="release-history--commons-statistics-release-history"></a>

# Commons Statistics Release History

*Note.* For older release javadocs see the individual artifact sub-sites.

| Version | Release date (YYYY-MM-DD) | Required Java Version | Release notes |
| --- | --- | --- | --- |
| 1.3 | 2026-05-01 | 8+ | [Release notes for 1.3](assets/files/release-notes-1-3_1363961532ba6ba2.txt) |
| 1.2 | 2025-09-17 | 8+ | [Release notes for 1.2](assets/files/release-notes-1-2_87f9f8abb53c6010.txt) |
| 1.1 | 2024-08-20 | 8+ | [Release notes for 1.1](assets/files/release-notes-1-1_dbdeb885d23732ce.txt) |
| 1.0 | 2022-12-05 | 8+ | [Release notes for 1.0](assets/files/release-notes-1-0_5290a42ddd863965.txt) |

---

<a id="userguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/userguide/index.html -->

<!-- page_index: 5 -->

#

<a id="userguide--apache-commons-statistics-user-guide"></a>

# Apache Commons Statistics User Guide

<a id="userguide--overview"></a>

# Overview

Apache Commons Statistics provides utilities for statistical applications. The code
originated in the `commons-math` project but was pulled out into a separate project for better
maintainability and has since undergone numerous improvements.

Commons Statistics is divided into a number of submodules:

- `commons-statistics-descriptive` - Provides computation
  of descriptive statistics (mean, variance, median, etc).
- `commons-statistics-distribution` - Provides interfaces
  and classes for probability distributions.
- `commons-statistics-inference` - Provides hypothesis testing.
- `commons-statistics-interval` - Provides statistical intervals.
- `commons-statistics-ranking` - Provides rank transformations.

<a id="userguide--example-modules"></a>

# Example Modules

In addition to the modules above, the Commons Statistics
[source distribution](https://commons.apache.org/statistics/download_statistics.cgi)
contains example code demonstrating library functionality and/or providing useful
development utilities. These modules are not part of the public API of the library and no
guarantees are made concerning backwards compatibility. The
[example module parent page](#commons-statistics-examples-modules)
contains a listing of available modules.

---

<a id="userguide--descriptive-statistics"></a>

# Descriptive Statistics

The `commons-statistics-descriptive` module provides descriptive statistics.

<a id="userguide--overview-2"></a>

## Overview

The module provides classes to compute univariate statistics on `double`, `int` and `long` data using array input or a Java stream. The
result is returned as a
[StatisticResult](https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/apidocs/org/apache/commons/statistics/descriptive/StatisticResult.html).
The `StatisticResult` provides methods to supply the result as a
`double`, `int`, `long` and `BigInteger`.
The integer types allow the exact result to be returned for integer data. For example
the sum of `long` values may not be exactly representable as a
`double` and may overflow a `long`.

Computation of an individual statistic involves creating an instance of
`StatisticResult` that can supply the current statistic value.
To allow addition of single values to update the statistic, instances
implement the primitive consumer interface for the supported type:
`DoubleConsumer`, `IntConsumer`, or `LongConsumer`.
Instances implement the
[StatisticAccumulator](https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/apidocs/org/apache/commons/statistics/descriptive/StatisticAccumulator.html)
interface and can be combined with other instances. This allows computation in parallel on
subsets of data and combination to a final result. This can be performed using the
Java stream API.

Computation of multiple statistics uses a
[Statistic](https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/apidocs/org/apache/commons/statistics/descriptive/Statistic.html)
enumeration to define the statistics to evaluate. A container class is created to
compute the desired statistics together and allows multiple statistics to be computed
concurrently using the Java stream API. Each statistic result is obtained using the
`Statistic` enum to access the required value. Providing a choice of the
statistics allows the user to avoid the computational cost of results that are not
required.

Note that `double` computations are subject to accumulated floating-point
rounding which can generate different results from permuted input data. Computation
on an array of `double` data can use a multiple-pass algorithm to increase
accuracy over a single-pass stream of values. This is the recommended approach if
all data is already stored in an array (i.e. is not dynamically generated).

If the data is an integer type then it is
preferred to use the integer specializations of the statistics.
Many implementations use exact integer math for the computation. This is faster than
using a `double` data type, more accurate and returns the same result
irrespective of the input order of the data. Note that for improved performance there
is no use of `BigInteger` in the accumulation of intermediate values; the
computation uses mutable fixed-precision integer classes for totals that may
overflow 64-bits.

Some statistics cannot be computed using a stream since they require all values for
computation, for example the median. These are evaluated on an array using an instance
of a computing class. The instance allows computation options to be changed. Instances
are immutable and the computation is thread-safe.

<a id="userguide--examples"></a>

## Examples

Computation of a single statistic from an array of values, an array range or a
stream of data:

```

int[] values = {1, 1, 2, 3, 5, 8, 13, 21};

double v = IntVariance.of(values).getAsDouble();

// Range uses inclusive start and exclusive end
int max = IntMax.ofRange(values, 3, 6).getAsInt();   // 8

double m = Stream.of("one", "two", "three", "four")
                 .mapToInt(String::length)
                 .collect(IntMean::create, IntMean::accept, IntMean::combine)
                 .getAsDouble();
```

Computation of multiple statistics uses the `Statistic` enum.
These can be specified using an `EnumSet` together with the input array data.
Note that some statistics share the same underlying computation, for example the variance, standard deviation and mean. When a container class is constructed using one of the
statistics, the other co-computed statistics are available in the result even if not
specified during construction. The `isSupported` method can
identify all results that are available from the container class.

```

double[] data = {1, 2, 3, 4, 5, 6, 7, 8};
DoubleStatistics stats = DoubleStatistics.of(
    EnumSet.of(Statistic.MIN, Statistic.MAX, Statistic.VARIANCE),
    data);

stats.getAsDouble(Statistic.MIN);        // 1.0
stats.getAsDouble(Statistic.MAX);        // 8.0
stats.getAsDouble(Statistic.VARIANCE);   // 6.0

// Get other statistics supported by the underlying computations
stats.isSupported(Statistic.STANDARD_DEVIATION));   // true
stats.getAsDouble(Statistic.STANDARD_DEVIATION);    // 2.449...
```

Computation of multiple statistics on individual values can accumulate the results
using the `accept` method of the container class:

```

IntStatistics stats = IntStatistics.of(
    Statistic.MIN, Statistic.MAX, Statistic.MEAN);
Stream.of("one", "two", "three", "four")
    .mapToInt(String::length)
    .forEach(stats::accept);

stats.getAsInt(Statistic.MIN);       // 3
stats.getAsInt(Statistic.MAX);       // 5
stats.getAsDouble(Statistic.MEAN);   // 15.0 / 4
```

Computation of multiple statistics on a stream of values in parallel.
This requires use of a `Builder` that
can supply instances of the container class to each worker with the
`build` method. These are populated using `accept` and then
collected using `combine`:

```

IntStatistics.Builder builder = IntStatistics.builder(
    Statistic.MIN, Statistic.MAX, Statistic.MEAN);
IntStatistics stats =
    Stream.of("one", "two", "three", "four")
    .parallel()
    .mapToInt(String::length)
    .collect(builder::build, IntConsumer::accept, IntStatistics::combine);

stats.getAsInt(Statistic.MIN);       // 3
stats.getAsInt(Statistic.MAX);       // 5
stats.getAsDouble(Statistic.MEAN);   // 15.0 / 4
```

Computation on multiple arrays. This requires use of a `Builder` that
can supply instances of the container class to compute each array with the
`build` method:

```

double[][] data = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
};
DoubleStatistics.Builder builder = DoubleStatistics.builder(
    Statistic.MIN, Statistic.MAX, Statistic.VARIANCE);
DoubleStatistics stats = Arrays.stream(data)
    .map(builder::build)
    .reduce(DoubleStatistics::combine)
    .get();

stats.getAsDouble(Statistic.MIN);        // 1.0
stats.getAsDouble(Statistic.MAX);        // 8.0
stats.getAsDouble(Statistic.VARIANCE);   // 6.0

// Get other statistics supported by the underlying computations
stats.isSupported(Statistic.MEAN));   // true
stats.getAsDouble(Statistic.MEAN);    // 4.5
```

If computation on multiple arrays is to be repeated then this can be done with a
re-useable `java.util.stream.Collector`:

```

double[][] data = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
};
DoubleStatistics.Builder builder = DoubleStatistics.builder(
    Statistic.MIN, Statistic.MAX, Statistic.VARIANCE);
Collector<double[], DoubleStatistics, DoubleStatistics> collector =
    Collector.of(builder::build, (s, d) -> s.combine(builder.build(d)), DoubleStatistics::combine);
DoubleStatistics stats = Arrays.stream(data).collect(collector);

stats.getAsDouble(Statistic.MIN);        // 1.0
stats.getAsDouble(Statistic.MAX);        // 8.0
stats.getAsDouble(Statistic.VARIANCE);   // 6.0
```

Combination of multiple statistics requires them to be compatible, i.e. all supported
statistics in one container are also supported in the other. Note that combining another
container ignores any unsupported statistics and the compatibility
may be asymmetric.

```

double[] data1 = {1, 2, 3, 4};
double[] data2 = {5, 6, 7, 8};
DoubleStatistics varStats = DoubleStatistics.builder(Statistic.VARIANCE).build(data1);
DoubleStatistics meanStats = DoubleStatistics.builder(Statistic.MEAN).build(data2);

// throws IllegalArgumentException
varStats.combine(meanStats);

// OK - mean is updated to 4.5
meanStats.combine(varStats)
```

Computation of a statistic that requires all data (i.e. does not support the
`Stream` API) uses a configurable instance of the computing class:

```

double[] data = {8, 7, 6, 5, 4, 3, 2, 1};
// Configure the statistic
double m = Median.withDefaults()
                 .withCopy(true)          // do not modify the input array
                 .with(NaNPolicy.ERROR)   // raise an exception for NaN
                 .evaluate(data);
// m = 4.5
```

Computation of multiple values of a statistic that requires all data:

```

int size = 10000;
double origin = 0;
double bound = 100;
double[] data =
    new SplittableRandom(123)
    .doubles(size, origin, bound)
    .toArray();
// Evaluate multiple statistics on the same data
double[] q = Quantile.withDefaults()
                     .evaluate(data, 0.25, 0.5, 0.75);   // probabilities
// q ~ [25.0, 50.0, 75.0]
```

Computation of quantiles requires partial sorting of array data.
Quantile support for pre-sorted numeric data of type `double` or
`long` uses the interfaces `IntToDoubleFunction` and
`IntToLongFunction` to specify the value at each position in the sorted data.
This allows computation on numeric types such as `short` or `float`
not supported by the array computation methods.

```

int size = 10000;
int exclusiveBound = 101;
short[] data = new short[size];
SplittableRandom rng = new SplittableRandom(123);
for (int i = 0; i < size; i++) {
    data[i] = (short) rng.nextInt(exclusiveBound);
}
// Sorted data
Arrays.sort(data);
double[] q = Quantile.withDefaults()
                     .evaluate(size, i -> data[i], 0.25, 0.5, 0.75);
// q ~ [25.0, 50.0, 75.0]
```

Note it is not recommended to sort supported array types
**only** for use in the quantile evaluation.
However if the data must be sorted for other reasons, or is already sorted, then these
methods can be used on supported array data to compute
the same result without the cost of partial re-sorting of sorted data.

<a id="userguide--probability-distributions"></a>

# Probability Distributions

<a id="userguide--overview-3"></a>

## Overview

The `commons-statistics-distribution` module provides a framework and implementations for some commonly used
probability distributions. Continuous univariate distributions are represented by
implementations of the
[ContinuousDistribution](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/org/apache/commons/statistics/distribution/ContinuousDistribution.html)
interface. Discrete distributions implement
[DiscreteDistribution](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/org/apache/commons/statistics/distribution/DiscreteDistribution.html)
(values must be mapped to integers).

<a id="userguide--api"></a>

## API

The distribution framework provides the means to compute probability density, probability mass and cumulative probability functions for several well-known
discrete (integer-valued) and continuous probability distributions.
The API also allows for the computation of inverse cumulative probabilities
and sampling from distributions.

For an instance `f` of a distribution `F`, and a domain value, `x`, `f.cumulativeProbability(x)`
computes `P(X <= x)` where `X` is a random variable distributed
as `F`. The complement of the cumulative probability, `f.survivalProbability(x)` computes `P(X > x)`. Note that
the survival probability is approximately equal to `1 - P(X <= x)` but
does not suffer from cancellation error as the cumulative probability approaches 1.
The cancellation error may cause a (total) loss of accuracy when
`P(X <= x) ~ 1`
(see [complementary probabilities](#userguide--complements)).

```

TDistribution t = TDistribution.of(29);
double lowerTail = t.cumulativeProbability(-2.656);   // P(T(29) <= -2.656)
double upperTail = t.survivalProbability(2.75);       // P(T(29) > 2.75)
```

For [discrete](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/org/apache/commons/statistics/distribution/DiscreteDistribution.html)
`F`, the probability mass function is given by `f.probability(x)`.
For [continuous](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/org/apache/commons/statistics/distribution/ContinuousDistribution.html)
`F`, the probability density function is given by `f.density(x)`.
Distributions also implement `f.probability(x1, x2)` for computing
`P(x1 < X <= x2)`.

```

PoissonDistribution pd = PoissonDistribution.of(1.23);
double p1 = pd.probability(5);
double p2 = pd.probability(5, 5);
double p3 = pd.probability(4, 5);
// p2 == 0
// p1 == p3
```

Inverse distribution functions can be computed using the
`inverseCumulativeProbability` and `inverseSurvivalProbability`
methods. For continuous `f` and `p` a probability, `f.inverseCumulativeProbability(p)` returns

\[ x = \begin{cases}
\inf \{ x \in \mathbb R : P(X \le x) \ge p\} & \text{for } 0 \lt p \le 1 \\
\inf \{ x \in \mathbb R : P(X \le x) \gt 0 \} & \text{for } p = 0
\end{cases} \]

where `X` is distributed as `F`.
Likewise `f.inverseSurvivalProbability(p)` returns

\[ x = \begin{cases}
\inf \{ x \in \mathbb R : P(X \gt x) \le p\} & \text{for } 0 \le p \lt 1 \\
\inf \{ x \in \mathbb R : P(X \gt x) \lt 1 \} & \text{for } p = 1
\end{cases} \]

```

NormalDistribution n = NormalDistribution.of(0, 1);
double x1 = n.inverseCumulativeProbability(1e-300);
double x2 = n.inverseSurvivalProbability(1e-300);
// x1 == -x2 ~ -37.0471
```

For discrete `F`, the definition is the same, with \( \mathbb Z \)
(the integers) in place of \( \mathbb R \). Note that, in the discrete case, the strict inequality on \( p \) in the definition can make a difference when
\( p \) is an attained value of the distribution. For example moving to the next
larger value of \( p \) will return the value \( x + 1 \) for inverse CDF.

All distributions provide accessors for the parameters used to create the distribution, and a mean and variance. The return value when the mean or variance
is undefined is noted in the class javadoc.

```

ChiSquaredDistribution chi2 = ChiSquaredDistribution.of(42);
double df = chi2.getDegreesOfFreedom();    // 42
double mean = chi2.getMean();              // 42
double variance = chi2.getVariance();      // 84

CauchyDistribution cauchy = CauchyDistribution.of(1.23, 4.56);
double location = cauchy.getLocation();    // 1.23
double scale = cauchy.getScale();          // 4.56
double undefined1 = cauchy.getMean();      // NaN
double undefined2 = cauchy.getVariance();  // NaN
```

The supported domain of the distribution is provided by the
`getSupportLowerBound` and `getSupportUpperBound` methods.

```

BinomialDistribution b = BinomialDistribution.of(13, 0.15);
int lower = b.getSupportLowerBound();  // 0
int upper = b.getSupportUpperBound();  // 13
```

All distributions implement a `createSampler(UniformRandomProvider rng)`
method to support random sampling from the distribution, where `UniformRandomProvider`
is an interface defined in [Commons RNG](https://commons.apache.org/proper/commons-rng/).
The sampler is a functional interface whose functional method is `sample()`, suitable for generation of `double` or `int` samples.
Default `samples()` methods are provided to create a
`DoubleStream` or `IntStream`.

```

// From Commons RNG Simple
UniformRandomProvider rng = RandomSource.KISS.create(123L);

NormalDistribution n = NormalDistribution.of(0, 1);
double x = n.createSampler(rng).sample();

// Generate a number of samples
GeometricDistribution g = GeometricDistribution.of(0.75);
int[] k = g.createSampler(rng).samples(100).toArray();
// k.length == 100
```

Note that even when distributions are immutable, the sampler is not immutable as it
depends on the instance of the mutable `UniformRandomProvider`. Generation of
many samples in a multi-threaded application should use a separate instance of
`UniformRandomProvider` per thread. Any synchronization should be avoided
for best performance. By default the streams returned from the `samples()`
methods are sequential.

<a id="userguide--implementation-details"></a>

## Implementation Details

Instances are constructed using factory methods, typically a static method in the
distribution class named `of`. This allows the returned instance
to be specialised to the distribution parameters.

Exceptions will be raised by the factory method when constructing the distribution
using invalid parameters. See the class javadoc for exception conditions.

Unless otherwise noted, distribution instances are immutable. This allows sharing
an instance between threads for computations.

Exceptions will not be raised by distributions for an invalid `x` argument
to probability functions. Typically the cumulative probability functions will return
0 or 1 for an out-of-domain argument, depending on which the side of the domain bound
the argument falls, and the density or probability mass functions return 0.
Return values for `x` arguments when the result is
undefined should be documented in the class javadoc. For example the beta distribution
is undefined for `x = 0, alpha < 1` or `x = 1, beta < 1`.
Note: This out-of-domain behaviour may be different from distributions in the
`org.apache.commons.math3.distribution` package. Users upgrading from
`commons-math`
should check the appropriate class javadoc.

An exception will be raised by distributions for an invalid `p` argument
to inverse probability functions. The argument must be in the range `[0, 1]`.

<a id="userguide--complementary-probabilities"></a>

## Complementary Probabilities

The distributions provide the cumulative probability `p` and its complement, the survival probability, `q = 1 - p`. When the probability
`q` is small use of the cumulative probability to compute `q` can
result in dramatic loss of accuracy. This is due to the distribution of floating-point
numbers having a
[log-uniform](https://en.wikipedia.org/wiki/Reciprocal_distribution)
distribution as the limiting distribution. There are far more
representable numbers as the probability value approaches zero than when it approaches
one.

The difference is illustrated with the result of computing the upper tail of a
probability distribution.

```

ChiSquaredDistribution chi2 = ChiSquaredDistribution.of(42);
double q1 = 1 - chi2.cumulativeProbability(168);
double q2 = chi2.survivalProbability(168);
// q1 == 0
// q2 != 0
```

In this case the value `1 - p` has only a single bit of information as
`x` approaches 168. For example the value `1 - p(x=167)`
is `2-53` (or approximately `1.11e-16`).
The complement `q` retains information
much further into the long tail as shown in the following table:

<table class="bodyTableBorder" style="width: auto">
<tr>
<th colspan="3">Chi-squared distribution, 42 degrees of freedom</th></tr>
<tr>
<th>x</th>
<th>1 - p</th>
<th>q</th></tr>
<tr>
<td>166</td>
<td>1.11e-16</td>
<td>1.16e-16</td></tr>
<tr>
<td>167</td>
<td>1.11e-16</td>
<td>7.96e-17</td></tr>
<tr>
<td>168</td>
<td>0</td>
<td>5.43e-17</td></tr>
<tr>
<td>...</td>
<td></td>
<td></td></tr>
<tr>
<td>200</td>
<td>0</td>
<td>1.19e-22</td></tr>
</table>

Probability computations should use the appropriate cumulative or survival function
to calculate the lower or upper tail respectively. The same care should be applied
when inverting probability distributions. It is preferred to compute either
`p ≤ 0.5` or `q ≤ 0.5` without loss of accuracy and then
invert respectively the cumulative probability using `p` or the survival
probabilty using `q` to obtain `x`.

```

ChiSquaredDistribution chi2 = ChiSquaredDistribution.of(42);
double q = 5.43e-17;
// Incorrect: p = 1 - q == 1.0 !!!
double x1 = chi2.inverseCumulativeProbability(1 - q);
// Correct: invert q
double x2 = chi2.inverseSurvivalProbability(q);
// x1 == +infinity
// x2 ~ 168.0
```

Note: The survival probability functions were not present in the
`org.apache.commons.math3.distribution` package. Users upgrading from
`commons-math`
should update usage of the cumulative probability functions where appropriate.

<a id="userguide--inference"></a>

# Inference

The `commons-statistics-inference` module provides hypothesis testing.

<a id="userguide--overview-4"></a>

## Overview

The module provides test classes that implement a single, or family, of statistical
tests. Each test class provides methods to compute a test statistic and a p-value for the
significance of the statistic. These can be computed together using a `test`
method and returned as a
[SignificanceResult](https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/apidocs/org/apache/commons/statistics/inference/DiscreteDistribution.html).
The `SignificanceResult` has a method that can be used to `reject`
the null hypothesis at the provided significance level. Test classes may extend the
`SignificanceResult` to return more information about the test result, for example the computed degrees of freedom.

Alternatively a `statistic` method is provided to compute *only* the
statistic as a `double` value. This statistic can be compared to a pre-computed
critical value, for example from a table of critical values.

A test is obtained using the `withDefaults()` method to return the test with
all options set to their default value. Any test options can be configured using
property change methods to return a new instance of the test. Tests that support an
[alternate hypothesis](https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/apidocs/org/apache/commons/statistics/inference/AlternativeHypothesis.html) will use a two-sided test by default. Test that support multiple
[p-value methods](https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/apidocs/org/apache/commons/statistics/inference/PValueMethod.html) will default to an appropriate computation for the size of the input
data. Unless otherwise noted test instances are immutable.

<a id="userguide--examples-2"></a>

## Examples

A chi-square test that the observed counts conform to the expected frequencies.

```

double[] expected = {0.25, 0.5, 0.25};
long[] observed = {57, 123, 38};

SignificanceResult result = ChiSquareTest.withDefaults()
                                         .test(expected, observed);
result.getPValue();    // 0.0316148
result.reject(0.05);   // true
result.reject(0.01);   // false
```

A paired t-test that the marks in the math exam were greater than the science
exam. This fails to reject the null hypothesis (that there was no difference) with
95% confidence.

```

double[] math    = {53, 69, 65, 65, 67, 79, 86, 65, 62, 69};   // mean = 68.0
double[] science = {75, 65, 68, 63, 55, 65, 73, 45, 51, 52};   // mean = 61.2

SignificanceResult result = TTest.withDefaults()
                                 .with(AlternativeHypothesis.GREATER_THAN)
                                 .pairedTest(math, science);
result.getPValue();    // 0.05764
result.reject(0.05);   // false
```

A G-test that the allele frequencies conform to the expected Hardy-Weinberg proportions.
This is an example of an intrinsic hypothesis where the expected frequencies are computed
using the observations and the degrees of freedom must be adjusted.
The data is from McDonald (1989) Selection component analysis
of the Mpi locus in the amphipod Platorchestia platensis.
*Heredity* **62**: 243-249.

```

// Allele frequencies: Mpi 90/90, Mpi 90/100, Mpi 100/100
long[] observed = {1203, 2919, 1678};
// Mpi 90 proportion
double p = (2.0 * observed[0] + observed[1]) /
           (2 * Arrays.stream(observed).sum());   // 5325 / 11600 = 0.459

// Hardy-Weinberg proportions
double[] expected = {p * p, 2 * p * (1 - p), (1 - p) * (1 - p)};
// 0.211, 0.497, 0.293

SignificanceResult result = GTest.withDefaults()
                                 .withDegreesOfFreedomAdjustment(1)
                                 .test(expected, observed);
result.getStatistic();   // 1.03
result.getPValue();      // 0.309
result.reject(0.05);     // false
```

A one-way analysis of variance test. This is an example where the result has more
information than the test statistic and the p-value.
The data is from McDonald *et al* (1991) Allozymes and morphometric characters of
three species of Mytilus in the Northern and Southern Hemispheres.
*Marine Biology* **111**: 323-333.

```

double[] tillamook = {0.0571, 0.0813, 0.0831, 0.0976, 0.0817, 0.0859, 0.0735, 0.0659, 0.0923, 0.0836};
double[] newport = {0.0873, 0.0662, 0.0672, 0.0819, 0.0749, 0.0649, 0.0835, 0.0725};
double[] petersburg = {0.0974, 0.1352, 0.0817, 0.1016, 0.0968, 0.1064, 0.105};
double[] magadan = {0.1033, 0.0915, 0.0781, 0.0685, 0.0677, 0.0697, 0.0764, 0.0689};
double[] tvarminne = {0.0703, 0.1026, 0.0956, 0.0973, 0.1039, 0.1045};

Collection<double[]> data = Arrays.asList(tillamook, newport, petersburg, magadan, tvarminne);
OneWayAnova.Result result = OneWayAnova.withDefaults()
                                       .test(data);
result.getStatistic();   // 7.12
result.getPValue();      // 2.8e-4
result.reject(0.001);    // true
```

The result also provides the between and within group degrees of freedom and the mean
squares allowing reporting of the results in a table:

|  | degrees of freedom | mean square | F | p |
| --- | --- | --- | --- | --- |
| between groups | 4 | 0.001113 | 7.12 | 2.8e-4 |
| within groups | 34 | 0.000159 |  |  |

<a id="userguide--interval"></a>

# Interval

The `commons-statistics-interval` module provides statistical intervals.

The `Interval` interface provides a bounded interval with a lower and upper
bound: \( [l, u] \).

The `BinomialConfidenceInterval` enumeration provides methods
to create a confidence interval for a binomial proportion. This is an interval
containing the probability of success given a series of success-failure experiments.
The interval is constructed using a confidence level. For example a 95% confidence interval
will contain the true proportion of successes 95% of the times that the procedure
for constructing the confidence interval is employed. The target error rate \( \alpha \)
is defined as \( 1 - confidence \) when expressing the confidence level as a probability
in \( (0, 1) \).

The following example demonstrates an ideal coin toss experiment. Note how the 95%
confidence interval containing the true probability narrows as the number of trials
increases.

```

BinomialConfidenceInterval method = BinomialConfidenceInterval.WILSON_SCORE;
double alpha = 0.05;

Interval interval = method.fromErrorRate(10, 5, alpha);
interval.getLowerBound();   // 0.23659
interval.getUpperBound();   // 0.76341

method.fromErrorRate(100, 50, alpha);       // 0.40383, 0.59617
method.fromErrorRate(1000, 500, alpha);     // 0.46907, 0.53093
method.fromErrorRate(10000, 5000, alpha);   // 0.49020, 0.50980
```

The `NormalConfidenceInterval` enumeration provides methods
to create a confidence interval for a normally distributed population.
Intervals can be created for the mean or the variance from a sample of
the population.

The following example demonstrates how to generate a 95% confidence interval
for the mean given a sample. The mean and variance of the sample are
required for the interval; here they are generated using the descriptive
statistics API.

```

double[] x = {
    1.47, 1.40, 1.55, 1.44, 1.41,
    1.38, 1.53, 1.42, 1.55, 1.55,
    1.31, 1.37, 1.53, 1.47, 1.51
};
DoubleStatistics stats = DoubleStatistics.of(EnumSet.of(Statistic.MEAN, Statistic.VARIANCE), x);

double mean = stats.getAsDouble(Statistic.MEAN);          // 1.46
double variance = stats.getAsDouble(Statistic.VARIANCE);  // 0.0058
long n = stats.getCount();                                // 15
double alpha = 0.05;

Interval interval = NormalConfidenceInterval.MEAN.fromErrorRate(mean, variance, n, alpha);
interval.getLowerBound();   // 1.4170
interval.getUpperBound();   // 1.5017
```

<a id="userguide--ranking"></a>

# Ranking

The `commons-statistics-ranking` module provides rank transformations.

The `NaturalRanking` class provides a ranking based on the natural ordering
of floating-point values. Ranks are assigned to the input numbers in ascending order, starting from 1.

```

NaturalRanking ranking = new NaturalRanking();
ranking.apply(new double[] {5, 6, 7, 8});   // 1, 2, 3, 4
ranking.apply(new double[] {8, 5, 7, 6});   // 4, 1, 3, 2
```

The special case of `NaN` values are handled using the configured
`NaNStragegy`. The default is to raise an exception.

```

double[] data = new double[] {6, 5, Double.NaN, 7};
new NaturalRanking().apply(data);                      // IllegalArgumentException
new NaturalRanking(NaNStrategy.MINIMAL).apply(data);   // (4, 2, 1, 3)
new NaturalRanking(NaNStrategy.MAXIMAL).apply(data);   // (3, 1, 4, 2)
new NaturalRanking(NaNStrategy.REMOVED).apply(data);   // (3, 1, 2)
new NaturalRanking(NaNStrategy.FIXED).apply(data);     // (3, 1, NaN, 2)
new NaturalRanking(NaNStrategy.FAILED).apply(data);    // IllegalArgumentException
```

Ties are handled using the configured `TiesStragegy`. The default is to
use an average.

```

double[] data = new double[] {7, 5, 7, 6};
new NaturalRanking().apply(data);                          // (3.5, 1, 3.5, 2)
new NaturalRanking(TiesStrategy.SEQUENTIAL).apply(data);   // (3, 1, 4, 2)
new NaturalRanking(TiesStrategy.MINIMUM).apply(data);      // (3, 1, 3, 2)
new NaturalRanking(TiesStrategy.MAXIMUM).apply(data);      // (4, 1, 4, 2)
new NaturalRanking(TiesStrategy.AVERAGE).apply(data);      // (3.5, 1, 3.5, 2)
new NaturalRanking(TiesStrategy.RANDOM).apply(data);       // (3, 1, 4, 2)  or  (4, 1, 3, 2)
```

The source of randomness defaults to a system supplied generator. The randomness can be
provided as a `LongSupplier` of random 64-bit values.

```

double[] data = new double[] {7, 5, 7, 6};
new NaturalRanking(TiesStrategy.RANDOM).apply(data);
new NaturalRanking(new SplittableRandom()::nextInt).apply(data);
// From Commons RNG
UniformRandomProvider rng = RandomSource.KISS.create();
new NaturalRanking(rng::nextInt).apply(data);
// ranks: (3, 1, 4, 2)  or  (4, 1, 3, 2)
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/project-info.html -->

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons Statistics project provides tools for statistics. |
| [Summary](#summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-statistics/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-statistics/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-statistics/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-statistics/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-statistics/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-statistics/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-statistics/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/summary.html -->

<!-- page_index: 7 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics |
| Description | The Apache Commons Statistics project provides tools for statistics. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/](#index) |

<a id="summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-parent |
| Version | 1.3 |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/modules.html -->

<!-- page_index: 8 -->

<a id="modules--project-modules"></a>

# Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons Statistics Descriptive](#commons-statistics-descriptive) | Descriptive statistics. |
| [Apache Commons Statistics Distribution](#commons-statistics-distribution) | Statistical distributions. |
| [Apache Commons Statistics Ranking](#commons-statistics-ranking) | Statistical rank transformations. |
| [Apache Commons Statistics Inference](#commons-statistics-inference) | Statistical hypothesis testing. |
| [Apache Commons Statistics Interval](#commons-statistics-interval) | Statistical intervals. |
| [Apache Commons Statistics (Bill of Materials)](#commons-statistics-bom) | Bill of Materials (BOM) to aid in dependency management when referencing multiple Apache Commons Statistics artifacts. |
| [Apache Commons Statistics Documentation](#commons-statistics-docs) | Aggregator module to genenerate Apache Commons Statistics documentation. |
| [Apache Commons Statistics Examples](#commons-statistics-examples) | Examples of use of the "Commons Statistics" library. Codes in this module and its sub-modules are not part of the library. They provide checking, benchmarking tools to enhance the documentation and to help ensure correctness of the implementations. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/team.html -->

<!-- page_index: 9 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_b8001c46682e71ed.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_b8001c46682e71ed.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_b8001c46682e71ed.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_b8001c46682e71ed.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_b8001c46682e71ed.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/scm.html -->

<!-- page_index: 10 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/ci-management.html -->

<!-- page_index: 11 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-docs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/index.html -->

<!-- page_index: 12 -->

<a id="commons-statistics-docs--apache-commons-statistics"></a>

# Apache Commons Statistics

Commons Statistics provides provides tools for statistics.

Browse the [Javadoc](https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/apidocs/index.html) for more information.

---

<a id="commons-statistics-bom"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-bom/index.html -->

<!-- page_index: 13 -->

<a id="commons-statistics-bom--apache-commons-statistics"></a>

# Apache Commons Statistics

Commons Statistics provides tools for statistics.

The Bill of Materials (BOM) is provided to aid in
[dependency management](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#bill-of-materials-bom-poms)
of the Apache Commons Statistics modules.

The BOM can be imported into a Maven pom to manage the module versions:

```xml

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-statistics-bom</artifactId>
      <version>1.3</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

---

<a id="commons-statistics-interval"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/index.html -->

<!-- page_index: 14 -->

<a id="commons-statistics-interval--apache-commons-statistics:-interval"></a>

# Apache Commons Statistics: Interval

Apache Commons Statistics provides statistical intervals.

Example:

```
import org.apache.commons.statistics.interval.Interval;
import org.apache.commons.statistics.interval.BinomialConfidenceInterval;

int n = 400;
int x = 20;
double alpha = 0.05;
Interval interval = BinomialConfidenceInterval.CLOPPER_PEARSON.fromErrorRate(n, x, alpha);
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/apidocs/index.html) for more information.

---

<a id="commons-statistics-ranking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/index.html -->

<!-- page_index: 15 -->

<a id="commons-statistics-ranking--apache-commons-statistics:-ranking"></a>

# Apache Commons Statistics: Ranking

Apache Commons Statistics provides statistical rank transformations.

Example:

```
import org.apache.commons.statistics.ranking.NaturalRanking;

NaturalRanking ranking = new NaturalRanking();
ranking.apply(new double[] {5, 6, 7, 8});   // 1, 2, 3, 4
ranking.apply(new double[] {8, 5, 7, 6});   // 4, 1, 3, 2
ranking.apply(new double[] {6, 5, 6, 7});   // 2.5, 1, 2.5, 4
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/apidocs/index.html) for more information.

---

<a id="commons-statistics-inference"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/index.html -->

<!-- page_index: 16 -->

<a id="commons-statistics-inference--apache-commons-statistics:-inference"></a>

# Apache Commons Statistics: Inference

Apache Commons Statistics provides statistical hypothesis testing.

Example:

```
import org.apache.commons.statistics.inference.ChiSquaredTest;

double[] expected = ...
long[] observed = ...
double alpha = 1e-3;

// Fail if we can *reject* the null hypothesis with confidence (1 - alpha)
// that the observed match the expected
if (ChiSquareTest.withDefaults().test(expected, observed).reject(alpha)) {
    // Significant deviation from the expected ...
}
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/apidocs/index.html) for more information.

---

<a id="commons-statistics-descriptive"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/index.html -->

<!-- page_index: 17 -->

<a id="commons-statistics-descriptive--apache-commons-statistics:-descriptive"></a>

# Apache Commons Statistics: Descriptive

Apache Commons Statistics provides implementation of univariate statistics.

Example:

```
java.util.stream.Stream
import org.apache.commons.statistics.descriptive.Variance;

// Support a fixed size array
double[] values = {1, 1, 2, 3, 5, 8, 13, 21};

double v = Variance.of(values).getAsDouble();

// Support streams
double v2 = Stream.of("one", "two", "three", "four")
                  .mapToDouble(String::length)
                  .collect(Variance::create, Variance::accept, Variance::combine)
                  .getAsDouble();
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/apidocs/index.html) for more information.

---

<a id="commons-statistics-distribution"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/index.html -->

<!-- page_index: 18 -->

<a id="commons-statistics-distribution--apache-commons-statistics:-distribution"></a>

# Apache Commons Statistics: Distribution

Apache Commons Statistics provides a framework and implementations for commonly used
probability distributions.

Continuous univariate distributions are represented by the
[ContinuousDistribution](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/org/apache/commons/statistics/distribution/ContinuousDistribution.html)
interface. Discrete distributions implement
[DiscreteDistribution](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/org/apache/commons/statistics/distribution/DiscreteDistribution.html)
(values must be mapped to integers).

Example:

```
import org.apache.commons.statistics.distribution.TDistribution;

double degreesOfFreedom = 29;
TDistribution t = TDistribution.of(degreesOfFreedom);
double lowerTail = t.cumulativeProbability(-2.656);   // P(T(29) <= -2.656)
double upperTail = t.survivalProbability(2.75);       // P(T(29) > 2.75)
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/apidocs/index.html) for more information.

---

<a id="commons-statistics-bom-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-bom/ci-management.html -->

<!-- page_index: 19 -->

<a id="commons-statistics-bom-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-bom-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-bom-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-bom-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-bom/scm.html -->

<!-- page_index: 20 -->

<a id="commons-statistics-bom-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-bom-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-bom
```

<a id="commons-statistics-bom-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-bom-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-bom-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-bom-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-bom/summary.html -->

<!-- page_index: 21 -->

<a id="commons-statistics-bom-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-bom-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics (Bill of Materials) |
| Description | Bill of Materials (BOM) to aid in dependency management when referencing multiple Apache Commons Statistics artifacts. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-bom/](#commons-statistics-bom) |

<a id="commons-statistics-bom-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-bom-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-bom |
| Version | 1.3 |
| Type | pom |

---

<a id="commons-statistics-bom-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-bom/team.html -->

<!-- page_index: 22 -->

<a id="commons-statistics-bom-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-bom-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_8e89de0c99728f0f.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_8e89de0c99728f0f.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-bom-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_8e89de0c99728f0f.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_8e89de0c99728f0f.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_8e89de0c99728f0f.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-descriptive-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/ci-management.html -->

<!-- page_index: 23 -->

<a id="commons-statistics-descriptive-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-descriptive-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-descriptive-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-descriptive-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/scm.html -->

<!-- page_index: 24 -->

<a id="commons-statistics-descriptive-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-descriptive-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-descriptive
```

<a id="commons-statistics-descriptive-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-descriptive-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-descriptive-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-descriptive-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/summary.html -->

<!-- page_index: 25 -->

<a id="commons-statistics-descriptive-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-descriptive-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Descriptive |
| Description | Descriptive statistics. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/](#commons-statistics-descriptive) |

<a id="commons-statistics-descriptive-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-descriptive-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-descriptive |
| Version | 1.3 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-statistics-descriptive-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-descriptive/team.html -->

<!-- page_index: 26 -->

<a id="commons-statistics-descriptive-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-descriptive-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_10ebba58c35d5279.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_10ebba58c35d5279.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-descriptive-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_10ebba58c35d5279.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_10ebba58c35d5279.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_10ebba58c35d5279.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-distribution-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/ci-management.html -->

<!-- page_index: 27 -->

<a id="commons-statistics-distribution-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-distribution-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-distribution-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-distribution-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/scm.html -->

<!-- page_index: 28 -->

<a id="commons-statistics-distribution-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-distribution-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-distribution
```

<a id="commons-statistics-distribution-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-distribution-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-distribution-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-distribution-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/summary.html -->

<!-- page_index: 29 -->

<a id="commons-statistics-distribution-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-distribution-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Distribution |
| Description | Statistical distributions. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/](#commons-statistics-distribution) |

<a id="commons-statistics-distribution-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-distribution-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-distribution |
| Version | 1.3 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-statistics-distribution-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-distribution/team.html -->

<!-- page_index: 30 -->

<a id="commons-statistics-distribution-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-distribution-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1d13711b29d78480.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_1d13711b29d78480.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-distribution-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1d13711b29d78480.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_1d13711b29d78480.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_1d13711b29d78480.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-docs-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/ci-management.html -->

<!-- page_index: 31 -->

<a id="commons-statistics-docs-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-docs-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-docs-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-docs-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/scm.html -->

<!-- page_index: 32 -->

<a id="commons-statistics-docs-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-docs-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-docs
```

<a id="commons-statistics-docs-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-docs-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-docs-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-docs-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/summary.html -->

<!-- page_index: 33 -->

<a id="commons-statistics-docs-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-docs-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Documentation |
| Description | Aggregator module to genenerate Apache Commons Statistics documentation. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/](#commons-statistics-docs) |

<a id="commons-statistics-docs-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-docs-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-docs |
| Version | 1.3 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-statistics-docs-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-docs/team.html -->

<!-- page_index: 34 -->

<a id="commons-statistics-docs-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-docs-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_e5ada91e1e2e63d8.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_e5ada91e1e2e63d8.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-docs-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_e5ada91e1e2e63d8.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_e5ada91e1e2e63d8.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_e5ada91e1e2e63d8.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-examples-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/ci-management.html -->

<!-- page_index: 35 -->

<a id="commons-statistics-examples-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-examples-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-examples-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/index.html -->

<!-- page_index: 36 -->

<a id="commons-statistics-examples--about-apache-commons-statistics-examples"></a>

# About Apache Commons Statistics Examples

Examples of use of the "Commons Statistics" library.
Codes in this module and its sub-modules are not part of the library.
They provide checking, benchmarking tools to enhance the documentation
and to help ensure correctness of the implementations.

<a id="commons-statistics-examples--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons Statistics Distribution Utilities](https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/commons-statistics-examples-distribution/index.html) | Application for calling the distributions defined in Commons Statistics. Code in this module is not part of the public API. |
| [Apache Commons Statistics JMH Benchmark](https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/commons-statistics-examples-jmh/index.html) | Code for running JMH benchmarks that assess performance. Code in this module is not part of the public API. |

---

<a id="commons-statistics-examples-modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/modules.html -->

<!-- page_index: 37 -->

<a id="commons-statistics-examples-modules--project-modules"></a>

# Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons Statistics Distribution Utilities](https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/commons-statistics-examples-distribution/index.html) | Application for calling the distributions defined in Commons Statistics. Code in this module is not part of the public API. |
| [Apache Commons Statistics JMH Benchmark](https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/commons-statistics-examples-jmh/index.html) | Code for running JMH benchmarks that assess performance. Code in this module is not part of the public API. |

---

<a id="commons-statistics-examples-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/scm.html -->

<!-- page_index: 38 -->

<a id="commons-statistics-examples-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-examples-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-examples
```

<a id="commons-statistics-examples-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-examples-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-examples-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-examples-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/summary.html -->

<!-- page_index: 39 -->

<a id="commons-statistics-examples-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-examples-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Examples |
| Description | Examples of use of the "Commons Statistics" library. Codes in this module and its sub-modules are not part of the library. They provide checking, benchmarking tools to enhance the documentation and to help ensure correctness of the implementations. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/](#commons-statistics-examples) |

<a id="commons-statistics-examples-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-examples-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-examples |
| Version | 1.3 |
| Type | pom |

---

<a id="commons-statistics-examples-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-examples/team.html -->

<!-- page_index: 40 -->

<a id="commons-statistics-examples-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-examples-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1b9b4a08e5b5a7bb.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_1b9b4a08e5b5a7bb.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-examples-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1b9b4a08e5b5a7bb.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_1b9b4a08e5b5a7bb.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_1b9b4a08e5b5a7bb.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-inference-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/ci-management.html -->

<!-- page_index: 41 -->

<a id="commons-statistics-inference-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-inference-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-inference-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-inference-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/scm.html -->

<!-- page_index: 42 -->

<a id="commons-statistics-inference-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-inference-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-inference
```

<a id="commons-statistics-inference-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-inference-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-inference-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-inference-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/summary.html -->

<!-- page_index: 43 -->

<a id="commons-statistics-inference-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-inference-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Inference |
| Description | Statistical hypothesis testing. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/](#commons-statistics-inference) |

<a id="commons-statistics-inference-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-inference-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-inference |
| Version | 1.3 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-statistics-inference-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-inference/team.html -->

<!-- page_index: 44 -->

<a id="commons-statistics-inference-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-inference-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1a6c77fb64d704cb.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_1a6c77fb64d704cb.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-inference-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_1a6c77fb64d704cb.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_1a6c77fb64d704cb.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_1a6c77fb64d704cb.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-interval-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/ci-management.html -->

<!-- page_index: 45 -->

<a id="commons-statistics-interval-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-interval-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-interval-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-interval-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/scm.html -->

<!-- page_index: 46 -->

<a id="commons-statistics-interval-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-interval-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-interval
```

<a id="commons-statistics-interval-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-interval-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-interval-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-interval-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/summary.html -->

<!-- page_index: 47 -->

<a id="commons-statistics-interval-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-interval-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Interval |
| Description | Statistical intervals. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/](#commons-statistics-interval) |

<a id="commons-statistics-interval-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-interval-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-interval |
| Version | 1.3 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-statistics-interval-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-interval/team.html -->

<!-- page_index: 48 -->

<a id="commons-statistics-interval-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-interval-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_28a835964265a32a.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_28a835964265a32a.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-interval-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_28a835964265a32a.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_28a835964265a32a.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_28a835964265a32a.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---

<a id="commons-statistics-ranking-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/ci-management.html -->

<!-- page_index: 49 -->

<a id="commons-statistics-ranking-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-statistics-ranking-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-statistics/actions
```

<a id="commons-statistics-ranking-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-statistics-ranking-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/scm.html -->

<!-- page_index: 50 -->

<a id="commons-statistics-ranking-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-statistics-ranking-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-statistics.git/commons-statistics-ranking
```

<a id="commons-statistics-ranking-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-ranking-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-statistics.git
```

<a id="commons-statistics-ranking-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-statistics-ranking-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/summary.html -->

<!-- page_index: 51 -->

<a id="commons-statistics-ranking-summary--project-summary"></a>

# Project Summary

<a id="commons-statistics-ranking-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Statistics Ranking |
| Description | Statistical rank transformations. |
| Homepage | [https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/](#commons-statistics-ranking) |

<a id="commons-statistics-ranking-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-statistics-ranking-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-statistics-ranking |
| Version | 1.3 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-statistics-ranking-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-statistics/commons-statistics-ranking/team.html -->

<!-- page_index: 52 -->

<a id="commons-statistics-ranking-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-statistics-ranking-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_5f9ca1ac42e15c29.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_5f9ca1ac42e15c29.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-statistics-ranking-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_5f9ca1ac42e15c29.jpg) | Ben Nguyen | [bennguyenib at gmail dot com](mailto:bennguyenib at gmail dot com) |
| ![](assets/images/00000000000000000000000000000000_5f9ca1ac42e15c29.jpg) | Arturo Bernal | - |
| ![](assets/images/00000000000000000000000000000000_5f9ca1ac42e15c29.jpg) | Anirudh Joshi | [janirudhg at gmail dot com](mailto:janirudhg at gmail dot com) |

---
