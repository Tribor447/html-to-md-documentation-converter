# Project Information

## Navigation

- Commons Logging
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [User Guide](#guide)
  - [Troubleshooting Guide](#troubleshooting)
  - [Building](#building)
  - [Proposal](#proposal)
  - [Tech Guide](#tech)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/index.html -->

<!-- page_index: 1 -->

<a id="index--the-logging-component"></a>

# The Logging Component

When writing a library it is very useful to log information. However there
are many logging implementations out there, and a library cannot impose the use
of a particular one on the overall application that the library is a part of.

The Logging package is an ultra-thin bridge between different logging
implementations. A library that uses the commons-logging API can be used with
any logging implementation at runtime. Commons Logging comes with support for a
number of popular logging implementations, and writing adapters for others is a
reasonably simple task.

Applications (rather than libraries) may also choose to use commons-logging.
While logging-implementation independence is not as important for applications
as it is for libraries, using commons-logging does allow the application to
change to a different logging implementation without recompiling code.

Note that commons-logging does not attempt to initialize or terminate the underlying
logging implementation that is used at runtime; that is the responsibility of
the application. However many popular logging implementations do automatically
initialize themselves; in this case an application may be able to avoid
containing any code that is specific to the logging implementation used.

<a id="index--documentation"></a>

# Documentation

The [Release Notes](assets/files/release-notes_a5814c76063abfd7.txt) document the new features and bug fixes that have been
included in the latest release.

The [Javadoc API documents](https://commons.apache.org/proper/commons-logging/https/commons.apache.org/logging/apidocs/index.html) for the latest release are available online.
In particular, you should read the package overview of the `org.apache.commons.logging`
package. In addition, there is a (short)
[User Guide](#guide).

The [Wiki site](https://commons.apache.org/proper/commons-logging/https/wiki.apache.org/commons/Logging) has
the latest updates, an FAQ, and much other useful information.

Users needing to become experts or wanting to help develop JCL should
(in addition) consult the [Tech Guide](#tech).
This gives short introductions to topics such as advanced class loading.

<a id="index--releases"></a>

# Releases

Binary and source distributions are available
[here](https://commons.apache.org/proper/commons-logging/https/commons.apache.org/proper/commons-logging/download_logging.cgi).

The full release history is [here](https://commons.apache.org/proper/commons-logging/changes.html).

<a id="index--release-1.3.x"></a>

## Release 1.3.x

See [change-report](https://commons.apache.org/proper/commons-logging/changes.html).

<a id="index--release-1.2-july-2014"></a>

## Release 1.2 - July 2014

The main purpose of the 1.2 release is to drop support for Java 1.1.

For a full list of changes since the 1.1.3 release, please refer to the
[change-report](https://commons.apache.org/proper/commons-logging/changes.html).

<a id="index--release-1.1.3-may-2013"></a>

## Release 1.1.3 - May 2013

The 1.1.3 release only updates the Bundle-SymbolicName in the manifest
to "org.apache.commons.logging".

For a full list of changes since the 1.1.1 release, please refer to the
[change-report](https://commons.apache.org/proper/commons-logging/changes.html).

<a id="index--release-1.1.2-march-2013"></a>

## Release 1.1.2 - March 2013

The 1.1.2 release is a packaging of bug fixes since release 1.1.1.

For the full details, see the release notes for this version.

<a id="index--release-1.1.1-november-2007"></a>

## Release 1.1.1 - November 2007

This release is a minor update to the 1.1 release that fixes a number of bugs, and
resolves packaging issues for maven 1.x and maven 2.x users.

For the full details, see the release notes for this version.

<a id="index--release-1.1-10-may-2006"></a>

## Release 1.1 - 10 May 2006

This release makes several changes that are intended to resolve issues that
have been encountered when using commons-logging in servlet containers or j2ee
containers where complex classpaths are present and multiple copies of
commons-logging libraries are present at different levels.

This release also adds support for the TRACE level added to Log4j in the
1.2.12 release. In former commons-logging versions, the log.trace method
caused Log4j to output the message at the DEBUG level (the lowest level
supported by Log4j at that time).

For the full details, see the release notes for this version.

<a id="index--release-1.0.5-alpha"></a>

## Release 1.0.5 (Alpha)

**Note:** the 1.0.5 release was abandoned at alpha status.

The next JCL release will be designated 1.1 since we feel this more
accurately reflects the improvements made to the codebase.

<a id="index--release-1.0.4-16-jun-2004"></a>

## Release 1.0.4 - 16 Jun 2004

The 1.0.4 release of commons-logging is a service release containing support
for both the 1.2.x and 1.3.x series of Log4J releases.

<a id="index--release-1.0.3-7-apr-2003"></a>

## Release 1.0.3 - 7 Apr 2003

The 1.0.3 release is primarily a maintenance and code cleanup release with minimal new features.

<a id="index--release-1.0.2-27-september-2002"></a>

## Release 1.0.2 - 27 September 2002

The 1.0.2 release is a packaging of bug fixes since release 1.0.1.

<a id="index--release-1.0.1-13-august-2002"></a>

## Release 1.0.1 - 13 August 2002

The 1.0.1 release is a packaging of bug fixes and minor enhancements since release 1.0.

<a id="index--development-builds"></a>

# Development Builds

Regular builds of the current Git `master` branch code are made available in the
[snapshot repository](https://repository.apache.org/content/repositories/snapshots/). See the
[wiki](https://commons.apache.org/proper/commons-logging/https/wiki.apache.org/commons/Logging) for details.

Copyright © 2001-2026
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Logging, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-logging
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-logging
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-logging
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/security.html -->

<!-- page_index: 3 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-logging/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

None.

---

<a id="guide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/guide.html -->

<!-- page_index: 4 -->

<a id="guide--contents"></a>

# Contents

1. [Introduction](#guide--introduction)
2. [Quick Start](#guide--quick_start)
   1. [Configuration](#guide--configuration)
   2. [Configuring The Underlying Logging System](#guide--configuring_the_underlying_logging_system)
   3. [Configuring Log4J](#guide--configuring_log4j)
3. [Developing With JCL](#guide--developing_with_jcl)
   1. [Obtaining a Log Object](#guide--obtaining_a_log_object)
   2. [Logging a Message](#guide--logging_a_message)
   3. [Serialization Issues](#guide--serialization_issues)
4. [Jars Included in the Standard Distribution](#guide--jars_included_in_the_standard_distribution)
   1. [commons-logging.jar](#guide--commons-logging.jar)
   2. [commons-logging-api.jar](#guide--commons-logging-api.jar)
   3. [commons-logging-adapters.jar](#guide--commons-logging-adapters.jar)
5. [JCL Best Practices](#guide--jcl_best_practices)
6. [Best Practices (General)](#guide--best_practices_.28general.29)
   1. [Code Guards](#guide--code_guards)
   2. [Message Priorities/Levels](#guide--message_priorities.2flevels)
   3. [Default Message Priority/Level](#guide--default_message_priority.2flevel)
7. [Best Practices (Enterprise)](#guide--best_practices_.28enterprise.29)
   1. [Logging Exceptions](#guide--logging_exceptions)
   2. [When Info Level Instead of Debug?](#guide--when_info_level_instead_of_debug.3f)
   3. [More Control of Enterprise Exception Logging](#guide--more_control_of_enterprise_exception_logging)
   4. [National Language Support And Internationalization](#guide--national_language_support_and_internationalization)
   5. [Classloader and Memory Management](#guide--classloader_and_memory_management)
8. [Extending Commons Logging](#guide--extending_commons_logging)
   1. [Contract](#guide--contract)
   2. [Creating a Log Implementation](#guide--creating_a_log_implementation)
   3. [Creating A LogFactory Implementation](#guide--creating_a_logfactory_implementation)
9. [A Quick Guide To Simple Log](#guide--a.2520quick.2520guide.2520to.2520simple.2520log)
10. [Frequently Asked Questions](#guide--frequently_asked_questions)

<a id="guide--introduction"></a>

# Introduction

The Apache Commons Logging (JCL) provides a `Log` interface that
is intended to be both light-weight and an independent abstraction of other logging toolkits.
It provides the middleware/tooling developer with a simple
logging abstraction, that allows the user (application developer) to plug in
a specific logging implementation.

JCL provides thin-wrapper `Log` implementations for other logging APIs and backends, including
[Log4j API](https://logging.apache.org/log4j/2.x/manual/api-separation), [SLF4J](https://www.slf4j.org) and `java.util.logging`.

**Warning:** implementations for older logging backends such as
[Log4j 1.2](https://logging.apache.org/log4j/1.2/), [Avalon LogKit](https://avalon.apache.org), and
[Lumberjack](https://javalogging.sourceforge.net) are also provided, although they are disabled by default.

Familiarity with high-level details of the relevant Logging implementations is presumed.

<a id="guide--quick-start"></a>

# Quick Start

JCL tries to be as unobtrusive as possible.
In most cases, including the (full) `commons-logging.jar` in the classpath
should result in JCL configuring itself in a reasonable manner.
There's a good chance that it'll guess (discover) your preferred logging system, and you won't
need to do any configuration of JCL at all.

Note, however, that if you have a particular preference, then providing a simple
`commons-logging.properties` file which specifies the concrete logging library to be
used is recommended, since (in this case) JCL will log only to that system
and will report any configuration problems that prevent that system being used.

When no particular logging library is specified, then JCL will silently ignore any logging library
that it finds but cannot initialize and continue to look for other alternatives. This is a deliberate
design decision; no application should fail to run because a "guessed" logging library cannot be
used. To ensure an exception is reported when a particular logging library cannot be used, use one
of the available JCL configuration mechanisms to force that library to be selected (ie disable
JCL's discovery process).

<a id="guide--configuration"></a>

## Configuration

There are two base abstractions used by JCL: `Log`
(the basic logger) and `LogFactory` (which knows how to create `Log`
instances). Specifying a particular Log implementation is very useful (whether that is
one provided by Commons Logging or a user-defined one). Specifying a
`LogFactory` implementation explicitly is a subject for
advanced users only, so will not be addressed here.

JCL provides three standard log factories:

1. if [Log4j API](https://logging.apache.org/log4j/2.x/manual/api-separation)
   is present on the classpath and it is not redirected to SLF4J, then `Log4jApiLogFactory`
   is used. This factory redirects all output to Log4j API.
2. otherwise if [SLF4J](https://www.slf4j.org) is present on the classpath,
   then `Slf4jLogFactory` is used. This factory redirects all output to SLF4J.
3. otherwise the legacy `LogFactoryImpl` is used.

The legacy `LogFactory` implementation uses the following discovery process
to determine what type of `Log` implementation it should use
(the process terminates when the first positive match - in order - is found):

1. Look for a configuration attribute of this factory named
   `org.apache.commons.logging.Log` (for backwards compatibility with
   pre-1.0 versions of this API, an attribute
   `org.apache.commons.logging.log` is also consulted).

   Configuration attributes can be set explicitly by Java code, but they are more
   commonly set by placing a file named `commons-logging.properties` in the classpath.
   When such a file exists, every entry in the properties file becomes an "attribute"
   of the LogFactory. When there is more than one such file in the classpath, releases
   of commons-logging prior to 1.1 simply use the first one found. From release 1.1,
   each file may define a `priority` key, and the file with
   the highest priority is used (no priority definition implies priority of zero).
   When multiple files have the same priority, the first one found is used.

   Defining this property in a `commons-logging.properties` file is the recommended
   way of explicitly selecting a Log implementation.
2. Look for a system property named
   `org.apache.commons.logging.Log` (for backwards
   compatibility with pre-1.0 versions of this API, a system property
   `org.apache.commons.logging.log` is also consulted).
3. If the `java.logging` module is available, use
   the corresponding wrapper class
   ([Jdk14Logger](https://commons.apache.org/logging/apidocs/org/apache/commons/logging/impl/Jdk14Logger.html)).
4. Fall back to the default simple logging wrapper
   ([SimpleLog](https://commons.apache.org/logging/apidocs/org/apache/commons/logging/impl/SimpleLog.html)).

Consult the JCL javadocs for details of the various `Log`
implementations that ship with the component. (The discovery process is also covered in more
detail there.)

<a id="guide--configuring-the-underlying-logging-system"></a>

## Configuring The Underlying Logging System

The JCL SPI
can be configured to use different logging toolkits (see [above](#guide--configuration)).
JCL provides only a bridge for writing log messages. It does not (and will not) support any
sort of configuration API for the underlying logging system.

Configuration of the behavior of the JCL ultimately depends upon the
logging toolkit being used. Please consult the documentation for the chosen logging system.

JCL is NOT responsible for initialization, configuration, or shutdown of the underlying logging library.
In many cases logging libraries will automatically initialize/configure themselves when first used, and
need no explicit shutdown process. In these situations an application can simply use JCL and not depend
directly on the API of the underlying logging system in any way. However if the logging library being used
requires special initialization, configuration, or shutdown, then some logging-library-specific code will
be required in the application. JCL simply forwards logging method calls to the correct underlying
implementation. When writing library code this issue is of course not relevant as the calling application
is responsible for handling such issues.

<a id="guide--developing-with-jcl"></a>

# Developing With JCL

<a id="guide--obtaining-a-log-object"></a>

## Obtaining a Log Object

To use the JCL SPI from a Java class, include the following import statements:

`import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;`

Note that some components using JCL may
either extend Log, or provide a component-specific LogFactory implementation.
Review the component documentation for guidelines
on how commons-logging should be used in such components.

For each class definition, declare and initialize a
`log` attribute as follows:

```

public class CLASS
{
    private Log log = LogFactory.getLog(CLASS.class);
    ...
    ;
        
```

Note that for application code, declaring the log member as "static" is more
efficient as one Log object is created per class, and is recommended.
However this is not safe to do for a class which may be deployed via a "shared"
classloader in a servlet or j2ee container or similar environment. If the class
may end up invoked with different thread-context-classloader values set, then the
member must *not* be declared static. The use of "static" should therefore
be avoided in code within any "library" type project.

<a id="guide--logging-a-message"></a>

## Logging a Message

Messages are logged to a *logger*, such as `log`
by invoking a method corresponding to *priority*.
The `org.apache.commons.logging.Log` interface defines the
following methods for use
in writing log/trace messages to the log:

```

    log.fatal(Object message);
    log.fatal(Object message, Throwable t);
    log.error(Object message);
    log.error(Object message, Throwable t);
    log.warn(Object message);
    log.warn(Object message, Throwable t);
    log.info(Object message);
    log.info(Object message, Throwable t);
    log.debug(Object message);
    log.debug(Object message, Throwable t);
    log.trace(Object message);
    log.trace(Object message, Throwable t);
        
```

Semantics for these methods are such that it is expected
that the severity, from highest to lowest, of messages is ordered as above.

In addition to the logging methods, the following are provided for code guards:

```

    log.isFatalEnabled();
    log.isErrorEnabled();
    log.isWarnEnabled();
    log.isInfoEnabled();
    log.isDebugEnabled();
    log.isTraceEnabled();
        
```

<a id="guide--serialization-issues"></a>

## Serialization Issues

Prior to release 1.0.4, none of the standard Log implementations were
Serializable. If you are using such a release and have a Serializable class
with a member that is of type Log, then it is necessary to declare
that member to be transient and to ensure that the value is restored on
deserialization. The recommended approach is to define a custom
readObject method on the class which reinitializes that member.

In release 1.0.4, all standard Log implementations are Serializable. This
means that class members of type Log do *not* need to be declared transient;
on deserialization the Log object will "rebind" to the same category for the
same logging library. Note that the same underlying logging library will be
used on deserialization as was used in the original object, even if the
application the object was deserialized into is using a different logging
library. There is one exception; LogKitLogger (adapter for the Avalon LogKit
library) is not Serializable for technical reasons.

Custom Log implementations not distributed with commons-logging may
or may not be Serializable. If you wish your code to be compatible with
any arbitrary log adapter, then you should follow the advice given above
for pre-1.0.4 releases.

<a id="guide--jars-included-in-the-standard-distribution"></a>

# Jars Included in the Standard Distribution

<a id="guide--commons-logging.jar"></a>

## commons-logging.jar

The `commons-logging.jar` file includes the JCL API, the default
`LogFactory` implementation and thin-wrapper `Log`
implementations for
[Log4J](https://logging.apache.org/log4j/docs/index.html), [Avalon LogKit](https://avalon.apache.org/logkit/index.html), the Avalon Framework's logging infrastructure, java.util.logging, as well as an implementation of java.util.logging APIs (JSR-47) for
pre-1.4 systems.

In most cases, including `commons-logging.jar` and your preferred
logging implementation in the classpath should be all that is required to
use JCL.

<a id="guide--commons-logging-api.jar"></a>

## commons-logging-api.jar

The `commons-logging-api.jar` file includes the JCL API and the
default `LogFactory` implementation as well as the built-in
`Log` implementations SimpleLog and NoOpLog. However it does not
include the wrapper `Log` implementations that require additional
libraries such as `Log4j`, `Avalon` and
`Lumberjack`.

This jar is intended for use by projects that recompile the commons-logging
source using alternate java environments, and cannot compile against all of
the optional libraries that the Apache release of commons-logging supports.
Because of the reduced dependencies of this jarfile, such projects should be
able to create an equivalent of this library with fewer difficulties.

This jar is also useful for build environments that automatically track
dependencies, and thus have difficulty with the concept that the main
commons-logging.jar has "optional" dependencies on various logging
implementations that can safely go unsatisfied at runtime.

<a id="guide--commons-logging-adapters.jar"></a>

## commons-logging-adapters.jar

The `commons-logging-adapters.jar` file includes only adapters
to third-party logging implementations, and none of the core commons-logging
framework. As such, it cannot be used alone; either commons-logging.jar or
commons-logging-api.jar must also be present in the classpath.

This library will not often be used; it is only intended for situations where
a container has deployed commons-logging-api.jar in a shared classpath but a
webapp wants to bind logging to one of the external logging implementations
that the api jar does not include. In this situation, deploying the
commons-logging.jar file within the webapp can cause problems as this leads to
duplicates of the core commons-logging classes (Log, LogFactory, etc) in
the classpath which in turn can cause unpleasant ClassCastException exceptions
to occur. Deploying only the adapters avoids this problem.

<a id="guide--jcl-best-practices"></a>

# JCL Best Practices

Best practices for JCL are presented in two categories:
General and Enterprise.
The general principles are fairly clear.Enterprise practices are a bit more involved
and it is not always as clear as to why they are important.

Enterprise best practice principles apply to middleware components
and tooling that is expected to execute in an "Enterprise" level
environment.
These issues relate to Logging as Internationalization, and fault detection.
Enterprise requires more effort and planning, but are strongly encouraged (if not required)
in production level systems. Different corporate enterprises/environments have different
requirements, so being flexible always helps.

<a id="guide--best-practices-general"></a>

# Best Practices (General)

<a id="guide--code-guards"></a>

## Code Guards

Code guards are typically used to guard code that
only needs to execute in support of logging, that otherwise introduces undesirable runtime overhead
in the general case (logging disabled).
Examples are multiple parameters, or expressions (e.g. string + " more") for parameters.
Use the guard methods of the form `log.is<Priority>()` to verify
that logging should be performed, before incurring the overhead of the logging method call.
Yes, the logging methods will perform the same check, but only after resolving parameters.

<a id="guide--message-priorities-levels"></a>

## Message Priorities/Levels

It is important to ensure that log message are
appropriate in content and severity.
The following guidelines are suggested:

- **fatal** - Severe errors that cause premature termination.
  Expect these to be immediately visible on a status console.
  See also [Internationalization](#guide--national.2520language.2520support.2520and.2520internationalization).
- **error** - Other runtime errors or unexpected conditions.
  Expect these to be immediately visible on a status console.
  See also [Internationalization](#guide--national.2520language.2520support.2520and.2520internationalization).
- **warn** - Use of deprecated APIs, poor use of API, 'almost' errors,
  other runtime situations that are undesirable or unexpected, but not
  necessarily "wrong".
  Expect these to be immediately visible on a status console.
  See also [Internationalization](#guide--national.2520language.2520support.2520and.2520internationalization).
- **info** - Interesting runtime events (startup/shutdown).
  Expect these to be immediately visible on a console,
  so be conservative and keep to a minimum.
  See also [Internationalization](#guide--national.2520language.2520support.2520and.2520internationalization).
- **debug** - detailed information on the flow through the system.
  Expect these to be written to logs only.
- **trace** - more detailed information.
  Expect these to be written to logs only.

<a id="guide--default-message-priority-level"></a>

## Default Message Priority/Level

By default the message priority should be no lower than **info**.
That is, by default **debug** message should not be seen in the logs.

<a id="guide--best-practices-enterprise"></a>

# Best Practices (Enterprise)

<a id="guide--logging-exceptions"></a>

## Logging Exceptions

The general rule in dealing with exceptions is to assume that
the user (developer using a tooling/middleware API) isn't going
to follow the rules.
Since any problems that result are going to be assigned to you, it's in your best interest to be prepared with the proactive
tools necessary to demonstrate that your component works correctly, or at worst that the problem can be analyzed from your logs.
For this discussion, we must make a distinction between different types of exceptions
based on what kind of boundaries they cross:

- **External Boundaries - Expected Exceptions**.
  This classification includes exceptions such as `FileNotFoundException`
  that cross API/SPI boundaries, and are exposed to the user of a component/toolkit.
  These are listed in the 'throws' clause of a method signature.
  Appropriate handling of these exceptions depends upon the type
  of code you are developing.
  API's for utility functions and tools should log these at the **debug** level,
  if they are caught at all by internal code.
  For higher level frameworks and middleware components,
  these exceptions should be caught immediately prior to crossing
  the API/SPI interface back to user code-space,
  logged with full stack trace at **info** level,
  and rethrown.
  The assures that the log contains a record of the root cause for
  future analysis *in the event that the exception is not caught and resolved
  as expected by the user's code*.
- **External Boundaries - Unexpected Exceptions**.
  This classification includes exceptions such as `NullPointerException`
  that cross API/SPI boundaries, and are exposed to the user of a component/toolkit.
  These are runtime exceptions/error that are NOT
  listed in the 'throws' clause of a method signature.
  Appropriate handling of these exceptions depends upon the type
  of code you are developing.
  APIs for utility functions and tools should log these at the **debug** level,
  if they are caught at all.
  For higher level frameworks and middleware components,
  these exceptions should be caught immediately prior to crossing
  the API/SPI interface back to user code-space,
  logged with full stack trace at **info** level,
  and rethrown/wrapped as `ComponentInternalError`.
  This ensures that the log contains a record of the root cause for
  future analysis *in the event that the exception is not caught and
  logged/reported as expected by the user's code*.
- **Internal Boundaries**.
  Exceptions that occur internally and are resolved internally.
  These should be logged when caught as **debug** or **info** messages,
  at the programmer's discretion.
- **Significant Internal Boundaries**.
  This typically only applies to middleware components that span networks or runtime processes.
  Exceptions that cross over significant internal component boundaries such as networks
  should be logged when caught as **info** messages.
  Do not assume that such a (process/network) boundary will deliver exceptions to the 'other side'.

<a id="guide--when-info-level-instead-of-debug"></a>

## When Info Level Instead of Debug?

You want to have exception/problem information available for
first-pass problem determination in a production level
enterprise application without turning on **debug**
as a default log level. There is simply too much information
in **debug** to be appropriate for day-to-day operations.

<a id="guide--more-control-of-enterprise-exception-logging"></a>

## More Control of Enterprise Exception Logging

If more control is desired for the level of detail of these
'enterprise' exceptions, then consider creating a special
logger just for these exceptions:

```

   Log log = LogFactory.getLog("org.apache.component.enterprise");
```

This allows the 'enterprise' level information to be turned on/off explicitly
by most logger implementations.

<a id="guide--national-language-support-and-internationalization"></a>

## National Language Support And Internationalization

NLS internationalization involves looking up messages from
a message file by a message key, and using that message for logging.
There are various tools in Java, and provided by other components, for working with NLS messages.

NLS enabled components are particularly appreciated
(that's an open-source-correct term for 'required by corporate end-users' :-)
for **tooling** and **middleware** components.

NLS internationalization SHOULD be strongly considered for used for
**fatal**, **error**, **warn**, and **info** messages.
It is generally considered optional for **debug** and **trace** messages.

Perhaps more direct support for internationalizing log messages
can be introduced in a future or alternate version of the `Log` interface.

<a id="guide--classloader-and-memory-management"></a>

## Classloader and Memory Management

The `LogFactory` discovery process (see
[Configuration](#guide--configuration) above) is a fairly expensive
operation, so JCL certainly should not perform it each time user code
invokes:

```
LogFactory.getLog()
```

Instead JCL caches the
`LogFactory` implementation created as a result of the discovery
process and uses the cached factory to return `Log` objects.
Since in JEE and similar multi-classloader environments, the result of the
discovery process can vary depending on the thread context classloader
(e.g. one webapp in a web container may be configured to use Log4j and
another to use java.util.logging), JCL internally caches the
`LogFactory` instances in a static hashtable, keyed by classloader.

While this approach is efficient, it can lead to memory leaks if container
implementors are not careful to call

```
LogFactory.release()
```

whenever a classloader that has utilized JCL is undeployed. If
`release()` is not called, a reference to the undeployed
classloader (and thus to all the classes loaded by it) will be
held in `LogFactory`'s static hashtable.

`LogFactory` caches factory implementations in a
"WeakHashtable". This class is similar to `java.util.WeakHashMap` in
that it holds a `WeakReference` to each key (but a strong reference
to each value), thus allowing classloaders to be GC'd even if
`LogFactory.release()` is never invoked.

If a custom LogFactory implementation is used, however, then a
`WeakHashtable` alone can be insufficient to allow garbage collection
of a classloader without a call to `release`. If the abstract class
`LogFactory` is loaded by a parent classloader and a concrete
subclass implementation of `LogFactory` is loaded by a child
classloader, the WeakHashtable's key is a weak reference to the TCCL (child
classloader), but the value is a strong reference to the LogFactory instance, which in turn contains a strong reference to its class and thus loading
classloader - the child classloader. This chain of strong references prevents
the child loader from being garbage collected.

If use of a custom `LogFactory` subclass is desired, ensuring that
the custom subclass is loaded by the same classloader as `LogFactory`
will prevent problems. In normal deployments, the standard implementations
of `LogFactory` found in package `org.apache.commons.logging.impl`
will be loaded by the same classloader that loads `LogFactory`
itself, so use of the standard `LogFactory` implementation
should not pose problems. Alternatively, use the provided ServletContextCleaner
to ensure this reference is explicitly released on webapp unload.

<a id="guide--extending-commons-logging"></a>

# Extending Commons Logging

JCL is designed to encourage extensions to be created that add functionality.
Typically, extensions to JCL fall into two categories:

- new `Log` implementations that provide new bridges to logging systems
- new `LogFactory` implementations that provide alternative discovery strategies

<a id="guide--contract"></a>

## Contract

When creating new implementations for `Log` and `LogFactory`, it is important to understand the implied contract between the factory
and the log implementations:

- **Life cycle**
  > The JCL LogFactory implementation must assume responsibility for
  > either connecting/disconnecting to a logging toolkit,
  > or instantiating/initializing/destroying a logging toolkit.
- **Exception handling**
  > The JCL Log interface doesn't specify any exceptions to be handled,
  > the implementation must catch any exceptions.
- **Multiple threads**
  > The JCL Log and LogFactory implementations must ensure
  > that any synchronization required by the logging toolkit
  > is met.

<a id="guide--creating-a-log-implementation"></a>

## Creating a Log Implementation

The minimum requirement to integrate with another logger
is to provide an implementation of the
`org.apache.commons.logging.Log` interface.
In addition, an implementation of the
`org.apache.commons.logging.LogFactory` interface
can be provided to meet
specific requirements for connecting to, or instantiating, a logger.

The default `LogFactory` provided by JCL
can be configured to instantiate a specific implementation of the
`org.apache.commons.logging.Log` interface
by setting the property of the same name (`org.apache.commons.logging.Log`).
This property can be specified as a system property, or in the `commons-logging.properties` file, which must exist in the CLASSPATH.

<a id="guide--creating-a-logfactory-implementation"></a>

## Creating A LogFactory Implementation

If desired, the default implementation of the
`org.apache.commons.logging.LogFactory`
interface can be overridden, allowing the JDK 1.3 Service Provider discovery process
to locate and create a LogFactory specific to the needs of the application.
Review the Javadoc for the `LogFactoryImpl.java`
for details.

<a id="guide--a-quick-guide-to-simple-log"></a>

# A Quick Guide To Simple Log

JCL is distributed with a very simple `Log` implementation named
`org.apache.commons.logging.impl.SimpleLog`. This is intended to be a minimal
implementation. Developers requiring a fully functional open source logging system are
directed to [Log4J](https://logging.apache.org/log4j).

`SimpleLog` sends all (enabled) log messages, for all defined loggers, to `System.err`. The following system properties
are supported to configure the behavior of this logger:

- **org.apache.commons.logging.simplelog.defaultlog** -
  Default logging detail level for all instances of SimpleLog.
  Must be one of:
  - `trace`
  - `debug`
  - `info`
  - `warn`
  - `error`
  - `fatal`If not specified, defaults to `info`.
- **org.apache.commons.logging.simplelog.log.xxxxx** -
  Logging detail level for a SimpleLog instance named "xxxxx".
  Must be one of:
  - `trace`
  - `debug`
  - `info`
  - `warn`
  - `error`
  - `fatal`If not specified, the default logging detail level is used.
- **org.apache.commons.logging.simplelog.showlogname** -
  Set to `true` if you want the `Log` instance name to be
  included in output messages. Defaults to `false`.
- **org.apache.commons.logging.simplelog.showShortLogname** -
  Set to `true` if you want the last component of the name to be
  included in output messages. Defaults to `true`.
- **org.apache.commons.logging.simplelog.showdatetime** -
  Set to `true` if you want the current date and time
  to be included in output messages. Default is `false`.
- **org.apache.commons.logging.simplelog.dateTimeFormat** -
  The date and time format to be used in the output messages.
  The pattern describing the date and time format is the same that is
  used in `java.text.SimpleDateFormat`. If the format is not
  specified or is invalid, the default format is used.
  The default format is `yyyy/MM/dd HH:mm:ss:SSS zzz`.

In addition to looking for system properties with the names specified
above, this implementation also checks for a class loader resource named
`"simplelog.properties"`, and includes any matching definitions
from this resource (if it exists).

<a id="guide--frequently-asked-questions"></a>

# Frequently Asked Questions

See the [FAQ document](https://cwiki.apache.org/confluence/display/COMMONS/Logging+FrequentlyAskedQuestions)
on the commons-logging wiki site

---

<a id="troubleshooting"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/troubleshooting.html -->

<!-- page_index: 5 -->

<a id="troubleshooting--contents"></a>

# Contents

- [Contents](#troubleshooting--contents)
- [Using JCL Diagnostics](#troubleshooting--using_jcl_diagnostics)
  - [When To Use Diagnostic Logging](#troubleshooting--when_to_use_diagnostic_logging)
  - [How To Use Diagnostic logging](#troubleshooting--how_to_use_diagnostic_logging)
  - [OIDs](#troubleshooting--oids)
  - [Diagnostic Message Prefix](#troubleshooting--diagnostic_message_prefix)
  - [ClassLoader Hierarchy Tree](#troubleshooting--classloader_hierarchy_tree)
  - [LogFactory Class Bootstrap](#troubleshooting--logfactory_class_bootstrap)
  - [Construction Of LogFactoryImpl Instances](#troubleshooting--construction_of_logfactoryimpl_instances)
  - [Log Discovery Diagnostics](#troubleshooting--log_discovery_diagnostics)
- [Containers With Custom LogFactory Implementations](#troubleshooting--containers_with_custom_logfactory_implementations)
  - [The Incompatible LogFactory Issue](#troubleshooting--the_incompatible_logfactory_issue)
    - [Symptoms](#troubleshooting--symptoms)
    - [Explanation](#troubleshooting--explanation)
    - [Fixes](#troubleshooting--fixes)
- [Containers With Custom ClassLoading Behaviour for Logging](#troubleshooting--containers_with_custom_classloading_behaviour_for_logging)
  - [Apache Tomcat](#troubleshooting--apache_tomcat)
  - [JBoss Application Server](#troubleshooting--jboss_application_server)
  - [Other Containers](#troubleshooting--other_containers)

<a id="troubleshooting--using-jcl-diagnostics"></a>

# Using JCL Diagnostics

Diagnostics is a feature introduced in JCL 1.1 as an aid to debugging problems
with JCL configurations. When diagnostics are switched on, messages are logged
to a stream (specified by the user) by the two main classes involved in discovery
in JCL (`LogFactory` and `LogFactoryImpl`).

Diagnostics are intended to be used in conjunction with the source. The source
contains numerous and lengthy comments. Often these are intended to help explain
the meaning of the messages.

<a id="troubleshooting--when-to-use-diagnostic-logging"></a>

## When To Use Diagnostic Logging

Diagnostic logging is intended only to be used when debugging a problematic
configuration. It *should* be switched off for production.

<a id="troubleshooting--how-to-use-diagnostic-logging"></a>

## How To Use Diagnostic logging

Diagnostic logging is controlled through the system property
`org.apache.commons.logging.diagnostics.dest`. Setting the property value
to the special strings `STDOUT` or `STDERR` (case-sensitive)
will output messages to `System.out` and `System.err` respectively.
Setting the property value to a valid file name will result in the messages being logged
to that file.

<a id="troubleshooting--oids"></a>

## OIDs

Diagnostics uses the concept of an Object ID (OID). This allows the identity of objects
to be tracked without relying on useful `toString` implementations.
These are of the form:

`classname@system identity hash code`

The *system identity hash code* is found by calling `System.identityHashCode()`
which should uniquely identify a particular instance. The classname is usually the fully qualified
class name though in a few cases, `org.apache.commons.logging.impl.LogFactoryImpl` may be
shortened to `LogFactoryImpl` to increase ease of reading. For example:

`sun.misc.Launcher$AppClassLoader@20120943
LogFactoryImpl@1671711`

OIDs are intended to be used to cross-reference. They allow particular instances of classloaders
and JCL classes to be tracked in different contexts. This plays a vital role in building
up the understanding of the classloader environment required to diagnose JCL problems.

<a id="troubleshooting--diagnostic-message-prefix"></a>

## Diagnostic Message Prefix

Each diagnostic message is prefixed with details of the relevant class in a standard format.
This takes the form:

`[class-identifier from ClassLoader OID]`

*ClassLoader OID* is the [OID](#troubleshooting--oids) of a classloader which loaded
the class issuing the message.
*class-identifier* identifies the object issuing the message.

In the case of
`LogFactory`, this is just `LogFactory`. For example (line split):

`[LogFactory
from sun.misc.Launcher$AppClassLoader@20120943] BOOTSTRAP COMPLETED`

In the case of
`LogFactoryImpl`, the prefix is the instance OID. This can be cross referenced
to discover the details of the TCCL used to manage this instance. For example (line split):

`[LogFactoryImpl@1671711
from sun.misc.Launcher$AppClassLoader@20120943] Instance created.`

<a id="troubleshooting--classloader-hierarchy-tree"></a>

## ClassLoader Hierarchy Tree

Understanding the relationships between classloaders is vital when debugging JCL.
At various points, JCL will print to the diagnostic log the hierarchy for important
classloaders. This is obtained by walking the tree using `getParent`.
Each classloader is represented (visually) by an OID (to allow cross referencing)
and the relationship indicated in `child --> parent` fashion.
For example (line split for easy reading):

`ClassLoader tree:java.net.URLClassLoader@3526198
--> sun.misc.Launcher$AppClassLoader@20120943 (SYSTEM)
--> sun.misc.Launcher$ExtClassLoader@11126876
--> BOOT`

Represents a hierarchy with four elements ending in the boot classloader.

<a id="troubleshooting--logfactory-class-bootstrap"></a>

## LogFactory Class Bootstrap

Whenever the `LogFactory` class is initialized, diagnostic messages about
the classloader environment are logged. The content of each of these messages is prefixed by
`[ENV]` to help distinguish them. The extension directories, application classpath, details of the classloader (including the [OID](#troubleshooting--oids) and `toString`
value) used to load `LogFactory` and the
[classloader tree](#troubleshooting--classloader.2520hierarchy.2520tree) for that classloader
are logged.

Many Sun classloaders have confusing `toString` values. For example, the OID may be

`sun.misc.Launcher$AppClassLoader@20120943`

with a `toString` value of

`sun.misc.Launcher$AppClassLoader@133056f`

Other classloader implementations may give very useful information (such as the local classpath).

Finally, once initialization is complete a `BOOTSTRAP COMPLETED` message is issued.

<a id="troubleshooting--construction-of-logfactoryimpl-instances"></a>

## Construction Of LogFactoryImpl Instances

`LogFactoryImpl` is the standard and default `LogFactory` implementation.
This section obviously only applies to configurations using this implementation.

Before assigning a `Log` instance, `LogFactory` loads a
`LogFactory` implementation. The content is prefixed by `[LOOKUP]`
for each diagnostic message logged by this process.

The implementation used can vary per Thread context classloader (TCCL). If this is the first time
that a Log has been requested for a particular TCCL a new instance will be created.

Information of particular interest is logged at this stage. Details of the TCCL are logged
allowing the [OID](#troubleshooting--oids) later to be cross-referenced to the `toString` value
and the [classloader tree](#troubleshooting--classloader.2520hierarchy.2520tree). For example, the
following log snippet details the TCCL (lines split):

`[LogFactory from sun.misc.Launcher$AppClassLoader@20120943]
[LOOKUP] LogFactory implementation requested for the first time for context
classloader java.net.URLClassLoader@3526198
[LogFactory from sun.misc.Launcher$AppClassLoader@20120943]
[LOOKUP] java.net.URLClassLoader@3526198 == 'java.net.URLClassLoader@35ce36'
[LogFactory from sun.misc.Launcher$AppClassLoader@20120943]
[LOOKUP] ClassLoader tree:java.net.URLClassLoader@3526198
--> sun.misc.Launcher$AppClassLoader@20120943 (SYSTEM)
--> sun.misc.Launcher$ExtClassLoader@11126876
--> BOOT`

<a id="troubleshooting--log-discovery-diagnostics"></a>

## Log Discovery Diagnostics

The standard `LogFactoryImpl` issues many diagnostic messages when discovering
the `Log` implementation to be used.

During discovery, environment variables are loaded and values set. This content is prefixed by
`[ENV]` to make it easier to distinguish this material.

The possible messages issued during discovery are numerous. To understand them, the source
should be consulted. Attention should be paid to the classloader hierarchy trees for the
classloader used to load `LogFactory` and to the TCCL.

<a id="troubleshooting--containers-with-custom-logfactory-implementations"></a>

# Containers With Custom LogFactory Implementations

Some containers use a custom `LogFactory` implementation to adapt JCL to their particular
logging system. This has some important consequences for the deployment of applications using JCL within
these containers.

Containers known to use this mechanism:

- [WebSphere Application Server](https://commons.apache.org/proper/commons-logging/https/www.ibm.com/software/websphere/) from
  [IBM](https://commons.apache.org/proper/commons-logging/https/www.ibm.com/software/websphere/) (versions 5 and 6).

Containers suspected to use this mechanism:

- WebSphere Application Server (other versions).

The Apache Commons team would be grateful if reports were posted to the development list
of other containers using a custom implementation.

<a id="troubleshooting--the-incompatible-logfactory-issue"></a>

## The Incompatible LogFactory Issue

<a id="troubleshooting--symptoms"></a>

#### Symptoms

An exception is thrown by JCL with a message similar to:

`The chosen LogFactory implementation does not extend LogFactory. Please check your configuration.
(Caused by java.lang.ClassCastException: The application has specified that a custom LogFactory
implementation should be used but Class 'com.ibm.ws.commons.logging.TrLogFactory' cannot be converted
to 'org.apache.commons.logging.LogFactory'. The conflict is caused by the presence of multiple
LogFactory classes in incompatible classloaders. Background can be found in
https//commons.apache.org/logging/tech.html. If you have not explicitly specified a custom
LogFactory then it is likely that the container has set one without your knowledge.
In this case, consider using the commons-logging-adapters.jar file or specifying the standard
LogFactory from the command line. Help can be found @https//commons.apache.org/logging.`

This is a WebSphere example so the name of the custom LogFactory is
`com.ibm.ws.commons.logging.TrLogFactory`. For other containers, this class name will
differ.

<a id="troubleshooting--explanation"></a>

#### Explanation

A custom `LogFactory` implementation can only be used if the implementation class loaded
dynamically at runtime can be cast to the `LogFactory` class that loaded it. There are
several ways in which this cast can fail. The most obvious is that the source code may not actually
extend `LogFactory`. The source may be compatible but if the `LogFactory` class
against which the source is compiled is not binary compatible then the cast will also fail.

There is also another more unusual way in which this cast can fail: even when the binary is compatible, the implementation class loaded at runtime may be linked to a different instance of the
`LogFactory` class. For more information, see the [tech guide](#tech).

This situation may be encountered in containers which use a custom `LogFactory` implementation.
The implementation will typically be provided in a shared, high level classloader together with JCL.
When an application classloader contains `LogFactory`, the implementation will be loaded
from that higher level classloader. The implementation class will be linked to the `LogFactory`
class loaded by the higher level classloader. Even if the
`LogFactory` implementations are binary compatible, since they are loaded by different classloaders
the two `LogFactory` Class instances are not equal and so the cast must fail.

The policy adopted by JCL in this situation is to re-throw this exception. Additional information
is included in the message to help diagnosis. The reasoning behind this choice is that a
particular `LogFactory` implementation has been actively specified and this
choice should not be ignored. This policy has unfortunate consequences when running in
containers which have custom implementations: the above runtime exception may be thrown
under certain classloading policies without the user knowingly specifying a custom
implementation.

<a id="troubleshooting--fixes"></a>

#### Fixes

There are various ways to fix this problem. Which fix is right depends on the circumstances.

If you are happy using another classloading policy for the application, select a
classloading policy which ensures that `LogFactory` will be loaded from the
shared classloader containing the custom implementation.

If you want to bypass the container adaption mechanism then set the appropriate system property
to the default value when the container is started:

`-Dorg.apache.commons.logging.LogFactory=org.apache.commons.logging.impl.LogFactoryImpl`

If you want to continue to use the default container mechanism then:

- Find and replace the commons-logging implementation used by the container with
  the most modern release
- Replace the commons-logging jar in the application with the commons-logging-adapters jar.
  This will ensure that application classloader will delegate to it's parent when loading
  `LogFactory`.

If you encounter difficulties when applying the fixes recommended, please turn on
[diagnostics](#troubleshooting--using_jcl_diagnostics) and consult the logs.

<a id="troubleshooting--containers-with-custom-classloading-behaviour-for-logging"></a>

# Containers With Custom ClassLoading Behaviour for Logging

Because commons-logging is such a fundamental library, some containers modify the way
in which classloading behaves for commons-logging classes.

<a id="troubleshooting--apache-tomcat"></a>

## Apache Tomcat

At the current date, Tomcat 5.5.16 is the current release. All releases from version
4.1.x through 5.5.16 have a startup process that places jarfile
${tomcat.home}/bin/commons-logging-api.jar in the system classpath and then
prevents any webapp from overriding the classes in that jarfile. Effectively, all
webapps behave as if "parent-first" classloading were enabled for those classes.

This has some benefits; in particular it means that there are no problems in
these Tomcat versions with having multiple copies of the commons-logging Log
interface in the classpath (which avoids the "Log does not implement Log"
problem described elsewhere).

However it also means that no webapp can override the core commons-logging
classes by including an updated commons-logging jarfile in WEB-INF/lib; any
class already loaded via the container takes priority. In particular, as
Tomcat bundles logging 1.0.4 only, the new diagnostics and memory-leak-prevention
features of the 1.1 release will not be available unless the container's
library version is updated.

Because the commons-logging-api.jar in the container does not contain any
log-library-adapter classes, updated behavior for these *will* be
seen when logging 1.1 is bundled in WEB-INF/lib. In particular, the
support for Log4j's TRACE level will take effect without having to update
the container.

If you do wish to update Tomcat's version of commons-logging, then you
*must* use the commons-logging-1.1-api jar only, not the full jar.
Classes in the webapp cannot override classes loaded from the system
classpath set up during Tomcat's startup process, and logging adapters
can only see their matching concrete logging library if that library is
available in the same classpath. Bundling the full commons-logging jarfile
(with adapters) into the system classpath therefore means that logging
libraries (eg Log4j) within WEB-INF/lib are not accessible.

Note that the behavior described here only applies if the standard Tomcat
startup process is run. When Tomcat is embedded in a larger
framework (eg run embedded within an IDE) this may not apply.

<a id="troubleshooting--jboss-application-server"></a>

## JBoss Application Server

The JBoss Application Server can be configured to prevent deployed
code from overriding classes higher in the hierarchy, effectively
forcing "parent-first" behavior for selected classes. By default, commons-logging is in this list (at least for some JBoss versions
starting with 4.0.2), and therefore including an updated version
of commons-logging in WEB-INF/lib or similar will have no effect.
See the JBoss classloading documentation for more details.

<a id="troubleshooting--other-containers"></a>

## Other Containers

As more information becomes available on this topic, it may be added
to the commons-logging wiki site.

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/building.html -->

<!-- page_index: 6 -->

<a id="building--overview"></a>

# Overview

Commons Logging uses [Maven 2.0.x](https://maven.apache.org) as its
primary build system. [Ant](https://ant.apache.org) can also be used.

<a id="building--maven"></a>

# Maven

To build the full website, run

```
mvn site
```

The result will be in the `target/site` folder.
You must be online and using JDK 1.4 or higher to successfully complete this target.

To build the jar files, run

```
mvn package
```

The resulting 4 jar files will be in the `target` folder.
You must use JDK 1.4 or higher to successfully complete this target.

To create a full distribution, run

```
mvn clean site assembly:assembly
```

The resulting .zip and .tar.gz files will be in the `target` folder.
You must use JDK 1.4 or higher to successfully complete this target.

Further details can be found in the
[commons build instructions](https://commons.apache.org/proper/commons-logging/https/commons.apache.org/building.html).

<a id="building--ant"></a>

# Ant

We still use Ant to test the artifacts built my Maven.
Please follow the instructions in the file `build-testing.xml`.

**Note:** A 1.2 JDK is needed to run the tests.

---

<a id="proposal"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/proposal.html -->

<!-- page_index: 7 -->

<a id="proposal--proposal-for-logging-package"></a>

# Proposal for Logging Package

<a id="proposal--0-rationale"></a>

## (0) Rationale

There is a great need for debugging and logging information inside of
Commons components such as HTTPClient and dbcp. However, there are many
logging APIs out there and it is difficult to choose among them.

The Logging package will be an ultra-thin bridge between different logging
libraries. Commons components may use the Logging JAR to remove
compile-time/runtime dependencies on any particular logging package, and contributors may write Log implementations for the library of their choice.

<a id="proposal--1-scope-of-the-package"></a>

## (1) Scope of the Package

The package shall create and maintain a package that provides extremely
basic logging functionality and bridges to other, more sophisticated logging
implementations.

The package should :

- Have an API which should be as simple to use as possible
- Provide support for Log4j
- Provide pluggable support for other logging APIs

Non-goals:

- This package will not perform logging itself, except at the most basic
  level.
- We do not seek to become a "standard" API.

<a id="proposal--1.5-interaction-with-other-packages"></a>

## (1.5) Interaction With Other Packages

*Logging* relies on:

- Java Development Kit (Version 1.1 or later)
- Avalon Framework (compile-time dependency only unless this Log
  implementation is selected at runtime)
- Avalon LogKit (compile-time dependency only unless this Log
  implementation is selected at runtime)
- JDK 1.4 (compile-time dependency only unless this log implementation
  is selected at runtime).
- Log4J (compile-time dependency only unless this Log
  implementation is selected at runtime)
- [Lumberjack](https://commons.apache.org/proper/commons-logging/https/sourceforge.net/projects/lumberjack/)
  (compile-time dependency only unless this Log
  implementation is selected at runtime)

<a id="proposal--2-required-jakarta-commons-resources"></a>

## (2) Required Jakarta-Commons Resources

- CVS Repository - New directory `logging` in the
  `jakarta-commons` CVS repository.
- Initial Committers - The list is provided below.
- Mailing List - Discussions will take place on the general
  *dev@commons.apache.org* mailing list. To help list
  subscribers identify messages of interest, it is suggested that the
  message subject of messages about this component be prefixed with
  [Logging].
- Bugzilla - New component "Logging" under the "Commons" product
  category, with appropriate version identifiers as needed.
- Jyve FAQ - New category "commons-logging" (when available).

<a id="proposal--4-initial-committers"></a>

## (4) Initial Committers

The initial committers on the Logging component shall be:

- Morgan Delagrange
- Rodney Waldhoff
- Craig McClanahan

---

<a id="tech"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/tech.html -->

<!-- page_index: 8 -->

<a id="tech--overview"></a>

# Overview

<a id="tech--contents"></a>

## Contents

- Overview
  - Contents
  - [Introduction](#tech--introduction)
- [A Short Introduction to Class Loading and Class Loaders](#tech--a_short_introduction_to_class_loading_and_class_loaders)
  - [Preamble](#tech--preamble)
  - [Resolution Of Symbolic References](#tech--resolution_of_symbolic_references)
  - [Loading](#tech--loading)
  - [Linking](#tech--linking)
  - [Loading Classes](#tech--loading_classes)
  - [Bootstrap Classloader](#tech--bootstrap_classloader)
  - [Runtime Package](#tech--runtime_package)
  - [Loader Used To Resolve A Symbolic Reference](#tech--loader_used_to_resolve_a_symbolic_reference)
  - [Bibliography](#tech--bibliography)
- [A Short Guide To Hierarchical Class Loading](#tech--a_short_guide_to_hierarchical_class_loading)
  - [Delegating Class Loaders](#tech--delegating_class_loaders)
  - [Parent-First And Child-First Class Loaders](#tech--parent-first_and_child-first_class_loaders)
  - [Class ClassLoader](#tech--class_classloader)
  - [Context ClassLoader](#tech--context_classloader)
  - [The Context Classloader in Container Applications](#tech--the_context_classloader_in_container_applications)
  - [Issues with Context ClassLoaders](#tech--issues_with_context_classloaders)
  - [Reflection And The Context ClassLoader](#tech--reflection_and_the_context_classloader)
  - [More Information](#tech--more_information)
- [A Short Theory Guide To JCL](#tech--a_short_theory_guide_to_jcl)
  - [Isolation And The Context Class Loader](#tech--isolation_and_the_context_class_loader)
  - [Log And LogFactory](#tech--log_and_logfactory)
  - [Log Implementations](#tech--log_implementations)
  - [Using Reflection To Load Log Implementations](#tech--using_reflection_to_load_log_implementations)

<a id="tech--introduction"></a>

## Introduction

This guide is aimed at describing the technologies that JCL developers and expert users
(and users who need to become experts)
should be familiar with. The aim is to give an understanding whilst being precise but brief.
Details which are not relevant for JCL have been suppressed.
References have been included.

These topics are a little difficult and it's easy for even experienced developers to make
mistakes. We need you to help us get it right! Please submit corrections, comments, additional references
and requests for clarification
by either:

- posting to the [Apache Commons dev mailing list](https://commons.apache.org/proper/commons-logging/https/commons.apache.org/mail-lists.html) or
- creating an issue in [JIRA](https://commons.apache.org/proper/commons-logging/https/issues.apache.org/jira/browse/LOGGING/).

TIA

<a id="tech--a-short-introduction-to-class-loading-and-class-loaders"></a>

# A Short Introduction to Class Loading and Class Loaders

<a id="tech--preamble"></a>

## Preamble

This is intended to present a guide to the process by which Java bytecode uses bytecode in other classes
from the perspective of the language and virtual machine specifications. The focus will be on deciding
which bytecode will be used (rather than the mechanics of the usage). It focuses on facts and terminology.

The process is recursive: it is therefore difficult to pick a starting point.
Sun's documentation starts from the perspective of the startup of a new application.
This guide starts from the perspective of an executing application.

During this discussion, please assume that each time that *class* is mentioned, the comments applied equally well to interfaces.

This document is targeted at Java 1.2 and above.

<a id="tech--resolution-of-symbolic-references"></a>

## Resolution Of Symbolic References

([LangSpec 12.3.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/jls/second_edition/html/execution.doc.html#a44524))
The bytecode representation of a class contains symbolic names for other classes referenced.

*In practical development terms: If a class is imported (either explicitly in the list of imports at the top of
the source file or implicitly through a fully qualified name in the source code) it is referenced symbolically.*

([VMSpec 5.4.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/ConstantPool.doc.html#a73492))
Resolution of a symbolic reference occurs dynamically at runtime and is carried out by
the Java Virtual Machine. Resolution of a symbolic reference requires loading and linking of the new class.

*Note: references are not statically resolved at compile time.*

<a id="tech--loading"></a>

## Loading

([VMSpec 2.17.2](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/Concepts.doc.html#a19175))
Loading is the name given to the process by which a binary form of a class is obtained
by the Java Virtual Machine.
Java classes are always loaded and linked dynamically by the Java Virtual Machine
(rather than statically by the compiler).

*In practical development terms:
This means that the developer has no certain knowledge about the actual
bytecode that will be used to execute any external call (one made outside the class). This is determined only
at execution time and is affected by the way that the code is deployed.*

<a id="tech--linking"></a>

## Linking

([VMSpec 2.17.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/Concepts.doc.html#a22574))
Linking is the name used for combining the
binary form of a class into the Java Virtual Machine. This must happen before the class can be used.

([VMSpec 2.17.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/Concepts.doc.html#a22574))
Linking is composed of verification, preparation and resolution (of symbolic references).
Flexibility is allowed over the timing of resolution. (Within limit) this may happen at any time after
preparation and before that reference is used.

*In practical development terms: This means that different JVMs may realize that a reference cannot be
resolved at different times during execution. Consequently, the actual behavior cannot be precisely predicted
without intimate knowledge of the JVM (on which the bytecode will be executed).
This makes it hard to give universal guidance to users.*

<a id="tech--loading-classes"></a>

## Loading Classes

([VMSpec 2.17.2](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/Concepts.doc.html#a19175))
The loading process is performed by a `ClassLoader`.

([VMSpec 5.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/ConstantPool.doc.html#a72007))
A classloader may create a class either by delegation or by defining it directly.
The classloader that initiates loading of a class is known as the initiating loader.
The classloader that defines the class is known as the defining loader.

*In practical terms: understanding and appreciating this distinction is crucial when debugging issues
concerning classloaders.*

<a id="tech--bootstrap-classloader"></a>

## Bootstrap Classloader

([VMSPEC 5.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/ConstantPool.doc.html#a72007))
The bootstrap is the base `ClassLoader` supplied by the Java Virtual Machine.
All others are user (also known as application) `ClassLoader` instances.

*In practical development terms: The System classloader returned by `Classloader.getSystemClassLoader()`
will be either the bootstrap classloader or a direct descendant of the bootstrap classloader.
Only when debugging issues concerning the system classloader should there be any need to consider the detailed
differences between the bootstrap classloader and the system classloader.*

<a id="tech--runtime-package"></a>

## Runtime Package

([VMSpec 5.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/ConstantPool.doc.html#a72007))
At runtime, a class (or interface) is determined by its fully qualified name
and by the classloader that defines it. This is known as the class's runtime package.

([VMSpec 5.4.4](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/ConstantPool.doc.html#a75929))
Only classes in the same runtime package are mutually accessible.

*In practical development terms: two classes with the same symbolic name can only be used interchangeably
if they are defined by the same classloader. A classic symptom indicative of a classloader issue is that
two classes with the same fully qualified name are found to be incompatible during a method call.
This may happen when a member is expecting an interface which is (seemingly) implemented by a class
but the class is in a different runtime package after being defined by a different classloader. This is a
fundamental java language security feature.*

<a id="tech--loader-used-to-resolve-a-symbolic-reference"></a>

## Loader Used To Resolve A Symbolic Reference

([VMSpec 5.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/2nd-edition/html/ConstantPool.doc.html#a72007))
The classloader which defines the class (whose reference is being resolved) is the one
used to initiate loading of the class referred to.

*In practical development terms: This is very important to bear in mind when trying to solve classloader issues.
A classic misunderstanding is this: suppose class A defined by classloader C has a symbolic reference to
class B and further that when C initiates loading of B, this is delegated to classloader D which defines B.
Class B can now only resolve symbols that can be loaded by D, rather than all those which can be loaded by C.
This is a classic recipe for classloader problems.*

<a id="tech--bibliography"></a>

## Bibliography

- [VMSpec](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/vmspec/) *The Java Virtual Machine Specification, Second Edition*
- [LangSpec](https://commons.apache.org/proper/commons-logging/https/java.sun.com/docs/books/jls/) *The Java Language Specification, Second Edition*

<a id="tech--a-short-guide-to-hierarchical-class-loading"></a>

# A Short Guide To Hierarchical Class Loading

<a id="tech--delegating-class-loaders"></a>

## Delegating Class Loaders

When asked to load a class, a class loader may either define the class itself or delegate.
The base `ClassLoader` class insists that every implementation has a parent class loader.
This delegation model therefore naturally forms a tree structure rooted in the bootstrap classloader.

Containers (i.e. applications such as servlet engines or application servers
that manage and provide support services for a number of "contained" applications
that run inside of them) often use complex trees to allow isolation of different applications
running within the container. This is particularly true of J2EE containers.

<a id="tech--parent-first-and-child-first-class-loaders"></a>

## Parent-First And Child-First Class Loaders

When a classloader is asked to load a class, a question presents itself: should it immediately
delegate the loading to its parent (and thus only define those classes not defined by its parent)
or should it try to define it first itself (and only delegate to its parent those classes it does
not itself define). Classloaders which universally adopt the first approach are termed parent-first
and the second child-first.

**Note:** the term child-first (though commonly used) is misleading.
A better term (and one which may be encountered on the mailing list) is parent-last.
This more accurately describes the actual process of classloading performed
by such a classloader.

Parent-first loading has been the standard mechanism in the JDK
class loader, at least since Java 1.2 introduced hierarchical classloaders.

Child-first classloading has the advantage of helping to improve isolation
between containers and the applications inside them. If an application
uses a library jar that is also used by the container, but the version of
the jar used by the two is different, child-first classloading allows the
contained application to load its version of the jar without affecting the
container.

The ability for a servlet container to offer child-first classloading
is made available, as an option, by language in the servlet spec (Section
9.7.2) that allows a container to offer child-first loading with
certain restrictions, such as not allowing replacement of java.\* or
javax.\* classes, or the container's implementation classes.

Though child-first and parent-first are not the only strategies possible, they are by far the most common.
All other strategies are rare.
However, it is not uncommon to be faced with a mixture of parent-first and child-first
classloaders within the same hierarchy.

<a id="tech--class-classloader"></a>

## Class ClassLoader

The class loader used to define a class is available programmatically by calling
the `getClassLoader` method
on the class in question. This is often known as the class classloader.

<a id="tech--context-classloader"></a>

## Context ClassLoader

Java 1.2 introduces a mechanism which allows code to access classloaders
which are not the class classloader or one of its parents.
A thread may have a class loader associated with it by its creator for use
by code running in the thread when loading resources and classes.
This classloader is accessed by the `getContextClassLoader`
method on `Thread`. It is therefore often known as the context classloader.

Note that the quality and appropriateness of the context classloader depends on the
care with which the thread's owner manages it.

<a id="tech--the-context-classloader-in-container-applications"></a>

## The Context Classloader in Container Applications

The Javadoc for
[`Thread.setContextClassLoader`](https://commons.apache.org/proper/commons-logging/https/java.sun.com/j2se/1.5.0/docs/api/java/lang/Thread.html#setContextClassLoader.28java.lang.ClassLoader.29) emphasizes the setting of the
context classloader as an aspect of thread creation. However, in many
applications the context classloader is not fixed at thread creation but
rather is changed throughout the life of a thread as thread execution moves
from one context to another. This usage of the context classloader is
particularly important in container applications.

For example, in a hypothetical servlet container, a pool of threads
is created to handle HTTP requests. When created these threads have their
context classloader set to a classloader that loads container classes.
After the thread is assigned to handle a request, container code parses
the request and then determines which of the deployed web applications
should handle it. Only when the container is about to call code associated
with a particular web application (i.e. is about to cross an "application
boundary") is the context classloader set to the classloader used to load
the web app's classes. When the web application finishes handling the
request and the call returns, the context classloader is set back to the
container classloader.

In a properly managed container, changes in the context classloader are
made when code execution crosses an application boundary. When contained
application `A` is handling a request, the context classloader
should be the one used to load `A`'s resources. When application
`B` is handling a request, the context classloader should be
`B`'s.

While a contained application is handling a request, it is not
unusual for it to call system or library code loaded by the container.
For example, a contained application may wish to call a utility function
provided by a shared library. This kind of call is considered to be
within the "application boundary", so the context classloader remains
the contained application's classloader. If the system or library code
needs to load classes or other resources only visible to the contained
application's classloader, it can use the context classloader to access
these resources.

If the context classloader is properly managed, system and library code
that can be accessed by multiple applications can not only use it to load
application-specific resources, but also can use it to detect which
application is making a call and thereby provided services tailored to the
caller.

<a id="tech--issues-with-context-classloaders"></a>

## Issues with Context ClassLoaders

In practice, context classloaders vary in quality and issues sometimes arise
when using them.
The owner of the thread is responsible for setting the classloader.
If the context classloader is not set then it will default to the system
classloader.
Any container doing so will cause difficulties for any code using the context classloader.

The owner is also at liberty to set the classloader as they wish.
Containers may set the context classloader so that it is neither a child nor a parent
of the classloader that defines the class using that loader.
Again, this will cause difficulties.

Introduced in [Java J2EE 1.3](https://commons.apache.org/proper/commons-logging/https/java.sun.com/j2ee/j2ee-1_3-fr-spec.pdf)
is a requirement for vendors to appropriately set the context classloader.
Section 6.2.4.8 (1.4 text):

```

This specification requires that J2EE containers provide a per thread
context class loader for the use of system or library classes in
dynamically loading classes provided by the application.  The EJB
specification requires that all EJB client containers provide a per
thread context class loader for dynamically loading system value classes.
The per thread context class loader is accessed using the Thread method
getContextClassLoader.

The classes used by an application will typically be loaded by a
hierarchy of class loaders. There may be a top level application class
loader, an extension class loader, and so on, down to a system class
loader.  The top level application class loader delegates to the lower
class loaders as needed.  Classes loaded by lower class loaders, such as
portable EJB system value classes, need to be able to discover the top
level application class loader used to dynamically load application
classes.

We require that containers provide a per thread context class loader
that can be used to load top level application classes as described
above.
```

This specification leaves quite a lot of freedom for vendors.
(As well as using unconventional terminology and containing the odd typo.)
It is a difficult passage (to say the least).

<a id="tech--reflection-and-the-context-classloader"></a>

## Reflection And The Context ClassLoader

Reflection cannot bypass restrictions imposed by the java language security model, but, by avoiding symbolic
references, reflection can be used to load classes which could not otherwise be loaded. Another `ClassLoader`
can be used to load a class and then reflection used to create an instance.

Recall that the runtime packaging is used to determine accessibility.
Reflection cannot be used to avoid basic java security.
Therefore, the runtime packaging becomes an issue when attempting to cast classes
created by reflection using other class loaders.
When using this strategy, various modes of failure are possible
when common class references are defined by the different class loaders.

Reflection is often used with the context classloader. In theory, this allows a class defined in
a parent classloader to load any class that is loadable by the application.
In practice, this only works well when the context classloader is set carefully.

<a id="tech--more-information"></a>

## More Information

- Articles On Class Loaders And Class Loading
  - [Article on J2EE class loading](https://commons.apache.org/proper/commons-logging/https/www.onjava.com/pub/a/onjava/2001/07/25/ejb.html)
  - [Article on class loading](https://commons.apache.org/proper/commons-logging/https/www.onjava.com/pub/a/onjava/2003/11/12/classloader.html)
  - [Article on context class loaders](https://commons.apache.org/proper/commons-logging/https/www.javaworld.com/javaworld/javaqa/2003-06/01-qa-0606-load.html)
- Specific Containers
  - [Tomcat 4.1 ClassLoader Guide](https://commons.apache.org/proper/commons-logging/https/tomcat.apache.org/tomcat-4.1-doc/class-loader-howto.html)
  - [Tomcat 5.0 ClassLoader Guide](https://commons.apache.org/proper/commons-logging/https/tomcat.apache.org/tomcat-5.0-doc/class-loader-howto.html)
  - [Classloading In WebSphere](https://commons.apache.org/proper/commons-logging/https/publib.boulder.ibm.com/infocenter/wasinfo/v6r0/index.jsp?topic=%2Fcom.ibm.websphere.express.doc%2Finfo%2Fexp%2Fae%2Ftrun_classload_web.html)

<a id="tech--a-short-theory-guide-to-jcl"></a>

# A Short Theory Guide To JCL

<a id="tech--isolation-and-the-context-class-loader"></a>

## Isolation And The Context Class Loader

JCL takes the view that different context class loader indicate boundaries between applications
running in a container environment. Isolation requires that JCL honours these boundaries
and therefore allows different isolated applications to configure their logging systems
independently.

<a id="tech--log-and-logfactory"></a>

## Log And LogFactory

Performance dictates that symbolic references to these classes are present in the calling application code
(reflection would simply be too slow). Therefore, these classes must be loadable by the classloader
that loads the application code.

<a id="tech--log-implementations"></a>

## Log Implementations

Performance dictates that symbolic references to the logging systems are present in the implementation
classes (again, reflection would simply be too slow). So, for an implementation to be able to function, it is necessary for the logging system to be loadable by the classloader that defines the implementing class.

<a id="tech--using-reflection-to-load-log-implementations"></a>

## Using Reflection To Load Log Implementations

However, there is actually no reason why `LogFactory` requires symbolic references to particular `Log`
implementations. Reflection can be used to load these from an appropriate classloader
without unacceptable performance degradation.
This is the strategy adopted by JCL.

JCL uses the context classloader to load the `Log` implementation.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/project-info.html -->

<!-- page_index: 9 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Logging is a thin adapter allowing configurable bridging to other, well-known logging systems. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-logging/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-logging/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-logging/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-logging/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-logging/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-logging/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-logging/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/summary.html -->

<!-- page_index: 10 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Logging |
| Description | Apache Commons Logging is a thin adapter allowing configurable bridging to other, well-known logging systems. |
| Homepage | [https://commons.apache.org/proper/commons-logging/](#index) |

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
| GroupId | commons-logging |
| ArtifactId | commons-logging |
| Version | 1.3.6 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/team.html -->

<!-- page_index: 11 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | baliuka | Juozas Baliuka | [baliuka@apache.org](mailto:baliuka@apache.org) | - | - | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | morgand | Morgan Delagrange | [morgand@apache.org](mailto:morgand@apache.org) | - | Apache | - | Java Developer | - |
| ![](assets/images/d7c9c04cdf16500005212d9a2bcbc3f6_f21aaa5564d35985.jpg) | donaldp | Peter Donald | [donaldp@apache.org](mailto:donaldp@apache.org) | - | - | - | - | - |
| ![](assets/images/30f9094d5dbe2ce93f1a41afc9615b83_53d8aa600350c7cb.jpg) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | skitching | Simon Kitching | [skitching@apache.org](mailto:skitching@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/c8686cad245196c9e392201ad7bb364f_60b54b5605cb4592.jpg) | dennisl | Dennis Lundberg | [dennisl@apache.org](mailto:dennisl@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | costin | Costin Manolache | [costin@apache.org](mailto:costin@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | craigmcc | Craig McClanahan | [craigmcc@apache.org](mailto:craigmcc@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | sanders | Scott Sanders | [sanders@apache.org](mailto:sanders@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | rsitze | Richard Sitze | [rsitze@apache.org](mailto:rsitze@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | bstansberry | Brian Stansberry | - | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | rwaldhoff | Rodney Waldhoff | [rwaldhoff@apache.org](mailto:rwaldhoff@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Roles |
| --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Matthew P. Del Buono | - | Provided patch |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Vince Eagen | [vince256 at comcast dot net](mailto:vince256 at comcast dot net) | Lumberjack logging abstraction |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Peter Lawrey | - | Provided patch |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Berin Loritsch | [bloritsch at apache dot org](mailto:bloritsch at apache dot org) | Lumberjack logging abstraction, JDK 1.4 logging abstraction |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Philippe Mouawad | - | Provided patch |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Neeme Praks | [neeme at apache dot org](mailto:neeme at apache dot org) | Avalon logging abstraction |
| ![](assets/images/00000000000000000000000000000000_4487cfcc235131b2.jpg) | Arturo Bernal | [arturobernalg@yahoo.com](mailto:arturobernalg@yahoo.com) | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-logging/ci-management.html -->

<!-- page_index: 12 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-logging/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
