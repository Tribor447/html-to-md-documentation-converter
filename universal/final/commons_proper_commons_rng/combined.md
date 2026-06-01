# Project Information

## Navigation

- RNG
  - [Overview](#index)
  - [Issue Tracking](#issue-tracking)
  - [Developers Guide](#developers)
  - [Release History](#release-history)
- User Guide
  - [Contents](#userguide-rng--table_of_contents)
  - [Usage](#userguide-rng--a2._usage_overview)
  - [Performance](#userguide-rng--a4._performance)
  - [Quality](#userguide-rng--a5._quality)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Project Modules](#modules)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- RNG Documentation
  - [Overview](#commons-rng-docs)
- RNG Bill of Materials
  - [Overview](#commons-rng-bom)
- RNG Simple
  - [Overview](#commons-rng-simple)
- RNG Client API
  - [Overview](#commons-rng-client-api)
- RNG Sampling
  - [Overview](#commons-rng-sampling)
- RNG Core
  - [Overview](#commons-rng-core)
- Other pages
  - [Overview](#commons-rng-bom-ci-management)
  - [Overview](#commons-rng-bom-scm)
  - [Project Summary](#commons-rng-bom-summary)
  - [Project Team](#commons-rng-bom-team)
  - [Overview](#commons-rng-client-api-ci-management)
  - [Overview](#commons-rng-client-api-scm)
  - [Project Summary](#commons-rng-client-api-summary)
  - [Project Team](#commons-rng-client-api-team)
  - [Overview](#commons-rng-core-ci-management)
  - [Overview](#commons-rng-core-scm)
  - [Project Summary](#commons-rng-core-summary)
  - [Project Team](#commons-rng-core-team)
  - [Overview](#commons-rng-docs-ci-management)
  - [Overview](#commons-rng-docs-scm)
  - [Project Summary](#commons-rng-docs-summary)
  - [Project Team](#commons-rng-docs-team)
  - [Overview](#commons-rng-examples-ci-management)
  - [Overview](#commons-rng-examples-commons-rng-examples-jmh-ci-management)
  - [About Apache Commons RNG JMH Benchmark](#commons-rng-examples-commons-rng-examples-jmh)
  - [Overview](#commons-rng-examples-commons-rng-examples-jmh-scm)
  - [Project Summary](#commons-rng-examples-commons-rng-examples-jmh-summary)
  - [Project Team](#commons-rng-examples-commons-rng-examples-jmh-team)
  - [Overview](#commons-rng-examples-commons-rng-examples-jpms-ci-management)
  - [About Apache Commons RNG JPMS Integration Test](#commons-rng-examples-commons-rng-examples-jpms)
  - [Project Modules](#commons-rng-examples-commons-rng-examples-jpms-modules)
  - [Overview](#commons-rng-examples-commons-rng-examples-jpms-scm)
  - [Project Summary](#commons-rng-examples-commons-rng-examples-jpms-summary)
  - [Project Team](#commons-rng-examples-commons-rng-examples-jpms-team)
  - [Overview](#commons-rng-examples-commons-rng-examples-quadrature-ci-management)
  - [About Apache Commons RNG Quadrature Example](#commons-rng-examples-commons-rng-examples-quadrature)
  - [Overview](#commons-rng-examples-commons-rng-examples-quadrature-scm)
  - [Project Summary](#commons-rng-examples-commons-rng-examples-quadrature-summary)
  - [Project Team](#commons-rng-examples-commons-rng-examples-quadrature-team)
  - [Overview](#commons-rng-examples-commons-rng-examples-sampling-ci-management)
  - [About Apache Commons RNG Examples Sampling Utilities](#commons-rng-examples-commons-rng-examples-sampling)
  - [Overview](#commons-rng-examples-commons-rng-examples-sampling-scm)
  - [Project Summary](#commons-rng-examples-commons-rng-examples-sampling-summary)
  - [Project Team](#commons-rng-examples-commons-rng-examples-sampling-team)
  - [Overview](#commons-rng-examples-commons-rng-examples-stress-ci-management)
  - [About Apache Commons RNG Examples Stress Utilities](#commons-rng-examples-commons-rng-examples-stress)
  - [Overview](#commons-rng-examples-commons-rng-examples-stress-scm)
  - [Project Summary](#commons-rng-examples-commons-rng-examples-stress-summary)
  - [Project Team](#commons-rng-examples-commons-rng-examples-stress-team)
  - [About Apache Commons RNG Examples](#commons-rng-examples)
  - [Project Modules](#commons-rng-examples-modules)
  - [Overview](#commons-rng-examples-scm)
  - [Project Summary](#commons-rng-examples-summary)
  - [Project Team](#commons-rng-examples-team)
  - [Overview](#commons-rng-sampling-ci-management)
  - [Overview](#commons-rng-sampling-scm)
  - [Project Summary](#commons-rng-sampling-summary)
  - [Project Team](#commons-rng-sampling-team)
  - [Overview](#commons-rng-simple-ci-management)
  - [Overview](#commons-rng-simple-scm)
  - [Project Summary](#commons-rng-simple-summary)
  - [Project Team](#commons-rng-simple-team)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.

Casual use is as simple as:

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.simple.RandomSource;

// Instantiate a generator with a factory method.
UniformRandomProvider rng = RandomSource.XO_RO_SHI_RO_128_PP.create();

// Use it to produce a floating-point value between 0 and 1.
double random = rng.nextDouble();
```

For more examples and more advanced usage, see the [userguide](#userguide-rng).

Commons RNG is intended to be a repository of pure Java implementations of
random number generators that produce deterministic sequences.
The current design has made no provision for features generally needed for
cryptography applications (e.g. strong unpredictability).

The emphasis is on state-of-the-art generators that pass stringent uniformity
tests such as [TestU01 (BigCrush)](http://simul.iro.umontreal.ca/testu01/tu01.html), [Dieharder](http://www.phy.duke.edu/~rgb/General/dieharder.php) and
[PractRand](http://pracrand.sourceforge.net/).
Weaker algorithms, with known shortcomings, are also provided (for reference or
due to their historical importance) but their use is best avoided in new
applications.

<a id="index--download-apache-commons-rng"></a>

# Download Apache Commons RNG

<a id="index--releases"></a>

## Releases

Download the
[latest release](https://commons.apache.org/rng/download_rng.cgi) of Apache Commons RNG.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/issue-tracking.html -->

<!-- page_index: 2 -->

<a id="issue-tracking--apache-commons-rng-issue-tracking"></a>

# Apache Commons RNG Issue tracking

Apache Commons RNG uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons RNG JIRA project page](https://issues.apache.org/jira/browse/RNG).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons RNG please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320623&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-rng/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12320623&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12320623&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons RNG are all unpaid volunteers

For more information on git and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons RNG bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320623&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons RNG bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320623&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons RNG bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12320623&sorter/field=issuekey&sorter/order=DESC)

---

<a id="developers"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/developers.html -->

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

1. Download the Commons RNG source code. Follow the instructions
   under the heading "Repository Checkout" on the
   [Git at the ASF page](https://gitbox.apache.org/).
   The git url for the current development sources of Commons RNG
   is

```
http://gitbox.apache.org/repos/asf/commons-rng.git
```

   for anonymous read-only access and

```
https://apacheid@gitbox.apache.org/repos/asf/commons-rng.git
```

   (where apacheid should be replaced by each committer Apache ID) for committers
   read-write access.
2. Like most commons components, Commons RNG uses Apache Maven as our
   build tool.
   To build Commons RNG using Maven, you can follow the instructions for
   [Building a
   project with Maven](https://maven.apache.org/run-maven/index.html).
   Launch Maven from the top-level directory
   in the checkout of Commons RNG trunk. No special setup is required,
   except that currently to build the site (i.e. to execute Maven's
   "site" goal), you may need to increase the default memory allocation
   (e.g. `export MAVEN_OPTS=-Xmx512m`) before launching
   Maven.
3. Be sure to join the commons-dev and commons-user
   [email lists](https://commons.apache.org/proper/commons-rng/mail-lists.html) and use them appropriately (make sure the string
   "[RNG]" starts the Subject line of all your postings).
   Make any proposals here where the group can comment on them.
4. [Setup an account on JIRA](https://issues.apache.org/jira/secure/Signup!default.jspa)
   and use it to submit patches and
   identify bugs. Read the
   [directions](https://issues.apache.org/bugwritinghelp.html)
   for submitting bugs and search the database to
   determine if an issue exists or has already been dealt with.
   See the [Commons RNG Issue Tracking Page](https://commons.apache.org/rng/issue-tracking.html)
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
   The Commons RNG repository can be forked and changes merged via a PR.
   See [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) for more information on pull requests.

**Contributing ideas and code**

Follow the steps below when making suggestions for additions or
enhancements to Commons RNG. This will make it easier for the community
to comment on your ideas and for the committers to keep track of them.
Thanks in advance!

1. Start with a post to the commons-dev mailing list, with [RNG] at
   the beginning of the subject line, followed by a short title
   describing the new feature or enhancement; for example, "[RNG]
   New cryptographically secure generator".
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
   Create a JIRA ticket using the the feature title as the short
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

Commons RNG follows [Code Conventions for the Java Programming Language (circa 1999)](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html). As part of the maven
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
- Commons RNG javadoc generation supports embedded LaTeX formulas via the
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

- Exceptions generated by Commons RNG are all unchecked.
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

It must be noted that, due to the nature of random number generation, some unit tests
are bound to fail with some probability. This is applicable for tests that compare
random output to an expected distribution. These tests *should* **not**
use a fixed seed to ensure consistent output. The 'maven-surefire-plugin' is configured to
re-run tests that fail, and pass the build if they succeed within the allotted number of
reruns (the test will be marked as 'flaky' in the report). Any test that is consistently
'flaky' may require an update to the test assumptions and assertions.

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

<!-- source_url: https://commons.apache.org/proper/commons-rng/release-history.html -->

<!-- page_index: 4 -->

<a id="release-history--commons-rng-release-history"></a>

# Commons RNG Release History

*Note.* For older release javadocs see the individual artifact sub-sites.

| Version | Release date (YYYY-MM-DD) | Required Java Version | Release notes |
| --- | --- | --- | --- |
| 1.7 | 2026-04-20 | 8+ | [Release notes for 1.7](assets/files/release-notes-1-7_4736eeec47d25d7f.txt) |
| 1.6 | 2024-07-15 | 8+ | [Release notes for 1.6](assets/files/release-notes-1-6_37412ea86f78f73a.txt) |
| 1.5 | 2022-09-10 | 8+ | [Release notes for 1.5](assets/files/release-notes-1-5_12316c18322203b1.txt) |
| 1.4 | 2021-09-13 | 8+ | [Release notes for 1.4](assets/files/release-notes-1-4_2ef0ed0f49264832.txt) |
| 1.3 | 2019-11-08 | 6+ | [Release notes for 1.3](assets/files/release-notes-1-3_ca2167d09e494896.txt) |
| 1.2 | 2018-12-07 | 6+ | [Release notes for 1.2](assets/files/release-notes-1-2_c33c43ca44cf19b4.txt) |
| 1.1 | 2018-08-14 | 6+ | [Release notes for 1.1](assets/files/release-notes-1-1_ff00f091b52d4d9b.txt) |
| 1.0 | 2016-12-13 | 6+ | [Release notes for 1.0](assets/files/release-notes-1-0_18b5f2513e81defc.txt) |

---

<a id="userguide-rng"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/userguide/rng.html -->

<!-- page_index: 5 -->

<a id="userguide-rng--the-apache-commons-rng-user-guide"></a>

# The Apache Commons RNG User Guide

<a id="userguide-rng--table-of-contents"></a>

## Table of contents

- [Purpose of the library](#userguide-rng--a1._purpose)
- [Usage overview (for users)](#userguide-rng--a2._usage_overview)
- [Library layout (for developers)](#userguide-rng--a3._library_layout)
- [Performance](#userguide-rng--a4._performance)
- [Quality](#userguide-rng--a5._quality)
- [Examples](#userguide-rng--a6._examples)
- [Release compatibility](#userguide-rng--a7._release_compatibility)
- [Dependencies](#userguide-rng--a8._dependencies)

<a id="userguide-rng--1.-purpose"></a>

# 1. Purpose

`Commons RNG` provides generators of "pseudo-randomness", i.e. the generators produce deterministic sequences of bytes, currently in chunks of 32 (a.k.a. `int`) or 64 bits (a.k.a. `long`), depending on the implementation.

The goal was to provide an API that is simple and unencumbered with old design decisions.

The design is clean and its rationale is explained in the code and Javadoc (as well as in the extensive discussions on the "Apache Commons" project's mailing list).

The code evolved during several months in order to accommodate the requirements gathered from the design issues identified in the `org.apache.commons.math3.random` package and the explicit design goal of [severing ties](https://commons.apache.org/proper/commons-rng/userguide/why_not_java_random.html) to `java.util.Random`.

The library is divided into modules:

- [Client API](https://commons.apache.org/proper/commons-rng/commons-rng-client-api/apidocs/org/apache/commons/rng/package-summary.html) (requires Java 8)

  This module provides the [interface](https://commons.apache.org/proper/commons-rng/commons-rng-client-api/apidocs/org/apache/commons/rng/RestorableUniformRandomProvider.html) to be passed as argument to a procedure that needs to access to a sequence of random numbers.
- [Core](https://commons.apache.org/proper/commons-rng/commons-rng-core/apidocs/org/apache/commons/rng/core/package-summary.html) (requires Java 8)

  This module contains the implementations of several generators of pseudo-random sequences of numbers. Code in this module is intended to be internal to this library and no user code should access it directly. With the advent of [Java modularization](http://openjdk.java.net/projects/jigsaw/), it is possible that future releases of the library will enforce access through the [RandomSource](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/RandomSource.html) factory.
- [Simple](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/package-summary.html) (requires Java 8)

  This module provides factory methods for creating instances of all the generators implemented in the `commons-rng-core` module.
- [Sampling](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/package-summary.html) (requires Java 8)

  This module provides implementations that: generate a sequence of numbers according to some specified probability distribution; sample coordinates from geometric shapes; sample from generic collections of items; and other sampling utilities. It is an example of usage of the API provided in the `commons-rng-client-api` module.
- Examples

  This module provides miscellaneous complete applications that illustrate usage of the library. Please note that this module is not part of the library's API; no compatibility should be expected in successive releases of "Commons RNG". The examples can be download in the [source distribution](https://commons.apache.org/rng/download_rng.cgi).

  As of version 1.1, the following modules are provided:

  - `examples-jmh`: JMH benchmarking (requires Java 8)

    This module uses the [JMH micro-benchmark framework](http://openjdk.java.net/projects/code-tools/jmh/) in order to assess the relative performance of the generators (see tables below).
  - `examples-stress`: Stress testing (requires Java 8)

    This module implements a wrapper that calls external tools that can assess the quality of the generators by submitting their output to a battery of "stress tests" (see tables below).
  - `examples-sampling`: Probability density (requires Java 8)

    This module contains the code that generates the data used to produce the probability density plots shown in [this userguide](https://commons.apache.org/proper/commons-rng/userguide/dist_density_approx.html).
  - `examples-jpms`: JPMS integration (requires Java 11)

    This module implements a dummy application that shows how to use the artefacts (produced from the maven modules described above) as Java modules ([JPMS](https://en.wikipedia.org/wiki/Java_Platform_Module_System)).
  - `examples-quadrature`: Quadrature (requires Java 8)

    This module contains an application that estimates the number 𝞹 using quasi-Montecarlo integration.

<a id="userguide-rng--2.-usage-overview"></a>

# 2. Usage overview

Please refer to the generated documentation (of the appropriate module) for details on the API illustrated by the following examples.

- Random number generator objects are instantiated through factory methods defined in `RandomSource`, an `enum` that declares [all the available implementations](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/RandomSource.html#enum.constant.detail).

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.simple.RandomSource;

UniformRandomProvider rng = RandomSource.XO_RO_SHI_RO_128_PP.create();
```

- A generator can return a randomly selected element from a range of possible values of some Java (primitive) type.

```
boolean isOn = rng.nextBoolean(); // "true" or "false".
```


```
int n = rng.nextInt();         // Integer.MIN_VALUE <= n <= Integer.MAX_VALUE.
int m = rng.nextInt(max);      // 0 <= m < max.
int l = rng.nextInt(min, max); // min <= l < max.
```


```
long n = rng.nextLong();         // Long.MIN_VALUE <= n <= Long.MAX_VALUE.
long m = rng.nextLong(max);      // 0 <= m < max.
long l = rng.nextLong(min, max); // min <= l < max.
```


```
float x = rng.nextFloat();         // 0 <= x < 1.
float y = rng.nextFloat(max);      // 0 <= y < max.
float z = rng.nextFloat(min, max); // min <= z < max.
```


```
double x = rng.nextDouble();         // 0 <= x < 1.
double y = rng.nextDouble(max);      // 0 <= y < max.
double z = rng.nextDouble(min, max); // min <= z < max.
```

- A generator can fill a given `byte` array with random values.

```
byte[] a = new byte[47];
// The elements of "a" are replaced with random values from the interval [-128, 127].
rng.nextBytes(a);
```


```
byte[] a = new byte[47];
// Replace 3 elements of the array (at indices 15, 16 and 17) with random values.
rng.nextBytes(a, 15, 3);
```

- A generator can return a stream of primitive values.

```
IntStream s1 = rng.ints();         // [Integer.MIN_VALUE, Integer.MAX_VALUE]
IntStream s2 = rng.ints(max);      // [0, max)
IntStream s3 = rng.ints(min, max); // [min, max)
```


```
LongStream s1 = rng.longs();         // [Long.MIN_VALUE, Long.MAX_VALUE]
LongStream s2 = rng.longs(max);      // [0, max)
LongStream s3 = rng.longs(min, max); // [min, max)
```


```
DoubleStream s1 = rng.doubles();         // [0, 1)
DoubleStream s2 = rng.doubles(max);      // [0, max)
DoubleStream s3 = rng.doubles(min, max); // [min, max)
```

  Streams can be limited by a stream size argument.


```
// Roll a die 1000 times
int[] rolls = rng.ints(1000, 1, 7).toArray();
```

  It should be noted that streams returned by the interface default implementation perform repeat calls to the relevant `next` generation method and may have a performance overhead. Efficient streams can be created using an instance of a sampler which can precompute coefficients on construction (see the [sampling](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/package-summary.html) module).
- The `UniformRandomProvider` interface provides default implementations for all generation methods except `nextLong`. Implementation of a new generator must only provide a 64-bit source of randomness.

```
UniformRandomProvider rng = new SecureRandom()::nextLong;
```

  Abstract classes for a 32-bit or 64-bit source of randomness, with additional functionality not present in the interface, are provided in the [core](https://commons.apache.org/proper/commons-rng/commons-rng-core/apidocs/org/apache/commons/rng/core/package-summary.html) module.
- In order to generate reproducible sequences, generators must be instantiated with a user-defined seed.

```
UniformRandomProvider rng = RandomSource.SPLIT_MIX_64.create(5776);
```

  If no seed is passed, a random seed is generated implicitly.

  Convenience methods are provided for explicitly generating random seeds of the various types.


```
int seed = RandomSource.createInt();
```


```
long seed = RandomSource.createLong();
```


```
int[] seed = RandomSource.createIntArray(128); // Length of returned array is 128.
```


```
long[] seed = RandomSource.createLongArray(128); // Length of returned array is 128.
```

- Any of the following types can be passed to the `create` method as the "seed" argument:
  - `int` or `Integer`
  - `long` or `Long`
  - `int[]`
  - `long[]`
  - `byte[]`
```
UniformRandomProvider rng = RandomSource.ISAAC.create(5776);
```


```
UniformRandomProvider rng = RandomSource.ISAAC.create(new int[] { 6, 7, 7, 5, 6, 1, 0, 2 });
```


```
UniformRandomProvider rng = RandomSource.ISAAC.create(new long[] { 0x638a3fd83bc0e851L, 0x9730fd12c75ae247L });
```

  Note however that, upon initialization, the underlying generation algorithm

  - may not use all the information contents of the seed,
  - may use a procedure (using the given seed as input) for further filling its internal state (in order to avoid a too uniform initial state).

  In both cases, the behavior is not standard but should not change between releases of the library (bugs notwithstanding).

  Each RNG implementation has a single "native" seed; when the seed argument passed to the `create` method is not of the native type, it is automatically converted. The conversion preserves the information contents but is otherwise not specified (i.e. different releases of the library may use different conversion procedures).

  Hence, if reproducibility of the generated sequences across successive releases of the library is necessary, users should ensure that they use native seeds.


```
long seed = 9246234616L;
if (!RandomSource.TWO_CMRES.isNativeSeed(seed)) {
    throw new IllegalArgumentException("Seed is not native");
}
```

  For each available implementation, the native seed type is specified in the [Javadoc](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/RandomSource.html#enum.constant.detail).
- Whenever a random source implementation is parameterized, the custom arguments are passed after the seed.

```
int seed = 96912062;
int first = 7; // Subcycle identifier.
int second = 4; // Subcycle identifier.
UniformRandomProvider rng = RandomSource.TWO_CMRES_SELECT.create(seed, first, second);
```

  In the above example, valid "subcycle identifiers" are in the interval [0, 13].
- The current state of a generator can be [saved](https://commons.apache.org/proper/commons-rng/commons-rng-client-api/apidocs/org/apache/commons/rng/RestorableUniformRandomProvider.html#saveState--) and [restored](https://commons.apache.org/proper/commons-rng/commons-rng-client-api/apidocs/org/apache/commons/rng/RestorableUniformRandomProvider.html#restoreState-org.apache.commons.rng.RandomProviderState-) later on.

```
import org.apache.commons.rng.RestorableUniformRandomProvider;
import org.apache.commons.rng.RandomProviderState;

RestorableUniformRandomProvider rng = RandomSource.XO_RO_SHI_RO_128_PP.create();
RandomProviderState state = rng.saveState();
double x = rng.nextDouble();
rng.restoreState(state);
double y = rng.nextDouble(); // x == y.
```

- The `UniformRandomProvider` objects returned from the `create` methods do not implement the `java.io.Serializable` interface.

  However, users can easily set up a custom serialization scheme if the random source is known at both ends of the communication channel. This would be useful namely to save the state to persistent storage, and restore it such that the sequence will continue from where it left off.


```
import org.apache.commons.rng.RestorableUniformRandomProvider;
import org.apache.commons.rng.simple.RandomSource;
import org.apache.commons.rng.core.RandomProviderDefaultState;

RandomSource source = RandomSource.KISS; // Known source identifier.

RestorableUniformRandomProvider rngOrig = source.create(); // Original RNG instance.

// Save and serialize state.
RandomProviderState stateOrig = rngOrig.saveState(rngOrig);
ByteArrayOutputStream bos = new ByteArrayOutputStream();
ObjectOutputStream oos = new ObjectOutputStream(bos);
oos.writeObject(((RandomProviderDefaultState) stateOrig).getState());

// Deserialize state.
ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
ObjectInputStream ois = new ObjectInputStream(bis);
RandomProviderState stateNew = new RandomProviderDefaultState((byte[]) ois.readObject());

RestorableUniformRandomProvider rngNew = source.create(); // New RNG instance from the same "source".

// Restore original state on the new instance.
rngNew.restoreState(stateNew);
```

- The `JumpableUniformRandomProvider` interface allows creation of a copy of the generator and advances the state of the current generator a large number of steps in a single jump. This can be used to create a set of generators that will not overlap in their output sequence for the length of the jump for use in parallel computations.

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.JumpableUniformRandomProvider;
import org.apache.commons.rng.simple.RandomSource;
import java.util.concurrent.ForkJoinPool;

RandomSource source = RandomSource.XO_RO_SHI_RO_128_SS; // Known to be jumpable.

JumpableUniformRandomProvider jumpable = (JumpableUniformRandomProvider) source.create();

// For use in parallel
int streamSize = 10;
jumpable.jumps(streamSize).forEach(rng -> {
    ForkJoinPool.commonPool().execute(() -> {
        // Task using the rng
    });
});
```

  Note that here the stream of RNGs is sequential; each RNG is used within a potentially long-running task that can run concurrently with other tasks using an executor service.
- The `ArbitrarilyJumpableUniformRandomProvider` interface allows creation of a copy of the generator and advances the state of the current generator an *arbitrary* number of steps in a single jump. Jump distances are supported using a `double` or using a power-of-2. Streams of jumpable generators can be created using a `double` distance. Since each copy generator is also an `ArbitrarilyJumpableUniformRandomProvider` with care it is possible to further distribute generators within the original jump distance and use the entire state cycle in different ways.

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.ArbitrarilyJumpableUniformRandomProvider;
import org.apache.commons.rng.simple.RandomSource;

RandomSource source = RandomSource.PHILOX_4X64; // Known to be arbitrarily jumpable.

ArbitrarilyJumpableUniformRandomProvider jumpable = (ArbitrarilyJumpableUniformRandomProvider) source.create();

double distance = 42;
for (int i = 0; i < 5; i++) {
    // Copy the state and then jump ahead
    UniformRandomProvider copy = jumpable.jump(distance);

    // Catch up the jump using the native 64-bit output
    for (int j = 0; j < distance; j++) {
        copy.nextLong();
    }

    // The copy matches the jumped generator
    assert copy.nextLong() == jumpable.nextLong();
}

int logDistance = 123;
ArbitrarilyJumpableUniformRandomProvider copy = jumpable.jumpPowerOfTwo(logDistance);

// Catch up the jump using: 4 * 2^119 + 2^121 + 2^122
copy.jumpPowerOfTwo(logDistance - 4);
copy.jumpPowerOfTwo(logDistance - 4);
copy.jumpPowerOfTwo(logDistance - 2);
copy.jumpPowerOfTwo(logDistance - 4);
copy.jumpPowerOfTwo(logDistance - 1);
copy.jumpPowerOfTwo(logDistance - 4);

// The copy matches the jumped generator
assert copy.nextLong() == jumpable.nextLong();
```

  In the above examples, the source is known to implement the appropriate jumpable interface. Not all generators support this functionality. You can determine if a `RandomSource` is jumpable without creating one using the instance methods `isJumpable()`, `isLongJumpable()` and `isArbitrarilyJumpable`.


```
import org.apache.commons.rng.simple.RandomSource;
public void initialise(RandomSource source) {if (!source.isJumpable()) {throw new IllegalArgumentException("Require a jumpable random source");} // ...}
```

  Jumping can be used to create a series of non-overlapping generators for use in multithreaded applications. Note that there is not a one-to-one relationship between the number of output random values from a provider and the number of steps from the underlying state cycle. This is due to:

  - Possible use of rejection algorithms to output a random value using multiple values from the state cycle.
  - The number of bits required to generate a random value differing from the number of bits generated by the underlying source of randomness. For example generation of a 64-bit `long` value using a 32-bit source of randomness.

  Users are advised to use jumping generators with care to avoid overlapping output of multiple generators in parallel computations. A cautious approach is to use a jump distance far larger than the expected output length used by each generator.
- The `SplittableUniformRandomProvider` interface allows splitting a generator into two objects (the original and a new instance) each of which implements the same interface (and can be recursively split indefinitely). This can be used for parallel computations where the number of forks is unknown. These generators provide support for parallel streams. It should be noted that in general creation of a new generator instance may result in correlation of the output sequence with an existing generator. The generators that support this interface have algorithms designed to minimise correlation between instances. In particular the stream of generators provided by recursive splitting of a parallel stream are robust to collision of their sequence output.

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.SplittableUniformRandomProvider;
import org.apache.commons.rng.simple.RandomSource;

RandomSource source = RandomSource.L64_X128_MIX; // Known to be splittable.

SplittableUniformRandomProvider splittable = (SplittableUniformRandomProvider) source.create();

// For use in parallel
int streamSize = 10;
jumpable.splits(streamSize).parallel().forEach(rng -> {
    // Task using the rng
});
```

  Note that here the stream of RNGs is parallel; each RNG is used within a potentially long-running task that can run concurrently with other tasks if the enclosing stream parallel support utilises multiple threads.

  In the above example, the source is known to implement the `SplittableUniformRandomProvider` interface. Not all generators support this functionality. You can determine if a `RandomSource` is splittable without creating one using the instance method `isSplittable()`.


```
import org.apache.commons.rng.simple.RandomSource;
public void initialise(RandomSource source) {if (!source.isSplittable()) {throw new IllegalArgumentException("Require a splittable random source");} // ...}
```

- Generation of [random deviates](https://commons.apache.org/proper/commons-rng/userguide/dist_density_approx.html) for various [distributions](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/distribution/package-summary.html).

```
import org.apache.commons.rng.sampling.distribution.ContinuousSampler;
import org.apache.commons.rng.sampling.distribution.GaussianSampler;
import org.apache.commons.rng.sampling.distribution.ZigguratSampler;

ContinuousSampler sampler = GaussianSampler.of(ZigguratSampler.NormalizedGaussian.of(RandomSource.ISAAC.create()),
                                               45.6, 2.3);
double random = sampler.sample();
```


```
import org.apache.commons.rng.sampling.distribution.DiscreteSampler;
import org.apache.commons.rng.sampling.distribution.RejectionInversionZipfSampler;

DiscreteSampler sampler = RejectionInversionZipfSampler.of(RandomSource.ISAAC.create(),
                                                           5, 1.2);
int random = sampler.sample();
```

- Sampler interfaces are provided for generation of the primitive types `int`, `long`, and `double` and objects of type `T`. The `samples` method creates a stream of sample values using the Java 8 streaming API:

```
import org.apache.commons.rng.sampling.distribution.PoissonSampler;
import org.apache.commons.rng.simple.RandomSource;

double mean = 15.5;
int streamSize = 100;
int[] counts = PoissonSampler.of(RandomSource.L64_X128_MIX.create(), mean)
                             .samples(streamSize)
                             .toArray();
```


```
import org.apache.commons.rng.sampling.distribution.ZigguratSampler;
import org.apache.commons.rng.simple.RandomSource;

// Lower-truncated Normal distribution samples
double low = -1.23;
double[] samples = ZigguratSampler.NormalizedGaussian.of(RandomSource.L64_X128_MIX.create())
                                                     .samples()
                                                     .filter(x -> x > low)
                                                     .limit(100)
                                                     .toArray();
```

- The `SharedStateSampler` interface allows creation of a copy of the sampler using a new generator. The samplers share only their immutable state and can be used in parallel computations.

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.sampling.distribution.MarsagliaTsangWangDiscreteSampler;
import org.apache.commons.rng.sampling.distribution.SharedStateDiscreteSampler;
import org.apache.commons.rng.simple.RandomSource;

RandomSource source = RandomSource.XO_RO_SHI_RO_128_PP;

double[] probabilities = {0.1, 0.2, 0.3, 0.4};
SharedStateDiscreteSampler sampler1 = MarsagliaTsangWangDiscreteSampler.Enumerated.of(source.create(),
                                                                                      probabilities);

// For use in parallel
SharedStateDiscreteSampler sampler2 = sampler1.withUniformRandomProvider(source.create());
```

  All samplers support the `SharedStateSampler` interface.
- [Permutation](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/PermutationSampler.html), [Combination](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/CombinationSampler.html), [sampling from a `Collection`](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/CollectionSampler.html) and shuffling utilities.

```
import org.apache.commons.rng.sampling.PermutationSampler;
import org.apache.commons.rng.sampling.CombinationSampler;

// 3 elements from the (0, 1, 2, 3, 4, 5) tuplet.
int n = 6;
int k = 3;

// If the order of the elements matters.
PermutationSampler permutationSampler = new PermutationSampler(RandomSource.KISS.create(),
                                                               n, k);
// n! / (n - k)! = 120 permutations.
int[] permutation = permutationSampler.sample();

// If the order of the elements does not matter.
CombinationSampler combinationSampler = new CombinationSampler(RandomSource.KISS.create(),
                                                               n, k);
// n! / (k! (n - k)!) = 20 combinations.
int[] combination = combinationSampler.sample();
```


```
import java.util.HashSet;
import org.apache.commons.rng.sampling.CollectionSampler;

HashSet<String> elements = new HashSet<>();
elements.add("Apache");
elements.add("Commons");
elements.add("RNG");

CollectionSampler<String> sampler = new CollectionSampler<>(RandomSource.MWC_256.create(),
                                                            elements);
String word = sampler.sample();
```


```
import java.util.Arrays;
import java.util.List;
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.sampling.ListSampler;

List<String> list = Arrays.asList("Apache", "Commons", "RNG");

UniformRandomProvider rng = RandomSource.XO_RO_SHI_RO_128_PP.create();

// Get 2 random items
int k = 2;
List<String> sample = ListSampler.sample(rng, list, k);

// Shuffle the list
ListSampler.shuffle(rng, list)
```

- Sampling from geometric shapes: [Box](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/shape/BoxSampler.html), [Ball](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/shape/UnitBallSampler.html), [Line](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/shape/LineSampler.html), [Triangle](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/shape/TriangleSampler.html), and [Tetrahedron](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/shape/TetrahedronSampler.html).

```
import org.apache.commons.rng.sampling.shape.BoxSampler;

double[] lower = {1, 2, 3};
double[] upper = {15, 16, 17};
BoxSampler sampler = BoxSampler.of(RandomSource.KISS.create(),
                                   lower, upper);
double[] coordinate = sampler.sample();
double[][] coordinates = sampler.samples(100).toArray(double[][]::new);
```

- The [CompositeSamplers](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/CompositeSamplers.html) utility class can create a composite sampler that is a weighted combination of samplers that return the same type.

  The following example will create a sampler to uniformly sample the border of a triangle using the line segment lengths as weights:


```
import org.apache.commons.rng.sampling.shape.LineSampler;

UniformRandomProvider rng = RandomSource.JSF_64.create();

// Triangle vertices
double[] a = {1.23, 4.56};
double[] b = {6.78, 9.01};
double[] c = {3.45, 2.34};
// Line lengths
double ab = Math.hypot(a[0] - b[0], a[1] - b[1]);
double bc = Math.hypot(b[0] - c[0], b[1] - c[1]);
double ca = Math.hypot(c[0] - a[0], c[1] - a[1]);

ObjectSampler<double[]> sampler =
    CompositeSamplers.<double[]>newObjectSamplerBuilder()
        .add(LineSampler.of(rng, a, b), ab)
        .add(LineSampler.of(rng, b, c), bc)
        .add(LineSampler.of(rng, c, a), ca)
        .build(rng);

double[] coordinate = sampler.sample();
```

<a id="userguide-rng--3.-library-layout"></a>

# 3. Library layout

The API for client code consists of classes and interfaces defined in package [org.apache.commons.rng](https://commons.apache.org/proper/commons-rng/commons-rng-client-api/apidocs/org/apache/commons/rng/package-summary.html).

- Interface `UniformRandomProvider` provides access to a sequence of random values uniformly distributed within some range.
- Interfaces `RestorableUniformRandomProvider` and `RandomProviderState` provide the "save/restore" API.
- Interfaces `JumpableUniformRandomProvider`, `LongJumpableUniformRandomProvider` and `ArbitrarilyJumpableUniformRandomProvider` provide the "copy and jump" API for parallel computations. These are suitable for tasks where the number of instances to use in parallel is known.
- Interface `SplittableUniformRandomProvider` provides the "split" API for parallel computations. This is suitable for tasks where the number of instances to use in parallel is unknown, for example execution of tasks within a stream using the JDK parallelism support.

The API for instantiating generators is defined in package [org.apache.commons.rng.simple](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/package-summary.html).

- Enum `RandomSource` determines which algorithm to use for generating the sequence of random values.

The `org.apache.commons.rng.simple.internal` package contains classes for supporting initialization (a.k.a. "seeding") of the generators. They must not be used directly in applications, as all the necessary utilities are accessible through methods defined in `RandomSource`.

- `ProviderBuilder`: contains methods for instantiating the concrete RNG implementations based on the source identifier; it also takes care of calling the appropriate classes for seed type conversion.
- `SeedFactory`: contains factory methods for generating random seeds.
- `SeedConverter`: interface for classes that transform between supported seed types.
- Various classes that implement `SeedConverter` in order to transform from caller's seed to "native" seed.

The [org.apache.commons.rng.core](https://commons.apache.org/proper/commons-rng/commons-rng-core/apidocs/org/apache/commons/rng/core/package-summary.html) package contains the implementation of the algorithms for the generation of pseudo-random sequences. Applications should not directly import or use classes defined in this package: all generators can be instantiated through the `RandomSource` factory.

- Class `RandomProviderDefaultState` implements the `RandomProviderState` interface to enable "save/restore" for all `RestorableUniformRandomProvider` instances created through the `RandomSource` factory methods.
- `BaseProvider`: base class for all concrete RNG implementations; it contains higher-level algorithms `nextInt(int n)` and `nextLong(long n)` common to all implementations.
- `org.apache.commons.rng.core.util`
  - `NumberFactory`: contains utilities for interpreting and combining the output (`int` or `long`) of the underlying source of randomness into the requested output, i.e. one of the Java primitive types supported by `UniformRandomProvider`.
  - `RandomStreams`: contains utilities for generating a stream of objects created using a random seed and source of randomness.
- `org.apache.commons.rng.core.source32`
  - `RandomIntSource`: describes an algorithm that generates randomness in 32-bits chunks (a.k.a Java `int`).
  - `IntProvider`: base class for concrete classes that implement `RandomIntSource`.
  - Concrete RNG algorithms that are subclasses of `IntProvider`.
- `org.apache.commons.rng.core.source64`
  - `RandomLongSource`: describes an algorithm that generates randomness in 64-bits chunks (a.k.a Java `long`).
  - `LongProvider`: base class for concrete classes that implement `RandomLongSource`.
  - Concrete RNG algorithms that are subclasses of `LongProvider`.

<a id="userguide-rng--4.-performance"></a>

# 4. Performance

This section reports performance benchmarks of the RNG implementations. All runs were performed on a platform with the following characteristics:

- CPU: Apple M2 Max
- Java version: 21
- JVM: OpenJDK 64-Bit Server VM Homebrew (build 21.0.9, mixed mode, sharing)

Performance was measured using the [Java Micro-benchmark Harness (JMH)](http://openjdk.java.net/projects/code-tools/jmh/) and the code is provided in the [Examples](#userguide-rng--a6._examples).

Timings are representative of performance; the relative ranking of results may change depending on the JVM, operating system and hardware.

In these tables:

- The first column is the RNG identifier (see [RandomSource](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/RandomSource.html))
- *Lower* is *better*.

<a id="userguide-rng--4.1-generating-primitive-values"></a>

## 4.1 Generating primitive values

The following table indicates the performance for generating:

- a sequence of true/false values (a.k.a. Java type `boolean`)
- a sequence of 64-bit floating point numbers (a.k.a. Java type `double`)
- a sequence of 64-bit integers (a.k.a. Java type `long`)
- a sequence of 32-bit floating point numbers (a.k.a. Java type `float`)
- a sequence of 32-bit integers (a.k.a. Java type `int`)

Scores are normalized to the score of `RandomSource.JDK`.

Note that the core implementations use all the bits from the random source. For example a native generator of 32-bit `int` values requires 1 generation call per 32 `boolean` values; a native generator of 64-bit `long` values requires 1 generation call per 2 `int` values. This implementation is fast for all generators but requires a high quality random source. See the [Quality](#userguide-rng--a5._quality) section.

| RNG identifier | `boolean` | `double` | `long` | `float` | `int` |
| --- | --- | --- | --- | --- | --- |
| JDK | 1.00000 | 1.00000 | 1.00000 | 1.00000 | 1.00000 |
| WELL\_512\_A | 0.98406 | 0.39947 | 0.41063 | 0.49594 | 0.47166 |
| WELL\_1024\_A | 1.00844 | 0.37799 | 0.37230 | 0.40633 | 0.38654 |
| WELL\_19937\_A | 0.99749 | 0.43187 | 0.48963 | 0.48491 | 0.46106 |
| WELL\_19937\_C | 1.03270 | 0.49032 | 0.48756 | 0.49783 | 0.47090 |
| WELL\_44497\_A | 1.02807 | 0.46649 | 0.44125 | 0.48693 | 0.46331 |
| WELL\_44497\_B | 1.05406 | 0.50246 | 0.48431 | 0.54510 | 0.48850 |
| MT | 0.93440 | 0.24441 | 0.24019 | 0.26725 | 0.27400 |
| ISAAC | 0.96870 | 0.42654 | 0.43685 | 0.54373 | 0.51136 |
| SPLIT\_MIX\_64 | 1.09912 | 0.09394 | 0.09414 | 0.31157 | 0.29574 |
| XOR\_SHIFT\_1024\_S | 1.19090 | 0.15728 | 0.16436 | 0.15319 | 0.13644 |
| TWO\_CMRES | 1.14304 | 0.15882 | 0.16118 | 0.15503 | 0.14543 |
| MT\_64 | 1.12332 | 0.12830 | 0.13547 | 0.13100 | 0.11757 |
| MWC\_256 | 0.92903 | 0.32660 | 0.35377 | 0.46743 | 0.44503 |
| KISS | 0.89721 | 0.27929 | 0.29906 | 0.38787 | 0.39688 |
| XOR\_SHIFT\_1024\_S\_PHI | 1.21406 | 0.15735 | 0.16299 | 0.14430 | 0.13764 |
| XO\_RO\_SHI\_RO\_64\_S | 0.86964 | 0.28881 | 0.27716 | 0.35317 | 0.33174 |
| XO\_RO\_SHI\_RO\_64\_SS | 0.87965 | 0.30068 | 0.35496 | 0.37802 | 0.44112 |
| XO\_SHI\_RO\_128\_PLUS | 0.87328 | 0.22295 | 0.18769 | 0.35164 | 0.34567 |
| XO\_SHI\_RO\_128\_SS | 0.87516 | 0.25105 | 0.23422 | 0.32450 | 0.27225 |
| XO\_RO\_SHI\_RO\_128\_PLUS | 1.12940 | 0.15030 | 0.15852 | 0.14714 | 0.13403 |
| XO\_RO\_SHI\_RO\_128\_SS | 1.10529 | 0.17659 | 0.22253 | 0.15107 | 0.15285 |
| XO\_SHI\_RO\_256\_PLUS | 1.09700 | 0.13169 | 0.17398 | 0.17743 | 0.16242 |
| XO\_SHI\_RO\_256\_SS | 1.10314 | 0.14432 | 0.13481 | 0.18434 | 0.17936 |
| XO\_SHI\_RO\_512\_PLUS | 1.12281 | 0.13157 | 0.18988 | 0.14470 | 0.16157 |
| XO\_SHI\_RO\_512\_SS | 1.13177 | 0.13415 | 0.21849 | 0.17113 | 0.16460 |
| PCG\_XSH\_RR\_32 | 0.87186 | 0.18591 | 0.18147 | 0.26266 | 0.23753 |
| PCG\_XSH\_RS\_32 | 0.86321 | 0.18775 | 0.18550 | 0.27155 | 0.24805 |
| PCG\_RXS\_M\_XS\_64 | 1.10923 | 0.12366 | 0.11974 | 0.24369 | 0.23146 |
| PCG\_MCG\_XSH\_RR\_32 | 0.90426 | 0.13419 | 0.12457 | 0.24044 | 0.20793 |
| PCG\_MCG\_XSH\_RS\_32 | 0.86853 | 0.12945 | 0.12226 | 0.23505 | 0.21101 |
| MSWS | 0.97807 | 0.22247 | 0.20847 | 0.32584 | 0.31681 |
| SFC\_32 | 0.86725 | 0.22908 | 0.24208 | 0.27041 | 0.35094 |
| SFC\_64 | 1.10769 | 0.16930 | 0.17019 | 0.15732 | 0.15014 |
| JSF\_32 | 0.93478 | 0.18231 | 0.18021 | 0.35872 | 0.28842 |
| JSF\_64 | 1.12192 | 0.17763 | 0.16808 | 0.18130 | 0.16090 |
| XO\_SHI\_RO\_128\_PP | 0.90638 | 0.23333 | 0.19644 | 0.30718 | 0.34596 |
| XO\_RO\_SHI\_RO\_128\_PP | 1.08265 | 0.16797 | 0.15479 | 0.14812 | 0.21495 |
| XO\_SHI\_RO\_256\_PP | 1.09547 | 0.13462 | 0.18466 | 0.13471 | 0.11804 |
| XO\_SHI\_RO\_512\_PP | 1.11719 | 0.13308 | 0.13519 | 0.18637 | 0.12390 |
| XO\_RO\_SHI\_RO\_1024\_PP | 1.11454 | 0.11654 | 0.11859 | 0.12228 | 0.10176 |
| XO\_RO\_SHI\_RO\_1024\_S | 1.11434 | 0.11567 | 0.11981 | 0.11188 | 0.09909 |
| XO\_RO\_SHI\_RO\_1024\_SS | 1.83765 | 0.12472 | 0.12456 | 0.12780 | 0.11088 |
| PCG\_XSH\_RR\_32\_OS | 0.87458 | 0.18953 | 0.18210 | 0.26172 | 0.23733 |
| PCG\_XSH\_RS\_32\_OS | 0.87389 | 0.18785 | 0.18671 | 0.26381 | 0.24775 |
| PCG\_RXS\_M\_XS\_64\_OS | 1.09256 | 0.12434 | 0.11960 | 0.24351 | 0.22953 |
| L64\_X128\_SS | 1.19064 | 0.16720 | 0.16213 | 0.21711 | 0.21302 |
| L64\_X128\_MIX | 1.11597 | 0.18518 | 0.18237 | 0.22892 | 0.22044 |
| L64\_X256\_MIX | 1.13742 | 0.15913 | 0.19086 | 0.18938 | 0.18010 |
| L64\_X1024\_MIX | 1.13353 | 0.12702 | 0.12948 | 0.14959 | 0.12512 |
| L128\_X128\_MIX | 1.14595 | 0.20402 | 0.21031 | 0.21287 | 0.19027 |
| L128\_X256\_MIX | 1.12560 | 0.42397 | 0.20869 | 0.41922 | 0.19029 |
| L128\_X1024\_MIX | 1.20275 | 0.21251 | 0.21320 | 0.21454 | 0.40626 |
| L32\_X64\_MIX | 0.91357 | 0.31074 | 0.35720 | 0.39415 | 0.36384 |
| PHILOX\_4X32 | 1.08214 | 0.57003 | 0.40638 | 0.39130 | 0.33465 |
| PHILOX\_4X64 | 1.45384 | 0.14840 | 0.13167 | 0.17748 | 0.15659 |

Notes:

The `RandomSource.JDK` generator uses thread-safe (synchronized) `int` generation which has a performance overhead (see the `int` generation results). Note that the output will be low quality and this generator should not be used. See the [Quality](#userguide-rng--a5._quality) section for details. Multi-threaded applications should use a generator for each thread.

The speed of `boolean` generation is related to the base implementation that caches the 32-bit or 64-bit output from the generator. In these results the 32-bit generators have the better performance. These timings are relative and all implements are very fast. A RNG to compute boolean samples should be chosen based on the [quality](#userguide-rng--a5._quality) of the output.

The `RandomSource.PHILOX_4X64` generator uses multiply high methods from `java.lang.Math` if available. The `multiplyHigh` (JDK 9+) and `unsignedMultiplyHigh` (JDK 18+) significantly increase performance if the 128-bit product of two 64-bit factors is supported by hardware instructions. These results are on a platform with supported hardware.

<a id="userguide-rng--4.2-generating-gaussian-samples"></a>

## 4.2 Generating Gaussian samples

The following table compares the [BoxMullerNormalizedGaussianSampler](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/distribution/BoxMullerNormalizedGaussianSampler.html), [MarsagliaNormalizedGaussianSampler](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/distribution/MarsagliaNormalizedGaussianSampler.html), [ZigguratNormalizedGaussianSampler](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/distribution/ZigguratNormalizedGaussianSampler.html), and [ZigguratSampler.NormalizedGaussian](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/org/apache/commons/rng/sampling/distribution/ZigguratSampler.NormalizedGaussian.html).

Each score is normalized to the score of [nextGaussian()](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/random/RandomGenerator.html#nextGaussian()) method of `java.util.Random` which internally uses the Box-Muller algorithm in a synchronized method.

| RNG identifier | `BoxMullerNormalizedGaussianSampler` | `MarsagliaNormalizedGaussianSampler` | `ZigguratNormalizedGaussianSampler` | `ZigguratSampler.NormalizedGaussian` |
| --- | --- | --- | --- | --- |
| JDK | 0.68777 | 0.81843 | 0.63294 | 0.64404 |
| WELL\_512\_A | 0.75101 | 0.76327 | 0.33895 | 0.31547 |
| WELL\_1024\_A | 0.73373 | 0.77183 | 0.31694 | 0.30482 |
| WELL\_19937\_A | 0.98253 | 1.09219 | 0.39356 | 0.37716 |
| WELL\_19937\_C | 1.01706 | 1.33765 | 0.42391 | 0.41528 |
| WELL\_44497\_A | 0.94706 | 1.10975 | 0.40873 | 0.38855 |
| WELL\_44497\_B | 1.07158 | 1.45448 | 0.43492 | 0.43214 |
| MT | 0.73850 | 0.71401 | 0.22460 | 0.22366 |
| ISAAC | 0.78218 | 0.76143 | 0.34581 | 0.33332 |
| SPLIT\_MIX\_64 | 0.67904 | 0.40813 | 0.10945 | 0.09004 |
| XOR\_SHIFT\_1024\_S | 0.60941 | 0.46003 | 0.14489 | 0.13733 |
| TWO\_CMRES | 0.59634 | 0.43879 | 0.14193 | 0.13045 |
| MT\_64 | 0.64925 | 0.52747 | 0.14545 | 0.12482 |
| MWC\_256 | 0.59802 | 0.51695 | 0.18319 | 0.17699 |
| KISS | 0.70982 | 0.54934 | 0.25360 | 0.24010 |
| XOR\_SHIFT\_1024\_S\_PHI | 0.62823 | 0.47054 | 0.14687 | 0.14116 |
| XO\_RO\_SHI\_RO\_64\_S | 0.64133 | 0.49153 | 0.24208 | 0.27114 |
| XO\_RO\_SHI\_RO\_64\_SS | 0.68614 | 0.50950 | 0.24196 | 0.27433 |
| XO\_SHI\_RO\_128\_PLUS | 0.59398 | 0.40979 | 0.17945 | 0.15669 |
| XO\_SHI\_RO\_128\_SS | 0.64363 | 0.44195 | 0.19775 | 0.17960 |
| XO\_RO\_SHI\_RO\_128\_PLUS | 0.57394 | 0.36482 | 0.14416 | 0.17495 |
| XO\_RO\_SHI\_RO\_128\_SS | 0.58773 | 0.38655 | 0.15829 | 0.17833 |
| XO\_SHI\_RO\_256\_PLUS | 0.57167 | 0.36364 | 0.15275 | 0.11214 |
| XO\_SHI\_RO\_256\_SS | 0.58883 | 0.38003 | 0.13301 | 0.11511 |
| XO\_SHI\_RO\_512\_PLUS | 0.57162 | 0.37981 | 0.12786 | 0.15007 |
| XO\_SHI\_RO\_512\_SS | 0.60068 | 0.38822 | 0.16683 | 0.11567 |
| PCG\_XSH\_RR\_32 | 0.63515 | 0.43201 | 0.16654 | 0.16535 |
| PCG\_XSH\_RS\_32 | 0.62909 | 0.41471 | 0.16475 | 0.15260 |
| PCG\_RXS\_M\_XS\_64 | 0.62697 | 0.39972 | 0.12651 | 0.11403 |
| PCG\_MCG\_XSH\_RR\_32 | 0.63055 | 0.42255 | 0.13217 | 0.12350 |
| PCG\_MCG\_XSH\_RS\_32 | 0.61018 | 0.39879 | 0.12573 | 0.11380 |
| MSWS | 0.63346 | 0.43842 | 0.19578 | 0.18195 |
| SFC\_32 | 0.60542 | 0.42090 | 0.22415 | 0.21120 |
| SFC\_64 | 0.55247 | 0.37325 | 0.15304 | 0.10980 |
| JSF\_32 | 0.58862 | 0.41063 | 0.21022 | 0.17664 |
| JSF\_64 | 0.55953 | 0.37250 | 0.15263 | 0.11131 |
| XO\_SHI\_RO\_128\_PP | 0.62308 | 0.43179 | 0.18214 | 0.16867 |
| XO\_RO\_SHI\_RO\_128\_PP | 0.58869 | 0.37695 | 0.14941 | 0.18867 |
| XO\_SHI\_RO\_256\_PP | 0.62218 | 0.40224 | 0.17566 | 0.13831 |
| XO\_SHI\_RO\_512\_PP | 0.63007 | 0.38958 | 0.13534 | 0.16165 |
| XO\_RO\_SHI\_RO\_1024\_PP | 0.59214 | 0.43627 | 0.12489 | 0.11273 |
| XO\_RO\_SHI\_RO\_1024\_S | 0.55932 | 0.41749 | 0.12111 | 0.10776 |
| XO\_RO\_SHI\_RO\_1024\_SS | 0.58143 | 0.43408 | 0.13265 | 0.11737 |
| PCG\_XSH\_RR\_32\_OS | 0.63783 | 0.43019 | 0.16740 | 0.16241 |
| PCG\_XSH\_RS\_32\_OS | 0.61018 | 0.40376 | 0.16254 | 0.15108 |
| PCG\_RXS\_M\_XS\_64\_OS | 0.62263 | 0.39527 | 0.12241 | 0.10696 |
| L64\_X128\_SS | 0.61355 | 0.39603 | 0.19675 | 0.18417 |
| L64\_X128\_MIX | 0.71570 | 0.43616 | 0.20192 | 0.19443 |
| L64\_X256\_MIX | 0.67443 | 0.43273 | 0.14705 | 0.17261 |
| L64\_X1024\_MIX | 0.62038 | 0.49208 | 0.14579 | 0.12868 |
| L128\_X128\_MIX | 0.75821 | 0.57463 | 0.20535 | 0.18531 |
| L128\_X256\_MIX | 0.76666 | 0.56904 | 0.21025 | 0.18677 |
| L128\_X1024\_MIX | 0.65788 | 0.58239 | 0.22308 | 0.19761 |
| L32\_X64\_MIX | 0.74795 | 0.55989 | 0.25632 | 0.27548 |
| PHILOX\_4X32 | 1.08207 | 1.07704 | 0.38838 | 0.37289 |
| PHILOX\_4X64 | 0.91379 | 0.91941 | 0.26007 | 0.24542 |

Notes:

The reference `java.util.Random` nextGaussian() method uses synchronized method calls per sample. The `RandomSource.JDK` RNG will use synchronized method calls when generating numbers for the `BoxMullerNormalizedGaussianSampler` but the calls to obtain the samples are not synchronized, hence the observed difference. All the other RNGs are not synchronized.

The `RandomSource.PHILOX_4X64` generator uses multiply high methods from `java.lang.Math` if available. The `multiplyHigh` (JDK 9+) and `unsignedMultiplyHigh` (JDK 18+) significantly increase performance if the 128-bit product of two 64-bit factors is supported by hardware instructions. These results are on a platform with supported hardware.

<a id="userguide-rng--5.-quality"></a>

# 5. Quality

This section reports results of [performing "stress tests"](https://commons.apache.org/proper/commons-rng/commons-rng-examples/apidocs/org/apache/commons/rng/examples/stress/package-summary.html) that aim at detecting failures of an implementation to produce sequences of numbers that follow a uniform distribution.

Three different test suites were used:

- [Dieharder v3.31.1](http://www.phy.duke.edu/~rgb/General/dieharder.php)
- [PractRand v0.94](http://pracrand.sourceforge.net/)
- [TestU01 v1.2.3](http://simul.iro.umontreal.ca/testu01/tu01.html)

Note that the *Dieharder* and *TestU01* test suites accept 32-bit integer values. Any generator of 64-bit `long` values has the upper and lower 32-bits passed to the test suite. *PractRand* supports 64-bit generators.

The first column is the RNG identifier (see [RandomSource](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/org/apache/commons/rng/simple/RandomSource.html)). The remaining columns contain the results of separate runs of the test suite using different random seeds. Click on one of the entries of the comma-separated list in order to see the text report of the corresponding run.

The *Dieharder* and *TestU01* test suites contain many tests each requiring an approximately fixed size of random output; in the case of multiple tests different output is used for each test. *Dieharder* was run using the full set of tests. *TestU01* was run using BigCrush. The number in the table indicates the number of failed tests, i.e. tests reported as below the accepted threshold for considering the sequence as uniformly random; hence *lower* is *better*. Note: For *Dieharder* the flawed "Diehard Sums Test" is [ignored](http://www.phy.duke.edu/~rgb/General/dieharder.php) from the failure counts.

*PractRand* tests a length of the RNG output with all the selected tests; this is repeated with doubling lengths until a failure is detected or the maximum size is reached. *PractRand* was run using the core tests and smart folding. This is the default mode and comprises tests with little overlap in their characteristics and additional targeting testing of the lower bits of the output sequence. The limit for these results was 4 terabytes (4 TiB). A number in the table indicates the size in bytes of output where a failure occurred expressed as an exponent of 2; hence *higher* is *better*. A dash (*-*) indicates no failure and is *best*.

Spurious failures are a failure in a single run of the test suite. These are to be expected as the tests use probability thresholds to determine if the output is non-random. Systematic failures where the RNG fails the same test in every run indicate a problem with the RNG output. The count of systematic failures for *Dieharder* and *TestU01* are shown in parentheses. The maximum output at which a failure always occurs for *PractRand* is shown in parentheses.

Any RNG with *no systematic failures* is highlighted in **bold**. Note that some RNGs fail *PractRand* on tests which target the lower bits. These are not suitable as all purpose generators but have utility in floating-point number generation where the lower bits are not used.

| RNG identifier | Dieharder | TestU01 (BigCrush) | PractRand |
| --- | --- | --- | --- |
| JDK | [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_1_1), [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_1_2), [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_1_3), [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_1_4), [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_1_5) (4) | [50](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_1_1), [51](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_1_2), [52](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_1_3), [49](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_1_4), [51](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_1_5) (48) | [20](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_1_1), [20](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_1_2), [20](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_1_3) (1 MiB) |
| WELL\_512\_A | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_2_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_2_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_2_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_2_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_2_5) | [6](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_2_1), [7](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_2_2), [8](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_2_3), [6](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_2_4), [6](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_2_5) (6) | [24](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_2_1), [24](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_2_2), [24](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_2_3) (16 MiB) |
| WELL\_1024\_A | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_3_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_3_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_3_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_3_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_3_5) | [5](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_3_1), [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_3_2), [5](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_3_3), [5](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_3_4), [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_3_5) (4) | [27](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_3_1), [27](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_3_2), [27](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_3_3) (128 MiB) |
| WELL\_19937\_A | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_4_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_4_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_4_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_4_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_4_5) | [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_4_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_4_2), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_4_3), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_4_4), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_4_5) (2) | [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_4_1), [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_4_2), [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_4_3) (512 GiB) |
| WELL\_19937\_C | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_5_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_5_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_5_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_5_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_5_5) | [4](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_5_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_5_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_5_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_5_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_5_5) (2) | [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_5_1), [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_5_2), [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_5_3) (512 GiB) |
| WELL\_44497\_A | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_6_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_6_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_6_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_6_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_6_5) | [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_6_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_6_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_6_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_6_4), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_6_5) (2) | [42](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_6_1), [42](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_6_2), [42](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_6_3) (4 TiB) |
| WELL\_44497\_B | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_7_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_7_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_7_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_7_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_7_5) | [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_7_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_7_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_7_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_7_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_7_5) (2) | [42](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_7_1), [42](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_7_2), [42](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_7_3) (4 TiB) |
| MT | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_8_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_8_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_8_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_8_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_8_5) | [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_8_1), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_8_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_8_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_8_4), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_8_5) (2) | [38](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_8_1), [38](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_8_2), [38](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_8_3) (256 GiB) |
| **ISAAC** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_9_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_9_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_9_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_9_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_9_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_9_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_9_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_9_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_9_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_9_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_9_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_9_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_9_3) |
| **SPLIT\_MIX\_64** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_10_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_10_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_10_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_10_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_10_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_10_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_10_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_10_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_10_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_10_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_10_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_10_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_10_3) |
| XOR\_SHIFT\_1024\_S | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_11_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_11_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_11_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_11_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_11_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_11_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_11_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_11_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_11_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_11_5) | [31](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_11_1), [31](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_11_2), [31](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_11_3) (2 GiB) |
| TWO\_CMRES | [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_12_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_12_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_12_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_12_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_12_5) (2) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_12_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_12_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_12_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_12_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_12_5) | [32](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_12_1), [32](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_12_2), [32](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_12_3) (4 GiB) |
| MT\_64 | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_14_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_14_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_14_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_14_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_14_5) | [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_14_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_14_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_14_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_14_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_14_5) (2) | [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_14_1), [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_14_2), [39](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_14_3) (512 GiB) |
| **MWC\_256** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_15_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_15_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_15_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_15_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_15_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_15_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_15_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_15_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_15_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_15_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_15_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_15_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_15_3) |
| **KISS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_16_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_16_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_16_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_16_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_16_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_16_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_16_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_16_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_16_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_16_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_16_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_16_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_16_3) |
| XOR\_SHIFT\_1024\_S\_PHI | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_17_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_17_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_17_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_17_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_17_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_17_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_17_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_17_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_17_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_17_5) | [33](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_17_1), [33](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_17_2), [33](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_17_3) (8 GiB) |
| XO\_RO\_SHI\_RO\_64\_S | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_18_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_18_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_18_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_18_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_18_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_18_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_18_2), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_18_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_18_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_18_5) (1) | [21](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_18_1), [21](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_18_2), [21](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_18_3) (2 MiB) |
| **XO\_RO\_SHI\_RO\_64\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_19_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_19_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_19_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_19_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_19_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_19_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_19_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_19_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_19_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_19_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_19_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_19_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_19_3) |
| XO\_SHI\_RO\_128\_PLUS | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_20_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_20_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_20_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_20_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_20_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_20_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_20_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_20_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_20_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_20_5) | [24](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_20_1), [24](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_20_2), [24](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_20_3) (16 MiB) |
| **XO\_SHI\_RO\_128\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_21_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_21_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_21_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_21_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_21_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_21_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_21_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_21_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_21_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_21_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_21_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_21_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_21_3) |
| XO\_RO\_SHI\_RO\_128\_PLUS | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_22_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_22_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_22_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_22_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_22_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_22_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_22_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_22_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_22_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_22_5) | [25](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_22_1), [25](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_22_2), [25](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_22_3) (32 MiB) |
| **XO\_RO\_SHI\_RO\_128\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_23_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_23_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_23_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_23_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_23_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_23_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_23_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_23_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_23_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_23_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_23_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_23_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_23_3) |
| XO\_SHI\_RO\_256\_PLUS | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_24_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_24_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_24_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_24_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_24_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_24_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_24_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_24_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_24_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_24_5) | [27](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_24_1), [27](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_24_2), [27](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_24_3) (128 MiB) |
| **XO\_SHI\_RO\_256\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_25_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_25_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_25_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_25_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_25_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_25_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_25_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_25_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_25_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_25_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_25_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_25_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_25_3) |
| XO\_SHI\_RO\_512\_PLUS | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_26_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_26_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_26_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_26_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_26_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_26_1), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_26_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_26_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_26_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_26_5) | [30](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_26_1), [30](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_26_2), [30](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_26_3) (1 GiB) |
| **XO\_SHI\_RO\_512\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_27_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_27_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_27_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_27_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_27_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_27_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_27_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_27_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_27_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_27_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_27_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_27_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_27_3) |
| **PCG\_XSH\_RR\_32** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_28_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_28_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_28_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_28_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_28_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_28_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_28_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_28_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_28_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_28_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_28_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_28_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_28_3) |
| **PCG\_XSH\_RS\_32** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_29_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_29_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_29_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_29_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_29_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_29_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_29_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_29_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_29_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_29_5) | [41](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_29_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_29_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_29_3) |
| **PCG\_RXS\_M\_XS\_64** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_30_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_30_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_30_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_30_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_30_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_30_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_30_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_30_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_30_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_30_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_30_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_30_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_30_3) |
| **PCG\_MCG\_XSH\_RR\_32** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_31_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_31_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_31_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_31_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_31_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_31_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_31_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_31_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_31_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_31_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_31_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_31_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_31_3) |
| PCG\_MCG\_XSH\_RS\_32 | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_32_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_32_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_32_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_32_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_32_5) | [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_32_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_32_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_32_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_32_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_32_5) | [40](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_32_1), [41](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_32_2), [41](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_32_3) (2 TiB) |
| **MSWS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_33_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_33_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_33_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_33_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_33_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_33_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_33_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_33_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_33_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_33_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_33_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_33_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_33_3) |
| **SFC\_32** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_34_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_34_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_34_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_34_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_34_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_34_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_34_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_34_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_34_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_34_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_34_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_34_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_34_3) |
| **SFC\_64** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_35_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_35_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_35_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_35_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_35_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_35_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_35_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_35_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_35_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_35_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_35_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_35_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_35_3) |
| **JSF\_32** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_36_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_36_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_36_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_36_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_36_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_36_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_36_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_36_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_36_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_36_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_36_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_36_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_36_3) |
| **JSF\_64** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_37_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_37_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_37_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_37_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_37_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_37_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_37_2), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_37_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_37_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_37_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_37_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_37_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_37_3) |
| **XO\_SHI\_RO\_128\_PP** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_38_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_38_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_38_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_38_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_38_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_38_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_38_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_38_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_38_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_38_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_38_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_38_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_38_3) |
| **XO\_RO\_SHI\_RO\_128\_PP** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_39_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_39_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_39_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_39_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_39_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_39_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_39_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_39_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_39_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_39_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_39_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_39_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_39_3) |
| **XO\_SHI\_RO\_256\_PP** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_40_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_40_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_40_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_40_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_40_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_40_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_40_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_40_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_40_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_40_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_40_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_40_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_40_3) |
| **XO\_SHI\_RO\_512\_PP** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_41_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_41_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_41_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_41_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_41_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_41_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_41_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_41_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_41_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_41_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_41_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_41_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_41_3) |
| **XO\_RO\_SHI\_RO\_1024\_PP** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_42_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_42_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_42_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_42_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_42_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_42_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_42_2), [3](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_42_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_42_4), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_42_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_42_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_42_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_42_3) |
| XO\_RO\_SHI\_RO\_1024\_S | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_43_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_43_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_43_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_43_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_43_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_43_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_43_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_43_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_43_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_43_5) | [33](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_43_1), [33](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_43_2), [33](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_43_3) (8 GiB) |
| **XO\_RO\_SHI\_RO\_1024\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_44_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_44_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_44_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_44_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_44_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_44_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_44_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_44_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_44_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_44_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_44_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_44_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_44_3) |
| **PCG\_XSH\_RR\_32\_OS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_45_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_45_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_45_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_45_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_45_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_45_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_45_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_45_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_45_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_45_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_45_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_45_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_45_3) |
| **PCG\_XSH\_RS\_32\_OS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_46_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_46_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_46_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_46_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_46_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_46_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_46_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_46_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_46_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_46_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_46_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_46_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_46_3) |
| **PCG\_RXS\_M\_XS\_64\_OS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_47_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_47_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_47_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_47_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_47_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_47_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_47_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_47_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_47_4), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_47_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_47_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_47_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_47_3) |
| **L64\_X128\_SS** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_48_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_48_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_48_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_48_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_48_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_48_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_48_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_48_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_48_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_48_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_48_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_48_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_48_3) |
| **L64\_X128\_MIX** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_49_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_49_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_49_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_49_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_49_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_49_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_49_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_49_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_49_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_49_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_49_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_49_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_49_3) |
| **L64\_X256\_MIX** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_50_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_50_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_50_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_50_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_50_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_50_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_50_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_50_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_50_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_50_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_50_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_50_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_50_3) |
| **L64\_X1024\_MIX** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_51_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_51_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_51_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_51_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_51_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_51_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_51_2), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_51_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_51_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_51_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_51_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_51_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_51_3) |
| **L128\_X128\_MIX** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_52_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_52_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_52_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_52_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_52_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_52_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_52_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_52_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_52_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_52_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_52_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_52_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_52_3) |
| **L128\_X256\_MIX** | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_53_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_53_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_53_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_53_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_53_5) | [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_53_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_53_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_53_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_53_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_53_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_53_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_53_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_53_3) |
| **L128\_X1024\_MIX** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_54_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_54_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_54_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_54_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_54_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_54_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_54_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_54_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_54_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_54_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_54_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_54_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_54_3) |
| **L32\_X64\_MIX** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_55_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_55_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_55_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_55_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_55_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_55_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_55_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_55_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_55_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_55_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_55_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_55_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_55_3) |
| **PHILOX\_4X32** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_56_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_56_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_56_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_56_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_56_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_56_1), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_56_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_56_3), [1](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_56_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_56_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_56_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_56_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_56_3) |
| **PHILOX\_4X64** | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_57_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_57_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_57_3), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_57_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/dh_57_5) | [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_57_1), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_57_2), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_57_3), [2](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_57_4), [0](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/tu_57_5) | [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_57_1), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_57_2), [-](https://commons.apache.org/proper/commons-rng/txt/userguide/stress/pr_57_3) |

<a id="userguide-rng--6.-examples"></a>

# 6. Examples

The [source distribution](https://commons.apache.org/rng/download_rng.cgi) for Apache Commons RNG contains example applications to demonstrate functionality of the library. These are contained in the following modules:

| Example Module | Description |
| --- | --- |
| Stress | Application for calling external tools that perform stringent uniformity tests. This application is used to generate results in the [Quality](#userguide-rng--a5._quality) section. |
| Sampling | Application producing output from distribution samplers to create an approximate probability density function (PDF) as shown [here](https://commons.apache.org/proper/commons-rng/userguide/dist_density_approx.html). |
| Quadrature | Application for computing numerical quadrature by Monte-Carlo (random) integration. |
| JMH | Benchmarks that assess the performance of the generators using the Java Microbenchmark Harness. This application is used to generate results in the [Performance](#userguide-rng--a4._performance) section. |
| JPMS | Example JPMS application using all the JPMS modules of Commons RNG (requires Java 11+). |

The examples require Java 8+ unless specifed as requiring a higher version.

The examples can be built using profiles in the relevant module. For example to build the JMH benchmarks application and show the help information:

```
cd commons-rng-examples/examples-jmh
mvn package -P examples-jmh
java -jar target/examples-jmh.jar -h
```

Details of each example module is contained in a `HOWTO.md` document in the module directory.

<a id="userguide-rng--7.-release-compatibility"></a>

# 7. Release compatibility

Apache Commons RNG will maintain binary compatibility within a major release number. However the *output* from a random generator *may differ* between releases. This is a functional compatibility change. The result is that when upgrading the library any code based on a random generator may produce different results. For example any unit test code written with a fixed seed to generate pseudo-random test data may fail after update as the test data has changed.

The library generators are algorithms that produce a stream of random bits using 32-bit or 64-bit integer output. The output from the primary type will maintain functional compatibility for the lifetime of the library. This output is tested to match a reference implementation of the algorithm and should be invariant. The only exception is to address bug fixes identified in the upstream implementation.

The primary output of the generator is used to produced derived types, for example floating point values, byte arrays and integers within a range. The output for derived types is not subject to functional compatibility constraints. Put simply the output from a generator may be different even when using the same starting seed due to updates to generation algorithms that use the underlying stream of random bits. Any library changes that result in a functional compatibility should be recorded in the release notes.

The library is provided as modules. It is recommended to explicitly include all required RNG modules in a project using the same version number. This will avoid version mismatch occurring between modules due to transitive dependencies; specifically this avoids using an alternative version number explicitly specified in the dependency tree. A [Bill of Materials](#commons-rng-bom) (BOM) is provided to ease [dependency management](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#bill-of-materials-bom-poms).

<a id="userguide-rng--8.-dependencies"></a>

# 8. Dependencies

Apache Commons RNG requires JDK 1.8+ and has no runtime dependencies.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/project-info.html -->

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons RNG project provides pure-Java implementation of pseudo-random generators. |
| [Summary](#summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-rng/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-rng/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-rng/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-rng/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-rng/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-rng/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-rng/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/summary.html -->

<!-- page_index: 7 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG |
| Description | The Apache Commons RNG project provides pure-Java implementation of pseudo-random generators. |
| Homepage | [https://commons.apache.org/proper/commons-rng/](#index) |

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
| ArtifactId | commons-rng-parent |
| Version | 1.7 |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/modules.html -->

<!-- page_index: 8 -->

<a id="modules--project-modules"></a>

# Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons RNG Client API](#commons-rng-client-api) | API for client code that uses random numbers generators. |
| [Apache Commons RNG Core](#commons-rng-core) | Pure Java implementations of random numbers generator algorithms. Code in this module should not be used directly by applications; please use the client interface defined in module "commons-rng-client-api" and the factory methods defined in module "commons-rng-simple". In a future release, modularization may be enforced through JPMS access restrictions. |
| [Apache Commons RNG Simple](#commons-rng-simple) | Simple API for instantiating random numbers generators. |
| [Apache Commons RNG Sampling](#commons-rng-sampling) | The Apache Commons RNG Sampling module provides samplers for various distributions. |
| [Apache Commons RNG (Bill of Materials)](#commons-rng-bom) | Bill of Materials (BOM) to aid in dependency management when referencing multiple Apache Commons RNG artifacts. |
| [Apache Commons RNG Documentation](#commons-rng-docs) | Aggregator module to genenerate Apache Commons RNG documentation. |
| [Apache Commons RNG Examples](#commons-rng-examples) | Examples of use of the "Commons RNG" library. Codes in this module and its sub-modules are not part of the library. They provide checking, benchmarking tools to enhance the documentation and to help ensure correctness of the implementations. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/team.html -->

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
| ![](assets/images/00000000000000000000000000000000_c3729f0e3a7532f1.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_c3729f0e3a7532f1.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_c3729f0e3a7532f1.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/scm.html -->

<!-- page_index: 10 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/ci-management.html -->

<!-- page_index: 11 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-docs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-docs/index.html -->

<!-- page_index: 12 -->

<a id="commons-rng-docs--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.

Browse the [Javadoc](https://commons.apache.org/proper/commons-rng/commons-rng-docs/apidocs/index.html) for more information.

---

<a id="commons-rng-bom"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-bom/index.html -->

<!-- page_index: 13 -->

<a id="commons-rng-bom--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.
Utilities are provided for sampling from distributions, collections and geometric shapes.

The Bill of Materials (BOM) is provided to aid in
[dependency management](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#bill-of-materials-bom-poms)
of the Apache Commons RNG modules.

The BOM can be imported into a Maven pom to manage the module versions:

```xml

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-rng-bom</artifactId>
      <version>1.7</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

---

<a id="commons-rng-simple"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-simple/index.html -->

<!-- page_index: 14 -->

<a id="commons-rng-simple--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.

The "simple" module contains factory methods for easy instantiation of the
generation algorithms implemented in the "commons-rng-core" module.

Example:

```
import org.apache.commons.rng.UniformRandomProvider; import org.apache.commons.rng.simple.RandomSource;
public class Dice {private final UniformRandomProvider rng = RandomSource.XO_RO_SHI_RO_128_PP.create();
public int roll() {return 1 + rng.nextInt(6);}}
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-rng/commons-rng-simple/apidocs/index.html) for more information.

---

<a id="commons-rng-client-api"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-client-api/index.html -->

<!-- page_index: 15 -->

<a id="commons-rng-client-api--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.

The "client API" module contains the code that defines the API for client code.

Example:

```
import org.apache.commons.rng.UniformRandomProvider;
public class Dice {public int roll(UniformRandomProvider rng) {// Sample in [1, 6] return rng.nextInt(1, 7);}}
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-rng/commons-rng-client-api/apidocs/index.html) to see the complete API.

---

<a id="commons-rng-sampling"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-sampling/index.html -->

<!-- page_index: 16 -->

<a id="commons-rng-sampling--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.

The "sampling" module contains classes to generate samples that follow the statistics
of a given distribution.

Example:

```
import org.apache.commons.rng.UniformRandomProvider; import org.apache.commons.rng.sampling.distribution.ContinuousSampler; import org.apache.commons.rng.sampling.distribution.ZigguratSampler.Gaussian;
public class NormalDeviates {private final ContinuousSampler normalizedGaussian;
public NormalDeviates(UniformRandomProvider rng) {normalizedGaussian = ZigguratSampler.Gaussian.of(rng);}
public double sample(double mean,double sigma) {return mean + sigma * normalizedGaussian.sample();}}
```

Utilities are provided to sample from generic collections.

Example:

```
import org.apache.commons.rng.UniformRandomProvider;
import java.util.HashSet;
import org.apache.commons.rng.sampling.CollectionSampler;

HashSet<String> elements = new HashSet<>();
elements.add("Apache");
elements.add("Commons");
elements.add("RNG");

CollectionSampler<String> sampler = new CollectionSampler<>(RandomSource.MWC_256.create(),
                                                            elements);
String word = sampler.sample();
```

The module also contains classes to generate coordinate samples from geometric shapes
such as inside a ball, box or triangle or on the surface of a sphere.

Example:

```
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.sampling.UnitSphereSampler;

int dimension = 3;
UnitSphereSampler sampler = UnitSphereSampler.of(dimension, RandomSource.KISS.create());

double[] vector = sampler.sample();
```

Browse the [Javadoc](https://commons.apache.org/proper/commons-rng/commons-rng-sampling/apidocs/index.html) for more information.

---

<a id="commons-rng-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-core/index.html -->

<!-- page_index: 17 -->

<a id="commons-rng-core--apache-commons-rng:-random-numbers-generators"></a>

# Apache Commons RNG: Random Numbers Generators

Commons RNG provides implementations of pseudo-random numbers generators that are
faster; of higher quality; and/or of a longer period than
`java.util.Random` and `java.util.SplittableRandom`.

The "core" module contains pure Java implementations of algorithms that generate
pseudo-random sequences of numbers.

**This module is not intended for direct use by applications.**
For instantiating a generator, application developers are advised to use the
factory methods provided by the "commons-rng-simple" module.

The [Javadoc](https://commons.apache.org/proper/commons-rng/commons-rng-core/apidocs/index.html) is available for the benefit of
developers who would like to contribute to this library.

---

<a id="commons-rng-bom-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-bom/ci-management.html -->

<!-- page_index: 18 -->

<a id="commons-rng-bom-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-bom-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-bom-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-bom-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-bom/scm.html -->

<!-- page_index: 19 -->

<a id="commons-rng-bom-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-bom-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-bom
```

<a id="commons-rng-bom-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-bom-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-bom-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-bom-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-bom/summary.html -->

<!-- page_index: 20 -->

<a id="commons-rng-bom-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-bom-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG (Bill of Materials) |
| Description | Bill of Materials (BOM) to aid in dependency management when referencing multiple Apache Commons RNG artifacts. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-bom/](#commons-rng-bom) |

<a id="commons-rng-bom-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-bom-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-bom |
| Version | 1.7 |
| Type | pom |

---

<a id="commons-rng-bom-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-bom/team.html -->

<!-- page_index: 21 -->

<a id="commons-rng-bom-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-bom-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_e49f09ab86cafbb3.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_e49f09ab86cafbb3.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_e49f09ab86cafbb3.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-bom-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-client-api-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-client-api/ci-management.html -->

<!-- page_index: 22 -->

<a id="commons-rng-client-api-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-client-api-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-client-api-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-client-api-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-client-api/scm.html -->

<!-- page_index: 23 -->

<a id="commons-rng-client-api-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-client-api-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-client-api
```

<a id="commons-rng-client-api-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-client-api-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-client-api-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-client-api-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-client-api/summary.html -->

<!-- page_index: 24 -->

<a id="commons-rng-client-api-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-client-api-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Client API |
| Description | API for client code that uses random numbers generators. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-client-api/](#commons-rng-client-api) |

<a id="commons-rng-client-api-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-client-api-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-client-api |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-client-api-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-client-api/team.html -->

<!-- page_index: 25 -->

<a id="commons-rng-client-api-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-client-api-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_bef7f65cbec81877.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_bef7f65cbec81877.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_bef7f65cbec81877.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-client-api-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-core-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-core/ci-management.html -->

<!-- page_index: 26 -->

<a id="commons-rng-core-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-core-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-core-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-core-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-core/scm.html -->

<!-- page_index: 27 -->

<a id="commons-rng-core-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-core-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-core
```

<a id="commons-rng-core-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-core-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-core-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-core-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-core/summary.html -->

<!-- page_index: 28 -->

<a id="commons-rng-core-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-core-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Core |
| Description | Pure Java implementations of random numbers generator algorithms. Code in this module should not be used directly by applications; please use the client interface defined in module "commons-rng-client-api" and the factory methods defined in module "commons-rng-simple". In a future release, modularization may be enforced through JPMS access restrictions. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-core/](#commons-rng-core) |

<a id="commons-rng-core-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-core-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-core |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-core-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-core/team.html -->

<!-- page_index: 29 -->

<a id="commons-rng-core-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-core-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_85ff94a79d2c0141.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_85ff94a79d2c0141.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_85ff94a79d2c0141.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-core-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-docs-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-docs/ci-management.html -->

<!-- page_index: 30 -->

<a id="commons-rng-docs-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-docs-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-docs-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-docs-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-docs/scm.html -->

<!-- page_index: 31 -->

<a id="commons-rng-docs-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-docs-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-docs
```

<a id="commons-rng-docs-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-docs-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-docs-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-docs-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-docs/summary.html -->

<!-- page_index: 32 -->

<a id="commons-rng-docs-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-docs-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Documentation |
| Description | Aggregator module to genenerate Apache Commons RNG documentation. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-docs/](#commons-rng-docs) |

<a id="commons-rng-docs-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-docs-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-docs |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-docs-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-docs/team.html -->

<!-- page_index: 33 -->

<a id="commons-rng-docs-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-docs-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_8217e983baf31a48.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_8217e983baf31a48.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_8217e983baf31a48.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-docs-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-examples-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/ci-management.html -->

<!-- page_index: 34 -->

<a id="commons-rng-examples-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-examples-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-examples-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-examples-commons-rng-examples-jmh-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jmh/ci-management.html -->

<!-- page_index: 35 -->

<a id="commons-rng-examples-commons-rng-examples-jmh-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-examples-commons-rng-examples-jmh-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-examples-commons-rng-examples-jmh-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-examples-commons-rng-examples-jmh"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jmh/index.html -->

<!-- page_index: 36 -->

<a id="commons-rng-examples-commons-rng-examples-jmh--about-apache-commons-rng-jmh-benchmark"></a>

# About Apache Commons RNG JMH Benchmark

Code for running JMH benchmarks that assess the performance of the generators.
Code in this module is not part of the public API.

---

<a id="commons-rng-examples-commons-rng-examples-jmh-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jmh/scm.html -->

<!-- page_index: 37 -->

<a id="commons-rng-examples-commons-rng-examples-jmh-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-examples-commons-rng-examples-jmh-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-examples/commons-rng-examples-jmh
```

<a id="commons-rng-examples-commons-rng-examples-jmh-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-jmh-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-jmh-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-examples-commons-rng-examples-jmh-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jmh/summary.html -->

<!-- page_index: 38 -->

<a id="commons-rng-examples-commons-rng-examples-jmh-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-examples-commons-rng-examples-jmh-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG JMH Benchmark |
| Description | Code for running JMH benchmarks that assess the performance of the generators. Code in this module is not part of the public API. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jmh/](#commons-rng-examples-commons-rng-examples-jmh) |

<a id="commons-rng-examples-commons-rng-examples-jmh-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-examples-commons-rng-examples-jmh-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-examples-jmh |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-examples-commons-rng-examples-jmh-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jmh/team.html -->

<!-- page_index: 39 -->

<a id="commons-rng-examples-commons-rng-examples-jmh-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-examples-commons-rng-examples-jmh-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_004fab36f8815290.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_004fab36f8815290.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_004fab36f8815290.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-examples-commons-rng-examples-jmh-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-examples-commons-rng-examples-jpms-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/ci-management.html -->

<!-- page_index: 40 -->

<a id="commons-rng-examples-commons-rng-examples-jpms-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-examples-commons-rng-examples-jpms-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-examples-commons-rng-examples-jpms-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-examples-commons-rng-examples-jpms"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/index.html -->

<!-- page_index: 41 -->

<a id="commons-rng-examples-commons-rng-examples-jpms--about-apache-commons-rng-jpms-integration-test"></a>

# About Apache Commons RNG JPMS Integration Test

Testing JPMS. Code in this module is not part of the public API.

<a id="commons-rng-examples-commons-rng-examples-jpms--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons RNG JPMS Module Example (Library)](https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/commons-rng-examples-jpms-lib/index.html) | Testing JPMS. Code in this module is not part of the public API. |
| [Apache Commons RNG JPMS Module Example (Application)](https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/commons-rng-examples-jpms-app/index.html) | Testing JPMS. Code in this module is not part of the public API. |

---

<a id="commons-rng-examples-commons-rng-examples-jpms-modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/modules.html -->

<!-- page_index: 42 -->

<a id="commons-rng-examples-commons-rng-examples-jpms-modules--project-modules"></a>

# Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons RNG JPMS Module Example (Library)](https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/commons-rng-examples-jpms-lib/index.html) | Testing JPMS. Code in this module is not part of the public API. |
| [Apache Commons RNG JPMS Module Example (Application)](https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/commons-rng-examples-jpms-app/index.html) | Testing JPMS. Code in this module is not part of the public API. |

---

<a id="commons-rng-examples-commons-rng-examples-jpms-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/scm.html -->

<!-- page_index: 43 -->

<a id="commons-rng-examples-commons-rng-examples-jpms-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-examples-commons-rng-examples-jpms-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-examples/commons-rng-examples-jpms
```

<a id="commons-rng-examples-commons-rng-examples-jpms-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-jpms-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-jpms-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-examples-commons-rng-examples-jpms-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/summary.html -->

<!-- page_index: 44 -->

<a id="commons-rng-examples-commons-rng-examples-jpms-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-examples-commons-rng-examples-jpms-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG JPMS Integration Test |
| Description | Testing JPMS. Code in this module is not part of the public API. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/](#commons-rng-examples-commons-rng-examples-jpms) |

<a id="commons-rng-examples-commons-rng-examples-jpms-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-examples-commons-rng-examples-jpms-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-examples-jpms |
| Version | 1.7 |
| Type | pom |

---

<a id="commons-rng-examples-commons-rng-examples-jpms-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-jpms/team.html -->

<!-- page_index: 45 -->

<a id="commons-rng-examples-commons-rng-examples-jpms-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-examples-commons-rng-examples-jpms-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_740a1ab93e2976ca.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_740a1ab93e2976ca.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_740a1ab93e2976ca.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-examples-commons-rng-examples-jpms-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-examples-commons-rng-examples-quadrature-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-quadrature/ci-management.html -->

<!-- page_index: 46 -->

<a id="commons-rng-examples-commons-rng-examples-quadrature-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-examples-commons-rng-examples-quadrature-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-examples-commons-rng-examples-quadrature-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-examples-commons-rng-examples-quadrature"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-quadrature/index.html -->

<!-- page_index: 47 -->

<a id="commons-rng-examples-commons-rng-examples-quadrature--about-apache-commons-rng-quadrature-example"></a>

# About Apache Commons RNG Quadrature Example

Contains examples for computing numerical quadrature (integration).
Code in this module is not part of the public API.

---

<a id="commons-rng-examples-commons-rng-examples-quadrature-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-quadrature/scm.html -->

<!-- page_index: 48 -->

<a id="commons-rng-examples-commons-rng-examples-quadrature-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-examples-commons-rng-examples-quadrature-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-examples/commons-rng-examples-quadrature
```

<a id="commons-rng-examples-commons-rng-examples-quadrature-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-quadrature-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-quadrature-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-examples-commons-rng-examples-quadrature-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-quadrature/summary.html -->

<!-- page_index: 49 -->

<a id="commons-rng-examples-commons-rng-examples-quadrature-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-examples-commons-rng-examples-quadrature-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Quadrature Example |
| Description | Contains examples for computing numerical quadrature (integration). Code in this module is not part of the public API. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-quadrature/](#commons-rng-examples-commons-rng-examples-quadrature) |

<a id="commons-rng-examples-commons-rng-examples-quadrature-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-examples-commons-rng-examples-quadrature-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-examples-quadrature |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-examples-commons-rng-examples-quadrature-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-quadrature/team.html -->

<!-- page_index: 50 -->

<a id="commons-rng-examples-commons-rng-examples-quadrature-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-examples-commons-rng-examples-quadrature-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_ed3825ab46756177.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_ed3825ab46756177.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_ed3825ab46756177.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-examples-commons-rng-examples-quadrature-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-examples-commons-rng-examples-sampling-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-sampling/ci-management.html -->

<!-- page_index: 51 -->

<a id="commons-rng-examples-commons-rng-examples-sampling-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-examples-commons-rng-examples-sampling-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-examples-commons-rng-examples-sampling-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-examples-commons-rng-examples-sampling"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-sampling/index.html -->

<!-- page_index: 52 -->

<a id="commons-rng-examples-commons-rng-examples-sampling--about-apache-commons-rng-examples-sampling-utilities"></a>

# About Apache Commons RNG Examples Sampling Utilities

Contains examples of output from the samplers.
Code in this module is not part of the public API.

---

<a id="commons-rng-examples-commons-rng-examples-sampling-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-sampling/scm.html -->

<!-- page_index: 53 -->

<a id="commons-rng-examples-commons-rng-examples-sampling-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-examples-commons-rng-examples-sampling-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-examples/commons-rng-examples-sampling
```

<a id="commons-rng-examples-commons-rng-examples-sampling-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-sampling-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-sampling-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-examples-commons-rng-examples-sampling-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-sampling/summary.html -->

<!-- page_index: 54 -->

<a id="commons-rng-examples-commons-rng-examples-sampling-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-examples-commons-rng-examples-sampling-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Examples Sampling Utilities |
| Description | Contains examples of output from the samplers. Code in this module is not part of the public API. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-sampling/](#commons-rng-examples-commons-rng-examples-sampling) |

<a id="commons-rng-examples-commons-rng-examples-sampling-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-examples-commons-rng-examples-sampling-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-examples-sampling |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-examples-commons-rng-examples-sampling-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-sampling/team.html -->

<!-- page_index: 55 -->

<a id="commons-rng-examples-commons-rng-examples-sampling-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-examples-commons-rng-examples-sampling-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_e9dfe94ec3c71f5c.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_e9dfe94ec3c71f5c.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_e9dfe94ec3c71f5c.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-examples-commons-rng-examples-sampling-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-examples-commons-rng-examples-stress-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-stress/ci-management.html -->

<!-- page_index: 56 -->

<a id="commons-rng-examples-commons-rng-examples-stress-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-examples-commons-rng-examples-stress-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-examples-commons-rng-examples-stress-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-examples-commons-rng-examples-stress"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-stress/index.html -->

<!-- page_index: 57 -->

<a id="commons-rng-examples-commons-rng-examples-stress--about-apache-commons-rng-examples-stress-utilities"></a>

# About Apache Commons RNG Examples Stress Utilities

Application for calling external tools that perform stringent uniformity tests.
Code in this module is not part of the public API.

---

<a id="commons-rng-examples-commons-rng-examples-stress-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-stress/scm.html -->

<!-- page_index: 58 -->

<a id="commons-rng-examples-commons-rng-examples-stress-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-examples-commons-rng-examples-stress-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-examples/commons-rng-examples-stress
```

<a id="commons-rng-examples-commons-rng-examples-stress-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-stress-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-commons-rng-examples-stress-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-examples-commons-rng-examples-stress-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-stress/summary.html -->

<!-- page_index: 59 -->

<a id="commons-rng-examples-commons-rng-examples-stress-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-examples-commons-rng-examples-stress-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Examples Stress Utilities |
| Description | Application for calling external tools that perform stringent uniformity tests. Code in this module is not part of the public API. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-stress/](#commons-rng-examples-commons-rng-examples-stress) |

<a id="commons-rng-examples-commons-rng-examples-stress-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-examples-commons-rng-examples-stress-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-examples-stress |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-examples-commons-rng-examples-stress-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/commons-rng-examples-stress/team.html -->

<!-- page_index: 60 -->

<a id="commons-rng-examples-commons-rng-examples-stress-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-examples-commons-rng-examples-stress-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_ed59665fd421a1d1.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_ed59665fd421a1d1.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_ed59665fd421a1d1.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-examples-commons-rng-examples-stress-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/index.html -->

<!-- page_index: 61 -->

<a id="commons-rng-examples--about-apache-commons-rng-examples"></a>

# About Apache Commons RNG Examples

Examples of use of the "Commons RNG" library.
Codes in this module and its sub-modules are not part of the library.
They provide checking, benchmarking tools to enhance the documentation
and to help ensure correctness of the implementations.

<a id="commons-rng-examples--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons RNG Examples Stress Utilities](#commons-rng-examples-commons-rng-examples-stress) | Application for calling external tools that perform stringent uniformity tests. Code in this module is not part of the public API. |
| [Apache Commons RNG Examples Sampling Utilities](#commons-rng-examples-commons-rng-examples-sampling) | Contains examples of output from the samplers. Code in this module is not part of the public API. |
| [Apache Commons RNG Quadrature Example](#commons-rng-examples-commons-rng-examples-quadrature) | Contains examples for computing numerical quadrature (integration). Code in this module is not part of the public API. |
| [Apache Commons RNG JMH Benchmark](#commons-rng-examples-commons-rng-examples-jmh) | Code for running JMH benchmarks that assess the performance of the generators. Code in this module is not part of the public API. |
| [Apache Commons RNG JPMS Integration Test](#commons-rng-examples-commons-rng-examples-jpms) | Testing JPMS. Code in this module is not part of the public API. |

---

<a id="commons-rng-examples-modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/modules.html -->

<!-- page_index: 62 -->

<a id="commons-rng-examples-modules--project-modules"></a>

# Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons RNG Examples Stress Utilities](#commons-rng-examples-commons-rng-examples-stress) | Application for calling external tools that perform stringent uniformity tests. Code in this module is not part of the public API. |
| [Apache Commons RNG Examples Sampling Utilities](#commons-rng-examples-commons-rng-examples-sampling) | Contains examples of output from the samplers. Code in this module is not part of the public API. |
| [Apache Commons RNG Quadrature Example](#commons-rng-examples-commons-rng-examples-quadrature) | Contains examples for computing numerical quadrature (integration). Code in this module is not part of the public API. |
| [Apache Commons RNG JMH Benchmark](#commons-rng-examples-commons-rng-examples-jmh) | Code for running JMH benchmarks that assess the performance of the generators. Code in this module is not part of the public API. |
| [Apache Commons RNG JPMS Integration Test](#commons-rng-examples-commons-rng-examples-jpms) | Testing JPMS. Code in this module is not part of the public API. |

---

<a id="commons-rng-examples-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/scm.html -->

<!-- page_index: 63 -->

<a id="commons-rng-examples-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-examples-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-examples
```

<a id="commons-rng-examples-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-examples-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-examples-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/summary.html -->

<!-- page_index: 64 -->

<a id="commons-rng-examples-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-examples-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Examples |
| Description | Examples of use of the "Commons RNG" library. Codes in this module and its sub-modules are not part of the library. They provide checking, benchmarking tools to enhance the documentation and to help ensure correctness of the implementations. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-examples/](#commons-rng-examples) |

<a id="commons-rng-examples-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-examples-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-examples |
| Version | 1.7 |
| Type | pom |

---

<a id="commons-rng-examples-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-examples/team.html -->

<!-- page_index: 65 -->

<a id="commons-rng-examples-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-examples-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_57003e28cdd16bad.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_57003e28cdd16bad.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_57003e28cdd16bad.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-examples-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-sampling-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-sampling/ci-management.html -->

<!-- page_index: 66 -->

<a id="commons-rng-sampling-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-sampling-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-sampling-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-sampling-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-sampling/scm.html -->

<!-- page_index: 67 -->

<a id="commons-rng-sampling-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-sampling-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-sampling
```

<a id="commons-rng-sampling-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-sampling-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-sampling-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-sampling-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-sampling/summary.html -->

<!-- page_index: 68 -->

<a id="commons-rng-sampling-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-sampling-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Sampling |
| Description | The Apache Commons RNG Sampling module provides samplers for various distributions. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-sampling/](#commons-rng-sampling) |

<a id="commons-rng-sampling-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-sampling-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-sampling |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-sampling-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-sampling/team.html -->

<!-- page_index: 69 -->

<a id="commons-rng-sampling-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-sampling-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_51840b9302115a01.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_51840b9302115a01.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_51840b9302115a01.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-sampling-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---

<a id="commons-rng-simple-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-simple/ci-management.html -->

<!-- page_index: 70 -->

<a id="commons-rng-simple-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-rng-simple-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-rng/actions
```

<a id="commons-rng-simple-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-rng-simple-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-simple/scm.html -->

<!-- page_index: 71 -->

<a id="commons-rng-simple-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-rng-simple-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-rng.git/commons-rng-simple
```

<a id="commons-rng-simple-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-simple-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-rng.git
```

<a id="commons-rng-simple-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-rng-simple-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-simple/summary.html -->

<!-- page_index: 72 -->

<a id="commons-rng-simple-summary--project-summary"></a>

# Project Summary

<a id="commons-rng-simple-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons RNG Simple |
| Description | Simple API for instantiating random numbers generators. |
| Homepage | [https://commons.apache.org/proper/commons-rng/commons-rng-simple/](#commons-rng-simple) |

<a id="commons-rng-simple-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-rng-simple-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-rng-simple |
| Version | 1.7 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-rng-simple-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-rng/commons-rng-simple/team.html -->

<!-- page_index: 73 -->

<a id="commons-rng-simple-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-rng-simple-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_79f61638b89c8241.jpg) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_79f61638b89c8241.jpg) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](assets/images/00000000000000000000000000000000_79f61638b89c8241.jpg) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-rng-simple-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Artem Barger

Abhishek Singh Dhadwal

Arturo Bernal

---
