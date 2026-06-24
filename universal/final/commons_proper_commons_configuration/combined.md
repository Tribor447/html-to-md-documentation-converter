# Project Information

## Navigation

- Commons Configuration
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Javadoc](#index)
  - [Building](#building)
  - [User's Guide](#userguide-user_guide)
  - [Upgrade Guide: 1.x to 2.0](#userguide-upgradeto2_0)
  - [Upgrade Guide: 2.x](#userguide-upgradeto2_x)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Other pages
  - [Basic features and AbstractConfiguration](#userguide-howto_basicfeatures)
  - [Declaring and Creating Beans](#userguide-howto_beans)
  - [Creating Configurations](#userguide-howto_builders)
  - [Combining Configuration Sources](#userguide-howto_combinedbuilder)
  - [Combined Configuration](#userguide-howto_combinedconfiguration)
  - [Configurations and Concurrent Access](#userguide-howto_concurrency)
  - [File-based Configurations](#userguide-howto_filebased)
  - [Hierarchical Configurations](#userguide-howto_hierarchical)
  - [Multi-tenant Configurations](#userguide-howto_multitenant)
  - [Properties files](#userguide-howto_properties)
  - [Automatic Reloading of Configuration Sources](#userguide-howto_reloading)
  - [Using Configuration](#userguide-overview)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/index.html -->

<!-- page_index: 1 -->

<a id="index--introducing-apache-commons-configuration"></a>

# Introducing Apache Commons Configuration

The Commons Configuration software library provides a generic configuration interface which enables
a Java application to read configuration data from a variety of sources. Commons Configuration
provides typed access to single, and multi-valued configuration parameters as demonstrated
by the following code:

```
Double double = config.getDouble("number");
Integer integer = config.getInteger("number");
```

Configuration parameters may be loaded from the following sources:

- Properties files
- XML documents
- Windows INI files
- Property list files (plist)
- JNDI
- JDBC Datasource
- System properties
- Applet parameters
- Servlet parameters

Configuration objects are created using configuration builders.
Different configuration sources can be mixed using a `CombinedConfigurationBuilder` and
a `CombinedConfiguration`. Additional sources of configuration parameters can
be created by using custom configuration objects. This customization can be achieved by
extending `AbstractConfiguration` or `AbstractHierarchicalConfiguration`.

The full Javadoc API documentation is available [here](https://commons.apache.org/proper/commons-configuration/apidocs/index.html).

<a id="index--commons-configuration-1.x-and-2.x"></a>

# Commons Configuration 1.x and 2.x

New projects should use 2.x, first released in 2016, under the Maven coordinates `org.apache.commons:commons-configuration2`.

The 1.x codebase no longer receives updates.
Denial of service issues that rely on loading untrusted data from configuration files, or passing untrusted data to the API, are outside the scope of the 1.x security model
and will not be fixed. Upgrading your application from 1.x to 2.x will require at least changing import statement
code changes and possibly more, see the [migration guide for 2.0](#userguide-upgradeto2_0).

The most recent Commons Configuration 2.x release can be downloaded from the
[Apache download area](https://commons.apache.org/configuration/download_configuration.cgi).
The artifacts have also been deployed to
[Maven central](https://repo1.maven.org/maven2/). Commons Configuration 1.x
artifacts are also available under their original Maven coordinates.

<a id="index--history"></a>

# History

Commons Configuration started as code in Apache JServ. The JServ code was subsequently
added to [Jakarta Turbine](https://jakarta.apache.org/turbine). After Jakarta
Turbine, this configuration interface moved to [Jakarta Velocity](https://jakarta.apache.org/velocity)
and underwent various improvements. After Velocity, this code was introduced to the
[Apache Commons](https://commons.apache.org/) as `ExtendedProperties`.
Configuration began life in the Commons as a Sandbox component and was promoted to the
Commons Proper in late 2003.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-configuration.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch rel/commons-configuration-2.15.0 https://gitbox.apache.org/repos/asf/commons-configuration.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/commons-configuration-2.15.0 https://gitbox.apache.org/repos/asf/commons-configuration.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/security.html -->

<!-- page_index: 3 -->

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

For information about reporting or asking questions about
security, please see the
[security page](https://commons.apache.org/security.html)
of the Apache Commons project.

This page lists all security vulnerabilities fixed in released versions of this component.

Binary patches are never provided. Refer to a component's building instructions to apply source patches.

If you need help building this component or other help following the instructions to
mitigate the known vulnerabilities listed here, please send your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-configuration/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has a security
impact, or if the descriptions here are incomplete, please report them privately to the Apache Security
Team. Thank you.

<a id="security--security-model"></a>

## Security Model

The [Apache Commons security model](https://commons.apache.org/security.html#Security_Model)
specifies that it is unsafe to pass possibly malicious input to Commons libraries.
For Commons Configuration 2.x, the library is designed to support processing untrusted configuration files, without allowing those to trigger arbitrary code execution or denial of service situations.
'Denial of service' here means causing resource usage disproportionate to the input size.

<a id="security--cve-2022-33980-prior-to-2.8.0-rce-when-applied-to-untrusted-input"></a>

## CVE-2022-33980, prior to 2.8.0, RCE when applied to untrusted input

On 2022-07-06, the Apache Commons Configuration team disclosed
[CVE-2022-33980](https://www.cve.org/CVERecord?id=CVE-2022-33980)
. Key takeaways:

- If you rely on software that uses a version of Commons Configuration before 2.8.0, you are likely
  still not vulnerable: only if this software loads configuration
  files from untrusted sources, which is likely rare.
- If your software uses Commons Configuration, double-check whether it loads
  configuration files from untrusted sources. If so, an update to 2.8.0 could be a
  quick workaround, but the recommended solution is to validate and sanitize
  untrusted input.

Apache Commons Configuration is a library that reads configuration data from many sources.
It supports variable interpolation with lookups using various mechanisms, such as system properties
or environment variables. Some of the available interpolators can trigger network
access or code execution. This is intended, but it also means an application that includes user
input in the configuration passed to Commons Configuration without properly sanitizing it would allow an
attacker to trigger those interpolators.

For that reason, the Apache Commons Configuration team decided to update the list of interpolators
enabled by default to be more conservative, so that the impact of a failure to validate inputs is mitigated and will not
give an attacker access to these interpolators. However, it is still recommended that users treat
untrusted input with care.

We're not currently aware of any applications that load untrusted input as configuration
and thus would have been impacted by this problem before Apache Commons Configuration 2.8.0.

This issue is different from
[Log4Shell (CVE-2021-44228)](https://logging.apache.org/log4j/2.x/security.html#log4j-2.15.0)
because in Log4Shell, string interpolation was possible from the log message body, which commonly
contains untrusted input. In the Apache Common Configuration issue, the processed configuration data
is much less likely to come from an untrusted source.

Credit: this issue was reported by
[@pwntester (Alvaro Muñoz)](https://github.com/pwntester)
of the
[GitHub Security Lab team](https://securitylab.github.com)
. Thank you!

References:

- [Announcement on dev@commons.apache.org](https://lists.apache.org/thread/tdf5n7j80lfxdhs2764vn0xmpfodm87s)
- [Announcement on oss-security](https://www.openwall.com/lists/oss-security/2022/07/06/5)
- [Advisory on cve.org](https://www.cve.org/CVERecord?id=CVE-2022-33980)
- [GHSL advisory](https://securitylab.github.com/advisories/GHSL-2022-017_Apache_Commons_Configuration/)

<a id="security--cve-2024-29131-prior-to-2.10.1-out-of-bounds-write-vulnerability"></a>

## CVE-2024-29131, prior to 2.10.1, Out-of-bounds Write vulnerability

On 2024-03-20, the Apache Commons Configuration team disclosed [CVE-2024-29131](https://www.cve.org/CVERecord?id=CVE-2024-29131).

This Out-of-bounds Write vulnerability in Apache Commons Configuration affects Apache Commons Configuration: from 2.0 before 2.10.1.
Users can see this as a `StackOverflowError` when adding a property in `AbstractListDelimiterHandler.flattenIterator()`.
Users are recommended to upgrade to version 2.10.1, which fixes the issue.
The details are in [CONFIGURATION-840](https://issues.apache.org/jira/browse/CONFIGURATION-840).

<a id="security--cve-2024-29133-prior-to-2.10.1-out-of-bounds-write-vulnerability"></a>

## CVE-2024-29133, prior to 2.10.1, Out-of-bounds Write vulnerability

On 2024-03-20, the Apache Commons Configuration team disclosed [CVE-2024-29133](https://www.cve.org/CVERecord?id=CVE-2024-29133).

This Out-of-bounds Write vulnerability in Apache Commons Configuration affects Apache Commons Configuration: from 2.0 before 2.10.1.
Users can see this as a `StackOverflowError` calling `ListDelimiterHandler.flatten(Object, int)` with a cyclical object tree.
Users are recommended to upgrade to version 2.10.1, which fixes the issue.
The details are in [CONFIGURATION-841](https://issues.apache.org/jira/browse/CONFIGURATION-840).

<a id="security--cve-2026-45205-prior-to-2.15.0-stackoverflowerror-for-yaml-input-with-cycles"></a>

## CVE-2026-45205, prior to 2.15.0, StackOverflowError for YAML input with cycles

On 2026-05-14, the Apache Commons Configuration team disclosed [CVE-2026-45205](https://www.cve.org/CVERecord?id=CVE-2026-45205).

When processing an untrusted configuration file, Commons Configuration will throw a StackOverflowError for YAML input with cycles.
This issue affects Apache Commons: from 2.2 before 2.15.0.
Users are recommended to upgrade to version 2.15.0, which fixes the issue.

References:

- [CVE-2026-45205](https://www.cve.org/CVERecord?id=CVE-2026-45205)
- [PR #634](https://github.com/apache/commons-configuration/pull/634)

<a id="security--safe-deserialization"></a>

# Safe Deserialization

For information about safe deserialization, please see [Safe Deserialization](https://commons.apache.org/io/description.html#Safe_Deserialization).

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/building.html -->

<!-- page_index: 4 -->

<a id="building--building"></a>

# Building

Commons Configuration uses [Maven](https://maven.apache.org) as its build tool.
Any recent version of Maven should work. To build the Configuration
jar, change into the directory where the source distribution resides and run
"mvn install". This will compile the source and tests, run the tests, and then
package the jar. The jar will also be copied into the local maven repository
for use by other builds. According to the minimum Java version of
Commons Configuration, this build requires a JDK 8 or higher.

To build the web site run "mvn site". When it completes the web site will reside in
the target/site directory and may be viewed by opening target/site/index.html.

---

<a id="userguide-user_guide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/user_guide.html -->

<!-- page_index: 5 -->

<a id="userguide-user_guide--about-this-document"></a>

# About this document

This document describes the features of the Commons Configuration
component starting with the very basics and up to the more advanced
topics. If you read it in a linear way, you should get a sound
understanding of the provided classes and the possibilities they
offer. But you can also skip sections and jump directly to the topics
you are most interested in.

---

<a id="userguide-upgradeto2_0"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/upgradeto2_0.html -->

<!-- page_index: 6 -->

<a id="userguide-upgradeto2_0--migration-guide-to-version-2.0"></a>

# Migration Guide to Version 2.0

This document aims at supporting with the migration from version 1.x of
*Commons Configuration* to version 2.0. Target audience are
users of an older version who want to upgrade. The document describes the
areas in which major changes have been implemented; here problems are
likely to be encountered during migration. It has the following content:

- [Introduction](#userguide-upgradeto2_0--introduction)
- [Structural Changes](#userguide-upgradeto2_0--structural_changes)
- [Accessing Configuration Properties](#userguide-upgradeto2_0--accessing_configuration_properties)
- [Creating Configurations](#userguide-upgradeto2_0--creating_configurations)
- [Reloading](#userguide-upgradeto2_0--reloading)
- [Combining Configuration Sources](#userguide-upgradeto2_0--combining_configuration_sources)
- [Concurrency Issues](#userguide-upgradeto2_0--concurrency_issues)
- [Events](#userguide-upgradeto2_0--events)

<a id="userguide-upgradeto2_0--introduction"></a>

## Introduction

Version 2.0 of *Commons Configuration* is the result of a major
redesign of this library. While version 1.x has become pretty stable and
does what it is expected to do, there are some limitations and design
flaws which could not be fixed in a painless and compatible way.

In order to overcome these restrictions, version 2.0 has applied significant
changes to some of the problematic concepts or even replaced them by
alternative approaches. This has lead to an ambivalent situation: On one
hand, you will recognize many similarities to the old version - classes
with familiar names that continue to do what they have done before. On
the other hand, completely new approaches have been introduced; in the
affected areas *Commons Configuration* 2.0 will look like a
completely new product rather than a plain upgrade.

Because of such major changes, you cannot simply drop the new jar in your
classpath and expect that everything continues to work. In the remaining
part of this document the most important changes are described. This
should give you an impression about the effort required to integrate the
new version with your application.

Also note that the [user's guide](#userguide-user_guide) has been
fully reworked to cover all the new features and concepts offered by
*Commons Configuration* 2.0. Because of that, this document will not
describe interfaces or classes in detail, but simply refer to the
corresponding sections of the user guide.

<a id="userguide-upgradeto2_0--structural-changes"></a>

## Structural Changes

The most obvious change you will notice at the very beginning is that
the root package was renamed to `org.apache.commons.configuration2`
- the major version is now part of the package name. This certainly makes
migration harder, but it is the only possibility to avoid jar hell.
Imagine for a moment that we had kept the old package name. This
would work well for applications that are the only user of the
*Commons Configuration* library. But as soon as there are 3rd
party libraries also using this component, but in version 1.x, then there
is real trouble: The class path then contains classes with identical
names in different versions - results will be unpredictable! The change
of the package name solves this problem because the new version can now
coexist with an old version without interfering. The very first step
you have to when migrating to version 2.0 is to reorganize your imports
to adapt them to the new package name. Modern IDEs will support you with
this task.

For the same reason the [Maven](https://maven.apache.org)
coordinates have been changed. Use the following dependency declaration
in your pom:

```

<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-configuration2</artifactId>
  <version>2.7</version>
</dependency>
```

So for Maven version 2.0 is a completely different artifact. This
allows a peaceful coexistence of *Commons Configuration* 1.x and
2.0 in the dependency set of a project.

<a id="userguide-upgradeto2_0--accessing-configuration-properties"></a>

## Accessing Configuration Properties

The good news is that there are only minor changes in the central
`Configuration` interface used for reading and writing configuration
data. A few methods have been added supporting new features, but the
principle patterns for dealing with `Configuration` objects
remain valid. These concepts are described in the user's guide in the
sections [Using Configuration](#userguide-overview--using_configuration)
and [Basic
features and AbstractConfiguration](#userguide-howto_basicfeatures--basic_features_and_abstractconfiguration).

What has changed is the default implementation of
[List handling](#userguide-howto_basicfeatures--list_handling) in
`AbstractConfiguration`. In version 1.x list splitting was
enabled per default; string properties containing a "," character
were interpreted as lists with multiple elements. This was a frequent
source for confusion and bug reports. In version 2.0 list splitting is now
disabled initially. The implementation also has been extended: it is no
longer limited to providing a delimiter character, but an implementation
of the `ListDelimiterHandler` interface can be set which controls all
aspects of list handling. In order to enable list handling again, pass a
`DefaultListDelimiterHandler` object to your
`AbstractConfiguration` instance. This class supports splitting
string properties at specific delimiter characters. However, its results
are not 100% identical to the ones produced by *Commons Configuration*
1.0: this version contained some inconsistencies regarding the escaping of
list delimiter characters. If you really need the same behavior in this
area, then use the
`LegacyListDelimiterHandler` class.

Version 2.0 also has changes related to
[Hierarchical
Configurations](#userguide-howto_hierarchical--hierarchical_configurations).
`HierarchicalConfiguration`, formally the base class for all
hierarchical configurations, is now an interface. The equivalent to the
old base class is now named
`BaseHierarchicalConfiguration`. It extends the abstract base class
`AbstractHierarchicalConfiguration`. The difference between these
classes is that `AbstractHierarchicalConfiguration` provides
generic algorithms for dealing with an arbitrary hierarchical node
structure. `BaseHierarchicalConfiguration` in contrast defines
its own node structure based on objects kept in memory. In future, it
should be possible to support other kinds of hierarchical structures
directly by creating specialized sub classes from
`AbstractHierarchicalConfiguration`. Refer to section
[Internal Representation](#userguide-howto_hierarchical--internal_representation)
for further information. The node objects a hierarchical configuration
deals with are now exposed as a generic type parameter; for instance, `BaseHierarchicalConfiguration` is actually an
`AbstractHierarchicalConfiguration<ImmutableNode>`.
For most applications only interested in accessing configuration data via
the typical access methods, this parameter is not relevant and can be
replaced by a wildcard ("?") in variable declarations. Extended
query facilities on hierarchical configurations work in the same way as
in version 1.x; so applications need not be updated in this area.

<a id="userguide-upgradeto2_0--creating-configurations"></a>

## Creating Configurations

A major difference between *Commons Configuration* 1.x and 2.0 is
the way configuration objects are created, initialized, and managed. In
version 1.x configurations are created directly using their constructor.
Especially for file-based configuration implementations - like
`PropertiesConfiguration` or
`XMLConfiguration` - there were constructors which immediately
populated the newly created instances from a data source. If additional
settings were to be applied, this was done after the creation using
bean-like set methods. For instance, in order to create an initialized
`PropertiesConfiguration` object, the following code could be
used:

```

// Version 1.x: Initializing a properties configuration
PropertiesConfiguration config = new PropertiesConfiguration("myconfig.properties");
config.setThrowExceptionOnMissing(true);
config.setIncludesAllowed(false);
config.setListDelimiter(';');
```

While this code is easy to write, there are some non-obvious problems:

- Some settings influence the loading of the configuration data. In
  this example, the definition of the list delimiter and the
  *includesAllowed* flag fall into this category. However, because
  the data is directly loaded by the constructor these settings are
  applied too late and thus ignored by the load operation.
- The constructor calls a protected method for loading the data. This
  can lead to subtle bugs because at this time the instance is not yet
  fully initialized.
- The various set methods are not thread-safe; if this configuration
  instance is to be accessed from another thread, there may be problems.

To overcome these problems, *Commons Configuration* uses a
different approach for the creation of configuration objects based on
[configuration builders](#userguide-howto_builders). The basic idea
is that a configuration builder is created and initialized with all
parameters to be applied to the new configuration object. When the
configuration instance is queried from its builder it is guaranteed that
it has been fully initialized in the correct order. In addition, access
to configuration builders is thread-safe. Configuration builders offer a
fluent API for setting the initialization parameters for the configuration
to be created. The example above would become something like the
following in version 2.0:

```

FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
    new FileBasedConfigurationBuilder<PropertiesConfiguration>(PropertiesConfiguration.class)
    .configure(new Parameters().properties()
        .setFileName("myconfig.properties")
        .setThrowExceptionOnMissing(true)
        .setListDelimiterHandler(new DefaultListDelimiterHandler(';'))
        .setIncludesAllowed(false));
PropertiesConfiguration config = builder.getConfiguration();
```

Builders also offer an increased flexibility regarding the management of
configuration objects. While in version 1.x of *Commons Configuration*
typically `Configuration` objects were kept centrally and
accessed throughout an application, the recommended way in version 2.0 is
to work with configuration builders. A builder not only creates a new
configuration object but also caches a reference to it so that it can be
accessed again and again. This makes it possible to add special
functionality to the builder. For instance, it may decide to return a
different configuration object under certain circumstances - e.g. when a
change on an external configuration source is detected and a reload
operation is performed. For the application this is fully transparent.

Working with builders may seem a bit verbose at first. There are some ways
to simplify their usage. Be sure to read the section
[Making it easier](#userguide-howto_filebased--making_it_easier)
which describes some useful short cuts. It is also possible to define
default values for initialization parameters. This allows simplifying of
builder configurations and can establish application-global standard
settings for configuration objects. This mechanism is described in
[Default
Initialization Parameters](#userguide-howto_builders--default_initialization_parameters).

<a id="userguide-upgradeto2_0--reloading"></a>

## Reloading

Support for reloading of externally changed configuration sources was
limited in *Commons Configuration* 1.x. There was a reloading
strategy implementation that was triggered on each access to a
configuration property and checked whether an underlying file was changed
in the meantime. If this was the case, the configuration was automatically
reloaded. [CONFIGURATION-520](https://issues.apache.org/jira/browse/CONFIGURATION-520) contains a discussion about the problems and
limitations of this approach.

In version 2.0 reloading functionality has been completely redesigned.
The new approaches are described in the chapter
[Automatic Reloading of Configuration
Sources](#userguide-howto_reloading) of the user's guide. In a nutshell, [configuration builders](#userguide-howto_builders) play an important
role here. There are builder implementations available which can be
configured to monitor external configuration sources in a pretty generic
way. When a change is detected, the builder resets its managed configuration
so that the next time it is accessed a new instance is created. In addition, an event can be generated notifying the application that new configuration
information might be available. The whole mechanism can be setup to
perform reloading checks periodically and automatically in a background
thread.

The `FileChangedReloadingStrategy` class from version 1.0
no longer exists. It is replaced by the new, more powerful reloading
mechanisms. The mentioned chapter about [reloading](#userguide-howto_reloading)
describes in detail how a reloading-aware configuration builder can be
setup and fine-tuned to an application's needs.

<a id="userguide-upgradeto2_0--combining-configuration-sources"></a>

## Combining Configuration Sources

In *Commons Configuration* 1.x, there were two options for
creating a
[combined
configuration](#userguide-howto_combinedbuilder--combining_configuration_sources) out of multiple sources:

- The already deprecated `ConfigurationFactory` class
- The `DefaultConfigurationBuilder` class

The former has been removed. The functionality provided by
`DefaultConfigurationBuilder` is still available, but the
class has been renamed to
`CombinedConfigurationBuilder` (the old name was no longer
appropriate as builders are now a common concept in the library) and
adapted to other builder implementations.

In version 1.x `DefaultConfigurationBuilder` inherited from
`XMLConfiguration` - it was itself a configuration and could be
populated dynamically. `CombinedConfigurationBuilder` in
contrast is a regular builder implementation. In its initialization
parameters it can be passed another builder object from which the
definition for the combined configuration is obtained. So a dynamic
approach is possible here as well. In both cases, the
`getConfiguration()` method is used to obtain the
`CombinedConfiguration` object constructed by the builder. From
a usage point of view there is not that much difference between these
classes.

In both the old and the version, a XML-based definition file is used to
declare the different configuration sources that are to be combined plus
some additional settings. The principle structure of this file has not
changed - the full description of the new format is available at
[Configuration
definition file reference](#userguide-howto_combinedbuilder--configuration_definition_file_reference).

A problem when migrating from `DefaultConfigurationBuilder` to
`CombinedConfigurationBuilder` is that those definition files
can contain [bean definitions](#userguide-howto_beans), i.e. references
to classes which will be automatically instantiated by *Commons
Configuration*. Because of the change of the package name definition files
written for version 1.x will not work with the new version if they make
use of this feature and reference internal classes shipped with the
library. Here the fully-qualified class names in definition files have to
be adapted.

A prominent example of bean definitions were reloading strategies assigned
to specific configuration sources. As the whole reloading mechanism has
changed significantly, such declarations are no longer supported. There is
a much simpler replacement: just add the *config-reload* attribute
to a configuration source declaration to enable reloading support for this
source.

Another incompatible change is related to the extensibility of the
definition file format. It used to be possible - and still is - to define
custom tags for declaring special configuration sources. This is done by
registering provider objects at the configuration builder. Because the
internal implementation of `CombinedConfigurationBuilder` is
very different from the old one, this also affects the interface used for
providers. The main difference is that providers for the old version used
to create configuration objects directly, while the new providers create
configuration builders. If custom providers have been used in the past, additional migration effort has to be planned in.

A complete description of `CombinedConfigurationBuilder`, its
usage and supported extension points can be found in chapter
[Combining Configuration Sources](#userguide-howto_combinedbuilder)
of the user's guide.

<a id="userguide-upgradeto2_0--concurrency-issues"></a>

## Concurrency Issues

An important design goal of *Commons Configuration* 2.0 was to
improve the behavior of configuration objects when accessed by multiple
threads. In the 1.x series, support for concurrent access to configuration
data has grown historically: The original intent was that a configuration
object can be read by multiple threads in a safe way, but as soon as one
thread modifies the data, the user has to ensure proper synchronization
manually. Later on, also due to the reloading implementation, more and
more synchronization was added. This even caused performance bottlenecks, for instance as reported in
[CONFIGURATION-530](https://issues.apache.org/jira/browse/CONFIGURATION-530).

The changes in version 2.0 related to multi-threading include multiple
aspects. The most obvious change is probably that synchronization of
configurations is now much more flexible. A configuration instance is
assigned a
`Synchronizer` object which controls if and how locks are obtained
when executing operations on this configuration. By changing the
synchronizer, an application can adapt the locking behavior to its specific
needs. For instance, if a configuration is only accessed by a single
thread, there is no need for any synchronization. Typical usage modes are
reflected by different default implementations of the
`Synchronizer` interface:

- `NoOpSynchronizer` does not use any synchronization at all.
  This is the option of choice for single-threaded access, but fails in a
  multi-threaded environment.
- `ReadWriteSynchronizer` implements synchronization based on a
  read/write lock.

Note that the default option is `NoOpSynchronizer`. This means
that configuration objects are not thread-safe per default! You have to
change the synchronizer in order to make them safe for concurrent access.
This can be done for instance by using a builder which is configured
accordingly.

Talking about builders: This is another concept which supports access to
configuration data by multiple threads. Access to a builder is always
thread-safe. By shifting the responsibility for reloading operations from
the configuration to the builder, the need for intensive locking on each
property access could be eliminated.

Hierarchical configurations derived from
`BaseHierarchicalConfiguration` now use a new implementation
which allows for concurrent access without locking. So this group of
configurations can be used without having to set a fully-functional
synchronizer.

There are some other changes on classes with the goal to make them
well-behaving citizens in a concurrent environment. This includes:

- Some classes have been made immutable, passing all information to the
  constructor rather than using bean-style properties for their
  initialization. An example is
  `DefaultExpressionEngine` whose instances can now be shared between
  different hierarchical configuration objects.
- Static utility classes with state have been rewritten so that they
  can be instantiated. Mutable static fields are in general
  thread-hostile. Refer to
  [CONFIGURATION-486](https://issues.apache.org/jira/browse/CONFIGURATION-486)
  for further details.

Please refer to [Configurations and
Concurrent Access](#userguide-howto_concurrency) for a full description of this complex topic.

<a id="userguide-upgradeto2_0--events"></a>

## Events

Another area in which major changes took place is the support for
[event notifications](https://commons.apache.org/proper/commons-configuration/userguide/howto_events.html). *Commons
Configuration* 1.x had two types of event listeners for configuration
update events and error events. Version 2.0 adds some more event sources -
events generated by configuration builders and reloading events. Despite
this increased number of event sources, there is now only a single event
listener interface
(`EventListener`), and the mechanisms for adding and removing event
listeners are the same everywhere; the basic protocol is defined by the
`EventSource` interface. (Note that `EventSource` used
to be a class in version 1.x; it actually was the base class of
`AbstractConfiguration` and therefore inherited by all concrete
configuration implementations. In version 2.0 this role has been taken
over by the `BaseEventSource` class.)

While the old version used numeric constants to define specific event types, the new events are classified by instances of the
`EventType` class. Event types can be used to determine the
semantic meaning of an event, but also for filtering for specific events.
They stand in a logic hierarchical relation with each other; an event
listener that is registered for a base event type also receives notifications
for derived types. This makes a flexible and fine-grained event processing
possible. The whole event mechanism is very similar to the one implemented
in JavaFX.

The most basic use case for event listeners in version 1.x was probably
the registration of a change listener at a single configuration instance.
To achieve an equivalent effect with the new API, one would implement an
event listener and register it for the event type
`ConfigurationEvent.ANY`. This listener will then receive
notifications for all kinds of updates performed on the monitored
configuration. Structure and content of these events is nearly
identical to the counterparts in version 1.x.

There is, however, an important difference with the event listener
registration: The recommended way is to add the listener to the
[configuration builder](#userguide-upgradeto2_0--creating_configurations) which
creates the configuration rather than to the configuration itself. This
ensures that registration is done at the correct moment in time and also
updated when the builder decides to replace its managed configuration
instance.

All in all the new event mechanism should be much more flexible and
powerful than the old one.

---

<a id="userguide-upgradeto2_x"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/upgradeto2_x.html -->

<!-- page_index: 7 -->

<a id="userguide-upgradeto2_x--migration-guide-between-2.x-versions"></a>

# Migration Guide Between 2.x Versions

This document aims to assist with the migration between different versions
within the 2.x line. While all Commons Configuration artifacts maintain binary
compatibility with previous versions with the same major number, there are
some behavioral and/or configuration differences that may need to be addressed when
upgrading.

<a id="userguide-upgradeto2_x--v2.8.0"></a>

## v2.8.0

Version 2.8.0 of *Commons Configuration* introduced a change in the variable interpolation lookups
included by default. In previous versions, all lookups defined in the
`DefaultLookups`
enum were included by default. With version 2.8.0, some of these lookups are disabled.
Specifically, the
`dns`, `url`, and
`script`
lookups must now be enabled explicitly. As described in the
[user guide](#userguide-howto_basicfeatures--default_interpolation_lookups), this can be done either
programmatically or through a system property. If the behavior of previous versions must be maintained exactly
without changes to the code, then the following system property can be used:

```

org.apache.commons.configuration2.interpol.ConfigurationInterpolator.defaultPrefixLookups=BASE64_DECODER,BASE64_ENCODER,CONST,DATE,DNS,ENVIRONMENT,FILE,JAVA,LOCAL_HOST,PROPERTIES,RESOURCE_BUNDLE,SCRIPT,SYSTEM_PROPERTIES,URL,URL_DECODER,URL_ENCODER,XML
```

If the disabled lookups listed above are not used by the target application, then no changes are required.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/project-info.html -->

<!-- page_index: 8 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Commons Configuration software library provides a generic configuration interface that enables an application to read configuration data from various sources and requires Java 8. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-configuration/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-configuration/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-configuration/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-configuration/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-configuration/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-configuration/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-configuration/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/summary.html -->

<!-- page_index: 9 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Configuration |
| Description | The Commons Configuration software library provides a generic configuration interface that enables an application to read configuration data from various sources and requires Java 8. |
| Homepage | [https://commons.apache.org/proper/commons-configuration/](#index) |

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
| ArtifactId | commons-configuration2 |
| Version | 2.15.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/team.html -->

<!-- page_index: 10 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | mpoeschl | Martin Poeschl | [mpoeschl@marmot.at](mailto:mpoeschl@marmot.at) | - | tucana.at | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | dion | dIon Gillard | [dion@multitask.com.au](mailto:dion@multitask.com.au) | - | Multitask Consulting | - | Java Developer | - |
| ![](assets/images/126d93a0374e9fa5faa40527b2faa177_7fdd665d93e3d4ea.jpg) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | epugh | Eric Pugh | [epugh@upstate.com](mailto:epugh@upstate.com) | - | upstate.com | - | Java Developer | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | bdunbar | Brian E. Dunbar | [bdunbar@dunbarconsulting.org](mailto:bdunbar@dunbarconsulting.org) | - | dunbarconsulting.org | - | Java Developer | - |
| ![](assets/images/8304c64641badd4218a89a5f97d2ae86_77b1b0d2c138f6ee.jpg) | ebourg | Emmanuel Bourg | [ebourg@apache.org](mailto:ebourg@apache.org) | - | Ariane Software | - | Java Developer | +1 |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | oheger | Oliver Heger | [oheger@apache.org](mailto:oheger@apache.org) | - | Bosch Software Innovations | - | Java Developer | +1 |
| ![](assets/images/b57f757efea9e04ad3a5cb489499ec01_f6a52f7a08b191a0.jpg) | joehni | Jörg Schaible | [joerg.schaible@gmx.de](mailto:joerg.schaible@gmx.de) | - | - | - | Java Developer | +1 |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | rgoers | Ralph Goers | [rgoers@apache.org](mailto:rgoers@apache.org) | - | Intuit | - | Java Developer | -8 |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | claudenw | Claude Warren | [claude@apache.org](mailto:claude@apache.org) | - | - | - | Java Developer | 0 |
| ![](assets/images/a010ac0916b6b9b10883e9359cfcd7f9_51479c81d891bafa.jpg) | chtompki | Rob Tompkins | [chtompki@apache.org](mailto:chtompki@apache.org) | - | - | - | Java Developer | -4 |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | Konstantin Shaposhnikov | [ksh@scand.com](mailto:ksh@scand.com) | scand.com | - | - | - |
| ![](assets/images/6d77b357b99fe3b791235b1f7ebac068_398ea4788493cfa6.jpg) | Jamie M. Guillemette | [JMGuillemette@gmail.com](mailto:JMGuillemette@gmail.com) | TD Bank | - | - | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | Jorge Ferrer | [jorge.ferrer@gmail.com](mailto:jorge.ferrer@gmail.com) | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | Gabriele Garuglieri | [gabriele.garuglieri@infoblu.it](mailto:gabriele.garuglieri@infoblu.it) | Infoblu S.p.A | - | - | - |
| ![](assets/images/2983ff4b1cfdd190e9a42e1e6c6e7327_bf66c8e0ddba0c1f.jpg) | Nicolas De Loof | [nicolas.deloof@gmail.com](mailto:nicolas.deloof@gmail.com) | Cap Gemini | - | - | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | Oliver Kopp | [koppdev@gmail.com](mailto:koppdev@gmail.com) | - | - | - | - |
| ![](assets/images/6da8b0926ce146bee20982ffcb57f11b_dc14bc8575be8ec6.jpg) | Dennis Kieselhorst | [deki@apache.org](mailto:deki@apache.org) | IRIAN Deutschland | - | - | - |
| ![](assets/images/4b10f95b68fb001e4880b477a41bd5a1_51698ce365874a55.jpg) | Raviteja Lokineni | [raviteja.lokineni@gmail.com](mailto:raviteja.lokineni@gmail.com) | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | Vincent Maurin | [vincent.maurin.fr@gmail.com](mailto:vincent.maurin.fr@gmail.com) | glispa GmbH | - | - | - |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | The Alchemist | [kap4020@gmail.com](mailto:kap4020@gmail.com) | - | - | - | - |
| ![](assets/images/0db3f413e4b5f2f1d2f16852ce719089_fd4c201bbe643d3d.jpg) | Pascal Essiembre | [pascal.essiembre@norconex.com](mailto:pascal.essiembre@norconex.com) | Norconex Inc. | <https://www.norconex.com> | developer | -4 |
| ![](assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg) | Patrick Schmidt | [patrick.schmidt@codecamp.de](mailto:patrick.schmidt@codecamp.de) | - | - | - | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/ci-management.html -->

<!-- page_index: 11 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-configuration/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="userguide-howto_basicfeatures"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_basicfeatures.html -->

<!-- page_index: 12 -->

<a id="userguide-howto_basicfeatures--basic-features-and-abstractconfiguration"></a>

# Basic features and AbstractConfiguration

The `Configuration` interface defines a whole bunch of methods.
Implementing these methods all from scratch can be quite hard. Because of
that the `AbstractConfiguration` class exists. This class serves as a
common base class for most of the `Configuration` implementations
in *Commons Configuration* and provides a great deal of the
functionality required by the interface. So for creating a custom
`Configuration` implementation this class will be a good
starting point.

In addition to base implementations for lots of the methods declared in
the `Configuration` interface the `AbstractConfiguration`
class provides some other handy and convenient features. Because this
class is at the very root of the class hierarchy in *Commons
Configuration* these features are available in most of the specific
implementations of the `Configuration` interface provided by
this library. We will cover some of these basic features in this section.

<a id="userguide-howto_basicfeatures--handling-of-missing-properties"></a>

## Handling of missing properties

What is a configuration object supposed to do if you pass in a key to one
of its get methods that does not map to an existing property? Well, the
default behavior as implemented in `AbstractConfiguration` is
to return **null** if the return value is an object type. For primitive
types as return values returning **null** (or any other special
value) is not possible, so in this case a `NoSuchElementException`
is thrown:

```

// This will return null if no property with key "NonExistingProperty" exists
String strValue = config.getString("NonExistingProperty");

// This will throw a NoSuchElementException exception if no property with
// key "NonExistingProperty" exists
long longValue = config.getLong("NonExistingProperty");
```

For object types like `String`, `BigDecimal`, or
`BigInteger` this default behavior can be changed: If the
`setThrowExceptionOnMissing()` method is called with an
argument of **true**, these methods will behave like their primitive
counter parts and also throw an exception if the passed in property key
cannot be resolved.

*Note:* Unfortunately support for the `throwExceptionOnMissing`
property is not always consistent: The methods `getList()` and
`getStringArray()` do not evaluate this flag, but return an
empty list or array if the requested property cannot be found. Maybe this
behavior will be changed in a future major release.

<a id="userguide-howto_basicfeatures--list-handling"></a>

## List handling

With `getList()` and `getStringArray()` the
`Configuration` interface defines methods for dealing with
properties that have multiple values. When a configuration source (e.g.
a properties file, an XML document, or a JNDI context) is processed the
corresponding `Configuration` implementation detects such
properties with multiple values and ensures that the data is correctly
stored.

When modifying properties the `addProperty()` and
`setProperty()` methods of `AbstractConfiguration`
also implement special list handling. The property value that is passed
to these methods can be a list or an array resulting in a property
with multiple values.

For some use cases it makes sense to treat string values in a special way.
For instance, some configuration formats do not support lists directly.
As an example, properties files can be used: they just consist of
key-value pairs, and there is no default syntax to assign multiple values
to a key. `AbstractConfiguration` supports a mechanism to split
strings at specific characters, so that effectively multiple values are
generated from a single string. To achieve this, an
`AbstractConfiguration` instance collaborates with an object
implementing the
`ListDelimiterHandler` interface. This interface defines methods
for dealing with objects that may contain multiple values. Examples of
such complex objects are arrays, lists, and strings containing a specific
list delimiter. Depending on a concrete implementation of the
`ListDelimiterHandler` interface, these objects are treated in
a special way.

Per default, `AbstractConfiguration` uses an instance of the
`DisabledListDelimiterHandler` class as list handler. This
class can deal with lists and arrays, but it does not recognize any list
delimiter characters in strings. (Hence the name, as splitting of strings
at list delimiters is disabled.)

An alternative implementation of `ListDelimiterHandler` is
`DefaultListDelimiterHandler`. This class actually supports
string splitting; the list delimiter character has to be passed to the
constructor. Whenever a property is added to the configuration (or the
configuration is loaded from its source), it is checked whether the
property value is a string and - if so - if it contains the list
delimiter character. In this case, the string is split, and its single
parts are added one by one. By using the `setListDelimiterHandler()`
method you can set a specific list handler implementation. Here are some
examples:

```

// Enable list delimiter handling using a slash as delimiter character
config.setListDelimiterHandler(new DefaultListDelimiterHandler('/'));
// Now add some properties
config.addProperty("greeting", "Hello, how are you?");
config.addProperty("colors.pie",
  new String[] { "#FF0000", "#00FF00", "#0000FF" });
config.addProperty("colors.graph", "#808080/#00FFCC/#6422FF");

// Access data
String salut = config.getString("greeting");
List<Object> colPie = config.getList("colors.pie");
String[] colGraph = config.getStringArray("colors.graph");

String firstPieColor = config.getString("colors.pie");
```

In this example splitting of strings is enabled using the slash character
as delimiter. Because this character is not contained in the
`greeting` property it won't be split, but remains a single
string. In contrast, the string passed as value for the
`colors.graph` property contains the delimiter character and
thus will result in a property with three values. Note that the
version of the `getList()` method used here returns lists of type
`Object`. This is because the concrete class of the values of a
property is not known. For instance, if you call
`addProperty("answer", 42)`, an
`Integer` object will be stored in the configuration. However, there are overloaded versions of `getList()` supporting a
data type conversion to a specific target class (see below).

Of interest is also the last line of the example fragment. Here the
`getString()` method is called for a property that has
multiple values. This call will return the first value of the list.

One word of warning at the end: Be careful when changing the list
delimiter handler on a configuration which already contains values. List
handling is typically applied already when properties are added to the
configuration. If later another handler is set which processes lists
differently, results may be unexpected; some operations may even cause
exceptions!

<a id="userguide-howto_basicfeatures--variable-interpolation"></a>

## Variable Interpolation

If you are familiar with Ant or Maven, you have most certainly already encountered
the variables (like `${token}`) that are automatically expanded when the
configuration file is loaded. Commons Configuration supports this feature as well, here is an example (we use a properties file in this example, but other
configuration sources work the same way; you can learn more about
properties files in the chapter [Properties
files](#userguide-howto_properties)):

```

application.name = Killer App
application.version = 1.6.2

application.title = ${application.name} ${application.version}
```

If you now retrieve the value for the `application.title`
property, the result will be `Killer App 1.6.2`. So per default
variables are interpreted as the keys of other properties. This is only a
special case, the general syntax of a variable name is
`${prefix:name}`. The prefix tells Commons Configuration that
the variable is to be evaluated in a certain context. We have already seen
that the context is the current configuration instance if the prefix is
missing. The following table lists a few of the prefixes supported by default.
(See the next section for more details.)

| Prefix | Description |
| --- | --- |
| sys | This prefix marks a variable to be a system property. Commons Configuration will search for a system property with the given name and replace the variable by its value. This is a very easy means for accessing the values of system properties in every configuration implementation. |
| const | The `const` prefix indicates that a variable is to be interpreted as a constant member field of a class (i.e. a field with the **static final** modifiers). The name of the variable must be of the form `<full qualified class name>.<field name>`. The specified class will be loaded and the value of this field will be obtained. |
| env | Variables can also reference OS-specific environment properties. This is indicated by the `env` prefix. |

Here are some examples (again using properties syntax):

```

user.file = ${sys:user.home}/settings.xml

action.key = ${const:java.awt.event.KeyEvent.VK_CANCEL}

java.home = ${env:JAVA_HOME}
```

Below is some more information related to variable interpolation users
should be aware of:

- If a variable cannot be resolved, e.g. because the name is invalid
  or an unknown prefix is used, it won't be replaced, but is returned as
  is including the dollar sign and the curly braces.
- References to variables can be nested; a variable can refer to a
  variable which in turn can have references to other variables and so
  on.
- Cyclic references are detected. In this case, no interpolation is
  done.
- Variable interpolation happens when properties are queried from the
  configuration, not at creation time. Therefore, the mechanism is quite
  dynamic: changes on one property can impact the value of another
  property that references the first one.
- Variable interpolation is done by all property access methods. One
  exception is the generic `getProperty()` method which
  returns the raw property value.

<a id="userguide-howto_basicfeatures--default-interpolation-lookups"></a>

## Default interpolation lookups

Commons configuration comes with a number of default prefix interpolators in addition
to the few demonstrated above. The full list can be found in the documentation of
the `ConfigurationInterpolator.getDefaultPrefixLookups()` method. This method returns a map of
standard interpolation lookup objects keyed by prefix, which are enabled by default in all
interpolation operations performed through the `Configuration` interface. Prior to version
`2.8.0`, this map was constant. However, starting in version `2.8.0`, the lookups
included in this map can be optionally configured via system property, allowing users greater control over the
types of interpolation performed in their applications. The system property in question is named
`org.apache.commons.configuration2.interpol.ConfigurationInterpolator.defaultPrefixLookups`
and is expected to contain a comma-separated list of names from the
`DefaultLookups`
enum. For example, launching an application with the system property given below will only enable the
`sys` and `env` lookups.

```

org.apache.commons.configuration2.interpol.ConfigurationInterpolator.defaultPrefixLookups=SYSTEM_PROPERTIES,ENVIRONMENT
```

It is also important to note that starting in version `2.8.0`, several previously enabled
default lookups were changed to be disabled by default. These include the
`dns`, `url`, and
`script` lookups.
These lookups are still present in the library but must be explicitly enabled by either

1. listing them in the system property described above (along with all other enabled lookups), or
2. adding them programmatically using the techniques laid out in the next section.

Users who do not make use of these disabled lookups do not need to make any changes to their code or
deployment scripts when upgrading from previous versions to `2.8.0`.

<a id="userguide-howto_basicfeatures--customizing-interpolation"></a>

## Customizing interpolation

This sub section goes a bit behind the scenes of interpolation and
explains some approaches for adding your own interpolation facilities.
Under the hood the implementation of interpolation relies on objects
implementing the
`Lookup` interface. `Lookup` defines a simple
`lookup()` method that must be implemented by custom
implementations; it expects the name of a variable as argument and
returns the corresponding value. The standard prefixes for variables we
have covered so far are indeed provided by special classes implementing
`Lookup`.

It is now possible to create your own implementation of `Lookup`
and configure a [configuration builder](https://commons.apache.org/proper/commons-configuration/userguide/howto_builder.html)
(builders are introduced in the next chapter of this user's guide) to
make it available for all configuration objects it creates under a custom
prefix. We will show how this can be achieved. The first step is to
create a new class implementing `Lookup`, which must
define the `lookup()` method. As an example we implement a
rather dull lookup object that simply returns a kind of "echo"
for the variable passed in:

```
import org.apache.commons.configuration2.interpol.Lookup;
public class EchoLookup implements Lookup {@Override public Object lookup(String varName) {return "Value of variable " + varName;}}
```

Now we want this class to be called for variables with the prefix
`echo`. For this purpose the `EchoLookup` class
has to be registered at the
`ConfigurationInterpolator` instance of our configuration with
the desired prefix. Each `Configuration` object is associated
with a `ConfigurationInterpolator` object that handles variable
interpolation. It manages the `Lookup` objects that should be
used to resolve variables.

There are multiple ways to make a `Lookup` object known to a
`ConfigurationInterpolator`. The most direct way is to call
the interpolator's `registerLookup()` method passing in the
`Lookup` and the desired prefix:

```

// simple, but not recommended approach
ConfigurationInterpolator interpolator = config.getInterpolator();
interpolator.registerLookup("echo", new EchoLookup());
```

This approach works, but has some drawbacks, especially when used with
advanced features like reloading of configurations. The recommended way
is to set custom lookup objects via the builder which creates the
configuration object; this ensures that every `Configuration`
instance created via the builder has a correctly initialized
`ConfigurationInterpolator` object. To achieve this, create
a map using the variable prefixes as keys and the associated
`Lookup` objects as values. This map can then be passed to the
`setPrefixLookup()` method of a parameters object for the
builder. Note that the lookups for the default prefixes are added
explicitly; omitting a lookup would remove support for the corresponding
prefix:

```

// Create a map with defaults and one additional lookup
Map<String, Lookup> lookups = new HashMap<String, Lookup>(
    ConfigurationInterpolator.getDefaultPrefixLookups());
lookups.put("echo", new EchoLookup());

// Configure builder with lookups
Parameters params = new Parameters();
BasicConfigurationBuilder<PropertiesConfiguration> builder =
        new BasicConfigurationBuilder<PropertiesConfiguration>(
                PropertiesConfiguration.class)
                .configure(params.basic()
                        .setPrefixLookups(lookups);
PropertiesConfiguration config = builder.getConfiguration();
```

<a id="userguide-howto_basicfeatures--using-expressions"></a>

## Using Expressions

In addition to the simple lookup mechanisms previously described, Commons Configuration
provides `ExprLookup` which uses [Apache
Commons Jexl](https://commons.apache.org/jexl) to allow expressions to be resolved wherever a StrLookup is allowed. This
example shows an alternate way of obtaining a system property if the ExprLookup is
configured.

```

user.file = ${expr:System.getProperty("user.home")}/settings.xml
```

`ExprLookup` is not enabled by default, it must be manually added or configured via
`DefaultConfigurationBuilder`. Builds that use Maven 2 and reference Commons
Configuration will not include a dependency on Jexl, so if this feature is used the
dependency on Jexl must be manually added to the project.

When using `DefaultConfigurationBuilder` adding `ExprLookup` is
straightforward.

```

<configuration>
  <header>
    <result/>
    <lookups>
      <lookup config-prefix="expr"
              config-class="org.apache.commons.configuration2.interpol.ExprLookup">
        <variables>
          <variable name="System" value="Class:java.lang.System"/>
          <variable name"net" value="Class:java.net.InetAddress"/>
          <variable name="String" value="Class:org.apache.commons.lang.StringUtils"/>
        </variables>
      </lookup>
    </lookups>
  </header>
  <override>
    <xml fileName="${expr:System.getProperty('basePath') +
         String.lowercase(net.localHost.hostName) + '/testMultiConfiguration_default.xml'}"
         config-name="defaultConfig" delimiterParsingDisabled="true">
    </xml>
  </override>
</configuration>
```

The example above shows how to invoke static methods during expression evaluation. The
next example shows mixing expression evaluation with a subordinate lookup to
obtain the "basePath" system property. Note the difference in how the
system property was obtained in the previous example.

```

<configuration>
  <header>
    <result/>
    <lookups>
      <lookup config-prefix="expr"
              config-class="org.apache.commons.configuration2.interpol.ExprLookup">
        <variables>
          <variable name"net" value="Class:java.net.InetAddress"/>
          <variable name="String" value="Class:org.apache.commons.lang.StringUtils"/>
        </variables>
      </lookup>
    </lookups>
  </header>
  <override>
    <xml fileName="${expr:$[sys:basePath] +
         String.lowercase(net.localHost.hostName) + '/testMultiConfiguration_default.xml'}"
         config-name="defaultConfig" delimiterParsingDisabled="true">
    </xml>
  </override>
</configuration>
```

<a id="userguide-howto_basicfeatures--data-type-conversions"></a>

## Data type conversions

As was already mentioned when discussing the
`Configuration` interface, there are various `get()`
methods returning property values in different target data types. If
necessary, a data type conversion is performed. Take a look at the
following example:

```

config.addProperty("answer", "42");
int theAnswer = config.getInt("answer");
```

Here a string value is assigned to the key *answer*. Then the
`getInt()` method is called to query this key as an integer
value. `getInt()` triggers a type conversion automatically.
If such a conversion is not possible, a runtime exception of type
`ConversionException` is thrown.

The `Configuration` interface defines a bunch of methods
returning property values in different data types. All of these methods
work in the same way: they obtain the actual value of the property and
attempt a data type conversion if necessary. In addition, there are
generic methods for accessing properties in specific data types:

<T> get(Class<T> cls, String key);
:   Obtains the value of the specified property and tries to convert it
    to the specified target type. If the key cannot be resolved, result is
    **null**, or - if the *throwExceptionOnMissing* flag is set -
    an exception is thrown.

<T> get(Class<T> cls, String key, T defValue);
:   Obtains the value of the specified property and tries to convert it
    to the specified target type. If the key cannot be resolved, the
    specified default value is returned (which may be **null**).

In fact, all specialized `get()` methods are based on these
generic methods.

Generic conversion methods are also available for obtaining arrays or
collections. For instance, it is possible to obtain the value of a
property as an array of **int** or a list of `java.lang.Long`
objects. For arrays these conversions are directly supported by the generic
`get()` methods: if the target type passed to the method is an
array class, an array conversion is done automatically. So to obtain an
array of **int** from a configuration, the following code
can be used:

```

int[] result = config.getInt(int[].class, "myIntArrayKey");
```

For conversions to collections specific methods are provided (this is
necessary because the element type of the collection cannot be
determined automatically as in case of arrays). These are the following
ones:

<T> List<T> getList(Class<T> cls, String key);
:   Returns a list of the specified element class.

<T> Collection<T> getCollection(Class<T> cls, String key, Collection<T> target);
:   This method is similar to `getList()`, but it allows
    specifying the target collection. This is useful if the result should
    be stored in a different collection type, e.g. a set to remove
    duplicates.

These methods obtain all values stored for the property with the
passed in key. For each value a conversion to the desired target type is
performed. Then the resulting values are stored in the target array or
collection. There are also variants supporting default values.

It is worth to mention that data type conversion plays well together with
[variable interpolation](#userguide-howto_basicfeatures--variable_interpolation): Before a
data type conversion is attempted interpolation is handled first. Then
the resulting object is converted if necessary.

<a id="userguide-howto_basicfeatures--customizing-data-type-conversions"></a>

## Customizing data type conversions

*Commons Configuration* supports a number of conversions to
standard types out of the box. In addition to the result types of the
`get()` methods in the `Configuration` interface, some more types are supported. These are listed in the documentation of the
`DataConfiguration` class. `DataConfiguration` is a
*decorator* providing additional data type conversion methods for
more target types; these additional methods are implemented on top of the
generic conversion methods provided by `AbstractConfiguration`.

If your application deals with special objects, there may be the
requirement to extend the conversion capabilities offered by the
library. To support this use case, there is the
`ConversionHandler` interface. Each instance of a configuration
class derived from `AbstractConfiguration` is associated with
such a `ConversionHandler` object. The interface defines
methods for converting an object to a target class, and for converting
values to arrays or collections of a given element type. The data type
conversion methods implemented in `AbstractConfiguration`
delegate to this handler object.

The `ConversionHandler` interface gives a developer full
control over the whole data conversion process. By implementing the
different conversion methods, it is possible to integrate existing
conversion libraries (e.g. the converters offered by
[Commons
BeanUtils](https://commons.apache.org/proper/commons-beanutils/)) with *Commons Configuration*.

If the conversion facilities provided by *Commons Configuration*
are not to be fully replaced, but only extended by some custom types, the class `DefaultConversionHandler` is a good starting point. As the name
implies, an instance of this class is used per default for doing type
conversions. `DefaultConversionHandler` has some protected
methods which can be overridden by subclasses in order to extend data type
conversions:

`convertValue()`
:   This is the main conversion method for single values. It is called
    when a single value is to be converted to a target type and also for
    the single elements of arrays or collections. If a conversion to another
    target class is to be supported, this is the method to override. A
    custom implementation typically checks whether the desired target class
    is one of the classes it supports. If this is the case, the passed in
    source object is converted, and the result is returned. Otherwise, the
    super method is called to handle standard conversions.

`isComplexObject()`
:   This boolean method determines whether a passed in object contains
    multiple values. When doing a conversion to a target class
    `DefaultConversionHandler` checks whether the source object
    is a complex object like an array or a collection. If this is the case,
    it first extracts the value to be converted from the source object
    before it calls `convertValue()`.

`extractConversionValue()`
:   `extractConversionValue()` is called if a complex object
    (i.e. an object containing multiple values) is to be converted to a
    single object (i.e. not an array or a collection). In this case, it is
    not directly obvious how the multiple values should be handled. This
    situation occurs for example if a client calls `getInt()`
    on a property which actually has multiple values. The default
    implementation of `extractConversionValue()` simply returns
    the first value available. If an application needs a different
    behavior, it can provide a custom implementation of this method.

`convert()`
:   This method contains the logic for converting a single value. It
    delegates to the other methods discussed here. It first checks whether
    the object to be converted is a complex one. If so, it extracts the
    value to be converted. Eventually, it delegates to
    `convertValue()` for performing the actual conversion. So
    in order to gain more control over the whole conversion process, this
    method is a good candidate for overriding.

After a custom `ConversionHandler` implementation has been
created, it can be installed at a configuration instance by using the
`setConversionHandler()` method:

```

CustomConversionHandler handler = new CustomConversionHandler(...);
config.setConversionHandler(handler);
```

Another feature of `DefaultConversionHandler` is that is
allows defining the format for the conversion of `Date` and
`Calendar` objects. This can be done by calling
`setDateFormat()` with the corresponding date pattern. The
expected string argument must be a pattern string compatible with the
`java.text.SimpleDateFormat` class. If no date format was set, the default pattern `yyyy-MM-dd HH:mm:ss` is used.

<a id="userguide-howto_basicfeatures--encoded-properties"></a>

## Encoded Properties

Sometimes property values cannot be stored in plain text in configuration
files. For instance, security-related information like database passwords
should be encrypted. *Commons Configuration* does not provide
algorithms for encrypting (or otherwise encoding) properties. However, there is a generic mechanism for automatically reading encoded properties
and transforming them into plain text before they are handed over to the
caller. A key role in this mechanism plays the
`ConfigurationDecoder` interface.

`ConfigurationDecoder` defines a single method *decode()*
which expects a string as input and returns a decoded string. It should be
easy for an application to provide a custom implementation for the
encoding algorithm it uses. The
`ImmutableConfiguration` interface defines two overloaded methods
for querying the values of encoded properties:

```

    String getEncodedString(String key, ConfigurationDecoder decoder);

    String getEncodedString(String key);
```

Both methods operate on string properties. Basically, the string value for
the passed in key is retrieved by delegating to `getString()`.
This value is then passed to a `ConfigurationDecoder` to
obtain the plain text value. One of these methods expects the
`ConfigurationDecoder` to be used as argument. The other
variant makes use of a decoder associated with this configuration. For
this purpose
`AbstractConfiguration` offers a property named
*configurationDecoder*. Making use of this property simplifies
access to encoded properties: When the central configuration object is
created the decoder is initialized. Other parts of the application do not
need any knowledge about the decoding algorithm to be applied; rather, it
is sufficient to call the simple variant of `getEncodedString()`
to obtain a property value which can be processed immediately.

---

<a id="userguide-howto_beans"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_beans.html -->

<!-- page_index: 13 -->

<a id="userguide-howto_beans--declaring-and-creating-beans"></a>

# Declaring and Creating Beans

Often it is good practice to make heavy use of Java interfaces and program
an application or components against these interfaces rather than concrete
implementation classes. This makes it possible to switch to different implementations
without having to modify calling code. However, the problem remains how a
concrete implementation of an interface is obtained. Simply using the
**new** operator on a specific implementation class would somehow break
the interface concept because then the code would have an explicit reference
to a concrete implementation.

A solution to this problem is to define the concrete implementation class
that should be used in a configuration file. Client code would obtain an
object (or a bean) from the configuration and cast it to the service
interface. This way the caller would have no knowledge about which concrete
implementation is used; it would only interact with the service through
the interface. By changing the configuration file and entering a different
class name for the implementation class the behavior of the application
can be altered, e.g. to inject a test stub for the used service.

*Note: The concept of defining service objects in configuration files
and let them be created by a special container has grown popular these
days. Especially IoC containers like [Spring](https://www.springframework.org/) offer wide
functionality related to this topic. Commons Configuration is not and has
no ambitions to become an IoC container. The provided functionality for
declaring and creating beans is very basic and limited compared to the
specialists. So if you are in need of enhanced features like the creation
of complete networks of service objects, life cycle handling and such things, you should in any case use a real IoC container. For simple use cases
however the functionality of Commons Configuration might be sufficient, and we have tried to provide hooks for extending the predefined mechanisms.*

<a id="userguide-howto_beans--basic-concepts"></a>

## Basic Concepts

Beans (we use the term *bean* here to name any plain old Java
object that is defined in a configuration file and can be instantiated
by Commons Configuration) are defined in configuration files in a specific
format, a so-called *Bean declaration*. Such a declaration contains
all information needed to create an instance of this bean class, e.g.
the fully-qualified name of the class and initialization parameters. We will
explain how a bean declaration looks like in short.

On the Java side three entities are involved in the creation of a bean:

- A *bean factory*: This is an object that implements the
  `BeanFactory`
  interface and knows how to create an instance of a bean class. In most
  cases calling code does not directly deal with a bean factory.
- An implementation of the
  `BeanDeclaration`
  interface. This object knows how the bean declaration in the configuration
  file is organized and how the needed information can be extracted. So
  the way the bean is declared in the configuration file must match the
  expectations of this object.
- The helper class
  `BeanHelper`
  brings all these together and performs the bean creation operation.
  Usually client code will create a `BeanDeclaration` object
  from a `Configuration` implementation and then pass it to
  one of the `createBean()` methods of `BeanHelper`.
  That's it!

For all of the interfaces mentioned above default implementations are
provided, which in many cases can be used out of the box.

<a id="userguide-howto_beans--an-example"></a>

## An Example

After this theory let's get into practice using an example. Consider a
GUI application that makes use of a *Window manager* to display
its windows and dialogs to the user. There is a `WindowManager`
interface containing methods for opening, displaying, hiding, and
disposing windows. Different implementations of this interface exist, e.g.
providing different look & feel or special functionality. The concrete
set of methods of the interface does not matter for this example.

Now in the application's configuration it shall be specified that the
concrete implementation `DefaultWindowManager` should be
used as `WindowManager`. This is a plain Java class implementing
the `WindowManager` interface. Some fragments are shown in
the following listing:

```

package examples.windows;

public class DefaultWindowManager implements WindowManager
{
    // are windows allowed to be resized?
    private boolean resizable;
    // do windows have a close button?
    private boolean closable;

    // Default size of new windows
    private int defaultWidth;
    private int defaultHeight;

    WindowStyleDefinition styleDefinition;

    // getters and setters ommitted, also the WindowManager methods
}
```

As you can see, the `DefaultWindowManager` class has some
simple properties for defining the windows. There is also a property
named `StyleDefinition` whose type is another bean (such
a style definition may contain information about themes, colors, fonts
of the window and so on). How can we now write a configuration file so
that a bean of the `DefaultWindowManager` class is declared
and initialization properties are defined? In an XML configuration file
this will look as follows:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>
<config>
  <gui>
    <windowManager config-class="examples.windows.DefaultWindowManager"
      closable="false" resizable="true" defaultWidth="400"
      defaultHeight="250">
      <styleDefinition config-class="examples.windows.WindowStyleDefinition"
        backColor="#ffffff" foreColor="0080ff" iconName="myicon" />
    </windowManager>
  </gui>
</config>
```

This XML document contains a valid bean declaration starting with the
`windowManager` element and including its sub elements. Note
the following points:

- The (fully-qualified) class of the bean is specified using the
  `config-class` attribute. (Attributes starting with the
  prefix "config-" are reserved; they contain special meta
  data for the bean creation process.)
- Other attributes of the `windowManager` element correspond
  to properties of the `DefaultWindowManager` class. These
  properties will be initialized with the values specified here.
- For the `styleDefinition` property, which is itself a
  bean, a sub element (matching the property's name) exists. The structure
  of this element is analogous to the structure of the `windowManager`
  element; indeed it could even have further sub elements defining
  bean properties of the `WindowStyleDefinition` class.

The basic structure of a bean declaration should have become clear by
this example.

Now let's see how we can access this declaration and create an instance.
This is demonstrated in the code fragment below:

```

Parameters params = new Parameters();
FileBasedConfigurationBuilder<XMLConfiguration> builder =
    new FileBasedConfigurationBuilder<XMLConfiguration>(XMLConfiguration.class)
    .configure(params.xml()
        .setFileName("windowconfig.xml"));
XMLConfiguration config = builder.getConfiguration();
BeanDeclaration decl = new XMLBeanDeclaration(config, "gui.windowManager");
WindowManager wm = (WindowManager) BeanHelper.INSTANCE.createBean(decl);
```

This fragment loads the configuration file using a `XMLConfiguration`
object. Then a bean declaration object is created, in this case an
instance of the `XMLBeanDeclaration`
class, which can deal with bean declarations in XML documents. This
declaration is passed to the `createBean()` method of
the default instance of the
`BeanHelper`
class, which returns the new bean instance.

A `BeanHelper` object does the hard work behind the scenes to
create a bean instance. It determines the class of the bean to be
created and delegates to a `BeanFactory` to create an
instance. Then all initialization properties defined in the bean
declaration are evaluated and set on the newly created bean. The
`BeanFactory` to be used is determined based on the
bean helper's configuration:

- A `BeanHelper` can be configured with a number of
  `BeanFactory` objects that are registered under a specific
  key. The `BeanDeclaration` can contain the key of the
  `BeanFactory` to be used. Please refer to the
  Javadocs of `XMLBeanDeclaration` for further information.
- When a `BeanHelper` object is constructed a default
  `BeanFactory` is set. This one is used if no specific
  factory is referenced by the bean declaration.

If an application does not need special bean factories, it can use the
default `BeanHelper` instance which is available via the
static `INSTANCE` member field (as shown in the example
fragment above). This instance uses a
`DefaultBeanFactory` object as bean factory.
Otherwise, specialized `BeanHelper`
instances can be created that are configured with other bean factories.
A `BeanHelper` object is thread-safe and can be passed
around between the components of an application.

`BeanHelper` defines some overloaded versions of the
`createBean()` method. Some allow passing in a default bean
class; then it is not necessary to define the class in the bean declaration
- an instance of this default class will be created if it is missing in
the configuration file. If the bean cannot be created for some reason
(e.g. a wrong class name was specified), a `ConfigurationRuntimeException`
will be thrown.

<a id="userguide-howto_beans--constructor-arguments"></a>

## Constructor arguments

In the examples so far we assumed that beans are created using their
standard constructor. This is appropriate for classes conforming to the
Java Beans specification which requires bean classes to have such a
no-argument constructor. *Commons Configuration* also supports invoking
an arbitrary constructor passing in the corresponding constructor
arguments. Let's extend the example from the previous section and assume
that the `WindowStyleDefinition` class is now an immutable
class which has to be initialized by passing parameters to its
constructor. The constructor may look as follows:

```
public class WindowStyleDefinition {...public WindowStyleDefinition(String foreground, String background,Font stdFont) {...} ...}
```

In order to create an instance of `WindowStyleDefinition`, we have to pass the foreground and background colors and a standard
font to the constructor. The colors are simple strings while a font is
again a complex object. The following code fragment shows the complete
bean declaration for this scenario:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>
<config>
  <gui>
    <windowManager config-class="examples.windows.DefaultWindowManager"
      closable="false" resizable="true" defaultWidth="400"
      defaultHeight="250">
      <styleDefinition config-class="examples.windows.WindowStyleDefinition">
        <config-constrarg config-value="#0080ff"/>
        <config-constrarg config-value="#ffffff"/>
        <config-constrarg config-class="java.awt.Font">
          <config-constrarg config-value="Monospaced"/>
          <config-constrarg config-value="0"/>
          <config-constrarg config-value="12"/>
        </config-constrarg>
      </styleDefinition>
    </windowManager>
  </gui>
</config>
```

The *styleDefinition* property is still defined as a nested
bean declaration in the body of the `<windowManager>`
element. But this time there are nested
`<config-constrarg>` elements. Each element defines
one constructor argument. In this example there are three constructor
arguments for the foreground color, the background color, and the
standard font. The first two arguments are simple values (i.e. primitive
Java data types) and are defined using the `config-value`
attribute. The third argument, the font, is actually another nested
bean declaration. This is indicated by the presence of the
`config-class` attribute which defines the class of this
constructor argument. To create a `Font` instance, we again
have to define constructor arguments: the font name, its style, and its
size. Note that corresponding type conversions are performed
automatically; while all values in the XML configuration file are
strings, they are converted to the correct parameter type when calling
the constructor.

*Commons Configuration* uses a pretty simple algorithm to determine the
constructor to be invoked: it is mainly based on the number of
constructor arguments. This works as expected as long as there are not
multiple constructors with the same number of arguments. If this is
the case, the developer has to provide some hints indicating which
constructor to select. Consider a bean class with the following
constructors:

```
public class MyBean {...public MyBean(String svalue) {...}
public MyBean(int ivalue) {...} ...}
```

This bean class has two constructors expecting a single argument. A
bean declaration like the following one will not work because it is
not clear which constructor to choose:

```

<config>
  <!-- This will not work as the constructor is ambiguous! -->
  <bean config-class="examples.MyBean">
    <config-constrarg config-value="100"/>
  </bean>
</config>
```

The solution is to explicitly specify the data type (the fully-qualified
Java class) of the constructor argument. This can be done by adding
the `config-type` attribute as in the following fragment:

```

<config>
  <bean config-class="examples.MyBean">
    <config-constrarg config-value="100" config-type="int"/>
  </bean>
</config>
```

Now it is clear that the constructor expecting an `int`
argument is desired. The `config-type` attribute can be
used for both simple constructor arguments and nested bean
declarations. It does not have to be specified for all arguments; it
is sufficient to define a minimum number of data types so that there is
no ambiguity any more. The type specified for the attribute must be the
exact same type as expected by the constructor. This is not necessarily
the same type as the value passed to this argument. (For instance, the constructor expects an object implementing a specific interface, while the actual argument value is an instance of a concrete
implementation class.) Also, the `config-type` attribute is
only evaluated to determine a matching constructor; it is not related
to data type conversion.

<a id="userguide-howto_beans--extending-the-basic-mechanism"></a>

## Extending the Basic Mechanism

As was pointed out in the introduction of this chapter, support for creating
beans is focused on the basics. But there are some possibilities of hooking
in and add custom extensions. This can be done in the following ways:

- By defining a custom `BeanDeclaration` implementation
- By providing a custom `BeanFactory` implementation

A specialized bean declaration is needed when you have to deal with
configuration files that contain bean declarations in a different format
than the ones supported by the available default implementations. Then it
is the responsibility of your implementation to parse the configuration
data and extract the required information to create the bean. Basically
your `BeanDeclaration`
implementation must be able to provide the following data:

- The name of the class for which an instance is to be created.
- The name of the bean factory that is used to create the bean. Here
  **null** can be returned, then a default factory is used. (See
  below for more information about working with custom bean factories.)
- An optional parameter to be passed to the bean factory. If a factory
  is used that supports additional parameters, the current parameter
  values are also obtained from the bean declaration.
- A map with the properties to be set on the newly created bean.
  This map's keys are names of properties, its values are the corresponding
  property values. The default bean factory will process this map and
  call the corresponding setter methods on the newly created bean object.
- A map with further `BeanDeclaration` objects for
  initializing properties of the new bean that are itself beans. These
  bean declarations are treated exactly as the one that is currently
  processed. The resulting beans will then be set as properties on the
  processed bean (the names of these properties are again obtained from
  the keys of the map).

While creating a custom `BeanDeclaration` implementation
allows you to adapt the format of bean declarations in configuration files, you can manipulate the bean creation mechanism itself by creating a
specialized implementation of the
`BeanFactory`
interface. For this purpose the following steps are necessary:

1. Create a class implementing the `BeanFactory` interface.
   This interface is quite simple. It defines one method for creating an
   instance of a class whose `Class` object is provided, and
   another method, which is called for querying a default class.
2. Register this new factory class at the `BeanHelper`
   instanced used for bean creation.
3. In the bean declaration in your configuration file refer to the
   factory that should be used for creating the bean (unless this factory
   is used as the `BeanHelper`'s default bean factory).

We will provide an example that covers all these steps. This example
deals with a *singleton* factory, i.e. an implementation of
`BeanFactory` that returns always the same instance of a
provided bean class.

We start with the creation of the factory class. The basic idea is that
the functionality for creating and initializing beans is already provided
by the `DefaultBeanFactory`
class, so we extend this class. Our implementation only has to deal with
the singleton stuff: We keep a map that stores already created bean
instances and can be accessed by the name of their classes. In the
factory's `createBean()` method we check if for the passed in
class already an instance exists. If this is the case, it is directly
returned. Otherwise we call the inherited `createBean()` method
and store its result in the map. (Note that this implementation is a bit
simplistic. A real world implementation would also have to take
initialization parameters into account and use a more sophisticated
approach to deal with concurrency issues. But for the purpose of an
example it should be good enough). Here is the code:

```
public class SingletonBeanFactory extends DefaultBeanFactory {/** A map for the so far created instances.*/ private final Map<String, Object> beans;
public SingletonBeanFactory() {super(); beans = new HashMap<String, Object>();}
// Creates the bean. Checks if already an instance exists.public synchronized Object createBean(BeanCreationContext bcc) throws Exception {Object bean = beans.get(bcc.getBeanClass().getName()); if (bean != null) {// Yes, there is already an instance return bean;} else {// No, create it now (done by the super class) bean = super.createBean(bcc); // Store it in map beans.put(beanClass.getName(), bean); return bean;}}}
```

The main method to define is `createBean()`. It is passed
a `BeanCreationContext` object which contains all information
required for creating a bean (e.g. via reflection).
Note the **synchronized** key word, which is necessary because the
method can be accessed by multiple threads concurrently.

Now we have to register an instance of this class at a
`BeanHelper` instance. There are multiple ways how this can
be done. For applications making use of the default
`BeanHelper` instance, the factory can be added using the
`registerBeanFactory()` method. This can happen in the
initialization phase of your application and looks as follows:

```

BeanHelper.INSTANCE.registerBeanFactory("SINGLETON", new SingletonBeanFactory());
```

To make use of the new factory a bean declaration must contain an
attribute that refers to the name under which the factory was registered.
This is demonstrated by the fragment below:

```

<config>
...
    <services>
      <fileService config-class="my.package.services.FileServiceImpl"
        config-factory="SINGLETON"
        property1="value1" property2="value2">
        <!-- Here can be nested bean declarations -->
      </fileService>
      ...
</config>
```

In this fragment the `fileService` element contains a bean
declaration for some service object. Apart from the `config-class`
attribute the important part is the `config-factory` attribute.
This attribute tells the `BeanHelper` class that it should
use a special factory when it processes this bean declaration.

Alternatively, a separate `BeanHelper` instance can be
created passing in the new factory object as its default bean factory.
In the bean declarations, it is then no longer necessary to refer to
a specific bean factory. Below is an example showing this approach:

```

BeanHelper singletonBeanHelper = new BeanHelper(new SingletonBeanFactory());
BeanDeclaration decl = ... // somehow obtain the bean declaration
Object mySingletonBean = singletonBeanHelper.createBean(decl);
```

Of course, this new `BeanHelper` instance must now be used
everywhere where singleton beans are required. So it has to be made
available globally. Because a `BeanHelper` object is
thread-safe this can be done safely. As was demonstrated by this example, it should not be too difficult to extend the custom mechanism for
creating beans.

---

<a id="userguide-howto_builders"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_builders.html -->

<!-- page_index: 14 -->

<a id="userguide-howto_builders--creating-configurations"></a>

# Creating Configurations

Before a configuration and the data it contains can be accessed it has
to be created and initialized first. Although the concrete
`Configuration` implementations provided by *Commons
Configuration* typically have a public default constructor, instances should only be created directly in exceptional cases. The
recommended way is to use a *configuration builder*.

<a id="userguide-howto_builders--configuration-builders"></a>

## Configuration Builders

*Commons Configuration* defines the generic
`ConfigurationBuilder` interface which is used for creating
initialized configuration objects. The interface defines a
`getConfiguration()` method returning a generic type
derived from `Configuration`. Here a specific
`Configuration` implementation class can be inserted.

Note that the name of this method is `getConfiguration()` and
not `createConfiguration()`. This is because a builder is not
required to create a new instance on each invocation. Rather, a builder
is also responsible for managing the instance it has created. A basic
implementation may create its managed configuration once on first
access and will then always return the same instance in its
`getConfiguration()` method. A builder which is aware of
reloading in contrast may invalidate its managed configuration when it
detects that the content of the configuration has changed on disk; then
the next invocation of `getConfiguration()` returns an updated
configuration object. (Reloading is discussed in more detail in a later
section of this user's guide.) Builder implementations must be
thread-safe so that it is guaranteed that they behave correctly even if
accessed concurrently by multiple threads.

The recommended usage for accessing configuration data from multiple
parts of an application is to create a builder object initially and keep
a reference to it centrally. Whenever configuration information is needed
the builder is asked for its `Configuration` object; from
there the actual configuration settings can be obtained. While this
approach introduces another level of indirection, it enables the
application to add new functionality transparently by replacing the builder
implementation. For instance, if at a later stage the
requirement occurs to react on external changes of configuration data, the builder object can be replaced by a reloading-aware builder. This
enables support for reloading all over in the application immediately
without having to change anything.

<a id="userguide-howto_builders--basicconfigurationbuilder"></a>

## BasicConfigurationBuilder

*Commons Configuration* provides multiple concrete
`ConfigurationBuilder` implementations supporting different
features. The most basic implementation is
`BasicConfigurationBuilder`. It is the base class for all other
builder implementations and defines a framework for creating and
initializing configuration objects. The functionality provided is as
follows:

- When an instance of `BasicConfigurationBuilder` is
  constructed the class of the `Configuration` implementation
  to be created has to be passed. This class must be compatible with
  the generic type parameter of the builder.
- It is possible to set arbitrary initialization parameters for
  the configuration object to be created. Such parameters correspond to
  the special properties offered by the configuration class (e.g. the
  `throwExceptionOnMissing` flag, the object for handling
  lists, helper objects for variable interpolation, and so on).
- The `getConfiguration()` method checks whether the managed
  configuration instance has already been created. If so, it can be
  directly returned.
- If this is the first access to `getConfiguration()`,
  the managed configuration object is created. This is done via
  reflection: the configuration object is created, and all initialization
  parameters which have been set are applied.
- There is also a `reset()` method which removes the
  managed configuration instance. Calling this method causes a new
  instance to be created the next time `getConfiguration()`
  is invoked.

Note that these methods are all properly synchronized so that the builder
class is thread-safe.

The following code fragment shows how a `BasicConfigurationBuilder`
can be used to create an empty `PropertiesConfiguration`
object. At this stage of the discussion, the details of this example will
not yet be understandable; they will be explained in the following
sections. This is just to get a feeling how the usage of configuration
builders looks like in practice:

```

Parameters params = new Parameters();
BasicConfigurationBuilder<PropertiesConfiguration> builder =
        new BasicConfigurationBuilder<PropertiesConfiguration>(
                PropertiesConfiguration.class)
                .configure(params.basic()
                        .setListDelimiterHandler(
                            new DefaultListDelimiterHandler(','))
                        .setThrowExceptionOnMissing(true));
PropertiesConfiguration config = builder.getConfiguration();
```

<a id="userguide-howto_builders--initialization-parameters"></a>

## Initialization Parameters

Depending on the concrete `Configuration` class to be
instantiated, it can be necessary to set a bunch of initialization
parameters. In order to simplify this and make the code somewhat
concise, a fluent API is provided for setting initialization parameters.
Basically, initialization parameters are defined by POJOs (plain old
Java objects) with properties corresponding to the special properties
supported by the configuration object to be created. In the package
`org.apache.commons.configuration2.builder.fluent` a number
of interfaces is contained defining the possible initialization
parameters for the standard `Configuration` implementations
shipped with *Commons Configuration*. These interfaces form a
natural inheritance hierarchy corresponding to the inheritance graph
used by concrete `Configuration` implementations. So there is
a fundamental set of initialization parameters supported by all classes
derived from
`AbstractConfiguration`. Configurations loaded from a file
also support these parameters plus additional ones for defining the file
to be loaded. An XML-based configuration supports all basic and
file-related parameters plus specific parameters defining its specific
properties, and so on.

Exposing such parameter objects via a fluent interface becomes tricky in
Java if inheritance is involved. In *Commons Configuration* the
`Parameters` class is responsible for the creation of parameters
objects. It serves as a type-safe factory for parameter objects with
support for inheritance. It defines a set of methods for creating
parameter objects for special `Configuration` classes. On
the objects returned by these methods fluent `set` methods can
be invoked in order to set the single properties. As an example consider
the following code fragment which defines some properties for an
`XMLConfiguration`:

```

Parameters params = new Parameters();
XMLBuilderParams xmlParams = params.xml()
    .setThrowExceptionOnMissing(true)
    .setValidating(true)
    .setEncoding("UTF-8")
    .setFileName("config.xml")
    .setExpressionEngine(new XPathExpressionEngine());
```

Note how properties from different parameter interfaces can be set in an
arbitrary order: the `throwExceptionOnMissing` flag is part
of the basic initialization parameters common to all configuration
classes, the encoding and the file name parameters are common to all
file-based configurations, the expression engine parameter is supported
by all hierarchical configurations, and the `validating` flag is
specific to XML configurations. We will not describe all available
initialization parameters in detail now; they are explained in the
sections dealing with specific `Configuration` classes (and
of course, the Javadoc is the ultimate reference). For
now a short overview over the existing parameter objects and the
corresponding methods in the `Parameters` class should be
sufficient:

| `Parameters` method | Interface | Description |
| --- | --- | --- |
| `basic()` | `BasicBuilderParameters` | Defines fundamental properties common to all `Configuration` implementations derived from `AbstractConfiguration`. |
| `fileBased()` | `FileBasedBuilderParameters` | Properties related to file-based configurations. For instance, multiple ways for defining the file to be loaded are provided. |
| `combined()` | `CombinedBuilderParameters` | This object is used by the specialized builder for combined configurations. Here properties can be set which define the content of the resulting combined configuration. |
| `jndi()` | `JndiBuilderParameters` | A parameters object for initializing JNDI configurations. |
| `hierarchical()` | `HierarchicalBuilderParameters` | Here special parameters common to all hierarchical configurations are defined, for instance the expression engine. |
| `xml()` | `XMLBuilderParameters` | The parameters for XML configurations. |
| `properties()` | `PropertiesBuilderParameters` | The parameters for [properties configurations](#userguide-howto_properties). |
| `multiFile()` | `MultiFileBuilderParameters` | This parameters class is used by the builder for [multi file configurations](#userguide-howto_multitenant--multifilehierarchicalconfiguration). |
| `database()` | `DatabaseBuilderParameters` | The parameters for `DatabaseConfiguration`. |

After a parameters object has been created and initialized via its fluent
`set()` methods, it can be passed to a configuration builder's
`configure()` method. This method extracts all properties from
the passed in object and stores them internally. They are then used to
initialize a newly created `Configuration` object. Calling
`configure()` another time with a different parameters object
overrides all properties set so far; more precise, the existing properties are
cleared, and the new ones are copied over. However, it is possible to
pass multiple parameters objects at once to the `configure()` method
(it has a varargs argument). In this case, the union of all parameters
is constructed.

Configuring a configuration builder with parameters objects is an
expressive and type-safe way. For initialization parameters constructed
more dynamically there is an alternative based on maps. Some
constructors of `BasicConfigurationBuilder` accept a
`Map<String, Object>`. Here arbitrary initialization
parameters can be passed. The keys of the map are strings corresponding
to the names of the initialization parameters (they are equivalent to
the property names in the associated `Configuration`
implementations; for instance `throwExceptionOnMissing`);
the map's values are the values of the parameters. No matter which
mechanism is used to define initialization parameters, it has to be
ensured that the configuration object to be constructed supports all of
these parameters; otherwise, an exception is thrown when the instance is
created.

<a id="userguide-howto_builders--default-initialization-parameters"></a>

## Default Initialization Parameters

Big applications may use configuration data from multiple files or
sources. If they need special settings for all their configuration
objects, there is the issue that these settings have to be repeated
again and again for each configuration source to be created. For instance, all files to be read may have a specific encoding, or hierarchical
configurations should use a special expression engine. In a naive
approach, all these settings have to be set on each configuration builder
used by the application.

To make life of developers easier and in compliance with the DRY (don't
repeat yourself) principle, *Commons Configuration* supports
default initialization parameters for configuration sources. It was
already shown how an instance of the
`Parameters` class is used to create initialization parameter
objects for various types of configuration sources. In addition to the
methods for creating these objects, `Parameters` also deals
with default values for them. The mechanisms are as follows:

`Parameters` defines methods for registering so-called
*defaults handler* objects. A defaults handler is an object
implementing the
`DefaultParametersHandler` interface. This interface defines a
single method which accepts a parameters object of a generic type and
populates it according to its logic. Such handlers can be registered for
specific initialization parameter interfaces.

When an initialization parameters object of a specific class is to be
created the `Parameters` instance checks whether
`DefaultParameterHandler` objects have been registered for this
class or its base classes. If this is the case, the matching handler
objects are invoked on the newly created parameters object - they can now
initialize it as they like.

Note that the inheritance hierarchy of parameters objects is implicitly
taken into account: A defaults handler registered for file-based
parameters is also invoked for XML parameters because XML parameters are
derived from file-based parameters and thus contain all the properties
the handler may initialize. When registering a defaults handler it is
also supported to specify the start class in the inheritance hierarchy of
parameters objects on which the handler should be executed. This makes it
possible for instance to register a handler for file-based parameters, but define that it should be invoked only for XML parameters. That way
special file-related properties can be set for XML configurations, but
they will not apply to, say, properties configurations although they are
file-based, too. When registering default handlers the registration order
matters. Defaults handlers are invoked in the order they have been
registered; so a handler registered later can override initializations
made by a handler registered before. With these options a very
fine-grained control of initialization parameters is possible;
especially, different initialization parameters can be set for specific
configuration classes even if the parameters are of the same (base) type.

After all this theory let's come to some concrete examples. For now we
assume that we already have some `DefaultParametersHandler`
implementations in place that we want to register on a `Parameters`
object. (The next section will focus on the implementation of handlers.)
In this example the following is to be achieved:

- There is a `CommonDefaultsHandler` class setting
  default initialization parameters to be applied for all configuration
  sources.
- There is a defaults handler for file-based parameters which sets
  the expected encoding of the file: `EncodingDefaultsHandler`.
  We want this handler to be applied on XML configurations only.
- Our application will also load some properties files. For these
  configuration sources we want an alternative setting of some basic
  properties. This is implemented by a handler class called
  `PropertiesDefaultHandler`.

The code for this initialization could look as follows:

```

// Create the defaults handler objects.
DefaultParametersHandler<BasicBuilderParameters> basicHandler =
    new CommonDefaultsHandler();
DefaultParametersHandler<FileBasedBuilderParameters> encodingHandler =
    new EncodingDefaultsHandler("iso-8859-1");
DefaultParametersHandler<PropertiesBuilderParameters> propsHandler =
    new PropertiesDefaultHandler();

// Register the handlers
Parameters params = new Parameters();
params.registerDefaultsHandler(BasicBuilderParameters.class, basicHandler);
params.registerDefaultsHandler(FileBasedBuilderParameters.class,
    encodingHandler, XMLBuilderParameters.class);
params.registerDefaultsHandler(PropertiesBuilderParameters.class, propsHandler);
```

Now every time this `Parameters` instance is used for the
creation of specific initialization parameters objects, the defaults
handlers registered are applied. So the produced parameters objects are
already initialized (at least partly).
This registration of defaults handlers could be done in the startup phase
of an application. The `Parameters` class is thread-safe, so
an application can create and configure a single instance and use it
across all modules to create parameter objects. The actual functionality
of managing and invoking `DefaultParametersHandler` objects is
implemented by the
`DefaultParametersManager` class - `Parameters` just
delegates to a wrapped instance. In some usage scenarios it may make sense
to use `DefaultParametersManager` directly.

<a id="userguide-howto_builders--defining-default-parameters-handlers"></a>

## Defining Default Parameters Handlers

After the registration of default handlers has been discussed, it is still
open how such handlers can be created. Because the
`DefaultParametersHandler` interface is very simple, it is easy
to create a specialized implementation. The following listing shows how
the `EncodingDefaultsHandler` from the previous example could
be implemented:

```
public class EncodingDefaultsHandler implements DefaultParametersHandler<FileBasedBuilderParameters> {/** The encoding to be set. */ private final String encoding;
/** * Creates a new instance and sets the encoding.* @param enc the encoding to be set on the parameters objects */ public EncodingDefaultsHandler(String enc) {encoding = enc;}
@Override public void initializeDefaults(FileBasedBuilderParameters parameters) {parameters.setEncoding(encoding);}}
```

The point to take is that in the `initializeDefaults()` method
arbitrary initializations can be performed. In many scenarios the
implementation of a specialized `DefaultParametersHandler` is
not necessary because *Commons Configuration* provides a pretty
generic default implementation:
`CopyObjectDefaultHandler`. The name stems from the fact that a
handler is constructed from a parameters object to be used as reference.
In the `initializeDefaults()` method the handler copies all
properties of this reference object onto the object to be initialized.
So all a developer needs to do is creating a parameters object of the
correct type, initializing all desired properties, and passing this object to
a newly created `CopyObjectDefaultHandler` object. Let's
explore how the `EncodingDefaultsHandler` class discussed
previously class can be replaced by `CopyObjectDefaultHandler`:

```

Parameters params = new Parameters();

// Create a file-based parameters object to be used as copy source
FileBasedBuilderParameters encParams =
    params.fileBased().setEncoding("iso-8859-1");

// Perform handler registration with a copy handler
params.registerDefaultsHandler(FileBasedBuilderParameters.class,
    new CopyObjectDefaultHandler(encParams), XMLBuilderParameters.class);
```

So this fragment has the same effect (regarding the initialization of the
*encoding* property) as the example using the custom
`EncodingDefaultsHandler` class - but without the need to
provide a custom `DefaultParametersHandler` implementation.
Because of the flexibility of `CopyObjectDefaultHandler`
custom implementations are probably only required for initializations
that depend on conditional logic.

This completes the description of the builder concept in *Commons
Configuration* and the `BasicConfigurationBuilder` base
class. Following chapters will deal with specialized builders and
explain the extended functionality they provide to the user of this
library.

---

<a id="userguide-howto_combinedbuilder"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_combinedbuilder.html -->

<!-- page_index: 15 -->

<a id="userguide-howto_combinedbuilder--combining-configuration-sources"></a>

# Combining Configuration Sources

While simple applications often store their configuration data in a
single configuration file, there may be advanced requirements for more
complex systems. From a certain size of configuration data it surely
makes sense to divide the settings available on a set of configuration
files each of which is related to a specific sub-domain. This makes it
easier for users or administrators to adapt specific configuration
settings. However, rather than reading multiple files and dealing with
multiple `Configuration` objects, an application probably
prefers a combined view on its configuration data. *Commons
Configuration* supports this use case with a special configuration
builder implementation:
`CombinedConfigurationBuilder`.

`CombinedConfigurationBuilder` is the option of choice for
applications that have to deal with multiple configuration sources. It
provides the following features:

- Various configuration sources can be combined to a single
  [CombinedConfiguration](#userguide-howto_combinedconfiguration) object. This is a truly hierarchical
  configuration supporting enhanced query facilities.
- As configuration sources the most relevant `Configuration`
  implementations provided by this library are supported. Sources are
  defined as [bean
  declarations](#userguide-howto_beans), so complex initializations are possible.
- Meta data can be provided to fine-tune the constructed
  configuration.
- `CombinedConfigurationBuilder` is extensible. Custom
  configuration sources can be added.

This document starts with some explanations of
`CombinedConfigurationBuilder` basics. Then the *configuration
definition files* processed by `CombinedConfigurationBuilder`
are discussed in detail. Finally an advanced example is presented.

<a id="userguide-howto_combinedbuilder--the-configuration-definition-file"></a>

## The configuration definition file

In previous chapters we have already seen how specific configuration
classes like `PropertiesConfiguration` or
`XMLConfiguration` can be used to load configuration data from
a single source. `CombinedConfigurationBuilder` now allows
combining multiple configuration sources to a single
`CombinedConfiguration` object. The sources to be loaded have to
be defined in an XML document with a specific structure, a so-called
*configuration definition file*. The following listing shows a
simple example of such a definition file:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration>
  <properties fileName="usergui.properties"/>
</configuration>
```

A configuration definition file can contain an arbitrary number of
elements declaring the configuration sources to load. The
`<properties>` element is one of these; it is used to
include properties files. For this example we store the definition file
in the same directory as the properties file and call it
`config.xml`. The properties file used in this example is the
same as in the section about [properties
files](#userguide-howto_properties).

<a id="userguide-howto_combinedbuilder--setting-up-a-combinedconfigurationbuilder"></a>

## Setting up a CombinedConfigurationBuilder

Now we have to create a `CombinedConfigurationBuilder` object
and let it read this definition file. This works in a similar way as
the construction of other typical [configuration builders](#userguide-howto_builders): A new instance is created, and the
`configure()` method is called with initialization parameters
(`CombinedConfigurationBuilder` is derived from
`BasicConfigurationBuilder`; so all features common to
configuration builders are available here as well). The combined configuration collecting
all sources defined in the configuration definition file can then be
obtained by calling the builder's `getConfiguration()` method.

The easiest way to define the configuration definition file is to pass an
initialized parameters object for file-based configurations to the
builder. In this case, no other specific settings are set for the builder, and the file is read as an XML document:

```

Parameters params = new Parameters();
CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
    .configure(params.fileBased().setFile(new File("config.xml")));
CombinedConfiguration config = builder.getConfiguration();
```

Now the *config* object can be accessed in the usual way to query
configuration properties, e.g. by using methods like `getString()`, or `getInt()`. A frequent use case is that a configuration
file is shipped with an application inside its jar archive. For instance, the jar could have a special folder where all configuration files are
located as in the following example:

```

/classes
/conf
/conf/mainConfig.xml
/conf/subConfig1.properties
/conf/subConfig2.xml
```

Here the *conf* folder in the jar contains a main configuration
file - this is the definition file for the combined builder - and two
configuration sources referenced from the main file.
`mainConfig.xml` looks as follows:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration>
  <properties fileName="subConfig1.properties"/>
  <xml fileName="subConfig2.xml"/>
</configuration>
```

In order to load this file and the referenced configuration sources, the
previous example can slightly be adapted to determine a URL to the main
configuration file from the application's class loader:

```

Parameters params = new Parameters();
CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
    .configure(params.fileBased().setURL(
      getClass().getClassLoader().getResource("/conf/mainConfig.xml")
    ));
CombinedConfiguration config = builder.getConfiguration();
```

The point to take here is that it is possible to load a combined
configuration directly from a jar file by specifying the URL to the
configuration definition file. The configuration sources to be embedded
are specified as relative paths; they are automatically resolved based on
the URL of the main configuration file.

Just defining the configuration definition file
via a file-based parameters object is a special case. Internally, a builder
for an `XMLConfiguration` object is constructed which is then
used to load and interpret the definition file. This should be appropriate
for many cases. A drawback of this method is that there is no way to set
additional initialization parameters for the
`CombinedConfigurationBuilder`. For this purpose, a special
parameters object exists offering some more specialized settings. If this
object is to be used, information about the file to be loaded can be
passed via the `definitionBuilderParameters` property:

```

Parameters params = new Parameters();
CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
    .configure(params.combined().setDefinitionBuilderParameters(
        params.fileBased().setFileName("definition.xml")
    ));
CombinedConfiguration config = builder.getConfiguration();
```

In this example, the `combined()` method of
`Parameters` is used to obtain a special parameters object for a
combined configuration builder. Internally, again a builder for
constructing an `XMLConfiguration` for the definition file is
created. The object stored in the `definitionBuilderParameters`
property is passed to this builder's `configure()` method.

It is even possible to construct the builder for the configuration
definition file externally and then pass it to the
`CombinedConfigurationBuilder` via the
`definitionBuilder` property of its initialization parameters
object:

```

Parameters params = new Parameters();
// set up the builder for the configuration definition file
ConfigurationBuilder<? extends HierarchicalConfiguration<?>> defBuilder = ...;

// Create the combined builder and pass it the definition builder
CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
    .configure(params.combined().setDefinitionBuilder(defBuilder));
CombinedConfiguration config = builder.getConfiguration();
```

This is the most flexible variant. It makes it possible in theory to
read the definition for the combined configuration builder from a
completely different source. In practice, most applications will stick
to XML files defining a combined configuration source because this is
the native format for listing configuration sources and defining
additional meta data (as described in the following sections). But
making use of the `definitionBuilder` property allows at least
passing in a specially configured builder object. Please refer to the
section [Builder Configuration Related to Combined Configurations](#userguide-howto_combinedbuilder--builder_configuration_related_to_combined_configurations) for
additional parameters supported by builders for combined configurations.

If you do not need any specific initialization and just want to read the
configuration definition from an XML document, the
`Configurations` helper class introduced in section
[Making it easier](#userguide-howto_filebased--making_it_easier) is
made for you. It offers convenience methods for creating a builder for
combined configurations from various sources. Here is an example how a
builder can be constructed from a definition file specified as a file
path:

```

Configurations configs = new Configurations();
CombinedConfigurationBuilder builder = configs.combinedBuilder("path/to/definition/file.xml");
```

<a id="userguide-howto_combinedbuilder--overriding-properties"></a>

## Overriding properties

Using `CombinedConfigurationBuilder` to collect configuration
sources does not make much sense if there is only a single source to be
loaded. So let's add another one to the example definition file used
before! This time we will embed a XML file: *gui.xml* which is
shown in the next listing:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>
<gui-definition>
  <colors>
    <background>#808080</background>
    <text>#000000</text>
    <header>#008000</header>
    <link normal="#000080" visited="#800080"/>
  </colors>
  <rowsPerPage>15</rowsPerPage>
</gui-definition>
```

To make this XML document part of our global configuration we have to
modify our configuration definition file to also include the new file. For
XML documents the element `<xml>` can be used so that we
have now:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration>
  <properties fileName="usergui.properties"/>
  <xml fileName="gui.xml"/>
</configuration>
```

The code for setting up the `CombinedConfigurationBuilder`
object remains the same. From the `Configuration` object
returned by the factory the new properties can be accessed in the usual
way.

There is one open question with this example configuration setup: The
`color.background` property is defined in both the properties
and the XML file, and - to make things worse - with different values.
Which value will be returned by a call to `getString()`?

The answer is that the configuration sources are searched in the order
they are defined in the configuration definition file. Here the properties
file is included first, then comes the XML file. Because the
`color.background` property can be found in the properties file
the value specified there will be returned (which happens to be
`#FFFFFF`).

It might not be obvious why it makes sense to define the value of one and
the same property in multiple configuration sources. But consider the
following scenario: An application comes with a set of default properties
and allows the user to override some or all of them. This can now easily
be realized by saving the user's settings in one file and the default
settings in another. Then in the configuration definition file the file
with the user settings is included first and after that the file with the
default values. The application code that queries these settings does not
have to bother whether a property was overridden by the user. `CombinedConfigurationBuilder`
takes care that properties defined in the first file (the user file) are
found; other properties which the user has not changed will still be
returned from the second file (the defaults file).

<a id="userguide-howto_combinedbuilder--optional-configuration-sources"></a>

## Optional configuration sources

The example above with two configuration sources - one for user settings
and one with default values - raises an interesting question: What happens
if the user has not defined specific properties yet? Or what if a new user
starts our application for the first time and thus no user specific
properties exist?

The default behavior of `CombinedConfigurationBuilder` is to
throw a `ConfigurationException` exception if one of the sources
defined in the configuration definition file cannot be loaded. For our
example this behavior is not desired: the properties file with specific user
settings is not required. If it cannot be loaded, the example application
should still work because a complete set of configuration properties is
defined in the second file.

`CombinedConfigurationBuilder` supports such optional configuration
sources. For this purpose in the definition of a configuration source the
`config-optional` attribute can be placed. An example of this
is shown below:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration>
  <properties fileName="usersettings.properties" config-optional="true"/>
  <properties fileName="default.properties"/>
</configuration>
```

In this configuration definition file the first properties file with user
specific settings is marked as optional. This means that if it cannot be
loaded, `CombinedConfigurationBuilder` will not throw an exception, but only write a warning message to its logger. Note that the
`config-optional` attribute is absent for the second properties
file. Thus it is mandatory, and the `getConfiguration()` method
of `CombinedConfigurationBuilder` would throw an exception if it
could not be found.

A configuration source with the `config-optional` attribute
that cannot be loaded is simply ignored; in the resulting combined
configuration no reference for this source is stored. In the example
with the user configuration, it would be good if in case of a failure
(because the user configuration file does not yet exist) an empty
configuration object is created and added to the combined configuration.
This configuration object can then be used to store specific user
settings which the user might define.

For configuration sources marked as optional, an additional attribute is
supported providing exactly this functionality: `config-forceCreate`.
If set to **true**, a configuration is created in any case
for this source. If the source can be loaded successfully, this is of
course the resulting configuration. Otherwise, an empty configuration
(of the same type) is created. The example below shows how this attribute
can be used. Here we also define a name for the configuration source, so
that the produced configuration can later be retrieved from the resulting
combined configuration.

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration>
  <properties fileName="usersettings.properties" config-name="userConfig"
    config-optional="true" config-forceCreate="true"/>
  <properties fileName="default.properties"/>
</configuration>
```

<a id="userguide-howto_combinedbuilder--union-configuration"></a>

## Union configuration

In an earlier section about the configuration definition file for
`CombinedConfigurationBuilder` it was stated that configuration
files included first can override properties in configuration files
included later, and an example use case for this behavior was given. There
may be cases when there are other requirements.

Let's continue the example with the application that somehow process
database tables and that reads the definitions of the affected tables from
its configuration. This example and the corresponding XML configuration
files were introduced in the section about
[hierarchical configurations](#userguide-howto_hierarchical).
Now consider that this application grows larger and must be maintained by
a team of developers. Each developer works on a separated set of tables.
In such a scenario it would be problematic if the definitions for all
tables were kept in a single file. It can be expected that this file
needs to be changed very often and thus can be a bottleneck for team
development when it is nearly steadily checked out. It would be much better
if each developer had an associated file with table definitions, and all
these information could be linked together at the end.

`CombinedConfigurationBuilder` provides support for such a use case, too. It is possible to specify in the configuration definition file that
from a set of configuration sources a logic union configuration is to be
constructed. Then all properties defined in the provided sources are
collected and can be accessed as if they had been defined in a single source.
To demonstrate this feature let us assume that a developer of the database
application has defined a specific XML file with a table definition named
`tasktables.xml`:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<config>
  <table tableType="application">
    <name>tasks</name>
    <fields>
      <field>
        <name>taskid</name>
        <type>long</type>
      </field>
      <field>
        <name>name</name>
        <type>java.lang.String</type>
      </field>
      <field>
        <name>description</name>
        <type>java.lang.String</type>
      </field>
      <field>
        <name>responsibleID</name>
        <type>long</type>
      </field>
      <field>
        <name>creatorID</name>
        <type>long</type>
      </field>
      <field>
        <name>startDate</name>
        <type>java.util.Date</type>
      </field>
      <field>
        <name>endDate</name>
        <type>java.util.Date</type>
      </field>
    </fields>
  </table>
</config>
```

This file defines the structure of an additional table, which should be
added to the so far existing table definitions. To achieve this the
configuration definition file has to be changed: A new section is added
that contains the declaring elements of all configuration sources which
are to be combined.

```

<?xml version="1.0" encoding="ISO-8859-1" ?>
<!-- Configuration definition file that demonstrates the
     override and additional sections -->

<configuration>
  <override>
    <properties fileName="usergui.properties"/>
    <xml fileName="gui.xml"/>
  </override>

  <additional>
    <xml fileName="tables.xml"/>
    <xml fileName="tasktables.xml" config-at="tables"/>
  </additional>
</configuration>
```

Compared to the older versions of this file some changes have been done.
One major difference is that the elements for including configuration
sources are no longer direct children of the root element, but are now
contained in either an `<override>` or `<additional>`
section. The names of these sections already imply their purpose.

The `override` section is not strictly necessary. Elements in
this section are treated as if they were children of the root element, i.e.
properties in the included configuration sources override properties in
sources included later. So the `<override>` tags could have
been omitted, but for the sake of clarity it is recommended to use them
if there is also an `<additional>` section.

It is the `<additional>` section that introduces a new behavior.
All configuration sources listed here are combined to a union configuration.
In our example we have put two `xml` elements in this area
that load the available files with database table definitions. The syntax
of elements in the `additional` section is analogous to the
syntax described so far. In this example the `config-at`
attribute is introduced. It specifies the position in the logic union
configuration where the included properties are to be added. Here it is set
for the second element to the value *tables*. This is because the
file starts with a `<table>` element, but to be compatible
with the other table definition file it should be accessible under the key
`tables.table`.

After these modifications have been performed, the configuration obtained
from `CombinedConfigurationBuilder` allows access to three database
tables. A call of `config.getString("tables.table(2).name");`
results in a value of *tasks*. In an analogous way it is possible
to retrieve the fields of the third table.

Note that it is also possible to override properties defined in an
`additional` section. This can be done by placing a configuration
source in the `override` section that defines properties that
are also defined in one of the sources listed in the `additional`
section. The example does not make use of that. Note also that the order of
the `override` and `additional` sections in a
configuration definition file does not matter. Sources in an `override`
section are always treated with higher priority (otherwise they could not
override the values of other sources).

<a id="userguide-howto_combinedbuilder--configuration-definition-file-reference"></a>

## Configuration definition file reference

Configuration definition files are XML documents telling
`CombinedConfigurationBuilder` which configuration sources to
load and how to process them in order to create the resulting combined
configuration.

**Overall structure of a configuration definition file**

A configuration definition file for `CombinedConfigurationBuilder`
can contain three sections, all of which are optional. A skeleton looks as
follows:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration systemProperties="path to property file">
  <header>
    <!-- Meta data about the resulting combined configuration -->
  </header>
  <override>
    <!-- Configuration declarations with override semantics -->
  </override>
  <additional>
    <!-- Configuration declarations that form a union configuration -->
  </additional>
</configuration>
```

**Declaring configuration sources**

The `override` and `additional` sections have already
been introduced when the basics of `CombinedConfigurationBuilder`
were discussed. They contain declarations for the configuration sources to be
embedded. For convenience reasons it is also possible to declare
configuration sources outside these sections; they are then treated as if
they were placed inside the `override` section.

Each declaration of a configuration source is represented by an XML
element whose name determines the type of the configuration source.
Attributes or nested elements can be used to provide additional
configuration options for the sources to be included (e.g. a name of a
file to be loaded or further flags). Below is a list of all
tags which can be used out of the box:

properties
:   With this element properties files can be included. The name of
    the file to load is specified using the `fileName`
    attribute. Which configuration class is created by this tag
    depends on the extension of the file to load: If the extension
    is ".xml", a
    `XMLPropertiesConfiguration` object is
    created, which is able to process the XML properties format
    introduced in Java 5.0. Otherwise a
    `PropertiesConfiguration` object is created, the default reader
    for properties files.

xml
:   The `xml` element can be used to load XML configuration
    files. It also uses the `fileName` attribute to
    determine the name of the file to load and creates an instance
    of `XMLConfiguration`.

jndi
:   As the name implies, with this element JNDI resources can be
    included in the resulting configuration. Under the hood this is
    done by an instance of the
    `JndiConfiguration` class. The `prefix` attribute
    can be used to select a subset of the JNDI tree.

plist
:   The `plist` element allows embedding configuration
    files in the NeXT / OpenStep or Mac OS X format. Again the
    name of the file to load is specified through the
    `fileName` attribute. If a XML file is specified,
    a `XMLPropertyListConfiguration` object is created
    to process the file. Otherwise, this task is delegated to a
    `PropertyListConfiguration` instance.

system
:   With this element an instance of
    `SystemConfiguration` is added to the resulting configuration
    allowing access to system properties. *Note:* Using this element
    system properties are directly made available. Alternatively the
    interpolation features (see [Variable Interpolation](#userguide-howto_basicfeatures--variable_interpolation) for more details) can be used for referencing
    system properties.

ini
:   This tag can be used to include an ini file into the resulting
    combined configuration. Behind the scenes an instance of
    `INIConfiguration` is used to load the ini file.

env
:   With this tag direct access to environment properties can be enabled.
    This works in the same way as the `<system>` tag for
    Java system properties.

multFile
:   Using this tag, a builder for a multi-file configuration can be
    integrated into the resulting combined configuration. This is described in a
    [later
    chapter](#userguide-howto_multitenant--multifilehierarchicalconfiguration).

configuration
:   The `configuration` tag allows other configuration
    definition files to be included. This makes it possible to nest these
    definition files up to an arbitrary depth. In fact, this tag will
    create another `CombinedConfigurationBuilder` object,
    initialize it, and obtain the `CombinedConfiguation` from it.
    This combined configuration will then be added to the resulting
    combined configuration. Like all file-based configurations the
    `fileName` attribute can be used to specify the configuration
    definition file to be loaded. This file must be an XML document that
    conforms to the format described here. Some of the most important
    settings are copied from the original `CombinedConfigurationBuilder`
    object to the newly created builder:

    - the base path under which configuration files are searched
    - some flags, e.g. for controlling delimiter parsing or throwing
      exceptions on missing properties
    - the logger
    - the configuration and error listeners

In the declaration of a configuration source it is possible to set
properties on the corresponding configuration objects. Configuration
declarations are indeed
[Bean declarations](#userguide-howto_beans). That means they can have attributes matching simple
properties of the configuration object to create, and sub elements
matching complex properties. The following example fragment shows how
complex initialization can be performed in a configuration declaration:

```

  <properties fileName="test.properties" throwExceptionOnMissing="true">
    <reloadingDetectorFactory
    config-class="com.foo.MyReloadingDetector" strict=true"/>
  </properties>
  <xml fileName="test.xml" validating="true">
    <expressionEngine config-class="org.apache.commons.configuration2.tree.xpath.XPathExpressionEngine"/>
  </xml>
```

In this example a configuration source for a properties file and one for
an XML document are defined. For the properties source the
`throwExceptionOnMissing` property is set to **true**, which means that it should throw an exception if a requested property is
not found. In addition, it is assigned a custom reloading detector, which is
declared and configured in a sub element. The XML configuration source is
initialized in a similar way: a simple property is set, and an expression
engine is assigned. In fact, the properties defined in these declarations
are not directly set on configuration instances, but on
[initialization
parameters objects](#userguide-howto_builders--initialization_parameters) for configuration builders. These builders are
created for the declared configuration sources and configured with the
defined properties. Then their managed configurations are obtained and
combined into the resulting configuration. Nevertheless, the declarations
share the same syntax as other bean declarations supported by
*Commons Configuration*. More information about the format for
declaring beans and initializing their properties can be found in the
section about [bean declarations](#userguide-howto_beans).

In addition to the attributes that correspond to properties of the
configuration sources to be created, a configuration declaration can have a
set of special attributes that are evaluated by
`CombinedConfigurationBuilder` when it creates the objects.
These attributes are listed in the following table:

| Attribute | Meaning |
| --- | --- |
| `config-name` | Allows a name to be specified for this configuration. This name can be used to obtain a reference to the configuration from the resulting combined configuration (see below). |
| `config-at` | With this attribute an optional prefix can be specified for the properties of the corresponding configuration. |
| `config-optional` | Declares a configuration as optional. This means that errors that occur when creating the configuration are silently ignored. The default behavior when an error occurs is that no configuration is added to the resulting combined configuration. This behavior can be used to find out whether an optional configuration could be successfully created or not. If you specify a name for the optional configuration (using the `config-name` attribute), you can later check whether the combined configuration contains a configuration with this name. With the `config-forceCreate` attribute (see below) this default behavior can be changed. |
| `config-forceCreate` | This boolean attribute is only evaluated for configurations declared as optional. It determines the behavior of the combined configuration builder when the optional configuration could not be created. If set to **true**, the builder tries to create an empty, uninitialized configuration of the correct type and add it to the resulting combined configuration. This is especially useful for file-based configurations. Consider a use case where an application wants to store user specific configuration files in the users' home directories. When a user starts this application for the first time, the user configuration does not exist yet. If it is declared as *optional* and *forceCreate*, the missing configuration file won't cause an error, but an empty configuration will be created. The application can then obtain this configuration, add properties to it (e.g. user specific settings) and save it. Without the `config-forceCreate` attribute the application would have to check whether the user configuration exists in the combined configuration and eventually create it manually. Note that not all configuration providers support this mechanism. Sometimes it may not be possible to create an empty configuration if the standard initialization fails. In this case no configuration will be added to the combined configuration (with other words: the `config-forceCreate` attribute will not have any effect). |

*Note:* In older versions of Commons Configuration the attributes
`config-at` and `config-optional` were named
`at` and `optional` respective. They have been
renamed in order to avoid possible name clashes with property names for
configuration sources. However, for reasons of backwards compatibility, the old attribute names can still be used.

Another useful feature is the built-in support for interpolation (i.e.
variable substitution): You can use variables in your configuration
definition file that are defined in declared configuration sources. For
instance, if the name of a configuration file to be loaded is defined by
the system property `CONFIG_FILE`, you can do something like
this:

```

<configuration>
  <!-- Load the system properties -->
  <system/>
  <!-- Now load the config file, using a system property as file name -->
  <properties fileName="${CONFIG_FILE}"/>
</configuration>
```

Note that you can refer only to properties that have already been loaded.
If you change the order of the `<system>` and the
`<properties>` elements in the example above, an error
will occur because the `${CONFIG_FILE}` variable will then be
undefined at the moment it is evaluated.

```

<configuration systemProperties="systemProperties.xml">
  <!-- Load the system properties -->
  <system/>
  <!-- Now load the config file, using a system property as file name -->
  <properties fileName="${CONFIG_FILE}"/>
</configuration>
```

This example differs from the previous one by the `systemProperties`
attribute added to the root element. It causes the specified properties file to be read
and all properties defined therein to be added to the system properties.
So properties like *CONFIG\_FILE* can be defined in a properties
file and are then treated as if they were system properties.

**The header section**

In the header section properties of the resulting combined configuration
object can be set. The main part of this section is a bean declaration
that is used for creating the resulting configuration object. Other
elements can be used for customizing the
[Node combiners](#userguide-howto_combinedconfiguration--node_combiners)
used by the override and the union combined configuration. The following
example shows a header section that uses some of the supported properties:

```

  <header>
    <result throwExceptionOnMissing="true">
      <nodeCombiner config-class="org.apache.commons.configuration2.tree.OverrideCombiner"/>
      <expressionEngine config-class="org.apache.commons.configuration2.tree.xpath.XPathExpressionEngine"/>
    </result>
    <combiner>
      <override>
        <list-nodes>
          <node>table</node>
          <node>list</node>
        </list-nodes>
      </override>
      <additional>
        <list-nodes>
          <node>table</node>
        </list-nodes>
      </additional>
    </combiner>
  </header>
```

The `result` element points to the bean declaration for the
resulting combined configuration. In this example we set some attributes
and initialize the node combiner (which is not necessary because the
default override combiner is specified), and the expression engine to be
used. Note that the `config-class` attribute makes it
possible to inject custom classes for the resulting configuration or the
node combiner.

The `combiner` section allows nodes to be defined as list nodes.
This can be necessary for certain node combiner implementations to work
correctly. More information can be found in the section about
[Node combiners](#userguide-howto_combinedconfiguration--node_combiners).

There are some more tags for specific use cases which can occur in the
header section of a configuration declaration:

providers
:   This tag can be used to define new tags for including custom
    configuration sources. An example is provided later in this document.

fileSystem
:   Allows defining the [File
    System](#userguide-howto_filebased--file_systems) to be used for file-based configuration sources:

```

<configuration>
  <header>
    <fileSystem
      config-class="org.apache.commons.configuration2.io.VFSFileSystem"/>
  </header>
  <xml fileName="test.xml" config-name="xml"/>
</configuration>
```

lookups
:   In the sub section
    [Customizing
    interpolation](#userguide-howto_basicfeatures--customizing_interpolation) it was described how variable interpolation can be
    extended by defining custom lookup objects. In the configuration
    definition file of `CombinedConfigurationBuilder` it is
    possible to declare such lookup objects and make them available for
    the processing of this definition file and the resulting combined
    configuration. For this purpose, the header section of the definition
    file can contain a `<lookup>` element in which an
    arbitrary number of lookups can be defined. Have a look at the
    following example:

```

<configuration>
  <header>
    <lookups>
      <lookup config-prefix="file"
              config-class="com.foo.FileLookup"/>
    </lookups>
  </header>
  <!-- Fetch the file name from a variable -->
  <xml fileName="${file:config_file}" config-name="xml"/>
</configuration>
```

    Here a custom lookup class is declared and registered under the prefix
    *file* (as defined by the `config-prefix` attribute).
    The lookup is immediately active. It is then used to obtain the concrete
    file name for the embedded XML configuration. Note that the variable
    prefix matches the prefix provided in the lookup declaration. The
    variable name is passed to the lookup object, and the custom implementation
    can compute a suitable value.

*Note:* From time to time the question is raised whether there is a
document type definition or a schema defining exactly the structure of a
configuration definition file. Frankly, the answer is no. This is due to
the fact that the format is extensible. As will be shown below, it is
possible to register your own tags in order to embed custom configuration
sources.

<a id="userguide-howto_combinedbuilder--reloading-support"></a>

## Reloading Support

The chapter [Automatic
Reloading of Configuration Sources](#userguide-howto_reloading) explains how reloading facilities
can be enabled for single configuration sources. This feature is also
useful when working with combined configuration sources. Here you might
want to support reloading for some or all of the configuration sources
referenced in the configuration definition file. And - to be really
flexible - external changes in the configuration definition file itself
should also be detected and cause a re-construction of the whole
combined configuration.

To enable reloading support for combined configurations, *Commons
Configuration* provides a special extension of
`CombinedConfigurationBuilder`:
`ReloadingCombinedConfigurationBuilder`. The relation between the
two is analogous to the relation between
`FileBasedConfigurationBuilder` and
`ReloadingFileBasedConfigurationBuilder`. The reloading-enabled
variant of combined configuration builder manages and exposes a special
`ReloadingController` that can be used to trigger reloading
checks. (Please refer to the chapter about [reloading](#userguide-howto_reloading)
for a detailed description of the reloading implementation in *Commons
Configuration* and the components involved.)

The reloading controller exposed by a `ReloadingCombinedConfigurationBuilder`
is special because it is also a combined reloading controller. It manages
the specific reloading controllers of all configuration sources with
reloading support. So when the reloading controller of the combined
builder is triggered, in fact all reloading-aware configuration sources
perform a reload check; sources that have actually been changed generate
a reloading event causing the invalidation of the combined builder's
managed configuration - it has to be re-constructed the next time it is
accessed making the reloaded changes visible.

The configuration builder providing access to the configuration definition
file is treated in the same way as a configuration source in respect to
reloading, i.e. if this builder supports reloading, it becomes part of the
combined reloading controller. `ReloadingCombinedConfigurationBuilder`
per default creates a reloading-aware builder for its definition configuration
when no specific builder was defined in the initialization parameters. (If
a builder for the definition configuration is explicitly passed in the
initialization parameters, it lies in the responsibility of the caller to
use a builder with reloading support.)

With a `ReloadingCombinedConfigurationBuilder` in place, enabling
reload support for specific configuration sources is as simple as adding
another attribute to the source declaration: `config-reload`.
Remember that a combined configuration builder internally creates child
configuration builders for each of the configuration sources to be loaded.
For sources having a `config-reload` attribute with a value of
**true** a builder with reloading support is created if
possible. This may not be supported by all types of configuration
sources, but it is for instance for file-based configuration sources; in
this case the builder created for a source with enabled reloading support
is of type `ReloadingFileBasedConfigurationBuilder`.

A more complex example of a combined configuration populated from multiple
sources with reloading support is presented below.

<a id="userguide-howto_combinedbuilder--an-example"></a>

## An example

After all that theory let's go through a more complex example! We start
with the configuration definition file that looks like the following:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>
<!-- Test configuration definition file that demonstrates complex initialization -->
<configuration>
  <header>
    <result>
      <expressionEngine config-class="org.apache.commons.configuration2.tree.xpath.XPathExpressionEngine"/>
      <listDelimiterHandler
        config-class="org.apache.commons.configuration2.convert.DefaultListDelimiterHandler">
        <config-constrarg config-value=","/>
      </listDelimiterHandler>
    </result>
    <combiner>
      <additional>
        <list-nodes>
          <node>table</node>
        </list-nodes>
      </additional>
    </combiner>
  </header>
  <override>
    <properties fileName="user.properties" throwExceptionOnMissing="true"
      reloadingRefreshDelay="10000" config-name="properties"
      config-reload="true" config-optional="true"/>
    <xml fileName="settings.xml" config-name="xml"/>
  </override>
  <additional>
    <xml config-name="tab1" fileName="table1.xml" config-at="database.tables"/>
    <xml config-name="tab2" fileName="table2.xml" config-at="database.tables"
        validating="true"/>
  </additional>
</configuration>
```

This configuration definition file includes four configuration sources and
sets some properties for the resulting `CombinedConfiguration`.
We also set some properties for the configurations to be loaded; for
instance we declare that one of the XML configurations should be validated.

With the following code we can create a `CombinedConfigurationBuilder`
and load this file; because one of the configuration sources supports
reloading we use the reloading-aware variant of a combined configuration
builder:

```

Parameters params = new Parameters();
ReloadingCombinedConfigurationBuilder builder = new ReloadingCombinedConfigurationBuilder()
    .configure(params.fileBased().setFile(new File("configuration.xml")));
CombinedConfiguration cc = builder.getConfiguration();
```

Here the easiest way to specify the configuration definition file was used:
a parameters object for a file-based configuration. This is sufficient for
this example because no other properties for the builder have to be set.
As described under [Setting
up a CombinedConfigurationBuilder](#userguide-howto_combinedbuilder--setting_up_a_combinedconfigurationbuilder), other options are available. If we
wanted a special processing of the XML document with the configuration
definition - e.g. enabling validation to a schema -, we could have passed
a correspondingly initialized XML parameters object in the
`definitionBuilderParameters` property of a combined parameters
object or even use a specially configured builder for the definition
configuration.

In the `header` section we have chosen an XPATH expression
engine for the resulting configuration. So we can query our properties
using the convenient XPATH syntax. We also enabled list delimiter parsing
by specifying a
`DefaultListDelimiterHandler` object. (Note the syntax for
creating a bean instance via its constructor.) By providing the `config-name`
attribute we have given all configuration sources a name. These names can
be used to obtain the corresponding sources from the combined
configuration. For configurations in the override section this is
directly possible:

```

Configuration propertiesConfig = cc.getConfiguration("properties");
Configuration xmlConfig = cc.getConfiguration("xml");
```

Configurations in the `additional` section are treated a bit
differently: they are all packed together in another combined configuration
and then added to the resulting combined configuration. So in our example
the combined configuration `cc` will contain three configurations:
the two configurations from the override section, and the combined
configuration with the `additional` configurations. The latter
is stored under a name determined by the `ADDITIONAL_NAME`
constant of `CombinedConfigurationBuilder`. The following
code shows how the configurations of the `additional` section
can be accessed:

```

CombinedConfiguration ccAdd = (CombinedConfiguration)
  cc.getConfiguration(CombinedConfigurationBuilder.ADDITIONAL_NAME);
Configuration tab1Config = ccAdd.getConfiguration("tab1");
Configuration tab2Config = ccAdd.getConfiguration("tab2");
```

To make sure that reloading checks are periodically performed, a suitable
trigger has to be used to ensure that the reloading controller managed by
the builder is called in regular intervals. This can be done in the same
way as for simple configuration sources, for instance by setting up a
`PeriodicReloadingTrigger` object:

```

PeriodicReloadingTrigger trigger = new PeriodicReloadingTrigger(builder.getReloadingController(),
    null, 1, TimeUnit.MINUTES);
trigger.start();
```

<a id="userguide-howto_combinedbuilder--extending-the-configuration-definition-file-format"></a>

## Extending the configuration definition file format

If you have written a custom configuration class, you might want to
declare instances of this class in a configuration definition file, too.
`CombinedConfigurationBuilder` supports this use case by
registering a
`ConfigurationBuilderProvider` object.

The task of a `ConfigurationBuilderProvider` is to create and
initialize a configuration builder object which can then be used to obtain
a configuration source. Whenever `CombinedConfigurationBuilder`
encounters a tag in the `override` or the `additional`
section it checks whether for this tag a `ConfigurationBuilderProvider`
has been registered. If this is the case, the provider is asked to create a
new configuration builder instance; otherwise an exception is thrown.

So for adding support for a new configuration class you have to create an
implementation of `ConfigurationBuilderProvider` and
register an instance of it. Registration can be done via the combined
parameters object passed to the builder which offers a
`registerProvider()` method. This method expects the
name of the associated tag and the provider instance as arguments.

There is already a fully functional implementation of the
`ConfigurationBuilderProvider` interface available in the class
`BaseConfigurationBuilderProvider` class. When creating an
instance the following information has to be passed:

- The fully-qualified name of the configuration builder class to be
  used for the associated configuration source.
- The fully-qualified name of the configuration builder class to be
  used if reloading is enabled for this source. This is optional; if a
  configuration source does not support reloading, **null**
  can be passed here. Then an exception is thrown if a configuration
  source of this type is declared with the `config-reload`
  attribute set to **true**.
- The fully-qualified name of the configuration class created by
  this builder.
- A collection with parameter object classes supported by this
  builder.

With this information, `BaseConfigurationBuilderProvider` can
create and configure a correct configuration builder object for a specific
configuration source. In detail, it performs the following steps:

- It determines the builder class to be used based on the presence and
  value of the `config-reload` attribute; this means that either
  the normal or the reloading builder - if defined - is used.
- An instance of the builder class is created via reflection.
- Instances of all of the parameter object classes are created.
- The parameter objects are initialized from the properties defined
  for the current configuration source.
- The initialized parameter objects are passed to the configuration
  builder's `configure()` method.

For most cases, the functionality provided by
`BaseConfigurationBuilderProvider` should be sufficient. So
a properly initialized instance can be directly used for the registration
of a new builder provider. Let's take a look at an example
where we want to add support for a configuration class called
`com.foo.MyConfiguration`. The class is a file-based configuration;
therefore, already existing standard builder classes can be used to
construct instances. (Otherwise, a custom builder implementation has to be
created, and its name has to be passed to the provider instance.) The
corresponding tag in the configuration definition file should have the
name `myconfig`. The code for registering the new provider and
loading the configuration definition file looks as follows:

```

ConfigurationProvider provider = new BaseConfigurationProvider(
    /* normal builder */
    "org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder",
    /* reloading builder */
    "org.apache.commons.configuration2.builder.ReloadingFileBasedConfigurationBuilder",
    /* configuration class */
    "com.foo.MyConfig",
    /* Parameters; here we assume that we have a custom parameters class
       derived from FileBasedBuilderParametersImpl */
    Collections.singleton(MyConfigParams.class.getName()));

Parameters params = new Parameters();
CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
    .configure(
        params.combined()
            .setDefinitionBuilderParameters(
                params.fileBased().setFileName("definition.xml"))
            .registerProvider("myconfig", provider)
    );
CombinedConfiguration config = builder.getConfiguration();
```

If your configuration provider is registered this way, your configuration
definition file can contain the `myconfig` tag just as any
other tag for declaring a configuration source:

```

<configuration>
  <additional>
    <xml fileName="settings.xml"/>
    <myconfig fileName="special.cfg" throwExceptionOnMissing="false"/>
  </additional>
</configuration>
```

Alternatively, it is also possible to declare and register custom
configuration builder providers directly in the configuration definition
file. This is an interesting option because it makes the definition
file self-contained; no special initialization is required on the
configuration builder in order to load them. The registration of builder
providers is done in the `<providers>` section in the
header of the definition file. Each builder provider to be added has to
be defined by specifying the tag name and the fully-qualified provider
class. To make use of this mechanism for the custom configuration class
used in this example, a specialized provider class has to be created
(before `BaseConfigurationBuilderProvider` was instantiated
directly):

```
package com.foo;
public class MyConfigurationBuilderProvider extends BaseConfigurationBuilderProvider {public MyConfigurationBuilderProvider() {super("org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder","org.apache.commons.configuration2.builder.ReloadingFileBasedConfigurationBuilder","com.foo.MyConfig",Collections.singleton(MyConfigParams.class.getName()));}}
```

Now this class can be referenced in the configuration definition file.

```

<configuration>
  <header>
    <providers>
      <provider config-tag="myconfig"
                config-class="com.foo.MyConfigurationBuilderProvider"/>
    </providers>
  </header>
  <additional>
    <xml fileName="settings.xml"/>
    <myconfig fileName="special.cfg" throwExceptionOnMissing="false"/>
  </additional>
</configuration>
```

Now this file can be processed by a default `CombinedConfigurationBuilder`
instance. No special configuration related to builder providers is
necessary any more:

```

Parameters params = new Parameters();
CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
    .configure(params.fileBased().setFileName("definition.xml"));
CombinedConfiguration config = builder.getConfiguration();
```

<a id="userguide-howto_combinedbuilder--builder-configuration-related-to-combined-configurations"></a>

## Builder Configuration Related to Combined Configurations

The special parameters object for `CombinedConfigurationBuilder`
has already been mentioned and used within examples before. It can be obtained
from the `combined()` method of a
`Parameters` instance. Its type is
`CombinedBuilderParameters`.

This type supports the settings common to all configurations. Additional
settings specific to `CombinedConfigurationBuilder` are
defined by the
`CombinedBuilderProperties` interface. This includes

- the configuration builder for obtaining the definition configuration
- the parameters object for the configuration builder for obtaining the
  definition configuration
- a base path for file-based configuration sources; sources with a
  relative file name are searched in this path.
- information about
  [custom
  configuration builder providers](#userguide-howto_combinedbuilder--extending_the_configuration_definition_file_format)
- default handlers for initialization parameters of configuration
  sources. They work in the same way as global
  [default
  initialization parameters](#userguide-howto_builders--default_initialization_parameters) for configuration builders,
  but only impact the configuration sources defined in the current
  definition file. For instance, it is possible to define default settings
  for all XML configuration sources. These are applied for every XML
  source defined in the definition file unless they are overridden there.
  See below for an example.
- controlling the inheritance of builder parameters to child
  configuration builders (see below).

Specifying default settings for the configuration sources to be included
is a convenient feature. Often the configuration files to be included
share similar conventions, and thus can be read using similar
parameters. Rather than repeating these settings in the configuration
definition file for each configuration source, there are ways to define
default settings.

One option is to use a mechanism similar to
[default
initialization parameters](#userguide-howto_builders--default_initialization_parameters): The parameters object for a combined
configuration builder allows defining default parameter objects for
specific types of configuration sources. In the following example all
XML configuration sources are configured to make use of a specific list
delimiter handler:

```

DefaultListDelimiterHandler listDelimiterHandler = new DefaultListDelimiterHandler(',');
Parameters params = new Parameters();
XMLBuilderParameters xmlParams = params.xml()
    .setListDelimiterHandler(listDelimiterHandler);
XMLBuilderParameters definitionParams = params.xml()
    .setFile(new File("configDefinition.xml"));
CombinedBuilderParameters combinedParameters = params.combined()
    .setDefinitionBuilderParameters(definitionParams)
    .registerChildDefaultsHandler(XMLBuilderProperties.class,
        new CopyObjectDefaultHandler(xmlParams));
builder.configure(combinedParameters);
CombinedConfiguration config = builder.getConfiguration();
```

Here the `xmlParams` object defines default settings for all
XML configuration sources to be included. Note how it is used to register
a defaults handler using the `registerChildDefaultsHandler()`
method of the parameters object for the combined builder. This mechanism
of default parameters is very flexible because it allows setting
different options for different types of configuration sources. However, as the example demonstrates, the initialization of the builder becomes
complex; multiple parameter objects have to be dealt with.

A more lightweight alternative is the ability of a combined configuration
builder to inherit its parameters to the child configurations created by
it. This feature is enabled by default and it works as follows: Whenever
a parameter object for a child configuration source is created, it is
first populated with compatible parameters set for the combined builder.
Then the specific settings as defined by the configuration definition
file are applied. So the settings defined for the combined builder as a
whole serve as a kind of default parameters. With this mechanism the
following code can be used to set a special list delimiter handler for
all child configurations and a special expression engine for all
hierarchical child configurations:

```

Parameters params = new Parameters();
DefaultExpressionEngineSymbols symbols = new DefaultExpressionEngineSymbols.Builder(
    DefaultExpressionEngineSymbols.DEFAULT_SYMBOLS)
    .setPropertyDelimiter("/").create();
DefaultExpressionEngine engine = new DefaultExpressionEngine(symbols);
DefaultListDelimiterHandler listDelimiterHandler = new DefaultListDelimiterHandler(',');
XMLBuilderParameters xmlParams = params.xml()
    .setExpressionEngine(engine)
    .setListDelimiterHandler(listDelimiterHandler)
    .setFile(new File("configDefinition.xml"));
builder.configure(xmlParams);
CombinedConfiguration config = builder.getConfiguration();
```

So here the builder is configured with an XML parameters object which
defines some default settings and also the file to be loaded. The default
settings are applied automatically to child configuration sources where
applicable. This is often a natural approach; for many use cases it makes
sense that settings defined for the parent combined builder are also
applied to child configuration sources. Only if child configuration
sources follow different conventions - maybe some files from a legacy
system need to be integrated that use a different list delimiter
character -, inheritance does not help. But in such cases it is often
possible to use settings inheritance by default and override specific
settings in affected child configuration sources; of course, the settings
defined for a configuration source in the configuration definition file
take precedence over inherited settings. The inheritance mechanism can
also be turned off completely by invoking
`CombinedBuilderParameters.setInheritSettings()` with a
value of **false**.

---

<a id="userguide-howto_combinedconfiguration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_combinedconfiguration.html -->

<!-- page_index: 16 -->

<a id="userguide-howto_combinedconfiguration--combined-configuration"></a>

# Combined Configuration

The `CombinedConfiguration` class provides an alternative for handling
multiple configuration sources. Its API is very similar to the
`CompositeConfiguration` class, which was discussed in the
[previous
section](https://commons.apache.org/proper/commons-configuration/userguide/howto_compositeconfiguration.html#Composite_Configuration_Details). There are the following differences however:

- A `CombinedConfiguration` is a truly
  [hierarchical
  configuration](https://commons.apache.org/proper/commons-configuration/userguide/howto_xml.html#Hierarchical_properties). This means that all the enhanced facilities
  provided by `HierarchicalConfiguration` (e.g. expression
  engines) can be used.
- A `CombinedConfiguration` is not limited to implementing
  an override semantics for the properties of the contained configurations.
  Instead it has the concept of so-called *node combiners*, which
  know how properties of multiple configuration sources can be combined.
  Node combiners are discussed later in detail. For instance, there is a
  node combiner implementation available that constructs a union of the
  contained configurations.
- Contained configurations can be assigned a name. They can later be
  accessed by their name.
- Each contained configuration can have an optional prefix. Its
  properties are then added under this prefix to the combined
  configuration.
- There is no concept of an *in memory configuration*.

<a id="userguide-howto_combinedconfiguration--how-it-works"></a>

## How it works

A `CombinedConfiguration` provides a logic view on the
properties of the configurations it contains. This view is determined
by the associated node combiner object. Because of that it must be
re-constructed whenever one of these contained configurations is
changed.

To achieve this, a `CombinedConfiguration` object registers
itself as an event listener at the configurations that are added to it.
It will then be notified for every modification that occurs. If such a
notification is received, the internally managed view is invalidated.
When a property of the combined configuration is to be accessed, the view
is checked whether it is valid. If this is the case, the property's value
can be directly fetched. Otherwise the associated node combiner is asked
to re-construct the view.

<a id="userguide-howto_combinedconfiguration--node-combiners"></a>

## Node combiners

A *node combiner* is an object of a class that inherits from the
abstract `NodeCombiner`
class. This class defines an abstract `combine()` method, which
takes the root nodes of two hierarchical configurations and returns the
root node of the combined node structure. It is up to a concrete
implementation how this combined structure will look like. *Commons
Configuration* ships with three concrete implementations
`OverrideCombiner`, `MergeCombiner`
and `UnionCombiner`, which implement an override, merge, and union semantics respectively.

Constructing a combination of multiple node hierarchies is not a trivial
task. The available implementations descend the passed in node hierarchies
in a recursive manner to decide, which nodes have to be copied into the
resulting structure. Under certain circumstances two nodes of the source
structures can be combined into a single result node, but unfortunately
this process cannot be fully automated, but sometimes needs some hints
from the developer. As an example consider the following XML configuration
sources:

```

<configuration>
  <database>
    <tables>
      <table>
        <name>users</name>
        <fields>
          <field>
            <name>user_id</name>
          </field>
          ...
        </fields>
      </table>
    </tables>
  </database>
</configuration>
```

and

```

<configuration>
  <database>
    <tables>
      <table>
        <name>documents</name>
        <fields>
          <field>
            <name>document_id</name>
          </field>
          ...
        </fields>
      </table>
    </tables>
  </database>
</configuration>
```

These two configuration sources define database tables. Each source
defines one table. When constructing a union for these sources the result
should look as follows:

```

<configuration>
  <database>
    <tables>
      <table>
        <name>users</name>
        <fields>
          <field>
            <name>user_id</name>
          </field>
          ...
        </fields>
      </table>
      <table>
        <name>documents</name>
        <fields>
          <field>
            <name>document_id</name>
          </field>
          ...
        </fields>
      </table>
    </tables>
  </database>
</configuration>
```

As you can see, the resulting structure contains two `table`
nodes while the nodes `database` and `tables` appear
only once. For a human being this is quite logic because `database`
and `tables` define the overall structure of the configuration
data, and there can be multiple tables. A node combiner however does not
know anything about structure nodes, list nodes, or whatever. From its point of
view there is no detectable difference between the `tables`
nodes and the `table` nodes in the source structures: both
appear once in each source file and have no values. So without any
assistance the result constructed by the `UnionCombiner` when
applied on the two example sources would be a bit different:

```

<configuration>
  <database>
    <tables>
      <table>
        <name>users</name>
        <fields>
          <field>
            <name>user_id</name>
          </field>
          ...
        </fields>
        <name>documents</name>
        <fields>
          <field>
            <name>document_id</name>
          </field>
          ...
        </fields>
      </table>
    </tables>
  </database>
</configuration>
```

Note that the `table` node would be considered a structure
node, too, and would not be duplicated. This is probably not what was
desired. To deal with such situations it is possible to tell the node
combiner that certain nodes are list nodes and thus should not be
combined. So in this concrete example the `table` node should
be declared as a list node, then we would get the expected result. We will
see below how this is done. Note that this explicit declaration of a list
node is necessary only in situations where there is ambiguity. If in one
of our example configuration sources multiple tables had been defined, the
node combiner would have concluded itself that `table` is a list
node and would have acted correspondingly.

The examples that follow are provided to further illustrate the differences
between the combiners that are delivered with *Commons Configuration*. The first
two files are the files that will be combined.

<table class="bodyTable">
<tr>
<th>testfile1.xml</th>
<th>testfile2.xml</th>
</tr>
<tr>
<td>
<pre><code>&lt;config&gt;
  &lt;gui&gt;
    &lt;bgcolor&gt;green&lt;/bgcolor&gt;
    &lt;selcolor&gt;yellow&lt;/selcolor&gt;
    &lt;level default="2"&gt;1&lt;/level&gt;
  &lt;/gui&gt;
  &lt;net&gt;
    &lt;proxy&gt;
      &lt;url&gt;http://www.url1.org&lt;/url&gt;
      &lt;url&gt;http://www.url2.org&lt;/url&gt;
      &lt;url&gt;http://www.url3.org&lt;/url&gt;
    &lt;/proxy&gt;
    &lt;service&gt;
      &lt;url&gt;http://service1.org&lt;/url&gt;
    &lt;/service&gt;
    &lt;server&gt;
    &lt;/server&gt;
  &lt;/net&gt;
  &lt;base&gt;
    &lt;services&gt;
      &lt;security&gt;
        &lt;login&gt;
          &lt;user&gt;Admin&lt;/user&gt;
          &lt;passwd type="secret"/&gt;
        &lt;/login&gt;
      &lt;/security&gt;
    &lt;/services&gt;
  &lt;/base&gt;
  &lt;database&gt;
    &lt;tables&gt;
      &lt;table id="1"&gt;
        &lt;name&gt;documents&lt;/name&gt;
        &lt;fields&gt;
          &lt;field&gt;
            &lt;name&gt;docid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;docname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;authorID&lt;/name&gt;
            &lt;type&gt;int&lt;/type&gt;
          &lt;/field&gt;
        &lt;/fields&gt;
      &lt;/table&gt;
    &lt;/tables&gt;
  &lt;/database&gt;
  &lt;Channels&gt;
    &lt;Channel id="1" type="half"&gt;
      &lt;Name&gt;My Channel&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id="2"&gt;
      &lt;MoreChannelData&gt;more test 2 data&lt;/MoreChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id="3" type="half"&gt;
      &lt;Name&gt;Test Channel&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id="4"&gt;
      &lt;Name&gt;Channel 4&lt;/Name&gt;
    &lt;/Channel&gt;
  &lt;/Channels&gt;
&lt;/config&gt;
</code></pre></td>
<td>
<pre><code>&lt;config&gt;
  &lt;base&gt;
    &lt;services&gt;
      &lt;security&gt;
        &lt;login&gt;
          &lt;user type="default"&gt;scotty&lt;/user&gt;
          &lt;passwd&gt;BeamMeUp&lt;/passwd&gt;
        &lt;/login&gt;
      &lt;/security&gt;
    &lt;/services&gt;
  &lt;/base&gt;
  &lt;gui&gt;
    &lt;bgcolor&gt;black&lt;/bgcolor&gt;
    &lt;fgcolor&gt;blue&lt;/fgcolor&gt;
    &lt;level min="1"&gt;4&lt;/level&gt;
  &lt;/gui&gt;
  &lt;net&gt;
    &lt;server&gt;
      &lt;url&gt;http://appsvr1.com&lt;/url&gt;
      &lt;url&gt;http://appsvr2.com&lt;/url&gt;
      &lt;url&gt;http://testsvr.com&lt;/url&gt;
      &lt;url&gt;http://backupsvr.com&lt;/url&gt;
    &lt;/server&gt;
    &lt;service&gt;
      &lt;url type="2"&gt;http://service2.org&lt;/url&gt;
      &lt;url type="2"&gt;http://service3.org&lt;/url&gt;
    &lt;/service&gt;
  &lt;/net&gt;
  &lt;database&gt;
    &lt;tables&gt;
      &lt;table id="2"&gt;
        &lt;name&gt;tasks&lt;/name&gt;
        &lt;fields&gt;
          &lt;field&gt;
            &lt;name&gt;taskid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;taskname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
        &lt;/fields&gt;
      &lt;/table&gt;
    &lt;/tables&gt;
  &lt;/database&gt;
  &lt;Channels&gt;
    &lt;Channel id="1"&gt;
      &lt;Name&gt;Channel 1&lt;/Name&gt;
      &lt;ChannelData&gt;test 1 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id="2" type="full"&gt;
      &lt;Name&gt;Channel 2&lt;/Name&gt;
      &lt;ChannelData&gt;test 2 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id="3" type="full"&gt;
      &lt;Name&gt;Channel 3&lt;/Name&gt;
      &lt;ChannelData&gt;test 3 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id="4" type="half"&gt;
      &lt;Name&gt;Test Channel 1&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id="4" type="full"&gt;
      &lt;Name&gt;Test Channel 2&lt;/Name&gt;
    &lt;/Channel&gt;
  &lt;/Channels&gt;
&lt;/config&gt;
</code></pre></td></tr></table>

The first listing shows the result of using the `OverrideCombiner`.

<table class="bodyTable">
<tr>
<th>OverrideCombiner Results</th>
<th>Notes</th></tr>
<tr>
<td>
<pre><code>&lt;config&gt;
  &lt;gui&gt;
    &lt;bgcolor&gt;green&lt;/bgcolor&gt;
    &lt;selcolor&gt;yellow&lt;/selcolor&gt;
    &lt;level default='2' min='1'&gt;1&lt;/level&gt;
    &lt;fgcolor&gt;blue&lt;/fgcolor&gt;
  &lt;/gui&gt;
  &lt;net&gt;
    &lt;proxy&gt;
      &lt;url&gt;http://www.url1.org&lt;/url&gt;
      &lt;url&gt;http://www.url2.org&lt;/url&gt;
      &lt;url&gt;http://www.url3.org&lt;/url&gt;
    &lt;/proxy&gt;
    &lt;service&gt;
      &lt;url&gt;http://service1.org&lt;/url&gt;
    &lt;/service&gt;
    &lt;server&gt;
      &lt;url&gt;http://appsvr1.com&lt;/url&gt;
      &lt;url&gt;http://appsvr2.com&lt;/url&gt;
      &lt;url&gt;http://testsvr.com&lt;/url&gt;
      &lt;url&gt;http://backupsvr.com&lt;/url&gt;
    &lt;/server&gt;
  &lt;/net&gt;
  &lt;base&gt;
    &lt;services&gt;
      &lt;security&gt;
        &lt;login&gt;
          &lt;user type='default'&gt;Admin&lt;/user&gt;
          &lt;passwd type='secret'&gt;BeamMeUp&lt;/passwd&gt;
        &lt;/login&gt;
      &lt;/security&gt;
    &lt;/services&gt;
  &lt;/base&gt;
  &lt;database&gt;
    &lt;tables&gt;
      &lt;table id='1'&gt;
        &lt;name&gt;documents&lt;/name&gt;
        &lt;fields&gt;
          &lt;field&gt;
            &lt;name&gt;docid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;docname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;authorID&lt;/name&gt;
            &lt;type&gt;int&lt;/type&gt;
          &lt;/field&gt;
        &lt;/fields&gt;
      &lt;/table&gt;
    &lt;/tables&gt;
  &lt;/database&gt;
  &lt;Channels&gt;
    &lt;Channel id='1' type='half'&gt;
      &lt;Name&gt;My Channel&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id='2'&gt;
      &lt;MoreChannelData&gt;more test 2 data&lt;/MoreChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id='3' type='half'&gt;
      &lt;Name&gt;Test Channel&lt;/Name&gt;
    &lt;/Channel&gt;
  &lt;/Channels&gt;
&lt;/config&gt;
</code></pre></td>
<td>
<p>
        The features that are significant in this file are:
      </p>
<ul>
<li>In the gui section each of the child elements only appears once. The level element
          merges the attributes from the two files and uses the element value of the first file.</li>
<li>In the security section the user type attribute was obtained from the second file
          while the user value came from the first file. Alternately, the password type was
          obtained from the first file while the value came from the second.</li>
<li>Only the data from table 1 was included.</li>
<li>Channel 1 in the first file completely overrode Channel 1 in the second file.</li>
<li>Channel 2 in the first file completely overrode Channel 2 in the second file. While
          the attributes were merged in the case of the login elements the type attribute
          was not merged in this case.</li>
<li>Again, only Channel 3 from the first file was included.</li>
</ul>
<p>
        How the Channel elements ended up may not at first be obvious. The <code>OverrideCombiner</code>
        simply noticed that the Channels element had three child elements named Channel and
        used that to determine that only the contents of the Channels element in the first file
        would be used.
      </p></td></tr></table>

The next file is the the result of using the `UnionCombiner`

<table class="bodyTable">
<tr>
<th>UnionCombiner Results</th>
<th>Notes</th>
</tr>
<tr>
<td>
<pre><code>&lt;config&gt;
  &lt;gui&gt;
    &lt;bgcolor&gt;green&lt;/bgcolor&gt;
    &lt;selcolor&gt;yellow&lt;/selcolor&gt;
    &lt;level default='2'&gt;1&lt;/level&gt;
    &lt;bgcolor&gt;black&lt;/bgcolor&gt;
    &lt;fgcolor&gt;blue&lt;/fgcolor&gt;
    &lt;level min='1'&gt;4&lt;/level&gt;
  &lt;/gui&gt;
  &lt;net&gt;
    &lt;proxy&gt;
      &lt;url&gt;http://www.url1.org&lt;/url&gt;
      &lt;url&gt;http://www.url2.org&lt;/url&gt;
      &lt;url&gt;http://www.url3.org&lt;/url&gt;
    &lt;/proxy&gt;
    &lt;service&gt;
      &lt;url&gt;http://service1.org&lt;/url&gt;
      &lt;url type='2'&gt;http://service2.org&lt;/url&gt;
      &lt;url type='2'&gt;http://service3.org&lt;/url&gt;
    &lt;/service&gt;
    &lt;server&gt;&lt;/server&gt;
    &lt;server&gt;
      &lt;url&gt;http://appsvr1.com&lt;/url&gt;
      &lt;url&gt;http://appsvr2.com&lt;/url&gt;
      &lt;url&gt;http://testsvr.com&lt;/url&gt;
      &lt;url&gt;http://backupsvr.com&lt;/url&gt;
    &lt;/server&gt;
  &lt;/net&gt;
  &lt;base&gt;
    &lt;services&gt;
      &lt;security&gt;
        &lt;login&gt;
          &lt;user&gt;Admin&lt;/user&gt;
          &lt;passwd type='secret'&gt;&lt;/passwd&gt;
          &lt;user type='default'&gt;scotty&lt;/user&gt;
          &lt;passwd&gt;BeamMeUp&lt;/passwd&gt;
        &lt;/login&gt;
      &lt;/security&gt;
    &lt;/services&gt;
  &lt;/base&gt;
  &lt;database&gt;
    &lt;tables&gt;
      &lt;table id='1' id='2'&gt;
        &lt;name&gt;documents&lt;/name&gt;
        &lt;fields&gt;
          &lt;field&gt;
            &lt;name&gt;docid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;docname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;authorID&lt;/name&gt;
            &lt;type&gt;int&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;taskid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;taskname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
        &lt;/fields&gt;
        &lt;name&gt;tasks&lt;/name&gt;
      &lt;/table&gt;
    &lt;/tables&gt;
  &lt;/database&gt;
  &lt;Channels&gt;
    &lt;Channel id='1' type='half'&gt;
      &lt;Name&gt;My Channel&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id='2'&gt;
      &lt;MoreChannelData&gt;more test 2 data&lt;/MoreChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id='3' type='half'&gt;
      &lt;Name&gt;Test Channel&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id='1'&gt;
      &lt;Name&gt;Channel 1&lt;/Name&gt;
      &lt;ChannelData&gt;test 1 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id='2' type='full'&gt;
      &lt;Name&gt;Channel 2&lt;/Name&gt;
      &lt;ChannelData&gt;test 2 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id='3' type='full'&gt;
      &lt;Name&gt;Channel 3&lt;/Name&gt;
      &lt;ChannelData&gt;test 3 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
  &lt;/Channels&gt;
&lt;/config&gt;
</code></pre></td>
<td>
<p>
        The feature that is significant in this file is rather obvious. It is just a simple
        union of the contents of the two files.
      </p>
</td></tr></table>

Finally, the last file is the result of using the `MergeCombiner`

<table class="bodyTable">
<tr>
<th>MergeCombiner Results</th>
<th>Notes</th>
</tr>
<tr>
<td>
<pre><code>&lt;config&gt;
  &lt;gui&gt;
    &lt;bgcolor&gt;green&lt;/bgcolor&gt;
    &lt;selcolor&gt;yellow&lt;/selcolor&gt;
    &lt;level default='2' min='1'&gt;1&lt;/level&gt;
    &lt;fgcolor&gt;blue&lt;/fgcolor&gt;
  &lt;/gui&gt;
  &lt;net&gt;
    &lt;proxy&gt;
      &lt;url&gt;http://www.url1.org&lt;/url&gt;
      &lt;url&gt;http://www.url2.org&lt;/url&gt;
      &lt;url&gt;http://www.url3.org&lt;/url&gt;
    &lt;/proxy&gt;
    &lt;service&gt;
      &lt;url&gt;http://service1.org&lt;/url&gt;
    &lt;/service&gt;
    &lt;server&gt;
      &lt;url&gt;http://appsvr1.com&lt;/url&gt;
      &lt;url&gt;http://appsvr2.com&lt;/url&gt;
      &lt;url&gt;http://testsvr.com&lt;/url&gt;
      &lt;url&gt;http://backupsvr.com&lt;/url&gt;
    &lt;/server&gt;
  &lt;/net&gt;
  &lt;base&gt;
    &lt;services&gt;
      &lt;security&gt;
        &lt;login&gt;
          &lt;user type='default'&gt;Admin&lt;/user&gt;
          &lt;passwd type='secret'&gt;&lt;/passwd&gt;
        &lt;/login&gt;
      &lt;/security&gt;
    &lt;/services&gt;
  &lt;/base&gt;
  &lt;database&gt;
    &lt;tables&gt;
      &lt;table id='1'&gt;
        &lt;name&gt;documents&lt;/name&gt;
        &lt;fields&gt;
          &lt;field&gt;
            &lt;name&gt;docid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;docname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;authorID&lt;/name&gt;
            &lt;type&gt;int&lt;/type&gt;
          &lt;/field&gt;
        &lt;/fields&gt;
      &lt;/table&gt;
      &lt;table id='2'&gt;
        &lt;name&gt;tasks&lt;/name&gt;
        &lt;fields&gt;
          &lt;field&gt;
            &lt;name&gt;taskid&lt;/name&gt;
            &lt;type&gt;long&lt;/type&gt;
          &lt;/field&gt;
          &lt;field&gt;
            &lt;name&gt;taskname&lt;/name&gt;
            &lt;type&gt;varchar&lt;/type&gt;
          &lt;/field&gt;
        &lt;/fields&gt;
      &lt;/table&gt;
    &lt;/tables&gt;
  &lt;/database&gt;
  &lt;Channels&gt;
    &lt;Channel id='1' type='half'&gt;
      &lt;Name&gt;My Channel&lt;/Name&gt;
      &lt;ChannelData&gt;test 1 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id='2' type='full'&gt;
      &lt;MoreChannelData&gt;more test 2 data&lt;/MoreChannelData&gt;
      &lt;Name&gt;Channel 2&lt;/Name&gt;
      &lt;ChannelData&gt;test 2 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
    &lt;Channel id='3' type='half'&gt;
      &lt;Name&gt;Test Channel&lt;/Name&gt;
    &lt;/Channel&gt;
    &lt;Channel id='3' type='full'&gt;
      &lt;Name&gt;Channel 3&lt;/Name&gt;
      &lt;ChannelData&gt;test 3 data&lt;/ChannelData&gt;
    &lt;/Channel&gt;
  &lt;/Channels&gt;
&lt;/config&gt;
</code></pre></td>
<td>
<p>
        The features that are significant in this file are:
      </p>
<ul>
<li>In the gui section the elements were merged.</li>
<li>In the net section the elements were merged, with the exception of the urls.</li>
<li>In the security section the user and password were merged. Notice that the
          empty value for the password from the first file overrode the password in the
          second file.</li>
<li>Both table elements appear</li>
<li>Channel 1 and Channel 2 were merged</li>
<li>Both Channel 3 elements appear as they were determined to not be the same.</li>
</ul>
<p>
        When merging elements attributes play a critical role. If an element has an attribute that
        appears in both sources, the value of that attribute must be the same for the elements to be
        merged.
      </p>
<p>
        Merging is only allowed between a single node in each of the files, so if an element
        in the first file matches more than one element in the second file no merging will take
        place and the element from the first file (and its contents) are included and the elements
        in the second file are not. If the element is marked as a list node then the elements from
        the second file will also be included.
      </p></td></tr></table>

<a id="userguide-howto_combinedconfiguration--constructing-a-combinedconfiguration"></a>

## Constructing a CombinedConfiguration

To create a `CombinedConfiguration` object you specify the node
combiner to use and then add an arbitrary number of configurations. We will
show how to construct a union configuration from the two example sources
introduced earlier:

```

// Load the source configurations
Parameters params = new Parameters();
FileBasedConfigurationBuilder<XMLConfiguration> builder1 =
    new FileBasedConfigurationBuilder<XMLConfiguration>(XMLConfiguration.class)
    .configure(params.xml()
        .setFileName("table1.xml"));
FileBasedConfigurationBuilder<XMLConfiguration> builder2 =
    new FileBasedConfigurationBuilder<XMLConfiguration>(XMLConfiguration.class)
    .configure(params.xml()
        .setFileName("table2.xml"));

// Create and initialize the node combiner
NodeCombiner combiner = new UnionCombiner();
combiner.addListNode("table");  // mark table as list node
            // this is needed only if there are ambiguities

// Construct the combined configuration
CombinedConfiguration cc = new CombinedConfiguration(combiner);
cc.addConfiguration(builder1.getConfiguration(), "tab1");
cc.addConfiguration(builder2.getConfiguration());
```

Here we also specified a name for one of the configurations, so it can
later be accessed by `cc.getConfiguration("tab1");`. Access by
index is also supported. After that the properties in the combined
configuration can be accessed as if it were a normal hierarchical
configuration.

<a id="userguide-howto_combinedconfiguration--dealing-with-changes"></a>

## Dealing with changes

There is nothing that prevents you from updating a combined configuration, e.g. by calling methods like `addProperty()` or
`clearProperty()`. However, this will not have the expected
effect!

Remember that a `CombinedConfiguration` is just a view over a
set of other configurations processed by a `NodeCombiner`. The
combiner sets up a nodes structure consisting of
`ImmutableNode` objects. Some of these nodes are likely to be
shared with the child configurations. Because the nodes are immutable
updates on the combined configuration cause nodes to be replaced in the
hierarchy, but this does not affect any of the child configurations. When now
one of the child configurations is changed, the combined configuration
is re-constructed, and all the changes made before on it are lost! With
other words, changes on a combined configuration are only temporary.

The recommended approach is to treat a combined configuration as
immutable and to perform updates on selected child configurations only.
It is in the responsibility of an application anyway to decide which
child configuration is affected by a change; there is no easy way to
determine the target configuration of a change automatically.

If an editable combined configuration is really needed, a possible
solution is to create a `CombinedConfiguration` as usual, and then copy it into another hierarchical configuration. Hierarchical
configuration classes typically have constructors that copy the content
of another configuration. The following example shows how a combined
configuration is copied into a `XMLConfiguration`; it is
then even possible to save the content of the original configuration as
an XML document:

```

// Set up the combined configuration, e.g. like in the example before
CombinedConfiguration cc = ...;

// Create an XMLConfiguration with the content of the combined configuration
XMLConfiguration config = new XMLConfiguration(cc);
```

In this scenario, the `CombinedConfiguration` object is used
only temporarily to apply the node combiner to the data contained in the
child configurations. The resulting nodes structure is then passed to the
`XMLConfiguration`. This is now a full-blown, editable
configuration. However, the connection to the child configurations does
no longer exist.

---

<a id="userguide-howto_concurrency"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_concurrency.html -->

<!-- page_index: 17 -->

<a id="userguide-howto_concurrency--configurations-and-concurrent-access"></a>

# Configurations and Concurrent Access

Configuration objects are often central resources of an application and
are accessed by multiple components. If multiple threads are involved
which read or even update configuration data, care has to be taken that
access to a Configuration object is properly synchronized to avoid data
corruption or spurious exceptions. This section of the user's guide deals
with concurrency and describes the actions necessary to make a
Configuration work in a multi-threaded environment.

<a id="userguide-howto_concurrency--synchronizers"></a>

## Synchronizers

Whether a Configuration object has to be thread-safe or not strongly
depends on a concrete use case. For an application which only reads
some configuration properties in its `main()` method at
startup, it does not matter whether this configuration can safely be
accessed from multiple threads. In this case, the overhead of synchronizing
access to the configuration is not needed, and thus operations on the
`Configuration` object can be more efficient. On the other
hand, if the Configuration object is accessed by multiple components
running in different threads it should better be thread-safe.

To support these different use cases, Commons Configuration takes a
similar approach as the Java Collections framework. Here collections are
per default not thread-safe (and thus more efficient). If an application
needs a thread-safe collection, it can "upgrade" an existing
one by calling a method of the `Collections` class.

Objects implementing the `Configuration` interface can be
associated with a
`Synchronizer` object. This synchronizer is triggered on each
access to the configuration (distinguishing between read and write
access). It can decide whether access is allowed or block the calling
thread until it is safe to continue. Per default, a Configuration object
uses a `NoOpSynchronizer` instance. As the name implies, this class does
nothing to protect its associated configuration against concurrent
access; its methods are just empty dummies. It is appropriate for use
cases in which a configuration is only accessed by a single thread.

If multiple threads are involved, Configuration objects have to be
thread-safe. For this purpose, there is another implementation of
`Synchronizer`:
`ReadWriteSynchronizer`. This class is based on the
`ReentrantReadWriteLock` class from the JDK. It implements
the typical behavior desired when accessing a configuration in a
multi-threaded environment:

- An arbitrary number of threads can read the configuration
  simultaneously.
- Updates of a configuration can only happen with an exclusive lock;
  so if a thread changes configuration data, all other threads (readers
  and writers) are blocked until the update operation is complete.

The synchronizer associated with a Configuration can be changed at any
time by calling the `setSynchronizer()` method. The following
example shows how this method is used to make a `Configuration`
instance thread-safe:

```

config.setSynchronizer(new ReadWriteSynchronizer());
```

Rather than setting the synchronizer on an existing
`Configuration` instance, it is usually better to configure
the [configuration builder](https://commons.apache.org/proper/commons-configuration/userguide/howto_builder.html) responsible
for the creation of the configuration to set the correct synchronizer
directly after a new instance has been created. This is done in the usual
way by setting the corresponding property of a parameters object passed
to the builder's `configure()` method, for instance:

```

Parameters params = new Parameters();
BasicConfigurationBuilder<PropertiesConfiguration> builder =
        new BasicConfigurationBuilder<PropertiesConfiguration>(
                PropertiesConfiguration.class)
                .configure(params.basic()
                        .setSynchronizer(new ReadWriteSynchronizer());
PropertiesConfiguration config = builder.getConfiguration();
```

It is also possible to set the synchronizer to **null**. In
this case, the default `NoOpSynchronizer` is installed, which
means that the configuration is no longer protected against concurrent
access.

With the two classes `NoOpSynchronizer` and
`ReadWriteSynchronizer` the Commons Configuration library
covers the basic use cases of no protection and full protection of
multi-threaded access. As the `Synchronizer` interface is
pretty simple, applications are free to provide their own implementations
according to their specific needs. However, this requires a certain
understanding of internal mechanisms in Configuration implementations.
Some caveats are provided in the remaining of this chapter.

<a id="userguide-howto_concurrency--basic-operations-and-thread-safety"></a>

## Basic operations and thread-safety

`AbstractConfiguration` already provides a major part of the
implementation of correctly interacting with a `Synchronizer`
object. Methods for reading configuration data (such as
`getProperty()`, `isEmpty()`, or
`getKeys()`) and for changing properties (e.g.
`setProperty()`, `addProperty()`, or
`clearProperty()`) already call the correct methods of the
`Synchronizer`. These methods are declared **final**
to avoid that subclasses accidently break thread-safety by incorrectly
usage of the `Synchronizer`.

Classes derived from `AbstractConfiguration` sometimes offer
specific methods for accessing properties. For instance, hierarchical
configurations offer operations on whole subtrees, or
`INIConfiguration` allows querying specific sections. These
methods are also aware of the associated `Synchronizer` and
invoke it correctly.

There is another pair of methods available for each `Configuration`
object allowing direct control over the `Synchronizer`:
`lock()` and `unlock()`. Both methods expect an
argument of type
`LockMode` which tells them whether the configuration is to be
locked for read or write access. These methods can be used to extend the
locking behavior of standard methods. For instance, if multiple properties
are to be added in an atomic way, `lock()` can be called first, then all properties are added, and finally `unlock()` is called.
Provided that a corresponding `Synchronizer` implementation is
used, other threads will not interfere with this sequence. Note that it is
important to always call `unlock()` after a `lock()`
call; this is done best in a **finally** block as shown in
the following example:

```
config.lock(LockMode.WRITE); try {config.addProperty("prop1", "value1"); ...config.addProperty("prop_n", "value_n");} finally {config.unlock(LockMode.WRITE);}
```

So, in a nutshell: When accessing configuration data from standard
configuration classes all operations are controlled via the
configuration's `Synchronizer` object. Client code is only
responsible for setting a correct `Synchronizer` object
which is suitable for the intended use case.

<a id="userguide-howto_concurrency--other-flags"></a>

## Other flags

In addition to the actual configuration data, each `Configuration`
object has some flags controlling its behavior. One example for such a
flag is the boolean `throwExceptionOnMissing` property. Other
helper objects like the object responsible for interpolation or the
expression engine for hierarchical configurations fall into the same
category. The manipulation of those flags and helper objects is also
related to thread-safety.

In contrast to configuration data, access to flags is **not**
guarded by the `Synchronizer`. This means that when changing a
flag in a multi-threaded environment, there is no guarantee that this
change is visible to other threads.

The reason for this design is that the preferred way to create a
`Configuration` object is using a *configuration builder*.
The builder is responsible for fully initializing the configuration;
afterwards, no behavioral changes should be performed any more. Because
builders are always synchronized the values of all flags are safely
published to all involved threads.

If there really is the need to change a flag later on in the life-cycle
of a `Configuration` object, the `lock()` and
`unlock()` methods described in the previous section should be
used to do the change with a write lock held.

<a id="userguide-howto_concurrency--special-cases"></a>

## Special cases

Thread-safety is certainly a complex topic. This section describes some
corner cases which may occur when some of the more advanced configuration
classes are involved.

- All hierarchical configurations derived from
  `BaseHierarchicalConfiguration` internally operate on a nodes
  structure implemented by immutable nodes. This is beneficial for
  concurrent access. It is even possible to share (sub) trees of
  configuration nodes between multiple configuration objects.
  Updates of these structures are implemented in a thread-safe and
  non-blocking way - even when using the default `NoOpSynchronizer`.
  So the point to take is that when using hierarchical configurations
  it is not required to set a special synchronizer because safe
  concurrent access is already a basic feature of these classes.
  The only exception is that change events caused by updates of a
  configuration's data are not guaranteed to be delivered in a
  specific order. For instance, if one thread clears a configuration
  and immediately afterwards another thread adds a property, it may be
  the case that the clear event arrives after the add property event at
  an event listener. If the listener relies on the fact that the
  configuration is empty now, it may be up for a surprise. In cases in
  which the sequence of generated configuration events is important, a
  fully functional synchronizer object should be set.
- `CombinedConfiguration` is a bit special regarding lock
  handling. Although derived from `BaseHierarchicalConfiguration`,
  this class is not thread-safe per default. So if accessed by multiple
  threads, a suitable synchronizer has to be set.
  An instance manages a node tree which is constructed
  dynamically from the nodes of all contained configurations using the
  current *node combiner*. When one of the child configurations is
  changed the node tree is reset so that it has to be re-constructed on
  next access. Because this operation changes the configuration's internal
  state it is performed with a write lock held. So even if only data is
  read from a `CombinedConfiguration`, it may be the case that
  temporarily a write lock is obtained for constructing the combined node
  tree. Note that the synchronizers used for the children of a combined
  configuration are independent. For instance, if configuration objects
  derived from `BaseHierarchicalConfiguration` are added as
  children to a `CombinedConfiguration`, they can continue
  using a `NoOpSynchronizer`.
- Derived from `CombinedConfiguration` is
  `DynamicCombinedConfiguration` which extends its base class by
  the ability to manage multiple combined configuration instances. The
  current instance is selected based on a key constructed by a
  `ConfigurationInterpolator` instance. If this yields a key
  which has not been encountered before, a new `CombinedConfiguration`
  object is created. Here again it turns out that even a read access to a
  `DynamicCombinedConfiguration` may cause internal state
  changes which require a write lock to be held. When creating a new
  child combined configuration it is passed the `Synchronizer`
  of the owning `DynamicCombinedConfiguration`; so there is
  actually only a single `Synchronizer` controlling the
  access to all involved configurations.

<a id="userguide-howto_concurrency--read-only-configurations"></a>

## Read-only configurations

Objects that are not changed typically play well in an environment with
multiple threads - provided that they are initialized in a safe way.
For the safe initialization of `Configuration` objects
specialized [builders](#userguide-howto_builders) are responsible. These are classes derived from
`BasicConfigurationBuilder`. Configuration builders are designed
to be thread-safe: their `getConfiguration()` method is
synchronized, so that configurations can be created and initialized in a
safe way even if multiple threads are interacting with the builder.
Synchronization also ensures that all values stored in member fields of
newly created `Configuration` objects are safely published to
all involved threads.

As long as a configuration returned freshly from a builder is not changed
in any way, it can be used without a special `Synchronizer`
(this means that the default `NoOpSynchronizer` is used).
As was discussed in the previous section, there are special cases in which
read-only access to `Configuration` objects causes internal
state changes. This would be critical without a fully functional
`Synchronizer` object. However, the builders dealing with
affected classes are implemented in a way that they take care about these
special cases and perform extra initialization steps which make write
locks for later read operations unnecessary.

For instance, the builder for combined configurations explicitly accesses
a newly created `CombinedConfiguration` object so that it is
forced to construct its node tree. This happens in the builder's
`getConfiguration()` method which is synchronized. So provided
that the combined configuration is not changed (no other child
configurations are added, no updates are performed on existing child
configurations), no protection against concurrent access is needed - a
simple `NoOpSynchronizer` can do the job.

Situation is similar for the other special cases described in the previous
section. One exception is `DynamicCombinedConfiguration`:
Whether an instance can be used in a read-only manner without a fully
functional `Synchronizer` depends on the way it constructs its
keys. If the keys remain constant during the life time of an instance
(for instance, they are based on a system property specified as startup
option of the Java virtual machine), `NoOpSynchronizer` is
sufficient. If the keys are more dynamic, a fully functional
`Synchronizer` is required for concurrent access - even if only
reads are performed.

So to sum up, except for very few cases configurations can be read by
multiple threads without having to use a special `Synchronizer`.
For this to be safe, the configurations have to be created through a
builder, and they must not be updated by any of these threads. A good way
to prevent updates to a `Configuration` object is to wrap it
by an immutable configuration.

---

<a id="userguide-howto_filebased"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_filebased.html -->

<!-- page_index: 18 -->

<a id="userguide-howto_filebased--file-based-configurations"></a>

# File-based Configurations

Often configuration properties are stored in files on the user's hard
disk, e.g. in .properties files or as XML documents. In order to
access this data, functionality is needed to select the configuration
files, load them into memory, and write changes back to disk. The
following sections describe how this can be done.

<a id="userguide-howto_filebased--filebasedconfigurationbuilder"></a>

## FileBasedConfigurationBuilder

In *Commons Configuration* a specialized
[configuration
builder](#userguide-howto_builders--configuration_builders) implementation is responsible for the creation of
file-based configuration objects and the management of their
associated data files:
`FileBasedConfigurationBuilder`. Usage of this class follows
the typical pattern for configuration builders, i.e. a builder
instance is created providing the class of the `Configuration`
object to be created, the `configure()` method is called
with initialization parameters, and finally `getConfiguration()`
returns an initialized instance of the configuration class. When
configuring the builder the file to be loaded can be specified; if this
was done, the `Configuration` object returned by the
builder contains all properties read from the underlying file.

In order to define the file to be loaded, a parameters object
implementing the
`FileBasedBuilderProperties` interface can be passed to the
builder's `configure()` method. Using this interface the
location of the file to be loaded can be provided in multiple ways:

- With the `setFile()` method the data file can be
  specified as a `java.io.File` object.
- The `setURL()` method takes a `java.net.URL`
  as argument; the file will be loaded from this URL.
- The methods `setFileName()` and `setBasePath()`
  allow specifying the path of the data file. The base path is
  important if relative paths are to be resolved based on this file.
- With `setPath()` an absolute path to the file to be
  loaded can be provided.

A parameters object for file-based configurations is typically obtained
from a `Parameters` instance. Here the `fileBased()` method
or one of the methods returning parameter objects derived from
`FileBasedBuilderProperties` can be used. In addition to
the properties that define the location of the file to be loaded, the
parameters object support a couple of other properties, too, which
are mainly related to way how the file is resolved. This is described
later on in this chapter.

As an example for using a file-based configuration builder, the
following code fragment shows how a properties file can be read whose
location is specified using a `File` object:

```
Parameters params = new Parameters(); // Read data from this file File propertiesFile = new File("config.properties");
FileBasedConfigurationBuilder<FileBasedConfiguration> builder =new FileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class) .configure(params.fileBased() .setFile(propertiesFile)); try {Configuration config = builder.getConfiguration(); // config contains all properties read from the file} catch(ConfigurationException cex) {// loading of the configuration file failed}
```

In this example a parameters object for file-based configurations
is obtained from a `Parameters` instance. We could of
course also have used a derived parameters class - when loading a
properties file a parameters object for properties configurations
would have been a logic choice. Here only a single parameter, the
file to be loaded, is set; but remember that all other initialization
parameters common to all configuration classes are available as well.

A configuration instance created this way stays connected to its
builder. Especially, the builder stores the location of the
underlying configuration file. This comes in handy if changes on
the configuration object are to be written back to disk. For this
purpose, `FileBasedConfigurationBuilder` provides a
convenient `save()` method. Calling this method stores
the current content of the associated configuration into its original
configuration file, overwriting the existing file on disk. This is
demonstrated in the following code fragment which continues from the
previous example:

```
// Some manipulations on the configuration object config.addProperty("newProperty", "new"); config.setProperty("updateProperty", "changedValue");
// Make changes persistent try {builder.save();} catch(ConfigurationException cex) {// saving of the configuration file failed}
```

Note that the `save()` method of the builder does not
expect a configuration object as parameter. It always operates on
the instance managed by this builder. Because of this relationship
it is typically better to store the builder object rather than the
configuration. The configuration can always be obtained via the
builder's `getConfiguration()` method, but operations
related to the configuration file are only available through the
builder.

In addition to the `save()` method, `FileBasedConfigurationBuilder` offers functionality for
automatically saving changes on its managed configuration. This can
be used to ensure that every modification of a configuration object is
immediately written to disk. This feature is enabled via the
`setAutoSave()` method as shown in the following example:

```

FileBasedConfigurationBuilder<FileBasedConfiguration> builder =
    new FileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class)
    .configure(params.fileBased()
        .setFile(new File("config.properties")));
// enable auto save mode
builder.setAutoSave(true);

Configuration config = builder.getConfiguration();
config.setProperty("colors.background", "#000000"); // the configuration is saved after this call
```

Be careful with this mode when you have many updates on your
configuration. This will lead to many I/O operations, too. Behind
the scenes, automatic saving is implemented via the
[event notification mechanism](https://commons.apache.org/proper/commons-configuration/userguide/howto_events.html) available
for all configuration objects. A specialized event listener is
registered at the builder's managed configuration object which triggers
the `save()` method every time an update event is received.

<a id="userguide-howto_filebased--making-it-easier"></a>

## Making it easier

The code fragments presented so far in this chapter and the previous
one show that the fluent API offered by configuration builders in many
cases allows the creation and initialization of a configuration
builder in a single expression. Nevertheless, especially in simple
cases when no complex initialization is required, this approach tends
to become verbose. For instance, if just a configuration is to be
loaded from a file, you always have to create a file-based
parameters object, initialize it, create a builder, and pass the
parameters to its `configure()` method.

To support this frequent use case in a more convenient way, the
`Configurations` class exists. This class contains a bunch
of convenience methods that simplify the creation of many standard
configurations from different sources like files or URLs. Using
this class, the code for the creation of a configuration builder can
be reduced. The example for loading a properties configuration
presented above becomes now:

```

Configurations configs = new Configurations();
// Read data from this file
File propertiesFile = new File("config.properties");

FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
    configs.propertiesBuilder(propertiesFile);
```

From this builder the properties configuration can be obtained in the
usual way. It is even possible to by-pass the builder at all:

```

Configurations configs = new Configurations();
// Read data from this file
File propertiesFile = new File("config.properties");

PropertiesConfiguration config = configs.properties(propertiesFile);
```

Here behind the scenes a configuration builder is created and
initialized; then its managed configuration is queried and returned
to the caller. A `ConfigurationException` is thrown if
an error occurs. Skipping the configuration builder and accessing the
configuration directly is recommended only for simple use cases. A
builder typically offers more flexibility for the handling and
management of configuration objects.

In these examples, a `java.io.File` object was used to
access configuration data. There are overloaded methods for
specifying the data to be loaded in alternative ways: using URLs or
file names/paths. In addition to properties configurations, the
`Configurations` class supports a couple of other
frequently used configuration formats. For instance, the methods
`xml()` and `xmlBuilder()` provide easy access
to XML documents.

Even if there is no direct support for a specific configuration
implementation, with the generic `fileBased()` or
`fileBasedBuilder()` methods, access to all kinds of
file-based configurations can be simplified. We take the
`PropertyListConfiguration` class as an example for which no
specific access methods exist. The code fragment below shows how a
builder for such a configuration can be constructed using a generic
method:

```

Configurations configs = new Configurations();
// Read data from this URL
URL sourceURL = ...;

FileBasedConfigurationBuilder<PropertyListConfiguration> builder =
    configs.fileBasedBuilder(PropertyListConfiguration.class, sourceURL);
PropertyListConfiguration config = builder.getConfiguration();
```

`Configurations` instances are thread-safe and can be stored
centrally by an application. So they can be used as a central configuration
factory - of course, with limited flexibility; this is the price to
be payed for simplicity. However, these restrictions can be partly
circumvented by making use of
[default
initialization parameters](#userguide-howto_builders--default_initialization_parameters). An instance is associated with a
`Parameters` object which is used to construct parameter
objects for the created configuration builders. By assigning default
parameters to this object the default settings used for the created
builders can be tweaked. Note however, that the class typically
creates only generic parameter objects; file-based parameters rather
than, say, specialized parameters for properties configurations. This
makes default settings only possible for basic parameters.

<a id="userguide-howto_filebased--file-operations-on-configurations"></a>

## File Operations on Configurations

With `FileBasedConfigurationBuilder` a single configuration
file is assigned to a configuration instance. For some use cases a
more flexible approach is required. For instance, a modified
configuration is to be stored in another file, or multiple configuration
files should be loaded into the same instance. To achieve this, the
underlying mechanisms for dealing with files have to be used.

I/O operations on files are controlled by the
`FileHandler` class. Basically, this class connects a location
of a configuration file (and some other meta information like the
file's encoding) with an object which can read data from or write data
to this location. `FileHandler` defines the typical
properties for defining the file to be loaded, i.e. the location can be
specified as a URL, a File, an absolute path, etc.

The object which actually reads and writes the data is represented by the
`FileBased` interface. This is a pretty lean interface
consisting of only two methods for reading data from a Reader and
writing data to a Writer. All configuration implementations that can
be initialized from configuration files implement this interface; but
in theory the `FileHandler` could interact with other
objects implementing `FileBased` as well.

`FileHandler` has the two methods `load()` and
`save()`. They work as follows:

- The location of the managed file is evaluated, and a corresponding
  stream is opened. Depending on the way the location was specified,
  this could mean opening a connection on a URL, opening a stream to
  a `File` or an absolute path name, resolving relative
  file names, etc.
- The resulting stream is then passed to the associated
  `FileBased`'s `read()` or `write()`
  method.

Next to these simple `load()` and `save()`
methods a number of overloaded methods exists which expect additional
parameters defining the source or target of the operation. For
instance, there is a `load(URL)` method which reads data
directly from the passed in URL ignoring the location stored in the
`FileHandler` instance. In fact, there are overloaded
methods for all the supported variants for defining a file. When
making use of these methods the following points have to be kept in
mind:

- The location stored in the `FileHandler` instance is
  not changed; it is completely by-passed by these methods. Only
  explicit calls to the various setter methods modify the location.
- The `load()` methods eventually call the target
  object's `read()` method, no matter if it has already been
  called before. For configuration objects as target this means that
  the configuration is not cleared before new data is loaded.
  (Actually a `FileHandler` is not aware which kind of
  target object it is serving; so it has no chance to clear it first.)
  This behavior makes it easy to construct union configurations by
  simply executing multiple load operations. But if you want to reuse
  a configuration object and load a different file, remember to call the
  `clear()` method first to ensure that old properties are
  wiped out.

When constructing a `FileHandler` instance the
`FileBased` object it operates on has to be passed to the
constructor. With this information we are now able to look at a
concrete example. The goal is to create a configuration for a
properties file, read in another properties file (so that a union of
the properties is constructed), and finally write the resulting
configuration to a new file. The code can look as follows (the
handling of exceptions has been omitted):

```

// Read first file directly via the builder
FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
    new FileBasedConfigurationBuilder<PropertiesConfiguration>(PropertiesConfiguration.class)
    .configure(params.fileBased()
        .setFile(new File("config.properties")));
PropertiesConfiguration config = builder.getConfiguration();

// Create a file handler and associate it with the configuration
FileHandler handler = new FileHandler(config);

// Load another configuration source, for instance from a relative path
handler.load("user.properties");

// Store the resulting configuration in a new file
File out = new File("union.properties");
handler.save(out);
```

The `FileHandler` class is thread-safe; it is no problem
for instance to define a file location in one thread and then call
`load()` on another thread. It is also possible to have
multiple `FileHandler` objects associated with the same
target object. Here concurrent I/O operations could cause problems.
Therefore, `FileHandler` checks whether the target object
implements the
`SynchronizerSupport` interface. If this is the case, proper
synchronization for load and save operations can be performed. Because
all configuration implementations implement `SynchronizerSupport`
they can safely be used together with `FileHandler`.

Another important class related to file access is
`FileLocator`. An instance stores all information
required for resolving a file to be accessed. `FileHandler`
uses a `FileLocator` instance to maintain this part of
file-related information. If you need to customize the access to
configuration files, you sometimes have to deal with
`FileLocator` objects because the files to be operated on are
described in terms of such objects.

<a id="userguide-howto_filebased--customizing-file-access"></a>

## Customizing File Access

When working with file-based configurations application code has multiple
ways to specify the location of the file to be loaded. If a URL
is provided, the source file to be loaded is defined in a pretty
unambiguous way. If relative file names or paths are used, situation
is less obvious.

*Commons Configuration* provides two mechanisms to customize the
way configuration files are accessed:

- File systems
- File location strategies

They are described in the following sub sections.

<a id="userguide-howto_filebased--file-systems"></a>

## File Systems

In its default mode of operation *Commons Configuration* supports retrieving and storing
configuration files either on a local file system or via http. However, *Commons
Configuration* provides support for allowing other File System adapters. All file
access is accomplished through the `FileSystem` class so accessing files using other mechanisms is possible.

*Commons Configuration* also provides a second `FileSystem` implementation which allows retrieval using
[Apache Commons VFS](https://commons.apache.org/vfs). As of this writing
Commons VFS supports 18 protocols for manipulating files.

The `FileSystem` used by *Commons Configuration* can be set in
the builder's parameter object, together with other properties defining
the file to be loaded. When working with
[CombinedConfigurationBuilder](#userguide-howto_combinedconfiguration)
it is also possible to
define the file system in the configuration definition file to be
processed by the builder - in both a global way and for each referenced
sub configuration. The following listing shows a configuration definition
file for a combined builder making use of this functionality. Per
default, the `VFSFileSystem` is used, but the included XML
configuration is loaded via a
`DefaultFileSystem` instance:

```

<configuration>
  <header>
    <fileSystem config-class="org.apache.commons.configuration2.io.VFSFileSystem"/>
  </header>
  <override>
    <xml fileName="settings.xml" config-name="xml">
      <fileSystem config-class="org.apache.commons.configuration2.io.DefaultFileSystem"/>
    </xml>

    <!-- Other sources omitted -->
  </override>
</configuration>
```

Commons VFS allows options to the underlying file systems being used. *Commons Configuration*
allows applications to provide these by implementing the
`FileOptionsProvider` interface
and registering the provider with the `FileSystem`. `FileOptionsProvider`
has a single method that must be implemented, `getOptions()`, which returns a Map
containing the keys and values that the `FileSystem` might use. The `getOptions()`
method is called as each configuration uses VFS to create a `FileOjbect` to
access the file. The map returned does not have to contain the same keys and/or values
each time it is called. For example, the value of the `currentUser` key can be
set to the id of the currently logged in user to allow a WebDAV save to record the userid
as a file attribute.

<a id="userguide-howto_filebased--file-location-strategies"></a>

## File Location Strategies

Before a file can be accessed it has to be located first. In the 1.x
versions of *Commons Configuration*, there was a hard-coded
algorithm for looking up configuration files defined by a file name
and an optional base path in various places. Starting with version 2.0, it is now possible to adapt this algorithm. The key to this is the
`FileLocationStrategy` interface. The interface defines
a single method:

```

URL locate(FileSystem fileSystem, FileLocator locator);
```

The purpose of this method is to resolve a file described by the passed
in `FileLocator` object and return a URL for it. If
required, the provided `FileSystem` can be used. The URL
yielded by a successful locate operation is directly used to access
the affected file. If the file could not be resolved, a
`FileLocationStrategy` implementation should not throw an
exception, but return **null** instead. This allows multiple
strategies to be chained so that different locations can be searched for
the file one after the other.

*Commons Configuration* ships with a set of standard
`FileLocationStrategy` implementations. They are pretty
specialized, meaning that a single implementation focuses on a very
specific search algorithm. The true power lies in combining these
strategies in a way suitable for an application or use case. The
following table describes the available `FileLocationStrategy`
implementations:

| Location Strategy class | Description |
| --- | --- |
| `ProvidedURLLocationStrategy` | Directly returns the URL stored in the passed in `FileLocator`. Unless an application needs some special URL transformation, a file locator's URL - if defined - can typically be used directly to access a file. So it makes sense to use this strategy at the very beginning of your chain of strategies. |
| `FileSystemLocationStrategy` | Passes the base path and the file name stored in the passed in `FileLocator` to the `locateFromURL()` method of the current `FileSystem`. This gives the file system the opportunity to perform a special resolution. |
| `AbsoluteNameLocationStrategy` | Checks whether the file name stored in the passed in `FileLocator` is actually an absolute path name pointing to an existing file. If this is the case, the URL to this file is returned. |
| `BasePathLocationStrategy` | This strategy creates a concatenation of the base path and file name stored in the passed in `FileLocator` (of course, only if both are defined). If this results in a path pointing to an existing file, this file's URL is returned. |
| `HomeDirectoryLocationStrategy` | Searches for the referenced file in the current system user's home directory. It is also possible to specify a different directory in which the strategy should search; the path to the target directory can be passed to the constructor. |
| `ClasspathLocationStrategy` | Interprets the file name stored in the passed in `FileLocator` as a resource name and tries to look it up on the current classpath. |
| `CombinedLocationStrategy` | This is a kind of meta strategy which allows combining an arbitrary number of other `FileLocationStrategy` objects. At construction time a collection with sub strategies has to be passed in. In its implementation of the `locate()` method, the strategy iterates over all its sub strategies (in the order they were passed to the constructor) until one returns a non **null** URL. This URL is returned. |

As an example, consider that an application wants configuration files
to be looked up (in this order)

- by their URL
- by the file system (which will evaluate base path and file name)
- on the classpath

Then a concrete location strategy could be constructed as follows:

```

List<FileLocationStrategy> subs = Arrays.asList(
  new ProvidedURLLocationStrategy(),
  new FileSystemLocationStrategy(),
  new ClasspathLocationStrategy());
FileLocationStrategy strategy = new CombinedLocationStrategy(subs);
```

This strategy can now be passed to a file-based configuration builder.
If no strategy is passed to a builder, a default one is used. This
default strategy is almost identical to the hard-coded search algorithm
that was used in earlier versions of *Commons Configuration*.
In fact, the pre-defined basic `FileLocationStrategy`
implementations were extracted from this algorithm.

Because the `FileLocationStrategy` interface is very simple
it should be easy to create a custom implementation. The specific
search algorithm just has to be coded into the `locate()`
method. Then this custom strategy implementation can be combined with
other standard strategies by making use of a
`CombinedLocationStrategy`.

---

<a id="userguide-howto_hierarchical"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_hierarchical.html -->

<!-- page_index: 19 -->

<a id="userguide-howto_hierarchical--hierarchical-configurations"></a>

# Hierarchical Configurations

Many sources of configuration data have a hierarchical or tree-like
nature. They can represent data that is structured in many ways.
Such configuration sources are represented by classes implementing the
`HierarchicalConfiguration` interface. With
`BaseHierarchicalConfiguration` there is a fully functional
implementation of the interface from which most of the hierarchical
configuration classes shipped with *Commons Configuration* are
derived.

Prominent examples of hierarchical configuration sources are XML
documents. They can be read and written using the
`XMLConfiguration` class. This section explains how
to deal with such structured data and demonstrates the enhanced query
facilities supported by `HierarchicalConfiguration`. We
use XML documents as examples for structured configuration sources, but the information provided here (especially the rules for accessing
properties) applies to other hierarchical configurations as well.
Examples for other hierarchical configuration classes are

- `CombinedConfiguration`
- `INIConfiguration`
- `PropertyListConfiguration`
- `JSONConfiguration`
- `YAMLConfiguration`

<a id="userguide-howto_hierarchical--accessing-properties-in-hierarchical-configurations"></a>

## Accessing properties in hierarchical configurations

We will start with a simple XML document to show some basics
about accessing properties. The following file named
`gui.xml` is used as example document:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>
<gui-definition>
  <colors>
    <background>#808080</background>
    <text>#000000</text>
    <header>#008000</header>
    <link normal="#000080" visited="#800080"/>
    <default>${colors.header}</default>
  </colors>
  <rowsPerPage>15</rowsPerPage>
  <buttons>
    <name>OK</name>
    <name>Cancel</name>
    <name>Help</name>
  </buttons>
  <numberFormat pattern="###,###.##"/>
</gui-definition>
```

(As becomes obvious, this tutorial does not bother with good
design of XML documents, the example file should rather
demonstrate the different ways of accessing properties.)
To access the data stored in this document it must be loaded
by `XMLConfiguration`. Like for other
[file-based](#userguide-howto_filebased) configuration classes
a `FileBasedConfigurationBuilder` is used for reading the source
file as shown in the following code fragment:

```
Parameters params = new Parameters(); FileBasedConfigurationBuilder<XMLConfiguration> builder =new FileBasedConfigurationBuilder<XMLConfiguration>(XMLConfiguration.class) .configure(params.xml() .setFileName("gui.xml")); try {XMLConfiguration config = builder.getConfiguration(); ...} catch(ConfigurationException cex) {// loading of the configuration file failed}
```

If no exception was thrown, the properties defined in the
XML document are now available in the configuration object.
Other hierarchical configuration classes that operate on files can be
loaded in an analogous way. The following fragment shows how the
properties in the configuration object can be accessed:

```

String backColor = config.getString("colors.background");
String textColor = config.getString("colors.text");
String linkNormal = config.getString("colors.link[@normal]");
String defColor = config.getString("colors.default");
int rowsPerPage = config.getInt("rowsPerPage");
List<Object> buttons = config.getList("buttons.name");
```

This listing demonstrates some important points about constructing the
keys for accessing properties in hierarchical configuration sources and about
features of `HierarchicalConfiguration` in general:

- Nested elements are accessed using a dot notation. In
  the example document there is an element `<text>`
  in the body of the `<color>` element. The
  corresponding key is `color.text`.
- The root element is ignored when constructing keys. In
  the example you do not write `gui-definition.color.text`,
  but only `color.text`.
- Attributes of XML elements are accessed in a XPath like notation.
- [Interpolation](#userguide-howto_basicfeatures--variable_interpolation)
  can be used in the same way as for all other standard configuration
  implementations. Here the `<default>` element in the
  `colors` section refers to another color.
- Lists of properties can be defined by just repeating elements.
  In this example the `buttons.name` property
  has the three values *OK*, *Cancel*, and
  *Help*, so it is queried using the `getList()`
  method. This works with attributes, too. In addition, a special
  `ListDelimiterHandler` implementation can be set which
  supports splitting texts at a specific list delimiter character. This
  works in the same way as described in the section about
  [properties
  configuration](#userguide-howto_properties--lists_and_arrays). If this mode was used, the three button names could
  be defined in a single XML element. However, then the *pattern*
  attribute of the `<numberFormat>` element needs to
  escape the list delimiter which occurs in its content using a
  backslash character. With these changes the affected part of the XML
  document would look as follows:

```

  <buttons>
    <name>OK, Cancel, Help</name>
  </buttons>
  <numberFormat pattern="###\,###.##"/>
```

  Because repeating elements is a natural pattern for XML documents
  using list splitting is rather untypical for this format.

The next section will show how data in a more complex XML
document can be processed.

<a id="userguide-howto_hierarchical--complex-hierarchical-structures"></a>

## Complex hierarchical structures

Consider the following scenario: An application operates on
database tables and wants to load a definition of the database
schema from its configuration. A XML document provides this
information. It could look as follows:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<database>
  <tables>
    <table tableType="system">
      <name>users</name>
      <fields>
        <field>
          <name>uid</name>
          <type>long</type>
        </field>
        <field>
          <name>uname</name>
          <type>java.lang.String</type>
        </field>
        <field>
          <name>firstName</name>
          <type>java.lang.String</type>
        </field>
        <field>
          <name>lastName</name>
          <type>java.lang.String</type>
        </field>
        <field>
          <name>email</name>
          <type>java.lang.String</type>
        </field>
      </fields>
    </table>
    <table tableType="application">
      <name>documents</name>
      <fields>
        <field>
          <name>docid</name>
          <type>long</type>
        </field>
        <field>
          <name>name</name>
          <type>java.lang.String</type>
        </field>
        <field>
          <name>creationDate</name>
          <type>java.util.Date</type>
        </field>
        <field>
          <name>authorID</name>
          <type>long</type>
        </field>
        <field>
          <name>version</name>
          <type>int</type>
        </field>
      </fields>
    </table>
  </tables>
</database>
```

This XML is quite self explanatory; there is an arbitrary number
of table elements, each of it has a name and a list of fields.
A field in turn consists of a name and a data type. This
XML document (let's call it `tables.xml`) can be
loaded in exactly the same way as the simple document in the
section before.

When we now want to access some of the properties we face a
problem: the syntax for constructing configuration keys we
learned so far is not powerful enough to access all of the data
stored in the tables document.

Because the document contains a list of tables some properties
are defined more than once. E.g. the configuration key
`tables.table.name` refers to a `name`
element inside a `table` element inside a
`tables` element. This constellation happens to
occur twice in the tables document.

Multiple definitions of a property do not cause problems and are
supported by all classes of Configuration. If such a property
is queried using `getProperty()`, the method
recognizes that there are multiple values for that property and
returns a collection with all these values. So we could write

```

Object prop = config.getProperty("tables.table.name");
if(prop instanceof Collection)
{
	System.out.println("Number of tables: " + ((Collection<?>) prop).size());
}
```

An alternative to this code would be the `getList()`
method of `Configuration`. If a property is known to
have multiple values (as is the table name property in this example), `getList()` allows retrieving all values at once.
**Note:** it is legal to call `getString()`
or one of the other getter methods on a property with multiple
values; it returns the first element of the list.

<a id="userguide-howto_hierarchical--accessing-structured-properties"></a>

## Accessing structured properties

Okay, we can obtain a list with the names of all defined
tables. In the same way we can retrieve a list with the names
of all table fields: just pass the key
`tables.table.fields.field.name` to the
`getList()` method. In our example this list
would contain 10 elements, the names of all fields of all tables.
This is fine, but how do we know, which field belongs to
which table?

When working with such hierarchical structures the configuration keys
used to query properties can have an extended syntax. All components
of a key can be appended by a numerical value in parentheses that
determines the index of the affected property. So if we have two
`table` elements we can exactly specify, which one we
want to address by appending the corresponding index. This is
explained best by some examples:

We will now provide some configuration keys and show the results
of a `getProperty()` call with these keys as arguments.

`tables.table(0).name`
:   Returns the name of the first table (all indices are 0 based),
    in this example the string *users*.

`tables.table(0)[@tableType]`
:   Returns the value of the tableType attribute of the first
    table (*system*).

`tables.table(1).name`
:   Analogous to the first example returns the name of the
    second table (*documents*).

`tables.table(2).name`
:   Here the name of a third table is queried, but because there
    are only two tables result is **null**. The fact that a
    **null** value is returned for invalid indices can be used
    to find out how many values are defined for a certain property:
    just increment the index in a loop as long as valid objects
    are returned.

`tables.table(1).fields.field.name`
:   Returns a collection with the names of all fields that
    belong to the second table. With such kind of keys it is
    now possible to find out, which fields belong to which table.

`tables.table(1).fields.field(2).name`
:   The additional index after field selects a certain field.
    This expression represents the name of the third field in
    the second table (*creationDate*).

`tables.table.fields.field(0).type`
:   This key may be a bit unusual but nevertheless completely
    valid. It selects the data types of the first fields in all
    tables. So here a collection would be returned with the
    values [*long, long*].

These examples should make the usage of indices quite clear.
Because each configuration key can contain an arbitrary number
of indices it is possible to navigate through complex structures of
hierarchical configurations; each property can be uniquely identified.

<a id="userguide-howto_hierarchical--sub-configurations"></a>

## Sub Configurations

Sometimes dealing with long property keys may become inconvenient, especially if always the same properties are accessed. For this
case `HierarchicalConfiguration` provides a short cut
with the `configurationAt()` method. This method can
be passed a key that selects exactly one node of the hierarchy
of nodes contained in a hierarchical configuration. Then a new
hierarchical configuration will be returned whose root node is
the selected node. So all property keys passed into that
configuration should be relative to the new root node. For
instance, if we are only interested in information about the
first database table, we could do something like that:

```

HierarchicalConfiguration<ImmutableNode> sub = config.configurationAt("tables.table(0)");
String tableName = sub.getString("name");  // only need to provide relative path
List<Object> fieldNames = sub.getList("fields.field.name");
```

For dealing with complex list-like structures there is another
short cut. Often it will be necessary to iterate over all items
in the list and access their (sub) properties. A good example are
the fields of the tables in our demo configuration. When you want
to process all fields of a table (e.g. for constructing a
`CREATE TABLE` statement), you will need all information
stored for them in the configuration. An option would be to use
the `getList()` method to fetch the required data one
by one:

```

List<Object> fieldNames = config.getList("tables.table(0).fields.field.name");
List<Object> fieldTypes = config.getList("tables.table(0).fields.field.type");
List<Object> ... // further calls for other data that might be stored in the config
```

But this is not very readable and will fail if not all field
elements contain the same set of data (for instance the
`type` property may be optional, then the list for
the types can contain less elements than the other lists). A
solution to these problems is the `configurationsAt()`
method, a close relative to the `configurationAt()`
method covered above. This method evaluates the passed in key and
collects all configuration nodes that match this criterion. Then
for each node a `HierarchicalConfiguration` object is
created with this node as root node. A list with these configuration
objects is returned. As the following example shows this comes in
very handy when processing list-like structures:

```
List<HierarchicalConfiguration<ImmutableNode>> fields =config.configurationsAt("tables.table(0).fields.field"); for(HierarchicalConfiguration sub : fields) {// sub contains all data about a single field String fieldName = sub.getString("name"); String fieldType = sub.getString("type"); ...
```

Per default, the configurations returned by the `configurationAt()` and
`configurationsAt()` methods are a kind of snapshots of
the data stored in the original configuration. If the original
configuration is later changed, these changes are not visible in the
sub configuration and vice versa. If configuration settings just need
to be read, this is fine.

It is also possible to connect a sub configuration more directly to
its original configuration. This is done by using overloaded versions
of `configurationAt()` and `configurationsAt()`
which accept an additional **boolean** parameter. If
here the value **true** is passed, a special
configuration implementation is returned (in fact, an instance of the
`SubnodeConfiguration` class) that operates on the same
data structures as the original configuration. Therefore, changes made
on one configuration are directly reflected by the other one.

Connecting a sub configuration with its parent configuration in the
described way is useful in use cases in which configurations are
updated. However, there can be pretty drastic updates which break
such a connection. As an example, consider the case that a sub
configuration is created for a certain sub tree of an original
configuration. Now this sub tree gets removed from the original
configuration. In this case, the sub configuration becomes detached
from its parent. Its content is not changed, but it is now again like
a snapshot or a copy of the original. This is demonstrated again in
the following example:

```

// sub points to the 2nd table
HierarchicalConfiguration<ImmutableNode> sub = config.configurationAt("tables.table(1)", true);
assertEquals("documents", sub.getString("name"));

// Now change name in parent configuration => should be visible in sub config
config.setProperty("tables.table(1).name", "tasks");
assertEquals("tasks", sub.getString("name"));

// Clear the whole content of the 2nd table
config.clearTree("tables.table(1)");
// The key used to create the sub configuration is no longer valid,
// so it is now detacted; it contains the recent data.
assertEquals("tasks", sub.getString("name"));
```

This example uses the `clearTree()` method of
`HierarchicalConfiguration` to remove all information
about the second database table from the configuration data. While
`clearProperty()` only removes the value of a property, `clearTree()` also removes all child elements and their
children recursively. After this operation the key
*tables.table(1)* specified when the sub configuration was
created no longer points to an existing element; therefore, the
sub configuration gets detached. Once detached, a sub configuration
cannot be reconnected to its parent again. Even if another table
element was added (making the sub key valid again), the sub
configuration remains detached.

<a id="userguide-howto_hierarchical--adding-new-properties"></a>

## Adding new properties

So far we have learned how to use indices to avoid ambiguities when
querying properties. The same problem occurs when adding new
properties to a structured configuration. As an example let's
assume we want to add a new field to the second table. New properties
can be added to a configuration using the `addProperty()`
method. Of course, we have to exactly specify where in the tree like structure new
data is to be inserted. A statement like

```

// Warning: This might cause trouble!
config.addProperty("tables.table.fields.field.name", "size");
```

would not be sufficient because it does not contain all needed
information. How is such a statement processed by the
`addProperty()` method?

`addProperty()` splits the provided key into its
single parts and navigates through the properties tree along the
corresponding element names. In this example it will start at the
root element and then find the `tables` element. The
next key part to be processed is `table`, but here a
problem occurs: the configuration contains two `table`
properties below the `tables` element. To get rid off
this ambiguity an index can be specified at this position in the
key that makes clear, which of the two properties should be
followed. `tables.table(1).fields.field.name` e.g.
would select the second `table` property. If an index
is missing, `addProperty()` always follows the last
available element. In our example this would be the second
`table`, too.

The following parts of the key are processed in exactly the same
manner. Under the selected `table` property there is
exactly one `fields` property, so this step is not
problematic at all. In the next step the `field` part
has to be processed. At the actual position in the properties tree
there are multiple `field` (sub) properties. So we here
have the same situation as for the `table` part.
Because no explicit index is defined the last `field`
property is selected. The last part of the key passed to
`addProperty()` (`name` in this example)
will always be added as new property at the position that has
been reached in the former processing steps. So in our example
the last `field` property of the second table would
be given a new `name` sub property and the resulting
structure would look like the following listing:

```

	...
    <table tableType="application">
      <name>documents</name>
      <fields>
        <field>
          <name>docid</name>
          <type>long</type>
        </field>
        <field>
          <name>name</name>
          <type>java.lang.String</type>
        </field>
        <field>
          <name>creationDate</name>
          <type>java.util.Date</type>
        </field>
        <field>
          <name>authorID</name>
          <type>long</type>
        </field>
        <field>
          <name>version</name>
          <name>size</name>    <== Newly added property
          <type>int</type>
        </field>
      </fields>
    </table>
  </tables>
</database>
```

This result is obviously not what was desired, but it demonstrates
how `addProperty()` works: the method follows an
existing branch in the properties tree and adds new leaves to it.
(If the passed in key does not match a branch in the existing tree, a new branch will be added. E.g. if we pass the key
`tables.table.data.first.test`, the existing tree can be
navigated until the `data` part of the key. From here a
new branch is started with the remaining parts `data`, `first` and `test`.)

If we want a different behavior, we must explicitly tell
`addProperty()` what to do. In our example with the
new field our intension was to create a new branch for the
`field` part in the key, so that a new `field`
property is added to the structure rather than adding sub properties
to the last existing `field` property. This can be
achieved by specifying the special index `(-1)` at the
corresponding position in the key as shown below:

```

config.addProperty("tables.table(1).fields.field(-1).name", "size");
config.addProperty("tables.table(1).fields.field.type", "int");
```

The first line in this fragment specifies that a new branch is
to be created for the `field` property (index -1).
In the second line no index is specified for the field, so the
last one is used - which happens to be the field that has just
been created. So these two statements add a fully defined field
to the second table. This is the default pattern for adding new
properties or whole hierarchies of properties: first create a new
branch in the properties tree and then populate its sub properties.
As an additional example let's add a complete new table definition
to our example configuration:

```

// Add a new table element and define the name
config.addProperty("tables.table(-1).name", "versions");

// Add a new field to the new table
// (an index for the table is not necessary because the latest is used)
config.addProperty("tables.table.fields.field(-1).name", "id");
config.addProperty("tables.table.fields.field.type", "int");

// Add another field to the new table
config.addProperty("tables.table.fields.field(-1).name", "date");
config.addProperty("tables.table.fields.field.type", "java.sql.Date");
...
```

For more information about adding properties to a hierarchical
configuration also have a look at the javadocs for
`HierarchicalConfiguration`.

<a id="userguide-howto_hierarchical--escaping-special-characters"></a>

## Escaping special characters

Some characters in property keys or values require a special
treatment.

Per default the dot character is used as delimiter by most
configuration classes (we will learn how to change this for
hierarchical configurations in a later section). In some
configuration formats however, dots can be contained in the
names of properties. For instance, in XML the dot is a legal
character that can occur in any tag. The same is true for the names
of properties in windows ini files. So the following XML
document is completely valid:

```

<?xml version="1.0" encoding="ISO-8859-1" ?>

<configuration>
  <test.value>42</test.value>
  <test.complex>
    <test.sub.element>many dots</test.sub.element>
  </test.complex>
</configuration>
```

This XML document can be loaded by `XMLConfiguration`
without trouble, but when we want to access certain properties
we face a problem: The configuration claims that it does not
store any values for the properties with the keys
`test.value` or `test.complex.test.sub.element`!

Of course, it is the dot character contained in the property
names, which causes this problem. A dot is always interpreted
as a delimiter between elements. So given the property key
`test.value` the configuration would look for an
element named `test` and then for a sub element
with the name `value`. To change this behavior it is
possible to escape a dot character, thus telling the configuration
that it is really part of an element name. This is simply done
by duplicating the dot. So the following statements will return
the desired property values:

```

int testVal = config.getInt("test..value");
String complex = config.getString("test..complex.test..sub..element");
```

Note the duplicated dots wherever the dot does not act as
delimiter. This way it is possible to access properties containing
dots in arbitrary combination. However, as you can see, the
escaping can be confusing sometimes. So if you have a choice, you should avoid dots in the tag names of your XML configuration
files or other configuration sources.

<a id="userguide-howto_hierarchical--internal-representation"></a>

## Internal Representation

You might have noted that the
`HierarchicalConfiguration` interface has a type parameter
defining the type of nodes it operates on. Internally, the nodes build up
a tree structure on which queries or manipulating operations can be
executed. There is an abstract base class
`AbstractHierarchicalConfiguration` implementing a major part of
the provided functionality in terms of abstract node objects. These nodes
are not directly accessed, but via a so-called
`NodeHandler`. The `NodeHandler` interface defines a
number of methods for accessing properties of a node like its name, its
value, or its children in a generic way.

This constellation makes it possible to integrate hierarchical configurations
with different hierarchical data structures, e.g. file systems, JNDI, etc.
The standard configurations shipped with *Commons Configuration*
mainly use an in-memory representation of their data based on the
`ImmutableNode` class. There is a special base class for
configurations of this type called
`BaseHierarchicalConfiguration`. As the name implies, the nodes
used by these configurations are immutable; this is beneficial especially
when it comes to [concurrent
access](#userguide-howto_concurrency--special_cases). It is possible to obtain the root node of a
`BaseHierarchicalConfiguration` object as shown in the
following example, but this is necessary for very special use cases only
because the most typical queries and manipulations can be done via the
`HierarchicalConfiguration` interface.

```

// config is of type BaseHierarchicalConfiguration
ImmutableNode root = config.getNodeModel().getNodeHandler().getRootNode();
```

<a id="userguide-howto_hierarchical--expression-engines"></a>

## Expression engines

In the previous chapters we saw many examples about how properties
in a `XMLConfiguration` object (or more general in a
`HierarchicalConfiguration` object, because this is the
base interface, which defines this functionality) can be queried or
modified using a special syntax for the property keys. Well, this
was not the full truth. Actually, property keys are not processed
by the configuration object itself, but are delegated to a helper
object, a so called *Expression engine*.

The separation of the task of interpreting property keys into a
helper object is a typical application of the *Strategy*
design pattern. In this case it also has the advantage that it
becomes possible to plug in different expression engines into a
`HierarchicalConfiguration` object. So by providing
different implementations of the
`ExpressionEngine`
interface hierarchical configurations can support alternative
expression languages for accessing their data.

Before we discuss the available expression engines that ship
with Commons Configuration, it should be explained how an
expression engine can be associated with a configuration object.
`HierarchicalConfiguration` and all implementing classes
provide a `setExpressionEngine()` method, which expects
an implementation of the `ExpressionEngine` interface as
argument. After this method was called, the configuration object will
use the passed expression engine, which means that all property keys
passed to methods like `getProperty()`, `getString()`, or `addProperty()` must
conform to the syntax supported by this engine. Property keys
returned by the `getKeys()` method will follow this
syntax, too.

The recommended approach is that a configuration object is fully
initialized by the [configuration
builder](#userguide-howto_builders) which creates it. The initialization parameters for
hierarchical configurations allow setting the expression engine as
shown in the following code fragment (more information about
initialization parameters for hierarchical and XML configurations
is provided in a later section in this chapter):

```

Parameters params = new Parameters();
FileBasedConfigurationBuilder<XMLConfiguration> builder =
    new FileBasedConfigurationBuilder<BaseHierarchicalConfiguration>(BaseHierarchicalConfiguration.class)
    .configure(params.hierarchical()
        .setExpressionEngine(new MyExpressionEngine()));
```

Remember that it is possible to define
[Default
Initialization Parameters](#userguide-howto_builders--default_initialization_parameters) for specific configuration classes.
Using this mechanism, it is possible to instance to set a special
expression engine for all XML configurations used by an
application.

**The default expression engine**

The syntax described so far for property keys of hierarchical
configurations is implemented by a specific implementation of the
`ExpressionEngine` interface called
`DefaultExpressionEngine`. An instance of this class
is used by the base implementation of
`HierarchicalConfiguration` if no specific expression
engine was set (which is the reason why our examples above worked).

After reading the examples of property keys provided so far in
this document you should have a sound understanding regarding
the features and the syntax supported by the
`DefaultExpressionEngine` class. But it can do a
little bit more for you: it defines a bunch of settings, which can be used to customize most tokens that can appear in a
valid property key. You prefer curly brackets over paranthesis
as index markers? You find the duplicated dot as escaped
property delimiter counter-intuitive? Well, simply go ahead and
change it! The following example shows how the syntax of a
`DefaultExpressionEngine` object is modified. The
key is to create an instance of the
`DefaultExpressionEngineSymbols` class and to
initialize it with the desired syntax elements. This is done
using a builder approach:

```

DefaultExpressionEngineSymbols symbols =
    new DefaultExpressionEngineSymbols.Builder(
        DefaultExpressionEngineSymbols.DEFAULT_SYMBOLS)
        // Use a slash as property delimiter
        .setPropertyDelimiter("/")
        // Indices should be specified in curly brackets
        .setIndexStart("{")
        .setIndexEnd("}")
        // For attributes use simply a @
        .setAttributeStart("@")
        .setAttributeEnd(null)
        // A Backslash is used for escaping property delimiters
        .setEscapedDelimiter("\\/")
        .create();
DefaultExpressionEngine engine = new DefaultExpressionEngine(symbols);

// Now create a configuration using this expression engine
Parameters params = new Parameters();
FileBasedConfigurationBuilder<XMLConfiguration> builder =
    new FileBasedConfigurationBuilder<XMLConfiguration>(XMLConfiguration.class)
    .configure(params.xml()
        .setFileName("tables.xml")
        .setExpressionEngine(engine));
XMLConfiguration config = builder.getConfiguration();

// Access properties using the new syntax
String tableName = config.getString("tables/table{0}/name");
String tableType = config.getString("tables/table{0}@type");
         
```

`DefaultExpressionEngineSymbol` objects are
immutable; the same is true for `DefaultExpressionEngine`.
Thus a single expression engine instance can be shared between
multiple configuration instances. The example fragment shows the
typical usage pattern for constructing new
`DefaultExpressionEngine` instances with an alternative
syntax: A builder for a symbols object is constructed passing in
an instance that serves as starting point - here the constant
`DEFAULT_SYMBOLS` is used which defines the standard
syntax. Then methods of the builder are used to modify only the
settings which are to be adapted.

*Tip:* Sometimes when processing an XML document you
don't want to distinguish between attributes and "normal"
child nodes. You can achieve this by setting the
`AttributeEnd` property to **null** and the
`AttributeStart` property to the same value as the
`PropertyDelimiter` property. Then the syntax for
accessing attributes is the same as the syntax for other
properties:

```

DefaultExpressionEngineSymbols symbolsNoAttributes =
    new DefaultExpressionEngineSymbols.Builder(
        DefaultExpressionEngineSymbols.DEFAULT_SYMBOLS)
        .setAttributeStart(
            DefaultExpressionEngineSymbols.DEFAULT_SYMBOLS.getPropertyDelimiter())
        .setAttributeEnd(null)
        .create();
DefaultExpressionEngine engine = new DefaultExpressionEngine(symbolsNoAttributes);
...
Object value = config.getProperty("tables.table(0).name");
// name can either be a child node of table or an attribute
         
```

There is another property which can be used to customize an
instance of `DefaultExpressionEngine`: the *node
name matcher*. This is an object implementing the
`NodeMatcher` interface which controls how the names of
configuration nodes are matched against the single parts of a
configuration key. It can be passed as an optional second argument
to the constructor. Per default, an exact match is performed, i.e.
in order to successfully resolve a key like *tables.table.name*, there has to be a node named *tables* with a child node
named *table* which in turn has a child with the name
*name* - this is what most people would expect.

There are use cases, however, when more flexibility or tolerance
is desired. For instance, applications under Windows storing their
settings in ini files sometimes expect that they can access keys
in a case insensitive manner. The node name matcher can help
here. The enumeration class
`NodeNameMatchers` defines some standard matchers which
can collaborate with `DefaultExpressionEngine`. In
addition to the `EQUALS` matcher used by default, there
is also an `EQUALS_IGNORE_CASE` matcher. According to
its name, this matcher ignores case when matching configuration
keys against nodes. The following fragment shows how this matcher
can be enabled (we use an `INIConfiguration` as
example here, but this technique works with all other hierarchical
configurations, too):

```

DefaultExpressionEngine engine = new DefaultExpressionEngine(
  DefaultExpressionEngineSymbols.DEFAULT_SYMBOLS,
  NodeNameMatchers.EQUALS_IGNORE_CASE);

Parameters params = new Parameters();
FileBasedConfigurationBuilder<INIConfiguration> builder =
    new FileBasedConfigurationBuilder<INIConfiguration>(INIConfiguration.class)
    .configure(params.hierarchical()
        .setFileName("settings.ini")
        .setExpressionEngine(engine));
INIConfiguration config = builder.getConfiguration();

// Access properties no matter of their concrete case
String backGroundColor = config.getString("colors.background");
String foreGroundColor = config.getString("COLORS.ForeGround");
         
```

**The XPATH expression engine**

The expression language provided by the `DefaultExpressionEngine`
class is powerful enough to address all properties in a
hierarchical configuration, but it is not always convenient to
use. Especially if list structures are involved, it is often
necessary to iterate through the whole list to find a certain
element.

Think about our example configuration that stores information about
database tables. A use case could be to load all fields that belong
to the "users" table. If you knew the index of this
table, you could simply build a property key like
`tables.table(<index>).fields.field.name`, but how do you find out the correct index? When using the
default expression engine, the only solution to this problem is
to iterate over all tables until you find the "users"
table.

Life would be much easier if an expression language could be used, which would directly support queries of such kind. In the XML
world, the XPATH syntax has grown popular as a powerful means
of querying structured data. In XPATH a query that selects all
field names of the "users" table would look something
like `tables/table[@name='users']/fields/name` (here
we assume that the table's name is modelled as an attribute).
This is not only much simpler than an iteration over all tables, but also much more readable: it is quite obvious, which fields
are selected by this query.

Given the power of XPATH it is no wonder that we got many
user requests to add XPATH support to *Commons Configuration*.
Well, here is it!

For enabling XPATH syntax for property keys you need the
`XPathExpressionEngine` class. This class
implements the `ExpressionEngine` interface and can
be plugged into a `HierarchicalConfiguration` object
in the same way as described above. Because instances of
`XPathExpressionEngine` are thread-safe and can be
shared between multiple configuration objects it is also
possible to set an instance as the default expression engine
in the [default initialization parameters](#userguide-howto_builders--default_initialization_parameters) for configuration
builders, so that all hierarchical configuration
objects make use of XPATH syntax. The following code fragment
shows how XPATH support can be enabled for a configuration
object:

```

Parameters params = new Parameters();
FileBasedConfigurationBuilder<XMLConfiguration> builder =
    new FileBasedConfigurationBuilder<XMLConfiguration>(XMLConfiguration.class)
    .configure(params.xml()
        .setFileName("tables.xml")
        .setExpressionEngine(new XPathExpressionEngine()));
XMLConfiguration config = builder.getConfiguration();

// Now we can use XPATH queries:
List<Object> fields = config.getList("tables/table[1]/fields/name");
         
```

XPATH expressions are not only used for selecting properties
(i.e. for the several getter methods), but also for adding new
properties. For this purpose the keys passed into the
`addProperty()` method must conform to a special
syntax. They consist of two parts: the first part is an
arbitrary XPATH expression that selects the node where the new
property is to be added to, the second part defines the new
element to be added. Both parts are separated by whitespace.

Okay, let's make an example. Say, we want to add a `type`
property under the first table (as a sibling to the `name`
element). Then the first part of our key will have to select
the first table element, the second part will simply be
`type`, i.e. the name of the new property:

```

config.addProperty("tables/table[1] type", "system");
         
```

(Note that indices in XPATH are 1-based, while in the default
expression language they are 0-based.) In this example the part
`tables/table[1]` selects the target element of the
add operation. This element must exist and must be unique, otherwise an exception
will be thrown. `type` is the name of the new element
that will be added. If instead of a normal element an attribute
should be added, the example becomes

```

config.addProperty("tables/table[1] @type", "system");
         
```

It is possible to add complete paths at once. Then the single
elements in the new path are separated by "/"
characters. The following example shows how data about a new
table can be added to the configuration. Here we use full paths:

```

// Add new table "tasks" with name element and type attribute
config.addProperty("tables table/name", "tasks");
// last() selects the last element of this name,
// which is the newest table element
config.addProperty("tables/table[last()] @type", "system");

// Now add fields
config.addProperty("tables/table[last()] fields/field/name", "taskid");
config.addProperty("tables/table[last()]/fields/field[last()] type", "int");
config.addProperty("tables/table[last()]/fields field/name", "name");
config.addProperty("tables/table[last()]/fields field/name", "startDate");
...
         
```

The first line of this example adds the path `table/name`
to the `tables` element, i.e. a new `table`
element will be created and added as last child to the
`tables` element. Then a new `name` element
is added as child to the new `table` element. To this
element the value "tasks" is assigned. The next line
adds a `type` attribute to the new table element. To
obtain the correct `table` element, to which the
attribute must be added, the XPATH function `last()`
is used; this function selects the last element with a given
name, which in this case is the new `table` element.
The following lines all use the same approach to construct a new
element hierarchy: At first complete new branches are added
(`fields/field/name`), then to the newly created
elements further children are added.

There is one gotcha with these keys described so far: they do
not work with the `setProperty()` method! This is
because `setProperty()` has to check whether the
passed in key already exists; therefore it needs a key which can
be interpreted by query methods. If you want to use
`setProperty()`, you can pass in regular keys (i.e.
without a whitespace separator). The method then tries to figure
out which part of the key already exists in the configuration
and adds new nodes as necessary. In principle such regular keys
can also be used with `addProperty()`. However, they
do not contain sufficient information to decide where new nodes
should be added.

To make this clearer let's go back to the example with the
tables. Consider that there is a configuration which already
contains information about some database tables. In order to add
a new table element in the configuration
`addProperty()` could be used as follows:

```

config.addProperty("tables/table/name", "documents");
         
```

In the configuration a `<tables>` element
already exists, also `<table>` and
`<name>` elements. How should the expression
engine know where new node structures are to be added? The
solution to this problem is to provide this information in the
key by stating:

```

config.addProperty("tables table/name", "documents");
         
```

Now it is clear that new nodes should be added as children of
the `<tables>` element. More information about
keys and how they play together with `addProperty()`
and `setProperty()` can be found in the Javadocs for
[`XPathExpressionEngine`](https://commons.apache.org/proper/commons-configuration/apidocs/org/apache/commons/configuration2/tree/xpath/XPathExpressionEngine.html).

*Note:* XPATH support is implemented through
[Commons JXPath](https://commons.apache.org/jxpath).
So when making use of this feature, be sure you include the
commons-jxpath jar in your classpath.

In this tutorial we don't want to describe XPATH syntax and
expressions in detail. Please refer to corresponding documentation.
It is important to mention that by embedding Commons JXPath the
full extent of the XPATH 1.0 standard can be used for constructing
property keys.

<a id="userguide-howto_hierarchical--builder-configuration-related-to-hierarchical-configurations"></a>

## Builder Configuration Related to Hierarchical Configurations

There is special support for the initialization parameters of
configuration builders for hierarchical configurations. The
`HierarchicalBuilderProperties` interface defines additional
settings applicable to hierarchical configurations. Currently, the
[expression engine](#userguide-howto_hierarchical--expression_engines) can be set.

A parameters object for a hierarchical configuration can be obtained using
the `hierarchical()` method of a
`Parameters` instance. It returns an object implementing the
`HierarchicalBuilderParameters` interface which contains set
methods for all the available properties, including the ones inherited
from base interfaces.

---

<a id="userguide-howto_multitenant"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_multitenant.html -->

<!-- page_index: 20 -->

<a id="userguide-howto_multitenant--multi-tenant-configurations"></a>

# Multi-tenant Configurations

In a multi-tenant environment a single instance of the application
will run on behalf of many clients. Typically, this will require
that each client has its own unique configuration. The easiest
approach to enable an application to be multi-tenant is for it
to not really be aware of it at all. This requires that the
configuration framework takes on some of the responsibility for
making the application work correctly.

One approach to enable this support in a web application might be
to use a Servlet Filter and then use the Log4j or SLF4J MDC to
save the attributes needed to identify the client. These attributes
can then be used to identify the specific client configuration to
be used. The classes described below use this technique to allow
configurations to transparently provide the configuration appropriate
for the clients.

<a id="userguide-howto_multitenant--multifileconfigurationbuilder"></a>

## MultiFileConfigurationBuilder

`MultiFileConfigurationBuilder` is a specialized configuration
builder implementation which internally manages a set of builders for
[file-based configurations](#userguide-howto_filebased). In the
initialization parameters of this builder a file name pattern has to
be passed. The pattern can contain keys that will be resolved using the
`ConfigurationInterpolator` every time the builder's
`getConfiguration()` method is called. The resolved pattern
is then interpreted as the name of a configuration file to be loaded
by a newly created `FileBasedConfigurationBuilder`.

The file-based configuration builder is stored in an internal map
together with the naming pattern. The next time the same pattern is
accessed, it can be retrieved from the map and used directly. If the
evaluation of the pattern changes, a new file-based configuration
builder is created, and a new configuration file is loaded.

When used in a [combined
configuration](https://commons.apache.org/proper/commons-configuration/userguide/howto_configurationbuilder.html) it is often acceptable for a file
matching a particular pattern to be missing. The behavior of
`MultiFileConfigurationBuilder` regarding exceptions
thrown for missing configuration files can be controlled using the
boolean *allowFailOnInit* argument accepted by the most generic
constructor. If here the value **true** is passed, exceptions while loading a configuration file are ignored. Instead, an empty configuration of the configured type is created for this
pattern.

<a id="userguide-howto_multitenant--dynamiccombinedconfiguration"></a>

## DynamicCombinedConfiguration

The `CombinedConfigurationBuilder` class allows multiple configuration files to be
merged together. However, it will not collaborate with a `MultiFileConfiguration`
properly since the underlying managed configuration will be different depending
on the resolution of the location pattern.
`DynamicCombinedConfiguration` solves this by creating a new
`CombinedConfiguration` for each pattern.

<a id="userguide-howto_multitenant--sample-configuration"></a>

## Sample Configuration

This sample configuration illustrates how to use
`CombinedConfigurationBuilder`
in combination with
`MultiFileConfigurationBuilder` to create a multi-tenant
configuration.

```

<configuration>
  <header>
    <result loggerName="TestLogger"
            config-class="org.apache.commons.configuration2.DynamicCombinedConfiguration"
            keyPattern="$${sys:Id}">
      <nodeCombiner config-class="org.apache.commons.configuration2.tree.MergeCombiner"/>
      <expressionEngine
          config-class="org.apache.commons.configuration2.tree.xpath.XPathExpressionEngine"/>
    </result>
  </header>
  <override>
    <multiFile filePattern="testMultiConfiguration_$${sys:Id}.xml"
               config-name="clientConfig" config-optional="true"
               config-forceCreate="true"
               schemaValidation="true">
       <expressionEngine
          config-class="org.apache.commons.configuration2.tree.xpath.XPathExpressionEngine"/>
    </multiFile>
    <xml fileName="testMultiConfiguration_default.xml"
         config-name="defaultConfig" schemaValidation="true">
      <expressionEngine
          config-class="org.apache.commons.configuration2.tree.xpath.XPathExpressionEngine"/>
    </xml>
  </override>
</configuration>
```

In this example configuration definition file for a
`CombinedConfigurationBuilder` two configuration sources
are declared:

- A multi-file source with a file pattern containing a system
  property. This means that depending on the current value of this
  system property a different configuration file is loaded. Because
  this source is declared as optional it is legal that for certain
  values of the property no configuration file exists.
- An XML configuration source with common setting independent on
  the value of a system property. This source may also contain
  default values in case no configuration file could be loaded by the
  multi-file source.

Of special importance is the declaration of the result configuration
in form of the `<result>` element in the *header*
section. Here the `config-class` attribute specifies that
an instance of `DynamicCombinedConfiguration` is created
rather than a default `CombinedConfiguration` object. Also, the value of the *keyPattern* property is set which has to
conform to the pattern used by the multi-file source.

Note how the variables have multiple '$'. This is how variables are escaped and
is necessary because the variables will be interpolated multiple times. Each
attempt will remove the leading '$'. When there is only a single '$' in front
of the '{' the interpolator will then resolve the variable. The first extra '$'
is necessary because `CombinedConfigurationBuilder` will interpolate any variables
in the configuration. In the case of the multi-file configuration item two
leading '$' characters are necessary before the variable because it will be
interpolated by both `CombinedConfigurationBuilder` and `DynamicCombinedConfiguration`
before `MultiFileConfigurationBuilder` gets the chance to evaluate it.
Although in this example one would not expect system properties to change
at runtime, other types of lookups such as the MDCStrLookup provided with
SLF4J require that the variables be evaluated as the configuration is being
accessed instead of when the configuration file is processed to behave as desired.

<a id="userguide-howto_multitenant--builder-configuration-related-to-multi-file-configurations"></a>

## Builder Configuration Related to Multi-file Configurations

When setting up a
`MultiFileConfigurationBuilder` a special object with
initialization parameters can be used as argument to the
`configure()` method. It is of type
`MultiFileBuilderParameters` and can be obtained via the
`multiFile()` method of a
`Parameters` object. The properties specific to this
configuration type are defined by the
`MultiFileBuilderProperties` interface. They include

- The pattern string for determining the name of the
  configuration file to be loaded. This is of course the most
  important setting as it tells the builder how to perform interpolation
  in order to resolve the correct configuration file.
- A parameters object for the file-based configuration builder
  used behind the scenes to load the configuration file. Here some
  additional settings can be provided. For instance, if the
  configuration files to be loaded are XML documents, validation
  could be enabled via these parameters.

Below is a code fragment demonstrating the set up of a
`MultiFileConfigurationBuilder` which loads configuration
files of type XML:

```

Parameters params = new Parameters();
MultiFileConfigurationBuilder<XMLConfiguration> builder =
    new MultiFileConfigurationBuilder(XMLConfiguration.class)
    .configure(params.multiFile()
        .setFilePattern("configuration_${sys:Id}.xml")
        .setManagedBuilderParameters(params.xml()
            .setValidating(true)
        )
    );

XMLConfiguration config = builder.getConfiguration();
```

<a id="userguide-howto_multitenant--patternsubtreeconfigurationwrapper"></a>

## PatternSubtreeConfigurationWrapper

Applications are often composed of many components each of which need their
own configuration. This can be accommodated by having a configuration file
per component, but this can make things hard to manage when there are many
clients and many components. A second approach is to combine them into
a single configuration file. However, this either means the subcomponent
has to be aware of the surrounding configuration and navigate past it or the
application must be provided just the portion of the configuration it
can process. `PatternSubtreeConfigurationWrapper` can be used for this purpose.

Normal practice when using dependency injection frameworks is to have the
attributes needed to make components work correctly injected into them.
When working with Commons Configuration this works very well. Components
simply need to have a
`HierarchicalConfiguration` attribute along with
a corresponding setter and getter. The injection framework can then be
used to provide the component with the correct configuration using
`PatternSubtreeConfigurationWrapper` as shown in the next example.

```

  <bean id="configurationBuilder"
        class="org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder">
    <constructor-arg index="0"
      value="org.apache.commons.configuration2.XMLConfiguration"/>
    <constructor-arg index="1">
        <map>
            <entry key="config-fileBased">
                <map>
                    <entry key="fileName" value="configuration.xml"/>
                </map>
            </entry>
        </map>
    </constructor-arg>
  </bean>
  <bean id="applicationConfig" factory-bean="configurationBuilder"
        factory-method="getConfiguration">
  </bean>
  <bean id="subcomponentConfig"
        class="org.apache.commons.configuration2.PatternSubtreeConfigurationWrapper"
        autowire='autodetect'>
    <constructor-arg index="0">
      <ref bean="applicationConfig"/>
    </constructor-arg>
    <constructor-arg index="1" value="/Components/MyComponent"/>
  </bean>
  <bean id='MyComponent' class='org.test.MyComponent' autowire='autodetect'>
    <property name="configuration">
      <ref bean="subcomponentConfig"/>
    </property>
  </bean>
```

This example shows a [Spring](https://spring.io/)
configuration defining beans to be used in an application. The bean
named "MyComponent" is a component with its own
configuration which is injected into the *configuration*
property. Here an instance of `PatternSubtreeConfigurationWrapper`
is passed (defined by the "subcomponentConfig" bean) that
selects a subtree in the configuration data specific to this component;
the corresponding prefix is defined as second constructor argument.

It is also of interest how the global configuration of the
application is defined. It is loaded by a configuration builder
declared by the "configurationBuilder" bean. The fluent
API offered by configuration builders does not work very well here.
Therefore, the builder is initialized via a map with settings passed
to its constructor. Simple properties to be propagated to the
managed configuration instance can be declared directly as keys of
this map. The configuration of the file to be loaded is an
exceptional case: This information is stored internally as a
`FileHandler` object, and the properties of this object are
contained in a sub map under the key *config-fileBased*.

With the declaration of the configuration builder in place, the actual
configuration object can now be defined as bean using the builder's
`getConfiguration()` method as factory method. From
there it can be injected into arbitrary other beans.

Copyright © 2001-2026
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Configuration, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="userguide-howto_properties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_properties.html -->

<!-- page_index: 21 -->

<a id="userguide-howto_properties--properties-files"></a>

# Properties files

Properties files are a popular means of configuring applications. Of course, *Commons Configuration*
supports this format and enhances significantly the basic `java.util.Properties` class.
This section introduces the features of the
`PropertiesConfiguration` class.
Note that `PropertiesConfiguration` is a very typical example
for an implementation of the `Configuration` interface; it
extends
`AbstractConfiguration`, thus all the features provided by this base class are available here as
well. More information about functionality common to all standard
`Configuration` implementations can be found in the section
[Basic features and AbstractConfiguration](#userguide-howto_basicfeatures).

<a id="userguide-howto_properties--using-propertiesconfiguration"></a>

## Using PropertiesConfiguration

Let's start with a simple properties file named
`usergui.properties` with the following content:

```

# Properties definining the GUI
colors.background = #FFFFFF
colors.foreground = #000080

window.width = 500
window.height = 300
```

To load this file, you'll write something like:

```
Parameters params = new Parameters(); FileBasedConfigurationBuilder<FileBasedConfiguration> builder =new FileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class) .configure(params.properties() .setFileName("usergui.properties")); try {Configuration config = builder.getConfiguration(); ...} catch(ConfigurationException cex) {// loading of the configuration file failed}
```

As is demonstrated by this example, a configuration object for a
properties file is obtained via a
`FileBasedConfigurationBuilder` as described in the section
[File-based Configurations](#userguide-howto_filebased).

After the properties file was loaded you can access its content through
the methods of the `Configuration` interface, e.g.

```

String backColor = config.getString("colors.background");
Dimension size = new Dimension(config.getInt("window.width"),
  config.getInt("window.height"));
```

<a id="userguide-howto_properties--includes"></a>

## Includes

If a property is named "`include`", and the value of that property is the
name of a file on the disk, that file will be included into the configuration.

The difference between "`include`" and "`includeOptional`" (below) is that if the file value
is absent, processing continues with "`includeOptional`" but stops with "`include`".

For example:

```

# usergui.properties

include = colors.properties
include = sizes.properties
```

```

# colors.properties

colors.background = #FFFFFF
```

<a id="userguide-howto_properties--oprional-includes"></a>

## Oprional Includes

If a property is named "`includeOptional`", and the value of that property is the
name of a file on the disk, that file will be included into the configuration.

The difference between "`include`" (above) and "`includeOptional`" is that if the file value
is absent, processing continues with "`includeOptional`" but stops with "`include`".

For example:

```

# usergui.properties

includeOptional = colors.properties
includeOptional = sizes.properties
```

```

# colors.properties

colors.background = #FFFFFF
```

<a id="userguide-howto_properties--lists-and-arrays"></a>

## Lists and arrays

As was already pointed out in the section
[List handling](#userguide-howto_basicfeatures--list_handling)
of *Basic features*, *Commons Configuration* has the ability to
return easily a list of values. For example, a properties file can
contain a list of comma separated values:

```

# chart colors
colors.pie = #FF0000, #00FF00, #0000FF
```

Provided that an appropriate
`ListDelimiterHandler` object was set for the
configuration instance, the value is split automatically, and
you can retrieve an array or a `java.util.List` directly with:

```

String[] colors = config.getStringArray("colors.pie");
List<Object> colorList = config.getList("colors.pie");
```

Splitting of string values at list delimiter characters is disabled
by default. It can be enabled by specifying an instance of
`DefaultListDelimiterHandler`. This can be done when loading
the configuration via the builder:

```

Parameters params = new Parameters();
FileBasedConfigurationBuilder<Configuration> builder =
    new FileBasedConfigurationBuilder<Configuration>(PropertiesConfiguration.class)
    .configure(params.properties()
        .setFileName("usergui.properties")
        .setListDelimiterHandler(new DefaultListDelimiterHandler(','));
Configuration config = builder.getConfiguration();
```

Alternatively, you can specify a list of values in your properties file by using
the same key on several lines as shown in the following example. This is an
example of a feature not provided by `java.util.Properties`:

```

# chart colors
colors.pie = #FF0000;
colors.pie = #00FF00;
colors.pie = #0000FF;
```

All of the features related to list handling described for
`AbstractConfiguration` also apply to properties files, including changing the list delimiter or disabling list handling at
all.

<a id="userguide-howto_properties--saving"></a>

## Saving

To save your configuration, just call the `save()` method
on the associated configuration builder.

```

Parameters params = new Parameters();
FileBasedConfigurationBuilder<FileBasedConfiguration> builder =
    new FileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class)
    .configure(params.properties()
        .setFileName("usergui.properties")
        .setListDelimiterHandler(new DefaultListDelimiterHandler(',')));
Configuration config = builder.getConfiguration();
config.setProperty("colors.background", "#000000");
builder.save();
```

More information about saving properties files (and file-based
configurations in general) can be found in the section about
[File-based Configurations](#userguide-howto_filebased).

<a id="userguide-howto_properties--special-characters-and-escaping"></a>

## Special Characters and Escaping

If you need a special character in a property like a line feed, a tabulation or
an unicode character, you can specify it with the same escaped notation used for
Java Strings. The list separator ("," by default), can also be escaped:

```

key = This \n string \t contains \, escaped \\ characters \u0020
```

When dealing with lists of elements that contain backslash characters
(e.g. file paths on Windows systems) escaping rules can become pretty
complex. The first thing to keep in mind is that in order to get a
single backslash, you have to write two:

```

config.dir = C:\\Temp\\
      
```

This issue is not specific to *Commons Configuration*, but is related to
the standard format for properties files. Refer to the Javadocs of the
`load()` method of `java.util.Properties` for more
information. Now if you want to define a list with file paths, you may
be tempted to write the following:

```

# Wrong way to define a list of directories
config.dirs = C:\\Temp\\,D:\\data\\
      
```

As the comment indicates, this will not work. The trailing backslash of
the first directory is interpreted as escape character for the list
delimiter. So instead of a list with two elements only a single value
of the property is defined - clearly not what was desired. To get a
correct list the trailing backslash has to be escaped. This is achieved
by duplicating it (yes, in a properties file that means that we now need
4 backslashes):

```

# Correct way to define a list of directories
config.dirs = C:\\Temp\\\\,D:\\data\\
      
```

So a sequence of 4 backslashes in the value of a property is interpreted
as an escaped backslash and eventually results in a single backslash.
This creates another problem when a properties file should refer to the
names of network shares. Typically these names start with two
backslashes, so the obvious way to define such a property is as follows:

```

# Wrong way to define a list of network shares
config.dirs = \\\\share1,\\\\share2
      
```

Unfortunately, this will not work because the shares contain the reserved
sequence of 4 backslashes. So when reading the value of the
*config.dirs* property a list with two elements is returned
starting only with a single backslash. To fix the problem the sequence
for escaping a backslash has to be duplicated - we are now at 8
backslashes:

```

# Correct way to define a list of network shares
config.dirs = \\\\\\\\share1,\\\\\\\\share2
      
```

As becomes obvious, escape sequences can become pretty complex and
unreadable. In such situations it is recommended to use the alternative
way of defining a list: just use the same key multiple times. In this
case no additional escaping of backslashes (beyond the usual duplicating
required by properties files) is needed because there is no list
delimiter character involved. Using this syntax the list of network
shares looks like the following:

```

# Straightforward way to define a list of network shares
config.dirs = \\\\share1
config.dirs = \\\\share2
      
```

Please also refer to the Javadocs of the
`DefaultListDelimiterHandler` class; it describes the
escaping rules to be applied in detail.

<a id="userguide-howto_properties--layout-objects"></a>

## Layout Objects

Each `PropertiesConfiguration` object is associated with a
*Layout object*, an instance of the class
`PropertiesConfigurationLayout`. This layout object is
responsible for preserving most of the structure of loaded configuration
files. This means that things like comments or blank lines in a saved
properties file will closely resemble the original properties file
(the algorithm is not 100 percent perfect, but for most use cases it
should be sufficient).

Normally a developer does not have to deal with these layout objects.
However, there are some methods that might be of interest if enhanced
control over the output of properties files is needed. The following
list describes these methods (note that corresponding get methods are
of course also provided):

- `setComment()`
  With this method a comment can be set for a specified property. When
  storing the configuration the comment is output before the property,
  followed by a line break. The comment can span multiple lines; in this
  case the newline character "\n" must be used as line
  separator.
- `setHeaderComment()`
  With `setHeaderComment()` a global comment can be set for the
  properties file. This comment is written at the very start of the file,
  followed by an empty line.
- `setFooterComment()`
  Analogous to `setHeaderComment()`, but the comment defined by
  this method is written at the very end of the properties file.
- `setBlancLinesBefore()`
  This methods allows defining the number of empty lines to be written
  before the specified property. It can be used, for instance, to
  divide the properties file into multiple logical sections.
- `setSingleLine()`
  If a property has multiple values, with `setSingleLine()` it
  can be specified that all these values should be written into a single
  line separated by the default list separator. It is also possible to
  write multiple definitions for this property (i.e. multiple lines of the
  form `property = value1`, `property = value2` etc.).
  This is supported by `PropertiesConfiguration`, but will
  probably not work when processing the properties file with other tools.
- `setForceSingleLine()`
  This is similar to `setSingleLine()`, but sets a global
  single line flag. If set to **true**, all properties with multiple
  values are always written on a single line.
- `setGlobalSeparator()`
  Sometimes it may be necessary to define the properties separator, i.e.
  the string that separates the property key from the value. This can be
  done using `setGlobalSeparator()`. Here an arbitrary string
  can be specified that will be used as separator. (Note: In order to
  produce valid properties files only the characters `=` and
  `:` should be used as separators (with or without leading or
  trailing whitespace), but the method does not enforce this.
- `setSeparator()`
  This method is similar to `setGlobalSeparator()`, but
  allows setting the property separator for a specific property.
- `setLineSeparator()`
  Using this method the line separator can be specified. Per default the
  platform-specific line separator is used (e.g. `\n` on Unix).

The default settings of `PropertiesConfigurationLayout` are
chosen in a way that most of the original layout of a properties file
is retained. With the methods listed above specific layout restrictions
can be enforced.

<a id="userguide-howto_properties--custom-properties-readers-and-writers"></a>

## Custom properties readers and writers

There are situations when more control over the process of reading and
writing properties files is needed. For instance, an application might
have to deal with some legacy properties file in a specific format, which is not supported out of the box by
`PropertiesConfiguration`, but must not be modified. In these
cases it is possible to inject a custom reader and writer for
properties files.

Per default properties files are read and written by the nested classes
`PropertiesReader` and `PropertiesWriter`
(defined within `PropertiesConfiguration`). These classes are
regular reader and writer classes (both are derived from typical base
classes of the `java.io` package) that provide some
additional methods making dealing with properties files more
convenient. Custom implementations of properties readers and writers
must extend these base classes.

For installing a custom properties reader or writer
`PropertiesConfiguration` provides the `IOFactory`
interface (which is also defined as a nested class). An object
implementing this interface is stored in each
`PropertiesConfiguration` instance. Whenever a properties
file is to be read or written (i.e. when one of the `load()`
or `save()` methods is called), the `IOFactory`
object is asked for creating the properties reader or writer to be
used.

The `IOFactory` interface is pretty simple; it defines one
method for creating a properties reader and another one for creating a
properties writer. A default implementation called
`DefaultIOFactory` is also available and is used by
`PropertiesConfiguration` when no specific
`IOFactory` is set.
The original goal of `PropertiesConfiguration` wasn't to be
strictly compatible with the exact file format defined in
`java.util.Properties` (JUP). However, in cases where this
compatibility is required, the alternative `JupIOFactory` can
be used, as it aims to mimic the exact behavior of `JUP`. The
main differences concern the handling of leading and trailing whitespace
and the handling of escape sequences. `JupIOFactory` can also
be configured to avoid Unicode escape sequences (like \u00DF) when
the used encoding already supports all characters natively. E.g. UTF-8
is the new default encoding for resource bundle properties files since
Java 9, so Unicode escapes are not required anymore and not using them
can make properties files much more readable in regular text editors.

To make this discussion more concrete we provide an example of how to
inject a custom properties reader. The use case is that we have to load
a properties file that contains keys with whitespace, which is not
supported by `PropertiesConfiguration` per default. A
fragment from such a properties file could look as follows:

```

Background Color = #800080
Foreground Color = #000080
```

The first step is to create a custom properties reader implementation
that can deal with such properties. The class is derived from
`PropertiesConfiguration.PropertiesReader` and overrides the
`parseProperty()` method:

```
public class WhitespacePropertiesReader extends PropertiesConfiguration.PropertiesReader {public WhitespacePropertiesReader(Reader in, char delimiter) {super(in, delimiter);}
/** * Special algorithm for parsing properties keys with whitespace. This * method is called for each non-comment line read from the properties * file.*/ @Override protected void parseProperty(String line) {// simply split the line at the first '=' character // (this should be more robust in production code) int pos = line.indexOf('='); String key = line.substring(0, pos).trim(); String value = line.substring(pos + 1).trim();
// now store the key and the value of the property initPropertyName(key); initPropertyValue(value);}}
```

Notice the calls to the methods `initPropertyName()` and
`initPropertyValue()`. Here the results of the parsing
operation are stored. The next step is to provide a specialized
implementation of the `IOFactory` interface that returns
the new properties reader class. As we only want to replace the
properties reader (and use the standard writer), we can derive our
implementation from `DefaultIOFactory` and thus only have
to override the `createPropertiesReader()` method.

```
public class WhitespaceIOFactory extends PropertiesConfiguration.DefaultIOFactory {/** * Return our special properties reader.*/ @Override public PropertiesReader createPropertiesReader(Reader in, char delimiter) {return new WhitespacePropertiesReader(in, delimiter);}}
```

Finally an instance of our new `IOFactory` implementation
has to be created and passed to the `PropertiesConfiguration`
object. This can be done via the initialization parameters passed to
the configuration builder:

```

Parameters params = new Parameters();
FileBasedConfigurationBuilder<Configuration> builder =
    new FileBasedConfigurationBuilder<Configuration>(PropertiesConfiguration.class)
    .configure(params.properties()
        .setFileName("myfile.properties")
        .setIOFactory(new WhitespaceIOFactory());
Configuration config = builder.getConfiguration();
```

<a id="userguide-howto_properties--builder-configuration-related-to-properties-files"></a>

## Builder Configuration Related to Properties Files

When setting up a configuration builder to produce a
`PropertiesConfiguration` instance typically an object
implementing the
`PropertiesBuilderParameters` interface is used. In addition
to the parameters common to all file-based configurations, there are
settings specific to properties files which are defined by the
`PropertiesBuilderProperties` interface. These include

- A flag whether [include files](#userguide-howto_properties--includes) are supported.
  This is **true** by default, but can be switched off if
  properties named *include* should not have a special meaning.
- A custom [layout object](#userguide-howto_properties--layout_objects).
- A custom [I/O
  factory](#userguide-howto_properties--custom_properties_readers_and_writers).

A parameters object for a properties configuration can be obtained using
the `properties()` method of a
`Parameters` instance

---

<a id="userguide-howto_reloading"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/howto_reloading.html -->

<!-- page_index: 22 -->

<a id="userguide-howto_reloading--automatic-reloading-of-configuration-sources"></a>

# Automatic Reloading of Configuration Sources

If an application has special requirements regarding its availability, it is probably desired that changes on configuration files can be done
without the need for a restart. The application should automatically
detect such changes an react accordingly. This feature is referred to as
automatic reloading.

Providing support for automatic reloading is difficult because applications
may have very specific needs how and when to perform a reload. Also, reloading should not only be limited to file-based configurations, but
work for other configuration sources as well; for instance for
configuration settings kept in a database. Therefore, *Commons
Configuration* provides some generic classes and interfaces that deal
with reloading. In the following section the basic concepts are discussed.
After that some more concrete scenarios are presented.

<a id="userguide-howto_reloading--components-for-reloading"></a>

## Components for Reloading

The reloading mechanism defined by *Commons Configuration*
involves multiple components which all work together to detect changes
on a configuration source and trigger the actual reload operation.

A basic component is a *reloading detector*, defined by the
`ReloadingDetector` interface. This object is responsible for
detecting a change on an external configuration source. An example
implementation could check whether the last-modified data of a specific
file has changed. Note that a reloading detector does not have to monitor
a configuration source actively for changes; it only has to be able to
detect a change when it is triggered. This is reflected in the methods
defined by the `ReloadingDetector` interface:

- The `isReloadingRequired()` method is called to trigger
  a check. The detector has to determine whether something has changed on
  the monitored source and returns a boolean flag as result.
- The `reloadingPerformed()` method is called after a
  reload operation was performed. This method gives the detector the
  opportunity to reset itself so that new changes on the associated
  configuration source can be detected.

The next component taking part in reloading is an instance of the
`ReloadingController` class. This is a fully functional class
implementing a generic protocol for executing a reload check (based on an
external trigger) and reacting accordingly. The actual check whether a
reload is required is delegated to a `ReloadingDetector`
associated with the controller. When the detector reports a change a
corresponding notification is sent out to registered *reloading
listeners*. Like `ReloadingDetector`, a reloading
controller does not actively monitor a certain resource; it has a
`checkForReloading()` method which has to be invoked in order
to trigger a reloading check. If this method returns **true**, the
controller changes into the so-called *reloading state*. This
means that the need for a reload was detected and now the reload has
actually to happen. Typically, this is done by one of the
`ReloadingListener` objects registered at the controller. As long
as the controller is in reloading state, no further changes on the
configuration source monitored by the associated `ReloadingDetector`
are detected. A manual invocation of the `resetReloadingState()`
method is necessary to terminate this state and enable the detection of
further changes.

The components discussed so far only perform reload checks on demand. In
order to implement automatic reloading, it has to be ensured that the
`checkForReloading()` method of a `ReloadingController`
is called periodically or at least when something happens which might
affect the monitored configuration source. This part of the reloading
mechanism is hard to provide in a generic form; in this area requirements
and use cases tend to be very specific. Therefore, *Commons
Configuration* just ships with a pretty simple, timer-based
solution; this may be sufficient in simple cases, for more complex
requirements it may be necessary to create a custom component triggering
a reload check.

After this theory, let's come to some examples how reloading of
configuration sources may be done in practice.

<a id="userguide-howto_reloading--reloading-file-based-configurations"></a>

## Reloading File-based Configurations

As was already stated, reloading is not limited to file-based
configurations. However, configuration files on the user's hard disk
which get changed by external sources are a typical use case for an
automatic reloading feature. Therefore, *Commons Configuration*
has some special support in this area. This is mainly provided by the
`ReloadingFileBasedConfigurationBuilder` class, an extension of
the standard builder for file-based configurations.

`ReloadingFileBasedConfigurationBuilder` already creates a
`ReloadingController` and initializes it with a
`ReloadingDetector` that is associated with the file managed
by the builder. (Actually, the situation is a bit more complex: the
creation of the reloading detector is delegated to an object implementing
the `ReloadingDetectorFactory` interface. The factory to be used can
be configured via the builder's initialization parameters. Per default, a
`DefaultReloadingDetectorFactory` object is used which creates
an instance of the
`FileHandlerReloadingDetector` class. Such an object can detect
changes on a file referenced by a `FileHandler`.) The builder
is already registered as change listener at the reloading controller;
when the controller sends a notification that a change was detected the
builder resets itself. The next time the managed configuration is queried
from the builder, a fresh - updated - instance is returned. So the basic
components of a reloading setup are already in place. What is missing is
a periodic trigger initiating a reload check.

For this example we use the
`PeriodicReloadingTrigger` class which is based on a scheduled
executor service. When constructing an instance of this class the
`ReloadingController` and the period in which to trigger a
check have to be specified. Optionally, the
`ScheduledExecutorService` can be provided; if this argument
is undefined, a default executor is created. It is also possible to pass
an arbitrary parameter object which will then be contained in change
events generated by the `ReloadingController`. This is useful
if a component monitors multiple configuration sources which may be
reloaded. For this simple example this parameter is not used and therefore
set to **null**.

Note that the `PeriodicReloadingTrigger` class - although fully
functional - may not be the right choice depending on the environment in
which an application is running. For instance, applications running in a
JEE container are typically not allowed to create threads; here a
different triggering mechanism has to be found.

Let's finally get to the code. We slightly adapt the example from the
section about [builders for file-based configurations](#userguide-howto_filebased--filebasedconfigurationbuilder). Goal is to load a properties
configuration from a file and enable a periodic reload check which
happens every minute:

```

Parameters params = new Parameters();
// Read data from this file
File propertiesFile = new File("config.properties");

ReloadingFileBasedConfigurationBuilder<FileBasedConfiguration> builder =
    new ReloadingFileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class)
    .configure(params.fileBased()
        .setFile(propertiesFile));
PeriodicReloadingTrigger trigger = new PeriodicReloadingTrigger(builder.getReloadingController(),
    null, 1, TimeUnit.MINUTES);
trigger.start();
```

In this setup, the scheduler service used by the periodic trigger executes
a task every minute which asks the reloading builder's
`ReloadingController` to perform a reload check. If the
underlying file has not been changed, this check has no effect. However, if the file has been changed by an external source, an updated
last-modified date is detected, and the reloading detector signals a
need for a reload. This causes the reloading controller to fire a reloading
event to all registered listeners. The builder is itself registered as
reloading listener at its controller. In reaction to this event it resets
itself, so that the managed configuration becomes invalid. In addition, a builder reset event is generated (see chapter
[Configuration Events](https://commons.apache.org/proper/commons-configuration/userguide/howto_events.html)) which can notify
interested parties that an updated configuration is now available. The
next call to the builder's `getConfiguration()` method causes
a new configuration instance to be created and initialized from the
content of the modified configuration file. At this time the reload
actually happens, and the controller's reloading state is reset.

The `PeriodicReloadingTrigger` class has the methods
`stop()` and `start()` for pausing or resuming the
trigger. This may be useful if an application enters a state in which no
reload checks should be done - for instance during an update. When a
periodic trigger is no longer needed, its `shutdown()` method
should be called which frees all resources and also terminates the
scheduled executor service gracefully.

One important point to keep in mind when using this approach to reloading
is that reloads are only functional if the builder is used as central
component for accessing configuration data. The configuration instance
obtained from the builder will not change automagically! So if an
application fetches a configuration object from the builder at startup
and then uses it throughout its life time, changes on the external
configuration file become never visible. The correct approach is to
keep a reference to the builder centrally and obtain the configuration
from there every time configuration data is needed.

Users familiar with older versions of *Commons Configuration* will
notice that this is a fundamental change compared to the old reloading
implementation. In the old implementation a reload could happen at any
time on a configuration the application was operating on. This had the
advantage that it was fully transparent to the application. But on the
other hand, the application had no control over the reloading mechanism.
With the new approach, an application can obtain a configuration object
from a builder and then perform a unit of work with this instance. As long
as the builder is not accessed any more during this unit of work, it is
guaranteed that the data in the configuration is not changing in an
uncontrolled way due to a reload operation. This gives the access to
configuration data a kind of "transactional" behavior.

<a id="userguide-howto_reloading--builder-configuration-related-to-reloading"></a>

## Builder Configuration Related to Reloading

When setting up a configuration builder with reloading support for
file-based configurations some settings can be defined that influence
reloading operations. These settings are part of the initialization
parameters for file-based configurations and defined by the
`FileBasedBuilderProperties` interface:

- The `ReloadingDetectorFactory` to be used when the reloading
  controller is created. An application with special requirements related
  to the detection of changes can here provide a custom factory. As was
  mentioned above, the default factory creates a suitable detector for
  detecting changes on a file.
- The so-called *reloading refresh delay*. This is a numeric
  value in milliseconds limiting the access to the underlying file. The
  reloading detector will check for updates on the file only if the last
  check was not within the time span defined by the refresh delay. This
  value can be used to improve performance if there are many accesses to
  a configuration builder in short intervals.

<a id="userguide-howto_reloading--generic-reloading-support"></a>

## Generic Reloading Support

In fact, `ReloadingFileBasedConfigurationBuilder` is a pretty thin
implementation around a generic reloading mechanism already supported by
the `BasicConfigurationBuilder` base class. What it does is mainly
specific to file-based configurations: It ensures that a suitable
`ReloadingDetector` is used which is connected to the file
managed by the builder, and that this detector is used by a
`ReloadingController` object also created by the builder.

It is pretty easy to make use of the same generic reloading support to
enable reloading functionality for other types of configuration builders
as well. The key to this lies in the method
`connectToReloadingController()` provided by
`BasicConfigurationBuilder`. This method expects a
`ReloadingController` object as argument. It performs some
event listener registrations to ensure that reloading events fired by
the controller cause the builder's result object to be invalidated, and
that the creation of a new result object causes the controller's
reloading state to be reset. In a nutshell, this is a full implementation
of the reloading protocol.

So the recipe to activate reloading for a builder instance is as follows:

- Create and initialize the builder instance as usual.
- Create a `ReloadingDetector` which is able to monitor
  the configuration source in question and to find out whether a reload
  action has to be performed. For this probably a custom implementation is
  required (as *Commons Configuration* currently supports only
  reloading detector implementations dealing with file handlers).
- Create a `ReloadingController` object and initialize it
  with the `ReloadingDetector` created in the previous step.
- Pass this reloading controllers to the builder's
  `connectToReloadingController()` method.
- Now reloading facilities are set up for this builder. In order to
  actually trigger reload checks ensure that the reloading controller's
  `checkForReloading()` method is called at appropriate points
  of time (e.g. initiate a corresponding trigger as described earlier in
  this chapter.

<a id="userguide-howto_reloading--reloading-checks-on-builder-access"></a>

## Reloading Checks on Builder Access

For some applications it may not be necessary to react on external
changes on their configuration immediately. It just has to be ensured
that when an access to configuration data is performed, the most recent
settings are read. This is in principle similar to the mechanism
implemented in *Commons Configuration 1.x*; here checks for reloads
were triggered by each access to a configuration property - and only by
that.

It is possible to set up a configuration builder in a way that each time
the `getConfiguration()` method is called a reloading check
is performed. If the reloading controller detects that the monitored
source has changed, the managed configuration is replaced by an updated
one. So the builder returns the fresh configuration instance. If used
this way, no special reloading trigger has to be installed; reloading
can only happen when the builder is queried for its managed configuration.
But then it is guaranteed that an up-to-date configuration instance is
returned. Note the main difference to the old model as used in
*Commons Configuration 1.x*: Only invocations of a builder's
`getConfiguration()` method trigger a reloading check, not
access to the managed configuration's properties.

In order to configure a configuration builder to trigger reloading checks
each time its managed configuration is accessed, a special event generated
by the builder can be used: the *configuration request* event.
This event is passed to registered event listeners before the managed
configuration is accessed. (More information about event listeners can
be found in the chapter about [events](https://commons.apache.org/proper/commons-configuration/userguide/howto_events.html).)
A listener for this event just has to trigger a reloading controller.
This will cause the managed configuration to be invalidated and replaced
before it is returned to the caller. The following example shows how this
can be achieved. It makes use of a `ReloadingFileBasedConfigurationBuilder`
because this class provides easy access to its associated reloading
controller. However, the same principle also works for other builders
connected to a reloading controller (as described in the previous section):

```
// Create and initialize the builder final ReloadingFileBasedConfigurationBuilder<FileBasedConfiguration> builder =new ReloadingFileBasedConfigurationBuilder<FileBasedConfiguration>(PropertiesConfiguration.class) .configure(...);
// Register an event listener for triggering reloading checks builder.addEventListener(ConfigurationBuilderEvent.CONFIGURATION_REQUEST,new EventListener() {@Override public void onEvent(Event event) {builder.getReloadingController().checkForReloading(null);} });
```

<a id="userguide-howto_reloading--managed-reloading"></a>

## Managed Reloading

`ManagedReloadingDetector` is an alternative to automatic
reloading. It allows to hot-reload properties on a running application, but only when requested by an administrator. The detector class defines a
`refresh()` method which forces a reload of the configuration
source the next time a reloading check on the associated
`ReloadingController` is triggered.

A typical use of this feature is to setup `ManagedReloadingDetector`
as a JMX MBean. The following code sample uses Spring framework's
`MBeanExporter` to expose the managed reloading detector to the
JMX console:

```


<!-- The managed reloading detector for the configuration builder -->
<bean id="reloadingDetector" class="...ManagedReloadingDetector"/>

<!-- The MBeanExporter that exposes reloadingDetector to the JMX console -->
<bean id="mbeanMetadataExporter" class="org.springframework.jmx.export.MBeanExporter">
    <property name="server" ref="mbeanServer"/>
    <property name="beans">
        <map>
            <entry key="myApp:bean=configuration" value-ref="reloadingStrategy"/>
        </map>
    </property>
</bean>
```

With this configuration, the JMX console will expose the
"myApp:bean=configuration" MBean and it's refresh operation.

---

<a id="userguide-overview"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/userguide/overview.html -->

<!-- page_index: 23 -->

<a id="userguide-overview--using-configuration"></a>

# Using Configuration

Commons Configuration allows you to access configuration properties from
a variety of different sources. No matter if they are stored in a properties file, a XML document, or a JNDI tree, they can all be accessed in the same way
through the generic `Configuration`
interface.

Another strength of Commons Configuration is its ability to mix configurations
from heterogeneous sources and treat them like a single logic configuration.
This section will introduce you to the different configurations
available and will show you how to combine them.

<a id="userguide-overview--configuration-sources"></a>

## Configuration Sources

Currently there are quite a number of different sources of Configuration objects. But, by just using a Configuration object versus a specific type like XMLConfiguration or
JNDIConfiguration, you are sheltered from the mechanics of actually retrieving the
configuration values. These various sources include:

- **EnvironmentConfiguration**
  Reads the plattform specific environment variables.
- **PropertiesConfiguration**
  Loads configuration values from a properties file.
- **XMLConfiguration**
  Takes values from an XML document.
- **INIConfiguration**
  Loads the values from a .ini file as used by Windows.
- **PropertyListConfiguration**
  Loads values from an OpenStep .plist file. XMLPropertyListConfiguration is also
  available to read the XML variant used by Mac OS X.
- **JNDIConfiguration**
  Using a key in the JNDI tree, can retrieve values as configuration properties.
- **BaseConfiguration**
  An in-memory method of populating a Configuration object.
- **HierarchicalConfiguration**
  An in-memory Configuration object that is able to deal with complex
  structured data.
- **SystemConfiguration**
  A configuration using the system properties
- **ConfigurationConverter**
  Takes a java.util.Properties or an org.apache.commons.collections.ExtendedProperties
  and converts it to a Configuration object.

<a id="userguide-overview--the-configuration-interface"></a>

## The Configuration interface

All the classes in this package that represent different kinds of configuration
sources share a single interface:
`Configuration`.
This interface allows you to access and manipulate configuration properties
in a generic way.

The methods defined in the `Configuration` interface can be
divided into methods which query data from the configuration and
methods which alter the configuration object. In fact, the
`Configuration` interface extends a base interface called
`ImmutableConfiguration`. `ImmutableConfiguration`
defines all methods which read data from a configuration object without
changing its state. `Configuration` adds methods for
manipulating the configuration.

A major part of the methods defined in the `ImmutableConfiguration`
interface deals with retrieving properties of different data types. All
these methods take a key as an argument that points to the desired
property. This is a string value whose exact meaning depends on the
concrete `Configuration` implementation used. They try to
find the property specified by the passed in key and convert it to their
target type; this converted value will be returned. There are also
overloaded variants of all methods that allow to specify a default value, which will be returned if the property cannot be found. The following
data types are supported out of the box:

- BigDecimal
- BigInteger
- boolean
- byte
- double
- float
- int
- long
- short
- String

The names of these methods start with `get` followed by their
data type. The `getString()` method for instance will return
String values, `getInt()` will operate on integers.

Properties can have multiple values, so it is also possible to query a
list or an array containing all of the available values. This is done
using the `getList()` or `getArray()` methods.

In addition, there are a couple of generic get methods which try to
convert the requested property value to a specified data type. Such
conversions are also supported for the elements of collections or arrays.
More details about conversions can be found in the section
[Data type conversions](#userguide-howto_basicfeatures--data_type_conversions).

The `subset()` method is useful if configuration settings
are organized in a specific structure and a module of an
application is only interested in a part of this structure.
`subset()` is passed a String with a key prefix and returns
a `Configuration` object that contains only the keys starting
with this prefix.

For manipulating properties or their values the following methods can
be used:

`addProperty()`
:   Adds a new property to the configuration. If this property already
    exists, another value is added to it (so it becomes a multi-valued
    property).

`clearProperty()`
:   Removes the specified property from the configuration.

`setProperty()`
:   Overwrites the value of the specified property. This is the same
    as removing the property and then calling `addProperty()`
    with the new property value.

`clear()`
:   Wipes out the whole configuration

<a id="userguide-overview--immutable-configurations"></a>

## Immutable Configurations

Most of the classes provided by the *Commons Configuration*
library implement the `Configuration` interface, i.e. they
allow client code to change their internal state. For some use cases, this may not be desired. For instance, an application may want to
protect a central configuration object against uncontrolled modifications
done by sub modules.

There is an easy way to convert a normal `Configuration`
object into an `ImmutableConfiguration`: just pass the
configuration in question to the `unmodifiableConfiguration()`
method of the
`ConfigurationUtils` utility class. This results in an
immutable configuration containing the same data as the original
configuration.

<a id="userguide-overview--threading-issues"></a>

## Threading issues

When accessing configurations from multiple threads - be it in a
read-only or in a manipulating manner - the question arises whether
`Configuration` implementations are thread-safe. When
using immutable configurations as described in the previous section
you are typically on the safe side because immutable objects can
safely be shared between multiple threads. However, the
`ImmutableConfiguration` objects created by
`ConfigurationUtils` are just wrappers around a mutable
`Configuration` object. So if code holds a reference to the
underlying `Configuration`, it can still be changed.

Because concurrency is a complex topic this user's guide contains a
dedicated section to this topic: [Configurations and Concurrent Access](#userguide-howto_concurrency).

---
