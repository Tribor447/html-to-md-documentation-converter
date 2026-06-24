# Math – Project Information

## Navigation

- Math
  - [Overview](#index)
  - [Issue Tracking](#issue-tracking)
  - [Developers Guide](#developers)
  - [Proposal](#proposal)
- User Guide
  - [Contents](#userguide)
  - [Overview](#userguide-overview)
  - [Statistics](#userguide-stat)
  - [Data Generation](#userguide-random)
  - [Linear Algebra](#userguide-linear)
  - [Numerical Analysis](#userguide-analysis)
  - [Special Functions](#userguide-special)
  - [Utilities](#userguide-utilities)
  - [Complex Numbers](#userguide-complex)
  - [Distributions](#userguide-distribution)
  - [Fractions](#userguide-fraction)
  - [Transform Methods](#userguide-transform)
  - [Geometry](#userguide-geometry)
  - [Optimization](#userguide-optimization)
  - [Curve Fitting](#userguide-fitting)
  - [Least Squares](#userguide-leastsquares)
  - [Ordinary Differential Equations](#userguide-ode)
  - [Genetic Algorithms](#userguide-genetics)
  - [Filters](#userguide-filter)
  - [Exceptions](#userguide-exceptions)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Project Modules](#modules)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Math Documentation
  - [Overview](#commons-math-docs)
- Other pages
  - [Math – CI Management](#commons-math-docs-ci-management)
  - [Math – Source Code Management](#commons-math-docs-scm)
  - [Math – Project Summary](#commons-math-docs-summary)
  - [Math – Project Team](#commons-math-docs-team)
  - [Example applications – CI Management](#commons-math-examples-ci-management)
  - [Example applications – About](#commons-math-examples)
  - [Example applications – Project Modules](#commons-math-examples-modules)
  - [Example applications – Source Code Management](#commons-math-examples-scm)
  - [Example applications – Project Summary](#commons-math-examples-summary)
  - [Example applications – Project Team](#commons-math-examples-team)
  - [Miscellaneous core classes – CI Management](#commons-math4-core-ci-management)
  - [Miscellaneous core classes – About](#commons-math4-core)
  - [Miscellaneous core classes – Source Code Management](#commons-math4-core-scm)
  - [Miscellaneous core classes – Project Summary](#commons-math4-core-summary)
  - [Miscellaneous core classes – Project Team](#commons-math4-core-team)
  - [Miscellaneous core classes (Legacy) – CI Management](#commons-math4-legacy-core-ci-management)
  - [Miscellaneous core classes (Legacy) – About](#commons-math4-legacy-core)
  - [Miscellaneous core classes (Legacy) – Source Code Management](#commons-math4-legacy-core-scm)
  - [Miscellaneous core classes (Legacy) – Project Summary](#commons-math4-legacy-core-summary)
  - [Miscellaneous core classes (Legacy) – Project Team](#commons-math4-legacy-core-team)
  - [Exception classes (Legacy) – CI Management](#commons-math4-legacy-exception-ci-management)
  - [Exception classes (Legacy) – About](#commons-math4-legacy-exception)
  - [Exception classes (Legacy) – Source Code Management](#commons-math4-legacy-exception-scm)
  - [Exception classes (Legacy) – Project Summary](#commons-math4-legacy-exception-summary)
  - [Exception classes (Legacy) – Project Team](#commons-math4-legacy-exception-team)
  - [Apache Commons Math (Legacy) – CI Management](#commons-math4-legacy-ci-management)
  - [Apache Commons Math (Legacy) – About](#commons-math4-legacy)
  - [Apache Commons Math (Legacy) – Source Code Management](#commons-math4-legacy-scm)
  - [Apache Commons Math (Legacy) – Project Summary](#commons-math4-legacy-summary)
  - [Apache Commons Math (Legacy) – Project Team](#commons-math4-legacy-team)
  - [Artificial neural networks – CI Management](#commons-math4-neuralnet-ci-management)
  - [Artificial neural networks – About](#commons-math4-neuralnet)
  - [Artificial neural networks – Source Code Management](#commons-math4-neuralnet-scm)
  - [Artificial neural networks – Project Summary](#commons-math4-neuralnet-summary)
  - [Artificial neural networks – Project Team](#commons-math4-neuralnet-team)
  - [Transforms – CI Management](#commons-math4-transform-ci-management)
  - [Transforms – About](#commons-math4-transform)
  - [Transforms – Source Code Management](#commons-math4-transform-scm)
  - [Transforms – Project Summary](#commons-math4-transform-summary)
  - [Transforms – Project Team](#commons-math4-transform-team)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-math:-the-apache-commons-mathematics-library"></a>

## Commons Math: The Apache Commons Mathematics Library

Commons Math is a library of lightweight, self-contained
mathematics and statistics components addressing the most common
problems not available in the Java programming language or Commons
Lang.

Guiding principles:

1. Real-world application use cases determine development
   priority.
2. This package emphasizes small, easily integrated components
   rather than large libraries with complex dependencies and
   configurations.
3. All algorithms are fully documented and follow generally
   accepted best practices.
4. In situations where multiple standard algorithms exist, a
   Strategy pattern is used to support multiple
   implementations.
5. Limited dependencies. No external dependencies beyond Commons
   components and the core Java platform (at least Java 1.3 up to
   version 1.2 of the library, at least Java 5 starting with version
   2.0 of the library).

<a id="index--download-math"></a>

## Download Math

<a id="index--releases"></a>

### Releases

Download the
[Latest Release](http://commons.apache.org/math/download_math.cgi) of Commons Math.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/issue-tracking.html -->

<!-- page_index: 2 -->

<a id="issue-tracking--commons-math-issue-tracking"></a>

## Commons Math Issue tracking

Commons Math uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Commons Math JIRA project page](https://issues.apache.org/jira/browse/MATH).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Commons Math please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310485&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-math/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310485&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310485&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Commons Math are all unpaid volunteers

For more information on subversion and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Commons Math bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310485&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Commons Math bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310485&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Commons Math bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310485&sorter/field=issuekey&sorter/order=DESC)

---

<a id="developers"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/developers.html -->

<!-- page_index: 3 -->

<a id="developers--aims"></a>

## Aims

Creating and maintaining a mathematical and statistical library that is
accurate requires a greater degree of communication than might be the
case for other components. It is important that developers follow
guidelines laid down by the community to ensure that the code they create
can be successfully maintained by others.

<a id="developers--guidelines"></a>

## Guidelines

Developers are asked to comply with the following development guidelines.
Code that does not comply with the guidelines including the word *must*
will not be committed. Our aim will be to fix all of the exceptions to the
"*should*" guidelines prior to a release.

<a id="developers--coding-style"></a>

### Coding Style

Commons Math follows [Code
Conventions for the Java Programming Language](http://java.sun.com/docs/codeconv/). As part of the maven
build process, style checking is performed using the Checkstyle plugin, using the properties specified in `checkstyle.xml`.
Committed code *should* generate no Checkstyle errors. One thing
that Checkstyle will complain about is tabs included in the source code.
Please make sure to set your IDE or editor to use spaces instead of tabs.

Committers should configure the

```
user.name
```

and

```
user.email
```

and git repository (or global) settings
with

```
git config
```

.
They define the identity and mail of the committer.
See [Customizing
Git - Git Configuration](http://www.git-scm.com/book/en/Customizing-Git-Git-Configuration) in the git book for explanation about how to
configure these settings and more.

<a id="developers--documentation"></a>

### Documentation

- Committed code *must* include full javadoc.
- All component contracts *must* be fully specified in the javadoc class,
  interface or method comments, including specification of acceptable ranges
  of values, exceptions or special return values.
- External references or full statements of definitions for all mathematical
  terms used in component documentation *must* be provided.
- Commons math javadoc generation now supports embedded LaTeX formulas via the
  [MathJax](http://www.mathjax.org) javascript display engine. To
  embed mathematical expressions formatted in LaTeX in javadoc, simply surround
  the expression to be formatted with either

```
\( ... \)
```

  for inline
  formulas, or

```
\[ ... \]
```

  to have the formula appear on a separate line.
  For example,

```
\(a^2 + b^2 = c^2\)
```

  will render an inline formula
  saying that (a, b, c) is Pythagorean triplet: \( a^2 + b^2 = c^2 \).
  See the MathJax and LaTex documentation for details on how to represent
  formulas and escape special characters.
- Implementations *should* use standard algorithms and
  references or full descriptions of all algorithms *should* be
  provided.
- Additions and enhancements *should* include updates to the User
  Guide.

<a id="developers--exceptions"></a>

### Exceptions

- Exceptions generated by Commons Math are all unchecked.
- All public methods advertise all exceptions that they can generate.
  Exceptions *must* be documented in both javadoc and method signatures
  and the documentation in the javadoc *must* include full description
  of the conditions under which exceptions are thrown.
- Methods *should* fully specify parameter preconditions required for
  successful activation. When preconditions are violated, a
  MathIllegalArgumentException should be thrown. Subclasses of
  MathIllegalArgumentException may be used to represent common parameter
  contract violations (for example, NoBracketingException). Exception
  messages *must* contain sufficient information on parameter values to
  determine the exact precondition failure.
- Exceptions generated by Commons Math make sense without knowing
  implementation details other than those stated in the public API.
  For example, a NoBracketingException makes sense thrown by a solver that
  has a precondition requiring that initial points bracket a root. This
  exception does not make sense, however, thrown by an inverse cumulative
  probability estimator.
- MathIllegalArgumentException should only be thrown in situations
  where preconditions can be exhaustively provided so that what arguments
  are "illegal" can be specified fully to the caller. Domain-specific
  exceptions need to be defined for cases where failures cannot be
  attributed to parameter precondition violation. For example, the exact
  domain of successful activation of a solver or quadrature method may be
  impossible to specify because of numerical properties of the method.
  If a solver fails to find a root or a quadrature method fails to converge
  for a given set of parameters, *unless those parameters violate the
  advertised preconditions* it is not appropriate to throw
  MathIllegalArgumentException.
- State information included in exception messages *must* be available
  in exception properties - i.e., successful handling or reporting of
  Commons Math exceptions must not require parsing exception messages.

<a id="developers--unit-tests"></a>

### Unit Tests

- Committed code *must* include unit tests.
- Unit tests *should* provide full path coverage.
- Unit tests *should* verify all boundary conditions specified in
  interface contracts, including verification that exceptions are thrown or
  special values (e.g. Double.NaN, Double.Infinity) are returned as
  expected.

<a id="developers--licensing-and-copyright"></a>

### Licensing and copyright

- All new source file submissions *must* include the Apache Software
  License in a comment that begins the file
- All contributions must comply with the terms of the Apache
  [Contributor License
  Agreement (CLA)](http://www.apache.org/licenses/cla.pdf)
- Patches *must* be accompanied by a clear reference to a "source"
  - if code has been "ported" from another language, clearly state the
  source of the original implementation. If the "expression" of a given
  algorithm is derivative, please note the original source (textbook,
  paper, etc.).
- References to source materials covered by restrictive proprietary
  licenses should be avoided. In particular, contributions should not
  implement or include references to algorithms in
  [Numerical Recipes (NR)](http://www.nr.com/).
  Any questions about copyright or patent issues should be raised on
  the commons-dev mailing list before contributing or committing code.

<a id="developers--recommended-readings"></a>

## Recommended Readings

Here is a list of relevant materials. Much of the discussion surrounding
the development of this component will refer to the various sources
listed below, and frequently the Javadoc for a particular class or
interface will link to a definition contained in these documents.

<a id="developers--recommended-readings-2"></a>

### Recommended Readings

Concerning floating point arithmetic.
:   <http://www.validlab.com/goldberg/paper.pdf>
    <http://www.cs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF>
    <http://www.cs.berkeley.edu/~wkahan/JAVAhurt.pdf>

Numerical analysis
:   [Scientific Computing FAQ @ Mathcom](http://www.mathcom.com/corpdir/techinfo.mdir/scifaq/index.html)
    [Bibliography of accuracy and stability of numerical algorithms](http://www.ma.man.ac.uk/~higham/asna/asna2.pdf)
    [SUNY Stony Brook numerical methods page](http://tonic.physics.sunysb.edu/docs/num_meth.html)
    [SIAM Journal of Numerical Analysis Online](http://epubs.siam.org/sam-bin/dbq/toclist/SINUM)

Probability and statistics
:   [Statlib at CMU](http://lib.stat.cmu.edu/)
    [NIST Engineering Statistics Handbook](http://www.itl.nist.gov/div898/handbook/)
    [Online Introductory Statistics (David W. Stockburger)](http://www.psychstat.smsu.edu/sbk00.htm)
    [Online Journal of Statistical Software](http://www.jstatsoft.org/)

<a id="developers--javadoc-comment-resources"></a>

### Javadoc comment resources

References for mathematical definitions.
:   <http://rd11.web.cern.ch/RD11/rkb/titleA.html>
    <http://mathworld.wolfram.com/>
    <http://www.itl.nist.gov/div898/handbook>
    [Chan, T. F. and J. G. Lewis 1979, *Communications of the ACM*,
    vol. 22 no. 9, pp. 526-531.](http://doi.acm.org/10.1145/359146.359152)

<a id="developers--xml"></a>

### XML

XML related resources.
:   <http://www.openmath.org>

Copyright © 2003-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Math, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="proposal"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/proposal.html -->

<!-- page_index: 4 -->

<a id="proposal--proposal-for-math-package"></a>

## Proposal for math Package

<a id="proposal--0-rationale"></a>

### (0) Rationale

The Java programming language and the math extensions in commons-lang provide implementations
for only the most basic mathematical algorithms. Routine development tasks such as computing
basic statistics or solving a system of linear equations require components not available in java
or commons-lang.

Most basic mathematical or statistical algorithms are available in open source implementations, but to assemble a simple set of capabilities one has to use multiple libraries, many of which have
more restrictive licensing terms than the ASF. In addition, many of the best open source
implementations (e.g. the R statistical package) are either not available in Java or require large
support libraries and/or external dependencies to work.

A commons-math community will provide a productive environment for aggregation, testing and
support of efficient Java implementations of commonly used mathematical and statistical algorithms.

<a id="proposal--1-scope-of-the-package"></a>

### (1) Scope of the Package

The Math project shall create and maintain a library of lightweight, self-contained mathematics
and statistics components addressing the most common practical problems not immediately available in
the Java programming language or commons-lang. The guiding principles for commons-math will be:

1. Real-world application use cases determine priority
2. Emphasis on small, easily integrated components rather than large libraries with complex
   dependencies
3. All algorithms are fully documented and follow generally accepted best practices
4. In situations where multiple standard algorithms exist, use the Strategy pattern to support
   multiple implementations
5. Limited dependencies. No external dependencies beyond Commons components and the JDK

<a id="proposal--1.5-interaction-with-other-packages"></a>

### (1.5) Interaction With Other Packages

*math* relies only on standard JDK 1.2 (or later) APIs for
production deployment. It utilizes the JUnit unit testing framework for
developing and executing unit tests, but this is of interest only to
developers of the component.

No external configuration files are utilized.

<a id="proposal--2-initial-source-of-the-package"></a>

### (2) Initial Source of the Package

The initial codebase will consist of implementations of basic statistical algorithms such
as the following:

- Simple univariate statistics (mean, standard deviation, n, confidence intervals)
- Frequency distributions
- t-test, chi-square test
- Random numbers from Gaussian, Exponential, Poisson distributions
- Random sampling/resampling
- Bivariate regression, corellation

and mathematical algorithms such as the following:

- Basic Complex Number representation with algebraic operations
- Newton's method for finding roots
- Binomial coefficients
- Exponential growth and decay (set up for financial applications)
- Polynomial Interpolation (curve fitting)
- Basic Matrix representation with algebraic operations

The proposed package name for the new component is
`org.apache.commons.math`.

<a id="proposal--3-required-jakarta-commons-resources"></a>

### (3) Required Jakarta-Commons Resources

- CVS Repository - New directory `math` in the
  `jakarta-commons` CVS repository.
- Mailing List - Discussions will take place on the general
  *dev@commons.apache.org* mailing list. To help
  list subscribers identify messages of interest, it is suggested that
  the message subject of messages about this component be prefixed with
  [math].
- Bugzilla - New component "math" under the "Commons" product
  category, with appropriate version identifiers as needed.
- Jyve FAQ - New category "commons-math" (when available).

<a id="proposal--4-initial-committers"></a>

### (4) Initial Committers

The initial committers on the math component shall be:

- [Robert Burrell Donkin](mailto:rdonkin@apache.org)
- [Tim O'Brien](mailto:tobrien@apache.org)

---

<a id="userguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/index.html -->

<!-- page_index: 5 -->

# Math – The Commons Math User Guide - Table of Contents

Copyright © 2003-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Math, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="userguide-overview"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/overview.html -->

<!-- page_index: 6 -->

<a id="userguide-overview--overview"></a>

## Overview

<a id="userguide-overview--0.1-about-the-user-guide"></a>

### 0.1 About The User Guide

This guide is intended to help programmers quickly find what they need to develop
solutions using Commons Math. It also provides a supplement to the javadoc API documentation, providing a little more explanation of the mathematical objects and functions included
in the package.

<a id="userguide-overview--0.2-what-s-in-commons-math"></a>

### 0.2 What's in commons-math

Commons Math is made up of a small set of math/stat utilities addressing
programming problems like the ones in the list below. This list is not exhaustive, it's just meant to give a feel for the kinds of things that Commons Math provides.

- Computing means, variances and other summary statistics for a list of numbers
- Fitting a line to a set of data points using linear regression
- Fitting a curve to a set of data points
- Finding a smooth curve that passes through a collection of points (interpolation)
- Fitting a parametric model to a set of measurements using least-squares methods
- Solving equations involving real-valued functions (i.e. root-finding)
- Solving systems of linear equations
- Solving Ordinary Differential Equations
- Minimizing multi-dimensional functions
- Generating random numbers with more restrictions (e.g distribution, range) than what
  is possible using the JDK
- Generating random samples and/or datasets that are "like" the data in an input file
- Performing statistical significance tests
- Miscellaneous mathematical functions such as factorials, binomial
  coefficients and "special functions" (e.g. gamma, beta functions)

We are actively seeking ideas for additional components that fit into the
[Commons Math vision](#index--summary) of a set of lightweight, self-contained math/stat components useful for solving common programming problems.
Suggestions for new components or enhancements to existing functionality are always welcome!
All feedback/suggestions for improvement should be sent to the
[commons-dev mailing list](http://commons.apache.org/mail-lists.html) with
[math] at the beginning of the subject line.

<a id="userguide-overview--0.4-how-interface-contracts-are-specified-in-commons-math-javadoc"></a>

### 0.4 How interface contracts are specified in commons-math javadoc

You should always read the javadoc class and method comments carefully when using
Commons Math components in your programs. The javadoc provides references to the algorithms
that are used, usage notes about limitations, performance, etc. as well as interface contracts.
Interface contracts are specified in terms of preconditions (what has to be true in order
for the method to return valid results), special values returned (e.g. Double.NaN)
or exceptions that may be thrown if the preconditions are not met, and definitions for returned
values/objects or state changes.

When the actual parameters provided to a method or the internal state of an object
make a computation meaningless, a
[MathIllegalArgumentException](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/exception/MathIllegalArgumentException.html) or
[MathIllegalStateException](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/exception/MathIllegalStateException.html) may be thrown. Exact conditions under which runtime
exceptions (and any other exceptions) are thrown are specified in the javadoc method
comments.
In some cases, to be consistent with the [IEEE 754 standard](http://grouper.ieee.org/groups/754/) for floating point arithmetic and with java.lang.Math, Commons Math
methods return `Double.NaN` values. Conditions under which `Double.NaN`
or other special values are returned are fully specified in the javadoc method comments.

As of version 2.2, the policy for dealing with null references is as
follows: When an argument is unexpectedly null, a
[NullArgumentException](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/exception/NullArgumentException.html) is raised to signal the illegal argument. Note that this
class does not inherit from the standard `NullPointerException` but is a subclass
of `MathIllegalArgumentException`.

<a id="userguide-overview--0.5-dependencies"></a>

### 0.5 Dependencies

Commons Math requires JDK 1.8+ and has no runtime dependencies.

<a id="userguide-overview--0.6-license"></a>

### 0.6 License

Commons Math is distributed under the terms of the Apache License, Version 2.0:
.

This product includes software developed by other third parties and
distributed under licenses terms compatible with Apache License, Version 2.0.
All the licenses of such third parties products are available in the distribution
in the LICENSE file. Some products require additional attribution, these
attributions can be found in the NOTICE file. These files are available
both in the source packages and in the binaries distribution jar files.

Copyright © 2003-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Math, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="userguide-stat"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/stat.html -->

<!-- page_index: 7 -->

<a id="userguide-stat--1-statistics"></a>

## 1 Statistics

<a id="userguide-stat--1.1-overview"></a>

### 1.1 Overview

The statistics package provides frameworks and implementations for
basic Descriptive statistics, frequency distributions, bivariate regression, and t-, chi-square and ANOVA test statistics.

[Descriptive statistics](#userguide-stat--a1.2_descriptive_statistics)
[Frequency distributions](#userguide-stat--a1.3_frequency_distributions)
[Simple Regression](#userguide-stat--a1.4_simple_regression)
[Multiple Regression](#userguide-stat--a1.5_multiple_linear_regression)
[Rank transformations](#userguide-stat--a1.6_rank_transformations)
[Covariance and correlation](#userguide-stat--a1.7_covariance_and_correlation)
[Statistical Tests](#userguide-stat--a1.8_statistical_tests)

<a id="userguide-stat--1.2-descriptive-statistics"></a>

### 1.2 Descriptive statistics

The stat package includes a framework and default implementations for
the following Descriptive statistics:

- arithmetic and geometric means
- variance and standard deviation
- sum, product, log sum, sum of squared values
- minimum, maximum, median, and percentiles
- skewness and kurtosis
- first, second, third and fourth moments

With the exception of percentiles and the median, all of these
statistics can be computed without maintaining the full list of input
data values in memory. The stat package provides interfaces and
implementations that do not require value storage as well as
implementations that operate on arrays of stored values.

The top level interface is
[UnivariateStatistic](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/UnivariateStatistic.html).
This interface, implemented by all statistics, consists of
`evaluate()` methods that take double[] arrays as arguments
and return the value of the statistic. This interface is extended by
[StorelessUnivariateStatistic](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/StorelessUnivariateStatistic.html), which adds `increment(),`
`getResult()` and associated methods to support
"storageless" implementations that maintain counters, sums or other
state information as values are added using the `increment()`
method.

Abstract implementations of the top level interfaces are provided in
[AbstractUnivariateStatistic](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/AbstractUnivariateStatistic.html) and
[AbstractStorelessUnivariateStatistic](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/AbstractStorelessUnivariateStatistic.html) respectively.

Each statistic is implemented as a separate class, in one of the
subpackages (moment, rank, summary) and each extends one of the abstract
classes above (depending on whether or not value storage is required to
compute the statistic). There are several ways to instantiate and use statistics.
Statistics can be instantiated and used directly, but it is generally more convenient
(and efficient) to access them using the provided aggregates, [DescriptiveStatistics](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/DescriptiveStatistics.html) and
[SummaryStatistics.](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/SummaryStatistics.html)

`DescriptiveStatistics` maintains the input data in memory
and has the capability of producing "rolling" statistics computed from a
"window" consisting of the most recently added values.

`SummaryStatistics` does not store the input data values
in memory, so the statistics included in this aggregate are limited to those
that can be computed in one pass through the data without access to
the full array of values.

| Aggregate | Statistics Included | Values stored? | "Rolling" capability? |
| --- | --- | --- | --- |
| [DescriptiveStatistics](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/DescriptiveStatistics.html) | min, max, mean, geometric mean, n, sum, sum of squares, standard deviation, variance, percentiles, skewness, kurtosis, median | Yes | Yes |
| [SummaryStatistics](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/SummaryStatistics.html) | min, max, mean, geometric mean, n, sum, sum of squares, standard deviation, variance | No | No |

`SummaryStatistics` can be aggregated using
[AggregateSummaryStatistics.](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/AggregateSummaryStatistics.html) This class can be used to concurrently
gather statistics for multiple datasets as well as for a combined sample
including all of the data.

`MultivariateSummaryStatistics` is similar to
`SummaryStatistics` but handles n-tuple values instead of
scalar values. It can also compute the full covariance matrix for the
input data.

Neither `DescriptiveStatistics` nor `SummaryStatistics`
is thread-safe.
[SynchronizedDescriptiveStatistics](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/SynchronizedDescriptiveStatistics.html) and
[SynchronizedSummaryStatistics](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/SynchronizedSummaryStatistics.html), respectively, provide thread-safe
versions for applications that require concurrent access to statistical
aggregates by multiple threads.
[SynchronizedMultivariateSummaryStatistics](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/SynchronizedMultiVariateSummaryStatistics.html) provides thread-safe
`MultivariateSummaryStatistics.`

There is also a utility class, [StatUtils](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/StatUtils.html), that provides static methods for computing statistics
directly from double[] arrays.

Here are some examples showing how to compute Descriptive statistics.

Compute summary statistics for a list of double values
:   Using the `DescriptiveStatistics` aggregate
    (values are stored in memory):


```

// Get a DescriptiveStatistics instance
DescriptiveStatistics stats = new DescriptiveStatistics();

// Add the data from the array
for( int i = 0; i < inputArray.length; i++) {
        stats.addValue(inputArray[i]);
}

// Compute some statistics
double mean = stats.getMean();
double std = stats.getStandardDeviation();
double median = stats.getPercentile(50);
        
```

:   Using the `SummaryStatistics` aggregate (values are
    **not** stored in memory):


```

// Get a SummaryStatistics instance
SummaryStatistics stats = new SummaryStatistics();

// Read data from an input stream,
// adding values and updating sums, counters, etc.
while (line != null) {
        line = in.readLine();
        stats.addValue(Double.parseDouble(line.trim()));
}
in.close();

// Compute the statistics
double mean = stats.getMean();
double std = stats.getStandardDeviation();
//double median = stats.getMedian(); <-- NOT AVAILABLE
        
```

:   Using the `StatUtils` utility class:


```

// Compute statistics directly from the array
// assume values is a double[] array
double mean = StatUtils.mean(values);
double std = FastMath.sqrt(StatUtils.variance(values));
double median = StatUtils.percentile(values, 50);

// Compute the mean of the first three values in the array
mean = StatUtils.mean(values, 0, 3);
        
```

Maintain a "rolling mean" of the most recent 100 values from an input stream
:   Use a `DescriptiveStatistics` instance with
    window size set to 100


```

// Create a DescriptiveStatistics instance and set the window size to 100
DescriptiveStatistics stats = new DescriptiveStatistics();
stats.setWindowSize(100);

// Read data from an input stream,
// displaying the mean of the most recent 100 observations
// after every 100 observations
long nLines = 0;
while (line != null) {
        line = in.readLine();
        nLines++;
        stats.addValue(Double.parseDouble(line.trim()));
        if (nLines == 100) {
                nLines = 0;
                System.out.println(stats.getMean());
       }
}
in.close();
        
```

Compute statistics in a thread-safe manner
:   Use a `SynchronizedDescriptiveStatistics` instance


```

// Create a SynchronizedDescriptiveStatistics instance and
// use as any other DescriptiveStatistics instance
DescriptiveStatistics stats = new SynchronizedDescriptiveStatistics();
        
```

Compute statistics for multiple samples and overall statistics concurrently
:   There are two ways to do this using `AggregateSummaryStatistics.`
    The first is to use an `AggregateSummaryStatistics` instance
    to accumulate overall statistics contributed by `SummaryStatistics`
    instances created using
    [AggregateSummaryStatistics.createContributingStatistics()](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/AggregateSummaryStatistics.html#createContributingStatistics):


```

// Create a AggregateSummaryStatistics instance to accumulate the overall statistics
// and AggregatingSummaryStatistics for the subsamples
AggregateSummaryStatistics aggregate = new AggregateSummaryStatistics();
SummaryStatistics setOneStats = aggregate.createContributingStatistics();
SummaryStatistics setTwoStats = aggregate.createContributingStatistics();
// Add values to the subsample aggregates
setOneStats.addValue(2);
setOneStats.addValue(3);
setTwoStats.addValue(2);
setTwoStats.addValue(4);
...
// Full sample data is reported by the aggregate
double totalSampleSum = aggregate.getSum();
        
```

    The above approach has the disadvantages that the `addValue` calls must be synchronized on the
    `SummaryStatistics` instance maintained by the aggregate and each value addition updates the
    aggregate as well as the subsample. For applications that can wait to do the aggregation until all values
    have been added, a static
    [aggregate](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/AggregateSummaryStatistics.html#aggregatejava.util.Collection) method is available, as shown in the following example.
    This method should be used when aggregation needs to be done across threads.


```

// Create SummaryStatistics instances for the subsample data
SummaryStatistics setOneStats = new SummaryStatistics();
SummaryStatistics setTwoStats = new SummaryStatistics();
// Add values to the subsample SummaryStatistics instances
setOneStats.addValue(2);
setOneStats.addValue(3);
setTwoStats.addValue(2);
setTwoStats.addValue(4);
...
// Aggregate the subsample statistics
Collection<SummaryStatistics> aggregate = new ArrayList<SummaryStatistics>();
aggregate.add(setOneStats);
aggregate.add(setTwoStats);
StatisticalSummary aggregatedStats = AggregateSummaryStatistics.aggregate(aggregate);

// Full sample data is reported by aggregatedStats
double totalSampleSum = aggregatedStats.getSum();
        
```

<a id="userguide-stat--1.3-frequency-distributions"></a>

### 1.3 Frequency distributions

[Frequency](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/Frequency.html)
provides a simple interface for maintaining counts and percentages of discrete
values.

Strings, integers, longs and chars are all supported as value types, as well as instances of any class that implements `Comparable.`
The ordering of values used in computing cumulative frequencies is by
default the *natural ordering,* but this can be overridden by supplying a
`Comparator` to the constructor. Adding values that are not
comparable to those that have already been added results in an
`IllegalArgumentException.`

Here are some examples.

Compute a frequency distribution based on integer values
:   Mixing integers, longs, Integers and Longs:


```

 Frequency f = new Frequency();
 f.addValue(1);
 f.addValue(new Integer(1));
 f.addValue(new Long(1));
 f.addValue(2);
 f.addValue(new Integer(-1));
 System.out.prinltn(f.getCount(1));   // displays 3
 System.out.println(f.getCumPct(0));  // displays 0.2
 System.out.println(f.getPct(new Integer(1)));  // displays 0.6
 System.out.println(f.getCumPct(-2));   // displays 0
 System.out.println(f.getCumPct(10));  // displays 1
          
```

Count string frequencies
:   Using case-sensitive comparison, alpha sort order (natural comparator):


```

Frequency f = new Frequency();
f.addValue("one");
f.addValue("One");
f.addValue("oNe");
f.addValue("Z");
System.out.println(f.getCount("one")); // displays 1
System.out.println(f.getCumPct("Z"));  // displays 0.5
System.out.println(f.getCumPct("Ot")); // displays 0.25
          
```

:   Using case-insensitive comparator:


```

Frequency f = new Frequency(String.CASE_INSENSITIVE_ORDER);
f.addValue("one");
f.addValue("One");
f.addValue("oNe");
f.addValue("Z");
System.out.println(f.getCount("one"));  // displays 3
System.out.println(f.getCumPct("z"));  // displays 1
          
```

<a id="userguide-stat--1.4-simple-regression"></a>

### 1.4 Simple regression

[SimpleRegression](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/SimpleRegression.html) provides ordinary least squares regression with
one independent variable estimating the linear model:

`y = intercept + slope * x`

or

`y = slope * x`

Standard errors for `intercept` and `slope` are
available as well as ANOVA, r-square and Pearson's r statistics.

Observations (x,y pairs) can be added to the model one at a time or they
can be provided in a 2-dimensional array. The observations are not stored
in memory, so there is no limit to the number of observations that can be
added to the model.

**Usage Notes**:

- When there are fewer than two observations in the model, or when
  there is no variation in the x values (i.e. all x values are the same)
  all statistics return `NaN`. At least two observations with
  different x coordinates are required to estimate a bivariate regression
  model.
- getters for the statistics always compute values based on the current
  set of observations -- i.e., you can get statistics, then add more data
  and get updated statistics without using a new instance. There is no
  "compute" method that updates all statistics. Each of the getters performs
  the necessary computations to return the requested statistic.
- The intercept term may be suppressed by passing `false` to the
  [SimpleRegression(boolean)](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/SimpleRegression.html#SimpleRegressionboolean) constructor. When the `hasIntercept`
  property is false, the model is estimated without a constant term and
  `getIntercept()` returns `0`.

**Implementation Notes**:

- As observations are added to the model, the sum of x values, y values,
  cross products (x times y), and squared deviations of x and y from their
  respective means are updated using updating formulas defined in
  "Algorithms for Computing the Sample Variance: Analysis and
  Recommendations", Chan, T.F., Golub, G.H., and LeVeque, R.J.
  1983, American Statistician, vol. 37, pp. 242-247, referenced in
  Weisberg, S. "Applied Linear Regression". 2nd Ed. 1985. All regression
  statistics are computed from these sums.
- Inference statistics (confidence intervals, parameter significance levels)
  are based on on the assumption that the observations included in the model are
  drawn from a [Bivariate Normal Distribution](http://mathworld.wolfram.com/BivariateNormalDistribution.html)

Here are some examples.

Estimate a model based on observations added one at a time
:   Instantiate a regression instance and add data points


```

regression = new SimpleRegression();
regression.addData(1d, 2d);
// At this point, with only one observation,
// all regression statistics will return NaN

regression.addData(3d, 3d);
// With only two observations,
// slope and intercept can be computed
// but inference statistics will return NaN

regression.addData(3d, 3d);
// Now all statistics are defined.
         
```

:   Compute some statistics based on observations added so far


```

System.out.println(regression.getIntercept());
// displays intercept of regression line

System.out.println(regression.getSlope());
// displays slope of regression line

System.out.println(regression.getSlopeStdErr());
// displays slope standard error
         
```

:   Use the regression model to predict the y value for a new x value


```

System.out.println(regression.predict(1.5d)
// displays predicted y value for x = 1.5
         
```

    More data points can be added and subsequent getXxx calls will incorporate
    additional data in statistics.

Estimate a model from a double[][] array of data points
:   Instantiate a regression object and load dataset


```

double[][] data = { { 1, 3 }, {2, 5 }, {3, 7 }, {4, 14 }, {5, 11 }};
SimpleRegression regression = new SimpleRegression();
regression.addData(data);
          
```

:   Estimate regression model based on data


```

System.out.println(regression.getIntercept());
// displays intercept of regression line

System.out.println(regression.getSlope());
// displays slope of regression line

System.out.println(regression.getSlopeStdErr());
// displays slope standard error
         
```

    More data points -- even another double[][] array -- can be added and subsequent
    getXxx calls will incorporate additional data in statistics.

Estimate a model from a double[][] array of data points, *excluding* the intercept
:   Instantiate a regression object and load dataset


```

double[][] data = { { 1, 3 }, {2, 5 }, {3, 7 }, {4, 14 }, {5, 11 }};
SimpleRegression regression = new SimpleRegression(false);
//the argument, false, tells the class not to include a constant
regression.addData(data);
          
```

:   Estimate regression model based on data


```

System.out.println(regression.getIntercept());
// displays intercept of regression line, since we have constrained the constant, 0.0 is returned

System.out.println(regression.getSlope());
// displays slope of regression line

System.out.println(regression.getSlopeStdErr());
// displays slope standard error

System.out.println(regression.getInterceptStdErr() );
// will return Double.NaN, since we constrained the parameter to zero
         
```

    Caution must be exercised when interpreting the slope when no constant is being estimated. The slope
    may be biased.

<a id="userguide-stat--1.5-multiple-linear-regression"></a>

### 1.5 Multiple linear regression

[OLSMultipleLinearRegression](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/OLSMultipleLinearRegression.html) and
[GLSMultipleLinearRegression](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/GLSMultipleLinearRegression.html) provide least squares regression to fit the linear model:

`Y=X*b+u`

where Y is an n-vector **regressand**, X is a [n,k] matrix whose k columns are called
**regressors**, b is k-vector of **regression parameters** and u is an n-vector
of **error terms** or **residuals**.

[OLSMultipleLinearRegression](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/OLSMultipleLinearRegression.html) provides Ordinary Least Squares Regression, and
[GLSMultipleLinearRegression](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/GLSMultipleLinearRegression.html) implements Generalized Least Squares. See the javadoc for these
classes for details on the algorithms and formulas used.

Data for OLS models can be loaded in a single double[] array, consisting of concatenated rows of data, each containing
the regressand (Y) value, followed by regressor values; or using a double[][] array with rows corresponding to
observations. GLS models also require a double[][] array representing the covariance matrix of the error terms. See
[AbstractMultipleLinearRegression#newSampleData(double[],int,int)](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/AbstractMultipleLinearRegression.html#newSampleDatadouble_int_int),
[OLSMultipleLinearRegression#newSampleData(double[], double[][])](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/OLSMultipleLinearRegression.html#newSampleDatadouble_double) and
[GLSMultipleLinearRegression#newSampleData(double[],double[][],double[][])](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/regression/GLSMultipleLinearRegression.html#newSampleDatadouble_double_double) for details.

**Usage Notes**:

- Data are validated when invoking any of the newSample, newX, newY or newCovariance methods and
  `IllegalArgumentException` is thrown when input data arrays do not have matching dimensions
  or do not contain sufficient data to estimate the model.
- By default, regression models are estimated with intercept terms. In the notation above, this implies that the
  X matrix contains an initial row identically equal to 1. X data supplied to the newX or newSample methods should not
  include this column - the data loading methods will create it automatically. To estimate a model without an intercept
  term, set the `noIntercept` property to `true.`

Here are some examples.

OLS regression
:   Instantiate an OLS regression object and load a dataset:


```

OLSMultipleLinearRegression regression = new OLSMultipleLinearRegression();
double[] y = new double[]{11.0, 12.0, 13.0, 14.0, 15.0, 16.0};
double[][] x = new double[6][];
x[0] = new double[]{0, 0, 0, 0, 0};
x[1] = new double[]{2.0, 0, 0, 0, 0};
x[2] = new double[]{0, 3.0, 0, 0, 0};
x[3] = new double[]{0, 0, 4.0, 0, 0};
x[4] = new double[]{0, 0, 0, 5.0, 0};
x[5] = new double[]{0, 0, 0, 0, 6.0};
regression.newSampleData(y, x);
          
```

:   Get regression parameters and diagnostics:


```

double[] beta = regression.estimateRegressionParameters();

double[] residuals = regression.estimateResiduals();

double[][] parametersVariance = regression.estimateRegressionParametersVariance();

double regressandVariance = regression.estimateRegressandVariance();

double rSquared = regression.calculateRSquared();

double sigma = regression.estimateRegressionStandardError();
         
```

GLS regression
:   Instantiate a GLS regression object and load a dataset:


```

GLSMultipleLinearRegression regression = new GLSMultipleLinearRegression();
double[] y = new double[]{11.0, 12.0, 13.0, 14.0, 15.0, 16.0};
double[][] x = new double[6][];
x[0] = new double[]{0, 0, 0, 0, 0};
x[1] = new double[]{2.0, 0, 0, 0, 0};
x[2] = new double[]{0, 3.0, 0, 0, 0};
x[3] = new double[]{0, 0, 4.0, 0, 0};
x[4] = new double[]{0, 0, 0, 5.0, 0};
x[5] = new double[]{0, 0, 0, 0, 6.0};
double[][] omega = new double[6][];
omega[0] = new double[]{1.1, 0, 0, 0, 0, 0};
omega[1] = new double[]{0, 2.2, 0, 0, 0, 0};
omega[2] = new double[]{0, 0, 3.3, 0, 0, 0};
omega[3] = new double[]{0, 0, 0, 4.4, 0, 0};
omega[4] = new double[]{0, 0, 0, 0, 5.5, 0};
omega[5] = new double[]{0, 0, 0, 0, 0, 6.6};
regression.newSampleData(y, x, omega);
          
```

<a id="userguide-stat--1.6-rank-transformations"></a>

### 1.6 Rank transformations

Some statistical algorithms require that input data be replaced by ranks.
The [org.apache.commons.math4.stat.ranking](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/package-summary.html) package provides rank transformation.
[RankingAlgorithm](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/RankingAlgorithm.html) defines the interface for ranking.
[NaturalRanking](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/NaturalRanking.html) provides an implementation that has two configuration options.

- [Ties strategy](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/TiesStrategy.html) deterimines how ties in the source data are handled by the ranking
- [NaN strategy](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/NaNStrategy.html) determines how NaN values in the source data are handled.

Examples:

```

NaturalRanking ranking = new NaturalRanking(NaNStrategy.MINIMAL,
TiesStrategy.MAXIMUM);
double[] data = { 20, 17, 30, 42.3, 17, 50,
                  Double.NaN, Double.NEGATIVE_INFINITY, 17 };
double[] ranks = ranking.rank(exampleData);
         
```

results in `ranks` containing `{6, 5, 7, 8, 5, 9, 2, 2, 5}.`

```

new NaturalRanking(NaNStrategy.REMOVED,TiesStrategy.SEQUENTIAL).rank(exampleData);
         
```

returns `{5, 2, 6, 7, 3, 8, 1, 4}.`

The default `NaNStrategy` is NaNStrategy.MAXIMAL. This makes `NaN`
values larger than any other value (including `Double.POSITIVE_INFINITY`). The
default `TiesStrategy` is `TiesStrategy.AVERAGE,` which assigns tied
values the average of the ranks applicable to the sequence of ties. See the
[NaturalRanking](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/NaturalRanking.html) for more examples and [TiesStrategy](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/TiesStrategy.html) and [NaNStrategy](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/NaNStrategy.html)
for details on these configuration options.

<a id="userguide-stat--1.7-covariance-and-correlation"></a>

### 1.7 Covariance and correlation

The [org.apache.commons.math4.stat.correlation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/package-summary.html) package computes covariances
and correlations for pairs of arrays or columns of a matrix.
[Covariance](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/Covariance.html) computes covariances, [PearsonsCorrelation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/PearsonsCorrelation.html) provides Pearson's Product-Moment correlation coefficients, [SpearmansCorrelation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/SpearmansCorrelation.html) computes Spearman's rank correlation and
[KendallsCorrelation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/KendallsCorrelation.html) computes Kendall's tau rank correlation.

**Implementation Notes**

- Unbiased covariances are given by the formula
  `cov(X, Y) = sum [(xi - E(X))(yi - E(Y))] / (n - 1)`
  where `E(X)` is the mean of `X` and `E(Y)`
  is the mean of the `Y` values. Non-bias-corrected estimates use
  `n` in place of `n - 1.` Whether or not covariances are
  bias-corrected is determined by the optional parameter, "biasCorrected," which
  defaults to `true.`
- [PearsonsCorrelation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/PearsonsCorrelation.html) computes correlations defined by the formula
  `cor(X, Y) = sum[(xi - E(X))(yi - E(Y))] / [(n - 1)s(X)s(Y)]`
  where `E(X)` and `E(Y)` are means of `X` and `Y`
  and `s(X)`, `s(Y)` are standard deviations.
- [SpearmansCorrelation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/SpearmansCorrelation.html) applies a rank transformation to the input data and computes Pearson's
  correlation on the ranked data. The ranking algorithm is configurable. By default,
  [NaturalRanking](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/ranking/NaturalRanking.html) with default strategies for handling ties and NaN values is used.
- [KendallsCorrelation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/correlation/KendallsCorrelation.html) computes the association between two measured quantities. A tau test
  is a non-parametric hypothesis test for statistical dependence based on the tau coefficient.

**Examples:**

**Covariance of 2 arrays**
:   To compute the unbiased covariance between 2 double arrays,
    `x` and `y`, use:


```

new Covariance().covariance(x, y)
          
```

    For non-bias-corrected covariances, use


```

covariance(x, y, false)
          
```

**Covariance matrix**
:   A covariance matrix over the columns of a source matrix `data`
    can be computed using


```

new Covariance().computeCovarianceMatrix(data)
          
```

    The i-jth entry of the returned matrix is the unbiased covariance of the ith and jth
    columns of `data.` As above, to get non-bias-corrected covariances,
    use


```

computeCovarianceMatrix(data, false)
         
```

**Pearson's correlation of 2 arrays**
:   To compute the Pearson's product-moment correlation between two double arrays
    `x` and `y`, use:


```

new PearsonsCorrelation().correlation(x, y)
          
```

**Pearson's correlation matrix**
:   A (Pearson's) correlation matrix over the columns of a source matrix `data`
    can be computed using


```

new PearsonsCorrelation().computeCorrelationMatrix(data)
          
```

    The i-jth entry of the returned matrix is the Pearson's product-moment correlation between the
    ith and jth columns of `data.`

**Pearson's correlation significance and standard errors**
:   To compute standard errors and/or significances of correlation coefficients
    associated with Pearson's correlation coefficients, start by creating a
    `PearsonsCorrelation` instance


```

PearsonsCorrelation correlation = new PearsonsCorrelation(data);
          
```

    where `data` is either a rectangular array or a `RealMatrix.`
    Then the matrix of standard errors is


```

correlation.getCorrelationStandardErrors();
          
```

    The formula used to compute the standard error is
    `SEr = ((1 - r2) / (n - 2))1/2`
    where `r` is the estimated correlation coefficient and
    `n` is the number of observations in the source dataset.
    **p-values** for the (2-sided) null hypotheses that elements of
    a correlation matrix are zero populate the RealMatrix returned by


```

correlation.getCorrelationPValues()
          
```

    `getCorrelationPValues().getEntry(i,j)` is the
    probability that a random variable distributed as `tn-2` takes
    a value with absolute value greater than or equal to
    `|rij|((n - 2) / (1 - rij2))1/2`,
    where `rij` is the estimated correlation between the ith and jth
    columns of the source array or RealMatrix. This is sometimes referred to as the
    *significance* of the coefficient.
    For example, if `data` is a RealMatrix with 2 columns and 10 rows, then


```

new PearsonsCorrelation(data).getCorrelationPValues().getEntry(0,1)
          
```

    is the significance of the Pearson's correlation coefficient between the two columns
    of `data`. If this value is less than .01, we can say that the correlation
    between the two columns of data is significant at the 99% level.

**Spearman's rank correlation coefficient**
:   To compute the Spearman's rank-moment correlation between two double arrays
    `x` and `y`:


```

new SpearmansCorrelation().correlation(x, y)
          
```

    This is equivalent to


```

RankingAlgorithm ranking = new NaturalRanking();
new PearsonsCorrelation().correlation(ranking.rank(x), ranking.rank(y))
          
```

**Kendalls's tau rank correlation coefficient**
:   To compute the Kendall's tau rank correlation between two double arrays
    `x` and `y`:


```

new KendallsCorrelation().correlation(x, y)
          
```

<a id="userguide-stat--1.8-statistical-tests"></a>

### 1.8 Statistical tests

The [org.apache.commons.math4.stat.inference](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/) package provides implementations for
[Student's t](http://www.itl.nist.gov/div898/handbook/prc/section2/prc22.htm), [Chi-Square](http://www.itl.nist.gov/div898/handbook/eda/section3/eda35f.htm), [G Test](http://en.wikipedia.org/wiki/G-test), [One-Way ANOVA](http://www.itl.nist.gov/div898/handbook/prc/section4/prc43.htm), [Mann-Whitney U](http://www.itl.nist.gov/div898/handbook/prc/section3/prc35.htm), [Wilcoxon signed rank](http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test) and
[Binomial](http://en.wikipedia.org/wiki/Binomial_test) test statistics as well as
[p-values](http://www.cas.lancs.ac.uk/glossary_v1.1/hyptest.html#pvalue) associated with `t-`, `Chi-Square`, `G`, `One-Way ANOVA`, `Mann-Whitney U`
`Wilcoxon signed rank`, and `Kolmogorov-Smirnov` tests.
The respective test classes are
[TTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/TTest.html), [ChiSquareTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/ChiSquareTest.html), [GTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/GTest.html), [OneWayAnova](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/OneWayAnova.html), [MannWhitneyUTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/MannWhitneyUTest.html), [WilcoxonSignedRankTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/WilcoxonSignedRankTest.html), [BinomialTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/BinomialTest.html) and
[KolmogorovSmirnovTest](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/KolmogorovSmirnovTest.html).
The [TestUtils](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/inference/TestUtils.html) class provides static methods to get test instances or
to compute test statistics directly. The examples below all use the
static methods in `TestUtils` to execute tests. To get
test object instances, either use e.g., `TestUtils.getTTest()`
or use the implementation constructors directly, e.g. `new TTest()`.

**Implementation Notes**

- Both one- and two-sample t-tests are supported. Two sample tests
  can be either paired or unpaired and the unpaired two-sample tests can
  be conducted under the assumption of equal subpopulation variances or
  without this assumption. When equal variances is assumed, a pooled
  variance estimate is used to compute the t-statistic and the degrees
  of freedom used in the t-test equals the sum of the sample sizes minus 2.
  When equal variances is not assumed, the t-statistic uses both sample
  variances and the
  [Welch-Satterwaite approximation](http://www.itl.nist.gov/div898/handbook/prc/section3/gifs/nu3.gif) is used to compute the degrees
  of freedom. Methods to return t-statistics and p-values are provided in each
  case, as well as boolean-valued methods to perform fixed significance
  level tests. The names of methods or methods that assume equal
  subpopulation variances always start with "homoscedastic." Test or
  test-statistic methods that just start with "t" do not assume equal
  variances. See the examples below and the API documentation for
  more details.
- The validity of the p-values returned by the t-test depends on the
  assumptions of the parametric t-test procedure, as discussed
  [here](http://www.basic.nwu.edu/statguidefiles/ttest_unpaired_ass_viol.html)
- p-values returned by t-, chi-square and ANOVA tests are exact, based
  on numerical approximations to the t-, chi-square and F distributions in the
  `distributions` package.
- The G test implementation provides two p-values:
  `gTest(expected, observed)`, which is the tail probability beyond
  `g(expected, observed)` in the ChiSquare distribution with degrees
  of freedom one less than the common length of input arrays and
  `gTestIntrinsic(expected, observed)` which is the same tail
  probability computed using a ChiSquare distribution with one less degeree
  of freedom.
- p-values returned by t-tests are for two-sided tests and the boolean-valued
  methods supporting fixed significance level tests assume that the hypotheses
  are two-sided. One sided tests can be performed by dividing returned p-values
  (resp. critical values) by 2.
- Degrees of freedom for G- and chi-square tests are integral values, based on the
  number of observed or expected counts (number of observed counts - 1).
- The KolmogorovSmirnov test uses a statistic based on the maximum deviation of
  the empirical distribution of sample data points from the distribution expected
  under the null hypothesis. Specifically, what is computed is
  \(D\_n=\sup\_x |F\_n(x)-F(x)|\), where \(F\) is the expected distribution and
  \(F\_n\) is the empirical distribution of the \(n\) sample data points. Both
  one-sample tests against a `RealDistribution` and two-sample tests
  (comparing two empirical distributions) are supported. For one-sample tests,
  the distribution of \(D\_n\) is estimated using the method in
  [Evaluating Kolmogorov's Distribution](http://www.jstatsoft.org/v08/i18/) by
  George Marsaglia, Wai Wan Tsang, and Jingbo Wang, with quick decisions in some cases
  for extreme values using the method described in
   [Computing the Two-Sided Kolmogorov-Smirnov
  Distribution](http://www.jstatsoft.org/v39/i11/) by Richard Simard and Pierre L'Ecuyer. In the 2-sample case, estimation
  by default depends on the number of data points. For small samples, the distribution
  is computed exactly and for large samples a numerical approximation of the Kolmogorov
  distribution is used. Methods to perform each type of p-value estimation are also exposed
  directly. See the class javadoc for details.

**Examples:**

**One-sample `t` tests**
:   To compare the mean of a double[] array to a fixed value:


```

double[] observed = {1d, 2d, 3d};
double mu = 2.5d;
System.out.println(TestUtils.t(mu, observed));
          
```

    The code above will display the t-statistic associated with a one-sample
    t-test comparing the mean of the `observed` values against
    `mu.`
:   To compare the mean of a dataset described by a
    [StatisticalSummary](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/stat/descriptive/StatisticalSummary.html) to a fixed value:


```

double[] observed ={1d, 2d, 3d};
double mu = 2.5d;
SummaryStatistics sampleStats = new SummaryStatistics();
for (int i = 0; i < observed.length; i++) {
    sampleStats.addValue(observed[i]);
}
System.out.println(TestUtils.t(mu, observed));
```

:   To compute the p-value associated with the null hypothesis that the mean
    of a set of values equals a point estimate, against the two-sided alternative that
    the mean is different from the target value:


```

double[] observed = {1d, 2d, 3d};
double mu = 2.5d;
System.out.println(TestUtils.tTest(mu, observed));
           
```

    The snippet above will display the p-value associated with the null
    hypothesis that the mean of the population from which the
    `observed` values are drawn equals `mu.`
:   To perform the test using a fixed significance level, use:


```

TestUtils.tTest(mu, observed, alpha);
          
```

    where `0 < alpha < 0.5` is the significance level of
    the test. The boolean value returned will be `true` iff the
    null hypothesis can be rejected with confidence `1 - alpha`.
    To test, for example at the 95% level of confidence, use
    `alpha = 0.05`

**Two-Sample t-tests**
:   **Example 1:** Paired test evaluating
    the null hypothesis that the mean difference between corresponding
    (paired) elements of the `double[]` arrays
    `sample1` and `sample2` is zero.

    To compute the t-statistic:


```

TestUtils.pairedT(sample1, sample2);
          
```

    To compute the p-value:


```

TestUtils.pairedTTest(sample1, sample2);
           
```

    To perform a fixed significance level test with alpha = .05:


```

TestUtils.pairedTTest(sample1, sample2, .05);
           
```

    The last example will return `true` iff the p-value
    returned by `TestUtils.pairedTTest(sample1, sample2)`
    is less than `.05`
:   **Example 2:**  unpaired, two-sided, two-sample t-test using
    `StatisticalSummary` instances, without assuming that
    subpopulation variances are equal.

    First create the `StatisticalSummary` instances. Both
    `DescriptiveStatistics` and `SummaryStatistics`
    implement this interface. Assume that `summary1` and
    `summary2` are `SummaryStatistics` instances,
    each of which has had at least 2 values added to the (virtual) dataset that
    it describes. The sample sizes do not have to be the same -- all that is required
    is that both samples have at least 2 elements.

    **Note:** The `SummaryStatistics` class does
    not store the dataset that it describes in memory, but it does compute all
    statistics necessary to perform t-tests, so this method can be used to
    conduct t-tests with very large samples. One-sample tests can also be
    performed this way.
    (See [Descriptive statistics](#userguide-stat--a1.2_descriptive_statistics) for details
    on the `SummaryStatistics` class.)

    To compute the t-statistic:


```

TestUtils.t(summary1, summary2);
          
```

    To compute the p-value:


```

TestUtils.tTest(sample1, sample2);
           
```

    To perform a fixed significance level test with alpha = .05:


```

TestUtils.tTest(sample1, sample2, .05);
           
```

    In each case above, the test does not assume that the subpopulation
    variances are equal. To perform the tests under this assumption,
    replace "t" at the beginning of the method name with "homoscedasticT"

**Chi-square tests**
:   To compute a chi-square statistic measuring the agreement between a
    `long[]` array of observed counts and a `double[]`
    array of expected counts, use:


```

long[] observed = {10, 9, 11};
double[] expected = {10.1, 9.8, 10.3};
System.out.println(TestUtils.chiSquare(expected, observed));
          
```

    the value displayed will be
    `sum((expected[i] - observed[i])^2 / expected[i])`
:   To get the p-value associated with the null hypothesis that
    `observed` conforms to `expected` use:


```

TestUtils.chiSquareTest(expected, observed);
          
```

:   To test the null hypothesis that `observed` conforms to
    `expected` with `alpha` significance level
    (equiv. `100 * (1-alpha)%` confidence) where `0 < alpha < 1`  use:


```

TestUtils.chiSquareTest(expected, observed, alpha);
          
```

    The boolean value returned will be `true` iff the null hypothesis
    can be rejected with confidence `1 - alpha`.
:   To compute a chi-square statistic statistic associated with a
    [chi-square test of independence](http://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm) based on a two-dimensional (long[][])
    `counts` array viewed as a two-way table, use:


```

TestUtils.chiSquareTest(counts);
          
```

    The rows of the 2-way table are
    `count[0], ... , count[count.length - 1].`
    The chi-square statistic returned is
    `sum((counts[i][j] - expected[i][j])^2/expected[i][j])`
    where the sum is taken over all table entries and
    `expected[i][j]` is the product of the row and column sums at
    row `i`, column `j` divided by the total count.
:   To compute the p-value associated with the null hypothesis that
    the classifications represented by the counts in the columns of the input 2-way
    table are independent of the rows, use:


```

 TestUtils.chiSquareTest(counts);
          
```

:   To perform a chi-square test of independence with `alpha`
    significance level (equiv. `100 * (1-alpha)%` confidence)
    where `0 < alpha < 1`  use:


```

TestUtils.chiSquareTest(counts, alpha);
          
```

    The boolean value returned will be `true` iff the null
    hypothesis can be rejected with confidence `1 - alpha`.

**G tests**
:   G tests are an alternative to chi-square tests that are recommended
    when observed counts are small and / or incidence probabilities for
    some cells are small. See Ted Dunning's paper,
    [Accurate Methods for the Statistics of Surprise and Coincidence](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.14.5962) for
    background and an empirical analysis showing now chi-square
    statistics can be misleading in the presence of low incidence probabilities.
    This paper also derives the formulas used in computing G statistics and the
    root log likelihood ratio provided by the `GTest` class.
:   To compute a G-test statistic measuring the agreement between a
    `long[]` array of observed counts and a `double[]`
    array of expected counts, use:


```

double[] expected = new double[]{0.54d, 0.40d, 0.05d, 0.01d};
long[] observed = new long[]{70, 79, 3, 4};
System.out.println(TestUtils.g(expected, observed));
          
```

    the value displayed will be
    `2 * sum(observed[i]) * log(observed[i]/expected[i])`
:   To get the p-value associated with the null hypothesis that
    `observed` conforms to `expected` use:


```

TestUtils.gTest(expected, observed);
          
```

:   To test the null hypothesis that `observed` conforms to
    `expected` with `alpha` siginficance level
    (equiv. `100 * (1-alpha)%` confidence) where `0 < alpha < 1`  use:


```

TestUtils.gTest(expected, observed, alpha);
          
```

    The boolean value returned will be `true` iff the null hypothesis
    can be rejected with confidence `1 - alpha`.
:   To evaluate the hypothesis that two sets of counts come from the
    same underlying distribution, use long[] arrays for the counts and
    `gDataSetsComparison` for the test statistic


```

long[] obs1 = new long[]{268, 199, 42};
long[] obs2 = new long[]{807, 759, 184};
System.out.println(TestUtils.gDataSetsComparison(obs1, obs2)); // G statistic
System.out.println(TestUtils.gTestDataSetsComparison(obs1, obs2)); // p-value
          
```

:   For 2 x 2 designs, the `rootLogLikelihoodRatio` method
    computes the
    [signed root log likelihood ratio.](http://tdunning.blogspot.com/2008/03/surprise-and-coincidence.html) For example, suppose that for two events
    A and B, the observed count of AB (both occurring) is 5, not A and B (B without A)
    is 1995, A not B is 0; and neither A nor B is 10000. Then


```

new GTest().rootLogLikelihoodRatio(5, 1995, 0, 100000);
          
```

    returns the root log likelihood associated with the null hypothesis that A
    and B are independent.

**One-Way ANOVA tests**
: ```

double[] classA =
   {93.0, 103.0, 95.0, 101.0, 91.0, 105.0, 96.0, 94.0, 101.0 };
double[] classB =
   {99.0, 92.0, 102.0, 100.0, 102.0, 89.0 };
double[] classC =
   {110.0, 115.0, 111.0, 117.0, 128.0, 117.0 };
List classes = new ArrayList();
classes.add(classA);
classes.add(classB);
classes.add(classC);
          
```

    Then you can compute ANOVA F- or p-values associated with the
    null hypothesis that the class means are all the same
    using a `OneWayAnova` instance or `TestUtils`
    methods:


```

double fStatistic = TestUtils.oneWayAnovaFValue(classes); // F-value
double pValue = TestUtils.oneWayAnovaPValue(classes);     // P-value
          
```

    To test perform a One-Way ANOVA test with significance level set at 0.01
    (so the test will, assuming assumptions are met, reject the null
    hypothesis incorrectly only about one in 100 times), use


```

TestUtils.oneWayAnovaTest(classes, 0.01); // returns a boolean
                                          // true means reject null hypothesis
          
```

**Kolmogorov-Smirnov tests**
:   Given a double[] array `data` of values, to evaluate the
    null hypothesis that the values are drawn from a unit normal distribution


```

final NormalDistribution unitNormal = new NormalDistribution(0d, 1d);
TestUtils.kolmogorovSmirnovTest(unitNormal, sample, false)
          
```

    returns the p-value and


```

TestUtils.kolmogorovSmirnovStatistic(unitNormal, sample)
          
```

    returns the D-statistic.
    If `y` is a double array, to evaluate the null hypothesis that
    `x` and `y` are drawn from the same underlying distribution,
    use


```

TestUtils.kolmogorovSmirnovStatistic(x, y)
          
```

    to compute the D-statistic and


```

TestUtils.kolmogorovSmirnovTest(x, y)
          
```

    for the p-value associated with the null hypothesis that `x` and
    `y` come from the same distribution. By default, here and above strict
    inequality is used in the null hypothesis - i.e., we evaluate \(H\_0 : D\_{n,m} > d \).
    To make the inequality above non-strict, add `false` as an actual parameter
    above. For large samples, this parameter makes no difference.
    To force exact computation of the p-value (overriding the selection of estimation
    method), first compute the d-statistic and then use the `exactP` method


```

final double d = TestUtils.kolmogorovSmirnovStatistic(x, y);
TestUtils.exactP(d, x.length, y.length, false)
          
```

    assuming that the non-strict form of the null hypothesis is desired. Note, however,
    that exact computation for large samples takes a long time.

---

<a id="userguide-random"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/random.html -->

<!-- page_index: 8 -->

<a id="userguide-random--2-data-generation"></a>

## 2 Data Generation

<a id="userguide-random--2.1-overview"></a>

### 2.1 Overview

Utilities in package [o.a.c.m.legacy.random](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/random/package-summary.html) often uses an underlying "source of randomness": A pseudo-random
number generator (PRNG) that produces sequences of numbers that are uniformly distributed
within their range.
Commons Math depends on [Commons RNG](http://commons.apache.org/rng) for the
PRNG implementations.

<a id="userguide-random--2.2-correlated-random-vectors"></a>

### 2.2 Correlated random vectors

Some algorithms require random vectors instead of random scalars.
When the components of these vectors are uncorrelated, they may be generated
simply one at a time and packed together in the vector.

When the components are correlated however, generating them is more difficult.
The [CorrelatedVectorFactory](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/random/CorrelatedVectorFactory.html) class provides this service.
In this case, a complete covariance matrix must be provided (instead of a
simple standard deviations vector) gathering both the variance and the
correlation information of the probability law.

The main use for correlated random vector generation is for Monte-Carlo
simulation of physical problems with several variables, for example to
generate error vectors to be added to a nominal vector. A particularly
common case is when the generated vector should be drawn from a [Multivariate Normal Distribution](http://en.wikipedia.org/wiki/Multivariate_normal_distribution).

Generating random vectors from a bivariate normal distribution:

```

import java.util.function.Supplier;
import org.apache.commons.rng.UniformRandomProvider;
import org.apache.commons.rng.RandomSource;

// Import common PRNG interface and factory class that instantiates the PRNG.
// Create (and possibly seed) a PRNG.
long seed = 17399225432L; // Fixed seed means same results every time
UniformRandomProvider rng = RandomSource.create(RandomSource.MT, seed);

// Create a a factory of correlated vectors.
CorrelatedVectorFactory factory = new CorrelatedVectorFactory(mean, covariance, 1e-12);
Supplier<double[]> generator = factory.gaussian(rng);

// Use the generator to generate correlated vectors.
double[] randomVector = generator.get();
... 
```

The `mean` argument is a `double[]` array holding the means
of the random vector components. In the bivariate case, it must have length 2.
The `covariance` argument is a `RealMatrix`, which has to
be 2 x 2.
The main diagonal elements are the variances of the vector components and the
off-diagonal elements are the covariances.
For example, if the means are 1 and 2 respectively, and the desired standard deviations
are 3 and 4, respectively, then we need to use

```

double[] mean = {1, 2};
double[][] cov = {{9, c}, {c, 16}};
RealMatrix covariance = MatrixUtils.createRealMatrix(cov);
      
```

where "c" is the desired covariance. If you are starting with a desired correlation, you need to translate this to a covariance by multiplying it by the product of the
standard deviations. For example, if you want to generate data that will give Pearson's
R of 0.5, you would use c = 3 \* 4 \* 0.5 = 6.

<a id="userguide-random--2.3-low-discrepancy-sequences"></a>

### 2.3 Low discrepancy sequences

There exist several quasi-random sequences with the property that for all values of N, the subsequence
x1, ..., xN has low discrepancy, which results in equi-distributed samples.
While their quasi-randomness makes them unsuitable for most applications (i.e. the sequence of values
is completely deterministic), their unique properties give them an important advantage for quasi-Monte Carlo simulations.
Currently, the following low-discrepancy sequences are supported:

- [Sobol sequence](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/random/SobolSequenceGenerator.html) (pre-configured up to dimension 1000)
- [Halton sequence](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/random/HaltonSequenceGenerator.html) (pre-configured up to dimension 40)

```

// Create a Sobol sequence generator for 2-dimensional vectors
RandomVectorGenerator generator = new SobolSequence(2);

// Use the generator to generate vectors
double[] randomVector = generator.nextVector();
... 
```

The figure below illustrates the unique properties of low-discrepancy sequences when
generating N samples in the interval [0, 1]. Roughly speaking, such sequences "fill"
the respective space more evenly which leads to faster convergence in quasi-Monte Carlo
simulations.
![Comparison of low-discrepancy sequences](assets/images/low-discrepancy-sequences_3b901cef9f6653b9.png)

---

<a id="userguide-linear"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/linear.html -->

<!-- page_index: 9 -->

<a id="userguide-linear--3-linear-algebra"></a>

## 3 Linear Algebra

<a id="userguide-linear--3.1-overview"></a>

### 3.1 Overview

Linear algebra support in commons-math provides operations on real matrices
(both dense and sparse matrices are supported) and vectors. It features basic
operations (addition, subtraction ...) and decomposition algorithms that can
be used to solve linear systems either in exact sense and in least squares sense.

<a id="userguide-linear--3.2-real-matrices"></a>

### 3.2 Real matrices

The [RealMatrix](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/RealMatrix.html) interface represents a matrix with real numbers as
entries. The following basic matrix operations are supported:

- Matrix addition, subtraction, multiplication
- Scalar addition and multiplication
- transpose
- Norm and Trace
- Operation on a vector

Example:

```

// Create a real matrix with two rows and three columns, using a factory
// method that selects the implementation class for us.
double[][] matrixData = { {1d,2d,3d}, {2d,5d,3d}};
RealMatrix m = MatrixUtils.createRealMatrix(matrixData);

// One more with three rows, two columns, this time instantiating the
// RealMatrix implementation class directly.
double[][] matrixData2 = { {1d,2d}, {2d,5d}, {1d, 7d}};
RealMatrix n = new Array2DRowRealMatrix(matrixData2);

// Note: The constructor copies  the input double[][] array in both cases.

// Now multiply m by n
RealMatrix p = m.multiply(n);
System.out.println(p.getRowDimension());    // 2
System.out.println(p.getColumnDimension()); // 2

// Invert p, using LU decomposition
RealMatrix pInverse = new LUDecomposition(p).getSolver().getInverse();
         
```

The three main implementations of the interface are [Array2DRowRealMatrix](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/Array2DRowRealMatrix.html) and [BlockRealMatrix](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/BlockRealMatrix.html) for dense matrices (the second one being more suited to
dimensions above 50 or 100) and [SparseRealMatrix](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/SparseRealMatrix.html) for sparse matrices.

<a id="userguide-linear--3.3-real-vectors"></a>

### 3.3 Real vectors

The [RealVector](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/RealVector.html) interface represents a vector with real numbers as
entries. The following basic matrix operations are supported:

- Vector addition, subtraction
- Element by element multiplication, division
- Scalar addition, subtraction, multiplication, division and power
- Mapping of mathematical functions (cos, sin ...)
- Dot product, outer product
- Distance and norm according to norms L1, L2 and Linf

The [RealVectorFormat](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/RealVectorFormat.html) class handles input/output of vectors in a customizable
textual format.

<a id="userguide-linear--3.4-solving-linear-systems"></a>

### 3.4 Solving linear systems

The `solve()` methods of the [DecompositionSolver](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/DecompositionSolver.html)
interface support solving linear systems of equations of the form AX=B, either
in linear sense or in least square sense. A `RealMatrix` instance is
used to represent the coefficient matrix of the system. Solving the system is a
two phases process: first the coefficient matrix is decomposed in some way and
then a solver built from the decomposition solves the system. This allows to
compute the decomposition and build the solver only once if several systems have
to be solved with the same coefficient matrix.

For example, to solve the linear system

```

           2x + 3y - 2z = 1
           -x + 7y + 6z = -2
           4x - 3y - 5z = 1
          
```

Start by decomposing the coefficient matrix A (in this case using LU decomposition)
and build a solver

```

RealMatrix coefficients =
    new Array2DRowRealMatrix(new double[][] { { 2, 3, -2 }, { -1, 7, 6 }, { 4, -3, -5 } },
                       false);
DecompositionSolver solver = new LUDecomposition(coefficients).getSolver();
          
```

Next create a `RealVector` array to represent the constant
vector B and use `solve(RealVector)` to solve the system

```

RealVector constants = new ArrayRealVector(new double[] { 1, -2, 1 }, false);
RealVector solution = solver.solve(constants);
          
```

The `solution` vector will contain values for x
(`solution.getEntry(0)`), y (`solution.getEntry(1)`), and z (`solution.getEntry(2)`) that solve the system.

Each type of decomposition has its specific semantics and constraints on
the coefficient matrix as shown in the following table. For algorithms that
solve AX=B in least squares sense the value returned for X is such that the
residual AX-B has minimal norm. Least Square sense means a solver can be computed
for an overdetermined system, (i.e. a system with more equations than unknowns, which corresponds to a tall A matrix with more rows than columns). If an exact
solution exist (i.e. if for some X the residual AX-B is exactly 0), then this
exact solution is also the solution in least square sense. This implies that
algorithms suited for least squares problems can also be used to solve exact
problems, but the reverse is not true. In any case, if the matrix is singular
within the tolerance set at construction, an error will be triggered when
the solve method will be called, both for algorithms that compute exact solutions
and for algorithms that compute least square solutions.

<table align="center" border="1" class="bodyTable">
<tr>
<td align="center" colspan="3">Decomposition algorithms</td></tr>
<tr>
<td align="center">Name</td>
<td>coefficients matrix</td>
<td>problem type</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/LUDecomposition.html">LU</a></td>
<td>square</td>
<td>exact solution only</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/CholeskyDecomposition.html">Cholesky</a></td>
<td>symmetric positive definite</td>
<td>exact solution only</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/QRDecomposition.html">QR</a></td>
<td>any</td>
<td>least squares solution</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/EigenDecomposition.html">eigen decomposition</a></td>
<td>square</td>
<td>exact solution only</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/linear/SingularValueDecomposition.html">SVD</a></td>
<td>any</td>
<td>least squares solution</td></tr>
</table>

It is possible to use a simple array of double instead of a `RealVector`.
In this case, the solution will be provided also as an array of double.

It is possible to solve multiple systems with the same coefficient matrix
in one method call. To do this, create a matrix whose column vectors correspond
to the constant vectors for the systems to be solved and use `solve(RealMatrix),`
which returns a matrix with column vectors representing the solutions.

<a id="userguide-linear--3.5-eigenvalues-eigenvectors-and-singular-values-singular-vectors"></a>

### 3.5 Eigenvalues/eigenvectors and singular values/singular vectors

Decomposition algorithms may be used for themselves and not only for linear system solving.
This is of prime interest with eigen decomposition and singular value decomposition.

The `getEigenvalue()`, `getEigenvalues()`, `getEigenVector()`, `getV()`, `getD()` and `getVT()` methods of the
`EigenDecomposition` interface support solving eigenproblems of the form
AX = lambda X where lambda is a real scalar.

The `getSingularValues()`, `getU()`, `getS()` and
`getV()` methods of the `SingularValueDecomposition` interface
allow to solve singular values problems of the form AXi = lambda Yi where lambda is a
real scalar, and where the Xi and Yi vectors form orthogonal bases of their respective
vector spaces (which may have different dimensions).

Copyright © 2003-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Math, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="userguide-analysis"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/analysis.html -->

<!-- page_index: 10 -->

<a id="userguide-analysis--4-numerical-analysis"></a>

## 4 Numerical Analysis

<a id="userguide-analysis--4.1-overview"></a>

### 4.1 Overview

The analysis package is the parent package for algorithms dealing with
real-valued functions of one real variable. It contains dedicated sub-packages
providing numerical root-finding, integration, interpolation and differentiation.
It also contains a polynomials sub-package that considers polynomials with real
coefficients as differentiable real functions.

Functions interfaces are intended to be implemented by user code to represent
their domain problems. The algorithms provided by the library will then operate
on these function to find their roots, or integrate them, or ... Functions can
be multivariate or univariate, real vectorial or matrix valued, and they can be
differentiable or not.

<a id="userguide-analysis--4.2-error-handling"></a>

### 4.2 Error handling

For user-defined functions, when the method encounters an error
during evaluation, users must use their *own* unchecked exceptions.
The following example shows the recommended way to do that, using root
solving as the example (the same construct should be used for ODE
integrators or for optimizations).

```
private static class LocalException extends RuntimeException {
// the x value that caused the problem private final double x;
public LocalException(double x) {this.x = x;}
public double getX() {return x;}
}
private static class MyFunction implements UnivariateFunction {public double value(double x) {double y = hugeFormula(x); if (somethingBadHappens) {throw new LocalException(x);} return y;}}
public void compute() {try {solver.solve(maxEval, new MyFunction(a, b, c), min, max); } catch (LocalException le) {// retrieve the x value}}
```

As shown in this example the exception is really something local to user code
and there is a guarantee Apache Commons Math will not mess with it.
The user is safe.

<a id="userguide-analysis--4.3-root-finding"></a>

### 4.3 Root-finding

[UnivariateSolver](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/UnivariateSolver.html), [UnivariateDifferentiableSolver](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/UnivariateDifferentiableSolver.html) and [PolynomialSolver](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/PolynomialSolver.html) provide means to find roots of
[univariate real-valued functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html), [differentiable univariate real-valued functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateDifferentiable.html), and [polynomial functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/polynomials/PolynomialFunction.html) respectively.
A root is the value where the function takes the value 0. Commons-Math
includes implementations of the several root-finding algorithms:

<table align="center" border="1" class="bodyTable">
<tr>
<td align="center" colspan="5">Root solvers</td></tr>
<tr>
<td align="center">Name</td>
<td>Function type</td>
<td>Convergence</td>
<td>Needs initial bracketing</td>
<td>Bracket side selection</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/BisectionSolver.html">Bisection</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>linear, guaranteed</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/BrentSolver.html">Brent-Dekker</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>super-linear, guaranteed</td>
<td>yes</td>
<td>no</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/BracketingNthOrderBrentSolver.html">bracketing nth order Brent</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>variable order, guaranteed</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/IllinoisSolver.html">Illinois Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>super-linear, guaranteed</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/LaguerreSolver.html">Laguerre's Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/polynomials/PolynomialFunction.html">polynomial functions</a></td>
<td>cubic for simple root, linear for multiple root</td>
<td>yes</td>
<td>no</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/MullerSolver.html">Muller's Method</a> using bracketing to deal with real-valued functions</td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>quadratic close to roots</td>
<td>yes</td>
<td>no</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/MullerSolver2.html">Muller's Method</a> using modulus to deal with real-valued functions</td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>quadratic close to root</td>
<td>yes</td>
<td>no</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/NewtonRaphsonSolver.html">Newton-Raphson's Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateDifferentiableFunction.html">differentiable univariate real-valued functions</a></td>
<td>quadratic, non-guaranteed</td>
<td>no</td>
<td>no</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/PegasusSolver.html">Pegasus Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>super-linear, guaranteed</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/RegulaFalsiSolver.html">Regula Falsi (false position) Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>linear, guaranteed</td>
<td>yes</td>
<td>yes</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/RiddersSolver.html">Ridder's Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>super-linear</td>
<td>yes</td>
<td>no</td>
</tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/SecantSolver.html">Secant Method</a></td>
<td><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html">univariate real-valued functions</a></td>
<td>super-linear, non-guaranteed</td>
<td>yes</td>
<td>no</td>
</tr>
</table>

Some algorithms require that the initial search interval brackets the root
(i.e. the function values at interval end points have opposite signs). Some
algorithms preserve bracketing throughout computation and allow user to
specify which side of the convergence interval to select as the root. It is
also possible to force a side selection after a root has been found even
for algorithms that do not provide this feature by themselves. This is
useful for example in sequential search, for which a new search interval is
started after a root has been found in order to find the next root. In this
case, user must select a side to ensure his loop is not stuck on one root
and always return the same solution without making any progress.

There are numerous non-obvious traps and pitfalls in root finding.
First, the usual disclaimers due to the way real world computers
calculate values apply. If the computation of the function provides
numerical instabilities, for example due to bit cancellation, the root
finding algorithms may behave badly and fail to converge or even
return bogus values. There will not necessarily be an indication that
the computed root is way off the true value. Secondly, the root finding
problem itself may be inherently ill-conditioned. There is a
"domain of indeterminacy", the interval for which the function has
near zero absolute values around the true root, which may be large.
Even worse, small problems like roundoff error may cause the function
value to "numerically oscillate" between negative and positive values.
This may again result in roots way off the true value, without
indication. There is not much a generic algorithm can do if
ill-conditioned problems are met. A way around this is to transform
the problem in order to get a better conditioned function. Proper
selection of a root-finding algorithm and its configuration parameters
requires knowledge of the analytical properties of the function under
analysis and numerical analysis techniques. Users are encouraged
to consult a numerical analysis text (or a numerical analyst) when
selecting and configuring a solver.

In order to use the root-finding features, first a solver object must
be created by calling its constructor, often providing relative and absolute
accuracy. Using a solver object, roots of functions
are easily found using the `solve` methods. These methods takes
a maximum iteration count `maxEval`, a function `f`, and either two domain values, `min` and `max`, or a
`startValue` as parameters. If the maximal number of iterations
count is exceeded, non-convergence is assumed and a `ConvergenceException`
exception is thrown. A suggested value is 100, which should be plenty, given that a
bisection algorithm can't get any more accurate after 52 iterations because of the
number of mantissa bits in a double precision floating point number. If a number of
ill-conditioned problems is to be solved, this number can be decreased in order
to avoid wasting time.
[Bracketed
solvers](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/BracketedUnivariateSolver.html) also take an [allowed solution](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/AllowedSolution.html)
enum parameter to specify which side of the final convergence interval should be
selected as the root. It can be `ANY_SIDE`, `LEFT_SIDE`, `RIGHT_SIDE`, `BELOW_SIDE` or `ABOVE_SIDE`. Left and right are used to specify the root along
the function parameter axis while below and above refer to the function value axis. The solve methods
compute a value `c` such that:

- `f(c) = 0.0` (see "function value accuracy")
- `min <= c <= max` (except for the secant method, which may find a solution outside the interval)

Typical usage:

```
UnivariateFunction function = // some user-defined function object
final double relativeAccuracy = 1.0e-12;
final double absoluteAccuracy = 1.0e-8;
final int    maxOrder         = 5;
UnivariateSolver solver   = new BracketingNthOrderBrentSolver(relativeAccuracy, absoluteAccuracy, maxOrder);
double c = solver.solve(100, function, 1.0, 5.0, AllowedSolution.LEFT_SIDE);
```

Force bracketing, by refining a base solution found by a non-bracketing solver:

```
UnivariateFunction function = // some user-defined function object
final double relativeAccuracy = 1.0e-12;
final double absoluteAccuracy = 1.0e-8;
UnivariateSolver nonBracketing = new BrentSolver(relativeAccuracy, absoluteAccuracy);
double baseRoot = nonBracketing.solve(100, function, 1.0, 5.0);
double c = UnivariateSolverUtils.forceSide(100, function,
                                           new PegasusSolver(relativeAccuracy, absoluteAccuracy),
                                           baseRoot, 1.0, 5.0, AllowedSolution.LEFT_SIDE);
```

The `BrentSolver` uses the Brent-Dekker algorithm which is
fast and robust. If there are multiple roots in the interval, or there is a large domain of indeterminacy, the
algorithm will converge to a random root in the interval without
indication that there are problems. Interestingly, the examined text
book implementations all disagree in details of the convergence
criteria. Also each implementation had problems for one of the test
cases, so the expressions had to be fudged further. Don't expect to
get exactly the same root values as for other implementations of this
algorithm.

The `BracketingNthOrderBrentSolver` uses an extension of the
Brent-Dekker algorithm which uses inverse nth order polynomial
interpolation instead of inverse quadratic interpolation, and which allows
selection of the side of the convergence interval for result bracketing.
This is now the recommended algorithm for most users since it has the
largest order, doesn't require derivatives, has guaranteed convergence
and allows result bracket selection.

The `SecantSolver` uses a straightforward secant
algorithm which does not bracket the search and therefore does not
guarantee convergence. It may be faster than Brent on some well-behaved
functions.

The `RegulaFalsiSolver` is variation of secant preserving
bracketing, but then it may be slow, as one end point of the search interval
will become fixed after and only the other end point will converge to the root, hence resulting in a search interval size that does not decrease to zero.

The `IllinoisSolver` and `PegasusSolver` are
well-known variations of regula falsi that fix the problem of stuck
end points by slightly weighting one endpoint to balance the interval
at next iteration. Pegasus is often faster than Illinois. Pegasus may
be the algorithm of choice for selecting a specific side of the convergence
interval.

The `BisectionSolver` is included for completeness and for
establishing a fall back in cases of emergency. The algorithm is
simple, most likely bug free and guaranteed to converge even in very
adverse circumstances which might cause other algorithms to
malfunction. The drawback is of course that it is also guaranteed
to be slow.

The `UnivariateSolver` interface exposes many
properties to control the convergence of a solver. The accuracy properties
are set at solver instance creation and cannot be changed afterwards, there are only getters to retriveve their values, no setters are available.

| Property | Purpose |
| --- | --- |
| Absolute accuracy | The Absolute Accuracy is (estimated) maximal difference between the computed root and the true root of the function. This is what most people think of as "accuracy" intuitively. The default value is chosen as a sane value for most real world problems, for roots in the range from -100 to +100. For accurate computation of roots near zero, in the range form -0.0001 to +0.0001, the value may be decreased. For computing roots much larger in absolute value than 100, the default absolute accuracy may never be reached because the given relative accuracy is reached first. |
| Relative accuracy | The Relative Accuracy is the maximal difference between the computed root and the true root, divided by the maximum of the absolute values of the numbers. This accuracy measurement is better suited for numerical calculations with computers, due to the way floating point numbers are represented. The default value is chosen so that algorithms will get a result even for roots with large absolute values, even while it may be impossible to reach the given absolute accuracy. |
| Function value accuracy | This value is used by some algorithms in order to prevent numerical instabilities. If the function is evaluated to an absolute value smaller than the Function Value Accuracy, the algorithms assume they hit a root and return the value immediately. The default value is a "very small value". If the goal is to get a near zero function value rather than an accurate root, computation may be sped up by setting this value appropriately. |

<a id="userguide-analysis--4.4-interpolation"></a>

### 4.4 Interpolation

A [UnivariateInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/UnivariateInterpolator.html) is used to find a univariate real-valued
function `f` which for a given set of ordered pairs
(`xi`,`yi`) yields
`f(xi)=yi` to the best accuracy possible. The result
is provided as an object implementing the [UnivariateFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html) interface. It can therefore be evaluated at any point, including point not belonging to the original set.
Currently, only an interpolator for generating natural cubic splines and a polynomial
interpolator are available. There is no interpolator factory, mainly because the
interpolation algorithm is more determined by the kind of the interpolated function
rather than the set of points to interpolate.
There aren't currently any accuracy controls either, as interpolation
accuracy is in general determined by the algorithm.

Typical usage:

```
double x[] = { 0.0, 1.0, 2.0 };
double y[] = { 1.0, -1.0, 2.0};
UnivariateInterpolator interpolator = new SplineInterpolator();
UnivariateFunction function = interpolator.interpolate(x, y);
double interpolationX = 0.5;
double interpolatedY = function.value(x);
System.out println("f(" + interpolationX + ") = " + interpolatedY);
```

A natural cubic spline is a function consisting of a polynomial of
third degree for each subinterval determined by the x-coordinates of the
interpolated points. A function interpolating `N`
value pairs consists of `N-1` polynomials. The function
is continuous, smooth and can be differentiated twice. The second
derivative is continuous but not smooth. The x values passed to the
interpolator must be ordered in ascending order. It is not valid to
evaluate the function for values outside the range
`x0`..`xN`.

The polynomial function returned by the Neville's algorithm is a single
polynomial guaranteed to pass exactly through the interpolation points.
The degree of the polynomial is the number of points minus 1 (i.e. the
interpolation polynomial for a three points set will be a quadratic
polynomial). Despite the fact the interpolating polynomials is a perfect
approximation of a function at interpolation points, it may be a loose
approximation between the points. Due to [Runge's phenomenom](http://en.wikipedia.org/wiki/Runge's_phenomenon)
the error can get worse as the degree of the polynomial increases, so
adding more points does not always lead to a better interpolation.

Loess (or Lowess) interpolation is a robust interpolation useful for
smoothing univariate scaterplots. It has been described by William
Cleveland in his 1979 seminal paper [Robust
Locally Weighted Regression and Smoothing Scatterplots](http://www.math.tau.ac.il/~yekutiel/MA%20seminar/Cleveland%201979.pdf). This kind of
interpolation is computationally intensive but robust.

Microsphere interpolation is a robust multidimensional interpolation algorithm.
It has been described in William Dudziak's [MS thesis](http://www.dudziak.com/microsphere.pdf).

[Hermite interpolation](http://en.wikipedia.org/wiki/Hermite_interpolation)
is an interpolation method that can use derivatives in addition to function values at sample points. The [HermiteInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/HermiteInterpolator.html)
class implements this method for vector-valued functions. The sampling points can have any spacing (there are
no requirements for a regular grid) and some points may provide derivatives while others don't provide them
(or provide derivatives to a smaller order). Points are added one at a time, as shown in the following example:

```
HermiteInterpolator interpolator = new HermiteInterpolator;
// at x = 0, we provide both value and first derivative
interpolator.addSamplePoint(0.0, new double[] { 1.0 }, new double[] { 2.0 });
// at x = 1, we provide only function value
interpolator.addSamplePoint(1.0, new double[] { 4.0 });
// at x = 2, we provide both value and first derivative
interpolator.addSamplePoint(2.0, new double[] { 5.0 }, new double[] { 2.0 });
// should print "value at x = 0.5: 2.5625"
System.out.println("value at x = 0.5: " + interpolator.value(0.5)[0]);
// should print "derivative at x = 0.5: 3.5"
System.out.println("derivative at x = 0.5: " + interpolator.derivative(0.5)[0]);
// should print "interpolation polynomial: 1 + 2 x + 4 x^2 - 4 x^3 + x^4"
System.out.println("interpolation polynomial: " + interpolator.getPolynomials()[0]);
```

A [BivariateGridInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/BivariateGridInterpolator.html) is used to find a bivariate real-valued
function `f` which for a given set of tuples
(`xi`,`yj`,`fij`)
yields `f(xi,yj)=fij` to the best accuracy
possible. The result is provided as an object implementing the
[BivariateFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/BivariateFunction.html) interface. It can therefore be evaluated at any point, including a point not belonging to the original set.
The arrays `xi` and `yj` must be
sorted in increasing order in order to define a two-dimensional grid.

In [bicubic interpolation](http://en.wikipedia.org/wiki/Bicubic_interpolation), the interpolation function is a 3rd-degree polynomial of two variables. The coefficients
are computed from the function values sampled on a grid, as well as the values of the
partial derivatives of the function at those grid points.
From two-dimensional data sampled on a grid, the
[BicubicSplineInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/BicubicSplineInterpolator.html) computes a
[bicubic interpolating function](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/BicubicSplineInterpolatingFunction.html).
Prior to computing an interpolating function, the
[SmoothingPolynomialBicubicSplineInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/SmoothingPolynomialBicubicSplineInterpolator.html) class performs smoothing of
the data by computing the polynomial that best fits each of the one-dimensional
curves along each of the coordinate axes.

A [TrivariateGridInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/TrivariateGridInterpolator.html) is used to find a trivariate real-valued
function `f` which for a given set of tuples
(`xi`,`yj`,`zk`, `fijk`)
yields `f(xi,yj,zk)=fijk`
to the best accuracy possible. The result is provided as an object implementing the
[TrivariateFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/TrivariateFunction.html) interface. It can therefore be evaluated at any point, including a point not belonging to the original set.
The arrays `xi`, `yj` and
`zk` must be sorted in increasing order in order to define
a three-dimensional grid.

In [tricubic interpolation](http://en.wikipedia.org/wiki/Tricubic_interpolation), the interpolation function is a 3rd-degree polynomial of three variables. The coefficients
are computed from the function values sampled on a grid, as well as the values of the
partial derivatives of the function at those grid points.
From three-dimensional data sampled on a grid, the
[TricubicSplineInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/TricubicSplineInterpolator.html) computes a
[tricubic interpolating function](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/interpolation/TricubicSplineInterpolatingFunction.html).

<a id="userguide-analysis--4.5-integration"></a>

### 4.5 Integration

A [UnivariateIntegrator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/integration/UnivariateIntegrator.html) provides the means to numerically integrate
[univariate real-valued functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html).
Commons-Math includes implementations of the following integration algorithms:

- [Romberg's method](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/integration/RombergIntegrator.html)
- [Simpson's method](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/integration/SimpsonIntegrator.html)
- [trapezoid method](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/integration/TrapezoidIntegrator.html)
- [Legendre-Gauss method](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/integration/LegendreGaussIntegrator.html)

<a id="userguide-analysis--4.6-polynomials"></a>

### 4.6 Polynomials

The [org.apache.commons.math4.analysis.polynomials](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/polynomials/package-summary.html) package provides real
coefficients polynomials.

The [PolynomialFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/polynomials/PolynomialFunction.html) class is the most general one, using traditional
coefficients arrays. The
[PolynomialsUtils](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/polynomials/PolynomialsUtils.html) utility class provides static factory methods to build
Chebyshev, Hermite, Jacobi, Laguerre and Legendre polynomials. Coefficients are
computed using exact fractions so these factory methods can build polynomials
up to any degree.

<a id="userguide-analysis--4.7-differentiation"></a>

### 4.7 Differentiation

The [org.apache.commons.math4.analysis.differentiation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/package-summary.html) package provides a general-purpose
differentiation framework.

The core class is [DerivativeStructure](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/DerivativeStructure.html) which holds the value and the differentials of a function. This class
handles some arbitrary number of free parameters and arbitrary derivation order. It is used
both as the input and the output type for the [UnivariateDifferentiableFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateDifferentiableFunction.html) interface. Any differentiable function should implement this
interface.

The main idea behind the [DerivativeStructure](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/DerivativeStructure.html) class is that it can be used almost as a number (i.e. it can be added, multiplied, its square root can be extracted or its cosine computed... However, in addition to
computed the value itself when doing these computations, the partial derivatives are also computed
alongside. This is an extension of what is sometimes called Rall's numbers. This extension is
described in Dan Kalman's paper [Doubly Recursive
Multivariate Automatic Differentiation](http://www1.american.edu/cas/mathstat/People/kalman/pdffiles/mmgautodiff.pdf), Mathematics Magazine, vol. 75, no. 3, June 2002.
Rall's numbers only hold the first derivative with respect to one free parameter whereas Dan Kalman's
derivative structures hold all partial derivatives up to any specified order, with respect to any
number of free parameters. Rall's numbers therefore can be seen as derivative structures for order
one derivative and one free parameter, and primitive real numbers can be seen as derivative structures
with zero order derivative and no free parameters.

The workflow of computation of a derivatives of an expression `y=f(x)` is the following
one. First we configure an input parameter `x` of type [DerivativeStructure](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/DerivativeStructure.html) so it will drive the function to compute all derivatives up to order 3 for
example. Then we compute `y=f(x)` normally by passing this parameter to the f function.At
the end, we extract from `y` the value and the derivatives we want. As we have specified
3rd order when we built `x`, we can retrieve the derivatives up to 3rd
order from `y`. The following example shows that (the 0 parameter in the DerivativeStructure
constructor will be explained in the next paragraph):

```
int params = 1;
int order = 3;
double xRealValue = 2.5;
DerivativeStructure x = new DerivativeStructure(params, order, 0, xRealValue);
DerivativeStructure y = f(x);
System.out.println("y    = " + y.getValue();
System.out.println("y'   = " + y.getPartialDerivative(1);
System.out.println("y''  = " + y.getPartialDerivative(2);
System.out.println("y''' = " + y.getPartialDerivative(3);
```

In fact, there are no notions of *variables* in the framework, so neither `x`
nor `y` are considered to be variables per se. They are both considered to be
*functions* and to depend on implicit free parameters which are represented only by
indices in the framework. The `x` instance above is there considered by the framework
to be a function of free parameter `p0` at index 0, and as `y` is
computed from `x` it is the result of a functions composition and is therefore also
a function of this `p0` free parameter. The `p0` is not represented by itself, it is simply defined implicitely by the 0 index above. This index is the third argument in the
constructor of the `x` instance. What this constructor means is that we built
`x` as a function that depends on one free parameter only (first constructor argument
set to 1), that can be differentiated up to order 3 (second constructor argument set to 3), and
which correspond to an identity function with respect to implicit free parameter number 0 (third
constructor argument set to 0), with current value equal to 2.5 (fourth constructor argument set
to 2.5). This specific constructor defines identity functions, and identity functions are the trick
we use to represent variables (there are of course other constructors, for example to build constants
or functions from all their derivatives if they are known beforehand). From the user point of view, the `x` instance can be seen as the `x` variable, but it is really the identity
function applied to free parameter number 0. As the identity function, it has the same value as its
parameter, its first derivative is 1.0 with respect to this free parameter, and all its higher order
derivatives are 0.0. This can be checked by calling the getValue() or getPartialDerivative() methods
on `x`.

When we compute `y` from this setting, what we really do is chain `f` after the
identity function, so the net result is that the derivatives are computed with respect to the indexed
free parameters (i.e. only free parameter number 0 here since there is only one free parameter) of the
identity function x. Going one step further, if we compute `z = g(y)`, we will also compute
`z` as a function of the initial free parameter. The very important consequence is that
if we call `z.getPartialDerivative(1)`, we will not get the first derivative of `g`
with respect to `y`, but with respect to the free parameter `p0`: the derivatives
of g and f *will* be chained together automatically, without user intervention.

This design choice is a very classical one in many algorithmic differentiation frameworks, either
based on operator overloading (like the one we implemented here) or based on code generation. It implies
the user has to *bootstrap* the system by providing initial derivatives, and this is essentially
done by setting up identity function, i.e. functions that represent the variables themselves and have
only unit first derivative.

This design also allow a very interesting feature which can be explained with the following example.
Suppose we have a two arguments function `f` and a one argument function `g`. If
we compute `g(f(x, y))` with `x` and `y` be two variables, we
want to be able to compute the partial derivatives `dg/dx`, `dg/dy`, `d2g/dx2` `d2g/dxdy` `d2g/dy2`. This does make sense since we combined
the two functions, and it does make sense despite g is a one argument function only. In order to do
this, we simply set up `x` as an identity function of an implicit free parameter
`p0` and `y` as an identity function of a different implicit free parameter
`p1` and compute everything directly. In order to be able to combine everything, however, both `x` and `y` must be built with the appropriate dimensions, so they will both
be declared to handle two free parameters, but `x` will depend only on parameter 0 while
`y` will depend on parameter 1. Here is how we do this (note that
`getPartialDerivative` is a variable arguments method which take as arguments the derivation
order with respect to all free parameters, i.e. the first argument is derivation order with respect to
free parameter 0 and the second argument is derivation order with respect to free parameter 1):

```
int params = 2;
int order = 2;
double xRealValue =  2.5;
double yRealValue = -1.3;
DerivativeStructure x = new DerivativeStructure(params, order, 0, xRealValue);
DerivativeStructure y = new DerivativeStructure(params, order, 1, yRealValue);
DerivativeStructure f = DerivativeStructure.hypot(x, y);
DerivativeStructure g = f.log();
System.out.println("g        = " + g.getValue();
System.out.println("dg/dx    = " + g.getPartialDerivative(1, 0);
System.out.println("dg/dy    = " + g.getPartialDerivative(0, 1);
System.out.println("d2g/dx2  = " + g.getPartialDerivative(2, 0);
System.out.println("d2g/dxdy = " + g.getPartialDerivative(1, 1);
System.out.println("d2g/dy2  = " + g.getPartialDerivative(0, 2);
```

There are several ways a user can create an implementation of the [UnivariateDifferentiableFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateDifferentiableFunction.html) interface. The first method is to simply write it directly using
the appropriate methods from [DerivativeStructure](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/DerivativeStructure.html) to compute addition, subtraction, sine, cosine... This is often quite
straigthforward and there is no need to remember the rules for differentiation: the user code only
represent the function itself, the differentials will be computed automatically under the hood. The
second method is to write a classical [UnivariateFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html) and to
pass it to an existing implementation of the [UnivariateFunctionDifferentiator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateFunctionDifferentiator.html) interface to retrieve a differentiated version of the same function.
The first method is more suited to small functions for which user already control all the underlying code.
The second method is more suited to either large functions that would be cumbersome to write using the
[DerivativeStructure](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/DerivativeStructure.html) API, or functions for which user does not have control to the full underlying code
(for example functions that call external libraries).

Apache Commons Math provides one implementation of the [UnivariateFunctionDifferentiator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateFunctionDifferentiator.html) interface: [FiniteDifferencesDifferentiator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/FiniteDifferencesDifferentiator.html). This class creates a wrapper that will call the user-provided function
on a grid sample and will use finite differences to compute the derivatives. It takes care of boundaries
if the variable is not defined on the whole real line. It is possible to use more points than strictly
required by the derivation order (for example one can specify an 8-points scheme to compute first
derivative only). However, one must be aware that tuning the parameters for finite differences is
highly problem-dependent. Choosing the wrong step size or the wrong number of sampling points can lead
to huge errors. Finite differences are also not well suited to compute high order derivatives. Here is
an example on how this implementation can be used:

```
// function to be differentiated
UnivariateFunction basicF = new UnivariateFunction() {
                                public double value(double x) {
                                    return x * FastMath.sin(x);
                                }
                            });

// create a differentiator using 5 points and 0.01 step
FiniteDifferencesDifferentiator differentiator =
    new FiniteDifferencesDifferentiator(5, 0.01);

// create a new function that computes both the value and the derivatives
// using DerivativeStructure
UnivariateDifferentiableFunction completeF = differentiator.differentiate(basicF);

// now we can compute display the value and its derivatives
// here we decided to display up to second order derivatives,
// because we feed completeF with order 2 DerivativeStructure instances
for (double x = -10; x < 10; x += 0.1) {
    DerivativeStructure xDS = new DerivativeStructure(1, 2, 0, x);
    DerivativeStructure yDS = f.value(xDS);
    System.out.format(Locale.US, "%7.3f %7.3f %7.3f%n",
                      yDS.getValue(),
                      yDS.getPartialDerivative(1),
                      yDS.getPartialDerivative(2));
}
```

Note that using [FiniteDifferencesDifferentiator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/FiniteDifferencesDifferentiator.html)a> in order to have a [UnivariateDifferentiableFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateDifferentiableFunction.html) that can be provided to a [Newton-Raphson's](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/NewtonRaphsonSolver.html)
solver is a very bad idea. The reason is that finite differences are not really accurate and needs lots
of additional calls to the basic underlying function. If user initially have only the basic function
available and needs to find its roots, it is *much* more accurate and *much* more
efficient to use a solver that only requires the function values and not the derivatives. A good choice is
to use [bracketing
nth order Brent](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/BracketingNthOrderBrentSolver.html) method, which in fact converges faster than [Newton-Raphson's](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/solvers/NewtonRaphsonSolver.html) and
can be configured to a highere order (typically 5) than Newton-Raphson which is an order 2 method.

Another implementation of the [UnivariateFunctionDifferentiator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/UnivariateFunctionDifferentiator.html) interface is under development in the related project
[Apache Commons Nabla](http://commons.apache.org/sandbox/nabla/). This implementation uses
automatic code analysis and generation at binary level. However, at time of writing
(end 2012), this project is not yet suitable for production use.

---

<a id="userguide-special"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/special.html -->

<!-- page_index: 11 -->

<a id="userguide-special--5-special-functions"></a>

## 5 Special functions

<a id="userguide-special--5.1-overview"></a>

### 5.1 Overview

The "gamma", "beta" and "erf" functions are implemented in
[Commons Numbers](http://commons.apache.org/numbers).

---

<a id="userguide-utilities"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/utilities.html -->

<!-- page_index: 12 -->

<a id="userguide-utilities--6-utilities"></a>

## 6 Utilities

<a id="userguide-utilities--6.1-overview"></a>

### 6.1 Overview

The [org.apache.commons.math4.util](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/package-summary.html) package collects a group of array utilities, value transformers, and numerical routines used by implementation classes in
commons-math.

<a id="userguide-utilities--6.2-double-array-utilities"></a>

### 6.2 Double array utilities

To maintain statistics based on a "rolling" window of values, a resizable
array implementation was developed and is provided for reuse in the
`util` package. The core functionality provided is described in
the documentation for the interface, [DoubleArray](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/DoubleArray.html). This interface adds one method, `addElementRolling(double)` to basic list accessors.
The `addElementRolling` method adds an element
(the actual parameter) to the end of the list and removes the first element
in the list.

The [ResizableDoubleArray](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/ResizableDoubleArray.html) class provides a configurable, array-backed
implementation of the `DoubleArray` interface.
When `addElementRolling` is invoked, the underlying
array is expanded if necessary, the new element is added to the end of the
array and the "usable window" of the array is moved forward, so that
the first element is effectively discarded, what was the second becomes the
first, and so on. To efficiently manage storage, two maintenance
operations need to be periodically performed -- orphaned elements at the
beginning of the array need to be reclaimed and space for new elements at
the end needs to be created. Both of these operations are handled
automatically, with frequency / effect driven by the configuration
properties `expansionMode`, `expansionFactor` and
`contractionCriteria.` See
[ResizableDoubleArray](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/ResizableDoubleArray.html)
for details.

<a id="userguide-utilities--6.3-int-double-hash-map"></a>

### 6.3 int/double hash map

The [OpenIntToDoubleHashMap](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/OpenIntToDoubleHashMap.html) class provides a specialized hash map
implementation for int/double. This implementation has a much smaller memory
overhead than standard `java.util.HashMap` class. It uses open addressing
and primitive arrays, which greatly reduces the number of intermediate objects and
improve data locality.

<a id="userguide-utilities--6.4-continued-fractions"></a>

### 6.4 Continued Fractions

The [ContinuedFraction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/ContinuedFraction.html) class provides a generic way to create and evaluate
continued fractions. The easiest way to create a continued fraction is
to subclass `ContinuedFraction` and override the
`getA` and `getB` methods which return
the continued fraction terms. The precise definition of these terms is
explained in [Continued Fraction, equation (1)](http://mathworld.wolfram.com/ContinuedFraction.html) from MathWorld.

As an example, the constant π can be computed using a [continued fraction](http://functions.wolfram.com/Constants/Pi/10/0002/). The following anonymous class
provides the implementation:

```
ContinuedFraction c = new ContinuedFraction() {public double getA(int n, double x) {switch(n) {case 0: return 3.0; default: return 6.0;}}
public double getB(int n, double x) {double y = (2.0 * n) - 1.0; return y * y;}}
```

Then, to evalute π, simply call any of the `evalute` methods
(Note, the point of evaluation in this example is meaningless since π is a
constant).

For a more practical use of continued fractions, consider the [exponential function](http://functions.wolfram.com/ElementaryFunctions/Exp/10/).
The following anonymous class provides its implementation:

```
ContinuedFraction c = new ContinuedFraction() {public double getA(int n, double x) {if (n % 2 == 0) {switch(n) {case 0: return 1.0; default: return 2.0;} } else {return n;}}
public double getB(int n, double x) {if (n % 2 == 0) {return -x; } else {return x;}}}
```

Then, to evalute *e*x for any value x, simply call any of the
`evalute` methods.

<a id="userguide-utilities--6.5-binomial-coefficients-factorials-stirling-numbers-and-other-common-math-functions"></a>

### 6.5 Binomial coefficients, factorials, Stirling numbers and other common math functions

A collection of reusable math functions is provided in the
[ArithmeticUtils](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/ArithmeticUtils.html)
utility class. ArithmeticUtils currently includes methods to compute the following:

- Binomial coefficients -- "n choose k" available as an (exact) long value,
  `binomialCoefficient(int, int)` for small n, k; as a double,
  `binomialCoefficientDouble(int, int)` for larger values; and in
  a "super-sized" version, `binomialCoefficientLog(int, int)`
  that returns the natural logarithm of the value.
- Stirling numbers of the second kind -- S(n,k) as an exact long value
  `stirlingS2(int, int)` for small n, k.
- Factorials -- like binomial coefficients, these are available as exact long
  values, `factorial(int)`; doubles,
  `factorialDouble(int)`; or logs, `factorialLog(int)`.
- Least common multiple and greatest common denominator functions.

<a id="userguide-utilities--6.6-fast-mathematical-functions"></a>

### 6.6 Fast mathematical functions

Apache Commons Math provides a faster, more accurate, portable alternative
to the regular `Math` and `StrictMath`classes for large
scale computation.

FastMath is a drop-in replacement for both Math and StrictMath. This
means that for any method in Math (say `Math.sin(x)` or
`Math.cbrt(y)`), user can directly change the class and use the
methods as is (using `FastMath.sin(x)` or `FastMath.cbrt(y)`
in the previous example).

FastMath speed is achieved by relying heavily on optimizing compilers to
native code present in many JVM todays and use of large tables. Precomputed
literal arrays are provided in this class to speed up load time. These
precomputed tables are used in the default configuration, to improve speed
even at first use of the class. If users prefer to compute the tables
automatically at load time, they can change a compile-time constant. This will
increase class load time at first use, but this overhead will occur only once
per run, regardless of the number of subsequent calls to computation methods.
Note that FastMath is extensively used inside Apache Commons Math, so by
calling some algorithms, the one-shot overhead when the constant is set to
false will occur regardless of the end-user calling FastMath methods directly
or not. Performance figures for a specific JVM and hardware can be evaluated by
running the FastMathTestPerformance tests in the test directory of the source
distribution.

FastMath accuracy should be mostly independent of the JVM as it relies only
on IEEE-754 basic operations and on embedded tables. Almost all operations
are accurate to about 0.5 ulp throughout the domain range. This statement, of
course is only a rough global observed behavior, it is *not* a guarantee
for *every* double numbers input (see William Kahan's [Table
Maker's Dilemma](http://en.wikipedia.org/wiki/Rounding#The_table-maker.27s_dilemma)).

FastMath additionally implements the following methods not found in Math/StrictMath:

- asinh(double)
- acosh(double)
- atanh(double)
- pow(double,int)

The following methods are found in Math/StrictMath since 1.6 only, they are
provided by FastMath even in 1.5 Java virtual machines

- copySign(double, double)
- getExponent(double)
- nextAfter(double,double)
- nextUp(double)
- scalb(double, int)
- copySign(float, float)
- getExponent(float)
- nextAfter(float,double)
- nextUp(float)
- scalb(float, int)

<a id="userguide-utilities--6.7-miscellaneous"></a>

### 6.7 Miscellaneous

The [MultidimensionalCounter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/util/MultidimensionalCounter.html) is a utility class that converts a set of indices
(identifying points in a multidimensional space) to a single index (e.g. identifying
a location in a one-dimensional array.

Copyright © 2003-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Math, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="userguide-complex"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/complex.html -->

<!-- page_index: 13 -->

<a id="userguide-complex--7-complex-numbers"></a>

## 7 Complex Numbers

<a id="userguide-complex--7.1-overview"></a>

### 7.1 Overview

The concept of "complex number" is implemented in
[Commons Numbers](http://commons.apache.org/numbers).

---

<a id="userguide-distribution"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/distribution.html -->

<!-- page_index: 14 -->

<a id="userguide-distribution--8-probability-distributions"></a>

## 8 Probability Distributions

<a id="userguide-distribution--8.1-overview"></a>

### 8.1 Overview

Standard distributions are now available in the
[Commons Statistics](https://commons.apache.org/proper/commons-statistics/userguide/index.html) component.

Commons Math provides

- an [EnumeratedDistribution](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/distribution/EnumeratedDistribution.html) class that represents discrete distributions of a finite,
  enumerated set of values.
- a [MultivariateNormalDistribution](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/distribution/MultiVariateNormalDistribution.html) interface that represents multivariate Gaussian
  distributions.

Inverse distribution functions can be computed using the
`inverseCumulativeProbability` methods. For continuous `f`
and `p` a probability, `f.inverseCumulativeProbability(p)` returns

- inf{x in R | P(X≤x) ≥ p} for 0 < p < 1,
- inf{x in R | P(X≤x) > 0} for p = 0.

where `X` is distributed as `f`.
For discrete `f`, the definition is the same, with `Z` (the integers)
in place of `R`. Note that in the discrete case, the ≥ in the definition
can make a difference when `p` is an attained value of the distribution.

<a id="userguide-distribution--8.2-generating-data-like-an-input-file"></a>

### 8.2 Generating data like an input file

Using the `EmpiricalDistribution` class, you can generate data based on
a given set of values:

```

double[] input = load("data.txt"); // Get some data.
int binCount = 500;
EmpiricalDistribution empDist = EmpiricalDistribution.from(binCount, input);
ContinuousDistribution.Sampler sampler = empDist.createSampler(RandomSource.MT.create());
double value = sampler.nextDouble(); 
```

The probability density function is estimated from the data passed as input.
The estimation method is essentially the
[Variable Kernel Method](http://nedwww.ipac.caltech.edu/level5/March02/Silverman/Silver2_6.html) with Gaussian smoothing.
The created sampler will return random values whose probability distribution
matches the empirical distribution (i.e. if you generate a large number of
such values, their distribution should "look like" the distribution of the
values in the input file.
The input values are not stored in memory.

---

<a id="userguide-fraction"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/fraction.html -->

<!-- page_index: 15 -->

<a id="userguide-fraction--9-fractions"></a>

## 9 Fractions

<a id="userguide-fraction--9.1-overview"></a>

### 9.1 Overview

The concept of "fraction" is implemented in
[Commons Numbers](http://commons.apache.org/numbers).

---

<a id="userguide-transform"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/transform.html -->

<!-- page_index: 16 -->

<a id="userguide-transform--10-transforms"></a>

## 10 Transforms

Function transforms (direct and inverse) for signal analysis.

- [FastFourierTransform](https://commons.apache.org/proper/commons-math/commons-math4-transform/apidocs/org/apache/commons/math4/transform/FastFourierTransform.html) (produces `Complex` results)
- [FastCosineTransform](https://commons.apache.org/proper/commons-math/commons-math4-transform/apidocs/org/apache/commons/math4/transform/FastCosineTransform.html) (produces real results)
- [FastSineTransform](https://commons.apache.org/proper/commons-math/commons-math4-transform/apidocs/org/apache/commons/math4/transform/FastSineTransform.html) (produces real results)
- [FastHadamardTransform](https://commons.apache.org/proper/commons-math/commons-math4-transform/apidocs/org/apache/commons/math4/transform/FastHadamardTransform.html) (produces real results)

---

<a id="userguide-geometry"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/geometry.html -->

<!-- page_index: 17 -->

<a id="userguide-geometry--11-geometry"></a>

## 11 Geometry

<a id="userguide-geometry--11.1-overview"></a>

### 11.1 Overview

Geometry utilities are implemented in
[Commons Geometry](http://commons.apache.org/geometry).

---

<a id="userguide-optimization"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/optimization.html -->

<!-- page_index: 18 -->

<a id="userguide-optimization--12-optimization"></a>

## 12 Optimization

*The contents of this section currently describes deprecated classes.*
Please refer to the new [API
description](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optim/package-summary.html).

Least squares optimizers are not in this package anymore, they have been moved
in a dedicated least-squares sub-package described in the [least squares](#userguide-leastsquares)
section.

<a id="userguide-optimization--12.1-overview"></a>

### 12.1 Overview

The optimization package provides algorithms to optimize (i.e. either minimize
or maximize) some objective or cost function. The package is split in several
sub-packages dedicated to different kind of functions or algorithms.

- the univariate package handles univariate scalar functions,
- the linear package handles multivariate vector linear functions
  with linear constraints,
- the direct package handles multivariate scalar functions
  using direct search methods (i.e. not using derivatives),
- the general package handles multivariate scalar or vector functions
  using derivatives.
- the fitting package handles curve fitting by univariate real functions

The top level optimization package provides common interfaces for the optimization
algorithms provided in sub-packages. The main interfaces defines defines optimizers
and convergence checkers. The functions that are optimized by the algorithms provided
by this package and its sub-packages are a subset of the one defined in the
`analysis` package, namely the real and vector valued functions. These
functions are called objective function here. When the goal is to minimize, the
functions are often called cost function, this name is not used in this package.

The type of goal, i.e. minimization or maximization, is defined by the enumerated
[GoalType](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/GoalType.html) which has only two values: `MAXIMIZE` and `MINIMIZE`.

Optimizers are the algorithms that will either minimize or maximize, the objective
function by changing its input variables set until an optimal set is found. There
are only four interfaces defining the common behavior of optimizers, one for each
supported type of objective function:

- [UnivariateOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/univariate/UnivariateOptimizer.html) for [univariate real functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/UnivariateFunction.html)
- [MultivariateOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/MultivariateOptimizer.html) for [multivariate real functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateFunction.html)
- [DifferentiableMultivariateOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/DifferentiableMultivariateOptimizer.html) for [differentiable multivariate real functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/DifferentiableMultivariateFunction.html)
- [DifferentiableMultivariateVectorOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/DifferentiableMultivariateVectorOptimizer.html) for [differentiable multivariate vectorial functions](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/DifferentiableMultivariateVectorFunction.html)

Despite there are only four types of supported optimizers, it is possible to optimize
a transform a [non-differentiable multivariate vectorial function](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateVectorFunction.html) by converting it to a [non-differentiable multivariate real function](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateFunction.html) thanks to the [LeastSquaresConverter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/LeastSquaresConverter.html) helper class. The transformed function can be optimized using
any implementation of the [MultivariateOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/MultivariateOptimizer.html) interface.

For each of the four types of supported optimizers, there is a special implementation
which wraps a classical optimizer in order to add it a multi-start feature. This feature
call the underlying optimizer several times in sequence with different starting points
and returns the best optimum found or all optima if desired. This is a classical way to
prevent being trapped into a local extremum when looking for a global one.

<a id="userguide-optimization--12.2-univariate-functions"></a>

### 12.2 Univariate Functions

A [UnivariateOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/univariate/UnivariateOptimizer.html) is used to find the minimal values of a univariate real-valued
function `f`.

These algorithms usage is very similar to root-finding algorithms usage explained
in the analysis package. The main difference is that the `solve` methods in root
finding algorithms is replaced by `optimize` methods.

<a id="userguide-optimization--12.3-linear-programming"></a>

### 12.3 Linear Programming

This package provides an implementation of George Dantzig's simplex algorithm
for solving linear optimization problems with linear equality and inequality
constraints.

<a id="userguide-optimization--12.4-direct-methods"></a>

### 12.4 Direct Methods

Direct search methods only use cost function values, they don't
need derivatives and don't either try to compute approximation of
the derivatives. According to a 1996 paper by Margaret H. Wright
([Direct
Search Methods: Once Scorned, Now Respectable](http://cm.bell-labs.com/cm/cs/doc/96/4-02.ps.gz)), they are used
when either the computation of the derivative is impossible (noisy
functions, unpredictable discontinuities) or difficult (complexity, computation cost). In the first cases, rather than an optimum, a
*not too bad* point is desired. In the latter cases, an
optimum is desired but cannot be reasonably found. In all cases
direct search methods can be useful.

Simplex-based direct search methods are based on comparison of
the cost function values at the vertices of a simplex (which is a
set of n+1 points in dimension n) that is updated by the algorithms
steps.

The instances can be built either in single-start or in
multi-start mode. Multi-start is a traditional way to try to avoid
being trapped in a local minimum and miss the global minimum of a
function. It can also be used to verify the convergence of an
algorithm. In multi-start mode, the `minimizes`method
returns the best minimum found after all starts, and the `etMinima`
method can be used to retrieve all minima from all starts (including the one
already provided by the `minimizes` method).

The `direct` package provides four solvers:

- the classical [Nelder-Mead](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/direct/NelderMeadSimplex.html) method,
- Virginia Torczon's [multi-directional](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/direct/MultiDirectionalSimplex.html) method,
- Nikolaus Hansen's Covariance Matrix Adaptation Evolution Strategy (CMA-ES),
- Mike Powell's [BOBYQA](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/direct/BOBYQAOptimizer.html) method.

The first two simplex-based methods do not handle simple bounds constraints by themselves.
However there are two adapters([MultivariateFunctionMappingAdapter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/direct/MultivariateFunctionMappingAdapter.html) and [MultivariateFunctionPenaltyAdapter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/direct/MultivariateFunctionPenaltyAdapter.html)) that can be used to wrap the user function in
such a way the wrapped function is unbounded and can be used with these optimizers, despite
the fact the underlying function is still bounded and will be called only with feasible
points that fulfill the constraints. Note however that using these adapters are only a
poor man solutions to simple bounds optimization constraints. Better solutions are to use an
optimizer that directly supports simple bounds. Some caveats of the mapping adapter
solution are that

- behavior near the bounds may be numerically unstable as bounds are mapped from
  infinite values,
- start value is evaluated by the optimizer as an unbounded variable,
  so it must be converted from bounded to unbounded by user,
- optimum result is evaluated by the optimizer as an unbounded variable,
  so it must be converted from unbounded to bounded by user,
- convergence values are evaluated by the optimizer as unbounded variables,
  so there will be scales differences when converted to bounded variables,
- in the case of simplex based solvers, the initial simplex should be set up
  as delta in unbounded variables.

One caveat of penalty adapter is that if start point or start simplex is outside of the allowed
range, only the penalty function is used, and the optimizer may converge without ever entering
the allowed range.

The last methods do handle simple bounds constraints directly, so the adapters are not needed
with them.

<a id="userguide-optimization--12.5-general-case"></a>

### 12.5 General Case

The general package deals with non-linear vectorial optimization problems when
the partial derivatives of the objective function are available.

One important class of estimation problems is weighted least
squares problems. They basically consist in finding the values
for some parameters pk such that a cost function
J = sum(wi(mesi - modi)2) is
minimized. The various (targeti - modeli(pk))
terms are called residuals. They represent the deviation between a set of
target values targeti and theoretical values computed from
models modeli depending on free parameters pk.
The wi factors are weights. One classical use case is when the
target values are experimental observations or measurements.

Solving a least-squares problem is finding the free parameters pk
of the theoretical models such that they are close to the target values, i.e.
when the residual are small.

Two optimizers are available in the general package, both devoted to least-squares
problems. The first one is based on the [Gauss-Newton](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/general/GaussNewtonOptimizer.html) method. The second one is the [Levenberg-Marquardt](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/general/LevenbergMarquardtOptimizer.html) method.

In order to solve a vectorial optimization problem, the user must provide it as
an object implementing the [DifferentiableMultivariateVectorFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/DifferentiableMultivariateVectorFunction.html) interface. The object will be provided to
the `estimate` method of the optimizer, along with the target and weight arrays, thus allowing the optimizer to compute the residuals at will. The last parameter to the
`estimate` method is the point from which the optimizer will start its
search for the optimal point.

Quadratic Problem Example
:   We are looking to find the best parameters [a, b, c] for the quadratic function
    **`f(x) = a x2 + b x + c`**.
    The data set below was generated using [a = 8, b = 10, c = 16].
    A random number between zero and one was added to each y value calculated.

| **X** | **Y** |
| --- | --- |
| 1 | 34.234064369 |
| 2 | 68.2681162306108 |
| 3 | 118.615899084602 |
| 4 | 184.138197238557 |
| 5 | 266.599877916276 |
| 6 | 364.147735251579 |
| 7 | 478.019226091914 |
| 8 | 608.140949270688 |
| 9 | 754.598868667148 |
| 10 | 916.128818085883 |

    First we need to implement the interface [DifferentiableMultivariateVectorFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/DifferentiableMultivariateVectorFunction.html).
    This requires the implementation of the method signatures:

    - **MultivariateMatrixFunction jacobian()**
    - **double[] value(double[] point)**

    We'll tackle the implementation of the `MultivariateMatrixFunction jacobian()` method first. You may wish to familiarize yourself with what a  [Jacobian Matrix](http://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant) is.
    In this case the Jacobian is the partial derivative of the function with respect
    to the parameters a, b and c. These derivatives are computed as follows:

    - d(ax2 + bx + c)/da = x2
    - d(ax2 + bx + c)/db = x
    - d(ax2 + bx + c)/dc = 1

    For a quadratic which has three variables the Jacobian Matrix will have three columns, one for each variable, and the number
    of rows will equal the number of rows in our data set, which in this case is ten. So for example for `[a = 1, b = 1, c = 1]`, the Jacobian Matrix is (excluding the first column which shows the value of x):


| **x** | **d(ax2 + bx + c)/da** | **d(ax2 + bx + c)/db** | **d(ax2 + bx + c)/dc** |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 2 | 4 | 2 | 1 |
| 3 | 9 | 3 | 1 |
| 4 | 16 | 4 | 1 |
| 5 | 25 | 5 | 1 |
| 6 | 36 | 6 | 1 |
| 7 | 49 | 7 | 1 |
| 8 | 64 | 8 | 1 |
| 9 | 81 | 9 | 1 |
| 10 | 100 | 10 | 1 |

    The implementation of the `MultivariateMatrixFunction jacobian()` for this problem looks like this (The `x`
    parameter is an ArrayList containing the independent values of the data set):


```
private double[][] jacobian(double[] variables) {double[][] jacobian = new double[x.size()][3]; for (int i = 0; i < jacobian.length; ++i) {jacobian[i][0] = x.get(i) * x.get(i); jacobian[i][1] = x.get(i); jacobian[i][2] = 1.0;} return jacobian;}
public MultivariateMatrixFunction jacobian() {return new MultivariateMatrixFunction() {private static final long serialVersionUID = -8673650298627399464L; public double[][] value(double[] point) {return jacobian(point);} };}
```

    Note that if for some reason the derivative of the objective function with respect
    to its variables is difficult to obtain,
    [Numerical differentiation](http://en.wikipedia.org/wiki/Numerical_differentiation) can be used.

    The implementation of the `double[] value(double[] point)` method, which returns
    a `double` array containing the
    values the objective function returns per given independent value
    and the current set of variables or parameters,
    can be seen below:


```
public double[] value(double[] variables) {double[] values = new double[x.size()]; for (int i = 0; i < values.length; ++i) {values[i] = (variables[0] * x.get(i) + variables[1]) * x.get(i) + variables[2];} return values;}
```

    Below is the the class containing all the implementation details
    (Taken from the Apache Commons Math **org.apache.commons.math4.optimization.general.LevenbergMarquardtOptimizerTest**):


```
private static class QuadraticProblem implements DifferentiableMultivariateVectorFunction, Serializable {
private static final long serialVersionUID = 7072187082052755854L; private List<Double> x; private List<Double> y;
public QuadraticProblem() {x = new ArrayList<Double>(); y = new ArrayList<Double>();}
public void addPoint(double x, double y) {this.x.add(x); this.y.add(y);}
public double[] calculateTarget() {double[] target = new double[y.size()]; for (int i = 0; i < y.size(); i++) {target[i] = y.get(i).doubleValue();} return target;}
private double[][] jacobian(double[] variables) {double[][] jacobian = new double[x.size()][3]; for (int i = 0; i < jacobian.length; ++i) {jacobian[i][0] = x.get(i) * x.get(i); jacobian[i][1] = x.get(i); jacobian[i][2] = 1.0;} return jacobian;}
public double[] value(double[] variables) {double[] values = new double[x.size()]; for (int i = 0; i < values.length; ++i) {values[i] = (variables[0] * x.get(i) + variables[1]) * x.get(i) + variables[2];} return values;}
public MultivariateMatrixFunction jacobian() {return new MultivariateMatrixFunction() {private static final long serialVersionUID = -8673650298627399464L; public double[][] value(double[] point) {return jacobian(point);} };}}
```

    The below code shows how to go about using the above class
    and a LevenbergMarquardtOptimizer instance to produce an
    optimal set of quadratic curve fitting parameters:


```

 QuadraticProblem problem = new QuadraticProblem();

 problem.addPoint(1, 34.234064369);
 problem.addPoint(2, 68.2681162306);
 problem.addPoint(3, 118.6158990846);
 problem.addPoint(4, 184.1381972386);
 problem.addPoint(5, 266.5998779163);
 problem.addPoint(6, 364.1477352516);
 problem.addPoint(7, 478.0192260919);
 problem.addPoint(8, 608.1409492707);
 problem.addPoint(9, 754.5988686671);
 problem.addPoint(10, 916.1288180859);

 LevenbergMarquardtOptimizer optimizer = new LevenbergMarquardtOptimizer();

 final double[] weights = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };

 final double[] initialSolution = {1, 1, 1};

 PointVectorValuePair optimum = optimizer.optimize(100,
                                                   problem,
                                                   problem.calculateTarget(),
                                                   weights,
                                                   initialSolution);

 final double[] optimalValues = optimum.getPoint();

 System.out.println("A: " + optimalValues[0]);
 System.out.println("B: " + optimalValues[1]);
 System.out.println("C: " + optimalValues[2]);

    
```

    If you run the above sample you will see
    the following printed by the console:


```

A: 7.998832172372726
B: 10.001841530162448
C: 16.324008168386605
```

In addition to least squares solving, the [NonLinearConjugateGradientOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/general/NonLinearConjugateGradientOptimizer.html) class provides a non-linear conjugate gradient algorithm
to optimize [DifferentiableMultivariateFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/DifferentiableMultivariateFunction.html). Both the Fletcher-Reeves and the Polak-Ribière
search direction update methods are supported. It is also possible to set up a preconditioner
or to change the line-search algorithm of the inner loop if desired (the default one is a Brent
solver).

The [PowellOptimizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optimization/direct/PowellOptimizer.html) provides an optimization method for non-differentiable functions.

---

<a id="userguide-fitting"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/fitting.html -->

<!-- page_index: 19 -->

<a id="userguide-fitting--13-curve-fitting"></a>

## 13 Curve Fitting

<a id="userguide-fitting--13.1-overview"></a>

### 13.1 Overview

The fitting package deals with curve fitting for univariate real functions.
When a univariate real function y = f(x) does depend on some unknown parameters
p0, p1 ... pn-1, curve fitting can be used to
find these parameters. It does this by *fitting* the curve so it remains
very close to a set of observed points (x0, y0), (x1, y1) ... (xk-1, yk-1). This
fitting is done by finding the parameters values that minimizes the objective
function Σ(yi - f(xi))2. This is actually a
least-squares problem.

For all provided curve fitters, the operating principle is the same.
Users must

- create an instance of the fitter using the `create` factory method of the
  appropriate class,
- call the [fit](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/AbstractCurveFitter)
  with a `Collection` of [observed data points](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/WeightedObservedPoint.html) as argument, which will return an array with the parameters that
  best fit the given data points.

The list of observed data points to be passed to `fit` can be built by incrementally
adding instances to an instance of [WeightedObservedPoints](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/WeightedObservedPoints.html), and then retrieve the list of `WeightedObservedPoint` by calling the `toList`
method on that container.
A weight can be associated with each observed point; it allows to take into account uncertainty
on some points when they come from noisy measurements for example. If no such information exist and
all points should be treated the same, it is safe to put 1.0 as the weight for all points (and this
is the default when no weight is passed to the `add`.

Some fitters require that initial values for the parameters are provided by the user, through the `withStartPoint` method, before attempting to perform the fit.
When that's the case the fitter class usually defines a guessing procedure within a
`ParameterGuesser` inner class, that attempts to provide appropriate initial
values based on the user-supplied data.
When initial values are required but are not provided, the `fit` method will
internally call the guessing procedure.

<a id="userguide-fitting--13.2-implemented-functions"></a>

### 13.2 Implemented Functions

Fitting of specific functions are provided through the following classes:

- [PolynomialFitter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/PolynomialCurveFitter.html) fits a
  [polynomial](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/polynomials/PolynomialFunction.Parametric.html) function.
- [HarmonicFitter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/HarmonicCurveFitter.html) fits a
  [harmonic](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/function/HarmonicOscillator.Parametric.html) function.
  An instance of the inner class [ParameterGuesser](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/HarmonicCurveFitter.ParameterGuesser.html) can be used to retrieve initial values for the fitting procedure.
- [GaussianFitter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/GaussianCurveFitter.html) fits a
  [Gaussian](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/function/Gaussian.Parametric.html) function.
  An instance of the inner class [ParameterGuesser](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/GaussianCurveFitter.ParameterGuesser.html) can be used to retrieve initial values for the fitting procedure.

The following example shows how to fit data with a polynomial function.

```
// Collect data.
final WeightedObservedPoints obs = new WeightedObservedPoints();
obs.add(-1.00, 2.021170021833143);
obs.add(-0.99, 2.221135431136975);
obs.add(-0.98, 2.09985277659314);
obs.add(-0.97, 2.0211192647627025);
// ... Lots of lines omitted ...
obs.add(0.99, -2.4345814727089854);

// Instantiate a third-degree polynomial fitter.
final PolynomialCurveFitter fitter = PolynomialCurveFitter.create(3);

// Retrieve fitted parameters (coefficients of the polynomial function).
final double[] coeff = fitter.fit(obs.toList());
        
```

<a id="userguide-fitting--13.3-general-case"></a>

### 13.3 General Case

The [AbstractCurveFitter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/AbstractCurveFitter.html) class provides the basic functionality for implementing other
curve fitting classes.
Users must provide their own implementation of the curve template as a class that implements
the [ParametricUnivariateFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/ParametricUnivariateFunction.html) interface.

---

<a id="userguide-leastsquares"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/leastsquares.html -->

<!-- page_index: 20 -->

<a id="userguide-leastsquares--14-least-squares"></a>

## 14 Least squares

<a id="userguide-leastsquares--14.1-overview"></a>

### 14.1 Overview

The least squares package fits a parametric model to a set of observed
values by minimizing a cost function with a specific form.
The fitting basically consists in finding the values
for some parameters pk such that a cost function
J = sum(wi(targeti - modeli)2) is
minimized. The various (targeti - modeli(pk))
terms are called residuals. They represent the deviation between a set of
target values targeti and theoretical values computed from
models modeli depending on free parameters pk.
The wi factors are weights. One classical use case is when the
target values are experimental observations or measurements.

Two engines devoted to least-squares problems are available. The first one is
based on the [Gauss-Newton](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/GaussNewtonOptimizer.html) method. The second one is the [Levenberg-Marquardt](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LevenbergMarquardtOptimizer.html) method.

<a id="userguide-leastsquares--14.2-leastsquaresbuilder-and-leastsquaresfactory"></a>

### 14.2 LeastSquaresBuilder and LeastSquaresFactory

In order to solve a least-squares fitting problem, the user must provide the following elements:

- a mean to evaluate all the components of the model for a given set of parameters:
  modeli = fi(p1, p2, ... pk),
  this is code
- the target (or observed) components: targeti, this is data
- the start values for all pk parameters: sk, this is data
- optionally a validator for the pk parameters, this is code
- optionally the weight for sample point i: wi, this is data and defaults to 1.0 if not provided
- a maximum number of iterations, this is data
- a maximum number of evaluations, this is data
- a convergence criterion, this is code

The elements of the list above can be provided as an implementation of the
[LeastSquaresProblem](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresProblem.html) interface. However, this is cumbersome to do directly, so some helper
classes are available. The first helper is a mutable builder:
[LeastSquaresBuilder](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresBuilder.html). The second helper is an utility factory:
[LeastSquaresFactory](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresFactory.html).

The builder class is better suited when setting the various elements of the least squares
problem is done progressively in different places in the user code. In this case, the user
would create first an empty builder andconfigure it progressively by calling its methods
(`start`, `target`, `model`, ...). Once the configuration
is complete, calling the `build` method would create the least squares problem.

The factory utility is better suited when the various elements of the least squares
problem are all known at one place and the problem can be built in just one sweep, calling
to one of the static `LeastSquaresFactory.create` method.

<a id="userguide-leastsquares--14.3-model-function"></a>

### 14.3 Model Function

The model function is used by the least squares engine to evaluate the model components
modeli given some test parameters pk. It is therefore a multivariate
function (it depends on the various pk) and it is vector-valued (it has several
components modeli). There must be exactly one component modeli for
each target (or observed) component targeti, otherwise some residuals to be
squared and summed could not be computed. In order for the problem to be well defined, the
number of parameters pk must be less than the number of components modeli.
Failing to ensure this may lead to the engine throwing an exception as the underlying linear
algebra operations may encounter singular matrices. It is not unusual to have a large number
of components (several thousands) and only a dozen parameters. There are no limitations on these
numbers, though.

As the least squares engine needs to create Jacobians matrices for the model function, both
its value and its derivatives *with respect to the pk parameters* must
be available. There are two ways to provide this:

- provide one
  [MultivariateVectorFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateVectorFunction.html)
  instance for computing the components values and one
  [MultivariateMatrixFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateMatrixFunction.html)
  instance for computing the components derivatives (i.e. the Jacobian matrix) with
  respect to the parameters,
- or provide one
  [MultivariateJacobianFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/MultivariateJacobianFunction.html)
  instance for computing both the components values and their derivatives simultaneously.

The first alternative is best suited for models which are not computationally intensive
as it allows more modularized code with one method for each type of computation. The second
alternative is best suited for models which are computationally intensive and evaluating
both the values and derivatives in one sweep saves a lot of work.

The `point` parameter of the `value` methods in the
[MultivariateVectorFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateVectorFunction.html), [MultivariateMatrixFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/MultivariateMatrixFunction.html), or [MultivariateJacobianFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/MultivariateJacobianFunction.html)
interfaces will contain the parameters pk. The values will be the model components
modeli and the derivatives will be the derivatives of the model components
with respect to the parameters dmodeli/dpk.

There are no requirements on how to compute value and derivatives. The
[DerivativeStructure](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/analysis/differentiation/DerivativeStructure.html) class may be useful to compute analytically derivatives in
difficult cases, but this class is not mandated by the API which only expects the derivatives
as a Jacobian matrix containing primitive double entries.

One non-obvious feature provided by both the builder and the factory is lazy evaluation. This feature
allows to defer calls to the model functions until they are really needed by the engine. This
can save some calls for engines that evaluate the value and the Jacobians in different loops
(this is the case for Levenberg-Marquardt). However, lazy evaluation is possible *only*
if the model functions are themselves separated, i.e. it can be used only with the first
alternative above. Setting up the `lazyEvaluation` flag to `true` in the builder
or factory and setting up the model function as one
[MultivariateJacobianFunction](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/MultivariateJacobianFunction.html)
instance at the same time will trigger an illegal state exception telling that the model function
misses required functionality.

<a id="userguide-leastsquares--14.4-parameters-validation"></a>

### 14.4 Parameters Validation

In some cases, the model function requires parameters to lie within a specific domain. For example
a parameter may be used in a square root and needs to be positive, or another parameter represents
the sine of an angle and should be within -1 and +1, or several parameters may need to remain in
the unit circle and the sum of their squares must be smaller than 1. The least square solvers available
in Apache Commons Math currently don't allow to set up constraints on the parameters. This is a
known missing feature. There are two ways to circumvent this.

Both ways are achieved by setting up a
[ParameterValidator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/ParameterValidator.html)
instance. The input of the value and jacobian model functions will always be the output of
the parameter validator if one exists.

One way to constrain parameters is to use a continuous mapping between the parameters that the
least squares solver will handle and the real parameters of the mathematical model. Using mapping
functions like `logit` and `sigmoid`, one can map a finite range to the
infinite real line. Using mapping functions based on `log` and `exp`, one
can map a semi-infinite range to the infinite real line. It is possible to use such a mapping so
that the engine will always see unbounded parameters, whereas on the other side of the mapping the
mathematical model will always see parameters mapped correctly to the expected range. Care must be
taken with derivatives as one must remember that the parameters have been mapped. Care must also
be taken with convergence status. This may be tricky.

Another way to constrain parameters is to simply truncate the parameters back to the domain when
one search point escapes from it and not care about derivatives. This works *only* if the
solution is expected to be inside the domain and not at the boundary, as points out of the domain
will only be temporary test points with a cost function higher than the real solution and will soon
be dropped by the underlying engine. As a rule of thumb, these conditions are met only when the
domain boundaries correspond to unrealistic values that will never be achieved (null distances, negative masses, ...) but they will not be met when the domain boundaries are more operational
limits (a maximum weight that can be handled by a device, a minimum temperature that can be
sustained by an instrument, ...).

<a id="userguide-leastsquares--14.5-tuning"></a>

### 14.5 Tuning

Among the elements to be provided to the least squares problem builder or factory
are some tuning parameters for the solver.

The maximum number of iterations refers to the engine algorithm main loop, whereas the
maximum number of iterations refers to the number of calls to the model method. Some
algorithms (like Levenberg-Marquardt) have two embedded loops, with iteration number
being incremented at outer loop level, but a new evaluation being done at each inner
loop. In this case, the number of evaluations will be greater than the number of iterations.
Other algorithms (like Gauss-Newton) have only one level of loops. In this case, the
number of evaluations will equal to the number of iterations. In any case, the maximum
numbers are really only intended as safeguard to prevent infinite loops, so the exact
value of the limit is not important so it is common to select some almost arbitrary number
much larger than the expected number of evaluations and use it for both
`maxIterations` and `maxEvaluations`. As an example, if the least
squares solver usually finds a solution in 50 iterations, setting a maximum value to 1000
is probably safe and prevents infinite loops. If the least squares solver needs several
hundreds of evaluations, it would probably be safer to set the maximum value to 10000 or
even 1000000 to avoid failures in slightly more demanding cases. Very fine tuning of
these maximum numbers is often worthless, they are only intended as safeguards.

Convergence checking is delegated to a dedicated interface from the `optim`
package: [ConvergenceChecker](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optim/ConvergenceChecker.html), parameterized with either the specific
[Evaluation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresProblem.Evaluation.html)
class used for least squares problems or the general
[PointVectorValuePair](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optim/PointVectorValuePair.html).
Each time convergence is checked, both the previous
and the current evaluations of the least squares problem are provided, so the checker can
compare them and decide whereas convergence has been reached or not. The predefined convergence
checker implementations that can be useful for least squares fitting are:

- [EvaluationRmsChecker](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/EvaluationRmsChecker.html),
  which uses only the normalized cost (square-root of the sum of squared of the residuals,
  divided by the number of measurements),
- [SimpleVectorValueChecker](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optim/SimpleVectorValueChecker.html),
  which uses the model components themselves (*not* the residuals),
- [SimplePointChecker<PointVectorValuePair>](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optim/SimplePointChecker.html),
  which uses the parameters.

Of course, users can also provide their own implementation of the
[ConvergenceChecker](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/optim/ConvergenceChecker.html)
interface.

<a id="userguide-leastsquares--14.6-optimization-engine"></a>

### 14.6 Optimization Engine

Once the least squares problem has been created, using either the builder or the factory, it is passed to an optimization engine for solving. Two engines devoted to least-squares
problems are available. The first one is
based on the [Gauss-Newton](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/GaussNewtonOptimizer.html) method. The second one is the [Levenberg-Marquardt](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LevenbergMarquardtOptimizer.html) method. For both increased readability and in order to leverage
possible future changes in the configuration, it is recommended to use the fluent-style API to
build and configure the optimizers. This means creating a first temporary version of the optimizer
with a default parameterless constructor, and then to set up the various configuration parameters
using the available `withXxx` methods that all return a new optimizer instance. Only the
final fully configured instance is used. As an example, setting up a Levenberg-Marquardt with
all configuration set to default except the cost relative tolerance and parameter relative tolerance
would be done as follows:

```

  LeastSquaresOptimizer optimizer = new LevenbergMarquardtOptimizer().
                                    withCostRelativeTolerance(1.0e-12).
                                    withParameterRelativeTolerance(1.0e-12);
        
```

As another example, setting up a Gauss-Newton optimizer and forcing the decomposition to SVD (the
default is QR decomposition) would be done as follows:

```

  LeastSquaresOptimizer optimizer = new GaussNewtonOptimizer().
                                    withwithDecomposition(GaussNewtonOptimizer.Decomposition.QR);
        
```

<a id="userguide-leastsquares--14.7-solving"></a>

### 14.7 Solving

Solving the least squares problem is done by calling the `optimize` method of the
optimizer and passing the least squares problem as the single parameter:

```

  LeastSquaresOptimizer.Optimum optimum = optimizer.optimize(leastSquaresProblem);
        
```

The [LeastSquaresOptimizer.Optimum](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresOptimizer.Optimum.html) class is a specialized
[Evaluation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresProblem.Evaluation.html)
with additional methods te retrieve the number of evaluations and number of iterations performed.
The most important methods are inherited from the
[Evaluation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/fitting/leastsquares/LeastSquaresProblem.Evaluation.html)
class and correspond to the point (i.e. the parameters), cost, Jacobian, RMS, covariance ...

<a id="userguide-leastsquares--14.8-example"></a>

### 14.8 Example

The following simple example shows how to find the center of a circle of known radius to
to best fit observed 2D points. It is a simplified version of one of the JUnit test cases.
In the complete test case, both the circle center and its radius are fitted, here the
radius is fixed.

```

  final double radius = 70.0;
  final Cartesian2D[] observedPoints = new Cartesian2D[] {
      new Cartesian2D( 30.0,  68.0),
      new Cartesian2D( 50.0,  -6.0),
      new Cartesian2D(110.0, -20.0),
      new Cartesian2D( 35.0,  15.0),
      new Cartesian2D( 45.0,  97.0)
  };

  // the model function components are the distances to current estimated center,
  // they should be as close as possible to the specified radius
  MultivariateJacobianFunction distancesToCurrentCenter = new MultivariateJacobianFunction() {
      public Pair<RealVector, RealMatrix> value(final RealVector point) {

          Cartesian2D center = new Cartesian2D(point.getEntry(0), point.getEntry(1));

          RealVector value = new ArrayRealVector(observedPoints.length);
          RealMatrix jacobian = new Array2DRowRealMatrix(observedPoints.length, 2);

          for (int i = 0; i < observedPoints.length; ++i) {
              Cartesian2D o = observedPoints[i];
              double modelI = Cartesian2D.distance(o, center);
              value.setEntry(i, modelI);
              // derivative with respect to p0 = x center
              jacobian.setEntry(i, 0, (center.getX() - o.getX()) / modelI);
              // derivative with respect to p1 = y center
              jacobian.setEntry(i, 1, (center.getX() - o.getX()) / modelI);
          }

          return new Pair<RealVector, RealMatrix>(value, jacobian);

      }
  };

  // the target is to have all points at the specified radius from the center
  double[] prescribedDistances = new double[observedPoints.length];
  Arrays.fill(prescribedDistances, radius);

  // least squares problem to solve : modeled radius should be close to target radius
  LeastSquaresProblem problem = new LeastSquaresBuilder().
                                start(new double[] { 100.0, 50.0 }).
                                model(distancesToCurrentCenter).
                                target(prescribedDistances).
                                lazyEvaluation(false).
                                maxEvaluations(1000).
                                maxIterations(1000).
                                build();
  LeastSquaresOptimizer.Optimum optimum = new LevenbergMarquardtOptimizer().optimize(problem);
  Cartesian2D fittedCenter = new Cartesian2D(optimum.getPoint().getEntry(0), optimum.getPoint().getEntry(1));
  System.out.println("fitted center: " + fittedCenter.getX() + " " + fittedCenter.getY());
  System.out.println("RMS: "           + optimum.getRMS());
  System.out.println("evaluations: "   + optimum.getEvaluations());
  System.out.println("iterations: "    + optimum.getIterations());
        
```

---

<a id="userguide-ode"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/ode.html -->

<!-- page_index: 21 -->

<a id="userguide-ode--15-ordinary-differential-equations-integration"></a>

## 15 Ordinary Differential Equations Integration

<a id="userguide-ode--15.1-overview"></a>

### 15.1 Overview

The ode package provides classes to solve Ordinary Differential Equations problems.

This package solves Initial Value Problems of the form y'=f(t,y) with t0
and y(t0)=y0 known. The provided integrators compute an estimate
of y(t) from t=t0 to t=t1.

All integrators provide dense output. This means that besides computing the state vector
at discrete times, they also provide a cheap means to get both the state and its derivative
between the time steps. They do so through classes extending the
[StepInterpolator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/StepInterpolator.html)
abstract class, which are made available to the user at the end of each step.

All integrators handle multiple discrete events detection based on switching
functions. This means that the integrator can be driven by user specified discrete events
(occurring when the sign of user-supplied *switching function* changes). The steps are
shortened as needed to ensure the events occur at step boundaries (even if the integrator
is a fixed-step integrator). When the events are triggered, integration can
be stopped (this is called a G-stop facility), the state vector can be changed, or integration
can simply go on. The latter case is useful to handle discontinuities in the differential
equations gracefully and get accurate dense output even close to the discontinuity.

All integrators support setting a maximal number of evaluations of differential
equations function. If this number is exceeded, an exception will be thrown during
integration. This can be used to prevent infinite loops if for example error control or
discrete events create a really large number of extremely small steps. By default, the
maximal number of evaluation is set to `Integer.MAX_VALUE` (i.e. 231-1
or 2147483647). It is recommended to set this maximal number to a value suited to the ODE
problem, integration range, and step size or error control settings.

All integrators support expanding the main ODE with one or more secondary ODE to manage
additional state that will be integrated together with the main state. This can be used
for example to integrate variational equations and compute not only the main state but also
its partial derivatives with respect to either the initial state or some parameters, these
derivatives being handled be secondary ODE (see below for an example).

Two parallel APIs are available. The first is devoted to solve ode for which the integration free
variable t and the state y(t) are primitive double and primitive double array respectively. Starting
with version 3.6, a second API is devoted to solve ode for which the integration free
variable t and the state y(t) are `RealFieldElement` and `RealFieldElement`
array respectively. This allow for example users to integrate ode where the computation values
are for example `DerivativeStructure` elements, hence automatically computing
partial derivatives with respect to some equations parameters without a need to set up the
variational equations. Another example is to use `Dfp` elements in order to solve
ode with extended precision. As of 3.6, the API are slightly different, mainly in the way they
handle arrays. Both API will become more similar in 4.0 and future versions as the older
primitive double API will be modified to match the newer field API. This cannot be done in
3.6 for compatibility reasons.

The user should describe his problem in his own classes which should implement the
[FirstOrderDifferentialEquations](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderDifferentialEquations.html)
interface (or [FirstOrderFieldDifferentialEquations](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderFieldDifferentialEquations.html)
interface). Then they should pass it to the integrator they prefer among all the classes that implement
the [FirstOrderIntegrator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderIntegrator.html)
interface (or the [FirstOrderFieldIntegrator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderFieldIntegrator.html)
interface). The following example shows how to implement the simple two-dimensional problem using double primitives:

- y'0(t) = ω × (c1 - y1(t))
- y'1(t) = ω × (y0(t) - c0)

with some initial state y(t0) = (y0(t0), y1(t0)).
In fact, the exact solution of this problem is that y(t) moves along a circle
centered at c = (c0, c1) with constant angular rate ω.

```
private static class CircleODE implements FirstOrderDifferentialEquations {
private double[] c; private double omega;
public CircleODE(double[] c, double omega) {this.c     = c; this.omega = omega;}
public int getDimension() {return 2;}
public void computeDerivatives(double t, double[] y, double[] yDot) {yDot[0] = omega * (c[1] - y[1]); yDot[1] = omega * (y[0] - c[0]);}
}
```

Computing the state y(16.0) starting from y(0.0) = (0.0, 1.0) and integrating the ODE
is done as follows (using Dormand-Prince 8(5,3) integrator as an example):

```

FirstOrderIntegrator dp853 = new DormandPrince853Integrator(1.0e-8, 100.0, 1.0e-10, 1.0e-10);
FirstOrderDifferentialEquations ode = new CircleODE(new double[] { 1.0, 1.0 }, 0.1);
double[] y = new double[] { 0.0, 1.0 }; // initial state
dp853.integrate(ode, 0.0, y, 16.0, y); // now y contains final state at time t=16.0
        
```

<a id="userguide-ode--15.2-continuous-output"></a>

### 15.2 Continuous Output

The solution of the integration problem is provided by two means. The first one is aimed towards
simple use: the state vector at the end of the integration process is copied in the y array of the
`FirstOrderIntegrator.integrate` method, as shown by previous example. The second one
should be used when more in-depth information is needed throughout the integration process. The user
can register an object implementing the
[StepHandler](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/StepHandler.html) interface or a
[StepNormalizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/StepNormalizer.html) object wrapping
a user-specified object implementing the
[FixedStepHandler](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/FixedStepHandler.html) interface
into the integrator before calling the `FirstOrderIntegrator.integrate` method. The user object
will be called appropriately during the integration process, allowing the user to process intermediate
results. The default step handler does nothing. Considering again the previous example, we want to print the
trajectory of the point to check it really is a circle arc. We simply add the following before the call
to integrator.integrate:

```
StepHandler stepHandler = new StepHandler() {public void init(double t0, double[] y0, double t) {}
public void handleStep(StepInterpolator interpolator, boolean isLast) {double   t = interpolator.getCurrentTime(); double[] y = interpolator.getInterpolatedState(); System.out.println(t + " " + y[0] + " " + y[1]);} }; integrator.addStepHandler(stepHandler);
```

[ContinuousOutputModel](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/ContinuousOutputModel.html)
is a special-purpose step handler that is able to store all steps and to provide transparent access to
any intermediate result once the integration is over. An important feature of this class is that it
implements the `Serializable` interface. This means that a complete continuous model of the
integrated function throughout the integration range can be serialized and reused later (if stored into
a persistent medium like a file system or a database) or elsewhere (if sent to another application).
Only the result of the integration is stored, there is no reference to the integrated problem by itself.

Other default implementations of the [StepHandler](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/StepHandler.html)
interface are available for general needs
([DummyStepHandler](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/DummyStepHandler.html), [StepNormalizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/StepNormalizer.html)) and custom
implementations can be developed for specific needs. As an example, if an application is to be
completely driven by the integration process, then most of the application code will be run inside a
step handler specific to this application.

Some integrators (the simple ones) use fixed steps that are set at creation time. The more efficient
integrators use variable steps that are handled internally in order to control the integration error
of the main state with respect to a specified accuracy (these integrators extend the
[AdaptiveStepsizeIntegrator](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/AdaptiveStepsizeIntegrator.html)
abstract class). The secondary equations are explicitly ignored for step size control, in order to get reproducible
results regardless of the secondary equations being integrated or not. The step handler which is called after each
successful step shows up the variable stepsize. The [StepNormalizer](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/StepNormalizer.html)
class can be used to convert the variable stepsize into a fixed stepsize that can be handled by classes
implementing the [FixedStepHandler](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/sampling/FixedStepHandler.html)
interface. Adaptive stepsize integrators can automatically compute the initial stepsize by themselves, however the user can specify it if they prefer to retain full control over the integration or if the
automatic guess is wrong.

<a id="userguide-ode--15.3-discrete-events-handling"></a>

### 15.3 Discrete Events Handling

ODE problems are continuous ones. However, sometimes discrete events must be
taken into account. The most frequent case is the stop condition of the integrator
is not defined by the time t but by a target condition on state y (say y[0] = 1.0
for example).

Discrete events detection is based on switching functions. The user provides
a simple [g(t, y)](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/events/EventHandler.html)
function depending on the current time and state. The integrator will monitor
the value of the function throughout integration range and will trigger the
event when its sign changes. The magnitude of the value is almost irrelevant.
For the sake of root finding, it should however be continuous (but not necessarily smooth)
at least in the roots vicinity. The steps are shortened as needed to ensure the events occur
at step boundaries (even if the integrator is a fixed-step integrator).

When an event is triggered, the event time, current state and an indicator
whether the switching function was increasing or decreasing at event time
are provided to the user. Several different options are available to him:

- integration can be stopped (this is called a G-stop facility),
- the state vector or the derivatives can be changed,
- or integration can simply go on.

The first case, G-stop, is the most common one. A typical use case is when an
ODE must be solved up to some target state is reached, with a known value of
the state but an unknown occurrence time. As an example, if we want to monitor
a chemical reaction up to some predefined concentration for the first substance, we can use the following switching function setting:

```
public double g(double t, double[] y) {return y[0] - targetConcentration;}
public int eventOccurred(double t, double[] y, boolean increasing) {return STOP;}
```

The second case, change state vector or derivatives is encountered when dealing
with discontinuous dynamical models. A typical case would be the motion of a
spacecraft when thrusters are fired for orbital maneuvers. The acceleration is
smooth as long as no maneuvers are performed, depending only on gravity, drag, third body attraction, radiation pressure. Firing a thruster introduces a
discontinuity that must be handled appropriately by the integrator. In such a case, we would use a switching function setting similar to this:

```
public double g(double t, double[] y) {return (t - tManeuverStart) * (t - tManeuverStop);}
public int eventOccurred(double t, double[] y, boolean increasing) {return RESET_DERIVATIVES;}
```

The third case is useful mainly for monitoring purposes, a simple example is:

```
public double g(double t, double[] y) {return y[0] - y[1];}
public int eventOccurred(double t, double[] y, boolean increasing) {logger.log("y0(t) and y1(t) curves cross at t = " + t); return CONTINUE;}
```

<a id="userguide-ode--15.4-available-integrators"></a>

### 15.4 Available Integrators

The tables below show the various integrators available for non-stiff problems. Note that the
implementations of Adams-Bashforth and Adams-Moulton are adaptive stepsize, not fixed stepsize
as is usual for these multi-step integrators. This is due to the fact the implementation relies
on the Nordsieck vector representation of the state.

<table align="center" border="1" class="bodyTable">
<tr>
<td align="center" colspan="2">Fixed Step Integrators</td></tr>
<tr>
<td align="center">Name</td>
<td>Order</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/EulerIntegrator.html">Euler</a></td>
<td>1</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/MidpointIntegrator.html">Midpoint</a></td>
<td>2</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/ClassicalRungeKuttaIntegrator.html">Classical Runge-Kutta</a></td>
<td>4</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/GillIntegrator.html">Gill</a></td>
<td>4</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/ThreeEighthesIntegrator.html">3/8</a></td>
<td>4</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/LutherIntegrator.html">Luther</a></td>
<td>6</td></tr>
</table>

<table align="center" border="1" class="bodyTable">
<tr>
<td align="center" colspan="3">Adaptive Stepsize Integrators</td></tr>
<tr>
<td align="center">Name</td>
<td>Integration Order</td>
<td>Error Estimation Order</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/HighamHall54Integrator.html">Higham and Hall</a></td>
<td>5</td>
<td>4</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/DormandPrince54Integrator.html">Dormand-Prince 5(4)</a></td>
<td>5</td>
<td>4</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/DormandPrince853Integrator.html">Dormand-Prince 8(5,3)</a></td>
<td>8</td>
<td>5 and 3</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/GraggBulirschStoerIntegrator.html">Gragg-Bulirsch-Stoer</a></td>
<td>variable (up to 18 by default)</td>
<td>variable</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/AdamsBashforthIntegrator.html">Adams-Bashforth</a></td>
<td>variable</td>
<td>variable</td></tr>
<tr>
<td align="center"><a href="https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/nonstiff/AdamsMoultonIntegrator.html">Adams-Moulton</a></td>
<td>variable</td>
<td>variable</td></tr>
</table>

<a id="userguide-ode--15.5-derivatives"></a>

### 15.5 Derivatives

If in addition to state y(t) the user needs to compute the sensitivity of the final state with respect to
the initial state (dy/dy0) or the sensitivity of the final state with respect to some parameters
of the ODE (dy/dpk), they need to register the variational equations as a set of secondary equations
appended to the main state before the integration starts. Then the integration will propagate the compound
state composed of both the main state and its partial derivatives. At the end of the integration, the Jacobian
matrices are extracted from the integrated secondary state. The [JacobianMatrices](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/JacobianMatrices.html) class can do most of
this as long as the local derivatives are provided to it. It will set up the variational equations, register
them as secondary equations into the ODE, and it will set up the initial values and retrieve the intermediate
and final values as Jacobian matrices.

If for example the original state dimension is 6 and there are 3 parameters, the compound state will be a 60
elements array. The first 6 elements will be the original state, the next 36 elements will represent the 6x6
Jacobian matrix of the final state with respect to the initial state, and the remaining 18 elements will
represent the 6x3 Jacobian matrix of the final state with respect to the 3 parameters. The [JacobianMatrices](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/JacobianMatrices.html) class does the mapping
between the 60 elements compound state and the Jacobian matrices and sets up the correcsponding secondary equations.

As the variational equations are considered to be secondary equations here, variable step integrators ignore
them for step size control: they rely only on the main state. This feature is a design choice. The rationale is
to get exactly the same steps, regardless of the Jacobians being computed or not, hence ensuring reproducible
results in both cases.

What remains of user responsibility is to provide the local Jacobians df(t, y, p)/dy and df(t, y, p)/dpk
corresponding the the main ODE y'=f(t, y, p). The main ODE is as usual provided by the user as a class implementing
the [FirstOrderDifferentialEquations](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderDifferentialEquations.html)
interface or a sub-interface.

If the ODE is simple enough that the user can implement df(t, y, p)/dy directly, then instead of providing an
implementation of the [FirstOrderDifferentialEquations](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderDifferentialEquations.html)
interface only, the user should rather provide an implementation of the [MainStateJacobianProvider](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/MainStateJacobianProvider.html) interface, which extends the previous interface by adding a method to compute df(t, y, p)/dy. The user class is used as a
constructor parameter of the [JacobianMatrices](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/JacobianMatrices.html)
class. If the ODE is too complex or the user simply does not bother implementing df(t, y, p)/dy directly, then
the ODE can still be implemented using the simple [FirstOrderDifferentialEquations](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/FirstOrderDifferentialEquations.html)
interface and given as such to another constructor of the [JacobianMatrices](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/JacobianMatrices.html) class, but in this case an array
hy must also be provided that will contain the step size to use form each component of the main state vector y, and
the Jacobian f(t, y, p)/dy will be computed internally using finite differences. This will of course trigger more evaluations
of the ODE at each step and will suffer from finite differences errors, but it is much simpler to implement from a user
point of view.

The parameters are identified by a name (a simple user-defined string), which are also specified at [JacobianMatrices](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/JacobianMatrices.html) class construction. If the ODE
is simple enough that the user can implement df(t, y, p)/dpk directly for some of the parameters pk, then they can provide one or more classes implementing the [ParameterJacobianProvider](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/ode/ParameterJacobianProvider.html) interface by
calling the JacobianMatrices.addParameterJacobianProvide method. The parameters are handled one at a time, but all the calls to
ParameterJacobianProvider.computeParameterJacobian will be grouped in one sequence after the call to MainStateJacobianProvider.computeMainStateJacobian
This feature can be used when all the derivatives share a lot of costly computation. In this case, the user
is advised to compute all the needed derivatives at once during the call to computeMainStateJacobian, including the
partial derivatives with respect to the parameters and to store the derivatives temporary. Then when the next calls to
computeParameterJacobian will be triggerred, it will be sufficient to return the already computed derivatives. With this
architecture, many computation can be saved. This of course implies that the classes implementing both interfaces know
each other (they can even be the same class if desired, but it is not required). If the ODE is too complex or the user
simply does not bother implementing df(t, y, p)/dpk directly for some k, then
the JacobianMatrices.setParameterStep method should be called so finite differences are used to compute the derivatives
for this parameter. It is possible to have some parameters for which derivatives are provided by a direct implementation
while other parameters are computed using finite differences during the same integration.

The following example corresponds to a simple case where all derivatives can be computed analytically. The state is
a 2D point travelling along a circle. There are three parameters : the two coordinates of the center and the
angular velocity.

```

public class CircleODE implements MainStateJacobianProvider, ParameterJacobianProvider {

    public static final String CENTER_X = "cx";
    public static final String CENTER_Y = "cy";
    public static final String OMEGA    = "omega";

    private double[] c;
    private double omega;
    private double[][] savedDfDp;

    public CircleODE(double[] c, double omega) {
        this.c     = c;
        this.omega = omega;
        this.savedDfDp = new double[2][3];
    }

    public int getDimension() {
        return 2;
    }

    public void computeDerivatives(double t, double[] y, double[] yDot) {
        // the state is a 2D point, the ODE therefore corresponds to the velocity
        yDot[0] = omega * (c[1] - y[1]);
        yDot[1] = omega * (y[0] - c[0]);
    }

    public Collection<String> getParametersNames() {
        return Arrays.asList(CENTER_X, CENTER_Y, OMEGA);
    }

    public boolean isSupported(String name) {
        return CENTER_X.equals(name) || CENTER_Y.equals(name) || OMEGA.equals(name);
    }

    public void computeMainStateJacobian(double t, double[] y, double[] yDot, double[][] dFdY) {

        // compute the Jacobian of the main state
        dFdY[0][0] = 0;
        dFdY[0][1] = -omega;
        dFdY[1][0] = omega;
        dFdY[1][1] = 0;

        // precompute the derivatives with respect to the parameters,
        // they will be provided back when computeParameterJacobian are called later on
        savedDfDp[0][0] = 0;
        savedDfDp[0][1] = omega;
        savedDfDp[0][2] = c[1] - y[1];
        savedDfDp[1][0] = -omega;
        savedDfDp[1][1] = 0;
        savedDfDp[1][2] = y[0] - c[0];

    }

    public void computeParameterJacobian(double t, double[] y, double[] yDot,
                                         String paramName, double[] dFdP) {
        // we simply return the derivatives precomputed earlier
        if (CENTER_X.equals(paramName)) {
            dFdP[0] = savedDfDp[0][0];
            dFdP[1] = savedDfDp[1][0];
        } else if (CENTER_Y.equals(paramName)) {
            dFdP[0] = savedDfDp[0][1];
            dFdP[1] = savedDfDp[1][1];
        } else {
            dFdP[0] = savedDfDp[0][2];
            dFdP[1] = savedDfDp[1][2];
        }
     }

}
        
```

This ODE is integrated as follows:

```

        CircleODE circle = new CircleODE(new double[] {1.0,  1.0 }, 0.1);

        // here, we could select only a subset of the parameters, or use another order
        JacobianMatrices jm = new JacobianMatrices(circle, CircleODE.CENTER_X, CircleODE.CENTER_Y, CircleODE.OMEGA);
        jm.addParameterJacobianProvider(circle);

        ExpandableStatefulODE efode = new ExpandableStatefulODE(circle);
        efode.setTime(0);
        double[] y = { 1.0, 0.0 };
        efode.setPrimaryState(y);

        // create the variational equations and append them to the main equations, as secondary equations
        jm.registerVariationalEquations(efode);

        // integrate the compound state, with both main and additional equations
        DormandPrince853Integrator integrator = new DormandPrince853Integrator(1.0e-6, 1.0e3, 1.0e-10, 1.0e-12);
        integrator.setMaxEvaluations(5000);
        integrator.integrate(efode, 20.0);

        // retrieve the Jacobian of the final state with respect to initial state
        double[][] dYdY0 = new double[2][2];
        jm.getCurrentMainSetJacobian(dYdY0);

        // retrieve the Jacobians of the final state with resepct to the various parameters
        double[]   dYdCx = new double[2];
        double[]   dYdCy = new double[2];
        double[]   dYdOm = new double[2];
        jm.getCurrentParameterJacobian(CircleODE.CENTER_X, dYdCx);
        jm.getCurrentParameterJacobian(CircleODE.CENTER_Y, dYdCy);
        jm.getCurrentParameterJacobian(CircleODE.OMEGA,    dYdOm);
        
```

---

<a id="userguide-genetics"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/genetics.html -->

<!-- page_index: 22 -->

<a id="userguide-genetics--16-genetic-algorithms"></a>

## 16 Genetic Algorithms

<a id="userguide-genetics--16.1-overview"></a>

### 16.1 Overview

The genetics package provides a framework and implementations for
genetic algorithms.

<a id="userguide-genetics--16.2-ga-framework"></a>

### 16.2 GA Framework

[GeneticAlgorithm](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/GeneticAlgorithm.html) provides an execution framework for Genetic Algorithms (GA).
[Populations,](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/Population.html) consisting of [Chromosomes](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/Chromosome.html) are evolved by the `GeneticAlgorithm` until a
[StoppingCondition](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/StoppingCondition.html) is reached. Evolution is determined by [SelectionPolicy](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/SelectionPolicy.html), [MutationPolicy](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/MutationPolicy.html) and [Fitness](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/Fitness.html).

The GA itself is implemented by the `evolve` method of the
`GeneticAlgorithm` class, which looks like this:

```
public Population evolve(Population initial, StoppingCondition condition) {Population current = initial; while (!condition.isSatisfied(current)) {current = nextGeneration(current);} return current;}
```

The `nextGeneration` method implements the following algorithm:

1. Get nextGeneration population to fill from `current`
   generation, using its nextGeneration method
2. Loop until new generation is filled:

- Apply configured `SelectionPolicy` to select a pair of parents
  from `current`
- With probability =
  [getCrossoverRate()](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/GeneticAlgorithm.html#getCrossoverRate), apply configured `CrossoverPolicy` to parents
- With probability =
  [getMutationRate()](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/GeneticAlgorithm.html#getMutationRate),
  apply configured `MutationPolicy` to each of the offspring
- Add offspring individually to nextGeneration,
  space permitting

3. Return nextGeneration

<a id="userguide-genetics--16.3-implementation"></a>

### 16.3 Implementation

Here is an example GA execution:

```

// initialize a new genetic algorithm
GeneticAlgorithm ga = new GeneticAlgorithm(
    new OnePointCrossover<Integer>(),
    1,
    new RandomKeyMutation(),
    0.10,
    new TournamentSelection(TOURNAMENT_ARITY)
);

// initial population
Population initial = getInitialPopulation();

// stopping condition
StoppingCondition stopCond = new FixedGenerationCount(NUM_GENERATIONS);

// run the algorithm
Population finalPopulation = ga.evolve(initial, stopCond);

// best chromosome from the final population
Chromosome bestFinal = finalPopulation.getFittestChromosome();
        
```

The arguments to the `GeneticAlgorithm` constructor above are:

| Parameter | value in example | meaning |
| --- | --- | --- |
| crossoverPolicy | [OnePointCrossover](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/OnePointCrossover.html) | A random crossover point is selected and the first part from each parent is copied to the corresponding child, and the second parts are copied crosswise. |
| crossoverRate | 1 | Always apply crossover |
| mutationPolicy | [RandomKeyMutation](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/RandomKeyMutation.html) | Changes a randomly chosen element of the array representation to a random value uniformly distributed in [0,1]. |
| mutationRate | .1 | Apply mutation with probability 0.1 - that is, 10% of the time. |
| selectionPolicy | [TournamentSelection](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/TournamentSelection.html) | Each of the two selected chromosomes is selected based on an n-ary tournament -- this is done by drawing n random chromosomes without replacement from the population, and then selecting the fittest chromosome among them. |

The algorithm starts with an `initial` population of `Chromosomes.` and executes until
the specified [StoppingCondition](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/StoppingCondition.html)
is reached. In the example above, a
[FixedGenerationCount](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/genetics/FixedGenerationCount.html)
stopping condition is used, which means the algorithm proceeds through a fixed number of generations.

---

<a id="userguide-filter"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/filter.html -->

<!-- page_index: 23 -->

<a id="userguide-filter--17-filters"></a>

## 17 Filters

<a id="userguide-filter--17.1-overview"></a>

### 17.1 Overview

The filter package currently provides only an implementation of a Kalman filter.

<a id="userguide-filter--17.2-kalman-filter"></a>

### 17.2 Kalman Filter

[KalmanFilter](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/filter/KalmanFilter.html) provides a discrete-time filter to estimate
a stochastic linear process.

A Kalman filter is initialized with a [ProcessModel](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/filter/ProcessModel.html) and a [MeasurementModel](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/org/apache/commons/math4/legacy/filter/MeasurementModel.html), which contain the corresponding transformation and noise covariance matrices.
The parameter names used in the respective models correspond to the following names commonly used
in the mathematical literature:

- A - state transition matrix
- B - control input matrix
- H - measurement matrix
- Q - process noise covariance matrix
- R - measurement noise covariance matrix
- P - error covariance matrix

Initialization
:   The following code will create a Kalman filter using the provided
    DefaultMeasurementModel and DefaultProcessModel classes. To support dynamically changing
    process and measurement noises, simply implement your own models.

```

// A = [ 1 ]
RealMatrix A = new Array2DRowRealMatrix(new double[] { 1d });
// no control input
RealMatrix B = null;
// H = [ 1 ]
RealMatrix H = new Array2DRowRealMatrix(new double[] { 1d });
// Q = [ 0 ]
RealMatrix Q = new Array2DRowRealMatrix(new double[] { 0 });
// R = [ 0 ]
RealMatrix R = new Array2DRowRealMatrix(new double[] { 0 });

ProcessModel pm
   = new DefaultProcessModel(A, B, Q, new ArrayRealVector(new double[] { 0 }), null);
MeasurementModel mm = new DefaultMeasurementModel(H, R);
KalmanFilter filter = new KalmanFilter(pm, mm);
            
```

Iteration
:   The following code illustrates how to perform the predict/correct cycle:

```

for (;;) {
   // predict the state estimate one time-step ahead
   // optionally provide some control input
   filter.predict();

   // obtain measurement vector z
   RealVector z = getMeasurement();

   // correct the state estimate with the latest measurement
   filter.correct(z);

   double[] stateEstimate = filter.getStateEstimation();
   // do something with it
}
          
```

Constant Voltage Example
:   The following example creates a Kalman filter for a static process: a system with a
    constant voltage as internal state. We observe this process with an artificially
    imposed measurement noise of 0.1V and assume an internal process noise of 1e-5V.

```

double constantVoltage = 10d;
double measurementNoise = 0.1d;
double processNoise = 1e-5d;

// A = [ 1 ]
RealMatrix A = new Array2DRowRealMatrix(new double[] { 1d });
// B = null
RealMatrix B = null;
// H = [ 1 ]
RealMatrix H = new Array2DRowRealMatrix(new double[] { 1d });
// x = [ 10 ]
RealVector x = new ArrayRealVector(new double[] { constantVoltage });
// Q = [ 1e-5 ]
RealMatrix Q = new Array2DRowRealMatrix(new double[] { processNoise });
// P = [ 1 ]
RealMatrix P0 = new Array2DRowRealMatrix(new double[] { 1d });
// R = [ 0.1 ]
RealMatrix R = new Array2DRowRealMatrix(new double[] { measurementNoise });

ProcessModel pm = new DefaultProcessModel(A, B, Q, x, P0);
MeasurementModel mm = new DefaultMeasurementModel(H, R);
KalmanFilter filter = new KalmanFilter(pm, mm);

// process and measurement noise vectors
RealVector pNoise = new ArrayRealVector(1);
RealVector mNoise = new ArrayRealVector(1);

RandomGenerator rand = new JDKRandomGenerator();
// iterate 60 steps
for (int i = 0; i < 60; i++) {
    filter.predict();

    // simulate the process
    pNoise.setEntry(0, processNoise * rand.nextGaussian());

    // x = A * x + p_noise
    x = A.operate(x).add(pNoise);

    // simulate the measurement
    mNoise.setEntry(0, measurementNoise * rand.nextGaussian());

    // z = H * x + m_noise
    RealVector z = H.operate(x).add(mNoise);

    filter.correct(z);

    double voltage = filter.getStateEstimation()[0];
}
          
```

Increasing Speed Vehicle Example
:   The following example creates a Kalman filter for a simple linear process: a
    vehicle driving along a street with a velocity increasing at a constant rate. The process
    state is modeled as (position, velocity) and we only observe the position. A measurement
    noise of 10m is imposed on the simulated measurement.

```

// discrete time interval
double dt = 0.1d;
// position measurement noise (meter)
double measurementNoise = 10d;
// acceleration noise (meter/sec^2)
double accelNoise = 0.2d;

// A = [ 1 dt ]
//     [ 0  1 ]
RealMatrix A = new Array2DRowRealMatrix(new double[][] { { 1, dt }, { 0, 1 } });
// B = [ dt^2/2 ]
//     [ dt     ]
RealMatrix B = new Array2DRowRealMatrix(new double[][] { { Math.pow(dt, 2d) / 2d }, { dt } });
// H = [ 1 0 ]
RealMatrix H = new Array2DRowRealMatrix(new double[][] { { 1d, 0d } });
// x = [ 0 0 ]
RealVector x = new ArrayRealVector(new double[] { 0, 0 });

RealMatrix tmp = new Array2DRowRealMatrix(new double[][] {
    { Math.pow(dt, 4d) / 4d, Math.pow(dt, 3d) / 2d },
    { Math.pow(dt, 3d) / 2d, Math.pow(dt, 2d) } });
// Q = [ dt^4/4 dt^3/2 ]
//     [ dt^3/2 dt^2   ]
RealMatrix Q = tmp.scalarMultiply(Math.pow(accelNoise, 2));
// P0 = [ 1 1 ]
//      [ 1 1 ]
RealMatrix P0 = new Array2DRowRealMatrix(new double[][] { { 1, 1 }, { 1, 1 } });
// R = [ measurementNoise^2 ]
RealMatrix R = new Array2DRowRealMatrix(new double[] { Math.pow(measurementNoise, 2) });

// constant control input, increase velocity by 0.1 m/s per cycle
RealVector u = new ArrayRealVector(new double[] { 0.1d });

ProcessModel pm = new DefaultProcessModel(A, B, Q, x, P0);
MeasurementModel mm = new DefaultMeasurementModel(H, R);
KalmanFilter filter = new KalmanFilter(pm, mm);

RandomGenerator rand = new JDKRandomGenerator();

RealVector tmpPNoise = new ArrayRealVector(new double[] { Math.pow(dt, 2d) / 2d, dt });
RealVector mNoise = new ArrayRealVector(1);

// iterate 60 steps
for (int i = 0; i < 60; i++) {
    filter.predict(u);

    // simulate the process
    RealVector pNoise = tmpPNoise.mapMultiply(accelNoise * rand.nextGaussian());

    // x = A * x + B * u + pNoise
    x = A.operate(x).add(B.operate(u)).add(pNoise);

    // simulate the measurement
    mNoise.setEntry(0, measurementNoise * rand.nextGaussian());

    // z = H * x + m_noise
    RealVector z = H.operate(x).add(mNoise);

    filter.correct(z);

    double position = filter.getStateEstimation()[0];
    double velocity = filter.getStateEstimation()[1];
}
          
```

Copyright © 2003-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Math, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="userguide-exceptions"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/userguide/exceptions.html -->

<!-- page_index: 24 -->

<a id="userguide-exceptions--19-exceptions"></a>

## 19 Exceptions

<a id="userguide-exceptions--19.1-overview"></a>

### 19.1 Overview

Commons Math defines a set of exceptions in order to convey the
precise low-level cause of failure.

<a id="userguide-exceptions--19.2-unchecked-exceptions"></a>

### 19.2 Unchecked Exceptions

Starting from version 3.0, all exceptions generated by the
Commons Math code are *unchecked* (i.e. they inherit from
the standard `RuntimeException` class).
The main rationale supporting this design decision is that the
exceptions generated in the library are not recoverable: They most
of the time result from bad input parameters or some failure due to
numerical problems.
A thorough discussion of the pros and cons of checked and unchecked
exceptions can be read in
[this post](http://www.mindview.net/Etc/Discussions/CheckedExceptions) by Bruce Eckel.

<a id="userguide-exceptions--19.3-hierarchies"></a>

### 19.3 Hierarchies

The exceptions defined by Commons Math follow the Java standard
hierarchies:

- [`IllegalArgumentException`](http://docs.oracle.com/javase/6/docs/api/java/lang/IllegalArgumentException.html):
  A [`MathIllegalArgumentException`](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/MathIllegalArgumentException.html) is thrown when some input
  parameter fails a precondition check.
- [`IllegalStateException`](http://docs.oracle.com/javase/6/docs/api/java/lang/IllegalStateException.html):
  A [`MathIllegalStateException`](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/MathIllegalStateException.html) is thrown when some inconsistency
  has been detected.
- [`ArithmeticException`](http://docs.oracle.com/javase/6/docs/api/java/lang/MathArithmeticException.html):
  A [`MathArithmeticException`](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/MathArithmeticException.html) is thrown when conditions such as
  "division by zero" or "overflow" are encountered.
- [`UnsupportedOperationException`](http://docs.oracle.com/javase/6/docs/api/java/lang/MathUnsupportedOperationException.html):
  A [`MathUnsupportedOperationException`](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/MathUnsupportedOperationException.html) indicates that a feature
  is missing or does not make sense in the given context.

In all of the above exception hierarchies, several subclasses can
exist, each conveying a specific underlying cause of the problem.

<a id="userguide-exceptions--19.4-features"></a>

### 19.4 Features

- Localization

  The detailed error messages (i.e. the string returned by the
  [getLocalizedMessage](http://docs.oracle.com/javase/6/docs/api/java/lang/Throwable.html#getLocalizedMessage()) method) can be localized.
  However, besides the American/English default, French is the only language
  for which a translation resource is available.
- Exception "context"

  Every exception generated by Commons Math implements the
  [ExceptionContextProvider](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/util/ExceptionContextProvider.html) interface. A call to the
  [getContext](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/util/ExceptionContextProvider.html#getContext) method will return the
  [ExceptionContext](https://commons.apache.org/proper/commons-math/commons-math-legacy-exception/apidocs/org/apache/commons/math4/legacy/exception/util/ExceptionContext.html) instance stored in the exception, which the
  user can further customize by adding messages and/or any object.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/project-info.html -->

<!-- page_index: 25 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons Math project is a library of lightweight mathematics and statistics components addressing common practical problems. |
| [Summary](#summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-math/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-math/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependency Information](https://commons.apache.org/proper/commons-math/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-math/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-math/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-math/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-math/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/summary.html -->

<!-- page_index: 26 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Math |
| Description | The Apache Commons Math project is a library of lightweight mathematics and statistics components addressing common practical problems. |
| Homepage | [http://commons.apache.org/proper/commons-math/](#index) |

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
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-parent |
| Version | 4.0-SNAPSHOT |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/modules.html -->

<!-- page_index: 27 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Miscellaneous core classes](#commons-math4-core) | Alternate implementations of JDK's "Math" functions. |
| [Artificial neural networks](#commons-math4-neuralnet) | Artificial neural networks: Self-organizing feature map (SOFM). |
| [Transforms](#commons-math4-transform) | Fourier, Sine, Cosine, Hadamard. |
| [Exception classes (Legacy)](#commons-math4-legacy-exception) | Exception classes used by code in "legacy" modules. |
| [Miscellaneous core classes (Legacy)](#commons-math4-legacy-core) | Field, Dfp, ... |
| [Apache Commons Math (Legacy)](#commons-math4-legacy) | Codes that are either currently unsupported or not yet modularized. |
| [Apache Commons Math Documentation](#commons-math-docs) | Aggregator module to genenerate Apache Commons Math documentation. |
| [Example applications](#commons-math-examples) | Usage examples of the "Commons Math" library. Codes in this module and its sub-modules are not part of the library's API; they can be updated or removed at any time. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/team.html -->

<!-- page_index: 28 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/scm.html -->

<!-- page_index: 29 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/ci-management.html -->

<!-- page_index: 30 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math-docs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-docs/index.html -->

<!-- page_index: 31 -->

<a id="commons-math-docs--commons-math:-the-apache-commons-mathematics-library"></a>

## Commons Math: The Apache Commons Mathematics Library

Commons Math is a library of lightweight, self-contained
mathematics and statistics components addressing the most common
problems not available in the Java programming language or Commons
Lang.

Browse the [Javadoc](https://commons.apache.org/proper/commons-math/commons-math-docs/apidocs/index.html) for more information.

---

<a id="commons-math-docs-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-docs/ci-management.html -->

<!-- page_index: 32 -->

<a id="commons-math-docs-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math-docs-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math-docs-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math-docs-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-docs/scm.html -->

<!-- page_index: 33 -->

<a id="commons-math-docs-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math-docs-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math-docs
```

<a id="commons-math-docs-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math-docs-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math-docs-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math-docs-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-docs/summary.html -->

<!-- page_index: 34 -->

<a id="commons-math-docs-summary--project-summary"></a>

## Project Summary

<a id="commons-math-docs-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Math Documentation |
| Description | Aggregator module to genenerate Apache Commons Math documentation. |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math-docs/> |

<a id="commons-math-docs-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math-docs-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math-docs |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math-docs-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-docs/team.html -->

<!-- page_index: 35 -->

<a id="commons-math-docs-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math-docs-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math-docs-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math-examples-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-examples/ci-management.html -->

<!-- page_index: 36 -->

<a id="commons-math-examples-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math-examples-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math-examples-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math-examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-examples/index.html -->

<!-- page_index: 37 -->

<a id="commons-math-examples--about-example-applications"></a>

## About Example applications

Usage examples of the "Commons Math" library.
Codes in this module and its sub-modules are not part of the library's API;
they can be updated or removed at any time.

<a id="commons-math-examples--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [SOFM](https://commons.apache.org/proper/commons-math/commons-math-examples/examples-sofm/index.html) | Self-organized feature map (ANN) sample codes. |
| [K-Means](https://commons.apache.org/proper/commons-math/commons-math-examples/examples-kmeans/index.html) | K-Means++ clustering sample codes. |

---

<a id="commons-math-examples-modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-examples/modules.html -->

<!-- page_index: 38 -->

<a id="commons-math-examples-modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [SOFM](https://commons.apache.org/proper/commons-math/commons-math-examples/examples-sofm/index.html) | Self-organized feature map (ANN) sample codes. |
| [K-Means](https://commons.apache.org/proper/commons-math/commons-math-examples/examples-kmeans/index.html) | K-Means++ clustering sample codes. |

---

<a id="commons-math-examples-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-examples/scm.html -->

<!-- page_index: 39 -->

<a id="commons-math-examples-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math-examples-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math-examples
```

<a id="commons-math-examples-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math-examples-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math-examples-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math-examples-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-examples/summary.html -->

<!-- page_index: 40 -->

<a id="commons-math-examples-summary--project-summary"></a>

## Project Summary

<a id="commons-math-examples-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Example applications |
| Description | Usage examples of the "Commons Math" library. Codes in this module and its sub-modules are not part of the library's API; they can be updated or removed at any time. |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math-examples/> |

<a id="commons-math-examples-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math-examples-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math-examples |
| Version | 4.0-SNAPSHOT |
| Type | pom |

---

<a id="commons-math-examples-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math-examples/team.html -->

<!-- page_index: 41 -->

<a id="commons-math-examples-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math-examples-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math-examples-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math4-core-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-core/ci-management.html -->

<!-- page_index: 42 -->

<a id="commons-math4-core-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math4-core-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math4-core-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math4-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-core/index.html -->

<!-- page_index: 43 -->

<a id="commons-math4-core--about-miscellaneous-core-classes"></a>

## About Miscellaneous core classes

Alternate implementations of JDK's "Math" functions.

---

<a id="commons-math4-core-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-core/scm.html -->

<!-- page_index: 44 -->

<a id="commons-math4-core-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math4-core-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math4-core
```

<a id="commons-math4-core-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-core-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-core-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math4-core-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-core/summary.html -->

<!-- page_index: 45 -->

<a id="commons-math4-core-summary--project-summary"></a>

## Project Summary

<a id="commons-math4-core-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Miscellaneous core classes |
| Description | Alternate implementations of JDK's "Math" functions. |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math4-core/> |

<a id="commons-math4-core-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math4-core-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-core |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math4-core-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-core/team.html -->

<!-- page_index: 46 -->

<a id="commons-math4-core-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math4-core-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math4-core-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math4-legacy-core-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-core/ci-management.html -->

<!-- page_index: 47 -->

<a id="commons-math4-legacy-core-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math4-legacy-core-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math4-legacy-core-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math4-legacy-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-core/index.html -->

<!-- page_index: 48 -->

<a id="commons-math4-legacy-core--about-miscellaneous-core-classes-legacy"></a>

## About Miscellaneous core classes (Legacy)

Field, Dfp, ...

---

<a id="commons-math4-legacy-core-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-core/scm.html -->

<!-- page_index: 49 -->

<a id="commons-math4-legacy-core-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math4-legacy-core-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math4-legacy-core
```

<a id="commons-math4-legacy-core-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-legacy-core-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-legacy-core-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math4-legacy-core-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-core/summary.html -->

<!-- page_index: 50 -->

<a id="commons-math4-legacy-core-summary--project-summary"></a>

## Project Summary

<a id="commons-math4-legacy-core-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Miscellaneous core classes (Legacy) |
| Description | Field, Dfp, ... |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math4-legacy-core/> |

<a id="commons-math4-legacy-core-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math4-legacy-core-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-legacy-core |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math4-legacy-core-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-core/team.html -->

<!-- page_index: 51 -->

<a id="commons-math4-legacy-core-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math4-legacy-core-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math4-legacy-core-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math4-legacy-exception-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-exception/ci-management.html -->

<!-- page_index: 52 -->

<a id="commons-math4-legacy-exception-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math4-legacy-exception-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math4-legacy-exception-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math4-legacy-exception"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-exception/index.html -->

<!-- page_index: 53 -->

<a id="commons-math4-legacy-exception--about-exception-classes-legacy"></a>

## About Exception classes (Legacy)

Exception classes used by code in "legacy" modules.

---

<a id="commons-math4-legacy-exception-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-exception/scm.html -->

<!-- page_index: 54 -->

<a id="commons-math4-legacy-exception-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math4-legacy-exception-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math4-legacy-exception
```

<a id="commons-math4-legacy-exception-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-legacy-exception-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-legacy-exception-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math4-legacy-exception-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-exception/summary.html -->

<!-- page_index: 55 -->

<a id="commons-math4-legacy-exception-summary--project-summary"></a>

## Project Summary

<a id="commons-math4-legacy-exception-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Exception classes (Legacy) |
| Description | Exception classes used by code in "legacy" modules. |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math4-legacy-exception/> |

<a id="commons-math4-legacy-exception-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math4-legacy-exception-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-legacy-exception |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math4-legacy-exception-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy-exception/team.html -->

<!-- page_index: 56 -->

<a id="commons-math4-legacy-exception-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math4-legacy-exception-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math4-legacy-exception-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math4-legacy-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy/ci-management.html -->

<!-- page_index: 57 -->

<a id="commons-math4-legacy-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math4-legacy-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math4-legacy-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math4-legacy"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy/index.html -->

<!-- page_index: 58 -->

<a id="commons-math4-legacy--about-apache-commons-math-legacy"></a>

## About Apache Commons Math (Legacy)

Codes that are either currently unsupported or not yet modularized.

---

<a id="commons-math4-legacy-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy/scm.html -->

<!-- page_index: 59 -->

<a id="commons-math4-legacy-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math4-legacy-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math4-legacy
```

<a id="commons-math4-legacy-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-legacy-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-legacy-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math4-legacy-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy/summary.html -->

<!-- page_index: 60 -->

<a id="commons-math4-legacy-summary--project-summary"></a>

## Project Summary

<a id="commons-math4-legacy-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Math (Legacy) |
| Description | Codes that are either currently unsupported or not yet modularized. |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math4-legacy/> |

<a id="commons-math4-legacy-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math4-legacy-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-legacy |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math4-legacy-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-legacy/team.html -->

<!-- page_index: 61 -->

<a id="commons-math4-legacy-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math4-legacy-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math4-legacy-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math4-neuralnet-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-neuralnet/ci-management.html -->

<!-- page_index: 62 -->

<a id="commons-math4-neuralnet-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math4-neuralnet-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math4-neuralnet-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math4-neuralnet"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-neuralnet/index.html -->

<!-- page_index: 63 -->

<a id="commons-math4-neuralnet--about-artificial-neural-networks"></a>

## About Artificial neural networks

Artificial neural networks: Self-organizing feature map (SOFM).

---

<a id="commons-math4-neuralnet-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-neuralnet/scm.html -->

<!-- page_index: 64 -->

<a id="commons-math4-neuralnet-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math4-neuralnet-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math4-neuralnet
```

<a id="commons-math4-neuralnet-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-neuralnet-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-neuralnet-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math4-neuralnet-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-neuralnet/summary.html -->

<!-- page_index: 65 -->

<a id="commons-math4-neuralnet-summary--project-summary"></a>

## Project Summary

<a id="commons-math4-neuralnet-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Artificial neural networks |
| Description | Artificial neural networks: Self-organizing feature map (SOFM). |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math4-neuralnet/> |

<a id="commons-math4-neuralnet-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math4-neuralnet-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-neuralnet |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math4-neuralnet-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-neuralnet/team.html -->

<!-- page_index: 66 -->

<a id="commons-math4-neuralnet-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math4-neuralnet-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math4-neuralnet-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---

<a id="commons-math4-transform-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-transform/ci-management.html -->

<!-- page_index: 67 -->

<a id="commons-math4-transform-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-math4-transform-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-math/actions
```

<a id="commons-math4-transform-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-math4-transform"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-transform/index.html -->

<!-- page_index: 68 -->

<a id="commons-math4-transform--about-transforms"></a>

## About Transforms

Fourier, Sine, Cosine, Hadamard.

---

<a id="commons-math4-transform-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-transform/scm.html -->

<!-- page_index: 69 -->

<a id="commons-math4-transform-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-math4-transform-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-math.git/commons-math4-transform
```

<a id="commons-math4-transform-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-transform-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-math.git
```

<a id="commons-math4-transform-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-math4-transform-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-transform/summary.html -->

<!-- page_index: 70 -->

<a id="commons-math4-transform-summary--project-summary"></a>

## Project Summary

<a id="commons-math4-transform-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Transforms |
| Description | Fourier, Sine, Cosine, Hadamard. |
| Homepage | <http://commons.apache.org/proper/commons-math/commons-math4-transform/> |

<a id="commons-math4-transform-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-math4-transform-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-math4-transform |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-math4-transform-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-math/commons-math4-transform/team.html -->

<!-- page_index: 71 -->

<a id="commons-math4-transform-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-math4-transform-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email |
| --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/7270d560c39b7631fafe7218e8437b78?d=mm&s=60) | mikl | Mikkel Meyer Andersen | [mikl at apache dot org](mailto:mikl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9c235adbb0d7523454c3ce744a2d5b65?d=mm&s=60) | billbarker | Bill Barker | [billbarker at apache dot org](mailto:billbarker at apache dot org) |
| ![](http://www.gravatar.com/avatar/9e962672e3b1e70c9a74ae245281362a?d=mm&s=60) | celestin | Sébastien Brisard | [celestin at apache dot org](mailto:celestin at apache dot org) |
| ![](http://www.gravatar.com/avatar/7394df2d4502ea57c8937c4d8602e892?d=mm&s=60) | achou | Albert Davidson Chou | [achou at apache dot org](mailto:achou at apache dot org) |
| ![](http://www.gravatar.com/avatar/5c6822036e9ffbc8e76a575f7608bba2?d=mm&s=60) | mdiggory | Mark Diggory | [mdiggory at apache dot org](mailto:mdiggory at apache dot org) |
| ![](http://www.gravatar.com/avatar/c69faab236d9abab3516c8ff37f74c50?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin at apache dot org](mailto:rdonkin at apache dot org) |
| ![](http://www.gravatar.com/avatar/b028907f95ce37c7a93a242dfd9ad5b9?d=mm&s=60) | oertl | Otmar Ertl | [oertl at apache dot org](mailto:oertl at apache dot org) |
| ![](http://www.gravatar.com/avatar/9d0d4ef4fa836e96ac1e72879a287901?d=mm&s=60) | luc | Luc Maisonobe | [luc at apache dot org](mailto:luc at apache dot org) |
| ![](http://www.gravatar.com/avatar/cd01a2f80eb3c08db03d6d3fd35ba8e2?d=mm&s=60) | tobrien | Tim O'Brien | [tobrien at apache dot org](mailto:tobrien at apache dot org) |
| ![](http://www.gravatar.com/avatar/0921b2aae09be8223e588ff2b821531d?d=mm&s=60) | pietsch | J. Pietschmann | [j3322ptm at yahoo dot de](mailto:j3322ptm at yahoo dot de) |
| ![](http://www.gravatar.com/avatar/0430706732e8d26f954fe38fc3983c0f?d=mm&s=60) | dimpbx | Dimitri Pourbaix | [dimpbx at apache dot org](mailto:dimpbx at apache dot org) |
| ![](http://www.gravatar.com/avatar/f668657e0a1300c5f94973881041ebd2?d=mm&s=60) | erans | Gilles Sadowski | [erans at apache dot org](mailto:erans at apache dot org) |
| ![](http://www.gravatar.com/avatar/8c829113cc67a1d81693ecf62d42576e?d=mm&s=60) | gregs | Greg Sterijevski | [gregs at apache dot org](mailto:gregs at apache dot org) |
| ![](http://www.gravatar.com/avatar/69b077c0c6a80a3797d58b374b61d2b0?d=mm&s=60) | brentworden | Brent Worden | [brentworden at apache dot org](mailto:brentworden at apache dot org) |
| ![](http://www.gravatar.com/avatar/644e4857b38eb565d1d32c04f93d2ca2?d=mm&s=60) | evanward | Evan Ward | [evanward at apache dot org](mailto:evanward at apache dot org) |
| ![](http://www.gravatar.com/avatar/98df4324ce33df916eba7dbf922a8750?d=mm&s=60) | chtompki | Rob Tompkins | [chtompki at apache dot org](mailto:chtompki at apache dot org) |
| ![](http://www.gravatar.com/avatar/dfc7f83290370f941a7b5f219b00b306?d=mm&s=60) | ericbarnhill | Eric Barnhill | [ericbarnhill at apache dot org](mailto:ericbarnhill at apache dot org) |
| ![](http://www.gravatar.com/avatar/e99e5789b5439720d66a54d0facd566c?d=mm&s=60) | aherbert | Alex Herbert | [aherbert at apache dot org](mailto:aherbert at apache dot org) |

<a id="commons-math4-transform-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Eldar Agalarov

Tim Allison

C. Scott Ananian

Mark Anderson

Peter Andrews

Rémi Arntzen

Matt Adereth

Jared Becksfort

Michael Bjorkegren

Brian Bloniarz

John Bollinger

Cyril Briquet

Dave Brosius

Dan Checkoway

Anders Conbere

Charles Cooper

Paul Cowan

Benjamin Croizet

Larry Diamond

Aleksei Dievskii

Rodrigo di Lorenzo Lopes

Hasan Diwan

Ted Dunning

Ole Ersoy

Ajo Fod

John Gant

Ken Geis

Hank Grabowski

Bernhard Grünewaldt

Elliotte Rusty Harold

Dennis Hendriks

Reid Hochstedler

Matthias Hummel

Curtis Jensen

Bruce A Johnson

Ismael Juma

Eugene Kirpichov

Oleksandr Kornieiev

Piotr Kochanski

Sergei Lebedev

Bob MacCallum

Jake Mannix

Benjamin McCann

Patrick Meyer

J. Lewis Muir

Venkatesha Murthy

Thomas Neidhart

Christopher Nix

Fredrik Norin

Sean Owen

Sujit Pal

Todd C. Parnell

Qualtagh

Andreas Rieger

Sébastien Riou

Karl Richter

Benedikt Ritter

Bill Rossi

Matthew Rowles

Pavel Ryzhov

Joni Salonen

Michael Saunders

Thorsten Schaefer

Christopher Schuck

Christian Semrau

David Stefka

Mauro Talevi

Radoslav Tsvetkov

Kim van der Linde

Alexey Volkov

Andrew Waterman

Jörg Weimar

Christian Winter

Piotr Wydrych

Xiaogang Zhang

Chris Popp

Artavazd Balaian

Samy Badjoudj

---
