# Project Information

## Navigation

- Commons Configuration
  - [About](#index)
  - [Release History](#changes)
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
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
  - [Project Reports](#project-reports)
    - [Changes](#changes)
    - [JIRA Report](#jira-changes)
    - [Surefire](#surefire)
    - [RAT Report](#rat-report)
    - [japicmp](#japicmp)
    - [Checkstyle](#checkstyle)
    - [SpotBugs](#spotbugs)

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

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/changes.html -->

<!-- page_index: 2 -->

<a id="changes--apache-commons-configuration-release-notes"></a>

# Apache Commons Configuration Release Notes

<a id="changes--release-history"></a>

## Release History

| Version | Date | Description |
| --- | --- | --- |
| [2.14.0](#changes--a2.14.0) | 2026-04-03 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.13.0](#changes--a2.13.0) | 2025-11-21 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.12.0](#changes--a2.12.0) | 2025-04-22 | This is a feature and maintenance release. Java 8 or later is required. |
| [2.11.0](#changes--a2.11.0) | 2024-06-07 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.10.1](#changes--a2.10.1) | 2024-03-17 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.10.0](#changes--a2.10.0) | 2024-03-06 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.9.0](#changes--a2.9.0) | 2023-03-25 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.8.0](#changes--a2.8.0) | 2022-07-05 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.7](#changes--a2.7) | 2020-03-07 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.6](#changes--a2.6) | 2019-09-13 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.5](#changes--a2.5) | 2019-05-23 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.4](#changes--a2.4) | 2018-10-23 | Minor release with new features and updated dependencies; requires Java 8 or above. |
| [2.3](#changes--a2.3) | 2018-08-04 | Minor release with new features and updated dependencies; requires Java 7 or above. |
| [2.2](#changes--a2.2) | 2017-10-12 | Minor release with new APIs and bug fixes. |
| [2.1.1](#changes--a2.1.1) | 2017-02-05 | Bugfix release for 2.1 |
| [2.1](#changes--a2.1) | 2016-08-20 | First maintenance release for Configuration 2.x. |
| [2.0](#changes--a2.0) | 2016-03-24 | Major redesign of the Configuration 1.x API |
| [2.0-beta2](#changes--a2.0-beta2) | 2015-12-05 | Second beta release, some minor API changes. |
| [2.0-beta1](#changes--a2.0-beta1) | 2015-06-19 | First beta release, getting closer to final. |
| [2.0-alpha2](#changes--a2.0-alpha2) | 2014-12-20 | Some more API fine-tuning. |
| [2.0-alpha1](#changes--a2.0-alpha1) | 2014-09-23 | First alpha release after a major redesign. |
| [1.10](#changes--a1.10) | 2013-10-27 | Minor bug fixes and improvements |
| [1.9](#changes--a1.9) | 2012-08-22 | Minor bug fixes and improvements |
| [1.8](#changes--a1.8) | 2012-02-04 | Support for Java 1.5 |
| [1.7](#changes--a1.7) | 2011-09-07 | Many bugfixes, some new features. |
| [1.6](#changes--a1.6) | 2008-12-25 | Another set of smaller bug fixes |
| [1.5](#changes--a1.5) | 2007-11-24 | Many smaller bugfixes |
| [1.4](#changes--a1.4) | 2007-04-08 | Improved interpolation, configuration for INI files, reloading strategy triggered with JMX, bug fixes. |
| [1.3](#changes--a1.3) | 2006-09-24 |  |
| [1.3-rc2](#changes--a1.3-rc2) | 2006-09-03 |  |
| [1.3-rc1](#changes--a1.3-rc1) | 2006-07-30 |  |
| [1.2](#changes--a1.2) | 2005-12-17 |  |
| [1.2-rc3](#changes--a1.2-rc3) | 2005-12-07 |  |
| [1.2-rc2](#changes--a1.2-rc2) | 2005-11-23 |  |
| [1.2-rc1](#changes--a1.2-rc1) | 2005-11-11 |  |
| [1.1](#changes--a1.1) | 2005-04-02 |  |
| [1.1-rc2](#changes--a1.1-rc2) | 2005-03-06 |  |
| [1.1-rc1](#changes--a1.1-rc1) | 2005-02-13 |  |
| [1.0](#changes--a1.0) | 2004-10-11 | First official release |
| [1.0-rc2](#changes--a1.0-rc2) | 2004-09-24 |  |
| [1.0-rc1](#changes--a1.0-rc1) | 2004-08-14 |  |

<a id="changes--release-2.14.0-2026-04-03"></a>

## Release 2.14.0 – 2026-04-03

| Type | Changes | By |
| --- | --- | --- |
| Fix | Fix Apache RAT plugin console warnings. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | FMigrate from deprecated APIs. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add XMLConfiguration.read(Element). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ConfigurationException.ConfigurationException(String, Object...). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ConfigurationException.ConfigurationException(Throwable, String, Object...). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ConversionException.ConversionException(String, Object...). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ConversionException.ConversionException(Throwable, String, Object...). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ConfigurationRuntimeException.ConfigurationRuntimeException(Throwable, String, Object...). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 92 to 97. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-text from 1.14.0 to 1.15.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | [test] Bump org.apache.commons:commons-pool2 from 2.12.1 to 2.13.1 #474. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | [test] Bump org.apache.commons:commons-dbcp2 from 2.13.0 to 2.14.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.logging.log4j:log4j-core from 2.25.2 to 2.25.4 #626. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.20.0 to 1.21.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.20.1 to 2.21.2 #632. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.3.5 to 1.3.6. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.yaml:snakeyaml from 2.5 to 2.6 #631. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-2.13.0-2025-11-21"></a>

## Release 2.13.0 – 2025-11-21

| Type | Changes | By |
| --- | --- | --- |
| Fix | Shared primitive variable "throwExceptionOnMissing" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.configuration2.AbstractConfiguration] At AbstractConfiguration.java:[line 1493] AT\_STALE\_THREAD\_WRITE\_OF\_PRIMITIVE. Thanks to Gary Gregory, SpotBugs. | [ggregory](#team--ggregory) |
| Fix | Shared primitive variable "forceSingleLine" in one thread may not yield the value of the most recent write from another thread [org.apache.commons.configuration2.PropertiesConfigurationLayout] At PropertiesConfigurationLayout.java:[line 821] AT\_STALE\_THREAD\_WRITE\_OF\_PRIMITIVE. Thanks to Gary Gregory, SpotBugs. | [ggregory](#team--ggregory) |
| Fix | Fix undoubling of strings #569. Fixes [CONFIGURATION-849](https://issues.apache.org/jira/browse/CONFIGURATION-849). Thanks to Willy van Diepen, Gary Gregory, Rob Tompkins. | [ggregory](#team--ggregory) |
| Fix | Mark the package jakarta.servlet.\* import as optional in OSGi #574. Fixes [CONFIGURATION-852](https://issues.apache.org/jira/browse/CONFIGURATION-852). Thanks to Robbie Gemmell, Justin Bertram, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix build [WARNING] Parameter 'forkMode' is unknown for plugin 'maven-surefire-plugin:3.5.3:test (default-test)'. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add org.apache.commons.configuration2.ImmutableConfiguration.entrySet(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add org.apache.commons.configuration2.ImmutableConfiguration.forEach(BiConsumer<String, Object>). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add VEX entry for CVE-2025-48924 #587. Thanks to Piotr P. Karwasz, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 81 to 92 #604, #623. Thanks to Gary Gregory, Dependabbot. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.18.3 to 2.20.1 #565, #599, #618. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-beanutils:commons-beanutils from 1.10.1 to 1.11.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump log4j.version from 2.24.3 to 2.25.2 #579, #608. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-lang3 from 3.17.0 to 3.20.0 #582. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.19.0 to 2.21.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.18.0 to 1.20.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-text from 1.13.1 to 1.14.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.sun.mail:mailapi from 2.0.1 to 2.0.2 (#586) #1627. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.yaml:snakeyaml from 2.4 to 2.5 #601. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-2.12.0-2025-04-22"></a>

## Release 2.12.0 – 2025-04-22

| Type | Changes | By |
| --- | --- | --- |
| Fix | PropertyConverter.to(Class, Object, DefaultConversionHandler) doesn't convert custom java.lang.Number subclasses. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | DefaultConversionHandler.convertValue(Object, Class, ConfigurationInterpolator) doesn't convert custom java.lang.Number subclasses. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | DefaultConversionHandler.to(Object, Class, ConfigurationInterpolator) doesn't convert custom java.lang.Number subclasses. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | SubsetConfiguration does not account for delimiters as it did in 2.9.0. Fixes [CONFIGURATION-848](https://issues.apache.org/jira/browse/CONFIGURATION-848). Thanks to Laszlo Hujber, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | CompositeConfiguration does not account for delimiters as it did in 2.9.0. Fixes [CONFIGURATION-848](https://issues.apache.org/jira/browse/CONFIGURATION-848). Thanks to Laszlo Hujber, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Describe the security model #540. Thanks to Arnout Engelen, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | De-emphasize the 1.x version line on the website #539. Thanks to Arnout Engelen, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | HomeDirectoryLocationStrategy no longer resolves the user HOME directory correctly. Fixes [CONFIGURATION-851](https://issues.apache.org/jira/browse/CONFIGURATION-851). Thanks to Scott Babcock, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add PrefixedKeysIterator.toString() to package-private PrefixedKeysIterator. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | New web configurations using the jakarta.servlet namespace are now available. Fixes [CONFIGURATION-836](https://issues.apache.org/jira/browse/CONFIGURATION-836). Thanks to Emmanuel Bourg. | [ebourg](#team--ebourg) |
| Add | Add org.apache.commons.configuration2.web.JakartaServletConfiguration. Fixes [CONFIGURATION-836](https://issues.apache.org/jira/browse/CONFIGURATION-836). Thanks to Emmanuel Bourg. | [ebourg](#team--ebourg) |
| Add | Add org.apache.commons.configuration2.web.JakartaServletContextConfiguration. Fixes [CONFIGURATION-836](https://issues.apache.org/jira/browse/CONFIGURATION-836). Thanks to Emmanuel Bourg. | [ebourg](#team--ebourg) |
| Add | Add org.apache.commons.configuration2.web.JakartaServletFilterConfiguration. Fixes [CONFIGURATION-836](https://issues.apache.org/jira/browse/CONFIGURATION-836). Thanks to Emmanuel Bourg. | [ebourg](#team--ebourg) |
| Add | Add org.apache.commons.configuration2.web.JakartaServletRequestConfiguration. Fixes [CONFIGURATION-836](https://issues.apache.org/jira/browse/CONFIGURATION-836). Thanks to Emmanuel Bourg. | [ebourg](#team--ebourg) |
| Add | Add org.apache.commons.configuration2.AbstractHierarchicalConfiguration.getKeysInternal(String, String). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 70 to 81 #434, #453, #466, #470, #479, #486, #491, #499, #537. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.3.2 to 1.3.5 #442, #467. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.17.1 to 2.18.3 #447, #483, #518. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.17.0 to 1.18.0 #449, #533. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-lang3 from 3.14.0 to 3.17.0 #450, #458, #471. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump slf4j.version from 2.0.13 to 2.0.17 #457, #462, #464, #549. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spring.version from 5.3.35 to 5.3.39. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.yaml:snakeyaml from 2.2 to 2.4 #473. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump log4j.version from 2.23.1 to 2.24.3 #475, #486, #514, #519. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.16.1 to 2.19.0 #480, #513. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-dbcp2 from 2.12.0 to 2.13.0 #515. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-text from 1.12.0 to 1.13.1 #521. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-beanutils:commons-beanutils from 1.9.4 to 1.10.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-pool2 from 2.12.0 to 2.12.1 #532. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.dbunit:dbunit from 2.8.0 to 3.0.0 #534. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-vfs2 from 2.9.0 to 2.10.0. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-2.11.0-2024-06-07"></a>

## Release 2.11.0 – 2024-06-07

| Type | Changes | By |
| --- | --- | --- |
| Add | Add support for empty sections #408. Fixes [CONFIGURATION-844](https://issues.apache.org/jira/browse/CONFIGURATION-844). Thanks to Thomas Steiner, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ImmutableConfiguration.containsValue(Object). Thanks to Rikkarth, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if DataConfiguration.DataConfiguration(Configuration) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if XMLPropertiesConfiguration.XMLPropertiesConfiguration(Element) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if a SubsetConfiguration constructor is called with a null Configuration. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Methods should not be empty #393. Fixes [CONFIGURATION-843](https://issues.apache.org/jira/browse/CONFIGURATION-843). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Guard MapConfiguration against null maps #381. Thanks to Heewon Lee, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if AppletConfiguration(Applet) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if ServletConfiguration(Servlet) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if ServletConfiguration(ServletConfig) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if ServletContextConfiguration(Servlet) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if ServletContextConfiguration(ServletContext) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if ServletFilterConfiguration(FilterConfig) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fail-fast with a NullPointerException if ServletRequestConfiguration(ServletRequest) is called with null. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Deprecate DatabaseConfiguration.getDatasource() in favor of getDataSource(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix PMD DynamicCombinedConfiguration in AbstractImmutableNodeHandler. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix PMD DynamicCombinedConfiguration in AbstractListDelimiterHandler. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix PMD DynamicCombinedConfiguration in DefaultPrefixLookupsHolder. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix PMD DynamicCombinedConfiguration in DynamicCombinedConfiguration. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix PMD DynamicCombinedConfiguration in PropertiesConfiguration. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Restore previous behavior allowing Spring to inject multiple values #425. Fixes [CONFIGURATION-846](https://issues.apache.org/jira/browse/CONFIGURATION-846). Thanks to Andrea Bollini, Gary Gregory, Tim Donohue, kbarlowgw. | [ggregory](#team--ggregory) |
| Fix | Property with an empty string value was not processed #431. Fixes [CONFIGURATION-847](https://issues.apache.org/jira/browse/CONFIGURATION-847). Thanks to Andrea Bollini, Gary Gregory, Tim Donohue, kbarlowgw. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.3.0 to 1.3.2 #390, #418. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.15.1 to 2.16.1 #394, #400. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 67 to 70 #396. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump slf4j.version from 2.0.12 to 2.0.13 #403. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-text from 1.11.0 to 1.12.0 #404. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spring.version from 5.3.33 to 5.3.35 #424. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.16.1 to 1.17.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.17.0 to 2.17.1 #417. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-2.10.1-2024-03-17"></a>

## Release 2.10.1 – 2024-03-17

| Type | Changes | By |
| --- | --- | --- |
| Fix | java.lang.module.FindException: Module servlet.api not found. Fixes [CONFIGURATION-839](https://issues.apache.org/jira/browse/CONFIGURATION-839). Thanks to Bob Marinier, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | StackOverflowError adding property in AbstractListDelimiterHandler.flattenIterator(). Fixes [CONFIGURATION-840](https://issues.apache.org/jira/browse/CONFIGURATION-840). Thanks to Bob Marinier, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | StackOverflowError calling ListDelimiterHandler.flatten(Object, int) with a cyclical object tree. Fixes [CONFIGURATION-841](https://issues.apache.org/jira/browse/CONFIGURATION-841). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump jackson-databind from 2.16.1 to 2.17.0 #378. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump log4j.version from 2.23.0 to 2.23.1 #379. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spring.version from 5.3.32 to 5.3.33 #380. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-2.10.0-2024-03-06"></a>

## Release 2.10.0 – 2024-03-06

| Type | Changes | By |
| --- | --- | --- |
| Fix | [StepSecurity] ci: Harden GitHub Actions #307. Thanks to step-security-bot, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | ConfirgurationPropertySource doesn't supply resolved values #309. Fixes [CONFIGURATION-834](https://issues.apache.org/jira/browse/CONFIGURATION-834). Thanks to Keith Barlow, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Take prefix delimiter into account when SubsetConfiguration.getKeysInternal() is called #300. Thanks to KeijoB, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Guard ConfigurationMap against null configuration #355. Thanks to Heewon Lee, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Properties parser stack overflows on large single-key inputs #369. Fixes [CONFIGURATION-838](https://issues.apache.org/jira/browse/CONFIGURATION-838). Thanks to Ian Lynagh. | [ggregory](#team--ggregory) |
| Fix | DatabaseConfiguration.AbstractJdbcOperation.execute() throws NullPointerException when no data source is set #368. Thanks to Heewon Lee, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add AbstractConfiguration.getKeysInternal(String, String) #300. Thanks to KeijoB, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ImmutableConfiguration.getKeys(String, String) #300. Thanks to KeijoB, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add PrefixedKeysIterator.PrefixedKeysIterator(Iterator<String%gt;, String, String) #300. Thanks to KeijoB, Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add Maven property project.build.outputTimestamp for build reproducibility. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Guard PatternSubtreeConfigurationWrapper constructor against null #365. Thanks to Heewon Lee. | [ggregory](#team--ggregory) |
| Update | Bump jackson-databind from 2.14.2 to 2.16.1 #297, #303, #326, #331, #340. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-io:commons-io from 2.11.0 to 2.15.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spring-\* from 5.3.26 to 5.3.32. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 57 to 67. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.15 to 1.16.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-lang3 from 3.11 to 3.14.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.yaml:snakeyaml from 2.0 to 2.2 #312, #315. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump slf4j.version from 2.0.7 to 2.0.12 #358. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-dbcp2 from 2.9.0 to 2.12.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-pool2 from 2.11.1 to 2.12.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.logging.log4j:log4j-1.2-\* from 2.20.0 to 2.23.0 #334, #339, #367. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-text from 1.10.0 to 1.11.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-logging:commons-logging from 1.2 to 1.3.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-2.9.0-2023-03-25"></a>

## Release 2.9.0 – 2023-03-25

| Type | Changes | By |
| --- | --- | --- |
| Fix | CombinedConfiguration#getKeys() can throw NoSuchElementException. Fixes [CONFIGURATION-799](https://issues.apache.org/jira/browse/CONFIGURATION-799). Thanks to Jarek Sacha, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix ambiguity on the section determining #229. Fixes [CONFIGURATION-822](https://issues.apache.org/jira/browse/CONFIGURATION-822). Thanks to Branislav Beňo, Gary Gregory, Bruno P. Kinoshita. | [ggregory](#team--ggregory) |
| Fix | Use Java style array decelerations #244. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Add | Add DefaultConversionHandler#setListDelimiterHandler(ListDelimiterHandler). Fixes [CONFIGURATION-799](https://issues.apache.org/jira/browse/CONFIGURATION-799). Thanks to Xinshiyou, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Add ImmutableNode.stream(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Avoid NullPointerException in org.apache.commons.configuration2.web.AppletConfiguration.getKeysInternal(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix JDBC prepared statements leak in org.apache.commons.configuration2.DatabaseConfiguration.clearPropertyDirect(String). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from 3.0.8 to 3.0.10 #223, #225. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump actions/checkout from 3 to 3.1.0 #224. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from 3 to 3.5.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump optional Apache Log4j 1.2.17 with 2.20.0. Fixes [CONFIGURATION-815](https://issues.apache.org/jira/browse/CONFIGURATION-815). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.7.0.0 to 4.7.3.0 #193, #195, #228, #237. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs from 4.7.0 to 4.7.3. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.springframework:spring-\* from 5.3.21 to 5.3.26. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump junit-jupiter from 5.8.2 to 5.9.1 #197, #217. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump mockito-core from 4.6.1 to 4.11.0 #200, #235, #249, #257, #259. Thanks to Dependabot, Gary Gregory. | [kinow](#team--kinow) |
| Update | Bump slf4j.version from 1.7.36 to 2.0.7 #202, #210, #215, #238, #241, #291. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump maven-checkstyle-plugin from 3.1.2 to 3.2.0 #201. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump maven-javadoc-plugin from 3.4.0 to 3.4.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-pmd-plugin 3.17.0 to 3.19.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump pmd from 6.47.0 to 6.53.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump snakeyaml from 1.30 to 2.0 #203, #212, #219, #282, #283. Thanks to Dependabot, strangelookingnerd. | [kinow](#team--kinow) |
| Update | Bump jackson-databind from 2.13.3 to 2.14.2 #227, #246, #274. Thanks to Gary Gregory. | [kinow](#team--kinow) |
| Update | Bump spring.version from 5.3.22 to 5.3.23 #211. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump commons-parent from 53 to 57 #216, #253, #299. Thanks to Dependabot, Gary Gregory. | [kinow](#team--kinow) |
| Update | Bump log4j.version from 2.18.0 to 2.20.0 #213, #281. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Bump japicmp-maven-plugin from 0.15.7 to 0.17.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-text from 1.9 to 1.10.0 #221. Thanks to Dependabot. | [kinow](#team--kinow) |

<a id="changes--release-2.8.0-2022-07-05"></a>

## Release 2.8.0 – 2022-07-05

| Type | Changes | By |
| --- | --- | --- |
| Fix | Make interpolation of collections and arrays in ConfigurationInterpolator consistent with behavior of DefaultConversionHandler. Add ConfigurationInterpolator.setStringConverter to allow customized string conversion behavior. Fixes [CONFIGURATION-753](https://issues.apache.org/jira/browse/CONFIGURATION-753). | [mattjuntunen](#team--mattjuntunen) |
| Fix | Computation of blank lines after header comment #82. Fixes [CONFIGURATION-795](https://issues.apache.org/jira/browse/CONFIGURATION-795). Thanks to dpeger. | [ggregory](#team--ggregory) |
| Fix | Remove redundant initializer #110. Fixes [CONFIGURATION-801](https://issues.apache.org/jira/browse/CONFIGURATION-801). Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Use final #111. Fixes [CONFIGURATION-802](https://issues.apache.org/jira/browse/CONFIGURATION-802). Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Java 8 lambda improvements and more #112. Fixes [CONFIGURATION-803](https://issues.apache.org/jira/browse/CONFIGURATION-803). Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Redundant local variable #113. Fixes [CONFIGURATION-804](https://issues.apache.org/jira/browse/CONFIGURATION-804). Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Use try with resource #114. Fixes [CONFIGURATION-805](https://issues.apache.org/jira/browse/CONFIGURATION-805). Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | [Javadoc] Specify that typed getList returns null for missing key #100. Fixes [CONFIGURATION-805](https://issues.apache.org/jira/browse/CONFIGURATION-805). Thanks to Roman Zaynetdinov. | [ggregory](#team--ggregory) |
| Fix | Mention EnvironmentConfiguration in the list of configuration sources #45. Thanks to Oliver B. Fischer. | [ggregory](#team--ggregory) |
| Fix | DefaultListDelimiterHandler.escapeList working only for List>String< #137. Fixes [CONFIGURATION-808](https://issues.apache.org/jira/browse/CONFIGURATION-808). Thanks to cigaly. | [ggregory](#team--ggregory) |
| Fix | Use final #141. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Replace test asserts by simpler but equivalent calls. #139 Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Single Variable Interpolation #182. Fixes [CONFIGURATION-764](https://issues.apache.org/jira/browse/CONFIGURATION-764). Thanks to Ning Zhang, Matt Juntunen, Bruno P. Kinoshita, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Implement proper concurrency in ConstantLookup. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Support new namespace jakarta.mail.\* used by javamail 2.0+ (first release October 2020) #186. Fixes [CONFIGURATION-813](https://issues.apache.org/jira/browse/CONFIGURATION-813). Thanks to Dependabot. | [kinow](#team--kinow) |
| Add | Implement Iterable in ImmutableNode #74. Thanks to SethiPandi. | [ggregory](#team--ggregory) |
| Update | Unclosed file handle when reading config from JAR file URL. Add and use FileBasedBuilderProperties.setURL(URL, URLConnectionOptions). Fixes [CONFIGURATION-794](https://issues.apache.org/jira/browse/CONFIGURATION-794). Thanks to Robin Jansohn, Gary Gregory, Rob Spoor. | [ggregory](#team--ggregory) |
| Add | Add PropertiesConfigurationLayout.getBlankLinesBefore() and deprecate getBlancLinesBefore(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add PropertiesConfigurationLayout.setBlankLinesBefore() and deprecate setBlancLinesBefore(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add PropertiesConfigurationLayout.PropertyLayoutData.getBlankLines() and deprecate getBlancLines(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add PropertiesConfigurationLayout.PropertyLayoutData.setBlankLines() and deprecate setBlancLines(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ImmutableConfiguration.getEnum() methods. Fixes [CONFIGURATION-789](https://issues.apache.org/jira/browse/CONFIGURATION-789). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Add ImmutableConfiguration.getDuration() methods. Fixes [CONFIGURATION-789](https://issues.apache.org/jira/browse/CONFIGURATION-789). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Make default interpolation prefix lookups configurable via system property. Remove dns, url, and script lookups from defaults. If these lookups are required for use in AbstractConfiguration subclasses, they must be enabled via system property. See ConfigurationInterpolator.getDefaultPrefixLookups() for details. | [mattjuntunen](#team--mattjuntunen) |
| Update | Bump actions/cache from 2 to 3.0.4 #99, #151, #169. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/checkout from 1 to 3 #47, #62, #70, #85, #150, #163. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from 1.4.0 to 3 #63, #65, #73, #174. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump codeql-action from v1 to v2. Thanks to Dependabot, Matt Juntunen. | [mattjuntunen](#team--mattjuntunen) |
| Update | Bump Spring dependency versions: org.springframework:spring-beans 4.3.26.RELEASE -> 5.3.21 org.springframework:spring-context 4.3.26.RELEASE -> 5.3.21 org.springframework:spring-core 4.3.26.RELEASE -> 5.3.21 org.springframework:spring-test 4.3.26.RELEASE -> 5.3.21 #165, #172 Thanks to Dependabot, Matt Juntunen, kinow, Gary Gregory. | [mattjuntunen](#team--mattjuntunen) |
| Update | Bump commons-parent from 52 to 53. Thanks to Dependabot, Matt Juntunen. | [mattjuntunen](#team--mattjuntunen) |
| Update | Bump Apache Commons Lang from 3.9 to 3.12.0. Fixes [CONFIGURATION-787](https://issues.apache.org/jira/browse/CONFIGURATION-787). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.10.3 to 2.13.3, #60. Fixes [CONFIGURATION-790](https://issues.apache.org/jira/browse/CONFIGURATION-790). Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump Slf4j test dependencies: org.slf4j:slf4j-api 1.7.26 -> 1.7.33, org.slf4j:slf4j-ext 1.7.26 -> 1.7.33, org.slf4j:slf4j-log4j12 1.7.26 -> 1.7.33, org.slf4j:slf4j-nop 1.7.26 -> 1.7.33. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 50 to 52. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump mailapi from 1.6.4 to 1.6.7 #48. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 3.1.12.2 to 4.7.0.0, #55, #75, #79, #93, #116, #183. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump hsqldb from 2.5.0 to 2.5.2 #54, #128. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-text from 1.8 to 1.9. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump servlet-api from 2.4 to 2.5 #58. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.1.0 to 3.1.2, #57, #97. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-pool2 from 2.8.0 to 2.10.0, #61, #124. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump optional commons-codec from 1.14 to 1.15. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump checkstyle from 8.26 to 9.3, #66, #71, #90, #101, #118, #121, #132, #155. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons.jacoco.version 0.8.5 to 0.8.8 (Fixes Java 15 builds). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from commons-pool2 2.10.0 to 2.11.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from commons-dbcp2 2.7.0 to 2.9.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump snakeyaml from 1.26 to 1.30 #68, #126, #137. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons.japicmp.version from 0.14.1 to 0.15.7. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump junit from 4.13 to 4.13.2 #78. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons VFS 2.6.0 -> 2.9.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump jackson-databind from 2.11.3 to 2.13.2.2 ,#88, #94, #127, #159, #168, #173. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons.animal-sniffer.version 1.19 -> 1.20. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons.javadoc.version from 3.1.1 to 3.4.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.dbunit:dbunit from 2.7.0 to 2.7.3, #167. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump tests to hamcrest v2.2 #143. Thanks to John Patrick. | [ggregory](#team--ggregory) |
| Update | Bump slf4j.version from 1.7.33 to 1.7.36 #166. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump mailapi from 1.6.6 to 2.0.1 #186. Thanks to Dependabot. | [kinow](#team--kinow) |
| Update | Use GitHub Actions setup-java Maven cache property #190. Thanks to sullis. | [kinow](#team--kinow) |

<a id="changes--release-2.7-2020-03-07"></a>

## Release 2.7 – 2020-03-07

| Type | Changes | By |
| --- | --- | --- |
| Fix | Single argument DataConfiguration APIs always create empty arrays. Fixes [CONFIGURATION-761](https://issues.apache.org/jira/browse/CONFIGURATION-761). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Use variable arguments. Fixes [CONFIGURATION-762](https://issues.apache.org/jira/browse/CONFIGURATION-762). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.puppycrawl.tools:checkstyle from 8.24 to 8.25. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.9.9 to 2.10.0. Fixes [CONFIGURATION-763](https://issues.apache.org/jira/browse/CONFIGURATION-763). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Refactor XMLConfiguration.write(Writer) to add XMLConfiguration.write(Writer, Transformer). Fixes [CONFIGURATION-765](https://issues.apache.org/jira/browse/CONFIGURATION-765). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | NullPointerException in XMLConfiguration#createTransformer() when no FileLocator is set. Fixes [CONFIGURATION-767](https://issues.apache.org/jira/browse/CONFIGURATION-767). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | XMLConfiguration#write does not indent XML elements. Fixes [CONFIGURATION-768](https://issues.apache.org/jira/browse/CONFIGURATION-768). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Bump com.fasterxml.jackson.core:jackson-databind 2.10.0 -> 2.10.1. Fixes [CONFIGURATION-771](https://issues.apache.org/jira/browse/CONFIGURATION-771). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | [test] org.easymock:easymock 4.0.2 -> 4.1. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | User's Guide > Properties files > Saving - small documentation bugs #41. Fixes [CONFIGURATION-773](https://issues.apache.org/jira/browse/CONFIGURATION-773). Thanks to Dan Dragut. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons VFS from 2.4.1 to 2.5.0. Fixes [CONFIGURATION-775](https://issues.apache.org/jira/browse/CONFIGURATION-775). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons VFS from 2.5.0 to 2.6.0. Fixes [CONFIGURATION-777](https://issues.apache.org/jira/browse/CONFIGURATION-777). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump optional Apache Commons Codec from 1.13 to 1.14. Fixes [CONFIGURATION-778](https://issues.apache.org/jira/browse/CONFIGURATION-778). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from JUnit 4.12 to 4.13. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump optional jackson-databind from 2.10.1 to 2.10.2. Fixes [CONFIGURATION-779](https://issues.apache.org/jira/browse/CONFIGURATION-779). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump com.fasterxml.jackson.core:jackson-databind from 2.10.2 to 2.10.3. Fixes [CONFIGURATION-783](https://issues.apache.org/jira/browse/CONFIGURATION-783). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Update org.yaml:snakeyaml from 1.25 to 1.26 and tweak parser configuration. Fixes [CONFIGURATION-784](https://issues.apache.org/jira/browse/CONFIGURATION-784). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.springframework:spring-\* from 4.3.25.RELEASE to 4.3.26.RELEASE. Fixes [CONFIGURATION-785](https://issues.apache.org/jira/browse/CONFIGURATION-785). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 48 to 50 Thanks to Rob Tompkins. | [chtompki](#team--chtompki) |

<a id="changes--release-2.6-2019-09-13"></a>

## Release 2.6 – 2019-09-13

| Type | Changes | By |
| --- | --- | --- |
| Fix | XMLPropertyListConfiguration cannot set arrays in the correct plist form. Fixes [CONFIGURATION-750](https://issues.apache.org/jira/browse/CONFIGURATION-750). Thanks to Jason Pickens, Gary Gregory, Emmanuel Bourg. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Text from 1.6 to 1.7. Fixes [CONFIGURATION-751](https://issues.apache.org/jira/browse/CONFIGURATION-751). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons VFS from 2.3 to 2.4.1. Fixes [CONFIGURATION-752](https://issues.apache.org/jira/browse/CONFIGURATION-752). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Text from 1.7 to 1.8. Fixes [CONFIGURATION-754](https://issues.apache.org/jira/browse/CONFIGURATION-754). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Fix Javadoc for org.apache.commons.configuration2.PropertiesConfiguration.getIncludeOptional(). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Document "includeOptional" on the site. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | [CVE-2014-0114] Bump Apache Commons BeanUtils from 1.9.3 to 1.9.4. Fixes [CONFIGURATION-755](https://issues.apache.org/jira/browse/CONFIGURATION-755). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Fix syntax in user guide documentation #33. Thanks to Kevin Wang. | [ggregory](#team--ggregory) |
| Add | Allow for custom behavior to handle errors loading included properties files. Fixes [CONFIGURATION-756](https://issues.apache.org/jira/browse/CONFIGURATION-756). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.yaml:snakeyaml from 1.24 to 1.25. Fixes [CONFIGURATION-757](https://issues.apache.org/jira/browse/CONFIGURATION-757). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from org.apache.commons:commons-dbcp2 2.6.0 to 2.7.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from org.apache.commons:commons-pool2 2.6.2 to 2.7.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-codec:commons-codec from 1.12 to 1.13. Fixes [CONFIGURATION-758](https://issues.apache.org/jira/browse/CONFIGURATION-758). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from org.hsqldb:hsqldb 2.4.1 to 2.5.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump tests from com.sun.mail:mailapi 1.6.3 to 1.6.4. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Spring from 4.3.24.RELEASE to 4.3.25.RELEASE. Fixes [CONFIGURATION-759](https://issues.apache.org/jira/browse/CONFIGURATION-759). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Properties file using cyclical includes cause a StackOverflowError instead of detecting the misconfiguration. Fixes [CONFIGURATION-760](https://issues.apache.org/jira/browse/CONFIGURATION-760). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump maven-checkstyle-plugin from 3.0.0 to 3.1.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Use current version of Checkstyle: 6.18 to 8.24. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-2.5-2019-05-23"></a>

## Release 2.5 – 2019-05-23

| Type | Changes | By |
| --- | --- | --- |
| Fix | Allow user to specify the comments and separator chars. Fixes [CONFIGURATION-731](https://issues.apache.org/jira/browse/CONFIGURATION-731). Thanks to Shuai Zhang, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Jackson from 2.9.7 to 2.9.8. Fixes [CONFIGURATION-738](https://issues.apache.org/jira/browse/CONFIGURATION-738). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Codec from 1.11 to 1.12. Fixes [CONFIGURATION-739](https://issues.apache.org/jira/browse/CONFIGURATION-739). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons VFS from 2.2 to 2.3. Fixes [CONFIGURATION-740](https://issues.apache.org/jira/browse/CONFIGURATION-740). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Spring from 4.3.19 to 4.3.22. Fixes [CONFIGURATION-741](https://issues.apache.org/jira/browse/CONFIGURATION-741). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump optional library snakeyaml from 1.23 to 1.24. Fixes [CONFIGURATION-743](https://issues.apache.org/jira/browse/CONFIGURATION-743). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Lang from 3.8.1 to 3.9. Fixes [CONFIGURATION-747](https://issues.apache.org/jira/browse/CONFIGURATION-747). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Jackson from 2.9.8 to 2.9.9. Fixes [CONFIGURATION-746](https://issues.apache.org/jira/browse/CONFIGURATION-746). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump Spring from 4.3.22 to 4.3.24. Fixes [CONFIGURATION-747](https://issues.apache.org/jira/browse/CONFIGURATION-747). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Add the special key "includeoptional" for properties files. Fixes [CONFIGURATION-745](https://issues.apache.org/jira/browse/CONFIGURATION-745). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-2.4-2018-10-23"></a>

## Release 2.4 – 2018-10-23

| Type | Changes | By |
| --- | --- | --- |
| Fix | Fixed numerous typos in user guides. Fixes [CONFIGURATION-710](https://issues.apache.org/jira/browse/CONFIGURATION-710). Thanks to thc202. | [oheger](#team--oheger) |
| Fix | Bump Apache Commons Lang from 3.7 to 3.8.1. Fixes [CONFIGURATION-711](https://issues.apache.org/jira/browse/CONFIGURATION-711). | [ggregory](#team--ggregory) |
| Add | FileHandlerReloadingDetector now has a new refresh() method to initialize the reloading state from the underlying file. This new method is called by DefaultReloadingDetectorFactory when a new detector instance is created. This makes sure that a changed configuration file is directly detected on the first invocation of the isReloadingRequired() method. Fixes [CONFIGURATION-712](https://issues.apache.org/jira/browse/CONFIGURATION-712). Thanks to Rolland Hobbie. | [oheger](#team--oheger) |
| Add | Configuration properties can now be converted to regular expressions. Fixes [CONFIGURATION-713](https://issues.apache.org/jira/browse/CONFIGURATION-713). Thanks to Lars W. | [oheger](#team--oheger) |
| Add | With JupIOFactory a new IOFactory implementation is now available that implements handling of whitespace in a way closer to java.util.Properties. This class can be used when stricter compatibility with Java standard methods for reading and writing properties files is needed. Fixes [CONFIGURATION-715](https://issues.apache.org/jira/browse/CONFIGURATION-715). Thanks to Patrick Schmidt. | [oheger](#team--oheger) |
| Add | JupIOFactory (introduced for CONFIGURATION-715) also implements handling of escape sequences in a way closer to java.util.Properties. Fixes [CONFIGURATION-716](https://issues.apache.org/jira/browse/CONFIGURATION-716). Thanks to Patrick Schmidt. | [oheger](#team--oheger) |
| Update | Replace use of deprecated Commons Lang string substitution code for Commons Text. Fixes [CONFIGURATION-720](https://issues.apache.org/jira/browse/CONFIGURATION-720). | [ggregory](#team--ggregory) |
| Update | Bump Java requirement from version 7 to 8. Fixes [CONFIGURATION-694](https://issues.apache.org/jira/browse/CONFIGURATION-694). | [ggregory](#team--ggregory) |
| Update | Bump Jackson from 2.9.6 to 2.9.7. Fixes [CONFIGURATION-721](https://issues.apache.org/jira/browse/CONFIGURATION-721). | [ggregory](#team--ggregory) |
| Update | Bump optional dependency snakeyaml from 1.21 to 1.23. Fixes [CONFIGURATION-722](https://issues.apache.org/jira/browse/CONFIGURATION-722). | [ggregory](#team--ggregory) |
| Update | Bump optional Spring dependencies from 4.3.18.RELEASE to 4.3.19.RELEASE. Fixes [CONFIGURATION-723](https://issues.apache.org/jira/browse/CONFIGURATION-723). | [ggregory](#team--ggregory) |
| Add | Add support for Commons Text 1.4 localhost string lookup as a default lookup. Fixes [CONFIGURATION-724](https://issues.apache.org/jira/browse/CONFIGURATION-724). | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Text from 1.4 to 1.5. Fixes [CONFIGURATION-725](https://issues.apache.org/jira/browse/CONFIGURATION-725). | [ggregory](#team--ggregory) |
| Add | Add support for Commons Text 1.5 new string lookups as default lookups. Fixes [CONFIGURATION-726](https://issues.apache.org/jira/browse/CONFIGURATION-726). | [ggregory](#team--ggregory) |
| Fix | org.apache.commons.configuration2.DatabaseConfiguration never closes result sets and statements. Fixes [CONFIGURATION-727](https://issues.apache.org/jira/browse/CONFIGURATION-727). | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Text from 1.5 to 1.6. Fixes [CONFIGURATION-728](https://issues.apache.org/jira/browse/CONFIGURATION-728). | [ggregory](#team--ggregory) |

<a id="changes--release-2.3-2018-08-04"></a>

## Release 2.3 – 2018-08-04

| Type | Changes | By |
| --- | --- | --- |
| Update | Bump Spring from 4.3.14.RELEASE to 4.3.18.RELEASE. Fixes [CONFIGURATION-707](https://issues.apache.org/jira/browse/CONFIGURATION-707). | [ggregory](#team--ggregory) |
| Update | Bump optional dependency snakeyaml from 1.20 to 1.21. Fixes [CONFIGURATION-706](https://issues.apache.org/jira/browse/CONFIGURATION-706). | [ggregory](#team--ggregory) |
| Update | Bump Jackson from 2.9.5 to 2.9.6. Fixes [CONFIGURATION-705](https://issues.apache.org/jira/browse/CONFIGURATION-705). | [ggregory](#team--ggregory) |
| Fix | Root node attributes are now updated correctly when loading XML configuration files. Fixes [CONFIGURATION-652](https://issues.apache.org/jira/browse/CONFIGURATION-652). Thanks to Claude Warren. | [oheger](#team--oheger) |
| Update | Added a .gitignore file to the project. Fixes [CONFIGURATION-675](https://issues.apache.org/jira/browse/CONFIGURATION-675). | [oheger](#team--oheger) |
| Update | Bump Apache Commons Codec from 1.10 to 1.11. Fixes [CONFIGURATION-678](https://issues.apache.org/jira/browse/CONFIGURATION-678). | [ggregory](#team--ggregory) |
| Update | Bump Jackson from 2.8.9 to 2.9.3. Fixes [CONFIGURATION-679](https://issues.apache.org/jira/browse/CONFIGURATION-679). | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Lang from 3.6 to 3.7. Fixes [CONFIGURATION-680](https://issues.apache.org/jira/browse/CONFIGURATION-680). | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons VFS from 2.1 to 2.2. Fixes [CONFIGURATION-681](https://issues.apache.org/jira/browse/CONFIGURATION-681). | [ggregory](#team--ggregory) |
| Update | Bump Snakeyaml from 1.18 to 1.19. Fixes [CONFIGURATION-682](https://issues.apache.org/jira/browse/CONFIGURATION-682). | [ggregory](#team--ggregory) |
| Update | Bump optional dependency snakeyaml from 1.19 to 1.20. Fixes [CONFIGURATION-696](https://issues.apache.org/jira/browse/CONFIGURATION-696). | [ggregory](#team--ggregory) |
| Update | Bump Spring from 4.3.9.RELEASE to 4.3.13.RELEASE. Fixes [CONFIGURATION-683](https://issues.apache.org/jira/browse/CONFIGURATION-683). | [ggregory](#team--ggregory) |
| Update | Bump optional dependency Jackson from 2.9.3 to 2.9.5. Fixes [CONFIGURATION-695](https://issues.apache.org/jira/browse/CONFIGURATION-695). | [ggregory](#team--ggregory) |
| Update | Bump optional dependency Spring from 4.3.13.RELEASE to 4.3.14.RELEASE. Fixes [CONFIGURATION-697](https://issues.apache.org/jira/browse/CONFIGURATION-697). | [ggregory](#team--ggregory) |
| Fix | JSONConfiguration can now handle list structures with complex objects as elements. Fixes [CONFIGURATION-686](https://issues.apache.org/jira/browse/CONFIGURATION-686). | [oheger](#team--oheger) |
| Fix | Fixed a memory leak in CombinedConfigurationBuilder. Builder for the child sources were created each time a new result configuration was requested; thus the list with child builders got longer and longer. This also had an impact on reloading because unnecessary reloading operations could be triggered. Now it is guaranteed that child builders are created only once. Fixes [CONFIGURATION-687](https://issues.apache.org/jira/browse/CONFIGURATION-687). | [oheger](#team--oheger) |
| Fix | Fixed a bug related to the handling of multiple include files in PropertiesConfiguration. Fixes [CONFIGURATION-688](https://issues.apache.org/jira/browse/CONFIGURATION-688). | [oheger](#team--oheger) |
| Fix | ExprLookup.getVariables() no longer returns null, but a copy of the current variables of this lookup object. Fixes [CONFIGURATION-690](https://issues.apache.org/jira/browse/CONFIGURATION-690). | [oheger](#team--oheger) |
| Fix | ExprLookup now handles expressions that do not return a string result by converting them to string. Fixes [CONFIGURATION-691](https://issues.apache.org/jira/browse/CONFIGURATION-691). | [oheger](#team--oheger) |
| Add | ConversionExceptions thrown when accessing the properties of a configuration now contain the original cause of the exception. Fixes [CONFIGURATION-692](https://issues.apache.org/jira/browse/CONFIGURATION-692). | [oheger](#team--oheger) |
| Add | Configuration properties can now be converted to the data types File and Path. Fixes [CONFIGURATION-693](https://issues.apache.org/jira/browse/CONFIGURATION-693). Thanks to Lars W. | [oheger](#team--oheger) |
| Add | Add org.apache.commons.configuration2.MapConfiguration.toString(). Fixes [CONFIGURATION-698](https://issues.apache.org/jira/browse/CONFIGURATION-698). | [ggregory](#team--ggregory) |
| Add | CompositeConfiguration now supports an addConfigurationFirst() method to add child configurations with a higher priority. Fixes [CONFIGURATION-701](https://issues.apache.org/jira/browse/CONFIGURATION-701). Thanks to Nicholas Verbeck. | [oheger](#team--oheger) |
| Fix | XMLConfiguration now handles elements correctly whose value consists only of whitespace if the xml:space attribute is set to preserve. Fixes [CONFIGURATION-703](https://issues.apache.org/jira/browse/CONFIGURATION-703). Thanks to Pascal Essiembre. | [oheger](#team--oheger) |

<a id="changes--release-2.2-2017-10-12"></a>

## Release 2.2 – 2017-10-12

| Type | Changes | By |
| --- | --- | --- |
| Add | Added an Automatic-Module-Name header to the manifest for compatibility with the Java 9 module system. Fixes [CONFIGURATION-673](https://issues.apache.org/jira/browse/CONFIGURATION-673). Thanks to Andreas Kuhtz. | [oheger](#team--oheger) |
| Fix | Fixed a NPE in INIConfiguration when saving a configuration with an empty section. Fixes [CONFIGURATION-671](https://issues.apache.org/jira/browse/CONFIGURATION-671). | [oheger](#team--oheger) |
| Fix | The node model returned by SubnodeConfiguration.getNodeModel() has now the correct root node set. Fixes [CONFIGURATION-670](https://issues.apache.org/jira/browse/CONFIGURATION-670). | [oheger](#team--oheger) |
| Update | Bump optional Spring dependency from 4.2.5.RELEASE to 4.3.9.RELEASE. Fixes [CONFIGURATION-669](https://issues.apache.org/jira/browse/CONFIGURATION-669). | [ggregory](#team--ggregory) |
| Update | Bump Apache Commons Lang from 3.3.2 to 3.6. Fixes [CONFIGURATION-667](https://issues.apache.org/jira/browse/CONFIGURATION-667). | [ggregory](#team--ggregory) |
| Add | Add convenience ctor ConfigurationRuntimeException(String, Object...). Fixes [CONFIGURATION-666](https://issues.apache.org/jira/browse/CONFIGURATION-666). | [ggregory](#team--ggregory) |
| Add | Add org.apache.commons.configuration2.AbstractHierarchicalConfiguration.toString(). Fixes [CONFIGURATION-665](https://issues.apache.org/jira/browse/CONFIGURATION-665). | [ggregory](#team--ggregory) |
| Add | Add API org.apache.commons.configuration2.tree.ImmutableNode.getChildren(String). Fixes [CONFIGURATION-664](https://issues.apache.org/jira/browse/CONFIGURATION-664). | [ggregory](#team--ggregory) |
| Update | Fixed a typo in the upgrade to 2.0 guide. Fixes [CONFIGURATION-663](https://issues.apache.org/jira/browse/CONFIGURATION-663). | [oheger](#team--oheger) |
| Update | Bump platform requirement from Java 6 to 7. Fixes [CONFIGURATION-661](https://issues.apache.org/jira/browse/CONFIGURATION-661). | [ggregory](#team--ggregory) |
| Add | Add toString() methods here and there to help debugging. Fixes [CONFIGURATION-660](https://issues.apache.org/jira/browse/CONFIGURATION-660). | [ggregory](#team--ggregory) |
| Add | Add API org.apache.commons.configuration2.DataConfiguration.getURI(String) methods. Fixes [CONFIGURATION-658](https://issues.apache.org/jira/browse/CONFIGURATION-658). | [ggregory](#team--ggregory) |
| Add | Added new YAMLConfiguration class to support configuration files in YAML format. Fixes [CONFIGURATION-656](https://issues.apache.org/jira/browse/CONFIGURATION-656). Thanks to The Alchemist. | [oheger](#team--oheger) |
| Add | ConfigurationUtils and ConfigurationConverter now offer better support for immutable configurations. Fixes [CONFIGURATION-653](https://issues.apache.org/jira/browse/CONFIGURATION-653). Thanks to Vincent Maurin. | [oheger](#team--oheger) |
| Add | INIConfiguration can now be configured to use a custom separator between properties and values when writing an ini file. Fixes [CONFIGURATION-647](https://issues.apache.org/jira/browse/CONFIGURATION-647). Thanks to Vladimir Martinek. | [oheger](#team--oheger) |
| Add | Added new JSONConfiguration class to support configuration files in JSON format. Fixes [CONFIGURATION-258](https://issues.apache.org/jira/browse/CONFIGURATION-258). Thanks to The Alchemist. | [oheger](#team--oheger) |

<a id="changes--release-2.1.1-2017-02-05"></a>

## Release 2.1.1 – 2017-02-05

| Type | Changes | By |
| --- | --- | --- |
| Fix | Improved the handling of lists defined by a string with delimiter characters in XMLConfiguration. Such lists now retain their original format when the configuration is saved. Fixes [CONFIGURATION-649](https://issues.apache.org/jira/browse/CONFIGURATION-649). | [oheger](#team--oheger) |
| Fix | Made the IOFactory property of PropertiesBuilderParameter compatible with the most recent version of Commons BeanUtils. This version changed the handling of properties starting with multiple uppercase letters. Fixes [CONFIGURATION-648](https://issues.apache.org/jira/browse/CONFIGURATION-648). | [oheger](#team--oheger) |
| Fix | PropertiesConfiguration now works correctly with the auto-save mode. Fixes [CONFIGURATION-646](https://issues.apache.org/jira/browse/CONFIGURATION-646). | [oheger](#team--oheger) |
| Fix | PropertiesConfigurationLayout no longer duplicates a header comment if a file with another comment is loaded. Fixes [CONFIGURATION-644](https://issues.apache.org/jira/browse/CONFIGURATION-644). Thanks to Andrew DeMaria. | [oheger](#team--oheger) |
| Fix | Documentation improvements for the user's guide. Fixes [CONFIGURATION-643](https://issues.apache.org/jira/browse/CONFIGURATION-643). | [oheger](#team--oheger) |
| Fix | Improved documentation of FileBased interface. The Javadocs now state explicitly that the methods should not be called by client code. Exception handling in configuration classes implementing FileLocatorAware has been improved. Fixes [CONFIGURATION-641](https://issues.apache.org/jira/browse/CONFIGURATION-641). | [oheger](#team--oheger) |
| Fix | PropertiesConfiguration now correctly unescapes some special characters that are always escaped in Java properties files. Fixes [CONFIGURATION-640](https://issues.apache.org/jira/browse/CONFIGURATION-640). | [oheger](#team--oheger) |
| Update | In the OSGi bundle manifest of the Commons Configuration bundle the package imports for Spring packages are now marked as optional. Fixes [CONFIGURATION-639](https://issues.apache.org/jira/browse/CONFIGURATION-639). Thanks to Rico Neubauer. | [oheger](#team--oheger) |
| Update | Improved handling of temporary files and folders in unit tests. Fixes [CONFIGURATION-638](https://issues.apache.org/jira/browse/CONFIGURATION-638). Thanks to Ahmet Celik. | [oheger](#team--oheger) |
| Update | Updated dependency to Commons BeanUtils to version 1.9.3. This fixes an issue with an exception stacktrace that was logged when a ConfigurationBuilder was used. Fixes [CONFIGURATION-627](https://issues.apache.org/jira/browse/CONFIGURATION-627). | [oheger](#team--oheger) |

<a id="changes--release-2.1-2016-08-20"></a>

## Release 2.1 – 2016-08-20

| Type | Changes | By |
| --- | --- | --- |
| Fix | PropertiesConfigurationLayout now allows manipulating the order of keys when the properties file is written. Fixes [CONFIGURATION-636](https://issues.apache.org/jira/browse/CONFIGURATION-636). Thanks to Tim Lark. | [oheger](#team--oheger) |
| Fix | HomeDirectoryLocationStrategy now works correctly in the mode that evaluates the FileLocator's base path. Fixes [CONFIGURATION-634](https://issues.apache.org/jira/browse/CONFIGURATION-634). Thanks to Raviteja Lokineni. | [oheger](#team--oheger) |
| Fix | Interpolation was improved to better support properties with multiple values. Fixes [CONFIGURATION-633](https://issues.apache.org/jira/browse/CONFIGURATION-633). | [oheger](#team--oheger) |
| Fix | The methods getStringArray() and getList() of CompositeConfiguration now support the interpolation of variables that reference properties with multiple values. Fixes [CONFIGURATION-632](https://issues.apache.org/jira/browse/CONFIGURATION-632). | [oheger](#team--oheger) |
| Update | Support for the ant build was dropped. Fixes [CONFIGURATION-628](https://issues.apache.org/jira/browse/CONFIGURATION-628). | [oheger](#team--oheger) |
| Update | ImmutableConfiguration.getArray() has been deprecated. Arrays can now be queried using the generic get() method in a type-safe way. Fixes [CONFIGURATION-626](https://issues.apache.org/jira/browse/CONFIGURATION-626). | [oheger](#team--oheger) |
| Add | Support Commons Configuration as PropertySource in Spring. Fixes [CONFIGURATION-624](https://issues.apache.org/jira/browse/CONFIGURATION-624). | [deki](#team--deki) |
| Fix | Fixed a problem in INIConfiguration.write() with keys containing a separator character. This separator had been duplicated. Such keys are now handled correctly when the configuration is saved. Fixes [CONFIGURATION-622](https://issues.apache.org/jira/browse/CONFIGURATION-622). | [oheger](#team--oheger) |
| Update | Bump Apache Commons VFS from 2.0 to 2.1. Fixes [CONFIGURATION-631](https://issues.apache.org/jira/browse/CONFIGURATION-631). | [ggregory](#team--ggregory) |
| Update | Bump optional dependency Apache Commons Codec from 1.9 to 1.10. Fixes [CONFIGURATION-635](https://issues.apache.org/jira/browse/CONFIGURATION-635). | [ggregory](#team--ggregory) |

<a id="changes--release-2.0-2016-03-24"></a>

## Release 2.0 – 2016-03-24

| Type | Changes | By |
| --- | --- | --- |
| Update | Moved ConfigurationLogger class to io package to avoid cyclic dependencies between packages. Fixes [CONFIGURATION-621](https://issues.apache.org/jira/browse/CONFIGURATION-621). | [oheger](#team--oheger) |
| Fix | Fixed two invalid examples in the user's guide for file-based configurations. Fixes [CONFIGURATION-620](https://issues.apache.org/jira/browse/CONFIGURATION-620). Thanks to Mark Vedder. | [oheger](#team--oheger) |
| Add | CombinedConfigurationBuilder now supports inheritance of its parameters to child configuration sources. This is enabled by default. Fixes [CONFIGURATION-619](https://issues.apache.org/jira/browse/CONFIGURATION-619). | [oheger](#team--oheger) |
| Fix | When using immutable configurations exceptions thrown by the wrapped configuration came out as UndeclaredThrowableException. This has been fixed; now the correct original exception is thrown. Fixes [CONFIGURATION-618](https://issues.apache.org/jira/browse/CONFIGURATION-618). | [oheger](#team--oheger) |
| Update | Changed generic types in the signatures of a MapConfiguration constructor and AbstractConfiguration.getList(String, List). These changes were made in version 1.10 as fixes for CONFIGURATION-557 and CONFIGURATION-558. But it had been missed to merge them to trunk. Fixes [CONFIGURATION-615](https://issues.apache.org/jira/browse/CONFIGURATION-615). | [oheger](#team--oheger) |

<a id="changes--release-2.0-beta2-2015-12-05"></a>

## Release 2.0-beta2 – 2015-12-05

| Type | Changes | By |
| --- | --- | --- |
| Update | References to Commons Logging have been removed from the Configuration API. It is still possible to influence logging by making use of the new ConfigurationLogger abstraction. Fixes [CONFIGURATION-614](https://issues.apache.org/jira/browse/CONFIGURATION-614). | [oheger](#team--oheger) |
| Update | The return type of ConfigurationBuilder.getConfiguration() was changed from Configuration to ImmutableConfiguration because this is the base interface for all configuration objects. Fixes [CONFIGURATION-612](https://issues.apache.org/jira/browse/CONFIGURATION-612). Thanks to Jon Weygand. | [oheger](#team--oheger) |
| Fix | Fixed a bug in PropertiesConfiguration related to the loading of include files. The FileHandler used for this purpose was not fully initialized. Fixes [CONFIGURATION-609](https://issues.apache.org/jira/browse/CONFIGURATION-609). | [oheger](#team--oheger) |
| Fix | Adapted the return type of ReloadingFileBasedConfigurationBuilder.configure(). Fixes [CONFIGURATION-608](https://issues.apache.org/jira/browse/CONFIGURATION-608). | [oheger](#team--oheger) |
| Fix | XMLConfiguration no longer drops keys when list delimiter characters occur in element values. Fixes [CONFIGURATION-605](https://issues.apache.org/jira/browse/CONFIGURATION-605). | [oheger](#team--oheger) |
| Fix | Fixed a problem in the conversion of a flat configuration to a hierarchical one that could cause the loss of properties in a combined configuration constructed by an override combiner. Fixes [CONFIGURATION-604](https://issues.apache.org/jira/browse/CONFIGURATION-604). | [oheger](#team--oheger) |

<a id="changes--release-2.0-beta1-2015-06-19"></a>

## Release 2.0-beta1 – 2015-06-19

| Type | Changes | By |
| --- | --- | --- |
| Update | Removed obsolete ConfigurationBuilder interface in the base package. Fixes [CONFIGURATION-598](https://issues.apache.org/jira/browse/CONFIGURATION-598). Thanks to Bjarne Boström. | [oheger](#team--oheger) |

<a id="changes--release-2.0-alpha2-2014-12-20"></a>

## Release 2.0-alpha2 – 2014-12-20

| Type | Changes | By |
| --- | --- | --- |
| Add | DefaultExpressionEngine can now be customized to match configuration keys in a case-insensitive manner. This is useful for instance for dealing with Windows INI files. Fixes [CONFIGURATION-574](https://issues.apache.org/jira/browse/CONFIGURATION-574). | [oheger](#team--oheger) |
| Add | Added support for querying encoded properties. Fixes [CONFIGURATION-565](https://issues.apache.org/jira/browse/CONFIGURATION-565). | [oheger](#team--oheger) |
| Fix | PropertiesConfiguration now supports again properties without a value and a separator character. The keys of such properties are added to the configuration with an empty String as value. Fixes [CONFIGURATION-564](https://issues.apache.org/jira/browse/CONFIGURATION-564). | [oheger](#team--oheger) |
| Update | XMLPropertyListConfiguration can now save arrays in the correct form. Fixes [CONFIGURATION-427](https://issues.apache.org/jira/browse/CONFIGURATION-427). | [oheger](#team--oheger) |
| Add | A size() method was added to the ImmutableConfiguration interface. Fixes [CONFIGURATION-200](https://issues.apache.org/jira/browse/CONFIGURATION-200). | [oheger](#team--oheger) |

<a id="changes--release-2.0-alpha1-2014-09-23"></a>

## Release 2.0-alpha1 – 2014-09-23

| Type | Changes | By |
| --- | --- | --- |
| Update | Removed methods from ConfigurationConverter related to ExtendedProperties. This class is no longer supported by recent versions of Commons Collections. Fixes [CONFIGURATION-591](https://issues.apache.org/jira/browse/CONFIGURATION-591). | [oheger](#team--oheger) |
| Update | Removed Serializable interface from all configuration implementations. Some configuration classes declared this interface without being actually serializable. Fixes [CONFIGURATION-590](https://issues.apache.org/jira/browse/CONFIGURATION-590). | [oheger](#team--oheger) |
| Update | The name of the top-level package and the maven coordinates have been changed to allow a coexistence of Commons Configuration 1.x with 2.0. Fixes [CONFIGURATION-588](https://issues.apache.org/jira/browse/CONFIGURATION-588). | [oheger](#team--oheger) |
| Update | The event mechanism has been reworked. There is now a generic event listener interface which can be used to receive notifications from multiple types of event sources. Fixes [CONFIGURATION-584](https://issues.apache.org/jira/browse/CONFIGURATION-584). | [oheger](#team--oheger) |
| Fix | Fixed a StringIndexOutOfBoundsException in PropertiesConfigurationLayout which was caused by lines containing only whitespace. Fixes [CONFIGURATION-582](https://issues.apache.org/jira/browse/CONFIGURATION-582). | [oheger](#team--oheger) |
| Add | A migration guide has been created which supports when upgrading from version 1.x to 2.0. Fixes [CONFIGURATION-579](https://issues.apache.org/jira/browse/CONFIGURATION-579). | [oheger](#team--oheger) |
| Update | The user's guide has been fully reworked to cover all new and enhanced features of version 2.0. Fixes [CONFIGURATION-578](https://issues.apache.org/jira/browse/CONFIGURATION-578). | [oheger](#team--oheger) |
| Update | The dependency to Commons Collections is no longer needed. Fixes [CONFIGURATION-577](https://issues.apache.org/jira/browse/CONFIGURATION-577). | [oheger](#team--oheger) |
| Update | A new abstract base class for hierarchical configurations was introduced which supports arbitrary hierarchical data structures. The type of the nodes used by the configuration can now be specified as a generic type argument. This makes the integration of other hierarchical structures easier. Fixes [CONFIGURATION-576](https://issues.apache.org/jira/browse/CONFIGURATION-576). | [oheger](#team--oheger) |
| Update | Hierarchical configurations now operate on immutable structures. Data is no longer represented by ConfigurationNode objects. The ImmutableNode class now serves as data container. Fixes [CONFIGURATION-575](https://issues.apache.org/jira/browse/CONFIGURATION-575). | [oheger](#team--oheger) |
| Update | XPathExpressionEngine can now deal with namespace prefixes in node and attribute names. Fixes [CONFIGURATION-573](https://issues.apache.org/jira/browse/CONFIGURATION-573). | [oheger](#team--oheger) |
| Fix | When a CombinedConfiguration is cleared it removes itself as change listener from all child configurations. This fixes a possible memory leak. Fixes [CONFIGURATION-572](https://issues.apache.org/jira/browse/CONFIGURATION-572). | [oheger](#team--oheger) |
| Fix | Fixed a possible ConcurrentModificationException when a SystemConfiguration instance is passed to the append() or copy() methods. Fixes [CONFIGURATION-570](https://issues.apache.org/jira/browse/CONFIGURATION-570). | [oheger](#team--oheger) |
| Fix | XMLBeanDeclaration now escapes node names before they are used to determine nested properties. Fixes [CONFIGURATION-567](https://issues.apache.org/jira/browse/CONFIGURATION-567). Thanks to Shen liang. | [oheger](#team--oheger) |
| Update | The DefaultExpressionEngine class is now immutable. An instance can be shared between multiple configuration objects. Fixes [CONFIGURATION-563](https://issues.apache.org/jira/browse/CONFIGURATION-563). | [oheger](#team--oheger) |
| Update | Improved the API of ExprLookup. Fixes [CONFIGURATION-562](https://issues.apache.org/jira/browse/CONFIGURATION-562). | [oheger](#team--oheger) |
| Add | It is now possible to define default values for initialization properties of configurations. Fixes [CONFIGURATION-559](https://issues.apache.org/jira/browse/CONFIGURATION-559). | [oheger](#team--oheger) |
| Update | Fixed a bug in the handling of the xml:space attribute in XMLConfiguration. The attribute is now also applied to the current element, not only to sub elements. Fixes [CONFIGURATION-555](https://issues.apache.org/jira/browse/CONFIGURATION-555). | [oheger](#team--oheger) |
| Update | BeanHelper is no longer a static utility class. Instances can be created with a specific configuration of bean factories. There is still a default instance which can be obtained via the BeanHelper.INSTANCE field. Fixes [CONFIGURATION-554](https://issues.apache.org/jira/browse/CONFIGURATION-554). | [oheger](#team--oheger) |
| Update | The code for accessing configuration files hs been reworked. Methods related to locating configuration files have been moved from ConfigurationUtils to a new FileLocatorUtils class. Customizable strategy classes (implementing the new FileLocationStrategy) can be used for searching for configuration files. Fixes [CONFIGURATION-553](https://issues.apache.org/jira/browse/CONFIGURATION-553). | [oheger](#team--oheger) |
| Add | The data type conversion mechanism has been made extensible. There is a new interface ConversionHandler which controls the data type conversions available for a configuration object. By setting a custom implementation, conversions can be adapted or extended. Fixes [CONFIGURATION-551](https://issues.apache.org/jira/browse/CONFIGURATION-551). | [oheger](#team--oheger) |
| Add | Conversion to Character is now supported. Fixes [CONFIGURATION-550](https://issues.apache.org/jira/browse/CONFIGURATION-550). | [oheger](#team--oheger) |
| Update | BeanHelper can now process BeanDefinitions initializing properties of collection types of their target beans. Fixes [CONFIGURATION-546](https://issues.apache.org/jira/browse/CONFIGURATION-546). Thanks to Justin Couch. | [oheger](#team--oheger) |
| Update | Added missing dependencies to build.xml. Fixes [CONFIGURATION-544](https://issues.apache.org/jira/browse/CONFIGURATION-544). Thanks to Oliver Kopp. | [oheger](#team--oheger) |
| Update | The mechanism for synchronizing configurations has been completely redesigned. It is now based on Synchronizer objects which can be configured by client code. A new chapter was added to the user's guide regarding thread-safety of configurations. Fixes [CONFIGURATION-542](https://issues.apache.org/jira/browse/CONFIGURATION-542). | [oheger](#team--oheger) |
| Update | MapConfiguration now directly uses a Properties object passed to its constructor as data store rather than copying it. This allows SystemConfiguration to be connected to system properties; i.e. changing a property through SystemConfiguration immediately affects the corresponding system property. Fixes [CONFIGURATION-540](https://issues.apache.org/jira/browse/CONFIGURATION-540). | [oheger](#team--oheger) |
| Add | Multi-file configurations are no longer restricted to XML configuration files. Arbitrary file-based configurations are now supported. Fixes [CONFIGURATION-541](https://issues.apache.org/jira/browse/CONFIGURATION-541). | [oheger](#team--oheger) |
| Update | The deprecated INIConfiguration class was removed. HierarchicalINIConfiguration was renamed to INIConfiguration. Fixes [CONFIGURATION-539](https://issues.apache.org/jira/browse/CONFIGURATION-539). | [oheger](#team--oheger) |
| Update | The deprecated ConfigurationFactory class was removed. Fixes [CONFIGURATION-537](https://issues.apache.org/jira/browse/CONFIGURATION-537). | [oheger](#team--oheger) |
| Update | File-based configurations are now implemented in a different way. The interfaces FileConfiguration and ReloadingStrategy have been removed, also the base classes AbstractFileConfiguration and AbstractHierarchicalFileConfiguration. They are replaced by the FileBased interface and the FileHandler class which implements central I/O functionality. Reloading is now in the responsibility of configuration builders. Fixes [CONFIGURATION-536](https://issues.apache.org/jira/browse/CONFIGURATION-536). | [oheger](#team--oheger) |
| Add | DatabaseConfiguration now provides get methods for querying its properties defining the underlying database structures. Fixes [CONFIGURATION-535](https://issues.apache.org/jira/browse/CONFIGURATION-535). | [oheger](#team--oheger) |
| Update | The includesAllowed property of PropertyConfiguration is now independent from the existence of a base path. Fixes [CONFIGURATION-534](https://issues.apache.org/jira/browse/CONFIGURATION-534). | [oheger](#team--oheger) |
| Add | DatabaseConfiguration now automatically converts CLOBs to strings if they appear in property values. Fixes [CONFIGURATION-533](https://issues.apache.org/jira/browse/CONFIGURATION-533). | [oheger](#team--oheger) |
| Update | Concurrent access to configurations and reloading have been completely redesigned. Because reloading is now handled by configuration builders there is no need to acquire a lock in order to protected against a reload operations. Fixes [CONFIGURATION-530](https://issues.apache.org/jira/browse/CONFIGURATION-530). | [oheger](#team--oheger) |
| Update | AbstractConfiguration.clearPropertyDirect() is now abstract. Fixes [CONFIGURATION-527](https://issues.apache.org/jira/browse/CONFIGURATION-527). Thanks to Matthias Richter. | [oheger](#team--oheger) |
| Update | XMLPropertiesConfiguration now supports loading from and saving to DOM nodes. Fixes [CONFIGURATION-526](https://issues.apache.org/jira/browse/CONFIGURATION-526). Thanks to Oliver Kopp. | [oheger](#team--oheger) |
| Add | PropertiesConfiguration now keeps a comment at the bottom of a properties file. A new footer property was added for reading and writing this footer comment. Fixes [CONFIGURATION-525](https://issues.apache.org/jira/browse/CONFIGURATION-525). | [oheger](#team--oheger) |
| Update | Interpolation now works correctly after a configuration was cloned. The ConfigurationInterpolator instance is now cloned, too. Fixes [CONFIGURATION-524](https://issues.apache.org/jira/browse/CONFIGURATION-524). | [oheger](#team--oheger) |
| Update | ConfigurationUtils.fileFromUrl() now correctly handles URL containing encoded percent characters. Fixes [CONFIGURATION-521](https://issues.apache.org/jira/browse/CONFIGURATION-521). Thanks to Oliver Kopp. | [oheger](#team--oheger) |
| Update | Support for reloading of configuration data has been reworked. Fixes [CONFIGURATION-520](https://issues.apache.org/jira/browse/CONFIGURATION-520). | [oheger](#team--oheger) |
| Add | Configuration objects are now created via configuration builders. A new API for configuration builders has been added. Fixes [CONFIGURATION-519](https://issues.apache.org/jira/browse/CONFIGURATION-519). | [oheger](#team--oheger) |
| Update | Classes and interfaces related to interpolation have been slightly reworked. ConfigurationInterpolator is now thread-safe. There are multiple ways to define the ConfigurationInterpolator object to be used by an AbstractConfiguration instance. Fixes [CONFIGURATION-518](https://issues.apache.org/jira/browse/CONFIGURATION-518). | [oheger](#team--oheger) |
| Add | Hierarchical configurations now provide methods to obtain sub configurations for all child elements of a given key. Fixes [CONFIGURATION-517](https://issues.apache.org/jira/browse/CONFIGURATION-517). | [oheger](#team--oheger) |
| Update | PropertiesConfiguration no longer escapes double quotes on saving. Fixes [CONFIGURATION-516](https://issues.apache.org/jira/browse/CONFIGURATION-516). | [oheger](#team--oheger) |
| Update | The visibility of some internal methods of PropertiesConfiguration.PropertiesWriter has been increased to protected. This simplifies the implementation of a custom escaping strategy. Fixes [CONFIGURATION-515](https://issues.apache.org/jira/browse/CONFIGURATION-515). | [oheger](#team--oheger) |
| Add | Bean declarations now support constructor invocations. Fixes [CONFIGURATION-514](https://issues.apache.org/jira/browse/CONFIGURATION-514). | [oheger](#team--oheger) |
| Update | HierarchicalConfiguration is now an interface. The base implementation class is named BaseHierarchicalConfiguration. Fixes [CONFIGURATION-513](https://issues.apache.org/jira/browse/CONFIGURATION-513). | [oheger](#team--oheger) |
| Add | It is now possible to obtain an immutable view on a Configuration or HierarchicalConfiguration object. New interfaces, ImmutableConfiguration, and ImmutableHierarchicalConfiguration have been introduced. Fixes [CONFIGURATION-512](https://issues.apache.org/jira/browse/CONFIGURATION-512). | [oheger](#team--oheger) |
| Add | Generic get() methods have been added to the Configuration interface. These methods expect a target class and try to convert the value of the specified property to this target class. Fixes [CONFIGURATION-508](https://issues.apache.org/jira/browse/CONFIGURATION-508). | [oheger](#team--oheger) |
| Update | Removed obsolete nested classes Node and NodeVisitor of HierarchicalConfiguration. The related deprecated class ConfigurationKey was removed, too. Fixes [CONFIGURATION-506](https://issues.apache.org/jira/browse/CONFIGURATION-506). | [oheger](#team--oheger) |
| Update | XMLConfiguration no longer supports attributes with multiple values or list delimiter parsing in attributes. This feature was complex and error prone and brought little value to the user. Fixes [CONFIGURATION-505](https://issues.apache.org/jira/browse/CONFIGURATION-505). | [oheger](#team--oheger) |
| Update | SubnodeConfiguration now provides a new method for clearing it and removing its root node from the parent configuration. The method HierarchicalConfiguration.configurationsAt() now returns a list of SubnodeConfiguration so that it is easier to make direct use of this feature. Fixes [CONFIGURATION-504](https://issues.apache.org/jira/browse/CONFIGURATION-504). | [oheger](#team--oheger) |
| Update | XMLConfiguration now adds attributes of elements defining a list to all list nodes. Fixes [CONFIGURATION-500](https://issues.apache.org/jira/browse/CONFIGURATION-500). | [oheger](#team--oheger) |
| Update | Concurrent access to configurations and reloading have been completely redesigned. This should reduce the amount of synchronization. Fixes [CONFIGURATION-496](https://issues.apache.org/jira/browse/CONFIGURATION-496). | [oheger](#team--oheger) |
| Update | Removed some static fields for specifying global default values. Using static fields in this way is thread-hostile. There are now alternatives for setting default values. Fixes [CONFIGURATION-486](https://issues.apache.org/jira/browse/CONFIGURATION-486). | [oheger](#team--oheger) |
| Update | Updated dependency to Commons Lang from version 2.6 to 3.1. Fixes [CONFIGURATION-462](https://issues.apache.org/jira/browse/CONFIGURATION-462). | [oheger](#team--oheger) |
| Update | EventSource is now an interface. With BaseEventSource there is a default implementation. Fixes [CONFIGURATION-419](https://issues.apache.org/jira/browse/CONFIGURATION-419). | [oheger](#team--oheger) |
| Update | The handling of list delimiters and their escape characters has been reworked. A new ListDelimiterHandler interface was introduced allowing applications to customize the treatment of list delimiters. Fixes [CONFIGURATION-418](https://issues.apache.org/jira/browse/CONFIGURATION-418). | [oheger](#team--oheger) |
| Update | Concurrent access to configurations has been reworked. Fixes [CONFIGURATION-330](https://issues.apache.org/jira/browse/CONFIGURATION-330). | [oheger](#team--oheger) |
| Add | With the new reloading mechanism automatic and periodic reloading checks can be performed. Fixes [CONFIGURATION-204](https://issues.apache.org/jira/browse/CONFIGURATION-204). | [oheger](#team--oheger) |
| Add | Reloading checks can now be performed in a background thread. Fixes [CONFIGURATION-202](https://issues.apache.org/jira/browse/CONFIGURATION-202). | [oheger](#team--oheger) |
| Update | It is now possible to define the strategy used for locating configuration files. Fixes [CONFIGURATION-153](https://issues.apache.org/jira/browse/CONFIGURATION-153). | [oheger](#team--oheger) |
| Update | Reloading can no longer corrupt a configuration instance. This is now handled by a configuration builder; the original configuration instance is not modified. Fixes [CONFIGURATION-136](https://issues.apache.org/jira/browse/CONFIGURATION-136). | [oheger](#team--oheger) |
| Update | It is now possible to influence the conversion from a container object (a collection or an array) to a single value (e.g. what is returned by getString() if the current property has multiple values). Per default, the first value is returned. By overriding methods of the configuration's ConversionHandler, this behavior can be changed. Fixes [CONFIGURATION-26](https://issues.apache.org/jira/browse/CONFIGURATION-26). | [oheger](#team--oheger) |

<a id="changes--release-1.10-2013-10-27"></a>

## Release 1.10 – 2013-10-27

| Type | Changes | By |
| --- | --- | --- |
| Update | XMLConfiguration now adds attributes of elements defining a list to all list nodes. Fixes [CONFIGURATION-500](https://issues.apache.org/jira/browse/CONFIGURATION-500). | [oheger](#team--oheger) |
| Add | PropertiesConfiguration now keeps a comment at the bottom of a properties file. A new footer property was added for reading and writing this footer comment. Fixes [CONFIGURATION-525](https://issues.apache.org/jira/browse/CONFIGURATION-525). | [oheger](#team--oheger) |
| Update | XMLPropertiesConfiguration now supports loading from and saving to DOM nodes. Fixes [CONFIGURATION-526](https://issues.apache.org/jira/browse/CONFIGURATION-526). Thanks to Oliver Kopp. | [oheger](#team--oheger) |
| Update | The includesAllowed property of PropertyConfiguration is now independent from the existence of a base path. Fixes [CONFIGURATION-534](https://issues.apache.org/jira/browse/CONFIGURATION-534). | [oheger](#team--oheger) |
| Update | BeanHelper can now process BeanDefinitions initializing properties of collection types of their target beans. Fixes [CONFIGURATION-546](https://issues.apache.org/jira/browse/CONFIGURATION-546). Thanks to Justin Couch. | [oheger](#team--oheger) |
| Add | Conversion to Character is now supported. Fixes [CONFIGURATION-550](https://issues.apache.org/jira/browse/CONFIGURATION-550). | [oheger](#team--oheger) |
| Update | Fixed a bug in the handling of the xml:space attribute in XMLConfiguration. The attribute is now also applied to the current element, not only to sub elements. Fixes [CONFIGURATION-555](https://issues.apache.org/jira/browse/CONFIGURATION-555). | [oheger](#team--oheger) |
| Fix | In 1.7 and before, any change to the system properties was immediately reflected in a SystemConfiguration object. This behavior broke in 1.8 and 1.9. This has been fixed for 1.10. Fixes [CONFIGURATION-556](https://issues.apache.org/jira/browse/CONFIGURATION-556). | [henning](#team--henning) |
| Fix | In 1.7 and before, it was possible to pass an arbitrary Map into the constructor of MapConfiguration. With the generification in 1.8, this actually broke and it was no longer possible to pass in e.g. a Map<String, String> because the signature now required a Map<String, Object>. Changing the constructor to accept a Map<String, ?> restores this. Fixes [CONFIGURATION-557](https://issues.apache.org/jira/browse/CONFIGURATION-557). | [henning](#team--henning) |
| Fix | Similar to CONFIGURATION-557, the getList(String, List) method was generified to be getList(String, List<Object>) but needs to be getList(String, List<?>) so that code that used a more specific list (such as a List<String>) still compiles against the new API. Fixes [CONFIGURATION-558](https://issues.apache.org/jira/browse/CONFIGURATION-558). | [henning](#team--henning) |

<a id="changes--release-1.9-2012-08-22"></a>

## Release 1.9 – 2012-08-22

| Type | Changes | By |
| --- | --- | --- |
| Update | Small changes in user guide documentation. Fixes [CONFIGURATION-503](https://issues.apache.org/jira/browse/CONFIGURATION-503). Thanks to Tino Sino. | [oheger](#team--oheger) |
| Update | Improvements of basic features and AbstractConfiguration documentation. Fixes [CONFIGURATION-502](https://issues.apache.org/jira/browse/CONFIGURATION-502). Thanks to Tino Sino. | [oheger](#team--oheger) |
| Add | XMLPropertyListConfiguration no longer swallows exception caused by invalid date properties. Now a warning message is logged. Fixes [CONFIGURATION-501](https://issues.apache.org/jira/browse/CONFIGURATION-501). | [oheger](#team--oheger) |
| Fix | List properties can now be set correctly on a HierarchicalConfiguration if delimiter parsing is disabled. Fixes [CONFIGURATION-495](https://issues.apache.org/jira/browse/CONFIGURATION-495). | [oheger](#team--oheger) |
| Update | Made static DateFormat fields in XMLPropertyListConfiguration.PListNode final and added a note about proper synchronization. Fixes [CONFIGURATION-488](https://issues.apache.org/jira/browse/CONFIGURATION-488). | [oheger](#team--oheger) |
| Fix | DataConfiguration.get() now also works with String properties and if no data type conversion is required. Fixes [CONFIGURATION-487](https://issues.apache.org/jira/browse/CONFIGURATION-487). | [oheger](#team--oheger) |
| Update | DatabaseConfiguration now always closes the result set. Fixes [CONFIGURATION-483](https://issues.apache.org/jira/browse/CONFIGURATION-483). | [oheger](#team--oheger) |
| Update | The Import-Package section in the OSGi manifest now uses the resolution:=optional directive for optional dependencies. Fixes [CONFIGURATION-482](https://issues.apache.org/jira/browse/CONFIGURATION-482). Thanks to Chris Seieroe. | [oheger](#team--oheger) |
| Fix | Variable substitution in configuration sources declared in a definition file for DefaultConfigurationBuilder now works across multiple sources. Fixes [CONFIGURATION-481](https://issues.apache.org/jira/browse/CONFIGURATION-481). | [oheger](#team--oheger) |
| Fix | PropertyListConfiguration now can deal with C-style comments in plist configuration files. Both block and single-line comments are supported. Fixes [CONFIGURATION-477](https://issues.apache.org/jira/browse/CONFIGURATION-477). | [oheger](#team--oheger) |

<a id="changes--release-1.8-2012-02-04"></a>

## Release 1.8 – 2012-02-04

| Type | Changes | By |
| --- | --- | --- |
| Fix | Fixed possible ClassCastExceptions in CompositeConfiguration related to special in-memory configurations. Fixes [CONFIGURATION-476](https://issues.apache.org/jira/browse/CONFIGURATION-476). | [oheger](#team--oheger) |
| Update | Class ConfigurationKey was deprecated in favor of DefaultConfigurationKey. Fixes [CONFIGURATION-475](https://issues.apache.org/jira/browse/CONFIGURATION-475). | [oheger](#team--oheger) |
| Update | Implemented delimiter parsing in HierarchicalINIConfiguration to be consistent with other Configuration implementations. Note that this can impact existing code. To switch back to the old behavior, call setDelimiterParsingDisabled(true) before loading the configuration. Fixes [CONFIGURATION-474](https://issues.apache.org/jira/browse/CONFIGURATION-474). | [oheger](#team--oheger) |
| Add | CompositeConfiguration now provides better support for child configurations that are used as in-memory configuration. Fixes [CONFIGURATION-471](https://issues.apache.org/jira/browse/CONFIGURATION-471). | [oheger](#team--oheger) |
| Update | Classes generated by JavaCC are now created dynamically during the build process. Fixes [CONFIGURATION-470](https://issues.apache.org/jira/browse/CONFIGURATION-470). | [oheger](#team--oheger) |
| Add | Commons Configuration now requires Java 5 or later. | [ebourg](#team--ebourg) |
| Add | Binary literals are now supported (i.e Ob11010001). Fixes [CONFIGURATION-466](https://issues.apache.org/jira/browse/CONFIGURATION-466). | [ebourg](#team--ebourg) |
| Update | Updated the dependency to Commons Jexl to version 2.1.1. This version provides correct OSGi manifest headers. Fixes [CONFIGURATION-465](https://issues.apache.org/jira/browse/CONFIGURATION-465). | [oheger](#team--oheger) |
| Update | Improved documentation of AbstractFileConfiguration related to load() methods and their impact on the base path. Fixes [CONFIGURATION-463](https://issues.apache.org/jira/browse/CONFIGURATION-463). | [oheger](#team--oheger) |
| Update | The project now uses standard Maven directory layout. Fixes [CONFIGURATION-461](https://issues.apache.org/jira/browse/CONFIGURATION-461). | [oheger](#team--oheger) |

<a id="changes--release-1.7-2011-09-07"></a>

## Release 1.7 – 2011-09-07

| Type | Changes | By |
| --- | --- | --- |
| Fix | Reloading now also works for configuration sources declared in the additional section of a configuration definition file for DefaultConfigurationBuilder. Fixes [CONFIGURATION-460](https://issues.apache.org/jira/browse/CONFIGURATION-460). | [oheger](#team--oheger) |
| Update | ConfigurationFactory has been deprecated. The user guide was updated to no more mention this class. Fixes [CONFIGURATION-459](https://issues.apache.org/jira/browse/CONFIGURATION-459). | [oheger](#team--oheger) |
| Add | HierarchicalConfiguration now provides a specific implementation of the clear() method. This is more efficient and also solves some other problems related to clearing a SubnodeConfiguration. Fixes [CONFIGURATION-458](https://issues.apache.org/jira/browse/CONFIGURATION-458). | [oheger](#team--oheger) |
| Update | Improved Javadocs of getKeys(String) method for some configuration classes. Fixes [CONFIGURATION-456](https://issues.apache.org/jira/browse/CONFIGURATION-456). | [oheger](#team--oheger) |
| Update | HierarchicalINIConfiguration.getSection() now creates a section if it does not exist. The SubnodeConfiguration returned by this method is now always connected to the parent ini configuration. Fixes [CONFIGURATION-455](https://issues.apache.org/jira/browse/CONFIGURATION-455). | [oheger](#team--oheger) |
| Add | XPathExpressionEngine now provides better support for the setProperty() method. Fixes [CONFIGURATION-452](https://issues.apache.org/jira/browse/CONFIGURATION-452). | [oheger](#team--oheger) |
| Add | The parsing of ini files has been improved for property definitions containing multiple separator characters. Fixes [CONFIGURATION-448](https://issues.apache.org/jira/browse/CONFIGURATION-448). | [oheger](#team--oheger) |
| Add | DefaultConfigurationBuilder now supports including environment properties using the "env" tag. Fixes [CONFIGURATION-447](https://issues.apache.org/jira/browse/CONFIGURATION-447). | [oheger](#team--oheger) |
| Update | XMLConfiguration now handles attributes correctly whose value is an empty string. Fixes [CONFIGURATION-446](https://issues.apache.org/jira/browse/CONFIGURATION-446). | [oheger](#team--oheger) |
| Fix | Transforming a CombinedConfiguration with ViewNodes to an XMLConfiguration could cause problems with attributes. This has been fixed. Fixes [CONFIGURATION-445](https://issues.apache.org/jira/browse/CONFIGURATION-445). | [oheger](#team--oheger) |
| Update | Child configuration builders created for a <configuration> element in a configuration definition file now inherit the configuration and error listeners from the original DefaultConfigurationBuilder. This makes it possible to suppress log output created for optional configurations. Fixes [CONFIGURATION-439](https://issues.apache.org/jira/browse/CONFIGURATION-439). | [oheger](#team--oheger) |
| Update | JNDIConfiguration.getKeys() no more logs an exception if the prefix does not exist. Fixes [CONFIGURATION-438](https://issues.apache.org/jira/browse/CONFIGURATION-438). Thanks to Mike Noordermeer. | [oheger](#team--oheger) |
| Update | Child configuration builders created for a <configuration> element in a configuration definition file now inherit some of their properties from the builder object which processed the file. Fixes [CONFIGURATION-437](https://issues.apache.org/jira/browse/CONFIGURATION-437). | [oheger](#team--oheger) |
| Update | The optional dependency to Apache Ant has been changed to the new groupId org.apache.ant. The version was updated to the most recent version 1.8.2 (older versions should still work). Fixes [CONFIGURATION-436](https://issues.apache.org/jira/browse/CONFIGURATION-436). | [oheger](#team--oheger) |
| Fix | HierarchicalINIConfiguration now recognizes comment characters in property definitions only if they are preceded by whitespace. Thus comment characters can now be part of the property value. This is for instance required for the definition of file paths which use the semicolon as path separator. Fixes [CONFIGURATION-434](https://issues.apache.org/jira/browse/CONFIGURATION-434). | [oheger](#team--oheger) |
| Fix | Minor improvements of the support for indexed properties in ConfigurationDynaBean. Fixes [CONFIGURATION-433](https://issues.apache.org/jira/browse/CONFIGURATION-433). | [oheger](#team--oheger) |
| Fix | The methods getList() and getStringArray() of AbstractConfiguration can now handle single-valued properties of primitive types. Fixes [CONFIGURATION-432](https://issues.apache.org/jira/browse/CONFIGURATION-432). | [oheger](#team--oheger) |
| Fix | XMLConfiguration no longer escapes backslashs in the values of XML elements. Fixes [CONFIGURATION-428](https://issues.apache.org/jira/browse/CONFIGURATION-428). | [oheger](#team--oheger) |
| Fix | HierarchicalINIConfiguration now works correctly with configurations that contain only properties in the global section. Fixes [CONFIGURATION-424](https://issues.apache.org/jira/browse/CONFIGURATION-424). | [oheger](#team--oheger) |
| Fix | testFromClassPath() can fail when it should not because of inconsistent escaping of output from PropertiesConfiguration.getURL() and FileChangedReloadingStrategy.getFile().toURL(). Fixes [CONFIGURATION-423](https://issues.apache.org/jira/browse/CONFIGURATION-423). Thanks to William Buckley. | [rgoers](#team--rgoers) |
| Fix | A bug related to the interpretation of escape sequences for backslashes has been fixed. The user guide has also been improved in this area. Fixes [CONFIGURATION-418](https://issues.apache.org/jira/browse/CONFIGURATION-418). | [oheger](#team--oheger) |
| Fix | Files with a plus character in their names are now handled correctly. Fixes [CONFIGURATION-415](https://issues.apache.org/jira/browse/CONFIGURATION-415). | [oheger](#team--oheger) |
| Fix | SubsetConfiguration now produces correct events. Fixes [CONFIGURATION-413](https://issues.apache.org/jira/browse/CONFIGURATION-413). Thanks to Alexander Prishchepov. | [oheger](#team--oheger) |
| Add | DatabaseConfiguration can now be instructed to perform a commit after an update of the managed database table. This makes it usable in environments where the connections do not use auto-commit mode. Fixes [CONFIGURATION-412](https://issues.apache.org/jira/browse/CONFIGURATION-412). | [oheger](#team--oheger) |
| Add | Added a refresh() method to AbstractFileConfiguration and AbstractHierarchicalFileConfiguration. Fixes [CONFIGURATION-410](https://issues.apache.org/jira/browse/CONFIGURATION-410). | [oheger](#team--oheger) |
| Fix | HierarchicalINIConfiguration now correctly saves sections whose name contains delimiter characters. Fixes [CONFIGURATION-409](https://issues.apache.org/jira/browse/CONFIGURATION-409). | [oheger](#team--oheger) |
| Update | PropertiesConfiguration.save() escaped slashes in properties values. This was caused by a bug in commons-lang 2.4. Updating to the new version commons-lang 2.5 fixed this problem. Fixes [CONFIGURATION-408](https://issues.apache.org/jira/browse/CONFIGURATION-408). | [oheger](#team--oheger) |
| Fix | Fixed a potential IllegalStateException in HierarchicalINIConfiguration that can be thrown when the global section is requested concurrently. Fixes [CONFIGURATION-407](https://issues.apache.org/jira/browse/CONFIGURATION-407). | [oheger](#team--oheger) |
| Fix | XMLPropertyListConfiguration no longer throws a ConfigurationException if the file to be loaded does not have an outer dict element. Fixes [CONFIGURATION-405](https://issues.apache.org/jira/browse/CONFIGURATION-405). | [oheger](#team--oheger) |
| Fix | The default expression engine used by hierarchical configurations used to throw a NumberFormatException if invalid indices were used in property keys. This has been fixed. As a side effect brackets can now be used in property keys. Fixes [CONFIGURATION-404](https://issues.apache.org/jira/browse/CONFIGURATION-404). Thanks to Rob Walker. | [oheger](#team--oheger) |
| Fix | When an empty XMLConfiguration was saved and reloaded the root element was assigned an empty text value. Because of this isEmpty() returned false for this configuration. This has been fixed. Fixes [CONFIGURATION-403](https://issues.apache.org/jira/browse/CONFIGURATION-403). | [oheger](#team--oheger) |
| Add | Default variable interpolation now supports the env: prefix for referencing environment variables. Fixes [CONFIGURATION-399](https://issues.apache.org/jira/browse/CONFIGURATION-399). | [oheger](#team--oheger) |
| Fix | Schema violation exceptions are now propagated back to the caller. Fixes [CONFIGURATION-397](https://issues.apache.org/jira/browse/CONFIGURATION-397). | [rgoers](#team--rgoers) |
| Fix | XMLConfiguration and CombinedConfiguraton are now synchronized to fix problems caused by reloading in a multithreaded environment. Fixes [CONFIGURATION-390](https://issues.apache.org/jira/browse/CONFIGURATION-390). | [rgoers](#team--rgoers) |
| Fix | HierarchicalConfiguration.NodeVisitor is now passed the correct key to its visitAfterChildren() method. Fixes [CONFIGURATION-396](https://issues.apache.org/jira/browse/CONFIGURATION-396). | [oheger](#team--oheger) |
| Fix | BaseConfiguration.clone() now also clones collections stored in the internal map. This causes list properties to be handled correctly. Fixes [CONFIGURATION-393](https://issues.apache.org/jira/browse/CONFIGURATION-393). | [oheger](#team--oheger) |
| Add | DefaultConfigurationBuilder now supports defining ini files in its configuration definition file. Fixes [CONFIGURATION-389](https://issues.apache.org/jira/browse/CONFIGURATION-389). | [oheger](#team--oheger) |
| Fix | Attribute or element values will not be escaped when attribute or element splitting are disabled. Fixes [CONFIGURATION-388](https://issues.apache.org/jira/browse/CONFIGURATION-388). | [rgoers](#team--rgoers) |
| Add | When using Commons Lang 2.6 or higher as dependency nested interpolation in variable names is supported. Fixes [CONFIGURATION-363](https://issues.apache.org/jira/browse/CONFIGURATION-363). | [oheger](#team--oheger) |
| Fix | Empty dictionaries in a PropertyList configuration are now preserved when the configuration is saved. Fixes [CONFIGURATION-362](https://issues.apache.org/jira/browse/CONFIGURATION-362). | [ebourg](#team--ebourg) |
| Fix | DatabaseConfiguration now generates correct events for the clear() and clearProperty() methods. Fixes [CONFIGURATION-385](https://issues.apache.org/jira/browse/CONFIGURATION-385). | [oheger](#team--oheger) |
| Add | Add ExprLookup to allow expressions to be evaluated in configurations. When used, this requires that Apache Commons Jexl be added as a dependency to projects using Commons Configuration. Fixes [CONFIGURATION-380](https://issues.apache.org/jira/browse/CONFIGURATION-380). | [rgoers](#team--rgoers) |
| Add | MapConfiguration now provides a way of controlling the trimming behavior. Fixes [CONFIGURATION-374](https://issues.apache.org/jira/browse/CONFIGURATION-374). | [oheger](#team--oheger) |
| Add | Added MergeCombiner to allow elements in two configurations to be merged when the element and attributes in the first file match those in the second file. Fixes [CONFIGURATION-378](https://issues.apache.org/jira/browse/CONFIGURATION-378). | [rgoers](#team--rgoers) |
| Add | File system access has been abstracted to a FileSystem interface. Two implementations are provided, DefaultFileSystem that behaves in a backward compatible manner and VFSFileSystem which uses Commons VFS to retreive and store files. Fixes [CONFIGURATION-340](https://issues.apache.org/jira/browse/CONFIGURATION-340). | [rgoers](#team--rgoers) |
| Add | PropertiesConfigurationLayout now allows setting the line separator to be used when writing the properties file. Fixes [CONFIGURATION-314](https://issues.apache.org/jira/browse/CONFIGURATION-314). | [oheger](#team--oheger) |
| Add | PropertiesConfigurationLayout now also stores the property separators used for the single properties. It is also possible to change them for specific properties or set a global properties separator. In earlier versions the separator was hard-coded to " = ". Fixes [CONFIGURATION-371](https://issues.apache.org/jira/browse/CONFIGURATION-371). | [oheger](#team--oheger) |
| Add | PropertiesConfiguration now defines a nested interface IOFactory. Using this interface it is possible to inject custom PropertiesReader and PropertiesWriter implementations. Fixes [CONFIGURATION-370](https://issues.apache.org/jira/browse/CONFIGURATION-370). | [oheger](#team--oheger) |
| Fix | SubnodeConfiguration now fires an event of type EVENT\_SUBNODE\_CHANGED if a structural change of the parent configuration was detected. If the SubnodeConfiguration is contained in a CombinedConfiguration, the CombinedConfiguration receives this event and can update itself. Fixes [CONFIGURATION-368](https://issues.apache.org/jira/browse/CONFIGURATION-368). | [oheger](#team--oheger) |
| Fix | MultiFileHierarchicalConfiguration was not using basepath to construct the file url. It also threw an exception if the file pattern resolved to a non-existent file. This is now configurable. Fixes [CONFIGURATION-361](https://issues.apache.org/jira/browse/CONFIGURATION-361). | [rgoers](#team--rgoers) |
| Update | Align interpolation functionality of SubnodeConfiguration and SubsetConfiguration. SubsetConfiguration will now also interpolate keys of the parent configuration or use the local lookups of its parent. SubnodeConfiguration is in turn now able to lookup local keys as well. Fixes [CONFIGURATION-375](https://issues.apache.org/jira/browse/CONFIGURATION-375). | [joehni](#team--joehni) |
| Update | Align interpolation functionality of SubnodeConfiguration and SubsetConfiguration. Fixes [CONFIGURATION-376](https://issues.apache.org/jira/browse/CONFIGURATION-376). | [joehni](#team--joehni) |
| Update | Align interpolation functionality of SubnodeConfiguration and SubsetConfiguration. Fixes [CONFIGURATION-377](https://issues.apache.org/jira/browse/CONFIGURATION-377). | [joehni](#team--joehni) |
| Fix | SubsetConfiguration did not use locally registered lookups of its interpolator. Fixes [CONFIGURATION-369](https://issues.apache.org/jira/browse/CONFIGURATION-369). | [joehni](#team--joehni) |
| Fix | Fixed broken links to the API documentation in the user's guide. Fixes [CONFIGURATION-359](https://issues.apache.org/jira/browse/CONFIGURATION-359). | [oheger](#team--oheger) |
| Update | Improvements of the user's guide for hierarchical configurations. Fixes [CONFIGURATION-358](https://issues.apache.org/jira/browse/CONFIGURATION-358). | [oheger](#team--oheger) |
| Fix | The message of the ConversionException thrown by AbstractConfiguration.getBigInteger() is now correct. Fixes [CONFIGURATION-357](https://issues.apache.org/jira/browse/CONFIGURATION-357). | [oheger](#team--oheger) |
| Add | Added getConfigurations and getConfigurationNameList. Fixes [CONFIGURATION-356](https://issues.apache.org/jira/browse/CONFIGURATION-356). | [rgoers](#team--rgoers) |
| Add | Allow configurations to be validated using XML Schemas. Fixes [CONFIGURATION-257](https://issues.apache.org/jira/browse/CONFIGURATION-257). | [rgoers](#team--rgoers) |
| Add | Allow configurations to be validated using XML Schemas. Fixes [CONFIGURATION-355](https://issues.apache.org/jira/browse/CONFIGURATION-355). | [rgoers](#team--rgoers) |

<a id="changes--release-1.6-2008-12-25"></a>

## Release 1.6 – 2008-12-25

| Type | Changes | By |
| --- | --- | --- |
| Update | Some dependencies to other Commons components have been updated to the recent versions. Affected are Commons Lang, Commons Collections, Commons Logging, Commons BeanUtils, and Commons JXPath. The older versions should still work. | [oheger](#team--oheger) |
| Add | Allow system properties to be set from a configuration file. Fixes [CONFIGURATION-353](https://issues.apache.org/jira/browse/CONFIGURATION-353). | [rgoers](#team--rgoers) |
| Add | Allow variable resolvers to be defined configured in DefaultConfigurationBuilder. Fixes [CONFIGURATION-351](https://issues.apache.org/jira/browse/CONFIGURATION-351). | [rgoers](#team--rgoers) |
| Add | Added MultiFileHierarchicalConfiguration, DynamicCombinedConfiguration and PatternSubtreeConfigurationWrapper. Fixes [CONFIGURATION-350](https://issues.apache.org/jira/browse/CONFIGURATION-350). | [rgoers](#team--rgoers) |
| Add | The visibility of DefaultConfigurationBuilder.XMLConfigurationProvider was changed from package local to public. This makes it easier to implement providers that create configuration classes derived from XMLConfiguration. Fixes [CONFIGURATION-349](https://issues.apache.org/jira/browse/CONFIGURATION-349). Thanks to Ralph Goers. | [oheger](#team--oheger) |
| Fix | AbstractHierarchicalFileConfiguration.getKeys() now also checks whether a reload is required. Fixes [CONFIGURATION-348](https://issues.apache.org/jira/browse/CONFIGURATION-348). | [oheger](#team--oheger) |
| Fix | AbstractFileConfiguration.getKeys() now returns an iterator that points to a snapshot of the keys of the configuration. This prevents ConcurrentModificationExceptions during iteration when a reload is performed. Fixes [CONFIGURATION-347](https://issues.apache.org/jira/browse/CONFIGURATION-347). | [oheger](#team--oheger) |
| Fix | ConfigurationUtils.convertToHierarchical() now creates multiple configuration nodes for properties with multiple values. This improves compatibility with queries. Fixes [CONFIGURATION-346](https://issues.apache.org/jira/browse/CONFIGURATION-346). | [oheger](#team--oheger) |
| Fix | PropertiesConfiguration now per default uses the encoding "ISO-8859-1" for loading properties files. Fixes [CONFIGURATION-345](https://issues.apache.org/jira/browse/CONFIGURATION-345). | [oheger](#team--oheger) |
| Fix | CombinedConfiguration could cause a deadlock when it was accessed while concurrently a reload of one of its child configuration happened. This was fixed by reducing synchronization where it is not strictly necessary. Fixes [CONFIGURATION-344](https://issues.apache.org/jira/browse/CONFIGURATION-344). | [oheger](#team--oheger) |
| Fix | The "force reload check" mechanism of CombinedConfiguration now also works with sub configurations created by configurationAt(). Fixes [CONFIGURATION-341](https://issues.apache.org/jira/browse/CONFIGURATION-341). | [oheger](#team--oheger) |
| Fix | When performing interpolation the methods getList() and getStringArray() of CompositeConfiguration did not take the order of child configurations into account. This could lead to wrong interpolated values when the key was contained in multiple child configuration. Interpolation is now always done in the correct order. Fixes [CONFIGURATION-339](https://issues.apache.org/jira/browse/CONFIGURATION-339). | [oheger](#team--oheger) |
| Add | PropertiesConfiguration now also performs interpolation when searching for include files. This means that the name of a file to include can be determined by another property. Fixes [CONFIGURATION-338](https://issues.apache.org/jira/browse/CONFIGURATION-338). Thanks to David Donn. | [oheger](#team--oheger) |
| Add | DefaultConfigurationBuilder now supports defining new configuration providers in the configuration definition file. Fixes [CONFIGURATION-337](https://issues.apache.org/jira/browse/CONFIGURATION-337). Thanks to Ralph Goers. | [oheger](#team--oheger) |
| Add | When converting a flat configuration to a hierarchical one it is now possible to specify the expression engine to be used for this purpose. This may be necessary if the flat configuration contains keys with special characters interpreted by the expression engine. CombinedConfiguration defines the new setConversionExpressionEngine() method. The expression engine passed to this method will be used when converting flat child configurations to hierarchical ones. Fixes [CONFIGURATION-336](https://issues.apache.org/jira/browse/CONFIGURATION-336). | [oheger](#team--oheger) |
| Add | XMLConfiguration now allows disabling the attribute splitting mechanism introduced in the 1.5 release (as part of the fix for CONFIGURATION-268). This may be necessary for correctly processing attributes containing both the list delimiter and the attribute delimiter character. The new property "disableAttributeSplitting" was added for this purpose. Fixes [CONFIGURATION-335](https://issues.apache.org/jira/browse/CONFIGURATION-335). | [oheger](#team--oheger) |
| Fix | Made handling of parent nodes more consistent when setRoot() or setRootNode() of HierarchicalConfiguration are involved. Fixes [CONFIGURATION-334](https://issues.apache.org/jira/browse/CONFIGURATION-334). | [oheger](#team--oheger) |
| Fix | Properties written through a DataConfiguration to a wrapped PropertiesConfiguration got lost when the PropertiesConfiguration was saved. This has been fixed. Fixes [CONFIGURATION-332](https://issues.apache.org/jira/browse/CONFIGURATION-332). | [oheger](#team--oheger) |
| Add | XMLBeanDeclaration now defines a factory method createBeanDeclaration() for creating the declarations for complex nested properties. This method can be overridden by derived classes for injecting custom BeanDeclaration implementations. Fixes [CONFIGURATION-331](https://issues.apache.org/jira/browse/CONFIGURATION-331). | [oheger](#team--oheger) |
| Fix | A bug in XMLConfiguration.addNodes() made it impossible to add attribute nodes using this method. This has been fixed. Fixes [CONFIGURATION-328](https://issues.apache.org/jira/browse/CONFIGURATION-328). | [oheger](#team--oheger) |
| Fix | INIConfiguration misinterpreted variables in the global section with a dot in their name as section names. HierarchicalINIConfiguration fixes this problem. Fixes [CONFIGURATION-327](https://issues.apache.org/jira/browse/CONFIGURATION-327). | [oheger](#team--oheger) |
| Add | INIConfiguration does not support obtaining a subset for the global section. HierarchicalINIConfiguration provides the getSection() method that returns the content of the global section if null is passed in as section name. Fixes [CONFIGURATION-326](https://issues.apache.org/jira/browse/CONFIGURATION-326). | [oheger](#team--oheger) |
| Fix | INIConfiguration does not return the global section in its getSections() method. HierarchicalINIConfiguration fixes this problem. Fixes [CONFIGURATION-325](https://issues.apache.org/jira/browse/CONFIGURATION-325). | [oheger](#team--oheger) |
| Add | HierarchicalINIConfiguration adds support for line continuation. Fixes [CONFIGURATION-324](https://issues.apache.org/jira/browse/CONFIGURATION-324). | [oheger](#team--oheger) |
| Update | INIConfiguration has been deprecated. Its functionality is now available through the new HierarchicalINIConfiguration class. | [oheger](#team--oheger) |
| Add | With HierarchicalINIConfiguration a complete new Configuration implementation for parsing Windows INI files is available. This new class is a full replacement of INIConfiguration and addresses some of its shortcomings. Being derived from HierarchicalConfiguration it offers the enhanced functionality of hierarchical configurations. | [oheger](#team--oheger) |
| Fix | ConfigurationDynaBean now works properly with indexed properties stored internally in the underlying configuration as arrays. Fixes [CONFIGURATION-322](https://issues.apache.org/jira/browse/CONFIGURATION-322). | [ebourg](#team--ebourg) |
| Fix | The iterator returned by HierarchicalConfiguration.getKeys(String prefix) now also contains the prefix if this key is contained in the configuration. Fixes [CONFIGURATION-321](https://issues.apache.org/jira/browse/CONFIGURATION-321). | [oheger](#team--oheger) |
| Fix | XMLPropertyListConfiguration is no longer limited to 32 bits integers. Fixes [CONFIGURATION-320](https://issues.apache.org/jira/browse/CONFIGURATION-320). | [ebourg](#team--ebourg) |
| Fix | When an XMLConfiguration is created using the copy constructor, the name of the root element is now preserved. Fixes [CONFIGURATION-318](https://issues.apache.org/jira/browse/CONFIGURATION-318). | [oheger](#team--oheger) |
| Fix | Changing the text of the root element of an XMLConfiguration had no effect when the configuration was saved. This has been fixed. Fixes [CONFIGURATION-316](https://issues.apache.org/jira/browse/CONFIGURATION-316). | [oheger](#team--oheger) |
| Fix | CombinedConfiguration used to send two EVENT\_COMBINED\_INVALIDATE events for each modified child configuration. Now this event is sent only once after the affected child configuration was updated. Fixes [CONFIGURATION-315](https://issues.apache.org/jira/browse/CONFIGURATION-315). | [oheger](#team--oheger) |
| Fix | XMLConfiguration now supports the xml:space attribute. This attribute can be used to preserve whitespace in the content of XML elements. Fixes [CONFIGURATION-307](https://issues.apache.org/jira/browse/CONFIGURATION-307). | [oheger](#team--oheger) |
| Fix | INIConfiguration now preserves whitespace in quoted values. Fixes [CONFIGURATION-306](https://issues.apache.org/jira/browse/CONFIGURATION-306). | [oheger](#team--oheger) |
| Fix | If a change has been detected by FileChangedReloadingStrategy, the reloadingRequired() method will now return true until reloadingPerformed() has been called. Fixes [CONFIGURATION-302](https://issues.apache.org/jira/browse/CONFIGURATION-302). | [oheger](#team--oheger) |
| Fix | Fixed a NullPointerException that could be thrown under certain circumstances when saving an XMLConfiguration that was created using the constructor that takes a HierarchicalConfiguration. Fixes [CONFIGURATION-301](https://issues.apache.org/jira/browse/CONFIGURATION-301). | [oheger](#team--oheger) |
| Fix | Instantiating an XMLPropertyListConfiguration no longer fails if the DTD is missing from the classpath. Fixes [CONFIGURATION-309](https://issues.apache.org/jira/browse/CONFIGURATION-309). | [ebourg](#team--ebourg) |
| Fix | It's now possible to read a configuration file containing a '#' in its name (requires Java 1.4 or above). Fixes [CONFIGURATION-300](https://issues.apache.org/jira/browse/CONFIGURATION-300). | [ebourg](#team--ebourg) |
| Fix | Fixed the date format for XMLPropertyListConfiguration. Fixes [CONFIGURATION-260](https://issues.apache.org/jira/browse/CONFIGURATION-260). | [ebourg](#team--ebourg) |

<a id="changes--release-1.5-2007-11-24"></a>

## Release 1.5 – 2007-11-24

| Type | Changes | By |
| --- | --- | --- |
| Update | Some of the dependencies in the m2 pom have been updated to be more consistent. Thanks to Jörg Schaible. | [oheger](#team--oheger) |
| Update | The dependency to commons-logging was updated to the current version 1.1. Older versions of commons-logging will still work. Thanks to Jörg Schaible. | [oheger](#team--oheger) |
| Add | A new method interpolatedConfiguration() was added to AbstractConfiguration. This method returns a configuration with the same type and content as the original configuration, however all variables have been resolved. Fixes [CONFIGURATION-273](https://issues.apache.org/jira/browse/CONFIGURATION-273). | [oheger](#team--oheger) |
| Fix | Resolving of variables with the prefix const (constant fields) caused a ClassCastException under certain circumstances if non-String fields were involved. This has been fixed. Fixes [CONFIGURATION-299](https://issues.apache.org/jira/browse/CONFIGURATION-299). | [oheger](#team--oheger) |
| Update | The dependencies to commons-codec and commons-jxpath have been marked as optional. They are not required by the core classes. Thanks to Nicolas De Loof. | [oheger](#team--oheger) |
| Add | There is a new configuration implementation EnvironmentConfiguration, which provides access to (OS) environment variables. On Java >= 1.5 this class can be directly used; on earlier versions a dependency to ant is required. Fixes [CONFIGURATION-284](https://issues.apache.org/jira/browse/CONFIGURATION-284). Thanks to Nicolas De Loof. | [oheger](#team--oheger) |
| Fix | A bug in XMLConfiguration caused that attributes of the root element could not be changed. This has been fixed. Fixes [CONFIGURATION-296](https://issues.apache.org/jira/browse/CONFIGURATION-296). | [oheger](#team--oheger) |
| Add | A new method registerEntityId() was added to XMLConfiguration, which allows to register URLs for entities. A new default implementation of the EntityResolver interface handles these entities automatically. Fixes [CONFIGURATION-290](https://issues.apache.org/jira/browse/CONFIGURATION-290). | [oheger](#team--oheger) |
| Fix | The subset() method of HierarchicalConfiguration now takes the value of the subset's root node into account if it is not ambigous. Fixes [CONFIGURATION-295](https://issues.apache.org/jira/browse/CONFIGURATION-295). | [oheger](#team--oheger) |
| Fix | Nodes added to a XMLConfiguration using the addNodes() method could lose their value when the configuration was saved. This is now fixed. Fixes [CONFIGURATION-294](https://issues.apache.org/jira/browse/CONFIGURATION-294). | [oheger](#team--oheger) |
| Fix | New copy() and append() methods have been added to AbstractConfiguration. They replace the methods with the same names in ConfigurationUtils, which do not handle all features of AbstractConfiguration properly (e.g. list delimiters in property values are incorrectly treated). To avoid such problems, the new methods should be used. Fixes [CONFIGURATION-272](https://issues.apache.org/jira/browse/CONFIGURATION-272). | [oheger](#team--oheger) |
| Fix | The addNodes() method of hierarchical file-based configurations now correctly triggers an auto save. Fixes [CONFIGURATION-291](https://issues.apache.org/jira/browse/CONFIGURATION-291). | [oheger](#team--oheger) |
| Fix | HierarchicalConfiguration.addNodes() now resets the reference property of all nodes to be added. This fixes a problem with XMLConfiguration, which now detects the added nodes as new and treats them correctly when the configuration is saved. Fixes [CONFIGURATION-287](https://issues.apache.org/jira/browse/CONFIGURATION-287). | [oheger](#team--oheger) |
| Add | DefaultConfigurationBuilder will now notify registered error listeners about optional configuration sources that could not be created. Before exceptions thrown by optional configurations were swallowed. Fixes [CONFIGURATION-285](https://issues.apache.org/jira/browse/CONFIGURATION-285). | [oheger](#team--oheger) |
| Fix | ConfigurationUtils.convertToHierarchical() now correctly deals with property values containing escaped list delimiters. This also affects CombinedConfiguration when sub configurations with such property values are contained. Fixes [CONFIGURATION-283](https://issues.apache.org/jira/browse/CONFIGURATION-283). | [oheger](#team--oheger) |
| Fix | AbstractConfiguration.addProperty() now correctly deals with list and array properties if delimiter parsing is disabled. Fixes [CONFIGURATION-275](https://issues.apache.org/jira/browse/CONFIGURATION-275). | [oheger](#team--oheger) |
| Fix | The default expression engine used by HierarchicalConfiguration instances is now lazily initialized. This avoids NullPointerExceptions in certain server environments after a redeploy. Fixes [CONFIGURATION-282](https://issues.apache.org/jira/browse/CONFIGURATION-282). | [oheger](#team--oheger) |
| Fix | Cycles in the JNDI tree no longer cause a stack overflow in JNDIConfiguration. Fixes [CONFIGURATION-281](https://issues.apache.org/jira/browse/CONFIGURATION-281). | [oheger](#team--oheger) |
| Add | The base implementation of clear() in AbstractConfiguration now checks for a potential UnsupportedOperationException when iterating over the existing properties. Fixes [CONFIGURATION-277](https://issues.apache.org/jira/browse/CONFIGURATION-277). | [oheger](#team--oheger) |
| Fix | Using file-based configurations in auto-save mode together with a reloading strategy could cause data loss. This has been fixed. Fixes [CONFIGURATION-280](https://issues.apache.org/jira/browse/CONFIGURATION-280). Thanks to Roman Kurmanowytsch. | [oheger](#team--oheger) |
| Fix | A PropertiesConfiguration that was created from a non existing file lost its content when it was saved. This problem has been solved. Fixes [CONFIGURATION-279](https://issues.apache.org/jira/browse/CONFIGURATION-279). | [oheger](#team--oheger) |
| Add | A new getSource() method was added to CompositeConfiguration and CombinedConfiguration, which returns the child configuration, in which a given property is defined. Fixes [CONFIGURATION-215](https://issues.apache.org/jira/browse/CONFIGURATION-215). | [oheger](#team--oheger) |
| Fix | PropertiesConfiguration now supports escaping the escape character for list delimiters. Fixes [CONFIGURATION-274](https://issues.apache.org/jira/browse/CONFIGURATION-274). | [oheger](#team--oheger) |
| Fix | PropertiesConfiguration no longer escapes the list delimiter on saving if the list delimiter has been disabled. Fixes [CONFIGURATION-269](https://issues.apache.org/jira/browse/CONFIGURATION-269). | [ebourg](#team--ebourg) |
| Fix | List properties and properties containing interpolated variables are now properly saved by INIConfiguration. Fixes [CONFIGURATION-270](https://issues.apache.org/jira/browse/CONFIGURATION-270). | [ebourg](#team--ebourg) |
| Update | When delimiter parsing was disabled for XMLConfiguration, saving and loading the configuration accidently added escape characters to properties containing the list delimiter character. This has been fixed. It is now also possible to escape the escape character itself. Fixes [CONFIGURATION-268](https://issues.apache.org/jira/browse/CONFIGURATION-268). | [oheger](#team--oheger) |
| Update | The return value of FileConfiguration.getFile() is now always consistent with the result of getURL(). Fixes [CONFIGURATION-253](https://issues.apache.org/jira/browse/CONFIGURATION-253). | [oheger](#team--oheger) |
| Update | INIConfiguration uses the platform's specific line separator instead of the Windows line separator. | [ebourg](#team--ebourg) |
| Fix | INIConfiguration flushes the output at the end of a save operation. Fixes [CONFIGURATION-267](https://issues.apache.org/jira/browse/CONFIGURATION-267). | [ebourg](#team--ebourg) |
| Update | For hierarchical file-based configurations the auto-save mechanism is now also triggered if a subnode configuration is changed. In such a case the new event type EVENT\_SUBNODE\_CHANGED will be sent to registered listeners. Fixes [CONFIGURATION-265](https://issues.apache.org/jira/browse/CONFIGURATION-265). | [oheger](#team--oheger) |
| Update | ConfigurationInterpolator now also invokes the default lookup object for variables with a prefix that could not be resolved by their associated lookup object. Fixes [CONFIGURATION-266](https://issues.apache.org/jira/browse/CONFIGURATION-266). Thanks to Tobias Noebel. | [oheger](#team--oheger) |
| Add | A SubnodeConfiguration per default does not see certain changes of its parent configuration (e.g. reloads). With a new boolean parameter of HierarchicalConfiguration's configurationAt() method a mode can be enabled, in which the subnode configuration checks for such changes and reconstructs itself if necessary. Fixes [CONFIGURATION-264](https://issues.apache.org/jira/browse/CONFIGURATION-264). | [oheger](#team--oheger) |
| Fix | byte[] properties are properly saved as data fields in the plist configurations (PropertyListConfiguration and XMLPropertyListConfiguration). | [ebourg](#team--ebourg) |
| Add | DataConfiguration now supports java.net.InetAddress, javax.mail.internet.InternetAddress, and Java 5 enumeration types. Properties are converted to these types using the new generic getters. | [ebourg](#team--ebourg) |
| Fix | The object getters in DataConfiguration with no default value (i.e getURL(key)) now throw a NoSuchElementException if the flag throwExceptionOnMissing is set. | [ebourg](#team--ebourg) |
| Add | Generic get methods have been added to DataConfiguration (get(), getArray() and getList()) | [ebourg](#team--ebourg) |
| Fix | XMLConfiguration used to drop attributes when an element's value was a list. This has been fixed. Fixes [CONFIGURATION-263](https://issues.apache.org/jira/browse/CONFIGURATION-263). | [oheger](#team--oheger) |
| Add | File configurations can now be saved to FTP URLs, or any other URL protocol supporting data output. Fixes [CONFIGURATION-249](https://issues.apache.org/jira/browse/CONFIGURATION-249). | [ebourg](#team--ebourg) |
| Fix | Fixed a potential issue in DatabaseConfiguration where an error on closing a statement would prevent the connection from being closed. Fixes [CONFIGURATION-180](https://issues.apache.org/jira/browse/CONFIGURATION-180). | [ebourg](#team--ebourg) |
| Add | Date objects are now supported in ASCII plist files. Fixes [CONFIGURATION-261](https://issues.apache.org/jira/browse/CONFIGURATION-261). | [ebourg](#team--ebourg) |
| Update | XMLPropertyListConfiguration no longer requires commons-digester and commons-beanutils to work. | [ebourg](#team--ebourg) |
| Update | Fixed INIConfiguration to handle the quoted values and the lines containing a value and a comment. | [ebourg](#team--ebourg) |

<a id="changes--release-1.4-2007-04-08"></a>

## Release 1.4 – 2007-04-08

| Type | Changes | By |
| --- | --- | --- |
| Update | MapConfiguration and the web-based configurations now treat strings that contain an escaped list delimiter correctly: The escape character will be removed, so that for instance "foo\,bar" becomes "foo,bar". Fixes [CONFIGURATION-256](https://issues.apache.org/jira/browse/CONFIGURATION-256). | [oheger](#team--oheger) |
| Update | DatabaseConfiguration now handles list delimiters in property values correctly. Fixes [CONFIGURATION-255](https://issues.apache.org/jira/browse/CONFIGURATION-255). | [oheger](#team--oheger) |
| Update | After cloning a XMLConfiguration there was still a connection to the original configuration. So when the clone was modified and then saved the content of the original configuration was written. This has now been fixed. Fixes [CONFIGURATION-254](https://issues.apache.org/jira/browse/CONFIGURATION-254). Thanks to Carsten Kaiser. | [oheger](#team--oheger) |
| Update | Class loading in BeanHelper is now done using ClassUtils of Commons Lang. | [oheger](#team--oheger) |
| Add | With ManagedReloadingStrategy a new reloading strategy for file-based configurations was added that can be triggered through JMX. Fixes [CONFIGURATION-237](https://issues.apache.org/jira/browse/CONFIGURATION-237). Thanks to Nicolas de Loof. | [oheger](#team--oheger) |
| Update | The dependencies to Commons Lang, Commons Collections, and Commons Digester are updated to use the recent available version. However older versions will still work. | [oheger](#team--oheger) |
| Add | A pom for maven 2 was added. | [oheger](#team--oheger) |
| Update | ConfigurationUtils.getFile() now always checks first whether the passed in file name is absolute. If it is, this file will be returned. This prevents that on Unix under certain circumstances absolute file names are interpreted as relative ones. Fixes [CONFIGURATION-252](https://issues.apache.org/jira/browse/CONFIGURATION-252). | [oheger](#team--oheger) |
| Update | The dependency to xml-apis was changed to the version 1.0.b2. The so far used version 2.0.2 is reported to be bogus. Fixes [CONFIGURATION-251](https://issues.apache.org/jira/browse/CONFIGURATION-251). | [oheger](#team--oheger) |
| Add | In addition to configuration event listeners now so-called configuration error listeners are supported. These listeners are notified about internal errors that had been logged and swallowed by privious versions. The new enableRuntimeExceptions() method of ConfigurationUtils registers a special error listener at the passed in configuration that generates a runtime exception when an error event is received. Fixes [CONFIGURATION-245](https://issues.apache.org/jira/browse/CONFIGURATION-245). | [oheger](#team--oheger) |
| Add | AbstractConfiguration now allows to set an instance specific logger using the setLogger() method. This gives clients more control over a configuration's logging behavior. | [oheger](#team--oheger) |
| Add | SubsetConfiguration and CompositeConfiguration were updated to fully support an instance specific list delimiter. Concerning splitting of string properties that contain a list delimiter character, these classes now behave like a "normal" configuration. Fixes [CONFIGURATION-155](https://issues.apache.org/jira/browse/CONFIGURATION-155). | [oheger](#team--oheger) |
| Add | Variable interpolation features have been improved. A variable can now have the form ${prefix:variableName} where the prefix defines the type of the variable. The standard types sys for system properties and const for constants are supported. Variables without a prefix are treated as references to other configuration properties (which is compatible to earlier versions). Fixes [CONFIGURATION-192](https://issues.apache.org/jira/browse/CONFIGURATION-192). | [oheger](#team--oheger) |
| Update | Commons Configuration now depends on Commons Lang 2.2. Some features of Lang's new text package are used. | [oheger](#team--oheger) |
| Update | The number of dependencies needed for DefaultConfigurationBuilder was reduced by letting some of the default configuration providers resolve their classes per reflection. Fixes [CONFIGURATION-244](https://issues.apache.org/jira/browse/CONFIGURATION-244). | [oheger](#team--oheger) |
| Update | File-based configurations with a reloading strategy did not work well together with CombinedConfiguration because the reloading strategy is only checked when its associated configuration is accessed (which does not happen when only the combined configuration is queried). As a workaround CombinedConfiguration now provides the boolean forceReloadCheck property. If this is set to true, all contained configurations will be triggered when a property is queried. This will cause a reload if necessary. Fixes [CONFIGURATION-240](https://issues.apache.org/jira/browse/CONFIGURATION-240). | [oheger](#team--oheger) |
| Add | Configuration declarations in the configuration definition file for DefaultConfigurationBuilder that are marked as optional now support a new attribute config-forceCreate. If this attribute is set to true and the initialization of the configuration fails, DefaultConfigurationBuilder tries to add an empty configuration of the correct type to the resulting combined configuration. Before this change optional configurations that caused errors were never added to the combined configuration. Fixes [CONFIGURATION-243](https://issues.apache.org/jira/browse/CONFIGURATION-243). | [oheger](#team--oheger) |
| Update | CompositeConfiguration.clearProperty() now generates the correct update events. Fixes [CONFIGURATION-241](https://issues.apache.org/jira/browse/CONFIGURATION-241). | [oheger](#team--oheger) |
| Update | The configuration returned by HierarchicalConfiguration.subset() performed variable interpolation only in the keys that belong to the subset. Now the parent configuration is searched, too, to resolve the value of the referenced property. This is consistent with the way SubnodeConfiguration works. Fixes [CONFIGURATION-242](https://issues.apache.org/jira/browse/CONFIGURATION-242). | [oheger](#team--oheger) |
| Update | DefaultConfigurationBuilder now internally uses the standard expression engine for hierarchical configurations. So the dependency to Commons JXPath is no more needed when this class is used. Note that this change has some impact on existing code that manually sets properties before the combined configuration is created; this code must now be adapted to the changed syntax of property keys. Fixes [CONFIGURATION-234](https://issues.apache.org/jira/browse/CONFIGURATION-234). | [oheger](#team--oheger) |
| Add | HierarchicalConfiguration and some of its sub classes now define a copy constructor. Fixes [CONFIGURATION-236](https://issues.apache.org/jira/browse/CONFIGURATION-236). | [oheger](#team--oheger) |
| Add | A new configuration class for windows ini files was added. Fixes [CONFIGURATION-197](https://issues.apache.org/jira/browse/CONFIGURATION-197). Thanks to Trevor Charles Miller. | [oheger](#team--oheger) |
| Update | For file-based configurations loaded by ConfigurationFactory the load() method was called before all of the properties specified by attributes of the XML element have been initialized. Now load() is called after property initialization. Fixes [CONFIGURATION-229](https://issues.apache.org/jira/browse/CONFIGURATION-229). | [oheger](#team--oheger) |
| Update | Interpolation of non string values did not work when SubsetConfiguration was involved. This has now been fixed. Fixes [CONFIGURATION-235](https://issues.apache.org/jira/browse/CONFIGURATION-235). | [oheger](#team--oheger) |
| Update | The compatibility of ConfigurationDynaBean with other configuration types than those that inherit from BaseConfiguration was improved. Fixes [CONFIGURATION-227](https://issues.apache.org/jira/browse/CONFIGURATION-227). | [oheger](#team--oheger) |
| Update | The getList() method of CompositeConfiguration does now fully support variable interpolation. So it is possible to refer to a variable in one (sub) configuration that is defined in another configuration. Fixes [CONFIGURATION-233](https://issues.apache.org/jira/browse/CONFIGURATION-233). Thanks to Rainer Jung. | [oheger](#team--oheger) |
| Update | XPathExpressionEngine used to create wrong keys for attribute nodes. This caused some operations on XMLConfiguration to fail when such an expression engine was set (e.g. reloading). Now correct keys for attributes are constructed. Fixes [CONFIGURATION-230](https://issues.apache.org/jira/browse/CONFIGURATION-230). | [oheger](#team--oheger) |
| Update | Some of the methods of file-based hierarchical configurations (e.g. subset() or configurationAt()) did not take an eventually set reloading strategy into account. This is now fixed by overriding the internal fetchNodeList() method in AbstractHierarchicalFileConfiguration and letting it always check for a reload. Fixes [CONFIGURATION-228](https://issues.apache.org/jira/browse/CONFIGURATION-228). | [oheger](#team--oheger) |

<a id="changes--release-1.3-2006-09-24"></a>

## Release 1.3 – 2006-09-24

No changes in this release.

<a id="changes--release-1.3-rc2-2006-09-03"></a>

## Release 1.3-rc2 – 2006-09-03

| Type | Changes | By |
| --- | --- | --- |
| Update | AbstractFileConfiguration now overrides addProperty() and setProperty() instead of addPropertyDirect() to implement the auto save feature. This was necessary to properly integrate PropertiesConfigurationLayout. It has also the advantage that an auto save is triggered only once if multi-valued properties are involved (before a save operation was performed for each property value). Fixes [CONFIGURATION-223](https://issues.apache.org/jira/browse/CONFIGURATION-223). Thanks to Gabriele Garuglieri. | [oheger](#team--oheger) |
| Update | The new PropertiesConfigurationLayout class broke the save() operation of PropertiesConfiguration when an instance was newly created and populated in memory. This is fixed now by ensuring that a layout object is immediately created and registered as event listener at the configuration. Fixes [CONFIGURATION-222](https://issues.apache.org/jira/browse/CONFIGURATION-222). Thanks to Gabriele Garuglieri. | [oheger](#team--oheger) |
| Add | ConfigurationFactory now supports variables in its configuration definition files. These variables are resolved using system properties and have the typical ${} syntax. Fixes [CONFIGURATION-221](https://issues.apache.org/jira/browse/CONFIGURATION-221). Thanks to Rainer Jung. | [oheger](#team--oheger) |
| Update | There were still some problems with resolving relative paths when configuration files are loaded from classpath. This fix addresses these issues. Fixes [CONFIGURATION-216](https://issues.apache.org/jira/browse/CONFIGURATION-216). Thanks to Gabriele Garuglieri. | [oheger](#team--oheger) |
| Update | DataConfiguration.getDateArray() used to ignore the format argument. This was fixed. Fixes [CONFIGURATION-220](https://issues.apache.org/jira/browse/CONFIGURATION-220). | [oheger](#team--oheger) |
| Update | PropertiesConfiguration now defines its own clone() method to handle the associated PropertiesConfigurationLayout object correctly. Fixes [CONFIGURATION-219](https://issues.apache.org/jira/browse/CONFIGURATION-219). | [oheger](#team--oheger) |

<a id="changes--release-1.3-rc1-2006-07-30"></a>

## Release 1.3-rc1 – 2006-07-30

| Type | Changes | By |
| --- | --- | --- |
| Update | The dependency to servletapi was updated from version 2.3 to version 2.4, but version 2.3 will still work. Fixes [CONFIGURATION-217](https://issues.apache.org/jira/browse/CONFIGURATION-217). | [oheger](#team--oheger) |
| Add | A new class PropertiesConfigurationLayout was introduced whose task is to preserve the structure (e.g. comments, blank lines) of a file loaded by PropertiesConfiguration. Each PropertiesConfiguration object is now associated with such a layout object. A saved properties file will look very similar to its original. Fixes [CONFIGURATION-104](https://issues.apache.org/jira/browse/CONFIGURATION-104). | [oheger](#team--oheger) |
| Add | clone() methods have been added to BaseConfiguration, AbstractFileConfiguration, MapConfiguration, CompositeConfiguration, and CombinedConfiguration. So the most important Configuration implementations now support cloning. To ConfigurationUtils an utility method cloneConfiguration() was added that allows to conveniently clone a configuration. Fixes [CONFIGURATION-145](https://issues.apache.org/jira/browse/CONFIGURATION-145). | [oheger](#team--oheger) |
| Update | If a configuration file was to be loaded from classpath, the constructor of AbstractFileConfiguration dropped the file's path. The path is now taken into account. Fixes [CONFIGURATION-216](https://issues.apache.org/jira/browse/CONFIGURATION-216). | [oheger](#team--oheger) |
| Update | The getter methods for numeric data types in AbstractConfiguration now support conversions between different Number types, e.g. you can now call getLong(key) when key points to an Integer value. Fixes [CONFIGURATION-214](https://issues.apache.org/jira/browse/CONFIGURATION-214). | [oheger](#team--oheger) |
| Add | The new class DefaultConfigurationBuilder was added as an alternative to ConfigurationFactory. It provides some more features and creates a CombinedConfiguration object | [oheger](#team--oheger) |
| Add | The new class CombinedConfiguration was added as a hierarchical alternative to CompositeConfiguration. | [oheger](#team--oheger) |
| Add | Support for low-level configuration events was added to all classes derived from AbstractConfiguration. The major part of this is handled by the new super class EventSource of AbstractConfiguration. Fixes [CONFIGURATION-143](https://issues.apache.org/jira/browse/CONFIGURATION-143). | [oheger](#team--oheger) |
| Add | A new method convertToHierarchical() was added to ConfigurationUtils, which is able to convert an arbitrary configuration object into a hierarchical configuration. | [oheger](#team--oheger) |
| Update | Loading of file-based configurations no longer throws a NullPointerException in setups where the thread context class loader is not set. Fixes [CONFIGURATION-63](https://issues.apache.org/jira/browse/CONFIGURATION-63). | [oheger](#team--oheger) |
| Update | The dependency to dom4j was removed; it was only used by two test classes, which have been re-written. | [oheger](#team--oheger) |
| Update | XMLConfiguration used to drop the DOCTYPE declaration when saving the configuration. It is now able to extract the DTD's public and system ID and write them back (more complex DOCTYPE declarations are still not supported). With the new methods setSystemID() and setPublicID(), the DOCTYPE declaration can be configured. Fixes [CONFIGURATION-100](https://issues.apache.org/jira/browse/CONFIGURATION-100). | [oheger](#team--oheger) |
| Add | Added two new constructors in CompositeConfiguration accepting a collection of configurations as a parameter. Fixes [CONFIGURATION-178](https://issues.apache.org/jira/browse/CONFIGURATION-178). | [ebourg](#team--ebourg) |
| Add | (Basic) Support for declaring beans in configuration files was added. Some new classes in the beanutils package allow to create instances from these declarations. Fixes [CONFIGURATION-186](https://issues.apache.org/jira/browse/CONFIGURATION-186). | [oheger](#team--oheger) |
| Update | The implementation of the interpolation features have been extracted out off AbstractConfiguration and moved to PropertyConverter. The interpolateHelper() method of AbstractConfiguration is now deprectated and will not be called any more during interpolation. | [oheger](#team--oheger) |
| Add | A new method configurationsAt() was added to HierarchicalConfiguration that provides a convenient way of iterating over complex list-like structures without the need of manually constructing configuration keys with indices. Fixes [CONFIGURATION-182](https://issues.apache.org/jira/browse/CONFIGURATION-182). | [oheger](#team--oheger) |
| Add | A new class SubnodeConfiguration was introduced that wraps a configuration node of a HierarchicalConfiguration. All operations performed on this configuration use this wrapped node as root. The new configurationAt() method of HierarchicalConfiguration returns such a SubnodeConfiguration for a specified sub node. | [oheger](#team--oheger) |
| Add | With XPathExpressionEngine an expression engine for hierarchical configurations is now available that can evaluate XPATH expressions in property keys. This expression engine implementation is based on Commons JXPath, which is now declared as a new dependency (but at runtime it is only needed if the XPathExpressionEngine class is used). Fixes [CONFIGURATION-173](https://issues.apache.org/jira/browse/CONFIGURATION-173). | [oheger](#team--oheger) |
| Add | The code for interpreting property keys was refactored out off HierarchicalConfiguration. Instead this class now supports pluggable expression engines (using the setExpressionEngine() method). So it is possible to plug in different expression languages. A default expression engine is provided that understands the native expression language used by hierarchical configurations in older versions. During the process of this refactoring some methods of HierarchicalConfiguration have been deprecated; they will not be called any more when searching or adding properties. These are the following: createAddPath(), fetchAddNode(), findLastPathNode(), findPropertyNodes(). | [oheger](#team--oheger) |
| Update | A larger refactoring was performed on the inner Node class of HierarchicalConfiguration: A ConfigurationNode interface was extracted for which a default implementation (DefaultConfigurationNode) is provided. HierarchicalConfiguration.Node now extends this default implementation. The new ConfigurationNode interface defines some more methods than the Node class did originally for conveniently dealing with sub nodes and attributes. HierarchicalConfiguration now uses the new type ConfigurationNode whereever possible. Some methods dealing with Node objects have been deprecated and replaced by versions operating on ConfigurationNode objects instead. | [oheger](#team--oheger) |
| Update | All configuration classes derived from AbstractConfiguration now allow to set an instance specific list delimiter. This can be done through the new method setListDelimiter(). As before it is possible to define a default list delimiter, which will be used if no instance specific delimiter is set. This can be done using the new setDefaultListDelimiter() method (the methods get/setDelimiter() have been deprecated). With the new setDelimiterParsingDisabled() method parsing of lists can be disabled at all. Fixes [CONFIGURATION-155](https://issues.apache.org/jira/browse/CONFIGURATION-155). Thanks to Jorge Ferrer. | [oheger](#team--oheger) |

<a id="changes--release-1.2-2005-12-17"></a>

## Release 1.2 – 2005-12-17

No changes in this release.

<a id="changes--release-1.2-rc3-2005-12-07"></a>

## Release 1.2-rc3 – 2005-12-07

| Type | Changes | By |
| --- | --- | --- |
| Update | Commons Configuration now declares a dependency to Xalan. As with Xerces this dependency is only needed for JDK 1.3. It was introduced in a process of making Configuration buildable on a JDK 1.3. Documentation about the build process was also added. | [oheger](#team--oheger) |
| Update | The dependency to Commons Beanutils Collections was unnecessary and thus removed. | [oheger](#team--oheger) |
| Update | Commons Configuration now depends on Commons Digester 1.6 instead of 1.5. (This was done only to pick up the latest available release of digester.) | [oheger](#team--oheger) |

<a id="changes--release-1.2-rc2-2005-11-23"></a>

## Release 1.2-rc2 – 2005-11-23

| Type | Changes | By |
| --- | --- | --- |
| Update | ConfigurationDynaBean now implements the java.util.Map interface (as was stated in the javadocs). This was done by deriving the class from ConfigurationMap. Fixes [CONFIGURATION-2](https://issues.apache.org/jira/browse/CONFIGURATION-2). | [oheger](#team--oheger) |

<a id="changes--release-1.2-rc1-2005-11-11"></a>

## Release 1.2-rc1 – 2005-11-11

| Type | Changes | By |
| --- | --- | --- |
| Update | The reload() method in AbstractFileConfiguration was updated to prevent reentrant invocation, which may be caused by some methods when they are called during a reloading operation. Fixes [CONFIGURATION-33](https://issues.apache.org/jira/browse/CONFIGURATION-33). | [oheger](#team--oheger) |
| Update | AbstractHierarchicalFileConfiguration, a new base class for file based hierarchical configurations, was introduced. XMLConfiguration now extends this class. | [ebourg, oheger](#team--ebourg-oheger) |
| Update | XMLConfiguration now prints the used encoding in the XML declaration of generated files. In earlier versions always the default encoding was written. PropertiesConfiguration now always uses the platform specific line separator when saving files. Fixes [CONFIGURATION-41](https://issues.apache.org/jira/browse/CONFIGURATION-41). Thanks to Kay Doebl. | [oheger](#team--oheger) |
| Update | PropertiesConfiguration now translates properly the escaped unicode characters (like \u1234) used in the property keys. This complies with the specification of java.util.Properties. Fixes [CONFIGURATION-8](https://issues.apache.org/jira/browse/CONFIGURATION-8). | [ebourg](#team--ebourg) |
| Update | ConfigurationConverter.getProperties() now uses the delimiter of the specified configuration to convert the list properties into strings. Fixes [CONFIGURATION-123](https://issues.apache.org/jira/browse/CONFIGURATION-123). | [ebourg](#team--ebourg) |
| Update | The interpolation of variables (${foo}) is now performed in all property getters of AbstractConfiguration and DataConfiguration. As a side effect the Properties object returned by ConfigurationConverter.getProperties() contains only interpolated values. Fixes [CONFIGURATION-123](https://issues.apache.org/jira/browse/CONFIGURATION-123). | [ebourg](#team--ebourg) |
| Update | PropertiesConfiguration now uses the ISO-8859-1 encoding by default instead of the system encoding to comply with the specification of java.util.Properties. Fixes [CONFIGURATION-35](https://issues.apache.org/jira/browse/CONFIGURATION-35). | [ebourg](#team--ebourg) |
| Update | JNDIConfiguration no longer logs an error when attempting to get a property that doesn't exist in the configuration. Fixes [CONFIGURATION-44](https://issues.apache.org/jira/browse/CONFIGURATION-44). | [ebourg](#team--ebourg) |
| Update | Attempting to load a configuration from a directory instead of a file will now throw a ConfigurationException. Fixes [CONFIGURATION-99](https://issues.apache.org/jira/browse/CONFIGURATION-99). | [ebourg](#team--ebourg) |
| Update | If a multi-valued property was involved in an interpolation operation, AbstractConfiguration created a string representation of the list of all values. This was changed to only use the first value, which makes more sense in this context and is consistent with other getters for single valued properties. Fixes [CONFIGURATION-28](https://issues.apache.org/jira/browse/CONFIGURATION-28). | [oheger](#team--oheger) |
| Add | If an include file with a relative path cannot be found in the base path, PropertiesConfiguration now also tries to resolve it based on its own location. Fixes [CONFIGURATION-83](https://issues.apache.org/jira/browse/CONFIGURATION-83). | [oheger](#team--oheger) |
| Update | Fixed MapConfiguration to store the list of values added under a same key instead of the last value added. Fixes [CONFIGURATION-117](https://issues.apache.org/jira/browse/CONFIGURATION-117). Thanks to Steve Bate. | [ebourg](#team--ebourg) |
| Update | Fixed a bug in the handling of relative file names in ConfigurationFactory: In most cases relative file names were not resolved relative to the location of the configuration definition file as stated in the documentation. This behavior was now changed to always be in sync with the documentation. This may have an impact on existing code which uses workarounds for the erroneous resolving mechanism. Fixes [CONFIGURATION-80](https://issues.apache.org/jira/browse/CONFIGURATION-80). | [oheger](#team--oheger) |
| Update | Empty elements or elements whose content consists only of comments or whitespace are now taken into account by XMLConfiguration. They are added to the configuration; their value is an empty string. Fixes [CONFIGURATION-6](https://issues.apache.org/jira/browse/CONFIGURATION-6). | [oheger](#team--oheger) |
| Add | XMLConfiguration now sets a valid system id in the InputSource used for loading files. This enables XML parsers to correctly resolve relative files, e.g. DTDs. | [oheger](#team--oheger) |
| Update | getKeys() in HierarchicalConfiguration now returns the keys in the same order the properties were inserted. Fixes [CONFIGURATION-74](https://issues.apache.org/jira/browse/CONFIGURATION-74). | [ebourg](#team--ebourg) |
| Update | Commons Configuration now depends on Commons Collections 3.1 instead of 3.0 | [ebourg](#team--ebourg) |
| Add | New configurations implementing the "property list" format used in NeXT/OpenStep and its XML variant used in Mac OS X. (PropertyListConfiguration and XMLPropertyListConfiguration). Fixes [CONFIGURATION-195](https://issues.apache.org/jira/browse/CONFIGURATION-195). | [ebourg](#team--ebourg) |
| Update | Resolved some issues with XMLConfiguration and properties containing the delimiter character. These properties are now correctly treated, escaping the delimiter will work, too. Fixes [CONFIGURATION-97](https://issues.apache.org/jira/browse/CONFIGURATION-97). | [oheger](#team--oheger) |
| Add | Added support for XMLPropertiesConfiguration in ConfigurationFactory. A <properties> element will generate a XMLPropertiesConfiguration if the filename ends with ".xml". | [ebourg](#team--ebourg) |
| Add | PropertiesConfiguration now supports escaped key/value separators in the keys (i.e foo\:key = bar). Fixes [CONFIGURATION-184](https://issues.apache.org/jira/browse/CONFIGURATION-184). | [ebourg](#team--ebourg) |
| Add | PropertiesConfiguration now supports all key/value separators supported by java.util.Properties ('=', ':' and white space characters). Fixes [CONFIGURATION-166](https://issues.apache.org/jira/browse/CONFIGURATION-166). | [ebourg](#team--ebourg) |
| Update | Commons Configuration now depends on Commons Lang 2.1 instead of 2.0 | [ebourg](#team--ebourg) |
| Update | Comment lines for PropertiesConfiguration can start with the '!' char (compatibility with java.util.Properties). Fixes [CONFIGURATION-207](https://issues.apache.org/jira/browse/CONFIGURATION-207). | [ebourg](#team--ebourg) |
| Update | Because ConfigurationUtils.copy() does not fully support hierarchical configurations a clone() method was added to HierarchicalConfiguration that can be used instead. Fixes [CONFIGURATION-84](https://issues.apache.org/jira/browse/CONFIGURATION-84). | [oheger](#team--oheger) |
| Add | XMLConfiguration now provides some support for validating XML documents. With the setValidating() method DTD validation can be enabled. It is also possible to set a custom DocumentBuilder allowing a caller to perform enhanced configuration of the XML loading process. Fixes [CONFIGURATION-206](https://issues.apache.org/jira/browse/CONFIGURATION-206). | [oheger](#team--oheger) |
| Update | AbstractFileConfiguration now always sets a valid base path if the configuration file could be located. This allows PropertiesConfiguration to resolve include files even when loaded from class path. Fixes [CONFIGURATION-121](https://issues.apache.org/jira/browse/CONFIGURATION-121). | [oheger](#team--oheger) |
| Update | Updated XMLConfiguration to correctly deal with properties containing dots in their names. Such properties could not be accessed before. Fixes [CONFIGURATION-85](https://issues.apache.org/jira/browse/CONFIGURATION-85). | [oheger](#team--oheger) |
| Update | PropertiesConfiguration's handling of backslash characters at the end of line was incorrect when there was an even number of trailing backslashes. This is now fixed. Fixes [CONFIGURATION-9](https://issues.apache.org/jira/browse/CONFIGURATION-9). | [oheger](#team--oheger) |
| Update | Fixed a problem related to file based configurations that are loaded from a URL which is application/x-www-form-urlencoded: the save() method would store such files at a wrong location. Fixes [CONFIGURATION-130](https://issues.apache.org/jira/browse/CONFIGURATION-130). | [oheger](#team--oheger) |
| Update | Updated FileChangedReloadingStrategy to use the file based configuration's source URL to find the file to watch. Before that it was possible that the strategy checked the wrong file. For configuration files loaded from a jar FileChangedReloadingStrategy now checks the jar file itself for changes. Finally a bug was fixed which caused the strategy to check the watched file's last change date on every invocation of its reloadingRequired() method ignoring its refresh delay. Thanks to Jorge Ferrer. Fixes [CONFIGURATION-50](https://issues.apache.org/jira/browse/CONFIGURATION-50). | [oheger](#team--oheger) |
| Update | Fixed a bug in the collaboration between XMLConfiguration and its reloading strategy: The configuration did not check its reloading strategy, so no reload was performed. Fixes [CONFIGURATION-62](https://issues.apache.org/jira/browse/CONFIGURATION-62). | [oheger](#team--oheger) |
| Update | Disabled auto save mode during PropertiesConfiguration.load(). Prior it was possible that the properties file to be loaded was immideately overwritten. Fixes [CONFIGURATION-119](https://issues.apache.org/jira/browse/CONFIGURATION-119). | [oheger](#team--oheger) |
| Update | Under certain circumstances it was possible that a reloading strategy set for PropertiesConfiguration interferred with the save() method causing the configuration file to be erased. This has now been fixed. Fixes [CONFIGURATION-89](https://issues.apache.org/jira/browse/CONFIGURATION-89). | [oheger](#team--oheger) |
| Update | AbstractFileConfiguration now stores the URL of the config file in the load() methods. This URL is reused by the save() method to ensure that the same file is written. Fixes [CONFIGURATION-94](https://issues.apache.org/jira/browse/CONFIGURATION-94). Thanks to Jamie M. Guillemette. | [oheger](#team--oheger) |
| Update | XMLPropertiesConfiguration no longer depends on Digester to parse the configuration file, it's now implemented with a pure SAX parser. Thanks to Alistair Young. | [ebourg](#team--ebourg) |
| Update | Fixed a bug which causes XMLConfiguration.save to lose attribute values under some circumstances. The clear() method now also ensures that the associated DOM document is always cleared. Fixes [CONFIGURATION-49](https://issues.apache.org/jira/browse/CONFIGURATION-49). Thanks to Mi Zhang. | [oheger](#team--oheger) |
| Update | XMLConfiguration now parse the configuration using the encoding declared in the XML header instead of the OS default encoding. Fixes [CONFIGURATION-13](https://issues.apache.org/jira/browse/CONFIGURATION-13). Thanks to Kunihara Tetsuya. | [ebourg](#team--ebourg) |
| Update | XMLConfiguration now uses the delimiter set by setDelimiter(char). Thanks to Zsolt Koppany. | [ebourg](#team--ebourg) |

<a id="changes--release-1.1-2005-04-02"></a>

## Release 1.1 – 2005-04-02

| Type | Changes | By |
| --- | --- | --- |
| Update | Fixed a ConcurrentModificationException thrown when calling clear() on a SubsetConfiguration applied to a BaseConfiguration. Fixes [CONFIGURATION-134](https://issues.apache.org/jira/browse/CONFIGURATION-134). | [ebourg](#team--ebourg) |
| Update | The resolveContainerStore() method in AbstractConfiguration now works properly with arrays of objects and arrays of primitives. This means it is possible to store an array of value in the configuration and retrieve the first element with the getString(), getInt()... methods. Fixes [CONFIGURATION-81](https://issues.apache.org/jira/browse/CONFIGURATION-81). | [ebourg](#team--ebourg) |

<a id="changes--release-1.1-rc2-2005-03-06"></a>

## Release 1.1-rc2 – 2005-03-06

| Type | Changes | By |
| --- | --- | --- |
| Update | Updated documentation for FileConfiguration's load() methods. Fixed a problem in XMLConfiguration with the output of the save() method when multiple files were loaded. Fixes [CONFIGURATION-118](https://issues.apache.org/jira/browse/CONFIGURATION-118). | [oheger](#team--oheger) |
| Update | Fixed a bug in FileChangedReloadingStrategy preventing the detection of a file change in some cases. | [ebourg](#team--ebourg) |
| Update | Changed getXXXArray() and getXXXList() in DataConfiguration to return an empty array/list for empty values. | [ebourg](#team--ebourg) |
| Update | Fixed getLongArray(), getFloatArray() and getDoubleArray() in DataConfiguration, the values were cast into integers. Fixes [CONFIGURATION-58](https://issues.apache.org/jira/browse/CONFIGURATION-58). | [ebourg](#team--ebourg) |

<a id="changes--release-1.1-rc1-2005-02-13"></a>

## Release 1.1-rc1 – 2005-02-13

| Type | Changes | By |
| --- | --- | --- |
| Add | ConfigurationFactory now always configures digester to use the context classloader. This avoids problems in application server environments, which use their own version of digester. Thanks to Mike Colbert for the patch!. Fixes [CONFIGURATION-88](https://issues.apache.org/jira/browse/CONFIGURATION-88). | [oheger](#team--oheger) |
| Add | Added a new configuration, XMLPropertiesConfiguration, supporting the new XML format for java.util.Properties introduced in Java 1.5. A 1.5 runtime is not required to use this class. Fixes [CONFIGURATION-148](https://issues.apache.org/jira/browse/CONFIGURATION-148). | [ebourg](#team--ebourg) |
| Add | Added a comment header to PropertiesConfiguration. The header is not parsed when the file is loaded yet. Fixes [CONFIGURATION-190](https://issues.apache.org/jira/browse/CONFIGURATION-190). | [ebourg](#team--ebourg) |
| Add | Added the setEncoding(String) and the getEncoding() methods to the FileConfiguration interface to control the encoding of the configuration file. | [ebourg](#team--ebourg) |
| Add | Access to the top level element of the XML document is now provided. For newly created configurations this element can be changed before the document is written. Fixes [CONFIGURATION-210](https://issues.apache.org/jira/browse/CONFIGURATION-210). | [oheger](#team--oheger) |
| Update | Merged the two XML related configuration classes into one new class XMLConfiguration. This new class should provide the best of its ancestors. Fixes [CONFIGURATION-168](https://issues.apache.org/jira/browse/CONFIGURATION-168). | [oheger](#team--oheger) |
| Update | Replaced the PropertyTokenizer inner class in AbstractConfiguration with the split method in PropertyConverter. Also moved the method building an iterator on the elements of a composite value in PropertyConverter as toIterator(). | [ebourg](#team--ebourg) |
| Fix | Some cleanup of the handling of the base path in file based configurations. The base path is now always taken into account. Fixes [CONFIGURATION-15](https://issues.apache.org/jira/browse/CONFIGURATION-15). | [oheger](#team--oheger) |
| Fix | Calling getProperties on a JNDIConfiguration no longer throws an UnsupportedOperationException. | [ebourg](#team--ebourg) |
| Remove | Removed the getPropertyDirect method from AbstractConfiguration, concrete configurations now implement directly the getProperty method from the Configuration interface. | [ebourg](#team--ebourg) |
| Add | Added implementation of a save() method for HierarchicalXMLConfiguration. Fixes [CONFIGURATION-187](https://issues.apache.org/jira/browse/CONFIGURATION-187). | [oheger](#team--oheger) |
| Update | Constructing a file based configuration with a File no longer throws an exception when the file doesn't exist. | [ebourg](#team--ebourg) |
| Add | Saving a configuration now creates the path to the file if it doesn't exist. | [ebourg](#team--ebourg) |
| Update | AbstractFileConfiguration.save(File) no longer fails silently when an error occurs, a ConfigurationException is thrown instead. Fixes [CONFIGURATION-45](https://issues.apache.org/jira/browse/CONFIGURATION-45). | [ebourg](#team--ebourg) |
| Fix | ConfigurationUtils.locate() now checks if the URL based resources exist. This fixes a bug preventing configuration files from being found if the configuration descriptor is in a JAR file (reported by Grant Ingersoll). | [ebourg](#team--ebourg) |
| Fix | Fixed NPE that were caused in the constructors of file based configurations if an invalid file name was specified. Fixes [CONFIGURATION-96](https://issues.apache.org/jira/browse/CONFIGURATION-96). | [oheger](#team--oheger) |
| Add | Added support for optional configuration sources in definition files for ConfigurationFactory. A new optional attribute allows to specify whether a configuration source is mandatory or optional. Fixes [CONFIGURATION-162](https://issues.apache.org/jira/browse/CONFIGURATION-162). | [oheger](#team--oheger) |
| Fix | JNDIConfiguration.getKeys() now returns an empty iterator instead of throwing a ConfigurationRuntimeException when a NamingException occurs. The NamingExceptions are now logged. | [ebourg](#team--ebourg) |
| Fix | DatabaseConfiguration.isEmpty() now returns true if an SQLException occurs. | [ebourg](#team--ebourg) |
| Add | Added two methods copy(Configuration, Configuration) and append(Configuration, Configuration) in ConfigurationUtils to copy properties between configurations. | [ebourg](#team--ebourg) |
| Update | Moved the constructors implementations from PropertiesConfiguration and XMLConfiguration to AbstractFileConfiguration. | [ebourg](#team--ebourg) |
| Remove | Remove deprecated getVector() implementations. | [epugh](#team--epugh) |
| Add | File based configurations can now be automatically reloaded when the underlying file is modified. Fixes [CONFIGURATION-147](https://issues.apache.org/jira/browse/CONFIGURATION-147). | [ebourg](#team--ebourg) |
| Add | Added a clear() method to the Configuration interface to remove all properties. Fixes [CONFIGURATION-156](https://issues.apache.org/jira/browse/CONFIGURATION-156). | [ebourg](#team--ebourg) |
| Add | Added a SystemConfiguration wrapping the system properties. ConfigurationFactory recognizes the corresponding <system/> element. Fixes [CONFIGURATION-208](https://issues.apache.org/jira/browse/CONFIGURATION-208). | [ebourg](#team--ebourg) |
| Add | Added a MapConfiguration to turn any Map into a Configuration. The getConfiguration() methods in ConfigurationConverter now use MapConfiguration, as a result the Configuration returned is always synchronized with the underlying Properties or ExtendedProperties, changes made to the Configuration are available in the Properties, and reciprocally. | [ebourg](#team--ebourg) |
| Add | The "autoSave" feature of XMLConfiguration has been generalized to all file based configurations. Fixes [CONFIGURATION-146](https://issues.apache.org/jira/browse/CONFIGURATION-146). | [ebourg](#team--ebourg) |
| Add | Numeric properties can now be specified in hexadecimal format, for example "number = 0xC5F0". Fixes [CONFIGURATION-191](https://issues.apache.org/jira/browse/CONFIGURATION-191). | [ebourg](#team--ebourg) |
| Fix | Fixed HierarchicalConfiguration.getKeys(String), it returned an empty iterator if the prefix string contained indices. Fixes [CONFIGURATION-36](https://issues.apache.org/jira/browse/CONFIGURATION-36). | [oheger](#team--oheger) |
| Add | Added a DataConfiguration decorator providing getters for all useful types found in a configuration (URL, Locale, Date, Calendar, Color, lists and arrays) | [ebourg](#team--ebourg) |
| Add | Added 5 new configurations to be used in a web environment: AppletConfiguration, ServletConfiguration, ServletContextConfiguration, ServletRequestConfiguration, ServletFilterConfiguration. | [ebourg](#team--ebourg) |

<a id="changes--release-1.0-2004-10-11"></a>

## Release 1.0 – 2004-10-11

| Type | Changes | By |
| --- | --- | --- |
| Fix | The getStringArray() method in CompositeConfiguration now interpolates the strings. Fixes [CONFIGURATION-66](https://issues.apache.org/jira/browse/CONFIGURATION-66). | [ebourg](#team--ebourg) |
| Fix | SubsetConfiguration now shares the "throwExceptionOnMissing" property with its parent. Fixes [CONFIGURATION-23](https://issues.apache.org/jira/browse/CONFIGURATION-23). | [ebourg](#team--ebourg) |
| Fix | Removed "file:" at the beginning of the base path when calling setFile() on a FileConfiguration. This prevented auto saving an XMLConfiguration loaded from a File (issue reported by Mark Roth). | [ebourg](#team--ebourg) |
| Update | All NamingEnumerations in JNDIConfiguraiton are now properly closed (Suggested by Eric Jung). | [ebourg](#team--ebourg) |
| Fix | Properties added to an XMLConfiguration are no longer duplicated in the resulting XML file. Fixes [CONFIGURATION-90](https://issues.apache.org/jira/browse/CONFIGURATION-90). | [ebourg](#team--ebourg) |

<a id="changes--release-1.0-rc2-2004-09-24"></a>

## Release 1.0-rc2 – 2004-09-24

| Type | Changes | By |
| --- | --- | --- |
| Update | Unified the mechanisms for loading and saving file based configurations. PropertiesConfiguration, XMLConfiguration and HierarchicalXMLConfiguration now implement the same FileConfiguration interface. BasePathLoader, BasePathConfiguration, ClassPropertiesConfiguration and BasePropertiesConfiguration have been removed. | [ebourg](#team--ebourg) |
| Fix | Replaced the calls to Boolean.booleanValue(boolean) in AbstractConfiguration and ConfigurationDynaBean to be Java 1.3 compatible. Fixes [CONFIGURATION-22](https://issues.apache.org/jira/browse/CONFIGURATION-22). | [ebourg](#team--ebourg) |
| Fix | Changing the prefix of a JNDIConfiguration will now reset the base context used. Fixes [CONFIGURATION-112](https://issues.apache.org/jira/browse/CONFIGURATION-112). | [ebourg](#team--ebourg) |
| Add | The context used by JNDIConfiguration can be specified in its constructor or through the setContext() method. The context can be accessed with the getContext() method which is now public. Thanks to Eric Jung. | [ebourg](#team--ebourg) |
| Add | Make the behavior on missing properties for the get methods that return objects configurable. A property throwExceptionOnMissing can be set and then the getters throw an NoSuchElementException. The old default behavior of returning a null value has been restored. | [henning](#team--henning) |
| Add | Allow configurations extending AbstractConfiguration to change the delimiter used from "," to something else. Fixes [CONFIGURATION-151](https://issues.apache.org/jira/browse/CONFIGURATION-151). | [epugh](#team--epugh) |
| Fix | PropertiesConfiguration.save() method has issues with preserving the filename | [epugh](#team--epugh) |
| Fix | Test cases for HierarchicalConfigurationXMLReader stores comments as text nodes. Fixes [CONFIGURATION-132](https://issues.apache.org/jira/browse/CONFIGURATION-132). Thanks to Mark Woodman. | [epugh](#team--epugh) |
| Fix | Clarify for ConfigurationDynaBean that the get method should throw an illegalArgumentException if there is no property specified. Fixes [CONFIGURATION-183](https://issues.apache.org/jira/browse/CONFIGURATION-183). Thanks to Ricardo Gladwell. | [epugh](#team--epugh) |
| Fix | Fixed a ClassCastException when adding a non String property to an XMLConfiguration. Fixes [CONFIGURATION-25](https://issues.apache.org/jira/browse/CONFIGURATION-25). | [ebourg](#team--ebourg) |
| Fix | Fixed the handling of attribute properties by HierarchicalConfigurationConverter. Fixes [CONFIGURATION-138](https://issues.apache.org/jira/browse/CONFIGURATION-138). Thanks to Oliver Heger. | [ebourg](#team--ebourg) |
| Fix | Fixed a ClassCastException thrown on adding a non string property in a DatabaseConfiguration. Fixes [CONFIGURATION-125](https://issues.apache.org/jira/browse/CONFIGURATION-125). | [ebourg](#team--ebourg) |
| Add | Bring back the getVector() methods in the Configuration interface. These methods are needed for "drop-on" replacement of the various pre-1.0 commons-configuration snapshots and are already deprecated. These methods will be removed for 1.1. | [henning](#team--henning) |

<a id="changes--release-1.0-rc1-2004-08-14"></a>

## Release 1.0-rc1 – 2004-08-14

| Type | Changes | By |
| --- | --- | --- |
| Add | HierarchicalConfigurationXMLReader stores comments as text nodes. Fixes [CONFIGURATION-132](https://issues.apache.org/jira/browse/CONFIGURATION-132). Thanks to Oliver Heger. | [epugh](#team--epugh) |
| Add | project.xml contains bad dependencies. Fixes [CONFIGURATION-122](https://issues.apache.org/jira/browse/CONFIGURATION-122). Thanks to Ricardo Gladwell. | [epugh](#team--epugh) |
| Add | clearXmlProperty doesn't remove list properties completely. Fixes [CONFIGURATION-64](https://issues.apache.org/jira/browse/CONFIGURATION-64). Thanks to Brent Worden. | [epugh](#team--epugh) |
| Add | new ConfigurationDynaBean. Fixes [CONFIGURATION-183](https://issues.apache.org/jira/browse/CONFIGURATION-183). Thanks to Ricardo Gladwell. | [epugh](#team--epugh) |
| Add | new ConfigurationMap and ConfigurationSet. Fixes [CONFIGURATION-185](https://issues.apache.org/jira/browse/CONFIGURATION-185). Thanks to Ricardo Gladwell. | [epugh](#team--epugh) |
| Fix | Problem adding property XMLConfiguration. Fixes [CONFIGURATION-91](https://issues.apache.org/jira/browse/CONFIGURATION-91). Thanks to Ricardo Gladwell. | [epugh](#team--epugh) |
| Remove | ConfigurationXMLDocument removed until post 1.0. | [epugh](#team--epugh) |
| Fix | DatabaseConfiguration doesn't support List properties. Fixes [CONFIGURATION-18](https://issues.apache.org/jira/browse/CONFIGURATION-18). | [epugh](#team--epugh) |
| Fix | Fixed a bug related to XMLConfiguration. Can't add a new property as an attribute in XMLConfiguration. Fixes [CONFIGURATION-137](https://issues.apache.org/jira/browse/CONFIGURATION-137). | [ebourg](#team--ebourg) |
| Fix | Fixed a bug related to XMLConfiguration. XMLConfiguration doesn't support attribute names with a dot. Fixes [CONFIGURATION-116](https://issues.apache.org/jira/browse/CONFIGURATION-116). | [ebourg](#team--ebourg) |
| Fix | Fixed a bug related to XMLConfiguration. XMLConfiguration doesn't ignore comments. Fixes [CONFIGURATION-4](https://issues.apache.org/jira/browse/CONFIGURATION-4). | [ebourg](#team--ebourg) |
| Fix | Fixed a bug related to XMLConfiguration. XMLConfiguration.save() doesn't escape reserved characters. Fixes [CONFIGURATION-32](https://issues.apache.org/jira/browse/CONFIGURATION-32). | [ebourg](#team--ebourg) |
| Add | Added save methods in XMLConfiguration similar to PropertiesConfiguration to save the configuration to another file. Fixes [CONFIGURATION-114](https://issues.apache.org/jira/browse/CONFIGURATION-114). | [ebourg](#team--ebourg) |
| Update | Removed the DOM4J implementations in favor of the DOM ones. DOMConfiguration has been renamed to XMLConfiguration, and HierarchicalDOMConfiguration to HierarchicalXMLConfiguration. The elements parsed by the ConfigurationFactory have been changed accordingly. | [ebourg](#team--ebourg) |
| Add | Added a save() method to PropertiesConfiguration and save(Writer out), save(OutputStream out), save(OutputStream out, String encoding) to BasePropertiesConfiguration. | [ebourg](#team--ebourg) |
| Fix | List values are now properly stored as comma separated values in the Properties object returned by ConfigurationConverter.getProperties(). Fixes [CONFIGURATION-98](https://issues.apache.org/jira/browse/CONFIGURATION-98). | [ebourg](#team--ebourg) |
| Update | Introduced a ConversionException thrown when the value of a property is not compatible the type requested. It replaces the ClassCastException and the NumberFormatException thrown previously. | [ebourg](#team--ebourg) |
| Fix | Tokens like ${ref} in a PropertyConfiguration are now properly saved. Fixes [CONFIGURATION-174](https://issues.apache.org/jira/browse/CONFIGURATION-174). | [ebourg](#team--ebourg) |
| Fix | The getList() method of a CompositeConfiguration now returns the list composed of the elements in the first matching configuration and the additional elements found in the in memory configuration. Fixes [CONFIGURATION-127](https://issues.apache.org/jira/browse/CONFIGURATION-127). | [ebourg](#team--ebourg) |
| Fix | SubsetConfiguration returns a List on getList(). AbstractConfiguration wouldn't properly deal with a List, only with a Container for getList()! Thanks to jschaible for the unit test. | [epugh](#team--epugh) |
| Add | Direct support of XML via DOM. New classes DOMConfiguration and HierarchicalDOMConfiguration. | [jschaible](#team--jschaible) |
| Update | Update build to not include test configuration files in resulting jar. | [jschaible](#team--jschaible) |
| Update | Refactored JNDIConfiguration to use AbstractConfiguration. | [ebourg](#team--ebourg) |
| Update | Fixed invalid subsets by refactoring out the subset logic into a SubsetConfiguration. Fixes [CONFIGURATION-76](https://issues.apache.org/jira/browse/CONFIGURATION-76). | [ebourg](#team--ebourg) |
| Fix | Reapply the ConfigurationXMLDocument that went missing during migration out of sandbox. | [oheger](#team--oheger) |
| Update | Apply ASL 2.0 license. Thanks to Jeff Painter for scripting the conversion! | [epugh](#team--epugh) |
| Add | Changed CompositeConfiguration to extend from AbstractConfiuration. This means that the behavior of CompositeConfiguration is much similar to others like PropertiesConfiguration in handling of missing keys, interpolation, etc.. Previously CompositeConfiguration had quite a few differences. | [epugh](#team--epugh) |
| Update | Removed "defaults" from BaseConfiguration. Defaults are now done via using a CompositeConfiguration, either directly or via a ConfigurationFactory. if you want to save changes made to a Configuration, then you use a CompositeConfiguration and get back the inMemoryConfiguration that has the delta of changes. Added a bit of documentation on this. | [epugh](#team--epugh) |
| Update | Enhancement: Configuration Comparator. Fixes [CONFIGURATION-154](https://issues.apache.org/jira/browse/CONFIGURATION-154). | [epugh](#team--epugh) |
| Update | BaseConfiguration: containsKey ignores default properties. I have changed it so that now the defaults are paid attention to. Fixes [CONFIGURATION-54](https://issues.apache.org/jira/browse/CONFIGURATION-54). | [epugh](#team--epugh) |
| Add | The Configuration interface now supports BigDecimal and BigInteger numbers. | [ebourg](#team--ebourg) |
| Add | ConfigurationException is now thrown by public methods instead of Exception or IOException or whatnot. | [epugh](#team--epugh) |
| Add | For configuration based on properties files, allow characters like \n etc to be escaped and unescaped. | [ebourg](#team--ebourg) |
| Add | New DatabaseConfiguration that uses a database to store the properties. It supports 2 table structures: one table per configuration (2 colums key/value), one table for multiple configurations (2 columns key/value + 1 column for the name of the configuration). | [ebourg](#team--ebourg) |
| Add | ConfigurationFactory now supports the hierarchicalDom4j element in configuration definition file | [oheger](#team--oheger) |
| Update | Change all Vector objects to List objects. | [ebourg](#team--ebourg) |
| Add | ConfigurationFactory now supports two types of properties files, additional and override. Additional properties add each other together. Override override each other. This allows you to have a single property that is either aggregated from a number of sources, or have a property that is overridden according to a specific order of sources. | [oheger](#team--oheger) |
| Update | AbstractConfiguration addProperty now delegates to an abstract addPropertyDirect implemented by BaseConfiguration. | [oheger](#team--oheger) |
| Update | Changed getString() method to throw a NoSuchElementException instead of "" if the configuration property doesn't exist. | [kshaposhnikov](#team--kshaposhnikov) |
| Add | Added AbstractConfiguration to make it easier to create subclasses by only having to implement the methods required. | [kshaposhnikov](#team--kshaposhnikov) |
| Fix | ClassPropertiesConfiguration Additions: Use the classloader of class that is provided by the constructor. Add a constructor that indicates whether to use relative or absolute. Change getPropertyStream to utilize the relative or absolute flag. Add a test case that checks that absolute paths work. | [bdunbar](#team--bdunbar) |
| Fix | JNDIConfiguration.getKeys() Addition: The JNDIConfiguration.getKeys() method was returning an unsupported operation error. However, this is an important method to have supported. | [epugh](#team--epugh) |
| Fix | CompositeConfiguration.getKeys() Fix The CompositeConfiguration.getKeys() method was returning an unordered list of configuration values. However, many apps expect the order that keys are returned to be the order they are added into the properties file. | [epugh](#team--epugh) |

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/scm.html -->

<!-- page_index: 3 -->

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
$ git clone --branch rel/commons-configuration-2.13.0 https://gitbox.apache.org/repos/asf/commons-configuration.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch rel/commons-configuration-2.13.0 https://gitbox.apache.org/repos/asf/commons-configuration.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/security.html -->

<!-- page_index: 4 -->

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

## CVE-2022-33980 prior to 2.8.0, RCE when applied to untrusted input

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

## CVE-2024-29131 prior to 2.10.1, Out-of-bounds Write vulnerability

On 2024-03-20, the Apache Commons Configuration team disclosed [CVE-2024-29131](https://www.cve.org/CVERecord?id=CVE-2024-29131).

This Out-of-bounds Write vulnerability in Apache Commons Configuration affects Apache Commons Configuration: from 2.0 before 2.10.1.
Users can see this as a `StackOverflowError` when adding a property in `AbstractListDelimiterHandler.flattenIterator()`.
Users are recommended to upgrade to version 2.10.1, which fixes the issue.
The details are in [CONFIGURATION-840](https://issues.apache.org/jira/browse/CONFIGURATION-840).

<a id="security--cve-2024-29133-prior-to-2.10.1-out-of-bounds-write-vulnerability"></a>

## CVE-2024-29133 prior to 2.10.1, Out-of-bounds Write vulnerability

On 2024-03-20, the Apache Commons Configuration team disclosed [CVE-2024-29133](https://www.cve.org/CVERecord?id=CVE-2024-29133).

This Out-of-bounds Write vulnerability in Apache Commons Configuration affects Apache Commons Configuration: from 2.0 before 2.10.1.
Users can see this as a `StackOverflowError` calling `ListDelimiterHandler.flatten(Object, int)` with a cyclical object tree.
Users are recommended to upgrade to version 2.10.1, which fixes the issue.
The details are in [CONFIGURATION-841](https://issues.apache.org/jira/browse/CONFIGURATION-840).

<a id="security--safe-deserialization"></a>

# Safe Deserialization

For information about safe deserialization, please see [Safe Deserialization](https://commons.apache.org/io/description.html#Safe_Deserialization).

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/building.html -->

<!-- page_index: 5 -->

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

<!-- page_index: 6 -->

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

<!-- page_index: 7 -->

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
sections [Using Configuration](https://commons.apache.org/proper/commons-configuration/userguide/overview.html#Using_Configuration)
and [Basic
features and AbstractConfiguration](https://commons.apache.org/proper/commons-configuration/userguide/howto_basicfeatures.html#Basic_features_and_AbstractConfiguration).

What has changed is the default implementation of
[List handling](https://commons.apache.org/proper/commons-configuration/userguide/howto_basicfeatures.html#List_handling) in
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
Configurations](https://commons.apache.org/proper/commons-configuration/userguide/howto_hierarchical.html#Hierarchical_Configurations).
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
[Internal Representation](https://commons.apache.org/proper/commons-configuration/userguide/howto_hierarchical.html#Internal_Representation)
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
[configuration builders](https://commons.apache.org/proper/commons-configuration/userguide/howto_builders.html). The basic idea
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
[Making it easier](https://commons.apache.org/proper/commons-configuration/userguide/howto_filebased.html#Making_it_easier)
which describes some useful short cuts. It is also possible to define
default values for initialization parameters. This allows simplifying of
builder configurations and can establish application-global standard
settings for configuration objects. This mechanism is described in
[Default
Initialization Parameters](https://commons.apache.org/proper/commons-configuration/userguide/howto_builders.html#Default_Initialization_Parameters).

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
Sources](https://commons.apache.org/proper/commons-configuration/userguide/howto_reloading.html) of the user's guide. In a nutshell, [configuration builders](https://commons.apache.org/proper/commons-configuration/userguide/howto_builders.html) play an important
role here. There are builder implementations available which can be
configured to monitor external configuration sources in a pretty generic
way. When a change is detected, the builder resets its managed configuration
so that the next time it is accessed a new instance is created. In addition, an event can be generated notifying the application that new configuration
information might be available. The whole mechanism can be setup to
perform reloading checks periodically and automatically in a background
thread.

The `FileChangedReloadingStrategy` class from version 1.0
no longer exists. It is replaced by the new, more powerful reloading
mechanisms. The mentioned chapter about [reloading](https://commons.apache.org/proper/commons-configuration/userguide/howto_reloading.html)
describes in detail how a reloading-aware configuration builder can be
setup and fine-tuned to an application's needs.

<a id="userguide-upgradeto2_0--combining-configuration-sources"></a>

## Combining Configuration Sources

In *Commons Configuration* 1.x, there were two options for
creating a
[combined
configuration](https://commons.apache.org/proper/commons-configuration/userguide/howto_combinedbuilder.html#Combining_Configuration_Sources) out of multiple sources:

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
definition file reference](https://commons.apache.org/proper/commons-configuration/userguide/howto_combinedbuilder.html#Configuration_definition_file_reference).

A problem when migrating from `DefaultConfigurationBuilder` to
`CombinedConfigurationBuilder` is that those definition files
can contain [bean definitions](https://commons.apache.org/proper/commons-configuration/userguide/howto_beans.html), i.e. references
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
[Combining Configuration Sources](https://commons.apache.org/proper/commons-configuration/userguide/howto_combinedbuilder.html)
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
Concurrent Access](https://commons.apache.org/proper/commons-configuration/userguide/howto_concurrency.html) for a full description of this complex topic.

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

<!-- page_index: 8 -->

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
[user guide](https://commons.apache.org/proper/commons-configuration/userguide/howto_basicfeatures.html#Default_interpolation_lookups), this can be done either
programmatically or through a system property. If the behavior of previous versions must be maintained exactly
without changes to the code, then the following system property can be used:

```

org.apache.commons.configuration2.interpol.ConfigurationInterpolator.defaultPrefixLookups=BASE64_DECODER,BASE64_ENCODER,CONST,DATE,DNS,ENVIRONMENT,FILE,JAVA,LOCAL_HOST,PROPERTIES,RESOURCE_BUNDLE,SCRIPT,SYSTEM_PROPERTIES,URL,URL_DECODER,URL_ENCODER,XML
```

If the disabled lookups listed above are not used by the target application, then no changes are required.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/project-info.html -->

<!-- page_index: 9 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Commons Configuration software library provides a generic configuration interface that enables an application to read configuration data from various sources and requires Java 8. |
| [Summary](https://commons.apache.org/proper/commons-configuration/summary.html) | This document lists other related information of this project |
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

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/team.html -->

<!-- page_index: 10 -->

# Project Team

<table class="layout-table">
<tr>
<td>
</td>
<td>
<section><a id="Project_Team"></a>
DOC2MDPLACEHOLDERTOKEN0END<h1>Project Team</h1>
<p>A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.</p>
<p>The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.</p><section><a id="Members"></a>
DOC2MDPLACEHOLDERTOKEN1END<h2>Members</h2>
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
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="dlr"></a>dlr</td>
<td>Daniel Rall</td>
<td><a href="mailto:dlr@finemaltcoding.com">dlr@finemaltcoding.com</a></td>
<td>-</td>
<td>CollabNet, Inc.</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="jvanzyl"></a>jvanzyl</td>
<td>Jason van Zyl</td>
<td><a href="mailto:jason@zenplex.com">jason@zenplex.com</a></td>
<td>-</td>
<td>Zenplex</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="mpoeschl"></a>mpoeschl</td>
<td>Martin Poeschl</td>
<td><a href="mailto:mpoeschl@marmot.at">mpoeschl@marmot.at</a></td>
<td>-</td>
<td>tucana.at</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="dion"></a>dion</td>
<td>dIon Gillard</td>
<td><a href="mailto:dion@multitask.com.au">dion@multitask.com.au</a></td>
<td>-</td>
<td>Multitask Consulting</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/126d93a0374e9fa5faa40527b2faa177_7fdd665d93e3d4ea.jpg"/></figure></td>
<td><a id="henning"></a>henning</td>
<td>Henning P. Schmiedehausen</td>
<td><a href="mailto:hps@intermeta.de">hps@intermeta.de</a></td>
<td>-</td>
<td>INTERMETA - Gesellschaft fuer Mehrwertdienste mbH</td>
<td>-</td>
<td>Java Developer</td>
<td>2</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="epugh"></a>epugh</td>
<td>Eric Pugh</td>
<td><a href="mailto:epugh@upstate.com">epugh@upstate.com</a></td>
<td>-</td>
<td>upstate.com</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="bdunbar"></a>bdunbar</td>
<td>Brian E. Dunbar</td>
<td><a href="mailto:bdunbar@dunbarconsulting.org">bdunbar@dunbarconsulting.org</a></td>
<td>-</td>
<td>dunbarconsulting.org</td>
<td>-</td>
<td>Java Developer</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/8304c64641badd4218a89a5f97d2ae86_77b1b0d2c138f6ee.jpg"/></figure></td>
<td><a id="ebourg"></a>ebourg</td>
<td>Emmanuel Bourg</td>
<td><a href="mailto:ebourg@apache.org">ebourg@apache.org</a></td>
<td>-</td>
<td>Ariane Software</td>
<td>-</td>
<td>Java Developer</td>
<td>+1</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="oheger"></a>oheger</td>
<td>Oliver Heger</td>
<td><a href="mailto:oheger@apache.org">oheger@apache.org</a></td>
<td>-</td>
<td>Bosch Software Innovations</td>
<td>-</td>
<td>Java Developer</td>
<td>+1</td></tr>
<tr>
<td><figure><img src="assets/images/b57f757efea9e04ad3a5cb489499ec01_f6a52f7a08b191a0.jpg"/></figure></td>
<td><a id="joehni"></a>joehni</td>
<td>Jörg Schaible</td>
<td><a href="mailto:joerg.schaible@gmx.de">joerg.schaible@gmx.de</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>+1</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="rgoers"></a>rgoers</td>
<td>Ralph Goers</td>
<td><a href="mailto:rgoers@apache.org">rgoers@apache.org</a></td>
<td>-</td>
<td>Intuit</td>
<td>-</td>
<td>Java Developer</td>
<td>-8</td></tr>
<tr>
<td><figure><img src="https://people.apache.org/~ggregory/img/garydgregory80.png"/></figure></td>
<td><a id="ggregory"></a>ggregory</td>
<td>Gary Gregory</td>
<td><a href="mailto:ggregory at apache.org">ggregory at apache.org</a></td>
<td><a href="https://www.garygregory.com">https://www.garygregory.com</a></td>
<td>The Apache Software Foundation</td>
<td><a href="https://www.apache.org/">https://www.apache.org/</a></td>
<td>PMC Member</td>
<td>America/New_York</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td><a id="claudenw"></a>claudenw</td>
<td>Claude Warren</td>
<td><a href="mailto:claude@apache.org">claude@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>0</td></tr>
<tr>
<td><figure><img src="assets/images/a010ac0916b6b9b10883e9359cfcd7f9_51479c81d891bafa.jpg"/></figure></td>
<td><a id="chtompki"></a>chtompki</td>
<td>Rob Tompkins</td>
<td><a href="mailto:chtompki@apache.org">chtompki@apache.org</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Java Developer</td>
<td>-4</td></tr></table></section><section><a id="Contributors"></a>
DOC2MDPLACEHOLDERTOKEN2END<h2>Contributors</h2>
<p>The following additional people have contributed to this project through the way of suggestions, patches or documentation.</p>
<table>
<tr>
<th>Image</th>
<th>Name</th>
<th>Email</th>
<th>Organization</th>
<th>Organization URL</th>
<th>Roles</th>
<th>Time Zone</th></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>Konstantin Shaposhnikov</td>
<td><a href="mailto:ksh@scand.com">ksh@scand.com</a></td>
<td>scand.com</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/6d77b357b99fe3b791235b1f7ebac068_398ea4788493cfa6.jpg"/></figure></td>
<td>Jamie M. Guillemette</td>
<td><a href="mailto:JMGuillemette@gmail.com">JMGuillemette@gmail.com</a></td>
<td>TD Bank</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>Jorge Ferrer</td>
<td><a href="mailto:jorge.ferrer@gmail.com">jorge.ferrer@gmail.com</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>Gabriele Garuglieri</td>
<td><a href="mailto:gabriele.garuglieri@infoblu.it">gabriele.garuglieri@infoblu.it</a></td>
<td>Infoblu S.p.A</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/2983ff4b1cfdd190e9a42e1e6c6e7327_bf66c8e0ddba0c1f.jpg"/></figure></td>
<td>Nicolas De Loof</td>
<td><a href="mailto:nicolas.deloof@gmail.com">nicolas.deloof@gmail.com</a></td>
<td>Cap Gemini</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>Oliver Kopp</td>
<td><a href="mailto:koppdev@gmail.com">koppdev@gmail.com</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/6da8b0926ce146bee20982ffcb57f11b_dc14bc8575be8ec6.jpg"/></figure></td>
<td>Dennis Kieselhorst</td>
<td><a href="mailto:deki@apache.org">deki@apache.org</a></td>
<td>IRIAN Deutschland</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/4b10f95b68fb001e4880b477a41bd5a1_51698ce365874a55.jpg"/></figure></td>
<td>Raviteja Lokineni</td>
<td><a href="mailto:raviteja.lokineni@gmail.com">raviteja.lokineni@gmail.com</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>Vincent Maurin</td>
<td><a href="mailto:vincent.maurin.fr@gmail.com">vincent.maurin.fr@gmail.com</a></td>
<td>glispa GmbH</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>The Alchemist</td>
<td><a href="mailto:kap4020@gmail.com">kap4020@gmail.com</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr>
<tr>
<td><figure><img src="assets/images/0db3f413e4b5f2f1d2f16852ce719089_fd4c201bbe643d3d.jpg"/></figure></td>
<td>Pascal Essiembre</td>
<td><a href="mailto:pascal.essiembre@norconex.com">pascal.essiembre@norconex.com</a></td>
<td>Norconex Inc.</td>
<td><a href="https://www.norconex.com">https://www.norconex.com</a></td>
<td>developer</td>
<td>-4</td></tr>
<tr>
<td><figure><img src="assets/images/00000000000000000000000000000000_8f8c7367165cd615.jpg"/></figure></td>
<td>Patrick Schmidt</td>
<td><a href="mailto:patrick.schmidt@codecamp.de">patrick.schmidt@codecamp.de</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td></tr></table></section></section>
</td>
</tr>
</table>

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

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/project-reports.html -->

<!-- page_index: 12 -->

<a id="project-reports--generated-reports"></a>

# Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](https://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [Changes](#changes) | Changes report on releases of this project. |
| [JIRA Report](#jira-changes) | Report on Issues from the JIRA Issue Tracking System. |
| [Javadoc](https://commons.apache.org/proper/commons-configuration/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-configuration/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-configuration/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire](#surefire) | Report on the test results of the project. |
| [RAT Report](#rat-report) | Report on compliance to license related source code policies |
| [japicmp](#japicmp) | Comparing source compatibility of commons-configuration2-2.14.0.jar against commons-configuration2-2.13.0.jar |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [SpotBugs](#spotbugs) | Generates a source code report with the SpotBugs Library. |

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/jira-changes.html -->

<!-- page_index: 13 -->

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
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-807">CONFIGURATION-807</a></td>
<td>-</td>
<td>Method addProperty don't work if the property not exist in the file</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-708">CONFIGURATION-708</a></td>
<td>Build</td>
<td>Not able to build the source code</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-651">CONFIGURATION-651</a></td>
<td>-</td>
<td>Configuration 2 does not declare optional imports in OSGI correctly</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-622">CONFIGURATION-622</a></td>
<td>Format</td>
<td>Writing INI file, keys with . become ..</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-593">CONFIGURATION-593</a></td>
<td>-</td>
<td>Internal Server Error in Download area</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-509">CONFIGURATION-509</a></td>
<td>Build</td>
<td>Maven central maven-metadata.xml contains only a small subset of available versions</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-491">CONFIGURATION-491</a></td>
<td>-</td>
<td>XMLConfiguration.XMLBuilderVisitor.listDelimiter initial value is always overridden</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-138">CONFIGURATION-138</a></td>
<td>-</td>
<td>[configuration] HierarchicalConfigurationConverter has problems with attributes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-137">CONFIGURATION-137</a></td>
<td>-</td>
<td>[configuration] Can't add a new property as an attribute in XMLConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-135">CONFIGURATION-135</a></td>
<td>-</td>
<td>[configuration] Invalid resource names in XMLConfiguration generate a NPE</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-134">CONFIGURATION-134</a></td>
<td>-</td>
<td>[configuration] SubsetConfiguration.clear() throws a ConcurrentModificationException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-133">CONFIGURATION-133</a></td>
<td>-</td>
<td>[configuration][patch] Replace AbstractConfiguration.testBoolean with BooleanUtils.toBooleanObject</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-132">CONFIGURATION-132</a></td>
<td>-</td>
<td>[configuration] HierarchicalConfigurationXMLReader stores comments as text nodes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-130">CONFIGURATION-130</a></td>
<td>-</td>
<td>[configuration] FileConfiguration - Save problem when embedded spaces are in the path</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-129">CONFIGURATION-129</a></td>
<td>-</td>
<td>[configuration] Comma separation in Strings</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-127">CONFIGURATION-127</a></td>
<td>-</td>
<td>[configuration] Lists in a CompositeConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-125">CONFIGURATION-125</a></td>
<td>-</td>
<td>[configuration] setting non-string values in DatabaseConfiguration always throws ClassCastException</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-123">CONFIGURATION-123</a></td>
<td>-</td>
<td>[configuration] ConfigurationConverter.getProperties() and interpolate behaviour inconsequent with getList()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-122">CONFIGURATION-122</a></td>
<td>-</td>
<td>[configuration] project.xml contains bad dependencies</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-121">CONFIGURATION-121</a></td>
<td>-</td>
<td>[configuration] Included properties w/ relative path fails in v1.1</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-120">CONFIGURATION-120</a></td>
<td>-</td>
<td>[configuration] Missing classes after move to commons proper</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-119">CONFIGURATION-119</a></td>
<td>-</td>
<td>[configuration] ConfigurationFactory auto save overwrites properties file</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-118">CONFIGURATION-118</a></td>
<td>-</td>
<td>[configuration] Loading a configuration twice creates duplicate properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-117">CONFIGURATION-117</a></td>
<td>-</td>
<td>[configuration] MapConfiguration doesn't support multiple-valued properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-116">CONFIGURATION-116</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration doesn't support attribute names with a dot</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-115">CONFIGURATION-115</a></td>
<td>-</td>
<td>[configuration]Documentation updates</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-114">CONFIGURATION-114</a></td>
<td>-</td>
<td>[configuration] Saving XML configurations to another file</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-112">CONFIGURATION-112</a></td>
<td>-</td>
<td>[configuration] JNDI prefix can't be changed once getContext() has been called</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-111">CONFIGURATION-111</a></td>
<td>-</td>
<td>[configuration] addProperty throws a NPE in XMLConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-109">CONFIGURATION-109</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration partially supports List properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-106">CONFIGURATION-106</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration.save() does not keep element hierarchy</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-105">CONFIGURATION-105</a></td>
<td>-</td>
<td>[configuration] setUrl and getUrl for FileConfiguration are incorrect</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-104">CONFIGURATION-104</a></td>
<td>-</td>
<td>[configuration] Preserve file structure (line comments) when re-saving properties file</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-103">CONFIGURATION-103</a></td>
<td>-</td>
<td>[configuration] subset() method alters XMLConfiguration when invoked</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-101">CONFIGURATION-101</a></td>
<td>-</td>
<td>[configuration] testSaveInvalidURL in TestFileConfiguration fails</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-100">CONFIGURATION-100</a></td>
<td>-</td>
<td>[Configuration] XMLConfiguration.save() drops&lt;! DOCTYPE...  &gt;</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-99">CONFIGURATION-99</a></td>
<td>-</td>
<td>[configuration] PropertiesConfiguration doesn't throw exception when path is directory</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-97">CONFIGURATION-97</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration does not correctly handle comma delimited lists</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-96">CONFIGURATION-96</a></td>
<td>-</td>
<td>[configuration] File based configurations throw NPE when file does not exist</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-92">CONFIGURATION-92</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration.clearTree does not Auto Save.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-91">CONFIGURATION-91</a></td>
<td>-</td>
<td>[configuration] Problem adding property XMLConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-88">CONFIGURATION-88</a></td>
<td>-</td>
<td>[configuration] ClassNotFoundException on Sun App Server</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-87">CONFIGURATION-87</a></td>
<td>-</td>
<td>[configuration] getKeys(String) broken in JNDIConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-86">CONFIGURATION-86</a></td>
<td>-</td>
<td>[configuration] NullPointerException thrown by AbstractFileConfiguration.getFile()</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-85">CONFIGURATION-85</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration does not handle tag names with dots correctly</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-84">CONFIGURATION-84</a></td>
<td>-</td>
<td>[configuration] ConfigurationUtils.copy() does not work for XMLConfigurations with repeated keys</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-83">CONFIGURATION-83</a></td>
<td>-</td>
<td>[configuration] properties file with include in subdir does not work as expected</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-82">CONFIGURATION-82</a></td>
<td>-</td>
<td>[configuration] ServletRequestConfiguration getList null pointer exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-81">CONFIGURATION-81</a></td>
<td>-</td>
<td>[configuration] resolveContainerStore doesn't work with arrays</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-80">CONFIGURATION-80</a></td>
<td>-</td>
<td>[configuration] ConfigurationFactory not working as expected with include path resolution</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-76">CONFIGURATION-76</a></td>
<td>-</td>
<td>[configuration] Invalid subsets</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-75">CONFIGURATION-75</a></td>
<td>-</td>
<td>[configuration] HierarchicalXMLConfiguration.setProperty() deletes subelements</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-74">CONFIGURATION-74</a></td>
<td>-</td>
<td>[configuration] getKeys() in HierarchicalConfiguration doesn't preserve the order of the keys</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-71">CONFIGURATION-71</a></td>
<td>-</td>
<td>[configuration] Fake "resources" dependency kills Maven2</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-69">CONFIGURATION-69</a></td>
<td>-</td>
<td>[configuration] FileChangedReloadingStrategy cannot be resolved or is not a type</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-65">CONFIGURATION-65</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration cannot load from a jar</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-63">CONFIGURATION-63</a></td>
<td>-</td>
<td>[configuration] ConfigurationUtils.locate throws NullPointerException if the context ClassLoader is null</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-57">CONFIGURATION-57</a></td>
<td>-</td>
<td>[configuration] Do not fetch resources-1.0.jar in build.xml</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-47">CONFIGURATION-47</a></td>
<td>-</td>
<td>[configuration] ConfigurationFactory loading from classpath issue</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-44">CONFIGURATION-44</a></td>
<td>-</td>
<td>[configuration] Composite configuration with JNDI logs failed access as ERROR</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-32">CONFIGURATION-32</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration.save() doesn't escape reserved characters</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-31">CONFIGURATION-31</a></td>
<td>-</td>
<td>[configuration] Absolute paths in build.xml</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-29">CONFIGURATION-29</a></td>
<td>-</td>
<td>[configuration] SubsetConfiguration.getKeys() always appends "." delimiter to prefix</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-28">CONFIGURATION-28</a></td>
<td>-</td>
<td>[configuration] Interpolation method returns multi-valued properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-25">CONFIGURATION-25</a></td>
<td>-</td>
<td>[configuration] ClassCastException in XMLConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-22">CONFIGURATION-22</a></td>
<td>-</td>
<td>[configuration] JDK 1.3 compatibility</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-21">CONFIGURATION-21</a></td>
<td>-</td>
<td>[configuration] API Javadoc not in sync with jar nor with source code</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-19">CONFIGURATION-19</a></td>
<td>-</td>
<td>[configuration] DataConfiguration.getXXXArray() fails on empty values</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-18">CONFIGURATION-18</a></td>
<td>-</td>
<td>[configuration] DatabaseConfiguration doesn't support List properties</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-15">CONFIGURATION-15</a></td>
<td>-</td>
<td>[configuration] PropertyConfiguration.save() does not take basePath into account</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-13">CONFIGURATION-13</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration ignore a specific encoding in XML declaration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-12">CONFIGURATION-12</a></td>
<td>-</td>
<td>[configuration] fix project.xml to avoid cruft in resulting jar</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-11">CONFIGURATION-11</a></td>
<td>-</td>
<td>[configuration] Unclosed streams in BasePropertiesConfiguration</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-9">CONFIGURATION-9</a></td>
<td>-</td>
<td>[configuration] PropertiesConfiguration doesn't handle trailing backslashes properly</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-8">CONFIGURATION-8</a></td>
<td>-</td>
<td>[configuration] Escaped unicode characters in the key are not unescaped</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-4">CONFIGURATION-4</a></td>
<td>-</td>
<td>[configuration] XMLConfiguration doesn't ignore comments</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-759">CONFIGURATION-759</a></td>
<td>-</td>
<td>Update Spring from 4.3.24.RELEASE to 4.3.25.RELEASE</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-758">CONFIGURATION-758</a></td>
<td>-</td>
<td>Update commons-codec:commons-codec from 1.12 to 1.13.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-752">CONFIGURATION-752</a></td>
<td>-</td>
<td>Update Apache Commons VFS from 2.3 to 2.4.1</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-751">CONFIGURATION-751</a></td>
<td>-</td>
<td>Update Apache Commons Text from 1.6 to 1.7.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-720">CONFIGURATION-720</a></td>
<td>Interpolation</td>
<td>Replace use of deprecated Commons Lang string substitution code for Commons Text</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-707">CONFIGURATION-707</a></td>
<td>-</td>
<td>Update optional Spring dependencies from 4.3.14.RELEASE to 4.3.18.RELEASE.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-694">CONFIGURATION-694</a></td>
<td>-</td>
<td>Update Java requirement from version 7 to 8.</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-683">CONFIGURATION-683</a></td>
<td>Build</td>
<td>Update Spring from 4.3.9.RELEASE to 4.3.13.RELEASE</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-364">CONFIGURATION-364</a></td>
<td>-</td>
<td>Enhance StrSubstitutor to support nested ${var-${subvr}} expansion</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-213">CONFIGURATION-213</a></td>
<td>-</td>
<td>[configuration] Load file configurations from the classpath</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-210">CONFIGURATION-210</a></td>
<td>-</td>
<td>[configuration] Access to top level tag in XMLConfiguration</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-208">CONFIGURATION-208</a></td>
<td>-</td>
<td>[configuration] System property interpolation</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-207">CONFIGURATION-207</a></td>
<td>-</td>
<td>[configuration] Support "!" as a comment marker for PropertiesConfiguration</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-206">CONFIGURATION-206</a></td>
<td>-</td>
<td>[configuration] DTD validation on loading xml based configurations</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-205">CONFIGURATION-205</a></td>
<td>-</td>
<td>[configuration] AbstractConfiguration.addProperty doesn't split arrays</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-199">CONFIGURATION-199</a></td>
<td>-</td>
<td>[configuration][patch] ConfigurationXMLDocument and cleanup</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-195">CONFIGURATION-195</a></td>
<td>-</td>
<td>[configuration] Support the OpenStep property list format</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-194">CONFIGURATION-194</a></td>
<td>-</td>
<td>[configuration][patch] Enhancement: ConfigurationUtils</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-193">CONFIGURATION-193</a></td>
<td>-</td>
<td>[configuration]Added new examples page to documentation</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-191">CONFIGURATION-191</a></td>
<td>-</td>
<td>[configuration] Hexadecimal support</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-190">CONFIGURATION-190</a></td>
<td>-</td>
<td>[configuration] .properties header</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-189">CONFIGURATION-189</a></td>
<td>-</td>
<td>[configuration] Declaring reloadable configurations in the configuration descriptor</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-188">CONFIGURATION-188</a></td>
<td>-</td>
<td>[configuration] Disabling string splitting</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>-</td>
<td><a href="https://issues.apache.org/jira/browse/CONFIGURATION-187">CONFIGURATION-187</a></td>
<td>-</td>
<td>[configuration] Add save() method and comment handling to HierarchicalXMLConfiguration</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr></table></section>
</td>
</tr>
</table>

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/surefire.html -->

<!-- page_index: 14 -->

<a id="surefire--surefire-report"></a>

# Surefire Report

<a id="surefire--summary"></a>

## Summary

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 3014 | 0 | 0 | 2 | 99.9% | 18.51 s |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

<a id="surefire--package-list"></a>

## Package List

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Package | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.configuration2.tree.xpath](#surefire--org.apache.commons.configuration2.tree.xpath) | 88 | 0 | 0 | 0 | 100% | 0.073 s |
| [org.apache.commons.configuration2.interpol](#surefire--org.apache.commons.configuration2.interpol) | 90 | 0 | 0 | 0 | 100% | 0.033 s |
| [org.apache.commons.configuration2.builder](#surefire--org.apache.commons.configuration2.builder) | 197 | 0 | 0 | 0 | 100% | 0.087 s |
| [org.apache.commons.configuration2.builder.combined](#surefire--org.apache.commons.configuration2.builder.combined) | 205 | 0 | 0 | 0 | 100% | 11.00 s |
| [org.apache.commons.configuration2.reloading](#surefire--org.apache.commons.configuration2.reloading) | 45 | 0 | 0 | 0 | 100% | 0.062 s |
| [org.apache.commons.configuration2.plist](#surefire--org.apache.commons.configuration2.plist) | 73 | 0 | 0 | 0 | 100% | 0.274 s |
| [org.apache.commons.configuration2.beanutils](#surefire--org.apache.commons.configuration2.beanutils) | 168 | 0 | 0 | 0 | 100% | 0.043 s |
| [org.apache.commons.configuration2.event](#surefire--org.apache.commons.configuration2.event) | 131 | 0 | 0 | 0 | 100% | 0.125 s |
| [org.apache.commons.configuration2.builder.fluent](#surefire--org.apache.commons.configuration2.builder.fluent) | 53 | 0 | 0 | 0 | 100% | 0.037 s |
| [org.apache.commons.configuration2.web](#surefire--org.apache.commons.configuration2.web) | 146 | 0 | 0 | 0 | 100% | 0.050 s |
| [org.apache.commons.configuration2](#surefire--org.apache.commons.configuration2) | 1204 | 0 | 0 | 1 | 99.9% | 6.260 s |
| [org.apache.commons.configuration2.tree](#surefire--org.apache.commons.configuration2.tree) | 341 | 0 | 0 | 0 | 100% | 0.204 s |
| [org.apache.commons.configuration2.spring](#surefire--org.apache.commons.configuration2.spring) | 14 | 0 | 0 | 0 | 100% | 0.089 s |
| [org.apache.commons.configuration2.io](#surefire--org.apache.commons.configuration2.io) | 175 | 0 | 0 | 0 | 100% | 0.150 s |
| [org.apache.commons.configuration2.convert](#surefire--org.apache.commons.configuration2.convert) | 81 | 0 | 0 | 1 | 98.8% | 0.009 s |
| [org.apache.commons.configuration2.sync](#surefire--org.apache.commons.configuration2.sync) | 3 | 0 | 0 | 0 | 100% | 0.011 s |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

<a id="surefire--org.apache.commons.configuration2.tree.xpath"></a>

### org.apache.commons.configuration2.tree.xpath

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestConfigurationIteratorAttributes](#surefire--org.apache.commons.configuration2.tree.xpath.testconfigurationiteratorattributes) | 6 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestConfigurationNodePointer](#surefire--org.apache.commons.configuration2.tree.xpath.testconfigurationnodepointer) | 7 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestXPathExpressionEngineInConfig](#surefire--org.apache.commons.configuration2.tree.xpath.testxpathexpressionengineinconfig) | 6 | 0 | 0 | 0 | 100% | 0.014 s |
|  | [TestConfigurationNodeIteratorChildren](#surefire--org.apache.commons.configuration2.tree.xpath.testconfigurationnodeiteratorchildren) | 13 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestConfigurationNodePointerFactory](#surefire--org.apache.commons.configuration2.tree.xpath.testconfigurationnodepointerfactory) | 8 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [TestXPathContextFactory](#surefire--org.apache.commons.configuration2.tree.xpath.testxpathcontextfactory) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestConfigurationAttributePointer](#surefire--org.apache.commons.configuration2.tree.xpath.testconfigurationattributepointer) | 13 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestXPathExpressionEngine](#surefire--org.apache.commons.configuration2.tree.xpath.testxpathexpressionengine) | 34 | 0 | 0 | 0 | 100% | 0.033 s |

<a id="surefire--org.apache.commons.configuration2.interpol"></a>

### org.apache.commons.configuration2.interpol

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestExprLookup](#surefire--org.apache.commons.configuration2.interpol.testexprlookup) | 7 | 0 | 0 | 0 | 100% | 0.017 s |
|  | [TestConstantLookup](#surefire--org.apache.commons.configuration2.interpol.testconstantlookup) | 8 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestSystemPropertiesLookup](#surefire--org.apache.commons.configuration2.interpol.testsystempropertieslookup) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestDummyLookup](#surefire--org.apache.commons.configuration2.interpol.testdummylookup) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestEnvironmentLookup](#surefire--org.apache.commons.configuration2.interpol.testenvironmentlookup) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestInterpolatorSpecification](#surefire--org.apache.commons.configuration2.interpol.testinterpolatorspecification) | 10 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestConfigurationInterpolator](#surefire--org.apache.commons.configuration2.interpol.testconfigurationinterpolator) | 60 | 0 | 0 | 0 | 100% | 0.011 s |

<a id="surefire--org.apache.commons.configuration2.builder"></a>

### org.apache.commons.configuration2.builder

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestDefaultParametersManager](#surefire--org.apache.commons.configuration2.builder.testdefaultparametersmanager) | 9 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestBasicBuilderParameters](#surefire--org.apache.commons.configuration2.builder.testbasicbuilderparameters) | 34 | 0 | 0 | 0 | 100% | 0.014 s |
|  | [TestBasicConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.testbasicconfigurationbuilder) | 27 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestBasicConfigurationBuilderEvents](#surefire--org.apache.commons.configuration2.builder.testbasicconfigurationbuilderevents) | 11 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestPropertiesBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.testpropertiesbuilderparametersimpl) | 8 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestReloadingBuilderSupportListener](#surefire--org.apache.commons.configuration2.builder.testreloadingbuildersupportlistener) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestDefaultReloadingDetectorFactory](#surefire--org.apache.commons.configuration2.builder.testdefaultreloadingdetectorfactory) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestAutoSaveListener](#surefire--org.apache.commons.configuration2.builder.testautosavelistener) | 7 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [TestFileBasedBuilderParameters](#surefire--org.apache.commons.configuration2.builder.testfilebasedbuilderparameters) | 24 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestBuilderConfigurationWrapperFactory](#surefire--org.apache.commons.configuration2.builder.testbuilderconfigurationwrapperfactory) | 8 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestJndiBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.testjndibuilderparametersimpl) | 4 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestXMLBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.testxmlbuilderparametersimpl) | 8 | 0 | 0 | 0 | 100% | 0.008 s |
|  | [TestEventListenerParameters](#surefire--org.apache.commons.configuration2.builder.testeventlistenerparameters) | 4 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestFileBasedConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.testfilebasedconfigurationbuilder) | 25 | 0 | 0 | 0 | 100% | 0.016 s |
|  | [TestReloadingFileBasedConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.testreloadingfilebasedconfigurationbuilder) | 9 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestDatabaseBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.testdatabasebuilderparametersimpl) | 8 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestCopyObjectDefaultHandler](#surefire--org.apache.commons.configuration2.builder.testcopyobjectdefaulthandler) | 4 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestHierarchicalBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.testhierarchicalbuilderparametersimpl) | 3 | 0 | 0 | 0 | 100% | 0 s |

<a id="surefire--org.apache.commons.configuration2.builder.combined"></a>

### org.apache.commons.configuration2.builder.combined

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestMultiWrapDynaBean](#surefire--org.apache.commons.configuration2.builder.combined.testmultiwrapdynabean) | 13 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestBaseConfigurationBuilderProvider](#surefire--org.apache.commons.configuration2.builder.combined.testbaseconfigurationbuilderprovider) | 9 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestMultiFileConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.combined.testmultifileconfigurationbuilder) | 16 | 0 | 0 | 0 | 100% | 0.652 s |
|  | [TestCombinedConfigurationBuilderVFS](#surefire--org.apache.commons.configuration2.builder.combined.testcombinedconfigurationbuildervfs) | 52 | 0 | 0 | 0 | 100% | 5.141 s |
|  | [TestFileExtensionConfigurationBuilderProvider](#surefire--org.apache.commons.configuration2.builder.combined.testfileextensionconfigurationbuilderprovider) | 10 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestReloadingCombinedConfigurationBuilderFileBased](#surefire--org.apache.commons.configuration2.builder.combined.testreloadingcombinedconfigurationbuilderfilebased) | 4 | 0 | 0 | 0 | 100% | 0.059 s |
|  | [TestCombinedBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.combined.testcombinedbuilderparametersimpl) | 27 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestReloadingCombinedConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.combined.testreloadingcombinedconfigurationbuilder) | 5 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestCombinedConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.combined.testcombinedconfigurationbuilder) | 51 | 0 | 0 | 0 | 100% | 5.119 s |
|  | [TestMultiFileBuilderParametersImpl](#surefire--org.apache.commons.configuration2.builder.combined.testmultifilebuilderparametersimpl) | 7 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestConfigurationDeclaration](#surefire--org.apache.commons.configuration2.builder.combined.testconfigurationdeclaration) | 5 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestReloadingMultiFileConfigurationBuilder](#surefire--org.apache.commons.configuration2.builder.combined.testreloadingmultifileconfigurationbuilder) | 6 | 0 | 0 | 0 | 100% | 0.003 s |

<a id="surefire--org.apache.commons.configuration2.reloading"></a>

### org.apache.commons.configuration2.reloading

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestManagedReloadingDetector](#surefire--org.apache.commons.configuration2.reloading.testmanagedreloadingdetector) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestReloadingController](#surefire--org.apache.commons.configuration2.reloading.testreloadingcontroller) | 8 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestFileHandlerReloadingDetector](#surefire--org.apache.commons.configuration2.reloading.testfilehandlerreloadingdetector) | 11 | 0 | 0 | 0 | 100% | 0.014 s |
|  | [TestPeriodicReloadingTrigger](#surefire--org.apache.commons.configuration2.reloading.testperiodicreloadingtrigger) | 9 | 0 | 0 | 0 | 100% | 0.012 s |
|  | [TestVFSFileHandlerReloadingDetector](#surefire--org.apache.commons.configuration2.reloading.testvfsfilehandlerreloadingdetector) | 6 | 0 | 0 | 0 | 100% | 0.030 s |
|  | [TestCombinedReloadingController](#surefire--org.apache.commons.configuration2.reloading.testcombinedreloadingcontroller) | 8 | 0 | 0 | 0 | 100% | 0.002 s |

<a id="surefire--org.apache.commons.configuration2.plist"></a>

### org.apache.commons.configuration2.plist

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestPropertyListConfiguration](#surefire--org.apache.commons.configuration2.plist.testpropertylistconfiguration) | 23 | 0 | 0 | 0 | 100% | 0.034 s |
|  | [TestXMLPropertyListConfigurationEvents](#surefire--org.apache.commons.configuration2.plist.testxmlpropertylistconfigurationevents) | 10 | 0 | 0 | 0 | 100% | 0.146 s |
|  | [TestPropertyListConfigurationEvents](#surefire--org.apache.commons.configuration2.plist.testpropertylistconfigurationevents) | 10 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [TestPropertyListParser](#surefire--org.apache.commons.configuration2.plist.testpropertylistparser) | 4 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestXMLPropertyListConfiguration](#surefire--org.apache.commons.configuration2.plist.testxmlpropertylistconfiguration) | 26 | 0 | 0 | 0 | 100% | 0.084 s |

<a id="surefire--org.apache.commons.configuration2.beanutils"></a>

### org.apache.commons.configuration2.beanutils

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestCombinedBeanDeclaration](#surefire--org.apache.commons.configuration2.beanutils.testcombinedbeandeclaration) | 12 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestBeanHelper](#surefire--org.apache.commons.configuration2.beanutils.testbeanhelper) | 27 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestXMLBeanDeclaration](#surefire--org.apache.commons.configuration2.beanutils.testxmlbeandeclaration) | 28 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestConstructorArg](#surefire--org.apache.commons.configuration2.beanutils.testconstructorarg) | 6 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestConfigurationDynaBeanXMLConfig](#surefire--org.apache.commons.configuration2.beanutils.testconfigurationdynabeanxmlconfig) | 42 | 0 | 0 | 0 | 100% | 0.018 s |
|  | [TestConfigurationDynaBean](#surefire--org.apache.commons.configuration2.beanutils.testconfigurationdynabean) | 42 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestDefaultBeanFactory](#surefire--org.apache.commons.configuration2.beanutils.testdefaultbeanfactory) | 11 | 0 | 0 | 0 | 100% | 0.005 s |

<a id="surefire--org.apache.commons.configuration2.event"></a>

### org.apache.commons.configuration2.event

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestEventType](#surefire--org.apache.commons.configuration2.event.testeventtype) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestSubsetConfigurationEvents](#surefire--org.apache.commons.configuration2.event.testsubsetconfigurationevents) | 8 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestXMLConfigurationEvents](#surefire--org.apache.commons.configuration2.event.testxmlconfigurationevents) | 13 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestPropertiesConfigurationEvents](#surefire--org.apache.commons.configuration2.event.testpropertiesconfigurationevents) | 8 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestEventSource](#surefire--org.apache.commons.configuration2.event.testeventsource) | 19 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestConfigurationEventTypes](#surefire--org.apache.commons.configuration2.event.testconfigurationeventtypes) | 19 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestMapConfigurationEvents](#surefire--org.apache.commons.configuration2.event.testmapconfigurationevents) | 8 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestHierarchicalConfigurationEvents](#surefire--org.apache.commons.configuration2.event.testhierarchicalconfigurationevents) | 13 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestEvent](#surefire--org.apache.commons.configuration2.event.testevent) | 3 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestDatabaseConfigurationEvents](#surefire--org.apache.commons.configuration2.event.testdatabaseconfigurationevents) | 8 | 0 | 0 | 0 | 100% | 0.117 s |
|  | [TestEventListenerList](#surefire--org.apache.commons.configuration2.event.testeventlistenerlist) | 31 | 0 | 0 | 0 | 100% | 0.002 s |

<a id="surefire--org.apache.commons.configuration2.builder.fluent"></a>

### org.apache.commons.configuration2.builder.fluent

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestParameters](#surefire--org.apache.commons.configuration2.builder.fluent.testparameters) | 19 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [TestConfigurations](#surefire--org.apache.commons.configuration2.builder.fluent.testconfigurations) | 34 | 0 | 0 | 0 | 100% | 0.028 s |

<a id="surefire--org.apache.commons.configuration2.web"></a>

### org.apache.commons.configuration2.web

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestJakartaServletConfiguration](#surefire--org.apache.commons.configuration2.web.testjakartaservletconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestServletConfiguration](#surefire--org.apache.commons.configuration2.web.testservletconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestJakartaServletFilterConfiguration](#surefire--org.apache.commons.configuration2.web.testjakartaservletfilterconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestJakartaServletRequestConfiguration](#surefire--org.apache.commons.configuration2.web.testjakartaservletrequestconfiguration) | 17 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [TestJakartaServletContextConfiguration](#surefire--org.apache.commons.configuration2.web.testjakartaservletcontextconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.014 s |
|  | [TestAppletConfiguration](#surefire--org.apache.commons.configuration2.web.testappletconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestServletContextConfiguration](#surefire--org.apache.commons.configuration2.web.testservletcontextconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestServletRequestConfiguration](#surefire--org.apache.commons.configuration2.web.testservletrequestconfiguration) | 17 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [TestServletFilterConfiguration](#surefire--org.apache.commons.configuration2.web.testservletfilterconfiguration) | 16 | 0 | 0 | 0 | 100% | 0.002 s |

<a id="surefire--org.apache.commons.configuration2"></a>

### org.apache.commons.configuration2

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestAbstractHierarchicalConfiguration](#surefire--org.apache.commons.configuration2.testabstracthierarchicalconfiguration) | 55 | 0 | 0 | 0 | 100% | 0.014 s |
|  | [TestDatabaseConfiguration](#surefire--org.apache.commons.configuration2.testdatabaseconfiguration) | 39 | 0 | 0 | 0 | 100% | 0.788 s |
|  | [TestMapConfiguration](#surefire--org.apache.commons.configuration2.testmapconfiguration) | 25 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestEqualBehavior](#surefire--org.apache.commons.configuration2.testequalbehavior) | 7 | 0 | 0 | 0 | 100% | 0.026 s |
|  | [TestXMLListHandling](#surefire--org.apache.commons.configuration2.testxmllisthandling) | 5 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestSubsetConfiguration848](#surefire--org.apache.commons.configuration2.testsubsetconfiguration848) | 2 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestBaseConfigurationXMLReader](#surefire--org.apache.commons.configuration2.testbaseconfigurationxmlreader) | 4 | 0 | 0 | 0 | 100% | 0.004 s |
|  | [TestPatternSubtreeConfiguration](#surefire--org.apache.commons.configuration2.testpatternsubtreeconfiguration) | 3 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestCompositeConfiguration](#surefire--org.apache.commons.configuration2.testcompositeconfiguration) | 52 | 0 | 0 | 0 | 100% | 0.031 s |
|  | [TestYAMLConfiguration](#surefire--org.apache.commons.configuration2.testyamlconfiguration) | 12 | 0 | 0 | 0 | 100% | 0.030 s |
|  | [TestSubsetConfiguration](#surefire--org.apache.commons.configuration2.testsubsetconfiguration) | 23 | 0 | 0 | 0 | 100% | 0.180 s |
|  | [TestPropertiesSequence](#surefire--org.apache.commons.configuration2.testpropertiessequence) | 3 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestEnvironmentConfiguration](#surefire--org.apache.commons.configuration2.testenvironmentconfiguration) | 5 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestConfigurationLookup](#surefire--org.apache.commons.configuration2.testconfigurationlookup) | 5 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestThreesomeConfiguration](#surefire--org.apache.commons.configuration2.testthreesomeconfiguration) | 3 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestHierarchicalXMLConfiguration](#surefire--org.apache.commons.configuration2.testhierarchicalxmlconfiguration) | 10 | 0 | 0 | 0 | 100% | 0.010 s |
|  | [TestNullCompositeConfiguration](#surefire--org.apache.commons.configuration2.testnullcompositeconfiguration) | 23 | 0 | 0 | 0 | 100% | 0.016 s |
|  | [TestPropertiesConfiguration](#surefire--org.apache.commons.configuration2.testpropertiesconfiguration) | 114 | 0 | 0 | 0 | 100% | 0.096 s |
|  | [TestHierarchicalConfigurationXMLReader](#surefire--org.apache.commons.configuration2.testhierarchicalconfigurationxmlreader) | 1 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestAbstractConfigurationBasicFeatures](#surefire--org.apache.commons.configuration2.testabstractconfigurationbasicfeatures) | 65 | 0 | 0 | 0 | 100% | 0.025 s |
|  | [TestCompositeConfigurationNonStringProperties](#surefire--org.apache.commons.configuration2.testcompositeconfigurationnonstringproperties) | 23 | 0 | 0 | 0 | 100% | 0.008 s |
|  | [TestJNDIConfiguration](#surefire--org.apache.commons.configuration2.testjndiconfiguration) | 27 | 0 | 0 | 0 | 100% | 0.057 s |
|  | [TestConfigurationMap](#surefire--org.apache.commons.configuration2.testconfigurationmap) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestEqualsProperty](#surefire--org.apache.commons.configuration2.testequalsproperty) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestPatternSubtreeConfigurationWrapper](#surefire--org.apache.commons.configuration2.testpatternsubtreeconfigurationwrapper) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestNonStringProperties](#surefire--org.apache.commons.configuration2.testnonstringproperties) | 23 | 0 | 0 | 0 | 100% | 0.008 s |
|  | [TestXMLPropertiesConfiguration](#surefire--org.apache.commons.configuration2.testxmlpropertiesconfiguration) | 4 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestINIConfiguration](#surefire--org.apache.commons.configuration2.testiniconfiguration) | 77 | 0 | 0 | 0 | 100% | 0.038 s |
|  | [TestDefaultImmutableConfiguration](#surefire--org.apache.commons.configuration2.testdefaultimmutableconfiguration) | 4 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestCombinedConfiguration](#surefire--org.apache.commons.configuration2.testcombinedconfiguration) | 59 | 0 | 0 | 0 | 100% | 0.093 s |
|  | [TestDynamicCombinedConfiguration](#surefire--org.apache.commons.configuration2.testdynamiccombinedconfiguration) | 12 | 0 | 0 | 0 | 100% | 4.225 s |
|  | [TestJSONConfiguration](#surefire--org.apache.commons.configuration2.testjsonconfiguration) | 11 | 0 | 0 | 1 | 90.9% | 0.057 s |
|  | [TestXMLConfiguration605](#surefire--org.apache.commons.configuration2.testxmlconfiguration605) | 8 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestBaseHierarchicalConfigurationSynchronization](#surefire--org.apache.commons.configuration2.testbasehierarchicalconfigurationsynchronization) | 14 | 0 | 0 | 0 | 100% | 0.015 s |
|  | [TestDataConfiguration](#surefire--org.apache.commons.configuration2.testdataconfiguration) | 61 | 0 | 0 | 0 | 100% | 0.200 s |
|  | [TestXMLDocumentHelper](#surefire--org.apache.commons.configuration2.testxmldocumenthelper) | 11 | 0 | 0 | 0 | 100% | 0.035 s |
|  | [TestHierarchicalConfiguration](#surefire--org.apache.commons.configuration2.testhierarchicalconfiguration) | 37 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestConfigurationSet](#surefire--org.apache.commons.configuration2.testconfigurationset) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestBaseNullConfiguration](#surefire--org.apache.commons.configuration2.testbasenullconfiguration) | 37 | 0 | 0 | 0 | 100% | 0.004 s |
|  | [TestImmutableConfiguration](#surefire--org.apache.commons.configuration2.testimmutableconfiguration) | 10 | 0 | 0 | 0 | 100% | 0.009 s |
|  | [TestConfigurationUtils](#surefire--org.apache.commons.configuration2.testconfigurationutils) | 36 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestJNDIEnvironmentValues](#surefire--org.apache.commons.configuration2.testjndienvironmentvalues) | 12 | 0 | 0 | 0 | 100% | 0.013 s |
|  | [TestCatalogResolver](#surefire--org.apache.commons.configuration2.testcatalogresolver) | 5 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestSubnodeConfiguration](#surefire--org.apache.commons.configuration2.testsubnodeconfiguration) | 24 | 0 | 0 | 0 | 100% | 0.011 s |
|  | [TestPropertiesConfigurationLayout](#surefire--org.apache.commons.configuration2.testpropertiesconfigurationlayout) | 39 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestBaseConfiguration](#surefire--org.apache.commons.configuration2.testbaseconfiguration) | 65 | 0 | 0 | 0 | 100% | 0.008 s |
|  | [TestNullJNDIEnvironmentValues](#surefire--org.apache.commons.configuration2.testnulljndienvironmentvalues) | 12 | 0 | 0 | 0 | 100% | 0.014 s |
|  | [TestSystemConfiguration](#surefire--org.apache.commons.configuration2.testsystemconfiguration) | 5 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestConfigurationConverter](#surefire--org.apache.commons.configuration2.testconfigurationconverter) | 6 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestAbstractConfigurationSynchronization](#surefire--org.apache.commons.configuration2.testabstractconfigurationsynchronization) | 19 | 0 | 0 | 0 | 100% | 0.005 s |
|  | [TestStrictConfigurationComparator](#surefire--org.apache.commons.configuration2.teststrictconfigurationcomparator) | 2 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestXMLConfiguration](#surefire--org.apache.commons.configuration2.testxmlconfiguration) | 99 | 0 | 0 | 0 | 100% | 0.182 s |

<a id="surefire--org.apache.commons.configuration2.tree"></a>

### org.apache.commons.configuration2.tree

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestImmutableNode](#surefire--org.apache.commons.configuration2.tree.testimmutablenode) | 36 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestMergeCombiner](#surefire--org.apache.commons.configuration2.tree.testmergecombiner) | 8 | 0 | 0 | 0 | 100% | 0.015 s |
|  | [TestDefaultExpressionEngineSymbols](#surefire--org.apache.commons.configuration2.tree.testdefaultexpressionenginesymbols) | 6 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestNodeUpdateData](#surefire--org.apache.commons.configuration2.tree.testnodeupdatedata) | 7 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestDefaultExpressionEngine](#surefire--org.apache.commons.configuration2.tree.testdefaultexpressionengine) | 38 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestNodeSelector](#surefire--org.apache.commons.configuration2.tree.testnodeselector) | 12 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestInMemoryNodeModelTrackedNodes](#surefire--org.apache.commons.configuration2.tree.testinmemorynodemodeltrackednodes) | 43 | 0 | 0 | 0 | 100% | 0.011 s |
|  | [TestTreeData](#surefire--org.apache.commons.configuration2.tree.testtreedata) | 25 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestDefaultConfigurationKey](#surefire--org.apache.commons.configuration2.tree.testdefaultconfigurationkey) | 33 | 0 | 0 | 0 | 100% | 0.006 s |
|  | [TestInMemoryNodeModelReferences](#surefire--org.apache.commons.configuration2.tree.testinmemorynodemodelreferences) | 12 | 0 | 0 | 0 | 100% | 0.015 s |
|  | [TestUnionCombiner](#surefire--org.apache.commons.configuration2.tree.testunioncombiner) | 6 | 0 | 0 | 0 | 100% | 0.018 s |
|  | [TestOverrideCombiner](#surefire--org.apache.commons.configuration2.tree.testoverridecombiner) | 9 | 0 | 0 | 0 | 100% | 0.013 s |
|  | [TestNodeHandlerDecorator](#surefire--org.apache.commons.configuration2.tree.testnodehandlerdecorator) | 25 | 0 | 0 | 0 | 100% | 0.004 s |
|  | [TestQueryResult](#surefire--org.apache.commons.configuration2.tree.testqueryresult) | 9 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestNodeTreeWalker](#surefire--org.apache.commons.configuration2.tree.testnodetreewalker) | 8 | 0 | 0 | 0 | 100% | 0.004 s |
|  | [TestTrackedNodeHandler](#surefire--org.apache.commons.configuration2.tree.testtrackednodehandler) | 2 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestTrackedNodeModel](#surefire--org.apache.commons.configuration2.tree.testtrackednodemodel) | 13 | 0 | 0 | 0 | 100% | 0.049 s |
|  | [TestInMemoryNodeModel](#surefire--org.apache.commons.configuration2.tree.testinmemorynodemodel) | 39 | 0 | 0 | 0 | 100% | 0.041 s |
|  | [TestNodeNameMatchers](#surefire--org.apache.commons.configuration2.tree.testnodenamematchers) | 6 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestNodeAddData](#surefire--org.apache.commons.configuration2.tree.testnodeadddata) | 4 | 0 | 0 | 0 | 100% | 0.001 s |

<a id="surefire--org.apache.commons.configuration2.spring"></a>

### org.apache.commons.configuration2.spring

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestConfigurationPropertySource](#surefire--org.apache.commons.configuration2.spring.testconfigurationpropertysource) | 4 | 0 | 0 | 0 | 100% | 0.088 s |
|  | [TestConfigurationPropertiesFactoryBean](#surefire--org.apache.commons.configuration2.spring.testconfigurationpropertiesfactorybean) | 10 | 0 | 0 | 0 | 100% | 0.001 s |

<a id="surefire--org.apache.commons.configuration2.io"></a>

### org.apache.commons.configuration2.io

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestFileHandler](#surefire--org.apache.commons.configuration2.io.testfilehandler) | 85 | 0 | 0 | 0 | 100% | 0.119 s |
|  | [TestClasspathLocationStrategy](#surefire--org.apache.commons.configuration2.io.testclasspathlocationstrategy) | 3 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestAbsoluteNameLocationStrategy](#surefire--org.apache.commons.configuration2.io.testabsolutenamelocationstrategy) | 4 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestDefaultFileSystem](#surefire--org.apache.commons.configuration2.io.testdefaultfilesystem) | 3 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestFileLocatorUtils](#surefire--org.apache.commons.configuration2.io.testfilelocatorutils) | 36 | 0 | 0 | 0 | 100% | 0.007 s |
|  | [TestFileLocator](#surefire--org.apache.commons.configuration2.io.testfilelocator) | 8 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestFileSystemLocationStrategy](#surefire--org.apache.commons.configuration2.io.testfilesystemlocationstrategy) | 1 | 0 | 0 | 0 | 100% | 0 s |
|  | [TestCombinedLocationStrategy](#surefire--org.apache.commons.configuration2.io.testcombinedlocationstrategy) | 7 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestBasePathLocationStrategy](#surefire--org.apache.commons.configuration2.io.testbasepathlocationstrategy) | 4 | 0 | 0 | 0 | 100% | 0.001 s |
|  | [TestHomeDirectoryLocationStrategy](#surefire--org.apache.commons.configuration2.io.testhomedirectorylocationstrategy) | 6 | 0 | 0 | 0 | 100% | 0.002 s |
|  | [TestProvidedURLLocationStrategy](#surefire--org.apache.commons.configuration2.io.testprovidedurllocationstrategy) | 2 | 0 | 0 | 0 | 100% | 0.010 s |
|  | [TestConfigurationLogger](#surefire--org.apache.commons.configuration2.io.testconfigurationlogger) | 16 | 0 | 0 | 0 | 100% | 0.004 s |

<a id="surefire--org.apache.commons.configuration2.convert"></a>

### org.apache.commons.configuration2.convert

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestDisabledListDelimiterHandler](#surefire--org.apache.commons.configuration2.convert.testdisabledlistdelimiterhandler) | 13 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestPropertyConverter](#surefire--org.apache.commons.configuration2.convert.testpropertyconverter) | 29 | 0 | 0 | 1 | 96.6% | 0.002 s |
|  | [TestDefaultConversionHandler](#surefire--org.apache.commons.configuration2.convert.testdefaultconversionhandler) | 25 | 0 | 0 | 0 | 100% | 0.003 s |
|  | [TestDefaultListDelimiterHandler](#surefire--org.apache.commons.configuration2.convert.testdefaultlistdelimiterhandler) | 14 | 0 | 0 | 0 | 100% | 0.001 s |

<a id="surefire--org.apache.commons.configuration2.sync"></a>

### org.apache.commons.configuration2.sync

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [TestReadWriteSynchronizer](#surefire--org.apache.commons.configuration2.sync.testreadwritesynchronizer) | 3 | 0 | 0 | 0 | 100% | 0.011 s |

<a id="surefire--test-cases"></a>

## Test Cases

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

<a id="surefire--testabstracthierarchicalconfiguration"></a>

### TestAbstractHierarchicalConfiguration

|  |  |  |
| --- | --- | --- |
|  | testNodeKeyCachePopulated | 0 s |
|  | testClearTreeComplex | 0.001 s |
|  | testInterpolationUnknownProperty | 0 s |
|  | testInterpolation | 0 s |
|  | testGetKeysWithKeyAsPrefixMultiple | 0 s |
|  | testNodeKeyEmptyCache | 0 s |
|  | testInitCopyNull | 0 s |
|  | testInterpolationBasic | 0.001 s |
|  | testResolveNodeKey | 0 s |
|  | testNodeKeyCacheHit | 0 s |
|  | testClear | 0 s |
|  | testClone | 0 s |
|  | testInterpolator | 0 s |
|  | testIsEmptyRootOnly | 0 s |
|  | testInterpolationSubset | 0 s |
|  | testSize | 0 s |
|  | testInterpolationLocalhost | 0.006 s |
|  | testNodeKeyRootNode | 0 s |
|  | testSetExpressionEngine | 0.001 s |
|  | testInterpolationEscaped | 0 s |
|  | testGetKeysAttribute | 0 s |
|  | testGetKeysAttributePrefix | 0 s |
|  | testClearTree | 0 s |
|  | testAddNodes | 0 s |
|  | testInterpolationSubsetMultipleLayers | 0 s |
|  | testCloneWithEventListeners | 0.001 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testNodeKeyCacheUsage | 0 s |
|  | testAddNodesForNonExistingKey | 0 s |
|  | testAddNodesWithAttributeKey | 0 s |
|  | testInterpolationConstants | 0 s |
|  | testGetKeysOrder | 0 s |
|  | testContainsValue | 0.001 s |
|  | testClearTreeHierarchy | 0 s |
|  | testClearProperty | 0 s |
|  | testSetProperty | 0 s |
|  | testGetProperty | 0 s |
|  | testInterpolatedConfiguration | 0.001 s |
|  | testGetPropertyKeyWithBrackets | 0 s |
|  | testAddPropertyWithListHandling | 0 s |
|  | testInterpolationLoop | 0 s |
|  | testIsEmptyNodesWithNoValues | 0 s |
|  | testInterpolationSystemProperties | 0 s |
|  | testAddPropertyInvalidKey | 0 s |
|  | testAddNodesCopy | 0 s |
|  | testGetNodeModel | 0 s |
|  | testResolveNodeKeyAttribute | 0 s |
|  | testAddProperty | 0 s |
|  | testInterpolationMultipleLevels | 0 s |
|  | testGetKeysString | 0 s |
|  | testGetMaxIndex | 0 s |
|  | testGetKeysWithKeyAsPrefix | 0 s |
|  | testCloneInterpolation | 0.001 s |
|  | testIsEmptyFalse | 0 s |

<a id="surefire--testdatabaseconfiguration"></a>

### TestDatabaseConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetKeysMultiple | 0.165 s |
|  | testGetListWithDelimiter | 0.022 s |
|  | testClearPropertyCommit | 0.020 s |
|  | testClearError | 0.021 s |
|  | testContainsKeySingle | 0.018 s |
|  | testClearPropertySingle | 0.020 s |
|  | testSetPropertyWithDelimiter | 0.018 s |
|  | testAddNonStringProperty | 0.016 s |
|  | testGetKeysInternalNoDatasource | 0.002 s |
|  | testContainsKeyError | 0.016 s |
|  | testAddWithDelimiter | 0.017 s |
|  | testGetKeys | 0.017 s |
|  | testGetList | 0.018 s |
|  | testIsEmptyMultiple | 0.019 s |
|  | testGetKeysError | 0.016 s |
|  | testContainsValue | 0.015 s |
|  | testExtractPropertyValueCLOBEmpty | 0.031 s |
|  | testLogErrorListener | 0.016 s |
|  | testGetPropertyDirectMultiple | 0.015 s |
|  | containsValueInternal | 0.017 s |
|  | testGetListWithDelimiterParsingDisabled | 0.015 s |
|  | testContainsKeyMultiple | 0.015 s |
|  | testAddPropertyDirectCommit | 0.016 s |
|  | testClearPropertyMultipleOtherConfig | 0.018 s |
|  | testClearPropertyError | 0.016 s |
|  | testClearPropertyMultiple | 0.015 s |
|  | testGetPropertyError | 0.016 s |
|  | testAddPropertyDirectSingle | 0.014 s |
|  | testExtractPropertyValueCLOB | 0.014 s |
|  | testGetPropertyDirectSingle | 0.015 s |
|  | testAddPropertyDirectMultiple | 0.014 s |
|  | testClearCommit | 0.014 s |
|  | testIsEmptySingle | 0.015 s |
|  | testGetKeysSingle | 0.014 s |
|  | testClearMultiple | 0.014 s |
|  | testClearSingle | 0.017 s |
|  | testClearSubset | 0.013 s |
|  | testIsEmptyError | 0.014 s |
|  | testAddPropertyError | 0.015 s |

<a id="surefire--testmapconfiguration"></a>

### TestMapConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testClearProperty | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0 s |
|  | testAddPropertyDirect | 0 s |
|  | testClone | 0.001 s |
|  | testCloneModify | 0 s |
|  | testGetPropertyTrimNoSplit | 0 s |
|  | testContainsValue | 0 s |
|  | testGetPropertyTrim | 0 s |
|  | testGetMap | 0 s |
|  | testAddProperty | 0 s |
|  | testNullMap | 0 s |
|  | testGetPropertyTrimDisabled | 0 s |
|  | testCloneInterpolation | 0.001 s |

<a id="surefire--testimmutablenode"></a>

### TestImmutableNode

|  |  |  |
| --- | --- | --- |
|  | testRemoveChildExisting | 0.001 s |
|  | testGetChildrenByMissingName | 0 s |
|  | testAddAttributesNull | 0 s |
|  | testChildrenImmutable | 0 s |
|  | testSetAttribute | 0 s |
|  | testSetAttributes | 0 s |
|  | testSetAttributesEmpty | 0 s |
|  | testSimpleProperties | 0 s |
|  | testReplaceChildrenNullCollection | 0.001 s |
|  | testNodeWithAttributes | 0 s |
|  | testSetAttributesNull | 0 s |
|  | testAttributesImmutable | 0 s |
|  | testNodeWithNullChild | 0 s |
|  | testAddChildrenNullElement | 0 s |
|  | testRemoveAttributeExisting | 0.001 s |
|  | testAddChild | 0 s |
|  | testReplaceChildNotExisting | 0 s |
|  | testNodeWithAttributesManipulateLater | 0 s |
|  | testNodeWithChildren | 0 s |
|  | testNodeWithAddMultipleChildren | 0 s |
|  | testSetAttributeOverride | 0 s |
|  | testNodeWithMultipleAttributes | 0 s |
|  | testRemoveChildMultiple | 0 s |
|  | testAddChildNull | 0.001 s |
|  | testRemoveAttributeNotExisting | 0 s |
|  | testGetChildrenByName | 0 s |
|  | testSetName | 0 s |
|  | testRemoveChildNodeNotExisting | 0 s |
|  | testStream | 0 s |
|  | testGetChildrenByNullName | 0 s |
|  | testReplaceChildExisting | 0 s |
|  | testReplaceChildNull | 0.001 s |
|  | testReplaceChildren | 0 s |
|  | testNodeWithChildrenManipulateLater | 0 s |
|  | testAddChildrenNull | 0 s |
|  | testSetValue | 0 s |

<a id="surefire--testmultiwrapdynabean"></a>

### TestMultiWrapDynaBean

|  |  |  |
| --- | --- | --- |
|  | testGetMappedProperty | 0.001 s |
|  | testGetDynaClass | 0 s |
|  | testSetIndexedProperty | 0 s |
|  | testContains | 0.001 s |
|  | testSetSimpleProperty | 0 s |
|  | testOrderOfProperties | 0 s |
|  | testGetPropertyUnknown | 0 s |
|  | testGetDynaClassName | 0 s |
|  | testSetMappedProperty | 0 s |
|  | testGetDynaClassNewInstance | 0 s |
|  | testRemove | 0 s |
|  | testGetSimpleProperty | 0 s |
|  | testGetIndexedProperty | 0.001 s |

<a id="surefire--testequalbehavior"></a>

### TestEqualBehavior

|  |  |  |
| --- | --- | --- |
|  | testAddingUnset | 0.007 s |
|  | testDeletingNonExisting | 0.004 s |
|  | testLoading | 0.003 s |
|  | testSettingExisting | 0.002 s |
|  | testAddingSet | 0.002 s |
|  | testSettingNonExisting | 0.002 s |
|  | testDeletingExisting | 0.002 s |

<a id="surefire--testxmllisthandling"></a>

### TestXMLListHandling

|  |  |  |
| --- | --- | --- |
|  | testRemoveListItem | 0.001 s |
|  | testAddListItem | 0 s |
|  | testIncompatibleListDelimiterOnSaving | 0.001 s |
|  | testSaveNoChanges | 0 s |
|  | testMixedList | 0.001 s |

<a id="surefire--testdefaultparametersmanager"></a>

### TestDefaultParametersManager

|  |  |  |
| --- | --- | --- |
|  | testRegisterDefaultsHandlerNoClass | 0.001 s |
|  | testUnregisterDefaultsHandlerAll | 0 s |
|  | testApplyDefaults | 0 s |
|  | testApplyDefaultsStartClass | 0 s |
|  | testInitializeParametersNull | 0 s |
|  | testApplyDefaultsOnSubClass | 0 s |
|  | testApplyDefaultsMultipleHandlers | 0 s |
|  | testRegisterDefaultsHandlerNoHandler | 0 s |
|  | testUnregisterDefaultsHandlerSpecific | 0 s |

<a id="surefire--testmanagedreloadingdetector"></a>

### TestManagedReloadingDetector

|  |  |  |
| --- | --- | --- |
|  | testReloadingPerformed | 0 s |
|  | testRefresh | 0 s |
|  | testReloadingRequiredInitial | 0 s |

<a id="surefire--testfilehandler"></a>

### TestFileHandler

|  |  |  |
| --- | --- | --- |
|  | testLocateUnknownFile | 0.004 s |
|  | testLoadFromFileNoContent | 0.001 s |
|  | testSettingFileNames | 0 s |
|  | testSaveToFileNameURLException | 0.002 s |
|  | testLocationChangedEncoding | 0 s |
|  | testSaveFileLocatorAwareToStream | 0.001 s |
|  | testAssignNullHandler | 0 s |
|  | testSaveFileLocatorAwareToWriter | 0 s |
|  | testLoadFromURL | 0.015 s |
|  | testSetFileSystemNull | 0 s |
|  | testResetFileSystem | 0.003 s |
|  | testSetURLFileScheme | 0.001 s |
|  | testLocateSuccess | 0.001 s |
|  | testLoadNoLocation | 0 s |
|  | testGetFileSystemDefault | 0.001 s |
|  | testSetFileLocator | 0 s |
|  | testLoadEvents | 0.001 s |
|  | testSetURLWithParams | 0.050 s |
|  | testClearLocation | 0 s |
|  | testLoadFileLocatorAware | 0 s |
|  | testLocationChangedFileSystem | 0 s |
|  | testPathWithPlus | 0.001 s |
|  | testLocationChangedBasePath | 0.001 s |
|  | testLoadInputStreamSupportIOException | 0.003 s |
|  | testSetFileNameFileScheme | 0 s |
|  | testSaveToStream | 0 s |
|  | testSaveToWriter | 0.001 s |
|  | testPathWithSpaces | 0.001 s |
|  | testAssignWithFileBased | 0 s |
|  | testSaveToWriterNoContent | 0.001 s |
|  | testLoadDirectoryFile | 0 s |
|  | testSetBasePath | 0 s |
|  | testLoadFromFilePath | 0.001 s |
|  | testLoadFileLocatorAwareReader | 0 s |
|  | testLoadFileLocatorAwareStream | 0 s |
|  | testIsLocationDefinedFalse | 0.001 s |
|  | testLocationChangedFileName | 0 s |
|  | testSaveEvents | 0 s |
|  | testLoadInputStreamSupport | 0 s |
|  | testSaveNoLocation | 0 s |
|  | testInitFromMap | 0.001 s |
|  | testLocationChangedLocator | 0 s |
|  | testSaveSynchronized | 0 s |
|  | testLoadNoContent | 0 s |
|  | testSaveToFile | 0 s |
|  | testLocateUndefinedLocator | 0.001 s |
|  | testSetBasePathFileScheme | 0 s |
|  | testLocatorAwareEncoding | 0 s |
|  | testSaveToFileName | 0.001 s |
|  | testSetFileName | 0 s |
|  | testGetBasePathUndefined | 0 s |
|  | testSaveToURL | 0.001 s |
|  | testIsLocationDefinedFileName | 0 s |
|  | testGetFileNameUndefined | 0 s |
|  | testLocationChangedURL | 0.001 s |
|  | testSaveToFileNameLocation | 0.001 s |
|  | testLoadFromReaderIOException | 0.001 s |
|  | testLoadFromFilePathWithURLDefined | 0.001 s |
|  | testLoadFromFile | 0 s |
|  | testSaveFileLocatorAware | 0.001 s |
|  | testLoadFromClassPath | 0 s |
|  | testSetURLNull | 0.001 s |
|  | testGetLocationStrategyDefault | 0 s |
|  | testLoadFromURLLocation | 0 s |
|  | testIsLocationDefinedBasePathOnly | 0.001 s |
|  | testIsLocationDefinedFile | 0 s |
|  | testIsLocationDefinedPath | 0.001 s |
|  | testLoadSynchronized | 0 s |
|  | testLocationChangedFile | 0.001 s |
|  | testLocationChangedPath | 0 s |
|  | testSetLocationStrategy | 0 s |
|  | testSetFileLocatorNull | 0 s |
|  | testIsLocationDefinedURL | 0 s |
|  | testSetFile | 0 s |
|  | testSetPath | 0 s |
|  | testSetURL | 0.001 s |
|  | testLoadDirectoryString | 0 s |
|  | testLoadFromReader | 0.001 s |
|  | testInitPropertiesMultiThreaded | 0.002 s |
|  | testSaveToWriterIOException | 0 s |
|  | testLoadFromStream | 0.002 s |
|  | testSaveToURLLocation | 0.001 s |
|  | testAddFileHandlerListenerNull | 0 s |
|  | testLoadFromFileNameLocation | 0 s |
|  | testSaveToFileNameURLNotResolved | 0.001 s |

<a id="surefire--testjakartaservletconfiguration"></a>

### TestJakartaServletConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.001 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0.001 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testsubsetconfiguration848"></a>

### TestSubsetConfiguration848

|  |  |  |
| --- | --- | --- |
|  | testSubsetWithJSONConfiguration | 0.001 s |
|  | testSubsetConfigurationWithIndexAndDelimiter | 0.001 s |

<a id="surefire--testbaseconfigurationbuilderprovider"></a>

### TestBaseConfigurationBuilderProvider

|  |  |  |
| --- | --- | --- |
|  | testGetBuilderNotReloading | 0 s |
|  | testGetBuilderNoFailOnInit | 0 s |
|  | testGetBuilderAllowFailOnInit | 0 s |
|  | testGetBuilderReloading | 0 s |
|  | testInitNoParameterClasses | 0 s |
|  | testInitNoBuilderClass | 0 s |
|  | testGetParameterClassesModify | 0 s |
|  | testGetReloadingBuilderNotSupported | 0.001 s |
|  | testInitNoConfigurationClass | 0 s |

<a id="surefire--testbaseconfigurationxmlreader"></a>

### TestBaseConfigurationXMLReader

|  |  |  |
| --- | --- | --- |
|  | testParse | 0.003 s |
|  | testParseSAXException | 0.001 s |
|  | testParseIOException | 0 s |
|  | testSetRootName | 0 s |

<a id="surefire--testmergecombiner"></a>

### TestMergeCombiner

|  |  |  |
| --- | --- | --- |
|  | testInit | 0.001 s |
|  | testOverrideValues | 0.002 s |
|  | testListFromSecondStructure | 0.002 s |
|  | testMerge | 0.002 s |
|  | testAttributes | 0.003 s |
|  | testCombinedTable | 0.002 s |
|  | testSimpleValues | 0.001 s |
|  | testListFromFirstStructure | 0.002 s |

<a id="surefire--testdefaultexpressionenginesymbols"></a>

### TestDefaultExpressionEngineSymbols

|  |  |  |
| --- | --- | --- |
|  | testEqualsOtherClass | 0.001 s |
|  | testEqualsFalse | 0 s |
|  | testToString | 0.001 s |
|  | testDefaultSymbols | 0 s |
|  | testEqualsNull | 0.001 s |
|  | testEqualsTrue | 0 s |

<a id="surefire--testeventtype"></a>

### TestEventType

|  |  |  |
| --- | --- | --- |
|  | testToString | 0 s |

<a id="surefire--testpatternsubtreeconfiguration"></a>

### TestPatternSubtreeConfiguration

|  |  |  |
| --- | --- | --- |
|  | testSaveNotFileBased | 0.003 s |
|  | testReadNotFileBased | 0.001 s |
|  | testMultiConfiguration | 0.002 s |

<a id="surefire--testcompositeconfiguration"></a>

### TestCompositeConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetListWithInterpolation | 0.001 s |
|  | testGetKeys2PreservesOrder | 0.001 s |
|  | testStringArrayInterpolation | 0 s |
|  | testInterpolationArrayReference | 0.001 s |
|  | testInterpolationInMultipleConfigs | 0 s |
|  | testCantRemoveMemoryConfig | 0.001 s |
|  | testGetPropertyMissing | 0.001 s |
|  | testGetSourceSingle | 0 s |
|  | testSubsetCanResolve | 0.001 s |
|  | testClone | 0 s |
|  | testAddRemoveConfigurations | 0.001 s |
|  | testGetKeysPreservesOrder | 0 s |
|  | testList | 0.001 s |
|  | testSetListDelimiter | 0 s |
|  | testEventSetProperty | 0.001 s |
|  | testInstanciateWithCollection | 0.001 s |
|  | testGetList | 0 s |
|  | testUseChildConfigAsInMemoryConfig | 0.001 s |
|  | testGettingSubset | 0 s |
|  | testMultipleTypesOfConfigs | 0.001 s |
|  | testAddingProperty | 0.001 s |
|  | testPropertyExistsInOnlyOneConfig | 0 s |
|  | testGetSourceInMemory | 0.001 s |
|  | testThrowExceptionOnMissing | 0 s |
|  | testCloneNotSupported | 0.001 s |
|  | testListInterpolation | 0 s |
|  | testGetStringWithDefaults | 0.001 s |
|  | testRemoveConfigurationSynchronized | 0 s |
|  | testEventClearProperty | 0.001 s |
|  | testAddFirstRemoveConfigurations | 0 s |
|  | testGetNumberOfConfigurationsSynchronized | 0.001 s |
|  | testGetProperty | 0 s |
|  | testGetSourceNull | 0.001 s |
|  | testCheckingInMemoryConfiguration | 0 s |
|  | testSetListDelimiterInMemoryConfigNonBaseConfig | 0.001 s |
|  | testReplaceInMemoryConfig | 0 s |
|  | testEventAddProperty | 0.001 s |
|  | testGetConfigurationSynchronized | 0 s |
|  | testAddConfigurationSynchronized | 0 s |
|  | testCloneEventListener | 0 s |
|  | testGetSourceMultiple | 0 s |
|  | testGettingConfiguration | 0.001 s |
|  | testGetInMemoryConfigurationSynchronized | 0 s |
|  | testClearingProperty | 0.001 s |
|  | testDefaultValueWhenKeyMissing | 0 s |
|  | testSettingMissingProperty | 0.001 s |
|  | testGetPropertyWIncludes | 0 s |
|  | testSetListDelimiterAfterClear | 0.003 s |
|  | testGetStringArrayWithInterpolation | 0.001 s |
|  | testGetSourceUnknown | 0 s |
|  | testStringArray | 0.001 s |
|  | testCloneInterpolation | 0 s |

<a id="surefire--testmultifileconfigurationbuilder"></a>

### TestMultiFileConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testFileNotFoundAllowFailOnInit | 0 s |
|  | testRecursiveInterpolation | 0.001 s |
|  | testGetManagedBuilderClonedParameters | 0 s |
|  | testAddConfigurationListener | 0 s |
|  | testSchemaValidationError | 0.640 s |
|  | testGetConfiguration | 0.003 s |
|  | testRemoveBuilderListenerOnReset | 0.001 s |
|  | testCaching | 0.001 s |
|  | testManagedConfigurationSettings | 0.001 s |
|  | testNoPattern | 0 s |
|  | testInterpolatorFromParameters | 0.001 s |
|  | testFileNotFound | 0 s |
|  | testCachingWithReset | 0.001 s |
|  | testBuilderListenerReset | 0.001 s |
|  | testInterpolatorReset | 0 s |
|  | testBuilderListenerOtherTypes | 0 s |

<a id="surefire--testyamlconfiguration"></a>

### TestYAMLConfiguration

|  |  |  |
| --- | --- | --- |
|  | testCopyConstructor | 0.014 s |
|  | testSave | 0.005 s |
|  | testGetPropertyInteger | 0.002 s |
|  | testGetPropertyDictionary | 0.001 s |
|  | testObjectCreationFromReader | 0.001 s |
|  | testGetPropertyNested | 0.001 s |
|  | testObjectCreationFromStream | 0.001 s |
|  | testGetPropertySimple | 0.001 s |
|  | testGetPropertySubset | 0 s |
|  | testGetPropertyNestedWithList | 0.001 s |
|  | testGetPropertyVeryNestedProperties | 0.001 s |
|  | testDoubleStringValues | 0.001 s |

<a id="surefire--testclasspathlocationstrategy"></a>

### TestClasspathLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testLocateSuccess | 0.002 s |
|  | testLocateFailed | 0 s |
|  | testLocateNoFileName | 0 s |

<a id="surefire--testabsolutenamelocationstrategy"></a>

### TestAbsoluteNameLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testNoAbsoluteFileName | 0 s |
|  | testNoFileName | 0 s |
|  | testExistingAbsoluteFile | 0 s |
|  | testNonExistingAbsoluteFile | 0 s |

<a id="surefire--testbasicbuilderparameters"></a>

### TestBasicBuilderParameters

|  |  |  |
| --- | --- | --- |
|  | testInheritFromUndefinedProperties | 0.001 s |
|  | testMergeNull | 0 s |
|  | testFetchInterpolatorSpecificationInvalidMapValue | 0 s |
|  | testSetConversionHandler | 0 s |
|  | testMerge | 0.005 s |
|  | testCloneDefaultLookups | 0 s |
|  | testSetDefaultLookups | 0 s |
|  | testSetParentInterpolator | 0 s |
|  | testSetListDelimiter | 0 s |
|  | testFetchBeanHelperNoSet | 0 s |
|  | testSetConfigurationDecoder | 0 s |
|  | testCloneValues | 0.005 s |
|  | testSetPrefixLookups | 0 s |
|  | testFetchInterpolatorSpecificationInvalidDataType | 0 s |
|  | testSetLookupsAndInterpolator | 0 s |
|  | testSetInterpolator | 0 s |
|  | testFetchInterpolatorSpecification | 0 s |
|  | testFetchInterpolatorSpecificationInvalidMapKey | 0 s |
|  | testSetBeanHelper | 0 s |
|  | testFetchInterpolatorSpecificationInvalidCollectionValue | 0 s |
|  | testClonePrefixLookups | 0 s |
|  | testInheritFromNull | 0 s |
|  | testSetSynchronizer | 0.001 s |
|  | testFetchInterpolatorSpecificationEmpty | 0 s |
|  | testSetPrefixLookupsNull | 0 s |
|  | testSetLogger | 0 s |
|  | testGetParametersDefensiveCopy | 0 s |
|  | testFetchBeanHelperNullMap | 0 s |
|  | testDefaults | 0 s |
|  | testFetchInterpolatorSpecificationNull | 0 s |
|  | testSetDefaultLookupsNull | 0 s |
|  | testInheritFrom | 0 s |
|  | testFetchInterpolatorSpecificationWithInterpolator | 0 s |
|  | testSetThrowExceptionOnMissing | 0 s |

<a id="surefire--testpropertylistconfiguration"></a>

### TestPropertyListConfiguration

|  |  |  |
| --- | --- | --- |
|  | testAddDataProperty | 0.005 s |
|  | testEmptyArray | 0.001 s |
|  | testParseDateNoNumber | 0.002 s |
|  | testSetDataProperty | 0.002 s |
|  | testParseDateNull | 0.001 s |
|  | testArray | 0.001 s |
|  | testData | 0.001 s |
|  | testDate | 0.001 s |
|  | testLoad | 0.001 s |
|  | testSave | 0.003 s |
|  | testSaveEmptyDictionary | 0.002 s |
|  | testDictionaryArray | 0.002 s |
|  | testFormatDate | 0.001 s |
|  | testLoadWithError | 0.001 s |
|  | testDictionary | 0 s |
|  | testQuotedString | 0 s |
|  | testQuoteString | 0 s |
|  | testInitCopy | 0.001 s |
|  | testParseDateTooShort | 0.001 s |
|  | testNestedDictionaries | 0.001 s |
|  | testNestedArrays | 0.001 s |
|  | testString | 0.001 s |
|  | testParseDateInvalidChar | 0.001 s |

<a id="surefire--testservletconfiguration"></a>

### TestServletConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.003 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0.001 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testbasicconfigurationbuilder"></a>

### TestBasicConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testAddParameters | 0 s |
|  | testInitNoClass | 0 s |
|  | testResetResult | 0 s |
|  | testSetParameters | 0 s |
|  | testInitializationErrorAllowed | 0 s |
|  | testReservedParameter | 0 s |
|  | testGetParametersModify | 0 s |
|  | testReset | 0 s |
|  | testGetResultDeclarationInvalidBeanClass | 0 s |
|  | testAddConfigurationListener | 0 s |
|  | testConnectToReloadingControllerNull | 0 s |
|  | testGetConfiguration | 0 s |
|  | testConfigure | 0 s |
|  | testBeanHelperInConfiguration | 0 s |
|  | testEventListenerConfiguration | 0 s |
|  | testRemoveConfigurationListenersOnReset | 0 s |
|  | testRemoveConfigurationListener | 0 s |
|  | testGetConfigurationConcurrently | 0.001 s |
|  | testInitWithParameters | 0 s |
|  | testAddParametersNull | 0 s |
|  | testConnectToReloadingController | 0.001 s |
|  | testResetParameters | 0 s |
|  | testInitializationErrorNotAllowed | 0 s |
|  | testInitializableCalled | 0 s |
|  | testInitWithParametersNull | 0 s |
|  | testInitWithParametersDefensiveCopy | 0.001 s |
|  | testCopyEventListeners | 0 s |

<a id="surefire--testdefaultfilesystem"></a>

### TestDefaultFileSystem

|  |  |  |
| --- | --- | --- |
|  | testDefaultLogger | 0 s |
|  | testSetLogger | 0 s |
|  | testGetOutputStreamInvalidPath | 0.001 s |

<a id="surefire--testsubsetconfiguration"></a>

### TestSubsetConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetChildKey | 0 s |
|  | testClear | 0.001 s |
|  | testGetParentKey | 0 s |
|  | testInterpolator | 0.001 s |
|  | testGetKeys | 0 s |
|  | testGetList | 0.001 s |
|  | testThrowExceptionOnMissing | 0.001 s |
|  | testConstructNullParent | 0 s |
|  | testPrefixDelimiter | 0 s |
|  | testSetProperty | 0 s |
|  | testGetProperty | 0.001 s |
|  | testSetPrefix | 0 s |
|  | testSetListDelimiterHandlerParentNotSupported | 0.134 s |
|  | testInterpolationForKeysOfTheParent | 0 s |
|  | testGetParent | 0 s |
|  | testGetPrefix | 0 s |
|  | testPrefixDelimiterNegativeTest | 0.001 s |
|  | testNested | 0.036 s |
|  | testLocalLookupsInInterpolatorAreInherited | 0.001 s |
|  | testSetListDelimiterHandlerInParent | 0 s |
|  | testListDelimiterHandling | 0 s |
|  | testGetKeysWithPrefix | 0.001 s |
|  | testGetListDelimiterHandlerFromParent | 0 s |

<a id="surefire--testcombinedconfigurationbuildervfs"></a>

### TestCombinedConfigurationBuilderVFS

|  |  |  |
| --- | --- | --- |
|  | testLoadAdditional | 0.003 s |
|  | testConfigurationBuilderProviderInheritBasicProperties | 0.005 s |
|  | testLoadOptional | 0.003 s |
|  | testMultiTenentConfigurationReloading | 5.044 s |
|  | testReloadingBuilder | 0.004 s |
|  | testEnvironmentProperties | 0.007 s |
|  | testGetChildBuilders | 0.004 s |
|  | testGetNamedBuilder | 0.003 s |
|  | testGetNamedBuilderBeforeConfigurationAccess | 0 s |
|  | testConfigurationBuilderProviderInheritEventListeners | 0.003 s |
|  | testMultiTenentConfigurationProperties | 0.003 s |
|  | testINIConfiguration | 0.008 s |
|  | testCombinedConfigurationAttributes | 0.002 s |
|  | testDefaultBasePathFromDefinitionBuilder | 0.002 s |
|  | testReactOnSubBuilderChange | 0.001 s |
|  | testNoDefinitionBuilder | 0 s |
|  | testBasePathForChildConfigurations | 0 s |
|  | testProviderInDefinitionConfig | 0.001 s |
|  | testCustomEntityResolver | 0.002 s |
|  | testCombinedConfigurationNoAdditional | 0.001 s |
|  | testSystemProperties | 0.001 s |
|  | testConcurrentReadAccessWithoutSynchronizer | 0.003 s |
|  | testCustomFileSystemForSubConfig | 0.002 s |
|  | testMultiTenentConfiguration | 0.002 s |
|  | testConfigurationBuilderProviderInheritCustomProviders | 0.001 s |
|  | testConfigurationBuilderProvider | 0.002 s |
|  | testConfigurationBuilderProviderInheritBasePath | 0.001 s |
|  | testChildBuildersAreInitializedOnlyOnce | 0.003 s |
|  | testBuilderNamesBeforeConfigurationAccess | 0 s |
|  | testConfigureResult | 0 s |
|  | testInitChildBuilderParametersDefaultChildProperties | 0.002 s |
|  | testCustomBuilderProvider | 0.001 s |
|  | testCustomResultConfiguration | 0.001 s |
|  | testResetBuilder | 0.001 s |
|  | testJndiConfiguration | 0.004 s |
|  | testInheritProperties | 0.002 s |
|  | testDefaultBasePathInParameters | 0.001 s |
|  | testBuilderNames | 0.001 s |
|  | testSuppressChildBuilderPropertyInheritance | 0.001 s |
|  | testConfigureEntityResolverWithProperties | 0 s |
|  | testCustomFileSystem | 0.001 s |
|  | testRootNodeInitializedAfterCreation | 0.001 s |
|  | testLoadConfiguration | 0.002 s |
|  | testLoadOptionalForceCreate | 0 s |
|  | testBuilderNamesManipulate | 0.002 s |
|  | testCustomLookup | 0.001 s |
|  | testGetNamedBuilderUnknown | 0.002 s |
|  | testCombinedConfigurationListNodes | 0.001 s |
|  | testRemoveSubBuilderListener | 0.001 s |
|  | testInterpolationOverMultipleSources | 0.002 s |
|  | testLoadOptionalWithException | 0.001 s |
|  | testSetConfigurationBasePath | 0 s |

<a id="surefire--testpropertiessequence"></a>

### TestPropertiesSequence

|  |  |  |
| --- | --- | --- |
|  | testConfigurationValuesInSameOrderFromFile | 0.002 s |
|  | testConfigurationValuesInSameOrderWithManualAdd | 0.002 s |
|  | testMappingInSameOrder | 0.001 s |

<a id="surefire--testenvironmentconfiguration"></a>

### TestEnvironmentConfiguration

|  |  |  |
| --- | --- | --- |
|  | testClear | 0 s |
|  | testInit | 0 s |
|  | testClearProperty | 0.001 s |
|  | testSetProperty | 0 s |
|  | testAddProperty | 0 s |

<a id="surefire--testbasicconfigurationbuilderevents"></a>

### TestBasicConfigurationBuilderEvents

|  |  |  |
| --- | --- | --- |
|  | testRemoveEventListenerNotExisting | 0 s |
|  | testResultCreatedEventNoConfiguration | 0.001 s |
|  | testConfigurationRequestEvent | 0 s |
|  | testConfigurationRequestEventType | 0 s |
|  | testResultCreatedEventType | 0 s |
|  | testBuilderResetEvent | 0 s |
|  | testResultCreatedEvent | 0 s |
|  | testBuilderResetEventType | 0 s |
|  | testResetOnConfigurationRequestEvent | 0 s |
|  | testBuilderEventType | 0 s |
|  | testRemoveEventListener | 0 s |

<a id="surefire--testconfigurationlookup"></a>

### TestConfigurationLookup

|  |  |  |
| --- | --- | --- |
|  | testInitNoConfig | 0 s |
|  | testLookupNotFound | 0 s |
|  | testLookupComplex | 0 s |
|  | testLookupNotFoundEx | 0 s |
|  | testLookupSuccess | 0 s |

<a id="surefire--testfileextensionconfigurationbuilderprovider"></a>

### TestFileExtensionConfigurationBuilderProvider

|  |  |  |
| --- | --- | --- |
|  | testInitNoDefaultConfigClass | 0 s |
|  | testDetermineConfigurationClassNoExtension | 0.006 s |
|  | testDetermineConfigurationClassMatchCase | 0 s |
|  | testDetermineConfigurationClassExtensionMatch | 0 s |
|  | testInitNoExt | 0 s |
|  | testInitSuper | 0 s |
|  | testInitNoMatchingConfigClass | 0.001 s |
|  | testDetermineConfigurationClassNoParams | 0 s |
|  | testDeterminieConfigurationClassNoFileName | 0 s |
|  | testDetermineConfigurationClassExtensionNoMatch | 0 s |

<a id="surefire--testexprlookup"></a>

### TestExprLookup

|  |  |  |
| --- | --- | --- |
|  | testLookupNoConfigurationInterpolator | 0.009 s |
|  | testLookupNullExpression | 0.004 s |
|  | testGetVariablesDefensiveCopy | 0.001 s |
|  | testLookupLog4j1 | 0 s |
|  | testGetVariables | 0 s |
|  | testLookup | 0.002 s |
|  | testLookupNonStringExpression | 0.001 s |

<a id="surefire--testsubsetconfigurationevents"></a>

### TestSubsetConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0 s |
|  | testSetPropertyEventWithDetails | 0 s |
|  | testSetPropertyEvent | 0 s |
|  | testClearPropertyEventWithDetails | 0 s |
|  | testClearPropertyEvent | 0 s |
|  | testAddPropertyEventWithDetails | 0 s |
|  | testClearEventWithDetails | 0 s |
|  | testAddPropertyEvent | 0 s |

<a id="surefire--testcombinedbeandeclaration"></a>

### TestCombinedBeanDeclaration

|  |  |  |
| --- | --- | --- |
|  | testGetBeanClassNameDefined | 0 s |
|  | testGetBeanFactoryNameUndefined | 0.001 s |
|  | testGetBeanFactoryNameDefined | 0 s |
|  | testGetConstructorArgsUndefined | 0 s |
|  | testGetNestedBeanDeclarationsNull | 0 s |
|  | testGetBeanProperties | 0 s |
|  | testGetBeanFactoryParameterDefined | 0 s |
|  | testGetBeanClassNameUndefined | 0.001 s |
|  | testGetConstructorArgsDefined | 0 s |
|  | testGetBeanFactoryParameterUndefined | 0 s |
|  | testGetNestedBeanDeclarations | 0 s |
|  | testGetBeanPropertiesNull | 0 s |

<a id="surefire--testjakartaservletfilterconfiguration"></a>

### TestJakartaServletFilterConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0.001 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testbeanhelper"></a>

### TestBeanHelper

|  |  |  |
| --- | --- | --- |
|  | testDefaultInstance | 0 s |
|  | testRegisterBeanFactory | 0 s |
|  | testDeregisterBeanFactoryNonExisting | 0 s |
|  | testCreateBeanWithException | 0 s |
|  | testCreateWrapDynaBean | 0.001 s |
|  | testCreateBeanWithNullDeclaration | 0 s |
|  | testInitWithBeanFactory | 0.002 s |
|  | testCreateBeanWithParameter | 0.001 s |
|  | testCreateBeanWithFactoryDefaultClass | 0 s |
|  | testCreateBeanWithListChildBean | 0 s |
|  | testRegisteredFactoriesEmptyForNewInstance | 0 s |
|  | testDeregisterBeanFactoryNull | 0 s |
|  | testCreateBean | 0 s |
|  | testDefaultBeanFactory | 0 s |
|  | testCreateBeanWithDefaultFactory | 0 s |
|  | testCreateBeanWithDefaultClass | 0 s |
|  | testInitBean | 0 s |
|  | testCreateBeanWithNoClass | 0 s |
|  | testInitBeanWithNoData | 0 s |
|  | testRegisterBeanFactoryNull | 0 s |
|  | testCreateWrapDynaBeanNull | 0 s |
|  | testRegisterBeanFactoryNullName | 0 s |
|  | testDeregisterBeanFactory | 0 s |
|  | testInitBeanWithInvalidProperty | 0 s |
|  | testCopyProperties | 0.001 s |
|  | testCreateBeanWithInvalidClass | 0 s |
|  | testCreateBeanWithUnknownFactory | 0 s |

<a id="surefire--testthreesomeconfiguration"></a>

### TestThreesomeConfiguration

|  |  |  |
| --- | --- | --- |
|  | testList1 | 0 s |
|  | testList2 | 0 s |
|  | testList3 | 0 s |

<a id="surefire--testparameters"></a>

### TestParameters

|  |  |  |
| --- | --- | --- |
|  | testDatabase | 0 s |
|  | testProperties | 0.002 s |
|  | testRegisterDefaultsHandlerNoStartClass | 0.003 s |
|  | testApplyDefaults | 0 s |
|  | testXml | 0.001 s |
|  | testBasic | 0 s |
|  | testDefaultParametersManager | 0 s |
|  | testJndi | 0 s |
|  | testFileBasedInheritance | 0 s |
|  | testProxyObjectMethods | 0 s |
|  | testFileBased | 0 s |
|  | testMultiFile | 0 s |
|  | testPropertiesInheritance | 0 s |
|  | testCombined | 0 s |
|  | testXmlInheritance | 0 s |
|  | testRegisterDefaultsHandlerWithStartClass | 0 s |
|  | testInheritance | 0 s |
|  | testHierarchical | 0.001 s |
|  | testHierarchicalInheritance | 0 s |

<a id="surefire--testjakartaservletrequestconfiguration"></a>

### TestJakartaServletRequestConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.007 s |
|  | testList | 0 s |
|  | testSize | 0.001 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testListWithEscapedElements | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testxmlpropertylistconfigurationevents"></a>

### TestXMLPropertyListConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0.115 s |
|  | testSetPropertyEventWithDetails | 0.004 s |
|  | testSetPropertyEvent | 0.003 s |
|  | testClearPropertyEventWithDetails | 0.003 s |
|  | testClearPropertyEvent | 0.002 s |
|  | testAddPropertyEventWithDetails | 0.002 s |
|  | testClearEventWithDetails | 0.002 s |
|  | testAddPropertyEvent | 0.002 s |
|  | testSetByteArrayPropertyEvent | 0.002 s |
|  | testAddByteArrayPropertyEvent | 0.003 s |

<a id="surefire--testxmlbeandeclaration"></a>

### TestXMLBeanDeclaration

|  |  |  |
| --- | --- | --- |
|  | testGetBeanPropertiesEmpty | 0 s |
|  | testGetBeanFactoryNameUndefined | 0 s |
|  | testInitFromNullConfiguration | 0 s |
|  | testInitFromUndefinedKey | 0 s |
|  | testGetBeanClassName | 0 s |
|  | testGetBeanFactoryParameterUndefinedWithEx | 0 s |
|  | testGetBeanFactoryParameter | 0 s |
|  | tetGetBeanClassNameDefaultOverride | 0 s |
|  | testGetInterpolatedBeanProperties | 0.001 s |
|  | testGetBeanClassNameUndefinedWithEx | 0 s |
|  | testGetNestedBeanDeclarationsEmpty | 0 s |
|  | testInterpolateNoInterpolator | 0 s |
|  | testGetConstructorArgs | 0 s |
|  | testInitFromMultiValueKey | 0 s |
|  | testGetBeanFactoryName | 0 s |
|  | testGetBeanPropertiesWithReservedAttributes | 0 s |
|  | testGetBeanProperties | 0 s |
|  | testGetNestedBeanDeclarationsReservedCharacter | 0 s |
|  | testGetBeanClassNameUndefined | 0 s |
|  | testGetNestedBeanDeclarationsFactoryMethod | 0 s |
|  | testGetBeanFactoryNameUndefinedWithEx | 0 s |
|  | testGetBeanClassNameFromDefault | 0 s |
|  | testGetBeanFactoryParameterUndefined | 0 s |
|  | testGetNestedBeanDeclarations | 0.001 s |
|  | testGetInterpolatedConstructorArgs | 0 s |
|  | testInitFromNullConfigurationAndKey | 0 s |
|  | testInitFromUndefinedKeyOptional | 0 s |
|  | testGetConstructorArgsNullArg | 0 s |

<a id="surefire--testfilelocatorutils"></a>

### TestFileLocatorUtils

|  |  |  |
| --- | --- | --- |
|  | testFileFromURLWithPlus | 0 s |
|  | testLocateSuccessWithStrategyDefaultFileSystem | 0 s |
|  | testConvertToURIException | 0.001 s |
|  | testPutNoMap | 0 s |
|  | testLocateNullLocator | 0 s |
|  | testDefaultFileLocationStrategy | 0 s |
|  | testFromMapNoMap | 0 s |
|  | testObtainLocationStrategySetInLocator | 0 s |
|  | testGetFile | 0 s |
|  | testObtainLocationStrategyNotSetInLocator | 0 s |
|  | testFileFromURLWithEncodedPercent | 0 s |
|  | testObtainFileSystemNullLocator | 0 s |
|  | testGetBasePath | 0 s |
|  | testIsLocationDefinedFalse | 0 s |
|  | testPutNoLocator | 0 s |
|  | testFullyInitializedLocatorFileName | 0.002 s |
|  | testObtainFileSystemSetInLocator | 0 s |
|  | testFullyInitializedLocatorUndefined | 0 s |
|  | testConvertFileToURL | 0.001 s |
|  | testGetFileName | 0 s |
|  | testFileFromURLNull | 0 s |
|  | testIsLocationDefinedFileName | 0 s |
|  | testFullyInitializedLocatorURL | 0.002 s |
|  | testFullyInitializedLocatorLocateFails | 0 s |
|  | testLocateSuccessWithStrategyAndFileSystem | 0 s |
|  | testIsLocationDefinedNull | 0 s |
|  | testFullyInitializedLocatorAlreadyComplete | 0 s |
|  | testLocateOrThrowFailed | 0 s |
|  | testLocateSuccessWithDefaults | 0 s |
|  | testIsLocationDefinedURL | 0 s |
|  | testIsFullyInitializedNoBasePath | 0 s |
|  | testStoreFileLocatorInMap | 0 s |
|  | testLocateWithNullTCCL | 0 s |
|  | testObtainFileSystemNotSetInLocator | 0 s |
|  | testObtainLocationStrategyNullLocator | 0 s |
|  | testIsFullyInitializedNull | 0 s |

<a id="surefire--testreloadingcombinedconfigurationbuilderfilebased"></a>

### TestReloadingCombinedConfigurationBuilderFileBased

|  |  |  |
| --- | --- | --- |
|  | testReloadDefinitionFileDefaultBuilder | 0.003 s |
|  | testReloadDefinitionFileExplicitBuilder | 0.001 s |
|  | testReloadFromFile | 0.003 s |
|  | testConcurrentGetAndReload | 0.052 s |

<a id="surefire--testhierarchicalxmlconfiguration"></a>

### TestHierarchicalXMLConfiguration

|  |  |  |
| --- | --- | --- |
|  | testSetRootElementNameWhenLoadedFromFile | 0.001 s |
|  | testSave | 0.002 s |
|  | testXmlNodeTypes | 0.001 s |
|  | testLoadURL | 0.001 s |
|  | testSaveModified | 0.002 s |
|  | testGetProperty | 0 s |
|  | testLoadBasePath1 | 0.001 s |
|  | testLoadBasePath2 | 0.001 s |
|  | testSaveNew | 0.001 s |
|  | testRootElement | 0 s |

<a id="surefire--testconstructorarg"></a>

### TestConstructorArg

|  |  |  |
| --- | --- | --- |
|  | testIsNestedBeanDeclarationFalse | 0.001 s |
|  | testForBeanDeclarationNull | 0 s |
|  | testMatchesWithType | 0 s |
|  | testMatchesNull | 0 s |
|  | testMatchesNoType | 0 s |
|  | testIsNestedBeanDeclarationTrue | 0.002 s |

<a id="surefire--testjakartaservletcontextconfiguration"></a>

### TestJakartaServletContextConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.010 s |
|  | testList | 0.001 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0.001 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0.001 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0.001 s |

<a id="surefire--testnullcompositeconfiguration"></a>

### TestNullCompositeConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetKeys2PreservesOrder | 0.002 s |
|  | testCantRemoveMemoryConfig | 0 s |
|  | testGetPropertyMissing | 0.001 s |
|  | testSubsetCanResolve | 0.001 s |
|  | testAddRemoveConfigurations | 0 s |
|  | testGetKeysPreservesOrder | 0.001 s |
|  | testList | 0.001 s |
|  | testGetList | 0 s |
|  | testGettingSubset | 0.001 s |
|  | testMultipleTypesOfConfigs | 0.001 s |
|  | testAddingProperty | 0 s |
|  | testPropertyExistsInOnlyOneConfig | 0.001 s |
|  | testThrowExceptionOnMissing | 0.001 s |
|  | testGetStringWithDefaults | 0 s |
|  | testGetProperty | 0.001 s |
|  | testCheckingInMemoryConfiguration | 0 s |
|  | testGettingConfiguration | 0.001 s |
|  | testClearingProperty | 0.001 s |
|  | testDefaultValueWhenKeyMissing | 0.001 s |
|  | testSettingMissingProperty | 0 s |
|  | testGetVector | 0.001 s |
|  | testGetPropertyWIncludes | 0 s |
|  | testStringArray | 0.001 s |

<a id="surefire--testxmlconfigurationevents"></a>

### TestXMLConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0 s |
|  | testSetPropertyEventWithDetails | 0 s |
|  | testSetPropertyEvent | 0 s |
|  | testClearPropertyEventWithDetails | 0 s |
|  | testClearPropertyEvent | 0 s |
|  | testAddPropertyEventWithDetails | 0 s |
|  | testClearEventWithDetails | 0 s |
|  | testAddPropertyEvent | 0 s |
|  | testAddNodesEvent | 0 s |
|  | testSubConfigurationChangedEventNotConnected | 0 s |
|  | testAddNodesEmptyEvent | 0 s |
|  | testSubConfigurationChangedEventConnected | 0 s |
|  | testClearTreeEvent | 0.001 s |

<a id="surefire--testpropertiesconfigurationevents"></a>

### TestPropertiesConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0 s |
|  | testSetPropertyEventWithDetails | 0 s |
|  | testSetPropertyEvent | 0 s |
|  | testClearPropertyEventWithDetails | 0 s |
|  | testClearPropertyEvent | 0 s |
|  | testAddPropertyEventWithDetails | 0 s |
|  | testClearEventWithDetails | 0 s |
|  | testAddPropertyEvent | 0 s |

<a id="surefire--testpropertiesbuilderparametersimpl"></a>

### TestPropertiesBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testSetIOFactory | 0 s |
|  | testSetIOFactoryProperty | 0 s |
|  | testSetIncludesAllowed | 0.001 s |
|  | testSetLayout | 0 s |
|  | testInheritFrom | 0 s |
|  | testSetIncludeListener | 0 s |
|  | testSetIncludeListenerProperty | 0 s |
|  | testBeanPropertiesAccess | 0 s |

<a id="surefire--testfilelocator"></a>

### TestFileLocator

|  |  |  |
| --- | --- | --- |
|  | testFileLocatorEqualsFalse | 0 s |
|  | testCreateFileLocatorUndefined | 0 s |
|  | testFileLocatorEqualsNull | 0 s |
|  | testFileLocatorEqualsTrue | 0 s |
|  | testFileLocatorToString | 0 s |
|  | testFileLocatorEqualsOtherClass | 0 s |
|  | testCreateFileLocatorFromSource | 0 s |
|  | testCreateFileLocator | 0 s |

<a id="surefire--testpropertiesconfiguration"></a>

### TestPropertiesConfiguration

|  |  |  |
| --- | --- | --- |
|  | testCopyAndSave | 0.001 s |
|  | testSaveToCustomURL | 0.002 s |
|  | testPropertyLoadedInclude | 0.001 s |
|  | testBackslashEscapingInLists | 0 s |
|  | testCompress840PriorityQueue(int)[1] | 0.002 s |
|  | testCompress840PriorityQueue(int)[2] | 0 s |
|  | testCompress840PriorityQueue(int)[3] | 0 s |
|  | testCompress840PriorityQueue(int)[4] | 0.001 s |
|  | testCompress840PriorityQueue(int)[5] | 0.001 s |
|  | testSetFooterSynchronized | 0 s |
|  | testLoadIncludeInterpol | 0.001 s |
|  | testSaveWithBasePath | 0 s |
|  | testIsCommentLine | 0 s |
|  | testJupRead | 0.003 s |
|  | testSlashEscaping | 0.001 s |
|  | testCompress840ArrayListCycle(int)[1] | 0.001 s |
|  | testCompress840ArrayListCycle(int)[2] | 0 s |
|  | testCompress840ArrayListCycle(int)[3] | 0 s |
|  | testCompress840ArrayListCycle(int)[4] | 0 s |
|  | testCompress840ArrayListCycle(int)[5] | 0.001 s |
|  | testEscapedKeyValueSeparator | 0.001 s |
|  | testDisableListDelimiter | 0 s |
|  | testLoadIncludeFileViaFileSystem | 0.001 s |
|  | testSetIOFactoryNull | 0.001 s |
|  | testLoadViaPropertyWithBasePath2 | 0 s |
|  | testEmptyNoSeparator | 0 s |
|  | testUnescapeJava | 0 s |
|  | testIncludeLoadCyclicalMultiStepReferenceFail | 0.001 s |
|  | testLoadUnexistingFile | 0 s |
|  | testClone | 0.001 s |
|  | testEmpty | 0.001 s |
|  | testPropertyLoadedIncludeNotAllowed | 0 s |
|  | testList | 0.001 s |
|  | testLoad | 0 s |
|  | testSave | 0.001 s |
|  | testCompress840ArrayList(int)[1] | 0 s |
|  | testCompress840ArrayList(int)[2] | 0.001 s |
|  | testCompress840ArrayList(int)[3] | 0.001 s |
|  | testCompress840ArrayList(int)[4] | 0 s |
|  | testCompress840ArrayList(int)[5] | 0.001 s |
|  | testSetIOFactoryReader | 0 s |
|  | testLoadIncludeFromClassPath | 0.001 s |
|  | testEscapedKey | 0 s |
|  | testIncludeIncludeLoadAllOnNotFound | 0.001 s |
|  | testChangingListDelimiter | 0.001 s |
|  | testJupWriteUtf8WithoutUnicodeEscapes | 0.001 s |
|  | testNewLineEscaping | 0 s |
|  | testLargeKey | 0.002 s |
|  | testKeyValueSeparators | 0 s |
|  | testSetIOFactoryWriter | 0.001 s |
|  | testReadFooterComment | 0.001 s |
|  | testUnEscapeCharacters | 0 s |
|  | testSaveWithDelimiterParsingDisabled | 0.001 s |
|  | testEscapeQuote | 0 s |
|  | testGetIOFactoryDefault | 0.001 s |
|  | testConfiguration | 0 s |
|  | testIncludeLoadCyclicalMultiStepReferenceIgnore | 0 s |
|  | testMixedArray | 0.001 s |
|  | testSaveToHTTPServerFail | 0.001 s |
|  | testReference | 0 s |
|  | testGetFooterSynchronized | 0.001 s |
|  | testSaveToHTTPServerSuccess | 0.001 s |
|  | testIncludeLoadAllOnLoadException | 0.002 s |
|  | testSetHeaderSynchronized | 0.001 s |
|  | testSetInclude | 0 s |
|  | testIncludeIncludeLoadCyclicalReferenceIgnore | 0.001 s |
|  | testMultipleIncludeFiles | 0.001 s |
|  | testInMemoryCreatedSave | 0 s |
|  | testSetPropertyListWithDelimiterParsingDisabled | 0.001 s |
|  | testIncludeLoadCyclicalReferenceFail | 0.001 s |
|  | testIncludeLoadCyclicalReferenceIgnore | 0 s |
|  | testIncludeIncludeLoadCyclicalReferenceFail | 0 s |
|  | testSaveEscapedEscapingCharacter | 0.001 s |
|  | testCompress840BeanContextSupport | 0.001 s |
|  | testSaveWithDataConfig | 0.001 s |
|  | testJupWrite | 0.001 s |
|  | testMultilines | 0 s |
|  | testGetStringWithEscapedChars | 0.001 s |
|  | testGetStringWithEscapedComma | 0 s |
|  | testComment | 0 s |
|  | testInitFromNonExistingFile | 0.001 s |
|  | testLoadIncludeFromReader | 0 s |
|  | testAppendAndSave | 0.001 s |
|  | testLoadInclude | 0.001 s |
|  | testPropertyLoaded | 0 s |
|  | testLoadFromFile | 0.001 s |
|  | testIncludeInSubDir | 0.002 s |
|  | testFileWithSharpSymbol | 0 s |
|  | testAppend | 0.001 s |
|  | testGetLayout | 0 s |
|  | testCloneNullLayout | 0 s |
|  | testDisableIncludes | 0.001 s |
|  | testCompress840BeanContextServicesSupport | 0 s |
|  | testKeepSeparators | 0 s |
|  | testGetHeaderSynchronized | 0.001 s |
|  | testLoadIncludeOptional | 0.001 s |
|  | testWriteFooterComment | 0 s |
|  | testIncludeLoadAllOnNotFound | 0 s |
|  | testSaveWithDefaultListDelimiterHandler | 0 s |
|  | testCompress840Exception(int)[1] | 0 s |
|  | testCompress840Exception(int)[2] | 0.001 s |
|  | testCompress840Exception(int)[3] | 0.001 s |
|  | testCompress840Exception(int)[4] | 0 s |
|  | testCompress840Exception(int)[5] | 0.001 s |
|  | testClearFooterComment | 0 s |
|  | testLoadViaPropertyWithBasePath | 0.001 s |
|  | testCompress840Path(int)[1] | 0.001 s |
|  | testCompress840Path(int)[2] | 0 s |
|  | testCompress840Path(int)[3] | 0.001 s |
|  | testCompress840Path(int)[4] | 0 s |
|  | testCompress840Path(int)[5] | 0.001 s |
|  | testReadCalledDirectly | 0.001 s |
|  | testLineSeparator | 0 s |
|  | testSaveMissingFileName | 0 s |

<a id="surefire--testconfigurationiteratorattributes"></a>

### TestConfigurationIteratorAttributes

|  |  |  |
| --- | --- | --- |
|  | testIterateSpecificAttribute | 0.001 s |
|  | testIterateUnknownAttribute | 0 s |
|  | testIterateAllAttributes | 0 s |
|  | testIterateNamespaceUnknown | 0.001 s |
|  | testIterateNamespaceWildcard | 0 s |
|  | testIterateNamespaceAttribute | 0 s |

<a id="surefire--testconfigurationnodepointer"></a>

### TestConfigurationNodePointer

|  |  |  |
| --- | --- | --- |
|  | testIterators | 0.003 s |
|  | testIsLeafTrue | 0.001 s |
|  | testIsAttribute | 0.001 s |
|  | testCompareChildNodePointersAttributes | 0 s |
|  | testCompareChildNodePointersChildren | 0.001 s |
|  | testIsLeave | 0 s |
|  | testSetValue | 0.001 s |

<a id="surefire--testnodeupdatedata"></a>

### TestNodeUpdateData

|  |  |  |
| --- | --- | --- |
|  | testGetChangedValuesModify | 0 s |
|  | testInitNoData | 0.001 s |
|  | testInitRemovedNodesDefensiveCopy | 0 s |
|  | testGetRemovedNodesModify | 0 s |
|  | testGetNewValuesModify | 0 s |
|  | testInitNewValuesDefensiveCopy | 0 s |
|  | testInitChangedValuesDefensiveCopy | 0 s |

<a id="surefire--testhierarchicalconfigurationxmlreader"></a>

### TestHierarchicalConfigurationXMLReader

|  |  |  |
| --- | --- | --- |
|  | testParse | 0.001 s |

<a id="surefire--testcombinedbuilderparametersimpl"></a>

### TestCombinedBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testRegisterMissingProviders | 0.003 s |
|  | testProviderForUnknown | 0 s |
|  | testRegisterChildDefaultsHandler | 0 s |
|  | testSetInheritSettings | 0 s |
|  | testGetChildDefaultParametersManagerUndefined | 0 s |
|  | testRegisterChildDefaultsHandlerWithStartClass | 0.001 s |
|  | testRegisterProviderNoProvider | 0 s |
|  | testGetChildDefaultParametersManagerSpecific | 0 s |
|  | testInheritFromNoParametersInMap | 0 s |
|  | testClone | 0 s |
|  | testRegisterMissingProvidersParamsNull | 0 s |
|  | testGetParametersInherited | 0 s |
|  | testSetBeanProperties | 0 s |
|  | testGetProvidersModify | 0.001 s |
|  | testSetBasePath | 0 s |
|  | testFromParametersNotFound | 0 s |
|  | testRegisterMissingProvidersNullEntry | 0 s |
|  | testRegisterProviderNoTag | 0 s |
|  | testGetProvidersInitial | 0 s |
|  | testFromParametersExisting | 0 s |
|  | testSetDefinitionBuilderParameters | 0 s |
|  | testFromParametersCreate | 0 s |
|  | testInheritFrom | 0.001 s |
|  | testRegisterMissingProvidersParams | 0 s |
|  | testRegisterMissingProvidersNullMap | 0 s |
|  | testSetDefinitionBuilder | 0 s |
|  | testRegisterProvider | 0 s |

<a id="surefire--testdefaultexpressionengine"></a>

### TestDefaultExpressionEngine

|  |  |  |
| --- | --- | --- |
|  | testCanonicalKeyRootNoParentKey | 0 s |
|  | testInitNoSymbols | 0 s |
|  | testPrepareAddWithSameAttributeDelimiter | 0 s |
|  | testPrepareAddWithIndex | 0.001 s |
|  | testPrepareAddInvalidKeyAttribute | 0 s |
|  | testNodeKeyWithRoot | 0 s |
|  | testPrepareAddWithPath | 0 s |
|  | testQueryRootNodeEmptyKey | 0 s |
|  | testCanonicalKeyNoDuplicates | 0 s |
|  | testQueryAttributeEmulation | 0.001 s |
|  | testAttributeKeyRoot | 0 s |
|  | testAttributeKeyWithAlternativeSyntax | 0 s |
|  | testQueryRootNodeNullKey | 0 s |
|  | testNodeKeyWithEscapedDelimiters | 0 s |
|  | testQueryKeys | 0 s |
|  | testQueryEscapedKeys | 0 s |
|  | testDefaultSymbols | 0 s |
|  | testPrepareAddInvalidKey | 0 s |
|  | testQueryNodes | 0 s |
|  | testCanonicalKeyRootWithParentKey | 0 s |
|  | testPrepareAddDirectly | 0 s |
|  | testQueryNonExistingKeys | 0 s |
|  | testPrepareAddWithAlternativeMatcher | 0 s |
|  | testCanonicalKeyWithDuplicates | 0 s |
|  | testAttributeKey | 0 s |
|  | testAttributeKeyNoParent | 0 s |
|  | testPrepareAddEmptyKey | 0 s |
|  | testCanonicalKeyNoParentKey | 0 s |
|  | testPrepareAddWithAlternativeSyntax | 0.001 s |
|  | testQueryAlternativeSyntax | 0 s |
|  | testQueryKeyWithAlternativeMatcher | 0 s |
|  | testNodeKeyWithAlternativeSyntax | 0 s |
|  | testPrepareAddAttribute | 0 s |
|  | testNodeKey | 0 s |
|  | testPrepareAddAttributeRoot | 0 s |
|  | testNodeKeyWithAlternativeSyntaxAttributePropertyDelimiter | 0.001 s |
|  | testQueryRootAttribute | 0 s |
|  | testPrepareAddNullKey | 0 s |

<a id="surefire--testeventsource"></a>

### TestEventSource

|  |  |  |
| --- | --- | --- |
|  | testSetDetailEvents | 0 s |
|  | testAddEventListener | 0 s |
|  | testCopyEventListenersNullSource | 0 s |
|  | testClone | 0 s |
|  | testInit | 0 s |
|  | testGetEventListenersAddNew | 0 s |
|  | testGetEventListenersUpdate | 0 s |
|  | testClearEventListeners | 0 s |
|  | testFireError | 0 s |
|  | testFireEvent | 0 s |
|  | testRemoveListenerInFireEvent | 0 s |
|  | testRemoveNullEventListener | 0 s |
|  | testFireErrorNoListeners | 0 s |
|  | testFireEventNoDetails | 0 s |
|  | testClearErrorListeners | 0 s |
|  | testFireEventNoListeners | 0 s |
|  | testCopyEventListeners | 0 s |
|  | testAddNullEventListener | 0 s |
|  | testRemoveEventListener | 0.001 s |

<a id="surefire--testappletconfiguration"></a>

### TestAppletConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.002 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testconstantlookup"></a>

### TestConstantLookup

|  |  |  |
| --- | --- | --- |
|  | testLookupNonExisting | 0 s |
|  | testLookupPrivate | 0 s |
|  | testLookupInvalidSyntax | 0 s |
|  | testLookupNull | 0 s |
|  | testLookupUnknownClass | 0 s |
|  | testLookupCache | 0.001 s |
|  | testLookupNonStringFromCache | 0 s |
|  | testLookupConstant | 0 s |

<a id="surefire--testabstractconfigurationbasicfeatures"></a>

### TestAbstractConfigurationBasicFeatures

|  |  |  |
| --- | --- | --- |
|  | testInterpolationUnknownVariable | 0 s |
|  | testCopyEvents | 0 s |
|  | testGetCollectionNullTarget | 0.001 s |
|  | testGetArrayPrimitive | 0 s |
|  | testAppendDelimiterHandling | 0 s |
|  | testInterpolateEnvironmentVariables | 0.002 s |
|  | testSetPrefixLookupsNoInterpolator | 0.002 s |
|  | testGetArray | 0 s |
|  | testSetDefaultConversionHandler | 0 s |
|  | testAddPropertyListNoDelimiterParsing | 0 s |
|  | testDefaultConversionHandlerSharedInstance | 0.001 s |
|  | testGet | 0 s |
|  | testGetUnknownWithDefaultValue | 0 s |
|  | testDefaultListDelimiterHandler | 0 s |
|  | testGetArrayDefaultValueWrongComponentClass | 0 s |
|  | testCopy | 0 s |
|  | testInterpolateRecursive | 0.001 s |
|  | testSetDefaultLookupsNoInterpolator | 0 s |
|  | testCopyDelimiterHandling | 0 s |
|  | testGetArrayUnknownWithDefault | 0 s |
|  | testSizeInternal | 0 s |
|  | testSetPrefixLookupsExistingInterpolator | 0 s |
|  | testGetUnknownWithThrowExceptionOnMissing | 0.001 s |
|  | testGetEncodedStringValue | 0.002 s |
|  | testGetList | 0 s |
|  | testGetEncodedStringNoValue | 0 s |
|  | testCyclicInterpolation | 0 s |
|  | testGetStringArrayUnknown | 0 s |
|  | testGetEncodedStringWithDefaultDecoder | 0 s |
|  | testGetCollection | 0.001 s |
|  | testGetArrayUnknownNoDefault | 0 s |
|  | testSetDefaultConversionHandlerNull | 0 s |
|  | testSetParentInterpolatorNoInterpolator | 0.009 s |
|  | testGetStringArrayNonString | 0 s |
|  | testClearIteratorNoRemove | 0 s |
|  | testGetArrayDefaultValueNotAnArray | 0 s |
|  | testGetUnownWithDefaultValueThrowExceptionOnMissing | 0 s |
|  | testCopyNull | 0 s |
|  | testGetCollectionUnknownWithDefault | 0 s |
|  | testInterpolateList | 0 s |
|  | testInterpolateEscape | 0 s |
|  | testGetCollectionSingleValue | 0 s |
|  | testInterpolateString | 0 s |
|  | testSetListDelimiterHandlerNull | 0 s |
|  | testInterpolationNoInterpolator | 0.001 s |
|  | testGetListUnknownWithDefault | 0 s |
|  | testGetEncodedStringNoDecoder | 0 s |
|  | testAddPropertyList | 0 s |
|  | testInterpolateStringWithListVariable | 0 s |
|  | testInstallInterpolatorNull | 0 s |
|  | testGetUnknownNoDefaultValue | 0 s |
|  | testAppend | 0 s |
|  | testAppendWithLists | 0 s |
|  | testCopyWithLists | 0.001 s |
|  | testGetEncodedStringNoDefaultDecoderDefined | 0 s |
|  | testGetCollectionUnknownNoDefault | 0 s |
|  | testAppendNull | 0 s |
|  | testGetListNonString | 0 s |
|  | testInterpolateArray | 0 s |
|  | testSetDefaultLookupsExistingInterpolator | 0 s |
|  | testAppendEvents | 0.001 s |
|  | testDefaultConversionHandler | 0 s |
|  | testNestedVariableInterpolation | 0 s |
|  | testGetListUnknownNoDefault | 0 s |
|  | testSetParentInterpolatorExistingInterpolator | 0 s |

<a id="surefire--testsystempropertieslookup"></a>

### TestSystemPropertiesLookup

|  |  |  |
| --- | --- | --- |
|  | testLookupUnknownProperty | 0 s |
|  | testLookupProperties | 0 s |

<a id="surefire--testdummylookup"></a>

### TestDummyLookup

|  |  |  |
| --- | --- | --- |
|  | testLookup | 0 s |

<a id="surefire--testfilesystemlocationstrategy"></a>

### TestFileSystemLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testLocate | 0 s |

<a id="surefire--testconfigurationpropertysource"></a>

### TestConfigurationPropertySource

|  |  |  |
| --- | --- | --- |
|  | testSystemPropertyValueInjection | 0 s |
|  | testEmptyStringValueInjection | 0 s |
|  | testListValueInjection | 0 s |
|  | testNullValueInjection | 0 s |

<a id="surefire--testcompositeconfigurationnonstringproperties"></a>

### TestCompositeConfigurationNonStringProperties

|  |  |  |
| --- | --- | --- |
|  | testDoubleArrayValue | 0 s |
|  | testShortArrayValue | 0 s |
|  | testBooleanArrayValue | 0.001 s |
|  | testFloat | 0 s |
|  | testShort | 0 s |
|  | testByte | 0.001 s |
|  | testLong | 0 s |
|  | testLongDefaultValue | 0.001 s |
|  | testIntegerArrayValue | 0 s |
|  | testLongArrayValue | 0 s |
|  | testShortDefaultValue | 0 s |
|  | testBoolean | 0.001 s |
|  | testFloatArrayValue | 0 s |
|  | testBooleanDefaultValue | 0 s |
|  | testDoubleDefaultValue | 0.001 s |
|  | testListMissing | 0 s |
|  | testFloatDefaultValue | 0 s |
|  | testDouble | 0 s |
|  | testByteArrayValue | 0.001 s |
|  | testIntegerDefaultValue | 0 s |
|  | testInteger | 0 s |
|  | testIsEmpty | 0.001 s |
|  | testSubset | 0 s |

<a id="surefire--testxpathexpressionengineinconfig"></a>

### TestXPathExpressionEngineInConfig

|  |  |  |
| --- | --- | --- |
|  | testPropertiesWithNamespace | 0.009 s |
|  | testSetPropertyExisting | 0.001 s |
|  | testSetPropertyNewKey | 0 s |
|  | testSetPropertyNewAttribute | 0.001 s |
|  | testSetPropertyPartlyExisting | 0.001 s |
|  | testAddPropertyComplexStructures | 0.002 s |

<a id="surefire--testpropertylistconfigurationevents"></a>

### TestPropertyListConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0.001 s |
|  | testSetPropertyEventWithDetails | 0.001 s |
|  | testSetPropertyEvent | 0 s |
|  | testClearPropertyEventWithDetails | 0 s |
|  | testClearPropertyEvent | 0 s |
|  | testAddPropertyEventWithDetails | 0.001 s |
|  | testClearEventWithDetails | 0.001 s |
|  | testAddPropertyEvent | 0.001 s |
|  | testSetByteArrayPropertyEvent | 0.001 s |
|  | testAddByteArrayPropertyEvent | 0 s |

<a id="surefire--testcombinedlocationstrategy"></a>

### TestCombinedLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testInitDefensiveCopy | 0.001 s |
|  | testLocateSuccessFirstSubStrategy | 0 s |
|  | testGetSubStrategiesModify | 0 s |
|  | testLocateSuccessSecondSubStrategy | 0 s |
|  | testInitCollectionWithNullEntries | 0 s |
|  | testInitNullCollection | 0.001 s |
|  | testLocateFailed | 0 s |

<a id="surefire--testjndiconfiguration"></a>

### TestJNDIConfiguration

|  |  |  |
| --- | --- | --- |
|  | testResetRemovedProperties | 0.013 s |
|  | testLogListener | 0.004 s |
|  | testProperties | 0.002 s |
|  | testFloat | 0.002 s |
|  | testShort | 0.002 s |
|  | testByte | 0.001 s |
|  | testLong | 0.002 s |
|  | testContainsKeyError | 0.001 s |
|  | testLongDefaultValue | 0.001 s |
|  | testShortDefaultValue | 0.001 s |
|  | testContainsKey | 0.001 s |
|  | testBoolean | 0.001 s |
|  | testGetKeysError | 0.002 s |
|  | testBooleanDefaultValue | 0.001 s |
|  | testDoubleDefaultValue | 0.001 s |
|  | testListMissing | 0.001 s |
|  | testChangePrefix | 0.001 s |
|  | testGetPropertyError | 0.002 s |
|  | testFloatDefaultValue | 0.001 s |
|  | testGetKeysWithCycles | 0.003 s |
|  | testDouble | 0.003 s |
|  | testIntegerDefaultValue | 0.002 s |
|  | testInteger | 0.001 s |
|  | testGetKeysNoData | 0.001 s |
|  | testSubset | 0.001 s |
|  | testConstructor | 0.003 s |
|  | testIsEmptyError | 0.001 s |

<a id="surefire--testconfigurationmap"></a>

### TestConfigurationMap

|  |  |  |
| --- | --- | --- |
|  | testPut | 0 s |
|  | testNullConfig | 0 s |

<a id="surefire--testreloadingcombinedconfigurationbuilder"></a>

### TestReloadingCombinedConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testNoReloadableSources | 0.001 s |
|  | testInitWithFailOnInitFlag | 0 s |
|  | testNestedReloadableSources | 0.002 s |
|  | testInitWithParameters | 0.002 s |
|  | testReloadableDefinitionBuilder | 0.001 s |

<a id="surefire--testnodeselector"></a>

### TestNodeSelector

|  |  |  |
| --- | --- | --- |
|  | testEqualsFalse | 0 s |
|  | testSelectMultipleTargets | 0 s |
|  | testSelectSubKey | 0.001 s |
|  | testToString | 0 s |
|  | testSelectSubKeyMultipleResults | 0.001 s |
|  | testEqualsTrue | 0 s |
|  | testSelectSingleKeySuccess | 0.001 s |
|  | testSelectSubKeyUnknown | 0 s |
|  | testSelectSingleAttributeKey | 0.002 s |
|  | testEqualsOtherObjects | 0 s |
|  | testSelectIgnoreAttributeResults | 0.001 s |
|  | testSelectSubKeyComplexEvaluation | 0 s |

<a id="surefire--testreloadingbuildersupportlistener"></a>

### TestReloadingBuilderSupportListener

|  |  |  |
| --- | --- | --- |
|  | testResetReloadingStateOnResultCreation | 0 s |
|  | testResetBuilderOnReloadingEvent | 0 s |

<a id="surefire--testequalsproperty"></a>

### TestEqualsProperty

|  |  |  |
| --- | --- | --- |
|  | testEquals | 0 s |

<a id="surefire--testreloadingcontroller"></a>

### TestReloadingController

|  |  |  |
| --- | --- | --- |
|  | testReloadingStateAfterInit | 0.002 s |
|  | testReloadingEventType | 0 s |
|  | testCheckForReloadingInReloadingState | 0 s |
|  | testCheckForReloadingFalse | 0 s |
|  | testResetReloadingNotInReloadingState | 0 s |
|  | testInitNoDetector | 0 s |
|  | testResetReloadingState | 0 s |
|  | testCheckForReloadingTrue | 0 s |

<a id="surefire--testinmemorynodemodeltrackednodes"></a>

### TestInMemoryNodeModelTrackedNodes

|  |  |  |
| --- | --- | --- |
|  | testIsDetachedTrue | 0 s |
|  | testSelectAndTrackNodesNoSelection | 0 s |
|  | testIsDetachedAfterClear | 0 s |
|  | testTrackChildNodeWithCreationNonExisting | 0 s |
|  | testTrackChildNodes | 0.001 s |
|  | testSetPropertyOnDetachedNode | 0 s |
|  | testTrackNodeMultipleTimes | 0.001 s |
|  | testAddPropertyOnTrackedNode | 0 s |
|  | testAddPropertyOnDetachedNode | 0 s |
|  | testIsDetachedAfterSetRoot | 0 s |
|  | testGetTrackedNodeHandlerActive | 0 s |
|  | testTrackChildNodeWithCreationNoResults | 0 s |
|  | testClearTreeOnDetachedNode | 0 s |
|  | testReplaceTrackedNodeNull | 0 s |
|  | testTrackNodeKeyNoResults | 0 s |
|  | testTrackedNodeClearedInOperation | 0.001 s |
|  | testGetTrackedNodeAfterUpdateNoLongerExisting | 0 s |
|  | testGetTrackedNodeAfterSetRootNode | 0 s |
|  | testTrackChildNodeWithCreationExisting | 0 s |
|  | testSelectAndTrackNodesNodeAlreadyTracked | 0.001 s |
|  | testReplaceTrackedNodeForDetachedNode | 0 s |
|  | testUntrackNode | 0 s |
|  | testGetTrackedNodeExisting | 0.001 s |
|  | testTrackChildNodesMultipleResults | 0 s |
|  | testTrackChildNodesNodeWithNoChildren | 0 s |
|  | testSetPropertyOnTrackedNode | 0 s |
|  | testGetTrackedNodeAfterUpdate | 0 s |
|  | testClearPropertyOnTrackedNode | 0.001 s |
|  | testTrackNodeKeyMultipleResults | 0 s |
|  | testGetTrackedNodeNonExisting | 0 s |
|  | testAddNodesOnTrackedNode | 0 s |
|  | testClearPropertyOnDetachedNode | 0.001 s |
|  | testIsDetachedFalseNoUpdates | 0 s |
|  | testAddNodesOnDetachedNode | 0 s |
|  | testClearTreeOnTrackedNode | 0 s |
|  | testReplaceTrackedNodeForActiveTrackedNode | 0 s |
|  | testTrackChildNodeWithCreationMultipleResults | 0.001 s |
|  | testGetTrackedNodeAfterClear | 0 s |
|  | testSelectAndTrackNodes | 0 s |
|  | testUntrackNodeNonExisting | 0 s |
|  | testGetTrackedNodeHandlerDetached | 0 s |
|  | testIsDetachedFalseAfterUpdate | 0 s |
|  | testTrackChildNodesNoResults | 0.001 s |

<a id="surefire--testconfigurationeventtypes"></a>

### TestConfigurationEventTypes

|  |  |  |
| --- | --- | --- |
|  | testFetchSuperEventTypesNull | 0 s |
|  | testBaseErrorEventType | 0 s |
|  | testClearPropertyEventType | 0 s |
|  | testClearTreeEventType | 0 s |
|  | testIsInstanceOfBaseNull | 0 s |
|  | testWriteErrorEventType | 0 s |
|  | testReadErrorEventType | 0 s |
|  | testAddPropertyEventType | 0 s |
|  | testIsInstanceOfFalse | 0 s |
|  | testConfigurationEventType | 0 s |
|  | testFetchSuperEventTypesForBaseType | 0 s |
|  | testIsInstanceOfDerivedNull | 0 s |
|  | testHierarchicalEventType | 0 s |
|  | testFetchSuperEventTypesOfType | 0 s |
|  | testSetPropertyEventType | 0 s |
|  | testSubnodeChangedEventType | 0 s |
|  | testIsInstanceOfTrue | 0 s |
|  | testClearEventType | 0 s |
|  | testAddNodesEventType | 0 s |

<a id="surefire--testfilehandlerreloadingdetector"></a>

### TestFileHandlerReloadingDetector

|  |  |  |
| --- | --- | --- |
|  | testDefaultRefreshDelay | 0 s |
|  | testRefreshIsReloadingRequiredTrue | 0.013 s |
|  | testGetFileJarURL | 0 s |
|  | testIsReloadingRequiredFileDoesNotExist | 0 s |
|  | testRefreshReloadingAndReset | 0 s |
|  | testInitWithFileHandler | 0.001 s |
|  | testReloadingAndReset | 0 s |
|  | testLocationAfterInit | 0 s |
|  | testRefreshDelay | 0 s |
|  | testIsReloadingRequiredNoLocation | 0 s |
|  | testIsReloadingRequiredTrue | 0 s |

<a id="surefire--testtreedata"></a>

### TestTreeData

|  |  |  |
| --- | --- | --- |
|  | testNodeHandlerGetMatchingChildrenCount | 0 s |
|  | testNodeHandlerGetAttributeValue | 0 s |
|  | testNodeHandlerIsDefinedAttributes | 0 s |
|  | testNodeHandlerGetAttributesImmutable | 0 s |
|  | testNodeHandlerIndexOfChild | 0 s |
|  | testNodeHandlerIndexOfUnknownChild | 0.001 s |
|  | testNodeHandlerGetChildrenCountAll | 0 s |
|  | testNodeHandlerGetChildren | 0 s |
|  | testNodeHandlerHasAttributesFalse | 0 s |
|  | testNodeHandlerGetChildrenByName | 0 s |
|  | testNodeHandlerValue | 0 s |
|  | testNodeHandlerGetChildrenByNameImmutable | 0 s |
|  | testGetParentInvalidNode | 0 s |
|  | testNodeHandlerGetMatchingChildrenImmutable | 0 s |
|  | testNodeHandlerHasAttributesTrue | 0 s |
|  | testNodeHandlerIsDefinedFalse | 0 s |
|  | testNodeHandlerIsDefinedValue | 0.001 s |
|  | testNodeHandlerGetChildAtIndex | 0 s |
|  | testNodeHandlerGetChildrenCountSpecific | 0 s |
|  | testGetParentNode | 0 s |
|  | testNodeHandlerIsDefinedChildren | 0 s |
|  | testNodeHandlerGetMatchingChildren | 0 s |
|  | testNodeHandlerGetAttributes | 0 s |
|  | testNodeHandlerName | 0 s |
|  | testGetParentForRoot | 0 s |

<a id="surefire--testbasepathlocationstrategy"></a>

### TestBasePathLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testLocateSuccess | 0 s |
|  | testNullBasePath | 0 s |
|  | testNullFileName | 0 s |
|  | testLocateSuccessRelativePrefix | 0 s |

<a id="surefire--testservletcontextconfiguration"></a>

### TestServletContextConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.003 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0.001 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0.001 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testpatternsubtreeconfigurationwrapper"></a>

### TestPatternSubtreeConfigurationWrapper

|  |  |  |
| --- | --- | --- |
|  | testReadNotFileBased | 0 s |

<a id="surefire--testdefaultreloadingdetectorfactory"></a>

### TestDefaultReloadingDetectorFactory

|  |  |  |
| --- | --- | --- |
|  | testCreateReloadingDetectorDefaultRefreshDelay | 0 s |
|  | testCreateReloadingDetector | 0 s |

<a id="surefire--testnonstringproperties"></a>

### TestNonStringProperties

|  |  |  |
| --- | --- | --- |
|  | testDoubleArrayValue | 0 s |
|  | testShortArrayValue | 0.001 s |
|  | testBooleanArrayValue | 0 s |
|  | testFloat | 0 s |
|  | testShort | 0.001 s |
|  | testByte | 0 s |
|  | testLong | 0 s |
|  | testLongDefaultValue | 0.001 s |
|  | testIntegerArrayValue | 0 s |
|  | testLongArrayValue | 0.001 s |
|  | testShortDefaultValue | 0 s |
|  | testBoolean | 0.001 s |
|  | testFloatArrayValue | 0 s |
|  | testBooleanDefaultValue | 0 s |
|  | testDoubleDefaultValue | 0.001 s |
|  | testListMissing | 0 s |
|  | testFloatDefaultValue | 0 s |
|  | testDouble | 0 s |
|  | testByteArrayValue | 0.001 s |
|  | testIntegerDefaultValue | 0 s |
|  | testInteger | 0 s |
|  | testIsEmpty | 0.001 s |
|  | testSubset | 0 s |

<a id="surefire--testautosavelistener"></a>

### TestAutoSaveListener

|  |  |  |
| --- | --- | --- |
|  | testConfigurationChangedAutoSave | 0.014 s |
|  | testConfigurationChangedAutoSaveException | 0 s |
|  | testConfigurationChangedAfterLoading | 0 s |
|  | testUpdateFileHandler | 0.010 s |
|  | testConfigurationChangedWhileLoading | 0 s |
|  | testUpdateFileHandlerNull | 0 s |
|  | testConfigurationChangedBeforeUpdateNoSave | 0 s |

<a id="surefire--testservletrequestconfiguration"></a>

### TestServletRequestConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.006 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testListWithEscapedElements | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testdefaultconfigurationkey"></a>

### TestDefaultConfigurationKey

|  |  |  |
| --- | --- | --- |
|  | testTrimLeft | 0 s |
|  | testCommonKeyNull | 0 s |
|  | testAttributeKeyWithIndex | 0 s |
|  | testAppendDelimiters | 0 s |
|  | testIsAttributeKeyWithoutEndMarkers | 0 s |
|  | testAppendDelimitersWithoutEscaping | 0 s |
|  | testIterateAttributeEqualsPropertyDelimiter | 0 s |
|  | testTrim | 0.001 s |
|  | testIterateAlternativeEscapeDelimiter | 0 s |
|  | testIterateEscapedDelimiters | 0 s |
|  | testIterateWithoutEscapeDelimiter | 0 s |
|  | testDifferenceKey | 0 s |
|  | testCommonKey | 0 s |
|  | testConstructAttributeKeyWithoutEndMarkers | 0.001 s |
|  | testTrimRight | 0 s |
|  | testDifferenceKeySame | 0 s |
|  | testAppendAttribute | 0 s |
|  | testAttributeName | 0 s |
|  | testAppendDecoratedAttributeKey | 0.001 s |
|  | testAppendWithEscapeFlag | 0 s |
|  | testAppendComplexKey | 0 s |
|  | testIterateStrangeKeys | 0 s |
|  | testAppend | 0 s |
|  | testIsAttributeKey | 0 s |
|  | testConstructAttributeKey | 0 s |
|  | testEquals | 0 s |
|  | testSetNullExpressionEngine | 0 s |
|  | testLength | 0 s |
|  | testIterateWithRemove | 0 s |
|  | testIterate | 0 s |
|  | testAppendIndex | 0 s |
|  | testIterateWithBrackets | 0.001 s |
|  | testAppendNullAttributeKey | 0 s |

<a id="surefire--testxmlpropertiesconfiguration"></a>

### TestXMLPropertiesConfiguration

|  |  |  |
| --- | --- | --- |
|  | testLoad | 0.001 s |
|  | testSave | 0.002 s |
|  | testDOMLoad | 0.001 s |
|  | testDOMSave | 0.003 s |

<a id="surefire--testiniconfiguration"></a>

### TestINIConfiguration

|  |  |  |
| --- | --- | --- |
|  | testQuotedValueEmpty | 0 s |
|  | testSaveWithGlobalSection | 0.001 s |
|  | testListParsingDisabled | 0 s |
|  | testGetSections | 0 s |
|  | testMultipleSeparatorsQuoted | 0 s |
|  | testLineContinuationQuoted | 0.001 s |
|  | testLoadAlternativeSeparator | 0 s |
|  | testLineContinuationEmptyLine | 0 s |
|  | testWriteValueWithCommentChar | 0.001 s |
|  | testIsCommentLine | 0 s |
|  | testGlobalSectionNodeHandlerGetChildByIndex | 0.001 s |
|  | testKeysOfGlobalSection | 0.001 s |
|  | testLineContinuationNone | 0 s |
|  | testLoadFromBuilder | 0.001 s |
|  | testValueWithDelimiters | 0 s |
|  | testEmptySection | 0 s |
|  | testGetSectionsGlobalOnly | 0.001 s |
|  | testLineContinuationQuotedComment | 0 s |
|  | testSaveKeysWithDelimiters | 0 s |
|  | testLoad | 0.001 s |
|  | testSave | 0 s |
|  | testQuotedValueWithComment | 0 s |
|  | testSaveClearedSection | 0.001 s |
|  | testLineContinuation | 0 s |
|  | testGetSectionsSynchronized | 0 s |
|  | testGetSectionGloabalMultiThreaded | 0.009 s |
|  | testGetSectionsNoGlobal | 0 s |
|  | testGetSectionNonExistingManipulate | 0.001 s |
|  | testGetSectionsWithInLineComment(String, boolean, String[])[1] | 0.001 s |
|  | testGetSectionsWithInLineComment(String, boolean, String[])[2] | 0 s |
|  | testGetSectionsWithInLineComment(String, boolean, String[])[3] | 0 s |
|  | testGetSectionsWithInLineComment(String, boolean, String[])[4] | 0 s |
|  | testGetPropertyNoValue | 0 s |
|  | testSaveWithDelimiterParsingDisabled | 0 s |
|  | testGetSectionDuplicate | 0 s |
|  | testValueWithComment(String, String, String)[1] | 0.001 s |
|  | testValueWithComment(String, String, String)[2] | 0 s |
|  | testValueWithComment(String, String, String)[3] | 0.001 s |
|  | testValueWithComment(String, String, String)[4] | 0 s |
|  | testValueWithComment(String, String, String)[5] | 0 s |
|  | testValueWithComment(String, String, String)[6] | 0.001 s |
|  | testGetSectionExisting | 0 s |
|  | testPropertyWithDelimiter | 0 s |
|  | testMultipleSeparators | 0.001 s |
|  | testMergeDuplicateSection | 0 s |
|  | testGetSectionGlobal | 0 s |
|  | testSeparatorUsedInINIOutput | 0.002 s |
|  | testExpressionEngineIgnoringCase | 0 s |
|  | testGetSectionNonExisting | 0 s |
|  | testSeparatorUsedInINIInput | 0.001 s |
|  | testGetSectionMerged | 0 s |
|  | testSaveWithOnlyGlobalSection | 0 s |
|  | testQuotedValueWithWhitespace | 0.001 s |
|  | testQuotedValue | 0 s |
|  | testGlobalSectionConnected | 0 s |
|  | testWriteEmptySection | 0 s |
|  | testLineContinuationComment | 0.001 s |
|  | testIsSectionLine | 0 s |
|  | testQuotedValueWithQuotes | 0 s |
|  | testGetPropertyNoKey | 0 s |
|  | testListDelimiterHandlingInList | 0.001 s |
|  | testGetSectionsAdded | 0 s |
|  | testGlobalSectionNodeHandlerGetChildrenByName | 0 s |
|  | testGetSectionsWithGlobal | 0 s |
|  | testQuotedValueWithWhitespaceAndComment | 0 s |
|  | testGlobalSectionNodeHandlerGetChildrenCount | 0 s |
|  | testValueWithSemicolon | 0 s |
|  | testSeparators | 0 s |
|  | testQuotedValueWithSingleQuotes | 0.001 s |
|  | testGetSectionsDottedVar | 0 s |
|  | testCommentLeadingSeparatorUsedInINIInput | 0 s |
|  | testLineContinuationAtEnd | 0.001 s |
|  | testListDelimiterHandling | 0 s |
|  | testGetSectionGlobalNonExisting | 0 s |
|  | testGlobalProperty | 0 s |
|  | testGetSectionConnected | 0.001 s |
|  | testGlobalSectionNodeHandlerIndexOfChild | 0 s |

<a id="surefire--testperiodicreloadingtrigger"></a>

### TestPeriodicReloadingTrigger

|  |  |  |
| --- | --- | --- |
|  | testStart | 0.010 s |
|  | testStop | 0.001 s |
|  | testShutdownNoExecutor | 0 s |
|  | testDefaultExecutor | 0 s |
|  | testInitNoController | 0 s |
|  | testShutdown | 0 s |
|  | testStopNotRunning | 0 s |
|  | testIsRunningAfterInit | 0 s |
|  | testStartTwice | 0 s |

<a id="surefire--testinmemorynodemodelreferences"></a>

### TestInMemoryNodeModelReferences

|  |  |  |
| --- | --- | --- |
|  | testQueryReferences | 0.006 s |
|  | testMergeRootOverrideName | 0 s |
|  | testQueryReferencesAfterUpdate | 0.001 s |
|  | testQueryReferenceUnknown | 0 s |
|  | testReplaceRoot | 0 s |
|  | testReplaceRootNull | 0.001 s |
|  | testMergeRootReference | 0 s |
|  | testMergeRootWithAttributes | 0.001 s |
|  | testRemovedReferencesModify | 0.001 s |
|  | testQueryRemovedReferencesAfterRemove | 0 s |
|  | testQueryRemovedReferencesEmpty | 0.001 s |
|  | testMergeRootWithValue | 0.001 s |

<a id="surefire--testconfigurations"></a>

### TestConfigurations

|  |  |  |
| --- | --- | --- |
|  | testCombinedFromURL | 0.004 s |
|  | testFileBasedURL | 0 s |
|  | testINIBuilderFromURL | 0.001 s |
|  | testPropertiesBuilderFromPathIncludeNotFoundFail | 0 s |
|  | testPropertiesBuilderFromPathIncludeNotFoundPass | 0.002 s |
|  | testCombinedBuilderFromFile | 0.003 s |
|  | testCombinedBuilderFromPath | 0.004 s |
|  | testCombinedFromFile | 0.002 s |
|  | testCombinedFromPath | 0.002 s |
|  | testPropertiesFromURL | 0.001 s |
|  | testDefaultParameters | 0 s |
|  | testPropertiesBuilderFromFile | 0 s |
|  | testPropertiesBuilderFromPath | 0.001 s |
|  | testXMLBuilderFromFile | 0 s |
|  | testXMLBuilderFromPath | 0 s |
|  | testCombinedBuilderFromURL | 0.003 s |
|  | testXMLFromFile | 0.001 s |
|  | testXMLFromPath | 0 s |
|  | testFileBasedFile | 0.001 s |
|  | testFileBasedPath | 0 s |
|  | testINIBuilderFromFile | 0 s |
|  | testINIBuilderFromPath | 0 s |
|  | testXMLFromURL | 0 s |
|  | testINIFromURL | 0.001 s |
|  | testPropertiesBuilderFromURL | 0 s |
|  | testPropertiesFromFile | 0 s |
|  | testPropertiesFromPath | 0 s |
|  | testFileBasedBuilderWithFile | 0 s |
|  | testFileBasedBuilderWithPath | 0 s |
|  | testInitWithParameters | 0 s |
|  | testINIFromFile | 0 s |
|  | testINIFromPath | 0 s |
|  | testFileBasedBuilderWithURL | 0 s |
|  | testXMLBuilderFromURL | 0 s |

<a id="surefire--testdefaultimmutableconfiguration"></a>

### TestDefaultImmutableConfiguration

|  |  |  |
| --- | --- | --- |
|  | testContainsValueDefaultImplementation | 0 s |
|  | testGetDurationUnknown | 0 s |
|  | testGetDuration | 0 s |
|  | testGetDurationIncompatibleType | 0 s |

<a id="surefire--testcombinedconfiguration"></a>

### TestCombinedConfiguration

|  |  |  |
| --- | --- | --- |
|  | testAccessPropertyEmpty | 0 s |
|  | testAccessPropertyMulti | 0 s |
|  | testGetSourceMulti | 0 s |
|  | testGetConfigurationNameListSynchronized | 0 s |
|  | testGetSourcesUnknownKey | 0 s |
|  | testGetSourceWithCombinedChildConfiguration | 0.001 s |
|  | testInvalidateSynchronized | 0 s |
|  | testEscapeListDelimiters | 0 s |
|  | testSetNodeCombinerSynchronized | 0 s |
|  | testGetConfigurationsSynchronized | 0 s |
|  | testGetSourceSynchronized | 0 s |
|  | testCloneSynchronized | 0 s |
|  | testConversionExpressionEngine | 0 s |
|  | testRemoveNonContainedConfiguration | 0.001 s |
|  | testClear | 0 s |
|  | testClone | 0 s |
|  | testInit | 0 s |
|  | testClearRemoveChildListener | 0 s |
|  | testGetConversionExpressionEngineSynchronized | 0 s |
|  | testCloneModify | 0 s |
|  | testConfigurationsAt | 0 s |
|  | testGetSourceNonHierarchical | 0 s |
|  | testGetKeys | 0 s |
|  | testGetConfigurationNamesSynchronized | 0 s |
|  | testRemoveNamedConfiguration | 0 s |
|  | testAddConfigurationAt | 0 s |
|  | testGetConfigurationByNameSynchronized | 0 s |
|  | testGetNodeCombinerSynchronized | 0 s |
|  | testGetSourceCombined | 0 s |
|  | testLockHandlingWithExceptionWhenConstructingRootNode | 0.001 s |
|  | testSubConfigurationWithUpdates | 0 s |
|  | testAddConfigurationWithNameTwice | 0 s |
|  | testAddNullConfiguration | 0 s |
|  | testRemoveConfiguration | 0 s |
|  | testGetSourceMultiSources | 0 s |
|  | testGetNumberOfConfigurationsSynchronized | 0 s |
|  | testAddConfigurationComplexAt | 0 s |
|  | testRemoveConfigurationByName | 0 s |
|  | testGetSourceNull | 0.001 s |
|  | testInvalidateEventBeforeAndAfterChange | 0 s |
|  | testGetSourceHierarchical | 0 s |
|  | testAddConfiguration | 0 s |
|  | testSetNodeCombiner | 0 s |
|  | testRemoveConfigurationByUnknownName | 0 s |
|  | testAddConfigurationSynchronized | 0 s |
|  | testRemoveConfigurationAt | 0 s |
|  | testAddConfigurationWithName | 0 s |
|  | testRemoveNamedConfigurationAt | 0 s |
|  | testCombinedCopyToXML | 0.002 s |
|  | testGetConfigurations | 0 s |
|  | testSetConversionExpressionEngineSynchronized | 0 s |
|  | testConcurrentAccess | 0.083 s |
|  | testGetSourcesMultiSources | 0 s |
|  | testConfigurationsAtWithUpdates | 0.001 s |
|  | testGetConfigurationByIdxSynchronized | 0 s |
|  | testGetSourceUnknown | 0 s |
|  | testUpdateContainedConfiguration | 0 s |
|  | testSetNullNodeCombiner | 0 s |
|  | testGetConfigurationNameList | 0 s |

<a id="surefire--testenvironmentlookup"></a>

### TestEnvironmentLookup

|  |  |  |
| --- | --- | --- |
|  | testLookupNonExisting | 0 s |
|  | testLookup | 0.001 s |

<a id="surefire--testconfigurationdynabeanxmlconfig"></a>

### TestConfigurationDynaBeanXMLConfig

|  |  |  |
| --- | --- | --- |
|  | testGetDescriptorArguments | 0 s |
|  | testGetDescriptorLong | 0.001 s |
|  | testSetSimpleBoolean | 0 s |
|  | testGetSimpleArguments | 0.001 s |
|  | testGetDescriptorInt | 0 s |
|  | testSetNonIndexedProperties | 0.001 s |
|  | testGetSimpleInt | 0 s |
|  | testNestedPropeties | 0.001 s |
|  | testSetSimpleFloat | 0 s |
|  | testSetSimpleShort | 0 s |
|  | testMappedRemove | 0.001 s |
|  | testGetIndexedString | 0 s |
|  | testGetIndexedValues | 0.001 s |
|  | testGetSimpleDouble | 0 s |
|  | testMappedContains | 0.001 s |
|  | testGetDescriptorFloat | 0 s |
|  | testGetDescriptorShort | 0 s |
|  | testGetSimpleBoolean | 0.001 s |
|  | testGetMappedValues | 0 s |
|  | testGetSimpleString | 0.001 s |
|  | testGetSimpleLong | 0 s |
|  | testSetSimpleInt | 0 s |
|  | testSetIndexedArguments | 0.001 s |
|  | testSetSimpleDouble | 0 s |
|  | testGetDescriptorDouble | 0.001 s |
|  | testGetDescriptors | 0 s |
|  | testGetMappedArguments | 0.001 s |
|  | testSetSimpleLong | 0 s |
|  | testGetSimpleFloat | 0.001 s |
|  | testGetSimpleShort | 0 s |
|  | testSetMappedValues | 0 s |
|  | testSetSimpleString | 0 s |
|  | testGetNonIndexedProperties | 0 s |
|  | testGetDescriptorSecond | 0.001 s |
|  | testGetDescriptorString | 0 s |
|  | testSetArrayValue | 0 s |
|  | testGetDescriptorBoolean | 0.001 s |
|  | testAddNullPropertyValue | 0 s |
|  | testGetIndexedNonExisting | 0.001 s |
|  | testGetNonExistentProperty | 0 s |
|  | testGetIndexedArguments | 0 s |
|  | testSetIndexedValues | 0.001 s |

<a id="surefire--testdynamiccombinedconfiguration"></a>

### TestDynamicCombinedConfiguration

|  |  |  |
| --- | --- | --- |
|  | testConfiguration | 0.012 s |
|  | testGetConfigurationNamesSynchronized | 0.001 s |
|  | testGetConfigurationByNameSynchronized | 0.001 s |
|  | testConcurrentGetAndReloadMultipleClients | 0.100 s |
|  | testConcurrentGetAndReload2 | 0.039 s |
|  | testUpdateConfiguration | 0.006 s |
|  | testRemoveConfigurationSynchronized | 0.001 s |
|  | testGetNumberOfConfigurationsSynchronized | 0.001 s |
|  | testAddConfigurationSynchronized | 0 s |
|  | testConcurrentGetAndReload | 0.031 s |
|  | testGetConfigurationByIdxSynchronized | 0.001 s |
|  | testConcurrentGetAndReloadFile | 4.031 s |

<a id="surefire--testmapconfigurationevents"></a>

### TestMapConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0 s |
|  | testSetPropertyEventWithDetails | 0 s |
|  | testSetPropertyEvent | 0 s |
|  | testClearPropertyEventWithDetails | 0 s |
|  | testClearPropertyEvent | 0 s |
|  | testAddPropertyEventWithDetails | 0 s |
|  | testClearEventWithDetails | 0 s |
|  | testAddPropertyEvent | 0 s |

<a id="surefire--testhomedirectorylocationstrategy"></a>

### TestHomeDirectoryLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testLocateFailedWithBasePath | 0 s |
|  | testLocateSuccessIgnoreBasePath | 0.001 s |
|  | testInitDefaults | 0 s |
|  | testNoFileName | 0 s |
|  | testLocateSuccessNoBasePath | 0.001 s |
|  | testLocateSuccessInSubFolder | 0 s |

<a id="surefire--testdisabledlistdelimiterhandler"></a>

### TestDisabledListDelimiterHandler

|  |  |  |
| --- | --- | --- |
|  | testParseIterable | 0 s |
|  | testParseIterator | 0 s |
|  | testParseArray | 0 s |
|  | testEscapeNonStringValue | 0 s |
|  | testParseNull | 0 s |
|  | testEscapeStringValueTransformer | 0.002 s |
|  | testEscapeList | 0 s |
|  | testFlattenCollectionWithLimit | 0 s |
|  | testEscapeNonStringValueTransformer | 0 s |
|  | testParseSimpleValue | 0 s |
|  | testEscapeStringValue | 0 s |
|  | testFlattenCollectionWithArrayWithLimit | 0 s |
|  | testFlattenArrayWithLimit | 0 s |

<a id="surefire--testfilebasedbuilderparameters"></a>

### TestFileBasedBuilderParameters

|  |  |  |
| --- | --- | --- |
|  | testFromParametersDefaultInstance | 0 s |
|  | testFromParametersExtract | 0 s |
|  | testInheritFromSkipMissingProperties | 0 s |
|  | testSetEncoding | 0.001 s |
|  | testClone | 0 s |
|  | testFromMap | 0 s |
|  | testSetBasePath | 0 s |
|  | testInitDefaults | 0 s |
|  | testFromParametersNull | 0 s |
|  | testFromParametersNotFound | 0 s |
|  | testSetFileSystem | 0 s |
|  | testSetReloadingDetectorFactory | 0 s |
|  | testFromMapNull | 0 s |
|  | testInheritFromNoParametersObject | 0 s |
|  | testSetFileName | 0 s |
|  | testInitFileHandler | 0 s |
|  | testSetLocationStrategy | 0 s |
|  | testSetFile | 0 s |
|  | testSetPath | 0 s |
|  | testSetReloadingRefreshDelay | 0 s |
|  | testInheritFrom | 0 s |
|  | testSetURL | 0 s |
|  | testBeanPropertiesAccess | 0 s |
|  | testGetParameters | 0 s |

<a id="surefire--testconfigurationdynabean"></a>

### TestConfigurationDynaBean

|  |  |  |
| --- | --- | --- |
|  | testGetDescriptorArguments | 0 s |
|  | testGetDescriptorLong | 0 s |
|  | testSetSimpleBoolean | 0.001 s |
|  | testGetSimpleArguments | 0 s |
|  | testGetDescriptorInt | 0 s |
|  | testSetNonIndexedProperties | 0 s |
|  | testGetSimpleInt | 0 s |
|  | testNestedPropeties | 0 s |
|  | testSetSimpleFloat | 0 s |
|  | testSetSimpleShort | 0 s |
|  | testMappedRemove | 0.001 s |
|  | testGetIndexedString | 0 s |
|  | testGetIndexedValues | 0 s |
|  | testGetSimpleDouble | 0 s |
|  | testMappedContains | 0 s |
|  | testGetDescriptorFloat | 0 s |
|  | testGetDescriptorShort | 0 s |
|  | testGetSimpleBoolean | 0 s |
|  | testGetMappedValues | 0.001 s |
|  | testGetSimpleString | 0 s |
|  | testGetSimpleLong | 0 s |
|  | testSetSimpleInt | 0 s |
|  | testSetIndexedArguments | 0 s |
|  | testSetSimpleDouble | 0 s |
|  | testGetDescriptorDouble | 0 s |
|  | testGetDescriptors | 0 s |
|  | testGetMappedArguments | 0.001 s |
|  | testSetSimpleLong | 0 s |
|  | testGetSimpleFloat | 0 s |
|  | testGetSimpleShort | 0 s |
|  | testSetMappedValues | 0 s |
|  | testSetSimpleString | 0 s |
|  | testGetNonIndexedProperties | 0 s |
|  | testGetDescriptorSecond | 0 s |
|  | testGetDescriptorString | 0 s |
|  | testSetArrayValue | 0 s |
|  | testGetDescriptorBoolean | 0 s |
|  | testAddNullPropertyValue | 0 s |
|  | testGetIndexedNonExisting | 0 s |
|  | testGetNonExistentProperty | 0 s |
|  | testGetIndexedArguments | 0 s |
|  | testSetIndexedValues | 0 s |

<a id="surefire--testbuilderconfigurationwrapperfactory"></a>

### TestBuilderConfigurationWrapperFactory

|  |  |  |
| --- | --- | --- |
|  | testConfigurationBuilderWrapper | 0.003 s |
|  | testEventSourceSupportNone | 0 s |
|  | testEventSourceSupportMockBuilder | 0 s |
|  | testEventSourceSupportBuilder | 0.002 s |
|  | testEventSourceSupportDummy | 0 s |
|  | testDefaultEventSourceSupport | 0 s |
|  | testCreateBuilderConfigurationWrapperNoBuilder | 0 s |
|  | testCreateBuilderConfigurationWrapperNoClass | 0 s |

<a id="surefire--testcombinedconfigurationbuilder"></a>

### TestCombinedConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testLoadAdditional | 0.001 s |
|  | testConfigurationBuilderProviderInheritBasicProperties | 0.003 s |
|  | testLoadOptional | 0.002 s |
|  | testMultiTenentConfigurationReloading | 5.037 s |
|  | testReloadingBuilder | 0.003 s |
|  | testEnvironmentProperties | 0.005 s |
|  | testGetChildBuilders | 0.003 s |
|  | testGetNamedBuilder | 0.003 s |
|  | testGetNamedBuilderBeforeConfigurationAccess | 0 s |
|  | testConfigurationBuilderProviderInheritEventListeners | 0.004 s |
|  | testMultiTenentConfigurationProperties | 0.002 s |
|  | testINIConfiguration | 0.005 s |
|  | testCombinedConfigurationAttributes | 0.002 s |
|  | testDefaultBasePathFromDefinitionBuilder | 0.001 s |
|  | testReactOnSubBuilderChange | 0.001 s |
|  | testNoDefinitionBuilder | 0 s |
|  | testBasePathForChildConfigurations | 0 s |
|  | testProviderInDefinitionConfig | 0.001 s |
|  | testCustomEntityResolver | 0 s |
|  | testCombinedConfigurationNoAdditional | 0.002 s |
|  | testSystemProperties | 0.001 s |
|  | testConcurrentReadAccessWithoutSynchronizer | 0.007 s |
|  | testCustomFileSystemForSubConfig | 0.001 s |
|  | testMultiTenentConfiguration | 0.002 s |
|  | testConfigurationBuilderProviderInheritCustomProviders | 0.001 s |
|  | testConfigurationBuilderProvider | 0.002 s |
|  | testConfigurationBuilderProviderInheritBasePath | 0.001 s |
|  | testChildBuildersAreInitializedOnlyOnce | 0.002 s |
|  | testBuilderNamesBeforeConfigurationAccess | 0 s |
|  | testConfigureResult | 0 s |
|  | testInitChildBuilderParametersDefaultChildProperties | 0.003 s |
|  | testCustomBuilderProvider | 0 s |
|  | testCustomResultConfiguration | 0.001 s |
|  | testResetBuilder | 0.001 s |
|  | testJndiConfiguration | 0.004 s |
|  | testInheritProperties | 0.002 s |
|  | testDefaultBasePathInParameters | 0.001 s |
|  | testBuilderNames | 0.001 s |
|  | testSuppressChildBuilderPropertyInheritance | 0.001 s |
|  | testConfigureEntityResolverWithProperties | 0.001 s |
|  | testCustomFileSystem | 0 s |
|  | testRootNodeInitializedAfterCreation | 0.001 s |
|  | testLoadConfiguration | 0.002 s |
|  | testLoadOptionalForceCreate | 0 s |
|  | testBuilderNamesManipulate | 0.001 s |
|  | testCustomLookup | 0.001 s |
|  | testGetNamedBuilderUnknown | 0.001 s |
|  | testCombinedConfigurationListNodes | 0.002 s |
|  | testRemoveSubBuilderListener | 0.001 s |
|  | testInterpolationOverMultipleSources | 0.001 s |
|  | testLoadOptionalWithException | 0.001 s |

<a id="surefire--testunioncombiner"></a>

### TestUnionCombiner

|  |  |  |
| --- | --- | --- |
|  | testInit | 0 s |
|  | testTableList | 0.005 s |
|  | testLists | 0.003 s |
|  | testAttributes | 0.003 s |
|  | testSimpleValues | 0.002 s |
|  | testSimpleValuesWithAttributes | 0.002 s |

<a id="surefire--testprovidedurllocationstrategy"></a>

### TestProvidedURLLocationStrategy

|  |  |  |
| --- | --- | --- |
|  | testLocateSuccess | 0.009 s |
|  | testLocateFail | 0 s |

<a id="surefire--testconfigurationpropertiesfactorybean"></a>

### TestConfigurationPropertiesFactoryBean

|  |  |  |
| --- | --- | --- |
|  | testMergeConfigurations | 0 s |
|  | testSetLocationsNull | 0 s |
|  | testInitialConfiguration | 0 s |
|  | testGetConfigurationDefensiveCopy | 0 s |
|  | testGetLocationsDefensiveCopy | 0 s |
|  | testSetConfigurationsDefensiveCopy | 0 s |
|  | testSetLocationsDefensiveCopy | 0 s |
|  | testLoadResources | 0 s |
|  | testAfterPropertiesSet | 0 s |
|  | testGetObject | 0 s |

<a id="surefire--testoverridecombiner"></a>

### TestOverrideCombiner

|  |  |  |
| --- | --- | --- |
|  | testInit | 0 s |
|  | testOverrideValues | 0.002 s |
|  | testListFromSecondStructure | 0.002 s |
|  | testAttributes | 0.002 s |
|  | testSimpleValues | 0.002 s |
|  | testListFromFirstStructure | 0.002 s |
|  | testCombineProperties | 0 s |
|  | testCombinedTableNoList | 0.002 s |
|  | testCombinedTableList | 0.001 s |

<a id="surefire--testjsonconfiguration"></a>

### TestJSONConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetPropertyDictionaryInList | 0.047 s |
|  | testCopyConstructor | 0.001 s |
|  | testSave | 0.004 s |
|  | testGetPropertyInteger | 0.001 s |
|  | testGetPropertyDictionary | 0 s |
|  | testGetPropertyNested | 0.001 s |
|  | [testListOfObjects](#surefire--org.apache.commons.configuration2.testjsonconfiguration.testlistofobjects) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.configuration2.TestJSONConfiguration.testListOfObjects');) | 0 s |
| - | void org.apache.commons.configuration2.TestJSONConfiguration.testListOfObjects() is @Disabled | - |
|  | testGetPropertySimple | 0.001 s |
|  | testGetPropertySubset | 0 s |
|  | testGetPropertyNestedWithList | 0 s |
|  | testGetPropertyVeryNestedProperties | 0 s |

<a id="surefire--testconfigurationnodeiteratorchildren"></a>

### TestConfigurationNodeIteratorChildren

|  |  |  |
| --- | --- | --- |
|  | testIterateStartsWith | 0.001 s |
|  | testIterateWithNodeType | 0 s |
|  | testIterateStartsWithInvalid | 0.001 s |
|  | testIterateWithWildcardTest | 0 s |
|  | testIterateWithPrefixTest | 0.001 s |
|  | testIterateWithNameTest | 0 s |
|  | testIterateWithUnknownTest | 0 s |
|  | testIterateWithUnknownType | 0.001 s |
|  | testIterateWithWildcardTestPrefix | 0 s |
|  | testIterateReverse | 0.001 s |
|  | testIterateAllChildren | 0 s |
|  | testIterateWithMatchingPrefixTest | 0 s |
|  | testIterateStartsWithReverse | 0.001 s |

<a id="surefire--testxmlconfiguration605"></a>

### TestXMLConfiguration605

|  |  |  |
| --- | --- | --- |
|  | testWithNoComma | 0.002 s |
|  | testWithCommaSeparatedList | 0 s |
|  | testWithOnlyComma | 0.001 s |
|  | testWithSeparatingWhitespace | 0 s |
|  | testWithOnlyCommaWithStringBuilderWithoutDelimiterParsing | 0 s |
|  | testWithOnlyCommaWithStringBuilder | 0.001 s |
|  | testWithOnlyCommaWithoutDelimiterParsing | 0 s |
|  | testWithSeparatingNonWhitespace | 0.001 s |

<a id="surefire--testbasehierarchicalconfigurationsynchronization"></a>

### TestBaseHierarchicalConfigurationSynchronization

|  |  |  |
| --- | --- | --- |
|  | testConfigurationAtSynchronized | 0.001 s |
|  | testGetRootElementNameSynchronized | 0.001 s |
|  | testChildConfigurationsAtSynchronized | 0.001 s |
|  | testConfigurationsAtSynchronized | 0.001 s |
|  | testCloneSynchronized | 0 s |
|  | testReadOnlyAccessToSubConfigurations | 0.006 s |
|  | testCopyConstructorSynchronized | 0.001 s |
|  | testSubnodeUpdateBySubnode | 0.001 s |
|  | testAddNodesSynchronized | 0.001 s |
|  | testGetMaxIndexSynchronized | 0 s |
|  | testClearTreeSynchronized | 0.001 s |
|  | testCloneCopySubnodeData | 0 s |
|  | testSubsetSynchronized | 0 s |
|  | testSubnodeUpdate | 0 s |

<a id="surefire--testreadwritesynchronizer"></a>

### TestReadWriteSynchronizer

|  |  |  |
| --- | --- | --- |
|  | testReentrance | 0 s |
|  | testSynchronizerInAction | 0.007 s |
|  | testInitLock | 0.004 s |

<a id="surefire--testdataconfiguration"></a>

### TestDataConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetDoubleList | 0.019 s |
|  | testGetBigDecimalArray | 0.001 s |
|  | testClearPropertyDirect | 0.001 s |
|  | testGetColor | 0 s |
|  | testGetCalendarArrayWithFormat | 0.001 s |
|  | testGetColorArray | 0 s |
|  | testConversionException | 0.004 s |
|  | testGetLocaleList | 0.001 s |
|  | testGetColorList | 0 s |
|  | testConversionExceptionCause | 0.001 s |
|  | testGetShortArray | 0 s |
|  | testGetPropertyWithoutConversion | 0 s |
|  | testGetIntegerList | 0.001 s |
|  | testGetFloatList | 0 s |
|  | testGetDateList | 0.001 s |
|  | testGetDateNoFormatPropertyConversionHandler | 0 s |
|  | testGetByteArray | 0.001 s |
|  | testGetShortList | 0 s |
|  | testGetInetAddressInvalidType | 0.015 s |
|  | testGetURIList | 0.001 s |
|  | testGetURLList | 0.105 s |
|  | testGetLongList | 0.001 s |
|  | testGetBigDecimalList | 0 s |
|  | testGetDate | 0.001 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0.001 s |
|  | testGetByteList | 0 s |
|  | testGetConfiguration | 0 s |
|  | testGetCalendarArray | 0.001 s |
|  | testContainsValue | 0.001 s |
|  | testGetLocaleArray | 0 s |
|  | testGetInternetAddressInvalidType | 0.001 s |
|  | testGetUnknown | 0 s |
|  | testClearPropertyDirectNoAbstractConf | 0.001 s |
|  | testClearProperty | 0 s |
|  | testNullConfiguration | 0 s |
|  | testGetArrayInvalidDefaultType | 0.001 s |
|  | testGetBooleanArray | 0 s |
|  | testGetIntegerArray | 0 s |
|  | testGetFloatArray | 0.001 s |
|  | testGetBooleanList | 0 s |
|  | testGetDateArray | 0.001 s |
|  | testGetDateNoFormatPropertyDirectlySpecified | 0 s |
|  | testGetDoubleArray | 0 s |
|  | testGetUnknownException | 0.001 s |
|  | testGetURIArray | 0 s |
|  | testGetCalendarList | 0.001 s |
|  | testGetLongArray | 0 s |
|  | testGetURLArray | 0.001 s |
|  | testGetInetAddress | 0 s |
|  | testGetCalendar | 0.001 s |
|  | testGetLocale | 0 s |
|  | testGetBigIntegerArray | 0.001 s |
|  | testGetURI | 0 s |
|  | testGetURL | 0.031 s |
|  | testGetInvalidType | 0.001 s |
|  | testGetBigIntegerList | 0 s |
|  | testIsEmpty | 0.001 s |
|  | testGetPrimitiveArrayInvalidType | 0 s |
|  | testGetInternetAddress | 0 s |
|  | testGetDateArrayWithFormat | 0 s |

<a id="surefire--testnodehandlerdecorator"></a>

### TestNodeHandlerDecorator

|  |  |  |
| --- | --- | --- |
|  | testNodeHandlerGetMatchingChildrenCount | 0 s |
|  | testNodeHandlerGetAttributeValue | 0 s |
|  | testNodeHandlerIsDefinedAttributes | 0 s |
|  | testNodeHandlerGetAttributesImmutable | 0 s |
|  | testNodeHandlerIndexOfChild | 0 s |
|  | testNodeHandlerIndexOfUnknownChild | 0 s |
|  | testNodeHandlerGetChildrenCountAll | 0 s |
|  | testNodeHandlerGetChildren | 0 s |
|  | testNodeHandlerHasAttributesFalse | 0 s |
|  | testNodeHandlerGetChildrenByName | 0 s |
|  | testNodeHandlerValue | 0 s |
|  | testNodeHandlerGetChildrenByNameImmutable | 0 s |
|  | testGetParentInvalidNode | 0 s |
|  | testNodeHandlerGetMatchingChildrenImmutable | 0.001 s |
|  | testNodeHandlerHasAttributesTrue | 0 s |
|  | testNodeHandlerIsDefinedFalse | 0 s |
|  | testNodeHandlerIsDefinedValue | 0 s |
|  | testNodeHandlerGetChildAtIndex | 0 s |
|  | testNodeHandlerGetChildrenCountSpecific | 0 s |
|  | testGetParentNode | 0 s |
|  | testNodeHandlerIsDefinedChildren | 0.001 s |
|  | testNodeHandlerGetMatchingChildren | 0 s |
|  | testNodeHandlerGetAttributes | 0 s |
|  | testNodeHandlerName | 0 s |
|  | testGetParentForRoot | 0 s |

<a id="surefire--testjndibuilderparametersimpl"></a>

### TestJndiBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testSetContext | 0 s |
|  | testSetBeanProperties | 0 s |
|  | testGetParametersBaseProperties | 0 s |
|  | testSetPrefix | 0 s |

<a id="surefire--testxmldocumenthelper"></a>

### TestXMLDocumentHelper

|  |  |  |
| --- | --- | --- |
|  | testElementMappingForNewDocument | 0 s |
|  | testInitForNewDocument | 0 s |
|  | testTransformException | 0.008 s |
|  | testInitForSourceDocument | 0.012 s |
|  | testCreateTransformerFactory | 0 s |
|  | testCopyDocument | 0.001 s |
|  | testCopyElementMappingForComplexDocument | 0.002 s |
|  | testCreateDocumentBuilderFromFactoryException | 0.008 s |
|  | testCreateTransformerFactoryException | 0.002 s |
|  | testElementMappingForSourceDocument | 0 s |
|  | testCopyElementMapping | 0 s |

<a id="surefire--testhierarchicalconfigurationevents"></a>

### TestHierarchicalConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0 s |
|  | testSetPropertyEventWithDetails | 0 s |
|  | testSetPropertyEvent | 0 s |
|  | testClearPropertyEventWithDetails | 0 s |
|  | testClearPropertyEvent | 0 s |
|  | testAddPropertyEventWithDetails | 0 s |
|  | testClearEventWithDetails | 0 s |
|  | testAddPropertyEvent | 0 s |
|  | testAddNodesEvent | 0 s |
|  | testSubConfigurationChangedEventNotConnected | 0 s |
|  | testAddNodesEmptyEvent | 0 s |
|  | testSubConfigurationChangedEventConnected | 0.001 s |
|  | testClearTreeEvent | 0 s |

<a id="surefire--testpropertyconverter"></a>

### TestPropertyConverter

|  |  |  |
| --- | --- | --- |
|  | testToCustomNumber | 0 s |
|  | [testToBigDecimalStringConstructor](#surefire--org.apache.commons.configuration2.convert.testpropertyconverter.testtobigdecimalstringconstructor) [+  - [ Detail ]](javascript:toggleDisplay('org.apache.commons.configuration2.convert.TestPropertyConverter.testToBigDecimalStringConstructor');) | 0 s |
| - | void org.apache.commons.configuration2.convert.TestPropertyConverter.testToBigDecimalStringConstructor() is @Disabled | - |
|  | testToNumberDirect | 0 s |
|  | testToNumberFromHexString | 0 s |
|  | testToNumberWithInvalidClass | 0 s |
|  | testToPathFromString | 0 s |
|  | testToNoConversionNeeded | 0 s |
|  | testToPathDirect | 0 s |
|  | testToCharFailed | 0 s |
|  | testToCharViaToString | 0 s |
|  | testToFileFromPath | 0 s |
|  | testToNumberFromInvalidHexString | 0.001 s |
|  | testToPathFromFile | 0 s |
|  | testToEnumFromEnum | 0 s |
|  | testToNumberFromInvalidBinaryString | 0 s |
|  | testToStringConversion | 0 s |
|  | testToFileDirect | 0 s |
|  | testToEnumFromInvalidNumber | 0 s |
|  | testToEnumFromInvalidString | 0 s |
|  | testToNumberFromBinaryString | 0 s |
|  | testToEnumFromNumber | 0 s |
|  | testToEnumFromString | 0 s |
|  | testToPatternDirect | 0 s |
|  | testToNumberFromString | 0 s |
|  | testToPatternFromString | 0 s |
|  | testToNumberFromInvalidString | 0.001 s |
|  | testToCharSuccess | 0 s |
|  | testToBigDecimalDoubleConstructor | 0 s |
|  | testToFileFromString | 0 s |

<a id="surefire--testhierarchicalconfiguration"></a>

### TestHierarchicalConfiguration

|  |  |  |
| --- | --- | --- |
|  | testChildConfigurationsAtNotFound | 0 s |
|  | testConfigurationAtUnknownSubTree | 0 s |
|  | testChildConfigurationsAtWithUpdates | 0.001 s |
|  | testInitCopyNull | 0 s |
|  | testConfigurationsAtAttributeKey | 0 s |
|  | testClone | 0 s |
|  | testInitCopyUpdate | 0 s |
|  | testConfigurationAtUpdateSubConfigConnected | 0 s |
|  | testInterpolationSubset | 0 s |
|  | testConfigurationsAtNoUpdate | 0 s |
|  | testConfigurationAtUnknownSubTreeWithUpdates | 0 s |
|  | testChildConfigurationsAtNoUniqueKey | 0 s |
|  | testConfigurationAtClearAndDetach | 0 s |
|  | testConfigurationAtAttributeNodeWithUpdates | 0 s |
|  | testSubsetMultipleNodesWithValues | 0 s |
|  | testInterpolationSubsetMultipleLayers | 0 s |
|  | testInterpolatedConfigurationEmpty | 0 s |
|  | testConfigurationsAtEmpty | 0 s |
|  | testConfigurationAtUpdateParentConnected | 0 s |
|  | testSubsetNodeWithValue | 0 s |
|  | testConfigurationAtUpdateSubConfigIndependent | 0 s |
|  | testConfigurationAtAttributeNode | 0 s |
|  | testInterpolatedConfiguration | 0.001 s |
|  | testSubsetAttributeResult | 0 s |
|  | testImmutableConfigurationsAt | 0.001 s |
|  | testInitCopy | 0 s |
|  | testConfigurationAtUpdateParentIndependent | 0 s |
|  | testConfigurationAtReadAccess | 0 s |
|  | testConfigurationAtMultipleNodes | 0 s |
|  | testImmutableConfigurationAt | 0 s |
|  | testImmutableChildConfigurationsAt | 0 s |
|  | testImmutableConfigurationAtSupportUpdates | 0 s |
|  | testSubset | 0 s |
|  | testConfigurationsAtWithUpdates | 0.001 s |
|  | testChildConfigurationsAtNoUpdates | 0 s |
|  | testConfigurationAtMultipleNodesWithUpdates | 0 s |
|  | testConfigurationAtWithUpdateInitialized | 0 s |

<a id="surefire--testconfigurationset"></a>

### TestConfigurationSet

|  |  |  |
| --- | --- | --- |
|  | testSize | 0 s |
|  | testIterator | 0 s |

<a id="surefire--testbasenullconfiguration"></a>

### TestBaseNullConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetByteUnknown | 0 s |
|  | testInterpolation | 0 s |
|  | testGetShortUnknown | 0.001 s |
|  | testGetFloat | 0 s |
|  | testGetShort | 0 s |
|  | testCommaSeparatedStringEscaped | 0 s |
|  | testCommaSeparatedString | 0 s |
|  | testGetFloatUnknown | 0 s |
|  | testGetBigIntegerIncompatibleType | 0 s |
|  | testGetByte | 0 s |
|  | testGetList | 0 s |
|  | testGetLong | 0 s |
|  | testGetByteIncompatibleType | 0 s |
|  | testGetBooleanUnknown | 0.001 s |
|  | testThrowExceptionOnMissing | 0 s |
|  | testGetBooleanIncompatibleType | 0 s |
|  | testGetBigDecimalUnknown | 0 s |
|  | testGetBigIntegerUnknown | 0 s |
|  | testGetDoubleIncompatibleType | 0 s |
|  | testGetBoolean | 0 s |
|  | testGetProperty | 0 s |
|  | testGetLongUnknown | 0.001 s |
|  | testPropertyAccess | 0 s |
|  | testGetBigDecimalIncompatibleType | 0 s |
|  | testMultipleInterpolation | 0 s |
|  | testInterpolationLoop | 0 s |
|  | testGetDouble | 0 s |
|  | testGetBigDecimal | 0 s |
|  | testGetListAsScalar | 0 s |
|  | testGetBigInteger | 0 s |
|  | testGetString | 0 s |
|  | testSubset | 0.001 s |
|  | testGetFloatIncompatibleType | 0 s |
|  | testGetDoubleUnknown | 0 s |
|  | testGetLongIncompatibleTypes | 0 s |
|  | testGetStringUnknown | 0 s |
|  | testGetShortIncompatibleType | 0 s |

<a id="surefire--testxmlbuilderparametersimpl"></a>

### TestXMLBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testSetValidating | 0 s |
|  | testSetPublicID | 0 s |
|  | testSetSystemID | 0 s |
|  | testSetSchemaValidation | 0 s |
|  | testSetEntityResolver | 0.002 s |
|  | testInheritFrom | 0.005 s |
|  | testBeanPropertiesAccess | 0 s |
|  | testSetDocumentBuilder | 0 s |

<a id="surefire--testmultifilebuilderparametersimpl"></a>

### TestMultiFileBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testFromParametersNewInstance | 0 s |
|  | testFromParatersNotFound | 0 s |
|  | testClone | 0 s |
|  | testFromParametersFound | 0 s |
|  | testSetManagedBuilderParameters | 0 s |
|  | testSetFilePattern | 0.001 s |
|  | testBeanProperties | 0 s |

<a id="surefire--testqueryresult"></a>

### TestQueryResult

|  |  |  |
| --- | --- | --- |
|  | testEqualsFalse | 0 s |
|  | testGetAttributeValueNoAttributeResult | 0 s |
|  | testToStringNodeResult | 0 s |
|  | testEqualsTrue | 0 s |
|  | testGetAttributeValue | 0 s |
|  | testToStringAttributeResult | 0.001 s |
|  | testEqualsOtherObjects | 0 s |
|  | testIsAttributeResultFalse | 0 s |
|  | testIsAttributeResultTrue | 0 s |

<a id="surefire--testvfsfilehandlerreloadingdetector"></a>

### TestVFSFileHandlerReloadingDetector

|  |  |  |
| --- | --- | --- |
|  | testLastModificationDateFileSystemEx | 0.016 s |
|  | testLastModificationDateUndefinedHandler | 0 s |
|  | testLastModificationDateUnresolvableURI | 0.008 s |
|  | testLastModificationDateNonExisting | 0.003 s |
|  | testGetRefreshDelay | 0.001 s |
|  | testLastModificationDateExisting | 0.002 s |

<a id="surefire--testservletfilterconfiguration"></a>

### TestServletFilterConfiguration

|  |  |  |
| --- | --- | --- |
|  | testListEscaped | 0.001 s |
|  | testList | 0 s |
|  | testSize | 0 s |
|  | testGetBigIntegerConversion | 0 s |
|  | testGetKeys | 0 s |
|  | testContainsKey | 0 s |
|  | testContains | 0 s |
|  | testGetProperty | 0 s |
|  | givenNullIteratorTestContains | 0 s |
|  | testSetLogger | 0 s |
|  | testSizeEmpty | 0 s |
|  | testIsEmpty | 0 s |
|  | givenNullValueTestContains | 0 s |
|  | testContainsValue | 0 s |
|  | testClearProperty | 0 s |
|  | testAddPropertyDirect | 0 s |

<a id="surefire--testimmutableconfiguration"></a>

### TestImmutableConfiguration

|  |  |  |
| --- | --- | --- |
|  | testUnmodifiableConfigurationAccess | 0.003 s |
|  | testUnmodifiableConfigurationLiveUpdate | 0.001 s |
|  | testUnmodifiableHierarchicalConfiguration | 0.001 s |
|  | testImmutableSubset | 0.001 s |
|  | testUnmodifiableConfigurationIterate | 0 s |
|  | testUnmodifiableConfigurationCast | 0.001 s |
|  | testUnmodifiableConfigurationNull | 0 s |
|  | testUnmodifiableConfigurationIteratorRemove | 0 s |
|  | testExceptionHandling | 0.001 s |
|  | testUnmodifiableConfigurationOtherTypes | 0.001 s |

<a id="surefire--testdefaultconversionhandler"></a>

### TestDefaultConversionHandler

|  |  |  |
| --- | --- | --- |
|  | testToArrayNullInput | 0 s |
|  | testToCustomNumber | 0 s |
|  | testToCalendarWithDefaultFormat | 0.001 s |
|  | testSetDateFormat | 0 s |
|  | testToFromEmptyCollection | 0 s |
|  | testToCollectionNullInput | 0 s |
|  | testToNoInterpolator | 0 s |
|  | testToFromCollection | 0 s |
|  | testToArrayPrimitiveSameType | 0 s |
|  | testToFromArray | 0 s |
|  | testToCollectionSuccess | 0 s |
|  | testToFailedConversion | 0 s |
|  | testToWithInterpolator | 0 s |
|  | testToCollectionEmptyString | 0 s |
|  | testToArrayEmptyString | 0 s |
|  | testToFromIterator | 0 s |
|  | testToPrimitive | 0 s |
|  | testToCollectionNullCollection | 0 s |
|  | testToArrayPrimitiveOtherType | 0 s |
|  | testGetDateFormatNotSet | 0 s |
|  | testToArrayObject | 0 s |
|  | testListDelimiterHandler | 0 s |
|  | testToNull | 0 s |
|  | testToDateWithFormat | 0 s |
|  | testToArrayPrimitiveWrapperType | 0 s |

<a id="surefire--testconfigurationnodepointerfactory"></a>

### TestConfigurationNodePointerFactory

|  |  |  |
| --- | --- | --- |
|  | testSimpleXPath | 0.001 s |
|  | testQueryAttribute | 0.001 s |
|  | testText | 0.003 s |
|  | testParentAxis | 0.001 s |
|  | testPrecedingSiblingAxis | 0.001 s |
|  | testIndices | 0.001 s |
|  | testFollowingSiblingAxis | 0 s |
|  | testQueryRootAttribute | 0 s |

<a id="surefire--testconfigurationutils"></a>

### TestConfigurationUtils

|  |  |  |
| --- | --- | --- |
|  | testLoadClassFromCCL | 0 s |
|  | testCloneSynchronizerNoOp | 0 s |
|  | testCloneSynchronizerNull | 0 s |
|  | testCloneIfPossibleError | 0 s |
|  | testConvertToHierarchicalEngine | 0.001 s |
|  | testAsEventSourceUnsupportedMock | 0.002 s |
|  | testAsEventSourceNonSupportedEx | 0 s |
|  | testLoadClassCCLNull | 0 s |
|  | testLoadClassNoExFound | 0 s |
|  | testCloneSynchronizerNewInstance | 0 s |
|  | testConvertHierarchicalToHierarchicalEngine | 0 s |
|  | testCloneConfigurationNull | 0 s |
|  | testEnableRuntimeExceptionsInvalid | 0 s |
|  | testCloneConfigurationNotSupported | 0.001 s |
|  | testEnableRuntimeExceptions | 0 s |
|  | testCopy | 0 s |
|  | testToString | 0 s |
|  | testCloneIfPossibleNull | 0 s |
|  | testCloneConfiguration | 0.001 s |
|  | testCloneIfPossibleNotSupported | 0 s |
|  | testLoadClassCCLNotFound | 0 s |
|  | testConvertNullToHierarchical | 0 s |
|  | testConvertToHierarchicalDelimiters | 0 s |
|  | testLoadClassNoExNotFound | 0 s |
|  | testConvertToHierarchical | 0 s |
|  | testCloneIfPossibleSupported | 0 s |
|  | testConvertToHierarchicalOrderOfProperties | 0 s |
|  | testAsEventSourceSupported | 0 s |
|  | testCloneSynchronizerClone | 0 s |
|  | testEnableRuntimeExceptionsNull | 0 s |
|  | testCloneSynchronizerFailed | 0 s |
|  | testAppend | 0 s |
|  | testConvertHierarchicalToHierarchicalNullEngine | 0 s |
|  | testConvertHierarchicalToHierarchical | 0 s |
|  | testLoadClassNotFound | 0.001 s |
|  | testConvertToHierarchicalMultiValues | 0 s |

<a id="surefire--testdefaultlistdelimiterhandler"></a>

### TestDefaultListDelimiterHandler

|  |  |  |
| --- | --- | --- |
|  | testEscapeWithTransformer | 0 s |
|  | testEscapeList | 0 s |
|  | testSplitSingleElement | 0 s |
|  | testSplitEscapeListDelimiterAndBackslashes | 0 s |
|  | testEscapeIntegerList | 0 s |
|  | testSplitEscapeBackslash | 0 s |
|  | testSplitEscapeLineDelimiter | 0 s |
|  | testSplitList | 0.001 s |
|  | testEscapeStringBackslash | 0 s |
|  | testSplitNoTrim | 0 s |
|  | testSplitUnexpectedEscape | 0 s |
|  | testEscapeStringListDelimiter | 0 s |
|  | testEscapeStringNoSpecialCharacter | 0 s |
|  | testEscapeStringListDelimiterAndBackslash | 0 s |

<a id="surefire--testxpathcontextfactory"></a>

### TestXPathContextFactory

|  |  |  |
| --- | --- | --- |
|  | testCreateContext | 0 s |

<a id="surefire--testnodetreewalker"></a>

### TestNodeTreeWalker

|  |  |  |
| --- | --- | --- |
|  | testWalkDFSTerminate | 0 s |
|  | testWalkDFSNoNode | 0.003 s |
|  | testWalkNoVisitor | 0 s |
|  | testWalkBFS | 0 s |
|  | testWalkDFS | 0 s |
|  | testWalkBFSNoNode | 0 s |
|  | testWalkBFSTerminate | 0 s |
|  | testWalkNoNodeHandler | 0 s |

<a id="surefire--testjndienvironmentvalues"></a>

### TestJNDIEnvironmentValues

|  |  |  |
| --- | --- | --- |
|  | testGetKeysWithExistingPrefix | 0.002 s |
|  | testSimpleGet | 0.001 s |
|  | testGetKeys | 0.001 s |
|  | testContainsKey | 0.001 s |
|  | testThrowExceptionOnMissing | 0.001 s |
|  | testClearProperty | 0.001 s |
|  | testGetMissingKeyWithDefault | 0.001 s |
|  | testMoreGets | 0.001 s |
|  | testGetKeysWithUnknownPrefix | 0.001 s |
|  | testGetMissingKey | 0.001 s |
|  | testIsEmpty | 0.001 s |
|  | testGetKeysWithKeyAsPrefix | 0.001 s |

<a id="surefire--testcatalogresolver"></a>

### TestCatalogResolver

|  |  |  |
| --- | --- | --- |
|  | testDebug | 0 s |
|  | testRewriteSystem | 0.001 s |
|  | testLogger | 0 s |
|  | testPublic | 0.001 s |
|  | testSchemaResolver | 0.001 s |

<a id="surefire--testcombinedreloadingcontroller"></a>

### TestCombinedReloadingController

|  |  |  |
| --- | --- | --- |
|  | testInitNullEntries | 0.001 s |
|  | testResetInitialReloadingState | 0 s |
|  | testGetSubControllers | 0 s |
|  | testCheckForReloadingFalse | 0 s |
|  | testInitNull | 0 s |
|  | testGetSubControllersModify | 0 s |
|  | testResetReloadingState | 0.001 s |
|  | testCheckForReloadingTrue | 0 s |

<a id="surefire--testsubnodeconfiguration"></a>

### TestSubnodeConfiguration

|  |  |  |
| --- | --- | --- |
|  | testInterpolation | 0 s |
|  | testInterpolationFromConfigurationAtWithUpdateSupport | 0 s |
|  | testSetThrowExceptionOnMissingAffectsParent | 0 s |
|  | testClone | 0 s |
|  | testClose | 0.006 s |
|  | testInterpolator | 0 s |
|  | testSetExpressionEngine | 0.001 s |
|  | testGetKeys | 0 s |
|  | testSetListDelimiterHandler | 0 s |
|  | testConfiguarationAtNoUpdates | 0 s |
|  | testInterpolationFromConfigurationAtNoUpdateSupport | 0 s |
|  | testSetProperty | 0.001 s |
|  | testParentChangeDetach | 0 s |
|  | testConfigurationAtWithUpdateSupport | 0 s |
|  | testGetProperties | 0 s |
|  | testInitSubNodeConfig | 0 s |
|  | testInitSubNodeConfigWithNullParent | 0 s |
|  | testLocalInterpolationFromConfigurationAt | 0 s |
|  | testGetNodeModel | 0.001 s |
|  | testLocalLookupsInInterpolatorAreInherited | 0 s |
|  | testAddProperty | 0 s |
|  | testSetThrowExceptionOnMissing | 0 s |
|  | testParentChangeDetatchException | 0.001 s |
|  | testInitSubNodeConfigWithNullNode | 0 s |

<a id="surefire--testconfigurationattributepointer"></a>

### TestConfigurationAttributePointer

|  |  |  |
| --- | --- | --- |
|  | testGetParentPointer | 0 s |
|  | testGetValue | 0 s |
|  | testGetImmediateNode | 0 s |
|  | testGetBaseValue | 0 s |
|  | testAttributeIterator | 0 s |
|  | testGetName | 0 s |
|  | testTestNode | 0 s |
|  | testIsAttribute | 0 s |
|  | testChildIterator | 0 s |
|  | testGetLength | 0 s |
|  | testIsLeaf | 0.001 s |
|  | testIsCollection | 0 s |
|  | testSetValue | 0 s |

<a id="surefire--testpropertiesconfigurationlayout"></a>

### TestPropertiesConfigurationLayout

|  |  |  |
| --- | --- | --- |
|  | testCombineComments | 0.001 s |
|  | testEventAddMultiple | 0 s |
|  | testHeaderComment | 0 s |
|  | testRecursiveLoadCall | 0 s |
|  | testInitCopyModify | 0 s |
|  | testReadAndWrite | 0.001 s |
|  | testReadSimple | 0 s |
|  | testBlankLines | 0 s |
|  | testInit | 0 s |
|  | testSave | 0 s |
|  | testTrimComment | 0 s |
|  | testSetNullComment | 0 s |
|  | testSaveForceSingleLine | 0.001 s |
|  | testEventDelete | 0 s |
|  | testEventAddBefore | 0 s |
|  | testTrimCommentTrainlingCR | 0 s |
|  | testSetGlobalSeparator | 0 s |
|  | testHeaderCommentWithBlanksAndPresetHeaderComment | 0 s |
|  | testSaveCommentForUnexistingProperty | 0 s |
|  | testHeaderCommentNull | 0 s |
|  | testEventAddExisting | 0 s |
|  | testIsSingleLine | 0.001 s |
|  | testSetSeparator | 0 s |
|  | testGetNullLayouttData | 0 s |
|  | testSetLineSeparator | 0 s |
|  | testHeaderCommentWithBlanksAndPropComment | 0 s |
|  | testEventSetNonExisting | 0 s |
|  | testBlankLinesWithHeaderComment | 0 s |
|  | testEventClearConfig | 0 s |
|  | testHeaderCommentWithBlanks | 0 s |
|  | testInitCopy | 0 s |
|  | testInitNull | 0 s |
|  | testEventAdd | 0 s |
|  | testSetLineSeparatorInComments | 0 s |
|  | testLineWithBlank | 0 s |
|  | testGetNonExistingLayouData | 0 s |
|  | testTrimCommentFalse | 0 s |
|  | testIsSingleLineMulti | 0 s |
|  | testSaveEmptyLayout | 0 s |

<a id="surefire--testtrackednodehandler"></a>

### TestTrackedNodeHandler

|  |  |  |
| --- | --- | --- |
|  | testGetRootNode | 0 s |
|  | testGetParent | 0.001 s |

<a id="surefire--testeventlistenerparameters"></a>

### TestEventListenerParameters

|  |  |  |
| --- | --- | --- |
|  | testRegistrationsAfterCreation | 0 s |
|  | testAddEventListener | 0 s |
|  | testAddEventListenerRegistration | 0 s |
|  | testGetParameters | 0 s |

<a id="surefire--testinterpolatorspecification"></a>

### TestInterpolatorSpecification

|  |  |  |
| --- | --- | --- |
|  | testWithPrefixLookupNoLookup | 0 s |
|  | testGetPrefixLookupsModify | 0 s |
|  | testWithPrefixLookupNoPrefix | 0 s |
|  | testGetDefaultLookupsModify | 0 s |
|  | testCreateInstance | 0 s |
|  | testBuilderReuse | 0 s |
|  | testCreateInstanceCollections | 0 s |
|  | testWithDefaultLookupNull | 0 s |
|  | testWithPrefixLookupsNull | 0 s |
|  | testWithDefaultLookupsNull | 0 s |

<a id="surefire--testconfigurationlogger"></a>

### TestConfigurationLogger

|  |  |  |
| --- | --- | --- |
|  | testDummyLogger | 0 s |
|  | testSubClass | 0 s |
|  | testDebug | 0.002 s |
|  | testError | 0 s |
|  | testInfo | 0.001 s |
|  | testWarn | 0 s |
|  | testErrorWithException | 0 s |
|  | testInitNoLoggerClass | 0 s |
|  | testInitNoLoggerName | 0 s |
|  | testWarnWithException | 0 s |
|  | testInitWithLoggerSpec | 0 s |
|  | testIsInfoEnabled | 0 s |
|  | testAbstractConfigurationDefaultLogger | 0 s |
|  | testAbstractConfigurationSetLogger | 0 s |
|  | testIsDebugEnabled | 0 s |
|  | testAbstractConfigurationSetLoggerNull | 0 s |

<a id="surefire--testbaseconfiguration"></a>

### TestBaseConfiguration

|  |  |  |
| --- | --- | --- |
|  | testGetInterpolatedPrimitives | 0 s |
|  | testGetByteUnknown | 0 s |
|  | testInterpolationUnknownProperty | 0 s |
|  | testInterpolation | 0 s |
|  | testNumberConversions | 0 s |
|  | testGetShortUnknown | 0 s |
|  | testGetFloat | 0 s |
|  | testGetShort | 0 s |
|  | testCommaSeparatedStringEscaped | 0 s |
|  | testGetHexadecimalValue | 0 s |
|  | testCommaSeparatedString | 0 s |
|  | testNoInterpolator | 0 s |
|  | testGetFloatUnknown | 0 s |
|  | testGetBigIntegerIncompatibleType | 0 s |
|  | testClone | 0 s |
|  | testInterpolationSubset | 0 s |
|  | testSize | 0 s |
|  | testInterpolationLocalhost | 0 s |
|  | testInterpolationEscaped | 0 s |
|  | testCloneModify | 0.001 s |
|  | testGetInterpolator | 0 s |
|  | testGetDurationUnknown | 0 s |
|  | testGetDuration | 0 s |
|  | testGetByte | 0 s |
|  | testGetEnum | 0 s |
|  | testGetList | 0 s |
|  | testGetLong | 0 s |
|  | testGetInterpolatedList | 0.001 s |
|  | testGetStringForListValue | 0 s |
|  | testGetByteIncompatibleType | 0 s |
|  | testInterpolationConstants | 0 s |
|  | testGetBooleanUnknown | 0 s |
|  | testContainsValue | 0 s |
|  | testThrowExceptionOnMissing | 0 s |
|  | testGetBooleanIncompatibleType | 0 s |
|  | testCloneListProperty | 0 s |
|  | testGetBigDecimalUnknown | 0 s |
|  | testGetBigIntegerUnknown | 0 s |
|  | testGetDoubleIncompatibleType | 0.001 s |
|  | testSetInterpolator | 0 s |
|  | testGetBoolean | 0 s |
|  | testGetProperty | 0 s |
|  | testGetLongUnknown | 0 s |
|  | testInterpolatedConfiguration | 0 s |
|  | testGetDurationIncompatibleType | 0 s |
|  | testPropertyAccess | 0 s |
|  | testGetBigDecimalIncompatibleType | 0 s |
|  | testMultipleInterpolation | 0 s |
|  | testGetBinaryValue | 0.001 s |
|  | testInterpolationLoop | 0 s |
|  | testGetDouble | 0 s |
|  | testGetBigDecimal | 0 s |
|  | testInterpolationSystemProperties | 0 s |
|  | testGetBigInteger | 0 s |
|  | testGetString | 0 s |
|  | testInstallInterpolator | 0 s |
|  | testAddProperty | 0 s |
|  | testSubset | 0 s |
|  | testGetFloatIncompatibleType | 0.001 s |
|  | testGetDoubleUnknown | 0 s |
|  | testInterpolationEnvironment | 0 s |
|  | testGetLongIncompatibleTypes | 0 s |
|  | testGetStringUnknown | 0 s |
|  | testGetShortIncompatibleType | 0.001 s |
|  | testCloneInterpolation | 0 s |

<a id="surefire--testconfigurationinterpolator"></a>

### TestConfigurationInterpolator

|  |  |  |
| --- | --- | --- |
|  | testEnableSubstitutionInVariables | 0 s |
|  | testResolveDefault | 0 s |
|  | testGetDefaultPrefixLookups | 0.001 s |
|  | testResolveWithPrefix | 0 s |
|  | testRegisterLookup | 0 s |
|  | testAddDefaultLookups | 0 s |
|  | testRegisterLookupNullPrefix | 0 s |
|  | testInterpolationBeginningAndEndingRiskyVariableLookups | 0.004 s |
|  | testGetLookupsModify | 0 s |
|  | testInterpolateBlankVariable | 0 s |
|  | testResolveParentVariableNotFound | 0 s |
|  | testInterpolationMultipleVariables | 0.001 s |
|  | testFromSpecificationNewInstance | 0 s |
|  | testAddDefaultLookupsNull | 0 s |
|  | testInterpolationSingleArrayVariable | 0 s |
|  | testDefaultStringLookupsHolderInvalidLookupsDefinition | 0 s |
|  | testRegisterLookupsNull | 0 s |
|  | testInit | 0 s |
|  | testNullSafeLookupExisting | 0 s |
|  | testResolveNoDefault | 0.001 s |
|  | testRemoveDefaultLookup | 0 s |
|  | testDefaultStringLookupsHolderLookupsPropertyNotPresent | 0 s |
|  | testGetDefaultLookupsModify | 0 s |
|  | testFromSpecificationNull | 0 s |
|  | testResolveParentVariableFound | 0 s |
|  | testInterpolationVariableIncomplete | 0 s |
|  | testResolveEmptyVarName | 0 s |
|  | testInterpolateCollection | 0 s |
|  | testDeregisterLookupNonExisting | 0 s |
|  | testInterpolationSingleVariable | 0 s |
|  | testRegisterLookups | 0 s |
|  | testInterpolateEmptyVariable | 0.001 s |
|  | testResolveDefaultEmptyVarName | 0 s |
|  | testResolveEmptyPrefix | 0 s |
|  | testPrefixSetModify | 0 s |
|  | testDeregisterLookup | 0 s |
|  | testDefaultStringLookupsHolderMultipleLookups | 0 s |
|  | testInterpolateObject | 0 s |
|  | testNullSafeLookupNull | 0 s |
|  | testDefaultStringLookupsHolderAllLookups | 0 s |
|  | testRemoveDefaultLookupNonExisting | 0 s |
|  | testInterpolateString | 0 s |
|  | testRegisterLookupNull | 0 s |
|  | testInterpolationSingleCollectionVariable | 0 s |
|  | testInterpolationMultipleCollectionVariables | 0.001 s |
|  | testDefaultStringLookupsHolderGivenSingleLookup | 0 s |
|  | testSetStringConverterNullArgumentUsesDefault | 0 s |
|  | testDefaultStringLookupsHolderGivenSingleLookupWeirdString | 0 s |
|  | testResolveNull | 0 s |
|  | testInterpolationSingleVariableDefaultValue | 0 s |
|  | testInterpolateStringUnknownVariable | 0.001 s |
|  | testInterpolationMultipleSimpleNonStringVariables | 0 s |
|  | testInterpolationMultipleArrayVariables | 0 s |
|  | testGetDefaultPrefixLookupsModify | 0 s |
|  | testResolveDefaultAfterPrefixFails | 0 s |
|  | testResolveWithUnknownPrefix | 0 s |
|  | testInterpolateArray | 0 s |
|  | testSetStringConverter | 0 s |
|  | testFromSpecificationInterpolator | 0 s |
|  | testDefaultStringLookupsHolderLookupsPropertyEmptyAndBlank | 0 s |

<a id="surefire--testevent"></a>

### TestEvent

|  |  |  |
| --- | --- | --- |
|  | testToString | 0 s |
|  | testInitNoType | 0 s |
|  | testInitNoSource | 0 s |

<a id="surefire--testtrackednodemodel"></a>

### TestTrackedNodeModel

|  |  |  |
| --- | --- | --- |
|  | testClear | 0.033 s |
|  | testClose | 0 s |
|  | testGetInMemoryRepresentation | 0.006 s |
|  | testClearTree | 0.001 s |
|  | testAddNodes | 0 s |
|  | testGetNodeHandler | 0.001 s |
|  | testCloseMultipleTimes | 0 s |
|  | testClearProperty | 0 s |
|  | testSetProperty | 0.001 s |
|  | testSetRootNode | 0 s |
|  | testInitNoParentModel | 0 s |
|  | testAddProperty | 0.003 s |
|  | testInitNoSelector | 0 s |

<a id="surefire--testfilebasedconfigurationbuilder"></a>

### TestFileBasedConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testAutoSave | 0.002 s |
|  | testGetConfigurationNoLocation | 0.001 s |
|  | testGetConfigurationLoadFromFile | 0.001 s |
|  | testFileBasedConfigurationBuilderWithHomeDirectoryLocationStrategy | 0.001 s |
|  | testResetLocation | 0 s |
|  | testDisableAutoSave | 0.001 s |
|  | testSetLocationNoFileHandler | 0.001 s |
|  | testChangeLocationAfterCreation | 0 s |
|  | testInitFileHandlerSetDefaultEncoding | 0.001 s |
|  | testAutoSaveWithReset | 0 s |
|  | testSave | 0.001 s |
|  | testGetDefaultEncodingInterface | 0 s |
|  | testLocationSurvivesResetResult | 0.001 s |
|  | testInitFileHandlerOverrideDefaultEncoding | 0 s |
|  | testGetConfigurationLoadFromJarFile | 0.002 s |
|  | testAutoSaveWithPropertiesConfiguration | 0 s |
|  | testGetDefaultEncodingSubClass | 0.001 s |
|  | testGetDefaultEncodingXmlProperties | 0 s |
|  | testChangeLocationAfterReset | 0.001 s |
|  | testCreateConfigurationNonExistingFileAndThenSave | 0 s |
|  | testGetDefaultEncodingProperties | 0 s |
|  | testInitAllowFailOnInitFlag | 0.001 s |
|  | testSetDefaultEncodingNull | 0 s |
|  | testSaveNewFile | 0.001 s |
|  | testLocationIsFullyDefined | 0 s |

<a id="surefire--testinmemorynodemodel"></a>

### TestInMemoryNodeModel

|  |  |  |
| --- | --- | --- |
|  | testConcurrentUpdate | 0.006 s |
|  | testCompactReplacementMapping | 0.021 s |
|  | testAddNodesToAttribute | 0 s |
|  | testClearPropertyAttribute | 0.001 s |
|  | testClearTreeAttribute | 0 s |
|  | testSetPropertyNoChanges | 0 s |
|  | testSetPropertyClearValues | 0 s |
|  | testClearTreeNodesAndAttributes | 0 s |
|  | testClearTreeNodeRemovedFromParentMapping | 0.001 s |
|  | testClear | 0 s |
|  | testClearTreeRootNode | 0 s |
|  | testClearTreeRemoveUndefinedNodes | 0 s |
|  | testGetInMemoryRepresentation | 0 s |
|  | testAddNodesToExistingNode | 0 s |
|  | testAddPropertyNoValues | 0 s |
|  | testGetNodeHandler | 0.001 s |
|  | testClearPropertyNode | 0 s |
|  | testAddNodesEmptyCollection | 0 s |
|  | testClearTreeNonExistingKey | 0 s |
|  | testClearTreeChildrenRemovedFromParentMapping | 0 s |
|  | testAddPropertyAttributeWithPathNodes | 0.001 s |
|  | testAddNodesNullCollection | 0 s |
|  | testAddNodesToNewAttributeKey | 0.001 s |
|  | testClearTreeResultIsEmpty | 0 s |
|  | testSetPropertyNewValues | 0 s |
|  | testAddPropertyUpdateParentReferences | 0.001 s |
|  | testClearTreeUpdateParentReferences | 0.001 s |
|  | testSetPropertyChangedValues | 0.004 s |
|  | testAddPropertyNoPathNodes | 0 s |
|  | testSetRootNull | 0.001 s |
|  | testAddPropertyWithPathNodes | 0 s |
|  | testAddPropertyAttributeNoPathNodes | 0 s |
|  | testSetRoot | 0 s |
|  | testClearTreeNodes | 0 s |
|  | testGetRootNodeFromConstructor | 0 s |
|  | testClearPropertyNonExisting | 0 s |
|  | testInitDefaultRoot | 0.001 s |
|  | testAddPropertyAttributeWithSinglePathNode | 0 s |
|  | testAddNodesToNewNode | 0 s |

<a id="surefire--testnulljndienvironmentvalues"></a>

### TestNullJNDIEnvironmentValues

|  |  |  |
| --- | --- | --- |
|  | testGetKeysWithExistingPrefix | 0.002 s |
|  | testSimpleGet | 0.001 s |
|  | testGetKeys | 0.001 s |
|  | testContainsKey | 0.001 s |
|  | testThrowExceptionOnMissing | 0.001 s |
|  | testClearProperty | 0.001 s |
|  | testGetMissingKeyWithDefault | 0.001 s |
|  | testMoreGets | 0.001 s |
|  | testGetKeysWithUnknownPrefix | 0.001 s |
|  | testGetMissingKey | 0.001 s |
|  | testIsEmpty | 0.001 s |
|  | testGetKeysWithKeyAsPrefix | 0.001 s |

<a id="surefire--testdatabaseconfigurationevents"></a>

### TestDatabaseConfigurationEvents

|  |  |  |
| --- | --- | --- |
|  | testClearEvent | 0.015 s |
|  | testSetPropertyEventWithDetails | 0.014 s |
|  | testSetPropertyEvent | 0.020 s |
|  | testClearPropertyEventWithDetails | 0.013 s |
|  | testClearPropertyEvent | 0.013 s |
|  | testAddPropertyEventWithDetails | 0.015 s |
|  | testClearEventWithDetails | 0.012 s |
|  | testAddPropertyEvent | 0.015 s |

<a id="surefire--testnodenamematchers"></a>

### TestNodeNameMatchers

|  |  |  |
| --- | --- | --- |
|  | testEqualsNoMatch | 0 s |
|  | testEqualsMatch | 0 s |
|  | testEqualsIgnoreCaseNullCriterion | 0 s |
|  | testEqualsIgnoreCaseMatch | 0 s |
|  | testEqualsIgnoreCaseNoMatch | 0 s |
|  | testEqualsNullCriterion | 0 s |

<a id="surefire--testsystemconfiguration"></a>

### TestSystemConfiguration

|  |  |  |
| --- | --- | --- |
|  | testSystemConfiguration | 0 s |
|  | testSetSystemPropertiesFromPropertiesFile | 0.001 s |
|  | testSetSystemProperties | 0 s |
|  | testChangeSystemProperties | 0.001 s |
|  | testAppendWhileConcurrentAccess | 0.001 s |

<a id="surefire--testconfigurationconverter"></a>

### TestConfigurationConverter

|  |  |  |
| --- | --- | --- |
|  | testConfigurationToMap | 0 s |
|  | testConfigurationToPropertiesDefaultListHandling | 0.001 s |
|  | testPropertiesToConfiguration | 0 s |
|  | testConfigurationToPropertiesScalarValue | 0 s |
|  | testConfigurationToPropertiesListDelimiterHandler | 0 s |
|  | testConfigurationToPropertiesNoAbstractConfiguration | 0.001 s |

<a id="surefire--testpropertylistparser"></a>

### TestPropertyListParser

|  |  |  |
| --- | --- | --- |
|  | testParseDate | 0 s |
|  | testUnescapeQuotes | 0.001 s |
|  | testRemoveQuotes | 0 s |
|  | testFilterData | 0 s |

<a id="surefire--testxpathexpressionengine"></a>

### TestXPathExpressionEngine

|  |  |  |
| --- | --- | --- |
|  | testCanonicalKeyRootNoParentKey | 0 s |
|  | testNodeKeyForRootChild | 0.001 s |
|  | testPrepareAddNode | 0.022 s |
|  | testPrepareAddPath | 0 s |
|  | testCanonicalKeyNoDuplicates | 0 s |
|  | testPrepareAddInvalidPathWithSlash | 0.001 s |
|  | testPrepareAddInvalidAttributePath | 0 s |
|  | testNodeKeyNormal | 0 s |
|  | testCanonicalKeyRootWithParentKey | 0 s |
|  | testQueryWithEmptyKey | 0 s |
|  | testDefaultContextFactory | 0 s |
|  | testNodeKeyAttribute | 0 s |
|  | testCanonicalKeyWithDuplicates | 0 s |
|  | testPrepareAddInvalidPath | 0 s |
|  | testQueryNodeExpression | 0 s |
|  | testPrepareAddInvalidAttributePath2 | 0.001 s |
|  | testPrepareAddRootAttribute | 0 s |
|  | testPrepareAddEmptyPath | 0 s |
|  | testPrepareAddEmptyKey | 0 s |
|  | testNodeKeyForRootNode | 0.001 s |
|  | testPrepareAddRootChild | 0 s |
|  | testQueryAttributeExpression | 0 s |
|  | testCanonicalKeyNoParentKey | 0.001 s |
|  | testQueryWithoutResult | 0 s |
|  | testPrepareAddInvalidPathMultipleAttributes | 0 s |
|  | testPrepareAddToAttributeResult | 0 s |
|  | testNodePointerFactory | 0.002 s |
|  | testPrepareAddAttribute | 0 s |
|  | testAttributeKeyOfRootNode | 0 s |
|  | testPrepareAddAttributePath | 0.001 s |
|  | testNodeKeyNoNodeName | 0 s |
|  | testPrepareAddInvalidParent | 0 s |
|  | testQueryWithNullKey | 0 s |
|  | testPrepareAddNullKey | 0.001 s |

<a id="surefire--testnodeadddata"></a>

### TestNodeAddData

|  |  |  |
| --- | --- | --- |
|  | testPathNodesNullModify | 0 s |
|  | testPathNodesDefinedModify | 0 s |
|  | testPathNodesNull | 0 s |
|  | testInitPathNodesDefensiveCopy | 0 s |

<a id="surefire--testabstractconfigurationsynchronization"></a>

### TestAbstractConfigurationSynchronization

|  |  |  |
| --- | --- | --- |
|  | testGetKeysPrefixSynchronized | 0 s |
|  | testContainsKeySychronized | 0 s |
|  | testGetKeysSynchronized | 0.001 s |
|  | testLockNull | 0 s |
|  | testLockRead | 0 s |
|  | testUnlockRead | 0 s |
|  | testUnlockWrite | 0 s |
|  | testClearSynchronized | 0 s |
|  | testAddPropertySynchronized | 0 s |
|  | testGetPropertySynchronized | 0 s |
|  | testLockWrite | 0.001 s |
|  | testIsEmptySynchronized | 0 s |
|  | testCopySynchronized | 0 s |
|  | testDefaultSynchronizer | 0 s |
|  | testClearPropertySynchronized | 0.001 s |
|  | testSubsetSynchronized | 0 s |
|  | testSizeSynchronized | 0 s |
|  | testSetPropertySynchronized | 0 s |
|  | testAppendSynchronized | 0.001 s |

<a id="surefire--testeventlistenerlist"></a>

### TestEventListenerList

|  |  |  |
| --- | --- | --- |
|  | testReceiveEventDifferentType | 0 s |
|  | testGetEventListenersIteratorRemove | 0 s |
|  | testRemoveEventListenerNonExistingListener | 0 s |
|  | testGetEventListenersIteratorNextNoElement | 0 s |
|  | testClear | 0 s |
|  | testGetRegistrations | 0 s |
|  | testListenerRegistrationWithNullListenerData | 0.001 s |
|  | testReceiveEventSubType | 0 s |
|  | testListenerRegistrationWithListenerData | 0 s |
|  | testRemoveEventListenerNullListener | 0 s |
|  | testEventListenerIteratorNullEvent | 0 s |
|  | testRemoveEventListenerExisting | 0 s |
|  | testRemoveEventListenerNullType | 0 s |
|  | testFireNullEvent | 0 s |
|  | testRemoveEventListenerNullRegistration | 0 s |
|  | testAddAllNull | 0 s |
|  | testReceiveEventOfExactType | 0 s |
|  | testGetEventListenersNull | 0 s |
|  | testGetEventListenersMatchingType | 0 s |
|  | testEventListenerIteratorWrongEvent | 0 s |
|  | testRegisterListenerNull | 0 s |
|  | testRemoveEventListenerNonExistingEventType | 0 s |
|  | testGetRegistrationsModify | 0 s |
|  | testGetEventListenersNoMatch | 0 s |
|  | testSuppressEventOfSuperType | 0 s |
|  | testGetEventListenersBaseType | 0 s |
|  | testAddAll | 0 s |
|  | testReceiveEventMultipleListeners | 0 s |
|  | testMultipleListenerRegistration | 0 s |
|  | testRegisterEventTypeNull | 0 s |
|  | testGetEventListenerRegistrationsForSuperType | 0 s |

<a id="surefire--testxmlpropertylistconfiguration"></a>

### TestXMLPropertyListConfiguration

|  |  |  |
| --- | --- | --- |
|  | testAddDataProperty | 0.021 s |
|  | testSetDataProperty | 0.003 s |
|  | testAddList | 0.003 s |
|  | testArray | 0.003 s |
|  | testDate | 0.002 s |
|  | testReal | 0.002 s |
|  | testSave | 0.009 s |
|  | testLoadNoDict | 0.003 s |
|  | testSaveEmptyDictionary | 0.004 s |
|  | testLoadNoDictConstr | 0.003 s |
|  | testDictionaryArray | 0.001 s |
|  | testAddArray | 0.002 s |
|  | testBoolean | 0.002 s |
|  | testDictionary | 0.001 s |
|  | testSaveNoEncoding | 0.002 s |
|  | testSetDatePropertyInvalid | 0.003 s |
|  | testInitCopy | 0.002 s |
|  | testInteger | 0.002 s |
|  | testNested | 0.001 s |
|  | testSaveWithEncoding | 0.002 s |
|  | testSetList | 0.001 s |
|  | testWriteCalledDirectly | 0.002 s |
|  | testString | 0.001 s |
|  | testSubset | 0.001 s |
|  | testNestedArray | 0.001 s |
|  | testSetArray | 0.001 s |

<a id="surefire--testconfigurationdeclaration"></a>

### TestConfigurationDeclaration

|  |  |  |
| --- | --- | --- |
|  | testConfigurationDeclarationIsReservedOptional | 0 s |
|  | testConfigurationDeclarationGetAttributes | 0 s |
|  | testConfigurationDeclarationIsReservedAt | 0 s |
|  | testConfigurationDeclarationIsReserved | 0 s |
|  | testConfigurationDeclarationOptionalAttributeInvalid | 0 s |

<a id="surefire--teststrictconfigurationcomparator"></a>

### TestStrictConfigurationComparator

|  |  |  |
| --- | --- | --- |
|  | testCompareNull | 0 s |
|  | testCompare | 0 s |

<a id="surefire--testxmlconfiguration"></a>

### TestXMLConfiguration

|  |  |  |
| --- | --- | --- |
|  | testDelimiterParsingDisabledXPath | 0.002 s |
|  | testLoadInvalidXML | 0.002 s |
|  | testPreserveSpace | 0.001 s |
|  | testGetComplexProperty | 0.001 s |
|  | testSetAttribute | 0.001 s |
|  | testSaveWithDoctypeIDs | 0.004 s |
|  | testAddObjectProperty | 0.001 s |
|  | testSetRootNamespace | 0.004 s |
|  | testAutoSaveWithSubnodeConfig | 0.004 s |
|  | testCopyRootNameNoDocument | 0.001 s |
|  | testAddList | 0 s |
|  | testLoadWithRootNamespace | 0.002 s |
|  | testLoadWithEncoding | 0.001 s |
|  | testAttributeKeyWithMultipleValues | 0.003 s |
|  | testDtd | 0.004 s |
|  | testClearPropertyNonText | 0.002 s |
|  | testCopyRootName | 0.002 s |
|  | testSaveAfterCreateWithCopyConstructor | 0.001 s |
|  | testgetProperty | 0.001 s |
|  | testClone | 0.001 s |
|  | testSaveWindowsPath | 0.002 s |
|  | testWrite | 0.002 s |
|  | testSave | 0.003 s |
|  | testClearPropertySingleElement | 0.001 s |
|  | testCloneWithSave | 0.002 s |
|  | testEmptyElements | 0.003 s |
|  | testListWithAttributesMultiValue | 0.001 s |
|  | testSplitLists | 0.001 s |
|  | testXPathExpressionEngine | 0.002 s |
|  | testSaveToStreamWithEncoding | 0.003 s |
|  | testListWithAttributes | 0.002 s |
|  | testAutoSaveAddNodes | 0.002 s |
|  | testSetTextRootElement | 0.003 s |
|  | testPublicIdSynchronized | 0.002 s |
|  | testSaveToStream | 0.002 s |
|  | testValidating | 0.002 s |
|  | testSaveWithRootAttributesByHand | 0.002 s |
|  | testOverrideAttribute | 0.001 s |
|  | testSaveWithRootAttributes | 0.001 s |
|  | testClearAttributeNonExisting | 0.001 s |
|  | testSaveWithInvalidTransformerFactory | 0.002 s |
|  | testSaveWithDelimiterParsingDisabled | 0.004 s |
|  | testAutoSaveWithSubSubnodeConfig | 0.003 s |
|  | testReadDomElement | 0.001 s |
|  | testSaveWithDoctype | 0.002 s |
|  | testSaveWithValidation | 0.005 s |
|  | testGetPropertyWithXMLEntity | 0.001 s |
|  | testClearPropertyNotExisting | 0.001 s |
|  | testPreserveSpaceInvalid | 0.001 s |
|  | testWriteIndentSize | 0.001 s |
|  | testNoDelimiterParsingInAttrValues | 0.001 s |
|  | testPreserveSpaceOnElement | 0.001 s |
|  | testSetPropertyListWithDelimiterParsingDisabled | 0.003 s |
|  | testDelimiterParsingDisabled | 0.001 s |
|  | testClearPropertyMultipleSiblings | 0.002 s |
|  | testClearPropertySingleElementWithAttribute | 0.001 s |
|  | testReadDomElementManually | 0.002 s |
|  | testLoadAndSaveFromFile | 0.002 s |
|  | testCopyNull | 0 s |
|  | testAddPropertyListWithDelimiterParsingDisabled | 0.002 s |
|  | testSetProperty | 0.001 s |
|  | testValidatingInvalidFile | 0.001 s |
|  | testAddNodesAndSave | 0.004 s |
|  | testClearAttributeSingle | 0.001 s |
|  | testGetProperty | 0.001 s |
|  | testEmptyReload | 0.002 s |
|  | testCustomDocBuilder | 0.001 s |
|  | testEmptyAttribute | 0.002 s |
|  | testCustomDocBuilderValidationError | 0.001 s |
|  | testPreserveSpaceOverride | 0.001 s |
|  | testComplexNames | 0.001 s |
|  | testSaveWithValidationFailure | 0.004 s |
|  | testSaveToURL | 0.003 s |
|  | testClearPropertyCData | 0.001 s |
|  | testInitCopy | 0.002 s |
|  | testSaveWithNullEncoding | 0.001 s |
|  | testLoadChildNamespace | 0.001 s |
|  | testGetAttribute | 0.001 s |
|  | testListWithMultipleAttributesMultiValue | 0 s |
|  | testAppend | 0.002 s |
|  | testSystemIdSynchronized | 0 s |
|  | testAddNodesToSubnodeConfiguration | 0.001 s |
|  | testAddNodesCopy | 0.003 s |
|  | testSaveDelimiterParsingDisabled | 0.003 s |
|  | testSetRootAttribute | 0.003 s |
|  | testGetCommentedProperty | 0.001 s |
|  | testSaveWithEncoding | 0.001 s |
|  | testWriteWithTransformer | 0.001 s |
|  | testAddProperty | 0.001 s |
|  | testSaveAttributes | 0.002 s |
|  | testSubset | 0.002 s |
|  | testCustomDocBuilderValidationSuccess | 0.002 s |
|  | testClearPropertyMultipleDisjoined | 0.001 s |
|  | testClearTextRootElement | 0.001 s |
|  | testConcurrentGetAndReload | 0.008 s |
|  | testAddObjectAttribute | 0.001 s |
|  | testReadCalledDirectly | 0.001 s |
|  | testLoadFromStream | 0 s |
|  | testClearAttributeMultipleDisjoined | 0.001 s |

<a id="surefire--testreloadingfilebasedconfigurationbuilder"></a>

### TestReloadingFileBasedConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testGetConfigurationNoLocation | 0 s |
|  | testCreateReloadingDetectoryCustomFactory | 0.002 s |
|  | testCreateReloadingDetectorDefaultFactory | 0 s |
|  | testReloadingControllerEvents | 0 s |
|  | testReloadingDetectorNoFileHandler | 0 s |
|  | testResetReloadingStateInGetConfiguration | 0 s |
|  | testReloadingDetectorReloadingPerformed | 0 s |
|  | testInitAllowFailOnInitFlag | 0 s |
|  | testReloadingDetectorIsReloadingRequired | 0 s |

<a id="surefire--testdefaultbeanfactory"></a>

### TestDefaultBeanFactory

|  |  |  |
| --- | --- | --- |
|  | testFindMatchingConstructorAmbiguous | 0 s |
|  | testFindMatchingConstructorNoArgs | 0 s |
|  | testInitWithConversionHandler | 0.004 s |
|  | testFindMatchingConstructorExplicitType | 0 s |
|  | testFindMatchingConstructorNoMatch | 0 s |
|  | testCreateBean | 0 s |
|  | testCreateBeanConstructorNestedBean | 0.001 s |
|  | testCreateBeanConstructor | 0 s |
|  | testGetDefaultBeanClass | 0 s |
|  | testFindMatchingConstructorArgCount | 0 s |
|  | testDefaultConversionHandler | 0 s |

<a id="surefire--testdatabasebuilderparametersimpl"></a>

### TestDatabaseBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testSetConfigurationNameColumn | 0 s |
|  | testSetValueColumn | 0 s |
|  | testSetDataSource | 0 s |
|  | testSetConfigurationName | 0 s |
|  | testSetKeyColumn | 0 s |
|  | testSetAutoCommit | 0 s |
|  | testBeanProperties | 0.001 s |
|  | testSetTable | 0 s |

<a id="surefire--testcopyobjectdefaulthandler"></a>

### TestCopyObjectDefaultHandler

|  |  |  |
| --- | --- | --- |
|  | testInitializeDefaultsBaseType | 0.002 s |
|  | testInitNull | 0 s |
|  | testInitializeDefaultsException | 0.001 s |
|  | testInitializeDefaultsSameType | 0 s |

<a id="surefire--testhierarchicalbuilderparametersimpl"></a>

### TestHierarchicalBuilderParametersImpl

|  |  |  |
| --- | --- | --- |
|  | testSetExpressionEngine | 0 s |
|  | testInheritFrom | 0 s |
|  | testBeanPropertiesAccess | 0 s |

<a id="surefire--testreloadingmultifileconfigurationbuilder"></a>

### TestReloadingMultiFileConfigurationBuilder

|  |  |  |
| --- | --- | --- |
|  | testReloadingControllerCheckReloadingRequired | 0.001 s |
|  | testReloadingControllerResetReloadingState | 0.001 s |
|  | testInitWithParameters | 0 s |
|  | testCreateManagedBuilderWithAllowFailFlag | 0.001 s |
|  | testCreateManagedBuilder | 0 s |
|  | testReloadingControllerCheck | 0 s |

<a id="surefire--failure-details"></a>

## Failure Details

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

|  |  |
| --- | --- |
|  | testListOfObjects |
| - | skipped: void org.apache.commons.configuration2.TestJSONConfiguration.testListOfObjects() is @Disabled |
|  | testToBigDecimalStringConstructor |
| - | skipped: void org.apache.commons.configuration2.convert.TestPropertyConverter.testToBigDecimalStringConstructor() is @Disabled |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/rat-report.html -->

<!-- page_index: 15 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

# RAT (Release Audit Tool) results

The following document contains the results of [RAT (Release Audit Tool)](https://creadur.apache.org/rat/apache-rat-plugin/) Apache Creadur RAT::Plugin4Maven 0.17 (Apache Software Foundation).

```
*****************************************************
Summary
*****************************************************
Generated at: 2026-04-08T14:57:30Z
    by Apache Creadur RAT::Core 0.17 (Apache Software Foundation)

-----------------------------------------------------
Counters
-----------------------------------------------------
    (Entries starting with '!' exceed the minimum or maximum values)
  Approved:           661    A count of approved licenses.
  Archives:           1    A count of archive files.
  Binaries:           12    A count of binary files.
  Document types:     5    A count of distinct document types.
  Ignored:            12    A count of ignored files.
  License categories: 2    A count of distinct license categories.
  License names:      2    A count of distinct license names.
  Notices:            3    A count of notice files.
  Standards:          663    A count of standard files.
! Unapproved:         2    A count of unapproved licenses.
  Unknown:            2    A count of unknown file types.


-----------------------------------------------------
Licenses detected
-----------------------------------------------------

Apache License 2.0: 661 
Unknown license: 2 

-----------------------------------------------------
License Categories detected
-----------------------------------------------------

?????: 2 
AL   : 661 

-----------------------------------------------------
Document Types detected
-----------------------------------------------------

ARCHIVE: 1 
BINARY: 12 
IGNORED: 12 
NOTICE: 3 
STANDARD: 663 

*****************************************************
Files with unapproved licenses
*****************************************************

  /src/conf/cpd-exclusions.txt
  /src/test/resources/test.yaml

*****************************************************
Archives
*****************************************************

 /src/test/resources/org/apache/commons/configuration2/test.jar

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

  /.checkstyle
  I         application/octet-stream    

  /.classpath
  I         text/plain    

  /.git
  I         application/octet-stream     (directory)

  /.github
  I         application/octet-stream     (directory)

  /.gitignore
  I         application/octet-stream    

  /.project
  I         text/plain    

  /.settings
  I         application/octet-stream     (directory)

  /CODE_OF_CONDUCT.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /CONTRIBUTING.md
  S         text/x-web-markdown    ISO-8859-1
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

  /src/changes/changes.xml
  I         application/xml    ISO-8859-1

  /src/changes/release-notes.vm
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/CommonsConfiguration.xsd
  S         application/xml    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/conf/HEADER.txt
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/checkstyle-suppressions.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/conf/checkstyle.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

! /src/conf/cpd-exclusions.txt
  S         text/plain    ISO-8859-1
    ?????    ?????         Unknown license (Unapproved)

  /src/conf/findbugs-exclude-filter.xml
  I         application/xml    ISO-8859-1

  /src/conf/security/README.md
  S         text/x-web-markdown    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/conf/security/VEX.cyclonedx.xml
  S         application/xml    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/main/assembly/bin.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/assembly/src.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/AbstractConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/AbstractHierarchicalConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/AbstractYAMLBasedConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/BaseConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/BaseConfigurationXMLReader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/BaseHierarchicalConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/CombinedConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/CompositeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/Configuration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationComparator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationConsumer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationConverter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationDecoder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationMap.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ConfigurationXMLReader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/DataConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/DatabaseConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/DynamicCombinedConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/EnvironmentConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/FileBasedConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/FindNodeVisitor.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/HierarchicalConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/HierarchicalConfigurationConverter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/HierarchicalConfigurationXMLReader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/INIConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ImmutableConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ImmutableConfigurationInvocationHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ImmutableHierarchicalConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/Initializable.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/JNDIConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/JSONConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/MapConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/PatternSubtreeConfigurationWrapper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/PrefixedKeysIterator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/PropertiesConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/PropertiesConfigurationLayout.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/StrictConfigurationComparator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/SubnodeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/SubsetConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/SystemConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/XMLConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/XMLDocumentHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/XMLListReference.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/XMLPropertiesConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/YAMLConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/BeanCreationContext.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/BeanDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/BeanFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/BeanHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/CombinedBeanDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/ConfigurationDynaBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/ConfigurationDynaClass.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/ConstructorArg.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/DefaultBeanFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/XMLBeanDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/beanutils/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/AutoSaveListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/BasicBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/BasicBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/BasicConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/BuilderConfigurationWrapperFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/BuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/ConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/ConfigurationBuilderEvent.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/ConfigurationBuilderResultCreatedEvent.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/CopyObjectDefaultHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/DatabaseBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/DatabaseBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/DefaultParametersHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/DefaultParametersManager.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/DefaultReloadingDetectorFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/EventListenerParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/EventListenerProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/FileBasedBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/FileBasedBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/FileBasedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/HierarchicalBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/HierarchicalBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/INIBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/INIBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/JndiBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/JndiBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/PropertiesBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/PropertiesBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/ReloadingBuilderSupportListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/ReloadingDetectorFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/ReloadingFileBasedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/XMLBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/XMLBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/BaseConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/CombinedBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/CombinedBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/CombinedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/CombinedConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/ConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/ConfigurationDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/FileExtensionConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/MultiFileBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/MultiFileBuilderProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/MultiFileConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/MultiFileConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/MultiWrapDynaBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/MultiWrapDynaClass.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/ReloadingCombinedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/ReloadingMultiFileConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/combined/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/CombinedBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/Configurations.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/DatabaseBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/FileBasedBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/HierarchicalBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/INIBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/JndiBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/MultiFileBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/Parameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/PropertiesBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/XMLBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/fluent/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/builder/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/AbstractListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/ConversionHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/DefaultConversionHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/DefaultListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/DisabledListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/LegacyListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/ListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/PropertyConverter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/ValueTransformer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/convert/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/BaseEventSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/ConfigurationErrorEvent.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/ConfigurationEvent.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/Event.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/EventListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/EventListenerList.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/EventListenerRegistrationData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/EventSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/EventType.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/event/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ex/ConfigurationException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ex/ConfigurationRuntimeException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ex/ConversionException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/ex/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/ConfigurationInterpolator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/ConstantLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/DefaultLookups.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/DummyLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/EnvironmentLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/ExprLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/InterpolatorSpecification.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/Lookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/StringLookupAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/SystemPropertiesLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/interpol/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/AbsoluteNameLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/BasePathLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/ClasspathLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/CombinedLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/ConfigurationLogger.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/DefaultFileSystem.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileBased.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileHandlerListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileHandlerListenerAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileLocator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileLocatorAware.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileLocatorUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileOptionsProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileSystem.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileSystemLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/FileUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/HomeDirectoryLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/InputStreamSupport.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/ProvidedURLLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/URLConnectionOptions.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/VFSFileSystem.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/VerifiableOutputStream.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/io/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/plist/PropertyListConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/plist/XMLPropertyListConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/plist/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/CombinedReloadingController.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/FileHandlerReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/ManagedReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/ManagedReloadingDetectorMBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/PeriodicReloadingTrigger.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/ReloadingController.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/ReloadingControllerSupport.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/ReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/ReloadingEvent.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/VFSFileHandlerReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/reloading/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/resolver/CatalogResolver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/resolver/DefaultEntityResolver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/resolver/EntityRegistry.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/resolver/EntityResolverSupport.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/resolver/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/spring/ConfigurationPropertiesFactoryBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/spring/ConfigurationPropertySource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/spring/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/sync/LockMode.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/sync/NoOpSynchronizer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/sync/ReadWriteSynchronizer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/sync/Synchronizer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/sync/SynchronizerSupport.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/sync/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/AbstractImmutableNodeHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ConfigurationNodeVisitor.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ConfigurationNodeVisitorAdapter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/DefaultConfigurationKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/DefaultExpressionEngine.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/DefaultExpressionEngineSymbols.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ExpressionEngine.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ImmutableNode.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/InMemoryNodeModel.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/InMemoryNodeModelSupport.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/MergeCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ModelTransaction.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeAddData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeHandlerDecorator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeKeyResolver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeMatcher.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeModel.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeModelSupport.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeNameMatchers.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeSelector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeTracker.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeTreeWalker.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/NodeUpdateData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/OverrideCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/QueryResult.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ReferenceNodeHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/ReferenceTracker.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/TrackedNodeHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/TrackedNodeModel.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/TreeData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/TreeUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/UnionCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/AbstractConfigurationNodeIterator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/ConfigurationAttributePointer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/ConfigurationNodeIteratorAttribute.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/ConfigurationNodeIteratorChildren.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/ConfigurationNodePointer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/ConfigurationNodePointerFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/XPathContextFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/XPathExpressionEngine.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/tree/xpath/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/AppletConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/BaseWebConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/JakartaServletConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/JakartaServletContextConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/JakartaServletFilterConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/JakartaServletRequestConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/ServletConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/ServletContextConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/ServletFilterConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/ServletRequestConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/configuration2/web/package-info.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/javacc/PropertyListParser.jj
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/resources/PropertyList-1.0.dtd
  B         application/xml-dtd    

  /src/main/resources/properties.dtd
  B         application/xml-dtd    

  /src/media/commons-logo-component-100.xcf
  B         image/x-xcf    

  /src/media/commons-logo-component.xcf
  B         image/x-xcf    

  /src/media/logo.png
  B         image/png    

  /src/site/resources/download_configuration.cgi
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

  /src/site/xdoc/building.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/dependencies.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/download_configuration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/issue-tracking.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/javadocarchive.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/mail-lists.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/security.xml
  S         application/xml    UTF-8
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_basicfeatures.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_beans.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_builders.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_combinedbuilder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_combinedconfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_compositeconfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_concurrency.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_events.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_filebased.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_hierarchical.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_multitenant.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_properties.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_reloading.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_utilities.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/howto_xml.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/overview.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/quick_start.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/upgradeto2_0.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/upgradeto2_x.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide/user_guide.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_basicfeatures.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_beans.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_combinedconfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_compositeconfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_configurationbuilder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_events.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_filebased.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_filesystems.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_multitenant.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_properties.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_utilities.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/howto_xml.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/overview.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/userguide_v1.10/user_guide.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/BaseNonStringProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/ConfigurationAssert.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/DatabaseConfigurationTestHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/EnumFixture.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/FileURLStreamHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/InterpolationTestHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/Logging.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/MockInitialContextFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/NonCloneableConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/NonStringTestHolder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/SynchronizerTestImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TempDirUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestAbstractConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestAbstractConfigurationBasicFeatures.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestAbstractConfigurationSynchronization.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestAbstractHierarchicalConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestBaseConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestBaseConfigurationXMLReader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestBaseHierarchicalConfigurationSynchronization.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestBaseNullConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestCatalogResolver.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestCombinedConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestCompositeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestCompositeConfigurationNonStringProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestConfigurationConverter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestConfigurationLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestConfigurationMap.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestConfigurationSet.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestConfigurationUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestDataConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestDatabaseConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestDefaultImmutableConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestDynamicCombinedConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestEnvironmentConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestEqualBehavior.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestEqualsProperty.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestHierarchicalConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestHierarchicalConfigurationXMLReader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestHierarchicalXMLConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestINIConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestImmutableConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestJNDIConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestJNDIEnvironmentValues.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestJSONConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestMapConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestNonStringProperties.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestNullCompositeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestNullJNDIEnvironmentValues.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestPatternSubtreeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestPatternSubtreeConfigurationWrapper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestPropertiesConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestPropertiesConfigurationLayout.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestPropertiesSequence.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestStrictConfigurationComparator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestSubnodeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestSubsetConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestSubsetConfiguration848.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestSystemConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestThreesomeConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestXMLConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestXMLConfiguration605.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestXMLDocumentHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestXMLListHandling.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestXMLPropertiesConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/TestYAMLConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/BeanCreationTestBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/BeanCreationTestBeanWithListChild.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/BeanCreationTestCtorBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/BeanDeclarationTestImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestBeanHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestCombinedBeanDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestConfigurationDynaBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestConfigurationDynaBeanXMLConfig.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestConstructorArg.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestDefaultBeanFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/beanutils/TestXMLBeanDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/BuilderEventListenerImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/ParametersBeanTestImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestAutoSaveListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestBasicBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestBasicConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestBasicConfigurationBuilderEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestBuilderConfigurationWrapperFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestCopyObjectDefaultHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestDatabaseBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestDefaultParametersManager.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestDefaultReloadingDetectorFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestEventListenerParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestFileBasedBuilderParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestFileBasedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestHierarchicalBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestJndiBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestPropertiesBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestReloadingBuilderSupportListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestReloadingFileBasedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/TestXMLBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/AbstractMultiFileConfigurationBuilderTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestBaseConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestCombinedBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestCombinedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestCombinedConfigurationBuilderVFS.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestConfigurationDeclaration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestFileExtensionConfigurationBuilderProvider.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestMultiFileBuilderParametersImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestMultiFileConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestMultiWrapDynaBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestReloadingCombinedConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestReloadingCombinedConfigurationBuilderFileBased.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/combined/TestReloadingMultiFileConfigurationBuilder.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/fluent/TestConfigurations.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/builder/fluent/TestParameters.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/convert/MyNumber.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/convert/TestDefaultConversionHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/convert/TestDefaultListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/convert/TestDisabledListDelimiterHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/convert/TestPropertyConverter.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/AbstractEventListenerTestImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/AbstractTestConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/ErrorListenerTestImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/EventListenerTestImpl.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestConfigurationEventTypes.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestDatabaseConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestEvent.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestEventListenerList.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestEventSource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestEventType.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestHierarchicalConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestMapConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestPropertiesConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestSubsetConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/event/TestXMLConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestConfigurationInterpolator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestConstantLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestDummyLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestEnvironmentLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestExprLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestInterpolatorSpecification.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/interpol/TestSystemPropertiesLookup.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestAbsoluteNameLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestBasePathLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestClasspathLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestCombinedLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestConfigurationLogger.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestDefaultFileSystem.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestFileHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestFileLocator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestFileLocatorUtils.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestFileSystemLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestHomeDirectoryLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/io/TestProvidedURLLocationStrategy.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/plist/AbstractTestPListEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/plist/TestPropertyListConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/plist/TestPropertyListConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/plist/TestPropertyListParser.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/plist/TestXMLPropertyListConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/plist/TestXMLPropertyListConfigurationEvents.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/AlwaysReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/RandomReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/TestCombinedReloadingController.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/TestFileHandlerReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/TestManagedReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/TestPeriodicReloadingTrigger.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/TestReloadingController.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/reloading/TestVFSFileHandlerReloadingDetector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/spring/TestConfigurationPropertiesFactoryBean.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/spring/TestConfigurationPropertySource.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/sync/TestReadWriteSynchronizer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/test/HsqlDB.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/AbstractCombinerTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/AbstractImmutableNodeHandlerTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/NodeStructureHelper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestDefaultConfigurationKey.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestDefaultExpressionEngine.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestDefaultExpressionEngineSymbols.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestImmutableNode.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestInMemoryNodeModel.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestInMemoryNodeModelReferences.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestInMemoryNodeModelTrackedNodes.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestMergeCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestNodeAddData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestNodeHandlerDecorator.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestNodeNameMatchers.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestNodeSelector.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestNodeTreeWalker.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestNodeUpdateData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestOverrideCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestQueryResult.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestTrackedNodeHandler.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestTrackedNodeModel.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestTreeData.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/TestUnionCombiner.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/AbstractXPathTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestConfigurationAttributePointer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestConfigurationIteratorAttributes.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestConfigurationNodeIteratorChildren.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestConfigurationNodePointer.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestConfigurationNodePointerFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestXPathContextFactory.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestXPathExpressionEngine.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/tree/xpath/TestXPathExpressionEngineInConfig.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestAppletConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestJakartaServletConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestJakartaServletContextConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestJakartaServletFilterConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestJakartaServletRequestConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestServletConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestServletContextConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestServletFilterConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/configuration2/web/TestServletRequestConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/01/testMultiConfiguration_1001.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/catalog.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/catalog2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/deep/deepinclude.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/deep/deeptest.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/deep/deeptestinvalid.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/deep/test.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/deep/testEqualDeep.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/deep/testFileFromClasspath.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/test.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/config/testMultiInclude.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/configA.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/configB.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/dataset.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-cyclical-back-to-root.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-cyclical-reference.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-cyclical-root.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-cyclical-step.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-include-cyclical-reference.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-include-not-found.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-interpol.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-load-exception.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include-not-found.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/include.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/includeoptional-target.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/includeoptional.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/jndi.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/jup-test.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/log4j-test.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/org/apache/commons/configuration2/test.jar
  A         application/java-archive    

  /src/test/resources/resolver.dtd
  B         application/xml-dtd    

  /src/test/resources/sample.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/sample.xsd
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/sample_1001.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/test-configuration-848.json
  B         application/json    

  /src/test/resources/test.ini
  S         text/x-ini    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/test.json
  B         application/json    

  /src/test/resources/test.plist
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/test.plist.xml
  B         application/x-plist    

  /src/test/resources/test.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/test.properties.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/test.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

! /src/test/resources/test.yaml
  S         text/x-yaml    ISO-8859-1
    ?????    ?????         Unknown license (Unapproved)

  /src/test/resources/test2.plist.xml
  B         application/x-plist    

  /src/test/resources/test2.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCCombinedChildBuilder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCCustomProvider.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCEntityResolver.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCEnvProperties.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCFileSystem.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCFileSystemSubConfig.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCLookup.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCMultiTenent.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCMultiTenentReloading.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCReloading.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCReloadingNested.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCResultClass.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCResultInitialization.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testCCSystemProperties.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testChildNamespace.xml
  S         application/xml    UTF-16BE
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testClasspath.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testComplexInitialization.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testConfigurationFactoryBean.file
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testConfigurationInterpolatorUpdate.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testConfigurationProvider.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testConfigurationXMLDocument.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterBadXML.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfiguration2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfiguration3.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationBasePath.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationInclude1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationInclude2.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationNamespaceAware.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationOverwrite.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationReverseOrder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationSysProps.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterConfigurationWithProps.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterCreateObject.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterOptionalConfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDigesterOptionalConfigurationEx.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDtd.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testDtdPublic.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testEncoding.xml
  S         application/xml    UTF-16BE
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testEqual.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testEqualDigester.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testExpression.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testExtendedClass.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testExtendedXMLConfigurationProvider.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testFactoryPropertiesInclude.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testFileReloadConfigurationBuilder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testFileReloadConfigurationBuilder2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testFileSystem.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testGlobalLookup.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testHierarchicalXMLConfiguration.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testHierarchicalXMLConfiguration2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testInterpolation.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testInterpolation.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testInterpolationBuilder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration.xsd
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_1001.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_1002.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_1003.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_1004.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_2001.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_2002.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_3001.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_3002.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiConfiguration_default.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiDynamic_default.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiDynamic_default2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiTenentConfigurationBuilder.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiTenentConfigurationBuilder2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiTenentConfigurationBuilder3.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiTenentConfigurationBuilder4.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testMultiTenentConfigurationBuilder5.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testPatternSubtreeConfig.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testResolver.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testRootNamespace.xml
  S         application/xml    UTF-16BE
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testSequence.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testSequenceDigester.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testSystemProperties.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testVFSMultiTenentConfigurationBuilder1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testVFSMultiTenentConfigurationBuilder2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testValidateInvalid.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testValidateValid.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testValidation.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testValidation2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testValidation3.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/test_invalid_date.plist.xml
  B         application/x-plist    

  /src/test/resources/testcombine1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testcombine2.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/testdb.script
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/resources/threesome.properties
  S         text/x-java-properties    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /target
  I         application/octet-stream     (directory)
```

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/japicmp.html -->

<!-- page_index: 16 -->

# Apache Commons Configuration

Comparing source compatibility of commons-configuration2-2.14.0.jar against commons-configuration2-2.13.0.jar

|  |  |
| --- | --- |
| Old: | commons-configuration2-2.13.0.jar |
| New: | commons-configuration2-2.14.0.jar |
| Created: | 2026-04-08T14:57:33.037+0000 |
| Access modifier filter: | PROTECTED |
| Only modifications: | true |
| Only binary incompatible modifications: | false |
| Ignore missing classes: | false |
| Includes: | all |
| Excludes: | n.a. |
| Semantic Versioning: | 0.0.1 |

- [Classes](#japicmp--toc)

Classes:

| Status | Fully Qualified Name |
| --- | --- |
| MODIFIED | [org.apache.commons.configuration2.ex.ConfigurationException](#japicmp--org.apache.commons.configuration2.ex.configurationexception) |
| MODIFIED | [org.apache.commons.configuration2.ex.ConfigurationRuntimeException](#japicmp--org.apache.commons.configuration2.ex.configurationruntimeexception) |
| MODIFIED | [org.apache.commons.configuration2.ex.ConversionException](#japicmp--org.apache.commons.configuration2.ex.conversionexception) |
| MODIFIED | [org.apache.commons.configuration2.io.AbsoluteNameLocationStrategy](#japicmp--org.apache.commons.configuration2.io.absolutenamelocationstrategy) |
| MODIFIED | [org.apache.commons.configuration2.io.BasePathLocationStrategy](#japicmp--org.apache.commons.configuration2.io.basepathlocationstrategy) |
| MODIFIED | [org.apache.commons.configuration2.io.ClasspathLocationStrategy](#japicmp--org.apache.commons.configuration2.io.classpathlocationstrategy) |
| MODIFIED | [org.apache.commons.configuration2.io.FileSystemLocationStrategy](#japicmp--org.apache.commons.configuration2.io.filesystemlocationstrategy) |
| MODIFIED | [org.apache.commons.configuration2.io.ProvidedURLLocationStrategy](#japicmp--org.apache.commons.configuration2.io.providedurllocationstrategy) |
| MODIFIED | [org.apache.commons.configuration2.XMLConfiguration](#japicmp--org.apache.commons.configuration2.xmlconfiguration) |

Binary incompatible changes are marked with (!) while source incompatible changes are marked with (\*).

MODIFIED
 (Serializable compatible)
public
class
org.apache.commons.configuration2.ex.ConfigurationException
[top](#japicmp--toc)

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| UNCHANGED | java.lang.Exception | n.a. |

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | true | -4498675951590519872 | -1316746661346991484 |
| New | true | 2086081643894861116 | -1316746661346991484 |

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
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>ConfigurationException(<span>java.lang.String</span>, <span>java.lang.Object[]</span>)</td>
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
			n.a.
		</td>
<td>
			53
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>ConfigurationException(<span>java.lang.Throwable</span>, <span>java.lang.String</span>, <span>java.lang.Object[]</span>)</td>
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
			n.a.
		</td>
<td>
			86
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED
 (Serializable compatible)
public
class
org.apache.commons.configuration2.ex.ConfigurationRuntimeException
[top](#japicmp--toc)

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| UNCHANGED | java.lang.RuntimeException | n.a. |

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | true | 1405507988484275987 | -7838702245512140996 |
| New | true | -8205051164801704468 | -7838702245512140996 |

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
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>ConfigurationRuntimeException(<span>java.lang.Throwable</span>, <span>java.lang.String</span>, <span>java.lang.Object[]</span>)</td>
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
			n.a.
		</td>
<td>
			87
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>

MODIFIED
 (Serializable compatible)
public
class
org.apache.commons.configuration2.ex.ConversionException
[top](#japicmp--toc)

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| UNCHANGED | org.apache.commons.configuration2.ex.ConfigurationRuntimeException | n.a. |

|  | Serializable | default serialVersionUID | serialVersionUID in class |
| --- | --- | --- | --- |
| Old | true | 6866920758663532082 | -5167943099293540392 |
| New | true | 3330588849646595113 | -5167943099293540392 |

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
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>ConversionException(<span>java.lang.Throwable</span>, <span>java.lang.String</span>, <span>java.lang.Object[]</span>)</td>
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
			n.a.
		</td>
<td>
			87
		</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span>NEW</span></td>
<td><span>public</span>
</td>
<td>n.a.</td>
<td>ConversionException(<span>java.lang.String</span>, <span>java.lang.Object[]</span>)</td>
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
			n.a.
		</td>
<td>
			55
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
org.apache.commons.configuration2.io.AbsoluteNameLocationStrategy
[top](#japicmp--toc)

MODIFIED
public
class
org.apache.commons.configuration2.io.BasePathLocationStrategy
[top](#japicmp--toc)

MODIFIED
public
class
org.apache.commons.configuration2.io.ClasspathLocationStrategy
[top](#japicmp--toc)

MODIFIED
public
class
org.apache.commons.configuration2.io.FileSystemLocationStrategy
[top](#japicmp--toc)

MODIFIED
public
class
org.apache.commons.configuration2.io.ProvidedURLLocationStrategy
[top](#japicmp--toc)

MODIFIED
public
class
org.apache.commons.configuration2.XMLConfiguration
[top](#japicmp--toc)

Superclass:

| Status | Superclass | Compatibility Changes |
| --- | --- | --- |
| UNCHANGED | org.apache.commons.configuration2.BaseHierarchicalConfiguration | n.a. |

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
<td><span>public</span>
</td>
<td>n.a.</td>
<td><span>void</span></td>
<td>read(<span>org.w3c.dom.Element</span>)</td>
<td><table>
<thead>
<tr>
<td>Status:</td>
<td>Name:</td>
</tr>
</thead>
<tbody>
<tr>
<td><span>NEW</span></td>
<td>org.apache.commons.configuration2.ex.ConfigurationException</td>
</tr>
</tbody>
</table>
</td>
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
			953
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

<!-- source_url: https://commons.apache.org/proper/commons-configuration/checkstyle.html -->

<!-- page_index: 17 -->

<a id="checkstyle--checkstyle-results"></a>

# Checkstyle Results

The following document contains the results of [Checkstyle](https://checkstyle.org/) 13.2.0 with /Users/garygregory/git/commons/commons-configuration/src/conf/checkstyle.xml ruleset.

<a id="checkstyle--summary"></a>

## Summary

| Files | Info | Warnings | Errors |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |

<a id="checkstyle--files"></a>

## Files

| File | I | W | E |
| --- | --- | --- | --- |

<a id="checkstyle--details"></a>

## Details

---

<a id="spotbugs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-configuration/spotbugs.html -->

<!-- page_index: 18 -->

<a id="spotbugs--spotbugs-bug-detector-report"></a>

# SpotBugs Bug Detector Report

The following document contains the results of [SpotBugs](https://spotbugs.github.io/)

SpotBugs Version is *4.9.8*

Threshold is

Effort is *default*

<a id="spotbugs--summary"></a>

# Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 392 | 0 | 0 | 0 |

<a id="spotbugs--files"></a>

# Files

| Class | Bugs |
| --- | --- |

---
